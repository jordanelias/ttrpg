# Valoria Session Log - Updated

```yaml
session_id: 2026-04-04T_CROSS_MODE_SIM
phase: SESSION CLOSED
status: COMPLETE

## WORK COMPLETED
1. SIM-X-26: TTRPG Personal Combat non-optimal actors. Davan fixed 8/4 vs Solmund Momentum hoarder. 4 rounds, 0 hits by Davan, 2 Momentum wasted by Solmund. 5 findings, 2 gaps.
2. SIM-X-27: Hybrid Domain Season. Church delays TC, Crown 6% probability action, PC indirect. 5 findings, 2 gaps.
3. SIM-X-28: BG multi-faction. Coalition pact fails, Crown self-inflicted crisis, Varfell timing error. 8 findings, 2 gaps.

## GAPS FLAGGED
- GAP-SIM-X26-01: Stamina exhaustion threshold (P2)
- GAP-SIM-X26-02: Momentum between-scenes carry (P2)
- GAP-SIM-X27-01: RS natural decay rate (P1 - carried SIM-H-01)
- GAP-SIM-X27-02: Presence vs Charisma (P2)
- GAP-SIM-X28-01: BG Wealth diminishing returns above 5 (P2)
- GAP-SIM-X28-02: BG coalition pact partial fulfilment (P2)

## CARRIED FORWARD
- ED-139, ED-140, ED-142: P1-BLOCKERs unchanged
- ED-143 to ED-146: PC simulation constructs, user approval required
- AUD-P1-15, AUD-P1-16: unchanged
- SIM-DEBT-03/04: deferred

## KEY DESIGN SIGNALS
- TN differential > pool size in combat
- Momentum hoarding dominated; mechanism needed
- Failed Domain Actions need blowback
- Coalition salience problem in BG
- RS decay rate P1 - blocks trajectory modelling all modes

next_session_start:
  priority: RS decay rate definition (P1), ED-143-146 PC approval
  read_first: [tests/sim_x26_x27_x28_cross_mode.md, session_log_current.md]
```
