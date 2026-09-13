# HANDOFF_MB — CLOSED WORK

**Lane:** `MB` — mass battle. **Split out of `HANDOFF_MB.md` on 2026-09-13 (`ED-IN-0221`),
on Jordan's instruction:** *"why don't you just hive off all closed IN work into its own document"* …
*"tbh it's applicable to all handoffs"*.

## What this file is, and what it is NOT

**It is the closed narrative of this lane, moved VERBATIM and in original order.** Nothing was
rewritten, summarised or deleted — the split is proved lossless: the line multiset of this file
plus `HANDOFF_MB.md` equals the original file's, exactly.

**It is NOT a continuity surface. Do not orient from it and do not add to it.** New work goes in
`HANDOFF_MB.md`; this file only ever receives units that file has finished with.

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
are instead **flagged on the index in `HANDOFF_MB.md`**, so a standing order is one file-open
away rather than buried.

---

## Pending

(none beyond the items tracked under Next actions below.)

## Decisions

(none logged yet under this lane split — prior mass-battle decisions predate the lane-tagged
namespace and are folded into Next actions below, which carries the full narrative.)

- **⛔ `main` IS CI-RED (16 failures) as of `94bb902`. READ ED-MB-0061 BEFORE ANY MB WORK.**
  The flags-ON ruling (every mechanic defaults ON) landed with PR #271 and moved every golden while
  the pin vector in `tools/ci_golden_modes_check.py` still certifies the OLD configuration. **No lane
  can currently distinguish a new regression from the known 16.** Full accounting + the corrected
  plan: `audit/2026-07-30-mb-session-retrospective/00_lessons.md` (nine new guardrails G13–G21,
  Track F, the authoritative geometry spec, and a new Phase 0 that re-orders both workplans).
  - **Do NOT re-base the goldens first.** Doing so bakes nine defects into the definition of correct.
    Order is: bisect each failure → fix F1–F8 → Jordan rules the golden **mode matrix** →
    re-base once as the single global golden-moving PR → G11 resumes → existing B1a/D1 path.
  - **Proven so far:** F3/F4 (body interpenetration) are caused by **`PC_FACING_MODEL` alone**;
    `PC_CELL_EXCLUSION` is exonerated by bisect. Every other failure still needs its own bisect
    before being called "pre-existing".
  - **✅ F2 CLOSED 2026-08-01 (ED-MB-0063) — it was a CONFOUNDED TEST, not an engine regression,
    and the flag bisect that "explains" it is wrong.** A full single-flag sweep fingers
    `PC_FRACTIONAL_POOL` as the only flag whose OFF state restores the pass. **That is a mask, not a
    cause.** The real chain, measured: the two arms flipped the defender's `advance_dir`, which
    orients the whole *subunit*, so they contacted **different cells of B** — rank `(0,*)` vs
    `(2,*)` in the original frame — moving B's own pool 3.6 → 1.333 **via support depth**
    (`core/exchange.py::_pair_engaged_troops` credits deeper cells at `SUPPORT_WEIGHTS`; rank 0 has
    two ranks behind it, rank 2 has none: `(5+5·1.0+5·0.7)/15 = 0.9` vs `5/15 = 1/3`, exactly 3.6 vs
    1.333 at base pool 4). `compute_degree` is **relative**, so B's smaller pool rolling better
    (net 2 vs 1) downgraded A's *identical* net of 1.0 from `Success` to `Partial`; `Partial`
    (damage 1) − the universal `dr=1` = **0.0**. Flooring just happens to keep B under A at that
    seed. Fixed by holding the body fixed and rotating only `cell_facing_vec`. **No golden
    re-recorded.** This **implements** `audit/2026-07-30-mb-session-retrospective/00_lessons.md`'s
    existing classification of F2 as a test-premise defect — it does not discover it.
  - **⚠ THREE CORRECTIONS from the independent critic pass, kept because the errors instruct
    (full detail in the ED-MB-0063 correction row):** the first write-up blamed "different cells
    carry different troops" — **false**, `distribution` is uniform; it recorded support-stack loss as
    *refuted* by measuring `support_engage_frac`, which is **never called** here (`POOL_VARIANT ==
    "C-ii"` guards it out) — so the right concept was discarded on the wrong function; and it claimed
    "mutation-verified 3/3" when `OCTAGON_DMG_MULT["YELLOW"]` has **no readers at all** (flank is
    interpolated), so that mutant kills nothing. Real score **2/3**. All three passed my own
    adversarial pass and were caught only by a structurally independent reader.
  - **The falsifier that replaced them:** `test_arc_ratio_is_invariant_to_the_fractional_pool_flag`
    parametrizes `PC_FRACTIONAL_POOL` over both settings — the property that was *false* before, and
    the flag-dependence that **defined** F2. Reintroducing the confound fails `[1]` and passes `[0]`,
    reproducing F2's exact signature. "7 of 12 seeds" was near-vacuous by comparison: with the body
    fixed, both arms share one RNG stream and the ratio is arithmetically forced.
  - **Recorded, NOT fixed (all pre-existing):** `test_rear_penalty_persists_across_reaction_window`
    **does not traverse the window it names** — the reaction counter is consecutive-tick in a
    per-subunit map and each call builds a fresh `Subunit`, so `_cnt` never exceeds 1 against
    `FACING_REACTION_TICKS = 2`; an engine that *did* wheel would still pass. Fix by ticking a
    persistent subunit (the template is `test_visible_flank_refuses_after_delay`, same file).
    `test_front_takes_no_arc_penalty` still uses the confounded pairing, justified by an
    uncontrolled structural claim. And the new isolation is **scenario-dependent**: it holds only
    while this fixture has no brace, no momentum differential, one subunit per side.
  - **⚠ Bisect discipline, learned here:** a single-flag bisect answers "what changes this result",
    which is **not** "what causes it". F1/F3–F8 bisect results should each be re-checked against the
    mechanism before being written down as causes — F3/F4's `PC_FACING_MODEL` attribution above has
    not had that second step.
  - **Jordan's geometry spec (§4.5) is unimplemented:** the octagon is POINT-forward (a vertex, not a
    face, touches the subunit facing line) and **the subunit has a PERIMETER that is the surface of
    battle**. No perimeter object exists in the tree.

- **▶ SESSION 2026-07-29c (ED-MB-0058/0059/0060) — SPATIAL INTEGRITY + the PC_CELL_MORALE confound.**
  Three landings, and one of them is a retraction of this session's own earlier numbers.
  - **ED-MB-0058 — PC_CELL_MORALE was never inert; it was shadowed.** `between_turn_recovery` routed
    own-morale subunits through `set_morale`, the ABSOLUTE writer, which flattens every cell to the
    unit mean — so per-cell divergence was erased once per turn, every turn. Now `pull_morale`.
    This closes ED-MB-0042's named blocker. `cell_cm` golden b42343db → d11cb4fb; the other four
    modes byte-identical, which is the control that proves the fix stayed in its own scope.
  - **ED-MB-0059 — same-side cell exclusion, `PC_CELL_EXCLUSION` default ON.** Deep inter-subunit
    overlap **−48.6%**, cross-side **−74.4%**. It first shipped accepting `s == 0.0` and **deadlocked
    the engine** — the formation lattice is permanently tangent (pitch 1.0, bodies 1.0×1.0), so 46.9%
    of same-side solves capped their cell to zero motion; halted cells fell 20,356→3,300 and tick
    count rose 8.05×. That tick inflation *was* the "8.2× slowdown", which is why a broad phase built
    to fix the cost bought nothing. Fixed with `s > 0`; runtime now 1.41× baseline; broad phase
    removed. Goldens unit_field 6f594233 → 0194efcc, cell_field 2a9214eb → da6d685e, with an
    attribution control (flag OFF reproduces both old goldens byte-for-byte).
  - **ED-MB-0060 — RETRACTION.** Both previously-reported co-location figures were wrong. "17.31%"
    was rounded-square, not body-box. "17.31% → 0.35%" was measured **on the deadlocked arm** — cells
    weren't overlapping because they weren't moving. Textbook §0.1 confound, banked because it was
    favourable. `measure_colocation.py` is now a tracked probe reporting depth-thresholded
    `obb_overlap`.
  - **Cost, measured with a control:** the pass suppresses contact. Mean end-state hp over all 20
    historical rows 0.8684 → 0.8939 — total attrition **−19%**, on a casualty model already far too
    low. Shipped ON per the standing "gate models ON" directive, cost recorded not buried.

  **Open, in priority order, all newly specific:**
  1. **The solve is enemy-gated.** `toi_deferred = FIELD_MOVEMENT and enemy_cells_float` — so
     same-side exclusion inherits a cross-side precondition it has no reason to, and formations with
     no enemy supplied interpenetrate freely. Ungating is a small change with a broad blast radius
     (golden re-record); it is the highest-value next move on this axis.
  2. **Nothing separates already-overlapped bodies.** The `s > 0` rule prevents new interpenetration
     but by construction never undoes existing overlap. `resolve_internal_collisions` (ED-MB-0057,
     still dead) is the only primitive ever built for that and is intra-subunit + grid-era; an
     inter-subunit sibling does not exist.
  3. **Same-subunit deep overlap is unmoved** (43,068 → 44,531). Formations still shear — H3's Roman
     mass fragments into ribbons by t=8 — though H5's massed blocks now hold as distinct rectangles
     through t=24, which is a real visible gain over the pre-fix render.
  4. Attrition at historical scale remains far too low; the exclusion pass makes it 19% lower. Feeds
     D1 directly.

- **▶ SESSION 2026-07-29b (PR #271, ED-MB-0047..0051) — E4+I4, A3, A5a, A6a→A6b, A2 EXECUTED.**
  Five commits, five guards (all mutation-verified: 3/3, 3/3, 3 mutants, identifiability, 5/5).
  **The headline: the attrition-law instrument now measures what it claims, and it says melee fits
  `p=3.20` (cv 0.00245, identifiable) against a ≤1.4 linear bar** — super-square, an ENGINE finding,
  and an independent re-derivation of ED-MB-0007's historical p≈3.2 on clean untruncated data. The
  `melee p=2.50` two audits quoted was literally `FIT_P_HI=2.51`. Volley confirms the square law
  exactly (`p=2.00`). Three reasons the harness was broken, **one not in the plan**: the morale pin
  cannot disable a *casualty-fraction* break-point; the volley scenario fired nothing (0 engagements,
  0.00 loss — the `inf` was a 0/0 guard); and `TRAJ_FLOOR` sat BELOW the engine's own annihilation
  threshold, so it was unreachable and every trajectory ended in annihilation-rout.
  **A2's no-movement prediction FAILED — and the prediction was the wrong thing.** Decomposed before
  re-recording: the degree epsilon is the sole mover, the sigma snap is behaviour-neutral. Flip
  census: unit 0/17,312 · **cell 38/31,958 (0.119%)** · unit_field 0/18,152 · **cell_field 14/20,412
  (0.069%)**, every flip `Partial → Success` at 1–4 ulp from a *continuous* `ob`. **S1.2 is NOT
  incidence-zero** — the audit's "0 in 209,778" and its N=3,120 replication were both `PER_CELL=0`.
  The two per-cell goldens were re-recorded deliberately (`cell` dc3d3414…→f58a9cb4…, `cell_field`
  3a0952b3…→13bd02dd…); both `PER_CELL=0` goldens byte-exact throughout.
  **A fourth and fifth unresolvable citation found by hand:** `mass_battle_v30.md §deployment —
  anchor columns` (no such section; values not derivable either — measured centres 12/12/11/11 admit
  no rule giving 11/10/9/8), still live at its origin in `gauge_mb.py:60,64-66`; and the ENTIRE
  conserved-quantity block's `mb_lanchester_design.md §4` tags (that section names no protocol, no
  grid, no bars — "1.4"/"1.6" do not occur in it). Both re-labelled `[JUSTIFIED:]` in the files this
  session touched; the `gauge_mb.py` origin is filed, not chased.
  **⚠ NEEDS JORDAN, called out in the PR body rather than buried:** (1) **fork #2 is now UNBLOCKED**
  — A6a landing was its stated precondition; (2) the `p=3.20` result itself; (3) `.github/workflows/`
  edited (report-only `lanchester-signature` job) — CODEOWNERS; (4) the F7 convention question
  (should engine-mechanics changes allocate `PP-NNN`? — filing retroactive PPs to move a graph metric
  would be fabrication, so it went to the docket, not the register).
  **PROCESS FINDING worth carrying:** the first A2 mutation run was corrupted by stale `__pycache__`
  (CPython invalidates by `(mtime, size)`, so a same-size edit inside one mtime second is served from
  cache) — it silently mis-scored 2 of 5 mutants. **Run mutation matrices under `python -B` with
  caches cleared.** The A2 and I4 matrices were re-run that way.
  **NEXT, in order — the chain is unchanged and C1 is the head:**
  **C1** (per-phase casualty attribution; also the second behaviour-preservation instrument) →
  **§4a** (record the 5th digest mode at `PC_CELL_MORALE=1`; mode-key extension MANDATORY — `bat.py`'s
  key reads only `PER_CELL`/`FIELD_MOVEMENT`, so a 5th golden without it would silently check the
  wrong baseline) → **rekey_cells** (the cheap standalone fix for the live `cell_facing_vec` loss;
  ~30 lines, no B1a risk) → **B1a/B1b** → **D1** with its pre-registration and Fable referee.
  A5b, E5/E6/E7, D2–D6 and the §7 forks are untouched.

- **A1b EXECUTED (2026-07-29, MB session — this PR).** The shipped configuration's regression
  oracle now exists: CI job `field-goldens` runs `bat.py --check` in both `FIELD_MOVEMENT=1`
  modes via `tools/ci_field_golden_check.py` — the **single owner** of the full digest-relevant
  pin vector (52 pins from the A1b inventory: `_PINNED_OFF` carry-over + Groups A/B/C; env-name
  keyed, note `SIGMA_HEAD` not `SIGMA_HEAD_ENABLED`). Drift guard:
  `tests/valoria/test_field_golden_pins.py` (pins ≡ source `environ.get` defaults,
  mutation-verified; a default flip without a deliberate pin+golden update fails it loudly).
  `PYTHONHASHSEED='0'` added to `_PINNED_OFF` too (A1a critic residual; digests shown
  hash-order-independent empirically, pinned anyway). Registered in `ci_checks_registry.yaml`
  (blocking cross-check c). **⚠ Jordan CODEOWNERS review required** (`.github/workflows/` edit).
  Mutation artifact + the `PC_WHEEL=0` probe result (the A1a critic's open decomposition
  question) in the PR body. **Next: Wave-3 parallel batch** (A4-sweep, E8, E4+I4 once A1a's
  merge gate is open — it is, #260 merged; A3/A5a/A6a once this job is green on main; A2 last,
  alone in the golden slot).

- **A1a EXECUTED (2026-07-29, merged as #260).** Both field goldens bisected and
  re-recorded after 5 days red. Per-mechanism delta (base `4b80ad5` = #232's all-four recording;
  full matrix in the PR): **exactly two movers** — (1) PR #235 `fbc93b0`'s change set moved
  `unit_field` `d44f211f…→27aa9ee0…` and `cell_field` `a1a97940…→3a5807fb…` at fixed
  `PC_STOCHASTIC_ROUT=0` (⚠ commit-level attribution: NOT decomposed to one mechanism on the
  field arm — `PC_WHEEL`'s node-path port is an unmeasured second candidate beside impulse
  momentum; the grid inertness arguments are `PC_NODE_COHESION=0`-conditioned, per the Opus
  critic pass); (2) PR #236 `584c683`'s
  `PC_STOCHASTIC_ROUT` default flip 0→1 moved them to the new goldens (`6f594233…`/`3a0952b3…`)
  as a **pure config effect** — #236's code alone is byte-identical at rout=0, verifying its
  set_morale-sweep claim on the field path. #233/#234 verified byte-exact on both field modes.
  No third mechanism: `584c683`@rout=1 reproduces HEAD's observed digests exactly. Recorded on
  Linux/Python 3.11.15 (grid modes reproduce reference digests on this box; reference-env
  confirmation = A1b's first CI run). **Next: A1b** (CI job, full pin vector from the 47-flag
  inventory; `.github/workflows/` is Jordan-CODEOWNERS). Then the Wave-3 parallel batch.

- **PLAN v2 EXECUTION UNDERWAY (2026-07-29, MB session).** Wave 0: ED block **0046–0060 drawn
  from IN's Wave-0 pre-allocation (PR #256)** — the MB session's own parallel block PR (#255)
  was closed per its declared race-handling the moment #256 landed first; `id_reservations.yaml`
  is now frozen for the run. Premise re-verified at HEAD `81948c1` — grid modes green ×2 locally
  (reference digests reproduce on this box), both field modes deterministically red ×2 (identical
  wrong digests both runs; no non-determinism) — **A1a proceeds**. E1 executed in this PR
  (`scene_outcome.battle_concluded` emit row deleted; ED-MB-0010 resolved by merge-ratification,
  ED-1094; artifact regeneration deferred to IN Wave 5 per §12 I5). A1a bisect frame established:
  base `4b80ad5` (PR #232, last all-four-mode re-record), candidates `47f9cac` (#233) →
  `5f1afc7` (#234) → `fbc93b0` (#235, impulse momentum + unconditional path fixes, re-recorded
  grid only) → `584c683` (#236, PC_STOCHASTIC_ROUT default flip, re-recorded grid only).

- **E8 EXECUTED (2026-07-29, MB session — this PR): the record corrected.** Three refuted claims
  retired, with per-claim scope discipline (a critic pass caught and fixed a timeline overreach —
  the A6a rout-pin defect applies only to post-2026-07-25 runs; ED-MB-0006/0007's p≈2.50/p≈3.2
  predate the mechanism and rate as leads under their own caveats): (1) ED-MB-0041's
  armour-inversion claim — ledger `correction` field, figures tagged agent-reported per G12,
  direction independently backed by `test_volley_armour_direction.py`; (2) the current-harness
  `p=2.50` / "true exponent ≥2.5" reading — STRUCK in the SEV-1 bullet, the findings register, the
  ledger (ED-MB-0041 + ED-MB-0015), and bracketed at the ED-MB-0006/0007/0013 historical mentions;
  (3) the ED-MB-0038 APEX-forward interaction hypothesis — bracket-superseded at the NEXT item
  (dead code path in these harnesses; verified `engine.py:414-419` + both harness call sites).
  ⚠ The frozen `id_reservations.yaml` MB comment still carries the armour claim verbatim — correct
  at the next unfreeze (logged in the ledger correction).

- **A4-SWEEP EXECUTED (2026-07-29, MB session — this PR).** The test-commensurability repairs
  (Jordan's vet-all-tests directive + plan A4): A4a counted (floor 6 of measured 9, reorder-robust);
  A4b's fixture genuinely on the own-morale path via `build_army` (was two copies of the inheriting
  branch); S6 pattern fixed with ONE owner — `tests/valoria/_conservation.py` — routing all four I1
  sites, the routed/broken skip REMOVED (structurally safe: `run_battle` breaks on rout,
  `orchestration.py:1695`; critic-verified) with a PER_CELL precondition in the owner (the one real
  false-red path); S12 counters added (measured floors); S7's inverted docstrings corrected
  (stochastic rout is the ONLY shipped break-point, not a retirement candidate). Producer's G1
  correction banked: the rout-skip was one tuning change from vacuous, NOT currently vacuous
  (Line-vs-Line routs 0/120 at shipped defaults). **NEW: ED-MB-0046 filed** — `between_turn_recovery`
  flattens per-cell morale on the own-morale path (`orchestration.py:2098-2103`; inert at shipped
  defaults, a LIVE CONFOUND for D1 arm 1; fix gated behind §4a's fifth digest). Minor unledgered
  residues in the PR body: hp-clamp/spill edge (recorded in `_conservation.py`), octagon reaction
  test floor candidate.

- **▶ START HERE — THE MASS BATTLE PLAN, v2 (2026-07-26):**
  **v2 exists because v1 was substantially wrong.** Four Fable-5 critics attacked it and instrumented
  measurement refuted its headline: **three of five severity-1 findings are code-true but
  INCIDENCE-ZERO** (0 degree flips in 209,778 calls; 0 truncations in 102,260; the cell desync latent
  behind an off flag). What IS wrong: **both shipped-mode goldens are RED** (stale since #235/#236,
  undetected across both audits) and **casualty realism is 2/20** with loser means 29.1–79.2%.
  v2 folds every correction into the tasks and promotes all eleven failures into **§1 GUARDRAILS** —
  including one of my own guards that could not fail, and a `CellTable` rationale that benchmarking
  showed backwards. **Critical path: A1a → A1b → §4a → B1a → B1c → D1.** First PR: **A1a** (the
  goldens are red now). **⚠ Fork #5 is REWORDED** — the v1 wording generalised a gated-off feature to
  the whole substrate and must not go to Jordan as written.
  _(superseded v1 pointer follows)_

- **THE MASS BATTLE PLAN v1 (superseded):**
  **`audit/2026-07-26-mass-battle-fable-audit/03_execution_plan.md`**
  Self-contained; a fresh session needs nothing else. Consolidates BOTH audits from that session
  (ED-MB-0043 vector, ED-MB-0045 Fable-5 six-dimension) plus the four pre-existing open MB items into
  one ordered plan, with per-task files, verification commands, required guards, and whether each
  changes battle outcomes.

  **Three governing facts, all verified:** (1) **battles are being distorted right now** — a float
  compare with no epsilon guard turns 3 damage into 0 at the universal `dr=1`, a bare `break` drops
  engagement groups past the 5th unlogged, and `check_drift` re-keys 1 of 10 cell maps; (2) **the
  engine cannot explain a battle** — every diagnosis in both audits needed a bespoke probe, and there
  are now 23; (3) **the instruments are not watching** — the Lanchester harness is red and unwired
  (`melee p=2.50` vs a `≤1.4` bar) and the shipped configuration has no regression oracle at all.
  Fact 3 is *why* two default flips were made on confounded measurements and retracted.

  **Five tracks.** **A** trustworthy instrument (gates everything) · **B** ownership — `CellTable`,
  ten maps → one owner with a loud invariant · **C** observability, the battle explains itself (new,
  no prior tracking item) · **D** the system itself — DG-6, cell phases 3–4, envelopment, R3, the
  inverted casualty shape · **E** canon/params/contract/registries.

  **⚠ CRITICAL PATH CORRECTED (§11.1) to `A1a → A1 → B1a/b/c → D1`** — the earlier `A1 → A5 → D1`
  was a regression I introduced against `02_remediation_plan.md`'s correct ordering. **AND §11–§13
  carry an adversarial review that overturns much of the plan's framing: the shipped-mode goldens are
  ALREADY RED (measured), and three of five severity-1 findings are code-true but INCIDENCE-ZERO
  (0 degree flips in 209,778 calls; 0 truncations in 102,260). Read §11–§13 before executing anything.**
  Superseded text: **Critical path: A1 → A5 → D1** (wire the shipped goldens → finish the scalar sweep → re-measure
  DG-6's CV-vs-N with cell correlation ON). **First merged PR in an hour: E1** — delete the
  `scene_outcome.battle_concluded` emit row, one line, = ED-MB-0010 open since 2026-07-13, closes five
  downstream surfaces.

  **D1 is the plan's central bet, stated as a hypothesis with a falsifier:** DG-6's research names
  correlation as the only lever that breaks CLT self-averaging, then implements the simplest form — a
  shared per-battle shock costing gauge 6/20 → 4/20. But cell-morale lattice contagion already
  generates correlation *from a primitive*, and has never been measured against this problem.
  **Falsifier: if CV-vs-N still decays as O(1/√N) with `PC_CELL_MORALE=ON`, the recommendation is
  wrong and the shared shock is right.** That measurement does not exist yet.

  **Eight forks are held for Jordan (§7) — do not work around them.** Note §7.8: terrain, pursuit in
  the measured mode, the general as an entity, surrender, ammunition, weather would change battles
  more than all of tracks A–E combined, but they are design, not repair.

- **ED-MB-0045 REMEDIATION PLAN (2026-07-26): all MB surfaces.**
  `audit/2026-07-26-mass-battle-fable-audit/02_remediation_plan.md`. Scoped to the **13 mass-battle
  surfaces** (§1): live engine, stale twin, 24 CI tests, goldens, gauge, 4 harnesses, workbench,
  23 probes, 6 design docs, params, the module contract, 12 registries, research diagrams.

  **Framing (Jordan's correction, verbatim):** *"it may not change the next battle, but it sure as
  heck should. make identifying what's happening and preventing conflicts etc going forward."*
  The first draft filed this as hygiene; that was wrong. **Three mechanisms are silently changing
  battles today** — the un-guarded degree-boundary float compare (a 1-ulp error turns 3 damage into
  0 at the universal `dr=1`), the bare `MAX_SUB_PHASES` break (engagement groups past the 5th deal
  zero damage, unlogged), and `check_drift` re-keying 1 of 10 cell maps (morale immortality +
  phantom breaks the moment cell morale is on). Plus: the campaign resolves battles on the **stale**
  tree, so none of the last month's work reaches the game.

  **Two goals:** **G1 identify what's happening** — the engine cannot currently explain why a battle
  ended as it did, which is *why* two default flips were made on confounded measurements and
  retracted; **G2 prevent conflicts** — one owner per fact, one loudly-failing invariant per owner.

  **PHASES.** **A** trustworthy instrument (HARD GATE — A1 wires the shipped configuration's goldens
  into CI; they are checked by *nothing* today, so B has no safety net without it). **B** `CellTable`
  — struct-of-arrays with an owner and a `.check()` invariant, **not** a per-cell object (AoS is
  slower in a Monte-Carlo oracle and further from the `PackedFloat32Array` layout the port wants);
  supersedes ED-MB-0043's phase-3/4 ordering, because each of the six remaining directed fields
  otherwise repeats the ten-map tax. **C** collapse the 7 duplicate owners. **D** conflict-prevention
  guards (multi-owner scan, config-liveness, citation integrity, flag-pair coverage, golden-drift
  disclosure). **E** gauge integrity. **F** docs/params/contract/registries. **H** *observability* —
  per-phase casualty attribution, break decision log, mechanism attribution, invariant reporting,
  promote the workbench trace. **H is the new one and it has no prior tracking item:** every
  diagnosis in the last two audits required a bespoke probe, and there are now 23 of them. That cost
  IS the finding.

  **Critical path: A1 → B1 → B3.** **Cheapest real win: F4** — delete the
  `scene_outcome.battle_concluded` emit row (= ED-MB-0010, open 13 days), one line, closes five
  downstream surfaces.

  **Explicitly NOT in scope:** the ~26k LOC of other subsystems (unmeasured — the parallel-dict
  counts I gathered are NOT evidence of the same defect), the §9 forks, and the absent mechanisms
  (terrain, pursuit in the measured mode, the general as an entity, surrender, ammunition, weather)
  which would change battles more than everything in the plan combined — but are design, not repair.

- **ED-MB-0045 (2026-07-26): FABLE-5 SIX-DIMENSION READ-ONLY AUDIT.** Six independent Fable-5
  auditors with read-only tools (structural independence, §10); every promoted finding re-derived by
  the orchestrator. Register: `audit/2026-07-26-mass-battle-fable-audit/01_findings_register.md`.
  **Nothing in the engine was modified.**

  **⚠ THREE CORRECTIONS TO THIS HANDOFF, all verified — read before acting on the items below:**
  1. **ED-MB-0038/0039's side-asymmetry diagnosis names a DEAD CODE PATH.** The text blames "the
     enveloper's APEX-forward centre (`build_envelopment`, `start_row+APEX*advance_dir`) + wing
     placement vs the flat command line". `engine.py:414-419` applies `APEX` **only in the `else`
     branch — when the caller omits the centre's `starting_position`**. Both harnesses pass it
     explicitly (`gauge_mb.py:257`, `bat.py:70`), so **in H3/H10 and the whole bat.py battery the apex
     offset never executes.** Do not spend more effort on that hypothesis. The pathing auditor could
     not find a deterministic bias statically and says so; its two candidates are `min()` over a
     **set** (`orchestration.py:1744`, value-dependent iteration order) and banker's rounding at
     exactly `.5` (consistent with the measured start-row *parity* sensitivity). Falsifiers given:
     canonicalise to `min(sorted(...))` and re-run the mirror; sweep start rows preserving the exact
     mirror midpoint.
  2. **ED-MB-0043's "ship R3 without a ruling" was WRONG.** Removing the `hold` early-return does
     nothing on its own — `STANCE_SPEED_MOD['hold'] = -99` independently zeroes `step`, and all goal
     resolution sits behind `step > 0`. It is a **two-gate** change. `hold` is load-bearing for
     `build_envelopment`'s `freeze_wings` (documented as relying on it), `build_refused_flank`, and
     `STANCE_COMMITMENT`'s defensive-pool treatment. And `_kite_goal` does **not** generalise:
     `PC_KITE_STANDOFF=5` vs max melee reach 0.3 makes the band `[5, 0.3]` inverted. Lower-blast-radius
     alternative: change the **R3 scenario** (`stance='balanced'` + `kite`), not `hold` semantics.
  3. **ED-MB-0041's "armour causes MORE arrow casualties" is REFUTED as current** — measured
     0.115/0.061/0.035/0.015 at dr 0/1/2/3, strictly monotone decreasing. Retire the claim.
     Relatedly **ED-MB-0008 drops in priority**: neither contradictory DR table is what the code
     implements (the armour catalogue is explicitly unwired; the live engine uses a free scalar
     defaulting to 1 everywhere) — it is a docs contradiction with no current code consequence.

  **SEV-1, all verified by re-execution:**
  - **The engine's own Lanchester instrument is RED and NOTHING runs it.** `melee p=2.50` against a
    `≤1.4` linear bar — the scan-grid ceiling, so the true exponent is ≥2.5, *worse than the square law
    `core/attrition.py` says frontage-capping prevents*; `volley p=0.50` against `≥1.6`. Exits 1. Not
    in CI, not in pytest. **[STRUCK 2026-07-29, plan-v2 E8/A6a (G4):** the "true exponent ≥2.5,
    worse than the square law" inference is UNSUPPORTED — `p=2.50` is a grid-endpoint artifact of an
    unidentifiable fit on rout-truncated data (per plan-v2 A6a's diagnosis, agent-measured, G12: the
    `NO_ROUT_MORALE` pin does not disable `_stochastic_break` — verified against `core/state.py:34-48`,
    which keys on casualty fraction, never morale — with the reported 40/40 routed trajectories and
    monotone cv objective not yet orchestrator-replicated). **Scope of the strike: post-2026-07-25
    measurements only** — the rout mechanism landed 2026-07-23 (ED-MB-0031) and defaulted ON
    2026-07-25, so earlier-era exponents (ED-MB-0006's p≈2.50, ED-MB-0007's p≈3.2) are NOT
    invalidated by this defect; they carry their own era's caveats (wrong-PER_CELL setting; fit
    identifiability never verified) and rate as leads, not measurements. No current-harness exponent
    is derivable until A6a repairs the pin and the volley scenario. The harness being
    red-and-unwired stands; the NUMBER does not. The "NOT in CI" clause becomes stale when A1b
    (PR #261, in Jordan's CODEOWNERS review) merges its blocking field-goldens job.**] Two of its three PASSes are degenerate (volley passes on `cas_exchange=inf`;
    the melee 2:1 check demands ≥65% and measures **100%** while dg6 adopts ~70% as the historical
    target — **two incompatible validation targets for one quantity; one must be repudiated**).
  - **The 1-ulp degree defect is LIVE at the consumer.** `3 + σ(-1e-16) → Partial → 0 damage` at the
    universal `dr=1` default, vs `Success → 3`. The historical fix patched one *producer*; three others
    remain. `compute_degree` has no epsilon guard while the pool floor beside it does.
  - **`orchestration.py:1431` silently drops engagement groups past `MAX_SUB_PHASES`** — bare `break`,
    no log, zero damage that tick.
  - **`check_drift` re-keys `cell_troops` and NONE of the other nine per-cell maps** → post-drift
    morale immortality + phantom cell breaks. **A re-flip blocker not currently listed below.**
  - **The shipped default (`FIELD_MOVEMENT=1`) has no automated regression oracle** — CI pins it to 0
    and the test says the field goldens are "NOT checked here".

  **SEV-2 themes:** the verification apparatus reports green without looking (vacuous-capable octagon
  assertion; the write-sweep fixture mislabeled so the own-morale flatten branch has zero coverage; a
  docstring claiming CI coverage of a path CI pins off; `provenance.py` unconsumed with every line
  number stale; diagonal-only flag coverage with `reform_check`, a canon-required mechanic,
  permanently dark). And **nothing has one owner** — pool formula ×2 (self-declared "Mirrors EXACTLY",
  no test), arc systems ×2, stamina ×3, morale dialects ×3, damage laws ×2, ten per-cell maps with no
  key-set invariant.

  **On "the cell needs to be a class":** semantically yes, but a per-cell **object** is
  array-of-structs — slower in a Monte-Carlo oracle and further from the `PackedFloat32Array` layout
  the Godot port wants. What is missing is an **owner and an invariant**: one `CellTable` owning all
  ten maps, sole writer, enforcing key-set agreement and troop conservation. **This supersedes the
  ED-MB-0043 plan's ordering — give cell state an owner BEFORE phases 3–4**, or each new field repeats
  the ritual that produced the retracted flip.

  **Emergence verdict: subunit-emergent, not cell-emergent.** Envelopment is builder-authored, and the
  repo's own sweep found H4 passes with envelopment pathing OFF. Delete the cell layer and little
  shipped behaviour changes (phases 1+2 byte-identical across all 20 rows; the whole cell-morale
  programme moved win-share one row; discipline/quality/stamina/armour are not per-cell at all).

  **Historical:** `triplex acies` is misapplied (a **depth** arrangement cited for a lateral
  tripartition) and load-bearing — `n_cmd` is the only free parameter landing H3 in band and was chosen
  *after* measuring the 0/53/95 sweep. Casualty totals are near-band but the causal shape is inverted:
  `pursuit_damage` is never called in the measured mode, so the engine kills the loser then breaks him;
  history breaks then kills. **CEV naming is wrong** — Dupuy's CEV is a persistent per-force fitted
  residual, not an i.i.d. per-battle draw; rename to Clausewitz/Beyerchen friction and expect σ to
  shrink as real mechanisms land. That strengthens ED-MB-0043's measure-the-primitive-first ordering.

- **ED-MB-0042 (2026-07-25): THE CELL IS THE PRIMITIVE FOR MORALE — built, measured, flipped ON.**
  Jordan's directive ("the cell needs to be the primitive for morale, discipline, quality, stamina,
  route, health, armour, facing, damage, troops count, etc"), executed for the first of those states.
  Cells carry morale; the subunit's morale is the troop-weighted mean of its live cells (derived, not
  stored); that aggregate pulls its own cells back at a discipline-gated rate. A broken cell stops
  contributing combat weight while its men remain present and killable; breaks spread over the
  8-neighbourhood lattice. **Phase 2 was unreachable** until cells got their OWN du Picq break-point —
  bodies had erosion *and* a break-point, cells had erosion only, so a cell had to be destroyed twice
  over to break and the body always won that race by construction. An asymmetry, not a magnitude.
  **⚠ The default flip was made and RETRACTED the same day. `PC_CELL_MORALE` is OFF.** The measurement
  (win-share 7→8/20, casualty realism 2→7/20) was confounded: `between_turn_recovery` and
  `reset_morale_between_battles` write the morale **scalar**, which `eff_morale` stops reading once
  cells are seeded, so under the flag they are **silent no-ops**. Multi mode runs multi-turn battles
  and resets morale between them — the ON arm fought with morale that never recovered, the OFF arm's
  did. "The loser breaks earlier" is exactly what an unrecoverable body also produces. Goldens and the
  `_PINNED_OFF` pin are back to their pre-flip values; net shipped behaviour change is zero.

  Same defect class as the `erode_morale` silent no-op earlier in this lane. That was fixed as a single
  instance with no sweep, so it recurred — and this time reached a shipped default. **When the cause is
  "a representation change orphaned its writers", the unit of repair is every writer, found by grep.**

  Two genuine bugs the failing suite exposed are **kept** (both independent of the flip): subunits that
  inherit their morale were **born broken** (seeded at `eff_morale`'s no-parent 0 because `_unit` is set
  after `Subunit.__post_init__`), and the weighted mean returned a **1-ulp** value for a uniform body,
  which crossed a `DAMAGE_BY_DEGREE` boundary via `_morale_sigma` and zeroed exchanges.

  **Next in this thread, in strict order:**
  1. ~~**The scalar-write sweep — the blocker.**~~ **DONE.** `Subunit.set_morale` / `Unit.set_morale`
     are the single owners of an absolute write; `erode_morale`/`pull_morale` already owned the
     relative one. Routed: `between_turn_recovery` (unit + atom), `reset_morale_between_battles`
     (unit + atom), the rout write `u.morale = 0.0`, `Unit.cascade_morale_hit`. One site is
     deliberately left bare and annotated (`core/state.py`'s `atom.morale = atom.eff_morale`
     materialises the scalar so the stochastic-rout punch stays local). Guarded by
     `tests/valoria/test_morale_write_sweep.py`, whose `_CELL_OWNED` registry is field-parameterized
     so phases 3/4 inherit it by adding a key.

     ⚠ **RE-FLIP PRE-CONDITION — two harness writers are NOT swept.**
     `tests/sim/mass_battle/lanchester_signature.py` (~line 126) and
     `tests/sim/mass_battle/test_persubunit_stress.py` (~line 191) each still hold a bare morale write.
     They were swept and then **reverted on purpose**: the anti-fabrication gate scans the changeset,
     so touching either file dragged ~100 pre-existing uncited constants (none introduced by that
     change) into a blocking gate. Under `PC_CELL_MORALE=OFF` they are inert. **Sweep them before the
     flag flips** — `lanchester_signature` pins morale high specifically to *disable* rout, so a silent
     no-op there would let bodies rout mid-signature and measure the Lanchester exponent on truncated
     battles. Expect to have to cite or ledger those constants as part of that work.
  2. **Re-measure the flag honestly**, then decide the flip. Not before 1.
  3. **Phase 3 — stamina + discipline + quality per cell.** Retires `col_grid`, the third granularity
     between cell and subunit.
  4. **Phase 4 — hp + armour per cell.**
  5. **Decide `PC_STOCHASTIC_ROUT`'s fate.** Measured inert under cell morale (35.6% vs 36.1%) — but
     those absolutes were taken under the same no-recovery confound and must be re-taken after 1. The
     OFF-vs-ON *comparison* is still fair (both arms share the confound). Still load-bearing on the
     unseeded path, so a retirement candidate, not dead code.
  6. **Re-decide `ROUT_CASCADE_FRAC`** (still inert at 1.0) once phase 3 settles what a "section" is.

- **ED-MB-0038 (2026-07-24): MATCHED COMMAND-GRANULARITY honest gauge — envelopment artifact fixed, H3
  flagship 0→70.7%.** The density-matched gauge (ED-MB-0027) had unmasked a SECOND measurement artifact
  one axis up: the composed enveloper/refused presets always faced a SINGLE-subunit opponent, and a
  monolith is unbreakable by envelopment (casualties dilute across one HP pool; the ED-1019 per-subunit
  rout cascade has nothing to bite), pinning H3/H4/H6 to 0% regardless of geometry. `granularity_probe.py`:
  H3 = 0%@1-command → ~53%@3 → ~95%@6. **Fix** (the granularity analog of the density-constant): new
  `_command_army(shape,n_cmd=3)` builds the composed side's opponent as a 3-command tripartite battle line
  (Polybius VI / triplex acies) at constant density; wired H3/H4/H6/H10/H11. **Gauge multi 6→8/20** — H3
  0→70.7 (band 55-72 OK), H11 0→45.6 (OK), **zero regressions** (only all-failing envelop rows touched).
  Refuted en route: naive persistent defender reface (made it worse — a multiply-engaged subunit can't face
  everyone). Gauge-harness only; no engine .py, byte-exact goldens untouched.
  **NEXT (remaining envelop misses, characterized this session):**
  1. **SIDE-ASYMMETRY (highest value — contaminates every reverse row).** Enveloper wins **73.7% as side A,
     22.5% as side B** vs the same 3-command line, same seeds (`side_probe.py`). CONFIRMED not an RNG-stream
     artifact (construction doesn't consume `random`). Composed MIRRORS show only a modest intrinsic side-A
     bias (~53-58% @ n=40, near noise) — so the 51pp swing is an **INTERACTION**, not a pure side bias:
     the enveloper's APEX-forward centre (`build_envelopment`, `start_row+APEX*advance_dir`) + wing placement
     vs the flat command-line flips favorability by closing direction **[APEX HALF SUPERSEDED
     2026-07-29, E8/D3 — see correction 1 above: `engine.py:414-419` applies APEX only when the
     caller omits `starting_position`, and both harnesses pass it, so the apex offset NEVER EXECUTES
     in these batteries. Live candidates are `min()` over a set (`orchestration.py:1744`) and
     banker's rounding at exactly .5; do not spend further effort on the APEX hypothesis]**.
     `side_face_probe.py` shows the granular
     defender is struck **F-only** both sides (the win is frontage/overlap + rout-cascade, NOT flank-arc —
     the defender refaces). Needs a tick-by-tick geometry trace of the enveloper-as-B closing; do NOT hack
     blind. This is a genuine engine deployment bug, not a gauge calibration knob.
  2. **H4** envelop-vs-3-command-Arrowhead = 0% (the wedge centre punches the holding line).
  3. **H5** refused-vs-envelop = 100% (refused too strong).
  4. **H6** refused-vs-line = all-draw stalemate (UNRESOLVED at n=60).
  Plus the Cannae deep-baiting-centre + cavalry-rear composition (Jordan: ≥6 subunits, deep centre holds via
  rotational depth, cavalry wheels the rear, baiting) and the box-brace primitive (C2/C6, currently
  NOT-REPELLED at 86.7 raw cav-a). Evidence + probes: `audit/2026-07-22-mass-battle-stress-test/`
  (granularity_probe, cannae_calib, depth_factorial, cluster_probe, reface_probe, side_probe, side_face_probe;
  honest_gauge_readout.md §"Matched command-granularity").

- **ED-MB-0034..0037 (2026-07-24):** field-coordinate unification (abandon the dead spawn lattice) + orphaned
  `perimeter.py`/cavalry orbital-wheel envelopment + B6 multi-side + MORALE_EROSION_DAMP/SUBUNIT_ROUT_FLOOR
  wiring + dead-mechanic removal. See `registers/editorial_ledger_mb.jsonl` + `tests/coverage_matrix.md`.

- **ED-MB-0018 (2026-07-23): octagon facing = DAMAGE-RECEIVED MULTIPLIER + reaction delay + multi-side
  shock** (Jordan directive, verbatim: "the facing octagon is a damage-received multiplier — attacks from
  behind do ~**2×** the damage of from the front; cells **cannot turn instantaneously** (needs a couple-tick
  reaction); attacked from **multiple sides** is **extra bad**, not just divide-by-two"). Replaces the legacy
  `-2`-dice octagon **pool** penalty (too weak: legacy rear was only 1.25× front). New `_octagon_dmg_mod`
  (orchestration.py) → pure per-cell facing arc (front **1.0×** / flank **1.5×** / rear **2.0×**) multiplying
  the defender's casualties; reads the arc against the **LOCAL** attacker centroid (`OCTAGON_LOCAL_REACH=2.0`)
  so a wide line's wing stays GREEN head-on — **verified front→1.00×, rear→2.00× exactly per-seed**. Reaction:
  a cell hit outside its front arc keeps its exposed facing until `FACING_REACTION_TICKS=2` elapse, and only
  refuses if it can SEE the threat (≤105° FOV) and isn't frontally pinned — a **rear** strike is blind → 2×
  persists the whole engagement. Multi-side: `eng_counts≥2` → `×(1+MULTI_SIDE_SHOCK=0.5)` compounding.
  `PC_OCTAGON_DMG` **default ON**; legacy path preserved **byte-exact** under `=0` (the wrapper/pocket/roll-up
  pool machinery goes dormant under the flag — subsumed by arc + shock). Compounds with frontal-brace
  stripping → a braced front that parries to 0 is annihilated from behind (Cannae). **All 4 bat.py goldens
  re-recorded** (grid+field; head-on single-subunit rows all-GREEN→unchanged; envelop/cannae/oblique move).
  `test_octagon_damage.py` (5). Disclosure: `audit/2026-07-22-mass-battle-stress-test/octagon_damage_model.md`.
  **Follow-on:** graded ≥2/3/4-side escalation; full-campaign A/B of the default-ON flip once ED-MB-0016
  friction + the conjunctive-envelopment gate land (all three interact on the envelopment rows).

- **ED-MB-0017 (2026-07-22): multi-unit deployment geometry + envelopment pathing fix** (Jordan-flagged
  from the hierarchy snapshot: overlapping subunits, both envelopment wings on one side, refused flank
  level with the line). Root cause: `build_army` deployed subunit i at `col=15+i*4` (fixed step < subunit
  frontage). Fixed with frontage-aware anchor-centred deployment (`_centered_line_cols`, fit-to-field, no
  overlap 1–11 subunits), symmetric opposite-flank envelopment wings (mirror double envelopment), and an
  echeloned-back refused wing. **Speed (Jordan):** envelopers must be fast — `PC_ENVELOP_SPEED_MULT=2.0`
  (envelop maneuver) + `PC_CAVALRY_SPEED_MULT` 2.0→3.0 (cavalry ~3× infantry); cavalry double envelopment
  now wraps behind by ~t6–8 (was t16–20). Independent adversarial critic run: F1 over-wide crash + F2
  gauge_mb same-defect FIXED, F3/F4 tested. Machine-vision comparison + sources saved to
  `research/diagrams/mass_battle_formations/`. All 4 bat.py goldens re-recorded (3 multi-subunit rows
  re-baselined, ED-909 precedent; 7 single-subunit unchanged; byte-exact green). `test_deployment_geometry.py`
  (16). **Follow-on:** the wrap seals a horseshoe not a full ring (no cavalry rear-transit); single line only
  (no triplex depth-lines); envelopment still often loses the outcome (DG-6 "envelopment not rewarded" —
  ED-MB-0016 friction + a still-needed conjunctive envelopment gate; this fast correct wrap is its precondition).

- **ED-MB-0015 (2026-07-22): spatial-model v2 Stage F — verification + golden re-record + P-DEC-4
  historical revalidation.** All I1–I7 hold; stress harness S0–S5 green; Lanchester exponent + depth-2
  preserved; field goldens re-recorded (`unit_field 2da5183…` verified, `cell_field 5f5db96…`; grid
  unchanged). **P-DEC-4:** gauge pre-D baseline (A–C) = **10/20**, v2 (A–E) = **6/20** multi — D+E moved
  it down 4 rows (authorized re-baseline, but material; see `stage_F_verification.md` §5). Dominant
  failure = **DG-6 over-decisiveness**, root-caused: melee pool sums N independent dice → CV collapses
  ~1/√N → `compute_degree` deterministic from force ratio → 100%/0% vs historical bands. **Now being
  RESOLVED** (Jordan directive 2026-07-22: extend code to resolve standing issues via academic research /
  military theory / mathematics / historical precedent) — the DG-6 grounded resolution (restore
  scale-invariant outcome variance so a large advantage is decisive-but-uncertain/banded) is UNDERWAY as
  a follow-on ED-MB, built on stochastic-Lanchester/breakpoint models + Sabin's *Lost Battles*
  decisiveness bands. **Stage G (retire integer engine)** remains after: note the field engine lives in
  `tests/sim/mass_battle` (not `systems/`), so routing `resolve_mass_battle` (`systems/mass_battle/sim/
  massbattle.py`, called by `systems/factions/sim/faction_action.py:_try_conquest`) onto it needs a
  faction→army adapter + outcome→`{degree,attacker_wins}` mapping + likely a field-engine relocation —
  an architecturally-significant, cross-lane (MB+FA) epic.

- **ED-MB-0014 (2026-07-22): spatial-model v2 Stage E — weapon-class reach + the `pike` troop type.**
  Per `spatial_model_v2_plan.md` §3 Stage E / Jordan P-DEC-1. `reach_for`/`TROOP_TYPE_REACH` now return
  the per-type front-face reach (non-pole 0.1 / pole 0.2 / **pike 0.3** / lance 0.2 / ranged 0.1 sidearm),
  replacing the flat `REACH_SHORT=0.5` placeholder Stages B/C carried; feeds `cell_boxes_for →
  obb_front_reach_overlap` + the TOI halt. Authored the **`pike`** troop type end-to-end (stats mirror
  heavy_infantry — reach 0.3 the sole differentiator, provisional-by-analogy since §B.2 has no pike row;
  pike weapon + ('pike','medium') loadout + ShieldWall/Hold/Anvil roles). **Reach advantage emerges** via
  the already-wired charge-recoil reach gate: braced pike/spear (reach ≥ lance 0.2) repel a cavalry charge
  (defender ~96.7% hp, cavalry recoils ~88.3%), levy (0.1) is run down (~90.7%) — the anti-cavalry pike
  role, emergent from the reach data. **Disclosed finding:** reach differentiation does NOT change
  symmetric standing melee (mutual exchange once contact fires; reach only shifts timing) — reach is a
  charge/brace lever, not a standing-melee one. A directional-reach exchange term (pike-pins-forever
  hazard under halt-on-contact) is flagged for Jordan, NOT introduced. Gates green:
  `test_reach_weapon_class.py` (10); **I4 byte-exact grid oracle green** (no kite in the battery). Two
  items flagged for Stage F: (1) the 0.1/0.2/0.3 scale vs PP-290's 0.5/1.5 meter-grounding needs
  reconciliation (deferred, not overwritten); (2) **P-DEC-3 cavalry density cap (< infantry) deferred** as
  a separate follow-up (kept out of Stage E to keep the reach A/B clean). Next: **Stage F** (full
  verification + field-golden re-record + historical revalidation), then **Stage G** (retire the integer
  `systems/mass_battle/sim` engine, route `resolve_mass_battle` onto the field engine — P-DEC-2 resolved).

- **ED-MB-0013 (2026-07-22): spatial-model v2 Stage D — the LAST live integer on the field contact
  path removed.** Per `audit/2026-07-22-mass-battle-stress-test/spatial_model_v2_plan.md` §3 Stage D.
  The melee Lanchester frontage term `len(set(int_col))` (the only integer left on the live position/
  contact path, per `backwards_analysis.md`) is now a CONTINUOUS OBB front-overlap **width**:
  `geometry.engaged_frontage(a_boxes, b_boxes, heading)` = the union length, along a side's frontage
  axis, of each engaged cell body's width-interval clipped to the enemy's covered meeting span.
  `_find_contacts_standoff` threads `a_front`/`b_front` onto pairs; `_lanchester_strength(front_width=…)`
  consumes it, falling back to the integer count on the grid/OFF path (**I4 byte-exact — grid oracle
  green, 30 passed**). **Scoping call:** the snapped `(rank,file)` cell identities are KEPT — they key the
  formation-lattice casualty/density/stamina substrate (a discrete troop-block identity, I3's
  defensible-quantization carve-out, NOT a live-position integer); only the frontage MAGNITUDE moved to
  continuous. Gates green: `tests/valoria/test_frontage_conservation.py` (15) — integer-limit reduction,
  fractional on offset, depth-invariant, frontage-capped (Lanchester linear), I1 conservation ×5 seeds,
  I2; maneuvers/movement/yield 20 passed/1 xpassed (pre-existing). **DG-6 disclosure (not tuned):** A/B
  12-seed field battery — axis-aligned symmetric meetings byte-identical; shift only on offset/asymmetric
  meetings (Line4-vs-Line2 wide-attacker overkill capped to the narrow defender's meeting width, A_win
  12→10/12, def hp .452→.487). Lanchester melee exponent unchanged (p=2.50 before/after — pre-existing
  DG-6 artifact, frontage-independent **[the p=2.50 magnitude itself was later shown to be a harness
  artifact — E8/A6a 2026-07-29; the unchanged-before/after comparison stands]**). **Field goldens NOT re-recorded (Stage F, per plan §7).** Next
  in this v2 sequence: **Stage E** (weapon-class reach 0.1/0.2/0.3 + author the `pike` troop type, P-DEC-1;
  P-DEC-3 cavalry density cap), then **Stage F** (full verification + digest re-record + historical
  revalidation), then **Stage G** (retire the integer `systems/mass_battle/sim` engine, route
  `resolve_mass_battle` onto the field engine — P-DEC-2 RESOLVED=retire).

- **ED-MB-0011 (2026-07-22): DG-10 field-movement freeze FIXED + full field-based stress test.**
  Jordan asked for a field-based (not grid) stress test with all flags/gates activated on the
  *active* engine (`tests/sim/mass_battle/`, NOT the wired `systems/mass_battle/sim/` bare port,
  which has none of these flags). The stress test surfaced the dominant field-path defect: `_node_advance`
  floored any sub-Discipline-5 body's velocity to 0 (`floor(1×0.7)=0`), so the MAJORITY of canonical
  troop types (levy/light_inf/heavy_inf/archers/crossbow/sling/artillery, all disc<5 per §B.2) NEVER
  advanced to contact on the live field path — every such battle a vacuous 0-casualty draw. This is
  **DG-10** (opened by ED-MB-0007) generalized: the continuous-velocity accumulator meant to prevent it
  was wired only into the legacy grid `advance_cells` and sat dead there. **Jordan ruled in-session**
  ("fields, not grids. no grids." / "if it's broken and not commensurate with system, disable" / "what
  even is the point of the continuous velocity accumulator?"): the `math.floor` is the grid-snap the
  field exists to remove; the accumulator is itself just a Bresenham workaround. **Fix:** on the FIELD
  path `step` is now the real velocity (no floor, no accumulator) — anchor/pos are already floats and
  the sole consumer moves by `min(step,mag)`; whole velocities stay int so disc≥5 rows are byte-exact,
  fractions (disc<5) advance the float anchor at their true 0.7 cells/tick. **Legacy GRID path
  untouched** (gated on `if FIELD_MOVEMENT`) → CI byte-exact grid oracle still passes (2 passed). Field
  goldens (bat.py cell_field/unit_field, NOT CI-checked) re-recorded: mirror/ranged byte-identical, the
  8 decisive rows change because a unit degrading below disc-5 MID-battle used to freeze and now keeps
  moving (trace: wedge seed 0 → disc 3). maneuvers+yield: 12 passed/1 xpassed. **Scope: MOVEMENT only** —
  it shifts the 20-row Cannae balance gauge (frozen units now fight), which is the **DG-6-gated**
  calibration surface; NOT a balance claim, no balance constant tuned. Stress harness + full findings:
  `audit/2026-07-22-mass-battle-stress-test/` (S0 wiring: all 30 MECHANICS resolve; S1 fuzz: 0 engine
  failures / 77.7% contact / 1-of-197 minor cell-vs-hp accounting drift on a clean unit; S3: 12/16 gates
  proven WIRED by A/B, 4 inert-on-scenario incl. by-design-exempt PC_BRACE_SETUP_DELAY; S4: PC_FACING_MODEL/
  FIELD_CONTACT/REFORM_CHECK all SAFE when activated; S5: determinism + perfect mirror symmetry).
  **Next for this lane:** (1) the residual cell-vs-hp accounting drift (RC-1 family, 1/197 clean units)
  and the fragile envelopment-shock validators (V-SHOCK/V-BRACE proxy ≈0) are both DG-6-layer, Jordan-
  gated; (2) DG-6 itself (the resolution-architecture calibration) remains the open highest-leverage gate.

- **Mass battle — Stages A–D + LC-8 landed on `main` (2026-06-30 → 2026-07-02, PRs #45/#52/#56/#57/#59).**
  Coordinate-field true-adjacency contact (Stage A), facing/attention/reaction physics (Stage B), the command layer
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
  `using-opus-4-8-ultracode-floating-tiger.md` if resuming this thread).

- **Three Jordan rulings landed 2026-07-02 (all executed same day):**
  1. **ED-1089** — `FIELD_MOVEMENT=1`/`PC_NODE_COHESION=1` are now the DEFAULTS (Stage A step 7 executed;
     "yes, field movement is default."); the grid stays the byte-exact oracle via explicit
     `FIELD_MOVEMENT=0 PC_NODE_COHESION=0` pins (the CI gate was updated from env.pop to explicit '0'
     pins — load-bearing, see `test_mass_battle_byte_exact.py`), and `bat.py`'s field digests were
     re-recorded (they had gone stale vs the LC-8 battery).
  2. **ED-1090** — videogame sub-unit cap is **11** ("subunits can be as high as 11."), lifting the
     TTRPG hard cap of 3; enforced in `engine.build_army`; open reconciliation flagged: Command clamps
     1–7, so >7 commanded subunits needs a future Command-exceeding mechanism (subordinate officers?)
     — future ED.
  3. **ED-1091** — the charge-recoil now zone-gates to the frontal (GREEN) arc (`PC_RECOIL_FRONTAL`,
     default ON; historical-validity condition verified against `mass_battle_gauge_grounding.md`
     §4.3/Burkholder before executing, per Jordan's "c7 if it is historically valid"); gauge row C7
     can now legitimately add a braced+enveloped variant (grounding doc §4.3/§5.7 still says "flagged,
     not fixed" — update on the next gauge pass).

- **Stage E MVP shipped, Stage F investigated (2026-07-02, PRs #62/#64/#65).** Army Configuration Mode
  (click-to-place deployment) landed as an MVP. Stage F ("Charge/Depth/Equipment Physics") was
  investigated before writing new physics code (ED-1092): speed-differential punctures and
  depth-absorption are already DONE; fidelity D1's zone half is done (ED-1091 above), the actor half
  remains OPEN (no canonical predicate exists for "actor-gate," flagged for Jordan); fidelity D2 was
  VERIFIED ALREADY CORRECT by direct numeric probe, no code change needed.

- **Still open:** Stage E's deeper UX beyond the MVP, and the rest of Stage F (actor-gate predicate,
  `PC_CHARGE_*` derive-not-assert — tracked separately as Track M Stage 5, the engine-wide
  calibrated-debt retirement sweep).

- **An orphaned-proposal audit (2026-07-02) also flagged:** `references/
  mass_battle_redesign_workplan_v1.md` is fully superseded (no banner exists — worth a supersession
  marker); `proposals/multiunit_envelopment_plan.md`'s cross-**Unit** spatial envelopment
  ("Path B") is a materially different, still-unbuilt mechanism from the Unit-level `build_envelopment`
  that landed — don't conflate "Envelopment shipped" with "Path B shipped."

## Catch-up (2026-07-04) — this file fell behind; see root HANDOFF.md for the fuller narrative

This lane file wasn't kept in sync since the entries above (predates ED-MB-0001). Condensed summary of
what's landed since, in order — full detail lives in root `HANDOFF.md`'s mass-battle block and
`tests/coverage_matrix.md`'s dated entries:

- **T1-T4 charge-recoil ruling (ED-1095)** executed; **movement/pathing audit (ED-1096)** found
  `envelop`/`sweep`/`wheel`/`kite` only worked on the legacy grid path, unreachable on the live default
  node path since ED-1089's field-movement flip.
- **ED-MB-0001 (2026-07-02, PR #66, merged):** the movement/pathing fix-plan executed end-to-end —
  waypoint primitive gives `_node_advance` real per-tick steering for `envelop`/`sweep`; `PER_CELL`
  default flipped 0→1 (gate 4). Disclosed, not chased: enabling `PER_CELL`'s fatigue/attrition mechanics
  made the H3-H6 Cannae-pattern gauge rows collapse (0-13% losses vs. a 45-72% expected band) — landed
  as a loud `xfail` on `test_envelop_reaches_rear_node`, flagged as the next investigation.
- **ED-MB-0002 (2026-07-04, PR #73 audit + PR #75 ratification):** a Fable-led Workflow diagnosed the
  H3-H6 collapse as composition-coupling defects in the pool/morale accounting layer (RC-1), not the
  "two racing clocks" theory the xfail's own docstring proposed (refuted by gauge row C7). Jordan ruled
  DG-3 (bottom-up per-cell pool split — corrected mid-session from an initial flat-divide attempt per
  Jordan's own "per-cell troop density... bottom-up" feedback) and DG-4 (a blend of per-subunit and
  whole-unit morale, with continuous sibling-pull, wiring already-existing `agg_morale`/`derive_rout`/
  `cascade_morale_hit` machinery). Both implemented on `claude/mass-battle-cannae-gauge-dg-rulings`; all
  4 `bat.py` digests re-recorded (expected — touches shared, non-gated combat-resolution code);
  `tests/valoria` 87 passed/17 skipped/1 xfailed (after an adversarial review found and fixed 4 real
  bugs: a pool-zeroing bug for continuous-scale subunits; a same-phase-rout-masking ordering bug and a
  Gauss-Seidel sibling-aggregation bug in the new morale pull, both fixed by snapshotting siblings and
  running self-erosion last; a dormant `morale: None` footgun in `build_army`). **DG-5 CLOSED**: a
  frozen-vs-wheeling-wings gauge ablation (H3-H6) shows byte-identical outcomes — no maneuver-timing
  race exists at all, refuting the original "two racing clocks" theory outright, not just narrowly.
  C4-vs-C7's gap is fully explained by `stance='hold'` alone (discipline contributes nothing).
  **Honest result: the DG-3/DG-4 fix did NOT close the targeted gap.** Gauge re-run (n=20): aggregate
  pass counts unchanged (single 2/20, multi 4/20) but composition shifted (H1 newly fails, C1 newly
  passes); H3/H5/H6 remain fully unresolved (100% draws); H4/C4 show real but insufficient movement
  toward their bands. RC-1's accounting fix looks necessary but not sufficient — DG-1 (was the
  pinning-force composition ever historically ratified, given it only passed under the now-confirmed
  RC-2 invincibility artifact) and DG-2 (a fighting-withdrawal/yield mechanic) are the better-evidenced
  remaining levers. `test_envelop_reaches_rear_node`'s xfail reason/docstring updated to retire the
  superseded racing-clocks narrative and record this finding instead. **Next action: this is now a
  Jordan-ruling unblock (DG-1/DG-2), not further engine implementation.** RC-5 (9/20 gauge rows failing
  for unrelated reasons) remains a separate, not-yet-opened lane item.

- **ED-MB-0003 (2026-07-05): follow-up Fable-5 audit found 4 more real defects; Jordan ruled all 3
  gates; DG-2 captured as a workplan, not built.** The "RC-1 fully fixed" story was false — D1 (an
  outer army-size dilution multiplier double-diluting a composed subunit's pool, removed per Jordan's
  ratified "intensive/partition-invariant" semantics), D2/D2b (`_envelop_goal`'s hysteresis-free limit
  cycle + `_node_advance`'s step-freeze bug, together the actual reason wings never reached contact —
  both fixed), D3 (routed atoms resurrected to pool 1; first-pass fix was a no-op per adversarial
  review, corrected to force `a_net`/`b_net=0` directly since `roll_pool`/`_sigma_net_boost` re-floor
  pool internally), D4 (`distribute_casualties` cross-subunit column-leak, fixed via per-subunit
  scoping), plus a harness force-ratio bug (`_envelop_army`/`_refused_army` fielding 3x/2x a
  single-subunit opponent's troops, fixed via `total_troops` force parity). **Jordan's rulings
  (AskUserQuestion): DG-3 completion = intensive pool semantics; DG-1 = symmetric-at-parity (infantry)
  + majority-pin/cavalry-wing (C4/C7, Polybius/Livy order of battle); DG-2 = "create as workplan"** —
  `proposals/mass_battle_fighting_withdrawal_v1.md`, PROPOSED, NOT implemented. Independent
  adversarial review caught 2 more real bugs (D3's no-op; `wing_speed` never reaching `Unit.speed`) —
  both fixed. **Honest result: H3/H4/H5/H6/C4's draws are entirely GONE, but every row now OVERSHOOTS
  its band decisively in the attacker's favor** (except C7, still passing). Full 20-row gauge: 4/20 →
  5/20 (C1 newly passes; RC-5's 9 rows untouched). **New, deliberately undecided finding:**
  `subunit_combat_pool`'s Command-driven score may not scale by troop share, letting spatially-separated
  attacking fronts each roll near-full combat strength against one defender at once — genuine defect or
  historically-correct mechanism (with bands needing reconsideration)? Flagged, not silently tuned.
  DG-5 re-confirmed closed for a corrected reason (D2's bug, not a genuine non-race). All 4 `bat.py`
  digests re-recorded; `tests/valoria` 88 passed/16 skipped(numpy)/1 xfailed. See
  `tests/coverage_matrix.md`'s 2026-07-05 entry + ED-MB-0003. **Next action: Jordan's ruling on the new
  partition-invariance question and DG-2's build sequencing — not further unprompted implementation.**

- **ED-MB-0004 (2026-07-08): partition-invariance fix landed; RC-5 preliminary finding; DG-2 build
  in progress.** Jordan ruled (AskUserQuestion): partition-invariance = **"genuine defect — fix it"**;
  DG-2 = **"build it now"**; RC-5 triage = **start now**. Fixed `subunit_combat_pool`'s Command-driven
  score being troop-count-independent per atom in a way that let >=2 of one side's atoms simultaneously,
  fully engage the SAME single opposing atom (a pinning center + 2 wings converging on one Line/Arrowhead
  defender — H3-H6/C4/C7's exact shape) each roll near-full base_pool, multiplying total dice by the
  convergence-group size for identical total troops. New `core/exchange.py:_pair_engaged_troops` +
  `orchestration.py:_convergence_scale`/`PC_CONVERGENCE_NORM` (default ON) renormalize any such group to
  what ONE merged atom of the combined troops would contribute; verified live via direct trace (fires on
  1446/1686 sampled ticks of an H3-style battle, max group size 3 — not a no-op). All 4 `bat.py` digests
  re-recorded (shared, non-gated code). `tests/valoria`: 112 passed/57 skipped/1 xfailed/0 failed (the 7
  `test_names.py` failures seen locally are PRE-EXISTING and unrelated — confirmed via `git stash`
  bisection, an environment/fixture issue). **Honest result:** gauge re-run (multi, n=60) shows the fix
  does NOT move H3-H6/C4's win/loss/draw split at all (bit-for-bit identical to the pre-fix baseline) —
  the defect was real and is now closed, but was never the dominant lever for these rows' overshoot
  (envelopment/charge-shock morale collapse dominates). Full 20-row gauge unchanged (single 2/20, multi
  6/20). **RC-5 preliminary finding (diagnostic only):** a controlled A/B-slot-swap test on 3 pairs
  (Arrowhead/Line, GappedLine/Line, GappedLine/Arrowhead) found an inconsistent slot-dependent asymmetry
  that tracks neither a uniform side bias nor shape hierarchy (a true Line-Line mirror stays near-even,
  17/13 of 30, ruling out a blanket engine-wide bug) — likely shared ingredient (not traced further):
  `ANCHOR_MAP`'s per-shape deployment column (Line=9/Arrowhead=8/GappedLine=7) applied regardless of
  which side carries that shape, so differently-shaped sides deploy at different absolute columns. Next
  concrete lead for RC-5, not claimed solved; the other 6 rows (H7,H8,R1,R3,C1,C3,C5) untouched. Full
  record: `tests/coverage_matrix.md`'s 2026-07-08 entry + ED-MB-0004 (now resolved).

- **ED-MB-0005 (2026-07-08): DG-2 fighting-withdrawal/yield mechanic — commanded-entry slice built.**
  Per Jordan's "build it now" ruling, built exactly the proposal doc's own §4 step-1 scope: `Subunit.
  yielding`/`yield_active` (discipline-gated, melee-only), a `'yield'` order (composes with existing
  Order/check_orders — `yielding` added to `_ORDER_SAFE_FIELDS`), movement (`_yield_goal`, reuses
  `_kite_goal`'s flee vector, capped 1 cell/tick, node/field path only — same scope as envelop/sweep),
  facing-lock (fires regardless of `PC_FACING_MODEL`, the mechanically load-bearing "faces the enemy,
  unlike rout" distinction), combat-pool malus (`YIELD_POOL_MULT`, reuses `PC_SHOCK_HOLD_BRACE`=0.35),
  and anti-abuse (no volleying while yielding). Both new magnitudes (`D_YIELD=3`, `YIELD_POOL_MULT`)
  flagged `[CALIBRATED-DEBT]`, not independently derived, per the doc's own §5. All 4 `bat.py` digests
  confirmed BYTE-IDENTICAL (genuinely inert-by-default, no re-record needed). New
  `tests/valoria/test_mass_battle_yield.py` (9 tests, all green); full `tests/valoria` suite green, no
  regressions (123 passed/56 skipped/1 xfailed/6 pre-existing-unrelated `test_names.py` failures).
  **NOT built this pass (disclosed):** emergent auto-entry, rally exit, pocket exit — only the free
  "collapse to routed" exit exists (needed no new code).
  **Honest measurement:** center-yields-from-tick-0 (n=20, node path) raises center hp retained
  35.8%→40.6% (the mechanism works) but collapses the attacking army's win rate 70%→0% — an
  unconditional, whole-battle yield trades far more offense than it recoups. Not a broken mechanic;
  Cannae's yield was TIMED, this pass didn't build/measure timed entry — flagged as the natural next
  experiment. Full record: `tests/coverage_matrix.md`'s second 2026-07-08 entry + ED-MB-0005.
  **Next actions for whoever continues this lane:** (1) a timed/conditional yield-entry experiment
  (Order `tick:N` trigger, or emergent entry keyed to encirclement progress) to see whether a properly
  time-boxed yield recovers the army-level win-rate cost while keeping the center-survival benefit;
  (2) RC-5's other 6 untriaged rows (H7,H8,R1,R3,C1,C3,C5) plus tracing the ANCHOR_MAP deployment-column
  asymmetry lead to a root cause; (3) DG-1's composition question and the still-live envelopment-shock
  magnitude remain the larger unaddressed levers for H3-H6's overshoot (the partition-invariance fix
  closed a real defect but was never the dominant one there).

- **ED-MB-0006 (2026-07-08): combat pool abandons Command entirely — troop type/quality/numbers.**
  Per Jordan's direct instruction ("consider abandoning combat pools being related to the commander,
  and instead being solely derived from the subunit troop type, quality and numbers"), new
  `POOL_QUALITY_MODEL` (default ON): base pool = `eff_power × eff_size × POOL_QUALITY_SCALE` —
  troop-TYPE quality (`TROOP_TYPE_STATS`/§B.2) × NUMBERS (troops/BLOCK_SIZE), no Command anywhere.
  `POOL_QUALITY_SCALE=0.5` renormalizes to the historical baseline magnitude. Discipline/stamina
  penalties unchanged. Command still governs morale/formation-speed/orders/`derive_rout`, just not
  the dice pool. Applied consistently to both `subunit_combat_pool` and `Unit.base_combat_pool`
  (pursuit path). `COMMAND_SIGMA_ENABLED` branches remain selectable (`POOL_QUALITY_MODEL=0`) for
  A/B. All 4 `bat.py` digests re-recorded; `tests/valoria` 121 passed/57 skipped/1 xpassed (the
  usual pre-existing `test_names.py` failures aside).
  **Honest, mixed gauge result:** 6/20→7/20 (multi). C4/C5 newly pass (bigger-force cavalry rows
  correctly reward numbers now); **H4 (actual Cannae) flips from attacker-WIN-OUT to attacker
  LOSING badly** (1.7%/65%/33% draws) — composed-army rows lose out because their PER-ATOM numbers
  are now smaller than the single consolidated defender's, an real emergent trade-off, not a bug.
  **Open, disclosed residual:** `lanchester_signature.py`'s law-exponent check (melee should conserve
  p≤1.4) fails under BOTH models — pre-existing baseline already measured p≈1.55 (previously
  undetected, unrelated to this change) and a separate apparent "2:1 army loses 97% of the time"
  reading that a quick trace suggests may be test-methodology noise (single 18-tick `run_battle`
  call rarely resolves decisively at this ratio), not independently confirmed. The new model measures
  p≈2.50 **[exponent numbers from this harness rate as LEADS, not measurements — fit identifiability
  was never verified in this era, and the current harness is broken differently (A6a); E8
  2026-07-29]**, tested extensively (sqrt-numbers variant, 8-point scale sweep) without finding a scale that
  reaches ≤1.4 — plateaus at p≈1.65-1.7, confirmed NOT a Lanchester double-count (disabling
  `LANCHESTER_ENABLED` doesn't change the exponent at all) — the amplification is internal to how
  larger absolute pools reduce variance and make `compute_degree`'s discrete tier assignment
  near-deterministic from the pool ratio alone. **Next action: this needs the degree/damage-tier
  discretization or the Lanchester coefficient's own interaction reconsidered — not another pool-
  formula scale tweak (provably can't fix a ratio-sensitive test).** Full record: `tests/
  coverage_matrix.md`'s third 2026-07-08 entry; canon note in `designs/provincial/mass_battle_v30.md`
  §A.1 (ED-MB-0006).

- **ED-MB-0007 (2026-07-08): full 11-surface agonist-antagonist gauge architecture audit — why
  7/20, and what to do about it.** Per Jordan's direct instruction to investigate "from all
  directions and surfaces" (widened mid-session to explicitly add movement/pathing/routes/
  strategies/tactics/stances/reach, then ranged weaponry), two Workflow waves (7 + 4 surfaces;
  producer → isolated adversarial critic → opus-4.8-max synthesis per wave, then a third
  opus-4.8-max combination pass) fielded 24 subagents across ~1288 tool calls. **Full record:**
  `designs/audit/2026-07-08-mass-battle-gauge-architecture-audit/README.md` (+ `01_wave1_synthesis.md`/
  `02_wave2_synthesis.md` for per-wave detail). **Honest result:** the 13 nominal failures decompose
  to ~9 genuinely-deep engine divergences (C3/H9 are n=60 sampling noise; R1/R3 are
  harness-construction failures). Two mechanisms dominate, both causally proven by reversal
  ablation: **E1**, a cell-count/density plumbing defect (`geometry.py`'s two unreconciled
  cell-count generators → a static, never-recomputed `Unit.ncells` → the Lanchester density term)
  that reverses H3/H10 outright when patched; and **D1**, the super-linear resolution architecture
  ED-MB-0006 already flagged, now measured at melee exponent **p≈3.2 under the live PER_CELL=1
  path** — worse than ED-MB-0006's disclosed p≈2.50, which turns out to have been measured under
  the WRONG `PER_CELL` setting by `lanchester_signature.py`'s own hardcoded default. **[E8
  2026-07-29: this p≈3.2 PREDATES the stochastic-rout mechanism (ED-MB-0031, 2026-07-23), so A6a's
  rout-pin defect does NOT apply to it — but its fit identifiability was never verified either;
  rate it a lead. No exponent is derivable from the current harness until A6a lands.]** **These two are
  multiplicative, not competing, and neither alone lands a row in-band — this investigation is
  diagnostic, not curative**, disclosed as a first-class finding. **Granularity directive verdict:**
  the per-cell quality/type axis (veteran-front/levy-rear) is confirmed byte-inert for all 20 rows
  by four independent lines of evidence — a legitimate future architecture, not a gauge fix. The
  per-cell COUNT axis is already the #1 defect (E1). Troop-grounded speed and the entire
  ranged/volley pool were never brought under `POOL_QUALITY_MODEL` and remain ungrounded. **New
  empirical result** (found by the wave-2 synthesis's own probe, not present in either wave in
  isolation): the two cheapest-looking fixes for the ranged rows (R1: correct archer stats; R3:
  the `kite` instruction) are **mutually incompatible** — a correctly-statted discipline-3 archer
  computes a live movement step of exactly zero (no fractional-velocity accumulator on the node
  path), so `kite` cannot rescue a unit physically unable to move. This reverses an earlier reading
  that had listed a ranged-`hold` variant as a safe, contained fix — it is not; it is gated on
  **DG-10**. Ten new engine defects (E1-E10) and a harness-artifact cluster identified and bucketed
  (full detail + file:line citations in the audit README). **Eleven new Jordan-ruling decision
  points opened: DG-6 (the resolution-architecture calibration itself — the deepest, highest-
  leverage call) through DG-16 (tactical/role-layer grounding).** DG-numbering note: an earlier
  combination draft had reused DG-1..DG-5 for these new gates, colliding with the ALREADY-RULED
  namespace from ED-MB-0002/0003/0005 — caught and corrected to the DG-6..DG-16 sequence above
  (crosswalk in the audit README's Appendix). **Not yet implemented:** this ED closes the
  investigation itself; the ~10-item safe-to-fix list and all eleven DG-6..DG-16 rulings remain
  open follow-up work, gated primarily on Jordan's ruling on DG-6.
  **[CALIBRATED-DEBT] flagged, not resolved:** the currently-passing cavalry rows (C4, C5, C7) may
  be passing partly on the same E1/D1 artifacts targeted for removal — the pass count is not
  confirmed monotonic in fixes applied. **Next action for whoever continues this lane: DG-6 first**
  (it gates the highest-leverage fix and several other rulings) — either via Jordan's direct ruling
  or an `AskUserQuestion` pass through DG-6..DG-16 in priority order, then land the safe-to-fix list
  paired with whichever DG-6/DG-7 direction is chosen, then re-run the full 20-row gauge (no surface
  in this audit ran the complete battery — only directional/single-row causal evidence exists for
  any proposed fix).

---
