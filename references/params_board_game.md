<!-- version: v0.14+design | sources: stage_bg_board_game_mode.md, designs/board_game/valoria_bg_v05_simulation_and_patches.md | last_updated: 2026-04-02 -->
<!-- STALE CHECK: BG params include v05 design patches. Values marked [v05-PATCH] supersede stage_bg content where they conflict. -->
<!-- BG editorial blockers pending: BG-E-30 (Card-Hand adoption) and others — see canon/editorial_ledger.yaml. -->

# params_board_game.md — Board Game Mode

## Dice System [v05-PATCH — CORRECTION 1]
Same d10 engine as TTRPG. Supersedes all prior d6 references.
| Face | Effect |
|------|--------|
| 1 | −1 success |
| 2–6 | 0 |
| 7–9 | +1 success |
| 10 | +2 successes |

Majority-1s override: If dice showing 1 outnumber dice showing 7–10 → Catastrophic Failure (Failure + one additional consequence).
Negative net successes = treated as 0 for degree purposes; Catastrophic Failure if majority-1s also fires.

## Ob Rules [v05-PATCH — CORRECTION 2]
Ob minimum = 1. No modifier may reduce Ob below 1. Modifiers that would push below 1 are wasted.

## Degree Table [v05-PATCH — CORRECTION 3]
| Net Successes | Degree |
|---------------|--------|
| Ob + 1 or more | Overwhelming |
| = Ob | Success |
| Ob − 1 | Partial |
| 0 | Failure |
| Negative | Failure (Catastrophic if majority-1s also fires) |

## Faction Pools
Faction stat (1–7) = dice pool for BG domain actions. TN 7 standard.
| Pool | E(net) | P(≥1) | P(≥2) | P(≥3) |
|------|--------|-------|-------|-------|
| 2 | 0.80 | ~58% | ~22% | ~5% |
| 3 | 1.20 | ~74% | ~40% | ~15% |
| 4 | 1.60 | ~85% | ~56% | ~27% |
| 5 | 2.00 | ~91% | ~69% | ~42% |
| 6 | 2.40 | ~95% | ~80% | ~57% |
| 7 | 2.80 | ~97% | ~88% | ~69% |

## Key Resolved Patches (v05)
| Patch | Issue | Resolution |
|-------|-------|-----------|
| P-12 | Majority-1s used d6 language | Updated to d10 threshold (7–10) |
| P-13 | Varfell Patience Protocol body text contradicted P-07 | Body updated: +1 PC max/season from inaction |
| P-14 | Casus Belli expiration contradiction | Treaty CB: permanent. Other CB: 3 seasons. Varfell PC CB: expires on exposure. |
| P-15 | Faction Collapse: Mandate freeze contradiction | Mandate drops to 0 first, then all OTHER attributes freeze |
| P-16 | Battle resolution: no compare rule for both sides rolling | Compare net successes; margin determines outcome tier |
| P-17 | Restoration RS≥50 win condition framing | Explicit: RS≥50 must be met at moment of declaration |
| P-18 | Phase 4 tiebreaking (2-way vs 3-way) | 3+ tied on Stability: alphabetical order |
| P-19 | Parliamentary Manoeuvre interrupt scope | Applies to Crown Policy Instrument only (once/season bonus), not normal card plays |
| P-20 | Fog of War boundary roll used d6 | d6 exception noted explicitly (50/50 coin-flip, not success-count) |

## Faction Collapse [v05-PATCH P-15]
On collapse: Mandate → 0 immediately. All other stats freeze at pre-collapse values. Mandate drop occurs before freeze snapshot.

## Ob Modifier Stacking Examples [v05-PATCH floor check]
Church in TC 30–49 with doctrine-aligned −1 + territory −1 + framework −1 on Ob 3 = Ob 1 (not 0). Floor holds.

## Fog of War (Hybrid Interface) [v05-PATCH P-20]
Stats 1–3: Poor (observed as-is). Stats 5–7: Good. Stat exactly 4: roll 1d6 (not d10) — 1–3 Poor, 4–6 Good.

## Editorial Blockers (do not simulate card-hand system until resolved)
BG-E-30: Card-Hand adoption — BLOCKER for all Tier 1 work.
See canon/editorial_ledger.yaml for full list.
