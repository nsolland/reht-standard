# PEACE Protocol Security Policy

Status: publication proposal, 2026-08-19

## Scope

Security reports are relevant when they affect PEACE normative semantics, schemas, conformance vectors or published reference material.

Examples include:

- a protocol path that lets a replaceable worker produce consequence directly;
- stale or revoked authority remaining executable;
- state/evidence confusion that permits unauthorized state mutation;
- recovery semantics that permit identity transfer or single-provider takeover;
- route/provider selection creating authority;
- canonicalization/digest ambiguity that breaks cross-implementation binding;
- disclosure semantics that permit scope/purpose/destination escape;
- replay or action-substitution weaknesses;
- schema/conformance contradictions that could cause unsafe divergent implementations.

## Reporting

Until the dedicated PEACE repository defines its own security contact, report suspected vulnerabilities through the private security-reporting channel maintained for the hosting repository/VALO.

Do not disclose exploitable details publicly before coordinated review when doing so would materially increase risk.

## Security invariants

Security review treats the following as high-value boundaries:

```text
credential != principal
compute != authority
route != authority
candidate != decision
authorization != effect
evidence != authoritative state
recovery != identity transfer
provider != sovereignty root
```

The `NO_DIRECT_EFFECT_PATH` and fresh consequence-time authorization requirements are security boundaries, not optional architecture preferences.

## Fail-closed expectation

Where required authority, standing, state freshness, disclosure basis, exact-action binding or recovery evidence cannot be established, the safe protocol result is non-execution/non-admission rather than inferred permission.

## Coordinated protocol fixes

A security fix may be developed privately first. If it changes normative semantics, the public resolution MUST eventually include:

- a forward version;
- a public change/provenance record;
- compatibility/security impact;
- conformance vectors reproducing the vulnerable condition and expected refusal;
- an immutable release/tag once safe to publish.

Historical protocol tags are not rewritten.

## Non-security topics

General design proposals, feature requests, commercial support and certification requests are not security reports.

## No security warranty

Publication of PEACE or passing conformance vectors does not by itself establish that an implementation is secure, legally compliant, correctly deployed or suitable for a specific risk environment.
