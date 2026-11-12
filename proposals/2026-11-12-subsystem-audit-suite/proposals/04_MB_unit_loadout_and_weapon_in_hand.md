# MB · the unit-scale half of the weapon-carry rule: one roster, a loadout with a secondary, the weapon in hand as state

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` Part 2) — **superseded by `04_MB_unit_loadout_and_weapon_in_hand_B.md`** where the two differ; this file's confirmations of the PC proposal's statements about the module (its first table) stand and are what `03_PC_loadout_and_carry.md` now cites. Superseded: §1's roster merge (personal combat's roster holds no missile weapon, pike or lance: addendum C-3; decided instead as one owner a fact, R-36); §2's seven-table list (twelve tables and four name tests); §4's default switch order added by the builder (a default the commander did not write is a rule standing where a choice should be: the doctrine row writes it); §4's last bullet (`PhaseOrder` gains `in_hand`: the decider's return is the manager proposal's `GeneralAction`, whose `order` behaviour carries `in_hand`). Kept by `_B`: `in_hand` as subunit state changed by an order and costing a tick; the cost by personal combat's function, handed in as factors.

## Status: PROPOSED

Lane MB. The unit-scale half of `03_PC_loadout_and_carry.md` (the PC lane's proposal, which owns the
rule and its leaf function `carry_demand`); this file confirms or corrects that proposal's statements
about mass battle and designs what the unit reads. Carries the audit's §3 finding F-MB-19 and its §14
designer surface. Reference, not mechanism (`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

Nothing while every troop type's secondary is absent (the control, and the shipped data at landing).
With a secondary authored: a subformation carrying two weapons tires faster and moves slower by the same
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

## The resolution, decided

### 1. One weapon roster (the merge)

The surviving roster is personal combat's (`modules/combat/weapons.py::WEAPONS`, the one with located
mass), read through its typed export as the PC proposal's leaf does. Mass battle's `ARSENAL` and
`ARMOURY` are deleted. What mass battle needs from a weapon is derived, not authored twice: `reach
class` (melee or ranged) and the P-DEC-1 reach band (non-pole 0.1, pole 0.2, pike 0.3) from the record's
length class; damage type and weight class from the record. `08_mass_battle_units.md`'s U-2 asked for
this merge and both modules' docstrings say they expect it.

### 2. The troop table, as data (the designer's surface, audit §14)

One typed file under `engine/engine_params/` behind an exporter with a `--check` round-trip, generated
from one authored YAML under `references/` (the shape `battle_orders.json` already has). One row per
troop type:

```
key · power · discipline · morale · strength · mounted · cell_cap
primary · secondary (or none) · armour          # weapon keys of the one roster; an armour tier
roles (the menu) · training_site · min_site_condition
```

`TROOP_TYPE_STATS`, `TROOP_TYPE_REACH`, `MOUNTED_TYPES`, `TROOP_TYPE_DENSITY_CAP`, `TROOP_TYPE_ROLES`,
`TROOP_LOADOUT` and `TRAINING_SITE` become reads of it. To define a new troop type or loadout a designer
adds a row; the loader refuses an unknown weapon key, armour tier, role or site kind by name. Giving
pikemen or archers an arming sword is one cell (`secondary`), with no code edit.

### 3. The cost, by the same function

The module does not import the leaf (it reads no `engine/` code today). The host does: when
`armyrecord.fielded` or the headcount constructors' inputs are built, the host evaluates
`carry_demand` for each subformation's loadout in both states (primary in hand; secondary in hand)
against the row's `strength`, and hands the module two numbers per state on the typed input
(`Subformation.carry = ((fatigue_factor, step_factor), (fatigue_factor, step_factor))`), each computed
from `short = max(0, carry_demand - strength)` with the coefficients the PC proposal names
(`ACT_WEIGHT / D_WT` for fatigue, `CARRY_CLOSE_K` for movement). The module multiplies: the per-clash
drain in `percell.update_stamina` and the subunit drain in `battle_loop` by the fatigue factor; the rest
recovery (`MB_STAMINA_REST`, `STAMINA_RECOVERY_PER_RESERVE_RANK`) divided by it; the step in
`Subunit._node_advance` by the step factor. A row with no secondary and `strength` at or over its
harness demand gets factors of 1: today's battle exactly. No coefficient is authored in the module.

### 4. The weapon in hand is subunit state, changed by an order

- `Subunit.in_hand: str = 'primary'`. `unit_type` and the front reach are read from the weapon in hand
  (properties, not stored), so a body with a bow in hand is ranged and with a sword in hand is melee.
- `in_hand` joins `hierarchy/units.py::_ORDER_SAFE_FIELDS`. The existing `Order` triggers carry the
  change; nothing new is needed to express "when the enemy closes, draw swords":
  `Order('enemy_range:<VOLLEY_MIN_RANGE>', {'in_hand': 'secondary'})`, which `orderofbattle._spec_for`
  adds by default to any subformation whose primary is ranged and whose secondary is melee. For a pike
  body with a sword the default trigger is its own break in order: `own_strength:<fall-back fraction>`
  is the wrong reading, so the default is contact inside the pike's reach band on a flank or rear arc,
  which the engine already computes per pair (`b_angle_mod <= -0.5`); a new trigger kind `flanked` is
  the one addition to `_ORDER_TRIGGER_KINDS`.
- **The switch costs a tick.** On the tick the order fires the subunit's pair pools are 0 and its brace
  latch resets (`_brace_since_tick`), the unit-scale form of the PC proposal's spent readiness.
- `orchestration.volley_phase::fire` requires the weapon in hand to be ranged, so a body that has drawn
  swords stops shooting; `RANGED_MELEE_SIGMA` applies only to a body fighting hand to hand with a ranged
  weapon in hand (a type with no secondary, or one caught before its order fires).
- A played side changes it through the phase decider (`04_MB_playable_field_scenario.md` B):
  `PhaseOrder` gains `in_hand` per subformation.

## Gate (execution artifacts)

1. Hash equal with every `secondary` absent: `tools/ci_golden_modes_check.py` digests and the season
   pins unchanged.
2. The exporter's `--check` round-trip passes; a row naming an unknown weapon key is refused by name.
3. The mirror of the audit's probe, with the loadout now read: two spearmen bodies differing only in
   a carried secondary differ in stamina at tick 7 and in first-contact tick; at a `strength` over the
   demand they do not.
4. Archers with a sword secondary, reached: volley events stop at the tick after the order fires; one
   tick with no melee from that body; thereafter melee without the ranged handicap. Archers with no
   secondary: today's result, byte-equal.
5. A 72-tick mirror in which one side carries a secondary: the carrying side's stamina recovers more
   slowly out of contact, measured, so the cost is visible after tick 18.
6. The PC proposal's cross-scale assertion: the factor the host hands the module equals `carry_demand`
   evaluated by the same function on the same loadout and strength, asserted by calling it.

## Falsifier

A carried secondary that changes nothing at any strength; a reached ranged body that still shoots after
switching; a second roster or a second carry rule appearing in `modules/mass_battle/`; a result that
moves with all secondaries absent.

## NERS

- **N.** From the player's direction this is the first equipment decision that reaches a battle at all
  (today none does). Laterally it is the same rule as a person's kit, at one owner. Cut it and the pike
  that cannot fight when its order breaks and the archer who shoots while being cut down both stay.
- **R.** A real trade (versatility against tiring and slowness), customisable by data, complete at its
  extremes (no secondary is the control; a strong troop pays nothing).
- **S.** One function, one roster, one vocabulary across the two scales; the switch pauses the body for
  a tick, as it costs a person his next action.
- **E, last.** Two catalogues and seven tables become one roster and one table; one state field, one
  trigger kind.

## Cost class

Design-first for the trigger default and the saturation fix (item 3's recovery clause is a judgment);
small build after `03_PC_loadout_and_carry.md` lands. Depends on PC (the function and the roster) and
CHAR (the capability surface, audit §14).

## Conflict with a ruled item, named

`ED-MB-0001` (Jordan, 2026-07-02: "Ranged is troop type as per the weapon assigned to troop") fixes
`unit_type` from the assigned weapon. Reading it as "from the weapon in hand" extends it; reading it as
"a troop type is ranged or it is not" forbids the switch. The brief's 2026-11-12 text (archers carry
arming swords; the switch is a state change) is the later statement.
