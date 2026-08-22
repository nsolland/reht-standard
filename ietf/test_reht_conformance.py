from dataclasses import replace

import pytest

from reht_reference_impl import (
    Action,
    AgentTrace,
    AuthorityRegistry,
    AuthorityState,
    EvidenceRecord,
    NonceRegistry,
    PolicyEnforcementPoint,
    RACSDecision,
    REHTNode,
    canonical_digest,
)


@pytest.fixture()
def action():
    return Action(
        action_id="a-1",
        actor_ref="agent-1",
        capability="payments.create",
        target="merchant-1",
        payload={"amount": "12.00", "currency": "EUR"},
        purpose_ref="purchase",
    )


@pytest.fixture()
def authority():
    return AuthorityState(
        authority_ref="auth-1",
        principal_ref="agent-1",
        capabilities=frozenset({"payments.create"}),
        targets=frozenset({"merchant-1"}),
        purpose_refs=frozenset({"purchase"}),
    )


@pytest.fixture()
def system(authority):
    registry = AuthorityRegistry()
    registry.put(authority)
    nonces = NonceRegistry()
    reht = REHTNode(registry, nonces)
    pep = PolicyEnforcementPoint(reht)
    return registry, nonces, reht, pep


def prepare(reht, action, nonce="nonce-0000000001"):
    return reht.prepare(action, "auth-1", nonce, "verify-1")


def test_canonical_racs_vocabulary_exact():
    assert {v.value for v in RACSDecision} == {
        "ALLOW", "MODIFY", "DEFER", "DENY", "STEP_UP", "HALT"
    }


def test_action_digest_is_deterministic(action):
    assert action.digest == action.digest


def test_canonical_digest_ignores_dict_key_order():
    assert canonical_digest({"a": 1, "b": 2}) == canonical_digest({"b": 2, "a": 1})


def test_prepare_accepts_current_exact_authority(system, action):
    _, _, reht, _ = system
    prepared = prepare(reht, action)
    assert prepared.action_digest == action.digest


def test_prepare_rejects_unknown_authority(system, action):
    _, _, reht, _ = system
    with pytest.raises(ValueError):
        reht.prepare(action, "missing", "nonce-x", "verify-x")


def test_prepare_rejects_wrong_actor(system, action):
    _, _, reht, _ = system
    wrong = replace(action, actor_ref="agent-2")
    with pytest.raises(PermissionError):
        prepare(reht, wrong)


def test_prepare_rejects_wrong_capability(system, action):
    _, _, reht, _ = system
    wrong = replace(action, capability="payments.refund")
    with pytest.raises(PermissionError):
        prepare(reht, wrong)


def test_prepare_rejects_wrong_target(system, action):
    _, _, reht, _ = system
    wrong = replace(action, target="merchant-2")
    with pytest.raises(PermissionError):
        prepare(reht, wrong)


def test_prepare_rejects_wrong_purpose(system, action):
    _, _, reht, _ = system
    wrong = replace(action, purpose_ref="other")
    with pytest.raises(PermissionError):
        prepare(reht, wrong)


def test_commit_allows_unchanged_current_authority(system, action):
    _, _, reht, _ = system
    prepared = prepare(reht, action)
    result = reht.commit_time_verify(prepared, action)
    assert result.authorized is True
    assert result.reason_codes == ()


def test_action_drift_fails_closed(system, action):
    _, _, reht, _ = system
    prepared = prepare(reht, action)
    changed = replace(action, payload={"amount": "99.00", "currency": "EUR"})
    result = reht.commit_time_verify(prepared, changed)
    assert result.authorized is False
    assert result.reason_codes == ("ACTION_DRIFT",)


def test_revocation_between_prepare_and_commit_halts(system, action):
    registry, _, reht, _ = system
    prepared = prepare(reht, action)
    registry.revoke("auth-1")
    verification = reht.commit_time_verify(prepared, action)
    binding = reht.bind_racs(verification)
    assert verification.authorized is False
    assert "AUTHORITY_REVOKED" in verification.reason_codes
    assert binding.decision is RACSDecision.HALT


def test_authority_epoch_drift_fails_closed(system, action, authority):
    registry, _, reht, _ = system
    prepared = prepare(reht, action)
    registry.put(replace(authority, epoch=2))
    result = reht.commit_time_verify(prepared, action)
    assert result.authorized is False
    assert result.reason_codes == ("AUTHORITY_DRIFT",)


def test_authority_scope_drift_fails_closed(system, action, authority):
    registry, _, reht, _ = system
    prepared = prepare(reht, action)
    registry.put(
        replace(authority, epoch=2, targets=frozenset({"merchant-2"}))
    )
    result = reht.commit_time_verify(prepared, action)
    assert result.authorized is False
    assert result.reason_codes == ("AUTHORITY_SCOPE_MISMATCH",)


def test_missing_authority_at_commit_steps_up(system, action):
    registry, _, reht, _ = system
    prepared = prepare(reht, action)
    registry._states.pop("auth-1")
    verification = reht.commit_time_verify(prepared, action)
    binding = reht.bind_racs(verification)
    assert verification.authorized is False
    assert binding.decision is RACSDecision.STEP_UP


def test_replay_fails_closed(system, action):
    _, nonces, reht, _ = system
    prepared = prepare(reht, action)
    nonces.consume(prepared.nonce)
    verification = reht.commit_time_verify(prepared, action)
    assert verification.authorized is False
    assert verification.reason_codes == ("REPLAY",)


def test_nonce_registry_rejects_double_consume():
    registry = NonceRegistry()
    registry.consume("n")
    with pytest.raises(ValueError):
        registry.consume("n")


def test_pep_executes_only_after_fresh_reht_check(system, action):
    _, _, reht, pep = system
    prepared = prepare(reht, action)
    called = []
    binding, effect_ref = pep.execute(
        prepared, action, lambda a: called.append(a.action_id) or "effect-1"
    )
    assert binding.decision is RACSDecision.ALLOW
    assert effect_ref == "effect-1"
    assert called == ["a-1"]


def test_pep_does_not_execute_after_revocation(system, action):
    registry, _, reht, pep = system
    prepared = prepare(reht, action)
    registry.revoke("auth-1")
    called = []
    binding, effect_ref = pep.execute(
        prepared, action, lambda a: called.append(a.action_id) or "effect-1"
    )
    assert binding.decision is RACSDecision.HALT
    assert effect_ref is None
    assert called == []


def test_pep_does_not_execute_modified_action_under_old_binding(system, action):
    _, _, reht, pep = system
    prepared = prepare(reht, action)
    modified = replace(action, target="merchant-2")
    binding, effect_ref = pep.execute(prepared, modified, lambda _: "effect-1")
    assert binding.decision is RACSDecision.DENY
    assert effect_ref is None


def test_successful_effect_consumes_nonce(system, action):
    _, nonces, reht, pep = system
    prepared = prepare(reht, action)
    pep.execute(prepared, action, lambda _: "effect-1")
    assert nonces.is_consumed(prepared.nonce)


def test_second_execution_is_blocked_as_replay(system, action):
    _, _, reht, pep = system
    prepared = prepare(reht, action)
    first, first_effect = pep.execute(prepared, action, lambda _: "effect-1")
    second, second_effect = pep.execute(prepared, action, lambda _: "effect-2")
    assert first.decision is RACSDecision.ALLOW
    assert first_effect == "effect-1"
    assert second.decision is RACSDecision.DENY
    assert second_effect is None


def test_racs_never_expands_failed_reht_result(system, action):
    _, _, reht, _ = system
    prepared = prepare(reht, action)
    changed = replace(action, payload={"amount": "999.00"})
    verification = reht.commit_time_verify(prepared, changed)
    binding = reht.bind_racs(verification)
    assert binding.decision is not RACSDecision.ALLOW


def test_agent_trace_signature_does_not_create_authority():
    trace = AgentTrace(
        trace_id="trace-1",
        action_id="a-1",
        claims={"authorized": True},
        trace_signature="signed-by-agent",
    )
    assert trace.claims["authorized"] is True
    assert not isinstance(trace, AuthorityState)


def test_evidence_uses_issuer_local_sequence_not_global_order(system, action):
    _, _, reht, _ = system
    prepared = prepare(reht, action)
    binding = reht.bind_racs(reht.commit_time_verify(prepared, action))
    first = reht.evidence("e-1", "issuer-a", binding)
    second = reht.evidence("e-2", "issuer-a", binding, parent_hash=first.digest)
    assert first.issuer_sequence == 1
    assert second.issuer_sequence == 2
    assert second.parent_hash == first.digest


def test_evidence_digest_is_integrity_sensitive(system, action):
    _, _, reht, _ = system
    prepared = prepare(reht, action)
    binding = reht.bind_racs(reht.commit_time_verify(prepared, action))
    record = reht.evidence("e-1", "issuer-a", binding)
    changed = EvidenceRecord(
        record_id=record.record_id,
        issuer=record.issuer,
        issuer_sequence=record.issuer_sequence,
        parent_hash=record.parent_hash,
        verification_id=record.verification_id,
        action_digest=record.action_digest,
        decision=record.decision,
        effect_ref="different",
    )
    assert record.digest != changed.digest


def test_authority_epoch_cannot_move_backwards(system, authority):
    registry, _, _, _ = system
    registry.put(replace(authority, epoch=2))
    with pytest.raises(ValueError):
        registry.put(replace(authority, epoch=1))


def test_racs_modify_is_non_executable_without_fresh_reht(system):
    _, _, _, pep = system
    assert RACSDecision.MODIFY not in pep.EXECUTABLE


def test_racs_defer_is_non_executable(system):
    _, _, _, pep = system
    assert RACSDecision.DEFER not in pep.EXECUTABLE


def test_racs_step_up_is_non_executable(system):
    _, _, _, pep = system
    assert RACSDecision.STEP_UP not in pep.EXECUTABLE


def test_racs_halt_is_non_executable(system):
    _, _, _, pep = system
    assert RACSDecision.HALT not in pep.EXECUTABLE
