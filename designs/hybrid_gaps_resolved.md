# Hybrid Gap Resolutions
## Session: 2026-03-26

All 17 open hybrid design gaps resolved. Ready for compilation into Hybrid Mode Supplement.

---

## BATCH G1 — SESSION STRUCTURE

### G-075 — Hybrid Session Structure
Phase sequence: Personal → Strategic → Cascade.
Personal phase duration: 90–150 minutes, depending on number of TTRPG scenes that session.
Strategic and Cascade phases follow; no fixed time target for these (accounting-driven).
A phase may be shortened if no content fires (e.g. no board orders pending = Strategic phase skipped).

### G-091 — Hybrid Session Pacing
Minimum 1 real-world session per in-game season. No maximum — a season may span multiple sessions if scene volume warrants. Seasonal accounting fires at the end of the session in which the season closes, not mid-session.

---

## BATCH G2 — HANDOFFS

### G-079 — Information Asymmetry (Fog of War)
All faction stats (Mandate, Influence, Wealth, Military, Intelligence, Stability) are displayed to non-owning players in four qualitative states:

| Display | Underlying value |
|---------|-----------------|
| In ruins | 1 |
| Poor | 2–3 |
| Good | 4–5 |
| Excellent | 6–7 |

**Boundary ambiguity:** A stat at exactly 4 has a 50/50 chance of displaying as Poor or Good each time it is observed. Roll 1d6 at point of observation: 1–3 = Poor, 4–6 = Good. The result is fixed for that scene but re-rolled next observation.

**Faction-leader PCs** see their own faction's exact numerical values at all times. All other factions are fog-of-war.

**Hidden stats:** Intelligence is always hidden (no qualitative display to any player for rival factions). It is only revealed through successful Intelligence Domain Actions or TTRPG scene discoveries.

### G-080 — Cross-System Handoff Rules
Default: all TTRPG personal-scene consequences batch to the **Cascade phase** for application to the board. GM tracks consequences on a ledger during the Personal phase and applies them in bulk.

Exception: if the GM judges a consequence is simple enough to track inline (single stat change, no threshold risk), they may apply it immediately. This is a GM call, not a player option.

The 12 handoff types resolve as follows:

| Handoff type | Resolution |
|---|---|
| Personal action → faction stat change | Batch to Cascade |
| Thread op → clock change | Batch to Cascade (applied in Cascade step 2) |
| Domain Echo from personal scene | Batch to Cascade (applied in Cascade step 1) |
| Board order → TTRPG scene trigger | Fires at start of next Personal phase (see G-081) |
| Faction stat change → personal consequence | GM narrates consequence in next Personal phase scene |
| NPC action → personal character impact | GM narrates; fires in correct scene sequence (see G-081) |
| Clock threshold → institutional response | Fires in Cascade step 3; GM queues response for next Personal phase |
| PC death → faction state | Fires in Cascade (see G-086) |
| Faction collapse → personal state | Fires in Cascade (see G-087) |
| Flashback → board state | Not permitted (see G-092) |
| Resources spent → Wealth impact | Evaluated in Cascade (see G-093) |
| Expedition absence → faction orders | Handled per G-095 |

### G-081 — Board Game Order → TTRPG Scene Triggers
**Zoom In is for player-involved interactions only.** Any order that resolves entirely between NPCs (no PC present) does not generate a TTRPG scene — the GM narrates the outcome so players have the information for their next scene.

An order generates a mandatory TTRPG scene if:
- A PC is the target or perpetrator of the order's primary action
- A PC's named Knot or Inspiration focus is directly affected
- A clock crosses a threshold as a direct result and a PC is present in the affected territory

**Sequencing rule:** NPC-only orders resolve first within the Strategic phase. Their outcomes are narrated before player-involved scenes begin, so that player scenes that are impacted by prior NPC action occur in the correct narrative order. Players may not retroactively modify NPC-only resolutions via Flashback (see G-092).

### G-083 — Thread Operation Scale Authority in Hybrid
Personal-scale Thread operations performed during the Personal phase resolve as TTRPG narrative consequences. Their clock and tracker effects (TT, ThS, Coherence, co-movement) are noted by the GM and batched to the Cascade phase.

A **faction-scale Thread order** (Weave, Investigate, Harvest on the board) represents a collective, premeditated, planned operation by faction agents — distinct from a personal practitioner's Leap. These resolve in the Strategic phase under board game rules and generate a Co-Movement Card draw rather than personal co-movement effects.

A personal Thread op during the Personal phase does not substitute for or generate a faction Thread order. The two tracks are parallel.

### G-085 — Hybrid Siege Protocol
Sieges run at board game scale across multiple seasons. TTRPG scenes fire during a siege when:

1. **Players seek contact** — players choose to hunt down a named opponent (e.g. pursuing a general, attempting to negotiate surrender). This generates a mandatory TTRPG scene at player initiative.
2. **Mechanical trigger** — a named NPC's mass battle unit attacks a PC's mass battle unit (or vice versa). This generates a mandatory Zoom In TTRPG scene for that engagement.

All other siege activity resolves at board game scale without Zoom In. The siege duration, attrition, and strategic outcome remain board game mechanics.

### G-092 — Flashback Scope Limits
Flashbacks are Personal phase only. A Flashback may establish facts from the character's past but may not alter, retcon, or modify any board game state that was resolved in the Strategic phase of the same or any prior session. Flashback scope is bounded by the Personal phase in which it is declared.

### G-093 — Cross-Mode Resource/Wealth Interaction
When a PC spends Resources during a TTRPG scene, evaluate at Cascade phase:

**No faction Wealth impact** if: Faction Wealth ≥ 2× Resources rolled.
*Example: PC rolls 2 Resources; faction Wealth 5 (≥ 4). No impact.*

**Faction Wealth stressed** (−1 Wealth, recovers next season) if: Faction Wealth < 2× Resources rolled.
*Example: PC rolls 3 Resources; faction Wealth 5 (< 6). Wealth stressed.*

**Stress formula:** threshold = 2 × Resources rolled. If Wealth < threshold → stressed.

Note for testing: the formula may need adjustment to 2×−1 (threshold = (2 × Resources) − 1) if edge cases produce narrative mismatches. Flag during Phase 3 stress testing.

Same logic applies to Circles vs. Influence: Circles dice rolled vs. Influence × 2.

### G-094 — Cascade Phase Process
The Cascade phase is GM-controlled accounting. Players do not take actions during it. The GM works through the following steps in order:

1. **Domain Echoes** — apply all TTRPG personal-scene consequences from the GM ledger to faction stats on the board.
2. **Thread consequences** — apply co-movement clock/tracker effects from any Thread operations this session (TT changes, ThS loss, Coherence changes).
3. **Clock checks** — check TT, TC, IP against thresholds. Fire threshold events in order: TT first, then TC, then IP. Queue any institutional responses for the next Personal phase.
4. **Seasonal accounting** (end of season only) — faction stat changes from board orders, Knot strain ticks, ThS recovery (+2 if no Thread ops this season), Coherence recovery (Corrective Weaving results), advancement (CP awards, test track advances).
5. **Board state update** — GM physically updates the board to reflect all of the above. This is the final state players see at the start of the next Strategic phase.

The Cascade phase is not skippable. If nothing fires in steps 1–3 and it is not end of season, steps 4–5 are abbreviated (board update only).

### G-095 — Southernmost Expedition: Multi-Season Management
Only relevant if the expeditioning PC is a faction leader.

If **another PC can proxy**: that PC takes over faction orders during the Strategic phase for the duration of the expedition. They use the faction's stats as normal. The absent PC retains faction leadership narratively.

If **no PC can proxy**: the faction runs on NPC AI logic for the duration. The GM executes orders according to the faction's AI algorithm (as established in the board game NPC rules). The faction leader PC may send one instruction per season (a Belief-level directive) which the AI prioritises if not in conflict with faction survival logic.

The expedition PC continues TTRPG scenes normally during the Personal phase. Their faction participation is suspended, not their character activity.

---

## BATCH G3 — CONSEQUENCES

### G-086 — PC Death → Faction Succession
On PC death: faction enters **Crisis** state (−1 to all faction stats for one season; no cap on further natural decline during Crisis).

Player options (choose one):
1. **Take over an existing faction-loyal NPC** as new PC. That NPC becomes a full PC with their existing stat block. No newly generated characters.
2. **Designate another PC** as faction successor (if another player agrees). The dying player then creates a new personal character (not faction leader) using standard creation rules.
3. **Let the faction pass to a named NPC** (GM-controlled). The dying player creates a new personal character unaffiliated with that faction.

The succession must be resolved within the same Cascade phase as the death. If unresolved, option 3 defaults automatically.

### G-087 — Faction Collapse → Personal Consequences
The PC continues as a personal character. They lose all dice bonuses derived from that faction (Circles dice tied to the faction, any faction-stat-derived pool modifiers). Personal attributes, Histories, Knots, Inspirations, and Beliefs are unaffected.

The PC may attempt to found or join a successor faction through play — this is a narrative path, not a mechanical reset.

### G-088 — Hybrid Downtime
Downtime activities (training, Inspiration recovery, Knot repair, Approach Training practice) run concurrently with the Strategic phase. PCs may declare and resolve downtime actions during the Strategic phase without consuming Personal phase time. Downtime is not replaced by Strategic phase participation.

### G-089 — Hybrid Advancement
Board game successes generate CP and personal advancement. The character performed those actions; the zoom level does not affect whether the experience counts. CP award uses the same criteria as TTRPG (Belief engagement, significant Domain Action, Maxim expression). GM adjudicates at Cascade/seasonal accounting.

### G-090 — Knot/Inspiration Tracking from Board Events
**Gated by information.** Mechanical consequences to Knots and Inspirations from board events do not apply until the PC learns about the event in a TTRPG scene.

**Exception:** If the very next TTRPG scene after the board event is directly and immediately connected to that event (e.g. the PC witnesses the death, or the scene opens in the immediate aftermath), the consequence applies at scene open — time has not passed and the gating condition is met.

In all other cases (subsequent sessions, time skip implied), the consequence applies at the moment of in-scene discovery.

---

## SUMMARY TABLE

| Gap | Status | Key decision |
|-----|--------|-------------|
| G-075 | Resolved | Personal phase 90–150 min |
| G-079 | Resolved | Four qualitative states; fog for all; exact for own faction; Intel always hidden |
| G-080 | Resolved | Batch to Cascade; GM ledger; inline exception at GM discretion |
| G-081 | Resolved | Zoom In player-only; NPC-only narrated; sequencing enforced |
| G-083 | Resolved | Personal → TTRPG narrative + clock batch; faction order → Co-Movement Card |
| G-085 | Resolved | Player-initiated or mechanical trigger; all else board scale |
| G-091 | Resolved | 1 session minimum per season |
| G-092 | Resolved | Personal phase only; no Strategic phase impact |
| G-093 | Resolved | Threshold = 2× rolled; below threshold = stressed; test 2×−1 variant |
| G-094 | Resolved | 5-step Cascade sequence; GM-only; not skippable |
| G-095 | Resolved | PC proxy or NPC AI + 1 directive/season |
| G-086 | Resolved | Crisis penalty; take over loyal NPC or succession; no new characters |
| G-087 | Resolved | Continue as personal character; lose faction dice bonuses |
| G-088 | Resolved | Downtime concurrent with Strategic phase |
| G-089 | Resolved | Board successes generate CP; zoom level irrelevant |
| G-090 | Resolved | Gated by in-scene discovery; exception for immediate-next scene |
