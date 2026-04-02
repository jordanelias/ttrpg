<!-- version: v0.14 | sources: stage6_factions.md | last_updated: 2026-03-26 -->
<!-- STALE CHECK: If current ruleset version ≠ v0.14, halt and flag before using. -->

# params_factions.md — Factions

## Faction Stats (1–7 scale)
Mandate / Influence / Wealth / Military / Intel / Stability

Seasonal cap: ±2 per stat per season.

## Starting Values
| Faction | M | I | W | Mil | Int | Sta |
|---------|---|---|---|-----|-----|-----|
| Crown | 5 | 5 | 4 | 4 | — | 4 |
| Church | 5 | 6 | 5 | 4 | — | 5 |
| Hafenmark | 4 | 4 | 5 | 3 | — | 4 |
| Varfell | 4 | 4 | 4 | 4 | — | 4 |
| Guilds | 3 | 4 | 6 | 2 | — | 5 |
| Niflhel | — | 5 | 4 | — | — | 4 |
| Revolution | — | 3 | — | — | — | 3 |
| Löwenritter | — | 3 | — | 5 | 3 | 5 |

Partial sheets: Niflhel (no Mandate, no Military), Revolution (Influence/Stability/Intel only), Löwenritter (no Mandate, no Wealth).
Schoenland: spoiler actor, not a playable faction.

## Domain Action Ob
Target faction's relevant stat directly (1–7 = Ob 1–7). No division.
Attacker may add own faction's relevant stat as bonus dice if holding leadership.
NPC factions: roll relevant stat as d10 pool, TN 7.

## Ethical Framework Ob Modifiers
| Condition | Ob Modifier |
|-----------|------------|
| Action aligned with framework | −1 Ob |
| Action contradicts framework | +1 Ob |
| Church only: reveals Thread truth | +2 Ob |

## Leadership Deviation Stability Check Obs
| Faction | Ob |
|---------|----|
| Crown | 2 |
| Church | 3 |
| Hafenmark | 2 |
| Varfell | 2 |
| Guilds | 2 |
| Revolution | 2 |
| Löwenritter | 2 |

## Clocks (Starting Values)
| Clock | Start | Win threshold | Loss threshold |
|-------|-------|---------------|---------------|
| RS (Resonance Score) | 72 | — | 0 (campaign collapse) |
| TC (Theocracy Clock) | 0 | 100 (Church institutional win) | — |
| IP (Inquisitor Presence) | 0 | — | 100 |

TC generation: Church Mandate ≥ 5 at accounting → +1 TC/season. Pauses if Church Stability ≤ 4.
TC 60 triggers: Church territorial seizure procedure available.

## Unique Actions (summary)
| Faction | Action | Roll | Key Effect |
|---------|--------|------|-----------|
| Crown | Royal Decree | Mandate vs Ob 2 | Bypass timing; one faction stat ±1 immediate. Consecutive use: +1 Ob/season. |
| Church | Excommunication | Mandate vs target Mandate (leader) or Ob 2 | Strips Circles bonus, Mandate −1 to target faction. |
| Hafenmark | [See stage6] | — | — |
| Varfell | Patience Protocol | — | PC counter; Casus Belli on exposure |
| Guilds | [See stage6] | — | — |
| Niflhel | [See stage6] | — | — |
| Revolution | Community Weaving | — | Presence markers; Mending Mandate |
| Löwenritter | [See stage6] | — | — |

[GAP: Unique actions for Hafenmark, Guilds, Niflhel, Löwenritter not extracted — read stage6_factions.md §8.4–8.8]
