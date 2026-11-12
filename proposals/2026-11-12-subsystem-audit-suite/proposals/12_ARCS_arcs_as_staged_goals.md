# ARCS 02 — a counter becomes a resolve: staged goals armed by what a person learns

Folded: 2026-11-12 by `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md`. Nothing here is deleted. The `mandatory` mark this file adds to a question is reused, not re-made, by `30_WR_A_the_era_is_a_named_period.md` commit 3: a vacant head seat is a mandatory question for a person who may claim it (`state/gate.py::may_claim`), behind `Fixtures era_mandatory_vacancy`; that commit **waits on this file's**. A stage of a goal may be armed by an era turn with no new mechanism, because a turn reaches a person as claims (a `held_by` change; a death, apart: A-33). The player sees the mark on the slate (`30_GO_F`: `AskedRow.mandatory`) and in the recap's `waits` line.

Reconciled: 2026-11-12, U5d closure — folded **A-47** (a threshold may open a mandatory scene, never decide it), **A-16** and **A-24**. Kept: a counter becomes stages of the holder's goal, each armed by a claim in his own ledger; a stage names no act and no outcome. Added: when a goal's last stage is armed the holder's next question on that goal is **mandatory** (it cannot be passed over for another; for a player it must be answered, A-48), so the world can corner a character; what he then does is his choice among the offered acts and its result is the drawn band. Step rewritten: the stage row gains `opens: mandatory | ordinary` (default `ordinary`), read at the one formation site; the gate for ARC-47 gains an arm in which the armed stage's question is first on her slate in every seed while her act and its band vary across seeds. Murder as an own-motive act is lawful, rarely (A-16), so NPC-088's and ARC-31's last stages may arm a killing; its gate and its draw are `22_HAPPENINGS_C_a_killing_is_a_crime_someone_commits.md`'s.

Folded: 2026-11-12 by `U5a_CHAR_owed_amendments.md` §3 — *a want can be kept or laid down*: the standing `need` question for a commitment is not raised while the holder's own ledger reads the content true (a met stage predicate counts), and the holder may `release` his own `commit`, whether it was kept being read by `world_q.commitment_kept` (computed where read). It lands in this file's batch.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.6 row (CONFORMS), §2 row (the missing pointer), §7, §7b-T; `unified/U3_DEPENDENCY_ORDER.md` node B10). Added: the `Folded:` pointer above, which `U5a_CHAR_owed_amendments.md` §3 said this head carries; the body's edit list carries the head's `opens: mandatory | ordinary` key; named tests; lands-it and tier. Left INCOMPLETE with its reason: item 5's `org.person` against AM-B-09 (the ruling's text was not opened by any lane; the row is dropped if it excludes person-level goals).

Reconciled: 2026-11-12, unification lane U4c (test 9; grepped at the tree) — (1) **Depends on:** no other proposal (`unified/U3_DEPENDENCY_ORDER.md` §3.1, node B10 has no inbound edge); it lands in B10 with `U5a_CHAR_owed_amendments.md` §3 (the `Folded:` line above). (2) Item 5's AM-B-09 mark is narrowed, not closed: AM-B-09 is built as `world_q.aim_state` for rung goals only (`engine/season/rosters.yaml:2324-2330`, `tests/test_cp_t02_03_aim_state.py:1`), every other goal kind "reads `open` always", and `person` is a listed goal-object kind (`rosters.yaml:2321`), so the ruling bars a person goal from being *met by `aim_state`*, not from existing; the stages here are armed by held claims and do not read `aim_state`. What stays open is the one grep at landing: whether `data/goals.py` admits an `org: {person: <id>}` form (if not, the row is dropped, as the file already says).

## Status: PROPOSED

Source: `audits/12_ARCS_adjudication.md` §4 (M-LATENT, M-AIM), §5 stage 5, §6 row 1, §9 (c1, c2).

## What changes in `engine/season/` at runtime

`goals.yaml` gains `goal_stages:` rows (the key's loader exists and the list is empty) and, if the
ruling it must be checked against allows, goal rows attached to a person. The chooser gains nothing
here: the term that reads a goal on its own question is `02_CHAR_goal_lean_on_its_own_question.md`. With
no stage rows authored the game is unchanged (hash EQUAL).

## The problem, with evidence

- 84 core needs in 54 cases are a private counter, a clock or a faction scalar that fires with nobody
  deciding. Layer 1 refuses that shape for social quantities (`state/world.py:64-107`;
  `loop/matter.py:132-135`), and the 2026-08-30 adjudication (§4) gave the replacement: a person holds a
  resolve whose act is not chosen until enabling claims reach his ledger. Nothing implements it.
- 21 cases need a person to hold back with a stated condition (c1) and 57 need an act chosen for what it
  does for the person's want (c2). The score reads the verb only (CHAR F-CHAR-01); goals attach to a
  faction, body or seat and never to a person (`goals.yaml` header).
- `goals.yaml` already specifies the right object: a stage is `{id, term, predicate, pursuits}`, its
  predicate a typed cell read person-side off the holder's own ledger, never off world truth.

## Resolution (decided)

1. **A case's counter is authored as stages of the holder's goal.** Example, ARC-47 and NSC-08
   (Ehrenwall): the Löwenritter's existing goal `goal_lowenritter_throne_security` gets a stage row whose
   first stage is the default lean and whose later stages require, each, a claim in her own ledger of a
   kind the case names (a seizure she has heard of, the heir's turning, territory lost). Each stage shifts
   the goal's `pursuits` lean. The demand she issues is an ordinary seat act that the later lean makes
   rank; nothing fires.
2. **Holding is the absence of the lean, not a new candidate.** Before the enabling stage the goal adds
   nothing to that act's score, so it stays low; after it, the lean applies. No "hold" verb, no timer.
3. **A stage never names a verb, an act, a subject or an outcome.** It names a predicate over the
   holder's ledger and a lean. That is the scripting-drift line.
4. **Irreversibility is not authored.** "Never decrements" becomes: a stage reached stays reached while
   the claims are held; claims fade and can be contradicted, so a resolve can lapse. The case's property
   is then a measurement (how often it lapses), not a rule.
5. **Person-level goals.** `org: {person: <case id>}` for characters with no seat (Vedel, Askeland,
   Virke, Solberg). `[UNVERIFIED against AM-B-09, which CHAR §5 records as narrowing aim states to rung
   goals; if it excludes this, the row is dropped and seatless persons are served through their existing
   `commit` propositions only]`.

## Edits, by owner

- `engine/season/goals.yaml`: `goal_stages:` rows for the cast, case by case, each with a `source:`
  quoting the case need it stands for, and the key `opens: mandatory | ordinary` (default `ordinary`; head
  line, A-47: the last stage's question is mandatory, it opens a scene and decides nothing).
- `engine/season/data/goals.py`: accept `org.person` (if allowed) and refuse an `opens:` value outside the
  two; nothing else. The one formation site that reads `opens:` is `world_q.questions_for`'s ordering
  (`Question.mandatory`), also read by `30_WR_A` commit 3.
- `decision/`: none here; the reader is CHAR's proposal, to which the active stage's `pursuits` are the
  input.

## Gate (execution artifact)

ARC-47 on the realm (`12_ARCS_case_on_the_realm.md`), seeds 0, 1, 2: with the three enabling claims
delivered by prehistory and play, Ehrenwall's `issue` (or `petition`) toward the king's seat is chosen
within the span; with one claim withheld (off-arm) it is not; with a false third claim planted by another
person's `lie`, it is. The third arm is the property the old counter could not have. A fourth arm (head):
the armed stage's question is first on her slate in every seed while her act and its band vary across
seeds. Named tests (new, `engine/season/tests/test_staged_goals.py`): `test_no_stage_rows_is_hash_equal`,
`test_arc47_on_arm_off_arm_and_lie_arm`, `test_the_last_stage_opens_a_mandatory_question_and_decides_nothing`,
`test_a_stage_naming_a_verb_or_outcome_is_refused_at_load`.

## Falsifier

Run the on-arm with the stage rows deleted: if the beat still occurs at the same rate, the stages decide
nothing. Run with her pursuits shuffled to another officer: if he issues the demand as often, the beat
is the seat's, not hers.

## NERS reading

**N**: without it 54 cases have no faithful form; from below (the ledger), from above (the goal), across
(any seat-holder) the same object serves. **R**: a resolve that can be armed by a lie or starved of news
is strategy for a player and drama without one. **S**: one ladder for "how near is this person to
acting", read where questions are already read; pauses with the person's attention. **E (last)**: a
reader's rule of thumb: "he will act when he has heard enough", against 84 authored gauges removed.

## Cost class

Edit plus data authoring; design-first only for item 5.

**Lands it and tier.** The B10 batch, a WR/IN `valoria-author` session on `sonnet` (`high`), with
`U5a_CHAR_owed_amendments.md` §3; closed by B10's `methodology-close` once; stage rows are per-case content.
**Hash movers.** None with no stage row (control).
