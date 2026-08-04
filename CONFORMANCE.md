# REHT Conformance

Version: 0.1.0-draft

A conforming implementation MUST:

1. Accept and/or emit versioned REHT objects.
2. Preserve authority, evidence, policy and governance-state references.
3. Return exactly one defined admissibility outcome.
4. Treat `INDETERMINATE` and `NO_LONGER_ADMISSIBLE` as non-executable states.
5. Produce an Execution Receipt for every terminal evaluation.
6. Preserve receipt integrity and linkage where receipt chaining is used.
7. Re-evaluate admissibility after a material Continuous Integrity event.
8. Reject malformed objects that fail the published JSON Schemas.
9. Avoid representing schema compatibility as certification or legal compliance.
10. Treat content-origin and AI-influence detector outputs as evidence rather than authorization authority.
11. Preserve available production-provenance and semantic-integrity references when they materially affect admissibility.
12. Bind material human approval attestations and accountable-principal references when policy requires human control over meaning or consequence.

A conforming producer MUST NOT:

- silently omit required authority or policy context;
- convert uncertainty into admissibility;
- infer authorship, deception, intent or accountability solely from a detector label;
- produce `INADMISSIBLE` solely from a detector result unless an applicable policy independently makes that evidence dispositive and its evidence threshold is satisfied;
- reuse an expired or invalidated result as current;
- alter evidence references after receipt creation without creating a new receipt;
- claim REHT compatibility while using incompatible outcome semantics.

## Conformance levels

### Level 1 — Schema

Objects validate against the published schemas.

### Level 2 — Semantic

Outcome and state semantics match the specification.

### Level 3 — Integrity

Receipts, hashes, timestamps, provenance references and continuous-integrity transitions are preserved and testable.

### Level 4 — Operational

The implementation demonstrates end-to-end enforcement at an execution boundary.

Only Levels 1–3 are defined by this repository. Level 4 depends on an implementation and is not certified here.
