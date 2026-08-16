# Work anchor — REHT Economic Authority Profile v0.1

- Active delivery: add a rail-neutral economic-authority profile over existing REHT execution authorization without duplicating Kernel or RACS contracts.
- Repository: `nsolland/reht-standard`
- Canonical base: `b88101a26bf157185405cacc71e405e268dd9b61`
- Branch: `feat/economic-authority-profile-v0.1`
- Draft PR: pending creation from this anchor commit.
- Proposal: `#18`
- Owner/claim: ChatGPT on behalf of Njål; public REHT profile/specification/conformance surface.
- Owned files: `SPECIFICATION.md`, `CONFORMANCE.md`, `CHANGELOG.md`, `docs/ECONOMIC_AUTHORITY_PROFILE_V0_1.md`, `conformance/economic-authority-v0.1.json`, this anchor.
- Dependencies: VALO Kernel Authority / Delegation / Purpose semantics; canonical RACS v0.2 runtime wire contracts and signed artifact chain; existing REHT causal execution continuity. No dependency may grant or widen authority.
- Version decision: additive optional normative profile => target `0.5.0-draft.1`; existing `0.4.x` conformance remains valid unless this profile is claimed.
