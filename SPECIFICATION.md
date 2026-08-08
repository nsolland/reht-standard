# REHT Standard Specification

Version: 0.2.0-draft

## 1. Purpose

REHT defines a bounded public contract for evaluating whether a proposed AI-mediated action is admissible under the current authority, evidence, policy, context and governance state.

## 2. Principles

1. Reasoning and execution authority are separate responsibilities.
2. Authentication and authorization do not by themselves establish admissibility.
3. Admissibility is evaluated against the present governed state.
4. Material state changes may invalidate an earlier result.
5. Every terminal execution decision should produce a receipt.
6. The standard defines contracts, not proprietary evaluation logic.
7. A conforming implementation must not make the governed action dependent on one model, agent, runtime, protocol or infrastructure provider.
8. Policies, authority definitions, evidence references, workflow state, receipts and persisted learned methods must remain portable and independently verifiable where the implementation stores or exchanges them.
9. Probabilistic content-origin or AI-influence detection is evidence, never execution authority; accountable intent, judgment and approval must be established through governed provenance, authority and attestations.
10. Authorization is not a durable truth about an action. Execution validity must be re-established at the execution boundary.
11. Across independently owned systems, synchronized wall-clock time must not be the authoritative primitive for proving continuity between authorization and execution.
12. A conforming execution boundary must fail closed when causal continuity with the evaluated action, authority or governed state cannot be proven.

## 3. Core objects

### 3.1 Action Envelope

A complete representation of the proposed action and the context required for evaluation.

Minimum fields:

- specification version
- action identifier
- timestamp for audit/forensic context
- actor
- action type
- target
- authority context
- evidence references
- policy references
- governance state

Where an admissibility result may be presented later to an independently owned executor, the evaluated action must also be bound through a deterministic execution-envelope digest or equivalent external binding reference.

### 3.2 Authority Context

Represents who or what proposes the action, the delegation chain and the bounded scope of authority.

Time-based fields may constrain policy or scope, but an unexpired wall-clock interval is not sufficient proof that authority remains executable. Relevant authority changes or revocations that causally intervene after evaluation invalidate reliance on the prior result.

### 3.3 Evidence Package

References evidence used during evaluation. Evidence should be attributable, bounded by applicable policy and integrity-verifiable where possible.

Where an action depends materially on authorship, disclosure, semantic integrity or accountable human control, the Evidence Package should reference available production provenance. This may include original-input digests, transformation history, model and tool identifiers, material human review, disclosure assertions, semantic-integrity checks, approval attestations and detector observations.

Content-origin and AI-influence detector outputs must retain their provider, version, evaluated artifact binding, score or confidence, threshold, timestamp and known limitations where available. A detector label alone does not establish authorship, deception, intent or accountability.

### 3.4 Policy Context

Identifies the policies, rules or controls applicable to the proposed action.

Policy may include explicit temporal constraints. Such constraints remain enforceable as scope or policy conditions, but they do not replace execution-time continuity proof.

### 3.5 Governance State

Represents the execution-relevant system state at evaluation time.

Reference states:

- NORMAL
- SAFE
- HALT

A prior Governance State must not be assumed current solely from timestamps. The execution boundary must re-establish the execution-relevant governed state required by the applicable conformance profile.

### 3.6 Admissibility Result

Reference outcomes:

- ADMISSIBLE
- INADMISSIBLE
- INDETERMINATE
- REQUIRES_STEP_UP
- NO_LONGER_ADMISSIBLE

These outcomes are semantic results, not execution commands.

`ADMISSIBLE` does not become a durable bearer verdict. Before consequence-bearing execution, the executor must establish that the proposed action remains causally continuous with the action, authority and governed state over which the result was produced. A successful binding comparison permits evaluation to continue; it does not itself force an `ADMISSIBLE` result.

When provenance required by applicable policy is materially missing, disputed or inconsistent, an implementation should return `REQUIRES_STEP_UP` when a legitimate principal can resolve the uncertainty, or `INDETERMINATE` when the evidence remains insufficient. A detector result must not by itself produce `INADMISSIBLE` unless an applicable policy independently makes that evidence dispositive and its evidence threshold is satisfied.

### 3.7 Continuous Integrity Event

Records a material event that may affect reliance on an earlier admissibility result.

For execution-boundary conformance, relevant state, authority or consumption events are evaluated by causal order where the applicable profile provides causal lineage. Wall-clock observation time remains useful for audit and forensics but is not sufficient to establish ordering across independent systems.

### 3.8 Execution Receipt

Records the evaluated action, result, relevant evidence references, time, state and integrity data.

Where production provenance or semantic representation integrity materially affected admissibility, the receipt should bind the relevant provenance references, approval attestations and detector observations used in the result.

Where causal-continuity conformance applies, the receipt should preserve the binding, causal-position or lineage references needed to verify the relationship between evaluation and execution. Wall-clock timestamps remain forensic metadata, not proof of continuity.

### 3.9 Causal Execution Continuity

REHT defines a normative execution-continuity profile for independently owned systems.

The canonical invariant is:

> Authorization is not a durable truth. At execution, the system must prove that this is still the thing that was approved.

A conforming implementation must bind the evaluated action to a deterministic execution envelope, re-derive the execution-relevant envelope immediately before consequence, and fail closed on any material mismatch or unproven continuity.

The profile, negative cases and migration semantics are defined in [`docs/CAUSAL_EXECUTION_CONTINUITY.md`](docs/CAUSAL_EXECUTION_CONTINUITY.md).

## 4. Portability and anti-lock-in

### 4.1 Neutrality requirement

REHT contracts must remain usable when the surrounding model, agent, workflow engine, tool protocol, runtime, storage layer or infrastructure provider changes.

Implementations must not require users to redefine authority, policy, evidence bindings or execution controls solely because an underlying provider or runtime is replaced.

### 4.2 Portable governed state

A conforming implementation must provide documented, versioned and independently verifiable representations for the governed state it exchanges or persists, including where applicable:

- authority definitions and delegation chains;
- policy references and applicable policy versions;
- evidence references and provenance;
- workflow and checkpoint state required to resume governed work;
- admissibility results and their input bindings;
- execution-envelope bindings and causal-lineage references where required;
- execution receipts and integrity data;
- persisted learned methods, procedures or workflow adaptations.

The implementation may protect proprietary evaluation logic. It must not use that protection to trap the user's governed records, prevent independent verification or make migration materially dependent on one vendor-specific runtime.

### 4.3 Protocol and infrastructure substitution

Interoperability protocols such as A2A, MCP or future equivalents may transport tasks, tools, messages, artifacts, grants, capabilities or context references. No protocol declaration, agent capability claim, external authorization object or provider-specific object may replace the standard authority, evidence, policy, admissibility or execution-continuity semantics.

Migration or fallback between local, edge, sovereign and cloud infrastructure must preserve the same governed meaning and must not broaden authority, context scope or execution permission.

### 4.4 Independent verification

An external verifier must be able to determine, from the exported contracts and referenced evidence, at least:

- which action was evaluated;
- under which authority and policy;
- which evidence and governed state were used;
- which admissibility result was produced;
- whether material state or authority changes occurred;
- whether required causal continuity between evaluation and execution was established;
- whether the bound action was replayed or consumed where applicable;
- which execution receipt, if any, was bound to the decision.

Independent verification does not require disclosure of proprietary scoring algorithms unless a separate conformance profile requires it.

## 5. Conformance

A conforming implementation:

- accepts or produces versioned Action Envelopes;
- preserves authority, evidence, policy and state references;
- returns one defined admissibility outcome;
- does not represent an indeterminate result as admissible;
- creates a receipt for terminal decisions;
- treats content-origin and AI-influence detection as evidence rather than authorization authority;
- preserves production provenance and semantic-integrity references when they materially affect admissibility;
- does not treat wall-clock expiry alone as proof that a prior admissibility remains executable;
- re-establishes required execution-relevant state at the execution boundary;
- fails closed when causal continuity or required receipt continuity cannot be proven;
- rejects stale authority, material drift and replay according to the applicable profile;
- supports documented export of governed contracts and receipt chains in a provider-independent representation;
- preserves governed meaning when models, agents, protocols or infrastructure are substituted;
- does not technically or contractually block migration of portable governed records;
- does not claim certification solely through schema compatibility.

## 6. Non-goals

This specification does not define:

- model architecture;
- agent reasoning;
- a universal AI-content detector;
- moral truth;
- organizational legitimacy;
- domain policy content;
- proprietary scoring methods;
- production runtime implementation;
- global distributed consensus;
- a mandatory time-synchronization service;
- a mandatory causal-time implementation;
- certification or legal compliance.

## 7. Versioning

Breaking contract changes require a new major specification version. Additive optional fields may be introduced in minor versions. Clarifications and corrections may be introduced in patch versions.

This v0.2 draft introduces a semantic migration for execution validity while retaining the existing v0.1 time fields for compatibility. Existing `timestamp`, `observed_at`, `evaluated_at`, `valid_from`, `valid_until` and `expires_at` fields may remain as policy, scope, audit, forensic or correlation data, but they are not sufficient proof that a prior admissibility remains executable.

Canonical runtime-wire schema changes owned by RACS/spec must be changed there and referenced here rather than duplicated.
