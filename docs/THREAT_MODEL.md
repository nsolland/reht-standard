# Threat Model

REHT Standard addresses failures at the boundary between AI-generated proposals and real-world execution.

## Protected properties

- authority is explicit and time-bounded;
- evidence is attributable and integrity-verifiable;
- applicable policy is identified;
- current governance state is preserved;
- uncertainty never silently becomes permission;
- material changes invalidate stale results;
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

## Required mitigations

Implementations SHOULD use authenticated transport, canonical serialization, cryptographic digests, replay protection, bounded validity periods, explicit revocation, immutable receipt storage and fail-closed behavior for indeterminate states.

This standard does not secure model internals, hosts, networks or physical systems. Implementers must perform a system-specific threat assessment.
