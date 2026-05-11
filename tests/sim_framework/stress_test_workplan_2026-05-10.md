---
title: Valoria Mechanical Systems — Comprehensive Stress-Test Workplan
date: 2026-05-10
scope: every-system
status: planning
revision: V1.1
revision_basis: stress_workplan_resolutions_2026-05-10.md (Jordan directive 'resolve all, no naval')
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
9. **Canonize Battle Scale 5-tier table** (`params/mass_combat.md:223`) — strip [PROPOSAL] marker. Per Q8 resolution.
10. **Author Crisis Scene catalog** (~6–12 templates) for Stability-Crisis Zoom-In trigger (Q10 resolution).
11. **Commit Influence-split 60/40 spec patch** (B2 ready; Q17 resolution; same 60/40 rule extends to Wealth/Military pending balance test).

Items 1–4 are repo-level. Items 5–6 are infrastructure. Items 7–8 are housekeeping. Items 9–11 are V1.1 canonization tasks deriving from Q-resolutions. None block this workplan's authoring, but they block reproducible stress execution.

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
- **E1.1 — V1 Formula validation.** Reproduce EV/die across 1d–20d for **all canonical TN variants**. Per Q21: default TN 7 (EV 0.4); TN 6 for Volley Phase (`params/mass_combat.md` PP-503 Power-stat ranged); TN 8 for rushed pre-contest prep. Verify boundary outputs: pool=0 (auto-fail or impossible?), pool=1 (canonical bounds: −1 / 0 / +1 / +2), pool ≥ 20 (verify the engine doesn't truncate or overflow). Additional gate: full grep across `params/` for any `TN \d` token not already enumerated; surface as V1.1.update if found.
- **E1.2 — V2 Probability distribution.** Full distribution tables for {TN 6, TN 7, TN 8} × {1d, 3d, 5d, 7d, 10d, 15d, 20d}. Verify P(net ≥ 0), P(net ≥ +N) for N ∈ {0, 1, 2, 3, 5, 8}. Cross-check against any degree-table assumptions in `combat.md` and `contest.md`.
- **E1.3 — V4 NERS edge cases.** Boundary: pool=0 behavior, pool=1 lone-die, max canonical pool (verify there is one). Crunch: simultaneous +2/−1 from a single die — does a 10 also fail the 1-counting? Ambiguity: re-rolls (do any mechanics grant them?), bonus dice, exploding-on-10. Optimal play: when does adding +1D have diminishing return vs +1 TN swing?
- **E1.4 — V6 Coverage matrix.** Pool × TN × modifier-stack × situational-bonus (advantage / disadvantage if applicable). Verify the resolution surface is closed under composition.
- **E1.5 — V11 Obligation cap UI flow (engine logic).** Per Q16 resolution. Engine-side stress: when a character would acquire a 4th Obligation, the engine surfaces a forced-choice UI prompt (retire existing / dissolve via Wager / decline new). Verify: (a) all three player paths reach a canonical resolution; (b) state transitions are atomic (no partial Obligation state); (c) decline path leaves the offered Obligation cleanly closed without ghost-state; (d) dissolve-via-Wager invokes F1 Wager mechanic correctly per fieldwork canon.

**Canon gates.** None — dice are foundational. **TN-variant enumeration** (Q21 resolution) lists TN 6 / TN 7 / TN 8 as the canonical set.
**Open questions.** RESOLVED via Q21: the d10 pool is universal; TN varies (6 / 7 / 8). E1.1 includes a grep-sweep gate to catch any unenumerated TN.

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
- **E2.1 — V1 Formula validation per clock.** Canonical clock set (per Q22 resolution — per-system implementations sharing a common 0–100 / banded-effects convention): MS (Mending Stability), CI (Church Influence), IP (Invasion Pressure), PI (Parliamentary Integrity), RDT (Reformed Doctrine Track), TD (Theological Dissatisfaction), WC (Warden Cooperation), WR (Warden Recognition), Torben Loyalty, Elske Loyalty, Patience Counters (Varfell), Coup Counter [REMOVED per Q2 — replaced by Löwenritter Graduated Autonomy state machine, not a clock]. For each: declare canonical bounds, fill rate (per source), drain rate, trigger threshold, post-trigger behavior.
- **E2.2 — V3 Interaction chain.** When multiple clocks fill from the same source event (e.g., a Seizure attempt advances CI, may advance RS, may interact with Coup Counter). Verify ordering is canonical.
- **E2.3 — V4 NERS edge cases.** Boundary: clock at 0 with negative input — does it stay at 0 or wrap? Cascade: simultaneous trigger on multiple clocks. Crunch: clock fully fills and over-fills in a single event — does overflow carry? Optimal play: can a player intentionally stall a clock by avoiding source events?
- **E2.4 — V8 Convergence.** Does every active clock eventually resolve? Are there pathological inputs where a clock stalls indefinitely?
- **E2.5 — V9 Save/load.** Clock state at save boundary — partial fill, mid-trigger-resolution, mid-cascade.
- **E2.6 — V6 Coverage matrix per Q22.** Map every clock to: range, fill sources, drain sources, threshold effects, visibility (public/private), interactions with other clocks (couplings per E3.5). Surface missing clocks (orphans referenced elsewhere) or unused clocks (defined but unreferenced).

**Canon gates.** Clock registry consolidated. (`designs/provincial/clock_registry_v30_infill.md` is small at 645 chars — verify it covers all clocks, not just a sample.)
**Open questions.** RESOLVED via Q22: per-system implementations sharing scale convention, not a unified state machine.

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
- **E3.5 — V3 explicit coupling map per Q23.** Tracks are mixed (some orthogonal, some explicitly coupled — RDT→TD direct gating; WR→WC gating; AP→Inquisitor deployment thresholds). Enumerate every active track and list dependencies (other tracks affecting it) and dependents (other tracks affected by it). Surface unintended couplings or coupling gaps.

**Canon gates.** `params/bg/tracks.md` (8,082 chars) — read fully.
**Open questions.** RESOLVED via Q23: mixed model — some tracks coupled (RDT→TD, WR→WC), others orthogonal. E3.5 maps coupling explicitly.

---

#### E4 — Scale transitions

**Description.** Multi-scale handoff. The game's core UX flow per `<design_doc_framing>`. Per Q24 correction: canon distinguishes **seven scales**, not four. Canonical taxonomy from `params/scale_transitions.md` Scale Table:

| Scale | Example | Base Ob | Min Thread Sensitivity |
|---|---|---|---|
| Object | One item, one wound | 1 | 30+ |
| Personal | One person | 2 | 30+ |
| Relational | Small group, social agreement | 3 | 50+ |
| Territorial | A duchy, a district | 4 | 50+ |
| Structural | A kingdom, an institution | 5+ | 70+ |

Plus **Mass** (battle) as a distinct scale invoked via mass-combat handoff rules, and **Thread** scale (Leap-triggered contact-duration). Seven scales total with explicit handoff rules between each pair (eight handoff rules in `scale_transitions.md`).

**Canonical.** `params/scale_transitions.md` (6,040 chars), `designs/architecture/scale_transitions_v30_infill.md` (4,535 chars).
**Coupling.** Every system that exposes player input at multiple scales. Combat, fieldwork, faction, governance.
**Prior coverage.** R9 (two-architecture sufficiency, A+C confirmed) addresses the personal-scale architectural cardinality. Personal↔settlement transition implicit in fieldwork-combat tempo R8. **Inter-scale transitions other than Personal↔Mass never explicitly stressed.**
**Priority.** P0 (UX-load-bearing).
**Effort.** 2.5–3 sessions (expanded from V1.0's 2 sessions per Q24 — 21 transition pairs, not 6).
**Suite ID.** `E4_scale_transitions_stress_01`.

**Stress modules:**
- **E4.1 — V7 Scale transition (21 directional pairs).** Seven scales: Object, Personal, Relational, Territorial, Structural, Mass, Thread. 7×6/2 = 21 unique pairs; per-direction = 42 transitions but symmetric pairs reduce to 21 in canon (per scale_transitions.md "Eight Handoff Rules" which canonicalize the load-bearing transitions; remaining 13 pairs are either trivial (Object→Personal is a zoom) or not currently in canon — flag as gap). For each pair: enumerate state that propagates, resets, recomputes. Verify the eight canonical handoff rules (Personal→Thread, Personal→Faction, Personal→Scene, Scene→Faction, Thread→Faction, Thread→Mass, Mass→Personal, Scene→Mass) hold under stress. Surface remaining non-canonical transition pairs as gap-list output.
- **E4.2 — V3 Cross-scale interaction chain.** A territory-scale decision propagates to settlement-scale opportunities propagates to personal-scale scenes — verify the chain is coherent. Specific test: faction-layer Mass Seizure decision propagates to settlement-level garrison disposition propagates to potential personal-scale arrest scene.
- **E4.3 — V4 NERS edge cases.** Boundary: zoom-in to scale that has nothing to resolve. Crunch: zoom-out request while a personal-scale clock is mid-fill. Ambiguity: which scale "owns" a given decision (e.g., bishop appointment: settlement or territory?).
- **E4.4 — V12 Narrative emergence.** Does the player experience scale transition as a meaningful zoom (vs as a UI mode change)? Specifically: does a personal-scale outcome read as having strategic-scale consequence? (Per `<intent_of_game>`: "makes players feel important to the game world.")
- **E4.5 — V11 NPC coherence across scales.** A named NPC at personal scale must remain the same entity at settlement scale (state, disposition, threadwork knots intact). Verify referential integrity.
- **E4.6 — V9 Save/load across scale boundary.** Save while transitioning — what state survives?

**Canon gates.** `params/scale_transitions.md` must be fully read; `designs/architecture/scale_transitions_v30_infill.md` consulted. **ED-587 (Stability Crisis Zoom In trigger absent)** RESOLVED via Q10 proposal — stress against the Q10 baseline.
**Open questions.** RESOLVED via Q24 — 7 scales canonical. Residual: which of the 13 non-canonical pairs (e.g., Object→Structural skip-transitions) are gap vs intentionally out-of-scope. Surface in E4.1 output.

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
- **P2.1 — V1 Formula validation.** Stake declaration, opposed pool resolution, degree-to-outcome table. **Per Q14 resolution: Recall citation bonus (+2D) applies once per cited source per Contest instance. Re-citing the same source within one Contest grants no further bonus. Across separate Contests, the same source may be cited again (fresh adjudication).** Engine logic: per-Contest citation-set tracking.
- **P2.2 — V3 Interaction chain.** Contest outcome → state change → subsequent contest. Verify cascading contests don't interact pathologically.
- **P2.3 — V4 NERS edge cases.** Boundary: zero-pool participant (auto-loss?), tied degrees (canonical tiebreak?). Cascade: multi-party contest (>2 sides). Crunch: contest stakes that exceed participant capacity. Optimal play: stake declaration as game-theory problem (do players over-stake or under-stake systematically?).
- **P2.4 — V10 Dominant strategy probe.** Is there a stake level that strictly dominates? An always-decline-low-stake heuristic?
- **P2.5 — V11 NPC coherence.** NPC stake selection — does it read as character-driven or mechanically optimal? (Per W6 priority trees.)

**Canon gates.** `params/contest.md` fully read.
**Open questions.** Contest family relationship across Wager (F1) / social contest (P3) — verify in P2.4 dominant strategy probe. **ED-617 Grand Contest Recall** RESOLVED via Q14 (once-per-source-per-Contest); baseline embedded in P2.1.

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
- **S1.1 — V1 Formula validation across all 5 canonical Battle Scales (per Q8: canonize the [PROPOSAL] table).** Skirmish (~10 soldiers, TS 30+) / Company (~100, TS 30+) / Battle (~500, TS 50+) / Campaign (~1,000, TS 50+) / War (~5,000, TS 70+). Per-scale: force-composition arithmetic, march-budget arithmetic, casualty/strain computation (Battles on Valorian soil: MS −1 normally, MS −2 at Campaign/War per `peninsular_strain_v1.md §3`), retreat logic.
- **S1.2 — V3 Interaction chain.** Mass-combat → casualty propagation to personal-scale (named NPCs in the engagement) → Realm Stability tick → faction Mandate/Influence shift.
- **S1.3 — V4 NERS edge cases.** Boundary: 0-force vs 0-force, single-unit forces. Cascade: chained engagements in same season. Crunch: simultaneous engagements at multiple territories. Optimal play: dominant force-composition or always-engage / always-decline strategies.
- **S1.4 — V7 Scale transition.** Mass-combat → zoom-in to personal-scale (named NPC engagement, e.g., Almud leads a charge) → zoom-out back to mass result. Verify state coherence both directions.
- **S1.6 — V4 Campaign-tier edge cases.** Per Q8 promotion. Boundary: 999-soldier vs 1,001-soldier engagement at Battle/Campaign threshold (does Strain cost shift cleanly?). Campaign-scale Dissolution PP-201 application (campaign-altering decision warning). Stress the Strain step-function at scale boundaries.

**Naval is OUT OF SCOPE.** Per Q1 directive 2026-05-10. No naval stress modules; no coastal scenarios; Schoenland (T16) remains canonical-tributary with no naval-projection mechanic; coastal-territory adjacency assumed land-only.

**Canon gates.** PP-726 settlement registry (already landed; verify integration). 37-settlement adjacency map. Battle Scale [PROPOSAL] canonization (Phase 0a item).
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
**Priority.** P3 — primary mechanic mature per Q4 / Q18 (canon explicit on Failure consequences and CI seasonal cap two-tier structure); only systemic-cycle and cross-system stress remain.
**Effort.** 0.5 session.
**Suite ID.** `S5_ci_seizure_extended_stress_01`.

**Stress modules:**
- **S5.1 — V3 Post-PP-716 propagation check.** Did wound-permanence shift affect any CI inputs? (PP-716 was combat-domain; expect no direct effect, but verify.)
- **S5.2 — V4 NERS extension.** Crunch: simultaneous Seizure attempts on multiple territories. **Failure consequences canonical per Q4: Stability −1 (PP-509) + Casus Belli granted on every attempt (PP-510). Verify simulated cascade matches.** Cascade: chained failed-Seizure → Casus Belli granted → mass combat triggered next season.
- **S5.3 — V8 Convergence.** Mass-Seizure → resolution → next-season state. Can a faction get stuck in indefinite pre-Seizure buildup?

**Canon gates.** None new (per Q4 + Q18 resolutions, B4 gap #13 obsolete and B3 #5 already resolved at PP-504 two-tier cap).

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
**Priority.** P2 (Q5 proposal supplies the missing coupling; ratification-pending).
**Effort.** 1 session.
**Suite ID.** `S7_treaty_accord_stress_01`.

**Stress modules:**
- **S7.1 — V1 Treaty × Strain coupling per Q5 baseline.** Two-clause proposal: (a) active Treaty between two factions implies no inter-faction battle between them; if a battle occurs anyway, Treaty automatically breaks (Diplomatic Token removed) and Strain advances normally — no double penalty. (b) Treaty violation event = Strain +1 single tick on Diplomatic Token removal. Verify both clauses produce coherent outcomes across multi-party Treaty graphs.
- **S7.2 — V3 Accord revolt cascade re-stress.** Verify B4 Medium-confidence finding at full simulator fidelity (B4 used simplified-CI).
- **S7.3 — V4 NERS.** Boundary: treaty with 1 signatory (degenerate). Crunch: multi-party treaty with one defector. Cascade: treaty-violation chain producing multiple simultaneous Strain +1 advances.
- **S7.4 — V8 Convergence.** Can a treaty deadlock — both sides bound to incompatible actions? Q5 clause (b) ensures defection is always Strain-costed, providing the exit-pressure.

**Canon gates.** Q5 ratification (Jordan accepts or refines the two-clause proposal).

---

#### S8 — Löwenritter Graduated Autonomy

**Description.** Per Q2/Q3 supersession. Canonical 4-stage state machine (Loyal → Restless → Autonomous → Split) **replacing** the binary Coup Counter from `params/bg/core.md:87–99`. The B4 #11/#12 gaps (Counter advancement sources, Coup effect on Crown Mandate) are obsolete — the canonical state machine specifies all triggers, effects, and reversal rules. S13 (Graduated Löwenritter autonomy) merged into S8.
**Canonical.** `params/bg/core.md:87–99` (state machine + triggers + effects + reversal rule).
**Coupling.** S3 (Crown state), S5 (Crown Stability is a primary trigger axis), S10 (Realm Stability indirectly), S15 (succession), threadwork (Ehrenwall Disposition toward Almud is a trigger axis).
**Prior coverage.** B4 Löwenritter Coup Medium confidence (against the older binary model — superseded). The canonical state machine has not been stressed.
**Priority.** P1.
**Effort.** 1.5 sessions.
**Suite ID.** `S8_lowenritter_graduated_autonomy_stress_01`.

**Canonical state machine (per `params/bg/core.md:87–99`):**

| Stage | Trigger | T14 Status | Crown Effect |
|---|---|---|---|
| **Loyal** | Start | S014 Barracks answers to Crown via Ehrenwall; garrison deployable | Normal |
| **Restless** | Crown Stability ≤ 3, OR no military action 4+ seasons, OR Crown loses a province | S014 follows Löwenritter orders for defensive actions only; Crown +1 Ob offensive deployment | Fragmentation checks at T14 Ob +1 |
| **Autonomous** | Crown Stability ≤ 2, OR Ehrenwall Disposition toward Almud < 0, OR 4+ seasons Restless without resolution | S014 does not respond to Crown; T14 garrison under Ehrenwall exclusively; Crown retains sovereignty claim | Crown Military reduced by T14 garrison; cannot access Fort 3; **PI −1** |
| **Split** | Crown attacks Löwenritter, OR Crown eliminated, OR 4+ seasons Autonomous without resolution | T14 becomes Löwenritter territory; Löwenritter = separate faction (M3/I2/W3/Mil6/Stab5) | Crown loses T14; **PV drops by 3; PI −3** |

**Reversal:** Stages 1–3 reversible. Crown returns to Loyal by raising Stability above 3, conducting military action validating Löwenritter identity, or improving Ehrenwall Disposition through diplomatic engagement. Stage 4 (Split) is irreversible without reconquest.

**Stress modules:**
- **S8.1 — V1 State machine validation.** Verify all 4 stages canonical with their triggers (3 conditions per stage, OR-composed) and effects. Verify reversal rule for stages 1–3.
- **S8.2 — V3 Multi-channel interaction chain.** State transitions couple Crown Stability, Ehrenwall Disposition toward Almud (threadwork), military activity tempo (cross-season), Crown territorial holdings (S3), and the PI/PV strategic effects. Run end-to-end chain across 5+ campaigns.
- **S8.3 — V4 NERS.** Boundary trigger thrash: Crown Stability oscillates 2/3/2/3 around the Restless trigger. Cascade: simultaneous trigger from multiple conditions in one Accounting. Ambiguity: 4-seasons-without-resolution trigger when 3.5 seasons elapse before Reversal then thread breaks again. Optimal play: can Crown intentionally stall Restless by maintaining marginal Stability at 4?
- **S8.4 — V8 Convergence under hostile inputs.** Does the autonomy state ever deadlock? E.g., Crown blocks Reversal paths (refuses military validation) while Restless trigger remains marginal — does the system reach a stable cycle or a degenerate loop?
- **S8.5 — V12 Narrative emergence per stage transition.** Each transition (Loyal→Restless, Restless→Autonomous, Autonomous→Split) should read as Löwenritter character development. Stress for 5+ campaigns; count transitions; rate each for narrative legibility (vs state-machine artifact).
- **S8.6 — V11 NPC coherence: Ehrenwall.** Ehrenwall's Disposition toward Almud is a load-bearing trigger axis. Verify the priority-tree NPC behavior driving Ehrenwall Disposition produces coherent character motion (not random walk).

**Canon gates.** None new — canon mature per Q2/Q3.

---

#### S9 — Altonian Vanguard / IP

**Description.** External pressure mechanic. Imperial Pressure (IP) gauge; Altonian Vanguard deployment at IP threshold; AER generation mechanic.
**Canonical.** Referenced across `params/bg/` and B3/B4.
**Coupling.** S10 (RS decay drives IP), S1 (mass combat once deployed), S6 (Tensions external cards), S5 (CI suppression interactions).
**Prior coverage.** B3/B4 Medium confidence; **AER removed from canon 2026-05-04 per Q6** (Church-Altonian diplomacy now via Altonian hooks); **Warden emergence post-RS40 reframed per Q7** (PP-605 introduced WC/WR two-track gating — Varfell-private WR gates peninsula-wide WC; supersedes single-trigger model); **Campaign-scale vs standard battle promoted to canon per Q8** (5-tier Battle Scale table canonized).
**Priority.** P1 (still load-bearing despite gap resolutions — IP/Vanguard chain never simulated at full fidelity).
**Effort.** 2 sessions.
**Suite ID.** `S9_altonian_vanguard_stress_01`.

**Stress modules:**
- **S9.1 — V1 IP gauge formula validation.** IP fill, drain, threshold for Vanguard deployment, T10→T3→T2→T1 advance schedule (per `params/bg/clocks.md` PP-568 Vanguard mechanics: 2-consecutive-season uncontested advance, Military-5-equivalent contested-battle at Ob 3, T1 occupation triggers all-factions −1 Stability/season).
- **S9.2 — V3 Interaction chain.** RS decay → IP advance → Vanguard deployment → mass combat. End-to-end campaign-late-game chain.
- **S9.3 — V4 NERS.** Boundary: high-RS late-game (Vanguard non-deployment scenario), low-RS early-game (premature Vanguard? Canonical block?). Cascade: simultaneous internal crisis + Vanguard arrival.
- **S9.4 — V5 Full scenario.** S20–S30 campaign with Vanguard as primary external pressure. Match against B3 reference timeline (Vanguard at T10 by S22–28; T10→T1 advance by S27).
- **S9.5 — V11 Vanguard NPC behavior.** Per `params/bg/clocks.md`: Vanguard "cannot be negotiated, traded, or Diplomatically managed." Engine NPC behavior is deterministic-on-uncontested. Stress for behavioral coherence: does Vanguard read as inexorable external pressure or as state-machine artifact? [PROVISIONAL ED-340] authorial review status — track separately.
- **S9.6 — V3 WC × WR × MS interaction (per Q7 reframe).** Verify Varfell-private WR (gates) → peninsula-wide WC (effects) → MS decay modulation chain. WC ≥ 1: +1D Thread peninsula-wide. WC ≥ 2: MS decay halved (−1 → −0.5 floor). WC = 3: MS +2/season (active stabilization). Stress the WC=3 endpoint — does it produce stable MS or thrash?
- **S9.7 — V4 NERS WC = 3 boundary.** Active MS stabilization vs ongoing radiation effects. Boundary: MS approaches 100 (Restoration complete — what happens to WC?). Cascade: WC drops from 3 to 2 mid-season (rapid drain).

**Canon gates.** [PROVISIONAL ED-340] Vanguard authorial review (faction identity, advance route, elimination conditions). Battle Scale canonization Phase 0a item (Q8).

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

**Description.** Per Q20 supersession. Canonical **Royal Crisis Fuse** in `params/bg/royal_assassination.md` (CANON, derived from `designs/architecture/conflict_architecture_proposal.md`). Almud's father is **backstory (struck)** per Session A Patch 7. Live mechanic is the Royal Crisis Tension Card (Card #1) which triggers a Fuse (S0 seed → S8+ fire, succeed-on-fire) with a 3-target sub-roll at game start or card-draw: Lenneth (1–2), Torben (3–4), Almud (5–6). Each target produces a distinct mid-game consequence arc.
**Canonical.** `params/bg/royal_assassination.md` (full); cross-refs `designs/architecture/conflict_architecture_proposal.md`.
**Coupling.** S6 (Royal Crisis = Tension Card #1), S15 (succession), S3 (Crown faction state), S8 (Löwenritter graduated-autonomy reaction to Crown crisis), threadwork (target-NPCs are threadwork participants), C1 (ignition).
**Prior coverage.** None directly. The canonical Fuse + 3-target structure has not been stress-tested.
**Priority.** P1 (load-bearing for ignition narrative arc; mature canon but never stressed).
**Effort.** 1 session.
**Suite ID.** `S11_royal_assassination_stress_01`.

**Stress modules:**
- **S11.1 — V1 Canonical Fuse + sub-roll validation.** Fuse timeline (S0 seed, S1–S7 escalation visible + player-investigation opportunity, S8–S12 fire). Target sub-roll distribution (uniform across 3 targets). Player-investigation cost vs faction-building tradeoff verified.
- **S11.2 — V3 Per-target interaction chain.** Three distinct consequence arcs:
  - **Lenneth → Almud revenge arc.** Crown investigation arc; defensive posture breaks; Crown's Einhir policy hardens; RM PW advances; Southern Accord erodes.
  - **Torben → Elske retrieval.** Crown military deployment to T4 (Varfell territory); provocation + Altonian diplomatic crisis (IP spike). Succession-question and Altonian-question merge.
  - **Almud → Lenneth takes throne.** Crown factional identity inverts. Lenneth pro-Einhir, pro-Thread-research, anti-caste-suppression. Crown becomes Varfell+RM ally on Einhir question, Church-heresy-target. Löwenritter forced decision (protect heretic queen vs advance toward Autonomous/Split — couples to S8).
- **S11.3 — V4 NERS.** Boundary: investigation succeeds at S7 (assassination averted vs un-averted-but-extended-fuse). Cascade: Royal Crisis card drawn early (S1–S4) — does Fuse compress? Ambiguity: target already incapacitated by other event when Fuse fires.
- **S11.4 — V10 Player investigation strategy.** Investigation costs card slots; competing with faction-building. Stress: is there a dominant investigation-or-ignore strategy?
- **S11.5 — V12 Narrative emergence per target.** Each of three arcs should produce distinctly different mid-game. Stress 3+ campaigns per target (9+ total). Verify mid-game divergence is legible.

**Canon gates.** None — canon mature per Q20.

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

#### S13 — [REMOVED]

**S13 merged into S8** per Q2/Q3 resolution (2026-05-10). The Graduated Löwenritter Autonomy state machine is canon in `params/bg/core.md:87–99` (not proposal/deferred); S13's V1.0 framing as "needs engine_v4" was based on stale reading. S8 now covers the canonical state-machine stress.

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
- **S15.1 — RM canonical model (PP-460-superseded).** ED-588/589 references obsolete per Q11/Q12: PP-460 establishes RM as statless faction operating exclusively via Presence markers + Community Weaving. Stress the canonical model: Community Organising pool scales 1D-base + 1D-per-adjacent-Presence-marker; Community Weaving pool = (100−MS)÷20 round up min 1, −1 per Presence marker in territory.
- **S15.2 — V3 Cross-system chain.** Royal Crisis Fuse outcome (S11.2 — particularly Almud → Lenneth-takes-throne arc) → succession-axis tension → potential RM Presence-marker accumulation acceleration. End-to-end chain.
- **S15.3 — V4 NERS extension.** Cascade: chain succession (heir dies before resolution). Ambiguity: contender from non-national faction (B1 finding restricted to national, confirm canon).
- **S15.4 — Splinter Influence split (Q17 baseline).** Per Q17: **Influence splits 60/40 same as Mandate** (majority-successor 60%, splinter 40%). Wealth/Military follow same 60/40 rule pending balance test. Stress the proposal under multi-stat split scenarios; surface any per-stat asymmetries that break.
- **S15.5 — V5 full-scenario RM ignition + propagation (new per Q11).** Drive 5+ campaigns with RM enabled (5-player config). Verify Presence markers accumulate to political significance via Community Organising / Community Weaving. If not, surface as rate-tuning issue (not structural gap).
- **S15.6 — V4 NERS Presence marker removal (new per Q12).** Q12 proposed orphan-prune-only baseline (markers persist until no adjacent territory has any RM presence, OR MS = 100 dissolves RM). Test removal scenarios; verify whichever model Jordan ratifies (orphan-prune-only or with-Community-Suppression).

**Canon gates.** Q12 ratification (Jordan picks orphan-prune-only vs with-Community-Suppression). Q17 ratification (Influence-split 60/40 + Wealth/Military follow-on).

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
**Prior coverage.** `geography_phase4_stress_01` 2026-05-10 — Phase 3 land-based verified (Mountain Pass, cavalry, coastal landing); ED-055 naval gap **dropped per Q1 (Jordan directive 2026-05-10)**.
**Priority.** P2 (land-only remaining; reduced scope).
**Effort.** 0.5 session.
**Suite ID.** `W1_geography_land_only_stress_01`.

**Stress modules:**
- **W1.2 — V4 Terrain NERS.** Boundary: territory with no land-route (island? exclave?). Cascade: cross-terrain movement when terrain effects compound (river + mountain + forest). **Naval scenarios excluded.**
- **W1.3 — V7 Cross-scale terrain consistency.** Terrain at territory scale must be coherent at settlement scale (settlement in forested territory has forest-flavored scenes).

**Canon gates.** None. Naval coverage permanently out of scope per Q1.

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
- **W6.4 — Q9 baseline: Priority 6 at degraded Mandate.** ED-586 resolution proposal: at Mandate < 3 (Legitimacy OR Popular_Support < 3), Priority 6 ("Attacked") response degrades from "Military proportional" to **defensive-only** (no offensive deployment, no covert escalation). Engine logic: substitute Priority 6 action set on Mandate-degradation flag. Verify the proposal produces coherent low-Mandate response under stress; alternative-considered fallbacks per Q9.
- **W6.5 — V11 NPC coherence cross-cut.** Does the priority tree produce behavior that reads as character?
- **W6.6 — Crown priority tree at T2 Kronmark.** Per Q19 resolution: T2 Kronmark defense is already canonical at Priority 4 Default with Varfell-T4-trigger conditional (`params/bg/npc_priority_trees.md:44`). Stress the conditional under degraded-Mandate Crown.

**Canon gates.** Q9 ratification (Jordan accepts defensive-only degradation OR refines).

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
- **W7.3 — Q15 baseline: Torben Conviction window.** ED-618 resolution proposal: S1–S8 = formative window, Torben's Conviction values respond to player interactions / threadwork knots / faction events the player participates in. S9+ = locked. Early lock if Altonian Tutoring Demand fires (IP ≥ 40) before S8. Stress: verify lock semantics; verify formative-window mutability; verify early-lock edge cases.
- **W7.4 — V11 Torben + Elske + Lenneth NPC coherence (cross-cut with S11 Royal Crisis Fuse).** Each is a Royal Crisis target; each has bespoke special-NPC mechanics. Stress for cross-interaction (e.g., Torben dies → Elske retrieval invokes both Elske Off-Board Card and Torben Loyalty reset path).

**Canon gates.** Q15 ratification (Jordan accepts S1–S8 window OR refines length — Q15 alternatives consider S1–S5 shorter window).

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
- **G2.1 — Q13 baseline: Parliamentary Procedural Block on Tribune.** ED-616 resolution proposal: when Parliament is in active Session AND a Tribune Intel action is declared, opposition factions may move for Procedural Block. Block roll: Influence pool from non-acting factions (each contributing 1D if voting block) vs Ob = (Acting faction PI value) + 1. Success: Tribune action suspended this season; may re-declare next season. Overwhelming: suspended + acting faction PI −1. Failure: Tribune proceeds normally. Limit: one Block attempt per Parliamentary Session.
- **G2.2 — V1 Action enumeration** — Tribune actions, parliamentary actions, voting mechanic.
- **G2.3 — V3 Tribune-action → PI-track interaction chain.**
- **G2.4 — V4 NERS.** Boundary: parliament with deadlock. Crunch: simultaneous tribune challenges + Block votes.

**Canon gates.** Q13 ratification.

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
- **C4.3 — Q10 baseline: Stability-Crisis Zoom-In trigger.** ED-587 resolution proposal: at any phase boundary, if an active faction has Stability ≤ 1 AND no Crisis Scene has fired this season, engine offers Zoom-In into a Crisis Scene at next legal Phase-Lock entry point (After Phase 1 / 3 / 6 Step 1 per PP-103). Player opt-in. Declined → log narrative beat, no penalty. Accepted → Crisis Scene from canonical catalog (Phase 0a authoring item); resolves at personal scale; Domain Echo to Stability at next Accounting per PP-108/PP-109. Stress: trigger correctness (no double-fire same season), Domain-Echo coherence on accept path, no-penalty semantics on decline path.

**Canon gates.** E4 complete. Q10 ratification + Crisis Scene catalog authored (Phase 0a).

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

Repository-level cleanup + V1.1 canonization tasks + ratification batch.

- **Phase 0a** — Repo hygiene + V1.1 canonization. Editorial-ledger archive auto-fix, file_index_summary regeneration, freshness gate update, canonical_sources SHA drift remediation, PP-726 SHA pin update, Battle Scale [PROPOSAL] → canon (Q8), Crisis Scene catalog authoring (Q10), Influence-split 60/40 spec patch commit (Q17), prior session checkpoint commit, PAT rotation (Jordan-side).
- **Phase 0b** — Ratification batch (post-V1.1). 10 PROPOSED items from Q-resolutions awaiting Jordan decision: Q5 (Treaty/Strain), Q8 (Battle Scale promotion already in 0a), Q9 (Priority 6 degradation), Q10 (Crisis Zoom-In already in 0a as catalog), Q12 (RM Presence removal model), Q13 (Tribune Block), Q14 (Recall once-per-source), Q15 (Torben window), Q16 (Obligation cap UI), Q17 (Influence-split already in 0a). Bundle as one ratification session per V1.1 §6 — each is a single-decision item.

**Workplan V1.0 had 8 B-batch gaps + 8 ED gaps slated for Phase 0b. V1.1 post-resolution:** 6 of 8 B-batch gaps were RESOLVED or SUPERSEDED (Q2/Q3/Q4/Q6/Q7/Q18); 5 of 8 EDs were RESOLVED or SUPERSEDED (ED-588/589 via PP-460, ED-587 via Q10, ED-617 via Q14, ED-618 via Q15, ED-619 via Q16, ED-586 via Q9, ED-616 via Q13). Phase 0b session count drops from ~16 to ~1–2 (one ratification bundle session + possibly one follow-up for Crisis Scene catalog content).

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

**Total estimated sessions (V1.1 revised): ~45–55** (excluding Phase 7 engine_v4-deferred and excluding open-ended per-session retries on hook fires). Reduction from V1.0 ~55–65 reflects Phase 0b shrinkage (~9 sessions) partially offset by V1.1 added modules (~3 sessions: E1.5, E2.6, E3.5, S1.6, S8 expanded, S9.6/S9.7, S11.5, S15.5/S15.6).

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

**Phase 0b: Ratification batch.**

Bundle the 10 Q-resolution proposals awaiting Jordan ratification (Q5/Q8/Q9/Q10/Q12/Q13/Q14/Q15/Q16/Q17). Each is a single-decision item with proposal + alternatives surfaced in `stress_workplan_resolutions_2026-05-10.md`. Bulk-ratify in one session; produce one or more PP-commits to canonize accepted proposals.

ED-055 naval scope is **dropped** per Jordan directive 2026-05-10; not in session-two scope.

### Session-three recommended

**Phase 1 / E1 — Dice/TN/Degree stress.** Foundation; one session bundle; produces verification commit. Followed by E2/E3/E4 in sequence.

### Parallelization windows

Once Phase 1 (E-suite) complete, the following can run in parallel sessions (different scopes):
- Phase 2 (Personal-scale) — `editorial` or `design` scope.
- Phase 4 (World substrate) — independent of personal-scale work.
- Phase 0b gap-closure follow-ons — `editorial`.

Phase 3 (strategic) should not parallelize until S6 (Tensions Deck) is verified — S6 gates most downstream Phase 3 modules.

---

## 7. Open questions — residual ratifications pending Jordan

V1.1 post-resolution status. V1.0 listed 25 open questions; Jordan directive "resolve all, no naval" (2026-05-10) processed them — 1 dropped (Q1 naval), 6 RESOLVED via existing canon, 8 SUPERSEDED via later PP/ED, **10 PROPOSED with rationale awaiting ratification.** Full resolution detail in `tests/sim_framework/stress_workplan_resolutions_2026-05-10.md`.

### Residual ratifications

Each is single-decision; bundle as one Phase 0b session per §6.

| Q | Proposal | Decision required | Blocks if unratified |
|---|---|---|---|
| Q5 | Treaty defection → Strain +1; Treaty break automatic on inter-faction battle | accept / refine / reject | S7.1 |
| Q8 | Promote Battle Scale 5-tier table from [PROPOSAL] to canon | accept / refine | S1.1, S1.6 |
| Q9 | Priority 6 at Mandate < 3 → defensive-only response | accept / refine | W6.4 |
| Q10 | Stability ≤ 1 → engine offers Zoom-In at next Phase-Lock entry; Crisis catalog authored | accept / refine; window length | C4.3 |
| Q12 | RM Presence markers: orphan-prune-only OR with Community-Suppression action | pick one | S15.6 |
| Q13 | Parliamentary Procedural Block on Tribune: Influence-pool vs PI Ob, once/Session | accept / refine | G2.1 |
| Q14 | Recall once-per-source-per-Contest; fresh across Contests | accept / refine | P2.1 |
| Q15 | Torben Conviction window S1–S8 (formative), lock at S9 or Altonian Tutoring fire | accept / refine; window length | W7.3 |
| Q16 | Obligation cap: engine surfaces forced-choice on 4th Obligation; retire/dissolve/decline | accept / refine | E1.5 |
| Q17 | Influence splits 60/40 same as Mandate; Wealth/Military follow pending balance test | accept / refine | S15.4 |

### Resolved Qs (audit trail)

- **DROPPED:** Q1 (naval).
- **RESOLVED via existing canon:** Q4 (Seizure failure), Q18 (CI cap), Q19 (Kronmark priority), Q21 (TN variants), Q22 (clocks per-system), Q24 (5+ scales corrected).
- **SUPERSEDED:** Q2/Q3 (Coup → Graduated Autonomy), Q6 (AER removed 2026-05-04), Q7 (Warden via PP-605 WC/WR), Q11/Q12 (RM via PP-460), Q20 (Almud's father → Royal Crisis Fuse).
- **CLARIFIED:** Q23 (tracks mixed coupling), Q25 (faction actions hybrid visibility).

Detail: `tests/sim_framework/stress_workplan_resolutions_2026-05-10.md`.

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
- **Naval mechanics.** Out of scope per Jordan directive 2026-05-10 (V1.1 Q1 resolution). Schoenland T16 remains in canon as Altonian tributary; no naval-projection mechanic, no coastal-landing scenarios, no sea-zone adjacency. Coastal territories assumed land-only-adjacent. Re-scope only on explicit directive reversal.

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

- **V1.1 (2026-05-10).** Post-Q-resolution. Jordan directive "resolve all, no naval" processed 25 open questions: 1 dropped (Q1 naval), 6 RESOLVED via existing canon, 8 SUPERSEDED by later PP/ED, 10 PROPOSED with rationale + alternatives + fallback. Workplan deltas: §0.4 +3 canonization prerequisites; §4.E1 add TN 6/8 variants + E1.5 Obligation UI; §4.E2 enumerate clocks + E2.6 coverage matrix; §4.E3 add E3.5 coupling map; §4.E4 expanded 4→7 scales (21 transition pairs); §4.P2.1 Recall once-per-source; §4.S1 explicit 5-scale + drop naval + S1.6; §4.S5 demoted to P3; §4.S7.1 Q5 baseline; §4.S8 rewritten as Löwenritter Graduated Autonomy + S13 merged in; §4.S9 reframe AER/Warden + S9.6/S9.7; §4.S11 canonical Royal Crisis Fuse + 3-target sub-roll; §4.S13 REMOVED; §4.S15 PP-460-supersedes + S15.5/S15.6; §4.W1 land-only; §4.W6.4/W7.3/G2.1/C4.3 Q-proposal baselines; §5 phase counts revised (~55–65 → ~45–55); §6 session-two = ratification batch; §7 collapsed to 10 residual ratifications; §8 naval out-of-scope; Phase 0b shrunk ~16 → ~1–2 sessions. Resolution audit trail: `tests/sim_framework/stress_workplan_resolutions_2026-05-10.md`. Commit: see infrastructure commit message.
- **V1.0 (2026-05-10).** Initial authorship. Post-bootstrap, post-`context_gate` fix commit `b7f0ad7`. Canonical sources read: simulator SKILL, mechanic-audit SKILL, coverage_matrix, sim_coverage_index, combat manifest, fieldwork stress, workplan_rebuild_2026-04-19 (format exemplar), canonical_sources.yaml (systems registry).

---

`[SELF-AUTHORED — bias risk]` This workplan was authored in the same session as the canonical-sources read. Independent reviewer would likely add: (a) explicit prioritization criteria (this workplan ranks by gap-density and load-bearing-ness; alternative criteria like player-visibility-priority or engine-surface-readiness would produce a different ordering); (b) estimated effort numbers are educated guesses based on prior-suite session counts and should be validated against actual per-system specification complexity; (c) no per-system risk-of-cascading-canon-shift analysis (a stress finding in S6 might cascade to revise C1 plans — the workplan acknowledges this only structurally via "canon gates," not quantitatively).

`[ASSUMPTION: Letter-prefix suite convention (A/F/G/R-suite + new P/S/W/G/C/E letters) is acceptable — basis: existing harness uses A, F, G, R; extension to other letters is a workplan-authoring decision Jordan can override. CONFIDENCE: medium]`

`[ASSUMPTION: ~55–65 session estimate excludes hook-fire retries and Jordan-decision wait-time — basis: completed suites averaged ~1 session per stress module of moderate complexity. CONFIDENCE: low — high variance across systems]`

`[GAP: Q21–Q25 (clarification questions) should be answered before fine-grained per-system stress planning is finalized — these answers may collapse or split system entries.]`
