# GAME — the propagation reading counts what moved, not what was written about

Reconciled: 2026-11-12, U5d closure — folded **A-15**, **A-19** and the land rulings (**A-57, A-58, A-66**): the game gate's clauses (`person.died` and `tenure.closed` among the causes of another's executed act; the played skeleton differing between seeds) now have producers the rulings order: natural death, the deed race for an empty throne, and a victor's seizure passing land and seats. The reading gains one column, tenure changes by cause (death, term, revocation, claim, conquest). No other step changes.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: U3 C3-K5 and C-U5a-01 (one instrument per property: the
removal test of `16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading.md` is R-01's and R-02's `measure:`; this file's
`requirements.yaml` edit is **withdrawn** and the status rule that rode it is removed; the propagation reading is a
chronicle reading wired to no `measure:`); `R5_READ.md` §2 (the collision on R-01/R-02 `measure:`; R5's "list both
commands" is superseded by C3-K5), §7/§7b (signatures, tests, tier); U3 B02, §6.2 (`runs/PES_GAME/*`, `x2_death.py`
are not in the repository). **Corrected at the tree:** `01_CORE_requirements_reading_record.md` §2 is withdrawn and
`harness/chronicle.py` has no `--propagation` flag (its arguments are `--seed` (required), `--seasons`, `--arm`, `--cap`,
`--all-acts`, `--chains`, `--min-depth`, read 2026-11-12), so this file adds the flag itself and composes on nothing
of CORE 03 §2; the gate runs per `--seed`. Changed: the head paragraph, "What it changes", the status section, the
edits, the gate command.

## Status: PROPOSED

Lands in batch: **B02** (IN), after `16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading.md`. Depends on: nothing
unlanded (`harness/chronicle.py`, `corpus_run`'s census and `verb_table.yaml` exist).

Source: `audits/16_PESSIMIST_GAME.md` F-PES-GAME-01, F-PES-GAME-02, §1.1, §1.2. Read at `4995824`.
Reference only (`CLAUDE.md` §0.05). Lane IN. A reading beside the removal test, not a second `measure:` for the
same property (C3-K5): the removal test asks whether one person's choice changes others' acts; this asks whether
the played world's state differs from a world where nobody acts.

## What it changes in `engine/season/` at runtime

Nothing in the loop. `harness/chronicle.py` gains a `--propagation` reading that prints three columns. No
`requirements.yaml` row reads it.

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

The propagation reading reports, per seed:

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

**No status is read on these** (C3-K5: the removal test is R-01's and R-02's `measure:`). The columns are
a reading a session runs and reports beside it; no threshold beyond "above the null arm" is stated.

## Edits

- `engine/season/harness/chronicle.py`: a `--propagation` flag (new; `main`'s parser at `:204`), running the
  played arm and the null arm (the same built world, a chooser that returns no act, MATTER and CALENDAR
  running) for `--seed` and `--seasons`, and printing the three columns. Three pure functions over `World`
  (they read the stores the content hash reads and own no rule):
  `moved_by_persons(w_played, w_null) -> dict[str, int]` (column 1, by component),
  `answered_outside_writing(w, verb_table) -> int` (column 2; reads `verb_table.yaml`'s `writes` column and
  `corpus_run`'s `EMITS AND WRITES NOTHING` census, the engine map in the scratch file is NOT carried),
  `terminals_answered(w) -> dict[str, tuple[int, int]]` (column 3: emitted, and among another person's
  executed act's causes). Source of the projection: the scratch `runs/PES_GAME/pes.py::proj`, rewritten here,
  not copied (the scratch is not in the repository). The docstring and `--help` define the reading in one
  sentence (CLAUDE.md §4).
- Nothing else. No `requirements.yaml` edit (withdrawn, C3-K5).

## Gate

NEW `engine/season/tests/test_chronicle_propagation.py`: `test_null_arm_against_itself_reads_zero_in_every_column`
(control a), `test_planted_body_hazard_moves_persons_and_seat_holds` (control b; the plant replaces the scratch
`x2_death.py`: the bodies hazard set to 1 for one seat-holder). Command:
`python -m pytest engine/season/tests/test_chronicle_propagation.py -q`, then
`python -m engine.season.harness.chronicle --seed N --seasons 3 --propagation` for N in 0, 1, 2 prints the columns.
**The instrument's control, both directions** (§0.1 pt 4): (a) the null arm against itself reads zero in
every column; (b) a planted consequence is seen — the bodies hazard set to 1 for one seat-holder
(`x2_death.py`'s proxy) moves `persons` and `seat holds` in column 1 and puts a `person.died` in column
3's denominator. If either control fails the reading is void.

Falsifier for the claim this proposal rests on: a played arm that differs from the null arm in seats,
sites or rungs at any seed without a planted hazard. At seeds 0, 1, 2 over three seasons none does,
except the one `capture` death.

## NERS

- **N.** Without it nothing reports whether the played world differs from a world where nobody acts. Cut
  the null arm and the reading again counts correspondence.
- **R.** Completeness: the reading is defined at the extreme (nobody acts) and uses it as its zero.
- **S.** One instrument per property (C3-K5): the removal test measures R-01/R-02; this reports state moved;
  consistent with `aperture`'s control line.
- **E** (last): three pure functions and three printed columns.

Cost class: edit. Tier: `sonnet`, effort `high`. Hash movers declared: none (a harness reading). Lands it: B02,
after the nine-gate file; one commit with its test file.
