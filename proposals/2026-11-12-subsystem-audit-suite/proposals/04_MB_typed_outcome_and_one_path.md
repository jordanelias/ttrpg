# MB · a typed outcome, one code path, no hidden inputs

## Status: PROPOSED

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
    verdict: str               # 'won' | 'lost' | 'drawn'  (attacker's; proposal 04_MB_headcount_grade_and_scale)
    ended: str                 # 'rout' | 'concession' | 'time'
    turns: int                 # ticks run
    attacker: SideOutcome
    defender: SideOutcome
```

Shares are integers on the exported body scale (`condition_scale` arrives on the input), so the seam is
the point where the engine's floats are quantised (`architecture/holonic_ARCHITECTURE.md` §48).
`__post_init__` refuses a `verdict` or `ended` outside its set.

Army path: a part is a cohort. Each subformation's surviving fraction is applied to the troops each
cohort assigned to it (`armyrecord`'s `assigned` rows, carried on `OrderOfBattle` as
`drawn: ((subformation, cohort, troops), ...)` in place of `drawn_from`), and summed per cohort.
`broke_first` is read from the engine's own order of breaking: `battle_loop.run_battle` appends
`(side, subunit index)` to a list on its return value when it first sets `routed` on a subunit while its
unit stands. `massbattle._PersonSubunit` and its property setter are deleted.

`_eff_march` (`engine/season/loop/effects_combat.py`) reads `outcome.attacker` / `.defender`: a person
named in `parts` is scaled by his part's share, anyone else by the side's. `broke_observed` is written
for both sides.

### 2. One path

- `run_multi_turn_battle`, `run_multi_unit_battle`, `between_turn_recovery`,
  `reset_morale_between_battles`, `reset_positions`, `pursuit_damage`, `recall_check`,
  `feigned_retreat_recognized`, `feigned_retreat_check`, `resolve_feigned_retreat`, `unit_in_reserve`,
  `freed_attacker_damage` and `Unit.base_combat_pool` move from `modules/mass_battle/` to
  `systems/mass_battle/sim/multi.py`, beside the harnesses that call them (`engine.py::resolve_battle`,
  `bat.py`, `validators.py`). They import the module; the module does not import them.
- `systems/mass_battle/sim/workbench/trace.py::run_traced_battle` takes `kind='field'` as its default:
  it builds a `MassBattleInput` and calls `massbattle.resolve_field` under `resolution.tracing()`.
- Deleted outright: `orchestration.rally_check`, `threadwork_check`, `Subunit.halt_before_enemy` and
  their call sites; `tactic_cards.py`; `altonian_reinforcements.py` (each with its `FORK:` row in
  `references/restructure_ledger.md`, and the pointers at `registers/placeholder_names.yaml:73-88` and in
  `registers/mechanics_index.yaml`).
- `config.TROOP_TYPE_ROLES` and `ROLE_SPEC` lose the roles and keywords that resolve to no primitive
  (`Screen`, `Pursue`, `Harass`; keywords `pin`, `loose`, `screen`, `pursue`, `volley`, `shoot_move`,
  `harass`), per `hierarchy/units.py::ROLE_INSTRUCTION_PRIMITIVES`' own table. A role returns when a
  primitive exists for it.
- `massbattle.py`'s module docstring is cut to what the file is.
- The provider's `resolver="dice_pool"` key is dropped from its three return shapes.

### 3. No hidden inputs

- `modules/mass_battle/config.py`: every `os.environ.get(NAME, default)` becomes the default. A frozen
  `EngineConfig` dataclass holds the flags and magnitudes that the oracle varies; `config.DEFAULT` is the
  shipped instance; the engine reads `config.active()` (a context variable, as `rngsource` is) and the
  oracle harnesses scope a variant with `config.using(replace(DEFAULT, PER_CELL=False))`. `os.environ` is
  read only under `systems/mass_battle/sim/`, to build that variant.
- `equipment/_base.py::Registry.override` and `remove` are deleted (no caller).

### 4. The first capability input (audit §14)

`MassBattleInput.command: tuple = (4, 4)`, integers 1 to 7, read by the three constructors in place of
the literal. The host fills it when CHAR names the capability (`rosters.yaml: verb_capability` gains a
`march` row); until then the default is today's value. `config.CMD_CHA_WEIGHT`, `CMD_COG_WEIGHT` and
`core/exchange.py::derive_command` move with the harness code (the season's derivation is
`vocation_attribute`'s).

## Gate (execution artifacts)

1. The reach probe of the audit's §12, re-run: every function left under `modules/mass_battle/` is
   entered by a season arm or by one of the four query rows.
2. `git grep -n "environ" modules/mass_battle` prints nothing.
3. `python3 tools/ci_golden_modes_check.py`: the three field digests equal (the moves and the config
   object change no arithmetic).
4. A folded army field in which one subformation routs and another holds leaves the cohorts that fed
   them with different bodies; a planted "side share for every cohort" reddens it.
5. `build_realm(0..2)`, one season: content hashes equal to the base at seeds 0 and 1; seed 2 moves only
   if proposal `04_MB_headcount_grade_and_scale.md` has landed.

## Falsifier

A season arm that enters a function now under `systems/`; a run whose outcome changes when an `MB_*`
variable is exported; an army field whose reserve cohort is cut as deeply as its line.

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
