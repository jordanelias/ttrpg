"""`season.queries` — the ownerless functions. Nothing here owns state and nothing here writes.

  * `world_q`   -- the World-FIRST functions, plus `WorldReader`.
  * `person_q`  -- the asker-first family: `entrenchment`, plus `LedgerReader`.
  * `cache`     -- the barrier indexes, single-owned.
  * `faction_q` -- `resolve, holdings, purview, subordinates, at_war, head`. §B.6.1's
    one constructor for the five-field governance VIEW plus the five Queries plan position
    `20-ii` (U9/R-04) completed, and §C.5.1's roster contract calls `resolve` by that dotted name;
    `04 §A.2:132` names the module. It also names `SHEET_KIND`, the `record_kinds` member a `survey`
    freezes one `Faction` into (plan position `20-iii`), and re-exports `at_war` and `WAR_MOOD`, the
    `Proposition.mood` value it reads, whose bodies live in `world_q` -- and refuses at import if
    `SHEET_KIND`'s roster row stops being `Faction`'s fields. No function here writes.
  * `inputs`    -- not a query module: the typed INPUT records the host builds for a module entry
    (A-25, plan positions `31a`, `31b`, `31c`) and one OUTPUT record, `Margin`, the social contest
    provider's module -> host return (v9 SC-01 step 15); a stdlib-only leaf a module may import. No
    function, no state.

`04_CODE_ARCHITECTURE.md` §A.2: *"queries/ ownerless functions: world_q (World first) · person_q
(asker first) · cache (barrier-built) · faction_q (§B.6.1's VIEW, §B.10-12's `resolve`/`at_war`)"*
-- FOUR members as of `20-ii`, and the table below it gives every function here the token column
`—`: **no function in this package takes a write token, so none of them can write.** The package is a
superset of the roster by exactly `inputs` (above), which holds records rather than functions.

⚠ **`faction_q` AND THE ENUMERATION.** `world_q.py`'s own docstring argues against a `polity_q.py`
"rather than left as a FOURTH module in a package the spec enumerates with three", and
`WorldReader`/`LedgerReader` live in `world_q`/`person_q` for the same reason. `faction_q` is
not that case: §B.6.1 and §C.5.1 name it by its own dotted path (`faction_q.resolve`), which
neither `WorldReader` nor a hypothetical `polity_q` was ever named as. The precedent is followed
where it applies (do not mint a module the spec never names) and distinguished where it does not
(do not fold code the spec explicitly names elsewhere into a module the spec does not name it in).

⚠ **`WorldReader` is in `world_q` and `LedgerReader` in `person_q`.** `WorldReader` takes a
`World` and asks it; `LedgerReader` takes claims and nothing else. **Splitting them by source is
what makes §A.3 row 2's property checkable** — with the person-side reader in `person_q`,
`test_person_q_cannot_reach_the_world_side` can assert by import that this half cannot reach the
other, which is the whole content of *"two modules; the second cannot import the first"* (T-f).

⚠ THIS FILE IMPORTS NONE OF ITS SUBMODULES, for the reason `season/state/__init__.py` and
`season/data/__init__.py` both record at length: an eager package import makes anything that wants
one name pay for every registry the other module loads, and it silently removes the loaders' last
external patch point. Within the package, `cache` imports `world_q` and `faction_q` imports
`world_q` (reusing `members()` rather than re-deriving membership, §8, and re-exporting `at_war`,
whose body moved to `world_q` so `open_referents` reads it with no edge back), and `world_q` imports
neither — all WORLD-FIRST modules reading another world-first
module, never the direction §A.3 row 2 forbids: `person_q` still
imports neither, and `test_person_q_cannot_reach_the_world_side` is what holds THAT half, which is
the half that matters for T-f ("in one class, a person-side function calls a resolver-side one
with no import to scan").
"""
