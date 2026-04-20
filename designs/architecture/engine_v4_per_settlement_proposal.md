<!-- SKELETON — mechanical spec only -->
<!-- Status: PROPOSAL (Jordan editorial permission, 2026-04-20) -->
<!-- Source: post-ED-722 simulation gap (engine_v3 models per-territory aggregate; ED-722 specifies per-settlement infrastructure) -->

# Engine v4 — Per-Settlement Architecture Proposal

**Date:** 2026-04-20
**Status:** PROPOSAL (editorial — Jordan permission)
**Author:** Session refresh-state
**Replaces target:** `tests/sim_framework/engine_v3.py`

---

## §1 — Motivation

Engine v3 models territories as aggregates. ED-722 (dynamic SW) and `settlement_layer_v30` Part 1 (per-settlement governance, religious building axis, building tier, Order, Wing slots) presuppose a per-settlement model. The v3 workaround (`Territory.sw` as mutable aggregate + `sack_religious_building` helper) is sufficient for stress tests but cannot represent:

- Independent settlement governors (Bishop-Governor mechanic, PP-666)
- Subnational faction management (Guild-managed Port, Church-managed Cathedral within Crown territory)
- Per-settlement Order tracks driving black-market emergence (`settlement_layer_v30 §4.7`)
- Settlement-level Religious Building tier independent of territory aggregate
- Per-settlement Wing slots (Cardinals, Prelates, Magnates)
- Adjacency-based invasion sequencing (`settlement_adjacency_v30`)

Engine v3 simulations of these are necessarily approximate. Engine v4 makes the data model match the design model.

---

## §2 — Data Model Changes

### §2.1 Settlement (NEW first-class entity)

```python
@dataclass
class Settlement:
    id: str                    # e.g., 'S-023'
    name: str                  # 'Himmelenger Cathedral'
    territory_id: str          # 'T9'
    settlement_type: str       # 'Seat' | 'City' | 'Town' | 'Fortress' | 'Cathedral' | 'Mine' | 'Outpost' | 'Port'
    controller: str            # province controller OR sub-faction (Church, Guild, RM-covert, etc.)
    prosperity: int            # 0–5
    defense: int               # 0–5
    order: int                 # 0–5
    population_tier: int       # 0–5

    # Religious Building Axis 1 (settlement_layer_v30 §1.5)
    religious_building: str    # 'None' | 'Chapel' | 'Church' | 'Cathedral'

    @property
    def religious_building_tier(self) -> int:
        return {'None': 0, 'Chapel': 1, 'Church': 2, 'Cathedral': 3}[self.religious_building]

    # Axes 2-4 (per-settlement, NOT per-territory anymore)
    templar_station: bool      # Axis 2: +1 CI/season in territory if Church Prominent
    inquisitor_base: bool      # Axis 3: surveillance; RM Ob +1
    church_governor: bool      # Axis 4: settlement governance uses Church stats

    # Wing slots (per settlement_type)
    wings: List[str] = field(default_factory=list)  # e.g., ['Cardinal of Temperance']

    # Black market / intelligence broker / Thread exploitation (settlement_layer_v30 §4.7-4.9)
    has_black_market: bool = False           # auto-emerges when order ≤ 1 OR no governor
    intelligence_broker: Optional[str] = None  # NPC name if present
    thread_exploitation_site: bool = False   # auto if Thread Proximity ≤ 2
```

### §2.2 Territory (REVISED — derived properties)

```python
@dataclass
class Territory:
    id: str
    name: str
    pv: int
    pr: int                    # Thread Proximity (fixed)
    controller: str            # province controller
    accord: int
    pt: int
    fort: int = 0

    # Settlements in this territory (by ID; full Settlement objects in GameState.settlements)
    settlement_ids: List[str] = field(default_factory=list)

    @property
    def settlements(self) -> List[Settlement]:
        # Resolved via GameState.settlements registry
        ...

    @property
    def sw(self) -> int:
        """ED-722 dynamic SW: Σ religious_building_tier per settlement, capped 5."""
        return min(5, sum(s.religious_building_tier for s in self.settlements))

    @property
    def has_templar_presence(self) -> bool:
        """ED-722-aligned: any settlement in territory has templar_station."""
        return any(s.templar_station for s in self.settlements)

    @property
    def seat_settlement(self) -> Optional[Settlement]:
        for s in self.settlements:
            if s.settlement_type == 'Seat':
                return s
        return None
```

### §2.3 GameState (REVISED — adds settlements registry)

```python
@dataclass
class GameState:
    # ... existing fields ...
    settlements: Dict[str, Settlement] = field(default_factory=dict)
```

---

## §3 — Mechanic Implementations Affected

### §3.1 CI Generation (`generate_ci`)

**Engine v3 (current):** loops over territories, reads `t.sw`, `t.templar`.
**Engine v4:** loops over territories, reads `t.sw` (now a property aggregating settlements), `t.has_templar_presence` (any-settlement aggregator). Same formula, different data resolution.

### §3.2 Seizure (`attempt_mass_seizure`)

**Engine v3:** Ob = 10 − PT − infrastructure modifier (territory-level church_building).
**Engine v4:** per-settlement seizure. Ob = 10 − PT − Σ(settlement_seizure_modifier) where the modifier comes from `settlement_layer_v30 §1.5` table (Chapel 0, Church −1, Cathedral −2, Templar −1, Inquisitor −1, Church Governor −2, cap −4 per settlement). Mass Seizure (CI=100) declares simultaneous seizure across all territories with Church infrastructure.

### §3.3 Battle / Conquest (`attempt_conquest`)

**Engine v3:** territory-level conquest attempt.
**Engine v4:** per-settlement assault sequence (`settlement_layer_v30 §5.1` Capture sequence). Attacker chooses settlement to assault first; can siege, bypass (if Mil > Def + 2), or assault. Province transfers when Seat captured. Other settlements may resist with their own garrisons.

### §3.4 Bishop Appointment / Ecclesiastical Appointment

**Engine v3:** territory-level church_building tier increment.
**Engine v4:** Settlement-level. Church installs religious building in a chosen settlement (Chapel +1 Order; Church +1 Order one-time; Cathedral +1 Order + decay −1). Bishop-Governor (Axis 4) installation overrides settlement controller; province fractionalizes if controller ≠ Seat holder (`settlement_layer_v30 §3.6` PP-TBD).

### §3.5 Black Markets (settlement_layer_v30 §4.7)

**Engine v3:** not modeled.
**Engine v4:** at Phase 5 each season, evaluate each settlement: if `order ≤ 1` OR `controller is None`: `has_black_market = True`. Effect: settlement Wealth +0.5, Accord −0.5. If order ≥ 3: `has_black_market = False`. Provides Niflhel-dissolution-canonical mechanic.

### §3.6 Intelligence Brokers (settlement_layer_v30 §4.8)

**Engine v3:** not modeled.
**Engine v4:** at game start, each settlement with Prosperity ≥ 3 AND (no governor OR governor Stability ≤ 2) gets an `intelligence_broker` NPC. Per-NPC behavior tracked separately. Can be killed, bought, turned.

### §3.7 Thread Exploitation Sites (settlement_layer_v30 §4.9)

**Engine v3:** not modeled.
**Engine v4:** auto-derived from territory PR ≤ 2: all settlements in the territory have `thread_exploitation_site = True`. Harvesting reduces RS by 0.5 per season per harvest, +1 Wealth per harvesting faction.

---

## §4 — Implementation Strategy

### §4.1 Phased migration

| Phase | Scope | Test |
|-------|-------|------|
| v4.0 (foundational) | Add `Settlement` dataclass; populate from `settlement_layer_v30` §3 table; `Territory.sw` becomes a property aggregating settlements | B6: re-run B3/B4/B5; results should match (same aggregates) |
| v4.1 (per-settlement seizure) | Implement `attempt_mass_seizure` per-settlement; Mass Seizure simultaneous declaration | B7: Mass Seizure declaration test — confirm declaration probability + per-settlement Ob |
| v4.2 (per-settlement conquest) | Implement Capture sequence (assault / siege / bypass) per `settlement_layer_v30 §5.1` | B8: Conquest test — confirm Seat-capture provincial transfer + non-Seat resistance |
| v4.3 (Bishop appointment) | Bishop-Governor installation; province fractionalization on controller mismatch | B9: Bishop ladder test — confirm pre-Mass Seizure accumulation path |
| v4.4 (settlement-derived phenomena) | Black markets, intelligence brokers, Thread exploitation sites | B10: Niflhel-dissolution effects test |

### §4.2 Test harness changes

- `init_state` accepts `settlement_seed` param: dict of `S-### → Settlement(...)` from settlement_layer_v30 §3 table
- Backward-compatible: if no seed provided, falls back to per-territory aggregate (engine v3 behavior)

### §4.3 Backward compatibility

For sims that operate at province scale only (e.g., re-running B3/B4): `Territory.sw` property returns the same value as v3's mutable field once settlements are populated. No call-site changes required for province-scale code.

---

## §5 — Out of Scope (for v4)

- Per-settlement combat resolution at scene scale (still aggregated via `mass_battle_v30`)
- Settlement-level Discovery Events (Wing-slot interactions remain narrative-only at sim scale)
- Calamity Radiation per-settlement effects (territory PR is the granularity)
- Engine integration with valoria-game Godot project (cross-repo work)

---

## §6 — Editorial Decision Required

This proposal is editorially approved (2026-04-20, Jordan permission). Implementation may proceed in phases. The current engine_v3 + ED-722 mutator helpers are sufficient for non-architectural sim work; engine_v4 is required only for tests that specifically exercise per-settlement mechanics (B7+).

**Recommended action:** v4.0 (foundational data-model migration) is high-priority — unblocks B6 stress-test of Cathedral construction (currently impossible to model individual Cathedral builds in v3). v4.1–v4.4 can be deferred until specific stress tests require them.
