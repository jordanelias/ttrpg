# Valoria Multi-Session Workplan
**Date:** 2026-05-16
**Author:** Session `14f97c38f9daf6f0` (72h-audit + plan)
**Lifespan:** Active until v17 M7 ships or Jordan supersedes. Tracks close in place.
**Surface:** Operational coordination for 1–N concurrent Claude sessions.

---

## How to use this document

Every session start, in this order:

1. `bootstrap <scope>` per PI
2. Read `session_logs/index.md` — note other active sessions and their `owns` claims
3. Read this file — pick a track that is **not currently owned** by another active session
4. Run that track's **entry checklist** verbatim
5. Do the work
6. Run that track's **exit checklist** verbatim (handoff + session close)

Tracks have uniform structure: `status` · `dependencies` · `entry checklist` · `work` · `exit handoff schema` · `blockers`.

If a track lists `BLOCKED on Jordan decision`, do not pick it up — surface the blocker, wait. If a track is mid-flight (handoff exists at `tests/handoffs/`), resume from the handoff. Do not restart.

---

## Throughput reality

The dominant bottleneck remains Jordan-decision throughput; GraphQL budget is **no longer** a constraint after F.4/F.5/F.6 (commits `d72cc86`, `a41af6b`) cut bootstrap cost from ~130 to 2 GraphQL/call (warm cache). 15 open Q's (Q1–Q15 below) still gate most tracks.

**Track Classes** (state as of 2026-05-16 20:13 UTC):

| Class | Tracks |
|---|---|
| ✅ **DONE** | A.M2, A.M3, A.M4, E (partial — atomizer ran), F.4, F.5, F.6 |
| **Claude-safe** (no Jordan decision needed) | A.M1, A.M5, F.1 (default fix (a)), F.2, G.Tier-2 |
| **Jordan-gated** (blocked until decision lands) | B (all sessions), C, D, G.Tier-1 |
| **Chain-dependent** (Claude-safe once predecessor lands) | A.M6, A.M7 |
| **Deferred** (out of current cycle) | F.3, H |

**Critical-path status:** v17 integration is ~50% through the module sequence. M1 + M5 are the remaining foundational pieces; M6 depends on M1–M5; M7 is the integration sweep. Next pickup for a Claude-safe critical-path worker is **A.M1** (still the queued next_action per session_log).

Realistic concurrent ceiling for pure-Claude work: **2–3 tracks**. Worker(s) finishing early should pick up F.1 / F.2 rather than wait on Jordan-gated chains.

---

## Completed workstreams — do not redo

The following are **done**. A resuming session that "discovers" a need to build them is pattern-matching, not reading. Skim the named directory before restarting any of them.

| Workstream | Location | Closed at |
|---|---|---|
| Settlement Management Mode-G Modules 01–13 | `tests/sim/settlement_mgmt_stress_01/` | 2026-05-13–14 (commits `b5545aa` → `6c9cdd3`) |
| Mass battle comparative audit (Chunks 0–12) | `designs/audit/2026-05-15-mb-comparative-audit/` | 2026-05-16 `a734f63` (consolidated plan) |
| Dice calibration Phases 1a / 5 / 6 / 7 / 8 | `tests/sim/phase*` + `params/combat.md` Combat Balance Note | 2026-05-16 `48f8360` (Phase 8 update final) |
| Decision E (continuous engine canonical for Godot) | `params/core.md §Continuous Engine`, ED-833 resolved | 2026-05-16 `721acc1` |
| Engine NERS audit (architectural scope) | `designs/audit/.../engine_ners_*.md` | 2026-05-15 `02e2dd7`; REC-1/2/3 closed `0cb7beb` |
| Workstream meta-audit | ED-835 resolved | 2026-05-16 `ba13777` |
| Handoff infrastructure (schema, conflict-detection, resumption) | `skills/valoria-orchestrator/scripts/github_ops.py` | 2026-05-14 `a8893c7` → `84ad6b0` |
| Project governance v2.3 / PI v2 | architecture spec + PI in Project Knowledge | 2026-05-15 (chat `785edb8e`) |
| Pre-firearms research catalogue (17 files, ~6k lines) | `research/pre_firearms_formations/` | 2026-05-15 `bd0b0ba` (research-vs-design comparison) |
| Combat Integration Session A (chassis) | `tests/sim/combat_integration/session_a_chassis.py` | 2026-05-15 `b31c84c` audited `b29c0c5` |
| GraphQL leak diagnosis + F.4/F.5/F.6 fix | `tools/freshness_gate.py`, `tools/compliance_check.py`, `skills/valoria-orchestrator/scripts/valoria_hooks.py` | 2026-05-16 `d72cc86` + `a41af6b` (cost 130 → 2 GraphQL/bootstrap warm cache) |
| Editorial ledger atomizer auto-fix | `canon/editorial_ledger.yaml` + archive | 2026-05-16 `d98192b` (archived 8 resolved entries ED-832..ED-839) |
| Freshness gate canonical_sha resync | `references/canonical_sources.yaml` | 2026-05-16 `4c9770c` |
| A.M2 CI Political Revision | `tests/sim/v17-integration/m2_ci_political_revision.py` | 2026-05-16 `29b5242` (78 tests pass) |
| A.M3 Mass Battle Resolution | `tests/sim/v17-integration/m3_mass_battle.py` | 2026-05-16 `dc9a71a` (canonical §B.3) |
| A.M4 Unit State Management | `tests/sim/v17-integration/m4_unit_state.py` | 2026-05-16 `e33849c` (9-class roster) |

If you are about to scaffold something on this list, **stop**, read the named location, and either pick up follow-on work (per the relevant Track below) or surface a gap if the existing work is materially incomplete.

---

## Parallelism contract

**File-region ownership.** A session that picks up a track owns these write regions until session close. Other sessions must treat them read-only.

| Track | Owned write regions | Read-only (cross-track refs) |
|---|---|---|
| A (v17) | `tests/sim/v17-integration/`, `tests/coverage_matrix.md` (append-only section), per-module new files | `designs/territory/`, `designs/provincial/`, `canon/`, `params/` |
| B (combat sessions B–F) | `tests/sim/combat_integration/`, `tests/handoffs/2026-05-*_combat_integration_*.md` | `designs/scene/combat_v30.md`, `params/combat.md` |
| C (mass-battle ED) | `canon/editorial_ledger.yaml` (append entries only), `designs/audit/2026-05-14-balance-audit/` | `designs/provincial/mass_battle_v30.md`, `params/mass_combat.md` |
| D (duel ratification) | `tests/sim/duel_architecture_stress_01/`, new params files for duel-system ratification | `params/combat.md`, `designs/scene/` |
| E (editorial hygiene) | `canon/editorial_ledger.yaml` (archive + summary regen), `references/canonical_sources.yaml`, `references/file_index_summary.md` | all design files |
| F (architecture/tooling) | `skills/valoria-orchestrator/scripts/*`, `tools/index_gen.py`, `tests/hooks/`, PI script clauses | none (infra-only) |
| G (pre-firearms integration) | `research/pre_firearms_formations/`, new propagation entries in `designs/provincial/`, `designs/scene/`, `params/` | `canon/editorial_ledger.yaml` |
| H (Godot kickoff) | `jordanelias/valoria-game/*` (entire repo) | `jordanelias/ttrpg/canon/`, `designs/`, `params/` |

**Write-contention points:**

- **C + E both touch `canon/editorial_ledger.yaml`.** C appends new ED entries; E archives resolved ones + regenerates summary. **Resolution:** E runs *between* C-sessions; if both must run concurrently, E waits until C session-closes. Never two open writers on the ledger.
- **G writes to `designs/provincial/*` and `designs/scene/*`; A reads them.** A.M1 / A.M3 must skeleton-fetch *after* G's relevant propagation commits land. Resolution: G commits propagation first, then A.Mx starts.
- **C writes ED entries that G may resolve.** Resolution: G consults C's open EDs at session start; close them in same session if resolution is in the propagation.
- **B and D both reference `params/combat.md`.** B reads-only (Session A chassis already committed). D may write if ratification adds canonical entries. Resolution: D writes are PP-prefixed and Jordan-decision-gated; no silent overwrites.

**Editorial ledger access pattern:**
- Read at session start: `canon/editorial_ledger.yaml` SHA via `g.get_fetch_head()`
- Before `safe_commit`: re-check SHA. If changed mid-session, fetch fresh and rebase your appends. `safe_commit` will halt on stale parent anyway; this is the explicit pre-check to avoid the halt.
- Never delete entries — archive via `atomizer.archive_by_status` (Track E only).

**Merge points (sequenced gates):**
1. Track E completes ledger archival → unblocks bootstrap warnings cluster. ✅ (`d98192b`)
2. Track G commits Tier-1 propagations (P1 drift findings) → unblocks A.M1 / A.M6 canonical reads.
3. Track A.M1 + A.M5 → unblocks A.M6 (faction action expansion needs settlement + aggregation state).
4. Track A.M1–M6 complete → unblocks A.M7 (integration sweep).
5. Track B Sessions B–F complete → unblocks final personal-scale combat ratification.
6. Track A.M7 PASSES (Wilson CI ∈ [20%, 30%] all factions) → unblocks Track H Godot kickoff.

(Original gate 2 — Track C unblocking A.M3 — removed: A.M3 shipped without Track C and Track C is now independent ED hygiene. See Track C section.)

---

## Recommended session-launch order

**State as of 2026-05-16 20:13 UTC:** A.M2/M3/M4 + Track E (ledger) + F.4/F.5/F.6 already shipped. M1 and M5 are the remaining v17 foundational modules; M6 + M7 chain-dependent.

**Assumption:** Jordan-decision turnaround is faster than a Claude session length. If it isn't, treat Jordan-gated tracks as `WAIT` slots and pick a Claude-safe track instead.

**N = 1 (sequential single worker), Claude-safe-first ordering:**
F.1 → F.2 → A.M1 → A.M5 → A.M6 → *(if Jordan resolves Q1–Q4 for hygiene)* C → *(if Jordan resolves G design Q's)* G.Tier-1 → A.M7 → *(if Jordan resolves Q5–Q11)* B → D → H

**N = 2 (two concurrent workers):**
- **Worker 1 — Claude-safe critical-path:** A.M1 → A.M5 → A.M6 → A.M7
- **Worker 2 — opportunistic:** F.1 → F.2 → G.Tier-2 → *(when Jordan answers)* C → G.Tier-1 → B → D

**N = 3 (three concurrent workers):**
- **Worker 1 — critical-path:** A.M1 → A.M5 → A.M6 → A.M7
- **Worker 2 — Claude-safe tooling:** F.1 → F.2 → G.Tier-2 → F.3
- **Worker 3 — Jordan-gated chain:** *(when Jordan answers)* C → G.Tier-1 → B → D

At N=3, Worker 3 has the highest idle risk — every step is Jordan-gated. If Q1–Q4 aren't answered for Track C, Worker 3 stalls at step 1. Reassign Worker 3 to F.3 (CI work, multi-session) or H.0 spec-only work rather than idle. Worker 1's critical path is now shorter than v1's recommendation since M2/M3/M4 already shipped.

---

## Track A — v17 Integration (CRITICAL PATH)

**Purpose:** Integrate 27 missing canonical mechanics into the strategic faction-balance simulator. Closes Church 0% / Varfell 0% structural defects. Reference: `tests/sim/v17-integration/module_manifest.md`, `tests/sim/v17-integration/gap_analysis.md`.

**Manifest:** `simulation` task type. All Track A sessions call:
```python
h.task_gate('simulation')
# at artifact production:
h.completeness_gate('simulation', scope={'systems_touched': [...], 'integration_module': 'mc_v17.py'}, claim='full-canon')
```

### A.M1 — Church Settlement Infrastructure
**Status:** READY · **Claude-safe** (next_action per session_log_current.md)
**Dependencies:** none (foundational). Reads must reflect any Track G propagation.
**Owns:** new file `tests/sim/v17-integration/m1_church_infrastructure.py`, append to `coverage_matrix.md`
**Entry checklist:**
- `bootstrap simulation`
- `h.task_gate('simulation')`
- Skeleton-fetch then full-read: `designs/territory/settlement_layer_v30.md` §1.5, §1.6, §1.7, §3, §4.3
- Skeleton-fetch then full-read: `designs/provincial/ci_political_v30.md` §1
- Skeleton-fetch then full-read: `designs/provincial/victory_v30.md` §3.2
- Skeleton-fetch: `params/core.md` (Continuous Engine spec for ED-833 compliance)
- Check Track G open propagations against settlement_layer; if pending, wait

**Work:**
- Implement per-territory Church infrastructure state (Religious Building tier, Templar Station bool, Inquisitor Base bool, Church Governor bool)
- Encode starting infrastructure from canonical settlement registry (37 settlements → 15 territories)
- PT generation: Chapel +0.5 / Church +1.0 / Cathedral +2.0 (+0.5 adjacent)
- CI generation: +1 CI/season per territory with Templar
- RM Ob modifier: +1 Ob to RM governance actions per Inquisitor
- Seizure Ob formula: `10 − PT − infra_mod` (Chapel 0, Church −1, Cathedral −2, Templar −1, Inquisitor −1, Governor −2; cap −4; floor 1)
- Spiritual Weight (SW) per territory as fixed attribute
- SW-weighted CI generation replaces v15's simple piety_yield
- Unit tests: 15+ tests covering each mechanic in isolation
- Integration smoke-test against current mc_v16 baseline

**Exit handoff schema (per `g.write_handoff` real contract — see `_validate_handoff_schema` in `github_ops.py`):**
```yaml
id: 2026-05-XX_v17_m1_to_m2
task:
  skill: valoria-simulator
  description: A.M1 Church Settlement Infrastructure complete; A.M2 next
context_files:
  - path: tests/sim/v17-integration/m1_church_infrastructure.py
    depth: full
    reason: M1 implementation; M2 imports infrastructure-state dataclass
  - path: tests/sim/v17-integration/module_manifest.md
    depth: full
    reason: dependency declarations + canonical-source list
  - path: designs/provincial/ci_political_v30.md
    depth: skeleton
    reason: M2 reads §1–§3 for milestone changes; full-read at M2 start
working_state:
  next:
    - Implement CI milestones (55, 80, 100) per ci_political_v30 §2
    - Revise Mass Seizure to per-territory Ob
    - Add 10+ unit tests; integration smoke-test against M1 baseline
last_commit: <sha-of-M1-commit>
owns:
  - tests/sim/v17-integration/m2_ci_political.py
```

**Blockers:** none (foundational module).

### A.M2 — CI Political Revision
**Status:** ✅ **DONE** (commit `29b5242`, 2026-05-16)
**Shipped:** `tests/sim/v17-integration/m2_ci_political_revision.py` · 78 tests pass · 26 ledger entries · seasonal cap (±5/±3), milestone effect queries (40/55/65), Bonus Dice + Obstacle Modifier, Hafenmark suppress, Unification target generator.
**Follow-ups:** any ledger entries opened during M2 work flow to Track C (ED hygiene) for disposition; not blocking other work.

### A.M3 — Mass Battle Resolution
**Status:** ✅ **DONE-WITH-CAVEATS** (commit `dc9a71a`, 2026-05-16)
**Shipped:** `tests/sim/v17-integration/m3_mass_battle.py` (451 lines, 63 tests pass, 23 ledger entries) · canonical §B.3 6-step BG resolution + military_layer §2.1–§2.2 outcome margin table · 4 shared tactic cards mechanical, 16 faction-specific registered for M6 · Fort dice in defender pool · structured `BattleResult` dataclass.
**5 provisional assumptions** in `m3_sim_verification_ledger.json` awaiting Jordan ratification:
- **A1** Faction-specific tactic-card mechanical effects deferred to M6 (Stratagem requires two-pass resolution M3 doesn't support — architectural follow-up).
- **A2** Deterministic RNG via optional `rng` parameter — no follow-up.
- **A3** Damage-allocation policy "weakest defender first" — can be faction-overridden in M6/M7.
- **A4** Disposition table simplified to pool modifiers because canonical table B6 isn't in current canon; flagged divergence from §B.3 Step 2 wording.
- **A5** Morale check fires per unit class that took any losses (aggregate-count semantics from M4); refine if per-unit Health added.
**Track-C relationship clarified:** A.M3 shipped without resolving ED-811 / ED-813 / ED-822 / ED-823 — those EDs were never inline-resolved (verified by reading `m3_sim_verification_ledger.json`; none of the 4 EDs appear in M3's 23 ledger entries). Track C remains an independent ED-disposition track, not an M3 prerequisite.

### A.M4 — Unit State Management
**Status:** ✅ **DONE** (commit `e33849c`, 2026-05-16)
**Shipped:** `tests/sim/v17-integration/m4_unit_state.py` · schema-complete 9-class roster · per-faction `defaultdict(lambda: defaultdict(int))` semantics · Muster + commit-to-battle (model b) + loss application · JSONL serialization. Note: M4 ships as "schema-complete, semantics-partial" per the commit message — A1/A2/A3/A4/A5 cross-reference M4's aggregate-count assumptions (see M3's A5 in particular).
**Follow-ups:** semantics-partial gaps will surface in M3 / M6 / M7 integration; not blocking work in those modules but worth scanning M4's own assumption ledger before M7.

### A.M5 — Settlement-Territory Aggregation
**Status:** PENDING M1 · **Claude-safe once M1 lands**
**Dependencies:** A.M1 (settlement state)
**Owns:** new file `tests/sim/v17-integration/m5_aggregation.py`
**Entry checklist:** resume from M1 or M2 handoff; full-read `settlement_layer_v30.md §4.3`, `§3`.

**Work:**
- Settlement Order → Province Accord aggregation at arc boundary
- Settlement events (revolt at Order 0, famine, Domain Echoes) feed territory state
- RM Cell Resilience: +1 Ob to suppression at ≥3 settlements
- Economic effects: settlement Prosperity → territory Wealth modifiers
- 10+ tests


**Blockers:** none beyond M1 dependency.

### A.M6 — Faction Action Expansion
**Status:** PENDING M1–M5 · **Claude-safe once chain clears**
**Dependencies:** A.M1, A.M2, A.M3, A.M4, A.M5
**Owns:** new file `tests/sim/v17-integration/m6_faction_actions.py`
**Entry checklist:** resume from latest A.Mx handoff; full-read `faction_canon_v30.md`, `victory_v30.md §3.1`, `peninsular_strain_v30.md §5`.

**Work:**
- Crown Initiative 3 modes: Royal Progress / Great Work / Coronation Renewal
- Church Absolution at Mandate cost
- RM Uprising (from `victory_v30 §3.4`)
- Varfell Colonist/Transformation
- Hafenmark Trade Network
- Updated AI scoring for all new/revised actions
- 20+ tests

**Blockers:** none. (Track D ratifies personal-scale duel mechanics; faction-level AI scoring does not materially consume that surface. Informational only.)

### A.M7 — Integration + Balance Sweep
**Status:** PENDING M1–M6 · **Claude-safe once chain clears**
**Dependencies:** all M1–M6 complete and unit-tested
**Owns:** new file `tests/sim/v17-integration/mc_v17.py` (the integration), JSONL outputs
**Entry checklist:** resume from M6 handoff; verify all M1–M6 commit SHAs match manifest; pre-flight smoke test.

**Work:**
- Wire all modules into `mc_v17.py`
- N=1000 balance sweep across parameter grid
- Wilson CI check: all factions ∈ [20%, 30%] at 95% confidence
- Sensitivity analysis on key parameters
- JSONL output to audit dir
- NERS audit pass on integrated engine
- If Wilson CI fails: parameter-sweep loop until convergence or hit Phase 1b sweep budget

**Exit:** Track A complete; unblocks Track H (Godot kickoff).

**Blockers:** none if M1–M6 ratify cleanly.

---

## Track B — Combat Integration Sessions B → F

**Purpose:** Continue personal-scale combat integration. Session A complete and audited; Session B prepped via handoff at `tests/handoffs/2026-05-15_combat_integration_session_a_to_b.md` (commit `fc0053a`).

**Manifest:** `simulation` task type. Reference: `tests/sim/combat_integration/session_a_chassis.py` (commit `b31c84c`).

All Track B sessions call:
```python
h.task_gate('simulation')
# at artifact production:
h.completeness_gate('simulation', scope={'systems_touched': ['combat'], 'integration_module': 'session_<X>_chassis.py'}, claim='full-canon')
```

### B.Session B — Feint, Establish Distance, Escape
**Status:** PREPPED · **Jordan-gated** on Q10–Q11 (handoff exists)
**Entry checklist:**
- `bootstrap simulation`
- `view /mnt/user-data/uploads/handoff_2026-05-13.md` if uploaded, else `g.read_files_graphql(['tests/handoffs/2026-05-15_combat_integration_session_a_to_b.md'])`
- Read handoff in full per PI `<read_handoffs_fully>`
- Full-read: `designs/scene/combat_v30.md`, `params/combat.md`
- Verify Session A chassis at `b31c84c` is the base

**Work:**
- Extend Session A chassis with Feint (PP-294), Establish Distance, Escape
- Resolve two open Jordan decisions surfaced in handoff: distance system (binary vs graduated), STR multiplier (text vs example reconciliation)
- Match v2 reference matchups (diagnose I14/I15 deviations)

**Exit handoff:** `tests/handoffs/2026-05-1X_combat_integration_session_b_to_c.md` with same schema.

**Blockers:** two Jordan decisions before Session C.

### B.Session C — Disarm, Tie Up, Retrieve, Dodge
**Status:** SCOPED · **Jordan-gated** (awaits Session B)
**Dependencies:** B.Session B
**Work:** add four maneuvers to chassis; canon-check against `combat_v30.md` maneuver section.
**Blockers:** Session B blockers + any Jordan decisions on the maneuver cost economy.

### B.Session D — Rescue, Fibonacci, multi-combatant
**Status:** SCOPED · **Jordan-gated** (awaits Session C; ED-823 affects Fibonacci denominator)
**Dependencies:** B.Session C
**Work:** multi-combatant orchestration; Fibonacci-divided pool integration (ED-823 may modify denominators).
**Blockers:** ED-823 disposition (Track C).

### B.Session E — Stunt
**Status:** SCOPED · **Jordan-gated** (awaits Session D)
**Dependencies:** B.Session D
**Work:** Stunt mechanic; cross-reference duel Session arena Stunt findings (Track D).
**Blockers:** Track D ratification status.

### B.Session F — Balance review + NERS
**Status:** SCOPED · **Jordan-gated** (awaits Session E)
**Dependencies:** B.Sessions B–E
**Work:** full chassis balance review; NERS audit all six directions; canonization commit if PASS.
**Blockers:** none beyond chain.

---

## Track C — Mass Battle ED Disposition

**Purpose:** Dispose four open P1/P2 EDs (ED-811 / ED-813 / ED-822 / ED-823). Originally framed as "blocking A.M3" in v1; A.M3 shipped without resolving these (verified via `m3_sim_verification_ledger.json` — none of the four EDs appear in M3's 23 raised entries). Track C is now an **independent ED-disposition track** for hygiene + future calibration work, not an M3 prerequisite.

**Manifest:** `audit` task type (closing existing EDs).

**Status:** READY · **Jordan-gated** on Q1–Q4 (no track now depends on it; runs in 1 session whenever Jordan provides decisions).

**Downstream relevance:**
- ED-823 (Fibonacci denominator) still relevant for B.Session D combat integration (multi-combatant resolution).
- ED-811 / ED-813 / ED-822 inform any future mass-battle re-calibration; not blocking M3 / M6 / M7 as currently scoped.

**Entry checklist:**
- `bootstrap general`
- `h.task_gate('audit')` (uses `audit` manifest)
- Full-read: `canon/editorial_ledger.yaml` (each of the four entries)
- Full-read: `designs/provincial/mass_battle_v30.md`, `params/mass_combat.md`
- Full-read: `designs/audit/2026-05-15-mb-comparative-audit/plan.md` (consolidated plan from `a734f63`)
- Check Track E lock on ledger; if E is open, wait

**Work — entries to dispose:**

| ED | Topic | Decision needed |
|---|---|---|
| ED-811 (P1) | Engagement damage formula | Margin-of-net-successes vs net-successes×(1+Power); fix `SIM-MB-04 FINDING-1` |
| ED-813 (P2) | Withdrawal phase gate | Phase 5 vs Phase 3 placement; `SIM-MB-04 FINDING-7` |
| ED-822 (P2) | Volley/Engagement composition balance | Adopt TN7 primary fix; raise ED-825 for secondary composition-balance measure (Phase 3+ work) |
| ED-823 (P2) | Combined-attack effectiveness calibration | Fibonacci denominator options a/b/c; defer SIM-MB-06 rebuild or close-with-decision |

**Additionally surface to ledger** (from cross-system audit `ad109dde`):
- Concentration range 2–14 vs Stamina 2–8 inconsistency (Grand Debate immunity edge case)
- Any further B-* findings from that audit not yet in ledger

**Exit checklist:**
- Each ED gets `status: resolved` + `jordan_decision: <date> — <text>` + `resolution_commit: <sha>`
- Single commit `[editorial] mass battle ED disposition — ED-811/813/822/823`
- Citations block listing all canon files consulted
- Handoff: not needed if single-session close

**Blockers:** Jordan decisions on each ED. Surface options inline; do not assume.

---

## Track D — Duel Architecture Ratification

**Purpose:** Close 5 open Jordan questions on duel architecture v9. Reference: `tests/sim/duel_architecture_stress_01/` (commits `3b1c497` through `570d373`).

**Manifest:** `propose_mechanic` task type if ratification adds new canonical mechanics; else `audit`.

**Status:** BLOCKED · **Jordan-gated** on Q5–Q9.

**5 open questions (per handoff in chat `9a035656`):**

1. 2H bonus stacking: cap at −0.5 (test-recommended) or stack at −1.0 (original directive)
2. Warhammer balance: STR×3 at TN 7.0 (14–17 dmg/hit) — acceptable or rebalance
3. Pierce vs Heavy = `floor(STR/2)`: keep for half-sword accuracy, or use flat +1
4. Normal weight STR multiplier: ×1 (current) or ×1.5
5. Duel system ratification: now, or wait for weapon v2 to stabilize (Track A / Track B)

**Entry checklist** (when Jordan unblocks):
- `bootstrap design` or `simulation`
- `h.task_gate(<type>)`
- Full-read: `params/combat.md`, `designs/scene/combat_v30.md`
- Read all duel commits since `3b1c497` chronologically

**Work:** decision per question → if ratifying, append canonical entries to `params/combat.md` with PP-prefix; commit `[editorial] PP-### duel architecture v9 ratification`. If deferring, write disposition to `tests/sim/duel_architecture_stress_01/disposition_2026-05-XX.md`.

**Blockers:** all 5 questions for Jordan.

---

## Track E — Editorial Hygiene

**Purpose:** Clear bootstrap warnings; restore ledger compliance.

**Manifest:** `infrastructure` task type.

**Status:** 🟡 **PARTIALLY DONE** — ledger archival complete (commit `d98192b`, 2026-05-16: archived 8 resolved entries ED-832..ED-839); freshness refresh shipped separately (commit `4c9770c`, 2026-05-16: `freshness_gate --update`). Remaining: any new auto-fixable violations that surface during M5–M7 work.

**Bootstrap warnings to resolve:**
- `canon/editorial_ledger.yaml` 2,838 tokens (threshold 2,000) — `[ERROR] [AUTO-FIXABLE] size_exceeded` + `archive_needed`
- 4 stale canonical sources flagged by freshness_gate

**Entry checklist:**
- `bootstrap general`
- `h.task_gate('infrastructure')`
- Skeleton + full-read: `canon/editorial_ledger.yaml`
- Skeleton + full-read: `references/canonical_sources.yaml`
- Identify which 4 sources are stale (SHA mismatch via freshness_gate)
- Check Track C lock on ledger; if C is open, wait

**Work:**
- Run `atomizer.archive_by_status` (auto-fix on ledger) — moves resolved entries to next archive range file
- Regenerate `canon/editorial_ledger_summary.yaml` via `tools/index_gen.py` if available; else hand-regen
- Run `freshness_gate.py --update` on the 4 stale sources
- Commit `[infrastructure] Compliance auto-fix: archive ledger + freshness refresh`
- Single commit, no handoff needed

**Blockers:** if `tools/index_gen.py` defect (per arch v2.3 open_items M6) corrupts summary YAML: stop, surface to Track F.2, do not commit a bad summary.

---

## Track F — Architecture / Tooling Debt

**Purpose:** Close open architecture-spec items.

**Manifest:** `infrastructure` task type.

### F.4 — Freshness gate batch + cache
**Status:** ✅ **DONE** (commit `d72cc86`, 2026-05-16)

**What it fixed:** `assert_bootstrap` freshness loop fired 106 GraphQL calls per bootstrap (one per `canonical_sha` pair, uncached). With concurrent sessions sharing the per-PAT 5000/hour budget, the project routinely exhausted GraphQL mid-session and blocked all writes for ~30+ min. The 2026-05-14 cache work covered file-content caching but did not cover per-pair SHA lookups.

**Implementation:** `tools/freshness_gate.py` gains `get_blob_shas_batch(paths)` — 1 GraphQL call for ≤200 paths via alias queries. `valoria_hooks.assert_bootstrap` gains `/home/claude/.freshness_cache.json` keyed by `sha256(canonical_sources.yaml content)` with 10-min TTL.

**Measured:** freshness GraphQL cost 106 → 0–1 per bootstrap.

### F.5 — Compliance check result cache
**Status:** ✅ **DONE** (commit `a41af6b`, 2026-05-16)

**What it fixed:** `compliance_check.check_all` fired ~30 GraphQL calls per bootstrap via 6 `read_files_graphql(..., skip_cache=True)` invocations. The `skip_cache=True` was correct for `context_gate` accounting (tool-side bulk fetches shouldn't count as Claude-side conversation tokens) but bypassed the GraphQL-budget cache as a side effect.

**Implementation:** `compliance_check.check_all_cached(repo)` caches the violations result keyed by current HEAD OID with 10-min TTL. Reuses `_github_ops._fetch_head` when a prior fetch this session has populated it (0 extra GraphQL on warm). `valoria_hooks.assert_bootstrap` prefers the cached entry via `getattr` for graceful rollout.

**Measured:** compliance GraphQL cost ~30 → 0–1 per bootstrap.

### F.6 — Rate-limit pre-check
**Status:** ✅ **DONE** (commit `d72cc86`, 2026-05-16, bundled with F.4)

**What it fixed:** GraphQL budget exhaustion produced opaque `KeyError('data')` failures mid-commit, orphaning in-flight work. No early-warning mechanism existed.

**Implementation:** `assert_bootstrap` calls REST `/rate_limit` (free, not rate-limited) and bands the response: HALT < 200 remaining, WARN < 1000, INFO < 3000, silent otherwise. Hard halt before budget exhaustion produces a clear `RuntimeError` instead of mid-flight failure.

**Net effect of F.4+F.5+F.6 (measured end-to-end, fresh subprocess):**
- Cold-cache bootstrap: 130 → 12 GraphQL/call (11× reduction)
- Warm-cache bootstrap: 130 → 2 GraphQL/call (65× reduction)
- Per-hour bootstrap budget ceiling (across all concurrent sessions): ~38 → ~2500
- GraphQL budget no longer the project bottleneck

### F.1 — `print_status_block` drift fix
**Status:** READY · **Claude-safe** (default fix-path (a); Q14 only if Jordan vetoes default)
**Severity:** P2 — bootstrap uses `quick_bootstrap()` workaround; PI script as-written halts

**Issue:** PI `<bootstrap_script>` calls `g.print_status_block(token)`. Function does not exist in `github_ops.py` (verified 2026-05-16). Every bootstrap currently routes through `quick_bootstrap()` workaround.

**Two valid fixes:**
- **(a)** Add `print_status_block(token)` to `github_ops.py` — fetches both-repo HEADs, parses session-log regex, formats output. Honors PI as-written.
- **(b)** Update PI `<bootstrap_script>` to call `quick_bootstrap()` directly. Lower-friction fix but PI loses the explicit Status Block contract.

**Recommendation:** (a). PI text is the contract; code should honor it. `quick_bootstrap` exists for in-session subprocess re-bootstrap, not session-start.

**Entry checklist:**
- `bootstrap infrastructure`
- `h.task_gate('infrastructure')`
- Full-read: `skills/valoria-orchestrator/scripts/github_ops.py` (full file)
- Full-read: `skills/valoria-orchestrator/scripts/valoria_hooks.py` (focus: `assert_bootstrap`, `context_gate`)
- Full-read: `tests/hooks/` directory (existing tests for these primitives)

**Work:**
- Implement `print_status_block(token)`: fetch both-repo HEADs via `gh_api`, parse current session_log + ledger_summary + file_index_summary, format the Status Block to match PI bootstrap script's expected output
- Add tests under `tests/hooks/test_print_status_block.py`
- Commit `[infrastructure] github_ops: implement print_status_block per PI bootstrap contract`
- Citations block listing PI script reference

**Exit:** PI v2.1 changelog entry (or note in commit msg) acknowledging drift closed.

**Blockers:** none.

### F.2 — `tools/index_gen.py` M6 rewrite
**Status:** SPECCED · **Claude-safe** (rewrite is mechanical per architecture v2.3)
**Severity:** P2 (blocks strict YAML consumers; current regex-tolerance carries us)

**Per architecture v2.3 `<open_items>`:** `tools/index_gen.py` produces malformed YAML (HTML comments embedded), archive-blind `next_id`. Bootstrap regex-reads tolerate; strict `yaml.safe_load` halts.

**Entry checklist:**
- `bootstrap infrastructure`
- `h.task_gate('infrastructure')`
- Full-read: `tools/index_gen.py` (existing)
- Full-read: `canon/editorial_ledger.yaml` + archive files (for `next_id` correctness)
- Full-read: `references/canonical_sources.yaml`

**Work:**
- Rewrite generator: emit valid YAML (round-trip verified before write); archive-aware `next_id` (scan all `editorial_ledger_archive_*.yaml`); comprehensive tree walk of canonical directories (not regex-over-prior-summary)
- Schema version: bump `schema_version` field; bootstrap consumers warn on mismatch
- Tests under `tests/tools/test_index_gen.py`
- Migrate bootstrap consumers from regex to strict `yaml.safe_load` in a follow-up commit (do not bundle — landing migrations together = no rollback granularity)

**Blockers:** none.

### F.3 — CI Level 5 (GitHub Actions)
**Status:** SPECCED · **Deferred** (aspirational per architecture v2.3; multi-session)
**Severity:** P3 (local hooks are sole enforcement; `--no-verify` is the leak)

**Work:** add `.github/workflows/` mirroring local hook gates. Out of scope for short sessions; multi-session task. Defer until F.1 + F.2 land.

---

## Track G — Pre-firearms Research Integration

**Purpose:** Propagate 6 P1/P2 drift findings from `research/pre_firearms_formations/` (commits `8d71638` through `bd0b0ba`) into game design.

**Manifest:** `propose_mechanic` task type for P1 propagations; `audit` for P2 surface-to-ledger.

**6 findings** (per chat `22bbcf87` synthesis):

| Sev | Finding | Action |
|---|---|---|
| P1 | Prediction-tech corrupts T-9 (discipline-timing under uncertainty) + T-10 (secondary-commit surprises) | Player-side projection only; AI plans hidden behind doctrinal-posture cues |
| P1 | Cultural-doctrinal compatibility filter (T-17, M-6) absent | Faction cultural-attitudes as doctrine-constraint primitives (3–5 traits/faction) |
| P2 | Universal victory conditions contradict T-18 | Faction-specific victory conditions |
| P2 | Cross-battle doctrinal learning (M-5) absent | AI doctrinal-distribution shifts on player's recent doctrines |
| P3 | Steppe horse-archer asymmetry (T-14) untreated | Asymmetric resolution rules for steppe-doctrine factions |
| P3 | Threadwork-transition narrative arc undesigned | V1 campaign spans threadwork-transition; doctrines fail across arc; M-5 as central narrative |

**Tier-1 (P1):** propagate immediately; affects A.M3 / A.M6 reads. **Jordan-gated** — Tier-1 findings add new primitives (`cultural_attitudes` faction state, AI projection-info hiding); both require design intent confirmation before commit.
**Tier-2 (P2/P3):** ED entries; defer propagation to dedicated session. **Claude-safe** — ledger entries are findings (status: open, jordan_decision: pending), not commitments.

**Entry checklist:**
- `bootstrap design`
- `h.task_gate('propose_mechanic')` for P1; `h.task_gate('audit')` for ED-only Tier-2
- Full-read: `research/pre_firearms_formations/16_*.md` (historical vs game-design comparison)
- Full-read: `designs/provincial/mass_battle_v30.md`, `designs/scene/combat_v30.md`, `params/mass_combat.md`

**Work — Tier-1:**
- Add `cultural_attitudes` primitive to faction state (3–5 traits/faction)
- Update mass_battle AI doctrine selection to read `cultural_attitudes`
- Add player-side projection cues; remove perfect-info AI predictions
- Commit `[editorial] pre-firearms research Tier-1 propagation — cultural attitudes + doctrinal posture`
- Citations block

**Work — Tier-2:** append ED entries to `canon/editorial_ledger.yaml` with `status: open` and `jordan_decision: pending`. Each ED references the research file by line number.

**Blockers:** Track A.M1 / A.M3 / A.M6 must skeleton-fetch design files *after* Tier-1 commits land.

---

## Track H — Godot Kickoff (specced, deferred)

**Purpose:** Begin `jordanelias/valoria-game` implementation consuming canon from `ttrpg`.

**Manifest:** new task type needed: `godot_implementation`. **Define task manifest before first H-session.**

**Status:** DEFERRED · **Jordan-gated** on Q15 (unblocks when A.M7 PASSES).

**Pre-conditions:**
- Track A.M7 Wilson CI ∈ [20%, 30%] all factions confirmed
- Track B Sessions B–F complete (combat chassis ratified)
- Continuous engine (ED-833) is canonical reference for any randomness implementation

**H.0 — Setup (1 session):**
- Define `canon/task_manifests/godot_implementation.yaml`
- Inventory current `valoria-game` repo state (last commit pre-2026-05-14)
- Decide: which canonical layer to implement first (recommended: continuous-engine dice + derived-stats from `params/core.md` + `derived_stats_v30.md`)
- Commit task manifest to `ttrpg`; commit project skeleton scaffolding to `valoria-game`

**H.1 — Continuous engine + derived stats (1–2 sessions):**
- Godot 4.6 implementation of continuous-engine sampler (Normal-distribution per `params/core.md` §Continuous Engine)
- Implement derived-stats layer per `derived_stats_v30.md`
- Unit tests in Godot's GUT framework
- Statistical equivalence check vs `mc_v17.py` reference

**H.2..N — incremental subsystem implementation:**
- Each subsystem (combat, mass-battle, settlement, faction-action) gets a dedicated session-pair (implementation + cross-validation)

**Blockers:** A.M7 PASS, B.Session F complete, task manifest definition.

---

## Open questions blocking specific tracks

| # | Question | Blocks | Surface |
|---|---|---|---|
| Q1 | ED-811 engagement damage formula resolution | Track C (ED hygiene) | Jordan decision; surfaced in chat `67ed7db1`. Reframed v2.2: A.M3 shipped without using this resolution. |
| Q2 | ED-813 withdrawal phase gate (Phase 3 vs 5) | Track C (ED hygiene) | Jordan decision. Reframed v2.2: A.M3 shipped without using this resolution. |
| Q3 | ED-822 Volley/Engagement composition: TN7 alone, or TN7 + secondary measure | Track C (ED hygiene) | Jordan decision. Reframed v2.2: A.M3 shipped without using this resolution. |
| Q4 | ED-823 Fibonacci denominator path a/b/c | Track C (ED hygiene) → B.Session D | Jordan decision. B.Session D still consumes this for multi-combatant resolution. |
| Q5 | 2H bonus stacking cap | Track D ratification | Jordan decision |
| Q6 | Warhammer balance at STR×3 | Track D ratification | Jordan decision |
| Q7 | Pierce vs Heavy formula | Track D ratification | Jordan decision |
| Q8 | Normal weight STR multiplier | Track D ratification | Jordan decision |
| Q9 | Duel ratification timing | Track D | Jordan decision |
| Q10 | Distance system: binary or graduated | Track B Session B | Jordan decision; surfaced in chat `e5b812c2` |
| Q11 | STR multiplier text vs example reconciliation | Track B Session B | Jordan decision |
| Q12 | Decision A revisit (revert of PP-717 D2) — Phase 8 finding | Combat balance | Jordan decision; surfaced in chat `ad109dde` Phase 8 close |
| Q13 | Pool advantage acceptance (Reframing 2) vs address | Combat design intent | Jordan decision |
| Q14 | F.1 fix (a) implement vs (b) update PI | Track F.1 | Jordan decision (default (a) per recommendation) |
| Q15 | Track H first-implementation-layer selection | Track H.0 | Jordan decision when H unblocks |
| Q16 | A.M3 A1 — faction-specific tactic card mechanical effects in M6: accept M3's "register only" + M6 overlay pattern, or implement Stratagem's two-pass resolution requirement (architectural impact on M3 → M6 interface)? | A.M6 | Jordan decision; from `m3_sim_verification_ledger.json` provisional_assumptions[0] |
| Q17 | A.M3 A3 — damage-allocation policy: keep "weakest defender first" as global default, or specify per-faction AI overrides at M6/M7? | A.M6 / A.M7 | Jordan decision; from M3 ledger A3 |
| Q18 | A.M3 A4 — disposition table B6 from §B.3 Step 2 is not in current canon; accept the §B.4-per-card pool-modifier interpretation as canonical, or surface B6 from archive if it exists? | A.M3 / A.M7 | Jordan decision; from M3 ledger A4 |
| Q19 | A.M3 A5 — morale check fires per unit class that took any losses (aggregate-count semantics from M4). Accept "any-loss-checks-route" policy as canonical, or escalate per-unit Health tracking? | A.M6 / A.M7 | Jordan decision; from M3 ledger A5 + M4 A5 cross-reference |

---

## Track close protocol (uniform)

When a track session ends, **always**:

1. `h.completeness_gate(task_type, scope, claim='full-canon')` if claiming completion
2. `h.safe_commit(additions, deletions, message)` with `Citations:` block
3. `g.write_handoff(handoff_dict)` if track continues. Schema per `_validate_handoff_schema` (`github_ops.py` line 1542):
   ```yaml
   id: <unique-id>                              # required
   task:                                        # required
     skill: <skill-name>                        # required
     description: <one-line summary>            # required
   context_files:                               # required, non-empty
     - path: <repo path>                        # required
       depth: full | skeleton                   # required, must be one of these two
       reason: <why next session needs this>    # required
       repo: ttrpg | valoria-game               # optional, defaults to 'ttrpg'
   working_state:                               # required
     next: [<at least one item>]                # required, non-empty list
   last_commit: <sha>                           # required
   owns: [<at least one path/glob>]             # required, non-empty list
   ```
   Common halts: empty `next`, empty `owns`, missing `depth` on context_files entry, invalid `depth` value.
4. `g.close_session_log(...)` — closes per-session file (not legacy `safe_session_close`)
5. `g.print_resumption_block(handoff_id)` for the next session's copy-paste resume

If session ends mid-track (context exhausted, blocker hit): `status: in_progress`, handoff includes exact resumption point.

---

## Changelog

- **2026-05-16 v2.2** — Pass-3-on-v2.1 patch. (1) **P1**: launch-order section rewritten to reflect M2/M3/M4 + Track E + F.4/F.5/F.6 DONE — N=1/N=2/N=3 pickup sequences now start from M1 / F.1, no longer recommend starting on shipped modules. (2) **P2**: A.M2/M3/M4 bodies compacted — pending-style Entry/Work/Blockers sections replaced with `Shipped:` + `Follow-ups:` summary. (3) **P2**: Track C purpose rewritten — "blocking A.M3" framing removed; Track C is now an independent ED-disposition track. Verified via reading `m3_sim_verification_ledger.json` (commit `dc9a71a`) that ED-811 / ED-813 / ED-822 / ED-823 are NOT among M3's 23 raised entries — A.M3 shipped without resolving or using those EDs. (4) **P2**: Q1–Q4 reframed to remove stale `→ A.M3` downstream; Q4 retains B.Session D downstream. (5) **Verification finding** added inline to A.M3 entry: 5 provisional assumptions in `m3_sim_verification_ledger.json` await Jordan ratification — A1/A2/A3/A4/A5 listed with topic + follow-up path. (6) **New open Qs**: Q16–Q19 surfaced from M3's provisional assumptions (faction-specific tactic-card mechanical effects, damage-allocation policy, disposition table B6 absence, morale check per-loss vs per-unit-Health).
- **2026-05-16 v2.1** — Reflects live state at 20:13 UTC. A.M2/M3/M4 marked DONE (committed by concurrent session at `29b5242`, `dc9a71a`, `e33849c`). Track E marked PARTIALLY DONE (ledger atomizer `d98192b`, freshness sync `4c9770c`). Track F gains F.4/F.5/F.6 DONE entries (GraphQL leak fix at `d72cc86`, `a41af6b`; bootstrap cost 130 → 2 GraphQL/call warm cache). Completed-workstreams section augmented. Throughput-reality table rebuilt: GraphQL no longer a constraint; new "DONE" class added; pickup recommendation updated to A.M1 as next Claude-safe critical-path item.
- **2026-05-16 v2 (originally pending, superseded by v2.1)** — Pass-3 patch. Added `<throughput_reality>` and `<completed_workstreams>` sections, per-track Status annotations (Claude-safe / Jordan-gated / Chain-dependent / Deferred), corrected A.M2 false Track-C dependency, softened A.M6 Track-D dependency, added Track B hook-call block matching Track A pattern, corrected handoff schema example to match `_validate_handoff_schema` at `github_ops.py:1542` (was P3, upgraded to P2 during Pass 3). Rebuilt launch-order recommendations Claude-safe-first; Worker 3 at N=3 gets fallback when Jordan-gated chain stalls.
- **2026-05-16 v1** — Initial workplan. 8 tracks (A–H). Reflects 169 commits / 72h ttrpg surface as of `48f8360`. Successor to ad-hoc multi-session coordination via handoff system shipped 2026-05-14.
