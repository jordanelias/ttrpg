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

## 2. Check 2, fields of §5.3 (script `fieldcheck2.py`; 122 full-form items = BUILD, DESIGN-FIRST, CONTENT and HELD-with-HASH; 12 fields each)

Grade rule used: ABSENT = field line missing; THIN = under 40 characters and not `none`, or "as B21d.07"-style reference, or a COST line with no tier; `.99` positions grade GATE/HASH MOVERS/DEPENDS ON/ADVANCES/GLOSSARY by reference as PRESENT (the form of E-1). NAMES and IDS are conditional and not counted. The 15 POINTER/READING/HELD-without-HASH items (B41.01, B41.12, B11F1.07, B20.18, B20.22, B25.07, B25.08, B25.12, B25.18, B25.21, B37.07, B37.17, B37.18, B11F2.01, B11F2.04) are graded under E-5/§5.3 as pointers/readings (3 to 8 lines, target, gate) and are all present as such.

| field | PRESENT | THIN | ABSENT |
|---|---|---|---|
| SOURCE | 119 | 3 (B21d.08, B21d.09, B27.08) | 0 |
| ADVANCES | 112 | 10 | 0 |
| INSTRUCTION | 121 | 0 | 1 (B27.27, a READING) |
| WHERE | 121 | 0 | 1 (B27.27) |
| TESTS | 120 | 1 (B27.24) | 1 (B27.27) |
| FALSIFIER and CONTROL | 119 | 2 (B21d.08, B21d.09: "as B21d.07") | 1 (B27.27) |
| GATE | 120 | 2 (B21d.08, B21d.09: "as B21d.07.") | 0 |
| HASH MOVERS | 120 | 1 (B20.06 "as B20.05") | 1 (B27.27) |
| DEPENDS ON | 113 | 8 | 1 (B27.27) |
| GLOSSARY | 105 | 16 (a row name and a step number only) | 1 (B27.27) |
| COST and TIER | 122 | 0 | 0 |
| LANDS IT | 121 | 0 | 1 (B27.27) |

B27.27 is a READING that carries a position-table row, an item heading with HASH EQUAL and four fields (SOURCE, ADVANCES, GATE, COST); the other READING items (B20.22, B25.07, B25.21, B37.17, B37.18, B41.12) carry no fields at all, and all READING items have no COST/TIER line, so check 8 grades them "reading, tier not stated" (B27.27 alone says `haiku`; B20.22 says `haiku` inline).

Per batch, PRESENT/THIN/ABSENT cells of the 12 fields over the full-form items: B21d 108/12/0 (10 items); B41 155/1/0 (13); B11F1 81/3/0 (7 incl. B11F1.99); B20 247/5/0 (21); B25 197/7/0 (18); B27 315/13/8 (27); B37 190/2/0 (16); B11F2 120/0/0 (10).

THIN items an agent cannot run from the item alone (check 10) are listed in §9.
