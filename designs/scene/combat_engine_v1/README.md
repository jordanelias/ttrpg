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

Status: canonical-candidate (ratification proposed; see designs/audit/2026-06-02-combat-engine/).
