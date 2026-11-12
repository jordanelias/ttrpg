# PC — the typed export carries the weapons, the wound model and the physics constants, not their names

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` §1.4) — item 6 is confirmed from the MB side and named: one owner a fact, not one file (`04_MB_unit_loadout_and_weapon_in_hand_B.md` §2, R-36): an arm's mass lives here when its key is in this roster and in `references/troops.yaml: arms` when it is not, and that loader refuses a mass stated in both. The carry leaf reads the exported `mass` through its keyed spelling and takes bare masses for a troop row (`03_PC_loadout_and_carry.md` as reconciled). A-29 (declared floats) means the `derived` section's 1e-9 parity is stated against the float contract `11_GO_float_contract.md` carries (U5d's), not against integers. No edit below changes.

## Status: PROPOSED

Lane: PC, with GO (the port reads the export) and MB (one weapon roster). Source:
`audits/03_PC_audit_addendum_B.md` F-PC-15 and F-PC-20; it widens the first audit's F-PC-10 and
R-PC-18. Read at `2c24c81`. Reference only (CLAUDE.md §0.05); not ratified by being written.

## What it changes in `engine/season/` at runtime

Nothing. `engine/substrate/combat_kit.py` reads the `kit` section only; the one behavioural edge is
that `kit.weapons` stops listing the four half-sword forms, so `rosters.yaml: arms_kinds` could no
longer name a form as a person's weapon. The shipped roster is empty.

## The problem, with evidence

CLAUDE.md §5 and §6: a value the port uses comes from a typed artifact behind an exporter, never from
prose and never hand-transcribed. `engine/engine_params/combat_engine_v1.json` states its source as
`config.py + core.py + attributes.py + weapons.py + vocabulary.py + combatant.py`
(`tools/export_engine_params.py:141`). What it holds (probe `probe_weapons.txt` and a follow-up
count, addendum §B11):

| the oracle owns | in the export |
|---|---|
| `config.CFG`, 214 keys | all |
| `core.py`, 19 numeric module constants and its tables | 18 of the 19, and the tables |
| 54 weapon records: mass, lengths, hands, head, located parts, geometry, mode elements, edges, adornments (`modules/combat/weapons.py`) | **the 54 names** (`sections.kit.weapons`); no field of any record |
| `weapon_physics.py`, 33 module constants (`PERC_SCALE`, `PERC_EXP`, `PERC_CAP`, `AGILITY_EXP`, `AGILITY_REF`, `HEFT_REF`, `THRUST_POB`, `STRIKE_HAND_LEVER`, the `GRIP_*` bounds and the rest) | none |
| `combat_systems.py`, 18 module constants (the first audit's F-PC-10) | none |
| `combatant.py`, 8 constants: the whole wound and stamina model (`WOUND_INTERVAL_BASE`, `SPI_WI_W`, `STR_HEALTH_W`, `MAXWOUNDS_DIV`, `MAXWOUNDS_ADD`, `MAXWOUNDS_CAP`, `STAMINA_PER_END`, `STAMINA_PER_SPIRIT`) | none |
| `ability_primitives.py`: 30 abilities and 3 bounds; `traditions.py`: 8 traditions, the adjacency and 2 familiarity constants | none |
| inline literals in function bodies (the engine's own `structure_scan.py` counts 94: `weapon_physics` 40, `combat_systems` 24, `geometry` 13, `contact` 9) | none |

So a port regenerating from the export has the coefficients of the σ assembly and no weapon to apply
them to, no Health and no Wound Interval. The engine's central design claim (a weapon is its physical
primitives and every behaviour derives from them) is exactly the part that does not cross. Two
smaller defects ride with it: `kit.weapons` lists `longsword_halfsword`, `estoc_halfsword`,
`greatsword_halfsword` and `flamberge_halfsword` as things a person can be armed with, though they
are grips the engine switches into (`weapons.py:136-137`, `:926-934`); and `config.py:1`'s "all
tunable coefficients in one place" has been recorded false since the July wiring audit and is false
at this SHA.

**The roster's coverage, for the one-roster merge the MB lane proposes**
(`04_MB_unit_loadout_and_weapon_in_hand.md`, its R-27: personal combat's roster becomes the only
one). The personal roster is melee only. It has no pike, javelin, bow, crossbow or sling, which are
five of the ten classes of `modules/mass_battle/equipment/weapons.py::ARSENAL`; no shield (ruled out
of scope, ED-PC-0055 last row); no unarmed record (the first audit's F-PC-12). The engine has no
ranged resolution at all.

## The resolution, decided

| # | decided | ladder step |
|---|---|---|
| 1 | The export gains a `weapons` section: for each record its **authored** fields, in the schema `weapons.py:10-70` states. Baked fields (`geo`, `gap`, `_derived`, `hand_guard`, `blade_guard`) are not exported as inputs | 3. CLAUDE.md §5: the typed layer is where a value the port uses lives |
| 2 | The export gains a `derived` section: per startable weapon, the quantities `workbench/catalogue.py::QUANTITIES` already enumerates (heft, agility, percussion authority, reach, tempo and the rest), computed by the oracle. It is the parity oracle a port checks its own derivation against, never an input | 4. The catalogue is the tree's own list of derived quantities, generated from code |
| 3 | The exporter collects the numeric constants **defined in** `weapon_physics.py`, `combat_systems.py`, `combatant.py`, `ability_primitives.py` and `traditions.py` into sections of those names, by the syntax tree (assignment targets in the module's own body), not by `dir()`: `combat_systems` imports `WEAPONS` and `NEUTRAL`, which `dir()` would sweep in | 4. `_module_constants(core)` is the precedent; the narrowing is what keeps it honest |
| 4 | `kit.weapons` lists the records without a `base` (50); `kit.forms` maps each form to its base (4) | 5. A form is not a kit; `workbench/balance.py:36-38` and `catalogue.py::roster` already exclude forms by that test |
| 5 | The first audit's R-PC-18 (move the 18 `combat_systems` constants into `CFG`) is kept as the better end state for tunables; item 3 is what makes the export complete in the meantime and covers the constants that are physical anchors rather than tunables | 3 |
| 6 | Roster coverage is **not** built here. A pike is authorable today in the existing schema (a `hafted_tip` record longer than `yari`), and is content. A ranged weapon needs a ranged resolution, which the engine lacks and which no design at this SHA specifies for `combat_engine_v1`. Until one exists, MB's ranged classes cannot be rows of the personal roster; they need only a `mass` to be charged by `carry_demand` (`03_PC_loadout_and_carry.md`), and that one field is the declared exception to "one roster" | 3 for the pike (the schema decides); 5 for the exception |
| 7 | Inline literals stay where they are; the count is reported by `structure_scan.py` and each is a candidate for `CFG` on the pass that next touches its function | 2. No reader needs them moved today |

## Exact edits, by owner

1. `tools/export_engine_params.py`: `_weapons_section(weapons)` (authored fields only, an explicit
   field list taken from the schema header and refused on an unknown field, so a new field is a
   deliberate schema bump); `_derived_section(...)` calling the catalogue's quantity registry;
   `_defined_constants(path)` over the five modules; `_kit_section` split into `weapons` and `forms`;
   `SCHEMA_VERSION` 7 → 8 with its note.
2. `engine/engine_params/combat_engine_v1.json`: regenerated, committed with the exporter.
3. `modules/combat/config.py:1`: the header sentence corrected to say which constants `CFG` holds and
   which live with the physics (R-PC-18's wording if that lands first).
4. `engine/substrate/combat_kit.py`: `WEAPONS` reads the 50; `FORMS` added for a reader that needs
   the mapping. No season file changes.

## Gate (execution artifacts)

- `python tools/export_engine_params.py --check` green on the new shape.
- A script that rebuilds every weapon from the exported `weapons` and constant sections **alone**
  (no import of `modules/combat/weapons.py`) and recomputes the `derived` section reproduces it to
  1e-9 for all 50. This is the round trip the port will have to pass; run once here it shows the
  export is sufficient.
- `structure_scan.py` section [H] (dead exported keys) still prints `[]`.
- `build_realm(0)` one-season hash EQUAL.

## Falsifier

A quantity the engine computes for a weapon that cannot be recomputed from the export; a constant
defined in one of the five modules and absent from its section; a form accepted as a person's kit; a
second copy of a weapon's mass in MB's tables after the merge for a weapon the personal roster holds.

## NERS reading

- N: from the port's direction, the oracle is unreadable without it; from the designer's, a weapon
  is authored once and should be visible once; from MB's, a shared roster needs a place both scales
  read. From the season's direction nothing changes, and the proposal says so.
- R: completeness. A weapon is the game's main lever on a fight (the workbench's archetype table
  still lands four different builds at 93.6 to 95.7 because of the weapon), and it is the one thing
  the typed layer does not carry.
- S: one export, one round trip, the same collection rule for every module.
- E, last: three exporter functions and one regenerated file, against hand-transcribing 54 records
  and 64 constants into a second language.

## Cost class

Edit (the exporter and one regenerated artifact). The parity script is a one-off run, not a new gate.
