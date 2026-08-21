# Credential-Delivery Interoperability Profile (reht-standard #5)

Status: DRAFT. Provider-neutral portable profile for **clearance-bound credential
delivery and sender-constrained execution**.

## Purpose

Let an implementer map a REHT clearance to credential delivery **without
depending on VALO runtime internals**. The profile is a portable envelope that
binds the exact clearance, the exact action, the exact payload, the workload,
the target, proof of possession, validity and receipt requirements. It
complements — it does not replace — `ExecutionEnvelopeV1`.

## Normative sources

- `nsolland/Racs#90` — clearance-bound credential delivery and lease artifacts
  (normative; `capability-credential-v0.2.schema.json` binds
  `clearance_ref`/`clearance_digest`/`credential_delivery`).
- `draft-hartman-credential-broker-4-agents-00` (IETF Internet-Draft) — treated
  as an **informative** implementation reference only. No IETF standard
  conformance is claimed; its authorization model is NOT normative for REHT.
- `contracts/execution-envelope-v1.schema.json` — existing contract (unchanged).

## Portable envelope (`credential-delivery-interop-v1.schema.json`)

Required bindings:

| Group | Fields | Meaning |
|-------|--------|---------|
| clearance | `clearance_id`, `clearance_digest` | binds the REHT clearance |
| action | `action_ref`, `payload_digest` | binds the exact action + exact payload |
| workload/target | `workload_ref`, `target_ref` | sender-constrained execution scope |
| possession | `confirmation_key_thumbprint` | proof of possession (key id only, never the key) |
| principals | `principal_id`, `executor_id` | who + who executes |
| purpose | `purpose_ref` | bound purpose |
| validity | `issued_at`, `expires_at`, `nonce` | time-bounded, single-use nonce |
| receipts | `receipt_requirements` | usage + execution receipts required |
| narrowing | `scope_narrowing` (optional) | scope can only narrow |

## Rules (I1–I7)

1. **I1 — clearance-bound.** The envelope always carries the exact clearance id
   and digest. A credential without a clearance binding is not deliverable.
2. **I2 — exact effect.** `action_ref` + `payload_digest` pin the exact effect;
   payload mutation or a changed authority/delegation/policy/context digest
   invalidates the envelope.
3. **I3 — validity containment.** `expires_at` must not exceed the clearance
   validity; renewable or unbounded leases are forbidden.
4. **I4 — proof of possession.** `confirmation_key_thumbprint` references the
   key by thumbprint only; a missing thumbprint fails validation.
5. **I5 — secret prohibition.** Secret material (token, secret, password,
   api_key, bearer, private_key, credential_value) is **structurally
   prohibited** by the schema (`propertyNames` + `additionalProperties: false`).
6. **I6 — receipts.** Usage receipts bind to the exact request digest;
   execution receipts are required; a credential receipt MUST NOT be used as a
   GovernanceClearance.
7. **I7 — narrow only.** Scope can only narrow from the clearance (optional
   `scope_narrowing`); widening is rejected.

## Rejections

Validation rejects: payload mutation, changed authority/delegation/policy/
context digest, validity beyond clearance, renewable/unbounded lease, missing
confirmation-key thumbprint, token/secret value in any portable artifact, usage
receipt not bound to exact request digest, missing execution receipt, credential
receipt used as GovernanceClearance, and CB4A Task Request Envelope treated as
authority.

## Conformance

A conforming implementation:

- validates against `credential-delivery-interop-v1.schema.json`
  (Draft 2020-12, strict unknown-field rejection, canonical digest stability);
- maps REHT clearance → credential delivery without VALO runtime internals;
- adds no IAM / OAuth / identity-provider / credential-vault semantics to REHT;
- treats RACS as the normative artifact contract for the runtime implementation;
- does not change REHT decision semantics.

## Tests

- JSON Schema Draft 2020-12 validation;
- strict unknown-field rejection;
- canonical digest stability;
- positive and negative vectors;
- cross-reference and expiry containment checks;
- secret-field/name/value rejection tests;
- mapping compatibility with `Racs#90` schemas;
- existing REHT Standard conformance suite remains green.