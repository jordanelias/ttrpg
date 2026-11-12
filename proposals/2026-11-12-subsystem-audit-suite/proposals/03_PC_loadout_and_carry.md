# PC — one loadout and one carry-cost rule for a person and a unit; the weapon in hand as round state

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` §1.2, §1.4) — the addendum's §B7 amendments and the MB addendum's two corrections are folded. (1) The round it builds on is `03_PC_duel_round_and_approach_B.md` (state in the calling loop's frame; a choice per phase), not the first proposal's. (2) `in_hand` and the half-sword `form` are **one field**: the key of the record currently held (item 5). (3) The leaf takes masses: `carry_demand_of(masses, armour)` is the one body and `carry_demand(weapons, armour)` calls it, because a troop's bow or pike has no key in the personal roster (item 2; MB addendum C-3, R-36). (4) "One roster" is decided as one owner a fact: a weapon's mass lives in personal combat's export when its key is there and in `references/troops.yaml: arms` when it is not, refused if stated in both (item 4; `04_MB_unit_loadout_and_weapon_in_hand_B.md` §2; `03_PC_weapon_records_in_the_export.md` item 6). (5) On the capability surface the carry cost is the `threshold` role with two holders, a person's Strength and a troop row's `strength` (U1 §9). The statements about mass battle marked `[UNVERIFIED]` below are confirmed or corrected in `04_MB_unit_loadout_and_weapon_in_hand.md`'s table.

## Status: PROPOSED

Lane: PC, with MB (troop loadouts), SE (stores as arms) and CHAR (the capability surface). Source:
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
2. **Carried mass is the quantity, Strength demand is the unit.** A leaf beside
   `engine/substrate/combat_kit.py`, reading the typed export and nothing else, owns one function:

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
   0 as the control. A fighter at or over the demand pays nothing, as now.
4. **A unit reads the same function.** Mass battle's fatigue and speed for a troop type call
   `carry_demand` over that type's loadout with the troop's own strength score, which requires its
   loadout to name weapons the function knows. The prerequisite is one weapon roster or a declared
   key map between `ARSENAL` and `WEAPONS`; which survives is MB's and the holistic stage's call, and
   is the capability surface's equipment question (audit §14).
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
`04_MB_unit_loadout_and_weapon_in_hand_B.md`). *(Reconciled:)* depends on
`03_PC_duel_round_and_approach_B.md` steps 1 to 4 for item 5 and on
`03_PC_weapon_records_in_the_export.md` (the `mass` field in the export) for item 2.
