# Handoff — PC (Personal Combat)

Lane-scoped continuity for the `PC` (personal/scene combat) lane, per the `ED-<LANE>-NNNN`
namespace (`ED-IN-0001`) and `CLAUDE.md` §3's session-lane-scoping convention. Root
`HANDOFF.md` is the index; see it for cross-lane/global items.

## Pending

- **R3 consolidation plan-of-record — `designs/audit/2026-07-04-weapon-morphology-granularity/consolidation_v1.md`
  (RATIFIED 2026-07-04 via PR #76 per ED-1094; JD-1…JD-8 remain OPEN, loudly held back).** Implementation
  progress:
  - **U0 (units honesty, ED-PC-0001) — DONE 2026-07-05** (branch `claude/begin-u0-arppwt`). head_len/grip_len →
    honest metres (×0.30, all 53 records); `WP.UNIT_M` deleted; per-length gains /0.30 (`PERC_2H_ARC`, `LEVER_K`,
    `REACH_GEOM_SCALE`); stored-length constants ×0.30 (`PERC_GRIP_1H`, `GRIP_SHORT/LONG`, `LEVER_REF`,
    `REC_GRIP_REF`, `GRAB_SHORT_REACH_LU`→**`GRAB_SHORT_REACH_M`**=0.375, name-honesty rename); wind saturation
    3.0 lu → 0.90 m; `_geom_slide_max_lu`→`_geom_slide_max` (the `at_circumstance` bundle's `geom_slide` member
    now reports METRES). Built **`tests/valoria/r3_identity_golden.json` PRE-edit** (the §4 process wrapper's
    OLD-vs-NEW sweep fixture, unit-invariant metres — REUSE it for U3/U4/U5/U6/U7/U8's byte-identical claims;
    regenerate only at deliberate re-baselines U1/U2/U9 with recorded reasons). Acceptance met:
    `test_units_refactor_byte_identical` green at 1e-9 (worst diff 1.8e-15); suite 8 failed / 168 passed /
    1 xfailed — accepted-red set unchanged (5 parity + 3 named), zero new red; params JSON re-exported.
    **Two documented deviations from the U0 row, both forced by its own byte-identity contract:** `reach_adj`
    NOT rescaled (it is a reach-POINTS residual added outside `REACH_GEOM_SCALE`, not a stored length — scaling
    it breaks identity and `test_reach_base_byte_identical_at_grip_zero`); `PERC_2H_ARC` rescaled though the
    row omits it (identity forces it once grip_len is metres). See the ED-PC-0001 ledger entry.
  - **NEXT: U1 (PoB recalibration, ED-PC-0002) — GATED on JD-1** (PoB target bands sign-off, consolidation_v1
    §6; default = the plan's arms-scholarship bands if Jordan waves it through). U2 ⊣ U1. T-P2 may start any
    time (post-U0), scope per JD-6; the F5 renderer recovery (JD-8) is still outstanding.

  Original adjudication summary: Fable-adjudicated merge of two parallel PC-lane efforts: this session's R3 plan
  (units-honesty, PoB recalibration, graded mode-affordance retiring the `head`-category gating of
  cut/thrust/percussion + wiring the dead `thrust_factor`, edge-count, half-sword-from-primitives,
  counterbalance, retreat-default, weapon-class facing) **×** the weapon-morphology granularity audit
  (`audit_v1.md`, merged to `main` as PR #74 — P1 edges / P2 transverse profile / P3 grippable half-sword /
  P4 guard axis + the silhouette renderer). Output = one non-colliding sequence **U0→U9 + T-P2 + T5**, ED-PC
  ids allocated at implementation (`next_free=1`). Key rulings: adopt the audit's `edges={sides,false_edge_frac}`
  encoding (this session's 53-weapon table is the migration data); adopt attested-`grippable` half-sword +
  this session's derived-form generator; one channel per edge-effect (edge-lines→legibility, spine→bind_sigma,
  grab-hazard→contact, drop the double-counts); forced high-risk ordering **PoB → modes+percussion → capstone
  → P2-c cross_section swap**; **U2+U9 ARE the Phase-C percussion enactment — no separate future Phase C
  remains.** Base = post-#72 `main` (merge PR #72 first; the other branch `claude/weapon-morphology-viz-7wmfvq`
  is content-identical to #74 and can be deleted). Open Jordan forks JD-1…JD-8 in §6. Action items: recover the
  never-committed `render_weapons.py` (F5); add a "superseded-in-part by consolidation_v1 §4" header note to
  `audit_v1.md` (on `main`) when the branches unite.

- **Scene-combat engine v1 — MERGED to `main`** (`d4bf2af3`, PR #40, 2026-07-01T04:46Z; Track-2 cleanup
  `8fbc4b66`, PR #47, 2026-07-01T06:48Z). `design/scene-combat-v1` is now fully redundant — its history is
  the same work under different SHAs, confirmed byte-for-byte against `main`'s squash. `pytest tests/valoria -q`
  → 92 passed on `main`. Superseded text below kept as build provenance; see "Still open" for what's left.
  - **Committed Phase-3 chain:** `297458d7` (foundation: leverage→lever-arm, FIX-1b, M3, half-sword geometry) →
    `210dd1b4` (armor_defeat→derived percussion + FIX-1 reach-threat) → `360325d0` (Tier-2/3 primitives) →
    `d069be7c` (**reach wired to geometry — the grip insight: a centre-gripped staff reaches less than a butt-gripped
    spear, emergent; staff now close-capable**) → `d5a25cc3` (**primitive-law purge Wave 1, behaviour-identical:**
    retired `is_poleaxe`→`butt_kg` primitive, the `longsword_halfsword` name-filter→derived, dead `HEAD_REACH`) →
    `877c8a06` (**recovery/grip FOUNDATION, build-only**).
  - **Two Ultracode assessments banked:** (1) **weapon-name leak audit** (11 agents) — register in
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
    Report: `designs/audit/2026-06-30-scene-combat-gate1-audit/gate1_audit_report.md`.
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
    - **→ MERGED — PR #40** (`design/scene-combat-v1`→`main`, 78 commits, squash `d4bf2af3`, 2026-07-01T04:46Z;
      https://github.com/jordanelias/ttrpg/pull/40). Three catch-up merges landed pre-merge (main's #32/#35/#38/
      #39/#41/#42 — confirmed `#32` shared lineage with this branch, so the branch was the authoritative superset;
      one real ID collision resolved, combat re-baseline renumbered ED-1055→ED-1080 after `contest_rebuild`
      formally reserved 1055-1079). All 16 CI checks green at merge. The fuller `.gd` module re-export
      (RESIST/GAP_EXPOSURE/gap-game logic) remains deferred behind the non-compilable skeleton, Key-log parity
      known-red — low priority per CLAUDE.md §6 (skeleton covers 1/27 modules, can't compile regardless).
    - **Phase-A cleanups DONE + MERGED (`8fbc4b66`, PR #47, 2026-07-01T06:48Z):** `_HEAD2DMG` dedup (systems.py,
      proven byte-identical — exhaustive case analysis, not spot-check); dead `pob_frac`/`percussion` WEAPONS
      fields removed (weapons.py + weapon_physics.py's STAGE-1 self-test retired — the stale spear comment claiming
      `recoverability_factor` still reads `pob_frac` was itself wrong, corrected); `capabilities.py`→`afforded_heads`
      resync (a real bug: the state-graph doc generator reported the poleaxe unable to gap-thrust, contradicting the
      engine's own tested gap-game behavior — fixed the `gap_thrust` predicate + its test's independent cross-check;
      exactly one cell changed, hand-verified against all three blunt weapons' point_concentration, not just the
      poleaxe). **`WP.reach()`/`authority()` deletion was attempted and CORRECTLY CAUGHT by adversarial review** —
      "zero callers" is not the same as "safe to unilaterally delete" when the Gate-1 audit already reserved this
      exact fork (item 6 below) for Jordan; reverted the deletion, instead labeled both functions
      `[BUILD-ONLY/DIAGNOSTIC]` in their docstrings (no functional change) per the review's offered safe option —
      the single-source-target decision stays open. All 92 tests green on `main` post-merge.
    - **Still open on `main`, explicitly Jordan-gated:** the `wt`/`spd` cost-path single-source de-leak
      (`core.py:55` `heft_resp`, `systems.py:46` `weapon_tempo` — would shift damage/tempo output across the whole
      roster; needs a measured before/after presented for sign-off, not folded into an autonomous batch); the
      `WP.reach()`/`authority()` (`weapon_physics.py:193,205`) vs `systems.reach_base`/`wield_heft` canonical-home
      decision (both sides already docstring-labeled `[BUILD-ONLY/DIAGNOSTIC]`, safely deferred rather than silently
      resolved); the greedy-comparator-vs-damage docstring; the displace/reach `sel_head` consistency (D-1/D-2).
      Forward-roadmap reference: `designs/audit/2026-06-30-combat-grounding/forward_roadmap.md` Track 2. **Track 4**
      build-forward (abilities-as-access, §C, contact axis, WS-7) remains design-gated — full detail recovered in
      `designs/scene/combat_engine_v1/phase4_5_plan_v1.md` (the Phase 4a game-theoretic layer, Phase 4b access
      catalogue, Phase 4c §C fix, Phase 5 contact axis — none of this was previously committed to the repo).
    - **Track-2 residuals now carry RECONCILED RECOMMENDATIONS (2026-07-01), awaiting Jordan's ratification —
      not yet applied to any code.** Full record (measurement packets + an agonist/antagonist debate, synthesis,
      adversarial skeptic pass, and reconciliation for each residual — every stage independently re-verified
      the prior stage's citations against actual source, not just trusted them):
      `designs/audit/2026-07-01-scene-combat-track2-decision-prep/track2_residual_recommendations.md` (+
      `wt_spd_deleak_report.md`, `wp_reach_authority_comparison.md`, and the two reproducible `.py` harnesses).
      **wt/spd cost-path de-leak — split by path:** damage-path (`core.heft_resp`→`wield_heft`-reuse) is
      **ready for ratification** for every weapon *except the spear* (doubles its damage +10 to +14 flat,
      compounding the already-known spear-dominance problem — carve it out, re-measure once the separate
      approach-phase fix lands). Tempo-path (`weapon_tempo`'s `spd`→`recoverability_factor`) is **NOT ready** —
      confirmed structural double-counting against `pen`'s existing `wield_heft` weight/hands terms (not a
      style question); needs a decomposed candidate isolating the thrust-vs-swing shape from the weight/hands
      magnitude before it's even measurable. **`WP.reach()`/`authority()` canonical-home — ready for
      ratification, in the "do nothing structural" direction:** retire both docstrings' "pending decision"
      framing to "retired diagnostic, not a live candidate" (no functional change) — `reach()` fails on its own
      evidence (non-affine, non-monotonic ratio to the live path; wiring it unscaled would zero the spear's
      close-combat penalty, its core archetype); `authority()`'s only plausible target is `heft_resp`, i.e. the
      *other* residual — deciding it here would resolve that residual by the back door. Three explicit
      "Jordan design taste" questions (not settled by the record) are listed in the memo's final sections.
    - **Polearm close-quarters grounding (2026-07-01), a NEW gap found while investigating the spear-dominance
      anomaly — Jordan's overhang/choke-handling critique confirmed as real, unmodeled physics.** Full record:
      `designs/audit/2026-07-01-scene-combat-track2-decision-prep/polearm_close_quarters_grounding.md`
      (4 research angles + engine verification + synthesis + independent skeptic re-check of every source +
      reconciliation). Two claims tested: **(A) choking up on an asymmetric pole carries a real handling cost
      beyond a scalar MoI reduction** — form-only grounded (T2/T3 consensus: ARMA "difficult to turn the butt
      end of a spear around if you're surrounded"; Escamilla & Fleisig 2009 *J. Appl. Biomech.* confirms
      choke-up measurably lowers implement velocity via trailing-mass drag, not a free win) — no source gives a
      magnitude. **(B) a thrust degrades to a shaft/butt strike at close range/high choke** — well-grounded,
      directly attested: *Le Jeu de la Hache*'s **"demy-hache"** (independently re-verified this session, not
      just trusted) names the exact shaft zone between the hands used to strike/push when the head can't be
      brought to bear; Fiore's *Zogho Stretto* and Winn's *Broadsword & Singlestick* corroborate. **Confirmed
      against actual code (not just suspected): neither exists anywhere in the engine.** `WP.at_grip` is a
      single forward-only pivot with no trailing-mass/rear-overhang term; `select_mode`/`afforded_heads` never
      read `grip_position` at all, so nothing ever converts a thrust to a shaft-strike. `grip_choke_max=1.0`
      for the spear (identical to the staff) is the specific numeric root of the 94-96% win-rate anomaly — the
      engine currently grants a choked-up spear free, unlimited regrip with no asymmetry tax and no thrust-range
      floor. **Ready to greenlight as a concrete build task:** a new `overhang_penalty(c,cfg)` (trailing-mass
      moment `m_trail*L_behind²` feeding `recoverability_factor`) + an `available_extension` hard gate in
      `select_mode` that substitutes a shaft-strike coupling at high choke/close range, + a matching
      `lunge_quality` consistency check (a skeptic-flagged addition, folded in). **Jordan's call, not settled by
      the record:** the `K_OVERHANG`/`MIN_POINT_CLEARANCE` magnitudes — no source of any tier gives a number;
      both are [FIAT]/[SIM-CALIBRATE], to be set by playtesting against the 94-96% anomaly this targets.

- **ED-1050 (combat parity oracle) — RESOLVED 2026-06-30, residual open.** ADEF_THRESHOLD monotonicity
  fixed (config.py + combat_config.gd re-exported, byte-identical, re-verified 2026-07-02 in the D1-D5
  docket adjudication, ED-IN-0002). Residual: re-export RESIST/GAP_EXPOSURE/gap-game logic to
  `weapon_resource.gd`/`strike_module.gd`; Key-log parity stays known-red until done (tracked as
  `decision_queue.md` item 5).

## Decisions

- 2026-07-01 — **Scene-combat engine v1 merged to `main`; lost Phase 4/5 provenance recovered.** PR #40
  (`d4bf2af3`, 78 commits, 2026-07-01T04:46:19Z) merged the ratify-ready branch; PR #47 (`8fbc4b66`,
  2026-07-01T06:48:32Z) merged the Phase-A Track-2 cleanup (HEAD_MODE dedup, dead `pob_frac`/`percussion`
  field retirement, `capabilities.py` resync). `pytest tests/valoria -q` → 92 passed on `main`.
  `design/scene-combat-v1` is now fully redundant (its 4-commits-ahead-of-`origin/main` delta is the
  identical work, already squash-merged under different SHAs) — candidate for deletion pending Jordan's
  confirmation (see Next actions). Separately, tracing "the workplan" back to its source (per Jordan's
  request to review prior scene-combat sessions) found the actual master workplan existed only as two
  **local, never-committed** Claude Code plan files: the v4 master plan (WS-0..WS-8, the three co-equal
  access gates, §C) and a Phase 3/4/5 completion plan (Workstream-0 grounding spine, 7 review lenses,
  3 named principles, Phase 4a game-theoretic layer, Phase 4b abilities-as-access, Phase 4c §C residual,
  Phase 5 contact axis) — and that `forward_roadmap.md`'s "Track 4" summary had silently dropped the
  entire Phase 4a game-theoretic layer plus the grounding-ledger deliverables in compressing it. Recovered
  the full Phase 3/4/5 plan verbatim (with status annotations) into
  `designs/scene/combat_engine_v1/phase4_5_plan_v1.md`; repointed `forward_roadmap.md` Track 4 and this
  file's Next actions at it. Two Track-2 residuals remain open and Jordan-gated: `wt`/`spd` damage-path
  de-leak, `WP.reach()`/`authority()` vs `systems.reach_base`/`wield_heft` single-source decision.
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

## Next actions

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
- **ED-1051 residual affecting this lane:** `engine_clock`'s doc:null grade now has a candidate home doc
  (`propagation_spec_v1.md`, ED-1093) but ED-1051 itself (module-contract closure priorities across all 27
  modules) is an **IN**-lane item — see `handoffs/HANDOFF_IN.md`.
