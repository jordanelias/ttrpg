# Evidence, Pressure, and Persuasion-Jitter — emergent behavior validated by precedent

Bottom-up: three additions to the substrate, their emergent behavior read from the primitives.
Top-down: each checked against the institution it models. All 46 tests pass.

## Evidence apparatus — forensic proof  ✓
**Design.** A side holds a dossier of items, each with a **hidden weight** (the engine's true value =
relevance × quality) the player never sees — the player sees only *that it holds evidence* (a count).
Presenting a **relevant** item (its ground == the live stasis) adds its value as **hard proof**:
readiness-independent (a document speaks regardless of the advocate's standing), weighted by how much
*this* adjudicator credits that kind of proof. **Corroboration** accumulates with **diminishing
returns**; **irrelevant** evidence has nothing to present.

**Emergent.** An evidence-holder beats a non-holder 1.00; three relevant items beat one (0.77); a
holder-vs-holder stays symmetric; irrelevant evidence is no edge (coin-flip). The value stays hidden
(the view exposes the count, not the weight).

**Precedent.** This is the forensic core the corpus keys the system to (stasis = what is *at issue*;
the proof is the substance). It matches Roman/medieval evidence practice: **testimony and documents
carry the case**, **corroboration strengthens it** ("in the mouth of two or three witnesses"),
**relevance gates admissibility**, and **the court — not the advocate — weighs the proof** (hence the
hidden value: you present, the tribunal adjudges). The hard-proof/rhetoric split (evidence is
readiness-independent, argument is readiness-gated) matches the intuition that a damning document
convicts whatever the pleader's standing, while a rhetorical flourish needs the audience disposed.

## Institutional / public pressure on the adjudicator  ✓
**Design.** A `Pressure(toward, institutional, public)` is a force on the adjudicator beyond role and
character. **Institutional** pressure is a thumb on the scale — it tilts advancement toward the
favoured side (the Crown/Church/party leaning on the verdict). **Public** pressure raises the
adjudicator's **leak** (susceptibility) — under the public eye the judge bends toward the room's
mood/character — and tilts toward the publicly favoured side.

**Emergent.** Institutional pressure toward A moves the verdict monotonically (0.48 → 0.87 → 0.96 as
it rises). Public pressure **unlocks a disciplined crowd-judge**: a demagogue who *loses* before a
by-the-book judge (0.37) *wins* once public pressure raises the leak and the judge's pathos-character
governs (0.98). No pressure → symmetric.

**Precedent.** Adjudicators are never insulated. **Institutional** pressure is the documented reality
of judges ruling as the Crown wants (political/show trials, royal interference) — the verdict bends.
**Public** pressure is the jury swayed by the mob, the assembly carried by its mood, the sovereign's
grace bending to court factions and popular sentiment. Modelling public pressure as *raised
susceptibility* (the disciplined judge's guard drops under scrutiny, the character beneath the role
takes over) matches how popular pressure actually operates on an adjudicator.

## Persuasion-jitter — resolution, not exact-tie deadlock  ✓
**Design.** A small (±8%) variability on each advancement increment — no two arguments land
identically. **Emergent.** The high-faculty exact-tie draws (matched masters getting *identical*
discrete advancement → ~40% draws at faculty 7) collapse to ~0: a winner emerges by the margin.
**Precedent.** Persuasion has irreducible variability (delivery, mood, the moment); a perfectly
even contest is decided by a hair rather than deadlocked. (A deliberate **hung** outcome — tied vote,
hung jury — can be re-introduced as a venue option via a draw-margin; it is not the default.)

## Bottom line
Evidence reproduces forensic proof (relevant, corroborated, court-adjudged, hidden-valued); pressure
reproduces the institutional and popular forces that bend real adjudication; the jitter removes an
artifact and makes contests resolve. All three are general primitives the venue composes — none is
bespoke to one institution.
