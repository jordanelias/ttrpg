# Workplan v12 — part 10: the head of batch B07-task-draw (its block is `_part10_cont2`)

## Status: RATIFIED, ED-IN-0362 (a body part of workplan v12, drafted under `master/workplan_v12/`; adopted 2026-11-15 as the one active plan; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Written against: the working tree at `aa31fd2` (branch `ccr-62958c70-0kjhsw`), read 2026-11-12; author lane A10 of `V12_STRUCTURE_part2.md` §4.2. Every item is written against the tree as the batches before it will leave it (B00 to B05, B13); where a symbol named does not exist at `aa31fd2`, the item says which batch makes it, and a line number into a file B03a edits is dropped for its symbol (`V12_STRUCTURE_part2.md` §5.4).

**What this part holds.** The head, words, paths and realm hash reading of author lane A10's part, which the block of `B07-task-draw` (IN, S9: an uncontested verb graded by a draw; `valoria_master_workplan_v12_part10_cont2.md`) reads as its own. No batch block is in this file. A batch is one block with one close, in the form of `V12_STRUCTURE_part2.md` §5.2 and §5.3 as amended by `V12_STRUCTURE_part4.md` (E-1 to E-15). A part cites another part's batch or item by handle only.

**Words.** `unified/U1_GLOSSARY.md`; a person's numbers are an attribute, a skill and its skill score, a martial skill, a derived score (A-98); armies use the lexicon's words (army, unit, army formation, unit formation; no size word); a *lap* is one pass of the season's scene budget, a *round* one engagement of a fight (A-101); the riposte keeps its code id `finalblow_riposte`. Every item here lands after B04, so source text that says `round` for the season's pass is copied with a `NAMES:` line (`Claim.round` → `Claim.lap`, `SeasonDriver.round` → `.lap`, `scenes_per_round` → `scenes_per_lap`); B14 lands before B16, so the fight's words in code are still `max_bouts`, `turn_start`, `engagement_end`, `CombatTurnView`, `TURN_CHOICES` (PCR-3 renames them in B16) and an item here uses the tree's identifier with the plain word beside it.

**Paths.** A bare path is under `proposals/2026-11-12-subsystem-audit-suite/`; `U3` is `unified/U3_DEPENDENCY_ORDER.md`; `the intake` is `master/eval/V12_INTAKE.md`; `IS-A` is `master/instructions/IS_A_NINE.md` and `_part2`; `IS-B1` is `master/instructions/IS_B1_PC_MB_DICE.md`. A path under `engine/`, `modules/`, `tools/`, `references/`, `registers/`, `tests/`, `systems/` is the repository's. A proposal named without a path is under the suite's `proposals/`.

**The realm hash reading** used by every item of this part: `build_realm(s)` (`engine/season/boot/realm.py`, B03c), one season through the shipped chooser, then `World.content_hash()`, under `PYTHONHASHSEED=0` — the one-season realm hash B02's golden owner `engine/season/tests/_realm_goldens.py` pins. Per item the seed-0 reading (E-2); at the batch's `.99` seeds 0, 1, 2. A before-reading is the previous item's or close's after-reading, quoted `reading @<sha>`, never re-taken.

---
