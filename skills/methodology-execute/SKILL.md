---
name: methodology-execute
description: >
  METHODOLOGY-EXECUTE — invoked as `/methodology-execute <free-text task>` (e.g.
  `/methodology-execute build out governance branch for faction`), build every item a task or
  workplan area names, THEN verify once per batch rather than once per item. EVERY task,
  assignment or workplan is first expressed as ordered BATCHES — items linked by a shared edit or a
  gate are one batch by default (a plan's, or a carved-out workplan's, own batches, boundary rows
  and batch-named gates are followed as stated; grouping is derived only where nothing defines it) — and a batch is the unit of CONTEXT as well as of verification: when it closes
  its finished positions are deleted from the plan and the next batch opens as a session opens,
  carrying only what the two batches' context sets have in common (their intersection; everything
  else is cleared, never summarised). PHASE 0.1: resolve
  the free text against the live workplan first — one matching position with its GATE already met
  proceeds straight through; more than one matching position, or none at all, STOPS and presents
  the resolved sequence (or the freshly-stated plan) for approval before anything is built, per
  CLAUDE.md §0's "ambiguous or spanning lanes" rule. PHASE 0.2+: read each item's own instruction
  (a workplan position's content-owner entry, or the stated plan for an ad hoc task) and dispatch a
  `valoria-author` producer to build it — one producer by default, fanned into
  `isolation: worktree` lanes only when the instruction itself names independent sub-parts with no
  shared file — then commit. **No test, validator, forward sweep or skill after each
  item** (no suite, `/code-review`/`/simplify`/`layer-conformance`, agonist/antagonist fan or
  terminal critique) — all of it is BATCH-CLOSE's job, not Phase 0's, run once per batch (§BATCHES) or at the run's own final
  `/close`, never per item.
  BATCH-CLOSE: `methodology-close`'s full Phases 1–3, run once against the batch's commit-range
  diff (its recorded starting SHA through HEAD, since every item already committed) — invoked
  verbatim, not copied here. Use for: "run methodology-execute",
  "/methodology-execute <task>", "build out this phase/area", a workplan position, phase, or
  free-text area of work that has not been built yet and needs both building and verifying before
  `/close`. Not for: a diff that already exists and only needs verifying — use `methodology-close`
  directly; design-quality grading (`ners`); a target that resolves by a draw
  (`resolution-diagnostic`); Layer placement alone with no build to do (`layer-conformance`
  directly).
---

# METHODOLOGY-EXECUTE — build, then close

## Created 2026-09-29, split out of `methodology` (now `methodology-close`) per Jordan's directive that the pipeline also orchestrate the build, not only verify one already built. Revised 2026-10-06 per Jordan: a batch is a partition by shared files and gates, and the unit of context — finished batches are deleted from the plan and cleared from the window before the next opens. Invocable as a project skill through the symlink `.claude/skills/methodology-execute`.

## What this skill owns, and what it copies

| the content | its single owner |
|---|---|
| the build phase — dispatching the producer(s) that write the diff a unit of work specifies, sizing the fan, and integrating parallel write lanes | **this file** |
| batching — the partition of items into batches, each batch's context set, where the boundary falls between many cheap BUILDs and one BATCH-CLOSE, and what is deleted and cleared between batches | **this file** — except a plan's own batch structure where it has one, which is the plan's (§BATCHES) |
| the status line every invocation ends with, and the `approved:` prefix | **this file**; `tools/methodology_drive.py` reads and writes them by that spelling and defines neither |
| deleting a finished position from the plan | **CLAUDE.md §2** (*"Finished positions leave the plan; the commit is their record"*); this file adds the pre-deletion reference check and says when (§BATCH BOUNDARY) |
| the sequence, tiers, checklists, the handshake, the guardrails and the falsifiers for verifying the resulting (batch) diff | **`methodology-close`**, invoked by reference — not copied |
| the producer contract — full toolset, a receipt not a transcript, no commit, no full-suite mid-lane | **`.claude/agents/valoria-author.md`** |
| model tiers, the effort ladder, and the fan-out sizing rule ("ask what N-1 would miss") | **CLAUDE.md §10** |
| the tier and effort of each BATCH-CLOSE dispatch | **`methodology-close`** (§1.3, §1.4, §3.2); this file sets Phase 0's only (§0.3) |
| a workplan position's INSTRUCTION / WHERE / FALSIFIER / GATE | **that position's own content-owner file** — never re-derived or restated here |

**Word discipline, inherited, not re-opened.** `methodology-close` defines *agonist* and
*antagonist* narrowly as read-only review roles, run on `valoria-critic`, and states that the
definition "does not travel forward into `methodology-execute`'s build phase." This file honours
that: every Phase 0 dispatch is `valoria-author`, a **producer**, and is never called agonist or
antagonist. When a build is fanned, the orchestrator's merge step is called the **integrator** —
a third word, not a stretch of either of the first two. Three roles, three words, each read cold
the same way every time, per CLAUDE.md §4.

**Relation to `methodology-close` and to `/close`.** This skill's BATCH-CLOSE *is*
`methodology-close`'s Phases 1–3, unmodified. A change to that sequence is made once, in that
file. This skill adds exactly one thing ahead of it: a phase that writes the diff, for when one
does not exist yet — and it changes *when* the closing phases fire, not what they do.

**Per Jordan's rulings — the split from `methodology-close`; 2026-10-06, *"code review and simplify to
be at batch close"*; 2026-10-07, *"everything is to occur at batch close rather than per step when it
comes to validation and skills etc"* — an item gets a build and a commit, and nothing else.** No
test, validator, forward sweep or skill runs after it: not the agonist/antagonist fan,
`/code-review`, `/simplify`, `layer-conformance` or the terminal critique, and not the covering test
file, the lane validator, `tools/valoria_local.py --staged`, the plan's forward sweep or the suite.
All of it runs once per batch, at BATCH-CLOSE. The live plan's per-step cadence (its §0.4, ruled
2026-09-18: one step is one position and one commit, with `/code-review`, `/simplify` and a forward
sweep at each step's end) is written for a session working one position by hand; the plan's §0.4,
§0.5 and §O.4 carry the supersession. `methodology-execute` orchestrates many items in one run, and
re-running that cadence per item is the over-fanning CLAUDE.md §10 warns against, plus the "full
suite is a close step, not an inner loop" mistake CLAUDE.md §0.4 already forbids. Every item still
gets its own commit; the review, validation and test cost is deferred to BATCH-CLOSE, below. This
is a named, deliberate scoping — not a silent departure from the per-step cadence, and not licence
to skip BATCH-CLOSE itself. (CLAUDE.md §0.4 cl.2 permits a mid-session run of the covering test
file; under this skill that permission is not taken up.)

---

## THE SHAPE OF A RUN: BATCHES, EACH MANY CHEAP ITEMS AND ONE EXPENSIVE PASS

```
  BATCH k    OPEN ──▶ item 1 ──▶ PHASE 0 · BUILD ──▶ commit ─┐
  (as a      (orient  item 2 ──▶ PHASE 0 · BUILD ──▶ commit ─┼─▶ BATCH-CLOSE (once per batch):
  session    from        ⋮  (repeats for every item)         ┘     PHASE 1 · AGONIST FAN → ANTAGONIST
  opens)     disk)                                                 PHASE 2 · MECHANICAL GATES (+ the one suite run, CLAUDE.md §0.4)
                                                                   PHASE 3 · TERMINAL CRITIQUE
                                                                          │
                                                          EXPUNGE ◀───────┘  (delete the batch from the plan)
                                                              │
       BOUNDARY — reload C(k) ∩ C(k+1) from disk · never reload C(k) ∖ C(k+1) · load C(k+1) ∖ C(k)
                                                              │
  BATCH k+1  OPEN ──▶ …
```

**Phase 0 repeats per item; BATCH-CLOSE does not.** Each item is one producer and one commit,
and nothing else: no test, validator, sweep or skill. Everything that checks — the agonist/antagonist
fan, `/code-review`→`/simplify`→`layer-conformance`, the plan's forward sweep and validators, the
covering test files, the suite, and the terminal critique — fires once, against every item's cumulative diff since the last BATCH-CLOSE, at a batch boundary
(§BATCHES) or at the run's own final `/close`. **A batch is also the unit of context:** nothing a
finished batch built, read or found is carried into the next except what the two have in common
(§BATCH BOUNDARY).

This is additive sequencing, not a lowered bar: a producer's own confidence that it built an item
correctly is not evidence of that, which is exactly why BATCH-CLOSE's Phase 1 exists — it is
deferred, not skipped. Reporting a run "closed" when only Phase 0 ran for its items is the same
false claim `methodology-close`'s own falsifier table already catches for a single diff, now
scoped to a batch.

---

## PHASE 0 · BUILD

### 0.1 SCOPE — resolve the invocation's free text before touching anything

`/methodology-execute <task>` hands this skill free text (e.g. *"build out governance branch for
faction"*), not a position handle. A vague area of work is not one buildable unit, and this file
does not guess which unit was meant.

1. **Search the live workplan first.** Run `/currency` and follow `CURRENT.md` to whichever
   document it names as the live plan — this file does not name that document itself, because a
   filename written here would be exactly the stale pointer `CLAUDE.md` §1 exists to prevent. Check
   that document, any scoped workplan it carves out by name (CLAUDE.md §2), and the lane's
   `HANDOFF_<LANE>.md` Open table (where an ad hoc task's batches and any in-flight row live), for
   a position whose handle or `what runs` plausibly matches the text.
2. **Classify what the search found.** **Text beginning `approved:`** means a person already
   approved the sequence the "more than one position" stop below would present (an interactive
   first run, or a driver's operator passing `--approved`). It skips **only that stop**: the gate
   checks, the in-flight check and every other `STOPPED` condition of §THE STATUS LINE still apply.
   **It never licenses a new task:** finished positions are expunged, so `approved:` text that
   matches nothing now is `STOPPED` (*finished, or the plan changed*) — otherwise a re-run after the
   last expunge would rebuild the work. An optional trailing `[next: <handle>]` (a driver copies it
   from the previous `NEXT` line) fixes the batch to run: if the plan's next batch is not that
   handle, `STOPPED`.
   - **Exactly one position, `GATE` already met, and it is a whole batch of its own (not part of a
     larger plan batch)** — proceed straight to 0.2 with that position's content-owner entry. No confirmation needed: the position's own gate already establishes it
     is buildable now, and building it is exactly what was asked.
   - **More than one matching position** — a free-text area of work ("governance branch for
     faction") will usually name a *cluster*, not one step. Resolve the ordered subsequence
     (respecting each position's own `GATE`), then **stop and present the resolved sequence —
     handles, in order, any unmet gate flagged — before building anything.** This is CLAUDE.md
     §0's own rule, not a new one: *"Anything ambiguous or spanning lanes: get the plan approved or
     ask a focused question."* Naming a whole area of the plan is exactly that case.
   - **No matching position** — a genuinely new, unplanned task. Write the plan per
     `methodology-close` §1.1 / CLAUDE.md §0's first bullet (what changes, in what order, how you
     will verify) and **stop and present it for approval**, unless the task is small enough that a
     one-sentence plan already fully states it and CLAUDE.md §0 lets that stand alone.
3. **Express the resolved sequence as batches** — §BATCHES: the plan's own, where it has them;
   otherwise derived, and presented in the same stop as the sequence, so one approval covers both.
   The single-position case is a one-item batch and needs no confirmation. **Once the batches are
   confirmed, take them in order: for each, BATCH OPEN, then 0.2 onward once per item**
   — one BUILD → integrate → commit per item (the commit carries the `Item: <handle>` trailer, the in-flight
   row's update, and the producer's receipt in its body, `NOT DONE` included) — **then BATCH-CLOSE, then the BATCH BOUNDARY.**
   **Never one diff spanning several items**: each item keeps its own commit, the one part of
   the per-step cadence this skill does not defer (see "What this skill owns" above).
   If a later queued item's `GATE` turns out unmet when its turn comes (something outside this
   run's scope, or a `JORDAN` item), **stop there and report it** (`STOPPED`, §THE STATUS LINE) — do not skip it silently and continue to the next, and do not run BATCH-CLOSE on a batch
   that stopped short without saying so.

### 0.2 Read the unit's instruction — never invented here

Whichever way 0.1 resolved it, take one unit of work at a time:

- a **workplan position** — read its content-owner entry (INSTRUCTION / WHERE / FALSIFIER / GATE)
  in full before dispatching anything; or
- an **ad hoc task** with no workplan position — the instruction is the plan 0.1 step 2 just had
  you write (or the user's own one-sentence statement, if that already sufficed).

Either way, that instruction **is** the plan Phase 1 will check fidelity against. Do not restate
it, paraphrase it, or draft a second version for the producer — hand it the same text you read.

### 0.3 Size the build — one producer is the default

Dispatch one `Agent({ subagent_type: "valoria-author", model: ..., effort: ..., ... })` to build the
entire instruction, sequentially. **Set `model` and `effort` on every dispatch** — an un-annotated
producer inherits the session's model (CLAUDE.md §10), and a line of prose in the prompt sets no
effort. **Model:** the item's own `tier` where the plan carries one; otherwise `sonnet`. `haiku` for
deterministic work (find-replace, a deletion, a re-host, a transcription); `opus` only where the
instruction names a competing-considerations judgment (design intent, contract closure).
**Effort:** `medium`; `high` only for an `opus` item. The orchestrator that reads receipts and
commits needs no more than sonnet-class: a driver passes `--model` and `--effort` after its `--`. No `isolation: worktree` is needed for a single producer — nothing else is writing
this tree concurrently within this run.

**Fan only when the instruction itself names genuinely independent sub-parts that share no file**
— the same test the live plan's own hard-serial-edge table (reached through `CURRENT.md`) exists to
catch. Never fan by default, and never size the fan to "how many
files changed" alone — CLAUDE.md §10: *"before spawning N agents, ask what N-1 would miss."* Most
workplan positions are one commit, one step, one producer.

When fanned:

- each producer runs `isolation: worktree`, and is handed **only its own sub-part's instruction**,
  never the others' — the same "handed output, not reasoning" discipline Phase 1 uses to keep
  critics independent, applied here to keep parallel write lanes from cross-contaminating;
- each returns a receipt — path, what changed, one line — `valoria-author`'s own contract, so a
  long build never crosses the orchestrator's window;
- fire the first dispatch alone, wait for its first streamed token, *then* send the rest in one
  message — CLAUDE.md §10 point 3, the same cache-priming step `methodology-close` §1.3 uses for
  its agonist fan.

**Either way — one producer or several — the producer never commits** (0.5); that is always the
**orchestrator's** own next action once a receipt (or, when fanned, 0.4's integration) is in hand.
The default, single-producer path has no worktree to merge, so it skips 0.4 and goes straight from
receipt to the orchestrator's commit.

### 0.4 Integrate — only when fanned

The **orchestrator**, not a subagent, merges each worktree into the working branch, in an order
that respects any named serial edge between the sub-parts, **then commits.** **If two lanes touched
the same file, the split was wrong, not the merge** — stop, do not resolve the collision by hand,
and rebuild that file's portion as one producer instead. A silent auto-merge of a same-file
collision is exactly the failure the `FALSIFIERS` table below is written to catch.

### 0.5 What this phase must not do

- **Never review or validate its own output.** The dispatch prompt tells `valoria-author` to write
  the edit, return its receipt, and run no test, validator or sweep: its own file otherwise says to
  run the covering test file, and that run is BATCH-CLOSE's here (Jordan, 2026-10-07). Phase 0 is
  not Phase 1's independent fidelity check and does not attempt to be one.
- **Never commit, and never run the full suite mid-lane** — `valoria-author`'s own file already
  forbids both; this skill adds no exception.
- **Never skip 0.1's gate check** because the instruction "looks buildable" — a position gated on
  another position or on Jordan is not this skill's to build around by reinterpreting its own gate.

---

## BATCHES — the unit of work, of verification and of context

**Whatever this skill is handed — a workplan area, a cluster of positions, an ad hoc task — is a
set of items, and the first thing done with it is to express it as ordered batches.** A batch is
three units at once: what is **built** together, what is **closed** together (one BATCH-CLOSE),
and what is **held in context** together. A single position or a one-sentence task is a one-item
batch, not an exception to the rule.

### The partition — boolean intersection, not a headcount

Read each item's sets from its own content-owner entry (an ad hoc item: from the plan 0.1 wrote,
which must name them) — never guessed, never restated here:

- **edits** — what its WHERE writes;
- **gates** — what its GATE names (positions, decisions), any serial edge the plan states for it,
  and any item whose commit it needs.

Two items are **linked** when `edits(i) ∩ edits(j) ≠ ∅`, when `gates(i) ∩ gates(j) ≠ ∅` (a common
dependency: the same position or the same ruling), or when one gates on the other. What an item
only *reads* — a falsifier's instrument, a registry — goes into its context set `C`, below: it
decides what BATCH OPEN reloads, not which items share a diff. The **permanent surface** links nothing,
and is defined by kind, never by how many items name it (in a two-item run every shared file is
named by every item): `CLAUDE.md`, `CURRENT.md`, `HANDOFF.md` and the lane file, the plan's head,
and the ledgers and registers every position of the *plan* appends to (the hole register, the
requirements register).

**By default a batch is a connected group of linked items**, ordered so every gate points from an
earlier item to a later one. Items with no link belong to different batches unless merged for a stated reason (below); they
commute, so the plan's order stands, or any order where there is none.

Why: linked items read and edit the same things, so they need one window, and their edits land in
one diff where the batch's reviewers see them together. The second reason is the weaker one —
`methodology-close`'s INTERDEPENDENCIES greps the *whole* tree (§3.4), so a later batch's close
still sees earlier landed work — which is why a group may be cut:

- **A group may be cut along any link, provided every cut link points forward** (the later batch's
  gates and files are met by the earlier batch's close and expunge having landed) and the cut is
  stated. Before cutting, name what carrying the whole group would risk (a long run with no
  verification checkpoint; a batch too large for Phase 1's fan or Phase 3's critique to hold);
  before not cutting, name what the cut costs (a re-read of shared files; an interaction only the
  joint diff shows). By judgment, never a fixed item-count.
- **Keep unlinked groups apart or merge them, by a stated reason either way.** Apart buys a cleared
  window and costs a full close each; merged saves a close and costs the union of their contexts,
  with nothing cleared between them.

### Where the batches live — follow whoever defined them; derive only what nobody did

**Sources, highest first; a lower source never overrides a higher one:**

1. **An in-flight row** (any session may have written it) — resume that batch (§The in-flight row).
2. **The live plan, and any scoped workplan it carves out by name** (CLAUDE.md §2: a carve-out's
   batches are its own and the plan schedules none of them). Recognise the forms plans actually
   write, and follow them as stated:
   - a **batch table or heading** (handle → positions, in dependency order) and a **`Batch` column**
     on a position table;
   - an explicit **boundary row** (`STOP. Batch N closes here`) — building stops there:
     BATCH-CLOSE, the boundary, the status line; the positions after it are the next batch;
   - a **gate that names a batch** (`GATE: Batch 1`) — met iff that batch's close has landed (BATCH
     OPEN item 3);
   - the plan's own **serial-edge and file-census tables** — they are the gates and edit sets, so
     derive nothing the plan states;
   - **per-batch discipline** the plan states (reading list, receipt, commit shape, tiers) — the
     plan's, and **below** CLAUDE.md and `methodology-close`: a plan-stated close, cadence or suite
     rule that differs from Phases 1–3, from this skill's per-item rule, or from CLAUDE.md §0.4 —
     lighter *or heavier* — is a conflict to state at the 0.1 stop, never silently substituted and
     never silently adopted. (`/code-review` and `/simplify` at batch close is RULED — Jordan,
     2026-10-06 — so a plan still asking for them per step is stale on that point, not a conflict.)
3. **Batch rows another agent or session left in the lane's handoff** for a task with no plan.
4. **A proposal or another agent's unratified plan** (`proposals/`, a delegate's report): input to
   the 0.1 stop, presented and never adopted silently — a plan lives under `workplans/` (CLAUDE.md §2).
5. **Derived by the partition**, only where 1–4 are silent: present at the 0.1 stop and, once
   approved, write into the plan that owns the positions or, for an ad hoc task with no plan, into
   the lane's `HANDOFF_<LANE>.md` Open table (lane work lives in its lane file), one row per
   remaining batch (its items, files, gates); 0.1 step 1 reads both. That is an edit, in the commit
   that opens the first batch. A cleared window finds nothing else: no scratchpad file and no
   summary carries batch state across a boundary.

**The invocation text selects which batch to run; it never changes a batch's membership.** Text
naming a plan batch by its handle runs that batch. Text naming some but not all of one batch's
positions, or spanning batches, is stated at the 0.1 stop: build the whole batch, or run a
**partial batch** — BATCH-CLOSE over just those items' range, and the expunge removing just them;
the plan's batch and its boundary row stay.

Test every plan batch against the partition. A batch that gates on a later batch, or two of the
plan's own sources that disagree about a batch (a table against a column), is a conflict — say so
at the 0.1 stop and leave the plan's grouping standing until it is ruled. Lumping or splitting
more finely than the partition would is the plan's judgment, not a conflict. This skill does not
re-split a plan on its own authority. **A one-batch task writes no batch rows:** its commits and its
in-flight row are its record.

### The context set — what each batch declares

A batch's **context set**, written `C(k)`, is the reading list BATCH OPEN loads: its items'
content-owner entries, the files they edit and read, the registries their FALSIFIERS run against,
the commits their gates name, and the permanent surface. It is derived from the items' own entries
— what *this* batch needs, not what the last one happened to read. (A plan that already keeps a
per-batch reading list owns it.)

What persists across a boundary is the **intersection, `C(k) ∩ C(k+1)`** — in practice `CLAUDE.md`
and the user-level file, this skill and `methodology-close`, `CURRENT.md`, `HANDOFF.md` and the
lane file, the plan's head, and any registry both batches read. All of it is on disk, and a clear
empties the window's copy too, so BATCH OPEN reloads it: the intersection is what is *certain to be
reloaded*, `C(k) \ C(k+1)` is what is never reloaded, `C(k+1) \ C(k)` is what is newly
loaded. **A fact one batch establishes and the next needs is not context, it is a dependency:** it travels as a commit, a plan edit or a handoff pointer — already
on disk — and appears in the next batch's `C` as a gate, never as a recollection.
`valoria-author` is told the same: a fact worth keeping goes into the artifact.

### The in-flight row — where a cleared window learns where the batch stands

While a batch is open, **one row in the Open table of the lane file its plan names**
(`registers/handoffs/HANDOFF_<LANE>.md` — CLAUDE.md §2's place for mid-task state) carries:
the batch handle, a pointer to the batch in the plan, **`open <sha>`** (`HEAD` before the first
item), **`built <handles>`** (each item's handle, appended **in that item's own commit**, which also
carries the trailer line `Item: <handle>`, so a handle is listed if and only if its commit
exists), and **`close <none|1|2|3|final>`** (the last BATCH-CLOSE phase finished, `final` once `/close` has
committed; **each phase's end updates the row, in a commit of its own if the phase edited nothing**
— a clean phase leaves no other mark, and a resume would re-run it). Handles and
SHAs are ids and pointers, never a count or narrative (CLAUDE.md §1). In the lane's three-column Open table (item | where it lives | next step):
item `Batch <handle> — IN FLIGHT`; where it lives, the batch's place in the plan plus `open <sha>`;
next step, `built <handles> · close <phase> · <what remains>`. For an ad hoc task with no batch
row, the in-flight row is created whole (items, files, gates, then these fields).
**The expunge deletes the row with the batch: the ledger exists only while the batch is open,
which is why it is allowed (CLAUDE.md §2 — a finished position's record is its commit, not a mark).**

**Resuming.** If the lane's Open table already holds an in-flight row, that batch is the one to
continue — the first check of any invocation, ahead of 0.1's classification. Build only the items not in `built`,
run BATCH-CLOSE from the phase after `close`, and take `open` as the batch's starting commit. **Check
the row against the tree before trusting it:** every `built` handle must have a commit in
`open..HEAD` carrying `Item: <handle>`, and every such trailer there must be in the row; where
they disagree, the commits win — correct the row and say so; if they cannot be reconciled, ask.
**Then look at the tree:** a killed run leaves residue. If `git status` is dirty, it is the killed
item's partial build — report its paths, `git stash push -u` it (reversible) and rebuild the
item; never commit it unreviewed. `git worktree list` shows fan lanes left behind: integrate or
remove each. **A position the plan or handoff already records as BUILT with its close not run** enters at
BATCH-CLOSE: write the row with `built` filled and `open` the range start that record names; if it
names none, ask. An invocation whose text does not match an in-flight batch stops and reports
it (`STOPPED`); it never opens a second batch.

### BATCH OPEN — orient as a session opens

1. **Establish currency:** `/currency`, then the lane's handoff and the plan's rows for this batch
   only (CLAUDE.md §0's first bullet).
2. **Load this batch's context set from disk**, the overlap with the last batch included. Do not
   rely on having read it.
3. **Check every item's gate against the tree**, never an earlier window's belief that it landed.
   By gate kind: a **SHA** is met iff `git merge-base --is-ancestor <sha> HEAD`; a **position** is
   met iff the plan no longer holds it and its landing SHA is written in the gate, or the plan's
   own status vocabulary marks it landed with the evidence named — a position recorded BUILT with
   its close not run is **not** landed; a **batch** is met iff its close landed (its rows gone or
   marked closed by the plan's own rule, its closing SHA in the gate and an ancestor of `HEAD`); a
   **ruling or decision** is met iff the ledger row that owns it (`registers/`, last row governs)
   records it resolved. A gate of none of these kinds is unmet — `STOPPED`.
4. **Record the starting commit — `HEAD` — in the in-flight row (below), in the first item's own
   commit.** Every item commits at once (0.1 step 3), so when BATCH-CLOSE runs the tree is clean
   and there is no uncommitted diff. The batch's diff is the **commit range from that SHA to `HEAD`** (`git diff <batch-start-sha>..HEAD`
   for the content; `/code-review`'s own branch/PR-target mode, not its bare "current diff" mode,
   for the dispatch itself), and BATCH-CLOSE hands every phase that range. `valoria-critic` holds
   only Read, Grep and Glob and cannot run `git diff`: write the range's diff to a scratchpad file
   and hand the critics its path.

### Share the reading — once per batch, on Haiku

After BATCH OPEN's reads, one `valoria-measure` dispatch (Haiku) extracts the batch's reading list into
a table, handed to every producer so none re-opens the same files (CLAUDE.md §10 pt 1: the cost of a
fan-out is its reading). Fire one producer, await its first token, then the rest (§0.3). The extract
is a claim the producer checks where it edits, not a verdict.

### The last batch is also the run's `/close`

When the resolved sequence is exhausted, BATCH-CLOSE is followed by `/close` itself (its suite step
is BATCH-CLOSE's, not run twice — lane validator, commit, handoff), per that skill's own
definition, and **then** the BATCH BOUNDARY's expunge. The order is deliberate: the in-flight row is
deleted by the expunge, so it is the last thing to go and a death anywhere earlier — the long
suite-running stretch included — still resumes from the row. A mid-run boundary does not invoke
`/close`; it runs BATCH-CLOSE, then the BATCH BOUNDARY.

---

## BATCH-CLOSE · PHASES 1–3, ONCE PER BATCH, BY REFERENCE

Run `methodology-close`'s Phases 1 through 3 **once**, against the **commit-range diff** BATCH OPEN
had you record (`<batch-start-sha>..HEAD`) — not against any single item's diff alone, and not
against a working-tree diff, since nothing is left uncommitted by the time a batch ends.

- Its **Phase 1 precondition** ("there must be a plan to check fidelity against") is satisfied by
  the batch's own instructions taken together — the plan's stated scope for the batch; the union of
  whichever positions 0.1 resolved into it, even if they span more than one of the plan's named
  phases; or the concatenation of the ad hoc instructions 0.2 read for each item in the batch.
  FIDELITY TO PLAN now means fidelity to *that*, not to one item's `WHERE` in isolation.
- Its **fan sizing, dispatch order, cache-priming step, and reconciliation** (§1.2–1.5) apply as
  written there, sized to the batch's own independent parts — which will usually be larger than a
  single item's, since a batch holds several items' worth of change.
- Its **Phase 2 order and apply-before-next-reads discipline** (§2.1–2.4) apply as written there,
  against the batch's full cumulative diff. **The test suite is CLAUDE.md §0.4's, not
  `methodology-close`'s:** it runs at most once per batch, here, and only if it can observe
  something CI will not (cl.1), over only the files and suites the batch's diff can reach (§0.4's
  closing paragraph); a
  batch of prose or ledger edits runs just the files that read what it touched. No item inside the
  batch runs it.
- **Plan-defined per-step validation, moved here.** What a plan asks of every step beyond BUILD and
  commit — its forward sweep, its lane validator, `tools/valoria_local.py --staged`, a covering
  test file — runs once here over the batch's range, after Phase 2 and before Phase 3, so Phase 3
  sees any fix it forces. The plan's own definition of each check governs what it is; this skill
  only moves when. A falsifier that fails here follows the plan's own stopping rule for that
  position.
- Its **Phase 3 tier, checklist, and the top-down/bottom-up handshake**
  (§3.1–3.7) apply as written there, run against the batch's post-Phase-2 diff. INTERDEPENDENCIES
  and the FORWARD/BACKWARD SWEEPS are more likely to find something real here than at single-item
  scale, precisely because several items have now landed together — that is the case BATCH-CLOSE
  exists to catch that per-item verification would have missed one item at a time.

Nothing in this section is restated in full here; a change to any of it is made once, in
`methodology-close`.

---

## BATCH BOUNDARY — expunge, then clear

Runs after BATCH-CLOSE's reconciliations are committed, after **every** batch including the last
(for the last, only item 1 applies, and it follows `/close`).

1. **Expunge on disk — one commit.** **Before deleting anything, grep the tree for what points at
   it:** every remaining batch's rows (the plan and the lane handoff) for each handle and file
   about to go, and the code and registries for citations of the plan section it sits in
   (`git grep -n '<plan file> §<section>'` — `engine/season/requirements.yaml` cites plan sections
   and reads them). Delete only what nothing still needs. A **gate** naming a finished position or batch
   is satisfied: rewrite that reference, per the plan's own convention for it, to carry the
   landing SHA (a batch's: its closing commit) in this same commit. A position a remaining batch **reads**, or a section
   code cites, stays, narrowed, until that stops being true. The same test governs any file or row
   judged stale. Then remove the batch's finished positions, and its `STOP … closes here` boundary row if the
   plan has one, **by the plan's own rule for finished positions, edges and census rows** (CLAUDE.md §2: the commit is their record) — where that rule
   is a one-line evidence record in a history part, writing it is the plan's convention and is
   done, once per position; this skill adds no row, count or narrative of its own (CLAUDE.md §1).
   In the lane handoff, remove the batch's handles from the Open rows that name them: a row naming
   only this batch's items goes, a row spanning other batches is narrowed. Delete the in-flight
   row. Report the batch's record as its commit range, `<open sha>..HEAD`. A position the batch
   only part-finished stays, narrowed to its receipt's `NOT DONE`. A measured gap goes to the one
   `hole_register.yaml` row the plan's own rule allows; what BATCH-CLOSE found and applied is
   already in the commits; a finding nobody can apply without a decision becomes a ledger row only
   if it is `needs_jordan` after CLAUDE.md §0's five-step ladder, and is otherwise dropped —
   nothing is kept "for the next batch".
2. **Clear the window.** This skill cannot clear its own context and nothing inside one window
   forgets selectively, so the boundary is a **stop**: report in a few lines the batch closed, its
   commit range, and the next batch's handle with whether its gates are met, then end with the
   status line (§THE STATUS LINE). **A fresh process is the clear:** `tools/methodology_drive.py`
   starts one per batch and re-invokes as `approved: <the same text>`, so nobody returns between
   batches. Run by hand instead, tell the user to `/clear` (**not `/compact`**: a summary carries
   forward exactly the `C(k) \ C(k+1)` this rule discards) and re-invoke the same way. The
   finished positions are gone from the plan, so 0.1 resolves only what remains and BATCH OPEN
   loads `C(k+1)` from disk. The driver is the operator's loop, outside any session; this skill
   never arms its own (CLAUDE.md §11).
3. **Do not hand a batch to a subagent to obtain the clean window.** A delegate that cannot
   dispatch `valoria-author` and `valoria-critic` cannot run a batch, and a general-purpose
   subagent probed 2026-10-06 held `Skill` but not `Agent`. That is a dated observation — the docs describe nested subagents to a configurable depth, so it
   may vary by agent type and version: re-run the probe before relying on it either way.
4. **If the invocation told the run to continue through several batches in one window**, do — and
   say at each boundary that **context was NOT cleared**: only the on-disk expunge happened, and
   every batch after the first carries the earlier ones' residue. Never report a fresh start the
   window did not have.

---

## THE STATUS LINE — the one thing a driver reads

Every invocation ends its final message with exactly one line, last, plain text (no markdown),
after the human-readable report:

- `METHODOLOGY-EXECUTE: NEXT <batch handle, as its plan writes it>` — a batch closed and was
  expunged; at least one remains and its first item's gates are met. A driver copies the handle
  into the next invocation as `[next: <handle>]`.
- `METHODOLOGY-EXECUTE: COMPLETE` — the sequence is exhausted, `/close` ran and the last expunge
  landed.
- `METHODOLOGY-EXECUTE: STOPPED <one-line reason>` — anything that needs a person: the 0.1
  approval stop; `approved:` text that matches nothing; an unmet gate or a `JORDAN` item; a `needs_jordan` ruling that survives
  CLAUDE.md §0's five-step ladder; an in-flight row that cannot be reconciled with the commits; a
  BATCH-CLOSE finding that can neither be applied nor rejected with a measurement; the next
  batch's gate unmet.

An invocation that dies before the line produces no line, and **a driver treats absence as
`STOPPED`**. The line is defined here and nowhere else; `tools/methodology_drive.py` reads it by
this spelling.

---

## GUARDRAILS

- **Phase 0 is additive, never a substitute** (see above). Reporting a batch as "built and closed"
  when only its items' Phase 0 ran, with no BATCH-CLOSE, is a false claim of the same shape
  `methodology-close`'s own falsifier table exists to catch.
- **Deferred is not skipped.** Batching BATCH-CLOSE to the batch boundary defers the expensive
  pass; it never licenses dropping it. A run that builds every item and never reaches a
  BATCH-CLOSE has not closed anything, whatever its commit count.
- **Nothing crosses a boundary but the tree.** A receipt, a finding, a SHA or a decision that is
  not in a commit, the plan, the handoff or the permanent surface does not exist for the next
  batch; if the next batch needs it, the partition missed a link — add the link or write the fact
  down, never reconstruct it from memory. No scratchpad file or summary carries state between
  batches. (Auto memory, where enabled, loads in every fresh process: fresh context, not fresh
  memory — treat it as permanent surface and put nothing batch-specific in it.)
- **Expunge deletes; it keeps no log of its own.** The boundary commit removes the in-flight row
  with the batch. A "batch k done" row, count or narrative that the plan's own rule for finished
  positions does not prescribe is the growth CLAUDE.md §1 forbids; the only state this skill keeps
  is the in-flight row, and only while its batch is open.
- **No new roster entry.** Phase 0 dispatches `valoria-author`; BATCH-CLOSE dispatches
  `valoria-critic`, exactly as `methodology-close` already does. Nothing here mints a third agent
  file.
- **Every dispatch names its model and its effort.** A Phase 0 producer, a Haiku extract, a critic:
  none inherits the session's, and none is set by prose in the prompt (§0.3).
- **Nothing here is a fixed count.** Producer-fan size, agonist-fan size, and batch size are each
  read from the instruction (or the batch) at hand every time — never a default fan, never a
  fixed item-count per batch.
- **No self-scheduling** (CLAUDE.md §11, as always).
- **Produces edits, not documents.** No directory beyond `skills/methodology-execute/`, no
  findings file, no build log kept past the receipts Phase 0's producers already returned.

## FALSIFIERS

| the claim | what would show it false |
|---|---|
| "one producer was enough" | the instruction itself named independent, file-disjoint sub-parts, and only one dispatch ran with no stated reason to collapse them |
| "the build matched the instruction" | the produced diff's scope is broader or narrower than the instruction's own `WHERE`, or silently substitutes a different fix for the one named — this is exactly what BATCH-CLOSE's FIDELITY TO PLAN lens exists to catch; if it passed anyway, name why |
| "fanned lanes integrated cleanly" | 0.4's merge resolved a same-file collision instead of stopping and rebuilding that file as one producer |
| "the gate was met before building" | a workplan-position item's `GATE` column named a position or a Jordan decision that had not actually landed (an ad hoc item has no `GATE` and is exempt from this one) |
| "the batches were partitioned, not sized" | an item's gate is met only by a later batch, or a link was cut with no stated reason |
| "the batch size was right" | a linked group was carried whole through BATCH-CLOSE with no stated reason not to cut it along a link, or was cut with no stated reason the whole group would have been too large |
| "the plan's batches and boundaries were followed" | a batch, boundary row, batch-named gate or carve-out that a plan defines was re-derived, re-split, merged or crossed (building ran past a `STOP … closes here` row without BATCH-CLOSE) with no conflict stated at the 0.1 stop; or a plan-stated close or suite rule was adopted over `methodology-close` or CLAUDE.md §0.4, or overridden, without that statement |
| "the context was cleared at the boundary" | the next batch's work cites a receipt, finding, SHA or fact that is neither on disk nor in the permanent surface; or two batches ran in one window and the report did not say context was NOT cleared |
| "the expunge took only what no remaining batch needs" | after the boundary commit, a remaining batch's gate or reading list names a handle or file that is gone from the tree, with no landing SHA written in its place |
| "the batch was expunged" | a finished position, or its in-flight row, is still present after the boundary commit, or that commit added a narrative, a "done" row or a count beyond what the plan's own rule for finished positions prescribes |
| "the batch resumed from its row" | a resumed batch rebuilt an item whose handle was in `built`, skipped one that was not, or re-ran a BATCH-CLOSE phase at or before `close` — or the row was trusted over the commits where they disagreed |
| "BATCH-CLOSE ran once per batch" | a test file, validator, forward sweep or the suite, `/code-review`, `/simplify`, `layer-conformance`, the agonist/antagonist fan, or the terminal critique ran between two items of the *same* batch, or the review phases did not run before the batch's items were reported done (the suite runs per CLAUDE.md §0.4 cl.1, not unconditionally) |
| every Phase 1–3 claim, at BATCH-CLOSE | `methodology-close`'s own falsifier table, unchanged, checked against the batch's cumulative post-Phase-0 diff |

**If this skill's guidance conflicts with `CLAUDE.md`, `architecture/`, or `methodology-close`,
they win.** This file and `methodology-close` are methods; those are the rules, and
`methodology-close` is the senior method where the two overlap.
