# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_BG_SIM_01
phase: SESSION CLOSED
status: COMPLETE

completed_this_session:
  - SIM-BG-01: BG mode simulation Modes G5 + D + J (3-player full turn sequence, edge cases, cognitive load). 8 findings. Output: tests/sim_bg_01.md.
  - PP-169: params_board_game — phase structure, order priority, unit Muster Ob table, faction capitals, Order token rules extracted from compilation B4/B6/B3.
  - PP-170: params_board_game — Parliamentary Manoeuvre Partial=no effect (explicit ruling); Failure=Mandate -1.
  - ED-064: Hafenmark Wealth sink undefined (P2).
  - ED-065: Novice planning time P1 (~12 min/player). Requires design decision before playtesting.
  - ED-066: Mandate recovery mechanism undefined in BG spec (P2).

open_editorials_requiring_user_input:
  - ED-064: Hafenmark Wealth sink — design sink mechanic or confirm ceiling is intended.
  - ED-065 (P1): Novice play time — confirm simplification approach: (a) preset menus; (b) fewer tokens; (c) action cards (links ED-001).
  - ED-066: Mandate recovery — confirm or design restoration mechanic.
  - ED-001 (existing P1 blocker): Card-Hand system — still unresolved; blocking compilation sync.

remaining_open_P1s_from_sim:
  - F-03/ED-065: Novice planning time. Design-level issue.
  - F-06: TC starting value conflict in compilation (stale). Compilation sync blocked by ED-001.

commits_this_session:
  - 340847431280b0b81de8f4b56c5e5a60fc08b80b: sim_bg_01 + PP-169/170 + ED-064/065/066

next_session_start:
  priority_1: "Resolve ED-065 (novice play time P1) — user decision on simplification approach."
  priority_2: "Resolve ED-064 (Hafenmark Wealth sink) and ED-066 (Mandate recovery)."
  priority_3: "Continue simulate board game — Modes C (full scenario) + L (precedent) + M (narrative flowchart). Recommended seed: Church-Hafenmark tension, TC approaching 40, S6-8."
  priority_4: "Resolve prior-session items: ED-053 (Composure), GAP-TTRPG-04 (Belief CP)."
```
