# Valoria Clock & Track Registry
## Created: 2026-04-08 | Status: CANONICAL
## Single source of truth for all clocks, tracks, and counters.
## Cross-references to authoritative source for each track's rules.

---

## Shared Clocks (All Modes)

| Clock | Range | Start | Direction | Source |
|-------|-------|-------|-----------|--------|
| Rendering Stability (RS) | 0–100 | 72 | ↓ (decay) | params_threadwork.md §RS |
| Theocracy Counter (TC) | 0–75 (freezes at 75) | 28 | ↑ | victory_architecture_v1.md §7 |
| Invasion Pressure (IP) | 0–100 | 5 | ↑ | params_board_game.md §IP |
| Public Instability (PI) | 0–? | 0 | ↑ | params_board_game.md §PI [ED-361: thresholds pending] |

## Faction-Specific Tracks (BG/Hybrid)

| Track | Owner | Range | Start | Source |
|-------|-------|-------|-------|--------|
| Vaynard Thread Mastery (VTM) | Varfell | 0–5 | 0 | params_board_game.md §VTM |
| Altonian Ecclesiastical Accord (AER) | Church/Hafenmark | 0–5 | 0 | victory_architecture_v1.md §AEA |
| Torben Loyalty | Crown → Löwenritter | 0–10 | 10 | params_board_game.md §Torben [ED-329: start/range disputed — 3 on 0–7 recommended] |
| Elske Loyalty | Crown | 0–7 | 4 | params_board_game.md §Elske |
| Coup Counter | Löwenritter (GM private) | 0–3 | 0 | stage6_factions.md §8.9 |
| Popular Will (PW) | Shared (Hybrid only) | 0–5 | 0 | params_board_game.md §RM Founding |
| Warden Cooperation (WC) | Shared | 0–3 | 0 | victory_architecture_v1.md §6 |
| Warden Recognition (WR) | Varfell | 0–4 | 0 | victory_architecture_v1.md §6 |

## Faction Stats (All Factions)

| Stat | Range | Source |
|------|-------|--------|
| Mandate | 0–7 | params_factions.md §Faction Stats |
| Influence | 0–7 | params_factions.md §Faction Stats |
| Wealth | 0–7 | params_factions.md §Faction Stats |
| Military | 0–7 | params_factions.md §Faction Stats |
| Stability | 0–7 | params_factions.md §Faction Stats |

## Per-Territory Tracks (BG/Hybrid)

| Track | Range | Start | Source |
|-------|-------|-------|--------|
| Conviction (CV) | 0–5 | Varies by territory | victory_architecture_v1.md §2 |
| Fort Level | 0–4 | Per geography_design.md | geography_design.md |
| Prosperity | 0–? | Varies | params_board_game.md §Prosperity |

## Personal Tracks (TTRPG/Hybrid)

| Track | Range | Start | Source |
|-------|-------|-------|--------|
| Coherence | 0–10 | 10 | params_threadwork.md §Coherence |
| Certainty | 0–Spirit | Spirit score | params_threadwork.md §Certainty |
| Thread Sensitivity (TS) | 0–100 | Varies (0 for non-sensitives) | params_threadwork.md §TS |
| Composure | 0–varies | Poise + 6 | params_contest.md §Composure |
| Concentration | 0–varies | Focus | params_contest.md §Concentration |
| Health | 0–varies | Forte + 6 | params_core.md |
| Wounds | 0–varies | 0 (accumulates) | params_combat.md §Wounds |
| Stamina | 0–varies | Forte | params_combat.md §Stamina |

## NPC-Specific Tracks

| Track | NPC | Range | Start | Source |
|-------|-----|-------|-------|--------|
| Cardinal Influence | 3 Cardinals | 0–5 each | Varies | params_factions.md §Cardinals |
| Church Attention Pool (AP) | Church NPC AI | 0–? | 0/season | params_board_game.md §Church AP |
| Ministry AP-Tokens | Ministry NPC | per-territory | 4 tokens | params_board_game.md §Ministry |

## Cooldown/Duration Tracks

| Track | Range | Source |
|-------|-------|--------|
| Cooldown Track | per-card slots | params_board_game.md §Phase 5 |
| Thread Debt | per-token | params_board_game.md §Thread Debt |
| Casus Belli | per-faction | params_board_game.md §Casus Belli |
| Martial Law duration | until removed | stage6_factions.md §8.9 |

---

*Registry maintained by valoria-orchestrator. Update in same commit as any clock/track creation or modification.*
