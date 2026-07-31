# Handoff — PC (Personal Combat)

Lane-scoped continuity for the `PC` (personal/scene combat) lane, per the `ED-<LANE>-NNNN`
namespace (`ED-IN-0001`) and `CLAUDE.md` §3's session-lane-scoping convention. Root
`HANDOFF.md` is the index; see it for cross-lane/global items.

## Pending

- **▶▶ W8d DONE (2026-07-30) — the measuring instrument is now audited, and it does not support the
  inference the plan's other packages were going to make of it.** New:
  `tests/valoria/_draw_stream.py` (single owner of the RNG draw-stream instrument, following the
  `_conservation.py` precedent) + `tests/valoria/test_combat_draw_stream.py` (11 guards, 8 mutants run,
  7 killed, 1 equivalent, 1 deliberate survivor). **No engine change — `wrapper.fight` already takes
  `rng` as a parameter, so this is test-side only and no golden can move.**
  - **THE HEADLINE: shifting the draw count by ONE flips 40.2% of seeded outcomes** (161/400,
    longsword vs rapier). **Seeds are not experimental control across a code change that moves the
    stream**, so every paired-seed claim in the plan needs the stream pinned on both arms.
  - **Same seed ≠ same experiment across contexts.** One seed, longsword vs arming: **57 underlying
    draws at `armour='none'`, 168 at `'heavy'`** (2.95×). `wrapper.py:93` documents the mechanism in
    its own comment; the consequence was never drawn.
  - **A parity latch inside the stdlib.** `random.Random.gauss` caches its second Box–Muller variate, so
    k calls consume `2*ceil(k/2)` underlying draws — 2 on odd, 0 on even. `core.resolve` reaches `gauss`
    on the *same object* the engine draws `random()` from, so one added resolution shifts the bare-
    `random()` sub-stream by 0 or 2 **depending on parity**. No constant offset realigns two streams.
    Pinned as an environment guard: a CPython change here would move every combat golden silently.
  - **Inventory: 34 `rng.*` calls across 33 lines** (`wrapper.py:327` carries two). Pinned STATICALLY
    (AST) because 3 sites are unreached by a 256-fight sweep, so a dynamic pin would miss a new draw on
    a cold branch. The unreached three: `capabilities.py:154` (a `__main__` self-test probe, genuinely
    off-path), `wrapper.py:235` (`randrange` — the exact-tie tiebreak, needs float equality of two
    accumulated readiness values), `wrapper.py:419` (the disrupt-resist draw). **Reported, not deleted**
    — `state_graph.py` already records (ED-PC-0042) that this same sweep produced two false dead-branch
    verdicts.
  - **⚠ TWO NEW DEFECTS found while building, both verified:**
    1. **`PARRY_MOMENT_K` and `WIND_MOMENT_K` had ZERO test coverage anywhere.** ED-PC-0052 shipped
       three gains and guarded one. Now covered by an *exactly-once* guard (perturb
       `contact_moment_edge` by a known delta, require the sigma to move by exactly `K × delta ×
       attenuation`) — which is also a **double-charge detector** and killed MUT-7.
    2. **The three gains' nominal parity is not effective parity.** All three are 0.30, and ED-PC-0052
       presents that as considered parity — but `bind_sigma` returns unattenuated while `mode_sigma`
       returns `(base+sig)*cap`. Measured: bind moves **0.300**, parry and wind **0.120** each
       (tsurugi's parry/wind affinity is exactly 0.40). The effective parry gain is weapon-dependent —
       rapier 0.70 vs tsurugi 0.40, a **1.75× spread in one declared constant**. Whether a mass fact
       should be affinity-attenuated is a design question → **routed to W8c**, not changed here.
  - **⚠ A guard of my own was decoration and was rewritten.** The first form of the moment guard
    asserted `0.0 * edge == 0.0` — a property of floating-point multiplication, not of the engine. Third
    instance of this defect class in this arc; caught by the adversarial pass, not by the suite passing.
  - **Consequence for the plan: W8a's owed texture measurement for ED-PC-0052/0054 must be re-taken with
    the stream pinned.** Their aggregate-inert results were measured on this unaudited instrument. This
    does **not** show them wrong — it shows they are unvalidated, which is the W8d scope.
  - **⚠ NO ED ALLOCATED — the PC lane is ID-BLOCKED.** Reserved block `0041–0055` is exhausted (all 15
    used) and `references/id_reservations.yaml` is FROZEN for the three-session run (`next_free: 56`,
    "no session bumps any next_free until the W5 capstone"). Further PC work that needs a ledger entry
    needs either an ID release or a new reservation — **this is now a blocker, not a formality.**

- **▶ RATIFICATION STATE after PR #273 merged (2026-07-30, `3005096`) — read before resuming.** ED-1094's
  ratify-on-merge default was applied *selectively*, because that PR declared its exceptions loudly:
  - **RATIFIED:** `combat_completion_plan_v4.md` (v4.1) as the PC lane's **plan-of-record** — its method,
    §0 re-classification and §5 ordering. `session_retrospective_and_plan_v3.md` as **findings**; its §5
    sequencing is superseded by v4.1.
  - **STILL PROPOSED, deliberately:** `curvature_and_bind_model_v1.md` — channels 2–5 are unbuilt
    specification, declared PROPOSED-by-design in the PR body. The note is now at the doc head so nobody
    later infers ratification from the merge.
  - **NOTHING in the ledger was flipped.** All eight entries (ED-PC-0048..0055) were re-verified
    post-merge and are already at their true state; the seven `needs_jordan: true` each name a real
    held-back call (0049 spike/hammer parity · 0050 the two-direction split · 0051 the katana anchor ·
    0052 and 0054 whether to keep K=0 · 0053 `CLOSE_ENGAGE_M`'s value · 0055 the confirmed dead physics).
    PR #273's body enumerated five of these under "Merging does **not** ratify these."
  - **⚖1b and ⚖6 are OPEN and are Jordan's** — merging v4.1 ratified *that they are his*, not an answer.
  - **No new ED allocated** for this flip: the PC reserved block 0041–0055 is exhausted and
    `references/id_reservations.yaml` is frozen. Recorded here instead, per ED-1094 (the flip belongs to
    the merge, not to a new item).

- **▶▶ THE LIVE PLAN (2026-07-30): `audit/2026-07-26-combat-balance-customization-state/combat_completion_plan_v4.md`
  — v4.1, RATIFIED plan-of-record.** Research-led (HEMA/treatise-grounded per Jordan's 2026-07-30 authorization),
  iteratively tuned, and revised after a read-only Fable 5 adversarial pass whose findings were
  **verified against the working tree** rather than accepted (§7 records all 11, including one the
  critic got wrong). It supersedes the **sequencing** of `combat_execution_plan.md` §7,
  `combat_remediation_plan.md` §8, and v3 §5 below; their content stands.
  - **Order: W0 → W7a → W1 → W8d → W4/N4 → W2 → W6 → W5 → [W3 when scoped] → W7b → W8a/b/c.**
  - **Two ⚖ items came BACK to Jordan** after the adversarial pass: **⚖1b** the katana anchor for
    `CUT_REF_NATIVE` (ED-PC-0051 ships `needs_jordan: true` and v4 had silently ratified it), and
    **⚖6** off-hand scope (a budget question, not a researchable one). W3 is blocked on ⚖6.
  - **Retracted in v4.1:** v4 proposed deriving `CLOSE_ENGAGE_M` from `L0`. `L0`=4.0 is a
    **1.89 m reach-point fit anchor**, not an arm, and `Combatant` has no anthropometry — that
    derivation would have re-committed the ED-PC-0053 fiat gate one layer up. `config.py:176`'s
    "the fighter's own arm" comment is quantitatively false and is fixed as part of W0.
  - **Two new defects found while verifying:** **W8c** — `weapon_tempo` charges `I_g` **twice in one
    function** (`wield_heft` at `combat_systems.py:101` + the `TEMPO_RECOVER_K·tanh(...)` term at
    line 110). **W8d** — `wrapper.py`'s RNG stream is order-dependent, so a `K=0` ablation is a
    different experiment, not a control; **every paired-seed measurement in the plan rests on an
    unaudited instrument.** W8d is scheduled before the first ablation.
  - **Plate participation re-measured: 36/53** zero-decided at heavy (`8a054d0`), via
    `workbench/armour_participation.py`. The corpus's 38 is stale; v4's 35 was wrong; it was 34 at
    session start and **no weapon gained the ability to decide** during the session.

- **▶ Background (2026-07-30): `audit/2026-07-26-combat-balance-customization-state/session_retrospective_and_plan_v3.md`**
  — lessons, an adversarial pass on the session's own work, 9 newly-flagged items (N1–N9), and a
  **REORDERED work list that supersedes `combat_execution_plan.md` §7 and `combat_remediation_plan.md`
  §8's sequencing.** The headline that reorders everything: **three correct, absent mechanisms
  (ED-PC-0051/0052/0054) each moved the field by NOTHING; one fiat-gate removal (ED-PC-0053) moved it
  immediately.** Both original plans would send the next session to E4 (more benefit-side grading),
  which is the shape proven not to work. **Next work is (1) Jordan rules `CLOSE_ENGAGE_M`, (2) the owed
  texture measurement, (3) E6/M10 off-hand — the rapier's real counterweight, with the shield hook
  already plumbed and callerless.**
  - **⚠ SELF-FLAGGED, the session's worst finding: `CLOSE_ENGAGE_M=0.45` is the BEST of four swept
    values on both rapier win-rate and field spread** (0.30→83.5%/41.1pp · **0.45→75.5%/35.1pp** ·
    0.60→79.8%/41.7pp · 0.75→80.8%/38.5pp), and the response is NON-MONOTONE. It was chosen on physical
    grounds before measuring and never swept — but the artifact cannot prove that, and the value is
    therefore **not safely defensible as "just physical."** Jordan's call.
  - **⚠ Corrected: every field number reported mid-session was one batch stale.** TRUE current state
    (post-0054/0055): **rapier 71.8%, spread 30.7pp, sd 8.2pp** — not the 73.5/32.5/8.3 reported.
  - **⚠ Owed: the texture measurement that justified shipping ED-PC-0052 and ED-PC-0054.** Both are
    aggregate-inert and both cite U10's texture-not-winrate ruling; neither ran it.

- **▶ JORDAN RULED THE CARRY-CONTEXT FORK AND GROUNDED THE CURVATURE MODEL (2026-07-29, live). READ
  `audit/2026-07-26-combat-balance-customization-state/curvature_and_bind_model_v1.md` FIRST** — his
  six-part direction is recorded verbatim there with every measurement taken against it. Summary:
  - **⚖5 / M14 / Q8 / D2 (carry context) is RULED and adoptable** — battlefield: all; settlement public/
    religious/parliamentary: none-or-light armour + 1H non-blunt only; soldier/troop exempt. Derives
    entirely from stored primitives (`head_len+grip_len`, `hands`, `head`), threshold in the roster's own
    0.30 m empty gap. **Diverges from proposal §12 by exactly one weapon (the mace — Jordan bars blunt);
    his ruling governs.**
  - **⚠ §12.1's CENTRAL CLAIM IS FALSIFIED.** Carry context does NOT remove the dominance problem; it
    RELOCATES it. Civilian field spread **66.8pp is LARGER than the battlefield's 52.1pp**; sidearms-only
    45.1pp. Do not build on §12's promise.
  - **Legality delivers "pikes fare poorly in duels" by EXCLUSION only, not performance** — with war
    weapons present under civilian armour the spread is **78pp** (guandao 88%). Jordan accepts legality
    for now. **The performance half now routes to a future GRID TACTICAL LAYER (FFT-shaped, per-attack
    mini-resolutions) — on a grid reach is POSITIONAL (range in tiles), so DO NOT commission the
    closed-phase LEVERAGE/DAMAGE rework the older handoff scoped; the grid may subsume it.**
  - **A7a channel 1 DONE (ED-PC-0051)** — native edge quality finally consumed; the register's own
    proposed fix was re-confirmed a NO-OP. Keen cutters gained (scimitar +6.1pp … sabre +2.3pp), spread
    45.1→40.6pp. **⚖ TWO ITEMS FOR JORDAN:** the greatsword/hook_sword flip to point at `none` (a
    consequence of the katana anchor), and the anchor choice itself.
  - **Channel 5 DONE (ED-PC-0052) — and its FAILURE is the most useful result of the session.**
    `contact_moment_edge` now supplies displacement resistance to all three weapon-contact sites
    (bind + parry + wind), keyed on the grip-adjusted moment `S_g` rather than mass (the rapier is the
    *heavier* weapon, so mass moves the wrong way). Correct physics, mutation-verified, ablatable.
    **It does NOT fix the rapier: K swept 0/0.20/0.40/0.60 gives 75.6/76.2/75.9/75.3% — flat.**
    Per-event texture moves a lot (122 of 212 armour cells) while aggregate ordering does not — the
    ED-PC-0022 texture-vs-aggregate lesson again.
  - **▶▶ THE RAPIER'S ACTUAL DRIVER, and it changes the whole plan: `corr(overall length, civilian
    win%) = +0.850` (+0.742 excluding the rapier itself).** The civilian duel field is ordered by
    **REACH**, not by contact mechanics, edge quality, or the hilt. The rapier is simply the longest
    civilian weapon at 1.14 m. **This UNIFIES the civilian-field problem with the already-tracked
    off-plate reach dominance — ONE root cause at two scales, not two problems.** Reach is proven not
    reachable by lever (four swept; every fix broke `guisarme@heavy`), and Jordan has routed it to the
    future GRID layer where reach becomes positional range.
    **CONSEQUENCE FOR SEQUENCING: no further contact-side or cut-side lever can fix the civilian field.
    Do not spend another batch trying.** A7a (ED-PC-0051) and channel 5 (ED-PC-0052) were both aimed at
    the wrong pathway — they were each real, independently-worth-fixing defects, and neither moved the
    field. The remaining curvature channels (2–4) should be judged on physical correctness, NOT on any
    expectation that they will level the duel.
  - **Channels 3–4 (curved thrust) — the defect is DATA, not formula.**
    **corr(curvature, point_concentration) = −0.729 across 42 bladed weapons**: the tip data was
    authored largely AS a function of blade curvature, and `thrust_factor` then applies a curvature
    penalty AGAIN — a double-count of the class the R3 ruling forbids. **shamshir pc 0.08 is below
    sparr_axe's 0.10, an axe.** Template for the correction exists in-roster: **szabla, curv 0.30 /
    pc 0.60.** ⚠ Interacts with ED-PC-0050's binary shear-OR-puncture arm split — do not extend that
    split further until resolved.
  - **Channel 2 DONE (ED-PC-0054) — and its PRE-REGISTERED PREDICTION FAILED, which is the headline.**
    `_recovery_mode_commitment`'s C_swing branch is discounted by `(1 − CURVE_RECOVERY_K·curvature)`;
    swing-only, bounded [1−K,1] by construction. Throughput was checked FIRST this time (recovery feeds
    tempo debt on every committed attack). **Predicted curved cutters +1..+3pp; measured
    corr(curvature, delta) = −0.003, mean |delta| 2.6pp against a ~4pp floor — aggregate-INERT, like
    channel 5.** Shipped because the physics was absent, is per-event live, and U10/ED-PC-0022 already
    ruled TEXTURE (not aggregate winrate) is the right instrument for a situational lever. **The texture
    measurement is NOT done and is the honest gap.** ⚠ Its effective size rides on the pc-confound
    (−0.729), so **re-measure it when channels 3–4 fix the tip data.**
  - **▶ ADVERSARIAL SWEEP DONE (ED-PC-0055) — engine is CLEAN on dead code.** AST call-graph over
    engine+workbench+tests: zero unreferenced functions, zero CFG keys with no reader, zero
    test-only tunables. Two duplications fixed byte-identically (`_puncture_adef` — a §8 violation
    ED-PC-0049 introduced two batches earlier; `wound_impairment` — the ED-1041 rule written FOUR
    times under different local names). ⚠ **The sweep's FIRST detector was wrong** and called 8 live
    functions dead by ignoring intra-module calls — hand-verified before reporting, nothing acted on.
    **Confirmed dead physics, Jordan's call not a defect: `core.COVERAGE_GAP['partial']=0.5` is plumbed
    into `_transmit` with no caller ever passing `coverage='partial'`** — the shield/off-hand hook
    (⚖6), independently reproducing ED-PC-0035's F8.
  - **⚠ THE SESSION'S STANDING LESSON, three batches deep: a correct absent mechanism is not a balance
    fix.** A7a (cut grading), channel 5 (contact moment) and channel 2 (curve recovery) were each a
    real missing physical fact, each correctly built and mutation-verified, and **none moved the
    field.** The only change that moved the rapier was ED-PC-0053, which removed a *fiat gate* and gave
    an existing dominant quantity a *cost*. **Look for missing COSTS on dominant quantities, not
    missing benefits on weak ones.**

- **▶ E0–E3 ARE COMPLETE (2026-07-29, second session).** E0/E1a/E1b/I4 merged (PRs #259,
  #269), E2a merged (PR #270), and **E2b/E3a/E3b landed this session as ED-PC-0048/0049/0050** — the
  whole no-⚖ span of `combat_execution_plan.md` is done. EDs 0041–0050 filed; **draw 0051+ from the
  reserved block 0041–0055 (`id_reservations.yaml` is FROZEN for the run — do not edit it).**
  Live suite baseline **1142 passed / 21 skipped / 3 xfailed / 3 xpassed**.
  **NEXT: E4+ are all ⚖-blocked (plan §7) — nothing further is startable without Jordan.** The
  unblocked work is the three I4 wrapper defects (F-1/F-2/F-3, below) and the largest blind spot
  (`wrapper.py`, §12 of the plan). Both need Jordan's priority call.
  - **E2a's adversarial re-read is DONE (it was the one batch in the arc with no critic relay), and
    it found a real defect — in E2a's PRESCRIPTION for E2b, not in E2a's own code.** E2a's docstring,
    plan §5 and the E2a commit all specified `strike_point_lever(w, elem_mass, elem_x)` for the
    element scale. That signature double-counts mass (the function divides its mass argument by the
    weapon's total, so mass enters at power 1.5) and was measured to drop percussion **19–37% on all
    53 weapons** — a roster-wide balance change inside a batch declared "no balance intent". It was
    measured before being consumed and **not taken**; the correct call passes the delivered mass so
    the lever reduces to the geometric `(h+|x|)/(h+Lt)`. `test_element_lever_does_not_double_count_mass`
    pins it so the prescription cannot be re-followed. **Do not "restore" the prescribed form.**
    Also corrected: E2a's claim that its lever is a *strict* generalisation of `PoB_frac` is false
    (it takes `|x|`, so the 3 weapons whose balance sits behind the hand map to the positive lever);
    harmless, since all three are non-blunt and never reach that line, but the prose was wrong.
  - **⚖ E3a's residual parity is Jordan's (ED-PC-0049, needs_jordan).** The blunt-composite spike is
    no longer de-rated by the reach-thrust lever, so poleaxe adef 0.6013 → 1.0200 and its plate sigma
    −0.20 → +0.51 — plate no longer shields against a poleaxe. But that is **78% of its own hammer's
    1.3000, not the parity `ADEF_POINT`'s comment claims**. Closing the last 22% needs
    `ADEF_POINT ≥ ~1.53`, which lifts `armor_defeat_sigma` for every selected-point weapon at every
    armoured tier and trips the export gate — the plan flags it escalate-rather-than-take, and it was
    not taken. Note the hammer reference is itself inflated by E2a's saturation residue (poleaxe pins
    at `PERC_CAP`: 1.3000 where it read 1.2162), against which the spike already sits at 84%.
  - **⚖ E3b's two-direction split is Jordan's (ED-PC-0050, needs_jordan).** Heft now follows the
    resolved arm. Forward-balanced polearms' thrusts fall hard (voulge 5.21→1.72, partisan 4.17→1.70,
    ranseur 2.52→0.80) while hand-balanced swords' thrusts **rise** (arming 0.77→1.07, longsword
    1.00→1.26) because their `PoB_frac` sits below `THRUST_POB=0.16`. That is the constant's own
    definition, not a tuning choice — but whether the rise is the intended feel is a design call.
  - **NEW WORK-LIST HANDED TO E5/M7 (ED-PC-0050):** `core.cut_thrust_arm` picks the arm on **coupling
    alone**, so now that impact differs by arm the chosen arm is no longer the max-damage arm for
    some weapons — a fresh instance of the B1/F24 "selection contradicts damage" class, live at every
    tier. Deliberately NOT fixed (bundling it would repeat the batch-4/5 half-stands); the affected
    population is pinned by `test_selection_contradicts_damage_is_disclosed_not_silent` so it cannot
    widen unnoticed before E5 picks it up.
  - **The PC ledger hit its 50k cap and now has an archive** (`registers/editorial_ledger_pc_archive.jsonl`,
    PC is the second lane after IN). 28 settled entries moved; open/deferred/needs_jordan stayed live.
    Archived-ED citations resolve through `validate_ed_citations`' archive glob — verified by hiding
    the file (28 violations) and restoring it (0), not assumed from the size-checker's comment.
  - **⚖ TWO CALIBRATION RESIDUES FOR JORDAN, disclosed not tuned (ED-PC-0047):** the repaired staff
    reads 5.629 vs core.py's recorded "~4" intent (unreachable at PERC_EXP=0.30 while mace pins at
    PERC_CAP — the arithmetic is in the docstring), and mace/poleaxe/goedendag now all compress to
    an identical 8.000 against the cap (an ordering computed then discarded — the M8/F8 saturation
    class). Both are the deferred Phase-C `PERC_SCALE`/`PERC_EXP` re-fit.
  - **⚖ THREE HIGH WRAPPER DEFECTS from I4, open, each needs its own batch:** F-1 half-sword form
    carries across engagement boundaries (turn-1 0/120 vs turns-2+ 398/398; no test sees it) · F-2
    every fatal blow bypasses the damage-bearing `outcome` emit (199 fellings, 0 preceded by it) ·
    F-3 the `sim` flag is provably always False (dead `disrupt_resist_p`). Priority vs E2b/E3a/E3b
    is Jordan's call.
  - **Open sign-safety residue (ED-PC-0045):** `init_hold_decay` multiplies the SIGNED initiative
    state by an `eff_cw('measure')` factor — `misura` keeps a deficit alive longer. The E1a guard is
    lever-keyed so it cannot see second consumers of a covered lever.
  - **TIERING — read before spawning anything (this session's costly mistake):** ~16 critic/refuter
    subagents inherited the session model and ran on **Fable at 10×** because no `model:` was set.
    §10 is explicit that Fable is *an upgrade trigger, never a default*. **Set `model:` on EVERY
    dispatch** — Sonnet for bounded/mechanical checks, Opus for gating verdicts.

- **E0 BATCH EXECUTED + I4 DELIVERED (2026-07-29, ED-PC-0041..0044) — PRs #259/#269 MERGED.**
  Six gated commits (each: Opus producer → independent suite run → read-only valoria-critic pass):
  CI enforcement restored (18 combat test modules were silently skipping in the shipping gate — 837/93
  CI vs 972/21 local, proven from live CI logs), vocabulary ownership (`vocabulary.py` owner, 2 guards
  red-first, dead surface deleted, export 201→200), riders I1a/I1b/I3 (I1a's briefed defect was STALE —
  fixed by ED-PC-0023; recurrence guards delivered), and I4's `wrapper_emit_key_map.md` (15 emit kinds
  classified for IN's Wave 3 + 8 registry findings). Suite 972→999, byte-identical throughout, goldens
  untouched. **⚠ I4 audit found 3 HIGH wrapper defects, reported NOT fixed (each needs its own batch):
  F-1 half-sword form carries across engagement boundaries (the §12-predicted ED-PC-0033 class, no test
  sees it) · F-2 fatal blows bypass the damage-bearing outcome emit · F-3 the `sim` flag is provably
  always False (dead disrupt_resist_p).** Next: after PR #259 merges, restart the branch and run
  E1a→E3b per `combat_execution_plan.md` (EDs 0045+ from the reserved block); slot F-1/F-2/F-3 by
  Jordan's priority call. Register corrections relayed to IN in the PR body (OI-13/44/45/46).

- **2026-07-26 COMBAT ARC — report, register, catalogue, proposal, independent audit, remediation plan (no ED;
  all report/design-only, HELD FOR JORDAN).** Consolidated to a pointer because appending full summaries pushed
  this file past its 20k cap four times; the detail is durable in the artifacts.
  - **▶ START HERE (merged 2026-07-29, PR #249): `combat_execution_plan.md`** — the WORK ORDER for a fresh
    session. Batches **E0–E3 need no decision from Jordan and are fully specified**; E4+ list their ⚖ blockers.
    Carries §2 the traps this arc actually hit, §13 orchestration, §13.2a the **red-state ledger** (the
    pre-measured failing pin for all 11 guards, incl. the one that is tautologically green and must be
    mutation-verified instead), and §14 the Fable review record (11 findings, 5 would have caused a wrong result).
  - **Artifacts.** `audit/2026-07-26-combat-balance-customization-state/` — **`combat_balance_state.md`** (the
    measured balance state; the former `_index`/`_infill` pair was merged into it when CLAUDE.md §4 retired that
    convention on 2026-07-26 — **the old filenames no longer exist**), **`combat_defect_register.md`** (§A–§I:
    every defect, each tagged `[tracked]` vs `[new]`, incl. §G the independent audit and §H the structural
    scan), **`combat_remediation_plan.md` (PLAN OF RECORD — M1–M18, batches R0–R9)**,
    `combat_value_catalogue_GENERATED.md`. Proposal:
    `proposals/2026-07-26-personal-combat-player-agency-and-tradition-curriculum.md` (§1–§20).
    New instruments, all re-runnable: **`workbench/build_levers.py`** (the 4 build inputs `balance._mk` cannot
    express; `mirror 2000` is the fairness control), **`workbench/catalogue.py`** (51 weapons × 49 quantities +
    coupling matrix + 226 tunables; mechanics generated from live docstrings so it cannot drift),
    **`workbench/structure_scan.py`**.
  - **START HERE if picking this up: plan §8.** R0 → R1 → R2 → R3 are defect-only and ⚖-free. **If only one
    batch runs, run R1 (M5+M4) — M5 makes the investment system PUNISH investment**, live for every invested
    build, invisible only because `equipped=[]` by default. If two, **R0 first** (vocabulary ownership), because
    **M15 is a PREREQUISITE for M6/M7/M9** — all three edit token-keyed branches, and F6/A7b prove an unowned
    token set makes such edits silently wrong. **M16 scopes INTO M8** (`defense_affinities`' 23 literals ARE the
    band edges F7 shows floor-pinning 36/53).
  - **Do-not-re-discover facts:**
    1. **F1 the staff's `percussion_authority` is EXACTLY 0** (lever is CoM offset; centre-gripped haft ⇒ 0
       regardless of mass) — verified; diagnoses A4's staff cliff. **F3 PLATE SHIELDS AGAINST THE POLEAXE**
       (hammer 1.216, spike 0.601, threshold 0.72) — verified; PC-5's `tauth` broke ED-1080 after its comment
       was written. **F5 ability channels are SIGN-BLIND** (bind_sigma −1.0562 → −1.1904 when the disadvantaged
       side invests) — verified; **proposal §5 re-classed `measure`/`leverage` C-BROKEN + new sign-safety rule 5;
       do NOT author content onto them (I-7) until fixed.**
    2. **A7a `core.coupling` IGNORES `eff` for native cut tokens** — 20× sweep returns a constant; 16 weapons
       (31% of roster) couple identically regardless of edge; curvature is all cost, no benefit. **SURVIVED the
       blind audit** (not a duplicate). **⚠ my own A7d fix sketch was a NO-OP** — `min(1,eff/0.70)` against a
       0.71–1.33 population; amended at source; **do not implement as written.**
    3. **`core.COVERAGE_GAP{'partial':0.5}` is plumbed but has NO caller** — the shield's damage hook exists and
       is merely unreachable (A6 becomes "wire a caller", not "design a subsystem").
    4. **Carriability derives from `head_len+grip_len`** (already stored): roster self-separates ≤0.60 /
       0.75–1.20 / **≥1.50 m**, 0.30 m empty gap, and **all 26 weapons in the dominant 91–97% band are ≥1.50 m —
       the dominant band IS the war band.** Re-derive the bands, never freeze them (X6).
    5. **All 226 params are exported to Godot**, so every increment trips the round-trip gate — which checks
       JSON-matches-config, NOT that the port implements it. **B13 is the PATTERN, not a one-off.**
    6. **Single ownership is HOLDING** — the one cross-module duplicate (`adef_cap`) is a documented ED-PC-0038
       delegate; zero constants defined twice.
  - **⚖ 8 calls are Jordan's** (plan §3): M6 direction · armour cost · disposition shape · 38/53 plate
    participation · carry-context taxonomy + scene-tagging (X2 — the 55-arc corpus was tested and is NEGATIVE:
    every "court" hit is legal/political, not a location) · off-hand scope · the thrust-lean · typed weapons.
  - **⚠ LARGEST BLIND SPOT, covered by NO batch:** `wrapper.py`'s mutation ordering, RNG-draw sequencing and
    burst/latch state machine were only spot-checked. Stale `sel_*` carryover and draw-order divergence live
    there. Strongest candidate for the next independent audit.
  - **CI PIN:** `test_build_proposals.py` pins the proposals-doc count (**19**). Bump + comment when adding to
    `proposals/`. `valoria_local --staged` does NOT run pytest — run `pytest tests/valoria` AFTER adding one.

- **FOUR-DIMENSION AUDIT + REMEDIATION (ED-PC-0034..0040) — batches 1–5.2 landed, batch 6 pending.**
  *(This block was missing until 2026-07-25 — the lane handoff had not been updated since batch 3, flagged by the
  ED-PC-0039 adversarial review. Note the "prototype ED-PC-0034" mentioned further down in the off-plate-reach item
  is an ABANDONED experiment label, not this ED-PC-0034; the number was reallocated after that prototype was reverted.)*
  Jordan's charter: four independent read-only audits — **fiat, orphans, conflicts, tuning/balance**, each covering
  *all directions and conditionals* — then resolve every finding in priority order, batch by batch, adversarially
  reviewing after each batch. Full record: `audit/2026-07-24-combat-four-dimension-audit/` (index + infill, co-filed).
  - **Landed:** 0034 correctness (represent-gate path-dependence, riposte exposure floor, grab sign-flip) ·
    0035 dead code + stale prose · 0036 fiat retirement (percussion single-source, cut_thrust branch, pursuit σ) ·
    0037 (+0037.1) structural thresholds — first-actor race resolved as **cadence × anticipation from an arbitrary
    initial phase**, not noise (Jordan: *"what happened to feinting and anticipating"*), soft closed-latch,
    `ATTACKER_BIAS` retired · 0038 capability-gated penetration (`adef_cap` moved to `core` as single owner) ·
    0039 knee corrections (clamp capability at ≥0; grip/room threaded; K swept) · **0040 the 0039 review response.**
  - **Review record, unflattering on purpose:** batches 4, 5 **and 5.1** each returned **half-stands**. Every
    correction is in the ledger; nothing was quietly re-based.
  - **META-REVIEW → ENFORCEMENT (ED-PC-0040).** All three half-stands share one cause: quantitative claims written
    faster than they were measured, with the falsifying scripts ad-hoc and discarded. Converted into gates, not
    resolutions (a resolution is what failed three times) — **use these rather than re-deriving them**:
    - **`workbench/armour_participation.py`** — the armour-interaction instrument. `participation` (capability
      partition vs measured decided-rate), `strikes` (per-strike damage **by selected head** — this is what found
      F24), `tiers` (all four tiers; run in a worktree at another sha and diff), `--update` / `--drift`.
      **Every armour claim should be a query against this, not a recollection.**
    - **`tests/valoria/data/combat_armour_reference.json`** + `test_combat_armour_reference.py` — full roster × all
      four tiers, drift gate at 0.15. If your change trips it: *intended* → regenerate with `--update` and commit,
      **the diff is the required disclosure**; *unintended* → you just learned your blast radius. Do NOT regenerate
      to turn a build green without reading the diff — that defeats the gate entirely.
    - **`test_plate_participation_guard_is_not_blind`** — declared mutations that must make the participation guard
      fail *and* be named in its message. Add a mutation when you add a guard; never weaken a guard until a mutation
      stops being caught.
    - **`tools/ci_claim_provenance_check.py`** (blocking, CI + local) — a PC-lane ledger entry from ED-PC-0040 onward
      that states measured numbers must carry `MEASURED-BY: <path>` pointing at something that exists.
    - The CI guard **imports** its capability derivation from the instrument (CLAUDE.md §8 — every rule lives once).
      Do not inline a second copy; the first draft did, and that is the same duplication class as the bug.
  - **NEXT — batch 6, in this order:**
    1. **F24 (new, high) — selection contradicts damage.** `select_mode` picks heads that provably cannot wound:
       falchion selects `point` on 46/47 plate strikes for 0 damage; podao picks `point` (mean 0.00) over its own
       `curved_cut` (mean 2.40) 78% of the time; every 2H sword flips to `blunt` at *mail* (odachi 703/703 strikes,
       mean 2.77 vs the arming sword's 8.48). Selection is keyed on afforded effectiveness with no reference to
       whether the head can defeat the armour in front of it — the ED-PC-0038 defect class one layer up. Golden-parity
       blast radius: budget it a batch of its own.
    2. **F21 — `ADEF_CUT` grading by mass/keenness.** Now load-bearing: ED-PC-0039's clamp floors every pure cutter
       to capability 0, so nothing distinguishes a bardiche from a shamshir. The sigma path has to carry it.
    3. **F22 — roster gaps** (sparr_axe horn, falchion point, greatsword/odachi half-sword, staff wound-coupling).
    4. **F23 — hollow `eff_cw` channels** (5 of 8 are identity ×1.0 for every legal build).
  - **Carried open (do not re-discover):** off-plate reach still ~0.94 vs Jordan's ~0.75 (see the item below — proven
    NOT reachable by lever); the **ranseur** is a surviving covert plate-killer (cap 0.284, settles ~12% of plate
    fights, wins ~100% of them); the medium tier never round-tripped after 0038 (odachi −41pp, naginata −25pp,
    staff −12pp); the four-channel armour-defeat double-count has no recorded budget; `PEN_DEFICIT_K` is exported to
    a Godot contract whose port has no penetration knee.

- **REACH-ARC (ED-PC-0029..0033) LANDED on PR #231 (2026-07-24) — full suite green (656).** arrest-impulse +
  tanh true_time (0029); closed-phase disengage (0030); percussion→stamina + poise stagger (0031); rapier plate
  fall-off via penetration threshold (0032, `core.PEN_THR`); **stale-grip fix + measure continuity (0033):**
  engagement() resets grip/lunge to open measure each engagement and threads `prev_closed`; `represent_measure_p`
  crowds a reach weapon off measure at plate (exp(−K·ADEF_W·deficit), exactly 1.0 off-plate so the RNG stream/
  tradition-texture is inert). Spear heavy 0.97→0.08; poleaxe 0.95, guisarme 0.61 (gap-defeaters still present).
- **OPEN (Jordan-flagged on PR #231): off-plate reach re-baseline — turn the lever down.** Fixing the grip bug
  (0033) globally strengthened reach weapons off-plate (spear ~0.93–0.95 at none/light/medium, was bug-suppressed
  ~0.75). Jordan chose **turn it down** (target ~0.75, "duel edge not auto-win"). **INVESTIGATED 2026-07-24 — it
  is NOT a knob:** ablation proved off-plate dominance is *structural* — the spear beats arming **0.92 even when
  forced fully closed** (represent=0), i.e. it out-fights the sword at every measure, not just via approach stop-
  hits. `STOPHIT_CHANCE`/`STOPHIT_COMMIT`/`REPRESENT_BASE` all fail to reach 0.75 without breaking guisarme@heavy
  (proven by sweep). Root cause: a crowded long weapon "chokes up" (`grip_target`→1) and `close_unwieldiness` only
  penalizes TEMPO, not exchange power — so a crowded spear still wins the bind. **The honest fix is a closed-
  measure EXCHANGE penalty for crowded long weapons** (a spear should be out-fought inside its point; choking
  shouldn't fully rescue it) **coupled with a `REPRESENT_BASE`<1 off-plate contest** (a pressing swordsman denies
  re-presentation even unarmoured). **ATTEMPTED 2026-07-24 as a prototype ED-PC-0034 and REVERTED — even the
  closed-measure exchange penalty is INSUFFICIENT.** Built `close_crowd_sigma` (grip × native over-length →
  net-σ penalty, added to reach_pen) + `REPRESENT_BASE` + `STOPHIT_COMMIT`; joint-swept all four levers.
  Findings: (a) the crowd penalty barely moves forced-closed spear (0.92→~0.87) — the spear out-fights the sword
  in the close through MULTIPLE composing channels (2H leverage in the bind, damage, reach-even-when-choked), so a
  single σ penalty can't overturn it; (b) it TANKS guisarme@heavy below its 0.30 floor (guisarme is also long → is
  crowd-penalized at plate where it must win); (c) off-plate the kill often happens in ENGAGEMENT 1's approach
  (prev_closed=False → the re-presentation gate is inert on turn 1), so `REPRESENT_BASE` can't bite; (d)
  `STOPHIT_COMMIT`/`STOPHIT_CHANCE` barely move off-plate (reach wins even at 0.35 chance / 0.4 commit) yet also
  break guisarme@heavy. **Conclusion: bringing off-plate reach to ~0.75 is NOT achievable via approach/represent/
  crowd levers without violating guisarme@heavy — it needs a fundamental rework of the closed-phase LEVERAGE/
  DAMAGE model (why a spear out-fights a sword in the bind at all), a large high-risk change with no bounded fix.**
  All experiments reverted; ED-PC-0033 state is clean/green (656). Recommend either accepting off-plate reach at
  ~0.93-0.95 (honest un-bugged value) or scheduling a dedicated closed-phase-model session with its own
  invariant-safety plan.
- **OPEN (matrix quirks, pre-existing — NOT from the reach arc; PC-lane roster calibration):**
  1. **`sparr_axe` armour cliff (0.94 light → 0.20 medium → 0.06 heavy).** Weapon record has a SINGLE
     `straight_cut` element, `adef_cap=−0.90` — it cannot defeat *any* armour. A sparth/war-axe realistically has
     a concentrated edge (and, poleaxe-family, a top-spike) that defeats mail; cf. `poleaxe` = 3 elements
     (blunt+spike). Fix = give it a proper armour-defeating mode (design call: spike vs concentrated-edge
     percussion). `bardiche` shares the single-`straight_cut` record but is a genuine cleaver, so its fall-off is
     more defensible (borderline).
  2. **`jian`/`tsurugi` marginal plate edge (heavy ~0.94 but decided only 17–45% → mostly stalemate).** Their
     geometry yields `adef_cap` 0.543/0.535 > arming's 0.504, so a light straight sword slightly out-points the
     arming in the plate stalemate. Minor geometry recalibration; low-decided so low-impact.

- **'BUILD ALL' PASS DONE (ED-PC-0026/0027/0028, 2026-07-23) — Phases 1-4, all committed & pushed to PR #227.**
  - **Phase 1 (ED-PC-0026):** HEMA grounding corrections — atajo measure→leverage, zwerchhau edge_read→counter_select,
    guardia REMOVED (facing_regime now a bare lever), phi_grip tag narrowed, stale winden comment fixed.
  - **Phase 2 (ED-PC-0027):** T_vuln undefended-time model + mode-aware heft. Thrust heft PoB-DECOUPLED
    (m_head*THRUST_POB=0.16) — fixes spear flat-dominance + heft ordering (ED-PC-0010). T_vuln exposure
    (EXPOSE_CLOSE_K=0.6, EXPOSE_SELECT_K=0.3) makes swings cost their undefended window in the fight AND in
    select_mode → thrust-capable weapons prefer the point in the 1v1 (poleaxe spikes every tier), pure cutters keep
    cutting. Resolves poleaxe gap-game (ED-PC-0012 lineage).
  - **Phase 3:** the 9 pre-existing intentional-red failures all resolved emergence-first (heft ordering via Phase 2;
    poleaxe → thrust-in-1v1; sabre pure-cutter fiat retired via continuous THRUST_AUTH_REF de-rating; element-parity +
    r3_identity + heft goldens regenerated/reshaped for the roster growth + new signatures). Combat suite 160 green;
    full suite 639 passed / 0 non-combat regressions.
  - **Phase 4 (ED-PC-0028):** tradition-gate on equipped — an untaught cross-tradition technique is inert (closes the
    interaction-critic's build-legality gap); cross-training via `known_traditions`.
  - **OPEN / NEXT ACTIONS:**
    1. **Balance re-verification** — the independent adversarial balance critic was LOST to a worker restart mid-run;
       I finalized calibration on my own foreground measurement (defensible: rapier rules the light duel, plate-defeaters
       vs plate, mirrors fair). RE-RUN an independent balance critic to double-check the roster-wide thrust-lean.
    2. **Jordan's steer on the roster-wide thrust-lean** — the emergent consequence (cut+point weapons prefer the point
       in a 1v1) is [SIM-CALIBRATE]-magnitude (THRUST_POB/EXPOSE_SELECT_K); confirm the feel is desired vs. giving
       cut-primary weapons more cut-identity. Watch items: spear/yari soft vs longsword (0.33/0.37), guandao strong
       (0.84) — within the PRE-EXISTING reach-above-band (i8 item 1), reduced not worsened by this change.

- **COMBINATORIAL/ISOLATION AUDIT + NODE INTERROGATION DONE (ED-PC-0025, 2026-07-23).** Isolation sweep +
  node-grouped interaction matrix + all-node pipeline trace + two adversarial critics (dead-wire forensics,
  interaction degeneracy). **VERDICT: no dead wires** — the morphology levers are situational-per-event and
  *frequency-gated by their enabling skill* (no bind skill → no binds → spine lever has nothing to amplify;
  deep+paired investment = +13pp vs an equal opponent). Contact axis is decisive (35% dagger flip); only its knobs
  are aggregate-neutral. **FIXED (ratified):** single-source overflow-safe `core.logistic()` (5-way open-coded squash
  collapsed; out-of-contract OverflowError 99/300→0/300, byte-identical legal builds); `INJECTION_POINTS`
  imposition-doctrine residual → emergent model. See `audit/2026-07-23-combat-combinatorial-audit/findings_v1.md`.
  - **DEFERRED / NEXT ACTIONS (surfaced, awaiting Jordan — Jordan is actively designing #1):**
    1. **Mode-exposure / undefended-time model `T_vuln`** — Jordan directive 2026-07-23: swing-vs-thrust
       exposure-to-counterattack is NOT modelled at the mode level (`select_mode` is exposure-blind;
       `overcommit_exposure`→`recoverability_factor` reads whole-weapon pc, not `sel_pc`). Design agreed: a
       vulnerability window `T_vuln` = delivery + recovery + measure, blended by point_concentration, driving the
       counter/exposure path and feeding mode selection so the poleaxe spike *emerges* vs plate. Grounding hierarchy:
       structure from first-principles kinematics (self-consistent with `_recovery_mode_commitment`), magnitudes
       cross-checked against HEMA-biomechanics **mocap** (supplement), direction from Silver's "times" / Le Jeu de la
       Hache. **NOT BUILT — Jordan paused implementation; build on his word.**
    2. **HEMA historical-grounding corrections** (adversarial critic): `guardia`→facing_regime WRONG (guardia stretta
       = close-*measure* guard, not body-facing), `atajo`→measure WRONG (→leverage), `zwerchhau`→edge_read WRONG-leaning
       (real function tempo-interception), `phi_grip` `[ASSERTED]` tag overclaims, stale `combat_systems.py:766`
       "German Winden" comment → shinogi. Not applied.
    3. **No-tradition-gate on `equipped`** — build-legality gap (any fighter can equip every tradition's kit).
    4. **The 9 pre-existing intentional-red failures** — Jordan chose "fix all emergence-first" (element-parity golden
       regen; sabre pure-cutter = retire the fiat assertion; poleaxe = resolve via `T_vuln` #1, NOT a test-relax;
       spear heft/ED-PC-0010 = derivation fix). Not executed (paused with #1).

- **LEVELS OF INVESTMENT FOR TECHNIQUES DONE (ED-PC-0024, 2026-07-23) + PR #226 ratification-flip.** Graded the
  binary equipped-ability into a continuum: `ability_factor` = product of `value**level`, `ability_bonus` = sum of
  `value*level`; `equipped` supports a list (level 1.0, back-compat) or `{name: level}` (level>=0; 0=inert). Efficacy
  emerges from the invested level, not tradition membership (tradition gates access; investment+skill drive efficacy
  — realises ability_primitives' own TARGET MODEL). Back-compat byte-identical; suite 9 accepted-red + 2 investment
  tests. Also flipped the PR #226 ratification bookkeeping (ED-1094): u10_activation_v1.md + fiat_audit_v1.md
  Status PROPOSED→RATIFIED, ED-PC-0022/0023 needs_jordan→false, CURRENT.md combat row corrected to the post-review
  final state (shinogi not winden; +2.8pp retracted; texture instrument; imposition retired; design principle).
  Forward: a character-gen/economy layer to BOUND investment (out of engine scope); the roster `value` constants are
  the level-1 anchors [SIM-CALIBRATE].

- **IMPOSITION FIAT RETIRED (Jordan ruling 2026-07-23, ED-PC-0023) + design principle recorded.** `impose_node`
  FORCED a tradition's preferred node via a label coin-flip overriding the emergent resolution — top-down scripting.
  Retired: `IMPOSITION_GATE=False`, `impose_node` → no-op, `IMPOSE_BIND_BOOST`/`IMPOSE_REFUSE_P` deleted (reverses the
  ratified WS-4 default, per Jordan's live authority). Tradition-preference now EMERGES from build (skill investment
  + weapon + abilities + disposition, all already live in mode_sigma/bind_sigma — verified: bind-skill 1/2/3 →
  61/71/75% win-share, monotonic, no fiat). **GOVERNING DESIGN PRINCIPLE (Jordan, recorded in
  `audit/2026-07-23-combat-fiat-audit/fiat_audit_v1.md`):** each combatant's feel emerges from their full stack
  (tradition/abilities/attributes/weapon/armour/disposition), resolving true to their style; every build AVAILABLE
  (not every build good) — expressive availability over parity; efficacy from INVESTMENT/EXPERTISE, not membership;
  no fiat. **NEXT INCREMENT (forward architecture): levels of investment for techniques** — grade `ability_factor`
  by an invested level (the pattern `skill()` already sets), turning binary equipped-abilities into a continuum
  (the ability system's own target model: tradition gates access, investment+skill drive efficacy). Also open:
  PREFERRED (traditions.py) is now vestigial (kept as metadata for a future EMERGENT selection-bias, never a forced
  override); full `impose_node` call-site removal is a tidy-up follow-up.

- **ADVERSARIAL REVIEW of U10 + fiat-audit DONE (2026-07-23) — 4 independent critics + pessimistic NERS.**
  Correctness: CLEAN (signs verified by sign-flip, no bugs). NERS: SAFE (no runaway/degeneracy/new-extreme/dead-branch).
  Balance: the "+2.8pp specialist edge" was a CONFOUND (german+ability vs none+empty) — abilities are ~0 aggregate,
  per-event real; "field within noise" over-stated (grounded moves for grab/edge weapons, but no new extremes).
  Grounding: ability layer under-grounded. **Corrections applied (folded under ED-PC-0023):** retag winden->shinogi
  (japanese — grounded to the katana that HAS a spine; winden was a longsword technique inert on the single-edge
  lever); tagged all ability multipliers [SIM-CALIBRATE]; removed the confounded aggregate test → deterministic
  per-event test; tightened the guisarme re-baseline (none/light back to strict >0.5, medium contest only);
  corrected the u10 doc (§4 retraction + §7 review addendum) + the ED-PC-0022 ledger claim. **Ability layer is now
  framed as illustrative infrastructure, not a proven aggregate-balance feature.** Open follow-up: ground more
  traditions' abilities; the abilities' aggregate ~0 means the *activation's* value is the surface + per-event, not
  field balance — a Jordan design call on whether the (safe, grounded, ~0-aggregate) activation is worth keeping vs
  reverting to K=0-with-surface.

- **COMBAT FIAT / BROKEN-LOGIC AUDIT DONE (ED-PC-0023, 2026-07-23) — 4 independent adversarial passes.** FIXED
  (clean, contained, 9-accepted-red unchanged): THRUST_LEVER_FLOOR 0.30->0.24 (un-flattened 7 polearms);
  GAP_EXPOSURE ordering corrected to match core.py's own grounding (mail>plate; cloth mostly-accessible; plate
  anchor kept); removed dead Combatant.pool (§8); struck stale weapon_physics WIRING-STATUS doc. The flagged
  grip-invariant-thrust tenet was RULED GROUNDED (the force invariant is correct; costs homed elsewhere, no
  double-count). Doc: `audit/2026-07-23-combat-fiat-audit/fiat_audit_v1.md`.
  - **FLAGGED broken-logic — future increments (evidenced, fix-spec'd, NOT yet fixed; each needs its own verification):**
    1. **MAX_TEMPO_PEN=0.8 hard-cap flat-tops 38/53 weapons to 0.80** (biggest emergence-suppressor). Fix = surgical
       over-cap-tail `min(pen,MAXP)+K*tanh(max(0,pen-MAXP))` (arming sub-cap => mirror byte-identical); REQUIRES a
       deliberate regen of `tests/valoria/r3_identity_golden.json` (no generator exists — hand-reproduce). Own increment.
    2. **PERC_EXP=0.30 low-mass compression** over-credits native secondary blunt elements (lucerne fluke/bec beak) —
       the REVERSED_GRIP_EFFICIENCY=0.25 discount only patches Mordhau. Root recalibration, every blunt weapon — Jordan-gated.
    3. **PERC_TRANSMIT_FLOOR=0.35** flat-tops 11 Mordhau armour-transmission ratios.
    4. **IMPOSE_BIND_BOOST/IMPOSE_REFUSE_P fixed 0.5** — imposition carries zero skill-gradient (rewards membership not
       mastery); candidate to couple to eff_cw/ability_factor (design call).
    5. **adef_cap blunt branch doesn't thread sel_head** — puncture_pressure reads whole-weapon blade-tip concentration
       for a pommel-strike; latent/inert (ADEF_BLUNT wins the max()), structurally wrong.
  - **Editorial nit:** CLAUDE.md §5 "Combat Pool three ways" is overstated — live engine + core.md + module_contracts
    agree on max(5,History+6); only values_master.yaml is stale (self-flagged). Could tighten the §5 wording.

- **U10 morphology-lever ACTIVATION DONE (ED-PC-0022, 2026-07-23) — supersedes the U9 keep-at-K=0 verdict.**
  Re-examined the U9 verdict and found the six edge/choke/facing levers inert for FOUR reasons (wrong instrument /
  amputated tradition surface / choke-thrust mis-parked against the D2 force-invariant / near-invisible facing
  consumers). Executed the capstone's own re-charter: (1) RE-HOMED choke-thrust out of `phi_grip('point')` — D2
  force-invariant kept byte-identical, `CHOKE_THRUST_K` retired, the held-back `needs_jordan` DISSOLVED (no D2
  exception needed); (2) built the tradition-modulation surface — every lever site routed through
  `ability_factor(c,<channel>)`; (3) ACTIVATED to small grounded baselines (LEGIB_EDGELINE 0.04 / BIND_SPINE 0.03 /
  GRAB_EDGE 0.07 / CHOKE_ACCURACY 0.03 / FACING_REGIME 0.12) — no-ability field within harness noise; (4) added 4
  treatise-grounded abilities (winden/zwerchhau/ringen_am_schwert/guardia). Efficacy measured on the per-matchup
  specialist duel (Winden katana +2.8pp). The **U9 test-hygiene defect is FIXED** here (the global-write leak in
  `test_both_channels_live_not_dead` is gone — the constant is retired and the channel is exercised via cfg+equipped).
  9 accepted-red baseline unchanged; ONE grounded re-baseline (guisarme off-plate reach — see doc). Doc:
  `audit/2026-07-04-weapon-morphology-granularity/u10_activation_v1.md`.
  - **Open follow-ups (not blocking):** `choke_control` channel has the surface but no ability yet (needs a grounded
    pole/staff tradition); facing stays conservative pending C1 (absolute polearm facing direction) resolution; the
    ability baselines/multipliers are `[SIM-CALIBRATE]` and open to per-scenario tuning.

- **ED-PC-0007 (DEFERRED 2026-07-08, Jordan: "Defer PC") — pessimist-audit PC verdicts do NOT execute now.**
  The pessimist-action audit (ED-IN-0027) judged the discrete `combat_v30 §4` ACTIONS menu, but that menu is
  **PARTIALLY SUPERSEDED** (ED-900): its resolution layer is replaced by the canonical continuous resolver
  `designs/scene/combat_engine_v1/` (the ONLY up-to-date PC surface; `combat_v30 §4` and `sim/personal/combat.py`
  are stale). `combat_engine_v1` has no discrete player-action menu yet, and it **already realizes** the
  consolidations the audit recommended (continuous commit ⊇ Feint; Contact node I7b/D8-D9 ⊇ Disarm/Tie-Up/Retrieve;
  base offence/defence split ⊇ Full-Guard/Dodge) — so the audit retroactively validated the move to
  `combat_engine_v1` rather than finding live work. **No edits made to any stale doc.** The forward constraints
  (don't re-introduce these as separate discrete verbs when a player layer is built; Rescue/Take-a-Breath/Stunt
  refinements) attach to **ED-PC-0001** (the post-R3 player-input surface). Re-open only if `combat_engine_v1`
  grows a discrete menu that reintroduces the over-articulation.

- **R3 consolidation plan-of-record — `designs/audit/2026-07-04-weapon-morphology-granularity/consolidation_v1.md`
  (RATIFIED 2026-07-04 via PR #76 per ED-1094; JD-1 RULED 2026-07-08, JD-2…JD-8 remain OPEN, loudly held back).**
  Implementation progress:
  - **U0 (units honesty, ED-PC-0002) — DONE 2026-07-05** (branch `claude/begin-u0-arppwt`). head_len/grip_len →
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
    row omits it (identity forces it once grip_len is metres). See the ED-PC-0002 ledger entry.
  - **U1 (PoB recalibration, ED-PC-0010) — DONE 2026-07-08.** JD-1 RULED (Jordan: "accept plan bands" —
    consolidation_v1's default arms-scholarship ranges: rapier 3–11cm, greatsword 8–20cm, 1H 6–14cm, poleaxe
    20–55cm forward, staff ~0). `weapons.py` data-only blade/head→pommel/haft mass redistribution (total mass
    unchanged per weapon) for the 6 V7-flagged weapons: rapier 17.0→9.0cm, arming 17.8→11.0cm, longsword
    19.4→13.9cm (chosen so `recoverability_factor(longsword)`≈0.98, inside the existing anchor test's
    tolerance), greatsword 30.4→18.0cm, bec_de_corbin 5.1→22.0cm, lucerne_hammer 7.2→24.0cm (both poleaxe-family
    heads scaled ~2x to match poleaxe's own physical proportions). `weapon_physics.HEFT_REF` re-anchored to the
    new longsword value (preserves `heft(longsword)==1.0`; rescales `heft()` roster-wide, a deliberate
    re-baseline). Cinquedea (also flagged in V7 but with no JD-1-named band) deliberately left untouched — no
    invented band. Fixtures regenerated with recorded reasons: `r3_identity_golden.json` (53 weapons; only the
    6 flagged weapons' physics genuinely moved, confirmed via diff — every other weapon's shift is float noise
    or the uniform HEFT_REF rescale), `golden_heft_percussion_snapshot.json`. New
    `tests/valoria/test_combat_pob_bands.py::test_pob_within_realistic_range` pins the bands going forward.
    Retired 2 accepted-red tests as predicted (`test_anchor_is_near_one`, `test_lunge_quality_…`).
    **NEW finding (undocumented by the plan, not silently patched):** the correctly-banded arming/longsword now
    read BELOW spear's own untouched heft numerator even at each band's ceiling (checked exhaustively — no
    JD-1-compliant sword value can beat it) — `test_falsifiable_heft_ordering` /
    `test_heft_percussion_ordering_at_ideal`'s spear<arming term now fails. This corroborates, not contradicts,
    the already-tracked "SPEAR flat-dominance" finding below via a second symptom; both tests are left
    deliberately failing with the finding recorded in their own docstrings, per the same convention as the
    pre-existing `test_gap_game_poleaxe_spikes_plate` [PHASE-C FLAG]. A second, positive side effect:
    `lucerne_hammer`'s corrected head mass now makes it join `poleaxe`'s existing percussion-dominance
    exclusion in `test_use_mode_selection_emerges_from_primitives` (updated). Net accepted-red count 8→8 (2
    retired, 2 new — both PHASE-C-flagged, not silent); the 5 pre-existing `test_combat_element_parity.py`
    Phase-A fixture-schema-drift failures and `test_gap_game_poleaxe_spikes_plate` are untouched, confirmed
    out of U1 scope. `engine/engine_params/combat_engine_v1.json` unaffected (config.py untouched, verified
    via `export_engine_params.py --check`). 196 passed / 8 failed / 1 xfailed; `valoria_local.py --staged`
    clean. See the ED-PC-0010 ledger entry for full detail.
  - **U2 ATTEMPTED 2026-07-08, PARTIAL — findings filed as ED-PC-0008, then JD-4/JD-9 DETERMINED same day as
    ED-PC-0009 (Jordan: "determine both by testing bottom-up emergent primitives and validating top-down
    against history and hema and physics").** Immediately after U1 unblocked it, attempted U2 (graded mode
    affordance + Phase-C percussion enactment) and found consolidation_v1's one-line spec insufficient for a
    safe implementation (ED-PC-0008, 3 findings). Jordan then directed resolving JD-4/JD-9 via grounded
    research rather than deferring — both are now DONE at the formula level:
    - **JD-9 (thrust_factor floor bug) — RESOLVED.** Dropped the additive `point_concentration` floor
      (matching `cut_factor`'s already-fixed shape) — physics: pressure=force/area, a broad pointless face
      reads ~0 regardless of rigidity. Verified: mace/staff 0.34/0.31→0.02/0.04; every U2-named acceptance
      weapon still clears comfortably. `MODE_EDGE_MIN`/`MODE_TIP_MIN` both set to 0.15 (systems.py) — a clean
      margin, not the old fragile 0.34–0.37 window. `element_afforded`'s `cut_thrust` branch now compares cut
      against `geo['thrust']` instead of `geo['gap']` (the literal "wire geo[thrust]" ask; `gap` stays
      threaded separately for the armour-gap math) — a narrow, fully re-validated, zero-regression swap.
    - **JD-4 (pommel/Mordhau percussion) — RESOLVED.** Researched HEMA sourcing (Wikipedia "Mordhau
      (weaponry)"; Malevus "Mordhau: The Murder Stroke Technique") — a documented half-sword technique: both
      hands move onto the blade, guard+pommel project out as an improvised mace, used specifically when
      cuts/thrusts fail against rigid armour, explicitly "far less injurious" than a dedicated mace/warhammer.
      New `weapon_physics.hilt_assembly_mass(w)` + `reversed_grip_percussion(w)` (bottom-up: reuses the
      EXISTING `percussion_element_authority` per-element form with the hilt assembly as striking mass and
      `grip_len` as the lever arm, gated to hands==2 bladed weapons) + an explicit `REVERSED_GRIP_EFFICIENCY
      =0.25` [FIAT, HEMA-grounded direction] discount — needed because `percussion_authority`'s own
      PERC_EXP=0.30 power-law was measured to be UNABLE to express "structurally weak" from input magnitude
      alone (every mass/lever combination tried saturates toward 5-7/8). Result: two-handed swords read
      1.4–1.8/8, clearly weak vs mace's 8.0/poleaxe's ~7.5. `percussion_authority`'s non-blunt self-gate now
      routes here instead of a hard 0.0.
    - **NOT wired into live mode-selection (both).** Tried wiring reversed_grip_percussion into
      `element_afforded` as a competing 'blunt' token; reverted after finding `select_mode`'s comparator
      (`core.coupling`) doesn't read percussion magnitude except vs mail/plate — `DELIVERY['blunt']=1.6` is a
      FIXED constant, so the weak option incorrectly WON selection against unarmoured targets (backwards from
      the sourcing). That's a genuine, separate `core.coupling` gap, not routed around. Also reverted the
      independent cut/point secondary checks (the other half of "graded mode affordance") — they turn 7
      roster armour-tier "changers" into 27 (e.g. bear_spear newly prefers an incidental cut over its own
      point, breaking `test_thrust_protection_grip_invariant`) — a full roster re-validation, not attempted.
      `MODE_EDGE_MIN`/`MODE_TIP_MIN`/`MODE_PERC_MIN` stay defined in systems.py for whoever picks up both
      follow-ons (the `core.coupling` fix + the roster-wide cut/point re-validation).
    - New `tests/valoria/test_combat_reversed_grip.py` (6 tests) exercises the grounded functions directly.
      Fixtures regenerated (`r3_identity_golden.json`, `golden_heft_percussion_snapshot.json` — percussion_
      authority/puncture_pressure now nonzero for every hands==2 bladed weapon, confirmed via diff, everything
      else unchanged). 202 passed / 8 failed (identical pre-existing set) / 1 xfailed; `valoria_local.py`
      clean; 0 ED-citation violations. See the ED-PC-0009 ledger entry for full detail + sourcing.
    - **U2 live wiring — RESOLVED 2026-07-08 as ED-PC-0011 (same day, follow-on session).** Fixed exactly the
      `core.coupling` gap named above: `_transmit`'s percussion-authority scaling extended to every material
      via a DUAL reference (mail/plate keeps `PERC_AUTH_REF=8.0` unchanged, preserving the pre-existing tested
      calibration; none/cloth uses a new `PERC_AUTH_REF_SOFT=6.5`, anchored on the weakest attested dedicated
      hammer-class weapon rather than mace's own peak — a first attempt using ONE reference for both material
      classes was caught by adversarial review silently flipping bec_de_corbin/lucerne_hammer's selected mode
      at the unarmoured tier, backwards from the HEMA framing). `reversed_grip_percussion` now safely competes
      in `select_mode` — the weak Mordhau option correctly loses to a weapon's own cut/thrust vs soft targets,
      wins only vs rigid armour. The re-enabled cut/point secondary checks were ALSO re-validated (not just the
      percussion path): a new `CUT_AUTH_REF=0.70` fix (anchored on the weakest attested native cutter,
      hook_sword) stops an incidental secondary 'cut' token from outscoring a weapon's own dedicated 'point'
      regardless of how weak the edge actually is — this is the fix for the SESSION'S ORIGINAL reported bug
      (rapier's incidental cut beating its own dedicated point at zero armour). Validated via a 13-agent
      agonist/antagonist adversarial Workflow (6 Sonnet producer/critic weapon-group pairs + 1 Opus synthesis)
      against HEMA/physics grounding across the full 53-weapon roster, per Jordan's explicit request for that
      methodology. `test_use_mode_selection_emerges_from_primitives`'s expected-changers list grows 7→17 (ten
      new weapons' secondary half-sword-thrust/incidental-edge judged historically defensible);
      `test_afforded_heads_emerge_from_phase_b2_mode_elements` updated for ji/kama_yari's genuine incidental
      'cut' token. **NEW residual, deliberately deferred rather than rushed (filed as ED-PC-0012):** the
      adversarial pass found a SECOND, structurally identical gap on 'point' — DELIVERY['point'] doesn't scale
      by thrust magnitude either, and core._transmit's puncture path is floor-locked (verified: scimitar/sabre/
      falchion/hook_sword's secondary point ALL score an identical coupling at 'light' armour regardless of
      0.16-0.40 geometry spread). Judged to matter concretely for the one-handed sabre-class roster (sabre/
      scimitar/falchion — FLAG, historically dedicated slashers with the weakest thrust geometry in the roster)
      but not the two-handed cutters (historically defensible regardless). A `THRUST_AUTH_REF` fix analogous to
      `CUT_AUTH_REF` is recommended but NOT implemented — it would also touch several of the newly-accepted
      two-handed cutters (tachi/nandao/glaive/podao all sit below the natural reference too) and needs its own
      roster-wide re-verification pass, not a third redesign-and-reverify cycle in the same session.
      `test_pure_cutters_have_no_gates` updated: greatsword removed (legitimately gained real capability),
      sabre kept and left deliberately failing, documenting ED-PC-0012 rather than silently patching around it
      — matching this suite's `test_gap_game_poleaxe_spikes_plate` convention. Full suite: 210 passed / 9 failed
      (8 pre-existing + this one new, fully-documented failure) / 1 xpassed (pre-existing, unrelated
      mass-battle test); all local gates clean; 0 ED-citation violations. T-P2 may start any time (post-U0),
      scope per JD-6; the F5 renderer recovery (JD-8) is confirmed closed on option (a) — the scratchpad script
      is genuinely gone — only a from-scratch rebuild at T-P2 remains live.

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

- 2026-07-08 — **JD-4 + JD-9 DETERMINED via grounded research, not deferred.** Jordan: *"please determine
  both by testing bottom-up emergent primitives and validating top-down against history and hema and
  physics."* Directed resolving both ED-PC-0008-surfaced forks directly rather than waiting for a separate
  ruling — executed as ED-PC-0009 (see Pending above for the full record). JD-9 (thrust_factor floor)
  resolved cleanly and fully wired. JD-4 (Mordhau percussion) resolved at the formula level
  (`reversed_grip_percussion`, HEMA-sourced + physically grounded) but explicitly NOT wired into live mode-
  selection — a real `core.coupling` architectural gap (DELIVERY constants don't scale with percussion
  magnitude except vs mail/plate) made a naive wiring backwards (weak options winning vs unarmoured targets),
  so that integration is left as documented follow-on work rather than forced through.
- 2026-07-08 — **JD-1 RULED + executed: PoB target bands = the plan's own arms-scholarship ranges.** Jordan:
  *"accept plan bands"* (offered rapier 3–11cm / greatsword 8–20cm / 1H 6–14cm / poleaxe 20–55cm forward /
  staff ~0). Executed as U1, ED-PC-0010 — see Pending above for the full mass-redistribution + finding record.
  Unblocks the rest of the U-series toward M1's juncture 4 (one legible fight).
- 2026-07-08 — **ED-PC-0005 RULED + executed: wounds never −1D, always a fractional Ob.** Jordan:
  *"never −1D, always increase fractional Ob."* Wounds NEVER cut the pool −1D; each wound ALWAYS adds a
  fractional Ob. ED-1041's bilateral wound-Ob channel (+0.15 Ob attacking / +0.25 defending per wound)
  fully supersedes the −1D-to-Pools rule, **reversing PP-716's −1D unification.** Scope (AskUserQuestion) =
  **"Combat now, flag rest."** COMBAT executed fully: `derived_stats_v30 §4.1` row + universality paragraph
  rewritten (struck PP-716, SUPERSEDED marker); `combat_v30 §7/§10` + `combat_design_v1` rewritten;
  `WOUND_POOL_PENALTY` + the dead `pool_penalty()` **deleted** from `combatant.py` (felled gate keys on
  Health depletion, unaffected); `contest_legacy_stub` −1*wounds term removed. NON-COMBAT flagged not
  valued: −1D stripped from Thread/`threadwork_v30`, fieldwork/`fieldwork_v30 §2.2`, mass-battle Command/
  `params/mass_combat` ED-167 (+ `params/core`, `params/fieldwork` mirrors) → *"fractional Ob per wound,
  value ED-PC-0006"* — **no invented numbers.** PP-716 superseded in `supersession_register.yaml`;
  ED-PC-0005 → resolved (`needs_jordan: false`); **ED-PC-0006 filed (`open`)** for the non-combat
  calibration. 387 sim / 90 combat+gate tests green; goldens unmoved.
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

- **R2 (closing-distance/facing/grip/contact redesign) — I0→I8 COMPLETE (2026-07-03), PR #72, awaiting
  review/merge.** Implemented the full ratified plan
  (`designs/audit/2026-07-02-scene-combat-closing-distance-redesign/plan_r1_RATIFIED.md`) per its own
  per-increment discipline. All 9 Jordan-decisions (JD-1..JD-9) taken at the plan's own stated default.
  I8's capstone measurement + findings record:
  `designs/audit/2026-07-02-scene-combat-closing-distance-redesign/i8_capstone_audit.md` — **the one open
  finding**: the plan's ~55-75%/~30-45% reach-class/dagger CONTESTED-balance target is **not yet met**
  (reach-class weapons run 75-93% vs arming; not inverted, but above the band), traced to the same
  pre-existing Phase-B mass-model calibration debt already carried by the 3 accepted `[PHASE-C FLAG]` reds
  — explicitly out of R2's scope, deferred to Phase C's engine-scale re-tune. **Next action, if a Phase C
  recalibration effort starts:** read the capstone audit doc's item 1 table first.
- **ED-PC-0006 (`open`) — non-combat wound fractional-Ob calibration, follow-on to the ED-PC-0005 ruling.**
  Direction is ruled (wounds add a fractional Ob, never −1D); only the per-pool VALUES remain. Sites now
  reading *"fractional Ob per wound, value ED-PC-0006"* awaiting a number: Thread ops (`threadwork_v30`,
  `combat_v30 §10`, `params/fieldwork`), physical fieldwork (`fieldwork_v30 §2.2`, `params/fieldwork`),
  mass-battle Command (`params/mass_combat` ED-167). ACTION: sim-calibrate against the combat anchor
  (ED-1041 +0.15/+0.25), reconcile the pre-ruling "+1 Ob to Leap Thread ops" datum, propagate + land a
  verified PR (merge-ratifies). Also reconcile the two downstream narrative citations of the old −1D seed
  (`arcs/simulated/arcs_46_55.md` + `arcs_46_55_resolved.md`, PP-232 framing). No invented numbers.
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
  modules) is an **IN**-lane item — see `registers/handoffs/HANDOFF_IN.md`.
