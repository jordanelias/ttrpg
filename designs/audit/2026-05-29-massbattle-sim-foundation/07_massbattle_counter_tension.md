# Mass Battle Sim — M3 Findings: The Casualty–Counter Tension (stages 3-0 → 3b)

**Date:** 2026-05-29
**Skill:** valoria-simulator (NERS framing: valoria-resolution-diagnostic)
**Scope:** simulation
**Session token:** df5079812d207c7e
**Relates to:** `tests/sim/HANDOFF_massbattle_foundation_M3.md`; foundation audit set `01`–`06` in `designs/audit/2026-05-29-massbattle-sim-foundation/`
**Status:** FINDINGS — **supersedes the v23-base recommendation** that an earlier draft of this doc (presented last turn) carried. The base-selection question is **reopened**; the real obstacle is the counter mechanism, which is a Jordan design decision. No tuning past this point until ratified.

`[SELF-AUTHORED — bias risk]` This doc corrects a recommendation I made one turn earlier (adopt v23). The 3a stabilization step refuted it. That inversion is the Stage-4 re-test discipline functioning as intended — a pre-stabilization result failing post-stabilization — not a defect in the new conclusion. The independent-reviewer challenge surface is in §9.

---

## VERDICT

**Across the entire v9–v25 engine lineage, the formation-counter spread the v9 historical bands require only emerges when battles are fought to catastrophic casualties (~60–100% loser). At historically-typical casualties (~26% per side), every engine collapses to 5/11 melee in-band.** This holds for two structurally *different* engines — v23 (cell-pair frontage) and v14 (grind-to-annihilation) — so it is not an artifact of any one engine's mechanic. The counter *effect size* is too small to be decisive within the historical casualty budget; only prolonged/catastrophic combat accumulates enough advantage to register in win-rates.

**Consequences:**
- The 3-0b recommendation to **adopt v23 is WITHDRAWN.** Its 9/11 was a catastrophic-regime artifact (loser ~86–100%); stabilising casualties to target drops it to 5/11.
- This is a **counter-mechanism problem, not a base-selection problem.** Choosing among v22 / v23 / v14 / v24 / v25 does not fix it — they are all 5/11 at realistic casualties.
- **D-C's empirical premise is re-supported** (the cell-physics lineage does not fix counters at realistic operating points). **D-C's prescription is also inadequate** (v14, the proposed reference, achieves its bands only at catastrophic casualties, over-annihilates even mirrors, and has no multi-turn engine).
- **3c (counter tuning) is moot** until the counter mechanism is strengthened. That strengthening is a design change to the §A.6/§A.8 counter modifiers — **Jordan's call.**

---

## §0 — Re-anchor & provenance (unchanged, clean)

Foundation PR #2 merged to `main` (squash) since the handoff. All 9 foundation files (`gauge_mb.py`, `sim_mb_06_v22_DB/v22/v23/v24/v25/v14`, `sim_mb_06_v9_historical_spec.md`, `precedents_warfare.md`) resolve on `main` and **hash-match** local copies byte-for-byte; the +10 commits only *added* the foundation + work products, modifying no verified engine. Mechanics files (`mass_battle_v30.md`, `params/mass_combat.md`) untouched. Gates re-passed each session: `task_gate('simulation')` ✓, `sim_gate('custom',['mass_combat'])` ✓.

`[DRIFT: B6 — resolved on main]` Commit `f051d911` added a PR-merge fallback to `atomic_commit`; PR #2 merged through it. Cached `github_ops.py` predated the fix; **re-fetched from main this session** (79452 bytes, has `pulls`/`merge` signals) — commit is now possible via `safe_commit`. Audit slot `06` is taken (`06_B6_fix.md`); this doc targets slot `07`.

`[READ: tests/sim/gauge_mb.py — full]` `[READ: tests/sim/sim_mb_06_v9_historical_spec.md — full]` `[READ: references/historical/precedents_warfare.md — all 326 lines]` `[READ: tests/sim/HANDOFF_massbattle_foundation_M3.md — full]` `[READ: sim_mb_06_v23_DB.py — erosion (217–224, 321–328, 1693, 2027), cell_pair_count (1364–1378), rout_resolution (330–348), winner/rout paths (1003, 1696–1706)]` `[READ: params/mass_combat.md — morale/rout/discipline mechanics: PP-232 Command (Morale floor=1 w/ general), Morale Degradation Triggers (L155–169), Discipline Degradation (PP-251), Cascade phase (PP-235)]`

---

## §1 — 3-0: Verify the rebuild ✓

`CASUALTY_SCALE=20 gauge_mb.py sim_mb_06_v22_DB.py`, single, n=60: **5/11** melee (H1,H5,H6,H9,H11); H1 mirror casualties 25.2%/25.6% (on target); draw 5.0%. Exact handoff match. `[CONFIDENCE: high]`

---

## §2 — 3-0b: v23 = 9/11 (PROVISIONAL — now shown to be an artifact)

Fresh gauge, single, D-B scaling applied uniformly: v22_ratio 5/11, v22_DB 5/11, v24_DB 5/11, v25_DB 5/11, **v23_DB 9/11** (H1,H2,H3,H4,H5,H7,H8,H9,H11). v23 net-gained the offensive counters (H2 wedge, H3/H4 envelopment+Cannae, H7 Pydna, H8). The earlier draft flagged this as *provisional pending 3a* — correctly, because v23's H1-mirror casualties were already 46.7/63.3% (vs v22_DB's 26%), i.e. the result sat in an un-stabilised, high-casualty regime. 3a was run to stabilise the instrument; it inverted the conclusion.

---

## §3 — 3a: Stabilisation refutes the v23 advantage

### 3a.1 — The actual defect (read, not remembered)
The v20 morale-erosion model (inherited by v23): `erosion = total_dmg / (discipline × command)` per tick (sites: line 1693 single, 2027 multi); rout at morale ≤ 0; **no hard threshold** — the ~30% rout fraction *emerges*, and `cmd` in the denominator is deliberate ("generalship dominates", §A.4: cmd=6 → 45% to rout, cmd=2 → 15%). Cumulative analysis shows this routs at casualties = `morale × disc × cmd` soldiers, which **as a fraction of hp_max is already CS-invariant.** So the handoff's diagnosis ("erosion mis-dimensioned → switch to `K × total_dmg/hp_max`, dropping disc×cmd") would have **destroyed generalship dominance** while not addressing the true defect.

The true defect is **magnitude/granularity**: the D-B patch placed `CASUALTY_SCALE` (=20, calibrated for v22's non-frontage damage) in front of `per_pair_dmg × cell_pair_count`. The frontage factor (cell_pair_count, mirror = 34) was never in CASUALTY_SCALE's derivation, so per-tick damage is ~34× too large on the mirror → battles resolve in **3 ticks**, casualties **overshoot** the morale-rout into size=0 annihilation (the second rout channel, line 1003), and mutual overshoot drives elevated draws.

### 3a.2 — The variance diagnostic (decisive)
Instrumented degree-roll counts, mirror (Line vs Line), n=60:

| Engine | ticks | **damage-rolls / battle** | loser casualties |
|---|---|---|---|
| v22_DB (CS=20) | 7.6 | **11.2** | 34% (loser-side) / 26% (per-side gauge) |
| v23_DB raw (CS=20) | 3.0 | **2.0** | **100% (annihilation)** |
| v23_3a (CS=20, FR=34) | 6.3 | 8.5 | 39% (loser-side) |

v23's frontage is structurally **fewer, bigger damage rolls** (one degree-roll × cell_pair_count, vs v22's many small unit-pair rolls). **That is a variance increase, not a geometric counter model.** High variance → decisive single-tick snowball → *both* the 9/11 spread *and* the casualty overshoot, from one cause. Magnitude tuning cannot separate them.

### 3a.3 — Stabilisation (frontage normalisation) and the collapse
Built `sim_mb_06_v23_3a.py`: `dmg += CASUALTY_SCALE × per_pair_dmg × (cell_pair_count / FRONTAGE_REF)`, FRONTAGE_REF = 34 (mirror mean → mirror multiplier 1.0, preserving cpc *ratios* and CASUALTY_SCALE's calibration). Dividing cpc by a constant is a global magnitude rescale that preserves the counter ratios. Result, single, n=60: **5/11** (in-band H1,H3,H4,H9,H11; out H2/H5/H6/H7/H8/H10 — washed toward 50/50). **Identical to v22.**

FRONTAGE_REF sweep @ CS=20 (mirror loser-cas / melee): FR=20 → 50% / 8/11 (but draws 15%); FR=27 → 45% / 5; FR=34 → 39% / 5; FR=45 → 39% / 5; FR=60 → 35% / 6. **No value gives both historical casualties and >5–6/11.**

### 3a.4 — The handoff's prescribed fix, tested across a grid
Built `sim_mb_06_v23_3a_efrac.py` (the handoff's literal casualty-fraction erosion, `MORALE_K × total_dmg / hp_max`). Grid FRONTAGE_REF{6,10,20,34} × MORALE_K{12,16,20,28}, n=40, cell = melee/11 (mirror loser-cas% / mean-draw%):

| FR\K | 12 | 16 | 20 | 28 |
|---|---|---|---|---|
| 6 | 4 (80/10) | 5 (58/8) | 4 (40/11) | 6 (40/12) |
| 10 | 7 (82/9) | 6 (49/8) | 4 (49/10) | 5 (35/9) |
| 20 | 5 (66/7) | 7 (61/10) | **9 (50/11)** | 5 (30/9) |
| 34 | 6 (61/7) | 6 (48/8) | 3 (39/10) | 6 (34/11) |

The **only 9/11 cell** sits at **50% mirror casualties** (catastrophic) + 11% draws. The best cell with mirror-cas ≤38% and draws <15% is **6/11** (FR=34, K=28, 34% cas). Fraction-erosion controls the rout *threshold* but not the per-tick *overshoot* (damage applies before the rout check, line 1695). **The prescribed fix does not rescue the count at historical casualties either.**

---

## §4 — 3b: v14 reproduces 9/11 — but only at catastrophic casualties

v14 (the handoff's claimed 12/13 reference; no battery was preserved) run through the current gauge, single mode, n=60 (API-adapted; v14 has `run_battle`, **no** `run_multi_turn_battle`):

- **9/11 melee** in-band (H2,H4,H5,H6,H7,H8,H9,H10,H11; out H1,H3). The "12/13" headline is in the same neighbourhood; not reproduced exactly on this 13-test gauge, but directionally consistent.
- **Casualties: 64% per-side / 86% loser-side — catastrophic — on *every* matchup, including the H1 mirror (62%/68%).** A mirror (two identical lines, a coin-flip) annihilating both sides 64% is itself wrong.
- **rolls/battle: 13.8** — *more* than v22 (11.2), ticks 9.1. So v14 is **not** a fewer-bigger-dice variance artifact. It is a *different* mechanism: no realistic-casualty rout, so it grinds every match to ~86% and the better formation wins the long grind.

So v14's 9/11 lives in the **catastrophic-casualty regime via a different route than v23's.** Two structurally different engines, same regime-dependence.

---

## §5 — The structural finding: counters ⟺ catastrophic casualties

| Engine | melee | per-side casualties | rolls/battle | regime | mechanism |
|---|---|---|---|---|---|
| v22_DB | 5/11 | 26% | 11.2 | **historical** | many small rolls, realistic rout |
| v24_DB | 5/11 | ~24% | — | historical | (D-B) |
| v25_DB | 5/11 | ~24% | — | historical | (D-B + angle mult) |
| v23_3a (FR=34) | 5/11 | 39% loser | 8.5 | ~historical | frontage-normalised |
| **v23_DB raw** | **9/11** | 100% loser | 2.0 | **catastrophic** | few big rolls (variance) |
| **v14** | **9/11** | 86% loser / 64% side | 13.8 | **catastrophic** | grind-to-annihilation |

The **within-engine** demonstration is the cleanest proof it is the *regime*, not the engine: inside a single engine (v23_3a) the band count tracks the casualty level — FR=20 (50% cas) → 8/11; FR=34 (39%) → 5/11; FR=60 (35%) → 6/11. As casualties fall from catastrophic to historical, the counters wash out. The grid shows the same (9/11 only at 50% cas). The cross-engine pattern (v22_DB 5/11@26% vs v14 9/11@86% vs v23 9/11@100%) confirms it across mechanisms.

**Diagnosis:** the formation-counter effect size is too small to be decisive within the first ~30% of casualties. The advantage only accumulates to a win-rate signal under prolonged/catastrophic combat. The v9 bands implicitly assume the counters show at the historical casualty band; the mechanics deliver them only at the catastrophic end.

---

## §6 — Historical-precedent validation (the counters are real; the failure is mechanical)

`precedents_warfare.md` §1.2 and §6 state the formation-counter system and "generalship dominates" axiom are **historically correct**; Cannae (216 BC) is the canonical double envelopment. So the model *should* produce these counters — the failure is mechanical (effect size too small early), not conceptual.

A genuine nuance the data raises: historically, a *decisive* formation-counter victory often DID produce catastrophic loser casualties (Cannae: ~50,000 of 86,000 ≈ 58% destroyed, *because* the envelopment led to slaughter). The "15–30% typical" band is for indecisive/even battles. So catastrophic loser casualties on the *decisive* matchups are not unhistorical. **What is unhistorical is the H1 mirror at 64–86% casualties** — an even, coin-flip match should grind to ~15–30%, not annihilate. The engines that show the counters (v23 raw, v14) over-annihilate the mirror; the engines with realistic mirror casualties (v22_DB, v23_3a) lose the counters. That is the tension stated precisely.

---

## §7 — The decision for Jordan (counter mechanism — owner contract)

This is a design call I will not make. Three coherent directions:

1. **Strengthen the counter modifiers** (§A.6/§A.8 dice differentials) so a formation advantage is decisive *early* — i.e. produces its win-rate within ~30% casualties rather than requiring a grind to annihilation. This keeps realistic casualties (D-B) *and* the counters. It is the most historically faithful (Cannae's envelopment was decisive quickly, not after mutual attrition), and it is a mechanics edit, not a base swap. **Recommended direction to evaluate first**, but the magnitude of the strengthening is a design choice.
2. **Accept a two-regime model**: decisive matchups run to catastrophic loser casualties (historical for Cannae-type outcomes), even matchups stay ~15–30%. Requires fixing only the *mirror/even* over-annihilation, not the counter effect size. Lighter change; less general.
3. **Re-examine the v9 bands themselves.** They may implicitly encode catastrophic-decisive battles; if so the bands, not the engine, are mis-specified. This reopens the spec, so it is the heaviest option.

All three need Jordan. Until one is chosen, **3c is moot** (tuning counters that the mechanism cannot express at realistic casualties).

---

## §8 — D-C disposition

- **Empirical premise — RE-SUPPORTED.** "v9 / ratio-v22 / D-B-v22 all ~5/11; the cell machinery added complexity for zero band gain at realistic operating points" is correct (confirmed: 5/11 across v22/v23_3a/v24/v25 at historical casualties). My 3-0b refutation of this was based on the v23 artifact and is withdrawn.
- **Prescription — INADEQUATE.** "Revert toward v14 geometry, may delete v20–v25." v14 achieves its bands only at catastrophic casualties, over-annihilates mirrors, and has no multi-turn engine (violates D-A). It is not a drop-in reference. **Do not delete v20–v25** — they are the only engines with realistic casualties, and the cell-physics is a Jordan design; deletion is premature and Jordan's call regardless.
- Net: D-C as written is **superseded** by the deeper finding (§5). The path is not "pick v14" but "strengthen the counter mechanism" (§7), on a D-B-capable base.

---

## §9 — Independent-reviewer challenge surface `[SELF-AUTHORED — bias risk]`

1. **"You flip-flopped: v23 last turn, not-v23 now."** Yes — and the earlier draft explicitly labelled the 9/11 *provisional pending 3a*. 3a is the test that resolves it. The flip is the re-test catching an artifact, which is the point of staging 3a before 3c. The new conclusion rests on four independent results (variance diagnostic, FR sweep, the grid, v14), not one run.
2. **"v14's 12/13 wasn't reproduced (you got 9/11) — maybe your gauge is wrong for v14."** The exact count is secondary; the load-bearing fact is v14's casualties (86% loser, including the mirror) — that is regime, not count. Even a literal 12/13 would be catastrophic-regime.
3. **"You didn't confirm v14's bands collapse at realistic casualties (you couldn't rescale it — no CASUALTY_SCALE)."** True — that is the one clean confirming experiment not yet run (§10). The within-engine v23_3a sweep + grid already demonstrate the tension inside an engine that *can* be rescaled; v14 (no realistic-rout, 86% everywhere) is consistent with it. `[CONFIDENCE: high on the lineage-wide tension; the v14-specific collapse is inferred, not directly shown]`
4. **"Maybe catastrophic casualties on decisive matchups are fine and you're over-indexing on the mirror."** Addressed in §6 — decisive catastrophic casualties are historical; the disqualifier is the *mirror/even* over-annihilation, which is unambiguous.

---

## §10 — Next steps

- **Clean confirming experiment (recommended next):** port the D-B realistic-casualty rout into v14 (or add a casualty-% rout cap) and show v14's 9/11 also collapses toward 5/11 at ~30% casualties. That converts the §5 inference into a direct demonstration and closes challenge #3.
- **Jordan decision (§7):** which counter-mechanism direction. Blocking for any further tuning.
- **3c:** deferred until the mechanism is chosen; then tune §A.6/§A.8 modifiers and validate on the gauge to ≥10/11 *at realistic casualties* (the real bar, not the old 9/11-at-catastrophic).
- **Commit:** B6 resolved; this doc can go to `designs/audit/2026-05-29-massbattle-sim-foundation/07_massbattle_counter_tension.md` via `safe_commit` (re-fetched `github_ops.py`) on Jordan's OK. The engine artifacts (`sim_mb_06_v23_3a.py`, `_efrac.py`) are diagnostic scaffolding, not proposed canon — keep local unless Jordan wants them archived.

---

### Audit trail
- `[READ: …]` as listed in §0.
- `[CORRECTION: stage 3-0b → 3a — the v23-base recommendation is withdrawn; v23's 9/11 is a catastrophic-regime/variance artifact, not a counter fix]`
- `[CORRECTION: stage 3a — the true 3a defect is damage magnitude/granularity (frontage × a v22-tuned CASUALTY_SCALE), not erosion mis-dimensioning; the v20 erosion is already CS-invariant and generalship-preserving, so the handoff's prescribed casualty-fraction erosion (which drops disc×cmd) was not applied as the fix]`
- `[ASSUMPTION: v14 9/11 collapses at realistic casualties — basis: within-engine v23_3a sweep + grid + v14's uniform 86% casualties; not directly shown, see §10]`
- `[BIAS: prior-commitment — I recommended v23 last turn; actively tested the four ways it could be rescued (CS, FRONTAGE_REF, fraction-erosion grid, v14 alternative) before concluding against it]`
- `[CONFIDENCE: high — lineage-wide casualty↔counter tension; high — v23 advantage is an artifact; medium — exact path forward (a §7 design choice for Jordan)]`
- `[DRIFT: B6 resolved on main; open in PI/handoff]`
- `[GAP: ED-875 mass-battle low-Command sigma-leverage — open Jordan-design item in the 2026-05-29 resolution-diagnostic handoff; same low-pool/Command region as the erosion/generalship mechanics here; may interact with §7 option 1; unverified]`
- `[PASS-3: verdict stands — counters are catastrophic-regime-dependent across the lineage; base selection cannot fix it; v23 withdrawn; D-C empirical premise re-supported, prescription inadequate; §7 is a Jordan decision]`
