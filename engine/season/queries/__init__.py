"""`season.queries` — the ownerless functions. Nothing here owns state and nothing here writes.

  * `world_q`  -- the thirteen World-FIRST functions, plus `WorldReader`.
  * `person_q` -- the asker-first family: `entrenchment`, plus `LedgerReader`.
  * `cache`    -- the barrier indexes, single-owned.

`04_CODE_ARCHITECTURE.md` §A.2: *"queries/ ownerless functions: world_q (World first) · person_q
(asker first) · cache (barrier-built)"*, and the table below it gives every function here the
token column `—`: **no function in this package takes a write token, so none of them can write.**
**All three modules exist as of unit L3 (ED-IN-0206)**, and the package is no longer a superset of
the roster.

⚠ **`readers.py` IS GONE, AND ITS DISPOSAL IS THE ANSWER TO A QUESTION THIS FILE ASKED AND
DEFERRED.** It said: *"By source they would split `WorldReader` → `world_q` and `LedgerReader` →
`person_q`; `person_q` does not exist until step 7 ... whether §A.2's roster then absorbs them is a
Layer-1 call for that step, not this one."* L3 is that step and took the call as written, rather
than leaving a fourth module in a package the spec enumerates with three. `WorldReader` takes a
`World` and asks it; `LedgerReader` takes claims and nothing else. **Splitting them by source is
also what makes §A.3 row 2's property checkable** — with the person-side reader in `person_q`,
`test_person_q_cannot_reach_the_world_side` can assert by import that this half cannot reach the
other, which is the whole content of *"two modules; the second cannot import the first"* (T-f).

⚠ THIS FILE IMPORTS NONE OF THE THREE, for the reason `season/state/__init__.py` and
`season/data/__init__.py` both record at length: an eager package import makes anything that wants
one name pay for every registry the other module loads, and it silently removes the loaders' last
external patch point. `cache` imports `world_q`, and nothing else here imports anything else here —
which is not an accident but §A.3 row 2's property, and `test_person_q_cannot_reach_the_world_side`
is what holds the half of it that matters.
"""
