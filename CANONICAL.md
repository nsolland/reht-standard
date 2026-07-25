# Canonical contract reference (issue #991, ruling #991.1)

**reht-standard is canonical ONLY for REHT-specific clearance and authorization standards.**
It MUST reference the RACS runtime execution-governance contracts, not duplicate them.

## Reference relationship

| reht-standard schema (REHT-specific profile) | Canonical RACS contract (source of truth) |
|----------------------------------------------|-------------------------------------------|
| `schemas/action-envelope.schema.json` | `Racs/spec/action-envelope-v0.2.schema.json` |
| `schemas/authority-context.schema.json` | `Racs/spec/authority-context.yaml` |
| `schemas/policy-context.schema.json` | `Racs/spec/policy-context.yaml` |
| `schemas/evidence-package.schema.json` | `Racs/spec/evidence-package.yaml` |
| `schemas/governance-state.schema.json` | `Racs/spec/governance-state.schema.json` |
| `schemas/continuous-integrity-event.schema.json` | `Racs/spec/continuous-integrity-event-v0.2.schema.json` |
| `schemas/execution-receipt.schema.json` | `Racs/spec/execution-receipt-v0.2.schema.json` |
| `schemas/admissibility-result.schema.json` | **REHT-specific** — retained, no RACS equivalent |

## Rules

1. reht-standard schemas are REHT clearance/authorization *profiles*. The runtime wire
   format, canonicalization (RACS-JCS-1 / RFC 8785) and digest (SHA-256) semantics are
   defined by RACS/spec and MUST NOT be redefined here.
2. Each overlapping schema carries a `racs_canonical` field naming the canonical RACS
   `$id` it references, so consumers can resolve the authoritative contract.
3. Canonicalization and digest rules: `Racs/spec/CANONICALIZATION.md` (RACS-JCS-1) and
   `Racs/spec/CANONICAL_CONTRACTS.md`.
4. No new runtime execution-governance contract may be introduced in reht-standard that
   duplicates a RACS contract.
5. ACS/VACS (VAIG) is deprecated as an execution decision layer; RACS replaces it.

## Supersession

See `Racs/spec/SUPERSEDED.md` for the explicit supersession record and compatibility
mappings (e.g. `vacs/acs_packet` → RACS `action-envelope-v0.2`).
