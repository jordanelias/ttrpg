# Handoff

Plain, hand-maintained continuity for Valoria. Update this when you pause mid-task; a
git commit *is* the session close. The SessionStart banner (`tools/session_status.py`)
surfaces the "Next actions" section below, alongside `git status` / last commit.

This replaces the old session-log + `canon/session_checkpoint.md` + checkpoint machinery
(which depended on the retired GitHub-API harness and token budgets).

## History

Full narrative for the work below (2026-06-24 through 2026-07-02) moved to
`registers/handoffs/HANDOFF_archive.md` (2026-07-08, token-efficiency pass) — this file had drifted from
"index" to a full append-only session log. Nothing was deleted, only relocated; the archive is
frozen, do not resume work from it.

<<<<<<< HEAD
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
  - **GATE-1 ARCHITECTURE AUDIT — DONE + partial-resume committed (2026-06-30).** Ran the 7-lens adversarial audit
    (67 agents, each finding skeptic-verified + a completeness critic): **54 confirmed / 5 refuted**. Headline: the
    Phase-2 "wrapper computes NO σ" invariant was only PARTIALLY met (the APPROACH path + several sites still
    assembled σ inline) and "ONE derivation" is violated (percussion authority derived twice with DIFFERENT inputs —
    `core.p_auth` reads hand-set `pob_frac`, `WP.percussion_authority` the derived `PoB_frac`; diverge up to Δ0.359).
    Report: `audit/lane-a/2026-06-30-scene-combat-gate1_audit_report.md`.
    - **LANDED (byte-identical — seeded 576-cell SHA `71c3bce9…` reproduced; pytest 65→73):** `250eefd7` wrapper
      de-leak completion (lifted the real inline σ-assemblies — `stophit_sigma`/`init_emphasis_sigma`/
      `counter_success_prob`/`close_rate`/`consistency`/`mental_fatigue`/`poise_regen`/`bind_dominance_p`/
      `disrupt_resist_p` — into pure `systems.*`; **left** the gate-compositions the audit REFUTED as σ-leaks) +
      the missing mirror-fairness/determinism guard (`tests/valoria/test_combat_balance_guard.py`); `81850e85` safe
      cleanup (deleted the dead STAGE-4 block + `HANDS2` + the vestigial `Combatant.reach/.weight`; corrected the
      false "BUILD-ONLY/nothing reads STAGE 3/4" header + the `MOI_AGILITY_K` "superseded" comment).
    - **GATED on Jordan (re-baseline — change balance, NOT done unilaterally; see report §Decisions):** (1) single-source
      the percussion authority (`core.p_auth`→derived; ties **ED-1050** + D-A lethality); (2) `wt`/`spd` damage-path
      de-leak (route to derived MoI/agility); (3) the agility `min(1.0,…)` FIAT clamp + `_band` re-clipping (flatten
      light-weapon dodge/parry — emergence partly cosmetic); (4) `ADEF_THRESHOLD` non-monotonicity + the
      `combat_config.gd` port-corrects-oracle drift (**ED-1050**); (5) abilities-as-ACCESS (Phase-4; `eff_cw` is a
      near-no-op threaded through ~18 sites as dormant scaffolding); (6) the `WP.reach()`/`authority()` vs
      `systems.reach_base`/`wield_heft` single-source target. **Allocate ED-1080+ (block D) for these on Jordan's call.**
  - **GROUNDED PERCUSSION/ARMOUR/USE-MODE RE-BASELINE — BUILT + committed (2026-06-30).** The percussion single-source
    (ED-1050 cluster) grew, on Jordan's direction, into a full evidence-grounded weapon×armour×technique model — 4
    adversarial workflows (treatise `w4h8gl48w`, biomech `wpwi3b9qf`, armour `wht7pkx1c`, use-mode `w4bekmb5e`),
    consolidated in `designs/audit/2026-06-30-combat-grounding/`. **Jordan's principle (memory
    `combat-grounding-methodology`): DERIVE constants from physics/biomechanics/treatises/materials — never pick or
    floor to a sim-fit; and modes must EMERGE from primitives, not a per-weapon table.**
    - **Committed:** `80a3a077` armour RESIST (4 Williams cells + the primitive-emergent doc correction); `66a7c5ec`
      concussion single-source (`core.p_auth`→`WP.percussion_authority` with the biomech energy_credit A_HANDS=0.25/
      B_ARC=0.04; mace 7.45/poleaxe 5.83/staff 2.51) + PRIMITIVE-EMERGENT use-mode selection (`systems.afforded_heads`
      + `select_mode` — modes derive from geometry primitives, retiring the head-collapse; poleaxe the only weapon
      affording >1 head, emergent; every other weapon byte-identical). 73 tests, mirror ~50, no one-shot, grounded
      ranking holds (poleaxe>mace>staff vs plate).
    - **RESOLVED (Jordan) — the poleaxe's plate default = the SITUATIONAL GAP GAME** (`f7f7596f`). A thrust now SEEKS
      gaps: its plate-defeat = max(through-material, GAP_EXPOSURE[mat]·gap_precision), scaled by the weapon's derived
      gap_precision (emergent, no weapon name). The poleaxe now SPIKES the reach-ladder vs plate (Le Jeu de la Hache);
      the rondel dagger comes alive as the armour-gap weapon (dagger>mace vs plate 12→69%); the mace hammers (no
      point); the staff stays weak; the whippy rapier is mediocre. GAP_EXPOSURE [SIM-CALIBRATE, reach-ladder frame].
    - **Forward roadmap:** `designs/audit/2026-06-30-combat-grounding/forward_roadmap.md` (WS + REARCHITECTURE + Gate-1
      folded; strategy = CONSOLIDATE before building). **Track 1 progress:** 1a **adef-consistency lever DONE**
      (`b79615f4`, ADEF_POINT 1.0→1.2 — the gap-thrust's CONTROL now matches its DAMAGE, so the poleaxe's spike is a net
      win; plate win-rate 88.6→90; rondel strengthened; grounded ranking holds); 1c **heavy-mirror guard DONE**
      (`e4da1f04`, 73→78 tests — symmetry + non-degeneracy, catches an armour-defeat draw-stalemate regression the
      light-only test missed).
    - **Track 1 DONE** (`b79615f4` adef · `64bc95dc` ED-1080, filed as 1055 · `e4da1f04` heavy-mirror guard). **Track 2 substantially
      done:** agility FIAT clamp fixed (`2cbd8b1c` — emergent light-weapon dodge/parry spread restored); **the pre-merge
      re-audit** (ultracode Workflow `wi4q11myc`, 4 lenses, 28 confirmed) CLEARED the branch as architecturally sound
      (no name-table / emergence real / concussion single-sourced / RESIST grounded — all survived adversarial trace)
      with **exactly one merge gate**, now CLOSED: `d9fd1f1a` **ADEF_THRESHOLD monotone re-sweep (ED-1050 RESOLVED)** +
      re-exported `combat_config.gd` from the oracle (retired the port's §6 private [AUDIT-FIX]); `e1fc0686` **architecture-
      invariant guards** (no-name-table ast scan + single-source + emergent-selection + gap-game — 84 tests).
    - **→ THE BRANCH IS RATIFY-READY — PR #40 CLEAN/MERGEABLE** (`design/scene-combat-v1`→`main`, 78 commits;
      https://github.com/jordanelias/ttrpg/pull/40). Three catch-up merges landed (main's #32/#35/#38/#39/#41/#42 —
      confirmed `#32` shared lineage with this branch, so the branch is the authoritative superset; one real ID
      collision resolved, combat re-baseline renumbered **ED-1055→ED-1080** after `contest_rebuild` formally reserved
      1055-1079). All 16 CI checks green, 0 behind main, awaiting Jordan's merge click. Then the fuller `.gd` module
      re-export (RESIST/GAP_EXPOSURE/gap-game logic — deferred behind the non-compilable skeleton, Key-log parity known-red).
    - **Phase-A cleanups DONE (2026-07-01, agonist/antagonist Workflow + 2 solo-verified agent pairs, uncommitted):**
      `_HEAD2DMG` dedup (systems.py, proven byte-identical — exhaustive case analysis, not spot-check); dead
      `pob_frac`/`percussion` WEAPONS fields removed (weapons.py + weapon_physics.py's STAGE-1 self-test retired —
      the stale spear comment claiming `recoverability_factor` still reads `pob_frac` was itself wrong, corrected);
      `capabilities.py`→`afforded_heads` resync (a real bug: the state-graph doc generator reported the poleaxe unable
      to gap-thrust, contradicting the engine's own tested gap-game behavior — fixed the `gap_thrust` predicate +
      its test's independent cross-check; exactly one cell changed, hand-verified against all three blunt weapons'
      point_concentration, not just the poleaxe). **`WP.reach()`/`authority()` deletion was attempted and CORRECTLY
      CAUGHT by adversarial review** — "zero callers" is not the same as "safe to unilaterally delete" when the
      Gate-1 audit already reserved this exact fork (item 6 below) for Jordan; reverted the deletion, instead
      labeled both functions `[BUILD-ONLY/DIAGNOSTIC]` in their docstrings (no functional change) per the review's
      offered safe option — the single-source-target decision stays open. All 92 tests green throughout; not yet
      committed.
    - **Still open, explicitly Jordan-gated (NOT touched this pass):** the `wt`/`spd` cost-path single-source de-leak
      (would shift damage output across the whole roster — needs a measured before/after presented for sign-off, not
      folded into an autonomous batch); the `WP.reach()`/`authority()` vs `systems.reach_base`/`wield_heft` canonical-
      home decision (see above — now safely deferred rather than silently resolved); the greedy-comparator-vs-damage
      docstring; the displace/reach `sel_head` consistency (D-1/D-2). **Track 4** build-forward (abilities-as-access,
      §C, contact axis, WS-7) remains design-gated.
=======
Per-lane continuity now lives in `registers/handoffs/HANDOFF_<LANE>.md`, using the same 9 lane codes as
the `ED-<LANE>-NNNN` editorial namespace (`ED-IN-0001`, `CLAUDE.md` §3). This file is the
**index** plus genuinely cross-cutting items — read the lane file(s) relevant to your session
before starting work, and keep your own updates scoped to your lane's file (or this one, only
for cross-cutting items).
>>>>>>> origin/main

| Lane | Subsystem | File |
|---|---|---|
| `MB` | Mass battle | `registers/handoffs/HANDOFF_MB.md` |
| `PC` | Personal / scene combat | `registers/handoffs/HANDOFF_PC.md` |
| `FI` | Field investigation | `registers/handoffs/HANDOFF_FI.md` |
| `SC` | Social contest | `registers/handoffs/HANDOFF_SC.md` |
| `FA` | Faction actions | `registers/handoffs/HANDOFF_FA.md` |
| `WR` | World | `registers/handoffs/HANDOFF_WR.md` |
| `IN` | Infrastructure / cross-cutting | `registers/handoffs/HANDOFF_IN.md` |
| `GO` | Godot conversion | `registers/handoffs/HANDOFF_GO.md` |
| `SE` | Settlements | `registers/handoffs/HANDOFF_SE.md` |

**Why the split:** the ID-collision incidents that motivated `ED-<LANE>-NNNN` (two same-session
concurrent-allocation collisions on the flat sequence within one PR — see `ED-1094`'s ledger
entry) are the same failure class that makes one shared `HANDOFF.md` a merge-collision magnet
once multiple lane-sessions run concurrently. This is a **partial, deliberate exception** to the
repo's earlier "one continuity surface" consolidation (`deprecated/session_machinery/` retired
per-topic session-log files because they rotted independently) — the difference is this split is
keyed to the SAME lane taxonomy the ID system already enforces, not an ad-hoc per-topic split,
and this root file remains the one stable SessionStart entry point.

**Full detail on the split itself, and every historical decision predating it, is filed at
`registers/handoffs/HANDOFF_IN.md`'s Decisions log** — this root file does not duplicate that history.

## Next actions

_(Reserved-ID state healthy as of 2026-07-01: **LB-21 executed** — `id_reservations.yaml` v3
verified live max, allocated ED 1081–1087 to the month-overview consolidation from
block D, and pre-provisioned disjoint Round-3 block E (ED 1100–1149 / PP 830–849). Allocate
per the file's protocol; never max+1. Since the 2026-07-02 cutover (ED-IN-0001), new EDs
allocate per-lane from `lane_ids` — the flat sequence is frozen.)_

- **Current state (2026-07-16).** The **sole remaining T0 blocker** on M1 is **ED-1051**
  (engine_clock ratification — default: flip `references/module_contracts.yaml` `engine_clock`
  `doc:null` → `systems/_architecture/propagation_spec_v1.md`); it also gates the GO lane's
  Gate-0 entry. Governance **D1–D6 RULED 2026-07-13** (ED-IN-0046/0047): the FA §1.0c/§1.0d/§2.5
  riders, B1 faction-count = 4, and B12's new Settlement→Territory→Province→Duchy→Country
  hierarchy await ratification-flip + authoring (E11 symmetric suspicion-reduction; **L/PS
  wiring** is flagged the single highest-priority open item). The dashboard's proposals register
  was made honest 2026-07-16 (**ED-IN-0072**): of the open work, ~136 items are genuinely
  agent-executable (no ruling needed) and ~97 need your decision — see
  `tools/observability/PROPOSALS.md`. Lane detail in each `registers/handoffs/HANDOFF_<LANE>.md`.
- **Mobile-friendly status dashboard built (2026-07-11, ED-IN-0031)** — `dashboard/`,
  published by `.github/workflows/dashboard.yml` to GitHub Pages. Surfaces workplan progress,
  recent activity, a "needs your decision" inbox, and audit/simulation-balance verdicts
  (`references/audit_registry.jsonl`, now kept current by the 8 audit/simulation skills'
  retrofitted registry-append step). **One manual step needed from Jordan before it goes
  live:** repo Settings → Pages → Source: "GitHub Actions" (the default token can't flip this).
  **Extended 2026-07-11 (ED-IN-0037** — renumbered from a collision with PR #122's concurrent
  audit-ecosystem batch, which independently claimed ED-IN-0032 through 0036; see
  `references/id_reservations.yaml`'s IN-lane comment**)**: Balance & victory data card (personal-combat weapon
  matrix — flagged stale; faction win-share goldens from `sim/tests/`, labeled as CI regression
  guards, not a persisted full-campaign run; honest no-data flags for mass_battle/social_contest/
  threadwork/settlement_territory) + Registers card (editorial-ledger open/needs_jordan counts by
  lane, active patch-register counts). Also corrected a stale dashboard callout that had been
  repeating the now-debunked "~87% degenerate win-share" claim (CLAUDE.md §7) — see
  `sim/tests/test_f7_smoke_oracle.py`'s docstring for the actual correction.
- **ED-IN-0044 RATIFIED 2026-07-12 (simulation/test harness methodology + Gate-0 prototype).**
  `designs/audit/2026-07-12-simulation-test-harness-methodology/` +
  `tools/sim_harness/` (six rounds of adversarial review/stress-testing since filing, 34 real bugs
  found and fixed — see the package's own README). §11's four open questions were put to Jordan
  directly, not assumed: rollout order extended (§8 gained faction actions/settlement-territory/
  threadwork as waves 5–7, per Jordan flagging the gap; field investigation excluded as still
  stub-only); Wave 1 CI burn-in stays full report-only; `mc_v18` never gates a PR; the four §9
  quick wins filed separately as **ED-IN-0045** (open, execution pending — see
  `registers/handoffs/HANDOFF_IN.md`). Full resolution text: `registers/editorial_ledger_in.jsonl`.
- **JORDAN RULING NEEDED — ED-SC-0015 (Parliamentary total-victory Mandate stacking).** Full
  detail in `registers/handoffs/HANDOFF_SC.md`'s Pending section (also cross-referenced from
  `registers/handoffs/HANDOFF_FA.md`). The one item from the 2026-07-08 FA/SE historical-precedent build
  genuinely needing Jordan's own call, not routine merge-ratification — everything else in that
  build ratifies normally on merge per ED-1094.
- **START HERE — Master Workplan v6 is the live steering surface, RATIFIED with the whole
  of PR #78 (2026-07-05, ED-IN-0009/ED-IN-0011 — Jordan: "Ratify commit merge all").** `workplans/valoria_master_workplan_v6.md`: North-Star milestones (M1 one
  playable season · M2 any-seed story bar · M3 Godot slice), per-lane workstreams (status
  stays in `registers/handoffs/HANDOFF_<LANE>.md` — v6 only sequences), and the tiered T0/T1/T2
  Jordan-decision register (§5) that **supersedes the 2026-07-01 `decision_queue.md` as the
  live decision list** (that file is now a dated snapshot; its items 1–3 were refreshed at
  supersession). Steering reconciliation ED-IN-0006 EXECUTED: `roadmap_state.yaml` retired to
  `deprecated/references/`, workplan v5 archived with banner (its J-38 contradiction
  corrected), hierarchy adopted (CURRENT.md → lane handoffs → workplan-derived). Same PR:
  the **narrative engine v2 "Churn Engine"** (`designs/audit/2026-07-05-emergent-narrative-engine/
  narrative_engine_design_v2_churn.md`, five-refuter adversarial pass applied) — **RATIFIED
  in full 2026-07-05 (ED-IN-0011), including F-F/fork-8 at its default** (subtract-only +
  the weight set as versioned data; values revisable anytime). Remaining T0 wall: **ED-1051
  (engine_clock) alone** — JD-1 RULED 2026-07-08 (U1/ED-PC-0010) and fork 10's faction count
  RULED = 4 (2026-07-13, ED-IN-0047, resolves ED-FA-0001); both struck from the wall.
- **Month-overview + consolidation (2026-07-01), doctrine + propagation spec RATIFIED (2026-07-02).**
  Full narrative + the 23-item Jordan decision queue: `designs/audit/2026-07-01-month-overview-architecture-consolidation/`
  (`decision_queue.md` first) and `registers/handoffs/HANDOFF_IN.md`'s Next actions. Doctrine ratification
  (ED-1083) and J-38 propagation-spec authorship (ED-1093) are both **CANONICAL** as of PR #58
  (ED-1094 merge-ratifies-by-default).
- **Per-lane "Next actions" content lives in each lane's own file (2026-07-08 atomization pass)** —
  this root file no longer carries lane-owned detail, only genuinely cross-cutting items. Every
  lane-specific bullet previously here was cross-checked against its lane file first and dropped only
  where already covered (one gap found and backfilled: the R2 capstone finding → `HANDOFF_PC.md`;
  J-36 → `HANDOFF_IN.md`). Start with:
  - **Mass battle** (coordinate-field engine, DG-1..DG-5, the open partition-invariance ruling):
    `registers/handoffs/HANDOFF_MB.md`.
  - **Personal / scene combat** (R2 capstone finding, Track-2 residuals, weapon-morphology
    consolidation, JD-1..JD-9): `registers/handoffs/HANDOFF_PC.md`.
  - **Infrastructure / CI** (LB-22/23/24 residuals, LA-23 ledger reconciliation, J-36):
    `registers/handoffs/HANDOFF_IN.md`.
  - **Social contest** (ED-SC-0015, J-31): `registers/handoffs/HANDOFF_SC.md`.
- **Reserved-ID state:** the flat `ED-NNNN` sequence is FROZEN (2026-07-02 cutover,
  `ED-IN-0001`) — the ruling `ED-1094` established the freeze; the live ceiling is `ED-1096`
  (ED-1095/1096 landed same-day). All NEW EDs use `ED-<LANE>-NNNN` — `references/id_reservations.yaml`'s
  `lane_ids` section is the live allocation source; read `next_free` for your lane, allocate,
  bump, co-commit. Never max+1.
