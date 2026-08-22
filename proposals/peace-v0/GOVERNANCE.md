# PEACE Protocol Governance

Status: publication proposal, 2026-08-19

## 1. Scope

This file defines how PEACE normative changes are proposed, reviewed, accepted, versioned and, if appropriate, transferred to an external standards authority.

PEACE governance exists to prevent silent semantic drift and vendor capture while preserving the ability to evolve the protocol quickly during the v0.x period.

## 2. Current editorial authority

Until an explicit canonical transfer is recorded, VALO acts as editor/maintainer of the public PEACE specification.

Repository ownership does not permit silent normative changes. Normative meaning changes only through accepted, versioned public changes.

## 3. Normative vs non-normative surfaces

Normative surfaces may include:

- protocol specification text;
- schemas;
- mandatory conformance requirements and vectors;
- versioned profile definitions.

Non-normative surfaces include:

- discussions;
- issues not yet accepted;
- papers and presentations;
- examples;
- reference implementations;
- commercial VALO products and services;
- partner feedback and design notes.

A reference implementation is evidence of implementability, not the definition of the protocol.

## 4. Change proposals

Every substantive normative change requires a public proposal record containing:

- stable proposal identifier;
- problem/rationale;
- proposed normative change;
- affected protocol objects/profiles;
- compatibility class;
- security/privacy impact;
- authority/state/recovery impact where applicable;
- conformance impact and required negative cases;
- migration impact;
- external references/evidence;
- decision and decision date;
- target version.

A GitHub issue or pull request may serve as the proposal record.

## 5. Acceptance gates

A normative change may be accepted only when:

1. its compatibility class is explicit;
2. affected schemas/profiles are identified;
3. required negative behavior is specified;
4. security/privacy impact is recorded;
5. the change preserves implementation neutrality unless an explicit profile says otherwise;
6. the change does not make a provider or VALO a mandatory authority/intermediary;
7. conformance/validation checks are green on the exact head;
8. changelog and target version are updated.

## 6. Constitutional review

Any proposal that changes one of the following receives heightened review:

- authority root;
- authoritative-state semantics;
- standing/delegation/revocation semantics;
- disclosure boundary;
- fresh consequence authorization;
- no-direct-effect-path invariant;
- recovery identity-preservation semantics;
- evidence vs state separation;
- provider/route neutrality;
- implementation vs protocol separation.

A proposal that weakens one of these must explicitly state why PEACE remains sovereign under the world contract.

## 7. Versioning

PEACE uses semantic versioning for normative protocol meaning.

- MAJOR — incompatible change to existing normative semantics.
- MINOR — additive normative semantics/profile capability.
- PATCH — clarification/correction with no conformance change.

Drafts use immutable prerelease identifiers such as `0.1.0-draft.1`.

Historical tags are never moved, deleted or retargeted.

## 8. Extensions

Vendors may define extensions without changing PEACE core.

Extensions MUST NOT:

- redefine core fields with incompatible meaning;
- claim authority merely because an extension is present;
- bypass mandatory conformance behavior;
- imply official certification without authorization.

Extensions SHOULD be namespaced and independently ignorable where interoperability permits.

## 9. Certification independence

Protocol conformance and commercial certification are separate.

Anyone may implement and self-test PEACE under the public licence. A commercial `PEACE Certified` programme, if created, may add independent testing/assurance requirements but cannot revoke the right to implement the protocol.

## 10. External standards transfer

If a neutral foundation, consortium or formal standards body becomes canonical:

1. record the transfer publicly;
2. identify external canonical source and effective version/date;
3. tag/freeze the last locally canonical release;
4. map local schemas/conformance vectors to external versions;
5. preserve the Apache-licensed history;
6. avoid two simultaneous canonical sources for the same normative contract.

## 11. Emergency security process

A vulnerability may be coordinated privately before disclosure. Any resulting normative change still receives a public forward version and decision record when disclosure is safe.

## 12. Decision rule

> **Discussion proposes. Evidence informs. Conformance tests constrain. A versioned accepted specification decides.**
