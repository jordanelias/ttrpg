# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_BG_BALANCE_01
phase: SESSION CLOSED
status: COMPLETE

completed_this_session:
  - SIM-BG-01: BG G5/D/J simulation (3-player full turn sequence). PP-169/170. ED-064/065/066. Committed.
  - BAL-BG-01: Win probability balance analysis (all 6 factions). 6 structural/design patches applied.
  - PP-171: Church Deed 4 — 'Control Valorsplatz' -> 'Crown Mandate <= 2 for 2 consecutive seasons'.
  - PP-172: Crown Deed 4 — Add IP < 30 escape clause to Torben Loyalty condition.
  - PP-173: Intel advancement mechanic added (+0.25/successful Intel season).
  - PP-174: Mandate recovery mechanic added (Govern Overwhelming in own capital = +1 Mandate).
  - PP-175: Guild Favour advancement explicitly defined.
  - PP-176: Varfell Deed 1 — Intel 6 -> Intel 5.
  - compilation/v0.14/stage_bg_board_game_mode.md bumped to v0.7 (PP-171/172/176 applied in-place).

post_patch_win_index:
  Crown: MEDIUM (8-12 seasons)
  Church: MEDIUM (10-14 seasons)
  Hafenmark: MEDIUM (6-10 seasons)
  Varfell: MEDIUM (8-12 seasons)
  Guilds: MEDIUM (8-12 seasons)
  Niflhel: MEDIUM (6-10 seasons)

open_params_gaps:
  PG-09: Torben Loyalty Clock decrease mechanics (partial — activation defined, decrease not)
  PG-10: Parliamentary ruling mechanic — what action produces a ruling token?
  PG-11: Intel advancement — now resolved by PP-173 (mark closed)
  PG-12: Hidden information persistence — does revealed Niflhel intel expire?

open_editorials:
  ED-064: Hafenmark Wealth sink (P2)
  ED-065: Novice play time P1 — requires design decision
  ED-066: Mandate recovery — now resolved by PP-174 (mark closed)

dependency_checker_note: "6 false-positive broken refs — all are wildcard glob patterns in propagation_map.md, not actual broken paths. Pre-existing checker limitation."

commits_this_session:
  - 340847431: sim_bg_01 + PP-169/170 + ED-064/065/066
  - 400eb116a: bal_bg_01 + PP-171 through PP-176
  - 18c45619f: PP-171/172/176 in-place to compilation v0.7
  - "[this]": session close

next_session_start:
  priority_1: "Resolve ED-065 (novice play time P1) — user decision required before playtesting."
  priority_2: "Fill PG-10 (Parliamentary ruling mechanic) and PG-12 (hidden info persistence) — params gaps blocking Hafenmark Deed 4 and Niflhel Deed 3 verification."
  priority_3: "Continue simulate board game — Modes C (full scenario) + L (precedent) + M (narrative flowchart). Recommended seed: Church-Crown Mandate contest, TC 40 crossed, S6-8."
  priority_4: "Resolve prior open items: ED-053 (Composure formula), GAP-TTRPG-04 (Belief CP)."
```
