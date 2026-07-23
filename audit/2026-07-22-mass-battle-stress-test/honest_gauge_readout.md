# Honest-Gauge Readout — measurement integrity landed (ED-MB-0027, 2026-07-23)

**Status: DIAGNOSTIC (the gauge now flags engine divergence honestly; bands NOT re-fit).**
Companion to `fiat_register_v1.md` (§1 measurement integrity, §10 A/B, §11 adversarial review).

## What changed

The gauge's confirmed **#1 distortion (M1)** was a per-cell **density mismatch** between its two
deployment paths: single-subunit opponents built via `make_unit → build_unit` (legacy tier footprint,
~16 troops/cell for a tier-3 Line) vs. the composed Envelopment/Refused presets that set an explicit
`concentration=100` (~100–133/cell). Because density enters `_lanchester_strength` **linearly**, that
~8× gap — not the flanking geometry — drove the envelopment rows to a hard 100%. The adversarial-review
**null test** (dense-vs-thin line, *zero* envelopment) already reproduced 100%, proving the maneuver was
never the cause.

**Fix (`gauge_mb.py`, ED-MB-0027):** hold per-cell density **constant at `GAUGE_CONC=100`** across
*every* gauge unit — single and composed alike — by building all units from the **same** explicit
`troops`/`concentration` path (`build_army` → `footprint_for`). `GAUGE_TROOPS=600` is chosen so every
historical split divides evenly by 100 (pin 1/3→200→2 cells; pin 2/3→400→4 cells; wings 200/100→2/1
cells; strong 1/2→300→3 cells) → integer-cell quantization is **exact**, no density overshoot. Verified:
single Line, envelop (3×), refused (2×), C4 cav-envelop, Arrowhead, GappedLine **all build at exactly
100.0 troops/cell, `hp_max=600`.** The only thing that now varies across rows is **frontage + geometry +
posture** — a fair ruler.

Safety: the gauge is a manually-run harness (no `test_` functions → not collected by pytest, not a CI
gate). `bat.py` (the byte-exact digest oracle) has its **own** `make_unit` copy and does **not** import
`gauge_mb`, so the goldens are unaffected. No canon touched.

## Before → after (multi mode, DECISIVE-split `decA`; `rawA` for braced-repel rows)

| id | matchup | band | UNFAIR (n=18/30) | **HONEST (n=14)** | verdict |
|----|---------|------|------------------|-------------------|---------|
| H1 | Line vs Line (mirror) | 42–58 | 44.4 | **42.9** | OK — mirror now fair |
| H2 | Arrowhead(wedge) vs Line | 48–62 | — | **0.0** | OUT — wedge loses frontally |
| H3 | Envelopment vs Line | 55–72 | 100.0 | **0.0** | OUT — **flipped**; splitting force is downside |
| H4 | Envelop vs Arrowhead (Cannae) | 45–62 | 100.0 | **35.7** | OUT — envelop under-delivers |
| H5 | RefusedFlank vs Envelopment | 48–62 | — | **0.0 (92.9% draw)** | OUT — two split armies stalemate |
| H6 | RefusedFlank vs Line | 48–60 | — | **0.0** | OUT — split loses to single body |
| H7 | GappedLine(manip) vs Line | 48–62 | — | **85.7** | OUT — GappedLine over-strong |
| H8 | GappedLine vs Arrowhead | 50–65 | — | **100.0** | OUT — GappedLine over-strong |
| H9 | Line vs Arrowhead (rev H2) | 38–52 | — | **92.9** | OUT — line beats wedge |
| H10 | Line vs Envelopment (rev H3) | 28–45 | 0.0 | **100.0** | OUT — line beats envelop outright |
| H11 | Arrowhead vs Envelopment (rev H4) | 38–55 | — | **7.1** | OUT — envelop loses to wedge |
| R1 | Ranged vs Line (open) | 0–30 | — | **21.4** | OK |
| R3 | Ranged vs Ranged (mirror) | 42–58 | — | **50.0 (all draw)** | OK |
| C1 | Cav vs steady unbraced Line | 35–55 | — | **0.0** | OUT — cav loses to steady foot |
| C2 | Cav vs BRACED Line (raw) | 0–30 | — | **57.1** | OUT — **brace not repelling** |
| C3 | Cav vs Cav (mirror) | 42–58 | — | **71.4** | OUT — **charge asymmetry** |
| C4 | Cav flank/envelop vs Line | 75–95 | 100.0 | **0.0** | OUT — **flipped** |
| C5 | Cav vs SHAKEN Line | 65–98 | — | **71.4** | OK |
| C6 | Cav vs BRACED-shallow (raw) | 0–30 | — | **57.1** | OUT — brace not repelling |
| C7 | Cav envelop vs holding Line | 65–100 | — | **100.0** | OK |

Pass 5/20 (H1, R1, R3, C5, C7). Battles also resolve **fast** on the fair ruler (t≈2–3 vs 5–9 before) —
the density crush is gone, but so is any staying power; the DG-6 over-decisiveness/low-variance concern
(fiat register V4/CEV) is now visible without the density confound.

## What the fair ruler reveals — CORRECTED per Jordan's Cannae analysis (2026-07-23)

⚠️ **An earlier draft of this section concluded "force-splitting is pure downside." That conclusion was
itself a scale + construction artifact — retracted.** Jordan's Cannae-diagram analysis (the 60,000-strong
deep Roman block vs. Hannibal's thin, wide, *withdrawing* crescent + enveloping wings) plus two follow-up
probes show why the gauge's envelop rows read ~0%, and it is **not** that the maneuver is worthless:

- **Depth-reserve WORKS (probe `_depth_probe.py`, equal troops + equal 100/cell density, only aspect
  varies):** a narrow-DEEP column beats a wide-SHALLOW line **100%** (6×4 / 4×6 / 3×8 all beat 24×1). The
  depth machinery (`PC_DEPTH_ROTATE` fatigue-damping, `PC_REFILL_FLOOR` rear-rank refill, `PC_FRONT_RANKS`)
  is real and decisive at scale. So depth is *not* worthless — the opposite.
- **Why the gauge envelop CENTER loses:** `footprint_for` builds it **wide-shallow and under-strength** —
  200 of 600 troops as a **2-cell-wide × 1-deep** Line — so the single 6-cell opponent out-frontages it
  **3:1** at equal depth (at equal depth, more columns = more men engaged = win). It is a mis-*built*,
  mis-*scaled* center, not proof the flank geometry fails.
- **The three things the gauge cannot express at 600 troops / 6 cells (Jordan's point):**
  1. **Frontage saturation.** At Cannae the frontage is capped by the battlefield and armies vastly exceed
     it, so most troops are held in DEPTH behind a saturated front and rotate. At the gauge's scale both
     lines fit inside the meeting frontage — *everyone engages*, there is never a rear reserve waiting to
     rotate. The mechanic can't fire.
  2. **A deep, holding pin.** The Cannae center's job is to be DEEP and HOLD (absorb + rotate) long enough
     for the wings to wrap. The gauge center is shallow and under-strength, so it is beaten in detail
     before the wings arrive.
  3. **Backward pathing / strategic withdrawal (the actual Cannae mechanism).** Hannibal's center gave
     ground deliberately — a *fighting withdrawal* to bait the Romans deeper — while the wings enveloped.
     The gauge center marches **forward** into the crush.

## The real backlog, re-ranked (Jordan's directive: intent + scale)

1. **Intent as a first-class resolution axis (NEW, Jordan 2026-07-23: "intent makes a big difference in
   how things resolve").** `stance` ∈ {aggressive, balanced, hold, retreat} currently modifies only
   *movement speed* (`STANCE_SPEED_MOD`), not *trade quality*. A subunit **holding to defend** should
   trade favorably and grind the attacker; one **pressing to break/rout** should push morale harder at a
   casualty cost; one **withdrawing to bait** (the `yielding`/DG-2 fighting-withdrawal — real but gated
   off and morale-*triggered*, not a deliberate order) should give ground while staying intact. Wire
   intent into the exchange, not just the move.
2. **Cannae-scale test + deep-holding-center construction.** Rebuild the envelop scenario at a scale where
   frontage saturates (deep Roman block; thin wide crescent) and build the pin DEEP + set to
   withdraw/hold, so depth-reserve and the wrap can actually be measured. The current small-scale envelop
   rows should be treated as **not-yet-measurable**, not as "envelopment broken."
3. **Backward pathing as a deliberate order.** Expose fighting-withdrawal (`stance='retreat'` +
   `yielding`) as an up-front intent so the baiting-center maneuver is orderable, not only an emergent
   morale response.
4. **Brace is broken (P2 confirmed live).** C2/C6 = 57% raw cavalry win into a braced disc-8 wall that
   should **repel** (band 0–30). `PC_CHARGE_RECOIL` not firing / insufficient — matches fiat register P2.
5. **Mild wide-mirror asymmetry.** A perfect mirror should be 50/50; measured (N=72/width, 3 seed bases)
   it is fair at width ≤6 (~48–51%) but drifts to ~55–57% A at width ≥12. Minor, but a genuine residual
   order-effect that accumulates with column count. (The n=16 "75/25" first read was sampling noise —
   confirmed by re-running larger; a reminder to not trust small-n on the mirrors, incl. C3=71.)
6. **GappedLine over-strong.** H7=86, H8=100 (bands cap 62/65) — likely a frontage/contact-count artifact
   (gapped cells present more engaged columns per troop). Re-examine after the intent/scale work.

## Guardrails honored

- **Bands were NOT lowered to make the engine pass** (fiat register §8 north star: calibrate to
  independent history — Dupuy DLEDB, Sabin — never to these 20 rows). A failing row is the gauge
  *working*: it flags engine divergence that the density fiat previously hid.
- **No canon touched.** `compute_degree` tiers, the octagon 1.0/1.5/2.0 table + `MULTI_SIDE_SHOCK`, the
  50/25 morale triggers, and the `CELL_FLOOR/CELL_CAP` values are all left intact (§11 false-positives).
- The measurement fix is isolated to the harness; the engine change (item 1 above) is the next
  adversarially-reviewed step.
