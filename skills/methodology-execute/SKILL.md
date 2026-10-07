---
name: methodology-execute
description: >
  METHODOLOGY-EXECUTE — `/methodology-execute <free-text task>`: build every item a task or workplan
  area names, then verify once per BATCH, never per item. Whatever it is handed is first expressed as
  ordered batches (a plan's own batches and boundary rows are followed as stated; otherwise items
  linked by a shared edit or a gate form one batch). Each item is one `valoria-author` build and one
  commit. BATCH-CLOSE (agonist review, `/code-review`, `/simplify`, the plan's validation, one terminal
  critique) runs once over the batch; the finished batch is then deleted from the plan and the next opens from disk in a cleared
  window (one fresh `claude -p` per batch under `tools/methodology_drive.py`). A free text that
  resolves to more than one position stops for approval first. Use for: "run methodology-execute",
  "build out this phase/area", a workplan position or phase not yet built that needs building and
  verifying before `/close`. A diff that already exists enters at BATCH-CLOSE (give its range and plan). Not for: design
  grading (`ners`), a draw (`resolution-diagnostic`), placement alone (`layer-conformance`).
---

# METHODOLOGY-EXECUTE — build, then close

## What this file owns, and what it does not copy

| the content | its single owner |
|---|---|
| the build phase, batching, context sets, the boundary, the status line, the `approved:` prefix | **this file** — except a plan's own batch structure, which is the plan's |
| deleting a finished position | **CLAUDE.md §2**; this file adds the pre-deletion check and says when |
| the verification sequence, lenses, checklists, and BATCH-CLOSE's tiers and effort | **this file** |
| the producer contract (receipt not transcript, no commit) | **`.claude/agents/valoria-author.md`** |
| tier IDs, the effort ladder, fan-out sizing ("what would N-1 miss?") | **CLAUDE.md §10** |
| a position's INSTRUCTION / WHERE / FALSIFIER / GATE | **its own content-owner entry** — never restated here |

**Words.** A Phase 0 dispatch is a **producer** (`valoria-author`), never an *agonist* or *antagonist*
(BATCH-CLOSE's review roles, defined there). The orchestrator's merge of fanned lanes is the
**integrator**. Three roles, three words (CLAUDE.md §4).

## Cadence — RULED by Jordan

*"code review and simplify to be at batch close"* · *"everything is to occur at batch close rather
than per step when it comes to validation and skills etc"*

- **Per item: a build and a commit, nothing else.** No test, covering test file, validator
  (`tools/valoria_local.py --staged`, the lane validator), forward sweep, `/code-review`, `/simplify`,
  `layer-conformance`, agonist/antagonist pass or terminal critique. CLAUDE.md §0.4 cl.2's permission
  to run the covering file mid-session is not taken up.
- **All of it runs once per batch, at BATCH-CLOSE.** A plan's per-step cadence yields to this.
- **Deferred is not skipped.** A producer's confidence that it built an item correctly is not
  evidence of it. A batch reported "built and closed" with no BATCH-CLOSE is the false claim
  this file's falsifiers catch, scoped to a batch.

## The run

```
BATCH k    OPEN ─▶ per item: BUILD ─▶ commit ─▶ … ─▶ BATCH-CLOSE ─▶ (/close, if last) ─▶ EXPUNGE
                                                                                         │
                       BOUNDARY: stop; a fresh window opens the next batch from disk ◀───┘
BATCH k+1  OPEN ─▶ …   reload C(k) ∩ C(k+1) · load C(k+1) \ C(k) · C(k) \ C(k+1) is never reloaded
```

BATCH-CLOSE = review, gates, the plan's validation (with at most one suite run), then one terminal
critique (§BATCH-CLOSE). A batch is the unit of **work**, of **verification** and of **context**.

---

## PHASE 0 · BUILD

### 0.1 SCOPE — resolve the free text before touching anything

`/methodology-execute <task>` hands over free text, not a position handle; this file does not guess
which unit was meant.

1. **Search.** `/currency`, then follow `CURRENT.md` to the live plan (not named here: a filename
   written here is the stale pointer CLAUDE.md §1 forbids). Search it, any workplan it carves out by
   name (CLAUDE.md §2), and the lane's `HANDOFF_<LANE>.md` Open table (an ad hoc task's batches and
   any in-flight row live there) for a position whose handle or `what runs` matches.
2. **Classify.**
   - **Exactly one position, its `GATE` met, and a whole batch of its own** (not part of a larger plan
     batch): go to 0.2. No confirmation: the gate establishes it is buildable and building it is what
     was asked.
   - **More than one position:** resolve the ordered subsequence (each position's own `GATE`), then
     **stop and present it** — handles in order, unmet gates flagged. CLAUDE.md §0: *"Anything
     ambiguous or spanning lanes: get the plan approved or ask a focused question."*
   - **None:** a new task. Write the plan (CLAUDE.md §0's first bullet: what changes, in what order, how you will verify) and
     **stop and present it**, unless a one-sentence plan already states it.
   - **Text beginning `approved:`** means a person approved the sequence the "more than one position"
     stop would present. It skips **only that stop**; gate checks, the in-flight check and every
     other `STOPPED` condition still apply. **It never licenses a new task:** finished positions are
     expunged, so `approved:` text that now matches nothing is `STOPPED` (*finished, or the plan
     changed*) — otherwise a re-run after the last expunge would rebuild the work. A trailing
     `[next: <handle>]` (a driver copies it from the previous `NEXT` line) fixes the batch to run;
     if the plan's next batch is another, `STOPPED`.
3. **Batches.** Express the sequence as batches (§BATCHES): the plan's own where it has them,
   otherwise derived and presented in the same stop, so one approval covers both. Then, for each
   batch in order: BATCH OPEN; 0.2–0.5 once per item (one build, one commit per item, never one diff
   spanning items); BATCH-CLOSE; BATCH BOUNDARY. Each item commit carries the `Item: <handle>` trailer,
   the in-flight row's update, and the producer's receipt in its body (`NOT DONE` included). If a
   later item's `GATE` proves unmet when its turn comes (outside this run, or a `JORDAN` item),
   **stop and report it** (`STOPPED`) — never skip it silently, and never run BATCH-CLOSE on a batch
   that stopped short without saying so.

### 0.2 Read the instruction — never invented here

Take one unit at a time: a **workplan position** (read its content-owner entry — INSTRUCTION /
WHERE / FALSIFIER / GATE — in full before dispatching), or an **ad hoc task** (the plan 0.1 wrote, or
the user's one sentence if that sufficed). That instruction **is** the plan BATCH-CLOSE's review checks fidelity
against: hand the producer the same text you read, never a paraphrase or a second draft.

### 0.3 Size the build — one producer by default

`Agent({ subagent_type: "valoria-author", model: ..., effort: ..., ... })`, one dispatch for the whole
instruction. **Set `model` and `effort` on every dispatch:** an un-annotated producer inherits the
session's model (CLAUDE.md §10) and prose in the prompt sets no effort.

- **Model:** the item's own `tier` where the plan carries one, else `sonnet`; `haiku` for
  deterministic work (find-replace, a deletion, a re-host, a transcription); `opus` only where the
  instruction names a competing-considerations judgment (design intent, contract closure).
- **Effort:** `high`; `xhigh` for an `opus` item; never `max`.
- The orchestrating session reads receipts and commits and needs no more than sonnet-class; a driver
  passes `--model` and `--effort` after its `--`.

**Fan only when the instruction itself names independent sub-parts sharing no file** (the live plan's
hard-serial-edge table, reached through `CURRENT.md`, exists to catch the rest). Never fan by default
or by file count — *"before spawning N agents, ask what N-1 would miss."* When fanned: each producer
runs `isolation: worktree` and is handed **only its own sub-part's instruction**; each returns a
receipt (path, what changed, one line); fire the first dispatch alone, await its first streamed
token, then send the rest in one message (CLAUDE.md §10 pt 3). One producer or several, **the
producer never commits** — that is the orchestrator's next action.

### 0.4 Integrate — only when fanned

The **orchestrator** merges each worktree in an order that respects any named serial edge, then
commits. **If two lanes touched one file, the split was wrong, not the merge:** stop and rebuild that
file's portion as one producer; never resolve the collision by hand.

### 0.5 What this phase must not do

- **Never review or validate its own output.** The dispatch prompt tells `valoria-author` to write
  the edit, return its receipt and run no test, validator or sweep; its own file otherwise says to run
  the covering test file, and that run is BATCH-CLOSE's here.
- **Never commit, and never run the suite** — `valoria-author`'s file already forbids both.
- **Never skip 0.1's gate check** because an instruction "looks buildable": a position gated on
  another position or on Jordan is not this skill's to build around.

---

## BATCHES — the unit of work, of verification and of context

Whatever this skill is handed — an area, a cluster of positions, an ad hoc task — is a set of items,
expressed first as ordered batches. A single position is a one-item batch, not an exception.

### The partition — boolean intersection, not a headcount

Read each item's sets from its own entry (an ad hoc item: from the plan 0.1 wrote, which must name
them), never guessed: **edits** (what its WHERE writes) and **gates** (what its GATE names, any serial
edge the plan states, any item whose commit it needs).

Two items are **linked** when `edits(i) ∩ edits(j) ≠ ∅`, when `gates(i) ∩ gates(j) ≠ ∅` (a common
dependency), or when one gates on the other. What an item only *reads* goes into its context set `C`
(below), not into linking. The **permanent surface** links nothing and is defined by kind, never by
how many items name it: `CLAUDE.md`, `CURRENT.md`, `HANDOFF.md` and the lane file, the plan's head,
and the ledgers every position of the *plan* appends to (the hole and requirements registers).

**By default a batch is a connected group of linked items**, ordered so every gate points earlier to
later. Unlinked items go in different batches unless merged for a stated reason; they commute, so the
plan's order stands.

Why: linked items read and edit the same things, so they need one window, and their edits land in one
diff. The second reason is the weaker (BATCH-CLOSE's INTERDEPENDENCIES scan greps the whole tree, so
a later batch's close still sees earlier work), which is why a group may be cut:

- **Cut along any link, provided every cut link points forward** (the later batch's gates and files
  are met by the earlier batch's close and expunge having landed) and the cut is stated. Name what
  carrying the whole group would risk (a long run with no checkpoint; a batch too large for a
  reviewer to hold) and what the cut costs (a re-read; an interaction only the joint diff shows).
  By judgment, never a fixed item-count.
- **Keep unlinked groups apart or merge them, by a stated reason either way.** Apart buys a cleared
  window and costs a full close each; merged saves a close and costs the union of their contexts.

### Where the batches live — follow whoever defined them; derive only what nobody did

**Sources, highest first; a lower one never overrides a higher:**

1. **An in-flight row** (any session may have written it): resume that batch (§The in-flight row).
2. **The live plan and any workplan it carves out by name** (CLAUDE.md §2: a carve-out's batches are
   its own). Follow the forms plans actually write:
   - a **batch table or heading** (handle → positions) and a **`Batch` column**;
   - a **boundary row** (`STOP. Batch N closes here`): building stops there — BATCH-CLOSE, boundary,
     status line; the positions after it are the next batch;
   - a **gate that names a batch** (`GATE: Batch 1`): met iff that batch's close landed (BATCH OPEN 3);
   - the plan's **serial-edge and file-census tables**: they are the gates and edit sets — derive
     nothing the plan states;
   - **per-batch discipline** (reading list, receipt, commit shape, tiers): the plan's, and **below**
     CLAUDE.md and this file's BATCH-CLOSE. A plan-stated close, cadence or suite rule that differs
     from BATCH-CLOSE, this file's per-item rule or CLAUDE.md §0.4, lighter *or heavier*, is a conflict to
     state at the 0.1 stop — never silently adopted, never silently overridden. (`/code-review` and
     `/simplify` at batch close is ruled, so a plan still asking for them per step is stale, not
     conflicting.)
3. **Batch rows another agent or session left in the lane's handoff** for a task with no plan.
4. **A proposal or another agent's unratified plan** (`proposals/`, a delegate's report): input to
   the 0.1 stop, presented, never adopted silently (a plan lives under `workplans/`).
5. **Derived by the partition**, only where 1–4 are silent: present at the 0.1 stop and, once
   approved, write into the plan that owns the positions or, for an ad hoc task with no plan, into
   the lane's Open table, one row per remaining batch (items, files, gates) — in the commit that
   opens the first batch. A cleared window finds nothing else.

**The invocation text selects which batch runs; it never changes membership.** Naming a plan batch
runs it. Naming some but not all of a batch's positions, or spanning batches, is stated at the 0.1
stop: build the whole batch, or run a **partial batch** (BATCH-CLOSE over just those items' range;
the expunge removes just them; the plan's batch and boundary row stay).

Test every plan batch against the partition. A batch that gates on a later batch, or two of the
plan's own sources that disagree (a table against a column), is a conflict: say so at the 0.1 stop
and leave the plan's grouping standing until ruled. Lumping or splitting more finely than the
partition would is the plan's judgment, not a conflict. This skill never re-splits a plan on its own
authority. A one-batch task writes no batch rows; its commits and in-flight row are its record.

### The context set

A batch's **context set** `C(k)` is the reading list BATCH OPEN loads: its items' entries, the files
they edit and read, the registries their falsifiers run against, the commits their gates name, and the
permanent surface — derived from the items' own entries (what *this* batch needs, not what the last
read). A plan that keeps a per-batch reading list owns it.

What persists across a boundary is the **intersection `C(k) ∩ C(k+1)`**: in practice CLAUDE.md and the
user-level file, this skill, `CURRENT.md`, `HANDOFF.md` and the lane file, the
plan's head, and any registry both batches read. It is all on disk and a clear empties the window's
copy too, so BATCH OPEN reloads it; `C(k) \ C(k+1)` is never reloaded. **A fact one batch establishes
and the next needs is a dependency, not context:** it travels as a commit, a plan edit or a handoff
pointer and appears in the next `C` as a gate, never as a recollection.

### The in-flight row — where a cleared window learns where the batch stands

While a batch is open, **one row in the lane file's Open table** (`registers/handoffs/HANDOFF_<LANE>.md`,
the lane its plan names; CLAUDE.md §2's place for mid-task state) carries the batch handle, its place
in the plan, **`open <sha>`** (`HEAD` before the first item), **`built <handles>`** (each item's handle,
appended in that item's own commit, which also carries `Item: <handle>`, so a handle is listed iff
its commit exists) and **`close <none|1|2|3|4|final>`** (the last BATCH-CLOSE step finished; `final`
once `/close` committed; each step's end updates the row, **in a commit of its own if the step
edited nothing** — a clean step leaves no other mark and a resume would re-run it). Ids and
pointers only, never a count or narrative (CLAUDE.md §1). In the three-column table (item | where it
lives | next step): `Batch <handle> — IN FLIGHT` | place in the plan + `open <sha>` | `built … ·
close … · <what remains>`. An ad hoc task with no batch row gets the row whole (items, files, gates,
then these fields). **The expunge deletes the row**, which is why it is allowed (CLAUDE.md §2: a
finished position's record is its commit, not a mark).

**Resuming** is the first check of any invocation, ahead of 0.1's classification. If an in-flight row
exists, that batch continues: build only items not in `built`, run BATCH-CLOSE from the step after
`close`, take `open` as the start. **Check the row against the tree first:** every `built` handle
needs a commit in `open..HEAD` carrying its `Item:` trailer and every such trailer must be in the
row; where they disagree the commits win (correct the row, say so); if irreconcilable, ask. **Then
look at the tree:** a dirty `git status` is the killed item's partial build — report its paths,
`git stash push -u` it (reversible), rebuild the item, never commit it unreviewed; `git worktree
list` shows fan lanes left behind — integrate or remove each. **A position the plan or handoff
records as BUILT with its close not run** enters at BATCH-CLOSE: write the row with `built` filled and
`open` the range start that record names (ask if it names none). An invocation whose text does not
match an in-flight batch stops (`STOPPED`); it never opens a second.

### BATCH OPEN — orient as a session opens

1. `/currency`, then the lane's handoff and the plan's rows for this batch only.
2. **Load this batch's context set from disk**, overlap included; never rely on having read it.
3. **Check every item's gate against the tree**, never an earlier window's belief. A **SHA** is met
   iff `git merge-base --is-ancestor <sha> HEAD`. A **position** is met iff the plan no longer holds
   it and its landing SHA is in the gate, or the plan's own status vocabulary marks it landed with
   evidence named; BUILT-not-closed is **not** landed. A **batch** is met iff its close landed (rows
   gone or marked closed by the plan's rule; closing SHA in the gate and an ancestor of `HEAD`). A
   **ruling or decision** is met iff the ledger row that owns it (`registers/`, last row governs)
   records it resolved. Any other gate is unmet: `STOPPED`.
4. **Record the starting commit** (`HEAD`) in the in-flight row, in the first item's own commit.
   Every item commits at once, so at BATCH-CLOSE the tree is clean and the batch's diff is the
   **commit range `<open>..HEAD`** (`git diff` for content; `/code-review`'s branch/PR-target mode
   for its dispatch). `valoria-critic` holds only Read, Grep and Glob and cannot run `git diff`:
   write the range's diff to a scratchpad file and hand the critics its path.
5. **Share the reading, once, on Haiku:** one `valoria-measure` dispatch extracts the batch's reading
   list into a table handed to every producer so none re-opens the same files (CLAUDE.md §10 pt 1:
   a fan-out's cost is its reading). The extract is a claim the producer checks where it edits.

### The last batch is also the run's `/close`

When the sequence is exhausted, BATCH-CLOSE is followed by `/close` (its suite step is BATCH-CLOSE's,
not run twice; lane validator, commit, handoff), and **then** the expunge. The order is deliberate:
the expunge deletes the in-flight row, so a death anywhere earlier — the long suite stretch included
— still resumes from the row. A mid-run boundary does not invoke `/close`.

---

## BATCH-CLOSE · once per batch

Runs over the **commit range** from BATCH OPEN (never one item's diff, never a working-tree diff),
checked for fidelity against the **plan**: the plan's stated scope for the batch, the union of the
positions 0.1 resolved into it, or the ad hoc instructions 0.2 read. **A diff that already exists**
(built by hand or by an earlier run) enters here: give the range and the plan. Four steps, in this
order, none skipped because an earlier one found nothing — each checks a different axis:

```
1 REVIEW     Sonnet agonist(s) ─▶ (if more than one) Opus antagonist ─▶ reconcile
2 GATES      /code-review high --fix ─▶ /simplify ─▶ layer-conformance (on trigger)
3 VALIDATE   the plan's per-step checks, then at most one suite run
4 CRITIQUE   one Opus terminal critique, holistic × granular ─▶ reconcile
```

Cheap and broad runs first. Every dispatch is `valoria-critic` (Read, Grep, Glob only: read-only by
construction, so independence is structural), sets `model` and `effort` on the Agent call, and is
handed outputs, never reasoning. It cannot run `git diff`: hand it the range's diff as a scratchpad
file path. **Nothing runs at `max`.** Terms, scoped to this file: an **agonist** is one independent
first-pass reviewer holding one or more lenses over the existing diff; the **antagonist** is the
single reconciler cross-examining the agonists' outputs against the tree.

### 1 · Review

Lenses: **ACCURACY** (re-derive what each changed file does against the plan, not its commit
message); **FIDELITY TO PLAN** (scope matches: nothing broader, nothing narrower, no silent
substitution); **CORRECTNESS** (a first bug pass); **COMPLIANCE WITH CODE ARCHITECTURE** (placement
sanity only; the full pass is step 2); **LOGIC** (control flow and conditionals sound).

- **Roster.** One Sonnet agonist, `effort: "high"`, carrying every lens when one reader can hold the
  diff; split by lens or by independent module only when the diff is too large for one, and collapse
  a lens that plainly does not apply. Never a fixed count: before adding an agonist, name what it
  would catch that the others would not. Each is handed its lens(es), the plan and the diff — never
  another agonist's output. Fire the first alone, await its first token, then send the rest at once.
- **Antagonist, only when more than one agonist ran** (one leaves nothing to reconcile): `opus`,
  `effort: "xhigh"`, handed every agonist's output (not reasoning), the plan and the tree. It
  re-verifies every claim against disk, rules uphold / overturn / soften / sharpen on each, and
  cross-checks the agonists against each other: two lenses disagreeing about one site is itself a
  finding.
- **Reconcile** (here and after step 4): the orchestrator applies each surviving finding or rejects
  it with the measurement that rejects it — never a bare "disagree". With no antagonist, open each
  finding's site on disk before applying it.

### 2 · Gates — in this order, on one tree, each one's fixes applied before the next reads it

1. `/code-review high --fix` — correctness first. Name the level: with none given it reuses the last
   one typed.
2. `/simplify` — reuse, simplification, efficiency, on the now-correct tree.
3. `layer-conformance`, only on its trigger (`/close` step 4 has the same): **Lens B** when the range
   touches `engine/season/`; **Lens A** when the batch, step 1 or `/code-review` added a tool, guard,
   hook or governance rule. Otherwise skip: Lens B "runs only on Layer-2 code against a Layer-1 row".
   Its own A1–A5 and B-steps decide the rest.

### 3 · Validate

The plan's per-step checks (forward sweep, lane validator, `tools/valoria_local.py --staged`, a
covering test file) run once over the range, after step 2 and before step 4, so the critique sees any
fix they force. The plan's own definition governs each check; this file only sets when. A falsifier
that fails follows the plan's own stopping rule for that position. Gather the instruments' output on
Haiku (`valoria-measure`); the orchestrator judges it. **The suite is CLAUDE.md §0.4's:** at most once
per batch, only if it can observe something CI will not (cl.1), over only what the range can reach
(§0.4's closing paragraph); a prose or ledger batch runs just the files that read what it touched.

### 4 · Critique

One dispatch, `opus`, `effort: "xhigh"`. A chorus of Opus critics is the redundancy CLAUDE.md §10
warns against; what a second would catch is step-1-shaped, so run it there, at Sonnet. It is handed
the plan, the post-gate diff and a bare receipt of what steps 1–3 changed (path plus one line each),
never their transcripts.

- **Checklist:** CODE CORRECTNESS (re-run on the post-fix tree); INTERDEPENDENCIES (every caller or
  importer of anything the diff's signature-level changes touch, found by grepping each changed name
  across the whole tree with its floor asserted, assignments as well as readers per CLAUDE.md §0.1
  pt 1 — one `valoria-measure` dispatch on Haiku builds the table and the critic verifies it at the
  sites that matter); FORWARD AND BACKWARD SWEEPS (backward: does the diff still honour what every
  existing caller assumed; forward: does everything that will read the new state get it right);
  LOGIC again, since a fix from steps 1–3 can introduce a defect.
- **Handshake — neither pass is a verdict alone.** TOP-DOWN: does the diff cohere with the plan, the
  architecture and the system around it. BOTTOM-UP: does each line, function and call do what it
  claims, checked on disk. Every top-down finding traces to a `file:line`; every granular finding
  traces up to whether it matters holistically (a defect with no holistic consequence is reported
  downgraded, never silently dropped). This is not `ners`' six directions: name which axis you run.

The pass's output is edits to the diff plus at most one paragraph in the commit message; a finding
that needs no ruling is fixed in this commit or dropped.

---

## BATCH BOUNDARY — expunge, then clear

After BATCH-CLOSE's reconciliations are committed, after **every** batch (the last follows `/close`
and has only step 1).

1. **Expunge on disk — one commit.** **Before deleting anything, grep the tree for what points at
   it:** every remaining batch's rows (plan and lane handoff) for each handle and file about to go,
   and code and registries for citations of the plan section it sits in (`git grep -n '<plan file>
   §<section>'`; `engine/season/requirements.yaml` cites plan sections and reads them). Delete only
   what nothing still needs. A **gate** naming a finished position or batch is satisfied: rewrite it,
   by the plan's convention, to carry the landing SHA (a batch's: its closing commit). A position a
   remaining batch **reads**, or a section code cites, stays, narrowed, until that stops being true;
   the same test governs any file or row judged stale. Then remove the finished positions and the
   batch's `STOP … closes here` row **by the plan's own rule for finished positions, edges and census
   rows** (CLAUDE.md §2: the commit is their record) — where that rule is a one-line evidence record
   in a history part, writing it is the plan's convention; this skill adds no row, count or
   narrative of its own (CLAUDE.md §1). In the lane handoff remove the batch's handles from the Open
   rows naming them (a row naming only this batch goes; a row spanning others is narrowed) and delete
   the in-flight row. Report the record as `<open sha>..HEAD`. A part-finished position stays,
   narrowed to its receipt's `NOT DONE`. A measured gap goes to the one `hole_register.yaml` row the
   plan's rule allows; a finding nobody can apply without a decision becomes a ledger row only if
   `needs_jordan` after CLAUDE.md §0's five-step ladder, else it is dropped — nothing is kept "for the
   next batch".
2. **Clear the window.** This skill cannot clear its own context and nothing inside a window forgets
   selectively, so the boundary is a **stop**: report in a few lines the batch closed, its range, and
   the next batch's handle with whether its gates are met; end with the status line. **A fresh process
   is the clear:** `tools/methodology_drive.py` starts one per batch and re-invokes as `approved:
   <same text> [next: <handle>]`, so nobody returns between batches. By hand, tell the user to
   `/clear` (**not `/compact`**: a summary carries forward exactly the `C(k) \ C(k+1)` this rule
   discards) and re-invoke the same way. The driver is the operator's loop, outside any session; this
   skill never arms its own (CLAUDE.md §11).
3. **Do not hand a batch to a subagent to get a clean window:** a delegate that cannot dispatch
   `valoria-author` and `valoria-critic` cannot run a batch, and a general-purpose subagent has held
   `Skill` without `Agent`. Check the delegate's tool list before relying on one.
4. **If the invocation told the run to continue through several batches in one window,** do, and say
   at each boundary that **context was NOT cleared**: only the expunge happened, and each later batch
   carries the earlier ones' residue. Never report a fresh start the window did not have.

---

## THE STATUS LINE — the one thing a driver reads

Every invocation ends its final message with exactly one plain-text line, last, after the report:

- `METHODOLOGY-EXECUTE: NEXT <batch handle, as its plan writes it>` — a batch closed and was expunged;
  at least one remains and its first item's gates are met.
- `METHODOLOGY-EXECUTE: COMPLETE` — the sequence is exhausted, `/close` ran, the last expunge landed.
- `METHODOLOGY-EXECUTE: STOPPED <one-line reason>` — anything needing a person: the 0.1 approval stop;
  `approved:` text that matches nothing; an unmet gate or a `JORDAN` item; a `needs_jordan` ruling
  surviving the five-step ladder; an in-flight row irreconcilable with the commits; a BATCH-CLOSE
  finding neither applicable nor refutable by measurement; the next batch's gate unmet.

A death before the line produces none, and **a driver treats absence as `STOPPED`**. The line is
defined here and nowhere else; `tools/methodology_drive.py` reads it by this spelling.

---

## GUARDRAILS

- **Nothing crosses a boundary but the tree.** A receipt, finding, SHA or decision not in a commit, the
  plan, the handoff or the permanent surface does not exist for the next batch; if the next batch
  needs it, the partition missed a link — add the link or write the fact down, never reconstruct it.
  No scratchpad file or summary carries state. (Auto memory loads in every fresh process: fresh
  context, not fresh memory — put nothing batch-specific in it.)
- **Expunge keeps no log of its own.** A "batch k done" row, count or narrative that the plan's rule
  for finished positions does not prescribe is the growth CLAUDE.md §1 forbids; the only state this
  skill keeps is the in-flight row, while its batch is open.
- **Every dispatch names its model and effort** (producer, Haiku extract, critic); none inherits the
  session's and none is set by prose (§0.3). No roster entry is added: Phase 0 is `valoria-author`,
  BATCH-CLOSE is `valoria-critic`.
- **Nothing here is a fixed count:** fan size and batch size are read from the instruction or batch.
- **No self-scheduling** (CLAUDE.md §11). **Edits, not documents:** no directory beyond
  `skills/methodology-execute/`, no findings file, no build log past the receipts.

## FALSIFIERS

| the claim | what would show it false |
|---|---|
| "one producer was enough" | the instruction named independent, file-disjoint sub-parts and only one dispatch ran, with no stated reason |
| "the build matched the instruction" | the diff's scope is broader or narrower than the instruction's `WHERE`, or substitutes a different fix — what FIDELITY TO PLAN exists to catch; if it passed anyway, name why |
| "fanned lanes integrated cleanly" | 0.4's merge resolved a same-file collision instead of rebuilding that file as one producer |
| "the gate was met before building" | a position's `GATE` named a position, batch or ruling that had not landed (an ad hoc item has none and is exempt) |
| "the batches were partitioned, not sized" | an item's gate is met only by a later batch, a link was cut with no stated reason, or a linked group was carried whole (or cut) with no stated reason either way |
| "the plan's batches and boundaries were followed" | a batch, boundary row, batch-named gate or carve-out a plan defines was re-derived, re-split, merged or crossed (building ran past a `STOP … closes here` row without BATCH-CLOSE) with no conflict stated at the 0.1 stop; or a plan-stated close or suite rule was adopted over, or overridden against, BATCH-CLOSE or CLAUDE.md §0.4 without that statement |
| "the context was cleared" | the next batch cites a receipt, finding, SHA or fact neither on disk nor in the permanent surface; or two batches ran in one window and the report did not say context was NOT cleared |
| "the expunge took only what no remaining batch needs" | after the boundary commit, a remaining batch's gate or reading list names a handle or file gone from the tree with no landing SHA, or a finished position or its in-flight row is still present, or the commit added a narrative, "done" row or count the plan's rule does not prescribe |
| "the batch resumed from its row" | a resumed batch rebuilt an item in `built`, skipped one not in it, re-ran a phase at or before `close`, or trusted the row over the commits where they disagreed |
| "BATCH-CLOSE ran once per batch" | a test, validator, forward sweep, suite, `/code-review`, `/simplify`, `layer-conformance`, agonist/antagonist pass or terminal critique ran between two items of one batch, or the review phases did not run before the batch was reported done (the suite itself runs per CLAUDE.md §0.4 cl.1) |
| "the review matched the plan" | more or fewer independent lenses or modules existed than agonists dispatched with no stated reason, or a diff one reader could hold was fanned |
| "the antagonist checked every lens" | an antagonist ran after a single agonist, or ran and a lens has neither a finding nor a stated attack that failed |
| "the gates ran, fixed" | no invocation record for `/code-review` or `/simplify`, or for `layer-conformance` when its trigger held (or one when it did not), or a later gate graded a tree carrying an earlier gate's unapplied finding |
| "the critique handshook" | a top-down finding with no `file:line`, or a granular finding with no stated holistic disposition |
| "the dispatches ran at their tier" | an agonist was not `sonnet` at `effort: "high"`, the antagonist or critic was not `opus` at `"xhigh"`, any dispatch carried `"max"`, or effort was set by prose rather than the Agent call |
| "the critique found nothing" | no named failed attack, only an absent finding |

**If this file conflicts with `CLAUDE.md` or `architecture/`, they win.** This file is a method; those
are the rules.
