# VALORIA — v18 Integration Handoff

## Status: HANDOFF — authored 2026-05-17

## Session summary

This chat executed Pass 3 verdict on the v18 integration audit, then implemented Phases 1-2 of the 12-phase integration plan.

### Commits this session (4)

| # | Commit | Scope |
|---|---|---|
| 1 | `760f2d61` | Pass 3 verdict: APPROVE-WITH-FOLLOW-UP (3 issues found) |
| 2 | `9d25fcfb` | Pass 3 follow-up: 3 fixes (CSR L211 strike, hafenmark_equipment stub, companion index entry) |
| 3 | `6b8daa2d` | Phase 1: 6 autoload modules (dice_engine, game_state, victory, season_manager, registry, scene_slate) + mc_v18 orchestrator |
| 4 | `4e81887b` | Phase 2: faction_action (conquest/muster/govern), adjacency map, accounting (CI gen + MS decay), mc_v18 wired |

### Current sim state

v18 runs end-to-end campaigns. 200-campaign batch (seed 0-199):
- Crown 75.5%, Varfell 17%, Church 6%, Hafenmark 1.5%
- 3.0 battles/campaign mean
- Factions can be eliminated (0 territories)
- Victory by 11/15 threshold or fallback by territory count at season 50

Crown dominance is expected — 6 starting territories, highest L/I. Faction-unique actions (Crown Initiative, Excommunication) and mass battle will diversify.

### What's implemented

| Module | Path | Status |
|---|---|---|
| dice_engine | sim/autoload/dice_engine.py | d10 pool + continuous Normal engine + degrees |
| game_state | sim/autoload/game_state.py | World/Faction/Territory + serialize/restore |
| victory | sim/autoload/victory.py | GD-1 peninsular_sovereignty (11/15, Accord≥2, PS≤6, 2-season sustain) |
| season_manager | sim/autoload/season_manager.py | Season/arc advance, seasonal resets |
| registry | sim/autoload/registry.py | mechanics_index.yaml loader |
| scene_slate | sim/autoload/scene_slate.py | Scene queue with priority |
| faction_action | sim/provincial/faction_action.py | Conquest/Muster/Govern (30/35/20/15 mix) |
| adjacency | sim/territory/adjacency.py | 16-territory map from m1 |
| accounting | sim/peninsular/accounting.py | CI generation + MS decay |
| mc_v18 | sim/mc_v18.py | Campaign orchestrator (~100 lines) |

### What's NOT implemented (Phases 3-12)

| Phase | Scope | Blocked? | Priority for win-share impact |
|---|---|---|---|
| 3 | Thread layer (7 ops, coherence, co-movement) | opposing.py BLOCKED on TIER-DRIFT-001 | Low — personal-scale, no strategic impact |
| 4 | Cross-scale (handoff rules, zoom, domain echo, articulation) | No | Low — routing infrastructure |
| 5 | Fieldwork/Tribunal/Parliamentary + faction-unique actions | No | **HIGH** — Crown Initiative, Excommunication, Parliamentary Vote diversify outcomes |
| 6 | Knots + Thread integration | BLOCKED on TIER-DRIFT-001 | Low |
| 7 | Mass battle (v22-rich port, 10-step plan) | No | **HIGH** — replaces single-roll conquest |
| 8-9 | Strategic integration (full faction AI, GD-2 mandatory actions) | No | **HIGH** — proper action selection |
| 10-11 | World layer (insurgency pipeline, RM, miraculous events) | No | Medium — GD-3 emergent factions |
| 12 | v17-v18 parity check | Depends on 1-11 | Final validation |

### Recommended next session priorities

1. **Phase 5 faction-unique actions** — Crown Initiative (3 modes), Excommunication, Absolution, Council of Solmund. These are the v17 M6 actions that differentiate factions. Highest impact on win distribution.
2. **Phase 7 mass battle** — Replace single-roll conquest with v22-rich multi-unit resolution. Per `mass_battle_integration_v30.md` 10-step plan.
3. **Phase 8-9 strategic AI** — GD-2 mandatory-before-stochastic action selection. Proper threat response.

### Known issues / watch items

- **Crown 75% dominance** is an artifact of missing faction-unique actions (Church has no Excommunication, Crown has no CI costs). Will resolve with Phase 5.
- **Victory sustain check** uses Turmoil clock for Political Stability — may need remapping when peninsular strain module lands.
- **Muster action** currently boosts Mil stat directly instead of minting unit tokens (v17 M4 UnitRoster not ported). Acceptable for Phase 2; Phase 7 mass battle will need proper unit state.
- **No GD-2 mandatory actions** — current action selection is purely stochastic. Phase 8 adds the mandatory-first pass.
- **Accounting is simplified** — no settlement events, no M5 governance aggregation. Phase 7+ will add.
- **npc_ai.py** autoload module not implemented (BLOCKED on contamination audit per NPC-AI-PRIORITY-STACK-001).

### Architecture notes for next implementer

- v18 modules import each other via `from sim.<subpackage>.<module> import ...`. Test locally by creating the full `sim/` package tree with `__init__.py` files.
- Strategic-scale rolls use d6≥4 (v17 convention in `faction_action._successes`), NOT the d10 dice engine. The d10 engine is for personal-scale resolution (combat, contest, fieldwork). This is intentional — the strategic sim doesn't resolve individual dice pools.
- `victory.py` maintains module-level `_qualifying_streak` dict. Call `victory.reset()` before each campaign.
- `scene_slate.py` maintains module-level `_queue`. Call `scene_slate.clear()` before each campaign.

### Compliance notes

- 2 auto-fixable compliance violations pending: `canon/editorial_ledger.yaml` needs archiving (size exceeded threshold). Not blocking.
- 3 stale canonical sources flagged by freshness gate. Not blocking.
