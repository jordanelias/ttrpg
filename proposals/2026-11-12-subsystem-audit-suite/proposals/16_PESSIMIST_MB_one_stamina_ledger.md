# MB · one stamina ledger: the one that works, reported, and able to enter a field tired

## Status: PROPOSED

Lane MB (the input field is IN's). Carries resolution 6 of `audits/16_PESSIMIST_MB.md` §5 and its
finding F-PES-MB-06. It is the ledger that the addendum's
`04_MB_unit_loadout_and_weapon_in_hand_B.md` needs for a loadout's fatigue cost to bite on; that
proposal is not edited. Reference, not mechanism (`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

Steps 1 and 2: nothing a season can observe (the deleted ledger never moves in a season field; the
returned number changes from one that is always 100 to the one the fight used). Step 3: nothing until
a host writes the new input; at its default the field is today's, hash equal.

## The problem (evidence: `audits/16_PESSIMIST_MB.md` §2.6; run `p5_tired.py`)

There are two stamina ledgers for one quantity (`ED-MB-0045` counts three stores).

| | unit ledger | column ledger |
|---|---|---|
| state | `Unit.stamina`, `Subunit.stamina` (`hierarchy/units.py`) | `percell._ColBlock.stamina` |
| drained by | `STAMINA_DRAIN_PER_CONTACT_CELL` in `battle_loop.run_battle` | `MB_STAMINA_DRAIN` in `percell.update_stamina`, damped by depth |
| read by | `core/exchange.py::_stamina_pool_penalty`: one die off at exactly zero | `percell._fatigue_sigma`: a sigma malus that grows to `MB_STAM_SIGMA` |
| a fresh 18-tick field ends at | 99.5 and 100.0 of 100; zero on 0 of 80 sides | 35 of 100 |
| entering at 50 instead of 100 (mirror, n 100, friction off) | 36 / 54 / 10 → **36 / 54 / 10** | 36 / 54 / 10 → **15 / 79 / 6** |
| reported by `run_battle` | **yes** (`a_stamina`, `b_stamina`) | no |

The ledger that is reported does nothing; the ledger that does something is reported nowhere, starts
at 100 in every field, and has no input, so a forced march, a siege, a second field in one season or a
heavy kit cannot arrive in the fight.

## The resolution, decided

One ledger: the column ledger. By the ladder's fifth step: the cut of the other is free (identical
tallies and mean losses over 100 fields), and the survivor is the one that already is bottom-up (a
column's own fights tire it; depth rests it).

## Exact edits

**Step 1, delete the unit ledger (hash equal on every season field; the goldens say).**

| file · owner | edit |
|---|---|
| `modules/mass_battle/battle_loop.py::run_battle` | delete the "v20: stamina drain proportional to cells in contact" block (the `drain_stamina` loop) |
| `modules/mass_battle/core/exchange.py` | delete `_stamina_pool_penalty` and the `stam_pen` term in `subunit_combat_pool` and `command_base_pool` |
| `modules/mass_battle/config.py` | delete `STAMINA_DRAIN_PER_CONTACT_CELL`, `STAMINA_RECOVERY_PER_RESERVE_RANK`, `STAMINA_POOL_THRESHOLDS`, `STAMINA_EXHAUSTED_POOL_PENALTY`; `STAMINA_MAX` stays (the column ledger's ceiling) |
| `modules/mass_battle/hierarchy/units.py` | delete `Subunit.stamina`, `stamina_max`, `eff_stamina`, `eff_stamina_max`, `drain_stamina`, `recover_stamina`, `Unit.stamina`, `stamina_max`; `Unit.agg_stamina()` becomes the troop-weighted mean of the unit's column blocks (the expression `_fatigue_sigma` already forms) |
| `modules/mass_battle/orchestration.py` | `stamina_check` is deleted from `phase_boundary` (the column ledger already rests every unengaged column each tick, `percell.update_stamina`); `between_turn_recovery`'s stamina line adds `BETWEEN_TURN_STAMINA_RECOVERY` to each column block instead of the deleted field; `Unit.base_combat_pool` loses its `stam_pen` |
| `armies.build_army` | the per-subunit `stamina` / `stamina_max` spec keys are refused with a message naming `entry_stamina` |

If any golden moves at step 1, the unit ledger was not inert on that path: stop, and record which.

**Step 2, report the ledger that is used.** `run_battle`'s `a_stamina` / `b_stamina` are
`agg_stamina()` as redefined: the number returned is the number that set the fatigue malus.

**Step 3, let a field be entered tired.**

| file · owner | edit |
|---|---|
| `engine/season/queries/inputs.py::MassBattleInput` | new field `entry_stamina: tuple[float, float] = (1.0, 1.0)`, each side's share of full stamina at the start, in `[0, 1]` |
| `modules/mass_battle/massbattle.py::resolve_field` | after each `Unit` is built: `for b in unit.col_grid: b.stamina = STAMINA_MAX * share`; at `1.0` nothing is written |
| `engine/season/seam/wrappers/mass_battle.py::field_input` | passes `(1.0, 1.0)`. **What writes a lower value is not decided here**: it is the campaign layer's (a march's length, a ration short, a second field this season) and the loadout proposal's (a kit's carry cost), each through this one field |

The `PER_CELL` off arm has no column grid; there `entry_stamina` other than `(1.0, 1.0)` is refused
loudly rather than ignored.

## Gate (execution artifact)

One test in the file covering `resolve_field`: a mirror field, n 100 seeds, friction pinned off for
the test; `entry_stamina (0.5, 1.0)` loses more often than `(1.0, 1.0)` by more than the sampling band
(the measured gap is 36 → 15 wins); `(1.0, 1.0)` equals the field with the argument omitted, field for
field; the returned stamina is below 100 at the end of a fought field. Step 1's own gate is the
existing goldens, unchanged.

## Falsifier

A field whose result is unchanged by `entry_stamina` 0.1 against 1.0 on one side; or a returned
stamina of 100 after eighteen ticks of contact.

## NERS (E last)

- **N.** From the campaign down, a march can cost something in the field; from the cell up, nothing
  changes (the columns already tire). Lateral: personal combat's kit (`CP-T03-03`) gets a sibling
  place to charge a carry cost. Cut the unit ledger: nothing dies (measured). Cut the column ledger:
  "a tired unit fights worse" dies.
- **R.** A reason to rest an army, to keep a reserve fresh, to weigh a second weapon.
- **S.** One quantity, one ladder, and the number shown is the number used.
- **E, against that.** Fewer lines than before: a ledger, four constants and six accessors go; one
  input field arrives.

## Cost class

Edit (steps 1 and 2), small build (step 3).
