"""systems/combat/ — personal-combat subsystem (PC lane; ED-900/904).

Scene split (ED-IN-0071 P4): the combat_* design docs + the combat_engine_v1/ resolver
(a scripts-on-path oracle dir, moved wholesale at identical depth) + scene_combat_v1/
(ED-911 envelope) from designs/scene/ + the DEPRECATED sim/personal/combat.py -> sim/.
combat_engine_v1/systems.py was renamed combat_systems.py to retire the `import systems`
collision with this top-level package. sim/combat.py imports as systems.combat.sim.combat.
combat_engine_v1/ stays a NON-package scripts dir (bare sibling imports on sys.path).
"""
