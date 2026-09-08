# Causal Effect Boundary

Status: draft interoperability extension for REHT causal execution conformance v0.6.

## Normative invariant

`NO_DIRECT_EFFECT_PATH` applies to causal trust-boundary crossings, not only direct tool or API execution.

> No externally consequential state transition or causal influence may leave an untrusted computation domain except through a known governed effect boundary.

A conforming deployment MUST treat a crossing as governed whenever information, state, capability, resource demand or another causal signal can affect a different trust domain. Payload type does not create an exemption.

Purely internal computation does not require effect authorization under this invariant while it remains inside the same untrusted domain and creates no external causal influence.

## Required channel inventory

A deployment claiming `NO_DIRECT_EFFECT_PATH` MUST inventory and bind all known consequence-capable crossings, including where applicable:

- direct APIs and service integrations;
- human relay paths;
- agent/workflow/machine relay paths;
- shared state, queues, caches and databases;
- messages, files, artifacts and externally observable logs;
- credentials and actuators;
- externally consequential resource consumption, cost or availability demand; and
- side channels or other observable causal signals.

An unknown or uninventoried trust-boundary crossing MUST fail closed for the affected consequence path. It MUST NOT be presumed harmless.

## Human and agent relay

A human or another agent can be an actuator. If untrusted computation emits action-significant output and the recipient can cause the relevant consequence without the resulting action traversing the governed boundary, the architecture contains an ungoverned effect path.

Human-in-the-Lead therefore means human judgment governs authority; it does not mean a human relay may bypass consequence-time authorization.

## Standing low-risk policy

This invariant does not require bespoke human approval for every byte or every low-risk output. A governed boundary MAY apply standing policy, deterministic classification, bounded authority or other defined rules to permit low-risk crossings. The boundary itself MUST NOT be bypassed by labelling a channel harmless upstream.

## Enforcement scope

REHT evaluates fresh exact-action authority at a consequence boundary. REHT alone cannot physically eliminate network, process, credential, human or side-channel bypasses. A production `NO_DIRECT_EFFECT_PATH` claim is therefore bounded to the channels and trust boundaries that are actually inventoried and enforced by the surrounding Gateway/PEP, runtime and infrastructure.

Conformance proves that bypass conditions are rejected. Deployment evidence must prove that the claimed inventory corresponds to real reachable effect paths.

## Required negative cases

`conformance/causal-execution-v0.6.json` adds refusal cases for:

- direct API bypass;
- human relay bypass;
- agent relay bypass;
- shared-state bypass;
- message/file/artifact bypass;
- credential/actuator bypass;
- resource-consumption bypass;
- side-channel bypass; and
- unknown/uninventoried boundary crossings.

These are additional to the existing causal-continuity, authority, state, receipt, replay, contract, constraint, substrate and verification-evidence cases.
