# MB · troop types and loadouts as designer-editable data: one troop file, a second weapon, the weapon in hand

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` Part 2) — three joins to its neighbours; no decision changes. (1) §5's leaf correction is taken on the PC side: `carry_demand_of(masses, armour)` is the one body (`03_PC_loadout_and_carry.md` as reconciled), and on the capability surface a troop row's `strength` is the `threshold` role's second holder (U1 §9). (2) §5's factors apply to **the column ledger only**: `16_PESSIMIST_MB_one_stamina_ledger.md` deletes the unit ledger, so "the subunit drain in `battle_loop`" and `STAMINA_RECOVERY_PER_RESERVE_RANK` named in the first lane's text have no successor; the fatigue factor multiplies `percell.update_stamina`'s drain and divides its rest. (3) Order: stages 1–2 in the data batch, stages 3–4 after the field calibration batch and the arrangement (`U5b_MB_rulings_in_the_field.md` §6 rows 3, 4, 9). A-2: `secondary` on the unit row is a column. ED-MB-0001's reading ("per the weapon in hand") is the brief's later statement, as this file says.

## Status: PROPOSED

Folded: 2026-11-12 by `audits/27_MB_COMMAND_AND_DYNAMIC_STRENGTH.md` (ruling A-59, clause 2: each unit has its own prowess from the quality of its troops and its equipment, as affected by its subformation and tactics). Nothing here is deleted and no term is changed. `27_MB_B_unit_prowess_on_the_row.md` states where each of this file's terms meets the one function that composes a unit's pool: `power` is the quality in the base dice; the arm in hand sets reach, support ranks and melee or missile for the pair; `armour` acts against the attacker's roll; the carry factors act on the column ledger and the step. None of them is multiplied by a value belonging to the unit's side. One row is added to §3's file: `infantry`, the unmustered body of a side with no army Record, carrying the literals that side lends it today (`power: 4`, `discipline: 5`), so that no unit's quality comes from anywhere but a troop row. `switch` and `reform` are orders and take effect through the obedience draw (`27_MB_A`).

Folded: 2026-11-12 by `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md` (rows B-12, S-1, M-8, M-1). Nothing here is deleted. (1) **A body itself in melee contact does not volley**, whichever weapon is in hand; a body not in contact may shoot into a melee (Agincourt and Crécy as page-read, `research/historical/mass_battle_maneuver_sequences_grounding.md` §5). This is added to §4: without it a reached missile body with no switch order still shoots while it is fought, which stage 3's gate does not catch; the gate gains the row "a reached archer body with no order: zero volley events after its first tick in contact". (2) **The archer's switch is sourced** for Agincourt ("when the archers ran out of arrows, they 'dropped their bows' and attacked with 'hatchets, swords, spears and the mallets'") and **not found** for Crécy; the `volleys_spent` trigger stands on the first. (3) **Per-arm `range`** takes the stated scale's values (javelin about six cells, bow and crossbow the board, sling and engines not established and left at `[2, 8]`): `26_MASS_BATTLE_cell_scale_and_time.md` §2. (4) **No historical magnitude exists for what a second weapon costs** in fatigue or speed (`…_movement_and_behaviour_grounding.md` T7): the trade is Jordan's design, the form here is confirmed, and every `mass_kg` and `strength` stays a seed. (5) `pace` joins the troop row and `MB_CAVALRY_SPEED_MULT` leaves the code (`26_MASS_BATTLE_movement_and_fatigue_as_data.md` §1); the carry `step_factor` multiplies it.

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — rows applied: `U1_OWNERS_AND_VOCABULARY.md` D-U1-11d (the carry rule's home is `engine/substrate/combat_kit.py::carry_demand_of`; the mass-battle host calls it and hands the factors in; `R1_READ.md` §1.2's conditional "the host resolves `combat.carry_demand`" does not apply, since U1 took the leaf, not a composition role), §1.2 (the loader's data dependency on personal combat's export, stated), `U3_CONFLICT_LEDGER.md` C3-N18 (the roster counted is named; six of ten re-counted at `modules/mass_battle/equipment/weapons.py:38-47`: this file's count is the right one), D-U1-11c (the troop file is the home of table-shaped MB content); test 9 (call sites, tests, lands-it, tier; `Depends on:` / `Lands in batch:`, U3 §4.1 row 61 SPLIT).

**Depends on:** stages 1–2 on nothing unlanded (the exporter shape is `tools/export_battle_orders.py`'s); stages 3–4 on `03_PC_loadout_and_carry.md` (B18: `carry_demand_of` in `combat_kit.py`), `03_PC_weapon_records_in_the_export.md` (B14: `mass` in the export), `04_MB_cell_hierarchy_as_data.md` (B19, the arrangement), `16_PESSIMIST_MB_one_stamina_ledger.md` (B19), `04_MB_manager_battle_one_resolver.md` §2 (B20, standing orders carry `in_hand`).
**Lands in batch:** stages 1–2 in B17 (`B17-mb-scale`, MB); stages 3–4 in B31 (`B31-mb-loadout-economy`, MB).

Lane MB, with PC (the carry leaf and the melee roster), SE (training sites) and CHAR (the skill
surface). **Supersedes `04_MB_unit_loadout_and_weapon_in_hand.md`** (the first MB lane's; that file is left
unedited). It keeps that proposal's state design (`in_hand` on the subunit, changed by an order, costing a
tick) and its use of personal combat's carry function, and replaces its roster merge, which cannot be
executed (below), and its seven-table list, which is twelve tables and four name tests. Carries R-35 and
R-36 of `audits/04_MB_audit_addendum_B.md` §B6 and that addendum's §B3.3, §B3.5. Reference, not mechanism
(`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

In four stages. Stages 1 to 3 change nothing a season computes: the tables become reads of one exported
file whose rows are a transcription of today's constants, and every `secondary` is absent. Stage 4 changes
a field only for a troop row that names a second weapon: that unit tires faster, recovers more slowly,
steps shorter, and changes what it fights with when its order fires. No natural season fights an army
field today, so nothing moves until the first audit's steps 1 to 5 land.

## The problem (evidence in the addendum, F-MB-22, F-MB-23, C-3; first audit F-MB-19)

1. **A troop type is twelve tables and four spellings.** `TROOP_TYPE_STATS`, `TROOP_TYPE_REACH`,
   `MOUNTED_TYPES` (`troop_types/registry.py:44-75`, `:108-124`), `TROOP_TYPE_DENSITY_CAP`,
   `TROOP_TYPE_ROLES`, `ROLE_SPEC` (`config.py:124-126`, `:589-626`), `TROOP_LOADOUT`, `ARSENAL`, `ARMOURY`
   (`equipment/`), `TRAINING_SITE` (`troop_types/recruitment.py:55-69`), `ARM_SHARES`, `ROLE_OF`
   (`troop_types/presets.py:37-50`); and behaviour selected by a type's name at `hierarchy/units.py:943`
   (charge), `:1491` (wheel), `orchestration.py:1213`, `:1217` (recoil), `armies.py:267` and
   `orderofbattle.py:150` (stand-off). "Mounted" has two owners that disagree on knights templar.
2. **The weapon a type carries is read for one bit** (melee or missile). Run: a pike line and a
   heavy-infantry line give identical results to six decimal places in 440 of 440 fields; armour never
   becomes `dr`.
3. **The first lane's merge has nowhere to go.** Personal combat's roster (`modules/combat/weapons.py`,
   54 keys) holds no bow, crossbow, sling, javelin, pike, lance or engine. Six of `ARSENAL`'s ten classes
   (`pike, javelin, bow, crossbow, sling, siege`; `ARSENAL` registered at
   `modules/mass_battle/equipment/weapons.py:38-47`; the roster counted is the personal record roster
   `WEAPONS`, C3-N18, re-counted by W3-1) have no record there, and an archer's primary weapon has none.
4. **No second weapon, no state for the one in hand, no cost for carrying** (first audit F-MB-19, by run:
   reached archers volley through the melee; stamina saturates within one engagement).

## The resolution, decided

### 1. One authored file, one export, one loader

- Authored head: `references/troops.yaml` (owner MB). Export: `engine/engine_params/troops.json` by
  `tools/export_troops.py`, with the blocking `--check` round-trip the order vocabulary already has
  (`tools/export_battle_orders.py` → `battle_orders.json`).
- Reader: `modules/mass_battle/troop_types/table.py`, loaded once. It reads a data file and imports no
  `engine` code. It refuses, by name: an unknown column; a troop row naming an arm, armour tier, role or
  site kind that is not a member of its closed set; an arm whose mass is stated both here and in personal
  combat's export; a `secondary` equal to the `primary`. The third refusal reads
  `engine/engine_params/combat_engine_v1.json` (its `weapons` section) as a **data** dependency, never an
  import of `modules/combat/` (`R1_READ.md` §1.2).
- Every table in "the problem" item 1 becomes a function of this loader with its present name and
  signature (`stats_for`, `reach_for`, `is_mounted`, `cell_cap_for`, `roles_for`, `loadout_for`,
  `training_site_for`), so no call site changes at stage 1.

### 2. `arms`: what a soldier fights with

```yaml
arms:
  # key:        class        mass                missile only
  light_cut:   {class: non_pole, mass_kg: 1.2}
  heavy_cut:   {class: pole,     mass_kg: 2.0}      # see "content for Jordan" below
  heavy_blunt: {class: pole,     mass_kg: 1.5}
  spear:       {class: pole}                          # mass from personal combat's export (its key `spear`)
  arming:      {class: non_pole}                      # mass from personal combat's export (its key `arming`)
  pike:        {class: pike,     mass_kg: 3.5}
  bow:         {class: missile,  mass_kg: 2.0, range: [2, 8], volleys: 10}
  crossbow:    {class: missile,  mass_kg: 4.0, range: [2, 8], volleys: 10}
  sling:       {class: missile,  mass_kg: 0.8, range: [2, 8], volleys: 10}
  javelin:     {class: missile,  mass_kg: 2.5, range: [2, 8], volleys: 10}
  siege:       {class: missile,  mass_kg: 0.0, range: [2, 8], volleys: 10}   # crew-served: not carried
classes:       # the ruled P-DEC-1 map (ED-MB-0014), authored once
  non_pole: {reach: 0.1, support_ranks: 1}
  pole:     {reach: 0.2, support_ranks: 2}
  pike:     {reach: 0.3, support_ranks: 3}
  missile:  {reach: 0.1, support_ranks: 1}      # a missile weapon used hand to hand: REACH_MELEE_DEFAULT
```

- **One owner a fact, not one file.** An arm's mass lives in personal combat's typed export when its key
  is in that roster, and here (`mass_kg`) only when it is not; the loader refuses both. When personal
  combat gains a bow or a pike, the row here loses its `mass_kg` and nothing else changes. `class` is
  mass battle's own fact about an arm and lives only here.
- **Reach and support depth are derived from the arm in hand**, not kept per troop type. The
  transcription is exact: across today's tables every weapon key is carried only by types of one reach
  (`light_cut` 0.1; `heavy_cut`, `heavy_blunt`, `spear` 0.2; `pike` 0.3; every missile type 0.1), so
  `TROOP_TYPE_REACH` and `support_ranks_for` can be deleted with no result moving.
- `range` and `volleys` are today's `VOLLEY_MIN_RANGE`, `VOLLEY_MAX_RANGE` and `MB_VOLLEYS_START`,
  transcribed; they become per arm because a javelin and a crossbow should not share them, and stay equal
  until a designer changes one.
- **Seeds.** Every `mass_kg` above is a seed at memory grade (the tree sources masses only for the
  personal roster, `proposals/weapon_physics_and_concentration_model.md` §6); they are Jordan's content
  and affect nothing until a row carries a second weapon.

### 3. `troops`: a kind of soldier, one row

```yaml
troops:
  pike:
    power: 4            # today's stat line, transcribed
    discipline: 4
    morale: 5
    strength: 3         # the score the carry demand is charged against (new; seed rule below)
    mounted: false      # speed, deployment on the flanks
    charge: 0           # charge penetration: 3 for today's `cavalry`, 0 otherwise
    wheel: false        # the fast enveloping wheel: today's `cavalry`, `light_cavalry`
    default_role: null  # `Kite` for today's `mounted_archers`
    cell_cap: 200       # densest troops a cell: 100 for the four horse types today
    ranks: 4            # the unit's default depth (04_MB_cell_hierarchy_as_data.md)
    primary: pike
    secondary: null     # an `arms` key, or null. `arming` here is "pikemen who also carry arming swords"
    armour: medium      # none | light | medium | heavy
    roles: [ShieldWall, Hold, Anvil]
    training_site: barracks
    min_site_condition: 0.0
    upkeep: 0           # 04_MB_campaign_party_economy.md
```

- The four name tests become reads of `charge`, `wheel`, `default_role` and `mounted`. Knights templar
  keeps today's behaviour at landing (`mounted: false`, `cell_cap: 100`, lance class) and the
  contradiction becomes one visible cell for Jordan to set.
- **`strength` seed rule:** the smallest whole number at or above the demand of the row's own armour, so
  that a type carrying only its primary pays nothing, as today. A designer lowers it to make a levy in
  mail tire, or raises it so that veterans carry a sword for free.
- A unit row on the army Record may override `secondary` (`armyrecord.order`); nothing else of the troop
  row is overridable per unit.

**What a designer edits.** A new troop type: one `troops` row. Archers or pikemen with arming swords:
`secondary: arming`. A new missile weapon: one `arms` row. A type that charges: `charge: 3`.

### 4. The weapon in hand (kept from the first lane, with three changes)

- `Subunit.in_hand: str = 'primary'`, in `hierarchy/units.py::_ORDER_SAFE_FIELDS`. `unit_type`, reach
  and support depth are read from the arm in hand.
- A change is an `Order` behaviour, so a standing order carries it
  (`04_MB_manager_battle_one_resolver.md`): for example `(enemy_range:2, {in_hand: secondary})`.
- **The switch costs a tick:** on the tick the order fires, the unit's pair pools are 0 and its brace
  latch resets. A body with a missile weapon in hand does not volley once it has switched, and
  `RANGED_MELEE_SIGMA` applies only to a body fighting hand to hand with a missile weapon in hand.
- **Changes from the first lane's text.**
  1. Two trigger kinds are added to `_ORDER_TRIGGER_KINDS`, not one: `flanked` (contact on a flank or
     rear arc, which the engine computes per pair) and **`volleys_spent`** (ammunition at zero). The second
     is the archer's own switch in the tree's historical corpus
     (`research/pre_firearms_formations/05_late_med_renaissance_europe.md:194`, `:218`) and the concept's
     rule ("at 0 … its engagement channel falls back to its melee profile",
     `proposals/2026-09-25-squad-engagement-concept-v5.md:489`).
  2. **No default order is invented by the builder.** The first lane had `orderofbattle._spec_for` add a
     switch order to any ranged body with a melee secondary. A default the commander did not write is a
     rule standing where a choice should be; instead the *doctrine* row
     (`04_MB_manager_battle_one_resolver.md` §2) writes standing orders for an unplayed commander, and a body with
     no such order keeps its primary in hand and pays for it.
  3. The switch is one-way within an engagement unless a later order switches back; the tick is paid
     each time.

### 5. The cost, by personal combat's function, handed in as factors

Unchanged in principle from the first lane and from `03_PC_loadout_and_carry.md`: the host evaluates the
carry demand for each unit in both states and hands the module `(fatigue_factor, step_factor)` per state;
the module multiplies the per-clash drain, divides the rest recovery, and multiplies the step. Two
corrections.

- **The leaf must take masses.** `carry_demand(weapons: tuple, armour: str)` reads keys of personal
  combat's export; a troop's bow or pike has no key there. The interface mass battle needs is the same
  rule with its argument spelled as masses, `carry_demand_of(masses: tuple, armour: str)`, which the keyed
  form calls. One function body, in `engine/substrate/combat_kit.py` (D-U1-11d); the PC lane owns it. The
  caller is the host, `seam/wrappers/mass_battle.py::field_input` (and the army constructors' input
  builders); `modules/mass_battle/` neither imports nor copies it.
- **Order.** A second weapon can change a field only where the first weapon does. On today's one-rank
  bodies a change of reach class changes nothing (pike against heavy infantry, 440 of 440). Stage 4 lands
  after the arrangement change of `04_MB_cell_hierarchy_as_data.md`, or its gates cannot be read.

## Stages and gates (execution artifacts)

| stage | what lands | gate |
|---|---|---|
| 1 | the file, exporter, loader; tables become reads | `tools/export_troops.py --check` passes; `python3 tools/ci_golden_modes_check.py` digests equal; an unknown arm key is refused by name; a mass stated twice is refused |
| 2 | the four name tests become columns; `TROOP_TYPE_REACH` and `support_ranks_for` derive from the arm | digests equal; a new row `cataphracts` with `mounted: true, charge: 3, wheel: true` charges, recoils and wheels with no code edit (the 2026-07-26 audit's falsifier, inverted) |
| 3 | `in_hand`, the two triggers, the tick | digests equal with every `secondary` null; archers with `secondary: arming` and the order `(enemy_range:2, {in_hand: secondary})`: volley events stop at the order's tick, one tick with no melee from that body, then melee without the missile handicap |
| 4 | the carry factors | with a `secondary` and `strength` at the seed: stamina at tick 7 and first-contact tick differ from the same body without it; at a raised `strength` they do not; over 72 ticks the carrying side recovers more slowly out of contact; the factor handed in equals the leaf evaluated on the same masses, asserted by calling it |
| 4, after arrangement | the trade is a trade | a pike body four ranks deep with `secondary: arming` and a `flanked` switch order, against the same body with no secondary, flanked by cavalry: the switching body's share lost differs beyond the same-run control at n 200; against a frontal charge it does not win more than the control |

**Tests (W3-1).** Stage 1: the exporter's `--check` (a new `tests/valoria/test_export_troops.py` beside
`test_engine_params_bridge.py`: `test_round_trip`, `test_unknown_arm_key_refused_by_name`,
`test_mass_stated_twice_refused`); `tests/valoria/test_field_golden_pins.py` for the digests. Stage 2:
`tests/valoria/test_mass_battle_order_of_battle.py::test_a_new_row_charges_and_wheels_with_no_code_edit`.
Stage 3: `tests/valoria/test_mass_battle_ammo.py::test_switch_stops_volleys_and_costs_a_tick`,
`::test_reached_archers_with_no_order_stop_volleying`. Stage 4:
`tests/valoria/test_mass_battle_order_of_battle.py::test_the_factor_handed_in_equals_carry_demand_of`.
**Call sites.** `troop_types/table.py` loader functions replace the tables at their present names
(`stats_for`, `reach_for`, `is_mounted`, `cell_cap_for`, `roles_for`, `loadout_for`, `training_site_for`);
`percell.update_stamina` and `Subunit._node_advance` read the factors. **Hash movers:** none at stages 1–3
with every `secondary` null; stage 4 only rows naming a second weapon. **Lands:** an IN-lane implementation
session under `/methodology-execute` with MB review; stages 1–2 mechanical (`sonnet`, `haiku` for the
transcription check), stages 3–4 `sonnet`.

## Falsifier

After stage 2, a troop behaviour that still depends on the spelling of a type's name
(`grep -n "troop_type == '" modules/mass_battle` prints a line). After stage 4, a carried second weapon
that changes nothing at any `strength`; a reached missile body that still volleys after switching; a
second roster or a second carry rule under `modules/mass_battle/`; any result that moves with every
`secondary` null.

## NERS (definitions `CLAUDE.md` §0.06)

- **N.** From the designer's direction: today a troop type cannot be added without Python in four files.
  From the player's: no equipment decision reaches a field. Laterally: the carry rule is personal
  combat's, at one owner. From below: reach already is a property of the weapon (the transcription shows
  it); the tables only say so twice. Cut the second weapon and Jordan's stated trade has no carrier.
- **R.** Customisation by row; a real trade (versatility against tiring and slowness) with a control at
  both ends; complete at the extremes (no secondary is today's battle; a strong troop pays nothing).
- **S.** One function for a person's and a unit's load; `in_hand` is the same state name and the same
  "costs the next action" rule as the duel round's; reach has one methodology (the arm's class).
- **E, last.** Twelve tables and four name tests become one file of two sections; one state field, two
  trigger kinds. A player can say why a unit is slow: it is carrying two weapons.

## Cost class

Stages 1 and 2: edit (mechanical, hash-equal). Stage 3: small build. Stage 4: small build, after
`03_PC_loadout_and_carry.md` and the arrangement change. The masses and `strength` values are content.

## Content for Jordan, surfaced by the transcription (not decisions of this proposal)

- `heavy_cut` and `heavy_blunt` are weight classes, not weapons, and both carry a pole weapon's reach
  today (heavy infantry, cavalry and knights templar read 0.2). What those troops hold is unstated.
- Knights templar: mounted or not.
- Which named weapons of personal combat's roster troops carry (`arming` is used above because the brief
  names it).

## Conflict with a ruled item, named

`ED-MB-0001` (Jordan, 2026-07-02): "Ranged is troop type as per the weapon assigned to troop." Read as
"per the weapon in hand" it is extended; read as a fixed property of the type it forbids the switch. The
brief of 2026-11-12 (archers carry arming swords; the switch is a state change) is the later statement.
