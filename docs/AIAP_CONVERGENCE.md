# Causum AI Agency Protocol (AIAP) — REHT convergence note

Status: adopted external convergence reference; non-normative interoperability guidance.

Source reviewed: Causum AIAP v0.1 public specification page, 2026-08-20.

AIAP status note: the public page describes v0.1 as a working draft and proprietary for production use. Reading, studying, prototyping, conformance testing and internal assessment are permitted without a production operating license. REHT therefore treats AIAP as an optional interoperability reference, never as a strategic dependency.

## Why it matters

AIAP makes several distinctions that strongly converge with REHT/VALO execution-governance semantics:

- identity is persistent;
- capability describes what an agent could technically do;
- autonomy describes operating independence;
- authority describes what a principal has delegated;
- agency describes what authority may legitimately be exercised now toward a purpose.

AIAP then represents agency as a scoped, expiring, revocable grant mediated by a broker. It supports direct short-lived credentials, broker-mediated execution where the agent never receives credentials, and attenuating sub-agent delegation.

This converges with REHT on the separation of capability from authority, purpose-bound delegation, temporal validity, revocation, monotonic attenuation and pre-effect governance.

## REHT distinction

REHT does not adopt an agency grant as sufficient execution authority.

An external AIAP grant is evidence of a claimed, bounded authority/agency state. REHT still resolves the exact proposed action against fresh governed state and current Authority State immediately before consequence.

A cryptographically valid or behaviorally justified AIAP grant MUST NOT override:

- revocation or suspension;
- changed purpose or mandate;
- exhausted or consumed authority;
- stale World, Consequence, Epistemic or Capability State;
- exact-effect/adapter mismatch;
- missing required evidence or unresolved coverage debt;
- a non-ALLOW REHT/RACS decision.

## Adopted learning

### 1. Authority composition is intersectional, never additive

AIAP defines effective session policy as the intersection of role policy, use-case template and request, never their union.

REHT adopts the general invariant:

`EFFECTIVE_AUTHORITY_IS_INTERSECTION`

When multiple independent authority, policy, scope or delegation constraints apply to the same action, composition MUST NOT widen the permissible set. The effective execution scope is the deterministic intersection of applicable ceilings/constraints unless an authoritative rule explicitly defines otherwise.

This is stronger and more general than delegation attenuation alone because it covers composition across independent policy/scope sources, not only parent-child delegation.

### 2. Behavior may justify autonomy, but cannot manufacture authority

AIAP separates a normative ceiling from temporal justification derived from observed behavior. Positive behavior can move an agent within the ceiling, but cannot raise the ceiling itself.

REHT adopts:

`EVIDENCE_CANNOT_RAISE_AUTHORITY_CEILING`

Observed success, reliability, reputation, historical compliance, model confidence, accumulated learning or low incident rates MAY influence risk, autonomy budget, review intensity or evidence confidence. They MUST NOT create authority, widen delegated scope or exceed the current normative/authority ceiling.

This preserves the distinction:

capability/reliability/autonomy evidence != authority.

### 3. Credential non-possession is a stronger containment mode

AIAP's mediated level lets the broker execute on the agent's behalf so the agent never receives the underlying credential.

REHT adopts this as a preferred containment profile for consequence-bearing execution where feasible:

`EFFECTOR_EXCLUSIVE_CREDENTIALS`

The strongest deployment mode keeps consequence-bearing credentials/capabilities at the governed PEP/effector boundary rather than in the agent/harness. Short-lived JIT credentials remain an interoperability option, but possession by the agent is a weaker containment class and MUST NOT create a direct effect path around REHT/RACS/PEP.

### 4. Grants should decay unless continuity is actively justified

AIAP includes expiry, revocation and heartbeat semantics so authority does not persist silently.

REHT adopts the underlying continuity rule, not the specific heartbeat wire message:

`NO_SILENT_AUTHORITY_PERSISTENCE`

Where an authority/agency lease is time-bounded or continuity-dependent, expiration or missing required freshness/continuity evidence MUST cause revalidation or fail closed. A heartbeat MAY provide liveness evidence, but liveness alone never proves authority or admissibility.

### 5. Obligations belong in the governed envelope

AIAP includes obligations alongside principal, goal, purpose, actions, resources, context, temporal boundary and delegation constraints.

REHT treats ongoing obligations as first-class constraints/evidence where applicable. Obligations that must remain true during execution become Continuous Integrity inputs and can invalidate a pending or continuing action when breached.

## AIAP adapter profile

An optional AIAP -> REHT adapter MAY ingest an `AGENCY_GRANT` / session representation and preserve, where available:

- principal / on-behalf-of identity;
- agent identity;
- goal and purpose;
- authorized actions;
- resource scope;
- contextual constraints;
- temporal bounds;
- delegation constraints and lineage;
- obligations;
- agency level / credential-containment mode;
- decision identifier and governance-check evidence;
- revocation / lifecycle / heartbeat evidence;
- signed decision evidence.

Mapping ownership:

- identity -> identity evidence only;
- capability/agency level -> Capability State / containment evidence;
- principal/delegation/purpose/scope -> Authority Evidence inputs;
- obligations/context/expiry -> current-state and Continuous Integrity constraints;
- signed decisions -> Veritas evidence;
- final execution authorization -> REHT only;
- deterministic outcome -> RACS;
- consequence-bearing effect -> governed PEP/Gateway only.

The adapter MUST fail closed when required lineage, scope, purpose, validity or revocation state cannot be resolved.

## Interoperability messages

AIAP lifecycle messages can be mapped without importing AIAP as an internal authority model:

- `AGENCY_REQUEST` -> proposed authority/capability request evidence;
- `AGENCY_GRANT` -> bounded external authority/agency evidence;
- `AGENCY_DENY` -> external denial evidence;
- `AGENCY_EXECUTE` -> proposed exact effect at the governed boundary;
- `AGENCY_RESULT` -> external execution/result evidence, subject to outcome verification;
- `AGENCY_REVOKE` -> revocation evidence requiring immediate current-state invalidation;
- `AGENCY_HEARTBEAT` -> liveness/continuity evidence only.

No AIAP message self-authorizes a REHT-governed effect.

## Conformance implications

AIAP strengthens the case for explicit tests covering:

1. EFFECTIVE_AUTHORITY_IS_INTERSECTION — two valid scopes cannot compose into a broader scope;
2. EVIDENCE_CANNOT_RAISE_AUTHORITY_CEILING — perfect historical behavior cannot authorize an action outside current authority;
3. EFFECTOR_EXCLUSIVE_CREDENTIALS — mediated mode exposes no consequence-bearing credential to the agent and no bypass path exists;
4. NO_SILENT_AUTHORITY_PERSISTENCE — expired or continuity-invalid grants fail closed;
5. REVOCATION_BEFORE_EFFECT — revocation after grant but before consequence invalidates execution;
6. OBLIGATION_CONTINUITY — breached material obligations invalidate continuing/pending execution when action-relevant;
7. existing CURRENT_AUTHORITY_AT_COMMIT, NO_DIRECT_EFFECT_PATH, EXACT_EFFECT_BINDING, MATERIAL_STATE_CHANGE_INVALIDATES_CLEARANCE and EVERY_EFFECT_HAS_A_CHAIN invariants remain authoritative.

## What REHT should not copy

- Do not replace exact-action consequence-time authorization with session/grant authorization.
- Do not treat observed behavior as a source of authority.
- Do not require AIAP's proprietary production protocol or broker implementation.
- Do not collapse identity, capability, autonomy, authority and admissibility into one trust score.
- Do not treat heartbeat/liveness as proof that a grant remains legitimate.

## Strategic conclusion

AIAP validates a market shift from static IAM/tool permissions toward purpose-bound, revocable, time-bounded agent authority.

The useful adoption is narrower and stronger: deterministic authority intersection, authority-ceiling preservation, credential non-possession, no silent persistence and explicit ongoing obligations.

REHT remains the consequence-time authorization boundary against fresh governed state; AIAP is an optional external authority/agency evidence format.
