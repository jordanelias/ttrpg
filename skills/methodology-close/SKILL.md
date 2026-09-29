---
name: methodology-close
description: >
  METHODOLOGY-CLOSE — the three-phase agonist/antagonist pipeline for verifying a nontrivial code
  change against a stated plan, before it closes. PHASE 1: a fan of Sonnet reviewers (agonists,
  effort high), each holding one lens over the diff, reconciled by a single Sonnet cross-examiner
  (antagonist, effort xhigh) checking accuracy, fidelity to plan, correctness, compliance with code
  architecture, and logic — the same five lenses double as the default agonist roster, sized to
  the plan's own independent parts, never a fixed count. PHASE 2: the native `/code-review --fix`,
  then `/simplify`, then the `layer-conformance` skill, run in that order on one shared tree, each
  one's fixes applied before the next reads it. PHASE 3: one terminal critique — Opus, effort
  xhigh, escalated to max only on a named trigger — auditing code correctness, interdependencies,
  and forward/backward sweeps, run as a top-down holistic pass that HANDSHAKES a bottom-up granular
  one (every altitude-level finding traced to the site that causes it, and back). Reuses
  `valoria-critic` for every critic dispatch in all three phases; mints no new roster entry. Use
  for: "run methodology-close", "close this position", a finished implementation that needs
  checking against its plan before `/close`, "agonist antagonist pass", "final adversarial
  critique", pre-commit deep review of a code change **that already exists**. If the diff does not
  exist yet and needs building first, use `methodology-execute` instead — it runs this pipeline as
  its own closing phases, verbatim, after its own build phase. Not for: design-quality grading
  (`ners`), a target that resolves by a draw (`resolution-diagnostic`), Layer placement checked on
  its own with no code change to verify (`layer-conformance` directly), or a change with no stated
  plan — write the plan first (CLAUDE.md §0's first bullet).
---

# METHODOLOGY-CLOSE — the agonist/antagonist verification pipeline

## Created 2026-09-28 (ED-IN-0280) as `methodology`, per Jordan's directive to add this pipeline as a skill. Split 2026-09-29 into `methodology-close` (this file, unchanged in content) and `methodology-execute` (adds a build phase ahead of it), when Jordan asked for the pipeline to also orchestrate the build. Invocable as a project skill through the symlink `.claude/skills/methodology-close`.

## What this skill owns, and what it copies

| the content | its single owner |
|---|---|
| the relay itself — stateless dispatch, what makes a critic independent, what a producer is handed and withheld | **CLAUDE.md §10** |
| model tiers, the effort ladder, and the fan-out sizing rule ("ask what N-1 would miss") | **CLAUDE.md §10** |
| structural read-only independence | **`.claude/agents/valoria-critic.md`** |
| correctness bugs in the current diff | the native **`/code-review`** |
| reuse, simplification, efficiency, altitude cleanup | the native **`/simplify`** |
| Layer placement and Layer-1 conformance | **`layer-conformance`** |
| design quality — N/E/R/S | **`ners`** |
| a target that resolves by a draw | **`resolution-diagnostic`** |

**This file owns the sequence**: which phase runs when, at what tier, checking what, and how a
holistic finding and a granular one must be traced to each other rather than filed as two
unrelated lists. It mints no guard, adds no roster entry, and produces no document — its output is
edits to the diff under review, plus at most one paragraph in the commit message, the same bound
`ners` and `layer-conformance` declare for themselves.

⚠ **Two words this file uses narrowly, scoped to itself.** `valoria-critic.md` names itself the
*antagonist* half of a *producer→critic* relay. Nothing dispatched below produces new code — every
dispatch in every phase is read-only. Inside this file, and only inside this file, **agonist**
means *one independent first-pass reviewer, holding one lens over an already-existing diff*;
**antagonist** means *the single reconciler that cross-examines every agonist's output against the
working tree*. Both roles run on the same tool-restricted agent (`valoria-critic`) — what differs
is the prompt: which lens, and whether it is handed one output or several. CLAUDE.md §4 binds a
coinage to mean one thing read cold; this paragraph is that definition, and it does not travel
back to `valoria-critic.md`'s own producer/critic sense — **nor does it travel forward into
`methodology-execute`'s build phase.** That skill's build dispatches are `valoria-author`, a
producer, and are never called agonist or antagonist; this is the one definition of both words in
the `methodology-*` family, and `methodology-execute` cites it rather than restating or widening
it.

**Relation to `/close` and to `methodology-execute`.** This pipeline runs *before* `/close`, on a
diff that is otherwise ready to commit — whether that diff already existed, or
`methodology-execute` just built it. `/close` step 4 also runs `layer-conformance`; Phase 2 below
is not a duplicate of that step, it is why that step should find nothing new by the time it runs.
`methodology-execute`'s Phases 1–3 **are** this file's Phases 1–3, invoked by reference, not
copied; a change to the sequence, the tiers or the checklists below is made once, here.

---

## THE THREE PHASES, AND WHY THE ORDER IS NOT NEGOTIABLE

```
PHASE 1 · AGONIST FAN → ANTAGONIST     lens-review the diff against the plan, cheap and early   ──▶
PHASE 2 · MECHANICAL GATES             code-review → simplify → layer-conformance, fixed        ──▶
PHASE 3 · TERMINAL CRITIQUE            Opus: holistic × granular, interdependencies, sweeps
```

Cheap and broad runs first. Phase 1's Sonnet fan catches gross deviations from the plan and
obvious bugs for a fraction of Phase 3's cost; Phase 2's native tools catch the mechanical classes
they already exist to catch. **Opus is reserved for last because it is the top of the tier ladder
and the judgment-node use case CLAUDE.md §10 names for it** — spending it on defects a Sonnet pass
would have caught is the tiering mistake §10 exists to prevent. Running the phases out of order, or
skipping one because an earlier one found nothing, is not a shortcut: each phase checks a different
axis, and a clean pass on one is not evidence about the others (see GUARDRAILS).

---

## PHASE 1 · THE AGONIST FAN, RECONCILED BY ONE ANTAGONIST

### 1.1 Precondition — there must be a plan to check fidelity against

CLAUDE.md §0's first bullet: state what changes, in what order, and how you will verify, before
the first edit. If nothing was stated, this skill has nothing to check "fidelity to plan" against.
Write the plan (even one sentence, for a small change) before dispatching anything below.

### 1.2 Size the fan — the checklist is the default roster, not a floor or a ceiling

The antagonist's checklist (1.4) doubles as the default set of agonist lenses:

| lens | what it reviews |
|---|---|
| **ACCURACY** | for every changed file, re-derive what changed and why, and check it against the plan — not against the diff's own commit message |
| **FIDELITY TO PLAN** | does the diff's scope match the plan's scope — nothing broader, nothing narrower, no silent substitution of one fix for another |
| **CORRECTNESS** | for the diff's own stated inputs, does the code do the right thing — a first bug pass |
| **COMPLIANCE WITH CODE ARCHITECTURE** | a first-pass placement sanity check only — *not* the full Lens A/B pass, that is Phase 2's job |
| **LOGIC** | is the control flow and conditional structure internally sound, independent of whether it is the *right* thing |

Collapse a lens that plainly does not apply (a one-line config change has no architecture surface
worth a dedicated pass). Split a lens further along component lines if the diff touches several
independent modules under one lens. Before adding a sixth agonist, or collapsing below five, name
what the change buys — CLAUDE.md §10: *"before spawning N agents, ask what N-1 would miss."*

### 1.3 Dispatch the fan

Each agonist is `Agent({ subagent_type: "valoria-critic", model: "sonnet", ... })`, prompted with
its one lens, the plan, and the diff — never the other agonists' output. State the effort in the
prompt itself (`Effort: high`): the Agent tool carries no effort field of its own, so this is the
only place to put it. **No `isolation: worktree`** — every Phase 1 dispatch is read-only, so there
is no write-write hazard to isolate against.

Fire the first dispatch alone, wait for its first streamed token, *then* send the rest in one
message. CLAUDE.md §10 point 3: parallel agents sharing a long prefix (CLAUDE.md, the plan, the
diff) cannot read each other's cache until the first response begins streaming — firing all of
them at once pays full price on every one.

### 1.4 The antagonist

One dispatch, same agent, `model: "sonnet"`, `Effort: xhigh` stated in the prompt. Hand it every
agonist's output — not their reasoning — plus the plan and the tree. Its job is `valoria-critic`'s
own contract, run once across all five lenses: re-verify every claim against disk; rule
`uphold`/`overturn`/`soften`/`sharpen` per claim; and additionally cross-check the agonists against
*each other* — two lenses disagreeing about the same site is itself a finding, not a tie to average
away.

### 1.5 Reconcile

The orchestrator — not a subagent — applies each surviving finding, or rejects it with the
measurement that rejects it. Never a bare "disagree." This is an edit to the diff, not a document.

---

## PHASE 2 · THE MECHANICAL GATES, IN ONE ORDER, ON ONE TREE

### 2.1 Why sequential, not fanned

Each of the three edits the tree it runs against. Running them concurrently is the write-write
hazard CLAUDE.md §10 reserves `isolation: worktree` for; none of the three is given one here, so
they queue.

### 2.2 The order, and why it is this one

1. **`/code-review --fix`** — correctness bugs first. Nothing else here is worth checking on a tree
   that still has an open correctness defect.
2. **`/simplify`** — reuse, simplification, efficiency, on the now-correct tree. It applies its own
   fixes by contract; no flag needed.
3. **`layer-conformance`** — placement and Layer-1 conformance, last. Its own doc places it at
   `/close` step 4 for the same reason: it wants the tree to have stopped moving before it grades
   placement.

### 2.3 Apply before the next stage reads the tree

A `/simplify` fix changes what `layer-conformance` will see. Grading the pre-simplify tree is
grading a tree that is about to change again — apply each stage's fixes in full before starting
the next.

### 2.4 layer-conformance's own trigger, not re-derived here

Run its Lens B always — by the time this phase runs, the diff is Layer-2 code by definition. Run
Lens A too if Phase 1 or `/code-review` added a tool, a guard, a hook, or a governance rule. Its
own A1–A5 decide anything finer; this skill does not restate them.

---

## PHASE 3 · THE TERMINAL CRITIQUE

### 3.1 One dispatch, not a fan

The point of the top tier is a single judgment pass. A chorus of Opus critics is the redundancy
CLAUDE.md §10 warns against, not corroboration. If you can name what a second Opus critic would
catch that the first missed, that is Phase-1-shaped work — run it there, at Sonnet, first.

### 3.2 Tier and escalation

`model: "opus"`, `Effort: xhigh` by default in the prompt. Escalate to `max` only on a named
trigger — e.g. the diff crosses a module boundary in `references/module_contracts.yaml`, touches a
Layer-1-governed surface, or Phase 1/2 already surfaced a STRUCTURAL-grade finding
(`layer-conformance` §B2's grade). Defaulting straight to `max` is the tiering mistake §10 exists to
prevent — name the trigger in the dispatch, or stay at `xhigh`.

### 3.3 What it is handed

The plan, the post-Phase-2 diff, and a bare receipt of what Phases 1–2 already changed — path plus
one line each, the same shape `valoria-author`'s own receipt takes — never their transcripts or
reasoning. Independence here is structural, the same as everywhere else in this pipeline: it comes
from what the critic is handed, not from how hard it tries not to peek.

### 3.4 The checklist

| item | what it means here |
|---|---|
| **CODE CORRECTNESS** | as 1.2's sense, re-run against the post-fix tree, not the original diff |
| **INTERDEPENDENCIES** | every caller/importer of anything the diff's signature-level changes touch, found by grepping the changed name across the *whole* tree, not just the diff's own files. The method is CLAUDE.md §0.1 pt 1's — grep the assignments and the callers, not just the readers the diff itself touched — and `layer-conformance` §B3's discipline applies: put a floor on what the scan covered and assert it |
| **FORWARD AND BACKWARD SWEEPS** | **backward** — does the diff still honour what every existing caller assumed before it landed. **forward** — does everything that will read the diff's new state or contract get it right. CLAUDE.md §0.1 pt 1's read/write-asymmetry hazard (a getter moves to a new source while a setter still writes the old field) is the canonical worked failure of exactly this pair |
| **LOGIC** | as 1.2's sense, re-run once more — a fix applied in Phase 1 or 2 can introduce a defect the earlier pass had no occasion to check |

### 3.5 The handshake — the one requirement this phase cannot skip

Two passes, and neither is a verdict alone:

- **TOP-DOWN (holistic)** — does the diff cohere with the plan, the architecture, and the rest of
  the system it now sits inside.
- **BOTTOM-UP (granular)** — does each individual site (a line, a function, a call) actually do
  what it claims, checked against disk.
- **HANDSHAKE** — every top-down finding is traced down to the specific granular site that produces
  it; *"this feels wrong at a high level"* is not a finding until it names a `file:line`. Every
  granular finding is traced up to whether it matters at the holistic level — severity is a
  top-down question. A granular defect with no holistic consequence is reported as downgraded, not
  dropped silently.

⚠ **This is not `ners`' six directions, and not its ladder-vs-aggregate reading of top-down and
bottom-up.** `ners` §0.06 and §7.1 ask whether a *design mechanic's* demand or opportunity travels
the game's own scales. This phase asks whether a *code change's* coherence travels between the
system's altitude and its own lines — a different axis wearing the same two words. Name which one
you are running, the same discipline `layer-conformance`'s A5 applies to the word "Layer."

### 3.6 Worked example

*A diff adds a `settlement.morale_eff` cached property and updates the three call sites its author
found.* **Top-down:** the change coheres with the plan ("cache the derived morale read") and the
architecture (one owner, one cache, one invalidation point) — passes. **Bottom-up:**
`grep -rn 'settlement\.morale ='` finds a fourth site, a test fixture, still assigning the *old*
field directly, never read by the new property — CLAUDE.md §0.1 pt 1's exact hazard. **Handshake:**
the granular finding is traced up — it makes that fixture's test silently assert against stale
data, a false green, which *is* a holistic consequence, so it is not downgraded. A critique
reporting only "coheres with the plan" (top-down alone), or only "one stale assignment at
`fixtures.py:214`" with no stated consequence (bottom-up alone), would each have missed half of
what made this a real finding.

### 3.7 Reconcile

Same as 1.5 — the orchestrator applies or rejects with a measurement, in this commit.

---

## GUARDRAILS

- **Produces edits, not documents.** No directory beyond `skills/methodology-close/`, no findings
  file.
  The prohibitions `layer-conformance` states in its own WHAT THIS PASS MAY NOT PRODUCE section —
  each with its own failure clause — bind here without restatement.
- **A clean phase is not evidence about the others.** Phase 1 finding nothing is not licence to
  skip Phase 2; Phase 2 finding nothing is not licence to skip Phase 3. Each checks a different
  axis (lens-reviewed, mechanically-gated, holistic×granular) and says nothing about the rest.
- **No new roster entry.** Every dispatch in every phase is `valoria-critic`; "agonist" and
  "antagonist" are prompt-assigned roles, not agent files. Promoting a distinct agent belongs to
  CLAUDE.md §10's roster discipline — only after a shape has recurred enough to need one, and this
  one does not yet.
- **Nothing here is a fixed count.** Fan size, the escalation trigger, and the lens roster are read
  from the diff and the plan at hand every time. An edit that hard-codes a number into this file is
  the defect §10 names: "sized for its typical subject, not for yours."
- **No self-scheduling** (CLAUDE.md §11, as always).

## FALSIFIERS

| the claim | what would show it false |
|---|---|
| "the fan matched the plan" | more or fewer independent lenses existed in the plan than agonists were dispatched, with no stated collapse or split reason |
| "the antagonist checked all five" | one lens has neither a finding nor a stated attack that failed |
| "code-review, simplify, and layer-conformance all ran, fixed" | no invocation record for one of the three, or a later one graded a tree still carrying an earlier one's unapplied finding |
| "the terminal critique handshook" | a top-down finding with no cited `file:line`, or a granular finding with no stated holistic disposition |
| "escalated to max" | no named trigger in the dispatch |
| "Phase 3 found nothing" | no named failed attack — only an absent finding |

**If this skill's guidance conflicts with `CLAUDE.md` or `architecture/`, they win.** This file is a
method; those are the rules.
