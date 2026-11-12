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
