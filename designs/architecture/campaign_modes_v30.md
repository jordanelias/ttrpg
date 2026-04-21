<!-- SKELETON — mechanical spec only — atomized 2026-04-13 -->
<!-- Infill: campaign_modes_v30_infill.md -->

<!-- v30 baseline — design-layer doc created 2026-04-13 from compilation/v0.14/stage12_campaign_modes_deprecated.md -->
<!-- UNVERIFIED: mechanical values in this doc have not been confirmed by simulation. -->
<!-- Flag any value used in simulation: [UNVERIFIED: <value> — pending stress test] -->
<!-- Mode: ALL -->
<!-- Authority: designs/ working layer — pending compilation -->

# PART TWELVE: CAMPAIGN MODES


---

## 12.1 TTRPG Mode

### Session Structure


**Typical session flow:**

| Phase | Duration | Content |
|---|---|---|
| Opening | 10 min | Recap, clock positions, active Beliefs reviewed |
| Scene 1 | 60–90 min | Primary dramatic scene (combat, social, Thread operation, investigation) |
| Scene 2 (optional) | 45–60 min | Secondary scene driven by Scene 1 consequences |
| Accounting | 15 min | Apply Domain Echoes, advance clocks, assign CP |


**Campaign scale**: A full TTRPG campaign of 10–15 seasons runs 15–25 sessions.

### Session Zero Protocol

2. Set Safety Tools.
3. Create Characters: 3 Histories at 2 points each; 31 points; declare 3–5 Knots.
4. Set clocks: Mending Stability 72, Theocracy Counter 15, Institutional Pressure 20.
5. Review the Action Economy and Scope Shift procedure.

### TTRPG Endgame


**Endgame indicators (Game Master guidance — not triggers):**
- All PCs have resolved or abandoned their central Beliefs.
- Mending Stability has risen above 80 (world recovering) or fallen below 20 (world doomed).
- The succession crisis has resolved (Torben, Elske, Parliament, or coup).
- The Church's authority is broken or triumphant (Theocracy Counter below 20 or above 80).
- Altonia has invaded or been permanently deterred.
- At least one Player Character has died, retired, or fundamentally transformed.


---

## 12.2 Board Game Mode

### Session Structure


**Typical session flow:**

| Phase | Duration | Content |
|---|---|---|
| Setup | 10–15 min | Faction assignment, starting stats, clock positions, first-season orders |
| Season loop × 3–5 | 25–40 min each | Planning → Resolution → Accounting |
| Endgame check | 5 min | Victory condition evaluation |

### Board Game Endgame

Victory conditions are checked at the end of each season's accounting phase.

**Shared loss condition (all modes):** Mending Stability reaches 0. The Rupture. No faction wins.

**Additional endgame triggers:**
- Season 10 reached: highest point total wins.
- 3+ factions collapse (Stability 0): remaining factions share a diminished victory.

**Tiebreak:** Stability — the most internally coherent faction endures.

---

## 12.3 Hybrid Mode

### Hybrid Session Structure

One hybrid session covers one season, structured in four phases:

| Phase | Duration | Content |
|---|---|---|
| Personal Phase | 60–90 min | TTRPG scenes. Board game paused. Maximum 2–3 scenes. |
| Strategic Phase | 20–30 min | Board game orders placed and resolved. TTRPG paused. |
| Cascade Phase | 10–15 min | Domain Echoes, threshold events, and cross-mode consequences applied. |
| Accounting | 5–10 min | Attribute changes, clock advances, victory condition checks. |

**Total per hybrid season: ~2–2.5 hrs. A full hybrid campaign of 10 seasons = 10–15 sessions.**

### Pacing Controls




### Clock Synchronisation

All three clocks (Mending Stability, Theocracy Counter, Institutional Pressure) advance at Accounting regardless of mode. In hybrid:
- Board game orders that affect clocks resolve at Accounting.
- No clock advances between Personal and Strategic phases — everything batches to Accounting.

### Hybrid Endgame




**Hybrid loss:** Mending Stability 0, or faction collapse with no personal resolution.

---

## 12.4 Hybrid Timing Reference Table

| Measure | TTRPG | Board Game | Hybrid |
|---|---|---|---|
| 1 real session (~3–4 hrs) | 2–4 scenes (1 season or less) | 3–5 seasons | 1 season (all four phases) |
| 1 game season | 1–2 sessions | ~15–20 min | 1 session |
| Full campaign (10 seasons) | 15–25 sessions | 1 session (2–4 hrs) | 10–15 sessions |

---

## 12.5 Mode-Specific Rule Branching

Where the three modes diverge mechanically:

### Combat

| Rule | TTRPG | Board Game | Hybrid |
|---|---|---|---|
| Personal combat | Pool split, priority table, reach, maneuvers | Not applicable | TTRPG rules during Personal Phase |
| Mass combat | Zone-based operational; Zoom In/Out for personal moments | Disposition table, single roll per battle | Board game resolution; Zoom In to TTRPG for named-Non-Player Character moments |
| Siege | Multi-season procedure with scenes (§8.4) | Siege order vs Fortification (single roll) | Board game roll; TTRPG scenes for infiltration or breakout |

### Social

| Rule | TTRPG | Board Game | Hybrid |
|---|---|---|---|
| Debate/Appeal | Full social combat (exchanges, Composure, rhetoric) | Not applicable | TTRPG rules during Personal Phase |
| Negotiation | Roleplay + social roll | Treaty order (mechanical) | Treaty order triggers TTRPG social scene if both parties are PCs |
| Excommunication | Grand Debate (5 exchanges) | Single roll (Church Mandate vs target) | Board game roll; TTRPG scene for the trial if desired |

### Faction

| Rule | TTRPG | Board Game | Hybrid |
|---|---|---|---|
| Domain Actions | Implicit — Game Master recognises faction-scope from personal roll | Explicit — Order Set with placement and resolution | Strategic Phase uses board game orders; Personal Phase uses TTRPG Domain Echoes |
| Stability checks | Triggered by Domain Echo consequences | Triggered at Accounting | Batched to Cascade Phase |
| Seasonal cap | ±2 per attribute per season | ±2 per attribute per season | Shared — applies across both phases |

### Thread

| Rule | TTRPG | Board Game | Hybrid |
|---|---|---|---|
| Thread operations | Personal-scale (Weaving, Pulling, Mending, Leaps) with full narrative | Faction-scale (Weave/Mend/Investigate/Harvest orders) with Co-Movement Card | Personal Phase: TTRPG Thread ops. Strategic Phase: board game Thread orders. Both count toward seasonal Mending Stability. |
| Co-movement | Version C (automatic deterministic + actual d6) | Co-Movement Card deck (18 cards) | Personal Phase: Version C. Strategic Phase: Co-Movement Cards. |
| Discovery Events | Full narrative scene | Attribute change only (no scene) | TTRPG scene triggered by board game Discovery Event |

### Advancement

| Rule | TTRPG | Board Game | Hybrid |
|---|---|---|---|
| CP spending | Full menu (§10.2) | Not applicable — faction attributes change, not character skills | TTRPG CP spending during Personal Phase only |
| Faction attribute changes | Domain Echoes at seasonal accounting | Order resolution at Accounting | Both — cumulative, shared seasonal cap |
| Renown | Tracked per character | Not tracked (faction Mandate substitutes) | TTRPG Renown tracked; informs board game Mandate via Cascade Phase |

### Clocks

| Rule | TTRPG | Board Game | Hybrid |
|---|---|---|---|
| Mending Stability/Theocracy Counter/Institutional Pressure advance | At seasonal accounting | At Accounting | At Accounting (Cascade Phase) — identical |
| Threshold events | Game Master narrates and runs scenes | Event card or table lookup | Board game trigger; Game Master may run TTRPG scene for narratively significant thresholds |



---

## 12.6 The Game Master as Rendering Engine




### Co-Movement at the Table

1. Describes the primary intended effect.
3. Narrates the secondary consequence as part of the scene.


### Mending Stability Threshold Events

When Mending Stability crosses a threshold (downward), the Game Master determines a narratively appropriate consequence from the current situation. No event deck. The current political, social, and thread-level state of the world should generate the threshold consequence organically. See §5.4.3 for the full Mending Stability threshold table.

---

## 12.7 The Coherence Track as Campaign Arc

Coherence is not a per-session tactical resource. It degrades over the course of the campaign as practitioners operate at scale. Thresholds represent campaign stages:

| Coherence | State | Character experience |
|---|---|---|
| 10–8 | Stable | Early-campaign. No penalty. Rendering solid. |
| 7–5 | Dissonant | Narrative flickers. Knots begin sensing wrongness. |
| 4–3 | Fragmented | Mid-campaign cost of active practice. −1D social and memory rolls. +1 Ob Thread operations. |
| 2 | Fractured | Late-campaign pressure. −2D social/memory. Dissociative episodes on Thread ops. |
| 1 | Severed | Endgame condition. +2 Ob Thread operations. Barely functional rendering. |
| 0 | Rendering Crisis | The practitioner must choose: withdraw, recover, or accept the consequences. |

An active practitioner working at Relational+ scale through a full campaign will enter Dissonant by mid-campaign and approach Fragmented by the end. This is the game's structural statement about the cost of sustained Thread work. See §5.2.3 for full threshold effects.

---

## 12.8 Running the Noble-Church Triangle

The three-way relationship between Baralta (Church-devout, anti-overreach), Vaynard (anti-Church, knowledge-seeking), and Confessor Himlensendt (theocratic consolidation) generates political action without requiring predetermined outcomes. Track seasonal accounting. Apply triggers consistently. Outcomes emerge from the configuration.

**The excommunication scenario.** If Olafsson opens a Heresy Investigation against Baralta: Grand Debate, 5 exchanges. Church represented by Olafsson (Composure 7, pool: Church Reach 7 + Ecclesiastical Law). If it succeeds: Mandate −2, Theocracy Counter +3, Theocracy Counter suppression removed. If players defend her or supply documentary evidence: the investigation can be derailed or reversed.


**The Crown's choice when Vaynard is exposed.** Resolved as a Parliamentary Vote (§7.4):
- Defend Vaynard: Theocracy Counter +2; Crown-Church relations fracture; Baralta must choose sides.
