---
name: premise-check
description: >
  PREMISE-CHECK — does a gameplay element, AS CODED AND RUN, do what its premise says, in the
  sense a videogame player and an ordinary reader of its words would expect? The unit is a
  PREMISE SENTENCE ("a person holds an office in a faction and issues a decree the others follow")
  or a named element (a verb, track, stat, level, clock, office). The method: break the premise
  into a chain of plain-English links, write what each link should do BEFORE reading its code,
  locate the code that owns each link, RUN the smallest world that exhibits the premise with four
  controls, and compare. Three questions, one oracle: would a player who knows strategy/RPG games
  be surprised (genre)? does the behaviour correspond to the premise (intent)? do the results
  make sense of the words it uses (names, parameters, levels, values)? Verdict by execution,
  never by reading the code or the design prose. Use for: "does this work the way it should",
  "does the code do what the design says", "does X behave the way the word suggests", "premise
  check", "sanity check this mechanic", "play it through", "does a decree actually bind",
  "does this make sense as a game", "does the behaviour match the prose". Not for internal
  formula consistency with no run (valoria-mechanic-audit), the properties of a draw
  (resolution-diagnostic), the cut test (ners), P-01..P-15 (valoria-canon-guard), or a diff
  (/code-review).
---

# PREMISE-CHECK — does the running code do what the sentence says?

## Status: PROPOSED — ratified on merge of its landing PR (CLAUDE.md §2, ED-1094). Lane IN; no ED allocated. Invocable as a project skill through `.claude/skills/premise-check`.

## What it asks

1. **Genre.** Would a player of strategy and role-playing games be surprised by what happened?
2. **Premise.** Does the behaviour correspond to the premise as stated: the right actor, the right
   standing, the right addressees, the right effect?
3. **Words.** Do the outcomes make sense of the words the element is built from: its names, its
   parameters, its ordered levels, its values?

**All three are answered by running the premise.** Reading the code answers what the author meant;
reading the prose answers what the designer meant; only a run answers what the game does.

## The oracle, and what is not one

Ranked, and written down **before** the code is opened (STEP 2):

1. **The premise as stated** — the user's sentence, or a quotation from design prose. Prose is
   admissible here as **intent** (CLAUDE.md §0.05: "only for intent, history and vocabulary").
   It is the claim under test, never the reason the code is right.
2. **The ordinary meaning of its words** — the dictionary sense, not the repo's gloss. Where the repo
   has coined or repurposed a word, the test is CLAUDE.md §4's: a reader with no memory of this repo
   must land on the meaning. This skill is that rule's behavioural half.
3. **Genre convention** — stated as a general rule ("a resource at zero stops what it paid for").
   Name a particular game only when it is the sharpest precedent, and tag it `[UNVERIFIED]` unless
   checked.

**Not oracles:** the code's own docstrings and registry notes (claims under test); a design doc's
`## Status:` line (§0.05); the author's reasoning. The siblings own different questions —
`valoria-mechanic-audit` (internal consistency, no run), `resolution-diagnostic` (properties of a
draw), `ners` (the cut test), `valoria-canon-guard` (P-01..P-15), `efficient-coding-review` (a whole
subject's claims). This skill's difference is an oracle **outside** the repo's own definitions,
applied by execution.

## STEP 0 — FRAME

Write down: the **PREMISE** (one sentence, verbatim) and its **source** (the user, or `path` and
quoted text) · the **ELEMENT's head** (resolve through `CURRENT.md`, then its `## Status:`) · whether
a **successor ruling** already decided part of it (read the lane's `HANDOFF_<LANE>.md`; carry a ruling
into STEP 5 rather than re-litigating it) · **what review it already had**.

No GM exists (CLAUDE.md, opening): the engine resolves everything, so a premise that "a person does X"
is a claim about what the **decision layer forms and the resolver executes**, not what a human would
narrate. Hold that through every step.

## STEP 1 — DECOMPOSE INTO THE CLAIM CHAIN

Split the sentence into **links**, in the order a play-through would meet them. Nouns become **state**,
verbs become **acts**, and quantifiers, prepositions and adverbs ("a", "the others", "within", "for")
become **scope** — the usual hiding place of a broken premise. Each link gets a number and one plain
sentence. Typical shape: *actor exists → holds standing → performs act → act reaches addressees →
addressees respond → response changes the world → the world shows it*.

**Do not merge links.** "Others follow" is at least three: who counts as an other, what following is,
and what following changes. A chain of five to ten links is normal; more means the premise is two.

## STEP 2 — PREDICT BEFORE YOU READ

For every link write, **before opening any implementing file**, what a player would expect. Use these
classes as columns; skip one only by saying why it does not apply.

| # | class | the expectation, in plain words |
|---|---|---|
| E1 | **Standing** | Who may do this: the holder, here, now. A stranger, a holder of another body, a former holder and a vacated seat are refused — and the refusal is *visible*, not silent. |
| E2 | **Act** | It happens as a single event with an author and a time, and leaves a trace. |
| E3 | **Scope** | "Others" means a definite set. Name it: all of the body, those below the rung, those named. Who is inside it and who is not. |
| E4 | **Effect** | Direction (obeying does what was ordered, not its opposite), proportion (stronger authority, stronger effect; ordered levels give ordered results), zero (no decree, no change). |
| E5 | **Refusal** | The addressee may refuse; refusing has a cost or a consequence the issuer can see. An authority that cannot be defied is a script; one whose defiance is free is decoration. |
| E6 | **Time** | When it takes effect, how long it lasts, what ends it; the pace suits the calendar (a decree is not weather). |
| E7 | **Reversal** | Revocation, expiry, the issuer leaving office or dying: what becomes of what they issued. |
| E8 | **Conservation** | What is spent, created or moved arrives somewhere; nothing is made from nothing; what is shown as owed is owed. |
| E9 | **Bounds** | Empty, one, many; floor, ceiling; a body with no members; an office with two holders; a value at 0 and at its maximum. |
| E10 | **Feedback** | The issuer and the addressee can each tell, from the record, that it happened and why. |
| E11 | **Neighbours** | Opposites act oppositely (issue and revoke, comply and defy, appoint and dismiss); near-synonyms differ in something nameable. |
| E12 | **Genre sins** | A value that changes nothing (dead); an option always best (dominant); a state with no exit (softlock); a loop that pays more than it costs; a number shown that is not the number used; the same seed giving a different world. |

Each cell holds a prediction **a run could contradict**. "It should work" is not one.

**Blind predictions (recommended once the code has been read, or for six or more links).** The author
of a prediction who has read the implementation predicts what the code does. Hand a fresh-context
agent only the premise and the word list, and have it fill STEP 2's table; compare against yours.
Where the two disagree, the words are ambiguous (record both readings as AMBIGUOUS in STEP 5). This is
the one place a second agent buys independence (CLAUDE.md §10): the **reading** is shared, the
**oracle** is forked. One agent, `sonnet`; a second wave is scope growth (§0).

## STEP 3 — LOCATE THE OWNER OF EACH LINK

Open the code only now. For each link name the **owner at `file:line`**, or write **NO OWNER**: the
premise names it and no code does. Read the **call site**, not the declaration (CLAUDE.md §0.1 pt 3):
a roster existing is not a roster being used.

| the link is a… | look in |
|---|---|
| noun, a standing or a term | `engine/engine_params/names.json` through `engine/substrate/names.py` (an ambiguous display string raises; pass the key); `engine/engine_params/descriptors.json` through `engine/substrate/descriptors.py`; `engine/season/offices.yaml`, `rosters.yaml`; state in `engine/season/state/` |
| verb, an act | the row in `engine/season/verb_table.yaml` (`eligibility`, `requires_typed`, `writes`, `emits`, `emits_on_refusal`) and its effect in `engine/season/loop/effects_*.py` |
| scope, who it reaches | `loop/predicates.py`, `queries/`, the verb's `scale`, `counterparty` and `referent_class` |
| a response, another's act | the answering verb's row, and the decision code that FORMS it: `engine/season/decision/` — an act nobody is ever offered does not happen |
| a number, a level, a bound | `engine/engine_params/*.json`, the single Python owner, or the constant in `systems/` / `modules/` (the migration backlog, CLAUDE.md §0.05) |
| a module's resolution | `references/module_contracts.yaml` `composition_roles` → `engine/engine_params/composition.json` |
| a word | `references/names_index.yaml` (the owner), `references/descriptor_registry.yaml` |

A column in the verb table that says `writes: []` and a note that says "emission only" is a finding in
waiting: the act announces and changes nothing. Carry it to STEP 4 to see whether anything else does.

## STEP 4 — RUN IT

Build the **smallest world** that exhibits the premise, seeded, then execute. Fixtures live in
`engine/season/harness/`: `governance_spine.build` (a regular spine of seats — a **test fixture, not
canon**), `populated.build_realm` (the authored realm), `scarce`, `corpus_run.build_at`,
`headless` (`--case --seasons --seed --log` prints the Event log with its `causes[]`), `play_surface`
(a hand-built act through `dispatching_chooser`).

**Three depths of "it happens" — report which one you reached.** The first is the weakest and the one
most often mistaken for the second.

| depth | meaning | how to see it |
|---|---|---|
| **EXECUTES** | a hand-built act, given the right state, produces the effect | call the resolver with that act |
| **FORMS** | the decision layer offers the act to someone who would take it | read the opening set for that person; count the offers |
| **FIRES** | it appears in a seeded season with no hand in it | run N seasons; count occurrences, state N and the seeds |

With no GM, a premise that EXECUTES but never FORMS is **half-true**: a player's menu may reach it, a
world full of other people never will.

**Four controls — a result without them is not a measurement (§0.1 pt 4):**

- **P — positive.** Every condition of the premise holds. The act must succeed. A refusal here means
  the chain broke at the first link; do not read on as if it ran.
- **N — negative, one condition at a time.** Not the holder; a holder of another body; the wrong rung;
  the seat vacated. Each must be refused with a keyed, visible reason. A negative control that still
  succeeds is a standing defect (E1).
- **Z — null.** Same seed, same world, no decree. The addressees' behaviour must be what it was. This
  is the baseline the effect is read against.
- **C — counterfactual pair.** Same seed, decree against none. The difference must trace, through
  `causes[]`, to the decree. A difference that does not trace is noise; a decree with no difference is
  INERT.

Also: run twice on one seed and compare `World.content_hash()` (E12). **Check the run happened**
(§0.1 pt 3): diff the world before and after, assert the event was emitted, assert the loop asserted.
A test that skips, or a harness that returns 0, observes nothing.

**Sweep the words.** Where the premise uses ordered levels or a parameter ("minor … major", a rank, an
office's rung), run the whole ordered set once and read the effect against the order (E4, E11). A
non-monotonic or flat response to words that are ordered is a finding by itself.

A single seed is an instance, not a rate. Say n.

## STEP 5 — COMPARE, CLASSIFY, RANK

**Verdict per link:**

| verdict | meaning |
|---|---|
| **FOLLOWS** | observed, and as predicted |
| **DEPARTS** | observed, and differs |
| **INVERTED** | does the opposite of what its word says |
| **INERT** | code exists; a run that should reach it never does, or the effect is nil |
| **ASSERTED** | the premise names it; **no code owns it** |
| **UNREACHED** | an earlier link broke, so this one was not tested. Not a pass, not a fail |
| **AMBIGUOUS** | the words support two readings and the code picks one; name both |

**Cause, for DEPARTS, INVERTED and INERT:** **WORD** (the behaviour is sensible, the name misleads →
rename at its owner, `references/names_index.yaml`) · **BEHAVIOUR** (the word is right, the code is
wrong → change the code) · **EDGE** (fine mid-range, absurd at a reachable extreme) · **COMPOSITION**
(each link fine, the chain absurd) · **STALE-PROSE** (the prose was superseded; cite the successor, and
the prose changes) · **DELIBERATE** (a documented design departure, with its reason).

**Intent gate (as `resolution-diagnostic` Phase 5).** Deliberate, with an adequate safeguard: PASS
with a note. Deliberate without: finding. Accidental or undetermined: finding, tagged
`[INTENT UNDETERMINED]`. A departure claimed for a philosophical reason goes to `valoria-canon-guard`;
adjudicating P-01..P-15 is not this skill's.

**When prose and code disagree.** CLAUDE.md §0.05: decide, then change the code — a design document is
not edited to match code, and code is not left wrong because a document says so. Before flagging
anything `needs_jordan`, answer it by §0's five-step ladder (superseded · irrelevant · answered by a
document · answered by precedent · answered by what the architecture makes obvious). Escalate only
what survives: two defensible options that make materially different games.

**Rank worst first, by what a player would conclude, not by a score:** a link the premise cannot do
without that is ASSERTED or INVERTED → a DEPARTS on the ordinary path → INERT → an EDGE or COMPOSITION
failure at a reachable extreme → a WORD defect. **Tuned values are Jordan's:** "major is 1.0 or 1.2" is
not a finding; "major is not larger than minor" is.

## STEP 6 — PLAY IT BACK

Narrate the control-P run's Event log in plain English, three to six sentences, as a player who never
saw the code would tell it to a friend. Set it beside the premise sentence.

- A sentence you cannot write without repo jargon is an E10 finding: the player cannot tell.
- Each "wait, what?" is a candidate: trace it to a link, or discard it with a reason.
- A sentence the log supports and the premise does not say is a surprise the premise did not warn of.

This is the step that catches COMPOSITION failures the link-by-link table passes.

## STEP 7 — OUTPUT

**The first sentence is the verdict:** *the premise holds* / *holds to link k, then breaks* / *does
not hold*, and at which depth (EXECUTES, FORMS, FIRES). Then:

1. The **link table**: `# | link | predicted | observed | verdict · cause | file:line | the call that reproduces it`.
2. The play-back paragraph.
3. **Edits**, for every finding that needs no ruling (§0: fixed in this commit or dropped). A
   behaviour fix carries a test that **executes** the corrected behaviour; the failing probe from
   STEP 4 *is* that test, with its control shown. Registry renames go through the owner.
4. A `needs_jordan` row only for what survived the ladder.

The output is a reply plus edits and at most one commit paragraph (§0). **No audit directory, no
document that creates work for a future session, no guard** (§0.1 pt 5): this skill's findings are
about the game, but a sweep over every premise is exactly the tree-wide guard CLAUDE.md §0.05 does
not license. **One round, then stop** (§0): its fixes are not themselves re-audited.

## GUARDRAILS

- **Predict first.** A prediction written after reading the code is a description of the code.
- **Report the first break; do not paper over what follows.** Links after it are UNREACHED.
- **A hand-built act is evidence of EXECUTES only.** Do not write "the game does X" from it.
- **Absence is a claim.** "Nothing enforces this" is stated only after the search that would find it,
  with its variants (§0.1 pt 3).
- **Not a balance verdict.** "Too strong", "too weak" need a campaign-level instrument (CLAUDE.md §7);
  this skill reports sense, direction, scope and reachability.
- **Do not build the premise.** A link with NO OWNER is reported as ASSERTED. Inventing the missing
  mechanism to make the run pass is scope growth.
- **A fixture is not canon.** State which world the run used and what it does not show.
- **Size to the subject.** One reader runs a premise; a second agent is the blind predictor or a
  critic on a judgment call, never a copy of the first.

## WORKED STARTING POINT — "an officeholder issues a decree and the others follow"

**Leads read from `verb_table.yaml`'s own rows and notes. They have NOT been run; each is a
prediction to attack in STEP 4, not a finding.**

| link | the owner to open | what the table's own text already suggests testing |
|---|---|---|
| L1 holds office in a faction | `offices.yaml` seats (`post`, rung anchor, `body`, `remit_acts`, `holder`); the tenure in `state/world.py` | N controls: the holder of another body's seat, a vacated seat |
| L2 issues a decree | `issue` (`eligibility: remit:issue`; `writes: Record.exists`; emits `dispensation.issued`; refusals keyed `issue.unauthorized` / `issue.refused`); `dispatch` (emits `order.given`, `writes: []`) | `issue` carries one `counterparty: to`: one addressee per act. Is "the others" one act or many? A body-wide `proclaim` is recorded as deferred (K-50) |
| L3 it reaches the others | the writ is a Record held by its addressee (`loop/witness.py` content deposit); `comply` is offered "only to a writ's addressee who holds it" | FORMS: count who is offered `comply`. A non-addressee member of the same faction |
| L4 they follow | `comply` → `compliance.given`; `evade / defy` → `compliance.withheld`; `construe` → `terms.distorted` | `comply` and `defy` have `writes: []` and are **emission-only**; the table says what compliance *performs* is "the separate act". Does anything change in a C pair? E5: does defying cost anything? |
| L5 the world shows it | the Event log with `causes[]` | STEP 6: can the play-back be told without jargon? |
| `dispatch` as the decree | the `issue`/`dispatch` split | the table records that a dispatched order "mints no Record", so there is no writ for `comply` to answer |

The shape of the likely verdict, if these leads hold, is a chain that EXECUTES to L2, then narrows at
L3 (one addressee) and goes thin at L4 (announcement without consequence). Treat that as a hypothesis
the first run confirms or breaks.
