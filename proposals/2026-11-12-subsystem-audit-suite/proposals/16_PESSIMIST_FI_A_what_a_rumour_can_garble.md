# 16 · PESSIMIST · FI · A — What a rumour can garble: quantities drift, existence does not, a deed loses its hand

## Status: PROPOSED

Carries `audits/16_PESSIMIST_FI.md` F-PES-FI-02 and F-PES-FI-06 (§2.1). Amends, and does not replace,
`08_FI_02_rumour-that-travels.md` (edit 2's tier list) and depends on `08_FI_06_testimony-names-a-hand.md`
for edit 4.

## What this changes in `engine/season/` at runtime

1. The lossy copy of a `Partial` telling, and the liar's inflation, apply to a **quantity** and to
   nothing else. An existence reading (`exists:Person`, `exists:Record`, …) and a relation reading are
   passed on whole by the lossy copy and **negated** by the liar.
2. A `Partial` telling of a deed withholds the hand, by the row `finding_terms` already carries for
   that band.
3. Under `08_FI_02`'s `unshared` slant, a deed is preferred to a quantity and a quantity to an existence
   reading.

Declared hash mover for every world in which a `Partial` telling or a lie passes on an existence
reading (the shipped realm at seed 0: 3 of the 7 tellings that land in two seasons).

## The problem, with evidence

`told_dump.py 0 2` (`build_realm(0)`, two seasons, shipped fixtures and chooser, content hash
`bacd687f…`): twelve claims in the realm carry a teller. Seven are `(p_npc_004, exists:Person, 2)`;
one is `(p_npc_089, exists:Person, 3)`, from a lie that said `2`. Of 70 tellings attempted, 36 chose
to say `exists:Person`. The first FI audit's count of false beliefs formed by telling (7 of 7 told
cells false at seed 0) is this value.

`p2_proxy.py` (tiny world; each teller made to pass on the content he was told; six hops; twenty world
seeds; every telling `Partial`): `(S, stores:grain, 40)` reaches hop 6 with mean absolute error 0.72
(ordered by hop: 0.26, 0.30, 0.31, 0.44, 0.55, 0.72); `(King, person.died, True)` reaches hop 6
verbatim; `(King, exists:Person, 1)` reads `2, 1, 2, 1, 2, 1`; `(S, condition, 3)` reads
`4, 2, 3, 1, 2, 1`.

Owners. `loop/witness.py::_told_value` drifts any `int` or `float` that is not a `bool`.
`queries/person_q.py::lie_said_of` inflates any numeric cell by a whole band. `is_cell` is
`stem in CELL_STEMS`, and `CELL_STEMS` (`data/requires.py`) is every stem a requirement may ask less the
world-only ones, so it holds `exists` (a `1`/`0` reading, `Existence.stems`) beside `stores`.

## Resolution, decided

A number is garbled only where the number is an amount. The grammar already knows which stems those
are: the ones a `ScalarThreshold` requirement compares. Everything else that happens to be stored as
`1` or `0` is a yes or a no.

Ladder: step 4 (precedent). `CELL_STEMS` is derived from the grammar and not rostered; `_told_value`
already excludes `bool`; `lie_said_of` already negates a `bool`. The existence reading is a boolean the
grammar stores as a number (`_as_number`), and it takes the boolean's rule.

## Edits, by owner

1. **`engine/season/data/verbs.py`** (where the loaded table and the requirement forms meet), one
   derived constant: `QUANTITY_STEMS` = the union of `stems()` over every `ScalarThreshold`
   requirement any row's `requires_typed` carries, intersected with `CELL_STEMS`
   (`data/requires.py`). `ScalarThreshold.stems()` returns the cell's own `scalar` (and its
   `threshold_predicate`), so the set is whatever the table compares against a threshold: `stores`
   and `condition` today. Derived, not a roster, on `CELL_STEMS`' own precedent.
2. **`engine/season/loop/witness.py::_told_value`**, the numeric branch: add the conjunct
   `stem in QUANTITY_STEMS`. A numeric value on any other stem falls through to the last line and is
   deposited as held.
3. **`engine/season/queries/person_q.py::lie_said_of`**: the `isinstance(held, (int, float))` branch
   takes the whole-band drift only where the claim's stem is in `QUANTITY_STEMS`; a numeric value on
   another cell stem is negated by truthiness (`0 if held else 1`). A liar may then say that a living
   man is gone, which the hearer's clause 4 reads (`p1c_exists.py`: `(King, exists:Person, 0)` declines
   `challenge`, `interview`, `train` on the King): the first lie in the tree that changes what its
   hearer will attempt about a person.
4. **`engine/season/loop/witness.py`, the told deposit** (after `08_FI_06` gives a told deed its
   sighting on the same chain): at a degree whose `finding_terms` row lacks the hand term
   (`loop/witness.py::HAND_TERM`), deposit the deed claim without its sighting. One table, read by the
   finder's deposit and the hearer's: a hearer of a deed at a band holds what a finder at that band
   holds. No new roster.
5. **`08_FI_02` edit 2, the `prefers:` tier list** becomes `[told, inferred, deed, quantity, other]`:
   `deed` = a claim whose predicate is a kind some verb row emits and no row emits on refusal (derived
   from `VERB_TABLE`, never spelt); `quantity` = `QUANTITY_STEMS`; an existence reading falls in
   `other`. As written (`[told, inferred, cell, other]`) the slant prefers the 577 existence readings
   the realm holds to every deed.

## Gate (execution artifact)

- `p2_proxy.py`, unchanged script: `(King, exists:Person, 1)` reads `1` at every hop; `(S, condition, 3)`
  is decided by whether `condition` is in `QUANTITY_STEMS` (it is, as a `ScalarThreshold` stem; it keeps
  drifting, and that is a tuned matter); the grain rows reproduce today's values at every seed (control:
  the quantity path is untouched).
- `told_dump.py 0 2`: no ledger holds an `exists:` claim whose value is outside `{0, 1}` (today 8).
- `p1c_exists.py` (i) with the claim produced by a hand-built `lie` instead of a plant: the hearer's
  `challenge` on the named man is declined.

## Falsifier

After the edits, any claim in any ledger of a three-season realm run at seeds 0 to 2 whose stem is
outside `QUANTITY_STEMS` and whose numeric value differs from what its teller's `Said` carried, other
than a liar's negation.

## NERS reading

N: the lossy copy on quantities stays (cut it and a rumour of a store is always exact, §2.1's
`Success` row). What is cut is its application to non-quantities, and nothing dies: no reader does
anything with `exists = 2`. R: the liar gains one meaningful lie (a man reported gone) that clause 4
reads; the deed's lost hand makes a second-hand accusation weaker than an eyewitness's by a draw, not
by a rule. S: one ladder for "how much of a deed a band shows" (`finding_terms`), read by two
deposits, where today the finder's deposit is graded and the hearer's is not. E, last: one derived
set, two conjuncts, one roster row reordered; no new object.

## For Jordan (one survivor; two options that make different games)

**May a garbled deed name the wrong person?** Edit 4 makes distortion a *loss* (the hand is withheld).
The other reading of "a rumour distorts" is *substitution*: at `Partial`, the hand or the victim is
replaced by another person the teller's ledger names in the same place.
- *Loss only* (decided here as the shipped arm): gossip degrades toward "someone killed him"; nobody is
  wrongly named by accident; false accusation needs a liar.
- *Substitution*: an innocent is named by the mechanics of retelling; feuds and wrongful proceedings
  arise with no one lying. It needs a rule for who may be substituted, and a control arm.
Nothing in the tree decides it (ladder 1 to 4 silent; at step 5 loss is the smaller edit and reuses a
table).

## Cost class

Edit (1 to 3, 5). Edit 4 is an edit on top of `08_FI_06` (small build, proposed). Lane FI.
