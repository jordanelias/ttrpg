# GAME — the propagation reading counts what moved, not what was written about

## Status: PROPOSED

Source: `audits/16_PESSIMIST_GAME.md` F-PES-GAME-01, F-PES-GAME-02, §1.1, §1.2. Read at `4995824`.
Reference only (`CLAUDE.md` §0.05). **Amends** `01_CORE_requirements_reading_record.md` §2 (the chain
reading for R-01 and R-02); it does not add a second reading beside it. Lane IN.

## What it changes in `engine/season/` at runtime

Nothing in the loop. The one harness reading CORE 03 §2 adds (`harness/chronicle.py --propagation`)
prints three more columns, and `requirements.yaml` R-01 and R-02 are read on them.

## The problem, with evidence

CORE 03 §2 measures R-01 by counting consequence chains (A's Event deposited with B and cited by an act
of B) and R-02 by the share of B's later acts whose verb or subject differs when one of A's acts is
withheld. Both would read "above the control" today, and both would be true of a realm in which nothing
a person does changes anything but paper:

- **Chains are plentiful and are about paper.** Seed 0, three seasons (`runs/PES_GAME/x1_s0_k3.txt`):
  513 executed answers to another person's or a clock's Event; 436 (85%) land in the information
  verbs (83% and 85% at seeds 2 and 1); the largest sources are clock
  Events (`stores.changed → create_record` 29, `yield.taken → create_record` 25). No executed answer
  lands in personal combat, mass battle, the settlement verbs or training.
- **Divergence is plentiful and changes no state.** The King abstaining for three seasons
  (`runs/PES_GAME/x4_s0.txt`) changes the executed verbs of 59 of 82 other persons, and the world ends
  with the same persons, seats, sites, rungs and stores; one unheld office and 42 duties differ.
- **The world with nobody acting ends where the played world ends**, in every skeleton component, at
  seeds 0, 1 and 2, bar one death at seeds 1 and 2 (`x1_s*_k3.txt`, the PLAY vs NULL lines).

A reading that cannot tell this realm from one where decisions have consequences is §0.1 pt 2's absent
assertion.

## The resolution (decided)

The propagation reading reports, per seed, beside CORE 03's chain count and fork divergence:

1. **Moved by persons** — the state projection of the played arm against the **null arm** (the same
   built world, a chooser that returns no act, MATTER and CALENDAR running), by component: persons,
   seat `hold`s, site conditions, rungs, stores, stance rows, pursuits, convictions. Printed as counts
   of differing entries. The projection is `runs/PES_GAME/pes.py::proj`, moved into
   `harness/chronicle.py` as one pure function over a `World` (it reads the stores the content hash
   reads; it owns no rule).
2. **Answered outside writing** — executed cross-person answers whose answering verb is not a
   deposit-only or emission-only row. "Deposit-only / emission-only" is not a new list: it is
   `corpus_run`'s existing `EMITS AND WRITES NOTHING` census plus the rows whose only `writes` is a
   `Record`, a `Proposition` or a `Claim` (read from `verb_table.yaml`'s `writes` column).
3. **Terminals answered** — for `person.died`, `tenure.closed`, `field.won`/`field.lost`,
   `matter.determined`, `news.told`, `body.changed`: emitted, and of those, how many stand among the
   causes of another person's executed act.

**The statuses are read on these.** `[ASSUMPTION; medium; Jordan to correct]` R-01 reads `met` when, at
each of three seeds, column 2 is above zero and column 3 is above zero for at least `person.died` or
`tenure.closed` wherever one was emitted; R-02 reads `met` when a withheld act (CORE 03's fork) changes
column 1 in a component other than records, propositions and ledgers. Otherwise `partial`, in the commit
that lands the reading, with the line recorded in `reading:`. On today's tree both would read `partial`
(§ evidence above). No threshold beyond "above the null arm".

## Edits

- `engine/season/harness/chronicle.py`: `--propagation` (CORE 03's flag) gains the null arm and the three
  columns; `proj` and the seam count are two pure functions (source: `runs/PES_GAME/pes.py::proj`,
  `seam_edges`; the engine map in that scratch file is NOT carried — column 2 reads the verb table).
- `engine/season/requirements.yaml`: R-01 and R-02 `measure:` name the command; `status:` follows the
  first reading.
- Nothing else. No test asserts the columns' values (they are readings); the instrument's own control is
  below.

## Gate

`python -m engine.season.harness.chronicle --propagation --seeds 0 1 2 --seasons 3` prints the columns.
**The instrument's control, both directions** (§0.1 pt 4): (a) the null arm against itself reads zero in
every column; (b) a planted consequence is seen — the bodies hazard set to 1 for one seat-holder
(`x2_death.py`'s proxy) moves `persons` and `seat holds` in column 1 and puts a `person.died` in column
3's denominator. If either control fails the reading is void.

Falsifier for the claim this proposal rests on: a played arm that differs from the null arm in seats,
sites or rungs at any seed without a planted hazard. At seeds 0, 1, 2 over three seasons none does,
except the one `capture` death.

## NERS

- **N.** Without it the two `met` rows that carry the loop's central claim cannot fail. Cut the null arm
  and the reading again counts correspondence.
- **R.** Completeness: the reading is defined at the extreme (nobody acts) and uses it as its zero.
- **S.** One reading for R-01/R-02, not two; consistent with `aperture`'s control line.
- **E** (last): two pure functions and three printed columns.

Cost class: edit (after CORE 03 lands; it can land with it).
