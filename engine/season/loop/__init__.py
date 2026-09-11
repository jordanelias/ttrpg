"""`season.loop` — the driver, its six steps, and the two verb-keyed tables they dispatch on.

  * `driver`     -- `SeasonDriver`, `season()`, and the four module functions around them
  * `calendar` · `matter` · `deliberate` · `resolve` · `witness` · `census` -- THE SIX STEPS    L5
  * `predicates` -- `REQUIRES_PREDICATES`: the four hand-written `requires:` cells.   step 5
  * `effects`    -- `EFFECTS`: one body per verb that writes.                          step 5

`04_CODE_ARCHITECTURE.md` §A.2:134 names this module `loop/` and gives it *"driver + six steps. The
driver is the ONLY constructor of write tokens."* **The six exist as of unit L5 (ED-IN-0206)**; they
were methods on `SeasonDriver` and each body now has its own module, with the §A.2 table's owned
state, `emits` and token quoted at the head of each.

⚠ **THE STEPS ARE BOUND ONTO THE CLASS, NOT DELEGATED TO.** `driver.py` ends with
`SeasonDriver.witness = witness` and five siblings, so `SeasonDriver.witness` IS the module function
and `inspect.getsource` returns the MOVED BODY. Measured rather than argued: replace one binding
with a delegating stub and `test_d2` and `test_d9b` go red **while
`test_witness_writes_no_belief_and_no_conviction` — a pure NEGATIVE assertion — keeps PASSING over a
body it no longer reads.** That is the silent half, and it is why step 9 refused to delegate.

⚠ **`predicates` AND `effects` ARE NOT AMONG THE SIX, AND STAY.** §A.2's line enumerates the STEPS,
not the totality of `loop/`; these two are the verb-keyed tables the fold dispatches on, and they
sit beside the fold that reads them. Recorded rather than left for a later reader to re-derive as a
conformance gap — the same disposition L3 took for `queries/readers.py`, except that one had a
`04`-sanctioned home to go to and these do not.

⚠ **THE TOKEN IS STILL A `WriteClass` PARAMETER IN ALL SIX.** §A.3 row 3 replaces it with an
unforgeable token type minted only by the driver; that is Arc 2's G2, not this unit. L5 delivers the
MODULE boundary; the write discipline follows.

⚠ NEITHER MODULE HERE MAY IMPORT THE DRIVER, and the direction is what keeps it true: a table the
fold reads cannot also read the fold. The driver imports these two; they do not import it, and the six
step modules import them the same way -- `resolve` reads both tables and neither reads `resolve`.

⚠ THIS FILE IMPORTS NEITHER MODULE — the same reason `season/state/__init__.py` and
`season/data/__init__.py` both give at length, and for `effects` a sharper one: importing it runs
ELEVEN `@effect_for` registrations, so an eager package import would make anything wanting one name
from `loop` build the whole effect table. (This said "thirteen" when it shipped; there were ten
`_eff_*`, which `effects.py`, `shape.py` and the plan all stated correctly. A count written from
memory beside three correct copies of it. ⚠ AND IT HAPPENED AGAIN, ON THIS LINE, ON 2026-09-11:
`release` made eleven and both this sentence and `effects.py`'s still read ten — a count written
from memory beside the paragraph recording the last count written from memory. Found by the
`release` adversarial pass. The lesson the first parenthesis drew is the right one and the repair
is the same; what neither buys is a guarantee, because the carrier is prose.)
"""
