"""modules.mass_battle.equipment — standalone, adaptable WEAPON and ARMOUR modules.

Split out of troop_types per Jordan's directive (2026-06-30): "armour and weapons ... should be their own
modules so that they can be cleanly adjusted to map better onto scene combat if it changes." A troop type
NAMES a weapon and an armour from these catalogues; it no longer embeds equipment facts. The catalogues
are DYNAMIC (register/override at runtime) and ADAPTABLE (open records — add fields as the model grows),
so the eventual primitive grounding + the cross-scale (mass <-> personal) mapping can land here without a
schema migration and without touching the troop taxonomy.

This is a data surface: resolution does not read DR/speed from it. `troop_types.registry.unit_type_for`
reads a troop type's weapon `reach` ('melee'/'ranged') through `loadout_for`."""
from modules.mass_battle.equipment import weapons, armour
from modules.mass_battle.equipment.weapons import ARSENAL
from modules.mass_battle.equipment.armour import ARMOURY

from modules.mass_battle.troop_types import table as _table


def loadout_for(troop_type):
    """(weapon_record, armour_record) a troop type carries, or (None, None) if unknown. Provisional --
    a NAMED lookup over the two catalogues, not a derivation. [B17.10] The names are the troop file's `primary` and
    `armour` columns (`references/troops.yaml`, read by `troop_types/table.py::loadout_for_names`), transcribed from
    mass_battle_v30 §B.2; the old `TROOP_LOADOUT` table is deleted."""
    w, a = _table.loadout_for_names(troop_type)
    if w is None and a is None:
        return (None, None)
    return (ARSENAL.get(w), ARMOURY.get(a))


__all__ = ["weapons", "armour", "ARSENAL", "ARMOURY", "loadout_for"]
