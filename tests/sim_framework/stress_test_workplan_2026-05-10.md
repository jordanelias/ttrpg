---
title: Valoria Mechanical Systems — Comprehensive Stress-Test Workplan
date: 2026-05-10
scope: every-system
status: planning
session_token: 279993641470c167
authoring_model: Claude Opus 4.7
---

# Valoria Mechanical Systems — Comprehensive Stress-Test Workplan

> **Purpose.** Enumerate every mechanical system in the videogame, define the stress vectors that apply to each, catalog prior coverage, and produce an executable phased plan for the remaining stress work. This is a planning artifact, not stress output; downstream sessions execute against the modules defined here.
>
> **Output target.** Videogame (Godot 4.6). Every stress vector below evaluates whether the system can be implemented in-engine and whether the player experiences the result through UI or invisibly through engine logic.

---

## 0. Meta

### 0.1 Scope

- **In scope.** Every mechanical system referenced in `params/`, `params/bg/`, `params/factions/`, `designs/architecture/`, `designs/provincial/`, `designs/scene/`, `designs/threadwork/`, `designs/territory/`, `designs/world/`, and the `bg/` sub-tree. Coupled emergent behaviors (campaign arc shape, narrative coherence, scale-transition seams). Engine substrate (dice, TN, degrees, clocks, phases, tracks).
- **Out of scope.** Asset pipeline (art, audio, animations). GDScript scene wiring. UI/UX layouts. Persistence format. Localization. Anything that depends on engine_v4 surfaces not yet built.

### 0.2 Methodology

Follows the existing `valoria-simulator` skill (7 modes A–G) and `valoria-mechanic-audit` skill (5 modes A–E). Stress modules invoke specific mode combinations per system. Vector taxonomy in §2 defines the test surfaces; per-system plans in §4 select applicable vectors and specify modules.

**Stress module convention** (from existing harnesses): `<system>_<aspect>_stress_NN/` directory with a `module_manifest.md` index and per-vector sub-files. Single-bundle simpler systems may collapse to a single file. Letter prefixes (A/B/C/...R-suite/F-bundle/G) preserve the conventions emerging from prior work; new letters allocated below.

### 0.3 Success criteria for the workplan itself

A workplan is successful if a downstream session can pick up any phase, fetch the named files, run the specified modules in order, and produce verification commits matching the manifest. Acceptance test: for every system listed in §4, the entry contains canonical paths, applicable vectors, prior coverage status, specific stress modules with NERS or chain definitions, priority, and named canon gates.

### 0.4 Gating prerequisites (must complete before stress execution)

1. **`canon/editorial_ledger.yaml`** archive-by-status auto-fix (currently surfaced by compliance check on every bootstrap; 2 P2 entries blocking).
2. **`references/file_index_summary.md`** regenerate — currently 0 chars; bootstrap status block can't compute propagation-pending count.
3. **`freshness_gate.py --update`** — 1 stale canonical source pinned in `canonical_sources.yaml`.
4. **`references/canonical_sources.yaml`** — register drift on `combat`/`derived_stats` design_doc fields documented in `combat_arch_residual_stress_01/module_manifest.md` §"Registry drift" but not yet remediated.
5. **`canon/02_canon_constraints.md`** — verify load-bearing constraints used by `task_gate('simulation' | 'audit')` are current.
6. **`read_active_sessions`** concurrent-session detection (`github_ops`) is broken per prior session log — collision detection currently falls back to fetch-head OID. Either fix or document the fallback as canonical before parallel stress sessions are encouraged.
7. **`improvement_avenues_2026-05-10.md`** at `/home/claude/work/` — uncommitted, 283 lines, ephemeral. Either commit or discard before relying on its findings.
8. **PAT rotation** — VALORIA_PAT echoed across chat surfaces; outstanding from prior session.

Items 1–4 are repo-level. Items 5–6 are infrastructure. Items 7–8 are housekeeping. None block this workplan's authoring, but they block reproducible stress execution.

---

## 1. Guiding principle

> Stress testing is not "play the game and see if it breaks." Stress testing is the deliberate identification of input regions, interaction chains, and emergent compositions where the canonical mechanic produces incoherent, non-terminating, dominated, or narratively degenerate output. Every stress module finishes with one of three verdicts: **(1) canon preserved** (no change, sometimes with deferred refinements flagged); **(2) canon corrected** (specific PP- proposed); **(3) gap surfaced** (ED- raised, P1/P2 ranked).

The prior `combat_arch_residual_stress_01` and `fieldwork_lifecycle_stress_01` bundles are the format reference. Both produce "preserve" verdicts on mature canon with deferred refinements flagged — the goal is verification under hostile inputs, not mechanical churn.

**Anchor in what's working.** Most systems have a mature canonical surface. The workplan narrows stress to genuine residual risk surfaces, not blanket re-derivation. Where prior stress passes have closed a system, this workplan flags it as "verified" and limits further work to canon-shift propagation (e.g., did PP-716 wound correction touch this system's assumptions?).

---

## 2. Stress vector taxonomy

Each system in §4 selects a subset of these vectors. Definitions here apply globally; per-system plans specify which vectors and what inputs.

| Vector | Mode | Definition |
|---|---|---|
| **V1 — Formula validation** | Mode A | Single mechanic isolation. Verify the formula reproduces canonical outputs across declared input domain. Catches typos, sign errors, off-by-one. |
| **V2 — Probability distribution** | Mode A | d10 outcome distribution at TN7 (1=−1, 7–9=+1, 10=+2; EV 0.4 per die). Bounds: 1d, 5d, 10d, 20d pools. Check tails, modes, degenerate-pool behavior. |
| **V3 — Interaction chain** | Mode B | A→B→C chains where one mechanic feeds another. Identify state-coupling assumptions, race conditions, ordering dependencies. |
| **V4 — Edge cases (NERS)** | Mode D | Numerical Edge Resolution Sweep. Six edge-case categories per existing harness: boundary, cascade, regression, crunch (crunch cascade), ambiguity, incoherence, optimal play. |
| **V5 — Full scenario** | Mode C | Multi-round/multi-season state simulation. Verify the system behaves coherently in realistic play context. |
| **V6 — Coverage matrix** | Mode E | Cross-input × cross-output coverage check. Catches uncovered combinations. |
| **V7 — Scale transition** | new | Personal ↔ settlement ↔ territory ↔ peninsula handoff. State that survives the transition, state that resets, state that re-computes. The transition is the game's core UX flow per `<design_doc_framing>`. |
| **V8 — Convergence / termination** | new | Does the system terminate? Loop? Deadlock? Especially load-bearing for clocks, tracks, faction state machines. |
| **V9 — Save/load mid-mechanic** | new | Persistence boundary stress. What state must be serialized? What can be re-derived? Player saves mid-combat, mid-fieldwork, mid-phase. |
| **V10 — Dominant strategy probe** | new | Player-side game-theory. Is there a strategy that strictly dominates? A degenerate optimum? An exploit chain? |
| **V11 — NPC coherence** | new | Does the engine drive NPC responses that read as coherent character behavior, not as mechanical artifacts? Especially load-bearing for priority trees, faction-personal layer, threadwork. |
| **V12 — Narrative emergence** | new | Does the system's output produce legible emergent narrative? Or only mechanical state? Per intent-of-game: "engaging game world with emergent narratives." |

V1–V6 map directly to existing simulator-skill modes. V7–V12 are this workplan's additions — they cover surfaces that single-system stress tests systematically miss.

---

## 3. Prior coverage — do-not-redo register

### 3.1 Completed (verified 2026-05-09 to 2026-05-10)

| Suite | Scope | Verdict | Commit / Location |
|---|---|---|---|
| `combat_arch_residual_stress_01` R1–R10 | Combat videogame architecture residual-risk sweep | All 10 verified; PP-716 wound correction landed mid-task; R1 redone as v2 | `tests/sim/combat_arch_residual_stress_01/` |
| `conviction_stress_01` (A) | Conviction Taxonomy + Axis Matrix | A1 preserve PP-684 13-Conviction + 52-cell matrix; P1 drift defect surfaced (npc_behavior_v30 §1.2 stale redirect) | `tests/sim/conviction_stress_01/` |
| `fieldwork_lifecycle_stress_01` (F-bundle) | F1 Wager, F2 Knot Lifecycle, F3 Heresy Investigation, F4 Mending | All preserve canonical; PP-716 propagation re-validated | `tests/sim/fieldwork_lifecycle_stress_01/` |
| `geography_phase4_stress_01` | Mountain Pass, cavalry, coastal landing | Land-based verified; **P1 substrate gap surfaced on ED-055 naval — no canonical sea-zone adjacency** | `tests/sim/geography_phase4_stress_01/` |

### 3.2 Deferred refinements from completed suites (re-stress trigger if executed)

- **R4 C4.3** — T-trigger spec
- **R5 C5.3** — voluntary stake escalation
- **R7** — stress threshold criteria enumeration (FF on stress only)
- **R8** — partial-freeze ticker selection
- **R9** — routine-encounter B reservation (presentation flag)
- **conviction_stress_01 ⚠×5** — Community/Identity collinearity, Order/Authority collinearity, 5th-axis trigger spec, Self-Other UI display, cultural template count
- **F2** — EC-F2.A-01 sustained Disposition reduction definition

### 3.3 Historical batches (consulted, not redone)

`arc_test_batch2/3/4_results.md`, `arc_test_results.md`, `session_audit_2026-04-19.md`, `early_game_ignition_analysis.md` [SUPERSEDED], `tensions_pair_validation.md`, `conflict_architecture_proposal.md`. Findings from these batches are integrated into per-system entries below as `[B2]`, `[B3]`, `[B4]` annotations.

### 3.4 Open coverage findings (from `tests/coverage_matrix.md`, still open)

| ID | Description | Resolution path |
|---|---|---|
| SIM3-04 (ED-586) | Arc state vs Priority 6 at Mandate < 3 | Layer W6 stress (NPC priority trees) |
| SIM3-07 (ED-587) | Stability Crisis Zoom In trigger absent | Layer C4 stress (scale-transition seams) |
| SIM4-01 (ED-588) | RM Phase 2 T9 holding condition unreachable | Layer S15 stress (faction succession / RM) |
| SIM4-02 (ED-589) | RM Presence marker mechanics undefined | Layer S15 stress |
| SIM5-01 (ED-616) | No Parliamentary block on Tribune actions | Layer G2 stress (Parliament / PI) |
| SIM5-02 (ED-617) | Grand Contest Recall: once-per-source fix | Layer P2 stress (Contest) |
| SIM5-04 (ED-618) | Torben Conviction window: S1–8 formal def | Layer P6 stress (Conviction window) |
| SIM5-13 (ED-619) | 3-Obligation GM advisory cap | Layer C0 stress (engine — no GM in videogame; advisory must become engine logic) |

---

## 4. System enumeration and per-system stress plans

System IDs use the convention `<layer><N>` where layer ∈ {E, P, S, W, G, C}. Letter prefixes for stress suites (A, F, G, R-suite) preserve existing harness convention; new suites are allocated in §4.X.

### LAYER E — Engine substrate

#### E1 — Dice / TN / Degree resolution

**Description.** d10 pool resolution at TN7. 1=−1, 7–9=+1, 10=+2. Foundation of every contest, combat, fieldwork, and faction roll.
**Canonical.** `params/core.md` + `params/bg/core.md` + degree tables (referenced across `params/combat.md`, `params/contest.md`).
**Coupling.** Every resolution surface. Single point of failure if formula drifts.
**Prior coverage.** Implicit in every prior stress test. Never explicitly stress-tested in isolation.
**Priority.** P0 (foundation).
**Effort.** 1 session, single bundle.
**Suite ID.** `E1_dice_resolution_stress_01` (suite letter **E**).

**Stress modules:**
- **E1.1 — V1 Formula validation.** Reproduce EV 0.4/die across 1d–20d. Verify boundary outputs: pool=0 (auto-fail or impossible?), pool=1 (canonical bounds: −1 / 0 / +1 / +2), pool ≥ 20 (verify the engine doesn't truncate or overflow).
- **E1.2 — V2 Probability distribution.** Full distribution tables for 1d, 3d, 5d, 7d, 10d, 15d, 20d. Verify P(net ≥ 0), P(net ≥ +N) for N ∈ {0, 1, 2, 3, 5, 8}. Cross-check against any degree-table assumptions in `combat.md` and `contest.md`.
- **E1.3 — V4 NERS edge cases.** Boundary: pool=0 behavior, pool=1 lone-die, max canonical pool (verify there is one). Crunch: simultaneous +2/−1 from a single die — does a 10 also fail the 1-counting? Ambiguity: re-rolls (do any mechanics grant them?), bonus dice, exploding-on-10. Optimal play: when does adding +1D have diminishing return vs +1 TN swing?
- **E1.4 — V6 Coverage matrix.** Pool × TN × modifier-stack × situational-bonus (advantage / disadvantage if applicable). Verify the resolution surface is closed under composition.

**Canon gates.** None — dice are foundational.
**Open questions.** Are there any non-d10-pool resolution mechanics anywhere in the canon? (e.g. flat checks, fixed-degree assignments). If yes, those must be enumerated as exceptions to E1.

---

#### E2 — Clocks

**Description.** Pacing devices that fill across rounds/scenes/phases and trigger effects on completion. Includes Conviction Track, Claim Integrity, Realm Stability, faction-specific clocks.
**Canonical.** `params/bg/clocks.md` (skeleton: 6,787 chars; reference design `designs/provincial/clock_registry_v30_infill.md`).
**Coupling.** Every system that uses pacing — combat (no, but Conviction is here), fieldwork (lifecycle), faction layer (CI, RS, RDT/TD, PI), governance.
**Prior coverage.** Indirect via B3/B4 (RS decay verified; CI/Mass Seizure timing verified; PI track verified; RDT/TD verified at simplified-CI fidelity).
**Priority.** P0 (foundation; many systems depend on clock semantics).
**Effort.** 1–2 sessions.
**Suite ID.** `E2_clocks_stress_01` (suite letter **E**).

**Stress modules:**
- **E2.1 — V1 Formula validation.** For every named clock: declare canonical bounds, fill rate (per source), drain rate (if any), trigger threshold, post-trigger behavior (reset / persist / advance state).
- **E2.2 — V3 Interaction chain.** When multiple clocks fill from the same source event (e.g., a Seizure attempt advances CI, may advance RS, may interact with Coup Counter). Verify ordering is canonical.
- **E2.3 — V4 NERS edge cases.** Boundary: clock at 0 with negative input — does it stay at 0 or wrap? Cascade: simultaneous trigger on multiple clocks. Crunch: clock fully fills and over-fills in a single event — does overflow carry? Optimal play: can a player intentionally stall a clock by avoiding source events?
- **E2.4 — V8 Convergence.** Does every active clock eventually resolve? Are there pathological inputs where a clock stalls indefinitely?
- **E2.5 — V9 Save/load.** Clock state at save boundary — partial fill, mid-trigger-resolution, mid-cascade.

**Canon gates.** Clock registry consolidated. (`designs/provincial/clock_registry_v30_infill.md` is small at 645 chars — verify it covers all clocks, not just a sample.)
**Open questions.** Is there a unified clock state machine or are clocks one-off implementations per system?

---

#### E3 — Phases / Tracks

**Description.** Strategic-layer turn structure: phases within a season, season tracks, multi-season tracks.
**Canonical.** `params/bg/phases.md`, `params/bg/tracks.md`.
**Coupling.** Every strategic-layer action; clocks tick on phase boundaries; faction actions are phase-locked.
**Prior coverage.** B3/B4 used phase structure but didn't stress it.
**Priority.** P0.
**Effort.** 1 session.
**Suite ID.** `E3_phases_tracks_stress_01`.

**Stress modules:**
- **E3.1 — V1 Phase enumeration.** Verify the canonical phase list and ordering. Identify any phases gated by other-phase outcomes.
- **E3.2 — V3 Phase-boundary chain.** What state crosses phase boundaries? What resets? Faction actions consumed mid-phase but resolved at boundary — verify ordering.
- **E3.3 — V4 NERS edge cases.** Boundary: zero-action phase, all-skip phase, simultaneous trigger from multiple phases. Ambiguity: a clock fills mid-phase — does the trigger resolve immediately or at phase boundary?
- **E3.4 — V8 Convergence.** Does every season terminate? Are there inputs that produce infinite within-season loops?

**Canon gates.** `params/bg/tracks.md` (8,082 chars) — read fully.
**Open questions.** Are tracks orthogonal (independently advancing) or coupled?

---

#### E4 — Scale transitions

**Description.** Personal ↔ settlement ↔ territory ↔ peninsula handoff. The game's core UX flow per `<design_doc_framing>`.
**Canonical.** `params/scale_transitions.md` (6,040 chars), `designs/architecture/scale_transitions_v30_infill.md` (4,535 chars).
**Coupling.** Every system that exposes player input at multiple scales. Combat, fieldwork, faction, governance.
**Prior coverage.** R9 (two-architecture sufficiency, A+C confirmed) addresses the personal-scale architectural cardinality. Personal↔settlement transition implicit in fieldwork-combat tempo R8. **Personal↔territory and territory↔peninsula transitions never explicitly stressed.**
**Priority.** P0 (UX-load-bearing).
**Effort.** 2 sessions.
**Suite ID.** `E4_scale_transitions_stress_01`.

**Stress modules:**
- **E4.1 — V7 Scale transition.** For every transition pair (P↔S, P↔T, P↔Pen, S↔T, S↔Pen, T↔Pen): enumerate state that propagates, resets, recomputes. Verify each direction independently (transitions are not necessarily symmetric).
- **E4.2 — V3 Cross-scale interaction chain.** A territory-scale decision propagates to settlement-scale opportunities propagates to personal-scale scenes — verify the chain is coherent. Specific test: faction-layer Mass Seizure decision propagates to settlement-level garrison disposition propagates to potential personal-scale arrest scene.
- **E4.3 — V4 NERS edge cases.** Boundary: zoom-in to scale that has nothing to resolve. Crunch: zoom-out request while a personal-scale clock is mid-fill. Ambiguity: which scale "owns" a given decision (e.g., bishop appointment: settlement or territory?).
- **E4.4 — V12 Narrative emergence.** Does the player experience scale transition as a meaningful zoom (vs as a UI mode change)? Specifically: does a personal-scale outcome read as having strategic-scale consequence? (Per `<intent_of_game>`: "makes players feel important to the game world.")
- **E4.5 — V11 NPC coherence across scales.** A named NPC at personal scale must remain the same entity at settlement scale (state, disposition, threadwork knots intact). Verify referential integrity.
- **E4.6 — V9 Save/load across scale boundary.** Save while transitioning — what state survives?

**Canon gates.** `params/scale_transitions.md` must be fully read; `designs/architecture/scale_transitions_v30_infill.md` consulted. **ED-587 (Stability Crisis Zoom In trigger absent)** must be resolved as part of E4.3 or noted as gap.
**Open questions.** Are all four scales fully canonical, or does the game only formally distinguish personal vs strategic with finer subdivision implicit?

---

#### E5 — Campaign modes

**Description.** Campaign-level configuration: difficulty, scope (single-territory vs full peninsula), historical scenarios, etc.
**Canonical.** `params/campaign_modes.md` (3,711 chars), `designs/architecture/campaign_modes_v30_infill.md` (6,129 chars).
**Coupling.** Sets initial conditions for everything else. Wrong campaign mode = wrong starting state.
**Prior coverage.** None.
**Priority.** P2 (configuration-layer; doesn't affect canonical mechanics).
**Effort.** 0.5 session.
**Suite ID.** `E5_campaign_modes_stress_01`.

**Stress modules:**
- **E5.1 — V1 Mode enumeration.** List every canonical mode. Verify each has a fully-specified initial state.
- **E5.2 — V4 Mode-switching edges.** Can a campaign mode change mid-game? If so, what happens to in-flight state?
- **E5.3 — V12 Mode-driven narrative variance.** Does each mode produce distinctly different campaign arcs (per `<intent_of_game>` emergent narrative goal)?

**Canon gates.** `designs/architecture/campaign_modes_v30_infill.md` read fully.

---

### LAYER P — Personal-scale resolution

#### P1 — Personal combat

**Description.** Tactical combat at the individual-character scale. d10 pool resolution with degree tables, wound mechanics, Composure, IP gauge, Fibonacci-cap zone collapse.
**Canonical.** `params/combat.md` (16,731 chars), `designs/scene/combat_v30_infill.md` (9,860 chars).
**Coupling.** Conviction, fieldwork (R8 tempo coupling), threadwork (knot rupture from FR Dissolution), Faction layer (mass combat handoff).
**Prior coverage.** ✅ **`combat_arch_residual_stress_01` complete 2026-05-10.** All 10 R-modules verified against PP-716 canon. R1 v2 (wound permanence post-PP-716), R2 (skill input), R3 (mass three-mode reframe), R4 (hero participation default), R5 (wager stake range), R6 (Fibonacci cap), R7 (FF on stress), R8 (fieldwork tempo), R9 (two-architecture), R10 (IP gauge).
**Priority.** P3 — coverage closed; only deferred refinements remain.
**Effort.** 0 sessions main; 1–2 sessions for deferred refinements (optional).
**Suite ID.** N/A (suite closed).

**Remaining work (deferred refinements only):**
- **R4 C4.3** — T-trigger spec
- **R5 C5.3** — voluntary stake escalation
- **R7** — stress threshold criteria enumeration on adoption
- **R8** — partial-freeze ticker selection
- **R9 C9.3** — routine-encounter B-shape presentation reservation

Each deferred refinement is a single mini-module (~2–4 hours). Bundle into `combat_deferred_refinements_pack_01` if/when Jordan authorizes.

**Canon gates.** None (canon mature).

---

#### P2 — Contest (general)

**Description.** Stake-based resolution of opposed actions outside combat. The general-purpose adjudication mechanic for non-combat conflict.
**Canonical.** `params/contest.md` (17,152 chars).
**Coupling.** Fieldwork (Wager is a contest specialization), social contest (P3), Faction layer (negotiations).
**Prior coverage.** Indirect via R5 (wager stake range — but Wager is a specialization). General contest mechanic never explicitly stress-tested.
**Priority.** P1.
**Effort.** 1 session.
**Suite ID.** `P2_contest_general_stress_01` (suite letter **P**).

**Stress modules:**
- **P2.1 — V1 Formula validation.** Stake declaration, opposed pool resolution, degree-to-outcome table.
- **P2.2 — V3 Interaction chain.** Contest outcome → state change → subsequent contest. Verify cascading contests don't interact pathologically.
- **P2.3 — V4 NERS edge cases.** Boundary: zero-pool participant (auto-loss?), tied degrees (canonical tiebreak?). Cascade: multi-party contest (>2 sides). Crunch: contest stakes that exceed participant capacity. Optimal play: stake declaration as game-theory problem (do players over-stake or under-stake systematically?).
- **P2.4 — V10 Dominant strategy probe.** Is there a stake level that strictly dominates? An always-decline-low-stake heuristic?
- **P2.5 — V11 NPC coherence.** NPC stake selection — does it read as character-driven or mechanically optimal? (Per W6 priority trees.)

**Canon gates.** `params/contest.md` fully read.
**Open questions.** Is contest a single mechanic or a family? (Fieldwork has Wager as a contest; social contest is P3. How do they relate canonically?) **Open finding SIM5-02 (ED-617) "Grand Contest Recall: once-per-source fix"** belongs here.

---

#### P3 — Social contest

**Description.** Persuasion, negotiation, ideological clash. Resolution at the personal scale, possibly with strategic-scale consequence.
**Canonical.** `designs/scene/social_contest_v30_infill.md` (5,493 chars).
**Coupling.** Conviction Track (P6), threadwork (P5), Disposition modifiers, Faction-personal layer.
**Prior coverage.** None as a stress suite. Touched by F2 chain 2 (public counsel citation → immediate rupture at Disposition −4) but only at the disposition-modifier surface.
**Priority.** P1.
**Effort.** 1–1.5 sessions.
**Suite ID.** `P3_social_contest_stress_01`.

**Stress modules:**
- **P3.1 — V1 Formula validation.** Social contest pool composition (which attributes contribute?), TN, degree-to-outcome mapping.
- **P3.2 — V3 Interaction chain.** Social contest → Disposition change → threadwork knot strain → conviction shift. Verify the chain isn't underspecified.
- **P3.3 — V4 NERS edge cases.** Boundary: zero-Disposition target (always-hostile), max-Disposition target (immune to social contest?). Cascade: social contest in a public setting affecting bystander NPCs. Ambiguity: persuasion vs intimidation vs deception — are these distinct mechanical channels or one?
- **P3.4 — V11 NPC coherence.** NPC social-contest behavior must read as character-driven (priority-tree decision based on conviction + faction + disposition).
- **P3.5 — V12 Narrative emergence.** Does a successful persuasion read as character development or as mechanical state-flip?

**Canon gates.** `designs/scene/social_contest_v30_infill.md` fully read. Coupling to conviction (P6) must be canonical before P3.2 can run.

---

#### P4 — Fieldwork

**Description.** Personal-scale investigative / clandestine / interpersonal activity outside combat. Includes Wager, Heresy Investigation, Mending, Knot Lifecycle.
**Canonical.** `params/fieldwork.md` (12,220 chars), `designs/scene/fieldwork_v30_infill.md` (27,760 chars).
**Coupling.** Threadwork (knot lifecycle is a fieldwork product), combat (R8 tempo), conviction (Scar), Faction-personal layer.
**Prior coverage.** ✅ **`fieldwork_lifecycle_stress_01` complete 2026-05-10.** F1 (Wager covered in R5), F2 (Knot Lifecycle), F3 (Heresy Investigation), F4 (Mending). All verdicts: F2.1 / F3.1 / F4.1 preserve canonical.
**Priority.** P3 — coverage closed.
**Effort.** 0 main; 1 mini-pack for deferred refinement (EC-F2.A-01 sustained Disposition reduction definition).
**Suite ID.** N/A (suite closed).

**Remaining work.** EC-F2.A-01 sustained Disposition reduction spec ambiguity. Single mini-module.

---

#### P5 — Threadwork

**Description.** Narrative/relationship system. Knots, threads, FR (Friendship/Rivalry?) state, Bonds investment.
**Canonical.** `params/threadwork.md` (14,481 chars), `designs/threadwork/threadwork_v30.md` (canonical SHA `08e4dcf2`), `designs/threadwork/threadwork_v30_infill.md` (40,583 chars), `designs/threadwork/threadwork_philosophical_reference_v30_infill.md` (12,314 chars).
**Coupling.** Fieldwork (F2 knot lifecycle), conviction (Scar from close-knot break), combat (FR Dissolution from R1), social contest (P3 disposition channel).
**Prior coverage.** F2 (Knot Lifecycle) covered the knot state machine at full grain. **Thread-level dynamics** (threads as super-knot structures), **FR state machine**, **Bonds investment economics** never explicitly stressed.
**Priority.** P1.
**Effort.** 1.5–2 sessions.
**Suite ID.** `P5_threadwork_stress_01`.

**Stress modules:**
- **P5.1 — V1 Formula validation.** Bonds investment cost curve, max-Knot count per character (Chain 5 of F2 referenced but didn't stress), thread-level state aggregation.
- **P5.2 — V3 Interaction chain.** Knot rupture → thread strain → FR shift → conviction implication. Multi-knot threads with conflicting state.
- **P5.3 — V4 NERS edge cases.** Boundary: zero-knot thread (does it exist?), max-knot character (Chain 5 referenced), thread between two threadwork participants where both are also each other's knots. Cascade: a death/major event causes simultaneous rupture across multiple shared knots.
- **P5.4 — V8 Convergence.** Can the threadwork state machine deadlock? E.g., A and B both need C's input to advance, C is incapacitated.
- **P5.5 — V11 NPC coherence.** NPC threadwork participation — does the engine drive NPCs to invest, rupture, mend in character-coherent ways?
- **P5.6 — V12 Narrative emergence.** The signature emergent-narrative system. Does threadwork output read as relationships unfolding or as state-machine ticks?

**Canon gates.** Threadwork v30 fully read. F2 results integrated as baseline.
**Open questions.** Is "thread" a first-class entity in the data model or an emergent property of knot graphs?

---

#### P6 — Conviction Track

**Description.** Character ideological/moral state. 13-Conviction taxonomy across 52-cell axis matrix (PP-684 canon).
**Canonical.** `designs/scene/conviction_track_v30_infill.md` (6,078 chars), referenced in PP-684 conviction_taxonomy_v30.md.
**Coupling.** All personal-scale resolution (conviction modifiers), threadwork (Scar accumulation), fieldwork (Scar from close-knot break), Faction-personal layer.
**Prior coverage.** ✅ **`conviction_stress_01` A-module verified 2026-05-10.** A1 preserve PP-684 13-Conviction + 52-cell matrix. P1 drift defect: `npc_behavior_v30 §1.2` stale redirect to deprecated `conviction_track_v1.md`.
**Priority.** P2 — A coverage closed; B-C-D-E coverage remaining + P1 drift fix.
**Effort.** 1 session (modes B/C/D + drift fix).
**Suite ID.** `P6_conviction_extended_stress_01`.

**Stress modules (extension to A-coverage):**
- **P6.1 — V3 Interaction chain (Mode B).** Conviction shift cascade: a single event raises one conviction, lowers another via axis-matrix orthogonality. Verify cross-axis interactions canonical.
- **P6.2 — V5 Full scenario (Mode C).** Multi-scene conviction arc across a campaign. Specifically: stress **SIM5-04 (ED-618) Torben Conviction window S1–8 formal def** — Torben's conviction arc requires a formally-specified window.
- **P6.3 — V4 NERS edge cases (Mode D).** Boundary: character with all 13 convictions at max, all at min. Crunch: simultaneous Scar from multiple sources. Ambiguity: 5th-axis trigger spec (deferred from A).
- **P6.4 — V11 NPC coherence.** NPC behavior driven by conviction — verify priority-tree integration. Specifically: **SIM3-04 (ED-586) Arc state vs Priority 6 at Mandate < 3.**
- **P6.5 — Drift fix (infrastructure).** Remediate `npc_behavior_v30 §1.2` redirect.

**Canon gates.** PP-684 canon (already in place).
**Open questions.** Community/Identity collinearity, Order/Authority collinearity, Self-Other UI display, cultural template count (all deferred from A-coverage).

---

### LAYER S — Strategic-scale

#### S1 — Mass combat

**Description.** Territory-scale combat. Distinct from personal combat. Includes terrain, force composition, march budgets, fortification interactions.
**Canonical.** `params/mass_combat.md` (33,024 chars; large — read in full), `designs/provincial/mass_battle_v30_infill.md` (3,159 chars).
**Coupling.** Geography (W1), Faction layer (S2/S3), Realm Stability (S10), Altonian Vanguard (S9), Fort constraint (W?).
**Prior coverage.** B3 verified fort constraint (3 routes; T14 impassable at Mil 4). B3 verified RS decay. **`geography_phase4_stress_01` 2026-05-10**: mountain pass, cavalry, coastal landing — Phase 3 verified for land; Phase 4 surfaced **P1 ED-055 naval scope gap** (no canonical sea-zone adjacency between non-T1 coastal territories).
**Priority.** P1.
**Effort.** 2 sessions.
**Suite ID.** `S1_mass_combat_stress_01`.

**Stress modules:**
- **S1.1 — V1 Formula validation.** Force-composition arithmetic, march-budget arithmetic, casualty/strain computation, retreat logic.
- **S1.2 — V3 Interaction chain.** Mass-combat → casualty propagation to personal-scale (named NPCs in the engagement) → Realm Stability tick → faction Mandate/Influence shift.
- **S1.3 — V4 NERS edge cases.** Boundary: 0-force vs 0-force, single-unit forces. Cascade: chained engagements in same season. Crunch: simultaneous engagements at multiple territories. Optimal play: dominant force-composition or always-engage / always-decline strategies.
- **S1.4 — V7 Scale transition.** Mass-combat → zoom-in to personal-scale (named NPC engagement, e.g., Almud leads a charge) → zoom-out back to mass result. Verify state coherence both directions.
- **S1.5 — Naval gap closure (ED-055).** Block this stress until naval canon written, OR explicitly carve out naval scenarios as deferred. Recommendation: carve out, run S1 land-only, add `S1_mass_combat_naval_addendum_01` post-ED-055.

**Canon gates.** ED-055 naval scope (P1, blocks coastal). PP-726 settlement registry (already landed; verify integration). 37-settlement adjacency map.
**Open questions.** Is march-budget time-based or action-based? How are fortified settlements modeled at mass scale?

---

#### S2 — Faction layer (Personal)

**Description.** Per-NPC faction membership, mandate, influence, internal-faction dynamics.
**Canonical.** `params/factions_personal.md` (7,805 chars), `designs/provincial/factions_personal_v30.md` (canonical SHA `bde4d109`).
**Coupling.** S3 (BG faction layer aggregates from S2), W6 (NPC priority trees), threadwork (P5), conviction (P6).
**Prior coverage.** B1/B2 covered faction succession split and RM emergence (S15). General faction-personal layer never stressed.
**Priority.** P1.
**Effort.** 1.5 sessions.
**Suite ID.** `S2_factions_personal_stress_01`.

**Stress modules:**
- **S2.1 — V1 Formula.** Mandate/Influence formulas at individual scale; aggregation rule into faction-level totals.
- **S2.2 — V3 Interaction chain.** Personal-conviction shift → faction-mandate shift → faction-action availability shift. End-to-end propagation.
- **S2.3 — V4 NERS.** Boundary: faction with 1 member, faction with all members at 0 mandate, faction with internal civil war (members at opposite mandate poles). Cascade: high-influence-member death.
- **S2.4 — V11 NPC coherence.** NPC faction allegiance under stress (rival faction promotes them, family member dies — does behavior read coherently?).

**Canon gates.** `factions_personal_v30.md` (canonical SHA pinned) — must be read fully.

---

#### S3 — Faction layer (Strategic / BG)

**Description.** Faction as strategic-layer entity: actions, resources, territorial holdings, succession.
**Canonical.** `params/factions.md` (2,961 chars), `params/bg/factions.md`, `params/bg/faction_actions.md` (24,168 chars).
**Coupling.** S2 (aggregates personal), W2 (settlement holdings), S5 (CI), S15 (succession), S10 (RS), E3 (phase-locked actions).
**Prior coverage.** B1/B2/B3/B4 stressed multiple faction-layer aspects (succession, Mandate, Influence, CI suppression).
**Priority.** P1.
**Effort.** 2 sessions.
**Suite ID.** `S3_factions_strategic_stress_01`.

**Stress modules:**
- **S3.1 — V1 Action enumeration.** Every faction action: cost, prerequisites, resolution mechanic, output state.
- **S3.2 — V3 Action-chain interactions.** Faction A's action at phase N affects faction B's available actions at phase N+1. Verify ordering and information visibility (open vs hidden actions).
- **S3.3 — V4 NERS.** Boundary: faction with no actions available (canonical handling). Crunch: every faction acts simultaneously and outcomes conflict. Optimal play: dominant action sequences.
- **S3.4 — V10 Dominant strategy probe.** Across all factions, is there a faction-type or action-sequence that strictly dominates?
- **S3.5 — V12 Narrative emergence.** Faction-level action outcomes legible as faction-character (e.g., does the Crown's behavior across a campaign read as Crown-like)?

**Canon gates.** `faction_actions.md` (24,168 chars) — full read required. PP-726 political hierarchy integrated.
**Open questions.** Are faction actions canonically open-info or hidden? Faction-AI priority for action selection — engine logic, since no GM.

---

#### S4 — Faction stats (1–7 scale)

**Description.** Numerical faction-state representation on a 1–7 scale (Mandate, Influence, etc.).
**Canonical.** `params/factions/stats_1_7_scale.md` (24,804 chars), canonical SHA pinned.
**Coupling.** S2/S3, all faction-layer mechanics.
**Prior coverage.** B1/B2 stressed Mandate/Influence values; canonical SHA established.
**Priority.** P2 — established surface; spot-check sufficient.
**Effort.** 0.5 session.
**Suite ID.** `S4_faction_stats_stress_01`.

**Stress modules:**
- **S4.1 — V1 Stat enumeration.** Every named stat: scale, source modifiers, drain modifiers, threshold effects.
- **S4.2 — V4 NERS.** Boundary: stat at 1 (canonical floor), stat at 7 (canonical ceiling). Cascade: simultaneous shift of multiple stats from single event.
- **S4.3 — V8 Convergence.** Can a faction stat cycle indefinitely between two values?

**Canon gates.** None new.

---

#### S5 — Claim Integrity (CI) / Mass Seizure

**Description.** CI clock, fill from Tensions, threshold for Mass Seizure availability, Seizure resolution.
**Canonical.** `params/bg/ci_seizure.md` (10,175 chars).
**Coupling.** Tensions (S6), Realm Stability (S10), Mass combat (S1), Coup Counter (S8), PI track (S17).
**Prior coverage.** B3/B4 CI/Mass Seizure timing verified. PT corrected (T9 PT=5 canonical). Hafenmark CI suppression PP-431-COR corrected in B4.
**Priority.** P2 — primary closed; edge re-stress on PP-716 propagation.
**Effort.** 1 session.
**Suite ID.** `S5_ci_seizure_extended_stress_01`.

**Stress modules:**
- **S5.1 — V3 Post-PP-716 propagation check.** Did wound-permanence shift affect any CI inputs? (PP-716 was combat-domain; expect no direct effect, but verify.)
- **S5.2 — V4 NERS extension.** Crunch: simultaneous Seizure attempts on multiple territories. Cascade: failed Seizure consequences (open finding ED-588/589 territory and **Seizure Failure consequences → Stability−1 + Casus Belli chain** [B4 gap #13]).
- **S5.3 — V8 Convergence.** Mass-Seizure → resolution → next-season state. Can a faction get stuck in indefinite pre-Seizure buildup?

**Canon gates.** Resolution of B4-gap-#13 (Seizure Failure consequences spec).

---

#### S6 — Tensions Deck

**Description.** 6 external bilateral cards, draw 2 per season, S8+ fuse-burning, fires escalate per-card.
**Canonical.** `designs/architecture/conflict_architecture_proposal.md` (the unified design, "Start here" per sim_coverage_index). Tensions-pair validation in `designs/architecture/tensions_pair_validation.md` (15/15 pass).
**Coupling.** S5 (CI fill), S10 (RS), S3 (faction actions), C1 (ignition).
**Prior coverage.** Analytical validation (15/15 pair coherence). **Never simulated.** Coverage matrix flags as "Proposed; pair validation passed analytically" — not engine-verified.
**Priority.** P1 (load-bearing for ignition, never simulated).
**Effort.** 1.5 sessions.
**Suite ID.** `S6_tensions_deck_stress_01`.

**Stress modules:**
- **S6.1 — V1 Deck spec validation.** 6 cards × bilateral target pairs × fire-effect. Enumerate and confirm fully specified.
- **S6.2 — V2 Probability distribution.** Draw-2-per-season distribution. Across S8–S20 horizon: P(specific card draws), P(any-fire), P(stacked-fire from same card across seasons).
- **S6.3 — V3 Interaction chain.** Card fires → CI advance → Seizure availability → mass combat / political consequence. End-to-end chain.
- **S6.4 — V4 NERS.** Boundary: all-cards-drawn-no-fire scenario (low-tension campaign). Cascade: multiple simultaneous fires same season. Ambiguity: card fires but target faction is non-viable (eliminated / merged).
- **S6.5 — V5 Full scenario.** S1–S30 campaign with Tensions Deck driving ignition. Verify ignition occurs in canonical S8–S12 window per `arc_test_batch3` reference timeline.
- **S6.6 — V10 Player dominant-strategy.** Can the player game card draws by stalling actions until favorable cards burn?

**Canon gates.** `conflict_architecture_proposal.md` read fully. Tensions Deck is the load-bearing ignition mechanism; the entire C1 setup-ignition suite depends on S6.

---

#### S7 — Accord / Treaty

**Description.** Inter-faction agreements with state and decay; treaty effects on Strain recovery.
**Canonical.** Referenced in `params/bg/` and B4 batch (Accord revolt cascade tested; **Treaty recovery absent** flagged as gap, B4 gap #14).
**Coupling.** S3, S5, S10, S6 (some Tensions cards reference treaties).
**Prior coverage.** B4 Accord revolt cascade Medium confidence; treaty mechanic gap surfaced.
**Priority.** P1 (gap surfaced, never resolved).
**Effort.** 1 session.
**Suite ID.** `S7_treaty_accord_stress_01`.

**Stress modules:**
- **S7.1 — V1 Treaty mechanic spec gap.** Open finding B4-#14: **Treaty interaction with Strain recovery**. Block stress until canon written; OR carve out subset.
- **S7.2 — V3 Accord revolt cascade re-stress.** Verify B4 Medium-confidence finding at full simulator fidelity (B4 used simplified-CI).
- **S7.3 — V4 NERS.** Boundary: treaty with 1 signatory (degenerate). Crunch: multi-party treaty with one defector. Cascade: treaty-violation chain.
- **S7.4 — V8 Convergence.** Can a treaty deadlock — both sides bound to incompatible actions?

**Canon gates.** Treaty/Strain canon (B4 gap #14) must resolve before S7.1.

---

#### S8 — Löwenritter Coup

**Description.** Coup mechanic for the Löwenritter faction; Coup Counter advances per canonical events; coup effect on Crown Mandate.
**Canonical.** Referenced in `params/bg/`, B4 batch.
**Coupling.** S3, S5, S10, S15 (succession), `conflict_architecture_proposal.md` graduated-autonomy variant.
**Prior coverage.** B4 Löwenritter Coup Medium confidence; **Counter advancement sources** (B4 gap #11) and **Coup effect on Crown Mandate** (B4 gap #12) flagged.
**Priority.** P1.
**Effort.** 1.5 sessions.
**Suite ID.** `S8_lowenritter_coup_stress_01`.

**Stress modules:**
- **S8.1 — Spec gap closure (B4 gaps #11, #12).** Before stress can run, define Counter-advancement source events and Coup-effect-on-Crown-Mandate canonically.
- **S8.2 — V1 Mechanism validation.** Counter fill rate per source, threshold to trigger, post-coup state.
- **S8.3 — V3 Interaction chain.** Coup event → Crown state shift → faction-action availability changes → potential cascade to other factions.
- **S8.4 — V4 NERS.** Boundary: coup attempt at minimum Counter, coup attempt with Crown at max preparation. Crunch: simultaneous internal Crown crisis + coup. Ambiguity: graduated-autonomy variant interaction (per `conflict_architecture_proposal.md`).
- **S8.5 — V12 Narrative emergence.** Coup as climactic narrative beat — does the engine produce coup events that read as story climaxes?

**Canon gates.** B4 gaps #11 + #12 closed. Graduated-autonomy variant decision (current `conflict_architecture_proposal` is the canonical replacement for binary coup, but verify integration).

---

#### S9 — Altonian Vanguard / IP

**Description.** External pressure mechanic. Imperial Pressure (IP) gauge; Altonian Vanguard deployment at IP threshold; AER generation mechanic.
**Canonical.** Referenced across `params/bg/` and B3/B4.
**Coupling.** S10 (RS decay drives IP), S1 (mass combat once deployed), S6 (Tensions external cards), S5 (CI suppression interactions).
**Prior coverage.** B3/B4 Medium confidence; **AER generation mechanic not in any read doc** (B4 gap #8); Warden emergence post-RS40 (B4 gap #9); Campaign-scale vs standard battle distinction (B4 gap #10).
**Priority.** P1 (gap-dense).
**Effort.** 2 sessions.
**Suite ID.** `S9_altonian_vanguard_stress_01`.

**Stress modules:**
- **S9.1 — Spec gap closure (B4 gaps #8, #9, #10).** AER generation, Warden emergence, campaign-vs-standard battle.
- **S9.2 — V1 IP gauge formula validation.** IP fill, drain, threshold for Vanguard deployment, T10→T1 advance schedule.
- **S9.3 — V3 Interaction chain.** RS decay → IP advance → Vanguard deployment → mass combat. End-to-end campaign-late-game chain.
- **S9.4 — V4 NERS.** Boundary: high-RS late-game (Vanguard non-deployment scenario), low-RS early-game (premature Vanguard? Canonical block?). Cascade: simultaneous internal crisis + Vanguard arrival.
- **S9.5 — V5 Full scenario.** S20–S30 campaign with Vanguard as primary external pressure. Match against B3 reference timeline.

**Canon gates.** Three B4 gaps closed.

---

#### S10 — Realm Stability (RS) decay

**Description.** Long-running clock representing kingdom-level stability; deterministic decay per B3.
**Canonical.** Referenced in `params/bg/`.
**Coupling.** Every strategic-layer event. Drives Vanguard deployment, victory checks.
**Prior coverage.** B3 verified RS decay; fully deterministic.
**Priority.** P2 — closed; re-stress only if a system-shift touches RS inputs.
**Effort.** 0.25 session (spot-check only).
**Suite ID.** `S10_rs_decay_recheck` (optional).

**Stress modules:** Spot-check RS-input set against current canon (PP-716, PP-724–726). Confirm no new RS sources unaccounted.

---

#### S11 — Royal Assassination

**Description.** Mechanic for assassination of royal NPCs (e.g., Almud's father per ignition analysis).
**Canonical.** `params/bg/royal_assassination.md` (2,642 chars — small; read in full).
**Coupling.** S15 (succession), S3 (Crown faction state), S6 (Tensions card potentially), C1 (ignition mechanism).
**Prior coverage.** None. Almud's father case discussed in ignition analysis (B4 design decision #7: "strike as backstory, make live via Royal Crisis card?" — unresolved).
**Priority.** P1.
**Effort.** 1 session.
**Suite ID.** `S11_royal_assassination_stress_01`.

**Stress modules:**
- **S11.1 — V1 Mechanism enumeration.** Trigger conditions, target eligibility, perpetrator-selection (canonical or emergent), post-event state cascade.
- **S11.2 — V3 Interaction chain.** Royal assassination → succession trigger (S15) → Crown faction Mandate shift → potential coup window (S8).
- **S11.3 — V4 NERS.** Boundary: no eligible heir, contested heir. Cascade: multi-royal-death scenarios.
- **S11.4 — V12 Narrative emergence.** Does an assassination read as a major narrative beat or as a state-machine trigger?

**Canon gates.** B4 decision #7 (Almud's father as live event vs backstory).

---

#### S12 — Bishop appointment

**Description.** Church faction appointment mechanic; per `conflict_architecture_proposal` proposed structure.
**Canonical.** `conflict_architecture_proposal.md` (proposed).
**Coupling.** Church faction state, S3 (faction action), S6 (Tensions interaction), W4 (Institutions).
**Prior coverage.** Proposed; not tested; **needs engine_v4** per coverage map.
**Priority.** P2 (proposed mechanic; depends on engine_v4 surface).
**Effort.** 1 session post-engine_v4.
**Suite ID.** `S12_bishop_appointment_stress_01` (deferred).

**Stress modules (when engine_v4 ready):**
- **S12.1 — V1 Appointment-mechanic spec.**
- **S12.2 — V3 Cross-faction-interaction chain.**
- **S12.3 — V4 NERS.**

**Canon gates.** Engine_v4 surface. `conflict_architecture_proposal` mechanic formalized into params/.

---

#### S13 — Graduated Löwenritter autonomy

**Description.** Replaces binary coup with graduated-autonomy state per `conflict_architecture_proposal`.
**Canonical.** `conflict_architecture_proposal.md`.
**Coupling.** S8 (replaces binary coup mechanic), S3.
**Prior coverage.** Proposed; not tested.
**Priority.** P2 (proposed).
**Effort.** 1 session post-canon.
**Suite ID.** `S13_lowenritter_graduated_stress_01` (deferred).

**Stress modules.** V1, V3, V4 against the graduated-state machine.
**Canon gates.** Formalization into `core.md` or dedicated params file (B4 spec patch #3).

---

#### S14 — Three-scale resolution architecture

**Description.** Architectural spec for three-scale resolution (per `conflict_architecture_proposal`). Structural — defines how scale-transitions resolve.
**Canonical.** `conflict_architecture_proposal.md`.
**Coupling.** E4 (scale transitions), all resolution layers.
**Prior coverage.** Proposed; structural; **needs engine_v4.**
**Priority.** P1 (structural; high blast radius).
**Effort.** 2 sessions post-engine_v4.
**Suite ID.** `S14_three_scale_architecture_stress_01` (deferred).

**Stress modules.** Architectural verification (V1, V3, V7) once engine_v4 surfaces exist.

---

#### S15 — Faction succession / Restoration Movement (RM) emergence

**Description.** Faction succession mechanic on member death/incapacitation; Restoration Movement faction emergence at Order=0 threshold.
**Canonical.** Referenced in B1/B2 batch, `faction_succession_split_v30 §4`.
**Coupling.** S3, S11, S2, threadwork (relationships of contenders).
**Prior coverage.** B1/B2 High confidence; Order=0 threshold validated; sim bugs fixed (RM Inf inflation, PV variance).
**Priority.** P2 — primary mechanics closed; specific gaps remain.
**Effort.** 1 session.
**Suite ID.** `S15_succession_rm_extended_stress_01`.

**Stress modules:**
- **S15.1 — Open finding closure.** SIM4-01 (ED-588) RM Phase 2 T9 holding condition unreachable. SIM4-02 (ED-589) RM Presence marker mechanics undefined. Block until canon written or carve out.
- **S15.2 — V3 Cross-system chain.** Royal assassination (S11) → succession → contested heir cascade → potential RM emergence.
- **S15.3 — V4 NERS extension.** Cascade: chain succession (heir dies before resolution). Ambiguity: contender from non-national faction (B1 finding restricted to national, confirm canon).
- **S15.4 — Open design decisions (B2).** Splinter Influence split (60/40 or unsplit) — Jordan decision required.

**Canon gates.** ED-588 + ED-589 resolution. B2 design decision on Splinter Influence split.

---

#### S16 — Hafenmark CI suppression

**Description.** Hafenmark-specific CI suppression mechanic; PP-431-COR canonical replacement.
**Canonical.** Referenced in B4, PP-431-COR.
**Coupling.** S5, S3 (Hafenmark faction).
**Prior coverage.** B4 High confidence post-PP-431-COR.
**Priority.** P3 — closed.
**Effort.** Recheck only if CI canon shifts.
**Suite ID.** N/A.

---

#### S17 — Parliament Integrity (PI) track

**Description.** Parliament-faction track; stability confirmed; upper-bound effects observed weak per B4.
**Canonical.** `params/bg/parliament.md` (7,115 chars).
**Coupling.** S3, S5, G2 (governance — see Layer G).
**Prior coverage.** B4 High confidence; upper-bound effects flagged weak (Full Parliament band trivially met — B4 gap #20).
**Priority.** P2.
**Effort.** 0.5 session.
**Suite ID.** `S17_pi_track_recheck`.

**Stress modules:**
- **S17.1 — V4 Upper-bound band effects.** Stress the Full-Parliament band specifically: is the effect canonical-strength or accidentally-trivial?
- **S17.2 — Open finding SIM5-01 (ED-616).** No Parliamentary block on Tribune actions. Spec gap.

**Canon gates.** ED-616 spec.

---

#### S18 — Royal Dispute Track / Throne Dispute (RDT/TD) track

**Description.** Track for royal/throne-level disputes.
**Canonical.** Referenced in B4. Specific params file location TBD.
**Coupling.** S3, S15, S11, S5.
**Prior coverage.** B4 Medium confidence; simplified-CI model.
**Priority.** P2.
**Effort.** 1 session.
**Suite ID.** `S18_rdt_td_stress_01`.

**Stress modules:**
- **S18.1 — V1 Re-validate at full-fidelity CI** (B4 used simplified).
- **S18.2 — V3 Cross-track interaction with PI, CI.**
- **S18.3 — V4 NERS.**

**Canon gates.** Locate canonical params file for RDT/TD.

---

### LAYER W — World substrate

#### W1 — Geography

**Description.** Peninsular map, territories, terrain types, sea zones.
**Canonical.** `params/bg/geography.md` (26,470 chars), `designs/world/geography_v30_infill.md` (5,454 chars), `designs/territory/valoria_geography_v30.yaml` (35,053 chars).
**Coupling.** Every territory-scale system. S1 (mass combat terrain), W2 (settlement adjacency on geography), S9 (Vanguard routes).
**Prior coverage.** `geography_phase4_stress_01` 2026-05-10 — Phase 3 land-based verified (Mountain Pass, cavalry, coastal landing); **Phase 4 P1 gap on ED-055 sea-zone adjacency.**
**Priority.** P1.
**Effort.** 1 session (Phase 4 deferred items + ED-055).
**Suite ID.** `W1_geography_phase4_extended_stress_01`.

**Stress modules:**
- **W1.1 — ED-055 closure.** Author canonical sea-zone polygon + adjacency definition. Then run amphibious-scenarios stress.
- **W1.2 — V4 Terrain NERS.** Boundary: territory with no land-route (island? exclave?). Cascade: cross-terrain movement when terrain effects compound (river + mountain + forest).
- **W1.3 — V7 Cross-scale terrain consistency.** Terrain at territory scale must be coherent at settlement scale (settlement in forested territory has forest-flavored scenes).

**Canon gates.** ED-055 spec.

---

#### W2 — Settlement adjacency / Settlement Registry

**Description.** Per-settlement adjacency graph; PP-726 ratified 37-settlement registry; 55 canonical adjacency edges.
**Canonical.** `designs/territory/settlement_layer_v30.md` (canonical SHA `PENDING_PP_726`), PP-726 commit.
**Coupling.** W1, S1 (mass-combat routes), S15 (succession contender pools), all settlement-scale resolution.
**Prior coverage.** PP-724 + PP-726 ratified canon. **Adjacency stress at correct granularity never run** (PP-723 ran at wrong granularity; superseded).
**Priority.** P1.
**Effort.** 1 session.
**Suite ID.** `W2_settlement_adjacency_stress_01`.

**Stress modules:**
- **W2.1 — V1 Graph validation.** 37 nodes, 55 edges (28 intra-province + 24 primary inter-province + 1 sea + 2 second-routes). Verify every settlement ≥2 connections (Schoenland foreign-exempt).
- **W2.2 — V3 Pathfinding.** All-pairs shortest-path. Verify no orphans. Verify diameter is reasonable for game pacing.
- **W2.3 — V4 NERS.** Boundary: degree-1 settlements (foreign-exempt Schoenland — already; any others?). Crunch: edge removal (e.g., due to faction control flip) — does graph remain connected?
- **W2.4 — V7 Cross-scale.** Settlement at personal scale (named NPCs) ↔ settlement at strategic scale (territory holder).
- **W2.5 — Update canonical_sources.yaml.** Replace `PENDING_PP_726` placeholder with actual SHA.

**Canon gates.** Update `canonical_sources.yaml` SHA.

---

#### W3 — Fractional province ownership

**Description.** Province ownership at fractional granularity (multiple factions hold parts of one province).
**Canonical.** `fractional_province_ownership_v30 §2.6` (referenced in coverage map).
**Coupling.** S3, W2, S15.
**Prior coverage.** B1/B2 High confidence; **B2 spec patch ready: secession candidates restricted to national factions.**
**Priority.** P2 — primary closed; spec patch pending.
**Effort.** 0.25 session (commit spec patch).
**Suite ID.** N/A — spec patch commit only.

---

#### W4 — Institutions

**Description.** Institutional state (Church, Crown, guilds, etc.).
**Canonical.** `params/bg/institutions.md` (19,509 chars).
**Coupling.** S3, S12 (bishop), W5 (ministry), governance.
**Prior coverage.** ED-612 (Guilds) resolved per recent batch. General institutions surface not stressed.
**Priority.** P2.
**Effort.** 1 session.
**Suite ID.** `W4_institutions_stress_01`.

**Stress modules:**
- **W4.1 — V1 Institution enumeration.** Canonical list with state, change drivers, effect-on-factions.
- **W4.2 — V3 Institution-faction interaction chains.**
- **W4.3 — V4 NERS.** Boundary: institution at minimum/maximum state.

**Canon gates.** `institutions.md` read fully.

---

#### W5 — Ministry

**Description.** Crown administrative structure (likely; verify against canon).
**Canonical.** `params/bg/ministry.md` (13,950 chars).
**Coupling.** S3 (Crown faction), W4, S17 (parliament).
**Prior coverage.** None stress-suite.
**Priority.** P2.
**Effort.** 1 session.
**Suite ID.** `W5_ministry_stress_01`.

**Stress modules:**
- **W5.1 — V1 Ministry enumeration.**
- **W5.2 — V3 Ministry-action chain.**
- **W5.3 — V4 NERS.**

**Canon gates.** `ministry.md` read fully.

---

#### W6 — NPC behavior / Priority trees

**Description.** Per-NPC priority tree driving action selection; engine-driven NPC behavior (no GM).
**Canonical.** `params/bg/npc_priority_trees.md` (15,397 chars), `designs/npcs/npc_behavior_v30_infill.md` (19,327 chars).
**Coupling.** Every NPC-driven decision. S2/S3 (faction-allegiance behavior), threadwork (P5), conviction (P6), social contest (P3).
**Prior coverage.** Coverage matrix Medium-Low (priority-tree edge cases surface in B3/B4 findings; never explicit stress).
**Priority.** P1 (load-bearing; "no GM" makes this engine-critical).
**Effort.** 2 sessions.
**Suite ID.** `W6_npc_priority_trees_stress_01`.

**Stress modules:**
- **W6.1 — V1 Priority enumeration.** Every named NPC priority. Threshold conditions. Action set.
- **W6.2 — V3 Priority interaction chain.** Priority A triggers action that changes state used by Priority B; verify no priority-order pathologies.
- **W6.3 — V4 NERS.** Boundary: NPC with all priorities tied (canonical tiebreak). Crunch: simultaneous priority firing. Ambiguity: priority spec gaps.
- **W6.4 — Open finding SIM3-04 (ED-586).** Arc state vs Priority 6 at Mandate < 3.
- **W6.5 — V11 NPC coherence cross-cut.** Does the priority tree produce behavior that reads as character?
- **W6.6 — Crown priority tree at T2 Kronmark** (B3 design decision #6).

**Canon gates.** ED-586 closure. B3 decision #6.

---

#### W7 — Special NPCs

**Description.** Named NPCs with bespoke behavior outside generic priority trees.
**Canonical.** `params/bg/npcs_special.md` (6,001 chars).
**Coupling.** W6 (override), threadwork, faction-personal.
**Prior coverage.** Some named-NPC findings in B3/B4 (Almud, Yrsa Vossen, Torben referenced).
**Priority.** P2.
**Effort.** 1 session.
**Suite ID.** `W7_special_npcs_stress_01`.

**Stress modules:**
- **W7.1 — V1 Enumerate special NPCs and their bespoke logic.**
- **W7.2 — V3 Bespoke-vs-generic interaction.** What happens when a special NPC also matches a generic priority?
- **W7.3 — Open finding SIM5-04 (ED-618).** Torben Conviction window S1–8 formal def.

**Canon gates.** ED-618 closure (formal def).

---

### LAYER G — Governance / Editorial

#### G1 — ED (Editorial Decision) resolutions

**Description.** Editorial-decision mechanic at strategic scale (in-game ED, not the repo ED ledger).
**Canonical.** `params/bg/ed_resolutions.md` (10,401 chars).
**Coupling.** S3 (faction actions), S17 (parliament).
**Prior coverage.** None stress-suite.
**Priority.** P2.
**Effort.** 1 session.
**Suite ID.** `G1_ed_resolutions_stress_01`.

**Stress modules:**
- **G1.1 — V1 ED-resolution mechanic.**
- **G1.2 — V3 ED-resolution → faction-state cascade.**
- **G1.3 — V4 NERS.** Crunch: simultaneous ED resolutions. Cascade: ED outcome triggers another ED.

**Canon gates.** `ed_resolutions.md` read fully.

---

#### G2 — Parliament (Tribune, Tribune blocks)

**Description.** Parliamentary actions, Tribune mechanic, tribune blocks.
**Canonical.** `params/bg/parliament.md` (7,115 chars).
**Coupling.** S17 (PI track), S3, G1.
**Prior coverage.** B4 PI track verified; parliamentary-specifics not stressed.
**Priority.** P1 (open finding ED-616).
**Effort.** 1 session.
**Suite ID.** `G2_parliament_stress_01`.

**Stress modules:**
- **G2.1 — Open finding SIM5-01 (ED-616).** No Parliamentary block on Tribune actions — spec gap.
- **G2.2 — V1 Action enumeration** — Tribune actions, parliamentary actions, voting mechanic.
- **G2.3 — V3 Tribune-action → PI-track interaction chain.**
- **G2.4 — V4 NERS.** Boundary: parliament with deadlock. Crunch: simultaneous tribune challenges.

**Canon gates.** ED-616 spec.

---

#### G3 — Victory conditions

**Description.** Win/loss conditions; shared-loss possibility.
**Canonical.** `designs/provincial/victory_v30.md` (canonical SHA `75810e78`), `params/bg/victory.md` (12,534 chars).
**Coupling.** S10 (RS endgame collapse), S9 (Vanguard endgame), every faction long-term goal.
**Prior coverage.** AUD-VIC referenced as resolved. Victory architecture audit `tests/audit/audit_victory_architecture_v1.md` (25,277 chars).
**Priority.** P2.
**Effort.** 0.5 session.
**Suite ID.** `G3_victory_recheck`.

**Stress modules:**
- **G3.1 — V1 Victory-condition enumeration.** Verify canonical list against current `victory_v30` SHA.
- **G3.2 — V5 Full scenario.** Run campaigns to endgame; verify shared-loss can trigger; verify each named victory path is reachable.
- **G3.3 — V8 Convergence.** Does every campaign terminate in a victory state?

**Canon gates.** None new.

---

### LAYER C — Cross-system / emergent

#### C1 — Setup & ignition (next planned per combat suite completion)

**Description.** Game-setup and early-game ignition. Flagged "next" per combat-suite completion ("Ready to proceed: A → F → G").
**Canonical.** `designs/architecture/conflict_architecture_proposal.md`, `early_game_ignition_analysis.md` [SUPERSEDED — §2 mechanisms-list valid as reference].
**Coupling.** S6 (Tensions Deck — load-bearing for ignition), S11 (royal assassination as ignition mechanism), W3 (5 fractional provinces at start), S5 (CI buildup), W6 (NPC priorities seeding actions).
**Prior coverage.** B3 reference timeline; conflict_architecture proposal not engine-verified.
**Priority.** P0 (game can't play without correct setup; flagged as next sim).
**Effort.** 2 sessions.
**Suite ID.** `G_setup_ignition_stress_01` (suite letter **G**).

**Stress modules:**
- **G.1 — V1 Initial-state spec.** Canonical S0 state: 5 fractional provinces, faction positions, NPC dispositions, clock starts, deck state.
- **G.2 — V3 Ignition-mechanism interaction chain.** Six canonical ignition mechanisms (per superseded analysis §2) × current Tensions Deck × initial conditions → ignition event.
- **G.3 — V5 Full scenario S1–S12.** Drive 10+ campaigns from S0; verify ignition fires in S8–S12 canonical window per B3 reference. Variance characterization across seeds.
- **G.4 — V4 NERS.** Boundary: campaign with all-cooperative initial dispositions (does ignition still fire?). Crunch: all six mechanisms primed simultaneously. Ambiguity: ignition-event ambiguity (which mechanism "fired"?).
- **G.5 — V12 Narrative emergence.** Does the early game read as escalating tension or as state-machine pre-trigger?
- **G.6 — Open design decisions blocked here.**
  - B1 #4 Splinter Influence split (60/40 or unsplit)
  - B3 #5 CI seasonal cap vs Piety Yield at T9
  - B3 #6 T2 Kronmark garrison (explicit priority entry or accept exposed)
  - B4 #7 Almud's father (backstory or live)

**Canon gates.** Tensions Deck spec (S6) — load-bearing. Initial-state canonical specification.

---

#### C2 — Campaign arc shape

**Description.** Multi-season arc shape across S1–S30+. Reference timeline established in B3.
**Canonical.** B3 reference timeline (in `sim_coverage_index`).
**Coupling.** Everything; this is the integrative test surface.
**Prior coverage.** B3 single-pass reference established; variance characterization weak.
**Priority.** P1.
**Effort.** 3 sessions (long sims).
**Suite ID.** `C2_campaign_arc_stress_01`.

**Stress modules:**
- **C2.1 — V5 Reference replication.** Drive 10+ campaigns end-to-end. Verify all 7 season bands (S1–S4 / S4–S8 / S8–S12 / S12–S18 / S18–S22 / S22–S28 / S28+) realized.
- **C2.2 — V2 Variance characterization.** Distribution across seeds: P(ignition by S12), P(seizure by S15), P(vanguard by S25), P(victory by S35).
- **C2.3 — V4 Pathological-campaign edge cases.** No-ignition campaign (does the engine terminate it correctly?), all-three-duchies-secede campaign, all-factions-allied campaign.
- **C2.4 — V12 Narrative emergence.** Across 10 campaigns, do narrative-summary outputs (per Mode E coverage matrices) read distinctly?

**Canon gates.** Most upstream-system stresses complete (G, S1, S3, S5, S6, S9, S10).

---

#### C3 — Narrative emergence coherence

**Description.** Does the game produce engaging emergent narrative? Per `<intent_of_game>` foundational goal.
**Canonical.** `<intent_of_game>` clause: "positive feedback loop between player decisions and mechanics/system/designs that produces an engaging game world with emergent narratives."
**Coupling.** P3 (social contest as character beat), P5 (threadwork — signature emergent-narrative system), P6 (conviction), S8 (coup as climactic), S11 (royal assassination), C2 (arc shape).
**Prior coverage.** Implicit in every Mode-E coverage matrix. Never explicitly stress-tested as a coherence surface.
**Priority.** P1 (foundational goal).
**Effort.** 2 sessions.
**Suite ID.** `C3_narrative_emergence_stress_01`.

**Stress modules:**
- **C3.1 — V12 Beat density.** Across 5 campaigns, count narrative beats (knot ruptures, coup attempts, assassinations, succession events, parliamentary crises). Verify beat density reads as engaging-narrative pacing, not state-machine event-storm.
- **C3.2 — V12 Beat coherence.** For 10 randomly-sampled beats, evaluate whether the beat reads as character-driven story or as mechanical artifact.
- **C3.3 — V11 Cross-NPC behavior coherence.** For 5 named NPCs across 3 campaigns, evaluate whether per-NPC behavior reads as the same character (consistency) and as evolving over time (development).
- **C3.4 — V10 Player-engagement probe.** Are there mechanically-optimal play patterns that produce narratively-degenerate outcomes? (Dominant-strategy emergent-narrative interaction.)

**Canon gates.** P5 threadwork stress complete (P5.6 narrative emergence is direct upstream).

---

#### C4 — Scale-transition seams

**Description.** Specific stress on the seam between scales: state that should propagate but doesn't, state that does but shouldn't.
**Canonical.** `params/scale_transitions.md`.
**Coupling.** E4 (general scale transitions), every cross-scale system.
**Prior coverage.** E4 covers the general transition surface. C4 is targeted seam-stress (after E4 establishes baseline).
**Priority.** P2 (depends on E4).
**Effort.** 1 session.
**Suite ID.** `C4_scale_seam_stress_01`.

**Stress modules:**
- **C4.1 — V3 Personal→strategic propagation.** A personal-scale outcome (a duel result, a Wager outcome, a threadwork rupture) that should affect strategic-layer state — verify it does, with correct delay/timing.
- **C4.2 — V3 Strategic→personal propagation.** A strategic decision (Mass Seizure declared) that creates personal-scale scene opportunities — verify the engine generates appropriate scenes.
- **C4.3 — Open finding SIM3-07 (ED-587).** Stability Crisis Zoom In trigger absent — specific seam stress.

**Canon gates.** E4 complete. ED-587 spec.

---

#### C5 — Save/load mid-mechanic

**Description.** Persistence stress. What state must serialize? What can be re-derived? Player saves mid-mechanic.
**Canonical.** **No canonical spec yet** — engine_v4 surface.
**Coupling.** Every mechanic with state spanning multiple player decisions.
**Prior coverage.** None.
**Priority.** P1 (videogame essential).
**Effort.** 1 session (post-engine_v4).
**Suite ID.** `C5_persistence_stress_01` (deferred until engine_v4).

**Stress modules (when engine_v4 ready):**
- **C5.1 — V9 Save-load matrix.** For every system, identify save-boundaries and verify state survives.
- **C5.2 — V9 Mid-mechanic save.** Save mid-combat, mid-fieldwork, mid-phase. Reload and verify.
- **C5.3 — V9 Out-of-order replay.** Save → take action A → reload → take action B. Verify reload state is identical, not contaminated by A.

**Canon gates.** Engine_v4 persistence surface.

---

#### C6 — Player dominant-strategy probe

**Description.** Cross-system game-theory. Are there strategies that strictly dominate?
**Canonical.** Implicit; per `<robust>` definition "allows player to think strategically; allows customization."
**Coupling.** Every player-decision surface.
**Prior coverage.** Per-system V10 modules (S3.4, S6.6, P2.4, others). C6 aggregates.
**Priority.** P2 (depends on per-system V10s).
**Effort.** 2 sessions.
**Suite ID.** `C6_dominant_strategy_stress_01`.

**Stress modules:**
- **C6.1 — V10 Cross-system dominance.** Combine per-system dominant-strategy findings; identify cross-system strategies (combine S3 action + S5 timing + S6 deck-state) that exploit interactions.
- **C6.2 — V10 Reverse-design.** Given each victory condition (G3), back-derive optimal strategy and compare against canonical play archetypes.

**Canon gates.** Per-system V10s complete.

---

## 5. Phase ordering & critical path

### Phase 0 — Prerequisites (§0.4)

Repository-level cleanup. Editorial-ledger archive auto-fix, file_index_summary regeneration, freshness gate update, canonical_sources SHA drift remediation, ED-055 spec, B4 gap closures (#8 #9 #10 #11 #12 #13 #14), ED-586/587/588/589/616/617/618/619, PP-726 SHA pin update, PAT rotation, prior session checkpoint commit.

**Cannot be a single session** — these are heterogeneous. Group into:

- **Phase 0a** — Repo hygiene (archive auto-fix, file_index, freshness, SHA pin, ledger).
- **Phase 0b** — Spec-gap closures (8 B-batch gaps + 8 EDs). Each gap is one session.

### Phase 1 — Engine substrate

E1 (Dice) → E2 (Clocks) → E3 (Phases) → E4 (Scale transitions) → E5 (Campaign modes).
Sequence matters: E1 → E2 → E3 → E4 → E5. Each enables stress on dependent systems. E1 + E2 + E3 are foundational; E4 is structural; E5 is configuration.

**Phase-1 total: ~6 sessions.**

### Phase 2 — Personal-scale completion

P1 deferred refinements (combat — optional) → P2 (Contest general) → P3 (Social contest) → P5 (Threadwork) → P6 (Conviction extended).
P4 (Fieldwork) closed.

**Phase-2 total: ~5 sessions (P2/P3/P5/P6) + optional 1 (P1 deferred).**

### Phase 3 — Strategic-scale Tier 1 (load-bearing)

S6 (Tensions Deck — gates C1) → S1 (Mass combat) → S9 (Vanguard — gap-dense) → S3 (Factions strategic) → S8 (Löwenritter coup) → S11 (Royal assassination).

**Phase-3 total: ~10 sessions.**

### Phase 4 — World substrate

W1 (Geography Phase 4 + ED-055) → W2 (Settlement adjacency at PP-726 granularity) → W6 (NPC priority trees) → W7 (Special NPCs).
Lower-priority: W3 (Fractional ownership — spec patch only), W4 (Institutions), W5 (Ministry).

**Phase-4 total: ~7 sessions (W1/W2/W6/W7) + 3 (W3/W4/W5 lower priority).**

### Phase 5 — Strategic-scale Tier 2 + Governance

S2 (Factions personal) → S4 (Faction stats — light) → S5 (CI extended) → S7 (Treaty — post-gap-#14) → S15 (Succession extended) → S17 (PI track recheck) → S18 (RDT/TD) → G1 (ED resolutions) → G2 (Parliament — post-ED-616) → G3 (Victory recheck).

**Phase-5 total: ~9 sessions.**

### Phase 6 — Emergent / cross-system

C1 (Setup & ignition — gates everything else for full-arc replay) → C2 (Campaign arc) → C3 (Narrative emergence) → C4 (Scale-transition seams) → C6 (Dominant-strategy) → S10 (RS recheck spot-check).

**Phase-6 total: ~9 sessions.**

### Phase 7 — Engine_v4-deferred

S12 (Bishop appointment), S13 (Graduated Löwenritter autonomy), S14 (Three-scale architecture), C5 (Persistence stress).

**Phase-7 total: ~5 sessions post-engine_v4.**

### Critical-path summary

**Total estimated sessions: ~55–65** (excluding Phase 7 engine_v4-deferred and excluding open-ended per-session retries on hook fires).

**Critical path:** Phase 0 → E1 → E2 → E3 → E4 → S6 → C1 → C2. Other phases parallelizable across this critical path once Phase 0 + Phase 1 complete.

---

## 6. Per-phase session sketches

### Session-one recommended starting point

**Phase 0a: Repo hygiene single-session bundle.**
1. Editorial-ledger archive auto-fix (`atomizer.archive_by_status` manual invocation, commit).
2. file_index_summary regeneration (whatever tool produces it; verify against repo state).
3. `freshness_gate.py --update` for the 1 stale canonical source.
4. PP-726 canonical-sha update for `designs/territory/settlement_layer_v30.md` (currently `PENDING_PP_726`).
5. Combat/derived_stats registry drift remediation (per `combat_arch_residual_stress_01/module_manifest.md` §"Registry drift").
6. Confirm `read_active_sessions` fix priority — patch or document fallback as canonical.
7. Commit prior session's improvement_avenues file or discard.
8. PAT rotation (Jordan side; out-of-session).

Single session, ~3 hours. Unblocks every downstream stress.

### Session-two recommended

**Phase 0b: First spec-gap closure session.**

Pick the gap with the lowest blast radius / clearest constraint set. Recommendation: **ED-055 naval scope** — blocks W1 + S1 (S1.5 carve-out). Single decision, follow-on PP commit.

### Session-three recommended

**Phase 1 / E1 — Dice/TN/Degree stress.** Foundation; one session bundle; produces verification commit. Followed by E2/E3/E4 in sequence.

### Parallelization windows

Once Phase 1 (E-suite) complete, the following can run in parallel sessions (different scopes):
- Phase 2 (Personal-scale) — `editorial` or `design` scope.
- Phase 4 (World substrate) — independent of personal-scale work.
- Phase 0b gap-closure follow-ons — `editorial`.

Phase 3 (strategic) should not parallelize until S6 (Tensions Deck) is verified — S6 gates most downstream Phase 3 modules.

---

## 7. Open questions for Jordan (canon settlements required)

These block specific stress modules. Ordered by blast radius.

| # | Decision | Blocks | Priority |
|---|---|---|---|
| Q1 | ED-055 naval scope (sea-zone polygon + adjacency) | W1, S1 (coastal) | P1 |
| Q2 | B4 #11 Coup Counter advancement source events | S8 | P1 |
| Q3 | B4 #12 Coup effect on Crown Mandate | S8 | P1 |
| Q4 | B4 #13 Seizure Failure consequences (Stability−1 + Casus Belli chain) | S5 extended | P1 |
| Q5 | B4 #14 Treaty mechanic × Strain recovery | S7 | P1 |
| Q6 | B4 #8 AER generation mechanic | S9 | P1 |
| Q7 | B4 #9 Warden emergence behavior post-RS40 | S9 | P1 |
| Q8 | B4 #10 Campaign-scale vs standard battle distinction | S9, S1 | P1 |
| Q9 | ED-586 Arc state vs Priority 6 at Mandate < 3 | W6 | P2 |
| Q10 | ED-587 Stability Crisis Zoom In trigger | C4 | P2 |
| Q11 | ED-588 RM Phase 2 T9 holding condition | S15 | P2 |
| Q12 | ED-589 RM Presence marker mechanics | S15 | P2 |
| Q13 | ED-616 Parliamentary block on Tribune actions | G2 | P2 |
| Q14 | ED-617 Grand Contest Recall once-per-source | P2 (Contest) | P2 |
| Q15 | ED-618 Torben Conviction window S1–8 formal def | W7 (special NPCs), P6 | P2 |
| Q16 | ED-619 3-Obligation GM advisory cap → engine logic (no GM in videogame) | E-layer | P2 |
| Q17 | B1 #4 Splinter Influence split (60/40 or unsplit) | S15 | P2 |
| Q18 | B3 #5 CI seasonal cap vs Piety Yield at T9 | S5 | P2 |
| Q19 | B3 #6 T2 Kronmark garrison priority entry | W6 | P2 |
| Q20 | B4 #7 Almud's father (backstory or Royal Crisis card) | S11, C1 | P2 |
| Q21 | E1 — non-d10-pool resolution mechanics anywhere in canon? | E1 | P0 (clarification) |
| Q22 | E2 — unified clock state machine or per-system implementations? | E2 | P0 (clarification) |
| Q23 | E3 — tracks orthogonal or coupled? | E3 | P0 (clarification) |
| Q24 | E4 — four scales fully canonical or P/S only with subdivisions? | E4 | P1 (clarification) |
| Q25 | S3 — faction actions canonically open-info or hidden? | S3 | P1 (clarification) |

**Recommendation.** Q21–Q25 are clarification-only (Jordan responds with current canon understanding; no design work). Resolve those first. Q1–Q8 are design work; sequence by Phase priority.

---

## 8. Out of scope (explicit)

To prevent scope creep, the following are deliberately excluded from this workplan:

- **Engine_v4 implementation.** This workplan stresses mechanics-on-paper. Engine surfaces (persistence, threading, UI bindings) are out-of-scope until engine_v4 lands; then C5, S12, S13, S14 unblock.
- **Asset pipeline.** Art, audio, animation, localization. No stress vector applies.
- **GDScript-level testing.** Unit tests for GDScript classes belong in `valoria-game` repo and are separate from this design-stress effort.
- **Network / multiplayer.** Valoria is single-player per current architecture.
- **AI/ML system implementation.** NPC behavior stress (V11) evaluates priority-tree coherence, not LLM-driven behavior.
- **Modding surface.** Out of scope until 1.0.
- **Steam / platform integration.** Out of scope.
- **Balance tuning.** Stress identifies surfaces that work or break, not surfaces that need numerical retuning. Balance is a separate pass post-stress.
- **Lore-only systems.** Pure narrative content without mechanical surface (e.g., named-place history) is not stressed unless coupled to a mechanic (e.g., a place that grants a faction bonus).

---

## 9. Risks / anti-patterns to avoid

From prior stress work and session-log open_items:

1. **Re-deriving from scratch when canon is mature.** Combat R3, R5, R8 had synthesis-premises that were partially obsolete because canon was already mature. Always fetch and read canonical params before assuming a gap exists.
2. **Skill non-fetch.** A prior session "produced a full sim from scratch, ignoring the existing harness and anti-patterns, because the simulator skill was never fetched." `task_gate('simulation')` now enforces fetch — do not bypass.
3. **Granularity drift.** PP-723 modeled districts as siege-target settlements when the canonical level was settlement-as-siege-target. PP-726 supersedes. Verify canonical granularity before any structural simulation.
4. **Pre-commit verification skipped on multi-step work.** R1 was caught post-commit (off-by-one in m_summary). Self-review off-by-one detection was load-bearing this prior session. Verify before commit, every time.
5. **Auto-commit during bootstrap.** Previous bootstrap auto-committed `atomizer.archive_by_status` output and wiped 7 active P2 editorial entries (commits `a8f7b2f8`, `1df4259b`). Auto-commit during non-interactive bootstrap is too high-risk. Manual fixes only — current canon.
6. **Memory substitution for fetch.** "GitHub > memory" — the core rule. Never assume a mechanic value, name, or path from memory.
7. **Parallel-session collision without read_active_sessions.** Currently fetch-head OID is the working fallback; prior session had a parallel session through it that was missed. Until read_active_sessions is fixed (Phase 0a), assume serial work or accept fetch-head-OID collision recovery overhead.
8. **Hook bypass.** `--no-verify` is a defect, not a workflow. If a hook fires, investigate the input or the hook itself.

---

## 10. Changelog

- **V1.0 (2026-05-10).** Initial authorship. Post-bootstrap, post-`context_gate` fix commit `b7f0ad7`. Canonical sources read: simulator SKILL, mechanic-audit SKILL, coverage_matrix, sim_coverage_index, combat manifest, fieldwork stress, workplan_rebuild_2026-04-19 (format exemplar), canonical_sources.yaml (systems registry).

---

`[SELF-AUTHORED — bias risk]` This workplan was authored in the same session as the canonical-sources read. Independent reviewer would likely add: (a) explicit prioritization criteria (this workplan ranks by gap-density and load-bearing-ness; alternative criteria like player-visibility-priority or engine-surface-readiness would produce a different ordering); (b) estimated effort numbers are educated guesses based on prior-suite session counts and should be validated against actual per-system specification complexity; (c) no per-system risk-of-cascading-canon-shift analysis (a stress finding in S6 might cascade to revise C1 plans — the workplan acknowledges this only structurally via "canon gates," not quantitatively).

`[ASSUMPTION: Letter-prefix suite convention (A/F/G/R-suite + new P/S/W/G/C/E letters) is acceptable — basis: existing harness uses A, F, G, R; extension to other letters is a workplan-authoring decision Jordan can override. CONFIDENCE: medium]`

`[ASSUMPTION: ~55–65 session estimate excludes hook-fire retries and Jordan-decision wait-time — basis: completed suites averaged ~1 session per stress module of moderate complexity. CONFIDENCE: low — high variance across systems]`

`[GAP: Q21–Q25 (clarification questions) should be answered before fine-grained per-system stress planning is finalized — these answers may collapse or split system entries.]`
