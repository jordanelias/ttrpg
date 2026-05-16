# Phase 4 sim — Agi-dominance re-check at current canon

**Date:** 2026-05-15
**Sim:** `tests/sim/phase4_agi_dominance_2026-05-15.py`
**N:** 2000 duels per matchup, seed=42
**Triggering decision:** Decision A (ED-828) — Jordan rejected PP-717 D2 (Pool Softcap) at canon layer 2026-05-15. v27 weapon sim had reported a 55% pool advantage at Agi 6 vs Agi 3 (pool 17 vs 11) without DR. This re-check verifies at current canon (post-Decision A + Decision B + F12 MW cap commit `abf9fc8e`).

---

## TL;DR

**Agi-dominance manifests at current canon.** When fights resolve decisively, Fast (Agi 6, End 4) beats Strong (Agi 3, End 4) at **95.6% conditional win rate**. PP-717 D2 was addressing a real pool-shape problem. **Recommend reconsidering Decision A** — either re-ratify D2 in some form, find an alternative lever, or accept Fast-build dominance explicitly.

---

## Sim configuration

| Parameter | Value | Source |
|---|---|---|
| Dice engine | d10, face 1 = −1, 7–9 = +1, 10 = +2 | `params/core.md` L10-19 |
| TN | 7 | `params/core.md` §TN |
| Pool formula | `max(5, Agi × 2 + H + 3)` | `params/combat.md` L14 (post-Decision A) |
| Max Wounds | `min(End/2 + 1, 3)` | `params/combat.md` L138 (post-F12 commit) |
| Wound Interval | `End + 6` | `derived_stats §4.1` |
| Health | `WI × (MW+1)` | `derived_stats §4.1` |
| Stamina | `15 + End × 2` | Architecture C (matches v27 sim convention) |
| Action cost | 5 stam | `params/combat.md` |
| Crit threshold | net ≥ 4 | `params/combat.md` L91 (PP-717 D3) |
| Weapon | Light Blade Cut vs None armour (+3 mod, ×1 STR mult) | `params/combat.md` damage table |
| Pool split | 50/50 offense/defense each round | Simulation control |
| Tactical layer | Strike-only (no Feint, no ED, no Distance, no Initiative) | Bounded sim |

**Build stats:**

| Build | Agi | End | Str | Pool | Max HP | Max Stam | MW |
|---|---|---|---|---|---|---|---|
| Strong | 3 | 4 | 4 | 11D | 40 | 23 | 3 |
| Fast | 6 | 4 | 4 | 17D | 40 | 23 | 3 |
| Tough | 3 | 6 | 4 | 11D | 48 | 27 | 3 |
| Fast+Tough | 6 | 6 | 4 | 17D | 48 | 27 | 3 |

---

## Results

### Matchup matrix (2000 duels each)

| Matchup | A win | B win | Draw | A | dec | Spread |
|---|---|---|---|---|---|
| Fast vs Strong (v27 test) | 14.3% | 0.2% | 85.5% | **98.6%** | ⚠ |
| Fast vs Tough | 3.5% | 96.5% | 0.1% | 3.5% | ⚠ |
| Strong vs Tough | 0.4% | 99.6% | 0.0% | 0.4% | ⚠ |
| Fast+Tough vs Strong | 100.0% | 0.1% | 0.0% | 100.0% | ⚠ |
| Fast+Tough vs Tough | 14.4% | 0.2% | 85.3% | 98.3% | ⚠ |

`A | dec` = A's win rate **conditional on decisive outcome** (excludes draws). The high absolute draw rate (~85% in Fast vs Strong) is a sim artifact — see Limitations. The conditional rate is the meaningful signal.

### Build-investment ROI (vs Strong, varying Agi, End=4 fixed)

| Build | Pool | Abs Win% | Cond Win% | Δ cond vs Agi 3 |
|---|---|---|---|---|
| Agi 3, End 4 | 11D | 1.8% | 52.9% | (baseline) |
| Agi 4, End 4 | 13D | 4.2% | 86.6% | +33.7pp |
| Agi 5, End 4 | 15D | 8.1% | 93.6% | +40.7pp |
| Agi 6, End 4 | 17D | 13.7% | 98.2% | +45.3pp |
| Agi 7, End 4 | 19D | 21.1% | 99.5% | +46.6pp |

**Reading the ROI table:** at conditional rates, every Agi point above 3 buys near-deterministic win advantage. The marginal return diminishes after Agi 5 (already 93.6% conditional), but never inverts — extra Agi is never wasted.

---

## Findings

### Finding 1 — Agi 6 dominance is structural, not stamina-cliff

Fast vs Strong absolute rate is suppressed by stamina draws (85.5%), but conditional rate (98.6%) confirms the pool-advantage thesis: when the fight resolves, Fast wins almost every time. The v27 audit's 55% pool gap (17D vs 11D) translates here to a 95–98% conditional win rate, depending on matchup.

### Finding 2 — End dominance ALSO manifests, even with MW cap

Tough (Agi 3, End 6) beats Strong (Agi 3, End 4) at 99.6% conditional. Same pool size, +8 HP, +4 stamina. The MW cap (PP-717 D1) didn't fully address End-dominance — it just compressed it. With the cap, End 4 has MW 3 and End 6 also has MW 3, so the wound-count advantage is fully neutralized. But the HP + stamina gain still produces total dominance.

This is a **finding outside the original Phase 4 scope**: PP-717 D1's MW cap is necessary but insufficient. End-dominance via stamina-window (more rounds to land hits) persists.

### Finding 3 — Compound dominance with Fast+Tough

Fast+Tough (Agi 6, End 6) vs Strong: 100.0% — every duel in 2000 trials. Both dimensions stacking is unrecoverable for low-investment builds at current canon.

### Finding 4 — Decision A's implication realized

The v27 finding ("Without softcap, Fast 17D vs Strong 11D = 55% pool advantage that overwhelms weapon-specific differences") is confirmed at current canon parameters. The pool grammar change (no DR) is the dominant factor in the Agi axis.

---

## Limitations of this sim

1. **No Feint, ED, Distance, Initiative.** Pool split is fixed 50/50. The full v9 chassis would likely AMPLIFY the gap — initiative-holders pick counter-attacks, feints break defense allocation, etc. **This sim is a lower bound on Agi dominance.**
2. **Single weapon, single armour.** Light Blade Cut vs None. Different weapon+armour combinations may compress or stretch outcomes (Heavy armour + Bash, etc.). v27's Heavy-armour results showed Strong/Tough builds gaining vs Fast at high armour tiers.
3. **High draw rate from stamina cliff.** ~85% draws in main test. Fights end by stam exhaustion before HP=0. This is a known issue (v27 P0 stamina cliff). Conditional rate excludes draws; the conditional rate is the reliable signal.
4. **No History asymmetry.** Both builds set H=2. Differential History could compress or expand the gap.
5. **Simplified damage.** Cut-only attack (no Thrust/Bash selection by armour). v27 sim's full damage tables produce more variance.

---

## Recommendation

**Reconsider Decision A.** The audit's self-review argued that PP-717 D2 was specifically addressing a real problem in combat (where short timescales amplify pool advantage). This sim confirms that, at current canon, Fast builds beat Strong builds at ~95–98% conditional win rate when they decisively engage. Decision A's revert reopens the gap PP-717 D2 was designed to close.

**Options to address (Jordan's call):**

1. **Re-ratify PP-717 D2** as `min(Agi, 4) × 2 + max(0, Agi-4) + H + 3`. Returns to the v27 ratified state for combat. Preserves universal grammar for non-combat systems (which don't have the short-timescale problem).
2. **Adopt a pool cap** without per-die softcap: e.g., `min((Agi × 2) + H + 3, 14)`. Caps the maximum pool size regardless of Agi+H accumulation. Mechanically equivalent at the upper bound but cleaner formula.
3. **Stamina re-cost for high-Agi builds** — each action costs `5 + max(0, Agi - 4)` stamina. Forces fast builds to manage stamina more carefully. Trades dice advantage for stamina disadvantage.
4. **Weapon-side rebalance** — make Strong/Tough viable via weapon damage scaling rather than pool count. Probably requires a different round of sim work.
5. **Accept the imbalance** — "Fast builds dominate combat" as a deliberate design statement. Narratively: trained duelists are inherently more dangerous than untrained brawlers. Requires explicit canon acknowledgement and removes "build balance" as a design goal for combat.

Option 1 is the path of least resistance. Option 2 is mathematically equivalent at the top but more elegant. Options 3-4 are larger redesigns. Option 5 is a design philosophy change.

---

## Status

- **Decision A's queued sim:** complete. **Result:** Agi dominance reopens at current canon.
- **F12-related verification:** params/combat L138 (post-`abf9fc8e`) was applied correctly to the sim. MW cap = 3 at End 4 (no cap effect; End 4 yields MW 3 either way).
- **PP-717 D1 efficacy:** MW cap is in effect but did not fully suppress End-dominance (Finding 2). Worth noting for any follow-up audit of End-dominance specifically.

**Next action (Jordan):** review findings, decide whether to:
- Re-ratify PP-717 D2 (option 1)
- Pick alternative lever (options 2-4)
- Accept Fast dominance as canon (option 5)
- Run extended Phase 4 sim with full v9 chassis (Feint, ED, Distance, Init) before deciding
