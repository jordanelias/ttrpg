# Mass-Battle System — Survey & Inventory

**Date:** 2026-06-30 · **Branch:** `claude/mass-battle-audit-5c6nih` · **Status:** audit (read-only survey)
**Part of:** the bottom-up re-architecture audit (see `README.md`, plan
`/root/.claude/plans/using-opus-4-8-ultracode-floating-tiger.md`).

`[SELF-AUTHORED — bias note: much of the engine surveyed is Claude-authored across prior sessions;
this inventory is stated as an independent reviewer and verifies every path against the working tree.]`

This is directive (1): an exhaustive inventory of the mass-battle system across active, orphaned,
deprecated, and in-progress artifacts — the input set the rest of the audit operates on. Tags:
**ACTIVE** (live/canonical) · **WIP** (staged/in-flight) · **LEGACY** (superseded, retained) ·
**DEPRECATED** (retired) · **ORPHAN** (present, unreferenced).

---

## 1. Canonical design (ACTIVE)

| Path | Note |
|---|---|
| `designs/provincial/mass_battle_v30.md` | Primary canonical spec (v4.8). Part A TTRPG, Part B board-game, Parts D/E world-bridge + consequences. The leading **doc**; the engine leads it on the pool formula (ED-899). |
| `designs/provincial/mass_battle_v30_index.md` / `_infill.md` / `mass_battle_integration_v30.md` | Heading index, infill reconciliation, cross-system integration (faction/military/strategic layers). |
| `params/mass_combat.md` | Parameter sheet (v0.14). Carries the ED-899 supersession banner (engine = `2×Command` pool, Size via Lanchester frontage; ED-1013 smooth `Command×(1+cohesion)`). |
| `params/history/mass_combat.md` | Historical snapshot of the param sheet (tracking). |

## 2. Live engine (ACTIVE) — `tests/sim/mass_battle/`

| Module | LOC | Role |
|---|---|---|
| `orchestration.py` | **2,899** | **God-file** — Subunit/Unit data model, command-pool derivation, Lanchester attrition, targeting/contact, volley, the three battle loops, all phase hooks. |
| `config.py` | 180 | All module-level tunables + the inert `TROOP_TYPE_ROLES`/`ROLE_SPEC` scaffold. |
| `geometry.py` | 364 | Cell-pattern generators (some generative, some table-driven), octagon facing, support vectors, `cell_speed`. |
| `resolution.py` | 121 | σ-leverage head (roll, degree, morale/charge-shock sigma, softcap) — the underloaded "core". |
| `percell.py` | 182 | Per-column density/depth grid (`_ColBlock`), casualty distribution, fatigue, defender-depth, stamina. |
| `engine.py` | 74 | Namespace re-exporter + `MECHANICS` registry (29 mechanics). **Not a real wrapper.** |
| `lanchester_signature.py` | 182 | Lanchester linear/square signature harness. |
| `validators.py` | 382 | State-graph / byte-exact contract validators. |
| `test_persubunit_stress.py` | 285 | Per-subunit stamina/rout stress harness. |

Adjacent provincial sim: `sim/provincial/{massbattle.py, units.py, tactic_cards.py, faction_action.py,
mass_seizure.py}`; cross-scale `sim/cross_scale/handoff_rules.py`.

## 3. Validation gauge + grounding (ACTIVE)

| Path | Note |
|---|---|
| `tests/sim/gauge_mb.py` | The top-down validator: 11 bands (H1–H11/R1–R3/C1–C7) on the decisive split; `single`/`multi` modes; cavalry rows are `PER_CELL=1`-only. |
| `references/historical/mass_battle_gauge_grounding.md` (v2.4) | The academic/historical grounding: Lanchester (Hillestad/Taylor/Armstrong), cavalry (Sidnell/Burkholder/Boddy/Barua), rout (Sabin/Zhmodikov/du Picq/Clausewitz). Every band cited; engine validated *against* bands, bands never lowered. |
| `tests/sim/instrument_battle.py` | Instrumentation/telemetry. |

## 4. Historical research corpus (ACTIVE — unwired to constants)

`research/pre_firearms_formations/` (16 files, `00_MANIFEST.md`..`16_*.md`): exhaustive pre-firearms
formation catalogue with per-formation **geometry (frontage, depth, intervals, alignment)** and the
exact strategy/tactic vocabulary the audit adopts. **This is the primitive source the cell-layout
values must derive from — currently not connected to the engine.** Also
`research/rhetoric_oratory_contest/` (adjacent, not mass-battle).

## 5. Prior design/audit trajectory (ACTIVE references)

| Path | Note |
|---|---|
| `designs/audit/2026-06-01-massbattle-stub-wiring/mb_engine_workplan.md` | The dependency-ordered P-A..P-G workplan (modularize → Lanchester → FM formation/tactic). |
| `…/mb_engine_completeness_audit.md` | Mechanic-wiring completeness: 22 WIRED / 8 PARTIAL / 6 in-scope GAP. |
| `…/mb_lanchester_design.md`, `…/cavalry_shock_design.md` | The two foundational additions' designs. |
| `designs/proposals/pc_formation_system.md` | The bottom-up FM three-level formation/tactic/doctrine design ("emergence, not decree"). PROPOSAL. |
| `designs/proposals/multiunit_envelopment_plan.md` | Army-scale envelopment, Path B (unify the field → envelopment emerges). Phase 0 confirmed. |
| `designs/proposals/mass_battle_shape_echelon_revamp.md` | Echelon shape revisit. PROPOSAL. |
| `references/mass_battle_redesign_workplan_v1.md` | Earlier (v1.1) redesign workplan — note: predates the 2026-06-02 SHAPE-mod retirement; its per-shape `+2D` signatures are **superseded** by the emergent engine. |

## 6. Sim harnesses (mixed)

ACTIVE: `gauge_mb.py`, `mass_battle_stress.py`, `instrument_battle.py`, `test_persubunit_stress.py`.
Scenario records: `sim_mass_battle_SIM-MB-01..05.md` (+ `.py` for 04/05/05c), the `sim_x_0{3,4,7}` /
`sim_x_19` / `sim_x_22` cross-system records.
**LEGACY (consolidation targets):** ~18 evolutionary harnesses `sim_mb_06_v5..v25.py` (+ manifests,
battery, diag, visual) — the engine-evolution lineage, superseded by the modular package;
`tests/sim/v17-integration/m3_mass_battle*.py`; `sim_mass_combat_005.md`,
`sim_var_06_mass_combat_wounds.md`; `tests/sim/v32-combat-balance/`. Audit records:
`audit_sim_mb_06_v14.md`, `audit_sim_mb_06_v16.md`, `phase12_mass_archetype_v0_2026-05-17.md`.

## 7. Completed audits (LEGACY/reference)

`archives/audit/2026-06-09-massbattle-comprehensive/` (analysis + NERS verdict + flow-state critique);
`archives/audit/2026-06-20-massbattle-loose-ends/massbattle_loose_ends_resolution.md` (ED-907 ratified,
ED-1032 fix);
`archives/audit/2026-06-22-massbattle-wiring-historical/wiring_historical_validation.md`;
`designs/audit/2026-05-29-massbattle-sim-foundation/`, `2026-05-28-resolution-diagnostic/`, plus April
batch docs under `designs/audit/mass_battle_*_2026-04-29.md`.

## 8. Continuity / handoffs

`HANDOFF.md` (master), `handoffs/{la-8-massbattle-reconcile-2026-06-15.yaml,
mass-battle-per-subunit-stamina-2026-06-17.yaml, multiunit-envelopment.yaml}`; archived resumes under
`archives/handoffs/massbattle-*`.

## 9. Ledger / registers (ACTIVE)

`canon/editorial_ledger.jsonl` (single-source ED ledger; ceiling **ED-1042**, blocks exhausted —
re-block before new allocation); `canon/patch_register_active.yaml` (the PP-* mass-battle patch set);
`tests/coverage_matrix.md`; `sim_verification_ledger.json` (the sim anti-fabrication backbone).

## 10. Deprecated

`deprecated/params/combat.md`, `deprecated/proposals/combat_v3{1,2}_proposal.md`,
`deprecated/skills/valoria-orchestrator/`, archived ledger YAML snapshots.

---

## 11. In-flight / staged work (WIP) — fold into the roadmap, don't re-derive

| Item | Ref | State |
|---|---|---|
| Formation-drift cell orphaning fix | ED-1032 | resolved in ledger; the structural fix is the kind of mechanics-touch the roadmap Stage 5 absorbs. |
| Per-subunit rout + eroding morale/discipline | ED-1019 | resolved (byte-exact); the subunit granularity it enables is Stage 3's substrate. |
| Troop-taxonomy stat home | ED-1018 | resolved; `Subunit.of_type`/`TROOP_TYPE_STATS` already wire stats — Stage 2a builds on it. |
| Multi-unit envelopment Phases 1–4 | `multiunit_envelopment_plan.md` | Phase 0 confirmed; Phases 1–4 = roadmap Stage 4. |
| Player-control layers (allocation grid, intervention windows) | ED-907 | resolved; flagged videogame-UI/future — Stage 2d surfaces the engine side. |

## 12. Anti-pattern hotspots (pointer; full census in `02_antipattern_census.md`)

`geometry.py` `cell_speed` (L335) + the four table-driven `*_cells` (L19/33/47/60); `config.py`
`SUPPORT_WEIGHTS` (L31), `MIN_DISCIPLINE` (L61), `DAMAGE_BY_DEGREE` (L72), `ANGLE_DEF_MOD` (L65),
the `PC_*` σ block (L82–117), `K_LINEAR`/`K_SQUARE`/`CASUALTY_SCALE` (L39/125/126). Counter-evidence
that the bar is achievable: `arrowhead_cells`/`column_cells` are already generative, and
`SHAPE_OFF_MOD`/`SHAPE_DEF_MOD` were already retired (config.py L58).

## 13. Consolidation worklist (for roadmap Stage 0/5)

1. Archive the `sim_mb_06_v5..v25.py` lineage (+ manifests/battery/diag/visual) and
   `tests/sim/v17-integration/` to `archives/sim/` — keep only the modular package + `gauge_mb.py`.
2. Retire dead stubs surfaced by the engine audit (dormant `_envelopment_sigma`, any `SUBUNIT_ROUT_FLOOR`-class
   fossils, stale docstrings).
3. Collapse the scattered `PER_CELL`/`SIGMA_HEAD`/`MORALE_FIX`/`LANCHESTER_ENABLED` env reads behind one
   wrapper-level configuration surface + the `GRANULARITY` dial.
4. End-state: **one** importable package, **one** wrapper entry point (`resolve_battle`), **one**
   validator (`gauge_mb.py`).

## 14. Git state

Branch `claude/mass-battle-audit-5c6nih` @ `955db15`, working tree clean; `origin` tracking set; no
stash. The ED-1032 / tri-strata propagation commits referenced in older handoffs are already in main's
lineage. No uncommitted mass-battle WIP to recover.
