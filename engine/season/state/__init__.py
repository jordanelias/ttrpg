"""`season.state` -- the world-state package: what the world is made of, and what holds it.

  * `ids`      -- the mint (`H`) and its sentinel (`ROOT`).                      step 1
  * `carriers` -- THE PRIMITIVES: the sixteen things the world holds.            step 4

`world.py` -- the store and the gate on it -- is the second half of step 4 and lands next; the
carriers are separated first because the store imports them and nothing imports the store.

⚠ THIS FILE IMPORTS NEITHER OF THEM, AND THAT IS DELIBERATE -- the same finding
`season/data/__init__.py` records at length. Seven modules import `data.files` for PATHS ONLY, and
an eager package import made every one of them parse two YAML registries and become able to
`SystemExit` at import time. The arrow here is the same shape: `carriers` reads `data.rosters` and
`data.fixtures`, so importing `season.state` eagerly would load the registries for any module that
wanted only `H`.

The layering inside the package is one-way and checkable in one grep: `ids` imports nothing local,
`carriers` imports `data` and `gaps`. Nothing here imports `shape`, `queries`, `decision` or
`loop` -- a carrier may not know the store, and the store may not know what reads it.
"""
