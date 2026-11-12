# DICE — adversarial steelman audit, addendum B

## Status: REFERENCE (an audit addendum; resolves nothing at runtime)

## Read at: 618ec4b (working tree; the first audit was read at 601e715)

Addendum to `10_DICE_audit.md`. It does not edit that file or its five proposals. It covers what that
audit reported as unread, closes H-152 by a run, corrects the first audit where a second reading or a
probe shows it wrong, and writes the capability → axiom → resolver input map as a proposal
(`../proposals/10_DICE_capability_axiom_map.md`). Finding numbers continue from `F-DICE-14`.

## 0. Verdict on the first audit

The first audit's verdict stands and is sharpened: the dice engine is sound and is fed a constant.
What the first audit did not see, because it had not read `derived_stats_v30.md` and its sources, is
that the constant is not only a missing content switch. The design's capability model (attribute
doubled plus History plus three, floor five; derived resources that drain; a wound as a fraction of an
obstacle) and the season's built model (the score is the pool; the opponent's score halved is the
obstacle; a modifier is a named sigma level) are two different sets of RPG axioms, each internally
coherent, and the tree runs three of them at once: the season's, personal combat's, and mass battle's.
The sections below state each, by code, and the proposal names one authoring surface over them.

(Sections 1 to 6 follow; this head was written before the reading finished, per the brief.)

## 1. What was read

**In full.** `AUDIT_BRIEF.md`; `CLAUDE.md`; `dossiers/10_DICE.md`; `audits/10_DICE_audit.md`; three of the
first lane's five proposals (`10_DICE_one_roller_one_fraction_rule.md`, `10_DICE_one_score_two_roles.md`,
`10_DICE_advantage_sources_for_the_arcs.md`; the other two are known here only through the audit's own
account of them). Design set (archived, intent only): `derived_stats_v30.md` (613 lines) and its `_index`;
`complete_systems_reference.md`; `videogame_mode_spec.md`; `engine_atlas_v1.md`; `scale_transitions_v30.md`
§1 to §11 (`:20-318`; §12, Key delivery, describes a retired substrate and was not read);
`canonical_registry.md` Hierarchy 4 (`:140-211`, the individual scale: attributes, the universal pool, the
universal obstacle, derived values). `proposals/2026-11-05-attribute-rulings-by-subject.md` (Jordan's words
of 2026-11-05, ED-IN-0347). `proposals/2026-08-23-suite-01-rulings-and-execution.md` §0 and §3.1 (the
source of *Ruling C*, below). Other lanes' capability and loadout proposals, so that §4 states one
interface and not an eleventh: `01_CORE_capability_authoring_surface.md` and
`02_CHAR_capability_uses_table.md` in full; `05_SC_capability_surface.md:1-110`;
`06_FA_office_capabilities.md:1-50`; `03_PC_loadout_and_carry.md:26-106`;
`04_MB_unit_loadout_and_weapon_in_hand.md:16-93`; `11_GO_one_draw_owner.md:1-40`.

**Searched for the resolution terms (pool, Ob, TN, degree, derived, attribute, dice, sigma) and read at
every hit.** `integration_proposal_v30.md` (21 hits), `throughlines_complete.md` (8),
`campaign_architecture_v30.md` (19), `campaign_modes_v30.md` and `_infill` (11), `cogload_moderate_target.md`
(16), `conflict_architecture_proposal.md` (6), `early_game_ignition_analysis.md` (3),
`companion_app_design_note.md` (1), `hybrid_gaps_v30.md` (3), `session_a_spec_patches.md` (5). No hit:
`scale_transitions_v30_index` / `_infill`, `integration_proposal_v30_index`, `tensions_pair_validation.md`.
What these carry is the same thing eleven times: modifiers as whole dice (`+1D`) and whole obstacle steps
(`−1 Ob`, `+2 Ob`), and `floor(stat/2)+1` as the opposed obstacle. None states a pool, an obstacle or a
ladder that `derived_stats_v30.md` and `canonical_registry.md` §4 do not.

**Research.** `research/provenance/2026-08-28-systems-integration-harvest/`: `synthesis/SYN_GROUP_C.md:278-303`
(a twelve-row synthesis of the resolution kernel's seams), `H1.md:60-92`, and the kernel hits in `H2`, `H3`,
`H5`, `H9` and the harvest contract. The game-precedent companion, parts 1 to 8, at its fourteen kernel
lines; read around them in part 3 (`:205-216`), part 4 (`:146-155`), part 5 §12.9 (`:190-202`) and part 8
(`:50-60`). `research/historical/` (three files): a search for the kernel's terms returns nothing; not read
further.

**Tests the first audit named as unread.** `tests/valoria/test_knot_pool_formula.py` in full;
`tests/valoria/test_fractional_pool.py:1-34`; heads and test names of `engine/tests/test_sigma_leverage_parity.py`,
`engine/tests/test_knots_ed912.py`, `tests/valoria/test_engine_params_bridge.py`,
`tests/valoria/test_dice_engine_properties.py`. The bodies of the last four were not read.

**`.audit/` (lesser weight).** A census of all 35 entries for the kernel's function names: 16 carry one.
Read at the hits that bear on the roller: `2026-07-22-mass-battle-stress-test/fable_logic_audit_v1.md:38-45`
and `fiat_register_v1.md:117`; `2026-07-26-mass-battle-fable-audit/03_execution_plan.md:138-148`. The other
entries were not opened.

**Code, for this addendum.** `seam/wrappers/pool.py` (all); `seam/wrappers/sigma.py:60-258`;
`modules/social_contest/roll.py` (all); `modules/mass_battle/resolution.py` (all), `core/exchange.py:20-154`,
`orchestration.py:1218-1327` and `:1536-1550`, `equipment/_base.py`, `equipment/weapons.py`;
`modules/combat/core.py:1-150`, `attributes.py`, and in `combat_systems.py` `wield_heft`, `act_cost`,
`str_demand`, `handling_penalty`, `wound_impairment`; `loop/effects_combat.py:451-680`;
`state/gate.py:1690-1860`; `state/carriers.py` (`Person`); `seam/wrappers/mass_battle.py:225-281`;
`seam/wrappers/combat.py` (`combat_input`, `party_end`); `rosters.yaml:1498-1614`, `:3479-3650`;
`decision/sheet.py` (head); `tests/test_cp_t02_01_death_names_seats.py`; `tests/test_march.py:1-140`,
`:300-410`.

**Ledger rows opened by hand** (PP and ED provenance is unvalidated by tooling): ED-833, ED-836, ED-884,
ED-934, ED-901, ED-902, ED-939, ED-1041, ED-PC-0005, ED-PC-0006, ED-MB-0032 (both rows), ED-IN-0196,
ED-IN-0328, ED-IN-0330, ED-IN-0350; `registers/handoffs/HANDOFF_archive.md` *Resolver architecture — RULED
2026-08-15* and *PARTLY RULED 2026-08-23 — faction stats*.

**Not read.** `[SKIPPED: proposals/2026-10-16-attribute-derivation*, attributes-from-scratch*,
character-template*, 2026-11-05-verb-attribute-map*, 2026-11-05-attribute-rulings-adjudication,
2026-10-24-character-layers-*, 2026-11-05-cr85-* — Status lines only (all PROPOSED or held back; the one
ratified item among the brief's starting points, 2026-10-07-character-sheet-spaces, was read through its
code, decision/sheet.py); the CHAR lane owns their reconciliation]`. `[SKIPPED: the rest of
.designs/systems/_architecture/ (key substrate, governance, holonic doctrine, player agency, propagation) —
outside the resolution subject]`.

## 2. Corrections to the first audit, and new findings

### 2.1 Corrections

| # | the first audit says | what the reading or the probe shows | effect |
|---|---|---|---|
| C-1 | §14 (d): the implemented axiom is *"opposed tests against a static difficulty derived from the opponent (half the opponent's score, not an opposed roll)"* | True of two providers. Mass battle grades each side against the **other side's rolled net**: `a_deg = compute_degree(a_net, max(1, b_net))`, `b_deg = compute_degree(b_net, max(1, a_net))` (`modules/mass_battle/orchestration.py:1308-1309`, again at `:2185`). That is an opposed roll | F-DICE-15 |
| C-2 | §7: `[SKIPPED: research/provenance/ … the index places no resolution-kernel material in them]` | False as an absence claim. `SYN_GROUP_C.md:278-303` is headed *Resolution Kernel* and ranks its conflicts; `H1.md:68-86` records a Jordan ruling on pools that the first audit does not cite (below, C-5); companion part 3 `:213` names the wound's `+0.15 Ob` and its `1/√N` decay; part 5 §12.9 tabulates Valoria's resolver against four games; part 8 `:56` records that a battle reads no commander | the three leads are used in F-DICE-16, F-DICE-17, F-DICE-18 |
| C-3 | Proposal `10_DICE_advantage_sources_for_the_arcs.md` builds `wounds` as one named level **against** the actor per third of body lost, shipped `minor`, marked `[ASSUMPTION; Jordan to correct]`, decided at ladder step 4 | The form and the magnitude of a wound's penalty on a non-combat roll were ruled before the proposal was written: *wounds never impose a −1D pool cut; each wound adds a fractional Ob* (Jordan, 2026-07-08, ED-PC-0005), **+0.15 Ob per wound, cumulative** for an active roller outside combat (ED-PC-0006, resolved 2026-07-08). The ladder was entered at step 4 with step 3 unasked | F-DICE-16; §5.4 states the corrected edit |
| C-4 | Proposal `10_DICE_one_roller_one_fraction_rule.md`, falsifier: *"`grep -rn "randint(1, 10)" modules/ engine/` prints one line, in `dice_engine.roll_pool`"* | It cannot. Besides mass battle's line the grep prints three today: `engine/dice_engine/dice_engine.py:212` (the owner), `engine/dice_engine/sigma_leverage.py:303` (a docstring quoting it) and `engine/reference/contest-groundup/engine.py:66` (the parity golden's frozen oracle, which `tools/gen_sigma_parity_goldens.py` reads). After the edit it prints three | restated in §5.1: one line under `modules/`, and one *call* under `engine/dice_engine/` |
| C-5 | F-DICE-02, *the root*: the designed pools were *"an attribute doubled plus history with a floor of five (`complete_systems_reference.md:138`, `:183`)"*, and *"the game follows the code"* | `:138` is the combat pool the design itself struck (ED-901, 2026-06-04); the universal statement is `canonical_registry.md:158` and `derived_stats_v30.md` §14.4. And the code does not follow one regime: personal combat kept the designed one (`max(5, faculty + 6)`, `modules/combat/core.py:54-58`), the social roll took the bare score. One number on a sheet is three different pools (F-DICE-17). The ruling that should have prevented it exists: *"All pools are contained within one single document, which all subsystems call to get the appropriate pool"* (Jordan, Ruling C, `proposals/2026-08-23-suite-01-rulings-and-execution.md` §0) | F-DICE-17 |
| C-6 | §6.1: H-152 *"wrongly filed … `[UNVERIFIED at _eff_march's total branch]` … the MB lane verifies and closes"* | Verified and closed here (§3) | none further |
| C-7 | §14 (a) lists eight points where the subsystem takes a character capability | It omits the provider that takes none. `MassBattleInput` is byte-equal after every attacker is raised to 7 on all ten attributes and all four vocation keys (E-B04) | F-DICE-18 |
| C-8 | §14 (b), *hard-coded in a module*: the level table, combat's two pool constants, the source binding, the divisor 2 | Add: mass battle's whole pool rule (`eff_power × eff_size × POOL_QUALITY_SCALE`, a Discipline penalty of `(5 − disc) × 0.5` capped at two dice, one die at stamina 0; `core/exchange.py:101-124`, `config.py:157-158`, `:583`), and a second modifier vocabulary, `SIGMA_PER_D = 0.2` sigma per die-equivalent (`config.py:306`), beside `LEVEL_SIGMA`'s four names | F-DICE-21 |

One sentence of the first audit is confirmed by a reading it did not have: SYN_GROUP_C's first-ranked
conflict (*"the obstacle has no owner while the ladder does"*, 2026-08-28) is now false for the social
roll (`roll.py::obstacle`, ED-SC-0033 clause 3) and for combat (`core.ob_from_defender`), as the first
audit's §4 says; its prediction (*"ruling the obstacle without also owning the roller predicts the same
fork recurring"*) is what F-DICE-07 measured.

### 2.2 New findings

Numbering continues from the first audit's F-DICE-14.

#### F-DICE-15 · degrades narrative (NERS-S) · three obstacle axioms for one ruling

- **Claim.** *An obstacle against a person is their corresponding score halved plus that instance's
  modifiers* (Jordan, 2026-08-14) is executed three ways: the social roll halves the subject's held
  score and falls to a stand-in of 2.0; combat halves the defender's `faculty` (fallback and practice
  included); mass battle uses no score at all and sets each side's obstacle to the other side's dice.
- **Evidence.** `modules/social_contest/roll.py:141`; `modules/combat/core.py:124`;
  `modules/mass_battle/orchestration.py:1308-1309`.
- **Falsifier run.** E-B03, exact enumeration on the owner's face rule and ladder. Equal whole pools
  under the opposed rule: Failure / Partial / Success / Overwhelming 51.7 / 27.7 / 19.9 / 0.7 % at two
  dice, 46.0 / 20.3 / 26.9 / 6.8 at four, 44.7 / 13.2 / 23.3 / 18.8 at eight; and **both sides read
  Failure in the same exchange** 36.0 % of the time at one die, 17.6 % at two, 6.3 % at four. Under the
  static rule a side's band does not depend on the other side's luck.
- **Touches.** R-04, R-09.
- **Consequence.** The same word (*Overwhelming*, *Partial*) is reached by two different contests. An
  exchange in which both lines fail is a null exchange (`DAMAGE_BY_DEGREE["Failure"]` is 0,
  `config.py:303-304`), frequent exactly where units are small and worn, which is where a battle is
  decided. For the port, the field's obstacle is not a function of any authored quantity.
- **Disposition.** Not a defect to repair in the dice. An opposed roll is a lawful reading of *"Ob
  should be determined by your opponent more than anything"* (Jordan, 2026-08-15) for two bodies that
  both strike in one exchange. What is missing is that it is **named**: the axiom map (§4, proposal)
  carries it as its own row, `opposed_roll`, so a reader of the field's result knows which contest
  produced the band. The floor `max(1, ·)` is `OB_MIN` re-typed and should read the owner's constant
  (the roller proposal's edit C, one more line).

#### F-DICE-16 · degrades narrative · the wound's penalty was ruled, and the first proposal departs from it without saying so

- **Claim.** See C-3. The proposed `minor` level against is a different channel from the ruled one and
  about two to four times its size.
- **Evidence.** `registers/editorial_ledger_pc_archive.jsonl` ED-PC-0005, ED-PC-0006;
  `modules/combat/combatant.py:52-58` (the tracker's docstring carries the ruling live);
  `modules/combat/config.py:124` (`WOUND_ATK_OB = 0.15`, `WOUND_DEF_OB = 0.25`).
- **Falsifier run.** E-B03, Partial-or-better at Ob 2, change from the unwounded roll: the ruled
  `+0.15 Ob` costs 1.5 / 2.8 / 3.4 / 3.5 / 3.0 / 2.4 points at pools 1 / 2 / 3 / 4 / 6 / 8; one `minor`
  level against costs 2.0 / 5.3 / 7.8 / 9.2 / 9.7 / 8.8. Three ruled wounds (the cap) cost 8.6 points at
  pool 2; two `minor` levels (the proposal's cap) cost 10.4.
- **A complication the code adds, stated and not resolved.** In combat the "Ob" of ED-1041 is not added
  to an obstacle: `wound_impairment` (`combat_systems.py:1044-1050`) returns a figure every caller folds
  into `net_sigma`, so 0.15 is spent as 0.15 **sigma**, worth 0.29 to 0.42 successes at pools of six to
  twelve. The ruling's word and the code's unit differ inside the module the ruling was written for.
  That is the PC lane's to state; for the season's non-combat roll the ruling's own reading (an obstacle
  term) is the one with a ledger row.
- **Touches.** R-02; ARC-53.
- **Resolution.** Ladder step 3: a wound on a non-combat roll is an **obstacle term on the wounded
  actor's own roll**, +0.15 per wound, cumulative, capped at three wounds; it raises an obstacle and so
  breaches neither the mean-shift ruling (which forbids *lowering* one) nor `OB_MIN`. What remains an
  assumption is only how a season `body` maps to a wound count. The corrected edit is in §5.4; the first
  proposal's form is kept there as the second defensible option, because choosing it would overwrite a
  ruled channel.

#### F-DICE-17 · blocks a requirement (R-06, R-09) once content lands · one score, three pools

- **Claim.** A person's score for a verb is read once (`pool.py::faculty`) and then means three
  different amounts of dice: itself in a social roll, itself plus six with a floor of five in a fight,
  and nothing on a field. The pool *reader* is single-owned; the pool *rule* is not, and Ruling C asked
  for the rule.
- **Evidence.** `pool.py:94-100`; `modules/combat/core.py:51-58`; `core/exchange.py:124`.
- **Falsifier run.** E-B03. Equal scores `s` against `s`, each resolver's own pool and obstacle,
  F / P / S / O in %:

  | s | social as built (pool s, Ob s/2) | social as designed (pool max(5, 2s+3), Ob floor(s/2)+1) | combat as built (pool max(5, s+6), Ob s/2, Normal) |
  |---|---|---|---|
  | 2 | 42.0 / 32.0 / 25.0 / 1.0 | 27.4 / 17.9 / 33.9 / 20.8 | 16.5 / 13.2 / 34.0 / 36.2 |
  | 3 | 45.9 / 25.5 / 25.5 / 3.1 | 19.1 / 13.8 / 32.4 / 34.8 | 19.1 / 13.3 / 32.3 / 35.4 |
  | 4 | 48.8 / 23.2 / 24.1 / 3.8 | 23.9 / 13.4 / 29.3 / 33.4 | 21.5 / 13.2 / 30.7 / 34.6 |
  | 7 | 54.5 / 17.0 / 21.3 / 7.3 | 15.8 / 8.7 / 22.4 / 53.1 | 27.8 / 12.6 / 27.0 / 32.6 |

  Combat as built reproduces the designed social roll to within a point at a score of 3 and within
  three at 4. The season's social roll is a different game: between equals, Success-or-better is 28 %
  where the other two give 63 to 68 %. What one point buys (Success-or-better): an actor going from 3 to
  4 against a 3 gains 11.0 points in the social roll and 4.6 in a fight; a subject going from 3 to 4
  costs the actor 11.4 and 7.8.
- **Touches.** R-06, R-09; NERS-S (*calculations consistent in methodology*; two ladders for one
  quantity is the definition's own example).
- **Consequence.** With today's content nobody holds a score, so nothing is seen. The day `stats:` are
  authored, the same Presence 4 makes a middling debater and the same Coordination 4 a confident
  fighter, and a designer tuning one cannot predict the other. A character sheet that shows one number
  per capability cannot tell the player what it is worth.
- **The steelman, and what survives.** Combat's regime is not an accident: ED-901 chose a pool of six
  to twelve dice so that the Normal sampler is well-behaved and attributes act through sigma, not
  through the pool; the first audit's F-DICE-02 shows what a two-die pool does. What does not survive
  is that the *choice of regime* is a constant in each module. **Resolution** (ladder step 3, Ruling C):
  the pool rule is one row per resolver in the one authoring surface (proposal §C, `pool_rule`), read
  by the one pool reader; the social row ships as it is (`base: score, add: 0, floor: 1`), combat's row
  carries its 6 and 5, and whether the social roll should move to the designed regime is listed for
  Jordan (§5.6), since it changes every non-combat band in the game.

#### F-DICE-18 · blocks a design intent · a field battle reads no person

- **Claim.** No capability of any person reaches a field: not the commander's, not a soldier's.
- **Evidence.** `seam/wrappers/mass_battle.py:252-281` reads each member's `weight` and the sides'
  stances and loyalties; `_order_of_battle` (`:192-215`) reads the commander only to locate the army.
  `core/exchange.py:57-65` (`derive_command(charisma, cognition)`) is live code with no input: the pool
  is the troop type's, *"no Command anywhere"* (`:103-124`; Jordan directive 2026-07-08).
- **Falsifier run.** E-B04: `MassBattleInput` equal (every field but the geography table compared)
  before and after the whole attacking side is set to 7 on ten attributes and four keys. The same edit
  moves `PersonalCombatInput.faculties` from `(2, 2)` to `(7, 2)` and `ends` from `(4, 4)` to `(7, 4)`,
  and `SocialContestInput.pool` from 2 to 7.
- **A returning finding.** Companion part 8 `:56` recorded it of the deleted campaign driver (*"a
  commander … `derive_command` falls back to the hardcoded `command = 4`"*). The driver is gone; the
  season's field has the same shape.
- **Touches.** R-04, R-06; the stated intent that a match is resolved *"from those settings and the
  individuals' attributes"* and that a commander's *"own fighting and leadership matter"* (brief).
- **The conflict, named.** The directive of 2026-07-08 removed Command from the **pool**. The intent of
  2026-11-12 asks that leadership matter. They do not collide if leadership enters by the other door:
  as named levels on his side's exchanges (a mean shift), never as dice. The map carries that as a row
  (`edge`, site `field`); building it is the MB lane's.

#### F-DICE-19 · hygiene, latent, a returning finding half closed · below one die the sigma boost is a full die's

- **Claim.** A mass-battle pool under one die deals a die with probability equal to the pool, and takes
  a sigma boost sized for one whole die, so advantage alone can clear the bar with no die dealt.
- **Evidence.** `orchestration.py:1271-1272` passes `math.floor(pool)`; `resolution.py:230` then takes
  `sqrt(max(1, pool))`. The 2026-07-22 audit (`fable_logic_audit_v1.md:43-45`) named both halves
  (*"over-stated ~38% just below each integer; sub-1 pools get a full one-die σ-conversion"*) and
  offered *"`floor(pool)` (or a smooth sub-1 ramp)"*; the fix took the first option, which closes the
  first half only.
- **Falsifier run.** E-B03 and E-B05, at the function, not in a battle: at pool 0.4 the dice average
  0.16 successes; `_sigma_net_boost(+1σ, floor(0.4))` is 0.699 and at +2σ it is 1.044, which
  `compute_degree(1.044, max(1, b_net))` reads **Partial** (one casualty step) for any opposing net of
  1 or less, on every exchange, whatever the dice. `[UNVERIFIED: that a +2σ sum is reached by a
  sub-one-die body in a shipped battle; the sources (charge, stance, terrain, morale) can sum that high
  on paper.]`
- **Minimal fix.** In §5.1: one rule for the sub-one-die regime in the shared roller, the boost applied
  with the die.

#### F-DICE-20 · degrades narrative · derived resources exist for one scene of one subsystem, and the one stored resource runs backwards

- **Claim.** The design's second axiom after the pool (*a stat is what a character can do; a derived
  value is what he has now*: `derived_stats_v30.md` §1, §14.1) is implemented inside the combat module
  only, as per-scene working state, and the season's one stored resource feeds the attribute instead of
  being sized by it.
- **Evidence.** `modules/combat/combatant.py:28-29`, `:47-49`, `:172-183` (stamina `3·End + 2·Spirit`,
  concentration `3·Focus + 2·Spirit`, the wound tracker from Endurance, Spirit and Strength), rebuilt
  for every fight (`:60-63`). The season stores `Person.body` on `condition_scale` (1000 for everyone,
  `state/carriers.py:761`), and `party_end` (`seam/wrappers/combat.py:143-152`) lowers the fighter's
  Endurance by one point per body band: the resource degrades the stat for the next scene, where the
  design has the stat set the resource's size. Composure, Concentration outside a fight, and Thread
  Fatigue have no carrier in the season.
- **Touches.** R-02 (a scene's cost reaching the next scene), R-06.
- **Consequence.** A hardy character and a frail one enter the season with the same body; exhaustion
  and strain from one scene (SCN-03, SCN-04, SCN-07 in §13 of the first audit) have nowhere to persist
  except `body`. Jordan's later words keep the axiom and change the formula (AR-11, AR-20, AR-56 to
  AR-58: Strength and Endurance both size health, form *"to be resolved later"*).
- **Resolution.** The map carries `resource` as an axiom with its one implemented instance and the
  field a second would need (proposal §C); no formula is proposed, because the form is explicitly
  Jordan's and unresolved (AR-58).

#### F-DICE-21 · hygiene (NERS-S) · the field speaks sigma in die-equivalents and tires twice

- **Claim.** Mass battle's modifiers are mean shifts (lawful) but authored in a private unit, and
  fatigue reaches one roll by two channels.
- **Evidence.** `config.py:306` (`SIGMA_PER_D = 0.2`); `orchestration.py:1225-1260` (encirclement,
  stance and terrain as dice × 0.2; morale to −0.8σ, fatigue to −1.5σ, charge shock to −0.55σ, a ranged
  body in melee −1.0σ as bare sigma). Fatigue: `core/exchange.py:34-41` and `config.py:157-158` (one die
  off the pool at stamina 0) **and** `percell.py:267-282` (`_fatigue_sigma`).
- **Falsifier run.** E-B05: `_sigma_net_boost` equals `net_boost` to the last bit on 81 sigma values by
  eight pools, so the *function* is one; the *vocabulary* is not (a die-equivalent is 0.2σ, a `minor`
  level 0.25σ).
- **Disposition.** Continuous state (morale, stamina) is rightly continuous sigma and stays. What a
  designer authors by name (a stance, a terrain, a trait) should use the four level names. One line in
  §5.2; the MB lane's edit.

#### F-DICE-22 · hygiene · two of the tests the first audit left unread are prose guards

- `tests/valoria/test_knot_pool_formula.py` opens three files under `.designs/` and asserts that each
  still contains `(Spirit × 2) + History(Relevant) + 3`. The documents are quarantined (*"Do not edit
  it"*), the formula's History term was eliminated as a roll input on 2026-11-04 (ED-IN-0330), the
  attribute its third test pins (Bonds) is retired from the ten (`descriptor_registry.yaml:265`), and
  its own docstring says *"There is no sim/ oracle that computes the Knot Pool"*. It guards archived
  prose against being edited toward the current rulings. By `CLAUDE.md` §0.1 pt 5 its subject is
  load-bearing on nothing: **delete the file.**
- `tests/valoria/test_fractional_pool.py:23-26`: `test_default_gated_off` asserts the default is
  **on**; its module docstring says the fractional die preserves *"the net<=0 Failure boundary"*, which
  the ruled ladder replaced with `margin < 0`. Rename and reword; when the roller proposal lands the
  file's subject is the owner's function.
- The design's calibration line is not reproducible. `canonical_registry.md:183`: *"5D pool at Ob 1
  succeeds ~92%. At Ob 2: ~70%. At Ob 3: ~45%. At Ob 4: ~25%. 10D at Ob 3: ~73%"*. Exact, on the
  owner's faces, `P(net ≥ Ob)`: 79.8, 60.0, 38.0, 19.8 and 72.0 (E-B03). The ten-die figure is right
  and the five-die figures are 5 to 12 points high. Reference only; it matters because the case corpus
  and the companion quote pools in that regime as if calibrated.

## 3. H-152 closed

**The row** (`engine/season/hole_register.yaml:3439`): a `total`-casualty-model march loss removes a
person with no `person.died` Event. Its own falsifier, *"TO BE WRITTEN"*: sweep
`field_casualty_model = "total"`, fold a real march to `Lost`, and show that no `person.died` Event names
the removed person.

**The code, read.** `loop/effects_combat.py::_eff_march` (`:451-680`). At `:618` `dies = model == "total"`;
at `:668-672` each loser is named to the gate as `death_subjects(w, pid, loser_earns, fields=fields)` when
`dies`, else as a plain `Subject.entity`; at `:676-679` the same for a winner the arm kills (CR-24).
`state/gate.py::death_subjects` (`:1819-1832`) names the dying person earning the band's kinds plus
`person.died`, and each seat he holds earning `tenure.closed`. `verb_table.yaml:1077`'s `emits_note`
records that `march`'s `Won` and `Lost` bands declare both kinds since CP-T02-01 / HR-1 and cites this
row. The row's `owner:` (*"no owner exists yet"*) and its closing sentence (*"THE MISSING `person.died`
EVENT THIS ROW NAMES IS UNCHANGED AND STILL OPEN"*, dated 2026-09-29) predate that build and were not
updated by it.

**The probe that decides it** (E-B01; `probe_h152.py`, seed 0, the realm at build). A real `march`
(`p_npc_033` through `off_spymaster`, Crown, two mustered, on `set_s_036`, Church of Solmund, six
mustered), folded by the real driver at RESOLVE and then ENCOUNTER, so the resolution is the mass-battle
provider's and not a hand-built one (the existing test,
`engine/season/tests/test_cp_t02_01_death_names_seats.py:238`, constructs its `Resolution`).

| arm | Event kinds emitted | removed from `w.persons` | named by a `person.died` Event |
|---|---|---|---|
| `total` | `march.declared`, `field.lost`, `person.died`, `tenure.closed` | 8 | the same 8 |
| `scaled_by_degree` (shipped; control) | `march.declared`, `field.lost` | 0 | 0 |
| `total`, with `death_subjects` replaced by a version that does not add `person.died` (mutation) | `march.declared`, `field.lost` | 8 | 0 |

The mutation arm reproduces the row's defect exactly (eight people gone, nothing in the log), so the
probe can observe the failure it excludes; the unmutated arm does not show it. **H-152 is closed** (by
CP-T02-01, the B10-09 build). Action, a register edit for whoever closes this suite: the row's head
to CLOSED citing CP-T02-01 and this probe; `owner:` to `state/gate.py::death_subjects`. It never was a
dice-engine row; the dossier filed it here by a path rule on `effects.py`.

**A by-product, for the MB lane (not a dice finding).** Under `total` the same field removed all eight
people: the two losing attackers and the six winning defenders, because CR-24's rule (*"under `total`
only a winner who took a casualty dies"*, `:585-588`) reads the winning side's survivor ratio, and a
winning side that lost anyone has a ratio below 1 for every member. `_eff_march`'s docstring gives the
reason for the rule as avoiding the case that *"would annihilate both sides"* (`:466`); at the one
fixture measured, both sides are annihilated anyway. `total` is a control arm and not shipped, so this
costs nothing in play; it means the control re-runs *"fighting costs everyone everything"* where its
note says *"losing costs everything"*. Cross-listed, not adjudicated.

## 4. Capability → axiom → resolver input

The exact interface (field names, units, the reader of each, the authoring tables) is the proposal
`../proposals/10_DICE_capability_axiom_map.md`. This section is the audit behind it: what the design
intends, what the code does, and where they part. Design documents are cited for intent only.

### 4.1 The axioms the design intends, in three strata

The tree holds three statements of what a capability is and does, each later one overruling the earlier
where they meet.

**Stratum 1, the design set (April to July 2026; archived).** `canonical_registry.md` §4 and
`derived_stats_v30.md`:

| axiom, in the tradition's words | the design's statement | source |
|---|---|---|
| ten attributes, rated 1 to 7 | three physical, three mental, three social, one metaphysical; 31 points at creation, one at 5 and the rest at most 4 | `canonical_registry.md:146-150` |
| skill as bonus dice on an attribute | a History at level 1 to 3 adds that many dice, capped by Recall | `:152-154` |
| attribute doubled, plus skill, plus a base, gives the pool | `(Primary × 2) + History + 3`, minimum five dice | `:158`; `derived_stats_v30.md` §14.4 |
| a static obstacle from the opponent's attribute | `Ob = floor(Attribute / 2) + 1` | `canonical_registry.md:164` |
| the attribute is capacity, a derived resource is state | `derived = attribute × multiplier`; Health, Stamina, Composure, Concentration, Thread Fatigue; equipment changes drain and recovery, never the pool | `derived_stats_v30.md` §1, §3, §14.1 |
| a condition costs dice, a circumstance moves the obstacle | *"Ob channel reserved for circumstance, dice channel for condition"* (Rattled −1D; out of breath −2D) | `derived_stats_v30.md` §5.1 (ED-939) |
| a modifier is a whole die or a whole obstacle step | `+1D` and `−1 Ob` throughout the eleven cross-cutting documents; a disposition lowers the obstacle | §1 above |
| degrees by margin, a resource spent to shift a roll | four bands; Inspiration: +1D, or spent for Ob −1 | `derived_stats_v30.md` §5.3 |
| scale changes what a stat is worth | a faction rolls its bare stat (1 to 7 dice); a person rolls 5 to 17 | `derived_stats_v30.md` §14.5 |

**Stratum 2, the resolver rulings (May to September 2026).** TN 7 always (ED-IN-0196). One ladder on the
margin, four bands, for every scale (2026-08-14, 2026-08-15). Advantage is a shift of the mean in sigma,
never a lowered obstacle (ED-884, ED-934). An obstacle against a person is his corresponding score halved
plus that instance's modifiers (2026-08-14); no base obstacle by scale (2026-09-05). A wound is a
fraction of an obstacle, never a die (ED-PC-0005, ED-PC-0006), which overrules the condition-costs-dice
axiom for wounds. Combat's pool is skill plus six, minimum five, with attributes acting through sigma
(ED-901). All pools in one document every subsystem calls (Ruling C, 2026-08-23). Capability supplies
dice and gates nothing (`rosters.yaml:1499-1502`).

**Stratum 3, the attribute rulings (November 2026).** The ten are renamed and re-cut (ED-IN-0328:
Strength, Coordination, Endurance, Reason, Focus, Perception, Attunement, Presence, Grace, Spirit).
Histories are eliminated as a roll input; in their place are *"bundles of skills/aptitudes that are
learned abilities that complement character attributes"* (ED-IN-0330), and *"martial traditions are also
bundles of skills"* (AR-43a). A skill is *"a constant at the time when used by subsystem … just like any
other skills or whatever else informs state"* (AR-47, AR-48): grown outside a scene, fixed inside it.
An attribute's floor is 1 (AR-05). Attributes and capabilities weigh a character's **choice** as well as
his roll (AR-04). Spirit *"in different contexts you can see … as ignoring obstacle modifiers or adding
modifiers to dice pool"* (AR-44): one capability, two channels, by context. Different venues *"may
prioritize grace"*, and a parliament *"would penalize someone who lacks sufficient grace"* (AR-36, AR-36a):
a capability as a circumstance of the place. Strength prices the wearing and wielding of a kit (AR-10,
AR-12). Health's form is unresolved (AR-58).

What survives all three strata, and is therefore the intended axiom set: **(i)** a rated attribute and a
learned skill jointly give dice; **(ii)** the opponent's rating sets a static difficulty; **(iii)**
advantage and disadvantage are a bounded shift, in named steps; **(iv)** the situation moves the
difficulty; **(v)** an attribute sizes a resource that drains; **(vi)** an attribute sets what a kit
costs to bear; **(vii)** capability weighs choices; **(viii)** capability grows by training and by use
between scenes; **(ix)** capability never forbids an attempt (one named exception, Thread Sensitivity).

### 4.2 The axioms the code implements, per resolver

| axiom | social roll (`modules/social_contest/roll.py`) | personal combat (`modules/combat/`) | field (`modules/mass_battle/`) |
|---|---|---|---|
| (i) dice | `max(attribute, key)`, else `pool_default`; plus practice (`pool.py:94-100`) | the same read, then `max(5, faculty + 6)` (`core.py:54-58`) | none from a person; `power × size × 0.8`, less Discipline and stamina dice (`exchange.py:101-124`) |
| (ii) difficulty from the opponent | held score / 2, else a stand-in of 2.0; ceiling solved per pool (`roll.py:141-154`) | `faculty / 2`, fallback and practice included (`core.py:124`) | the opponent's own rolled net, floored at 1 (`orchestration.py:1308-1309`) |
| (iii) advantage in steps | named levels through one roster; one member, unsigned (`sigma.py:140-167`) | bare sigma terms summed inside the module (attributes, wounds, kit, tradition), soft-capped | bare sigma and die-equivalents at 0.2σ, soft-capped (`orchestration.py:1225-1260`) |
| (iv) situation moves difficulty | room terms and forgery quality, three named fields (`roll.py:142-144`) | none on the obstacle (wounds go to sigma) | none on the obstacle; terrain and walls go to sigma and to damage |
| (v) attribute sizes a resource | none | stamina, concentration, health, per scene (`combatant.py:172-183`) | per-column stamina from a constant 100, not from an attribute (`config.py:154`) |
| (vi) kit cost | none | Strength demand of the wielded weapon and worn harness, paid in stamina and handling (`combat_systems.py:168-189`) | none (the loadout has one reader, reach; `04_MB_unit_loadout…` confirms by run) |
| (vii) weighs a choice | believed odds multiply the term (`choose.py::odds_weight`) | none believed; true shares are sampled for a display no loop caller reaches (`fight_estimate`, `sigma.py:379-384`) | none believed; the same (`field_estimate`, `sigma.py:386-391`; first audit F-DICE-14) |
| (viii) growth | `train` +1 on a held key; practice from the act log | a fight that drew blood raises `arms` on survivors (`rosters.yaml:1531`) | none |
| (ix) never forbids | S27.4 refuses only the impossible (`ob > 2 × pool`) | none | none |
| sampler | whole dice, exact odds | Normal, half a success harder (first audit F-DICE-05) | whole dice, own roller, stochastic fractional die |

Reading across a row is the finding: no two resolvers execute (i), (ii) or (iii) the same way
(F-DICE-15, F-DICE-17, F-DICE-21), and (v) and (vi) exist in one resolver only. Reading down a column,
the field takes nothing from a person on any row (F-DICE-18), and combat is the one resolver in which a
character's whole sheet matters and the one whose design is unratified (ED-IN-0351).

### 4.3 Where the design and the code part, and which the game follows

| subject | design (stratum) | code | the game follows | cost of the difference |
|---|---|---|---|---|
| the pool, outside combat | attribute doubled + skill + 3, floor 5 (1); never re-ruled for the social roll | the score itself, floor 1 | code (B10-08 and B10-10, ratified on merge) | F-DICE-17; the first audit's F-DICE-02 |
| a skill | bonus dice on top of an attribute (1); a bundle that complements attributes (3) | the larger of the two, so a skill at or below its attribute adds nothing | code | a learned skill is invisible until it passes the attribute; *complement* is not yet a rule anyone wrote |
| the opposed obstacle | `floor(attr/2) + 1` (1); `score/2 + modifiers` (2) | `score/2`, unfloored, no `+1` | stratum 2 and code agree | none; the `+1` of stratum 1 is superseded |
| a wound | −1D (1); a fraction of an obstacle (2) | sigma in combat; nothing outside it | code in combat; nothing elsewhere | F-DICE-16 |
| a condition (strain, fatigue, rattled) | dice (1) | sigma and stamina in combat; one die **and** sigma on a field; nothing in the social roll | code | no carrier for strain in the season (first audit §13, SCN-04, SCN-07) |
| a modifier's unit | a die or an obstacle step (1); a named sigma level (2) | named levels in one roster; bare sigma in two modules | stratum 2 | every `+1D` in the case corpus and the design set must be restated as a level, an addend or an obstacle term (first audit, resolution 19) |
| the derived resources | five, sized by attributes (1, 3) | three, in one module, per scene | code | F-DICE-20 |
| scale changes a stat's worth | intended (1) | unintended: by subsystem, not by scale | code | F-DICE-17 |

### 4.4 The single authoring surface

Decided in the proposal; summarised here so the audit can be read alone. The existing owner is
`engine/season/rosters.yaml`: `verb_capability` (verb → capability), `vocation_attribute` (capability →
attribute, and what opposes it), `advantage_sources`, `lifepath_templates`; with
`references/descriptor_registry.yaml: attributes` for the ten and `references/npc_registry.yaml` for who
holds what. It is extended by three things and nothing is added beside it:

1. a **definition row** per capability (kind, base attribute, opposition, scale, untrained rule, growth),
   which `vocation_attribute` becomes;
2. a closed roster of **roles**, one per axiom of §4.1, each naming the one resolver input it feeds, its
   unit and its one reader;
3. one **uses table** (`capability_uses`, the CHAR lane's, with a `role` column) in which every place a
   capability changes an outcome is a row, the roll's and the choice's alike.

Five other lanes proposed pieces of this. The proposal's §F reconciles them row for row; the one
difference left for the holistic stage is which file holds the definition rows (this file, as the work
order directs, or `descriptor_registry.yaml` as `01_CORE_capability_authoring_surface.md` proposes; the
row is the same in both).

## 5. The shared roller, and what it meets

The first audit's `10_DICE_one_roller_one_fraction_rule.md` stands. Four things it meets were outside its
reading.

### 5.1 Mass battle's resolver

1. **The falsifier, restated (C-4).** After the edit: `grep -rn "randint(1, 10)" modules/` prints
   nothing, and under `engine/dice_engine/` the one *call* is `dice_engine.py:212`. The oracle under
   `engine/reference/` is frozen and is not a roller the game reaches.
2. **The opposed roll stays** (F-DICE-15) and is named. Its floor becomes
   `max(sigma_leverage.OB_MIN, b_net)`; the literal `1` is the owner's constant typed twice
   (`orchestration.py:1308-1309`, `:2185`).
3. **Below one die there must be one rule, and the first proposal keeps two.** It leaves mass battle's
   sub-one-die floor in `roll_pool_fractional` as *"mass battle's own"* while the owner floors at one
   die. Decided here, ladder step 4 (the fraction of a margin, and the fraction of a die above one, are
   both paid in probability): **the roller deals what it is handed.** `roll_net(pool)` deals
   `floor(pool)` dice and one more with probability equal to the fraction, for any `pool ≥ 0`; the
   floor of one die moves to where it is a statement about a *person* (`pool.py::faculty` returns at
   least 1, the proposal's `pool_rules.floor`), which is what the *minimum pool* axiom means. A unit's
   pool is an aggregate of troops and may fall below a die. E-B03 shows what the present split costs: at
   a pool of 0.25 the owner's roller averages 0.400 successes and mass battle's 0.100.
4. **The boost follows the die (F-DICE-19).** With the same rule in the owner: for a pool under one
   die, `net_boost` is applied on the draws in which the die is dealt, and not otherwise. Expected
   boost is then proportional to the pool, a sliver with every advantage still fails when it rolls
   nothing, and the band edge the 2026-07-24 fix protected stays protected. At or above one die nothing
   changes (`sqrt(max(1, floor(pool)))` as today). This is a mover for mass-battle goldens that contain
   a sub-one-die exchange with nonzero sigma; the gate reports the count of such exchanges in the
   golden batteries before the edit, and zero is a legitimate reading.
5. **One vocabulary for what is authored (F-DICE-21).** State that is continuous (morale, stamina)
   stays continuous sigma. The four authored quantities converted at `SIGMA_PER_D` (stance commitment,
   encirclement, terrain dice, charge recoil) are named levels in the owner's table when the troop and
   order tables become data (`04_MB_unit_loadout_and_weapon_in_hand.md` §2); until then the constant
   stays and is exported. Fatigue's second channel, the die at stamina 0, is the condition-costs-dice
   form the wound ruling retired for wounds; whether it goes is the MB lane's balance call, recorded,
   not decided.
6. **Order against the GO lane's draw owner.** `11_GO_one_draw_owner.md` replaces `randint` with an
   owned function of one uniform at nine sites and re-pins every golden that reaches a d10. Two of the
   nine are the two d10 rollers. Land the one-roller edit first (stream-equal, no re-pin), then GO's:
   one site changes instead of two and the goldens move once.

### 5.2 The duel round

`03_PC_duel_round_and_approach.md` makes a fight a loop over `fight.round`, each round on a private
stream derived from the fight's, with an approach chosen per phase. From the dice side:

- **One path, so the duality holds by construction.** The round a player plays and the round the grid
  resolves for him draw from the same sampler (`roll_net_continuous`), so the half-success offset of
  the first audit's F-DICE-05 cannot separate the two modes of a fight. It still separates a fight from
  a debate; that is unchanged.
- **An approach is an edge, not a pool rule.** Aggressive, normal and defensive must reach the roll as
  sigma for the attack and against the defence through the terms the module already sums (the
  commitment and defence-mode terms), with the three approaches as rows naming levels. An approach
  that adds dice or moves `ob_from_defender` would be a fourth pool regime (F-DICE-17).
- **The believed estimate takes the approach as an operand.** The first audit's interface for a
  fight's believed chance (`believed_estimate`, shares over the provider's own bands) was stated for a
  whole fight. With rounds, what a person weighs is a round at an approach: the role's signature gains
  the approach, and the shares are over the round's endings. Stated for the PC lane; nothing is built
  here.
- **The round's stream** (`random.Random(rng.getrandbits(64))`) is a tenth construction site for GO's
  one constructor. Cross-listed to GO.
- **Wounds inside a round** stay the module's (`wound_impairment`); the season-side wound term of §5.4
  is applied by the host to non-combat rolls only, so nothing is counted twice.

### 5.3 The weapon-carry cost: one rule, and where it lives

The PC and MB lanes have decided it, and this lane concurs: **the rule is one leaf function,
`carry_demand(weapons, armour)`, in Strength points, beside `engine/substrate/combat_kit.py`, reading
the combat module's typed export and nothing else** (`03_PC_loadout_and_carry.md` §2;
`04_MB_unit_loadout_and_weapon_in_hand.md` §3). A person's fight charges it in `act_cost`; a unit's
host evaluates the same function over the troop row's loadout and hands the module factors. What the
resolution lane adds:

- **It is the `threshold` role of the map, and it must stay off the dice.** The shortfall
  `max(0, carry_demand − strength)` is paid in the currencies each resolver already has for effort:
  stamina per action and a slower close for a person, stamina drain, slower recovery and a shorter step
  for a unit. It never changes a pool, an obstacle or a level directly; it reaches the roll only
  through fatigue's existing channel (a tired fighter's sigma, a tired column's `_fatigue_sigma`). That
  is what makes it one rule at two scales: the same Strength points, the same shortfall, and each
  resolver's own conversion of tiredness into odds.
- **Strength is read from the one surface.** A person's is `Person.attributes["attr.body.strength"]`
  (the combat spec's default where unauthored); a troop type's is the `strength` cell of the troop
  table. Both are the same registry key, so the map's row is one row with two holders.
- **One weapon roster.** `carry_demand` can only be one rule if a pike is one record. The MB proposal's
  merge onto `modules/combat/weapons.py::WEAPONS` is the precondition; `rosters.yaml: arms_kinds`
  already names a person's arms by that roster's keys.
- **The switch draws nothing.** Changing the weapon in hand costs tempo (a person) or a tick (a unit)
  and takes no draw, so it moves no stream.

### 5.4 The wound term, corrected (replaces edits B to D of the first audit's advantage proposal)

The signed channel (that proposal's edit A) stands. `wounds` is not a member of `advantage_sources`.
It is the first member of a second, parallel door for the situation, which the map needs in any case
(§4.1 (iv)):

- `engine/season/rosters.yaml`: a closed, ordered roster `obstacle_terms`, shipped `[wounds]`, on
  `advantage_sources`' pattern (a member with no binding function, or a function with no member, is
  refused at import).
- `seam/wrappers/sigma.py`: `OBSTACLE_TERMS = {"wounds": _wound_term}`, each
  `fn(fixtures, operands) -> float` in successes, signed, positive is harder. `contest_input` and
  `believed_input` sum them into one new field, `SocialContestInput.obstacle_terms: float = 0.0`.
- `modules/social_contest/roll.py::obstacle`: adds `inp.obstacle_terms` where it adds
  `forgery_quality`, before the ceiling. A favourable sum is clipped at `OB_MIN` as the room is.
- `_wound_term`: `wound_ob × min(wound_cap, wounds_of(body, body_ceiling))`. Fixtures: `wound_ob`
  (shipped **0.15**, *ruled*, ED-PC-0006; `None` is the control and today's bytes), `wound_cap` (3),
  and `wound_band` (the share of `body_ceiling` one wound is: a quarter, so three wounds stand between
  a person and felling, the design's Endurance-4 table). The last two are
  `[ASSUMPTION; medium; Jordan to correct]` with hole-register rows and three-point sweeps; the first
  is not.
- Gate and falsifier as in the first proposal, with the figures of E-B03 (2.8 points of
  Partial-or-better per wound at pool 2, Ob 2) in place of the level's.

### 5.5 Order of landing

1. The first audit's steps 1 and 2 (exported faces, edges, levels; context validated). No hash moves.
2. One roller, with §5.1's items 1 to 4. Stream-equal except sub-one-die exchanges with sigma.
3. GO's draw owner. One re-pin.
4. The map's part one (`10_DICE_capability_axiom_map.md`). Hash equal.
5. One score, two roles (first audit) and the signed channel; then §5.4's wound term.
6. The carry rule (PC, then MB), after the one weapon roster.
7. Content (`stats:`, capability rows, troop rows): CHAR, PC, MB.

### 5.6 For Jordan: two items, each already his

Neither is new; each is a measurement added to a question the ledger already holds.

- **The wound's channel.** Option A, as ruled (ED-PC-0005, ED-PC-0006): a fraction of an obstacle,
  0.15 per wound. As a game: a wound is a small, flat cost whose bite is largest on a middling roll and
  fades on a large pool (2.4 points at eight dice). Option B, as the first audit proposed and as combat
  itself spends it: a level against, in sigma. As a game: a wound costs the same share of a roll's
  spread at every pool (5 to 10 points), so it matters to experts as much as to novices, and it stacks
  under the soft cap with every other disadvantage. §5.4 is written for A.
- **What a score is worth outside a fight** (open under ED-IN-0351, which withdrew combat's
  ratification and reopened the question *"for combat and the social contest"*). Option A, as built:
  the score is the pool. Equals succeed 28 % of the time; one point is worth eleven. Option B, the
  regime combat kept: the score plus a base, floor five. Equals succeed about 65 %; one point is worth
  about five; the Normal approximation and the level table behave as designed; every non-combat band
  in the game moves. The map makes this one row (`pool_rules`), so the choice is an edit, not a build.

## 6. Evidence log

`PYTHONHASHSEED=0`, `PYTHONPATH` the repository root, `PYTHONDONTWRITEBYTECODE=1`. Scratchpad:
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/DICE_B/`.

| id | command or probe | seed · scope | outcome |
|---|---|---|---|
| E-B01 | `probe_h152.py`: a real `march` folded at RESOLVE then ENCOUNTER under `field_casualty_model` `total`, `scaled_by_degree`, and `total` with `death_subjects` mutated | 0 · the realm at build | `total`: 8 removed, 8 named by `person.died`; control: 0 and 0; mutation: 8 removed, 0 named (`h152.txt`) |
| E-B02 | ledger rows and rulings opened by hand (§1); greps: `randint(1, 10)` under `modules/` and `engine/`; `WOUND_ATK_OB`; `MB_FRACTIONAL_POOL`; readers of mass battle's equipment registry | — | four `randint` lines; fractional pool default on; the rows as quoted |
| E-B03 | `probe_axioms.py`: equal-skill bands under each resolver's own rule (exact enumeration over `_die_result` and `degree_from_net`; closed-form Normal for combat); the opposed roll; what one point buys; the design's calibration line; the wound as an obstacle term against a level; mass battle's roller against the owner's below one die | 11 · n 200,000 for the two sampled rows; the rest exact | §2.2 tables (`axioms.txt`) |
| E-B04 | `probe_inputs.py`: the three host input builders before and after a side is raised to 7 on ten attributes and four keys | 0 · build | `MassBattleInput` equal; combat `faculties` (2, 2) → (7, 2), `ends` (4, 4) → (7, 4); social `pool` 2 → 7, `opposition` `None` → 7.0 on the subject's side (`inputs.txt`) |
| E-B05 | inline: `_sigma_net_boost(s, floor(0.4))` for s in 1, 1.5, 2, 3 and `compute_degree` against a floor of 1 | — | 0.699, 0.914, 1.044, 1.157; Partial from +2σ with no die |
| E-B06 | `git status --short` at the end | — | this file and `proposals/10_DICE_capability_axiom_map.md` are this lane's only changes |

Not run: `pytest`; `aperture`; any battle long enough to observe F-DICE-19 in play (marked
`[UNVERIFIED]` there). The first audit's probes were not re-run; its figures are quoted as it gave them.
