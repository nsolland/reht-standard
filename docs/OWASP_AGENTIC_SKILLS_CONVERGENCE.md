# OWASP Agentic Skills Top 10 — REHT convergence note

Status: external convergence reference; non-normative.

Source: OWASP Agentic Skills Top 10 document shared 2026-08-19 via LinkedIn PDF metadata URL:
https://media.licdn.com/dms/document/media/v2/D561FAQEtL7JvpCegOQ/feedshare-document-url-metadata-scrapper-pdf/B56aAR64hMGcA4-/0/1787007046083?e=1787745600&v=beta&t=VuekkwmQxnVSUd5TTOwEXQIwImPFIXl3Cu8SZoEY--s

## Why it matters

The document treats agent skills as an independent security and governance surface. Its threat framing includes malicious or compromised skills, supply-chain compromise, over-privilege, instruction attacks, weak isolation, drift, missing governance, and loss of controls across execution environments.

Of particular relevance is the governance/admission pattern: an action is evaluated before execution, with an admission decision and evidence describing the actor, requested action, scope and governing policy. The document also separates pre-execution admission evidence from post-execution outcome evidence and correlates them through a common action/attempt reference.

This converges strongly with REHT on the need for:

- a pre-effect enforcement boundary;
- explicit ALLOW / DENY / ESCALATE-style outcomes;
- evidence for both permitted and blocked actions;
- deterministic correlation between decision and later outcome;
- revocation and governance as runtime concerns rather than purely design-time concerns.

## REHT distinction

This convergence does not collapse REHT into policy admission.

REHT requires authority to be resolved against current governed state at the moment a consequence-bearing action is about to commit. A previously valid admission is not sufficient if authority, delegation, constraints, revocation state, evidence freshness or other material state has changed before effect.

The operative question is therefore not only:

> Was this action admitted under policy?

but:

> Is this actor still entitled to perform this exact action, under this delegation and these constraints, at the moment of consequence?

REHT also retains stronger execution-integrity invariants:

- NO_DIRECT_EFFECT_PATH: consequence-bearing effects must traverse the governed enforcement boundary;
- commit-time revalidation of material authority and revocation state;
- null effect on non-ALLOW outcomes;
- deterministic decision/effect correlation;
- verifiable evidence for both clearance and outcome;
- deterministic replay at governed decision/effect boundaries.

## Adoption decision

Adopt the OWASP work as external validation and interoperability signal, not as a replacement architecture.

Where compatible, REHT artifacts SHOULD remain easy to map to external admission/outcome receipt models, including stable action references, actor identity, action type, scope, governing-policy reference, decision, timestamp and cryptographically bindable evidence.

Do not weaken REHT's commit-time authority semantics to match admission-only systems. Policy admission, skill approval or IAM entitlement are inputs to execution authorization, not proof that authority still exists at consequence time.

## Conformance implications

The OWASP convergence strengthens the case for the existing REHT conformance direction:

1. deny/escalate decisions produce evidence and no consequence-bearing effect;
2. outcome evidence is correlated to the exact cleared action;
3. stale or revoked authority invalidates execution before commit;
4. bypass paths around the enforcement boundary are non-conformant;
5. replay uses pinned governed inputs and boundary evidence rather than token-level model replay.
