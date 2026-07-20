# Armour System — Validation (bottom-up build, top-down precedent check)

**Date:** 2026-05-30 · **Module:** `armour_axes.py` (self-test 7/7) · **Status:** Class-C proposal; **no canon retconned** (the matrix reproduces the ratified weapon-vs-armour table exactly). `[CONFIDENCE: high]` `[SELF-AUTHORED — bias risk: this doc CORRECTS an over-claim in the design spec; see §3.]`

Built the armour system bottom-up (the matrix + axes + costs) and validated top-down against arms-and-armour history. The build is sound; the validation **corrected one design claim** (fatigue's role), which is logged below as the honest result.

## §1 — Build validated (self-test 7/7)

The load-bearing check: **the (attack-head × material) mitigation matrix reproduces the ratified weapon-vs-armour table EXACTLY** for all five rows × four tiers — so the new system changes **no** canonical value; it *explains* the table and extends it. Skeleton (STR-min 0/2/3/4, drain +0/+0/+1/+2, Health +4/+6/+8) reproduced. Matrix structure matches history (plate deflects cut / gaps for point / transmits blunt; mail stops slash but bursts to thrust). Trade-off ordering, coverage, and material-fidelity all pass.

## §2 — Top-down precedent check (combat-sim runs)

| Test | Result | Verdict |
|---|---|---|
| **Weapon head vs plate** (strikes to fell a full-harness foe) | blunt 3.0–3.1 · point 5.5–5.6 (gaps) · cut 6.2 (deflected) | ✓ exactly history — blunt transmits, point finds gaps, cut skates off |
| **Coverage** (partial vs full) | breastplate falls faster than full harness (longsword 3.3 vs 4.4; rapier 5.0 vs 5.5) | ✓ partial leaves limbs exposed |
| **Plate vs unarmoured** (short engagement) | plate ~82% and rising with fight length | ✓ — see §3 |
| **Mail** | cut mitigated more than thrust (rings stop the slash, a point bursts them) | ✓ — the historical rise of the thrust |

## §3 — The corrected finding (fatigue's real role)

**The design spec claimed armour's fatigue cost would "erode plate's advantage in a long duel." The validation falsified that, three ways:**
- A long stand-and-trade duel: plate stays ~96% (it doesn't erode).
- A *progressive* out-of-breath penalty: still ~96% — **symmetric fatigue cancels** (both fighters lose the same dice; plate's mitigation edge is never offset).
- A light fighter *kiting* the plate wearer: the kiter wins ~0% — **while kiting, neither lands, so the plate fighter simply waits it out**; when the kiter engages, mitigation negates its hits.

**The honest, historically-correct conclusion (stronger than the original claim):** a fresh, equally-skilled man in **full plate harness is ~95% dominant 1v1 against an unarmoured/lightly-armed opponent — and that is correct, not a bug.** Full plate genuinely was that dominant; it is *why* a harness cost a fortune and *why* specialist anti-armour tools existed. The period's real counters to plate are **exactly the three the sim validates** — and none of them is "tire him out" in a duel:
1. **Blunt percussion** (poleaxe/mace/war-flail) — transmits through plate; fells in 3. ✓
2. **Thrusts to the gaps** (rapier/estoc, half-swording, the rondel dagger) — the point retains its mod vs plate. ✓
3. **Grappling / half-sword → dagger** — wrestling the armoured man down (a *future* mechanic, not yet modelled).

**Fatigue's correct role is therefore re-scoped:** it is the **canonical per-action drain as a cost/constraint** — heavy armour shrinks your action budget, enforces the Stamina-floor wield-limit (can't drop ≤1), and is exhausting **across a campaign/day** (the strategic-attrition layer) — **not** a 1v1 duel equaliser. The σ-tempo penalty likewise is a real but *modest* cost (plate is a step slow), not a plate-defeating one. The design spec's "fatigue erodes the long duel" line is **struck** and replaced by this.

## §4 — What this means for the system (all validated)

- **Armour is mitigation** (matrix), reproducing canon; plate's 1v1 dominance is intended and historical.
- **The counters are weapon/technique, not endurance** — which makes the **weapon `head` choice vs armour material** the central tactical decision (blunt for plate, point for gaps, cut for the unarmoured), and gives the blunt/point weapons their *raison d'être*.
- **Coverage** makes "aim for the gaps" real; **material** distinguishes mail (anti-cut) from plate (anti-everything-but-blunt).
- **Fatigue + tempo** are genuine *costs* (campaign attrition, action budget, a step slow), creating the armour *choice* — just not by losing a duel of equals.

## §5 — Honest limits (self-review)

- **Robust:** the mitigation matrix, the weapon-head↔material interaction, coverage, and plate's validated dominance + its three real counters. These follow from the structure and match the record.
- **Corrected:** the fatigue-erodes-the-duel claim (struck — symmetric fatigue cancels; logged above).
- **A reviewer would add:** the system has **no grappling/anti-armour-wrestling mechanic** yet — historically the *third* major plate counter — so "an unarmed/light fighter vs full plate" currently has only blunt and gaps as outs. That is a real, flagged gap (a future mechanic), not an error in what's built. And the σ-tempo penalty's magnitude is a grounded seed, not canon.

## §6 — Canon status

- **No canonical value changed** — the matrix reproduces the ratified table; skeleton reproduced.
- **New, flagged for ratification:** the **σ-tempo penalty** (armour a step slow) and the **material/coverage axes + matrix** as the generative structure. The fatigue model uses the **canonical** per-action drain only (no invented progressive penalty — that was tested and rejected).
- **Flagged gap:** a grappling/wrestling anti-armour mechanic (the third historical plate-counter) — proposed for a future module, your call.

`[GAP: grappling/half-sword-to-dagger anti-armour mechanic — historically the third plate-counter, not yet modelled; flagged for a future build.]`
`[ASSUMPTION: plate's ~95% 1v1 dominance vs unarmoured is intended (it is historically accurate); flag if you want plate less dominant, which would mean nerfing canonical mitigation — a retcon I did not make.]`
