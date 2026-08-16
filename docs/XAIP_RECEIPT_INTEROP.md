# XAIP receipt interoperability

Status: additive interoperability profile. It does not change REHT admissibility semantics, RACS decision semantics, the governed effect path or canonical receipt ownership.

External reference: `draft-xkumakichi-xaip-receipts-03`, *Signed Execution Receipts for AI Agent Tool Calls (XAIP Receipts)*, published 2 July 2026 as an Informational Internet-Draft and therefore work in progress.

## Position

REHT adopts XAIP `formatVersion: "1"` as an external receipt wire-format target where interoperability is useful.

XAIP is not the authoritative REHT/RACS receipt and MUST NOT become an authorization, policy, scoring, state, clearance or effect-occurrence authority.

The ordering remains:

```text
current governed state + authority
        -> REHT
        -> deterministic RACS artifact
        -> governed effect boundary
        -> canonical execution/outcome evidence
        -> optional XAIP projection
```

A standalone XAIP projection is intentionally narrower than the canonical REHT/RACS evidence chain. Lossless REHT preservation therefore requires retaining the canonical source receipt and, where the XAIP projection must be independently correlated to it, producing the signed REHT-XAIP binding defined in `schemas/xaip-reht-binding-v1.schema.json`.

## XAIP fields adopted

A strict REHT interoperability producer emits only the XAIP v1 members:

- `formatVersion`
- `agentDid`
- `callerDid`
- `toolName`
- `taskHash`
- `resultHash`
- `success`
- `latencyMs`
- `failureType`
- `timestamp`
- `signature`
- optional `callerSignature`
- optional `toolMetadata`

The signed XAIP canonical payload contains exactly:

```text
agentDid
callerDid
failureType
formatVersion
latencyMs
resultHash
success
taskHash
timestamp
toolName
```

`signature`, `callerSignature` and `toolMetadata` are excluded from that payload.

REHT's strict profile rejects unknown top-level XAIP members rather than allowing an implementation to accidentally treat unsigned extension data as governed evidence.

## Canonicalization and cryptography

For XAIP v1 interoperability:

1. The signed payload is canonicalized with JCS / RFC 8785.
2. The UTF-8 bytes of that canonical JSON are signed with Ed25519.
3. `taskHash` and `resultHash` are lowercase 64-character SHA-256 hex strings.
4. Text inputs/outputs hash their raw UTF-8 content bytes.
5. Structured JSON inputs/outputs hash the UTF-8 bytes of their JCS canonical form.
6. Absent input/output and JSON `null` use the SHA-256 empty-input sentinel.
7. A successful call has `failureType: ""`; a failed call has a non-empty failure type.
8. Signature validity does not override structural invalidity. Malformed receipts fail closed.

Implementations MUST NOT assume that an existing REHT/RACS `payload_digest` or `response_digest` can be copied into XAIP. They may be reused only when the producer can prove that the digest was computed over exactly the XAIP v1 preimage profile.

## Mapping from governed execution evidence

The mapping is a projection, not a replacement contract:

- `agentDid` maps to the execution actor identity admitted for the effect.
- `callerDid` maps to the delegating caller identity; where no delegation exists XAIP permits it to equal `agentDid`.
- `toolName` maps to a stable callable/capability identifier. Tool version and manifest identity remain separately governed.
- `taskHash` commits to the actual tool input under the XAIP v1 preimage profile.
- `resultHash` commits to the actual tool output, failure description or empty-output sentinel under the XAIP v1 preimage profile.
- `success` is technical execution success, not proof of authorization, policy satisfaction, business correctness or outcome truth.
- `latencyMs` is the execution duration required by XAIP.
- `failureType` maps to `timeout`, `validation`, `error` or a deployment extension when the call failed.
- `timestamp` maps to execution completion time.
- `signature` is the executor/agent signature over the XAIP canonical payload.
- `callerSignature`, when present, is the caller co-signature over the same XAIP canonical payload.

A caller co-signature establishes attribution to the same signed record. It does not by itself prove that the caller independently observed the result, that the execution occurred correctly, or that either signer had current REHT authority.

## REHT-XAIP binding

XAIP v1 does not provide signed fields for REHT-specific receipt identity, authority state, deterministic decision identity, governing contract, workspace state, tool-manifest version, effect identity, outcome evidence or key identifier.

Those fields MUST NOT be inserted into XAIP `toolMetadata` and then treated as trusted, because `toolMetadata` is outside the XAIP signed payload.

Where cross-format correlation matters, produce `schemas/xaip-reht-binding-v1.schema.json` and preserve at least:

- canonical REHT receipt reference and hash;
- hash of the complete XAIP receipt as exported;
- binding signer DID;
- explicit `binding_key_id`;
- binding timestamp;
- Ed25519 binding signature.

The binding may additionally carry `action_ref`, `decision_ref`, `authority_state_ref`, `delegation_ref`, `purpose_ref`, `resource_ref`, `governing_contract_digest`, `workspace_state_ref`, `tool_manifest_digest`, `effect_ref` and `outcome_evidence_ref` when those identifiers exist in the governed chain.

The binding signature is computed over the JCS canonical form of every binding member except `binding_signature`, encoded as UTF-8 and signed with Ed25519.

The canonical RACS/REHT receipt remains the source of authority and effect evidence. The binding only proves integrity and signer attribution for the correlation between that source receipt and the XAIP projection.

## Verification dimensions remain separate

A conforming bridge does not collapse these into one boolean:

- cryptographic integrity;
- signer/key identity;
- signer authority;
- current REHT admissibility/clearance semantics;
- governing contract and state continuity;
- tool identity/version binding;
- external effect/outcome truth;
- receipt freshness and replay status.

A valid XAIP signature establishes only the dimensions its signed payload can establish.

## Known XAIP gaps preserved by REHT

The bridge explicitly compensates for the following format limitations without modifying XAIP itself:

- no signed receipt ID or nonce: preserve canonical REHT receipt identity and replay evidence;
- no signed `key_id`: preserve `binding_key_id` and key-resolution evidence outside XAIP;
- `toolName` is opaque and does not bind a tool version: preserve `tool_manifest_digest` or equivalent governed manifest evidence;
- no authority/policy/state/decision fields: preserve them in the canonical governed chain and optional binding refs;
- `toolMetadata` is unsigned: never use it for consequence-bearing trust decisions.

## Conformance

`schemas/xaip-receipt-v1.schema.json` is the strict structural profile.

`tests/validate_examples.py` includes negative cases for:

- unknown XAIP format version;
- malformed hashes;
- success/failure mismatch;
- malformed signatures;
- unknown top-level fields.

Cryptographic verification, DID resolution, JCS byte equality and hash-preimage verification remain implementation-level requirements beyond JSON Schema validation.

Reference: https://datatracker.ietf.org/doc/draft-xkumakichi-xaip-receipts/
