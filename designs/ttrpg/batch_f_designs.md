# Phase 1 — Batch F: Hybrid + Endgame
## Date: 2026-03-25 (Session 5)
## Status: Designed
## Covers: G-018, G-021, G-023

---

## G-018: Hybrid Timing Reference Table

Maps real-world session time to game time across all three modes.

### Time Equivalences

| Mode | 1 Real Session (~3-4 hrs) | 1 Game Season | 1 Campaign (~10 seasons) |
|------|--------------------------|---------------|--------------------------|
| TTRPG | 2-4 scenes (1 season or less) | 1-2 sessions | 15-25 sessions |
| Board game | 3-5 seasons | ~15-20 min | 1 session (2-4 hrs) |
| Hybrid | 1 season (Personal + Strategic + Cascade) | 1 session | 10-15 sessions |

### Hybrid Session Structure (per season)

| Phase | Duration | Content |
|-------|----------|---------|
| Personal Phase | 60-90 min | TTRPG scenes. Board game paused. 2-3 scenes max. |
| Strategic Phase | 20-30 min | Board game orders placed and resolved. TTRPG paused. |
| Cascade Phase | 10-15 min | Domain Echoes, threshold events, cross-mode consequences applied. |
| Accounting | 5-10 min | Attribute changes, clock advances, victory checks. |

**Total per hybrid season: ~2-2.5 hrs. A full hybrid campaign of 10 seasons = 10-15 sessions.**

### Pacing Controls

- **GM may compress:** Skip Personal Phase for a season if no TTRPG scenes are dramatically necessary. Announce "quiet season" — resolve Strategic + Cascade only (~30 min).
- **GM may expand:** Split one season across 2 sessions if TTRPG scenes demand it (siege, expedition, major social confrontation). Strategic Phase deferred to session 2.
- **Player-triggered scenes:** During Strategic Phase, if an order generates a scene (e.g., assassination attempt, diplomatic confrontation), pause resolution and run the TTRPG scene. Return to resolution queue after scene concludes.

### Clock Synchronization

All three clocks (TT, TC, IP) advance at Accounting regardless of mode. In hybrid, this means:
- TTRPG scenes may trigger Domain Echoes that modify clocks mid-season (applied at Cascade Phase, not immediately).
- Board game orders that affect clocks resolve at Accounting.
- No clock advances between Personal and Strategic phases — everything batches to Accounting.

---

## G-021: Endgame Conditions (All Three Modes)

### Shared Loss Condition (all modes)
**TT reaches 100.** The Rupture. Rendered reality fails. Campaign ends in catastrophe. No faction wins.

### TTRPG Endgame
**No explicit victory condition.** The TTRPG campaign ends when the GM and players agree the central dramatic questions have been resolved or exhausted. Endgame emerges from character arcs, not mechanical triggers.

**Endgame indicators (GM guidance, not rules):**
- All PCs have resolved or abandoned their central Beliefs.
- TT has been reduced below 20 or has exceeded 80 (the world is saved or doomed).
- The succession crisis has resolved (Torben, Elske, Parliament, or coup).
- The Church's authority is broken or triumphant (TC below 20 or above 80).
- Altonia has invaded or been permanently deterred.
- At least one PC has died, retired, or fundamentally transformed.

**The GM should signal endgame 2-3 sessions before the final session.** "We're approaching the end of this story. What does your character want to resolve?"

### Board Game Endgame
**Explicit victory conditions per faction** (see G-028 in Batch E). Checked at end of each season.

**Additional endgame triggers:**
- Season 10 reached: highest point total wins.
- TT 100: all lose.
- If 3+ factions collapse (Stability 0): remaining factions share a diminished victory (the world survives but is broken).

**Final scoring tiebreak:** Stability (most internally coherent faction endures).

### Hybrid Endgame
**Both systems active.** Victory requires satisfying BOTH personal and strategic conditions.

**Hybrid victory:** A faction achieves its board game primary victory condition AND the faction leader (PC) has resolved their central Belief arc in a way that supports the victory. If the board game condition is met but the PC's arc contradicts it (e.g., Crown controls 5 territories but Almud has abandoned his duty Belief), the victory is hollow — the faction wins but the character doesn't.

**Hollow victory:** The player may accept a hollow victory (mechanical win, narrative loss) or reject it (continue playing until the personal arc resolves or fails, risking the mechanical victory eroding). This is a player choice, not a rule.

**Hybrid loss:** TT 100, or faction collapse with no personal resolution. Both are catastrophic.

---

## G-023: Mode-Specific Rule Branching Catalogue

Comprehensive list of rules that differ by mode. This is a reference document, not a design — it catalogues where the three modes diverge.

### Combat

| Rule | TTRPG | Board Game | Hybrid |
|------|-------|-----------|--------|
| Personal combat | Pool split, priority table, reach, maneuvers | Not applicable | TTRPG rules during Personal Phase |
| Mass combat | Zone-based operational, Zoom In/Out | Disposition table (single roll per battle) | Board game resolution; Zoom In to TTRPG for key moments |
| Siege | Multi-season procedure with scenes | Siege order vs Fortification (single roll) | Board game resolution; TTRPG scenes for infiltration/breakout |

### Social

| Rule | TTRPG | Board Game | Hybrid |
|------|-------|-----------|--------|
| Debate/Appeal | Full social combat (exchanges, Composure, rhetoric) | Not applicable | TTRPG rules during Personal Phase |
| Negotiation | Roleplay + social roll | Treaty order (mechanical) | Treaty order triggers TTRPG social scene if both parties are PCs |
| Excommunication | Grand Debate (5 exchanges) | Single roll (Church Mandate vs target) | Board game roll; TTRPG scene for the trial if desired |

### Faction

| Rule | TTRPG | Board Game | Hybrid |
|------|-------|-----------|--------|
| Domain Actions | Implicit — GM recognizes faction-scope personal actions | Explicit — Order Set with placement and resolution | Strategic Phase uses board game orders; Personal Phase uses TTRPG Domain Echoes |
| Stability checks | Triggered by Domain Echo consequences | Triggered at Accounting | Batched to Cascade Phase |
| Seasonal cap | ±2 per attribute per season | ±2 per attribute per season | Same — shared across both phases |

### Thread

| Rule | TTRPG | Board Game | Hybrid |
|------|-------|-----------|--------|
| Thread operations | Personal-scale (Weaving, Pulling, Leaps) with full narrative | Faction-scale (Weave/Investigate/Harvest orders) with Co-Movement Card | Personal Phase: TTRPG Thread ops. Strategic Phase: board game Thread orders. Both count toward seasonal TT changes. |
| Co-movement | Version C (automatic deterministic + actual d6) | Co-Movement Card deck (15 cards) | Personal Phase: Version C. Strategic Phase: Co-Movement Cards. |
| Discovery Events | Full narrative scene | Attribute change only (no scene) | TTRPG scene triggered by board game Discovery Event |

### Advancement

| Rule | TTRPG | Board Game | Hybrid |
|------|-------|-----------|--------|
| CP spending | Full menu (Batch A design) | Not applicable — faction attributes change, not character skills | TTRPG CP spending during Personal Phase only |
| Faction attribute changes | Domain Echoes at seasonal accounting | Order resolution at Accounting | Both — cumulative, shared seasonal cap |
| Renown | Tracked per character | Not tracked (faction-level Mandate substitutes) | TTRPG Renown tracked; informs board game Mandate via Cascade Phase |

### Clocks

| Rule | TTRPG | Board Game | Hybrid |
|------|-------|-----------|--------|
| TT/TC/IP advance | At seasonal accounting | At Accounting (Phase 5) | At Accounting (Cascade Phase) — identical |
| Threshold events | GM narrates and runs scenes | Event card or table lookup | Board game trigger; GM may run TTRPG scene for narratively significant thresholds |

### Key Principle
Where a rule exists in both modes, the **seasonal cap is shared**. A faction attribute cannot change by more than ±2 per season regardless of how many Domain Echoes (TTRPG) and orders (board game) target it. This prevents hybrid mode from doubling attribute velocity.

---

## Canon Compliance
- **P-05 (three modes distinct):** This catalogue explicitly documents where modes diverge and why.
- **P-14 (all modes express inseparability):** Thread consequences present in all three modes — Version C in TTRPG, Co-Movement Cards in board game, both in hybrid.
- **P-11 (TD universal):** No mode permits free Thread operations. TTRPG has TD per Version C. Board game has Co-Movement Cards. Hybrid has both.

---

# BATCH F SUMMARY

| Gap | Status | Editorial |
|-----|--------|-----------|
| G-018 | Designed | None |
| G-021 | Designed | None — hollow victory is player choice, not mechanical |
| G-023 | Designed | None |

**Phase 1 complete. All 38 design gaps resolved (Batches A through F).**
