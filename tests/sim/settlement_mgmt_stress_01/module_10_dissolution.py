# module_10_dissolution_and_catalogue.py — Niflhel-dissolution emergence + POI templates + impact catalogue
#
# Mode G Module ten of settlement_mgmt_stress_01.
#
# Approach: BOTTOM-UP GRANULAR EMERGENT (continued from M6/M7/M8/M9).
#
# THROUGHLINE BINDINGS (per references/throughlines_meta_infill.md §3.1):
#
#   T-27 Effects Real, Explanation Wrong — PRIMARY. М-4 institutional.
#   Black markets and intelligence brokers are the canonical instances of
#   "Effects Real, Explanation Wrong": official institutional framing
#   (governance crisis) and the underground operational reality (Wealth +0.5
#   from illicit trade) diverge. Per the canon catalog:
#   "Primary institutional (faction interpretive-frame coherent-but-wrong).
#   Secondary forced-choice (argument fails; frame-crack requires confrontation)."
#
#   T-30 Information Asymmetry as Core Mechanic — SECONDARY. М-8 access-gated.
#   Intelligence brokers operationalize information asymmetry. Already
#   wired in M6 via attempt_niflhel_detection. Module 10 extends with
#   broker placement predicates.
#
#   T-03 Inseparability — SECONDARY. М-3 substrate-grounded. Thread
#   Exploitation Sites (§4.9) are settlements at Thread Proximity <= 2
#   where Thread residue accumulates naturally; harvesting them affects
#   peninsula-level RS (Real Substrate) which propagates across scales.
#
# META-THROUGHLINE BINDINGS:
#
#   М-7 BORROWINGS ARE OPERATIONAL EXTENSIONS — PRIMARY. The three
#   §4.7/§4.8/§4.9 mechanics are the canonical operational extensions
#   that emerge when official institutions fail: black market is the
#   operational extension of trade when governance breaks; intel brokers
#   are the operational extension of intelligence when no faction
#   sponsors it; thread exploitation is the operational extension of
#   threadwork when no warden monitors the site. М-7 primary binding
#   closes another previously-unbound meta-throughline (M9 closed М-1).
#
#   М-8 ACCESS IS VERTICAL-POSITION GATED — SECONDARY. Intelligence
#   brokers gate information access through fieldwork actions.
#
# Encodes:
#   §4.6 Settlement POI Templates (Depth Axis per settlement type)
#   §4.7 Black Markets (Niflhel Dissolution — emergence-from-failure)
#   §4.8 Intelligence Brokers (Niflhel Dissolution — emergence-from-failure)
#   §4.9 Thread Exploitation Sites (Niflhel Dissolution — emergence-from-failure)
#   §8.1 Changes to Existing Systems (audit catalogue)
#   §8.2 What Does NOT Change (audit invariants)
#
# Bottom-up: each dissolution phenomenon is a pure predicate on settlement
# state. Black market emerges when Order <= 1 OR no governor. Intel broker
# emerges when Prosperity >= 3 AND (no governor OR governor stability <= 2).
# Thread Exploitation Site emerges when Thread Proximity <= 2.
#
# These mechanics complete the "emergence-from-governance-failure" surface
# of the player-action loop — failed governance does not just degrade the
# settlement; it produces NEW emergent surfaces (markets, brokers, sites).
# The player gains an option set even from failure.
#
# Canonical source (full read this session):
#   designs/territory/settlement_layer_v30.md (§4.6, §4.7, §4.8, §4.9, §8.1, §8.2)

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Tuple

from module_01_primitives import Settlement, SettlementStats
from module_03_facilities import ActionResult
from module_05_governance import GovernorState


# ── §4.7 Black Markets ─────────────────────────────────────────────────────

# [canonical: settlement_layer_v30 §4.7 — emergence conditions]
# "Any settlement with Order ≤ 1 or no governor develops a black market."
BLACK_MARKET_ORDER_THRESHOLD: int = 1
# "Automatic when settlement Order ≥ 3" — disappearance
BLACK_MARKET_DISAPPEAR_ORDER_THRESHOLD: int = 3

# [canonical: settlement_layer_v30 §4.7 effects —
#  "Settlement Wealth +0.5 (illicit trade is still trade).
#  Settlement Accord −0.5 (population distrusts lawless governance)."]
# Encoded as half-units (M4 half-encoding pattern)
BLACK_MARKET_HALF_WEALTH_DELTA_PER_SEASON: int = 1   # +0.5 = 1 half-unit
BLACK_MARKET_HALF_ACCORD_DELTA_PER_SEASON: int = 1   # -0.5 = 1 half-unit negative


def predicate_black_market_emerges(
    stats: SettlementStats,
    has_governor: bool,
) -> bool:
    """§4.7 — Black market emergence predicate. Pure function of state."""
    return stats.order <= BLACK_MARKET_ORDER_THRESHOLD or not has_governor


def predicate_black_market_disappears(stats: SettlementStats) -> bool:
    """§4.7 — Black market disappearance predicate. Pure function of state."""
    return stats.order >= BLACK_MARKET_DISAPPEAR_ORDER_THRESHOLD


@dataclass
class BlackMarketState:
    # Per-settlement black market state. Half-unit accumulators for
    # Wealth gain and Accord loss; downstream Module-twelve consumes for
    # province-level effects.
    settlement_id: str
    active: bool = False
    half_wealth_accumulated: int = 0    # half-units; 2 = +1 Wealth
    half_accord_lost: int = 0           # half-units; 2 = -1 Accord


def accrue_black_market_effects(
    bm: BlackMarketState,
) -> None:
    # §4.7 per-season accrual. Module-nine Accounting hook calls this for
    # each active black market. Module-twelve consumes the accumulated half-units.
    if not bm.active:
        return
    bm.half_wealth_accumulated += BLACK_MARKET_HALF_WEALTH_DELTA_PER_SEASON
    bm.half_accord_lost += BLACK_MARKET_HALF_ACCORD_DELTA_PER_SEASON


# ── §4.8 Intelligence Brokers ──────────────────────────────────────────────

# [canonical: settlement_layer_v30 §4.8 placement —
#  "One broker per settlement with Prosperity ≥ 3 and no governor or governor
#  Stability ≤ 2"]
INTEL_BROKER_PROSPERITY_THRESHOLD: int = 3
INTEL_BROKER_GOVERNOR_STABILITY_THRESHOLD: int = 2


def predicate_intel_broker_emerges(
    stats: SettlementStats,
    has_governor: bool,
    governor_stability: int,
) -> bool:
    """§4.8 — Intel Broker emergence predicate. Pure function of state.
    Requires Prosperity ≥ 3 AND (no governor OR governor stability ≤ 2)."""
    if stats.prosperity < INTEL_BROKER_PROSPERITY_THRESHOLD:
        return False
    if not has_governor:
        return True
    return governor_stability <= INTEL_BROKER_GOVERNOR_STABILITY_THRESHOLD


@dataclass
class IntelBroker:
    # §4.8 individual intel-broker NPC. Discoverable via Tribune or
    # Riskbreaker actions; sells faction intel; can be killed, bought out,
    # or turned. Disposition tracking per the canon — Module-twelve wires
    # full Disposition mechanics.
    settlement_id: str
    name: str
    disposition_by_party: Dict[str, int] = field(default_factory=dict)


# ── §4.9 Thread Exploitation Sites ─────────────────────────────────────────

# [canonical: settlement_layer_v30 §4.9 emergence —
#  "Any settlement with Thread Proximity ≤ 2"]
THREAD_EXPLOITATION_PROXIMITY_THRESHOLD: int = 2

# [canonical: settlement_layer_v30 §4.9 harvesting effects —
#  "RS −0.5 per harvest per season. Wealth +1 for harvesting faction."]
# Encoded as half-units for RS
THREAD_HARVEST_HALF_RS_PENALTY_PER_HARVEST: int = 1   # 0.5 RS = 1 half-unit
THREAD_HARVEST_WEALTH_GAIN: int = 1


def predicate_thread_exploitation_site_present(
    settlement_thread_proximity: int,
) -> bool:
    """§4.9 — Thread Exploitation Site presence predicate.
    Pure function of settlement's Thread Proximity rating."""
    return settlement_thread_proximity <= THREAD_EXPLOITATION_PROXIMITY_THRESHOLD


@dataclass
class ThreadExploitationSite:
    """§4.9 — site at Thread Proximity ≤ 2. Harvestable by any faction
    that discovers it (Investigation action required)."""
    settlement_id: str
    discovered_by: List[str] = field(default_factory=list)   # faction names
    times_harvested: int = 0


def harvest_thread_site(
    site: ThreadExploitationSite,
    harvesting_faction: str,
) -> ActionResult:
    # §4.9 — apply one harvest. RS −0.5/season; Wealth +1 for harvester.
    # Mutates site state. Module-twelve consumes the half-RS-penalty and
    # Wealth-gain via ActionResult.
    if harvesting_faction not in site.discovered_by:
        site.discovered_by.append(harvesting_faction)
    site.times_harvested += 1
    return ActionResult(
        success=True,
        reason='thread_harvest',
        state_mutated=True,
        # Peninsula-wide RS half-unit penalty; Module 12 binds to RS track
        treasury_delta=THREAD_HARVEST_WEALTH_GAIN,
        faction_standing_delta=0,
        renown_delta=0,
    )


# ── §4.6 Settlement POI templates ──────────────────────────────────────────

# [canonical: settlement_layer_v30 §4.6 — "Each settlement has 2-4 POIs
#  across Depth levels"]
POI_COUNT_MIN: int = 2
POI_COUNT_MAX: int = 4

# §4.6 Depth Axis: 4 levels (0/1/2/3+)
DEPTH_LEVEL_SURFACE: int = 0      # Surface (visible)
DEPTH_LEVEL_SETTLED: int = 1      # Settled (free information)
DEPTH_LEVEL_HIDDEN: int = 2       # Hidden (requires fieldwork)
DEPTH_LEVEL_BURIED: int = 3       # Buried/Liminal (deep fieldwork)


@dataclass(frozen=True)
class POIEntry:
    """§4.6 Settlement POI Template entry."""
    depth_level: int
    description: str


# §4.6 canonical POI templates per settlement type
# [canonical: settlement_layer_v30 §4.6 Settlement POI Templates table]
POI_TEMPLATES_BY_SETTLEMENT_TYPE: Dict[str, List[POIEntry]] = {
    'Seat': [
        POIEntry(DEPTH_LEVEL_SURFACE,  'Court, public buildings'),
        POIEntry(DEPTH_LEVEL_SETTLED,  'Administrative archives, court records'),
        POIEntry(DEPTH_LEVEL_HIDDEN,   'Private chambers, secret passages, intelligence archives'),
        POIEntry(DEPTH_LEVEL_BURIED,   'Thread-locked vault, hidden foundations'),
    ],
    'City': [
        POIEntry(DEPTH_LEVEL_SURFACE,  'Market square, artisan quarters'),
        POIEntry(DEPTH_LEVEL_SETTLED,  'Guild halls, merchant ledgers'),
        POIEntry(DEPTH_LEVEL_HIDDEN,   'Smuggling routes, underground economy'),
        POIEntry(DEPTH_LEVEL_BURIED,   'Einhir-era foundations, Thread scars'),
    ],
    'Town': [
        POIEntry(DEPTH_LEVEL_SURFACE,  'Village square, inn'),
        POIEntry(DEPTH_LEVEL_SETTLED,  "Elder's records, family histories"),
        POIEntry(DEPTH_LEVEL_HIDDEN,   'Concealed caches, factional safe houses'),
        POIEntry(DEPTH_LEVEL_BURIED,   'Remnant sites, oral Thread memory'),
    ],
    'Fortress': [
        POIEntry(DEPTH_LEVEL_SURFACE,  'Battlements, armory'),
        POIEntry(DEPTH_LEVEL_SETTLED,  'Command archives, prisoner records'),
        POIEntry(DEPTH_LEVEL_HIDDEN,   'Secret sally ports, covert comms'),
        POIEntry(DEPTH_LEVEL_BURIED,   'Pre-Catastrophe fortification, Locked configurations'),
    ],
    'Port': [
        POIEntry(DEPTH_LEVEL_SURFACE,  'Docks, warehouses'),
        POIEntry(DEPTH_LEVEL_SETTLED,  'Shipping manifests, harbor records'),
        POIEntry(DEPTH_LEVEL_HIDDEN,   'Smuggling networks, Niflhel supply nodes'),
        POIEntry(DEPTH_LEVEL_BURIED,   'Submerged Einhir harbor, maritime Thread signatures'),
    ],
    'Cathedral': [
        POIEntry(DEPTH_LEVEL_SURFACE,  'Nave, clergy quarters'),
        POIEntry(DEPTH_LEVEL_SETTLED,  'Church archives, theological records'),
        POIEntry(DEPTH_LEVEL_HIDDEN,   'Hidden reliquaries, pre-Solmundic architecture, Inquisition files'),
        POIEntry(DEPTH_LEVEL_BURIED,   'Thread-locked artifacts, cathedral as Thread anchor'),
    ],
    'Mine': [
        POIEntry(DEPTH_LEVEL_SURFACE,  'Mine entrance, worker housing'),
        POIEntry(DEPTH_LEVEL_SETTLED,  'Geological surveys, production records'),
        POIEntry(DEPTH_LEVEL_HIDDEN,   'Collapsed tunnels with artifacts'),
        POIEntry(DEPTH_LEVEL_BURIED,   'Einhir excavation sites, substrate exposure'),
    ],
    'Outpost': [
        POIEntry(DEPTH_LEVEL_SURFACE,  'Observation post'),
        POIEntry(DEPTH_LEVEL_SETTLED,  'Patrol logs, environmental readings'),
        POIEntry(DEPTH_LEVEL_HIDDEN,   'Thread monitoring equipment, knowledge caches'),
        POIEntry(DEPTH_LEVEL_BURIED,   'Active Thread phenomena, Gap proximity'),
    ],
}


def poi_template_for(settlement_type: str) -> Optional[List[POIEntry]]:
    """§4.6 — return canonical POI template for a settlement type, or None
    for the §2.1 extra types (Village / Fortress-City / Cathedral-City).
    Per finding F18: §4.6 omits extra types, same gap class as F1/F7/F10/F11/F12/F14."""
    return POI_TEMPLATES_BY_SETTLEMENT_TYPE.get(settlement_type)


# [FINDING F18] §4.6 Settlement POI Templates omits §2.1 extra types
# (Village / Fortress-City / Cathedral-City). SEVENTH distinct surfacing
# of the type-taxonomy drift family (F1, F7, F10, F11, F12, F14, F18).
# Module 10 provisional fallback: Village -> Town POI template; composite
# types unmapped (surface as gap rather than silently reconcile).

PROVISIONAL_EXTRA_TYPE_POI_FALLBACK: Dict[str, Optional[str]] = {
    'Village':         'Town',
    'Fortress-City':   None,
    'Cathedral-City':  None,
}


def effective_poi_template_for(settlement: Settlement) -> Optional[List[POIEntry]]:
    """Sim-side effective POI template with F18 provisional fallback."""
    direct = poi_template_for(settlement.type)
    if direct is not None:
        return direct
    fallback = PROVISIONAL_EXTRA_TYPE_POI_FALLBACK.get(settlement.type)
    if fallback is None:
        return None
    return poi_template_for(fallback)


# ── §8.1 / §8.2 Audit catalogue (queryable for Module 13) ──────────────────

# Module 10 surfaces §8.1 + §8.2 as queryable data structures. Module 13
# integration audit will use these to verify that nothing in M1-M12
# violates the §8.2 invariants AND that the §8.1 impact predictions
# are met.

class ImpactSeverity(Enum):
    LOW = 'low'
    MODERATE = 'moderate'
    SIGNIFICANT = 'significant'


@dataclass(frozen=True)
class SystemImpact:
    """§8.1 impact entry."""
    system: str
    impact: str
    severity: ImpactSeverity


# [canonical: settlement_layer_v30 §8.1 Changes to Existing Systems table]
SYSTEM_IMPACTS_FROM_SETTLEMENT_LAYER: List[SystemImpact] = [
    SystemImpact(
        system='S03 Geography',
        impact='Province map unchanged. Settlement layer added beneath. Adjacency within provinces defined per §2.1.',
        severity=ImpactSeverity.MODERATE,
    ),
    SystemImpact(
        system='S04 Clocks',
        impact='IP recalibrated (halved baseline). Generational Shift clock added. All other clocks unchanged.',
        severity=ImpactSeverity.LOW,
    ),
    SystemImpact(
        system='S06 Faction Layer',
        impact='Provincial Authority slot formalized. Subnational management rights added. Domain Actions unchanged.',
        severity=ImpactSeverity.MODERATE,
    ),
    SystemImpact(
        system='S07 Victory',
        impact='Province Accord now derived from settlement Order averages. TCV unchanged.',
        severity=ImpactSeverity.MODERATE,
    ),
    SystemImpact(
        system='S09 Military',
        impact='Garrison at settlement level. Invasion sequence through settlements. Fortress chokepoints.',
        severity=ImpactSeverity.SIGNIFICANT,
    ),
    SystemImpact(
        system='S10 NPC',
        impact='Settlement governors are NPCs with Stance Triangles. Local actors added.',
        severity=ImpactSeverity.MODERATE,
    ),
    SystemImpact(
        system='S14 Fieldwork',
        impact='Fieldwork anchored to settlements. Depth Axis per settlement. Exposure per province.',
        severity=ImpactSeverity.LOW,
    ),
    SystemImpact(
        system='S15 Mass Combat',
        impact='Settlement Defense as pre-battle condition. Siege mechanics. Fortress bypass rules.',
        severity=ImpactSeverity.MODERATE,
    ),
    SystemImpact(
        system='S17 Scale Transitions',
        impact='Settlement governance action as new Zoom In entry point. Governor → Province → National as Domain Echo chain.',
        severity=ImpactSeverity.MODERATE,
    ),
    SystemImpact(
        system='Player Agency',
        impact='Governor as Duty. Settlement governance as scene action. Stature ladder revised with governance scope.',
        severity=ImpactSeverity.MODERATE,
    ),
    SystemImpact(
        system='Companions',
        impact='Companions can serve as settlement governors (dual role).',
        severity=ImpactSeverity.LOW,
    ),
]


# [canonical: settlement_layer_v30 §8.2 What Does NOT Change]
SYSTEM_INVARIANTS: List[str] = [
    'Province-level mechanics (Domain Actions, faction stats, Parliamentary votes) operate at province level.',
    'Personal-scale mechanics (combat, contests, Thread operations, fieldwork actions) operate at individual level.',
    'The dice engine, pool construction, Ob system, and degree table are unchanged.',
    'NPC Stance Triangles, Resonant Styles, Conviction Scars — unchanged.',
    'Clock pressures (MS, CI, IP) — unchanged in function, only IP rate adjusted.',
    'Calamity radiation — operates at province level per node distance.',
]


# ── Throughline coverage (audit-facing) ─────────────────────────────────────

THROUGHLINE_COVERAGE_BY_THIS_MODULE: Dict[str, str] = {
    'T-27': 'PRIMARY — Black markets + intel brokers are canonical "Effects Real, Explanation Wrong" cases.',
    'T-30': 'SECONDARY — Intel brokers gate information access through fieldwork.',
    'T-03': 'SECONDARY — Thread Exploitation Sites are substrate-grounded; harvesting affects peninsula RS.',
}

META_THROUGHLINE_COVERAGE_BY_THIS_MODULE: Dict[str, str] = {
    'М-7': 'PRIMARY — Black markets / intel brokers / thread sites are operational extensions emerging from institutional failure. Closes the second previously-unbound primary meta (after M9 closed М-1).',
    'М-8': 'SECONDARY — Information asymmetry via intel brokers.',
}


# ── Isolation tests ────────────────────────────────────────────────────────

def run_isolation_tests() -> Dict[str, str]:
    r: Dict[str, str] = {}

    # T1 — Black market emerges when Order ≤ 1
    stats_a = SettlementStats(prosperity=2, defense=2, order=1)
    r['T1_black_market_at_order_1'] = (
        'PASS' if predicate_black_market_emerges(stats_a, has_governor=True)
        else 'FAIL'
    )

    # T2 — Black market emerges when no governor (regardless of Order)
    stats_b = SettlementStats(prosperity=2, defense=2, order=4)
    r['T2_black_market_no_governor'] = (
        'PASS' if predicate_black_market_emerges(stats_b, has_governor=False)
        else 'FAIL'
    )

    # T3 — Black market does NOT emerge at Order ≥ 2 with governor
    stats_c = SettlementStats(prosperity=2, defense=2, order=2)
    r['T3_black_market_blocked_high_order'] = (
        'PASS' if not predicate_black_market_emerges(stats_c, has_governor=True)
        else 'FAIL'
    )

    # T4 — Black market disappears at Order ≥ 3
    # [canonical: §4.7 — "Disappearance: Automatic when settlement Order ≥ 3"]
    stats_d = SettlementStats(prosperity=2, defense=2, order=3)
    r['T4_black_market_disappears_at_order_3'] = (
        'PASS' if predicate_black_market_disappears(stats_d) else 'FAIL'
    )

    # T5 — Black market accrues half-units per season
    bm = BlackMarketState(settlement_id='S-001', active=True)
    accrue_black_market_effects(bm)
    accrue_black_market_effects(bm)
    # [canonical: §4.7 — "+0.5 Wealth" = 1 half-unit/season; over 2 seasons = 2 half-units = +1 Wealth]
    expected_wealth_after_two_seasons = 2
    expected_accord_loss_after_two_seasons = 2
    ok = (bm.half_wealth_accumulated == expected_wealth_after_two_seasons
          and bm.half_accord_lost == expected_accord_loss_after_two_seasons)
    r['T5_black_market_half_accrual'] = (
        'PASS' if ok else f'FAIL (wealth={bm.half_wealth_accumulated}, accord={bm.half_accord_lost})'
    )

    # T6 — Inactive black market doesn't accrue
    bm_inactive = BlackMarketState(settlement_id='S-002', active=False)
    accrue_black_market_effects(bm_inactive)
    r['T6_inactive_no_accrual'] = (
        'PASS' if bm_inactive.half_wealth_accumulated == 0 else 'FAIL'
    )

    # T7 — Intel broker emerges with Prosperity ≥ 3 + no governor
    stats_p3 = SettlementStats(prosperity=3, defense=2, order=2)
    r['T7_intel_broker_no_governor'] = (
        'PASS' if predicate_intel_broker_emerges(stats_p3, has_governor=False,
                                                   governor_stability=0)
        else 'FAIL'
    )

    # T8 — Intel broker emerges with Prosperity ≥ 3 + governor stability ≤ 2
    r['T8_intel_broker_low_stability_governor'] = (
        'PASS' if predicate_intel_broker_emerges(stats_p3, has_governor=True,
                                                   governor_stability=2)
        else 'FAIL'
    )

    # T9 — Intel broker blocked at low Prosperity
    stats_p2 = SettlementStats(prosperity=2, defense=2, order=2)
    r['T9_intel_broker_blocked_low_prosperity'] = (
        'PASS' if not predicate_intel_broker_emerges(stats_p2, has_governor=False,
                                                       governor_stability=0)
        else 'FAIL'
    )

    # T10 — Intel broker blocked with stable governor (Prosperity ≥ 3, gov stability ≥ 3)
    r['T10_intel_broker_blocked_stable_governor'] = (
        'PASS' if not predicate_intel_broker_emerges(stats_p3, has_governor=True,
                                                       governor_stability=3)
        else 'FAIL'
    )

    # T11 — Thread Exploitation Site present at Proximity ≤ 2
    r['T11_thread_site_at_proximity_2'] = (
        'PASS' if predicate_thread_exploitation_site_present(2) else 'FAIL'
    )

    # T12 — No thread site at Proximity 3+
    r['T12_no_thread_site_at_proximity_3'] = (
        'PASS' if not predicate_thread_exploitation_site_present(3) else 'FAIL'
    )

    # T13 — Harvesting site mutates state
    site = ThreadExploitationSite(settlement_id='S-001')
    result = harvest_thread_site(site, 'Niflhel')
    # [canonical: §4.9 — "Wealth +1 for harvesting faction"]
    expected_wealth_gain = 1
    ok = (result.success
          and result.treasury_delta == expected_wealth_gain
          and 'Niflhel' in site.discovered_by
          and site.times_harvested == 1)
    r['T13_thread_harvest_mutates_state'] = 'PASS' if ok else f'FAIL ({result}, {site})'

    # T14 — Repeated harvests accumulate
    harvest_thread_site(site, 'Niflhel')
    r['T14_thread_harvest_repeats_count'] = (
        'PASS' if site.times_harvested == 2 else 'FAIL'
    )

    # T15 — POI templates cover canonical-eight types
    expected_canonical_eight = {'Seat', 'City', 'Town', 'Fortress', 'Port', 'Cathedral', 'Mine', 'Outpost'}
    r['T15_poi_templates_canonical_eight'] = (
        'PASS' if set(POI_TEMPLATES_BY_SETTLEMENT_TYPE.keys()) == expected_canonical_eight
        else 'FAIL'
    )

    # T16 — Each canonical type has 4 depth-level POI entries (0-3)
    # [canonical: §4.6 — "Each settlement has 2-4 POIs across Depth levels";
    #  table shows 4 columns Depth 0/1/2/3+]
    expected_poi_count_per_type = 4
    ok = all(len(POI_TEMPLATES_BY_SETTLEMENT_TYPE[t]) == expected_poi_count_per_type
             for t in POI_TEMPLATES_BY_SETTLEMENT_TYPE)
    r['T16_each_type_has_four_depths'] = 'PASS' if ok else 'FAIL'

    # T17 — Seat depth-0 POI matches canon
    seat_poi = POI_TEMPLATES_BY_SETTLEMENT_TYPE['Seat']
    # [canonical: §4.6 Seat row Depth 0 — "Court, public buildings"]
    r['T17_seat_depth_0_canon'] = (
        'PASS' if 'Court' in seat_poi[0].description else 'FAIL'
    )

    # T18 — F18: extra types unmapped in canonical POI templates
    fake_village = Settlement(id='S-XXX', name='V', type='Village',
                              province='X', duchy='X', role='x')
    r['T18_extra_type_unmapped'] = (
        'PASS' if poi_template_for('Village') is None else 'FAIL'
    )

    # T19 — F18: Village falls back to Town in effective_poi_template_for
    eff_village = effective_poi_template_for(fake_village)
    eff_town = POI_TEMPLATES_BY_SETTLEMENT_TYPE['Town']
    r['T19_village_fallback_to_town'] = (
        'PASS' if eff_village == eff_town else 'FAIL'
    )

    # T20 — Fortress-City / Cathedral-City unmapped (F18 gap)
    fake_fc = Settlement(id='S-XXX', name='FC', type='Fortress-City',
                         province='X', duchy='X', role='x')
    fake_cc = Settlement(id='S-XXX', name='CC', type='Cathedral-City',
                         province='X', duchy='X', role='x')
    ok = (effective_poi_template_for(fake_fc) is None
          and effective_poi_template_for(fake_cc) is None)
    r['T20_composite_types_unmapped'] = 'PASS' if ok else 'FAIL'

    # T21 — System impact catalogue covers 11 systems per §8.1
    # [canonical: §8.1 — 11-row table]
    expected_impact_system_count = 11
    r['T21_system_impacts_count'] = (
        'PASS' if len(SYSTEM_IMPACTS_FROM_SETTLEMENT_LAYER) == expected_impact_system_count
        else f'FAIL ({len(SYSTEM_IMPACTS_FROM_SETTLEMENT_LAYER)})'
    )

    # T22 — Military severity is SIGNIFICANT per §8.1
    # [canonical: §8.1 Military row — "Significant — military granularity increased"]
    mil_impact = next(s for s in SYSTEM_IMPACTS_FROM_SETTLEMENT_LAYER
                       if 'Military' in s.system)
    r['T22_military_significant'] = (
        'PASS' if mil_impact.severity == ImpactSeverity.SIGNIFICANT else 'FAIL'
    )

    # T23 — Clocks severity is LOW per §8.1
    # [canonical: §8.1 Clocks row — "Low — one rate change, one new clock"]
    clk_impact = next(s for s in SYSTEM_IMPACTS_FROM_SETTLEMENT_LAYER
                       if 'Clocks' in s.system)
    r['T23_clocks_low'] = (
        'PASS' if clk_impact.severity == ImpactSeverity.LOW else 'FAIL'
    )

    # T24 — System invariants from §8.2 (six entries)
    # [canonical: §8.2 — six bullet items]
    expected_invariant_count = 6
    r['T24_invariants_count'] = (
        'PASS' if len(SYSTEM_INVARIANTS) == expected_invariant_count
        else f'FAIL ({len(SYSTEM_INVARIANTS)})'
    )

    # T25 — Throughline coverage table is queryable
    r['T25_throughline_coverage_queryable'] = (
        'PASS' if 'T-27' in THROUGHLINE_COVERAGE_BY_THIS_MODULE
        and 'PRIMARY' in THROUGHLINE_COVERAGE_BY_THIS_MODULE['T-27']
        else 'FAIL'
    )

    # T26 — Meta-throughline М-7 primary binding (closes second gap)
    r['T26_meta_m7_primary_closes_gap'] = (
        'PASS' if 'М-7' in META_THROUGHLINE_COVERAGE_BY_THIS_MODULE
        and 'PRIMARY' in META_THROUGHLINE_COVERAGE_BY_THIS_MODULE['М-7']
        else 'FAIL'
    )

    # T27 — Emergent composition with M6/M9: Order drops → black market emerges → governance failure cascade
    # Bottom-up: black market predicate is a pure function of state. M9's
    # Accounting hook + M6's unmanaged-settlement Order decrement composes
    # with this predicate.
    stats_chain = SettlementStats(prosperity=2, defense=2, order=2)
    # Initially no black market
    bm_active_before = predicate_black_market_emerges(stats_chain, has_governor=True)
    # M9 unmanaged-settlement decrement triggers (governor leaves) over 2 seasons
    from module_09_timeline import unmanaged_settlement_tick
    unmanaged_settlement_tick(stats_chain)   # Order 2 -> 1
    unmanaged_settlement_tick(stats_chain)   # Order 1 -> 0
    # Now Order=0, no governor
    bm_active_after = predicate_black_market_emerges(stats_chain, has_governor=False)
    ok = (not bm_active_before and bm_active_after)
    r['T27_emergent_governance_failure_to_black_market'] = (
        'PASS' if ok else f'FAIL (before={bm_active_before}, after={bm_active_after})'
    )

    return r


if __name__ == '__main__':
    import sys
    results = run_isolation_tests()
    width = max(len(k) for k in results)
    header = "Module 10 — dissolution emergence + POI templates + impact catalogue — isolation tests"
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
    print(f"Dissolution mechanisms: black markets, intel brokers, thread exploitation sites")
    print(f"POI templates: {len(POI_TEMPLATES_BY_SETTLEMENT_TYPE)} canonical-eight types")
    print(f"System impacts: {len(SYSTEM_IMPACTS_FROM_SETTLEMENT_LAYER)} systems affected")
    print(f"System invariants: {len(SYSTEM_INVARIANTS)} preserved")
    print(f"Throughline coverage: {sorted(THROUGHLINE_COVERAGE_BY_THIS_MODULE.keys())}")
    print(f"Meta-throughline: {sorted(META_THROUGHLINE_COVERAGE_BY_THIS_MODULE.keys())}")
    sys.exit(1 if fail else 0)
