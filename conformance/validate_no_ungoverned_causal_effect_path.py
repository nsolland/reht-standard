from __future__ import annotations

import json
from pathlib import Path


PROFILE = Path(__file__).with_name("causal-execution-v0.7.json")
REQUIRED_BOUNDARY_PROPERTIES = {
    "explicit_declared",
    "exact_effect_bound",
    "authorized_now",
    "deny_enforceable_before_commit",
    "fail_closed",
    "evidence_capable",
}
REQUIRED_ADDITIONAL_CHANNELS = {
    "DYNAMIC_REFERENCE",
    "TELEMETRY_TRIGGER",
    "FALLBACK_ROUTE",
    "IMPLICIT_INFLUENCE",
}
REQUIRED_NEGATIVE_CASES = {
    "NUGCEP-NEG-BOUNDARY-EXPLICIT-001",
    "NUGCEP-NEG-BOUNDARY-BINDING-001",
    "NUGCEP-NEG-BOUNDARY-AUTH-001",
    "NUGCEP-NEG-BOUNDARY-ENFORCEMENT-001",
    "NUGCEP-NEG-BOUNDARY-FAILCLOSED-001",
    "NUGCEP-NEG-BOUNDARY-EVIDENCE-001",
    "NUGCEP-NEG-DYNAMIC-001",
    "NUGCEP-NEG-TELEMETRY-001",
    "NUGCEP-NEG-FALLBACK-001",
    "NUGCEP-NEG-IMPLICIT-001",
    "NUGCEP-NEG-DEPLOYMENT-COVERAGE-001",
}


def validate() -> None:
    payload = json.loads(PROFILE.read_text(encoding="utf-8"))
    assert payload["version"] == "0.7.0-draft.1"
    assert payload["extends"] == "conformance/causal-execution-v0.6.json"
    assert payload["formal_invariant"] == "NO_UNGOVERNED_CAUSAL_EFFECT_PATH"
    assert payload["compatibility_invariant"] == "NO_DIRECT_EFFECT_PATH"

    assert set(payload["governed_boundary_required_properties"]) == REQUIRED_BOUNDARY_PROPERTIES
    assert set(payload["additional_channel_classes"]) == REQUIRED_ADDITIONAL_CHANNELS

    deployment = payload["deployment_claim"]
    assert deployment["scope"] == "BOUNDED_DECLARED_REACHABILITY"
    assert deployment["requires_reachable_path_inventory"] is True
    assert deployment["requires_enforcement_evidence"] is True
    assert deployment["unknown_path_disposition"] == "NON_EXECUTABLE"
    assert deployment["global_absence_inferred_from_design"] is False

    cases = payload["cases"]
    ids = [case["id"] for case in cases]
    assert len(ids) == len(set(ids)), "conformance case IDs must be unique"
    by_id = {case["id"]: case for case in cases}
    missing = REQUIRED_NEGATIVE_CASES - by_id.keys()
    assert not missing, f"missing required cases: {sorted(missing)}"

    for case_id in REQUIRED_NEGATIVE_CASES - {"NUGCEP-NEG-DEPLOYMENT-COVERAGE-001"}:
        assert by_id[case_id]["expected"] == "NON_EXECUTABLE"
    assert by_id["NUGCEP-NEG-DEPLOYMENT-COVERAGE-001"]["expected"] == "NON_CONFORMANT_DEPLOYMENT"
    assert by_id["NUGCEP-POS-BOUNDARY-001"]["expected"] == "MAY_CONTINUE_REHT_EVALUATION"


if __name__ == "__main__":
    validate()
    print("NO_UNGOVERNED_CAUSAL_EFFECT_PATH conformance v0.7: PASS")
