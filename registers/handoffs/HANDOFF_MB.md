# Handoff — MB (Mass Battle)

Lane-scoped continuity for the `MB` (mass battle) lane, per the `ED-<LANE>-NNNN` namespace
(`ED-IN-0001`) and `CLAUDE.md` §3's session-lane-scoping convention. Root `HANDOFF.md` is the
index; see it for cross-lane/global items.

## ⚠ CLOSED WORK LIVES IN `HANDOFF_MB_closed.md` — index, 2026-09-13 (`ED-IN-0221`)

**29 units · 18,880 tokens of finished narrative moved out of this file**, verbatim and in
order, by a predicate that reads each unit's body rather than its heading (the predicate, and why
heading markers were not trusted, are stated in that file's header). **The split is proved
lossless** — the two files' line multisets partition the original exactly.

**Nothing here needs doing.** The index exists so that a standing order inside finished work is one
file-open away instead of buried. **`!` marks a unit containing imperative language** (`Do not` /
`Never`) — check those before acting in their area.

| | tokens | unit |
|---|---|---|
|  | 4,584 | Catch-up (2026-07-04) — this file fell behind; see root HANDOFF.md for the fuller narrative |
| **!** | 1,883 | Next actions :: - **ED-MB-0045 (2026-07-26): FABLE-5 SIX-DIMENSION READ-ONLY AUDIT.** Six independent Fable-5 |
| **!** | 1,253 | Next actions :: - **⛔ `main` IS CI-RED (16 failures) as of `94bb902`. READ ED-MB-0061 BEFORE ANY MB WORK. |
|  | 1,153 | Next actions :: - **ED-MB-0042 (2026-07-25): THE CELL IS THE PRIMITIVE FOR MORALE — built, measured, flipped ON. |
|  | 910 | Next actions :: - **▶ SESSION 2026-07-29b (PR #271, ED-MB-0047..0051) — E4+I4, A3, A5a, A6a→A6b, A2 EXECUTED. |
|  | 823 | Next actions :: - **▶ SESSION 2026-07-29c (ED-MB-0058/0059/0060) — SPATIAL INTEGRITY + the PC_CELL_MORALE confound.* |
|  | 812 | Next actions :: - **ED-MB-0038 (2026-07-24): MATCHED COMMAND-GRANULARITY honest gauge — envelopment artifact fixed, |
|  | 792 | Next actions :: - **THE MASS BATTLE PLAN v1 (superseded): |
|  | 772 | Next actions :: - **ED-MB-0045 REMEDIATION PLAN (2026-07-26): all MB surfaces. |
|  | 714 | Next actions :: - **ED-MB-0011 (2026-07-22): DG-10 field-movement freeze FIXED + full field-based stress test. |
|  | 588 | Next actions :: - **ED-MB-0013 (2026-07-22): spatial-model v2 Stage D — the LAST live integer on the field contact |
|  | 484 | Next actions :: - **ED-MB-0014 (2026-07-22): spatial-model v2 Stage E — weapon-class reach + the `pike` troop type.* |
|  | 482 | Next actions :: - **ED-MB-0018 (2026-07-23): octagon facing = DAMAGE-RECEIVED MULTIPLIER + reaction delay + multi-si |
|  | 395 | Next actions :: - **ED-MB-0015 (2026-07-22): spatial-model v2 Stage F — verification + golden re-record + P-DEC-4 |
|  | 367 | Next actions :: - **ED-MB-0017 (2026-07-22): multi-unit deployment geometry + envelopment pathing fix** (Jordan-flag |
|  | 344 | Next actions :: - **Mass battle — Stages A–D + LC-8 landed on `main` (2026-06-30 → 2026-07-02, PRs #45/#52/#56/#57/# |
|  | 330 | Next actions :: - **A1a EXECUTED (2026-07-29, merged as #260).** Both field goldens bisected and |
|  | 325 | Next actions :: - **Three Jordan rulings landed 2026-07-02 (all executed same day): |
|  | 320 | Next actions :: - **A4-SWEEP EXECUTED (2026-07-29, MB session — this PR).** The test-commensurability repairs |
|  | 300 | Next actions :: - **A1b EXECUTED (2026-07-29, MB session — this PR).** The shipped configuration's regression |
|  | 276 | Next actions :: - **E8 EXECUTED (2026-07-29, MB session — this PR): the record corrected.** Three refuted claims |
|  | 260 | Next actions :: - **▶ START HERE — THE MASS BATTLE PLAN, v2 (2026-07-26): |
|  | 259 | Next actions :: - **PLAN v2 EXECUTION UNDERWAY (2026-07-29, MB session).** Wave 0: ED block **0046–0060 drawn |
|  | 141 | Next actions :: - **Stage E MVP shipped, Stage F investigated (2026-07-02, PRs #62/#64/#65).** Army Configuration Mo |
|  | 110 | Next actions :: - **An orphaned-proposal audit (2026-07-02) also flagged:** `references/ |
|  | 81 | Next actions :: - **ED-MB-0034..0037 (2026-07-24):** field-coordinate unification (abandon the dead spawn lattice) + |
|  | 57 | Next actions :: - **Still open:** Stage E's deeper UX beyond the MVP, and the rest of Stage F (actor-gate predicate, |
|  | 48 | Decisions |
|  | 17 | Pending |

---

## Next actions

- **ED-MB-0043 (2026-07-26): VECTOR AUDIT — all modules/scripts, all directions. Two observatory
  blind spots found and fixed; three MB findings held for Jordan.** Ran every structural graph the
  apparatus can build (vector L0+L1 VALIDATED 2/3, structure G_code+L2, formula, pointer, generation,
  ripple up/down/all-layers/impact, workbench, and the authoritative `build_graph.py` engine graph).
  Register: `audit/2026-07-26-mass-battle-vector-audit/02_weakness_register.md`.

  **The instrument was blind.** `structure_audit`'s `CODE_ROOTS` still read `('sim','tools')` after
  `sim/` was deleted 2026-07-21 — G_code covered 88 `tools/` modules and **zero simulation code** for
  five days, and nothing failed, because a dead scan root fails as an *absent finding*. Repaired
  (88 → 248 modules) and guarded on the CONFIGURATION, since no output assertion can see it. The
  naive fix would have been worse: the live MB package puts `tests/sim` on `sys.path` and imports
  itself as top-level `mass_battle.*`, so all 28 modules resolved 0 edges and would have entered the
  orphan list as false positives — `sys_path_aliases()` took internal edges 0 → 66. Both guards are
  mutation-verified. `pointer_audit`'s dead sim-root default was repointed too; measured effect NIL,
  and labelled as such.

  **SOLUTIONS PLAN (2026-07-26): `audit/2026-07-26-mass-battle-vector-audit/04_solutions_plan.md`.**
  Written under Jordan's steer that *we are still trying to solve mass battle the system, for itself* —
  so it orders MECHANICS first and plumbing after, which **reverses the audit's own top
  recommendation**. Two corrections to the audit are recorded in its §0: (a) the
  `scene_outcome.battle_concluded` finding is **not new** — it is ED-MB-0010, open since 2026-07-13
  with the same diagnosis and remediation; the action is to unblock, not re-decide. (b) The audit's
  "populate the contract, it's the top port blocker" priority is **wrong for this goal** — freezing a
  `state:` block before the cell-primitive programme lands would document the pre-cell model and
  attach a CI gate to it (plan §3.1; ship an honest `status`/`gap_notes` instead).

  **The plan's central recommendation — test the primitive before adopting the patch.** DG-6's
  research (ED-MB-0016) correctly names *correlation across combatants* as the only lever that breaks
  CLT self-averaging (Kress 2024), then implements the simplest form: one shared per-battle
  LogNormal shock. Disclosed cost: gauge **6/20 → 4/20** — it buys strategic realism by degrading
  tactical realism. But **a second, mechanistic source of correlation already exists and has never
  been measured against this problem**: ED-MB-0042's cell morale with 8-neighbourhood break contagion
  makes casualties arrive in correlated clumps *from a primitive*, at the tactical scale, per Jordan's
  own "cell is the primitive" directive. `PC_CELL_MORALE` is OFF and its one measurement was
  confounded. **Named falsifier:** if CV-vs-N still decays as O(1/√N) under the flag ON, the
  recommendation is wrong and the shared shock is right. That measurement does not exist yet — the
  plan's central claim is a hypothesis with a stated test, not a finding.

  **CRITICAL PATH — three steps, and everything expensive hangs off the third:**
  1. **A0 — finish the scalar-write sweep.** NOT hygiene, and not deferrable:
     `lanchester_signature.py` pins morale high *to disable rout*, so a silent no-op there measures
     the Lanchester exponent on **truncated** battles — and that exponent is what DG-6's entire
     root-cause analysis rests on. Deferring A0 doesn't delay the measurement, it **corrupts** it.
  2. **A2-step2 — re-measure cell morale honestly** (blocked on 1).
  3. **A1 — re-measure DG-6's CV-vs-N under cell correlation**, then decide `PC_FRICTION_SIGMA`:
     adopt / lower / drop. Three outcomes, all informative.

  **Ship without a ruling:** A4 (= ED-MB-0044) — R3 ranged closes into band **by ROLE**, reusing
  `_kite_goal` verbatim. No new mechanism, no new constant; it *removes* a special case. Narrowed by
  the adversarial pass: must be role-conditioned, since `hold` early-returning is plausibly correct
  for a deliberate holding order.

  **Parallel, no dependency:** A5 — unblock ED-MB-0008 (two live DR tables ~2× apart: **volley
  resolution is currently undefined**), ED-MB-0009 (orphaned fragment citing a never-existent
  `stage5_clocks.md`), ED-MB-0010 (the one-line emit deletion). All three diagnosed 2026-07-13.

  **Deferred ON PURPOSE (plan §3):** contract population (§3.1), typed MB params export (§3.2 — the
  exporter primitive exists but exports a *canonical oracle*, and ED-MB-0041 found only ~17 of ~92 MB
  magnitudes survive scrutiny). **§3.3 two-trees fork WEAKENED by the adversarial pass:** "two scales,
  two models" is a defensible architecture; the real defect is that the split is **undeclared** and
  `tests/sim/README.md` actively asserts the live tree is frozen run-output. Three options posed
  (declare / adapter / promote), recommending *declare* if the abstraction is intended — but note
  that under it, campaign-scale `mc_v18` conclusions are produced by the **stale** model and reflect
  none of A1–A4.

  **NEXT, in order:**
  1. **The empty contract — the port blocker.** `mass_battle` declares `consumes: []` and
     `state: []`; ripple returns **zero upstream in all four edge layers**. The typed wiring says a
     battle takes no inputs and persists nothing. This is *why* `formula_audit`/`pointer_audit` return
     zero MB rows and will keep doing so however often they run. 262 UPPER constants in the live
     engine; **40 (15%)** appear anywhere in `engine/params/` or the MB docs. **needs_jordan.**
  2. **The two-disjoint-trees fork.** `tests/sim/mass_battle/` (28 modules, ~10.5k LOC, 66 internal
     edges) has **zero production importers** and imports **nothing** from `engine/` or `systems/`;
     the wired `systems/mass_battle/sim/` has one importer (`faction_action.py:349`) and has not moved
     in 10 MB commits. ED-IN-0074 D5 says "reconcile before porting" — the measurement adds that there
     is **no shared substrate to reconcile onto**. Which tree is the port oracle, and does the live one
     leave `tests/`? **needs_jordan.**
  3. **Delete one line.** `scene_outcome.battle_concluded` is **not a Key** — it is the *family* name
     of `scene.battle_concluded`, duplicated into `mass_battle.emits`. Four instruments plus the
     Incompleteness Ledger report it as a real dangling/isolate Key; they agree because they share one
     blind spot (reading `module_contracts` without the Key Type Registry), which the authoritative
     graph resolves. Removing the row closes five findings at once. Held for an MB-lane call rather
     than bundled into a tooling PR.
  4. Lower priority: `Mass Battle`/`Mass Combat` alias tokens diverge on mu-degree (0 vs 23) and scale
     class (mechanic vs province) — one is wrong; `pp = 0` (the patch register has **no**
     case-insensitive match for the subsystem — MB work bypasses it entirely); 3 of 6 MB docs have no
     `## Status:` line and the `CURRENT.md` head is `WORKING DESIGN`, not `CANONICAL`.

  **Filed OUT of this lane (IN):** the same dead `sim/` root persists in the **A17 CI gate**
  (`ci_quantity_vocabulary_check --sim-root`), 11 dead `sim_module:` paths in `mechanics_index.yaml`,
  and four more tools (`audit_staleness`, `build_decisions`, `workplan_status`,
  `build_apparatus_registry`).

- **ED-MB-0044 (2026-07-26, FILED open/needs_jordan) — R3 is a DEFINITIONAL gap, not a balance one.**
  No longer a candidate: filed as a real ledger entry to end a dangling earmark that caused id churn
  twice (earmarked 0043 → renumbered 0044 → a reservation comment citing the unfiled id then failed
  the ED-citation-integrity gate). **⚠ Its proposed fix was UNDER-SCOPED — see ED-MB-0045 §5.2:**
  bypassing the `hold` early-return does nothing on its own (`STANCE_SPEED_MOD['hold'] = -99`
  independently zeroes `step`), `hold` is load-bearing for `freeze_wings`/refused-flank/
  `STANCE_COMMITMENT`, and `_kite_goal`'s band is inverted for melee. Recommended instead: change the
  R3 **scenario** (`stance='balanced'` + `kite`), not the engine's `hold` semantics. Ranged-vs-ranged is the only
  UNMEASURED gauge row: 100% draws at **0.0% casualties on both sides**, i.e. no engagement at all.
  Spawn distance is 18, `VOLLEY_MAX_RANGE` is 8, and `stance == "hold"` early-returns from *all*
  steering (both `_node_advance` and `advance_cells`), so neither archer body ever closes and
  `volley_phase` never fires. R1 resolves only because the infantry walks into range. The band-seeking
  primitive already exists and is live on the node path (`_kite_goal`: too close → flee, too far →
  close, in band → hold) but is gated on `'kite' in instructions`, which only `mounted_archers` carry.
  **Proposed fix:** for a missile body, `hold` means hold the *firing* position, not the spawn
  coordinate — a ranged subunit whose nearest enemy lies beyond `VOLLEY_MAX_RANGE` closes into the band
  by ROLE, reusing `_kite_goal` verbatim. No new magnitude, no new mechanism, no R3 special-case.

- **ED-MB-0039 (2026-07-24, needs_jordan): ENVELOPMENT STABILITY DIAGNOSIS — the ED-MB-0038 side-asymmetry
  root-caused.** Pure-infantry envelopment at strict parity is DEPLOYMENT-CHAOTIC: the parity centre (2
  cells) is narrower than the 3-command enemy (6) → out-flanked → a Lanchester-amplified knife-edge race
  whose tip is set by integer deployment parity (start-row sweep swings env win 54→50→17→9pp). Side-
  symmetric avg ~44% (envelop slightly LOSES); H3's 70.7 is the favourable side. Three regimes measured
  (`envelopment_stability_probe.py`): pure-infantry = chaotic ~44%±54pp; deep-narrow centre = stable
  (swing 51→7pp) but LOSES (bypassed — depth confers no holding without frontage; `width` alone is silently
  ignored, need `width`+`depth`); combined-arms (infantry pin + cavalry orbital-wheel rear, ED-MB-0035) =
  STABLE + side-symmetric + ~100% vs EVERY defender toughness. **Engine has two envelopment regimes and
  nothing between; the moderate 55-72/45-62 bands sit in an engine gap.** FORK for Jordan (both change
  history-grounded bands / a core mechanic; C4/C7 currently pass): **(A)** reframe H3/H4 as combined-arms
  (bands → ~75-100, loses inf/cav distinction) or **(B, recommended)** gated seal-failure/breakout variance
  → envelopment becomes a gradient (blast radius: lowers passing C4/C7 — needs A/B). Full write-up:
  `audit/2026-07-22-mass-battle-stress-test/envelopment_stability_diagnosis_v1.md`.

## 2026-07-24 — "Nothing is golden" campaign: Part-A flips + Part-B fixes (IN PROGRESS)

Jordan directive: *"implement all proposals. nothing is golden here."* The byte-exact golden constraint
is LIFTED — goldens become a re-recorded regression snapshot; the **honest gauge is now the primary
oracle**. Full steering doc + 6-phase plan: `audit/2026-07-22-mass-battle-stress-test/full_implementation_plan_v1.md`
(committed). Per-troop damage primitive (Jordan): troop = sub-cell isolate carrying weapon/quality/intent/
morale; density is LINEAR; the σ-head resolves per-troop quality → degree; count scales magnitude. This
resolves B4 = casualties-only-linear (behind a toggle). Decisions locked: PC_ flags KEPT; rotation DEFERRED.

**WORKING-TREE STATE (uncommitted): B1 applied to `tests/sim/mass_battle/geometry.py`** — the
`_oriented_abs_map` node branch now iterates `_oriented(atom)` (the continuous footprint _node_pos is keyed
by) and SKIPS absent ids instead of defaulting misses to origin `(0,0)`. **Verified:** H2 wedge decA
0.0 → 37.5 (audit predicted ~33). ✅

**CRITICAL COUPLING FOUND (do not commit B1 alone):** measuring the FULL gauge after B1 shows the
braced-wall C-rows REGRESS — C2/C6 `REPELLED` → `NOT-REPELLED` (cav wins 87.5% vs a braced wall), net
gauge 5/20 → 4/20. Root: the brace-repel silently relied on the broken `(0,0)`-collapsed contact map
feeding charge-shock / `_wall_prep` / `_defender_depth`; and the octagon-damage path
(`_per_cell_angle_mod`/`_octagon_dmg_mod`, orchestration ~L1156, zone binning ~L1021-1066) is STILL on the
dead `starting_position + cell_offsets` lattice (B3, unfixed) — so after B1 the contact map and the
octagon map DISAGREE. **The geometry frame (B1 + B2 + B3) and the B5 charge-zone fix are COUPLED through
the contact map and MUST land as ONE coherent set, measured together.**

**NEXT ACTION (resume here):**
1. B3 — route `_per_cell_angle_mod`/`_octagon_dmg_mod` onto the same live `_node_pos` identity map (kill
   the dead spawn-lattice open-code at geometry.py ~L259-262 path for these functions).
2. B5 — derive the charge/recoil zone (`_zb`/`_za`, orchestration L1021-1066) from the TRUE arc
   (`a_arc`/`b_arc`) not the `PC_REFUSE`-bundled `angle_mod`.
3. Re-measure the full gauge with B1+B3+B5 together; confirm C2/C6 return to REPELLED AND H2 stays fixed.
4. B2 — rebuild `col_grid` from live file bins per tick + re-center ANCHOR_MAP (H7/H8 fatigue-immunity).
5. Only when the frame set is NET-POSITIVE on the gauge: re-record bat.py goldens (4 modes) as the new
   baseline, update the byte-exact digest tests, run pytest, commit + ledger (ED-MB-0034), PR.

### 2026-07-24 continued — B1+B3 verified correct but NET-NEGATIVE on gauge alone (frame must land whole)

**Verified this increment (code preserved as `audit/2026-07-22-mass-battle-stress-test/frame_step1_B1_B3.patch`,
working tree reverted to keep the branch clean / avoid committing a gauge regression):**
- **B1** (geometry.py `_oriented_abs_map` node branch): iterate `_oriented(atom)`, skip absent `_node_pos`
  ids (no `(0,0)` default). **H2 wedge decA 0.0 → 40.0** ✅ (audit predicted ~33).
- **B1-grid** (same fn, grid branch): iterate `_oriented(atom)` not `oriented_pattern(shape,tier)` — matches
  `cell_offsets` keying (units.py: "_oriented is the sole source of the offset"); byte-identical for legacy
  troops=None. Makes `_oriented_abs_map` the SINGLE identity map. Add `_oriented_abs_map` to geometry `__all__`.
- **B3** (orchestration.py `_octagon_dmg_mod` L903 + `_per_cell_angle_mod` L748): replace the open-coded
  `abs_to_orig` (dead `starting_position+cell_offsets` lattice) with `abs_to_orig = _oriented_abs_map(defender_subunit)`.
  Live `_node_pos` on the field path; byte-identical on grid. H1 mirror → 52.5 (IN BAND).
- **make_unit** (gauge_mb.py): added `width`/`depth` params → spec (for deep-formation rows).

**KEY FINDING — the brace-repel (C2/C6) gap is DEEPER than B1/B3/B5:** with the contact map fixed, a braced
LINE cannot cleanly repel a charge. The reciprocal charge-recoil is depth-gated (`_wall_prep = _disc_prep ×
_depth_prep`; `_depth_prep(1)=0`, `(2)=0.33`, `(3)=0.67`), but the density-matched gauge units are only 2
ranks. Scaling depth at EQUAL FORCE: cav-win 62% (d2) → 40% (d6) → 70% (d8) — depth helps but a narrow-deep
line gets FLANKED by the wider wedge (envelopment), so it never cleanly repels. **A repelling formation is a
SQUARE/BOX (all-around brace), not a frontal deep line.** So C2/C6 need: (a) **B5** (charge/recoil zone from
the true arc, not the PC_REFUSE-bundled angle_mod), AND (b) a **box/square brace primitive** (all-around
facing), AND (c) gauge C-rows scaled up (bigger, deeper, fair force). The old brace-"repel" was an ARTIFACT
of the broken `(0,0)`-collapsed contact map — B1/B3 correctly remove it and expose the real gap.

**Full gauge with B1+B3 alone = 4/20 (was 5/20)** — net -1 because C2/C6 flip (brace-model gap) while the
H-rows improve directionally but aren't yet in band (need B2 + the brace/box work). **CONCLUSION: the
geometry frame (B1+B2+B3) + B5 + the box-brace primitive + the gauge C-row rescale must land as ONE
net-positive set — no piecemeal geometry commit reaches net-positive.** Next increment: apply
`frame_step1_B1_B3.patch`, then build B2 (col_grid live), B5 (arc zone), the box-brace primitive, and the
gauge C-row rescale together; measure the full 20-row gauge; re-record 4 goldens; land as ED-MB-0034.

### 2026-07-25 — ED-MB-0041 Tier-2 executed (dead machinery wired or deleted); gauge multi 5/20 → 10/20

**Shipped.** Seven Tier-2 items from `audit/2026-07-22-mass-battle-stress-test/adversarial_deep_audit_v1.md`
§4, all with regression tests verified to FAIL against the pre-fix code:

| item | verdict |
|---|---|
| `dynamic_facings` | **deleted** — write-only parallel facing store, zero readers; `cell_facing_vec` supersedes it |
| `_front_fixers` | **hoisted to full-tick scope** — was per cascade group, so the Cannae fixing-force never fired |
| `cell_last_speed` | **impulse + charger-role latch** — halted/`hold` cells record 0; the braced-wall repel now latches the charger role at impact instead of re-deriving it from a per-tick differential |
| `col_grid` | **rebuilt from live cells** — membership was frozen at spawn, so fatigue and depth-absorption both returned 0.0 for any moved body |
| rout triggers | **aligned on the tick clock** — the annihilation trigger lagged up to 5 ticks behind morale collapse |
| `PC_WHEEL` | **ported to `_node_advance`** — shipped ON, was a no-op; this fixed H6's 0.0/0.0-casualty broken instrument |
| `yielding` | **cleared at the battle boundary** — the one DG-2 transient the reset missed |

Plus **24 dangling `sim_verification_ledger.json` citations retagged `CALIBRATED-DEBT`** (Tier-0.1 deleted
that file; the tags still pointed at it as `canonical:`). Goldens re-recorded, both grid modes.

**Correction carried in the record:** I first wrote the momentum item up as a Tier-3 punt, believing the
impulse cost gauge row C1. Bisecting a clean pre-Tier-2 tree showed C1 was **already 86.7%** at baseline and
the impulse brings it to **48.3%, in band**. The audit doc §7.1 and the coverage-matrix entry both carry the
correction rather than the original claim.

**Gauge (multi) 10/20.** In band: H1 H2 H3 H7 H8 H11 C1 C3 C5 C7. Out: H4 H5 H6 H9 H10 R1 R3 C2 C4 C6.

### Next actions (MB)

1. **Reverse-row asymmetry.** H3 (Envelopment vs Line) 61.0 and its reverse H10 76.7 are the same physical
   matchup with the armies swapped between slots; complementary bands mean they should sum to ~100 and they
   sum to ~138. H2/H9 sum to 114. The mirrors are clean (H1 50.0, C3 50.8), so this is matchup-specific, not
   a uniform slot bias. Undiagnosed — this is the largest single cluster of remaining failures (4 rows).
2. **H5/H6 RefusedFlank = 100%.** Newly *live* rather than newly broken (H6 previously produced literally
   zero casualties across 60/60 seeds). Direction is historically right — the oblique order is supposed to
   win — but 100% is not. Check whether the ported overhang wheel is too permissive for a wing that is
   deployed wide of the enemy frontage by construction.
3. **C2/C6 still NOT-REPELLED — and it is NOT a magnitude problem. [CORRECTED 2026-07-25 by the sweep;
   my earlier entry here was wrong.]** I recorded this as "the latch removed the timing problem, what
   remains is magnitude — `PC_CHARGE_RECOIL=6` and `SIGMA_PER_D=0.2`", and queued it for Jordan as a
   magnitude call. The sweep falsifies that:

   | lever | C2 result | band |
   |---|---|---|
   | `PC_CHARGE_RECOIL` 0 / 3 / 12 / **24** (4x default) | 100.0 / 93.8 / 87.5 / **87.5** | 0-30 |
   | `SIGMA_PER_D` 0.1 / 0.4 / 0.8 | 93.8 / 93.8 / 93.8 — **totally insensitive** | 0-30 |
   | `PC_BRACE_ENABLED` off / on | 100.0 / 93.8 | 0-30 |

   Quadrupling the recoil buys 6 points of the ~64 needed, and switching the entire brace apparatus OFF
   costs only 6. So the whole braced-wall mechanism contributes ~6 points to a row that needs ~64 — the
   coefficient is not the binding constraint, the mechanism is. **This retires a Tier-3 magnitude call
   and replaces it with a mechanism gap:** a frontal deep line cannot repel a charge in this engine at
   any coefficient. (Consistent with the older finding already in this file that a repelling formation
   is a SQUARE/BOX with all-around brace, not a frontal deep line.)
4. **Tier-3 list** (`adversarial_deep_audit_v1.md` §4) is otherwise untouched and needs Jordan: depth
   support-stack cap, envelopment-as-morale-collapse, graded cavalry charge refusal, the Biddle σ-ceiling,
   the rout band + `PC_STOCHASTIC_ROUT` default, the `YIELD_POOL_MULT` split, and the missing
   disengage-and-recharge cycle (new, §7.1).

### 2026-07-25 — reachability sweep: 20/20 is NOT reachable by constants (audit §8)

Jordan asked whether some combination of constants gets the honest gauge to 20/20. Answered
empirically with `audit/2026-07-22-mass-battle-stress-test/reachability_sweep.py` (85 configs/row,
greedy stacking). **No.** Of the ten failing rows: **H5** legitimately reachable
(`PC_FRICTION_CEV=1 + PC_FRACTIONAL_POOL=1` → 48.3 OK); **H4** and **H9** reachable only by disabling
the mechanism under test (`PC_ENVELOP_PATH=0` passes Cannae) or refitting an already-fitted constant
(`K_LINEAR=24`); **H6, H10, R1, R3** have no reachable configuration at all. Full table in audit §8.2.

**Two instrument defects were found and fixed before the results were trusted** — both worth knowing:
- **Low-n positives are noise, asymmetrically.** R1's identical baseline reads 26.7/OK at n=16 and
  44.1/WIN-OUT at n=60. Noise only WIDENS a span, so negatives survive low n and positives do not.
  Every positive here was re-verified at n=60; four of H10's and both of R1's evaporated.
- **Ragged band parse.** Braced-repel rows carry a 10th `'rawA'` field, so counting from the end read
  C2's band as (30,'high') instead of (0,30) — wrong for exactly the cavalry-repel rows.

### Next actions (MB) — revised priority after the sweep

1. **Band casualties and duration, not just win-share.** `gauge_mb.py:417,421` already computes
   `a_cas`/`b_cas`/mean turns and bands none of them. This is now the top item: the sweep showed the
   cheapest route to a green row is to switch off the mechanism the row measures, and a casualty-banded
   gauge rejects that immediately (two lines colliding do not produce Cannae's casualty asymmetry).
   All 20 current bands are judgement calls with no literature-derived interval; casualty ratios and
   duration are what the sources actually constrain.
2. **Side-symmetry invariant test.** H2/H9, H3/H10, H4/H11 are the same matchup with the armies
   swapped, on exactly complementary bands, so their sums must be ~100; they are 114.2, 137.7, 61.7.
   Needs no history — swap the sides, the answer must invert. Cheapest high-information test available
   and it fails today. (H10 having ZERO reachable configs is the same finding from the other side.)
3. **Reachability gate in CI.** Assert each named mechanism fires at least once in a canonical
   scenario. Its absence produced six Tier-2 findings in one pass.
4. **Give the cell real state — morale first.** Per-cell state today is position/facing/halted/
   last-speed/troops. There is no per-cell morale, discipline, quality, stamina or rout, so Jordan's
   directive ("a cell should be able to have worse morale than another cell in same subunit") is not
   implemented, and of the five modulators named for a cell's damage output only density is per-cell.
5. **Collapse the column tier into the cell.** Fatigue/stamina/depth-rotation live on `col_grid` — a
   third granularity that is neither the primitive nor the holistic body (shape divergence).
6. Mechanism gaps: charge/recoil/re-charge cycle; a resolution path for the ranged mirror (R3); local
   (per-cell) break rather than whole-subunit rout.


### 2026-07-25 — instruments built; PC_STOCHASTIC_ROUT ratified ON; symmetry largely resolved

Jordan approved the two instruments and granted Tier-3 experiment permission. Both built
(`reverse_pair_symmetry.py`, casualty/duration scoreboard in `gauge_mb`, `test_gauge_invariants.py`).

**Ratified:** `PC_STOCHASTIC_ROUT` default OFF -> ON. Loser casualties 61-87% -> 29-41% (band 15-30);
win-share 10/20 -> 7/20 and the flip is still right. Both grid goldens re-recorded. Full suite green
(593 passed).

**Unpredicted second effect:** the flip also largely fixed the reverse-pair side-asymmetry — H3/H10 went
+4.5σ -> +1.7σ (resolved), H2/H9 +1.6σ -> +0.3σ, H4/H11 -5.3σ -> -3.8σ. The asymmetry was substantially
an artifact of battles running to annihilation, not an independent deployment-geometry bug. **H4/H11 at
-3.8σ is the surviving symmetry defect.**

**Held:** `ROUT_CASCADE_FRAC` (du Picq contagion) built and gated inert at 1.0. ⅔-of-line gives casualty
5/20 and fixes H6's 79.2% outlier; ⅓-of-line gives 7/20 but costs a win-share row and makes H6
undershoot. Not chosen, because per-cell state redefines what a "section" is.

### Next actions (MB)

1. **Per-cell state (Jordan directive).** Morale first. The contagion experiment pointed here
   independently: H1/H2/H7/H8/H9 are unmoved by ANY contagion threshold because they are single-subunit
   armies — no line to come apart. Their residual 30-33% loser casualties is the gap per-cell break closes.
2. **H4/H11 −3.8σ** — the surviving side-asymmetry, now isolated from the lethality confound.
3. **Re-decide `ROUT_CASCADE_FRAC`** once per-cell granularity lands (the "section" it counts changes).
4. Remaining Tier-3: box/square all-around brace (C2/C6 — mechanism, not magnitude, §8.4); ranged-mirror
   resolution path (R3, the only UNMEASURED row); disengage-and-recharge cycle.

---

## [OPEN] ED-MB-0065 — J2 is ruled-but-not-executable; record corrected, nothing deleted (2026-08-08)

**Do not delete `systems/mass_battle/sim/` without reading this.** J2 (2026-08-03) retired it; the
2026-08-04 CURRENT.md stamp recorded that as done. It was not done, and it is not doable as written.

**Three independently sufficient blockers, measured:**
1. **The retired tree holds the campaign's only faction-scale seam.** `engine/mc_v18.py` →
   `faction_take_action` → `_try_conquest` (`faction_action.py:431`) →
   `resolve_mass_battle(faction_a, faction_b, terrain, world)`. Runs every season. Deleting it
   breaks Military Conquest.
2. **The canon tree cannot receive that call.** `tests/sim/mass_battle/` is unit/geometry-scale and
   **cell-based**; the retired tree is the pre-cell v22 model. Feeding canon's `run_battle` a unit
   from `_faction_to_unit` raises `AttributeError: 'Subunit' object has no attribute 'cells_float'`.
   The two `run_battle` docstrings are identical — canon is a descendant fork that diverged at the
   cell model.
3. **A later ruling already kept it.** ED-IN-0127/0128 (2026-08-04, *one day after J2*) pin
   `systems/mass_battle/sim/massbattle.py` as `keep`, guarded by `test_evacuation_plan.py`.

**What executing J2 actually costs:** a strategic → cell-based-`Unit` adapter. `_faction_to_unit`'s
docstring already concedes *"[GAP: no canonical spec for faction.Mil → Unit construction]"*, so the
adapter needs a spec before it needs code.

**Guard:** `tests/valoria/test_j2_mass_battle_seam.py` — a **disjunction**, green in the current
state *and* after a completed migration, failing only on the half-done state. Mutation-verified:
deleting the tree while `faction_action` still imports it fails it.

**Next action — Jordan's call, three options:**
- **WITHDRAW** — accept the later keep-set; the trees coexist (canon tactical, `systems/` strategic
  seam) and the "not kept alongside" clause is struck.
- **DEFER** — J2 stands as intent, gated on the adapter + a canonical `faction.Mil → Unit` spec.
- **EXECUTE-WITH-SCOPE** — build the adapter as MB work, then delete.

This item takes none of the three. It only stops the record claiming the deletion happened.
