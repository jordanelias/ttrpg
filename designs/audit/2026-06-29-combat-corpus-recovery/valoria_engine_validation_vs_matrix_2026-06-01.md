# Valoria Combat Engine — External Validation vs the Four-State Weapon Matrix
**2026-06-01 · validates the engine against `weapon_matchup_matrix_v2` + A0–A3 CSVs (the just-uploaded set)**

> First validation of the engine against an EXTERNAL, sourced reference rather than targets I invented. The result
> is severe and overturns earlier session claims. Verdict first, then root cause, then what it invalidates.
> `[READ: weapon_matchup_matrix_v2.md 294 ln full; matrix_A0/A1/A2/A3 CSVs 17×17 full]`
> `[SELF-AUTHORED — bias risk: this is my engine; the reference is independent and I am reporting against my own prior
>  "reach curve fixed" claim, which this refutes.]`
> `[CONFIDENCE: high — 440 cells, 4 armour states; MC n≈600–1500, ±2–4pp, far below the effect sizes.]`

## VERDICT — the engine FAILS the external matrix, badly, on a structural axis
| State | both-armour | mean &#124;Δ&#124; vs reference |
|---|---|---|
| A0 unarmoured | none | **38.8 pp** |
| A1 textile/mail | light | **39.7 pp** |
| A2 transitional | medium | **43.7 pp** |
| A3 full plate | heavy | **49.8 pp** |

**Direction (who is favoured, |ref−50|≥8): 33% correct — WORSE than a coin-flip.** A blind 50%-everywhere predictor
scores ~25pp mean error; my engine scores 39–50pp and inverts the favourite two-thirds of the time. The engine is
**anti-correlated with the reference on the single axis the reference is most confident about: reach.**

This is not 110 independent miscalibrations. It is **two structural faults** producing a near-systematic inversion.

## ROOT CAUSE — reach is mis-weighted; tempo dominates the close (the "fix" was local, the disease is general)
The inversion is **specific to long-vs-mid-reach pairs**, which is most of the matrix:
| A0 pair | reach gap | my engine | reference | |
|---|---|---|---|---|
| spear vs **dagger** | 3.3 (huge) | 82 | 95 | ok |
| longsword vs **dagger** | 2.8 | 53 | 90 | low but right side |
| **spear vs arming** | 1.3 | **8** | **80** | INVERTED |
| **longsword vs arming** | 0.8 | **5** | **75** | INVERTED |
| **poleaxe vs dagger** | 2.3 | **28** | **90** | INVERTED |
| **staff vs dagger** | 2.3 | **37** | **85** | INVERTED |

**My engine only rewards reach against the very shortest weapon (dagger); for every smaller gap it INVERTS.** Cause
is the same class as the longsword-vs-spear bug I reported "fixed": a mid-reach, fast weapon (arming sword, tempo 2.9)
closes the modest gap in ~1–2 beats and then **out-tempos the long weapon in the closed phase**, so the faster weapon
almost always wins. My readiness-reset + pole-tempo fixes addressed only the *one pair I tested* (longsword-vs-spear,
now 53%). The underlying defect — **reach contributes almost nothing once closed, and closed-phase tempo decides
nearly everything** — is general and remains. The reference's central, high-confidence claim is the opposite: *reach
governs the unarmoured fight.* My engine encodes "tempo governs the fight," which is wrong for A0/A1.

Two compounding faults, ranked:
1. **[CRITICAL] Reach under-weighted / closed-phase tempo over-weighted.** Reach should *dominate* A0 (the reference
   weights reach=1.00 unarmoured, and reach-tools — pike/spear/halberd/greatsword — top the field). In my engine a
   weapon's reach edge evaporates the instant the shorter weapon closes, and closing is fast and cheap. Net: the
   *shorter, faster* weapon wins almost every non-dagger matchup. This single fault explains most of the 33% sign
   score. **The "reach curve is fixed and monotonic" claim from the prior turn is RETRACTED** — it was tuned to four
   hand-picked pairs (spear/rapier/longsword vs dagger + longsword-vs-spear) and does not generalise; against the
   full 11×11 it inverts.
2. **[CRITICAL] Armour-defeat absent → poleaxe/mace inverted in every state.** mace-vs-poleaxe is +83 wrong; poleaxe
   is bottom in my engine (tempo-starved, per the prior finding) where the reference puts it **apex in A2/A3** (the
   single most robust armoured result: concussion defeats plate). My `armor_defeat_bonus` is wired but inert because
   the slow weapon never lands. The reference's whole A2/A3 ranking (poleaxe/longsword-half-sword/estoc top; cut-
   swords bottom) is essentially **absent** from my engine — armour in my engine is a flat damage-reduction scalar
   with no weapon-class rotation, so plate doesn't re-sort weapons the way the reference (and history) require.

## WHAT THIS INVALIDATES (prior-session claims, corrected)
- ❌ **"Reach curve fixed and monotonic"** (re-tune progress #2) — RETRACTED. True only for the tested pairs; the
  full matrix shows systematic inversion at small/medium reach gaps.
- ❌ **"Full spectrum holds"** — the spectrum I validated was ~8 matchups I chose; the 440-cell external check fails.
- ⚠ **The 95% cap** still does its job (no cell is 100/0) but it now also *masks* the inversion — a capped 5% on an
  inverted pair still reads as "the wrong side wins 95%." The cap is cosmetic over a structural error.
- ✓ **Not invalidated:** mirror=50, mastery dominant (H6v3 78), the architecture/resolver/substrate separation, the
  σ-core. The engine is internally coherent; it is *externally wrong on reach and armour rotation*.

## WHAT THE ENGINE MUST CHANGE (the real re-tune, re-scoped from the matrix)
The matrix is a **parametric model with explicit structure** (§4): six attributes (reach/cut/thrust/percussion/clinch/
control) + gap-thrust, logistic over three differences (lethality-in-state, reach, clinch), with **reach weight high
unarmoured falling to low in plate, clinch weight rising**. My engine should adopt that shape:
1. **[CRITICAL] Make reach a standing advantage that does NOT vanish on closing.** The longer weapon keeps a measure
   edge throughout (the reference never lets the dagger reach parity vs a spear unarmoured — 5%). Options: a
   persistent per-exchange reach term (not just an approach stop-hit), and/or sharply raise the cost/così of closing
   so the short weapon pays heavily and stays disadvantaged even inside. Target A0: spear>arming ~80, longsword>arming
   ~75, staff/poleaxe>dagger ~85–90, NOT just spear>dagger.
2. **[CRITICAL] Armour must rotate the weapon ranking, not just scale damage.** Implement the reference's state
   rotation: A0 reach-led → A3 armour-defeat-led. Concretely: cut-multiplier collapses with armour (cut→~0.1 vs
   plate), thrust gated to gaps (gap-thrust factor), percussion multiplier *rises* with armour, and the reach weight
   falls while clinch rises. Then poleaxe/mace rise to apex in A2/A3 and cut-swords (sabre) sink — currently neither
   happens.
3. **[CRITICAL] Fix poleaxe viability FIRST** (prior finding stands) so the now-meaningful percussion multiplier has
   a weapon that can act.
4. Re-validate against all four CSVs; target sign-agreement ≥80% and mean |Δ| ≤15pp (the reference itself only claims
   band/ordering accuracy, so matching *direction + tier* is the bar, not the digits).

## METHOD NOTE / CAVEATS
- Mapped my 11 weapons → reference codes (rapier→RAP, arming→ASW, longsword→LSW, greatsword→GST, sabre→SAB,
  dagger→DAG, paired_short→S+B, spear→SPR, staff→QST(blunt 2H handy) , mace→MAC, poleaxe→PAX). staff→QST is the one
  loose map (mine is a blunt staff; QST fits). Armour none/light/medium/heavy → A0/A1/A2/A3.
- The reference is explicitly a **calibrated-judgment model, not data** (`[GAP: no measured win-% dataset]`), and is
  itself `[SELF-AUTHORED — bias risk]` by its author, tuned to their priors (§9.2). So this validates my engine
  against *a sourced expert prior*, the best available anchor — not against ground truth. But the qualitative
  findings it rests on (reach governs unarmoured; armour-defeat governs plate; cuts die vs plate) are **high-
  confidence and cross-culturally corroborated**, and those are exactly what my engine gets backwards.

## State
Engine UNCHANGED this turn (validation only). Findings supersede the prior "reach fixed" status. The joint re-tune is
re-scoped above around the two critical structural faults. Architecture/resolver/substrate intact. Nothing committed.
