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

