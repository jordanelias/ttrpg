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

**What the three subjects are, in one sentence each.** PC is the fight between named persons (`modules/combat/`, reached through `engine/substrate/pc_engine.py` and `engine/season/seam/wrappers/combat.py`). MB is the field: two armies of unit rows resolved on cells (`modules/mass_battle/`, reached through `engine/season/seam/wrappers/mass_battle.py`). DICE is the one roll every contest draws (`engine/dice_engine/`), a substrate and not a module: its standalone test is read as *one roll played as a decision* (part 2, §P2-2.0), an answer taken by the five-step ladder at step 5 and reversible on Jordan's word. This lane lists nothing in `IS_FOR_JORDAN.md`: no item here overwrites canon, a `(RULED)` item or a ratified Layer 1 row.

**Words after A-98** (`unified/DECISIONS_ANSWERED.md:134`). *Attribute* (never aptitude or talent); *skill* for a learned rank and for the one capability kind; *skill score* for a person's number in a skill; *martial skill* for a person's skill at arms; *prowess* only for a unit's quality (A-59); *training* only for the act of learning; *derived score* for health, wound count, resolve and their kin; *choice score* for the chooser's valuation. Tree identifiers keep their names in backticks (`capability`, `faculties`, `scores`). Proposals quoted here may still carry the retired words until the sweep lane reaches them; this file does not.

**The readings this file rests on** (probes run at this read, `PYTHONHASHSEED=0`; full log in part 2, §P2-5):

| id | probe | reading |
|---|---|---|
| P-1 | `composition.require("combat.fight")` on a hand-built `PersonalCombatInput` (ends 4 and 4, default kit), seeds 0–199 | under `death` terms the first party wins 99, loses 99, undecided 2; `blood` 103 / 97 / 0; `yield` 98 / 101 / 1. A decider that withdraws at his first wound: 67 / 32 / 101. A decider that always answers `engage` equals no decider, cell for cell. So the module entry already runs alone, ends three ways, and a choice moves the ending |
| P-2 | `composition.require("mass_battle.resolve_field")` on a hand-built `MassBattleInput`, 40 against 40, seeds 0–99 | at the shipped `field_troops_per_weight` 1 (`engine/season/data/fixtures.py:789`): `Failure` 100 of 100, the attacker never wins. At 25: `Success` 37, `Failure` 63; 80 against 40: 50 / 49 and one `Partial`; 40 against 80: 21 / 79. The return has four keys (`attacker_size_pct`, `attacker_wins`, `defender_size_pct`, `degree`): no drawn end state, no report |
| P-3 | the same field at 25, one side given a `FieldOrder(role, retreat_at)`, 15 roles × 3 fall-back points × seeds 0–99 | the fall-back point changed the result in 1 of 1,500 role-and-seed cells; seven roles (`Anvil`, `Screen`, `Pursue`, `Feint`, `VolleyLine`, `Support`, `Reserve`) change nothing against no order at any seed; four (`Skirmish`, `Shock`, `Harass`, `Kite`) change every seed. Control: 33 distinct results over the 100 seeds with no order. One matchup, one size: a lead, not a balance claim (CLAUDE.md §0.1 pt 4) |
| P-4 | an `ast` scan of `tests/valoria/test_combat*.py` for a `for` loop all of whose assertions sit under a condition | four test functions (nine loop nodes); listed at IS-PC-04 |

