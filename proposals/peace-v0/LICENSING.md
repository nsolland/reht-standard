# PEACE Protocol — Licensing Policy

Status: publication proposal, 2026-08-19

## Decision

The intended public PEACE protocol repository SHALL use **Apache License 2.0** for the specification text, schemas, conformance vectors, examples, reference code and repository automation unless a later accepted governance proposal changes that policy.

The objective is simple: PEACE must be free to adopt, free to implement, commercially usable, forkable and independently implementable without requiring a licence fee or permanent relationship with VALO.

## Why Apache 2.0

Apache 2.0 provides:

- broad commercial and non-commercial use;
- modification and redistribution rights;
- an explicit contributor patent grant;
- patent-retaliation protection;
- preservation of attribution/NOTICE information;
- no field-of-use restriction;
- no requirement that independent implementations or derivative products be open sourced.

The patent grant is materially important for an interoperability protocol intended for implementation by infrastructure providers, enterprises and device/platform vendors.

## Royalty-free interoperability

A conforming PEACE implementation MUST NOT require payment to VALO merely for implementing the public protocol.

The public protocol, public schemas and mandatory conformance semantics are intended to be royalty-free under Apache 2.0.

This does not prevent commercial services around PEACE, including managed control planes, certification, assurance, support, recovery services, hosted registries/resolvers, adapters, enterprise deployment or other operational infrastructure.

## No protocol capture

The licence SHALL NOT:

- require use of VALO software;
- require use of a VALO-operated service;
- make VALO a mandatory intermediary;
- restrict implementation to particular models, clouds, compute providers, payment rails, identity providers or devices;
- create field-of-use restrictions;
- condition protocol implementation on certification.

A third party must be able to implement PEACE from the public specification and conformance material alone.

## Trademark separation

Apache 2.0 does not grant trademark rights.

Descriptive statements such as `implements PEACE Protocol vX.Y` may be permitted under the trademark policy when accurate. Claims such as `PEACE Certified`, official badges, logos or endorsement remain controlled separately.

Certification is therefore a commercial/trust programme, not a licence gate to implementation.

## Contributions

Default contribution policy:

- inbound licence = outbound licence (Apache 2.0);
- contributors certify origin/right-to-submit through Developer Certificate of Origin style sign-off;
- no contributor licence agreement is required initially;
- contributions that introduce known third-party licence incompatibility MUST NOT be accepted;
- normative contributions require provenance, compatibility and conformance impact under `GOVERNANCE.md`.

A CLA may be introduced later only by explicit governance decision if required by a foundation, standards body or material legal need.

## Patents

PEACE should not rely on a separate patent licence where Apache 2.0 already supplies the contributor patent grant.

If a contributor knows that implementation of a proposed normative requirement necessarily depends on patent claims they cannot license under the project terms, that fact MUST be disclosed during proposal review.

No contributor may describe a known patent-encumbered extension as mandatory PEACE conformance without the applicable rights being available under the project policy.

## Future standards transfer

If PEACE moves to an external foundation, consortium or formal standards body, the canonical venue may adopt its own IPR policy. Any transfer must preserve a clear mapping from the Apache-licensed repository history to the external standard and must not retroactively revoke rights already granted under Apache 2.0.

## Commercial boundary

Canonical rule:

> **The protocol is free. Operational trust infrastructure is commercial.**

VALO may charge for implementation, hosting, certification, assurance, support, managed recovery, conformance services and consequence infrastructure. It does not charge for the mere right to speak PEACE.
