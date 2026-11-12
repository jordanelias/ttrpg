# MB — adversarial steelman audit

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 601e715 (working tree)

Scope: `modules/mass_battle/` (29 files, 11,624 lines, 4,634 executable statements), `systems/mass_battle/sim/`,
`engine/season/loop/effects_army.py`, `engine/season/harness/army_presets.py` and `military_menu.py`, the host
side of the seam (`engine/season/seam/wrappers/mass_battle.py`, `loop/sides.py`, `loop/effects_combat.py::_eff_march`,
`seam/ladder.py::field_degree`), the B10-Z residue (CR-12, CP-T04-04, CP-T04-10), the army phase-5 design, the
squad-engagement proposals, and `research/` in full where it bears on a finding.

How the large files were read is stated in §12 (the code of every module file was read; comment prose in the
five largest files was read only where a finding depends on it).

## 0. Verdict

**Not yet a sound basis: the tactical engine is a real, deterministic, well-instrumented battle simulator, but
as shipped it never runs in natural play, and when it is forced to run at the shipped scale it does not resolve
a battle at all.** The single largest obstacle is the **scale and grading seam on the headcount path**: every
realm force is under one 100-troop block (`field_troops_per_weight: 1`), so `Unit.recalc_size` routs both sides
at the first tick whatever their strengths, `_grade` then reads the attacker as the loser in every seed, and the
"survivor ratio" it hands the season is `hp / 100`, not a survivor ratio, so `_eff_march` scales a loser's
`body` by his side's headcount rather than by what happened to him (measured: 99 troops marching on 1 loses
20 of 20 seeds and is written at 0.99; 30 marching on 18 loses 20 of 20 and is written at 0.30, untouched in
the battle). Above that floor the engine resolves a real, graded, monotone contest. Around it, the season
integration is unusually complete: one typed entry, four query entries, person-named casualties, morale that
feeds back into the next field, provisioning, sieges, orders, retreat and concession are all coded and tested.
But every one of the choice-bearing surfaces is shipped off or withheld (`withheld_verbs` holds the six army
verbs, `marshal` and `surrender`; `march_postures` ships `[storm]`; `field_subunits` ships `side`;
`field_provisioning` ships `False`; the preset armies are called by nothing), and in two seasons of the
populated realm at seed 0 the loop emitted `field.unopposed` three times and `field.won`/`field.lost` zero
times. The module's size is about half earned by what the season can reach under any fixture (50% of
statements, measured), about 29% by what the shipped fixture reaches, and 0% by what natural play executes.
Mass battle therefore generates no story today. It is two decisions and a handful of owner edits away from
doing so, and those are listed in §8.

## 1. What it is, as coded

### 1.1 The module (`modules/mass_battle/`, Layer 2, registered)

A cell-based tactical battle simulator on a 51 x 51 field. A `Unit` (one side) holds `Subunit`s; a `Subunit` is a
footprint of cells generated from `(troops, concentration)` or a tier table, each cell carrying troops, morale,
facing and position as floats (`hierarchy/units.py`). One call to `run_battle(unit_a, unit_b, max_turns=18)`
(`battle_loop.py:13`) runs up to 18 ticks (three phases of six): friction draw per side, body separation,
volleys, contact detection, order checks, target assignment, movement by time-of-impact, engagement resolution
(a sigma-leverage pool roll per engaged pair, cascading), casualty distribution to cells, close-ranks, stamina,
`recalc_size`, morale and discipline cascades, per-subunit and whole-unit rout, a phase boundary every six
ticks, facing updates.

Five composition rows reach it (`references/module_contracts.yaml:64-114`):

| row | target | entry kind | caller | shipped state |
|---|---|---|---|---|
| `mass_battle.resolve_field` | `massbattle:resolve_field` | `verb_call`, `march` | `seam/wrappers/mass_battle.py::resolve` (`:446`), `field_estimate` (`:504`) | live; reached only when a march meets a mustered opposing side |
| `mass_battle.army` | `armyrecord:apply` | `query` | `loop/effects_army.py::_apply` (`:57`) | the six verbs are in `withheld_verbs` (`data/fixtures.py:1157`): reached only by a hand-built act |
| `mass_battle.army_order` | `armyrecord:fielded` | `query` | `seam/wrappers/mass_battle.py::_order_of_battle` (`:214`) | live, returns `None` in every shipped realm (no `army` Record exists) |
| `mass_battle.army_options` | `armyrecord:options` | `query` | `harness/military_menu.py` | harness only |
| `mass_battle.army_preset` | `troop_types/presets:plan` | `query` | `harness/army_presets.py` | harness only; nothing in the loop calls `install` |

`resolve_field(inp, rng, *, troops_a, troops_b)` (`massbattle.py:473`) takes the frozen `MassBattleInput`
(`queries/inputs.py:205`), builds two `Unit`s by one of three constructors, derives one terrain row, runs the
battle under `rngsource.using(rng)`, and returns `{attacker_wins, degree, attacker_size_pct, defender_size_pct}`
plus, on the `person` arm, `subunits` and `broke_first`. It reads no `World`, holds no token and keeps no state
between calls (the RNG is a context variable scoped to the call, `rngsource.py:45-64`).

The three constructors:

1. **headcount, `side`** (`_weighted_unit`, `:257`), the shipped path: one `Unit`, one `infantry` `Subunit`,
   `troops = Σ weight x troops_per_weight`, power 4, command 4, discipline 5, both sides anchored at `(8, 12)`.
2. **headcount, `person`** (`_person_unit`, `:312`), fixture `field_subunits: person`: one subunit per
   commanding person, with a `broke_log` recording who broke first.
3. **order of battle** (`_oob_unit` → `orderofbattle.build_unit` → `armies.build_army`), when either side's
   faction holds an `army` Record whose commander is present: multi-subunit, typed troops, roles, strategy.

### 1.2 The host side (`engine/season/`)

`march` declares `contests: a field`; the prize row names module `mass_battle`, provider `mass_battle`,
`module_entry: mass_battle.resolve_field` (`rosters.yaml:1685-1687`). `loop/sides.py::sides_of` musters the
attacker's side at the actor's origin under the seat's faction, names the target's holder faction as `subject`
(or `None` for own or unheld land), and refuses a non-settlement, non-territory target by an empty army
(`:122-130`). `seam/wrappers/mass_battle.py::resolve` then answers, in order: PARTY-GAP; `Unopposed` for an
empty defence (no engine call, `:401-414`); `Invested` for an opposed `besiege` (no engine call, `:415-422`);
otherwise builds the input (`field_input`, `:225`), asks `settlements.provision` for each side's fielded
troops (`_fed`, `:331`) and calls the entry. `seam/ladder.py::field_degree` (`:198`) grades the lifted
`unopposed` / `invested` / `attacker_wins` markers onto `Unopposed` / `Invested` / `Won` / `Lost`.
`loop/effects_combat.py::_eff_march` (`:450-683`) writes the outcome.

State mass battle owns in the season: none of its own. It writes `Person.body` (losers by the engine's ratio;
winners too under `field_winner_casualties: engine`), two `Person.stance` rows on each loser (a grudge toward
the winning faction, a morale row toward his own), the claimants' `contain` legs on `Won` and `Unopposed`
(arrival), `Rung.stores` debits when provisioning is on, `Site.condition` on `Invested`, and the `army`
Record's `subject_matter` through the army verbs.

### 1.3 Execution evidence (commands and seeds in §12)

- **Natural play fights nothing.** `python -m engine.season.harness.aperture 2 0` (`PYTHONHASHSEED=0`,
  `build_realm(0)`, two seasons): `march` formed 26, attempted 13 and refused 10 in season one, attempted 12
  and refused 12 in season two; events `field.unopposed` 3, `army.arrived` 3; `field.won`, `field.lost`,
  `siege.pressed`, `place.surrendered`, `order.marshaled` and all six `army.*` kinds are in the
  never-emitted list in both seasons; `recruit`, `form_unit`, `assign_troops`, `order_unit`, `marshal` and
  `surrender` formed 0. `engine/season/requirements.yaml:1447-1450` records the same at seeds 0 to 2 ("the
  realm fights 0").
- **Line reach, measured.** A `sys.settrace` probe over `resolve_field` (script and JSON in §12): the shipped
  arm (`side`, `troops_per_weight` 1, 3 seeds) executes 1,363 of 4,634 statements (29%); the union of every
  season-reachable arm (`side`, `side` at k 30, `person`, standing orders, two orders of battle, one order of
  battle against a headcount side; 4 seeds each) executes 2,295 (50%). Per file in §4.2.
- **The shipped-scale field is not a battle.** `_weighted_unit` pairs through `run_battle`, seeds 0 to 19:
  30 v 18, 30 v 6 and 99 v 1 all end at tick 2 with both sides routed and the attacker graded the loser in
  20 of 20; 120 v 60 and 150 v 60 end at tick 2 with the defender alone routed, 20 of 20, the attacker
  untouched. Only at 250 v 120 (and 300 v 180) does the outcome vary by seed.
- **The one fought field the shipped realm produces is that non-battle, written onto people.** `build_realm(2)`,
  one season (the register's own reading of seeds 0/1/2 is `field.lost` 0/0/1, `hole_register.yaml` H-359):
  one `field.lost`; of six persons whose `body` moved that season, four moved to exactly their side's weight
  sum over 100 (two attackers 1000 → 20, two defenders 1000 → 30).
- **Preset armies do not change it.** `army_presets.install(build_realm(0))` raises three armies, all levy
  (Hafenmark 600, Valorsmark 900, Varfell 600: the realm has no barracks, range or stable); two seasons
  afterwards read the same events as the control (`field.unopposed` 3, `army.arrived` 3, no fought field),
  with a different content hash (`0622a841` against `bacd687f`).

HEAD moved to `30de093` while this audit was written (the suite's own documentation commits);
`git diff --stat 601e715 HEAD -- modules engine systems tools tests references` is empty.

## 2. Steelman

Ranked by how much weight each bears.

1. **One resolver, reached by row, with a clean seam.** The season calls the same `run_battle` the oracle
   harnesses call; nothing in `engine/` imports the module (`resolve_field` is reached through
   `MODULE_ENTRIES`, the four query entries through `composition.require`); the module reads no `World`, the
   host decides nothing about the fight. This is the shape `04` asks for, and it is the property the
   precedent corpus treats as hardest to buy back later (auto-resolve as a second answer to the same
   battle). *Attack:* the reach probe. *Survives*, with a limit: the season asks the engine questions no
   harness asks (F-MB-01), so "one engine" has not yet meant "one calibrated answer".
2. **Determinism is real.** Every draw goes through `rngsource.get()` (a context variable scoped to the
   call); the same seed gave the same result in every repeated probe here; the estimate uses a private
   stream so asking the odds moves no hash (`_estimate.py`). *Attack:* looked for a bare `random.` call in
   the reached code: the only one is `rngsource`'s fallback outside a scope. *Holds.*
3. **Consequences name people and feed back.** A lost field writes each loser's `body` and two stance rows;
   the morale row is read back as the next field's morale-start (`_morale_start`), so a beaten faction
   fights worse next time, with no stored faction stat. Under the army path the bleeding lands on the
   cohorts the troops were drawn from (`parties["fielded"]`), so a lost battle shrinks the next muster and
   `tend` restores it. Under `field_subunits: person` each commander is scaled by his own subunit and the
   first to break rides the Event as an Observation. This is a complete consequence loop in code.
   *Attack:* is it reached? Only by hand-built acts (F-MB-03), and the magnitude it writes on the shipped
   path is wrong (F-MB-02). *The design survives; the shipped behaviour does not.*
4. **Every lever ships with its control arm.** Each of `field_casualty_model`, `field_winner_casualties`,
   `field_subunits`, `field_troops_per_weight`, `field_walls_dr`, `field_provisioning`,
   `field_morale_loyalty_gain` has a closed roster, a refusal on an unknown value, and a shipped value
   that reproduces the tree before it. That is exactly what makes a later flip a single-variable
   experiment. *Attack:* the cost is that the shipped game is the control arm of every experiment at once.
   *Holds as method; it is also the reason nothing plays.*
5. **The engine is honest about its debt.** Magnitudes are tagged `CALIBRATED-DEBT` or `ASSUMPTION` at the
   site with a revert; the attrition-law instrument refuses an unidentifiable fit; retractions are kept in
   the comments. *Attack:* opened the CR-12 design against the three code sites it names; all three read
   as it says (§5.3). *Holds.*
6. **The tactical model is rich where history says richness matters.** Cell-level morale and facing,
   time-of-impact movement, octagon damage, brace against charge, conditional orders and signals,
   contagion rout in a 15 to 30% band. *Attack:* does any of it reach a season outcome? At the shipped
   scale none of the phase logic executes at all (`core/state.py`: 0 of 82 statements, because the battle
   ends at tick 2, before the first phase boundary). *Fails as shipped; holds above the floor.*
7. **The module's size is partly a harness, by design.** `run_multi_turn_battle` and
   `run_multi_unit_battle` exist for the oracle and the workbench. *Attack:* §4.2 and F-MB-05: they are a
   second code path, and they are in `modules/`, the registered tree, not in `systems/.../sim/`.
   *Fails the one-code-path test.*

## 3. Adversarial findings

Ranked worst first. "Falsifier" names the run that would have shown the claim wrong, and its outcome.

### F-MB-01 · blocks a requirement · the shipped scale does not resolve a battle

- **Claim.** At `field_troops_per_weight: 1` every realm side is under `BLOCK_SIZE` (100), so
  `Unit.recalc_size` sets `size = floor(hp / 100) = 0` and routs the whole unit at the end of tick 1,
  untouched or not. Both sides rout; `_grade` then makes the attacker the loser in every seed.
- **Evidence.** `modules/mass_battle/hierarchy/units.py:2985-2990` (`recalc_size`); `:2865-2866`
  (`size = max(1, total // TROOPS_PER_SIZE)`); `battle_loop.py:392-393`; `massbattle.py:453-454`;
  `data/fixtures.py:789`. The weight to troops scale has **two owners that disagree by a factor of 30**:
  the fixture (1) for two headcount sides, and `recruitment.under_arms_cap` (`weight x 300 x 0.10`) for a
  headcount side facing an army (`massbattle.py:367-369`).
- **Falsifier.** A larger side winning at the shipped scale. Run: 30 v 18, 30 v 6, 99 v 1, seeds 0 to 19:
  attacker loses 60 of 60, every battle ends at tick 2 with both sides routed. `hole_register.yaml` H-250
  records 12 of 12 `Lost` at six weights through the real fold.
- **Touches.** R-04 (the fought-field conjunct), R-07 conjunct 3, R-09 (a contest whose outcome has one
  value is not probabilistic), R-05 (`march`'s `Won` band never earns its kinds from play).
- **Narrative consequence.** War cannot be won. Any character who marches on a defended place is
  maimed for it, deterministically.
- **Minimal fix at the owner.** One owner for the scale: `resolve_field`'s headcount path sizes a side by
  `under_arms_cap(weight)`, the function its army path already uses, and `field_troops_per_weight` is
  deleted (§6.2 R-01; proposal `04_MB_headcount_grade_and_scale.md`). This is necessary and not
  sufficient: a realm side is two to six persons at weight 1 (60 to 180 troops at that scale), so the
  100-troop cliff still decides small fields until armies exist (F-MB-03).

### F-MB-02 · blocks a requirement · the headcount path's "survivor ratio" is not a ratio

- **Claim.** `_grade` reads `effective_size / max(1, size_max)`. `size_max` is the starting troop count
  floored to whole hundreds (minimum 1) and `effective_size` is `hp / 100` unfloored, so the figure is
  `hp / (100 x floor(start / 100))`: below 100 troops it is headcount over 100; above, it over-reads by
  up to a factor of two. `_eff_march` multiplies each loser's `body` by it with no cap.
- **Evidence.** `massbattle.py:447-448`; `units.py:2866`, `:2985`; `loop/effects_combat.py:637` (loser,
  uncapped), `:587` and `:658` (winner, capped at 1). The army path was fixed for exactly this
  (`by_troops`, `massbattle.py:438-445`: "a lost field raised the loser's body to 1092 of 1000"); the
  headcount path was left "so its goldens do not move".
- **Falsifier.** A losing side whose ratio exceeds 1. Run: attacker wins 289 of 400 battles at 600 v 120,
  600 v 150, 450 v 190, 1200 v 199 (seeds 0 to 99 each); in **70 of the 289 the losing defender reads
  above 1.0**, worst 1.638 (199 troops, 163.8 left, routed): the fold would raise a beaten man's `body`
  by 64%. Second run, the other direction: 30 v 18 at the shipped scale, attacker untouched (30.0 of
  30.0), written at 0.30. Season confirmation: seed 2, one season, bodies 1000 → 20 and 1000 → 30.
- **Touches.** R-01 and R-02 (what propagates is an artefact), R-09 (graded magnitude), R-04.
- **Narrative consequence.** The smaller your war band, the worse a field hurts you, whatever happened in
  it; a defender who won is cut to 3% of his body; and at army scale a beaten garrison can come out
  stronger than it went in.
- **Minimal fix.** `_grade` reads `hp / hp_max` on both paths; the `by_troops` parameter is deleted
  (§6.2 R-02; same proposal). Hash: moves only where a field is fought (seed 2's one-season pin).
- **Also falsified by this:** `HANDOFF_MB.md`'s "a side under 100 troops routs at once with its
  survivors intact, so it is not hurt". True of the troops; false of the write.

### F-MB-03 · blocks a requirement · nothing in natural play reaches the engine, and no choice surface is on

- **Claim.** In computed play the engine is not called: defended targets are rare (the register reads
  5 of 37 settlements with their holder mustered at tick 0), marches form on hearths and undefended
  places, and nothing gives a seated person a reason to march on a defended enemy. Every surface that
  would let a person choose how a battle is fought is withheld or shipped off.
- **Evidence.** `data/fixtures.py:1157` (`withheld_verbs`: the six army verbs, `marshal`, `surrender`);
  `rosters.yaml:1159-1176` (`march_postures: [storm]`); `fixtures.py:797`, `:809`;
  `harness/army_presets.py:12-15` ("nothing in the season loop ... calls this");
  `requirements.yaml:1447-1460`; `workplans/valoria_master_workplan_v11_part5.md:228` (MB-08, who marches
  where: LEAVE).
- **Falsifier.** A `field.won` or `field.lost` in a seeded natural run, or an army verb formed by the
  chooser. Run: `aperture 2 0`: none; all six army verbs, `marshal` and `surrender` formed 0. With the
  presets installed first: still none in two seasons. And when two preset armies are made to meet
  (module scale, levy 900 with role `Reserve` against levy 600, seeds 0 to 19): 14 of 20 end `Partial`
  (no rout, graded `Lost` for the attacker) with mean survivors 0.98 and 0.96; the realm's only possible
  armies stand off and barely touch.
- **Touches.** R-04, R-05 (`march` bands, eight withheld rows), R-07 conjunct 3, the no-player half of
  NERS-R (the world generates no war).
- **Narrative consequence.** The largest subsystem in the tree contributes no Event to a season.
- **Minimal fix.** Three edits, in order (§8): the scale and the grade (above); install the presets at
  realm build behind one fixture, with levy able to close (§6.2 R-07); and give `march` formation a
  defended-enemy referent, which is CORE's and CHAR's edge, not this lane's.

### F-MB-04 · degrades narrative · a field neither side wins is written as the attacker's defeat

- **Claim.** `run_battle` returns `winner: "draw"` when both sides rout or neither does
  (`battle_loop.py:468-469`). `_run_and_grade` discards that return and `_grade` recomputes: the attacker
  wins only if unrouted, unconceded and ahead. A mutual rout and an eighteen-tick stalemate both become
  `Lost`, and the attacker takes the morale and grudge rows of a beaten army.
- **Evidence.** `massbattle.py:427` (return value dropped), `:453-463`; `seam/ladder.py:222`;
  `hole_register.yaml` H-354 (measured). There are **three verdicts for one battle**: `run_battle`'s
  winner, `_grade`'s `attacker_wins`, and `_grade`'s four-way `degree`, which no reader uses
  (`seam/ladder.py:211-216`).
- **Falsifier.** A stalemate graded other than `Lost`. Run: spearmen 900 v 600 (seeds 0 to 19): 10
  `Failure`; levy v levy: 14 `Partial`; both `Lost` at the seam.
- **Touches.** R-09 (two of the module's outcomes collapse into one band), R-02.
- **Minimal fix.** A fourth fought band, `Drawn`, read off the module's own verdict (§6.2 R-03).

### F-MB-05 · blocks the standing requirement · the standalone battle and the season battle are two code paths

- **Claim.** The interactive standalone surface (`systems/mass_battle/sim/workbench/`) defaults to
  `resolve_battle(kind='multi')`, which runs `run_multi_turn_battle`: repeated engagements with position
  resets, between-turn stamina and ammunition recovery, rally out of yielding. The multi-unit kind adds
  pursuit, recall, feigned-retreat resolution, reserve commitment and freed-attacker damage. None of that
  is reachable from `resolve_field`. Conversely the season runs things no standalone surface runs: the
  `person` arm, standing orders, concession grading, provisioning.
- **Evidence.** `systems/mass_battle/sim/workbench/trace.py:73-91`; `systems/mass_battle/sim/engine.py:284-297`;
  reach probe: 16 of `orchestration.py`'s 48 functions (655 lines) are entered by no season arm, among
  them `run_multi_unit_battle` (305 lines), `between_turn_recovery`, `pursuit_damage`,
  `resolve_feigned_retreat`, `freed_attacker_damage`. Only `systems/mass_battle/sim/walkthrough.py:124-136`
  runs the season's own constructor and grader, and it is a replay, not a choice surface.
- **Falsifier.** A season arm entering `run_multi_turn_battle`. The union probe (six arms, four seeds):
  not entered.
- **Touches.** The standing requirement (one code path); R-04; the port (two paths to port).
- **Minimal fix.** The standalone scenario calls `resolve_field` with a `MassBattleInput`; the multi-turn
  and multi-unit loops move to `systems/mass_battle/sim/` beside the harnesses that are their only
  callers, or are deleted (§6.2 R-05; proposal `04_MB_typed_outcome_and_one_path.md`).

### F-MB-06 · degrades narrative · the seam drops most of what the battle knows, and the outcome is an untyped dict

- **Claim.** The module returns a `dict` with four keys (six on the `person` arm). It drops how the field
  ended (rout, concession, time), how long it took, the module's own winner, and on the army path
  everything per subformation: every cohort an army drew from is scaled by the side's one ratio, whether
  its troops stood in the line that broke or in the reserve that never moved, and no person is named as
  the one who broke.
- **Evidence.** `massbattle.py:465-470`, `:337-346`; `seam/wrappers/mass_battle.py:323-328` (`_fielded_by`
  returns the cohort list only); `effects_combat.py:550-553`, `:636`. `04`'s seam row asks for a typed
  output (`architecture/meta/04_CODE_ARCHITECTURE.md:147-149`); the input is a frozen dataclass and the
  output is not.
- **Falsifier.** A per-cohort ratio on the army path. Reading `_eff_march`: `per_person` is filled only
  from `engine_result["subunits"]`, which `resolve_field` sets only when `persons is not None`, which is
  only the headcount `person` arm (`massbattle.py:573-580`).
- **Touches.** R-01, R-06 and R-07 (a battle that cannot say who broke gives characters nothing to remember
  each other by), R-09.
- **Minimal fix.** A frozen `FieldOutcome` record owned beside `MassBattleInput`; per-cohort ratios on the
  army path by the `assigned` rows the record already holds (§6.2 R-04).

### F-MB-07 · degrades process · CR-12 is parked on a question the ledger already answered, behind an instrument that cannot read its own exit

- **Claim.** `ED-MB-0045`'s superseding row of 2026-10-01 (`needs_jordan: false`) says the engine
  "deviates from the Jordan-locked linear melee law ... and `CLAUDE.md` §0.05 says change the code ... the
  wait is now on engine work, no longer on a ruling". It postdates the 2026-07-08 pool directive. The
  2026-11-08 design re-raises it as a choice between two directives, and `HANDOFF_MB.md` and the plan now
  hold it for Jordan. Separately, the design's own §5.1 shows the exit cannot be read: the volley arm of
  the exponent check is mostly melee, the fit reads an exactly linear law with a frontage edge as 1.30 to
  1.45 against a 1.4 bar, and the LINEAR 4:1 band reads 52% for a cause nobody has bisected.
- **Evidence.** `registers/editorial_ledger_mb_archive.jsonl:73`; `proposals/2026-11-08-cr12-melee-attrition-design.md`
  §4, §5.1; code sites verified: `core/attrition.py:41-42` (body-average density), `orchestration.py:1308-1309`
  (opposed degree), `core/exchange.py:124` (numbers in the pool), `hierarchy/units.py:3013` (second copy
  of the base term).
- **Falsifier.** A keep-numbers fix that reaches the bar: the design's probes found none; not re-run here.
- **Touches.** None of R-01..R-09 directly; it moves who wins at army scale.
- **Minimal fix.** Decide by the ladder (§5.3, §6.2 R-06); build in the order instrument, consolidation,
  fix (proposal `04_MB_cr12_linear_law.md`).

### F-MB-08 · degrades narrative · a ruled magnitude swamps every choice the subsystem offers (named, not resolved)

- **Claim.** The per-battle friction draw (LogNormal, sigma 1.1 per side; ruled, `ED-MB-0016`, closed again
  at `ED-MB-0080`) makes the ratio of the two sides' draws vary by a factor of about 4.7 at one standard
  deviation. Any choice worth less than that in effective strength is noise to the person making it.
- **Evidence.** `config.py:328-331`; `core/exchange.py:147`; `orchestration.py:1725-1736`. Run (n 60,
  open ground, headcount path): attacker wins 78% at 5:1, 62% at 2:1, 42% at 1:1, 25% at 1:2. Run (n 20,
  army path): spearmen at 3:2 win 50%. `hole_register.yaml` H-361: roles outside the infantry menu move
  the field against their orderer under the shipped friction.
- **Falsifier.** An order whose effect on the win share exceeds the sampling error at a few hundred
  fields: H-361 records `Shock` moving a 50-scene tally from 0.38 to 0.18, the wrong way.
- **Touches.** R-04 and R-08 by way of the standing requirement ("choices change what happens").
- **Disposition.** Friction is ruled; this audit does not re-raise it. The conflict with the standing
  requirement is named in §9 and §11.

### F-MB-09 · hygiene, with a port cost · hidden inputs and held state in a registered module

- **Claim.** A registered module is supposed to be a function of its typed input. This one also reads 91
  environment variables at import (`config.py` 66, `hierarchy/units.py` 12, `orchestration.py` 11,
  `core/exchange.py` 2), which set which mechanisms exist; seven test files reload modules to change
  them. `equipment/` holds two process-global mutable registries with `override` and `remove`
  (`equipment/_base.py:74-83`). The dynamics are float throughout (`math.exp`, `gauss`, `tanh`, `atan2`),
  where the port's rule is bit-identity on integers (`architecture/holonic_ARCHITECTURE.md` §48).
- **Falsifier.** Looked for a reader of `ARSENAL.override` or `remove` in `modules/` and `engine/`: none;
  the mutators are unused.
- **Touches.** The port gate; determinism across processes (the same seed under a different environment is
  a different game with no record of the difference).
- **Minimal fix.** §6.2 R-08: the flags become one frozen config value the entry reads; delete the unused
  mutators. The float question is the GO lane's.

### F-MB-10 · hygiene · dead and unreached code

- `systems/mass_battle/sim/tactic_cards.py`: an empty dict "BLOCKED" since 2026-05-18, imported by
  nothing. `systems/mass_battle/sim/altonian_reinforcements.py`: one function that raises
  `NotImplementedError`, annotated with an undefined name, depending on modules that no longer exist;
  imported by nothing.
- `orchestration.py::rally_check` and `threadwork_check` are `pass`, called at every phase boundary
  (`:271-273`, `:316-318`). `Subunit.halt_before_enemy` is `pass`, called for every subunit every tick
  (`units.py:2363-2370`, `battle_loop.py:220-221`).
- `perimeter.py` (173 lines): entered by no season arm; its one caller is `_envelop_goal` for a slow
  enveloper (`units.py:1494-1503`).
- `Unit.base_combat_pool` (`units.py:2998-3033`) is a second owner of the pool's base term.
- `equipment/armour.py`'s `dr_vs_piercing` and the weapons' `keywords` have no reader; only a weapon's
  `reach` is read (`troop_types/registry.py:177-180`).
- Seven of twelve role instruction keywords resolve to no primitive (`units.py:85-100`), so `Screen` and
  `Pursue` fight as plain lines while the menus offer them (`HANDOFF_MB.md`, the A5 row).
- `massbattle.py`'s module docstring is 59 lines, most of it the history of three deleted functions.
- **Fix.** Delete the two stubs with their `FORK:` rows and the two ledger pointers that name them
  (`registers/placeholder_names.yaml:73-88`, `registers/mechanics_index.yaml`); delete the three no-ops;
  take the unwired roles off `TROOP_TYPE_ROLES` (§6.2 R-09, R-10).

### F-MB-11 · degrades narrative · after a won field the loser stays and the winner stands beside him

`hole_register.yaml` H-355, measured: on `Won` the attackers are re-homed under the target and the
defenders, cut, stay mustered there; title does not move. Both halves are labelled assumptions in
`_eff_march` (`effects_combat.py:532-536`). The consequence chain a battle should start (occupation, flight,
`seize`, reprisal) therefore starts from a position no reader can interpret: two armies in one town.
Disposition in §6.2 R-11.

### F-MB-12 · hygiene · surfaces that disagree with the code

Listed and resolved in §6.2 (R-12 to R-16): the handoff's "not hurt"; the phase-5 design's "winners are
never depleted, RULED" against the shipped `field_winner_casualties: engine`; `requirements.yaml`'s
"reached via natural computed play" against its own "the realm fights 0"; the provider's
`resolver="dice_pool"` label on a result no dice pool produced (`seam/wrappers/mass_battle.py:410`,
`:447`); the `_MVP_SUBUNIT_SHAPE` anchor that starts both sides on the same cells.

### F-MB-13 · hygiene · the choice surfaces that exist are priced wrongly for the chooser

`marshal` fans 15 roles by 3 retreat lines into 45 candidates per (person, settlement), which the chooser
scores identically, multiplying the season's candidate count by about 3.7 (`hole_register.yaml` H-361);
and a person can give each army verb once a season through the menu callback because the opportunity key
is `(verb, subject)` and the subject is the army (`harness/military_menu.py:148-151`). Both are why the
verbs are withheld. Disposition in §6.2 R-17.

### F-MB-14 · blocks the stated intent · individuals' attributes do not reach the battle (Football Manager's premise)

- **Claim.** In the reference the match engine resolves from the settings *and the individuals' attributes*.
  Here no attribute, skill or condition of any person enters a field except his `weight` and his stance
  toward his faction. Command is the literal 4; officers are "bookkeeping only"; the derivation from
  Charisma and Cognition has no season caller; troop quality is a table by type.
- **Evidence.** `massbattle.py:184-188`, `:198`; `orderofbattle.py:75`; `hierarchy/units.py:2862-2863`
  (the only call of `derive_command`, on harness-built units); `queries/inputs.py:205-260` (no capability
  field). §14.
- **Falsifier.** Two fields identical but for the commander: nothing in `MassBattleInput` can differ, so
  the results are equal by construction.
- **Touches.** R-06, R-04; SCN-14, ARC-23, NPC-072, NPC-082.
- **Conflict, named.** The 2026-07-08 directive took the commander out of the combat *pool*. §14's
  resolution feeds the commander into Command (span, cohesion, recall) and not into the dice, which is
  consistent with it; a reading of the reference in which a general's skill wins exchanges is not.
- **Minimal fix.** §14 (c); §8 step 8.

### F-MB-15 · blocks the stated intent · no intervention during a battle and no account of it afterwards

- **Claim.** The reference lets the manager watch, change tactics and substitute, and then explains the
  result. The season's field is one opaque call; the engine's trace (`resolution.tracing`: tick, melee,
  volley, casualty, positions) and its conditional orders exist, and neither crosses the seam. The
  provider accepts `host` and does not use it (`seam/wrappers/mass_battle.py:361-363`).
- **Evidence.** `massbattle.py:425-427` (no trace block, by design: "no trace block is opened"); the
  combat module's `fight(inp, rng, decide)` is the built precedent for a host decider inside a module call
  (`modules/combat/fight.py:55-70`, REM-31, ratified `proposals/2026-10-07-grid-mode-suspension.md`).
- **Falsifier.** A season Event carrying anything about how the field went beyond its band and, on one
  arm, one name: none (`effects_combat.py:668-683`).
- **Touches.** R-03 (nothing happens between the start and the end of a field), R-04, R-09.
- **Minimal fix.** `resolve_field(..., decide=None)` called at the two phase boundaries with a typed view,
  on the combat module's precedent; `FieldOutcome.report` (a bounded summary derived from the trace).
  Proposal `04_MB_playable_field_scenario.md`.

### F-MB-16 · degrades narrative · the non-player commander is a script, and the player is shown what no NPC may see

- **Claim.** A faction nobody plays gets its army from one fixed doctrine (45% heavy foot, 25% missile,
  20% horse, levy the rest), the same for every faction and every leader, folded directly between seasons
  without passing through DELIBERATE or anyone's budget. The odds of a field are computed for the player's
  display only; no NPC may read them.
- **Evidence.** `troop_types/presets.py:37-50`; `harness/army_presets.py:17-20`, `:40-49`;
  `seam/wrappers/mass_battle.py:465-466` ("MODE (a), THE PLAYER'S DISPLAY ONLY -- no NPC reads it").
- **Falsifier.** Two factions with different leaders producing different armies from equal means: `plan`
  takes no person.
- **Touches.** R-06, R-08 (a commander who cannot estimate is not imperfectly rational, he is blind; one
  who all follow one doctrine is not a character).
- **Minimal fix.** §16 (e).

## 4. Code matters

### 4.1 Ownership and duplication

| fact | owners found | verdict |
|---|---|---|
| weight to troops | `Fixtures field_troops_per_weight` (1); `recruitment.TROOPS_PER_WEIGHT x MUSTER_FRACTION` (30) | two owners, F-MB-01 |
| who won | `run_battle`'s `winner`; `_grade`'s `attacker_wins`; `_grade`'s `degree` | three, F-MB-04 |
| survivor share | `hp / hp_max` (army path); `effective_size / size_max` (headcount path) | two, F-MB-02 |
| pool base term | `core/exchange.py::subunit_combat_pool`; `Unit.base_combat_pool` | two; the second has no season caller |
| degree ladder | `resolution.py::compute_degree`; `engine/dice_engine/dice_engine.py::degree_from_net` | two implementations of one ruled ladder [UNVERIFIED: whether a test pins them equal; `tests/valoria/test_degree_ladder_single_owner.py` exists and was not opened] |
| die roll | `resolution.py::roll_pool`; the substrate's | two; the module's asserts TN 7 |
| unit baseline 4/4/5 | `massbattle._SEASON_FORCE_POWER`, `_MVP_UNIT_COMMAND`; `orderofbattle._UNIT_POWER`... | duplicated to avoid an import cycle, pinned equal by a test (`orderofbattle.py:72-75`) |
| army constructor | `_weighted_unit`; `_person_unit`; `armies.build_army` | three; the first two are the stub Jordan named (research lane file, T-MB-19) |
| order vocabulary | `massbattle.ORDER_ROLES` exported to `engine/engine_params/battle_orders.json` | one owner, exported: correct |

### 4.2 Reach (the distil test)

`sys.settrace` over `resolve_field`. "Shipped" is the `side` arm at k 1 (3 seeds); "any arm" is the union
of six arms (4 seeds each). Import-time statements are not counted as hit, so the percentages are lower
bounds for files that are mostly constants; function counts are given where they say more.

| file | lines | statements | shipped | any season arm | what it contributes at runtime |
|---|---|---|---|---|---|
| `massbattle.py` | 597 | 141 | 40% | 70% | the entry, three constructors, the grade |
| `battle_loop.py` | 482 | 198 | 66% | 73% | the tick loop |
| `orchestration.py` | 2,497 | 980 | 40% | 55% (32 of 48 functions) | engagement resolution, volleys; 655 lines in functions no arm enters |
| `hierarchy/units.py` | 3,083 | 1,358 | 30% | 56% (74 of 100) | data model, movement, facing, cell morale |
| `core/contact.py` | 517 | 224 | 25% | 35% | contact, orders, targeting |
| `core/exchange.py` | 222 | 71 | 51% | 59% | pools |
| `core/state.py` | 236 | 82 | **0%** | 90% | phase morale, discipline, rout: never runs at the shipped scale |
| `core/attrition.py` | 43 | 14 | 50% | 57% | the linear term |
| `geometry.py` | 532 | 233 | 44% | 59% | footprints, octagon, frontage |
| `percell.py` | 321 | 173 | 65% | 83% | casualty distribution, stamina |
| `resolution.py` | 230 | 94 | 41% | 70% | dice, degree, sigma head, trace |
| `terrain.py` | 290 | 76 | 9% | 9% | under-read here: the probe passed no territory |
| `armies.py`, `orderofbattle.py` | 599 | 239 | 0% | 65% | the army path only |
| `troop_types/registry.py` | 180 | 36 | 14% | 47% | stats, reach, roles |
| `equipment/` | 305 | 127 | 0% | 9% | one lookup (`reach`) |
| `perimeter.py` | 173 | 104 | 0% | 0% | nothing the season reaches |
| `armyrecord.py`, `presets.py`, `recruitment.py` | 618 | 318 | by their own rows | | reached through `mass_battle.army`, `army_order`, `army_options`, `army_preset`; pure, small, earned |
| **total** | **11,624** | **4,634** | **29%** | **50%** | |

**Judgment on size.** The record-keeping half (`armyrecord`, `recruitment`, `presets`, `orderofbattle`,
`armies`, about 1,200 lines) is earned: small pure functions, each reached by a row. The tactical half
(about 8,000 lines) is earned only above the 100-troop floor and only on the army path; on the shipped
path it is 1,363 statements run for two ticks to produce a constant. The remainder is oracle-only and sits
in the wrong tree (F-MB-05) or is dead (F-MB-10). Roughly: one tenth earned today in every sense that
counts, one half earnable by two fixture-level decisions, one third to move or delete.

### 4.3 Contract and seam fidelity

- Input: a frozen record, built by the host, the module's only reader. Conforms.
- Output: an untyped `dict`, with a second, different shape on one arm. Does not conform to "returns the
  typed output" (`04` `:147-149`). F-MB-06.
- No token, no write, no `World`: conforms (read `resolve_field` and all four query entries; none takes `w`).
- No state between calls: conforms for the RNG and the trace (context variables); does not for the
  environment flags and the equipment registries (F-MB-09).
- `_PersonSubunit` subclasses the engine's `Subunit` to observe a flag through a property setter
  (`massbattle.py:290-309`). It works and changes no value; it is also a second definition of what
  "broke" means, held in the adapter rather than the engine. Resolved by R-04 (the outcome record carries
  the order of breaking from the engine's own trace).
- The provider labels its result `resolver="dice_pool"` on all three return shapes; nothing reads the
  label for a field. Cosmetic, R-15.

### 4.4 Determinism

Same seed, same result in every probe run twice here. The risk is not in the draws but in the
environment (F-MB-09) and in iteration order: `resolve_engagements` keys several maps by `id(atom)`
(`orchestration.py:509`, `:634`, `:668-670`), which is stable within a call but orders nothing; the
iteration is over lists built in subunit order, so no dependence on `id` ordering was found
[UNVERIFIED beyond reading: no run permuted subunit order].

### 4.5 Test strength

Not opened in full (43 files; see §12). What the register and the code say about them:

- The season-level tests of a fought field are hand-built by necessity (`hole_register.yaml` H-359: "a
  HAND-BUILT field, because the shipped realm fights almost no field"). They execute the fold; they
  cannot show a field arises.
- The shipped `side` plus `engine` winner write "is seen by no test of its own, only by the seed-2 season
  pin" (H-360). That pin now holds F-MB-02's artefact (bodies of 20 and 30) as the expected value. A
  golden that encodes a defect is a change detector, not a falsifier; fixing F-MB-02 re-records it, and
  the commit should say so plainly (`CLAUDE.md` §7).
- `test_army_battle.py` found the above-1.0 ratio on the army path, which is the assertion that can see
  the failure; no equivalent exists for the headcount path, which is where it still happens.
- The byte-exact golden modes pin flags off for hermeticity (`config.py:321-327`), so the goldens cover
  three configurations that are not the shipped one, by design and disclosed.

### 4.6 Performance

One 18-tick field at a few hundred troops a side ran in well under a second here; `estimate_samples: 400`
therefore costs seconds per displayed estimate at army scale [UNVERIFIED: not timed in isolation; the
machine was shared]. `resolve_toi_and_commit` is quadratic in cells across sides and within a side
(`units.py:2686-2713`); at the 5,000-troop stress scale that is the cost centre (`ED-MB-0080`).

## 5. Design matters

### 5.1 Where intent, ruling and code agree

- An army is an order-of-battle record, raised from population and trained at infrastructure (Jordan,
  `ED-IN-0306`): coded as the `army` Record, `recruit_limit`, four site kinds. Agreed, and dark.
- One engine at every fidelity (ruled 2026-07-08): coded. Agreed.
- A lost field costs casualties, morale and a grudge (`ED-IN-0279` clause (b)): coded. Agreed.
- A won field moves presence, not title: coded as an assumption (R-6), consistent with `seize` owning
  title. Accepted here by precedent.
- Rout comes from broken cohesion in a 15 to 30% band (Jordan's value): coded, on by default, unreached at
  the shipped scale.

### 5.2 Where they disagree, and which the game follows

| design or ruling | code | the game follows | cost |
|---|---|---|---|
| Jordan, 2026-10-16: the single 4/4 Line is "a stub" | `_weighted_unit` is the shipped path | the stub | every realm field |
| phase-5 design M11: winners never depleted, RULED | `field_winner_casualties: engine` shipped (CR-24, M4 Ask B (b)) | the code | the design file is stale (R-13) |
| phase-5 design M1: the realm can field a surviving army after the scale change | it can, as levy, which barely fights | the code | presets are not a battle yet (R-07) |
| `04` §C.5.1: "units = PersonId[] at weight ... no unit class" | amended for armies by `ED-IN-0306`; inside the module a `Unit` class | consistent at the seam | none |
| melee is linear, locked | melee fits p 1.5 to 1.7 | the code | CR-12 (§5.3) |
| a field is graded on the one ladder | Won / Lost / Unopposed / Invested read off markers; the module's four-way degree unused | the markers | acceptable: `field_degree` is one owner; the four-way degree is dead (R-03) |

### 5.3 CR-12, judged against the code it would change

**The diagnosis is right.** All three channels by which troop numbers enter the melee term are in the
code as the design says: `lin_*` uses the whole body's average density (`core/attrition.py:41`), so every
casualty anywhere thins the contact rank; the pair pool is `eff_power x eff_size x POOL_QUALITY_SCALE`
split by engaged share (`core/exchange.py:124`, `:184-185`); and the degree is each side's net against
the other's (`orchestration.py:1308-1309`) with `Failure` dealing nothing. The design misses a fourth
route that its probe E also removes: `_sigma_net_boost` scales every sigma modifier by the square root of
the pool (`resolution.py:230`), so a bigger pool also amplifies morale, fatigue and stance terms.

**The stop condition did not need to fire.** Its two directives are answerable by the ladder:

1. *Superseded.* The later row governs. `ED-MB-0045` (2026-10-01, `needs_jordan: false`) was written with
   the pool-quality model already shipped and says: change the code to the locked law. A design that
   then finds the only way to do so removes numbers from the dice has found the *cost* of that decision,
   not a new question.
2. *Answered by a design document and by precedent*, in case step 1 is read narrowly. The 2026-07-08
   directive's contrast is the commander ("abandon combat pools being related to the commander"); its
   positive clause is satisfied when the exchange's strength comes from troop type, quality and numbers.
   Under option (a) numbers still set the exchange through the frontage term and through staying power;
   what leaves is their second entry through the dice. `config.py`'s own 2026-06-02 block made the same
   trade in the same words ("numbers enter outcomes ONLY through the Lanchester frontage term").

So: **(a), numbers out of the melee dice.** It is listed in §11 as the brief requires, because it narrows
the plain word of a standing directive, with this lane's reading that it is already decided.

**The build is not ready, for reasons the design itself gives and then defers.** Its exit ("melee p at or
below 1.4, volley at or above 1.6, on both arms, all four checks passing") cannot be read today: the
volley scenario is mostly melee over a no-rout trajectory, so a correct melee fix fails the volley bar;
the fit cannot tell a linear law with a 7:5 frontage edge from a super-linear one near the bar; and LINEAR
4:1 fell from 77% to 52% for a cause not bisected. Those are owed first, and none is a ruling. Order:
instrument repairs; the base-term consolidation (hash equal); then the fix and its re-calibration
(`POOL_QUALITY_SCALE`, the 4:1 band). And it should not run ahead of F-MB-01 and F-MB-02: the law's
exponent is measured over 160-tick no-rout trajectories, a regime the season never enters; what the
season feels is the win share by size ratio, which is the LINEAR check, the one currently failing for an
unknown reason.

### 5.4 NERS cuts (definitions `CLAUDE.md` §0.06; E scored last, as a ratio)

- **`_weighted_unit` at k 1 (the shipped field).** N: remove it and play is unchanged except that
  marchers stop being maimed; it fails N from every direction. R: fails completeness at its only
  operating point. S: one quantity, two ladders (F-MB-02). **Dies**; nothing is lost.
- **The army Record and its six verbs.** N: without it an army is whoever stands at a rung; raising,
  losing and refilling cannot be decisions. R: customisation, strategic thought, a player's impact; the
  no-player half fails today (nobody raises one). S: integrates through one row and one Record field.
  E, against that: 600 lines for the whole of force composition is proportionate. **Survives**; the cut
  would lose the only customisation the subsystem has.
- **`marshal`'s role and `retreat_at` on a headcount line.** N: narrowed. It holds only where the side has
  no army (bottom-up), and there the role is cosmetic or perverse (H-361). Once presets exist every side
  has an order of battle and the standing order is not read (`resolve_field` docstring: "an order of
  battle here is not read"). R: a retreat line is a real decision; a 15-way role on one infantry line is
  not. **The role dies on the headcount path; `retreat_at` survives and should apply to an army as
  `fall_back_at` does.** Lost: nothing a player could use.
- **Preset doctrine (45/25/20/levy).** N: holds from the no-player direction only where sites exist. R:
  fails completeness in the shipped realm (levy-only). **Survives with R-07.**
- **Friction at sigma 1.1.** Ruled; not cut. Recorded: it fails the first clause of E ("allows the player
  to intuit complex outcomes from simple choices") at the shipped magnitude, because the outcome of a
  simple choice is dominated by a draw the player cannot see. §11.
- **`run_multi_unit_battle` in `modules/`.** N: fails from the season's direction (unreached) and holds
  only from the oracle's. **Moves** to `systems/.../sim/`; what the cut loses in the registered tree is
  nothing.
- **Four fought bands (Won, Lost, Unopposed, Invested).** S: `Invested` is a clean pause ("pauses
  correctly when other systems are called for"); the fought pair fails to pause when a field is undecided.
  **Gains `Drawn`.**

### 5.5 Design that exists only as prose

Pursuit and the killing in the rout (the engine has `pursuit_damage`; the season reaches none of it);
captives taken on a field (the custody edge exists, `_eff_march` writes none); supply and attrition on the
march beyond the one ration debit; the troop stock (`CL-TROOP`, `CP-T04-10`: held on M3); a general who
decides where to march (MB-08); terrain chosen by the commander; the tactic cards (an empty dict since
May); mass-scale threadwork (ARC-43, SCN-14).

### 5.6 Against the stated intent: Football Manager and Total War (Jordan, 2026-11-12)

Full table in §17. The short judgment: **Total War is understood; Football Manager is named.** The
battlefield half (formations as footprints, terrain rows, morale as a track that breaks locally and
spreads, flanks and rear as damage multipliers, charge and brace, fatigue, ammunition) is built from the
mechanism up, with measurement. The campaign-to-battle-and-back half is built and is the best-designed
part of the seam (§2 item 3), though dark. The manager half exists as vocabulary: roles carry instruction
packages (`armies.py`'s own words: "the FM position->role model"), seven of twelve instruction keywords do
nothing, the roles that do something move the field against whoever ordered them (H-361), no individual's
attribute enters, nothing can be changed once the field starts, and nothing explains the result. The
squad-engagement synthesis (RULED 2026-09-25) built the orders, signals and officers that a manager would
use; `HANDOFF_MB.md` records them as built; the season reads none of them.

## 6. Hole-register and workplan disposition, and resolutions

### 6.1 Items the dossier lists

| item | listed | verified | evidence | action |
|---|---|---|---|---|
| H-151 same-faction march | open? | **closed** | `loop/sides.py:159-160` (`subject = None` when the holder is the marcher's faction); the row's own `default:` says closed by v9 IN-13 | none |
| H-250 the scale | closed? | **open** | the value is still 1; every realm field degenerate (F-MB-01) | R-01 |
| H-308 fortification is a step | open? | **closed in mechanism, open as shipped** | `seam/wrappers/mass_battle.py:270` grades `walls_dr` by `fort_level` when the fixture is set; `fixtures.py:781` ships `None`, the flat row. Run: walls at DR 3 cut a 5:1 attacker from 78% to 45% (n 60) | R-18 |
| H-354 mutual rout graded a loss | open? | **open** | F-MB-04 | R-03 |
| H-359 one body or commanding persons | closed? | **closed as built, dark** | `massbattle.py:573-580`; `fixtures.py:797` ships `side` | R-19 |
| H-150 garrison strength (WR) | secondary | closed in mechanism | `field_input` reads `fortification_of` | none |
| H-256 loyalty row (CHAR) | secondary | open, not this lane's | `seam/wrappers/mass_battle.py:134-138` records the collision | CHAR decides where loyalty is read; MB reads whatever row results |
| H-361 role against its orderer (CHAR) | secondary | open | F-MB-08, F-MB-13 | R-17 |
| H-355, H-360 (not listed, bear here) | | open as assumptions | F-MB-11; §5.2 | R-11, R-13 |
| CL-TROOP | HELD on M3 | held; largely overtaken | `ED-IN-0306` built the army Record, recruiting and presets; what remains of the troop stock is the population cost of raising (a cohort's `weight` does not fall when it is recruited) | answer M3 against `ED-IN-0306`: step 1 of the ladder for the stock, the rest LEAVE |
| MB-08 map, AI generals | LEAVE | **its falsifier has fired** | its entry says it is scheduled "the day" a requirement row names it as a cause; `requirements.yaml:1447-1460` names the absence of a march on a defended settlement as R-07 conjunct 3's failed link, which is the AI-general half | split: the "who marches where" half is scheduled (§8 step 5); the map generator stays LEAVE |
| CR-12 | HELD for Jordan | **answered by the ladder; build blocked on the instrument** | §5.3 | R-06 |
| CP-T04-04 field a round later | HELD on Ask C (b) | held, correctly | `ED-IN-0301` confirmed same round | none; R-03's `Drawn` band gives the later rounds without touching it |
| CP-T04-10 raise and keep a force | HELD on M3 | **superseded in part** | `recruit`, `disband_unit`, `discharge_troops` exist (`effects_army.py`); `levy` as a troop-raising verb is `recruit` under another name | close the `levy`/`disband` rows as superseded by `ED-IN-0306`'s verbs (step 1); the larder stock stays held |
| CR-52 the menu door | BUILD | open [UNVERIFIED: no harness file names it; not searched beyond `harness/` and the tests] | grep of `CR-52` under `engine/season/harness`, `tests/valoria`, `engine/season/tests`: no hit | build after R-17 |
| CP-T04-02/05/06/07 repairs | CLOSED | closed | the code paths read in §1 | none |

### 6.2 Resolutions (every inconsistency, gap and unclear passage found)

Ladder steps: 1 superseded · 2 irrelevant · 3 design document · 4 precedent · 5 architecture.
Proposal files are under `proposals/2026-11-12-subsystem-audit-suite/proposals/`.

| id | kind | what | decided resolution | step | proposal |
|---|---|---|---|---|---|
| R-01 | inconsistency | weight to troops has two owners (1 and 30 per weight) | one owner, `recruitment.under_arms_cap`; the headcount path calls it; `field_troops_per_weight` and H-250's "Jordan names the value" are closed. Jordan delegated the conversion ("you can invent one that makes sense", `recruitment.py:3-6`) and the tree already uses it for the same side against an army | 4 | `04_MB_headcount_grade_and_scale.md` |
| R-02 | inconsistency | two survivor-share formulas | `hp / hp_max` everywhere; delete `by_troops`; cap the loser's write at 1.0 at the one multiplication in `_eff_march` as the winner's already is | 5 | same |
| R-03 | gap | no band for a field neither side wins; three verdicts | `_grade` returns one verdict from one rule: `won`, `lost` or `drawn`; `field_degree` gains `Drawn`; `_eff_march` on `Drawn` writes each side's `body` by its own ratio, no stance row, no arrival. Delete the unused four-way `degree`. Precedent: `Invested` is already a band in which nobody wins, and `run_battle` already says "draw" | 4 | same |
| R-04 | gap | untyped outcome; army path names no cohort and no breaker | frozen `FieldOutcome` in `queries/inputs.py`: `verdict`, `ended` (`rout`, `concession`, `time`), `turns`, `sides` (two `SideOutcome`: `share`, `routed`, `conceded`, `parts` = per member or per cohort `(id, share, routed)`, `broke_first`). The army path fills `parts` per cohort from the record's `assigned` rows | 5 | `04_MB_typed_outcome_and_one_path.md` |
| R-05 | inconsistency | standalone and season are two paths | the standalone scenario is a host that builds `MassBattleInput` and calls the entry; `run_multi_turn_battle`, `run_multi_unit_battle` and their eleven helpers move to `systems/mass_battle/sim/` with their harness callers | 5 | same |
| R-06 | unclear | CR-12's two directives | (a) numbers out of the melee dice; superseded by `ED-MB-0045`'s 2026-10-01 row; build order: instrument, consolidation, fix | 1, 3 | `04_MB_cr12_linear_law.md` (and §11) |
| R-07 | gap | the realm's only armies are levy, and levy does not fight | install presets at realm build behind one fixture (`army_presets`, shipped `off`, then flipped as a declared mover); plant one training site per faction seat in the realm data so the doctrine has something to train (data, SE's file); give the levy line the `Hold` role, not `Reserve`, so it is a line and not a body that waits | 4, 5 | `04_MB_playable_field_scenario.md` |
| R-08 | gap | 91 environment flags are hidden module input | one frozen `EngineConfig` built once from defaults; the oracle harnesses construct variants explicitly; `os.environ` is read only in `systems/.../sim/` | 5 | `04_MB_typed_outcome_and_one_path.md` |
| R-09 | gap | dead stubs | delete `tactic_cards.py`, `altonian_reinforcements.py`, with `FORK:` rows and the two ledger pointers | 2 | same |
| R-10 | unclear | role menu offers roles with no primitive (A5) | take `Screen`, `Pursue`, `Harass`, `VolleyLine`'s `volley`, and the `pin`, `loose`, `shoot_move` keywords off `TROOP_TYPE_ROLES` / `ROLE_SPEC` until one has a primitive; `#445 U-3` already said to stop presenting roles as a design axis | 3 | same |
| R-11 | unclear | H-355: where the beaten side goes | follow the code's two assumptions (presence moves, title does not; a routed attacker stays home) and add the missing third: a beaten **defender** who routed is re-homed to the nearest rung his faction holds, by `_relocate`, or stays if there is none. Precedent: `Lost` already says a routed army is at its origin; `surrender` (CP-T04-07) already hands a place over | 4 | `04_MB_playable_field_scenario.md` |
| R-12 | inconsistency | handoff: "under 100 troops ... not hurt" | the handoff row is corrected when R-02 lands (after which it is true) | 1 | none (pointer edit) |
| R-13 | inconsistency | phase-5 design M11 against CR-24 | the code governs (`engine` arm shipped); the design file gets a one-line superseded note on M11 | 1 | none |
| R-14 | inconsistency | `requirements.yaml` scales note "reached via natural computed play" | reword at the owner to what the instrument reads: `march` executes; a fought field does not (seeds 0 to 2: 0, 0, 1) | 3 | none |
| R-15 | unclear | `resolver="dice_pool"` on a field result | drop the key from the mass-battle provider's returns, or name the module; nothing reads it | 5 | `04_MB_typed_outcome_and_one_path.md` |
| R-16 | unclear | both headcount sides anchored at `(8, 12)` | both headcount constructors deploy through `orderofbattle._place` (one line each), so a headcount field starts three rows apart like an army field; delete `_MVP_SUBUNIT_SHAPE['starting_position']` | 4 | `04_MB_headcount_grade_and_scale.md` |
| R-17 | gap | `marshal` fan and the once-a-season army verb | the standing order's `role` is dropped from the fan (R-10, §5.4): `marshal` ranges `retreat_at` only (3 bags); army verbs get the opportunity key `(verb, subject, payload digest)` so a commander can give several in a season | 5 | `04_MB_playable_field_scenario.md` |
| R-18 | gap | H-308 walls are a step as shipped | ship `field_walls_dr: 3`, which with CP-T04-05's scaling is "A.9's +3 at a full garrison, proportionally less below"; `None` (flat) stays the control | 4 | `04_MB_headcount_grade_and_scale.md` |
| R-19 | unclear | `field_subunits`: `side` or `person` | `person`, after R-01. A battle that names who broke is the one the nine ask for; `side` stays the control | 5 | same |
| R-20 | gap | MB-08's falsifier fired | schedule the march-target half (§8 step 5) | 3 | `04_MB_playable_field_scenario.md` |
| R-21 | unclear | `massbattle.py`'s docstring is history | cut to what the file is; the history is in git and the ledger | 5 | `04_MB_typed_outcome_and_one_path.md` |
| R-22 | gap | recovery of morale | a lost field's morale row has one remover, `forgive`, which each loser must choose for himself [UNVERIFIED: whether the chooser forms `forgive` on a faction referent]; add the symmetric write: a `Won` field removes one morale row from each winner who holds one (`held_against`), so victory restores what defeat took | 4 | `04_MB_playable_field_scenario.md` |
| R-23 | inconsistency | `CP-T04-10`'s `levy`/`disband` against `recruit`/`disband_unit` | superseded by `ED-IN-0306`'s verbs | 1 | none |

Resolutions decided: **23**.

## 7. Research transfer

Read: `research/00_INDEX.md` (§1 and the mass-battle rows), `research/by_lane/MB_mass_battle.md` (§0, §7 in
full; headings of the rest), `research/game_precedent_suite/dispositions/D_T04.md` (the disposition table
rows cited below). Not read: `research/pre_firearms_formations/` beyond what the lane file reports of it,
`research/historical/`, `research/emergent_narrative_literature/` (§12). The lane file's own verdict on
the historical corpus stands unexamined here and is relied on: written from memory, self-checked, numbers
unsourced.

**Precedents that change what to build.**

| precedent (as the corpus records it) | what it changes here | where |
|---|---|---|
| The pre-battle panel: strength and projected result shown; fight, delegate or withdraw (Total War, Jagged Alliance 2, Bannerlord; D_T04 rows 3, 46, 55) | already transferred into code at B10-12 (`field_estimate`, `retreat_at`, `surrender`, `besiege`) and all four are dark. The transfer still owed is switching them on as one choice surface | §8 step 4; proposal 3 |
| A priced exit: only a hero may retreat or surrender, at the cost of the army or gold (Heroes of Might and Magic, D_T04 row 34) | `retreat_at` and `surrender` need a price a chooser can weigh; today concession costs exactly what losing costs | R-03 (`Drawn` and concession are distinct endings in `FieldOutcome.ended`) |
| Levy and professional troops are different economies; raising troops removes a cohort, not a number (Crusader Kings, Shogun 2, Jagged Alliance 2, Manor Lords; lane file T-MB-5) | the quality half is built (`TROOP_TYPE_STATS`); the population half is absent: `recruit` does not lower the cohort's working weight. An SE edge, named in §10 | not proposed here |
| A garrison is an assignment, not a unit type (lane file T-MB-6) | confirms `mustered at the target` and R-11's re-homing of a routed defender to a held rung | R-11 |
| Conquest is occupation, then title (Rome II, Crusader Kings 3; T-MB-14) | confirms presence-not-title on `Won` (accepted as precedent in §5.1) | none |
| One-clock games resolve battle by strategy selection (Empires in Arms, Pax Pamir; T-MB-12) | the playable field should offer one selection per engagement, not a tactical clock: this is why proposal 3 builds rounds out of the `Drawn` band and not a pause inside `run_battle` | proposal 3 |
| A tactics list of conditions and responses (Unicorn Overlord, D_T04 row 40) | the engine's `Order` triggers already are this; the army Record carries one of them (`fall_back_at`). Nothing to build | none |
| Cohesion breaks before the body; most killing is in the rout (du Picq as the lane file reports him; PFF T-29) | supports a verdict that distinguishes rout from attrition (`FieldOutcome.ended`) and the pursuit gap in §5.5 | R-04 |

**Tried, did not transfer.**

- *Football Manager's "three fidelities of one engine"*: D_T04 row 58 marks the repository's own claim
  CONTRADICTS, not established. The one-engine rule stands on the 2026-07-08 ruling and on Total War's
  documented counter-example (auto-resolve "casualties may be heavier"), not on Football Manager.
- *Total War's 30% and 20% wipe-out thresholds* (D_T04 row 6): community-tested mod discussion; a lead,
  not a number.
- *Ultimate General's "routers return when morale recovers"* (row 23): player claims; the engine has no
  rally (`rally_check` is `pass`). Not built on.
- *The pre-firearms formation matchup matrix*: single-author, over a hundred internal contradictions by
  the lane file's count. Decorative for any constant.
- *The gauge bands* (`mass_battle_gauge_grounding.md`): ceilings were raised after the engine exceeded
  them and they gate nothing. Decorative.
- *The 15 to 30% rout band's attribution to du Picq*: the lane file reports *Battle Studies* gives no
  percentage. The band is Jordan's value and binds as a ruling, not as history.

**Nulls.** The corpus records that no surveyed game keeps one person's leverage meaningful from a duel to
a battle of thousands, and that the nearest shape (a lone commander's death routs the army) is a known
failure (lane file T-MB-4; its Dominions leg is marked unverified at source). The engine implements that
failure shape (`battle_loop.py:411-413`, command 0 is an instant rout) and the season never reaches it.
ARC-23 and SCN-14 (§13) ask for exactly this seam; there is no precedent to copy, and §13 says so.

**Read against the two named references** (Jordan, 2026-11-12; the corpus's own account of each).

- *Football Manager.* What the corpus establishes is thin: D_T04 row 58 marks the repository's claim about
  its three fidelities as not established, and the squad-engagement concept "names nine games and surveys
  none" (lane file T-MB-16). What transfers without leaning on unverified detail is the *shape* the brief
  states: settings plus individuals in, an automatic result out, intervention at breaks, an explanation
  after. Three of those four are absent (F-MB-14, F-MB-15).
- *Total War.* The corpus is better here (`tutorials/T07_mass_battle.md`, `tables/R6`, D_T04 rows 3 to
  11): the contact panel with projected result and the choice to fight, delegate or withdraw; first-party
  warnings that auto-resolve differs from the played battle; post-battle captive and settlement options;
  stances and attrition on the march; siege as a state with a timer. Built from it: the estimate, the
  exit, the siege posture, presence-then-title. Not built: captives, march attrition, a siege clock, and
  the played battle itself.
- *Null carried from the corpus:* Total War's own auto-resolve is the documented case of two answers to
  one battle. Valoria's protection is the single engine; it holds only if the played mode is the same call
  with a decider (F-MB-15's fix), not a second loop (F-MB-05).

## 8. Best path forward

Ordered. "Alone" is what the subsystem needs to run well by itself; "compose" needs another lane.

| # | what changes | where | gate (execution artifact) | unblocks | cost | alone / compose |
|---|---|---|---|---|---|---|
| 1 | Survivor share is `hp / hp_max`; one weight to troops owner; headcount sides deploy three rows apart; graded walls shipped | `massbattle.py` (`_grade`, `_weighted_unit`, `_person_unit`, `resolve_field`); `effects_combat.py:637`; `data/fixtures.py` (delete `field_troops_per_weight`; `field_walls_dr: 3`) | the module probe of §12 re-run: no loser above 1.0 in 400 battles; at realm weights the larger side wins more than half at 3:1 over 60 seeds; the unmodified realm pair folds through the driver to a band that varies by seed; the seed-2 pin re-recorded, said plainly | R-04, R-07 c.3, R-09 | edit | alone |
| 2 | `Drawn` band; frozen `FieldOutcome`; per-cohort and per-person parts | `massbattle.py`; `queries/inputs.py`; `seam/ladder.py::field_degree`; `rosters.yaml` (band roster, `verb_table.yaml` `march` row); `effects_combat.py::_eff_march` | a hand-built stalemate folds `field.drawn`: both sides' bodies move by their own share, no stance row is written, nobody arrives; a planted side-ratio-for-every-cohort write reddens the army-path test | R-09, R-01, R-02 | small build | alone |
| 3 | One code path: multi-turn and multi-unit loops and their helpers leave `modules/`; environment flags become one frozen config; dead stubs and no-ops deleted; unwired roles off the menu | `modules/mass_battle/orchestration.py`, `config.py`, `hierarchy/units.py`; `systems/mass_battle/sim/` | the reach probe re-run: every function left in `modules/mass_battle/` is entered by a season arm or a composition row; `git grep -n environ modules/mass_battle` is empty; `tools/ci_golden_modes_check.py` digests equal | the standing requirement; the port | edit (large diff, hash equal) | alone |
| 4 | The playable field: a seeded two-faction scenario, a player chooser, the estimate before each choice, a battle report after | new `engine/season/harness/field_scene.py`; un-withhold `marshal` (retreat line only) and `surrender` inside the scenario's fixtures; `march_postures: [storm, besiege]` there | two policies at one seed end in different bands with different persons hurt; the same policy at two seeds differs; the report names who broke first on each side | R-04, R-05 (`marshal`, `surrender`, `besiege` earn their kinds) | small build | alone |
| 5 | Armies in the realm and a reason to march: presets installed at build (fixture), a training site per faction seat, levy as a line; `field_subunits: person`; army verbs keyed by payload; a `march` candidate on a defended enemy settlement | `harness/populated.py`, realm data (SE), `troop_types/presets.py::ROLE_OF`, `data/fixtures.py`, `data/verbs.py::opportunity_key`; the candidate is CORE's and CHAR's | `aperture 2 s`, s = 0 to 2: `field.won + field.lost + field.drawn` above 0 at every seed and the `army.*` kinds out of the never-emitted list; declared hash movers | R-04, R-05, R-07 c.3, NERS-R's no-player half | small build + two declared flips | **compose** (CORE, CHAR, SE) |
| 6 | Aftermath: a routed defender is re-homed to a rung his faction holds; a won field removes one morale row from each winner | `effects_combat.py::_eff_march` | after a folded `field.won`, `mustered(target, loser)` is empty where the loser routed and holds another rung; a faction that loses then wins starts its third field at morale 5 | R-01, R-02 | edit | alone |
| 7 | CR-12: repair the instrument (volley scenario out of contact for the whole trajectory; a frontage coefficient in the fit or the bar read against the frontage control; bisect LINEAR 4:1), consolidate the base term, then numbers out of the melee dice and re-calibrate | `systems/mass_battle/sim/lanchester_signature.py`; `core/exchange.py`; `hierarchy/units.py` | the instrument 4 of 4 on both arms, its planted collapse still failing | none of the nine; the size-to-outcome curve | design-first, then small build | alone |
| 8 | Command and quality from the commander and the troops' training (§14) | `MassBattleInput`, `field_input`, `rosters.yaml: verb_capability` | a field between equal armies under commanders of different capability differs in win share beyond sampling error at n 400 | R-06, R-04 | small build | compose (CHAR) |

Steps 1 and 2 are the only ones that must precede everything else. Step 7 should not run ahead of them.

**Added by the stated intent** (Football Manager, Total War) and by the NPC charge; each is in a proposal.

| # | what changes | where | gate | unblocks | cost | alone / compose |
|---|---|---|---|---|---|---|
| 4a | The played battle is the same call: `resolve_field(inp, rng, decide=None)`; at each phase boundary the decider gets a typed view of its own side and may change approach (`advance`, `line`, `defend`) or order the retreat; `None` is today's field exactly | `massbattle.py`, `battle_loop.py` (the phase-boundary hook), `seam/wrappers/mass_battle.py` (forward `host.decide`, as `combat.py:394-395` does) | same seed with `decide=None` and with a decider that returns no change: equal outcome and equal draw count; a decider that orders `defend` at phase 1 changes the outcome at some seed | R-03, R-04; the Football Manager and Total War "fight or delegate" requirement | small build | alone |
| 4b | The battle report: `FieldOutcome.report`, a bounded tuple of phase summaries (per part: share lost, broke or held, flanked or not) derived from the engine's own trace | `massbattle.py`; `effects_combat.py` writes it as Observations on the band Event | a folded field's Event answers "who broke first, in which phase, facing what" for both sides | R-01, R-07 | small build | alone |
| 5a | A commander's doctrine is a choice: the preset plan's shares become data keyed by a doctrine name, the leader's act names the doctrine, and the commands go through `dispatching_chooser` (CR-52), not a direct fold | `troop_types/presets.py`; a typed doctrine file; `harness/army_presets.py` | two leaders with different doctrine names raise different armies from equal means; with the door off, nothing | R-06, R-08 | small build | compose (CHAR) |
| 5b | An NPC may weigh a field: the estimate run on what the person believes of the enemy, not on the world | `seam/wrappers/mass_battle.py::field_estimate` with an input built from the person's claims | a commander told a false strength marches where one told the truth does not | R-07, R-08 | design-first | compose (CHAR, knowledge model); conflicts with AQ-X1 as written, §16 |

## 9. Playable standalone and integrated

The standing requirement, point by point.

**Playable alone.**

| element | exists today | missing |
|---|---|---|
| scenario seed | none that is a game. Oracle scenarios (`systems/mass_battle/sim/stress_scenarios.json`, `walkthrough_example.json`); hand-built worlds in tests (`P.tiny_world`, a re-weighted `build_realm`) | a seeded scenario world: two factions, each with a seat that may `march`, an army Record with real troop types, a defended settlement, stores |
| choice surface, before the field | in code: the `march` target; posture `storm` or `besiege`; the standing order's retreat line; the army verbs through `harness/military_menu.py`; `surrender` for the defender | all but the target are withheld or off (`fixtures.py:1157`, `rosters.yaml:1176`); the defender has no turn (same round, `ED-IN-0301`) |
| choice surface, during the field | none: one atomic call of up to 18 ticks | a second and third engagement when the first is `Drawn`, with a choice between (press, hold, besiege, withdraw, yield) |
| outcome legibility | the band Event; `army.arrived`; on the `person` arm the Observation of who broke; `field_estimate`'s shares beforehand | a battle report in the season: how it ended, how long, each part's share, who broke on both sides. Today that exists only as `walkthrough.py`'s page, outside the loop |
| stakes | `body` on both sides; morale and grudge rows; presence at the target; garrison wear on `Invested`; stores when provisioning is on | title (by design, `seize`'s); captives; a price for conceding that differs from losing; any stake at all at the shipped scale beyond the artefact of F-MB-02 |
| end condition | per engagement: rout, concession, the tick cap | per war: none (`hole_register.yaml` H-176, no season-side ending; CORE's) |
| instrument | `field_estimate`; `harness/arms.py` over `field_casualty_model`; `walkthrough.py`; `stress.py`; `lanchester_signature.py`; `bat.py` | one that runs the scenario under a named policy and prints the report |

**One code path.** No (F-MB-05). The workbench runs loops the season cannot reach; the season runs arms the
workbench cannot. Step 3 and step 4 close it from both sides.

**Layer 1 conformance as a registered module.**

| rule | reading |
|---|---|
| reached by composition row, never by import (`holonic_ARCHITECTURE.md` §43) | conforms: five rows; no executable import of `engine` or `systems` under `modules/mass_battle/` |
| resolution at boot | conforms: `ENGINE-UNAVAILABLE` is the typed refusal when no driver registered the role (`seam/wrappers/mass_battle.py:426-428`) |
| typed input | conforms (`MassBattleInput`, the four query records) |
| typed outcome | **does not** (F-MB-06) |
| holds no token, writes nothing, reads no `World` | conforms |
| keeps no state | conforms for RNG and trace; **does not** for 91 environment flags and two mutable registries (F-MB-09) |
| no simulation state behind a global name (§47) | at risk in the port: the flag constants are module globals |
| integer arithmetic on exported scales (§48) | **does not**: the engine is float throughout. The seam is the right place to quantise (`FieldOutcome` shares as integers on the body scale); the engine's internal floats are the GO lane's question |

**Integrates.** In (executed when a field is fought): member weights, stances, loyalty rows, territory and
fortification, origin, standing orders, the army Record, stores. Out (executed): `body`, `stance`,
`contain` legs, `stores`, `Site.condition`, the Record's `subject_matter`. Out and read by others:
`body` gates budget and acts (`decision/budget.py`), stance feeds regard and the next morale-start, presence
feeds `occupies` and so `seize`. Scale transition: there is no zoom. The field is resolved inside
ENCOUNTER in one call; nothing pauses and nothing can be entered. `Declared` exists as a deferral band
(`verb_table.yaml:807`), which is the hook a pause would use.

**No GM.** What still needs one: deciding to go to war and where (MB-08); choosing an order of battle for
a faction with real sites (the preset doctrine is a fixed split); interpreting a stalemate (R-03);
deciding what a beaten army does (R-11); pricing a retreat.

**Conflicts with ruled items, named and not resolved.**

1. *Friction at sigma 1.1* (`ED-MB-0016`, closed at `ED-MB-0080`) against "choices change what happens".
   Measured here: a 3:2 advantage in spearmen wins 10 of 20; a 5:1 advantage wins 47 of 60. The curve is
   the one Jordan calibrated to. A player's order of battle is worth less than one standard deviation of
   the draw. §11.
2. *Same-round resolution* (`ED-IN-0301`, Ask C (a)) against a defender's turn. Not in conflict once
   `Drawn` exists: the first engagement is still fought the round it is declared; later ones are new acts.

**Ordered work to close each gap:** §8 steps 1, 2, 3, 4, then 5.

**The played battle and the delegated battle (the stated intent).** There is no played battle. The
delegated one is the only one, which avoids Total War's two-answers failure by having one answer and
fails the intent by having no play. The built precedent for adding the played mode without a second path
is the combat module's `decide` parameter; step 4a applies it at the engine's own phase boundaries. A
battle then has three choice points for a played side (deployment by the army Record and strategy, the
first phase boundary, the second) and, with `Drawn`, a decision between engagements. For a side nobody
plays the same decider slot is filled by the standing instructions (`fall_back_at`, `retreat_at`, the
strategy), which is the reference's "instructions set before the match".

## 10. Interfaces

| with | consumes | emits | real (executed) or designed |
|---|---|---|---|
| CORE (loop, seam, ladder) | `Act` (`march`, payload posture), the contest seam's call, the seeded `rng` | a result dict graded to Won / Lost / Unopposed / Invested; Events `field.*`, `army.arrived`, `siege.pressed` | executed when reached; reached 3 times in two seasons at seed 0, all `Unopposed` |
| CHAR (persons) | `Person.weight`, `stance` rows toward the faction, `is_cohort`, `body` as fitness | `body`, two stance rows per loser, a `broke` Observation | executed by hand-built acts; the loyalty row is read as zero in every built realm (H-256) |
| FA (factions, seats) | `Act.via` → `seat_faction`; `holder_faction_of`; `leaders` for presets; standing orders held by seats | grudge rows toward the winning faction | executed; a faction's reason to march is absent (designed, MB-08) |
| SE (settlements, sites, stores) | `fortification_of` (garrison condition); `training_sites`; `Rung.stores` through `settlements.provision` | `Site.condition` wear on `Invested`; `stores` debits | fortification executed; provisioning and siege built and off; no training site exists in the built realm, so the recruiting rule reads zero for every trained type |
| WR (geography, territory) | the geography file: terrain polygons, rivers, province anchors | presence at a territory (occupation) | executed for terrain and river rows; territory occupation executed (`field.unopposed`) |
| PC (personal combat) | nothing | nothing | **no edge.** A commander is not a body on the field; a duel cannot occur inside a battle; `detain` is read (prisoners do not muster) and never written by a field |
| SC (social contest) | nothing | nothing | no edge; `surrender` is an act, not a contest; a parley before a field does not exist |
| FI (fieldwork) | nothing | Events an investigator could find | designed only |
| DICE | none of the substrate: the module owns its own `roll_pool` and `compute_degree` | | doubled (§4.1) |
| GO (port) | | the largest float-dynamics body in the tree | not started; §9 |

## 11. Survivors for Jordan

Two. Each is listed because the brief requires it, not because the ladder left it open.

1. **CR-12: do troop numbers stay in the melee dice?** This lane's resolution is (a) (§5.3, R-06,
   proposal `04_MB_cr12_linear_law.md`), reached at ladder step 1. It is listed because it narrows the
   plain words of a standing directive (2026-07-08: pools "solely from the subunit troop type, quality
   and numbers").
   - *(a) Numbers out of the dice.* Melee is linear: a bigger army wins by overlapping, enveloping and
     outlasting. Battles between unequal armies last longer and the smaller side can hold a line; depth,
     reserves and frontage become the decisions.
   - *(b) Numbers stay in the dice; the linear lock is lifted for melee.* The engine stays as built
     (exponent 1.5 to 1.7): the bigger army also hits harder per man in contact, so size snowballs,
     battles between unequal armies end fast, and concentration beats positioning.
2. **Friction at sigma 1.1 against the standing requirement of 2026-11-12.** A conflict between a ruled
   magnitude and a new requirement, named and not resolved here.
   - *(a) Keep 1.1.* War is a gamble calibrated to the historical win-rate curve; the game is about
     whether to fight, and with what odds, not how. The choice surface that matters is then the decision
     to march, the estimate and the exit, and proposal 3 is built for that reading.
   - *(b) A smaller draw at the season's scale, or one a commander's capability narrows.* Composition and
     orders become legible causes of victory; upsets become rare enough to be stories. This is the
     reading §14 would feed (a commander's capability as the thing that narrows the draw).

Nothing else survives. The scale (H-250), the grading of a stalemate (H-354), `side` against `person`
(H-359), what a beaten side does (H-355), the role menu (H-361, A5) and MB-08's march half are all
answered in §6.2.

## 12. Evidence log

All runs: Python 3.13.18 (the container's; CI is 3.11), `PYTHONHASHSEED=0`, read-only. Scripts and outputs
are under `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/MB/`.

| run | seed, size | outcome |
|---|---|---|
| `python -m engine.season.harness.register --requirements` | n/a | met 3, not_met 1, partial 5 (`requirements.txt`) |
| `python -m engine.season.harness.aperture 2 0` | `build_realm(0)`, 2 seasons | `march` formed 26, attempted 13 and 12, refused 10 and 12; `field.unopposed` 3, `army.arrived` 3; `field.won`, `field.lost`, `siege.pressed`, `place.surrendered`, `order.marshaled`, all `army.*` never emitted; army verbs, `marshal`, `surrender` formed 0 (`aperture_2_0.txt`) |
| `reach_probe.py side 3` | module, seeds 0 to 2 | 1,363 of 4,634 statements; all three fields `Failure`, attacker 0.3 |
| `reach_probe.py side,side_big,person,orders,oob,oob_one 4` | module, seeds 0 to 3, six arms | 2,295 of 4,634 statements; per-file table in §4.2; a defender share of 1.08 on the headcount path (`reach_all.txt`) |
| inline: `_weighted_unit` pairs through `run_battle` | seeds 0 to 19; 30 v 18, 30 v 6, 99 v 1, 120 v 60, 150 v 60, 250 v 120 at k 1; 30 v 18 at k 10 | below 100 a side: both routed at tick 2, attacker loses 20 of 20, attacker hp untouched; 120 v 60: defender alone routed, tick 2, 20 of 20 |
| inline: losers above 1.0 | seeds 0 to 99; 600 v 120, 600 v 150, 450 v 190, 1200 v 199 | attacker wins 289; losing defender above 1.0 in 70; worst 1.638 |
| `walls_probe.py 60` | seeds 0 to 59, five size pairs, open and walls at DR 3, 1, 0 | open: 5:1 78%, 2:1 62%, 1:1 42%, 4:1 78%, 1:2 25%; walls DR 3: 45%, 40%, 30%, 58%, 13%; DR 0 equals open (the control) |
| inline: preset armies meeting | seeds 0 to 19, army path | levy 900 (`Reserve`) v levy 600: 6 `Success`, 14 `Partial`, survivors 0.98 and 0.96; levy 900 v a headcount side of weight 20: 3 wins of 20; spearmen 900 v 600: 10 of 20 |
| `presets_probe.py 0 2 control` and `... presets` | `build_realm(0)`, 2 seasons | control: `field.unopposed` 3, hash `bacd687f`; presets: three levy armies (600, 900, 600), the same events, hash `0622a841` |
| `seed2_field.py 2 1` | `build_realm(2)`, 1 season | one `field.lost`; bodies 1000 → 20 (two), → 30 (two), → 400, → 225 |
| `python -m engine.season.harness.corpus_run` | 143 cases, seed 0 | `march`, `marshal`, `surrender`, `recruit`, `form_unit`, `assign_troops`, `order_unit`, `disband_unit` and `discharge_troops` are all among the 30 rows "foldable but never even attempted"; no field of any band is resolved in the corpus (`DEGREES RESOLVED` lists no `Won`, `Lost` or `Unopposed`) (`corpus_run.txt`) |
| `presets_probe.py 0 2 tpw30` | | **failed to run**: the probe could not replace a fixture value on a built world; not retried |

**How the code was read.** Read in full, as written: `massbattle.py`, `armies.py`, `armyrecord.py`,
`orderofbattle.py`, `troop_types/` (three files), `rngsource.py`, `core/attrition.py`,
`engine/season/seam/wrappers/mass_battle.py`, `loop/effects_army.py`, `loop/sides.py`,
`harness/army_presets.py`, `harness/military_menu.py`, `effects_combat.py:380-770`,
`seam/ladder.py:190-272`, and `config.py:1-380`. Read in full **with comments and docstrings stripped**
(original line numbers kept): `config.py:380-626`, `battle_loop.py`, `orchestration.py`,
`hierarchy/units.py`, `geometry.py`, `percell.py`, `resolution.py`, `terrain.py`, `core/contact.py`,
`core/exchange.py`, `core/state.py`, `equipment/`, and `perimeter.py:1-100`. The comment prose in those
files was read only where a finding cites it.

- `[SKIPPED: tests/valoria/test_*.py and engine/season/tests/test_cp_t04_*.py (43 files) — not opened; §4.5 rests on the hole register's statements about them and on the code they test]`
- `[SKIPPED: systems/mass_battle/sim/bat.py, stress.py, validators.py, lanchester_signature.py, test_persubunit_stress.py, workbench/server.py, rout_cascade_sweep.py — outlines only; walkthrough.py:120-172, workbench/trace.py:60-116 and engine.py:284-303 read]`
- `[SKIPPED: perimeter.py:100-173 — not reached by any season arm]`
- `[SKIPPED: proposals 2026-09-25-squad-engagement-*, 2026-10-16-troop-stock-design*, multiunit_envelopment_plan.md, pc_formation_system.md — Status lines only (dossier); none is RATIFIED]`
- `[SKIPPED: research/pre_firearms_formations/, research/historical/, research/emergent_narrative_literature/, the companion parts — relied on research/by_lane/MB_mass_battle.md's reading of them]`
- `[SKIPPED: .designs/ mass_battle_v30.md and mass_battle_integration_v30.md — reference only; no finding depends on them]`
- `[SKIPPED: hole-register rows H-148, H-149, H-175, H-241 in full — excerpts and citing rows only]`

## 13. Provided arcs and characters — adjudication

Cases were selected by reading every `season_requires` need in `engine/season/cases/` for one whose
mechanism is a field, an army, a siege or a military command. "Represented" means reached in a run, not
declared. The corpus instrument itself reaches none of it: `corpus_run` (143 cases, seed 0) attempts no
`march` and no army verb in any case, so every "yes in mechanism" below rests on the module and realm
probes of §12, and none on the corpus. Proposal numbers: 1 = `04_MB_headcount_grade_and_scale.md`, 2 =
`04_MB_typed_outcome_and_one_path.md`, 3 = `04_MB_playable_field_scenario.md`.

| case | need (short) | hardness | represented today? | evidence | change required | owner lane | proposal | gate |
|---|---|---|---|---|---|---|---|---|
| ARC-07 The Army That Stayed | a rare combat sub-outcome leaves consequences for seasons after the battle | core | **in part.** A lost field leaves a morale row that lowers the next morale-start, and cut bodies until `tend` | `massbattle.py:158-159`; `effects_combat.py:639-644`; seed-2 run (bodies) | the rare branch must cross the seam: `FieldOutcome` carries each part's `routed` and `broke_first`; ship `person` | MB | 2, 1 | a folded field in which one of two commanders routs leaves the two with different bodies and only one named `broke` (the existing CP-T04-01 falsifier, on the shipped arm) |
| ARC-07 | a persistent condition on a unit, not cleared by the battle ending or a declared victory | core | **in part**, as above; nothing persists for a *winner* except his casualties | `effects_combat.py:570-587` | none beyond R-22's inverse (a win clears a row); the arc's own reading puts the condition in the men's ledgers, not on a unit (`proposals/2026-08-30-arc-reachability/01_arcs_01_18.md:303-320`) | MB, CHAR | 3 | a faction's morale-start after lost, lost, won reads 4, not 3 |
| ARC-07 | the commander's stated reason for staying is true and self-serving | core | no | a won army arrives and nothing says why it stays (H-355) | R-11; the reason itself is a claim, CHAR's | CHAR (claims), MB (aftermath) | 3 | after `field.won`, the occupying force's presence is a fact a `tell` can carry |
| ARC-07 | resolving the condition needs a distinct act nobody wants to start | core | **yes in mechanism**: `forgive` and `tend` are distinct acts | `effects_combat.py:766-847` | none in MB | CHAR | | [UNVERIFIED: whether the chooser forms `forgive` on a faction] |
| ARC-07 | the condition is invisible to outsiders until investigated; becomes a standing drain | important | no (no upkeep; stores debit is off) | `fixtures.py:809` | provisioning on; an occupying army eats (H-212) | SE | | SE's |
| ARC-23 The General Falls | battle phases within a turn; a stabilising act in one phase only | core | no. The engine has three phases; the season call is atomic | `battle_loop.py:459-461`; `massbattle.py:427` | engagements as rounds on `Drawn`; a personal act between rounds | MB then PC, CORE | 3 | a `Drawn` field followed by a second `march` the same season resolves a second engagement on the survivors |
| ARC-23 | a commander's incapacitation penalises the whole force and removes a morale floor | core | no. Command is the constant 4; the commander is not on the field | `massbattle.py:184-188`; `battle_loop.py:411-413` (unreached) | command as an input read from the commander (§14); his `body` as its fitness | MB, CHAR | §14 | equal armies, one commander at half body: win share differs beyond sampling error |
| ARC-23 | failing to stabilise escalates next turn; capture instead of death | core, important | no | no `detain` is written by a field | a field's `FieldOutcome` names the losing commander; `capture` is PC's verb | PC | | PC's |
| ARC-23 | a threat that exists only because one person maintains it dies with her | core | not MB's | | | CHAR, FA | | |
| ARC-43 The Battle That Ate the South | a field is triggered because another arc drew the defenders away | core | **yes in mechanism.** An empty defence is `Unopposed`; a thin one is fought thin | `seam/wrappers/mass_battle.py:391-414`; `aperture 2 0` (`field.unopposed` 3) | someone must decide to march there (step 5) | CORE, CHAR | 3 | a seeded run in which a march elsewhere empties a garrison and a second faction's march on it is `Unopposed` |
| ARC-43 | reality-altering ability inside a battle costs a fixed multiple | core | no. No personal act occurs inside a field | | rounds (proposal 3) first; the multiplier is WR's fixture | WR, PC | | WR's |
| ARC-43 | the battle's outcome degrades adjacent territories and a remote group | important | no | | WR reads the band Event | WR | | WR's |
| SCN-14 personal action inside a mass battle | one personal act per unit of mass-scale time | core | no | the call is atomic | rounds on `Drawn`; one act per round is DELIBERATE's budget | MB, CORE | 3 | as ARC-23's first gate |
| SCN-14 | acting personally suspends that actor's command for the same unit of time | core | no; and wrongly stated for this engine: "command" is not something a person exercises during a field today | | with §14's commander input: a commander who spent his round on a personal act contributes no command to that engagement | MB, CHAR | §14 | |
| SCN-14 | a named NPC targeted during the battle changes status at the mass scale | important | no | | `FieldOutcome.parts` names persons; the inverse (a person's state into the next engagement) is the fitness read that already exists for cohorts (`_order_of_battle`: `body / condition_scale`) | MB | 2 | a commander wounded between engagements fields a smaller subunit in the next |
| SCN-14 | a social contest before the round changes the round's starting state | important | **in part**: stance toward one's faction sets morale-start, and a contest can move stance | `massbattle.py:121-159` | none | SC | | a `tell` that lowers stance before a march lowers that side's morale-start |
| SCN-14 | zone movement during mass combat | flavour | the engine's field is cells, not zones | | none: a different abstraction, not required | | | |
| ARC-20, ARC-45 | whether one military leader commits her forces decides the battle, and can go either way on the same facts | core | **yes in mechanism**: an army fights only where its commander is | `seam/wrappers/mass_battle.py:206-214` | her choice is a `march` the chooser must form (step 5) | CHAR, CORE | 3 | the same world with and without her present reads different `orders_of_battle` |
| ARC-45 | a demand coincides with capacity depleted by a separate battle | important | **yes in mechanism**: cohort bodies carry losses into the next muster | `seam/wrappers/mass_battle.py:212-214` | proposal 2's per-cohort shares make it exact | MB | 2 | two fields a season apart: the second army's strength is the first's survivors |
| ARC-11 | a commander's redeployment leaves another place exposed | important | **yes**: `march` relocates the claimants; the origin's muster is then empty | H-355's measurement (`mustered(set_s_014)` empty after the march) | none | | | |
| NPC-070 Lisbeth Ehrenwall | a military institution reassesses loyalty in stages; diplomacy changes its deployment | core, important | not MB's mechanism; MB reads the result (loyalty rows into morale-start, which today read zero: H-256) | `seam/wrappers/mass_battle.py:134-138` | H-256 decided (CHAR) | CHAR | | CHAR's |
| NPC-072, NPC-082 | a named commander commands forces distinct from the council; his break has material consequence | core, important | **yes in mechanism, dark**: the army Record's holder is its commander; if he leaves the faction he can no longer command it (`effects_army.py:40-42`) and the army fights only where he stands | `effects_army.py:34-42`; `test_army_verbs.py` (not opened) | presets on (step 5) so the commander exists in a built realm | MB | 3 | in a seeded realm with presets, the commander's absence leaves his faction's side a headcount line |
| NPC-089 | three graduated postures: probe, pressure, invasion | core | **in part**: `storm` and `besiege` exist as postures; `besiege` is off the roster; nothing lighter than a siege exists | `rosters.yaml:1159-1176` | `besiege` on (it waits on `restore` executing, the roster's own condition); a probing posture is a new roster member and a design call for FA | FA, MB | 3 | `march_postures` of three members fans three candidates, each folding a different band |
| NPC-006 | a faction's military posture moves gradually by his acts | important | **in part, dark**: the army verbs change the Record by increments | `effects_army.py` | step 5 | MB | 3 | |
| ARC-47 | losing two territories in a period fires a trigger | important | MB supplies the fact (`field.*`, occupation); the trigger is not MB's | | | FA, CORE | | |

**Needs wrongly stated.** SCN-14's "mass-scale command capability ... SUSPENDED" presumes a commander who
acts during the battle; in this engine command is a property of the side fixed before the field. The
faithful reading is the one in the table (a commander's attention is spent or not per engagement).
ARC-07's "condition on a unit" is refused at the signature by the season's design (no unit object); the
arc-reachability reading (claims in the men's ledgers) is the one the code can carry, and the need should
be read that way. NPC-006, NPC-082 and NPC-089 each carry an UNCLEAR need about which territory or what
forces the person commands; under `ED-IN-0306` the answer is data: the army Record he holds.

**Arcs this lane can bring up soonest, in order.**

1. **ARC-11 and ARC-43's trigger** (a redeployment exposes a place; a field happens because the defenders
   left): nothing but step 5's march candidate, which is CORE's and CHAR's. Edge: CORE → MB.
2. **ARC-45 and ARC-20's battle half** (depleted capacity; one commander's commitment decides): steps 1,
   2 and 5. Edge: MB → CHAR for her decision.
3. **ARC-07** (the aftermath of a battle nobody chose): steps 1, 2, 6, then CHAR's claims and SE's upkeep.
   Edges: MB → CHAR, MB → SE.
4. **NPC-072, NPC-082, NPC-006** (commanders whose command is material): step 5.
5. **ARC-23 and SCN-14** (a person's act inside a battle): steps 2, 4, then §14 and PC. These are last:
   they need the round structure, the commander input and a duel that can target a commander, and no
   precedent in the corpus solves the seam (§7, nulls). Edges: MB → PC, MB → CORE, CHAR → MB.

The execution artifact for each is a seeded realm run in which the beat occurs from persons' acts; none
of the gates above uses a hand-built `Resolution`.

## 14. Capability authoring surface

**(a) Where mass battle takes a character capability as input.** Nowhere. `MassBattleInput` carries
weights, stances, loyalty rows, place and orders (`queries/inputs.py:205-260`); no field is a capability
or an attribute. `march` has no row in `rosters.yaml: verb_capability` (its rows are `tell`, `speak`,
`argue`, `research`, `examine`, `surveil`, `fight`, `accept`, `capture`). Inside the module the places a
capability *would* enter are constants:

| quantity | what the engine reads | where it comes from today |
|---|---|---|
| Command (span of control; a whole-side rout at 0; the cascade and recall rolls) | `Unit.command` | the literal 4 (`massbattle.py:184-188`, `orderofbattle.py:75`) |
| Command derived from a leader | `derive_command(charisma, cognition)`, weights 2 and 1 | `config.py:528-529`; called only when a harness builds a `Unit` with both (`units.py:2862-2863`); never by the season |
| troop quality: Power, Discipline, Morale | `Subunit.power`, `.discipline`, `.morale` | `TROOP_TYPE_STATS`, a Python dict (`troop_types/registry.py:44-71`) |
| the side's baseline quality | `Unit.power`, `.discipline` | the literals 4 and 5 |
| morale at the start | `_morale_start` | stance rows: data, the one live personal input |
| what a role does | `ROLE_SPEC`, `TROOP_TYPE_ROLES` | Python dicts (`config.py:589-626`) |
| who may be recruited as what | `TRAINING_SITE`, `TROOPS_PER_WEIGHT`, `MUSTER_FRACTION` | Python constants (`troop_types/recruitment.py:44-69`) |
| officers | `Officer.command` | harness only; "bookkeeping only" at resolution |

**(b) Data-driven, hard-coded, doubled.** Data-driven: morale-start (stance rows), the order vocabulary
(exported to `engine/engine_params/battle_orders.json`), the army Record. Hard-coded: everything else in
the table. Doubled: Command (a literal on two constructors plus an unused derivation with its own
weights); the troop-type table is a second, parallel "what a kind of fighter is" beside the person-scale
attributes, with no declared relation between them.

**(c) Target shape.** The existing owner is the pair `rosters.yaml: verb_capability` (verb → capability
key) and `vocation_attribute` (key → attribute), read through `seam/wrappers/sigma.py::faculty`, over
`Person.capability` and the ten attributes of `references/descriptor_registry.yaml`. Mass battle should
extend that, not add a scheme:

1. `march` gets a `verb_capability` row naming a command capability (the name is Jordan's content; a
   new vocation key, with its `vocation_attribute` row, both data).
2. `field_input` reads the commander's `faculty` for that key by the same function every other provider
   uses, and hands it on as `MassBattleInput.command = (attacker, defender)`, each an integer on the
   engine's 1 to 7 Command scale, with the literal 4 as the value for a side with no commander. The
   commander is the army Record's holder, or on a headcount side the acting person.
3. The module uses it where it already uses `Unit.command`. `derive_command` and its two weights are
   deleted: the derivation from attributes belongs to `vocation_attribute`, once.
4. Troop quality stays a property of troop type, authored as data: `TROOP_TYPE_STATS`, `TROOP_TYPE_ROLES`,
   `ROLE_SPEC`, `TRAINING_SITE` and the two recruiting numbers move to one typed file under
   `engine/engine_params/` behind an exporter, as the order vocabulary already is.

**What a capability definition must say for mass battle to use it** (the interface for the holistic
stage): its key; that it is read at the *side* scale through one person (the commander); the integer
scale it lands on and the value for "none"; which engine quantity it feeds (Command, and nothing else at
first); and whether it is consumed (a commander who acted personally this round contributes none:
SCN-14). Mass battle needs **one integer per side per engagement**, supplied by the host. It does not
need to see the capability, the attribute or the person.

**(d) Axioms.** Implemented, in the tradition's words: a dice pool of d10s against a fixed target number
with exploding-style double successes and botches on 1 (`resolution.py:37-54`); opposed rolls graded by
margin into four degrees; unit stat blocks by troop type (Power, Discipline, Morale); morale as a track
that erodes and breaks; formation, facing and flanking as positional modifiers; fatigue; ammunition;
conditional orders. Contradicted or lacking, that a designer would expect:

- **Leadership does nothing.** The commander's skill is the classic input to mass combat and here it is a
  constant.
- **No advancement.** Troops do not gain experience from a field; a veteran and a recruit of one type are
  identical. (`train` raises a person's capability; nothing raises a cohort's.)
- **No hero on the field.** A named character adds his `weight` (one household) and nothing of what he
  can do; the corpus calls this the fully fused pole (D_T04 row 50).
- **Two unrelated stat systems.** Person attributes and troop stats share no scale and no derivation.
- **The degree ladder and the die roller are re-implemented** in the module rather than read from the
  substrate (§4.1), so a change to the axiom at its owner would not reach a battle.

**(e) Proposals, ordered.** (1) Command as a host-supplied integer, with `march`'s `verb_capability` row:
part of `04_MB_typed_outcome_and_one_path.md` (the input record) and §8 step 8; it waits on CHAR's
decision of the capability's name. (2) The troop tables as one exported typed file: same proposal,
R-08's sibling. (3) The module's `roll_pool` and `compute_degree` forward to the substrate's owners, a
DICE-lane edit recorded here and not proposed. No private capability scheme is proposed.

**Addendum (the stated intent: individuals' attributes feeding unit performance).** The interface stated
above (one integer per side per engagement, Command) is the minimum. The reference asks for more than the
commander: officers and soldiers as characters. The tree already has the carriers and no new scheme is
needed: an `Officer` per subformation is a person holding a post in the army Record (a `(subformation,
person)` pair in `subject_matter`, a record-kind change); a cohort's training is a capability on the
cohort `Person` (`train` already raises `Person.capability`), read as a bounded step on the troop type's
Discipline. Both are host reads handed in as integers on `MassBattleInput`; the module still sees no
person. Order: Command first (it is the one the arcs need), officers second, cohort training third.

## 15. Duels in and around a mass engagement (Jordan's personal-combat intent, 2026-11-12)

**Where a duel is embedded in or arises from a mass engagement today: nowhere.** There is no edge between
the two modules (§10). The combat entry is `modules/combat/fight.py::fight(inp, rng, decide)`, reached
through the `the body` prize; `decide` is the PLAYABLE per-turn decider and `None` is the automatic loop,
so that module already has the two modes on one path at the granularity of a whole fight. The mass-battle
provider accepts the same `host` keyword and ignores it (`seam/wrappers/mass_battle.py:361-363`). Nothing
in `resolve_field` knows a person as a fighter: a named character is one unit of `weight`.

**Where one should arise, by the code's own shapes.**

1. **A field between individuals is not a mass battle.** The realm's actual fields are two to six named
   persons a side at weight 1 (§1.3: the seed-2 field is two against three). `resolve_field` turns them
   into two "troops" against three and the engine, calibrated for hundreds, returns a constant. This is
   the Final Fantasy Tactics case exactly: a handful of characters on a grid. The resolver that knows what
   a character can do is the duel round. So the scale decides the module: **a side with no cohort member
   and no army Record is a squad, and a field between two squads belongs to personal combat's grid mode**;
   mass battle begins where a side fields a block. R-01 (one weight to troops owner) makes the present
   path coherent in the meantime; it does not make two men an army.
2. **Between engagements.** With `Drawn` (R-03) a field can run to a second engagement; the round between
   is where a `fight` on the enemy commander, a challenge, or a `capture` is an ordinary act through the
   ordinary combat seam. Its result re-enters the battle through inputs that already exist or are proposed:
   the commander's `body` as his subunit's fitness (`_order_of_battle` reads `body / condition_scale`
   for cohorts today) and Command (§14). ARC-23 and SCN-14 are this shape.
3. **At the end.** A routed side's commander is the person a pursuing victor could `capture`; the custody
   edge exists and a field never writes it (§5.5). That is a `capture` act offered on `field.won`, not a
   rule inside the battle.

**Can mass battle's own resolution call the duel-round path instead of being a second resolver?** In two
places yes, in one no.

- *Squad scale: yes, and it should.* The host adapter, not the module, pairs the claimants and calls
  `contest()` on `the body` for each pairing, through the registered combat provider. No module calls
  another; the row decides. This removes the mis-scaled battle instead of re-tuning it.
- *Persons at a mass battle: yes, by composition between engagements* (item 2), never by a call from inside
  `run_battle`.
- *The cell exchange: no.* A cell is 40 to 200 men; `resolve_engagements` resolves pooled strength over a
  frontage with an attrition term. That is a different quantity from a duel and running four hundred duels
  per contact would be a second, worse model of the same thing. What must be one is the *axiom*, not the
  call: both scales should grade on the substrate's ladder and roll the substrate's die (§4.1 records that
  mass battle re-implements both).

**The approach lever is the same lever at both scales, with two vocabularies.** Personal combat's intended
choice is aggressive, normal or defensive per phase. Mass battle already has it: stance `aggressive`,
`balanced`, `hold` (`config.py:286`, a signed commitment on offence and defence, "intent as resolution"),
army strategies `advance`, `line`, `defend` (`orderofbattle.py:53-57`), and a per-phase carrier
(`Order('tick:N', {'stance': ...})`, three phases of six ticks). For the calculations to be "consistent in
methodology" (NERS-S) the approach roster should have one owner read by both modules, as the order
vocabulary is exported today; proposal 3's between-engagement choice is that roster's three values.

**Shared geometry.** If personal combat's grid needs facing arcs, reach and contact, the owners exist in
`modules/mass_battle/geometry.py` (`octagon_angle`, `reach_reaches`, `CellBody`). A second module may not
grow its own copy; the primitives would move to `engine/substrate/` [UNVERIFIED: whether Layer 1 permits
one registered module to import another; the tree shows no instance].

**Conflicts with ruled items, named and not resolved.**

- *"One engine at every fidelity"* (2026-07-08) against a dispatch by scale. The ruling is about the played
  and the automatic resolution of the same battle; a squad fight and a battle are different contests.
  Read that way there is no conflict; if the ruling is read as "every `march` goes to the mass engine", the
  squad dispatch contradicts it.
- *`04` §C.5.1, "units = PersonId[] at weight — one type"* against "a side of individuals fights
  differently from a side with a cohort". `Person.is_cohort` already separates the two for duels
  (CP-T03-01, cohorts never fight a duel), so the distinction is in the tree; using it to pick the module
  is new.

**What this lane owes the PC lane:** the scale rule (which fields are squads), `FieldOutcome` naming the
losing commander, the round structure, and the approach roster's single owner. It owes no resolver.

## 16. NPC-facing and chooser-facing surface

The statement of the NPC and chooser intent is the CHAR lane's (`audits/02_CHAR_audit.md`); its section on
the intent was not yet written when this was, so this section cites that audit's findings as they stood
(F-CHAR-01, "the ranking does not read what an act would do"; F-CHAR-05, "four in ten resolved acts are
refusals the actor could have foreseen") and reads the mass-battle surface against the code.

**(a) Who decides, on what, at what budget, with what visible reasons.**

| decision | who | information | budget | what is visible afterwards |
|---|---|---|---|---|
| to march, and where | a person holding a seat whose remit grants `march` (26 persons at seed 0, `aperture 2 0`) | the Rungs his questions name; no estimate, no knowledge of the defence | one scene | `march.declared`, then the band Event |
| how to meet the enemy (storm, besiege) | the same act's payload | none | the same act | the posture in the act's payload |
| the standing order (retreat line; today also a role) | a seat, by `marshal` | none | one scene; withheld | an `order_of_battle` Record, which persists |
| what the army is (raise, form, assign, order, disband, discharge) | the army Record's holder | the menu's bounds and advisories (`armyrecord.options`) | once per verb per season through the callback; withheld | `army.*` Events; the Record |
| to yield a place | the defender's seat, by `surrender` | none | one scene; withheld | `place.surrendered` |
| anything during the field | nobody | | | |
| to fight or not when marched on | nobody: the defender has no turn | | | |

**(b) One interface for player and NPC.** Structurally yes: `play_surface.dispatching_chooser` hands a
person either to a client callback or to `auto`, and `military_menu.callback` rides it; the army verbs are
acts either would give. Two breaches. The estimate is the player's alone (`field_estimate`, "no NPC reads
it"): the player and the NPC are then not the same kind of agent at the one moment that matters. And the
non-player's army is not raised through the chooser at all (F-MB-16).

**(c) Rules hard-coded for NPCs instead of read from the chooser.** The preset doctrine and its role table
(`troop_types/presets.py:37-50`); the direct fold in `army_presets.install`; the stand-in troop type for a
side with no army (`massbattle.py:355`); the fixed deployment rule (`orderofbattle.py:15-19`); the
defender's absence of any decision. None is keyed to an entity, so none is scripting drift in the narrow
sense; all are one policy standing where a person's choice should be.

**(d) What would make an NPC characterful here, and legible afterwards.** Three closed sets already exist
as payload choices and are scored alike because the chooser keys on `(verb, subject)`: posture (`storm`,
`besiege`), retreat line (`none`, `0.5`, `0.25`), strategy (`advance`, `line`, `defend`). A bold commander
and a cautious one differ exactly on these. They need cells on the *value*, not only on the verb, which is
the pursuit worksheet's and CHAR's to own. Legibility: the standing order is a Record and the posture is
on the act, so "he ordered no retreat and stormed the walls" is already recoverable; what is not is why
(the score terms) and what he believed the odds were.

**(e) Missing, as proposals.** In `04_MB_playable_field_scenario.md`: the doctrine as a named choice
through the chooser (step 5a); the estimate on believed strength (step 5b); the phase decider slot filled
for a non-player by standing instructions (step 4a). Owed by CHAR and named here as the dependency: cells
on fanned payload values; the reason trail.

**Disagreement between sources, named.** AQ-X1 as recorded in the code ("no NPC reads" the estimate)
against the charge's "the player and NPC are the same kind of agent". The built rule wins today. Step 5b
does not let an NPC read the world's odds; it lets him compute odds on what he believes, which may satisfy
both. Whether it does is CHAR's reconciliation.

## 17. Against the stated design intent: Football Manager and Total War

"Understood" means the mechanism is built and reaches a season outcome under some shipped or switchable
arm; "named" means the vocabulary exists and the behaviour does not.

| what the reference is known for | in the code | verdict |
|---|---|---|
| **FM** a squad of individuals with roles, duties and instructions | `ROLE_SPEC` (15 roles, each a shape and an instruction package), `TROOP_TYPE_ROLES` (menus by troop type), `Subunit.instructions`; five keywords drive a primitive, seven do not (`units.py:71-101`); the army Record stores a role per subformation | **named.** Half the menu is inert and the live half is not a reliable lever (H-361) |
| **FM** instructions set before and adjusted during the match | before: strategy, stance, target preference, fall-back point, standing retreat line; conditional `Order`s with tick, range, strength and signal triggers (`units.py:312-390`, `core/contact.py:66-198`). During: nothing from outside the call | **understood before the match, absent during it** (F-MB-15) |
| **FM** the engine resolves automatically from settings and individuals' attributes | settings: yes. Attributes: none (F-MB-14) | **half** |
| **FM** watch, intervene, change tactics, substitute | trace exists for the workbench; reserves commit only in the multi-unit loop the season cannot reach (`orchestration.py:2219-2244`) | **absent in the game** |
| **FM** post-match analysis that explains the result | `resolution.tracing`, `walkthrough.py`'s page, `stress.py`'s analysis: harness only; the trace-cause design (A9) is "scoped down, not built" | **named** |
| **TW** formations and units on a battlefield | cells, footprints from troops and density, four shapes, multi-subunit deployment with wings and a rear line (`orderofbattle._place`) | **understood** |
| **TW** terrain | six rows derived from geography (`terrain.py:66-75`): walls, uphill and river crossing act; forest's speed half is inert and narrow pass applies nothing on a one-engagement field (`massbattle.py:386-399`); terrain is a modifier on a flat field, not ground | **partly understood**: a row, not a map (the map generator is MB-08, LEAVE) |
| **TW** morale and routing | per-cell morale, local breaks that spread, a stochastic break band, contagion across subunits, whole-army rout by share broken (`core/state.py`, `units.py:2260-2353`, `:2928-2948`) | **understood**, and the strongest part; never runs at the shipped scale |
| **TW** flanking, charges, fatigue | octagon arcs as damage multipliers with a reaction delay, multi-side shock, charge momentum and brace recoil, per-column stamina | **understood** |
| **TW** supply | ammunition per subunit; a ration debit per field, shipped off; nothing on the march | **named** at campaign scale |
| **TW** a campaign layer that feeds the battle | morale from members' stance, walls from garrison condition, river from the march's origin, the army from a Record raised from population and sites, troops from stores | **understood**, dark |
| **TW** ... and receives its result | bodies by share, morale and grudge rows, presence, garrison wear | **understood**; the magnitude is wrong on the shipped path (F-MB-02); no captives, no title |
| **TW** fight or auto-resolve, kept consistent | one engine, one answer, no played battle; `host` accepted and unused | **consistent by absence** |

**Reconciling the existing material.** The squad-engagement synthesis (RULED 2026-09-25) is the tree's
Football Manager document and its build slate is executed; its concept input is recorded there as never
having read the repository. `08_mass_battle_units.md` (PROPOSED) asked for U-1 (inputs beyond headcount),
U-3 (wire roles or stop presenting them) and U-4 (officers as persons): U-1 is partly answered by the army
path, U-3 is R-10, U-4 is §14. The phase-5 design is built. `multiunit_envelopment_plan.md` is PROPOSED and
un-adopted; under F-MB-05's resolution its subject (several Units a side) leaves the registered tree, so it
should be re-read as an oracle item or closed. None of these conflicts with the resolutions in §6.2.

**Conflicts with ruled items, named and not resolved.** (1) Individuals' attributes driving the result,
against the 2026-07-08 directive that took the commander out of the pool (F-MB-14). (2) Intervention during
the match, against a field resolved atomically in the round it is declared (`ED-IN-0301`): the decider
inside the call does not move the round, so this lane reads no conflict; a reading of `ED-IN-0301` as "no
decision after declaration" would. (3) Legible cause, against friction at sigma 1.1 (§11 item 2): an
explanation of a result that was mostly the draw is an honest explanation and a poor one.
