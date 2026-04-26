<!-- SKELETON — mechanical spec only — atomized 2026-04-13 -->
<!-- Infill: hybrid_gaps_v30_infill.md -->

<!-- v30 baseline — renamed from designs/hybrid/hybrid_gaps_resolved.md on 2026-04-13 -->
# Hybrid Gap Resolutions
## Session: 2026-03-26

All 17 open hybrid design gaps resolved. Ready for compilation into Hybrid Mode Supplement.

---

## BATCH G1 — SESSION STRUCTURE

### G-075 — Hybrid Session Structure
Phase sequence: Personal → Strategic → Cascade.
Personal phase duration: 90–150 minutes, depending on number of TTRPG scenes that session.
Strategic and Cascade phases follow; no fixed time target for these (accounting-driven).

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




### G-080 — Cross-System Handoff Rules

Exception: if the Game Master judges a consequence is simple enough to track inline (single stat change, no threshold risk), they may apply it immediately. This is a Game Master call, not a player option.

The 12 handoff types resolve as follows:

| Handoff type | Resolution |
|---|---|
| Personal action → faction stat change | Batch to Cascade |
| Thread op → clock change | Batch to Cascade (applied in Cascade step 2) |
| Domain Echo from personal scene | Batch to Cascade (applied in Cascade step 1) |
| Board order → TTRPG scene trigger | Fires at start of next Personal phase (see G-081) |
| Faction stat change → personal consequence | Game Master narrates consequence in next Personal phase scene |
| Non-Player Character action → personal character impact | Game Master narrates; fires in correct scene sequence (see G-081) |
| Clock threshold → institutional response | Fires in Cascade step 3; Game Master queues response for next Personal phase |
| Player Character death → faction state | Fires in Cascade (see G-086) |
| Faction collapse → personal state | Fires in Cascade (see G-087) |
| Flashback → board state | Not permitted (see G-092) |
| Resources spent → Wealth impact | Evaluated in Cascade (see G-093) |
| Expedition absence → faction orders | Handled per G-095 |

### G-081 — Board Game Order → TTRPG Scene Triggers

An order generates a mandatory TTRPG scene if:
- A Player Character is the target or perpetrator of the order's primary action
- A Player Character's named Knot or Inspiration focus is directly affected
- A clock crosses a threshold as a direct result and a Player Character is present in the affected territory


### G-083 — Thread Operation Scale Authority in Hybrid
Personal-scale Thread operations performed during the Personal phase resolve as TTRPG narrative consequences. Their clock and tracker effects (Thread Tension, ThS, Coherence, co-movement) are noted by the Game Master and batched to the Cascade phase.



### G-085 — Hybrid Siege Protocol
Sieges run at board game scale across multiple seasons. TTRPG scenes fire during a siege when:



### G-092 — Flashback Scope Limits

### G-093 — Cross-Mode Resource/Wealth Interaction

**No faction Wealth impact** if: Faction Wealth ≥ 2× Resources rolled.
*Example: Player Character rolls 2 Resources; faction Wealth 5 (≥ 4). No impact.*

*Example: Player Character rolls 3 Resources; faction Wealth 5 (< 6). Wealth stressed.*

**Stress formula:** threshold = 2 × Resources rolled. If Wealth < threshold → stressed.

Note for testing: the formula may need adjustment to 2×−1 (threshold = (2 × Resources) − 1) if edge cases produce narrative mismatches. Flag during Phase 3 stress testing.

Same logic applies to Circles vs. Influence: Circles dice rolled vs. Influence × 2.

### G-094 — Cascade Phase Process

2. **Thread consequences** — apply co-movement clock/tracker effects from any Thread operations this session (Thread Tension changes, ThS loss, Coherence changes).
3. **Clock checks** — check Thread Tension, Church Influence, Institutional Pressure against thresholds. Fire threshold events in order: Thread Tension first, then Church Influence, then Institutional Pressure. Queue any institutional responses for the next Personal phase.
4. **Seasonal accounting** (end of season only) — faction stat changes from board orders, Knot strain ticks, ThS recovery (+2 if no Thread ops this season), Coherence recovery (Corrective Weaving results), advancement (CP awards, test track advances).


### G-095 — Southernmost Expedition: Multi-Season Management
Only relevant if the expeditioning Player Character is a faction leader.




---

## BATCH G3 — CONSEQUENCES

### G-086 — Player Character Death → Faction Succession
On Player Character death: faction enters **Crisis** state (−1 to all faction stats for one season; no cap on further natural decline during Crisis).

Player options (choose one):


### G-087 — Faction Collapse → Personal Consequences
The Player Character continues as a personal character. They lose all dice bonuses derived from that faction (Circles dice tied to the faction, any faction-stat-derived pool modifiers). Personal attributes, Histories, Knots, Inspirations, and Beliefs are unaffected.


### G-088 — Hybrid Downtime

### G-089 — Hybrid Advancement

### G-090 — Knot/Inspiration Tracking from Board Events



---

## SUMMARY TABLE

| Gap | Status | Key decision |
|-----|--------|-------------|
| G-075 | Resolved | Personal phase 90–150 min |
| G-079 | Resolved | Four qualitative states; fog for all; exact for own faction; Intel always hidden |
| G-080 | Resolved | Batch to Cascade; Game Master ledger; inline exception at Game Master discretion |
| G-081 | Resolved | Zoom In player-only; Non-Player Character-only narrated; sequencing enforced |
| G-083 | Resolved | Personal → TTRPG narrative + clock batch; faction order → Co-Movement Card |
| G-085 | Resolved | Player-initiated or mechanical trigger; all else board scale |
| G-091 | Resolved | 1 session minimum per season |
| G-092 | Resolved | Personal phase only; no Strategic phase impact |
| G-093 | Resolved | Threshold = 2× rolled; below threshold = stressed; test 2×−1 variant |
| G-094 | Resolved | 5-step Cascade sequence; Game Master-only; not skippable |
| G-095 | Resolved | Player Character proxy or Non-Player Character artificial intelligence + 1 directive/season |
| G-086 | Resolved | Crisis penalty; take over loyal Non-Player Character or succession; no new characters |
| G-087 | Resolved | Continue as personal character; lose faction dice bonuses |
| G-088 | Resolved | Downtime concurrent with Strategic phase |
| G-089 | Resolved | Board successes generate CP; zoom level irrelevant |
| G-090 | Resolved | Gated by in-scene discovery; exception for immediate-next scene |
