# HANDOFF_PC — CLOSED WORK

**Lane:** `PC` — personal combat. **Split out of `HANDOFF_PC.md` on 2026-09-13 (`ED-IN-0221`),
on Jordan's instruction:** *"why don't you just hive off all closed IN work into its own document"* …
*"tbh it's applicable to all handoffs"*.

## What this file is, and what it is NOT

**It is the closed narrative of this lane, moved VERBATIM and in original order.** Nothing was
rewritten, summarised or deleted — the split is proved lossless: the line multiset of this file
plus `HANDOFF_PC.md` equals the original file's, exactly.

**It is NOT a continuity surface. Do not orient from it and do not add to it.** New work goes in
`HANDOFF_PC.md`; this file only ever receives units that file has finished with.

## The predicate that moved a unit here, stated so you can re-run it

A unit moved **only if it carried none of** `needs_jordan` · `[OPEN]`/`STILL OPEN` ·
`HELD`/`SUSPENDED`/`PARKED`/`DEFERRED`/`⏸` · `BLOCKED` · `TODO` · `awaits`/`awaiting`.

⚠ **THE CUT IS AT THE FINEST GRANULARITY THE DOCUMENT ITSELF LABELS, and that is the whole reason
this was safe to do mechanically.** Section-level disposition markers in this corpus are known to
lie — a prior attempt (step `6c`) was refused for exactly that reason: *"12 of 17 sections marked
`[DONE]`/`[RULED]`/`EXECUTED` carry open, held or `needs_jordan` items inside them."* That finding
is about SECTION headings. The `Pending`, `Decisions` and `Next actions` logs label every **entry**
(`[OPEN]`, `[LANDED]`, `[DONE]`, `✅`), so those three split per entry and the rest per section.
No marker was trusted: the predicate reads the unit's **body**, never its title.

⚠ **`do not` / `never` was deliberately NOT used as a signal.** Sampled across this corpus it is
~75% narrative (*"a Date with no `due_at` is never due"*), and the genuine standing orders are
meaningless without the referent the surrounding paragraph supplies — extracting them as a list
would reproduce the `evacuate` failure `CLAUDE.md` §4 records. Units carrying imperative language
are instead **flagged on the index in `HANDOFF_PC.md`**, so a standing order is one file-open
away rather than buried.

---

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

- **ED-1050 (combat parity oracle) — RESOLVED 2026-06-30, residual open.** ADEF_THRESHOLD monotonicity
  fixed (config.py + combat_config.gd re-exported, byte-identical, re-verified 2026-07-02 in the D1-D5
  docket adjudication, ED-IN-0002). Residual: re-export RESIST/GAP_EXPOSURE/gap-game logic to
  `weapon_resource.gd`/`strike_module.gd`; Key-log parity stays known-red until done (tracked as
  `decision_queue.md` item 5).

- **ED-1051 residual affecting this lane:** `engine_clock`'s doc:null grade now has a candidate home doc
  (`propagation_spec_v1.md`, ED-1093) but ED-1051 itself (module-contract closure priorities across all 27
  modules) is an **IN**-lane item — see `registers/handoffs/HANDOFF_IN.md`.

---

## 2026-08-27 — the 40% covert-plate-killer ceiling is ABOLISHED (ED-PC-0057)

> ⚠ **Filed as ED-PC-0041 and renumbered to ED-PC-0057 the same day.** ED-PC-0041 was already
> allocated on 2026-07-29 (the E0 batch), so this row was a duplicate id for the length of one
> merge. `next_free` for PC read **57** and I filed 0041 — CLAUDE.md §4 says read `next_free`
> and allocate THAT, never a number you reasoned to. Caught by a post-merge audit of the
> ledgers against `id_reservations.yaml`, not by a gate: **nothing in CI cross-checks a lane's
> allocated ids against its pointer**, which is a real gap and is recorded in `HANDOFF_IN.md`.

Jordan, verbatim: *"dude guandao not being able to hit 47.5% on its own merits is fucked up. stop
arbitrary fiat capping."* Assertion (C) of
`test_plate_participation_tracks_armour_defeat_capability` is deleted. **No replacement threshold
was invented** — a differently-numbered cap is the same fiat, and the ruling is about the class:
an assertion that bounds how often an outcome may occur, rather than measuring the mechanism that
produces it, is not a guard.

**It also overrode a sequencing objection I had raised** (that abolishing the ceiling before
combat's ladder migrates "deletes a guard and gains nothing"). Recorded rather than dropped: the
objection was about sequencing convenience; the ruling is about whether the thing should exist.

**What it costs, stated plainly.** The ceiling was the only assertion that would trip if
penetration decoupled from armour-defeat capability again (the ED-PC-0038 class). Nothing replaces
that job. What survives points the other way — (A) FORWARD and the `strong` class check catch
plate going *mute* for weapons that defeat it. A recurrence of the decoupling will now surface as
a balance observation, not a red test. The replacement is a `print`, and "report-only" is weaker
than it sounds: pytest captures stdout of a passing test, so it shows only under `-s`.

### THE NEXT PC ITEM, and it is the big one

**Derive Ob from the DEFENDER.** Jordan, 2026-08-15: *"DECISIVE_OB for combat is stupid as hell
and is dead because Ob should be determined by your opponent more than anything"* — the obstacle
is *"their corresponding score/2 plus whatever specific modifiers exist for them in that
instance"*. The sequence is settled and is the opposite of the obvious one: **derive Ob first,
THEN combat's bands migrate to the owner's ladder.** Migrating the bands against the fixed
`DECISIVE_OB` first is wasted work — `core.py`'s own docstring predicted it.

That derivation is genuine new mechanism, not a re-siting, and it is what makes guandao reach
47.5% *on its own merits*. It is the last declared HOLD in
`tests/valoria/test_degree_ladder_single_owner.py`. The ceiling that stood in its way is gone.

### 2026-09-09 — carried out of the CLAUDE.md rewrite (ED-IN-0179, PR #384)

- **Combat Pool is defined three different ways** and nothing reconciles them. The definitions live in
  the prose param head, `references/module_contracts.yaml`, and the A18 census; a third source that
  once held a fourth definition has been retired, but the collision survives its retirement. This was
  a live open item in the old CLAUDE.md §5 and was evicted as a state fact, not a rule — §0.05 puts it
  here rather than in Layer 0. **Do not bind Godot resource fields to these keys while it stands.**
  Resolving it is a PC-lane call: pick the definition, change the code, and let the prose follow.
  Sources: `references/module_contracts.yaml`; `systems/combat/reference/`'s param head; the A18
  census. Established by PP-247; the retired fourth source was `references/values_master.yaml`.
  Evicted from CLAUDE.md §5 by the 2026-09-09 rewrite as a state fact rather than a rule.
