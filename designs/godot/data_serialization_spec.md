# Phase 5.3 — Data Serialization Specification
# Date: 2026-04-18
# Purpose: Define Godot resource (.tres) schemas for all game data

---

## Schema Reference
All schemas derived from `sim_framework/state.py` data structures. 1:1 mapping.

---

## faction_data.tres

```gdscript
class_name FactionData extends Resource

@export var faction_name: String
@export var mandate: int          # 1-7
@export var wealth: int           # 1-7
@export var military: int         # 1-7
@export var influence: int        # 1-7
@export var stability: int        # 1-7
@export var territories: Array[String]  # ["T1", "T2", ...]
@export var active: bool = true
@export var ethical_framework: String   # "virtue_ethics", "divine_command", etc.
# Derived values computed at runtime from stats — not serialized
```

**Instances:** 8 (Crown, Church, Hafenmark, Varfell, Löwenritter, RM, Altonian, Wardens)

---

## settlement_data.tres

```gdscript
class_name SettlementData extends Resource

@export var settlement_name: String
@export var territory: String          # "T1"
@export var type: String               # "Seat", "City", "Town", etc.
@export var prosperity: int            # 0-5
@export var defense: int               # 0-5
@export var order: int                 # 0-5
@export var controller: String         # faction name
@export var governor: String           # NPC name or ""
@export var church_building: bool
@export var church_templar: bool
@export var church_inquisitor: bool
@export var church_governor: bool
@export var facility_slots: Dictionary  # {"wing": 3, "suite": 5, ...}
```

**Instances:** 34 (per state.py settlement_data)

---

## npc_data.tres

```gdscript
class_name NPCData extends Resource

@export var npc_name: String
@export var faction: String
@export var primary_conviction: String
@export var secondary_conviction: String
@export var primary_rs: String          # Resonant Style
@export var secondary_rs: String
@export var ts: int                     # Thread Sensitivity 0-100
@export var certainty: int              # 0-5
@export var disposition: int            # -3 to +5 (toward PC)
@export var scar_count: int
@export var arc_position: String        # "A", "B", "C", "D"
@export var alive: bool
@export var coherence: int              # 0-10
@export var beliefs: Array[String]      # 3 beliefs
@export var ethical_framework: String
```

**Instances:** 14+ (named NPCs, expandable to 30-NPC cap)

---

## weapon_data.tres

```gdscript
class_name WeaponData extends Resource

@export var weapon_name: String
@export var category: String            # "melee" or "ranged"
# Melee 3-axis
@export var reach: String               # "short" or "long"
@export var weight: String              # "light" or "heavy"
@export var damage_type: String         # "slash", "pierce", "blunt"
@export var tn: int                     # 5-8
@export var str_minimum: int
# Ranged-specific
@export var reload_rounds: int          # 0 = no reload
# Damage modifiers vs armor
@export var dmg_vs_none: int
@export var dmg_vs_light: int
@export var dmg_vs_medium: int
@export var dmg_vs_heavy: int
```

**Instances:** ~12 (8 melee profiles + 3 ranged + unarmed)

---

## clock_data.tres

```gdscript
class_name ClockData extends Resource

@export var clock_name: String
@export var range_min: int
@export var range_max: int
@export var starting_value: int
@export var direction: String           # "ascending", "descending", "bidirectional"
@export var source_doc: String          # canonical source reference
```

**Instances:** ~25 (MS, CI, IP, PI, Strain, VTM, AER, Coup Counter, Elske Loyalty, PT×15, etc.)

---

## territory_data.tres

```gdscript
class_name TerritoryData extends Resource

@export var territory_id: String        # "T1"
@export var territory_name: String
@export var pt: int                     # Piety Track 0-5
@export var fort_level: int
@export var controller: String          # faction name
@export var accord: int                 # derived from settlement Order
@export var church_attention_pool: int
@export var settlements: Array[String]  # settlement names in this territory
```

**Instances:** 15 (T1-T14, T17; T15 Askeheim special — PT hard-fixed 0, T16 unused)

---

## Loading Protocol

1. On game start: load all .tres resources from `res://data/`
2. `GameState` autoload instantiates runtime state from loaded resources
3. Runtime state is mutable; .tres files are read-only templates
4. Save games serialize runtime `GameState` to `.save` files (not .tres)
5. `init_validator.py` equivalent runs on load: compare loaded values against design doc expectations, flag discrepancies in debug log
