<!-- version: v1.0 | source: designs/systems/campaign_modes_v30.md | last_updated: 2026-04-13 -->
<!-- SIM STATUS: PROCEDURAL — no simulation required (timing/structure values) -->

# params_campaign_modes.md — Campaign Mode Structure

## Session Timing Reference
| Measure | TTRPG | Board Game | Hybrid |
|---------|-------|-----------|--------|
| Real session (3–4 hrs) | 2–4 scenes (≤1 season) | 3–5 seasons | 1 season (all 4 phases) |
| 1 game season | 1–2 sessions | ~15–20 min | 1 session |
| Full campaign (10 seasons) | 15–25 sessions | 1 session (2–4 hrs) | 10–15 sessions |

## TTRPG Session Structure
| Phase | Duration |
|-------|---------|
| Opening | 10 min |
| Scene 1 | 60–90 min |
| Scene 2 (optional) | 45–60 min |
| Accounting | 15 min |

Season pacing: 1 season = 1–2 sessions. Quiet seasons: compress to 1 accounting beat.

## Board Game Session Structure
| Phase | Duration |
|-------|---------|
| Setup | 10–15 min |
| Season loop ×3–5 | 25–40 min each |
| Endgame check | 5 min |

## Hybrid Session Structure (4 phases, 1 season/session ≈ 2–2.5 hrs)
| Phase | Duration | Content |
|-------|---------|---------|
| Personal Phase | 60–90 min | TTRPG scenes. Max 2–3 scenes. |
| Strategic Phase | 20–30 min | BG orders placed and resolved. |
| Cascade Phase | 10–15 min | Domain Echoes, threshold events, cross-mode consequences. |
| Accounting | 5–10 min | Attribute changes, clock advances, victory checks. |

GM compression options:
  Quiet season: skip Personal Phase → ~30 min.
  Expanded season: split across 2 sessions if TTRPG scenes demand it.

## Starting Clock Values (TTRPG Session Zero)
| Clock | Start | Source |
|-------|-------|--------|
| Rendering Stability | 72 | params_core.md |
| Theocracy Counter | 15 | params_factions_ttrpg.md |
| Institutional Pressure | 20 | params_board_game.md |

## Endgame Indicators (TTRPG — emergent, not triggers)
- All PCs resolved/abandoned central Beliefs
- RS > 80 (recovering) or RS < 20 (doomed)
- Succession crisis resolved
- TC < 20 (Church broken) or TC > 80 (Church triumphant)
- Altonian threat resolved
- At least one PC has died, retired, or transformed

## Hybrid Victory Conditions
Faction achieves BG primary victory AND faction leader (PC) resolved central Belief arc in support of victory.
Hollow victory: BG condition met but PC arc contradicts it. Player choice: accept or continue.

## Coherence Track — Campaign Arc Reference
| Coherence | State | Mechanical effect |
|-----------|-------|------------------|
| 10–8 | Stable | None |
| 7–5 | Dissonant | Narrative flickers |
| 4–3 | Fragmented | −1D social/memory; +1 Ob Thread ops |
| 2 | Fractured | −2D social/memory; dissociative episodes on Thread ops |
| 1 | Severed | +2 Ob Thread ops; barely functional |
| 0 | Rendering Crisis | Player choice: withdraw, recover, or accept consequences |

## Mode Rule Branching Summary
| System | TTRPG | Board Game | Hybrid |
|--------|-------|-----------|--------|
| Personal combat | Full pool split + priority table | N/A | TTRPG during Personal Phase |
| Mass combat | Zone-based; Zoom In/Out | Disposition table, single roll | BG resolution; Zoom In for named NPCs |
| Domain Actions | GM-recognised from personal roll | Explicit Order Set | Strategic Phase BG; Personal Phase TTRPG |
| Thread ops | Full ops, Version C co-movement | Faction-scale, Co-Movement Cards | Personal: Version C; Strategic: Cards |
| Seasonal stat cap | ±2/stat/season | ±2/stat/season | Shared — applies across both phases |
| CP spending | Full menu | N/A | TTRPG during Personal Phase only |

<!-- patch_history: not required (procedural doc — no mechanical values to patch) -->
<!-- canonical_sources: references/canonical_sources.yaml -->
