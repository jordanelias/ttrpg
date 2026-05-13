"""
module_01_primitives.py — Settlement primitives for settlement_mgmt_stress_01

Mode G Module 1. Substrate that all later modules import: settlement type
enumeration, the §1.3 stat schema, the §2.1 registry (37 entries), and the
revised §1.3 province-Accord derivation.

Canonical sources (full read this session):
  designs/territory/settlement_layer_v30.md  §1.1, §1.2, §1.3, §2.1

Out of scope (deferred):
  - Per-settlement starting stat values — not in §1.3 or §2.1 (Finding F4).
  - Adjacency graph — Module 2.
  - Facility tiers / capacity pressure — Module 3.
  - Player action handlers (improve / maintain / problem-solve / standing /
    renown). Module 1 surfaces the mutable state these handlers will touch.

See module_01_report.md for findings F1–F4 (canonical inconsistencies
surfaced, not silently reconciled).
"""

from dataclasses import dataclass
from math import floor
from typing import Dict, Tuple

# ── Canonical scales ─────────────────────────────────────────────────────────

STAT_MIN = 0
# [canonical: designs/territory/settlement_layer_v30.md §1.3
#  "Each settlement has 3 stats tracked on a 0–5 scale"]
STAT_MAX = 5

# Canonical stat names per §1.3 (the three-stat schema is mechanical canon).
STAT_NAMES: Tuple[str, ...] = ('Prosperity', 'Defense', 'Order')

# Derived-value coefficients per §1.3 derived-values table.
# [canonical: designs/territory/settlement_layer_v30.md §1.3 derived-values table]
LOCAL_ECONOMY_PER_PROSPERITY = 50   # "Prosperity × 50"
GARRISON_PER_DEFENSE = 20           # "Defense × 20 + Fort Level × 30"
GARRISON_PER_FORT_LEVEL = 30        # same line as above
PUBLIC_ORDER_PER_ORDER = 20         # "Order × 20"


# ── Canonical settlement types from §1.2 ─────────────────────────────────────

# Types explicitly listed in §1.2 settlement-type table.
# [canonical: designs/territory/settlement_layer_v30.md §1.2 Settlement Types]
CANONICAL_TYPES: Tuple[str, ...] = (
    'Seat', 'City', 'Town', 'Fortress', 'Port', 'Cathedral', 'Mine', 'Outpost',
)

# Types that appear in §2.1 registry but NOT in §1.2 — surfaced as Finding F1.
EXTRA_TYPES_IN_REGISTRY: Tuple[str, ...] = (
    'Village', 'Fortress-City', 'Cathedral-City',
)

ALL_REGISTRY_TYPES: Tuple[str, ...] = CANONICAL_TYPES + EXTRA_TYPES_IN_REGISTRY


# ── Duchies and special-case sovereign entities ──────────────────────────────

# [canonical: designs/territory/settlement_layer_v30.md §2.1 — three Kingdom
#  duchies listed in section headers as "Valorsmark duchy", "Hafenmark duchy",
#  "Varfell duchy"]
KINGDOM_DUCHIES: Tuple[str, ...] = ('Valorsmark', 'Hafenmark', 'Varfell')

# Himmelenger and Schoenland are NOT duchies. Per §2.1: Himmelenger is a
# "sovereign ecclesiastical city-state", Schoenland is a "foreign Altonian
# island ... politically independent of the Kingdom". They appear as the
# settlement's `duchy` field for structural uniformity; downstream modules
# must check is_special_entity().
SPECIAL_ENTITIES: Tuple[str, ...] = ('Himmelenger', 'Schoenland')


# ── §2.1 Settlement Registry ─────────────────────────────────────────────────

@dataclass(frozen=True)
class Settlement:
    """A march-target settlement per §2.1. Immutable identity; mutable state
    (stats, controlling faction, events) tracked in companion structures by
    downstream modules."""
    id: str
    name: str
    type: str
    province: str
    duchy: str
    role: str


# Registry order matches §2.1 reading order.
# [canonical: designs/territory/settlement_layer_v30.md §2.1 Settlement Registry]
_REGISTRY_DATA: Tuple[Tuple[str, ...], ...] = (
    # Valorsmark duchy — Valorsplatz province
    ('S-001', 'Valorsplatz',         'Seat',           'Valorsplatz',  'Valorsmark',  'province_primary'),
    ('S-002', 'Auerheim',            'Town',           'Valorsplatz',  'Valorsmark',  'spoke'),
    ('S-003', 'Königsbrück',         'Town',           'Valorsplatz',  'Valorsmark',  'spoke'),
    # Kronmark province
    ('S-004', 'Kronmark',            'Town',           'Kronmark',     'Valorsmark',  'province_primary'),
    ('S-005', 'Saatfeld',            'Village',        'Kronmark',     'Valorsmark',  'spoke'),
    ('S-006', 'Goldenfurt',          'Town',           'Kronmark',     'Valorsmark',  'spoke'),
    # Lowenskyst province
    ('S-007', 'Lowenskyst Fortress', 'Fortress',       'Lowenskyst',   'Valorsmark',  'province_primary'),
    ('S-008', 'Tiefental',           'Village',        'Lowenskyst',   'Valorsmark',  'spoke'),
    # Feldmark province
    ('S-009', 'Feldmark',            'Town',           'Feldmark',     'Valorsmark',  'province_primary'),
    ('S-010', 'Erntehof',            'Village',        'Feldmark',     'Valorsmark',  'spoke'),
    ('S-011', 'Spelzdorf',           'Village',        'Feldmark',     'Valorsmark',  'spoke'),
    # Stillhelm province
    ('S-012', 'Stillhelm',           'Town',           'Stillhelm',    'Valorsmark',  'province_primary'),
    ('S-013', 'Aschenbach',          'Village',        'Stillhelm',    'Valorsmark',  'spoke'),
    # Ehrenfeld province
    ('S-014', 'Ehrenfeld',           'Fortress-City',  'Ehrenfeld',    'Valorsmark',  'province_primary'),
    ('S-015', 'Nordhain',            'Village',        'Ehrenfeld',    'Valorsmark',  'spoke'),
    # Hafenmark duchy — Rendstad province
    ('S-016', 'Rendstad',            'Town',           'Rendstad',     'Hafenmark',   'province_primary'),
    ('S-017', 'Holzbrück',           'Village',        'Rendstad',     'Hafenmark',   'spoke'),
    # Gransol province
    ('S-018', 'Gransol',             'City',           'Gransol',      'Hafenmark',   'province_primary'),
    ('S-019', 'Niedersol',           'Town',           'Gransol',      'Hafenmark',   'spoke'),
    ('S-020', 'Saltbrück',           'Town',           'Gransol',      'Hafenmark',   'spoke'),
    # Spartfell province
    ('S-021', 'Spartfell Fortress',  'Fortress',       'Spartfell',    'Hafenmark',   'province_primary'),
    ('S-022', 'Gelbgrund',           'Village',        'Spartfell',    'Hafenmark',   'spoke'),
    # Halvarshelm province — DISTINCT from Varfell's "Halvardshelm" (with 'd')
    ('S-023', 'Halvarshelm Town',    'Town',           'Halvarshelm',  'Hafenmark',   'province_primary'),
    ('S-024', 'Erzbach',             'Village',        'Halvarshelm',  'Hafenmark',   'spoke'),
    ('S-025', 'Schmiedhof',          'Village',        'Halvarshelm',  'Hafenmark',   'spoke'),
    # Varfell duchy — Grauwald province
    ('S-026', 'Grauwald',            'Town',           'Grauwald',     'Varfell',     'province_primary'),
    ('S-027', 'Skogheim',            'Village',        'Grauwald',     'Varfell',     'spoke'),
    # Halvardshelm province (Varfell; distinct from Hafenmark's Halvarshelm)
    ('S-028', 'Halvardshelm',        'Town',           'Halvardshelm', 'Varfell',     'province_primary'),
    ('S-029', 'Geirsvik',            'Village',        'Halvardshelm', 'Varfell',     'spoke'),
    ('S-030', 'Yrnastead',           'Village',        'Halvardshelm', 'Varfell',     'spoke'),
    # Sigurdshelm province
    ('S-031', 'Sigurdshelm',         'Seat',           'Sigurdshelm',  'Varfell',     'province_primary'),
    ('S-032', 'Brynjard',            'Town',           'Sigurdshelm',  'Varfell',     'spoke'),
    ('S-033', 'Sundfjord',           'Town',           'Sigurdshelm',  'Varfell',     'spoke'),
    # Oastad province
    ('S-034', 'Oastad',              'Town',           'Oastad',       'Varfell',     'province_primary'),
    ('S-035', 'Salgrund',            'Village',        'Oastad',       'Varfell',     'spoke'),
    # Himmelenger city-state — sovereign ecclesiastical entity
    ('S-036', 'Himmelenger',         'Cathedral-City', 'Himmelenger',  'Himmelenger', 'sovereign_city_state'),
    # Schoenland — foreign Altonian tributary
    ('S-037', 'Schoenland',          'City',           'Schoenland',   'Schoenland',  'foreign_tributary'),
)

REGISTRY: Tuple[Settlement, ...] = tuple(Settlement(*row) for row in _REGISTRY_DATA)


# ── Expected counts per §2.1 final summary line ──────────────────────────────
# [canonical: designs/territory/settlement_layer_v30.md §2.1 summary:
#  "Total: 37 march-target settlements (35 Kingdom + 1 Church city-state + 1
#  foreign tributary). Province distribution: Valorsmark 6 provinces (15
#  settlements), Hafenmark 4 provinces (10), Varfell 4 provinces (10)."]
EXPECTED_TOTAL_SETTLEMENTS = 37
EXPECTED_KINGDOM_SETTLEMENTS = 35
EXPECTED_VALORSMARK_PROVINCES = 6
EXPECTED_VALORSMARK_SETTLEMENTS = 15
EXPECTED_HAFENMARK_PROVINCES = 4
EXPECTED_HAFENMARK_SETTLEMENTS = 10
EXPECTED_VARFELL_PROVINCES = 4
EXPECTED_VARFELL_SETTLEMENTS = 10


# ── Lookups ──────────────────────────────────────────────────────────────────

def by_id(sid: str) -> Settlement:
    for s in REGISTRY:
        if s.id == sid:
            return s
    raise KeyError(sid)

def by_province(province: str) -> Tuple[Settlement, ...]:
    return tuple(s for s in REGISTRY if s.province == province)

def by_duchy(duchy: str) -> Tuple[Settlement, ...]:
    return tuple(s for s in REGISTRY if s.duchy == duchy)

def is_special_entity(s: Settlement) -> bool:
    return s.duchy in SPECIAL_ENTITIES

def kingdom_settlements() -> Tuple[Settlement, ...]:
    return tuple(s for s in REGISTRY if s.duchy in KINGDOM_DUCHIES)


# ── §1.3 stat schema ─────────────────────────────────────────────────────────

@dataclass
class SettlementStats:
    """Three-stat block per §1.3. Range-checked on construction.
    Starting values are NOT canonical at §1.3 — downstream modules supply them
    (Finding F4)."""
    prosperity: int
    defense: int
    order: int

    def __post_init__(self):
        for name, v in (('prosperity', self.prosperity),
                        ('defense', self.defense),
                        ('order', self.order)):
            if not (STAT_MIN <= v <= STAT_MAX):
                raise ValueError(
                    f"Settlement stat {name!r}={v} outside canonical "
                    f"[{STAT_MIN}, {STAT_MAX}] range (§1.3)"
                )


# ── §1.3 derived values ──────────────────────────────────────────────────────

def local_economy(prosperity: int) -> int:
    """Gold income contribution to faction Treasury per §1.3."""
    return prosperity * LOCAL_ECONOMY_PER_PROSPERITY

def garrison_strength(defense: int, fort_level: int = 0) -> int:
    """Settlement defensibility score per §1.3."""
    return defense * GARRISON_PER_DEFENSE + fort_level * GARRISON_PER_FORT_LEVEL

def public_order(order: int) -> int:
    """Civil stability meter per §1.3. Below 0 triggers riot events
    (per §1.3 prose: 'below 0 triggers riot events')."""
    return order * PUBLIC_ORDER_PER_ORDER


# ── §1.3 province Accord derivation (REVISED rule) ───────────────────────────

def province_accord_from_settlements(
    province: str,
    stats_by_settlement: Dict[str, SettlementStats],
) -> int:
    """Province Accord = floor(mean(settlement Order across all settlements
    in the province)). [canonical: §1.3 'Province Accord is now the floor of
    the average Order across all settlements in the province, rounded down.']
    """
    settlements_in_p = by_province(province)
    if not settlements_in_p:
        raise KeyError(f"No settlements in province {province!r}")
    orders = [stats_by_settlement[s.id].order for s in settlements_in_p
              if s.id in stats_by_settlement]
    if not orders:
        raise ValueError(f"No stat blocks supplied for province {province!r}")
    return floor(sum(orders) / len(orders))


# ── Player-action substrate (Module 1 hook surface) ──────────────────────────
# Module 1 does not implement improvement/maintenance/problem-resolution
# handlers — those are Modules 3/6/7/8. Module 1 surfaces the substrate they
# attach to:
#   - Settlement (immutable identity)
#   - SettlementStats (mutable state — improvement/maintenance writes here)
#   - province_accord_from_settlements (mutation feedback into province layer)
# The player-action loop (Jordan, 2026-05-13): action → state mutation →
# faction Order/Accord delta → faction standing → Stature/renown. Module 1
# carries the first two; Modules 5/8/12 carry the rest.


# ── Isolation tests (Mode G verification) ────────────────────────────────────

def run_isolation_tests() -> Dict[str, str]:
    r: Dict[str, str] = {}
    import re as _re

    # T1 — total registry length matches §2.1 summary
    r['T1_total_count'] = (
        'PASS' if len(REGISTRY) == EXPECTED_TOTAL_SETTLEMENTS else
        f'FAIL (got {len(REGISTRY)}, expected {EXPECTED_TOTAL_SETTLEMENTS})'
    )

    # T2 — every ID unique
    ids = [s.id for s in REGISTRY]
    r['T2_id_uniqueness'] = (
        'PASS' if len(set(ids)) == len(ids) else 'FAIL (duplicates exist)'
    )

    # T3 — every ID matches S-NNN format
    ok = all(_re.fullmatch(r'S-\d{3}', s.id) for s in REGISTRY)
    r['T3_id_format'] = 'PASS' if ok else 'FAIL (non-S-NNN id present)'

    # T4 — Kingdom settlement count matches summary
    kingdom = kingdom_settlements()
    r['T4_kingdom_count'] = (
        'PASS' if len(kingdom) == EXPECTED_KINGDOM_SETTLEMENTS else
        f'FAIL (got {len(kingdom)}, expected {EXPECTED_KINGDOM_SETTLEMENTS})'
    )

    # T5 — Valorsmark province + settlement counts
    v = by_duchy('Valorsmark')
    v_provs = {s.province for s in v}
    ok = (len(v) == EXPECTED_VALORSMARK_SETTLEMENTS and
          len(v_provs) == EXPECTED_VALORSMARK_PROVINCES)
    r['T5_valorsmark_counts'] = (
        'PASS' if ok else
        f'FAIL (got {len(v_provs)} provinces / {len(v)} settlements)'
    )

    # T6 — Hafenmark province + settlement counts
    h = by_duchy('Hafenmark')
    h_provs = {s.province for s in h}
    ok = (len(h) == EXPECTED_HAFENMARK_SETTLEMENTS and
          len(h_provs) == EXPECTED_HAFENMARK_PROVINCES)
    r['T6_hafenmark_counts'] = (
        'PASS' if ok else
        f'FAIL (got {len(h_provs)} provinces / {len(h)} settlements)'
    )

    # T7 — Varfell province + settlement counts
    f = by_duchy('Varfell')
    f_provs = {s.province for s in f}
    ok = (len(f) == EXPECTED_VARFELL_SETTLEMENTS and
          len(f_provs) == EXPECTED_VARFELL_PROVINCES)
    r['T7_varfell_counts'] = (
        'PASS' if ok else
        f'FAIL (got {len(f_provs)} provinces / {len(f)} settlements)'
    )

    # T8 — every type appears in either canonical or extra types
    types_used = {s.type for s in REGISTRY}
    unknown = types_used - set(ALL_REGISTRY_TYPES)
    r['T8_type_membership'] = 'PASS' if not unknown else f'FAIL (unknown {unknown})'

    # T9 — distinct provinces "Halvarshelm" (Hafenmark) and "Halvardshelm" (Varfell)
    halv_pairs = [s.duchy for s in REGISTRY if s.province == 'Halvarshelm']
    halvd_pairs = [s.duchy for s in REGISTRY if s.province == 'Halvardshelm']
    ok = (set(halv_pairs) == {'Hafenmark'} and
          set(halvd_pairs) == {'Varfell'})
    r['T9_halvarshelm_vs_halvardshelm'] = (
        'PASS' if ok else 'FAIL (duchy assignment mismatch)'
    )

    # T10 — stat range validation accepts boundaries
    try:
        SettlementStats(prosperity=STAT_MIN, defense=STAT_MIN, order=STAT_MIN)
        SettlementStats(prosperity=STAT_MAX, defense=STAT_MAX, order=STAT_MAX)
        r['T10_stat_boundaries_accepted'] = 'PASS'
    except ValueError as e:
        r['T10_stat_boundaries_accepted'] = f'FAIL ({e})'

    # T11 — stat range validation rejects out-of-range
    rejected_low = False
    rejected_high = False
    try:
        SettlementStats(prosperity=-1, defense=0, order=0)
    except ValueError:
        rejected_low = True
    try:
        SettlementStats(prosperity=0, defense=STAT_MAX + 1, order=0)
    except ValueError:
        rejected_high = True
    r['T11_stat_range_enforced'] = (
        'PASS' if (rejected_low and rejected_high) else 'FAIL'
    )

    # T12 — derived values match §1.3 formulas
    e_econ = local_economy(prosperity=4)
    e_garr = garrison_strength(defense=3, fort_level=2)
    e_pord = public_order(order=3)
    # Expected:
    #   4 * 50 = 200
    #   3 * 20 + 2 * 30 = 60 + 60 = 120
    #   3 * 20 = 60
    ok = (
        e_econ == 4 * LOCAL_ECONOMY_PER_PROSPERITY and
        e_garr == 3 * GARRISON_PER_DEFENSE + 2 * GARRISON_PER_FORT_LEVEL and
        e_pord == 3 * PUBLIC_ORDER_PER_ORDER
    )
    r['T12_derived_value_formulas'] = (
        'PASS' if ok else
        f'FAIL (econ={e_econ}, garr={e_garr}, pord={e_pord})'
    )

    # T13 — province Accord derivation worked example from §1.3:
    # "If a province has 3 settlements with Order 4, 2, and 1, the province
    # Accord = floor((4+2+1)/3) = floor(2.33) = 2"
    # Use Valorsplatz (3 settlements).
    stats = {
        'S-001': SettlementStats(prosperity=0, defense=0, order=4),
        'S-002': SettlementStats(prosperity=0, defense=0, order=2),
        'S-003': SettlementStats(prosperity=0, defense=0, order=1),
    }
    accord = province_accord_from_settlements('Valorsplatz', stats)
    r['T13_province_accord_worked_example'] = (
        'PASS' if accord == 2 else f'FAIL (got {accord}, expected 2)'
    )

    # T14 — lookups are consistent
    first_s = by_id('S-001')
    ok = (first_s.name == 'Valorsplatz' and first_s.duchy == 'Valorsmark' and
          first_s.province == 'Valorsplatz' and first_s.role == 'province_primary')
    r['T14_lookup_by_id'] = 'PASS' if ok else f'FAIL ({first_s})'

    # T15 — special entities flag correctly
    ok = (is_special_entity(by_id('S-036')) and
          is_special_entity(by_id('S-037')) and
          not is_special_entity(by_id('S-001')))
    r['T15_special_entity_flag'] = 'PASS' if ok else 'FAIL'

    return r


if __name__ == '__main__':
    import sys
    results = run_isolation_tests()
    width = max(len(k) for k in results)
    header = "Module 01 — settlement primitives — isolation tests"
    bar_width = max(width, len(header))
    print("=" * bar_width)
    print(header)
    print("=" * bar_width)
    fail = False
    for k, v in results.items():
        marker = '✓' if v == 'PASS' else '✗'
        print(f"  {marker} {k:<{width}} {v}")
        if v != 'PASS':
            fail = True
    print("=" * bar_width)
    print(f"Registry: {len(REGISTRY)} settlements "
          f"({len(kingdom_settlements())} Kingdom + "
          f"{len([s for s in REGISTRY if s.duchy == 'Himmelenger'])} Church + "
          f"{len([s for s in REGISTRY if s.duchy == 'Schoenland'])} foreign)")
    print(f"Types in registry: {sorted({s.type for s in REGISTRY})}")
    sys.exit(1 if fail else 0)
