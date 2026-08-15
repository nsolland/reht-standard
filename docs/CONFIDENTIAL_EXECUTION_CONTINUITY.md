# Confidential Execution Continuity

Status: normative v0.4 draft profile extension

## Purpose

Some governed actions depend materially on executing inside a confidential or hardware-attested execution substrate, such as a Trusted Execution Environment (TEE).

The execution substrate is evidence about where and how execution is occurring. It is not authority, approval or clearance.

A conforming REHT flow therefore treats confidential-execution state as a material execution constraint under the existing causal execution continuity rule.

## Canonical invariant

When confidential execution is required for an evaluated action, consequence is executable only if the exact required substrate binding remains established, current and continuous at the execution boundary.

Conceptually:

```text
evaluated action
  + current authority
  + governed state
  + required confidential-execution binding
  -> fresh execution-boundary continuity check
  -> consequence or fail closed
```

A prior successful TEE attestation is not a durable bearer authorization.

## Required binding

Where confidential execution is material to admissibility, the evaluated execution envelope MUST bind the normalized substrate evidence by a deterministic digest or equivalent integrity-verifiable reference.

The binding SHOULD permit an independent executor to establish, where applicable:

- the required substrate class;
- the attested execution environment identity;
- the attestation evidence or evidence digest;
- the measurement or equivalent environment identity;
- the model/workload binding when material;
- the attestation validity/freshness basis;
- that the substrate evidence itself grants no authority.

The public REHT standard does not require one vendor-specific quote, certificate chain, TEE implementation or verifier API.

## Execution-time re-establishment

Immediately before consequence, the execution boundary MUST re-establish the material confidential-execution constraint from current governed evidence.

The action is non-executable when any required substrate basis is:

- missing or unresolved;
- invalid or revoked;
- stale or expired under the applicable freshness rule;
- bound to a different normalized substrate digest;
- bound to a different material measurement, model or workload;
- incapable of proving the required execution-environment continuity.

A wall-clock validity interval may be part of the freshness rule, but an unexpired timestamp alone does not create execution authority or replace causal continuity.

## Authority boundary

TEE, confidential-compute attestation, hardware identity, measurements and verifier outputs are evidence inputs only.

They MUST NOT:

- create or widen authority;
- issue REHT clearance;
- turn a non-executable REHT result into an executable result;
- bypass the governed effect path;
- legitimize an effect after the fact.

## Receipt continuity

When confidential execution materially affected admissibility, the execution receipt SHOULD preserve the exact substrate binding digest and evidence reference needed to verify what execution environment was bound to the consequence.

A verifier may attest that the receipt contains and preserves those observations. It must not infer authority merely from the presence of valid-looking attestation evidence.

## Portability

The normalized binding must remain provider neutral. NVIDIA, AMD, Intel, cloud confidential-compute services and future execution substrates may supply evidence through adapters without becoming required REHT dependencies.
