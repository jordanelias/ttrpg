# Handoff

Plain, hand-maintained continuity for Valoria. Update this when you pause mid-task; a
git commit *is* the session close. The SessionStart banner (`tools/session_status.py`)
surfaces the "Next actions" section below, alongside `git status` / last commit.

This replaces the old session-log + `canon/session_checkpoint.md` + checkpoint machinery
(which depended on the retired GitHub-API harness and token budgets).

## Pending

- **`design/scene-combat-v1`** (22 commits ahead of main, UNMERGED) — the scene-combat engine build (WS-0..WS-8).
  Substantially complete; awaiting Jordan's ratification before merge. See the Decisions entry below and
  `designs/scene/combat_engine_v1/`. Open follow-ups (Jordan's calls) listed in Next actions.

## Decisions

- 2026-06-29 — **Scene-combat engine (`design/scene-combat-v1`, 22 commits, UNMERGED — awaiting ratification).**
  Built the 1v1 scene-combat engine (`designs/scene/combat_engine_v1/`: wrapper=state machine, core=σ-leverage
  resolution, systems=subsystems, tradition=affinity model, combatant/config=continuous morphology, workbench=
  visual tuning + narrated n=1 watch + depth-2 branch explorer). Delivered the 7 requirements (WS-1 state-graph
  integrity+injection points, WS-2 continuous morphology weight=kg + affordance gates, WS-3 bottom-up tradition
  decomposition, WS-4 representation, WS-5 The Approach, WS-6 workbench, WS-8 balancing methodology) + WS-7
  multi-combatant design. Core design decisions this session:
  - **Commitment is a SPECTRUM** — commit is continuous (`2+3·Beta`), not integer rungs; feint↔all-in is one axis.
  - **Commitment = recovery, made PHYSICAL** — overcommit cost scales with how hard the weapon is to arrest, and
    weight is **NON-LINEAR** (`mass**1.5 · pob`): rapier 0.93 < longsword 1.0 < mace 1.45 < poleaxe 2.24.
  - **Grip/stance/lunge DERIVED from morphology, never flagged** (Jordan's directive) — `close_unwieldiness`(reach),
    `can_choke`(grip_len), `lunge_quality`(thrust × non-linear lightness × hand-balance × 1H). Emergent: the
    rapier (long reach, short grip) can't choke → suffers in the close; a longsword lunge ≠ a rapier lunge.
  - **Tempo coupled to commitment+recovery** — a deep/heavy commit costs readiness (slower next action); heavy
    weapons self-regulate. `RECOVERY_TEMPO_K=0.15` (structural ~5pp effect on extremes; magnitude is Jordan's).
  - **WS-4 dissolution** — the channel vector became an **affinity point-buy budget** (equal total per tradition;
    shape=identity, total=equal) + the **imposition gate** (default on). Fixed the `none` injustice (46→49) and
    beats the keep-bias baseline. **Weapons are NOT equalised** (spear 94 / mace 38) — a battlefield weapon ≠ a
    duelling weapon (the contextual-balance principle).
  - **§C verdict — PARTIAL** (honest, refines the "clears §C" commit msg): none-fairness fixed + beats keep-bias,
    but the C1 contextual test (`balance.tradition_context_matrix`) shows only **2 distinct leaders / 5 contexts**
    — spanish broadly strong (clean niche: rapier/measure), chinese broadly weak. Residual = channel **leverage**.
  All gates green; 26 combat tests pass; mirrors fair (~0.50).
- 2026-06-29 — **ED-citation integrity: full reconciliation (292 → 0; gate now BLOCKING).** Diagnosed the
  292 report-only violations: 286 `NONEXISTENT` from **dual ledger-of-record drift** (design docs minted ED
  numbers in inline `[EDITORIAL:]` tables never migrated to the JSONL), 6 `OPEN_AS_BASIS` (2 of them validator
  false positives). Fixed 3 validator defects (`tools/validate_ed_citations.py`): active-ledger precedence
  over stale archives, loud-parse + regex-salvage of 7 malformed archive YAMLs, and same-line basis scoping
  (table-row bleed). **Registered 91 grounded entries** (36 resolved / 12 provisional / 30 open / 13
  needs_jordan) — each verified against its citing doc by per-batch subagents (anti-fabrication). Repointed
  the ED-814→ED-907 phantom and reworded open/provisional over-claims to `pending`. Dropped `continue-on-error`
  on the `ed-citations` CI job + added to `ci-summary` needs. Report:
  `designs/audit/2026-06-28-ed-citation-triage/02_reconciliation.md`. **Residual for Jordan:** 13 needs_jordan
  items (NPC naming ED-634/595–602/610, ED-885 ratification ID); ID collisions ED-408–411/413/417/647.
- 2026-06-28 — **Editorial-ledger relevance triage.** Deep per-item verification of all **93 unresolved**
  entries (82 open + 10 provisional + 1 deferred) against the live working tree, in 6 read-only cluster
  passes. Result: **37 still relevant** (25 real open work + 12 NEEDS_JORDAN), **56 stale**. Applied via
  Workflow D: **31 struck** (21 superseded by later canon — esp. the mass-battle per-cell/Lanchester
  re-architecture + the 2026-06-22 `net-(Ob-0.5)` continuity fix; 10 `[PROPOSED:…]` migration residue),
  **25 resolved** (open-but-done — decision had landed, row never closed). Unresolved queue 93→37.
  ED-citation violations dropped 315→292 as a side effect. Report:
  `designs/audit/2026-06-28-editorial-relevance-triage/relevance_triage.md`. **Residual for Jordan:** 12
  NEEDS_JORDAN items (NPC naming ED-649/650/651, deferrals ED-644/788, design-intent gates
  ED-879/893/911/920/924/1033/1036); three of these (644/649/893) are the OPEN_AS_BASIS citations still
  holding the ED-citation validator report-only.
- 2026-06-28 — **Open-session unification + LB-22 closed.** Reviewed every `origin` session branch;
  six were already squash-merged into main (#14–#21), one (`claude/github-ci-environment-review` = PR #18)
  carried genuinely-unmerged work, and `claude/refresh-state-3m7nL` (abandoned 04-20 pre-migration line
  carrying the retired `session_checkpoint`/`session_log` harness) was excluded from the merge. Unified
  PR #18's **net-new** half (the LB-22 backlog) onto main — its already-landed half (12 skills +
  coverage_matrix, via #16) was kept at main's version, no re-litigation. **LB-22 done:** `valoria-orchestrator`
  retired to `deprecated/skills/`; `valoria-vector-audit` read-path rewritten; `ci_hooks_verifier.py`
  Check 4 flipped to **blocking for `skills/`** (`tools/` stays WARN pending the API→disk port). PR #18
  closed as superseded. `ci_register_size_check.py` taken from #18 (importable, no-PyYAML, ships the
  drift-guard test) with #22's `names_index.yaml` threshold line re-added; `lane_assignments.yaml`
  owns-globs repointed to `deprecated/`.
- 2026-06-28 — **Master Workplan v5** authored (`designs/audit/2026-06-28-recent-work-orchestration/`),
  reconciling the post-v4 work (06-12→06-28) into one register and superseding v4. Roadmap +
  lane_assignments repointed to v5. Ledger verified live: **713** entries / 0 duplicate IDs / ED 1042.
  (v5 de-staled this pass to live HEAD; PRs #16–#22 reconciled — see its §0/§10.)
- 2026-06-28 — **ED-912**: Disposition & Knot unified on a ±5 swing (Bonds ≥5 now a Knot
  prerequisite; break = Disposition −3 / 4 Composure). Resolves ED-841/842/912/914; supersedes
  PP-632/PP-684. Source-of-truth + consumer tail regenerated; "Stance table" rename in combat.
- 2026-06-26 — **J-31** social-contest docket recovered (ED-938/939/1042 + rule resolutions);
  22-doc cross-corpus reference + terminology repair landed (#13). contest.py sim edit deferred
  behind pre-existing sim-fabrication debt (19 uncited constants on main).
- 2026-06-24 — Migrated the Claude↔GitHub automation to a Claude Code-native model:
  retired the `/home/claude` GraphQL/cache/session harness; gates now live once in `tools/`
  and run in CI (authoritative) + local hooks/`.githooks` (advisory). See the migration PR.

## Next actions

_(Reserved-ID blocks are exhausted — ED ceiling 1042 past A/B/C 890–999. Re-block before any new ID
allocation: workplan-v5 **LB-21**, at the next integration pause.)_

- **Scene-combat (`design/scene-combat-v1`) — awaiting Jordan, then merge:**
  1. **Close the channel-leverage residual (the §C remainder).** The affinity budget fixed total-competence but
     not per-channel leverage → spanish broad-strong, chinese broad-weak, only 2 niches. The fix is the
     **effectiveness-functions calibration**: measure each channel's marginal win-leverage, then normalise so each
     paradigm is decisive in *its* context (chinese-burst should win a fast/light-weapon context; german-bind the
     longsword context — currently it doesn't). **Design-laden** (how strong each paradigm should be = Jordan).
     Re-measure with `python designs/scene/combat_engine_v1/workbench/balance.py context`.
  2. **The abilities-as-access depth** (WS-4's other half): the 7 phase-slots + techniques-as-permission + the
     learning-gate ("can't bind-and-wind / Spanish footwork without having trained it"). Carries the open
     decisions the plan flags as Jordan's: affinity full-point-buy vs thin, the cyclic node relation, naming.
  3. **Tunable magnitudes** (Class-C, workbench-adjustable): `RECOVERY_TEMPO_K` (0.15), `LUNGE_*`, `CLOSE_REACH_REF`.
  4. **Ratify → merge to main** (squash; the branch is self-contained under `designs/scene/` + `tests/valoria/`).
- **Done this pass:** unified PR #18's net-new into main → **LB-22 complete** (orchestrator retired to
  `deprecated/skills/`; `valoria-vector-audit` read-path rewritten; `ci_hooks_verifier` Check 4 blocking
  for `skills/`). Earlier passes already landed the coverage_matrix single-source + 12-skill boilerplate
  strip (#16) — kept at main's version during the unify.
- **LB-22 residual (small):** `tools/` analysis utilities still carry `/home/claude` refs (WARN tier in
  `ci_hooks_verifier`); flip the `tools/` scope to blocking only after the GitHub-API→working-tree port
  (`freshness_gate`, `broken_dependency_checker`, `compliance_check`, `extract_*`, `valoria_collator`,
  `valoria_bulk_fix`). `valoria-orchestrator`'s old `tests/registry/test_descriptor_registry.py` import
  is dead (reads `/home/claude/…`, not CI-collected) — left as-is.
- **CI debt blocking-flips (LB-23):** after the **K-2 SHA-split** (115 `canonical_sha` fields out of
  `canonical_sources.yaml` → `references/canonical_freshness.yaml`), flip `freshness_gate`'s
  stale-canonical step back to blocking; flip `validate_ed_citations` (tool `sys.exit(1)`s but the CI job
  pins `continue-on-error: true` → non-blocking) once its count is triaged toward 0 — **now 315 violations
  / 190 open-ref info live** (was 748/788; #20's validator-precision pass dropped it). Solo / K-2 / LB-6.
- **`ci_political_v30` read-routing (LB-24):** raw file ~26k but tracked read returns 0 (index-routes).
- **Ledger-status reconciliation (LA-23, Lane A — mostly done):** flipped ED-841/842/912 `open`→`resolved`
  and filed the never-written ED-938/ED-939 (backfilled from #13; artifacts verified). Dropped the
  report-only `validate_ed_citations` count 748→731. **Residual:** ED-914 left `open` — its mechanical
  parts remain (PP-719 record-or-strike; dead `fieldwork_design_v1` parent-path refs in `params/bg/core.md`,
  `designs/scene/fieldwork_v30.md`, `designs/scene/fieldwork_godot.md`).
- **Design-tier docket awaiting Jordan:** J-31 extended (social-contest deliberative-game findings,
  row #39 → LA-19) and the new **J-36** (Key-bus closure for the 6 off-bus writers, row #40 — gated on
  the distillation report's deferred adversarial pass).
