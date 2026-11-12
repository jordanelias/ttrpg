# 16 · PESSIMIST · SC · B — One reader of a ledger: what a person acts on, says, shows and plans by is one belief

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §2 (D-48 taken A, forgetting computed when
read: once `01_CORE_claim_fade_as_read.md` lands the stored `confidence` is the deposit-time value and the present value
is `state/ledgers.py::present_confidence`; the weight reads that, not raw `c.confidence`), §1 (CONFORMS; the read-time
weight is not the eviction comparator, `04` PART D 39, which keeps `confidence` and `recency` only), §7/§7b (tests, tier);
U3 B09 (after the fade-as-read commit), §6.2 (`p2c_two_readers.py`, `p2d_stale_sighting.py`, `p2b_lie_extremes.py` are
not in the repository). Changed: the formula, the sentence on what falls with age, edit 1, the gate's test names.

## Status: PROPOSED (not ratified by being written; `CLAUDE.md` §2)

Lands in batch: **B09** (SC with IN, FI), after `01_CORE_claim_fade_as_read.md` and `16_PESSIMIST_CORE_a_refusal_is_remembered.md`
(U3 §1 item 10). Depends on: `state/ledgers.py::present_confidence` (fade-as-read).

Finding: `audits/16_PESSIMIST_SC.md` F-PES-SC-01 (§2.2). Owners touched are the telling workplan's
(`ED-IN-0282`, lane IN) and FI's; listed for those lanes. Runs: `runs/PES_SC/p2c_two_readers.py`,
`p2d_stale_sighting.py`, `p2b_lie_extremes.py`.

## What it changes in `engine/season/` at runtime

`said_of` (what a person passes on), `decision/sheet.py::chronicle` (what his sheet shows) and
`world_q`'s stage reader (whether he thinks a goal's stage is passed) read his ledger through the same
weighed comparator `epistemic.belief_contradicts` already uses; and that comparator's weight gains one
factor, the claim's own decayed confidence. Hashes move wherever a person holds two values for one cell
from different sources; declared.

## The problem, measured

`LedgerReader` has two comparators (`queries/person_q.py::LedgerReader._best`): with a `weigh`,
*(support, when, confidence)*; without, *(when, confidence)*. One caller passes a `weigh`
(`epistemic.py:133`). The others do not: `person_q.py:1195` (`said_of`), `decision/sheet.py:199`
(`chronicle`), `world_q.py:2936` (stages; its docstring: *"The reader takes no `weigh` … [ASSUMPTION;
medium; Jordan to correct -- B3.1; revert: pass the closure in from the one caller B3.2 adds]"*).

A hearer who holds a cell firsthand, lied to one season later (120 seeded seasons per row):

| verb | landed | weighed reader holds the truth | plain reader holds the truth |
|---|---|---|---|
| `lie` | 32 | 32 | 1 |
| `tell` (a Partial copy is garbled) | 27 | 27 | 4 |

So the eyewitness is not stopped from acting on what he saw, and says, shows and plans on what he was
told last. In the realm (seed 1, season 3) a hearer lied to about a settlement's grain ends with weighed
belief 40 and plain belief 113.

Each reader is wrong at its own extreme (`p2d_stale_sighting.py`): a sighting nine seasons old at
confidence 5 against the same new value from `n` distinct tellers at confidence 100 —

| n tellers | 1 | 3 | 10 | 30 |
|---|---|---|---|---|
| weighed reader | old | old | old | **old** |
| plain reader | new | new | new | new |

The weighed reader gives a firsthand claim weight 1.0 whatever its age or confidence, and a told claim
at most `told_weight × relation × record`, which the noisy-OR over origins can bring near 1 and never to
it; worse, each fresh teller contradicts the stale sighting and so earns `record` 0.5 (each told claim
weighed 0.25 in the run). A man who saw a full granary last year cannot be told it is empty by the whole
town. The plain reader believes whoever spoke last.

## The resolution, decided

One comparator, used by every reader of a belief; its weight includes how sure the holder still is.

    weigh(c) = (present_confidence(c) / confidence_default) × ( 1.0                              if c.chain is empty
                                                                told_weight^hops × relation × record   otherwise )

The present confidence is the quantity that falls with age and with refraction: refraction
(`refracted_confidence`) sets the deposit-time `confidence`, and age is applied when read by
`state/ledgers.py::present_confidence` (`01_CORE_claim_fade_as_read.md`, one owner of fading; D-48), so no new
field or clock is needed. A fresh sighting (confidence 100) still
outweighs any single told claim (at most 1.0 × its own confidence share); a sighting decayed to 5 is
outweighed by one credible teller. Ladder step 5 (what the architecture makes plain: two owners of
"which belief does this person hold" is the §8 defect, and `_best`'s own docstring says the comparator
*"lives once"*), with step 3 for the stage reader (its own revert line).

`teller_weight`'s docstring says it *"never reads `confidence`"* so that deposit-time refraction and
read-time weighting *"multiply into nothing shared"*. They still do not: refraction writes
`confidence`; the reader multiplies by it once. What changes is that the reader stops discarding it.

## Exact edits

1. **`engine/season/decision/options.py::teller_weight`** — `weigh(c)` multiplies its result by
   `present_confidence(c) / fx.get("confidence_default")` for every claim, told or not (the empty-chain branch
   returns that share instead of `1.0`). Control: a fixture `weigh_confidence` (bool, shipped `True`,
   swept `False`), read once per closure; at `False` the function is today's, exactly.
2. **`engine/season/decision/options.py::ledger_weigh`** — returns the closure whenever the ledger
   holds *any* claim below full confidence or any told claim (today: any told claim), so a ledger of
   fresh firsthand claims still takes the plain reader and reads as before.
3. **`engine/season/queries/person_q.py::said_of` and `::lie_said_of`** — a keyword `weigh=None`,
   handed to `LedgerReader(pool, weigh)`. Caller: `decision/options.py::opening_set` passes
   `weigh=ledger_weigh(p, fx)` at the one call site (`said_of_entity[entity] = …`). `person_q` imports
   nothing from `decision/` (the closure is an argument, as it is for `LedgerReader`).
   ⚠ `_support` under a `weigh` ranks `latest_about` across predicates (its docstring: *"no caller
   weighs `latest_about` today, and the position that weighs `said_of` … decides it"*). Decided here:
   accepted. A person passes on what he is surest of about a subject, not the newest thing he holds.
4. **`engine/season/decision/sheet.py::chronicle`** — signature `chronicle(p, fx=None)`;
   `reader = LedgerReader(p.ledger, ledger_weigh(p, fx) if fx is not None else None)`; its callers in
   `decision/sheet.py` and the harness pass the fixtures they already hold.
5. **`engine/season/queries/world_q.py`** (the stage reader at `:2936`) — take the closure as a
   parameter from its one caller, as its docstring's revert line says.
6. **Hole register**: the row that carries `H-183` gains this proposal's control; no new row
   (`weigh_confidence` is a switch on an existing magnitude, `claim_decay_per_season`).

## Gate (an execution artifact)

The probes were lane scratch (not in the repository). NEW `engine/season/tests/test_one_reader_of_a_ledger.py`:
`test_said_of_sheet_and_belief_contradicts_agree_on_every_cell` (the falsifier as a planted ledger),
`test_stale_sighting_falls_to_enough_tellers`, `test_fresh_sighting_holds_against_one_teller`,
`test_weigh_confidence_false_reproduces_today`. Command:
`python -m pytest engine/season/tests/test_one_reader_of_a_ledger.py -q`; then `report` / `delta HEAD` (the declared mover).
The scratch readings, once committed:

`p2c_two_readers.py` after the edit: the two columns are equal on every row (32 / 32 and 27 / 27 for the
knowing hearer). `p2d_stale_sighting.py`: at `c0 = 80` the sighting holds against one teller and falls to
a number of tellers the run prints; at `c0 = 5` it falls to one. Control: `weigh_confidence=False`
reproduces today's weighed column, and the three re-pointed callers then agree with it.

## Falsifier

Any (holder, cell) in a seeded realm season for which `said_of`'s value, the sheet's value and
`belief_contradicts`' value differ. Present today (the seed 1, season 3 hearer above).

## NERS

- **N**: cut the second comparator and nothing is lost that any reader was built to rely on; three
  call sites stop disagreeing with the fourth. From the player's side (top-down) the sheet shows what
  the character will act on; from the propagation side (lateral, FI) a rumour passed on is the one the
  teller believes.
- **R**: non-omniscient and not perfectly rational (R-08) now has one definition of what a person
  believes; an old certainty can be worn down by testimony, which is a story (the town that convinces
  the absentee his granary burned) the weighed reader forbade and the plain reader made automatic.
- **S**: one ladder for belief.
- **E (ratio)**: one multiplication and three keyword arguments; removes a comparator's worth of
  special reading from every future caller.

## Cost class

Small build (five hunks, one fixture, three call sites; a declared hash mover that needs a realm
before-and-after reading at the batch close). Tier: `sonnet`, effort `high`. Hash movers declared: every world where a
person holds two values for one cell from different sources; one re-pin at B09's close. Lands it: B09, order 1 → 2
(with the control at `False`, hash-equal) → 3 → 4 → 5 → the flip to `True`.
