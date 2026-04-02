# VALORIA STATE TRANSFER SPECIFICATION
## Source: compilation/v0.14/stage11_scale_transitions.md §11.1–11.3, §11.8
## Purpose: Defines every variable that crosses mode/scale boundaries, with direction and transformation
## Used by: valoria-simulator Mode K2 (transition stress test)
## Last updated: 2026-04-02 | PP-103 Phase-Lock + PP-107 variable corrections applied

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
| Unit Strength (0–10) | Unit Str in TTRPG mass combat | Use B.2 conversion: TTRPG Str = ⌈BG Health ÷ 1.5⌉ (PP-103). state_transfer_spec "1:1" was wrong — corrected PP-107. |
| Unit Cohesion (BG: 0–6) | Unit Cohesion (TTRPG: 1–7) | BG Cohesion 0 → TTRPG Cohesion 1 (floor). BG 1–6 → TTRPG 1–6 direct. BG max 6 ≠ TTRPG max 7. [PP-107] |
| Unit Morale | Unit Morale (TTRPG: 1–7) | BG does not track Morale separately (PP-119: Cohesion subsumes both). On Zoom In: set TTRPG Morale = BG Cohesion + 1, max 7. [PROVISIONAL PP-107] |
| Unit Martial (BG: 1–5) | Unit CP (TTRPG: 1–7) | Use B.2 TTRPG CP column — not 1:1. BG Martial is a BG-specific stat; B.2 maps each unit type to TTRPG CP. [PP-107] |
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
| Debate outcome (Conviction Track ≥7 or ≤3) | Queue as Domain Echo: faction Mandate ±1 (winner's faction +1, loser −1 if applicable). Fires at next Accounting. [PP-108] |
| Gap aversion (Thread Weaving stabilised) | No BG stat change. RS unchanged (Object-scale). Narrative note: territory has a known instability for future Investigation actions. |

### Phase-Lock Protocol (PP-103) — replaces prior interruption protocol

Zoom In fires only at one of three legal phase-lock points:

| Phase-lock point | When it fires | State at Zoom In |
|-----------------|---------------|-----------------|
| After Phase 1 | Orders placed, nothing resolved | Clean — no damage recorded |
| After Phase 3 | Manoeuvre complete, pre-Engagement | Units positioned; no damage |
| After Phase 6 Step 1 | All damage applied simultaneously | Clean — no ghost units |

**If trigger occurs mid-phase:** Hold Zoom In until the end of the current phase.
The current phase completes fully before the TTRPG scene opens.

**Why three points only:** Phases 2 (Volley), 4 (Offensive Thread), and 5
(Engagement) record damage but do not apply it. Allowing Zoom In during these
phases creates ghost units — units at 0 recorded damage that haven't yet been
removed. Phase-Lock eliminates this class of error.

**Accounting:** Always completes before Zoom In fires (unchanged).

**Phase 6 Step 1 Zoom In — continuation protocol (PP-110):**
After Step 1 (all damage applied), Zoom In fires. TTRPG scene runs. Zoom Out updates Str and NPC kills using updated state. Then Phase 6 Steps 2–6 resume:
- Step 2 (Cohesion checks): use Strength values from Zoom Out update.
- Step 3 (Morale checks): use Morale values from Zoom Out update.
- Step 4 (General action): available unless the PC general is the Zoom In character (their Step 4 is consumed by the Zoom In scene).
- Steps 5–6 (Support Thread, Reform): resolve normally.

**Concurrent Zoom Ins — provisional procedure (PP-112):**
If two PCs simultaneously trigger Zoom In in different battles, resolve in faction-turn order (Accounting sequence). First battle's full scene (Zoom In → TTRPG → Zoom Out) completes before the second begins. All other faction turns hold throughout both.

**Non-battle Zoom In (PP-112 scope — ED-073 open):**
Zoom In can also trigger in BG territory contexts outside active battle (political scenes, Thread investigations). Phase-Lock only covers battle phases. For non-battle Zoom In: trigger at the end of the current BG Domain Action being resolved. No unit conversion needed (no units present). Faction stats still suspend; RS still transfers immediately. Full procedure pending ED-073.

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

## 5. TRANSITION P1 ITEMS STATUS

| ID | Issue | Location | Status |
|----|-------|----------|--------|
| T1-P1-01 | Thread→Mass timing: Priority 1 (stage11) vs Phase 5 (mass_battle_v3) | stage11 §11.3 vs mass_battle_v3 §A.7 | RESOLVED (2026-04-02 — see below) — [EDITORIAL: requires decision; see options A/B/C below] |
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


## DEBATE (Zoom In/Out — PARTIAL)

**Status:** Partially defined. State handoff at debate conclusion is documented in §6.5. BG→TTRPG Zoom In is undefined.

| Transition | State Variables | Conversion Rule | Status |
|-----------|----------------|-----------------|--------|
| TTRPG debate end → BG faction stats | TC position, winner's genre, Thread consequences | §6.5 stakes resolve; Domain Echo table stub PP-110 | Partially defined |
| BG Parliamentary Vote → TTRPG Formal Debate (Zoom In) | Vote count → TC start position | **UNDEFINED** [K2-F-02] | GAP — P1 |
| BG Parliamentary Vote → TTRPG Formal Debate (Zoom In) | Remaining vote rounds → Exchange count | **UNDEFINED** [K2-F-02] | GAP — P1 |

**K2-F-02 resolution needed before BG↔TTRPG debate Zoom In is playable.**
