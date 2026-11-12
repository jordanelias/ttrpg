---
name: methodology-execute
description: >
  METHODOLOGY-EXECUTE — invoked as `/methodology-execute <free-text task>`. Builds every item a
  task or workplan area names, as ordered BATCHES, then verifies once per batch (`methodology-close`'s
  Phases 1–3 plus an accretion pass) instead of once per item; between batches the finished positions
  are deleted from the plan and the context window is cleared. The run order, the approval stop and
  the status line a driver reads are in the body. Use for: "run methodology-execute",
  "/methodology-execute <task>", "build out this phase/area", a workplan position, phase or free-text
  area of work that has not been built yet and needs both building and verifying before `/close`.
  Not for: a diff that already exists and only needs verifying (`methodology-close`); design-quality
  grading (`ners`); a target that resolves by a draw (`resolution-diagnostic`); Layer placement with
  no build to do (`layer-conformance`).
---

# METHODOLOGY-EXECUTE — build, then close

Split out of `methodology-close` 2026-09-29 so the pipeline also orchestrates the build. A batch is a
partition by shared files and gates and is the unit of context (2026-10-06). Every agent assignment
of a batch is planned when the batch opens (2026-11-12). Invocable as a project skill through the
symlink `.claude/skills/methodology-execute`; dated history beyond this line is in `git log`.

## What this skill owns, and what it copies

| the content | its single owner |
|---|---|
| the build phase — dispatching producers, sizing the fan, integrating parallel write lanes | **this file** |
| the assignment plan — every agent dispatch of a batch, planned at BATCH OPEN | **this file**; the tiers it reads are CLAUDE.md §10's (producers) and `methodology-close`'s (critics) |
| batching — partition, context sets, where the boundary falls, what is deleted and cleared | **this file**, except a plan's own batch structure (§BATCHES) |
| the status line and the `approved:` prefix | **this file**; `tools/methodology_drive.py` reads and writes them by this spelling and defines neither |
| deleting a finished position from the plan | **CLAUDE.md §2** (*"Finished positions leave the plan; the commit is their record"*); this file adds the pre-deletion reference check (§BOUNDARY) |
| the sequence, tiers, checklists, handshake, guardrails and falsifiers for verifying the batch diff | **`methodology-close`**, by reference, never copied |
| the producer contract — full toolset, a receipt not a transcript, no commit, no full suite mid-lane | **`.claude/agents/valoria-author.md`** |
| model tiers, the effort ladder, the fan-out sizing rule ("ask what N-1 would miss") | **CLAUDE.md §10** |
| a workplan position's INSTRUCTION / WHERE / FALSIFIER / GATE | **that position's own content-owner file** — never restated here |

**Roles.** A Phase 0 dispatch is a `valoria-author` **producer**; a fanned build is merged by the
**integrator** (the orchestrator); *agonist* and *antagonist* are `methodology-close`'s read-only
review roles and never name a producer. **This skill's BATCH-CLOSE *is* `methodology-close`'s Phases
1–3, unmodified**, plus the accretion pass; a change to that sequence is made once, in that file.

**Cadence.** The expensive pass — the agonist/antagonist fan, `/code-review`→`/simplify`→
`layer-conformance`, the full suite, the terminal critique — runs once per batch, never per item
(CLAUDE.md §0.4; RULED, Jordan 2026-10-06: *"code review and simplify to be at batch close"*). Every
item still gets its own commit. Deferred is not skipped: a batch whose items were built and which
never reached BATCH-CLOSE has closed nothing, and reporting it "closed" is the false claim
`methodology-close`'s falsifier table already catches.

---

## THE SHAPE OF A RUN

```
  BATCH k    OPEN ──▶ item 1 ──▶ BUILD ──▶ commit ─┐
  (as a      (orient  item 2 ──▶ BUILD ──▶ commit ─┼─▶ BATCH-CLOSE (once per batch):
  session    from        ⋮  (every item)           ┘     PHASE 1 · AGONIST FAN → ANTAGONIST
  opens)     disk, then                                    PHASE 2 · MECHANICAL GATES (+ the one suite run, CLAUDE.md §0.4)
             PLAN ALL                                      ACCRETION PASS
             AGENTS)                                       PHASE 3 · TERMINAL CRITIQUE
                                                                  │
                                                  (last batch: /close)
                                                                  │
                                                  EXPUNGE ◀───────┘  (delete the batch from the plan)
                                                      │
       BOUNDARY — reload C(k) ∩ C(k+1) from disk · never reload C(k) ∖ C(k+1) · load C(k+1) ∖ C(k)
                                                      │
  BATCH k+1  OPEN ──▶ …
```

## RUN ORDER

One spine, in execution order. Steps 0–3 happen once per invocation; 4–8 once per batch.

### 0. Resume check — the first act of any invocation

If the lane's Open table (`registers/handoffs/HANDOFF_<LANE>.md`) holds an in-flight row (§THE IN-FLIGHT
ROW), that batch is the one to continue, whatever the invocation text says. An invocation whose text
does not match it stops and reports it (`STOPPED`); it never opens a second batch.

1. **Check the row against the tree.** Every `built` handle must have a commit in `open..HEAD`
   carrying `Item: <handle>`, and every such trailer there must be in the row. Where they disagree the
   commits win: correct the row and say so; if they cannot be reconciled, ask.
2. **Look at the tree.** A killed run leaves residue in a producer's worktree (`git worktree list`) or
   in the working tree (`git status`). Find the item's latest `[<scope>] WIP checkpoint: <handle>`
   commit (`git log --all --grep='WIP checkpoint:'` — unanchored, since the subject opens with the
   `[scope]` tag; `--all`, since a checkpoint sits on its producer's worktree branch). Where one
   exists, `git stash push -u` the residue (reversible) and CONTINUE from that checkpoint, naming its
   SHA in the producer's brief; where none exists, stash and rebuild. A handle with a checkpoint but
   no `Item:` commit is "continue", not "build whole". A `Falsified: <handle>` trailer marks an attempt
   its own falsifier rejected and a revert undid: it is not rebuilt, and the hole row it cites is its
   record. Never commit residue as an `Item:`; a checkpoint is the only unreviewed commit. Instrument
   worktrees (detached, named for their instrument) are removed and the instrument re-run, not
   integrated; each remaining producer worktree is verified and integrated (step 5) or removed.
3. **Re-enter.** Run BATCH OPEN items 1, 2, 3 and 5 (currency, context set, gate check, assignment
   plan — read back from the batch-open commit, not re-derived); **never item 4**: `open` stays the
   row's, or the range BATCH-CLOSE reads silently shrinks. Build only the items not in `built`; run
   BATCH-CLOSE from the phase after `close`.
4. **Built but not closed.** A position the plan or handoff records as BUILT with its close not run
   enters at BATCH-CLOSE: write the row with `built` filled and `open` the range start that record
   names; if it names none, ask.

No row: continue to step 1. (The row is committed at BATCH OPEN, before any dispatch, so a death in
item 1 still leaves one — step 4.)

### 1. Scope — resolve the free text before touching anything

`/methodology-execute <task>` hands this skill free text, not a position handle. A vague area is not
one buildable unit, and this file does not guess which was meant.

1. **Search the live workplan.** Run `/currency` and follow `CURRENT.md` to the live plan (no filename
   is written here: it would be the stale pointer CLAUDE.md §1 exists to prevent). Check it, any
   workplan it carves out by name (CLAUDE.md §2), and the lane's Open table (where an ad hoc task's
   batches live), for a position whose handle or `what runs` plausibly matches.
2. **Read the prefix.** Text beginning `approved:` means a person already approved the sequence the
   stop below would present (an interactive first run, or a driver's `--approved`). It skips **only
   that stop**; the gate checks, the in-flight check and every other `STOPPED` condition still apply.
   **It never licenses a new task:** finished positions are expunged, so `approved:` text that matches
   nothing now is `STOPPED` (*finished, or the plan changed*). An optional trailing `[next: <handle>]`
   (a driver copies it from the previous `NEXT` line) fixes the batch to run; if the plan's next batch
   is not that handle, `STOPPED`.
3. **Classify what the search found** — four cases, exhaustive:
   - **One position, `GATE` met, and it is a whole batch of its own** — proceed to step 2. No
     confirmation: its gate establishes it is buildable now.
   - **One position inside a larger plan batch, or some but not all of one batch's positions, or a
     span of batches** — the §BATCHES stop: build the whole batch, or run a **partial batch**.
   - **More than one matching position** — a free-text area usually names a *cluster*. Resolve the
     ordered subsequence (each position's own `GATE` respected) and **stop and present it**, any unmet
     gate flagged. This is CLAUDE.md §0's own rule: *"Anything ambiguous or spanning lanes: get the
     plan approved or ask a focused question."*
   - **No matching position** — a new, unplanned task. Write the plan (`methodology-close` §1.1,
     CLAUDE.md §0's first bullet: what changes, in what order, how you will verify) and **stop and
     present it**, unless a one-sentence plan already fully states it. **An ad hoc plan names each
     item's edit set and its gates, or states "none"** — the partition (§BATCHES) reads them from
     there.

### 2. Express the sequence as batches

§BATCHES: the plan's own batches, where it has them; otherwise derived by the partition. Take them in
order. A single position or a one-sentence task is a one-item batch.

### 3. The approval stop — one stop, not several

Where step 1 required a stop, one presentation covers the sequence **and** its batches (handles in
order, gates flagged, each cut along a link stated with its reason, each conflict between a plan's own
sources stated). **The assignment plan is not part of this stop** — it is made per batch, at BATCH
OPEN, when that batch's gates are known to be met. If a later queued item's `GATE` turns out unmet when
its turn comes (outside this run's scope, or a `JORDAN` item), **stop there and report it**
(`STOPPED`); never skip it silently and continue, and never run BATCH-CLOSE on a batch that stopped
short without saying so.

### 4. BATCH OPEN — orient as a session opens

1. **Establish currency:** `/currency`, then the lane's handoff and the plan's rows for this batch
   only. Skip it when step 1 ran it in this same window.
2. **Load this batch's context set from disk**, the overlap with the last batch included
   (§THE CONTEXT SET). Do not rely on having read it.
3. **Check every item's gate against the tree**, never an earlier window's belief that it landed. By
   kind: a **SHA** is met iff `git merge-base --is-ancestor <sha> HEAD`; a **position** is met iff the
   plan no longer holds it and its landing SHA is written in the gate, or the plan's own status
   vocabulary marks it landed with the evidence named (a position recorded BUILT with its close not run
   is **not** landed); a **batch** is met iff its close landed (its rows gone or marked closed by the
   plan's own rule, its closing SHA in the gate and an ancestor of `HEAD`); a **ruling or decision** is
   met iff the ledger row that owns it (`registers/`, last row governs) records it resolved. A gate of
   none of these kinds is unmet — `STOPPED`.
4. **Plan every agent assignment the batch will make** (§THE ASSIGNMENT PLAN). Runs after item 3, so an
   unmet gate stops the batch before any planning is spent on it.
5. **Record the starting commit and commit the row, before any dispatch.** `open <sha>` is `HEAD` as
   items 1–3 found it. Write the in-flight row (§THE IN-FLIGHT ROW) — and, for a derived batch, its
   batch rows (§BATCHES, source 5) — and commit them **row-only, `[skip ci]`**, with the assignment
   plan as the commit body's one paragraph. A death anywhere after this resumes from step 0; a death
   before it loses nothing but the plan. The batch's diff is the **commit range `<open sha>..HEAD`**;
   every item commits at once, so the tree is clean when BATCH-CLOSE runs.

### 5. Build, once per item (the producer's work, then the orchestrator's)

For each item in order — **serial: each commits before the next builds; a fan lives inside an item**:

**5.1 Read the unit's instruction — never invented here.** A workplan position: read its
content-owner entry (INSTRUCTION / WHERE / FALSIFIER / GATE) in full. An ad hoc task: the plan
step 1 wrote. Either way that instruction **is** the plan Phase 1 checks fidelity against; hand the
producer the same text, not a paraphrase or a second draft.

**5.2 Dispatch what the assignment plan says** for this item, or state the deviation (§THE
ASSIGNMENT PLAN, *Deviating*). Every producer is `Agent({ subagent_type: "valoria-author", ... })` in
`isolation: worktree` (RULED 2026-10-13, the session's user: *"just batch the work so the tree is
clean"*): the working branch's tree stays clean between items, and only a verified result reaches it,
as the item's one commit. **One producer is the default.** Fan only when the instruction names
genuinely independent sub-parts that share no file (the live plan's hard-serial-edge table, reached
through `CURRENT.md`, catches the same thing); each producer is handed **only its own sub-part's
instruction**, returns a receipt (path, what changed, one line), and the first dispatch fires alone,
its first streamed token awaited, before the rest go in one message (CLAUDE.md §10 pt 3).

**5.3 Checkpoint, then integrate.** At every producer hand-back, before verifying it, commit a
checkpoint (§CHECKPOINTS). Then the **orchestrator**, not a subagent, verifies each worktree's result
(the covering test file, or a one- or two-season probe) and merges it into the working branch — when
fanned, in an order that respects any named serial edge. **If two lanes touched the same file, the
split was wrong, not the merge:** stop, do not resolve the collision by hand, and rebuild that file's
portion as one producer. A silent auto-merge of a same-file collision is what the FALSIFIERS table
catches.

**5.4 Commit the item as one commit**, subject `[scope] …` with the `Item: <handle>` trailer, the
in-flight row's `built` update, and the producer's receipt in the body (`NOT DONE` included). **Never
one diff spanning several items.** Subject `[skip ci]` unless this is the batch's last item (§CI
CADENCE).

**5.5 What the phase must not do.** The producer never reviews its own output (verifying its edit runs
is not Phase 1's fidelity check). The **producer** never commits and never runs the full suite
mid-lane (`valoria-author`'s own file); the orchestrator commits (5.4). Never skip the gate check
because the instruction "looks buildable": a position gated on another position or on Jordan is not
this skill's to build around by reinterpreting its gate.

### 6. BATCH-CLOSE — `methodology-close`'s Phases 1–3, once, by reference

Run them **once**, against the commit range `<open sha>..HEAD` — not one item's diff, not a
working-tree diff. A batch has ONE close (RULED, Jordan 2026-11-06, §BATCHES).

0. **Open the PR if none exists, then push the last `Item:` commit** (no `[skip ci]`): that push is
   the first CI run (§CI CADENCE). Write the range diff to a scratchpad file, since `valoria-critic`
   holds only Read, Grep and Glob and cannot run `git diff`; hand the critics its path. **Regenerate
   it before Phase 1 and again before Phase 3**: Phase 3 reads the post-Phase-2 diff, and a file
   written once is stale by then.
1. **Phase 1.** `methodology-close`'s precondition ("there must be a plan to check fidelity against")
   is satisfied by the batch's own instructions together — the plan's stated scope, the union of the
   positions step 1 resolved into it, or the concatenation of the ad hoc instructions. FIDELITY TO
   PLAN means fidelity to *that*, not to one item's `WHERE`. Fan sizing, dispatch order, cache priming
   and reconciliation (§1.2–1.5) apply as written there. **The roster is the one the assignment plan
   provisionally fixed (§THE ASSIGNMENT PLAN), confirmed now against the real range diff**: dispatch it
   as planned, or change it with the reason stated.
2. **Phase 2.** Order and apply-before-next-reads (§2.1–2.4) as written there, against the cumulative
   diff. **The suite is CLAUDE.md §0.4's, not `methodology-close`'s:** at most once per batch, only
   if it can observe something CI will not (cl.1), over only what the diff can reach — name it with
   `python tools/tests_for_diff.py --base <open sha>` (a batch confined to one subsystem runs
   `-m <subsystem>`; one touching engine core, tools or a registry gets the full gates; a batch of
   prose or ledger edits runs just the files that read what it touched). No item inside the batch runs
   it.
3. **The accretion pass — this skill's one addition, between Phase 2 and Phase 3** (the session's
   user, 2026-11-05: *"each batch creates its own specific tools and they accrete causing increasingly
   longer run times for test suites"*; *"as part of methodology execute close"*). Phase 3 then grades
   the tree as it will be left. The orchestrator runs it in its own tree, over what the batch ADDED
   (`git diff --diff-filter=A --name-only <open sha>..HEAD -- tools tests engine`) and what it made
   redundant (an old tool or test an item replaced; CLAUDE.md §2 retires it in the same change).
   **A reader's discipline: NO GUARD MAY BE BUILT FOR THIS** (§0.1 pt 5); its output is deletions in
   the batch's close commit, never a document or a ledger row. For each added file:
   1. **A tool names its caller:** a CI step, a hook, a `ci_checks_registry.yaml` row, an import from
      `engine/` or `modules/`, or a named invocation in the plan. None: delete it; the commit is its
      record. A tool whose only consumer is this repository's own process is judged by §0.1 pt 5's
      predicate (not load-bearing on the game or a Jordan decision): delete it, or accept it and write
      nothing. It never earns a registry row because one batch needed it once.
   2. **A test names the behaviour it observes.** A test whose only subject is a tool step 1 deleted,
      or a one-off migration that has landed, goes with it. A test of game behaviour stays.
   3. **A test's cost is read, not guessed.** Run the batch's added test files alone with
      `--durations`. A test that starts a fresh interpreter (`subprocess`, `python -m
      engine.season…`) or runs seasons states what an in-process check of the same claim would miss;
      where none is named, rewrite it in-process or delete it.
   4. **Unearned, by `valoria-simplify`'s own list** (a second owner of a fact; apparatus where an edit
      to the existing owner would serve; dead or retired code), read at that skill. Its DISTIL mode is
      not run per batch.

   The commit body names the paths deleted; no count or running total (CLAUDE.md §1).
4. **Phase 3.** Tier, escalation trigger, checklist and the top-down/bottom-up handshake (§3.1–3.7) as
   written there, against the post-Phase-2 diff. INTERDEPENDENCIES and the FORWARD/BACKWARD SWEEPS are
   likelier to find something real here than at single-item scale, because several items have landed
   together.
5. **Update the row** at each phase's end (`close <phase>`), in a commit of its own if the phase edited
   nothing.

A CI result is **consumed only if it has already reported when its reconciliation step is reached**;
this skill never waits on GitHub (CLAUDE.md §11). A result not yet in is named in the report as
*unread*, and comes back through the user.

### 7. The last batch is also the run's `/close`

When the sequence is exhausted, BATCH-CLOSE is followed by `/close` (its suite step is BATCH-CLOSE's,
not run twice — lane validator, commit, handoff), **then** the BOUNDARY's expunge. The order is
deliberate: the in-flight row is deleted by the expunge, so it is the last thing to go and a death
anywhere earlier — the suite stretch included — still resumes from the row. A mid-run boundary does
not invoke `/close`.

### 8. BOUNDARY — expunge, merge `main`, then clear

Runs after BATCH-CLOSE's reconciliations are committed, after **every** batch including the last
(for the last, items 1 and 2 only, following `/close`).

1. **Expunge on disk — one commit.** **Before deleting anything, grep the tree for what points at it:**
   every remaining batch's rows (the plan and the lane handoff) for each handle and file about to go,
   and the code and registries for citations of the plan section it sits in (`git grep -n '<plan file>
   §<section>'` — `engine/season/requirements.yaml` cites plan sections and reads them). Delete only
   what nothing still needs. A **gate** naming a finished position or batch is satisfied: rewrite that
   reference, per the plan's own convention, to carry the landing SHA (a batch's: its closing commit)
   in this same commit. A position a remaining batch **reads**, or a section code cites, stays,
   narrowed, until that stops being true. Then remove the batch's finished positions and its `STOP …
   closes here` row, **by the plan's own rule for finished positions, edges and census rows**
   (CLAUDE.md §2); where that rule is a one-line evidence record in a history part, write it, once per
   position. This skill adds no row, count or narrative of its own (CLAUDE.md §1). In the lane
   handoff, remove the batch's handles from the Open rows that name them (a row naming only this
   batch goes; a spanning row is narrowed). Delete the in-flight row. Report the batch's record as its
   commit range, `<open sha>..HEAD`. A position the batch only part-finished stays, narrowed to its
   receipt's `NOT DONE`. A measured gap goes to the one `hole_register.yaml` row the plan's own rule
   allows; what BATCH-CLOSE found and applied is already in the commits; a finding nobody can apply
   without a decision becomes a ledger row only if it is `needs_jordan` after CLAUDE.md §0's
   five-step ladder, and is otherwise dropped — nothing is kept "for the next batch".
2. **Merge `main` into the branch — the run's last step before the stop.** GitHub squash-merges each
   batch's PR, so `main` holds the previous close's squash while this branch still holds that close's
   commits one by one, and the files the expunge edits conflict with it. **`git fetch origin main`
   first, then skip when `git rev-list HEAD..origin/main` is empty** — a test against a ref not yet
   fetched is empty exactly when `main` has moved. Otherwise `git merge origin/main`: never a rebase,
   never a force-push. Read `git diff origin/main HEAD` on each conflicted file: where `main`'s side
   carries nothing the branch lacks, keep the branch side (`git checkout --ours`); where it carries
   something (a PR number written into a record, another session's edit), keep both. A conflict in
   code, or one that cannot be reconciled this way, is `STOPPED`. Commit the merge without `[skip ci]`
   and push it: **it is the head the confirming CI run reads** (§CI CADENCE).
3. **Clear the window.** This skill cannot clear its own context, so the boundary is a **stop**: report
   in a few lines the batch closed, its commit range, whether the confirming CI run was read or is
   unread, and the next batch's handle with whether its gates are met, then end with the status line
   (step 9). **A fresh process is the clear:** `tools/methodology_drive.py` starts one per batch and
   re-invokes as `approved: <the same text>`. Run by hand, tell the user to `/clear` (**not
   `/compact`**: a summary carries forward exactly the `C(k) \ C(k+1)` this rule discards) and
   re-invoke the same way. The finished positions are gone from the plan, so step 1 resolves only
   what remains. The driver is the operator's loop, outside any session; this skill never arms its
   own (CLAUDE.md §11).
4. **A batch is not handed to a subagent to obtain the clean window**: a delegate that cannot
   dispatch `valoria-author` and `valoria-critic` cannot run a batch. Whether a given agent type can
   is a probe to re-run before relying on it either way.
5. **If the invocation told the run to continue through several batches in one window**, do — and say
   at each boundary that **context was NOT cleared**: only the on-disk expunge happened, and every
   batch after the first carries the earlier ones' residue.

### 9. THE STATUS LINE — the one thing a driver reads

Every invocation ends its final message with exactly one line, last, plain text (no markdown), after
the human-readable report:

- `METHODOLOGY-EXECUTE: NEXT <batch handle, as its plan writes it>` — a batch closed and was expunged;
  at least one remains and its first item's gates are met. A driver copies the handle into the next
  invocation as `[next: <handle>]`.
- `METHODOLOGY-EXECUTE: COMPLETE` — the sequence is exhausted, `/close` ran and the last expunge landed.
- `METHODOLOGY-EXECUTE: STOPPED <one-line reason>` — anything that needs a person: the approval stop;
  `approved:` text that matches nothing; an unmet gate or a `JORDAN` item; a `needs_jordan` ruling
  that survives CLAUDE.md §0's five-step ladder; an in-flight row that cannot be reconciled with the
  commits; a BATCH-CLOSE finding that can neither be applied nor rejected with a measurement; the next
  batch's gate unmet; **a partial batch closed** (its remainder shares the same text, which now
  matches nothing — name the remainder in the reason).

CI state goes in the report, never on this line. An invocation that dies before the line produces no
line, and **a driver treats absence as `STOPPED`**. The line is defined here and nowhere else.

---

## THE ASSIGNMENT PLAN — every agent dispatch of a batch, planned at BATCH OPEN item 4

Jordan's directive, 2026-11-12: *"at the beginning of a batch it will carefully plan out all
agent assignments"*. It covers **both halves of the batch** — every Phase 0 producer and every
BATCH-CLOSE dispatch — because the close's roster is knowable from the same items' entries, and sizing
it only when the close arrives is how a batch ends with a fan nobody weighed. It reads only what the
batch already holds (each item's entry, the partition's edit and gate sets, `valoria-author`'s
contract, CLAUDE.md §10, `methodology-close` §1.2–1.4 and §3.2) and invents no tier, count or effort.

**The default needs no rows.** One producer per item and `methodology-close`'s default Phase 1 roster,
antagonist and Phase 3 critic: the plan is one sentence saying so. **Rows are written only where the
plan departs from the default**, and for every producer a fan adds. Each row names:

- **item or lens** served · **agent type** · **model and effort**, set explicitly — producers by
  CLAUDE.md §10 (what the node does, not a habit); **critics as `methodology-close` §1.3, §1.4 and
  §3.2 fix them**, not re-judged · **isolation** (`worktree` for every producer; none for read-only
  critics and for a `valoria-measure` row) · **inputs handed** (the instruction text verbatim; the
  before-readings the baseline rule already holds; the commits it depends on) and **withheld**
  (another lane's instruction; any producer's reasoning) · **output form** (a receipt; a ruling per
  claim) · **what its absence would miss** (CLAUDE.md §10's *"ask what N-1 would miss"*). A row whose
  absence misses nothing is struck, not kept for symmetry.

**Order.** A shared-reading row first (a batched `valoria-measure` where several rows need the same
mechanical numbers — a census, a size sweep; CLAUDE.md §10 *"share the reading; fork only the
judgment"*; a single lookup is not a row), then Phase 0 rows in item order, then Phase 1, then Phase 3.
Phase 2 and the accretion pass are the orchestrator's own and are not rows.

**Fans are decided here, not at dispatch** (the test is 5.2's). Two sub-parts, or two items, that name
the same file are a collision found at planning, where it costs a sentence: collapse to one producer.

**Recorded once, in the batch-open commit's body** (BATCH OPEN item 5) — one paragraph, no file,
ledger row or scratchpad note; the commit is its record and it dies with the range. It is **not an
approval stop**: it needs no confirmation, and an unattended driver is never blocked on it.

**Deviating.** A dispatch the plan does not list, or one that differs from its row (a producer
re-sized after a receipt, a lens added), is stated where it happens — the item's commit body, or
BATCH-CLOSE's report — with what the plan did not foresee. Re-planning the remaining rows is
permitted when a receipt shows the partition was wrong (state it in that commit); planning once and
then ignoring the plan is not.

---

## BATCHES — the unit of work, of verification and of context

**Whatever this skill is handed is a set of items, and the first thing done with it is to express it
as ordered batches.** A batch is three units at once: what is **built** together, **closed** together
(one BATCH-CLOSE), and **held in context** together.

### The partition — boolean intersection, not a headcount

Read each item's sets from its own content-owner entry (an ad hoc item: from the plan step 1 wrote,
which names them) — never guessed, never restated here:

- **edits** — what its WHERE writes;
- **gates** — what its GATE names (positions, decisions), any serial edge the plan states for it, and
  any item whose commit it needs. An ad hoc item's gates are those its plan names, or none.

Two items are **linked** when `edits(i) ∩ edits(j) ≠ ∅`, when `gates(i) ∩ gates(j) ≠ ∅` (the same
position or the same ruling), or when one gates on the other. What an item only *reads* goes into its
context set `C`: it decides what BATCH OPEN reloads, not which items share a diff. The **permanent
surface** links nothing, and is defined by kind, never by how many items name it: `CLAUDE.md`,
`CURRENT.md`, `HANDOFF.md` and the lane file, the plan's head, and the ledgers and registers every
position of the *plan* appends to (the hole register, the requirements register).

**By default a batch is a connected group of linked items**, ordered so every gate points from an
earlier item to a later one. Items with no link belong to different batches unless merged for a stated
reason; they commute, so the plan's order stands, or any order where there is none. Linked items read
and edit the same things, so they need one window, and their edits land in one diff where the batch's
reviewers see them together. A group may therefore be cut:

- **along any link, provided every cut link points forward** (the later batch's gates and files are
  met by the earlier batch's close and expunge having landed) and the cut is stated. Before cutting,
  name what carrying the whole group would risk (a long run with no verification checkpoint; a batch
  too large for Phase 1's fan or Phase 3's critique to hold); before not cutting, name what the cut
  costs (a re-read of shared files; an interaction only the joint diff shows). By judgment, never a
  fixed item-count.
- **Unlinked groups are kept apart or merged, by a stated reason either way.** Apart buys a cleared
  window and costs a full close each; merged saves a close and costs the union of their contexts, with
  nothing cleared between them.

### Where the batches live — follow whoever defined them; derive only what nobody did

**Sources, highest first; a lower source never overrides a higher one:**

1. **An in-flight row** (any session may have written it) — resume it (step 0).
2. **The live plan, and any scoped workplan it carves out by name** (CLAUDE.md §2: a carve-out's
   batches are its own and the plan schedules none of them). Recognise the forms plans actually write,
   and follow them as stated:
   - a **batch table or heading** (handle → positions, in dependency order) and a **`Batch` column**
     on a position table;
   - an explicit **boundary row** (`STOP. Batch N closes here`) — building stops there: BATCH-CLOSE,
     the boundary, the status line; the positions after it are the next batch;
   - a **gate that names a batch** (`GATE: Batch 1`) — met iff that batch's close has landed (BATCH
     OPEN item 3);
   - the plan's own **serial-edge and file-census tables** — they are the gates and edit sets, so
     derive nothing the plan states;
   - **per-batch discipline** the plan states (reading list, receipt, commit shape, tiers) — the
     plan's, and **below** CLAUDE.md and `methodology-close`: a plan-stated close, cadence or suite
     rule that differs from Phases 1–3, from the per-item rule here, or from CLAUDE.md §0.4 — lighter
     *or heavier* — is a conflict to state at the approval stop, never silently substituted and never
     silently adopted.
3. **Batch rows another agent or session left in the lane's handoff** for a task with no plan.
4. **A proposal or another agent's unratified plan** (`proposals/`, a delegate's report): input to the
   approval stop, presented and never adopted silently — a plan lives under `workplans/` (CLAUDE.md §2).
5. **Derived by the partition**, only where 1–4 are silent: present at the approval stop and, once
   approved, write into the plan that owns the positions or, for an ad hoc task with no plan, into the
   lane's `HANDOFF_<LANE>.md` Open table, one row per remaining batch (its items, files, gates); step 1
   reads both. That is an edit, committed with the in-flight row (BATCH OPEN item 5). A cleared window
   finds nothing else: no scratchpad file and no summary carries batch state across a boundary.

**The invocation text selects which batch to run; it never changes a batch's membership.** Text naming
a plan batch by its handle runs that batch. Text naming some but not all of one batch's positions, or
spanning batches, is stated at the approval stop: build the whole batch, or run a **partial batch** —
BATCH-CLOSE over just those items' range, the expunge removing just them; the plan's batch and its
boundary row stay.

Test every plan batch against the partition. A batch that gates on a later batch, or two of the plan's
own sources that disagree about a batch (a table against a column), is a conflict — say so at the
approval stop and leave the plan's grouping standing until it is ruled. Lumping more coarsely than the
partition would is the plan's judgment, not a conflict.

**A batch has ONE close (RULED, Jordan 2026-11-06: *"a batch is only supposed to have ONE close. if a
batch has multiple closes, then it is not a batch but a series of batches"*; *"methodology-execute
should only run the three-phase close once per batch"*).** A plan card that writes several closes
("close one", "close two") is a series of batches under one heading: this skill re-expresses its
remaining rows as batches of one close each, by the partition above, states the cut at the approval
stop, and runs the first; it never opens a second close inside a window. Each close repeats the fixed
Phase 1 and Phase 3 floor, the expunge and a merge wait. **A one-batch task writes no batch rows:** its
commits and its in-flight row are its record.

### THE CONTEXT SET — what each batch declares

A batch's **context set**, `C(k)`, is the reading list BATCH OPEN loads: its items' content-owner
entries, the files they edit and read, the registries their FALSIFIERS run against, the commits their
gates name, and the permanent surface. It is derived from the items' own entries — what *this* batch
needs. (A plan that keeps a per-batch reading list owns it.)

What persists across a boundary is the **intersection, `C(k) ∩ C(k+1)`** — in practice `CLAUDE.md` and
the user-level file, this skill and `methodology-close`, `CURRENT.md`, `HANDOFF.md` and the lane file,
the plan's head, and any registry both batches read. All of it is on disk, and a clear empties the
window's copy too, so BATCH OPEN reloads it: `C(k) \ C(k+1)` is never reloaded, `C(k+1) \ C(k)` is
newly loaded. **A fact one batch establishes and the next needs is not context, it is a dependency:**
it travels as a commit, a plan edit or a handoff pointer, and appears in the next batch's `C` as a
gate, never as a recollection. `valoria-author` is told the same: a fact worth keeping goes into the
artifact.

### THE IN-FLIGHT ROW — where a cleared window learns where the batch stands

While a batch is open, **one row in the Open table of the lane file its plan names** carries: the
batch handle, a pointer to the batch in the plan, **`open <sha>`** (`HEAD` before the batch-open
commit), **`built <handles>`** (each item's handle, appended **in that item's own commit**, which also
carries the trailer `Item: <handle>`, so a handle is listed if and only if its commit exists), and
**`close <none|1|2|3|final>`** (the last BATCH-CLOSE phase finished; `final` once `/close` has
committed). Handles and SHAs are ids and pointers, never a count or narrative (CLAUDE.md §1). In the
lane's three-column Open table (item | where it lives | next step): item `Batch <handle> — IN FLIGHT`;
where it lives, the batch's place in the plan plus `open <sha>`; next step, `built <handles> · close
<phase> · <what remains>`. For an ad hoc task with no batch row, the in-flight row is created whole
(items, files, gates, then these fields). **The expunge deletes the row with the batch: the ledger
exists only while the batch is open, which is why it is allowed** (CLAUDE.md §2 — a finished
position's record is its commit, not a mark).

---

## CHECKPOINTS AND BASELINES — Jordan's directive, 2026-10-09 (a container restart killed a running producer); CI cadence and baselines RULED 2026-10-13

**Checkpoints.** Work that exists only in a working tree is one restart from lost. At every producer
hand-back *before* verifying it, and before any long instrument run, the orchestrator commits a
checkpoint **on the producer's worktree branch** and pushes that branch: subject `[<scope>] WIP
checkpoint: <handle>` (CLAUDE.md §2's `[scope]` format, 72 characters at most, so keep the handle
short; "unreviewed" goes in the body), **no `Item:` trailer** (so the in-flight row never lists it; the
item's own commit is the verified merge, 5.3–5.4), trailers as any commit. Producers still never
commit — the orchestrator checkpoints. A checkpoint is recovery, not review, and starts no CI run
(*"A WIP checkpoint is just committing work so we don't lose it"*): BATCH-CLOSE reviews the whole
range, and a falsified attempt and its revert net to zero in that range (nothing to review; the hole
row is the record). A position its own falsifier rejects is committed with a `Falsified: <handle>`
trailer, then `git revert`ed, and the hole row cites both SHAs (the live plan's stopping rule). Dispatch
a long build in bounded pieces that return in tens of minutes, not one that returns in an hour. A
pre-commit validator that fails a checkpoint is fixed or reported, never bypassed with `--no-verify`.

**CI cadence — RULED 2026-10-13 (the session's user: *"we don't need a CI run for a WIP checkpoint ...
A WIP checkpoint is just committing work so we don't lose it"*; *"We run CI at the end of a batch,
correct whatever is required then, implement all fixes and changes and everything as per the closing
sequence, and then we run CI again to confirm that we successfully did it"*; *"we also don't need to
re-run an entire CI if we can tell from one season or two if something isn't working"*).** CI runs
twice per batch:

1. **At the end of the batch** — the push of its last `Item:` commit, which opens BATCH-CLOSE.
2. **To confirm** — the push of the branch's head after every fix, CI's and the closing sequence's
   have landed: the BOUNDARY's merge commit, or, where no merge is needed, the last fix commit. There
   is one confirming head. A red confirming run is fixed with the failing file only (CLAUDE.md §0.4
   cl.4), then pushed once more.

**CI needs a PR.** This repo's CI triggers only on a push to `main` or a pull request into it, so
neither run starts unless a PR is open for the branch: BATCH-CLOSE step 0 opens it if it does not
exist, and no other push starts a run. Where the first run's place falls among the closing phases is
`methodology-close`'s ("Where CI runs"). **Neither
result is waited for** (CLAUDE.md §11): consumed if reported when its step is reached, otherwise
unread and returned through the user.

Every other commit of the batch — the batch-open row commit, checkpoints, earlier `Item:` commits,
`Falsified:` commits and their reverts — carries `[skip ci]` in its message. GitHub reads it from the
HEAD commit of a push or a pull request, so what matters is that no other push's head commit lacks it.
Between the two runs, judge a change with the cheapest instrument that can see it — the covering test
file, or a one- or two-season probe — never a full CI run, and never CI to find what a probe already
shows. How many seasons a probe runs, and when `aperture 4 0` runs at all, is the live plan's
test-horizon rule.

**Baselines — RULED 2026-10-13 (the session's user: *"Every previously run CI is a baseline to use for
the next run CI, so we don't need to constantly take baselines since we've already ran a CI"*).** The
readings of the previous CI run, and the after-reading each item records since, are the baseline: a
baseline already held is not re-taken. Every reading names its SHA (`reading @<sha>`) and is recorded
in the first commit made after it completes (an item's, in its commit body); the next item's
before-reading is that record, and producers are *given* their before-readings, never asked to
re-derive them. Re-measure only when `git diff <sha>..HEAD` touches what the instrument can reach AND
the item cannot be judged without it; then re-measure at the reading's own season count (a 1-season
hash cannot vouch for a 4-season reading), while an error is seen at the first season it occurs. No
new document holds the readings (CLAUDE.md §1, §0.1 pt 5).

**Running a slow instrument** (the live plan's caps and horizons govern; the unit of cost is seasons,
not "one realm, one season", and it is superlinear in them).
1. *Size it.* Time two sizes on the axis that will scale (1 and 2 seasons), fit the growth, extrapolate
   with a margin, and divide the CPU estimate by the CPU share the machine will give it. If the
   estimate exceeds the tool's background maximum, split the run (storybar by seed; re-merge the pooled
   rows only after checking the merge) or cap it: Jordan 2026-10-10, storybar at 3 realms.
2. *Launch.* `exec python -u … > log 2>&1`, so `$!` is python and not a wrapper shell; in the same call
   write `$!` and `ps -o lstart= -p $!` to a pid file; a reading counts only if the log ends with an
   `EXIT 0` line a wrapper appends. Export the same `PYTHONHASHSEED` to every process of a comparison.
   Parallel budget: `max(1, nproc - round(load average))`; the instruments are single-threaded, and
   producers' `pytest -n auto` already holds every core.
3. *Judge it.* CPU time (`ps -o cputime`) advancing separates a working process from a blocked one; it
   cannot separate a long run from a livelock, and these instruments print only at the end. The
   backstop is the size estimate: a process past 3x its estimate is examined, not assumed dead. Before
   trusting a PID, check `/proc/<pid>/cmdline` and the start time still match. `Monitor` (CLAUDE.md
   §11, allowed for local jobs) may watch the log and CPU time.
4. *Find it.* `pgrep -f '^python -m engine.season.harness.<name>'`, anchored: an unanchored or
   bracketed pattern matches the `bash -c` wrappers too. Never `pkill -f` from a shell whose own
   command line names the pattern.
5. *Say so.* State the measured runtime in the producer brief. Use the shell's `time`; `/usr/bin/time`
   is absent. A limit that kills a run is a measurement failure, reported as one, never read as a
   result.

## GUARDRAILS

- **Phase 0 is additive, never a substitute** (see Cadence).
- **Nothing crosses a boundary but the tree.** A receipt, a finding, a SHA or a decision that is not in
  a commit, the plan, the handoff or the permanent surface does not exist for the next batch; if the
  next batch needs it, the partition missed a link — add the link or write the fact down, never
  reconstruct it from memory. No scratchpad file or summary carries state between batches. (Auto
  memory, where enabled, loads in every fresh process: fresh context, not fresh memory — treat it as
  permanent surface and put nothing batch-specific in it.)
- **Expunge deletes; it keeps no log of its own.** A "batch k done" row, count or narrative that the
  plan's own rule for finished positions does not prescribe is the growth CLAUDE.md §1 forbids; the
  only state this skill keeps is the in-flight row, and only while its batch is open.
- **The assignment plan is a paragraph in a commit body**, never a file, ledger row or scratchpad note.
- **No new roster entry.** Phase 0 dispatches `valoria-author`; BATCH-CLOSE dispatches
  `valoria-critic`, exactly as `methodology-close` does; `valoria-measure` where the plan names a
  shared reading.
- **Nothing here is a fixed count.** Producer-fan size, agonist-fan size and batch size are each read
  from the instruction (or the batch) at hand every time.
- **No self-scheduling** (CLAUDE.md §11, as always).
- **Produces edits, not documents.** No directory beyond `skills/methodology-execute/`, no findings
  file, no build log kept past the receipts Phase 0's producers already returned.

## FALSIFIERS

| the claim | what would show it false |
|---|---|
| "the agent assignments were planned at batch open" | a producer was dispatched before the batch-open commit existed (it precedes the first `Item:` commit in `git log`); or a dispatch ran, at Phase 0 or BATCH-CLOSE, that the plan neither lists nor defaults to, with no deviation stated; or two sub-parts or items of the plan share a file and the plan did not collapse them to one producer; or a critic row sets a tier or effort `methodology-close` fixes differently |
| "one producer was enough" | the instruction itself named independent, file-disjoint sub-parts, and only one dispatch ran with no stated reason to collapse them |
| "the build matched the instruction" | the produced diff's scope is broader or narrower than the instruction's own `WHERE`, or silently substitutes a different fix for the one named — what BATCH-CLOSE's FIDELITY TO PLAN lens exists to catch; if it passed anyway, name why |
| "fanned lanes integrated cleanly" | 5.3's merge resolved a same-file collision instead of stopping and rebuilding that file as one producer |
| "the gate was met before building" | an item's gate (a workplan `GATE`, or the gates an ad hoc plan names) named a position or a Jordan decision that had not actually landed |
| "the batches were partitioned, not sized" | an item's gate is met only by a later batch, or a link was cut with no stated reason |
| "the batch size was right" | a linked group was carried whole through BATCH-CLOSE with no stated reason not to cut it along a link, or was cut with no stated reason the whole group would have been too large (a plan's own cut: stated at the approval stop) |
| "the plan's batches and boundaries were followed" | a batch, boundary row, batch-named gate or carve-out that a plan defines was re-derived, re-split, merged or crossed (building ran past a `STOP … closes here` row without BATCH-CLOSE) with no conflict stated at the approval stop; or a plan-stated close or suite rule was adopted over `methodology-close` or CLAUDE.md §0.4, or overridden, without that statement |
| "the context was cleared at the boundary" | the next batch's work cites a receipt, finding, SHA or fact that is neither on disk nor in the permanent surface; or two batches ran in one window and the report did not say context was NOT cleared |
| "the expunge took only what no remaining batch needs" | after the boundary commit, a remaining batch's gate or reading list names a handle or file that is gone from the tree, with no landing SHA written in its place |
| "the batch was expunged" | a finished position, or its in-flight row, is still present after the boundary commit, or that commit added a narrative, a "done" row or a count beyond what the plan's own rule for finished positions prescribes |
| "the batch resumed from its row" | a resumed batch rebuilt an item whose handle was in `built`, skipped one that was not, re-ran a BATCH-CLOSE phase at or before `close`, overwrote `open`, or trusted the row over the commits where they disagreed |
| "BATCH-CLOSE ran once per batch" | the full pytest suite, `/code-review`, `/simplify`, `layer-conformance`, the agonist/antagonist fan, or the terminal critique ran between two items of the *same* batch, or the review phases did not run before the batch's items were reported done (the suite runs per CLAUDE.md §0.4 cl.1, not unconditionally) |
| "CI ran twice per batch" | a CI run started on a commit other than the batch's last `Item:` commit or the confirming head (a pushed head commit without `[skip ci]`), no PR existed when the first run was due, or a full CI run was used to find what a covering test file or a one- or two-season probe could show |
| "the accretion pass ran" | a tool or test file in the batch's added list has no stated caller or observed behaviour and was neither deleted nor given a stated reason; or the pass ran after Phase 3; or it added a file, row or document rather than deleting one |
| every Phase 1–3 claim, at BATCH-CLOSE | `methodology-close`'s own falsifier table, unchanged, checked against the batch's cumulative post-Phase-0 diff |

**If this skill's guidance conflicts with `CLAUDE.md`, `architecture/`, or `methodology-close`, they
win.** This file and `methodology-close` are methods; those are the rules, and `methodology-close` is
the senior method where the two overlap.
