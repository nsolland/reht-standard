# REHT Standard Governance

Status: draft-governance, 2026-08-14

This file defines how normative REHT changes move from idea to versioned specification and how canonical authority changes if an external publisher, standards body or community governance process later takes over.

## 1. Current editorial authority

Until an explicit transfer is recorded, this repository is the canonical public REHT specification/conformance surface and Njål Gaute Solland acts as the specification editor/maintainer.

The editor may merge changes only through the process below. Repository ownership is not permission to silently change normative meaning.

## 2. Discussion is not specification

GitHub Discussions, issues, papers, workshops, publisher review, partner feedback and external standards discussions are proposal/evidence surfaces.

They are non-normative until a change is incorporated into a versioned specification commit/release through an accepted change proposal.

No statement in a discussion thread, paper draft, presentation or publisher correspondence silently changes the normative contract.

## 3. Change proposal record

Every normative change requires a public change record containing:

- stable proposal ID;
- problem/rationale;
- proposed normative text;
- affected objects/profiles;
- compatibility class;
- security impact;
- conformance impact and negative cases;
- migration impact;
- external references/evidence;
- decision and decision date;
- target specification version.

The GitHub issue or pull request number may serve as the proposal ID while this repository remains the canonical venue.

## 4. Change classes and versioning

REHT uses semantic versioning for specification meaning:

- MAJOR: breaking change to existing normative contracts or outcome semantics;
- MINOR: substantive additive normative requirement, optional interoperable field/profile, or expanded conformance surface;
- PATCH: clarification/correction that does not change conformance requirements.

Prerelease drafts use immutable forward-only identifiers such as `MAJOR.MINOR.PATCH-draft.N`. Historical tags are never moved, deleted or retargeted.

Examples:

- `0.2.0-draft.1 -> 0.3.0-draft.1`: new persistent-state and governing-contract continuity requirements;
- `0.3.0-draft.1 -> 0.3.0-draft.2`: revised prerelease text/conformance during review without pretending the earlier snapshot never existed;
- future `1.x -> 2.0`: incompatible contract or semantic change.

Runtime/package versions are independent. A REHT specification bump does not force a VALO runtime or reference package to match numerically.

## 5. Acceptance gates

A normative proposal may be accepted only when:

1. the compatibility class is explicit;
2. affected schemas/profiles are identified;
3. required negative conformance behavior is specified;
4. security and migration impact are recorded;
5. public normative text is implementation-neutral and does not leak private runtime/IP;
6. validation/conformance checks are green on the exact head;
7. the changelog records the change and target version.

A change may be technically implemented privately before acceptance. Private implementation does not itself make the public standard normative.

## 6. Editorial vs normative changes

Editorial changes may correct spelling, links, formatting and non-normative explanation without a minor/major bump if they do not alter required behavior.

If reasonable implementers could behave differently because of a text change, treat it as normative.

## 7. External review and publisher phase

Publisher, journal, conference or formal-review comments are tracked as external review input. They do not overwrite the specification directly.

Each accepted review point maps to a public proposal/PR and forward version entry. Rejected or deferred points remain visible as discussion history where appropriate.

This preserves provenance between published papers and the executable/conformance standard.

## 8. Transfer to an external standards body

If an external standards body, foundation, consortium or other governance venue becomes the normative authority:

1. record the transfer explicitly in this file and `CANONICAL.md`;
2. identify the external canonical document/registry and effective version/date;
3. tag/freeze the last repository-owned normative release;
4. change this repository's role to reference implementation, mirror, profile or proposal incubator as applicable;
5. maintain an explicit mapping between external normative versions and local conformance artifacts;
6. do not claim two simultaneous canonical sources for the same normative contract.

After transfer, local experiments may continue on branches/drafts but cannot be described as normative until accepted through the external authority's process.

## 9. Emergency security changes

A security issue may be privately coordinated before disclosure. The resulting normative change still requires a public decision record and forward version/changelog entry once disclosure is safe.

Security urgency may shorten review time; it does not remove provenance or versioning requirements.

## 10. Decision provenance

For every published release, the release tag/hash plus changelog and accepted proposal history together form the normative provenance record.

The rule is simple:

> Discussion proposes. Evidence informs. Maintainers edit. A versioned accepted specification decides.
