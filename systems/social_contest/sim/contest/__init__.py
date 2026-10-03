"""
systems/social_contest/sim/contest/ — promoted groundup social-contest kernel (Stage 1b).

Rationale: designs/audit/2026-06-30-contest-stage0-reconciliation/DECISIONS.md
Status:    [Stage 1b — substrate promotion + σ-kernel unification, 2026-06-30]

This package is the 9-module groundup kernel relocated from
designs/audit/2026-06-03-contest-groundup/ into a real sim package, unified onto the
ONE canonical σ-kernel (engine.dice_engine.sigma_leverage / dice_engine). The groundup local
engine.py is NOT copied in — its symbols (roll_net, net_boost, effective_ob, degree,
level) are imported from engine.dice_engine.sigma_leverage, retiring the "third σ-kernel"
hazard. This stage is BEHAVIOR-PRESERVING: the 151 groundup tests stay green
(sim/tests/test_contest_kernel.py runs _kernel_tests.py and gates on "151 passed").

Module names are KEPT (contract/primitives/resolver/modes/policy/faction/narrative) —
the v30 surface re-skin and the build_contest/resolve_contest wrapper + appeal
multiplicative/additive flag are the NEXT stage, not this one.

──────────────────────────────────────────────────────────────────────────────
⚠ THE BACK-COMPAT SHIM DESCRIBED HERE IS RETIRED (2026-09-26, ED-SC-0033 clause 2 unit 3a).
`systems.social_contest.sim.contest_legacy_stub` — the deprecated single-compare stub this
package used to re-export — is DELETED
(`FORK:10859d64:systems/social_contest/sim/contest_legacy_stub.py`). Its two claimed live
importers were measured before deletion: `scene_dispatch.py`'s `run_contest` call was already
retired by ED-SC-0006 (2026-07-08) — the comment at `scene_dispatch.py:286-287` is historical,
not a live call; the package's own `run_contest`/`ContestResult`/`ExchangeResult`/
`build_argue_pool`/`resolve_exchange`/`ARGUE_POOL_TN`/`CONCENTRATION_MULTIPLIER`/
`RESISTANCE_DEFAULT`/`CONTEST_FATIGUE_PENALTY` re-exports had ZERO live callers outside this
file and the stub's own re-export chain (measured by grep across `engine/ tools/ tests/`).
`parliamentary_vote.py`'s five `PERSUASION_*` thresholds were the one genuinely live import;
they are now inlined directly in `parliamentary_vote.py`, which no longer imports this package
for them. `resolve_exchange:132-190` was the only code implementing canon §4's compare-model
(the design fork `proposals/2026-09-04-social-contest-branches/11_FOUR_GAMES_AUDIT_AND_PLAN.md`
§8 E1 named) and is recoverable at the fork ref above, not lost.
──────────────────────────────────────────────────────────────────────────────
"""
from __future__ import annotations

# ── Promoted kernel public API (the real engine this stage relocates) ──
from .contract import (  # noqa: F401
    A, B, other, Move, FaultState, Adjudicator, Panel, ContestView, Pressure,
)
from .primitives import (  # noqa: F401
    Stasis, Appeal, Standing, Face, Reserve, Pool, SelfGating, Leverage, Room,
    Resonance, Readiness, DefeatCatalogue, EvidenceItem, Dossier, RhetoricalWeights,
    TRACKERS, RETIRED_TRACKERS, FaceScale,
)
from .resolver import (  # noqa: F401
    Bout, Contestant, Venue, run,
    ContestState, WinCondition, ThresholdRace, TallyAtClose, ProofBar,
    GraceThreshold, PersuasionTrack, VoteAtClose,
)
from .modes import (  # noqa: F401
    ContestedMode, VENUES, INSTITUTIONAL_MODES, CROSS_CULTURAL_VENUES,
    # Stage 1c canonical v30 re-skin:
    PROCEEDINGS, CANONICAL_PROCEEDINGS, CANONICAL_ADJUDICATORS, ADJUDICATOR_PRIMARY,
    proceeding_venue, proceeding_mode,
)
from .wrapper import (  # noqa: F401  (Stage 1c: build/resolve adapter+router)
    build_contest, resolve_contest, Contest, GAMES, MECHANICS, mechanics_selftest,
)
from .dictionaries import (  # noqa: F401  (Stage 2 / Gate B: typed dictionaries + flavor + ED-137 closure)
    Genre, Orientation, Style, STYLES_TABLE, STYLE_BY_AXES,
    InteractionType, INTERACTIONS_TABLE, derive_interaction,
    AdjudicatorType, ADJUDICATORS_TABLE, FactionBoost, FACTION_BOOSTS,
    Proceeding, PROCEEDINGS_TABLE, _crosscheck_proceedings,
    PANEL_AGGREGATION, PANEL_CLOSURE, panel_win_condition,
)
from .armature import (  # noqa: F401  (Stage 3 / Gate C: the adjudicator armature — Style×Conviction dot-product)
    ArmatureAxis, ArmaturePosition, ArmatureConfig, STYLE_AXIS,
    style_axis_alignment, style_axis_dsigma, position_of,
    ARMATURE_MAX_DSIGMA,
)
from .rhetoric import (  # noqa: F401  (Stage 3 / Gate C: CR4 stasis × genre + CR5 orientation self-gating)
    STASIS_PRIMARY_GENRE, STASIS_ROLE, primary_genre_for, is_pre_merits, is_higher_order_reframe,
    genre_of_ground, genre_of_style, primary_genre_pool_bonus, CR4_PRIMARY_GENRE_POOL_BONUS,
    EPIDEICTIC_COMPRESSION, orientation_channel, cr5_self_backfire, CR5_SELF_GATING,
    CR5_BACKFIRE_MAGNITUDE, CR5_ORIENTATION_CHANNEL,
)
from .appraise import (  # noqa: F401  (Stage 3 / Gate C: the Appraise-reveal boundary for armature_position)
    appraise_armature, APPRAISE_REVEAL_BOUNDARY,
)
from . import policy      # noqa: F401
from . import faction     # noqa: F401
from . import narrative   # noqa: F401
from .policy import POLICIES  # noqa: F401

__all__ = [
    # kernel surface
    "A", "B", "other", "Move", "FaultState", "Adjudicator", "Panel", "ContestView", "Pressure",
    "Stasis", "Appeal", "Standing", "Face", "Reserve", "Pool", "SelfGating", "Leverage", "Room",
    "Resonance", "Readiness", "DefeatCatalogue", "EvidenceItem", "Dossier", "RhetoricalWeights",
    "TRACKERS", "RETIRED_TRACKERS", "FaceScale",
    "Bout", "Contestant", "Venue", "run", "ContestState", "WinCondition", "ThresholdRace",
    "TallyAtClose", "ProofBar", "GraceThreshold", "PersuasionTrack", "VoteAtClose",
    "ContestedMode", "VENUES", "INSTITUTIONAL_MODES", "CROSS_CULTURAL_VENUES",
    # Stage 1c canonical re-skin + wrapper:
    "PROCEEDINGS", "CANONICAL_PROCEEDINGS", "CANONICAL_ADJUDICATORS", "ADJUDICATOR_PRIMARY",
    "proceeding_venue", "proceeding_mode",
    "build_contest", "resolve_contest", "Contest", "GAMES", "MECHANICS", "mechanics_selftest",
    "policy", "faction", "narrative", "POLICIES",
    # Stage 2 / Gate B typed dictionaries + flavor + ED-137 Panel closure:
    "Genre", "Orientation", "Style", "STYLES_TABLE", "STYLE_BY_AXES",
    "InteractionType", "INTERACTIONS_TABLE", "derive_interaction",
    "AdjudicatorType", "ADJUDICATORS_TABLE", "FactionBoost", "FACTION_BOOSTS",
    "Proceeding", "PROCEEDINGS_TABLE",
    "PANEL_AGGREGATION", "PANEL_CLOSURE", "panel_win_condition",
    # Stage 3 / Gate C — the adjudicator armature + CR4 stasis + CR5 self-gating + Appraise-reveal:
    "ArmatureAxis", "ArmaturePosition", "ArmatureConfig", "STYLE_AXIS",
    "style_axis_alignment", "style_axis_dsigma", "position_of", "ARMATURE_MAX_DSIGMA",
    "STASIS_PRIMARY_GENRE", "STASIS_ROLE", "primary_genre_for", "is_pre_merits", "is_higher_order_reframe",
    "genre_of_ground", "genre_of_style", "primary_genre_pool_bonus", "CR4_PRIMARY_GENRE_POOL_BONUS",
    "EPIDEICTIC_COMPRESSION", "orientation_channel", "cr5_self_backfire", "CR5_SELF_GATING",
    "CR5_BACKFIRE_MAGNITUDE", "CR5_ORIENTATION_CHANNEL",
    "appraise_armature", "APPRAISE_REVEAL_BOUNDARY",
]
