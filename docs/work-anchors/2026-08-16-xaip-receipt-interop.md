# Work anchor — XAIP receipt interoperability

- Active delivery: add a REHT-owned XAIP receipt interoperability/export profile without changing REHT authorization or receipt semantics.
- Repository: `nsolland/reht-standard`
- Canonical base: `b88101a26bf157185405cacc71e405e268dd9b61`
- Branch: `feat/xaip-receipt-interop`
- Draft PR: pending creation from this anchor commit.
- Owner/claim: ChatGPT on behalf of Njål; receipt interoperability/conformance surface.
- Owned files: `docs/XAIP_RECEIPT_INTEROP.md`, `schemas/xaip-receipt-export.schema.json`, `examples/xaip-receipt-export.json`, `tests/validate_examples.py`, `README.md`, `CHANGELOG.md`, this anchor.
- Dependencies: public REHT receipt profile and `draft-xkumakichi-xaip-receipts-03`; XAIP remains work in progress and is an external interoperability format only.
- Boundary: REHT/RACS authority, decision, state continuity, governed effect and Veritas evidence semantics remain authoritative. XAIP export MUST NOT weaken or replace them.
