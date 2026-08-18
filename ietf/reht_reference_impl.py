from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Callable


def canonical_digest(value: object) -> str:
    payload = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


class RACSDecision(str, Enum):
    ALLOW = "ALLOW"
    MODIFY = "MODIFY"
    DEFER = "DEFER"
    DENY = "DENY"
    STEP_UP = "STEP_UP"
    HALT = "HALT"


@dataclass(frozen=True)
class Action:
    action_id: str
    actor_ref: str
    capability: str
    target: str
    payload: dict
    purpose_ref: str | None = None

    @property
    def digest(self) -> str:
        return canonical_digest(asdict(self))


@dataclass(frozen=True)
class AuthorityState:
    authority_ref: str
    principal_ref: str
    capabilities: frozenset[str]
    targets: frozenset[str]
    active: bool = True
    revoked: bool = False
    epoch: int = 1
    purpose_refs: frozenset[str] = field(default_factory=frozenset)

    def permits(self, action: Action) -> bool:
        if not self.active or self.revoked:
            return False
        if action.actor_ref != self.principal_ref:
            return False
        if action.capability not in self.capabilities:
            return False
        if action.target not in self.targets:
            return False
        if self.purpose_refs and action.purpose_ref not in self.purpose_refs:
            return False
        return True

    @property
    def digest(self) -> str:
        return canonical_digest(
            {
                "authority_ref": self.authority_ref,
                "principal_ref": self.principal_ref,
                "capabilities": sorted(self.capabilities),
                "targets": sorted(self.targets),
                "active": self.active,
                "revoked": self.revoked,
                "epoch": self.epoch,
                "purpose_refs": sorted(self.purpose_refs),
            }
        )


class AuthorityRegistry:
    """Authoritative state provider used by REHT at the consequence boundary."""

    def __init__(self) -> None:
        self._states: dict[str, AuthorityState] = {}

    def put(self, state: AuthorityState) -> None:
        current = self._states.get(state.authority_ref)
        if current is not None and state.epoch < current.epoch:
            raise ValueError("authority epoch cannot move backwards")
        self._states[state.authority_ref] = state

    def get(self, authority_ref: str) -> AuthorityState | None:
        return self._states.get(authority_ref)

    def revoke(self, authority_ref: str) -> AuthorityState:
        current = self._states[authority_ref]
        revoked = AuthorityState(
            authority_ref=current.authority_ref,
            principal_ref=current.principal_ref,
            capabilities=current.capabilities,
            targets=current.targets,
            active=False,
            revoked=True,
            epoch=current.epoch + 1,
            purpose_refs=current.purpose_refs,
        )
        self._states[authority_ref] = revoked
        return revoked


class NonceRegistry:
    """Durable single-use registry for execution identities."""

    def __init__(self) -> None:
        self._consumed: set[str] = set()

    def is_consumed(self, nonce: str) -> bool:
        return nonce in self._consumed

    def consume(self, nonce: str) -> None:
        if nonce in self._consumed:
            raise ValueError("nonce replay")
        self._consumed.add(nonce)


@dataclass(frozen=True)
class PreparedAuthorization:
    verification_id: str
    action_digest: str
    authority_ref: str
    authority_epoch: int
    authority_state_digest: str
    nonce: str


@dataclass(frozen=True)
class CommitVerification:
    verification_id: str
    action_digest: str
    authority_ref: str
    authority_state_digest: str | None
    authorized: bool
    reason_codes: tuple[str, ...]
    nonce: str


@dataclass(frozen=True)
class RACSBinding:
    verification_id: str
    action_digest: str
    decision: RACSDecision
    reason_codes: tuple[str, ...] = ()


@dataclass(frozen=True)
class EvidenceRecord:
    record_id: str
    issuer: str
    issuer_sequence: int
    parent_hash: str | None
    verification_id: str
    action_digest: str
    decision: RACSDecision
    effect_ref: str | None = None

    @property
    def digest(self) -> str:
        return canonical_digest(
            {
                **asdict(self),
                "decision": self.decision.value,
            }
        )


@dataclass(frozen=True)
class AgentTrace:
    """An integrity-bindable agent claim. It is never authoritative state."""

    trace_id: str
    action_id: str
    claims: dict
    trace_signature: str | None = None


class REHTNode:
    """
    Reference execution-boundary verifier.

    REHT, not the PEP and not RACS, obtains current authoritative state and
    determines whether the exact candidate remains authorized at consequence.
    """

    def __init__(
        self,
        authority_registry: AuthorityRegistry,
        nonce_registry: NonceRegistry,
    ) -> None:
        self.authority_registry = authority_registry
        self.nonce_registry = nonce_registry
        self._sequence = 0

    def prepare(
        self,
        action: Action,
        authority_ref: str,
        nonce: str,
        verification_id: str,
    ) -> PreparedAuthorization:
        state = self.authority_registry.get(authority_ref)
        if state is None:
            raise ValueError("unknown authority")
        if not state.permits(action):
            raise PermissionError("action not currently within authority")
        if self.nonce_registry.is_consumed(nonce):
            raise ValueError("nonce already consumed")
        return PreparedAuthorization(
            verification_id=verification_id,
            action_digest=action.digest,
            authority_ref=authority_ref,
            authority_epoch=state.epoch,
            authority_state_digest=state.digest,
            nonce=nonce,
        )

    def commit_time_verify(
        self,
        prepared: PreparedAuthorization,
        action: Action,
    ) -> CommitVerification:
        if prepared.action_digest != action.digest:
            return CommitVerification(
                verification_id=prepared.verification_id,
                action_digest=action.digest,
                authority_ref=prepared.authority_ref,
                authority_state_digest=None,
                authorized=False,
                reason_codes=("ACTION_DRIFT",),
                nonce=prepared.nonce,
            )

        state = self.authority_registry.get(prepared.authority_ref)
        if state is None:
            return CommitVerification(
                prepared.verification_id,
                action.digest,
                prepared.authority_ref,
                None,
                False,
                ("AUTHORITY_UNAVAILABLE",),
                prepared.nonce,
            )

        if state.revoked or not state.active:
            return CommitVerification(
                prepared.verification_id,
                action.digest,
                prepared.authority_ref,
                state.digest,
                False,
                ("AUTHORITY_REVOKED",),
                prepared.nonce,
            )

        if not state.permits(action):
            return CommitVerification(
                prepared.verification_id,
                action.digest,
                prepared.authority_ref,
                state.digest,
                False,
                ("AUTHORITY_SCOPE_MISMATCH",),
                prepared.nonce,
            )

        if (
            state.epoch != prepared.authority_epoch
            or state.digest != prepared.authority_state_digest
        ):
            return CommitVerification(
                prepared.verification_id,
                action.digest,
                prepared.authority_ref,
                state.digest,
                False,
                ("AUTHORITY_DRIFT",),
                prepared.nonce,
            )

        if self.nonce_registry.is_consumed(prepared.nonce):
            return CommitVerification(
                prepared.verification_id,
                action.digest,
                prepared.authority_ref,
                state.digest,
                False,
                ("REPLAY",),
                prepared.nonce,
            )

        return CommitVerification(
            prepared.verification_id,
            action.digest,
            prepared.authority_ref,
            state.digest,
            True,
            (),
            prepared.nonce,
        )

    @staticmethod
    def bind_racs(verification: CommitVerification) -> RACSBinding:
        # RACS binds a REHT result deterministically; it never originates
        # authority and can never turn a failed REHT verification into ALLOW.
        if verification.authorized:
            decision = RACSDecision.ALLOW
        elif "AUTHORITY_REVOKED" in verification.reason_codes:
            decision = RACSDecision.HALT
        elif "AUTHORITY_UNAVAILABLE" in verification.reason_codes:
            decision = RACSDecision.STEP_UP
        else:
            decision = RACSDecision.DENY
        return RACSBinding(
            verification_id=verification.verification_id,
            action_digest=verification.action_digest,
            decision=decision,
            reason_codes=verification.reason_codes,
        )

    def evidence(
        self,
        record_id: str,
        issuer: str,
        binding: RACSBinding,
        parent_hash: str | None = None,
        effect_ref: str | None = None,
    ) -> EvidenceRecord:
        self._sequence += 1
        return EvidenceRecord(
            record_id=record_id,
            issuer=issuer,
            issuer_sequence=self._sequence,
            parent_hash=parent_hash,
            verification_id=binding.verification_id,
            action_digest=binding.action_digest,
            decision=binding.decision,
            effect_ref=effect_ref,
        )


class PolicyEnforcementPoint:
    """
    Consequence boundary.

    The PEP invokes REHT in the commit path and enforces its bound result. It
    does not independently decide whether organizational authority exists.
    """

    EXECUTABLE = frozenset({RACSDecision.ALLOW})

    def __init__(self, reht: REHTNode) -> None:
        self.reht = reht

    def execute(
        self,
        prepared: PreparedAuthorization,
        action: Action,
        effect: Callable[[Action], str],
    ) -> tuple[RACSBinding, str | None]:
        verification = self.reht.commit_time_verify(prepared, action)
        binding = self.reht.bind_racs(verification)

        if binding.decision not in self.EXECUTABLE:
            return binding, None

        # Consumption occurs inside the governed consequence path. A real
        # connector should make this durable before or atomically with effect.
        self.reht.nonce_registry.consume(prepared.nonce)
        effect_ref = effect(action)
        return binding, effect_ref


def demo() -> tuple[RACSBinding, str | None]:
    authorities = AuthorityRegistry()
    authorities.put(
        AuthorityState(
            authority_ref="auth-1",
            principal_ref="agent-1",
            capabilities=frozenset({"payments.create"}),
            targets=frozenset({"merchant-7"}),
            purpose_refs=frozenset({"purchase-approved"}),
        )
    )
    nonces = NonceRegistry()
    reht = REHTNode(authorities, nonces)
    pep = PolicyEnforcementPoint(reht)
    action = Action(
        action_id="pay-1",
        actor_ref="agent-1",
        capability="payments.create",
        target="merchant-7",
        payload={"amount": "10.00", "currency": "EUR"},
        purpose_ref="purchase-approved",
    )
    prepared = reht.prepare(action, "auth-1", "nonce-0000000001", "verify-1")
    return pep.execute(prepared, action, lambda _: "effect-1")


if __name__ == "__main__":
    decision, effect_ref = demo()
    print(decision.decision.value, effect_ref)
