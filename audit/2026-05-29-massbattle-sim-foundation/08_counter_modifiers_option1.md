# Mass Battle Sim — M3 §3c Milestone: Option 1 Executed (Strengthen the §A.6 Counter Differential)

**Date:** 2026-05-29
**Skill:** valoria-simulator (NERS framing: valoria-resolution-diagnostic)
**Scope:** simulation
**Session token:** df5079812d207c7e
**Builds on:** `07_massbattle_counter_tension.md` (the casualty↔counter tension; §7 option 1 chosen by Jordan)
**Status:** MILESTONE — option 1 is **validated** as the right mechanism. Counters now decide at realistic casualties (8/11, casualty-neutral) vs the lineage's 5/11 ceiling. The residual 3 misses are isolated to a named **geometric** defect, not a tuning gap. **Proposed counter-modifier values are surfaced for Jordan ratification — NOT committed to canon §A.6.**

`[SELF-AUTHORED — bias risk]` Engineering executed by me this session; the strengths below were tuned against the gauge and could over-fit the 11 matchups — the challenge surface is §6. The proposal does not change canon; it proposes values for Jordan to accept/adjust.

---

## VERDICT

Jordan chose §7 option 1: strengthen the formation-counter modifiers so a formation advantage **decides within the realistic casualty budget** rather than requiring a grind to catastrophic casualties. Executed on the realistic-casualty D-B base (v22_DB).

**Root cause found:** v22_DB has `SHAPE_OFF_MOD`/`SHAPE_DEF_MOD` tables wired into the offence pool — **but they are zeroed** (engine line 144: "flat per-shape bonuses removed"). The §A.6 dice differentials canon specifies (Wedge +2D off / −1D def vs Line) were deliberately removed; the engine relied on pure emergent cell-geometry. **That is exactly why the counters were too weak to decide at realistic casualties** — most of them were not expressed as a differential at all.

**Result of re-populating the differential (as a matchup-aware, casualty-neutral damage multiplier):**
- **8/11 melee in-band at realistic casualties** (loser ~36% / ≈26% per-side, draws <12%) — a clean **+3 over the entire v9–v25 lineage's 5/11 ceiling**.
- **Casualty-neutral:** loser casualties stay 34–38% across every counter strength tested (the modifier shifts *who routs first*, not *how many die* — the historical asymmetry). **The catastrophic-casualty dependence identified in `07` is broken.**
- The **finer damage-multiplier channel** (in-idiom with v25's `ANGLE_DMG_MULT`) is required; the integer dice-pool channel plateaus at ~6/11 because a +1D step is too coarse at these pool sizes.

**The residual 3 misses (H3, H7, H10) are GEOMETRY-capped, not counter-tunable.** All three are off-band *at zero counter strength* (pure v22 geometry: H3 66.7%, H7 70.0%, H10 31.7%). The Horseshoe and GappedLine shapes vs Line are intrinsically over-strong; an additive-advantage counter cannot pull an already-over-strong forward matchup *down*. Reaching ≥10/11 requires a **targeted geometry fix** to the Horseshoe/GappedLine-vs-Line contact pattern (or an asymmetric forward/reverse counter), which is a separate, scoped piece — and the geometry is Jordan-authored, so the fix direction is a design call.

---

## §1 — Mechanism (read, grounded)

`[READ: designs/provincial/mass_battle_v30.md §A.6 (287–321) + §A.8 (439–463) + flanking/terrain/stance modifiers]`
- **§A.6 gives explicit dice modifiers for only Wedge (+2D off / −1D def vs Line) and Shield Wall (−1D off / +2D def).** Line/Skirmish are "Normal." Horseshoe, GappedLine, RefusedFlank have **no §A.6 line modifier** — they appear in §A.8 as *tactics* (Envelopment, Refused Flank) gated behind Command checks and "requires Fast," or are pure geometry. So the historical-band shapes that fail (envelopment, manipular, oblique) were mechanically unmodeled as counters.
- **§A.8** confirms the counter directions: Envelopment (Ob 2, "requires Fast") countered by Refused Flank; this matches the v9 bands (Cannae, Leuctra).

`[READ: sim_mb_06_v22_DB.py — SHAPE_OFF_MOD/SHAPE_DEF_MOD (426–435, all zeroed), pool injection (1259–1287), engagement damage (1359–1360), dice engine roll_pool/compute_degree/DAMAGE_BY_DEGREE (1039–1055)]`
- The zeroed tables are added to the offence pool at `a_pool = max(1, floor(pool_raw) + off_a)`. The injection point is live; only the values were nulled.

**Two channels tested:**
1. **Dice-pool add** (`sim_mb_06_v22_DB_ck.py`): re-populate `SHAPE_OFF_MOD` as a matchup-aware `COUNTER_MATRIX`. At canonical Wedge=+2 the counters *overshoot* hard (H2 85%, H7 98%); below +1D the integer floor rounds to zero. **Plateaus at ~6/11** — the dice step is too coarse for fine placement. This is itself a finding: the pool granularity cannot finely calibrate counters at Company scale.
2. **Damage-multiplier** (`sim_mb_06_v22_DB_cm.py` → promoted to **`sim_mb_06_v26_counters.py`**): express the counter as a smooth multiplicative damage differential `dmg_to_opponent *= (1 + strength)`. Continuous, so sub-1D-equivalent strengths act. **Reaches 8/11.** This is the deliverable engine.

---

## §2 — Result at realistic casualties (the corrected bar)

The bar from `07` is **≥10/11 at realistic casualties** (~26% per-side, draws <15%) — NOT the old "9/11 at catastrophic." Best damage-multiplier configuration, single mode, n=60:

| # | Matchup (historical) | Band | A% | draw% | loser cas% | verdict |
|---|---|---|---|---|---|---|
| H1 | Line v Line (mirror) | 45–55 | 50.0 | 5.0 | 34 | **OK** |
| H2 | Arrowhead v Line (cuneus) | 50–65 | 58.3 | 3.3 | 36 | **OK** |
| H3 | Horseshoe v Line (envelopment) | 50–65 | 75.0 | 0.0 | 36 | **X** (geom) |
| H4 | Horseshoe v Arrowhead (**Cannae**) | 40–60 | 46.7 | 6.7 | 38 | **OK** |
| H5 | RefusedFlank v Horseshoe (Leuctra) | 50–65 | 60.0 | 5.0 | 36 | **OK** |
| H6 | RefusedFlank v Line (oblique) | 45–60 | 50.0 | 11.7 | 36 | **OK** |
| H7 | GappedLine v Line (**Pydna**) | 50–65 | 76.7 | 3.3 | 35 | **X** (geom) |
| H8 | GappedLine v Arrowhead | 45–60 | 45.0 | 3.3 | 36 | **OK** |
| H9 | Line v Arrowhead (rev H2) | 35–50 | 40.0 | 1.7 | 36 | **OK** |
| H10 | Line v Horseshoe (rev H3) | 35–50 | 20.0 | 3.3 | 38 | **X** (geom) |
| H11 | Arrowhead v Horseshoe (rev H4) | 40–60 | 46.7 | 0.0 | 37 | **OK** |

**8/11 melee in-band; loser casualties 34–38% (≈26% per-side); draws ≤11.7%.** Mirror is a clean 50/50 at 34% — the over-annihilation that disqualified v23/v14 is gone.

**Casualty-neutrality (the load-bearing property):** across global strength K = 0.5 → 2.0 and every per-matchup grid cell, loser casualties stayed **36–37%**. The counter changes the win-rate, not the casualty level. This is what the prior lineage could not do and what makes option 1 historically faithful (a decisive formation victory still costs the *loser* ~30%, the *winner* less — the Cannae asymmetry, not mutual annihilation).

---

## §3 — Why the last 3 are geometry, not tuning

CM=0 baseline (pure v22 geometry, the state the counter corrects *from*), per matchup:

| # | Matchup | A% @ CM=0 | In band? | Counter can fix? |
|---|---|---|---|---|
| H3 | Horseshoe v Line | **66.7** | no (already >65? in-band edge, climbs with any counter) | **No** — additive counter only pushes higher |
| H7 | GappedLine v Line | **70.0** | no | **No** — already above band at zero |
| H10 | Line v Horseshoe (reverse of H3) | **31.7** | no (below 35) | **No** — reverse of an over-strong forward matchup |

H3, H7, H10 are off-band *before any modifier*. The damage-multiplier counter only *adds* advantage to the designated attacker, so it cannot reduce H3/H7 (already too strong) and cannot lift H10 without also over-lifting H3 (same Horseshoe-vs-Line shape pair, opposite sides). **Root cause: the Horseshoe and GappedLine contact geometry vs a Line concentrates too many cell-adjacencies, inflating the forward matchup regardless of the dice/damage counter.** That is a geometry defect in `cell_pattern`/`role_at_contact` for those shapes against Line — fixable, but a different lever (reduce Horseshoe/GappedLine effective contact width vs Line, or apply an asymmetric forward/reverse counter), and Jordan-authored geometry.

---

## §4 — Historical validation

`precedents_warfare.md` §1.2/§6: the formation-counter system and "generalship dominates" axiom are historically correct; Cannae is the canonical envelopment. The 8 in-band matchups now reproduce the precedent at historically-correct casualties — wedge breaks line (H2), envelopment beats wedge at Cannae (H4), refused flank counters envelopment at Leuctra (H5), oblique edges line (H6), maniple edges wedge (H8), and the reverses (H9/H11) sit correctly low. The 3 geometric misses are *over*-counters (H3/H7 envelopment & manipular winning ~75% vs a ~55–60% target) — i.e. the right *direction*, wrong *magnitude*, capped by geometry. Historically envelopment and manipular flexibility WERE decisive (Cannae ~58% loser; Pydna routed the phalanx), so ~70% is not absurd — it is above the *band*, which the v9 spec sets for equal-quality non-catastrophic engagements. Tightening it is calibration on the geometry side.

---

## §5 — Proposed counter modifiers (PROPOSAL — Jordan ratifies; NOT committed)

Re-populate the §A.6 differential the engine zeroed. Two equivalent expressions; the damage-multiplier form is what reaches 8/11. Values are the tuned best from this session, anchored on canon (Wedge):

| Attacker vs Defender | Canon §A.6 | Proposed dmg-mult (× damage to defender) | Historical basis |
|---|---|---|---|
| Arrowhead (Wedge) v Line | +2D off / −1D def | **+20–35%** | cuneus breaks line (canon) |
| Horseshoe (Envelop) v Line | *(unmodeled)* | **+15–30%** *(geometry already over-delivers; small)* | Cannae pattern |
| Horseshoe v Arrowhead (Cannae) | *(unmodeled)* | **+15–20%** | §A.8 envelopment > single-axis |
| GappedLine (Maniple) v Line | *(unmodeled)* | **+10–15%** *(geometry over-delivers; small)* | Pydna |
| GappedLine v Arrowhead | *(unmodeled)* | **+10%** | maniples absorb+flank wedge |
| RefusedFlank v Horseshoe | *(unmodeled)* | **+20–25%** | Leuctra (§A.8 named counter) |
| RefusedFlank v Line | *(unmodeled)* | **+5–8%** | oblique slight edge |

These would become a canonical **formation-counter matrix** patch (PP-NNN) extending §A.6 beyond Wedge/Shield-Wall to the envelopment/manipular/oblique counters. **The exact magnitudes are a design choice** — I have shown the band these produce; Jordan sets the canonical numbers (and whether to express them as dice modifiers, damage multipliers, or geometry).

---

## §6 — Independent-reviewer challenge surface `[SELF-AUTHORED — bias risk]`

1. **"8/11 is over-fit to 11 matchups."** Partly fair — the strengths were tuned against the gauge. Mitigations: (a) the in-band set is *robust* across a wide grid (the top grid region is broad, not a knife-edge), (b) the strengths are small and monotone (no per-matchup hacks beyond one strength per shape-pair), (c) casualty-neutrality holds across all of it (not a tuned coincidence), (d) the misses are explained structurally (geometry), not waved away. `[CONFIDENCE: high on "counters now decide at realistic casualties"; medium on the exact 8/11 and the specific strengths]`
2. **"You picked the damage-mult channel because it scored better — is that legitimate?"** It is in-idiom (v25's `ANGLE_DMG_MULT` is the same lever class) and the *reason* it scores better is principled (continuous vs the dice-pool integer cliff), not arbitrary. The dice-pool channel's ~6/11 plateau is reported, not hidden.
3. **"Are H3/H7 really geometry-capped, or did you under-tune?"** Directly shown: both are off-band at CM=0 (zero counter). An additive-advantage counter is monotone-increasing in the attacker's win-rate, so it provably cannot reduce an over-strong forward matchup. The proof is structural, not empirical.
4. **"Casualty-neutrality might be an artifact of CASUALTY_SCALE=20."** The neutrality is mechanistic: rout fires at morale ≤ 0, and morale erodes on `dmg/(disc×cmd)` → the *loser* always routs at ~its threshold casualties regardless of the counter; the counter only changes *which* side reaches threshold first. CS sets pacing, not the rout fraction (established in M2 + `07`).

---

## §7 — Next steps

- **Jordan decision (1):** ratify the §A.6 counter-matrix proposal (§5) — accept/adjust the magnitudes and the expression (dice mod vs damage mult). Blocking for committing the values to canon.
- **Jordan decision (2):** authorize the Horseshoe/GappedLine-vs-Line **geometry fix** to clear H3/H7/H10 toward ≥10/11 (reduce those shapes' effective contact width vs Line, or asymmetric forward/reverse counter). Geometry is Jordan-authored; direction is a design call. This is the path from 8/11 → ≥10/11.
- **Then 3c-final:** re-tune the counter matrix on the corrected geometry and validate ≥10/11 at realistic casualties.
- **M4+ unchanged:** multi-turn dynamics (D-A L2; v26 inherits v22's `run_multi_turn_battle` — validate single≈multi under the counters), ranged (R1/R3), canon reconciliation.
- **Commit:** B6 resolved; `github_ops.py` re-fetched. This doc → `designs/audit/2026-05-29-massbattle-sim-foundation/08_counter_modifiers_option1.md`; the engine `sim_mb_06_v26_counters.py` → `tests/sim/` — both via `safe_commit` on Jordan's OK. The `_ck`/`_cm` variants are diagnostic scaffolding (keep local). Do **not** commit the §5 values to `mass_battle_v30.md` without ratification (owner contract).

---

### Audit trail
- `[READ: mass_battle_v30.md §A.6 + §A.8 + modifiers]` · `[READ: sim_mb_06_v22_DB.py — SHAPE_OFF/DEF_MOD, pool injection, dmg lines, dice engine]` · `[READ: precedents_warfare.md — all 326 lines, prior turn]`
- `[ASSUMPTION: base = v22_DB — option 1 is "a mechanics edit, not a base swap"; v22_DB is the realistic-casualty, multi-turn D-B engine]`
- `[FIXED: #1 — re-populated the zeroed §A.6 counter differential; counters now decide at realistic casualties (5/11 → 8/11)]`
- `[CONFIDENCE: high — option-1 mechanism validated + casualty-neutral; medium — exact 8/11 and the specific strength values (tuned, ratification-pending); high — H3/H7/H10 are geometry-capped]`
- `[GAP: Horseshoe/GappedLine-vs-Line geometric over-strength — off-band at zero counter; needs a geometry fix to reach ≥10/11; Jordan-authored geometry, direction is a design call]`
- `[GAP: ED-875 low-Command sigma-leverage — same low-pool/Command region as the erosion/generalship mechanics; unverified interaction with the counter strengths]`
- `[DRIFT: B6 resolved on main; github_ops.py re-fetched]`
- `[PASS-3: verdict stands — option 1 validated; counters decide at realistic casualties (8/11, casualty-neutral); residual 3 are a named geometry defect; proposed §A.6 values surfaced for Jordan, not committed]`
