# RECOUNT — part 2's figures re-run after repair lane V1

## Status: WORK NOTE (resolves nothing; deleted when v12 is adopted)

Scripts: `parse_parts.py`, `summ.py`, `graph.py`, `hashinfo.py`, `t1.py`, `totals.py` of `workplan_v12_part2_appendix.md`, unedited, run in `scratchpad/recount/` over parts 3 to 44.

| figure | old | new |
|---|---|---|
| positions, total | 1,455 | 1,455 |
| BUILD | 1,194 | **1,193** |
| HELD | 24 | **25** |
| POINTER / READING / BLOCKED / CONTENT / DESIGN-FIRST | 79 / 35 / 57 / 33 / 33 | same |
| old normaliser (any word) BUILD / HELD | 1,189 / 27 | **1,188 / 28** |
| B03 states | B61 P1 R1 H1 BL1 | **B60 P1 R1 H2 BL1** |
| every other batch's count and states | | same |
| movers (behaviour / encoding / conditional), mover and EQUAL batches | 442 / 21 / 6, 49 / 12 | same |
| serial hours, critical path, makespan | 748.5 / 390.5 / 425.3 h | same (hours depend on position counts, not states) |
| edges, waves, steps, chains | 526, 25, 25, 90 | same |

V1's other changes (B02, B08, B98, B99) added no position rows; B41.03 step 4 is a step, not a position.
