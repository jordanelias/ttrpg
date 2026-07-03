# Handoff

Plain, hand-maintained continuity for Valoria. Update this when you pause mid-task; a
git commit *is* the session close. The SessionStart banner (`tools/session_status.py`)
surfaces the "Next actions" section below, alongside `git status` / last commit.

This replaces the old session-log + `canon/session_checkpoint.md` + checkpoint machinery
(which depended on the retired GitHub-API harness and token budgets).

## Lane-tagged handoffs (2026-07-02)

Per-lane continuity now lives in `handoffs/HANDOFF_<LANE>.md`, using the same 9 lane codes as
the `ED-<LANE>-NNNN` editorial namespace (`ED-IN-0001`, `CLAUDE.md` §3). This file is the
**index** plus genuinely cross-cutting items — read the lane file(s) relevant to your session
before starting work, and keep your own updates scoped to your lane's file (or this one, only
for cross-cutting items).

| Lane | Subsystem | File |
|---|---|---|
| `MB` | Mass battle | `handoffs/HANDOFF_MB.md` |
| `PC` | Personal / scene combat | `handoffs/HANDOFF_PC.md` |
| `FI` | Field investigation | `handoffs/HANDOFF_FI.md` |
| `SC` | Social contest | `handoffs/HANDOFF_SC.md` |
| `FA` | Faction actions | `handoffs/HANDOFF_FA.md` |
| `WR` | World | `handoffs/HANDOFF_WR.md` |
| `IN` | Infrastructure / cross-cutting | `handoffs/HANDOFF_IN.md` |
| `GO` | Godot conversion | `handoffs/HANDOFF_GO.md` |
| `SE` | Settlements | `handoffs/HANDOFF_SE.md` |

**Why the split:** the ID-collision incidents that motivated `ED-<LANE>-NNNN` (two same-session
concurrent-allocation collisions on the flat sequence within one PR — see `ED-1094`'s ledger
entry) are the same failure class that makes one shared `HANDOFF.md` a merge-collision magnet
once multiple lane-sessions run concurrently. This is a **partial, deliberate exception** to the
repo's earlier "one continuity surface" consolidation (`deprecated/session_machinery/` retired
per-topic session-log files because they rotted independently) — the difference is this split is
keyed to the SAME lane taxonomy the ID system already enforces, not an ad-hoc per-topic split,
and this root file remains the one stable SessionStart entry point.

**Note on `designs/audit/2026-06-30-open-items-adjudication-docket.md`:** that file (PR #68,
filed concurrently by a different session while this session was independently adjudicating the
same five items from a pasted copy) is now **ADJUDICATED, not still pending** — see its own
updated status header. Verdicts: D1/D5 resolved and struck, D2/D3 still open with materially
changed context, D4 partially done and narrowed. Detail lives in `handoffs/HANDOFF_PC.md` (D1),
`handoffs/HANDOFF_IN.md` (D2/D3/D4/D5), and `decision_queue.md` items 5/12/24/25 — not repeated
here.

**Full detail on the split itself, and every historical decision predating it, is filed at
`handoffs/HANDOFF_IN.md`'s Decisions log** — this root file does not duplicate that history.

## Next actions

- **START HERE — month-overview + consolidation (2026-07-01), doctrine + propagation spec
  RATIFIED (2026-07-02); HANDOFF split into per-lane files (2026-07-02).** The month's
  comprehensive review, the consolidation execution/reconciliation logs, and the single
  consolidated Jordan decision queue live at
  `designs/audit/2026-07-01-month-overview-architecture-consolidation/` (see `decision_queue.md`
  first — every gated item below is indexed there). Highest-leverage queued decisions:
  **doctrine ratification** (ED-1083, `designs/architecture/holonic_container_doctrine_v1.md`),
  **J-38 propagation-spec authorship** (workplan v5 §3 — unblocks conversion register #1 +
  `engine_clock`/ED-1051), Track-2 residuals (below), field-ON, the values_master
  regenerate-vs-retire call, and the duplicate compilation homes.
- **Scene-combat — merged (`d4bf2af3` PR #40, `8fbc4b66` PR #47); next up, all Jordan-gated:**
  1. **Two Track-2 residuals awaiting Jordan's single-source-target decision** (forward_roadmap Track 2;
     "Still open on `main`" above): (a) `wt`/`spd` cost-path de-leak (`core.py:55`, `systems.py:46`) — an
     autonomous before/after measurement harness can be prepped (roster-wide damage/tempo delta report) without
     flipping the live code; (b) `WP.reach()`/`authority()` vs `systems.reach_base`/`wield_heft` canonical-home
     fork (`weapon_physics.py:193,205`) — a short comparison doc of what each side currently computes and where
     they diverge can be prepped without touching code. Neither decision itself is agent-actionable.
  2. **Close the channel-leverage residual (the §C remainder, Phase 4c).** The affinity budget fixed
     total-competence but not per-channel leverage → spanish broad-strong, chinese broad-weak, only 2 niches. The
     fix is the **effectiveness-functions calibration**: measure each channel's marginal win-leverage, then
     normalise so each paradigm is decisive in *its* context (chinese-burst should win a fast/light-weapon
     context; german-bind the longsword context — currently it doesn't). **Design-laden** (how strong each
     paradigm should be = Jordan). Full detail: `designs/scene/combat_engine_v1/phase4_5_plan_v1.md` §4c.
     Re-measure with `python designs/scene/combat_engine_v1/workbench/balance.py context`.
  3. **The abilities-as-access depth** (Phase 4b / REARCHITECTURE P4 / WS-4's other half): the 7 phase-slots +
     techniques-as-permission + the learning-gate ("can't bind-and-wind / Spanish footwork without having
     trained it"); resolves the dormant `eff_cw`. Carries open decisions flagged Jordan's: affinity
     full-point-buy vs thin, the cyclic node relation, naming. **Also gated: Phase 4a**, the full
     game-theoretic psychological layer (Bayesian-signaling reads, mixed-strategy feints, Stackelberg-timing
     initiative, two within-fight dynamics) — never built, and previously undocumented in the repo. Full detail:
     `designs/scene/combat_engine_v1/phase4_5_plan_v1.md` §Phase 4.
  4. **Tunable magnitudes** (Class-C, workbench-adjustable): `RECOVERY_TEMPO_K` (0.15), `LUNGE_*`,
     `CLOSE_REACH_REF`.
  5. **Phase 5 contact axis** (clinch/disengage/choke; consumes the dead `clinch` primitive) — full detail
     `phase4_5_plan_v1.md` §Phase 5 — and **WS-7 multi-combatant envelope** (gated on ED-911 ratification)
     remain design-gated, no immediate action.
  6. **Stale-branch cleanup (needs Jordan's confirmation before deletion):** `design/scene-combat-v1`
     (local+remote) and `origin/scene-combat-track2-cleanup` are fully merged and redundant. Do not delete
     unilaterally — switch the working branch to `main`, confirm no uncommitted work, then offer deletion as
     a separate explicitly-confirmed step.
- **Done this pass:** unified PR #18's net-new into main → **LB-22 complete** (orchestrator retired to
  `deprecated/skills/`; `valoria-vector-audit` read-path rewritten; `ci_hooks_verifier` Check 4 blocking
  for `skills/`). Earlier passes already landed the coverage_matrix single-source + 12-skill boilerplate
  strip (#16) — kept at main's version during the unify.
- **LB-22 residual (small):** `tools/` analysis utilities still carry `/home/claude` refs (WARN tier in
  `ci_hooks_verifier`); flip the `tools/` scope to blocking only after the GitHub-API→working-tree port
  (`freshness_gate`, `broken_dependency_checker`, `compliance_check`, `extract_*`, `valoria_collator`,
  `valoria_bulk_fix`). `valoria-orchestrator`'s old `tests/registry/test_descriptor_registry.py` import
  is dead (reads `/home/claude/…`, not CI-collected) — left as-is.
- **CI debt blocking-flips (LB-23) — reconciled 2026-07-01 (ED-1082):** `validate_ed_citations`
  is **already blocking** (since 2026-06-29, 0 genuine violations — the old "flip once triaged"
  action here was stale). `freshness_gate`'s remaining report-only step is being closed by the
  month-overview consolidation itself (pin refresh + blocking flip as its final commit); the
  optional K-2 SHA-split (115 `canonical_sha` fields → `references/canonical_freshness.yaml`)
  is a refactor that can follow independently, no longer a precondition.
- **`ci_political_v30` read-routing (LB-24):** raw file ~26k but tracked read returns 0 (index-routes).
- **Ledger-status reconciliation (LA-23, Lane A — mostly done):** flipped ED-841/842/912 `open`→`resolved`
  and filed the never-written ED-938/ED-939 (backfilled from #13; artifacts verified). Dropped the
  report-only `validate_ed_citations` count 748→731. **Residual:** ED-914 left `open` — its mechanical
  parts remain (PP-719 record-or-strike; dead `fieldwork_design_v1` parent-path refs in `params/bg/core.md`,
  `designs/scene/fieldwork_v30.md`, `designs/scene/fieldwork_godot.md`).
- **Design-tier docket awaiting Jordan:** J-31 extended (social-contest deliberative-game findings,
  row #39 → LA-19) and the new **J-36** (Key-bus closure for the 6 off-bus writers, row #40 — gated on
  the distillation report's deferred adversarial pass).
- **Mass-battle coordinate-field engine — Stages A–D merged (2026-07-02, PRs #52/#56); next up, all
  Jordan-gated.** Detailed continuity/history lives in the staged plan file (session-local, not in the
  repo tree): `using-opus-4-8-ultracode-floating-tiger.md`. All four stages are `FIELD_MOVEMENT=1`
  opt-in only — the grid path (`FIELD_MOVEMENT=0`, every existing scenario's default) stayed byte-exact
  throughout (`bat.py`'s frozen `unit`/`cell` digests unchanged across every commit in both PRs).
  - **A** — true-adjacency stand-off halt + an exact time-of-impact (continuous-collision) resolver
    (replacing an earlier halved-clamp heuristic), plus a reach-and-facing-asymmetric closing-budget
    throttle (a longer-reach, correctly-facing body "sets into formation" before a shorter-reach one).
  - **B** — facing/attention/reaction physics (anti-hyper-reactivity) on the field path.
  - **C** — command layer: `engine.build_army` (multi-subunit armies), a timed/conditional `Order`
    queue, and `escort_of`/formation-relative positioning.
  - **D** — wires the previously-inert `Subunit.role` (gated by `role_allowed`); new
    `engine.build_envelopment`/`build_refused_flank` realize ED-909's Unit-level "Envelopment"/"Refused
    Flank" postures as compositions of existing primitives (no new movement/combat mechanic).
  - **Open, Jordan-gated:** (1) **LC-8** — literally retiring `Horseshoe`/`RefusedFlank` as
    `Subunit.shape` values (`geometry.CELL_PATTERN_FN`/`config.MIN_DISCIPLINE`) would break the frozen
    `bat.py` grid digests (its own battery uses `Horseshoe` directly), so it needs an explicit
    sign-off + a deliberate re-baseline — deferred, not done in Stage D. (2) Stage E (Army
    Configuration Mode UI) needs a ruling on whether the videogame keeps the TTRPG's Command-rating
    subunit-cap hard limit of 3 or lifts it (`mass_battle_v30.md` §A.5) before it can be built; Stage E
    is also a genuinely different kind of work (frontend/UI over the now-complete engine primitives),
    not a natural default-continue from A–D. (3) Stage F (charge/depth/equipment physics) is only
    scoped at a high level in the plan — needs real design work before implementation.
  first — every gated cross-lane item is indexed there). For subsystem-specific continuity,
  go to your lane's file in the table above; `handoffs/HANDOFF_IN.md` carries the full
  cross-cutting/governance narrative (doctrine ratification, ED-<LANE>-NNNN namespace creation,
  merge-ratifies-by-default convention, ecosystem-review residuals not owned by another lane).
- **Reserved-ID state:** the flat `ED-NNNN` sequence is FROZEN at `ED-1094` (2026-07-02
  cutover, `ED-IN-0001`). All NEW EDs use `ED-<LANE>-NNNN` — `references/id_reservations.yaml`'s
  `lane_ids` section is the live allocation source; read `next_free` for your lane, allocate,
  bump, co-commit. Never max+1.
