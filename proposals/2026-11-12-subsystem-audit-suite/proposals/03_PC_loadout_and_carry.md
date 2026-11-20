# PC — one loadout and one carry-cost rule for a person and a unit; the weapon in hand as round state

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` §1.2, §1.4) — the addendum's §B7 amendments and the MB addendum's two corrections are folded. (1) The round it builds on is `03_PC_duel_round_and_approach_B.md` (state in the calling loop's frame; a choice per phase), not the first proposal's. (2) `in_hand` and the half-sword `form` are **one field**: the key of the record currently held (item 5). (3) The leaf takes masses: `carry_demand_of(masses, armour)` is the one body and `carry_demand(weapons, armour)` calls it, because a troop's bow or pike has no key in the personal roster (item 2; MB addendum C-3, R-36). (4) "One roster" is decided as one owner a fact: a weapon's mass lives in personal combat's export when its key is there and in `references/troops.yaml: arms` when it is not, refused if stated in both (item 4; `04_MB_unit_loadout_and_weapon_in_hand_B.md` §2; `03_PC_weapon_records_in_the_export.md` item 6). (5) On the capability surface the carry cost is the `threshold` role with two holders, a person's Strength and a troop row's `strength` (U1 §9). The statements about mass battle marked `[UNVERIFIED]` below are confirmed or corrected in `04_MB_unit_loadout_and_weapon_in_hand.md`'s table.

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — rows applied: `U1_OWNERS_AND_VOCABULARY.md` D-U1-11d (the carry rule is one pure function **in** `engine/substrate/combat_kit.py`; the host computes each party's shortfall for every kit he may wield and hands it raw on `PersonalCombatInput` and the unit row; neither module holds a copy or calls the leaf). This answers `R1_READ.md` §1.1's AMBIGUOUS placement row; R1 7b-5's [DECISION] (a `combat.carry_demand` composition role in `modules/combat/combat_systems.py`) is **not** applied: the U1 decision wins over the read lane. Also: §6.1 (c) (the MB statements are confirmed or corrected in `04_MB_unit_loadout_and_weapon_in_hand.md`'s table and `_B` decides the roster: item 4's "one weapon roster or a declared key map" is replaced by the one-owner-per-fact rule of head item (4)); 7b-4 (`DuelState.form` is kept as the key of the record in hand); U1 glossary *unit* ("unit row"); test 9 (call sites, tests, `Depends on:` / `Lands in batch:` from `U3_DEPENDENCY_ORDER.md`, §4.1 row 61). A-98 vocabulary lane (2026-11-12, A-98; ledger `unified/work/A98_SWEEP.md`): "capability" in prose → skill (1). A-101 round lane (2026-11-12, `master/pc_round/PC_ROUND_SPEC.md`, glossary §K): "the round" and "the duel round" here are A-101's round (close, 1 to 4 exchanges, separate); a switch spends the fighter's next action inside a round; "field turn" (§ on troop fatigue) is the battle's field tick or bout, never a combat word.

**Depends on:** `03_PC_duel_round_and_approach_B.md` steps 1–4 (B16: `DuelState.form`, the per-phase consult); `03_PC_weapon_records_in_the_export.md` (B14: `mass` in the export); `04_MB_unit_loadout_and_weapon_in_hand_B.md` stages 1–2 (B17: the troop file as data). `04_MB_unit_loadout_and_weapon_in_hand_B.md` stages 3–4 depend on this file and land after it in B31 (U3 §4.1 row 61, SPLIT).
**Lands in batch:** B18 (`B18-pc-content`, PC), after `03_PC_person_inputs_content.md` Parts B–D.

## Status: PROPOSED

Lane: PC, with MB (troop loadouts), SE (stores as arms) and CHAR (the skill surface). Source:
Jordan's direction of 2026-11-12 (`AUDIT_BRIEF.md`, "Mass battle: the cell-based approach and the
weapon-carry trade-off"); `audits/03_PC_audit.md` §10 and R-PC-26. Read at `601e715`. Reference only
(CLAUDE.md §0.05); not ratified by being written. The mass-battle side was read by search only
(`modules/mass_battle/troop_types/registry.py:160-170`, `equipment/weapons.py:1`); every statement
about it below is `[UNVERIFIED beyond those lines]` and is MB's to confirm.

## What it changes in `engine/season/` at runtime

Nothing while a kit holds one weapon (today's case everywhere). With a secondary weapon: a fighter who
carries more tires and closes more slowly, and may change the weapon in hand at the cost of a round's
tempo. A declared mover only for persons who carry a secondary.

## The questions asked, answered from the code

**Does personal combat already carry the loadout-cost rule a unit would share?** No. There is no
loadout and no carry cost.

- A kit is exactly one weapon and one armour tier: `engine/season/queries/world_q.py:3484-3509`
  (`kit_of`) takes the highest-ranked arms kind per field and discards the rest; `PersonalCombatInput.kits`
  is `(weapon, armor)`; `Combatant` has one `weapon` and one `armor` (`modules/combat/combatant.py:112`).
- What the engine charges is the cost of what is **wielded and worn**, never of what is carried:
  the weapon's Strength demand (`combat_systems.py:183-186`: length, swing inertia, handling, two
  hands, rear clearance, and `D_MASS × mass` in kilograms) feeding a handling penalty (`:187-189`);
  stamina per action from the wielded weapon's heft and from the harness's Strength demand
  (`:168-174`, `ARMOR_DEMAND`, `config.py:115`). The comment at `:169-172` already states the form as
  one ladder: "a Strength demand, whether weapon or harness", charged as `max(0, demand − strength)`.
- Movement: the only movement in a fight is closing the measure (`combat_systems.py:1380-1387`), which
  reads balance and the wielded weapon's tempo. Armour and carried mass do not slow it.
- Armour has no mass: a tier carries a Strength demand in points and nothing in kilograms.
- There are **two weapon rosters with two owners**: `modules/combat/weapons.py::WEAPONS` (54 records
  of located mass) and `modules/mass_battle/equipment/weapons.py::ARSENAL`, with a troop-type loadout
  table beside it. A search of both modules for a loadout, sidearm, secondary or encumbrance rule
  finds none. So an individual's and a unit's carry penalty are not one rule at one owner; neither
  exists, and the things they would be computed over are defined twice.

**Is switching weapons mid-fight a state the duel round reads?** Only in one narrow form. The engine
changes the weapon record in hand between a sword and its half-sword form, automatically and free of
cost, each beat (`wrapper.py:273-274`, `combat_systems.py:880-890`): the same object held differently.
There is no second weapon to draw, so there is no switch, no cost for one and no state naming what is
in hand beyond `Combatant.weapon` itself. The round state proposed in
`03_PC_duel_round_and_approach.md` (`DuelState`) does not carry it either.

## The resolution, decided

One rule, one owner, both scales (ladder rung 4: `act_cost`'s own one-ladder form is the precedent;
rung 5 for where it lives).

1. **A loadout is a kit with a secondary.** `kits` becomes `(primary, secondary, armor)` per party,
   `secondary` defaulting to none; `kit_of` returns the two highest-ranked weapon kinds the person's
   rungs stock instead of one. `rosters.yaml: arms_kinds` needs no new column.
2. **Carried mass is the quantity, Strength demand is the unit.** The leaf
   `engine/substrate/combat_kit.py` itself (the kit data's owner, D-U1-11d), reading the typed export and
   nothing else, owns one function:

   ```python
   def carry_demand_of(masses: tuple, armour: str) -> float:      # (Reconciled) the ONE body
       """Strength points demanded by what is CARRIED: D_MASS per kilogram of every carried mass that is
       not in hand, plus the harness's ARMOR_DEMAND. Reads the export's `cfg`."""

   def carry_demand(weapons: tuple, armour: str) -> float:
       """The keyed spelling: looks each weapon's mass up in the export's `weapons` section and calls
       `carry_demand_of`. A person's kit uses this; a troop row, whose arm may have no key here, uses the
       mass form. One rule, two spellings of its argument."""
   ```

   The export's `kit` section gains each weapon's `mass` (already a field of every record). No new
   constant: `D_MASS` and `ARMOR_DEMAND` exist and are exported.
3. **The penalty is the form the engine already uses,** `short = max(0, carry_demand − strength)`:
   fatigue as `ACT_WEIGHT / D_WT × short` stamina per action, added in `act_cost` where the harness
   term sits now (the harness term moves into `carry_demand`, same value); movement as a factor on
   `close_rate`, `1 / (1 + CARRY_CLOSE_K × short)`, one new `[SIM-CALIBRATE]` coefficient in `CFG`,
   0 as the control. A fighter at or over the demand pays nothing, as now. *(Reconciled, D-U1-11d:)*
   the host (`seam/wrappers/combat.py::combat_input`) evaluates `carry_demand` and hands each party's
   `short` raw on `PersonalCombatInput` (one value per kit he may have in hand: with the primary, with the
   secondary); `combat_systems.act_cost` (`:168`) and `close_rate` (`:1380`) read it from the Combatant the
   module builds from its input. `modules/combat/` imports nothing from `engine/substrate/` for this.
4. **A unit row is charged by the same function.** *(Reconciled, D-U1-11d and head item (4):)* the
   mass-battle host evaluates `carry_demand_of` over the troop row's loadout masses with the troop's own
   `strength` and hands the shortfall (as `(fatigue_factor, step_factor)` per in-hand state,
   `04_MB_unit_loadout_and_weapon_in_hand_B.md` §5) on the unit row's input; a weapon's mass comes from
   personal combat's export where its key is there and from `references/troops.yaml: arms` where it is not,
   refused if stated in both. No key map and no roster merge.
5. **The weapon in hand is round state, and changing it costs the round's tempo.** *(Reconciled:)*
   `DuelState.form` (PB §2) **is** this field: the key of the record in hand, whether a half-sword form
   of the primary or the secondary; no second field is added. The choice set a decider may answer at a
   phase entry gains `switch` beside the approaches (and `withdraw` at the top of a round): the fighter spends his next action's readiness
   (`ACT_THRESHOLD`, the unit the engine already debits, `wrapper.py:279`) and fights the rest of the
   round with the other weapon; the secondary's mass leaves `carry_demand` and the primary's enters.
   An NPC's or a standing order's trigger for it reads what the engine already computes: how badly the
   weapon in hand serves the present measure (`close_unwieldiness`, `combat_systems.py:275-304`). The
   half-sword form change stays as it is; it is a grip, not a second weapon.
6. **At unit scale** the same state is one value per subunit (which weapon the line has in hand) and
   the same trigger read at the unit's contact state; that half is MB's proposal to write.

## Gate (execution artifacts)

- Hash EQUAL with every secondary absent (the harness term relocated, same value): season pins and
  the combat goldens unchanged.
- Workbench, 1,000 fights per cell, disjoint-seed control: a Strength-4 spearman carrying an arming
  sword against the same spearman without one shows more stamina spent and a slower close; at
  Strength 7 the two are inside the control band.
- A spear-and-sword fighter closed on by a dagger switches (count reported) and his felled share is
  below the spear-only fighter's in that matchup and not below it at open measure.
- MB side, when built: one troop type's fatigue per field turn equals `carry_demand` evaluated on its
  loadout by the same function, asserted by calling it.

## Falsifier

A carried secondary that costs nothing at any Strength; a switch that takes no tempo; a unit and a
person with the same loadout and strength score who are charged different demands; a second
`carry_demand` in either module.

## Implementation (test 9, W3-1)

- **Order of edits.** (1) `engine/substrate/combat_kit.py`: `carry_demand_of`, `carry_demand` (the export's
  `kit` section gains `mass`, landed by `03_PC_weapon_records_in_the_export.md`); (2) `PersonalCombatInput`
  gains the per-party `short` pair; `seam/wrappers/combat.py::combat_input` fills it; (3)
  `combat_systems.act_cost` takes the harness term from the input and adds the carry term; `close_rate` gains
  `CARRY_CLOSE_K` (in `CFG`, exported, 0 shipped); (4) `queries/world_q.py::kit_of` returns
  `(primary, secondary, armor)`; (5) `switch` in the consult's choice set (after PB step 4).
- **Call sites.** `combat_systems.act_cost` (called at `wrapper.py:286`), `close_rate` (called at
  `wrapper.py:237`); `kit_of`'s callers in `seam/wrappers/combat.py`; the MB host's `field_input` (stage 3 of
  `04_MB_unit_loadout_and_weapon_in_hand_B.md`, B31).
- **Tests.** `tests/valoria/test_combat_units_refactor.py::test_carry_demand_of_equals_the_keyed_spelling`;
  `engine/season/tests/test_cp_t03_03_kit.py::test_kit_of_returns_a_secondary_when_two_kinds_are_stocked`;
  `tests/valoria/test_combat_units_refactor.py::test_a_switch_debits_one_act_threshold`; MB side (B31):
  `tests/valoria/test_mass_battle_order_of_battle.py::test_the_factor_handed_in_equals_carry_demand_of`.
- **Gate** as above; the workbench cells are a one-time reading in the commit body (`R1_READ.md` 7b-20).
- **Hash movers.** None while every kit holds one weapon (control: the harness term relocated, same value);
  persons with a secondary.
- **Lands:** an IN-lane implementation session under `/methodology-execute` with PC review; items 1–3 and 5
  `sonnet`; the workbench reading `haiku` (`valoria-measure`) read by `opus`.

## NERS reading

- N: from above, the stated trade (fight in either mode, pay for it) has no carrier at either scale;
  laterally, two weapon rosters would give two answers for one pike; from below, the mass per weapon
  and the one-ladder demand form already exist and are used for half of it.
- R: a loadout is a real choice (reach and a fallback against weight); a line that drops its pikes
  for swords at the moment it is broken into is a hook; an NPC or an order makes the same choice.
- S: one function, one unit (Strength points), the same form as the handling penalty; the round
  pauses for a switch exactly as for any other per-phase choice; one roster of weapons.
- E, last: one leaf function, one coefficient, one field on the round state, one member of the choice
  set, against a rule that would otherwise be written twice. High.

## Cost class

Small build in PC (items 1, 2, 3, 5). Design-first in MB for items 4 and 6 (carried by
`04_MB_unit_loadout_and_weapon_in_hand_B.md`). Dependencies: the `Depends on:` line at the head.
