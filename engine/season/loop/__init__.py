"""`season.loop` — the driver, its six steps, and the two verb-keyed tables they dispatch on.

  * `predicates` -- `REQUIRES_PREDICATES`: the four hand-written `requires:` cells.   step 5
  * `effects`    -- `EFFECTS`: one body per verb that writes.                          step 5

`04_CODE_ARCHITECTURE.md` §A.2 names this module `loop/` and gives it *"driver + six steps. The
driver is the ONLY constructor of write tokens."* The driver itself (`SeasonDriver`, `season()`)
arrives at step 9; these two tables land first because they are what the fold DISPATCHES ON, and
because they are the last two decorator-filled registries still sitting in `shape.py`.

⚠ NEITHER MODULE HERE MAY IMPORT THE DRIVER, and the direction is what keeps it true: a table the
fold reads cannot also read the fold. When step 9 brings `driver.py` in, it imports these two;
they will not import it.

⚠ THIS FILE IMPORTS NEITHER MODULE — the same reason `season/state/__init__.py` and
`season/data/__init__.py` both give at length, and for `effects` a sharper one: importing it runs
TEN `@effect_for` registrations, so an eager package import would make anything wanting one name
from `loop` build the whole effect table. (This said "thirteen" when it shipped; there are ten
`_eff_*`, which `effects.py`, `shape.py` and the plan all state correctly. A count written from
memory beside three correct copies of it.)
"""
