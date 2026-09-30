"""`season.queries` — the ownerless functions. Nothing here owns state and nothing here writes.

  * `world_q`   -- the thirteen World-FIRST functions, plus `WorldReader`.
  * `person_q`  -- the asker-first family: `entrenchment`, plus `LedgerReader`.
  * `cache`     -- the barrier indexes, single-owned.
  * `faction_q` -- `resolve, holdings, purview, superiors, subordinates, at_war, head`. §B.6.1's
    one constructor for the five-field governance VIEW plus the five Queries plan position
    `20-ii` (U9/R-04) completed, and §C.5.1's roster contract calls `resolve` by that dotted name.
    See `faction_q.py`'s own docstring for the history of the ambiguity this WAS: from
    2026-09-03 to `20-ii`, §A.2:132's enumeration named three modules while §B.6.1/§C.5.1/§B.10-12
    -- all also ratified, all untouched -- already presupposed this module existed by its own
    dotted path (`layer-conformance` B4's third disposition: an internal spec ambiguity, not a
    spec/code one, so the repair was never "edit `04` to match code" -- `CLAUDE.md` §0.05: "a spec
    edited to match its implementation checks nothing"). **`20-ii` is what makes the module
    complete rather than partial, and `04 §A.2:132` is edited in the SAME commit, per the
    contradiction's own resolution** ("edit `04 §A.2:132` at `20-ii`, when the fourth module is
    complete -- not before"). It also names `SHEET_KIND`, the `record_kinds` member a `survey`
    freezes one `Faction` into (plan position `20-iii`), and `WAR_MOOD`, the `Proposition.mood`
    value `at_war` reads -- and refuses at import if `SHEET_KIND`'s roster row stops being
    `Faction`'s fields. Still no function here writes.

`04_CODE_ARCHITECTURE.md` §A.2: *"queries/ ownerless functions: world_q (World first) · person_q
(asker first) · cache (barrier-built) · faction_q (§B.6.1's VIEW, §B.10-12's `resolve`/`at_war`)"*
-- FOUR members as of `20-ii`, and the table below it gives every function here the token column
`—`: **no function in this package takes a write token, so none of them can write.** **All four
of the enumerated modules exist**, and the package is no longer a superset of the roster.

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
