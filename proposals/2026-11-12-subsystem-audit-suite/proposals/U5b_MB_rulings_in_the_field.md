# U5b · MB — the rulings that land inside the field: one sampler, the end state and the land, the nested duel, the squad as a module entry, veterancy as a draw, and the one landing order

## Status: PROPOSED (a plan for future execution; nothing here is executed by the closing lane)

Folded: 2026-11-12 by `audits/27_MB_COMMAND_AND_DYNAMIC_STRENGTH.md` (rulings A-59 and A-69, given after this file was written). Nothing here is deleted. (1) **§1 row 3's carriers now exist**: `27_MB_A_command_and_the_obedience_draw.md` (the `command` row, `CommandRecord` for the commander and each unit's officer, the draw), `27_MB_B_unit_prowess_on_the_row.md` (a unit's pool from its own row; the commander is not in a pair's dice), `27_MB_C_dynamic_strength_and_the_residual_chance.md` (the multiplier's test), `27_MB_D_the_commander_as_chooser.md`, and `27_MB_E_what_an_army_carries_back.md` (A-69). (2) **One difference of order with §6 row 4, reconciled on lane 27's reading** (the coordinator's direction, 2026-11-12; recorded in `unified/U5_FINDINGS_CLOSURE_U5b.md`'s `Reconciled:` line): the multiplier's test is read last, and by A-77 its first arm passing ships zero. Row 4 places "the side-wide multiplier's three-arm test and the obedience draw" just after the sampler. The instrument can be built there. Its **reading** cannot be taken there, for two reasons `27_MB_C` §4 states: on the present pair rule twice the men win 299 of 300 with the multiplier off, so removal must be read on the new pair rule (row 4's later step); and the draws that are to carry the chance in its place (obedience, which needs row 5's standing orders; the stand draw and pursuit, row 4's last steps; the commander's record, row 10) do not exist until then. So the test is read last, and the multiplier's value changes in one commit after it. The arms are six, not three: the three values with the named draws on, and three controls. (3) `27_MB_B`'s consolidation is CR-12's step 2 inside row 4; `27_MB_E` lands after row 2.

Author: U5b closure lane (Fable), 2026-11-12. Read at `6910680`. Carries Jordan's answers A-1, A-2, A-3,
A-4, A-5, A-57 and A-58 (`unified/DECISIONS_ANSWERED.md`) into `modules/mass_battle/` and its
seam where no single file carried them, and composes the family's fifteen MB proposals into one order.
Handed across and specified here: `U5a_DICE_owed_edits.md` §1 row 4 (the module's sampler). The first
rows of the `field` site (`unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §5, §9) are lane 27's.
**Answered since, and not carried here:** battle luck (D-34) is A-59 (the day's luck lowered once order
friction exists; order friction from command; a unit's own prowess as data; no static side-wide
value), whose carriers are another lane's `audits/27_MB_COMMAND_AND_DYNAMIC_STRENGTH.md` and
`proposals/27_MB_*` (cited by title; not duplicated: an earlier draft of §1 specified the commander's
two inputs and is withdrawn in their favour); numbers in the melee dice (D-35) is A-60 (frontage, depth
and endurance, not the dice), carried by `04_MB_cr12_linear_law.md`; the rout floor is A-61 (a stand draw
beside the 15% band), carried by `26_MASS_BATTLE_rout_pursuit_and_giving_ground.md` §1. The history lane's
adjudication (`audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md`) and its six proposals are folded into
the order of §6. The land ruling's two owners are
`U5d_FA_land_and_seats_pass_on_a_won_march.md` (the title write) and
`26_MASS_BATTLE_aggression_and_land.md` (which end state is the aggressor's win); neither is restated.
Reference only (CLAUDE.md §0.05). No number below is a balance claim.

## What it changes in `engine/season/` at runtime

§1: every fought field (the module draws from the one sampler); one declared re-record, shared with the
whole batch of §6. §2: nothing of its own (it names which proposal's line each ruling lands on). §3: a
field between two sides of named persons only is resolved by a registered squad entry, a declared mover
for those fields. §4: nothing. §5: behind a fixture whose control is no veterancy.

## §1 · One sampler in the field (A-5)

**Problem.** `modules/mass_battle/resolution.py` owns a second die (`roll_pool`, `roll_pool_fractional`),
a second ladder (`compute_degree`) and a second sigma path (`_sigma_softcap`, `_sigma_net_boost`)
(`audits/04_MB_audit.md` §4.1; addendum C-5; `audits/10_DICE_audit.md` F-DICE-07, -08, by title). A-5
rules the bell curve everywhere and names *"the battle's whole-dice sampler"*.

| # | owner | exact edit |
|---|---|---|
| 1 | `modules/mass_battle/resolution.py` | `roll_pool`, `roll_pool_fractional` → `dice_engine.roll_net_continuous`; `compute_degree` → the owner's `degree_from_net` / `degree_label`; `_sigma_softcap`, `_sigma_net_boost` → `sigma_leverage.soft_cap`, `net_boost` (DOE §1 row 4, as written). The module's first `engine` import is this leaf, as the other two registered modules already import it (`modules/combat/core.py:20-21`, `modules/social_contest/roll.py:60`) |
| 2 | **the composition with the pair rule** (what DOE left to this lane) | DOE row 4 says the opposed roll "stays and is named". For the **melee pair** it does not stay: `16_PESSIMIST_MB_partition_and_the_pair_rule.md` edit 2 pays each side by its own net, on the ruled partition requirement (ED-MB-0003, ED-MB-0004) and a measured defect (0 wins of 60 for three bodies on one body's cells). So the contract row's `obstacle: opposed_roll` name is not created for the pair; a pair's casualties are `K_LINEAR × frontage × PAY_PER_NET × max(0, net) × (1 + power)` with `net` the continuous net. The discipline, rally and recall checks keep a stated obstacle |
| 3 | **the commander's inputs, the obedience draw and a unit's own prowess: not here** | A-59 rules them (command from a learned skill and social and mental attributes; each unit's prowess from its troops, equipment and subformation; no static side-wide value). Their carriers are `audits/27_MB_COMMAND_AND_DYNAMIC_STRENGTH.md` and `proposals/27_MB_*` (another lane's). Every Command draw those files define is drawn on this section's sampler; `04_MB_typed_outcome_and_one_path.md` §4's `command: tuple = (4, 4)` yields to their typed input |

**Gate.** (1) `grep -rn "randint(1, 10)" modules/mass_battle` prints nothing. (2) The owner's ladder and the module's agree at every cell
(the 6 of 10,000 tenth-step cells of F-DICE-07 are gone, because there is one function). (3) The mirror control of `audits/04_MB_audit_addendum_B.md` (`mirror_probe`, n 300)
stays side-fair within 1.5 standard deviations.
**Falsifier.** A d10 face dealt anywhere under `modules/mass_battle`; a degree graded by a function
other than the owner's.
**Hash movers.** Every fought field; `tools/ci_golden_modes_check.py`'s three digests and every
`engine/tests/` golden with a field, re-recorded once with §6's batch.

## §2 · What a field returns, and the land (A-3, A-57, A-58)

Decided by Jordan; this section only places each clause on the one line that carries it.

| ruling | lands on | what changes in this family's files |
|---|---|---|
| A-3: won, lost or drawn, with Unopposed and Invested; read off which side broke or conceded | `04_MB_manager_battle_one_resolver.md` §1 (`FieldOutcome` carries end state; `seam/ladder.py::field_degree` reads the band) | `FieldOutcome.verdict` and the module-side `verdict` of `04_MB_headcount_grade_and_scale.md` are withdrawn; `_grade` returns shares and flags. Battle internals stay draws |
| A-57, A-58 (1): only an aggressor's win on land another holds passes the land, and its seats | `U5d_FA_land_and_seats_pass_on_a_won_march.md` edits 1–5 (one tail, `_take_hold`) | `_eff_march`'s write order on `Won`: casualties and pursuit, then the arrival, then that tail (`26_MASS_BATTLE_aggression_and_land.md`, "Exact edits"). The first audit's "presence, never title" (§5.1, R-11) is superseded for this case |
| A-58 (2): a draw defends | `04_MB_headcount_grade_and_scale.md`'s `Drawn` band: no title, no arrival | unchanged; "nobody arrives" is that proposal's choice and is kept. Where a drawn aggressor then stands is open (26's open item 2) |
| A-58 (3): aggression is read from the act | U5d's decision 1 | the module receives no holder, purpose or leave (`26_…_aggression_and_land.md` §1); `MassBattleInput` gains nothing |
| the aftermath | `04_MB_playable_field_scenario.md` §G as reconciled | a routed defender is still re-homed to a rung his faction holds; after a `Won` that passed the land, "the winner stands beside the loser" (H-355) cannot occur for a routed defender, and a defender who conceded has withdrawn by his own order |

## §3 · A duel inside a field, and the squad as a registered entry (A-4; Layer 1 §44.3)

**Two texts in this family put a loop and state where Layer 1 forbids them.**
`04_MB_manager_battle_one_resolver.md` §7 has an officers' duel *"resolved by the host through
`combat.round`"*; the field is one provider call and its adapter runs before and after it, never at a
window (`audits/03_PC_audit_addendum_B.md` F-PC-19). `04_MB_squad_grid_of_named_characters.md` §3 puts
the squad's exchange loop and one `DuelState` a person in a new wrapper, `seam/wrappers/squad.py`, *"held
here for the length of the field"*; a wrapper never holds state, decides, resolves or drives a clock
(`architecture/holonic_ARCHITECTURE.md:1679-1686`).

| # | owner | exact edit |
|---|---|---|
| 1 | `modules/mass_battle/battle_loop.py` (the window of `04_MB_manager_battle_one_resolver.md` §4) | the officers' duel is called **by the module** at a window, through the `duel` callable its adapter handed in: `U5b_PC_rulings_in_the_fight.md` §1 edit 4 (nested, depth 1, cap 1, the typed result `NESTING-CAP`). `MassBattleInput` carries each officer's `PersonalCombatInput` half (built host-side by `combat_input`); the module builds the `DuelRoundInput` and keeps the two `DuelState`s in its loop's frame |
| 2 | `modules/mass_battle/squad.py` (new), with a sixth composition row `mass_battle.resolve_squad` in `references/module_contracts.yaml` | `resolve_squad(inp: SquadInput, rng, *, duel, deciders=None) -> FieldOutcome`: the pairing policy and the exchange loop of the squad proposal's §3, unchanged in rule, moved from a wrapper into a registered entry. It reads no `World`, holds its states in its own frame, calls `duel` and no other resolver, and returns the same `FieldOutcome`. `SquadInput` (frozen, beside `MassBattleInput`): the two sides' persons with place (`front` / `rear`, file), standing orders, the leader, and each person's `PersonalCombatInput` half |
| 3 | `engine/season/seam/wrappers/mass_battle.py::resolve` | the scale rule stays here as routing (which entry the projection is handed to: a side with no order of battle and no cohort member is a squad), on the precedent of the `Unopposed` and `Invested` branches, which already return without the cell engine. It builds `duel = nested_entry("combat.round", 1, fx)` once and passes it to either entry. `engine/season/seam/wrappers/squad.py` is **not** created |
| 4 | `04_MB_squad_grid_of_named_characters.md` gate 5 | re-pointed: `git grep -n "modules.combat" modules/mass_battle/squad.py engine/season/seam/wrappers/mass_battle.py` prints nothing |

**Gate.** The squad proposal's gates 1 to 4 and 6, run through the entry; the manager proposal's gate 6
(one `round` call at a window with two officers in contact) with the call made inside the module; with
the cap at 0, both return their band with the contact or pairing reported unresolved.
**Falsifier.** A `DuelState` on a wrapper attribute; a squad exchange that draws from the cell engine; a
second duel resolver.
**Hash movers.** Squad fields (every field the shipped realm fights today, e.g. seed 2's two against
three); fields with an officer contact.

## §4 · One resolver, and a unit as a row (A-1, A-2): where each proposal stands

A-1: no proposal of this family builds or implies a separate fast formula. The conforming statements are
`04_MB_manager_battle_one_resolver.md` §5 (delegated, commanded and replayed are one call) and §8 (the
estimate is the resolver sampled; a closed form is refused). The two loops in the registered tree that
are a second path (`run_multi_turn_battle`, `run_multi_unit_battle`) leave it
(`04_MB_typed_outcome_and_one_path.md` §2). A-2: every column the family adds (`post`, `ranks`, `files`,
`secondary`, `standing_orders`, `officer`, `experience`, `arrears`, `raw`) is a column of the army
Record's unit row; no proposal gives a unit claims, memory or identity. ARC-07's *"a condition on a
unit"* is read as claims in its officer's and its men's ledgers (`audits/04_MB_audit.md` §13).

**One fixture where two were proposed.** `04_MB_playable_field_scenario.md` §E proposes `Fixtures
army_presets: off | on`; `14_VERBS_MILITARY_C_the_muster.md` Edit 7 proposes `armies_at_build: off |
empty | mustered`. One owner: MIL-C's three-valued fixture; `mustered` is the playable-field proposal's
`on`. The opportunity-key edit both name (`data/verbs.py::opportunity_key`, a digest of the payload for
an army verb) is MIL-C's Edit 5, once.

## §5 · Veterancy is a draw (the standing rule; `audits/14_VERBS_MILITARY.md` §0.5)

`04_MB_campaign_party_economy.md` §1 raises a unit's `experience` by one, with certainty, when it lost
troops and did not rout on a side that did not lose. Whether men who stood come out better or only
fewer could go either way.

1. `_eff_march`, for each eligible unit (that proposal's conditions (a) and (b), unchanged): one draw on
   the one sampler: pool the pool rule on the unit officer's `command` score (the commander's where the
   unit has none; the untrained default where neither), obstacle `veterancy.ob` in the troop file's header
   plus one per step already held. Success or better: `experience += 1` to the cap. Partial or Failure:
   unchanged. A unit destroyed is reset, and the dilution rule stands: both are bookkeeping.
2. `veterancy: {arm: off | steps, …}` keeps `off` as the control. Arrears stay arithmetic (they set the
   odds: one Discipline lower); what unpaid men **do** is drawn where the MILITARY lane draws it
   (`14_VERBS_MILITARY_C_the_muster.md`: `discharge_troops`' Failure band and the dispersal draw).

**Gate.** The economy proposal's gate 2 with 200 seeds of one field: some eligible units gain and some do
not; an untouched reserve never gains. **Falsifier.** A gain in every eligible unit. **Movers.** None at
`off`.

## §6 · One landing order for mass battle

| # | batch | files | dependency | movers |
|---|---|---|---|---|
| 1 | scale, grade, the drawn band | `04_MB_headcount_grade_and_scale.md` (with `verdict` read host-side, §2) | none | fought fields (seed 2's pin) |
| 2 | the typed outcome, one path, no hidden inputs | `04_MB_typed_outcome_and_one_path.md`; `U5b_MB_residue.md` §1 (the one role list) | 1 | hash EQUAL but per-cohort shares |
| 3 | the troop file as data, no behaviour change | `04_MB_unit_loadout_and_weapon_in_hand_B.md` stages 1–2 | 2 | none |
| 4 | **the field calibration batch: one re-record** | §1 (the sampler) → the side-wide multiplier's three-arm test and the obedience draw (`proposals/27_MB_*`, A-59; with `26_MASS_BATTLE_maneuver_orders.md` §1) → `16_PESSIMIST_MB_one_stamina_ledger.md` steps 1–2 → `04_MB_cr12_linear_law.md` steps 1–3 with `16_PESSIMIST_MB_partition_and_the_pair_rule.md` edits 2–4 as its step 3 → `04_MB_cell_hierarchy_as_data.md` (`arm: grid`) with `26_MASS_BATTLE_cell_scale_and_time.md` → `26_MASS_BATTLE_rout_pursuit_and_giving_ground.md` with `16_PESSIMIST_MB_rout_has_two_exits.md` → `26_MASS_BATTLE_calibration_targets.md` read last | 1–3. Each step's gate is read before the next lands; goldens and digests are re-recorded once at the end. The partition row is read **before** the grid arm (the grid multiplies bodies; on the present pair rule it multiplies the defect) | every fought field |
| 5 | orders and the commanded battle | `04_MB_manager_battle_one_resolver.md` §2–§6 with `26_MASS_BATTLE_maneuver_orders.md`; `04_MB_playable_field_scenario.md` A, C, D | 4 (a decider is not built on levers the pair rule inverts) | none with no orders |
| 6 | armies in the realm | `14_VERBS_MILITARY_C`, `_D`; `04_MB_playable_field_scenario.md` §E as reconciled; `14_VERBS_PHYSICAL_B` B1 | FA's levy and remit; 1–4 | declared flips |
| 7 | the land | `U5d_FA_land_and_seats_pass_on_a_won_march.md` with `26_MASS_BATTLE_aggression_and_land.md` | 1 (the `Drawn` band) | every `Won` on held land |
| 8 | the nested duel and the squad | §3; `03_PC_duel_round_and_approach_B.md` steps 1–2 and 5 | PC's round entry; 5 (the window) | squad fields; officer contacts |
| 9 | the second weapon, movement and fatigue as data | `04_MB_unit_loadout_and_weapon_in_hand_B.md` stages 3–4; `26_MASS_BATTLE_movement_and_fatigue_as_data.md`; `16_PESSIMIST_MB_one_stamina_ledger.md` step 3 | 4; `03_PC_loadout_and_carry.md` | rows with a secondary |
| 10 | veterancy, upkeep, command and a unit's prowess as data | `04_MB_campaign_party_economy.md` with §5; `proposals/27_MB_*` (A-59) | 2; U5a's CAP Part B | none at the control arms |

The friction multiplier's residual size is set by calibration against
`26_MASS_BATTLE_calibration_targets.md` (A-59's marked assumption), inside row 4, by lane 27's test; no
row here edits its magnitude. Numbers leave the melee dice (A-60) in row 4's CR-12 step.

## Who lands it, and dependencies

IN-lane implementation sessions with the MB lane's review, in the order of §6. §1 lands in or after U5a's
sampler batch (DOE §1) and before the keyed draw (A-30). §3 waits on PC's round entry. Layer 1 is not
edited: the nesting text owed is drafted in `U5b_PC_rulings_in_the_fight.md` §1.

## NERS reading (E last)

- **N.** One die and one ladder for a fight, a debate and a field; one line each for the ruled end state and the ruled land; a squad that is a module entry and
  not a second kind of wrapper.
- **R.** A unit may or may not learn from a field. Complete at the extremes: the cap returns a typed
  result.
- **S.** The field stops being the one module with its own dice; the played, delegated and nested calls
  are one slice each.
- **E, against that.** One new entry and one composition row; a die, a ladder, a sigma path, a proposed
  wrapper and a proposed fixture retire.

## Cost class

§1: small build plus the calibration batch. §2, §4: none. §3: small build. §5: edit.
