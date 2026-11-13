# A-98 · derived scores: the inventory from the tree

## Status: REFERENCE (a lane's read of the working tree, 2026-11-12; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: the working tree of `main`, 2026-11-12. Lane: A-98 vocabulary sweep. Ruling: `unified/DECISIONS_ANSWERED.md` A-98 part (5).

**The family.** A-98 (5): a **derived score** is a value computed from attributes, skills and state, never held as
a learned rank and never trained (Jordan: *"and then we have derived scores (health, wound count, etc)"*). The
tree's own list name for the family is `references/descriptor_registry.yaml: not_descriptors.derived_values`
(`:274`), which mixes a person's values (Health, Stamina, Composure, Concentration, Thread Fatigue, Resolve, Wound
Interval, Max Wounds) with a faction's and a settlement's (Mandate, Treasury, Settlement Weight, …). This file
lists **a person's** derived scores only; the faction, settlement and unit values are out of A-98's subject and
are noted at the end.

**What is not a derived score, settled here** (by the ladder, step 5: what the code computes and where):

- **A track** is stored state that events write: `Person.body` (`state/carriers.py:761`), `Person.body_ceiling`
  (`:768`), the fight's `WoundTracker.cumulative_damage`, and the per-fight live values `Combatant.stamina`,
  `.conc`, `.initiative`, `.poise` (`modules/combat/combatant.py:150-158`, reset and moved by `wrapper.py`).
  A derived score is computed *from* a track; the track is not itself computed. The registry agrees in shape:
  `category_b_scalars` registers `pc.wounds`, `pc.poise`, `pc.initiative` as kind `personal_track` (`:114-119`).
- **The pool** is not a derived score: it is the dice for one act, composed from the skill score, the act's
  addends and the base (`pool_of`, glossary *pool*), and it needs a verb to exist. Likewise the **opposition**
  (per act) and the **choice score** (per candidate act).
- **The skill score** is not a derived score: it is the held rank (A-98 (2)), read by `pool.py::score`.

## The inventory (a person's derived scores)

| derived score | computed from | owner `file:symbol` | who reads it | family |
|---|---|---|---|---|
| **Wound Interval** | Endurance + base + Spirit at low weight | `modules/combat/combatant.py:37` `wound_interval` | `WoundTracker.rederive` (`:74`); `seam/wrappers/combat.py` (docstring only) | health and wounds |
| **Max Wounds** | Endurance (`floor(End/2)+1`, capped at 3) | `combatant.py:32` `max_wounds` | `WoundTracker.wounds`; lifted to the season as `max_wounds` on the wound state (`seam/wrappers/combat.py:401`), read by `loop/effects_combat.py:413-418` (the lasting mark) | health and wounds |
| **full Health** | Wound Interval × (Max Wounds + 1) + Strength × Endurance at low weight | `combatant.py:42` `health_full` | `WoundTracker.felled`, `.health_remaining`; `modules/combat/wrapper.py`; `loop/effects_combat.py::_harm` (`:427`, the scene fraction) | health and wounds |
| **Health remaining** | full Health − the fight's damage (a track) | `combatant.py:79` `WoundTracker.health_remaining` | `wrapper.py`; `loop/effects_combat.py::_harm`, which writes `Person.body` from it (`body × health_remaining // health_full`) | health and wounds |
| **wound count** | the fight's damage ÷ Wound Interval, capped at Max Wounds + 1 | `combatant.py:83` `WoundTracker.wounds` | `combat_systems.py:1044` `wound_impairment` (the bilateral wound obstacle, `WOUND_ATK_OB`/`WOUND_DEF_OB`); `wrapper.py:34,40` (the trace); `loop/effects_combat.py:418` | health and wounds |
| **felled** | the fight's damage ≥ full Health | `combatant.py:88` `WoundTracker.felled` | `wrapper.py` (the fight's end); the season's `fight_endings` | health and wounds (a yes/no reading) |
| **body band** (between scenes) | how many `band_floors["body"]` floors `Person.body` has fallen past | `engine/season/decision/budget.py:71` `body_band_penalty` | `decision/budget.py::budget` (scene actions); `seam/wrappers/combat.py::party_end`; `loop/effects_combat.py`; `loop/driver.py`; `harness/probes.py` | health and wounds (the season's form) |
| **Endurance in the fight** | authored Endurance − one point per body band, floor 1 | `engine/season/seam/wrappers/combat.py:143` `party_end` | `combat_input` → `PersonalCombatInput.ends` → the module's `Combatant.end` | health and wounds (the hand-over) |
| **Stamina (maximum)** | 3 × Endurance + 2 × Spirit | `combatant.py:47` `stamina_max` | `Combatant.rederive` (`:181`); `wrapper.py`, `combat_systems.py` (drain and recovery against it) | reserves |
| **Concentration (maximum)** | `CONC_FOCUS` × Focus + `CONC_SPIRIT` × Spirit (ED-902) | `combatant.py:182` (`Combatant.rederive`, `conc_max`) | `wrapper.py`, `combat_systems.py` (`mental_fatigue`, `:1450`) | reserves |
| **age** | the clock − `Person.born` | `engine/season/queries/world_q.py:1241` `age_of` | `body_hazard`; `data/cast.py`; `harness/populated.py` | the body over time |
| **body hazard** | `illness_rate + age_step × age`, capped at 1 | `world_q.py:1248` `body_hazard` | `loop/matter.py` (the bodies draw) | the body over time |
| **standing** | the gap between what others say of a person and what he holds of himself | `engine/season/decision/options.py:1524` `standing_of` | `decision/options.py`, `loop/deliberate.py`, `loop/witness.py`, `loop/matter.py`, `loop/driver.py` | the interior `[ASSUMPTION: A-98 (5)'s "computed from … state" admits it; Jordan's examples are bodily; reversible]` |
| **confliction** | Σ over incompatible affiliation pairs of the weaker conviction (ED-IN-0251 R1) | `engine/season/queries/person_q.py:778` `confliction` | `decision/choose.py` | the interior (same assumption) |
| **religious intensity** | the highest conviction on a religious concern ÷ the ceiling | `person_q.py:819` `religious_intensity` | `person_q.crisis_weights` (`:849`) | the interior (same assumption) |
| **decisiveness** (proposed) | the length of `projected_axes(p)` | `person_q.decisiveness` (P, `proposals/02_CHAR_resolve_and_temper.md`; D-U1-11m) | `decision/choose.py` (proposed) | the interior (same assumption) |
| **legibility** (proposed) | how far others can read a person (A-43) | `person_q.legibility` (P) | per its proposal | the interior (same assumption) |
| **Thread Pool Score** | `floor(Thread Sensitivity / 10)` | `references/descriptor_registry.yaml: practitioner_stats` `prac.tps` (`:75`), registry only | **no reader** in `engine/` or `modules/` (grep, 2026-11-12) | practitioner |

**Registry names with no tree reader** (`not_descriptors.derived_values`): **Resolve** ("Spirit's derived value",
`descriptor_registry.yaml:33`), **Composure** (the knot damage track; read only by the oracles
`systems/fieldwork/sim/knots.py` and `systems/social_contest/sim/contest/*`, not by the game), **Thread Fatigue**
(no reader in `engine/` or `modules/`; the WR lane's `fatigue_scale_per_will`, U1 architecture §3 `thread` site,
proposes one). Each is a derived score by name; none is built.

## Mislabels (settled by the ladder; the glossary rows carry the words)

1. **"a pool that drains (health, stamina, composure)"** — `proposals/10_DICE_capability_axiom_map.md` §A, the
   `resource` role's axiom cell. The glossary's *pool* is the dice for one act; a reserve an attribute sizes is a
   **derived score** (its maximum) drained as a **track**. Step 3 (A-98 (5)) and step 5 (the code: `stamina_max`,
   `health_full` are maxima computed from attributes; `stamina`, `cumulative_damage` are tracks). Fixed in the
   sweep: "an attribute sizes a reserve that drains (a derived score: health, stamina, composure)". The `resource`
   role is the one door by which an attribute becomes a derived score; the `threshold` role prices against one.
2. **`faculty` in the combat attribute spec** — `modules/combat/attributes.py` SPEC holds
   `AttributeSpec('faculty', 3, None, None, IN_FLUX)`: the party's dice score for the fight's verb (its own
   docstring: *"the party's dice score for the verb that opened the fight"*), i.e. a **skill score**, carried as a
   combat **attribute** (`c.faculty`). A-98 (1)–(2): an attribute and a skill are different things. A tree name;
   not renamed here. D-U1-08 already replaces the input field `PersonalCombatInput.faculties` with `scores` and
   `addends`; the spec entry itself is not yet ordered out. **For the orchestrator:** whether the PC batch that
   lands D-U1-08 also removes the `faculty` entry from the attribute spec (the module would read the score from
   its typed input, not from `c.attrs`). Cost not measured.
3. **`disp` in the combat attribute spec** (`attributes.py`, `registry_key: None`): a temperament (the aggression
   lean), not one of the ten attributes. Under A-98's marked assumption it is a disposition (a trait), not an
   attribute. A tree name; listed, not renamed.
4. **Thread Pool Score** (`prac.tps`): a derived score whose name says both "pool" and bare "score". Registry
   only, no reader; the plain name is **Thread dice** or the derived score "Thread rating" `[ASSUMPTION: not
   decided here; a WR-lane naming when a reader is built]`.
5. **"Resolve"** — A-98's own restatement lists "resolve" among derived scores; Jordan's quotation does not. The
   word already names the RESOLVE loop step and `faction_q.resolve` (glossary *resolve*; D-U1-11m renamed the
   proposed person reader `decisiveness`). The registry's "Resolve" (Spirit's derived value) has no reader. The
   suite does **not** use "resolve" for a derived score; a built one takes a different name (decisiveness is the
   one proposed).
6. **`Combatant.skills`** (`combatant.py:140`, a per-axis bias): these are **combat axes** (glossary *skill*,
   unchanged), not skills.

## Out of A-98's subject (not a person's)

A unit's `eff_morale` (`modules/mass_battle/hierarchy/units.py:683`, the troop-weighted mean of its cells'
morale) and `eff_stamina`, `eff_stamina_max` (`:778-783`) are a **unit's** derived values; a unit's **prowess**
(A-59, `27_MB_B`) is composed from its row. The faction and settlement entries of `derived_values` (Mandate,
Treasury, Levies Available, Public Order, Settlement Weight, …) belong to those lanes. The mass-battle lexicon
(`unified/MB_LEXICON.md`, another lane) owns the unit words.
