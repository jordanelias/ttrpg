# atoms_pending/2026-04-25 — Prioritization Pass (v2)

**Generated:** 2026-04-25
**Atoms analyzed:** 316

## Premise correction

First-pass v1 assumed the 10 masters were redundant copies. They are not. Each is a distinct topical mass-summary covering different sessions, audits, or design areas. Cross-source overlap exists at the *canonical-ID* level (atoms in different masters discussing the same ED/PP/T/M ID), not at the prose level.

## Method

1. **Per-source role classification** — manually identified each master's role and target canon areas from preamble inspection.
2. **Per-atom feature extraction** — canonical ID counts (ED/PP/T/M/RS/TC/CP), numeric-spec density, decision language, provisional/editorial markers, target-path inference from topical keywords.
3. **Cross-source ID clustering** — atoms across ≥2 source masters sharing a canonical ID are likely discussing the same thing from different angles.
4. **Signal scoring** — `signal = 3*IDs + 2*numeric_specs + 5*decision + 4*provisional + min(lines,200)/10 + 3*has_target_path − 18*meta − 10*provenance − 25*skip_target`.
5. **Priority assignment**:
   - **P1**: signal ≥ 20, ≥2 IDs, AND (decision OR provisional OR ≥3 numeric specs).
   - **P2**: signal ≥ 10.
   - **P3**: low/negative signal, meta, or content already in commit history.

## Caveat — interpreting signal scores

Signal score rewards ID density (3 pts per canonical ID). Some P1 atoms are *index-of-decisions* atoms (e.g. `Section 1 — Commit Manifest`, `Section 6 — Editorial Decisions Summary`) that list many EDs without restating their content. These are P1 not because the content is new, but because they are **high-yield verification targets**: every ED listed should already be in `canon/editorial_ledger.yaml`. Treat their P1 status as "check that nothing was dropped" rather than "ingest fresh content."

Atoms that score P1 *and* contain provisional/decision/numeric content are the ones with genuinely new material to consolidate.

## Totals

| | count |
|---|---|
| atoms | 316 |
| P1 (consolidate first) | 15 |
| P2 (consolidate next)  | 68 |
| P3 (last/skip)         | 233 |
| cross-source ID clusters | 26 |

## Per-source roadmap

Sorted by P1 count (highest-yield masters first).

| source | role | atoms | P1 | P2 | P3 | IDs | provisional | decision | top declared target |
|---|---|---|---|---|---|---|---|---|---|
| `master_consolidation.md` | consolidation | 13 | 5 | 4 | 4 | 88 | 0 | 5 | `canon/editorial_ledger.yaml` |
| `VALORIA_SESSION_2026-04-25_MASTER.md` | session_log | 11 | 5 | 4 | 2 | 139 | 0 | 2 | `session_logs/ (most already captured)` |
| `master_document_2026-04-25.md` | mechanical_design | 50 | 2 | 8 | 40 | 16 | 0 | 10 | `designs/provincial/faction_*` |
| `valoria_master_document.md` | mechanical_design | 125 | 1 | 23 | 101 | 80 | 0 | 7 | `designs/` |
| `valoria_master_analysis.md` | audit | 13 | 1 | 4 | 8 | 21 | 0 | 2 | `designs/audit/` |
| `valoria_session_master_2026-04-25.md` | session_log | 5 | 1 | 2 | 2 | 15 | 0 | 2 | `session_logs/ (most already captured)` |
| `valoria_master_consolidation.md` | consolidation | 40 | 0 | 12 | 28 | 20 | 0 | 6 | `canon/editorial_ledger.yaml` |
| `solmund_master_document.md` | editorial_setting | 32 | 0 | 4 | 28 | 0 | 1 | 3 | `designs/world/` |
| `valoria_session_2026_04_25_master_consolidation.md` | session_log | 15 | 0 | 5 | 10 | 8 | 0 | 3 | `canon/patch_register*.yaml (PP-675)` |
| `threadwork_master.md` | mechanical_design | 12 | 0 | 2 | 10 | 1 | 0 | 1 | `designs/threadwork/threadwork_v30.md` |

## Cross-source ID clusters (top 30)

Atoms across ≥2 sources sharing the same canonical ID — strong cross-source consolidation candidates. The atoms in each cluster are talking about the same thing from different angles.

| id | sources | atoms | cluster topic (sampled headers) |
|---|---|---|---|
| **T-36** | 3 | 9 | Section 7 — Throughlines and meta-throug / II.9 Connectivity (Mechanical Throughlin / §8 Open editorial decisions |
| **M-4** | 3 | 9 | Section 7 — Throughlines and meta-throug / Context Window 1 — Session B Core / Section 11 — Outstanding design decision |
| **T-31** | 3 | 8 | Section 7 — Throughlines and meta-throug / §9 Commit ledger / 19.3 Ontological Throughlines (Post-Atom |
| **M-3** | 3 | 7 | Section 7 — Throughlines and meta-throug / Section 11 — Outstanding design decision / Section 8 — Synthesis: Valoria's design  |
| **M-1** | 3 | 7 | Section 7 — Throughlines and meta-throug / Section 8 — Synthesis: Valoria's design  / 4.10 Conviction System Architectural Cen |
| **T-34** | 3 | 6 | Section 7 — Throughlines and meta-throug / 19.4 Meta-Throughlines (Emergent Structu / 19.3 Ontological Throughlines (Post-Atom |
| **PP-675** | 3 | 6 | 14. References / Status / (preamble) |
| **T-32** | 3 | 5 | Section 7 — Throughlines and meta-throug / §3 Throughlines T-31..T-41 / §4 Meta-throughlines М-7..М-11 |
| **T-35** | 3 | 5 | Section 7 — Throughlines and meta-throug / §3 Throughlines T-31..T-41 / §4 Meta-throughlines М-7..М-11 |
| **T-33** | 3 | 4 | Section 7 — Throughlines and meta-throug / 19.3 Ontological Throughlines (Post-Atom / §3 Throughlines T-31..T-41 |
| **T-41** | 2 | 9 | §9 Commit ledger / 19.4 Meta-Throughlines (Emergent Structu / 19.3 Ontological Throughlines (Post-Atom |
| **ED-738** | 2 | 7 | §9 Commit ledger / I. Foundational stance / §11 Methodological notes for continuatio |
| **ED-664** | 2 | 6 | Section 6 — Editorial Decisions Summary / Section 3 — Major New Specs Authored / Section 8 — Historical Research |
| **ED-783** | 2 | 6 | 10. Outstanding Work / 14. References / (preamble) |
| **T-38** | 2 | 5 | §3 Throughlines T-31..T-41 / 19.4 Meta-Throughlines (Emergent Structu / §4 Meta-throughlines М-7..М-11 |
| **T-40** | 2 | 4 | §6 Mechanical specifications / 19.3 Ontological Throughlines (Post-Atom / §3 Throughlines T-31..T-41 |
| **M-5** | 2 | 4 | Section 7 — Throughlines and meta-throug / Section 8 — Synthesis: Valoria's design  / §3 Throughlines T-31..T-41 |
| **M-2** | 2 | 4 | Section 7 — Throughlines and meta-throug / Section 8 — Synthesis: Valoria's design  / Section 12 — Session handoff |
| **ED-665** | 2 | 4 | Section 3 — Major New Specs Authored / Section 6 — Editorial Decisions Summary / 16.4 Belief Revision and Scars |
| **T-37** | 2 | 3 | 19.3 Ontological Throughlines (Post-Atom / §10 Next-stage work / §3 Throughlines T-31..T-41 |
| **PP-508** | 2 | 3 | From simulation review (`simulation_revi / II.2 Open Decisions Requiring Jordan (16 / 7.3 Key Mechanics |
| **T-39** | 2 | 2 | 19.3 Ontological Throughlines (Post-Atom / §3 Throughlines T-31..T-41 |
| **T-09** | 2 | 2 | Context Window 3 — ED-717 + Cleanup / §5 Proposal tier classification |
| **PP-674** | 2 | 2 | §10 Next-stage work / 2.4 Recent canonical strikes |
| **PP-632** | 2 | 2 | From holistic audit (`valoria_holistic_a / 5.7 Knots (PP-632) |
| **ED-663** | 2 | 2 | Phase 0 — Housekeeping (prerequisite, no / 16.4 Belief Revision and Scars |

## P1 — consolidate first

_15 atoms. Sorted by signal descending. These are the highest-density mechanical/decisional content; route to canon registers and design docs first._

| signal | atom_id | source | header | IDs | target |
|---|---|---|---|---|---|
| 145 | `valoria_session_2026-04-25_master__06__section-6-editorial-d` | VALORIA_SESSION_2026-04-25_MAS | Section 6 — Editorial Decisions Summary | ED-661,662,664,665,669,704,705,712,739,740,741,742,743,744,7 | `designs/scene/` |
| 118 | `valoria_session_2026-04-25_master__01__section-1-commit-mani` | VALORIA_SESSION_2026-04-25_MAS | Section 1 — Commit Manifest (chronological) | ED-661,662,664,665,669,704,705,712,739,743,745,748,751,753,7 | `designs/scene/` |
| 96 | `valoria_session_2026-04-25_master__04__section-4-stress-test` | VALORIA_SESSION_2026-04-25_MAS | Section 4 — Stress Tests Run | ED-753,759,760,761,762,763,764,765,766,767,772,773,774,775,7 | `designs/scene/` |
| 91 | `valoria_session_2026-04-25_master__03__section-3-major-new-s` | VALORIA_SESSION_2026-04-25_MAS | Section 3 — Major New Specs Authored | ED-664,665,712,739,760,762,772,773,774,775,776,777,778,779,7 | `designs/scene/` |
| 79 | `master_consolidation__03__3-throughlines-t-31-t-41` | master_consolidation.md | §3 Throughlines T-31..T-41 | T-01,30,31,32,33,34,35,36,37,38,39,40,41, M-3,4,5,6,8,9,10,1 | `references/throughlines_meta.md` |
| 48 | `master_consolidation__06__6-mechanical-specifications` | master_consolidation.md | §6 Mechanical specifications | T-02,36,40 | `designs/threadwork/` |
| 44 | `master_consolidation__10__10-next-stage-work` | master_consolidation.md | §10 Next-stage work | PP-674, T-26,30,31,35,37,38,41, M-9,10,11 | `references/throughlines_meta.md` |
| 39 | `master_consolidation__01__1-conversation-arc` | master_consolidation.md | §1 Conversation arc | ED-738, T-26,27,30,31,41, M-7,8,11 | `designs/threadwork/` |
| 39 | `valoria_master_document__99__19-3-ontological-throughlines-p` | valoria_master_document.md | 19.3 Ontological Throughlines (Post-Atomization, T | T-31,32,33,34,35,36,37,38,39,40,41 | `—` |
| 36 | `valoria_session_2026-04-25_master__02__section-2-p1-resoluti` | VALORIA_SESSION_2026-04-25_MAS | Section 2 — P1 Resolution | ED-739,743,759 | `designs/scene/` |
| 35 | `master_document_2026-04-25__49__8-9-faction-balance-simulati` | master_document_2026-04-25.md | §8.9 Faction-balance simulation work remains valid | PP-540,541 | `designs/provincial/` |
| 29 | `valoria_master_analysis__12__section-12-session-handoff` | valoria_master_analysis.md | Section 12 — Session handoff | M-1,2,4 | `references/throughlines_meta.md` |
| 28 | `master_document_2026-04-25__14__2-2-monte-carlo-simulation-r` | master_document_2026-04-25.md | §2.2 Monte Carlo simulation results | PP-540,541 | `simulations/` |
| 27 | `master_consolidation__05__5-proposal-tier-classification` | master_consolidation.md | §5 Proposal tier classification | T-09,36,41, M-11 | `designs/threadwork/` |
| 27 | `valoria_session_master_2026-04-25__03__context-window-3-ed-7` | valoria_session_master_2026-04 | Context Window 3 — ED-717 + Cleanup | ED-667,717, PP-675, T-08,09,11,21, M-4 | `designs/threadwork/` |

## P2 — consolidate next (top 50 by signal)

| signal | atom_id | header | IDs | target |
|---|---|---|---|---|
| 73 | `master_consolidation__04__4-meta-throughlines-7-11` | §4 Meta-throughlines М-7..М-11 | ED-738, T-26,30,31,32,33,34,35,38,40,41, M-1,2,3,4 | `references/throughlines_meta.m` |
| 42 | `valoria_master_analysis__07__section-7-throughlines-and-meta` | Section 7 — Throughlines and meta-throughlines | T-31,32,33,34,35,36, M-1,2,3,4,5 | `designs/npcs/` |
| 29 | `threadwork_master__03__iii-what-the-player-should-feel` | III. What the player should feel | — | `—` |
| 26 | `valoria_session_2026-04-25_master__09__section-9-open-items-` | Section 9 — Open Items at Session Close | ED-710,711,768,779,783, PP-675 | `canon/editorial_ledger.yaml` |
| 25 | `valoria_master_document__103__ii-2-open-decisions-requiring-` | II.2 Open Decisions Requiring Jordan (16 items) | ED-129,131,295,297, PP-508, TC-01 | `designs/provincial/` |
| 24 | `master_consolidation__02__2-ed-738-ein-sof-gradient-editoria` | §2 ED-738 — Ein Sof gradient editorial | ED-738, T-27,30, M-7,8 | `designs/threadwork/` |
| 21 | `valoria_master_analysis__08__section-8-synthesis-valoria-s-d` | Section 8 — Synthesis: Valoria's design identity | M-1,2,3,4,5 | `designs/threadwork/` |
| 20 | `master_consolidation__07__7-wave-1-workplans` | §7 Wave 1 workplans | ED-738, T-31,41, M-7,11 | `references/throughlines_meta.m` |
| 19 | `master_document_2026-04-25__26__p1-essential-for-modes-to-fe` | P1 — Essential for modes to feel rich | PP-540,541 | `designs/provincial/` |
| 19 | `valoria_master_document__100__19-4-meta-throughlines-emergen` | 19.4 Meta-Throughlines (Emergent Structural Patter | T-34,36,38,41 | `designs/threadwork/` |
| 19 | `valoria_master_document__101__19-5-connectivity-verification` | 19.5 Connectivity Verification | T-32,34,36 | `designs/threadwork/` |
| 19 | `valoria_session_2026_04_25_master_consolidation__10__10-outs` | 10. Outstanding Work | ED-783 | `designs/threadwork/` |
| 18 | `master_document_2026-04-25__33__6-5-framework-propagation-ga` | §6.5 Framework propagation gaps (deferred from pri | ED-706, PP-540,541,664 | `designs/provincial/` |
| 18 | `solmund_master_document__25__22-faction-response-pathways` | 22. Faction Response Pathways | — | `designs/threadwork/` |
| 18 | `valoria_master_document__102__ii-1-stale-references-10-items` | II.1 Stale References (10 items) | ED-694, PP-238,275,294 | `designs/threadwork/` |
| 18 | `valoria_master_document__25__4-6-key-sub-mechanics` | 4.6 Key Sub-Mechanics | PP-255,614,636 | `designs/threadwork/` |
| 18 | `valoria_master_document__58__10-2-domain-echo-the-upward-pip` | 10.2 Domain Echo (The Upward Pipe) | PP-109,329 | `designs/threadwork/` |
| 18 | `valoria_master_document__68__13-2-faction-toolkits-not-alter` | 13.2 Faction Toolkits (NOT Alternate Endpoints) | PP-512 | `—` |
| 18 | `valoria_session_master_2026-04-25__01__context-window-1-sess` | Context Window 1 — Session B Core | T-10, M-4 | `designs/threadwork/` |
| 17 | `master_consolidation__08__8-open-editorial-decisions` | §8 Open editorial decisions | T-36 | `—` |
| 17 | `master_document_2026-04-25__16__2-4-strategic-layer-victory-` | §2.4 Strategic-layer victory shape recommendations | — | `—` |
| 17 | `master_document_2026-04-25__30__6-2-strategic-layer-mechanic` | §6.2 Strategic-layer mechanical gaps | ED-727, PP-540,541 | `simulations/` |
| 17 | `valoria_master_consolidation__13__4-5-rendering-strain-subst` | 4.5 Rendering Strain (Substrate-Posture Cost) | ED-539 | `designs/threadwork/` |
| 17 | `valoria_master_document__13__3-3-weapon-system-3-binary-axes` | 3.3 Weapon System (3 Binary Axes) | ED-129,131 | `simulations/` |
| 17 | `valoria_master_document__85__16-4-belief-revision-and-scars` | 16.4 Belief Revision and Scars | ED-663,665, PP-261 | `designs/threadwork/` |
| 16 | `valoria_master_document__39__6-4-socializing-disposition` | 6.4 Socializing / Disposition | PP-684 | `—` |
| 15 | `solmund_master_document__31__28-implementation-priorities` | 28. Implementation Priorities | — | `—` |
| 15 | `valoria_master_consolidation__18__4-10-conviction-system-arc` | 4.10 Conviction System Architectural Centering | M-1 | `designs/threadwork/` |
| 15 | `valoria_master_consolidation__26__phase-i-foundations-compli` | Phase I — Foundations Compliance Gap Closure | M-1,3 | `designs/threadwork/` |
| 15 | `valoria_master_document__109__ii-8-architecture-weaknesses-m` | II.8 Architecture Weaknesses (Mechanical) | ED-129,694, PP-275 | `designs/threadwork/` |
| 15 | `valoria_master_document__36__6-1-depth-axis-0-5` | 6.1 Depth Axis (0–5) | — | `designs/threadwork/` |
| 15 | `valoria_master_document__83__16-2-named-npc-profiles-12-core` | 16.2 Named NPC Profiles (12 core) | ED-618 | `—` |
| 14 | `master_document_2026-04-25__25__p0-essential-for-mode-3-stra` | P0 — Essential for Mode 3 (Strategy) to function | — | `designs/provincial/` |
| 14 | `valoria_master_consolidation__19__from-rse-critique-valoria-` | From RSE critique (`valoria_rse_critique.md`) | ED-545,547 | `designs/scene/` |
| 14 | `valoria_master_consolidation__24__from-simulation-review-sim` | From simulation review (`simulation_review_2026-04 | PP-508 | `simulations/` |
| 14 | `valoria_master_document__10__2-2-derived-scores` | 2.2 Derived Scores | ED-694, PP-275 | `designs/threadwork/` |
| 14 | `valoria_master_document__16__3-6-actions-14` | 3.6 Actions (14) | PP-238,285,294,634 | `—` |
| 14 | `valoria_session_2026-04-25_master__08__section-8-historical-` | Section 8 — Historical Research | ED-662,664 | `canon/editorial_ledger.yaml` |
| 14 | `valoria_session_2026_04_25_master_consolidation__07__7-philo` | 7. Philosophical Content Established | — | `designs/threadwork/` |
| 13 | `valoria_master_consolidation__11__4-3-literal-rendering-per-` | 4.3 Literal Rendering + Per-Character Visual Filte | M-1 | `designs/threadwork/` |
| 13 | `valoria_master_consolidation__14__4-6-per-faction-thread-ent` | 4.6 Per-Faction Thread Entry Points | — | `designs/threadwork/` |
| 13 | `valoria_master_document__09__2-1-attributes-10-range-1-7` | 2.1 Attributes (10, range 1–7) | ED-694, PP-684 | `designs/threadwork/` |
| 13 | `valoria_session_2026_04_25_master_consolidation__09__9-verif` | 9. Verification Status | ED-783, PP-675 | `canon/editorial_ledger.yaml` |
| 12 | `solmund_master_document__23__20-the-mechanism-rendered-world` | 20. The Mechanism: Rendered-World Change Event (RW | — | `designs/threadwork/` |
| 12 | `threadwork_master__07__vii-architecture-in-implementation-or` | VII. Architecture in implementation order | — | `designs/threadwork/` |
| 12 | `valoria_master_analysis__06__section-6-holistic-system-level` | Section 6 — Holistic system-level | — | `designs/npcs/` |
| 12 | `valoria_master_analysis__11__section-11-outstanding-design-d` | Section 11 — Outstanding design decisions | M-3,4 | `references/throughlines_meta.m` |
| 12 | `valoria_master_consolidation__20__from-holistic-audit-valori` | From holistic audit (`valoria_holistic_audit.md`) | ED-543, PP-632, M-3 | `designs/threadwork/` |
| 12 | `valoria_master_consolidation__29__phase-iv-simulation-comple` | Phase IV — Simulation Completion | ED-539,577 | `simulations/` |
| 12 | `valoria_master_document__110__ii-9-connectivity-mechanical-t` | II.9 Connectivity (Mechanical Throughlines Only) | T-36 | `designs/threadwork/` |
| ... | _(18 more in `_priority_queue.yaml`)_ | | | |

## P3 — last / candidates to skip

_233 atoms. Mostly: session statistics, commit manifests, status snapshots, conversation arcs, methodological notes. Review `_priority_queue.yaml` if needed; in most cases this content is already captured in commit history, session logs, or canon registers._

## Recommended ingestion order

1. **`solmund_master_document.md`** (PROVISIONAL marker) — every atom requires Jordan editorial approval. Hand off as a single block before mechanical work; routes to `designs/world/` and `designs/npcs/`. **Editorial-path → blocks all of solmund's atoms unless Jordan confirms.**
2. **Cross-source ID clusters** — for each top ID cluster, read the atoms across sources, reconcile any drift, and update the existing canon entry (editorial_ledger / patch_register / throughlines_meta). This is the highest-leverage work because it deduplicates implicitly across masters.
3. **`master_document_2026-04-25.md`** + **`threadwork_master.md`** + **`valoria_master_document.md`** — mechanical design content. Route to `designs/`. Heavy P1 traffic per the roadmap.
4. **`master_consolidation.md`** + **`valoria_master_consolidation.md`** + **`valoria_master_analysis.md`** — synthesis/audit material. Use to verify canon registers caught everything; most P1 content here likely already has an editorial_ledger entry.
5. **`VALORIA_SESSION_2026-04-25_MASTER.md`**, **`valoria_session_master_2026-04-25.md`**, **`valoria_session_2026_04_25_master_consolidation.md`** — session logs. Mostly skip; spot-check P1 atoms only for any decision that didn't make it into a register.

## Outputs

- `_priority_queue.yaml` — full per-atom priority queue with rationale.
- `_id_clusters.yaml` — cross-source ID clusters.
- `_source_roadmap.yaml` — per-source distribution and target areas.
- `_prioritization.md` — this document.