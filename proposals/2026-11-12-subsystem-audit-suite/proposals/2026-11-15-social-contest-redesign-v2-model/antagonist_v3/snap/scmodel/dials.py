"""The dials: `controls()` = PLAN B24p.04's control column (part22_b24p.md:140); `shipped()` = PLAN B24p.23's
(part22_b24p_cont.md:187-188) = RD B's shipped columns, EXCEPT where the plan leaves a setting at control
(`reading_kept`, `presumption_level`, `strike_level`: left for B98). The plan governs (G17).

Both sets carry B05's values at B05.23's shipped arm (pool_add 6, pool_floor 5, opposition_rate MU_PER_DIE,
difficulty_ob half arm, regard_step 1.0, reception_gain 1.0, favour_level major, proof_level minor) and the live
fixtures (pool_default 2, obstacle_ceiling 2, ceiling_per_pool True, obstacle_refusal_multiple 2): B24p's controls are
taken against B05's close (G18). Plus the three tables the plan tunes as "pointer rows": `audience_room`,
`speech_blend` (content classes + venue bias) and `standard_demand`.
"""
from __future__ import annotations

from types import MappingProxyType

from . import data
from .dice import MU_PER_DIE

_B05 = dict(
    pool_add=6, pool_floor=5, pool_default=2, opposition_rate=MU_PER_DIE,
    obstacle_ceiling=2.0, ceiling_per_pool=True, obstacle_refusal_multiple=2.0,
    attribute_mid=4.0, attribute_floor=1.0, attribute_ceiling=7.0,     # descriptors: 1..7 (read live: 1, 7)
    difficulty_ob=dict(data.DIFFICULTY_OB_SHIPPED),
    stakes_ob=dict(data.STAKES_OB_CONTROL),                            # B98's, not B24p's (G19)
    reception_gain=1.0, regard_step=1.0, favour_level="major", proof_level="minor",
)

_CONTROL = dict(
    # Focus (RD B.1 table)
    off_topic_step=0.0, divert_pull=0.0, divert_gain=0.0, rattle_pull=0.0, strike_level=None,
    # Reason (RD B.2)
    proofs_per_reason=None, account_step=0.0, account_max=0.9,
    # Attunement (RD B.3)
    fit_level=None, misfit_level=None, read_ob=1.4, read_scale=1.0, read_blur=1.0, guard_step=0.0,
    reading_kept=False,
    # Presence (RD B.4)
    delivery_step=0.0, heard_step=0.0, heard_floor=1.0,
    # Grace (RD B.5)
    standard_step=0.0, standard_demand=dict(data.STANDARD_DEMAND_CONTROL), respect_step=0.0, mark_level=None,
    cover_step=0.0, cover_max=0.9, mark_shame=0.0,
    # Will (RD B.6)
    press_base=1.0, blow_gain=0.0, sore_gain=0.0, strain_carry=0.0, mark_resolve=0.0, resolve_base=None,
    resolve_per_will=0.0, shield_step=0.0, shield_max=0.6, resist_step=0.0, press_rebound=0.0, press_at=1.0,
    strain_rest=1, yield_level=None, break_level=None, break_at=None,
    # the close (RD A.5, C.1, C.4, C.5)
    track_step=0.0, track_clip=3.0, presumption_level=None, concede_step=0.0, deceive_pull=0.0, crowd_at=12,
    # the decider's four (RD B.9, R12)
    sense_step=0.0, relevance_step=0.0, ploy_ob=0.0, ploy_level=None,
    # pointer-row tables
    audience_room={k: dict(v) for k, v in data.AUDIENCE_KINDS_CONTROL.items()},
    content_w_reason=dict(data.CONTENT_CLASSES_CONTROL),
    reason_bias={k: 0.0 for k in data.REASON_BIAS_SHIPPED},
    row_standard={k: "plain" for k in data.ROW_IDS},                   # B05.21: every row `plain`
)

_SHIPPED = dict(
    off_topic_step=1.5, divert_pull=1.0, divert_gain=0.5, rattle_pull=0.5,
    strike_level=None,          # RD B.1 ships `minor`; PLAN B24p.23 leaves it for B98 (G17)
    proofs_per_reason=0.5, account_step=0.15, account_max=0.9,
    fit_level="strong", misfit_level="moderate", read_ob=1.4, read_scale=1.0, read_blur=1.0, guard_step=0.15,
    reading_kept=False,         # RD B.3 ships `on`; PLAN leaves it off (G17)
    delivery_step=0.25, heard_step=0.1, heard_floor=0.5,
    standard_step=0.5, standard_demand=dict(data.STANDARD_DEMAND_SHIPPED), respect_step=0.08,
    mark_level="moderate", cover_step=0.15, cover_max=0.9, mark_shame=0.25,
    press_base=1.0, blow_gain=0.5, sore_gain=1.0, strain_carry=0.5, mark_resolve=1.0, resolve_base=2.0,
    resolve_per_will=0.5, shield_step=0.1, shield_max=0.6, resist_step=0.15, press_rebound=0.25, press_at=0.4,
    strain_rest=1, yield_level="moderate", break_level="strong", break_at=2,
    track_step=0.3, track_clip=3.0,
    presumption_level=None,     # RD C.1 ships `minor`; PLAN leaves it for B98 (G17)
    concede_step=1.0, deceive_pull=0.5, crowd_at=12,
    sense_step=0.05, relevance_step=0.25, ploy_ob=1.4, ploy_level="moderate",
    audience_room={k: dict(v) for k, v in data.AUDIENCE_KINDS_SHIPPED.items()},
    content_w_reason=dict(data.CONTENT_CLASSES_SHIPPED),
    reason_bias=dict(data.REASON_BIAS_SHIPPED),
    row_standard={k: data.ROWS[k]["standard"] for k in data.ROW_IDS},   # RD C.3's column
)

assert set(_CONTROL) == set(_SHIPPED), set(_CONTROL) ^ set(_SHIPPED)


def _freeze(d):
    return MappingProxyType(dict(d))


def controls(**over):
    """B24p.04's controls (on B05's shipped arm). Keyword overrides for a planted run."""
    d = dict(_B05)
    d.update(_CONTROL)
    d.update(over)
    return _freeze(d)


def shipped(**over):
    """B24p.23's shipped values (RD B's shipped columns, plan-governed). Keyword overrides for a planted run."""
    d = dict(_B05)
    d.update(_SHIPPED)
    d.update(over)
    return _freeze(d)


def rd_shipped(**over):
    """RD B's shipped columns LITERALLY (strike_level minor, presumption_level minor, reading_kept on): the RD's
    reading where the plan departs from it (G17). For comparison runs only."""
    return shipped(strike_level="minor", presumption_level="minor", reading_kept=True, **over)
