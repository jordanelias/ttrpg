# U4 — intent traceability: each of Jordan's stated intents, traced to the proposal, the batch and the gate that carries it

## Status: WORK LEDGER (unification lane U4a, test 8 and test 9 of `UNIFICATION_BRIEF.md`; reference, resolves nothing at runtime, CLAUDE.md §0.05; deleted when workplan v12 is adopted)

## Read at: the working tree of branch `ccr-62958c70-0kjhsw`, 2026-11-12, after waves 1 to 3. Lane: U4a (Sonnet). One round; no second audit of this file.

## 0. What this file is, and how a row was marked

**Purpose.** `UNIFICATION_BRIEF.md` test 8: *each of Jordan's statements is traced through the suite to the proposals that carry it, and gaps are named.* Test 9: *every proposal and recommendation carries instructions a later batch can execute.* This file is the matrix for both. It edits no proposal, audit, code, canon or ruling.

**Sources of the rows (opened).** The nine: `engine/season/requirements.yaml` `rows:` (the `statement:` text is quoted verbatim below; `:199`, `:563`, `:725`, `:816`, `:926`, `:1151`, `:1388`, `:1473`, `:1566`). The standing intents: `AUDIT_BRIEF.md` (standing requirement `:10-34`; no-determinism `:36-59`; do-not-guess `:61-71`; capability authoring `:150-183`; detective and noir `:228-268`; mass battle cell approach `:270-298`; personal combat `:300-319`; NPC and chooser `:321-352`; mass battle intent `:354-391`; eras `:541-543`; coding instructions `:545-547`; entrenchment `:549-551`; no scene still `:553-555`), `IMPLEMENTATION_BRIEF_A.md:5-24` (computed play must reach; no dead ends), `INSTITUTIONS_BRIEF.md:10-32` (the fixed points), `VERBS_BRIEF.md:3-11`, `audits/23_STORY_ENABLEMENT.md:7` ("make the impossible stories possible"). The rulings: `unified/DECISIONS_ANSWERED.md` A-1 to A-93 (A-92 and A-93 are the last two rows of the table, `:128-129`). The carriers: `proposals/` (300 files), landed by the batches of `unified/U3_DEPENDENCY_ORDER.md` §2.1 (handles `B00`..`B41`; `B13` unused).

**The marks (the lane's rule).**

| mark | meaning | what it requires |
|---|---|---|
| **CARRIED** | the intent is carried | a proposal file and section **I opened**, a batch handle from U3 §2.1 that lists that file, a gate in that proposal that is an execution artifact (a named test, a command and its expected reading), and, where the intent is a draw or a hash mover, the declared mover |
| **PARTIAL** | carried in part | what is missing, stated in the cell |
| **GAP** | nothing carries it | beside it, the exact proposal text or v12 item that would carry it (decidable from the repository), or the reason it cannot yet be written |
| UNVERIFIED | a pointer I did not open | stated as such; never counted as CARRIED |

A row marked CARRIED means *the suite carries it in a proposal with a gate*. It does **not** mean the behaviour executes: no proposal is landed, and CLAUDE.md §0.2 says done is a run (`python tools/m1_acceptance.py --summary` is the instrument). The register's reading of the nine today is `status:` per row in `requirements.yaml` (R-01 `met`, R-02 `met`, R-03 `met`, R-04 `partial`, R-05 `not_met`, R-06 `partial`, R-07 `partial`, R-08 `partial`, R-09 `partial`, by the `status:` lines at `:201`, `:565`, `:729`, `:818`, `:930`, `:1154`, `:1392`, `:1477`, `:1568`). Those are the tree's, not this file's.

**How a pointer was verified.** For every row I opened the proposal file at the named section (by heading and `A-NN` / requirement grep, with the heading above the hit) and the batch row in U3 §2.1. A batch handle is quoted from the §2.1 table, not from the proposal's own `Lands in batch:` line, where the two differ the difference is stated. The whole of an A-row's proposal body was not re-read; a row where only the head line was seen is marked so.

**Hash movers and reading discipline.** Where a row's carrier is a hash mover, the cell says so only if the proposal declares it (U3 §2.1 column "declared hash movers"); I did not re-derive movers.

## 1. Counts (filled at the close of the file)

(See §9.)

