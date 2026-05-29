"""
m2_attribute_pool_builder.py -- Module 2 of the v32 combat-balance sim (attribute -> pool builder).

Builds the dice pools and derived resources that Module 1's engine consumes, from
a character's attributes and weapon History:
  - Combat Pool  (params/core.md, doubled formula)
  - Max Wounds, Wound Interval, Health  (derived_stats_v30, authoritative)
  - Stamina, Composure, Concentration   (derived_stats_v30)
Plus archetype stat blocks (Fast/Strong/Tough/Balanced/Mighty/...) carried forward
from the prior balance harness as sim-inputs (NOT game-canon).

Constant provenance: tests/sim/v32-combat-balance/m2_verification_ledger.json
  Class A = canonical (params/core.md, derived_stats_v30.md).
  Class B = archetype stat blocks (sim-inputs from tests/sim/scripts/phase11_c4_v0.py).
"""
from dataclasses import dataclass

# ===== canonical attribute + derived-value constants =====
ATTR_AVG = 3                    # [canonical: params/core.md §Attributes (average human; range 1-7)]
COMBAT_POOL_AGI_MULT = 2        # [canonical: params/core.md §Derived Scores (Agility x2)]
COMBAT_POOL_HISTORY_BASE = 3    # [canonical: params/core.md §Derived Scores (History points + 3)]
COMBAT_POOL_FLOOR = 5           # [canonical: derived_stats_v30 §4.1 (Combat Pool floor 5) / params/core.md min 5]
MAXWOUNDS_END_DIV = 2           # [canonical: derived_stats_v30 §4.1 (floor(End/2))]
MAXWOUNDS_BASE = 1              # [canonical: derived_stats_v30 §4.1 (+1)]
MAXWOUNDS_CAP = 3               # [canonical: derived_stats_v30 §4.1 (cap 3, PP-717)]
WOUND_INTERVAL_BASE = 6         # [canonical: derived_stats_v30 §4.1 (WI = End + 6)]
STAMINA_MULT = 5                # [canonical: derived_stats_v30 §4.2 (End x5)]
COMPOSURE_MULT = 3              # [canonical: derived_stats_v30 §5.1 (Charisma x3)]
CONCENTRATION_MULT = 3          # [canonical: derived_stats_v30 §5.2 (Focus x3)]


@dataclass
class StatBlock:
    """A character's attributes plus weapon loadout for the pool builder.
    Attributes not explicitly set default to the average-human value."""
    agi: int = ATTR_AVG
    end: int = ATTR_AVG
    strength: int = ATTR_AVG
    focus: int = ATTR_AVG
    charisma: int = ATTR_AVG
    attunement: int = ATTR_AVG
    weapon: str = "light_blade"
    history: int = 2            # weapon History points
    name: str = ""


def combat_pool(agi, history):
    """Combat Pool (params/core.md, doubled formula):
    (Agi x mult) + History points + base, floored at the Combat Pool floor."""
    return max(COMBAT_POOL_FLOOR, agi * COMBAT_POOL_AGI_MULT + history + COMBAT_POOL_HISTORY_BASE)


def max_wounds(end):
    """Max Wounds (derived_stats_v30, authoritative): min(floor(End / div) + base, cap)."""
    return min(end // MAXWOUNDS_END_DIV + MAXWOUNDS_BASE, MAXWOUNDS_CAP)


def wound_interval(end):
    """Wound Interval (derived_stats_v30, authoritative): End + base."""
    return end + WOUND_INTERVAL_BASE


def health(end):
    """Health (derived_stats_v30, authoritative): WI x (MaxWounds + 1)."""
    return wound_interval(end) * (max_wounds(end) + 1)


def stamina(end):
    """Stamina (derived_stats_v30): End x mult."""
    return end * STAMINA_MULT


def composure(charisma):
    """Composure (derived_stats_v30): Charisma x mult."""
    return charisma * COMPOSURE_MULT


def concentration(focus):
    """Concentration (derived_stats_v30): Focus x mult."""
    return focus * CONCENTRATION_MULT


def wound_adjusted_pool(base_pool, wounds):
    """Apply the universal wound penalty: minus 1D per wound (no Ob penalty),
    floored at the Combat Pool floor (derived_stats_v30, universal wound rule)."""
    return max(COMBAT_POOL_FLOOR, base_pool - wounds)


def build_pools(sb):
    """Derive every pool/resource for a StatBlock. Returns a dict."""
    return {
        "combat_pool": combat_pool(sb.agi, sb.history),
        "max_wounds": max_wounds(sb.end),
        "wound_interval": wound_interval(sb.end),
        "health": health(sb.end),
        "stamina": stamina(sb.end),
        "composure": composure(sb.charisma),
        "concentration": concentration(sb.focus),
    }


# ===== Archetype stat blocks =====
# Sim-inputs carried forward from the prior balance harness (tests/sim/scripts/phase11_c4_v0.py).
# Attribute values are sim constructs, NOT game-canon. Attributes the prior harness did not set
# (focus, charisma) default to average-human via StatBlock. These feed the Module 8 archetype sweep.
ARCHETYPES = {
    "Fast":         StatBlock(name="Fast",         agi=6, end=4, strength=4, weapon="light_blade",  attunement=5),  # [canonical: tests/sim/scripts/phase11_c4_v0.py build('Fast',6,4,4,light,attn=5) -- sim-input]
    "Strong":       StatBlock(name="Strong",       agi=3, end=4, strength=4, weapon="light_blade",  attunement=3),  # [canonical: tests/sim/scripts/phase11_c4_v0.py build('Strong',3,4,4,light,attn=3) -- sim-input]
    "Tough":        StatBlock(name="Tough",        agi=3, end=6, strength=4, weapon="light_blade",  attunement=3),  # [canonical: tests/sim/scripts/phase11_c4_v0.py build('Tough',3,6,4,light,attn=3) -- sim-input]
    "Tough-heavy":  StatBlock(name="Tough-heavy",  agi=3, end=6, strength=6, weapon="heavy_weapon", attunement=3),  # [canonical: tests/sim/scripts/phase11_c4_v0.py build('Tough-h',3,6,6,heavy,attn=3) -- sim-input]
    "Titan":        StatBlock(name="Titan",        agi=3, end=6, strength=7, weapon="heavy_weapon", attunement=3),  # [canonical: tests/sim/scripts/phase11_c4_v0.py build('Titan',3,6,7,heavy,attn=3) -- sim-input]
    "Mighty-heavy": StatBlock(name="Mighty-heavy", agi=3, end=4, strength=7, weapon="heavy_weapon", attunement=3),  # [canonical: tests/sim/scripts/phase11_c4_v0.py build('Mighty-h',3,4,7,heavy,attn=3) -- sim-input]
    "Mighty-light": StatBlock(name="Mighty-light", agi=3, end=4, strength=7, weapon="light_blade",  attunement=3),  # [canonical: tests/sim/scripts/phase11_c4_v0.py build('Mighty-l',3,4,7,light,attn=3) -- sim-input]
    "Polearm":      StatBlock(name="Polearm",      agi=3, end=5, strength=5, weapon="polearm",      attunement=3),  # [canonical: tests/sim/scripts/phase11_c4_v0.py build('Polearm',3,5,5,polearm,attn=3) -- sim-input]
    "Init-build":   StatBlock(name="Init-build",   agi=3, end=5, strength=4, weapon="light_blade",  attunement=8),  # [canonical: tests/sim/scripts/phase11_c4_v0.py build('Init-build',3,5,4,light,attn=8) -- sim-input]
    "Balanced":     StatBlock(name="Balanced",     agi=5, end=4, strength=5, weapon="light_blade",  attunement=5),  # [canonical: tests/sim/scripts/phase11_c4_v0.py build('Balanced',5,4,5,light,attn=5) -- sim-input]
}


# ============================== self-test ==============================
if __name__ == "__main__":
    checks = []
    rule = "================================================================"
    print("Module 2 (attribute -> pool builder) -- validation against canon")
    print(rule)

    # (a) Health / Max Wounds / Wound Interval vs the derived_stats per-Endurance table
    HEALTH_TABLE = {1: 14, 2: 24, 3: 27, 4: 40, 5: 44, 6: 48, 7: 52}  # [canonical: derived_stats_v30 §4.1 per-Endurance reference table]
    MW_TABLE     = {1: 1, 2: 2, 3: 2, 4: 3, 5: 3, 6: 3, 7: 3}         # [canonical: derived_stats_v30 §4.1 per-Endurance reference table]
    WI_TABLE     = {1: 7, 2: 8, 3: 9, 4: 10, 5: 11, 6: 12, 7: 13}     # [canonical: derived_stats_v30 §4.1 per-Endurance reference table]
    print("\n(a) Health / Max Wounds / Wound Interval vs derived_stats per-Endurance table:")
    a_ok = True
    for end in HEALTH_TABLE:
        row = (health(end) == HEALTH_TABLE[end]) and (max_wounds(end) == MW_TABLE[end]) and (wound_interval(end) == WI_TABLE[end])
        a_ok = a_ok and row
        print(f"    End {end}: Health {health(end):>2} (canon {HEALTH_TABLE[end]:>2})  MW {max_wounds(end)} (canon {MW_TABLE[end]})  WI {wound_interval(end):>2} (canon {WI_TABLE[end]:>2})  {'OK' if row else 'FAIL'}")
    checks.append(a_ok)

    # (b) Stamina / Composure / Concentration vs canonical anchors (range endpoints + worked example)
    STAMINA_ANCHORS = {1: 5, 4: 20, 7: 35}        # [canonical: derived_stats_v30 §4.2 (End x5; range 5-35; "End 4: Stamina 20")]
    COMPOSURE_ANCHORS = {1: 3, 4: 12, 7: 21}      # [canonical: derived_stats_v30 §5.1 (Charisma x3; range 3-21)]
    CONCENTRATION_ANCHORS = {1: 3, 4: 12, 7: 21}  # [canonical: derived_stats_v30 §5.2 (Focus x3; range 3-21)]
    b_ok = (all(stamina(k) == v for k, v in STAMINA_ANCHORS.items())
            and all(composure(k) == v for k, v in COMPOSURE_ANCHORS.items())
            and all(concentration(k) == v for k, v in CONCENTRATION_ANCHORS.items()))
    checks.append(b_ok)
    print(f"\n(b) End4->Stamina {stamina(4)} (canon 20); Cha4->Composure {composure(4)} (canon 12); Foc4->Concentration {concentration(4)} (canon 12); ranges checked  {'OK' if b_ok else 'FAIL'}")

    # (c) Combat Pool (doubled formula) + floor
    POOL_ANCHORS = {(4, 1): 12, (6, 2): 17, (3, 2): 11}   # [canonical: params/core.md §Derived Scores (Agi x2)+Hist+3; Alice Agi4/Hist1->12 per coverage_matrix]
    c_ok = all(combat_pool(a, hh) == v for (a, hh), v in POOL_ANCHORS.items())
    floor_ok = combat_pool(1, 0) == COMBAT_POOL_FLOOR     # min pool clamps to the floor
    c_ok = c_ok and floor_ok
    checks.append(c_ok)
    print(f"\n(c) Agi4/H1->{combat_pool(4,1)} (canon 12); Agi6/H2->{combat_pool(6,2)} (canon 17); floor Agi1/H0->{combat_pool(1,0)} (canon 5)  {'OK' if c_ok else 'FAIL'}")

    # (d) wound penalty: -1D per wound, floored at the Combat Pool floor
    fast_pool = combat_pool(ARCHETYPES["Fast"].agi, ARCHETYPES["Fast"].history)
    d_ok = (wound_adjusted_pool(fast_pool, 0) == fast_pool
            and wound_adjusted_pool(fast_pool, 3) == fast_pool - 3        # [canonical: derived_stats_v30 §4.1 (-1D per wound)]
            and wound_adjusted_pool(COMBAT_POOL_FLOOR, 9) == COMBAT_POOL_FLOOR)  # [canonical: derived_stats_v30 §4.1 (Combat Pool floor 5)]
    checks.append(d_ok)
    print(f"\n(d) Fast Combat Pool {fast_pool}; minus 3 wounds -> {wound_adjusted_pool(fast_pool,3)}; deep-wound floor clamp -> {wound_adjusted_pool(COMBAT_POOL_FLOOR,9)} (canon 5)  {'OK' if d_ok else 'FAIL'}")

    # archetype pool summary (illustrative)
    print("\n(archetype Combat Pools, doubled formula, History 2):")
    for nm, sb in ARCHETYPES.items():
        print(f"    {nm:<13} Agi {sb.agi} -> Combat Pool {combat_pool(sb.agi, sb.history):>2} | Health {health(sb.end):>2} | Stamina {stamina(sb.end):>2}")

    print("\n" + rule)
    bad = [i for i, c in enumerate(checks) if not c]
    if bad:
        print(f"RESULT: FAIL -- check indices failing: {bad}")
        raise SystemExit(1)
    print(f"RESULT: PASS -- all {len(checks)} checks match canon "
          f"(per-Endurance Health/MW/WI table, Stamina/Composure/Concentration, Combat Pool + floor, wound penalty).")
