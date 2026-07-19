"""mass_battle.equipment — standalone, adaptable WEAPON and ARMOUR modules.

Split out of troop_types per Jordan's directive (2026-06-30): "armour and weapons ... should be their own
modules so that they can be cleanly adjusted to map better onto scene combat if it changes." A troop type
NAMES a weapon and an armour from these catalogues; it no longer embeds equipment facts. The catalogues
are DYNAMIC (register/override at runtime) and ADAPTABLE (open records — add fields as the model grows),
so the eventual primitive grounding + the cross-scale (mass <-> personal) mapping can land here without a
schema migration and without touching the troop taxonomy.

NOT YET WIRED into resolution (the engine still reads DR/speed the old way). This is a data surface the
movement / behaviour / tactics work will read from once the grounding is settled. Importing it changes no
engine behaviour (byte-exact)."""
from mass_battle.equipment import weapons, armour
from mass_battle.equipment.weapons import ARSENAL
from mass_battle.equipment.armour import ARMOURY

# Provisional troop -> (weapon, armour) loadout, transcribed from mass_battle_v30 §B.2. INERT (nothing
# consumes it yet) and intentionally a thin NAMED association, NOT a derivation: the primitive mapping
# (weapon/armour physics -> speed / DR / lethality) is still being worked out. A troop type is thus a
# "dictionary definition" that points at equipment entries — the decoupling this split enables.
TROOP_LOADOUT = {
    "levy":             ("light_cut",   "none"),
    "light_infantry":   ("light_cut",   "light"),
    "heavy_infantry":   ("heavy_cut",   "medium"),
    "cavalry":          ("heavy_cut",   "heavy"),
    "archers":          ("bow",         "light"),
    "crossbow":         ("crossbow",    "light"),
    "sling":            ("sling",       "light"),
    "artillery":        ("siege",       "none"),
    "knights_templar":  ("heavy_blunt", "heavy"),
    # [ED-MB-0001, gate 2] mounted_archers isn't a §B.2 troop type -- added by ED-1095/T4 (Jordan
    # 2026-07-02) with no loadout entry yet. Same weapon as archers (a bow), light armour to keep
    # it mobile -- the whole point of the troop type is speed + range, not endurance.
    "mounted_archers":  ("bow",         "light"),
}


def loadout_for(troop_type):
    """(weapon_record, armour_record) a troop type carries, or (None, None) if unknown. Provisional —
    a NAMED lookup over the two catalogues, not a derivation."""
    pair = TROOP_LOADOUT.get(str(troop_type).strip().lower()) if troop_type else None
    if not pair:
        return (None, None)
    w, a = pair
    return (ARSENAL.get(w), ARMOURY.get(a))


__all__ = ["weapons", "armour", "ARSENAL", "ARMOURY", "TROOP_LOADOUT", "loadout_for"]
