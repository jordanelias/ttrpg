"""THE COMBAT ATTRIBUTE SPEC (PC-14) -- the one owner of which attributes a `Combatant` carries.

A leaf: imports nothing. Each entry holds COMBAT FACTS ONLY:

  key          : the engine's own attribute key (`c.history`, `c.attrs['history']`).
  default      : the value a fighter built without that attribute carries.
  neutral      : the centring value a formula subtracts (`c.agi - NEUTRAL['agi']`), present only where a direct
                 centring literal exists in the engine; `None` where none does.
  registry_key : the `references/descriptor_registry.yaml: attributes` key this attribute reads as, or `None`
                 where the registry names none. It is a POINTER, not a copy: the registry owns the scale, the
                 names, the aliases, the floor and the ceiling, and none of them is written here (a copied name or
                 bound would be a second owner).
  status       : `IN_FLUX` for every entry (Jordan, 2026-11-01: "ensure all attributes including history are
                 stored in such a way where they can be modified in future as they are currently in flux").

ADDING an attribute is one entry here: `Combatant` generates its property, the workbench factories and the typed
export (`tools/export_engine_params.py`, section `attributes`) read this tuple. RENAMING is the entry's `key` plus
its readers. RE-VALUING is `Combatant.set_attr` (or `c.<key> = v`), which re-derives every derived figure.

NOT delivered, and said so: re-centring the derived quantities stays formula constants anchored on the default
scale (`balance_eff - 3`, `reflex - 3`, `conc/5 - 3`, `Ob = History/2`, `pool = History + 6`).

INTERIM HOMES. `history`, `disp` carry `registry_key: None`: this spec is their only home until the registry or the
season's carrier (`Person.attributes`, CR-20) names a key for one; that commit sets the entry's `registry_key` in
the same change. `history` is ELIMINATED as a rolled integer by ED-IN-0330; CR-85's build is its owner-to-be and
edits this entry. `cog` keeps `attr.mind.acuity` until PC-18 removes it. `att` is Perception (ED-IN-0347).
"""
from collections import namedtuple

IN_FLUX = 'IN_FLUX'

AttributeSpec = namedtuple('AttributeSpec', 'key default neutral registry_key status')

SPEC = (
    AttributeSpec('strength', 4, None, 'attr.body.strength', IN_FLUX),
    AttributeSpec('agi', 4, 4, 'attr.body.agility', IN_FLUX),
    AttributeSpec('end', 4, None, 'attr.body.endurance', IN_FLUX),
    AttributeSpec('cog', 3, None, 'attr.mind.acuity', IN_FLUX),
    AttributeSpec('att', 3, None, 'attr.mind.perception', IN_FLUX),
    AttributeSpec('spirit', 3, None, 'attr.mind.will', IN_FLUX),
    AttributeSpec('focus', 3, 3, 'attr.mind.focus', IN_FLUX),
    AttributeSpec('history', 3, 3, None, IN_FLUX),
    AttributeSpec('disp', 4, 4, None, IN_FLUX),
)

KEYS = tuple(s.key for s in SPEC)
DEFAULT = {s.key: s.default for s in SPEC}
NEUTRAL = {s.key: s.neutral for s in SPEC if s.neutral is not None}

assert len(set(KEYS)) == len(KEYS), f"attribute spec repeats a key: {KEYS}"
