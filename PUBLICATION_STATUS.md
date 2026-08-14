# Publication Status

Status date: 2026-08-14

## Current fact

`nsolland/reht-standard` is a **public GitHub repository**.

The repository is the public, vendor-neutral REHT standards and conformance surface under Apache License 2.0. Repository visibility does not change ownership boundaries: this repository does not become the canonical VALO production runtime implementation by being public.

## Public repository contents

The public repository includes:

- normative REHT-specific specification material;
- conformance requirements and machine-readable vectors;
- threat/boundary documentation;
- public GitHub Actions validation;
- public specification governance and contribution rules;
- Apache-2.0 license, notice and trademark terms;
- contribution and security guidance.

It does not include VALO production runtime code, proprietary evaluation logic, customer integrations, internal thresholds, deployment secrets or private collaboration material.

## Release state

The current specification line is `0.3.0-draft.1`. The canonical next prerelease is `v0.3.0-draft.1` on an exact green release head.

The prior `0.2.0-draft.1` line remains historical provenance. An existing historical `v0.1.0` tag predates the current release discipline and MUST NOT be moved, deleted or retargeted. Corrective versioning is forward-only.

A release is considered published only when the specification version, tag and exact commit are aligned and the validation workflow is green on that commit.

## Versioned-release gate

Before publishing an exact snapshot, verify:

1. no credentials, tokens, private keys or customer data are tracked;
2. no private partner correspondence or unpublished third-party material is present;
3. every external citation may be redistributed or is referenced rather than copied improperly;
4. README, specification and conformance documents agree on scope, version and ownership;
5. `reht-standard` is presented as a standards/conformance source, not the canonical VALO runtime implementation;
6. current execution-architecture references do not restore historical ownership errors;
7. validation/conformance checks are green on the exact release head;
8. license/NOTICE/TRADEMARKS files are present and internally consistent;
9. `GOVERNANCE.md`, changelog and accepted change records account for every normative change in the release;
10. the exact release tag/version/hash is recorded.

## Release-state vocabulary

- **public repository** — GitHub metadata reports visibility `public`;
- **prerelease candidate** — repository content is prepared for an identified draft version but the exact release artifact has not yet been published;
- **published prerelease** — public repository plus an identified prerelease tag/version/hash on a validated release head;
- **conformant implementation** — a separate implementation has passed the applicable conformance requirements; repository publication alone does not establish this.

## Canonical-authority transition

If a publisher, standards body, foundation or consortium later becomes the normative authority, the transfer must be explicit under `GOVERNANCE.md`: identify the external canonical source, freeze/tag the last repository-owned normative release, update `CANONICAL.md`, map local conformance artifacts to the external version, and avoid simultaneous competing canonical sources.
