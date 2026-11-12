# MB · a typed outcome, one code path, no hidden inputs

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` Part 2) — four changes. (1) **A-3**: `FieldOutcome.verdict` is withdrawn; the record carries the end state per side and the host reads the band (`04_MB_manager_battle_one_resolver.md` §1). `ended` and `turns` stand. (2) The list of roles and keywords that leave the menu (§2, fifth bullet) is merged with the pessimist's measured list into one: `U5b_MB_residue.md` §1. (3) §4's `MassBattleInput.command: tuple = (4, 4)` yields to the typed input A-59's carriers define (command from a learned skill and social and mental attributes; each unit's own prowess as columns of its row): `audits/27_MB_COMMAND_AND_DYNAMIC_STRENGTH.md` and `proposals/27_MB_*`, another lane's. (4) The outcome gains the fields later proposals add to it, each named by its owner: `rallied`, `pursuit_loss` and the dead / taken split (`16_PESSIMIST_MB_rout_has_two_exits.md`; `26_MASS_BATTLE_rout_pursuit_and_giving_ground.md`), `report` and `interventions` (the manager proposal). A-29 (declared floats) leaves §1's quantising of shares at the seam as written. A-1: §2's removal of the two unreached loops is Layer 1 §27.2 conformance, confirmed.

## Status: PROPOSED

Folded: 2026-11-12 by `audits/27_MB_COMMAND_AND_DYNAMIC_STRENGTH.md` (rulings A-59 and A-69). Nothing here is deleted. (1) The typed input the Reconciled line's item (3) points to is `CommandRecord` (trained score, addends, levels, post), one for each side's commander and one on each unit row for its officer, with `pool_add`, `pool_floor` and the task obstacle carried raw (`27_MB_A_command_and_the_obedience_draw.md` §2). (2) `FieldOutcome` gains `report.draws` (the named draws and their bands), and each part gains its end-state word and `stamina_left` (`27_MB_C` §3; `27_MB_E` §1, §4). (3) **§1's army-path write** ("each subformation's surviving fraction is applied to the troops each cohort assigned to it ... and summed per cohort", then written to the cohort's body) is the control arm under A-69. With `recuperation: on` the per-unit loss is written to the unit's row by kind, the cohort's body takes the dead share only, and strength is read from the row; the read and the write move in one commit so that no loss is counted twice (`27_MB_E` §2, gate 2).

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — rows applied: `R1_READ.md` §1.2 config row (AMBIGUOUS, shape divergence from PC) with 7b-13 and `U1_OWNERS_AND_VOCABULARY.md` D-U1-11c (§3: no context variable; `resolve_field` takes `cfg` as an explicit parameter as `fight(inp, rng, decide, cfg)` does; table-shaped content goes to `references/troops.yaml`, scalar engine constants stay literals in `config.py` exported to `mass_battle_v1.json`; `EngineConfig` is the typed in-memory reader of the two, not a home), §2 row A-29 (§1's share quantising is a seam choice, not an integer-state commitment), D-U1-11g / U1 §4 M-23 (§4's `MassBattleInput.command` integer is removed: `CommandRecord` of `27_MB_A` replaces it; §2's `rally_check` pointer follows), D-U1-06 (the draws and the broke-first fact ride `Event.observed` as `observation_terms` members), D-U1-11e (the one `FieldOutcome` field list); test 9 (order of edits, tests, lands-it, tier; `Depends on:` / `Lands in batch:`). U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "subformation" (a row of `subformations`) → "unit" in prose (glossary *unit*; the Record key keeps its name). MB lexicon lane (2026-11-12, `unified/MB_LEXICON_part3.md` S-3, D-7): `FieldOutcome.turns` (it counts field ticks; "turn" is A-9's and the duel's word) → `ticks` at its declaration and in the base-field list.

**Depends on:** `04_MB_headcount_grade_and_scale.md` (B17, first).
**Lands in batch:** B17 (`B17-mb-scale`, MB), with `U5b_MB_residue.md` §1: §1, §2 and §4 before `04_MB_unit_loadout_and_weapon_in_hand_B.md` stages 1–2 (UMR §6 rows 2 → 3); **§3 after them** (U6 R-A, `U3_DEPENDENCY_ORDER.md` §1.2: §3 moves table content into `references/troops.yaml` and reads `tools/export_troops.py --check`, which those stages create).

Lane MB (seam edits IN). Carries R-04, R-05, R-08, R-09, R-10, R-15, R-21 of `audits/04_MB_audit.md`
§6.2 and the first step of its §14. Reference, not mechanism (`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

The provider receives a frozen `FieldOutcome` instead of a `dict`, and `_eff_march` writes casualties per
cohort on the army path (today every cohort an army drew from is cut by the side's one share). Nothing
else moves a season: the code moves and deletions are hash-equal by construction, and the gate says how
that is shown.

## The problem (audit F-MB-05, F-MB-06, F-MB-09, F-MB-10)

- The entry returns a four-key `dict`, six on one arm (`modules/mass_battle/massbattle.py:465-470`,
  `:337-346`); `04`'s seam row asks for a typed output. How the field ended, how long it ran and, on the
  army path, what happened to each part are dropped.
- The registered tree holds two battle loops the season cannot reach (`run_multi_turn_battle`,
  `run_multi_unit_battle` and eleven helpers: 655 lines in functions no season arm enters, measured),
  and the interactive standalone surface defaults to one of them
  (`systems/mass_battle/sim/workbench/trace.py:73-91`).
- 91 environment variables read at import decide which mechanisms exist (`config.py` 66,
  `hierarchy/units.py` 12, `orchestration.py` 11, `core/exchange.py` 2).
- Dead: `systems/mass_battle/sim/tactic_cards.py`, `altonian_reinforcements.py`; three no-op functions
  called every tick or phase; seven instruction keywords with no primitive.

## The resolution, decided

### 1. `FieldOutcome` (owner: `engine/season/queries/inputs.py`, beside `MassBattleInput`)

```
@dataclass(frozen=True)
class PartOutcome:
    id: str            # a member's person id (headcount `person` arm) or a cohort's (army path)
    share: int         # survivors on the body scale: round(condition_scale x hp_left / hp_start), 0..scale
    routed: bool

@dataclass(frozen=True)
class SideOutcome:
    share: int                 # the side's survivors, same scale
    routed: bool
    conceded: bool
    parts: tuple               # PartOutcome, in input order; () on the headcount `side` arm
    broke_first: Optional[str] # the part id that broke on its own account first, or None

@dataclass(frozen=True)
class FieldOutcome:
    # (Reconciled, A-3) no `verdict`: the host's `field_degree` reads the band off the two sides' flags
    ended: str                 # 'rout' | 'concession' | 'time'
    ticks: int                 # field ticks run (the engine's `run_battle` returns them as "turns")
    attacker: SideOutcome
    defender: SideOutcome
```

Shares are integers on the exported body scale (`condition_scale` arrives on the input), so the seam is
the point where the engine's floats are quantised (`architecture/holonic_ARCHITECTURE.md` §48); quantised
at the seam, not an integer-state commitment (A-29: declared floats now). `__post_init__` refuses an
`ended` outside its set.

*(D-U1-11e.)* This file declares the base fields (`ended, ticks, attacker, defender`; the per-side and
per-part records). The other fields of the one `FieldOutcome` land each with its own proposal and are
declared nowhere else: `parts, report, interventions` (`04_MB_manager_battle_one_resolver.md`);
`rallied, pursuit_loss, taken, gave_ground` (`26_MASS_BATTLE_rout_pursuit_and_giving_ground.md`);
`stamina_left` (`26_MASS_BATTLE_movement_and_fatigue_as_data.md`); `fight_loss, bouts`
(`26_MASS_BATTLE_cell_scale_and_time.md`); `report.draws` (`27_MB_C`).

Army path: a part is a cohort. Each unit's surviving fraction is applied to the troops each
cohort assigned to it (`armyrecord`'s `assigned` rows, carried on `OrderOfBattle` as
`drawn: ((subformation, cohort, troops), ...)` in place of `drawn_from`), and summed per cohort.
`broke_first` is read from the engine's own order of breaking: `battle_loop.run_battle` appends
`(side, subunit index)` to a list on its return value when it first sets `routed` on a subunit while its
unit stands. `massbattle._PersonSubunit` and its property setter are deleted.

`_eff_march` (`engine/season/loop/effects_combat.py`) reads `outcome.attacker` / `.defender`: a person
named in `parts` is scaled by his part's share, anyone else by the side's. `broke_observed` is written
for both sides; it and the field's named draws (`draw:<name>`, `27_MB_C`) ride `Event.observed` as members
of `rosters.yaml: observation_terms` (D-U1-06).

### 2. One path

- `run_multi_turn_battle`, `run_multi_unit_battle`, `between_turn_recovery`,
  `reset_morale_between_battles`, `reset_positions`, `pursuit_damage`, `recall_check`,
  `feigned_retreat_recognized`, `feigned_retreat_check`, `resolve_feigned_retreat`, `unit_in_reserve`,
  `freed_attacker_damage` and `Unit.base_combat_pool` move from `modules/mass_battle/` to
  `systems/mass_battle/sim/multi.py`, beside the harnesses that call them (`engine.py::resolve_battle`,
  `bat.py`, `validators.py`). They import the module; the module does not import them.
- `systems/mass_battle/sim/workbench/trace.py::run_traced_battle` takes `kind='field'` as its default:
  it builds a `MassBattleInput` and calls `massbattle.resolve_field` under `resolution.tracing()`.
- Deleted outright: `orchestration.threadwork_check`, `Subunit.halt_before_enemy` and their call sites
  (the archived integration spec ordered `halt_before_enemy` deleted in May 2026; it is still called
  twice a tick). `rally_check` is **kept as the commander's hook, not deleted**: the same spec gives it a
  body (a Command check at each phase boundary restoring Morale toward its start), and it is where the
  commander's `command` capability on `CommandRecord` (`27_MB_A`; D-U1-11g) first does something; until
  that lands it stays the no-op it is. Also deleted: `tactic_cards.py`; `altonian_reinforcements.py` (each with its `FORK:` row in
  `references/restructure_ledger.md`, and the pointers at `registers/placeholder_names.yaml:73-88` and in
  `registers/mechanics_index.yaml`).
- `config.TROOP_TYPE_ROLES` and `ROLE_SPEC` lose the roles and keywords that resolve to no primitive
  (`Screen`, `Pursue`, `Harass`; keywords `pin`, `loose`, `screen`, `pursue`, `volley`, `shoot_move`,
  `harass`), per `hierarchy/units.py::ROLE_INSTRUCTION_PRIMITIVES`' own table. A role returns when a
  primitive exists for it.
- `massbattle.py`'s module docstring is cut to what the file is.
- The provider's `resolver="dice_pool"` key is dropped from its three return shapes.

### 3. No hidden inputs

- `modules/mass_battle/config.py`: every `os.environ.get(NAME, default)` becomes the default.
  *(Reconciled, W3-1: 7b-13, D-U1-11c.)* Each of the 91 reads goes to one of two owners, never both: a
  column of a row a designer edits (a troop, an arm, a terrain, a formation, a doctrine, a fatigue rate, an
  `orders.obey` step) moves to `references/troops.yaml`, exported to `engine/engine_params/troops.json` by
  `tools/export_troops.py --check`; a global engine coefficient stays a literal in `config.py`, exported to
  `engine/engine_params/mass_battle_v1.json` by a section of `tools/export_engine_params.py --check`; the
  loader refuses a name present in both. A frozen `EngineConfig` dataclass is the typed in-memory form of
  those literals (`config.DEFAULT`, the shipped instance), **passed to `resolve_field(inp, rng, *, cfg=None,
  troops_a=None, troops_b=None, decide=None, duel=None)` as an explicit `cfg` parameter**, as
  `fight(inp, rng, decide, cfg)` does in personal combat; there is no `config.active()` and no
  `config.using()` (no ambient selector: `04` §C.12 rejection 4, `hol` §47). `os.environ` is read only under
  `systems/mass_battle/sim/`, which builds a variant with `replace(DEFAULT, PER_CELL=False)` and passes it.
- `equipment/_base.py::Registry.override` and `remove` are deleted (no caller).

### 4. The first capability input (audit §14)

*(Reconciled, W3-1, D-U1-11g, U1 §4 M-23: the integer `MassBattleInput.command: tuple = (4, 4)` this
section proposed is removed. The commander's and each officer's `command` capability reaches the field as
`CommandRecord` (trained score, addends, levels, post), `27_MB_A_command_and_the_obedience_draw.md` §2; the
old integer and `core/exchange.py::derive_command` retire with it; `command_span`, the 1..7 span read off
the score, keeps its name.)* `config.CMD_CHA_WEIGHT` and `CMD_COG_WEIGHT` move with the harness code.

## Gate (execution artifacts)

1. The reach probe of the audit's §12, re-run: every function left under `modules/mass_battle/` is
   entered by a season arm or by one of the four query rows.
2. `git grep -n "environ" modules/mass_battle` prints nothing.
3. `python3 tools/ci_golden_modes_check.py`: the three field digests equal (the moves and the config
   object change no arithmetic).
4. A folded army field in which one unit routs and another holds leaves the cohorts that fed
   them with different bodies; a planted "side share for every cohort" reddens it.
5. `build_realm(0..2)`, one season: content hashes equal to the base at seeds 0 and 1; seed 2 moves only
   if proposal `04_MB_headcount_grade_and_scale.md` has landed.

## Falsifier

A season arm that enters a function now under `systems/`; a run whose outcome changes when an `MB_*`
variable is exported; an army field whose reserve cohort is cut as deeply as its line.

## Implementation (test 9, W3-1)

- **Order** (each its own commit): (1) `FieldOutcome` and the per-cohort write (gate 4's mover, declared);
  (2) the moves to `systems/mass_battle/sim/multi.py` and the deletions, each deleted file with its `FORK:`
  row (hash EQUAL, gate 3); (3) the config split and the explicit `cfg` (hash EQUAL); (4) roles and keywords
  (with `U5b_MB_residue.md` §1's merged list).
- **Tests.** Gate 3: `tests/valoria/test_field_golden_pins.py` and `tools/ci_golden_modes_check.py`;
  gate 4: `tests/valoria/test_mass_battle_army_record.py::test_routed_and_holding_units_cut_their_own_cohorts`
  with the planted side-share control; `engine/season/tests/test_mass_battle_module.py::test_resolve_field_returns_a_frozen_field_outcome`,
  `::test_ended_outside_its_set_is_refused`; gates 1–2 are the reach probe and the grep, in the commit body.
- **Hash movers:** step (1) on the army path only (no natural season fights an army field); the rest EQUAL.
- **Lands:** an IN-lane implementation session under `/methodology-execute` with MB review; the moves
  `haiku`-assisted for the mechanical edits, the record and config `sonnet`.

## NERS

- **N.** From the standing requirement's direction (one path) and the port's (one body of code to
  translate, not two), and from the narrative's: a battle that says which part broke gives the people in
  it something to hold against each other. Cut the typed outcome and the seam stays the one untyped
  return in the three providers.
- **R.** Completeness at the extremes: an army whose reserve never fought is no longer bled for it.
  Customisation survives: the oracle can still vary every flag, explicitly.
- **S.** The outcome is one shape on every arm (today: two). Shares are on the body scale the rest of
  the season uses.
- **E, last.** About 700 lines leave the registered tree and nothing is added but four small records.

## Cost class

Edit, large and mechanical (moves, deletions, one config object), plus a small build (the outcome
record and per-cohort shares). Hash equal except item 4 of the gate.
