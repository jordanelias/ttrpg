<!-- version: v0.14 | sources: stage11_scale_transitions.md | last_updated: 2026-03-26 -->
<!-- STALE CHECK: If current ruleset version ≠ v0.14, halt and flag before using. -->

# params_scale_transitions.md — Scale and Mode Transitions

## Scale Table
| Scale | Example | Base Ob | Min TS | Coherence auto-cost |
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
| Personal → Faction | GM recognises faction scope. Personal Ob resolves first, Domain Action Ob second. Same roll. |
| Personal → Scene | Personal roll may serve as opening move or Appeal in a social scene. |
| Scene → Faction | Successful Appeal/Debate at sufficient scope → Domain Echo (faction attribute change). No extra roll. |
| Thread → Faction | Thread op targeting faction-level config resolves as Domain Action. Thread pool, appropriate Ob. No extra roll. |
| Thread → Mass | Combat ops: Phase 2 (before Engagement). Support ops: Phase 5 (Cascade). Both declared Phase 1. |
| Mass → Personal | Personal Action available at Phase 5 (Priority 8). Limit: 1 exchange/battle turn. General's Phase 5 consumed until personal combat resolved (CR suspended). |
| Scene → Mass | Social scene outcomes apply to mass combat opening state before next round declaration. |

## Scope Shift
Once per round, declared at turn start. No roll.
Second scope action in same round: +1 Inspiration spend.

## Mode Tags (for simulation tagging)
TTRPG / BG / HYB
Transition points requiring explicit procedure definition:
- TTRPG → BG: session boundary; faction stats carry over; personal character stats suspended
- BG → HYB: mid-game zoom-in; personal characters enter board state
- HYB → TTRPG: zoom-out; board state updated from personal scene results
[GAP: TTRPG↔BG↔HYB transition procedures not formally compiled — design intent in stage12_campaign_modes.md]
