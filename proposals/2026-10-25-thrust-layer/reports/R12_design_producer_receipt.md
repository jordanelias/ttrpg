# R12 — Design producer's hand-back (the thrust-layer design, v1)

## Status: REFERENCE — HELD BACK IN FULL

> **Reference — PROPOSED, HELD BACK IN FULL.** Merging the PR that carries this file ratifies nothing in it (ED-1094's default is not applied). This is the agent's hand-back message, reproduced verbatim, except that session-scratchpad paths are rewritten to their committed locations. Under CLAUDE.md §0 an adversarial pass is a stage, not a deliverable; this file records a terminal verdict about artifacts that already exist, as the §0 exception permits, and asks nothing of a future session.

**Role:** producer (agonist) of the thrust-layer design relay. **Wrote:** the v1 draft (not committed; the design committed is v2 after the critic's findings). **Model:** per the session record, opus.

---

I wrote the design document at thrust_layer_design_v1.md (not committed) (509 lines). I changed nothing in the repo, committed nothing and spawned no agents. I ran no tests, because the deliverable is prose. The checks I did run were read-only Python and grep over the tree, plus a few lookups in the toy outputs.

**Sections:** 0 status and is/isn't · 1 contract (the objects, and the arc criterion as a predicate over the log with a static half) · 2 data (new `thrust_axes` roster, new `goals.yaml` keys, loader refusals, cohort gap) · 3 runtime (R1 `current_stage`, R2 the stage's referents and pursuits added to the `need` question, R3 a due stage moves to tier 0; control and falsifier) · 4 four closure engines · 5 the three constraints · 6 ladders for all ten axes in build order · 7 repairs S1–S10 · 8 build batches B0–B6 with falsifier, control and instrument, plus the Layer 1 questions · 9 refusals and contraventions · 10 open decisions · 11 evidence grades · "what would make this design wrong".

**Things that correct or sharpen the brief:**
- Thirteen verbs write nothing, not nine. The four extra are `dispatch`, `challenge`, `evade / defy` and `speak`.
- `construe` is `grade: absent` with `requires_typed: none`, so it can't serve as a non-violent weapon today. The design drops it.
- `offices.yaml` has 31 seats: 16 with no revoker, 13 strippable by the rung above in the same faction, 2 by the rung above in holdings. The header's "14 of 29" is stale.
- The orientation-only rows mint no Proposition, so they produce no thrust at all. That covers the Crown's resist-Altonia row, both Einhir-revival rows, the caste-ended row and the community rows. Each of those axes needs a goal row with a referent before a ladder can attach.
- The standing gate can build on an access gate that already exists: `admits_audience` and `guard_weight` (`world_q.py:1250-1344`). It binds nobody today because guards are off by default.
- `succeed`, `tie` and `knot` have no code that opens their tenures (`rosters.yaml:141-143`), so hereditary seats can't be filled.
- Two consequence channels are currently silent. A death never reaches anyone's questions (H-209), and a dead holder's empty seat is named by no claim (H-206).
- Jordan's 2026-08-18 ruling ("script hooks and sequences, not entire arcs") is what licenses ladders.
- `_standing_crossings` (`loop/matter.py:187-240`) is the precedent for a threshold that writes nothing and only raises a question.
- ED-IN-0225 is cited in four `.py` files, not three; `chronicle.py` is the fourth.

**Decisions I took (reasoning is in §10):**
- The axes list lives in `rosters.yaml`.
- One ladder per goal.
- Stage predicates reuse the existing `requires_typed` grammar rather than a new one.
- A person's progress is read from his own ledger, not from the world.
- The need-starvation fix is R3 (promote only when a stage is due), not a global re-tier and not `one_per_source`.
- The standing gate is deterministic, not a dice roll.
- Hereditary succession goes through `confer` with a new `succession` basis, not a new verb.
- Axis 9 (heal the Calamity) is out of scope until a thread-operation act exists.

**Named contraventions:**
- ED-IN-0225 is narrowed, not lifted.
- The §3.4 refusal of scripted beats is narrowed; the ban on need-triggered injection is kept.
- `fight`'s comment that "Felled is the kill" is contravened.
- `fight`'s note that a wider precondition "would be an invention" (G4) is contravened.
- R-AI is kept.

**Needs Jordan (D1–D3):**
- D1: whether a beaten fighter is ever killed outright, and where the new `Slain` band's edge sits.
- D2: who holds axis 2 ("hide threadwork truth"), and who defends the caste order.
- D3: whether caste gets a store in code.

**[ASSUMPTION]s:**
- The opposite poles that aren't among the user's ten are members of the axes list too.
- The record of a write to a tenure names the tenure, so the predicate has to look up its owner.
- The combat scene's wound tracker can tell "down" from "dead". If it can't, the `Slain` band has nothing to read and must not be invented.
- Letting the `audience` stem accept a person as its subject is acceptable under Layer 1.
- Cohort goals can attach through a new `org: {rung: …}` kind.

**Not verified:**
- The 143-case count (I took it from ED-IN-0225's text).
- What `World.write` puts on a tenure write's record.
- Wound-tracker fields beyond `seam/ladder.py`.
- The WR file's claim about `restore` at `rosters.yaml:2149-2156`.
- The run figures (51/803, 929/1,318, 439/1,318 and the rest) are as reported in `proposals/2026-10-13-narration-mechanisms.md`; I did not re-run them.

**Cheapest test that could sink the design:** count the executed `determine`, `confer`, `covenant` and `open_case` acts over a few seeds. Every closure route ends through one of them, and the measured run refused all 7 `determine`s and all 4 `confer`s. If that stays near zero after candidate typing is fixed, ladders can be climbed but not closed.

---

## Brief given to the agent (verbatim)

The instruction the agent received, so a reader can judge what it was and was not told.

~~~text
You are the AGONIST (producer) in an agonist→antagonist relay for the Valoria repo at /home/user/ttrpg. Read /home/user/ttrpg/CLAUDE.md FIRST; its rules bind you (§0 incl. 0.05 "code is the mechanism, prose is reference", 0.1 measurement discipline, §8 single owner / no second parser, §10 guardrails: no scripting drift, no new scale-local dialect). A separate read-only critic will attack your output against the working tree, so every claim about the tree needs a path:line you actually opened; mark guesses [ASSUMPTION]. Do NOT edit anything in the repo, do NOT commit, do NOT spawn agents. Write ONLY to the output file below. WRITE THE DOCUMENT'S HEAD AND §1 BEFORE YOU FINISH READING, then append the rest as you learn it (a producer that has read far and written nothing is failing). Return only a SHORT RECEIPT: the path, the section list, the [ASSUMPTION]s and decisions the orchestrator must settle, and anything you could not verify.

OUTPUT FILE: thrust_layer_design_v1.md (not committed)

TASK. Design how to make the "THRUST LAYER" possible in engine/season/ (the game code, Layer 2). Do not build it; design it so that it could be built as plan positions with falsifiers and controls.

WHAT THE USER SAID (their words, binding as intent):
1. Characters pursue goals across these axes (not exhaustive, "major"): (1) suppress Einhir Revival; (2) hide threadwork truth; (3) overthrow Church of Solmund; (4) overthrow Einhir caste system; (5) purge Altonian influence from peninsula; (6) maintain or expand political authority; (7) increase standing within a faction; (8) benevolent community actions; (9) heal the Calamity; (10) revive Einhir heritage.
2. "An arc for a character needs to be something narrative that affects themselves and their world in some manner."
3. Ambitions are an OVERALL THRUST for a character, with a SERIES OF SHORT- OR MEDIUM-TERM GOALS beneath them. The guides the user named: character ambitions, office duties, faction goals, settlement/cohort politics and identities, settlement challenges, possibly "arc decks" (like event decks, but assigning arcs).
4. NPC death must be EXTREMELY RARE, or at least its consequences SIGNIFICANT. It must be HARD to even fight anyone with authority/standing. An arc does not need an NPC to die.
5. The user permits contravening existing rulings, but each contravention must be NAMED (candidates: ED-IN-0225 "ignore the arcs" as since cited, the v2 narrative-engine rule R-AI that forecast objects are actor-invisible, and the ban on need-triggered injection / scripted beats in proposals/2026-10-13-narration-mechanisms.md §3.4).
6. There is no GM: the engine resolves everything.

EVIDENCE ALREADY ESTABLISHED (re-verify before relying; cite paths):
- engine/season/goals.yaml holds 38 organization goals (loader data/goals.py; schema in its header, incl. `derives`, `object` kinds, `pursuits`). Its header says a goal only changes what a person attends to; it never acts; nothing aggregates (A-31). Rows exist for axes 1, 4, 6, 10; partial for 3, 5, 8; none for 2 (Varfell's row is the OPPOSITE pole), 7 (only 2 of 38 rows attach to a seat), 9. There is no row defending the caste order. Caste has no store in engine code (canon/03_canonical_timeline.md "The Caste System": informal geographic stigma). Healing the Calamity has no act: thread operations are unplugged from the season loop (research/by_lane/WR_world.md T-WR-7, T-WR-11).
- Ambition mechanism: queries/world_q.py `ambitions` (~:2168), `goal_referents` (~:2207), `attention_key` (~:2560-2640), `questions_for` Q4 `need` source. Measured (proposals/2026-10-13-narration-mechanisms.md §1.1; one seed, two seasons, uncommitted scratch instruments): the standing `need` question won 51 of 803 deliberations; 1,318 acts, 929 (70.5%) refused/blocked/null; 439 acts (33.3%) aimed at a subject that exists as another kind; 37 of 80 persons pursuit-less (seated cohorts, populated.py:391-398).
- Chooser: decision/choose.py `_sample_order` (~:241-392) is Plackett-Luce via Gumbel, softmax(score/tau), choice_temperature=0.1 (data/fixtures.py:286), noise keyed per candidate. Dice side: engine/dice_engine/sigma_leverage.py (mu-shift in sigma units, soft_cap; never an Ob shift).
- Verbs: verb_table.yaml (56 rows) declares `writes:` per verb; at least nine write nothing (comply, construe, tell, examine, interview, research, surveil, thread_read, reconstruct). `fight` (row ~:647) requires only existence + co-location (requires_typed_note: a "deontological gate" does not exist); its Felled band deletes the Person and emits person.died. offices.yaml header: seats are stripped only by "rung above of same faction" (ED-IN-0256 ruling 3; 13 seats rung_above_same_faction, 2 rung_above_in_holdings, 14 null). write_matrix.yaml keys writes by (kind, field).
- Closed authored cast (ED-WR-0011): nobody is generated; every death is a permanent loss. Exogenous motion ships dark (research/by_lane/WR_world.md T-WR-8).
- Existing precedent for the "script the predicate, not the arc" stance: proposals/2026-08-29-greenfield-systems-suite-v2/09_ambitions_and_arcs.md §4 (Jordan 2026-08-18) and §7 (arcs are tag chains, no arc object); that suite is built on the RETIRED Key substrate (ED-IN-0232), so treat its mechanisms as stale and its shapes as reference. The ratified narrative engine design (.audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md) is also Key-native.
- Corpus: engine/season/ENDINGS_CLASSIFIED.yaml (how 50 arcs close: DECIDER 20, ROLL 9, THRESHOLD 8, NEVER 10, UNCLEAR 3); engine/season/cases/ (143 cases: 46 characters, 97 arcs). Hand classification of the 46 characters' ends_when: 11 author a fork of outcomes, 7 name only exit events, 12 have a terminus the extractor presumed, 16 author nothing (ids: forks 004,020,021,050,052,070,003,032,031,030,001).
- TOY-WORLD EXPERIMENTS (grade: model-internal, low confidence; code and outputs in proposals/2026-10-25-thrust-layer/toy/: regimes10.py, out_v2.txt, posthoc_out.txt, exp_ladder_out.txt, exp_setpiece_out.txt, exp_contest_out.txt, exp_con_out.txt, lb_more_out.txt). Findings: (a) motive depth ("why") comes from standing ambitions (why_linked 0.80 vs 0.43); (b) a goal LADDER under an ambition adds modest closure and ~2.7x cross-person chain depth, but no ordering signal by itself; (c) arc shape needed a CLOSURE ENGINE: a threshold-raised, declinable tribunal decided by an actor, or an authored set piece with a decisive form whose winner is left to dice, or a forced schedule; (d) arc-shape signal depended on a lethal climax until a bound peace plus ladder was used (ladder + decisive-form set piece + bound peace: arc-minus-null +0.24 [+0.19,+0.30], deaths 0.24/run; ladder + tribunal lost its signal under the constraints); (e) lookahead-biased choice (a sigma-leverage-like tilt on the Plackett-Luce score) raised closure and chain depth but not ordering, cut explained motive, flipped ~32% of leveraged decisions, and cost ~3,200 rollouts/run; (f) with a 90% gate on violence against standing-holders and accusation as the usual weapon, a killing at season 10 produced ~9.5 acts by ~5 actors against the killer and ~1.3 tribunals but no runaway feud, and the world ended quieter; (g) the toy's arc test credits a lone interior closing event, so read arc rate beside its shuffled null; the toy's arcs close by silence. Treat all of this as a model of the regimes' logic, NOT of Valoria.

REQUIRED CONTENT of the design document (be concrete; prefer tables; no padding; ~350-500 lines):
 0. Status/scope line (PROPOSED; reference under CLAUDE.md §0.05; creates no plan position). A one-paragraph statement of what the thrust layer IS and ISN'T.
 1. THE CONTRACT. The objects (Thrust/ambition, ladder Goal/stage, Duty, Challenge, Identity), what each READS and WRITES, which ALREADY EXIST (cite), which are NEW. State the user's arc criterion (self effect + world effect, linked by causes[]) as a PREDICATE checkable from the log, and say how it is checked statically from verb_table `writes:`.
 2. DATA. Where the head of every fact lives (YAML under engine/season/ read by code, per §0.05; no .md as head). Concrete schema proposals extending goals.yaml (an axes roster; ladder templates keyed by axis; stage predicates typed by referent; deadlines; successor rule), with the loader REFUSALS each needs. No second parser (§8).
 3. RUNTIME. How a stage advances using EXISTING question sources and verbs only; why progress is a QUERY over state and not a stored arc object (reconcile with ED-IN-0225); how the starved `need` question is fixed (the ordering/aggregation, with a control); what is stored vs derived.
 4. CLOSURE ENGINES that are lawful (no outcome written by a non-person): threshold-raised declinable docket matters decided by an actor, bound peace via oblige/covenant tenures, succession, set pieces whose FORM is authored and whose winner is not. For each: the existing verbs/stores it uses, the new pieces, what it forbids.
 5. THE THREE CONSTRAINTS as mechanisms: (i) death rare (what `fight`'s Felled band should write instead; what still kills, and when), (ii) the standing gate (what precondition, where it lives, how the `argue`/`open_case`/`tell`/`construe` verbs serve as the non-violent weapon; cite verb_table), (iii) significant consequences of a killing (witness/claims, vacancy and succession, kin ambitions, tribunals) using existing carriers.
 6. PER-AXIS LADDERS for all ten axes: opposing pole (cite goals.yaml rows or say none), short/medium/long stages in EXISTING verbs with typed predicates, the closing form, the self effect and world effect with the cited `writes:`, and the GAPS (e.g., no caste store, no thread-operation act). Order the axes by buildability.
 7. SUBSTRATE REPAIRS THAT GATE IT (candidate-typing mismatch, refusal rate, need starvation, dark exogenous motion, ageing off), with the evidence path and what each blocks.
 8. BUILD ORDER as batches/positions, each with a FALSIFIER and a CONTROL per CLAUDE.md §0.1 (a number without a control is not a measurement; a loop that asserts conditionally must assert that it asserted). Name the instrument for each. Say which positions are Layer 1 conformance questions.
 9. REFUSALS and CONTRAVENTIONS: what the design refuses (arc carrier, outcome injection, actor-visible forecasts, lookahead steering) and each existing ruling it contravenes or narrows, named.
10. OPEN DECISIONS that survive CLAUDE.md §0's five-step answering for `needs_jordan` (superseded? irrelevant? answered by a doc? by precedent? by what is right for the architecture?) — keep this list short; TAKE the architecture-right option and record the reasoning for everything else.
11. EVIDENCE GRADES: a table separating [repo reading], [measured in the repo], [toy-world result, low confidence], [ASSUMPTION].

Also include a one-paragraph "what would make this design wrong" naming the cheapest observation that would show it.

If you cannot open a cited line, say so in the document rather than citing it. If two surfaces disagree, say which owner wins and why (CLAUDE.md §0.05 cl. 3). Do not assert a Godot engine version. Canadian spelling.
~~~
