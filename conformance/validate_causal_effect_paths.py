from __future__ import annotations

import json
from pathlib import Path


PROFILE = Path(__file__).with_name("causal-execution-v0.6.json")

REQUIRED_NEGATIVE_CASES = {
    "CEC-NEG-EFFECT-DIRECT-001",
    "CEC-NEG-EFFECT-HUMAN-001",
    "CEC-NEG-EFFECT-AGENT-001",
    "CEC-NEG-EFFECT-STATE-001",
    "CEC-NEG-EFFECT-MESSAGE-001",
    "CEC-NEG-EFFECT-CREDENTIAL-001",
    "CEC-NEG-EFFECT-RESOURCE-001",
    "CEC-NEG-EFFECT-SIDECHANNEL-001",
    "CEC-NEG-EFFECT-UNKNOWN-001",
}


def validate() -> None:
    payload = json.loads(PROFILE.read_text(encoding="utf-8"))
    assert payload["version"] == "0.6.0-draft.1"
    rule = payload["effect_boundary_rule"]
    assert rule["name"] == "NO_DIRECT_EFFECT_PATH"
    assert rule["scope"] == "all_causal_trust_boundary_crossings"
    assert rule["unknown_channel_disposition"] == "NON_EXECUTABLE"
    assert rule["unknown_boundary_disposition"] == "NON_EXECUTABLE"
    assert rule["payload_type_creates_exemption"] is False
    assert rule["internal_computation_requires_effect_authorization"] is False

    cases = payload["cases"]
    ids = [case["id"] for case in cases]
    assert len(ids) == len(set(ids)), "conformance case IDs must be unique"
    by_id = {case["id"]: case for case in cases}

    missing = REQUIRED_NEGATIVE_CASES - by_id.keys()
    assert not missing, f"missing causal effect-path negative cases: {sorted(missing)}"
    for case_id in REQUIRED_NEGATIVE_CASES:
        assert by_id[case_id]["expected"] == "NON_EXECUTABLE"

    assert by_id["CEC-POS-INTERNAL-001"]["expected"] == "MAY_CONTINUE_REHT_EVALUATION"
    assert by_id["CEC-POS-001"]["expected"] == "MAY_CONTINUE_REHT_EVALUATION"


if __name__ == "__main__":
    validate()
    print("causal-effect-path conformance: PASS")
