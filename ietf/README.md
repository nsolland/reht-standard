# REHT IETF Internet-Draft package

This directory contains the individual Internet-Draft source and a small open reference/conformance implementation for the REHT execution-time authorization protocol.

## Submission artifact

Submit `draft-solland-reht-protocol-00.xml` to the IETF Datatracker.

The XML file is RFCXML v3 and is the authoritative submission source. Datatracker generates plaintext and HTML renderings from it. A plaintext `.txt` rendering may also be uploaded alongside the XML, but LaTeX is not a Datatracker Internet-Draft submission format.

Official submission guidance:

- https://authors.ietf.org/submitting-your-internet-draft
- https://authors.ietf.org/naming-your-internet-draft
- https://datatracker.ietf.org/submit

Before submission, render and validate with current `xml2rfc` and run `idnits`/the Datatracker validation flow as applicable.

Example local rendering:

```bash
python -m pip install xml2rfc
xml2rfc --text --html draft-solland-reht-protocol-00.xml
```

## Reference implementation

`reht_reference_impl.py` demonstrates the protocol boundary without claiming to be the VALO production runtime.

Key invariants implemented:

- REHT obtains current authoritative state and performs the fresh commit-time authorization check.
- PEP invokes REHT in the consequence path and enforces the result; PEP does not originate organizational authority.
- RACS is deterministic binding only and uses the canonical v0.2 decision set: `ALLOW`, `MODIFY`, `DEFER`, `DENY`, `STEP_UP`, `HALT`.
- A failed REHT verification can never be expanded into `ALLOW`.
- Revocation between prepare and commit fails closed.
- Material action drift requires fresh REHT verification.
- Nonces are single-use and replay-resistant.
- Agent traces and trace signatures are claims/evidence, not authoritative state.
- Evidence uses issuer-local sequence plus causal parent hash; no global total order is claimed.

Run the demonstration:

```bash
cd ietf
python reht_reference_impl.py
```

Expected output:

```text
ALLOW effect-1
```

## Conformance tests

Run:

```bash
cd ietf
python -m pytest test_reht_conformance.py -q
```

The suite currently contains 31 tests covering the canonical RACS vocabulary, authority/scope/purpose checks, commit-time revocation, action drift, replay, PEP enforcement, non-authority agent traces, and causal evidence chaining.

## Standards boundary

This package is additive to the public REHT standards surface. It does not duplicate or supersede the canonical RACS runtime-wire contracts in `nsolland/Racs`, and it does not expose the private VALO production runtime.

W3C Verifiable Credentials or other credential systems may be composed with REHT as identity/credential representations. Credential validity does not replace fresh execution-time authority verification.
