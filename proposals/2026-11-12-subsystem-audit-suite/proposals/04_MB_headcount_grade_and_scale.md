# MB · the headcount field: one survivor share, one scale, a drawn field

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` Part 2) — three rulings folded. (1) **A-3**: the field returns its end state and the host reads the band; the module-side `verdict` this file adds to `_grade` is withdrawn in favour of `04_MB_manager_battle_one_resolver.md` §1 (`_grade` returns shares and the `routed` / `conceded` flags; `seam/ladder.py::field_degree` reads `Won`, `Lost` or `Drawn` by the same three-line rule stated below). The rule, the `Drawn` band, the one share and the one scale stand. (2) **A-57, A-58**: on `Drawn` the defender keeps the land; this file's "no mover; nobody arrives" is kept and is its own choice (`26_MASS_BATTLE_aggression_and_land.md` §2); on `Won` onto land another holds the title and its seats pass by `U5d_FA_land_and_seats_pass_on_a_won_march.md`, after this file's writes. (3) **A-4 and the squad**: `field_subunits="person"` stays the arm for a side of persons facing troops; a field of two sides of named persons only goes to the squad entry (`U5b_MB_rulings_in_the_field.md` §3). `field_walls_dr=3` keeps its value and changes its unit when `16_PESSIMIST_MB_partition_and_the_pair_rule.md` edit 3 lands (walls as dice on the attacker's roll, not armour subtracted from damage); the module's dice are the one sampler (A-5; same file §1).

## Status: PROPOSED

Folded: 2026-11-12 by `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md` (rows R-10, R-7, R-2, S-1). Nothing here is deleted. (1) **The three-valued verdict is the historical definition of a result** (one side "finally broke and fled", or neither did: `research/historical/mass_battle_casualties_and_results_grounding.md` A11, D4) and is what rulings A-57 and A-58 read: on a march onto land another holds, `won` passes the land and its seats, `drawn` leaves the defender holding, `lost` takes nothing in either direction (`U5d_FA_land_and_seats_pass_on_a_won_march.md`; `26_MASS_BATTLE_aggression_and_land.md` §2). A conceded defender is `won` for the aggressor under the rule in this file and so loses the ground. (2) **On `Drawn`, "no mover" stands**: A-58 settles the land and does not say where the aggressor's army then is; this file's write is kept and that question is listed open, not assumed. (3) **A drawn bout is not yet a drawn battle**: with `max_bouts` above 1 the wrapper fights again in the same scene and returns one band (`26_MASS_BATTLE_cell_scale_and_time.md` §3); at 1, this file is unchanged. (4) The one weight-to-troops owner puts season armies at 60 to 900 men, which is what fixes the cell's scale at sixteen men (same file §1). (5) The measured loser-to-winner loss of this path can be read against Krentz's table as a ratio (`26_MASS_BATTLE_calibration_targets.md` T-2).

Lane MB (the seam edits are IN). Carries resolutions R-01, R-02, R-03, R-16, R-18, R-19 of
`audits/04_MB_audit.md` §6.2. Reference, not mechanism (`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

Every fought field. Today a field between realm forces ends at tick 2 with both sides routed, the attacker
graded the loser, and each person's `body` multiplied by his side's headcount over 100. After this change
a field is a battle whose outcome depends on the sides and the draw, the share written is the share of
troops that survived, and a field nobody wins is written as one. In natural play at seed 0 nothing moves
(no field is fought there); at seed 2 the one-season pin moves and is re-recorded.

## The problem (evidence in the audit, F-MB-01, F-MB-02, F-MB-04)

1. `Unit.recalc_size` routs any unit under 100 troops at the first tick
   (`modules/mass_battle/hierarchy/units.py:2985-2990`); `field_troops_per_weight` ships 1
   (`engine/season/data/fixtures.py:789`), and realm sides are 2 to 30 weight. Run: 30 v 18, 30 v 6, 99 v 1,
   seeds 0 to 19: attacker loses 60 of 60.
2. The same side is sized two ways: `weight x 1` against a headcount side, `under_arms_cap(weight)`
   (`weight x 30`) against an army (`massbattle.py:279`, `:367-369`).
3. `_grade` reads `effective_size / max(1, size_max)` on the headcount path (`massbattle.py:447-448`), which
   is `hp / (100 x floor(start / 100))`. Run: in 70 of 289 attacker wins the losing defender reads above
   1.0 (worst 1.638), and `_eff_march` writes it uncapped (`loop/effects_combat.py:637`). Season: seed 2,
   bodies 1000 → 20 and 1000 → 30.
4. `run_battle` returns `winner: "draw"` (`battle_loop.py:468-469`); `_run_and_grade` drops it and grades a
   mutual rout or a stalemate as the attacker's loss (`massbattle.py:427`, `:453-463`).

## The resolution, decided

One survivor share (`hp / hp_max`), one weight to troops owner (`recruitment.under_arms_cap`), one
deployment rule for every side, one verdict with three values, and a fourth fought band.

The design intent agrees and is not the reason (§0.05): the archived mass-battle description has an
inconclusive ending in three places (mutual destruction is a draw with no territory change; three
bloodless turns end in a withdrawal where "neither side claims victory"; the strategic table's `Partial`
is "no territory change"). The ladder steps are in the audit: R-01 step 4 (the tree already sizes this
side by `under_arms_cap` on its other path, and Jordan delegated the conversion at `ED-IN-0306`), R-02
step 5, R-03 step 4 (`Invested` is already a band nobody wins; the module already says "draw").

## Exact edits

**`modules/mass_battle/massbattle.py`** (owner of the grade and the headcount constructors)

- `_grade(unit_a, unit_b)`: delete the `by_troops` parameter and its `else` branch. Both shares are
  `unit.hp / max(1.0, unit.hp_max)`.
- *(Reconciled, A-3:)* `_grade` returns each side's share and its `routed` / `conceded` flags, and **no** `verdict`; the rule below is evaluated by the host's `field_degree`, where `combat_degree` reads a scene. ~~`_grade` returns `verdict` in place of `attacker_wins` and `degree`:~~

  ```
  a_out = unit_a.routed or unit_conceded(unit_a)
  b_out = unit_b.routed or unit_conceded(unit_b)
  verdict = 'won'   if b_out and not a_out
            'lost'  if a_out and not b_out
            'drawn' otherwise            # both out, or neither out when the ticks ran down
  ```

  The survivor-share tie-break (`a_size_pct > b_size_pct`) goes: a field in which neither side broke is
  drawn. The constants `OVERWHELMING_ATTACKER_MIN`, `OVERWHELMING_DEFENDER_MAX`, `PARTIAL_ATTACKER_MIN`
  and the four-way `degree` are deleted (no reader: `seam/ladder.py:211-216`).
- `_weighted_unit` and `_person_unit`: `troops = max(under_arms_cap(weight), _MIN_TROOPS)`; the
  `troops_per_weight` parameter is deleted. Both are built with `faction` `'A'` / `'B'` and placed by
  `orderofbattle._place` (one line each), so a headcount field starts `_APPROACH_ROWS` apart as an army
  field does. `_MVP_SUBUNIT_SHAPE['starting_position']` is deleted.
- `_HEADCOUNT_LINE_TYPE` and `_oob_unit`'s `None` branch are unchanged (they already size by
  `under_arms_cap`).

**`engine/season/queries/inputs.py`**: delete `MassBattleInput.troops_per_weight`.

**`engine/season/data/fixtures.py`**: delete `field_troops_per_weight` (and its sweep row); ship
`field_walls_dr=3` (with CP-T04-05's scaling this is the archived table's +3 at a full garrison and
proportionally less below; `None`, the flat row, stays in the sweep as the control); ship
`field_subunits="person"`.

**`engine/season/hole_register.yaml`**: H-250 `default:` → closed, owner `recruitment.under_arms_cap`;
H-354 closed by the `Drawn` band; H-359 `default:` → `person` shipped; H-308 → graded as shipped.

**`engine/season/rosters.yaml`**, **`verb_table.yaml`**: the field-degree band roster gains `Drawn`;
`march` gains a `Drawn` row: writes `(Person, body)`, emits `field.drawn`. No arrival kind.

**`engine/season/seam/ladder.py::field_degree`**: *(Reconciled, A-3:)* reads the two sides' `routed` and `conceded` flags off the typed outcome and applies the rule above (`Won`, `Lost`, `Drawn`),
after `unopposed` and `invested`.

**`engine/season/seam/wrappers/mass_battle.py::resolve`**: *(Reconciled:)* lifts the typed outcome's two sides in place of
`attacker_wins`; `winner` is `claimants`, `other` or `[]`. `field_estimate` tallies four bands.

**`engine/season/loop/effects_combat.py::_eff_march`**

- the loser's write is capped as the winner's is: `min(1.0, max(0.0, mine))` at `:637`;
- on `Drawn`: every member of both sides (or the drawn cohorts of a side that fought as an army) has
  `body` scaled by his own side's (or own part's) share, under `field_casualty_model` as the winners'
  write is today; no stance row; no mover; the ration debit as on `Won` and `Lost`.

## Gate (execution artifacts)

1. Module: the audit's probe re-run (`_weighted_unit` pairs, seeds 0 to 99, four size pairs): no side
   reads a share above 1.0; a side that took no casualties reads exactly 1.0.
2. Module: realm-weight pairs through `resolve_field` (weights 30 v 18, 20 v 6, 6 v 20; seeds 0 to 59):
   the verdict varies by seed, and the larger side's `won` share exceeds the smaller's.
3. Season: `engine/season/tests/test_march.py`'s real-fold test at the shipped fixtures (no scale
   override) folds a `field.won` for the unmodified Crown pair at some seed in 0 to 11 and a
   `field.lost` or `field.drawn` at another.
4. Season: a hand-built stalemate folds `field.drawn`; both sides' bodies fall by their own shares;
   no `stance` row is added to anyone; nobody is re-homed.
5. Control: `build_realm(0)`, one season, content hash equal to the base (no field is fought there).
   Seed 2's one-season pin is re-recorded, and the commit says so.

## Falsifier

A fought field at the shipped fixtures whose loser's `body` rises, or whose untouched side's `body`
falls; or twelve seeds of the unmodified realm pair that all fold one band.

## NERS (definitions `CLAUDE.md` §0.06)

- **N.** Top-down: a war that cannot be won is not a strategic layer. Bottom-up: the engine's own share
  (`hp / hp_max`) is the quantity the tick loop maintains; the other was a display integer. Lateral: the
  army path already uses it. Removing `Drawn` returns the stalemate to "the attacker lost", which worsens
  play from every direction (H-354).
- **R.** Completeness: the grade no longer breaks below a block or between blocks. The no-player half:
  a drawn field leaves two hurt armies facing each other, which is a situation, where a false defeat
  was an accounting entry.
- **S.** One methodology for the share on both paths; one deployment rule; `Drawn` pauses correctly
  (nobody moves, the place is still contested) as `Invested` does.
- **E, last, against the above.** Net deletion: one parameter, one fixture, three constants, one dead
  ladder. A player can predict that more men survive when fewer are hit.

## Cost class

Edit (one module file, one effect, four data rows). Hash mover wherever a field is fought.

## What this does not do

It does not make a side of two named persons an army (audit §15: that is a squad, and personal combat's);
it does not bring a field about in natural play (proposal `04_MB_playable_field_scenario.md`).
