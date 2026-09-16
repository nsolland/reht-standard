from __future__ import annotations

import json
from pathlib import Path


PROFILE = Path(__file__).with_name("grant-lineage-revocation-v0.1.json")
INVARIANT = (
    "same permissions + different grant lineage + same revocation → opposite decision"
)
REQUIRED_REQUIREMENTS = {
    "exact_grant_lineage_resolved_at_consequence_time",
    "current_revocation_applied_to_each_lineage",
    "revoked_ancestor_grant_is_non_executable",
    "unaffected_independent_lineage_is_not_denied_by_association",
    "flattened_permission_projection_does_not_determine_authorization",
}


def validate() -> None:
    payload = json.loads(PROFILE.read_text(encoding="utf-8"))

    assert payload["profile"] == "reht.grant-lineage-sensitive-revocation"
    assert payload["version"] == "0.1.0-draft.1"
    assert payload["target_specification"] == "0.6.0-draft.1"
    assert payload["invariant"] == INVARIANT
    assert set(payload["requirements"]) == REQUIRED_REQUIREMENTS

    pairs = payload["paired_cases"]
    assert len(pairs) == 1, "the profile must contain the required paired case"
    pair = pairs[0]
    assert pair["id"] == "GLR-PAIR-001"

    shared = pair["shared"]
    action = shared["action"]
    permission_projection = shared["permission_projection"]
    revocation_state = shared["revocation_state"]
    revoked_grant_ref = revocation_state["revoked_grant_ref"]
    assert permission_projection["capabilities"]
    assert revoked_grant_ref
    assert action["actor_ref"] == permission_projection["principal_ref"]
    assert action["capability"] in permission_projection["capabilities"]
    assert action["target"] in permission_projection["targets"]
    assert action["purpose_ref"] in permission_projection["purpose_refs"]

    cases = pair["cases"]
    assert len(cases) == 2
    assert len({case["id"] for case in cases}) == 2
    assert {case["action_ref"] for case in cases} == {"shared.action"}
    assert {
        case["permission_projection_ref"] for case in cases
    } == {"shared.permission_projection"}
    assert {
        case["revocation_state_ref"] for case in cases
    } == {"shared.revocation_state"}

    lineages = [tuple(case["grant_lineage"]) for case in cases]
    assert lineages[0] != lineages[1], "the paired cases require different lineages"

    by_expected = {case["expected"]: case for case in cases}
    assert set(by_expected) == {
        "NON_EXECUTABLE",
        "MAY_CONTINUE_REHT_EVALUATION",
    }
    assert {
        case["expected_authorized"] for case in cases
    } == {False, True}, "the paired cases require opposite authorization decisions"
    assert by_expected["NON_EXECUTABLE"]["expected_authorized"] is False
    assert (
        by_expected["MAY_CONTINUE_REHT_EVALUATION"]["expected_authorized"] is True
    )

    blocked_lineage = set(by_expected["NON_EXECUTABLE"]["grant_lineage"])
    unaffected_lineage = set(
        by_expected["MAY_CONTINUE_REHT_EVALUATION"]["grant_lineage"]
    )
    assert revoked_grant_ref in blocked_lineage
    assert revoked_grant_ref not in unaffected_lineage


if __name__ == "__main__":
    validate()
    print("grant-lineage-sensitive revocation conformance: PASS")
