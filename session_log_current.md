# Valoria Session Log — Updated

```yaml
session_id: 2026-04-03T_DEBATE_RESIM_AND_DESIGN
phase: SESSION CLOSED
status: COMPLETE

## WORK COMPLETED
1. SIM-DEBT-01 resolved: debate re-simulation under (Cognition × 2) + History pool (PP-232).
   Modes A + D + J + L. n=10,000 per scenario. Results in tests/sim_d05_debate_resim.md.
2. PP-232 validated — Cognition correctly dominant over Presence in formal debate.
3. Findings: F-SIM-D05-01 (P1 doc fix → PP-233), F-02/03/04 (P2 GM guidance), F-05 (P3 → ED-134).
4. Part 6 body text conflict identified: still says Presence×2 (stale). PP-233 needed next session.
5. Design discussion: derived values explained (Presence modifier, Focus defence, Composure,
   Concentration). Poise confirmed deprecated (ED-027). ED-127 (Composure redesign) still open.
6. User proposed debate redesign elements:
   - Timing (initiative) via Attunement vs Ob 1, most successes goes first
   - Judging the Audience as gated roll (Attunement×2)+History+3
   - Argument Pool = (Cognition×2)+History+3 (adds +3 vs current)
   - Concentration = Focus+History+1 (drops Presence, adds History)
   - Stress/Composure parallel to Wounds/Health (addresses ED-127)
   - Strain formula revision
   - Forced-counter orientation — ABANDONED (breaks multi-party case)
7. Three open design questions identified for Opus session:
   - Presence vs Attunement attribute identity (leadership/command vs reading/intuition)
   - Conflation of debate/negotiation/appeal as separate social combat types
   - Different mechanical conditions per social context (judge, audience, jury, no audience)
8. Routed to Opus: all three questions are editorial-adjacent/philosophy-heavy design tier.

## COMMITS THIS SESSION
- [simulation] SIM-DEBT-01 resolve — debate re-sim under PP-232 pool — SIM-D-05 / ED-134

## OPEN ITEMS ADDED
- ED-134: Orator archetype viability in Formal Debate (P3)
- PP-233: Part 6 body text pool formula fix (pending next session)

## Gate: PASS

next_session_start:
  priority_1: "[OPUS] Presence vs Attunement identity + social combat type differentiation
               (3 questions from session close). Read philosophical_foundations first."
  priority_2: "PP-233: Update Part 6 body text pool formula (Presence→Cognition). Doc fix only."
  priority_3: "ED-127: Composure redesign to mirror Health/Wound structure. User proposed
               Stress=(Focus/2), Composure=(Focus+6)×(MaxStress+1). Needs sim before locking."
  priority_4: "ED-134: Orator archetype decision."
  priority_5: "SIM-DEBT-02: Corroboration in CLASH calibration."
  note: "ED-132 (Step 1 action name), ED-133 (Diverge trigger) still open."
```
