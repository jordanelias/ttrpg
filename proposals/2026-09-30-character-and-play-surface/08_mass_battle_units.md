# Mass battle units — what the engine allows, and how units should be designed

## Status: PROPOSED (2026-09-30) · design-only · ratifies nothing on merge · reference under `CLAUDE.md` §0.05
## Lane: MB, with PC for equipment · IDs: none allocated
## Read at HEAD `c8cc408` (no `systems/` file changed in #444).
## Suite: [README](README.md) · [05 two modes](05_two_modes_of_one_bout.md) · [06 weapons](06_weapons_from_physics.md) · **08** · [09 character sheet](09_the_character_sheet.md)

**What this answers.** What kinds of unit, and which qualities, `systems/mass_battle/sim/` supports
today; which of them reach a battle; and how units should be designed so that they compose from the
same primitives as everything else rather than acquiring a stat line of their own.

---

## 1. Analysis

### 1.1 Troop types

`troop_types/registry.py::TROOP_TYPE_STATS` gives **ten** types a preset of three per-subunit stats,
transcribed from the design's troop table (`mass_battle_v30.md` §B.2):

| type | power | discipline | morale |
|---|---|---|---|
| levy | 1 | 1 | 2 |
| sling | 2 | 2 | 3 |
| artillery | 2 | 2 | 3 |
| light infantry | 3 | 3 | 4 |
| archers | 3 | 3 | 3 |
| crossbow | 3 | 3 | 3 |
| heavy infantry | 4 | 4 | 5 |
| pike | 4 | 4 | 5 |
| cavalry | 5 | 5 | 5 |
| knights templar | 5 | 6 | 6 |

`pike` is marked provisional-by-analogy: the troop table has no pike row, so it mirrors heavy infantry
and differs only by reach. **`mounted_archers`** has reach, roles and a density cap but no stat preset.
The registry leaves armour (`dr`) and endurance (`stamina`) unbridged from the troop table on purpose —
the table's armour column and 1–6 endurance have no confirmed mapping to the engine's fields, and the
comment defers them rather than guess.

### 1.2 Reach, shape, role

- **Reach** (`TROOP_TYPE_REACH`, Jordan's P-DEC-1): 0.1 lattice units for ordinary melee and missile
  troops' sidearms, 0.2 for spear and lance (heavy infantry, cavalry, knights), 0.3 for the pike. It feeds
  an oriented-box front-reach overlap, so a pike block genuinely holds cavalry off at a distance a
  sword line cannot. Its reconciliation with the older metre-scale reach terms is deferred.
- **Shape** — `Line`, `Arrowhead`, `GappedLine`, `Column`, each with a minimum discipline to hold
  (1, 4, 5, 3). Horseshoe and refused flank were retired as shapes; they emerge from several bodies.
- **Role** — `TROOP_TYPE_ROLES` gates which roles a type may take (heavy infantry: ShieldWall, Hold,
  Anvil, Push; cavalry: Shock, Flanker, Feint, Screen, Pursue; archers: VolleyLine, Harass …), and
  `ROLE_SPEC` gives each role a shape and an instruction package (ShieldWall → Line + brace, hold).
  ⚠ Both are marked **"SCAFFOLD — data only; INERT"** (`config.py:568`): no instruction reaches a
  primitive yet. Roles are a menu, not a mechanism.

### 1.3 Size, cells, morale, facing

- **Size**: `TROOPS_PER_TIER {1: 100, 2: 200, 3: 400, 4: 800}`; cells hold 40–200 troops; a unit caps at
  10,000; a subunit routs below 80.
- **The cell is the primitive** for morale (per-cell morale is live, and `CELL_MORALE_PULL` draws each cell
  toward the subunit mean; the magnitude is marked calibration debt).
- **Rout** is stochastic between **15 %** and **30 %** losses (Jordan's historical research,
  2026-07-23).
- **Facing** is an octagon that multiplies damage received — front 1.0, flank 1.5, rear 2.0
  (ED-MB-0018) — with a two-tick reaction lag and compounding shock when struck from several sides.
- **Volleys** reach 2–8 cells and scale with the target's packing (a dispersed line bleeds at half the
  reference, a deep column up to double).

### 1.4 Equipment: two thin catalogues waiting to be merged

`equipment/weapons.py` and `equipment/armour.py` both say *"NOT YET WIRED into resolution"*. A weapon is
four tags — damage type (cut, blunt, pierce), weight band (light, heavy), reach (melee, ranged) and
keywords (`anti_armour`, `anti_cavalry`, `volley`, `armour_piercing`, `pole`). Armour is four tiers
whose only grounded number is `dr_vs_piercing` 0/1/2/3. Both modules state their purpose: to be
*"re-mapped onto the scene-combat (personal) weapon model"* — the physics of [06](06_weapons_from_physics.md)
— without a schema change. One derivation is already right: a unit's `unit_type` (melee or ranged) comes
from its assigned weapon's reach, per Jordan's ruling *"Ranged is troop type as per the weapon assigned
to troop."*

### 1.5 What actually builds the armies that fight

- **In the season loop**, `seam/wrappers/mass_battle.py` calls `massbattle.resolve_field`, which builds
  each side with `_weighted_unit` (`massbattle.py:283`): **troops = the summed `Person.weight`** of those
  mustered, but power fixed at 4 and morale at 5. Headcount is the only input from the world.
- **Cohorts** arrived with #444: `engine/season/cohorts.yaml` seats one weight-2 `Person` per settlement
  (37 rows), used today for subsistence, population and migration capacity.
- The mc_v18-era `_faction_to_unit` (power from `Mil`, morale from `Sta` since ED-MB-0068) is reached only
  from `resolve_mass_battle` on mc_v18's conquest path; the plan's end-state deletes both.
- **Officers** (`hierarchy/units.py::Officer`) carry `command`, `charisma` and `cognition`; when both
  of the latter are set, `command = derive_command(charisma, cognition)`, clamped to 1–7. These are
  mass-battle fields; no `Person` supplies them ([09](09_the_character_sheet.md)).
- `march` executes on the populated realm (`build_realm(0)`), and is never attempted in the 143-case
  corpus.

### 1.6 What the precedent research says about units

The repository's own survey (`research/valoria_game_precedent_companion_v1_part2.md` §3.1) found four of
four franchises treating **garrison as an assignment** of the same pool, never a unit type (X5), and four
of four treating **levy and professional as different economies**, not tiers (X4); it also recorded that
gating troop types on an officer's **class** survives losing the officer, while gating on **biography**
does not (S4). Those were written against the older campaign, but they are statements about design shape
and still apply.

---

## 2. How units should be designed

A unit should be **composed**, not authored. Every part it needs already exists somewhere in the tree:

| a unit is… | drawn from | status |
|---|---|---|
| **who** — its bodies | a cohort `Person` (weight = headcount) or named persons at the rung | exists; feeds troop count only |
| **what they carry** | a loadout of weapon and armour records from the one physics model | catalogues exist, unmerged |
| **who leads** | an `Officer` who is a `Person` | Officer exists; no Person feeds it |
| **how they fight** | role → shape + instructions, with instructions wired to primitives (brace → density and hold, charge → momentum) | scaffold, inert |
| **what kind it is** | a label derived from loadout and training, not a preset | presets exist; derivation does not |

The troop-type presets are a useful bootstrap and a poor destination: a preset is a hand-set stat line
of exactly the kind [06](06_weapons_from_physics.md) shows the personal engine retiring for weapons.

---

## 3. Recommendations

| # | recommendation | where | observable (falsifier) | cost | gate |
|---|---|---|---|---|---|
| **U-1** | Give `_weighted_unit` inputs beyond headcount: power and morale from the mustered persons (their loadout and condition), not fixed 4 and 5. | `massbattle._weighted_unit`, `seam/wrappers/mass_battle.py` | two musters of equal weight and different loadout produce different fights over N seeds | medium | MB, after U-2 |
| **U-2** | Merge the equipment catalogues with the personal-combat records, as both modules say they will: a troop's weapon is a weapon record; reach, armour-defeat and percussion derive from the same functions; retire `provisional`. | `equipment/`, `troop_types/registry.py` | the pike's front reach derives from its record's `head_len` rather than the 0.3 constant | medium | MB + PC |
| **U-3** | Wire role instructions to primitives, or stop presenting roles as a design axis until they are. | `ROLE_SPEC`, subunit behaviour | a `ShieldWall` and a `Push` of the same subunit produce different density and advance | medium | MB |
| **U-4** | Officers as persons: read `charisma` and `cognition` from the character sheet of whoever holds the command. `derive_command` stays the owner of the composite. | `Officer`, [09](09_the_character_sheet.md) | changing a seated commander's cognition moves `command` | small | after [09](09_the_character_sheet.md) K-2 |
| **U-5** | Give `mounted_archers` a stat preset or write down why it has none. | `TROOP_TYPE_STATS` | — | trivial | MB |
| **U-6** | Resolve the deferred armour and endurance bridges through U-2 — an armour record's tier maps to the same tiers `coupling` uses — instead of guessing a 1–6 → 0–100 conversion. | `troop_types/registry.py` comment | `Subunit.dr` equals the armour record's tier value | small | with U-2 |

**One item would need Jordan if pursued:** splitting `Muster` into levy and professional economies (X4).
The research notes that splitting a ratified action is a canon change. This suite does not propose it
now; it records where the ruling would sit.
