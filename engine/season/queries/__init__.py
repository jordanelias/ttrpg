"""`season.queries` — the ownerless functions. Nothing here owns state and nothing here writes.

  * `world_q`  -- the eleven World-FIRST functions, plus `questions_for` and `occasioned_by`.
  * `readers`  -- `WorldReader` / `LedgerReader`, the two sources the `requires` grammar reads.

`04_CODE_ARCHITECTURE.md` §A.2: *"queries/ ownerless functions: world_q (World first) · person_q
(asker first) · cache (barrier-built)"*, and the table below it gives every function here the
token column `—`: **no function in this package takes a write token, so none of them can write.**
`person_q` does not exist yet — the four person-side statics are still on `shape.Query` and go to
`decision` at step 7 — and `cache` is the barrier index work, which has no owner yet either.

⚠ THIS FILE IMPORTS NEITHER MODULE, for the reason `season/state/__init__.py` and
`season/data/__init__.py` both record at length: an eager package import makes anything that wants
one name pay for every registry the other module loads, and it silently removes the loaders' last
external patch point. `readers` imports `world_q`; nothing imports `readers`.
"""
