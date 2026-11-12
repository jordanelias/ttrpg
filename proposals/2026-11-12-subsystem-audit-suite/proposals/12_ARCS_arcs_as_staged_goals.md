# ARCS 02 — a counter becomes a resolve: staged goals armed by what a person learns

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
  quoting the case need it stands for.
- `engine/season/data/goals.py`: accept `org.person` (if allowed); nothing else.
- `decision/`: none here; the reader is CHAR's proposal, to which the active stage's `pursuits` are the
  input.

## Gate (execution artifact)

ARC-47 on the realm (`12_ARCS_case_on_the_realm.md`), seeds 0, 1, 2: with the three enabling claims
delivered by prehistory and play, Ehrenwall's `issue` (or `petition`) toward the king's seat is chosen
within the span; with one claim withheld (off-arm) it is not; with a false third claim planted by another
person's `lie`, it is. The third arm is the property the old counter could not have.

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
