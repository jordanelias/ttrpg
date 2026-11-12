# MB · the manager's battle: standing orders, a general's action at each window, a replayable command list, an honest report; one resolver for the commanded and the delegated mode

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` Part 2) — four rulings folded. (1) **A-3** answers §1: the field returns its end state and the host reads `Won`, `Lost` or `Drawn`; it is no longer listed for Jordan, and Layer 1's "the return type is `Margin`" is narrowed for the field on his word (APPLIED 2026-11-12, A-97, node `L1-A3`: `04:777`, `:786`, PART D row 24 `:1050`; `04:182` admits the person-supplied `duel` callable, node `L1-A4`; row 19 `:1045` makes the nesting cap a register fixture, node `L1-A72`). (2) **A-1** answers the addendum's §B11 item 1: §5 and §8 are the conforming form (one call at every depth; the estimate is the resolver sampled). (3) **A-4** rewrites §7's second read: an officers' duel is **called by the module at its window** through a `duel` callable the adapter built (nested, depth 1, cap 1, the typed depth-cap refusal: `Refusal(depth_cap)`, at the tree `seam/contest.py::ContestError`, D-U1-11b), never "resolved by the host": the adapter runs before and after the field, not at a window (`U5b_MB_rulings_in_the_field.md` §3; `U5b_PC_rulings_in_the_fight.md` §1). (4) **A-2**: `officer` and `standing_orders` are columns of the unit row; a unit holds no claim or memory. The module's Command draws (`rally`, an order's obedience) are drawn on the one sampler (A-5; `U5b_MB_rulings_in_the_field.md` §1) from the commander's **command**, a learned skill combined with social and mental attributes (A-59; `audits/27_MB_COMMAND_AND_DYNAMIC_STRENGTH.md` and `proposals/27_MB_*`, another lane's, cited and not restated). §6's `fortune` reports whatever side-wide factor survives that lane's test: under A-59 the per-side whole-day multiplier is lowered and tested for removal, and the chance in a field is the sum of its named draws (obedience, the stand draw of A-61, pursuit), each reported on the result.

Reconciled: 2026-11-12, A-97 (`unified/work/L1_APPLIED.md` §`L1-A3`, §`L1-A4`, §`L1-A72`, `unified/work/L1_PROPAGATION.md`): the "amendment text owed" clauses of the first Reconciled line, of the wave-3 line (A-4) and of the conflicts list are rewritten to the applied state.

## Status: PROPOSED

Folded: 2026-11-12 by `audits/27_MB_COMMAND_AND_DYNAMIC_STRENGTH.md` (ruling A-59, which answers D-34). Nothing here is deleted; four places assumed a static side value or left command as one number. (1) **§6's `fortune: (word_a, word_b)`** disclosed the side-wide multiplier. A-59 calls that value misleading and lowers it, with removal tested; the field is withdrawn in favour of `report.draws`, the list of the named draws and their bands (obedience, the stand, hold-or-chase, rally, recall, pursuit, a nested duel), which is where a field's chance is afterwards (`27_MB_C_dynamic_strength_and_the_residual_chance.md` §3). The last section's "Friction at sigma 1.1: untouched; section 6 discloses it" is superseded by the same. (2) **§7's officer** has a fourth read: he rolls his unit's standing orders, on his own `command` (`27_MB_A_command_and_the_obedience_draw.md` §3). The commander's improvised order to an officered unit is drawn twice, once by each. (3) **§4's `FieldWindowView.units`** gains `reach_bands`, `steady` and `officer_pool`, and `GeneralAction` a `reasons` tuple; `obey_odds` shows a player or a decider the odds of an action before it is given (`27_MB_D_the_commander_as_chooser.md` §2, §4). (4) **§5's "a decider draws nothing from `rng` and the module draws nothing on its behalf"** stands in the amended form audit 26 gave it; the draws are keyed (A-30), so replay holds. §2's standing orders and §5's interventions list are otherwise as written.

Folded: 2026-11-12 by `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md` (rows B-2, B-3, B-4, B-9, R-10). Nothing here is deleted. The sources read confirm the design: orders few, set before contact and released by a prearranged signal are what a pre-modern commander had (`research/historical/mass_battle_maneuver_sequences_grounding.md` §1 step 5; `…_movement_and_behaviour_grounding.md` E3). Four amendments. (1) **An order takes effect by a draw** (Command and Discipline against an obstacle by kind of order): at once, a tick late, or not at this trigger. The draw is the module's and is made whoever issued the order, so §5's "the module draws nothing on its behalf" becomes "the module draws the same for a standing order, a decider's action and a replayed intervention"; gate 1 (a decider returning `none`: equal outcome and equal draw count) and gate 2 (replay) hold as written. Detail: `26_MASS_BATTLE_maneuver_orders.md` §1. (2) **Triggers**: `enemy_broken` and `in_lull` join §2's set; behaviours `pursue`, `reform`, `feign` join it (same file §2). (3) **The lull between bouts is a window** with three actions of its own, `relieve`, `reform`, `commit` (`26_MASS_BATTLE_cell_scale_and_time.md` §3); §4's two windows inside an engagement stand. (4) **§7's last sentence**: the command-zero rout of a whole army does not stay unreached; it becomes a stand draw per unit (`26_MASS_BATTLE_rout_pursuit_and_giving_ground.md` §1). Also: §1's band is what the land ruling reads (A-57, A-58): a conceded defender is the aggressor's `Won` and loses the ground (`26_MASS_BATTLE_aggression_and_land.md` §2).

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — rows applied: `R1_READ.md` §2 rows A-59/A-77 (§6's `fortune` bullet and the conflicts list's friction line removed: `report.draws` replaces them, `27_MB_C` §3), A-61 (§7's "command-zero rout stays unreached" removed), A-30 (§5: the draws are keyed), A-4 (no edit: the callable class's Layer 1 text was owed, `OWED_TO_UNIFICATION.md` §A by C3-L2; now APPLIED, A-97, node `L1-A4`); §1.2 and `U1_OWNERS_AND_VOCABULARY.md` D-U1-11f (the standing-order cap is `battle_orders.json: standing_order_cap`, not a literal), D-U1-11g (`rally` reads the commander's `command` capability through `CommandRecord`; `MassBattleInput.command` is retired), D-U1-11b (the nested duel's typed refusal); the conflicts list's `Margin` line answered by A-3 (C3-L2); §3's pointer moved to PB; test 9 (tests from the existing set, `lever_probe` written as a file, lands-it, tier; `Depends on:` / `Lands in batch:` from `U3_DEPENDENCY_ORDER.md`). U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): MB unit "stance" → "posture" in prose (glossary *stance*, *posture*; the code field `stance` keeps its name).

**Depends on:** `04_MB_headcount_grade_and_scale.md` and `04_MB_typed_outcome_and_one_path.md` (B17); `27_MB_A_command_and_the_obedience_draw.md` 27A-1–27A-4 (B19, `CommandRecord`); for §7 `03_PC_duel_round_and_approach_B.md` (B16) and `U5b_PC_rulings_in_the_fight.md` §1 (`nested_entry`, B30); `11_GO_one_draw_owner.md` (B06, the key).
**Lands in batch:** §1–§6 and §8 in B20 (`B20-mb-orders`, MB) with `26_MASS_BATTLE_maneuver_orders.md`; §7 in B30 (`B30` MB nested).

Lane MB (seam and record edits IN's; the chooser's side CHAR's). Carries R-31, R-34, R-39, R-40, R-45 of
`audits/04_MB_audit_addendum_B.md` §B6 and its §B4, §B5.4. **Supersedes two parts of the first MB lane's
proposals, which are otherwise kept and are not edited:** §B of `04_MB_playable_field_scenario.md` (the
decider's return, `PhaseOrder(approach, retreat)`) and the `verdict` field of `FieldOutcome` in
`04_MB_typed_outcome_and_one_path.md`. Reference, not mechanism (`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

Nothing for a side that has no standing orders, no decider and no interventions: that is today's field.
Otherwise, in order of landing: (1) the field's result names no winner and the host reads the band off
its end state (the same three bands the first lane proposes; hash-equal where its `verdict` would have
agreed); (2) a unit's standing orders reach the engine's order queue; (3) a played or chooser-served
commander takes one action at each window of the same call; (4) the band Event carries which orders
fired, what the commander did and how the day's fortune fell. An army field is not fought in natural
play today, so (2) to (4) move no shipped season.

## The problem (addendum F-MB-21, F-MB-24, F-MB-26; first audit F-MB-14, F-MB-15)

- The engine has a manager's vocabulary: conditional orders on six trigger kinds, routes, go-code
  signals, a closed set of order-settable fields (`hierarchy/units.py:271-290`, `:309`, `:550`, `:2844`).
  The army Record can carry a role, a posture (`stance`), a targeting word and one fall-back fraction
  (`armyrecord.py:13-14`); `orderofbattle.py:167-168` makes the only `Order` a season can produce.
- The one army-wide lever the Record does carry is a trap. Even combined-arms field, n 200: control
  59 wins to 49; `advance` 20 to 77; `defend` 30 to 56. The first lane's phase decider chooses among
  exactly those three.
- Nothing can be decided once the field starts, and nothing says afterwards why it went as it did.
- The field returns `attacker_wins`; ratified Layer 1 says "a subsystem returning a winner has not met
  the contract" (`architecture/meta/04_CODE_ARCHITECTURE.md:786`, `:1050`;
  `03_VERBS_AND_LOOPS.md:286-289`). Combat's read-off-the-scene form is a ruled exemption
  (`engine/season/seam/ladder.py:193`); the field has none.
- Layer 1 also sets the bar for the two modes: "No second resolver. No auto-resolve formula. No fast
  path." (`architecture/holonic_ARCHITECTURE.md:984-990`) and, of fidelity, "they agree exactly, because
  they are the same slice" (`03_VERBS_AND_LOOPS.md:151-153`).

## The resolution, decided

### 1. The field returns its end state; the host reads the band (R-31)

`FieldOutcome` (first lane, `engine/season/queries/inputs.py`) loses `verdict`. It already carries, per
side, `share`, `routed`, `conceded`. `engine/season/seam/ladder.py::field_degree` reads:

```
a_out = attacker.routed or attacker.conceded
b_out = defender.routed or defender.conceded
WON   if b_out and not a_out
LOST  if a_out and not b_out
DRAWN otherwise
```

(after `unopposed` and `invested`, as now). The rule is the first lane's; only its owner moves, from the
module to the host's one grading function, which is where `combat_degree` reads a scene. `massbattle.py`'s
`_grade` returns shares and flags and no word for who won. *(Reconciled: answered by Jordan, A-3: an end
state, won, lost or drawn; the margin alternative is not taken.)*

### 2. Standing orders on the unit row (R-39)

```
standing_orders: ((trigger, behaviour), ...)     # at most `standing_order_cap` (seed 4; battle_orders.json, D-U1-11f), in priority order
trigger   ∈ immediate | tick:N | enemy_range:D | ally_at:D | own_strength:F | signal:NAME | flanked | volleys_spent
behaviour ⊂ { stance, target_condition, yielding, conceded, route, in_hand, fire_signal }
```

- The two sets are exported beside the order vocabulary (`tools/export_battle_orders.py`,
  `engine/engine_params/battle_orders.json` gains `triggers`, `behaviours` and the scalar
  `standing_order_cap`, read through `engine/substrate/battle_orders.py`; `armyrecord.order` refuses a list
  longer than it, so no literal 4 lives in `armyrecord`), from
  `hierarchy/units.py::_ORDER_TRIGGER_KINDS` and a named subset of `_ORDER_SAFE_FIELDS`. `flanked` and
  `volleys_spent` are added by `04_MB_unit_loadout_and_weapon_in_hand_B.md`.
- `modules/mass_battle/armyrecord.py::order` validates a row against those sets and refuses by name;
  `immediate` is legal only as the last row (an unconditional first row starves the rest, the failure
  Unicorn Overlord's own preview documents, `research/game_precedent_suite/tutorials/T19_tactics_narrative.md:146`).
- `orderofbattle._spec_for` builds one `Order` per row. `fall_back_at` leaves the record: it is the row
  `(own_strength:F, {stance: retreat})`.
- The `order_unit` verb's payload carries the list (`engine/season/loop/effects_army.py`); the menu
  (`harness/military_menu.py`) offers the closed sets.
- An unplayed commander's standing orders are written by his doctrine row (`troops.yaml: doctrines`,
  first lane's step 5a): a doctrine names, per class of unit, the orders it gives. Two commanders with
  two doctrines then differ in how their armies behave, not only in what they raise.

### 3. The strategy roster leaves the choice surface (R-34)

`STRATEGIES`' `advance` and `defend` are removed from `armyrecord`'s accepted values and from the menu;
the record's `strategy` key carries the army's **formation** name (`04_MB_cell_hierarchy_as_data.md`),
whose default `line` is today's deployment. A posture is still settable per unit by a standing order. An
army-wide posture returns as a roster only when each value beats the default in some named matchup and
none beats it in a mirror by more than the same-run control: the bar the PC lane sets for the duel's
approaches (`03_PC_duel_round_and_approach_B.md` §3, step 3). The first lane's proposal to share one approach roster
across the two scales waits on that.

### 4. The commanded battle: one general's action at each window (replaces the first lane's `PhaseOrder`)

`modules/mass_battle/massbattle.py::resolve_field(inp, rng, *, troops_a=None, troops_b=None, decide=None)`;
`battle_loop.run_battle(..., on_window=None)` called where `phase_boundary` is called, after it.

```python
@dataclass(frozen=True)
class FieldWindowView:          # one side's own view; built by the module, never a Unit
    window: int                 # 1-based
    side: str
    units: tuple                # ((name, share, routed, in_contact, in_hand, orders_pending), ...)
    signals_fired: tuple

@dataclass(frozen=True)
class GeneralAction:
    kind: str                   # 'signal' | 'order' | 'rally' | 'withdraw' | 'none'
    unit: Optional[str] = None  # for 'order' and 'rally'
    arg: Any = None             # a signal name, or one behaviour from the standing-order set
```

| action | what it does, by an existing primitive |
|---|---|
| `signal` | adds the name to `Unit.fired_signals`: every order waiting on `signal:NAME` fires, on every unit (`hierarchy/units.py:2844`) |
| `order` | applies one behaviour dict to one unit, through the same validation an `Order` uses |
| `rally` | the commander's hook: `rally_check` for that unit, a draw on the commander's `command` skill (carried on `CommandRecord`, `27_MB_A_command_and_the_obedience_draw.md` §2; the old integer `MassBattleInput.command` is retired, D-U1-11g) restoring morale toward its start |
| `withdraw` | the retreat `_retreat_orders` already sets on every unit |
| `none` | nothing |

- One action a window; the count of windows is the engine's phase boundaries (two in an 18-tick
  engagement). `signal` is the prepared act and `order` the improvised one.
- The wrapper never hands the decider a `Unit`, and the decider is handed nothing of the other side but
  what is in contact with its own units.
- `engine/season/seam/wrappers/mass_battle.py::resolve` forwards `host.decide` for a played claimant or
  defending commander, as `seam/wrappers/combat.py` does (REM-31, ratified
  `proposals/2026-10-07-grid-mode-suspension.md`). A commander nobody plays has no decider by default;
  CHAR may supply one through the same parameter, served by the chooser over the same closed set.

### 5. One slice at every depth: the interventions list

`MassBattleInput.interventions: tuple = ()`, each `(side, window, GeneralAction)`. When no decider is
given, the module applies the listed action at its window. `FieldOutcome.interventions` returns the
actions a decider took. So:

- **delegated** = `resolve_field(inp, rng)`: standing orders decide;
- **commanded** = `resolve_field(inp, rng, decide=d)`;
- **the same battle, summarised or replayed** = `resolve_field(replace(inp, interventions=out.interventions), rng)`,
  which returns the identical outcome.

*(Reconciled, A-30 and audit 26 B-2:)* a decider draws nothing, and every draw the module makes is keyed
`(field, tick, unit, purpose)` through `11_GO_one_draw_owner.md`'s owner, the same keys for a standing
order, a decider's action and a replayed intervention, so the draws do not depend on who decided. This is
what makes the two modes the same slice at two depths, which Layer 1 asks for, and not two calculations
that agree on average, which it refuses.

### 6. The report

`FieldOutcome.report` (first lane: per phase, per part, share lost, broke or held, flanked) gains:

- `orders_fired: ((tick, unit, trigger), ...)`, from one `trace_event('order', …)` at the point
  `core/contact.check_orders` applies a behaviour (the only engine addition in this proposal);
- `interventions`, as above;
- *(Reconciled, A-59, A-77: the `fortune` word pair is removed; `report.draws`, the named draws and their
  bands, replaces it, `27_MB_C_dynamic_strength_and_the_residual_chance.md` §3.)*

`_eff_march` writes these as Observations on the band Event (first lane, step 4b), as members of
`rosters.yaml: observation_terms` on `Event.observed` (D-U1-06).

### 7. Officers (R-40)

Unit row `officer`: a person id. The host puts him on the typed input with his unit. Three reads, in
this order of landing: the general's span counts officers (built, `armies.py:204-245`); an officer's
unit in contact with an enemy officer's unit at a window is a **duel contact**, *(Reconciled, A-4:)*
resolved **by the module at that window** through the `duel` callable its adapter handed it (the
`combat.round` role, nested at depth 1 under a cap of 1; `03_PC_duel_round_and_approach_B.md` §4 and
step 5), one round a window, the two `DuelState`s in the module's loop frame; an officer
felled or yielded erodes **his unit's** morale by `cascade_morale_hit`, scaled by that unit's own
discipline (never a flat amount, never the army: the PC lane's borrowed constraint, T-PC-15).
*(Reconciled, A-61: the command-zero instant rout of a whole army, `battle_loop.py:411-413`, becomes a
stand draw per unit, `26_MASS_BATTLE_rout_pursuit_and_giving_ground.md` §1.)*

### 8. The estimate stays samples of the resolver (R-45)

`field_estimate` runs the entry; at about 20 ms a field of 600 a side, 400 samples is some eight seconds,
and more once bodies have ranks. Conformant ways to pay: `estimate_samples` lower (a display is not a
measurement), and a cache keyed on the frozen `MassBattleInput`. A closed-form odds function is not
proposed and should be refused if proposed: it is the auto-resolve formula Layer 1 names.

## Gate (execution artifacts)

1. Seeds 0 to 199 on an army field: `decide=None`, and a decider that always returns `none`, give equal
   outcomes and an equal count of draws from `rng`.
2. A scripted decider (fire a signal at window 1, order one unit to `hold` at window 2): the outcome
   differs from the control at some seed; feeding its returned `interventions` back with no decider gives
   an outcome equal field by field, at every one of the 200 seeds.
3. A unit with `((enemy_range:4, {stance: hold}), (own_strength:0.6, {stance: retreat}))` holds when the
   enemy comes within four and retreats at 60%; `orders_fired` names both with their ticks; a row with an
   unknown trigger is refused by name at `order_unit`.
4. `advance` and `defend` are refused by `armyrecord`; the addendum's `lever_probe` control row is
   unchanged (W3-1, test 9: the scratch `lever_probe` is first written as
   `systems/mass_battle/sim/lever_probe.py`; expected output the control row of the even combined-arms
   field at n 200, 59 wins to 49, unchanged by the edit).
5. A hand-built stalemate, a mutual rout and a one-sided rout fold `field.drawn`, `field.drawn` and
   `field.won` through `field_degree` with no `verdict` anywhere in the result
   (`git grep -n "attacker_wins\|verdict" modules/mass_battle engine/season/seam/wrappers/mass_battle.py` prints nothing).
6. Two officers whose units are in contact at window 1: one `combat.round` call is made; the loser's unit
   reads lower morale than the same field without the duel, and no other unit's morale moves.
7. No function under `modules/mass_battle/` is entered by the commanded run and not by the delegated one
   (the first audit's reach probe, on the two modes).

**Tests (W3-1, from the existing set).** Gates 1–2: `tests/valoria/test_army_battle.py::test_none_decider_equals_no_decider`,
`::test_replay_from_interventions_is_identical` (`assert checked >= 200`). Gate 3:
`tests/valoria/test_conditional_orders.py::test_standing_orders_fire_and_report`,
`::test_unknown_trigger_refused_by_name`, `::test_more_than_standing_order_cap_rows_refused`. Signals:
`tests/valoria/test_mass_battle_signals.py`. Gate 4: `tests/valoria/test_army_verbs.py::test_advance_and_defend_refused`.
Gate 5: `engine/season/tests/test_march.py::test_field_degree_reads_flags_not_a_verdict` plus the grep in
the commit body. Gate 6 (B30): `tests/valoria/test_mass_battle_officers.py::test_officer_duel_moves_only_his_units_morale`.
**Hash movers:** none for a side with no orders, no decider and no interventions. **Lands:** an IN-lane
implementation session under `/methodology-execute` with MB review; `sonnet`; §7 in B30.

## Falsifier

A decider that changes the draw count; a commanded battle whose replay from its interventions differs in
any field; a standing order that cannot change an outcome at any of 200 seeds; a report whose
`orders_fired` is empty when an order visibly fired; a closed-form estimate anywhere in the tree.

## NERS (definitions `CLAUDE.md` §0.06)

- **N.** From the player: an instruction that reaches the field and an act during it are the manager's
  whole game, and neither exists. From the world: standing orders are how two unplayed commanders differ,
  at no chooser cost. From the architecture: the decider is combat's shape; the interventions list is
  what makes fidelity a rendering. From the referents: all five have the intent step, three the window,
  two the review.
- **R.** Prepared against improvised command; customisation by rows over closed sets; the no-player half
  (orders fire in a battle nobody watches, and the Event says so); complete at the extreme of no orders.
- **S.** One call at every depth; pauses at the engine's own boundaries; grading at the host's one
  function, like combat; triggers for a unit and conditions for a squad member are one idea.
- **E, last.** One field on the record, five actions, one list on the input, three lines in the report,
  one trace event; the `verdict`, the strategy roster and `fall_back_at` are deleted. A player can read
  his own orders back in the result.

## Cost class

Sections 1 and 3: edit. Sections 2, 5, 6: small build. Section 4: small build after 2. Section 7: small
build after the PC round entry and the first audit's Command input. Section 8: edit.

## Conflicts with ruled or ratified items, named and not resolved

- Layer 1's "the return type is `Margin`" against a field read off its end state: answered by A-3 (an end
  state); its Layer 1 text is APPLIED (2026-11-12, A-97, node `L1-A3`: `04:786`, row 24 `:1050`), so the
  field provider's end state conforms to Layer 1 and the field decider and the `duel` callable no longer wait
  on an amendment (`L1-A4`, `04:182`, row 22 `:1048`; the depth cap `L1-A72`, row 19 `:1045`).
- `ED-IN-0301` (a field is fought the round it is declared): unchanged; the windows are inside that call.
- *(Reconciled, A-59, A-77: the friction line is removed; the multiplier ships at zero when `27_MB_C`'s
  first arm passes.)*
- AQ-X1 as recorded at `seam/wrappers/mass_battle.py:465-466` ("no NPC reads" the estimate): untouched.
