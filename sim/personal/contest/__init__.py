"""
sim/personal/contest/ — promoted groundup social-contest kernel (Stage 1b).

Rationale: designs/audit/2026-06-30-contest-stage0-reconciliation/DECISIONS.md
Status:    [Stage 1b — substrate promotion + σ-kernel unification, 2026-06-30]

This package is the 9-module groundup kernel relocated from
designs/audit/2026-06-03-contest-groundup/ into a real sim package, unified onto the
ONE canonical σ-kernel (engine.autoload.sigma_leverage / dice_engine). The groundup local
engine.py is NOT copied in — its symbols (roll_net, net_boost, effective_ob, degree,
level) are imported from engine.autoload.sigma_leverage, retiring the "third σ-kernel"
hazard. This stage is BEHAVIOR-PRESERVING: the 151 groundup tests stay green
(sim/tests/test_contest_kernel.py runs _kernel_tests.py and gates on "151 passed").

Module names are KEPT (contract/primitives/resolver/modes/policy/faction/narrative) —
the v30 surface re-skin and the build_contest/resolve_contest wrapper + appeal
multiplicative/additive flag are the NEXT stage, not this one.

──────────────────────────────────────────────────────────────────────────────
BACK-COMPAT SHIM (deprecate-not-delete):
The two live importers of the OLD single-compare stub keep resolving through this
package, which re-exports the stub's public API from sim.personal.contest_legacy_stub
(the deprecated stub, retained as the provenance source):
  • sim/cross_scale/scene_dispatch.py:105  ->  import sim.personal.contest as contest ; contest.run_contest(...)
  • sim/personal/parliamentary_vote.py:42   ->  from sim.personal.contest import PERSUASION_* thresholds
These re-exports are the legacy surface; the promoted kernel's own API (Bout, Venue,
ContestedMode, the venue/mode registries, faction adapters, narrative) is exposed
alongside. The NEXT stage folds the legacy run_contest into the wrapper.
──────────────────────────────────────────────────────────────────────────────
"""
from __future__ import annotations

# ── Legacy surface re-exported for the two live importers (deprecate-not-delete) ──
# scene_dispatch.py uses run_contest; parliamentary_vote.py uses the PERSUASION_* thresholds.
from sim.personal.contest_legacy_stub import (  # noqa: F401
    run_contest,
    resolve_exchange,
    build_argue_pool,
    ContestResult,
    ExchangeResult,
    ARGUE_POOL_TN,
    CONCENTRATION_MULTIPLIER,
    PERSUASION_WIN_THRESHOLD,
    PERSUASION_LOSS_THRESHOLD,
    PERSUASION_TOTAL_VICTORY,
    PERSUASION_TOTAL_DEFEAT,
    PERSUASION_TRACK_START_DEFAULT,
    RESISTANCE_DEFAULT,
    CONTEST_FATIGUE_PENALTY,
)

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
    # legacy surface
    "run_contest", "resolve_exchange", "build_argue_pool", "ContestResult", "ExchangeResult",
    "ARGUE_POOL_TN", "CONCENTRATION_MULTIPLIER",
    "PERSUASION_WIN_THRESHOLD", "PERSUASION_LOSS_THRESHOLD", "PERSUASION_TOTAL_VICTORY",
    "PERSUASION_TOTAL_DEFEAT", "PERSUASION_TRACK_START_DEFAULT",
    "RESISTANCE_DEFAULT", "CONTEST_FATIGUE_PENALTY",
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
