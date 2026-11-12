# U5a · CAP — the capability surface in its decided home, and the roll with two inputs

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
| A4 | `rosters.yaml`: rosters `capability_roles`, `capability_use_sites`; `tables.capability_uses` with today's rules restated as rows; `advantage_sources: [effort, capability]`; `obstacle_terms: [capability]`; `_load_capability_uses` | MAP §G edits 1 (less `tables.capabilities`), 2 | U1 §3's six amendments: selectors `verb` / `verb.base`; `per: mid`; one meaning of `against`; hostile-only `circumstance`; `gate` closed; a seat's modifier is an `addend` |
| A5 | the decision layer's two literals become rows (`told_claim_credit`, `own_state_gate`); `capability_factor`, `capability_admits` in the substrate | `02_CHAR_capability_uses_table.md` edits 3–5 | none |
| A6 | `opposed_ob` once in `sigma_leverage`; `SocialContestInput.obstacle_terms`; `fed_by` on the provider's record; `pool_add` / `pool_floor` carried raw on `PersonalCombatInput` | MAP §G edits 5–8 | in Part A the fixtures reproduce today: social 0 and 0, combat 6 and 5, `opposition_rate` 0.5 |
| A7 | the cast row's `capabilities:`; `UNREAD_KEYS`; bundles at a rank; `rank_at_least` | CORE Edit 5; DEF Edits 2–4 | none |
| A8 | the sheet shows `attributes`, `thread_sensitivity`, `heritage`, tenures | CORE Edit 6; DEF Edit 5 | one change to one dataclass |
| A9 | one Endurance default | CORE Edit 7 | none |
| A10 | `raised_capability` reads the row's ceiling | MAP §G part two | control: no ceiling (today's bytes); a mover only for a rank that would pass 7 |

**Gate (Part A).** `python tools/export_descriptors.py --check` passes; the driver constructs;
`headless --case NPC-088 --seasons 2 --seed 0` prints `5405522c36b0399247f83fd9f6d29494`; `corpus_run` seed
0 reproduces its `DEGREES RESOLVED` tallies; MAP's probe E-B04 re-run reads the three host records byte-equal
and `fed_by` on a graded `argue` lists exactly its `dice` and `opposes` rows.
**Falsifier (Part A).** U1 §8's four: delete the block (load refuses); delete a contested row's
`capability:` (load refuses naming the row); a negative-gain `circumstance` row, a `dice` use of a trait, a
`gate` row keyed on any capability but Thread Sensitivity or at any site but `own_state_gate` and
`told_retain` (U1 §3 amendment 5), each refused at load. Any of them loading falsifies the edit.
**Hash movers.** None.

## Part B — the roll with two inputs (one calibrated landing; every seeded result re-pinned once)

Lands with `U5a_DICE_owed_edits.md` §1 (the one sampler): A-5, A-6, A-7 and A-26 are calibrated together
(Jordan's own note on A-6), so they land as one batch behind one set of fixtures whose control arm is
Part A's bytes.

| # | owner | exact edit | answer |
|---|---|---|---|
| B1 | `engine/season/seam/wrappers/pool.py` | `score(w, p, verb)`: `max(untrained score, held rank)`; no attribute in it (TWO Edit A, with the `max(int(attr), int(have))` branch removed). `talent(p, verb)`: the governing attribute as held, else `None`. `faculty`: `max(pool_floor, score + addends + pool_add)` | A-6, A-7 |
| B2 | `engine/season/data/fixtures.py`, register rows | `pool_add` (control 0; live 6), `pool_floor` (control 0; live 5), one pair for every site; `talent_level` (control `None`; live `minor`); `opposition_rate` (control 0.5; live `MU_PER_DIE`, read from the owner); each `[ASSUMPTION; medium; Jordan to correct]` with a three-point sweep. MAP's `social_pool_*` and `combat_pool_*` are not created | A-6, A-7, A-26 |
| B3 | `rosters.yaml: tables.capability_uses` | the `dice` rows of `social_roll`, `fight`, `task`, `notice` name `add: pool_add, floor: pool_floor`; two `edge` rows per site: `{role: edge, key: verb.base, side: actor, per: mid, level: talent_level}` and `{role: edge, key: verb.base, side: subject, per: mid, level: talent_level, against: true}` (the subject's row reads `opposed_by` where the capability names one) | A-7 |
| B4 | `engine/season/seam/wrappers/sigma.py` | `_opposition_of` returns the opponent's pool by the same rule on his own score, no practice addend (TWO Edit B with `score` → the pool); a person subject always has one; `advantage_sigma` reads the `edge` rows through the signed two-list form (ADV Edit A) | A-26, A-7 |
| B5 | `modules/social_contest/roll.py::obstacle`; `modules/combat/core.py::ob_from_defender` | `opposed_ob(inp.opposition, inp.opposition_rate)`; hostile terms added; no favourable term subtracted (those arrive as leverage) | A-26, A-25 |
| B6 | `rosters.yaml: advantage_sources`, `sigma.py` | `wounds`: one named level against the wounded roller per `wound_step` of body lost, capped (ADV Edits B–D as written) | A-8 |
| B7 | `modules/combat/` (PC's lane, U5b) | combat's attribute sigma terms and its pool are the same two inputs; `BASE_POOL`, `POOL_FLOOR` become the workbench's defaults of the carried pair. Named for U5b; not specified here | A-6, A-7 |

**Gate (Part B).** (1) Control: every fixture at its control arm reproduces Part A's hashes. (2) Equal
opponents: for equal trained ranks 0, 2, 4, 7 and mid talent, P(margin ≥ 0) is within sampling error of one
half at every rank (the even contest is even; today 28 % Success-or-better). (3) Training and talent
separate: two hand-built persons, one rank 5 with talent 2, one rank 2 with talent 5, against one opponent,
read different band shares, and swapping the two `capability_uses` rows of B3 swaps them with no code edit.
(4) R-09's conjunct: `python -m engine.season.harness.aperture 4 0` prints *two actors at different pools:
yes* on a non-combat verb once Part C's content is in. (5) The calibration reading (`13_SC_calibration.md`'s
instrument, U5c): band shares at the realm's pools, reported in the landing commit, seeds 0–2; no balance
claim from one run.
**Falsifier (Part B).** A person's first trained rank lowers his pool; an authored character is easier to
oppose than an unauthored one; a favourable circumstance lowers an obstacle; a hash moves at the control arm.
**Hash movers.** Every world in which a graded act resolves: all goldens, re-pinned once with the sampler.

## Part C — content and the switch

1. `references/npc_registry.yaml`: `stats:` and `capabilities:` for the cast (content: Jordan and the CHAR
   content pass; today one of 46 rows authors `stats:`, two persons hold a key).
2. `engine/season/harness/populated.py::build_realm`: `cast_attributes` defaults on, in the same commit as
   (1). Declared build-hash mover.
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

**N.** Without the home a capability has two definitions the first time two lanes land; without Part B the
answers of 2026-11-12 are four separate movers on four fixtures nobody reads together. Tested top-down (a
designer adds a skill as rows), bottom-up (one pool reader, one edge reader), lateral (a fight, a debate, a
task and a notice draw compose one way), vertical (the port reads the exported block), diagonal (a seat's
modifier and a person's skill enter by different doors and cannot double). **R.** Talent and training make
different people (A-7's point): the gifted novice and the schooled plodder roll differently and can be told
apart afterwards through `fed_by`. Complete at the extremes: floor five, soft-capped levels, a ceiling on
rank. **S.** One pool rule, one obstacle rule, one sampler, one unit per channel. **E (last).** Two tables,
one column, four fixtures and two selectors, against nine proposals' private schemes.

## Cost class

Part A: edit plus a small build. Part B: small build and a calibration. Part C: content.
