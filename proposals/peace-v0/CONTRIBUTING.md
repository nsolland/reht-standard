# Contributing to PEACE Protocol

Status: publication proposal, 2026-08-19

## Purpose

PEACE welcomes implementation-neutral contributions that improve the protocol, schemas, conformance vectors, security model, documentation and interoperability.

## Contribution licence

Unless explicitly marked otherwise, contributions accepted into PEACE are licensed under Apache License 2.0, matching the outbound project licence.

Contributors must have the right to submit their contribution.

## Developer Certificate of Origin style sign-off

Contributions SHOULD include a sign-off line in the commit message:

`Signed-off-by: Name <email>`

The sign-off represents that the contributor created the work or otherwise has the right to submit it under the project licence.

No CLA is required initially.

## Normative changes

A contribution that could change interoperable behavior MUST include:

- rationale/problem statement;
- proposed normative text;
- affected profile/schema/object;
- compatibility class;
- security/privacy impact;
- conformance impact;
- at least one negative case where relevant;
- migration impact;
- any known patent/IP dependency.

Normative changes follow `GOVERNANCE.md`.

## Protocol neutrality

Contributions MUST NOT make any of the following a mandatory authority root or permanent intermediary unless a separately named optional profile explicitly requires it:

- VALO;
- a specific cloud/provider;
- a specific model or model router;
- a specific compute provider;
- a specific payment rail;
- a specific device/OS;
- a specific identity provider;
- a specific storage system;
- a specific cryptographic vendor.

## Reference implementations

Reference code may demonstrate one implementation, but normative semantics MUST remain expressible independently of that codebase.

A language-specific implementation detail MUST NOT become normative merely because the reference implementation uses it.

## Third-party material

Do not submit:

- code or text you do not have rights to redistribute;
- confidential employer/customer material;
- private partner correspondence;
- credentials/secrets;
- incompatible third-party licensed material;
- copied standards text where redistribution is not permitted.

References are preferred over copying third-party normative text unless redistribution rights are clear.

## Conformance changes

Any new normative requirement SHOULD have corresponding machine-readable conformance coverage.

Where the requirement is security- or authority-sensitive, include a refusal/negative vector rather than only a happy-path test.

## AI-assisted contributions

AI assistance is permitted, but the human contributor remains responsible for provenance, correctness, licence compatibility and the submitted result.

Generated content does not acquire standing merely because it was produced by a model.

## Review standard

Review asks:

1. Is this actually required by the PEACE world contract?
2. Does it preserve state/authority/recovery separation?
3. Does it preserve provider neutrality?
4. Can an independent implementation reproduce the semantics?
5. Is negative behavior testable?
6. Does the change belong in core or an optional profile?

## Conduct

Technical disagreement is expected. Discuss behavior, evidence and protocol consequences rather than contributors.
