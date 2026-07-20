# Cross-System Attribute-Weight Standard

**Principle (Jordan, 2026-05-28):** Valoria does not require uniform cross-system resolution *methodology* in the videogame, so long as the different systems apply **roughly equivalent weight to player/faction attributes** in how those attributes impact each system's outcomes.

**Consequence for decision 1:** σ-space (Option A) for the combat modifier system is **accepted** — methodology may diverge from other systems. What must hold is attribute-weight equivalence, formalized below.

---

## Formalization: effective attribute weight = σ-leverage

"Weight in how attributes impact a system" = **outcome shift per +1 attribute point**, measured in standard-deviation units of that system's outcome distribution:

```
σ-leverage = (0.4 × multiplier) / (0.8 × √(baseline pool))      [per +1 primary attribute point, TN7]
```

**Why σ-units, not the raw multiplier:** because of the √N effect, the *same multiplier* gives *different outcome-leverage* at different baseline pool sizes. A ×2 system at 6D baseline (0.41σ/pt) gives ~63% more leverage than a ×2 system at 16D baseline (0.25σ/pt). Equivalence therefore requires comparable multipliers **and** comparable baseline pool scales — captured in one number by σ-leverage.

**The σ-space modifier system (Piece 2) uses the same currency** — modifier impact and attribute weight are both measured in σ-units. One currency serves both the F1/F2 fix and this cross-system standard.

---

## Reference target

**~0.30σ per primary-attribute point at the "typical" profile (attribute 3, History 2 → ~11D pool).**

Any system — existing or new — should deliver primary-attribute leverage within a rough band of this (proposal: ±20%, i.e. 0.24–0.36σ/pt at typical) to satisfy the equivalence principle. Sim-tunable band.

---

## Verified findings (current systems)

| System | Pool formula | Typical pool | σ-leverage | vs reference |
|---|---|---|---|---|
| **Combat** | (Agi × 2) + History + 3 | 11D | 0.302σ/pt | reference |
| **Thread** | (Spirit × 2) + History + TPS | 11D | 0.302σ/pt | **exact match ✓** |
| **Social (Argue)** | (Primary × 2) + History *[no +3]* | 8D | 0.354σ/pt | **+17%** |
| **Mass battle** | min(Size, Command) + Command | (ranges unverified) | ×2-effective on Command in Command-limited regime | structurally consistent; magnitude unverified |

### Detail

- **Combat = Thread:** identical construction (×2 primary, +constant, ~11D baseline). Exact equivalence. The social_contest design doc explicitly states it "follows the same pool construction pattern as combat" — the parallel is deliberate, not coincidental.
- **The ×3 in social is resource-side, not roll-side.** Composure = Charisma × 3 is the social *damage buffer* (parallel to combat's Health), NOT the contest roll. The contest roll (Argue Pool) is ×2, matching combat. Earlier worry about a ×3 social roll was misplaced.
- **Social Argue divergence (+17%):** the Argue Pool lacks combat's `+3` floor, so its baseline is ~3D smaller (8D vs 11D), giving ~17% more outcome-leverage per attribute point. A point invested in a social primary attribute is modestly more impactful than a point in Agility-for-combat.
- **Mass battle:** `min(Size, Command) + Command` gives `+1 Command = +2 pool` when Command ≤ Size — effective ×2 leverage on the faction attribute, structurally matching personal scale. Whether the *baseline magnitude* matches (so Command-leverage ≈ personal-attribute-leverage) depends on the Size/Command numeric ranges, which are **unverified** here.

---

## Action items (cross-system, mostly outside combat scope)

1. **Social Argue +3 floor** — `[DECISION for Jordan]` add `+3` to Argue Pool for exact combat parity (0.302σ/pt), or accept the +17% as within "rough equivalent." This is a social_contest_v30 change, not a combat change.
2. **Mass battle range verification** — `[GAP]` confirm Size/Command ranges produce a baseline effective pool comparable to personal ~11D, so faction-attribute leverage ≈ personal-attribute leverage. Requires reading mass_battle_v30 stat ranges.
3. **Fieldwork + remaining personal systems** — `[GAP]` not yet checked against the standard (fieldwork is largely deterministic five-filter, so attribute leverage may enter differently; verify).
4. **Adopt σ-leverage as the calibration check** for any new system or rebalance: compute σ-leverage at the typical profile, require it within ±20% of 0.30σ/pt.

---

## Implication for the combat implementation

Combat's attribute structure (Agi × 2, +3 floor, ~11D typical baseline) **sits at the reference** and is confirmed consistent with the equivalence principle. The combat work needs **no change** to attribute weighting to satisfy Jordan's constraint — it *is* the reference. σ-space (now selected) is the natural currency for keeping it there and for the modifier system (Piece 2).

`[CONFIDENCE: high on combat/Thread/social Argue (verified formulas); medium on mass battle (structure verified, magnitude unverified); the ±20% band is a proposed standard, sim-tunable]`
`[READ: designs/scene/social_contest_v30.md §pool-construction (L99,110,421) — Argue Pool formula; designs/provincial/mass_battle_v30.md L26,403,713 — Effective Combat Pool formula]`
`[SELF-AUTHORED — bias risk: I verified the social formula rather than assuming; the +17% divergence is reported as a real finding requiring a Jordan decision, not smoothed over]`
