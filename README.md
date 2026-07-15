# reht Standard

[![Status](https://img.shields.io/badge/status-draft%20v0.1-1f6f6d)](./CHANGELOG.md)
[![License](https://img.shields.io/badge/license-Apache%202.0-0b1d33)](./LICENSE)
[![Specification](https://img.shields.io/badge/specification-public-2e3a47)](./SPECIFICATION.md)
[![Schemas](https://img.shields.io/badge/schemas-JSON%20Schema%202020--12-2e3a47)](./schemas)
[![Validation](https://img.shields.io/github/actions/workflow/status/nsolland/reht-standard/validate.yml?branch=main&label=schema%20validation)](../../actions)

reht is a public, model-agnostic standard for representing and evaluating governed AI-mediated actions before execution.

> Is this action admissible to execute in the present governed state?

reht separates AI reasoning from execution authority. A model may propose an action. reht defines the public contracts required to determine whether that action is admissible under the current authority, evidence, policy, context and governance state.

## Why reht exists

Authentication answers who is acting.

Authorization answers what that actor is permitted to do.

reht addresses the missing question:

> Is this specific action still admissible now?

This matters because authority, evidence, policy and system state can change between proposal and execution.

## Architecture position

```text
Reality
  ↓
Observation
  ↓
Evaluation
  ↓
reht admissibility
  ↓
Execution boundary
  ↓
Receipt
```

reht defines the public contract at the admissibility boundary. It does not define a proprietary runtime implementation.

## Public contracts

The standard defines:

- Action Envelope
- Authority Context
- Evidence Package
- Policy Context
- Governance State
- Delegation Chain
- Admissibility Result
- Continuous Integrity Event
- Execution Receipt

## Reference outcomes

A conforming implementation returns one bounded semantic result:

- `ADMISSIBLE`
- `INADMISSIBLE`
- `INDETERMINATE`
- `REQUIRES_STEP_UP`
- `NO_LONGER_ADMISSIBLE`

These are admissibility outcomes, not execution commands.

## Start here

1. Read [`SPECIFICATION.md`](./SPECIFICATION.md).
2. Review [`docs/BOUNDARIES.md`](./docs/BOUNDARIES.md).
3. Review [`CONFORMANCE.md`](./CONFORMANCE.md).
4. Inspect the schemas in [`schemas/`](./schemas).
5. Validate against the reference examples in [`examples/`](./examples).
6. Review the public threat model in [`docs/THREAT_MODEL.md`](./docs/THREAT_MODEL.md).
7. Review [`TRADEMARKS.md`](./TRADEMARKS.md) before making compatibility or certification claims.

## Repository map

```text
.
├── SPECIFICATION.md
├── README.md
├── CHANGELOG.md
├── CONFORMANCE.md
├── CONTRIBUTING.md
├── SECURITY.md
├── TRADEMARKS.md
├── LICENSE
├── NOTICE
├── docs/
│   ├── BOUNDARIES.md
│   ├── THREAT_MODEL.md
│   └── VERSIONING.md
├── schemas/
│   ├── action-envelope.schema.json
│   ├── authority-context.schema.json
│   ├── evidence-package.schema.json
│   ├── policy-context.schema.json
│   ├── governance-state.schema.json
│   ├── admissibility-result.schema.json
│   ├── continuous-integrity-event.schema.json
│   └── execution-receipt.schema.json
├── examples/
│   ├── action-envelope.valid.json
│   ├── admissibility-result.valid.json
│   ├── continuous-integrity-event.valid.json
│   └── execution-receipt.valid.json
└── .github/workflows/
    └── validate.yml
```

## Conformance

A conforming implementation must:

- consume or produce versioned reht objects;
- preserve authority, evidence, policy and governance-state references;
- return exactly one defined admissibility outcome;
- never represent `INDETERMINATE` as admissible;
- produce an Execution Receipt for terminal decisions;
- preserve continuous-integrity events that materially affect validity;
- avoid claiming certification solely because schemas validate.

See [`CONFORMANCE.md`](./CONFORMANCE.md) for the complete requirements.

## What this repository does not contain

This repository intentionally excludes:

- VALO production code;
- VAIG evaluation logic;
- proprietary reht decision logic;
- BARO collection or analysis code;
- execution-kernel code;
- internal thresholds, weights or risk models;
- customer integrations or customer data;
- credentials, infrastructure or deployment configuration;
- unpublished research or patent material.

Schema compatibility does not imply implementation equivalence, certification, endorsement or regulatory compliance.

## Status

Current release: `0.1.0-draft`

This is an early public specification intended for review, implementation experiments and controlled interoperability work. It is not a certified standard, legal opinion, compliance guarantee or production authorization system.

## Versioning

reht follows semantic versioning for public contracts:

- major: breaking contract changes;
- minor: backward-compatible additions;
- patch: clarifications and corrections.

See [`docs/VERSIONING.md`](./docs/VERSIONING.md).

## Security

Security issues should not be reported through public issues. Follow [`SECURITY.md`](./SECURITY.md).

## Contributing

Public contributions are welcome when they improve clarity, interoperability, safety or conformance without exposing private implementation details.

See [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## Licensing and trademarks

Code, schemas, examples and repository automation are licensed under Apache License 2.0.

The specification and documentation may be quoted and adapted with attribution to VALO Research Group AS.

The Apache License does not grant rights to the names `reht` or `VALO`, their logos, certification marks or visual identity.

The terms `reht-compatible` and `reht-conformant` are subject to the conditions in [`TRADEMARKS.md`](./TRADEMARKS.md). The term `reht-certified` is reserved for a certification programme formally operated or authorized by VALO Research Group AS.

Copyright © 2026 VALO Research Group AS.