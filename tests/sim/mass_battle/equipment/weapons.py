"""mass_battle.equipment.weapons — the WEAPONS module: a standalone, adaptable weapon catalogue.

Separated out of the troop taxonomy (Jordan 2026-06-30): a troop type NAMES a weapon; it no longer
embeds weapon facts. Splitting weapons into their own module lets the weapon model evolve on its own and
later be re-mapped onto the scene-combat (personal) weapon model — which already decomposes a weapon into
physical primitives (mass, head geometry, reach) in designs/scene/combat_engine_v1/weapons.py — without
disturbing troop_types.

This seed is DELIBERATELY light. It holds only the descriptive axes the board-game troop table already
uses (mass_battle_v30 §B.2 — a damage TYPE and a WEIGHT class, plus melee/ranged reach and keywords),
marked PROVISIONAL. It does NOT yet derive anything from physical primitives (mass_kg, reach_m,
percussion, armour-defeat mode) — that grounding and the cross-scale mapping are still being worked out;
when they land they slot into these OPEN records (just add fields) without a schema migration and without
touching the resolver.

DYNAMIC: register / override / extend ARSENAL at import or runtime. ADAPTABLE: records are open;
`.variant()` spins regional/quality variants off a base. No engine import, no resolution logic — a data
surface. NOT YET WIRED into resolution, so importing this changes no engine behaviour (byte-exact).
[provisional source: mass_battle_v30.md §B.2 — TTRPG Weapon column + Anti-Armour / Volley keywords]
"""
from mass_battle.equipment._base import Registry

# Descriptive vocabulary (intentionally aligned in SPIRIT with the personal-combat head/material model so
# the future mapping is short, but kept as plain provisional tags — no cross-engine binding yet):
DAMAGE_TYPES = ("cut", "blunt", "pierce")   # personal combat: head -> {shear, percussion, puncture}
WEIGHT_CLASSES = ("light", "heavy")          # personal combat: a continuous mass/heft; here a 2-band tag
REACHES = ("melee", "ranged")

ARSENAL = Registry("weapon")


def _seed():
    """Provisional §B.2 catalogue: each weapon class as (damage_type, weight, reach) + keywords. No
    numeric magnitudes are asserted here — the per-unit damage modifier in §B.2 is a TROOP-level
    composite (it varies by unit, not by weapon alone), so it stays out of the weapon record until the
    grounded derivation exists. `provisional=True` flags every seeded entry as not-yet-grounded."""
    R = ARSENAL.register
    R("light_cut",  damage_type="cut",   weight="light", reach="melee",  keywords=(),                          provisional=True)
    R("heavy_cut",  damage_type="cut",   weight="heavy", reach="melee",  keywords=(),                          provisional=True)
    R("heavy_blunt",damage_type="blunt", weight="heavy", reach="melee",  keywords=("anti_armour",),            provisional=True)  # §B.2 Anti-Armour keyword
    R("pike",       damage_type="pierce",weight="heavy", reach="melee",  keywords=("pole", "anti_cavalry"),    provisional=True)  # [v2 Stage E, ED-MB-0014 / P-DEC-1] the pike: a pole weapon, longest melee reach (0.3, TROOP_TYPE_REACH)
    R("bow",        damage_type="pierce",weight="light", reach="ranged", keywords=("volley",),                 provisional=True)
    R("crossbow",   damage_type="pierce",weight="light", reach="ranged", keywords=("volley", "armour_piercing"),provisional=True)  # §B.2 +1 vs med/heavy post-DR
    R("sling",      damage_type="blunt", weight="light", reach="ranged", keywords=("volley",),                 provisional=True)
    R("siege",      damage_type="blunt", weight="heavy", reach="ranged", keywords=("volley", "anti_armour"),   provisional=True)  # §B.2 HBl (siege), Artillery


_seed()


# ── convenience selectors (relative queries over the catalogue, not hard-coded lists) ──
def get(name, default=None):
    return ARSENAL.get(name, default)

def melee():
    return ARSENAL.where(reach="melee")

def ranged():
    return ARSENAL.where(reach="ranged")

def with_keyword(keyword):
    return [w for w in ARSENAL if keyword in (w.get("keywords") or ())]


if __name__ == "__main__":
    print(f"weapons: {len(ARSENAL)} entries")
    for w in ARSENAL:
        print(" ", repr(w))
    print("ranged:", [w.name for w in ranged()])
    print("anti_armour:", [w.name for w in with_keyword("anti_armour")])
