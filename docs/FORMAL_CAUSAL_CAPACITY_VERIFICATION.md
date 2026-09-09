# Formal causal-capacity verification

Status: draft normative guidance for REHT causal conformance v0.7.

## Security property

`NO_UNGOVERNED_CAUSAL_EFFECT_PATH` is an absence-of-bad-paths safety property:

> No causal path from untrusted computation to a relevant external consequence may succeed unless it crosses an explicit governed effect boundary for the exact effect under current authority.

The existing identifier `NO_DIRECT_EFFECT_PATH` remains compatibility/canonical vocabulary in existing implementations. v0.7 makes the full causal semantics explicit.

## Boundary validity

A path is not governed merely because it traverses a named gateway. The boundary must be:

- explicitly declared;
- bound to the exact proposed effect;
- currently authorized from fresh authoritative state/evidence;
- able to enforce DENY before commitment;
- fail-closed; and
- able to preserve decision/outcome evidence.

Rollback, compensation and isolation are optional recovery mechanisms, not prerequisites for authorization. Irreversible effects make pre-commit enforcement essential.

## Formal methods mapping

### Information-flow control / non-interference

Treat external consequence as a protected observation/effect domain and governed boundaries as controlled release points. Robust declassification is the closer analogy than absolute non-interference because legitimate effects are intentionally permitted.

### Capability/effect systems

A strong implementation discipline removes ambient authority: an external effect is impossible without an unforgeable capability presented at a governed boundary. This is useful for proving complete mediation inside a capability-safe trusted computing base.

### Model checking

Construct a finite causal/dependence graph or transition system and check reachability from untrusted nodes to consequence nodes while excluding governed boundary nodes. TLA+/TLC is the reference approach for VALO's current bounded model because concurrency, retries, relay actors and shared-state interleavings are first-class.

### Theorem proving

TLAPS, Lean, Coq, Isabelle/HOL or similar systems may prove the abstract mediation invariant without finite-state enumeration. Such a proof is only as strong as the model-to-implementation refinement argument.

### Static/abstract analysis

Taint, dependency and effect analysis can over-approximate possible flows. If the over-approximation contains no ungoverned path, it supplies strong code-level evidence; false positives remain expected.

### Runtime verification

Static proof does not discover deployment drift by itself. Runtime path inventory, provenance, capability enforcement and monitors are complementary evidence that the concrete topology still matches the proved abstraction.

## TLA+ reference model

The VALO Kernel branch `feature/no-ungoverned-causal-effect-path-v1` contains:

- `formal/NoUngovernedCausalEffectPath.tla`
- `formal/NoUngovernedCausalEffectPath.cfg`

The model treats the untrusted component as adversarial and nondeterministic. It can attempt every declared causal channel. A blocked ungoverned attempt may change only internal accounting; it may not change the external-effect counter. Successful external effects record a known boundary, authorization, enforcement and evidence.

The principal invariant is:

```text
external effect
  => known governed boundary
  && current authorization
  && enforcement
  && evidence
```

## Deployment proof obligation

A formal proof of the abstract model does not prove that a real deployment has no omitted path. Deployment conformance therefore requires:

1. bounded reachable-path inventory;
2. mapping of each path to an enforced boundary or internal-only classification;
3. evidence of actual interception/enforcement;
4. fail-closed treatment of unknown paths; and
5. re-verification when topology, code, configuration, credentials, plugins, operators or integrations change.

Human relay, side channels and open-world external systems are never silently assumed absent.

## Zero Trust relationship

Zero Trust continuously verifies access requests. Consequence Governance carries the same distrust/re-verification discipline to a different control object: consequential causal capacity.

```text
Zero Trust:             subject -> access request -> resource
Consequence Governance: untrusted state -> causal path -> consequence
```

The relationship is complementary, not a claim that Zero Trust is defective. A path outside an access-control enforcement scope is simply outside what that access decision proves.

## Local-only execution

All validators, TLC runs and conformance runs are executed locally. No GitHub Actions/remote CI is part of the validation path.
