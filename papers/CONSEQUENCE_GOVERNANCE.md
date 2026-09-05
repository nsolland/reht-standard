# Consequence Governance: Governing the Transition from Proposed Action to Real-World Effect

Njål Gaute Solland  
VALO Research  
September 2026

## Abstract

AI governance commonly governs models, agents, identities, tools, policies, workflows, or organizational processes. These are necessary control surfaces, but none is identical to the final question that arises when a proposed action is about to change the external world: **may this exact consequence legitimately become real now?**

This paper defines **Consequence Governance** as the governance category concerned with that question. The governing object is the proposed consequence rather than the worker that proposed it. The proposer may be an AI agent, a person, a workflow, an API, a device, or another machine. We synthesize three public and independently inspectable VALO surfaces: the REHT standard for consequence-time admissibility, the RACS protocol for deterministic decision/action binding, and `valo-gateway` as reference mechanical enforcement infrastructure. Together they expose a separation of concerns from reasoning to authority, deterministic binding, enforcement, and evidence.

The central architectural claim is that consequential systems require a **Governed Effect Path**: no consequence-bearing action may bypass a fresh authorization boundary, deterministic binding to the exact action, bounded enforcement, and resulting evidence. This yields the invariant **NO_DIRECT_EFFECT_PATH**. The paper distinguishes capability, access, evaluation, admissibility, execution authorization, execution success, observed outcome, and value evidence; proposes falsifiable conformance properties; and identifies the limits of the current public evidence. The contribution is not another agent framework. It is a category and boundary model for governing the transition from proposed action to external consequence.

## 1. Introduction

Modern AI systems can increasingly plan, call tools, operate software, coordinate workflows, and initiate actions with external effects. Most governance mechanisms, however, attach control to upstream objects: the model, agent, user, role, tool, workflow, policy, or deployment environment.

Those objects matter, but the final unit of governance is different. A capable and authenticated worker can still propose an action that is no longer authorized. A previously approved action can become illegitimate after authority, policy, state, evidence, scope, purpose, or constraints change. A valid workflow can contain a consequence that should not occur. A cryptographically valid receipt can prove that something was signed without proving that the underlying authority remains current.

We therefore define:

> **Consequence Governance is the governance category for deciding whether an exact proposed consequence may legitimately become real under the authority, evidence, constraints, and governed state that exist at consequence time.**

The distinction is temporal and ontological. The system does not merely ask whether an actor generally has a capability or whether a plan once passed evaluation. It asks whether the exact state transition proposed at the effect boundary is legitimate now.

This paper develops that category from public implementation and standards artifacts rather than from a purely conceptual architecture. The public evidence consists of:

1. **REHT Standard** — a model-agnostic standard for consequence-time admissibility and causal execution continuity.
2. **RACS** — a deterministic protocol/schema layer that binds an already-made governance decision to the exact action, execution boundary, and evidence chain.
3. **valo-gateway** — vendor-neutral reference enforcement infrastructure that mechanically validates an external authorization binding, consumes one-shot execution capability, invokes a bounded adapter, and emits a receipt.

These surfaces are deliberately separate. Their separation is itself part of the claim.

## 2. The missing governance object

A useful governance architecture must distinguish questions that are often collapsed:

| Layer | Governing question |
|---|---|
| Identity | Who or what is acting? |
| Capability | What can the worker technically do? |
| Access control | What resource may the subject access? |
| Agent governance | How may the worker operate? |
| Workflow governance | How should the process proceed? |
| Evaluation | What do evidence, policy, risk and uncertainty indicate? |
| Consequence Governance | May this exact proposed effect legitimately become real now? |
| Enforcement | Does the exact authorized action cross the effect boundary? |
| Evidence | What was decided, attempted and observed? |

Consequence Governance does not replace the preceding layers. It consumes their authoritative outputs where applicable while refusing to treat any of them as durable execution authority.

The key distinction is:

**Capability != authority. Access != consequence authorization. Evaluation != execution authorization. Prior approval != current authority. Execution success != outcome proof. Outcome != value proof.**

## 3. Architecture: the Governed Effect Path

The category implies an architectural constraint. If a consequential action can reach the external world through an ungoverned path, a correct authorization mechanism on another path cannot guarantee governance.

We call the required architecture the **Governed Effect Path**.

```text
proposal / candidate action
          |
          v
current evidence + authority + policy + governed state
          |
          v
consequence-time admissibility / authorization
          |
          v
deterministic decision + exact-action binding
          |
          v
mechanical enforcement boundary
          |
          v
external consequence
          |
          v
execution / outcome evidence
```

Its primary invariant is:

> **NO_DIRECT_EFFECT_PATH:** no consequence-bearing effect may bypass the governed path.

This is stronger than requiring a policy check somewhere in the system. The claim is structural: the governed boundary must be causally necessary for the consequence.

## 4. Separation of concerns

### 4.1 REHT: consequence-time admissibility

The public REHT standard asks whether the exact action remains admissible under the authority, state, constraints, evidence, and governing basis that actually exist at execution. It explicitly rejects the assumption that authorization is a durable truth.

REHT's public semantic outcomes are:

- `ADMISSIBLE`
- `INADMISSIBLE`
- `INDETERMINATE`
- `REQUIRES_STEP_UP`
- `NO_LONGER_ADMISSIBLE`

These are semantic admissibility outcomes, not mechanical execution commands. This distinction matters: standards-level judgment about admissibility should not be conflated with downstream protocol vocabulary.

REHT also makes causal continuity explicit. A prior result remains relevant only when the executor can establish that the action, authority, governing contract, required constraints, evidence bindings, and execution-relevant state remain the ones evaluated and that no disqualifying event has intervened.

### 4.2 RACS: deterministic binding

RACS does not decide admissibility or grant authority. Its role is to represent and bind an already-made governance decision to exact artifacts and the execution/evidence chain.

The public RACS specification separates artifacts including AuthorityGrant, DelegationChain, ActionEnvelope, GovernanceEvaluation, AdmissibilityDetermination, GovernanceClearance, CoreExecutionPermit, CommitToken, ExecutionReceipt, OutcomeReceipt, ValueReceipt, and SettlementReceipt.

This decomposition prevents a common semantic collapse. For example:

- an `ActionEnvelope` is a proposal, not authority;
- an evaluation result is not execution authorization;
- a clearance binds one exact candidate;
- a permit and one-shot commit token narrow the path toward consequence;
- an execution receipt is not proof of beneficial outcome;
- an outcome receipt is not proof of value.

RACS therefore provides deterministic transport and binding semantics without becoming the source of organizational legitimacy.

### 4.3 Gateway: mechanical enforcement

The public `valo-gateway` repository describes a deliberately narrower role. The gateway does not evaluate risk, infer authority, or decide whether an action should be allowed. It accepts an exact action and an externally produced authorization/decision binding, validates required bindings immediately before execution, consumes one-shot execution capability, invokes the selected tool/runtime, and emits an execution receipt.

This creates a clean architectural property: adapters do not create authority. Runtime or vendor substitution does not inherently move the authorization boundary. A provider integration is mechanically downstream of the governance decision.

## 5. Consequence-time authorization

The phrase **consequence-time authorization** denotes fresh exact-action authorization immediately before an effect is permitted to cross into the external world.

“Fresh” does not mean merely “recent according to a wall clock.” The REHT public standard explicitly treats wall-clock freshness as insufficient across independently owned systems. The stronger requirement is causal continuity: the relevant action and governing basis must still be the evaluated ones, with no intervening invalidation.

This matters in at least six drift classes:

1. authority or delegation changes;
2. policy or governing-contract changes;
3. target, payload, purpose, or material action transformation;
4. required constraints become unresolved;
5. evidence loses required binding, trust, freshness, or replay properties;
6. governed state changes between evaluation and consequence.

The safe response to unresolved material uncertainty is not to silently preserve the old authorization. Unknown remains unknown and the path fails closed or requires an authorized step-up process.

## 6. Governed Contracts and worker neutrality

A Consequence Governance architecture should not make legitimacy depend on the internal form of the worker. The same consequential operation may be proposed by a person, an LLM agent, a deterministic workflow, a service, or a physical device.

A **Governed Contract** therefore describes the legitimate purpose, mandate, scope, constraints, required evidence, and completion conditions independently of the worker that attempts to realize it.

This yields a useful separation:

```text
worker / harness / agent
        |
        v
proposal under governed contract
        |
        v
current admissibility and authority
        |
        v
exact decision/action binding
        |
        v
governed effect path
```

Conformance to the contract is evidence for governance. It is not itself authorization.

## 7. Human-in-the-Lead

Consequence Governance does not require a human to approve every action. That would make human attention the enforcement mechanism and would not scale with machine-speed systems.

The stronger formulation is **Human-in-the-Lead**: human and institutional judgment establish legitimate authority, mandates, constraints, escalation rules, and accountability, while the execution architecture mechanically preserves those boundaries at consequence time.

Human judgment governs authority. Human attention is not the enforcement mechanism.

## 8. Falsifiable properties

The category is useful only if architectural claims can fail. A system claiming a Governed Effect Path should be testable against at least the following properties.

### P1. No-bypass property

For every consequence-bearing adapter or external mutation path, removal or refusal of the governed authorization artifact must make the external effect unreachable.

**Falsifier:** an action can still produce the effect through another tool, adapter, retry path, recovery path, or privileged interface.

### P2. Exact-action binding

Authorization for action `A` must not authorize a materially different action `A'`.

**Falsifier:** target, payload, purpose, principal, executor, or material parameters can change after authorization without fresh evaluation.

### P3. Revocation dominance

A valid earlier authorization must not survive a causally prior revocation or material authority invalidation.

**Falsifier:** an unexpired token or cached approval still executes after authoritative revocation.

### P4. Unknown fails closed

Missing mandatory authority, evidence, constraint, issuer, trust, or continuity information must not be silently converted into permission.

**Falsifier:** incomplete required state defaults to execution.

### P5. Replay resistance

A single-use execution capability must not create more than one consequence.

**Falsifier:** the same permit/commit identity can be consumed twice to create duplicate external effects.

### P6. Evidence separation

Execution success, observed outcome, and measured value must remain distinguishable.

**Falsifier:** a successful API response is automatically treated as proof that the intended real-world outcome or value occurred.

### P7. Worker substitution

Replacing the proposing model, agent framework, or runtime must not by itself confer authority or bypass consequence-time authorization.

**Falsifier:** a trusted runtime or registered agent gains an independent consequence-bearing path.

## 9. Threat model

The architecture primarily addresses semantic and authority drift between intention and consequence. Relevant threats include stale approvals, overbroad delegation, replay, post-evaluation action rewriting, persistent-state self-promotion, contract drift, missing constraints, forged or misbound evidence, adapter bypass, recovery self-authorization, and provider-specific privileged paths.

It does not claim that governance can establish moral truth, infer legitimate institutional authority from nothing, guarantee the correctness of upstream evidence, or make an unsafe physical system safe solely through software authorization.

Independent low-level safety interlocks remain distinct from Consequence Governance and should not be disabled by it.

## 10. Public evidence and current limits

The public repositories provide inspectable specifications, schemas, conformance semantics, reference enforcement code, and examples. They support a stronger claim than a conceptual diagram: the separation between admissibility, deterministic binding, enforcement, and receipts is represented in public artifacts.

However, this paper does **not** claim from those repositories alone that:

- all production VALO deployments implement every public draft feature;
- every invariant has been independently audited;
- the architecture is universally optimal;
- consequence-time authorization eliminates upstream model risk;
- cryptographic validity proves organizational legitimacy;
- the current public evidence establishes empirical superiority over all alternative governance architectures.

Those remain separate empirical or assurance questions.

## 11. Implications

### 11.1 Agent governance is upstream, not sufficient

An agent can be well-governed and still propose a consequence that is no longer legitimate. Conversely, multiple heterogeneous workers can share the same consequence boundary. This suggests that governance portability improves when the effect boundary is independent of the agent framework.

### 11.2 Authorization is a state-dependent relation

Authorization should be modeled less like a durable property attached to an actor and more like a current relation among actor, mandate, action, target, purpose, constraints, evidence, and governed state.

### 11.3 Receipts are part of control, not merely audit

When decisions and effects are explicitly bound, receipts support replay, verification, dispute, renewal, and later outcome/value evaluation. Evidence becomes part of the architecture rather than a log appended after the fact.

### 11.4 Model capability can scale independently

If the consequence boundary is structurally enforced, models and runtimes can improve or be replaced without requiring their internal reasoning to become the source of execution authority. This separates capability growth from authority growth.

## 12. Research agenda

The next useful work is empirical rather than terminological. Priority experiments include:

- adversarial bypass testing across all consequence-bearing adapters;
- authority-drift tests between evaluation, permit issuance, and commit;
- cross-runtime substitution with identical governed contracts;
- replay and recovery-path attacks;
- latency and availability cost of consequence-time authorization;
- comparison with identity-centric, agent-centric, and workflow-centric governance baselines;
- independent conformance implementations of REHT and RACS;
- formal verification of the no-direct-effect-path invariant under explicit system models.

A particularly strong test would hold worker capability constant while varying only whether the external consequence is structurally forced through the governed path. If bypass remains possible, the architecture fails its central claim.

## 13. Conclusion

AI systems do not become governed merely because their models are evaluated, their agents are registered, their tools are permissioned, or their workflows are approved. Those controls govern important upstream objects. The final transition into the world remains a distinct governance problem.

Consequence Governance names that problem: **may this exact proposed consequence legitimately become real now?**

The public REHT, RACS, and `valo-gateway` surfaces show one concrete decomposition of the answer. REHT evaluates current admissibility and causal continuity. RACS deterministically binds governance artifacts to the exact action and evidence chain. The gateway mechanically enforces the bound decision at the effect boundary. The resulting architecture is a Governed Effect Path whose central invariant is NO_DIRECT_EFFECT_PATH.

The claim is intentionally narrow. It does not solve intelligence, ethics, organizational legitimacy, or all AI safety. It establishes a testable boundary between the ability to propose an action and the authority to make its consequence real.

## References

1. VALO Research. *REHT Standard*. Public repository: `nsolland/reht-standard`, accessed 5 September 2026.
2. VALO Research. *Consequence Governance and REHT*. `CONSEQUENCE_GOVERNANCE.md`, REHT Standard public repository, 2026.
3. VALO Research. *RACS Specification*, Draft 0.2. Public repository: `nsolland/Racs`, accessed 5 September 2026.
4. VALO Research. *valo-gateway: Vendor-neutral reference enforcement infrastructure for governed actions*. Public repository: `nsolland/valo-gateway`, accessed 5 September 2026.
5. VALO Research. *Consequence Governance: Definition, Architecture and Principles*. `valoresearch.org/consequence-governance.html`, 2026.

## Artifact provenance

This paper is a synthesis of public repository surfaces. It intentionally excludes private runtime implementation details and unpublished research claims. Normative REHT and RACS semantics remain owned by their respective specifications; this paper is explanatory and does not supersede them.