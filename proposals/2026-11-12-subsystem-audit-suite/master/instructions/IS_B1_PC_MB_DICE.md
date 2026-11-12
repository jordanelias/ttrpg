# Instruction suite, lane IS-B1 — personal combat (PC), mass battle (MB) and the dice (DICE) as standalone playable games

## Status: PROPOSED (stage 4 of `STAGES.md`; batch-shaped instructions for workplan v12; nothing here is applied; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: `b07fc1c` (working tree, 2026-11-12). Producer: Fable, lane IS-B1 of `master/INSTRUCTION_SUITE_ORDER.md`. One round; no second wave.

Parts: this file (the frame, PC) · `IS_B1_PC_MB_DICE_part2.md` (MB, DICE, the tables v12 takes, what was not checked).

## 0. What this file is, and how v12 uses it

It is the instruction set for three subjects, written as items a `/methodology-execute` batch can run. It does **not** restate the coding instructions the proposals already carry (`proposals/03_PC_*`, `04_MB_*`, `10_DICE_*`, `16_PESSIMIST_{PC,MB,DICE}_*`, `26_MASS_BATTLE_*`, `27_MB_*`, `29_DICE_*`, `U5b_*`, `U5a_DICE_owed_edits`). For each subject it states:

1. **the standalone-playable test** (`INSTRUCTION_SUITE_ORDER.md`, third paragraph): the entry, the scenario or seed, the player-facing surface, the stub contract for the neighbours, the ending kinds, the execution artifact that proves each, and the integrated check (the same module in the season loop);
2. **the batch sequence** that gets the subject to that test, by the handles of `unified/U3_DEPENDENCY_ORDER.md` §2.1, with what each batch contributes to the test and nothing else;
3. **the items the proposals do not carry**: the gaps of `unified/U4_TRACEABILITY.md` §6 that fall in these three subjects, the decidable missing parts of the INCOMPLETE proposals (`unified/U4_DOCUMENT_STATUS.md` §3.4), the holistic audit's findings that bear on them (`master/HOLISTIC_AUDIT*.md`; items `CI-01..CI-11` of `master/CODEBASE_IMPROVEMENT_PROPOSAL*.md`), and the scenario, stub and reading work no proposal names.

**The item form** is the order's: `Item: <handle>` · subject advanced · INSTRUCTION · WHERE · FALSIFIER and control · GATE · hash movers · depends on (EXISTS-IN-TREE / PROPOSED / MISSING) · lane tag · batch it joins · cost class and model tier · what lands it. Handles are `IS-PC-nn`, `IS-MB-nn`, `IS-DICE-nn`. An item that only points at a proposal says **POINTER** and adds what is missing. An item whose missing part cannot be decided from the repository says **BLOCKED**, with the reason and its owner. Every claim about the tree cites the path and line opened at this read, or the probe run (§P2-5, the evidence log in part 2); a claim taken from a suite ledger and not re-opened is marked `[LEDGER: file]`; an inference is marked `[ASSUMPTION: … — basis]`.

**Words.** `unified/U1_GLOSSARY.md`; for the army and the field, `unified/MB_LEXICON.md` (A-95). A tree identifier that fails the ordinary-English test is given once in backticks and the plain word is used after (`STAGES.md`, "Terms mean what ordinary English says").

**What the three subjects are, in one sentence each.** PC is the fight between named persons (`modules/combat/`, reached through `engine/substrate/pc_engine.py` and `engine/season/seam/wrappers/combat.py`). MB is the field: two armies of unit rows resolved on cells (`modules/mass_battle/`, reached through `engine/season/seam/wrappers/mass_battle.py`). DICE is the one roll every contest draws (`engine/dice_engine/`), a substrate and not a module: its standalone test is read differently (part 2, §P2-2.0) and the difference is listed for Jordan (`IS_FOR_JORDAN.md`, J-IS-B1-01).

