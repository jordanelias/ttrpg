---
name: efficient-coding-review
description: >
  ADVERSARIAL REVIEW OF A WHOLE SUBJECT, NOT A DIFF — attacks the code base (the engine, its modules and
  subsystems, a data family, a pipeline) or a work product (an analysis, research corpus, survey, proposal,
  plan or instrument) on six lenses run in a fixed order: a HIGH-LEVEL SURVEY first (a
  one-screen map), then ACCURACY (is each claim true, at its source), APPLICATION (does each idea
  transfer to the target, step by step), LOGIC (do the conclusions follow), ALL DIRECTIONS (the work
  and its subject walked by several routes and from several perspectives, not only the one it was
  built along) and ACROSS MODULES (a coverage matrix read from the registry). Output is a reply plus
  edits to the subject; no file, and no ledger row unless a ruling is owed. Use for: "adversarial
  review", "attack this", "review the engine / this module / this subsystem", "review my research / survey / proposal / plan", "did we apply the
  ideas", "does it work across modules", "work it from all directions", "survey it from a high
  level". Not for code diffs (/code-review), distilling unearned complexity (valoria-simplify), the cut
  test on a design object (ners), placement or
  Layer-1 compliance (layer-conformance), inert mechanics (valoria-mechanic-audit), or P-01..P-15
  (valoria-canon-guard).
---

# EFFICIENT-CODING-REVIEW — adversarial attack on the code base or a work product

## Status: RATIFIED on merge of its landing PR (CLAUDE.md §2, ED-1094; #518). Lane IN; no ED allocated. Invocable as a project skill through `.claude/skills/efficient-coding-review`.

## What this skill owns, and what it copies

**It owns the METHOD**: the six lenses and their order, the claim ledger, the route-and-perspective
sweep, the module matrix and the reply shape. It copies no rule; each is read at its owner, every time.

| the content | its single owner |
|---|---|
| how to ground a claim: absence, citation, "I ran it", claim versus support | **CLAUDE.md §0.1 pt 3** |
| one bar for favourable and unfavourable claims | **CLAUDE.md §0.1 pt 4** |
| one round then stop; the pass is a stage, not a deliverable; `needs_jordan` | **CLAUDE.md §0** |
| code is the mechanism, prose is reference | **CLAUDE.md §0.05** |
| what makes a critic independent; sizing a fan-out; reading is the cost | **CLAUDE.md §10** |
| the pass discipline (a named failed attack licenses a PASS; a null result needs its trail) | **`skills/ners` THROUGHLINE** |
| what the modules are | **`references/module_contracts.yaml`** (`composition_roles`) and **`CURRENT.md`** |

## ALL DIRECTIONS — what Jordan means

*"all directions refers to working through the pipeline/code/logic/systems/mechanics/workflows from
different perspectives and routes, not a specific NERS thing."* (Jordan, in session, 2026-10-28.)
It is a **method for any subject**: never review, or build, along only the one route the thing was
made along. **CLAUDE.md §0 owns the rule**; STEP 5 operationalises it for a review. It is not delegated to `ners`.

## THE THROUGHLINE

1. **Survey first, attack second, verdict last.** The map is an output, not a warm-up: it decides what
   is attacked in full and what is sampled.
2. **Accuracy and application are different objects.** A faithful summary of a finding that does not
   transfer passes STEP 2 and fails STEP 3. Run both; never let one stand in for the other.
3. **The work is reviewed as filed.** A claim the work does not make is not attacked; a limit the work
   dropped *is* (STEP 3, A4).
4. **A PASS is licensed by a named failed attack**, not by the absence of a finding — *"I attacked X as
   Y and it holds, because Z"*. A clean lens stands only on its trail. Never manufacture a finding.

## STEP 0 — FRAME (five lines)

Name: the **WORK** (paths, commit, PR) · its **PURPOSE** (the decision it informs) · its **TARGET**
(the system its ideas are applied to) and the **modules it says it reaches** · its **DECLARED STATUS**
(what it says it read, ran or checked) · **WHAT REVIEW IT ALREADY HAD** (commit message, PR body, any
critic pass). Attack what that review did not reach; **never re-audit its fixes** (CLAUDE.md §0).

When the subject is the **code base**, the WORK is the named engine area, module, subsystem or pipeline; its
claims are its docstrings, contracts, registries and tests, and ACCURACY is settled by running it (CLAUDE.md
§0.2), not by reading the prose about it. A diff of it stays with `/code-review`; removing unearned
complexity stays with `valoria-simplify`; placement and Layer-1 conformance stay with `layer-conformance`.

Resolve the target's canonical head first (`CURRENT.md`, then its `## Status:` line), then **the plan row
that names the work** (`CURRENT.md`'s plan row). The work is in one of **three states**: **CURRENT**;
**PARTLY RULED** — a ratified plan row already decided parts of it (carry each ruling into STEPS 3 and
6, part by part; a status line that does not point at the ruling is a SURVEY finding); or
**SUPERSEDED**, which voids STEP 3. If the work is yours or this session's, prepend
`[SELF-AUTHORED — bias risk]` and run STEPS 2–4 in a critic (Guardrails).

## STEP 1 — SURVEY (the first screen of the reply)

- **THESIS** — the headline in one plain sentence.
- **SPINE** — the hops from raw material to headline (e.g. *source → entry → instrument →
  application*). Every hop is a handoff STEP 5 walks.
- **CLAIM LEDGER** (≤ 25 rows): `id | claim | kind | status | load`.
  **Kind**: FACT · ATTRIBUTION · ABSENCE · COUNT · TRANSFER · INFERENCE · SCOPE. **Status**: what the
  work says it did to know it (read in full / secondary / ran / assumed). **Load**: HIGH when a false
  claim collapses a conclusion.
- **LOAD-BEARING SET** — every HIGH row, with the three thinnest named. The rest are sampled; **state
  the rate**.
- **SIZE** — counts from an instrument (`wc`, `grep -c`, a parse), never by hand.

A map that needs more than one screen is not yet a map: cut rows.

## STEP 2 — ACCURACY *(is it true?)*

For each load-bearing FACT, ATTRIBUTION, ABSENCE and COUNT, **observe before you rule** (CLAUDE.md §0.1
pt 3): open the locus; for an **absence**, RUN the search with its variants (spacing stripped, plural,
synonym, the neighbouring document where it might actually live); recount with a tool; check a
quotation verbatim. Then:

- **Strength ≤ status.** A conclusion drawn from a summary is stated as the summary's.
- **Claims about itself are claims.** "Verified", "checked", "N of M": was the check run, over what,
  with what control? A guard with no control (a check that cannot fail) is no check.
- **"Frozen", "pre-registered", "pinned", "reproduced" each name an artifact.** Recompute its hash or
  re-run it, and confirm the artifact frozen is the artifact that ran (a freeze of the predictions
  does not freeze the code they ran against).

Rule per claim: **UPHOLD · OVERTURN · SOFTEN · SHARPEN · UNVERIFIABLE** (the first four are `valoria-critic`'s vocabulary; UNVERIFIABLE is this skill's).

## STEP 3 — APPLICATION *(does the idea transfer?)* — six tests per TRANSFER row

| # | test | finds |
|---|---|---|
| A1 | **CONDITIONS** — what the idea's source needed to be true (domain, scale, user role, size of its evidence) | the unstated premise |
| A2 | **TARGET MATCH** — which of those hold in the target; name each that does not | a transfer across a gap |
| A3 | **PATH** — a shipped object (`file:line`) at every step where the idea binds in the target. An object at every step *constructs*; a step with none is *asserted*. Downgrade the verb to match (implementable → expressible) | an idea that has no place to land |
| A4 | **LOSS IN TRANSIT** — the source's own limits against the limits the work carries forward | a limit dropped between source and application |
| A5 | **ADDITION** — does applying it add an object, gauge, table or guard? | an object for `ners` to cut-test; flag it, do not rule here |
| A6 | **FALSIFIER** — one observation *in the target* that would show the idea wrong as applied | an idea unfalsifiable as applied |

An idea with **no external source** is `NO SOURCE (own)`: skip A1 and run A2–A6 against the target's
**ratified architecture** (axioms, plan rulings, `architecture/`). A ratified ruling that excludes the
idea ends the test: DOES NOT TRANSFER, citing the ruling.

Verdict per idea: **TRANSFERS · NARROWED** (say how) **· ASSERTED · DOES NOT TRANSFER.**

## STEP 4 — LOGIC *(do the conclusions follow?)*

For each HIGH inference write the chain (premises → conclusion, ≤ 5 links) and attack **each link**:

- **equivocation** (one word, two senses — state both) · **scope shift** (some → all, one → the class)
- **missing denominator** (a count without what it is out of)
- **independence overstated** — sources sharing authors, lineage or data counted as separate
  corroboration. *Count the overlap by instrument.*
- **circular validation** (an instrument confirmed on the cases that built it) · **survivorship**
- **cause from correlation** · **authority for evidence** (cited for prominence)
- **asymmetric skepticism** (CLAUDE.md §0.1 pt 4): was one bar applied to both directions?
- **the instrument shares its template with the treatment** (a metric scoring the same shape the
  treatment was built to produce) · **post hoc arms reported beside pre-registered ones** (see which
  results come from which)
- **a guard, filter or null that claims to exclude X: construct an X that passes it.** The first
  draft usually excludes the leak just found and admits the next one (WORKED EXAMPLE).

Then the **contradiction sweep**: two parts ruling one fact pattern opposite ways — match the pattern,
not the wording, and **include contradictions this work introduced**. Last, the **falsifier**: every
conclusion names what would overturn it; one that cannot is paper.

## STEP 5 — ALL DIRECTIONS *(routes and perspectives)*

Walk the **SUBJECT** (the pipeline, code path, logic, system, mechanic or workflow the work is about)
**and the work itself** by each route, and name a **carrier** — a table, a mapping, an index, a
function — or record the gap.

| route | the walk | what it finds |
|---|---|---|
| **FORWARD** | an input through every stage to the output, as one item would travel | a stage never mentioned; a stage whose output the next does not consume |
| **BACKWARD** | an output (a claim, a player-visible line) to its origin | an output with no producer; a claim with no source |
| **TOP-DOWN** | the purpose or headline requirement to the parts that must exist | a required part that is absent |
| **BOTTOM-UP** | one smallest unit to what it feeds; then recount the whole | totals that do not add up; an aggregate that gains or loses |
| **VERTICAL** | one item through every level of the spine | the hop where meaning is lost or inflated |
| **DIAGONAL** | an item from one level applied in a different family at another level | silence about the translation |
| **LATERAL / HORIZONTAL** | peers at one level: same method, same evidence bar? contradictions? double-counting? | an inconsistency; a convention used once; **a correction that reached one sibling and not the other** (stale figures) |
| **OFF THE HAPPY PATH** | empty, extreme, failed, partial, restarted, regenerated | breakage at an extreme; an unwritten branch |

Walk each route **as** a **CONSUMER** (player, reader, downstream module), a **MAINTAINER** (who must
change it), a **SKEPTIC** (who wants it false) and a **NEWCOMER** (ten minutes). Not every cell is
owed; **every empty cell the subject needs is a finding.** A carrier that names things that do not
exist *delivers blind* — the same defect one step later.

⚠ **BUILT-DIRECTION BIAS.** A work runs well in the direction it was built (usually bottom-up from its
inputs) and often only that one. The finding is the directions it cannot run.

## STEP 6 — ACROSS MODULES

1. **Derive the module list from the registry** (`references/module_contracts.yaml`
   `composition_roles`, `CURRENT.md`'s subsystem rows) — never from memory. **Add the host owners the
   work's own citations bind to** (the loop, queries, goal and roster loaders): a registry lists modules,
   but an idea often lives in host code no composition row registers, and a matrix of registered
   modules alone comes out all N-A.
2. **The matrix.** Rows: the modules, the host owners, plus the **seams** between them. Columns: the
   work's ideas, tests or gates. Each cell: **APPLIES** (carrier named, `file:line`) · **N-A** (why) ·
   **UNTESTED** (no evidence either way) · **CONTRADICTS** (the module's code or contract, or a ratified
   ruling that governs it — name which). Open the code or contract for every cell that is not N-A; a
   design doc is reference (CLAUDE.md §0.05).
3. **Survivorship.** Which module was the work built from? Report **UNTESTED out of the total**;
   invent no threshold.
4. **Seams.** An idea that crosses modules names the contract row (producer → consumer) that carries
   it; a crossing named nowhere is a gap.

## STEP 7 — THE VERDICT (the reply; nothing is written to a file)

```
EFFICIENT-CODING-REVIEW: <work>      [SELF-AUTHORED — bias risk]      ROUNDS: 1

IN PLAIN WORDS   <≤ 5 sentences: what it is · whether to rely on it · the three things that limit it most>

MAP              <STEP 1, corrected by what the attacks found>

| lens         | verdict          | what would overturn it |
| SURVEY       | PASS / FINDINGS  | a stranger given ten minutes cannot find the thesis, the limits and the next step — JUDGED BY DOING IT |
| ACCURACY     | PASS / FINDINGS  | <a claim, and the search or recount that would falsify it> |
| APPLICATION  | n TRANSFERS · n NARROWED · n ASSERTED · n DOES NOT | <the idea, and the target step with no object> |
| LOGIC        | PASS / FINDINGS  | <the link in the chain> |
| DIRECTIONS   | route × perspective grid: carrier or GAP | <the route the work cannot run> |
| MODULES      | APPLIES a · N-A b · UNTESTED c · CONTRADICTS d of N | <the module and the cell> |

MUST BE STATED AS A LIMIT      - <claim> — <why it is not carried>
MAY BE CLAIMED, HAVING SURVIVED - <claim> — <the attack run, and why it failed>

REPAIRS (worst first; each an EDIT: a corrected claim, a limit carried forward, a deletion, or one object)
  <finding> → <fix>

GRADE: paper | runs — <the execution artifact, or its absence>
```

- **The SURVEY row is a property of the work**, judged by doing it: open the work cold, time yourself,
  and report what you could and could not find.
- **GRADE is the row you cannot fill by writing** (CLAUDE.md §0.2): run something and paste what it
  said. A work with nothing running stays **paper**.
- **Apply the repairs in the same change.** A finding that needs no ruling is fixed or dropped; at most
  one `needs_jordan: true` row, after CLAUDE.md §0's five answer-it-first tests.

## GUARDRAILS

- **One round, then stop** (CLAUDE.md §0). Your own fixes are not re-reviewed; before any second wave
  of agents, stop and report what the first found.
- **Edits, not documents.** No `audit/` directory, no verdict file, no registry entry, no guard.
- **Independence is structural** (CLAUDE.md §10). Spawn `valoria-critic` per **disjoint read set**, not
  per lens: lenses reading the same text share a critic; a lens reading another tree takes its own.
  Hand it the OUTPUT and the step text, never your reasoning. When you authored the work, STEPS 2–4
  run in a critic; you run STEPS 0–1, the instrument counts and the verdict.
- **Reading is the cost** (CLAUDE.md §10). Extract once and hand the extract down; make no critic
  re-read what another already opened.
- **Re-open before you relay.** A critic's citation you have not opened is not a citation.
- **A critic limited to Read, Grep and Glob** may be steered off Grep over `.md` by
  `tools/hook_md_sweep_guard.py` (CLAUDE.md §8): hand it the file list to Read whole, or the extract.
- **Observe, do not rule, outside the lens.** Another lane's defect is an observation.
- **Parameters and rulings are Jordan's.** Report a tuned value as `[OPEN — Jordan tuning]`.
- **Never defend prior output** (`[SELF-AUTHORED — bias risk]`), and say what an independent reviewer
  would add.

## WORKED EXAMPLE — the move this skill exists to make

*A design defines an arc as an act linked by `causes[]` to a write on its actor and a write on the
world. Its first draft counted any Receipt; a review round found that witness bookkeeping met the
test, so the second draft restricted the effect fields to cells whose steps include `RES`.*

1. **STEP 4, the guard rule: build the leak that passes the fix.** The cells the roster names
   (`Person.body`, `Rung.stores`, `Site.condition`) have steps `[MAT, RES, …]` and class
   `MATTER/ACTS` in `write_matrix.yaml`. MATTER rewrites them every season, with `causes` chained to
   the subject's previous emission (`loop/matter.py`). The filter excluded the leak just found and
   admitted the next one.
2. **STEP 5, backward:** from an ARC that reads TRUE, trace the write that met clause (3). It can be
   MATTER's, not an act's.
3. **The repair is an edit, not a system:** key on the write's class, not on the field name, and plant a
   MATTER-chained case in the instrument's falsifier list.
4. **The grade, honestly:** the mechanism is shown at the cited lines; no run has produced an ARC that
   reads TRUE through MATTER. **GRADE: paper.**
