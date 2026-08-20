# REHT Conformance

Version: 0.5.0-draft.1

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
13. Treat prior authorization or admissibility as non-durable and re-establish execution validity immediately before consequence.
14. Bind an evaluated action to a deterministic execution envelope or equivalent interoperable binding when evaluation and execution are separated.
15. Independently re-derive the execution-relevant action, authority and governed state at the execution boundary.
16. Fail closed when required causal continuity cannot be proven.
17. Reject material state drift, stale authority and replay according to the applicable execution-continuity profile.
18. Treat broken required receipt continuity as non-executable; missing continuity MUST NOT be inferred as continuity.
19. Keep explicit scope constraints independently enforceable, including temporal scope constraints where policy requires them.
20. Treat wall-clock timestamps as audit, forensic, correlation or policy inputs; wall-clock validity alone MUST NOT establish that a prior result remains executable across independently owned systems.
21. Treat persisted files, memory, configuration, instructions, handoffs and cached artifacts as non-authoritative unless their current integrity and standing are established under the governed context.
22. Prevent worker-produced or externally supplied persistent material from silently self-promoting into authoritative policy, instruction, evidence or state for later consequence-bearing work.
23. Bind material governing contract/policy state to the evaluation by deterministic reference, version, digest or equivalent continuity mechanism.
24. Treat amendment, termination, replacement or material drift of an applicable governing contract/policy as invalidating reliance on the prior result.
25. Distinguish material execution constraints established for the current evaluation from material constraints known to be required but unresolved or unavailable; a known unresolved required constraint MUST NOT yield `ADMISSIBLE`.
26. Treat any material post-evaluation action transformation as a new candidate action requiring fresh evaluation before consequence.
27. When confidential or hardware-attested execution is a material requirement, bind the normalized execution-substrate evidence by deterministic digest or equivalent integrity-verifiable reference.
28. Re-establish any required confidential-execution substrate immediately before consequence and fail closed when the required substrate evidence is missing, unresolved, invalid, revoked, stale, expired or materially mismatched.
29. When materially relying on an external verification receipt or equivalent evidence, establish the verifier/issuer identity, intended executor/audience where scoped, exact action/request and material-parameter binding, deterministic governing policy/configuration binding, integrity/trust basis, applicable freshness and replay/consumption state.
30. Treat cryptographic validity of external verification evidence as evidence integrity only; it MUST NOT by itself establish current authority, admissibility or execution permission.
31. Fail closed when a required external verification-evidence binding is missing, untrusted, stale, replayed, consumed or materially mismatched with the current governed execution context.

A conforming producer MUST NOT:

- silently omit required authority or policy context;
- silently treat a known unresolved material execution constraint as satisfied;
- convert uncertainty into admissibility;
- infer authorship, deception, intent or accountability solely from a detector label;
- produce `INADMISSIBLE` solely from a detector result unless an applicable policy independently makes that evidence dispositive and its evidence threshold is satisfied;
- reuse an invalidated result as current;
- treat persistence alone as standing, trust, authority or clearance;
- reuse a prior conformance/admissibility result after material governing-contract drift without fresh evaluation;
- let a materially rewritten, clamped, substituted or otherwise transformed action inherit the source action's admissibility result or receipt;
- represent an unexpired timestamp as sufficient proof of execution validity;
- treat TEE, confidential-compute attestation, hardware identity, measurement or verifier output as execution authority, approval or clearance;
- treat a cryptographically valid external verification receipt as proof that current authority or governed state remains valid;
- accept materially relied-upon external verification evidence for the wrong audience/executor, from an untrusted issuer/key, under a mismatched policy/configuration binding, for a mismatched action/request/parameter set, or after required freshness/replay constraints fail;
- allow required confidential-execution evidence to bypass the same execution-continuity and governed-effect boundary as the evaluated action;
- allow required external verification evidence to bypass the same execution-continuity and governed-effect boundary as the evaluated action;
- alter evidence references after receipt creation without creating a new receipt;
- claim REHT compatibility while using incompatible outcome semantics;
- claim conformance when negative refusal cases are not enforced at the execution boundary.

## Causal execution conformance vector

The v0.5 required interoperability vector consists of one positive control and sixteen negative cases:

1. Positive control — matching independently re-derived envelope, established required constraints, matching required confidential-execution binding, valid materially relied-upon external verification-evidence bindings and valid continuity permit REHT evaluation to continue; this does not force `ADMISSIBLE`.
2. Drift — material execution-state mismatch is non-executable.
3. Expired scope — invalid authority/delegation/purpose/scope is non-executable.
4. Broken receipt continuity — unproven required lineage is non-executable.
5. Stale authority — causally intervening revocation or authority mutation is non-executable.
6. Replay — previously consumed single-use binding or causal position is non-executable.
7. Persistent-state self-promotion — persisted material with no current governed standing cannot become operative solely by surviving a worker/session/context boundary.
8. Governing-contract drift — amendment, termination or replacement of a material governing contract invalidates the prior continuation.
9. Required constraint unresolved — a material execution constraint known to be required but not established is non-executable.
10. Post-evaluation action transformation — a materially revised/clamped/rewritten/substituted action cannot inherit the source result; fresh evaluation is required.
11. Confidential-execution continuity failure — when confidential execution is required, missing, unresolved, stale, revoked, expired or mismatched substrate evidence is non-executable.
12. Verification-evidence audience mismatch — evidence scoped to another audience/executor is non-executable.
13. Verification-evidence issuer/key mismatch — evidence from an unexpected verifier or untrusted/substituted key is non-executable.
14. Verification-evidence configuration mismatch — evidence bound to a materially different policy/configuration state is non-executable.
15. Verification-evidence action mismatch — evidence whose action/request/material-parameter binding differs from the action presented for consequence is non-executable.
16. Verification-evidence freshness failure — stale/expired evidence is non-executable where freshness is required, and an unexpired window cannot override intervening authority/state invalidation.
17. Verification-evidence replay — reused single-use evidence, nonce/sequence or consumed evidence binding is non-executable.

See [`docs/CAUSAL_EXECUTION_CONTINUITY.md`](docs/CAUSAL_EXECUTION_CONTINUITY.md), [`docs/STATE_AND_CONTRACT_CONTINUITY.md`](docs/STATE_AND_CONTRACT_CONTINUITY.md), [`docs/CONSTRAINT_OBSERVABILITY_AND_ACTION_TRANSFORMATION.md`](docs/CONSTRAINT_OBSERVABILITY_AND_ACTION_TRANSFORMATION.md), [`docs/CONFIDENTIAL_EXECUTION_CONTINUITY.md`](docs/CONFIDENTIAL_EXECUTION_CONTINUITY.md), [`docs/VERIFICATION_EVIDENCE_BINDING.md`](docs/VERIFICATION_EVIDENCE_BINDING.md) and [`conformance/causal-execution-v0.5.json`](conformance/causal-execution-v0.5.json).

## Conformance levels

### Level 1 — Schema

Objects validate against the published schemas.

### Level 2 — Semantic

Outcome, state, constraint-completeness, verification-evidence reliance and execution-validity semantics match the specification.

### Level 3 — Integrity

Receipts, hashes, timestamps, provenance references, governing-contract bindings, persistent-state standing references, constraint-resolution references, confidential-execution substrate bindings, external verification-evidence issuer/audience/action/configuration/freshness/replay bindings, causal-binding references and continuous-integrity transitions are preserved and testable.

### Level 4 — Operational

The implementation demonstrates end-to-end enforcement at an execution boundary, including the required negative causal-continuity cases.

Only Levels 1–3 are defined as static public conformance surfaces by this repository. Level 4 depends on an implementation and is not certified here.
