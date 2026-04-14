<!-- DEPRECATED -->
> **DEPRECATED — 2026-04-11**
> CP14 zoom reference card. Based on outdated CP14 mechanics.
> Do not use as a canonical source.

---

# ZOOM IN / ZOOM OUT — GM REFERENCE CARD
## Version: 1.1 | Source: PP-103/PP-104, state_transfer_spec.md, mass_battle_v3.md §B.2/B.5
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

| BG Unit | TTRPG CP | TTRPG Str* | TTRPG Morale* | Weapon | Armour | Dmg Mod* |
|---------|----------|------------|---------------|--------|--------|---------|
| Levy | 1 | 3 | 2 | LightCut | None | +1 |
| Light Infantry | 3 | 4 | 4 | LightCut | Light | +2 |
| Heavy Infantry | 4 | 5 | 5 | HeavyCut | Medium | +4 |
| Cavalry | 5 | 4 | 5 | HeavyCut | Heavy | +5 |
| Ranged | 3 | 3 | 3 | LP (arrows) | Light | +2 |
| Artillery | 2 | 3 | 3 | HBl (siege) | None | +5 |
| Knights Templar | 5 | 6 | 6 | HeavyBlunt | Heavy | +5 |

*Provisional — Str corrected PP-104 (−2 all, −3 Ranged/Artillery). Morale/Dmg Mod: ED-062.

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


---

## SIDE C — ARC-SPECIFIC ZOOM IN TRIGGERS (PP-556)

**Design extension (2026-04-12):** In addition to the standard trigger (Named Player Character present in BG battle territory), the following arc-specific board-state conditions call a Zoom In. These are supplementary triggers — the Phase-Lock, Freeze, Transfer, and Zoom Out procedures on Side A apply unchanged.

Each arc document carries a **Hybrid Trigger** field specifying the exact condition. Format:

```
Hybrid Trigger: [board-state condition] → Zoom In [scene type].
BG consequence resolves at next Accounting (Domain Echo).
```

**Example — Haelgrund Defection (Arc 41, npc_roster §4):**
```
Hybrid Trigger: Thread operation Overwhelming within 1 territory of Haelgrund's
current investigation AND Church has no active Inquisitor suppression →
Zoom In: Defection Scene.
BG consequence: Church Heresy Investigation Ob +1 permanently (best investigator lost).
Resolves at Accounting.
```

**Ordering rule:** Arc-specific triggers follow the same Phase-Lock as battle triggers (Step 2, Side A). If an arc trigger fires during Phase 2, 4, or 5, wait until that phase ends. If multiple arc triggers fire simultaneously, resolve in Mandate order (descending) per PP-269.

**TC threshold note:** TC threshold checks fire at the moment of crossing regardless of any Zoom In (PP-268/PP-293 — applies to victory condition checks, not all TC checks). Arc-specific Zoom Ins may be declared after a TC threshold crossing; they do not delay the threshold consequence.
