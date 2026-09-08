"""`season.queries` — the ownerless functions. Nothing here owns state and nothing here writes.

  * `world_q`  -- the eleven World-FIRST functions, plus `questions_for` and `occasioned_by`.
  * `readers`  -- `WorldReader` / `LedgerReader`, the two sources the `requires` grammar reads.

`04_CODE_ARCHITECTURE.md` §A.2: *"queries/ ownerless functions: world_q (World first) · person_q
(asker first) · cache (barrier-built)"*, and the table below it gives every function here the
token column `—`: **no function in this package takes a write token, so none of them can write.**
`person_q` does not exist yet — the four person-side statics are still on `shape.Query` and go to
`decision` at step 7 — and `cache` is the barrier index work, which has no owner yet either.

⚠ `readers` IS A FOURTH MODULE IN A PACKAGE §A.2 GIVES THREE, AND THAT IS DELIBERATE RATHER THAN
AN OVERSIGHT — recorded because the first version of this docstring quoted the three-module
roster and did not notice it was describing four files. The two readers are not a `Query`
family: they are what the `requires` GRAMMAR asks its questions through, and the grammar's own
module may not hold them (step 3's adjudication — it would give the grammar an opinion about
where its answers come from). By source they would split `WorldReader` → `world_q` and
`LedgerReader` → `person_q`; `person_q` does not exist until step 7, and filing `LedgerReader`
in `world_q` in the meantime would put an asker-scoped reader that takes NO `World` inside the
World-first module. So they sit together until step 7 can split them by their sources, and
whether §A.2's roster then absorbs them is a Layer-1 call for that step, not this one.

⚠ THIS FILE IMPORTS NEITHER MODULE, for the reason `season/state/__init__.py` and
`season/data/__init__.py` both record at length: an eager package import makes anything that wants
one name pay for every registry the other module loads, and it silently removes the loaders' last
external patch point. `readers` imports `world_q`; no module in this package imports `readers` — `shape.py` does, to
re-export it, and stating it flatly as "nothing imports `readers`" was wrong.
"""
