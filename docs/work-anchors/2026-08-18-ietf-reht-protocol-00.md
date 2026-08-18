# Work anchor — IETF REHT protocol -00

- Active delivery: correct and publish the first individual IETF Internet-Draft package for REHT without changing canonical REHT/RACS ownership semantics.
- Repository: `nsolland/reht-standard`
- Canonical base: `b88101a26bf157185405cacc71e405e268dd9b61`
- Branch: `feat/ietf-reht-protocol-00`
- Draft PR: to be created from this branch before substantive files are added.
- Owner/claim: Njål Gaute Solland / ChatGPT; public protocol/reference/conformance surface.
- Owned files: `ietf/draft-solland-reht-protocol-00.xml`, `ietf/reht_reference_impl.py`, `ietf/test_reht_conformance.py`, `ietf/README.md`, this anchor.
- Dependencies: current REHT standard semantics in this repository; canonical RACS v0.2 decision contract in `nsolland/Racs`; IETF RFCXML v3 submission rules.
- Invariants: REHT remains the fresh execution-authority boundary; RACS is deterministic binding only and uses `ALLOW`, `MODIFY`, `DEFER`, `DENY`, `STEP_UP`, `HALT`; a PEP enforces the REHT/RACS result but does not originate or independently redefine organizational authority.
