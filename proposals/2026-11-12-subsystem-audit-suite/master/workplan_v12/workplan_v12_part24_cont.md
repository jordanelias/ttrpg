# Workplan v12 — part 24, continued: B12b-weather-arcs-population from B12b.22; then B19a-mb-contact-instrument and B29-pc-custody

## Status: PROPOSED (continuation of `workplan_v12_part24.md`, same lane A24, same tree `aa31fd2`; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

The batch block of `B12b-weather-arcs-population` (its head lines and position table) is in `workplan_v12_part24.md`; the items below continue it in landing order, then its `## Readings`, its re-pin position and its boundary row. Words, paths and the line-number rule are that file's.

---

### B12b.22 — the weather bears on what is grown · `16_PESSIMIST_SE_B_harvest_walls_and_the_supply_gate` edit 1 · BUILD · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_SE_B_harvest_walls_and_the_supply_gate.md` R1, "Edits" 1, gate 1; rulings A-54; closes F-PES-SE-07 (with the source's "one commit per edit").
- ADVANCES: none of the nine; a bad harvest is not a bad year underground.
- INSTRUCTION: copied: "Roster row:
  ```yaml
  grown_kinds:
    source: "audits/16_PESSIMIST_SE.md F-PES-SE-07: the season factor is weather, and weather bears on what is grown."
    note: "The matter kinds a season's factor multiplies. A kind outside the set yields at factor 1."
    values: [grain]
  ```
  checked at load as a subset of `matter_kinds`. `ProduceInput` gains `grown: frozenset`. In `produce`:
  ```python
  f = factor[rung] if k in inp.grown else 1
  produced[k] = produced.get(k, 0) + int(base * (max(0, condition) / inp.scale) * f)
  ```
  `factor[rung]` is what `queries/world_q.py::season_factor_of` returns for the rung's territory: under A-54 the yield factor of the band of the season's keyed draw on the shared ladder … owned by `09_WR_B_weather_with_memory_and_the_year.md` edit 1. This file does not draw; it scopes the factor to grown kinds. At factor 1.0 the float expression is operand for operand today's, so no truncation moves." `[ASSUMPTION; medium; Jordan to correct: salt by evaporation and timber by felling are arguable members]` (R1). `world_q.produce_input` fills `grown` from `GROWN_KINDS`.
- WHERE: `engine/season/rosters.yaml` (`grown_kinds`); `engine/season/data/rosters.py` (`GROWN_KINDS`, the subset check); `engine/season/queries/inputs.py` (`ProduceInput.grown`); `engine/season/queries/world_q.py` (`produce_input`); `modules/settlements/produce.py` (`produce`).
- TESTS: in `engine/season/tests/test_season_weather_per_territory.py` (exists), written first: `test_ore_and_timber_ignore_the_weather` — "weather arm on, eight seasons at seed 0 [two seasons; eight in the source, A-114]: realm ore and timber yield equal the weather-off run season for season; grain differs"; red before.
- FALSIFIER and CONTROL: ore following the weather with the arm on. Control: "the weather-off run is hash-equal to base"; `()` arm → realm hash equal.
- GATE: `python -m pytest engine/season/tests/test_season_weather_per_territory.py -q` → pass; realm hash at seed 0, one season → equal to B12b.21's reading.
- HASH MOVERS: none at the shipped arm `()`.
- DEPENDS ON: V12 B12b.03 (`season_factor_of`'s band factor); EXISTS-IN-TREE `queries/inputs.py::ProduceInput`, `queries/world_q.py::produce_input`, `modules/settlements/produce.py::produce`.
- GLOSSARY: new row *grown kinds*: "the stores that come from fields and so follow the weather, as a harvest does"; owner `rosters.yaml: grown_kinds` (the source: "The vocabulary gains one word (`grown_kinds`), defined at its roster row").
- COST and TIER: small; `sonnet`, `high`.
- LANDS IT: B12b's producer; `Item: B12b.22`, `[skip ci]`.

### B12b.23 — a second wall adds · `16_PESSIMIST_SE_B` edit 3 · BUILD · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_SE_B_harvest_walls_and_the_supply_gate.md` R3, "Edits" 3, gate 3, "Falsifier"; closes F-PES-SE-08.
- ADVANCES: none of the nine; building a garrison is a choice with a return.
- INSTRUCTION: copied: "`modules/settlements/fortification.py`
  ```python
  def fortification(inp: FortInput) -> float:
      \"\"\"A settlement's defensive strength, `0.0` to `1.0`: the complement of the product of each
      garrison's shortfall, so a second wall never weakens the first.\"\"\"
      breach = 1.0
      for c in inp.conditions:
          breach *= 1.0 - max(0, min(c, inp.scale)) / inp.scale
      return 1.0 - breach
  ```
  No garrison gives `1.0 − 1.0 = 0.0`, as today."
- WHERE: `modules/settlements/fortification.py` (`fortification`); NEW `engine/season/tests/test_fortification_adds.py`.
- TESTS: in the new file, written first: "`test_second_wall_never_lowers_the_first`, `test_half_strength_pair_reads_075`, `test_no_garrison_reads_zero`" — gate 3's readings: "(1000,) → 1.0; (1000, 1000) → 1.0; (1000, 0) → 1.0; (500, 500) → 0.75; () → 0.0"; `(1000, 0)` reads 0.5 before the edit (red).
- FALSIFIER and CONTROL: "any consumer in `modules/mass_battle/` that relies on the mean's property that a ruined second garrison *lowers* the value … with one garrison per settlement the two formulas agree, and the MB lane should read this edit before any settlement gains a second." Control: "`build_realm(0)` barrier-only, three seasons [two; A-114]: hash equal to base".
- GATE: `python -m pytest engine/season/tests/test_fortification_adds.py -q` → pass; `git grep -n "fortification" -- modules/mass_battle` → each caller listed in the commit body with whether it reads a second garrison; realm hash at seed 0 after two seasons → equal.
- HASH MOVERS: none (one garrison per settlement in `build_realm`).
- DEPENDS ON: EXISTS-IN-TREE `modules/settlements/fortification.py::fortification`, `FortInput`.
- GLOSSARY: none.
- COST and TIER: small; `sonnet`, `high`.
- LANDS IT: B12b's producer; `Item: B12b.23`, `[skip ci]`.

### B12b.24 — the supply arm refuses a realm that cannot eat · `16_PESSIMIST_SE_B` edit 4 · BUILD · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_SE_B_harvest_walls_and_the_supply_gate.md` R4, "Edits" 4, gate 4; closes F-PES-SE-09; H-241's sweep arm.
- ADVANCES: none of the nine; one fixture flip cannot make army size meaningless.
- INSTRUCTION: copied: "Beside the existing refusals at driver construction (`manifest/registrar.py::require_entries`'s neighbours), when `fixtures.get("field_provisioning")` is true:
  ```python
  ration = {k: r for k, r in fixtures.get("subsistence_weight").items() if r > 0}
  rungs = {o.rung for o in w.offices.values() if o.rung in w.rungs}
  rungs |= {t.object for s in settlements if (t := world_q.governing_hold(w, s)) and t.object in w.rungs}
  if ration and not any(all((w.rungs[r].stores or {}).get(k, 0) >= n for k, n in ration.items()) for r in rungs):
      raise Unspecified("`field_provisioning` is on and no treasury the field reads holds one ration",
                        "H-241", needs="stock at a seat rung or a held rung (07_SE_treasury_granary_B R-SE-28)",
                        law="IN-52: a levied treasury provisions a field")
  ```
  `H-241`'s sweep arm *'True on empty treasuries'* becomes a test of this refusal." R4: "this is the loader's refusal for that data family (`CLAUDE.md` §0.05: licensed, the loader's refusal per data family), not a guard over the tree. It also fixes the order of work: the granary moves before the arm flips."
- WHERE: the driver's construction check (`engine/season/loop/driver.py`, beside the `require_entries` call) `[ASSUMPTION: the site — the producer opens the construction path at the item's open]`; `engine/season/hole_register.yaml` (H-241's sweep arm text).
- TESTS: in `engine/season/tests/test_hunger.py` `[ASSUMPTION: the nearest existing file covering subsistence fixtures — basis: SE_A's gate]` (the source's own tag): `test_field_provisioning_refused_on_empty_treasuries`, written first, red.
- FALSIFIER and CONTROL: gate 4, copied: "`build_realm(0)` with `field_provisioning=True` and no other change: construction refuses, naming H-241. With the first lane's seat-rung stock applied: construction passes and a seeded march fields more than the floor on both sides." Control: the shipped arm off → nothing read; realm hash equal.
- GATE: `python -m pytest engine/season/tests/test_hunger.py -k field_provisioning -q` → pass; realm hash at seed 0, one season → equal.
- HASH MOVERS: none (shipped off).
- DEPENDS ON: EXISTS-IN-TREE `queries/world_q.py::governing_hold`, `engine/season/gaps.py::Unspecified`, `manifest/registrar.py::require_entries`; V12 Batch B12a (`07_SE_treasury_granary_B`, R-SE-28's seat-rung stock, for the passing arm).
- GLOSSARY: none.
- COST and TIER: small; `sonnet`, `high`.
- LANDS IT: B12b's producer; `Item: B12b.24`, `[skip ci]`.

### B12b.25 — a yield is a fact with a size · `16_PESSIMIST_SE_B` edit 2 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/16_PESSIMIST_SE_B_harvest_walls_and_the_supply_gate.md` R2, "Edits" 2 (with the C3-R7 decision and the grounding G-06), gate 2; rulings A-54; closes F-PES-SE-05.
- ADVANCES: none of the nine; a chronicle can say what a place brought in.
- INSTRUCTION: copied: "`World.write` gains a `spec` parameter, passed through to `Gate.mint` at its mint sites; the `yield` write passes the produced map, `spec=tuple(sorted(produced.items()))`, and, under A-54, the band of the season's draw beside it. Grounding (25 G-06): `World.write`'s parameters today are `thing, token, apply, record_kind, fieldname, driver, caused_person_exists, emits, causes, subject, actor, via, change, matured_term, observed`; `Gate.mint` already takes a `spec` and `StateChange` has the field." The alternative (a `Change` on `Subject.entity("rungs", rid, fields=("yield",))`) is "not taken here (R5 §1)": U3 C3-R7 chose the `spec` pass-through.
- WHERE: `engine/season/state/world.py` (`World.write`'s signature and its `Gate.mint` calls); `engine/season/loop/matter.py` (the `yield` write).
- TESTS: in `test_season_weather_per_territory.py`: `test_yield_receipt_carries_the_produced_map` — "A planted `yield` write: its Event's receipt carries the produced map; `World.content_hash()` of a world with no Site is unchanged"; red before.
- FALSIFIER and CONTROL: a `yield.taken` receipt with `spec` empty at a rung that produced; a reader in the loop branching on it (none may: "No reader in the loop branches on it"). Control: a world with no Site → hash unchanged.
- GATE: `python -m pytest engine/season/tests/test_season_weather_per_territory.py -q` → pass; realm hash at seed 0 after one season → moved (declared).
- HASH MOVERS: "every world where a yield is written" (the receipt is in the log the hash folds). Declared; B12b's re-pin. Not an encoding mover: `StateChange.spec` exists; `World.write`'s parameter is no carrier field.
- DEPENDS ON: EXISTS-IN-TREE `state/world.py::World.write`, `state/gate.py::Gate.mint` (`spec`), `state/carriers.py::StateChange`; V12 B12b.03 (the band); V12 Batch B09 (`16_PESSIMIST_CORE_the_record_holds_what_changed` edit 1, receipts).
- GLOSSARY: none.
- COST and TIER: small; `sonnet`, `high`.
- LANDS IT: B12b's producer; `Item: B12b.25`, `[skip ci]`.

### B12b.26 — the settlement's mood, `unrest(w, S)` · CP-T08-06 · HELD (its stop rule: CP-T08-07's gate, H-163 limit 3(a), unmet)
- SOURCE: the intake `:317` (CP-T08-06 · rows E1:118, E4:306, E4:678, E5:47; lane's target "B12/B38 · stop rule kept"); carry-forward `master/eval/E1.md` "### CP-T08-06" (entry `2026-10-23-subsystem-completion-08-settlements-governance-economy_part2.md:9-25`) and `master/eval/E5.md` Block C16 (NARROW AM-E-17, with the stop rule of ED-IN-0311); placed by §5.6's first rule (`U5d_SE_owed_edits.md` names it at `:77`, `:102`).
- STOPS IF (the entry's own rule, copied): "STOP RULE: if CP-T08-07's gate (H-163 limit 3(a), owned by CR-23) is not met at B10-16's entry … CP-T08-06 moves to B10-Z as HELD with it, because alone it is a gauge whose only reader is a census line. It does not merge into CP-T08-07's commit (P5: one position, one commit)." In v12: CP-T08-07 is the intake's MISSING-DEP entry under B33 ("its gate H-163 limit 3(a) has no owner in the tree or any proposal (E5:48)"), so at B12b's open the rule fires and this position is HELD with CP-T08-07; it goes to the head's held table (§7.9) with that trigger. The producer confirms at the open that `H-163` limit 3(a) still has no owner (`grep -n "H-163" engine/season/hole_register.yaml`) and writes the reading in the first item's commit body; if it has one, the position is built here as the override states.
- WHAT IT WOULD BUILD (E5 C16's override over the entry, copied): "Delete home item 2: no `unrest_signs` roster and no clause added to `stability`. `unrest(w, S)` is the sum over cohorts residing at S of `-stability(c, S, unrest_window)` as it already counts (dominance deeds including `requisition.taken`, and shortfall claims); the band is an `unrest_band_floors` Fixtures tuple (shipped `()`), as `hunger_band_floors` is. The falsifier uses `shortfall:grain` claims, not hunger-band claims. Its reader before CP-T08-07 is the census line only (`uncontrolled`'s precedent), so it is a report until `requisition` executes. REM-51 is cut." With the entry's census line `unrest_by_settlement` and `test_unrest.py`'s falsifier; hash none alone.
- Consequence for this batch: `amount_shares`' flip has no consequence path from `unrest` until this is built (DIALS AT CONTROL).

### B12b.27 — four register rows brought to the tree · `U5d_SE_owed_edits` §1 · BUILD · HASH EQUAL
- SOURCE: `proposals/U5d_SE_owed_edits.md` §1 (R-SE-16, -17, -18; H-105, H-171, H-309, H-168); the source's land order puts §1 first.
- ADVANCES: none of the nine; the register says what the tree does.
- INSTRUCTION: copied: "`engine/season/hole_register.yaml`: H-105 and H-171 cites gain '`restore`: 0 attempts, seed 0, three seasons, tree `601e715`; cause not isolated'; H-309 closed (a seat is a `hold` exercised `via`; absence is not an act; ladder step 4); H-168's cite re-read (false since IN-45: 16 executed migrations from computed acts, `aperture 3 0`). … No code. Not done here: a fix for `restore` not reaching; it waits on the cause." The H-168 re-read is taken at two seasons (`aperture 2 0`; three in the source, A-114) and its figure written with its tree; the two quoted readings for H-105 and H-171 are copied as the source gives them, with their tree.
- WHERE: `engine/season/hole_register.yaml` (H-105, H-171, H-309, H-168).
- TESTS: none (a register edit).
- FALSIFIER and CONTROL: `register --check` refusing the edited rows. Control: no code moves; realm hash equal.
- GATE: copied: "`python -m engine.season.harness.register --requirements` loads"; `python -m engine.season.harness.register --check` → exit 0.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `hole_register.yaml` rows H-105, H-171, H-309, H-168.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B12b's producer; `Item: B12b.27`, `[skip ci]`.

### B12b.28 — a debit drops the key it empties · `U5d_SE_owed_edits` §9 d · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/U5d_SE_owed_edits.md` §9 d (F-PES-SE-13); the land order's fourth.
- ADVANCES: none of the nine.
- INSTRUCTION: copied: "`loop/effects_shared.py::_debit` drops a key it has brought to 0 (the rule `provision.py` already states). Gate: a `build` leaves no `timber: 0` in the payer's stores. A hash mover wherever a debit empties a kind; declared."
- WHERE: `engine/season/loop/effects_shared.py` (`_debit`).
- TESTS: `test_build_leaves_no_zero_key_in_the_payer_stores` in `engine/season/tests/test_demand_delivery.py` `[ASSUMPTION: test name and file]`, written first, red.
- FALSIFIER and CONTROL: a debit to 0 that leaves the key; a debit to above 0 that drops it. Control: a debit that leaves stock reads as before. Note for B12b.40: SE_A's R2 reads "the key is written when a rung first holds the kind and survives its emptying"; `_debit` is the act's debit (RESOLVE), not the larder's MATTER take, so the larder's survival rule is untouched `[ASSUMPTION: the larder's take does not call `_debit` — the producer greps `_debit(` at the open and records the callers]`.
- GATE: `python -m pytest engine/season/tests/test_demand_delivery.py -q` → pass; realm hash at seed 0 after one season → moved where a debit emptied a kind (declared).
- HASH MOVERS: every world where a debit empties a kind. Declared; B12b's re-pin.
- DEPENDS ON: EXISTS-IN-TREE `loop/effects_shared.py::_debit`, `modules/settlements/provision.py`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B12b's producer; `Item: B12b.28`, `[skip ci]`.

### B12b.29 — CR-49's class on `transfer` and `migrate` · `U5d_SE_owed_edits` §2 · POINTER (lands with CR-49, Batch B12c)
- WHAT IT POINTS AT: `proposals/U5d_SE_owed_edits.md` §2 — "`referent_class: Rung` restricted to a settlement rung … and a `to != from` decline. A plan edit to CR-49's entry, so the three rows land as one" (rows `transfer`, `migrate` in `engine/season/verb_table.yaml`, with CR-49's `exchange`). Gate: "`python -m engine.season.harness.aperture 3 0` before and after: `transfer.made` to self goes to 0 (2 today, both to self); no `migrate` candidate names a non-settlement rung" (at two seasons in v12). Movers: "Every seeded run with a `transfer` or `migrate` candidate". It lands in CR-49's item in B12c (`V12_STRUCTURE_part2.md` §5.6 places CR-49 there); UNDECIDED (2). Also the formation half of the same-place rule (`07_SE_kernel_repairs.md` §4: "CR-49's shape applied to `move`").

### B12b.30 — the kinds a trade is formed on · `U5d_SE_owed_edits` §7 · POINTER (with §2, Batch B12c)
- WHAT IT POINTS AT: `proposals/U5d_SE_owed_edits.md` §7 — owner `decision/options.py` (operand bags for `exchange` and `transfer`): "`kind` is the kind the actor's rung holds most of beyond its own draw; `return_kind` is a kind its ladder was short of at the last MATTER (`World._subsistence_shortfall`), else the fixture default." Gate: "In `harness/scarce.py`'s short town, the formed `exchange` asks for the kind it lacks." "Depends on §2", so it lands after B12b.29's text, beside CR-49 in B12c; UNDECIDED (2).

### B12b.31 — the ration's kinds at the supply flip · `U5d_SE_owed_edits` §4 · POINTER (inside IN-52's flip entry, B12b.47)
- WHAT IT POINTS AT: `proposals/U5d_SE_owed_edits.md` §4 — "`engine/season/data/fixtures.py`: `field_ration_kinds`, shipped `["grain"]`; `modules/…/provision` bounds a field by a kind only if the fixture lists it and `subsistence_weight` weights it. Lands inside plan IN-52's flip entry, after `07_SE_treasury_granary_B.md` and with `16_PESSIMIST_SE_B…` edit 4 (the load-time refusal). Gate: a grain-only treasury fields troops in the flipped arm." B12b.24 lands the refusal; the fixture lands in B12b.47, IN-52's flip (routed to this batch by B12a's author; `master/eval/E2.md:103`: "B12, last item").

### B12b.32 — the migration arm of the stocking gate · `U5d_SE_owed_edits` §10 · POINTER (carried by `07_SE_ground_and_granaries`, Batch B12a)
- WHAT IT POINTS AT: `proposals/U5d_SE_owed_edits.md` §10 — "`07_SE_ground_and_granaries.md` §4 (c)'s gate gains one arm: `migrate`'s executed count and refusal clauses in the stocked arm against the unstocked control". That file's head carries it ("The gate gains the migration arm of `U5d_SE_owed_edits.md` §10"), so the arm is in its item's gate in B12a; nothing lands here. If B12a's close record shows no such arm, it is read at this batch's close as R2's companion and the commit body says so.

### B12b.33 — `ore` gets a reader in five works costs · `U5d_SE_owed_edits` §9 a · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/U5d_SE_owed_edits.md` §9 a (R-PES-SE-07).
- ADVANCES: none of the nine; a registered kind with a reader.
- INSTRUCTION: copied: "`rosters.yaml: works_cost` rows `garrison`, `barracks`, `archery_range`, `stable`, `siege_workshop` gain `ore: 10` beside timber `[ASSUMPTION; medium; Jordan to correct]`, so `ore` has a reader. A data edit; a mover only where such a works is built."
- WHERE: `engine/season/rosters.yaml` (`works_cost`: five rows).
- TESTS: none new; the founding tests that read `works_cost` stay green (`grep -rl works_cost engine/season/tests` names them at the open).
- FALSIFIER and CONTROL: a `build` of a `garrison` that debits no `ore`. Control: a `build` of any other works unchanged.
- GATE: `python -m pytest $(grep -rl works_cost engine/season/tests) -q` → pass; realm hash at seed 0 after one season → equal unless one of the five was built (the commit body says which).
- HASH MOVERS: worlds in which one of the five works is built. Declared; B12b's re-pin.
- DEPENDS ON: EXISTS-IN-TREE `rosters.yaml: works_cost`, `loop/effects_founding.py` (`_cost`); V12 B12b.28 (`_debit`).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B12b's producer; `Item: B12b.33`, `[skip ci]`.

`B12b.34` is a READING (`U5d_SE_owed_edits` §5; its text is R2 in the `## Readings` block below).

### B12b.35 — the body loss is per head, behind `hunger_loss` · `07_SE_population_census` (a) · BUILD · HASH EQUAL
- SOURCE: `proposals/07_SE_population_census.md` R1, §4 (a), §5; rulings A-54 (the loss's draw is `09_WR_B_draws_not_thresholds.md` edit 2, Batch B12a); closes H-305.
- ADVANCES: none of the nine; one ladder for the body, per head everywhere.
- INSTRUCTION: copied: "The loss itself is drawn on the four-band ladder (A-54); the owner of that draw is `09_WR_B_draws_not_thresholds.md` edit 2 (the hungry body drawn in `subsist`). This edit supplies only the per-head scaling, which becomes the **Partial band's magnitude** of that draw (`body_step × units // weight`); the code below is the arithmetic at the shipped control (no draw), kept so the `per_head` arm can be read before the draw lands. … Old: `for pid in sorted(short): lost = inp.body_step * sum(short[pid].values())` New:
  ```python
      weight_of = {e.pid: e.weight for e in inp.larder.eaters}
      for pid in sorted(short):
          units = sum(short[pid].values())
          lost = inp.body_step * units // weight_of[pid] if inp.per_head else inp.body_step * units
  ```
  `SubsistInput` gains `per_head: bool`, projected by `world_q.subsist_input` from a fixture `hunger_loss="per_cohort"` (shipped, today's) `/ "per_head"`. At the shipped weight 2 the `per_head` arm halves every loss, so `body_step` is re-read at CR-22 under it." Since B12a has landed the drawn loss, the old line is the draw's Partial magnitude: the producer applies the `// weight` scaling to that magnitude where B12a left it and records the before text in the commit body. The test file is written first (U3 §6.1: `test_cr08_census_weight.py`, "written as the batch's first commit"; here the census's first commit).
- WHERE: `modules/settlements/subsist.py` (the loss); `engine/season/queries/inputs.py` (`SubsistInput.per_head`); `engine/season/queries/world_q.py` (`subsist_input`); `engine/season/data/fixtures.py` (`hunger_loss`, its tag); NEW `engine/season/tests/test_cr08_census_weight.py`.
- TESTS: in the new file: `test_per_head_halves_the_loss_at_weight_two`, `test_per_cohort_is_the_control` `[ASSUMPTION: test names]`, red before.
- FALSIFIER and CONTROL: under `per_head` a weight-20 cohort losing ten times a weight-2 cohort's body for the same per-head shortfall (H-305's defect). Control: `hunger_loss` `per_cohort` → realm hash equal.
- GATE: `python -m pytest engine/season/tests/test_cr08_census_weight.py engine/season/tests/test_hunger.py -q` → pass; realm hash at seed 0, one season → equal.
- HASH MOVERS: none at `per_cohort`.
- DEPENDS ON: EXISTS-IN-TREE `modules/settlements/subsist.py::subsist`, `queries/inputs.py::SubsistInput`, `queries/world_q.py::subsist_input`; V12 Batch B12a (`09_WR_B_draws_not_thresholds` edit 2's drawn loss).
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high` (the placement was decided once, C3-C3, `opus`).
- LANDS IT: B12b's producer; `Item: B12b.35`, `[skip ci]`.

### B12b.36 — a starving cohort thins before it dies, behind `famine_loss` · `07_SE_population_census` (b), (c), (e) · BUILD · HASH EQUAL
- SOURCE: `proposals/07_SE_population_census.md` R2, §4 (b), (c), (e), §5; C3-C3 (the writer at MATTER); rulings A-56, A-15; closes CR-08's falling half (H-49).
- ADVANCES: none of the nine; a famine damps itself (the first declared damping loop in the economy).
- INSTRUCTION: one commit for (b), (c), (e): they share the MATTER pass, the matrix cell and one gate (E-13). Copied:
  (b) "`engine/season/loop/matter.py`, inside the `for fall in sub.falls:` loop, after the body write and before the death test:
  ```python
          loss = w.fixtures.get("famine_loss")        # per-mille of weight; 0 is the control (no write)
          floor = (w.fixtures.get("band_floors") or {}).get("body", {}).get("withdrawal_only")
          if loss and floor is not None and person.is_cohort and person.body < floor:
              after = max(1, person.weight - max(1, person.weight * loss // 1000))
              if after != person.weight:
                  w.write("weight", token, lambda person=person, after=after: setattr(person, "weight", after),
                          record_kind="Person", fieldname="weight", driver="Event",
                          emits="weight.changed", subject=pid, causes=[fell.id] if fell else [ROOT])
  ```
  The cause is the `body.changed` just written (`fell`, in hand), not a log search. Fixture `famine_loss=0` in `data/fixtures.py` (swept `0 / 250 / 500`), with its hole-register row (H-49 gains the arm). **Matrix edit owed:** `engine/season/write_matrix.yaml`, the `(Person, weight)` row, `steps: [CEN]` → `steps: [MAT, CEN]` (the `(Rung, envelope)` row's two steps are the precedent); CENSUS keeps individuation. `04` §A.2 lists `weight` under `loop/census` while `holonic` §25 and §29 put deaths at MATTER and bar a clock at CENSUS: the ambiguity is named at this site and picked (layer-conformance B4); `04` is not edited."
  (c) "Old: `if fall.body_after <= 0: _die(w, token, pid)` New: `if fall.body_after <= 0 and (person.weight <= 1 or not w.fixtures.get("famine_loss")):`. With `famine_loss` 0 the condition is today's."
  (e) "The asymmetry sweep (CLAUDE.md §0.1 pt 1). `weight` gains a writer where every reader assumed a constant: list in the commit every reader of `Person.weight` found by grep at the build (`larder_draw`'s want, `housing`'s population, `has_room`, `sides.py`'s muster weight, `effects_army.py`'s `recruit`, `seat_guards`' ceiling check) and state for each whether a falling weight is read correctly."
- WHERE: `engine/season/loop/matter.py` (the hunger fall loop; the death test); `engine/season/data/fixtures.py` (`famine_loss`); `engine/season/write_matrix.yaml` (`(Person, weight)`: `steps: [MAT, CEN]`, the site's ambiguity note); `engine/season/hole_register.yaml` (H-49's arm); `engine/season/tests/test_cr08_census_weight.py`.
- TESTS: in `test_cr08_census_weight.py`, written first: "on `harness/scarce.build` with `famine_loss 500` and `hunger_loss per_head`: the hungry cohort's weight falls 10 → 5 → 3 → 2 → 1 across the seasons its body stands under the floor, each fall emits `weight.changed` whose cause is a `body.changed`, its `demanded` falls with it, and it is removed only at weight 1 and body 0" — split to keep to two seasons (A-114): `test_hungry_cohort_thins_ten_five_three` (two seasons: 10 → 5 → 3, each `weight.changed` caused by a `body.changed`, `demanded` falling with it) and `test_cohort_at_weight_two_thins_to_one_then_dies_at_body_zero` (a planted cohort at weight 2 under the floor: one season to weight 1, the next removed at body 0); `test_famine_loss_zero_is_the_control` ("`famine_loss 0` reproduces `scarce.build`'s shipped hash and the cohort dies as it does today") `[ASSUMPTION: test names; the split is this plan's, the readings the source's]`.
- FALSIFIER and CONTROL: copied: "A cohort under the floor that keeps its weight; a cohort over the floor that loses any; a `weight.changed` with `[ROOT]` as cause on a cohort whose body was ever written. Mutation: read `p.body <= 0` instead of the floor, and the 10 → 5 step never fires before death." Control: `famine_loss 0` → realm hash equal. "CR-08's own exit stands: `grep -rn "weight.changed" engine/season` finds the writer."
- GATE: `python -m pytest engine/season/tests/test_cr08_census_weight.py engine/season/tests/test_hunger.py -q` → pass; `git grep -n "weight.changed" -- engine/season/loop` → the writer; `python -m engine.season.harness.register --check` → exit 0; realm hash at seed 0, one season → equal.
- HASH MOVERS: none at `famine_loss 0`.
- DEPENDS ON: V12 B12b.35; EXISTS-IN-TREE `loop/matter.py::_die`, `write_matrix.yaml` `(Person, weight)` and `(Rung, envelope)`, `harness/scarce.py::build`, `band_floors.body.withdrawal_only` `[the producer reads the band name at the open]`.
- GLOSSARY: none (`famine_loss`'s fixture note: "the share of a starving cohort's people lost each season, in thousandths").
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B12b's producer; `Item: B12b.36`, `[skip ci]`.

### B12b.37 — a town with nobody in it reads `empty` · `07_SE_population_census` (d) · BUILD · HASH EQUAL
- SOURCE: `proposals/07_SE_population_census.md` R3, §4 (d), §7 ("The `hunger_bands` edit moves no hash (the loop does not read `hunger`); it moves the census text").
- ADVANCES: none of the nine; extinction is visible.
- INSTRUCTION: copied: "**`engine/season/rosters.yaml: hunger_bands`.** `values: [starving, hungry, lean, fed, empty]`; `world_q.hunger` returns `("empty", Fraction(0), 0)` when `D == 0` and no cohort resides under the rung, and `world_q`'s unpack of first and last members reads `fed` by name rather than by position. The census line `hunger_by_settlement` then prints `empty` for a depopulated town. `test_hunger.py` gains the case; its `test_g` limit text is corrected."
- WHERE: `engine/season/rosters.yaml` (`hunger_bands`); `engine/season/queries/world_q.py` (`hunger`; the first/last unpack); `engine/season/tests/test_hunger.py` (the case; `test_g`'s limit text).
- TESTS: `test_settlement_with_no_cohort_reads_empty` `[ASSUMPTION: test name]` in `test_hunger.py`, red before (reads `fed`).
- FALSIFIER and CONTROL: a settlement with a cohort and `D == 0` reading `empty` (only the absence of a cohort does). Control: realm hash equal (no loop reader of `hunger`).
- GATE: `python -m pytest engine/season/tests/test_hunger.py -q` → pass; realm hash at seed 0, one season → equal; the census line printed by `aperture 1 0` lists `empty` where a rung has no cohort.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `queries/world_q.py::hunger`, `rosters.yaml: hunger_bands`, `residence_of`; V12 B12b.36.
- GLOSSARY: the *hunger band* row gains `empty`: "no one lives there to be fed".
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B12b's producer; `Item: B12b.37`, `[skip ci]`.

### B12b.38 — a fed, housed, quiet cohort regrows, behind `regrow_seasons` · `07_SE_population_regrowth_B` (a)–(c) · BUILD · HASH EQUAL
- SOURCE: `proposals/07_SE_population_regrowth_B.md` R-SE-26, §4 (a), (b), (c), (d), §5; rulings A-51, A-55, ED-SE-0051 (RR-2's capacity bound); closes R-SE-26, S-SE-1, CR-08's rising half.
- ADVANCES: none of the nine; settlements breathe with nobody watching.
- INSTRUCTION: copied: "**(a) `engine/season/loop/matter.py`**, in the bodies-clock section ('THE BODIES CLOCK: AGEING AND ILLNESS (v9 IN-34)'), as its own guarded block after the hunger fall and before or beside the ageing hazard.
  ```python
      regrow = w.fixtures.get("regrow_seasons")           # 0 is the control: no read, no write
      if regrow:
          scale = w.fixtures.get("condition_scale")
          homes = world_q.residence_of(w)
          fell = {f.pid for f in sub.falls}
          for pid in sorted(w.persons):
              p = w.persons[pid]
              home = homes.get(pid)
              if not p.is_cohort or home is None or p.body < scale:    # the carrier's one owner of the test
                  continue
              if pid in short_by_person or pid in fell:                  # matter: fed in full this season
                  continue
              if world_q.quiet_since(w, pid, ("body.changed", "weight.changed")) < regrow:
                  continue
              if world_q.population(w, home, homes) >= world_q.capacity(w, home):   # the ruled room bound
                  continue
              prior = w.last_emission_of("weight.changed", pid, written=True)
              w.write("weight", token, lambda p=p: setattr(p, "weight", p.weight + 1),
                      record_kind="Person", fieldname="weight", driver="Event",
                      emits="weight.changed", subject=pid, causes=[prior] if prior else [ROOT])
  ```
  `quiet_since` (seasons since the newest written Event of the named kinds on the subject, or since tick 0) is one small reader in `queries/world_q.py`, beside `body_hazard`, the bodies clock's existing Query; it stores nothing. `residence_of`, `population` and `capacity` are the readers `migrate`'s `has_room` already uses: the same room, no second ladder. … **(b)** `engine/season/write_matrix.yaml`, the `(Person, weight)` row: `steps: [CEN]` becomes `steps: [MAT, CEN]` (made once, by `07_SE_population_census.md` §4 (b), which lands first in B12 under C3-C3; this file checks the cell is present and adds nothing if it is), `class: MATTER` and `social: false` unchanged, and its `by:` cell gains the ground: Layer 1 §25 ('envelope weight — births and deaths' at MATTER; bodies a licensed clock) and §29 (no clock at CENSUS). **(c)** `engine/season/data/fixtures.py`: `regrow_seasons=0`, with H-49's register row gaining the arm beside the first proposal's `famine_loss`." (d): "every reader it lists … is monotone in weight" — no edit; (e) "No edit to `modules/settlements/`."
- WHERE: `engine/season/loop/matter.py` (the bodies-clock block); `engine/season/queries/world_q.py` (`quiet_since`); `engine/season/write_matrix.yaml` (`(Person, weight)`'s `by:` cell); `engine/season/data/fixtures.py` (`regrow_seasons`); `engine/season/hole_register.yaml` (H-49's arm); `engine/season/tests/test_in34_bodies_clock.py`.
- TESTS: in `test_in34_bodies_clock.py`, written first, at two seasons (the source's run is longer; A-114): "on `harness/scarce.build` with `regrow_seasons 2` and the hungry cohort fed from tick 0: its weight rises by 1 every second season until `population == capacity`, then stops; build a dwelling there and it rises once more. Each rise emits `weight.changed`; `|w.persons|` is unchanged throughout" — as `test_quiet_fed_housed_cohort_rises_once_in_two_seasons` (`regrow_seasons 2`: one rise by the second season), `test_no_rise_at_capacity` (planted at `population == capacity`), `test_no_rise_in_a_short_season`, `test_person_count_unchanged`; the two-arm reading ("starve the cohort for three seasons, then feed it. Its weight falls, then returns") is written at two seasons with `regrow_seasons 1` and a one-season starvation `[ASSUMPTION: test names and the shortened arms; the readings are the source's]`.
- FALSIFIER and CONTROL: copied: "A rise in a season the cohort was short; a rise past capacity; a rise within `regrow_seasons` of a fall; any change in the count of persons; any `weight.changed` written with `w.step == Step.CENSUS` by this branch. Mutation: drop clause (iii) and the capacity assertion reds; remove `MAT` from the `(Person, weight)` cell and the write raises at the gate." "**Control.** `regrow_seasons 0` reproduces the shipped hashes."
- GATE: `python -m pytest engine/season/tests/test_in34_bodies_clock.py engine/season/tests/test_cr08_census_weight.py -q` → pass; realm hash at seed 0, one season → equal.
- HASH MOVERS: none at `regrow_seasons 0`.
- DEPENDS ON: V12 B12b.36 (the `MAT` step on the cell); EXISTS-IN-TREE `queries/world_q.py::residence_of`, `::population`, `::capacity`, `::body_hazard`, `World.last_emission_of`, `loop/matter.py`'s bodies-clock section; V12 Batch B12a (`seasons_of_year`, for A-51's prologue, which is B39's).
- GLOSSARY: none (`regrow_seasons`' fixture note: "how many quiet, fed seasons a housed cohort waits before it grows by one").
- COST and TIER: small build; `sonnet`, `high` (placement decided once, U3 C3-C3, `opus`).
- LANDS IT: B12b's producer; `Item: B12b.38`, `[skip ci]`.

### B12b.39 — a short rung is shared in proportion to want · `16_PESSIMIST_SE_A` edit 1 · BUILD · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_SE_A_the_granary_shares_and_the_dead_are_accounted.md` R1, "Edits" 1, gate rows 1–2, 6; the source's order "1 → 2 → 3 → 4"; closes F-PES-SE-01.
- ADVANCES: none of the nine; a dearth at a shared store is a shared hardship, not one arbitrary victim.
- INSTRUCTION: copied: R1 "For each kind, in rounds: every eater with want left points at the first rung on its ladder that holds any of the kind at the start of the round and that it has not yet drawn from this draw. Per rung, if the claims fit, each takes its claim; if they do not, each takes `held × claim // total` and the units left over go one each, in the order of a permutation the host draws for the season, to claimants still short. Under `larder_walk: first` (shipped) there is one round; under `through` (the first lane's R4) rounds repeat until one moves nothing." Edit 1: "`LarderInput` gains `order: tuple = ()`: the eaters' pids in the season's drawn order. The host fills it:
  ```python
  keyed = draw_factory(w.world_seed, lambda: w.tick)
  order = tuple(keyed("larder", "remainder").sample(sorted(cohort_pids), len(cohort_pids)))
  ```
  `()` is the control arm (remainder in host order) and reproduces today's remainder rule for tests that plant it. `larder_draw`'s body becomes the round loop of R1. Its cell keeps today's shape `(kind, want, take, src)` under `first`; under `through` it is the first lane's list of `(src, take)`, unchanged by this proposal. The module still draws nothing: the permutation arrives on its typed input." (The source's "in rounds" is the loop's passes over the eaters, not a fight's round.)
- WHERE: `engine/season/queries/inputs.py` (`LarderInput.order`); `engine/season/queries/world_q.py` (`_larder_parts`); `modules/settlements/larder.py` (`larder_draw`).
- TESTS: in `engine/season/tests/test_hunger.py`, written first: `test_short_rung_is_shared_in_proportion_to_want` (row 1: "Two cohorts of weight 2 on one rung holding grain 4, salt 2: each takes grain 2, salt 1; each falls 30; `shortfalls` names the rung with the gap (grain 4, salt 2). Control: the rung holding grain 8, salt 4: both fed, no report"), `test_odd_unit_varies_over_season_keys` (row 2: "Three cohorts on a rung holding 4 grain: takes sum to 4; over 200 season keys the cohort receiving the odd unit varies (the falsifier for 'drawn': one cohort receiving it 200 of 200)", asserting it checked 200); in `test_demand_delivery.py`: `test_takes_sum_to_what_was_held`.
- FALSIFIER and CONTROL: one cohort receiving the odd unit at all 200 keys; takes that do not sum to what was held. Control: "Edit 1 moves no shipped hash in `build_realm`: every settlement there eats from its own rung in surplus"; gate row 6: "`build_realm(0)`, three seasons [two, A-114], barrier-only: content hash equal to base at edit 1".
- GATE: `python -m pytest engine/season/tests/test_hunger.py engine/season/tests/test_demand_delivery.py -q` → pass; realm hash at seed 0 after two seasons → equal.
- HASH MOVERS: none in `build_realm` (one eater per rung, in surplus).
- DEPENDS ON: EXISTS-IN-TREE `queries/inputs.py::LarderInput`, `queries/world_q.py::_larder_parts`, `modules/settlements/larder.py::larder_draw`; V12 Batch B06 (`draw_factory`); V12 Batch B12a (`07_SE_ground_and_granaries`' `larder_walk`); V12 B12b.01 (the `want` scaling in `_larder_parts`, kept).
- GLOSSARY: none.
- COST and TIER: small; `sonnet`, `high`.
- LANDS IT: B12b's producer; `Item: B12b.39`, `[skip ci]`.

### B12b.40 — a first dearth is reported once · `16_PESSIMIST_SE_A` edit 2 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/16_PESSIMIST_SE_A…` R2 (with D-69's rewrite), "Edits" 2, gate row 3 and row 6's second half; rulings D-69.
- ADVANCES: none of the nine; the no-player half's first settlement hook: a reported crossing.
- INSTRUCTION: copied: "`SubsistInput` gains `short_before: tuple = ()` — `((pid, (kind, …)), …)` projected from `World._subsistence_shortfall` (the field's first loop reader) — and `once_held: tuple = ()` — `((rung, (kind, …)), …)`, the kinds each ladder rung's `stores` carries a key for. In `subsist`, after the existing `drained` pass:
  ```python
  before = {pid: frozenset(kinds) for pid, kinds in inp.short_before}
  held_once = {rung: frozenset(kinds) for rung, kinds in inp.once_held}
  ladders = dict(inp.larder.ladders)
  for row in draw.rows:
      for kind, want, take, src in row.cells:
          if take >= want or src is not None or kind in before.get(row.pid, ()):
              continue                      # fed; or already counted as drained; or not a crossing
          ladder = ladders.get(row.home, ())
          at = next((r for r in ladder if kind in held_once.get(r, ())), None)
          if at is None and ladder:
              at = ladder[0]                # D-69: a never-stocked ladder reports once, at its first rung
          if at is not None:
              drained.setdefault(at, set()).add(kind)
  ```
  The `kind in before` test makes either arm fire once per dearth (the crossing), never per season. `shortfalls` is then computed as today. In `loop/matter.py`, `short_seen[rung]` rides the rung's larder write where one exists this barrier (today's path). Where the rung has no write this barrier (it was already empty), the Observation rides the `body.changed` write of the first short cohort homed under it, by `observed=` on that write. With `body_step` at 0 there is no such write and the crossing is unreported, which the control arm's note should say. WITNESS's seat channel already routes an actorless Event's Observations by `Observation.subject` (`loop/witness.py`, `world_q.governors_of(w, o.subject)`), so the rung's governors receive it with no edit there."
- WHERE: `engine/season/queries/inputs.py` (`SubsistInput.short_before`, `.once_held`); `engine/season/queries/world_q.py` (`subsist_input`); `modules/settlements/subsist.py` (`subsist`); `engine/season/loop/matter.py` (`short_seen`'s carrier).
- TESTS: in `test_hunger.py`, written first: `test_exact_multiple_granary_reports_once` (row 3: "the exact-multiple granary reports once, in the season the town first goes unfed, at the granary rung; never again while the dearth lasts … Control: a cohort fed every season reports nothing" — the K7 granary replayed at two seasons with one season's stock), `test_never_stocked_ladder_reports_once_at_its_first_rung` ("A ladder with no key for the kind reports once, at its first rung, and then nothing (D-69)").
- FALSIFIER and CONTROL: a dearth reported twice in one run of short seasons; a never-stocked ladder silent. Control: a fed cohort reports nothing.
- GATE: `python -m pytest engine/season/tests/test_hunger.py -q` → pass; row 6: "edit 2 moves [the realm hash] by the season-0 ladders' one report each (declared, D-69)" — realm hash at seed 0 after one season → moved.
- HASH MOVERS: "the realm's season-0 ladders hold no key for any kind, so each short cohort's first dearth now reports once at the first rung of its ladder (D-69)". Declared; B12b's re-pin.
- DEPENDS ON: V12 B12b.39; EXISTS-IN-TREE `queries/inputs.py::SubsistInput`, `World._subsistence_shortfall`, `loop/witness.py`'s seat channel, `world_q.governors_of`.
- GLOSSARY: none.
- COST and TIER: small; `sonnet`, `high`.
- LANDS IT: B12b's producer; `Item: B12b.40`, `[skip ci]`.

### B12b.41 — hunger is a cause on the fall and the death · `16_PESSIMIST_SE_A` edit 3 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/16_PESSIMIST_SE_A…` R3, "Edits" 3, gate row 4.
- ADVANCES: none of the nine; a record can say *died of hunger at X*.
- INSTRUCTION: copied: "
  ```python
  prior_b = (w.last_emission_of("stores.changed", short_at[pid])      # R2's rung, where there is one
             or w.last_emission_of("body.changed", pid, written=True))
  …
  if fall.body_after <= 0:
      _die(w, token, pid, cause=fell.id if fell else None)
  ```
  and `_die(w, token, pid, cause=None)` writes `causes=[cause] if cause else ([prior_d] if prior_d else [ROOT])`. The bodies-clock caller passes nothing and is unchanged." The death test is B12b.36's guarded form (`and (person.weight <= 1 or not famine_loss)`), kept.
- WHERE: `engine/season/loop/matter.py` (the hunger fall's `causes`; `_die`'s `cause` parameter).
- TESTS: in `test_hunger.py`: `test_hunger_death_cites_the_fall_and_the_store` (row 4: "every death Event's `causes[0]` is a `body.changed` whose `causes[0]` is a `stores.changed` at a highland rung", on a planted world with the highland rungs stocked for one exact season, two seasons), written first, red.
- FALSIFIER and CONTROL: a hunger death citing `ROOT` or an earlier death. Control: an ageing death (bodies clock) unchanged.
- GATE: `python -m pytest engine/season/tests/test_hunger.py engine/season/tests/test_in34_bodies_clock.py -q` → pass; realm hash moved where a body falls by hunger (declared).
- HASH MOVERS: "every hash in which a body falls by hunger (the cause list is part of the Event)". Declared; B12b's re-pin.
- DEPENDS ON: V12 B12b.40 (`short_at`); V12 B12b.36 (the guarded death test); EXISTS-IN-TREE `loop/matter.py::_die`, `World.last_emission_of`.
- GLOSSARY: none.
- COST and TIER: small; `sonnet`, `high`.
- LANDS IT: B12b's producer; `Item: B12b.41`, `[skip ci]`.

### B12b.42 — `tend` declines a cohort the larder cannot feed · `16_PESSIMIST_SE_A` edit 4 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/16_PESSIMIST_SE_A…` R4, "Edits" 4 (the primary form), gate row 5; rulings A-56 (`tend` is a cohort move); U3 §4.1 row 47 (C-32: `tend`'s row is owned by `14_VERBS_MATERIAL_A_mending.md` §6); UNDECIDED (3).
- ADVANCES: none of the nine; food, not nursing, mends hunger (H-304).
- INSTRUCTION: copied, the primary form: "a typed `requires` conjunct on the `tend` row, `ScalarThreshold` on the cohort's unfed gap (`04` §F.24a: the typed form for 'a computed scalar against a threshold'): the gap is the sum over `world_q.subsistence_draw(w)`'s cells for the cohort of `want - take`, and the conjunct admits `tend` on a cohort only where it is 0. The refusal is then a keyed clause under `04` §B.13 inv. 4 (`tend.refused` at that clause), not an effect-body decline. The scalar's reader is a `world_q` Query over the present world (an eligibility read, not new state)." "`14_VERBS_MATERIAL_A_mending.md` §6 makes `tend` a graded draw; this conjunct sits in front of it and does not touch it." The fallback (an effect-body decline in `_eff_tend`) is not written: it would collide with MAT_A §6's `_eff_tend` edit in B12c; if the typed grammar cannot spell the gap, the item stops and reports (`STOPPED`), and B12c's author receives the fallback with MAT_A §6.
- WHERE: `engine/season/verb_table.yaml` (row `tend`: `requires_typed`); `engine/season/queries/world_q.py` (the unfed-gap Query); `engine/season/data/requires.py` (the `ScalarThreshold` stem, if the gap needs a stem) `[ASSUMPTION: whether a new stem is needed — the producer reads `04` §F.24a's form at the open]`.
- TESTS: in `test_hunger.py`: `test_tend_refused_on_an_unfed_cohort` (row 5: "cohort `tend` on a short cohort refused; highland bodies fall season on season. Control: the fed arm unchanged"), written first, red.
- FALSIFIER and CONTROL: a short cohort tended to full body; a fed cohort refused. Control: the fed arm unchanged.
- GATE: `python -m pytest engine/season/tests/test_hunger.py -q` → pass; realm hash after one season at seed 0 → moved ("the realm's season 1 (the season-0 fall is tended there today)").
- HASH MOVERS: "any run in which a short cohort is tended". Declared; B12b's re-pin.
- DEPENDS ON: V12 B12b.39 (the draw the gap reads); EXISTS-IN-TREE `verb_table.yaml` row `tend` (`requires_typed`), `queries/world_q.py::subsistence_draw`, `data/requires.py`.
- GLOSSARY: none.
- COST and TIER: small; `sonnet`, `high`; the typed-form choice read by `opus` if the grammar cannot spell the gap.
- LANDS IT: B12b's producer; `Item: B12b.42`, `[skip ci]`.

The five positions below are the intake entries the B12a authors routed here by `V12_STRUCTURE_part4.md` E-8 (each needs the calendar, the drawn weather or the census, which land in this batch). They are numbered after B12b.42 and land after it: each moves hashes, and §5.9 puts the hash-EQUAL items first; nothing above gates on them.

### B12b.43 — the weather arm goes live on the drawn form · CL-EVENTS commit (2) with `09_WR_B_weather` edit 2's sweep · BUILD · HASH MOVER(behaviour)
- SOURCE: the intake `:356` (CL-EVENTS · rows E1:158, E2:60, E4:233 · "before CR-73 and `09_WR_B_weather_with_memory_and_the_year` · amended by A-54 · hash: M (commit 2; commits 1, 3 and 4 EQUAL)" · settled: "`U5_FINDINGS_CLOSURE_U5d.md:579` carries 'plan B10-18 CL-EVENTS (2) with `09_WR_B_weather_with_memory_and_the_year`' (amended by A-54)"); carry-forward `master/eval/E1.md` "### CL-EVENTS" (the card row; the entry `workplans/valoria_master_workplan_v11_part4.md:308-316`, commit (2)); `proposals/09_WR_B_weather_with_memory_and_the_year.md` edit 2 (R1 below); routed here by B12a's author (E-8); rulings A-54, M16 (b); closes CL-EVENTS (2), H-26's sweep arm.
- ADVANCES: none of the nine; the shock branch of hunger (CR-22's "the shock branch is filled by CL-EVENTS (2)").
- INSTRUCTION: (1) The card's commit (2), copied: "(2) the live arm `((0.5, 1.0, 2.0),)*4` (H-26's declared sweep arm until Jordan names the values) … `[ASSUMPTION; medium; Jordan to correct; revert: ()]`." Under A-54 (the amendment the intake records) the table no longer multiplies: a non-empty `season_factor_draw` (length `len(SEASONS_OF_YEAR)`, B12b.03's load check) switches on B12b.03's drawn form, and the yield is `SEASON_BAND_FACTORS[band]` (UNDECIDED (8)). (2) `09_WR_B_weather` edit 2's sweep (R1), taken in this commit at two seasons (eight in the source; A-114), seeds 0–2: three candidate `season_band_factors` sets `[ASSUMPTION: (2.0, 1.2, 0.8, 0.4), (1.5, 1.1, 0.9, 0.5), (1.25, 1.0, 0.9, 0.7) for Overwhelming, Success, Partial, Failure — basis: none stated; the sweep picks]`; ship the set whose mean harvest factor is nearest one and inside the control's seed-to-seed spread; the table in the commit body. (3) `season_factor_draw` set to the live arm; `season_band_factors` to the chosen set, each `[ASSUMPTION; medium; Jordan to correct]`. `season_spell_draw` stays `()` (B98).
- WHERE: `engine/season/data/fixtures.py` (`season_factor_draw`); `engine/season/rosters.yaml` (`season_band_factors`); `engine/season/hole_register.yaml` (H-26's `default:`).
- TESTS: `test_season_weather.py` and `test_season_weather_per_territory.py` re-read; their arm-on tests already plant the arm; a moved shipped-arm pin is B12b.99's.
- FALSIFIER and CONTROL: the card's, re-read on the drawn form: "at the live arm two territories at one tick draw different factors at some seed, and a territory at 0.5 [at a Failure band] holds stores below the control's after its yield step; planted failure: the territory dropped from the key gives equal factors." Edit 2's: the shipped set's mean departs from one by more than the control's spread. Control: "`()` reproduces the base hash".
- GATE: `python -m pytest engine/season/tests/test_season_weather.py engine/season/tests/test_season_weather_per_territory.py -q` → pass; `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 2 0` (seeds 1, 2) → hashes moved (declared); the sweep table in the commit body.
- HASH MOVERS: every seeded world (every territory's yield is drawn). Declared; B12b's re-pin.
- DEPENDS ON: V12 B12b.03 (the drawn form), B12b.01 (`season_terms.hardship`), B12b.22 (grown kinds only); V12 Batch B12a (`seasons_of_year`).
- GLOSSARY: none.
- COST and TIER: calibration; `sonnet` runs, `opus` reads the sweep.
- LANDS IT: B12b's producer; `Item: B12b.43`, `[skip ci]`.

### B12b.44 — hunger binds: the per-head need chosen by a reading rule · CR-22, H-11, H-125 · BUILD · HASH MOVER(behaviour)
- SOURCE: the intake `:321` (CR-22, H-11, H-125 · STILL-NEEDED · rows E1:162, E2:28, E3:449, E3:552, E4:351, E6:42 · "B12 after CP-T08-02 · amended" · settled: "H-11: the register row's fixture is shipped, but its closure is v11 CR-22's MEASURE-then-BUILD (E3 Block 16); one item with CR-22"); carry-forward `master/eval/E1.md` "### CR-22" (entry `workplans/valoria_master_workplan_v11_part4.md:88-100`); routed here by B12a's author (E-8: it needs "CP-T10-03's calendar flip, CL-EVENTS (2)'s live weather draw and CR-08", which are B12b.01, B12b.43 and B12b.36); M6 taken (a); closes CR-22, H-11, H-125.
- ADVANCES: R-04's settlement row (the card's "R R-04"); the batch's requirement cell stays "re-read only" (`V12_STRUCTURE.md` §2.2), so the close quotes it.
- INSTRUCTION: copied, with the horizon at two seasons (eight in the source; A-114) and "calendar on" read as B12a's declared year: "THE RULE: run the per-head arms (×1, ×5, ×20 on both eaten kinds) on `build_realm` seeds 0-2 for eight seasons, calendar on, the live weather draw on, `body_step` 10; ship the gentlest arm at which REM-50 reads at least one settlement below `fed` in a season after season 1, at every seed; if ×5 does not bind and ×20 drains every settlement, bisect once (×10). SEASON-0 FLOOR RULE: no cohort's body crosses a floor at season 0 under any arm; an arm that does is refused, or a prior position stocks the larders as world-gen content. `body_step` is re-derived here by H-125's own 'season or campaign' test (10 is a delegated pick). The exit records the arms read, the count of eaters fed from a larder above their own settlement (A2-26's exposure, a reading), and the strict-top share at CR-17's τ (a reading only)." The owner is "`engine/season/rosters.yaml: subsistence_weight.weights`; H-11's row gains the chosen arm and the rule". With `07_SE_ground_and_granaries.md` §4 (f)'s clause (B12a's author routed it here with CR-22), copied: "its arms run under `ground` with `granary_seasons` at the shipped value, and its exit records the band spread across settlements". The arms are read with `hunger_loss` and `famine_loss` at their shipped values (B12b.35's note "`body_step` is re-read at CR-22 under it" is for the `per_head` arm, which stays B98's dial). The story-telling reading, copied: "per season, the `shortfall:<kind>` observations at settlement rungs … and the executed counts of `transfer`, `requisition`, `petition` and `migrate` by persons at or governing the shortfall rung; a reading, not a pass condition (V2). If shortfall occurs and none of the four executes, THAT, and only that, opens a position."
- WHERE: `engine/season/rosters.yaml` (`subsistence_weight.weights`) or `engine/season/data/fixtures.py` (`subsistence_weight`) as the tree holds it `[the producer opens both]`; `engine/season/data/fixtures.py` (`body_step`, if re-derived); `engine/season/hole_register.yaml` (H-11, H-125); `engine/season/requirements.yaml` (R-04's settlement-row `measure:`, per the card) — read at the item's open: `IS-A-01` (B02) restructured `measure:` into conjuncts, and a key it removed is not written (the pilots' rule; written in the commit body).
- TESTS: in `test_hunger.py`: the exit as `test_shipped_arm_reads_below_fed_after_season_one` (two seasons, seeds 0–2, asserting it checked three) and `test_dropping_the_per_head_term_reads_fed_everywhere` (the planted failure: "`want = Person.weight` (per-head term dropped) and every band reads `fed`"), and the season-0 check `test_floor_check_refuses_the_x20_arm` ("at `body_step` 10 the ×20 arm costs every cohort 1,200 body at season 0, so the floor check must refuse ×20 (the check reds if it admits it)") `[ASSUMPTION: test names]`.
- FALSIFIER and CONTROL: copied: "at the shipped arm `hunger_by_settlement` reads a band below `fed` after season 1; planted failure: `want = Person.weight` … every band reads `fed`." "CONTROL: ×1 reproduces the base hash."
- GATE: `python -m pytest engine/season/tests/test_hunger.py -q` → pass; the arms' table (×1, ×5, ×20, and ×10 if bisected) at seeds 0–2, two seasons, in the commit body; `python -m engine.season.harness.register --check` → exit 0.
- HASH MOVERS: "declared MOVER (every realm-seeded pin, the `BASE_EVENTS` files, `results.json`)". B12b's re-pin.
- DEPENDS ON: V12 B12b.01, B12b.36, B12b.37, B12b.43; V12 Batch B12a (CP-T08-02, the endowment); EXISTS-IN-TREE REM-50's census line `hunger_by_settlement`, `world_q.hunger`.
- GLOSSARY: none.
- COST and TIER: calibration; `sonnet` runs the arms; "an independent third-tier (judgment) critic judges the selected arm" (`opus`).
- LANDS IT: B12b's producer; `Item: B12b.44`, `[skip ci]`.

### B12b.45 — the Tensions receiver: registry, loader, roster, yield scale, build switch · CL-EVENTS commit (3) · BUILD · HASH EQUAL
- SOURCE: carry-forward `master/eval/E1.md` "### CL-EVENTS", sub-entry "CL-EVENTS commit (3) — the Tensions receiver" (order "→ CR-22 → CL-EVENTS (3) → CL-EVENTS (4)"); routed with CL-EVENTS (E-8).
- ADVANCES: none of the nine; something happens without the player at world generation (the second decision round, item 2).
- INSTRUCTION: the sub-entry's CHANGES, copied (E-12: the ladder and the struck-key reasoning are cited, not retyped): "`engine/season/tensions.yaml` (a header with the schema and the struck-key list; `tensions: []`); `engine/season/data/tensions.py`, the one loader (card keys checked; `goal` effects parsed together with `goals.yaml`'s rows through `data/goals.py::parse`, so ids, seats and `derives` resolve in one pass and there is one validator; `yield_scale` territory ids resolved by `data/geography.py`; effect kinds from the roster); `rosters.yaml: tension_effects: [goal, yield_scale]`, a closed two-member roster, with a note defining 'tension' (`CLAUDE.md` §4); `data/files.py: TENSIONS_YAML`; `data/fixtures.py: territory_yield_scale = ()`; `queries/world_q.py::season_factor_of` multiplies by its rung's territory scale on every return path (an absent territory reads 1.0); `harness/populated.py::build_realm(tensions: bool = False)`: `tensions=True` draws one card, equally likely, with `ids.draw_factory(world_seed, lambda: 0)("world", "tension")`, and each `choose_one` list with the same factory keyed on the card id and the list's index; the goal rows go to the existing `seed_goals`, the scales into a new `Fixtures` value by `.sweep` (a new value, never a mutation of the shared default). A card is a world-generation draw: read once at build, by no step of the season loop; no new World field … May not be data (M20's line applied to a card): a date, a deadline, a firing condition, an outcome, a write to standing, a seat, a tenure or a stance, and a `closing`, `successor` or `deal` key; the loader refuses every key outside the schema and names these."
- WHERE: NEW `engine/season/tensions.yaml`; NEW `engine/season/data/tensions.py`; `engine/season/rosters.yaml` (`tension_effects`); `engine/season/data/files.py` (`TENSIONS_YAML`); `engine/season/data/fixtures.py` (`territory_yield_scale`); `engine/season/queries/world_q.py` (`season_factor_of`); `engine/season/boot/realm.py` (`build_realm(tensions=False)`); NEW `engine/season/tests/test_tensions.py`.
- TESTS: the sub-entry's FALSIFIER, copied, in the new file, written first: "planted rows the loader must refuse, each by its own message: (i) a card with a `fires_at` key; (ii) an effect kind outside the roster; (iii) a `goal` row `data/goals.py::parse` rejects, refused with goals' own law string (one validator); (iv) a goal id colliding with `goals.yaml`. With a planted one-card test registry and the switch on, seeds 0-5: the same seed twice draws the same card and alternat[es] …; the card's Propositions are minted and at least one person commits to each (the count checked asserted ≥ 1 per goal row); a scaled territory's factor equals base × scale, an unscaled territory's equals base."
- FALSIFIER and CONTROL: the four refusals above. "CONTROL: switch off reproduces the base hash (`build_realm(0).content_hash()`; `aperture 1 s`, s = 0-2); switch on with a card whose lists are empty reproduces it."
- GATE: "`python -m pytest engine/season/tests/test_tensions.py -q` (new) and `engine/season/tests/test_season_weather.py`" → pass; `GO-09's registries exporter, as B03g landed it, with `--check` → exit 0 (the card's PORT line: "`engine/season/tensions.yaml` is named in `data/files.py`, so GO-09's registries export carries it with `--check`") `[ASSUMPTION: the exporter's path — no `tools/export_registries*` is in the tree at `aa31fd2`; the producer reads B03g's GO-09 item for it]`.
- HASH MOVERS: none ("HASH: EQUAL (switch off, empty registry, empty scale)").
- DEPENDS ON: V12 B12b.44 (order only: "the commits follow it for the reading only"); EXISTS-IN-TREE `data/goals.py::parse`, `seed_goals`, `ids.draw_factory`; V12 Batch B03c (`boot/realm.py`), Batch B03g (GO-09's export).
- NAMES: `harness/populated.py::build_realm` → `boot/realm.py::build_realm` (B03c).
- GLOSSARY: new row *tension*: "a strain drawn at the world's making that sets some people's aims, as a tension in a household is there before anyone acts on it"; owner `rosters.yaml: tension_effects`' note.
- COST and TIER: small build; `sonnet`, `high` ("BUILDER: `CLAUDE.md` §10's second tier for (1) to (3)").
- LANDS IT: B12b's producer; `Item: B12b.45`, `[skip ci]`.

### B12b.46 — the six Tensions cards as `[ASSUMPTION]` rows · CL-EVENTS commit (4) · CONTENT · HASH EQUAL
- SOURCE: carry-forward `master/eval/E1.md` "### CL-EVENTS", sub-entry "CL-EVENTS commit (4) — the six Tensions cards as `[ASSUMPTION]` data, and the on-arm reading (WR)"; D-19 (authored values drafted and ratified at the batch's merge).
- ADVANCES: none of the nine; per-seed variety of the opening (cards 1 and 2).
- INSTRUCTION: the sub-entry, copied in its essentials: "the six cards of the archived 6-card fuse deck (`conflict_architecture_proposal.md:127-146`, archived, intent; draw one at game start) as rows of `tensions.yaml`, each `source:` quoting the archived line and carrying `[ASSUMPTION; medium; Jordan to correct; revert: <row>]`; no code. Per card: (1) **Royal Crisis**: a goal row, object `seat_holders` of one royal seat by a keyed `choose_one` among `off_king`, `off_widow_regent`, `off_heir`, stance −1, on a plotting organisation by a second `choose_one` among Varfell, Restoration Movement and Hafenmark … (2) **Feldmark Famine**: `yield_scale` 0.75 on the Feldmark territory rung for the world's life `[revert: 1.0]` … (3) **Cardinal Independence**: a seat goal on one Cardinal seat with object `{kind: rung, rung: set_s_001}`; attention only … (4) **Guild Fracture**: a goal row on the Guild seat (`off_guild_comptroller`) with object `rung` `set_s_018` (Gransol) … (5) **Einhir Incident**: a seat goal on `off_restoration_leader` with object `rung` T4 and T13; no stance … (6) **Ministry Crisis**: a goal row on a Church seat with object `seat_holders` of the `Ministries` seats (one: `off_parliamentary_clerk`), stance −1." The full per-card text is the sub-entry's (cited, E-12). The ids are read at the open (the cast and seats as B10, BA1 and B21 leave them); a named seat absent is refused at seeding (the falsifier).
- WHERE: `engine/season/tensions.yaml` (six rows).
- TESTS: in `test_tensions.py`: the sub-entry's falsifier, at two seasons (four in the source; A-114): "switch on, seeds 0-5 × four seasons: every drawn card loads and seeds; for each seed at least one person committed to the drawn card's goal forms a candidate whose referent is that goal's object (the count checked asserted ≥ 1 per seed, so a vacuous loop fails). Planted failure: a card whose `seat_holders` object names a seat absent from `offices.yaml` is refused at seeding, naming the row; a built but vacant seat seeds a goal with no stance row."
- FALSIFIER and CONTROL: as TESTS. "CONTROL: switch off reproduces commit (3)'s hash."
- GATE: `python -m pytest engine/season/tests/test_tensions.py -q` → pass; realm hash (switch off) at seed 0, one season → equal to B12b.45's reading. The READING ("STORY-BAR on against off, seeds 0-2 … the on-arm's CI and Turmoil readings by CR-90's arc instrument") is taken at two seasons where its instruments exist at this tree (CR-90 is Batch B21d, later: that arm is not read here) and quoted in the commit body, "not a pass condition".
- HASH MOVERS: none ("HASH: EQUAL (switch off)").
- DEPENDS ON: V12 B12b.45.
- GLOSSARY: none.
- COST and TIER: content; `opus` drafts (the card's "third tier for (4)"), `sonnet` lands; the PR body lists "CONTENT THAT IS JORDAN'S": "the Royal Crisis plotters and targets; the Feldmark yield value (0.75 assumed); which Cardinal; whether to keep card 6; the pursuit weights".
- LANDS IT: B12b's producer; `Item: B12b.46`, `[skip ci]`.

### B12b.47 — the supply arm flipped on, with the ration's kinds · IN-52, DEF-7, `U5d_SE_owed_edits` §4 · BUILD · HASH MOVER(behaviour)
- SOURCE: the intake `:320` (IN-52 · rows E1:124, E2:103, E3:357, E4:476 · settled "`U5d_SE_owed_edits.md:61` keeps 'plan IN-52's flip entry'; three lanes carry it") and `:325` (DEF-7 · "with IN-52"); carry-forward `master/eval/E1.md` "### IN-52" (entry `workplans/valoria_master_workplan_v11_part4.md:748-760`), `master/eval/E2.md:103` ("B12-world-motion-and-ground, last item, after `07_SE_treasury_granary_B` and `16_PESSIMIST_SE_B` R4"), `master/eval/E4.md` "### DEF-7"; `proposals/U5d_SE_owed_edits.md` §4 ("Lands inside plan IN-52's flip entry"); routed here by B12a's author (E-8). The lane's target "B22 after `07_SE_campaign_supply_and_muster`" is not taken: E2 and U5d §4 put it here and no step of the flip reads the muster (UNDECIDED (9)). Closes IN-52's flip (its retirement stays HELD on M3), DEF-7, U5d §4; B12b.31 points here.
- ADVANCES: none of the nine; a side's fielded troops are bounded by its levied treasury.
- INSTRUCTION: (1) `U5d_SE_owed_edits` §4, copied: "`engine/season/data/fixtures.py`: `field_ration_kinds`, shipped `["grain"]`; `modules/…/provision` bounds a field by a kind only if the fixture lists it and `subsistence_weight` weights it." (2) IN-52, copied: "flip `field_provisioning` ON, in its own commit; moves no pinned hash while the realm fights no field (H-241); the decisions owed at the flip are H-241's `default:`" — "ration min over kinds, casualties on all losers, defender debit" (LF-1..3, delegated-ruled, `[ASSUMPTION; medium; Jordan to correct]`). "If CR-23 reverts (`stock_report = off`), the flip re-holds." (3) DEF-7, copied: "LF-1 (troops bounded by treasury) vs Jordan's 2026-10-16 wording … LF-1 DELEGATED-RULED (P5 J.2 ask-then, IN-52), tagged revertible" — the flip's commit body names LF-1 as revertible. B12b.24's construction refusal must pass on the shipped realm (B12a's seat-rung stock): if it refuses, the flip is not made and the item stops (`STOPPED`, the refusal's message quoted).
- WHERE: `engine/season/data/fixtures.py` (`field_ration_kinds`; `field_provisioning` default); `modules/settlements/provision.py` (`provision`'s kind bound); `engine/season/hole_register.yaml` (H-241's `default:`).
- TESTS: "the new refusal test `test_field_provisioning_refused_on_empty_treasuries`" (B12b.24) green; `test_grain_only_treasury_fields_troops` (U5d §4's gate) and `test_empty_treasury_side_fields_fewer_than_a_full_one` (IN-52's falsifier) in `test_hunger.py` `[ASSUMPTION: test names and file]`, written first.
- FALSIFIER and CONTROL: copied: "on, a side with an empty treasury fields as many troops as a full one -> the bound is not built"; U5d §4: "it fields nobody". EXIT: "with it on, in a seeded season a side's fielded troops are bounded by its levied treasury". Control: off reproduces B12b.46's hash.
- GATE: `python -m pytest engine/season/tests/test_hunger.py -q` → pass; `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 2 0` (seeds 1, 2) → construction passes; hash moved only if a field is fought (the commit body says which seeds fought one).
- HASH MOVERS: "moves no pinned hash while the realm fights no field (H-241)"; declared MOVER for every seeded world that fights one. B12b's re-pin.
- DEPENDS ON: V12 B12b.24; V12 Batch B12a (`07_SE_treasury_granary_B`'s seat-rung stock); EXISTS-IN-TREE `field_provisioning` (`data/fixtures.py`, shipped `False`), `modules/settlements/provision.py`, CR-23's `requisition` (H-163 limit 3(a) for this flip: "MET at its close").
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high` (E2: "second tier").
- LANDS IT: B12b's producer; `Item: B12b.47`, `[skip ci]`.

## Readings (B12b)

- **R1 (B12b.06), `09_WR_B_weather_with_memory_and_the_year.md` edit 2, copied:** "Not a table edit. The live arm's four `season_band_factors` are swept, and the reading recorded at three seeds over eight seasons is the realm's mean harvest factor under the arm against the control's; the calibration target is a mean of one (a forcing moves variance, not the long-run harvest). The former change of `((0.5, 1.0, 2.0),) * 4` to `((0.5, 1.0, 1.5),) * 4` is withdrawn with the multiplier form. `[ASSUMPTION; medium; Jordan to correct]` for the factors." Taken in B12b.43's commit at two seasons (eight in the source; A-114), seeds 0–2: the mean harvest factor per seed under three candidate factor sets against the control's seed-to-seed spread; B12b.43 ships the chosen set, and the close quotes the table again with its tree. Edit 2's falsifier, read there: "the recorded mean harvest factor under the chosen band factors departs from one by more than the control's own seed-to-seed spread, and the factors are nevertheless shipped".
- **R2 (B12b.34), `U5d_SE_owed_edits.md` §5, copied:** "No edit: the ruled ladder stands (the realm rung feeds every town beneath it; the Church's and Schoenland's ladders differ by the containment the world builds). Recorded so the consequence is read when `07_SE_treasury_granary_B.md` lands: its gate adds one reading, the stock drawn from `r_valoria` by settlements of each duchy per season, so a king's withholding (moving stock off the realm rung) is visible as an act with a trail." `07_SE_treasury_granary_B` landed in B12a without it, so it is read at this close: `build_realm(0)`, two seasons, the stock drawn from `r_valoria` per season grouped by the drawing settlement's duchy, from `subsistence_draw`'s cells whose `src` is `r_valoria` `[ASSUMPTION: the instrument — a short script over `subsistence_draw`, no new tool]`.

### B12b.99 — re-pin and close readings · `V12_STRUCTURE_part4.md` E-1 · BUILD · HASH MOVER (the re-pin)
- SOURCE: `V12_STRUCTURE_part4.md` E-1, E-2; `V12_STRUCTURE_part2.md` §5.9, §5.12.
- INSTRUCTION: re-record, once, every realm and corpus pin a B12b item moved (the batch head's RE-PIN line, `workplan_v12_part24.md`) in `engine/season/tests/_realm_goldens.py` against B12a's close (`reading @<sha>`); quote seeds 0–2, one and two seasons; take R1 and R2; the commit says "re-pin" and lists the movers. A pin only one item moved in its own test file stayed in that item's commit (E-1).
- GATE: the BATCH GATE above, once, on this commit's tree, with the one full-suite run CLAUDE.md §0.4 allows at the close.
- LANDS IT: B12b's producer; `Item: B12b.99` — the batch's last `Item:` commit, pushed without `[skip ci]`.

| STOP. Batch B12b-weather-arcs-population closes here |

---

## Batch B19a-mb-contact-instrument · lane MB · wave W14 · step S14 · HASH EQUAL
INVOCATION: /methodology-execute Batch B19a-mb-contact-instrument
IN-FLIGHT ROW: registers/handoffs/HANDOFF_MB.md, Open table
GATE: Batch B00-ids
GATE: Batch B01-laneA
GATE: Batch B02-tests
GATE: Batch B16M-mb-engine-words
GATE: Batch B14-pc-outcome
GATE: Batch B15-pc-calibration
GATE: Batch B16-pc-round
GATE: Batch B17-mb-scale
REQUIREMENT: none — the measured table B19's contact draw reads (A-100); nothing in a field reads it yet (`V12_STRUCTURE.md` §2.2: "none of its own (the table B19 reads)"); the close reads the nine lines and writes no `reading:` record
UNDECIDED:
  (1) MBA-02 step 2 loads the duel "through `engine/substrate/pc_engine.py` (`pc_engine.load()`)"; B13 (`CI-09`) deletes that seam before this batch. Taken as D-09 decides: `from modules.combat import wrapper, combatant` (a tool under `tools/`, not the engine), and each duel read per round through B16's `modules/combat/fight.py::fight_round` (PCR-2), not the trace events the pilot read.
  (2) MBA's handles in its own text (`Item: MBA-01`) are replaced by the plan's (`Item: B19a.01`); the source handle is in each title (`V12_STRUCTURE_part2.md` §5.3).
  (3) U3 §5.1 lists `tools/export_troops.py` and `modules/mass_battle/troop_types/table.py` as B17's creations; neither is in the tree at `aa31fd2` (`ls`), so every DEPENDS ON naming them reads `V12 Batch B17`.
BATCH GATE (read once, on the closing tree; `PYTHONHASHSEED=0`):
  `python tools/calibrate_mb_contact.py --trust` → seven `ok` lines; `python tools/calibrate_mb_contact.py --spot 20` → twenty `inside` lines;
  `python tools/export_mb_contact.py --check` → exit 0; `python tools/export_troops.py --check` → exit 0;
  `python -m pytest tests/valoria/test_export_troops.py tests/valoria/test_export_mb_contact.py -q` → all pass;
  `python tools/ci_golden_modes_check.py` → every digest equal to B17's close (`reading @<B17 closing sha>`); the realm hash at seeds 0–2 after one season equal to the step's base (`reading @<sha>`): nothing in a field or a season reads the table;
  `python -m engine.season.harness.register --check` → exit 0; `--requirements` → nine lines; `python tools/m1_acceptance.py --summary` → its verdict line, quoted;
  the glossary rows B19a.01–.03 name (MBA §8.3: *felling chance*, *exposure*, *matchup row*, *range band*, *power* retired for *skill*), read against the code;
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (`-m mass_battle` plus the tool tests: the batch touches `modules/mass_battle/`, `tools/` and registries);
  the close's commit body records `register --requirements`, `m1_acceptance --summary`'s verdict line, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`) and after, the full run's wall time and worker count, and the batch's measured wall time; `status:` is not edited (`IS-A-12`).
RE-PIN: none (B19a.99 records the EQUAL reading)
IDS: ED-MB 0; H 0
DIALS AT CONTROL: none set later by B98 (the `contact`, `missile` and matchup values ship `status: seed` and are read and set by MBA-08 in B19, that batch's own calibration; `matchups: []` is filled by B19's ★ rows and B31's)
C(B19a-mb-contact-instrument): this batch's entries; the plan's head parts; `master/mb_abstraction/MBA_DESIGN.md` §1.3, §1.4, §1.7, §2.1–§2.5 and `MBA_DESIGN_part2.md` §3.1, §3.2, §5.1, §5.2 (read whole for B19a.01–.03: the seeds, the grid, the schema, the trust checks);
  `references/troops.yaml`; `tools/export_troops.py`; `engine/engine_params/troops.json`; `modules/mass_battle/troop_types/table.py`, `registry.py`; `tests/valoria/test_export_troops.py`; `references/ci_checks_registry.yaml`; `tools/valoria_local.py`;
  read only: `modules/combat/fight.py` (`fight_round`), `modules/combat/vocabulary.py` (`ROUND_ENDS`), `wrapper.py`, `combatant.py`, `attributes.py`, `core.py`, `engine/engine_params/combat_engine_v1.json`, `systems/combat/combat_engine_v1/workbench/balance.py` (`winrate`), `systems/combat/combat_engine_v1/workbench/calibrate_generics.py` (the instrument precedent), `tools/export_battle_orders.py` (the exporter pattern), `tools/ci_golden_modes_check.py`;
  the closing SHAs of B14, B15, B16, B16M, B17; the permanent surface (CLAUDE.md, `CURRENT.md`, `HANDOFF.md`, `registers/handoffs/HANDOFF_MB.md`, the skill and `methodology-close`).
SERIAL EDGES: B19a.01 → B19a.02 (the instrument's grid is read from the troop file's new columns) → B19a.03 (the exporter builds from the measured table) → B19a.99.
  With other batches, by file (U3 §5.1, `→` is landing order): `references/troops.yaml`, `tools/export_troops.py`, `modules/mass_battle/troop_types/table.py`: B17 → B19a → B19 → B31 (and `troops.yaml` → B20 → B22 → B30); `references/ci_checks_registry.yaml`, `tools/valoria_local.py`, `tools/calibrate_mb_contact.py`, `tools/export_mb_contact.py`, `engine/engine_params/mb_contact.json`, `references/mb_contact/duel_grid.json`, `modules/mass_battle/core/contact_table.py`: B19a → B19; `modules/combat/*.py`: read only here (B13 → B14 → B15 → B16 edit them; the fingerprint makes a later edit refuse at `--check`).
PARALLEL: S14 with B12b (SE+WR), B21c (FA), B29 (PC), B34 (GO). No file shared with B12b or B29 (their WHERE lines: `engine/season/`, `modules/settlements/`, `modules/mass_battle/terrain.py` for B12b.02 — not edited here); `references/ci_checks_registry.yaml` with any sibling that adds a row: different rows, kept by hand at merge (§7.3). Hash EQUAL: merges at any position (§7.4). PC review is a read of B19a.02's use of the duel, not a PC batch.
BACKGROUND RUN: B19a.02's first full run, sized on two small runs (§2.2's estimate: about 7.7 core-hours, about 2 hours on four workers [estimate]), launched in the background at the batch's open after B19a.01 lands (`STAGES.md` efficiency rule 5; the skill, "Running a slow instrument"), read at B19a.02's gate; its wall time and worker count go in that commit body and replace the estimate.
COST: small builds and one instrument run; producer `valoria-author` on `sonnet`, `high`; the run `haiku`-supervised in the background; a `--trust` failure read by `opus` (is it the duel or the instrument); the close's one `opus` critique reads B19a.02's `--trust` output and B19a.03's gate (MBA-03 "Lands it").
EST: 6 h of agent time [estimate: §2.4's formula over four positions (0.4 h × 4 + 2.5 h) + 2 h for the instrument] plus the background run's wall time (about 2 h on four workers, MBA §2.2 [estimate])

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B19a.01 | the troop file carries the contact's data | MBA-01 | BUILD | EQUAL | Batch B17, Batch B14 |
| B19a.02 | the calibration instrument, melee cells, and its first full run | MBA-02 stage 1 (the duel loaded as D-09) | BUILD | EQUAL | B19a.01; Batch B15, Batch B16 |
| B19a.03 | the exporter, its blocking `--check`, the module's reader | MBA-03 | BUILD | EQUAL | B19a.02 |
| B19a.99 | the EQUAL reading and close readings | E-1 | BUILD | EQUAL (records it) | B19a.03 |

Not in this batch, and where each is: MBA-02 stage 2 (`--missile`) and MBA-09 (B31, behind J-MBA-01); MBA-04 to MBA-06 and MBA-08 (B19); MBA-07 (B30); the ★ matchup rows (B19) and the other 25 (B31).

### B19a.01 — the troop file carries the contact's data · MBA-01 · BUILD · HASH EQUAL
- SOURCE: `master/mb_abstraction/MBA_DESIGN_part3.md` §7.1 "Item: MBA-01"; `MBA_DESIGN.md` §1.3, §1.4 (the seeds), §1.7 (`power` → `skill`), §2.1 (the duel keys); `MBA_DESIGN_part2.md` §3.1 (the missile seeds), §3.2 (the matchup schema and its closed sets); rulings A-100, A-59 (2), A-98 (3), A-113.
- ADVANCES: none of the nine; A-100 (the data the contact draw reads).
- INSTRUCTION (in order; copied):
  1. "`references/troops.yaml: arms.<key>`: add `duel_key` (a key of personal combat's weapon export, or null) and `duel_key_status: exact | proxy | none`. Seeds: `light_cut: arming exact`, `heavy_cut: falchion proxy`, `heavy_blunt: mace exact`, `spear: spear exact`, `arming: arming exact`, `pike: spear proxy`, every missile arm `null none` with `sidearm: dagger`. [ASSUMPTION: these five — basis: nearest duel weapon by kind; content for Jordan's pass.]"
  2. "`troops.<type>`: rename the column `power` to `skill` (the men's martial skill on the duel's `faculty` scale, §1.7), values unchanged. Every reader of `power` in `modules/mass_battle/` reads it through `stats_for` (`troop_types/registry.py`) after B17's loader; the loader returns both keys during this batch (`power` an alias), and MBA-04 deletes the alias when the last pool reader goes." §1.7's transcription: "levy 1, archers 3, heavy infantry 4, cavalry and templars 5" (one for one).
  3. "A header block `contact:` with `exposure: {base, posture_k, cover: {walls}}`, `levels: {intent_offense, intent_defense, terrain_die, charge_cap, morale_near_rout}` and `K: 6`, each value with `status: seed` and its source constant named in a comment (§1.3, §1.4 give the seeds); `missile: {bands: [0.25, 0.5], hit: {...}, shots_per_tick: {...}, felling_per_hit: {...}, profile: {foot: 1.0, mounted: 1.6}}`, all `status: seed`." The seeds, copied from §1.3 and §1.4: `levels.intent_offense` 0.5 (`INTENT_OFFENSE_D`), `intent_defense` 1.0 (`INTENT_DEFENSE_D`), `terrain_die` 1 step a die, `charge_cap` 2.75 (`MB_CHARGE_SIGMA` 0.55 at its cap), `morale_near_rout` 4 (`MORALE_SIGMA_SCALE` 0.8), each "transcribed … by the tree's own conversion, `SIGMA_PER_D = 0.2`"; `exposure.posture_k` 0.5 (the factor `1 + 0.5 x (cA + cB)`, floor 0.25); `exposure.cover.walls` 0.5 (from `WALLS_DEFENDER_DR = 3`); `exposure.base`: "**Uncalibrated in absolute level**: set in B19" — shipped `null` with `status: seed` and the comment naming T-1, T-2 and Sabin's bound `[ASSUMPTION: null rather than a number — basis: §1.4 gives no seed; the loader admits `null` only for `base`]`. The missile seeds, copied from §3.1: `shots_per_tick` "bow 0.67, crossbow 0.13"; `hit` "decreases from close to long [seeds, ordering only]"; `felling_per_hit` "a **seed table** ordered by the canonical ranged armour table (none 0, light 1, medium 2, heavy 3 vs piercing): strictly decreasing with the tier, the crossbow's `armour_piercing` keyword raising medium and heavy; magnitudes **uncalibrated** and flagged" — the numbers the producer writes for `hit` and `felling_per_hit` are `[ASSUMPTION; content for Jordan]`, ordering as stated, listed in the PR body.
  4. "`matchups: []`, shipped empty, with the loader's schema (§3.2)": rows `{a, d, situation, closes, close_ob, first_tick: {exposure_a, exposure_d, levels_a, levels_d}, stand, status}`; classes `foot_short`, `foot_pole`, `foot_pike`, `foot_missile`, `crew`, `horse_shock`, `horse_light`, `horse_missile`; situations `charge_front_braced`, `charge_front_unbraced`, `charge_flank_or_rear`, `marching`, `in_cover`, `pursuit`, `skirmish`; `closes` in `closes | draw | evades | refused`; `status` in `seed | calibrated | derived`.
  5. "`modules/mass_battle/troop_types/table.py` (the loader B17 creates): reads the new columns; refuses, naming the row: an arm with neither `duel_key` nor `sidearm`; a `duel_key_status` outside its closed set; a `contact`/`missile` value with no `status`; a matchup row naming a class or situation outside the closed sets (§3.2's eight classes, seven situations) or a `closes` outside `closes | draw | evades | refused`. `tools/export_troops.py` carries the new columns into `engine/engine_params/troops.json`." Re-derive the artifact with the tool, never by hand.
- WHERE: `references/troops.yaml`; `tools/export_troops.py`; `engine/engine_params/troops.json` (re-derived); `modules/mass_battle/troop_types/table.py`; `tests/valoria/test_export_troops.py`; `unified/U1_GLOSSARY.md` (rows *exposure*, *matchup row*, *range band*; *power* retired for *skill*).
- TESTS: in `tests/valoria/test_export_troops.py`, written first and read red: "`test_every_arm_has_a_duel_key_or_a_sidearm`, `test_an_unstatused_contact_value_is_refused`, `test_a_matchup_row_outside_the_closed_sets_is_refused`".
- FALSIFIER and CONTROL: "a seeded field moves at this item (it must not: nothing reads the new columns); control: `tools/ci_golden_modes_check.py`'s digests before and after."
- GATE: "`python tools/export_troops.py --check` exits 0; `python -m pytest tests/valoria/test_export_troops.py -q` … `python tools/ci_golden_modes_check.py` digests unchanged."
- HASH MOVERS: none.
- DEPENDS ON: V12 Batch B17 (`references/troops.yaml`, `tools/export_troops.py`, `troop_types/table.py`: `04_MB_unit_loadout_and_weapon_in_hand_B` stages 1–2); EXISTS-IN-TREE `engine/engine_params/combat_engine_v1.json`; V12 Batch B14 (`03_PC_weapon_records_in_the_export`: its weapon records); EXISTS-IN-TREE `modules/mass_battle/troop_types/registry.py` (`stats_for`).
- NAMES: B16M (L2) and B16L (L1) renames apply to any army or unit identifier the loader touches (`Subunit` → `Unit`, `subformations` → `units`); none is named in MBA-01's text.
- GLOSSARY: MBA §8.3, in this commit: *exposure* (new, Jordan's word, A-100): "how many duel rounds a front-rank man fights in one field tick"; *matchup row*: "a row of data saying how one class of troops meets another in one situation"; *range band*: "a distance band in which a missile arm hits at a stated rate"; *power* (`MB_LEXICON.md:185`) retired as a troop stat, "skill" (the men's martial skill) replaces it, owner `troops.yaml: troops.<type>.skill`.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B19a's `valoria-author` producer, `isolation: worktree`; `Item: B19a.01`, `[skip ci]`.

### B19a.02 — the calibration instrument, melee cells, and its first full run · MBA-02 stage 1 · BUILD · HASH EQUAL
- SOURCE: `master/mb_abstraction/MBA_DESIGN_part3.md` §7.1 "Item: MBA-02"; `MBA_DESIGN.md` §2.1 (the grid), §2.2 (the stop rule and the cap), §2.3 (the measured table's schema; the instrument's sub-commands), §2.4 (the pilot's readings); `MBA_DESIGN_part2.md` §5.2 (the seven `--trust` checks); rulings A-100, A-101, A-5, A-30; D-09.
- ADVANCES: none of the nine; A-100 (weapon-on-weapon and weapon-on-armour numbers from simulated personal combat).
- INSTRUCTION (copied, steps 1–7; step 6's stage 2 is B31's):
  1. "New `tools/calibrate_mb_contact.py`, module docstring stating its role in one sentence ('runs the duel engine over a grid of matchups and writes the measured felling chances the mass-battle contact draw reads') and the same sentence as its `role:` line in `references/ci_checks_registry.yaml` (CLAUDE.md §4: coinage defined where invoked), with `blocking: false` and `notes: 'an instrument, run by hand at a calibration pass; not a CI check'`."
  2. "Loads the duel engine … never `modules/mass_battle`. The grid is read from `references/troops.yaml` (the fighter types are the distinct `(duel_key, armour, skill)` the troop rows can field, plus the §2.1 grid's levels) so a new troop type needs no edit here." The load is D-09's: `from modules.combat import wrapper, combatant` (UNDECIDED (1)). The grid, copied from §2.1: arms `arming`, `falchion`, `mace`, `spear`, `dagger`; armour `none`, `light`, `medium`, `heavy`; martial skill 1, 3, 5; round index 1 to `K = 6`; "5 x 4 x 3 = 60" fighter types; "60 x 61 / 2 = **1,830 cells**"; "Twelve **interpolation check cells** run skill 2 and 4 against 3 for each arm in light armour"; "Every duel runs with the default attributes of `modules/combat/attributes.py` (`end` 4, `spirit` 3, `strength` 4, `agi` 4, `focus` 3, `att` 3, `disp` 4) except `faculty`, under the lethal terms, through the module's round entry." (`faculty` is the skill score after B15's `IS-PC-05`; NAMES.)
  3. "Per cell: `random.Random(crc32(repr(cell_key)) % 100000)`; duels position-swapped in halves (the `balance.winrate` precedent, `systems/combat/combat_engine_v1/workbench/balance.py`); each duel read **per round from the round entry's typed result** (`master/pc_round/`, A-101 …); accumulate per side `h_k` with Wilson intervals, the damage-taken quantiles, `felled_mortal` when the round result carries a mortal-wound band; the stop rule and the cap of §2.2." The round entry is `modules/combat/fight.py::fight_round` (B16, PCR-2) and the round's end kinds `modules/combat/vocabulary.py::ROUND_ENDS`. §2.2, copied: "A cell stops when, for each side, the Wilson 95% half-width of `h_1`, `h_2` and `h_3` is at most `max(0.10 x h, 0.002)`, and never before **2,000 duels**." "**The cap: 20,000 duels.** A cell that reaches it is stored with its measured half-width and the flag `precision: absolute`; a side with no felling in 20,000 rounds is stored as the Wilson upper bound with `below_resolution: true`, never as 0 (the standing rule: no certain matchup)." "**The rounds `k >= 4`** are read where at least 400 duels reached round `k`; otherwise `h_k` carries forward the last estimated index and is flagged `carried`." The table's schema is §2.3's JSON (`schema`, `engine_fingerprint`, `round_source`, `terms`, `K`, `seed_rule`, `cells[]` with `a`, `b`, `duels`, `outcome`, `sides.{a,b}.{h, h_lo, h_hi, rounds_at_k, flags, damage, felled_mortal}`), cited (E-12).
  4. "Sub-commands: `run OUT [--workers W] [--cells F]`; `--cell KEY N`; `--spot M` (re-run M cells chosen as every `len/M`-th in key order, each `h_1` inside its stored interval); `--trust` (§5.2's seven checks, stop on the first failure, print which)." §5.2, copied: "1. **Fingerprint** recorded and equal to the tree's … 2. **Symmetry**: five mirror cells (one per arm, light armour, skill 3): each side's `h_1` inside the other's interval and win shares within 3 standard errors. 3. **Swap**: two asymmetric cells run both ways agree within their intervals. 4. **Reproducibility**: one cell twice at one seed, byte-identical. 5. **No certainty**: no cell's outcome share is 0 or 1 at its `n` …; a cell at 0 or 1 stops the run and is reported to the PC lane, not stored. 6. **Rounds run**: the mirror's mean rounds a duel is at least 2 … 7. **Round boundary**: the count of rounds the instrument reads equals the round entry's own count (`master/pc_round/`), for 100 duels."
  5. "`--workers` uses `multiprocessing` with one RNG per cell (no shared stream), so the table does not depend on the worker count."
  6. "**Stage 1 (B19a):** melee cells only."
  7. "The first full run is made in this batch, launched in the background at the batch's start … after two small runs size it; the measured table `references/mb_contact/duel_grid.json` is committed with the run's wall time, worker count and the `--trust` and `--spot 20` readings in the commit body (the time replaces §2.2's estimate)."
- WHERE: NEW `tools/calibrate_mb_contact.py`; NEW `references/mb_contact/duel_grid.json`; `references/ci_checks_registry.yaml` (one row, `blocking: false`).
- TESTS: none new in this item (the instrument's own checks are `--trust`; its exporter's tests are B19a.03's); the background run is launched by the skill's "Running a slow instrument" steps 1–5 (`exec python -u … > log 2>&1`, a pid file, an `EXIT 0` line).
- FALSIFIER and CONTROL: "a measured table whose mirror cells disagree beyond their intervals (the instrument is biased by position); a table that differs when `--workers` changes. Controls: the mirror cells; `--workers 1` against `--workers 4` on 10 cells, byte-identical."
- GATE: "`python tools/calibrate_mb_contact.py --trust` prints seven `ok` lines; `--spot 20` prints 20 `inside` lines; `--cell` on one pilot cell (`spear light 3 / arming light 3`) reproduces its stored row. Expected readings, from the pilot on today's engine (B15 will move them; the reading at B19a is the one recorded): mirror win shares within 0.03 of each other; mean rounds a mirror duel at least 2."
- HASH MOVERS: none.
- DEPENDS ON: V12 B19a.01; V12 Batch B14, B15, B16 (MBA §5.1: the weapon records the fingerprint hashes; every B15 change that "moves `h_k`"; `fight_round`); V12 Batch B13 (the import path, D-09); EXISTS-IN-TREE `systems/combat/combat_engine_v1/workbench/balance.py::winrate`, `modules/combat/attributes.py`.
- NAMES: `pc_engine.load()` → `from modules.combat import wrapper, combatant` (B13, D-09); the trace events `engagement_end`, `wound` → B16's typed round result (`fight_round`; PCR-3: `engagement_end` → `round_end`); the combat attribute `faculty` → the skill score read through the skill table (B15, `IS-PC-05`).
- GLOSSARY: *felling chance* (MBA §8.3): "the chance one man is put out of the fight in one duel round against one opponent"; rejected: "hazard", "lethality"; owner `mb_contact.json` (B19a.03); *duel round* unchanged (A-101).
- COST and TIER: small build `sonnet`, `high`; "the run `haiku`-supervised in the background; a `--trust` failure is read by `opus` (a judgment: is it the duel or the instrument)".
- LANDS IT: B19a's producer; `Item: B19a.02`, `[skip ci]` (the table committed with the run's readings in the body).

### B19a.03 — the exporter, its blocking `--check`, the module's reader · MBA-03 · BUILD · HASH EQUAL
- SOURCE: `master/mb_abstraction/MBA_DESIGN_part3.md` §7.1 "Item: MBA-03"; `MBA_DESIGN.md` §2.3 (the typed artifact; the `--check`'s three arms), §2.5 (the interpolation check); CLAUDE.md §5.
- ADVANCES: none of the nine; CLAUDE.md §5 (a value the engine uses lives in a typed artifact behind an exporter with a blocking `--check`).
- INSTRUCTION (copied):
  1. "New `tools/export_mb_contact.py` on the `tools/export_battle_orders.py` pattern (`build()`, `main(argv)`, `--check` diffs and exits 1): builds `engine/engine_params/mb_contact.json` from `references/mb_contact/duel_grid.json` and `references/troops.yaml` (§2.3: per ordered pair of fighter types, `h[1..K]`, `beta`, flags; the `contact`, `missile` and `matchups` blocks with their status tags)." §2.3: "the slope `beta` (the change in `logit(h_1)` per skill step, measured at that cell from its two skill neighbours) … Interpolation across skill is linear in log-odds".
  2. "`--check` also: (b) recomputes the duel-engine fingerprint (sha256 over `engine/engine_params/combat_engine_v1.json` and the sorted sources of `modules/combat/*.py`) and fails, printing `python tools/calibrate_mb_contact.py run …` as the remedy, when it differs from the table's; (c) refuses an arm whose `duel_key` the table lacks, and any pair of fighter types the troop file can field that has no cell."
  3. "New `modules/mass_battle/core/contact_table.py`: loads `mb_contact.json` once (the `troop_types/table.py` precedent: a data file, no `engine` import, no `modules.combat` import); `felling_chance(arm_a, armour_d, skill_a, skill_d, rounds_d) -> float` (log-odds interpolation on skill and rounds), `beta(...)`, `status(...)`."
  4. "`references/ci_checks_registry.yaml`: a row for the exporter, `blocking: true`, wired in `tools/valoria_local.py --staged` and proposed (not made) for the workflow's season job beside `export_battle_orders.py` (Jordan owns `.github/workflows/`; the registry note at `references/ci_checks_registry.yaml` for `tools/export_battle_orders.py` is the precedent)." The PR body names the proposed workflow line (held back: Jordan's file).
- WHERE: NEW `tools/export_mb_contact.py`; NEW `engine/engine_params/mb_contact.json`; NEW `modules/mass_battle/core/contact_table.py`; `references/ci_checks_registry.yaml`; `tools/valoria_local.py`; NEW `tests/valoria/test_export_mb_contact.py`.
- TESTS: in the new file, each written first and read red (U3 §6.1: "write its six tests first"): "`test_round_trip_is_clean`, `test_a_hand_edit_fails_check`, `test_a_changed_duel_engine_fails_check` (plants one byte in a copy of the fingerprinted sources, asserts exit 1 and the remedy line), `test_a_troop_arm_without_a_cell_is_refused`, `test_mass_battle_imports_no_combat` (subprocess import of `modules.mass_battle.core.contact_table`, asserting no path under `modules/combat` in `sys.modules`' files, the `test_importing_every_engine_module_pulls_in_no_subsystem` form), `test_interpolation_hits_the_check_cells` (§2.5: at most one of twelve outside)". §2.5: "if more than one of the twelve does not, skill 2 and 4 join the grid (cost: 60 to 100 fighter types, about 2.8 times the cells) and the close says so."
- FALSIFIER and CONTROL: "a hand edit of `mb_contact.json` that `--check` passes; a changed `modules/combat/core.py` that `--check` passes. Controls: the committed pair passes."
- GATE: `python -m pytest tests/valoria/test_export_mb_contact.py -q` → six pass; "`python tools/export_mb_contact.py --check` exits 0"; `python tools/valoria_local.py --staged` → the new row runs.
- HASH MOVERS: none.
- DEPENDS ON: V12 B19a.01, B19a.02; EXISTS-IN-TREE `tools/export_battle_orders.py` (the pattern), `tools/valoria_local.py`, `references/ci_checks_registry.yaml` (the `export_battle_orders.py` row); the subprocess-import test form (CLAUDE.md §3's `test_importing_every_engine_module_pulls_in_no_subsystem`).
- GLOSSARY: *felling chance*'s owner set to `engine/engine_params/mb_contact.json` (B19a.02's row).
- COST and TIER: small build; `sonnet`, `high`; "the close's one `opus` critique reads MBA-02's `--trust` output and this gate".
- LANDS IT: B19a's producer; `Item: B19a.03`, `[skip ci]`.

### B19a.99 — the EQUAL reading and close readings · `V12_STRUCTURE_part4.md` E-1 · BUILD · HASH EQUAL
- INSTRUCTION: record the EQUAL reading (golden-mode digests and the realm hash at seeds 0–2 equal to the step's base, `reading @<sha>`), the background run's wall time and worker count, the `--trust` and `--spot 20` readings, and the close's record (§5.12); re-pin nothing.
- GATE: the BATCH GATE above, once, on this commit's tree.
- LANDS IT: B19a's producer; `Item: B19a.99` — the batch's last `Item:` commit, pushed without `[skip ci]`.

| STOP. Batch B19a-mb-contact-instrument closes here |

---

## Batch B29-pc-custody · lane PC · wave W14 · step S14 · HASH MOVER, one re-pin
INVOCATION: /methodology-execute Batch B29-pc-custody
IN-FLIGHT ROW: registers/handoffs/HANDOFF_PC.md, Open table
GATE: Batch B00-ids
GATE: Batch B01-laneA
GATE: Batch B02-tests
GATE: Batch B15-pc-calibration
GATE: Batch B16-pc-round
GATE: Batch B21-fa-governance
REQUIREMENT: `BUILT OUT`: `arrest`, `accept` (`V12_STRUCTURE.md` §2.2; `IS-A-08`'s rule: the `BUILT OUT` line of `python -m engine.season.harness.aperture 2 --seeds 0 1 2` for each verb is in the gate, and a verb not built out at the close is a failed gate) → both built out; it completes two verbs of R-05 (IS-A §12.3 item 2, D-20); no `status:` edited
UNDECIDED:
  (1) A0 (`addressed_records`) lands with A4 in B14 (B14.27, "`14_VERBS_PHYSICAL_A` A0, A4"), though this file's Lands line says "A0–A2 in B29": A4 cannot land without its reader, so B14 carries it; here it is a DEPENDS ON.
  (2) CR-51's card reads "GATE: after CR-49 and CR-47", and both land in B12a/B12c, which B29 does not follow (S14 against B12c's S15). Taken by D-02's precedent (step 4): v11's GATE line is the P13 file serialisation of the verb cluster; CR-51's NEEDS are IN-12 (landed) and CR-50 (SUPERSEDED, the intake §2), so no data edge; the intake §2 places CR-51 (b) at B29's tail. Reading (b): CR-51 (b) moves after B12c.
  (3) A2's residue: "`world_q.mustered` does not read `restrained` today (25 G-32); the conjunct is residue §4, and A2's gate needs it" (`U5b_VERBS_military_physical_residue.md` §4, B22). The arm of A2's gate that reads a mustered prisoner is moved to B22's item (§5.8); the rest of A2's gate is read here.
  (4) The audit names two gate files (`test_v14_arrest_by_addressed_warrant.py`, `test_v14_capture_after_resisted_arrest.py`); the proposal's R4 7b.0 (3) makes them functions of one file, `engine/season/tests/test_vm_phy_a_custody.py` (created by B14.27). The proposal governs.
BATCH GATE (read once, on the closing tree; `PYTHONHASHSEED=0`):
  `python -m pytest engine/season/tests/test_vm_phy_a_custody.py engine/season/tests/test_cr87_violence_contexts.py -q` → all pass;
  `python -m engine.season.harness.aperture 2 --seeds 0 1 2` → `BUILT OUT` for `arrest` and `accept`; `capture` refusals on `exists:Person` and `individual` 0; `accept` refusals on `exists:challenge` 0 (the source's "`aperture 2 0` and `aperture 2 1` before and after, quoted in the commit"), before `reading @<sha>` and after;
  B29.03's reading (CR-51 (b)'s exit) quoted;
  `python -m engine.season.harness.register --check` → exit 0; `--requirements` → nine lines; `python tools/m1_acceptance.py --summary` → its verdict line, quoted;
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (engine core: the full gates);
  the close's commit body records `register --requirements`, `m1_acceptance --summary`'s verdict line, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`) and after, and the batch's measured wall time; `status:` is not edited (`IS-A-12`).
RE-PIN: once, in B29.99: the realm and corpus pins in `engine/season/tests/_realm_goldens.py` that B29.01 and B29.02 move ("every realm and spine pin in which these formations occurred (`capture`'s 26 formations … the arrest stamp's new referents)"), and B29.03's if it builds a link; read against the step's base and, in S14, rebased on B12b's merge (§7.4: B12b precedes B29 in §2.1's order); the commit says "re-pin".
IDS: ED-PC 0; H 0
DIALS AT CONTROL: none
C(B29-pc-custody): this batch's entries; the plan's head parts; `audits/14_VERBS_PHYSICAL.md` §1.7, §2.7 (the gates, read whole); `engine/season/queries/world_q.py` (`addressed_records` from B14.27, `_stamped`, `issuing_seat`, `mustered`); `engine/season/loop/effects_information.py` (`_held_warrants`, `_eff_arrest`, `_eff_seize`, `_may_close_custody`); `engine/season/loop/effects_combat.py` (`_eff_capture`); `engine/season/decision/options.py` (the `WARRANT_SOURCED` block, `warranted`, `violence_context_of`); `engine/season/verb_table.yaml` (rows `arrest`, `capture`); `engine/season/rosters.yaml` (`violence_contexts`); `engine/season/tests/test_vm_phy_a_custody.py`, `test_cr87_violence_contexts.py`; `master/eval/E1.md` "### CR-51" (read whole for B29.03); instruments `aperture`, `register`, `tools/m1_acceptance.py`, `tools/tests_for_diff.py`; the closing SHAs of B14, B15, B16, B21; the permanent surface (CLAUDE.md, `CURRENT.md`, `HANDOFF.md`, `registers/handoffs/HANDOFF_PC.md`, the skill and `methodology-close`).
SERIAL EDGES: B29.01 → B29.02 (`_eff_capture`'s custody reads `warrants_for`, which B29.01 lands) → B29.03 (the re-measure reads `arrest.made` after both) → B29.99.
  With other batches, by file (`→` is landing order): `queries/world_q.py`: B14 (A0, A4) → B21 → B29 → B22 (`mustered`, residue §4); `loop/effects_information.py` B21 → B29; `loop/effects_combat.py` B15 (A3) → B29; `rosters.yaml: violence_contexts` B15 (A3: `fight` drops `duel`, `context_terms`) → B29 (`capture`); `verb_table.yaml` rows `arrest`, `capture`: B29 only; `decision/options.py` B21 → B29.
PARALLEL: S14 with B12b (SE+WR), B19a (MB), B21c (FA), B34 (GO). Hot files shared with B12b: `queries/world_q.py` (different functions: B12b adds `route`, `road_input`, `tally_reached`, `quiet_since`, edits `season_factor_of`, `_larder_parts`, `hunger`, `questions_for`; B29 adds `warrants_for`, `warrants_heard` and edits `_stamped`), `rosters.yaml` and `verb_table.yaml` (different keys and rows), `decision/options.py` (B12b `_operands`; B29 the warrant block): kept by hand at merge in §2.1's order, never regenerated (§7.3). No file shared with B19a. Movers: B12b and B29 both re-pin; B29 merges after B12b and re-reads its after-reading as its baseline (§7.4).
COST: build and edits; producer `valoria-author` on `sonnet`, `high` (the source: "A0–A2, A4 `sonnet`, effort `high`; one `opus` read of each gate"); CR-51 (b)'s gap, if one is named, `opus` ("BUILDER: third tier").
EST: 4 h [estimate: §2.4's formula over four positions (0.4 h × 4 + 2.5 h)]

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B29.01 | `arrest` on a warrant addressed to the officer and heard of | `14_VERBS_PHYSICAL_A` A1 | BUILD | MOVER(behaviour) | Batch B14 (B14.27, A0), Batch B21 |
| B29.02 | `capture` forms only on persons under `war` or `crime`, custody to the warrant's court | `14_VERBS_PHYSICAL_A` A2 | BUILD | MOVER(behaviour) | B29.01; Batch B15, Batch B16 |
| B29.03 | the arrest re-measure, and the one gap it names | CR-51 (b) (intake `:195`) | BUILD (MEASURE, then BUILD only the gap) | EQUAL for the reading; MOVER if built | B29.02 |
| B29.99 | re-pin and close readings | E-1 | BUILD | MOVER (the re-pin) | B29.03 |

Not in this batch, and where each is: `14_VERBS_PHYSICAL_A` A0 and A4 (B14.27), A3 (B15); `U5b_VERBS_military_physical_residue.md` §4 (`mustered` excludes the restrained, B22).

### B29.01 — `arrest` on a warrant addressed to the officer and heard of · `14_VERBS_PHYSICAL_A_custody_and_force` A1 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/14_VERBS_PHYSICAL_A_custody_and_force.md` "A1 — `arrest`", "Order of landing" ("A1 (one commit: the reader, the stamp, both effects, the formation)"), "Gate", "Falsifier"; `audits/14_VERBS_PHYSICAL.md` §1.7; rulings A-21, A-22, A-23, D-25 (closed by the ladder: "an arrest needs no officer beside the prisoner; A1 is unchanged").
- ADVANCES: R-05 (`arrest` built out); the no-player half produces arrests.
- INSTRUCTION: the A1 table, copied:
  1. "`engine/season/queries/world_q.py` — add `warrants_for(w, actor, prisoner) -> tuple[str, ...]`: dispensations whose `terms` (via `record_sourced_operands`' `subject` key) is `prisoner` and that `actor` holds (`_held_warrants`' body, moved here from `loop/effects_information.py`) **or** that are in `addressed_records(w, actor_person, "dispensation")`, in tenure order then id."
  2. "same — add stamp term `warrants_heard(w, p)`: the persons named by `addressed_records(w, p, "dispensation")`, stamped in `_stamped` under `Person`."
  3. "`engine/season/loop/effects_information.py` — `_eff_arrest` and `_eff_seize`: replace `_held_warrants(w, a.actor, a.verb, prisoner)` with `warrants_for(w, a.actor, prisoner)`. Delete `_held_warrants`, since nothing else calls it `[verify by grep at landing]`. Docstrings: name the addressee half and cite this file." (At `aa31fd2` `_held_warrants` has a third caller in the same file, the `seize` licence helper that returns `bool(_held_warrants(w, actor, "seize", rid))`: it is re-pointed to `warrants_for` too, then the function is deleted; the grep's result in the commit body.)
  4. "`engine/season/decision/options.py` — `warranted` is the union of today's held-claims set and the person's `warrants_heard` stamp, read off `q.referents_for("Person")` where `addressed_records` put them. Pass the stamp through the Question, not the World (AX-2)."
  5. "`engine/season/verb_table.yaml`, row `arrest` — `requires_typed_note`: replace *'`arrest` forms only on a `subject` a HELD dispensation's `terms` names'* with *'…a dispensation he holds, or one addressed to him that he has heard of (`world_q.warrants_for`, `14_VERBS_PHYSICAL_A`), names'*. Add `payload_note`: the act's payload carries `warrant` (the Record id the effect licensed on), written by `_eff_arrest` on its Event for the reason trail. No other column changes."
- WHERE: `engine/season/queries/world_q.py` (`warrants_for`, `warrants_heard`, `_stamped`); `engine/season/loop/effects_information.py` (`_eff_arrest`, `_eff_seize`, the `seize` licence helper; `_held_warrants` deleted); `engine/season/decision/options.py` (`warranted`); `engine/season/verb_table.yaml` (`arrest`: `requires_typed_note`, `payload_note`).
- TESTS: in `engine/season/tests/test_vm_phy_a_custody.py`, a function for the audit's §1.7, written first and read red: "`build_realm(0)`; a court seat (a holder of `determine`) issues, through the real fold, a dispensation whose `terms` is a person and whose `to` is a seated holder of `dispatch` co-located with the issuer. One season through `SeasonDriver.season` with the shipped chooser and no hand-built act. Pass: the officer's opening set contains `arrest` on the named person; if attempted, its Event is `arrest.made` or `arrest.resisted`; on `arrest.made` the custodial holder's next opening set contains `interrogate` on the prisoner (`Detainee` read downstream)." — as `test_arrest_on_an_addressed_and_heard_warrant` `[ASSUMPTION: function name]`.
- FALSIFIER and CONTROL: "**Control:** the same world with `to` set to a third person forms no `arrest` for the officer. **Planted failure:** revert `_eff_arrest` to `_held_warrants`. The act forms and is refused at `write`. The test must fail on the refusal kind."
- GATE: `python -m pytest engine/season/tests/test_vm_phy_a_custody.py -q` → the A1 function and B14.27's A4 function pass; `git grep -n "_held_warrants" -- engine/season` → nothing; the realm hash at seed 0 after one season → moved where the stamp adds referents (declared).
- HASH MOVERS: "the arrest stamp's new referents" in every realm and spine pin where they occur. Declared; B29's re-pin.
- DEPENDS ON: V12 B14.27 (`world_q.addressed_records`); EXISTS-IN-TREE `loop/effects_information.py::_held_warrants`, `::_eff_arrest`, `::_eff_seize`, `queries/world_q.py::_stamped`, `decision/options.py` (`warranted`, the `WARRANT_SOURCED` block), `person_q.ledger_names`; V12 Batch B21 (`06_FA_remit_grant_by_row`; A-22's court that may order the officer).
- NAMES: none (no identifier this text uses is renamed by an earlier batch; "round" does not occur).
- GLOSSARY: none.
- COST and TIER: build; `sonnet`, `high`; the gate read by `opus`.
- LANDS IT: B29's `valoria-author` producer, `isolation: worktree`; `Item: B29.01`, `[skip ci]`.

### B29.02 — `capture` forms only on persons under `war` or `crime`, custody to the warrant's court · `14_VERBS_PHYSICAL_A` A2 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/14_VERBS_PHYSICAL_A_custody_and_force.md` "A2 — `capture`", the head's (4) and the 26_MASS_BATTLE fold paragraph (the custody write for named persons taken in a rout, under the `war` context); `audits/14_VERBS_PHYSICAL.md` §2.7; ED-IN-0337 (RULED: fighting is exceptional).
- ADVANCES: R-05's custody verbs; "beaten survivors exist (resentment, ransom, pardon, return). Courts hold people."
- INSTRUCTION: the A2 table, copied:
  1. "`verb_table.yaml`, row `capture` — add `referent_class: Person` and `referent_class_note: "14_VERBS_PHYSICAL_A A2: the challenge repair of 03_PC_duel_chain_reach (REM-28's precedent). Removes the exists:Person refusals. [ASSUMPTION; medium; revert: delete the column]"`"
  2. "`rosters.yaml: violence_contexts` — add the line `capture: [war, crime]`. In the note, add: *'`capture` (14_VERBS_PHYSICAL_A): ED-IN-0337 applied to the second violent row; no `duel` (a duel is `accept`'s), no `defence` (a man defending himself does not take prisoners).'*"
  3. "`loop/effects_combat.py::_eff_capture` — the `detain` object is `issuing_seat(w, rid)` of the first `rid` in `warrants_for(w, a.actor, captive)` that passes `_may_close_custody`. Otherwise it is `a.via`, as today. Docstring: 'custody goes to the court whose warrant it is: `arrest`'s rule, one owner'."
  The rout's taken persons (the 26_MASS_BATTLE fold) arrive "by this proposal's custody write, under its `war` context, with the seat that dispatched the march as the authority": no further edit here; the field's caller is B19's/B22's.
- WHERE: `engine/season/verb_table.yaml` (`capture`); `engine/season/rosters.yaml` (`violence_contexts`); `engine/season/loop/effects_combat.py` (`_eff_capture`).
- TESTS: in `test_vm_phy_a_custody.py`, a function for §2.7's planted scenario, written first and read red: "§1.7's world with the arrest forced to Failure by a fixture pool of 0 dice. The same officer's next opening set holds `capture` on the man. A scene fought to a yield opens `detain` to the warrant's issuing seat, not to `Act.via`." — as `test_capture_after_a_resisted_arrest_goes_to_the_warrant_court` `[ASSUMPTION: function name]`; `engine/season/tests/test_cr87_violence_contexts.py` green with the `capture` line.
- FALSIFIER and CONTROL: "**Control:** with no warrant, the officer forms no `capture` on him. **Planted failure:** delete the `capture` line from `violence_contexts`. Formation on a stranger returns, and the test asserts it does not."
- GATE: `python -m pytest engine/season/tests/test_vm_phy_a_custody.py engine/season/tests/test_cr87_violence_contexts.py -q` → pass; §2.7's aperture arm at the batch gate ("`aperture 2 s`, s = 0, 1, before and after: `capture` refusals on `exists:Person` and `individual` equal 0, and `capture` formed only on persons for whom `violence_context_of` returns `war` or `crime`"); the arm reading a mustered prisoner moves to B22 (UNDECIDED (3)).
- HASH MOVERS: "every realm and spine pin in which these formations occurred (`capture`'s 26 formations …)". Declared; B29's re-pin.
- DEPENDS ON: V12 B29.01 (`warrants_for`); EXISTS-IN-TREE `loop/effects_combat.py::_eff_capture`, `loop/effects_information.py::_may_close_custody`, `queries/world_q.py::issuing_seat`, `rosters.yaml: violence_contexts`; V12 Batch B15 (A3: `violence_contexts`' `fight` line drops `duel`, `context_terms`), Batch B16.
- GLOSSARY: none.
- COST and TIER: build; `sonnet`, `high`; the gate read by `opus`.
- LANDS IT: B29's producer; `Item: B29.02`, `[skip ci]`.

### B29.03 — the arrest re-measure, and the one gap it names · CR-51 (b) · BUILD (MEASURE, then BUILD only the gap) · HASH EQUAL for the reading; MOVER(behaviour) if built
- SOURCE: the intake `:195` (CR-51 · rows E1:174, E4:380 · "after B29 and B21 · gate: card exit (re-taken)") and §2 ("**CR-51 (b), the arrest re-measure, joins B29-pc-custody's tail**: it reads `arrest.made` after custody lands (B29) and after B21"); carry-forward `master/eval/E1.md` "### CR-51" (entry `workplans/valoria_master_workplan_v11_part4.md:443-455`); placed by §5.6's second rule (the entry's own text: "tail"); UNDECIDED (2); closes CR-51 (b).
- ADVANCES: R-05 (`arrest`; `pardon` read, built out in B32).
- INSTRUCTION: copied, with "four seasons" and `aperture 3 s` at two (A-114): "MEASURE first: print, at the base commit, `issue`'s minted terms by kind, the warrants held, the formed-and-attempted line of `arrest`, and `determine`'s refusals by read; BUILD only the link the reading names missing (a warrant naming a Person, or the `arrest` rank). No new motive and no special case for either verb (§0). `pardon` follows with no change of its own once an edge exists." "The church-custody warrant branch (a custody disposal becomes a warrant to a `dispatch` holder, who serves or declines, and a warrant that matures unserved is a witnessed decline) is this position's gap if the measure shows it, and is then built with CR-63's warrant duty." The measure is taken on this batch's tree after B29.02, seeds 0–2, two seasons; "the base commit" is read as B29.02's commit. A gap that is `pardon`'s (B32's `BUILT OUT`) or CR-63's (B24a) is named in the commit body and not built here.
- WHERE: none for the reading; for a named gap, the owner the reading names (`decision/options.py`'s `WARRANT_SOURCED` block, or the `arrest` row's rank), stated in the commit before it is edited.
- TESTS: none for the reading; a built gap adds one function to `test_vm_phy_a_custody.py` named after the link, written first and read red `[ASSUMPTION: the name follows the link]`.
- FALSIFIER and CONTROL: copied: "`aperture 3 s` [2 s]: `arrest.made` and `detention.ended` or `ban.ended` caused by computed acts; or the exit records the missing link by name and both verbs stay named residue (no position is invented to fix it). A planted `detain` on the seat: `pardon` closes it and emits (the check the effect already passes by hand)." Control: the reading moves nothing ("EQUAL for the reading").
- GATE: `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 2 --seeds 0 1 2` → `arrest.made` caused by a computed act at some seed, and `detention.ended` or `ban.ended` caused by a computed act, or the missing link named in the commit body; the four MEASURE lines quoted; if a link is built, its test passes and the realm hash moved (declared).
- STOPS IF: the reading names a link owned by another batch (`pardon`: B32; CR-63's warrant duty: B24a): the item records it and builds nothing.
- HASH MOVERS: none for the reading; "MOVER if built", declared and re-pinned at B29.99.
- DEPENDS ON: V12 B29.01, B29.02; EXISTS-IN-TREE `loop/effects_governance.py::_eff_pardon`, `_RESTRAINT_ENDED`, IN-12's warrant channel; V12 Batch B21.
- GLOSSARY: none.
- COST and TIER: reading, then a small build if named; `sonnet` reads, the build "third tier" (`opus`).
- LANDS IT: B29's producer; `Item: B29.03`, `[skip ci]` (a reading-only item commits its readings in the body).

### B29.99 — re-pin and close readings · `V12_STRUCTURE_part4.md` E-1 · BUILD · HASH MOVER (the re-pin)
- INSTRUCTION: re-record once, against B12b's merged after-reading (§7.4), every realm and corpus pin B29.01–.03 moved, in `engine/season/tests/_realm_goldens.py`; quote seeds 0–2; the commit says "re-pin" and lists the movers; write the close's record (§5.12).
- GATE: the BATCH GATE above, once, on this commit's tree, with the one full-suite run CLAUDE.md §0.4 allows at the close.
- LANDS IT: B29's producer; `Item: B29.99` — the batch's last `Item:` commit, pushed without `[skip ci]`.

| STOP. Batch B29-pc-custody closes here |
