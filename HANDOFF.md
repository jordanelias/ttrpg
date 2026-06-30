# Handoff

Plain, hand-maintained continuity for Valoria. Update this when you pause mid-task; a
git commit *is* the session close. The SessionStart banner (`tools/session_status.py`)
surfaces the "Next actions" section below, alongside `git status` / last commit.

This replaces the old session-log + `canon/session_checkpoint.md` + checkpoint machinery
(which depended on the retired GitHub-API harness and token budgets).

## Pending

- **`design/scene-combat-v1`** (UNMERGED) — the scene-combat engine build. After the WS-0..WS-8 build + the
  L0/L2/L3 re-architecture, now in **Phase 3 (wire derived weapon-physics into live consumers + re-baseline)**.
  - **Committed Phase-3 chain:** `297458d7` (foundation: leverage→lever-arm, FIX-1b, M3, half-sword geometry) →
    `210dd1b4` (armor_defeat→derived percussion + FIX-1 reach-threat) → `360325d0` (Tier-2/3 primitives) →
    `d069be7c` (**reach wired to geometry — the grip insight: a centre-gripped staff reaches less than a butt-gripped
    spear, emergent; staff now close-capable**) → `d5a25cc3` (**primitive-law purge Wave 1, behaviour-identical:**
    retired `is_poleaxe`→`butt_kg` primitive, the `longsword_halfsword` name-filter→derived, dead `HEAD_REACH`) →
    `877c8a06` (**recovery/grip FOUNDATION, build-only**).
  - **Two Ultracode assessments banked (this session):** (1) **weapon-name leak audit** (11 agents) — register in
    `tasks/wclbz78ux.output`; worst leak = `systems.GATE` (per-weapon parry/dodge/wind table keyed by `defender.weapon`),
    deferred because the derived `defense_affinities` does NOT yet reproduce it (parry rank-ρ 0.56, wind 0.33; needs the
    agility-clamp fix + band recalibration in the re-baseline). (2) **recovery+grip grounding** (HEMA+physics, survived
    its own adversarial refute — killed an extrapolated swing-exponent + a FABRICATED citation) — formulation in
    `tasks/w811gujrg.output`. Leads with body-extension/lunge (Silver+Giganti, best-grounded); mode-split secondary
    (exponent flagged [ASSERTED]); physics flagged [ASSERTED — first-principles].
  - **Spear decision (Jordan, 2026-06-30): option A — butt-weighted war spear.** Delivered at the mass-model layer in
    `877c8a06`: sauroter `butt_kg=0.25` + `haft_d=0.035` (35mm shaft) → real 0.40kg head; retracts free when gripped at
    balance (the grip-position model). Grip-position derivations (`grip_choke_max`/`grip_travel_max`/`at_grip`,
    parallel-axis, build-only) validated: gather monotone-down to the CoM, spear→balance, mace flat (a club, not a pole).
  - **Recovery/grip STAGE 2 + 2b + GATE — DONE + committed** (`baaa6d77` → `d3661936` → `1dae44e8`):
    - `baaa6d77` — grip-enum {normal,choke,lunge} → continuous `grip_position`+`lunge_depth`; `recoverability_factor`
      rewritten grounded (at_grip I_g/S_g + point_concentration + 1H/2H couple + lunge-led); `adopt_stance`→`grip_target`,
      `can_choke`→`grip_choke_max`, `lunge_quality` continuous. Mirror ~50, 27/27 tests.
    - `d3661936` — `wield_heft` (g-aware MoI) on the COST path → **fixes longsword-vs-plate** (the half-sword's tiny MoI
      now reads light; vs-plate 23/27% → 66/91%). Damage-impact path keeps heft_resp (the wt de-leak is separate).
    - `1dae44e8` — **retired systems.GATE** (the last per-weapon table); defence affinities DERIVE from geometry. The
      resolution spine now carries NO per-weapon table + NO weapon name.
    - Re-baselined matrix coherent: mace/dagger/poleaxe rise vs plate, cutters collapse, longsword half-sword holds,
      arming baseline ~50. "Balance is not symmetry" realized from primitives.
  - **NEXT (the remaining Phase-3 tail → Gate 1):** the SPEAR flat-dominance (94-96% all tiers — its win is REACH, not
    tempo: needs the reach/close-game + the spear gathering live in the wrapper, Phase-5-adjacent); residual de-leaks
    (`hand`→handling, `wt`/`spd`/`pob_frac` legacy fields, half-sword form→grip_position fold); the agility [FIAT] clamp
    (flattens light-weapon dodge); strikes-to-fell for the plate cells (longsword 87 / staff 93 heavy are baseline-collapse
    noise); calibrate the [FIAT] recovery/heft gains; then **Gate-1 adversarial audit (7 lenses)** → ED entries → merge.
  - **SPEAR-FIX FINDING (2026-06-30, measured — corrects the hypothesis above):** the dominance is ~88% the **APPROACH**,
    NOT the closed exchange. Tried a close-game (reach→clinch rotation: inside the point, `reach_sigma` returns a
    `close_handiness`/clinch edge instead of the static reach gap). Measured: at K=0 (closed-reach fully NEGATED) the
    spear STILL beats the dagger **91.8%** (vs 94.8% live) — so the closed-reach edge is only ~3pp of the win; and
    negating it **crashed the rapier** (54→27%, it legitimately banks closed-reach). So the close-game is the WRONG
    lever — the fix is **approach-side** (`stophit_p` / `reach_threat` / `close_rate` in `wrapper.engagement`, where the
    closing weapon eats stop-hits + the spear re-opens). The spear SHOULD win the approach (typology: "the short weapon's
    whole problem is surviving the approach") — just less than 95%; a survivable-close + modest grapple-reward is the
    shape, but it's a careful multi-lever calibration, not a single term. **Experiment reverted** (engine at known-good,
    spread ~52, rapier ~54); `clinch` confirmed the right close-suitability primitive (rapier≈spear, both poor grapplers).

- **Ecosystem-review Top-5 (filed 2026-06-30 as ED-1050..1054, all open).** Tracked, not yet actioned:
  ED-1050 combat parity oracle (config.py ADEF_THRESHOLD non-monotonic vs port's [AUDIT-FIX]; needs a
  harness re-sweep — **needs_jordan**); ED-1051 module-contract gaps (10/27 `doc:null`, 11/27 `[ASSUMPTION]`
  resolvers, Gate-0 spine unbuilt — **needs_jordan**); ED-1052 typed engine-params layer for Godot ingestion;
  ED-1054 navigation surface (partially done this pass). Full report:
  `designs/audit/2026-06-30-ecosystem-adversarial-review.md`.
  **ED-1053 RESOLVED 2026-06-30** (see Decisions). Residual: 12 stale `canonical_sha__` pins surfaced
  by the now-local freshness gate — refresh via `python3 tools/freshness_gate.py --update`, then flip
  the freshness CI step off `continue-on-error`.

## Decisions

- 2026-06-30 — **ED-1052 started: typed engine-params pipeline + Combat Pool collapse.** Established the
  Godot ingestion layer: `references/engine_params/core_resolution.json` (d10 engine + derived scores as
  numeric operands / structured formulas / explicit clamps), held honest by `tools/engine_params_check.py`
  — a CI round-trip gate ("Engine Params Round-Trip") that asserts every entry's `source.quote` still
  appears in its prose doc. Collapsed the Combat Pool triple-definition to one authoritative entry
  (`(Agility × 2) + weapon History (points + 3)`, min 5, PP-615). Bannered `values_master.yaml` as
  stale/not-the-Godot-source; updated CLAUDE.md §5 + `references/engine_params/README.md`. 10 new unit
  tests. **ED-1052 stays open** — only the core slice is typed; contest/mass_combat/threadwork/board_game/
  factions remain prose-only (drop a new `*.json` per the README to extend).
- 2026-06-30 — **ED-1053 resolved: working-tree integrity port + sim oracle.** Ported the three
  "integrity" gates off the GitHub API to the working tree (no PAT/network): `broken_dependency_checker`
  and `patch_propagation_checker` now `os.walk`/read locally (both green against the checkout);
  `freshness_gate` computes git blob SHAs locally (verified identical to `git hash-object`) and checks
  119/131 `canonical_sha__` pins (12 stale → report-only). Dropped `GITHUB_PAT` from the CI integrity job.
  Hardened `ci_sim_fabrication_check`: full float-literal capture + `(variable,value)` matching close the
  value-collision / float-split holes (corpus blast kept to +~200 latent, changeset-scoped; `tools/`
  excluded from sim-classification). Added the first `sim/` test — `sim/tests/test_mc_v18_regression.py`
  (deterministic seeded `run_batch(n=2,seed=0)`: determinism + golden + bounded smoke) — and a new
  'Sim Reference Regression' CI job wired into All-Gates-Green. Updated CLAUDE.md §8.
- 2026-06-30 — **Adversarial ecosystem review + safe fixes.** Ran a 72-agent verification workflow
  (6 audit dimensions × 2 skeptical lenses); 24 findings survived, headline items hand-spot-checked.
  Rewrote `CLAUDE.md` into a Claude-Code-optimized operating manual (numbered sections, currency
  priority, data→Godot pipeline, port state, known-defect callouts). Filed the report under
  `designs/audit/` and the Top-5 as ED-1050..1054. **Re-blocked IDs** (`references/id_reservations.yaml`
  v2: round-1 A/B/C exhausted+overrun to ED-1042; round-2 block D = ED 1050-1099 / PP 800-829, next_free
  ED-1055). **Safe code/doc fixes applied:** single-sourced the patch-register size cap
  (`ci_register_size_check.py` 20k→policy 15k; register is ~5k); RETIRED banners on
  `references/subsystems/{handoff,checkpoint,session_log}_subsystem.md`; flipped
  `canon/session_checkpoint.md` `status: active`→`retired`; STALE banners on the four `designs/godot/*.md`
  specs; rewrote `README.md` to defer to CLAUDE/CURRENT/HANDOFF. **Not done (needs Jordan / re-sweep):**
  the parity-oracle balance values (ED-1050) and the Gate-0/contracts authoring (ED-1051).

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
