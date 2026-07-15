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

## 4. Conformance

A conforming implementation:

- accepts or produces versioned Action Envelopes;
- preserves authority, evidence, policy and state references;
- returns one defined admissibility outcome;
- does not represent an indeterminate result as admissible;
- creates a receipt for terminal decisions;
- does not claim certification solely through schema compatibility.

## 5. Non-goals

This specification does not define:

- model architecture;
- agent reasoning;
- moral truth;
- organizational legitimacy;
- domain policy content;
- proprietary scoring methods;
- production runtime implementation;
- certification or legal compliance.

## 6. Versioning

Breaking contract changes require a new major specification version. Additive optional fields may be introduced in minor versions. Clarifications and corrections may be introduced in patch versions.