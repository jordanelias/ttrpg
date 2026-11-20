# WR · Weather with memory and neighbours, a journey priced before it is chosen, and the Rupture as an ending

Folded: 2026-11-12 by `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md`. Nothing here is deleted. Edit 2's spell (one drawn obstacle term shared under a parent rung for the year) is what makes a famine an **era condition** and its passing an era ending: when the spell is drawn at the realm rung in its worst band the condition `dearth` opens, and it closes on a later year's draw above it (`30_WR_A_the_era_is_a_named_period.md` commit 4's row; it reads the spell's Event, so the row lands with this file and is `n/a` before). The shared spell is also the compounding of LOOP row L12 (neighbours are short together), with this file's control `()` as its switch and the next year's draw, relief and fewer eaters as its brakes (`30_WR_D` §2). Edit 4's ending is a campaign ending and stays apart from an era ending (`30_WR_A`: "a campaign ending is not an era ending").

Reconciled: 2026-11-12, U5d closure — folded **A-54** (the one four-band ladder; against this file's multiplier form). Edits 1–2 are rewritten in what the draw is: the season's and the spell's draws are keyed draws on `degree_from_net`, pool the place's endurance (with its steward's skill, A-54's own words) and obstacle the season's hardship; the spell enters as an obstacle term shared by every territory under the parent rung for the year, not as a multiplier. "Mean one" becomes a calibration target for the band magnitudes (a declared sweep), not a property of a table. The keys (year, parent rung), the control (`()`), edit 3 (the leg's price) and edit 4 (the `site_band` ending reached by a draw) stand.

Reconciled: 2026-11-12, wave 3 (W3-3) — the body follows the U5d head (R3 §2, 7b-11, U1 ledger F-21): "The resolution"'s R-27 and "Mean one" bullets, edit 1's code and edit 2 are rewritten from a multiplier to a keyed draw on `degree_from_net` with the spell as a shared obstacle term and "mean one" as a calibration reading over band factors; the steward's part is named levels at site `settlement_effect` (D-U1-09, which overrides 7b-11's "the steward's `rate`"); the year is read from its one owner, `rosters.yaml: seasons_of_year` (`20_NARRATIVE_E` edit 1; D-U1-10, C3-K11), not `len(season_factor_draw)`; every pool and obstacle is a `[CALIBRATE]` row (R3 §2 last row; joint calibration, OWED §B); gate items (4) and edit 2's falsifier are re-read on the new form; tier and batch split (R3 7b-0; U3 B12 for the year and the spell, B38 for the era reading, cut edge §4.1 row 45). The problem section's evidence is kept as what `main` holds.

## Status: PROPOSED

Lands in batch: B12 (world motion and ground), after `16_PESSIMIST_WR_A_the_road_is_drawn` (U3 §1 item 13), for edits 1–4; the era reading of the spell (`30_WR_A` commit 4's `dearth` row) lands in B38.
Depends on: `20_NARRATIVE_E_the_year_and_the_reason.md` edit 1 (head of B12, `seasons_of_year`); `09_WR_B_draws_not_thresholds.md` (B12, the one shape); `07_SE_capability_rate_B.md` / the capability architecture's `settlement_effect` site (B04/B12) for the steward's levels; CP-T10-01 (plan position, `route` and `route_pricing`, edit 3; MISSING until STAGES.md step 5 carries it).

Carries findings F-WR-19 and F-WR-20 of `audits/09_WR_audit_addendum_B.md` (§5.3, §5.4), its resolutions
R-23, R-26 and R-27, and step 4 of its §3.8. Sits beside the first lane's `09_WR_world_motion.md` (the
wound at Askeheim, occupation of unheld land, the settled-territory victory selector) and supersedes none of
it. CP-T10-03's per-season terms (`season_terms`: yield, want, illness by season of the year) stay the
plan's (B10-18) and are not restated here.

## What it changes in `engine/season/` at runtime

- **Edit 1, edit 2:** nothing at the shipped fixtures. Both are new or changed *arm* values; the control
  (`season_factor_draw = ()`, `season_spell_draw = ()`) is today's tree, byte-identical. When B10-18 flips
  the weather arm, the flip's hash movement is the plan's declared mover, and these edits change what it
  moves to.
- **Edit 3:** nothing until `route_pricing` flips (CP-T10-01 ships it off).
- **Edit 4:** nothing: a loader grammar and a Query branch, with no roster row using them.

## The problem

**The scheduled weather cannot make the incident the design names** (a drought, then a famine; strife
opening A, natural shock). `queries/world_q.py:1178-1205`, `season_factor_of`: the factor is
`season_factor × choice(season_factor_draw[season_of_year])`, drawn from `draw_factory(world_seed, tick)`
keyed on the territory. Read off the code (F-WR-19):

- *no memory:* `tick` is in the key, so successive seasons are independent; with the swept arm
  `((0.5, 1.0, 2.0),) * 4` (`data/fixtures.py:535`'s comment) two low seasons in a row come one time in
  nine;
- *no neighbours:* the territory is in the key, so adjacent territories draw independently and relief from
  next door is almost always there;
- *a mean above one:* (0.5 + 1.0 + 2.0) / 3 = 1.167, and yield is linear in the factor
  (`modules/settlements/produce.py:19`), so the arm raises the long-run harvest by a sixth over its control
  in a realm whose stores already grow (#457 §8, not re-measured here).

The year itself is half-built, which the addendum's §5.1 understated: `season_of_year(w)` (`:1169-1175`)
reads the season of the year as `tick % len(season_factor_draw)`, so a declared table *is* the calendar.
What is absent is everything a season of the year should change besides yield (EB-06: `season_terms`,
`year_length` in no file).

**A journey's price is invisible to the person choosing it.** CP-T10-01 ships `route_pricing` off with
"[GAP: unowned]: no position gives a chooser a person-side reading of a leg's price". Today every leg costs
one scene point; `move` executes 21 of 78 at seed 0 over three seasons with 77 `travel.blocked` (§5.2).

**The world's survival has no end.** `rosters.yaml: endings`' grammar is `{post: …}` or `{rung_kind: …}`
(`data/rosters.py:1444`, `ENDING_SELECTORS = ("post", "rung_kind")`; `world_q.py:2675-2683`), selectors over
holds, so the design's survival terminal (the Rupture: "all factions lose", `wc_survival_spine.md`;
`threadwork_v30.md` §5.3, intent only) cannot be written (F-WR-20).

## The resolution, decided

- **R-27 · a spell, as an obstacle term (A-54).** The season's harvest is one keyed draw on the shared
  ladder (`dice_engine.degree_from_net`): **pool** the place's endurance, with its steward's skill as named
  levels (`edge` row, site `settlement_effect`, `side: steward`; D-U1-09); **obstacle** the season's
  hardship plus a **spell term** drawn on a coarser clock and a coarser place: the **year** (read from
  `rosters.yaml: seasons_of_year`, `20_NARRATIVE_E` edit 1: `year = tick // len(SEASONS_OF_YEAR)`) and the
  territory's **parent rung** (`state/containment.py::parent_of`, the one owner `state/gate.py` already
  imports). The spell term is drawn once per (seed, year, region) and shared by every territory under that
  region for the whole year; the season's own draw stays per territory and per season. The four bands map
  to four yield factors. Duration and neighbourhood come from the key, and no state is stored: the spell a
  territory is in is a function of `(world_seed, year, rung)`, as the season of the year already is.
- **Mean one is a calibration reading, not a table property.** The four band factors are swept (a
  declared sweep in `rosters.yaml`), and the reading recorded at three seeds is the realm's long-run
  harvest under the live arm against the control: a forcing should move variance and not the long-run
  harvest. A bias, if wanted, is `season_factor` (the constant), declared as such.
- **R-23 · the leg's price is not world state.** It is a pure function of two settlement ids and the
  loaded geography (`data/geography.py`'s adjacency and terrain matrices: identical for every person,
  changed by no act). `decision/budget.py::budget(p, v, k, fx)` (`:18`) already takes `fx` on exactly that
  ground (`:53`: "not world state"). The price is handed to `decision/` beside `fx`; whether the road is
  open stays a World read at the fold, and a priced journey refused there is `travel.blocked`, which is how
  a person learns the road is shut. No person-side World read is introduced.
- **R-26 · an ending over the condition of Sites.** The grammar gains `{site_band: <band>, of: <site kind
  or all>}`. **It is reached by a draw, not by a count crossing** (the brief's standing rule, "we do not do
  deterministic"): the row is *eligible* in a season when at least one selected Site reads at or below the
  band (an eligibility check, which the rule permits), and then a keyed draw on the shared ladder decides
  whether the fabric gives way this season, with odds set by state (below). A row using it carries
  `victory: false` and no `under:`. #457's END-VICTORY handle rules
  the form ("a Query over holds and seats that the season reports, never an actor"); the cut that removed
  the stored stability scalar (#457 §5) changes what the Query reads, not whether the ending exists. The
  roster's act-credit clause is not applied: a ruin nobody caused is what the row reports. **The row itself
  (which band, which kinds) is Jordan's content and ships absent.**

## The edits

### Edit 1 · the season's draw and the spell term (`engine/season/data/fixtures.py`, `rosters.yaml`, `queries/world_q.py::season_factor_of`)

`fixtures.py`, beside `season_factor_draw`:

```python
    season_spell_draw=(),        # R-27: the year's regional obstacle terms, equally likely;
                                 # swept () (control) / (-1, 0, +1)  [ASSUMPTION; medium; Jordan to correct]
```

`season_factor_draw` keeps its `()` control; when non-empty it is refused at load unless its length equals
`len(SEASONS_OF_YEAR)` (D-U1-10). `rosters.yaml` gains `season_band_factors: {Overwhelming: …, Success: …,
Partial: …, Failure: …}` (the four yield factors, a declared sweep) `[CALIBRATE; joint calibration, OWED §B]`.
`season_factor_of`, when the arm is on, composes (structure):

```python
    year = w.tick // len(SEASONS_OF_YEAR)                      # D-U1-10: the year's one owner
    region = (parent_of(w, territory) if territory else None) or "world"   # `state/containment.py`
    spell = (draw_factory(w.world_seed, lambda: year)(region, "season_spell").choice(spells)
             if spells else 0)                                 # shared by every territory under `region`
    pool = endurance_of(territory) + steward_levels            # place's endurance; D-U1-09 `settlement_effect` edge
    obstacle = hardship_of(season_of_year(w)) + spell          # the season's hardship plus the shared spell term
    band = degree_from_net(roll(pool, obstacle, draw))         # the one ladder; `draw` keyed as today
    return base * SEASON_BAND_FACTORS[band]
```

`endurance_of`, `hardship_of` and the steward's levels are `[CALIBRATE]` rows (CP-T10-03's `season_terms`
for hardship by season; the capability architecture's `settlement_effect` site for the steward), read by
this one function. A spell table with no season table refuses at load (a spell needs a year to last). The
docstring's "two territories at one tick draw independently" becomes "their season draws are independent;
their spell term is shared when they share a parent rung".

### Edit 2 · the band factors are a sweep with a mean-one reading (B10-18's arm)

Not a table edit. The live arm's four `season_band_factors` are swept, and the reading recorded at three
seeds over eight seasons is the realm's mean harvest factor under the arm against the control's; the
calibration target is a mean of one (a forcing moves variance, not the long-run harvest). The former
change of `((0.5, 1.0, 2.0),) * 4` to `((0.5, 1.0, 1.5),) * 4` is withdrawn with the multiplier form.
`[ASSUMPTION; medium; Jordan to correct]` for the factors.

### Edit 3 · the leg's price reaches the chooser (`decision/budget.py`, `loop/driver.py`)

`route(a, b)`'s cost (CP-T10-01, over the loaded geography) is exposed as `leg_price(a, b, geo) -> int`, a
pure function in `data/geography.py`. The driver hands `geo` to `choose` beside `fx`, as it hands `k`.
`decision/` prices a `move`/`travel` candidate with it when `route_pricing` is on and charges one point
when it is off (today). No `World` crosses: `test_w5_sense_is_still_the_only_world_taking_non_decision_function`
stays green. The flip of `route_pricing` then waits only on its own paired arm.

The price is bookkeeping (what a choice costs from the scene budget), which the standing rule permits. What
the journey *does* to the traveller is not: CP-T10-02's exposure at the leg's end is listed for its owner
(B10-18) as a draw, with odds from the `radiation_bands` distance and the leg's terrain and a graded result
on the body, never a fixed charge per band.

### Edit 4 · the `site_band` selector (`data/rosters.py`, `queries/world_q.py::_ending_edges`)

`ENDING_SELECTORS = ("post", "rung_kind", "site_band")`. The loader admits `site_band` with a required
`of:` (a `site_kinds` member with non-empty `band_floors`, or `all`, meaning every kind that has floors) and
refuses `under:` beside it, refuses `victory: true` with it, and refuses a band name not in the kind's
floors. `_ending_edges` gains the third branch: the Sites under the realm of the selected kinds, each
compared with the floor of the named band. **Eligible** when at least one is at or below it. Then the
draw: `draw_factory(w.world_seed, lambda: w.tick)("realm", f"ending:{row.name}")`, resolved through
`dice_engine.degree_from_net` (the one ladder owner), with **pool** the number of selected Sites still above
the band (what holds the world together) scaled by a parameter row, never below the dice engine's own
floor (a world with every Site fallen still rolls, so its loss is likely and not certain), and **obstacle** the number at or below
it plus one for each band below the named one. Failure: the ending is reached this season, and the edges
returned are the fallen Sites; Partial: not reached, and the season's report carries the row as `near`
(a reading, writing nothing); Success or Overwhelming: nothing. Recoverable: a restored Site moves from the
obstacle to the pool, so restoration lowers the odds the next season `[CALIBRATE: pool scale and
per-Site obstacle, joint calibration, OWED §B]`. The draw is keyed by
`(seed, tick, row)`, so `endings_reached` returns the same answer at every call in a season (`T-a`: a read,
recomputed, storing nothing) and advances no draw ordinal (`season_factor_of`'s precedent: a keyed draw
inside a Query). `endings_reached`'s antecedents are the `condition.band_crossed` Events that took each
fallen Site there. The roster's prose head gains one sentence naming the selector and the draw. **No
member row is added**; the pool scale is one fixture row, `[ASSUMPTION; medium; Jordan to correct]`.

## The gate that shows it worked

```sh
PYTHONHASHSEED=0 python -m engine.season.harness.aperture 1 0          # control: hashes unchanged (one short run)
python -m pytest engine/season/tests/test_season_weather.py engine/season/tests/test_season_weather_per_territory.py \
       engine/season/tests/test_in27_endings.py -q                     # covering files, at the close
```

Passes when: (1) every control reproduces `build_realm(0)` and the one- and two-season pins; (2) under
`season_spell_draw = (0.6, 1.0, 1.4)`, two territories under one parent rung read the same spell in every
season of a year and may differ the next year, and two under different parents may differ in the same
season; (3) the spell is a function of `(seed, year, region)` only (same inputs, same spell, from two
processes); (4) re-read on the drawn form: under the live arm with spells, at three seeds over eight
seasons, at least one territory reads `shortfall` in two consecutive seasons (a hard spell raising the
obstacle for a year), using CR-73's reading, and the same territory does not do so at every seed (the draw
did not collapse into a threshold) (`[UNVERIFIED]` until run; the falsifier below says what failing looks
like); (5) a planted `site_band` row over a planted world reads
never reached when no harbour is below the band (ineligible); over 200 seeds with every harbour below it,
reached at most seeds and **not** at all of them; with one harbour in three below, reached at fewer seeds
than that and at more than zero; (6) two calls in one season return the same answer and leave the draw
ordinal unchanged; (7) the loader refuses `site_band` beside `under:` and beside `victory: true`.

## The falsifier

For edit 1: the spell differs between two territories of one region in one season (the key leaked the
territory), or is the same for every year (the year is not in the key), or the year is read from
`season_factor_draw`'s length rather than `SEASONS_OF_YEAR`. For edit 2, re-read on the drawn form: the
recorded mean harvest factor under the chosen band factors departs from one by more than the control's own
seed-to-seed spread, and the factors are nevertheless shipped (the calibration reading was ignored). For
edit 3: any `World` reaching `decision/`. For edit 4: a `site_band` row reached while no selected Site is
at or below its band (eligibility leaked); or a state at which the row is reached at every seed or at none
across 200 seeds while eligible (the draw has collapsed into a threshold).

## NERS reading

- **N.** Without a spell the scheduled weather is a one-season event by construction (apparatus C9;
  Sylvester's "the richness comes when several events interact"), and the strife study's natural-shock
  opening cannot occur. Without the ending, the survival contest the design calls the game's strategic
  architecture has no loss. Holds top-down (a region's bad year), bottom-up (a governor relieving his own
  settlement), laterally (SE's larder, FA's `transfer` and `requisition`, SC's `petition` at the shortfall
  rung) and diagonally (a regional famine reaching a seat's vacancy through deaths under the illness arm).
- **R.** Drama with nobody watching: a dry year in one duchy makes "whose grain" into "there is no grain
  nearby". A priced journey makes going yourself or sending someone a strategic choice.
- **S.** One draw primitive, one more key; the year already read off the table's length; the leg's price
  on `fx`'s precedent; the ending on the roster's own grammar. Calculations consistent: the spell and the
  season's hardship are both obstacle terms of one draw on the one ladder, and the year has one owner.
- **E, last.** Two fixture values, one keyed draw, one pure function and one selector, against the
  incident the design names first and the end it names last. High.

## Cost class

Edit 1: small build (one draw composed on the ladder, one roster table). Edit 2: a calibration reading.
Edit 3: small build. Edit 4: small build, no row. Tier: `sonnet` (R3 7b-0).
