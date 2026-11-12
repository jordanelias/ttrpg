# U5a · CAP — the skill surface in its decided home, and the roll with two inputs

Folded: 2026-11-12, lane 29 (`audits/29_ONE_OPPOSED_RULE.md`; `proposals/29_DICE_one_opposed_rule_form_and_tuning.md`), on Jordan's A-71 (one opposed-contest rule for the argument and the fight) — rows B4 and B5 are amended in one word: the operand `opposed_ob` reads is the opponent's **trained score**, not his pool. The base dice's mean (`MU_PER_DIE × pool_add`, the *even line*) is a named term of the social composer and is absent from the fight, whose defence layer already spends the defender's base. Every social and task obstacle this file orders is numerically unchanged (0.4 × pool = even line + 0.4 × score), and gate (2) holds as written on a `plain` row (closed form: 50.0% at ranks 0, 2, 4, 7; a `routine` row fails 56.9 to 60.1%). Measured reason: 0.4 on the pool in a fight leaves 29.0% of season-default mirrors undecided at twelve turns (49.7% with A-31's scale); 0.4 on the score leaves 0.1%. One fixture `opposition_rate` serves both modules. All other rows stand.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.3 rows CAP, §7, §7b-T; `unified/U1_OWNERS_AND_VOCABULARY.md` D-U1-01, D-U1-02, D-U1-04, D-U1-08; `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §3, §11 U1-A to U1-C; `unified/U3_CONFLICT_LEDGER.md` C3-A3 (3), C3-N27). Changed: row A4's "a seat's modifier is an `addend`" → the `office` leverage source read off the seat row's `modifier:` (D-U1-01), and "six amendments" → U1 §3's seven; rows B4 and B5's bodies now say **trained score** where they said pool (D-U1-02, the head's fold applied to the body); B1 uses the one pool rule `sigma_leverage.pool_of` (D-U1-08) and starts from lane A's `pool.py::score` split with `max(attr, have)` removed (C3-A3 (3)); B7 is specified (D-U1-08: `PersonalCombatInput.scores`, `.addends` replace `.faculties`); rows B8 (the `difficulty:` column, `task_difficulty` retired) and B9 (`unauthored_attributes` retired) are added from D-U1-04; Part C (2) follows D-U1-04/U1 §6; gates gain named tests and expected readings; lands-it and tier added. Not applied: C3-N6's "replace 'holds'" for this head — this head's "holds" is gate (2) on a `plain` row (50.0%, true), not C1's `routine` ceiling; the C1 caveat is carried in `13_SC_calibration.md`. A-98 vocabulary lane (2026-11-12, A-98; ledger `unified/work/A98_SWEEP.md`): "capability" in prose → skill (5); "trained score/rank" → skill score (5); "talent" → attribute or governing attribute (5); proposed names `talent_level` → `attribute_level`, `pool.py::talent` → `pool.py::governing_attribute` and test names (8); rewordings by sense (1: retired kinds `aptitude`/`trait`, traits apart, Thread Sensitivity not a skill, line-wrapped "trained").

**Lands in batch:** Part A B04 (U1-A); Part B B05 (U1-B, with `U5a_DICE_owed_edits.md` §1, `U5c_SC_one_obstacle_form.md` steps 1a–5, `29_DICE_one_opposed_rule_form_and_tuning.md` items 29-2 to 29-4); Part C U1-C (content, after B05's control reads clean). **Depends on:** B01 (lane A rebased: its `score` split, `unauthored_attributes`, `task_difficulty` are the starting point), B02 (the pin file).

## Status: PROPOSED (a plan for future execution; nothing here is executed by the closing lane)

Authored by the U5a unification-closure lane, 2026-11-12. It is the executable form of
`unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` (**U1**) and carries F-CORE-15, F-CHAR-19, F-DICE-01,
-03, -04, -17, -23, F-PES-CHAR-05 and the brief's §14 charge, as Jordan's answers of 2026-11-12 decide them
(A-5 bell curve, A-6 score plus a base floor five, A-7 two inputs, A-8 a wound is a level, A-11 no gate,
A-25 favourable raises the speaker, A-26 0.4 per point). It **adds no edit of its own where an existing
proposal has it**: it orders the edits of `01_CORE_capability_authoring_surface.md` (**CORE**),
`10_DICE_capability_axiom_map.md` (**MAP**), `02_CHAR_capability_uses_table.md`,
`02_CHAR_capability_definitions.md` (**DEF**), `10_DICE_one_score_two_roles.md` (**TWO**) and
`10_DICE_advantage_sources_for_the_arcs.md` (**ADV**), names which of their sentences the answers replace
(each of those files carries a `Reconciled:` line), and writes the edits none of them has.

## What it changes in `engine/season/` at runtime

Part A: nothing a season computes (same pools, obstacles and content hash at shipped data); it moves where
facts are authored and adds refusals at load. Part B is the mover the answers ordered: every rolled act's
pool, obstacle and leverage are composed by U1 §4; every seeded result moves once, with the sampler
(`U5a_DICE_owed_edits.md` §1), in one calibrated landing. Part C is content and one switch, a declared
build-hash mover.

## Part A — the surface in its home (hash EQUAL)

In order; each row is an edit some proposal already states, with what U1 changes in it.

| # | edit | carried by | U1's change to it |
|---|---|---|---|
| A1 | `references/descriptor_registry.yaml: capabilities` (closed sets and the four rows `copying`, `argue`, `inquiry`, `arms`); exporter and leaf (`CAPABILITIES`, `capability`) | CORE Edits 1–2 | `kinds` drops `attribute`; `untrained` is `[default, none]`; every row gains `gloss` (DEF Edit 1); `growth_rules` gains `fixed` (MAP §B) |
| A2 | the `capability:` column on contested and graded verb rows; the loader's four refusals | CORE Edit 3 | values per U1 §5; `lie` and `determine` carry `none` with a note until SC's `deception` and `law` rows exist, then those ids |
| A3 | derive `VERB_CAPABILITY`, `VOCATIONS`, `VOCATION_ATTRIBUTE`, `VOCATION_OPPOSED_BY` from the leaf and the verb rows; delete `rosters.yaml: verb_capability`, `vocation_attribute` and their two loaders; `rosters.yaml` gains `capabilities: {from_descriptor: capabilities}` | CORE Edit 4 | the pointer row is U1 §1's |
| A4 | `rosters.yaml`: rosters `capability_roles`, `capability_use_sites`; `tables.capability_uses` with today's rules restated as rows; `advantage_sources: [effort, capability]`; `obstacle_terms: [capability]`; `_load_capability_uses` | MAP §G edits 1 (less `tables.capabilities`), 2 | U1 §3's seven amendments: selectors `verb` / `verb.base`; `per: mid`; one meaning of `against`; hostile-only `circumstance`; `gate` closed; a seat's modifier is the `office` leverage source (U1 §3 item 6; D-U1-01), never a use row; `capability_use_sites` a map from site to reader |
| A5 | the decision layer's two literals become rows (`told_claim_credit`, `own_state_gate`); `capability_factor`, `capability_admits` in the substrate | `02_CHAR_capability_uses_table.md` edits 3–5 | none |
| A6 | `opposed_ob` once in `sigma_leverage`; `SocialContestInput.obstacle_terms`; `fed_by` on the provider's record; `pool_add` / `pool_floor` carried raw on `PersonalCombatInput` | MAP §G edits 5–8 | in Part A the fixtures reproduce today: social 0 and 0, combat 6 and 5, `opposition_rate` 0.5 |
| A7 | the cast row's `capabilities:`; `UNREAD_KEYS`; bundles at a rank; `rank_at_least` | CORE Edit 5; DEF Edits 2–4 | none |
| A8 | the sheet shows `attributes`, `thread_sensitivity`, `heritage`, tenures | CORE Edit 6; DEF Edit 5 | one change to one dataclass |
| A9 | one Endurance default | CORE Edit 7 | none |
| A10 | `raised_capability` reads the row's ceiling | MAP §G part two | control: no ceiling (today's bytes); a mover only for a rank that would pass 7 |

**Gate (Part A).** `python tools/export_descriptors.py --check` passes; the driver constructs;
`headless --case NPC-088 --seasons 2 --seed 0` prints `5405522c36b0399247f83fd9f6d29494` (the working tree's
reading before B01; re-read on the batch's base and quote that, C3-N27); `corpus_run` seed
0 reproduces its `DEGREES RESOLVED` tallies; MAP's probe E-B04 re-run reads the three host records byte-equal
and `fed_by` on a graded `argue` lists exactly its `dice` and `opposes` rows.
**Falsifier (Part A).** U1 §8's four: delete the block (load refuses); delete a contested row's
`capability:` (load refuses naming the row); a negative-gain `circumstance` row, a `dice` use of a trait, a
`gate` row keyed on anything but Thread Sensitivity or at any site but `own_state_gate` and
`told_retain` (U1 §3 amendment 5), each refused at load. Any of them loading falsifies the edit.
**Named tests (Part A).** `engine/season/tests/test_u1_capability_surface.py` (U1 §11 U1-A: the five refusals
and `test_derived_vocation_maps_equal_the_retired_rosters`); `engine/tests/test_opposed_ob.py` and
`test_pool_of_is_the_max_of_floor_and_sum`.
**Hash movers.** None.

## Part B — the roll with two inputs (one calibrated landing; every seeded result re-pinned once)

Lands with `U5a_DICE_owed_edits.md` §1 (the one sampler): A-5, A-6, A-7 and A-26 are calibrated together
(Jordan's own note on A-6), so they land as one batch behind one set of fixtures whose control arm is
Part A's bytes.

| # | owner | exact edit | answer |
|---|---|---|---|
| B1 | `engine/season/seam/wrappers/pool.py` | starts from lane A's `pool.py::score` split (`c5bf18a`); `max(attr, have)` is removed (A-7; C3-A3). `score(w, p, verb)`: `max(untrained score, held rank)`; no attribute in it (TWO Edit A, with the `max(int(attr), int(have))` branch removed). `governing_attribute(p, verb)`: the governing attribute as held, else `None` (read as the scale's mid-point). `faculty`: `pool_of(score, Σ addends, fx.pool_add, fx.pool_floor)`, the one pure owner `engine/dice_engine/sigma_leverage.py::pool_of` = `max(pool_floor, score + addends + pool_add)` (D-U1-08) | A-6, A-7 |
| B2 | `engine/season/data/fixtures.py`, register rows | `pool_add` (control 0; live 6), `pool_floor` (control 0; live 5), one pair for every site; `attribute_level` (control `None`; live `minor`); `opposition_rate` (control 0.5; live `MU_PER_DIE`, read from the owner); each `[ASSUMPTION; medium; Jordan to correct]` with a three-point sweep. MAP's `social_pool_*` and `combat_pool_*` are not created | A-6, A-7, A-26 |
| B3 | `rosters.yaml: tables.capability_uses` | the `dice` rows of `social_roll`, `fight`, `task`, `notice` name `add: pool_add, floor: pool_floor`; two `edge` rows per site: `{role: edge, key: verb.base, side: actor, per: mid, level: attribute_level}` and `{role: edge, key: verb.base, side: subject, per: mid, level: attribute_level, against: true}` (the subject's row reads `opposed_by` where the skill names one) | A-7 |
| B4 | `engine/season/seam/wrappers/sigma.py` | `_opposition_of` returns the opponent's **skill score** (`pool.score` for the skill the verb's row names as opposed, else the verb's own): no base dice, no practice addend, no seat, no attribute (TWO Edit B as first written; A-79, D-U1-02); the pool's base is the social composer's even line; a person subject always has one (the untrained score); `advantage_sigma` reads the `edge` rows through the signed two-list form (ADV Edit A) | A-26, A-7 |
| B5 | `modules/social_contest/roll.py::obstacle`; `modules/combat/core.py::ob_from_defender` | `opposed_ob(inp.opposition, inp.opposition_rate)` on the opponent's skill score in both modules (A-79, D-U1-02); the social composer leads with the even line `even_line(pool_add)`, the fight adds nothing (its defence layer spends the defender's base); hostile terms added; no favourable term subtracted (those arrive as leverage) | A-26, A-25, A-71 |
| B6 | `rosters.yaml: advantage_sources`, `sigma.py` | `wounds`: one named level against the wounded roller per `wound_step` of body lost, capped (ADV Edits B–D as written) | A-8 |
| B7 | `modules/combat/core.py`, `engine/season/queries/inputs.py`, `seam/wrappers/combat.py::combat_input` (PC's lane, U5b) | `resolution_pool` calls `sigma_leverage.pool_of`; `ob_from_defender(defender, cfg)` → `opposed_ob(defender.score, …)`; `PersonalCombatInput.faculties` is replaced by `scores: (int, int)` (the skill score) and `addends: (int, int)`, beside `pool_add`, `pool_floor`, `opposition_rate` carried raw; `combat_input` fills them; `BASE_POOL`, `POOL_FLOOR` become the workbench's defaults of the carried pair (D-U1-08; U1 §11 U1-B step 6) | A-6, A-7, A-79 |
| B8 | `engine/season/verb_table.yaml`, `rosters.yaml`, `data/verbs.py`, `data/fixtures.py` | the `difficulty:` column on every rolled row (`routine` at control), roster `difficulty_levels: [plain, routine, demanding, hard]`, `Fixtures.difficulty_ob` (control 0/1/2/3; live 0/0.5/1/1.5); delete lane A's `rosters.yaml: task_difficulty`, `data/verbs.py::_load_task_difficulty` and `Fixtures obstacle_model`'s `task` arm; `obstacle_default` and H-127 deleted (C-04). Hash-equal at the control arm (D-U1-04 edit (1); OBS §4 step 1a) | A-25 |
| B9 | `engine/season/rosters.yaml`, `data/rosters.py`, `harness/populated.py` | delete lane A's `rosters.yaml: unauthored_attributes`, `data/rosters.py::_load_unauthored_attributes` and the `cast_attributes` seating of unauthored values; `pool.py::governing_attribute` returns `None` for an unauthored key (read as the mid-point `(ATTRIBUTE_FLOOR + ATTRIBUTE_CEILING) / 2`) (D-U1-04 edit (2)) | A-7 |

**Gate (Part B).** (1) Control: every fixture at its control arm reproduces Part A's hashes. (2) Equal
opponents: for equal skill scores 0, 2, 4, 7 and mid-point attributes, P(margin ≥ 0) is within sampling error of one
half at every rank (the even contest is even; today 28 % Success-or-better). (3) Skill score and attribute
separate: two hand-built persons, one rank 5 with attribute 2, one rank 2 with attribute 5, against one opponent,
read different band shares, and swapping the two `capability_uses` rows of B3 swaps them with no code edit.
(4) R-09's conjunct: `python -m engine.season.harness.aperture 4 0` prints *two actors at different pools:
yes* on a non-combat verb once Part C's content is in (the line is `engine/season/harness/aperture.py:772`;
expected **no** at Part B's landing, since every person holds the default, U1 §11 U1-B check (3)). (5) The calibration reading (`13_SC_calibration.md`'s
instrument, U5c): band shares at the realm's pools, reported in the landing commit, seeds 0–2; no balance
claim from one run.
**Named tests (Part B; `engine/season/tests/test_u1_two_inputs.py`, U1 §11 U1-B).** Gate (2):
`test_equal_trained_ranks_at_plain_are_even` (ranks 0, 2, 4, 7: P(margin ≥ 0) within 0.005 of 0.5 by the
closed form); gate (3): `test_the_skill_score_gives_dice_and_the_attribute_gives_levels`; plus
`test_an_unauthored_person_reads_zero_attribute_levels`, `test_a_first_rank_never_lowers_a_pool`,
`test_the_opposition_reads_the_skill_score_not_the_pool`. `engine/season/tests/test_cr85_faculty_replaces_history.py`
and `test_cr20_attributes.py` are re-pinned, named in the commit.
**Falsifier (Part B).** A person's first skill score lowers his pool; an authored character is easier to
oppose than an unauthored one; a favourable circumstance lowers an obstacle; a hash moves at the control arm.
**Hash movers.** Every world in which a graded act resolves: all goldens, re-pinned once with the sampler.

## Part C — content and the switch

1. `references/npc_registry.yaml`: `stats:` and `capabilities:` for the cast (content: Jordan and the CHAR
   content pass; today one of 46 rows authors `stats:`, two persons hold a key).
2. `engine/season/harness/populated.py::build_realm`: `cast_attributes` ships on (lane A already flips it,
   OWED §E); after B9 it gates only the authored `stats:` (no unauthored value is seated). Authoring (1) is the
   declared build-hash mover (U1 §6; D-U1-04).
3. SC's rows `deception`, `law`, `insight`; PC's `healing`; CHAR's four `moved_by_*` traits: each a
   definition row then a verb value or a use row, by its own lane's proposal.

**Gate.** `decision_spread --persons` shows the cast's pools differing; E-03's census (83 of 83 at pool 2)
no longer reads one value. **Falsifier.** Authoring a `stats:` row moves no roll.

## Order, dependencies, who lands it

Part A: an IN-lane implementation session, after `01_CORE_tests_one_golden_owner.md` (so "hash EQUAL" is
read against one file); no dependency on a ruling. Part B: IN and SC together, with
`U5a_DICE_owed_edits.md` §1, `05_SC_opposed_obstacle_parity.md`, `05_SC_obstacle_difficulty_and_modifiers_B.md`
and `16_PESSIMIST_DICE_soft_ceiling.md` (one composer, one landing); PC's B7 in the same batch or the fight
keeps its literals behind the carried pair. Part C: after Part B's control reads clean (otherwise authoring
a character moves him under the old regime first and again under the new).

## NERS reading (E last)

**N.** Without the home a skill has two definitions the first time two lanes land; without Part B the
answers of 2026-11-12 are four separate movers on four fixtures nobody reads together. Tested top-down (a
designer adds a skill as rows), bottom-up (one pool reader, one edge reader), lateral (a fight, a debate, a
task and a notice draw compose one way), vertical (the port reads the exported block), diagonal (a seat's
modifier and a person's skill enter by different doors and cannot double). **R.** Attribute and skill score make
different people (A-7's point): the gifted novice and the schooled plodder roll differently and can be told
apart afterwards through `fed_by`. Complete at the extremes: floor five, soft-capped levels, a ceiling on
rank. **S.** One pool rule, one obstacle rule, one sampler, one unit per channel. **E (last).** Two tables,
one column, four fixtures and two selectors, against nine proposals' private schemes.

## Cost class

Part A: edit plus a small build. Part B: small build and a calibration. Part C: content.

**Lands it and tier.** Part A: the B04 batch, an IN `valoria-author` session on `sonnet` (`high`), closed by
`methodology-close` with its terminal `opus` critique once. Part B: the B05 batch (IN, SC, PC lanes), edits on
`sonnet`, the calibration reading on `opus`, one close. Part C: the CHAR content pass with Jordan (U1-C), each
content commit a declared mover said plainly as a re-record (CLAUDE.md §7).
