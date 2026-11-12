# U5b · PC — the rulings that land inside the fight: the nesting cap, two inputs, the carried wound, the damage scale, the opener's edge, and the one landing order

Folded: 2026-11-12, lane 29 (`audits/29_ONE_OPPOSED_RULE.md`; `proposals/29_DICE_one_opposed_rule_form_and_tuning.md`), on Jordan's A-71, which supersedes the default this file took (J-U5b-01) — §2 edit 4 is replaced: the fight's obstacle is `opposed_ob(the defender's skill score, opposition_rate)` at the **one** rate the argument uses (`MU_PER_DIE`); `fight_opposition_rate` is not created. Gate (2) of §2 holds at the control rate (0.5) only; at the live rate the mirror is read by that proposal's gates 2 to 5 (4.27 turns, 4.50 blows, a lead change in 45.2%, 0.1% undecided at the 1.07 seed; mirrors flat from rank 0 to 12, where the half-score runs 4.33 to 5.88 turns and 0.5 to 4.1% undecided). §5 row 5 gains a first step: the rate flips before §4's sweep, so the scale is swept on the obstacle it ships with. §4's gate figures (blows above 3.2, undecided under 2%) stand and are met. Everything else stands.

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — rows applied: `U1_OWNERS_AND_VOCABULARY.md` D-U1-11b and §2's nested-duel row (`nested_entry` is kept and given a home; at the cap it returns the typed depth-cap refusal, not `dict(status="NESTING-CAP")`; at the tree that refusal is `seam/contest.py::ContestError("max_depth reached", depth, max_depth)` (`:28-36`, returned at `:238`), which `04` §C.5 calls `Refusal(depth_cap)`; `R1_READ.md` 7b-12's Option A, deleting `nested_entry` for a partial of `seam.contest`, is **not** applied: the U1 decision wins), D-U1-08 (§2: `faculties` → `scores` + `addends`; the pool is `sigma_leverage.pool_of`), U1 §4 P-02 (§4: `DMG_SCALE` is decided at 1.07, A-79 accepting lane 29, not a sweep result), `U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §3 item 7 and U1 §4 C-07 (§2 edit 5: the `applied_by: module` column becomes the `fight` site's `reader:` cell), D-U1-11a (§5 row 1: `prevailed`); `R1_READ.md` §1.1 and §2 row A-30 (§1 edit 4's sequential window stream becomes a keyed draw), §1.1 (§6: `expected_by` takes a `PersonInterior` and no query handle); `U3_CONFLICT_LEDGER.md` C3-N3 (§2 edit 4's 5.3% explained), C3-D4 (§5's rows mapped to U3 batches); test 9 (named tests per section, tier). The Layer 1 text drafted in §1 edit 5 is corrected to the typed refusal and stays owed, not applied. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "fought scene" → "fight" (glossary *scene*); "typed record" → "dataclass" (glossary *record*); "faculty" → "score" (glossary *faculty*, retired); "the riposte" (`18_DETERMINISM_no_certain_matchup.md`) → "the riposte" (glossary *riposte*). A-98 vocabulary lane (2026-11-12, A-98; ledger `unified/work/A98_SWEEP.md`): "trained score/rank" → skill score (4); "talent" → attribute or governing attribute (6); "training" for the rank → skill score (1); proposed names `talent_level` → `attribute_level`, `pool.py::talent` → `pool.py::governing_attribute` and test names (1); rewordings by sense (2: retired kinds `aptitude`/`trait`, traits apart, Thread Sensitivity not a skill, line-wrapped "trained").

**Depends on:** §1 on `03_PC_duel_round_and_approach_B.md` steps 1–2 (B16) and MB's window (`04_MB_manager_battle_one_resolver.md` §7, B20); §2 on `U5a_capability_home_and_two_inputs.md` Part B (B04/B05) and `U5a_DICE_owed_edits.md` §1 (B05); §3–§4 on the same; §6 on `22_HAPPENINGS_C_a_killing_is_a_crime_someone_commits.md` (B37) and `U5a_CORE_owed_edits.md` §E (the frozen `PersonInterior`, B03); every keyed draw on `11_GO_one_draw_owner.md` (B06).
**Lands in batch:** per §5 as mapped by `U3_CONFLICT_LEDGER.md` C3-D4: §2–§3 (row 4) in B05; §4 with rows 5 in B15 (`B15-pc-calibration`); §1 (row 9) in B30; §6 in B37 with HAP_C (U3 §4.1 row 59).

## Status: PROPOSED (a plan for future execution; nothing here is executed by the closing lane)

Author: U5b closure lane (Fable), 2026-11-12. Read at `6910680`. Carries Jordan's answers A-4, A-6, A-7,
A-8, A-31 and the ladder-closed D-40 and D-41 (`unified/DECISIONS_ANSWERED.md`) into `modules/combat/` and
its seam, where no file carried them: `U5a_capability_home_and_two_inputs.md` row B7 names this lane for
the module half and specifies nothing; `03_PC_duel_round_and_approach_B.md` §8 names the nesting question
and resolves nothing. Findings carried: `audits/03_PC_audit.md` §11 item 2, H-97, F-PC-08 (c) and (d);
`audits/03_PC_audit_addendum_B.md` §B4 rows 1 and 2; `audits/16_PESSIMIST_PC.md` F-PES-PC-01, -02, -11,
J-1, J-2. Reference only (CLAUDE.md §0.05); not ratified by being written. No number below is a balance
claim; every value named is a seed with its control arm.

## What it changes in `engine/season/` at runtime

§1: nothing until a field or a skirmish calls a nested round (`03_PC_duel_round_and_approach_B.md` step 5).
§2: nothing at the shipped realm (every person's skill score is the default; the pool and the obstacle
keep their values); the fight stops rounding a fractional pool. §3: behind a fixture whose control is
today's Endurance cut; at the live arm a wounded person enters a fight with his Health track whole and a
level against his rolls. §4: every season fight (the damage scale); one declared re-record of every
combat golden and the armour reference, shared by the whole batch of §5. §6: behind a fixture whose
control is no edge; at the live arm the first exchange of an attack the target did not expect.

## §1 · A duel inside a battle is a nested contest, counted against a cap (A-4)

**Decided by A-4:** called from inside the battle, as a nested contest; person-supplied decision functions
are one declared class of adapter input; *"nesting cap to be set (default decided by the PC/MB lane's
plan)"*. Layer 1 §39.3 (`architecture/holonic_ARCHITECTURE.md:1395-1401`) says the depth cap has no
default and that exceeding it *"must produce a typed error result, checked by the caller"*. A-4 supplies
the default the text withheld; the amendment text is owed (edit 5) and is not applied here.

**The cap is 1** (ladder step 5): the smallest value that admits what A-4 rules. Depth 0 is the contest a
provider was called for (a `fight`, a field, a squad field). Depth 1 is one duel round called from inside
a field or a squad field. Nothing in the suite calls anything from inside a duel round, and the round
entry takes no callable that could (`DuelRoundInput` carries records, never a `duel`). `[ASSUMPTION;
medium; Jordan to correct; revert: the fixture's value]`.

| # | owner | exact edit |
|---|---|---|
| 1 | `engine/season/data/fixtures.py` | `contest_nesting_cap: int = 1`, with its hole-register row (grade `assumption`, source A-4, sweep `1 / 2`) |
| 2 | `engine/season/seam/contest.py` (W3-1: home decided, `[ASSUMPTION: this file — basis: it already owns the contest depth cap and its typed refusal, `04` §C.5, so the cap stays enforced in one module]`) | `nested_entry(role: str, depth: int, fx) -> Callable`: resolves the composition role (`composition.require`) and returns a callable `(typed input, rng) -> typed outcome`. When `depth > fx.contest_nesting_cap` the callable returns the typed depth-cap refusal `ContestError("max_depth reached", depth, fx.contest_nesting_cap)` (`seam/contest.py:28-36`; `04` §C.5's `Refusal(depth_cap)`; D-U1-11b) and resolves nothing: a typed result the caller checks with `isinstance`, never a raise. `depth` and the cap are explicit at every call (no signature default, D-19). The function holds nothing and decides nothing (§44.3). The composition row: `combat.round {target: "modules.combat.fight:round", entry: query, needed_by: "engine/season/seam/contest.py::nested_entry"}` (`R1_READ.md` 7b-11) |
| 3 | `engine/season/seam/wrappers/mass_battle.py::resolve` (and the squad entry's adapter when it lands) | builds `duel = nested_entry("combat.round", depth=1, fx)` and passes it to the module beside `decide`. The wrapper's docstring names the class once: **callables supplied for persons** (`decide`, `duel`, a standing order evaluated into a decider) are one declared class of adapter input beside "the projection" (`04` §A.2), by A-4; the existing `host` departure note at `seam/wrappers/combat.py:331-332` is re-pointed to the same sentence |
| 4 | `modules/mass_battle/battle_loop.py` (the window, `04_MB_manager_battle_one_resolver.md` §4 and §7 as reconciled) | at a window, for each reported officer contact: the round's draws keyed `H(field_key, window, pair)` (A-30; `11_GO_one_draw_owner.md`; no sequential `getrandbits` from the field's stream, so the field's own draws are unaffected whether or not a `duel` was handed in), then `out = duel(DuelRoundInput(...), key)`; a depth-cap refusal leaves the contact unresolved and is reported on the field's outcome. The two `DuelState`s live in this loop's frame for the length of the call |
| 5 | Layer 1 text, **owed, not applied** (drafted here for the ratifying merge) | §39.3: *"The cap's default is 1 (A-4, Jordan 2026-11-12): a field or a squad field may call one duel round inside itself; a duel round calls nothing. Exceeding it returns the typed depth-cap refusal (`Refusal(depth_cap)`, §C.5)."* · `04` §A.2, the adapter row: *"…and callables supplied for persons (a decider; a nested entry), declared once as a class (A-4)."* |
| 6 | the ratified suspension (`proposals/2026-10-07-grid-mode-suspension.md`), **owed, CORE's** | one sentence admitting the consult at a phase entry inside a round, under the decider's existing contract (draws nothing, mutates nothing). A-9 (a turn is a short sequence) is the ruling that unblocks it; named for U5a's family, not edited here |

**Gate.** (1) With the cap at 1: a seeded field with two planted officers in contact shows one `round` per
window in the trace. (2) With the cap at 0: the same field returns the same band, its outcome names the
contact as unresolved with the depth-cap refusal, and the field's own keyed draws are those of (1). (3) `git grep -n
"modules.combat" modules/mass_battle engine/season/seam/wrappers/mass_battle.py` prints nothing (the role,
not an import).
**Falsifier.** A nested round that runs at depth 2; a field whose own draws change when the `duel`
callable is withheld; round state found on a wrapper attribute.
**Hash movers.** None until a contact is reported; then every field with one.
**Tests (W3-1).** `engine/season/tests/test_rem31_grid_suspension.py::test_a_field_contact_runs_one_duel_round_per_window`,
`::test_cap_zero_leaves_the_contact_unresolved_with_the_typed_refusal`; the grep of gate (3) in the commit body.

## §2 · The fight's two inputs and the one pool rule (A-6, A-7; CAP row B7)

**What the rulings fix.** A-6: one way of turning a score into dice, score plus a base, floor five. A-7:
the attribute and the skill score are two numbers. U1 §4 assigns them: the skill score gives dice; the governing attribute gives levels. The
fight is the one regime that already has this shape (ED-901: the pool from learned skill plus six, floor
five; attributes acting through sigma), which U1 cites as its precedent. So the module's arithmetic is
kept and its literals and its one folded input are what change.

| # | owner | exact edit |
|---|---|---|
| 1 | `engine/season/queries/inputs.py::PersonalCombatInput` | gains `pool_add: int`, `pool_floor: int`, `opposition_rate: float`, carried raw from the fixtures U1 §7 names; *(W3-1, D-U1-08:)* the field `faculties` is replaced by `scores: (int, int)` (each party's **skill score**, `pool.py::score`, CAP B1, what `ob_from_defender` opposes with) and `addends: (int, int)` (each party's registered pool addends, `POOL_ADDENDS`); the old name is retired in the same commit |
| 2 | `engine/season/seam/wrappers/combat.py::combat_input` | fills the three from `fx`; reads `score` and the addends where it reads `faculty` |
| 3 | `modules/combat/core.py` | `resolution_pool(score, addends, add=BASE_POOL, floor=POOL_FLOOR)` calls `sigma_leverage.pool_of(score, addends, add, floor)` = `max(floor, score + addends + add)` (the one owner, D-U1-08), with `int(round(·))` removed (F-PC-08 (d): a fractional pool is canonical and the bell-curve sampler takes one; a negative score meets the floor). `BASE_POOL` and `POOL_FLOOR` stay as the defaults the workbench passes. `ob_from_defender(defender, rate)` calls `sigma_leverage.opposed_ob(defender.score, rate)` (the one owner, CAP B5; never the addends) |
| 4 | **the fight's obstacle keeps its value (A-31: "obstacle left alone")** *[Folded (lane 29): superseded by A-71; one rate on the skill score, see the head line. The text is kept as the record of the default taken]* | the fight passes `opposed_ob` its own operand and rate: the defender's **score** at `fight_opposition_rate = 0.5`, which is today's `faculty / 2`. CAP row B5 as written would apply A-26's 0.4 to the defender's **pool** in the fight too; that moves every exchange (the pessimist's probe of that centring: 5.65 turns, 3.48 blows, 5.3% undecided (obstacle `0.4 × pool − 1`, `audits/16_PESSIMIST_PC.md:798`; lane 29's 29–50% is `0.4 × pool` with no offset; both superseded by A-79's skill-score operand, C3-N3), `audits/16_PESSIMIST_PC.md` §6.3) and contradicts A-31, the later and specific ruling for the fight. One function, two declared regimes, each named at the fixture: `opposition_rate` (argument, A-26) and `fight_opposition_rate` (the body, A-31; Jordan's obstacle ruling of 2026-08-15). **Flagged to U5a:** CAP B5's second file |
| 5 | `rosters.yaml: tables.capability_uses`, site `fight` (U1 §3; CAP B3) | the `dice` row names `add: pool_add, floor: pool_floor` as every site does. The site carries **no host-side attribute `edge` row**: in a fight the attribute input is the six attributes on `PersonalCombatInput.attributes`, applied by the module's own sigma assembly. *(W3-1, U1 architecture §3 item 7, U1 §4 C-07:)* who applies it is a fact of the site, said once: `rosters.yaml: capability_use_sites` maps `fight` to its one reader `seam/wrappers/combat.py::combat_input → PersonalCombatInput (applied by the module)`, and the row is `{role: edge, key: attributes, site: fight}` with no `applied_by` column; so `advantage_sigma` adds no second attribute term to a fight. CAP B3's two `edge` rows are for `social_roll`, `task` and `notice` |

**Gate.** (1) Control: `build_realm(0..2)` season hashes EQUAL (every score is the default, pool 8 against
obstacle 1.0, as today). (2) Module: the mirror band shares of `audits/16_PESSIMIST_PC.md` §1.1 reproduce
at score 2, 5 and 8 (the obstacle did not move). (3) A hand-built pair, one of skill score 5 and
Strength 2, one of score 2 and Strength 5, against one opponent: different felled shares beyond the
disjoint-seed band (skill score and attribute are separate). (4) `resolution_pool(2.5)` is 8.5 and
`resolution_pool(-3)` is 5. (5) `python tools/export_engine_params.py --check` green.
**Falsifier.** A fight whose pool moves when a person's attribute rises and his score does not; a second
attribute term on a fight (the same attribute counted by the module and by `advantage_sigma`); an even
exchange centred anywhere but where §1.1 measured it.
**Hash movers.** None at the shipped realm. Lands in the batch of CAP Part B and DOE §1 (B05).
**Tests (W3-1).** `engine/season/tests/test_combat_module.py::test_resolution_pool_is_unrounded_and_floored`
(gate 4), `::test_training_and_talent_move_the_fight_separately` (gate 3), and the export's `--check` (gate 5).

## §3 · A wound carried into a fight is a level, not a shorter Health track (A-8)

**Problem.** `seam/wrappers/combat.py:143-152` (`party_end`, H-97): a person's Endurance arrives one point
lower per body band and his tracker starts clean. So a wounded man's whole wound model shrinks (Health,
Wound Interval, Max Wounds all derive from Endurance), and at one band down a mirror is 58.8% felled, at
the bottom band the loser dies to his first blow in 97.2% (`audits/03_PC_audit.md` E5;
`16_PESSIMIST_PC.md` §3.6). Inside a fight the engine already spends a wound as a level on the roll
(`combat_systems.wound_impairment`, `WOUND_ATK_OB`, `WOUND_DEF_OB`, `config.py:124`). Two ladders for one
quantity; A-8 rules one: *a level against the roll, as combat spends it*.

| # | owner | exact edit |
|---|---|---|
| 1 | `engine/season/data/fixtures.py` | `carried_wound_model: "endurance_cut" (control, today) | "level"`; shipped at the control until the batch of §5 reads its gate |
| 2 | `engine/season/queries/inputs.py::PersonalCombatInput` | `carried: tuple = (0.0, 0.0)`: each party's signed level from the `wounds` advantage source (CAP B6; `10_DICE_advantage_sources_for_the_arcs.md` Edits B–D), computed host-side by the one reader `advantage_sigma` |
| 3 | `engine/season/seam/wrappers/combat.py` | under `level`: `party_end` returns the authored Endurance (no band cut) and `combat_input` fills `carried`; under `endurance_cut`: as today and `carried` zero |
| 4 | `modules/combat/combat_systems.py::assemble_net_sigma` | one term: the aggressor's carried level against his own attack and the defender's against his own defence, added where `wound_impairment` is added and in the same sign convention. No new constant: the size is the season's `wound_step` level |

**Gate.** Control arm: hashes EQUAL. Live arm, module scale, n 1,000 a cell with a disjoint-seed control:
a fighter one band down is felled more often than the mirror, and less often than the 58.8% the Endurance
cut gives; at the bottom band first-blow deaths fall below 97.2%; his Health and Max Wounds equal an
unwounded man's. Season: a person at `body` 400 rolls the same level against him in an `argue` and in a
`fight` (read off the two Events' recorded terms).
**Falsifier.** Under `level`, a wounded fighter whose Max Wounds differs from his unwounded self; a carried
level applied twice (host and module).
**Hash movers.** At the flip: every fight with a party below his first body band.
**Tests (W3-1).** `engine/season/tests/test_combat_module.py::test_a_carried_wound_leaves_health_and_max_wounds_whole`,
`::test_the_carried_level_is_applied_once`; the season reading (the same level in `argue` and `fight`) in the commit body.

## §4 · The damage scale: a Success is one Wound Interval (A-31)

**Decided by A-31:** longer fights; the damage scale lowered so a Success is one wound interval; the
obstacle left alone; combat recalibration owed.

| # | owner | exact edit |
|---|---|---|
| 1 | `modules/combat/core.py:168` | `DMG_SCALE` from 1.55 to **1.07**, the value at which an arming sword's Success against light armour equals the default fighter's Wound Interval (the pessimist's probe, `pK_scale2.py`: a Success is 13 against an interval of 9 at 1.55). *(W3-1, U1 §4 P-02:)* the value is decided (A-79 accepts lane 29's tuning, whose window is 0.99–1.08, `29_DICE…` item 29-3), not left to a sweep; the gate below reads it |
| 2 | `modules/combat/core.py:168`, the comment | restated to the rule it names ("even Success = 1 WI at the season default kit; 1.07, A-79 / `29_DICE` 29-3") |
| 3 | re-derived, never by hand | `engine/engine_params/combat_engine_v1.json` (`tools/export_engine_params.py`); `workbench/data/combat_armour_reference.json` (`armour_participation.py --update`, once, for the whole batch of §5) |

**Gate (readings with their controls; none is a target).** The pessimist's census re-run (`pF_story.py`
F1, 5,000 fights, and `pK_scale2.py`): a Success from an arming sword against light armour deals the
Wound Interval within 1; the share of deaths taking exactly two blows on the loser is below 70.0%; mean
wounding blows above 3.2; the lead-change share and the first-wounded-wins share are reported beside
their disjoint-seed controls; undecided stays under 2%. `--check` green.
**Falsifier.** After the edit, `blood` terms still one blow in more than nine duels in ten for a reason
other than first blood being the first wound gate; a mirror whose felled share leaves the control band
(the scale is symmetric, so it must not).
**Hash movers.** Every world with a fight; every combat golden; the armour reference.
**Gate artifact (W3-1, test 9).** `pF_story.py` and `pK_scale2.py` are the pessimist's scratch probes, not in
the tree: the step first writes them as one workbench file,
`systems/combat/combat_engine_v1/workbench/scale_census.py` (F1's 5,000-fight census and the
Success-against-interval reading), whose expected output is the five readings above with their controls.
Not a CI row.

## §5 · One landing order for personal combat

*(W3-1, `U3_CONFLICT_LEDGER.md` C3-D4: rows 1–3 → B14 (row 2's `03_PC_duel_chain_reach` already in B01);
row 4 → B05; row 5 → B15; rows 6–8 → B16; row 9 → B30; row 10 → B18.)*

Each row is one batch with one gate; an arrow in the dependency column is "must land before".

| # | batch | files | dependency | movers |
|---|---|---|---|---|
| 1 | the typed outcome and one door | `03_PC_typed_outcome_one_door.md` Parts A, B, C | none | two declared (`prevailed`, `fell_to`) |
| 2 | reach | `03_PC_duel_chain_reach.md`; then `14_VERBS_PHYSICAL_A` A4 → A3's `duel` drop | 1 is independent | formation |
| 3 | the export | `03_PC_weapon_records_in_the_export.md`; `03_PC_weapon_form_at_round_start.md` | 1 (Part C's `CFG` move first) | armour reference (PF) |
| 4 | the roll's inputs | §2 here, with `U5a_capability_home_and_two_inputs.md` Part B and `U5a_DICE_owed_edits.md` §1 | U5a's batch | none at the shipped realm |
| 5 | **the combat calibration batch: one re-record** | §4 (the scale) → `16_PESSIMIST_PC_B` (the deep tier) → `16_PESSIMIST_PC_D` (the bare zone) → `14_VERBS_PHYSICAL_A` A3 (the mortal-wound draw) → `18_DETERMINISM_no_certain_matchup.md` (the riposte) → `16_PESSIMIST_PC_A` (the yield) → §3's flip *(U6 R-A: A3 moved ahead of the riposte and the yield, each of which names A3 among its `Depends on`; A3 depends on neither)* | 1 (PES-C and A3 read the dataclass); each step's own gate is read before the next lands; the goldens, the armour reference and the export are re-recorded **once**, at the end, and the commit says so | every fight |
| 6 | the round | `03_PC_duel_round_and_approach_B.md` steps 1 and 2 | 1, 5 | one (the per-round key, A-30) |
| 7 | the approach | PB steps 3a, 3b, 3e; 3c ships at a coefficient of 0 (D-40: leans first, the transfer behind a dial at zero, set after A-31's scale has landed) | 5 and 6. **Added gate (pessimist R-6):** a state-reading policy beats never-lean by more than the interval in some named matchup, or the menu is not shipped | none at `normal` |
| 8 | deciders | PB step 4; `03_PC_exits_withdrawal_recovery.md` Part A | 7; CHAR's alignment block | none with no cell authored |
| 9 | the nested round | §1 here; PB step 5; `04_MB_manager_battle_one_resolver.md` §7; `04_MB_squad_grid_of_named_characters.md` | 6; MB's window | fields with a contact |
| 10 | content | `03_PC_person_inputs_content.md` Parts B–D, behind `U5b_PC_residue.md` §3's census; `03_PC_loadout_and_carry.md` | 3, 4, 6 | fights between persons who differ |

Why 5 precedes 7: the approach's measurements (`audits/03_PC_audit_addendum_B.md` E-B10 to E-B14) and the
pessimist's (§2.6) were taken on a fight of three blows with an unreachable deep tier; A-31 and PES-B
change both, so the lean coefficients are swept after them or not at all.

## §6 · The opener of an unexpected attack has an edge on the first exchange (D-41 B, after A-16)

**Decided by the ladder** (`DECISIONS_ANSWERED.md`, D-41: B, following A-16: murder needs ambush to mean
anything). Measured today: who acts first is worth nothing (A felled 50.7% first, 50.1% second, 6,000
fights), so "the opener goes first" would change nothing; the edge is a level on his first exchange.

| # | owner | exact edit |
|---|---|---|
| 1 | `engine/season/decision/options.py` (owner of `VIOLENCE_CONTEXT_READERS`) | one pure function `expected_by(target: PersonInterior, actor_id) -> bool` *(W3-1, `R1_READ.md` §1.1: a frozen snapshot and no query handle, `04` §C.3; the readers it mirrors already take the interior)*: true when any of the existing context readers, asked **from the target's side** about the actor, answers (a challenge Record naming both; a warrant or custody between them; a violent deed by the actor in the target's own ledger this season; a war he has heard of that puts the actor among his enemies). No new reader: the four that license violence, mirrored. Person-side, no `World` |
| 2 | `engine/season/seam/wrappers/combat.py::combat_input` | `opener_edge = fx.surprise_level if not expected_by(<the target's frozen PersonInterior>, actor) else None`, carried as `PersonalCombatInput.opener_edge: Optional[str]` (a named level of `dice_engine.LEVEL_SIGMA`, or `None`) |
| 3 | `engine/season/data/fixtures.py` | `surprise_level: None (control) | "minor" | "moderate"`, swept; shipped `None` until `22_HAPPENINGS_C_a_killing_is_a_crime_someone_commits.md` (A-16; U5d's) gives an own-motive attack a context, because under today's four contexts every attack that forms is one the target has reason to expect |
| 4 | `modules/combat/wrapper.py::engagement` | on the opener's first attack of the fight's first engagement only, the named level is added to his net sigma through `assemble_net_sigma` (under the soft cap, like every modifier); one `surprise` trace event. No draw is added or moved |

**Gate.** Control (`None`): byte-identical. Live, module scale, 6,000 fights (`pL_misc.py`'s first-mover
arm): the opener's felled share is below the mirror control by more than the interval at `moderate`; a
fight whose target `expected_by` is true reads the control. Season: a hand-built attack on a person with
no context against the actor carries the `surprise` event; the same attack after a witnessed threat does
not.
**Falsifier.** An edge on a duel (`accept`) or on an arrest resisted; an edge that persists past the first
exchange; a `surprise` event at the control arm.
**Hash movers.** None at the control; at the flip, every fight opened on a person who did not expect it.
**Not decided here.** Whether a watch (`capture`) should carry an edge of office (pessimist §2.5): no
ruling orders it; `14_VERBS_PHYSICAL_A` A1–A2 give the watch the warrant and the court, not a level.

## Who lands it, and dependencies

An IN-lane implementation session with the PC lane's review, in the order of §5. §2 waits on U5a's batch;
§1 on PB steps 1–2 and MB's window; §6 on U5d's murder carrier. Nothing here edits Layer 1; edits 5 and 6
of §1 are text owed to the ratifying merge. *Tier (W3-1):* §1, §2, §3, §6 `sonnet`; §4's census run by
`haiku` (`valoria-measure`) and read by `opus` (the calibration batch's judgment node). §6's gate names
`pL_misc.py` (scratch): the step first writes its first-mover arm as
`systems/combat/combat_engine_v1/workbench/opener_edge_probe.py`, expected output the opener's felled share
against the mirror control at 6,000 fights per arm.

## NERS reading (E last)

- **N.** Each section removes a second ladder or supplies a ruled thing with no carrier: one cap for every
  nested call; one pool rule; one channel for a wound in a debate and in a fight; a fight long enough for
  the approach the intent asks for; an ambush that is not a fair duel.
- **R.** A hurt man's next fight is harder, not a formality; a fight has a middle; a murderer is favoured
  on his first blow and no further. Complete at the extremes: the cap returns a typed result; a negative
  score meets the floor.
- **S.** The fight keeps its obstacle by ruling and says so at the fixture, so the one place the ladder is
  centred differently is named and not accidental.
- **E, against that.** Three fixtures, five record fields, one seam function, one sigma term, one scale
  value; `party_end`'s cut and two literals retire.

## Cost class

§1, §3, §6: small builds. §2: edit. §4: edit plus the calibration batch of §5 (one deliberate re-record).
