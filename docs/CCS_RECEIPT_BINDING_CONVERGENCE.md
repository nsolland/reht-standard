# Correctover CCS — REHT receipt-binding convergence

Status: external convergence reference and normative-change rationale.

Source: IETF Internet-Draft `draft-correctover-ccs-01`, Correctover Conformance Shape (CCS): A Receipt and Binding Specification for Agent Runtime Verification, published 2026-08-05.

Canonical source: https://www.ietf.org/ietf-ftp/internet-drafts/draft-correctover-ccs-01.html

## What CCS contributes

CCS specifies a tamper-evident receipt for an agent-runtime verification decision. Its useful contribution to REHT is not a new authorization model. It is a precise set of bindings around evidence produced before or around a tool invocation.

Relevant CCS bindings include:

- exact request binding;
- exact parameter binding;
- runtime-context binding;
- action identity binding;
- verifier/issuer identity;
- intended consumer/audience identity;
- canonical configuration and policy-version binding;
- nonce/sequence replay resistance;
- issued-at/expires-at freshness metadata;
- cryptographic integrity over the verification context.

CCS explicitly states that it is not an authorization framework. A CCS receipt records what a verifier decided under a particular request, context and configuration. A downstream enforcement boundary still decides whether that evidence is acceptable for execution.

## REHT interpretation

REHT therefore treats a CCS-style receipt as evidence, never as durable execution authority.

The important distinction is:

> cryptographic receipt validity != authority validity != execution authorization

A receipt may be cryptographically valid while the authority, delegation, policy, governed state or material execution constraints have changed. A conforming REHT boundary must still establish current execution validity immediately before consequence.

CCS freshness windows are useful evidence and policy inputs, but an unexpired receipt is not sufficient proof of continuity. A causally intervening revocation or state change still invalidates execution.

## Adoption decision

Adopt the following interoperability semantics into REHT where receipts or external verification evidence are relied upon:

1. Bind the exact evidence-producing verifier/issuer identity.
2. Bind the intended relying executor or audience when evidence is scoped to a consumer.
3. Bind the exact canonical policy/configuration state used to produce the evidence by deterministic digest or equivalent reference.
4. Bind evidence to the exact action/request and material parameters.
5. Require replay protection for single-use or consumption-bound evidence using nonce, sequence, consumption state or an equivalent mechanism.
6. Preserve freshness metadata while retaining REHT's stronger execution-time continuity rule.
7. Reject evidence when issuer, audience, action/request binding, configuration binding, signature/key trust, freshness or replay state does not match the current governed execution context.

Do not adopt CCS verdicts as REHT outcomes and do not allow CCS evidence to bypass REHT authority resolution or the governed effect boundary.

## Conformance implications

The negative conformance surface should explicitly cover:

- wrong intended audience/executor;
- untrusted or substituted verifier/issuer key;
- policy/configuration digest mismatch;
- request/action/parameter mismatch;
- stale or expired evidence where freshness is required;
- replayed nonce/sequence or previously consumed evidence;
- cryptographically valid evidence whose underlying authority or governed state is no longer current.

These cases strengthen receipt/evidence integrity without changing the canonical REHT rule: execution validity is re-established at the execution boundary, and evidence cannot create authority that the governed state does not currently provide.
