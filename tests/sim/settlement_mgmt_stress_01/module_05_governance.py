# module_05_governance.py — Dual-authority governance (Part 3 of settlement_layer)
#
# Mode G Module five of settlement_mgmt_stress_01.
#
# Encodes:
#   §3.1 two-tier authority model (Provincial Authority + Settlement Governor)
#   §3.2 governor assignment by Standing tier; four governance actions
#        (Develop / Fortify / Pacify / Administer); player-as-governor mechanic;
#        NPC governor priority tree; Bishop-Governor sub-type
#   §3.3 seven subnational factions with natural-settlement-type alignment;
#        Grant / Revoke management Domain Actions; RM cell resilience;
#        Contested management via social contest
#
# This module brings the MAINTENANCE arm of the player-action loop live:
#   - Develop -> mutates Prosperity
#   - Fortify -> mutates Defense
#   - Pacify -> mutates Order
#   - Administer -> maintains Order this season (no decay); reveals NPC conviction
#
# And the GOVERNANCE-CHANGE problem-solve arm:
#   - grant_subnational_management(settlement, subnational_faction)
#   - revoke_subnational_management(settlement)
#
# Also UPGRADES the GovernorState stub from Module four to the canonical type
# and supplies the Governor-assignment Ob lookup for the non-pastoral
# install_church_governor path.
#
# Canonical sources (full read this session):
#   designs/territory/settlement_layer_v30.md (§3.1, §3.2, §3.3)
#
# Out of scope (deferred):
#   - faction_politics_expanded_v1 §1 Hall Tier spec — Module twelve binds it
#   - npc_behavior_v30 §8.2 Church NPC Priority Tree — Module twelve
#   - player_agency_v30 §3 Duty system — referenced but not encoded here
#   - social_contest_v30 §7 contested-management resolution — Module twelve
#   - settlement_bridge_unification C-04 companion-governor 1-free-action —
#     surfaced as constant; integration is Module twelve
#   - Standing ladder mechanics — Module eight (player progression)

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Tuple

from module_01_primitives import (
    Settlement, SettlementStats, by_id, STAT_MAX, STAT_MIN,
    CANONICAL_TYPES,
)
from module_02_hierarchy import (
    province_is_fractured, PoliticalValueComputation,
)
from module_03_facilities import ActionResult


# ── §3.2 Standing-tier governor eligibility ─────────────────────────────────

class GovernorStanding(Enum):
    """Per §3.2 standing-tier table. Tier names are the canonical labels."""
    OPERATIVE_AGENT = 'operative_agent'   # Standing 0-2: cannot govern
    COUNSELOR       = 'counselor'         # Standing 3
    LIEUTENANT      = 'lieutenant'        # Standing 4
    SUCCESSOR       = 'successor'         # Standing 5

# [canonical: settlement_layer_v30 §3.2 standing-tier table — first column]
# Numeric standing range floors for each tier
TIER_STANDING_MIN: Dict[GovernorStanding, int] = {
    GovernorStanding.OPERATIVE_AGENT: 0,   # "0-2 (Operative/Agent)"
    GovernorStanding.COUNSELOR:       3,   # "3 (Counselor)"
    GovernorStanding.LIEUTENANT:      4,   # "4 (Lieutenant)"
    GovernorStanding.SUCCESSOR:       5,   # "5 (Successor)"
}

# §3.2 — settlement types each standing tier is eligible to govern
# [canonical: settlement_layer_v30 §3.2 standing-tier table second column]
# Operative/Agent: not eligible (empty tuple)
# Counselor: Town or Outpost
# Lieutenant: City, Fortress, or Mine
# Successor: Seat or Cathedral (requires faction leader approval)
ELIGIBLE_TYPES_BY_TIER: Dict[GovernorStanding, Tuple[str, ...]] = {
    GovernorStanding.OPERATIVE_AGENT: (),
    GovernorStanding.COUNSELOR:       ('Town', 'Outpost'),
    GovernorStanding.LIEUTENANT:      ('City', 'Fortress', 'Mine'),
    GovernorStanding.SUCCESSOR:       ('Seat', 'Cathedral'),
}

# [canonical: settlement_layer_v30 §3.2 Successor row —
#  "Eligible for Governor of a Seat or Cathedral (requires faction leader approval)"]
SUCCESSOR_REQUIRES_LEADER_APPROVAL: bool = True


def tier_for_standing(standing: int) -> GovernorStanding:
    """Map a Standing value (0-5+) to its GovernorStanding tier per §3.2."""
    if standing >= TIER_STANDING_MIN[GovernorStanding.SUCCESSOR]:
        return GovernorStanding.SUCCESSOR
    if standing >= TIER_STANDING_MIN[GovernorStanding.LIEUTENANT]:
        return GovernorStanding.LIEUTENANT
    if standing >= TIER_STANDING_MIN[GovernorStanding.COUNSELOR]:
        return GovernorStanding.COUNSELOR
    return GovernorStanding.OPERATIVE_AGENT


def is_eligible_governor(standing: int, settlement_type: str) -> bool:
    """Per §3.2: can a candidate at this Standing govern a settlement of
    this type?

    Returns False for §2.1 extra types (Village, Fortress-City,
    Cathedral-City) — see finding F10 below.
    """
    tier = tier_for_standing(standing)
    return settlement_type in ELIGIBLE_TYPES_BY_TIER[tier]


# ── F10 — extra-type eligibility gap ────────────────────────────────────────

# [FINDING F10] §3.2's standing-tier eligibility table uses the §1.2
# canonical eight settlement types (Town / Outpost / City / Fortress /
# Mine / Seat / Cathedral). The §2.1 registry contains three extra types
# (Village / Fortress-City / Cathedral-City) — same gap as M3's F7. The
# canon does not say which standing tier can govern these types.
#
# Affected: 17 of 37 settlements (14 Villages + 1 Fortress-City + 1
# Cathedral-City).
#
# Module 5 surfaces the gap explicitly — is_eligible_governor returns
# False for any extra type, which prevents the silent-zero failure mode
# (any candidate appears ineligible, blocking governor assignment
# entirely). Module 13 Mode D should stress-test the gap. Module 5
# does NOT silently reconcile.
#
# Provisional mapping IF editorial decides to add rows (sim-side
# best-guess, not canonical):
#   Village         -> Counselor (analogous to Town)
#   Fortress-City   -> Successor (composite tier; canonical Cathedral-equivalent)
#   Cathedral-City  -> Successor (Himmelenger is the Confessor's seat)

PROVISIONAL_EXTRA_TYPE_ELIGIBILITY: Dict[str, Optional[GovernorStanding]] = {
    'Village':         GovernorStanding.COUNSELOR,
    'Fortress-City':   GovernorStanding.SUCCESSOR,
    'Cathedral-City':  GovernorStanding.SUCCESSOR,
}


# ── §3.2 four governance actions ────────────────────────────────────────────

class GovernanceAction(Enum):
    """The four canonical governance actions per §3.2 governance-action table."""
    DEVELOP    = 'develop'
    FORTIFY    = 'fortify'
    PACIFY     = 'pacify'
    ADMINISTER = 'administer'


# §3.2 Administer action's flat Ob
# [canonical: settlement_layer_v30 §3.2 governance-action table —
#  "Administer | Attunement + Governance History | 2 | Maintain Order"]
ADMINISTER_OB: int = 2

# §3.2 Pacify Ob formula floor — "min 1"
# [canonical: settlement_layer_v30 §3.2 governance-action table —
#  "Pacify | Charisma + local History | floor((3 − Order) + 1), min 1 | Order +1"]
PACIFY_OB_MIN: int = 1

# §3.2 Pacify Ob formula uses constant (3 - Order)
# [canonical: settlement_layer_v30 §3.2 Pacify row formula]
PACIFY_FORMULA_BASELINE: int = 3

# Develop / Fortify Ob formulas use floor(stat/2) + 1 — the +1 below
# [canonical: settlement_layer_v30 §3.2 Develop row formula —
#  "floor(Prosperity/2) + 1"]
DEVELOP_FORTIFY_FORMULA_OFFSET: int = 1


def develop_ob(prosperity: int) -> int:
    """§3.2 Develop Ob = floor(Prosperity/2) + 1.
    [canonical: settlement_layer_v30 §3.2 Develop row formula]
    """
    return (prosperity // 2) + DEVELOP_FORTIFY_FORMULA_OFFSET


def fortify_ob(defense: int) -> int:
    """§3.2 Fortify Ob = floor(Defense/2) + 1.
    [canonical: settlement_layer_v30 §3.2 Fortify row formula]
    """
    return (defense // 2) + DEVELOP_FORTIFY_FORMULA_OFFSET


def pacify_ob(order: int) -> int:
    """§3.2 Pacify Ob = floor((3 - Order) + 1), min 1.
    For integer Order the floor is mathematically redundant — see F9 below.
    [canonical: settlement_layer_v30 §3.2 Pacify row formula]
    """
    raw = (PACIFY_FORMULA_BASELINE - order) + DEVELOP_FORTIFY_FORMULA_OFFSET
    return max(PACIFY_OB_MIN, raw)


# ── F9 — Pacify Ob formula notational quirk (informational) ─────────────────

# [FINDING F9] §3.2 Pacify Ob is stated as "floor((3 − Order) + 1), min 1".
# For integer Order in [0, 5], the floor is mathematically redundant —
# (3 − Order) + 1 is an integer, and floor of an integer is the integer.
# The min-clamp at 1 IS load-bearing for Order >= 3 (where the raw value
# drops to 1 or below).
#
# Module 5 implements `(3 - order) + 1` clamped at 1 — same result as
# the canonical formula. F9 is informational only — no functional
# divergence from canon. Worth surfacing if editorial wants to clean the
# formula presentation.

# Worked-example test values for the Pacify formula:
# [canonical: derived from §3.2 Pacify formula]
PACIFY_OB_AT_ORDER_0: int = 4   # (3-0)+1 = 4
PACIFY_OB_AT_ORDER_3: int = 1   # (3-3)+1 = 1
PACIFY_OB_AT_ORDER_5: int = 1   # (3-5)+1 = -1, clamped to 1


# ── Action handler: governance action → settlement stat mutation ────────────

@dataclass(frozen=True)
class GovernanceActionResult:
    """Result of attempting a governance action. Extends ActionResult with
    governance-specific signals. Roll resolution (pool vs Ob) is upstream —
    Module 5 surfaces the Ob value and applies the success/failure effect."""
    action: GovernanceAction
    ob: int
    success: bool
    state_mutated: bool
    stat_delta: int                 # +1 for success on Develop/Fortify/Pacify
    administer_no_decay_flag: bool  # §3.2 Administer "Maintain Order (no decay this season)"
    reveals_conviction: bool        # §3.2 Administer "Reveals one local NPC's active Conviction"
    faction_standing_delta: int     # Module 12 binds magnitude; M5 sets direction
    renown_delta: int               # Module 8 binds magnitude; M5 sets direction


def execute_governance_action(
    action: GovernanceAction,
    stats: SettlementStats,
    pool_roll: int,
) -> GovernanceActionResult:
    """Execute a governance action. `pool_roll` is the player/NPC roll
    against the action's Ob. Mutates `stats` on success per §3.2 effect column.

    Develop / Fortify / Pacify on success: +1 to the respective stat, capped
    at STAT_MAX (5).
    Administer on success: maintains Order (no decay this season), reveals
    one NPC's Conviction.
    Failure: no state mutation, but turn is consumed.
    """
    if action == GovernanceAction.DEVELOP:
        ob = develop_ob(stats.prosperity)
        success = pool_roll >= ob
        if success and stats.prosperity < STAT_MAX:
            stats.prosperity = min(STAT_MAX, stats.prosperity + 1)
            return GovernanceActionResult(
                action=action, ob=ob, success=True, state_mutated=True,
                stat_delta=+1, administer_no_decay_flag=False,
                reveals_conviction=False,
                faction_standing_delta=+1, renown_delta=+1,
            )
        return GovernanceActionResult(
            action=action, ob=ob, success=success, state_mutated=False,
            stat_delta=0, administer_no_decay_flag=False,
            reveals_conviction=False,
            faction_standing_delta=0, renown_delta=0,
        )
    if action == GovernanceAction.FORTIFY:
        ob = fortify_ob(stats.defense)
        success = pool_roll >= ob
        if success and stats.defense < STAT_MAX:
            stats.defense = min(STAT_MAX, stats.defense + 1)
            return GovernanceActionResult(
                action=action, ob=ob, success=True, state_mutated=True,
                stat_delta=+1, administer_no_decay_flag=False,
                reveals_conviction=False,
                faction_standing_delta=+1, renown_delta=+1,
            )
        return GovernanceActionResult(
            action=action, ob=ob, success=success, state_mutated=False,
            stat_delta=0, administer_no_decay_flag=False,
            reveals_conviction=False,
            faction_standing_delta=0, renown_delta=0,
        )
    if action == GovernanceAction.PACIFY:
        ob = pacify_ob(stats.order)
        success = pool_roll >= ob
        if success and stats.order < STAT_MAX:
            stats.order = min(STAT_MAX, stats.order + 1)
            return GovernanceActionResult(
                action=action, ob=ob, success=True, state_mutated=True,
                stat_delta=+1, administer_no_decay_flag=False,
                reveals_conviction=False,
                faction_standing_delta=+1, renown_delta=+1,
            )
        return GovernanceActionResult(
            action=action, ob=ob, success=success, state_mutated=False,
            stat_delta=0, administer_no_decay_flag=False,
            reveals_conviction=False,
            faction_standing_delta=0, renown_delta=0,
        )
    if action == GovernanceAction.ADMINISTER:
        ob = ADMINISTER_OB
        success = pool_roll >= ob
        return GovernanceActionResult(
            action=action, ob=ob, success=success,
            state_mutated=success,                # state-mutated means the
                                                  # no-decay flag was set
            stat_delta=0,
            administer_no_decay_flag=success,
            reveals_conviction=success,
            faction_standing_delta=(+1 if success else 0),
            renown_delta=0,                       # Administer is invisible work;
                                                  # no renown gain
        )
    raise ValueError(f'unknown action: {action}')


# ── §3.3 Subnational faction alignment ──────────────────────────────────────

class SubnationalFaction(Enum):
    """Per §3.3 — seven subnational factions."""
    CHURCH       = 'church'
    GUILDS       = 'guilds'
    MINISTRY     = 'ministry'
    LOEWENRITTER = 'loewenritter'
    RM           = 'rm'
    WARDENS      = 'wardens'
    NIFLHEL      = 'niflhel'


# §3.3 natural-settlement-type alignment per faction
# [canonical: settlement_layer_v30 §3.3 subnational-faction table]
NATURAL_SETTLEMENT_TYPES: Dict[SubnationalFaction, Tuple[str, ...]] = {
    SubnationalFaction.CHURCH:       ('Cathedral',),
    # Guilds: "City, Port, Market, Mine" — Market is district-level, not
    # in §1.2 canonical types post-PP-726; Module 5 omits it from the
    # natural-types tuple (the §3.3 mention reflects pre-PP-726 era when
    # Market was a settlement-type). Cited gap surfaced as F11.
    SubnationalFaction.GUILDS:       ('City', 'Port', 'Mine'),
    SubnationalFaction.MINISTRY:     ('Seat', 'City'),
    SubnationalFaction.LOEWENRITTER: ('Fortress',),
    # RM: "Outpost, Town (in low-CV territories)"; the "low-CV" precondition
    # is province-level state, not a type-table entry. M5 surfaces the
    # natural types; the low-CV precondition is checked by upstream callers.
    SubnationalFaction.RM:           ('Outpost', 'Town'),
    # Wardens: "Outpost (Askeheim, Stillhelm Watch)" — specific Outposts
    # in specific provinces. M5 lists the type; province-specific filter
    # is upstream.
    SubnationalFaction.WARDENS:      ('Outpost',),
    # Niflhel: "Any (covert)" — universal type-alignment via covert insertion
    SubnationalFaction.NIFLHEL:      tuple(CANONICAL_TYPES),  # "Any"
}


# ── F11 — §3.3 references pre-PP-726 type 'Market' ──────────────────────────

# [FINDING F11] §3.3 Guilds row lists natural settlement types as "City,
# Port, Market, Mine". Market is NOT in §1.2's canonical type list (which
# has 8 types: Seat / City / Town / Fortress / Port / Cathedral / Mine /
# Outpost). Per PP-726, Market is a sub-feature (district within a
# settlement), not a settlement type itself — see settlement_layer_v30
# §2.2 sub-features registry.
#
# Module 5 surfaces this by omitting Market from the Guilds natural-types
# tuple. Editorial decision: §3.3 Guilds row should be amended to
# "City, Port, Mine" (and Market access handled at sub-feature level), OR
# Market should be promoted to §1.2 as a settlement type (unlikely given
# PP-726's siege-target rationale — Market is sub-settlement).


# ── §3.3 management effects ─────────────────────────────────────────────────

@dataclass(frozen=True)
class SubnationalManagementEffect:
    """Per-faction management effects per §3.3 'Management Effect' column."""
    per_season_resource_delta: Dict[str, int]   # e.g. {'piety_influence': 1}
    order_decay_modifier: int                    # negative = slower decay
    passive_defense_bonus: int
    detection_band_shift: int                    # Warden RS-detection earlier
    governor_primary_stat: Optional[str]
    province_retains_taxation: bool
    province_retains_military_legal: bool
    is_covert: bool                              # Niflhel / RM in low-CV


# [canonical: settlement_layer_v30 §3.3 subnational-faction management-effect table]
MANAGEMENT_EFFECTS: Dict[SubnationalFaction, SubnationalManagementEffect] = {
    # Church row: "+1 Piety Influence per season. Church governor uses
    # Church stats, not province faction stats. Province faction retains
    # taxation rights."
    SubnationalFaction.CHURCH: SubnationalManagementEffect(
        per_season_resource_delta={'piety_influence': 1},
        order_decay_modifier=0,
        passive_defense_bonus=0,
        detection_band_shift=0,
        governor_primary_stat=None,   # "Church stats" — Module 12 binds
        province_retains_taxation=True,
        province_retains_military_legal=True,
        is_covert=False,
    ),
    # Guilds row: "+1 Trade per season. Guild governor uses Wealth as primary
    # stat. Province faction retains military and legal authority."
    SubnationalFaction.GUILDS: SubnationalManagementEffect(
        per_season_resource_delta={'trade': 1},
        order_decay_modifier=0,
        passive_defense_bonus=0,
        detection_band_shift=0,
        governor_primary_stat='Wealth',
        province_retains_taxation=True,
        province_retains_military_legal=True,
        is_covert=False,
    ),
    # Ministry row: "Administrative efficiency: Order decay −1 (Order is
    # more stable). Governor uses Influence as primary stat."
    SubnationalFaction.MINISTRY: SubnationalManagementEffect(
        per_season_resource_delta={},
        order_decay_modifier=-1,
        passive_defense_bonus=0,
        detection_band_shift=0,
        governor_primary_stat='Influence',
        province_retains_taxation=True,
        province_retains_military_legal=True,
        is_covert=False,
    ),
    # Löwenritter row: "Military efficiency: Defense +1 passive.
    # Löwenritter governor uses Military as primary stat. Province faction
    # retains legal authority but military operations defer to Löwenritter."
    SubnationalFaction.LOEWENRITTER: SubnationalManagementEffect(
        per_season_resource_delta={},
        order_decay_modifier=0,
        passive_defense_bonus=1,
        detection_band_shift=0,
        governor_primary_stat='Military',
        province_retains_taxation=True,
        province_retains_military_legal=False,   # "military operations defer"
        is_covert=False,
    ),
    # RM row: "Community presence: CV −1 potential per season ...
    # Only available in territories with PT ≤ 2. Province faction may not
    # know RM is managing the settlement (covert management)."
    SubnationalFaction.RM: SubnationalManagementEffect(
        per_season_resource_delta={'cv_potential': -1},
        order_decay_modifier=0,
        passive_defense_bonus=0,
        detection_band_shift=0,
        governor_primary_stat=None,
        province_retains_taxation=True,
        province_retains_military_legal=True,
        is_covert=True,
    ),
    # Wardens row: "Thread monitoring: RS effects detected 1 band earlier.
    # Warden governor operates independently."
    SubnationalFaction.WARDENS: SubnationalManagementEffect(
        per_season_resource_delta={},
        order_decay_modifier=0,
        passive_defense_bonus=0,
        detection_band_shift=1,
        governor_primary_stat=None,
        province_retains_taxation=True,
        province_retains_military_legal=True,
        is_covert=False,
    ),
    # Niflhel row: covert; no governance; Intel-gathering at +1D
    SubnationalFaction.NIFLHEL: SubnationalManagementEffect(
        per_season_resource_delta={},
        order_decay_modifier=0,
        passive_defense_bonus=0,
        detection_band_shift=0,
        governor_primary_stat=None,
        province_retains_taxation=True,
        province_retains_military_legal=True,
        is_covert=True,
    ),
}


# §3.3 RM cell-resilience threshold
# [canonical: settlement_layer_v30 §3.3 RM Cell Resilience —
#  "If RM has Presence markers in ≥ 3 settlements within a province,
#  Church/Crown suppression actions against RM in that province take +1 Ob"]
RM_RESILIENCE_PRESENCE_THRESHOLD: int = 3
RM_RESILIENCE_OB_DELTA: int = 1


# §3.3 RM "low-CV" precondition
# [canonical: settlement_layer_v30 §3.3 RM row —
#  "Only available in territories with PT ≤ 2"]
RM_NATURAL_PT_THRESHOLD: int = 2


# §3.3 Niflhel investigation threshold
# [canonical: settlement_layer_v30 §3.3 Niflhel row —
#  "Detection: province faction may discover Niflhel presence via
#  Investigation (Evidence Track threshold 3)"]
NIFLHEL_DETECTION_EVIDENCE_THRESHOLD: int = 3


# §3.3 Grant Management Ob
# [canonical: settlement_layer_v30 §3.3 —
#  "as a Domain Action (Influence, Ob 1 — it is an administrative act, not
#  a contested one)"]
GRANT_MANAGEMENT_OB: int = 1


# §3.3 Revoke Management costs
# [canonical: settlement_layer_v30 §3.3 —
#  "Revocation costs Order −1 in the settlement (the population perceives
#  institutional disruption) and Disposition −2 with the subnational
#  faction's leadership"]
REVOKE_MANAGEMENT_ORDER_COST: int = 1
REVOKE_MANAGEMENT_DISPOSITION_COST: int = 2


def revoke_management_ob(subnational_influence: int) -> int:
    """§3.3 Revoke Management Ob = subnational faction's Influence ÷ 2,
    rounded up.
    [canonical: settlement_layer_v30 §3.3 —
     "Influence, Ob = subnational faction's Influence ÷ 2, round up"]
    """
    return (subnational_influence + 1) // 2   # ceiling division for positive int


# ── Canonical GovernorState (upgrades Module 4 stub) ────────────────────────

@dataclass
class GovernorState:
    """Canonical governor-presence state per §3.1 + §3.2. Replaces and
    extends the Module 4 stub. Modules 4 and 5 share the type by name —
    M4 imports the stub from this module starting M5 (lazy upgrade pattern
    works because M4 only uses `has_governor`)."""
    settlement_id: str
    has_governor: bool
    current_order: int
    governor_standing: int = 0                 # 0-5+ Standing ladder per §3.2
    governor_is_player: bool = False
    governor_is_companion: bool = False
    governor_is_bishop: bool = False           # §3.2 Bishop-Governor sub-type
    managing_subnational: Optional[SubnationalFaction] = None
    leader_approval_granted: bool = False      # §3.2 Successor requirement


def can_assign_governor(
    candidate_standing: int,
    settlement: Settlement,
    leader_approval_granted: bool = False,
) -> Tuple[bool, str]:
    """§3.2 governor-assignment eligibility check. Returns (ok, reason)."""
    tier = tier_for_standing(candidate_standing)
    if tier == GovernorStanding.OPERATIVE_AGENT:
        return (False, 'standing_too_low')
    eligible_types = ELIGIBLE_TYPES_BY_TIER[tier]
    if settlement.type not in eligible_types:
        return (False, f'tier_{tier.value}_not_eligible_for_type_{settlement.type}')
    if (tier == GovernorStanding.SUCCESSOR
            and SUCCESSOR_REQUIRES_LEADER_APPROVAL
            and not leader_approval_granted):
        return (False, 'successor_requires_leader_approval')
    return (True, 'eligible')


# ── §3.3 grant / revoke management Domain Actions ───────────────────────────

def grant_subnational_management(
    governor_state: GovernorState,
    subnational: SubnationalFaction,
    settlement: Settlement,
) -> ActionResult:
    """§3.3 Grant Management Domain Action — Influence, Ob 1.
    Reassigns settlement management to a subnational faction; province
    retains Provincial Authority per §3.1.
    """
    if governor_state.managing_subnational == subnational:
        return ActionResult(success=False, reason='already_granted')
    # No natural-type check here — §3.3 explicitly says "may grant" without
    # restricting to natural types. The natural-type table is for default
    # alignment, not required alignment.
    governor_state.managing_subnational = subnational
    return ActionResult(
        success=True,
        reason=f'granted_to_{subnational.value}',
        state_mutated=True,
        faction_standing_delta=+1,
        renown_delta=0,   # administrative act; no renown gain
    )


def revoke_subnational_management(
    governor_state: GovernorState,
    stats: SettlementStats,
    subnational_influence: int,
    roll: int,
) -> ActionResult:
    """§3.3 Revoke Management Domain Action.
    Ob = ceil(subnational_influence / 2). On success: removes subnational
    management; Order −1; Disposition −2 with subnational leadership.
    """
    if governor_state.managing_subnational is None:
        return ActionResult(success=False, reason='no_subnational_to_revoke')
    ob = revoke_management_ob(subnational_influence)
    if roll < ob:
        return ActionResult(success=False, reason=f'roll_below_ob_{ob}')
    revoked = governor_state.managing_subnational
    governor_state.managing_subnational = None
    # Apply Order cost (clamped at STAT_MIN)
    new_order = max(STAT_MIN, stats.order - REVOKE_MANAGEMENT_ORDER_COST)
    stats.order = new_order
    return ActionResult(
        success=True,
        reason=f'revoked_from_{revoked.value}',
        state_mutated=True,
        faction_standing_delta=-REVOKE_MANAGEMENT_DISPOSITION_COST,
        renown_delta=0,
    )


# ── RM cell-resilience check ────────────────────────────────────────────────

def rm_suppression_ob_modifier(rm_presence_count_in_province: int) -> int:
    """§3.3 RM cell-resilience modifier.
    If ≥ RM_RESILIENCE_PRESENCE_THRESHOLD settlements have RM presence
    within a province, suppression actions take +RM_RESILIENCE_OB_DELTA Ob.
    """
    if rm_presence_count_in_province >= RM_RESILIENCE_PRESENCE_THRESHOLD:
        return RM_RESILIENCE_OB_DELTA
    return 0


# ── Companion-governor free-action allowance ────────────────────────────────

# [canonical: settlement_layer_v30 §3.2 —
#  "Companion-governor (per settlement_bridge_unification C-04): A companion
#  serving as governor gets 1 free action per season — social OR governance,
#  player chooses. Not both."]
COMPANION_GOVERNOR_FREE_ACTIONS_PER_SEASON: int = 1


# ── Isolation tests ─────────────────────────────────────────────────────────

def run_isolation_tests() -> Dict[str, str]:
    r: Dict[str, str] = {}

    # T1 — four GovernorStanding tiers exist
    # [canonical: §3.2 standing-tier table — four rows]
    expected_tier_count = 4
    r['T1_four_standing_tiers'] = (
        'PASS' if len(GovernorStanding) == expected_tier_count else 'FAIL'
    )

    # T2 — tier_for_standing maps standing 0-5 correctly
    ok = (tier_for_standing(0) == GovernorStanding.OPERATIVE_AGENT
          and tier_for_standing(2) == GovernorStanding.OPERATIVE_AGENT
          and tier_for_standing(3) == GovernorStanding.COUNSELOR
          and tier_for_standing(4) == GovernorStanding.LIEUTENANT
          and tier_for_standing(5) == GovernorStanding.SUCCESSOR)
    r['T2_tier_for_standing_mapping'] = 'PASS' if ok else 'FAIL'

    # T3 — eligibility table matches §3.2 exactly
    ok = (set(ELIGIBLE_TYPES_BY_TIER[GovernorStanding.COUNSELOR]) == {'Town', 'Outpost'}
          and set(ELIGIBLE_TYPES_BY_TIER[GovernorStanding.LIEUTENANT]) == {'City', 'Fortress', 'Mine'}
          and set(ELIGIBLE_TYPES_BY_TIER[GovernorStanding.SUCCESSOR]) == {'Seat', 'Cathedral'}
          and ELIGIBLE_TYPES_BY_TIER[GovernorStanding.OPERATIVE_AGENT] == ())
    r['T3_eligibility_table_matches_canon'] = 'PASS' if ok else 'FAIL'

    # T4 — Standing 0 cannot govern anything
    r['T4_standing_0_cannot_govern'] = (
        'PASS' if not is_eligible_governor(0, 'Town') else 'FAIL'
    )

    # T5 — Counselor (Std 3) can govern Town but not City
    ok = (is_eligible_governor(3, 'Town')
          and not is_eligible_governor(3, 'City'))
    r['T5_counselor_eligibility'] = 'PASS' if ok else 'FAIL'

    # T6 — Successor (Std 5) can govern Seat
    r['T6_successor_eligibility'] = (
        'PASS' if is_eligible_governor(5, 'Seat') else 'FAIL'
    )

    # T7 — F10 — extra types (Village, Fortress-City, Cathedral-City)
    # NOT eligible via canon at any standing
    ok = (not is_eligible_governor(5, 'Village')
          and not is_eligible_governor(5, 'Fortress-City')
          and not is_eligible_governor(5, 'Cathedral-City'))
    r['T7_extra_types_unmapped'] = 'PASS' if ok else 'FAIL'

    # T8 — Develop Ob formula at Prosperity 0
    # [canonical: §3.2 Develop formula — Ob(0) = floor(0/2) + 1 = 0 + 1 = 1]
    expected_develop_ob_at_0 = 1
    r['T8_develop_ob_at_0'] = (
        'PASS' if develop_ob(0) == expected_develop_ob_at_0 else f'FAIL ({develop_ob(0)})'
    )

    # T9 — Develop Ob formula at Prosperity 4
    # [canonical: §3.2 Develop formula — Ob(4) = floor(4/2) + 1 = 2 + 1 = 3]
    expected_develop_ob_at_4 = 3
    r['T9_develop_ob_at_4'] = (
        'PASS' if develop_ob(4) == expected_develop_ob_at_4 else f'FAIL ({develop_ob(4)})'
    )

    # T10 — Fortify Ob mirrors Develop formula
    # [canonical: §3.2 Fortify formula — Ob(3) = floor(3/2) + 1 = 1 + 1 = 2]
    expected_fortify_ob_at_3 = 2
    r['T10_fortify_ob_at_3'] = (
        'PASS' if fortify_ob(3) == expected_fortify_ob_at_3 else f'FAIL ({fortify_ob(3)})'
    )

    # T11 — Pacify Ob at Order 0 (high difficulty)
    # [canonical: §3.2 Pacify formula at Order 0 — (3-0)+1 = 4]
    r['T11_pacify_ob_at_order_0'] = (
        'PASS' if pacify_ob(0) == PACIFY_OB_AT_ORDER_0 else f'FAIL ({pacify_ob(0)})'
    )

    # T12 — Pacify Ob at Order 3 (mid)
    r['T12_pacify_ob_at_order_3'] = (
        'PASS' if pacify_ob(3) == PACIFY_OB_AT_ORDER_3 else f'FAIL ({pacify_ob(3)})'
    )

    # T13 — Pacify Ob at Order 5 clamps at min 1
    r['T13_pacify_ob_clamps_at_min_1'] = (
        'PASS' if pacify_ob(5) == PACIFY_OB_AT_ORDER_5 else f'FAIL ({pacify_ob(5)})'
    )

    # T14 — Administer Ob is flat 2
    r['T14_administer_ob_flat_2'] = 'PASS' if ADMINISTER_OB == 2 else 'FAIL'

    # T15 — Develop success increments Prosperity
    stats_a = SettlementStats(prosperity=2, defense=1, order=2)
    result = execute_governance_action(GovernanceAction.DEVELOP, stats_a, pool_roll=5)
    # [canonical: §3.2 Develop effect — Prosperity +1 on success]
    expected_prosperity_after_develop = 3
    r['T15_develop_success_increments'] = (
        'PASS' if result.success and stats_a.prosperity == expected_prosperity_after_develop
        else f'FAIL ({result}, prosperity={stats_a.prosperity})'
    )

    # T16 — Develop at STAT_MAX clamps (no further increase)
    stats_b = SettlementStats(prosperity=STAT_MAX, defense=1, order=2)
    result = execute_governance_action(GovernanceAction.DEVELOP, stats_b, pool_roll=5)
    r['T16_develop_clamps_at_max'] = (
        'PASS' if stats_b.prosperity == STAT_MAX else f'FAIL ({stats_b.prosperity})'
    )

    # T17 — Pacify success increments Order
    stats_c = SettlementStats(prosperity=1, defense=1, order=1)
    result = execute_governance_action(GovernanceAction.PACIFY, stats_c, pool_roll=5)
    # [canonical: §3.2 Pacify effect — Order +1]
    expected_order_after_pacify = 2
    r['T17_pacify_success_increments'] = (
        'PASS' if result.success and stats_c.order == expected_order_after_pacify
        else f'FAIL ({result}, order={stats_c.order})'
    )

    # T18 — Administer success sets no-decay flag
    stats_d = SettlementStats(prosperity=1, defense=1, order=3)
    result = execute_governance_action(GovernanceAction.ADMINISTER, stats_d, pool_roll=5)
    r['T18_administer_success_sets_flag'] = (
        'PASS' if result.success
        and result.administer_no_decay_flag
        and result.reveals_conviction
        and stats_d.order == 3   # Order unchanged
        else f'FAIL ({result})'
    )

    # T19 — Develop failure: no state mutation
    stats_e = SettlementStats(prosperity=4, defense=1, order=2)
    # Develop Ob at Prosperity 4 = 3; pool_roll=2 fails
    result = execute_governance_action(GovernanceAction.DEVELOP, stats_e, pool_roll=2)
    r['T19_develop_failure_no_mutation'] = (
        'PASS' if not result.success and stats_e.prosperity == 4 else f'FAIL'
    )

    # T20 — Subnational factions: seven canonical entries
    # [canonical: §3.3 table — seven rows]
    expected_subnational_count = 7
    r['T20_seven_subnational_factions'] = (
        'PASS' if len(SubnationalFaction) == expected_subnational_count else 'FAIL'
    )

    # T21 — Church natural type is Cathedral only
    r['T21_church_natural_cathedral'] = (
        'PASS' if NATURAL_SETTLEMENT_TYPES[SubnationalFaction.CHURCH] == ('Cathedral',)
        else 'FAIL'
    )

    # T22 — F11: Guilds natural types exclude Market (pre-PP-726)
    guild_types = set(NATURAL_SETTLEMENT_TYPES[SubnationalFaction.GUILDS])
    r['T22_guilds_excludes_market_F11'] = (
        'PASS' if 'Market' not in guild_types else 'FAIL'
    )

    # T23 — Ministry management gives order_decay_modifier -1
    # [canonical: §3.3 Ministry row — "Order decay −1"]
    expected_ministry_decay_mod = -1
    r['T23_ministry_decay_modifier'] = (
        'PASS' if MANAGEMENT_EFFECTS[SubnationalFaction.MINISTRY].order_decay_modifier == expected_ministry_decay_mod
        else 'FAIL'
    )

    # T24 — Löwenritter management gives Defense +1 passive
    # [canonical: §3.3 Löwenritter row — "Defense +1 passive"]
    expected_loew_defense_bonus = 1
    r['T24_loewenritter_defense_bonus'] = (
        'PASS' if MANAGEMENT_EFFECTS[SubnationalFaction.LOEWENRITTER].passive_defense_bonus == expected_loew_defense_bonus
        else 'FAIL'
    )

    # T25 — Wardens detection-band shift = 1
    # [canonical: §3.3 Wardens row — "RS effects detected 1 band earlier"]
    expected_warden_band_shift = 1
    r['T25_wardens_detection_shift'] = (
        'PASS' if MANAGEMENT_EFFECTS[SubnationalFaction.WARDENS].detection_band_shift == expected_warden_band_shift
        else 'FAIL'
    )

    # T26 — RM and Niflhel are covert
    r['T26_rm_niflhel_covert'] = (
        'PASS' if MANAGEMENT_EFFECTS[SubnationalFaction.RM].is_covert
        and MANAGEMENT_EFFECTS[SubnationalFaction.NIFLHEL].is_covert
        else 'FAIL'
    )

    # T27 — Löwenritter province does NOT retain military_legal
    r['T27_loewenritter_military_defer'] = (
        'PASS' if not MANAGEMENT_EFFECTS[SubnationalFaction.LOEWENRITTER].province_retains_military_legal
        else 'FAIL'
    )

    # T28 — Grant management Ob is 1
    r['T28_grant_management_ob_1'] = (
        'PASS' if GRANT_MANAGEMENT_OB == 1 else 'FAIL'
    )

    # T29 — Revoke management Ob = ceil(Influence / 2)
    # [canonical: §3.3 — "Influence ÷ 2, round up"]
    expected_revoke_ob_at_influence_5 = 3
    expected_revoke_ob_at_influence_4 = 2
    ok = (revoke_management_ob(5) == expected_revoke_ob_at_influence_5
          and revoke_management_ob(4) == expected_revoke_ob_at_influence_4)
    r['T29_revoke_management_ob_ceil'] = 'PASS' if ok else 'FAIL'

    # T30 — Grant management action handler succeeds
    seat_settlement = by_id('S-001')
    gov_a = GovernorState(
        settlement_id='S-001', has_governor=True, current_order=3,
        governor_standing=4,
    )
    result_act = grant_subnational_management(gov_a, SubnationalFaction.MINISTRY, seat_settlement)
    r['T30_grant_management_succeeds'] = (
        'PASS' if result_act.success
        and gov_a.managing_subnational == SubnationalFaction.MINISTRY
        else f'FAIL ({result_act})'
    )

    # T31 — Revoke management applies Order -1
    stats_f = SettlementStats(prosperity=3, defense=2, order=3)
    gov_b = GovernorState(
        settlement_id='S-001', has_governor=True, current_order=3,
        governor_standing=4,
        managing_subnational=SubnationalFaction.MINISTRY,
    )
    # Subnational influence 4; Ob = 2; roll 3 succeeds
    result_act = revoke_subnational_management(gov_b, stats_f,
                                                subnational_influence=4, roll=3)
    # [canonical: §3.3 — "Revocation costs Order −1"]
    expected_order_post_revoke = 2
    ok = (result_act.success
          and gov_b.managing_subnational is None
          and stats_f.order == expected_order_post_revoke)
    r['T31_revoke_costs_order_1'] = (
        'PASS' if ok else f'FAIL ({result_act}, order={stats_f.order})'
    )

    # T32 — Revoke management fails on roll < Ob
    gov_c = GovernorState(
        settlement_id='S-001', has_governor=True, current_order=3,
        governor_standing=4,
        managing_subnational=SubnationalFaction.MINISTRY,
    )
    stats_g = SettlementStats(prosperity=3, defense=2, order=3)
    # Subnational influence 8; Ob = 4; roll 2 fails — no state mutation
    result_act = revoke_subnational_management(gov_c, stats_g,
                                                subnational_influence=8, roll=2)
    r['T32_revoke_fails_low_roll'] = (
        'PASS' if not result_act.success
        and gov_c.managing_subnational == SubnationalFaction.MINISTRY
        and stats_g.order == 3
        else f'FAIL ({result_act})'
    )

    # T33 — RM cell resilience triggers at threshold (≥ 3 settlements)
    # [canonical: §3.3 RM Cell Resilience — "Presence markers in ≥ 3 settlements"]
    ok = (rm_suppression_ob_modifier(2) == 0
          and rm_suppression_ob_modifier(3) == RM_RESILIENCE_OB_DELTA
          and rm_suppression_ob_modifier(5) == RM_RESILIENCE_OB_DELTA)
    r['T33_rm_cell_resilience'] = 'PASS' if ok else 'FAIL'

    # T34 — Successor eligibility blocked without leader approval
    seat = by_id('S-001')   # Valorsplatz, Seat
    ok, reason = can_assign_governor(5, seat, leader_approval_granted=False)
    r['T34_successor_blocked_no_approval'] = (
        'PASS' if not ok and reason == 'successor_requires_leader_approval'
        else f'FAIL ({reason})'
    )

    # T35 — Successor eligibility succeeds with leader approval
    ok, reason = can_assign_governor(5, seat, leader_approval_granted=True)
    r['T35_successor_succeeds_with_approval'] = (
        'PASS' if ok else f'FAIL ({reason})'
    )

    return r


if __name__ == '__main__':
    import sys
    results = run_isolation_tests()
    width = max(len(k) for k in results)
    header = "Module 05 — dual-authority governance — isolation tests"
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
    print(f"Governance actions: {[a.value for a in GovernanceAction]}")
    print(f"Subnational factions: {len(SubnationalFaction)}")
    print(f"Standing tiers: {[t.value for t in GovernorStanding]}")
    sys.exit(1 if fail else 0)
