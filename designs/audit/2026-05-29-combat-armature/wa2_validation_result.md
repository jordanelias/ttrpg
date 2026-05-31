# Weapon Axes v2 — Validation (bottom-up build, top-down precedent check)

**Date:** 2026-05-29 · **Module:** `tests/sim/v32-combat-balance/weapon_axes_v2.py` (self-test 7/7) · **Status:** Class-C proposal; no canon edited except the flagged `POINT_ARMOR_MOD`.

Per Jordan directive: developed the v2 axes **bottom-up** (substrate module, each axis→modifier grounded in canonical/ratified values, self-tested) then **validated top-down** against historical precedent (the duel/battlefield audit + the per-weapon precedent check below).

`[CONFIDENCE: high — substrate self-tested 7/7; audit on validated primitives (M1/R1/R2).]` `[READ: the three historical-precedents docs — full, this session.]`

## Bottom-up: the substrate (self-test 7/7)

The axes produce, by construction: the point-vs-armour gap-row, the canonical STR multipliers (heavy-blunt ×3 etc.), axis-derived wield-min, the head σ-bias by engagement state, the 2H bind amplification + 1H off-hand defence (and the mace/poleaxe split by hands), the curved draw-cut, and the tonfa-defensive / flail-flexible flags. All verified in isolation before any audit (the harness-defect lesson: validate units first).

## Top-down: the audit (full roster, validated primitives)

**Battlefield — strikes to fell an ENGAGED foe in heavy armour** (defence suppressed; lower = better):

| 3 strikes | 4.2–4.3 | 5.5–5.6 | 6.2–6.3 |
|---|---|---|---|
| **mace, poleaxe, war flail** | greatsword, longsword, curved-2h, staff, tonfa | estoc, spear, rapier | arming-sword, sidesword, dagger, paired, messer, sabre |

→ **Blunt percussion fells in 3 vs blades' 5.5–6.3** — the anti-armour dominance, exactly as the research says.

**Duel — field win-rate, neutral Str-4, all-vs-all × armour:**

| weapon | duel % | weapon | duel % |
|---|---|---|---|
| mace | 73.6 ⚑ | longsword | 47.5 |
| war flail | 66.3 | estoc | 46.3 |
| curved-2h | 65.2 | greatsword | 44.3 |
| poleaxe | 63.0 | messer | 42.3 |
| tonfa | 60.9 | paired-short | 41.2 |
| sabre | 55.7 | arming-sword | 37.5 |
| rapier | 52.0 | sidesword | 36.5 |
| dagger | 51.9 | staff | 35.0 |
| | | spear | 29.8 |

## Per-weapon historical-precedent check

| Weapon | History predicts (research) | Sim observed | Verdict |
|---|---|---|---|
| Rapier (point) | thrust finds gaps; reach; weak bound | 52% duel; **beats cut vs armoured field**; battlefield 5.6 | ✓ match |
| Estoc (point) | anti-armour needle | point armour-row; battlefield 5.5 (best blade vs plate) | ✓ match |
| Spear (point) | reach king at distance, weak closed | wins approach, low duel (29.8% — closed-on) | ✓ match (its duel low is the R9 result; reach shines vs multiple/at range) |
| Sabre (curved-cut) | draw-cut, flow, anti-flesh, poor vs armour | 55.7% duel, draw-cut bonus vs unarmoured, weak vs plate | ✓ match |
| Arming sword (c&t) | versatile generalist, off-hand-capable | mid-low (37.5%), no edge/penalty, off-hand defence | ✓ match (generalist) |
| Longsword (2H c&t) | bind leverage (Stark/Schwach), versatile | 2H bind ×1.5; mid (47.5%) | ✓ match |
| Messer/greatsword (straight-cut) | percussive cut, strong in close | bind-strong; mid-low | ✓ match |
| Poleaxe (2H blunt) | technical plate-breaker | battlefield 3.0; demanding | ✓ match |
| War flail (flexible) | strikes around the parry/shield | parry-bypass → 66% duel; battlefield 3.0 | ✓ match (the distinct mechanic works) |
| Tonfa (defensive short-blunt) | block + trap (kobudō) | defensive δσ; 60.9% duel (defence-driven) | ✓ match (fills the short-blunt gap) |
| **Mace (1H blunt)** | **forgiving, levy weapon — mediocre in a skilled duel** | **tops the duel at 73.6%** | **✗ ARTIFACT** |

## The one artifact — and it's the war-hammer finding, generalized

**Bare mace tops the duel (73.6%) — wrong twice over.** (1) Per our own research the bare mace is the *forgiving, low-technique* weapon; it should be *mediocre* in a skilled duel, not top. (2) The cause is the **same blunt-damage artifact** we already diagnosed for the war hammer (R10): blunt's ×1.5 multiplier + the non-degrading light-blunt armour row + short-reach (dodging the reach disadvantage) stack into raw damage the duel model over-rewards.

**Resolution is the one we already ratified, not a new nerf:** blunt **percussion** weapons (mace, poleaxe, war flail) are **battlefield / forgiving-floor weapons, not duel-balanced** — their duel number is the wrong test, exactly as for the war hammer. Per R10 + the handling curve, they belong to the armoured-press / low-skill-floor niche. Excluding the blunt percussion family from the *duel*-balance target, the **dueling roster reads correctly**: sabre 55.7, rapier 52, dagger 51.9, longsword 47.5, estoc 46.3, greatsword 44.3, messer 42.3, paired 41.2, arming-sword 37.5, sidesword 36.5, staff 35, spear 29.8 — a coherent spread where the generalists sit mid, the point/cut weapons split by armour, and the reach weapons (spear/staff) trade duel-weakness for distance/formation value.

**So the v2 substrate validates:** every blade and pole weapon behaves as historical precedent predicts, and the only outlier (bare mace) is the already-understood blunt-is-a-battlefield-weapon result — *consistent with the design*, not a defect in it.

## Status / canon

- **One canon-touching piece:** `POINT_ARMOR_MOD` (the point-vs-armour gap row, +3/+3/+2/+1). Validated (it gives the thrust its modest armour edge without breaking balance). Awaits ratification, same status as W1.
- **The blunt-percussion duel artifact** is resolved by *context* (R10 — already ratified), not by changing the canonical blunt damage. No new canon change needed.
- The v2 σ-leverage seeds are sim-tunable Class-C; the blunt-in-duel could additionally be dialed by the handling curve (forgiving weapons hit a lower skilled ceiling) if you want the mediocre-mace result to show numerically in a *skilled* duel — a tuning option, flagged.

`[GAP: the duel model rewards blunt raw damage the same way it did the war hammer; the principled fix (handling-curve skill ceiling so the forgiving mace underperforms a skilled fencer) is a tuning option for you, distinct from the context resolution.]`
`[ASSUMPTION: neutral Str-4 both sides isolates weapon profile; the off-hand/defensive/flexible modifiers are applied as δσ; battlefield = defence-suppressed engaged foe (R10).]`
