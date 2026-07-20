# Month Overview — 2026-06-22 → 2026-07-01

## Status: FROZEN AUDIT ARTIFACT (2026-07-01) — historical record, not a canonical head

Comprehensive review of all work performed in `jordanelias/ttrpg` over the past month,
compiled as step 2 of the 2026-07-01 month-overview + architecture-consolidation session
(see `01_consolidation_execution.md` for what that session changed, and `decision_queue.md`
for everything awaiting Jordan).

**Totals.** 72 commits (the repo's entire tracked history in this environment), 38 distinct
merged PR numbers (#6–#51 range), 2026-06-22 → 2026-07-01, all authored by `jordanelias`
with AI co-execution. Scope-tag mix: `[infrastructure]` 23, `[simulation]` 11,
`[editorial]` 11, `[fix]` 7, `[design]` 3, remainder small/untagged (merges).

**Churn center of gravity.** `designs/audit/` (651 file-touches — audit/workplan churn),
`tests/sim/` (521 — mass-battle suite), `archives/` (197 — deprecation sweep),
`designs/scene/` (109 — combat engine v1), `references/` (99), `sim/` (90), `tools/` (87),
`skills/` (79), `params/` (54), `designs/provincial/` (46), `canon/` (29 — ledger appends).
`HANDOFF.md` touched 15×; `CLAUDE.md` rewritten twice; `CURRENT.md` created (generation v40).

---

## Work streams (chronological)

### A. Session-close / handoff bootstrapping — 06-22
`[infrastructure]` ×5. Closed out prior lanes (lane-A-2026-06-11, active-work-index,
multiunit-envelopment), synced `canonical_sha` pins. Start of tracked history here.

### B. ED-1041 bilateral-Ob wound model — 06-22 → 06-26
Replaced the old "-1D aggressor-only pool penalty" wound model with a bilateral Obstacle
mechanic on a continuous axis (`designs/scene/combat_engine_v1/{core,wrapper}.py`). Two-stage
rollout (initial land → ER-2 continuity fix → bind-resolution extension); PR #12 propagated
`degree()` and removed dead code. Left open by design: **ED-1042** (wound-model spec-vs-code
drift — Jordan decision, still open).

### C. Settlement governance redesign + Goldenfurt slice + territory audit — 06-22 → 06-23
Reworked settlement governance from four stat-pumps into an AP-budgeted verb/Directive/
event-deck loop; built the Goldenfurt vertical slice (6-NPC cast, 28-card deck); closed
audit gap G1 with a settlement registry + ledger (PRs #6/#8/#9). PP-726 migration flagged
half-applied.

### D. Faction-action audit, Passes A–C — 06-22 → 06-23
Three-pass audit of `params/bg/faction_actions.md` + `sim/provincial/faction_action.py`:
citation/naming fixes (PP-428/442/515/555/559) plus a Parliament/Treaty/Occupation extension
pass. Ran "inline" after the audit workflow hit a session limit — early signal of the
tooling fragility later addressed by the CI-native migration (stream G).

### E. Godot personal-combat extraction — 06-23
Extracted the ratified personal-combat engine into the mandated BaseEngine/EngineModule/
KeyBus shape (`designs/godot/skeleton/engines/combat/`), fixed the skeleton's use of the
deprecated v30 model, updated `references/module_contracts.yaml` (personal_combat →
extracted). ED-900/904, docket ED-1029.

### F. NPC v30 comprehensive audit + observability tooling — 06-22 → 06-24
Added `tools/observability/` (lexicon/graph/decisions builders + console UI — a static
design-corpus inspector) and ran a 449-finding audit across 24 NPCs, 6 systems, and
ethics/resonance.

### G. CI / native-tooling migration — 06-24 (the month's pivotal infra event)
Migrated the whole Claude↔GitHub ecosystem off the legacy orchestrator/harness bootstrap
onto Claude-Code-native tooling: versioned `.githooks/pre-commit`, session hooks
(`.claude/settings.json`), a decoupled CI gate aggregator (`valoria-ci.yml`), and a
rewritten `CLAUDE.md` as the operating manual (PR #11 + 5 satellite commits).

### H. J-31 social-contest terminology repair — 06-26
Recovered docket J-31 from a pre-switch WIP stash; renamed social-contest terminology across
22 docs (Past/Future → Memory/Projection etc.), rescaled Composure/Concentration/Health/
Stamina, refreshed 16 `canonical_sha` pins (PR #13). Deliberately parked: the matching
`contest.py` sim edit, blocked on 19 pre-existing uncited constants (fabrication debt).

### I. 2026-06-28 editorial mega-day — PRs #14–#28, #31 (15 commits, largest single day)
- **ED-912** Disposition/Knot unification (flat ±5 swing; resolves ED-841/842/912/914).
- **PP-688** deterministic-narration architecture proposal (architecture only, no schema).
- **Master Workplan v5** (supersedes v4) + LB-22 skill-port cleanup across 12 SKILL.md files.
- **Deprecation/currency sweep**: archived 34 superseded `designs/audit/` folders, declared
  **generation v40** via a new `CURRENT.md` manifest (declarative only — the 138-file rename
  was measured and rejected).
- **ED-citation trustworthiness**: validator precision 741→330 false positives, 93-item
  triage, backlog to zero, gate flipped to **blocking**.
- **`names_index.yaml`** seeded as the single source for definition display names (CI +
  pre-commit wired).
- Distillation-coherence passes (ESCP relabels); duplicate cleanup commits (#21/#31) — a
  re-land artifact.

### J. Scene-combat engine v1 + mass-battle re-architecture — 06-30 (PRs #32–#43)
- **Scene-combat engine v1** (PRs #32/#40): WS-0 state-graph correctness (TA-02,
  RR-01/02/03), WS-6 trace seam + workbench backbone; CANONICAL head at
  `designs/scene/combat_engine_v1/` (d_sigma resolution, additive-coupled damage, ED-1041
  wounds). **ED-1050** resolved by Jordan 06-30: `adef_threshold` re-swept monotone in the
  Python oracle and re-exported to `combat_config.gd` — retiring the port's earlier in-place
  `[AUDIT-FIX]` (the "port must never correct its oracle" rule now enforced by practice).
- **ED-1043** mass-battle bottom-up re-architecture audit: `orchestration.py` flagged as a
  2,899-line god-file, 9 anti-patterns, 6-stage gated roadmap. Stage 1g `engine.py` true
  wrapper (PR #35); Stage 2 standalone weapons/armour equipment modules (PR #38, deliberately
  not yet wired).
- **ED-1053** integrity hardening (PR #36): the three integrity gates ported off the GitHub
  API onto the working tree; first-ever `sim/` seeded regression test + CI job; fabrication
  guard matches `(variable, value)` and full float literals.
- Contest Stage 0/1a: reconciliation contract + numpy-free `sim/autoload/sigma_leverage.py`
  (single-sourcing σ-leverage for combat + social contest, with parity test).
- CLAUDE.md §10 model-tiering guidance for multi-agent work (PR #39).

### K. Coordinate-field + Track-2 + reconciliation — 06-30 → 07-01 (PRs #43–#51)
- Euclidean-distance coordinate field landed behind default-OFF toggles (PR #43/#45);
  **field-ON is an unratified candidate** (gauge OFF 5/13 → ON 4/13 with new H2/H9
  divergences) + a tick-by-tick browser visualizer workbench.
- Track-2 cleanup (PR #47): HEAD_MODE dedup, dead-field retirement, `capabilities.py`
  single-source-drift bugfix (poleaxe gap_thrust).
- Workplan-sprawl cleanup (PR #49): `designs/workplans/` established as the one live master-
  workplan home; the `sim/` vs `tests/sim/` vs `tests/sim_framework/` naming collision
  documented (rename assessed high-blast-radius, deferred).
- Merge-state reconciliation (PR #50): HANDOFF/roadmap still described PR #40/#47 as
  unmerged after landing — fixed, and the "lost" Phase 4/5 plan (existed only as uncommitted
  local plan files) recovered and committed (`phase4_5_plan_v1.md`; Phases 4a/4b/4c/5
  confirmed **NOT STARTED**).
- Track-2 decision prep (PR #51, HEAD): non-invasive measurement harnesses for the two
  Jordan-gated decisions (wt/spd de-leak; reach/authority single-source). No recommendation
  made — awaiting sign-off.

---

## Half-finished register (as of 2026-07-01 HEAD `23add55`)

| # | Item | State | Where |
|---|---|---|---|
| 1 | Coordinate-field **field-ON** mode | UNRATIFIED candidate, default-OFF | PR #45; gauge divergences H2/H9 |
| 2 | Track-2 residuals: wt/spd cost-path de-leak; reach/authority single-source | Jordan-gated; measurement harnesses built | `designs/audit/2026-07-01-scene-combat-track2-decision-prep/` |
| 3 | Scene-combat **Phase 4a/4b/4c + Phase 5** | Plan exists, NOT STARTED | `designs/scene/combat_engine_v1/phase4_5_plan_v1.md` |
| 4 | `contest.py` terminology propagation | Parked on 19-uncited-constant fabrication debt | stream H (J-31) |
| 5 | **ED-1042** wound-model spec-vs-code drift | Open, Jordan decision | ledger |
| 6 | Deprecation sweep combat-folder exclusions | Deferred by design (collision avoidance) | PR #17 |
| 7 | `sim/` vs `tests/sim/` vs `tests/sim_framework/` naming | Documented, unrenamed (blast radius) | PR #49, `sim/README.md` |
| 8 | Generation **v40** | Declarative only (CURRENT.md manifest; no file renames) | PR #17 |
| 9 | Mass-battle Stage 2 equipment modules | Built, deliberately unwired | PR #38 |
| 10 | ED-1050 residual: RESIST/GAP_EXPOSURE re-export to `.gd` | Key-log parity known-red until done | `combat_config.gd` notes |

## Process-fragility findings the consolidation acts on

1. **Currency surfaces drift within days** (PR #50's stale-merge-state bug; HANDOFF's ED
   ceiling stale same-day) → step 10 builds `tools/currency_consistency_check.py`.
2. **Dead machinery fails silently** (`broken_dependency_checker`'s ledger check read a
   nonexistent `.yaml` and returned clean; `.githooks/pre-commit` tracked non-executable, so
   the local advisory tier never ran on fresh clones) → steps 3 fixes both.
3. **Reserved-ID ceilings go stale against the ledger** (blocks A–C overran to 1042;
   `verified_live_max` lagged at 1042 while the ledger reached 1080) → step 1 re-blocks
   (LB-21) and step 10 gauges it continuously.
4. **Auto-extracted registries rot without regeneration gates** (`values_master.yaml`
   indexing a nonexistent file) → step 6 quarantines; typed-params seed (step 8) starts the
   successor discipline.
