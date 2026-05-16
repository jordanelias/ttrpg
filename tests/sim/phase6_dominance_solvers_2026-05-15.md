# Phase 6 sim — Dominance-solver formula comparison

**Date:** 2026-05-15
**Sim:** `tests/sim/phase6_dominance_solvers_2026-05-15.py`
**Trigger:** Jordan 2026-05-15 — Phase 5 confirmed continuous engine doesn't resolve dominance alone; this sim compares pool-formula alternatives.

---

## TL;DR

**Pool formula alone does NOT solve dominance.** All five candidate formulas (current canon, drop-doubling, cap-14, cap-12, PP-717 softcap) produce 72–98% conditional Fast win — all above the 65% dominance threshold. End-dominance is even more uniform: 99.6–99.9% across all formulas.

**The doubling decision is not the structural driver.** Or rather, it's not the *only* one. The simulation surfaces a deeper finding: dominance is driven by feedback loops the pool formula doesn't reach.

---

## Pool sizes under each candidate (H=2)

| Formula | Agi 3 | Agi 4 | Agi 5 | Agi 6 | Agi 7 |
|---|---|---|---|---|---|
| `(Attr×2)+H+3` current canon | 11D | 13D | 15D | 17D | 19D |
| `Attr+H+3` non-doubled | 8D | 9D | 10D | 11D | 12D |
| Cap at 14 | 11D | 13D | 14D | 14D | 14D |
| Cap at 12 | 11D | 12D | 12D | 12D | 12D |
| PP-717 softcap | 11D | 13D | 14D | 15D | 16D |

## Headline: Fast vs Strong conditional win rate

| Formula | Fast pool | Strong pool | Fast cond win | Status |
|---|---|---|---|---|
| Current canon `(Attr×2)+H+3` | 17D | 11D | **97.8%** | DOMINANT |
| PP-717 softcap | 15D | 11D | **92.6%** | DOMINANT |
| Non-doubled `Attr+H+3` | 11D | 8D | **90.2%** | DOMINANT |
| Cap at 14 | 14D | 11D | **89.1%** | DOMINANT |
| Cap at 12 | 12D | 11D | **72.3%** | DOMINANT |

**Even at Pool cap 12** — where Fast (12D) and Strong (11D) are within 1 die of each other — Fast still wins 72.3% conditional. The 1-die gap should be marginal; instead it produces structural dominance.

## Build-investment ROI

| Formula | Agi 4 | Agi 5 | Agi 6 | Agi 7 | Δ Agi 4→7 |
|---|---|---|---|---|---|
| Current canon | 79% | 92% | 97% | 99% | +20pp |
| Non-doubled | 61% | 85% | 87% | 97% | +36pp |
| Cap at 14 | 77% | 90% | 89% | 85% | +8pp |
| Cap at 12 | 65% | 69% | 65% | 65% | **+0pp** |
| PP-717 softcap | 80% | 88% | 91% | 97% | +17pp |

Cap at 12 actually **inverts** the build investment curve — Agi 7 (65%) does no better than Agi 4 (65%). The cap is so tight it eliminates the difference between mid and high Agi.

Most striking: **non-doubled has the WIDEST spread** (+36pp). It looks compressed at the bottom (Agi 4 only 61% vs Strong) but stretches at the top because high Agi still produces gains.

## End-dominance check (Tough vs Strong, same Agi, +2 End)

| Formula | Tough cond win | Status |
|---|---|---|
| Current canon | 99.8% | DOMINANT |
| Non-doubled | 99.9% | DOMINANT |
| Cap at 14 | 99.8% | DOMINANT |
| Cap at 12 | 99.6% | DOMINANT |
| PP-717 softcap | 99.9% | DOMINANT |

**End-dominance is essentially formula-independent.** Same Agi, same pool size (11D for Tough), and Tough still wins 99.6% — because:
- Tough has more HP (48 vs 40)
- Tough has more stamina (27 vs 23 = 5 vs 4 rounds before stamina exhaustion)
- The fight goes long; Tough survives

This isn't a pool-formula problem. It's a **damage/HP/stamina-window** problem. Fixing it requires a different lever than pool sizing.

---

## Critical insight: the structural driver isn't the pool formula

Even at Pool cap 12 (12D vs 11D, only 1 die advantage), Fast wins 72%. **A 1-die gap shouldn't produce structural dominance.** What's amplifying it?

Three feedback loops the formula doesn't reach:

### 1. The wound spiral

`-1D per wound` is canonical. The first side to land a wound gets a permanent advantage that compounds. Once Fast lands a wound, Strong's already-smaller pool gets smaller. Strong's chance to recover drops. The spiral becomes deterministic.

**Even small initial advantages get amplified through wounds.** A 1-die starting gap (12D vs 11D) → first wound likely → 12D vs 10D → next wound nearly certain → 12D vs 9D → done.

### 2. Stamina window asymmetry

Both Fast and Strong have same Stamina (23, End 4). But Fast's higher damage output means Strong takes more damage per round, reaches the wound threshold faster. Strong loses BEFORE the stamina cliff hits. Fast almost never reaches stamina exhaustion in a winning duel.

For End-dominance: Tough has +4 stamina = 1 more round. That extra round is the entire margin — Tough survives long enough for variance to favor them.

### 3. Critical hit cascade

Crit threshold ≥4 magnitude. With continuous engine and Fast's higher pool (more variance), Fast generates crits more often. A crit doubles weapon mod (6 damage instead of 3) — likely enough to land a wound in one strike. One crit → wound → spiral.

### Why the pool formula can't fix this

The pool formula determines the *initial* gap. The feedback loops *amplify* whatever gap exists. Even minimal initial advantage (12D vs 11D, expected margin 0.4 successes per round) becomes terminal because:
- Variance produces occasional Fast-advantage rounds
- Those rounds land wounds
- Wounds reduce Strong's pool further
- Strong's variance becomes asymmetric (rarely lands wounds back)
- Game over

This is the **rich-get-richer** problem in dueling games. It's not unique to Valoria; it's a known phenomenon in any system where damage accumulates and pool reduces with damage.

---

## What actually addresses dominance

The pool formula is the wrong lever. The actual levers are:

### Lever A — Break the wound spiral

Options:
- Wounds restore over rounds (`Take a Breath` already does this for stamina; could extend to wound recovery)
- Wound penalty is non-cumulative (only first wound applies −1D; subsequent wounds add damage but not pool penalty)
- Wound penalty caps at −2D regardless of wound count

### Lever B — Cap the damage cascade

Options:
- Crit threshold raised (≥5 magnitude instead of ≥4 — fewer crits, less cascade)
- Crit doesn't double weapon mod (just adds wound state, no damage multiplier)
- Damage scales differently: +net adds less damage per success

### Lever C — Compress HP/stamina spread

Options:
- Health cap (all builds get 40-60 HP regardless of End — End drives Stamina/Healing instead)
- Stamina cap
- Action cost scales with End (Strong builds use less stamina, balancing the window)

### Lever D — Action triangle counter-play (already in canon, not sim'd)

Strike/Feint/Defend triangle gives skill-based counter to raw pool advantage. The Phase 6 sim is Strike-only — it disables this lever entirely. Real combat with Feint+Defend choices may produce different dominance numbers.

### Lever E — Accept dominance

Phase 6 confirms: with current mechanics minus the action triangle, Fast and Tough both dominate. **If Strong/Average builds are supposed to dominate Mass Combat, Social Contest, and Thread (where Agi/End don't matter), the cross-system balance is the answer.** Personal combat may just be a Fast/Tough domain.

---

## My recommendation

**Stop trying to fix dominance through the pool formula.** It can't reach the problem.

Three paths forward:

**Path 1 — Run Phase 7 with action triangle.** Add Feint/Defend choices to the sim. If skilled play by Strong/Average can overcome Fast/Tough dominance through tactical depth, the system is already balanced — just hidden behind the simplification of Strike-only sims.

**Path 2 — Address the wound spiral directly.** Pick Lever A or B and sim it. The spiral is what amplifies small gaps into terminal dominance.

**Path 3 — Accept and document.** Personal combat is a Fast/Tough advantage zone. Build balance is system-wide, not combat-internal. This is consistent with the Reframing 2 argument from the audit's self-review.

I lean toward **Path 1 first** — the action triangle is the most under-tested lever in the sim chain. If it solves dominance, none of the more invasive changes are needed.

## What this changes about the broader decisions

**Decision A (revert PP-717 D2):** still correct based on this sim. PP-717 D2 produces 92.6% conditional Fast win — only 5pp better than current canon's 97.8%. It wasn't actually solving the problem effectively; just compressing the curve slightly. The audit and Decision A's reversal were correct.

**Decision E (continuous engine):** still recommend adopting. Phase 5 validated equivalence; Phase 6 shows pool formula doesn't matter much for dominance — so continuous engine's other benefits (fractional modifiers, no edge cases, continuous degree) are the right reasons to adopt. The wound-spiral problem exists in discrete or continuous identically.

**The doubling question:** less urgent than it seemed. Non-doubled (90.2%) is only marginally better than current canon (97.8%). Neither solves the problem. The doubling decision should be made on **design feel** (big pools vs tight pools, talent-dominant vs talent-and-training-equal) rather than balance grounds.

---

## Status

Phase 6 sim complete. Pool formula does not solve dominance. **Next decision is which lever to pull instead.** I recommend Phase 7 sim with action triangle before committing any canon change to the engine.

Current commit chain:
- `77a3d4c0` — DR → Softcap terminology cleanup
- `5cdd4292` — Phase 5 continuous engine prototype
- `<pending>` — Phase 6 dominance-solver comparison
