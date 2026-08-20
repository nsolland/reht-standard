# Verification Evidence Binding Profile

Version: 0.5.0-draft.1

Status: normative REHT profile.

## 1. Purpose

This profile defines how REHT treats receipts or equivalent verification evidence produced by an external verifier, policy layer, agent runtime or other independently owned component.

Such evidence may inform execution authorization. It does not itself create authority or force an admissibility outcome.

## 2. Core invariant

A cryptographically valid receipt proves only that the identified verifier produced the bound evidence under the bound verification context.

It does not prove that:

- the verifier was authorized to create execution authority;
- the principal still holds authority;
- delegation remains valid;
- the governing policy or contract remains current;
- the action presented for consequence is unchanged;
- the governed state still permits consequence.

The canonical distinction is:

> cryptographic validity != authority validity != execution authorization

REHT therefore treats external verification receipts as governed evidence that must remain bound to the current execution context and must pass the ordinary execution-time authority and continuity checks.

## 3. Required bindings

When an external verification receipt is materially relied upon for a consequence-bearing action, the relying REHT profile MUST be able to establish, directly or through integrity-verifiable references:

1. verifier/issuer identity;
2. intended relying executor or audience, when the evidence is scoped to a consumer;
3. exact action/request identity and all parameters material to consequence;
4. deterministic policy/configuration identity, version, digest or equivalent binding for the verification state that produced the evidence;
5. integrity of the receipt or evidence object and the trust basis for the signing or verification key where cryptographic verification is used;
6. freshness metadata required by applicable policy;
7. replay/consumption state for evidence that is single-use or consumption-bound.

The implementation MAY use issuer URIs, audience identifiers, nonces, monotonic sequences, canonical configuration digests, request hashes, parameter hashes, key identifiers or equivalent interoperable mechanisms. This standard does not require one external receipt format.

## 4. Execution-time treatment

A matching receipt binding permits the evidence to remain admissible as an input. It does not make the governed action executable by itself.

Immediately before consequence, the execution boundary MUST still re-establish the execution-relevant action, authority, delegation, governed state, governing basis and material constraints required by the applicable REHT profile.

An unexpired freshness window MUST NOT override a causally intervening revocation, authority mutation, policy/contract change, action transformation or other material state change.

## 5. Fail-closed conditions

External verification evidence is non-reliable for the current execution when any required material binding cannot be established, including:

- issuer/verifier mismatch;
- untrusted, substituted or no-longer-accepted signing/verification key;
- intended audience/executor mismatch;
- action, request or material parameter mismatch;
- governing policy/configuration mismatch;
- required freshness failure;
- replayed nonce/sequence or prior consumption where single-use semantics apply;
- broken integrity or signature verification;
- cryptographically valid evidence whose underlying authority or governed state is stale.

Where the missing or mismatched evidence is required for admissibility, the action MUST NOT execute under the affected result.

## 6. Relationship to external receipt specifications

External receipt formats may be mapped into this profile without becoming REHT dependencies.

IETF Internet-Draft `draft-correctover-ccs-01` is one interoperability reference because it specifies request, parameter, runtime-context, issuer, audience, nonce/sequence, freshness and canonical-configuration bindings around a verifier receipt.

REHT intentionally does not adopt CCS verdict semantics as REHT outcomes. A CCS-style ALLOW/DENY/ESCALATE record is evidence about a verifier decision. REHT retains its own authority, admissibility and execution-continuity semantics.

See [`CCS_RECEIPT_BINDING_CONVERGENCE.md`](CCS_RECEIPT_BINDING_CONVERGENCE.md).
