# PEACE Protocol — Publication Plan

Status: active publication plan, 2026-08-19

## Objective

Establish PEACE as a public, independently implementable, vendor-neutral protocol before the architecture becomes captured by any single provider or product stack.

The publication objective is not to publish every VALO implementation detail. It is to publish the **protocol physics**: world contract, invariants, normative semantics, schemas, conformance vectors, governance and release provenance.

## Publication principles

1. **Publish semantics before product polish.**
2. **Open protocol; commercial operational infrastructure.**
3. **No vendor — including VALO — is a required intermediary.**
4. **Normative protocol != reference implementation.**
5. **Historical snapshots are immutable and forward-only.**
6. **Every substantive normative change has public provenance.**
7. **Conformance is observable behaviour, not branding.**

## Phase 0 — Public seed / timestamp

Venue: `nsolland/reht-standard`, `proposals/peace-v0/`.

Purpose:

- establish public lineage and timestamp;
- publish the derivation from `govern the workspace, not the worker`;
- publish the world contract, protocol proposal, schema and conformance seed;
- make clear that PEACE is broader than REHT and is not normative REHT material.

Exit gate:

- proposal files public;
- licensing policy published;
- publication/governance/security/trademark docs prepared;
- validation green on exact proposal head.

## Phase 1 — Dedicated repository

Target repository: `nsolland/peace-protocol` or equivalent neutral canonical home.

Initial repository contents:

```text
README.md
LICENSE
NOTICE
LICENSING.md
GOVERNANCE.md
CONTRIBUTING.md
SECURITY.md
TRADEMARKS.md
PUBLICATION_STATUS.md
PUBLICATION_PLAN.md
CHANGELOG.md
protocol/
  PEACE_WORLD_V0.md
  PEACE_PROTOCOL_V0.md
schemas/
  peace-envelope-v0.schema.json
conformance/
  conformance-v0.json
examples/
.github/workflows/
```

Migration requirements:

- preserve the originating REHT proposal PR URL and exact seed commit hash;
- record the first dedicated-repository import commit;
- leave the original proposal directory intact as historical lineage;
- update the original proposal README to point to the canonical repository after transfer;
- do not claim canonical transfer until the destination repository is public and validated.

## Phase 2 — First immutable draft release

Target: `v0.1.0-draft.1` unless publication review identifies a better initial version.

Required gate:

- licence/NOTICE/trademark terms present and consistent;
- specification and schemas agree;
- mandatory conformance vectors executable/validate cleanly;
- threat model and security reporting process present;
- governance and contribution process present;
- no private/customer/partner material present;
- exact release head green;
- tag, version and commit hash aligned;
- release notes identify status as draft/prerelease.

The first immutable draft is the first clean public citation target.

## Phase 3 — Independent derivation and implementation challenge

PEACE claims should be tested by independent implementation, not by internal architecture resemblance.

Publish two exercises:

1. **Derivation challenge** — provide only the world contract and ask independent implementers/reasoning systems to derive the minimum required boundaries/invariants.
2. **Black-box conformance challenge** — implement PEACE without reading the VALO reference implementation and run the mandatory vectors.

Desired evidence:

- at least two implementation languages or independent implementations;
- one implementation not maintained by VALO if available;
- documented divergence points;
- negative-case results for direct-effect bypass, stale authority, route-as-authority, evidence-as-state and recovery transfer.

Independent derivation is evidence. Passing the normative conformance profile is the interoperability claim.

## Phase 4 — Public v0.x protocol line

Publish forward-only draft/minor releases as semantics mature.

Priority profiles:

- core sovereign-domain profile;
- state replication/lineage profile;
- recovery federation profile;
- capability/disclosure profile;
- execution-boundary binding to REHT;
- organisation-domain profile;
- settlement/consequence profile;
- provider/route interchangeability profile.

Do not force all profiles into core if independent interoperability is cleaner through optional profiles.

## Phase 5 — External governance / standardization

Once there is external implementation interest, evaluate transfer or co-governance through a neutral foundation, consortium, IETF-like process or other standards venue.

A transfer requires:

- explicit canonical-authority decision;
- exact last repository-owned release tag/hash;
- public mapping from local versions to external versions;
- preservation of Apache-licensed history;
- no simultaneous competing canonical source;
- continued availability of conformance artifacts.

## Publication channels

Minimum:

- public GitHub canonical repository;
- immutable Git tag/releases;
- DOI/archive snapshot when the first coherent draft is ready;
- short protocol paper/preprint describing derivation, invariants and boundaries;
- public conformance vectors.

Optional later:

- IETF/standards draft;
- foundation/consortium submission;
- independent test/certification programme.

## What is deliberately not published as protocol

PEACE publication does not require publication of:

- VALO production control-plane code;
- proprietary evaluation logic;
- internal risk thresholds;
- customer adapters/configuration;
- deployment secrets;
- commercial recovery operations;
- certification backend;
- internal assurance methods;
- private partner material.

## Publication sequence

Canonical sequence:

```text
public seed
  -> dedicated canonical repo
  -> licensing/governance/security complete
  -> green immutable draft tag
  -> independent derivation/conformance
  -> v0.x evolution
  -> external governance if warranted
```

## Core publication statement

> **PEACE is free to adopt and independently implement. No vendor, including VALO, is required for the protocol to remain usable.**
