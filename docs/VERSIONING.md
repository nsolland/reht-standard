# Versioning and Change Control

REHT uses Semantic Versioning for released specifications.

- Major: incompatible contract or semantic change.
- Minor: backward-compatible fields, objects or outcomes.
- Patch: corrections that do not change conformance behavior.

Draft identifiers use `-draft.N`. Release candidates use `-rc.N`.

Every release MUST include:

- tagged specification version;
- matching schema identifiers;
- changelog entry;
- migration notes for breaking changes;
- conformance test results;
- archived release artifacts.

Normative changes require a pull request describing rationale, compatibility impact, security impact and affected schemas. Released schema files are immutable. Corrections require a new version.
