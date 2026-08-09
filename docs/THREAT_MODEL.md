# Threat Model

REHT Standard addresses failures at the boundary between AI-generated proposals and real-world execution.

## Protected properties

- authority is explicit, bounded and re-established where execution requires it;
- evidence is attributable and integrity-verifiable;
- applicable policy is identified;
- current governance state is preserved or independently re-derived at execution;
- uncertainty never silently becomes permission;
- material changes invalidate stale results;
- execution validity is not inferred solely from wall-clock expiry;
- causal continuity is preserved where evaluation and execution are separated;
- terminal evaluations remain auditable.

## Threats

1. Forged or replayed authority.
2. Expired, circular, fabricated or substituted evidence.
3. Policy omission, ambiguity or version drift.
4. Stale admissibility reused after state change.
5. Result tampering between evaluation and execution.
6. Receipt deletion, reordering or hash-chain breakage.
7. Privilege escalation through delegation chains.
8. Human approval represented without a verifiable reference.
9. Fail-open behavior when evaluators are unavailable.
10. Schema-valid but semantically misleading payloads.
11. Clock drift or time-source asymmetry causing false execution validity.
12. A relevant authority or state mutation causally intervening after authorization.
13. Reuse of a single-use execution binding or causal position.
14. An executor trusting a producer's stale state instead of independently re-deriving execution-relevant state.
15. Missing receipt or evidence lineage being treated as continuity.

## Required mitigations

Implementations SHOULD use authenticated transport, canonical serialization, cryptographic digests, explicit replay protection, causal ordering where independently owned systems cross an execution boundary, explicit revocation, immutable receipt storage and fail-closed behavior for indeterminate states.

Wall-clock constraints MAY remain part of policy, scope, audit and forensic context. They MUST NOT be treated as sufficient proof that a prior admissibility remains executable across independently owned systems.

Execution-boundary implementations SHOULD bind the evaluated action to a deterministic execution envelope, independently re-derive the execution-relevant envelope immediately before consequence, and reject material drift, stale authority, replay and broken required continuity.

This standard does not secure model internals, hosts, networks or physical systems. Implementers must perform a system-specific threat assessment.
