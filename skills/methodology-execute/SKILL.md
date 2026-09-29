---
name: methodology-execute
description: >
  METHODOLOGY-EXECUTE — invoked as `/methodology-execute <free-text task>` (e.g.
  `/methodology-execute build out governance branch for faction`), build every item a task or
  workplan area names, THEN verify once per batch rather than once per item. PHASE 0.1: resolve
  the free text against the live workplan first — one matching position with its GATE already met
  proceeds straight through; more than one matching position, or none at all, STOPS and presents
  the resolved sequence (or the freshly-stated plan) for approval before anything is built, per
  CLAUDE.md §0's "ambiguous or spanning lanes" rule. PHASE 0.2+: read each item's own instruction
  (a workplan position's content-owner entry, or the stated plan for an ad hoc task) and dispatch a
  `valoria-author` producer to build it — one producer by default, fanned into
  `isolation: worktree` lanes only when the instruction itself names independent sub-parts with no
  shared file — then commit. **No full pytest suite, no `/code-review`/`/simplify`/
  `layer-conformance`, and no agonist/antagonist fan or terminal critique after each item** — those
  are BATCH-CLOSE's job, not Phase 0's, run once per batch (a plan-phase's worth of items, or a
  smaller sub-batch when a phase is large) or at the run's own final `/close`, never per item.
  BATCH-CLOSE: `methodology-close`'s full Phases 1–3, run once against the batch's cumulative diff
  — invoked verbatim, not copied here. Use for: "run methodology-execute",
  "/methodology-execute <task>", "build out this phase/area", a workplan position, phase, or
  free-text area of work that has not been built yet and needs both building and verifying before
  `/close`. Not for: a diff that already exists and only needs verifying — use `methodology-close`
  directly; design-quality grading (`ners`); a target that resolves by a draw
  (`resolution-diagnostic`); Layer placement alone with no build to do (`layer-conformance`
  directly).
---

# METHODOLOGY-EXECUTE — build, then close

## Created 2026-09-29, split out of `methodology` (now `methodology-close`) per Jordan's directive that the pipeline also orchestrate the build, not only verify one already built. Invocable as a project skill through the symlink `.claude/skills/methodology-execute`.

## What this skill owns, and what it copies

| the content | its single owner |
|---|---|
| the build phase — dispatching the producer(s) that write the diff a unit of work specifies, sizing the fan, and integrating parallel write lanes | **this file** |
| batch sizing — where the boundary falls between many cheap BUILDs and one BATCH-CLOSE | **this file** |
| the sequence, tiers, checklists, the handshake, the guardrails and the falsifiers for verifying the resulting (batch) diff | **`methodology-close`**, invoked by reference — not copied |
| the producer contract — full toolset, a receipt not a transcript, no commit, no full-suite mid-lane | **`.claude/agents/valoria-author.md`** |
| model tiers, the effort ladder, and the fan-out sizing rule ("ask what N-1 would miss") | **CLAUDE.md §10** |
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

**Per Jordan's directive when this skill was split from `methodology-close`: the expensive
pass — code-review/simplify/layer-conformance, the agonist/antagonist fan, the terminal critique,
and the full pytest suite — does not run after every item.** CLAUDE.md §0's baseline cadence
("one step is one position and one commit... at end of each step, `/code-review` and `/simplify`")
is written for a session working one position by hand. `methodology-execute` orchestrates many
items in one run, and re-running that cadence per item is the over-fanning CLAUDE.md §10 warns
against, plus the exact "full suite is a close step, not an inner loop" mistake CLAUDE.md §0.4
already forbids. So for a run this skill orchestrates: **every item still gets its own commit
(that part of the baseline cadence is unchanged); the review and test cost is deferred to
BATCH-CLOSE**, below. This is a named, deliberate scoping of the baseline cadence to this skill's
own batch granularity — not a silent departure from it, and not licence to skip BATCH-CLOSE
itself.

---

## THE SHAPE OF A RUN: MANY CHEAP ITEMS, ONE EXPENSIVE PASS PER BATCH

```
  item 1 ──▶ PHASE 0 · BUILD ──▶ commit ─┐
  item 2 ──▶ PHASE 0 · BUILD ──▶ commit ─┼─▶  BATCH-CLOSE (once per batch):
  item 3 ──▶ PHASE 0 · BUILD ──▶ commit ─┘      PHASE 1 · AGONIST FAN → ANTAGONIST
       ⋮  (repeats for every item in the batch)  PHASE 2 · MECHANICAL GATES (+ full pytest suite)
                                                  PHASE 3 · TERMINAL CRITIQUE
```

**Phase 0 repeats per item; BATCH-CLOSE does not.** Each item is one producer, one commit, and — at
most — the cheap, file-scoped self-check CLAUDE.md §0.4 already allows mid-session (the one test
file the change touches, never the full suite). The expensive layer — the agonist/antagonist fan,
`/code-review`→`/simplify`→`layer-conformance`, the full pytest suite, and the terminal critique —
fires once, against every item's cumulative diff since the last BATCH-CLOSE, at a batch boundary
(§BATCHING) or at the run's own final `/close`.

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

1. **Search the live workplan first.** Run `/currency` if you have not already this session, then
   check `CURRENT.md` and the live plan (today, `workplans/2026-09-28-the-plan-one-order-mc-v18-retired.md`
   + its `_part2` — re-check via `/currency`, this pointer will go stale) for a position whose
   handle or `what runs` plausibly matches the text.
2. **Classify what the search found:**
   - **Exactly one position, `GATE` already met** — proceed straight to 0.2 with that position's
     content-owner entry. No confirmation needed: the position's own gate already establishes it
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
3. **Once a sequence is confirmed (or the single-position case skipped confirmation), split it
   into batches** — see §BATCHING — **then run 0.2 onward once per item, in the resolved order**:
   one BUILD → integrate → commit per item. **Never one diff spanning several items**: each item
   keeps its own commit, the one part of CLAUDE.md §0's baseline cadence this skill does not defer
   (see "What this skill owns" above). If a later queued item's `GATE` turns out unmet when its
   turn comes (something outside this run's scope, or a `JORDAN` item), **stop there and report
   it** — do not skip it silently and continue to the next, and do not run BATCH-CLOSE on a batch
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

Dispatch one `Agent({ subagent_type: "valoria-author", ... })` to build the entire instruction,
sequentially. No `isolation: worktree` is needed for a single producer — nothing else is writing
this tree concurrently within this run.

**Fan only when the instruction itself names genuinely independent sub-parts that share no file**
— the same test the workplan's own hard-serial-edge tables (e.g. `THE PLAN` part 1 §3.5, and the
2026-09-18 plan's §3.9) exist to catch. Never fan by default, and never size the fan to "how many
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

### 0.4 Integrate

The **orchestrator**, not a subagent, merges each worktree into the working branch, in an order
that respects any named serial edge between the sub-parts. **If two lanes touched the same file,
the split was wrong, not the merge** — stop, do not resolve the collision by hand, and rebuild that
file's portion as one producer instead. A silent auto-merge of a same-file collision is exactly the
failure the `FALSIFIERS` table below is written to catch.

### 0.5 What this phase must not do

- **Never review its own output.** `valoria-author` may verify its own edit runs (it holds `Bash`
  for exactly that), but that is not Phase 1's independent fidelity check, and Phase 0 does not
  attempt to be one.
- **Never commit, and never run the full suite mid-lane** — `valoria-author`'s own file already
  forbids both; this skill adds no exception.
- **Never skip 0.1's gate check** because the instruction "looks buildable" — a position gated on
  another position or on Jordan is not this skill's to build around by reinterpreting its own gate.

---

## BATCHING — sizing the boundary between one BUILD and the next BATCH-CLOSE

**Default: one batch is one plan-phase's worth of items** — e.g. one of `THE PLAN`'s four
top-level phases, or the whole resolved sequence when 0.1 found a small cluster with no phase
structure of its own. **When a phase is large, split it into smaller batches** — sized the same
way Phase 0.3 sizes a producer fan: by judgment, never a fixed item-count. Name what waiting for
the whole phase would risk (a long run with no verification checkpoint, a batch too large for
Phase 1's fan or Phase 3's critique to hold) before splitting; name what a smaller batch would miss
(cross-item interactions only visible once several land) before *not* splitting. A single-item
0.1 resolution is trivially its own one-item batch — there is nothing to wait for, so BATCH-CLOSE
runs right after it.

**A batch boundary is also always the run's final `/close`, if nothing follows it.** When the
resolved sequence (or the current batch) is the last one in this invocation, BATCH-CLOSE is
immediately followed by `/close` itself (full suite — already run by BATCH-CLOSE's Phase 2, not
twice — lane validator, commit, handoff), per that skill's own definition. A mid-run batch
boundary that is not the run's end does not invoke `/close`; it only runs BATCH-CLOSE and then
continues to the next batch.

---

## BATCH-CLOSE · PHASES 1–3, ONCE PER BATCH, BY REFERENCE

Run `methodology-close`'s Phases 1 through 3 **once**, against the **cumulative diff of every item
built in this batch** since the last BATCH-CLOSE (or since the run started, for the first batch) —
not against any single item's diff alone.

- Its **Phase 1 precondition** ("there must be a plan to check fidelity against") is satisfied by
  the batch's own instructions taken together — the plan-phase's stated scope, or the concatenation
  of the ad hoc instructions 0.2 read for each item in the batch. FIDELITY TO PLAN now means
  fidelity to *that*, not to one item's `WHERE` in isolation.
- Its **fan sizing, dispatch order, cache-priming step, and reconciliation** (§1.2–1.5) apply as
  written there, sized to the batch's own independent parts — which will usually be larger than a
  single item's, since a batch holds several items' worth of change.
- Its **Phase 2 order, apply-before-next-reads discipline, and the full pytest suite**
  (§2.1–2.4, CLAUDE.md §0.4) run once here, against the batch's full cumulative diff — this is the
  one point in a batch where the full suite runs at all; no item inside the batch ran it.
- Its **Phase 3 tier, escalation trigger, checklist, and the top-down/bottom-up handshake**
  (§3.1–3.7) apply as written there, run against the batch's post-Phase-2 diff. INTERDEPENDENCIES
  and the FORWARD/BACKWARD SWEEPS are more likely to find something real here than at single-item
  scale, precisely because several items have now landed together — that is the case BATCH-CLOSE
  exists to catch that per-item verification would have missed one item at a time.

Nothing in this section is restated in full here; a change to any of it is made once, in
`methodology-close`.

---

## GUARDRAILS

- **Phase 0 is additive, never a substitute** (see above). Reporting a batch as "built and closed"
  when only its items' Phase 0 ran, with no BATCH-CLOSE, is a false claim of the same shape
  `methodology-close`'s own falsifier table exists to catch.
- **Deferred is not skipped.** Batching BATCH-CLOSE to the phase or sub-batch boundary defers the
  expensive pass; it never licenses dropping it. A run that builds every item and never reaches a
  BATCH-CLOSE has not closed anything, whatever its commit count.
- **No new roster entry.** Phase 0 dispatches `valoria-author`; BATCH-CLOSE dispatches
  `valoria-critic`, exactly as `methodology-close` already does. Nothing here mints a third agent
  file.
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
| "the gate was met before building" | an item's `GATE` column named a position or a Jordan decision that had not actually landed |
| "the batch size was right" | a phase was carried whole through BATCH-CLOSE with no stated reason not to split it, or a sub-batch was split with no stated reason the whole phase would have been too large |
| "BATCH-CLOSE ran once per batch" | the full pytest suite, `/code-review`, `/simplify`, `layer-conformance`, the agonist/antagonist fan, or the terminal critique ran between two items of the *same* batch, or did not run at all before the batch's items were reported done |
| every Phase 1–3 claim, at BATCH-CLOSE | `methodology-close`'s own falsifier table, unchanged, checked against the batch's cumulative post-Phase-0 diff |

**If this skill's guidance conflicts with `CLAUDE.md`, `architecture/`, or `methodology-close`,
they win.** This file and `methodology-close` are methods; those are the rules, and
`methodology-close` is the senior method where the two overlap.
