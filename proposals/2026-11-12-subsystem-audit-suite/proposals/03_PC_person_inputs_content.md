# PC — per-person combat inputs: the slot interface, a starter inventory, the unarmed fighter, and seeding

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` §1.1, §1.4, §1.5) — four changes. (1) The authoring home is decided: `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §1–§3 (definitions in `references/descriptor_registry.yaml`, uses in `rosters.yaml: tables.capability_uses`); Part A's slots are that surface's `fight` site, not a second scheme. (2) A-7, A-6: the `pool` slot is the **trained score** alone (dice by the one pool rule); talent is the `attr` family, applied by the module's own sigma; the opponent's obstacle keeps its value (A-31) (`U5b_PC_rulings_in_the_fight.md` §2). (3) Addendum R-PC-43: `technique` and `grab` are not exposed as `skill` slots until a sweep shows them outside the interval, and a skill's bound is its capability row's (`U5b_PC_residue.md` §1). (4) Pessimist R-9: Part B admits a kind only with its census row (`U5b_PC_residue.md` §3). A-11 stands: a capability supplies numbers and gates no act; the tradition's access table gates which technique rows compose, not whether a person may fight.

## Status: PROPOSED

Lane: PC, with CHAR (who authors a person) and SE (stores as arms). Source: `audits/03_PC_audit.md`
F-PC-02, F-PC-12, §14; resolutions R-PC-12, R-PC-13. Read at `601e715`. Reference only (CLAUDE.md
§0.05); not ratified by being written. **Every content value in Part B is `[ASSUMPTION; low; Jordan to
correct]`: the roster's own note reserves the inventory to Jordan (`engine/season/rosters.yaml:1848-1851`).
The mechanism in Parts A and C does not depend on the values.**

## What it changes in `engine/season/` at runtime

Part A: nothing until a slot is filled (every new field defaults to the value the engine uses today).
Part B and Part D: persons stop being identical fighters; a declared mover of every season fight
between persons whose inputs differ. Part C: a person who holds no weapon fights unarmed once an
inventory exists.

## The problem, with evidence

`build_realm(0)`, read at this SHA: 83 of 83 persons have no authored attribute, kit `(arming, light)`,
`faculty(fight)` 2 and `party_end` 4; nobody holds `arms`. The mechanisms are present and read empty
sources: `modules/combat/fight.py:44-52` (attributes), `engine/season/queries/world_q.py:3484-3509`
(kits, over `arms_kinds: {}`), `engine/season/seam/wrappers/pool.py:78-100` (faculty),
`engine/season/loop/effects_combat.py:271-296` (growth, which never mints a key). Tradition, technique
investment, the six skill axes and disposition have no carrier on a person and no field on the record.
What the engine would do with them, 1,000 fights per cell at the season default: one point of faculty
moves a mirror's win share from about 50% to 64%; a longsword against an arming sword 77%; heavy
against light armour 93% with no death of the wearer; Strength 6 against 4, 69%; an aggressive
disposition 56%.

## Part A — the slot interface (the module declares what it can take; the host fills it from data)

The module owns one list of input slots and nothing about who fills them. Extend
`modules/combat/attributes.py` (already the one owner of the attribute spec, PC-14) with two more
tuples in the same form, exported in the typed export's `attributes` section:

| slot family | members (as the engine reads them today) | read at | scale |
|---|---|---|---|
| `attr` | `strength, agi, end, att, spirit, focus` | `attributes.SPEC`, by `registry_key` | registry's 1 to 7 |
| `pool` | `faculty` *(Reconciled, A-7:)* the party's **trained score** (training gives dice; never the larger of attribute and key). The opponent's obstacle is read from the defender's score at the fight's own rate (A-31) | `core.py:54-58`, `:102-124` | a real number; the pool is `max(pool_floor, score + pool_add)`, unrounded |
| `skill` | `balance, parry, dodge, bind` *(Reconciled, R-PC-43: `technique` and `grab` measured inside the interval, 50.1% and 47.6% at +1, and are withheld from the slot family until a sweep shows otherwise)*; the engine's read sites for all six stand | `combat_systems.py:198`, `:345-362`, `:1060`; `contact.py:46` | additive σ bonus, 0 untrained |
| `lever` | `visual, precommit, tactile, tempo, balance, measure, leverage, counter_select, counter_success, anti_overcommit, edge_read, spine_press, edge_grab, choke_control, facing_regime` | `ability_primitives.py:188-218` and its callers | a factor (`*`) or a bonus (`+`) |
| `temper` | `disp` (the aggression axis) | `combat_systems.py:190-193` | 1 to 7, 4 neutral |
| `kit` | `weapon`, `armor` | `combatant.py:112` | a `weapons.py` key; an armour tier |

`PersonalCombatInput` (see `03_PC_typed_outcome_one_door.md` Part B) carries, per party, a mapping per
family. The module takes **numbers per slot**, never the name of a skill, technique or tradition: the
host composes a person's capabilities into slot values by the authoring surface's rule. That makes
`ABILITIES`, `TRADITION_KIT` and the tradition gate (`ability_primitives.py:30-185`) authoring data and
host-side composition, not module code; the module keeps `ability_factor`'s clamp and the lever maths.

## Part B — a starter inventory (content; Jordan's to correct)

- `engine/season/rosters.yaml: matter_kinds` gains seven kinds; `arms_kinds: kinds:` maps them:

  | kind | field | key | rank |
  |---|---|---|---|
  | `arms_dagger` | weapon | `dagger` | 1 |
  | `arms_spear` | weapon | `spear` | 2 |
  | `arms_sword` | weapon | `arming` | 3 |
  | `arms_longsword` | weapon | `longsword` | 4 |
  | `harness_light` | armor | `light` | 1 |
  | `harness_mail` | armor | `medium` | 2 |
  | `harness_plate` | armor | `heavy` | 3 |

- `arms_at_build: kinds:` seeds a small count on the rung kinds that would hold them (a settlement's
  armoury, a seat-holder's own holding). `[UNVERIFIED: the `rung_kinds` roster was not opened; the
  loader refuses a key that is not a member, so a wrong name fails at import, not silently]`.
- The ranking is by the engine's own measured ordering against an arming sword at light armour, not by
  taste; a different ranking is one edit.
- *(Reconciled, pessimist R-9.)* A kind joins `arms_kinds` only with its row of the roster census named
  in the commit (`U5b_PC_residue.md` §3): no cell beyond 95% against the kinds already admitted, or its
  answering kind admitted with it. On the readings taken before the calibration batch, `arms_spear`
  (99.2 to 99.8% against the arming sword) and `harness_plate` (0 fellings in 2,800) would each fail
  alone; the census is re-run after that batch and decides.

## Part C — the unarmed fighter

- `modules/combat/weapons.py` gains one record, `unarmed`: a one-handed blunt element with the mass
  and lever of a forearm and fist, `head_len` below `GRAB_SHORT_REACH_M` so `contact.py:19-27`'s
  open-contact exemption (which already speaks of an unarmed class) applies to it. It is a physical
  record like the other 54; nothing in the engine branches on its name.
- `engine/substrate/combat_kit.py` exposes it as the weapon a person holds when he holds none;
  `queries/world_q.py::kit_of` returns it for the weapon field when `ARMS_KINDS` is non-empty and
  neither his holdings nor his residence stock a weapon. While `ARMS_KINDS` is empty the default stays
  as it is, so nothing moves until Part B lands.
- Cost stated: a new roster record re-records `tests/valoria/r3_identity_golden.json` and the armour
  reference (`workbench/data/combat_armour_reference.json`) by their own generators, and must pass
  `tests/valoria/test_combat_invariants.py`.

## Part D — seeding who can fight (dependency on CHAR)

- `rosters.yaml: lifepath_templates`: the martial lifepaths hold `arms` (the template already says
  which `verb_capability` values a lifepath's starting skills draw on; `arms` was added to
  `verb_capability` at CP-T03-04 and no template names it). Held at `pool_default`, so no pool moves at
  creation; it makes `arms` a key that `train` and build-by-doing can raise.
- Authored attributes for realm persons are CHAR's (nothing generates a person's attributes today);
  the combat seam already reads them.
- Tradition and disposition: no carrier is proposed here. PC-21 (design-first) owns where a tradition
  lives; the approach choice in `03_PC_duel_round_and_approach.md` supplies the per-phase temperament.

## Gate (execution artifacts)

- The realm reading re-run: the count of distinct `(kit, faculty, end, attributes)` tuples over
  persons is above 1, reported per seed 0 to 2.
- R-09's by-person conjunct, for combat: two persons with different inputs, the same opponent and the
  same seed set, show different felled shares outside the disjoint-seed control band (46.1 to 49.3 in
  the mirror).
- `python tools/export_engine_params.py --check` green with the slot tuples in the export.
- With `arms_kinds` emptied and the templates reverted, the pre-change season hashes return.

## Falsifier

A realm in which every fight is still pool 8 against obstacle 1.0 after the content lands; a person
with no stocked weapon who still fights with an arming sword; a skill or lever value that changes an
outcome without appearing in the record.

## NERS reading

- N: from above, R-09 and R-06 cannot read for combat while every fighter is the default; from below,
  about 220 exported coefficients have nothing to act on; laterally, mass battle's troop quality
  wants the same equipment model (Jordan, 2026-10-16, statement 1 in `research/by_lane/README.md`).
- R: customisation of a character becomes real (kit, training, body); the no-player half gains
  mismatched fights, which is where upsets and reputations come from.
- S: one slot interface for the duel, the grid round and a duel inside a field; one equipment roster.
- E, last: Part A adds two tuples and four record fields and removes three module-side tables from the
  module's concern; Part B is seven roster rows. High, provided the tradition layer is not extended
  before a carrier exists.

## Cost class

Part A: small build. Part B: an edit, content Jordan's. Part C: small build with two generated
artifacts re-derived. Part D: an edit plus CHAR's attribute authoring (design-first there).
