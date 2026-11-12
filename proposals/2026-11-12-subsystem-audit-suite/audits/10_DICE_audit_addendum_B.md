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
