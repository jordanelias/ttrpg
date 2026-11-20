# W2 · import edges between areas (M1)

## Status: WORK FILE (a script-built extract for `master/HOLISTIC_AUDIT.md`; reference; deleted when the stage closes)

## Read at: `4dc8a7b` (working tree, 2026-11-12). Built by a throwaway `ast` or seeded-run probe in the session scratchpad; nothing here is a judgment.

Method: `ast` over every tracked `*.py` under `engine/`, `modules/`, `systems/`, `tools/`; one edge per (importing file, repo module imported), relative imports resolved; `lazy` counts imports inside a function body. Blind spot: seams resolved by string (`W3`), `sys.path` seams, shared data.

## M1 areas (git ls-files, *.py)

| area | files | lines |
|---|---|---|
| engine.<top> | 1 | 10 |
| engine.dice_engine | 3 | 796 |
| engine.reference | 5 | 1387 |
| engine.season.<top> | 4 | 1357 |
| engine.season.data | 13 | 8530 |
| engine.season.decision | 6 | 3159 |
| engine.season.harness | 30 | 16041 |
| engine.season.loop | 20 | 9673 |
| engine.season.manifest | 4 | 961 |
| engine.season.queries | 6 | 8040 |
| engine.season.seam | 11 | 2433 |
| engine.season.state | 10 | 5742 |
| engine.season.tests | 166 | 71169 |
| engine.substrate | 8 | 581 |
| engine.tests | 6 | 1301 |
| modules.<top> | 1 | 5 |
| modules.combat | 15 | 6009 |
| modules.fieldwork | 2 | 36 |
| modules.mass_battle | 29 | 11624 |
| modules.settlements | 8 | 371 |
| modules.social_contest | 2 | 168 |
| systems.<top> | 1 | 6 |
| systems.characters | 3 | 293 |
| systems.combat | 15 | 2919 |
| systems.fieldwork | 3 | 406 |
| systems.mass_battle | 14 | 3390 |
| systems.overview | 3 | 113 |
| systems.settlements | 1 | 10 |
| systems.social_contest | 18 | 6693 |
| systems.threadwork | 9 | 1955 |
| tools | 54 | 15016 |

## M1 cross-area import edges (one per importing file x imported repo module; `lazy` = import inside a def)

| from | to | edges | lazy |
|---|---|---|---|
| engine.season.tests | engine.season.data | 381 | 35 |
| engine.season.tests | engine.season.state | 248 | 14 |
| engine.season.tests | engine.season.harness | 239 | 34 |
| engine.season.tests | engine.season.loop | 181 | 17 |
| engine.season.tests | engine.season.queries | 144 | 7 |
| engine.season.tests | engine.season.decision | 114 | 12 |
| engine.season.tests | engine.season.<top> | 96 | 9 |
| engine.season.tests | engine.season.seam | 69 | 11 |
| engine.season.harness | engine.season.data | 67 | 5 |
| engine.season.loop | engine.season.state | 53 | 0 |
| engine.season.loop | engine.season.data | 44 | 0 |
| systems.mass_battle | modules.mass_battle | 38 | 10 |
| engine.season.harness | engine.season.state | 36 | 0 |
| engine.season.loop | engine.season.queries | 29 | 0 |
| engine.season.loop | engine.season.<top> | 26 | 0 |
| engine.season.tests | engine.substrate | 26 | 1 |
| engine.season.harness | engine.season.queries | 24 | 1 |
| engine.season.harness | engine.season.loop | 23 | 3 |
| engine.season.tests | engine.season.manifest | 18 | 4 |
| engine.season.queries | engine.season.data | 15 | 0 |
| engine.season.harness | engine.season.<top> | 13 | 1 |
| engine.season.harness | engine.season.decision | 11 | 0 |
| engine.season.state | engine.season.data | 11 | 0 |
| engine.season.queries | engine.season.state | 10 | 0 |
| engine.season.data | engine.season.<top> | 9 | 0 |
| engine.season.seam | engine.season.data | 9 | 0 |
| engine.season.seam | engine.season.queries | 9 | 0 |
| engine.season.tests | engine.dice_engine | 9 | 2 |
| engine.season.decision | engine.season.data | 8 | 0 |
| engine.season.seam | engine.season.<top> | 8 | 0 |
| engine.season.seam | engine.season.manifest | 8 | 0 |
| systems.social_contest | engine.dice_engine | 8 | 1 |
| engine.season.data | engine.substrate | 7 | 1 |
| engine.season.decision | engine.season.<top> | 7 | 0 |
| engine.season.state | engine.season.<top> | 7 | 0 |
| modules.settlements | engine.season.queries | 7 | 0 |
| engine.season.loop | engine.season.decision | 6 | 0 |
| engine.season.queries | engine.season.<top> | 6 | 0 |
| engine.season.seam | engine.season.state | 6 | 0 |
| engine.tests | engine.dice_engine | 6 | 1 |
| engine.reference | engine.season.data | 5 | 0 |
| engine.season.decision | engine.season.state | 5 | 0 |
| engine.season.<top> | engine.season.state | 4 | 0 |
| engine.season.harness | engine.substrate | 4 | 0 |
| engine.season.loop | engine.season.seam | 4 | 0 |
| engine.season.loop | engine.season.manifest | 4 | 1 |
| engine.season.seam | engine.substrate | 4 | 1 |
| systems.social_contest | engine.substrate | 4 | 0 |
| tools | engine.season.harness | 4 | 4 |
| engine.reference | engine.season.decision | 3 | 0 |
| engine.reference | engine.season.queries | 3 | 0 |
| engine.reference | engine.season.state | 3 | 0 |
| engine.season.decision | engine.season.queries | 3 | 0 |
| engine.season.<top> | engine.season.data | 3 | 0 |
| engine.season.<top> | engine.season.queries | 3 | 0 |
| engine.season.harness | engine.season.seam | 3 | 1 |
| engine.season.manifest | engine.season.data | 3 | 1 |
| engine.season.queries | engine.substrate | 3 | 0 |
| engine.season.seam | engine.dice_engine | 3 | 0 |
| systems.threadwork | engine.dice_engine | 3 | 0 |
| engine.reference | engine.season.<top> | 2 | 0 |
| engine.reference | engine.season.seam | 2 | 0 |
| engine.reference | engine.season.harness | 2 | 0 |
| engine.season.harness | engine.dice_engine | 2 | 0 |
| engine.season.loop | engine.substrate | 2 | 0 |
| engine.season.manifest | engine.season.<top> | 2 | 0 |
| engine.season.manifest | engine.substrate | 2 | 2 |
| engine.season.seam | engine.season.loop | 2 | 0 |
| modules.combat | engine.dice_engine | 2 | 0 |
| tools | modules.mass_battle | 2 | 2 |
| engine.reference | engine.season.loop | 1 | 0 |
| engine.season.data | engine.dice_engine | 1 | 0 |
| engine.season.decision | engine.substrate | 1 | 0 |
| engine.season.seam | engine.season.decision | 1 | 0 |
| engine.season.state | engine.season.manifest | 1 | 1 |
| engine.tests | systems.fieldwork | 1 | 0 |
| engine.tests | systems.characters | 1 | 1 |
| engine.tests | systems.social_contest | 1 | 0 |
| engine.tests | systems.threadwork | 1 | 0 |
| modules.combat | engine.season.queries | 1 | 0 |
| modules.combat | engine.substrate | 1 | 0 |
| modules.fieldwork | engine.season.queries | 1 | 0 |
| modules.social_contest | engine.dice_engine | 1 | 0 |
| modules.social_contest | engine.season.queries | 1 | 0 |
| systems.characters | engine.substrate | 1 | 0 |
| systems.fieldwork | engine.dice_engine | 1 | 0 |
| systems.fieldwork | systems.characters | 1 | 1 |
| systems.fieldwork | systems.threadwork | 1 | 1 |
| tools | engine.substrate | 1 | 1 |

total file-level edges 2621; crossing an area 2146

## area pairs that import each other

- engine.season.<top> <-> engine.season.data  (3 / 9)
- engine.season.<top> <-> engine.season.queries  (3 / 6)
- engine.season.<top> <-> engine.season.state  (4 / 7)
- engine.season.loop <-> engine.season.seam  (4 / 2)
