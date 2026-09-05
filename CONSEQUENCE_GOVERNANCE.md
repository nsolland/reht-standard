# Consequence Governance and REHT

## Canonical category

**Consequence Governance** is the governance category for deciding whether an exact proposed consequence may legitimately become real under the authority, evidence and conditions that exist at consequence time.

Canonical definition: https://valoresearch.org/consequence-governance.html

The governing object is the proposed consequence, not the worker. The proposer may be an AI agent, person, workflow, API, device or another machine.

## Where REHT fits

REHT is a public, model-agnostic standard for consequence-time authorization at the execution boundary.

It asks:

> Is this exact action still admissible to execute now, under the authority, state, constraints, evidence and governing basis that actually exist at consequence time?

REHT is therefore a standards/conformance layer within the broader Consequence Governance category. It does not redefine the whole category and does not govern agents as such.

## Canonical taxonomy

- **Consequence Governance** — top-level category.
- **Governed Effect Path** — architecture through which consequence-bearing effects must pass.
- **NO_DIRECT_EFFECT_PATH** — invariant prohibiting consequence-bearing effects from bypassing the governed path.
- **Consequence-time authorization** — fresh exact-action authorization immediately before effect.
- **Execution Authorization Infrastructure** — infrastructure that evaluates current authority, state, scope, purpose, constraints and evidence for the proposed consequence.
- **Governed Contract** — worker-neutral definition of legitimate purpose, mandate, scope, constraints, required evidence and correct completion.
- **RACS** — deterministic decision/action binding contract used to carry a governance decision to enforcement.
- **Gateway / PEP** — enforcement boundary.
- **Veritas / receipts** — evidence layer preserving evaluated state, decision and resulting consequence.
- **Trusted Execution** — evidenced downstream outcome of a permitted consequence passing through the governed path.

## Boundary distinctions

Consequence Governance is not identical to agent governance, access control, workflow governance, observability or generic execution control.

- Agent governance governs workers, identities, tools and runtime behavior.
- Access control governs whether a subject can access a resource.
- Workflow governance governs process and orchestration.
- Observability records what happened.
- Consequence Governance governs whether this exact proposed effect may legitimately become real now.

## Core invariants

- capability is not authority
- access is not authorization
- prior approval is not necessarily current authority
- conformance is not authorization
- unknown remains unknown
- no direct effect path
- fresh authority is resolved at consequence time
- consequential effects require evidence binding

## Related canonical resources

- Consequence Governance: https://valoresearch.org/consequence-governance.html
- Governed Effect Path: https://valoresearch.org/governed-effect-path.html
- Consequence-time authorization: https://valoresearch.org/consequence-time-authorization.html
- Execution Authorization Infrastructure: https://valoresearch.org/execution-authorization-infrastructure.html
- Governed Contract: https://valoresearch.org/governed-contract.html
- NO_DIRECT_EFFECT_PATH: https://valoresearch.org/no-direct-effect-path.html
- Trusted Execution: https://valoresearch.org/trusted-execution.html
- REHT product/developer surface: https://reht.valoresearch.org/

This document is explanatory and does not supersede the normative REHT specification or conformance requirements in this repository.
