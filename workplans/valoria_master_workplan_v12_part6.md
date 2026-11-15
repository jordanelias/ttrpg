# Workplan v12 — part 6: batches B03a-prose, B13-pc-package, B16M-mb-engine-words

## Status: RATIFIED, ED-IN-0362 (a body part of workplan v12, drafted under `master/workplan_v12/`; adopted 2026-11-15 as the one active plan; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Written against: the working tree at `aa31fd2` (branch `ccr-62958c70-0kjhsw`), read 2026-11-12; author lane A06 of `master/workplan_v12/V12_STRUCTURE_part2.md` §4.2, with `V12_STRUCTURE_part4.md`'s errata applied (E-1: every batch ends with a `.99` re-pin-and-readings position). Every item is written against the tree as B00 to B03 will leave it; where a symbol is named that does not exist at `aa31fd2`, the item says which batch makes it.

**What this part holds.** The head of parts 6 and 6_cont: the Status, the readings every gate of both uses, the words and the paths; the batches themselves are in `valoria_master_workplan_v12_part6_cont.md`: `B03a-prose` (IN, S5: annotations out of the registries and history out of the source, CI-01, CI-02), `B13-pc-package` (PC, S6: personal combat as a package, CI-09, D-09), `B16M-mb-engine-words` (MB, S6: the engine's army names, the lexicon's L2, D-07), in execution order (a topological order of `V12_STRUCTURE.md` §2.1). `B16L-mb-words` (S4, the lexicon's L1) closed and its block left this part. **Every one is hash EQUAL** (`V12_STRUCTURE.md` §2.2): each ends in a `.99` position that records the EQUAL readings and re-pins nothing, and each states the stop rule a moved hash triggers. A part cites another part's batch or item by handle only; the head's index maps a handle to its file.

**Words.** `unified/U1_GLOSSARY.md`. A person's numbers are an attribute, a skill and its skill score, a derived score (A-98); armies are an army, a unit, an army formation, a unit formation, with no size word (A-99, the lexicon); a *lap* is one pass of the season's scene budget and a *round* is one engagement of a fight (A-101); the riposte keeps its code id `finalblow_riposte`. No item in this part lands after `PCR-4` (B04), so source text that says `round` for the season's pass keeps the tree's word, and none says it. Copied source text that uses a word a later ruling retired is corrected and the correction said (`V12_STRUCTURE_part2.md` §5.11): the lexicon's "trooper" becomes "man" in the docstrings L1-1 touches (the lexicon's own instruction).

**Paths.** As `V12_STRUCTURE.md` states: a bare path is under `proposals/2026-11-12-subsystem-audit-suite/`; `CIP` is `master/CODEBASE_IMPROVEMENT_PROPOSAL.md` and `_part2`; `the lexicon` is `unified/MB_LEXICON_part3.md` (with `MB_LEXICON.md` and `_part2` for its rows); `the intake` is `master/eval/V12_INTAKE.md`; `U3` is `unified/U3_DEPENDENCY_ORDER.md`. A path under `engine/`, `modules/`, `systems/`, `tools/`, `references/`, `registers/`, `tests/`, `.github/` is the repository's.

**Two readings every gate in this part uses** (defined once here; each item names them by these words):
- **the realm hash at seed s, k seasons**: `PYTHONHASHSEED=0 python -c "import sys; from engine.season.boot.realm import build_realm; from engine.season.harness.populated import run; s, k = int(sys.argv[1]), int(sys.argv[2]); w = build_realm(s); run(k, s, w=w); print(w.content_hash())" <s> <k>`; `k = 0` is the build hash. `[ASSUMPTION: `run(k, s, w=w)` advances `w` in place, so `w.content_hash()` after it is the season's hash — basis: `harness/populated.py::run` at `aa31fd2` builds a `SeasonDriver(w)` on the passed world and calls `d.season` on it k times]`
- **the headless hash**: `PYTHONHASHSEED=0 python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0`, its `CONTENT HASH` line (CIP §1 "Baselines").

Every before-reading is the previous close's after-reading, quoted `reading @<sha>`, never re-taken (`V12_STRUCTURE_part2.md` §5.9; the skill, "Baselines"). Per item: the covering test file(s); at `.99`: seeds 0 to 2 and the batch's declared readings (E-2).

---


---

*The batches of this part are in `valoria_master_workplan_v12_part6_cont.md`: B03a-prose, B13-pc-package and B16M-mb-engine-words.*
