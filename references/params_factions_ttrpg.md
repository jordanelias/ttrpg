<!-- version: v1.0 | source: designs/ttrpg/factions_ttrpg_v30.md | last_updated: 2026-04-13 -->
<!-- PATCHES APPLIED: SIM-FAC verification pass 2026-04-13. No mechanical changes. -->
<!-- SIM STATUS: VERIFIED — domain actions, unique actions, ethical framework modifiers -->

# params_factions_ttrpg.md — TTRPG Faction Mechanics

## Faction Stats — 1-7 Scale
| Stat | Represents |
|------|-----------|
| Mandate | Public legitimacy and popular support |
| Influence | Political reach and diplomatic weight |
| Wealth | Economic capacity |
| Military | Armed force and unit capacity |
| Intel | Intelligence network and covert operations |
| Stability | Internal cohesion and crisis resistance |

## Starting Values (game start, 45 AG)
| Faction | Mandate | Influence | Wealth | Military | Intel | Stability |
|---------|---------|----------|--------|----------|-------|-----------|
| Crown | 5 | 5 | 4 | 4 | — | 4 |
| Church | 5 | 6 | 5 | 4 | — | 5 |
| Hafenmark | 4 | 4 | 5 | 3 | — | 4 |
| Varfell | 4 | 4 | 4 | 4 | — | 4 |
| Guilds | 3 | 4 | 6 | 2 | — | 5 |
| Niflhel | — | 5 | 4 | — | — | 4 |
| Revolution | — | 3 | — | — | — | 3 |
| Löwenritter | — | 3 | — | 5 | 3 | 5 |

Partial sheets: Niflhel (no Mandate, no Military). Revolution (Influence, Stability, Intel only).
Löwenritter (no Mandate, no Wealth). Guilds NPC-only: no deviation mechanic.

## Domain Action Resolution
Pool = character's relevant attribute + faction's relevant stat (if PC holds leadership).
NPC factions: Pool = faction's relevant stat.
Ob = target faction's relevant stat (1–7 scale, no division).
Seasonal cap: ±2 per stat per season at accounting. Minimum Ob: 1 (PP-285).

### Ethical Framework Modifiers
| Alignment | Ob Modifier |
|-----------|------------|
| Aligned with faction framework | −1 Ob |
| Neutral / unrelated | ±0 |
| Opposed to framework | +1 Ob |
| Church revealing Thread truth | +2 Ob |
Min Ob floor: 1 after all modifiers.

## Unique Actions
| Faction | Action | Pool | Ob | Notes |
|---------|--------|------|-----|-------|
| Crown | Royal Decree | Mandate | 2 | 1/season. Consecutive: +1 Ob per season. Cannot target absent stats. |
| Church | Excommunication | Mandate | vs target Mandate (or Ob 2 if non-leader) | Requires Mandate ≥ 3. |
| Hafenmark | Sovereign Authority Doctrine | Mandate | 4 | 1/campaign arc. Heresy Investigation risk. |
| Varfell | Private Collection | Intel | 2 | 1/season. +1 TS on use. TS 14+: triggers Spirit check. |
| Guilds | Economic Leverage | Wealth | vs target Wealth | Requires Guild Favour ≥ 5 in territory. |
| Niflhel Quiet (Intel) | Intel mode | Intel | vs target Intel | Learn 1 hidden attr (Overwhelm: 2). |
| Niflhel Quiet (Sabotage) | Sabotage mode | Intel | vs target Stability | Success: Stab −1. Fail: Intel −1. |
| Niflhel Quiet (Assassination) | Assassination mode | Intel | vs target Intel +2 | Fail: full exposure, Stab −2. |
| Revolution | Community Weaving | Influence | TT ÷ 20 (round up) | Requires practitioner TS 30+. Co-movement fires. |
| Löwenritter | Coup Counter | — | threshold | Increments at 3 conditions. Never decrements. |

## Probability Reference (verified by SIM-FAC-01/02)
| Pool | Ob | P(Success+) | P(Overwhelming) |
|------|----|------------|----------------|
| 5D (Mandate) | 2 | 60% | 23% |
| 6D | 3 | 48% | 8% |
| 4D | 4 | 14% | 0% |
| 5D | 4 | 23% | 0% |
| 5D | 6 | 4% | 0% |

NPC-only equal-stat contest: ~14% success, ~59% partial, ~27% fail (design intent: PC agency matters).

## Stability Check — Seasonal Accounting
| Situation | Ob |
|-----------|-----|
| Quiet season | 1 |
| One active threat | 2 |
| Two concurrent threats | 3 |
| Active attack on Mandate/Wealth | 4 |
| Campaign-level crisis | 5 |
Anti-death-spiral floor: Stability ≤ 2 → treat as Ob 4 regardless of actual pressure.
P(survive, Stab 2 vs Ob 4) ≈ 59%. ~2 seasons at Stab 2 before probable collapse.

## Parliamentary Vote
Pool: relevant faction stat (typically Mandate or Influence).
Ob: opponent's relevant stat.
Format: best of 3 exchanges. First to 2 wins. Ties (neither wins 2): motion fails, TT+1, TC+1.

## Theocracy Counter Generation
Church Mandate ≥ 5: TC +1/season at accounting.
Piety Domain Action (1/season): Mandate pool, Ob 2. Success: TC +1 (stacks with above).
TC seasonal cap: ±5 combined from all sources.
Stability ≤ 4: TC generation pauses.

## Coup Counter (Löwenritter)
Increments (+1) when:
  - TC reaches 40 and Crown took no TC-reduction action that season
  - Torben loyalty ≤ 2 (Altonian alignment)
  - Crown loses 2+ territories in one season without a military DA response
Counter never decrements. At 3: coup fires at next accounting.

## Southernmost Awareness (Faction Stat, 0–7 or 0–10 for research factions)
| Faction | Starting Awareness |
|---------|--------------------|
| Crown | 0 |
| Church | 0 |
| Hafenmark | 1 |
| Varfell | 2 |
| Revolution | 3 |
[NAME-PENDING: ED-048] Text holder: floor = 1.

<!-- patch_history: references/params_factions_history.md (to be created) -->
<!-- canonical_sources: references/canonical_sources.yaml -->
