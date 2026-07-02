# Handoff

Plain, hand-maintained continuity for Valoria. Update this when you pause mid-task; a
git commit *is* the session close. The SessionStart banner (`tools/session_status.py`)
surfaces the "Next actions" section below, alongside `git status` / last commit.

This replaces the old session-log + `canon/session_checkpoint.md` + checkpoint machinery
(which depended on the retired GitHub-API harness and token budgets).

## Pending

- **Social-contest staged rebuild (`claude/happy-shaw-da0f1d`, IN PROGRESS).** Agonist/antagonist gated rebuild
  of the contest engine: promote the stranded 62-test groundup engine (`designs/audit/2026-06-03-contest-groundup/`,
  actually **9 modules / 151 tests green**) onto the v30 surface + fold in CR1–CR7, build all four deliberative
  games (Agôn/Negotiation/Inquiry/Consensus), close J-36 seams, drive to settled canon (T-25 + sim-validation).
  Plan: `C:\Users\Jordan\.claude\plans\this-is-a-broader-nested-mountain.md`. Runs stage-by-stage via the Workflow
  tool (Opus agonist/antagonist/judge + Haiku scribe), Jordan ratifies each gate; cadence = auto-advance, interrupt
  only for design-authority forks.
  - **Stage 0 (Foundation) DONE + Gate 0 RATIFIED (2026-06-30).** Reconciliation contract + decisions:
    `designs/audit/2026-06-30-contest-stage0-reconciliation/DECISIONS.md` (+ raw map + gate packet). Three ratified
    forks: **D0-1** appeal ethos/pathos/logos = build both multiplicative+additive behind a flag, decide by seeded
    A/B (player-win-rate vs venue-identity-spread); **D0-2** σ-leverage → new numpy-free `sim/autoload/sigma_leverage.py`
    sibling (retires the test-dir/numpy/sys.path-hack + the two-σ-kernels debt); **D0-3** TN6/7/8 divergence + Jordan's
    fractional-Ob idea → contest stays δσ TN7 (unaffected), open a substrate probe (reopens CR6 uniformity), non-blocking.
    Good news: `faction.py` already has BG-Vote/Succession/committee-band → Consensus mostly promote-existing.
    IDs reserved: `contest_rebuild` = ED 1055-1079 / PP 800-809.
  - **Stage 1a DONE + committed (d64e2ffe).** `sim/autoload/sigma_leverage.py` — numpy-free σ sibling, byte-identical
    to the oracle, 623 tests green; two-σ-kernels debt retired.
  - **Stage 1b DONE + committed.** 9-module kernel promoted to `sim/personal/contest/`, rewired onto the σ sibling
    (no third kernel); `degree` = clean carry-across (pool-aware integer degree added to sigma_leverage, distinct from
    `dice_engine.Degree` combat enum); old stub → `contest_legacy_stub.py`; 815 sim tests + both importers green.
  - **D0-3 RESOLVED → HYBRID** (present-as-Ob display over the δσ substrate; CR6 upheld, not reopened). Memo:
    `designs/audit/2026-06-30-contest-fractional-ob-probe/MEMO.md`; decision → ED-1055. Probe also surfaced a LIVE
    combat bug (`dice_engine.roll_pool` ignores `tn`; TN5/6/8 weapons rolled at TN7 rate) → spun out as a
    combat-lane task (`task_210994b7`, out of contest scope).
  - **Stage 1c DONE + merged into main (PR #44, all CI green).** v30 re-skin (8 proceedings, Persuasion Track
    banding, 4 adjudicator types) + `build_contest`/`resolve_contest` wrapper + MECHANICS registry, mirroring
    `tests/sim/mass_battle/engine.py`. 888 tests green.
  - **Stage 1d / Gate A DONE — 3 forks ratified by Jordan (2026-07-01).** Propagated CR1 (wrapper, confirmed
    already-realized)/CR2 (σ-substrate, confirmed already-realized)/CR3 (three trackers: Concentration+Face+
    Persuasion, Composure retired — contest-scope only) into prose (`social_contest_v30.md` §4/§8 + co-files,
    `params/contest.md`) + code (`sim/personal/contest/` Face primitive) + ledger (ED-1055, ED-1056). Packet:
    `designs/audit/2026-07-01-contest-gate-a-packet/GATE_A_packet.md`. **Ratified:** (1) Face scale-binding =
    combo formula, not a straight rescale — `Face_max = Charisma×3` (ceiling, player-build-controlled) +
    `Face_current = round(Standing/10 × Face_max)` (position within ceiling, earned through play, Standing's
    kernel math/Readiness/leak feed untouched); (2) Composure retirement scoped to the contest tracker only
    (knots/combat/conviction untouched, confirmed); (3) provisional EDs use non-basis citation phrasing until
    ratified (standing policy). A small Sonnet-tier finalize pass is applying the resolved formula + 4 agreed
    nits (dead imports, ED-1056 recitation, prose wording, TRACKERS sourcing); that pass also caught the ratified
    Face formula shipped with zero test coverage and added 10 targeted kernel checks (boundary cases, midpoint
    round-half-to-even, non-mutation, live-tracking). **Committed (884cf89a).** 1041 sim+valoria + 244 kernel
    checks green. Push to `claude/happy-shaw-da0f1d` updates the open tracking PR ([ttrpg#44]) — Jordan merges,
    not this session.
  - **NEW standing requirement (decision 5, 2026-07-01): the player-interaction model is a concrete deliverable,
    not a late audit.** First-draft walkthrough seeded ahead of Stage 6 so every later stage designs toward it:
    `designs/audit/2026-07-01-contest-player-interaction/player_interaction_walkthrough_v1.md` — setup screen,
    the exchange loop (Appraise / style-choice cards / roll-and-resolve / Face+Concentration bars), the
    resolution screen, and how Negotiation/Inquiry/Consensus should each look different from Agôn's track meter
    so Stage 4 doesn't converge them onto one UI. Stage 2 now owns authoring the Style/Venue flavor text; Stage 3
    now owns the Appraise-reveal boundary for `armature_position`; Stage 4 now owns each game's interaction
    shape; Stage 6 finalizes+ratifies the model this seeds. Plan file amended accordingly.
  - **Gate A committed (`884cf89a` mechanics + `98ecdf41` player-model), PR #44 all-green.**
  - **Stage 2 / Gate B (dictionaries) DONE + committed.** Built Venue×8 / Adjudicator×4 / Style×4 /
    InteractionType×4 typed dicts (`sim/personal/contest/dictionaries.py`, new module) + Style/Venue
    flavor text; closed ED-137 (Panel adjudicator). Packet:
    `designs/audit/2026-07-01-contest-gate-b-packet/` (pre-ratification snapshot + the authoritative
    `GATE_B_closeout_audit.md`). **Ratified and independently re-verified in actual code (not just ledger
    text):** Panel votes weighted-by-standing (ED-1057; reuses the existing `Adjudicator.discipline` field,
    NOT the contestant `Standing` name — no new state invented); Panel reachability = rebind Guild
    Arbitration's adjudicator → Panel (ED-1059; NO appeals — "let the decision ride"; roster stays 8);
    Terminal Doubt = terminal-value-everywhere, banded (PersuasionTrack) + tally (TallyAtClose) branches
    both specified (ED-1060); Guilds "GM picks" boost = context-derived from the venue's dominant
    ethos/pathos/logos via the existing `Appeal` machinery (ED-1061; literal "GM picks" text removed from
    both prose heads). ED-1055/1056/1058 flipped to `status: ratified` (a bookkeeping fix — they were left
    `provisional` only because two earlier finalize-workflow attempts were killed by infrastructure
    issues — API 401/529 errors and a background-task stop, unrelated to the work itself — before
    flipping their own metadata; the ratifications themselves happened earlier via Jordan's answers).
    1041 sim+valoria + 319 kernel tests green; freshness gate clean (5/5 fresh); no scope drift (grep
    confirmed knots/combat/conviction untouched, Composure retirement still contest-scoped).
  - **SOURCE-RESEARCH GROUNDING (found 2026-07-01 via files13.zip → already in repo, NOT orphaned).** The
    deliberation-critique source research
    `designs/audit/2026-06-28-social-contest-deliberation-critique/source-research/` (a 3-part
    Renaissance-deliberation / machination-games-lens / model-testing trilogy) is READ-AND-CITED-BUT-NOT-APPLIED:
    it shaped the plan's four-games / alea / consensus / commitment-store / armature *shape* via `critique.md`,
    but its rich detail (Dowlen small-pool weighted lottery; `liberum veto` as self-undermining equilibrium;
    Padgett robust action; Putnam two-level bargaining) is not yet in the code. Plan amended: Stage 3 (armature)
    and Stage 4 (four games) agonists must now READ the source-research trilogy directly, not just the critique
    distillation, so this commissioned scholarship actually reaches the implementation.
  - **NEXT: Stage 3** (rhetoric grounding + adjudicator armature — CR4 stasis, CR5 self-gating, the
    Style×Conviction dot-product aimed at the judge — reading the source-research trilogy per above,
    not just the critique distillation).

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

- 2026-07-02 — **Merge-ratifies-by-default convention adopted (ED-1090); ED-1083 doctrine
  ratified; J-38 propagation spec ratified (ED-1089).** Jordan: merging a PR ratifies its
  PROPOSED/provisional contents by default unless the PR body explicitly holds an item back
  for separate review — closes a real recurring gap where PR #55 was reviewed and merged but
  `holonic_container_doctrine_v1.md` (ED-1083) sat PROPOSED in `main` afterward because the
  prior convention required a distinct explicit ratification step nothing forced to happen.
  Applied same-day: ED-1083 flipped provisional → ratified; doctrine `## Status:` line
  PROPOSED → **CANONICAL**; `CURRENT.md` gained an Architecture/Holonic-doctrine row;
  `decision_queue.md` item 20 struck resolved; `CLAUDE.md` §2 documents the standing rule.
  **Applied a second time to J-38 itself, same PR (#58):** rather than land the propagation
  spec as PROPOSED and rely on "ratifies on merge" text (which would repeat the exact ED-1083
  failure mode this convention exists to close), the flip to CANONICAL was pre-staged in the
  PR — `designs/architecture/propagation_spec_v1.md` `## Status:` line PROPOSED → **CANONICAL**,
  ED-1089 ledger entry `status` → `ratified`, `decision_queue.md` item 18 struck resolved. A
  whole-session Fable review (triggered after the ED-1088 ID-collision reconciliation) caught
  this risk plus stale cross-references before merge. Scope: governs future PRs; does not
  retroactively reopen closed decisions or ratify anything a PR explicitly holds back and flags
  loudly as such.

- 2026-07-01 — **Month-overview + architecture-consolidation session executed** (this branch;
  12+ commits, ED-1081..1087; overview + execution/reconciliation logs + the frozen 23-item
  Jordan decision queue at `designs/audit/2026-07-01-month-overview-architecture-consolidation/`).
  Landed: LB-21 round-3 ID re-block · two silently-dead enforcement pieces revived
  (`broken_dependency_checker` ledger check; non-executable tracked pre-commit hook) · CLAUDE.md
  §6 falsified claims corrected (ED-1050/ED-1054 states) · holonic container doctrine v1
  **PROPOSED** (`designs/architecture/holonic_container_doctrine_v1.md`, ED-1083 — Jordan-vetoable)
  from the ingested 2026-07-01 workflow spec · Combat Pool collapsed to `max(5, History+6)` across
  every live stale site (ED-1084) · `values_master.yaml` QUARANTINED · names_index v2 (proper-noun
  fold; mirror 23→83) · session-log machinery → `deprecated/session_machinery/` · combat engine
  runtime **numpy-free** (σ-kernel via `sim.autoload.sigma_leverage`; state kernel engine-owned;
  ED-1085) with new container-hygiene guard · **first typed Godot params artifact**
  (`references/engine_params/combat_engine_v1.json`, blocking round-trip CI; ED-1052 seed) ·
  contract-conformance CI (report-only; ED-1051 backlog surfaced per-PR) · CLAUDE.md §10 fable
  tier + relay patterns; workplan **J-38** (propagation-spec authorship) docketed ·
  `currency_consistency_check` self-updating recency gate (CI + SessionStart banner; ED-1087) ·
  freshness pins refreshed + gate flipped **blocking** (LB-23 residual closed). Three scope
  defaults adopted Jordan-vetoable (values_master quarantine-not-regenerate; Godot seed included;
  freshness flip). Rulings made: **none** — everything gated sits in the decision queue.

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
  ED-1081, after contest_rebuild reserved 1055-1079 + combat at 1080). **Safe code/doc fixes applied:** single-sourced the patch-register size cap
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
- 2026-07-01 — **Workplan sprawl cleanup.** `designs/workplans/` was dead (both files pre-dated v3/v4)
  while the live master workplan kept spawning in a fresh one-off `designs/audit/<date>-*/` folder each
  revision, so `CURRENT.md` had to manually chase it. Relocated v5 into `designs/workplans/` (now the
  one live home — see its `README.md`); archived the two dead files to `archives/workplans/`. Repointed
  `CURRENT.md`, `references/lane_assignments.yaml`, `references/roadmap_state.yaml`, and v5's own §0
  commit-path note. Frozen historical versions (v4 in `designs/audit/2026-06-11-orchestration/`, v3 in
  `2026-06-10-master-workplan-v3/`) were left in place intentionally — they're bundled with sibling
  audit artifacts and CURRENT.md already documents them as frozen records, not lost ones. Separately,
  flagged (not moved) the `sim/` vs `tests/sim/` vs `tests/sim_framework/` naming collision — three
  distinct-purpose directories, not duplicates; disambiguated via README notes in each rather than a
  path rename, since `tests/sim/` is path-matched by `ci_sim_fabrication_check.py`/`atomization_rules.yaml`/
  `lane_assignments.yaml` and a rename would need to update all three.

## Next actions

_(Reserved-ID state healthy as of 2026-07-01: **LB-21 executed** — `id_reservations.yaml` v3
verified live max, allocated ED 1081–1087 to the month-overview consolidation from
block D, and pre-provisioned disjoint Round-3 block E (ED 1100–1149 / PP 830–849). Allocate
per the file's protocol; never max+1.)_

- **START HERE — month-overview + consolidation (2026-07-01), doctrine + propagation spec now
  RATIFIED (2026-07-02).** The month's comprehensive review, the consolidation
  execution/reconciliation logs, and the **single consolidated 23-item Jordan decision queue**
  live at `designs/audit/2026-07-01-month-overview-architecture-consolidation/` (see
  `decision_queue.md` first — every gated item below is indexed there). **Doctrine ratification**
  (ED-1083, `designs/architecture/holonic_container_doctrine_v1.md`) and **J-38 propagation-spec
  authorship** (ED-1089, `designs/architecture/propagation_spec_v1.md` — supplies `engine_clock`'s
  candidate home doc; the `doc:null`/[ASSUMPTION] grade stays unflipped until ED-1051 is
  separately resolved) are both **CANONICAL** as of PR #58 (ED-1090 merge-ratifies-by-default).
  The propagation spec's own §5 carries its ranked open items (OF-7/OF-B1 amendments, D.6/OF-D6
  double-count, `decay()` spec, RNG-MODEL-COLLISION, cap constants, ORD-3/ORD-4) — ratification
  did not resolve these, only fixed the spec's home-doc status. Remaining highest-leverage queued
  decisions: Track-2 residuals (below), field-ON, the values_master regenerate-vs-retire call,
  the duplicate compilation homes, and item 19 (Agent-Teams/subagent-roster adoption).
- **Mass battle — Stages A–D + LC-8 landed on `main` (2026-06-30 → 2026-07-02, PRs #45/#52/#56/#57/#59);
  this file previously had zero record of any of it — closing that continuity gap now.** Coordinate-field
  true-adjacency contact (Stage A), facing/attention/reaction physics (Stage B), the command layer
  (`build_army`/timed `Order`s/escort — Stage C), and role/doctrine wiring + `build_envelopment`/
  `build_refused_flank` Unit-level presets (Stage D, ED-907/908/909) are all merged. **LC-8 executed
  2026-07-02 (ED-1088):** `Horseshoe`/`RefusedFlank` retired as `Subunit.shape` values per Jordan's
  go-ahead ("those are emergent outcomes") — only Line/Arrowhead/GappedLine/Column remain valid
  subunit shapes; envelopment/refused-flank exist only as the Unit-level presets above.
  `bat.py`'s grid-mode golden digests were deliberately re-baselined (approved behavior change).
  The workbench (`tests/sim/mass_battle/workbench/`) was extended to visualize the new multi-subunit
  presets — see `tests/coverage_matrix.md`'s 2026-07-02 entries for what shipped and two real bugs
  found/fixed along the way (a `reset_positions` multi-subunit collapse bug; a frontend preset-dispatch
  bug). **Governing plan:** `designs/audit/2026-06-30-massbattle-bottomup/05_redesign_workplan.md` +
  the session's own staged plan (Stages A–F, not yet promoted into the repo — ask the session for
  `using-opus-4-8-ultracode-floating-tiger.md` if resuming this thread). **Still open, Jordan-gated:**
  the `FIELD_MOVEMENT=1` default-flip (Stage A step 7 — byte-exact grid path stays the oracle either
  way); Stage E (Army Configuration Mode / deployment UI) and Stage F (charge/depth/equipment physics)
  are scoped but not started; a flagged-not-fixed pre-existing gap in the reciprocal charge-recoil
  (fires from the rear on an enveloped+braced unit — `gauge_mb.py` C7's own comment, out of scope for
  LC-8). **An orphaned-proposal audit (2026-07-02) also flagged:** `references/
  mass_battle_redesign_workplan_v1.md` is fully superseded (no banner exists — worth a supersession
  marker); `designs/proposals/multiunit_envelopment_plan.md`'s cross-**Unit** spatial envelopment
  ("Path B") is a materially different, still-unbuilt mechanism from the Unit-level `build_envelopment`
  that landed — don't conflate "Envelopment shipped" with "Path B shipped."
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
