<!-- version: v0.14+design | sources: stage6_factions.md (TTRPG), bg_v05 (BG/Hybrid) | last_updated: 2026-04-02 -->
<!-- NOTE: stage6_factions.md is STALE for BG faction mechanics. Use BG column for board game/hybrid. -->
<!-- STALE CHECK: TTRPG column from v0.14 compiled. BG column from bg_v05 design. -->

# params_factions.md — Factions

## Stats (1–7 scale)
Mandate / Influence / Wealth / Military / Intel / Stability
Seasonal cap: ±2 per stat per season (TTRPG); ±varies (BG — see accounting).

## Starting Stats
| Faction | M (TTRPG) | M (BG) | I | W (TTRPG) | W (BG) | Mil | Int | Sta |
|---------|-----------|--------|---|-----------|--------|-----|-----|-----|
| Crown | 5 | 5 | 5 | 4 | 4 | 4 | — | 4 |
| Church | 5 | 5 | 6 | 5 | 5 | 4 | — | 5 |
| Hafenmark | 4 | 4 | 4 | 5 | 5 | 3 | — | 4 |
| Varfell | 4 | 3 | 4 | 4 | 3 | 4 | — | 4 |
| Guilds | 3 | 3 | 4 | 6 | 6 | 2 | — | 5 |
| Niflhel | — | — | 5 | 4 | 4 | — | — | 4 |
| Revolution/Restoration | — | 2 | 3/4 | — | 2 | — | — | 3 |
| Löwenritter | — | 3 | 2/3 | — | — | 5/6 | 3 | 5/4 |

Note: Varfell BG Mandate 3/Wealth 3 is intentional (political isolation at game start, not their full institutional depth).

## Clock Starting Values
| Clock | TTRPG | BG (bg_v05 P-32) | Shared Loss |
|-------|-------|-----------------|-------------|
| TC | 0 | 28 | — |
| RS | 60 | 72 | RS = 0 |
| IP | 20 | 20 | — |
| PI | — | 5 | — |

## Domain Action Rules (TTRPG)
Ob = target faction's relevant stat (1–7 directly, no division).
Attacker bonus dice: own faction's relevant stat if holding faction leadership.
NPC faction rolls: relevant stat as d10 pool, TN 7.

## Ethical Framework Ob Modifiers
| Condition | Modifier |
|-----------|---------|
| Action aligned with framework | −1 Ob |
| Action contradicts framework | +1 Ob |
| Church only: reveals Thread truth | +2 Ob |

## Leadership Deviation Stability Check Obs
Crown: 2 | Church: 3 | Hafenmark: 2 | Varfell: 2 | Guilds: 2 | Revolution: 2 | Löwenritter: 2

## Unique Actions (TTRPG, from stage6)
| Faction | Action | Roll | Effect |
|---------|--------|------|--------|
| Crown | Royal Decree | Mandate vs Ob 2 | One faction stat ±1 immediate. Consecutive: +1 Ob/season. Cannot target Intel. |
| Church | Excommunication | Mandate vs target Mandate (leader) / Ob 2 (non-leader) | Strips Circles bonus; target faction Mandate −1. Reversal: Grand Debate (5 exchanges) or new Confessor. |
| Church | TC 60 Territorial Seizure | Mandate vs owner's Mandate ÷ 2 (round up, min 1) | Per-territory roll. Success: administrative control. Failure: Mandate −1. |
| Revolution | Community Weaving | Presence markers −1 Ob (base Ob 2) | Mending Mandate prerequisite: Mandate ≥ 1 |
| [Others] | See stage6_factions.md §8.4–8.9 | — | Hafenmark, Varfell, Guilds, Niflhel, Löwenritter unique actions not extracted |

[GAP: Hafenmark/Guilds/Niflhel/Löwenritter unique actions — read stage6_factions.md §8.4–8.8]

## Nine Political Axes (qualitative — not tracked numerically)
1. Sovereignty: Crown authority vs Church authority
2. Knowledge: Thread truth accessible vs suppressed
3. Legitimacy: Constitutional monarchy vs Theocratic governance
4. Cultural identity: Einhir recovery vs Colonial settlement
5. Economic control: Guild autonomy vs State/Church taxation
6. Military authority: Ducal/Crown vs Templar independence
7. Information: Transparency vs Secrecy
8. External threat: Accommodation vs Resistance to Altonia
9. Ontological: World as it appears vs World is more

## Faction NPC Trigger Conditions (key)
| NPC | Trigger | Effect |
|-----|---------|--------|
| Ehrenwall | Coup trigger | Martial Law; Crown Loyalty check |
| Vaynard | TK threshold | Research acceleration |
| Baralta | TC suppression | Church Mandate −1/season while Mandate ≥ 4 |
| Schoenland | Active spoiler | Various faction disruptions |

RS ≤ 10 adds +1 to coup/succession trigger check pools.
