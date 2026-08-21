# Personalized medicine: evidence is not execution authority

Status: non-normative explanatory case.

This note illustrates a REHT boundary using individualized cancer therapy. It is not medical guidance, a treatment recommendation, or a claim that REHT determines clinical appropriateness.

## External signal

On 19 August 2026, Moderna reported positive topline Phase 3 INTerpath-001 results for intismeran autogene plus pembrolizumab as adjuvant treatment in patients with completely resected Stage IIB-IV melanoma, describing a clinically meaningful improvement over pembrolizumab alone.

Intismeran autogene (V940/mRNA-4157) is an investigational individualized neoantigen therapy. Merck describes it as synthetic mRNA encoding up to 34 neoantigens selected from the unique mutational signature of an individual patient's tumor.

The important governance point is not the therapeutic result itself. It is the separation between evidence and authority to cause a specific consequence.

## The boundary

A system may hold strong population-level evidence that a treatment works and still lack authority to administer it to a particular patient.

The execution-relevant chain can include, at minimum:

1. population-level clinical evidence;
2. current regulatory and indication state;
3. current patient-specific evidence and treatment eligibility;
4. valid clinician/institutional authority and consent state;
5. the exact treatment/order/action being proposed;
6. current execution constraints immediately before consequence.

No upstream item is a bearer token for the downstream ones.

`positive trial evidence != patient-specific execution authority`

Likewise:

`same treatment class + same diagnosis != same execution authority`

In individualized medicine the distinction becomes especially concrete because the treatment artifact itself may be derived from patient-specific biological evidence.

## Material-state-change example

Assume a treatment action was previously considered admissible under the then-current patient state and authority context.

Before administration, new material evidence appears: for example, updated pathology, a changed clinical condition, a newly discovered contraindication, changed consent, a revised order, or another execution-relevant state transition.

The historical approval and its provenance remain evidence that the earlier state was validly evaluated. They do not silently remain current execution authority.

At the consequence boundary, REHT requires the execution-relevant action, authority, governed state, evidence and constraints to be re-established under the current state. If a material mismatch cannot be resolved, the prior result is non-executable.

This is the same core distinction expressed by REHT's causal-continuity model:

> evidence may support an admissibility determination; evidence does not self-authorize consequence.

## What REHT does not do

REHT does not diagnose disease, select a treatment, replace a clinician, establish regulatory approval, or infer authority from scientific evidence.

Those remain separate authoritative domains. REHT governs whether the exact proposed consequence is still admissible under the current authoritative inputs at execution time.

External clinical, regulatory, consent, identity or authority systems may supply governed inputs without becoming REHT dependencies.

## Why this case matters

Personalized medicine increases the number of execution-relevant states that can differ between two superficially similar actions. A population-level conclusion can be identical while patient-specific evidence, consent, authority, order state or constraints differ materially.

That makes the execution question irreducibly specific:

> Is this exact action still admissible for this exact subject, under the authority and state that exist now?

## Sources

- Moderna, 19 August 2026, “IR Insights: Recapping Positive Phase 3 Topline Results for Intismeran Autogene Plus Pembrolizumab in Adjuvant Melanoma”: https://www.modernatx.com/ir-insights-phase-3-intesmeran
- Merck, 1 June 2026, five-year Phase 2b follow-up and description of the individualized neoantigen program: https://www.merck.com/news/moderna-and-merck-present-5-year-data-for-intismeran-autogene-in-combination-with-keytruda-pembrolizumab-in-patients-with-high-risk-stage-iii-iv-melanoma-following-complete-resection-at-the-20/
- Financial Times discussion supplied as the external market/clinical-evidence prompt: https://www.ft.com/content/d8ff1233-01ff-496d-aa18-91233c1db051
