# Instruction suite, lane IS-A — the nine requirements (R-01 to R-09)

## Status: PROPOSED (stage 4 of `STAGES.md`; batch-shaped instructions for workplan v12; resolves nothing at runtime, CLAUDE.md §0.05; not canon; nothing here executes)

## Read at: branch `ccr-62958c70-0kjhsw`, HEAD `6e1ea91`, working tree of 2026-11-12 (dirty in `architecture/`, `references/id_reservations.yaml` and two ED ledgers: other lanes' work, not touched here). Producer: Fable, lane IS-A. Work order: `master/INSTRUCTION_SUITE_ORDER.md`.

**What this file is.** For each of the nine requirements of `engine/season/requirements.yaml`: the reading
today, what execution would make the row read `met` under CLAUDE.md §0.2, the sequence of batches that gets
there, and the items no existing proposal carries. Then the milestone grouping: how v12 groups the batches of
`unified/U3_DEPENDENCY_ORDER.md` into milestones by requirement. It does not restate a proposal's coding
instructions; an item that points at a proposal says so and adds only what is missing.

**Words.** `unified/U1_GLOSSARY.md`'s words are used. A *row* is one of R-01 to R-09. A *reading* is what an
instrument printed on a named tree. A *batch* is a handle `B00` to `B41` of `U3` (one close each); `IS-A-n`
is an item of this file; `BIS-n` is a batch this file creates. A *milestone* is a set of batches whose last
close moves a row (the ordinary sense: a stage reached; the tree's M1 is one such). The *act-count
instrument* is `harness/aperture.py`. `04` is `architecture/meta/04_CODE_ARCHITECTURE.md`.

**Parts.** This file: §0 the reading today, §1 what "met" has to mean, §2 to §10 one section per row.
`IS_A_NINE_part2.md`: §11 the items in full (item form), §12 the milestone grouping and the requirement map,
§13 gaps closed, §14 what was not checked.

---

## 0. The reading today (run by this lane, tree `6e1ea91`, `PYTHONHASHSEED=0`)

| command | printed | cost |
|---|---|---|
| `python -m engine.season.harness.register --requirements` | `met 3 · not_met 1 · partial 5`; R-01, R-02, R-03 `met`; R-05 `not_met`; R-04, R-06, R-07, R-08, R-09 `partial`; last line `REQUIREMENTS: every row carries a measurement or names one` | 0.7 s |
| `python tools/m1_acceptance.py --summary` | `verdict: NOT MET`, `1 row(s) failing`. Row 1 stub invocations `0 PASS` (seed 20260819, one season); row 2 same seed same hash `bbf88d55e218… PASS`; row 3 the nine `3/9 FAIL`, self-declared `DOC-DERIVED`; row 4 `0` invariant violations over 24 seeds × 4 seasons + 2 populated × 1, eight invariants, `PASS` | 21 s |

Both agree with the holistic audit's log (`master/HOLISTIC_AUDIT_part3.md` §9 rows 1 and 2, read at `4dc8a7b`):
nothing between the two trees moved either reading.

**What kind of reading each row's `status:` is.** The register checks one thing: that a row claiming `met`
carries a `measured:` line (`requirements.yaml:5-8`). It does not run a row's `measure:` command. So every
`status:` is a hand-edited string behind which a command was run once on a named tree; `m1_acceptance` row 3
counts those strings and says so. Two of the three `met` rows rest on a run nobody can repeat cheaply (R-02:
36 chunk cells, about 75 minutes, by a script under `proposals/`), and four rows share one eight-minute
command (`corpus_run`) whose printed line the row then interprets by prose. This is the first thing §1 fixes.
