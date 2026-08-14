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
- Apache-2.0 license, notice and trademark terms;
- contribution and security guidance.

It does not include VALO production runtime code, proprietary evaluation logic, customer integrations, internal thresholds, deployment secrets or private collaboration material.

## Versioned-release gate

Before describing an exact snapshot as a published release, verify:

1. no credentials, tokens, private keys or customer data are tracked;
2. no private partner correspondence or unpublished third-party material is present;
3. every external citation may be redistributed or is referenced rather than copied improperly;
4. README, specification and conformance documents agree on scope and ownership;
5. `reht-standard` is presented as a standards/conformance source, not the canonical VALO runtime implementation;
6. current execution-architecture references do not restore historical V5-Core/RACS ownership errors;
7. CI/conformance checks are green on the exact release head;
8. license/NOTICE/TRADEMARKS files are present and internally consistent;
9. an exact release tag/version/hash is selected.

## Release-state vocabulary

Use these terms precisely:

- **public-release candidate** — content intended for public release but repository may still be private;
- **public repository** — GitHub metadata reports visibility `public`;
- **published release** — a public repository has an identified tagged/versioned release artifact;
- **conformant implementation** — a separate implementation has passed the applicable conformance requirements; repository publication alone does not establish this.

## Current blocker

There is no repository-visibility blocker. The repository is public. The remaining step for a formally published release is to select and validate an exact version/tag/hash on a green release head.
