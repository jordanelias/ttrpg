"""mass_battle.equipment.armour — the ARMOUR module: a standalone, adaptable armour catalogue.

Separated out of the troop taxonomy (Jordan 2026-06-30): a troop type NAMES an armour; it no longer
embeds armour facts. A dedicated module lets the armour model evolve on its own and later be re-mapped
onto the scene-combat (personal) armour model — which routes damage through a tier->material->coverage
chain (designs/scene/combat_engine_v1/core.py TIER2MAT none/cloth/mail/plate) — without disturbing
troop_types.

This seed is DELIBERATELY light. The only NUMERIC axis is DR-vs-Piercing, which is a CANONICAL value (the
Ranged DR table), not an assertion. `material` and any future axis (mass_kg for the load/locomotion
model, coverage, per-damage-type DR) are PROVISIONAL placeholders; the physical grounding and the
cross-scale mapping are still being worked out and slot into these OPEN records without a schema
migration.

DYNAMIC: register / override / extend ARMOURY at import or runtime. ADAPTABLE: records are open;
`.variant()` spins regional/quality variants off a base. No engine import, no resolution logic — a data
surface. NOT YET WIRED into resolution (the engine still computes DR the old way), so importing this
changes no engine behaviour (byte-exact).
[canonical: params/mass_combat.md §Ranged DR Table — None=0 / Light=1 / Medium=2 / Heavy=3 vs Piercing]
[provisional source: mass_battle_v30.md §B.2 — TTRPG Armour column]
"""
from mass_battle.equipment._base import Registry

# Descriptive vocabulary. `tier` is the §B.2 armour class; `material` mirrors the personal-combat
# tier->material mapping in SPIRIT (so the future cross-scale bridge is short) but is a provisional tag,
# not a binding to that engine yet.
TIERS = ("none", "light", "medium", "heavy")

ARMOURY = Registry("armour")


def _seed():
    """Provisional §B.2 catalogue: each armour class with its CANONICAL DR-vs-Piercing and a provisional
    descriptive material. dr_vs_piercing is the only asserted number and it is canonical (Ranged DR
    table); everything else is a placeholder for the grounding pass."""
    R = ARMOURY.register
    R("none",   tier="none",   material="none",  dr_vs_piercing=0, provisional=True)  # [canonical: params/mass_combat.md §Ranged DR Table — None=0 vs Piercing]
    R("light",  tier="light",  material="cloth", dr_vs_piercing=1, provisional=True)  # [canonical: params/mass_combat.md §Ranged DR Table — Light=1 vs Piercing]
    R("medium", tier="medium", material="mail",  dr_vs_piercing=2, provisional=True)  # [canonical: params/mass_combat.md §Ranged DR Table — Medium=2 vs Piercing]
    R("heavy",  tier="heavy",  material="plate", dr_vs_piercing=3, provisional=True)  # [canonical: params/mass_combat.md §Ranged DR Table — Heavy=3 vs Piercing]


_seed()


# ── convenience selectors ──
def get(name, default=None):
    return ARMOURY.get(name, default)

def dr_vs_piercing(name, default=0):
    """Canonical ranged DR for an armour class (0 if unknown). The only currently-grounded armour number."""
    rec = ARMOURY.get(name)
    return rec.get("dr_vs_piercing", default) if rec is not None else default

def tiers():
    return [a.name for a in ARMOURY]


if __name__ == "__main__":
    print(f"armour: {len(ARMOURY)} entries")
    for a in ARMOURY:
        print(" ", repr(a))
    print("dr vs piercing (heavy):", dr_vs_piercing("heavy"))
