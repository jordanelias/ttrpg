# L1_APPLIED — running record of the Layer 1 amendment lane (A-97)

## Status: WORK RECORD (the Layer 1 amendment lane, 2026-11-12; reference, resolves nothing at runtime, CLAUDE.md §0.05; deleted with `unified/work/` when v12 is adopted)

Authority: Jordan, `unified/DECISIONS_ANSWERED.md` A-97 (*"Layer 1: make amendments as required"*) and A-96
(J-U6-01 Option A). Drafts: `unified/U3_LAYER1_AMENDMENTS.md`. Every edit below follows a ruling A-n; none edits
Layer 1 to match code.

## Method and conventions followed

- **Convention read at the heads.** `04` and `hol` carry their amendments as `⚠ AMENDED <date> (Jordan-directed,
  <ids>): <what>` on the `## Status:` line (2026-10-03, 2026-10-28) and in place, keeping the superseded text legible
  (`04:150` "This line read …"; `04:331` "⚠ AMENDED: `dates[]` DELETED …"; `04:1026` "CONSTRUCTION AMENDED, GRADE
  UNCHANGED"; rev. 2's rule: *"nothing is overwritten silently"*). Followed: each in-place edit says `⚠ AMENDED
  2026-11-12 (Jordan, A-n; A-97, node L1-An)` and quotes what the text read.
- **`hol` is append-only in this lane.** `engine/season/harness/register.py::verify_citations` checks every
  `hole_register.yaml` `cite:` quote against `hol` AT the cited line (±6). Inserting a line in `hol` would move
  every later citation, so every `hol` amendment is appended to an existing line; no `hol` sentence is replaced
  and no line is added. Baseline before any edit: `python -m engine.season.harness.register --verify-citations`
  → `CITATIONS: all resolve`, exit 0.
- **`04` new lines kept to the minimum** so the suite's `04:NNN` citations stay valid as far as possible: one new
  PART D row (52, A-96) placed after row 51, and one note line in §C.4 (A-96). Line shifts are recorded per node.
- **Other `architecture/` files** (the stage documents 00–10, `ARCHITECTURE_V2.md`, `PLAN.md`; all `## Status:
  RATIFIED`, Layer 1) are not amended in substance; where one restates an old rule as live, a one-clause pointer
  is appended to that line naming the node (append-only, for the same citation reason).
- **Ledger rows.** The ledger's superseding-row convention (ED-IN-0149 precedent, restated in `ED-MB-0016`'s
  2026-10-26 row: *"The earlier row is NOT rewritten; an id's effective status is its LAST row"*) puts a
  superseding row under the SUPERSEDED id with `supersedes_row: true`. Followed for A-22, A-24, A-77, A-85.
  One new id is allocated from `references/id_reservations.yaml` (IN `next_free` 358 → 359): `ED-IN-0358`, the
  record of this Layer 1 amendment, as every earlier Layer 1 amendment carries one (ED-IN-0284/0285, 0302/0303).
  `[ASSUMPTION: the orchestrator asked for new ids for the successors; the ledger's own convention is a same-id
  superseding row; taken because a new id would leave the old id's effective status (its last row) unchanged.
  Revert: re-key the four rows to fresh ids.]`

## Per node

