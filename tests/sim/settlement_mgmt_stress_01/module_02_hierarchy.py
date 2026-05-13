# module_02_hierarchy.py — Political hierarchy + adjacency graph
#
# Mode G Module two of settlement_mgmt_stress_01. Imports the Module 1
# registry and adds:
#   - PP-seven-two-six canonical hierarchy (Valn → Kingdom → Duchy →
#     Province → Territory=Settlement)
#   - Special-case entity treatment (Himmelenger / Askeheim / Schoenland)
#   - Canonical adjacency graph from
#     `designs/territory/valoria_geography_v30.yaml :: settlement_adjacency:`
#   - Greater-than-or-equal-to-two-march-route validator (Schoenland exempt;
#     Askeheim has zero settlements pending healing)
#   - Province fracturing predicate per §two-three
#   - Political-value structure per §two-four (scalars deferred; structure
#     here)
#   - Hierarchy aggregators (duchy → provinces → settlements; faction →
#     provinces fully owned vs. split)
#
# Canonical sources (full read this session):
#   designs/territory/valoria_political_hierarchy_v30.md (PP-rebuild doc)
#   designs/territory/settlement_adjacency_v30.md (PP-superseded doc —
#     partially superseded at granularity layer; §two mass-battle still active)
#   designs/territory/valoria_geography_v30.yaml (settlement_adjacency block)
#   designs/territory/march_layer_v30.md (strategic-movement layer on top;
#     downstream-module territory — read here for §one march-budget signature
#     only)
#
# Out of scope (deferred):
#   - March budget cost computation (downstream module — military granularity)
#   - Edge-type → battle modifier mapping (downstream module)
#   - Per-settlement starting stat values (Finding F-four — checked here
#     against geography YAML; reports outcome to Module one's open question)
#   - Faction-controller tracking (downstream module — governance)
#   - Fracturing state-machine event-trigger specifics (§two-three calls
#     these "deferred to Class B follow-up PP" — governance module carries
#     the integration test)

from dataclasses import dataclass, field
from typing import Dict, FrozenSet, List, Set, Tuple

# Import Module 1 substrate
from module_01_primitives import (
    REGISTRY,
    Settlement,
    KINGDOM_DUCHIES,
    SPECIAL_ENTITIES,
    by_id,
    by_province,
    by_duchy,
    is_special_entity,
)

# ── Canonical hierarchy (PP-726 §1) ──────────────────────────────────────────

# [canonical: designs/territory/valoria_political_hierarchy_v30.md §1.1
#  "Valn is the peninsula — pure geographic extent"]
GEOGRAPHIC_EXTENT_NAME = 'Valn'

# [canonical: political_hierarchy §1.1
#  "Kingdom of Valoria is the sovereign realm covering most of Valn"]
SOVEREIGN_REALM_NAME = 'Kingdom of Valoria'

# [canonical: political_hierarchy §1.2 — "Three entities sit within Valn
#  geographically but outside the standard duchy/province hierarchy:
#  Himmelenger ... Askeheim ... Schoenland"]
# Askeheim currently has zero settlements (Calamity wilderness), so it does
# NOT appear in the Module 1 registry — but it IS a recognized special
# entity in the hierarchy.
SPECIAL_CASE_ENTITIES: Tuple[str, ...] = ('Himmelenger', 'Askeheim', 'Schoenland')

# [canonical: political_hierarchy §1.1
#  "Almund (Almud), who is also Duke of Valorsmark"]
MONARCH_NAME = 'Almund'
MONARCH_DUCHY = 'Valorsmark'

# [canonical: political_hierarchy §1.1 — duchy → Duke mapping]
DUCHY_DUKE = {
    'Valorsmark': 'Almund',
    'Hafenmark':  'Baralta',
    'Varfell':    'Vaynard',
}

# [canonical: political_hierarchy §2.1
#  "Each province has 1–3 settlements ... minimum is 2"]
MIN_SETTLEMENTS_PER_PROVINCE = 2
MAX_SETTLEMENTS_PER_PROVINCE = 3

# [canonical: political_hierarchy §2.2
#  "Each settlement is connected by road to at least two other settlements"]
MIN_CONNECTIONS_PER_SETTLEMENT = 2

# [canonical: political_hierarchy §2.1
#  "14 provinces total in the duchy hierarchy = 35 settlements"]
EXPECTED_KINGDOM_PROVINCES = 14
EXPECTED_KINGDOM_SETTLEMENTS_PH = 35


# ── Adjacency graph from geography YAML (PP-726 rebuild, 56 edges) ───────────

# Edge type taxonomy from settlement_adjacency_v30 §1.1 and the canonical
# YAML usage. The YAML uses 'road' (most edges), 'sea' (S-001↔S-037 only),
# and (per settlement_adjacency §1.1) future types include 'river',
# 'mountain_pass', 'coastal', 'thread_witnessed'. Module 2 surfaces the
# taxonomy; Module 7 uses the modifiers.
# [canonical: designs/territory/settlement_adjacency_v30.md §1.1 edge-type
#  table]
EDGE_TYPES: Tuple[str, ...] = (
    'road', 'sea', 'river', 'mountain_pass', 'coastal', 'thread_witnessed',
)

@dataclass(frozen=True)
class Edge:
    """An adjacency edge. Frozen + hashable for set membership.
    Canonically authored in valoria_geography_v30.yaml :: settlement_adjacency:."""
    a: str  # endpoint S-ID (canonical 'from' or undirected lo-S-ID)
    b: str  # endpoint S-ID (canonical 'to'   or undirected hi-S-ID)
    type: str
    note: str = ''

    def endpoints(self) -> FrozenSet[str]:
        return frozenset((self.a, self.b))


# Edge data transcribed from geography YAML settlement_adjacency block.
# [canonical: designs/territory/valoria_geography_v30.yaml ::
#  settlement_adjacency: — 56 edges (28 intra + 24 primary inter + 1 sea +
#  3 second-routes)]
_EDGE_DATA: Tuple[Tuple[str, str, str, str], ...] = (
    # Intra-province (28 edges: 7 triangles × 3 + 7 singles × 1)
    ('S-001', 'S-002', 'road', 'intra-Valorsplatz'),
    ('S-001', 'S-003', 'road', 'intra-Valorsplatz'),
    ('S-002', 'S-003', 'road', 'intra-Valorsplatz triangle'),
    ('S-004', 'S-005', 'road', 'intra-Kronmark'),
    ('S-004', 'S-006', 'road', 'intra-Kronmark'),
    ('S-005', 'S-006', 'road', 'intra-Kronmark triangle'),
    ('S-007', 'S-008', 'road', 'intra-Lowenskyst'),
    ('S-009', 'S-010', 'road', 'intra-Feldmark'),
    ('S-009', 'S-011', 'road', 'intra-Feldmark'),
    ('S-010', 'S-011', 'road', 'intra-Feldmark triangle'),
    ('S-012', 'S-013', 'road', 'intra-Stillhelm'),
    ('S-014', 'S-015', 'road', 'intra-Ehrenfeld'),
    ('S-016', 'S-017', 'road', 'intra-Rendstad'),
    ('S-018', 'S-019', 'road', 'intra-Gransol'),
    ('S-018', 'S-020', 'road', 'intra-Gransol'),
    ('S-019', 'S-020', 'road', 'intra-Gransol triangle'),
    ('S-021', 'S-022', 'road', 'intra-Spartfell'),
    ('S-023', 'S-024', 'road', 'intra-Halvarshelm'),
    ('S-023', 'S-025', 'road', 'intra-Halvarshelm'),
    ('S-024', 'S-025', 'road', 'intra-Halvarshelm triangle'),
    ('S-026', 'S-027', 'road', 'intra-Grauwald'),
    ('S-028', 'S-029', 'road', 'intra-Halvardshelm'),
    ('S-028', 'S-030', 'road', 'intra-Halvardshelm'),
    ('S-029', 'S-030', 'road', 'intra-Halvardshelm triangle'),
    ('S-031', 'S-032', 'road', 'intra-Sigurdshelm'),
    ('S-031', 'S-033', 'road', 'intra-Sigurdshelm'),
    ('S-032', 'S-033', 'road', 'intra-Sigurdshelm triangle'),
    ('S-034', 'S-035', 'road', 'intra-Oastad'),
    # Inter-province primary (24 edges + 1 sea = 25)
    ('S-003', 'S-004', 'road', 'Valorsplatz↔Kronmark'),
    ('S-002', 'S-009', 'road', 'Valorsplatz↔Feldmark'),
    ('S-001', 'S-014', 'road', 'Valorsplatz↔Ehrenfeld (royal-fortress axis)'),
    ('S-001', 'S-037', 'sea',  'Valorsplatz↔Schoenland (port-mediated sea route)'),
    ('S-005', 'S-007', 'road', 'Kronmark↔Lowenskyst (granary→garrison)'),
    ('S-006', 'S-036', 'road', 'Kronmark↔Himmelenger (river-ford pilgrim route)'),
    ('S-004', 'S-014', 'road', 'Kronmark↔Ehrenfeld'),
    ('S-008', 'S-036', 'road', 'Lowenskyst↔Himmelenger (southern valley pilgrim)'),
    ('S-007', 'S-023', 'road', 'Lowenskyst↔Halvarshelm (military-mining ore)'),
    ('S-010', 'S-012', 'road', 'Feldmark↔Stillhelm'),
    ('S-011', 'S-014', 'road', 'Feldmark↔Ehrenfeld (grain to garrison)'),
    ('S-013', 'S-034', 'road', 'Stillhelm↔Oastad (Calamity-edge southern)'),
    ('S-014', 'S-026', 'road', 'Ehrenfeld↔Grauwald (west gate of crownlands)'),
    ('S-015', 'S-036', 'road', 'Ehrenfeld↔Himmelenger (north gate of crownlands)'),
    ('S-027', 'S-016', 'road', 'Grauwald↔Rendstad (cross-duchy timber)'),
    ('S-016', 'S-018', 'road', 'Rendstad↔Gransol (timber to lake-capital)'),
    ('S-018', 'S-036', 'road', 'Gransol↔Himmelenger (commerce-Church)'),
    ('S-019', 'S-021', 'road', 'Gransol↔Spartfell (lake-shore to NW pass)'),
    ('S-020', 'S-023', 'road', 'Gransol↔Halvarshelm (inland trade to mining)'),
    ('S-036', 'S-024', 'road', 'Himmelenger↔Halvarshelm (mineral pilgrim)'),
    ('S-021', 'S-028', 'road', 'Spartfell↔Halvardshelm (mountain pass to fjord)'),
    ('S-028', 'S-031', 'road', 'Halvardshelm↔Sigurdshelm (fjord to ducal capital)'),
    ('S-026', 'S-031', 'road', 'Grauwald↔Sigurdshelm (highland to capital)'),
    ('S-033', 'S-034', 'road', 'Sigurdshelm↔Oastad (coastal southward)'),
    # Inter-province second-routes (3 edges)
    ('S-017', 'S-020', 'road', 'Rendstad↔Gransol second route (bridge-trade alt)'),
    ('S-022', 'S-030', 'road', 'Spartfell↔Halvardshelm second route (foothills bypass)'),
    ('S-033', 'S-035', 'road', 'Sigurdshelm↔Oastad second route (salt-pans coastal alt)'),
)

EDGES: Tuple[Edge, ...] = tuple(Edge(*row) for row in _EDGE_DATA)

# [canonical: geography_v30.yaml settlement_adjacency header
#  "56 edges total: 28 intra-province ... + 28 inter-province"]
#
# [FINDING F5] The YAML *header comment* asserts 56 edges (28 intra + 28
# inter). The YAML *actual content* enumerates 55 edges: 28 intra-province
# + 24 primary inter (including the 1 sea-edge S-001↔S-037) + 3
# second-routes. Header math is internally inconsistent — "24 primary + 1
# sea" is one section but the count 24 already includes the sea (verified
# by counting the listed `- {from: ...}` lines). Module 2 trusts the
# content over the comment.
#
# This is surfaced for editorial reconciliation. The mechanically-meaningful
# question (≥2-march-route rule satisfied across the registry except
# Schoenland-exempt) holds either way.
EXPECTED_TOTAL_EDGES = 55                # actual YAML content
EXPECTED_INTRA_PROVINCE_EDGES = 28
EXPECTED_INTER_PROVINCE_EDGES = 27       # 24 primary (incl. 1 sea) + 3 second-routes
HEADER_ASSERTED_TOTAL_EDGES = 56         # canonical header comment
HEADER_ASSERTED_INTER_EDGES = 28         # canonical header comment


# ── Adjacency lookups ────────────────────────────────────────────────────────

def neighbors(sid: str) -> Tuple[str, ...]:
    """Return the S-IDs adjacent to `sid` in the canonical graph."""
    out: List[str] = []
    for e in EDGES:
        if e.a == sid:
            out.append(e.b)
        elif e.b == sid:
            out.append(e.a)
    return tuple(out)

def degree(sid: str) -> int:
    return len(neighbors(sid))

def is_intra_province(e: Edge) -> bool:
    a = by_id(e.a)
    b = by_id(e.b)
    return a.province == b.province

def is_inter_province(e: Edge) -> bool:
    return not is_intra_province(e)


# ── ≥2-connection rule per PP-726 §2.2 ───────────────────────────────────────

def validate_min_connections() -> Dict[str, int]:
    """Return mapping of every settlement S-ID to its degree. Caller checks
    against `MIN_CONNECTIONS_PER_SETTLEMENT` and `SCHOENLAND_FOREIGN_EXEMPT`.
    """
    return {s.id: degree(s.id) for s in REGISTRY}

# [canonical: political_hierarchy §1.2 — "Schoenland ... is exempt from the
#  Kingdom's ≥2 march-route rule (its singular sea-connection is the canonical
#  condition pending ED-055 naval-scope expansion)"]
SCHOENLAND_FOREIGN_EXEMPT: str = 'S-037'


# ── Province fracturing predicate (PP-726 §2.3) ──────────────────────────────

def province_is_fractured(province: str,
                          settlement_factions: Dict[str, str]) -> bool:
    """A province is fractured if its constituent settlements are aligned
    to different factions.
    [canonical: political_hierarchy §2.3 — "A province whose constituent
    territories are aligned to different factions is canonically fractured"]
    """
    settlements_in_p = by_province(province)
    factions = {settlement_factions.get(s.id, None)
                for s in settlements_in_p}
    # `None` (unowned) treated as its own faction-class for the purpose of
    # this predicate — an unowned territory in a faction-owned province
    # IS a fracture state.
    return len(factions) > 1


# ── Political-value structure (PP-726 §2.4) ──────────────────────────────────
# The structure is canonical; scalars are NOT (§2.4 explicitly: "Specific
# scalar values are TBD pending balance pass").
# Module 2 surfaces the structure with placeholder zero scalars. Module 12
# (faction integration) supplies real scalars from canonical params when
# balance pass completes.

@dataclass(frozen=True)
class PoliticalValueComputation:
    """Structure per §2.4; scalars deferred to balance pass."""
    territory_values: Dict[str, int] = field(default_factory=dict)
    province_unification_bonus: int = 0   # canonical TBD — placeholder zero

    def value_for(self,
                  faction: str,
                  ownership: Dict[str, str]) -> int:
        # Σ territory_values for owned territories
        owned = [sid for sid, f in ownership.items() if f == faction]
        total = sum(self.territory_values.get(sid, 0) for sid in owned)
        # + Σ province_unification_bonus for fully-owned provinces
        provinces = {by_id(sid).province for sid in owned}
        for p in provinces:
            settlements_in_p = by_province(p)
            if all(ownership.get(s.id) == faction for s in settlements_in_p):
                total += self.province_unification_bonus
        return total


# ── Aggregators ──────────────────────────────────────────────────────────────

def provinces_in_duchy(duchy: str) -> Tuple[str, ...]:
    """Return distinct province names in `duchy` (or special-entity name)."""
    return tuple(sorted({s.province for s in REGISTRY if s.duchy == duchy}))

def kingdom_provinces() -> Tuple[str, ...]:
    """Return distinct Kingdom provinces (excludes special-case entities)."""
    return tuple(sorted({s.province for s in REGISTRY
                         if s.duchy in KINGDOM_DUCHIES}))

def all_provinces() -> Tuple[str, ...]:
    """All provinces and special-case entities present in the registry."""
    return tuple(sorted({s.province for s in REGISTRY}))


# ── Isolation tests ──────────────────────────────────────────────────────────

def run_isolation_tests() -> Dict[str, str]:
    r: Dict[str, str] = {}

    # T1 — total edge count == 56
    r['T1_total_edge_count'] = (
        'PASS' if len(EDGES) == EXPECTED_TOTAL_EDGES else
        f'FAIL (got {len(EDGES)}, expected {EXPECTED_TOTAL_EDGES})'
    )

    # T2 — intra-province edge count == 28
    intra = [e for e in EDGES if is_intra_province(e)]
    r['T2_intra_province_edges'] = (
        'PASS' if len(intra) == EXPECTED_INTRA_PROVINCE_EDGES else
        f'FAIL (got {len(intra)}, expected {EXPECTED_INTRA_PROVINCE_EDGES})'
    )

    # T3 — inter-province edge count == 28
    inter = [e for e in EDGES if is_inter_province(e)]
    r['T3_inter_province_edges'] = (
        'PASS' if len(inter) == EXPECTED_INTER_PROVINCE_EDGES else
        f'FAIL (got {len(inter)}, expected {EXPECTED_INTER_PROVINCE_EDGES})'
    )

    # T4 — every settlement has a degree
    degrees = validate_min_connections()
    r['T4_every_settlement_in_degree_map'] = (
        'PASS' if len(degrees) == len(REGISTRY) else
        f'FAIL ({len(degrees)} vs {len(REGISTRY)})'
    )

    # T5 — every Kingdom settlement has ≥2 connections
    violations = [sid for sid, d in degrees.items()
                  if d < MIN_CONNECTIONS_PER_SETTLEMENT
                  and sid != SCHOENLAND_FOREIGN_EXEMPT]
    r['T5_min_connections_kingdom'] = (
        'PASS' if not violations else f'FAIL (violations: {violations})'
    )

    # T6 — Himmelenger has exactly 5 connections
    # [canonical: political_hierarchy §1.2 "Its march-route connections
    # (5 edges per valoria_geography :: settlement_adjacency)"]
    himm_degree = degrees['S-036']
    r['T6_himmelenger_degree_5'] = (
        'PASS' if himm_degree == 5 else f'FAIL (got {himm_degree})'
    )

    # T7 — Schoenland has exactly 1 connection (foreign-exempt)
    sch_degree = degrees['S-037']
    r['T7_schoenland_degree_1'] = (
        'PASS' if sch_degree == 1 else f'FAIL (got {sch_degree})'
    )

    # T8 — Schoenland's single edge is the sea-route to Valorsplatz S-001
    sch_neighbors = neighbors('S-037')
    r['T8_schoenland_sea_to_S001'] = (
        'PASS' if sch_neighbors == ('S-001',) else
        f'FAIL (got {sch_neighbors})'
    )

    # T9 — every edge endpoint is a known settlement
    known_ids = {s.id for s in REGISTRY}
    unknown_endpoints: List[Tuple[str, str]] = []
    for e in EDGES:
        if e.a not in known_ids:
            unknown_endpoints.append((e.a, 'edge.a'))
        if e.b not in known_ids:
            unknown_endpoints.append((e.b, 'edge.b'))
    r['T9_all_endpoints_known'] = (
        'PASS' if not unknown_endpoints else f'FAIL {unknown_endpoints}'
    )

    # T10 — no self-loops
    self_loops = [e for e in EDGES if e.a == e.b]
    r['T10_no_self_loops'] = (
        'PASS' if not self_loops else f'FAIL ({self_loops})'
    )

    # T11 — no duplicate undirected edges
    seen: Set[FrozenSet[str]] = set()
    dupes: List[Tuple[str, str]] = []
    for e in EDGES:
        ep = e.endpoints()
        if ep in seen:
            dupes.append((e.a, e.b))
        seen.add(ep)
    r['T11_no_duplicate_edges'] = (
        'PASS' if not dupes else f'FAIL ({dupes})'
    )

    # T12 — every Kingdom duchy has provinces in the registry
    for d in KINGDOM_DUCHIES:
        provs = provinces_in_duchy(d)
        if not provs:
            r['T12_duchy_provinces'] = f'FAIL ({d} has no provinces)'
            break
    else:
        r['T12_duchy_provinces'] = 'PASS'

    # T13 — kingdom_provinces() returns 14 distinct provinces (PP-726 §2.1)
    k_provs = kingdom_provinces()
    r['T13_kingdom_province_count_14'] = (
        'PASS' if len(k_provs) == EXPECTED_KINGDOM_PROVINCES else
        f'FAIL (got {len(k_provs)}, expected {EXPECTED_KINGDOM_PROVINCES})'
    )

    # T14 — every Kingdom province has 1–3 settlements (PP-726 §2.1)
    bad_provinces: List[Tuple[str, int]] = []
    for p in k_provs:
        n = len(by_province(p))
        if not (MIN_SETTLEMENTS_PER_PROVINCE <= n <= MAX_SETTLEMENTS_PER_PROVINCE):
            bad_provinces.append((p, n))
    r['T14_province_settlement_counts'] = (
        'PASS' if not bad_provinces else f'FAIL ({bad_provinces})'
    )

    # T15 — fracturing predicate fires on mixed-faction province
    # Worked example: Valorsplatz (S-001, S-002, S-003) — assign S-001 to
    # Crown, S-002 to Crown, S-003 to Hafenmark → fractured.
    ownership_fractured = {
        'S-001': 'Crown',
        'S-002': 'Crown',
        'S-003': 'Hafenmark',
    }
    r['T15_fracturing_predicate_fires'] = (
        'PASS' if province_is_fractured('Valorsplatz', ownership_fractured)
        else 'FAIL'
    )

    # T16 — fracturing predicate negative case
    ownership_unified = {
        'S-001': 'Crown',
        'S-002': 'Crown',
        'S-003': 'Crown',
    }
    r['T16_fracturing_predicate_unified'] = (
        'PASS' if not province_is_fractured('Valorsplatz', ownership_unified)
        else 'FAIL'
    )

    # T17 — political-value computation: unification bonus fires only on
    # full ownership
    pvc = PoliticalValueComputation(
        territory_values={'S-001': 10, 'S-002': 10, 'S-003': 10},
        province_unification_bonus=50,
    )
    val_partial = pvc.value_for('Crown', ownership_fractured)  # 2 owned
    val_full = pvc.value_for('Crown', ownership_unified)       # 3 owned + bonus
    # Expected partial = 2 territories × 10 each = 20; expected full =
    # 3 territories × 10 + 50 unification bonus = 80.
    # [canonical: derived arithmetic from §2.4 structure with test scalars]
    expected_partial = 20
    # [canonical: derived arithmetic from §2.4 structure with test scalars]
    expected_full = 80
    r['T17_unification_bonus_full_only'] = (
        'PASS' if val_partial == expected_partial and val_full == expected_full
        else f'FAIL (partial={val_partial}, full={val_full})'
    )

    # T18 — monarch / monarch_duchy consistency
    r['T18_monarch_consistency'] = (
        'PASS' if DUCHY_DUKE[MONARCH_DUCHY] == MONARCH_NAME else 'FAIL'
    )

    # T19 — Kingdom settlement total via hierarchy matches PP-726
    n_kingdom = sum(len(by_province(p)) for p in kingdom_provinces())
    r['T19_kingdom_settlement_total_via_provinces'] = (
        'PASS' if n_kingdom == EXPECTED_KINGDOM_SETTLEMENTS_PH else
        f'FAIL (got {n_kingdom}, expected {EXPECTED_KINGDOM_SETTLEMENTS_PH})'
    )

    # T20 — Askeheim has zero settlements (PP-726 §1.2 "Currently zero
    # settlements")
    askeheim_settlements = [s for s in REGISTRY if s.province == 'Askeheim']
    r['T20_askeheim_zero_settlements'] = (
        'PASS' if not askeheim_settlements else f'FAIL ({askeheim_settlements})'
    )

    # T21 — graph connectivity (component containing S-001 reaches all
    # Kingdom + Himmelenger + Schoenland — i.e. one connected component
    # across the entire registry)
    visited: Set[str] = set()
    stack = ['S-001']
    while stack:
        cur = stack.pop()
        if cur in visited:
            continue
        visited.add(cur)
        stack.extend(neighbors(cur))
    unreached = {s.id for s in REGISTRY} - visited
    r['T21_graph_connected'] = (
        'PASS' if not unreached else f'FAIL (unreached: {sorted(unreached)})'
    )

    # T22 — every edge type is in the canonical taxonomy
    bad_types = [e for e in EDGES if e.type not in EDGE_TYPES]
    r['T22_edge_types_in_taxonomy'] = (
        'PASS' if not bad_types else f'FAIL ({[(e.a, e.b, e.type) for e in bad_types]})'
    )

    return r


if __name__ == '__main__':
    import sys
    results = run_isolation_tests()
    width = max(len(k) for k in results)
    header = "Module 02 — political hierarchy + adjacency — isolation tests"
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
    print(f"Edges: {len(EDGES)} total "
          f"({sum(1 for e in EDGES if is_intra_province(e))} intra + "
          f"{sum(1 for e in EDGES if is_inter_province(e))} inter)")
    print(f"Provinces: {len(kingdom_provinces())} Kingdom + "
          f"{len([p for p in all_provinces() if p not in kingdom_provinces()])} special")
    sys.exit(1 if fail else 0)
