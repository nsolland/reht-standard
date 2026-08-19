from composition_closure import CompositionClosure, CompositionRule, GovernedEffect


def closure():
    return CompositionClosure(
        rules=(
            CompositionRule("read-then-send", ("data.read_sensitive", "external.send")),
            CompositionRule(
                "read-transform-send",
                ("data.read_sensitive", "data.transform", "external.send"),
            ),
        )
    )


def test_individually_allowed_action_can_fail_by_composition():
    c = closure()
    c.record_effect(GovernedEffect("case-1", "data.read_sensitive", "a-1"))
    assert c.admissible("case-1", "external.send") is False
    assert c.reason_codes("case-1", "external.send") == (
        "COMPOSITION_CLOSURE:read-then-send",
    )


def test_k_tuple_composition_is_enforced():
    c = closure()
    c.record_effect(GovernedEffect("case-1", "data.read_sensitive", "a-1"))
    c.record_effect(GovernedEffect("case-1", "data.transform", "a-2"))
    assert c.admissible("case-1", "external.send") is False
    assert "COMPOSITION_CLOSURE:read-transform-send" in c.reason_codes(
        "case-1", "external.send"
    )


def test_unrelated_sequence_remains_admissible():
    c = closure()
    c.record_effect(GovernedEffect("case-1", "inventory.read", "a-1"))
    assert c.admissible("case-1", "external.send") is True


def test_new_agent_session_does_not_reset_governed_history():
    c = closure()
    c.record_effect(GovernedEffect("principal-purpose-7", "data.read_sensitive", "s1-a1"))
    # A new model/agent session uses the same governed continuity scope.
    assert c.admissible("principal-purpose-7", "external.send") is False


def test_different_governed_scope_does_not_inherit_history():
    c = closure()
    c.record_effect(GovernedEffect("case-1", "data.read_sensitive", "a-1"))
    assert c.admissible("case-2", "external.send") is True


def test_rules_require_composition_not_single_action():
    try:
        CompositionRule("invalid", ("external.send",))
    except ValueError as exc:
        assert "at least two" in str(exc)
    else:
        raise AssertionError("single-action composition rule must be rejected")
