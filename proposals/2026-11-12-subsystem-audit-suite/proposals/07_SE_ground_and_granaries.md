# 07 · SE — places differ, and the larder ladder is the relief path: endowment by territory, stocked granaries, the remainder walk

Reconciled: 2026-11-12, U5d closure — folded **A-50** (some starting state is drawn, small and bounded), **A-54** and the addendum's decisions. §4 (c)'s world-gen stocking ("one season of yield per settlement and a granary") becomes the centre of a bounded draw: each settlement's starting stock is drawn around that value within the bounds `21_PROCEDURAL_D_world_cards_and_churn.md` authors, so some larders start low; with the bound at zero width the edit is the text as written (the control). The granary's rung is `07_SE_treasury_granary_B.md`'s (the nearest seat-bearing rung), not every territory rung (P-7). The yield the endowment feeds is drawn on the four-band ladder (A-54; `09_WR_B_draws_not_thresholds.md`), so the endowment is the pool's ground, not a fixed output. The gate gains the migration arm of `U5d_SE_owed_edits.md` §10.

Reconciled: 2026-11-12, wave 3 (W3-3) — the body follows the head on the granary's rung (U1 ledger F-15; R3 §3): §1 item 2, R2 and edit (c) now stock the nearest seat-bearing rung above a settlement (`world_q.treasury_above`, `07_SE_treasury_granary_B.md`), not every territory rung; R3 §2 (A-44, A-75): §6's `ED-WR-0011` line reworded; U3 §6.2 (the reading on the scratch `se_ground.py` is restated as a named test in `test_endowment.py`, written first, U3 §6.1); tier and batch (R3 7b-0; U3 B12, with the cut LATER edge to `21_PROCEDURAL_D`).

## Status: PROPOSED

Lands in batch: B12 (world motion and ground), with `07_SE_treasury_granary_B.md`, after `07_SE_kernel_repairs.md` (U3 §1 item 13).
Depends on: `07_SE_treasury_granary_B.md` (B12, `world_q.treasury_above`); `09_WR_B_draws_not_thresholds.md` edits 1–2 (B12, the drawn yield and body); `21_PROCEDURAL_D_world_cards_and_churn.md` (B39) for the bounded starting draw only (cut edge §4.1 row 42, LATER: the stocking runs at its zero-width control without it).

Carries findings F-SE-01, F-SE-03, F-SE-04 and resolutions R-SE-01, -02, -03, -11 of
`audits/07_SE_audit.md`. It amends three open positions rather than adding one: CP-T08-02 (endowment by
ground), CR-22 (hunger binds) and the open ruling row H-303. Nothing here is ratified by being written.

## 1. What changes in `engine/season/` at runtime

With the arm off (`endowment_mode: uniform`, shipped), nothing: every hash is the base hash.
With the arm on (`ground`):

1. `harness/populated.py::build_realm` mints producing Sites per settlement from an authored table keyed
   by territory instead of one of every producing kind everywhere.
2. `build_realm` seeds stores: every producing settlement starts with one season of its own yield, and
   each granary rung (the nearest rung above a settlement at which a seat sits, `world_q.treasury_above`,
   `07_SE_treasury_granary_B.md`) starts with `granary_seasons` seasons of the eaten-kind deficit of the
   settlements it is the granary of.
3. `modules/settlements/larder.py::larder_draw` walks on up the ladder for the remainder when the first
   stocked rung cannot cover the want (H-303's resolution; its own fixture arm, shipped at today's rule).

The effect, measured on a hand-made copy of (1) and (2) before any code was written (§5): the 11
highland settlements eat from their territory rung while it holds stock and starve when it empties,
while the 26 lowland settlements stay fed. No weather draw, no multiplier, no new verb.

## 2. The problem, with evidence

- **Every settlement is the same economic object.** `harness/populated.py:1215-1220` mints one Site per
  producing kind of `SITE_YIELD` at every settlement; `cohorts.yaml` seats one weight-2 cohort at each.
  Reading (`se_bind.py 0 8 10 0`, seed 0, eight seasons, no acts, per-head need ×10, weather off): all 37
  cohorts hold one body value in every season (`distinct_bodies=1`) and all 37 settlements sit in one
  hunger band. At ×20 all 37 cohorts die in season 0.
- **So scarcity, when CR-22 turns it on, has no geography.** With the per-territory weather draw on
  (`season_factor_draw ((0.5, 1.0, 2.0),)*4`) the same arm differentiates (seed 0: 8 cohort deaths by
  season 2; seed 1: 19 by season 7), but which town starves is the draw's, not the place's.
- **The planned gate on the fix is circular.** AM-E-13 holds the `ground` flip until *"a measured relief
  path in computed play (`transfer` or `exchange` moving stock to a short town)"*. In a uniform realm no
  town is short while another is long, so that path has nothing to move: computed play moved 2 units of
  13,690 in three seasons at seed 0 and 4 at seed 1 (`se_probe.py`, play arm): cohorts' 1-grain
  `transfer`s from their own settlement into their own person-rung, and one `requisition` of 1 at seed 1.
- **The planned derivation cannot classify the map.** CP-T08-02's build text reads the ground class
  *"from the authored geography by one function `ground_class(geo, settlement)`"* and its falsifier is
  *"a settlement whose coords fall inside a mountain polygon gets a seam"*. Point-in-polygon over
  `valoria_geography_v30.yaml` (run at this commit): **8 of 37 settlements fall inside no terrain
  polygon** (S-007, S-008, S-028, S-030, S-031, S-032, S-033, S-035, among them the Varfell seat and the
  primary pass fortress); **none falls in the mountain polygon**; T5 (canon: *"Crown breadbasket"*) and T1
  (the capital) are both `plains`, and T17 (canon: *"Northern mines"*) and T8 (the Hafenmark capital)
  are both `highland`. The file's own header says 21 settlements' coordinates are *"inferred, not
  hand-tuned"*.
- **Season 0 is a world-gen artefact.** Every larder is empty at build and the draw precedes the yield,
  so the first MATTER shorts all 37 cohorts by the whole want. It is the realm's only hunger event and
  `test_hunger.py::test_i_on_the_built_realm_every_populated_settlement_starves_before_the_first_yield`
  pins it.
- **A partly stocked rung blocks the walk** (H-303): with 1 grain at the first stocked rung and 1,000
  above, a want of 6 takes 1.

## 3. The resolution, decided

**R1. The endowment is authored per territory, in the roster the plan already names.** Keep CP-T08-02's
owner (`rosters.yaml: site_endowment`) and fixture (`endowment_mode`), and change its key from a derived
ground class to the geography territory code, with an optional settlement override. Ladder step 5: a
derivation that leaves 8 of 37 places unclassified and cannot tell the breadbasket from the capital is
not a second copy avoided, it is a fact missing; the canon file states each territory's economic
character in its `sub:` and `description:` strings, which are not typed, so the typed head is new and
`rosters.yaml` is where code reads it. `ground_class` is not built.

**R2. World-gen stocks the realm.** A settlement starts with one season of its own yield; its granary
rung (the nearest seat-bearing rung above it, `07_SE_treasury_granary_B.md`) starts with a granary. Ladder step 4: CR-22's own SEASON-0 FLOOR RULE offers this (*"or a prior
position stocks the larders as world-gen content"*); this takes that branch.

**R3. The relief path that gates the flip is the larder ladder, which already executes.** The draw
walks home first, then up (`larder.py:55-62`), so a granary rung holding grain feeds every settlement
beneath it at MATTER with no act. What fills it is `requisition` into its seat's rung (built), then
CP-T08-07's standing levy (planned). The flip's gate becomes: *in a seeded realm run under `ground`, at
least one settlement's draw names its granary rung as `source`, and the granary's runway is at
least `granary_seasons` seasons*. Acts that refill it (`requisition`, `transfer`) are a reading at the
flip, not its gate. AM-E-13's limit is replaced by this one.

**R4. The walk continues for the remainder.** `take` is summed over the rungs up the ladder until the
want is met or the ladder ends. Ladder step 5: under R3 a short town with a few units at home must
reach the granary above, or the granary feeds only towns that are wholly empty. See §6 for the standing
order this does not cross.

## 4. The exact edits, by owner

**(a) `engine/season/rosters.yaml` — `site_endowment` (new table; the one owner of which producing kinds
a place receives).**

```yaml
  site_endowment:
    source: "CP-T08-02 as amended (proposals/2026-11-12-subsystem-audit-suite/proposals/07_SE_ground_and_granaries.md)"
    row: H-07
    keys: [territories, site_kinds]
    uniform: [harbour, seam]            # the control: today's placement, every settlement
    ground:                             # [ASSUMPTION; medium; Jordan to correct; revert: endowment_mode uniform]
      T1:  [harbour]                    # capital, river-sea nexus
      T2:  [field]                      # heartland farmland
      T3:  [seam]                       # border fortress, mountain pass
      T4:  [seam]                       # highland timber
      T5:  [field, field]               # breadbasket
      T6:  [field]                      # southern farmland
      T7:  [seam]                       # timber valley
      T8:  [harbour]                    # west sea trade
      T9:  [seam]                       # mountain ridge
      T10: [seam]                       # border castle
      T11: [harbour]                    # central fjords
      T12: [harbour]                    # western fjords
      T13: [harbour]                    # southern fjords
      T14: [field]                      # central plains
      T16: [harbour]                    # island republic
      T17: [seam, seam]                 # northern mines
    settlement: {}                      # optional override, keyed by geography code (S-NNN)
```

The loader (`data/fixtures.py`, beside `_load_capacity_floor`) refuses a territory holding a settlement
with no row, a kind outside `site_kinds`, and an empty list. `field` joins `site_kinds`, `site_yield`
(`grain: 40`), `wear_per_season` (10), `band_floors` and `works_cost` exactly as CP-T08-02's build text
already states; under `ground`, `harbour` yields `salt: 30` and a reduced `grain` (fish) of 10
[ASSUMPTION; JQ-6's family]. Every magnitude here is a shape proposal and joins JQ-6's sweep.

**(b) `engine/season/data/fixtures.py` — two fixtures.** `endowment_mode="uniform"` (CP-T08-02's, swept
`uniform / ground`) and `granary_seasons=0` (swept `0 / 4 / 8`; 0 is the control, no territory stock).

**(c) `engine/season/harness/populated.py::build_realm` — the site loop and a stores seed.**

Old (`:1215-1220`):

```python
    for sid in geo["settlements"]:
        for k in sorted(SITE_YIELD):
            if SITE_YIELD[k]:
                s_id = f"s_{_slug(sid)}_{k}"
                w.sites[s_id] = Site(s_id, f"set_{_slug(sid)}", k,
                                     condition=w.fixtures.get("condition_scale"))
```

New (structure): `kinds = endowment_for(w.fixtures, sid, geo["settlements"][sid]["territory"])`, a pure
function in `data/fixtures.py` returning the `uniform` list or the `ground` row (settlement override
first); one Site per list entry, id `s_<slug>_<kind>` for the first of a kind and `s_<slug>_<kind>_<n>`
for the rest, so the `uniform` arm mints today's ids byte for byte. After the garrison loop, when
`endowment_mode == "ground"`: each settlement's `stores` is set to one season of its Sites' base yield,
and each granary rung's `stores` (`world_q.treasury_above(w, settlement)` for every settlement, grouped
by the rung it returns; `07_SE_treasury_granary_B.md` owns the rung and the re-keyed seed) to
`granary_seasons × Σ max(0, want_k − yield_k)` over the cohorts and Sites of the settlements it serves,
per eaten kind. The starting value is the centre of A-50's bounded draw (`21_PROCEDURAL_D`), at zero
width the value as written. Both are world-gen writes before any season (the precedent is
`harness/scarce.py`'s planted treasury).

**(d) `modules/settlements/larder.py::larder_draw` and `queries/inputs.py::LarderInput` — the remainder
walk.** `LarderInput` gains `walk: str` (`"first"`, shipped, today's rule; `"through"`). Under
`"through"`:

```python
            taken, src = 0, None
            for rung in ladders.get(e.home, ()):
                held = left.get((rung, kind), stock.get((rung, kind), 0))
                if held <= 0:
                    continue
                part = min(want - taken, held)
                left[(rung, kind)] = held - part
                taken += part
                src = src or rung
                if taken == want:
                    break
            cells.append((kind, want, taken, src))
```

A `DrawRow` cell then names the first source only; `subsist`'s debit must be per rung, so the cell gains
a fifth element `parts: ((rung, units), ...)` and `subsist.py`'s debit loop sums `parts` instead of
`(src, take)`. The fixture is `larder_walk` (`data/fixtures.py`, swept `first / through`), projected by
`world_q.larder_input`. The module docstring's rule text is rewritten in the same commit.

**(e) Tests.** `engine/season/tests/test_endowment.py` (CP-T08-02's, re-aimed; absent on `main`, written as
the batch's first commit, U3 §6.1): under `ground` every
settlement of T5 holds a `field` and none holds a `seam`; T17's hold a `seam` and no `field`; a geography
territory with a settlement and no row refuses at load. `test_hunger.py::test_i` is re-recorded under
`ground` to assert the opposite (no cohort short at season 0) and kept as written under `uniform`.
`test_demand_delivery.py` gains the H-303 pair: home 1, above 1,000, want 6 gives take 1 under `first`
and 6 under `through`, with the debit split 1 and 5.

**(f) Plan.** `workplans/valoria_master_workplan_v11_part14.md` AM-E-13: replace the limit's gate with
R3's. CR-22's rule gains one clause: its arms run under `ground` with `granary_seasons` at the shipped
value, and its exit records the band spread across settlements, not only "at least one below `fed`".

## 5. The gate that shows it worked, and the falsifier

- **Execution artifact.** Under `ground`, `granary_seasons 4`, seed 0, eight seasons, no acts: the
  hunger band differs between at least two settlements in every season after the first, with the weather
  draw off; at least one draw cell's `source` is a granary rung; no cohort is short at season 0.
- **The named test** (U3 §6.2: the scratch `se_ground.py` is not in the repository, so its reading is
  first written as a test): `test_endowment.py::test_ground_granaries_feed_the_highlands_then_run_down`
  (`ground`, `granary_seasons 4`, seed 0, eight seasons, no acts; expected: no highland cohort below full
  body while its granary holds grain, granary grain falling each season, highland body falling after the
  granary reaches 0, every lowland cohort at full body; control `granary_seasons 0`: the highland cohorts
  fall from season 0), each loop asserting it asserted.
- **The reading already taken on a hand-made copy** (`se_ground.py 0 8 4`, not a repo artifact: harbours
  deleted from the 11 highland settlements, their five territory rungs stocked with four seasons of
  deficit, lowland settlements stocked with one yield): seasons 0 to 2, all 11 highland cohorts at body
  1000 while their territory grain falls 48 → 36 → 24 → 12; season 3 the granaries reach 0; seasons 4 to
  7 the 11 lose 60 body a season (940, 880, 820, 760) while all 26 lowland cohorts stay at 1000. Control
  arm `granary_seasons 0`: the 11 fall from season 0. So the ladder is the relief path and the granary is
  the clock.
- **Falsifier.** If under `ground` every settlement still shares one band in every season, the endowment
  is not reaching `produce` (the planted failure: map every territory to `[harbour, seam]`; the test
  reds). If the `uniform` arm's `build_realm(0)` hash differs from the base, the id scheme moved.
- **What it will also show, and must be read rather than hidden:** the shortfall report is emitted only
  in the season a rung is drained with a mouth unfed (ruled a balance number, H-160 limit 3). In
  `se_ground.py` with the granary one unit short of a whole season, five territory rungs each emitted
  `shortfall:grain` and `shortfall:salt` once, at the draining season, and nothing after. Under `ground`
  that single report per territory is the governor's whole warning.

## 6. What this does not cross

- **ED-SE-0053's standing order** (*"do not re-propose hearth larders or any delivery move across a
  `contain` edge; matter moves only by `transfer`"*): no matter is delivered here. Stock enters a
  granary rung by an act (`requisition`, `transfer`) or by world-gen; the draw reading up the ladder is
  the rule ED-IN-0246 item 3a already built.
- **H-160 limit 3** (ruled a balance number): untouched.
- **The cast:** this arm mints no `Person` (a cohort's weight is a count). The cast is no longer closed
  (A-44: about 94 generated persons plus kin; A-75: named births behind `birth_rate`); named births are
  `23_STORY_B_a_house_continues.md`'s.
- **Canon**: `valoria_geography_v30.yaml` is read, not edited. If Jordan prefers the endowment as a typed
  field of the canon file, the table moves there unchanged; that is a canon amendment and is his.

## 7. NERS reading

- **N.** Cut it and the map's types and territories say nothing about what a place makes, nothing needs
  to move between places, and CP-T08-05 (price), CR-49 (`exchange`) and CP-T08-07 (tax) have nothing to
  steer. It holds bottom-up (the draw and `produce` are unchanged), top-down (the canon descriptions
  become true of the engine), laterally (a duchy's leverage over another's food is FA's missing input)
  and across scales (a field's provision, IN-52, reads the same treasuries).
- **R.** Strategic choice appears where there was none: whom a lord feeds, and from whose surplus. The
  no-player half holds: a granary runs down and a town starves with nobody acting. Completeness: a
  territory with no granary and no food Site starves from season 0, which the loader cannot prevent and
  the `granary_seasons` sweep must show.
- **S.** One ladder, one draw, one debit; the remainder walk keeps `demanded`/`delivered` on the same
  function. It pauses nothing. The methodology is the existing one (stores, yield, draw).
- **E, last, against N and R.** One table, two fixtures, one loop edit and a nine-line walk buy every
  item above. A player can read "the highlands eat from the lowlands" off the map.

## 8. Cost class

Small build (the table, the loader, the loop, the stores seed), plus one edit to a pure module function
with its record type. Hash: EQUAL at the shipped arms; the `ground` flip, the `granary_seasons` flip and
the `larder_walk` flip are each a declared mover in a commit of their own. Tier: `sonnet` (R3 7b-0).
