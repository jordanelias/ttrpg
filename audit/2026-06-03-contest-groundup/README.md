# Social Contest — venue-determined engine (general two-party adjudicated discourse)

General **emergent primitives** + a **top-down Venue spec** that imposes the conditions. There is no
privileged "merits": the primitives accumulate a per-side **advancement** (modulated persuasion), and
the **venue's win-condition** decides what winning *is* and how it resolves. The venue also supplies
the **defeat-catalogue** (which faults are fatal). Numbers are `[SEED]`s. **36/36 tests pass.**

## Layers
- **contract.py** — shared types (`Move`, `ContestView`, `FaultState`, `Adjudicator`, `Panel`, side identity). No package deps (breaks the resolver↔policy cycle).
- **engine.py** — shared stochastic core (σ-leverage + base d10).
- **primitives.py** — the general substrate: Stasis, Appeal, Standing/Reserve, Pool, SelfGating, Leverage (N-collapsed: faculty + on-ground only), Room, Resonance, Readiness, and the venue-configured `DefeatCatalogue`.
- **resolver.py** — the wrapper (`Bout`) + the **`Venue`** top-down spec + the **win-conditions**.
- **modes.py** — institutions as venue presets.
- **policy.py** — decoupled policies via the contract.

## Win-conditions (the venue says what winning is)
- **ThresholdRace** — first past T and ahead; higher at close (debate / disputation).
- **TallyAtClose** — the body votes at the end, higher total wins (assembly). *Resolves the mismatched-appeal deadlock the old single-merits clock left as ~100% draws.*
- **ProofBar** — asymmetric: the challenger must drive net persuasion past a bar; else the defender prevails on doubt (tribunal — burden of proof).
- **GraceThreshold** — asymmetric one-sided: the petitioner must reach a grace bar; else denied (appeal).

## Defeat-conditions are venue-configured
`DefeatCatalogue` sets which faults are fatal and at what count. A **disputation** clinches on the full *nigrahāsthana* (barred-device, self-contradiction, evasion, silence); an **assembly** disables the rhetorical-device bar; an **appeal** keeps silence/contradiction but drops the evasion clinch; a **ceremony** would have none. The general fault *detection* lives in the wrapper; the venue decides which are *fatal*.

## Adjudicator(s)
A single `Adjudicator` or a `Panel` (jury/bench/council) that aggregates its members' character, discipline, and learned/hostile — the wrapper treats one-or-many uniformly.

## Institutions as venues (modes.py)
`court` (tribunal: logos, ProofBar, full faults) · `disputation` (debate: logos, ThresholdRace, full faults) · `assembly` (deliberative: pathos, TallyAtClose, no device-bar) · `appeal` (petition: ethos, GraceThreshold, deference faults). Dyadic counsel, negotiation, ceremonial remain scaffolds (genuinely different sub-systems).

## What holds (tested)
Symmetry; context/adjudicator/tension modulation; defeat-conditions fire (and **vary by venue**); tally **resolves** the mismatch; proof-bar **favours the defender** on equal play (burden of proof); panels **aggregate**. Build-then-close pays in **mixed** venues; the **matched pure appeal** wins **extreme** venues — the historically faithful result.

## Remaining
- The proof **set** is still ethos/pathos/logos (correct for the setting; a fully general engine would parameterize it).
- Minor: exact-tie draws under TallyAtClose (discrete increments) — a legitimate tied-vote outcome, reducible with a tiebreak.
- Balance/feel: trim build-then-close's edge in mixed venues; soften strong-gap decisiveness; scale the clock with faculty (floor/ceiling draws).
- The new architecture warrants a fresh **audit + stress + historical-validation** cycle before ratification.

## Evidence, pressure, jitter (latest pass)
- **Evidence** — a dossier of items with **hidden weights** (the player sees a count, not the value); presenting a **relevant** item adds **hard proof** (readiness-independent), with **corroboration** (diminishing returns); irrelevant evidence has nothing to present. More relevant evidence is better.
- **Pressure on the adjudicator** — `Pressure(toward, institutional, public)`: institutional pressure tilts the verdict; public pressure raises the adjudicator's susceptibility (leak) and unlocks the character beneath the role.
- **Persuasion-jitter** (±8%) removes high-faculty exact-tie draws; contests resolve (a hung outcome can be a venue option later).
