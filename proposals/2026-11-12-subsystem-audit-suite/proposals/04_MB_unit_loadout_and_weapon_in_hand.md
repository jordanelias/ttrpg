# MB · the unit-scale half of the weapon-carry rule: one roster, a loadout with a secondary, the weapon in hand as state

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` Part 2) — **superseded by `04_MB_unit_loadout_and_weapon_in_hand_B.md`** where the two differ; this file's confirmations of the PC proposal's statements about the module (its first table) stand and are what `03_PC_loadout_and_carry.md` now cites. Superseded: §1's roster merge (personal combat's roster holds no missile weapon, pike or lance: addendum C-3; decided instead as one owner a fact, R-36); §2's seven-table list (twelve tables and four name tests); §4's default switch order added by the builder (a default the commander did not write is a rule standing where a choice should be: the doctrine row writes it); §4's last bullet (`PhaseOrder` gains `in_hand`: the decider's return is the manager proposal's `GeneralAction`, whose `order` behaviour carries `in_hand`). Kept by `_B`: `in_hand` as subunit state changed by an order and costing a tick; the cost by personal combat's function, handed in as factors.

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — rows applied: `R1_READ.md` §1.2 and §7 test 9 (SUPERSEDED, not an instruction: marked at the status line; the confirmations table and the saturation fact kept; the superseded resolution text replaced by a pointer to `_B` that names what `_B` keeps and replaces), §6.1 (c); `U3_DEPENDENCY_ORDER.md` B17 (listed as superseded), §4.1 row 7 (the census deletion edge to this file is SUP: no reader). No test, gate or lands-it is owed: nothing here lands. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "subformation" → "unit" in prose (glossary *unit*).

**Depends on:** nothing. **Lands in batch:** none (B17 lists it as superseded by `_B`).

## Status: SUPERSEDED by `04_MB_unit_loadout_and_weapon_in_hand_B.md` (its confirmations table stands as a record)

Lane MB. The unit-scale half of `03_PC_loadout_and_carry.md` (the PC lane's proposal, which owns the
rule and its leaf function `carry_demand`); this file confirms or corrects that proposal's statements
about mass battle and designs what the unit reads. Carries the audit's §3 finding F-MB-19 and its §14
designer surface. Reference, not mechanism (`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

Nothing while every troop type's secondary is absent (the control, and the shipped data at landing).
With a secondary authored: a unit carrying two weapons tires faster and moves slower by the same
function a person's kit is charged by, and a ranged body that is reached draws its sidearm, stops
shooting and fights as melee troops.

## The PC proposal's statements about mass battle, confirmed or corrected

| statement there | reading of `modules/mass_battle/` |
|---|---|
| two weapon rosters with two owners; a troop-type loadout table beside mass battle's | **confirmed.** `equipment/weapons.py::ARSENAL` (10 class records: damage type, weight class, reach, keywords; no mass), `equipment/armour.py::ARMOURY` (4 tiers), `equipment/__init__.py:21-42::TROOP_LOADOUT` (14 troop types, each ONE weapon and one armour) |
| no loadout, sidearm, secondary or encumbrance rule in the module | **confirmed, with one nuance.** A sidearm exists only as two constants: the comment "ranged, melee sidearm" on the 0.1 reach of ranged types (`troop_types/registry.py:116-122`) and `config.RANGED_MELEE_SIGMA = -1.0`, a flat handicap on a ranged body in melee. No datum names a second weapon |
| (implied) the loadout feeds resolution | **corrected: it does not.** The one read is the weapon's `reach` (`registry.py:172-180`, melee or ranged). Run: a spearmen mirror under loadouts (`spear`, `light`), (`pike`, `heavy`) and (`light_cut`, `none`) at one seed gives byte-identical results. Armour tier, damage type, weight class and keywords have no reader |
| a unit "with the troop's own strength score" | **corrected: troops have none.** A troop type carries Power, Discipline and Morale only (`registry.py:44-71`). The unit half needs a `strength` datum per troop type (below) |
| which weapon is in hand is not a state | **confirmed.** `Subunit.unit_type` is fixed at construction. Run: archers 300 against spearmen 300, three seeds: the archers are in melee from tick 3 and keep volleying through the melee (volley ticks 1 to 10 at seed 1) |
| fatigue and speed | per-column stamina drained per clash (`config.MB_STAMINA_DRAIN`, `percell.py:301-321`) and a per-tick step from shape, Discipline and a mounted multiplier (`units.py:1738-1783`). No equipment term in either. Run: first contact at tick 3 for light infantry, spearmen, heavy infantry and pike alike; tick 5 for levy (Discipline), 1 to 2 for horse |

One more fact the PC proposal needs: **fatigue saturates.** A 600 v 600 spearmen mirror reads stamina 52
of 100 at tick 7 and 0 at tick 18, and stays 0 to tick 72. A cost that only speeds the drain stops
mattering after one engagement; the rule below also slows recovery so it bites over a long battle.

## The resolution (superseded; read `04_MB_unit_loadout_and_weapon_in_hand_B.md`)

*(Reconciled, W3-1.)* This file's §1 to §4, its gate, falsifier, NERS reading, cost class and conflict
note were the first design and are not an instruction; the text was removed rather than left beside its
successor. What `_B` keeps from it: `in_hand` as subunit state changed by an order and costing a tick
(`_B` §4); the cost by personal combat's one function, evaluated by the host and handed to the module as
`(fatigue_factor, step_factor)` per in-hand state (`_B` §5; the function is
`engine/substrate/combat_kit.py::carry_demand_of`, D-U1-11d); the trigger kind `flanked`; the conflict with
`ED-MB-0001` (ranged is the troop type as per the weapon assigned), which `_B` carries. What `_B` replaces:
the roster merge (one owner a fact: a weapon's mass in personal combat's export when its key is there, in
`references/troops.yaml: arms` when not); the table list; the builder's default switch order (the doctrine
row writes it); `PhaseOrder.in_hand` (the manager proposal's `GeneralAction` `order` carries `in_hand`).
The confirmations table and the saturation fact above stand as this file's findings.
