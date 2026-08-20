# Changelog

All notable specification changes are recorded here.

## 0.5.0-draft.1 — 2026-08-20

Added:

- normative Verification Evidence Binding profile for external verifier/runtime/policy receipts materially relied upon before consequence;
- explicit verifier/issuer and intended audience/executor binding semantics;
- exact action/request/material-parameter binding and deterministic policy/configuration binding requirements;
- trust-basis, freshness and replay/consumption requirements for materially relied-upon external verification evidence;
- explicit rule that cryptographic receipt validity is evidence integrity, not current authority, admissibility or execution permission;
- six negative conformance cases covering audience mismatch, issuer/key mismatch, configuration mismatch, action/request mismatch, freshness failure and verification-evidence replay;
- `docs/VERIFICATION_EVIDENCE_BINDING.md` and `docs/CCS_RECEIPT_BINDING_CONVERGENCE.md`;
- proposal record #24.

Changed:

- specification advances from `0.4.0-draft.1` to `0.5.0-draft.1` because the required external-evidence binding and refusal surface expands materially while preserving existing REHT authority and continuity semantics;
- causal execution continuity now treats materially relied-upon external verification evidence as governed evidence whose bindings must remain valid at execution;
- conformance vector advances to `conformance/causal-execution-v0.5.json`; prior vectors remain historical draft evidence.

Research/standards context:

- IETF Internet-Draft `draft-correctover-ccs-01`, *Correctover Conformance Shape (CCS): A Receipt and Binding Specification for Agent Runtime Verification* (2026-08-05), informs the explicit issuer, audience, action/request, configuration, freshness and anti-replay binding surface. REHT adopts those interoperability semantics without adopting CCS as an authorization framework or dependency.

## 0.4.0-draft.1 — 2026-08-14

Added:

- normative constraint-observability rule distinguishing established material constraints from known required constraints that remain unresolved or unavailable;
- fail-closed semantics: known unresolved required material constraints cannot yield `ADMISSIBLE`;
- fresh-evaluation rule for any material post-evaluation action transformation, including deterministic clamping, rewritten tool arguments, substituted targets and equivalent changes;
- prohibition on allowing a transformed action to inherit the source action's admissibility result or receipt;
- `CEC-NEG-CONSTRAINT-001` and `CEC-NEG-TRANSFORM-001` negative conformance cases;
- `docs/CONSTRAINT_OBSERVABILITY_AND_ACTION_TRANSFORMATION.md`;
- proposal record #13.

Changed:

- specification advances from `0.3.0-draft.1` to `0.4.0-draft.1` because the required conformance surface expands materially while retaining compatibility with the v0.3 continuity model;
- causal execution continuity now makes material constraint completeness explicit and treats post-evaluation action transformation as a continuity break requiring fresh evaluation;
- conformance vector advances to `conformance/causal-execution-v0.4.json`; prior vectors remain historical draft evidence.

Research context:

- Shi et al., *Organizational Control Layer: Governance Infrastructure at the Execution Boundary of LLM Agent Systems*, arXiv:2606.04306 (2026), informs the observable/unresolved constraint distinction and proposal-to-execution separation. REHT adopts those lessons but intentionally requires fresh evaluation after material action revision rather than allowing a control-layer rewrite to inherit the prior decision.

## 0.3.0-draft.1 — 2026-08-14

Added:

- normative rule that persistence does not confer standing, trust, authority or clearance;
- persistent-state continuity requirements for files, memory, configuration, instructions, handoffs, checkpoints and cached artifacts that cross worker/session/context boundaries;
- prohibition on silent self-promotion of worker-produced artifacts into later authoritative context;
- governing-contract continuity: material contracts, policy sets or mandates must be identifiable/bound and drift must invalidate reliance on prior evaluation;
- `CEC-NEG-PERSIST-001` and `CEC-NEG-CONTRACT-001` negative conformance cases;
- `docs/STATE_AND_CONTRACT_CONTINUITY.md`;
- `GOVERNANCE.md` defining normative proposal records, semantic version classes, acceptance gates, publisher/review handling and transfer of canonical authority;
- normative-change issue template;
- version-consistency checks in the public validation workflow.

Changed:

- specification advances from `0.2.0-draft.1` to `0.3.0-draft.1` because the required conformance surface expands materially while retaining compatibility with the v0.2 causal-continuity model;
- causal execution continuity now covers consequence-relevant persistent inputs and material governing contract state in addition to action, authority and governed state;
- conformance vector advances to `conformance/causal-execution-v0.3.json`; v0.2 remains preserved as historical draft evidence;
- version governance follows immutable historical tags and forward-only prerelease identifiers.

Research context:

- Papadopoulos, Shah, Zimmerman and Lindsey, *Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems*, arXiv:2608.10218 (2026), informs the persistent-state threat class. REHT adopts the architectural lesson, not paper-specific terminology or prompt-only mitigations.

## 0.2.0-draft.1 — 2026-08-14

Added:

- explicit anti-lock-in and neutral-infrastructure principle;
- normative portability requirements for authority, policy, evidence, workflow state, receipts and persisted learned methods;
- independent-verification requirements across model, agent, protocol and infrastructure substitution;
- clarification that A2A, MCP and provider-specific objects cannot replace REHT authority, evidence, policy or admissibility contracts;
- provider-neutral guidance for Claudefishing, production provenance and expectation integrity;
- normative separation between probabilistic AI-content detection and execution authority;
- conformance requirements for preserving material production provenance, semantic-integrity references and accountable human approval attestations;
- REHT Causal Execution Continuity profile for independently owned systems;
- `execution_envelope_hash` binding semantics without making an external runtime a REHT dependency;
- execution-time independent re-derivation requirement;
- wall-clock demotion from execution-validity authority to policy, scope, audit, correlation and forensic context;
- bidirectional interoperability requirements and a machine-readable first conformance vector;
- required negative cases for drift, expired scope, broken receipt continuity, stale authority and replay;
- public GitHub Actions validation for JSON artifacts, schemas and required release files.

Changed:

- specification status advances to `0.2.0-draft.1` for the causal execution semantics proposal;
- prior authorization/admissibility is no longer treated as a durable bearer verdict;
- existing `timestamp`, `observed_at`, `evaluated_at`, `valid_from`, `valid_until` and `expires_at` fields are retained for compatibility but are not sufficient proof that a prior result remains executable;
- continuous-integrity semantics now distinguish causal ordering from wall-clock observation time;
- public release metadata now follows immutable historical tags plus forward corrective releases.

Research context:

- RS-2026-001, *Causal Substrate Audit: Lamport-Anchored Evidence Under Time-Source Asymmetry*, Jasper van de Meent / Humotica and Richard Barron / Red Specter Security Research, DOI `10.5281/zenodo.20338260`, informs the causal-ordering profile;
- the related TIBET Causal Time Internet-Draft is treated as technical background, not as an adopted IETF standard or required dependency.

Regulatory context:

- France's Autorité de la concurrence Opinion 26-A-05 of 17 July 2026 identifies competition risks from limited agent interoperability, barriers to data portability and concentrated control of technical standards, and recommends open, transparent and interoperable standards.

## 0.1.0-draft — 2026-07-15

Initial public draft.

Added:

- normative REHT specification;
- public repository boundaries;
- Action Envelope and Execution Receipt schemas;
- Authority Context, Evidence Package, Policy Context and Governance State schemas;
- Admissibility Result and Continuous Integrity Event schemas;
- conformance levels and requirements;
- threat model and versioning policy;
- valid reference examples;
- automated schema and example validation;
- contribution, security, attribution and trademark rules.
