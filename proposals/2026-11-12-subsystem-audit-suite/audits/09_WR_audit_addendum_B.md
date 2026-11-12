# WR — adversarial steelman audit, addendum B

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: a3ee7e6 (working tree)

The first WR audit (`09_WR_audit.md`) was read at `601e715`. `git diff --stat 601e715 a3ee7e6 -- engine modules
systems references architecture workplans registers research CURRENT.md` is empty: no code, registry, plan or
research file moved between the two readings, so every run the first audit logs (its §12, E-01 to E-17) is a
reading of the tree this addendum was written against. Findings continue the first audit's numbering from
`F-WR-13`; resolutions continue from `R-21`; evidence ids are `EB-nn` so they cannot be confused with the
first audit's `E-nn`. Nothing in the first audit or its five proposals is edited; where this file disagrees
it says so, and where a proposal is replaced the replacement carries a `_B` suffix and names what it
supersedes.

Design documents under `.designs/` and audits under `.audit/` are cited as referents for intent, vocabulary
and history (CLAUDE.md §0.05); none is the reason a behaviour is correct, and no proposal here makes code,
a tool or a test read either tree.

## 1. What was read

Written as the reading proceeded; the list at the end of this section is the final one.

**Read in full, block 1 (research and the narrative-engine referents).**
`research/emergent_narrative_literature/00_README.md`, `01` to `07` and `08_not_read.md` (all 42 entries and
the 75-row apparatus); `.audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v1.md`,
`narrative_engine_design_v2_churn.md`, `integration_with_ners_audit.md`.

