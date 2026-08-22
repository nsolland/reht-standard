# REHT Composition Closure Profile

Status: additive draft profile for REHT -00.

## Invariant

Fresh authorization of a Candidate Action is necessary but not sufficient when the admissibility of that action depends on prior governed effects.

A conforming deployment using this profile MUST evaluate the proposed Candidate Action against relevant prior governed effects before consequence. An action that is individually within current authority MUST still fail closed when its composition with prior effects violates a governed composition constraint.

Formally, execution admissibility is a function of:

`current authority + current governed state + prior governed effects + proposed effect`.

## Composition constraints

A composition constraint MAY prohibit an ordered pair or k-tuple of consequence-bearing capabilities or canonical actions. For example, `READ_SENSITIVE -> SEND_EXTERNAL` may be prohibited even where `READ_SENSITIVE` and `SEND_EXTERNAL` are each individually authorized.

The evaluator MUST be deterministic for pinned authority, governed state, effect history, composition rules, and Candidate Action.

Missing, stale, unverifiable, or unresolved history required by an applicable composition rule MUST fail closed.

## Continuity scope

Composition history MUST NOT be scoped only to an LLM conversation, worker process, agent session, or orchestrator session when consequence-bearing continuity survives that boundary.

Deployments MUST bind history to an appropriate governed continuity scope such as principal + purpose + resource/case/transaction lineage. Starting a new model or agent session MUST NOT erase applicable prior governed effects.

## Effect-path enforcement

Composition closure is evaluated inside the governed consequence path. No worker, model, runtime, orchestrator, or connector may bypass it when an applicable rule exists.

A failed composition-closure result MUST produce null effect. RACS or another downstream deterministic binding MUST NOT expand a failed composition result into an executable action.

## Evidence

The verification evidence SHOULD bind:

- the proposed action/action digest;
- governed continuity scope reference;
- composition-rule identifier(s);
- relevant prior effect references or a deterministic history digest;
- the resulting disposition;
- current authority/state references used at the boundary.

This permits deterministic boundary replay without requiring token-by-token model replay.

## External convergence

This profile adopts the composition-closure insight described in arXiv:2608.15888 as external validation and a useful formalization of sequential authority misuse. REHT does not adopt that paper's architecture wholesale. REHT retains fresh consequence-time authority, governed state continuity, no-direct-effect-path enforcement, narrowing-only delegation, fail-closed semantics, and governed evidence as its broader execution-authorization model.

Reference: https://arxiv.org/abs/2608.15888
