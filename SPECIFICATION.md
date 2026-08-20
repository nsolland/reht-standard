# REHT Standard Specification

Version: 0.5.0-draft.1

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
13. Persistence does not confer standing. Material that survives a worker, session or context boundary must not become governing state solely because it persisted.
14. A governing contract, policy basis or equivalent execution-relevant rule set must not drift during a governed continuation without invalidating reliance on the prior result.
15. A known unresolved material execution constraint must not be normalized into admissibility.
16. A material transformation of an evaluated action creates a new candidate action; the transformed action must not inherit the source action's admissibility result.
17. Cryptographic validity of an external verification receipt establishes evidence integrity only; it does not create current authority, admissibility or execution permission.

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

Where material execution constraints determine admissibility, the envelope or its referenced evidence/policy context must make it possible to distinguish constraints established for the evaluation from material constraints known to remain unresolved.

### 3.2 Authority Context

Represents who or what proposes the action, the delegation chain and the bounded scope of authority.

Time-based fields may constrain policy or scope, but an unexpired wall-clock interval is not sufficient proof that authority remains executable. Relevant authority changes or revocations that causally intervene after evaluation invalidate reliance on the prior result.

### 3.3 Evidence Package

References evidence used during evaluation. Evidence should be attributable, bounded by applicable policy and integrity-verifiable where possible.

Where an action depends materially on authorship, disclosure, semantic integrity or accountable human control, the Evidence Package should reference available production provenance. This may include original-input digests, transformation history, model and tool identifiers, material human review, disclosure assertions, semantic-integrity checks, approval attestations and detector observations.

Content-origin and AI-influence detector outputs must retain their provider, version, evaluated artifact binding, score or confidence, threshold, timestamp and known limitations where available. A detector label alone does not establish authorship, deception, intent or accountability.

Persisted files, memory, configuration, instructions, handoffs and cached artifacts may be referenced as evidence or context only when their integrity, provenance, standing and applicable freshness are established by the governing system. Persistence alone is not evidence of current authority, truth or policy standing.

Where a material execution constraint is required but cannot be established, the Evidence Package or equivalent governed context must preserve that unresolved status rather than silently omitting the constraint and allowing absence to be interpreted as satisfaction.

Where an external verifier, runtime, policy layer or independently owned component produces evidence that is materially relied upon for consequence-bearing execution, the evidence context must preserve the material bindings required by the applicable Verification Evidence Binding profile. These may include verifier/issuer identity, intended executor/audience, exact action/request and parameter bindings, policy/configuration identity, integrity/trust basis, freshness and replay/consumption state.

### 3.4 Policy Context

Identifies the policies, rules, contracts or controls applicable to the proposed action.

Policy may include explicit temporal constraints. Such constraints remain enforceable as scope or policy conditions, but they do not replace execution-time continuity proof.

Where a contract or equivalent rule set materially governs the action, the evaluator should bind the exact governing version or digest used for evaluation so that later amendment, termination or replacement can be detected before execution.

Policy may also identify material constraints that must be established before an action can be admissible. A required constraint that remains unresolved is an explicit governance state, not a permissive default.

Where external verification evidence is relied upon, policy may define accepted verifier identities, trust anchors/keys, intended audiences, configuration bindings, freshness limits and replay/consumption semantics. Satisfying those evidence conditions does not replace current authority or execution-continuity evaluation.

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

When a material execution constraint is known to be required but remains unresolved or unavailable, the result must not be `ADMISSIBLE`. Use `REQUIRES_STEP_UP` where an authorized process can resolve the gap; otherwise use `INDETERMINATE` until sufficient governed evidence or constraint state exists.

### 3.7 Continuous Integrity Event

Records a material event that may affect reliance on an earlier admissibility result.

For execution-boundary conformance, relevant state, authority, governing-contract, policy, constraint, external-evidence trust/binding or consumption events are evaluated by causal order where the applicable profile provides causal lineage. Wall-clock observation time remains useful for audit and forensics but is not sufficient to establish ordering across independent systems.

### 3.8 Execution Receipt

Records the evaluated action, result, relevant evidence references, time, state and integrity data.

Where production provenance or semantic representation integrity materially affected admissibility, the receipt should bind the relevant provenance references, approval attestations and detector observations used in the result.

Where causal-continuity conformance applies, the receipt should preserve the binding, causal-position or lineage references needed to verify the relationship between evaluation and execution. Where governing contract continuity is material, the receipt should preserve the governing contract reference/version/digest used by the evaluation. Where material constraint completeness affected the result, the receipt should preserve the relevant established/unresolved constraint references or equivalent governed evidence. Wall-clock timestamps remain forensic metadata, not proof of continuity.

Where external verification evidence materially affected admissibility or execution continuity, the receipt or referenced evidence chain should preserve the verifier/issuer identity and the material audience/executor, action/request/parameter, policy/configuration, integrity/trust, freshness and replay/consumption bindings used by the decision.

A receipt for one evaluated action must not be reused as the execution receipt for a materially transformed replacement action unless the replacement has itself received fresh evaluation and a new binding/result.

### 3.9 Causal Execution Continuity

REHT defines a normative execution-continuity profile for independently owned systems.

The canonical invariant is:

> Authorization is not a durable truth. At execution, the system must prove that this is still the thing that was approved.

A conforming implementation must bind the evaluated action to a deterministic execution envelope, re-derive the execution-relevant envelope immediately before consequence, and fail closed on any material mismatch or unproven continuity.

A material post-evaluation action transformation is a mismatch, not a harmless continuation. The transformed action becomes a new candidate and requires fresh evaluation before consequence.

The profile, negative cases and migration semantics are defined in [`docs/CAUSAL_EXECUTION_CONTINUITY.md`](docs/CAUSAL_EXECUTION_CONTINUITY.md).

### 3.10 Persistent State Continuity

Material that persists across a worker, session, model or context boundary must not become operative merely because it is present in a later workspace or context.

If persisted material can influence consequence-bearing work, a conforming implementation must be able to establish the integrity and standing of the exact material exposed to the next worker and bind it to the current governed context. A worker-produced artifact must not silently self-promote into authoritative instructions, policy, memory or evidence for a later worker.

The standard does not prescribe a storage format or admission engine. It requires the semantic boundary: persistence is transport/storage, not authority.

### 3.11 Governing Contract Continuity

If a contract, policy set, mandate or equivalent rule set materially governs a work unit, the exact governing state used for evaluation must be identifiable and continuity-checkable.

A conforming implementation must invalidate reliance on a prior result if a material governing contract is amended, terminated, replaced or otherwise changed before consequence. The old result must not be rebound under the changed contract without fresh evaluation.

The standard does not require the full governing contract to be disclosed to every worker. A deterministic reference/version/digest or equivalent binding is sufficient when it permits independent detection of drift.

See [`docs/STATE_AND_CONTRACT_CONTINUITY.md`](docs/STATE_AND_CONTRACT_CONTINUITY.md).

### 3.12 Constraint Observability and Action Transformation

A conforming implementation must distinguish material execution constraints established for evaluation from material constraints that are known to be required but remain unresolved or unavailable. Known constraint gaps fail closed; they are not silently treated as permissive defaults.

The consequence-bearing path is conceptually:

```text
candidate action -> REHT evaluation -> bound admissibility result -> execution continuity -> consequence -> receipt
```

Only the action bound to the current admissibility result may proceed under that result. A control, policy, orchestration or safety layer may reject an action or propose a modified replacement, but any material revision creates a new candidate that must receive fresh REHT evaluation.

See [`docs/CONSTRAINT_OBSERVABILITY_AND_ACTION_TRANSFORMATION.md`](docs/CONSTRAINT_OBSERVABILITY_AND_ACTION_TRANSFORMATION.md) and proposal #13.

### 3.13 Verification Evidence Binding

External verification receipts and equivalent artifacts are evidence inputs, not bearer authorization.

When such evidence is materially relied upon, a conforming implementation must be able to establish the exact evidence-producing verifier/issuer, intended audience/executor where scoped, exact action/request and material-parameter binding, deterministic policy/configuration binding, integrity/trust basis, applicable freshness and replay/consumption state.

Required evidence fails closed on material mismatch or unproven trust. A cryptographically valid receipt whose authority, delegation, governed state or governing basis has become stale remains non-executable.

See [`docs/VERIFICATION_EVIDENCE_BINDING.md`](docs/VERIFICATION_EVIDENCE_BINDING.md). IETF Internet-Draft `draft-correctover-ccs-01` is an external interoperability reference, not a REHT dependency or authorization authority.

## 4. Portability and anti-lock-in

### 4.1 Neutrality requirement

REHT contracts must remain usable when the surrounding model, agent, workflow engine, tool protocol, runtime, storage layer or infrastructure provider changes.

Implementations must not require users to redefine authority, policy, evidence bindings or execution controls solely because an underlying provider or runtime is replaced.

### 4.2 Portable governed state

A conforming implementation must provide documented, versioned and independently verifiable representations for the governed state it exchanges or persists, including where applicable:

- authority definitions and delegation chains;
- policy references and applicable policy versions;
- governing contract references and versions/digests;
- evidence references and provenance;
- workflow and checkpoint state required to resume governed work;
- persisted material that can influence later consequence-bearing work;
- material constraint requirements and established/unresolved constraint state when relevant to admissibility;
- admissibility results and their input bindings;
- execution-envelope bindings and causal-lineage references where required;
- external verification-evidence issuer/audience/action/configuration/freshness/replay bindings where materially relied upon;
- execution receipts and integrity data;
- persisted learned methods, procedures or workflow adaptations.

The implementation may protect proprietary evaluation logic. It must not use that protection to trap the user's governed records, prevent independent verification or make migration materially dependent on one vendor-specific runtime.

### 4.3 Protocol and infrastructure substitution

Interoperability protocols such as A2A, MCP or future equivalents may transport tasks, tools, messages, artifacts, grants, capabilities or context references. No protocol declaration, agent capability claim, external authorization object, verification receipt or provider-specific object may replace the standard authority, evidence, policy, admissibility or execution-continuity semantics.

Migration or fallback between local, edge, sovereign and cloud infrastructure must preserve the same governed meaning and must not broaden authority, context scope or execution permission.

### 4.4 Independent verification

An external verifier must be able to determine, from the exported contracts and referenced evidence, at least:

- which action was evaluated;
- under which authority and policy;
- which governing contract state applied where material;
- which evidence and governed state were used;
- which material execution constraints were established and which known required constraints remained unresolved where relevant;
- whether persisted material influencing the action retained current standing;
- which admissibility result was produced;
- whether material state, authority or governing-contract changes occurred;
- whether the action presented for execution materially differed from the evaluated action and, if so, whether fresh evaluation occurred;
- whether required causal continuity between evaluation and execution was established;
- whether materially relied-upon external verification evidence matched the required verifier/issuer, audience/executor, action/request/parameter, policy/configuration, integrity/trust, freshness and replay/consumption conditions;
- whether the bound action or evidence was replayed or consumed where applicable;
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
- does not treat persisted material as authoritative solely because it survived a worker/session/context boundary;
- binds consequence-relevant persisted material to current governed context with integrity/standing semantics appropriate to the implementation;
- identifies the governing contract/policy state used for evaluation where material and detects subsequent drift;
- distinguishes established material execution constraints from known required constraints that remain unresolved;
- never returns `ADMISSIBLE` while a known required material execution constraint remains unresolved;
- treats a materially transformed post-evaluation action as a new candidate requiring fresh evaluation;
- does not allow a rewritten, clamped or substituted action to inherit the source action's admissibility result or receipt;
- does not treat wall-clock expiry alone as proof that a prior admissibility remains executable;
- re-establishes required execution-relevant state at the execution boundary;
- fails closed when causal continuity or required receipt continuity cannot be proven;
- rejects stale authority, material state drift, governing-contract drift and replay according to the applicable profile;
- when materially relying on external verification evidence, establishes its required issuer/audience/action/configuration/integrity/freshness/replay bindings and fails closed on material mismatch;
- does not treat cryptographic receipt validity as current authority or execution permission;
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
- a mandatory external verification-receipt format;
- a mandatory workspace, memory or contract storage format;
- certification or legal compliance.

## 7. Versioning

Breaking contract changes require a new major specification version. Substantive additive normative requirements or optional interoperable fields require a minor version. Clarifications and corrections that do not change conformance requirements may use a patch version.

Prerelease drafts use forward-only immutable identifiers such as `MAJOR.MINOR.PATCH-draft.N`. Historical tags are never moved, deleted or retargeted.

This `0.5.0-draft.1` prerelease adds the Verification Evidence Binding profile: materially relied-upon external verification receipts must retain verifier/issuer, audience/executor, exact action/request/material-parameter, policy/configuration, integrity/trust, freshness and replay/consumption bindings, while cryptographic validity remains evidence rather than execution authority. It preserves the v0.4 constraint-observability/action-transformation requirements, the v0.3 persistent-state and governing-contract continuity requirements, and the rule that authorization is non-durable.

Specification versions, reference-package versions and private runtime versions are independent compatibility surfaces and do not need to match numerically.

Canonical runtime-wire schema changes owned by RACS/spec must be changed there and referenced here rather than duplicated.

Normative change governance, proposal classes and transfer-of-canonical-authority rules are defined in [`GOVERNANCE.md`](GOVERNANCE.md).
