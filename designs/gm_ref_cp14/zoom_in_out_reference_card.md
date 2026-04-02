# ZOOM IN / ZOOM OUT — GM REFERENCE CARD
## Version: 1.0 | Source: PP-103, state_transfer_spec.md, mass_battle_v3.md §B.2/B.5
## Purpose: Single-page reference. Eliminates mid-session multi-document lookup.
## Replaces: state_transfer_spec.md §1 (for table use) — spec remains authoritative for edge cases.

---

## SIDE A — ZOOM IN PROCEDURE (BG → TTRPG)

### Step 1 — Trigger check
Named Player Character present in BG battle territory? → Zoom In fires.

### Step 2 — Phase-Lock (wait for legal entry point)

| When trigger occurs | Wait until |
|---------------------|-----------|
| During Phase 2, 4, or 5 | End of that phase — then Zoom In |
| During Phase 1 or 3 | Fire immediately after phase completes |
| During Phase 6 Step 1 | Wait until ALL damage applied (Step 1 complete) |
| During Accounting | Accounting completes first |

### Step 3 — Freeze BG state

Write down current phase. Mark suspended:

- ☐ All other faction turns (hold)
- ☐ Domain Actions (hold)
- ☐ Seasonal Accounting (hold — does NOT fire mid-scene)
- ☐ Co-Movement card draws (hold)
- ☐ TC threshold check (hold — fires at next Accounting after scene)

### Step 4 — Transfer variables

| BG Variable | → TTRPG | How |
|-------------|---------|-----|
| RS | RS | 1:1 direct |
| Unit Cohesion | Unit Cohesion | 1:1 direct |
| Unit Morale | Unit Morale | 1:1 direct (see Side B for starting values) |
| Current BG phase | — | Suspend note only |
| Territory | — | Narrative context only |
| Faction stats (M/I/W/Mil/Sta) | — | Queue to Accounting; do not transfer |
| TC, IP, PI clocks | — | Queue; do not transfer |
| Commander present? | NPC stat block | Load from NPC roster |

### Step 5 — Convert units (use Side B)

### Step 6 — Run TTRPG scene

### Step 7 — Zoom Out (TTRPG → BG)

| TTRPG outcome | BG update | When |
|---------------|-----------|------|
| Unit Strength changed | Update BG unit Health: Str × 1.5 round up | Immediate |
| Named NPC killed | Remove from board; CR = 0 for that force | Immediate |
| Wounds on PC/general | No BG stat change (personal only) | — |
| Thread op RS consequence | Update RS track | Immediate |
| Fortification damaged | Apply −N to fortification | Immediate |
| Domain Action in scene | Queue as Domain Echo | Fires at next Accounting |
| All other stat changes | Queue as Domain Echo | Fires at next Accounting |

Resume BG from held phase. All suspended factions resume. Co-Movement draws resolve.

---

## SIDE B — UNIT CONVERSION TABLE (BG token → TTRPG stats)

| BG Unit | TTRPG CP | TTRPG Str* | TTRPG Morale* | Weapon | Armour |
|---------|----------|------------|---------------|--------|--------|
| Levy | 1 | 5 | 2 | LightCut | None |
| Light Infantry | 3 | 6 | 4 | LightCut | Light |
| Heavy Infantry | 4 | 7 | 5 | HeavyCut | Medium |
| Cavalry | 5 | 6 | 5 | HeavyCut | Heavy |
| Ranged | 3 | 6 | 3 | Projectile | Light |
| Artillery | 2 | 6 | 3 | HeavyBlunt | None |
| Knights Templar | 5 | 8 | 6 | HeavyBlunt | Heavy |

*Provisional — ED-057 resolved by Phase-Lock; Morale values pending editorial confirmation.

**Starting Cohesion:** = BG unit Cohesion column in §B.2 (1:1 transfer).

**Which units are present:** Faction Military stat sets max CP deployable.
Military ≥ unit CP required. Military 1 → Levy only. Military 3 → up to Light Infantry / Ranged. Etc.

---

## QUICK REFERENCE — LOAD REDUCTION VS PRIOR PROCEDURE

| Old procedure | New procedure |
|---------------|--------------|
| 4 documents open simultaneously | This card only |
| Interruption protocol: 4-row table, partial-state tracking | Phase-Lock: 3 entry points, no partial state |
| No Str/Morale values in B.2 | Pre-calculated on Side B |
| Ghost-unit risk at Phase 2/4/5 | Eliminated — Phase 6 Step 1 entry point |
| Estimated novice time: 12 min | Estimated novice time: ~4 min |

---

*Edge cases and full variable list: state_transfer_spec.md. This card handles ~95% of table use.*
