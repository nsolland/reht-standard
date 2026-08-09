# Reference Implementation Patterns

Status: non-normative guidance for REHT Standard v0.2

This document lists documented implementation patterns that may satisfy parts of REHT's causal execution continuity requirements.

These are examples, not required technologies. Conformance is determined by the normative properties in the REHT Standard and Causal Execution Continuity profile, not by use of any named implementation.

## Required properties

A conforming causal-continuity implementation must satisfy the applicable normative requirements for:

- causal ordering;
- integrity-protected lineage;
- independent reconstructability;
- identity binding where material;
- detection of relevant intervening state or authority transitions;
- replay detection where consumption semantics apply;
- fail-closed behavior when required continuity cannot be established.

## Documented reference patterns

### Lamport-anchored causal chains

Lamport-style causal positions can establish provable ordering without treating synchronized wall-clock time as the authoritative ordering source.

REHT does not require Lamport clocks. Equivalent causal-ordering mechanisms are permitted when they satisfy the normative properties.

### TIBET Causal Time

The TIBET Causal Time Internet-Draft is a documented technical approach to causal ordering under time-source asymmetry.

REHT references TIBET as technical background only. TIBET is not a required runtime, protocol dependency or adopted IETF standard for REHT conformance.

### Signed block-level evidence

Per-block digital signatures, including Ed25519 signatures, are one implementation pattern for integrity and signer binding across an evidence chain.

REHT does not require Ed25519 or per-block signing. Other cryptographic constructions may be used if they provide the required integrity and identity-binding properties.

### Reproducible signed evidence bundles

A signed evidence bundle that can be independently reconstructed from canonical source material provides a strong implementation pattern for independent verification.

Byte-identical output across independent mirrors is especially useful because it permits verifiers to establish that they are evaluating the same canonical artefact rather than semantically similar but different representations.

REHT does not mandate TBZ, a particular archive format, byte-identical mirroring or any specific bundle layout. Equivalent canonical and independently verifiable representations are permitted.

### Independent mirrors

Mirrored evidence artefacts can reduce dependence on a single evidence host and can provide additional evidence that the verifier and producer are operating over the same immutable material.

Mirror topology is external substrate and is not part of REHT authorization semantics.

## Research example: RS-2026-001

RS-2026-001, *Causal Substrate Audit: Lamport-Anchored Evidence Under Time-Source Asymmetry*, Jasper van de Meent / Humotica and Richard Barron / Red Specter Security Research, published 22 May 2026, DOI `10.5281/zenodo.20338260`, documents a concrete combination of these patterns.

The associated signed reproducible source-bundle material is a useful reference artefact for:

- Lamport-anchored causal ordering;
- operation under asymmetric or drifted wall clocks;
- block-level integrity/signing;
- independent reconstruction;
- reproducible evidence across mirrors.

The paper and bundle are evidence that such properties can be implemented. They do not define REHT conformance by themselves.

## Adoption rule

Implementations SHOULD choose the smallest substrate that satisfies the required REHT properties for their environment.

A conformance claim MUST be based on observable behavior and independently verifiable evidence, not on the presence of a named technology.

In particular:

- using TIBET does not automatically make an implementation REHT-conformant;
- using Ed25519 does not automatically establish causal continuity;
- producing a signed bundle does not automatically establish reconstructability;
- using another causal or cryptographic substrate does not prevent conformance.

REHT standardizes the boundary properties. Implementers choose the substrate.
