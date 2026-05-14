# Module 07 Report — Military granularity at settlement scope

**Date:** 2026-05-13
**Session:** Mode G Module 7 of `settlement_mgmt_stress_01`
**Module file:** `tests/sim/settlement_mgmt_stress_01/module_07_military.py`

**Canonical sources read at full depth:**
- `designs/territory/settlement_layer_v30.md` §5.1, §5.2
- `designs/territory/settlement_adjacency_v30.md` §2 (Mass Battle at Settlement Scale), §3 (Invasion Sequencing)

## Summary

Module 7 wires military mechanics at settlement scope. Strictly **bottom-up granular emergent** in keeping with the M6 architectural commitment:

- Every military mechanic is a **pure function** on settlement state (predicates + transforms). No "battle manager" object owns the loop.
- Composition with M6 events emerges from the per-season sweep: an M6 raid-predicate fires when conditions match, M7 supplies the resolution; a Siege initiated by M7 ticks Order down across seasons, eventually triggering M6's revolt-predicate without any direct link.
- M7's `is_auto_capture` and M6's `predicate_raid_or_siege` evaluate the same canonical condition (Defense=0 + hostile adjacent) from different mechanical angles — they compose naturally without explicit coupling.

## Isolation tests — 41/41 PASS

Highlights:
- T10: Fortress chokepoint canonical worked example — Defense 4 requires Military 7+ to bypass (= margin 3)
- T21–T27: Assault outcomes cover the full spectrum: captured, repelled, auto-capture (Defense 0 + ungarrisoned), Order/Prosperity decrements per §2.3, Cathedral Casus Belli, Mine prosperity capture
- T28–T29: Siege ticks Order down by 1/season, surrenders at Order=0 — multi-season state machine
- T30–T32: Bypass supply-strike (bypassed garrison's per-season attack on invader supply line)
- T40: M6 + M7 composition — undefended Defense-0 settlement fires both M6 raid-predicate AND M7 auto-capture (the two systems independently confirm the same canonical condition)
- **T41: emergent Siege → Revolt chain.** A siege at Order=3 ticks for 3 seasons (3→2→1→0). The third tick brings Order to 0, at which point M6's `predicate_local_revolt(stats)` fires. **No code anywhere links Siege to Revolt — the chain emerges from siege effect mutating state into the revolt predicate's match condition.** This is the structural proof Jordan's emergent-architecture directive requires.

## Findings NEW this session

### F14 — Stale pre-PP-726 settlement IDs in design-doc examples

§5.1 and adjacency §3 examples reference settlement IDs that don't match the post-PP-726 canonical registry:

**§5.1:** *"Lowenskyst Fortress (S-006, Defense 4) requires Military 7+ to bypass — effectively impossible for most armies."*
- S-006 in canonical registry is **Goldenfurt** (Town, Kronmark), NOT a Fortress named Lowenskyst.

**adjacency §3:** *"Hafenmark army at S-015 Gransol Parliament wishes to invade T2 Kronmark. Gransol is adjacent (via road edge) to S-012 Kronburg Seat. ... It cannot leap to S-014 Kronmark Cathedral..."*
- S-015 is **Nordhain** (Village, Ehrenfeld province), not Gransol Parliament. Gransol is **S-018** (City, Gransol province).
- S-012 is **Stillhelm** (Town), not Kronburg Seat. The Valorsmark Seat is **S-002** Valorsplatz.
- S-014 is **Ehrenfeld** (Fortress-City), not Kronmark Cathedral. Kronmark is S-004 (Town, no Cathedral district).

These are pre-PP-726 example IDs left in design docs after the §2.1 registry rebuild. **The mechanical content remains canonically valid** (Bypass margin = 2; Fortress margin = 3; Lowenskyst's Defense 4 → required Military 7 worked example is correct arithmetic). Only the S-IDs and settlement-name examples are stale.

**This is the sixth distinct surfacing of the type-taxonomy / S-ID drift family** (F1, F7, F10, F11, F12, F14). The drift has now appeared in 6 different design-doc sections.

### F15 — adjacency §2.2 settlement-type modifier table omits 'City'

§2.2's defender-modifier table lists 6 of §1.2's 8 canonical types (Fortress / Seat / Port / Cathedral / Mine / Town / Outpost), and the "Town / Outpost" row reads "No modifier". The §1.2 type **City** has no row in §2.2.

Module 7 provisionally treats City the same as Town/Outpost (zero modifier). This may be intentional but the omission is structurally suspicious given City is a §1.2 canonical type and gets distinct treatment in §1.4.1 (capacity matrix) and §3.2 (Lieutenant-tier governor eligibility).

Editorial decision needed: confirm City is intentionally "no modifier" in §2.2, or add the canonically-intended modifier.

## Findings from prior sessions revisited

- F1–F13: unchanged (F3 resolved, F4 partial; F1/F7/F10/F11/F12/F14 form the type-taxonomy drift family).
- F8, F9: informational, unchanged.

**Cumulative finding count: 15** (F3 resolved, F4 partial; 13 open).

## Module 7 data model (downstream contract)

```
MilitaryAction (enum)                  # Assault, Siege, Bypass

# Action-eligibility predicates (pure)
can_assault(attacker_military, eff_def) -> bool
can_siege(attacker_military, eff_def) -> bool
can_bypass(attacker_military, eff_def, settlement_type) -> bool
BYPASS_MIN_MILITARY_MARGIN = 2
FORTRESS_BYPASS_MIN_MARGIN = 3

# Garrison state
@dataclass Garrison
has_garrison(garrison) -> bool
effective_defense(stats, garrison) -> int
is_auto_capture(stats, garrison) -> bool
MAX_GARRISONS_PER_SETTLEMENT = 1

# Terrain modifiers (pure)
@dataclass TerrainModifier
TERRAIN_MODIFIER_BY_EDGE_TYPE       # road/river/mountain_pass/coastal/sea/thread_witnessed
terrain_modifier(edge_type) -> TerrainModifier

# Settlement-type modifiers (pure)
@dataclass SettlementTypeModifier
SETTLEMENT_TYPE_MODIFIER_BY_TYPE    # 8 §1.2 canonical types (City provisional per F15)

# Resolution handlers (mutate state)
@dataclass AssaultResult
resolve_assault(settlement, stats, garrison, attacker_military, edge_traversed, attacker_roll)
   -> AssaultResult

@dataclass SiegeState
resolve_siege_tick(siege, stats) -> (ActionResult, surrender_flag)
SIEGE_ORDER_DECREMENT_PER_SEASON = 1
SIEGE_SURRENDER_ORDER_THRESHOLD = 0

@dataclass BypassState
resolve_bypass_supply_strike(bypass, bypassed_garrison_military, roll) -> ActionResult
BYPASS_SUPPLY_STRIKE_OB = 1
BYPASS_SUPPLY_STRIKE_DISCIPLINE_PENALTY = 1

# Post-Seat-capture resistance check (per §5.1)
settlement_resists_post_seat_capture(stats) -> bool
POST_SEAT_CAPTURE_RESIST_ORDER_THRESHOLD = 3

# Fortress mobilization (per §4.3 + §5.1 + §5.2)
fortress_mobilize_check(stats, garrison, defense_pool_roll) -> bool
FORTRESS_MOBILIZE_HOLD_OB = 2

# Invasion sequencing (per adjacency §3)
can_jump_to_settlement(invader_pos, target) -> bool

# Maintenance action
reinforce_garrison(garrison, settlement, new_unit_id, new_discipline) -> ActionResult
```

## Player-action loop contribution

Cumulative action-handler count: **27** (1 M3 + 6 M4 + 6 M5 + 9 M6 + 5 M7).

| Module | Action | Arm |
|---|---|---|
| M7 | `resolve_assault` | Problem-solve (offensive) |
| M7 | `resolve_siege_tick` | Problem-solve (offensive multi-season) |
| M7 | `resolve_bypass_supply_strike` | Problem-solve (defensive — bypassed garrison fights back) |
| M7 | `reinforce_garrison` | **Maintenance** (install garrison) |
| M7 | `fortress_mobilize_check` | Problem-solve (M6 predicate resolution) |

### Maintenance arm now broader

M5 supplied 4 maintenance actions (Develop / Fortify / Pacify / Administer — stat-level). M7 adds **garrison reinforcement** which mutates the Garrison object directly without rolling. This expands the maintenance arm to include settlement-level military preparation as a distinct action surface.

## Emergent dynamics now end-to-end

Three full chains compose through M6 and M7 without authored links:

### Chain 1 — Defense erosion → Raid event → Auto-capture
```
Season N:   Player neglects Defense (low Develop priority).
            stats.defense = 1 after several seasons of decay.
Season N+M: Defense hits 0. M6 predicate_raid_or_siege evaluates True
            (Defense=0 AND adjacent_hostile=True). FiredEvent surfaces in
            Scene Slate.
Season N+M+1: M7 auto-capture predicate also evaluates True
            (Defense=0 AND no garrison). resolve_assault returns
            settlement_captured=True without rolling.
```

### Chain 2 — Siege → Order erosion → Revolt
```
Season 0: Hafenmark army arrives at Crown settlement (Defense 3).
          Hafenmark Military 6: can_siege == True, can_bypass == True (margin 4)
          (or 3 if it's a Fortress, etc). Player choice.
Season 1: Siege begun. resolve_siege_tick applies Order -1 (3 → 2).
Season 2: tick (2 → 1).
Season 3: tick (1 → 0). siege.surrender flag True.
          ALSO: M6 predicate_local_revolt evaluates True (Order=0).
          M6 resolve_local_revolt fires concurrently with M7 surrender.
          Both M6 and M7 surface independently; Scene Slate handles which
          narrative beat the player sees first.
```

### Chain 3 — Cathedral assault → Casus Belli → political cost emerges
```
Crown player decides to assault S-003 Cathedral (Church-controlled).
M7 resolve_assault returns AssaultResult.casus_belli_imposed = True.
Module 12 will consume this signal and apply faction-level political costs
(Church PT increase + Crown standing damage). Module 7 produces the
canonical signal; Module 12 wires the political cascade.
```

## Ledger entries this session

Approximately 25 new entries. Coverage:

- 3 action-margin constants (Assault, Siege, Bypass standard 2)
- 1 Fortress bypass margin (3)
- 2 Siege tick constants (decrement 1, surrender threshold 0)
- 2 Bypass supply-strike constants (Ob 1, Discipline penalty 1)
- 1 Post-Seat resist threshold (3)
- 1 Max garrisons per settlement (1)
- 4 Terrain dice deltas (river -1, mountain_pass -1, road 0, coastal 0)
- 1 Coastal fort-bonus loss flag
- 6 Settlement-type modifier values (Seat Discipline +1, plus 5 binary flags)
- 1 Fortress mobilize hold Ob (2)
- 1 Lowenskyst worked example: Defense 4 + margin 3 = Military 7 required

## Next session — Module 8 (player progression: Stature ladder)

Force-full read: settlement_layer_v30 §6.1, §6.2, §6.3 (Stature Ladder, Faction Emergence Local→National, Faction Collapse National→Local). Module 8 will:
- Encode the Standing 0–7 ladder canonical per §6.1
- Bind the provisional `renown_delta` signals from M3/M4/M5/M6/M7 to canonical scalars (Module 8 takes ownership of the renown tracking)
- Define faction emergence stages (the recruitment-pool threshold from M6 §4.5 wires here)
- Faction collapse trigger predicates

**6 modules remaining** before Module 13 integration runner.
