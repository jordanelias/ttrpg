# Workplan v2 — Extended Audit (Round 3)
**Generated:** 2026-04-27 · session token `8ca3fffeaca3bb9c`
**Companion to:** v2 workplan + gap addendum + round 2 audit
**Method:** Content sampling across atoms_pending, audit history, register truthfulness, governance layer.

---

## §0 The Reconciliation Problem

The headline of Round 2 was "a workplan already exists" (`designs/workplans/wave1_workplans.md`, 25 KB, 5 proposals). Round 3 reveals that statement understates the situation.

**Three workplans now identified:**

| Workplan | Location | Size | Scope | Authority |
|---|---|---|---|---|
| `designs/audit/valoria_workplan_final.md` | designs/audit/ | **92 KB** | "Comprehensive Workplan (Final) — All 19 review amendments integrated, target Godot 4.3" | 2026-04-18 audit-derived |
| `designs/workplans/wave1_workplans.md` | designs/workplans/ | 25 KB | Five proposal-specific workplans (P1, P3, P9, P10, P21) | Pending editorial approval |
| `valoria_workplan_v2.md` | (mine, /mnt/user-data/outputs) | ~16 KB | Throughline-organized infrastructure-and-validation | Generated 2026-04-26 |

**These workplans were generated independently and not reconciled.** v2 was generated without reading the existing 92 KB workplan_final. workplan_final was generated without reference to wave1_workplans (predates it). wave1 references baseline docs (`gameplay_assessment.md`, `mechanical_implementation_revised.md`, `mechanical_implications_revised.md`, `rigorous_audit_synthesis_s1_s7_v3_1.md`) that workplan_final does not engage with directly.

**The right action is not to produce a fourth workplan.** The right action is reconciliation: read all three, identify what each covers, what each misses, where they conflict, and produce a unified plan that supersedes all three.

This audit will not produce a fourth workplan. It surfaces what reconciliation needs to address.

---

## §1 valoria_workplan_final.md — What It Covers That v2 Doesn't

### G54 · The 5-Lens Inconsistency Detection System

workplan_final §HOW TO USE includes a five-lens inconsistency-sweep protocol the v2 workplan never references:

| Lens | Catches |
|---|---|
| **Propagation Map** | Files changed without downstream propagation. `tools/broken_dependency_checker.py` flags broken refs. Check `[PROP-STALE]` markers. |
| **Session Log** | `open_items` acknowledged but uncommitted. `files_modified` from last session. |
| **Editorial Ledger Summary** | `p0_blocker_ids`, `p1_blocker_ids`, `open_ids`. `external_blockers` for sim_debt. |
| **Coverage Matrix** | Open findings, SIM-DEBT items. Items marked "Open — ED-NNN" not in active ledger = inconsistency. |
| **File Index** | `Propagation-pending` count. Each is uncommitted downstream work. |

**Inconsistency sweep protocol** (run at session start):
1. Bootstrap (registers loaded)
2. Compare editorial ledger open items against coverage matrix open findings — flag mismatches
3. Compare session log open_items against editorial ledger — flag items in one but not the other
4. Run `tools/broken_dependency_checker.py` against propagation_map.md
5. Check file_index_summary.md propagation-pending — each is uncommitted downstream work
6. Check editorial_ledger_summary.yaml — if p1_blocker_count doesn't match active ledger count, summary is stale

**This is the discipline v2's F0 (data reconciliation) gestures at without specifying.** workplan_final operationalizes it.

**Required action:** v2 should adopt the 5-lens protocol verbatim into Sprint 1, or supersede workplan_final's protocol with explicit justification.

### G55 · The Phase 4 Calibration Gate

workplan_final defines a **calibration gate** before any Godot implementation begins. v2 does not have this discipline. The gate's exit criteria are concrete and testable:

| Criterion | Threshold |
|---|---|
| Death spirals | None — no faction enters unrecoverable decline before Season 30 |
| Stasis windows | None — no 10-season window where nothing changes |
| Victory timing | Within Season 60–100 (Year 15–25) |
| Feature coverage | All ~130 features fire at least once across 50 runs (100%) |
| MS crisis arc | Fractured band (39–20) between Season 40–80 |
| NPC arc transitions | ≥4 of 14 named NPCs transition by Season 60 |
| Player impact | Player's faction outperforms AI-only by ≥2 stat points |

**Until calibration report confirms these, no Godot implementation begins.**

This is far stronger than v2's V1 exit criteria ("specs land CANONICAL or fail-flagged"). It demands the *full simulation* satisfies game-feel properties, not just that PROVISIONAL specs pass smoke tests.

**Required action:** v2 must adopt the calibration gate, or replace it with equivalently specific criteria. The current "First Playable Season Loop" (P milestone) is downstream of calibration — not a substitute.

### G56 · The "~130 features" target

workplan_final references "all ~130 features fire at least once across 50 runs." v2 has no equivalent feature inventory or coverage-target metric. This implies workplan_final maintains a feature catalog the v2 workplan does not engage with.

**Required action:** Locate the ~130-feature catalog. Possibly in workplan_final itself; possibly in `coverage_matrix_archive.md` (105 KB).

### G57 · The 14 named NPCs (vs v2's 7)

v2 says "NPC priority trees for 7 named NPCs (Almud, Himlensendt, Baralta, Vaynard, Ehrenwall, Torben, Edeyja)." workplan_final says "14 named NPCs." The 24 character `.tres` files in valoria-game (9 extended + 15 primary) suggest the NPC roster is significantly larger than v2 acknowledges.

**Required action:** Reconcile NPC counts. Determine whether v2's "7 NPCs" is a typo, an MVP subset, or an underspecification.

### G58 · workplan_final's Phase 0 housekeeping items

workplan_final §Phase 0 lists items v2 does not include:

- 0.1 Rebuild editorial_ledger_summary.yaml (v2 has this in F2.10)
- 0.2 Deduplicate ED-663 in active ledger (v2 missing — ED-663 has both an open and resolved entry per workplan_final)
- 0.3–0.7 (truncated in head; full body needed)

**Required action:** Read full workplan_final Phase 0 body. Extract any items absent from v2's F0/F2 buckets.

---

## §2 Register Truthfulness — Critical Finding

### G59 · 11 of 14 active patches show `applied_commit: pending`

**Verified count:**

| State | Count | Patches |
|---|---|---|
| `applied_commit: pending` | **11** | PP-297, PP-664, PP-665, PP-666, PP-667, PP-668, PP-670, PP-671, PP-672, PP-673, PP-674 |
| Real commit SHA | 3 | (others) |

**This includes:**
- **PP-672** — the throughlines framework (2026-04-19)
- **PP-673** — the skeleton→index rename (2026-04-19)
- **PP-674** — the vetting framework + Tier N enforcement (2026-04-19)
- **PP-666** — the PROVISIONAL trio (settlement_adjacency, fractional_province, faction_succession_split) — the heart of V1 validation
- **PP-665** — Maret→Yrsa rename
- **PP-664** — VTM-strike residual cleanup

**Two interpretations:**

**Interpretation A (commits exist; SHAs unrecorded):** Work was applied to files and committed, but the patch register's `applied_commit:` field was never updated with the resulting SHA. Register lies; files are correct.

**Interpretation B (work pending commit):** Files reflect the patch contents, but the changes were never committed to the repo. Local working state diverges from the published `main` branch. The register correctly shows "pending."

**The audit cannot distinguish A from B without access to git history.** But the structural finding is unambiguous: **the patch register is not a reliable source of truth for what has been committed.** The compliance check infrastructure that should enforce SHA recording is the same compliance check that isn't running (G3 from gap addendum).

**Required action — F0.4 (new):** Patch-register truthfulness audit. For each `applied_commit: pending` entry, run a git log against the affected files and either:
- Replace `pending` with the actual commit SHA (if work was committed)
- Reset status to `proposed` (if work was not committed and needs commit)

This is currently **the most important register-integrity item in the project.** A workplan built on a register that lies about commit state is built on sand.

### G60 · The framework itself may be uncommitted

If Interpretation B is correct, then PP-672/673/674 — the framework I've been treating as canonical for the v2 workplan — has not been committed to `main`. The throughlines vetting hierarchy, the skeleton→index rename, and the vetting_gate enforcement may exist only in editorial intent.

This would explain:
- Why bootstrap doesn't run compliance_check (the integration was never committed)
- Why freshness_gate hasn't had its SHA-population pass run (the implementation was never committed)
- Why the workplan and reality diverge so substantially

**If true, this is the project's single largest risk:** months of editorial work ungrounded in committed files.

**Required action:** F0.4 must execute before any other audit/workplan work. If patches are uncommitted, the project is not at the state any workplan assumes.

---

## §3 atoms_pending Reality — A v2 Consolidation Plan Awaits Jordan

### G61 · The atoms_pending pipeline is a structured 4-stage process awaiting authority decision

`references/atoms_pending/2026-04-25/_consolidation_workplan.yaml` reveals:

- **Plan version: v2.** Supersedes v1 (committed e9a1c9c3 — "premise was incorrect; v1 dispersed atoms into canon, v2 assembles atoms into auditable documents").
- **Status: pending Jordan approval — DO NOT execute until plan signed off.**
- **316 atoms across 10 topics.** (Round 2 said 381 files; the 316 is atoms; the remaining ~65 are pipeline metadata/audit/review files.)
- **4 stages:**

| Stage | Goal | Jordan-decision-required | Duration |
|---|---|---|---|
| 1 | Topic decomposition approval | **YES** | 15–30 min |
| 2 | Document assembly (10 consolidated docs) | No | Long |
| 3 | Audit pass per consolidated doc | YES | Medium |
| 4 | Post-audit canon decisions | YES | Variable |

**The v2 workplan's A4 (Solmund T-A..T-E) addresses ONE OUTPUT of stage 2.** The Solmund consolidated doc (`02_solmund_cultural_guide.md`) is one of 10 expected stage-2 outputs. The workplan engages with the Solmund findings without engaging with the pipeline that produced them.

**Required action — A6 (new):** Stage 1 approval — Jordan reviews the 10-topic decomposition. This is currently the gating Authority decision for the entire atoms_pending pipeline. v2's A4 is downstream of this decision.

### G62 · 27 unknown canonical IDs referenced in atoms

Sample audit report (`06_mechanical_review_audit_audit.md`) shows the audit found:

- **8 unknown EDs**: ED-129, ED-131, ED-200, ED-295, ED-297, ED-618, ED-670, ED-694 — referenced in atoms but not in canon
- **18 unknown PPs**: PP-233, PP-238, PP-239, PP-246, PP-251, PP-285, PP-294, PP-402, PP-508, PP-512 (+8 more)
- **1 unknown TC**: TC-01

**27 canonical IDs referenced in atoms that don't exist in the canon.**

Three possible causes:
1. **Stale references** — atoms were generated against an older canon state where these IDs existed; the canon since archived/superseded them
2. **Anticipatory references** — atoms anticipate canonical items that should be created
3. **Fabricated references** — atoms hallucinate canonical IDs that never existed

Cause 1 is benign (atom needs update). Cause 2 is canonical work blocked on Jordan. Cause 3 is a serious content-integrity issue.

**Required action — F2.51:** Cross-reference the 8 unknown EDs against `archives/editorials/` and `canon/editorial_ledger_archive.yaml`. Cross-reference the 18 unknown PPs against `archives/patches/`. Classify each reference per cause 1/2/3.

### G63 · The pipeline has 11 audit reports and 11 reviews

`atoms_pending/2026-04-25/_audit_reports/` (11 files) and `atoms_pending/2026-04-25/_reviews/` (11 files) — sophisticated quality-control infrastructure was built around the atoms pipeline. Programmatic ID-presence + path-reference + drift-detection + targeted content scans. **MANUAL-REVIEW** flagging for substantive-content claims.

This level of infrastructure suggests the atoms pipeline is not casual — it's a serious content-management system with multiple checkpoints. The v2 workplan should treat it as a peer infrastructure layer, not as a bag of pending content.

---

## §4 Audit Tradition — 626 KB of Audit Content Unsurfaced

`designs/audit/` top 10 files by size:

| File | Size | Likely findings |
|---|---|---|
| `comprehensive_system_audit_2026-04-15.md` | 95 KB | Six-axis audit (Coherence/Consistency/Creativity/Elegance/Connectivity/Robustness) of Agency System + Investigation Systems |
| `valoria_workplan_final.md` | 92 KB | The pre-existing workplan (G54-G58) |
| `integration_audit_v1_2026-04-15.md` | 87 KB | Integration audit v1 |
| `integration_audit_v2_2026-04-16.md` | 86 KB | Integration audit v2 (one-day later iteration) |
| `session_master_2026_04_20.md` | 54 KB | Session master — major work session |
| `player_world_bridge_2026-04-16.md` | 46 KB | Player-world bridge (the C5 Player Domain content I flagged as missing!) |
| `throughline_specifications_2026-04-17.md` | 45 KB | Throughline specifications — likely the source for throughlines_complete or throughline_registry |
| `npc_faction_arc_interdependency_2026-04-18.md` | 43 KB | NPC/faction/arc interdependency |
| `valoria_complete_system_audit.md` | 41 KB | Complete system audit |
| `valoria_holistic_audit.md` | 36 KB | Holistic audit |

**Total of top 10: 626 KB of audit content the v2 workplan never engaged with.**

### G64 · `comprehensive_system_audit_2026-04-15.md` (95 KB) head reveals six-axis vocabulary

The audit uses the same vocabulary Jordan defined in project instructions: **Coherence, Consistency, Creativity, Elegance, Connectivity, Robustness.** This is precisely the elegance/smoothness/robustness lens I was asked to apply in Round 1.

The audit's executive summary says:

> Both proposals are architecturally sound and philosophically grounded. The Agency System correctly identifies the core motivation problem and solves it with three interlocking systems whose design quality is high. The Investigation Systems proposal extends the existing fieldwork/NPC architecture without redundancy and produces the most significant advance in the project to date.
>
> **The chief risk in both proposals is not design quality — it is incompleteness at the edges.**
>
> **The chief opportunity is importing more of what the referenced games do *viscerally* well.** Valoria's mechanical architecture is rigorous. What it doesn't yet have is the felt quality of a great investigation or the felt weight of a great consequence.

**This is the experiential-correctness gap I identified in Round 1 (player engagement section), surfaced in the audit two weeks earlier.** The v2 workplan recreates a finding the audit already produced.

### G65 · `player_world_bridge_2026-04-16.md` (46 KB) — likely contains C5 (Player Domain) content

The 46 KB file specifically about "player-world bridge" is presumably the design document for player-side mechanics that the gap addendum identified as missing (G15: Player Character Domain). This audit has likely already specified what the workplan needs.

**Required action — F2.52:** Read player_world_bridge_2026-04-16.md. Extract findings into C5 (Player Domain) bucket.

### G66 · Two integration audits in two days

`integration_audit_v1` (2026-04-15) and `integration_audit_v2` (2026-04-16) — 87 KB and 86 KB respectively, one day apart. v2 is presumably the iterated audit. Their findings should drive editorial ledger entries that may already exist or may have been lost.

**Required action — F2.53:** Diff or merge audit findings. Verify each finding has either (a) been resolved per ledger, (b) is in active ledger, or (c) was lost between audits and not tracked.

### G67 · Throughline specifications (45 KB, 2026-04-17)

`throughline_specifications_2026-04-17.md` predates throughlines_meta.md (PP-672, 2026-04-19) and throughline_registry.md. Likely the input to those documents.

**Required action — F2.54:** Verify the 45 KB throughline specifications doc is fully reflected in throughlines_meta.md / throughlines_complete.md / throughline_registry.md. Any T-### definitions or М-### patterns in the source doc that are missing from the canonical registries are propagation debt.

---

## §5 Earlier Audit Tradition — `tests/audit/aud_tw_001`

### G68 · Earlier threadwork audit (AUD-TW-001, 2026-04-02)

`tests/audit/aud_tw_001_threadwork_audit.md` is the **earlier** threadwork audit (2026-04-02, on threadwork_redesign_v25.md). The 28 P0 blockers in `tests/stress/thread/threadwork_audit_register.md` come from a later audit (2026-04-16). Both exist; both have findings.

Sample findings from AUD-TW-001:

| ID | Severity | Status |
|---|---|---|
| AUD-TW-01 | P2 | Temporal weight mechanically inert for non-POP ops; Ob modifier needed |
| AUD-TW-02 | **P1** | POP + actual d6=6 paradox window has no resolution mechanic; **blocks POP simulation** |
| AUD-TW-03 | P2 | Lock axis attribution ambiguous (three-way tension) |
| AUD-TW-04 | P2 | Coherence/RS independence unconfirmed |
| AUD-TW-05 | **P1** | Rendering Crisis (Coherence 0) resolution procedure missing |

**Two P1 blockers from an audit 24 days before workplan v2 was written. Neither appears in the v2 workplan.** They presumably live in editorial archive or were addressed by subsequent design iteration. But the workplan should verify, not assume.

**Required action — F2.55:** Cross-reference AUD-TW-01 through AUD-TW-05+ findings against current threadwork_v30.md spec and editorial archive. Any unresolved finding promotes to F2.

### G69 · 29 audit files in tests/audit/ — none fully surveyed

The remaining 28 files (after aud_tw_001) presumably contain audits of other systems: combat, debate, fieldwork, mass battle, faction politics, etc. Each could have findings that produced or *should have produced* editorial entries.

**Required action — F2.56:** Audit-tradition inventory across `tests/audit/`. For each file: still relevant? findings tracked? Any orphaned findings to surface?

---

## §6 Governance Layer — Critical Gaps

### G70 · No LICENSE file in either repo

Verified: `ttrpg` and `valoria-game` both have no LICENSE, LICENSE.md, or LICENSE.txt.

**Implications:**
- Default copyright attribution unclear
- Anyone reading the repos has no declared rights — under default copyright, they have *no* rights to copy, distribute, or modify
- Future contributors face legal ambiguity
- If repos are made public, the absence becomes a barrier to community engagement
- For a creative work with potential commercial value, this is also a personal IP-protection gap

**Required action — Governance G-1:** Decide and add LICENSE. Options:
- **Proprietary, all rights reserved** — explicit declaration that the project is closed
- **MIT/Apache 2.0** — permissive open-source
- **CC BY-NC 4.0** — Creative Commons for the design work; separate license for code
- **Custom** — bespoke license for game design + code

This is not a "deferred" item. It is a single 5-minute decision with significant downstream consequence.

### G71 · No README.md in ttrpg

Verified: `ttrpg` has no top-level README. Anyone arriving at the repo has nothing explaining what Valoria is, how the design system works, or how to navigate.

**Required action — Governance G-2:** Author top-level README.md for ttrpg explaining:
- What Valoria is (videogame, target Godot 4.6)
- Two-repo structure (ttrpg = design canon; valoria-game = Godot implementation)
- Project state pointer (link to current workplan, session log, editorial ledger summary)
- Bootstrap process for new sessions
- Key directories overview
- License (per G-1)

### G72 · valoria-game/README.md is 5 lines and stale

Verified content: `# Valoria Game / Godot 4 implementation of the Valoria hybrid TTRPG/board game.`

Two issues:
1. "Hybrid TTRPG/board game" still — confirms F1.7 (README update). The 2026-04-17 videogame-only collapse never reached the README.
2. No setup instructions, no how-to-run, no Godot version requirement, no project state pointer.

**Required action:** F1.7 expanded to author a real README with current project state, Godot version, dependencies, build instructions (when available), pointer to ttrpg design canon.

### G73 · No CONTRIBUTING.md, CODE_OF_CONDUCT.md, .github/templates

The infrastructure for collaborative development is absent. This is fine for solo dev but should be declared as a known-deferred item rather than an oversight.

### G74 · No declared playtesting protocol

Even for solo dev: how does the developer playtest? When? Against what? With what feedback collection? When the First Playable Season Loop (P milestone) is reached, what's the playtest process?

**Required action — Governance G-3:** Declare playtest protocol (or declare-deferred). Minimum: define what "the developer plays the game" looks like at P milestone — what's recorded, what's evaluated, what counts as pass/fail.

---

## §7 atoms_pending master_document content — substantial unincorporated design

Sample filenames from `master_document_2026-04-25/`:

- `04__faction-balance-audit-2026-04-25-md-47kb.md` — 47 KB faction balance audit
- `05__balance-simulation-report-2026-04-25-md-21kb.md` — 21 KB balance sim report
- `06__faction-balance-audit-player-experience-2026-04-25.md` — player-experience faction balance
- `07__leadership-win-proposal-2026-04-25-md-21kb.md` — leadership win proposal (21 KB)
- `08__three-modes-of-fulfilment-2026-04-25-md-39kb.md` — three modes of fulfilment (39 KB)
- `09__sim-balance-py-36kb-monte-carlo-simulator.md` — Monte Carlo sim (36 KB Python source)

### G75 · Faction balance work pending canonization

Two faction balance audits + one balance simulation report + a Monte Carlo simulator (likely Python source preserved as atoms). The v2 workplan's V1 (Sim S2) builds a 40-season smoke test. **A Monte Carlo simulator already exists in atoms_pending.** Whether it can be adapted for V1 or whether it's a different framework is unknown without reading the content.

**Required action — F2.57:** Read `09__sim-balance-py-36kb-monte-carlo-simulator.md`. Determine: integrate into V1 sim build, archive, or supersede.

### G76 · Leadership win proposal + three modes of fulfilment — likely victory-condition design

"Leadership win proposal" and "three modes of fulfilment" suggest design work on victory conditions and arc-completion mechanics. This is V2-territory (8-faction victory, T-20 Two Contests). The workplan's V2 may need this content as input.

**Required action — F2.58:** Read these atoms. Surface any findings as editorial entries. Determine V2 input dependency.

---

## §8 Cross-Cutting Contradictions Across Audits

After three rounds, several contradictions across my audits and the project's existing artifacts:

### G77 · v2 workplan's NPC count vs workplan_final's NPC count

- v2 workplan: "7 named NPCs (Almud, Himlensendt, Baralta, Vaynard, Ehrenwall, Torben, Edeyja)"
- workplan_final: "14 named NPCs"
- valoria-game/resources/instances: 24 character `.tres` files (9 extended + 15 primary)

**The 7-NPC list in v2 is wrong or scoped narrower than acknowledged.** Likely the 7 are major faction-leader NPCs; the 14 are "named" in some sense; the 24 are the full character roster. Without reconciliation, every "NPC priority tree" reference is ambiguous.

### G78 · v2's threadwork P0 count vs project's threadwork audit reality

- v2 workplan F2.7: "28 P0 blockers, ~23 still open" (referencing `threadwork_audit_register.md`)
- AUD-TW-001 (earlier audit): separate finding set with at least 2 P1 issues (POP paradox window, Rendering Crisis procedure)
- workplan_final §Phase 0.6: "P0 triage — may add items to Phase 1"

**Three audit traditions for threadwork. v2 only references one. workplan_final implies a triage layer that consolidates them.** Without consolidation, the actual count of open threadwork issues is unknown.

### G79 · v2's three v30-blockers vs design_registry's three v30-blockers

- v2 A2: factions_ttrpg, campaign_modes, southernmost (each blocks v30 rename)
- design_registry: same three (with `blocker:` field)
- workplan_final: not visible in head — needs full read

These align across registries. **No contradiction.** But the v2 description ("v30 design-doc renames") oversimplifies — the actual blocker is "no design-layer doc exists at all," which is a content-creation problem, not a rename problem.

### G80 · "applied_commit: pending" status vs workplan assumptions

- v2 workplan assumes PP-672/673/674 are committed (the throughlines framework is canonical)
- patch register shows all three as `applied_commit: pending`
- valoria_hooks.py is loaded at bootstrap (so the framework's enforcement code IS in the repo)
- references/throughlines_meta.md exists (the framework doc IS in the repo)

**Files exist; commits may or may not. The register lies about commit state OR the work is uncommitted.** This is the central ambiguity from G59.

---

## §9 Round 3 Consolidated Findings

### Critical (must address before any further workplan work)

| ID | Item | Severity |
|---|---|---|
| **G54-G58** | workplan_final.md (92 KB) exists and supersedes v2 in scope | Reconcile or deprecate v2 |
| **G59-G60** | Patch register may lie: 11 of 14 patches show `applied_commit: pending` | Verify or correct register before any other work |
| **G61** | atoms_pending v2 consolidation plan awaits Jordan stage-1 approval | Authority blocker for 316 atoms / 10 topics |
| **G62** | 27 unknown canonical IDs referenced in atoms (8 EDs, 18 PPs, 1 TC) | Content-integrity risk |
| **G70** | No LICENSE in either repo | Governance gap |

### High (extend F2)

| ID | Item |
|---|---|
| G55 | Adopt Phase 4 calibration gate from workplan_final |
| G56 | Locate ~130-feature catalog |
| G57 | Reconcile NPC counts (7 / 14 / 24) |
| G64 | comprehensive_system_audit_2026-04-15.md (95 KB) — six-axis findings unsurfaced |
| G65 | player_world_bridge_2026-04-16.md (46 KB) — likely C5 source |
| G66 | Two integration audits diff |
| G67 | Throughline specifications doc reflected in registries? |
| G68 | AUD-TW-001 P1 findings status |
| G71 | ttrpg has no top-level README |
| G75 | Monte Carlo simulator in atoms_pending — V1 input? |

### Moderate

| ID | Item |
|---|---|
| G69 | tests/audit/ 29-file inventory |
| G72 | valoria-game/README rewrite |
| G73 | CONTRIBUTING / CODE_OF_CONDUCT declared-deferred |
| G74 | Playtest protocol declaration |
| G76 | Leadership win + three modes of fulfilment atoms |

---

## §10 Recommended Next Action

**Stop producing workplan revisions.** Three workplans now exist (workplan_final, wave1, v2) plus this audit. Each iteration adds findings; none reduces them. The accretion has not converged.

**Sequence:**

1. **Verify register truthfulness (G59-G60).** Run a git history check on the 11 `applied_commit: pending` patches. Either the register lies (set actual SHAs) or the work is uncommitted (revert to `proposed`). This single check determines whether the project is in the state any workplan assumes.

2. **Read workplan_final.md fully.** 92 KB, ~30 KB tokens. One session worth of reading. After this, decide: does workplan_final still hold? Are its phases still the right structure? What has changed that requires updating?

3. **Reconcile the three workplans.** Produce ONE consolidated workplan that:
   - Uses workplan_final's phase structure as backbone
   - Incorporates wave1's proposal-specific decision points (P1 Leap UX, etc.)
   - Adds v2's findings (Meta.gd game_mode, no-CI, F1.1/F1.2 reclassification, throughline framework integration, etc.)
   - Drops items resolved since workplan_final was written
   - Adopts the 5-lens inconsistency protocol
   - Adopts the Phase 4 calibration gate

4. **Stage 1 atoms_pending decision (G61).** Jordan approves topic decomposition. Unblocks 316 atoms.

5. **Governance decisions (G70-G74).** LICENSE, READMEs, playtest protocol. Each is a one-decision item; the value is in declaring rather than building.

Only after these is the project in a state where forward execution makes sense. The current state — three workplans, one possibly-untruthful register, an unaudited 92 KB pre-existing comprehensive plan — is not ready for further iteration on top.

**The audit findings are converging on one structural truth:** the project has substantial work product, well-developed infrastructure, and serious editorial discipline — but its surface area exceeds its consolidation capacity. Every audit reveals more that exists than can be tracked. The right discipline now is *subtraction* — declaring scope, locking authority decisions, and committing register truth — not *addition* of new structures.

This audit should be the last extension. The next action should be reconciliation.
