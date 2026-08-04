# Claudefishing, provenance and expectation integrity

## Status

Interpretive guidance for REHT evidence, semantic representation integrity and execution-governance implementations.

This document does not define a detector, classifier or execution command.

## 1. The problem

Claudefishing is the material mismatch between how an audience reasonably believes a communication was produced and how it was actually produced with AI assistance.

The governance concern is not AI use by itself. The concern is an undisclosed or misleading production process that can alter authorship, meaning, accountability or the audience's basis for trust.

This is an expectation-integrity and provenance problem.

## 2. Canonical principle

A detector may estimate whether AI influenced an artifact. It cannot determine who originated the idea, owned the intent, exercised judgment, approved the final meaning or accepts responsibility for the consequence.

Therefore:

1. AI-content detection is a probabilistic evidence signal, never execution authority.
2. A detector result must not by itself establish deception, authorship or accountability.
3. A positive or uncertain result may increase uncertainty, request additional evidence or produce `REQUIRES_STEP_UP`.
4. A conforming implementation must not produce `INADMISSIBLE` solely because one detector classified an artifact as AI-influenced, unless an applicable policy independently makes that classification dispositive and the policy's evidence threshold is satisfied.
5. Human accountability must be bound through attestations, authority and receipts rather than inferred from writing style.

## 3. Human in the lead

Human in the lead means that a responsible human owns the purpose, mandate, values, material judgment and final authority for a consequential communication or action.

AI may draft, transform, translate, summarize or edit within delegated bounds. The accountable principal must be able to review, correct, reject and attest to the final representation before consequential execution when policy requires it.

The relevant question is not whether AI touched the artifact. It is whether a legitimate principal remained in control of meaning and consequence.

## 4. Production provenance

Where provenance is relevant to admissibility, an Evidence Package should bind references to the available production record. This may include:

- the original human input or a privacy-preserving digest;
- declared purpose and intended audience;
- transformation events in chronological order;
- models, tools and material system instructions used;
- material human edits and review checkpoints;
- semantic-integrity checks across translation, normalization and summarization;
- disclosure assertions shown to the audience;
- accountable principal and approval attestation;
- detector signals, including provider, model or version, timestamp, confidence and limitations;
- disputes, corrections and superseding attestations.

The production record should preserve the original language, meaning, provenance, ambiguity and transformation history required to reconstruct how the final representation was produced.

Raw private drafts or prompts need not be disclosed publicly. Implementations may use hashes, signed attestations, selective disclosure or controlled audit access while preserving independent verifiability.

## 5. Detector handling

Detector outputs are untrusted observations until bound to context and policy.

An implementation using a detector should:

- record the detector identity and version;
- record the evaluated artifact digest;
- preserve the score, threshold and uncertainty rather than only a binary label;
- account for detector drift, false positives, false negatives and language bias;
- permit contest, correction and independent verification;
- prevent the detector provider from becoming the authorization authority;
- avoid treating absence of detection as proof of human authorship.

Detector disagreement is evidence uncertainty. It is not proof of misconduct.

## 6. Admissibility pattern

A reference evaluation pattern is:

1. Determine whether the applicable policy requires provenance or disclosure.
2. Compare the declared production process with the available evidence.
3. Evaluate whether semantic meaning and accountable human control were preserved.
4. Treat detector outputs as supporting or conflicting observations.
5. Return `REQUIRES_STEP_UP` when material provenance is missing, disputed or inconsistent and a responsible human can resolve it.
6. Return `INDETERMINATE` when the evidence remains insufficient.
7. Return `INADMISSIBLE` only when the applicable policy, authority and evidence establish that the proposed action is outside the legitimate action space.
8. Bind the result and relevant provenance references to the execution receipt.

## 7. Threats

Implementations should account for:

- false accusation caused by detector error;
- AI laundering through repeated human or machine rewriting;
- selective or misleading disclosure;
- fabricated human-review attestations;
- semantic drift between the human's intent and the final artifact;
- loss of meaning through translation or normalization;
- detector bias across languages, dialects and writing styles;
- retroactive replacement of drafts or provenance records;
- over-collection of private prompts and working material;
- policy capture by a detector vendor or platform.

## 8. Boundary

REHT does not determine whether a text is morally authentic or whether AI use is acceptable in general.

REHT determines whether a proposed consequential action is admissible under the current authority, policy, evidence, context and governed state. Claudefishing detection may contribute evidence to that evaluation. It does not control the execution boundary.

## 9. Source context

This guidance was prompted by Substack's discussion of "Claudefishing" and its optional Pangram-based AI-content scanning. The architectural conclusion is provider-neutral: provenance, expectation integrity and accountable human control must be governed independently of any single detector.

Reference: https://post.substack.com/p/against-claudefishing
