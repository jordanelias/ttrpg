"""THE COMBAT ATTRIBUTE SPEC (PC-14) -- the one owner of which attributes a `Combatant` carries.

A leaf: imports only the standard library. Each entry holds COMBAT FACTS ONLY:

  key          : the engine's own attribute key (`c.agi`, `c.attrs['agi']`).
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
scale (`balance_eff - 3`, `reflex - 3`, `conc/5 - 3`, `Ob = score/2`, `pool = score + 6`).

INTERIM HOMES. `disp` carries `registry_key: None`: this spec is its only home until the registry or the
season's carrier (`Person.attributes`, CR-20) names a key for it; that commit sets the entry's `registry_key` in
the same change. `att` is Perception (ED-IN-0347) and is the whole of the read (PC-18 (1)); Reason (`attr.mind.acuity`) has no combat
role, so an authored acuity does not reach a `Combatant`. (the revert marker is on `combat_systems.reading`).

NOT AN ATTRIBUTE: the party's SKILL SCORE for the verb that opened the fight (A-98: a skill score is not an attribute; `IS-PC-05`,
A-112). It is the skill table's number (`engine/season/seam/wrappers/pool.py::score`, passed in `PersonalCombatInput.scores`) and
lives on the `Combatant` as `c.score` (`combatant.py`), not here. It is read in exactly two places, the pool (`core.resolution_pool`,
with the party's `pool_addends`) and the Ob the opponent rolls against (`core.ob_from_defender`).
"""
from collections import namedtuple

IN_FLUX = 'IN_FLUX'

AttributeSpec = namedtuple('AttributeSpec', 'key default neutral registry_key status')

SPEC = (
    AttributeSpec('strength', 4, 4, 'attr.body.strength', IN_FLUX),   # neutral 4: PC-20 (4)'s arrest term centres on it
    AttributeSpec('agi', 4, 4, 'attr.body.agility', IN_FLUX),
    AttributeSpec('end', 4, None, 'attr.body.endurance', IN_FLUX),
    AttributeSpec('att', 3, None, 'attr.mind.perception', IN_FLUX),
    AttributeSpec('spirit', 3, 4, 'attr.spirit.will', IN_FLUX),   # neutral 4: B15.10's yield roll counts Spirit in whole steps from the 1-7 scale's mid-point (`wrapper._spirit_levels`), as Strength and Coordination centre on it
    AttributeSpec('focus', 3, 3, 'attr.mind.focus', IN_FLUX),
    AttributeSpec('disp', 4, 4, None, IN_FLUX),
)

KEYS = tuple(s.key for s in SPEC)
DEFAULT = {s.key: s.default for s in SPEC}
NEUTRAL = {s.key: s.neutral for s in SPEC if s.neutral is not None}

assert len(set(KEYS)) == len(KEYS), f"attribute spec repeats a key: {KEYS}"
