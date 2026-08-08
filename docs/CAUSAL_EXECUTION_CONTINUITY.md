# Causal Execution Continuity

Status: normative draft for REHT Standard v0.2

## 1. Canonical invariant

Authorization is not a durable truth about an action.

A prior admissibility or authorization result MUST NOT remain executable merely because a wall-clock validity interval has not elapsed.

At the execution boundary, the executing side MUST independently re-establish that the action, authority and execution-relevant governed state are causally continuous with the state that was evaluated.

The operative question is:

> Is this still the thing that was approved?

If continuity cannot be proven for the requirements that apply to the selected profile, execution MUST fail closed.

## 2. Proportionality and profile scoping

REHT MUST NOT require every implementation to prove every available continuity property for every action.

Conformance requirements MUST be scoped to the execution profile that applies to the action, architecture and consequence boundary.

A profile SHOULD consider at minimum:

- whether evaluation and execution occur inside the same trusted execution boundary;
- whether independently owned systems participate between evaluation and execution;
- whether authority or governed state may materially change before consequence;
- whether replay, duplication or delayed execution is possible;
- whether evidence or receipt continuity is material to the action;
- the consequence and reversibility of the action.

For a local or atomic action where evaluation and execution occur within the same trusted boundary and no material intervening state can occur, direct execution-time re-derivation and deterministic binding MAY satisfy the applicable continuity profile without requiring external mirrors, portable evidence bundles or cross-system lineage reconstruction.

For execution that crosses independently owned systems, delayed execution, mutable authority/state, or other material continuity risks, the applicable profile MUST require the additional causal and reconstructability properties necessary to establish continuity.

Fail-closed means that an implementation MUST refuse execution when a requirement of the applicable profile cannot be established. It does not mean that every REHT requirement applies universally to every action.

Profiles MUST NOT weaken the canonical invariant or convert missing evidence into permission. Proportionality changes the evidence burden, not the requirement that execution validity be established at consequence.

## 3. Causal ordering, not shared-clock validity

Independently owned systems MUST NOT require synchronized wall-clock time as the authoritative primitive for execution validity.

A timestamp such as `valid_until` MAY express policy scope, forensic context, retention, operator expectations or external legal/contractual time constraints. It MUST NOT by itself establish that a prior admissibility remains executable.

Execution continuity is determined from causal ordering: what can be proven to have preceded, followed or intervened between evaluation and execution.

Wall-clock timestamps MAY remain in receipts and evidence for correlation, audit and forensics.

## 4. Execution binding

A conforming implementation MUST bind an admissibility result to a deterministic execution envelope when required by the applicable execution profile.

The binding identifier is referred to by this profile as `execution_envelope_hash`.

The execution envelope MUST be sufficient to bind, where relevant:

- the normalized action and material parameters;
- actor or principal identity;
- target or resource identity;
- authority and delegation references;
- scope and purpose constraints;
- evidence and governed-state references material to the result;
- causal position or lineage anchor;
- replay or idempotency semantics;
- canonicalization and profile version.

The runtime wire representation and canonical digest semantics remain owned by the canonical RACS contracts where an equivalent runtime contract exists. REHT defines the clearance and conformance semantics, not a duplicate wire protocol.

## 5. Execution-time re-derivation

Immediately before a consequence-bearing action crosses the execution boundary, the executing side MUST independently re-derive the execution-relevant state required by the applicable profile and compare it with the bound or evaluated state.

A matching binding is necessary but not sufficient for execution. It permits REHT evaluation to continue; it does not force an `ADMISSIBLE` result.

Any material mismatch MUST result in a non-executable state.

## 6. Independent reconstructability

Independent reconstructability is REQUIRED when the applicable profile crosses independently owned systems or otherwise requires portable causal proof. It is not a universal requirement for local atomic execution inside one trusted boundary.

Where reconstructability is required, a hash match alone is not sufficient evidence of causal continuity.

A conforming interoperability profile MUST expose enough integrity-protected causal evidence for an independent verifier to reconstruct the execution-relevant lineage and verify why the presented binding corresponds to the authorized state.

The verifier MUST be able to establish, where applicable:

- the ordered causal position of the authorization and proposed execution;
- the identity binding of the relevant producer or signer where identity is material;
- integrity of the lineage used for the comparison;
- whether a material state or authority transition intervened;
- whether required lineage contains an unproven gap;
- whether a consumption-bound position or action has already been used.

The profile MUST fail closed when required reconstruction cannot be completed from the presented and independently resolvable evidence.

REHT does not require a particular signature algorithm, block format, archive format, Lamport implementation, TIBET token, mirror topology or storage substrate. Ed25519-per-block signing, byte-identical mirrored bundles and similar mechanisms MAY satisfy parts of these properties, but they are external implementation choices rather than REHT dependencies.

Where reproducible evidence bundles are used, a conforming profile SHOULD permit an independent verifier to reproduce the canonical evidence representation and obtain the same integrity result from the same source material. Byte-for-byte reproducibility is a strong implementation property but is not mandated where an equivalent canonical, independently verifiable representation is used.

## 7. First conformance vector

The first cross-system interoperability profile defines one positive control and five required negative cases.

### Positive control

The independently re-derived execution envelope matches the authorized binding; required causal lineage is independently reconstructable and continuous; no disqualifying event intervened; scope is valid; receipt continuity is intact; replay constraints are satisfied.

Expected result: REHT may continue evaluation.

### Drift

The execution-relevant state differs from the state bound to the prior result.

Expected result: hard deny / non-executable.

### Expired scope

The authority, delegation, purpose or other explicit scope constraint is no longer valid for the proposed execution.

Expected result: hard deny / non-executable.

Scope expiry remains an explicit check. A wall-clock constraint may be one input to scope policy, but the existence of an unexpired timestamp does not establish execution continuity.

### Broken receipt continuity

Required receipt or evidence lineage contains an unproven gap or cannot be independently reconstructed where reconstruction is required by the profile.

Expected result: `INDETERMINATE`, `NO_LONGER_ADMISSIBLE` or equivalent fail-closed result. Missing continuity MUST NOT be inferred as continuity.

### Stale authority

A relevant revocation, delegation mutation, authority replacement or other authority event causally intervened after the prior result was established.

Expected result: hard deny / non-executable.

### Replay

A single-use or otherwise consumption-bound causal position/action has already been consumed.

Expected result: hard deny / non-executable.

## 8. Common continuity failures

Where implementation semantics permit, drift, stale authority and replay SHOULD be represented as variants of one underlying failure class: the execution state is not causally continuous with the state that was authorized.

Expired scope and broken receipt continuity remain explicit independent checks in this version of the profile.

## 9. Bidirectional interoperability

A cross-system conformance profile MUST specify both sides of the boundary:

- what the producer guarantees when presenting an external binding;
- what causal and integrity evidence the producer makes available for independent reconstruction;
- what the consumer is entitled to rely on;
- what the consumer MUST independently re-derive or reconstruct;
- which conditions invalidate reliance;
- required refusal behavior.

A profile that proves only that one producer can emit an accepted object is not sufficient. Negative refusal behavior and independent reconstruction are part of cross-system conformance where the profile requires them.

External systems MAY map their own capability or grant identifiers into this binding contract without becoming required REHT dependencies.

## 10. Independence rule

REHT does not require any specific identity, authority, evidence, runtime, capability, receipt or causal-time implementation.

External systems remain independently owned. They may supply evidence or binding references into the REHT execution boundary, but REHT retains the final clearance semantics.

A conforming integration MUST NOT invert this ownership boundary.

## 11. Research basis

This profile is informed by the causal-ordering and reconstructability approach described in:

- RS-2026-001, *Causal Substrate Audit: Lamport-Anchored Evidence Under Time-Source Asymmetry*, Jasper van de Meent / Humotica and Richard Barron / Red Specter Security Research, published 22 May 2026, DOI `10.5281/zenodo.20338260`.
- the signed reproducible source-bundle material associated with RS-2026-001, including its block-level integrity and mirrored reproducibility properties, as research evidence for independent reconstruction.
- the related TIBET Causal Time Internet-Draft as technical background.

REHT adopts no dependency on TIBET, the RS-2026-001 bundle format, Ed25519 or any particular causal substrate through these references. They are technical and research background for the required properties.

## 12. Migration note for v0.1 fields

Existing v0.1 objects contain fields such as `timestamp`, `observed_at`, `evaluated_at`, `valid_from`, `valid_until` and `expires_at`.

These fields are not removed by this document. Their execution-validity semantics are narrowed:

- they MAY remain policy, scope, forensic, audit or correlation inputs;
- they MUST NOT be treated as sufficient proof that a prior result remains executable;
- execution validity MUST be re-established at the execution boundary through the applicable causal-continuity profile;
- evidence used to establish continuity MUST be independently reconstructable where the selected profile requires cross-system reconstruction.

Any schema change to canonical RACS-owned runtime objects MUST be made in RACS/spec and referenced from reht-standard rather than duplicated here.
