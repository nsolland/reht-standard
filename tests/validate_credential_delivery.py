"""Validate the credential-delivery interop profile (reht-standard #5).

Positive + negative vectors, secret-field rejection and canonical digest
stability against `contracts/credential-delivery-interop-v1.schema.json`.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "contracts" / "credential-delivery-interop-v1.schema.json"
VALID = ROOT / "contracts" / "vectors" / "credential-delivery-interop-v1.valid.json"


def _validator():
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _valid_instance() -> dict:
    return json.loads(VALID.read_text(encoding="utf-8"))


def _errors(v, instance) -> list[str]:
    return [f"{sorted(error.path)}: {error.message}" for error in v.iter_errors(instance)]


def main() -> None:
    v = _validator()
    failures: list[str] = []

    # Positive vector must validate clean.
    ok = _valid_instance()
    errs = _errors(v, ok)
    if errs:
        failures.append(f"valid vector rejected: {errs}")
    else:
        print("ok: valid vector passes")

    # Negative: secret material is structurally prohibited.
    secret = dict(ok)
    secret["credential_value"] = "hunter2"
    if not _errors(v, secret):
        failures.append("secret field not rejected")
    else:
        print("ok: secret field rejected")

    # Negative: secret-named property key rejected.
    secret_key = dict(ok)
    secret_key["api_key"] = "x"
    if not _errors(v, secret_key):
        failures.append("api_key property not rejected")
    else:
        print("ok: api_key property rejected")

    # Negative: unknown field (strict unknown-field rejection).
    unknown = dict(ok)
    unknown["unexpected"] = 1
    if not _errors(v, unknown):
        failures.append("unknown field not rejected")
    else:
        print("ok: unknown field rejected")

    # Negative: missing receipt_requirements.
    no_receipts = dict(ok)
    del no_receipts["receipt_requirements"]
    if not _errors(v, no_receipts):
        failures.append("missing receipt_requirements not rejected")
    else:
        print("ok: missing receipt_requirements rejected")

    # Negative: wrong schema_version.
    wrong_version = dict(ok)
    wrong_version["schema_version"] = "ExecutionEnvelopeV1"
    if not _errors(v, wrong_version):
        failures.append("wrong schema_version not rejected")
    else:
        print("ok: wrong schema_version rejected")

    # Canonical digest stability: re-serialization with sorted keys is stable.
    canonical_a = json.dumps(ok, sort_keys=True, separators=(",", ":"))
    canonical_b = json.dumps(_valid_instance(), sort_keys=True, separators=(",", ":"))
    if canonical_a != canonical_b:
        failures.append("canonical serialization not stable")
    else:
        print("ok: canonical serialization stable")

    if failures:
        raise SystemExit("\n".join(failures))
    print("credential-delivery-interop profile: all checks passed")


if __name__ == "__main__":
    main()