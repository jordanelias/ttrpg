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
1. Track E completes ledger archival → unblocks bootstrap warnings cluster.
2. Track C disposes ED-811 / ED-813 / ED-822 / ED-823 → unblocks A.M3 (mass battle resolution canonical questions).
3. Track G commits Tier-1 propagations (P1 drift findings) → unblocks A.M1 / A.M3 / A.M6 canonical reads.
4. Track A.M1–M6 complete → unblocks A.M7 (integration sweep).
5. Track B Sessions B–F complete → unblocks final personal-scale combat ratification.
6. Track A.M7 PASSES (Wilson CI ∈ [20%, 30%] all factions) → unblocks Track H Godot kickoff.

---

## Recommended session-launch order

**N = 1 (sequential single worker):**
E → C → G(Tier-1) → A.M4 → A.M1 → A.M2 → A.M5 → A.M3 → A.M6 → B → D → A.M7 → F → H

**N = 2 (two concurrent workers):**
- Worker 1 (critical path): E → A.M4 → A.M1 → A.M2 → A.M5 → A.M3 → A.M6 → A.M7
- Worker 2 (parallel): C → G(Tier-1) → B → D → F → G(Tier-2) → H-spec

**N = 3 (three concurrent workers):**
- Worker 1 (critical path): A.M4 → A.M1 → A.M2 → A.M5 → A.M6 → A.M7
- Worker 2 (mass-battle subtrack): C → A.M3 → G(mass-battle research integration)
- Worker 3 (parallel-independent): E → B → D → F → G(Tier-2) → H-spec

Idle time at N≥3 is unavoidable around merge points 2 and 3. Worker who finishes early picks up E or F.

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
**Status:** READY (next_action per session_log_current.md)
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

**Exit handoff schema:**
```yaml
track: A.M1
status: complete
owns: [tests/sim/v17-integration/m1_church_infrastructure.py]
next: A.M2
context_files:
  - path: tests/sim/v17-integration/m1_church_infrastructure.py
    reason: M1 implementation; M2 imports infrastructure-state dataclass
  - path: tests/sim/v17-integration/module_manifest.md
    reason: dependency declarations + canonical-source list
  - path: designs/provincial/ci_political_v30.md
    reason: M2 next reads §1–§3 for milestone changes
blockers: []
```

**Blockers:** none (foundational module).

### A.M2 — CI Political Revision
**Status:** PENDING M1
**Dependencies:** A.M1 (consumes infrastructure-state)
**Owns:** new file `tests/sim/v17-integration/m2_ci_political.py`
**Entry checklist:**
- Resume from A.M1 handoff
- `h.task_gate('simulation')`
- Skeleton + full-read: `ci_political_v30.md` §1–§3, `victory_v30.md` §3.2
- Verify M1 commit SHA matches handoff `last_commit`

**Work:**
- CI milestones: 55 (Institutional Reach: +1 Ob to anti-Church), 80 (Church Ascendant: Seizure −1 global, PT drift +1), 100 (Theocracy Unification Attempt)
- Revised Mass Seizure: targets all Church-building territories, individual Ob per territory
- CI cap ±5/season from all sources, ±3 from player Domain Actions
- Verify Hafenmark suppress (−1 CI if Hafenmark L ≥ 4)
- 10+ tests; integration smoke-test against M1 baseline

**Exit handoff:** standard, next=A.M5 (per critical-path order) or A.M3 (if N≥2 worker available).

**Blockers:** ED-822 / ED-823 dispositions may modify Mass Seizure target set. Coordinate with Track C status before M2 starts.

### A.M3 — Mass Battle Resolution
**Status:** PENDING M4, BLOCKED on Track C dispositions
**Dependencies:** A.M4 (unit state), Track C resolution of ED-811 / ED-813
**Owns:** new file `tests/sim/v17-integration/m3_mass_battle.py`
**Entry checklist:**
- Confirm Track C closed ED-811 (engagement damage formula) and ED-813 (withdrawal phase gate)
- `h.task_gate('simulation')`
- Full-read: `mass_battle_v30.md` §B.2, §B.3, `params/mass_combat.md`
- Verify Track G mass-battle integration propagations are landed (P1 findings from `bd0b0ba`)

**Work:**
- `resolve_battle()` replacing single-roll Military Conquest
- 6-step BG resolution: tactic declaration → disposition lookup → pool construction → roll → margin → outcome
- Active classes: Levy, LightInf, HeavyInf
- Tactic cards from canonical set
- Fort dice in defense
- Outcomes: territory transfer, unit losses, Accord/Stability triggers
- 15+ tests; cross-validate against earlier `sim_mb_06_v25.py` battery (the v25 calibration battery is in `tests/sim/sim_mb_06_v25.py`)

**Blockers:** Track C must close ED-811 and ED-813 before M3 starts. If C is open, **do not** pick up M3 — pick up A.M4, A.M5, or another non-A track.

### A.M4 — Unit State Management
**Status:** READY (parallel-startable with M1)
**Dependencies:** none (foundational; parallel-track-startable)
**Owns:** new file `tests/sim/v17-integration/m4_unit_state.py`
**Entry checklist:**
- `bootstrap simulation`
- `h.task_gate('simulation')`
- Full-read: `mass_battle_v30.md` §B.2, `params/mass_combat.md` unit-stats section
- Skeleton: `integration_plan_v3 §5 Phase 2c` (model b for adjacent-territory commit)

**Work:**
- Per-faction unit roster: `defaultdict(lambda: defaultdict(int))`
- Active classes: Levy, LightInf, HeavyInf with Martial/Endurance/Discipline
- Muster action: mint Levy tokens in territory
- Commit-to-battle: tokens from adjacent territory (model b)
- Loss application reduces roster
- JSONL serialization
- 10+ tests

**Blockers:** none.

### A.M5 — Settlement-Territory Aggregation
**Status:** PENDING M1
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
**Status:** PENDING M1–M5
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

**Blockers:** Track D outcomes may add personal-scale ratifications that affect AI scoring; check D status.

### A.M7 — Integration + Balance Sweep
**Status:** PENDING M1–M6
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

### B.Session B — Feint, Establish Distance, Escape
**Status:** PREPPED (handoff exists)
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
**Status:** SCOPED, awaits Session B
**Dependencies:** B.Session B
**Work:** add four maneuvers to chassis; canon-check against `combat_v30.md` maneuver section.
**Blockers:** Session B blockers + any Jordan decisions on the maneuver cost economy.

### B.Session D — Rescue, Fibonacci, multi-combatant
**Status:** SCOPED, awaits Session C
**Dependencies:** B.Session C
**Work:** multi-combatant orchestration; Fibonacci-divided pool integration (ED-823 may modify denominators).
**Blockers:** ED-823 disposition (Track C).

### B.Session E — Stunt
**Status:** SCOPED, awaits Session D
**Dependencies:** B.Session D
**Work:** Stunt mechanic; cross-reference duel Session arena Stunt findings (Track D).
**Blockers:** Track D ratification status.

### B.Session F — Balance review + NERS
**Status:** SCOPED, awaits Session E
**Dependencies:** B.Sessions B–E
**Work:** full chassis balance review; NERS audit all six directions; canonization commit if PASS.
**Blockers:** none beyond chain.

---

## Track C — Mass Battle ED Disposition

**Purpose:** Dispose four open P1/P2 EDs blocking A.M3.

**Manifest:** `audit` task type (closing existing EDs).

**Status:** READY (independent of other tracks; runs in 1 session).

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

**Status:** BLOCKED on Jordan decisions.

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

**Status:** READY (independent, 1 short session).

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

### F.1 — `print_status_block` drift fix
**Status:** READY (blocking bootstrap noise every session)
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
**Status:** SPECCED in architecture v2.3; not implemented
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
**Status:** SPECCED, not implemented; aspirational per architecture v2.3
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

**Tier-1 (P1):** propagate immediately; affects A.M3 / A.M6 reads.
**Tier-2 (P2/P3):** ED entries; defer propagation to dedicated session.

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

**Status:** DEFERRED until A.M7 PASSES.

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
| Q1 | ED-811 engagement damage formula resolution | Track C → A.M3 | Jordan decision; surfaced in chat `67ed7db1` |
| Q2 | ED-813 withdrawal phase gate (Phase 3 vs 5) | Track C → A.M3 | Jordan decision |
| Q3 | ED-822 Volley/Engagement composition: TN7 alone, or TN7 + secondary measure | Track C → A.M3 | Jordan decision |
| Q4 | ED-823 Fibonacci denominator path a/b/c | Track C → A.M3, B.Session D | Jordan decision |
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

---

## Track close protocol (uniform)

When a track session ends, **always**:

1. `h.completeness_gate(task_type, scope, claim='full-canon')` if claiming completion
2. `h.safe_commit(additions, deletions, message)` with `Citations:` block
3. `g.write_handoff(handoff_dict)` if track continues; schema:
   ```yaml
   track: <track-id>
   status: <in_progress|complete|blocked>
   owns: [<file paths>]
   next: <next-track-id|null>
   context_files:
     - path: <path>
       repo: <ttrpg|valoria-game>
       reason: <why next session needs this>
   blockers: [<list>]
   ```
4. `g.close_session_log(...)` — closes per-session file (not legacy `safe_session_close`)
5. `g.print_resumption_block(handoff_id)` for the next session's copy-paste resume

If session ends mid-track (context exhausted, blocker hit): `status: in_progress`, handoff includes exact resumption point.

---

## Changelog

- **2026-05-16** — Initial workplan. 8 tracks (A–H). Reflects 169 commits / 72h ttrpg surface as of `48f8360`. Successor to ad-hoc multi-session coordination via handoff system shipped 2026-05-14.
