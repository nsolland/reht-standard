from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]

CASES = [
    ("schemas/action-envelope.schema.json", "examples/admissible-action.json"),
    ("schemas/execution-receipt.schema.json", "examples/execution-receipt.json"),
]


def load_json(path: str) -> dict:
    with (ROOT / path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> None:
    for schema_path, instance_path in CASES:
        schema = load_json(schema_path)
        instance = load_json(instance_path)
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
        if errors:
            details = "\n".join(f"{instance_path}: {error.message}" for error in errors)
            raise SystemExit(details)
        print(f"validated {instance_path}")


if __name__ == "__main__":
    main()
