# EU AI Act deployer authority — REHT convergence note

Status: external regulatory convergence reference; non-normative.

Sources:

- LinkedIn discussion shared 2026-08-21: https://lnkd.in/p/eczkMZtg
- Regulation (EU) 2024/1689, Article 3(4) and Article 26: https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng

## Why it matters

The EU AI Act defines a `deployer` as a natural or legal person, public authority, agency or other body using an AI system under its authority, except for purely personal non-professional use.

For high-risk AI systems, Article 26 places concrete obligations on deployers. These include appropriate technical and organisational measures, assignment of human oversight to persons with the necessary competence, training and authority, operational monitoring, logging obligations where applicable, and suspension of use when the system may present a relevant risk.

This is an important regulatory signal because it makes the deployer's authority and operational responsibility explicit. It does not, however, define a machine-verifiable execution-time entitlement for each consequence-bearing action.

The regulatory question and the REHT question are therefore related but distinct:

- EU AI Act: which actor or organisation bears the relevant provider/deployer obligations and must organise compliant use?
- REHT: is this exact actor still entitled to perform this exact action, under current authority, delegation, constraints, evidence and governed state, at the moment of consequence?

## REHT distinction

Provider or deployer classification is not itself execution authorization.

An organisation can hold regulatory responsibility for deployment while individual agents, services, operators or delegated actors within that organisation have different scopes of authority. Those scopes may also change between initial approval and execution because of revocation, delegation changes, policy changes, state changes, unresolved constraints or stale evidence.

REHT therefore treats regulatory role and organisational responsibility as possible governed inputs to the Authority Context, not as bearer tokens that make a later action executable.

A prior approval, valid deployment status or organisational role cannot override execution-time authority drift.

The operative REHT question remains:

> Who has the right to act on this exact action — right now?

## Adoption decision

Adopt the EU AI Act provider/deployer distinction as external regulatory validation of the need to separate organisational responsibility from execution-time authorization.

The useful market progression is:

1. provider responsibility;
2. deployer responsibility;
3. deployer control;
4. execution-time handlingsrett for the exact action.

REHT addresses the fourth layer without claiming that REHT conformance alone establishes EU AI Act compliance.

No new normative REHT requirement is introduced by this note.

## Conformance relevance

The regulatory signal strengthens, but does not change, the existing REHT conformance direction:

1. authority must be current at the execution boundary;
2. delegated authority may be narrower than organisational responsibility;
3. stale, revoked or otherwise invalid authority must prevent consequence;
4. non-executable outcomes must produce null effect;
5. the execution evidence chain must preserve which actor acted, under which authority and governing state, for which exact action.

Article 26 is specifically concerned with deployers of high-risk AI systems. REHT remains technology- and sector-neutral and should not broaden the legal scope of that provision by implication.
