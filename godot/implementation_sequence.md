# Phase 5.2 — Godot Implementation Sequence

> **⚠️ STALE / PARTIALLY SUPERSEDED (flagged 2026-06-30).** Dated 2026-04-18 — pre-`d+σ`, pre-LPS-2e.
> **Do not implement from this doc.** The governing Godot spec is
> `godot/godot_conversion_strategy_v1.md` (itself PROPOSED);
> resolve module order via `references/module_contracts.yaml`. Tracked by ED-1054.

# Date: 2026-04-18
# Build order based on interdependency (highest fan-out first)

---

## Implementation Phases

### Phase G1: Core Engine (Week 1-2)
**Dependencies:** None. Everything depends on this.

1. **Dice pool resolution** — `DiceEngine` autoload
   - d10 pool roller, TN comparison, Ob check, degree table
   - Net successes → {failure, partial, success, overwhelming}
   - Used by every system. Must be rock-solid before anything else.

2. **State management** — `GameState` autoload
   - All clocks (MS, CI, IP, PI, Strain) as tracked resources
   - Faction stats (1-7) + derived values (Treasury, Legitimacy, Reputation, Discipline)
   - Settlement registry (36 entries, P/D/O stats)
   - NPC registry (14+ entries, full stat blocks)
   - PC state (attributes, skills, Standing, Renown, Coherence, etc.)
   - Schema reference: `sim_framework/state.py` maps 1:1 to these structures

### Phase G2: Season Loop + Scene Slate (Week 3-4)
**Dependencies:** G1

3. **Season loop** — `SeasonManager` autoload
   - 4-phase sequence: Briefing → Personal Phase → Strategic Phase → Accounting
   - Phase transitions via signals
   - Seasonal clock ticks at Accounting

4. **Scene Slate generation** — `SceneSlateManager`
   - Priority 0-5 scene generation per player_agency §4.2
   - Scene selection UI (player picks from generated slate)
   - Scene resolution routing (fieldwork/combat/contest/thread/governance)

### Phase G3: Personal-Scale Systems (Week 5-8)
**Dependencies:** G1, G2

5. **Fieldwork** — `FieldworkManager`
   - 6 exploration depths, 6 investigation actions, 7 social actions
   - Evidence Track with 3 thresholds (Simple/Complex/Structural)
   - Exposure tracking with Cover-derived thresholds
   - Disposition system (−5 to +5)
   - Knot formation (§5.6a)
   - ~60% of player scene actions use this system

6. **Personal combat** — `CombatManager`
   - 11 action types with resolution order (§4, AUD-COM-01 fix)
   - Pool split (Offence/Defence allocation)
   - Wound intervals, Stamina, incapacitation stages
   - Weapon TN matrix (3-axis melee + distinct ranged)
   - Death Cascade (5-step consequences)
   - Combat Reputation tracking

7. **Social contest** — `ContestManager`
   - Exchange-based Piety Track (1-9)
   - 4 interaction types (CLASH/REINFORCE/CROSS/TIE)
   - 3 adjudicator types → different pool attributes
   - Composure, Concentration, Forfeit actions
   - Resonant Style targeting → Conviction Scar
   - Obligation generation, Chain Contest

### Phase G4: Threadwork (Week 9-10)
**Dependencies:** G1, G3 (combat for wound disruption)

8. **Threadwork** — `ThreadworkManager`
   - Leap resolution (Spirit pool, 4 degrees)
   - 5 operations (Weaving/Pulling/POP/Locking/Dissolution)
   - Mending (4 Gap severities)
   - Co-Movement card deck (18 cards, global reshuffle)
   - Coherence tracking (10→0 thresholds)
   - Rendering Crisis (4-beat arc)
   - Collective/Opposing operations
   - Unlocks for TS 30+ characters only

### Phase G5: Strategic-Scale Systems (Week 11-14)
**Dependencies:** G1, G2

9. **Mass battle** — `MassBattleManager`
   - 7-phase turn structure
   - Unit stats (Size/Power/Discipline/Morale/Command)
   - Formations, tactics, General Duel
   - Hybrid handoff (Zoom In at 3 entry points)
   - Battle consequences (MS, IP, Strain, territory, Accord)

10. **NPC AI** — `NPCAIManager`
    - Priority tree evaluation (§8.2-8.10)
    - Arc state machine (position A→D, transition triggers)
    - Conviction crisis (3+ Scars → weighted d6)
    - Framework Drift (passive stat changes)
    - Death/replacement, roster management (30-NPC cap)
    - Can run headless during development

### Phase G6: Settlement + Victory (Week 15-16)
**Dependencies:** G1, G5

11. **Settlement governance** — `SettlementManager`
    - 4 governance actions (Develop/Fortify/Pacify/Administer)
    - Settlement stat progression (0-5)
    - Church infrastructure (4 axes)
    - Order → Accord derivation (§2.5 Settlement Targeting)
    - Settlement map view (UI)

12. **Victory conditions** — `VictoryManager`
    - Universal + 4 faction-specific + 4 conditional faction conditions
    - Checked at each Accounting
    - Co-victory partition logic

### Phase G7: UI/UX (Week 17-20)
**Dependencies:** All systems functional

13. **UI/UX progressive disclosure** — capability-gated chrome
    - 14 UI states from UI/UX v4.1 §1.1
    - Derived stats display (Part 11 supplement)
    - Settlement map view (Part 3 supplement)
    - Scene Slate selection interface
    - Contest exchange UI
    - Thread visualization
    - Build last because it wraps everything

---

## Estimated Timeline

| Phase | Weeks | Cumulative |
|-------|-------|-----------|
| G1 Core | 2 | 2 |
| G2 Season Loop | 2 | 4 |
| G3 Personal | 4 | 8 |
| G4 Threadwork | 2 | 10 |
| G5 Strategic | 4 | 14 |
| G6 Settlement/Victory | 2 | 16 |
| G7 UI/UX | 4 | 20 |
| **Total** | **20 weeks** | |

## Cross-Repo Note
All implementation happens in `jordanelias/valoria-game`. Design docs remain in `jordanelias/ttrpg`. Cross-repo protocol per Phase 5.5.
