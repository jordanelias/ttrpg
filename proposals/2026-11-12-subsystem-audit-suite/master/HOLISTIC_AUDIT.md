# Holistic audit — the game as a suite of engines

## Status: REFERENCE (stage 3 of `STAGES.md`; an audit; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: `4dc8a7b` (working tree, 2026-11-12). Producer: Fable, the holistic lane. Companions: `master/CODEBASE_IMPROVEMENT_PROPOSAL.md` (the edits), `master/HOLISTIC_FOR_JORDAN.md` (what survives the ladder).

Parts: this file (§0 verdict, §1 method and limits, §2 the engines, §3 what the loop calls), `_part2`
(§4 findings ranked, §5 the six directions), `_part3` (§6 the nine requirements, §7 port cost, §8 evidence
log). The verdict in §0 is written last and placed first.

## 1. Method, partition and limits

**Subject.** `engine/season/`, `modules/`, `engine/substrate/`, `engine/dice_engine/`,
`engine/engine_params/`, `tools/` and the registries they read. Measured by `git ls-files` and `ast`
(`master/work/W1_AREAS_AND_LINES.md`): 293 Python files under `engine/` (131,180 lines, of which
`engine/season/tests/` is 166 files and 71,169 lines), 57 under `modules/` (18,213 lines), 54 under
`tools/` (15,016 lines). The line count overstates the code: see finding H-02.

**Instruments used** (the methods of three ratified skills, as planning instruments only; no edit was
made to the tree): `layer-conformance` Lens A (placement), `valoria-simplify` SURVEY (the map M1 to M6, the
six directions) and its DISTIL rules as a *plan* (EARN, the control C1 to C6, the ladder), then
`layer-conformance` Lens B (rows of `architecture/meta/04_CODE_ARCHITECTURE.md` read at the line). The
plants of `valoria-simplify` C2 were **not** run by this lane (they need a worktree and edits); every
item in the improvement proposal therefore names its plant as a step of its own gate.

**The partition, and why.** By the areas `valoria-simplify` M1 defines, grouped by what one engine is:

| # | partition | areas | why it is one reading |
|---|---|---|---|
| P1 | the season kernel | `engine/season/loop`, `state`, `gaps.py`, `trace_log.py` | one write gate, one fold, seven steps |
| P2 | the chooser and the readers | `engine/season/decision`, `queries`, `epistemic.py` | what a person reads and how he picks |
| P3 | the data channel | `engine/season/data`, `manifest`, the YAML registries, `engine/engine_params`, `engine/substrate` | every fact code reads and its loader |
| P4 | the resolvers and their seams | `engine/season/seam`, `modules/*`, `engine/dice_engine` | the draw, the ladder, the registered modules |
| P5 | the instruments | `engine/season/harness`, `engine/reference` | what observes the game |
| P6 | the apparatus | `tools/` | exporters (load-bearing on the game) apart from process gates |

**Shared reading, forked judgment.** The reading was shared in two ways. (1) The dossiers, digests,
census lists and the grounding audit (`dossiers/`, `digests/`, `census/`, `audits/17_CENSUS_*`,
`audits/25_GROUNDING_ENGINE.md`) already hold the per-file reading; they are cited, not redone. (2) The
mechanical extraction was done once by throwaway `ast` probes and seeded runs, and written as
fixed-format extract files under `master/work/` (`W1` to `W8`). **No reader agents were spawned: this
lane's toolset held no agent-dispatch tool** (stated in the receipt), so the per-partition extraction
the brief assigned to `valoria-measure` and `valoria-author` readers was done by script instead, which
for counting and edge extraction is the cheaper tier in any case. The judgment in §4 onward is this
lane's alone. One round; no second wave.

**What this lane did not do** (carried forward, not hidden):

- It did not read the 56,000 non-blank lines of non-test Python in full. It read heads, the seam files,
  the loaders' interfaces and every site a finding cites; everything else rests on the extracts and on
  the cited audits. A finding that rests on an extract says which.
- It ran no `pytest`, no long `aperture`, no `corpus_run` (eight minutes, already recorded by the CORE
  lane) and no C2 plant.
- It did not open `jordanelias/valoria-game` (not in this clone) and did not read the Godot reference
  for the ruled series (`ED-GO-0002`): no outbound read was made. **Every port-cost line in §7 is
  therefore a statement about the Python construct only, and the GDScript half is marked
  `[NOT READ]`** (`valoria-simplify` THE PORT NOTE requires the page; it was not read).
- `efficient-coding-review` excludes `tools/`, `tests/` and `systems/` from its subject (*"a standard
  pointed at the repository's own apparatus is the recursion CLAUDE.md §0.1 pt 5 exists to stop"*). The
  brief names `tools/`. This audit therefore reads `tools/` under one question only: which tools are
  load-bearing on the game (an exporter whose output the engine opens), and which are process apparatus.
  For the second kind the only dispositions offered are delete or leave; no guard, no grader.
- History: the clone is shallow (`.git/shallow` present; `audits/25_GROUNDING_ENGINE.md` §0), so the
  history instrument (I5: co-change, carried cost) did not run. The *over time* and *diagonal*
  directions are PARTLY at best and say so.
