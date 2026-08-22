# Public repository publication policy

This repository is a public standards surface. A branch push is public disclosure; merge review is therefore too late to be the primary IP gate.

No person, model, agent, automation or external tool may push new substantive research, architecture, unpublished mechanism or cross-project synthesis here until an explicit human IP/publication review has approved the exact material for public disclosure.

Unreleased or potentially IP-sensitive work must be developed in a private repository or non-public workspace. Only the minimum approved standards/interoperability surface may be promoted here.

Public by design:

- normative REHT protocol and standards semantics;
- schemas, interoperability profiles and conformance vectors deliberately selected for public standardization;
- reference implementations needed for conformance where explicitly approved;
- public regulatory/standards mappings that do not reveal protected implementation or research architecture.

Not public by default:

- discovery lineage and research derivations;
- unrelated protocol internals duplicated from another canonical repository;
- unpublished mechanisms, architecture or adaptive-network research;
- internal product topology, commercial roadmap or assurance methods;
- cross-project synthesis revealing how components combine into a protected system;
- partner/customer material, private data, credentials or production configuration.

Before promotion, review the exact diff and ask whether every disclosed element is necessary for the intended public standard or interoperability claim, whether a capable model could combine it with other public material to reconstruct protected work, and whether the same public objective can be achieved with less disclosure.

If uncertain, do not push it to this repository.
