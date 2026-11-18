"""
engine.dice_engine — the DICE ENGINE: the d10 chain, degree_from_net and sigma leverage, which the host and
every system read. It is not "the engine" (that is the season loop, engine/season/).
The package holds exactly three files: __init__.py, dice_engine.py, sigma_leverage.py.
⚠ NOT a Godot autoload and never to become one — the port's [autoload] table holds no simulation state or
service (architecture/holonic_ARCHITECTURE.md §47).

Status: the ruled owner of the d10 chain, the one sampler and the degree ladder; not a provisional stub. The code is the mechanism, this text is reference.

Modules:
  - dice_engine: d10 chain rule, TN values, degree of success
  - sigma_leverage: continuous sigma-leverage resolution
  (the season's World is engine/season/state/world.py, its realm is built by
   engine/season/boot/realm.py::build_realm, and the season loop is engine/season/loop/.)
"""
