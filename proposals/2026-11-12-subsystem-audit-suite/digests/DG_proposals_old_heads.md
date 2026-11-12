# Digest proposals_old_heads

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

HEADS-ONLY lane (350 files, proposals dated before 2026-09-20). Method per file: first lines of the head, Status line, heading list with line numbers, and a cross-citation check (the filename or directory name searched in `CURRENT.md`, `workplans/`, `engine/`, `modules/`, `tools/`, `references/`, `architecture/`, `registers/handoffs/`, `canon/`, `tests/`). Reading is of the head and heading skeleton only; body claims below are what the head and headings state, not independently re-verified, unless marked. `CURRENT.md` (41 lines) names none of the files in this lane as a live head except by the successor pointers noted in the closing sections. Line references are to the heading or head line in the file.

---

### proposals/2026-07-26-personal-combat-player-agency-and-tradition-curriculum.md
- **What it is:** design proposal, 2026-07-26, lane PC, 972 lines, no ED allocated.
- **Status:** "PROPOSED — DESIGN-ONLY, HELD FOR JORDAN. Nothing here is built, ratified, or scheduled." Reading: historical/unclear; cited only from `HANDOFF_PC_history.md`; `CURRENT.md` names `modules/combat/` as the PC head.
- **Bears on:** PC, CHAR, DICE.
- **Content that matters:**
  - Six player intents on a "Plan layer" (I1 MEASURE, I2 COMMITMENT, I3 GUARD, I4 COUNTER, I5 BIND-OR-BREAK, ...) bound to engine phases (`Approach`, `Exchange`, `Riposte`, `AwaitTempo`) :61-123.
  - Governing decision: where a player acts (tiers T1.., "three rules that make T1 legitimate") :31-47.
  - Premise: measured nine build levers, customization surface "broad and hollow" (findings D1-D8, F23 hollow `eff_cw` channels) :12.
  - Claims to close ED-PC-0001 (player-input surface) and `phase4_5_plan_v1.md` Phase 4b (abilities-as-access) :9.
  - Contains an ability-lever registry (title) and a section-9 precondition list.
- **Conflicts / stale:** Written against `systems/combat/combat_engine_v1/` at `248f344`; the PC head has since moved to `modules/combat/`. [UNVERIFIED] whether any registry in it was built.
- **Open items:** Whether the ability-lever registry and player-intent surface were ever adopted; ED-PC-0001 status.

### proposals/2026-08-15-character-and-faction-stats-and-progression.md
- **What it is:** measured design proposal, 2026-08-15, lane IN, 1677 lines (102 headings), rewritten twice on its day.
- **Status:** "PROPOSED — DESIGN-ONLY, HELD FOR JORDAN ... Every number below was produced by running the engine at HEAD." Reading: historical; cited by workplan v11 parts and `HANDOFF_IN_closed.md`.
- **Bears on:** CHAR, FA, DICE, CORE.
- **Content that matters:**
  - Revision note: draft 1 (Burning-Wheel test-marking) killed on four grounds incl. combat resolving against fixed `DECISIVE_OB = 3` making anti-farm inert :22-27.
  - Attribute parity re-measured (n=600) and Jordan's "+0.1D" continuous-dice probe measured :24, :51.
  - "Are attributes tacked on?" answered by a bottom-up census of what engines consume :77-102.
  - Role question and attribute proposal :131-185; progression on continuous dice (§4, "enabling ruling") :220.
  - Bears on `OPT-AV-1` (attribute roster, Jordan-skipped 2026-07-08) and M1 juncture 6 :21.
- **Conflicts / stale:** Attribute and progression facts since moved to `proposals/2026-09-20-pursuit-basis-worksheet.yaml` (CURRENT.md's character-model head, ED-IN-0261). [UNVERIFIED] which of its rulings survive.
- **Open items:** `OPT-AV-1` roster; §19 promotion criterion (shared with the scores census).

### proposals/2026-08-16-system-scores-census.md
- **What it is:** AST-measured census of every attribute/score by subsystem, 2026-08-16, lane IN, companion to the 08-15 stats proposal.
- **Status:** "MEASURED REFERENCE — not a proposal, not ratified, not canon." Reading: historical snapshot (paths pre-date the `modules/` move).
- **Bears on:** CHAR, PC, SC, MB, FA, SE, FI, WR.
- **Content that matters:**
  - Role legend per score: POOL, BLEND, GATE, CEILING, TRACK, META, STATE, DECLARED :34-37.
  - Per-system sections: PC §1 :15, SC §2 :41, threadwork §3 :61, knots §4 :79, MB §5 :97, factions §6 :119, settlements §7 :136, fieldwork §8 :155.
  - Overlap matrix (§9) and "scores declared but never read" (§10) :161, :180 - the dead-field list.
  - Notes grep frequency was measured to invert the truth :33.
- **Conflicts / stale:** Entity paths (`systems/combat/combat_engine_v1/`, `engine/autoload/game_state.py`) pre-date later moves. Dead-score list not re-verified.
- **Open items:** none stated beyond the §19 promotion criterion in the companion.

### proposals/2026-08-18-breaking-the-recursion.md
- **What it is:** process diagnosis and decision request, 2026-08-18, lane IN, 853 lines.
- **Status:** "PROPOSED — decision requested from Jordan. Terminal by design: executing it deletes it." Reading: historical, executed in effect by the culling plan.
- **Bears on:** PROCESS.
- **Content that matters:**
  - Measures what the repo spends itself on and that the trend accelerates; the "reduction paradox" :56-106.
  - Jordan gave the anti-recursion instruction four times :106.
  - Generative mechanism: what a session sees (T1) vs must produce (T2) :124-159.
  - No ED allocated: the IN ledger had ~108 tokens of headroom under a blocking cap :5.
- **Conflicts / stale:** The CLAUDE.md of today embodies its outcome (§0 request-is-scope). Process only, no game bearing.
- **Open items:** none live.

### proposals/2026-08-18-culling-plan-v1.md
- **What it is:** removal plan in five waves, 2026-08-18, lane IN, ED-IN-0194.
- **Status:** "RATIFIED AS PLAN OF RECORD (Jordan, 2026-08-18) — waves execute individually; section 5 gates are hard." **Flag: Status RATIFIED.** Reading: historical (executed; `.audit/` and `restructure_ledger.md` cite it).
- **Bears on:** PROCESS.
- **Content that matters:**
  - Decision procedure for what to cull (Jordan's rule: recursive guardrails are worthless) :25.
  - Waves: 1 leaves ~45k lines :140; 2 meta-gates :163; 3 wiring-checkers :190; 4 `audit/` to fork ref ~172k lines :212; 5 untrack generated data ~101k :248.
- **Conflicts / stale:** CLAUDE.md now says `.audit/` exists as a hidden surviving corpus; wave 4's end state differs in detail. Return-to-game plan says it is "still RATIFIED, absorbed as Act E".
- **Open items:** none live.

### proposals/2026-08-18-epistemic-propositions-and-provenance.md
- **What it is:** belief-layer design (Proposition, Holding, provenance), 2026-08-18, lane FI, 266 lines.
- **Status:** "DESIGN CALLS RULED 2026-08-18 (§10) ... the DESIGN remains PROPOSED and unbuilt." Reading: ruled intent, unbuilt; partly superseded by the Key retirement.
- **Bears on:** FI, CHAR, WR.
- **Content that matters:**
  - Directive (Jordan): epistemic propositions available alongside provenance references :4 (head).
  - `Proposition` content-addressed :43; `Holding` per-agent belief with provenance :61; provenance and independence make confidence honest :80; truth is separate :97.
  - Home is `npc_memory` (said to already specify this, empty) :114.
  - Defines Key type `state.proposition_revised` :145 - **built on the retired Key substrate.**
  - Five questions ruled; P1 took the population-scale branch.
- **Conflicts / stale:** Key transport (`state.*` key types) is RETIRED (ED-IN-0232): §5 is dead as written; the proposition/holding model may still stand.
- **Open items:** where beliefs live now that keys are gone.

### proposals/2026-08-18-fieldwork-architecture-and-nonadversarial-play.md
- **What it is:** fieldwork/investigation architecture with precedent research, 2026-08-18, lane FI, 1033 lines.
- **Status:** "DESIGN CALLS RULED 2026-08-18 (§13) — the nine §9 questions are answered and ED-FI-0006/0007/0008 are released; the ARCHITECTURE remains PROPOSED and unbuilt." Reading: ruled intent, unbuilt; cited by several workplan v11 parts.
- **Bears on:** FI, CHAR, SC.
- **Content that matters:**
  - "The finding that reorders everything" :18; six precedent problems P1 access, P2 deduction locus, P3 ground truth (no GM), P4 time/attrition, P5 confidently wrong, P6 the record :52-149.
  - Primitive map (compose, never re-implement) :179.
  - Bears on ED-916, ED-FI-0001/0002, godot Gate-0 :4.
  - §13 holds the nine ruled answers.
- **Conflicts / stale:** Pre-dates Key retirement and the proceedings/strife work. Workplan citations show it still feeds FI positions. [UNVERIFIED] which parts.
- **Open items:** architecture unbuilt; check workplan parts for the FI positions that cite it.

### proposals/2026-08-18-next-session-handoff.md
- **What it is:** session handoff, 2026-08-18, lane IN, 304 lines.
- **Status:** "LIVE HANDOFF — read this before CURRENT.md" (self-labelled; long stale). Reading: superseded by `2026-08-20-return-to-game-plan-v1.md` (sequencing) and by later handoffs.
- **Bears on:** PROCESS, GO.
- **Content that matters:**
  - Six unblocked items: compiler in CI :37, five compile defects :58, vendor gdUnit4 :87, add 20 missing Key types :96, close M1 junctures 1-2 :113, replace the SessionStart banner :130.
  - Held-for-Jordan list :144.
- **Conflicts / stale:** Key-type item dead (Key retired); banner item inverted (CLAUDE.md §0.3 forbids a printing banner). "LIVE" label false.
- **Open items:** none.

### proposals/2026-08-18-recursion-interrogation-log.md
- **What it is:** raw evidence log for the breaking-the-recursion proposal, 2026-08-18, 795 lines.
- **Status:** "REFERENCE — raw evidence log ... Delete with it." Reading: historical, should have been deleted with its parent.
- **Bears on:** PROCESS.
- **Content that matters:** CLAUDE.md section budget in chars :50; commit-attention census over whole history :104; tool ratchet measurement :116; Fable-5 resumption contract :20.
- **Conflicts / stale:** Stated death date (same commit as parent) not honoured if the parent still exists.
- **Open items:** none.

### proposals/2026-08-18-ruling-execution-plan.md
- **What it is:** execution plan derived from fifteen rulings of 2026-08-18, lane FI with IN/PC/SC/FA/SE dependencies, 213 lines.
- **Status:** "PLAN — derived from RULED decisions, not itself a design proposal." Reading: historical; superseded by workplan v11.
- **Bears on:** FI, DICE, CORE, PC, SC, FA, SE.
- **Content that matters:**
  - Five blockers (what cannot start and whose call) :11; execution sequence :25.
  - R1 obstacle doctrine, three-class census, ambiguity B3 :50-72; R3 type split :91; R7/R8 edit-site lists :108.
- **Conflicts / stale:** Later 08-23 ruling "TN is always 7" changes R1 premises.
- **Open items:** B3 ambiguity (obstacle reading) as a doctrine question.

### proposals/2026-08-19-obstacle-stat-and-identity-census.md
- **What it is:** 18-agent read-only census, 2026-08-19, 273 lines; 213 obstacle sites.
- **Status:** "FINDINGS — measurement, not design." Reading: historical snapshot.
- **Bears on:** DICE, PC, SC, MB, FA, SE, WR, FI.
- **Content that matters:**
  - Five defects: `tn` accepted but unused by the discrete dice owner (`engine/autoload/dice_engine.py:75-84`) :14; PC scene path an orphan in a real campaign :37; `Faction.intel` dead :53; two opposed-roll sites with opposite mechanics :59.
  - Obstacles organised by circumstance, three divergences :82-99; three readings of B3 :105.
- **Conflicts / stale:** `engine/autoload/` is gone; `fac.intel` is cited in CLAUDE.md §0.05 as an orphaned ruled bound. TN-always-7 ruling (08-23) changes finding 1.
- **Open items:** none stated.

### proposals/2026-08-19-roll-and-resolution-inventory.md  [partial 86%]
- **What it is:** AST-extracted inventory of dice calls and resolution that bypasses `engine/`, 2026-08-19, 231 lines.
- **Status:** "FINDINGS — mechanical inventory, AST-extracted. No design, no rulings." Reading: historical.
- **Bears on:** DICE, MB, PC, SC.
- **Content that matters:**
  - Headline: ladder was single-owned, roller and obstacle never owned; `massbattle.py:627` `roll_pool(n, tn=7, rng)` is a forked roller :10-32.
  - 55 production call sites; 19 TN parameters inert :32, :58.
  - Four subsystems import no engine dice module; six private roll/degree implementations :72, :90; PC resolves by probability gate, not dice :103; raw-RNG total :118.
- **Conflicts / stale:** `systems/mass_battle/sim` Tree A removal was ruled 08-23; counts predate that.
- **Open items:** §4 open rulings.

### proposals/2026-08-19-subsystem-delta-and-narrative-robustness.md
- **What it is:** designed-vs-built delta analysis, 2026-08-19 revised 08-22, 258 lines.
- **Status:** "FINDINGS. Content/design only." Reading: historical; its headline (world population is zero) is the subject of the later greenfield suites.
- **Bears on:** CHAR, WR, CORE, SE, FA, FI.
- **Content that matters:**
  - Headline: in every seeded campaign the population is zero; `generate_npc` has no call site; `world.npcs` empty :12-28. Antagonist upheld that this is a ruled honest deferral (`engine/tests/test_pipeline_reach.py:137-1..`) :28.
  - Three failure modes: orphaned, hollow, starved seam :28-86.
  - Conviction cluster reframed :120; new defects found by antagonists :130.
- **Conflicts / stale:** Whether the population is still zero must be checked in `engine/season/` (not here). Key substrate framing retired.
- **Open items:** none stated.

### proposals/2026-08-19-subsystem-input-shape-and-narrative-robustness.md
- **What it is:** corrected plan after critic returned UNSOUND, 2026-08-19, 138 lines.
- **Status:** "FINDINGS + CORRECTED PLAN. Content/design only." Reading: historical.
- **Bears on:** CORE, WR, PROCESS.
- **Content that matters:**
  - 15 per-subsystem flow skeletons already exist (IN, OUT, state, seams, gaps), guarded by `tests/valoria/test_flow_skeletons.py` (95 passed) :9-29.
  - Per-subsystem input profile :56; "open half-edges" as the corrected metric :79.
  - Inverse correlation: richer content, thinner runtime :101.
- **Conflicts / stale:** Key substrate no longer the input shape (retired).
- **Open items:** none.

### proposals/2026-08-20-return-to-game-plan-v1.md
- **What it is:** corrected plan of record request, 2026-08-20, lane IN, 490 lines.
- **Status:** "PROPOSED — plan of record requested. Supersedes the sequencing of 2026-08-18-next-session-handoff; does NOT supersede the culling plan." Reading: superseded in sequencing by `2026-08-21-execution-order-v1.md` (its §5) and later by workplan v11; cited by `engine` test `test_engine_does_not_import_sy...`.
- **Bears on:** PROCESS, CORE.
- **Content that matters:**
  - Binding premise RULED by Jordan 2026-08-20: "`systems/` should stem from `engine/` and `references/`" :22.
  - Audits established: recursion, guardrails where wrong change passes every gate, premise not yet true :56-93.
  - Corrected model of what is left :105; the plan :116.
- **Conflicts / stale:** The `systems/` stem-from-`engine/` premise is the origin of the engine-names-no-subsystem rule in CLAUDE.md §3.
- **Open items:** none live.

### proposals/2026-08-21-execution-order-v1.md
- **What it is:** step-by-step execution ordering (S1..), 2026-08-21, lane IN, 1155 lines.
- **Status:** "PROPOSED — merging this PR RATIFIES the step ordering (ED-1094) ... Two items are HELD." Reading: ratified on merge by its own terms [UNVERIFIED]; steps S1-S4 `state: done`; historical.
- **Bears on:** PROCESS, CORE.
- **Content that matters:**
  - THE BOARD current as of 2026-08-22 :21; ordering thesis :90; target state :136; steps :160 onward (S1 load-bearing claim, S2 culling waves 1+2, S3 wave 3, S4 wave 5).
  - Supersedes §5 of the 08-20 plan only :8.
  - Cited by `test_engine_params_bridge.py` and two handoff history files.
- **Conflicts / stale:** Tree has since changed enormously; the board is stale.
- **Open items:** the HELD items (unnamed in head read).

### proposals/2026-08-22-session-master-log-fieldwork-to-delta.md
- **What it is:** reconciliation and index over nine session documents, 2026-08-22, 566 lines.
- **Status:** "RECORD — reconciliation and index ... Findings, not design." Reading: historical.
- **Bears on:** FI, CHAR, WR, PROCESS.
- **Content that matters:** Trust order of surfaces (§2 > delta §8 > delta body > docs 1-6) :14; reconciliation ledger incl. "broken by verification" and "corrections owed to other surfaces, still unexecuted" :44-92; falsifier record :101; the surviving pattern, "two families and a control" :146-165.
- **Conflicts / stale:** the 08-23 suite 07 supersedes parts.
- **Open items:** §2.3 corrections owed to other surfaces.

### proposals/2026-08-22-wiring-map.md
- **What it is:** connection map, coded vs designed, 2026-08-22, 475 lines.
- **Status:** "FINDINGS — a connection map, not a work plan." Reading: historical snapshot.
- **Bears on:** CORE, CHAR, SC, WR, SE, FA.
- **Content that matters:** Five status terms CODED / CODED-BUT-UNREACHED / (three more) :21-30; two headline corrections of the delta (loader claim FALSE; "enrich the call site" half false) :21-62; A1 registry-to-world loader :64; A2 conviction-taxonomy split :89; A3 `Settlement.npc_ids` writer :110; B1 policies live :135; B2 `world=` to audience resistance blocked :147.
- **Conflicts / stale:** All "unreached" statuses pre-date `engine/season/`.
- **Open items:** none.

### proposals/2026-08-23-MASTER-vocabulary-and-rulings.md
- **What it is:** master index of competing vocabularies, three rulings, Jordan's queue, 2026-08-23, 417 lines.
- **Status:** "FINDINGS + RULING EXECUTION NOTES. Nothing here rules anything new." Reading: historical; supersedes the next two files "for reading purposes".
- **Bears on:** CORE, CHAR, DICE, MB, FA, SE, WR.
- **Content that matters:** Three rulings (Jordan): Mass Battle Tree A is deprecated and must be removed; TN is always 7 (threadwork too); all pools live in one document :104; queue of what waits on Jordan :23; person texture :32, place and polity :44, outcomes/events/scale :62, voice :74, machinery :82, structural causes :94.
- **Conflicts / stale:** Ruling 3 (one pool document) status unverified [UNVERIFIED]; check `engine/` for pool owner.
- **Open items:** the queue in §3.

### proposals/2026-08-23-competing-vocabularies-index.md
- **What it is:** index of conflicts/duplications/overlaps (CONFLICT, DUPLICATION, ...), 2026-08-23, 419 lines.
- **Status:** "FINDINGS — an index and analysis." Reading: superseded by MASTER; kept for citations.
- **Bears on:** CORE, CHAR, FA, SE, WR.
- **Content that matters:** Index by domain :24-111; three root causes: no roster primitive anywhere, naming gate enforces one rule, flagship subsystems have no currency row :132-157; convictions - five rosters, one runs :167; M8: 23 of 30 "missing status" warnings are encoding artifacts.
- **Conflicts / stale:** conviction roster later fixed (Suite 07 §2.1).
- **Open items:** none.

### proposals/2026-08-23-rulings-and-adversarial-review.md
- **What it is:** execution notes for the three rulings plus review of prior work, 2026-08-23, 268 lines.
- **Status:** "FINDINGS + RULING EXECUTION NOTES." Reading: superseded by MASTER; historical.
- **Bears on:** MB, DICE, CORE.
- **Content that matters:** Why Tree A removal did not stick (ruling history) :69; coupling is one line :80; blocker reproduced :91; ordering of execution :106; ruling 2 inverts a prior finding.
- **Conflicts / stale:** Suite 07 §2.2 says the port landed.
- **Open items:** none.

### proposals/2026-08-23-suite-00-index.md
- **What it is:** index of the six-document 2026-08-23 session suite, 139 lines.
- **Status:** none stated. Reading: historical entry point; tells reader to read Suite 07 first.
- **Bears on:** PROCESS.
- **Content that matters:** document list :27; most-important findings :44; what needs Jordan :72; what it supersedes (seven working docs) :91; how to trust it :114.
- **Conflicts / stale:** says six documents; Suite 07 added on 08-24.
- **Open items:** none.

### proposals/2026-08-23-suite-01-rulings-and-execution.md
- **What it is:** what the tree does today under the three rulings, 310 lines.
- **Status:** "EXECUTION-READY ANALYSIS." Reading: historical.
- **Bears on:** MB, DICE.
- **Content that matters:** Ruling A (remove Tree A): what depends :25, blocker real and not the adapter's absence :43, five guards fire not one :55, ordering :76; Ruling B (TN 7) true in behaviour false in declaration :99, every non-7 site by AST :121; design questions implied by each ruling :148.
- **Conflicts / stale:** Ruling A port landed (Suite 07).
- **Open items:** design questions implied but unanswered (§2.3).

### proposals/2026-08-23-suite-02-narrative-texture-census.md
- **What it is:** census of geography, factions, settlements, NPCs, 447 lines.
- **Status:** "INFORMATION-ONLY."
- **Bears on:** WR, CHAR, SE, FA.
- **Content that matters:** two mirror holes in world geography :32; 46 authored characters, 0 instantiated :92; convictions roster in code is the superseded one :135; Resonant Style: four voices, eighteen characters :182; where people live :209.
- **Conflicts / stale:** conviction roster fixed per Suite 07.
- **Open items:** none.

### proposals/2026-08-23-suite-03-competing-vocabularies.md
- **What it is:** adjudicated register of vocabulary conflicts, 379 lines.
- **Status:** "ADJUDICATED REGISTER." About a third of sweep findings overturned and kept in place.
- **Bears on:** CORE, CHAR, DICE, FA.
- **Content that matters:** taxonomy of four kinds :10; master register :32; convictions CONFLICT :59; `'Loyalty'` a fifth name :84; key-type registry NARROWED :123; `graze` SOFTENED then SHARPENED :153; scale vocabulary :176.
- **Conflicts / stale:** Key registry findings obsolete.
- **Open items:** none.

### proposals/2026-08-23-suite-04-wiring-gaps-and-orphans.md
- **What it is:** wiring analysis, 262 lines.
- **Status:** "WIRING ANALYSIS."
- **Bears on:** CORE, FA, SE, WR.
- **Content that matters:** person layer is the root :23; sixteen design gaps :64; Treaty system wholly inert :97; Mandate penalty permanent though stated temporary :126; settlement memory layer zero callers :142; `state.succession` three layers deep :154; chronicle chain :175; emission :204; needs Jordan :226.
- **Conflicts / stale:** Treaty/Mandate claims pre-date `engine/season/`; re-verify before use.
- **Open items:** §6.

### proposals/2026-08-23-suite-05-precedent-and-proposals.md
- **What it is:** precedent comparison plus eight proposals, 180 lines.
- **Status:** "COMPARATIVE ANALYSIS + PROPOSALS (unratified)." Evidence tags DOCUMENTED / REPORTED / INFERRED.
- **Bears on:** WR, CHAR, FI.
- **Content that matters:** Caves of Qud history generation :34; Prom Week / Comme il Faut negative lesson :43; Talk of the Town belief and fallibility :55; narrative sifting :64; storylets :75; the null band :83; eight proposals :92; disagreement worth preserving :125; what Valoria does not need :145. External precedent is tier 3.
- **Conflicts / stale:** none noted.
- **Open items:** eight proposals unratified.

### proposals/2026-08-23-suite-06-method-corrections-and-queue.md
- **What it is:** process record: method, retraction record, queue, 238 lines.
- **Status:** "PROCESS RECORD."
- **Bears on:** PROCESS.
- **Content that matters:** four-stage method :13; the one repeating error class :44; falsifier record: overturned :94, narrowed :117, inverted by ruling :126, correction to a correction :132; queue by age :159-177.
- **Conflicts / stale:** none.
- **Open items:** queue.

### proposals/2026-08-24-completion-plan-v1.md
- **What it is:** completion plans for cull, centralization, doc-vs-code conflicts, 2026-08-24, 309 lines.
- **Status:** "PROPOSED (Jordan-requested, 2026-08-24). Ratifies on merge." Reading: historical; cited in handoff history only.
- **Bears on:** PROCESS, CORE.
- **Content that matters:** what the relay killed (refuted plans) :15; Part I corrections to plan of record :35, sequence :63, Churn decision :90, stopping rule :104; Part II centralization headline :132; includes refuted claim "a hold marker in code outranks any ledger status".
- **Conflicts / stale:** executed or overtaken.
- **Open items:** none live.

### proposals/2026-08-24-error-regions-v1.md
- **What it is:** executable plan from the hub-and-bus session, five error regions, 527 lines.
- **Status:** "PROPOSED (Jordan-requested, 2026-08-24)." Self-declared "executed and deleted".
- **Bears on:** PROCESS, PC, CORE.
- **Content that matters:** R1 discriminators that do not discriminate :23 (e.g. `ED-PC-0016` ratified while `weapons.py:911` ...); R2 assertions that cannot observe failure :65 (source of CLAUDE.md §0.1 pt 2); R3 circular or synthetic numbers :101; R4 claims of novelty or enforcement that do not exist :125; R5 inventing canon while appearing to implement :161.
- **Conflicts / stale:** Items likely closed.
- **Open items:** whether all plan items closed; the file says delete if so.

### proposals/2026-08-24-suite-07-reconciliation-against-main.md
- **What it is:** reconciliation after rebase onto `origin/main` at `dcf38ef`, 278 lines.
- **Status:** "RECONCILIATION RECORD."
- **Bears on:** PROCESS, CHAR, MB.
- **Content that matters:** two findings now historical (conviction roster FIXED :43; Ruling A port LANDED :75); three frame-changing rulings (§0.05 :108, needs_jordan :131, markdown may not be swept :161); what still stands :176.
- **Conflicts / stale:** Reading order: read this before Suites 00-06.
- **Open items:** none.

### proposals/2026-08-25-throughlines-and-precedent/00_index.md
- **What it is:** index of a five-chapter cross-scale analysis (throughlines + shipped-game precedent), 2026-08-25, lane IN, no ED; directory has 10 files.
- **Status:** "PROPOSED — analysis and recommendation only. Nothing is ratified by merging it." Reading: historical analysis; the directory is cited by `ners_audit_2026-10-14.md` and `restructure_ledger.md`.
- **Bears on:** CHAR, CORE, DICE, FA, SE, WR, PC, MB, SC.
- **Content that matters:**
  - States itself reference not mechanism (§0.05) :13; corpus actually read :28; method is part of the finding (adversarial independence) :42-59.
  - Population count answerable from 35 authored `status: canonical` records of 46 (11 `proposed`; loading those would be fabrication).
  - Chapters: 1 world has no people; 2 ladder runs both ways; 3 one resolver/four scales/one scalar; 4 VSG weights bias noise chooses; 5 what we should not do.
- **Conflicts / stale:** HEAD `571ae14` locators are stale.
- **Open items:** see 02 register.

### proposals/2026-08-25-throughlines-and-precedent/01_verified_defects.md
- one line: findings verified at `571ae14` with falsifiers: D1 `T16` missing from the settlement adjacency graph :8; D2 retracted and re-adjudicated twice :31; D3 `hidden_allegiance` computed then dropped :57; D4 the empty world is a guarded invariant not an oversight :69; D5 `npc_registry.yaml` 46 officeholders (35 canonical) :82. Status "findings, verified 2026-08-25." Historical; re-verify against `engine/season/`. Tags SE, CHAR, FA, CORE.

### proposals/2026-08-25-throughlines-and-precedent/02_ruled_but_unexecuted.md
- one line: register of rulings with "state of the tree" and locator (table :1-14), "why this register is the most actionable artifact" :15, honest counter-note :31. Status "register, verified 2026-08-25". Historical; items since executed or superseded unknown [UNVERIFIED]. Tags CORE, PROCESS.

### proposals/2026-08-25-throughlines-and-precedent/03_method_and_corrections.md
- one line: process record; CORRECTION 1 the `Standing` retraction (three Standings) :12-58, plus 45 headings of further corrections. Status "process record". Historical. Tags PROCESS, FA.

### proposals/2026-08-25-throughlines-and-precedent/04_ch1_the_world_has_no_people.md
- one line: claim that the world has no people :13; what is built :39; the core narrowed to seven rows, two classes :62; why it is a pathology not a schedule :114; composition measured :171; NERS verdicts :238. No Status line. Precursor of the greenfield population work. Tags CHAR, WR, CORE.

### proposals/2026-08-25-throughlines-and-precedent/05_ch2_the_ladder_runs_both_ways.md
- one line: three Standings and the correction this chapter owns :47; real defect sharper than "unclamped" :73; are there officer objects :106; the cast is data and the data has a defect :131; what an officer must BE :156. No Status line. Tags FA, CHAR.

### proposals/2026-08-25-throughlines-and-precedent/06_ch3_one_resolver_four_scales_one_scalar.md
- one line: what is right first :36; first operand `net` ignores TN, defect verified and measured :88-116; three corrections to how it was reported :146. Pre-dates TN-always-7 ruling; `degree_from_net` is now the code owner. Tags DICE, PC, MB, SC.

### proposals/2026-08-25-throughlines-and-precedent/07_ch4_weights_bias_noise_chooses.md
- one line: VSG (Vectorized Slice Generator) reified from how Goldenfurt was hand-authored; verdict before evidence :7; method as algorithm (kernel/data/wrapper :23, SEED :35, CONDITIONED SLICES :45, NOISE :63). Relevant to generative NPC/world work and to "WE DO NOT DO DETERMINISTIC". Tags CHAR, WR, SE.

### proposals/2026-08-25-throughlines-and-precedent/08_ch5_what_we_should_not_do.md
- one line: precedent failures clustered into five shapes; legibility vs depth axes :18; guard table :46; both seam failure directions in tree :68; vanishing band audit (Blades) run on Valoria :112; do not build the second resolver :163; T-07 counter-force that never fires :193. Tags DICE, CORE, WR.

### proposals/2026-08-25-throughlines-and-precedent/09_adversarial_pass.md
- one line: corrections to chapters 2-4 (Ch3 corrections :16, what survived :78). "process record". Tags PROCESS.

### proposals/2026-08-28-greenfield-systems-suite/00_INDEX.md
- **What it is:** index of the v1 greenfield systems suite (hierarchy and compliance contract), 2026-08-28, lane IN, 12 files.
- **Status:** banner "ARCHIVED / SUPERSEDED (2026-08-29) ... pre-critique ... do not build from it. Six of its claims are known false"; Status line "PROPOSED (2026-08-28) ... ratifies nothing". Reading: SUPERSEDED by `2026-08-29-greenfield-systems-suite-v2/`.
- **Bears on:** CORE, CHAR, FA, SE, WR, MB, PC, SC.
- **Content that matters:** reads `research/valoria_systems_integration_master_v1*`, precedent companion, `cross_scale_action_catalogue_v1.md` :11-13; definition of what the suite is and is not :24.
- **Conflicts / stale:** uses the Key/emit substrate (retired).
- **Open items:** none.

### proposals/2026-08-28-greenfield-systems-suite/01_substrate_primitives.md
- one line: v1 substrate: P-1 Entity (kinds person :38, edge :72); capability reads the registry :61. ARCHIVED banner; Key-era; dead. Tags CORE, CHAR.
### proposals/2026-08-28-greenfield-systems-suite/02_character_generation.md
- one line: v1 character generation; four stages :37; `cg.demand` demand-driven generation :49. ARCHIVED. Tags CHAR.
### proposals/2026-08-28-greenfield-systems-suite/03_world_population.md
- one line: v1 world population; the rule :15, world-gen: exactly the people the gate requires plus a candidate pool :36, the bound stated arithmetically :60. ARCHIVED. Tags CHAR, WR.
### proposals/2026-08-28-greenfield-systems-suite/04_personnel_management.md
- one line: v1 personnel; `pm.vacancy` is an event not a null check :38; `pm.candidates` gate by class :50. ARCHIVED. Tags CHAR, FA.
### proposals/2026-08-28-greenfield-systems-suite/05_faction_actions.md
- one line: v1 faction actions; executes ED-IN-0201 (Jordan 2026-08-28) :11; C1 gate emits rather than returns silently :15-36; closed gate always recoverable :42. ARCHIVED. Tags FA.
### proposals/2026-08-28-greenfield-systems-suite/06_faction_management.md
- one line: v1 faction as composition not stat bundle :15; four derivations :39; naming question Q-4 unanswered :54. ARCHIVED. Tags FA.
### proposals/2026-08-28-greenfield-systems-suite/07_places_and_settlements.md
- one line: v1 Place object for every map node :15; new `references/tier_registry.yaml` :44; four load-time validations :81. ARCHIVED. Tags SE. [UNVERIFIED] whether `tier_registry.yaml` exists.
### proposals/2026-08-28-greenfield-systems-suite/08_settlement_management.md
- one line: v1 governor's season, two-stroke loop :35; unsettled-problem warning :15; gate :26. ARCHIVED. Tags SE, FA.
### proposals/2026-08-28-greenfield-systems-suite/09_adjacent_systems.md
- one line: v1 succession and collapse :19 (two paths declared by policy :25, claim contest :38) and three more adjacent systems. ARCHIVED. Tags FA, WR.
### proposals/2026-08-28-greenfield-systems-suite/10_handoff_build_order.md
- one line: v1 build order :42, impact classes :26, controls and what not to do. ARCHIVED. Tags PROCESS.
### proposals/2026-08-28-greenfield-systems-suite/ARCHIVED.md
- one line: Status "SUPERSEDED (2026-08-29) by proposals/2026-08-29-greenfield-systems-suite-v2/"; records what the critique found :16, what survived into v2 :37, an honest note about the audit that passed it :43. Tags PROCESS.

### proposals/2026-08-29-fable5-throughline-critique/00_INDEX.md
- **What it is:** synthesis index of nine read-only Fable-5 throughline critiques (T1-T9), 2026-08-29, lane IN, 6 files.
- **Status:** "FILED (2026-08-29) — analysis, not a proposal. Nothing here ratifies on merge." Reading: historical critique of the v1/v2 greenfield suites; not cited by CURRENT.md or workplan.
- **Bears on:** CORE, CHAR, FA, SE, WR, FI, MB, PC, SC.
- **Content that matters:**
  - The nine throughlines are defined here and are good vocabulary for audits: T1 all actions performed by characters; T2 memories/feelings/beliefs change; T3 fallible memory, bias, multiple perspectives; T4 no one omniscient; T5 granular actions aggregate upward (resentment to revolt); T6 large actions ripple downward; T7 events/clocks/gates are the basis of debate; T8 the world always churns without the player; T9 field investigations first-class :22-34.
  - Severity scale BLOCKER / DEFECT / GAP / NIT (file 01 :5).
  - Explicitly not the 08-25 throughlines corpus :17.
- **Conflicts / stale:** audits the Key-era suites; Key findings obsolete.
- **Open items:** none.

### proposals/2026-08-29-fable5-throughline-critique/01_findings_T1_T3.md
- one line: critic findings for T1 actions by characters (:29), T2 memories/feelings/beliefs (:110), T3 fallibility/perspective (:174 steelman). FILED analysis; historical. Tags CHAR, FI, WR.
### proposals/2026-08-29-fable5-throughline-critique/02_findings_T4_T6.md
- one line: T4 no one omniscient (:28), T5 upward aggregation (:136), T6 downward ripple (:213). Tags CHAR, FA, SE, WR.
### proposals/2026-08-29-fable5-throughline-critique/03_findings_T7_T9.md
- one line: T7 debate and negotiation basis (:29), T8 the world churns (:108), T9 field investigations (:191). Tags SC, WR, FI.
### proposals/2026-08-29-fable5-throughline-critique/04_keying_and_owner_map.md
- one line: consolidated owner map :9, keying register (key types :69, gauges and registry rows :86, registry files and checks :106). Key-based; **keying register is retired material** (ED-IN-0232). Tags CORE.
### proposals/2026-08-29-fable5-throughline-critique/05_independent_verification.md
- one line: method rule (verify by reading, not pattern match) :10; "P0-7 is real, and it is four dead clocks" :42; "`Key.causes` — P0-11 states it backwards" :68. Four-dead-clocks claim worth re-checking against `engine/season/` clocks. Tags WR, CORE.

### proposals/2026-08-29-greenfield-systems-suite-v2/00_INDEX.md
- **What it is:** index, hierarchy and compliance contract of the v2 greenfield systems suite (18 files incl. parts), 2026-08-29, lane IN.
- **Status:** "PROPOSED (2026-08-29) — held back from ratification-on-merge". Supersedes v1. Reading: superseded in turn by `2026-08-29-valoria-from-scratch/` and the 08-31 architecture suites; **cited by workplan v11 `_part4` and `_part6`** (check what those cite).
- **Bears on:** CORE, CHAR, FA, SE, WR, MB, PC, SC, FI.
- **Content that matters:**
  - Elegance criterion (what E in NERS demands) :71; playing-surface budget as the constraint that decides v2's shape :97.
  - The hierarchy :185; four primitives, a form bucket, seven changes :235; rulings the suite executes :281; design principles :347; uniform module contract :374; preconditions :482; registry landings :494; document map :560.
  - Reads `engine/substrate/{descriptors,composition,keys}.py` - `keys` is retired.
- **Conflicts / stale:** Key-based throughout (retired ED-IN-0232). Docs 08, 10 are versioned v3 internally.
- **Open items:** none recorded in head.

### proposals/2026-08-29-greenfield-systems-suite-v2/01_substrate_primitives.md
- one line: four primitives, a form bucket, four write leaves, one herald shape; has an `## Overrides` block :21; `derive_ob` with a commensurability gate (part 2 summary). Key-era. Tags CORE, DICE.
### proposals/2026-08-29-greenfield-systems-suite-v2/01_substrate_primitives_part2.md
- one line: edges and the Knot :17 (prohibition and three rulings :19), disclosure, the herald, contracts and the audit (§§7-13). Key-era. Tags CORE, FI, CHAR.
### proposals/2026-08-29-greenfield-systems-suite-v2/02_character_generation.md
- one line: life paths, caste and heritage, beliefs and flaws; reads `systems/characters/character_generation*` and `conviction_taxonomy_v30.md`. Tags CHAR.
### proposals/2026-08-29-greenfield-systems-suite-v2/02_character_generation_part2.md
- one line: determinism and totality, "the two properties" :14, the surface, contracts and audit. Note: "determinism" here is a generation property; AUDIT_BRIEF's WE DO NOT DO DETERMINISTIC rule should be checked against it. Tags CHAR.
### proposals/2026-08-29-greenfield-systems-suite-v2/03_world_population.md
- one line: who exists, how many, at what stage; reads `settlement_layer_v30.md` and a world-churn audit. Tags CHAR, WR, SE.
### proposals/2026-08-29-greenfield-systems-suite-v2/04_personnel_management.md
- one line: assignment surface (vacancy, candidates, appointment) predecessor of v1 04. Tags CHAR, FA.
### proposals/2026-08-29-greenfield-systems-suite-v2/05_faction_actions.md
- one line: every tier, ethos in the choosing, influence without conquest; per-tier gate, per-post budget, `appeal`, `act.contest_influence`. Tags FA.
### proposals/2026-08-29-greenfield-systems-suite-v2/05_faction_actions_part2.md
- one line: the eight action rows, resolution, contracts and the audit; J-N and J-O junctions. Tags FA.
### proposals/2026-08-29-greenfield-systems-suite-v2/06_faction_management.md
- one line: ethos, divergence, blocs, and being at a tier. Tags FA.
### proposals/2026-08-29-greenfield-systems-suite-v2/06_faction_management_part2.md
- one line: six political compositions, promotion/demotion/rivalry/contested posts :20, "Posture - the one player verb on this page" :49, collapse. Tags FA.
### proposals/2026-08-29-greenfield-systems-suite-v2/07_places_and_settlements.md
- one line: Place identity/form split, growth/decay, presences, strata, terrain; reads mass battle and settlement layer docs. Tags SE, MB.
### proposals/2026-08-29-greenfield-systems-suite-v2/08_settlement_management.md
- one line: "the governor's one decision"; v3 notes: O-5 deletes `sm.act`/`sm.gate`, O-6 deletes the per-place draw, `credence` write-back. Tags SE.
### proposals/2026-08-29-greenfield-systems-suite-v2/09_ambitions_and_arcs.md
- one line: a project is a composition, an arc is a chain you can walk; arc grammar, derived progress, hook grammar, obstruction, tag chains. Reads `political_dynamics_keys_mig*`. Tags WR, CHAR, FA.
### proposals/2026-08-29-greenfield-systems-suite-v2/09_ambitions_and_arcs_part2.md
- one line: latency, player surface, J-N: "the substrate supplies NO cross-se[ale ...]" :18. Tags WR, CORE.
### proposals/2026-08-29-greenfield-systems-suite-v2/10_the_slate_and_salience.md
- one line: the Slate - candidates, truncation, headless resolution (v3: funnel re-derived after O-6 deleted the draw; `informational`; `imminence` producer). Tags WR, SC, SE, FA, CORE.
### proposals/2026-08-29-greenfield-systems-suite-v2/10_the_slate_and_salience_part2.md
- one line: inertia, contracts, property audit; memory fallback CUT, inertia bootstrap fix, stale `pressure` loop, dominance hand-off. Tags WR, CORE.
### proposals/2026-08-29-greenfield-systems-suite-v2/11_world_events.md
- one line: conditioned exogenous pressure, bounded, reachable both ways. Tags WR.
### proposals/2026-08-29-greenfield-systems-suite-v2/12_adjacent_systems.md
- one line: adjacent systems (combat bridge `engine/cross_scale/combat_bridge.py`, import-boundary test `test_engine_does_not_import_systems`). Tags CORE, PC, MB.
### proposals/2026-08-29-greenfield-systems-suite-v2/13_handoff_build_order.md
- one line: finding that reframes the handoff: the causal model is "declared and unemitted" - 46 nodes, 139 edges, 43 of 94 module edges `notional`, 7 of 94 carried by a live-emitter Key type, `wiring_map_check` live 2 of 27 modules, `trace_execution_phases --seed 42 --seasons 40` showing no npc/character/fieldwork/threadwork/combat calls :20-35. Principle "a phase is done when something executes" (§0.2). Dated and Key-era; counts superseded. Tags CORE, PROCESS.

### proposals/2026-08-29-valoria-from-scratch/00_INDEX.md
- **What it is:** master plan index of a from-scratch Valoria design (17 docs), 2026-08-29, lane IN; "all existing work was reference, never ruling".
- **Status:** "PROPOSED (2026-08-29). HELD BACK FROM RATIFICATION-ON-MERGE, IN FULL." Reading: superseded by the 08-31 architecture suites and by `engine/season/`; not cited by CURRENT.md or workplan.
- **Bears on:** CORE, CHAR, FA, SC, MB, SE, WR, FI, DICE, GO.
- **Content that matters:**
  - Built on the nine throughlines and Jordan's containment axiom; explicitly not a repair of the greenfield suite :10-16.
  - States it does not run and no gain is measured :20.
  - Reading order table with ownership: 01 substrate (binding spine, two structures, one actor, three signatures), 02 person, 03 knowledge/telling/investigation ... :25.
- **Conflicts / stale:** three signatures `choose(person, view)->act`, `resolve(act, world)->event`, `witness(person, event)` are a candidate shape to compare with `engine/season/` verbs.
- **Open items:** none.

### proposals/2026-08-29-valoria-from-scratch/01_substrate.md
- one line: single idea: one kind of actor (person) and two relations - containment (strict single-parent tree: where you stand and whose jurisdiction your voice falls into) and alignment (unconstrained set-system: who you threw in with); houses, guilds, Church, councils are views :7-11. Tags CORE, CHAR, FA.
### proposals/2026-08-29-valoria-from-scratch/02_the_person.md
- one line: lane PC; the person's six fields turned into marks (:19), capability, stance, ties and Knots, computed needs, cohorts; defers to doc 10 resolver, 07 argument, 04 Thread. Tags CHAR.
### proposals/2026-08-29-valoria-from-scratch/03_knowledge_telling_investigation.md
- one line: lane FI; claims, witnessing, lying, view assembly, corroboration, field investigation; predicate vocabulary CLOSED :48; "standing on a null": no surveyed game ships an NPC acting on knowingly false political information (N-9) nor an expression channel for interior state (N-2). Throughlines T3, T4, T9. Tags FI, CHAR.
### proposals/2026-08-29-valoria-from-scratch/04_hearth_and_community.md
- one line: the two rungs the substrate names but does not build, Hearth :23 and Community; larder §1.2, community roster and `contest` §7-8. Tags SE, CHAR.
### proposals/2026-08-29-valoria-from-scratch/05_up_stroke.md
- one line: petition, aggregation and revolt - everything between one person's unmet need and a duchy changing its terms (T5). Tags FA, SE, WR.
### proposals/2026-08-29-valoria-from-scratch/06_down_stroke.md
- one line: Dispensation object :21, publication as telling with distortion :52, openings (T6); guards against a prior failed opportunity mechanism; owns `PriceTerm`, `LevyTerm`, `BlockadeTerm`. Tags FA, SE.
### proposals/2026-08-29-valoria-from-scratch/07_alignment.md
- one line: a faction is a proposition plus a map from persons to degree of commitment; no tier, size class, scale field or verb; growth and collapse are one `commit(person, faction, delta)`. Answers whether offices+alignment suffice for the Church's four Dicasteries and guild grade ladders. Tags FA.
### proposals/2026-08-29-valoria-from-scratch/08_argument.md
- one line: argument, debate, negotiation; "where I am inventing" :9; what an argument is made of :32; treaty breach owned by doc 06. Tags SC.
### proposals/2026-08-29-valoria-from-scratch/09_churning_world.md
- one line: owns T8, the world tick :29, three fidelities, anti-leverage, the personal-strategic battle seam, latency, compute budget. Tags WR, CORE, MB.
### proposals/2026-08-29-valoria-from-scratch/10_resolution_surface.md
- one line: resolver from scratch: N d10, 1-6 nothing, 7-9 one success, 10 two successes; mean Pool/2; why a pool not DC+mod :13-23; why a resolver is needed (what a GM does unwritten) :9. Compare with `engine/dice_engine/dice_engine.py` (`degree_from_net`). Tags DICE.
### proposals/2026-08-29-valoria-from-scratch/11_code_shape.md
- one line: idealized code shape adjudicated without reading any code; Status "adjudication". Ancestor of the 08-31 code-shape docs. Tags CORE, GO.
### proposals/2026-08-29-valoria-from-scratch/12_coercion_and_force.md
- one line: no coercive apparatus, only armed persons and `will()` evaluated over sets; the Hold is a sum over persons :28; garrison, revolt, siege, war one function. Lane MB with FA/PC seams. Tags MB, FA, PC.
### proposals/2026-08-29-valoria-from-scratch/13_material_life.md
- one line: production, prices, stakes people fight over; composes on larder and `PriceTerm`/`LevyTerm`/`BlockadeTerm`. Tags SE.
### proposals/2026-08-29-valoria-from-scratch/14_office_and_upper_rungs.md
- one line: office as an object, the remit is what an office is :25-38; rungs above settlement; lane GO/IN. Tags FA, GO.
### proposals/2026-08-29-valoria-from-scratch/15_adjudications.md
- one line: challenge register; "A. Challenges that AMENDED the spine" :16 (three of the first seven went against the spine). Tags PROCESS, CORE.
### proposals/2026-08-29-valoria-from-scratch/16_ners_audit.md
- one line: Status FILED; four read-only critics, steelman-first, synthesis retracts two of the orchestrator's own rulings. Tags PROCESS.

### proposals/2026-08-30-fixes/01_the_floor.md
- **What it is:** fix to the from-scratch suite for gap-report D-1 ("the most important defect"), 2026-08-30; directory `2026-08-30-fixes` has 5 files.
- **Status:** "PROPOSED (2026-08-30) — a fix to a design, not a new system." Historical (suite itself superseded).
- **Bears on:** CHAR, CORE, FA.
- **Content that matters:** defect is "not a missing feature"; the rank-3 gate is a second-class gate :17-22; composes on substrate §2-3, person §2.1-2.3, adjudications A-6/A-6b.
- **Conflicts / stale:** targets documents that never ran.
- **Open items:** none.
### proposals/2026-08-30-fixes/02_the_act_economy.md
- one line: reconciles two statements of the act budget (gap D-2, reached independently by three season lanes); three readings with their real arguments :29; coverage exercise already ran the experiment :60. Tags CORE, CHAR.
### proposals/2026-08-30-fixes/03_the_missing_needs.md
- one line: two missing need formulas (D-3, collision S15, with S5 and S20); composes on person §6 and hearth larder. Tags CHAR, SE.
### proposals/2026-08-30-fixes/04_relational_at_settlement.md
- one line: Relational EMPTY at two consecutive rungs (D-4) and a councillor has nowhere to stand (D-5); resolves collision S6, parameterises S18. Tags SE, SC, FA.
### proposals/2026-08-30-fixes/05_the_blocked_cores.md
- one line: Status DISPOSITION - a ruling on nineteen findings; "19 of 55 characters have a BLOCKED CORE; eleven are RICH". Tags CHAR, ARCS.

### proposals/2026-08-30-play-space-coverage/00_PLAN.md
- **What it is:** plan of an instrument that runs ~56 seasons as probes over the from-scratch suite using canon characters; 10 files in directory (plan, roster, machine, six season lanes, matrix, gap report).
- **Status:** "PLAN (2026-08-30) — orchestration, not design." Historical; exercise method has precedent value.
- **Bears on:** CHAR, ARCS, FA, SE, WR, PROCESS.
- **Content that matters:** method seasons-as-probes :16; play-space axes :41; roster assigned by coverage :77.
- **Conflicts / stale:** probes target a suite that did not run; no execution evidence.
- **Open items:** none.
### proposals/2026-08-30-play-space-coverage/01_ROSTER_AND_FINDINGS.md
- one line: canon roster from `references/npc_registry.yaml` (90 ids); FINDING 1 the merged suite borrowed canon names and gave them incompatible lives :10; FINDING 2 the King of Valoria has no stated ... :32. Useful for ARCS lanes. Jordan rulings 2026-08-30: Niflhel is not a faction (loose collective of economic factions) per 06/07 headers. Tags ARCS, CHAR.
### proposals/2026-08-30-play-space-coverage/01_the_machine.md
- one line: Lane 6 skeleton: tick, rungs, degrees, remit; "the negative half is the design" :46; strata inside P5 :68; Table A :96. Tags CORE.
### proposals/2026-08-30-play-space-coverage/02_seasons_crown.md
- one line: Lane 1, THE CROWN HOUSEHOLD, highest status/top of ladder; King Almud Almqvist season :39. Tags ARCS, FA.
### proposals/2026-08-30-play-space-coverage/03_seasons_church.md
- one line: Lane 2, Church of Solmund seasons. Tags ARCS, FA.
### proposals/2026-08-30-play-space-coverage/04_seasons_duchies.md
- one line: Lane 3, the Duchies; "is a Duke's season genuinely ..." lane question :7. Tags ARCS, FA, SE.
### proposals/2026-08-30-play-space-coverage/05_seasons_sword_and_shadow.md
- one line: Lane 4, Grandmaster Lisbeth Ehrenwal full season :39 plus probes. Tags ARCS, MB, PC.
### proposals/2026-08-30-play-space-coverage/06_seasons_without_office.md
- one line: Lane 5 power without office, one full season (Vossen) and nine probes; binding rulings (Jordan 2026-08-30) on Niflhel. Tags ARCS, WR, FA.
### proposals/2026-08-30-play-space-coverage/07_seasons_edges_and_ground.md
- one line: Lane 6 edges and ground; Jordan 2026-08-30 "Niflhel is not a faction" :6; opening state six fields :40. Tags ARCS, SE, WR.
### proposals/2026-08-30-play-space-coverage/08_coverage_matrix.md
- one line: 56 probes, 64 cells, Tables A/B; aggregation only. Tags PROCESS.
### proposals/2026-08-30-play-space-coverage/09_GAP_REPORT.md
- one line: Status ADJUDICATION (Fable 5); headline: RICH 33 (60%), THIN 16, BLOCKED 4 (Jarnstal, Palaiologina, Mertha, Falkenrath), SPLIT 1 (Torsvald), SPECTATOR 1 (Torben); "the design gives people plenty to do and cannot give them what they want"; 19 of 55 characters have a blocked core :10-22; what correlates with bad play :39. A coverage-by-canon-character instrument worth reusing for ARCS lanes. Tags ARCS, CHAR.

### proposals/2026-08-31-authoritative-architecture/00_INDEX.md
- **What it is:** index of an eight-document "authoritative architecture" suite, 2026-08-31.
- **Status:** "PROPOSED (2026-08-31). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE." Reading: superseded by `2026-08-31-ideal*`, `unified-code-shape`, `2026-09-01-holonic-architecture` and finally `architecture/` (Layer 1, ratified ED-IN-0204); not cited by CURRENT.md.
- **Bears on:** CORE, GO, PROCESS.
- **Content that matters:** self-declares reference not mechanism, "almost none of this runs" :3-5; why the suite exists :16; the eight documents :34; the architecture on one page :51.
- **Conflicts / stale:** Key-substrate as Event mechanism (R-1) retired.
- **Open items:** none.
### proposals/2026-08-31-authoritative-architecture/01_THE_ARCHITECTURE.md
- one line: primitive set: four carriers Person(id, weight, marks, capability, stance, ledger, ties), Rung, Office, Site; "a cohort IS a Person at weight > 1"; `Rung` chosen over Node/Container :33-48. Tags CORE, CHAR, SE, FA.
### proposals/2026-08-31-authoritative-architecture/02_THE_LOOP.md
- one line: "the season, nested in the tick that already runs"; three-phase tick runs and is pinned by tests, the six steps do not; CALENDAR barrier 1 :54, MATTER barrier 2 :63. Tags CORE.
### proposals/2026-08-31-authoritative-architecture/03_CODE_SHAPE_GODOT_4_6.md
- one line: targeting Godot 4.6, "the version, handled honestly" :9 with evidence for both sides :15. **CLAUDE.md now says the engine version is ruled by ED-GO-0002; this doc asserts none-binding.** Tags GO.
### proposals/2026-08-31-authoritative-architecture/04_THE_REGISTER.md
- one line: §1 describes the key substrate as it existed (code that executed then - now retired); key namespace :61, naming rule made mechanical :68, ED-IN-0200 discharged :86. Dead. Tags CORE.
### proposals/2026-08-31-authoritative-architecture/05_COVERAGE_AND_SUPERSESSION.md
- one line: measured coverage :8; supersession map of the design line #337 to #344 :44-63. Tags PROCESS.
### proposals/2026-08-31-authoritative-architecture/06_ADJUDICATIONS.md
- one line: twelve session rulings R-1..R-12 (not Jordan's): R-1 Key = Event mechanism, not Claim/witness/Query; R-2 six-step loop refines three-phase tick; R-3 `Site.condition` primary state; R-4 Faction row deleted, faction = Proposition + `commit` edges; R-8 fixed-point integers for condition/stores; R-10 degree ladder four bands not five; R-11 `mint`/`efface` kept; R-12 ED-IN-0200 discharged by spec :14-148. R-1 dead; R-10 compare with `degree_from_net`. Tags CORE, DICE, FA, SE.
### proposals/2026-08-31-authoritative-architecture/07_EXECUTION_PATH.md
- one line: "every step ends in something running"; where we are :9, Jordan's ruling that orders everything :30, the path :50. Tags PROCESS, CORE.
### proposals/2026-08-31-authoritative-architecture/08_PROVENANCE.md
- one line: Status reference; method, evidence base, findings by independent rediscovery :60, what the method could not see :77. Tags PROCESS.

### proposals/2026-08-31-ideal-v2/00_INDEX.md
- **What it is:** index of "The Idealized System v2" (four docs: architecture, season loop, compendium, Godot implementability), 2026-08-31.
- **Status:** "PROPOSED (2026-08-31). NOTHING HERE HAS EXECUTED." Reading: superseded by `architecture/` (Layer 1) and the running `engine/season/`; cited by workplan v11 `_part6`.
- **Bears on:** CORE, FA, SE, CHAR, GO.
- **Content that matters:**
  - Seven forks all answered: D-2 act economy ruled "one act per person or cohort, universally" (an office's throughput is its establishment's acts); F1 `Office.conferral` names the basis per office; F2 `Stores := map[MatterKind -> quantity]`; F3 rootless vacancy dissolves (conferral rule may name the office's own judging set); F4 Coherence-0 is de-individuation, not a fork; F5 off-board polities are an EVENT SOURCE not a simulated realm (large deletion); F6 RULED BY JORDAN "neither - the world is in flux": "If the world is not tended to by anyone, it will die. If it is tended to by everyone, it will thrive." :87-103.
  - What these documents refuse :104.
- **Conflicts / stale:** Jordan quote on F6 is a design-intent statement useful to WR/SE audits; check if it landed in `engine/season`.
- **Open items:** none in head.
### proposals/2026-08-31-ideal-v2/01_ARCHITECTURE.md
- one line: 2187 lines, 68 headings; citation key and namespace key before anything :30-40; "what this document may not do" :59. Architecture of persons/rungs/offices/sites. Tags CORE.
### proposals/2026-08-31-ideal-v2/02_THE_SEASON_LOOP.md
- one line: four barriers, six steps :96, four write classes :114, parallelism licence :134. Argument about text, no execution. Tags CORE.
### proposals/2026-08-31-ideal-v2/03_COMPENDIUM.md
- one line: cross-referenced register of keys, inputs, outputs, terms; five id families :37; identity register :65; five identity facts :105. Key-era vocabulary. Tags CORE.
### proposals/2026-08-31-ideal-v2/04_GODOT_IMPLEMENTABILITY.md
- one line: the port axis; no `.gd` parsed, no benchmark; Godot version evidence both sides. Superseded by `godot/` and ED-GO-0002. Tags GO.

### proposals/2026-08-31-ideal/00_THE_SHAPE.md
- **What it is:** direct answer to Jordan: the ideal design system and code shape from scratch (PR #343), 2026-08-31, 996 lines.
- **Status:** "DIRECT ANSWER (2026-08-31)". Reading: historical; superseded by `10_SUPERSEDING.md` in the same directory.
- **Bears on:** CORE, FA, SC, CHAR.
- **Content that matters:** notes cross-document contradictions in the 17-doc from-scratch suite (two pool formulas, two practice ranges, three signature spellings) :4; what the exercise established :10; the ideal system :28; what stays because it earned its place :30. "Four enlargements" (watch, convener, transfer act, option removal).
- **Conflicts / stale:** its evidentiary base partly overturned by 03.
- **Open items:** none.
### proposals/2026-08-31-ideal/01_review_b_findings.md
- one line: Fable read-only review; F-6 propagation gap (`:219` ruling), F-2 closure axis. Tags CORE.
### proposals/2026-08-31-ideal/02_review_a_findings.md
- one line: Fable review; contamination sweep null result :8, three overturns :34, S19 containerless cluster vacancy :55, ordering dependency nobody stated :63. Tags CORE, FA.
### proposals/2026-08-31-ideal/03_review_synthesis.md
- one line: verdict "four-enlargement shape survives in kind; evidentiary base does not"; S-1 (four shipped watch instances), S-2, S-3 overturned; section 10 fails its own falsifier on four counts :48. Tags PROCESS.
### proposals/2026-08-31-ideal/04_ners_audit.md
- one line: Status AUDIT, gates the superseding doc; option-removal clears `:219`; dominant option (silent burial) :26; the watch has zero exact shipped instances :50; petition-to-office :91; transfer act strongest N-line :123; section 10 falsifier run :146. Tags FA, SC, CORE.
### proposals/2026-08-31-ideal/10_SUPERSEDING.md
- **What it is:** "Valoria - the Ideal Design, enlarged by what the testing taught", the terminal deliverable of PR #343, 2018 lines, 87 headings.
- **Status:** "PROPOSED (2026-08-31). Supersedes PR #342's 17-doc suite and the palimpsest ... Nothing here has executed." Reading: superseded by `architecture/` and `engine/season/`; directory `2026-08-31-ideal` cited by workplan `_part6` and by `engine/season/queries/world_q.py`.
- **Bears on:** CORE, FA, SC, CHAR, SE.
- **Content that matters:**
  - Design on one page: one actor (person); containment (single-parent tree) and alignment (set system, faction = proposition + commitment map); three signatures (`choose` takes no world, `resolve` takes no person, `witness` per-person, consensus broadcast a type error); one resolver, one roll, one obstacle; containers hold stake, judging set, standing dates; offices hold remit and own dates; nobody holds an aggregate; knowledge lives only in ledgers :67-80.
  - Four enlargements = one promotion: standing date as spine; convening condition (§7), petition (§8), lost option (§10), unpaid wage (§11); principle "there is no fallback" (§13) :80-86.
- **Conflicts / stale:** `world_q.py` cites it - check that comment still true.
- **Open items:** none.
### proposals/2026-08-31-ideal/11_challenges_round1.md
- one line: antagonist round 1: 5 FATAL, 12 MAJOR, 6 MINOR; C-1/C-2 the dominance repair does not hold / the dominance defect is itself ... :12-31. Tags CORE, PROCESS.
### proposals/2026-08-31-ideal/12_challenges_round2.md
- one line: round 2: 1 FATAL, 8 MAJOR, 4 MINOR; nine of sixteen are regressions from round 1's own fixes :3; D-1 units error was relocated :27; shipped stochastic yield :42. Tags PROCESS.
### proposals/2026-08-31-ideal/20_FABLE5_ADVERSARIAL_REVIEW.md
- one line: adversarial review of PR #343's terminal deliverable, 1824 lines; verdict in one page :136, central finding :138, trajectory test :278, where the design is a direct hit :330. Tags PROCESS, CORE.

### proposals/2026-08-31-integration/00_REVIEW_BRIEF.md
- **What it is:** index entry of the 2026-08-31 integration relay directory (14 files: briefs 00-00d, reviews 01-03, integration proposals 04-05, antagonists 06-07, reconciliations 08/12, ledger 09, judgment 10, integrated doc 11), reconciling "body (a) NPC matrix/season machine" and "body (b) arcs" into the PR #342 suite.
- **Status:** "BRIEF (2026-08-31)". Reading: historical process record; the directory is not cited by CURRENT.md/workplan.
- **Bears on:** CHAR, ARCS, CORE, PROCESS.
- **Content that matters:** code-shape surface RESOLVED BY JORDAN :13; four axes :27; discipline :50.
- **Conflicts / stale:** sources suites are Key-era / unexecuted.
- **Open items:** none.
### proposals/2026-08-31-integration/00b_pessimistic_ners.md
- one line: Rule 1 E is a ratio against N and R never a fourth axis; Rule 2 S is T5/T6 restated; Rule 3 R binds at seats a player can occupy; five rules making the pass pessimistic :4-29. Compare skills/ners. Tags PROCESS.
### proposals/2026-08-31-integration/00c_relay_discipline.md
- one line: relay not dialogue; independence structural not declared; model tiering; antagonist's precise purpose :4-36. Precursor of CLAUDE.md §10 relay text. Tags PROCESS.
### proposals/2026-08-31-integration/00d_findings_digest.md
- one line: consolidated findings digest for (a) NPC matrix/season machine :5 and (b) arcs (`2026-08-30-arc-reach...` directory, not in this lane) :60. Tags ARCS, CHAR.
### proposals/2026-08-31-integration/01_review_b_arcs.md
- one line: verdict SOUND-WITH-CORRECTIONS for the arcs body. Tags ARCS.
### proposals/2026-08-31-integration/02_review_a_npc_matrix.md
- one line: NPC matrix SOUND-WITH-CORRECTIONS; F1 OVERTURN "eleven of the nineteen [blocked cores are RICH]" :6, F2 OVERTURN "the single most common result" :15. Tags CHAR, ARCS.
### proposals/2026-08-31-integration/03_corrected_findings.md
- one line: Status "BINDING INPUT for Part 2"; struck claims: S-1 "eleven of nineteen RICH" (really seven by intersection), S-2 blocked cores "most common result" unsupported (RICH 33/55 vs blocked 19), S-3 "22 convergences from lanes that could not see each other" (about half seeded by shared briefs) :8-26; survivors :27. Evidence that the gap-report headline needed correction. Tags CHAR, ARCS, PROCESS.
### proposals/2026-08-31-integration/04_integration_a_npc_matrix.md
- one line: proposal to change the from-scratch suite with the NPC matrix; verdict by 06 UNSOUND. Tags CHAR.
### proposals/2026-08-31-integration/05_integration_b_arcs.md
- one line: proposal edits to PR #342 for arcs; 07 verdict SOUND-WITH-CORRECTIONS; binds `CODESHAPE_FORBIDDEN.md` (not in this lane). Tags ARCS.
### proposals/2026-08-31-integration/06_antagonist_a_npc_matrix.md
- one line: cold critic (Read/Grep/Glob) verdict UNSOUND on 04. Tags PROCESS.
### proposals/2026-08-31-integration/07_antagonist_b_arcs.md
- one line: cold critic verdict SOUND-WITH-CORRECTIONS on 05. Tags PROCESS.
### proposals/2026-08-31-integration/08_part2_reconciliation.md
- one line: orchestrator adjudication closing Part 2; two lanes returned opposite verdicts :9. Tags PROCESS.
### proposals/2026-08-31-integration/09_citation_ledger.md
- one line: verified fact base by direct read; signatures and rules :15, the world-substrate object :59; "where this ledger and any earlier doc disagree, this ledger wins". Tags CORE.
### proposals/2026-08-31-integration/10_comparative_judgment.md
- one line: read-only top-tier judgment of the two bodies; three defects in the binding inputs :8. Tags PROCESS.
### proposals/2026-08-31-integration/11_INTEGRATED.md
- one line: integrated document answering Jordan's three questions on emergent narrative fit; 634 lines, 39 headings; judged UNSOUND by 12. Tags ARCS, CHAR.
### proposals/2026-08-31-integration/12_PART3_RECONCILIATION.md
- one line: Part 3 closes; D-1 "the floor" STRUCK on direct read: untrained attempt is always legal ("just a small pool", `10_resolution_surface.md:33`) and rank>=3 adds verbs to a list (`02_the_person.md:204`), only rank-5 is a true gate :8-20. So `09_GAP_REPORT` D-1 and `2026-08-30-fixes/01_the_floor.md` rest on a false premise. Tags CHAR, PROCESS.

### proposals/2026-08-31-pr350-archive-recovery/00_FINDINGS.md
- **What it is:** best ideas in the 2026-06-28 archive (tag `v30-snapshot-2026-06-28`) missing from PR #350 (the unified-code-shape suite), 12 lanes + 3 compare lanes, 2026-08-31; directory has 21 files (README, 00-02, evidence/COMPARE_1-3 and LANE_A-L).
- **Status:** "PROPOSED (2026-08-31). HELD BACK IN FULL." Reading: historical; directory cited by `architecture/holonic_ARCHITECTURE.md`.
- **Bears on:** FA, SE, CHAR, WR, ARCS, CORE.
- **Content that matters:** standard applied :17; how produced :39; reading order in README (method :28, reproducing :50, honest state :58).
- **Conflicts / stale:** the archive tag is now where `designs/` and `audit/` live (fork refs).
- **Open items:** none.
### proposals/2026-08-31-pr350-archive-recovery/01_CONVERGENCE.md
- one line: eleven cross-lane convergences: C-1 mandate derived from per-settlement legitimacy and popular support :17; C-2 personal-to-faction seam has a name, a throttle and a known defect :46; C-3 "derive it, don't store it" reached independently :68; C-4 a faction is an aggregate of named people not an agent :85; C-5 corpus's characteristic failure: ruled, then never propagated :103; C-6 feedback loops unbounded then closed with named dampers :120; C-7 world decays from neglect, power vacuum births a faction :142; C-8 scarcity of seats manufactures politics :160; C-9 institutional capture through helpfulness :175; C-10 13-conviction taxonomy and its 4-axis substrate :191; C-11 season shape and action budget, strongest convergence :222. Tags FA, SE, CHAR, WR.
### proposals/2026-08-31-pr350-archive-recovery/02_SCENE_BUDGET_RULING.md
- one line: **JORDAN RULING 2026-08-31: "i expect a character to get ~5 playable scenes per season, which may mean ~5 actions"**; overturns `unified-code-shape/02_ONTOLOGY.md` §8.1 and `07_THE_PLAYER_AND_THE_PERSON.md` §4 ("one act per person or cohort per season, universally"); also contradicts the ideal-v2 fork D-2 ruling; open question flagged :62. Compare against the act budget in `engine/season/`. Tags CORE, CHAR, GO.
### proposals/2026-08-31-pr350-archive-recovery/README.md
- one line: reading order; archive interrogation Jordan-directed. Tags PROCESS.
### proposals/2026-08-31-pr350-archive-recovery/evidence/COMPARE_1_governance.md
- one line: Fable lane 1 compare (governance, factions, settlements): verdict in three sentences :7; missing ranked :13; covered/superseded :71; where PR #350 is affirmatively wrong :96. Tags FA, SE.
### proposals/2026-08-31-pr350-archive-recovery/evidence/COMPARE_2_npc_narrative.md
- one line: Fable lane 2 (NPCs, persons, world churn, emergent narrative): missing :13, covered :64, wrong :85. Tags CHAR, WR.
### proposals/2026-08-31-pr350-archive-recovery/evidence/COMPARE_3_adversarial.md
- one line: Fable lane 3 adversarial cross-cut: missing :17, covered :55, wrong :75. Tags PROCESS.
### proposals/2026-08-31-pr350-archive-recovery/evidence/LANE_A.md
- one line: factions and Mandate (archives/audit); notes a ratified "Jordan ruling (2026-05-30, structural/metaphysical layer)". Tags FA.
### proposals/2026-08-31-pr350-archive-recovery/evidence/LANE_B.md
- one line: world, topography, settlement; notes a directory that is a citation-graph/TF-IDF tool not topography. Tags WR, SE.
### proposals/2026-08-31-pr350-archive-recovery/evidence/LANE_C.md
- one line: architecture, game flow, interdependency. Tags CORE.
### proposals/2026-08-31-pr350-archive-recovery/evidence/LANE_D.md
- one line: NPC modelling, attributes, NERS, investigation. Tags CHAR, FI.
### proposals/2026-08-31-pr350-archive-recovery/evidence/LANE_E.md
- one line: `designs/npcs/` and `designs/personal/` (CANONICAL; matrix provisional pending Stage-10 calibration, 12/14 sim pass). Tags CHAR.
### proposals/2026-08-31-pr350-archive-recovery/evidence/LANE_F.md
- one line: world, territory, settlement; a PROPOSAL of 2026-06-22 extending `settlement_layer_v30 §3.2`. Tags SE.
### proposals/2026-08-31-pr350-archive-recovery/evidence/LANE_G.md
- one line: governance, factions, strategic layer (CANONICAL after Stage-10 sim 12/14; faction_canon_v30 consolidation PROVISIONAL). Tags FA.
### proposals/2026-08-31-pr350-archive-recovery/evidence/LANE_H.md
- one line: political dynamics session and territory audits ("Foundational"). Tags FA, SE.
### proposals/2026-08-31-pr350-archive-recovery/evidence/LANE_I.md
- one line: NPC comprehensive audit and character audits (PROVISIONAL). Tags CHAR.
### proposals/2026-08-31-pr350-archive-recovery/evidence/LANE_J.md
- one line: cross-system syntheses, bridges, throughlines ("WORKING DOCUMENT"). Tags CORE.
### proposals/2026-08-31-pr350-archive-recovery/evidence/LANE_K.md
- one line: emergent narrative, arcs, articulation (self-contradictory status). Tags ARCS, WR.
### proposals/2026-08-31-pr350-archive-recovery/evidence/LANE_L.md
- one line: the scene and the season economy; numbers table (every number found, with citation) :7; "CANONICAL approved 2026-04-17". Tags CORE, CHAR.

### proposals/2026-08-31-shape-tracer/00_README.md
- **What it is:** index of two executed tests of PR #350's idealized code shape (a:NPC, b:ARCS) via a Python tracer, 2026-08-31; directory has 27 files incl. `tracer/` code, `results.json`, `gaps.json`, `workings/`.
- **Status:** "PROPOSED (2026-08-31). HELD BACK. Nothing ratifies on merge." Reading: historical evidence; directory cited by `architecture/holonic_ARCHITECTURE.md`.
- **Bears on:** CORE, CHAR, ARCS.
- **Content that matters:** `04_UNIFIED_SHAPE.md` is the deliverable, rest is evidence :3; the instrument and its own honesty :16, :30.
- **Conflicts / stale:** tracer implements the shape `shape.py`, not the real engine; results do not describe `engine/season/`.
- **Open items:** none.
### proposals/2026-08-31-shape-tracer/01_TEST_A_NPC.md
- one line: the test RAN (`TRACE.txt`, `results_npc.json` not in this lane's list): a season loop for each of 27 named NPCs, copyist to King; result :15, what succeeded :36. Tags CHAR, CORE.
### proposals/2026-08-31-shape-tracer/02_TEST_B_ARCS.md
- one line: 50 arcs from the archived `designs/arcs` extracted and run; headline distribution of how arcs END (a person chooses: 20 etc.) :36; useful number :55. Tags ARCS, CORE.
### proposals/2026-08-31-shape-tracer/03_THROUGHLINES_AND_CHANGES.md
- one line: throughlines of a:NPC :8 and b:ARCS :25 and where the two meet :38, each row produced by execution and naming its probe. Tags CORE, CHAR, ARCS.
### proposals/2026-08-31-shape-tracer/04_UNIFIED_SHAPE.md
- one line: measurement: 27 NPCs - 22 BLOCKED, 4 NOT-ASSESSED, 1 DEGRADED, 0 PLAYABLE; 50 arcs - 38 BLOCKED, 11 NOT-ASSESSED, 1 PLAYABLE; 527 need-rows, 65 probes, 80 acts, 337 class-checked writes; 243 needs UNMAPPED; top blockers `P36` budget, `A4` provenance, `P29` custody, `F6` sittings (NPC), `A2` endings, `P34` hidden tally, `P4` convictions, `A5` spirals (arcs) :18-30; laws L1 person is the only actor, L2 nobody omniscient, L3 every aggregate a function (amended: closed roster) :72, L4 state change partitioned by subject :113, L5 the EDGE LAW (new, "lets stories end") :123. Shape-tracer numbers, not engine numbers. Tags CORE, CHAR, ARCS.
### proposals/2026-08-31-shape-tracer/gaps.json
- one line: gap register: 47 gaps (NO-PRODUCER 29, UNSPECIFIED 11, FORBIDDEN 4, COLLISION 3), 80 acts, 117 events, 337 writes. Data; nothing reads it (one grep: only the sibling docs).
### proposals/2026-08-31-shape-tracer/results.json
- one line: keys `probe_results, need_rows, need_verdicts, case_verdicts, cases, unmapped`; 6489 lines of tracer output. Data, read by nothing.
### proposals/2026-08-31-shape-tracer/tracer/probes.py
- one line: concrete probes of the shape; a probe either completes or raises `ShapeGap`, never works around. Standalone; reads nothing in `engine/`.
### proposals/2026-08-31-shape-tracer/tracer/run_cases.py
- one line: maps each case's shape-neutral `season_requires` need onto a probe. Standalone (same-named `engine/season/harness/run_cases.py` is unrelated).
### proposals/2026-08-31-shape-tracer/tracer/shape.py
- one line: PR #350 shape implemented to run; a tracer not an engine. Dead relative to `engine/season/`.
### proposals/2026-08-31-shape-tracer/tracer/test_tracer_is_honest.py
- one line: adversarial self-test of the tracer (two false PASSes found by hand). A pytest-named file under `proposals/`; not under `tests/` so unlikely CI-collected [UNVERIFIED].
### proposals/2026-08-31-shape-tracer/tracer/trace_log.py
- one line: trace log and gap register writer. Standalone.
### proposals/2026-08-31-shape-tracer/workings/README.md
- one line: Status "WORKING MATERIAL. Not a finding, not a proposal, not reference"; what is deliberately not here :25; naming-lint note :51. Tags PROCESS.
### proposals/2026-08-31-shape-tracer/workings/briefs/FABLE_BRIEF.md
- one line: comparative analysis brief PR #350 vs 2026-06-28 archive; three dispositions :38, five kinds of value :56. Tags PROCESS.
### proposals/2026-08-31-shape-tracer/workings/briefs/LANE_BRIEF.md
- one line: archival scrape brief; five subjects with a hard exclusion :24; output format :52. Tags PROCESS.
### proposals/2026-08-31-shape-tracer/workings/briefs/PR350_DIGEST.md
- one line: orientation digest of PR #350 (merged `647fbdf`); architecture :15, four laws :37, governance/faction/settlement specifics :55, world churn (05) :82. Tags CORE, FA, SE.
### proposals/2026-08-31-shape-tracer/workings/classifier_inputs/ENDINGS.md
- one line: ONE_LINE and ENDS_WHEN for 50 arcs (ARC-01 The Unworked Clause ... ARC-05 The Quiet Fracture ...). A short summary list of the provided arcs. Tags ARCS.
### proposals/2026-08-31-shape-tracer/workings/classifier_inputs/UNMAPPED_CORE.md
- one line: needs that routed to no probe, e.g. ARC-01 players removing a named cost-component from a leader's decision calculus; ARC-04 NPC sustaining deliberate non-commitment toward a subordinate; ARC-05 forcing a stalled private inter-faction calculation into a public formal contest. Tags ARCS, FA, SC.
### proposals/2026-08-31-shape-tracer/workings/extraction/arc_lane1_cases.yaml
- one line: arc cases ARC-01.. with `one_line`, `ends_when`, `season_requires`; data. Tags ARCS.
### proposals/2026-08-31-shape-tracer/workings/extraction/arc_lane2_final.yaml
- one line: second arc lane (ARC-R16 "The World Without Direction" etc.); data. Tags ARCS.
### proposals/2026-08-31-shape-tracer/workings/extraction/build_yaml.py
- one line: helper `SR(need, why, hardness)`; builds yaml. Dead.
### proposals/2026-08-31-shape-tracer/workings/extraction/extract.py
- one line: hard-coded `/tmp/claude-0/.../78360267-.../tasks` session paths; cannot run elsewhere. Dead.
### proposals/2026-08-31-shape-tracer/workings/extraction/extract2.py
- one line: same, `/tmp` session paths. Dead.
### proposals/2026-08-31-shape-tracer/workings/extraction/lane2_output.yaml
- one line: NPC cases (NPC-004 Saemund Haelgrund, Church Field Inquisitor with unrecognised Thread perception ...). Data. Tags CHAR.
### proposals/2026-08-31-shape-tracer/workings/extraction/output.yaml
- one line: NPC cases (NPC-088 Carin Vedel, a copyist hand-reproducing suppressed Einhir texts ...). Data. Tags CHAR.
### proposals/2026-08-31-shape-tracer/workings/prbody.md
- one line: PR body: HELD BACK IN FULL; five findings that changed the proposal :29; what the unified proposal does :54; two adversarial audits :74; five instrument defects that flatter :91; a corpus finding :106. Tags PROCESS.

### proposals/2026-08-31-throughlines.md
- **What it is:** ten throughlines drawn from an adversarial review of PR #342/#343 and the rebuild that followed, 2026-08-31, 866 lines, 27 headings.
- **Status:** "PROPOSED (2026-08-31). ... Nothing in this session executed." Reading: historical reference; unclear whether superseded by the same-day `unified-code-shape` suite.
- **Bears on:** CORE, FA, SC, WR.
- **Content that matters:** self-declares no execution :4-7; ten throughlines distinct from the nine in the fable5 critique and the 08-25 chapters.
- **Conflicts / stale:** three overlapping throughline sets (08-25, 08-29 T1-T9, 08-31 ten) with no reconciliation seen.
- **Open items:** none.

### proposals/2026-08-31-unified-code-shape/00_INDEX.md
- **What it is:** index of PR #350's "Ideal Unified Code Shape" (17 numbered docs + ADVERSARIAL + TRACE_REGISTER), 2026-08-31, layered L0..L5.
- **Status:** "PROPOSED (2026-08-31). HELD BACK IN FULL." Reading: superseded by `architecture/` (Layer 1) and the running `engine/season/`; its comment citations remain in some `engine/season` files? (grep shows `proposals/2026-09-17...` cited, not this dir). Directory-level citations: `2026-08-31-unified-code-shape` found by name only in ledgers.
- **Bears on:** CORE, CHAR, FA, SC, MB, PC, WR, GO.
- **Content that matters:** six shaping rulings :68-90: (1) event log is the Event mechanism, not the Claim/witness/Query mechanism; (2) six steps refine the running three-phase tick; (3) a `Belief` is about MORALS not veracity (Jordan) - what a person holds true is a `Claim`, what they hold right is a Belief backed by Convictions; WITNESS never touches a Belief; (4) a Proposition of mood OUGHT is an uttered Belief, so a faction is somebody's morals said aloud that others signed; (5) degree ladder is four bands, corpus's five-band table overturned; (6) the world's trajectory is an OUTPUT (`wear` against tending) and the world-substrate hole closes as a `Site` kind.
  - Architecture on one page :18; reading order holistic to granular :50.
- **Conflicts / stale:** "degree ladder four bands" vs `degree_from_net` in code: check. Belief-vs-Claim split bears on conviction/decision-layer design (ED-IN-0251/0261).
- **Open items:** none in head.
### proposals/2026-08-31-unified-code-shape/01_THROUGHLINE.md
- one line: L1 laws; "a person is the unit, everything else is bookkeeping about persons" :38; four laws :66; later rows contradicting a law are defects. Tags CORE.
### proposals/2026-08-31-unified-code-shape/02_ONTOLOGY.md
- one line: L2, every type/field/closed set, 1231 lines, 42 headings; section 5 says exactly which parts run; §8.1 "one act per person or cohort per season, universally" - overturned by Jordan's ~5 scenes ruling (see pr350-archive-recovery/02). Tags CORE, CHAR.
### proposals/2026-08-31-unified-code-shape/03_OWNERSHIP.md
- one line: every value in exactly one row; four owners, one log :9; Faction row deleted :31. Mechanical test "name any value and this says who owns it". Tags CORE, FA.
### proposals/2026-08-31-unified-code-shape/04_THE_SEASON_LOOP.md
- one line: six steps, four barriers, four write classes; nests in the tick that already runs :38; "single most load-bearing document in this suite". Tags CORE.
### proposals/2026-08-31-unified-code-shape/05_WORLD_CHURN.md
- one line: what happens when nobody does anything; `wear` as the world's entropy :34. Tags WR.
### proposals/2026-08-31-unified-code-shape/06_EMERGENT_NARRATIVE.md
- one line: "a story is a provenance chain you can walk"; no narrative engine, quest object, story grammar or authored arc; four mechanisms :44. Tags WR, ARCS.
### proposals/2026-08-31-unified-code-shape/07_THE_PLAYER_AND_THE_PERSON.md
- one line: no player model :9; fidelity is a camera never a formula :29; `choose` is the whole of deliberation :64. §4 act budget overturned by Jordan ruling. Tags CHAR, CORE.
### proposals/2026-08-31-unified-code-shape/08_FUNCTION_SURFACE.md
- one line: every signature; enforcement by parameter list that fails; query catalogue :35. Tags CORE.
### proposals/2026-08-31-unified-code-shape/09_THE_SEAM.md
- one line: how personal combat, social contest, mass battle attach to the loop; says nothing about what happens inside one. Tags PC, SC, MB, CORE.
### proposals/2026-08-31-unified-code-shape/10_GODOT_4_6.md
- one line: the port to Godot 4.6; no `.gd` parsed; version handled honestly :10. Superseded by ED-GO-0002 ruling. Tags GO.
### proposals/2026-08-31-unified-code-shape/11_PARAMS.md
- one line: parameter ledger; proposes no values, grades measured/ruled/assumption; what is already exported :29. Tags CORE, DICE.
### proposals/2026-08-31-unified-code-shape/12_TESTS.md
- one line: structural tests; T1 no decision function can see the world :32; "none has ever been run". Tags CORE.
### proposals/2026-08-31-unified-code-shape/13_EXECUTION.md
- one line: execution path; where we actually are :10. Tags PROCESS.
### proposals/2026-08-31-unified-code-shape/14_NERS.md
- one line: NERS ledger auditing this shape; E as a ratio; N :36. Tags PROCESS.
### proposals/2026-08-31-unified-code-shape/15_ADJUDICATIONS.md
- one line: rulings R-1.. each with a falsifier; "session rulings not Jordan's except quoted". Tags CORE.
### proposals/2026-08-31-unified-code-shape/16_PROVENANCE.md
- one line: method; what the lanes overturned :61. Tags PROCESS.
### proposals/2026-08-31-unified-code-shape/ADVERSARIAL.md
- one line: reference review against HEAD `d080535`; three that matter most :24; status/what was run :46. Tags PROCESS.
### proposals/2026-08-31-unified-code-shape/TRACE_REGISTER.md
- one line: LIVE / BUILT-INERT status of pre-`engine/season` code (`engine/autoload/engine_clock.py`, `season_manager.py`, `systems/overview/sim/season.py`, accounting) at `f59fd0e`; all line numbers stale after the engine moves; historical. Tags CORE.

