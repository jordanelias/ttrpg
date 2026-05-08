# Workplan Review — Exhaustive Multi-Perspective Audit
**Reviewed:** 2026-04-26 · session token `8ca3fffeaca3bb9c`
**Subject:** `valoria_workplan_throughline_organized.md`
**Sources cross-referenced:** throughlines_meta.md (skeleton + infill), throughlines_complete.md, throughlines_meta_solmund_appendix.md, design_registry.yaml, canonical_sources.yaml, patch_register_active.yaml, editorial_ledger.yaml, editorial_ledger_summary.yaml, supersession_register.yaml, canonical_sources_notes.md, session_checkpoint.md, session_log_current.md, arc_register.md (index), coverage_matrix.md, conversion_ledger.md, design_sync.md, architecture.md — all from both repos.

---

## I · TOP-DOWN (Framework hierarchy → workplan structure)

**Question:** Does the workplan correctly derive from the N→Ω→Μ→М→Τ→Q→Μ̄ hierarchy? Does each bucket serve its claimed tier?

### 1.1 Bucket derivation — sound but with tier-assignment errors

The five-bucket structure (F/A/V/C/M) is a correct translation of the framework's priority ordering. Items that impair the framework's ability to function belong before items the framework should vet. This is right.

**Error 1: F1.A-02 and F1.B-07 are misclassified as Class E.**

The workplan calls A-02 and B-07 "Class E (architectural)" and "Class E" respectively, but then describes them as Μ-mode violations. This is contradictory. Per §8.1, Class E is "Bug/typo/rename/reorg/register" with the escalation test: "touches mechanics? → escalate to D." Both A-02 and B-07 touch mechanics — they are the mechanics. A-02 controls whether the entire Μ-β layer fires. B-07 controls whether Μ-δ cross-scale consequences propagate. These are Class B at minimum (system extensions that are broken), arguably Class A (the autonomous-agent system and the cross-scale consequence system are each subsystems whose implementation is incomplete). The workplan correctly prioritizes them highest but then gives them the lowest class label.

**Consequence:** If these were submitted as PP entries with `vetting: { class: E }`, the vetting_gate would not require a full vetting block. But their scope demands one. Mislabeling them E means vetting_gate would pass them without N/Ω/Μ/М checks.

**Error 2: D-5 Einhir site-network tier assignment is overclaimed.**

The workplan assigns D-5 as "N + Ω-b." The N question ("what Renaissance analogue?") is correct. But the Ω-b question ("how does engagement transform the player?") is overclaimed — D-5 is a geographical/settlement model, not a personal-transformation mechanic. The Ω-b question applies to the *player's interaction with* Einhir sites (which is threadwork + fieldwork), not to the site-network model itself. The site-network is Μ-δ (cross-scale geography) and М-2 (geography holds pressure). It indirectly serves Ω-b through T-15c (RM substrate-heritage), but that's Τ-tier, not Ω-tier.

**Error 3: campaign_modes blocker overclaims "Ω-d lives here."**

The workplan says campaign_modes "defines the unified videogame mode." But `references/videogame_mode_spec.md` already exists in valoria-game as a design_sync entry (design_sync.md: "READ FIRST. Single-mode extraction reference"). The campaign_modes blocker is about the TTRPG-era campaign_modes doc (compilation/stage12), not the videogame mode spec. Ω-d (non-dominance) lives in the *game's mechanical balance*, not in a document that defines what "campaign mode" means. The blocker's actual impact is narrower than stated: it affects campaign-mode-specific starting conditions and campaign length parameters, not the whole Ω-d apparatus.

### 1.2 Protocol application — structural alignment without vetting

The workplan assigns throughline tags and Μ-tier labels to every item. This is useful for ordering. But it does not *perform* the §8 vetting protocol on any item. For grandfathered items this is correct (pre-PP-672). For the PP-666 trio (post-PP-672), the workplan defers vetting to Sim S2 — also correct, since they're PROVISIONAL pending smoke-test.

But the workplan includes one post-PP-672 item that should have been vetted and wasn't: **A3 Varfell victory paths editorial rewrite.** This is a Class B extension (new victory-path gates replacing VTM-dependent ones). It post-dates PP-672 (2026-04-19). It has no PP number, no `vetting:` block, and the workplan doesn't flag this as a protocol gap. It should.

### 1.3 Tier ownership — correctly observed

The workplan correctly routes N/Ω decisions to Jordan (A1, A2) and marks Claude as protocol-applicant for Q and М. The authority table from §10 is respected. No tier-ownership violation.

---

## II · BOTTOM-UP (Every known outstanding item → workplan placement)

**Question:** Does every outstanding item in both repos have a home in the workplan? What's missing?

### 2.1 Items present and correctly placed

- ED-543, ED-710, ED-711, ED-745–748, ED-768 — all present, correctly placed.
- D-4, D-5, Ministry NPC — present in A1.
- Three v30 blockers (factions_ttrpg, campaign_modes, southernmost) — present in A2.
- VTM/CR strike follow-up — present in A3.
- PP-666 trio — present in V1.
- GAP-T-01 through GAP-T-04 — present in V3.
- DA-01/DA-02/DA-03 — present in C3.
- Church stats — present in F1.
- Solmund T-A..T-E — present in A4.
- RS test disambiguation, TD disambiguation, doc_index_gen regen — present in M.

### 2.2 Items MISSING from workplan

**MISSING-01: GameMode enum strip (P1 action item).**
`conversion_ledger.md` Phase 0 Action Items lists "Strip GameMode enum — Remove `enum GameMode { TTRPG, HYBRID, BOARD }` from Enums.gd. Collapse all mode-branched constants." Status: not done. design_sync.md §Key Architectural Changes confirms: "GameMode enum: STRIP. The videogame has one mode." This is a F1-level item — the engine still has a three-mode enum that contradicts the 2026-04-17 videogame-only collapse. Every Constants.gd branch on GameMode is dead code or a latent bug.

**MISSING-02: videogame_mode_spec.md extraction prerequisite.**
conversion_ledger.md Phase 0 Action Items: "Read videogame_mode_spec.md — This document governs all Phase 1+ extraction decisions." This document determines which rules from every design doc apply to the videogame. It's the filter between "design canon" and "Godot implementation." The workplan treats the two repos as having a sim→Godot pipeline but never mentions the spec that governs what enters that pipeline.

**MISSING-03: rs_budget.md as centralized RS source.**
design_sync.md §Key Architectural Changes: "RS Budget: CENTRALIZE. `references/rs_budget.md` is the single source for all RS drain/restoration values. Meta.gd `run_accounting()` should implement all drain sources." The workplan mentions T-04 (RS Decay) repeatedly but never mentions the rs_budget.md document that canonicalized all RS values. Sim S2 needs this as a source; Godot Phase 6 needs this as the extraction source for Meta.gd.

**MISSING-04: Four Open Provisional Values in Godot codebase.**
conversion_ledger.md §Open Provisional Values:

| Location | Value | Provisional Since |
|---|---|---|
| Constants.gd RS_BASELINE_DECAY | 1 | Phase 0 |
| Meta.gd RS initial value | 100 | Phase 0 |
| CombatLogic health placeholder | 4 | Phase 0 |
| CombatLogic damage formula | placeholder | Phase 0 |

These are Phase-0 provisional values that were supposed to be confirmed in Phase 1. design_sync says Phase 1 extraction is "COMPLETE" — but conversion_ledger.md still lists Phase 1 as "NOT STARTED." Either the values were confirmed and the ledger is stale, or they weren't and the code ships with unverified placeholders. The workplan flags the ledger staleness in the roadmap but doesn't track these four specific values.

**MISSING-05: conversion_ledger Phase 0/1 status contradiction.**
conversion_ledger.md says Phase 0 "IN PROGRESS" and Phase 1 "NOT STARTED."
design_sync.md says "workplan_phases_complete: 0,1,2,3,4,5" and shows Phase 1 extraction table as all ✓.
This is the single most dangerous data-integrity issue in the project because it means one of the two tracking documents is wrong, and both are used as sources-of-truth for different decisions. The workplan mentions this in the roadmap document as "a ledger that still says Phase 0 IN PROGRESS" but the throughline-organized workplan itself doesn't include the fix as an item.

**MISSING-06: 132 threadwork audit findings (28 P0 blockers).**
design_sync.md §New Documents: "`tests/thread_stress/threadwork_audit_register.md` — 132 findings, 28 P0 blockers. Thread horizontal integration gaps." These 28 P0 blockers are NOT in the editorial ledger (they live in a separate test register), NOT in the workplan, and NOT accounted for in V3 (Godot Phase 6). They directly affect GAP-T-01 (ThreadworkSystem co-movement) and any threadwork implementation.

**MISSING-07: test_dice_engine.gd and test_tracker_registry.gd execution.**
conversion_ledger.md Phase 0 Action Items: "Run existing tests — test_dice_engine.gd and test_tracker_registry.gd have never been run." The roadmap includes this (Phase A item 1). The throughline workplan does not. These tests verify the entire F1-layer foundation.

**MISSING-08: PP-652 PROVISIONAL (starting PT values per territory).**
patch_register_active.yaml PP-652: "Starting PT values per territory proposed. T9 Himmelenger 5, T6 Stillhelm 1, T13 Oastad 1, T4/T11/T12 at 2, remainder at 3." Status: provisional. This is a Class C parameter change affecting T-07 (Turmoil, М-1) directly. It's in the patch register but absent from the workplan's V1 scope. Sim S2 needs starting PT values — if it uses PP-652's proposed values without verifying, it bakes in a provisional.

**MISSING-09: hybrid_gaps_v30 propagation debt.**
design_registry.yaml `hybrid_gaps` entry notes: "PROPAGATION-PENDING — 17 hybrid gaps not yet in bg_v05 / stage11." These are post-PP-672 design-doc propagation items that affect Μ-δ (cross-scale) integrity. Not in the workplan.

**MISSING-10: arc_register open editorials ED-401–405.**
canonical_sources_notes.md: "arc_register.md v8 (2026-04-13, PP-575). Vector format. Replaces v7. Open editorials ED-401-405." Five open editorials in the arc register. Not in the editorial ledger active file (presumably archived or pre-ledger). Not in the workplan. These affect T-23 (NPC Arc Emergence, М-5) and T-24 (Convergence as Crisis, М-5).

**MISSING-11: Solmund appendix Appendix B — 9 open editorial items.**
The workplan mentions these in A4 parenthetically ("Plus 9 open editorial items in Appendix B") but does not list them individually, assign classes, or specify which block sim work. Several are mechanical: "SA-gated faction actions — Accept thresholds?" (Class C), "Miraculous Event → Accord +1" (Class C), "Conviction mechanic for Miraculous Event — Accept Cognition vs Ob = Certainty?" (Class B). These need individual tracking because some are Authority-tier and some are not.

**MISSING-12: DA-01 as F1-level rather than C3.**
DA-01 (save/load registration order enforcement) is classified in C3 (Construction — post-V). But if save/load currently corrupts game state by loading in wrong order, this is a F1-level engine integrity failure, not a post-validation construction task. Need to verify whether the current code actually crashes or silently corrupts.

---

## III · LATERAL (Cross-stream interactions within a tier)

**Question:** Do the buckets interact correctly? Are there dependency edges the graph misses?

### 3.1 F1 ↔ V1 — False dependency on Church stats

The dependency graph implies F1 blocks V1 (Sim S2). But the Python sim (`valoria_full_campaign_sim.py`) uses its own `starting_factions()` function with hardcoded values from `params/factions/stats_1_7_scale.md`. It does NOT read `ValoriaDataLibrary.gd`. The Church stat error in ValoriaDataLibrary.gd is a *Godot-only* bug. It blocks V3 (Godot Phase 6 parity), not V1/V2.

The workplan's F1 exit criteria ("Engine serves Μ-β and Μ-δ as designed") is correct for A-02 and B-07, but the Church stats item is incorrectly elevated to F1. It's correctly sequenced ("Sequence with F2") but incorrectly implies it blocks sim work.

### 3.2 A2 ↔ V1 — Overstated blocking

The dependency graph says "A2 (3 design-doc blockers) ↓ blocks V1 + V2 — TTRPG-faction layer mechanically present in sim only via unverified compilation source." But Sim S1 already committed and passed smoke tests *without* any of these three docs. The sim's faction model comes from `params/factions/stats_1_7_scale.md` (canonical) and `params/bg/core.md` (canonical), not from compilation/stage6. The design-doc blockers affect *completeness* of the faction mechanical spec, not the sim's ability to run. Correct statement: A2 weakly constrains V1 (some faction mechanics may be underspecified); it does not block it.

### 3.3 V1 → V2 — Correct but missing intermediate gate

The workplan says V1 must complete before V2 starts. Correct. But there's no specified gate for what happens if V1 produces redesign requirements (all three specs fail-flagged). Does V2 wait for redesign+re-validation? Or does V2 proceed with temporary stubs? The workplan's exit criteria says "land CANONICAL or fail-flagged with redesign requirements" but doesn't specify the fail-path.

### 3.4 M· ↔ V2 — Hidden interaction

RS test disambiguation (~1,340 instances in `tests/`) is classified as M·-tier, non-blocking. But if any of those 1,340 instances appear in sim test files (e.g., `tests/sim/valoria_full_campaign_sim.py` or future sim_var_01–06 regression tests), then RS ambiguity could produce silent errors in V2. The workplan should specify: verify that sim files are RS-clean before V2 starts, or accept the disambiguation as a V2 prerequisite.

---

## IV · DIAGONAL (Cross-tier, cross-stream interactions)

**Question:** Do items at different tiers in different streams create unexpected interactions?

### 4.1 F2.ED-746 × A3 — STRUCK stat referenced in rewrite

ED-746 verifies whether "Intel Advancement Counter" is STRUCK. ED-748 verifies whether "Intelligence stat" is STRUCK. But A3 (Varfell victory rewrite, post VTM-strike) re-gates Path A to "Intelligence ≥ 4." If Intelligence-as-faction-stat is truly STRUCK (ED-748), then the VTM-strike's own replacement gate uses a struck stat. This is a *contradiction within the struck-system itself* that neither F2 nor A3 surface. The workplan should flag: F2.ED-748 resolution directly determines whether A3's Path A re-gate is valid.

### 4.2 A4 (Solmund T-A..T-E) × V2 — Partial blocking, not conditional

The workplan says A4 "blocks V2 if any T-A..T-E touches Sim S3 modules." This is too vague. Specifically:

- **T-A (Perceptual Prophylaxis as Literary Engine)** connects to Certainty track and SA stat. Both are mechanical. Both are in Sim S3 (NPC priority trees reference Certainty). **Blocks V2.**
- **T-B (Seam Texts as Mechanical Objects)** connects to POI discovery and fieldwork Survey. These are in V2's threadwork module if fieldwork is included, but Sim S3's checkpoint scope doesn't list fieldwork. **Probably doesn't block V2.**
- **T-C (Double Consciousness Spiral)** connects to faction AI and Conviction Track. Both are in Sim S3. **Blocks V2.**
- **T-D (Baralta as Accidental Prophylaxis Cracker)** is explicitly "generational, not in-game mechanical." **Does not block V2.**
- **T-E (Solmund Repetition)** is "emergent arc design" — connects to arc emergence (T-23). **Weakly blocks V2.**

So A4 blocks V2 for T-A and T-C; weakly for T-E; not for T-B/T-D. The workplan should disambiguate.

### 4.3 F1.B-07 × V1 — Sim doesn't use deferred consequences

B-07 (deferred consequence pipeline) is a Godot-only bug. The Python sim implements its own consequence routing without Godot's ConflictContainer. B-07 blocks V3, not V1 or V2. The dependency graph says "F1 blocks V3" which is correct, but the workplan's narrative implies F1 must complete before sim work, which overstates the dependency.

### 4.4 C1 independence — Some content is safe before V

The workplan says "C1, C2, C3 require V1 + V2 complete." This is overcautious for some C1 items:

- `weapons/`, `armour/` — data comes from `params/combat.md` (canonical, stable). Not affected by PP-666 smoke test or Sim S3. **Can start now.**
- `factions/` — extraction from `ValoriaDataLibrary.gd` to `.tres` Resources. Mechanical reshaping of already-shipped data. **Can start after F1.Church-stats correction.**
- `territories/` — depends on T1-T15 canonical data, which is what V1 locks. **Must wait for V1.**
- `action_cards/`, `co_movement_cards/` — depend on mechanical finalization. **Must wait for V1/V2.**
- `triggers/` — depend on full trigger catalogue, which doesn't exist yet (`trigger_catalogue.md` is empty). **Blocked on C1-internal work, not V.**

---

## V · PLAYER ENGAGEMENT

**Question:** What does a player experience at each workplan milestone? Does the sequencing serve the player?

### 5.1 Sprint-by-sprint player experience

| Sprint | Duration | Player sees |
|---|---|---|
| Sprint 1 (Foundation) | 1–2 sessions | Nothing. Engine fixes are invisible. |
| Sprint 2 (Authority) | Unknown — Jordan-blocking | Nothing. Design decisions happen in documents. |
| Sprint 3 (Sim S2) | 1–2 sessions | Nothing. Python simulation runs internally. |
| Sprint 4 (Sim S3) | 1 session | Nothing. |
| Sprint 5 (Godot Phase 6) | 2–3 sessions | Test passes visible. No playable content. First time Godot code changes in ~10 days. |
| Sprint 6+ (Construction) | Many sessions | First player-facing content: weapon/armour data, faction Resources, territory data, trigger conditions. Still no UI, no scenes, no playable loop. |

**The workplan is entirely infrastructure-forward.** The first moment a player could experience *anything* is deep into Sprint 6+, and even then only as data files, not as a playable game. The first playable moment requires C2 (UI scenes), which the workplan correctly flags as "Godot-editor sessions, out-of-band for orchestrator."

**This is not a flaw.** The project is at the stage where the infrastructure must be correct before content can be authored. Building player-facing content on a broken Μ-β layer (A-02 stub) or a broken Μ-δ layer (B-07 dropped consequences) would produce content that works against the framework's promises. The workplan's sequencing is framework-correct at the cost of being engagement-deferred.

### 5.2 What's missing: a player-experience milestone

The workplan has no milestone that produces a *playable moment*. Even a minimal one. The roadmap (separate document) mentions UI in Phase G but the throughline workplan's C2 treats all UI as equivalent and defers it uniformly.

A framework-aligned player-experience milestone would be: **First Playable Season Loop** — a single season where the player sees the SeasonSlate (Layer 2), enters one combat (Layer 3), sees the Cascade Display (Layer 4), and observes RS/CI clock advancement (Layer 1). This exercises the four-layer architecture from `architecture.md` end-to-end while remaining scope-minimal.

The workplan doesn't define this milestone, and its absence means there's no point at which the framework's promises become *testable by a human player* rather than by a Python simulation. The sim verifies mechanical correctness; only a playable loop verifies experiential correctness (Q-robust: "Dramatic legibility: designer familiar with Valoria can read game-state and answer in one sentence each").

### 5.3 Engagement implications of M-throughline coverage

The workplan's V2 (Sim S3) module list covers all four Μ modes. But from the player's perspective, the modes aren't experienced as modes — they're experienced as:

- **"The world doesn't wait for me"** (Μ-α + Μ-β): clocks advance, NPCs act, factions move. The player feels urgency.
- **"My choice here changed something there"** (Μ-δ): personal combat result shifts faction Standing; faction order affects settlement; settlement decay affects RS.
- **"This world is made of something"** (Μ-γ): Thread-state visualization, environmental rendering, substrate language.

The workplan verifies #1 and #2 mechanically (V1/V2 sim coverage). It verifies #3 only at the data level (T-01 through T-03 throughlines). But #3 is primarily an *aesthetic* experience — the player needs to *see* substrate state, not just calculate it. This is where the Q-robust "dramatic legibility" criterion becomes a player-engagement gap: legibility requires UI, and UI is deferred to Sprint 6+/C2.

---

## VI · ELEGANCE, SMOOTHNESS, ROBUSTNESS

Per the project's specific definitions (not generic usage).

### 6.1 ELEGANCE — Logically simple; clear approach; no unnecessary overhead; easy to understand; allows player to intuit complex outcomes from simple choices.

**What the workplan achieves for elegance:**

*Structurally:* The five-bucket model (F/A/V/C/M) is elegant. Each bucket has a clear sentence-length definition. A reader can classify any new item into a bucket without ambiguity (except the tier-assignment errors noted in §I). The dependency graph is readable.

*Mechanically:* The workplan's sim-as-oracle architecture is elegant. One source of truth (Python sim) validates design specs. One target (Godot) implements validated specs. No ambiguity about which direction authority flows. If the sim disagrees with the spec, the spec needs redesign. If Godot disagrees with the sim, Godot has a bug.

**What the workplan fails to achieve for elegance:**

*Unnecessary overhead — 11 missing items.* The workplan requires cross-referencing three separate documents (the workplan, the roadmap, and the conversion_ledger) to know the full scope of outstanding work. MISSING-01 through MISSING-12 demonstrate that the workplan is not self-contained. An elegant workplan would subsume the roadmap and conversion_ledger action items, not exist alongside them.

*"Easy to understand" — framework vocabulary barrier.* The workplan uses Μ-α, Μ-β, Μ-γ, Μ-δ, М-1 through М-11, T-01 through T-41, Class A through E, and 15 failure-lexicon terms. This is the framework's language and is internally consistent. But it makes the workplan unintelligible without the throughlines_meta.md skeleton loaded. An elegant workplan would include a one-line translation of each framework term at first use.

*"Allows player to intuit complex outcomes from simple choices" — not evaluated.* The workplan doesn't evaluate whether the *game mechanics it orders for implementation* achieve this. It orders work by framework-fidelity, not by whether the resulting player experience produces intuitable complexity. This is the right ordering for infrastructure maturity, but the workplan should note the gap: after V2, a separate Q-elegance audit of the full mechanical stack would verify whether the game itself is elegant, not just the workplan.

### 6.2 SMOOTHNESS — Integrates cleanly without friction points; mechanics interact cleanly; zooms out well; transitions well; sequences well; pauses correctly; calculations consistent; integrates without issue into a unified mechanical approach.

**What the workplan achieves for smoothness:**

*Sequencing:* F before V before C. Foundation repairs before validation before construction. No item in C depends on an item in F through a hidden path — dependencies are explicit.

*Cross-repo integration:* The workplan correctly identifies that the Python sim (ttrpg repo) and the Godot codebase (valoria-game repo) have different dependency chains. F1 items land in valoria-game; V1/V2 items land in ttrpg; V3 bridges them. Smooth.

*Pause behavior:* M· items are correctly marked "run in parallel, never blocking." The workplan pauses at Sprint 2 (Authority) and explicitly says these are Jordan-blocking. The pause is architecturally correct.

**What the workplan fails to achieve for smoothness:**

*Sprint 2 → Sprint 3 friction.* If Sprint 2 stalls (Jordan doesn't resolve authority items for weeks), the workplan provides no parallel path. Sprint 3 cannot start (V1 depends on A1.D-5). Sprint 1 is already done. M· continues but is low-impact. The workplan should define: what can Claude execute during a Sprint 2 stall? Candidates: MISSING-01 (GameMode strip), MISSING-04 (provisional value confirmation), MISSING-07 (run Godot tests), C1 items identified in §IV.4.4 as V-independent (weapons/armour extraction, faction Resource extraction post-Church-stats-fix).

*conversion_ledger ↔ design_sync ↔ workplan friction.* Three documents claim to track implementation state. conversion_ledger says Phase 0 IN PROGRESS. design_sync says Phases 0–5 complete. The workplan says "pre-Phase 0 (compliance_check.py absent)." These are three different answers to "where are we?" This friction is the project's most dangerous integration failure — not in the game mechanics, but in the *development infrastructure.* The workplan should have a single item: "Reconcile conversion_ledger, design_sync, and workplan status claims into a single source of truth." Currently that item exists only in the roadmap.

*Zoom inconsistency.* The workplan zooms between framework-tier language (Μ-β violation) and implementation-specific language (wire `NPCTrajectoryEvaluator.evaluate_all()`) without a consistent intermediate layer. The reader must mentally translate between "the autonomous-agent layer is dark" and "line N of SituationGenerator.gd calls a stub." An intermediate layer — mapping each F1/V/C item to specific files and functions — would smooth the zoom from framework to implementation.

### 6.3 ROBUSTNESS — Allows for strategic thinking; allows for customization; allows for creativity and variety in approach; makes players feel important; makes players feel impactful; provides emergent narrative hooks without player involvement.

**Robustness of the workplan as a plan (meta-level):**

*Strategic flexibility:* The workplan allows one strategic choice — the order of authority decisions in Sprint 2. Jordan can prioritize D-5 (unblocks Sim S2) or D-4 (unblocks deterministic tests) or A2 (unblocks faction completeness). The workplan doesn't advise which order; it should. Recommendation: D-5 first (highest downstream fan-out).

*Resilience to discovery risk:* The workplan's V1 exit criteria says specs land "CANONICAL or fail-flagged with redesign requirements." But it doesn't scope the redesign path. If settlement_adjacency_v30 fails smoke-test, the redesign could be trivial (parameter adjustment, stays in V1 scope) or fundamental (adjacency model wrong, requires new Authority decision, re-enters A1). The workplan should specify: redesign that stays within Class C (parameter) is handled inline in V1. Redesign that escalates to Class B (extension) or A (new system) re-enters A· with a new PP entry and vetting block.

*Resilience to scope growth:* The workplan accounts for "new Class A/B items generated during execution" with the vetting posture section. This is correct and robust. Every sim session historically generates new patches (Session 1 produced 103 verification ledger entries and multiple editorial closures). The pipeline for absorbing new work exists.

**Robustness of what the workplan builds (game-level):**

*"Allows for strategic thinking":* The workplan verifies this through V1 (three viable approaches for Consolidation via Q-robust) and V2 (8 factions × multiple victory paths). But the verification is mechanical (does the sim produce three viable approaches?) not experiential (does the player *perceive* three viable approaches?). The gap between mechanical robustness and perceived robustness is bridged by UI (C2) and dramatic legibility (Q-robust §5 criterion). Neither is tested until very late.

*"Makes players feel important/impactful":* Verified only if Μ-δ (cross-scale consequence) actually fires in the engine. F1.B-07 fix is the prerequisite. Pre-B-07-fix, the engine silently drops cross-scale consequences, which means player actions at personal scale produce no strategic-scale registration. This is the exact opposite of "impactful." The workplan correctly identifies this but the player-engagement section should say it explicitly: **until B-07 is fixed, the engine actively undermines the player's sense of impact.**

*"Provides emergent narrative hooks without player involvement":* Verified only if Μ-β (autonomous agents) fires. F1.A-02 fix is the prerequisite. Pre-A-02-fix, NPCs don't evaluate trajectories, don't transition arcs, don't generate Domain Echoes. The world doesn't move. The workplan correctly identifies this but again: **until A-02 is wired, the engine has no autonomous narrative generation.** The 7 named NPCs (Almud, Himlensendt, Baralta, Vaynard, Ehrenwall, Torben, Edeyja) and their arc emergence machinery (T-23, T-25) are inert.

---

## VII · CONSOLIDATED FINDINGS

### 7.1 Errors to correct

| # | Finding | Severity | Section |
|---|---|---|---|
| E-1 | F1.A-02 and F1.B-07 misclassified as Class E; should be Class B minimum | Moderate — affects vetting_gate enforcement | §I.1.1 |
| E-2 | D-5 Einhir tier overclaimed as N+Ω-b; should be N+Μ-δ+М-2 | Low — affects ordering rationale, not sequencing | §I.1.1 |
| E-3 | campaign_modes blocker overclaims Ω-d; actual impact is narrower | Low | §I.1.1 |
| E-4 | A3 (Varfell rewrite) missing vetting protocol application post-PP-672 | Moderate — protocol gap | §I.1.2 |
| E-5 | F2.ED-748 × A3 contradiction: Intelligence ≥4 gate uses potentially-STRUCK stat | High — design-integrity | §IV.4.1 |
| E-6 | Church stats in F1 don't actually block V1 (sim has own data); graph overstates | Low — sequencing correct anyway | §III.3.1 |
| E-7 | A2 doesn't block V1 as stated; sim already works without design-layer docs | Low | §III.3.2 |

### 7.2 Missing items to add

| # | Item | Recommended bucket | Impact |
|---|---|---|---|
| M-01 | GameMode enum strip | F1 | Engine still has three-mode enum post-videogame-only collapse |
| M-02 | videogame_mode_spec.md as extraction prerequisite | F2 (documented dependency) | Governs all Phase 1+ extraction decisions |
| M-03 | rs_budget.md centralized RS source | V1 input + C1 source | Single authoritative RS drain/restoration doc |
| M-04 | Four Open Provisional Values in Godot code | F1 | Unverified placeholders in shipped code |
| M-05 | conversion_ledger / design_sync status reconciliation | F2 | Three docs disagree on "where are we" |
| M-06 | 132 threadwork audit findings (28 P0 blockers) | V3 prerequisite | Directly affects ThreadworkSystem implementation |
| M-07 | Run test_dice_engine.gd + test_tracker_registry.gd | F1 | Never-run tests on foundation code |
| M-08 | PP-652 starting PT values verification | V1 input | Sim S2 needs starting PT values |
| M-09 | hybrid_gaps_v30 propagation (17 gaps) | M· or F2 | Design-doc propagation debt |
| M-10 | arc_register open editorials ED-401–405 | M· | NPC Arc Emergence (T-23) completeness |
| M-11 | Solmund Appendix B 9 editorial items — individual tracking | A4 expansion | Some are Class B/C, not all Authority-tier |
| M-12 | DA-01 severity re-evaluation | F1 or C3 | May be F1-level if save/load currently corrupts |

### 7.3 Structural additions to make

| # | Addition | Why |
|---|---|---|
| S-1 | Sprint 2 stall path: parallel work during Jordan-blocking period | Smoothness — no dead time |
| S-2 | V1 fail-path protocol: parameter redesign stays in V1; Class A/B redesign re-enters A· | Robustness — discovery risk |
| S-3 | First Playable Season Loop milestone (between V3 and C2) | Player engagement — first human-testable moment |
| S-4 | Status reconciliation item (conversion_ledger × design_sync × workplan) | Smoothness — single source of truth for project state |
| S-5 | Q-elegance audit of full mechanical stack (after V2) | Elegance — verify game is elegant, not just workplan |
| S-6 | C1 items safe to start before V — explicitly mark weapons/armour/factions as V-independent | Smoothness — unlocks parallel work earlier |
| S-7 | A4 Solmund throughline V2-blocking disambiguation (T-A and T-C block; T-B/T-D/T-E don't) | Diagonal clarity |

---

## VIII · WHAT THE WORKPLAN ACHIEVES IF FULLY EXECUTED

### Elegance achieved

The sim-as-oracle architecture is elegant. Single-file sim structure, ledger-first discipline, seed-deterministic regression tests — the verification apparatus is logically simple, clear in approach, and has no unnecessary overhead. A designer can read the sim's smoke-test output and intuit what the game will feel like.

The five-bucket workplan itself is elegant in structure. F/A/V/C/M is a one-sentence taxonomy that correctly classifies ~60 items. That is high compression.

The framework integration is elegant where it's accurate: tagging items with throughline identifiers makes it possible to answer "if I skip this item, which player experiences degrade?" — which is the throughline framework's core value proposition.

### Smoothness achieved

The cross-repo pipeline (ttrpg design → Python sim → Godot implementation) is smooth. Authority flows one direction. Discrepancies are caught at defined gates (sim smoke-test for V1; parity tests for V3). No mechanic's implementation requires reading both repos simultaneously — the sim translates design into testable form, and Godot implements against the sim's verified output.

The editorial infrastructure (patch register + editorial ledger + supersession register) is smooth where it's reconciled. The three-register system handles create/update/delete lifecycle cleanly: patches propose, editorials track, supersession logs retractions. The workplan's F2 items clean the registers; post-F2, the infrastructure is smooth.

### Robustness achieved

The vetting framework (PP-672/674) is robustness infrastructure. It forces every new Class A/B proposal through a five-tier filter before it can be committed. This prevents "fantasy imposition," "dominant strategy," and "flavor-only" mechanics from entering the codebase. The workplan's inclusion of the vetting posture section means that new work generated *during* plan execution is also filtered. This is robust to scope growth.

The 103-entry verification ledger (Sim S1) plus the projected ~200-entry growth (Sim S2) creates mechanical robustness: every canonical value in the sim is traced to a source document. If a design doc changes a value, the ledger flags which sim constants need updating. This prevents silent drift between design and implementation.

### What's not achieved

**Experiential robustness is unverified.** Mechanical robustness (sim produces plausible outcomes) does not guarantee experiential robustness (player feels strategic variety, impact, emergent narrative). The gap is: nobody has played the game. The workplan produces a fully verified, framework-aligned, mechanically correct system — but it doesn't produce a moment where a human tests whether the framework's promises feel true. The First Playable Season Loop milestone (S-3 above) is the minimum viable experiential test.

**Elegance of the game itself is unaudited.** The workplan achieves infrastructure elegance and architectural elegance. Whether the *mechanics* are elegant — "core rule restatable after one reading," "second-order consequence predictable without additional rule-reading" — is a Q-tier evaluation that the workplan defers. The sim verifies correctness, not elegance. A dedicated Q-elegance pass should follow V2.

**Smoothness across the full scale-transition chain is unverified in engine.** The workplan verifies scale transitions in the sim (V2: "personal → faction → strategic"). But the engine's ZoomManager (stack-based container transitions) has empty `.tscn` files and no animation code. The smoothness of *experiencing* a scale transition — zooming from Board to Battle to Combat and back — is entirely deferred to C2. The framework's Μ-δ (cross-scale consequence) is mechanically verified; the player's experience of Μ-δ is not.
