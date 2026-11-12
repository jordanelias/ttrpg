# Dossier 99 · cross-cutting and unclassified

Items no rule placed in one subsystem. The holistic audit reads this; per-subsystem audits may ignore it.

## code (unclassified) — 2

- `modules/__init__.py` — 5 lines — modules/ -- the A-25 modules: reachable running code only, one directory per module
- `systems/__init__.py` — 6 lines — systems/ — Valoria design docs by subsystem (ED-IN-0071 P4, §2a).

## tests (unclassified by name; cross-cutting or core) — 21

- `engine/season/tests/test_pc10b_challenge_record.py` — 374 lines
- `tests/valoria/test_balance_oracle_arms.py` — 191 lines
- `tests/valoria/test_dg2_yield_residuals.py` — 146 lines
- `tests/valoria/test_engine_does_not_import_systems.py` — 771 lines
- `tests/valoria/test_export_game_constants_ambiguity.py` — 76 lines
- `tests/valoria/test_export_sim_params.py` — 122 lines
- `tests/valoria/test_field_golden_pins.py` — 302 lines
- `tests/valoria/test_flow_skeletons.py` — 726 lines
- `tests/valoria/test_front_fixer_scope.py` — 84 lines
- `tests/valoria/test_import_cycle_game_state_npe.py` — 160 lines
- `tests/valoria/test_references_yaml_parse.py` — 63 lines
- `tests/valoria/test_registry.py` — 301 lines
- `tests/valoria/test_reserve_commit.py` — 91 lines
- `tests/valoria/test_season_invariant_sweep.py` — 217 lines
- `tests/valoria/test_season_providers_are_registered.py` — 315 lines
- `tests/valoria/test_stubwire.py` — 177 lines
- `tests/valoria/test_tag_normalizer.py` — 74 lines
- `tests/valoria/test_tn7_always.py` — 291 lines
- `tests/valoria/test_vocab_store.py` — 45 lines
- `tests/valoria/test_wiring_validation.py` — 101 lines
- `tests/sim/gauge_mb.py` — 576 lines

## workplan cards (mixed batches) — 2

- `B10-19` · DESIGN-FIRST CLUSTERS (NARRATION, CHARACTER, TROOP, EVENT DECK, THRUST LADDERS) — part3:380
- `B10-Z` · HELD AND LEAVE — part3:415

## workplan headings (part4) — 3

- part4:18 2. New positions (class:keyword)
- part4:23 CR-07 — Retire the stored `scale:` column (IN) · BATCH B10-Z (moved from B10-05 at its close) · STATE HELD · BUILD (deletion) when released · R — (class:keyword)
- part4:647 3. Carried v9 entries, part 1 (batches B10-02 to B10-16) (class:keyword)

## workplan headings (part5) — 5

- part5:97 3 (continued). Carried v9 entries, part 2 (batches B10-16 to B10-Z) (class:keyword)
- part5:292 4. Aliases and stale rows (what v10 does with each v9 handle that has no entry above) (class:keyword)
- part5:296 ALIAS (v9 handle -> v10 handle) (class:keyword)
- part5:305 STALE (v9 index rows for work that has landed) (class:keyword)
- part5:311 SEEN IN THE INPUTS BUT NOT A V9 KEY (flagged for the orchestrator; no entries written) (class:keyword)

## workplan headings (part6) — 6

- part6:17 1. The questions (class:keyword)
- part6:187 1a. The twelve narrow questions: Jordan's answers (class:keyword)
- part6:240 1c. Design-resolution questions M22 to M40 (the fold of 2026-10-30) (class:keyword)
- part6:270 2. Answers taken (each [ASSUMPTION; medium; Jordan to correct], each reverts alone) (class:keyword)
- part6:310 3. What the judges flagged for the orchestrator, and what v10 does with it (class:keyword)
- part6:320 4. Asks attached to the positions they block (class:keyword)

## workplan headings (part8) — 9

- part8:21 2. The hole-register rows (`engine/season/hole_register.yaml`) (class:keyword)
- part8:93 3. The editorial-ledger ids open since v9 (class:keyword)
- part8:119 4. v9's state index (42 rows; 40 here: CR-02 deleted the stale SC-08 and IN-38 rows) (class:keyword)
- part8:164 5. The nine requirements, the failing tests, and v9's self-contradictions (class:keyword)
- part8:185 6. The verb suite's stale and disputed gap entries (class:keyword)
- part8:213 7. The errata's open items (class:keyword)
- part8:236 8. Rows with no home (class:keyword)
- part8:256 The points where the two ladder judges disagree, and what follows (class:keyword)
- part8:264 9. Coverage (class:keyword)

## workplan headings (part9) — 4

- part9:15 2. The rows (class:keyword)
- part9:191 3. Rows that needed a new position, a question, or a stated gap (class:keyword)
- part9:209 4. Answers taken in this part (class:keyword)
- part9:222 5. Work v9 names that is not a hole row, and where it went (class:keyword)

## workplan headings (part10) — 7

- part10:17 2. The ids (class:keyword)
- part10:135 3. Closing rows to write at adoption step 4b (class:keyword)
- part10:181 4. What carries the work that stays open (class:keyword)
- part10:192 5. Answers taken in this part (class:keyword)
- part10:204 6. New positions this pass produced (class:keyword)
- part10:211 7. Coverage (class:keyword)
- part10:215 8. Not verified (class:keyword)

## workplan headings (part11) — 7

- part11:18 2. The register's 29 rows (class:keyword)
- part11:52 3. Reconciliations (class:keyword)
- part11:70 4. Answers taken, and the TL items that map to existing positions (class:keyword)
- part11:134 5. Sequence logic (class:keyword)
- part11:150 6. What is not folded, and why (class:keyword)
- part11:157 7. Coverage (class:keyword)
- part11:161 8. Not verified (class:keyword)

## workplan headings (part12) — 3

- part12:315 2. Items that are not positions (class:keyword)
- part12:368 3. The remediation proposal's deferred and declined rows (DEF-n, DEC-n) (class:keyword)
- part12:399 4. The verb suite's gap registers (class:keyword)

## workplan headings (part13) — 19

- part13:18 2. The amendments, by batch (class:keyword)
- part13:121 3. The entries (class:keyword)
- part13:125 REM-10 — REPAIR (B10-02) · HR-8 (class:keyword)
- part13:131 REM-16 — LIMIT (B10-02) · HR-5 (class:keyword)
- part13:138 REM-50 — REPAIR (B10-04) · AM-A-04 (class:keyword)
- part13:146 REM-52 — LIMIT (B10-05) · AM-A-05 (class:keyword)
- part13:153 REM-52 — LIMIT (B10-05) · HR-2 (class:keyword)
- part13:165 REM-21 — REPAIR (B10-05) · AM-A-06 (class:keyword)
- part13:173 REM-22 — LIMIT (B10-05) · AM-A-07 (class:keyword)
- part13:180 REM-23 — LIMIT (B10-05) · AM-A-08 (class:keyword)
- part13:186 REM-24 — LIMIT (B10-05) · AM-A-09 (class:keyword)
- part13:192 REM-25 — LIMIT (B10-05) · AM-A-10 (class:keyword)
- part13:198 REM-2C — LIMIT (B10-05) · AM-A-11 (class:keyword)
- part13:204 B10-05 exit (REM-21 to REM-25, REM-2C, CP-T05-04); REM-23 — LIMIT (B10-05) · HR-9 (class:keyword)
- part13:210 REM-27 — LIMIT (B10-06) · AM-A-13 (class:keyword)
- part13:216 REM-29 — LIMIT (B10-06) · AM-A-15 (class:keyword)
- part13:223 REM-2B — LIMIT (B10-06) · HR-3 (class:keyword)
- part13:314 REM-32 — REPAIR (B10-10) · AM-A-20 · LANDED in B10-10 (the Item commit is `69fa08a7`) (class:keyword)
- part13:359 B10-12 entry gate (CP-T04-01 … -08) — LIMIT (B10-12, CLOSED `6b6ec196`) · AM-C-13 (class:keyword)

## workplan headings (part14) — 5

- part14:85 B10-16 gates, IN-52 and `requisition` — RESEQUENCE (B10-16) · AM-E-21 (class:keyword)
- part14:309 REM-40 — CUT (?) · AM-A-02 (class:keyword)
- part14:316 REM-41 — CUT (?) · AM-A-01 (class:keyword)
- part14:323 REM-51 — CUT (?) · AM-A-03 (class:keyword)
- part14:331 4. Lane findings that changed nothing (class:keyword)

## workplan headings (part15) — 8

- part15:32 1. THE LADDER — M22 to M40 (class:keyword)
- part15:150 2. DESIGN LANES (class:keyword)
- part15:189 CL-SLICE · B10-S, the first playable slice (a landing, not a batch) (class:keyword)
- part15:196 CR-38 after #527 · the bench and the motion source (class:keyword)
- part15:203 3. ORDER AND GATES (class:keyword)
- part15:226 4. WHAT ESCALATES (class:keyword)
- part15:238 5. HOUSEKEEPING (not design items) (class:keyword)
- part15:248 6. VERIFICATION — what the next session runs to confirm each lane closed (class:keyword)

## workplan headings (part16) — 8

- part16:18 2. The positions (class:keyword)
- part16:86 3.1 Rules binding every position in this section (class:keyword)
- part16:93 3.2 Ids and order (class:keyword)
- part16:114 3.3 The entries (class:keyword)
- part16:116 `ED-IN-0352` — the record of Jordan's rulings of 2026-11-08 (IN) · a pointer, not a position · LANDED in this fold · R — (class:keyword)
- part16:389 3.4 Out of scope, with its owner (class:keyword)
- part16:409 3.6 Owed corrections (class:keyword)
- part16:414 3.7 Cadence (class:keyword)

## workplan headings (part2) — 6

- part2:16 1. The board (class:keyword)
- part2:43 4. R-03 — seasons tick scene by scene · met (class:keyword)
- part2:49 5. R-04 — strategic and management actions at differing scales · partial (class:keyword)
- part2:80 6. R-05 — all verbs built out · not_met (class:keyword)
- part2:138 10. R-09 — chains of events within a scene are probabilistic · partial (class:keyword)
- part2:150 11. The R-01/R-02 re-take (carried from v9 `_part2` §11; `requirements.yaml` cites it) (class:keyword)

## proposals (unclassified; cross-cutting) — 59

- `proposals/2026-08-18-breaking-the-recursion.md` — 852 lines — Breaking the recursion — diagnosis, and the one change that ends it — ## Status: PROPOSED — decision requested from Jordan. Terminal by design: executing it deletes it.
- `proposals/2026-08-18-culling-plan-v1.md` — 431 lines — Culling plan v1 — remove the apparatus that audits the apparatus — ## Status: RATIFIED AS PLAN OF RECORD (Jordan, 2026-08-18) — waves execute individually; §5 gates are hard
- `proposals/2026-08-18-recursion-interrogation-log.md` — 794 lines — Interrogation working log — "how do we break the infrastructure recursion?" — ## Status: REFERENCE — raw evidence log for `2026-08-18-breaking-the-recursion.md`. Delete with it.
- `proposals/2026-08-18-ruling-execution-plan.md` — 212 lines — Execution Plan — the fifteen rulings of 2026-08-18 — ## Status: PLAN — derived from RULED decisions, not itself a design proposal. Nothing here re-opens a ruling. No `.py` touched by this docum
- `proposals/2026-08-20-return-to-game-plan-v1.md` — 489 lines — Return to the game — the corrected plan — ## Status: PROPOSED — plan of record requested. Supersedes the *sequencing* of `2026-08-18-next-session-handoff.md`; does NOT supersede `202
- `proposals/2026-08-21-execution-order-v1.md` — 1154 lines — Execution order — the return to the game, as steps a session can perform — ## Status: PROPOSED — **merging this PR RATIFIES the step ordering** (ED-1094, and the flip is co-located here rather than left to an unprom
- `proposals/2026-08-22-wiring-map.md` — 474 lines — The Wiring Map — every required connection, where it lands, and whether it is coded or merely designed — ## Status: FINDINGS — a connection map, not a work plan and not a design. Nothing here rules anything. No `.py` touched. Content/design only
- `proposals/2026-08-23-MASTER-vocabulary-and-rulings.md` — 416 lines — MASTER — Competing Vocabularies, Three Rulings, and What Is Actually Waiting On You — ## Status: FINDINGS + RULING EXECUTION NOTES. Nothing here rules anything new. No `.py` touched, no registry edited, nothing deleted.
- `proposals/2026-08-23-competing-vocabularies-index.md` — 418 lines — Competing Vocabularies — the index, and what each conflict costs the fiction — ## Status: FINDINGS — an index and analysis. Nothing here rules anything. No `.py` touched, no registry edited. Content/design only; another
- `proposals/2026-08-23-rulings-and-adversarial-review.md` — 267 lines — Three Rulings, and an Adversarial Review of the Work That Preceded Them — ## Status: FINDINGS + RULING EXECUTION NOTES. Nothing here rules anything new. No `.py` touched, no registry edited, nothing deleted. Conten
- `proposals/2026-08-23-suite-00-index.md` — 138 lines — The 2026-08-23 Session Suite — Index — 
- `proposals/2026-08-23-suite-01-rulings-and-execution.md` — 309 lines — Suite 01 — The Three Rulings, and What the Tree Actually Does — 
- `proposals/2026-08-23-suite-03-competing-vocabularies.md` — 378 lines — Suite 03 — Competing Vocabularies, Adjudicated — 
- `proposals/2026-08-23-suite-04-wiring-gaps-and-orphans.md` — 261 lines — Suite 04 — What to Wire, Where, and What Is Missing — 
- `proposals/2026-08-23-suite-05-precedent-and-proposals.md` — 179 lines — Suite 05 — Precedent, and Eight Proposals — 
- `proposals/2026-08-23-suite-06-method-corrections-and-queue.md` — 237 lines — Suite 06 — Method, the Falsifier Record, and the Queue — 
- `proposals/2026-08-24-completion-plan-v1.md` — 308 lines — Completing the cull, the centralization, and the doc-vs-code conflicts — ## Status: PROPOSED (Jordan-requested, 2026-08-24). Ratifies on merge per CLAUDE.md §2.
- `proposals/2026-08-24-error-regions-v1.md` — 526 lines — Error regions from the 2026-08-24 hub-and-bus session — executable plan — ## Status: PROPOSED (Jordan-requested, 2026-08-24). Ratifies on merge per CLAUDE.md §2.
- `proposals/2026-08-24-suite-07-reconciliation-against-main.md` — 277 lines — Suite 07 — Reconciliation Against `main` — 
- `proposals/2026-08-25-throughlines-and-precedent/` — 10 files, 4390 lines — Throughlines and Precedent — a cross-scale analysis of Valoria — ## Status: PROPOSED — analysis and recommendation only. Nothing here is ratified by merging it.
- `proposals/2026-08-28-greenfield-systems-suite/` — 12 files, 3908 lines — Greenfield Systems Suite — Index, Hierarchy and Compliance Contract — ## Status: PROPOSED (2026-08-28) — surfaced by location (`proposals/`); ratifies nothing
- `proposals/2026-08-29-fable5-throughline-critique/` — 6 files, 1334 lines — Fable 5 throughline critique — index, verdicts, and the one finding that organizes the rest — ## Status: FILED (2026-08-29) — analysis, not a proposal. Nothing here ratifies on merge.
- `proposals/2026-08-29-greenfield-systems-suite-v2/` — 20 files, 11890 lines — Greenfield Systems Suite v2 — Index, Hierarchy and Compliance Contract — ## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
- `proposals/2026-08-29-valoria-from-scratch/` — 17 files, 9753 lines — Valoria, From Scratch — the master plan — ## Status: PROPOSED (2026-08-29). **HELD BACK FROM RATIFICATION-ON-MERGE, IN FULL.**
- `proposals/2026-08-30-fixes/` — 5 files, 2267 lines —  — 
- `proposals/2026-08-30-play-space-coverage/` — 11 files, 5908 lines — The Play-Space Coverage Instrument — plan — ## Status: PLAN (2026-08-30) — orchestration, not design. Nothing here ratifies on merge.
- `proposals/2026-08-31-authoritative-architecture/` — 9 files, 1857 lines — THE AUTHORITATIVE ARCHITECTURE — INDEX — ## Status: **PROPOSED (2026-08-31). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
- `proposals/2026-08-31-ideal/` — 9 files, 5876 lines — THE IDEAL DESIGN SYSTEM AND ITS CODE SHAPE — ## Status: DIRECT ANSWER (2026-08-31) to Jordan's question, from what the exercise established.
- `proposals/2026-08-31-ideal-v2/` — 5 files, 5442 lines — THE IDEALIZED SYSTEM, v2 — INDEX — ## Status: **PROPOSED (2026-08-31). NOTHING HERE HAS EXECUTED.**
- `proposals/2026-08-31-integration/` — 16 files, 4119 lines — Adversarial review brief — the two work lines — ## Status: BRIEF (2026-08-31) — planned by Fable 5; reviews by read-only critics; writing by Opus/Sonnet.
- `proposals/2026-08-31-pr350-archive-recovery/` — 19 files, 3393 lines — THE BEST IDEAS IN THE 2026-06-28 ARCHIVE — and what PR #350 is missing — ## Status: **PROPOSED (2026-08-31). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
- `proposals/2026-08-31-shape-tracer/` — 32 files, 18865 lines — Shape tracer — two executed tests of PR #350's idealized code shape, and what they demand — ## Status: **PROPOSED (2026-08-31). HELD BACK. Nothing ratifies on merge.**
- `proposals/2026-08-31-throughlines.md` — 865 lines — THROUGHLINES OF THE 2026-08-31 SESSION — the design and its code shape — ## Status: PROPOSED (2026-08-31). Ten throughlines drawn from an adversarial review of a merged design
- `proposals/2026-08-31-unified-code-shape/` — 19 files, 7435 lines — THE IDEAL UNIFIED CODE SHAPE — INDEX — ## Status: **PROPOSED (2026-08-31). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
- `proposals/2026-09-01-shape-tracer-audit/` — 3 files, 736 lines — 00 · THE AUDIT — PR #351's shape tracer — ## Status: **PROPOSED (2026-09-01). HELD BACK IN FULL.** Reference, never mechanism (`CLAUDE.md` §0.05).
- `proposals/2026-09-03-v2-against-the-meta-architecture.md` — 1119 lines — `03-design-v2.md` evaluated against the meta-architecture — ## Status: **EVALUATION. PROPOSED. NOTHING RATIFIES ON MERGE.**
- `proposals/2026-09-18-the-gather/` — 5 files, 657 lines — 00 · THE CENSUS — every tree in `proposals/`, measured — ## Status: **MEASURED (2026-09-18). This file asserts no verdict.** Dispositions are `01`.
- `proposals/2026-10-03-verb-coverage-and-gap-fill.md` — 4663 lines — Verb coverage and gap fill — the 44 verbs of `engine/season/verb_table.yaml`, what they reach, what is missing, and the resolved — ## Status: RATIFIED AS INTENT (v9, ED-IN-0288) — §7 suite and §10.4 scheduled (IN-10..IN-13, IN-18 step 2a, SC-03a/SC-03b); step 9 (`train`)
- `proposals/2026-10-07-grid-mode-suspension.md` — 248 lines — The grid mode's suspension at ENCOUNTER's barrier — ## Status: RATIFIED by Jordan (2026-11-05, in PR #559: "ratify all proposals and merge", ED-IN-0349) · design-only, builds nothing (its buil
- `proposals/2026-10-07-p25-scale-cost.md` — 78 lines — P-25 scale term on Mending Stability — the cost per scale, as the code returns it — ## Status: RATIFIED on merge (ED-1094) — a record of what the code returns, derived by running it
- `proposals/2026-10-07-unplugged-systems-replug.md` — 399 lines — The unplugged systems: what each needs before a composition row can reach it (IN-06, `33`) — ## Status: PROPOSED — the design half of IN-06 (`workplans/valoria_master_workplan_v9_part4.md` §4.5), written at B-C and RE-REVIEWED AT THE
- `proposals/2026-10-14-in48-delegation-carrier.md` — 536 lines — IN-48: the delegation carrier (a seat exercised by someone who does not hold it) — ## Status: PROPOSED (2026-10-14) · HELD: built at `40926a95` and REVERTED because it contradicts ratified Layer 1 (§9) · reference under `CL
- `proposals/2026-10-16-verbs/` — 23 files, 10262 lines —  — 
- `proposals/2026-10-21-verb-key-rows.md` — 346 lines — Verb key rows: every folded name of the uploaded verb list, disposed, and the key rows it needs — ## Status: PROPOSED (2026-10-21). Not ratified; merging ratifies nothing unless Jordan so rules. Static reading. No season, probe or test ra
- `proposals/2026-10-21-verb-key-rows_part2.md` — 540 lines — Verb key rows — part 2: §3.0-§3.1.9, the key rows (continued in `_part3`) — ## Status: PROPOSED (2026-10-21). Not ratified; merging ratifies nothing unless Jordan so rules. Static reading. No season, probe or test ra
- `proposals/2026-10-21-verb-key-rows_part3.md` — 320 lines — Verb key rows — part 3: §3.1.10-§3.2 key rows, §4 why no per-row value fan, §5 host rows, §6 cost and ordering, §7 open items — ## Status: PROPOSED (2026-10-21). Not ratified; merging ratifies nothing unless Jordan so rules. Static reading. No season, probe or test ra
- `proposals/2026-10-22-system-description/` — 18 files, 11774 lines —  — 
- `proposals/2026-10-23-subsystem-completion/` — 12 files, 4637 lines — Subsystem completion proposals — index, rulings between files, order and asks (T00 · lane IN) — ## Status: PROPOSED. Merging this file ratifies nothing (ED-1094's loud exception); every item, ruling and ask here is held back for Jordan'
- `proposals/2026-10-24-master-workplan-v10/` — 14 files, 2512 lines —  — 
- `proposals/2026-10-25-thrust-layer/` — 103 files, 17298 lines — The thrust layer — a design for `engine/season/` (v2, after one adversarial round) — ## Status: PROPOSED — HELD BACK IN FULL (v2). PARTLY RULED since: the v10 plan folds this design in as `CL-THRUST` (`workplans/valoria_maste
- `proposals/2026-10-28-content-architecture-suite/` — 21 files, 3215 lines — Valoria review suite: index — ## Status: PROPOSED (2026-10-28 session; reconstructed 2026-10-30) — HELD BACK IN FULL. Reference under CLAUDE.md §0.05: not a mechanism; me
- `proposals/2026-11-04-content-parameters-docket/` — 34 files, 12142 lines — Content parameters docket: master — ## Status: PROPOSED (2026-11-04). A collation of the content inputs that code and the active plan call for; reference under CLAUDE.md §0.05,
- `proposals/2026-11-08-design-and-code-critique-report.md` — 115 lines — Design and code critique: categorized findings, adversarial results, suggestions — ## Status: FILED — reference, not canon (CLAUDE.md §0.05). A one-round review record (CLAUDE.md §0): its suggestions are proposals, and none
- `proposals/2026-11-08-sc02-reception-proofs-own-commit-design.md` — 136 lines — SC-02 — where `reception` and `proofs` read under option B: the actor's own ledger, and the bench's public commits (F8) — ## Status: PROPOSED (design-first; builds nothing; ratified on merge by ED-1094's default unless held back)
- `proposals/2026-11-12-subsystem-audit-suite/` — 13 files, 2885 lines — Dossier 00 · THE NINE (engine/season/requirements.yaml) — 
- `proposals/canonical_nomenclature_v1.md` — 342 lines — Canonical Nomenclature — namespaced identifiers for every named thing — ## Status: PROPOSED — not ratified. Nothing in this document renames anything.
- `proposals/grounded_event_card_deck_v1.md` — 335 lines — Grounded Event-Card Deck — Breadth Pass Across All Four Research Dockets — ## Status: PROPOSED (2026-07-11) · Lane: IN (cross-cutting; SE, FA) · Author-pass, not yet Jordan-ratified
- `proposals/valoria_fork_plan_of_record_v1.md` — 522 lines — Valoria Fork — Plan of Record — ## Status: PROPOSED (ED-IN-0124, 2026-08-03). Jordan-vetoable throughout.
- `proposals/verb_list.md` — 506 lines —  — 

## research (unclassified; cross-cutting) — 34

- `research/00_INDEX.md` — 304 lines — Research and Precedent Index — game precedent and historical research, keyed for interrogating the subsystems and the plan
- `research/by_lane/00_COMPARATIVE_ANALYSIS.md` — 683 lines — Comparative analysis: how the ten lane evaluations interact
- `research/by_lane/README.md` — 88 lines — Research and precedent by lane — critical evaluation, missing areas and recommendations
- `research/cross_scale_action_catalogue_v1.md` — 919 lines — Valoria — Cross-Scale Action Catalogue (v1)
- `research/game_precedent_suite/README.md` — 40 lines — Game precedent suite
- `research/game_precedent_suite/THROUGHLINES.md` — 178 lines — Throughlines, templates and primitive equivalences across the precedent suite
- `research/game_precedent_suite/dispositions/ATTACHMENTS_CROSSCHECK.md` — 50 lines — Cross-check of four uploaded survey documents against the verified precedent tables and tutorials
- `research/game_precedent_suite/dispositions/D_T02.md` — 115 lines — D_T02 — dispositions against T02 (the season, persons and how an actor chooses; suite file 03)
- `research/game_precedent_suite/dispositions/repo_claims_checked.md` — 174 lines — What the Valoria repo already says about the comparison-set games
- `research/game_precedent_suite/tables/R1_dynasty_realm.md` — 258 lines — R1 - Dynasty / realm games vs Valoria capability checklist (v2, verified 2026-10-22)
- `research/game_precedent_suite/tables/R3b_colony_sims_2.md` — 200 lines — R3b - Colony sims 2: Manor Lords, Frostpunk (1 and 2), Banished  (v2, verified copy)
- `research/game_precedent_suite/tables/R9_policy_court_sims.md` — 197 lines — R9 (v2, verified) - Policy / court sims: Tropico 6, Suzerain, Dragon Age: Inquisition, Democracy 4
- `research/game_precedent_suite/tables/REPO_MENTIONS.md` — 174 lines — What the Valoria repo already says about the comparison-set games
- `research/game_precedent_suite/tutorials/T01_realm.md` — 336 lines — T01 - Realm / dynasty games: how to play (tutorial pass, 2026-10-22)
- `research/game_precedent_suite/tutorials/T02_warband.md` — 285 lines — T02 - Warband-style sandboxes: how to play (v3 tutorial pass, 2026-10-22)
- `research/game_precedent_suite/tutorials/T04_colony_b.md` — 291 lines — T04 - Colony sims B: Manor Lords, Frostpunk, Frostpunk 2, Banished (v3 tutorial pass)
- `research/game_precedent_suite/tutorials/T08_sanity_a.md` — 249 lines — T08 tutorial pass: sanity / stress / voyage games (Darkest Dungeon II, Sunless Sea, Eternal Darkness)
- `research/game_precedent_suite/tutorials/T09_sanity_b.md` — 207 lines — T09 tutorial pass: Don't Starve (+DST), Pathologic 2, Vampire: The Masquerade - Bloodlines
- `research/game_precedent_suite/tutorials/T11_policy_sims.md` — 248 lines — T11 (v3 tutorial pass) - Policy / court sims: Tropico 6, Suzerain, Dragon Age: Inquisition, Democracy 4
- `research/game_precedent_suite/tutorials/T17_repo_strategy_a.md` — 177 lines — T17 repo strategy tutorials A: Europa Universalis IV, Dominions 5 and 6, Heroes of Might and Magic III/V/VII
- `research/game_precedent_suite/tutorials/T18_repo_strategy_b.md` — 283 lines — T18 (v3) - Tutorials: Shadow Empire, Stellaris, XCOM (EU + XCOM 2), Brigandine (Runersia)
- `research/historical/precedents_analysis.md` — 397 lines — VALORIA — Historical Precedent Analysis for Core Dynamics
- `research/valoria_game_precedent_companion_v1.md` — 565 lines — Game Precedent Companion — What Other Games Did, and What Held
- `research/valoria_game_precedent_companion_v1_part2.md` — 325 lines — Game Precedent Companion — Part 2: Comparison, Complements, Synergies
- `research/valoria_game_precedent_companion_v1_part3.md` — 279 lines — Game Precedent Companion — Part 3: Valoria Judged Against the Precedent
- `research/valoria_game_precedent_companion_v1_part4.md` — 317 lines — Game Precedent Companion — Part 4: Reconcile and Unify
- `research/valoria_game_precedent_companion_v1_part5.md` — 245 lines — Game Precedent Companion — Part 5: The Comparative Matrix
- `research/valoria_game_precedent_companion_v1_part6.md` — 264 lines — Game Precedent Companion — Part 6: The Precedent Games, Decomposed in Valoria's Own Slices
- `research/valoria_game_precedent_companion_v1_part7.md` — 199 lines — Game Precedent Companion — Part 7: The Person Across Systems — Stance, Management, Presence
- `research/valoria_game_precedent_companion_v1_part8.md` — 197 lines — Game Precedent Companion — Part 8: The Personnel Precondition (ED-IN-0201)
- `research/valoria_systems_integration_master_v1.md` — 476 lines — Valoria Systems Integration Master — Part 1: Collation and Slices
- `research/valoria_systems_integration_master_v1_part2.md` — 243 lines — Valoria Systems Integration Master — Part 2: Flatten, the Personal Half
- `research/valoria_systems_integration_master_v1_part3.md` — 371 lines — Valoria Systems Integration Master — Part 3: Within-System Analysis
- `research/valoria_systems_integration_master_v1_part4.md` — 744 lines — Valoria Systems Integration Master — Part 4: Cross-Category Comparison and Integration Proposals
