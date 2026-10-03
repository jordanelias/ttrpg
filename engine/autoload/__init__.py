"""
engine.autoload — the DICE ENGINE: the d10 chain, degree_from_net and sigma leverage, which the host and
every system read. It is not "the engine" (that is the season loop, engine/season/).
The package holds exactly three files: __init__.py, dice_engine.py, sigma_leverage.py.
⚠ NOT a Godot autoload and never to become one — the port's [autoload] table holds no simulation state or
service (architecture/holonic_ARCHITECTURE.md §47). The name is a 2026-05 stub label; the package is
renamed engine/dice_engine/ at plan position `34` (workplans/valoria_master_workplan_v8_part5.md §SM),
which changes every importer.

Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17]

Modules:
  - dice_engine: d10 chain rule, TN values, degree of success
  - sigma_leverage: continuous sigma-leverage resolution
  (game_state, the global mutable state container, was deleted at plan position `29b`, 2026-10-01: the
   season's World is engine/season/state/world.py and its realm is harness/populated.build_realm.)
  (season_manager, scene_slate, npc_ai, victory and engine_clock were deleted at plan position
   `28-iii`, 2026-10-01; the season loop is engine/season/loop/.)
"""
