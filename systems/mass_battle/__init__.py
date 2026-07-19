"""systems/mass_battle/ — mass-battle subsystem (MB lane). Provincial split part 1
(ED-IN-0071 P4): the mass_battle_v30/mass_battle_integration_v30/military_layer_v30 docs
from designs/provincial/ + the massbattle/units/tactic_cards/altonian_reinforcements sim
from sim/provincial/. sim imports as systems.mass_battle.sim.* (was sim.provincial.*).
faction_action (FA lane, still in sim/provincial) lazy-imports massbattle across the lane
boundary until the factions slice.
"""
