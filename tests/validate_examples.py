from __future__ import annotations

import copy
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]

CASES = [
    ("schemas/action-envelope.schema.json", "examples/admissible-action.json"),
    ("schemas/execution-receipt.schema.json", "examples/execution-receipt.json"),
    (
        "schemas/policy-context.schema.json",
        "examples/eu-ai-act-omnibus-policy-context.json",
    ),
    ("schemas/xaip-receipt-v1.schema.json", "examples/xaip-receipt-v1.json"),
    (
        "schemas/xaip-reht-binding-v1.schema.json",
        "examples/xaip-reht-binding-v1.json",
    ),
]


def load_json(path: str) -> dict:
    with (ROOT / path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_pair(schema_path: str, instance_path: str) -> None:
    schema = load_json(schema_path)
    instance = load_json(instance_path)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
    if errors:
        details = "\n".join(f"{instance_path}: {error.message}" for error in errors)
        raise SystemExit(details)
    print(f"validated {instance_path}")


def assert_invalid_xaip(name: str, mutate) -> None:
    schema = load_json("schemas/xaip-receipt-v1.schema.json")
    instance = load_json("examples/xaip-receipt-v1.json")
    candidate = copy.deepcopy(instance)
    mutate(candidate)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    if not list(validator.iter_errors(candidate)):
        raise SystemExit(f"XAIP negative case unexpectedly valid: {name}")
    print(f"rejected XAIP negative case {name}")


def main() -> None:
    for schema_path, instance_path in CASES:
        validate_pair(schema_path, instance_path)

    negative_cases = [
        ("unknown-version", lambda value: value.__setitem__("formatVersion", "2")),
        ("uppercase-hash", lambda value: value.__setitem__("taskHash", "A" * 64)),
        ("success-with-failure", lambda value: value.__setitem__("failureType", "error")),
        (
            "failure-with-empty-type",
            lambda value: (value.__setitem__("success", False), value.__setitem__("failureType", "")),
        ),
        ("short-signature", lambda value: value.__setitem__("signature", "aa")),
        ("unknown-top-level", lambda value: value.__setitem__("authorityState", "trusted")),
    ]
    for name, mutate in negative_cases:
        assert_invalid_xaip(name, mutate)


if __name__ == "__main__":
    main()
