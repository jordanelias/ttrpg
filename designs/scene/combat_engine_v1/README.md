# Combat Engine v1 (modular, multimodal, matrix-validated)

Personal-combat resolution engine. Modular wrapper (state graph + A/B identity) over a physical substrate; a
multimodal cross-tradition resolver (tradition.py) translates martial-tradition vocabularies into shared
primitives (measure / commitment-window / contact-as-information). Validated against the four-state weapon
matchup matrix (A0 unarmoured -> A3 full plate).

Files: core.py (canonical sigma-resolution + armour-aware damage), combatant.py (objects + weapon vectors incl.
lever-arm head/grip lengths + half-sword form), config.py (all tunables), systems.py (subsystems: reach, tempo,
leverage, armour-defeat, half-sword switch, etc.), tradition.py (cognitive-mode profiles + cross-tradition
familiarity), wrapper.py (engagement state machine: measure/approach/close, displacement, re-opening, bind,
feinting, 95% cap).

Status: CANONICAL — ratified by ED-900/904 and docket ED-1029 (the 2026-06-02 proposal is EXECUTED/HISTORICAL).
Godot port: shaped into the module architecture at designs/godot/skeleton/engines/combat/ + references/module_contracts.yaml
(personal_combat); the canonical resolution is d_sigma (sigma-leverage), additive-coupled damage, and ED-1041 bilateral-Ob
wounds — NOT the v30 model (Agi×2 pool / TN-7 / multiplicative STR) still found in deprecated sims.
