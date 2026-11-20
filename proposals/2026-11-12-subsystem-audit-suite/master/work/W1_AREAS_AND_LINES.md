# W1 · areas, lines and what the lines are

## Status: WORK FILE (a script-built extract for `master/HOLISTIC_AUDIT.md`; reference; deleted when the stage closes)

## Read at: `4dc8a7b` (working tree, 2026-11-12). Built by a throwaway `ast` or seeded-run probe in the session scratchpad; nothing here is a judgment.

Method: `git ls-files engine modules tools`, `*.py`; a line is `docstring` if it lies inside the first-statement string of a module, class or function, `comment` if it is a whole-line `#` comment, `blank` if empty, else `code`. Areas as `valoria-simplify` M1 defines them.

| area | files | code | comment | docstring | blank | prose share of non-blank |
|---|---|---|---|---|---|---|
| engine.<top> | 1 | 0 | 0 | 10 | 1 | 100% |
| engine.dice_engine | 3 | 216 | 132 | 312 | 139 | 67% |
| engine.reference | 5 | 824 | 142 | 305 | 121 | 35% |
| engine.season.<top> | 4 | 341 | 179 | 641 | 200 | 71% |
| engine.season.data | 13 | 3687 | 2351 | 1609 | 896 | 52% |
| engine.season.decision | 6 | 1015 | 503 | 1272 | 375 | 64% |
| engine.season.harness | 30 | 8795 | 2413 | 3016 | 1847 | 38% |
| engine.season.loop | 20 | 3081 | 2604 | 3110 | 898 | 65% |
| engine.season.manifest | 4 | 432 | 146 | 267 | 120 | 49% |
| engine.season.queries | 6 | 2801 | 744 | 3450 | 1051 | 60% |
| engine.season.seam | 11 | 835 | 303 | 979 | 327 | 61% |
| engine.season.state | 10 | 1790 | 1310 | 2018 | 634 | 65% |
| engine.season.tests | 166 | 37230 | 12468 | 11891 | 9746 | 40% |
| engine.substrate | 8 | 160 | 110 | 205 | 114 | 66% |
| engine.tests | 6 | 674 | 136 | 273 | 224 | 38% |
| modules.<top> | 1 | 0 | 0 | 5 | 1 | 100% |
| modules.combat | 15 | 2560 | 1563 | 1517 | 384 | 55% |
| modules.fieldwork | 2 | 8 | 0 | 22 | 8 | 73% |
| modules.mass_battle | 29 | 5194 | 3259 | 2243 | 957 | 51% |
| modules.settlements | 8 | 152 | 0 | 170 | 57 | 53% |
| modules.social_contest | 2 | 36 | 0 | 112 | 22 | 76% |
| tools | 54 | 7575 | 2271 | 3113 | 2111 | 42% |

non-test total: code 39502 comment 18030 docstring 24376 blank 10263; prose share 52%

| file (non-test, top 40 by prose lines) | lines | code | comment | doc |
|---|---|---|---|---|
| engine/season/queries/world_q.py | 5557 | 1989 | 629 | 2245 |
| modules/mass_battle/hierarchy/units.py | 3084 | 1486 | 820 | 606 |
| engine/season/state/gate.py | 1933 | 503 | 428 | 783 |
| modules/mass_battle/orchestration.py | 2498 | 1119 | 944 | 265 |
| engine/season/decision/options.py | 1828 | 562 | 307 | 753 |
| engine/season/harness/populated.py | 2163 | 978 | 650 | 383 |
| engine/season/data/verbs.py | 2187 | 997 | 558 | 415 |
| engine/season/state/world.py | 1744 | 660 | 404 | 537 |
| engine/season/data/fixtures.py | 1170 | 219 | 861 | 62 |
| modules/combat/combat_systems.py | 1473 | 485 | 307 | 581 |
| engine/season/loop/effects_information.py | 1311 | 397 | 40 | 710 |
| engine/season/loop/resolve.py | 1299 | 462 | 497 | 251 |
| engine/season/state/carriers.py | 1254 | 391 | 393 | 340 |
| engine/season/harness/probes.py | 2956 | 1925 | 539 | 178 |
| engine/season/epistemic.py | 1084 | 241 | 176 | 532 |
| engine/season/queries/person_q.py | 1443 | 535 | 78 | 627 |
| engine/season/loop/witness.py | 1021 | 309 | 527 | 141 |
| engine/season/data/rosters.py | 1591 | 820 | 394 | 229 |
| modules/combat/weapon_physics.py | 973 | 305 | 218 | 361 |
| engine/season/harness/corpus_run.py | 1253 | 563 | 270 | 296 |
| engine/season/loop/matter.py | 904 | 316 | 432 | 106 |
| engine/season/data/requires.py | 1120 | 477 | 238 | 263 |
| modules/combat/core.py | 703 | 184 | 326 | 169 |
| tools/ci_common.py | 762 | 185 | 221 | 256 |
| engine/season/loop/predicates.py | 712 | 199 | 145 | 288 |
| engine/season/decision/choose.py | 801 | 281 | 118 | 312 |
| modules/mass_battle/config.py | 627 | 190 | 421 | 3 |
| engine/season/loop/driver.py | 621 | 170 | 310 | 101 |
| engine/season/loop/deliberate.py | 586 | 142 | 189 | 209 |
| engine/season/loop/effects_combat.py | 848 | 364 | 148 | 250 |
| modules/mass_battle/massbattle.py | 598 | 183 | 86 | 252 |
| engine/season/queries/inputs.py | 605 | 186 | 31 | 303 |
| engine/season/loop/effects_governance.py | 550 | 157 | 69 | 251 |
| tools/ci_sim_fabrication_check.py | 618 | 244 | 134 | 173 |
| engine/season/manifest/registry.py | 717 | 342 | 134 | 161 |
| engine/season/harness/register.py | 764 | 392 | 135 | 156 |
| engine/season/seam/wrappers/sigma.py | 556 | 197 | 39 | 249 |
| engine/season/harness/aperture.py | 1124 | 718 | 42 | 230 |
| engine/dice_engine/sigma_leverage.py | 469 | 116 | 60 | 205 |
| tools/verify_handoff_split.py | 662 | 321 | 137 | 128 |
