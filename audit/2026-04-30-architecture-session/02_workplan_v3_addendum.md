# Valoria Workplan v3 — Addendum (2026-04-30)

**Anchor:** `designs/workplans/valoria_workplan_v3_consolidated.md` (commit 27e1875, 2026-04-28).
This addendum **does not supersede** v3. It records what shifted in the 2-day window since v3 was published, integrates findings from the week-audit (`2026-04-30_week_audit_NERS.md`), and re-sequences the next ~20 sessions of work.

**Authority:** Jordan owns N/Ω/Μ/М-tier decisions (per v3 §0). Claude executes Q + protocol. PROVISIONAL items here remain PROVISIONAL until Jordan ratifies.

---

## §A · Status Delta Against Workplan v3

What v3 listed vs what is now true.

### A.1 Phase 0 (Foundation) — mostly CLEARED, one defect

| v3 item | Status now | Notes |
|---|---|---|
| 0.1 Register truthfulness | **DONE** | applied_commit SHAs populated PP-663..674 (commit 3d7e46b, Apr 28) |
| 0.2 P0 + threadwork triage | **DONE** | 28 P0s classified (3edf7f0, Apr 28) |
| 0.3 Params staleness | PARTIAL | values_master + alias_registry seeded; numeric_bounds_report exists; 5 real conflicts surfaced, not yet resolved |
| 0.4 Engine integrity | NOT-EVALUATED-THIS-WEEK | No engine-layer commits this week |
| 0.5 CI/orchestration | **DONE** | compliance_check + freshness_gate fixes (052b82d, b07c459) |
| 0.6 Status reconciliation | **DONE** | conversion_ledger updated (e4a62db, valoria-game) |
| 0.7 Governance | PARTIAL | top-level README in (b5ca0a7); 8 governance items declared-deferred (a266b80) |
| **NEW: hook coverage gap** | **OPEN** | ED-762 duplicate ID committed; CI did not block; `assert_unique_ids` missing |

### A.2 Phase 1 (P1 Blockers) — substantial progress, decisions pending

| v3 item | Status now | Notes |
|---|---|---|
| 1.1 Knot Formation During Play | **OPEN** (Jordan-decision) | Listed in ED-755 BLOCKED carryovers |
| 1.2 Accord Propagation to Settlement Order | **OPEN** (Jordan-decision) | Listed in ED-755 BLOCKED carryovers |
| 1.3 Derived Stats Numerical Calibration | OPEN | depends on 1.2 |
| 1.4 Faction Politics Simulation | PARTIAL | SIM-A..H ran against doc 12 (political dynamics, which is faction politics' authoritative spec); 9 design-fails + 8 gaps + 7 friction surfaced + patched |
| 1.5 Coverage matrix P1 EDs (588/589/612) | NOT-EVALUATED | No commits referenced these IDs this week |
| 1.6 ED-543 Clock registry | **DONE** | Resolved 88a82ce (Apr 26) |
| 1.7 PP-666 trio formal vetting | PARTIAL | PP-666 vetting block added (ba7497d, Apr 28); ED-710 settlement adjacency + ED-711 fractional province still open |
| 1.8 Varfell victory paths editorial rewrite | NOT-EVALUATED | No commits |
| 1.9 F2.5 Intelligence stat STRUCK verification | **REOPENED** | c2effdd (Apr 29) recommends *restoring* Intelligence as 6th stat — direct reversal of ED-748. Now in Jordan-decision queue |
| 1.10 F2 verification batch ED-745..748 | **DONE** | 7f640e5 (Apr 28) verified IP=20, IAC STRUCK, PW STRUCK; ED-748 partially reopened by 1.9 above |
| 1.11 ED-768 orphaned PROVISIONAL markers | **DONE** | e79105c (Apr 26) |

### A.3 Phase 2-3 — new center of mass: doc 12 (Political Dynamics)

The week's flagship work. Not in v3 by name (v3 references it under 1.4 Faction Politics Simulation, but the depth surprises the original estimate).

- doc 12 v1.0 → v1.2 in 4 days. Currently 1958 lines, PROVISIONAL.
- 8-stage simulation chain (SIM-A..H) + narrative pass + cross-system batch 3 + synthesis (doc 19/21) + final NERS audit (doc 22).
- 18 forward-looking observations tracked separately for post-canonical iteration.
- doc 22 itself recommends a v1.2.1 cleanup pass before promotion.

### A.4 Phase 4 (Full-Campaign Sim) — partially executed under different framing

The simulation chain SIM-A..H was Phase-4-grade work but ran against doc 12 specifically, not against full-campaign feature coverage. v3 §6.2 lists ~130 features for sim coverage; this week's chain covered the political-dynamics subset.

### A.5 Phase 5 (Godot Prep) — UNCHANGED, the structural problem

- 5 valoria-game commits this week (Apr 28 only): GameMode strip, README rewrite, CI workflow, conversion_ledger update.
- Zero scene work, zero GDScript, zero param-binding.
- 174:5 design:implementation ratio confirms v3's Phase 5 has not started, despite Phase 0 nearing completion.

---

## §B · Critical Path — Next 3 Sessions

The audit's three immediate findings drive these. **Sequence is mandatory** — each unblocks the next.

### Session N+1 (immediate, ≤2 hours)

| Step | Action | Owner | Acceptance |
|---|---|---|---|
| B1 | Resolve ED-762 collision: renumber doc 12 v1.2 entry to ED-763 (deliberately-skipped slot is now used) | Claude | `editorial_ledger.yaml` has unique IDs; `propagation_map` updated |
| B2 | Add `assert_unique_ids` hook covering `editorial_ledger.yaml`, `editorial_ledger_archive.yaml`, `patch_register_active.yaml` | Claude | Hook raises on duplicate; CI passes; existing files validate clean |
| B3 | Move CI-01, CI-02 to closed in session log carryover | Claude | session_log_current open_items list reflects actual state |
| B4 | Fix `editorial_ledger_summary.yaml` p1_blocker_count (currently reads 0; live ledger has ED-755 BLOCKED + ED-750/751 P1 = 3) | Claude | Summary count matches live ledger count |
| B5 | Cohesion → Discipline bulk-fix via `valoria_bulk_fix.py` | Claude | All Cohesion refs in design canon → Discipline; verify against PP-232 |

**Exit criteria for N+1:** Ledger integrity restored, hook coverage closed, vocabulary debt cleared, summary truthful.

### Session N+2 (Jordan-decision sweep, 60-90 min)

The single largest velocity drag. All items can be answered yes/no/defer in batch.

| Cluster | Count | Items |
|---|---|---|
| ED-755 BLOCKED batch | 4 + carryover | E-38-A/B symbolic_effects (keep+define vs cut 210-entry); E-TOP-A opacity stance; ST-31-B NPC self-monitoring; R-41-A crisis masking persistence |
| Doc 17 §6 carryover | 4 | Intelligence stat (6th faction stat) — c2effdd reversal proposal; LICENSE/GOV-08; §1.1 Knot Formation; §1.2 Accord Propagation |
| Mass-battle decisions | 8 | MB-01..08 from 1d9f864 |
| Mass-battle interdependency | 8 | INTER-10d, 12b, 14a, 14d, 14e, 12e, 17b, 09d from a50f098 |
| PP-676 v3 §V3-10 priority | 5 | NPC Behavior audit pass; isolate promotion to first-class docs; vocabulary debt sweep three concentrated cleanups; Turmoil + IP change-control |
| Outstanding | 3 | PT-01; ACCT-01; PP-677 throughline mappings ratify/revise |

**~32 decisions total.** Each is yes/no/defer. Format as a single batch document Jordan reviews top-to-bottom.

**Exit criteria for N+2:** All 32 items have a recorded decision (yes / no / defer with date / needs-more-context). Decisions committed to ledger as resolutions.

### Session N+3 (doc 12 promotion or v1.2.1 cleanup)

Driven by Jordan-decision N+2 outcomes.

**Branch A (promote v1.2 to canonical):**
- Run §13 Promotion Checklist on doc 12 v1.2 (1958 lines).
- Resolve any §13 items not satisfied.
- Promote: move to `designs/political_dynamics_v30.md` (or final canonical path).
- Archive ED-762 (after dedup), ED-755, ED-750/751.
- Update `references/canonical_sources.yaml`.

**Branch B (v1.2.1 cleanup first):**
- Apply doc 22 recommendations: cut coup/war/peace; apply §17 addendum surgically.
- Re-vet against §13.
- Then promote (one session later).

**Recommendation:** Branch A unless Jordan-decision N+2 surfaces blockers. The bloat doc 22 flagged is real but not promotion-blocking. Promote, then iterate.

**Exit criteria for N+3:** doc 12 is canonical or has a freeze date for v1.2.1.

---

## §C · Mid-Range Plan — Sessions N+4 through N+10

Once the critical path clears, the plan branches into three tracks running in parallel.

### Track 1 — Mechanical debt closure (1-2 sessions)

| ID | Item | Effort | Prereq |
|---|---|---|---|
| C1.1 | Doc 17 batch 3 application — 15 P2 patches (ED-752): concern_history cooldown, Knowledge Decay, npc_observes_event visibility gate, Opinion lazy init, Grieving Mood, Knot integration via Outreach (S-LAT-A fix), scars split, Vindicated/Resolved triggers, population_disposition recalc, Outreach Priority 3, NPC Standing §8.1, generate_new_project two-tier, ~80 visible_actions templates, Passive NPC Memory replacement | 0.5 session | doc 12 promotion path settled (B Branch A or v1.2.1 frozen) |
| C1.2 | Doc 17 batch 4 application — 16 P3 stub resolutions (ED-753) | 0.3 session | C1.1 complete |
| C1.3 | Doc 17 batch 5 application — 4 featured-behavior items (ED-754) | 0.2 session | C1.1 complete |
| C1.4 | PROVISIONAL→canonical sweep — 8+ ledger items currently PROVISIONAL | 0.5 session | Jordan-decision sweep N+2 done |
| C1.5 | PP-297 + PP-351 P1 resolution (28 days unresolved, Apr 2 origin) | 0.5 session | Read context; may require Jordan input |
| C1.6 | PP-653 P1 resolution (12 days unresolved, Apr 18 origin) | 0.3 session | Read context |
| C1.7 | params staleness 5-conflict resolution (from Apr 24 values_master seed) | 0.3 session | None |

**Track 1 total: ~2.6 sessions.**

### Track 2 — v3 carryover (settlement adjacency, fractional province) (2-3 sessions)

These are P2 in v3 §3.2 (1.7 sub-items) but have been **untouched since Apr 19**. They are physical infrastructure of the territory↔peninsula scale and block diagonal/vertical NERS robustness.

| ID | Item | Effort | Prereq |
|---|---|---|---|
| C2.1 | ED-710 settlement adjacency graph — full vetting block + N/Ω/Μ/М/Τ/Q evaluation | 1 session | Class A vetting framework (PP-672/674), already in canon |
| C2.2 | ED-711 fractional province ownership — same vetting | 1 session | C2.1 (shared spec) |
| C2.3 | faction_succession_split_v30 — third member of PP-666 trio | 0.5 session | C2.1, C2.2 |
| C2.4 | Cross-doc propagation: 15-25 individual rules in 7 docs need settlement targeting (per v3 §3.1 item 1.2) | 1 session | C2.1, C2.2 |

**Track 2 total: ~3.5 sessions.** Maps to v3 Phase 1.7 (PP-666 trio) and 1.2 (Accord Propagation).

### Track 3 — Implementation rebalance (the structural fix, ≥3 sessions)

The single highest-leverage track. Goal: break the 174:5 design:impl ratio. Even one Godot scene committed to valoria-game with canon-bound parameters changes the project's center of gravity.

| ID | Item | Effort | Prereq |
|---|---|---|---|
| C3.1 | Choose ingestion target: smallest viable scene that exercises a canonical mechanic. Recommended: Wager arc (social_contest §6) — discrete, parameter-driven, narratively complete | 0 (decision) | Jordan input |
| C3.2 | Build GDScript Resource schema for `params/contest.md` values (Wager-relevant subset) | 1 session | C3.1 |
| C3.3 | Build minimal scene tree: NPCEntity, ContestController, WagerResolver — reading from C3.2 resources | 2 sessions | C3.2 |
| C3.4 | Connect to scale-transition stub: scene-scale Wager → personal-scale resolution → settlement-scale outcome write-back | 1 session | C3.3, single-writer Opinion model from doc 12 v1.2 |
| C3.5 | Commit a sim-vs-engine parity test: same Wager scenario in TTRPG sim and Godot scene; outputs match | 1 session | C3.4 |

**Track 3 total: ~5 sessions for first scene.** This is **v3 Phase 5** activated against a single mechanic, ahead of full Phase 4 calibration. Departure from v3's strict phase order is justified by the 28-day implementation gap.

### Tracks parallel — sessions N+4..N+10 budget

| Track | Sessions | Cumulative |
|---|---|---|
| Track 1 (debt closure) | 2-3 | N+4..N+6 |
| Track 2 (PP-666 trio) | 3-4 | N+5..N+8 (overlaps T1) |
| Track 3 (Godot first scene) | 5 | N+5..N+10 (overlaps both) |

If sessions are roughly weekly: **6-7 weeks** to clear N+1 through N+10. If denser: **3-4 weeks**.

---

## §D · Decision Queue — Jordan-Action Items

All items requiring Jordan to choose. Format mirrors what session N+2 should produce. Each gets a **Yes / No / Defer (date) / Needs-more-context**.

### D.1 ED-755 BLOCKED batch

| # | Item | Default recommendation (per doc 17 §6) |
|---|---|---|
| D1.1 | E-38-A: keep symbolic_effects 210-entry table OR cut and define inline at use sites | Default: keep (cut would create 210 inline definitions) |
| D1.2 | E-38-B: define symbolic_effects axes formally OR document-as-designed | Default: define |
| D1.3 | E-TOP-A: opacity stance on diagonal chains — opaque (engine) vs surfaced (UI) | Default: surface, per "engaging game world" intent |
| D1.4 | ST-31-B: NPC self-monitoring scope (full / partial / none) | Default: partial (cost vs realism) |
| D1.5 | R-41-A: crisis masking persistence (transient vs persistent flag) | Default: persistent flag with decay |

### D.2 Doc 17 §6 carryover

| # | Item | Notes |
|---|---|---|
| D2.1 | Intelligence stat as 6th faction stat — restore (per c2effdd) or keep STRUCK (per ED-748) | c2effdd argued from Renaissance political-infrastructure review; ED-748 had STRUCK it as redundant. **Direct contradiction needs resolution.** |
| D2.2 | LICENSE / GOV-08 — choose license; populate top-level LICENSE | CC-BY-SA / GPL-3 / proprietary / CC0 are common videogame-design choices |
| D2.3 | §1.1 Knot Formation During Play — Disposition+5+TS≥30→Spirit/TN7/Ob2 procedure approve or revise | Proposed default in v3 §3.1 item 1.1 |
| D2.4 | §1.2 Accord Propagation to Settlement Order — `Province Accord = floor(mean settlement Order)` approve or revise | v3 §3.1 item 1.2 |

### D.3 Mass-battle decisions (16 items)

From 1d9f864 (8 patch decisions) + a50f098 (8 interdependency decisions). **Compile into single batch sheet for review** rather than enumerate here — reduces cognitive load.

### D.4 PP-676 v3 §V3-10 priority items

| # | Item |
|---|---|
| D4.1 | NPC Behavior audit pass — green-light / scope / defer |
| D4.2 | Isolate promotion to first-class docs — which isolates (5 of 7 Convictions, 3 of 4 Pressure Points)? |
| D4.3 | Vocabulary debt sweep — three concentrated cleanups (per PP-676 v3 finding) — list and approve |
| D4.4 | Turmoil change-control review |
| D4.5 | IP change-control review |

### D.5 Outstanding singletons

| # | Item |
|---|---|
| D5.1 | PT-01 — Pressure Token canonical handling (status?) |
| D5.2 | ACCT-01 — Accounting (16-Accounting trace surfaced from SIM-F? Or older?) |
| D5.3 | PP-677 throughline → system mappings (43 active throughlines × 2-6 systems each) — ratify provisional, revise specific cells, or full re-execute |
| D5.4 | Doc 12 v1.2 promotion — Branch A (promote now) or Branch B (v1.2.1 cleanup first) |
| D5.5 | Implementation rebalance scope (Track 3 above) — first-scene target = Wager arc, or different |

**Total: ~32 decisions across 5 clusters.** Pack into one document, present in priority order, time-box to 90 minutes.

---

## §E · Long-Range Plan — Sessions N+11 onward

Once critical path clears and tracks 1-3 reach milestone, the project is positioned for v3's full Phase 4 → Phase 6 sequence.

### E.1 Phase 4 (Full-Campaign Simulation) — re-scope

v3 §6 estimates 8-12 sessions for Phase 4. The doc 12 chain effectively executed a portion: SIM-A..H + narrative + cross-system batch covered the political-dynamics subset (~30 of v3's ~130 sim features). Remaining:

| Sub-area | Coverage status | Sessions |
|---|---|---|
| 4.0-4.1 Architecture + initialization | NOT-STARTED | 2 |
| 4.2 Season resolution engine | NOT-STARTED | 3-4 |
| 4.3 Feature coverage (~130 features, ~30 covered) | PARTIAL | 0.5 (track residuals) |
| 4.4 Baseline analysis (50 runs) | NOT-STARTED | 1-2 |
| 4.5 Stress tests (8 scenarios) | PARTIAL (SIM-A..H done for political dynamics; 8 broader stress scenarios remain) | 1-2 |
| 4.6 Calibration report | NOT-STARTED | 1 |
| 4.7 Regression | NOT-STARTED | 1 |

**Phase 4 remaining: 9-12 sessions.** Slight reduction from v3's 8-12 because doc 12 chain absorbed some Phase 4.5 work.

**Hard prerequisite for Phase 4:** v3's 2.2 Co-Movement (P2) and 0.7 governance complete. Co-Movement was not advanced this week; remains a Phase 2 dependency.

### E.2 Phase 5 (Godot Prep) — split into 5a / 5b

The audit's structural finding suggests splitting v3's Phase 5 into two halves:

| Phase | Items | Sessions | Trigger |
|---|---|---|---|
| **5a (early implementation)** | C3.1-C3.5 above (Wager-arc first scene + parity test) | 5 | Run in **parallel** with Tracks 1-2 |
| **5b (full Godot prep)** | v3 §7.1-7.5 minus 5a items | 4-6 | After Phase 4 calibration gate passes |

This is the addendum's primary structural recommendation. **5a is justified by:** (1) breaking the 174:5 ratio; (2) catching design defects via parity-test feedback before full Phase 4 invests 9-12 sessions; (3) honoring stated intent ("Valoria is a videogame only").

**Risk of 5a:** Wager-arc spec keeps changing (5 commits this week alone touched social_contest §6.1.1, §7.2). Mitigation: select a Wager arc **state** (specific commit SHA) and freeze it for the duration of 5a. Subsequent design revisions go to 5b.

### E.3 Phase 6 (First Playable) — unchanged from v3

v3 §8 estimates 2-3 sessions. Gated on Phase 5b GAP closure. No re-scope warranted.

### E.4 Phase 7 (Ongoing Maintenance) — add three new maintenance items

v3 §9.6 lists M-tier maintenance items. Add:

| ID | Item | Cadence |
|---|---|---|
| M+1 | PROVISIONAL→canonical promotion sweep | One session per week |
| M+2 | Workplan-execution linkage check (commits referencing v3 stage IDs) | Per-session at bootstrap |
| M+3 | Lateral cross-system invariant simulation pass | One session per quarter |

---

## §F · Process Improvements (parallel, not session-blocking)

Items that improve velocity but do not gate other work.

| ID | Item | Effort |
|---|---|---|
| F1 | Workplan-ID prefix convention in commits — e.g., `[v3 §3.1.1.7]` or `[W-042]` | 0.1 session (decide convention) + ongoing |
| F2 | Commit→stage automated rollup tool — generate weekly burndown vs v3 | 1 session |
| F3 | Decision-queue automation — script that emits a single batch document from `BLOCKED` items in ledger + carryovers in session log | 0.5 session |
| F4 | Hook coverage audit — beyond `assert_unique_ids`, what other invariants does the file system want? | 1 session |
| F5 | PROVISIONAL marker dashboard — count, age, source — surfaced in `editorial_ledger_summary.yaml` | 0.5 session |

---

## §G · Effort Re-Estimate (relative to v3 §11)

v3 estimated 22-34 sessions for full project completion. Updated estimate:

| Phase | v3 estimate | Updated estimate | Delta | Reason |
|---|---|---|---|---|
| 0 Foundation | 1-2 | **0.5** | -1 to -1.5 | Mostly done this week |
| 1 P1 Blockers | 2-3 | **2-3** | 0 | Some done (1.6, 1.10), some surfaced (1.9 reversal); net wash |
| 2 Calibration Inputs | 3-5 | **3-5** | 0 | Untouched this week |
| 3 Polish + Authority | 2-3 | **2-3** | 0 | Doc 17 batches 3-5 fold in |
| 4 Full-Campaign Sim | 8-12 | **9-12** | +1 | Doc 12 chain absorbed some 4.5 work; net slight reduction in 4.5, but 4.0-4.4 untouched |
| 5a Early implementation | (not in v3) | **5** | +5 | New track |
| 5b Full Godot prep | (rolled into 5) | **4-6** | -1 to -2 | Some workplan_final items absorbed by 5a |
| 6 First Playable | 2-3 | **2-3** | 0 | |
| **Total** | **22-34** | **27.5-39.5** | **+5 to +5.5** | Implementation rebalance is the additive cost |

**Critical-path minimum: ~27 sessions** (was 22). The +5 is the cost of activating implementation early. Without it, the design canon completes faster on paper but the videogame remains undelivered.

---

## §H · Updated Critical Path Diagram

Modified from v3 §12. New nodes in **bold**.

```
Phase 0 (Foundation) — 0.5 session remaining
  ├── 0.1-0.6 ✓ DONE
  ├── 0.7 PARTIAL (governance items declared-deferred, ok for now)
  └── B1-B5 IMMEDIATE ─→ ledger integrity + hook coverage + vocab debt

Session N+2: Jordan-decision sweep (32 items)
  ├── ED-755 BLOCKED batch (5)
  ├── Doc 17 §6 carryover (4)
  ├── Mass-battle decisions (16)
  ├── PP-676 v3 priority (5)
  └── Singletons (3)

Phase 1 (P1 Blockers) — 2-3 sessions remaining
  ├── 1.1, 1.2 ──→ unblocks 1.3, 1.4, settlement infrastructure
  ├── 1.5 Coverage matrix P1 EDs (588/589/612)
  ├── 1.7 PP-666 trio (settlement adjacency, fractional province) ◄── Track 2
  ├── 1.8 Varfell victory paths editorial rewrite
  └── 1.9 Intelligence stat — Jordan must reconcile c2effdd vs ED-748

Phase 2 (Calibration) — 3-5 sessions remaining
  ├── 2.2 Co-Movement ⚠ HARD DEP for Phase 4
  ├── 2.5 Settlement economy (depends on 1.2 + 1.3)
  ├── 2.6 RM victory (depends on 2.4)
  └── 2.13-2.20 post-2026-04-18 P2s

Phase 3 (Polish + Authority) — 2-3 sessions remaining
  ├── Doc 17 batches 3-5 (debt closure Track 1)
  └── Authority decisions (rolling, from N+2 sweep onward)

Phase 4 (Sim Framework) — 9-12 sessions
  ├── 4.0-4.1 Architecture
  ├── 4.2 Engine
  ├── 4.3 Coverage validation (residuals after doc 12 chain)
  ├── 4.4 50-run baseline
  ├── 4.5 Stress tests (8 scenarios beyond doc 12 chain)
  ├── 4.6 CALIBRATION GATE ⚠
  └── 4.7 Regression

Phase 5a (Early implementation) — 5 sessions ◄── PARALLEL with Track 1, 2
  ├── C3.1 Choose ingestion target (Wager arc recommended)
  ├── C3.2 GDScript Resource schema for params/contest.md
  ├── C3.3 Minimal scene tree (NPCEntity, ContestController, WagerResolver)
  ├── C3.4 Scale-transition stub (scene → personal → settlement)
  └── C3.5 Sim-vs-engine parity test ⚠ VALIDATION GATE

Phase 5b (Full Godot prep) — 4-6 sessions ◄── after Phase 4
  ├── 5.1-5.5 workplan_final items (less 5a coverage)
  ├── 5.G GAP closure
  ├── 5.W Wave 1 proposals
  └── 5.A Architecture reconciliation

Phase 6 (First Playable) — 2-3 sessions
  ├── 6.1 Season loop end-to-end
  └── 6.4 Q-elegance audit ⚠ EXIT GATE

Phase 7 (Ongoing) — permanent
```

**Critical path:** B1 → B2 → N+2-decisions → 1.1 → 1.2 → 1.3 → 2.2 → **5a** → 4.0 → 4.2 → 4.4 → 4.6 → 4.7 → 5b → 6.1 → 6.4

**Parallel tracks:** Track 1 (debt) and Track 2 (PP-666 trio) run alongside Phase 1; Track 3 (5a) runs alongside Phases 1-3.

---

## §I · Risk Register Update

Audit's R1-R9 mapped to v3's §15 Risk Register and this addendum.

| Audit risk | v3 §15 mapping | Addendum response |
|---|---|---|
| R1 Implementation lag is structural | (not in v3) | §E.2 Phase 5a track |
| R2 Doc 12 churn risks instability | (not in v3) | §B Session N+3 (promote or freeze v1.2.1) |
| R3 Hook coverage incomplete | partial (v3 0.5 references CI/freshness only) | §B B2 + §F F4 |
| R4 Cross-cutting peer-system density | (not in v3) | §E.4 M+3 lateral simulation pass |
| R5 Workplan-execution unjoined | (not in v3) | §F F1, F2 |
| R6 PROVISIONAL backlog growing | partial (v3 §9 maintenance) | §E.4 M+1 |
| R7 Carryover P1s aging | (not in v3 explicitly) | §C C1.5, C1.6 |
| R8 Atomization residual debt | v3 §3.A | §C C1 absorbs |
| R9 Vocabulary debt residuals | (not in v3) | §B B5 |

---

## §J · What Success Looks Like

Per project-stated NERS lens (R: "fully formed, error-free and complete opportunities for engaging the player"):

**End of Session N+1:** Ledger integrity restored. Hook coverage extended. Vocabulary debt cleared. Status reports truthful.

**End of Session N+3:** Doc 12 either canonical or has a freeze date. ~32 Jordan-decisions resolved. P1 ledger has zero BLOCKED items.

**End of Session N+10:** First Godot scene committed to valoria-game executes a Wager arc parity-tested against TTRPG sim. Design-impl ratio is < 10:1. Tracks 1-2 cleared.

**End of Phase 4 (~N+22):** Calibration gate passes. ~130 sim features covered. 50-run baseline produced. Engine has been stress-tested through 8 scenarios.

**End of Phase 6 (~N+27 to N+39):** One full season playable end-to-end in Godot. Q-elegance audit passes. **Project achieves stated intent.**

---

## §K · What This Plan Does Not Cover

To make scope explicit:

- **Content authoring** (faction names, scenario writing, art/sound assets, narrative copy). v3 §10 declares this out-of-scope until First Playable. Maintained.
- **Marketing / distribution / community.** Out-of-scope.
- **Multiplayer / networked play.** Out-of-scope unless Jordan opens it.
- **Modding interface.** Implicit in GDScript Resource schemas (C3.2) but not designed.
- **Localization.** Out-of-scope.

---

**End addendum.**

*Generated 2026-04-30. Anchors `valoria_workplan_v3_consolidated.md` (commit 27e1875) and `2026-04-30_week_audit_NERS.md`. PROVISIONAL pending Jordan review.*
