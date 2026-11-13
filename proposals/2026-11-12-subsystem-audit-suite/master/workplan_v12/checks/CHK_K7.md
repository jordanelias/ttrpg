# CHK_K7 — check lane K7 (Sonnet), workplan v12 parts 29 to 32 and their continuations

## Status: WORK ORDER (a check lane's table, one round; resolves nothing at runtime, CLAUDE.md §0.05; deleted with the suite)

**Scope (the brief of `chk_7.txt`, not `V12_STRUCTURE_part3.md` §10.1's grouping, which gives K7 parts 23 to 27):** `workplan_v12_part29.md`, `_part29_cont.md`, `_part30.md`, `_part30_cont.md`, `_part31.md`, `_part31_cont.md`, `_part32.md`, `_part32_cont.md`. Eight batch blocks: B21d-fa-arc, B41-go-port-gate, B11F1-flow-se (29); B20-mb-orders, B25-fi-questioning (30); B27-sc-proceedings (31); B37-happenings, B11F2-flow-in (32). 137 item headings, 137 position rows.

**Rulers used:** `V12_STRUCTURE.md` §5 (via `_part2` §5.2/5.3/6), `V12_STRUCTURE_part3.md` §10.1, `V12_STRUCTURE_part4.md` E-1..E-15 (they win), `workplan_v12_part2.md` §1.3 (the after-lists, HEAD `7257911`) and §11 (the conflicts register). Scripts: scratchpad `k7/parse.py`, `form.py`, `fieldcheck2.py`.

Sections are appended as each check finishes. Findings table at the end of the file (worst first) is written last.

---

## 1. Check 1, forms (script `form.py`, parsed from the files)

| batch | head lines §5.2 in order | INVOCATION exact | `GATE: Batch` = part 2's after-list | positions = items | `.99` position | one boundary row, exact |
|---|---|---|---|---|---|---|
| B21d | yes | yes | yes (2 of 2) | 10 = 10 | B21d.99 "re-pin and close readings" | yes |
| B41 | yes | yes | yes (8 of 8; B17, B20 added by H2 HD-10) | 15 = 15 | B41.99 titled "the close's readings (EQUAL)" | yes |
| B11F1 | yes | yes | yes (1 of 1) | 8 = 8 | B11F1.99 | yes |
| B20 | `SERIAL EDGES` present (carries "(written after the position table, E-11)") | yes | yes (10 of 10) | 23 = 23 | B20.99 | yes |
| B25 | order differs: COST, EST come before SERIAL EDGES, PARALLEL | yes | yes (6 of 6) | 22 = 22 | B25.99 | yes |
| B27 | yes | yes | yes (6 of 6) | 28 = 28 | B27.99 | yes |
| B37 | yes | yes | yes (11 of 11; B29 added by H2 HD-11) | 19 = 19 | B37.99 | yes |
| B11F2 | yes | yes | yes (3 of 3) | 12 = 12 | B11F2.99 "close readings (EQUAL: nothing re-pinned)" | yes |

Every block names its in-flight lane file (`HANDOFF_FA/GO/SE/MB/FI/SC/IN.md`, Open table; B11F1 is SE alone, not a two-lane batch).
