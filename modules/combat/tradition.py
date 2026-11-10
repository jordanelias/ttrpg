"""tradition.py — the tradition facade (re-export): the four names callers reach as `TR.<name>`.

  · traditions.py        — the traditions ROSTER and `familiarity`
  · ability_primitives.py — the ABILITY PRIMITIVES (the atoms a tradition is built from + the equip modulators)

`wrapper` passes this module to `combat_systems` as the parameter `TR`, which reads `TR.eff_cw`, `TR.ability_factor`,
`TR.ability_bonus` and `TR.familiarity`; anything else is imported from its owner. A tradition is a COGNITIVE MODE (a way
of reading the same shared physics), NOT a separate rule-set; differentiation is bottom-up only — learned abilities +
familiarity.
"""

from traditions import familiarity  # noqa: F401
from ability_primitives import ability_bonus, ability_factor, eff_cw  # noqa: F401
