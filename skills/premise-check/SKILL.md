---
name: premise-check
description: >
  PREMISE-CHECK — does a gameplay element, AS CODED AND RUN, do what its premise says, in the
  sense a videogame player and an ordinary reader of its words would expect? Scoped to the
  ELEMENT A PR TOUCHES (default: the PR's claims yield one or more premise sentences, each tested
  end to end), or to a SLICE the user names explicitly. The method: break each premise into a chain
  of plain-English links; write what each link should do from the ordinary meaning of its words
  BEFORE reading any note or code; build a second account from the code's own notes in aggregate;
  locate the code that owns each link; RUN the smallest world that exhibits the premise with
  controls; and compare three accounts (ordinary understanding, the notes, the running code).
  Three questions: would a player who knows strategy/RPG games be surprised (genre)? does the
  behaviour correspond to the premise (intent)? do the results make sense of the words (names,
  parameters, levels, values)? Verdict by execution, never by reading code or prose. Engine
  behaviour only; presentation layers are out of scope. Use for: "does this work the way it
  should", "does the code do what the design says", "does X behave the way the word suggests",
  "premise check", "sanity check this mechanic", "play it through", "does a decree actually bind",
  "does the behaviour match the notes". Not for internal formula consistency with no run
  (valoria-mechanic-audit), the properties of a draw (resolution-diagnostic), the cut test (ners),
  P-01..P-15 (valoria-canon-guard), or the lines of a diff (/code-review).
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
reading the notes answers what the designer recorded; only a run answers what the game does.

"Player" here means someone who can see consequences in the **engine's own outputs**: the Event log
and its `causes[]`, the world state, and what the decision layer offers an actor. Menus and any
presentation layer are out of scope.

## Scope

| scope | when | the premises come from | the chain covers |
|---|---|---|---|
| **PR** (default) | a PR, or a diff, is the subject | what the PR claims the element now does, put in plain words from its description and commit message. The notes it adds or changes are read in STEP 2b, not here. **A PR typically involves an entire element**, so it usually yields several premises (a combat PR: fighting, wounds, yielding) | the element **end to end**, links the diff did not touch included: a changed link can break its neighbours. Another element's broken link gets one line, "outside this PR", and no fix (CLAUDE.md §0: the request is the scope) |
| **SLICE** (explicit only) | the user names a slice: an element with no PR behind it, or a cut that crosses elements | the user's sentence, or the notes aggregate (STEP 2b) alone, and STEP 0 says so | the named **boundary**: an entry link and an exit link, or the verbs and files it covers. A slice with no boundary is the whole element; ask for one |

**Never widen a PR run to a slice on your own.** If a slice run looks worthwhile, say so and ask.

## The oracle, and what is not one

Ranked, and written down **before** the notes or the code are read (STEP 2):

1. **The premise as stated** — a user's sentence, or what a PR claims. Prose is admissible as
   **intent** (CLAUDE.md §0.05: "only for intent, history and vocabulary"). It is the claim under
   test, never the reason the code is right.
2. **The ordinary meaning of its words** — the dictionary sense, not the repo's gloss. Where the repo
   has coined or repurposed a word, the test is CLAUDE.md §4's: a reader with no memory of this repo
   must land on the meaning. This skill is that rule's behavioural half.
3. **Genre convention** — stated as a general rule ("a resource at zero stops what it paid for").
   Name a particular game only when it is the sharpest precedent, and tag it `[UNVERIFIED]` unless
   checked.

**Not oracles:** the code's docstrings and `*_note` columns (claims under test, and they are dense:
see STEP 2b); a design doc's `## Status:` line (§0.05); the author's reasoning.

Siblings own other questions: `valoria-mechanic-audit` (internal consistency, no run),
`resolution-diagnostic` (properties of a draw), `ners` (the cut test), `valoria-canon-guard`
(P-01..P-15), `efficient-coding-review` (a whole subject's claims). This skill's difference is an
oracle **outside** the repo's own definitions, applied by execution.

## STEP 0 — FRAME

Write down: the **PREMISE(S)**, verbatim, and the source of each (the user; or the PR claim and its
path; or `[ASSUMPTION]` where you rendered a bare word like "combat" into a sentence) · the **scope**
(PR or SLICE, and the slice's boundary) · the **element's head** (resolve through `CURRENT.md`, then
its `## Status:`).

Scoping reads **names only**: `CURRENT.md`, the verb names in `verb_table.yaml`, file lists. It does
not read the notes that describe behaviour, the standing orders, the hole register or the code:
those wait for STEP 2b, after O is written. **Write each premise sentence from the user's words or
the PR's description, not from the diff's docstrings.** A reviewer who has already read those notes
will write O as a paraphrase of N, and the "O = N" row below then fires by construction. In PR scope,
therefore, **the blind predictor (STEP 2) is the default**, fed only the premise sentences.

No GM exists (CLAUDE.md, opening): the engine resolves everything, so "a person does X" is a claim
about what the **decision layer forms and the resolver executes**, not what a human would narrate.

## STEP 1 — DECOMPOSE INTO THE CLAIM CHAIN

Split each premise into **links**, in the order a play-through would meet them. Nouns become
**state**, verbs become **acts**, and quantifiers, prepositions and adverbs ("a", "the others",
"within", "for") become **scope** — the usual hiding place of a broken premise. Each link gets a
number and one plain sentence. Typical shape: *actor exists → holds standing → performs act → act
reaches addressees → addressees respond → response changes the world → the world shows it*.

**Do not merge links.** "Others follow" is at least three: who counts as an other, what following is,
and what following changes. A chain of five to ten links is normal; more means the premise is two.

**Mark dependencies, provisionally.** Note which links appear to need which; links that share no
dependency are **independent branches** (a persuasion premise's trust, skill and conviction do not
depend on one another). This is a guess from the words. **Re-mark in STEP 3**, once the owners are
known, because a wrongly assumed dependency leaves a link UNREACHED and hides a second bug.

## STEP 2 — PREDICT BEFORE YOU READ (the ordinary account, O)

For every link write, **before opening any note or implementing file**, what a player would expect.
Use these classes as a checklist. **Fill a cell only where the class applies**, and skip a class with
one word ("n/a: no addressee"). Tag a cell **[GENRE]** when the premise's own words do not imply
that class: a genre expectation the premise never promised ranks lower in STEP 5.

| # | class | the expectation, in plain words |
|---|---|---|
| E1 | **Standing** | Who may do this: the holder, here, now. A stranger, a holder of another body, a former holder and a vacated seat are refused — and the refusal is *visible*, not silent. |
| E2 | **Act** | It happens as a single event with an author and a time, and leaves a trace. |
| E3 | **Scope** | "Others" means a definite set. Name it: all of the body, those below the rung, those named. Who is inside it and who is not. |
| E4 | **Effect** | Direction (obeying does what was ordered, not its opposite), proportion (stronger authority, stronger effect; ordered levels give ordered results), zero (no decree, no change). |
| E5 | **Refusal** | The addressee may refuse; refusing has a cost or a consequence the issuer can see. An authority that cannot be defied is a script; one whose defiance is free is decoration. |
| E6 | **Time** | When it takes effect, how long it lasts, what ends it; the pace suits the calendar. |
| E7 | **Reversal** | Revocation, expiry, the issuer leaving office or dying: what becomes of what they issued. |
| E8 | **Conservation** | What is spent, created or moved arrives somewhere; nothing is made from nothing. |
| E9 | **Bounds** | Empty, one, many; floor, ceiling; a body with no members; a value at 0 and at its maximum. A state the mechanism treats as immovable or unmovable at its extreme end should be so for a reason the words give. |
| E10 | **Feedback** | The actors can tell, from the engine's record, that it happened and why; a label means what it says (a result called "won" moved something). |
| E11 | **Neighbours** | Opposites act oppositely (issue and revoke, comply and defy, appoint and dismiss); near-synonyms differ in something nameable. |
| E12 | **Genre sins** | A value that changes nothing (dead); an option always best (dominant); a state with no exit; a loop that pays more than it costs; a number shown that is not the number used; the same seed giving a different world. |

Each cell holds a prediction **a run could contradict**. "It should work" is not one.

**Blind predictions (recommended once the code or notes have been read, or for six or more links).**
Hand a fresh-context agent only the premise and the word list, and have it fill this table; compare.
Where the two disagree, decide which is the error: mark the link AMBIGUOUS (STEP 5) **only if both
readings can be stated from the words alone**; otherwise one predictor erred, and the link keeps the
prediction that the words support. Reading is shared, the oracle is forked (CLAUDE.md §10). One
agent; the tier is the §10 calculation, `sonnet` when the table is long.

## STEP 2b — THE NOTES IN AGGREGATE (the designer's account, N)

This codebase documents itself densely: docstrings, `*_note` columns in `verb_table.yaml`, hole
register rows, ruling quotations. Read together, they are a statement of what the element is meant to
do. Use them as one, **after O is written and before the run**:

0. **Collect the standing rulings first** (they are N's spine): the lane's `HANDOFF_<LANE>.md`,
   `engine/season/hole_register.yaml` (it names a missing mechanism in one read), and a grep of the
   owner's docstrings for `ED-`, `RULED`, `HELD`, `ASSUMPTION` — a successor ruling often lives only
   in a docstring.
1. **Extract once, cheaply, if the notes are many.** A `valoria-measure` (Haiku) pass collects every
   note on the element's links, with `file:line`; for a handful of notes, read them yourself (§10's
   overhead calculation). **One reader** then builds N: a short coherent account in plain words of
   what the notes say the element does and does not do. That reader never sees the run's results.
2. **Resolve disagreement inside N.** Notes carry rulings from different dates. The latest ruling
   wins (CLAUDE.md §0's ladder). A disagreement it does not settle is a finding on the notes.
3. **A note is a claim, not evidence.** "X happens" becomes a run target. A note that records its own
   limit ("writes nothing", "emission only", "not answered", "HELD") is a lead the run confirms:
   report it as a **known limit confirmed**, not as a discovery.

**Three accounts, compared in STEP 5.** O (ordinary understanding), N (the notes), C (the code, run):

| pattern | reading |
|---|---|
| O = C, N differs | the notes are stale; the code is fine. **Unless N's latest item is a ruling**: then the code merely agrees with ordinary meaning while lagging the ruling, which is a BEHAVIOUR finding or goes up §0's ladder, not STALE-PROSE |
| O = N, C differs | **the code is wrong**: fix it |
| N = C, O differs | the code does what its notes say, but the design does not make plain sense |
| all three differ | layered rulings that disagree with each other as well as with the code |

The verdict is always C against O. N says what was *meant*, and so tells you which side of a
disagreement to change.

## STEP 3 — LOCATE THE OWNER OF EACH LINK

Open the code now. For each link name the **owner at `file:line`**, or write **NO OWNER**. Read the
**call site**, not the declaration (CLAUDE.md §0.1 pt 3): a roster existing is not a roster being used.

| the link is a… | look in |
|---|---|
| noun, a standing or a term | `engine/engine_params/names.json` through `engine/substrate/names.py` (an ambiguous display string raises; pass the key); `descriptors.json` through `descriptors.py`; `engine/season/offices.yaml`, `rosters.yaml`; state in `engine/season/state/` |
| verb, an act | the row in `engine/season/verb_table.yaml` (`eligibility`, `requires_typed`, `writes`, `emits`, `emits_on_refusal`) and its effect in `loop/effects_*.py`. Rows are named `evade / defy`, `tie / knot`: match the exact string |
| scope, who it reaches | `loop/predicates.py`, `queries/`, the verb's `scale`, `counterparty`, `referent_class`; ⚠ a document or writ may reach its addressee by a *separate* act (`give`), not by the issuing act |
| a response, another's act | the answering verb's row, and the decision code that FORMS it: `engine/season/decision/` — an act nobody is ever offered does not happen |
| a number, a level, a bound | `engine/engine_params/*.json`, the single Python owner, or the constant in `systems/` / `modules/` |
| a module's resolution | `references/module_contracts.yaml` `composition_roles` → `composition.json` names the entry (e.g. role `combat.fight` → `modules/combat/fight.py`). ⚠ **A module and the season loop may differ**: the module can implement a premise the season-scale wrapper never feeds (a wrapper that derives one field and defaults the rest). Treat them as two scales (STEP 4) |
| a word | a state, stat or term: `references/names_index.yaml` (the owner), `references/descriptor_registry.yaml`. **A verb or an event kind: its key in `engine/season/verb_table.yaml`**, not the names index |

**Re-mark STEP 1's dependencies here**, now that the owners are known.

A `writes: []` column plus a note saying "emission only" is a finding in waiting: the act announces
and changes nothing. Carry it to STEP 4 to see whether anything else does.

## STEP 4 — RUN IT

Build the **smallest world** that exhibits the premise, seeded, then execute. Fixtures in
`engine/season/harness/`: `probes.tiny_world` and `governance_spine.build` (**test fixtures, not
canon**; fast, use for EXECUTES), `populated.build_realm` (the authored realm; use for FIRES only),
`scarce`, `corpus_run.build_at`, `headless` (`--case --seasons --seed --log` prints the Event log
with `causes[]`), `play_surface` (`dispatching_chooser`).

**Recipes for a hand-built act** (the test files hold working examples; copy their shape):
`engine/season/tests/test_in10_record_operands.py` (`_resolve`, `_formed`: drive an act and ask what
is offered), `test_in18_obligee_report.py` (`_tell`), `test_season_shape.py` (`_we_bands`: a contested
act through `SeasonDriver.resolve` and `encounter`), `test_fi03_trail.py` (`trail_world`). For
independent draws vary the act id (`Act(id=f"x{i}")`) and use a fresh world per trial. Some helpers
live in pytest modules, and pytest may not be installed: run `python tools/session_provision.py`, or
stub the import.

**Three depths of "it happens" — report which you reached.** The first is the one most often
mistaken for the second.

| depth | meaning | how to see it |
|---|---|---|
| **EXECUTES** | a hand-built act, given the right state, produces the effect | call the resolver with that act |
| **FORMS** | the decision layer offers the act to someone who would take it | read the opening set for that person; count the offers |
| **FIRES** | it appears in a seeded season with no hand in it | run N seasons; count occurrences, state N and the seeds |

With no GM, a premise that EXECUTES but never FORMS is **half-true**: record it as INERT at FORMS
(STEP 5). **Zero occurrences at FIRES in few seeds is NOT OBSERVED, not INERT** (an absence claim,
§0.1 pt 3): write "0 in n seasons" with the FORMS count beside it, and call it INERT only when FORMS
shows nobody is offered the act or the effect is nil when it does fire.

**Report one chain per scale** when an element has a module and a season-loop wrapper: the same
premise can hold at module scale and break at season scale, and one "first broken link" hides it.
At **module scale** there is no Event log: call the module's composition-row entry directly, and
read the returned typed outcome and trace where the season scale reads `causes[]` (control C
compares outcomes; E10 reads the trace).

**Controls — a result without them is not a measurement (§0.1 pt 4):**

- **P — positive.** Every condition holds; the act must succeed. A refusal here is the first break.
- **N — negative, one condition at a time.** Not the holder; another body's holder; the wrong rung;
  the seat vacated. Each must be refused with a keyed, visible reason.
- **C — counterfactual pair, whose no-act arm is the null baseline.** Same seed, act against none
  (the no-act arm is the null control: the effect is read against it). The difference must trace
  through `causes[]` to the act. A difference that does not trace is noise; none at all is INERT.
- **M — mirror, for any draw-resolved contest.** Identical sides must come out near even; swap the
  sides and the result must flip. State n and the band you accept (for n trials at p = 0.5, about
  ±2·√(0.25/n)); a bias outside it is a defect in the harness or the rule.

Also: run twice on one seed and compare `World.content_hash()` (E12). **Check the run happened**
(§0.1 pt 3): diff the world before and after, assert the event was emitted, assert the loop asserted.

**Sweep the words.** Where the premise uses ordered levels or a parameter, run the whole ordered set
and read the effect against the order (E4, E11), including both extremes. A non-monotonic or flat
response to words that are ordered is a finding by itself. Say n; a single seed is an instance.

**Time.** `build_realm` can take one to two minutes per seed under load. Run FIRES in the
background with **one output file per job** (a shared file is clobbered by a rerun), keep n small
and stated, and do the sweeps on a fast fixture.

**An ASSERTED link may be run through a labelled PROXY** (a hand-planted state standing in for the
missing mechanism) to see what is downstream, provided the report says it is a proxy and the links it
feeds stay UNREACHED for the premise as worded.

## STEP 5 — COMPARE, CLASSIFY, RANK

**Verdict per link, with the depth it holds at** (EXECUTES, FORMS or FIRES): one link can FOLLOW on a
hand-built act and be INERT at FORMS, and the table records both rows, not whichever was reached
first.

| verdict | meaning |
|---|---|
| **FOLLOWS** | observed, and as predicted |
| **DEPARTS** | observed, and differs |
| **INVERTED** | a DEPARTS that does the opposite of what its word says; ranked first |
| **INERT** | code exists; a run that should reach it never does, or the effect is nil |
| **ASSERTED** | the premise names it; **no code owns it** |
| **UNREACHED** | a link it *depends on* broke, so it was not tested. Not a pass, not a fail. Independent branches (STEP 1) are tested and reported on their own |
| **AMBIGUOUS** | the words support two readings and the code picks one; name both |

**Cause, for DEPARTS, INVERTED and INERT:** **WORD** (the behaviour is sensible, the name misleads →
rename at its owner: `references/names_index.yaml` for a term, `engine/season/verb_table.yaml` for
a verb or event kind, where a rename moves `World.content_hash()` for any world whose log uses it,
so declare that move) · **BEHAVIOUR** (the word is right, the code is
wrong → change the code) · **EDGE** (fine mid-range, absurd at a reachable extreme) · **COMPOSITION**
(each link fine, the chain absurd) · **STALE-PROSE** (the notes were superseded; cite the successor,
and the prose changes) · **DELIBERATE** (a documented departure, with its reason and a safeguard).

**Intent gate (as `resolution-diagnostic` Phase 5).** Deliberate, with an adequate safeguard: PASS
with a note. Deliberate without: finding. Accidental or undetermined: finding, tagged
`[INTENT UNDETERMINED]`. A departure claimed for a philosophical reason goes to `valoria-canon-guard`.

**When prose and code disagree.** CLAUDE.md §0.05: decide, then change the code. Use N (STEP 2b) to
see which side was meant. Before flagging anything `needs_jordan`, answer it by §0's five-step ladder
(superseded · irrelevant · answered by a document · answered by precedent · answered by what the
architecture makes obvious). Escalate only what survives: two defensible options that make
materially different games.

**Rank worst first, bugs before gaps** (the user cares most whether code that runs makes sense to a
player):

1. **INVERTED**, then **DEPARTS on the ordinary path** — code that runs and does not make sense.
2. **EDGE** and **COMPOSITION** failures at a reachable extreme.
3. **INERT**.
4. **WORD** defects (a label that means something else) and **AMBIGUOUS** links.
5. **ASSERTED** links, and any finding on a cell tagged **[GENRE]** (STEP 2): listed in a short note.
   **A defect only if the PR (or the user) claims the mechanism or behaviour exists.** An unbuilt
   mechanism a premise merely mentions, or a genre expectation it never promised, is not a bug.

**Tuned values are Jordan's:** "major is 1.0 or 1.2" is not a finding; "major is not larger than
minor" is.

## STEP 6 — PLAY IT BACK

Narrate the control-P run's Event log in plain English, three to six sentences, as a player who never
saw the code would tell it to a friend. Set it beside the premise sentence.

- A sentence you cannot write without repo jargon is an E10 finding.
- Each "wait, what?" is a candidate: trace it to a link, or discard it with a reason.
- A sentence the log supports and the premise does not say is a surprise the premise did not warn of.

This catches COMPOSITION failures the link-by-link table passes.

## STEP 7 — OUTPUT

**The first sentence is the verdict:** *the premise holds* / *holds to link k, then breaks* / *does
not hold*, the depth reached (EXECUTES, FORMS, FIRES), and the scale if more than one. Then:

1. The **link table** (one per scale): `# | link | O predicted | N says | C observed | verdict · cause | file:line | the call that reproduces it`.
2. The play-back paragraph.
3. **Edits** for every finding that needs no ruling (§0: fixed in this commit or dropped), **when the
   request includes fixing**. A read-only run reports each fix as a proposal. A behaviour fix carries
   a test that **executes** the corrected behaviour; the failing probe from STEP 4 *is* that test,
   with its control shown. Registry renames go through the owner.
4. A `needs_jordan` row only for what survived the ladder.
5. A short **skill-friction** line only if a step could not be followed.

Output is a reply plus edits and at most one commit paragraph (§0). **No audit directory, no
document that creates work for a future session, no guard** (§0.1 pt 5): a sweep over every premise
is the tree-wide guard CLAUDE.md §0.05 does not license. **One round, then stop** (§0): fixes are not
re-audited.

## GUARDRAILS

- **Predict first, notes second, code third.** A prediction written after reading a note describes
  the note; one written after reading the code describes the code.
- **Report the first break on each chain and each independent branch.** Links that depend on a break
  are UNREACHED.
- **A hand-built act is evidence of EXECUTES only.** Do not write "the game does X" from it.
- **Absence is a claim.** "Nothing enforces this" is stated only after the search that would find it,
  with its variants (§0.1 pt 3).
- **Not a balance verdict.** "Too strong", "too weak" need a campaign-level instrument (CLAUDE.md §7);
  this skill reports sense, direction, order, bounds, scope and reachability.
- **Do not build the premise.** Inventing a missing mechanism to make the run pass is scope growth.
- **A fixture is not canon.** State which world the run used and what it does not show.
- **Size to the subject.** One reader runs a premise. A PR with several premises may run one reader
  per premise in parallel, read-only; a second agent is otherwise the blind predictor or a critic on a
  judgment call, never a copy of the first.

## THE SHAPE OF A FINISHED RUN — illustration, dated 2026-11-07

An illustration of the verdict types, not a record: **re-run before citing it.** A decree premise
("a person holds an office within a faction and issues a decree for others to follow") came out as:
*holds, and issues, then breaks at reaching the others.* Standing and the act FOLLOWED, with eight
negative controls refused. "Reaches the others" DEPARTED as BEHAVIOUR and COMPOSITION: one addressee
per act, and the writ stayed with its issuer until a separate `give`. "They follow" was INERT at FORMS
(no compliance on a decree in any seeded season), and refusing cost nothing, a [GENRE] note. Revocation and expiry were ASSERTED, and listed last. The play-back read: *the
Duke writes an order and keeps it in his drawer.* A combat premise showed why one chain per scale is
needed: it held at module scale and broke at season scale, where a person's skill, weapon and armour
never reached the fight.
