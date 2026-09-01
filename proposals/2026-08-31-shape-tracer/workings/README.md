# Workings — the session's raw material, kept so the results can be re-derived

## Status: **WORKING MATERIAL. Not a finding, not a proposal, not reference.**

Everything here is scratch: the briefs the lanes were given, the intermediate extraction, and the
exact text the two classification passes were handed. It is committed because the container it lived
in is ephemeral and **three claims in `04_UNIFIED_SHAPE.md` are only checkable against it.**

**Nothing in this directory is authoritative.** Where it disagrees with `01`–`04` or `cases/`, those
win — they are the corrected, re-run versions. The `.yaml` under `extraction/` in particular is
**pre-repair** and differs from the committed corpus; that difference is the point of keeping it.

| | what it is | what it lets you check |
|---|---|---|
| `briefs/LANE_BRIEF.md` · `briefs/FABLE_BRIEF.md` | what the 12 archive scrape lanes and the 3 comparative lanes were told | the **"blind to PR #350 by instruction"** claim. The instruction is in `LANE_BRIEF.md`, verbatim |
| `briefs/PR350_DIGEST.md` | the digest the comparative lanes were given **instead of** the suite | that the comparative lanes saw a summary, not the proposal |
| `classifier_inputs/ENDINGS.md` | the exact 50 `ends_when` strings handed to the ending classifier — **and nothing else** | that the **19-of-50 `forced_by_threshold`** figure was produced blind. This is the weakest evidence in the proposal and this file is what makes it auditable |
| `classifier_inputs/UNMAPPED_CORE.md` | the 95 `core` needs that failed to route, as handed to the clustering pass | the *"a third restate C1–C9, one primitive missing"* read in `02` §5 |
| `extraction/*.py` · `extraction/*.yaml` | the lane-output repair and assembly, **pre-repair** | how truncated lane output was trimmed to whole entries. The repair discards partial edges and invents nothing; this is the before-state |
| `extraction/a*.txt` | raw arc-source excerpts pulled for the second arc lane | that the arc cases came from the corpus and not from me |
| `prbody.md` | the PR body as posted | — |

---

## ⚠ WHAT IS DELIBERATELY NOT HERE, AND WHY

**The 21MB `snapshot/` tree — 819 files of `v30-snapshot-2026-06-28`'s `designs/`.** Every one of
those 819 files was verified byte-identical to the tag before this decision was made:

```
tag v30-snapshot-2026-06-28 = 21331dafcfe3fa169d8fe2597abd19f6aeb58fba
819 files compared · 819 identical · 0 differing
```

**The tag is in this repository.** Committing the tree would add a second copy of content already at
a named ref, which is the shape `CLAUDE.md` §3 names when it says a graveyard nothing visits is just
a second copy of `git log`. Reproduce it in one command:

```
git archive v30-snapshot-2026-06-28 designs | tar -x -C <somewhere>
```

**Also not duplicated, because it is already committed under its proper name:** the 15 lane reports
(`evidence/LANE_A..L.md` and `evidence/COMPARE_1..3.md` in the archive-recovery proposal — the three
`LANE_FABLE*.md` are the `COMPARE_*` files under their working names), the six case YAMLs
(`cases/`), `CASE_BRIEF.md`, `CONVERGENCE.md` (`01_CONVERGENCE.md`) and the scene-budget ruling
(`02_SCENE_BUDGET_RULING.md`). All verified identical by `cmp` rather than assumed.

---

## A note for whoever runs the naming lint here

`tools/ci_naming_check.py --warn` reports **four** drift hits in this directory — *"Cohesion"* in
`briefs/PR350_DIGEST.md` (×2) and `extraction/a31_35.txt` (×2), where canon now says *Discipline*.

**They are left alone deliberately.** Both files are **verbatim quotation**: `a31_35.txt` is a raw
excerpt of the arc corpus at `v30-snapshot-2026-06-28`, and `PR350_DIGEST.md` quotes PR #350's own
text. Renaming inside a quotation would corrupt the thing the file exists to preserve — and these
files exist *only* to be checkable against their sources.

The **blocking** gate (`ci_naming_check.py`, no flag) passes; `--warn` is the report-only drift lint
in `validators-report`, which never fails the build. If a future pass wants these silenced, the fix
is an exclusion for quoted archive material, **not** an edit to the quotations.
