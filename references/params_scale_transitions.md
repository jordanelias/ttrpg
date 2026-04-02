<!-- version: v0.14-ST2 | sources: stage11_scale_transitions.md + PP-107–112 hybrid audit patches | last_updated: 2026-04-02 -->
<!-- CANONICAL SOURCE: stage11 is canonical (no design doc for scale transitions). Updated with PP-089/090 and ED-050 Thread timing fix. -->
<!-- STALE CHECK: If current ruleset version ≠ v0.14, halt and flag before using. -->

# params_scale_transitions.md — Scale and Mode Transitions

## Scale Table
| Scale | Example | Base Ob | Min Thread Sensitivity | Coherence auto-cost |
|-------|---------|---------|--------|-------------------|
| Object | One item, one wound | 1 | 30+ | 0 |
| Personal | One person | 2 | 30+ | 0 |
| Relational | Small group, social agreement | 3 | 50+ | −1 |
| Territorial | A duchy, a district | 4 | 50+ | −1 |
| Structural | A kingdom, an institution | 5+ | 70+ | −2 |

## Eight Handoff Rules
| Transition | Rule |
|-----------|------|
| Personal → Thread | Leap triggers. Contact duration starts on round Leap succeeds. |
| Personal → Faction | Game Master recognises faction scope. Personal Ob resolves first, Domain Action Ob second. Same roll. |
| Personal → Scene | Personal roll may serve as opening move or Appeal in a social scene. |
| Scene → Faction | Successful Appeal/Debate at sufficient scope → Domain Echo (faction attribute change). No extra roll. |
| Thread → Faction | Thread op targeting faction-level config resolves as Domain Action. Thread pool, appropriate Ob. No extra roll. |
| Thread → Mass | Combat ops: Phase 2 (before Engagement). Support ops: Phase 5 (Cascade). Both declared Phase 1. |
| Mass → Personal | Personal Action available at Phase 5 (Priority 8). Limit: 1 exchange/battle turn. General's Phase 5 consumed until personal combat resolved (Coherence Rating suspended). |
| Scene → Mass | Social scene outcomes apply to mass combat opening state before next round declaration. |

## Domain Echo Rules (PP-108/PP-109)

**Amount:** Faction stat change = +1 per degree above Partial.
- Success: +1 to most relevant stat (Mandate for political, Influence for social, Military for combat)
- Overwhelming: +2
- Cap: ±2 per scene. [PROVISIONAL — ED-071]

**Timing by mode:**
- Full TTRPG (Register Shift): Domain Echo fires immediately at scene end. No extra roll.
- Hybrid (Zoom In active): Domain Echo queues; fires at next BG Seasonal Accounting.

**Intentional design (PP-109):** The timing difference is by design. Zoom In is a personal intervention in a strategic situation. Faction consequences propagate through seasonal accounting (not instantly) to prevent real-time manipulation of BG stats from personal scenes. This is documented here as an intentional mode asymmetry.

**Multiple Domain Echoes (same scene):** Fire in the order they occurred in the scene. Each applies independently; cap resets per stat per Echo (not per scene total). [PROVISIONAL — resolve ED-071]

**Debate outcome → Domain Echo:** Conviction Track ≥7 (winner) queues +1 Mandate for winner's faction. ≤3 queues −1 Mandate for loser's faction. [PP-108]

## Mass→Personal Register Shift Rules (PP-111)

One mass combat turn = one personal combat exchange. If general's duel is unresolved after one exchange, it continues into the next turn's Phase 5. The general's unit loses CR bonus (effective CR 0) each turn the general is in personal combat. Maximum 5 exchanges before forced disengage or incapacitation. General's Phase 5 consumed until combat resolved.

## Scope Shift
Once per round, declared at turn start. No roll.
Second scope action in same round: +1 Inspiration spend.

## Mode Tags (for simulation tagging)
TTRPG / BG / Hybrid
Transition points requiring explicit procedure definition:
- TTRPG → BG: session boundary; faction stats carry over; personal character stats suspended
- BG → Hybrid: mid-game zoom-in; personal characters enter board state
- Hybrid → TTRPG: zoom-out; board state updated from personal scene results
Phase-Lock Protocol (PP-103): legal Zoom In entry points are After Phase 1, After Phase 3, After Phase 6 Step 1. See state_transfer_spec.md for full variable inventory.
Phase 6 continuation: Steps 2–6 resolve after Zoom Out using updated state (PP-110).
Non-battle Zoom In: fires at end of current Domain Action being resolved (full procedure pending ED-073).
