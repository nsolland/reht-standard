# REHT Standard Specification

Version: 0.1.0-draft

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

## 3. Core objects

### 3.1 Action Envelope

A complete representation of the proposed action and the context required for evaluation.

Minimum fields:

- specification version
- action identifier
- timestamp
- actor
- action type
- target
- authority context
- evidence references
- policy references
- governance state

### 3.2 Authority Context

Represents who or what proposes the action, the delegation chain and the bounded scope of authority.

### 3.3 Evidence Package

References evidence used during evaluation. Evidence should be attributable, time-bounded and integrity-verifiable where possible.

### 3.4 Policy Context

Identifies the policies, rules or controls applicable to the proposed action.

### 3.5 Governance State

Represents the execution-relevant system state at evaluation time.

Reference states:

- NORMAL
- SAFE
- HALT

### 3.6 Admissibility Result

Reference outcomes:

- ADMISSIBLE
- INADMISSIBLE
- INDETERMINATE
- REQUIRES_STEP_UP
- NO_LONGER_ADMISSIBLE

These outcomes are semantic results, not execution commands.

### 3.7 Continuous Integrity Event

Records a material event that may affect the continuing validity of an admissibility result.

### 3.8 Execution Receipt

Records the evaluated action, result, relevant evidence references, time, state and integrity data.

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
- execution receipts and integrity data;
- persisted learned methods, procedures or workflow adaptations.

The implementation may protect proprietary evaluation logic. It must not use that protection to trap the user's governed records, prevent independent verification or make migration materially dependent on one vendor-specific runtime.

### 4.3 Protocol and infrastructure substitution

Interoperability protocols such as A2A, MCP or future equivalents may transport tasks, tools, messages, artifacts or context references. No protocol declaration, agent capability claim or provider-specific object may replace the standard authority, evidence, policy or admissibility contracts.

Migration or fallback between local, edge, sovereign and cloud infrastructure must preserve the same governed meaning and must not broaden authority, context scope or execution permission.

### 4.4 Independent verification

An external verifier must be able to determine, from the exported contracts and referenced evidence, at least:

- which action was evaluated;
- under which authority and policy;
- which evidence and governed state were used;
- which admissibility result was produced;
- whether material state changes occurred;
- which execution receipt, if any, was bound to the decision.

Independent verification does not require disclosure of proprietary scoring algorithms unless a separate conformance profile requires it.

## 5. Conformance

A conforming implementation:

- accepts or produces versioned Action Envelopes;
- preserves authority, evidence, policy and state references;
- returns one defined admissibility outcome;
- does not represent an indeterminate result as admissible;
- creates a receipt for terminal decisions;
- supports documented export of governed contracts and receipt chains in a provider-independent representation;
- preserves governed meaning when models, agents, protocols or infrastructure are substituted;
- does not technically or contractually block migration of portable governed records;
- does not claim certification solely through schema compatibility.

## 6. Non-goals

This specification does not define:

- model architecture;
- agent reasoning;
- moral truth;
- organizational legitimacy;
- domain policy content;
- proprietary scoring methods;
- production runtime implementation;
- certification or legal compliance.

## 7. Versioning

Breaking contract changes require a new major specification version. Additive optional fields may be introduced in minor versions. Clarifications and corrections may be introduced in patch versions.
