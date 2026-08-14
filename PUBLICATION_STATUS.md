# Publication Status

Status date: 2026-08-14

## Current fact

`nsolland/reht-standard` is currently hosted as a **private GitHub repository**.

The repository content is being prepared as a public, vendor-neutral REHT standard and conformance surface under Apache License 2.0, but public-release intent and actual repository visibility are separate facts.

Until GitHub visibility is changed to public, this repository MUST NOT be described as publicly accessible.

## Intended public release

The intended public release includes:

- normative REHT-specific specification material;
- conformance requirements and machine-readable vectors;
- threat/boundary documentation;
- Apache-2.0 license, notice and trademark terms;
- contribution and security guidance.

It does not include VALO production runtime code, proprietary evaluation logic, customer integrations, internal thresholds, deployment secrets or private collaboration material.

## Public-release gate

Before changing repository visibility to public, verify:

1. no credentials, tokens, private keys or customer data are tracked;
2. no private partner correspondence or unpublished third-party material is present;
3. every external citation may be redistributed or is referenced rather than copied improperly;
4. README, specification and conformance documents agree on scope and ownership;
5. `reht-standard` is presented as a standards/conformance source, not the canonical VALO runtime implementation;
6. current execution-architecture references do not restore historical V5-Core/RACS ownership errors;
7. CI/conformance checks are green on the exact release head;
8. license/NOTICE/TRADEMARKS files are present and internally consistent;
9. a release tag/version is selected;
10. GitHub repository visibility is explicitly changed to `public` by an authorized repository administrator.

## Release-state vocabulary

Use these terms precisely:

- **public-release candidate** — content intended for public release but repository may still be private;
- **public repository** — GitHub metadata reports visibility `public`;
- **published release** — a public repository has an identified tagged/versioned release artifact;
- **conformant implementation** — a separate implementation has passed the applicable conformance requirements; repository publication alone does not establish this.

## Current blocker

The remaining publication blocker recorded here is repository visibility. The connected automation used for this update does not expose a repository-visibility mutation, so the private→public switch requires a separate authorized GitHub administration action.
