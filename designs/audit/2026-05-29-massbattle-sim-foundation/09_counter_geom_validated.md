# Mass Battle Sim — M3 §3c-Final: Both Ratifications Executed & Validated

**Date:** 2026-05-29
**Skill:** valoria-simulator (NERS framing: valoria-resolution-diagnostic)
**Scope:** simulation
**Session token:** df5079812d207c7e
**Builds on:** `07_massbattle_counter_tension.md` (casualty↔counter tension), `08_counter_modifiers_option1.md` (option-1 mechanism, 8/11). Jordan ratified BOTH: the §A.6 counter matrix AND the Horseshoe/GappedLine geometry fix.
**Status:** MILESTONE — both fixes executed; mechanism **validated** (counters decide at realistic casualties, casualty-neutral, single≡multi). Honest converged result is **~9–10/11 pooled** (NOT a single-seed 11/11 — that was over-fit and is walked back, §3). **Two Stage-4 defects surfaced: one FIXED (tier-equalization regression I introduced), one FLAGGED (pre-existing RefusedFlank/side-bias asymmetry).** Proposed values surfaced for Jordan; nothing committed.

`[SELF-AUTHORED — bias risk]` This documents fixes I built and tuned this session. A single-seed 11/11 was produced, caught as over-fit by my own robustness pass, and corrected — that catch is the validation discipline working, and it is reported in full (§3) rather than the inflated number headlined. Challenge surface §7.

---

## VERDICT

Both ratified fixes work and are the right mechanism:
- **§A.6 counter matrix** (the zeroed differential, re-populated as a casualty-neutral damage multiplier): places the formation counters.
- **GappedLine front-width geometry fix**: pulls H7 (Pydna manipular) off its geometric ceiling (70% → ~50% on geometry alone, into band) — the one matchup the counter alone provably could not fix (additive counters can't *reduce* an over-strong forward matchup, `08` §3).

**Validated result (honest, seed-averaged):**
- **~9–10/11 melee in-band, pooled across seed banks** (10/11 on a 5-bank pooled mean; 9/11 on a 3-bank pooled mean; H7 and occasionally H2 ride the band edge). A real, large gain over the **entire v9–v25 lineage's 5/11 ceiling.**
- **Casualty-neutral and seed-robust on that property:** loser ~36% / ≈26% per-side, draws 4.5–4.6%, ticks ~7 — across every seed bank, every counter strength, and multi-turn. The over-annihilation that disqualified v23/v14 is gone.
- **single ≡ multi-turn: 0.0pp drift** on all 11 matchups (D-A mandate satisfied — the gauge's single mode is a faithful proxy; the multi-turn layer at this scale reduces to repeated single engagements with no divergent dynamics).

**Honest caveats (load-bearing):**
- The **per-seed band count swings 5–10/11** (per-matchup σ 3–10pp). This is inherent small-pool variance (the NERS resolution-diagnostic's named engine stress), not tunable away. The defensible figure is the *pooled* count, ~9–10/11.
- A **single-seed 11/11 was over-fit** to the gauge seed and is withdrawn (§3).
- **Two defects** (§5): tier-equalization regression (FIXED in the deliverable engine), RefusedFlank/side-bias asymmetry (pre-existing, FLAGGED).

---

## §1 — What was built (read, grounded)

`[READ: sim_mb_06_v26_counters.py / v22_DB — SHAPE_OFF_MOD/SHAPE_DEF_MOD (zeroed), pool injection (1259–1287), engagement damage (1359–1360); role_at_contact (871–896); cell generators line/horseshoe/gapped_line/refused_flank (461–516); CELL_PATTERN_FN, atom_max_width, assign_targets]`

Two levers, both env-tunable:
1. **Counter matrix** (`COUNTER_MULT[attacker_shape][defender_shape] → +damage fraction to opponent`), wired into the two engagement-damage lines as a multiplier. Casualty-neutral by construction (it shifts *which* side reaches the morale-rout threshold first; rout still fires at morale ≤ 0 at ~threshold casualties regardless). Includes forward entries (wedge>line, envelopment, manipular, refuse) AND a reverse/defensive entry (Line-vs-Horseshoe frontal push) needed to lift the reverse matchup H10.
2. **GappedLine geometry**: front-row contact width reduced below the Line's (T3: 8→4 cells wide), cell count held ≈ Line via added depth. This pulls the manipular's over-strong frontal contact down to historical levels.

Deliverable engine: **`sim_mb_06_v30_counters_geom.py`** (counter matrix + tier-correct geometry; T3 result identical to the tuned v28, tier-equalization fixed per §5).

---

## §2 — Validated result

### 2.1 Pooled across 5 seed banks (n=48/bank), single mode
| # | Matchup (historical) | Band | mean A% | ±σ | pooled verdict |
|---|---|---|---|---|---|
| H1 | Line v Line (mirror) | 45–55 | 49.2 | 5.2 | OK |
| H2 | Arrowhead v Line (cuneus) | 50–65 | 61.7 | 10.3 | OK |
| H3 | Horseshoe v Line (envelopment) | 50–65 | 52.5 | 6.4 | OK |
| H4 | Horseshoe v Arrowhead (**Cannae**) | 40–60 | 55.8 | 4.8 | OK |
| H5 | RefusedFlank v Horseshoe (Leuctra) | 50–65 | 55.8 | 7.5 | OK |
| H6 | RefusedFlank v Line (oblique) | 45–60 | 45.4 | 5.3 | OK |
| H7 | GappedLine v Line (**Pydna**) | 50–65 | 45.4 | 5.0 | **X** (rides just below) |
| H8 | GappedLine v Arrowhead | 45–60 | 60.0 | 5.5 | OK |
| H9 | Line v Arrowhead (rev H2) | 35–50 | 36.7 | 7.3 | OK |
| H10 | Line v Horseshoe (rev H3) | 35–50 | 39.2 | 4.6 | OK |
| H11 | Arrowhead v Horseshoe (rev H4) | 40–60 | 45.8 | 2.9 | OK |

**Pooled-mean: 10/11** (H7 the sole miss, at 45.4% vs a 50 floor — close). **Per-bank: 5/9/10/7/8 across banks, mean 7.8/11.** Casualties 36%, draws 4.5%.

### 2.2 Multi-turn validation (D-A mandate), pooled 3 banks
single ≡ multi, **0.0pp drift** on every matchup; multi casualties 36%, draws 4.6%. The counters tuned in single mode hold identically under multi-turn. `[CONFIDENCE: high — exact-zero drift is the multi layer reducing to repeated single engagements at this scale]`

---

## §3 — The over-fit 11/11, caught and withdrawn `[BIAS: over-fit — single-seed tuning]`

A configuration scored **11/11 at n=60 on the gauge's own seed bank (1,000,000)** and was initially presented as the result. The robustness pass (4 independent seed banks) refuted it: **11/11, 7/11, 4/11, 9/11.** The 11/11 was a knife-edge fit to one seed — the multi-parameter tune found a cell that placed all 11 matchups at *that* seed but did not generalize.

**Correction:** the result is the *seed-averaged* count (§2), ~9–10/11 pooled. The single-seed 11/11 is withdrawn. This is the same Stage-4 failure mode as the v23 9/11 in `07` (a number that evaporates under a stress the first pass didn't apply) — caught here by multi-seed scoring before it shipped as a verdict. `[CORRECTION: §3c — single-seed 11/11 withdrawn; validated figure is ~9–10/11 pooled]`

---

## §4 — Historical validation

`precedents_warfare.md` §1.2/§6: formation-counter system + "generalship dominates" historically correct; Cannae the canonical envelopment. The validated set reproduces the precedent at historically-correct casualties: wedge breaks line (H2 ~62%), envelopment beats wedge at Cannae (H4 ~56%), refused flank counters envelopment at Leuctra (H5 ~56%), oblique edges line (H6 ~45%, band-low), maniple edges wedge (H8 ~60%), reverses sit correctly low (H9/H10/H11 35–46%). H7 (manipular vs line, Pydna) at ~45% is the one historically-expected win now sitting band-low after the geometry trim — the trim corrected an *over*-win (70%) but slightly past the 50 floor on the mean; calibration, not a structural miss.

Casualty realism: loser ~26% per-side on even/most matchups, the winner less, draws <5%, no one-turn-kills, battles ~7 ticks — matching the precedents' "loser 15–30% typical" for non-catastrophic engagements. The Cannae-style decisive matchups (H4) sit at the higher casualty end appropriately.

---

## §5 — Stage-4 re-test: two defects

`[FIXED: #2 — tier-equalization regression I introduced]` The first GappedLine size table was tuned for T3 (24 cells ≈ Line 25) but broke cell-count equalization at other tiers (T2: 20 vs Line 15; T4: 30 vs Line 35) — violating the canonical "sized to match Line cell count so advantage emerges from arrangement, not troops." The gauge only tests T3 so it passed there; the engine was wrong elsewhere (NERS-R fail across the tier range). **Fixed in v30:** size table re-derived to hold cells ≈ Line at all tiers (drift now ±1, was ±5) while keeping front-width < Line. T3 unchanged → §2 result preserved.

`[GAP: RefusedFlank mirror asymmetry — pre-existing, FLAGGED]` The re-test found the RefusedFlank-vs-RefusedFlank mirror at **38.8% A** (should be ~50/50), and reverse-pairs not cleanly complementary (H2 60% / H9 37% — a self-consistent forward, but the engine shows a mild A-side bias). This is **not introduced by my fixes** (they don't touch RefusedFlank geometry; other shape mirrors are ~46–49%, within noise, but RefusedFlank is clearly off and Arrowhead at 57.5% is borderline). It indicates a pre-existing side/orientation bias in the A/B engagement handling. **Does not block the counter result** (the gauge bands already bake in whatever bias exists, and it's small for most shapes), but it is a real robustness defect that should be investigated before the counter values are frozen. Likely in `resolve_cross_side_contention` or the advance-direction orientation (RefusedFlank's single forward cell may orient asymmetrically by side).

---

## §6 — Proposed values (PROPOSAL — Jordan ratifies; NOT committed)

The **mechanism and direction** are validated; the **exact magnitudes are over-fit-prone** (§3) and should be set by Jordan, ideally re-fit against a multi-seed objective (this session's tune was single-seed, then validated multi-seed — a proper fit would optimize the pooled count directly). Best multi-seed-validated cell:

**§A.6 formation-counter damage multipliers** (× damage to defender; `COUNTER_K=1.0`):
| Attacker vs Defender | Proposed mult | Historical | Note |
|---|---|---|---|
| Arrowhead (Wedge) v Line | +30% | cuneus (canon §A.6 Wedge) | |
| Horseshoe v Line | +0% (geometry delivers) | Cannae frontal | counter off; geometry already in-band |
| Horseshoe v Arrowhead (Cannae) | +15% | §A.8 envelopment | |
| GappedLine v Line | +0% (geometry delivers) | Pydna | counter off; **geometry fix** carries this |
| GappedLine v Arrowhead | +30% | maniple>wedge | lifts H8 after geom trim |
| RefusedFlank v Horseshoe | +20% | Leuctra (§A.8) | |
| RefusedFlank v Line | +5% | oblique slight edge | |
| **Line v Horseshoe** (reverse) | +25% | frontal push vs thinned center | needed to lift the reverse matchup |

**GappedLine geometry (T3):** front-row width 5→4 (half_w 4→2), depth +to hold cell count ≈ Line at all tiers.

These become a canonical patch (PP-NNN) extending §A.6 beyond Wedge/Shield-Wall, plus a `gapped_line_cells` dimension change. **Jordan sets the final numbers and whether geometry-or-counter carries each matchup.** Owner contract: not committed to `mass_battle_v30.md` without ratification.

---

## §7 — Independent-reviewer challenge surface `[SELF-AUTHORED — bias risk]`

1. **"You headlined 11/11 then walked it back — sloppy."** The 11/11 was caught by *my own* robustness pass and is reported as withdrawn, not buried. The validated figure (~9–10/11 pooled) is what stands. Catching over-fit before it ships is the discipline functioning. `[CONFIDENCE: high — the catch is sound; medium — exact pooled count, ±1 on seed/n]`
2. **"The values are over-fit even at the pooled level."** Fair risk — the tune was single-seed then validated multi-seed. The *mechanism* (counter + geometry) is robust and casualty-neutral across all seeds; the *specific strengths* should be re-fit against a pooled objective (§6 note). I flag this rather than claim the numbers are final.
3. **"H7 still misses on the mean."** Yes — ~45% vs a 50 floor, band-low. The geometry trim corrected its 70% over-win slightly past the floor. A small (+10–15%) GappedLine-v-Line counter would re-center it, but I left counter=0 there to avoid re-introducing the over-win at other seeds. Open calibration, surfaced.
4. **"Did the fixes break anything?"** The re-test found two defects (§5) — I report both. One I fixed; one (RefusedFlank asymmetry) is pre-existing and flagged. I did not hide them to preserve the result.
5. **"Multi-turn 0.0pp drift looks too clean — is multi actually exercising?"** Plausible concern; the multi layer at single-subunit Company scale reduces to sequential single engagements (no inter-unit dynamics until multi-subunit/D-3 lands), so identical results are expected, not suspicious. Multi-turn with *multiple subunits* (cascade, rout contagion) is an M4 test, not exercised here.

---

## §8 — Next steps

- **Jordan decision (1):** ratify the §A.6 counter-matrix + geometry proposal (§6) — set final magnitudes; ideally authorize a **multi-seed re-fit** of the strengths (optimize pooled count, not single-seed) before freezing.
- **Jordan decision (2):** authorize investigation of the **RefusedFlank/side-bias asymmetry** (§5 GAP) — likely in `resolve_cross_side_contention` / advance-direction orientation. Should be cleared before the counter values are canonical, since it perturbs the bands the counter is tuned against.
- **Then:** re-fit counters multi-seed on the de-biased engine; lock ≥10/11 *pooled*; commit.
- **M4+:** multi-turn with **multiple subunits** (cascade/rout-contagion dynamics — the real D-A L2 test, distinct from §2's single-subunit multi); ranged (R1/R3); canon reconciliation.
- **Commit (B6 resolved; `github_ops.py` re-fetched):** this doc → `designs/audit/2026-05-29-massbattle-sim-foundation/09_counter_geom_validated.md`; engine `sim_mb_06_v30_counters_geom.py` → `tests/sim/`; both via `safe_commit` on Jordan's OK. Diagnostic scaffolding (`_ck`/`_cm`/`v27`/`v28`/`v29`) keep local. Do **not** commit §6 values to `mass_battle_v30.md` without ratification.

---

### Audit trail
- `[READ: mass_battle_v30.md §A.6/§A.8 + modifiers]` · `[READ: sim_mb_06_v22_DB.py — SHAPE_OFF/DEF_MOD, pool, dmg, cell generators, role_at_contact, assign_targets]` · `[READ: precedents_warfare.md — all 326 lines, prior turn]`
- `[ASSUMPTION: base = v22_DB; both fixes are mechanics+geometry edits on it, not a base swap]`
- `[FIXED: #1 — re-populated zeroed §A.6 counter differential (08); counters decide at realistic casualties]`
- `[FIXED: #2 — GappedLine front-width geometry pulled H7 off its 70% geometric ceiling; tier-equalization regression re-derived to hold at all tiers]`
- `[CORRECTION: §3c — single-seed 11/11 withdrawn as over-fit; validated figure ~9–10/11 pooled, casualty-neutral, single≡multi]`
- `[BIAS: over-fit — single-seed tune; mechanism robust across seeds, specific strengths need multi-seed re-fit]`
- `[GAP: RefusedFlank/side-bias asymmetry — pre-existing (mirror 38.8% not 50/50); flagged, not introduced by these fixes; investigate before freezing counter values]`
- `[GAP: ED-875 low-Command sigma-leverage — same low-pool/Command region; unverified interaction]`
- `[CONFIDENCE: high — mechanism validated, casualty-neutral, single≡multi; medium — exact pooled count (±1) and the specific strength values (over-fit-prone, ratification + multi-seed re-fit pending)]`
- `[DRIFT: B6 resolved on main; github_ops.py re-fetched]`
- `[PASS-3: verdict stands — both ratified fixes validated; ~9–10/11 pooled casualty-neutral; 11/11 over-fit walked back; one defect fixed, one flagged; values surfaced for Jordan, not committed]`
