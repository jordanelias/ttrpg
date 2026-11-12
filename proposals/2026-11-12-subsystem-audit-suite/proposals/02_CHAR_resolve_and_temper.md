# CHAR — resolve and temper: name what `choice_temperature` divides, and give the departure from the optimum to the person

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` §4) — the gate gains the test-retest reading of `U5a_CHAR_owed_amendments.md` §1 (F-PES-CHAR-04 a).

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.2 row (AMBIGUOUS, internal), §4 row *resolve*, §7, §7b-4, §7b-T; `unified/U1_OWNERS_AND_VOCABULARY.md` D-U1-11m, ledger C-23; `unified/U1_GLOSSARY.md` *resolve*; `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §8 ("nothing under `decision/` names an attribute"); `unified/U3_DEPENDENCY_ORDER.md` node B10, §6.2). Changed: the proposed reader is renamed **`person_q.decisiveness`** (D-U1-11m: `faction_q.resolve` is ratified, `04` §B.6.1, and the RESOLVE step owns the word) and takes `PersonInterior` (`04` §B.10-12), not `Person`; Edit 2's `temper` no longer resolves Focus by name in `decision/` — it is `capability_factor(p, "choice_temper", fx)`, the `choice_temper` use row in `02_CHAR_capability_uses_table.md` (U1 §8; PART D row 27); scratch `probe1.py` marked; named tests; lands-it and tier. The rest stands.

**Lands in batch:** B10. **Depends on:** `02_CHAR_capability_uses_table.md` (B04; the `choice_temper` row and `capability_factor`), `U5a_CHAR_owed_amendments.md` §1 (B10; the test-retest reading).

## Status: PROPOSED

Written by the CHAR audit lane (`audits/02_CHAR_audit.md`, findings F-CHAR-02, F-CHAR-06, F-CHAR-10).
Ratifies nothing. Reference under `CLAUDE.md` §0.05. It is evidence for the open asks M35 and M40 and
for CR-93's design item (2); it does not pre-empt CL-PERSON, which is HELD on a ruled sentence.

## What this changes in `engine/season/` at runtime

At the shipped values, nothing: every new term ships at its control and the one-season hash of
`build_realm(0)` is EQUAL. It adds one reader (`person_q.decisiveness`), one hook in
`decision/choose.py::_sample_order` that multiplies the temperature by a per-person factor read through the
`choice_temper` use row (1.0 for every person today, because the shipped cast carries no attributes and the
gain ships at 0), one
ordering fix (H-362), and a second column in one instrument.

## The problem, with evidence

**The departure from the optimum is not the person's.** R-08 asks that characters *"may not make the
optimal decision based upon their epistemic knowledge and personal inclinations"*. The built answer is
`_sample_order`: Gumbel noise at one realm-wide `choice_temperature` (0.05). Read on the built realm,
cast only, six common referents, fifteen common candidates (scratch `probe1.py`, not in the repository,
seeds 0 and 1, `PYTHONHASHSEED=0`; restated by the gate's `decision_spread --decisions` pairwise table):

| reading | seed 0 | seed 1 |
|---|---|---|
| sampled top is not the score's top | 127 of 276 (46%) | 117 of 276 (42%) |
| two cast persons whose vectors are near-identical (cosine > 0.99) take different tops | 56% | 62% |
| control: every person given the realm-mean vector; pairs taking different tops | 74% | 70% |
| two persons whose vectors are opposed (cosine < 0) take different tops | 95% | 95% |
| the same pairs at temperature 0 (score order only): near-identical / opposed | 11% / 95% | 11% / 95% |

So the score separates characters cleanly (11% against 95%), and the draw then makes two identical
characters disagree in seven decisions of ten. A watcher of one decision cannot tell a difference of
conviction from the draw.

**The effective temperature already varies by person, by accident.** The noise is `tau × Gumbel` in
score units, and a person's score margins scale with the length of his projected pursuit vector, which
runs from 0.14 to 0.89 across the 46 cast (a factor of six). The per-person share of outvoted tops
correlates with that length at r = −0.63 (seed 0) and −0.48 (seed 1). A person whose authored pursuits
cancel in axis space is close to random; one whose pursuits align is close to deterministic. Nothing
declares this, no sheet shows it, and no fixture's note says that `choice_temperature` is in the units
of a quantity that differs sixfold between persons.

**The instrument's headline cannot see any of this.** `decision_spread --season` reads *distinct
per-person resolved verb multisets*: 83 of 83 at the shipped tree, 83 of 83 with every person given the
realm-mean vector, 83 of 83 with the alignment table uniform (one season, seed 0, hashes `5ab73af2`,
`c90e4a6c`, `ef134b29`). A reading that is at its ceiling under both controls cannot observe the
failure it was built to exclude (`CLAUDE.md` §0.1 pt 2). `requirements.yaml` R-06 already records the
same of `--decisions`' faction leg (*"the leg rewards the draw"*).

**H-362** (register line 6554): `score_terms` and `pursuit_lean` sum over `PURSUIT_AXES`, a frozenset,
where `_lean` and `pursuit_cosine_axes` sum over the sorted `_AXES`. The row measures no divergence on
today's cells. It is still two orders for one dot product, and the port sums in neither.

## The resolution, decided

| # | decided | ladder step |
|---|---|---|
| 1 | The sixfold spread is KEPT and NAMED, not normalised away: `person_q.decisiveness(p)` = the length of `projected_axes(p)`; `choice_temperature`'s fixture note and hole row H-96 state that the draw is read against it | 5. Normalising would make a man of weak or self-cancelling pursuits as decisive as a zealot, which removes the one manner the tree already has; hiding it leaves a hidden variable. The architecture's answer is a reader with one owner |
| 2 | A per-person multiplier on the temperature, `temper(p)`, read through the `choice_temper` use row (key `attr.mind.focus`, role `judgement`), 1.0 where unauthored | 3. `ED-IN-0347` AR-23 and CR-93 item (2) already name it (*"a per-person τ falling with Focus"*); this fixes its site and its control, not its coefficient |
| 3 | `decision_spread --season` prints, beside the distinct-multiset count, the same count at temperature 0 on the same world, and `--decisions` prints the pairwise table above | 5. An instrument reading printed without the arm that can fail is the defect; a second column is an edit to the owner, not new apparatus |
| 4 | The three set-order sums iterate `_AXES` | 4. `data/pursuits.py::_AXES` is the stated owner of the order and its comment gives the reason |

Item 2 does **not** store an offset on a projected axis, so it does not meet the ruled sentence
CL-PERSON is held on (`ED-IN-0261`: *"two people with identical pursuits ARE identically disposed and
the variation comes from the candidates"*): two such people stay identically disposed in their scores
and differ in how reliably they follow them. Whether that is within the sentence is already answered
by a later ruling: CR-93's entry records that `ED-IN-0347` narrows the sentence and does not reverse it
(*"ED-IN-0261's 'identically disposed' sentence is narrowed, not reversed"*), and names this term. So
it is not escalated.

## The exact edits, by owner

1. **`engine/season/queries/person_q.py`** — add

   ```python
   def decisiveness(p: PersonInterior, shift: float = 0.0) -> float:
       """HOW FIRMLY `p`'s PURSUITS POINT ONE WAY: the length of `projected_axes(p, shift)`. The draw in
       `decision/choose.py::_sample_order` is read against score margins, which scale with this, so it is
       the person's decisiveness at a given `choice_temperature`. Person-side (AX-2); stores nothing."""
       v = projected_axes(p, shift)
       return math.sqrt(sum(v[a] ** 2 for a in _AXES))
   ```

   and show it on `decision/sheet.py::DevelopmentSheet` as a derived line (the sheet's docstring already
   separates stored fields from derived ones).
2. **`engine/season/decision/choose.py::_sample_order`** — `tau = float(fx.get("choice_temperature")) *
   temper(p, fx)`, with

   ```python
   def temper(p: PersonInterior, fx) -> float:
       """THE PERSON'S OWN FACTOR ON THE CHOICE TEMPERATURE (CR-93 item 2, AR-23):
       `capability_factor(p, "choice_temper", fx)`, 1.0 where no row or at `temper_gain` 0."""
   ```

   It names no attribute: the key, the role and the gain come from the use row
   `{use: choice_temper, role: judgement, key: attr.mind.focus, side: actor, gain: temper_gain}`
   (`02_CHAR_capability_uses_table.md`; U1 §8: nothing under `decision/` names an attribute); the factor is
   `about_mid`, monotone and exactly 1 at the scale's mid-point; `temper_gain` shipped at 0 (U1 ledger C-23).
   One hole-register row.
3. **`engine/season/decision/choose.py::score_terms`** and **`queries/person_q.py::pursuit_lean`** —
   `for ax in _AXES` (imported from `data/pursuits.py`, as `person_q` already imports it).
4. **`engine/season/harness/decision_spread.py`** — `play_season` takes the temperature-0 reading on a
   second build of the same seed; `print_season` prints both counts on one line; `read_decisions` adds
   the pairwise table (score-top and sampled-top disagreement by cosine bin). The docstring's *"NOTHING
   HERE IS PINNED AS A GOLDEN"* stands.
5. **`engine/season/data/fixtures.py`** and **`hole_register.yaml` H-96** — one sentence each: the
   temperature is in score units; score margins scale with `person_q.decisiveness`; the 46 cast read 0.14
   to 0.89 at this tree.

## Gate (an execution artifact, §0.2)

- `build_realm(0)` one-season hash EQUAL with every edit in (the control).
- `engine/season/tests/test_in62_decision_spread.py` extended by one assertion: under `--control` the
  temperature-0 column reads strictly fewer distinct multisets than the shipped arm's. If it does not,
  the instrument still cannot fail and the edit is wrong.
- Two hand-built persons with equal pursuits and Focus at the scale's two ends: at `temper_gain` > 0,
  over twenty draw seeds, the low-Focus person's top differs from the score's top strictly more often;
  at `temper_gain` 0 the two are byte-identical.
- Named tests (new, `engine/season/tests/test_temper.py`): `test_temper_is_one_at_gain_zero`;
  `test_low_focus_departs_from_the_score_top_more_often`; `test_decision_names_no_attribute` (a source scan
  of `decision/choose.py` for `attribute_key(`); `test_decisiveness_is_the_projected_vector_length`. And the
  one assertion added to the existing `engine/season/tests/test_in62_decision_spread.py`.

## Falsifier

Sweep `choice_temperature` to 0 and the pairwise table's near-identical row must fall to the score-top
row (11% at this tree). If it does not, something other than the draw separates identical persons and
the finding is wrong.

## NERS reading (§0.06)

- **N.** Without a named owner the manner the tree already has is invisible: a player cannot learn that
  one councillor is steady and another erratic, so two persons who want the same things are one
  character (CL-PERSON's own N-line). From the instrument's direction: a uniqueness count that reads
  full under both controls protects nothing.
- **R.** Customization: Focus becomes a lever on how reliably a character follows his values, with no
  effect on what they are. The world still surprises when nobody watches, and the surprise now has an
  author.
- **S.** One temperature, one multiplier, one reader. `temper` and `competence` are both
  `capability_factor` over a use row, so the two attribute uses in `decision/` share one method and name no
  attribute.
- **E (last, as a ratio).** One function, one hook, one column, one loop variable. The alternative
  (stored manner axes) is CL-PERSON's and costs a ruling.

## Cost class

Edit (items 1, 3, 4, 5) and small build (item 2, which lands with CR-93's design or after it).

**Lands it and tier.** The B10 batch, an IN `valoria-author` session on `sonnet` (`high`), closed by B10's
`methodology-close` once. **Hash movers.** None at `temper_gain` 0 (control); declared when it flips.
