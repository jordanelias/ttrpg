"""tradition.py — the tradition LAYER facade (re-export).

The tradition split lives in two modules now:
  · traditions.py        — the traditions DICTIONARY (aggregates + familiarity)
  · ability_primitives.py — the ABILITY PRIMITIVES (the atoms a tradition is built from + the equip modulators)

This facade re-exports both so `from . import tradition as TR; TR.eff_cw(...)/TR.familiarity(...)` call-sites work. A tradition is a COGNITIVE MODE (a way of reading the same shared physics), NOT a separate rule-set;
differentiation is bottom-up only — learned abilities + familiarity.
"""

from .traditions import (  # noqa: F401  the traditions dictionary
    TRADITIONS, FAMILIARITY_DEFAULT, FAMILIARITY_ADJACENT, ADJACENT,
    familiarity,
)
from .ability_primitives import (  # noqa: F401  the ability primitives + the tradition->ability bundle index
    ABILITIES, TRADITION_KIT, kit, ability_bonus, ability_factor, eff_cw,
)
