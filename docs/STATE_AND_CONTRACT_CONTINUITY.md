# State and Contract Continuity

Version: 0.3.0-draft.1

This profile extends REHT causal execution continuity with two additional invariants.

## 1. Persistence does not confer standing

Material that survives a worker, model, session or context boundary is not authoritative merely because it persists.

This includes files, memory entries, configuration, instructions, handoffs, checkpoints and cached artifacts.

Where persisted material can influence consequence-bearing work, the implementation MUST establish the current integrity and standing of the exact material exposed to the next worker. Persistence alone MUST NOT create truth, authority, policy status, clearance or evidence standing.

A worker-produced artifact MUST NOT silently become authoritative input for a later worker. It must cross whatever admission, evidence or governance boundary the implementation uses before it can acquire operative standing.

Implementations MAY use digests, provenance records, admission receipts, workspace bindings, state roots or equivalent mechanisms. REHT specifies the invariant, not the storage architecture.

## 2. Governing contracts cannot drift silently

Where a contract, policy set, mandate or equivalent rule set materially governs a work unit, the exact governing state used for evaluation MUST be identifiable.

The implementation MUST be able to detect material amendment, termination, replacement or supersession before consequence.

If material governing state changed after the prior evaluation, the prior result is non-executable and fresh evaluation is required. The old result MUST NOT be rebound under the changed governing contract.

The governing contract need not be disclosed in full to every worker. A deterministic reference, version, digest or equivalent binding is sufficient when it supports independent drift detection.

## 3. Interaction with REHT

These invariants do not create authority and do not replace REHT authorization semantics.

They protect the inputs and rule basis on which an authorization decision relies:

```text
current admitted/governed inputs
  -> bounded work context
  -> candidate result
  -> conformance/evaluation
  -> current governing contract check
  -> fresh REHT execution-boundary evaluation
  -> consequence
  -> receipt
```

## 4. Required negative behavior

A v0.3 conforming implementation must reject at least:

- persistent material whose current standing cannot be established;
- persistent material whose bytes/content materially changed after its binding;
- persistent material that attempts to self-promote from worker output to later authoritative input;
- a continuation evaluated under a governing contract that has since been materially amended;
- a continuation evaluated under a governing contract that has since been terminated or replaced.

## 5. Research context

The persistent-state invariant was made explicit after Papadopoulos, Shah, Zimmerman and Lindsey, *Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems*, arXiv:2608.10218 (2026), which demonstrates propagation through shared persistent surfaces across context resets.

REHT adopts the architectural lesson rather than any paper-specific terminology or model-specific mitigation. Prompt warnings may be defense in depth; they are not a standards-level authority or admission boundary.
