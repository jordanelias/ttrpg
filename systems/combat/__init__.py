"""systems/combat/ — personal-combat subsystem (PC lane; ED-900/904).

What remains here: combat_engine_v1/ (capabilities.py, state_graph.py and workbench/, a NON-package
scripts dir). The v30 oracle `sim/combat.py` was deleted at plan position PC-12 (FORK: row in
references/restructure_ledger.md). The resolver itself — core, wrapper,
combatant, config, weapons and the rest of the flat modules — moved to modules/combat/ at plan
position `31b`. The rest of the scene split (ED-IN-0071 P4) is history: the design documents are
quarantined under .designs/, and combat_engine_v1/systems.py was renamed combat_systems.py to
retire the `import systems` collision with this top-level package.
"""
