# Mass Battle Sim — Module 1 (Gauge) Built + F3/F1 Resolved + Build Manifest

**Date:** 2026-05-29
**Task:** simulation (gated; sim_gate passed; verification ledger present)
**Decisions in force:** D-A (two-level instrument, multi-turn canon) and D-B (complete bottom-up TroopCount model) — both approved by Jordan.
**Commit status:** nothing committed (B6). Gauge + engine variants are local; staged for manual push.
**Artifact:** `gauge_mb.py` (the reusable instrument).

---

## Verdict

The validation foundation now exists. Module 1 (the gauge) is built, runs against the current engine API, and is grounded in the v9 historical bands (Cannae/Pydna/Leuctra/Crécy via `precedents_warfare.md`). Running it as a 2×2 (as-is vs ratio-restored) × (single-engagement vs multi-turn) **empirically resolved the two open questions** the prior turn could not: the HP:damage ratio is the dominant binding constraint, and the multi-turn blowout was an artifact of the ratio break, not an independent defect. Lethality is now over-calibrated and the formation counters are the remaining work — both now measurable.

---

## The 2×2 result (gauge_mb.py, n=60/matchup, v9 historical bands)

```
engine variant            single   multi
as-is (v19 BLOCK_SIZE)      0/13     1/13
ratio-restored              5/13     6/13
```

### F3 RESOLVED — ratio is the dominant binding constraint
As-is single-engagement = **0/13, 100% draws** (4–8% casualties in 18 ticks): the v19 HP inflation (HP = Size×100 with damage left at ~3–4) makes single engagements unresolvable. Restoring the ratio (engagement HP on `h_per_size` scale, matching volley) → **5/13**. Necessary, not sufficient.

### F1 RESOLVED — multi-turn "blowouts" were a ratio artifact
As-is multi-turn produced landslides (H4 1.7/98.3, H7 100/0) because, with single engagements unresolvable, the multi-turn layer ran ~5–8 turns and compounded small edges. Ratio-restored, battles resolve in **~1 turn** (`battle_turns ≈ 1.0`), and **single ≈ multi** (5 vs 6, near-identical per-matchup win rates). The multi-turn amplification was downstream of the ratio break — not a separate Lesson-5 loop defect. (A real multi-turn dynamics check is still M4, but the pathological amplification is gone.)

### Lethality now over-calibrated → D-B target
Ratio-restored mirror (H1) casualties ≈ **58% on both sides** — Cannae-level and symmetric. Historical typical is **loser 15–30%, winner less (asymmetric)**. So:
- **D-B casualty target:** dial casualties-per-success down so a decisive mirror gives loser ~20–30%, winner ~10–15%.
- **D-B asymmetry target:** winner should lose materially less than loser (currently ~symmetric — the pursuit/rout phase isn't producing the winner-advantage). The gauge measures `casA%`/`casB%` per matchup, so both targets are directly observable.

### F5/D-C CONFIRMED — over-engineering
Ratio-restored v22 = **5/13**; the v9 engine = **5/13** (measured this session). The entire v13→v22 cell-physics stack (equal-speed contention, displacement ripple, formation-hold — Issues 2/3/4) left band-count **unchanged at ~5** while adding heavy complexity. The 12/13 high-water mark was **v14's formation-counter tuning specifically**, which sits between v9-simple and v22-elaborate. **Steer for D-C: revert toward v14's geometry rather than repairing/extending the v13+ cell-physics.** (Confirm by reconstructing the v14 battery — M3.)

### Remaining OUT bands (the genuine formation work, now measurable)
At ratio-restored single: H2 (Arrowhead vs Line 42, want 50–65 — wedge too weak), H3 (Horseshoe vs Line 68, want 50–65 — envelopment too strong vs line), H4 (Cannae 30, want 40–60 — horseshoe LOSES to wedge, wrong direction), H6, H7 (GappedLine vs Line 73, want 50–65), H8, R1, R3. In-band already: H1, H5, H9, H10, H11.

---

## Mode-G Build Manifest (one module per session)

| Module | Status | Scope | Validates against | Gate |
|---|---|---|---|---|
| **M1 — Gauge** | **DONE (this session)** | Historically-grounded single+multi battery, current API; `gauge_mb.py` | v9 spec bands (real battles) | — |
| **M2 — D-B combat model** | next | Complete bottom-up TroopCount (HP=soldiers; damage=soldiers killed); calibrate casualties/success to historical loser 15–30% + winner asymmetry, using M1 | historical casualty rates | sim_gate |
| **M3 — Formation counters** | after M2 | Bring 8 OUT bands in (H2/H3/H4/H6/H7/H8/R1/R3). Per D-C: revert toward v14 geometry; reconstruct v14-compatible battery as the reference for "correct" counters | v9 spec bands + v14 reference | sim_gate |
| **M4 — Multi-turn dynamics (D-A L2)** | after M3 | Once single is in-band, validate pacing/pursuit-asymmetry/morale-cascade; derive proper multi-turn bands | historical dynamics rates | sim_gate |
| **M5 — ED-822 volley/composition** | after M3 | Ranged matchups (R1/R3) + ranged-vs-melee composition on corrected base | Crécy/Agincourt/Hastings patterns | sim_gate |
| **M6 — Canon reconciliation** | last | Write validated degree-banded model + calibrated constants into §A.7/PP-233; strike additive §A.7 text | — (Jordan ratifies) | safe_commit |

**Sequencing rationale:** M1 makes everything falsifiable. M2 fixes the dominant defect (ratio) properly as the bottom-up model + calibrates lethality. M3 fixes the counters on a correct lethality base (and resolves D-C empirically). M4/M5 are downstream dynamics/composition. M6 ratifies into canon.

---

## How this answers "how do we stop wasting effort"
The disease (F6, prior doc): the validation gauge was never carried forward across 21 engine versions, so each version re-broke accuracy invisibly and "12/13" became unfalsifiable. **The fix is M1 itself + a discipline:** `gauge_mb.py` is engine-agnostic (takes the engine file as an argument) — every future version must pass it before commit. That is the buildable core of the roadmap's pending **P7 "Verify unread surfaces"** applied to the sim: a portable, grounded gauge that travels with the lineage. The same principle (`system_artifact_index` at task entry) prevents the read-the-oldest-artifact failure that started this thread.

## Confidence & limits
- `[CONFIDENCE: high]` — 2×2 result is direct measurement (n=60); F3/F1 resolution follows from it; the single≈multi collapse and v9/v22-ratio both=5/13 are cross-checks.
- `[CONFIDENCE: medium]` — exact casualty calibration targets (15–30%) are from `precedents_warfare.md` narrative, not a precise canon figure; D-B should confirm the target band with Jordan.
- The ratio-restore tested here is the v9 `Size×h_per_size` revert — a **proxy** that proves the ratio is binding. The real Issue-1 fix is M2's TroopCount-completion (D-B), not this revert.
- Engine variants (`sim_v22_asis.py`, `sim_v22_ratio.py`) and gauge are local; main untouched (B6).
- Note: a separate **production** mass-battle module exists (`sim/provincial/massbattle.py`, mc_v18 lineage) distinct from this `sim_mb_06` research lineage. The historical validation lives in the research lineage; reconciling the two is a later concern, not in this build.
