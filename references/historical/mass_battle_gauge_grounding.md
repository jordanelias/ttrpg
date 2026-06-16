# Mass-Battle Gauge — Historical & Academic Grounding (v2 recalibration)
**Date:** 2026-06-15 · **Status:** drives `tests/sim/gauge_mb.py` bands · **Supersedes the band-derivation basis of** `tests/sim/sim_mb_06_v9_historical_spec.md` (the v9 spec's H/R bands stand; its cavalry bands were never in scope and the gauge's later cavalry bands were *fitted to engine output* — this doc re-derives them bottom-up).

This is the bottom-up grounding for the recalibrated gauge bands. Every band is set by **historical precedent + peer-reviewed academic military analysis**, not by engine output. The engine is then validated *against* these bands; where it falls outside, the gauge **flags the divergence** — the band is not lowered to make the engine pass.

`[SELF-AUTHORED — bias risk: the engine fix (ED-1013) and this recalibration are Claude's; the academic sources and the historical record are the independent checks. Emergent figures are the smooth-cohesion engine at multi-mode n=120, SE ≈ 5pp.]`

---

## 1 — The metric change (raw-A% → decisive split)

The previous gauge checked **raw A%** (A's win-rate over *all* trials, draws included). This conflated two independent quantities — *who wins* and *whether anyone wins* — so a perfectly symmetric mirror failed its band purely because draws pulled raw-A% down (the Line mirror is 53/47 among decisive outcomes, yet raw-A% ≈ 32% with 40% draws). The recalibrated gauge checks the **decisive split**:

> `decA = A_wins / (A_wins + B_wins)` — "who wins **when** a result is reached."

The draw rate is validated **separately**, as a decisiveness dimension (`draw_exp`), because the quantitative combat-modelling literature establishes that **a high draw rate near parity is expected, not a defect**:

- Hillestad, Owen & Blumenthal (1995), *Naval Research Logistics* 42(2), DOI [10.1002/1520-6750(199503)42:2<209::AID-NAV3220420206>3.0.CO;2-M](https://doi.org/10.1002/1520-6750(199503)42:2%3C209::AID-NAV3220420206%3E3.0.CO;2-M): combat-outcome variance is *most pronounced in the "fair fight" regime in which the force balance is nearly even.*
- Taylor (1979), *NRLQ* 26(2), DOI [10.1002/nav.3800260216](https://doi.org/10.1002/nav.3800260216); Taylor (1983), *NRLQ* 30(1), DOI [10.1002/nav.3800300109](https://doi.org/10.1002/nav.3800300109): victory is *not guaranteed even when the force ratio is always changing to the advantage of one combatant.*
- Armstrong & Sodergren (2015), *Social Science Quarterly* 96(4), DOI [10.1111/ssqu.12178](https://doi.org/10.1111/ssqu.12178): the Lanchester square law yields an exact **tie** when `aC₀² = bU₀²`; Lanchester models are the validated quantitative framework for tactical engagements (Weiss applied them across 64 Civil War battles).

So: **even matchups** (mirrors, subtle formation edges) → `draw_exp='high'` (high draws OK); **gross-asymmetry matchups** (envelopment, cavalry vs braced/shaken) → `draw_exp='low'` (the matchup should resolve).

---

## 2 — The grounding sources

**Generalship / force-employment dominates numbers.**
- Biddle, *Military Power: Explaining Victory and Defeat in Modern Battle* (Princeton, 2004), rev. Wirtz (2006), *Journal of Politics* 68(2), DOI [10.1111/j.1468-2508.2006.00420_5.x](https://doi.org/10.1111/j.1468-2508.2006.00420_5.x): victory goes to whoever masters combined-arms force employment, *relatively insensitive to the numerical and technological balance.*
- `references/historical/precedents_warfare.md` §1.1 (Crécy 1346, Agincourt 1415, Austerlitz 1805): command quality, not numbers, decided. → **engine command-decisiveness (cmd6-vs-2 → 40-0) is correct.**

**Full envelopment is the one geometric edge that reliably tells.**
- Cannae 216 BC (double envelopment); Sidnell, *Warhorse: Cavalry in Ancient Warfare* (2006), rev. Basler (2008), *Historian* 70(3), DOI [10.1111/j.1540-6563.2008.00221_61.x](https://doi.org/10.1111/j.1540-6563.2008.00221_61.x): heavy cavalry was decisive in a **shock role** via physical + psychological effect *against the right target*.

**Formation geometry ALONE is a weak edge at strictly equal command.**
- Burkholder (2007), *History Compass* 5(2), DOI [10.1111/j.1478-0542.2007.00394.x](https://doi.org/10.1111/j.1478-0542.2007.00394.x): the cavalry-dominance and formation-dominance narratives (Oman, Fuller) are *overstated*; outcomes depended on a "dizzying array of factors," not one formation or weapon system. → wedge/oblique/manipular edges are **modest, near-even at equal stats**.

**Frontal cavalry vs STEADY close-order infantry is contested, not a cavalry win.**
- Burkholder (2007): *a horse will not run headlong into a solid object like a line of infantry*; foot were *perfectly capable of withstanding cavalry attacks* (Carolingian cavalry annihilated by Saxon infantry, 782); cavalry's killing was of **broken or flanked** foot, and its main weapon was the *feigned retreat* (Hastings 1066) — a ruse to make infantry break ranks. → **the old C1 band (52-80) encoded the popular misconception this source debunks.**

**Braced / squared infantry DEFEATS frontal cavalry.**
- Waterloo squares 1815; Bannockburn schiltrons 1314; Barua (2011), *Historian* 73(1), DOI [10.1111/j.1540-6563.2010.00284.x](https://doi.org/10.1111/j.1540-6563.2010.00284.x): British infantry *deployed in squares by which [Mysorean cavalry] could easily be beaten off* — Baillie's square (1780) the rare exception. → cavalry vs braced **LOW**.

**Cavalry is decisive vs SHAKEN/disordered foot and in the pursuit.**
- Boddy (2015), *Critical Quarterly* 57(4), DOI [10.1111/criq.12231](https://doi.org/10.1111/criq.12231): at Waterloo the Household Cavalry **dispersed 15,000 disordered French infantry**, then was itself destroyed once it over-pursued and lost cohesion (only 77 of 235 2nd Life Guards survived) — both cavalry's decisiveness vs disorder *and* its cohesion-fragility. → cavalry vs shaken **HIGH**.

---

## 3 — Per-band grounding (decisive split)

| ID | Band | draw_exp | Grounding |
|----|------|----------|-----------|
| H1 | 42–58 | high | Mirror symmetry. ±8pp = residual contact-asymmetry + sampling SE (the ED-1013 fix cut raw bias 21.7→3.3pp; residual is ~±6pp, *shape-dependent and opposite-signed* across H1/C3 = noise, not structural). |
| H2 | 48–62 | high | Wedge (cuneus) modest edge at equal command (v9 §A.6 +2D off; Biddle — geometry alone weak). |
| H3 | 55–72 | high | Full envelopment reliably tells (Cannae; Sidnell). The one geometric edge that survives equal command. |
| H4 | 45–62 | high | Cannae proper (envelopment vs single-axis wedge); tight — the wedge tip can punch a holding centre. |
| H5 | 48–62 | high | Refused flank / oblique as the explicit envelopment counter (Leuctra 371 BC). |
| H6 | 48–60 | high | Oblique order edge (Leuthen 1757). Modest. |
| H7 | 48–62 | high | Manipular checkerboard flexibility (Pydna 168 BC). |
| H8 | 50–65 | high | Maniples absorb wedge penetration and flank it. |
| H9/H10/H11 | inverse bands | high | Reverses of H2/H3/H4 (asymmetry confirmation). |
| R1 | 0–30 | low | Open-field ranged loses to melee that closes (Crécy/Agincourt won only with terrain/stakes — out of scope). `low`: melee should *close decisively*, not stand off. |
| R3 | 42–58 | high | Ranged mirror — symmetry sanity. |
| C1 | **35–55** | high | Frontal cavalry vs steady unbraced close-order foot is **contested** (Burkholder). **REBASELINE from 52-80** — the old band was the misconception. |
| C2 | 5–30 | low | Frontal cavalry vs braced foot (square/schiltron) — infantry wins (Waterloo; Barua). |
| C3 | 42–58 | high | Cavalry mirror — side-symmetry control. |
| C4 | 75–95 | low | Mounted envelopment of a line — devastating (Cannae rear-charge; Adrianople 378; Boddy). Near-decisive, not literally certain. |
| C5 | 65–90 | low | Cavalry vs already-shaken line — exploitation + pursuit (Boddy; Hastings post-feint). |
| C6 | 5–30 | low | Braced-shallow foot — a faced brace still repels frontally. = C2. |
| C7 | 65–90 | low | Cavalry envelops a braced line — bracing is bypassed from the flank/rear; you cannot face what wraps you (Cannae/Adrianople). Must be ≫ C2/C6. |

---

## 4 — Validation report (smooth-cohesion engine, multi, n=120)

**VALIDATED — engine within the history-grounded band (9/20):** H1, H3, H8, H10, H11, C1, C3, C4, C7. The engine correctly reproduces: mirror symmetry; **full envelopment, mounted and foot** (H3, H10, C4 93.8%, C7 86.7%); maniples-absorb-wedge (H8); command-decisiveness; and — notably — the **misconception-corrected** frontal-cavalry-vs-steady-infantry near-even (C1 45.7%).

**DIVERGE-soft — subtle formation edges washed to ~even, ~1 SE below band (6/20):** H2, H4, H5, H6, H7, H9. The smooth-cohesion pool (ED-1013) under-weights subtle formation geometry, so the wedge/oblique/manipular edges wash to even at equal command. **Defensible** as "geometry alone is a weak edge at equal command" (Biddle; Burkholder), but it sits below the §A.6-asserted modest edge → a residual, flagged not fitted.

**DIVERGE-hard — engine defect, flagged not fitted (3/20):** C2, C5, C6.
- **C2/C6 (cavalry vs braced):** the braced line *never wins decisively* (cavalry breaks the brace ~42%; decisive split 100% cavalry) — inverts Waterloo squares. The brace under-repels.
- **C5 (cavalry vs shaken):** decisive split 45.7% — **identical to C1** — i.e., the defender's morale (2 vs 6) has **no effect**. Morale-shock is inert in the cavalry exchange; cavalry does not exploit a wavering line.

The engine reproduces **envelopment geometry** correctly (C4, C7) but its **frontal cavalry shock / brace / morale** interactions are flat. This is the residual of "speed/charge not yet fully wired into combat" (S1) compounded by the smooth-pool wash. **Future-work engine targets, not band errors.**

**Ranged structural (R1, R3):** R1 ranged loses open-field (decisive split 0%, directionally correct) but the matchup is **too drawish** (85% — melee cannot force the close). R3 ranged mirror is **unresolvable** (all draws in 20 turns). Both are ranged-resolution engine gaps.

**Single mode:** ~all draws at the 18-tick cap for *every* config — a tick-cap artifact, not a calibration issue. Bands are evaluated in multi mode.

---

## 5 — Open judgment calls (Jordan-vetoable)

1. **Metric switch** raw-A% → decisive split — structural, but raw-A% was provably broken on symmetric mirrors. Draw rate retained as a separate validated dimension.
2. **C1 rebaseline** 52-80 → 35-55 — the old band encoded the cavalry-beats-unprepared-infantry trope Burkholder (2007) debunks; the near-even engine result is the more historically correct one.
3. **The 3 hard divergence flags (C2/C5/C6)** are left **failing** — the gauge's job is to flag where the engine is not yet historically accurate (braced infantry should repel cavalry; morale-shock should fire). These are engine-fix candidates, not bands to relax.
