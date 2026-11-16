"""`season.loop` — the driver, its seven steps, and the two verb-keyed tables they dispatch on.

  * `driver`     -- `SeasonDriver`, `season()`, and the four module functions around them
  * `calendar` · `matter` · `deliberate` · `resolve` · `encounter` · `witness` · `census` --
    THE SEVEN STEPS    L5 (`encounter` is the seventh, `ED-IN-0279` clause (a))
  * `predicates` -- `REQUIRES_PREDICATES`: the four hand-written `requires:` cells.   step 5
  * `effects`    -- `EFFECTS`: one body per verb that writes.                          step 5
  * `sides`      -- `sides_of`: which shape a contest's parties take.                  M4

`04_CODE_ARCHITECTURE.md` §A.2:134 names this module `loop/` and gives it *"driver + six steps. The
driver is the ONLY constructor of write tokens."* (AMENDED 2026-09-28 to seven). Each step has its
own module (unit L5, ED-IN-0206), with the §A.2 table's owned state, `emits` and token quoted at the head of each.

⚠ **THE STEPS ARE BOUND ONTO THE CLASS, NOT DELEGATED TO.** `driver.py` ends with
`SeasonDriver.witness = witness` and six siblings, so `SeasonDriver.witness` IS the module function
and `inspect.getsource` returns the real body. A delegating stub would fail `test_d9b` and silently
vacate every pure NEGATIVE assertion over a step's source, which is why step 9 refused to delegate.

⚠ **`predicates` AND `effects` ARE NOT AMONG THE STEPS, AND STAY.** §A.2's line enumerates the STEPS,
not the totality of `loop/`; these two are the verb-keyed tables the fold dispatches on, and they
sit beside the fold that reads them. Recorded rather than left for a later reader to re-derive as a
conformance gap — the same disposition L3 took for `queries/readers.py`, except that one had a
`04`-sanctioned home to go to and these do not.

⚠ **THE TOKEN (G2).** §A.3 row 3's token type is `state/gate.py::Token`, constructed only in
`driver.py::mint_token`. `SeasonDriver.season` mints one per barrier and passes it to six of the seven
steps as their first argument; `deliberate` receives none. `tests/test_g2_token.py` is the scan
`04:206` grades MECHANICAL.

⚠ NEITHER MODULE HERE MAY IMPORT THE DRIVER, and the direction is what keeps it true: a table the
fold reads cannot also read the fold. The driver imports these two; they do not import it, and the six
step modules import them the same way -- `resolve` reads both tables and neither reads `resolve`.

⚠ THIS FILE IMPORTS NEITHER MODULE — the same reason `season/state/__init__.py` and
`season/data/__init__.py` both give at length, and for `effects` a sharper one: importing it runs
every `@effect_for` registration, so an eager package import would make anything wanting one name
from `loop` build the whole effect table.
"""
