# REHT Economic Authority Profile v0.1

Status: normative proposal under issue #18; target REHT specification `0.5.0-draft.1`.

## 1. Purpose

The REHT Economic Authority Profile defines how existing REHT execution-authorization semantics apply to economic actions such as payments, treasury operations, settlement instructions, procurement commitments, refunds, lending draws, asset transfers and other consequence-bearing actions that consume or move organizational resources.

This profile does not create a payment protocol, identity protocol, wallet, bank rail or new authority model. It constrains how current organizational authority must be materialized, evaluated, bound and revalidated before an economic consequence becomes irreversible.

The profile is rail-agnostic and worker-agnostic.

## 2. Architectural boundary

The canonical execution path is:

```text
Authoritative state / Kernel
  -> governed execution context / workspace
  -> candidate economic action
  -> VAIG evaluation where applicable
  -> REHT fresh execution authorization
  -> RACS deterministic decision/action binding
  -> external PEP / bounded Gateway
  -> execution rail
  -> execution and outcome receipts / Veritas
```

No layer may infer authority from model output, tool availability, capability registration, schema validity, possession of a credential, prior approval, persisted context or successful execution.

REHT is the authorization boundary. RACS does not evaluate authority and does not authorize execution. The execution rail does not establish organizational mandate.

## 3. Canonical object ownership

This profile MUST NOT introduce parallel runtime-wire objects for concepts already owned elsewhere.

### 3.1 Authority semantics

Organizational authority is represented by the governing implementation's authoritative state model. In the VALO reference architecture, Kernel `Authority` is the semantic source for:

- `authority_id`;
- `principal`;
- `capability`;
- resource `scope`;
- `constraints`;
- legal or organizational `basis`;
- `validity`;
- delegation permission;
- revocation state and references.

The profile does not require Kernel as a dependency for independent implementations. It requires equivalent semantics to be explicit, current and independently verifiable.

### 3.2 Delegation semantics

Delegation MUST be derived from established authority and MUST only narrow or carry forward that authority.

In the VALO reference architecture, Kernel `Delegation` supplies the semantic fields for delegator, delegate, authority reference, scope reduction, purpose restriction, validity, conditions and revocation.

A delegation chain MUST NOT:

- add a capability not present in its parent authority;
- widen resource scope;
- relax an amount, counterparty, currency, jurisdiction, purpose, time or equivalent constraint;
- outlive the authority from which it derives;
- remain executable after a causally prior revocation.

Where a runtime materializes a narrowed task authority from a delegation chain, the materialized authority MUST be traceable to the complete chain and MUST NOT become a new independent source of authority.

### 3.3 Purpose semantics

Purpose is first-class governance state, not descriptive metadata.

In the VALO reference architecture, Kernel `Purpose` supplies the semantic fields for purpose identity/type, scope, basis, permitted data, permitted actions and validity.

When purpose is required by the applicable action class, policy, impact level or authority grant, REHT MUST establish that:

- the exact purpose is current;
- its basis is present;
- the action type is permitted;
- the target is within purpose scope;
- the authority is explicitly compatible with or bound to that purpose.

### 3.4 Runtime wire contracts

Canonical execution-governance wire artifacts are owned by RACS. This profile references rather than redefines, where applicable:

- `AuthorityGrant`;
- `DelegationChain`;
- `ActionEnvelope`;
- `GovernanceEvaluation`;
- `AdmissibilityDetermination`;
- `GovernanceClearance`;
- `CoreExecutionPermit`;
- `CommitToken`;
- `RevocationEvent`;
- `ContinuousIntegrityEvent`;
- `ExecutionReceipt` and downstream receipt types.

RACS canonicalization, digest, signature-envelope and cross-artifact binding rules remain the source of truth for those artifacts.

## 4. Economic action candidate

An economic action is represented through the canonical RACS `ActionEnvelope` or an equivalent implementation binding that preserves the same governed meaning.

The exact candidate MUST identify or deterministically bind, as applicable:

- actor and principal;
- action type;
- target / account / resource / counterparty;
- requested effect;
- amount and currency or equivalent resource quantity;
- purpose;
- authority and delegation references;
- applicable policy and evidence;
- governing state / state reference;
- connector or execution capability;
- replay identity / nonce;
- consequence and reversibility classification;
- material constraints and unresolved constraint state.

Agent-produced traces, plans, tool histories or self-attestations MAY be carried as evidence. They MUST NOT be treated as authoritative state or as proof of mandate solely because the agent produced them.

Any material change to amount, currency, counterparty, target, account, purpose, connector request, payload or other consequence-bearing field creates a new candidate action and requires fresh evaluation.

## 5. Fresh authority evaluation

Before an economic action may progress toward consequence, REHT MUST evaluate the exact candidate against current authoritative state.

A conforming profile implementation MUST fail closed unless it can establish all authority-relevant bindings required for the action, including where applicable:

1. verified execution identity;
2. current principal/actor relationship;
3. active authority for the required capability;
4. target/resource within scope;
5. all applicable constraints satisfied;
6. narrowing-only delegation continuity;
7. current purpose binding when required;
8. current evidence and policy state when required;
9. causal continuity with the governed state over which the action is evaluated;
10. replay protection;
11. required approval/gate evidence without treating the gate itself as authority;
12. resource bounds for actions that consume bounded economic capacity.

Wall-clock validity MAY constrain authority, but an unexpired timestamp alone is not proof that authority remains executable.

## 6. Outcome semantics

This profile does not create a new decision vocabulary.

The public REHT admissibility outcomes remain those defined by the REHT specification. Runtime implementations may bind those semantics into their existing decision contracts. The current VALO REHT reference implementation emits deterministic `ALLOW` or `DENY` for implemented conditions while the surrounding decision-contract plane supports `ALLOW`, `MODIFY`, `DEFER`, `DENY`, `STEP_UP` and `HALT`.

RACS merely represents and binds the governance result. A RACS `GovernanceEvaluation`, schema-valid artifact or favorable upstream evaluation is never execution authorization by itself.

## 7. Clearance and commitment

This profile does not define a separate `BindingCommitment` object.

A successful REHT authorization MUST be carried through the canonical RACS execution chain appropriate to the implementation profile. The reference chain is:

```text
AdmissibilityDetermination
  -> GovernanceClearance
  -> CoreExecutionPermit
  -> CommitToken
  -> bounded connector / PEP
  -> ExecutionReceipt
```

The artifacts MUST bind the exact action and current authority context strongly enough that a permit for action A cannot execute action B.

A clearance, permit or token is not durable authority. Before consequence, the enforcement boundary MUST establish the current validity required by the applicable profile.

## 8. Revocation and authority drift

Revocation and material authority drift dominate any non-terminal approval, clearance, permit, token or active continuation.

If a relevant revocation or authority mutation causally intervenes before terminal consequence, the action MUST NOT proceed under the prior authorization.

A short `valid_until` interval is a maximum validity bound, not a grace period that defeats a causally prior revocation.

The reference VALO Gateway behavior is aligned with this invariant: it revalidates active authority, clearance validity, workspace/substrate validity where applicable, exact action bindings and single-use permit state at the execution boundary.

## 9. Replay and consumption

Economic authorization MUST be replay-resistant.

Where the execution profile uses a single-use permit, token, reservation or nonce:

- the identity MUST be unique within its replay domain;
- consumption MUST be durable before or atomically with consequence as required by the connector profile;
- a consumed identity MUST NOT authorize a second consequence;
- retry behavior MUST distinguish a repeated observation/request from a new economic action.

Idempotency at an execution rail does not create authority and does not replace REHT replay protection.

## 10. Sensitive authority state

The worker or agent does not need access to the complete authoritative state used for evaluation.

A conforming implementation SHOULD minimize disclosure of sensitive authority state and SHOULD obtain execution-relevant authoritative state independently of worker-controlled assertions where practical.

This is a security property, not a transport mandate: the profile does not require the REHT component itself to call every source system. A trusted governed context may materialize the required state before deterministic REHT evaluation, provided freshness, provenance and continuity remain verifiable.

## 11. Rail neutrality

The profile may be used with bank APIs, card networks, treasury systems, settlement networks, blockchains, internal ledgers or future execution rails.

An execution rail adapter MUST NOT:

- widen authority;
- reinterpret a denied or non-executable action as executable;
- substitute a materially different transaction under an existing clearance;
- bypass required RACS/REHT bindings;
- treat rail-specific credentials or tokens as proof of organizational authority unless the governing authority model independently establishes that meaning.

Rail-specific authentication and fraud controls are complementary controls, not substitutes for REHT execution authorization.

## 12. Evidence and causal ordering

Economic execution evidence MUST preserve enough information to reconstruct which action was evaluated, under which authority, using which relevant state, and what consequence occurred.

The profile does not require or claim a global total order across institutions.

Where independently owned systems participate, causal lineage, issuer/log-local sequence, replay identity, cross-artifact digests and receipt-chain references SHOULD be used to establish continuity. Wall-clock timestamps remain useful forensic metadata.

## 13. Liability and legal effect

This profile does not assign legal liability between principals, state providers, REHT operators, execution rails or other parties.

Protocol evidence may support attribution and dispute resolution, but legal responsibility depends on applicable contracts, law, regulation and facts outside the protocol.

Implementations MUST NOT represent REHT conformance as a legal determination that an action is valid, enforceable or compliant in every jurisdiction.

## 14. Required conformance behavior

An implementation claiming `reht.economic-authority.v0.1` MUST pass the published positive control and MUST fail closed for the negative cases in `conformance/economic-authority-v0.1.json`.

At minimum, the implementation MUST reject or require fresh authorization when:

- delegation expands parent authority;
- authority is stale, expired or revoked at execution;
- required purpose is absent, inactive or mismatched;
- the consequence-bearing action differs materially from the authorized action;
- a single-use authorization identity is replayed;
- agent self-report is used as the sole source of authority;
- a favorable RACS/upstream evaluation is treated as execution authorization;
- revocation occurs before terminal consequence;
- an execution rail attempts to bypass the governed effect path;
- an economic limit or resource bound would be exceeded or widened.

## 15. Compatibility

This is an additive optional profile. Existing REHT `0.4.x` implementations remain conformant to their declared profile unless they claim Economic Authority Profile conformance.

The profile is designed to reuse existing VALO Kernel, REHT, RACS and Gateway semantics. Independent implementations may use different internal components if they preserve the normative boundaries and interoperable meanings defined here.
