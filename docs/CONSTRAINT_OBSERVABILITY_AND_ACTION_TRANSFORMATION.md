# Constraint Observability and Action Transformation

Status: proposed normative profile for REHT 0.4.0-draft.1.
Proposal: #13.

## 1. Constraint observability

A REHT evaluation may rely only on execution-relevant constraints that are established and available to the evaluator. A conforming implementation must distinguish those established constraints from material constraints that are known to be required but remain unresolved or unavailable.

A known missing material constraint is not neutral. The action must not be represented as `ADMISSIBLE` while that constraint remains unresolved.

Where an authorized process can resolve the missing constraint, the reference outcome is `REQUIRES_STEP_UP`. Where the required evidence or constraint cannot currently be established, the reference outcome is `INDETERMINATE`.

This requirement does not claim that a system can enumerate genuinely unknown constraints. It prevents known observability gaps from being silently treated as satisfied constraints.

## 2. Proposal, decision and consequence

The execution-boundary sequence is:

```text
candidate action
    -> REHT evaluation
    -> admissibility result bound to that exact action
    -> execution-boundary continuity check
    -> consequence-bearing execution
    -> state transition + receipt
```

Only the action bound to the current admissibility result may proceed to consequence.

## 3. Transformation requires fresh evaluation

A control, policy, safety or orchestration layer may reject an action or propose a modified replacement. It may not transform an evaluated action and allow the transformed action to inherit the source action's admissibility result.

Any material revision creates a new candidate action. The revised action must receive fresh REHT evaluation under current authority, evidence, policy, governed state and execution-relevant constraints before consequence.

This applies to deterministic clamping, rewritten tool arguments, changed prices or quantities, substituted targets, altered resource scope and equivalent material transformations.

## 4. Conformance consequences

A conforming implementation must fail closed when:

- a required material execution constraint is known to be unresolved;
- the action presented for execution differs materially from the action bound to the current admissibility result;
- a rewritten or substituted action is presented under the receipt or result of its source action.

## 5. Research provenance

The observability distinction and explicit separation between raw proposals and environment-facing actions are informed by Shi et al., *Organizational Control Layer: Governance Infrastructure at the Execution Boundary of LLM Agent Systems*, arXiv:2606.04306 (2026).

REHT adopts these useful execution-boundary lessons but intentionally differs on action revision: a revised action is a new candidate requiring fresh authorization, not an executable action created by the control layer under the prior decision.
