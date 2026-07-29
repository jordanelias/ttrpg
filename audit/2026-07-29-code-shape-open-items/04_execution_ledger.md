# Execution ledger — code-shape open-items program (ED-IN-0091)

## Role

This file is the program's **single STATUS surface**. `00_open_items_register.md`,
`01_orchestration_plan_v1.md`, and `02_disposition_map.md` are immutable snapshots taken at
program start (plus the 2026-07-29 adversarial reconciliation baked into the disposition map) —
**they do not change as waves execute.** Every wave (W0–W5) appends its rows here, and W5's
capstone additionally completes the diff against `02_disposition_map.md` (closing the
created-by-W5 / appended-by-every-wave tension the orchestration plan otherwise leaves open —
flagged explicitly in the W0b PR body). If a register/plan/map claim turns out stale or wrong
during execution, the correction lands as a row here, not as an edit to those files.

## Column format

`OI/item · wave · PR · ED · falsifier artifact · outcome`

## Rows

| OI/item | wave | PR | ED | falsifier artifact | outcome |
|---|---|---|---|---|---|
| W0a — 7-lane pre-allocation + `id_reservations.yaml` file freeze (no per-item OI; reservation only) | W0a | #256 | (reservation only, no ED filed) | `references/id_reservations.yaml` lane lines (IN 0092–0111, MB 0046–0060, PC 0041–0055, WR 0009–0012, FA 0036–0039, SE 0049–0052, SC 0017–0020; file frozen until W5) | done |
| §5 Jordan docket authored, HELD FOR JORDAN (rulings not yet made) | W0b | (this PR) | ED-IN-0092 | `05_jordan_docket_v1.md` | open — awaiting Jordan |
| OI-55 — orphan-detector integrity: `__init__` relative-import misresolution, CLI-entry-point noise, `vector_audit.py` known-answer coverage, re-scoped at W0b | W0b | (this PR) | ED-IN-0092 | `skills/valoria-vector-audit/scripts/structure_audit.py` diff + `tests/valoria/test_structure_audit.py` + `tests/valoria/test_vector_audit.py` (new known-answer cases) | landed |
| G12 correction — the `__init__` misresolution half of OI-55 was already fixed pre-W0b; re-verified not re-done | W0b | (this PR) | ED-IN-0092 | `structure_audit.py` lines ~271–278 (existing fix comment), confirmed by re-read, no duplicate change made | verified stale claim, no-op |
| G12 correction — the "no known-answer coverage beyond one total-pin" claim was already stale pre-W0b; re-verified not re-done | W0b | (this PR) | ED-IN-0092 | `tests/valoria/test_vector_audit.py` (pre-existing coverage beyond a single total-pin case), confirmed by re-read, no duplicate change made | verified stale claim, no-op |
| execution ledger created (this file) | W0b | (this PR) | ED-IN-0092 | this file's existence + first two waves' rows | done |
| critic relay (W0b) — 3 lanes upheld, 4 fixable defects folded in (docket OI-41 row, 2 stale citations, cli_entries caption + conservation test) | W0b | (this PR) | ED-IN-0092 | the critic report in the W0b PR body + this file's rows | done |
| duplication logged, not chased (§0.1 #5): __main__-guard predicate now defined in structure_audit.py (AST) AND build_apparatus_registry.py:116 (regex, pre-existing, behaviorally different) — single-owner consolidation routed to Wave 4 item 5 (which owns build_apparatus_registry inconsistencies, OI-15) | W0b→W4 | (this PR) | ED-IN-0092 | Wave 4's dedup mutation check when consolidated | open — routed to W4 |
| stale surface found by critic (OI-53 class): build_apparatus_registry.py:232-234 globs the deleted designs/audit tree, silently degrading its orphan signal — routed to Wave 4 item 3's re-verify list | W0b→W4 | (this PR) | ED-IN-0092 | W4's extended dead-root guard test | open — routed to W4 |
