# VALORIA STATE TRANSFER SPECIFICATION
## Source: compilation/v0.14/stage11_scale_transitions.md §11.1–11.3, §11.8
## Purpose: Defines every variable that crosses mode/scale boundaries, with direction and transformation
## Used by: valoria-simulator Mode K2 (transition stress test)
## Last updated: 2026-04-02

---

## MODE BOUNDARIES

Three boundary types exist:
1. **TTRPG ↔ Hybrid** — personal-scale rules engaging with strategic-scale rules
2. **BG ↔ Hybrid** — board game strategic rules engaging with personal-scale narrative
3. **Within-TTRPG Register Shift** — personal ↔ faction ↔ mass combat within the same mode

---

## 1. TTRPG → HYBRID (Zoom In: BG battle → TTRPG personal scene)

Triggered when a named PC enters a BG-resolved battle or territory.

### Variables that TRANSFER (BG → TTRPG)

| BG Variable | TTRPG Equivalent | Transformation |
|-------------|-----------------|----------------|
| Unit Strength (0–10) | Unit Str in TTRPG mass combat | 1:1 (same scale) |
| Unit Cohesion (1–7) | Unit Cohesion | 1:1 |
| Unit Morale (1–7) | Unit Morale | 1:1 |
| Unit Martial | Unit CP | 1:1 |
| Faction Military stat | Informs available units; not a TTRPG stat | Read-only reference |
| Territory control | Context (zone descriptions, defender positions) | Narrative only |
| Current BG turn phase | Sets constraint: Zoom In suspends BG turn at current phase | Phase held, not resolved |
| Commander (NPC general) present? | NPC stat block required | Load from stage13 |

### Variables that SUSPEND during Zoom In

| Variable | Suspension rule |
|----------|----------------|
| BG Domain Actions | Pause. Resume at Zoom Out. |
| BG Seasonal Accounting | Does not fire during TTRPG scene. |
| BG Co-Movement card draws | Suspend. Draw on resume. |
| Other faction turns (BG) | All other factions hold. Simultaneous resolution resumes at Zoom Out. |

### Variables that DO NOT transfer (remain in BG layer)

- Faction Stability, Wealth, Influence, Mandate (strategic stats — TTRPG personal scene cannot directly alter these; changes queue as Domain Echoes)
- TC, IP clocks (same — queue, fire at Accounting)
- Co-Movement deck state

### Zoom Out: TTRPG → BG state update

After TTRPG scene resolves:

| TTRPG Outcome | BG State Update |
|---------------|----------------|
| Unit Strength lost (TTRPG combat) | BG unit Strength updated 1:1 |
| Named NPC killed | BG general/commander removed; CR = 0 for that force |
| PC Domain Action in scene | Queue as Domain Echo; fires at next Accounting |
| Wounds taken by PC general | BG commander bonus unaffected (wounds are personal) |
| Thread operation RS consequence | RS track updated immediately (not queued) |
| Fortification damaged (siege scene) | Fortification −N applied immediately |

### Interruption protocol (Zoom In fires mid-BG-turn)

| BG phase at interruption | Protocol |
|--------------------------|----------|
| Planning (order selection) | Orders already placed hold. Zoom In resolves. Orders execute on resume. |
| Placement (unit positioning) | Partial placement holds. Zoom In resolves. Placement completes on resume. |
| Resolution (rolls in progress) | Current roll completes. Zoom In fires after. Resume from next roll. |
| Accounting | Accounting completes first. Zoom In fires after. |

---

## 2. HYBRID → TTRPG (Register Shift: strategic → personal)

Triggered within TTRPG mode when a faction-level event demands personal-scale resolution, or when a personal scene escalates to faction scope.

### Personal → Faction (Domain Echo direction)

| Personal Variable | Faction Effect | Transformation |
|------------------|---------------|----------------|
| Successful Domain Action roll | Faction stat change (±1–2 per degree) | Apply at Accounting unless immediate |
| Composure damage (Rattled/Unmask in social scene) | Impression Track update | Immediate |
| NPC Knot change | Faction's relationship network update | Immediate if faction-affecting |
| Combat death of faction leader | Faction Military −1; leadership question triggered | Immediate |
| Thread operation (Territorial+) | RS/TT update | Immediate |

### Faction → Personal (Domain Echo reverse: faction event forces personal scene)

| Faction Event | Personal Consequence | Trigger |
|---------------|---------------------|---------|
| Faction Stability = 0 | GM may trigger NPC crisis scenes | Immediate |
| Clock threshold crossed | Named NPCs respond (GM calls scenes) | At Accounting |
| Hostile Domain Action targeting PC | Scene forced (interrogation, arrest, confrontation) | Strategic Phase end |
| Mandate ≥ 6 (any faction) | Faction leader NPCs make major decisions | At Accounting |

---

## 3. WITHIN-TTRPG REGISTER SHIFTS

### Personal → Mass Combat (Zoom In to battle)

| Personal State | Mass Combat | Notes |
|---------------|------------|-------|
| PC attributes | PC serves as general (CR calculated) | CR = ⌈(Presence+Cognition)÷2⌉ |
| PC wounds | +1 Ob to CR checks per wound | Carries in |
| PC Thread contact | Can perform Thread operations in battle (Phase 5) | Carries in |
| PC Stamina | Not tracked during mass combat | Suspended |
| PC individual actions | Priority 8: one personal action per battle turn | Rate-limited |

### Mass Combat → Personal (Zoom In to duel within battle)

| Mass Combat State | Personal Scene | Notes |
|------------------|---------------|-------|
| Battle continues | 1 exchange per battle turn at Priority 8 | Time-compressed |
| Unit states | Frozen during duel exchange | Resume after Priority 8 |
| Commander's CR contribution | Suspended while in personal combat | Cannot also issue orders |
| Routed units | Hold position during Priority 8 | Resume drift at turn end |

### Mass Combat → Zoom Out (personal ends, return to battle)

| Personal Outcome | Mass Combat Update |
|-----------------|-------------------|
| PC kills opponent general | Battle CR = 0; all units uncommanded |
| PC takes wounds | CR checks +1 Ob per wound going forward |
| PC dies | Battle loses commander; CR = 0 |
| Scene produces no combat outcome | No mass combat state change |

---

## 4. BG → BG (within board game: intra-turn transitions)

### TC 80 Seizure (Church territorial event)

Trigger: Church TC reaches 80.
| State before | Protocol | State after |
|-------------|----------|------------|
| All faction turns in progress | Seizure interrupts at Accounting | All territory rolls resolve before remaining orders |
| Territory control | Per-territory roll (ED-032 pending: declared target or sweep) | Per result |
| BG turn order | Resume from where Accounting was interrupted | Normal |

---

## 5. UNRESOLVED TRANSITION P1 ITEMS (require fixing before K2 tests are valid)

| ID | Issue | Location | Status |
|----|-------|----------|--------|
| T1-P1-01 | Thread→Mass timing: Priority 1 (stage11) vs Phase 5 (mass_battle_v3) | stage11 §11.3 vs mass_battle_v3 §A.7 | UNRESOLVED — [EDITORIAL: requires decision; see options A/B/C below] |
| T5-P1-01 | TT Multiplier column in stage11 table is obsolete | stage11 §11.1 | NEEDS PATCH |

**T1-P1-01 RESOLVED (2026-04-02):** Option D applied per user decision. Offensive Thread (Dissolution, Pulling, Locking) fires Phase 4 between Manoeuvre and Engagement. Support Thread (Weaving, Mending) fires Phase 6 Cascade step 4–5. All damage from Volley, Thread, and Engagement applies simultaneously at Phase 6 Step 1.

---

## 6. INVARIANTS (variables that never cross any boundary)

These are always mode-specific and do not transfer:

| Variable | Mode | Why not transferred |
|---------|------|---------------------|
| BG Hand of cards | BG only | Not represented in TTRPG |
| TTRPG Inspiration tracks | TTRPG only | Too granular for BG |
| BG Victory Points (if any) | BG only | No TTRPG equivalent |
| TTRPG Belief text | TTRPG only | Narrative, not strategic |
| TTRPG Knot registry | TTRPG only | No BG equivalent |
| BG Co-Movement deck state | BG/Hybrid strategic only | Not used in personal scenes |
