# PEACE Protocol v0

**Personal Execution, Authority & Compute Environment**  
**Your Sovereign State.**

## 1. Status and method

This is the language-neutral normative proposal for PEACE v0.

PEACE is defined first by the **world that must remain possible**, then by the minimum invariants required to keep that world sovereign, safe and reconstructible. It is not defined by a reference codebase.

The canonical derivation input is `PEACE_WORLD_V0.md`.

A fresh implementation SHOULD be derivable from the world statement plus this specification, schemas and conformance vectors without reading another implementation's source code.

No programming language, operating system, model provider, database, device class, credential scheme, cryptographic library, compute provider or payment provider is a normative dependency.

Normative words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are requirements of this proposal.

## 2. Core principle

> **Everything can be routed except sovereignty.**

A person or organisation may continuously replace models, agents, devices, credentials, services, clouds, compute providers, routers and settlement rails. The sovereign domain must nevertheless preserve the same logical actor, authoritative state, standing, authority, delegation, governance, evidence lineage and recovery semantics.

Capability may move. Intelligence may move. Compute may move. Money may move. Authority does not move merely because any of those are routed.

## 3. Constitutional invariants

A conformant implementation MUST preserve all of the following:

1. **ACTOR_IS_AUTHORITY_ROOT** — the logical protected actor/domain is the root of authority. A credential, key, device, provider, model, runtime, storage location or compute node MUST NOT become the authority root merely by representing, authenticating or serving that actor.
2. **FRAMLEIS** — replacement or loss of a replaceable artifact MUST NOT by itself destroy continuity of the logical actor/domain, admitted state, standing, authority, rights, relationships, governance, evidence lineage or recovery path.
3. **CAPABILITY_NE_AUTHORITY** — capability, intelligence, possession of data, successful authentication, attestation, routing or computation MUST NOT create authority to act.
4. **CANDIDATE_NE_DECISION** — observation, inference, prediction, recommendation, plan or generated action is candidate material only.
5. **DISCLOSURE_IS_GOVERNED** — information leaving the sovereign domain MUST be minimized and bound to purpose, destination and current governed context.
6. **NO_DIRECT_EFFECT_PATH** — no replaceable worker, model, runtime, factory or service may turn its own output directly into a consequence-bearing effect.
7. **FRESH_AUTHORITY_AT_EFFECT** — consequence requires authorization against current authority and current relevant state for the exact action immediately before effect.
8. **EVIDENCE_NE_STATE** — evidence records what was claimed, observed, proposed, authorized, attempted or produced. It MUST NOT mutate authoritative state merely by existing, being signed or being tamper-evident.
9. **ROUTING_NE_AUTHORITY** — route or provider selection may affect admissibility or capability, but MUST NOT create authority.
10. **IMPLEMENTATION_NE_PROTOCOL** — implementation language, runtime, transport, storage and cryptographic mechanism are replaceable.
11. **AUTHORITY_OVER_ACTION_NE_AUTHORITY_OVER_ACTOR** — authorization for one action MUST NOT imply ownership or general authority over another actor.
12. **RECOVERY_NE_TRANSFER** — loss of access MUST permit recovery of control without permitting transfer of identity or authority to a recovery provider.
13. **REPLICA_NE_SOVEREIGN** — a replica MUST NOT become authoritative merely because it contains the newest bytes.

These invariants are the protocol. Component names and internal topology are not.

## 4. Minimal semantic separation

A PEACE design MUST preserve distinct semantic stages equivalent to:

```text
authoritative state
  -> bounded projection / disclosure
  -> external reasoning or work
  -> candidate
  -> current exact authorization
  -> effect / settlement
  -> evidence / outcome
  -> admitted state transition
```

Recovery and replication are orthogonal and MUST preserve the same logical actor/domain.

The following distinctions are normative:

```text
knowledge      != authority
proposal       != decision
authorization  != effect
evidence       != authoritative state
credential     != actor
compute route  != authority source
payment rail   != economic authority
implementation != protocol
```

## 5. Required logical roles

Implementations may use any names or data structures, but must be able to express semantics equivalent to:

- a logical protected actor/domain;
- current authoritative state and deterministic state commitment/root;
- current standing and authority/delegation/revocation state;
- a purpose- and destination-scoped governed projection/disclosure grant;
- a worker result represented as a candidate;
- an exact consequence action;
- a fresh authorization decision bound to that consequence and current state/authority;
- an effect/outcome receipt or evidence event;
- an admission decision that determines whether evidence changes authoritative state;
- a recovery representation sufficient to preserve actor/domain continuity;
- a replication lineage sufficient to reject stale or divergent state transitions.

## 6. Abstract lifecycle

```text
ADMIT
  -> PROJECT
  -> DISCLOSE
  -> PROPOSE
  -> AUTHORIZE
  -> EFFECT / SETTLE
  -> OBSERVE
  -> ADMIT

REPLICATE
RECOVER
```

### 6.1 ADMIT

Candidate information or evidence may be accepted, rejected or left unresolved. Persistence, signature validity, provider status or worker confidence MUST NOT establish standing by themselves. Only an admitted transition may mutate authoritative state.

### 6.2 PROJECT / DISCLOSE

A capability receives no more governed information than the task requires. A disclosure authorization MUST be bound sufficiently to prevent use outside the intended actor/domain, destination, purpose, projection/scope, relevant current state/authority context and validity conditions.

Disclosure clearance MUST NOT itself authorize an external effect.

### 6.3 PROPOSE

A worker, model, capability factory or external service may calculate, infer, recommend or construct a candidate action. The candidate is inert with respect to authoritative state and consequence.

### 6.4 AUTHORIZE

Before consequence, the system MUST evaluate the exact action against fresh current governed state and authority.

Where applicable, the authorization decision must bind or verify:

- protected actor/domain;
- acting delegate/capability;
- current standing;
- delegation chain and attenuation;
- purpose and scope;
- exact action semantics and parameters;
- current relevant state commitment/version;
- current authority/revocation state;
- validity/freshness conditions;
- required admissibility/evidence conditions.

A prior disclosure grant, old authorization, model confidence, route decision, credential possession, compute allocation or payment capability MUST NOT substitute for the fresh consequence-time check.

### 6.5 EFFECT / SETTLE

Only the exact authorized consequence may be attempted. If current authority, state, standing, revocation, purpose, scope, exact-action binding or required evidence no longer satisfies authorization, the result MUST be null effect / fail closed.

Settlement is a consequence and is therefore governed by the same rule. A payment rail may execute value transfer only after the exact economic action has been authorized.

### 6.6 OBSERVE

Effect attempts and outcomes produce evidence sufficient to correlate the candidate, authorization, exact effect attempt, settlement and observed result.

Cryptographic integrity, signer authority, policy meaning, artifact resolution and external truth remain separate questions.

### 6.7 REPLICATE

Replication MUST synchronize admitted state transitions and lineage, not blindly copy mutable files.

A replica MUST NOT become sovereign merely because it is newest. Stale or divergent lineage MUST fail closed to explicit resolution, re-authorization or rejection. Last-write-wins semantics are non-conformant for authoritative state.

### 6.8 RECOVER

Recovery MUST preserve the same logical actor/domain while allowing credentials, keys, devices, runtimes, storage and providers to rotate or be replaced.

No single recovery provider SHOULD be sufficient to unilaterally become or transfer the actor. Recovery mechanisms SHOULD support independent evidence, quorum, compartmentalization, revocation of lost credentials and auditable receipts.

## 7. Capability and routing model

PEACE does not prescribe a model router, compute scheduler, capability factory or payment processor.

Any system may propose routes based on capability, cost, latency, energy, locality, trust, privacy, availability or quality. Routing remains subordinate to disclosure, standing, authority and consequence constraints.

Examples of replaceable capability classes include:

```text
capability factory   -> one-shot software / agents / workflows
intelligence router  -> model selection / composition
compute provider     -> local / edge / GPU / cloud
service provider     -> external APIs / enterprise systems
settlement rail      -> payment / billing / value transfer
```

PEACE governs the sovereign domain; it does not require ownership of these capability classes.

## 8. Relationship to REHT and Open Agent Contract

PEACE is broader than both.

- Open Agent Contract MAY express portable governed contract/intent semantics inside a PEACE flow.
- REHT MAY implement the fresh exact consequence-time authorization boundary required by PEACE.

Neither is a mandatory dependency. A conformant PEACE implementation may use equivalent independent components if the observable semantics and conformance vectors are preserved.

## 9. Canonical digest encoding v0

Cross-language conformance vectors use this encoding before SHA-256:

1. UTF-8 JSON.
2. Object keys sorted lexicographically by Unicode code point.
3. No insignificant whitespace.
4. Array order preserved.
5. Standard JSON string escaping.
6. `true`, `false`, and `null` for booleans/null.
7. No floating-point values in canonical digest objects for v0; integers are permitted.

`digest(x) = "sha256:" + lowercase_hex(SHA256(canonical_json(x)))`

## 10. Conformance

A claimed PEACE v0 implementation MUST demonstrate, for its claimed profile, that:

- replacement artifacts do not become the authority root;
- worker/model/factory output cannot bypass the consequence boundary;
- possession of data/compute/credentials does not create authority;
- disclosure outside allowed purpose/destination/scope fails closed;
- revocation before effect prevents effect;
- stale relevant state or authority invalidates prior authorization;
- an authorization cannot be reused for materially different action semantics;
- evidence does not mutate authoritative state without admission;
- routing does not create authority;
- settlement cannot bypass current exact authorization;
- replicas cannot self-promote to sovereignty;
- conflicting lineage does not silently merge;
- recovery preserves the same logical actor/domain across replacement infrastructure;
- implementation language/runtime remains non-authoritative metadata;
- required canonical digest vectors are reproduced exactly.

Canonical machine-readable vectors are in `conformance-v0.json` and the logical envelope schema is in `peace-envelope-v0.schema.json`.

## 11. Independent derivability

A useful derivation test is to give an independent reasoning system only `PEACE_WORLD_V0.md` and ask what must necessarily be true. The system is not required to reproduce PEACE vocabulary or component names. The relevant question is whether it independently converges on equivalent boundaries and invariants.

Independent derivation is design evidence, not conformance certification.

## 12. Open protocol requirement

PEACE is intended to be free to adopt, independently implementable, royalty-free for interoperability and impossible for any single vendor — including VALO — to capture as a mandatory intermediary.

Commercial implementations, managed control planes, certification, assurance, recovery services, registries, adapters and support MAY be proprietary. The protocol semantics and interoperability surface MUST remain independently implementable.

## 13. Canonical user meaning

PEACE is the protocol by which a person's or organisation's digital domain remains theirs while models, devices, credentials, compute, runtimes, services and providers change.

```text
PEACE Protocol
Your Sovereign State.
```
