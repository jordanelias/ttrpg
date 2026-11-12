# U5a · Conflicts — CORE, CHAR, DICE, tests, census: what was decided, what is Jordan's, what was handed across

## Status: REFERENCE (a closure record for the suite; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: 601e715 (working tree), 2026-11-12. Closing lane: Fable unification-closure, family U5a.

Companion to `unified/U5_FINDINGS_CLOSURE_U5a.md` (every finding's disposition) and
`unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` (the one capability architecture). This file holds only
the places where two documents said different things. Each decided conflict names the documents, the
decision, the step of CLAUDE.md §0's ladder that decided it (1 superseded, 2 irrelevant, 3 a design
document, 4 precedent, 5 what is right for the code), and the edit made to the file that lost. Every edit
is a `Reconciled:` line at the head of that file, or a rewrite of the named item inside it; no finding of
any lane was deleted. Forty-six proposal files carry such a line from this lane.

`A-n` is an answer in `unified/DECISIONS_ANSWERED.md`; `D-nn` an entry of `unified/DECISIONS_FOR_JORDAN.md`.

---

## §1 · Conflicts decided

| id | the documents | the contradiction | decision | step | edit to the losing file |
|---|---|---|---|---|---|
| C-U5a-01 | `01_CORE_requirements_reading_record.md` §2 against `16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading.md` edits 2–3 | two instruments proposed for one property (does one person's act reach another): a `chronicle --propagation` reader, and a knockout arm with a planted control | the knockout arm is R-01's and R-02's `measure:`; `01_CORE_tests_shipped_world_falsifiers.md` rows 1–2 are the standing tests. One instrument per property | 5 | reading record: §2 withdrawn, §1 stands |
| C-U5a-02 | `audits/01_CORE_audit.md` resolution 13 (mark `(Person, weight)` `unproduced`) against workplan CR-08 (B10-18) | a matrix row marked as never produced, against a decided build of its writer | CR-08 stands; the row gets a producer, not a mark | 3 | none to a proposal (the resolution had no file); recorded in `U5a_CORE_owed_edits.md` §A |
| C-U5a-03 | `01_CORE_one_scene_contract.md` Edit 3 against `11_GO_player_surface_contract_B.md` §6 rules 2–4 and `18_DETERMINISM_SWEEP.md` D-06 | `decide=None` meant "the module's own policy" (a top-score pick), against "a person's own decider, sampled" | GO-B §6 governs: `decide=None` asks the decider the host builds from `decision/`, sampled; a module default is a named interim | 4 | Edit 3's sentence rewritten in the file; `Reconciled:` line |
| C-U5a-04 | `05_SC_playable_hearing_B.md` edit 4 against `01_CORE_one_scene_contract.md` Edit 1 | two shapes for the host's decider: one `decide` called with whichever view, or `deciders` keyed by module role | one `PlayHost` shape: `deciders` keyed by role; the hearing's is `deciders["social_contest.hearing"]` | 5 | SC hearing B: `Reconciled:` line (its stated revert, a second field, is not needed) |
| C-U5a-05 | `02_CHAR_reason_trail_and_small_edits.md` Part C against `01_CORE_requirements_reading_record.md` §1 | two proposals rewrite the same `requirements.yaml` `measured:` text in different shapes | the `reading:` record is the shape; Part C's two rewrites (R-06, R-08) land as records. Part B1 is workplan IN-14's own edit and lands there once | 5 | reason-trail file: `Reconciled:` line |
| C-U5a-06 | `02_CHAR_scar_cap_and_regard_unit.md` item 1 against `02_CHAR_scar_is_a_wound.md` (F-CHAR-17) | a cap per element per season, against the finding that such a cap bounds the rate and not the stock | one fixture `scar_season_cap` with the domain `None, element, person`; the old cap is its `element` arm; the old gate (median ≤ 4) is replaced, because it passes while every person is in crisis | 5 | scar-cap file: `Reconciled:` line |
| C-U5a-07 | `18_DETERMINISM_task_draw_for_uncontested_verbs.md` item 3 against `16_PESSIMIST_DICE_task_difficulty_and_throughput.md` | an unranked task rolled against `obstacle_default`, against the measurement that this stalls the realm | an unranked task is `plain`; the route never ships on `obstacle_default`; the throughput reading is a gate | 5 | 18-A: item 3 and gate item 5 rewritten in the file |
| C-U5a-08 | `02_CHAR_capability_uses_table.md`, `02_CHAR_capability_definitions.md`, `02_CHAR_which_ground_moves_whom.md` against `10_DICE_capability_axiom_map.md` and `01_CORE_capability_authoring_surface.md` | three lanes, three tables for one surface; a polarity (`against`) left to the builder; a definition table with no path | U1 §1–§3: one uses table with a `role` column; definitions in `descriptor_registry.yaml: capabilities` with `gloss` required; `against: true` means against the roller | 4, 5 | all five files: `Reconciled:` lines |
| C-U5a-09 | `16_PESSIMIST_CORE_the_record_holds_what_changed.md` edit 2 against `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md` item 4 | two emitters of `conviction.moved`, one silent and one witnessed | CHAR A emits it, witnessed (A-24: a crisis is drawn and seen); the CORE record proposal emits `scar.taken` only | 1 (A-24) | both files: `Reconciled:` lines |
| C-U5a-10 | `18_DETERMINISM_task_draw_for_uncontested_verbs.md` item 4 against `04` §B.13 invariant 12 and §C.4 | degree-keyed `writes:` on rows that declare no `contests:` | a `task` row keeps flat `writes:` and `emits:`, scales by `task_fraction`, and carries a failed draw as its keyed `emits_on_refusal` clause; a row whose cells differ by band declares `contests:`. Adopted by U5c for the verb proposals | 3 (Layer 1) | 18-A: item 4, the edits list and the cost line rewritten in the file |
| C-U5a-11 | `01_CORE_capability_authoring_surface.md` against `10_DICE_capability_axiom_map.md` §B (the home); `06_FA_office_capabilities.md` (`judgment`) against `05_SC_hearing_capabilities.md` (`law`); the verb values across five proposals | where a skill is defined; one skill under two names; four verbs with differing values | U1 §1, §5: definitions in the descriptor registry, the verb's skill a column on its row; the judge's skill is `law` (`judgment` collides with the role `judgement`); `interrogate: inquiry`, `lie: deception`, `determine: law`, `arrest: arms`, `march: none` | 4, 5 | CORE surface, FA office skills, DICE one-score: `Reconciled:` lines |
| C-U5a-12 | `10_DICE_capability_axiom_map.md` §B against U1; `10_DICE_one_score_two_roles.md` Edit A against A-7; `audits/10_DICE_audit_addendum_B.md` §5.4 against `10_DICE_advantage_sources_for_the_arcs.md` | definitions in `rosters.yaml`; the attribute folded into the score; a wound as an obstacle term | definitions move to the descriptor registry; `score` is the skill score and the governing attribute is read apart (A-7); a wound is a level against the roller (A-8), so the advantage-sources edits stand and §5.4 is not built | 1 (A-7, A-8), 5 | three DICE files: `Reconciled:` lines |
| C-U5a-13 | the DICE family, the DICE pessimist, three determinism proposals and the golden-owner proposal, against A-5 | each assumed the whole-dice roll, or named a second sampler | one sampler (`roll_net_continuous`), one resolver name, `band_odds` its closed form; the stochastic-die edit and the three-name vocabulary are withdrawn; the dice golden is regenerated, not trimmed | 1 (A-5) | nine files: `Reconciled:` lines |
| C-U5a-14 | `18_DETERMINISM_notice_is_a_draw.md` against `04` §A.2 (`loop/witness`'s may-read list) | WITNESS calling `sigma.faculty` to read the bystander's pool | the pool comes from a per-holder projection built at the barrier (D-74, taken B by the register: fix the code, not Layer 1), at the uses-table site `notice` | 3 (Layer 1) | 18-B: `Reconciled:` line |
| C-U5a-15 | `17_CENSUS_C1A_01_deletion_batches.md` D2 against `09_WR_B_chronicle_that_tells.md`, `09_WR_B_threadwork_session_and_practitioner.md`, `19_LACUNA_verdict_ladder_and_reversal.md`, `02_CHAR_voices_and_the_room.md` | the census deletes `world_q.projection` / `witnessed` / `PersonProjection` as caller-less; four proposals name them as a present reader | D2 stands; the one typed per-person reading is `account` and the host-side `receipt` (`11_GO_player_surface_contract_B.md` §3–§4); each of the four is re-pointed. Held if GO-B is rejected | 5 | four files: `Reconciled:` lines; the census file's premise corrected |
| C-U5a-16 | `17_CENSUS_C1A_02_wires_and_corrections.md` W4 against `02_CHAR_scar_cap_and_regard_unit.md` Addendum | two edits to `decision/choose.py::_stance_arm` | two facts about one term: `regard_sign` is how the act treats its subject, `beneficiary:` is whom it is done for; one term, written once | 5 | census A2: `Reconciled:` line |
| C-U5a-17 | `17_CENSUS_C1B_02_wires.md` W-3 and `17_CENSUS_C1B_03_corrections.md` C-6 against `09_WR_threadwork_module.md` edit 2 | two files moved into `modules/` with no caller; two files whose every function reads a deleted store | `threadcut.py` and `co_movement.py` are deleted before the move; `collective.py` and `opposing.py` move as inputs to `work`; an outcome field with no reader at landing is cut | 4 (a role no caller requires is not declared) | WR module proposal: `Reconciled:` line |
| C-U5a-18 | `17_CENSUS_REST_1_deletions.md` D1 row 6 against `17_CENSUS_C1B_01_deletions.md` D3; D1 row 1's condition against the dice proposals | a field cut from a file another batch deletes whole; a deletion conditional on a proposal since reconciled | row 6 withdrawn; row 1 stands (no reader of `pool_size` is gained under A-5); the two edits to `conviction.py` land in one commit | 2, 5 | REST deletions: `Reconciled:` line |
| C-U5a-19 | `17_CENSUS_C1B_01_deletions.md` D1, D3 against `01_CORE_tests_delete_what_cannot_fail.md` row 2 | edits to `tests/valoria/test_flow_skeletons.py`, a file the other proposal deletes | conditional on order: skip the edits if the file is gone; make them if it is not | 5 | C1B deletions: `Reconciled:` line |
| C-U5a-20 | `17_CENSUS_REST_2_wiring.md` W3 against U1 §3 amendment 5 | a second hand-written read of the Thread Sensitivity threshold, where U1 closed the `gate` role to one site | the gate is closed to one held value (Thread Sensitivity), at two sites (`own_state_gate`, `told_retain`), both read through `capability_admits`; A-11 admits this gate and no other | 1 (A-11), 5 | REST wiring: `Reconciled:` line; U1 §3 and `U5a_capability_home_and_two_inputs.md`'s falsifier amended to match |
| C-U5a-21 | `11_GO_player_surface_contract.md` §4 against `17_CENSUS_REST_3_corrections.md` C-5 and C-U5a-09 | "the row gains `scar.taken` / `conviction.folded`", where the rows already declare `scar.taken` and `conviction.moved`; "one edit" for two writers | no row gains a kind and `conviction.folded` is not created; the scar Event lands after the scar cap (883 writes in three seasons otherwise become 883 Events); the two writers have one carrier each | 5 | GO contract: `Reconciled:` line (§4 only) |

**Not conflicts this lane decided: holds lifted or closed by Jordan's answers and by the register.**

| document | what changed | by |
|---|---|---|
| `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md` | no longer held: a scene is a short sequence. Edits 1–4 are the plan; edit 5 is Layer-1 text (§2 below) | A-9 |
| `16_PESSIMIST_CHAR_C_the_stop_is_the_mans.md` item 4 | no longer held: a scruple is a drawn tendency; the threshold arm is the control | A-24 (D-28) |
| `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md` | the roll is confirmed; ED-IN-0261's "rolls nothing" is superseded | A-24 (D-26, D-27) |
| `01_CORE_capability_authoring_surface.md` Part three | withdrawn: a skill never gates an act | A-11 |
| `01_CORE_claim_fade_as_read.md` | Option A confirmed (forgetting is computed at the read) | the register's D-48, taken A |
| `16_PESSIMIST_CORE_a_refusal_is_remembered.md` | a refusal teaches privately | the register's D-46, taken B |
| `18_DETERMINISM_no_certain_matchup.md` | the form is closed: the upset happens inside the fight | the register's "not yours" table |
| `05_SC_opposed_obstacle_parity.md` | no longer held: an equal opponent costs 0.4 per point (U5c's file) | A-26 |

---

## §2 · For Jordan

Two items the register does not hold. Each is a live choice between two defensible readings; the default
is what the tree does today, and nothing is built on either until it is ruled.

**J-U5a-03 · Does a refused act leave a receipt for the scene it cost?**
`04_CODE_ARCHITECTURE.md` PART D row 51 says a refusal Event carries the debit's receipt. Measured
(`audits/01_CORE_audit_addendum_B.md`, headless, seed 0, three seasons): 27 refusal Events, 0 with
`changes[]`. The behaviour D-51 wants holds (a refused act costs its scene); the construction it names
does not. A second ratified source decides it the other way: #353 (`:877`, `:912-913`), ruled at H-28,
says budget is a Query, "without anybody storing a number".

- **Option A.** Build a spent-scenes write at the gate, so a refusal Event carries a receipt. D-51 holds as
  written. Cost: a stored number where #353 forbade one; every refusal becomes a write and every hash moves.
- **Option B.** Amend D-51 at workplan IN-44: the debit is observable as the Query's reading before and
  after, and a refusal Event carries no `changes[]`. #353 holds as written.
- **Default:** as built (B's behaviour); `U5a_CORE_owed_edits.md` §A row 10 refiles the register row and
  builds nothing.

**J-U5a-05 · Is the person you go to see occupied by your visit?**
Measured (`audits/16_PESSIMIST_CORE.md`): in 62 of 87 scenes with a named counterparty, that person was
also in another scene in the same round. A-9 gives a scene an internal order; it does not say whether the
counterparty is held by it.

- **Option A.** Not held (today). A person can be argued with by one visitor while acting elsewhere. Simple,
  and the realm keeps its throughput; the story "he was busy and I could not reach him" cannot be told.
- **Option B.** An interaction occupies its counterparty: his scene budget is debited or he is unavailable
  to a second visitor that round. Reaching a busy person becomes a real constraint; throughput falls by an
  amount that must be measured first.
- **Default:** A; no edit.

**Decided here and reversible on a word (not held).**

- **Which input is dice and which is levels (A-7).** The skill score (the skill's rank) adds dice to the pool;
  the governing attribute acts as levels, counted from the scale's mid-point. Grounds: A-6's own
  wording ("score plus a base") and the ED-901 precedent. The register's example read the other way.
  Reversing it is a swap of two rows of `capability_uses` (U1 §4; `U5a_capability_home_and_two_inputs.md`
  Part B gate 3 shows the swap), no code edit.

**Layer-1 text owed by the unification stage, applied only by Jordan's amendment** (never by an
implementation lane, never by editing Layer 1 to match code): A-9's restatement of #353 §27's order over
scenes (`16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md` edit 5); A-12's amendment of `04` §B.7 (a seat
may carry a modifier; U1 §3 amendment 6 says how it reaches a roll).

**Open in the register and bearing on this family** (cited, not re-filed): D-34 (luck in battle), D-61,
D-62 (one question or a list: it also decides whether the fixed order in which a person takes his
questions stands, PART 5), D-73 (the common people).

---

## §3 · Handed across to other families

Listed once. This lane decided none of these and edited none of their files beyond the `Reconciled:`
lines in §1. The subsystem named is what binds; the lane letter is verified only for U5b (PC, MB), U5c
(SC, FI, social verbs) and U5d (FA, SE).

| to | what | from |
|---|---|---|
| PC, MB (U5b) | mass battle's and combat's test strength: `approx` on exactness claims, an unasserted flag, an `or` that cannot fail, module-reload order dependence, ten golden pins off the shipped defaults, three strict known-red entries | addendum C §4; DG5, DG6 |
| PC (U5b) | `modules/combat/wrapper.py:565`'s unseeded generator fallback; combat's pool and attribute terms as the same two inputs (CAP row B7); the fight's believed estimate; the lasting mark; `test_rem31_grid_suspension.py` if a hand-built fight cannot reach ENCOUNTER (TDA §D) | CORE addendum B; U1; DG3 |
| MB (U5b) | the roller, ladder and per-die mean composed on the dice owner (`U5a_DICE_owed_edits.md` §1 row 4); F-DICE-21; F-PES-DICE-09; `04_MB_manager_battle_one_resolver.md` §2's row form gains `ally` (`17_CENSUS_REST_2_wiring.md` W1); `mass_battle.SEED_BASE` defined twice | DICE audits; census; DG6 |
| SC (U5c) | the amendments `16_PESSIMIST_DICE_task_difficulty_and_throughput.md` makes to SC's two files; rows that write nothing in any band (`speak`); the definition rows `deception`, `law`, `insight`; calibration of the four roll fixtures at the realm's pools; the favourable half of the room's composer; `covenant`'s one acceptance form | DICE pessimist; U1; sweep §3 |
| SC, FI (U5c) | what `HearingTurnView` may carry (a field enters with a reader: `17_CENSUS_REST.md` §1c); the roster name `speech_kinds` is held to (`17_CENSUS_REST_2_wiring.md` W2); the evidence and trail leads | census; DG1, DG3 |
| the verb strata | every band map follows 18-A's reconciled form (C-U5a-10); the 34 verbs that execute in neither instrument and the 39 consumers waiting on their kinds; six helper rows (`17_CENSUS_C1A_02…` W2) | sweep; census |
| FA (U5d) | which fields of `faction_standing` a faction's view shows (`U5a_CORE_owed_edits.md` §I); `faction_q.superiors`; succession under A-19 | census C1A; DG2 |
| SE | `weight.changed` and the CENSUS writer (CR-08); hunger erased inside the season; `(Rung, envelope)` has no writer in any proposal found by name | census REST; DG5 |
| ARCS | `12_ARCS_arcs_as_staged_goals.md` is amended by `U5a_CHAR_owed_amendments.md` §3 (a want can be kept or laid down); `audits/12_ARCS_adjudication.md` row 19's support becomes `17_CENSUS_REST_2_wiring.md` W3 | CHAR; census |
| WR | `world_q.within` (does a strife proposal call it); the `strife_kinds` reading (`17_CENSUS_REST_3_corrections.md` C-6); threadwork as reconciled (C-U5a-17); the document rule for a thread-substrate claim on paper (`14_VERBS_MATERIAL_E_knowledge.md`, not opened) | census |
| institutions | `convening_attached` is read as the quorum, or its key is deleted (`17_CENSUS_REST_2_wiring.md` W5) | census |
| GO | `11_GO_player_surface_contract.md` §4 as reconciled (C-U5a-21); the sheet's callers; D2 of the census waits on GO-B | census |
| the orchestrator | CLAUDE.md §7's sentence (`U5a_CORE_owed_edits.md` §G); the locked stale worktree `.claude/worktrees/agent-a737f996de1fa4752`; `references/what_valoria_is_and_what_runs.md` (eleven dead paths, not opened past the list) | addendum C; census REST §12 |

---

## §4 · Merged duplicates and owed amendments (one edit, named once)

| the same edit, stated twice | lands once, in |
|---|---|
| `02_CHAR_reason_trail_and_small_edits.md` B1 and workplan IN-14's narrowing of `offices` | IN-14 |
| the `decision/sheet.py` docstring row in the reason-trail file and `U5a_CORE_owed_edits.md` §B row 10 | the reason-trail file (CHAR Part C) |
| `audits/01_CORE_audit.md` resolution 21 and addendum C's T-22 | `U5a_CORE_owed_edits.md` §G |
| F-CHAR-05 and F-PES-CORE-01 | one finding; the CHAR carrier |
| the roll's record on its Event: `10_DICE_believed_odds_have_a_prior.md` Edit D, `10_DICE_capability_axiom_map.md` §D (`fed_by`), SC's `Margin.terms` | one record (U1 §8) |
| `17_CENSUS_REST_1_deletions.md` D1 rows 4–5 and `17_CENSUS_C1B_01_deletions.md` D1, both in `conviction.py` | one commit |

| amended proposal | by | what it gains |
|---|---|---|
| `02_CHAR_resolve_and_temper.md` | `U5a_CHAR_owed_amendments.md` §1 | a test-retest gate |
| `02_CHAR_scar_cap_and_regard_unit.md` item 3 | §2 | the `stance_scale` fixture |
| `12_ARCS_arcs_as_staged_goals.md` | §3 | a want can be kept or laid down |
| `02_CHAR_relations_have_a_ground.md` | §4 | `_bond` for every deed with a person subject |
| both reason-trail proposals | §5 | the stored deciding term, the draw included |
| `02_CHAR_scar_is_a_wound.md` | §6 | the fully scarred shift |
| `16_PESSIMIST_CHAR_B_a_pursuit_does_what_its_name_says.md` | §7 | `affiliation_signatures` |
| `16_PESSIMIST_CORE_a_refusal_is_remembered.md` | `01_CORE_claim_fade_as_read.md`; `U5a_DICE_owed_edits.md` §4 | one owner of fading; a failed search enters as a private claim |
| `01_CORE_tests_shipped_world_falsifiers.md` | `U5a_capability_home_and_two_inputs.md` Parts B, C | R-09's red-today falsifier is that proposal's gate |
| the three test proposals | `U5a_tests_digest_additions.md` | the instances the digests add, by the same rules |

---

## §5 · The three checks, by family (what was found and what was done)

**Layer 1 (Lens B; `04_CODE_ARCHITECTURE.md`).** Two proposals departed from a ratified row and were
rewritten to conform: 18-A item 4 (`04` §B.13 invariant 12; C-U5a-10) and 18-B's read (`04` §A.2's
may-read list; C-U5a-14). One internal ambiguity of the spec was named at the site and picked (B4's third
disposition): whether a verb's skill is a verb-row column (`04` §B.13) or a fold input (`04` §C.4);
U1 §1 picks the column. Two conflicts between Jordan's intent and a ratified row are listed with their
options and not resolved by editing Layer 1: J-U5a-03, and the two pieces of Layer-1 text owed in §2.
`U5a_CORE_owed_edits.md` §E carries the three conformance edits the CORE addendum found (a frozen
`PersonInterior`, the log's kind check, CR-07 with its precondition). `18_DETERMINISM_rival_acts_in_one_fold.md`
fills `04` F.26 and departs from nothing. No proposal of this family adds a `.md` under `systems/`, builds
on the retired Key substrate, or licenses a tree-wide guard.

**The standing rule (we do not do deterministic).** Rewritten or confirmed as draws: the crisis of faith
and the scruple (A-24), the uncontested verbs (18-A), notice (18-B), precedence between rival acts (18-C),
the upset inside a fight (18-D), the NPC decider inside a contest (C-U5a-03). Kept as computed, with the
reason: forgetting (the register's D-48, taken A), a term's lapse and a quorum (clocks and rules of an
institution, which decide no contested outcome), the told-drift selection (a keyed draw inside the act's
own band, A-30). The one hard gate left is Thread Sensitivity, by A-11, at two sites.

**Commensuration (`UNIFICATION_BRIEF.md`'s eight tests).** One vocabulary: `law` not `judgment`; one
resolver name; `account` for the per-person reading. One owner per fact: the capability home (U1 §1); one
pool pair and one opposition rate for every site (not `social_pool_*` and `combat_pool_*`); one owner of
fading. One unit and scale: one sampler, one ladder, one pool rule, one obstacle rule, levels as the one
unit of leverage. One interface per edge: U1 §8 between dice, character and every consumer; one `PlayHost`.
One order: the hash movers land after the golden-owner proposal, the roll's four changes in one calibrated
landing, content after the roll. No contradiction of fact: figures quoted from the whole-dice regime are
marked as the old regime's in the files that carry them. Stated intent: the capability-authoring charge
and the answers of 2026-11-12 are traced in U1 §9 and in the closure's preface.
