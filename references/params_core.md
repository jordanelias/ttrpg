<!-- version: v0.14-AUD1 | sources: stage1_core_engine.md | last_updated: 2026-04-02 -->
<!-- STALE CHECK: If current ruleset version ≠ v0.14, halt and flag before using. -->
<!-- PATCHES APPLIED: PP-164 (attribute range, derived stats table, Memory/Focus definitions) -->

# params_core.md — Core Dice Engine

## Die Rule (d10)
| Face | Effect |
|------|--------|
| 1 | −1 success |
| 2–6 | 0 |
| 7–9 | +1 success |
| 10 | +2 successes (no extra die) |

Net successes = sum of all contributions (may be negative).

## TN Values
| Mode | TN | When |
|------|----|------|
| Controlled | 6 | Prepared, unhurried, favourable |
| Standard | 7 | Default |
| Desperate | 8 | Duress, exhaustion, existential threat |

Thread operations: TN 7 standard; TN 8 for Forced Resolution and Past-Oriented Pulling.

## Obstacle Scale
| Ob | Difficulty |
|----|-----------|
| 1 | Routine |
| 2 | Moderate |
| 3 | Difficult |
| 5 | Entrenched |
| 8 | Structural |
| 10 | Foundational (cap; no stacking above 10) |

Ob minimum: 1. No modifier may reduce Ob below 1.

## Degrees of Success
| Degree | Condition |
|--------|-----------|
| Overwhelming | Net ≥ 2× Ob (+1 Momentum) |
| Success | Net ≥ Ob |
| Partial | Net > 0 but < Ob |
| Failure | Net ≤ 0 |

Ob 10 exception: Overwhelming unavailable. Partial requires net ≥ 5.

## Momentum
- Range: 0–4
- Gain: Overwhelming success OR Belief achieved
- Spend: 1 Momentum = 1 automatic success (non-Thread rolls only)
- Reset: start of each session

## Pool Minimum
No penalty may reduce a pool below 1D. Ob penalties still apply at 1D.

## Expected Value (per die)
| TN | E[net] per die |
|----|---------------|
| 6 | 0.40 |
| 7 | 0.30 |
| 8 | 0.20 |

## Quick Reference — P(≥N net), TN 7
| Pool | E[Net] | P(≥1) | P(≥2) | P(≥3) |
|------|--------|-------|-------|-------|
| 4D | 1.3 | ~80% | ~50% | ~25% |
| 6D | 2.0 | ~92% | ~70% | ~45% |
| 8D | 2.6 | ~97% | ~82% | ~60% |
| 10D | 3.3 | ~99% | ~90% | ~73% |
| 12D | 4.0 | ~99% | ~95% | ~83% |

Full multi-TN tables: references/tn_full_tables.md (generate via dice-model Task 8 if absent).

## Attributes

Range: **1–7** (all attributes). Average human: 3. Creation max: 5 (one attribute only; all others ≤ 4). Advancement max: 7.
Point pool at creation: 31 points across 10 attributes. Minimum 1 per attribute.

| Group | Attributes |
|-------|-----------|
| Physical | Agility (Agi), Endurance (End), Strength (Str) |
| Mental | Cognition (Cog), Memory (Mem), Focus (Foc) |
| Social | Attunement (Att), Bonds (Bon), Presence (Pres) |
| Metaphysical | Spirit (Spi) |

**Memory (Mem):** Knowledge, experience, retention. Sets the per-History point cap — a History can never hold more points than the character's Memory score.
**Focus (Foc):** Concentration, discipline, precision under pressure. Governs Thread contact duration: Contact Rounds = Focus score (range 1–7).

## Derived Scores

| Score | Formula | Range | Notes |
|-------|---------|-------|-------|
| Health | Endurance + 6 | 7–13 | Damage buffer before Wounds |
| Composure | Presence + 6 | 7–13 | Social damage buffer before Rattled |
| Combat Pool | Agility + weapon proficiency History (points + 3) | Variable | Split Offence/Defence each round |
| Contact Rounds | Focus | 1–7 | Max rounds maintaining Thread contact (practitioners only) |
| Certainty | Spirit (starting and maximum) | 1–7 | Existential coherence; at 0 → Rendering Crisis |
| Coherence | 10 (starting); countdown to 0 | 0–10 | Personal rendering legibility |
| Resolve | Spirit | 1–7 | Maximum total Inspiration value |

<!-- patch_history: references/params_core_history.md -->
