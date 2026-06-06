# Contest Engine — De-saturation & Venue-Balancing Pass (2026-06-05)

Applies the ratified balancing spec to the ground-up contest engine
(`designs/audit/2026-06-03-contest-groundup/`). Verdict: **all ratified +
verified changes land green (151/151 unit tests); the chronicle targets pass
except a drama-floor shortfall on the asymmetric venues, which is intrinsic to
their threshold structure, not a tuning error.** Three items are explicitly
**held for Jordan** (below); they are not part of this commit's ratification.

## Changes applied

| # | File | Change | Basis |
|---|------|--------|-------|
| 1 | engine.py | `OVERWHELM_SIGMA = 0.85`; `degree(net, ob, pool=None)` — pool-aware Overwhelming bar `μ·pool + σ·√pool` | de-saturation, diagnostic Lesson 2 |
| 2 | resolver.py | `RES_FLOOR = 0.15`; `_reception` passes `pool` to `degree`; resonance floored | de-saturation Lesson 6 |
| 3 | modes.py | court ProofBar 4.0→2.0; inquisition 3.0→2.5; excommunication 5.0→3.0; appeal Grace 7.0→5.0; memorial 6.0→5.5; imperial **Grace** 8.0→5.5 | ratified bar swaps |
| 4 | modes.py | secret_council `ThresholdRace(3.0)` → `VoteAtClose(jurors=5, sharpness=0.6, noise=0.8)` (ballotta) | un-fuse verdict from momentum |
| 5 | policy.py | new `counterpuncher` policy (+registered) | reactive rebuttal archetype |
| 6 | tests.py | two re-baselines, secret_council assertion → VoteAtClose, 5 stale cc labels corrected, +5 new regression checks | de-saturation lowered saturation-bound thresholds |

The pool-less `degree(net, ob)` legacy path is unchanged, so all direct-call
unit tests keep their meaning; only live reception (`_reception`) takes the
σ-gated degree-3.

### counterpuncher — design note
First written as "rebut when behind, advance only when ahead," it was a
dominated policy (lost 26–374 to logos) because it could never lead and so
never built. Redesigned to the classical *partes orationis* ordering —
**confirmatio before refutatio** (build the case in the first half, counter the
opponent's lead only in the back half). This is both viable (0.60–0.74 in
rebuttal/logos venues) and historically grounded (Quintilian). Bottom-up: the
live `rebut` move (`Reserve.COST["rebut"]=3`, capped at `REBUT_CAP=3.0`, gated
by `venue.allow_rebuttal`). Class-B, Jordan-vetoable.

## Validation — chronicle re-measurement (N=80/ordered pair, 6-policy round-robin, 5v5)

Targets: no single shape >50%; drama (REVERSAL+NAIL_BITER) 20–35%; asymmetric
venues viable (0.05–0.85) with ≥2 approaches; COLLAPSE reachable with
fault-prone policies; venues distinct.

| venue | top shape | top% | drama% | COLLAPSE% (faulty) | viable approaches |
|-------|-----------|------|--------|--------------------|-------------------|
| court | CLEAR_WIN | 0.33 | 0.15 | 0.99 | 4 |
| disputation | CLEAR_WIN | 0.38 | 0.27 | 0.95 | 6 |
| assembly | CLEAR_WIN | 0.30 | 0.22 | 1.00 | 5 |
| appeal | CLEAR_WIN | 0.35 | 0.22 | 1.00 | 3 |
| public_oration | CLEAR_WIN | 0.33 | 0.23 | 1.00 | 5 |
| inquisition_hearing | ROUT | 0.44 | 0.14 | 0.99 | 4 |
| excommunication_court | SPLIT_DECISION | 0.32 | 0.17 | 1.00 | 6 |
| imperial_petition | ROUT | 0.39 | 0.13 | 0.67 | 2 (+courtier dominates) |
| secret_council | ROUT | 0.38 | 0.19 | 1.00 | 6 |
| memorial_remonstrance | ROUT | 0.35 | 0.12 | 1.00 | 2 (+courtier dominates) |

- **PASS — no shape >50%** (max inquisition 0.44). secret_council ROUT 62%→38%
  (ballotta diversified it); excommunication SPLIT 49%→32%.
- **PASS — COLLAPSE reachable** (0.67–1.0 with overreacher/staller/off-ground).
- **PASS — distinctiveness**; **counterpuncher viable** and the strongest
  drama generator (REVERSAL 0.46 + NAIL 0.15 in rebuttal venues).
- **PASS — excommunication bar 3.0** ([was unverified]): ethos-accuser
  conviction 0.02 (bar 5.0) → 0.37 (bar 3.0); pathos/logos accusers stay ~0
  (ethos-keyed venue — correct character).
- **PASS — reserve-floor cliff with rebuttal live**: counterpuncher in a
  rebuttal venue takes zero faults / zero reserve-exhaustion.

## Findings (failure surface) — for Jordan, not changed here

1. **Drama floor missed by the five asymmetric bar/grace venues** (court 0.15,
   inquisition 0.14, excommunication 0.17, imperial 0.13, memorial 0.12). All
   *symmetric momentum-race* venues pass (0.22–0.27). REVERSAL/NAIL-BITER are
   momentum phenomena; a burden-of-proof bar produces threshold dynamics, not
   lead-changes. The low drama is largely intrinsic to the venue type.
   *Recommendation:* exempt asymmetric venues from the 20–35% drama target, or
   decide they warrant a dedicated drama lever. Not a tuning bug.

2. **imperial & memorial are courtier-dominated** (courtier 0.92 / 0.99; only
   two other viable approaches; logos-family at 0%). These are the
   ethos-GraceThreshold venues; ethos-dominance is thematically right, but
   0.92–0.99 is a degenerate single-dominant strategy. The handoff's own
   evidence (courtier ~98% even at discipline 0.20) shows the **discipline
   lever does not fix this** — the venue's ethos-weighting does.

3. **counterpuncher cannot see `venue.allow_rebuttal`** (not a `ContestView`
   field), so it self-destructs in no-rebuttal venues (evasion 0.57 / COLLAPSE
   0.48 in public_oration). It is effectively a rebuttal-venue specialist. A
   fix is a `ContestView` contract extension = Jordan's call.

4. **7v1 succession is ~73% split** (de-saturation roughly doubled the split
   share for an "overwhelming" faction gap). Faction-layer legibility question
   (succession band-mapping §7.2.1), separate from the contest de-saturation
   that caused it; the test was re-baselined per directive.

5. **narrative.py doc nit:** the SPLIT_DECISION comment says "only reachable
   under VoteAtClose," but ProofBar/GraceThreshold also decouple verdict from
   momentum and legitimately produce splits (pre-existing). Update the comment.

## HELD — requires Jordan's decision

- **Imperial sovereign `discipline` 0.05→0.25.** The handoff lists this in BOTH
  the ratified-apply set AND the Jordan-owned/out-of-scope set, and the
  evidence trail cites a third value ("disc 0.20"). Left at **0.05**
  (unchanged). Imperial GraceThreshold 8.0→5.5 was applied (separately
  approved). Note: imperial_petition above is measured at the held 0.05.

## Remaining work (follow-ups, not in this commit)

- Resolve the imperial-discipline value; possibly re-measure imperial at it.
- Decide findings 1–2 (drama exemption; ethos-venue monoculture).
- P8 documentation hygiene in the venue docs: split the "Bar" column by measure
  (net / absolute / relative); Beck 2018 → chapter DOI; fix the excommunication
  three-citation attribution (wrongly routed through Eichbauer); de-narrativize
  the [SEED] bar numbers.
- Faction succession §7.2.1 amplification (finding 4), if desired.

## NERS read (synthesized from the chronicle)

- **N (no dead apparatus):** counterpuncher resurrected from dead → viable;
  excommunication's ethos case resurrected (0.02→0.37). Residual dead apparatus:
  logos-family at 0% in the ethos-grace venues (finding 2) — directionally
  correct, but total death is worth Jordan's eye.
- **Viability / ≥2 approaches:** met in 8/10 venues with margin; imperial &
  memorial sit at the floor (2 + a dominator).
- **Legibility:** de-saturation removed the pool-size Overwhelming explosion
  (pool-8 degree-3 0.44→0.15); RES_FLOOR removes zero-resonance dead advances.
- **Drama:** met for momentum venues; finding 1 for bar venues.
