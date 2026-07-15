# REHT Standard

REHT defines a public, model-agnostic standard for representing governed AI-mediated actions before execution.

Core question:

> Is this action admissible to execute in the present governed state?

REHT Standard is a static specification repository. It does not contain VALO production code, runtime logic, customer integrations, internal thresholds, proprietary evaluation methods or deployment configuration.

## Scope

This repository defines public contracts for:

- Action Envelope
- Authority Context
- Evidence Package
- Policy Context
- Governance State
- Continuous Integrity events
- Admissibility Result
- Execution Receipt

## Architecture position

```text
Reality -> Observation -> Evaluation -> REHT admissibility -> Execution boundary -> Receipt
```

REHT Standard defines the public contract at the admissibility and evidence boundary. Implementations remain independent.

## Repository map

- `SPECIFICATION.md` — normative specification seed
- `docs/BOUNDARIES.md` — public scope and exclusions
- `schemas/action-envelope.schema.json` — reference Action Envelope schema
- `schemas/execution-receipt.schema.json` — reference receipt schema
- `examples/` — non-production examples
- `NOTICE` — attribution and trademark notice
- `CONTRIBUTING.md` — contribution rules
- `SECURITY.md` — security reporting guidance

## Status

Early public specification. Not a certified standard, legal opinion, compliance guarantee or production authorization system.

## Licensing

Code, schemas and examples are licensed under Apache License 2.0.

Specification text and documentation may be quoted and adapted with attribution to VALO Research Group AS. REHT and VALO names and marks are not licensed for branding or endorsement.