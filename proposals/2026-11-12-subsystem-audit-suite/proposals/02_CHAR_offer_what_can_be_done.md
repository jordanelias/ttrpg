# CHAR — offer what can be done: one person-side decline read off the row, and a declared aperture for a population

## Status: PROPOSED

Written by the CHAR audit lane (`audits/02_CHAR_audit.md`, findings F-CHAR-05, F-CHAR-07, F-CHAR-11).
Ratifies nothing. Reference under `CLAUDE.md` §0.05.

## What this changes in `engine/season/` at runtime

`decision/options.py::opening_set` stops forming a candidate whose refusal the actor can read off his
own state, and stops forming, for a population cohort, a row that declares it is an individual's act.
Both are declared hash movers. The fold, the verb effects and the write gate are untouched; a
hand-built act still folds exactly as today.

## The problem, with evidence

**Four in ten resolved acts are refusals, and the refusals teach nothing.** Read on `build_realm`,
two seasons, shipped chooser, `PYTHONHASHSEED=0` (scratch `probe2.py`):

| | seed 0 (`bacd687f`) | seed 1 (`8aae8412`) |
|---|---|---|
| resolved acts | 1,529 | 1,519 |
| `.refused` events | 656 | 620 |
| largest refused kinds | train 85, challenge 84, migrate 61, tell 57, transfer 41, sabotage 38, exchange 38, forge 35 | challenge 105, tell 81, train 67, transfer 60, exchange 45, forge 39, migrate 35, sabotage 31 |

H-346 (register line 6386) measured the same shape over five draws and found ten verbs with zero
successes in 4,089 releases, the same with every person's pursuits cleared, so the cause is formation
and not character. Each refused act costs its actor a scene of five. To a player seated through
`decision/sheet.py::development_space`, which shows `make_ranker`'s list as his options, these are
options that always fail.

**The person-side declines are nine rosters keyed by verb, grown one position at a time.**
`opening_set` reads, in order: `withheld_verbs`, `lie_verbs`, `OWN_STATE_STEMS`, the refusal axis,
`held_document_declines`, `terms_sourced`, `held_edge_declines`, `own_stance_declines`,
`violence_contexts`, `own_hold_declines`, `own_title_declines`, `vocation_sourced`, `warrant_sourced`
(`decision/options.py:136-267`). Each is one verb's own-state reading of one conjunct of its own
`requires:` cell, authored as a separate roster row with its own loader. The body is 345 lines, and a
verb whose conjunct nobody has yet written a roster for is offered and refused. That is the mechanism
behind the table above: the rule *"what the actor can know of himself is declined at formation"*
exists nine times and not once.

**A population takes an individual's acts.** A cohort is a `Person` at `weight > 1` (S9) and reaches
`opening_set` like anyone. Resolved acts by the 37 cohorts over the same two seasons:

| | seed 0 | seed 1 |
|---|---|---|
| `create_record` | 115 | 118 |
| `challenge` | 60 | 60 |
| `forge` | 47 | 51 |
| `sabotage` / `train` | 24 / 25 | — / 23 |

A settlement's people issue sixty challenges to single combat and forge fifty records in two seasons.
`data/requires.py` already owns the predicate that separates the two: the `individual` stem (v10
CP-T03-01, *"is `of` a single person, not a cohort"*), which `fight`, `capture` and `accept` ask of
their subject and of their actor (`verb_table.yaml:749-752`, `:883-886`, `:976`). Two things keep it
from working here. It is a WORLD-ONLY stem, so the person side reads UNKNOWN and forms the candidate;
and `challenge`, `forge`, `sabotage`, `train` and `create_record` do not carry it.

## The resolution, decided

| # | decided | ladder step |
|---|---|---|
| 1 | One decline: after operands bind, `opening_set` evaluates the row's own `requires_typed` against a reader of the ACTOR'S OWN STATE and declines on a conjunct that reader answers `False` | 4 and 5. `OwnStateReader` and the K-3 branch are the precedent (*"the SAME cell, asked of the same answerer the fold delegates to, so the two cannot disagree"*); one rule with one owner is what §8 asks for |
| 2 | The reader answers exactly the stems an actor cannot be wrong about when the subject is himself: the existing `OWN_STATE_STEMS`, his own live Tenures (`hold`, `commit`, `oblige`), his own `capability`, and his own judgement of a dispute (`person_q.holds_dispute`). Every other stem is UNKNOWN there and stays clause 4's | 3. §F1's asymmetry, as `opening_set` states it: *"being alone in a room is not a belief anyone can be wrong about"*. A belief about the world still forms the candidate and is refused by the fold, which is R-07 working |
| 3 | The roster rows that item 1 makes redundant are deleted in the same commit as the reading that shows the candidate sets equal; the ones that WIDEN referents (`terms_sourced`, `warrant_sourced`, `vocation_sourced`) are sources, not declines, and stay | 5. A second copy kept "for safety" is the two-owner defect |
| 4 | Whether the ACTOR is an individual is his own state, so the widened reader of item 1 answers the `individual` stem when it is asked of the actor (and stays UNKNOWN for anybody else) | 4. `Person.is_cohort` is the carrier's own predicate; the stem's note says *"whether a person is an individual NOW is the world's to decide"* of OTHER persons, which is unchanged |
| 5 | The rows a population does not take gain the conjunct `relation: individual` of `actor` that `fight` already carries. Proposed set: `challenge` (it opens the duel `accept` already bars a cohort from), `forge`, `sabotage`, `train`, `create_record`, `conceal`, `interview`, `surveil` | 4 for `challenge` (its sibling rows' own conjunct); the rest [ASSUMPTION; medium; Jordan to correct; revert: drop the conjunct from the row]. No new column and no new roster: the stem exists |

## The exact edits, by owner

1. **`engine/season/queries/person_q.py`** — `OwnStateReader.read` gains the own-state stems of
   items 2 and 4, each answered from `self._p` alone and only when the subject is `self._p.id`; `UNKNOWN`
   otherwise. `data/requires.py::OWN_STATE_STEMS` grows by the same names, and the import-time check
   below the class (which refuses a stem with no branch) keeps the two in step.
   `[UNVERIFIED: the exact stem names of the `hold`, `capability` and `dispute` conjuncts in
   `data/requires.py`; the audit read their readers, not the grammar file.]`
2. **`engine/season/decision/options.py::opening_set`** — the K-3 branch moves from before the
   referent loop (where it binds `{}`) to after `operand_bags`, evaluating with the candidate's own
   binding: `evaluate(row.requires_typed, OwnStateReader(p, fx), binding_of(p.id, ops)).value is False`
   declines. `False`, not `is not True`: UNKNOWN forms. (K-3's present `is not True` is kept for the
   rows whose cell is ONLY own-state stems, which is what `build_typed_requires` already guarantees for
   `thread_read`.)
3. **`engine/season/verb_table.yaml`** — the conjunct `relation: individual` of `actor` on the rows of
   item 5, in `fight`'s spelling. The fold then refuses a hand-built cohort act on those rows, and the
   person side (item 4) does not form it.
4. **`engine/season/rosters.yaml`** — delete each decline roster the reading in the gate shows
   redundant, with its loader in `data/verbs.py`.

## Gate (an execution artifact, §0.2)

- `python -m engine.season.harness.aperture 2 0` before and after: for each of H-346's ten
  always-refused verbs, `attempted` falls and `executed` does not fall. A verb whose `executed` falls
  was being formed correctly and the reader over-declines.
- The cohort conjunct: the cohorts' resolved multiset at seeds 0–2 holds none of item 5's verbs, and
  the cast's own formations of those verbs at round 0 are EQUAL (a row's cast formations must not move).
- For each roster proposed for deletion: `opening_set`'s candidate set for every person at round 0 of
  `build_realm(s)`, s = 0–2, with the roster and without it, compared as sets. Equal → delete.
  Unequal → the roster stays and the difference is recorded on its row.

## Falsifier

A hand-built person holding no dispute against `p_x` forms no `challenge` on `p_x`; given one planted
deed claim his pursuits judge against, he forms it. A cohort and a cast person handed the same question
differ by exactly the rows carrying the actor's `individual` conjunct. If H-346's refusals do not fall, the failing conjuncts are
world-side (the actor could not have known) and the proposal's premise is wrong for those verbs: they
then need the refusal deposited as a claim, which is a WITNESS change and another lane's.

## NERS reading (§0.06)

- **N.** From the player's direction: a menu in which four options of ten cannot succeed is the
  friction point of the whole play surface. From the world's: 40% of a realm's scenes produce
  `*.refused`, which is noise in every chronicle. From the cohort's: a population that duels is not a
  population.
- **R.** Completeness at the extremes: a person with no dispute, no capability and no seat is offered
  less, which is what being that person means. Nothing is taken from the mistaken-belief path, the one
  refusal that is a story.
- **S.** One decline, read off the row's own cell, asked of the same answerer the fold asks. The scale
  transition is cleaner: what a cohort does is what a body of people does.
- **E (last, as a ratio).** One reader widened by four stems and one existing conjunct on eight rows replace up to five rosters
  and their loaders; the rule a reader must learn falls from nine to one.

## Cost class

Design-first for the stem list (item 2), then small build; the cohort conjunct is verb-table content.
Shared files: `verb_table.yaml` (the verb cluster, serialise), `rosters.yaml`, `data/verbs.py`,
`data/requires.py`, `queries/person_q.py`, `decision/options.py`.
