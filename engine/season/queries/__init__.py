"""`season.queries` — the ownerless functions. Nothing here owns state and nothing here writes.

  * `world_q`   -- the thirteen World-FIRST functions, plus `WorldReader`.
  * `person_q`  -- the asker-first family: `entrenchment`, plus `LedgerReader`.
  * `cache`     -- the barrier indexes, single-owned.
  * `faction_q` -- `resolve(w, prop) -> Faction`, §B.6.1's one constructor for the five-field
    governance VIEW, and §C.5.1's roster contract calls it by that dotted name. See
    `faction_q.py`'s own docstring for the ambiguity this is: §A.2:132's enumeration names three
    modules and `04` is NOT edited to add a fourth (`layer-conformance` B4: "never resolve it by
    editing `04` ... a spec edited to match its implementation checks nothing"), even though
    §B.6.1/§C.5.1 -- both also ratified, both untouched -- already presuppose this module exists
    by that path. Named at the site rather than fixed at the source, per B4's third disposition.

`04_CODE_ARCHITECTURE.md` §A.2: *"queries/ ownerless functions: world_q (World first) · person_q
(asker first) · cache (barrier-built)"* -- unedited, and now stale on this one point rather than
authoritative for it -- and the table below it gives every function here the token column `—`:
**no function in this package takes a write token, so none of them can write.** **All three of
the enumerated modules exist as of unit L3 (ED-IN-0206)**, and the package is no longer a superset
of the roster.

⚠ **THIS IS THE SAME AMBIGUITY `world_q.py` AND THIS FILE ALREADY RESOLVED ONCE, THE OTHER WAY --
NAMED, NOT SILENTLY CONTRADICTED.** `world_q.py`'s own docstring argues against a `polity_q.py`
"rather than left as a FOURTH module in a package the spec enumerates with three", and unit L3
folded `WorldReader`/`LedgerReader` into `world_q`/`person_q` for the same reason. `faction_q` is
not that case: §B.6.1 and §C.5.1 name it by its own dotted path (`faction_q.resolve`), which
neither `WorldReader` nor a hypothetical `polity_q` was ever named as. The precedent is followed
where it applies (do not mint a module the spec never names) and distinguished where it does not
(do not fold code the spec explicitly names elsewhere into a module the spec does not name it in).

⚠ **`readers.py` IS GONE, AND ITS DISPOSAL IS THE ANSWER TO A QUESTION THIS FILE ASKED AND
DEFERRED.** It said: *"By source they would split `WorldReader` → `world_q` and `LedgerReader` →
`person_q`; `person_q` does not exist until step 7 ... whether §A.2's roster then absorbs them is a
Layer-1 call for that step, not this one."* L3 is that step and took the call as written, rather
than leaving a fourth module in a package the spec enumerates with three. `WorldReader` takes a
`World` and asks it; `LedgerReader` takes claims and nothing else. **Splitting them by source is
also what makes §A.3 row 2's property checkable** — with the person-side reader in `person_q`,
`test_person_q_cannot_reach_the_world_side` can assert by import that this half cannot reach the
other, which is the whole content of *"two modules; the second cannot import the first"* (T-f).

⚠ THIS FILE IMPORTS NONE OF ITS SUBMODULES, for the reason `season/state/__init__.py` and
`season/data/__init__.py` both record at length: an eager package import makes anything that wants
one name pay for every registry the other module loads, and it silently removes the loaders' last
external patch point. Within the package, `cache` imports `world_q` and `faction_q` imports
`world_q` (reusing `members()` rather than re-deriving membership, §8) — both WORLD-FIRST modules
reading another world-first module, never the direction §A.3 row 2 forbids: `person_q` still
imports neither, and `test_person_q_cannot_reach_the_world_side` is what holds THAT half, which is
the half that matters for T-f ("in one class, a person-side function calls a resolver-side one
with no import to scan").
"""
