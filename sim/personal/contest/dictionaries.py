"""
dictionaries.py — the Stage-2 TYPED DICTIONARIES (Gate B).

Per the staged plan (Stage 2 / Gate B) and DECISIONS.md locked decision 3 (sim + canon
only; NO Godot YAML), the contest's four canonical dictionaries live HERE as frozen Python
dataclasses, single-sourced with the canonical prose tables in params/contest.md +
designs/scene/social_contest_v30.md. There is deliberately NO data/*.yaml layer.

The four dictionaries:
  1. PROCEEDINGS_TABLE  — Proceeding×8   (Formal/Grand Contest, Royal Audience, Church
                          Tribunal, Guild Arbitration, Casual Dispute, Private Negotiation,
                          Personal Appeal). exchange_count / role_structure /
                          resistance_modifier / adjudicator_type / track_start (+ flavor).
  2. ADJUDICATORS_TABLE — AdjudicatorType×4 (Expert Judge / Crowd / No Adjudicator / Panel)
                          + FACTION_BOOSTS (the 6-faction ethical-mode boost table, +Löwenritter
                          conditional).
  3. STYLES_TABLE       — Style×4 (Precedent / Suppression / Vision / Insinuation =
                          Genre × Orientation) (+ flavor).
  4. INTERACTIONS_TABLE — InteractionType×4 (CLASH / REINFORCE / CROSS / TIE) derivation.

RELATIONSHIP TO modes.py: modes.py holds the MECHANICAL substrate (the groundup Venue /
Adjudicator / win-condition factories + the Stage-1c PROCEEDINGS registry that the wrapper
resolves through). This module holds the TYPED CANONICAL SURFACE — the player-/authoring-facing
dictionary rows with flavor text and hand-verified param provenance. The two are cross-checked
by _kernel_tests.py (every Proceeding row here == the matching modes.PROCEEDINGS row), so a
drift between the mechanical registry and the typed surface is a test failure, not a silent seam.

ANTI-FABRICATION (CLAUDE.md §7 — the auto gate is leaky): every field below carries an inline
`# <-` citation to the exact params/contest.md or social_contest_v30.md row it traces to,
hand-verified this stage. No numeric or structural value is invented here.

FLAVOR TEXT (locked decision 5): every Style and every Proceeding row carries `flavor` — real,
final, player-facing UI-card copy (short, sentence-case, active/verb-first, CDS voice),
behaviorally honest per Lens 6 (the copy must read the way the primitive actually behaves; it
differs for Church Tribunal vs Casual Dispute because they mechanically differ). The DRAFT
one-liners in the player-interaction walkthrough §2 Step 2 (Precedent "Cite settled fact
openly", etc.) are superseded by the authored `flavor` here.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Tuple

# The typed surface names its mechanical binding by string key, not by importing the factory,
# so this module stays a pure data layer (no resolution). modes.py is the mechanical authority.
from . import modes as _modes
from .resolver import VoteAtClose as _VoteAtClose
from .primitives import Appeal   # ED-1061: Guilds venue-derived boost maps the adjudicator's dominant appeal


# ══════════════════════════════════════════════════════════════════════════════════════════
# 1. GENRE × ORIENTATION → STYLE  (params/contest.md §Argument Styles PP-235;
#    social_contest_v30 §2 Step 3 / §4 Step 2)
# ══════════════════════════════════════════════════════════════════════════════════════════
# The two v30 genres (params/contest.md §Genres) and the two orientations (§4 Step 2). These are
# the SURFACE axis names; the kernel's own vocabulary (primitives.Stasis tense past/future;
# primitives.Appeal) is the substrate the reconciliation map bridges to — that bridge is Stage 1/3
# scope, NOT re-litigated here. Stage 2 owns only the surface Style dictionary.

class Genre:
    """The two canonical genres (params/contest.md §Genres — 'Memory' / 'Projection';
       PP-234 restructured 3 genres → 2)."""
    MEMORY = "Memory"          # <- params/contest.md §Genres: "Memory | Retention (has been) | Actual (settled)"
    PROJECTION = "Projection"  # <- params/contest.md §Genres: "Projection | Protention (yet to be) | Potential"
    ALL = (MEMORY, PROJECTION)

class Orientation:
    """The two canonical orientations (social_contest_v30 §4 Step 2 'Revealing or Obscuring';
       ED-897 aligned 'Direct→Revealing / Indirect→Obscuring')."""
    REVEALING = "Revealing"    # <- social_contest_v30 §4 Step 2; params §Faction Boosts axis
    OBSCURING = "Obscuring"    # <- social_contest_v30 §4 Step 2; §4 "Obscuring win: ... Doubt Marker"
    ALL = (REVEALING, OBSCURING)


@dataclass(frozen=True)
class Style:
    """One of the four canonical Argument Styles = Genre × Orientation (params/contest.md
       §Argument Styles PP-235). A single per-exchange choice (social_contest_v30 §4 Step 2:
       'a single style pick'). `flavor` is authored player-facing UI-card copy (locked decision 5)."""
    key: str
    name: str
    genre: str
    orientation: str
    canonical_flavor: str      # <- params/contest.md §Argument Styles "Flavour" column (verbatim canon)
    flavor: str                # authored UI-card copy (locked decision 5; CDS voice, behaviorally honest)
    source: str

# The four styles. genre/orientation/name/canonical_flavor are VERBATIM from
# params/contest.md §Argument Styles (PP-235). `flavor` is authored this stage.
STYLES_TABLE = {
    "precedent": Style(
        key="precedent", name="Precedent",
        genre=Genre.MEMORY, orientation=Orientation.REVEALING,
        canonical_flavor="Citing what happened openly",         # <- params §Argument Styles row Precedent
        # Behaviorally honest (Lens 6): Memory+Revealing = a forensic, logos-bearing OPEN citation of the
        # settled record. It BUILDS your standing (Revealing/ethos-bearing argument raises Face) and moves
        # the track directly; nothing is hidden, so there is no Doubt Marker and no self-backfire risk.
        flavor="Put the record on the table. Name the fact, cite the source, and let it stand.",
        source="params/contest.md §Argument Styles (PP-235); social_contest_v30 §2 Step 3"),
    "suppression": Style(
        key="suppression", name="Suppression",
        genre=Genre.MEMORY, orientation=Orientation.OBSCURING,
        canonical_flavor="Burying inconvenient history",         # <- params §Argument Styles row Suppression
        # Behaviorally honest (Lens 6): Memory+Obscuring works the SAME settled past as Precedent but
        # HIDES rather than reveals — an Obscuring win plants a Doubt Marker on the opponent (−2 to their
        # next winning margin) instead of openly advancing (social_contest_v30 §4 "Obscuring win"). It does
        # not build Face the way Revealing does; it is an attack on the opponent's footing, not on the record.
        # NB flavor honesty depends on ED-1060 (terminal-doubt): in a single/final exchange the marker only
        # "lands" if the terminal-value rule is ratified — see DOUBT_MARKER; the copy names the doubt planted,
        # not a guaranteed track gain (which Obscuring never gives).
        flavor="Steer the room away from the part of the record that hurts you. Leave a doubt where their next point should land.",
        source="params/contest.md §Argument Styles (PP-235); social_contest_v30 §4 Step 2"),
    "vision": Style(
        key="vision", name="Vision",
        genre=Genre.PROJECTION, orientation=Orientation.REVEALING,
        canonical_flavor="Proposing a transparent future",       # <- params §Argument Styles row Vision
        # Behaviorally honest (Lens 6): Projection+Revealing = an OPEN argument about what should come —
        # deliberative/future-tense, pathos-and-logos toward an outcome. Like Precedent it advances the
        # track openly and can build standing, but it argues the unsettled future (Projection genre), so it
        # CROSSes (not CLASHes) against a Memory opponent — talking past, not clashing.
        flavor="Argue the future out loud. Show the room what you would build, and make them want it.",
        source="params/contest.md §Argument Styles (PP-235); social_contest_v30 §2 Step 3"),
    "insinuation": Style(
        key="insinuation", name="Insinuation",
        genre=Genre.PROJECTION, orientation=Orientation.OBSCURING,
        canonical_flavor="Implying unstated consequences",       # <- params §Argument Styles row Insinuation
        # Behaviorally honest (Lens 6): Projection+Obscuring = an IMPLIED threat about what will follow —
        # future-tense, but Obscuring, so it plants a Doubt Marker rather than advancing openly, and (CR5,
        # Stage 3) an Indirect line carries self-Face backfire risk. Never states the consequence outright;
        # lets the room infer it. NB like Suppression, single/final-exchange honesty depends on ED-1060
        # (terminal-doubt) — see DOUBT_MARKER; the copy names the implication planted, not a track gain.
        flavor="Let the threat go unspoken. Imply what follows if they win, and let the room finish the sentence.",
        source="params/contest.md §Argument Styles (PP-235); social_contest_v30 §4 Step 2"),
}
# Lookup by (genre, orientation) — the canonical single-choice mapping (params §Argument Styles).
STYLE_BY_AXES = {(s.genre, s.orientation): s for s in STYLES_TABLE.values()}

# ── Obscuring single-exchange dominance (finding 4, ED-1060 — OPEN DECISION FOR JORDAN) ──
# An Obscuring WIN moves no track; it plants a Doubt Marker worth −2 to the opponent's NEXT winning
# exchange (social_contest_v30 §4:179-183). In a SINGLE-exchange contest (Casual Dispute (1,1), Personal
# Appeal (1,1); Church Tribunal/Private Negotiation at length 1) there IS no next exchange, so the marker's
# EV is exactly 0 — the Obscuring style forgoes the sole track/tally movement for nothing, and is STRICTLY
# DOMINATED by its Revealing genre-mate (Suppression < Precedent, Insinuation < Vision). The churn axiom
# requires every style be correct somewhere. RESOLUTION (best-grounded, flagged, easy to swap): give the
# marker a non-zero TERMINAL value at contest close, AGAINST the marked side (i.e. in the Obscuring winner's
# / planter's favour — the marker always works against the party it was placed on, v30:180-181; min 0).
#
# ── ROUND-4 FINDING 1 (major): the terminal rule must be SPLIT BY RESOLUTION MECHANISM ──
# The prior single-clause rule was written entirely in banded "margin / band / Compromise-zone" language —
# constructs that exist ONLY on the PersuasionTrack win-condition (resolver.PersuasionTrack: 0–10 axis read
# into bands). But of the FOUR single-exchange-capable proceedings this rule NAMES, only ONE is banded:
#   • Church Tribunal (tracker_mode="required")  -> PersuasionTrack  (BANDED — the written rule applies)
#   • Casual Dispute  (tracker_mode="none",     always)              -> TallyAtClose (RAW A/B/draw)
#   • Personal Appeal (tracker_mode="optional", default)            -> TallyAtClose (RAW A/B/draw)
#   • Private Negotiation (tracker_mode="optional", default, len 1) -> TallyAtClose (RAW A/B/draw)
# resolver.TallyAtClose.resolve returns bare A / B / "draw" from the raw `adv` tally — it has NO margin, NO
# band, NO Compromise zone for a "slides one band" rule to operate on. So the design commitment was
# WELL-DEFINED only for Church Tribunal and UNDEFINED for exactly the two proceedings (Casual Dispute always,
# Personal Appeal default) the finding cites as motivating cases — leaving Suppression/Insinuation still
# potentially dominated there. FIX: specify the terminal marker SEPARATELY for each mechanism, and add a
# DOUBT_MARKER_FIELD guard requiring BOTH branches to be present (so neither can silently go undefined again):
#   (i)  BANDED  (PersuasionTrack): the already-written rule — −2 subtracted from the closing MARGIN/BAND
#        against the marked side; slides a Compromise-zone result one step toward the Obscuring winner; min 0.
#   (ii) TALLY   (TallyAtClose): the terminal −2 is subtracted from the MARKED SIDE'S RAW `adv` before the
#        A/B/draw comparison (min 0). A close raw tally can therefore FLIP toward the Obscuring winner or fall
#        to a draw — but the marker can never MANUFACTURE a lead the planter did not earn (it only removes up
#        to 2 of the marked side's raw advancement). This mirrors the banded branch's direction (against the
#        marked side) using the only quantity a raw tally exposes (the adv difference), so Obscuring stops
#        being strictly dominated in the tally subset too. Alternative for the tally subset: gate Obscuring
#        out of the TallyAtClose proceedings specifically — recorded as tally_alternative below.
# Alternative (b) overall: gate Obscuring out of single-exchange proceedings entirely.
# This remains a DESIGN-TABLE commitment only: the resolver does NOT yet consume orientation (Stage-3 CR5
# rhetoric-armature scope), so NO resolution number changes here — the flags record the ratified-pending
# rule for Stage 3 to implement. Couples to the Suppression/Insinuation flavor honesty.
DOUBT_MARKER_TERMINAL = "terminal_value"   # OPEN DECISION FOR JORDAN (ED-1060): a) terminal_value [impl'd
                                           #   as the design rule] | b) gate_obscuring_out_of_single_exchange

# The two terminal-behavior branches the rule MUST separately specify (round-4 finding 1). Keyed by the
# resolution mechanism the closing proceeding uses (resolver.PersuasionTrack vs resolver.TallyAtClose);
# _crosscheck / _kernel_tests guard that BOTH are present so the tally subset can never go undefined again.
DOUBT_MARKER_FIELD = {
    # (i) banded proceedings (tracker_mode="required" -> PersuasionTrack): Church Tribunal among the named cases.
    "banded": "PersuasionTrack (banded): the terminal −2 is subtracted from the closing MARGIN/BAND against "
              "the marked side (in the Obscuring winner's / planter's favour) — slides a Compromise-zone "
              "result one step toward the Obscuring winner, min 0, cannot reach a decisive band it does not "
              "otherwise reach. This is the branch the original rule wrote; it applies ONLY to banded "
              "proceedings (Church Tribunal at length 1).",
    # (ii) tally proceedings (tracker_mode="none"/"optional" default -> TallyAtClose): Casual Dispute (always),
    #      Personal Appeal (default), Private Negotiation (default, at length 1). No band exists — raw A/B/draw.
    "tally": "TallyAtClose (raw A/B/draw): there is no band or margin, so the terminal −2 is subtracted from "
             "the MARKED SIDE'S RAW adv before the exchange-majority comparison (min 0). A close raw tally can "
             "flip toward the Obscuring winner or fall to a draw; the marker can never manufacture a lead the "
             "planter did not earn (it only removes up to 2 of the marked side's own advancement). Same "
             "direction as the banded branch (against the marked side), expressed on the only quantity a raw "
             "tally exposes.",
    "tally_alternative": "(b, tally-scoped) instead gate Obscuring style-selection out of the TallyAtClose "
                         "single-exchange proceedings (Casual Dispute / Personal Appeal / Private Negotiation "
                         "at length 1) specifically, leaving the banded branch as the sole terminal case.",
}

DOUBT_MARKER = {
    "ed": "ED-1060",
    "status": "OPEN DECISION FOR JORDAN (Gate B 2026-07-01; provisional pending Jordan ratification)",
    "problem": "Obscuring win in a single/final exchange forgoes all track movement for a Doubt Marker "
               "whose −2-to-next-winning-exchange effect has EV 0 when no next exchange exists — so "
               "Suppression is strictly dominated by Precedent, Insinuation by Vision, in every "
               "single-exchange contest (Casual Dispute, Personal Appeal; Church Tribunal/Private "
               "Negotiation at length 1). Dead/dominated choice (churn axiom). NB (round-4 finding 1): those "
               "single-exchange proceedings do NOT all resolve the same way — Church Tribunal is banded "
               "(PersuasionTrack) but Casual Dispute (always) / Personal Appeal (default) / Private "
               "Negotiation (default) resolve by RAW A/B/draw TallyAtClose, which has no band or margin — so "
               "the terminal rule must be specified separately per mechanism (see DOUBT_MARKER_FIELD).",
    "rule": DOUBT_MARKER_TERMINAL,
    # The terminal behavior is SPLIT BY MECHANISM (round-4 finding 1) — see DOUBT_MARKER_FIELD for the two
    # branches. `resolution` states the shared direction; `banded_terminal` / `tally_terminal` give each branch.
    "resolution": "An unconsumed Doubt Marker at contest close applies its −2 once, terminally, AGAINST the "
                  "marked side — i.e. in the Obscuring winner's (planter's) favour, the same direction the "
                  "marker fires in play (v30:180-181: the marker is placed on the opponent and reduces THAT "
                  "side's winning margin) (min 0). HOW it applies depends on the closing proceeding's "
                  "resolution mechanism — split by mechanism because banded and raw-tally proceedings expose "
                  "different quantities: (i) banded (PersuasionTrack) subtracts from the closing margin/band; "
                  "(ii) raw-tally (TallyAtClose — Casual Dispute always, Personal Appeal / Private Negotiation "
                  "by default) subtracts from the marked side's raw adv before the A/B/draw comparison. See "
                  "banded_terminal / tally_terminal.",
    "banded_terminal": DOUBT_MARKER_FIELD["banded"],
    "tally_terminal": DOUBT_MARKER_FIELD["tally"],
    "tally_alternative": DOUBT_MARKER_FIELD["tally_alternative"],
    "alternative": "(b) gate Obscuring style-selection out of single-exchange proceedings and document why.",
    "scope_note": "DESIGN-TABLE COMMITMENT ONLY — the resolver does not yet consume orientation (Stage-3 "
                  "CR5 rhetoric-armature scope), so no resolution-path number changes this pass; the flag "
                  "records the rule for Stage 3 to implement. The Obscuring flavor (Suppression/Insinuation) "
                  "is only behaviorally honest once this is ratified.",
    "source": "social_contest_v30 §4 (Obscuring win / Doubt Marker) + params/contest.md §Interaction Types; "
              "ED-1060",
}

def _doubt_marker_branches_specified():
    """Guard (round-4 finding 1): the Terminal Doubt rule must specify BOTH the banded (PersuasionTrack) and
       the tally (TallyAtClose) terminal behavior — the two resolution mechanisms the named single-exchange
       proceedings actually use (Church Tribunal banded; Casual Dispute/Personal Appeal/Private Negotiation
       raw tally). Return a list of the branches that are MISSING or empty; empty list => both defined, so the
       tally subset can never silently go undefined again. Asserted by _kernel_tests.py."""
    missing = []
    for branch in ("banded_terminal", "tally_terminal"):
        v = DOUBT_MARKER.get(branch)
        if not (isinstance(v, str) and v.strip()):
            missing.append(branch)
    return missing


# ══════════════════════════════════════════════════════════════════════════════════════════
# 2. INTERACTION TYPE  (params/contest.md §Interaction Types; social_contest_v30 §4 Step 4)
# ══════════════════════════════════════════════════════════════════════════════════════════
# The derivation is PURELY STRUCTURAL over the two chosen styles' (genre, orientation):
#   same genre, OPPOSITE orientation  -> CLASH     (social_contest_v30 §4: "same genre, opposite orientation")
#   same genre, SAME orientation      -> REINFORCE (§4: "same genre, same orientation")
#   DIFFERENT genres                  -> CROSS      (§4: "different genres"; orientation irrelevant)
#   TIE is OVERLAID on any of the above when successes are equal (§4 Step 4 "TIE (equal
#     successes, any interaction type)") — it is NOT a fourth structural branch; the structural
#     type (CLASH/REINFORCE/CROSS) still holds and governs the TIE's strain exception (CROSS+TIE
#     => no strain, PP-236). derive_interaction() returns the STRUCTURAL type; is_tie is a
#     separate boolean the resolver already computes from equal successes.
#
# This is the canonical v30 SURFACE derivation. It is single-sourced HERE (a typed lookup) so no
# other module re-implements it; the kernel's own resolution operates on the substrate primitives
# (Stasis/Appeal), and this surface derivation is the player-facing name the walkthrough §3 Step 2
# renders ("Direct Clash" / "Mutual Reinforcement" / "Talking Past Each Other" / "Deadlocked").

@dataclass(frozen=True)
class InteractionType:
    """A resolved interaction category between the two orators' styles. CLASH/REINFORCE/CROSS are
       the three STRUCTURAL types (derived from genre/orientation); TIE is the equal-successes
       overlay. `player_name` is the plain-language label the resolution screen shows (walkthrough
       §3 Step 2). `strain` / `resolution` summarize the canonical §Interaction Types row."""
    key: str
    name: str
    player_name: str           # <- player_interaction_walkthrough §3 Step 2 plain-language label
    condition: str             # <- social_contest_v30 §4 Step 4 / params §Interaction Types "Condition"
    resolution: str            # <- params §Interaction Types "Resolution"
    strain: str                # <- params §Interaction Types "Strain"
    source: str

INTERACTIONS_TABLE = {
    "clash": InteractionType(
        key="clash", name="CLASH", player_name="Direct Clash",
        condition="Same genre, opposite orientation",            # <- params §Interaction Types row CLASH
        resolution="Compare; margin vs resistance -> track movement toward winner",  # <- params §Interaction Types
        strain="Margin + Cha modifier - Foc defence (minimum 0)",  # <- params §Interaction Types CLASH; §4 Step 4
        source="params/contest.md §Interaction Types; social_contest_v30 §4 Step 4"),
    "reinforce": InteractionType(
        key="reinforce", name="REINFORCE", player_name="Mutual Reinforcement",
        condition="Same genre, same orientation",                # <- params §Interaction Types row REINFORCE
        resolution="Same as CLASH (compare; margin vs resistance -> track movement)",  # <- params §Interaction Types
        strain="max(0, (Margin - 1) + Cha modifier - Foc defence)",  # <- params §Interaction Types REINFORCE (PP-401, ED-296 floor)
        source="params/contest.md §Interaction Types (PP-401/ED-296); social_contest_v30 §4 Step 4"),
    "cross": InteractionType(
        key="cross", name="CROSS", player_name="Talking Past Each Other",
        condition="Different genres",                            # <- params §Interaction Types row CROSS
        resolution="Each side floor(successes/2) vs resistance; net movement = difference",  # <- params §Interaction Types
        strain="None",                                           # <- params §Interaction Types CROSS; PP-236
        source="params/contest.md §Interaction Types; social_contest_v30 §4 Step 4"),
    "tie": InteractionType(
        key="tie", name="TIE", player_name="Deadlocked",
        condition="Equal successes, any interaction type",       # <- params §Interaction Types row TIE
        resolution="Track +1 toward first-to-speak holder; first-to-speak stays",  # <- params §Interaction Types / §4 Step 4
        strain="1 each (except CROSS: 0 - PP-236)",              # <- params §Interaction Types TIE; PP-236
        source="params/contest.md §Interaction Types (PP-236); social_contest_v30 §4 Step 4"),
}

def derive_interaction(style_a, style_b):
    """Return the STRUCTURAL InteractionType (clash/reinforce/cross) between two Style objects (or
       two style keys), per the canonical v30 derivation (social_contest_v30 §4 Step 4;
       params/contest.md §Argument Styles 'Interaction type derived'). TIE is NOT returned here —
       it is the equal-successes overlay the resolver applies on top of the structural type
       (params §Interaction Types 'TIE ... any interaction type'), so callers pass is_tie
       separately. This is the ONE canonical typed lookup for the derivation; do not re-implement."""
    sa = STYLES_TABLE[style_a] if isinstance(style_a, str) else style_a
    sb = STYLES_TABLE[style_b] if isinstance(style_b, str) else style_b
    if sa.genre != sb.genre:
        return INTERACTIONS_TABLE["cross"]                       # different genres -> CROSS (orientation irrelevant)
    if sa.orientation == sb.orientation:
        return INTERACTIONS_TABLE["reinforce"]                   # same genre, same orientation -> REINFORCE
    return INTERACTIONS_TABLE["clash"]                           # same genre, opposite orientation -> CLASH


# ══════════════════════════════════════════════════════════════════════════════════════════
# 3. ADJUDICATOR TYPE ×4  +  FACTION BOOSTS
#    (social_contest_v30 §2 Step 1 + §3 Argue Pool; params/contest.md §Pools + §Faction Boosts)
# ══════════════════════════════════════════════════════════════════════════════════════════
# CANON BOUNDARY (mirrors modes.py): canon fixes, per adjudicator type, ONLY (a) the primary
# ATTRIBUTE the Argue pool doubles (§3 Argue Pool table) and (b) the structural shape (single
# authority vs collective vs parties-themselves vs deliberating bench). It fixes NO discipline or
# proof/character weighting — those live as [SEED] calibration in modes.py's factories, tagged
# there, Jordan to set. This typed surface carries the CANONICAL facts + the mechanical binding key.

@dataclass(frozen=True)
class AdjudicatorType:
    """One of the four canonical adjudicator types (social_contest_v30 §2 Step 1). `primary_attribute`
       is the ONLY per-type mechanical fact canon fixes (§3 Argue Pool). `collective` marks whether the
       type is a Panel (many) or a single Adjudicator. `mechanical_key` binds to
       modes.CANONICAL_ADJUDICATORS (the [SEED]-profiled factory)."""
    key: str
    name: str
    primary_attribute: str     # <- social_contest_v30 §3 Argue Pool table (CANONICAL)
    who_decides: str           # <- social_contest_v30 §2 Step 1 "Who decides" (verbatim canon)
    collective: bool           # single Adjudicator (False) vs Panel/collective (True)
    mechanical_key: str        # key into modes.CANONICAL_ADJUDICATORS (the mechanical factory)
    ed137: Optional[str]       # ED-137 note where applicable (Panel)
    source: str

ADJUDICATORS_TABLE = {
    "expert_judge": AdjudicatorType(
        key="expert_judge", name="Expert Judge",
        primary_attribute="Cognition",                           # <- §3 Argue Pool: "Expert judge | Cognition"
        who_decides="A single authority evaluates arguments on merits",  # <- §2 Step 1 verbatim
        collective=False, mechanical_key="expert_judge", ed137=None,
        source="social_contest_v30 §2 Step 1 / §3 Argue Pool; params/contest.md §Pools"),
    "crowd": AdjudicatorType(
        key="crowd", name="Crowd",
        primary_attribute="Charisma",                            # <- §3 Argue Pool: "Crowd | Charisma"
        who_decides="A collective audience reacts to delivery and force",  # <- §2 Step 1 verbatim
        collective=True, mechanical_key="crowd", ed137=None,
        source="social_contest_v30 §2 Step 1 / §3 Argue Pool; params/contest.md §Pools"),
    "no_adjudicator": AdjudicatorType(
        key="no_adjudicator", name="No Adjudicator",
        primary_attribute="Attunement",                          # <- §3 Argue Pool: "No adjudicator | Attunement"
        who_decides="The parties themselves are the decision-makers",  # <- §2 Step 1 verbatim
        collective=False, mechanical_key="no_adjudicator", ed137=None,
        source="social_contest_v30 §2 Step 1 / §3 Argue Pool; params/contest.md §Pools"),
    "panel": AdjudicatorType(
        key="panel", name="Panel",
        primary_attribute="Cognition",                           # <- §3 Argue Pool: "Panel | Cognition"
        who_decides="Multiple individual judges deliberating",   # <- §2 Step 1 verbatim
        collective=True, mechanical_key="panel",
        # ED-137 CLOSED this stage (Gate B): Panel is no longer "use Expert Judge as provisional" — it
        # is a bench of individual judges deliberating to a terminal VoteAtClose ballot (VoteAtClose is
        # the aggregation mechanism, promoted from the groundup). See PANEL_CLOSURE below + ED-1057.
        ed137="CLOSED Gate B 2026-07-01 (ED-1057): Panel = bench of individual expert judges; verdict "
              "by VoteAtClose per-member ballot, aggregated WEIGHTED-BY-STANDING (each juror's ballot "
              "counts by its bench-weight = Adjudicator.discipline). Reachable via Guild Arbitration "
              "(ED-1059 rebind). Was: provisional 'use Expert Judge' (ED-137).",
        source="social_contest_v30 §2 Step 1 / §3 Argue Pool; ED-137 closure ED-1057"),
}


@dataclass(frozen=True)
class FactionBoost:
    """A faction's single-axis Argument-Style boost (params/contest.md §Faction Boosts;
       social_contest_v30 §2 Step 3). One faction boosts exactly ONE of four options — one genre OR
       one orientation, never both (§2 Step 3). `axis` ∈ {'Genre','Orientation','Either'}; `boost` is
       the specific value boosted. `ethical_mode` is the faction's canonical ethical mode."""
    faction: str
    ethical_mode: str          # <- params §Faction Boosts "Ethical Mode" (verbatim canon)
    boost: str                 # <- params §Faction Boosts "Boost" (verbatim canon)
    axis: str                  # <- params §Faction Boosts "Axis" (verbatim canon)
    conditional: bool          # True for Löwenritter ("if emerged")
    source: str

# The faction-boost table. Six CORE factions (Church, Crown, Varfell, Hafenmark, Restoration,
# Guilds) + Löwenritter (conditional, "if emerged"). Every row VERBATIM from params/contest.md
# §Faction Boosts (== social_contest_v30 §2 Step 3). Niflhel row is STRUCK (ED-899/ED-764) and
# is correctly absent. (The scope's "6 factions" = the six unconditional core rows; Löwenritter is
# the canonical conditional 7th, carried with conditional=True so a caller can filter it out.)
FACTION_BOOSTS = {
    "church": FactionBoost(
        faction="Church", ethical_mode="Divine Command",
        boost="Obscuring", axis="Orientation", conditional=False,   # <- params §Faction Boosts row Church
        source="params/contest.md §Faction Boosts; social_contest_v30 §2 Step 3 (ED-899/ED-897)"),
    "crown": FactionBoost(
        faction="Crown", ethical_mode="Virtue Ethics",
        boost="Revealing", axis="Orientation", conditional=False,   # <- params §Faction Boosts row Crown
        source="params/contest.md §Faction Boosts; social_contest_v30 §2 Step 3"),
    "varfell": FactionBoost(
        faction="Varfell", ethical_mode="Consequentialism",
        boost="Projection", axis="Genre", conditional=False,        # <- params §Faction Boosts row Varfell
        source="params/contest.md §Faction Boosts; social_contest_v30 §2 Step 3"),
    "hafenmark": FactionBoost(
        faction="Hafenmark", ethical_mode="Categorical Imperative",
        boost="Memory", axis="Genre", conditional=False,            # <- params §Faction Boosts row Hafenmark
        source="params/contest.md §Faction Boosts; social_contest_v30 §2 Step 3"),
    "restoration": FactionBoost(
        faction="Restoration", ethical_mode="Rawlsian Social Contract",
        boost="Revealing", axis="Orientation", conditional=False,   # <- params §Faction Boosts row Restoration
        source="params/contest.md §Faction Boosts; social_contest_v30 §2 Step 3"),
    "guilds": FactionBoost(
        faction="Guilds", ethical_mode="Moral Relativism",
        # ED-1061 (Jordan, Gate B): CANON CORRECTED. params/contest.md §Faction Boosts said "GM picks" —
        # a genuine defect under the no-GM mandate (CLAUDE.md: "there is no GM — the engine resolves
        # everything"). The RATIFIED engine rule is CONTEXT-DERIVED-FROM-THE-VENUE: the Guilds either-axis
        # boost applies to whichever axis (genre or orientation) the CURRENT contest's adjudicator/venue
        # already favours — NOT a GM pick, an orator pick, or a random pick. Derived from the adjudicator's
        # ethos/pathos/logos weighting via the Aristotle mapping already in the corpus (Expert Judge/Panel
        # ↔ logos/Cognition, Crowd ↔ pathos/Charisma, No-adjudicator ↔ ethos/Attunement). See
        # guilds_boost_for() below. `boost="Context (venue-derived)"` / axis="Either" reflects that the
        # value is resolved per-contest, not fixed like the other six factions.
        boost="Context (venue-derived)", axis="Either", conditional=False,   # <- params §Faction Boosts row Guilds (ED-1061: engine-derived, was "GM picks")
        source="params/contest.md §Faction Boosts (ED-1061 correction); social_contest_v30 §2 Step 3"),
    "lowenritter": FactionBoost(
        faction="Löwenritter", ethical_mode="Duty-based (if emerged)",
        boost="Projection", axis="Genre", conditional=True,         # <- params §Faction Boosts row Löwenritter ("if emerged")
        source="params/contest.md §Faction Boosts; social_contest_v30 §2 Step 3"),
}


# ── Guilds either-axis boost — CONTEXT-DERIVED FROM THE VENUE (ED-1061, Jordan Gate B) ──
# The Guilds are the one faction whose boost axis is not fixed. params/contest.md §Faction Boosts said
# "GM picks" — a defect under the no-GM mandate (CLAUDE.md: "there is no GM — the engine resolves
# everything"). ED-1061 corrects the PROSE (params/contest.md + social_contest_v30 §2 Step 3) and this
# implements the corrected rule: the boost applies to whichever axis the CURRENT contest's ADJUDICATOR
# already favours, derived from the adjudicator's ethos/pathos/logos weighting — NOT a GM/orator/random
# pick.
#
# GROUNDING (reuses corpus mappings; invents nothing): the derivation reads the adjudicator's DOMINANT
# appeal (its heaviest char_ethos/pathos/logos weight — contract.Adjudicator.character(), which a Panel
# averages over its members) and maps it to the axis-value the Guilds boost via the Aristotelian chain
# already in the corpus:
#   • logos  (Expert Judge / Panel — Cognition-primary; forensic/PAST register, RhetoricalWeights
#             logos_past home; genre Memory = "Retention (has been)" = past) -> MEMORY (Genre)
#   • pathos (Crowd — Charisma-primary; deliberative/FUTURE register, pathos_future home; genre
#             Projection = "Protention (yet to be)" = future)               -> PROJECTION (Genre)
#   • ethos  (No Adjudicator — Attunement-primary; the ethos/standing-bearing OPEN appeal; Revealing is
#             the ethos-bearing orientation, per the Precedent style note "Revealing/ethos-bearing
#             argument raises Face")                                         -> REVEALING (Orientation)
# So the Guilds boost is fully engine-derivable from the venue's own already-computed signal (the
# adjudicator character), with no new venue field. Ties (exactly equal char weights) resolve by the
# Aristotelian appeal ORDER (logos, pathos, ethos) — deterministic, no randomness.
_GUILDS_APPEAL_TO_BOOST = {
    Appeal.LOGOS:  (Genre.MEMORY,       "Genre"),       # forensic/past  -> Memory
    Appeal.PATHOS: (Genre.PROJECTION,   "Genre"),       # deliberative/future -> Projection
    Appeal.ETHOS:  (Orientation.REVEALING, "Orientation"),  # ethos-bearing open standing -> Revealing
}

def guilds_boost_for(adjudicator):
    """Resolve the Guilds either-axis boost for a given contest, CONTEXT-DERIVED FROM THE VENUE'S
       adjudicator (ED-1061, Jordan Gate B — engine rule replacing the stale 'GM picks' prose). `adjudicator`
       is a contract.Adjudicator or contract.Panel (or anything exposing .character()); the boost applies to
       whichever axis the adjudicator's DOMINANT ethos/pathos/logos weight favours, mapped via the corpus
       Aristotelian chain (see _GUILDS_APPEAL_TO_BOOST). Returns (boost_value, axis) e.g. ('Memory','Genre')
       for a logos-dominant Expert Judge / Panel, ('Projection','Genre') for a pathos-dominant Crowd,
       ('Revealing','Orientation') for an ethos-dominant No-adjudicator. Deterministic (ties broken by the
       Aristotelian appeal order logos>pathos>ethos); no GM, no orator pick, no randomness. RESOLVES NOTHING
       in the contest — it only names which axis the +1D Audience boost attaches to at setup."""
    char = adjudicator.character()   # {'ethos':.., 'pathos':.., 'logos':..} — Panel averages its members
    # Dominant appeal = the heaviest char weight; ties broken by Aristotelian order (logos, pathos, ethos).
    order = (Appeal.LOGOS, Appeal.PATHOS, Appeal.ETHOS)
    dominant = max(order, key=lambda a: (char.get(a, 0.0), -order.index(a)))
    return _GUILDS_APPEAL_TO_BOOST[dominant]


# ══════════════════════════════════════════════════════════════════════════════════════════
# 4. PROCEEDING ×8  (params/contest.md §Proceeding Types; social_contest_v30 §2 Step 5)
# ══════════════════════════════════════════════════════════════════════════════════════════
# The typed surface over modes.PROCEEDINGS. ANTI-FABRICATION (CLAUDE.md §7): the NUMERIC structural
# fields (exchange_count, track_start, tracker_mode, adjudicator_type) are NOT re-typed as literals
# here — they are READ FROM the already-canonical, already-cited modes.PROCEEDINGS registry (Stage 1c,
# each row citing params/contest.md §Proceeding Types + the Church-Tribunal §7 bias). This makes the
# typed surface a genuine VIEW over the cited registry (no duplicated number to drift or fabricate) and
# is why _crosscheck_proceedings() is guaranteed empty by construction. Only the human-readable prose
# LABELS (role_structure / resistance_modifier — verbatim from the §Proceeding Types "Roles" /
# "Resistance Mod" columns) and the authored `flavor` (locked decision 5) live locally.

@dataclass(frozen=True)
class Proceeding:
    """One of the eight canonical proceedings (params/contest.md §Proceeding Types). Numeric structural
       fields are READ from modes.PROCEEDINGS (the cited registry — no re-typed literals); `role_structure`
       / `resistance_modifier` are the verbatim §Proceeding Types prose labels; `flavor` is authored UI
       copy (locked decision 5). `mechanical_key` binds to modes.PROCEEDINGS (the resolving registry)."""
    key: str
    name: str
    exchange_count: Tuple[int, int]  # (min, max) <- READ FROM modes.PROCEEDINGS["exchanges"] (cited registry)
    role_structure: str              # <- params §Proceeding Types "Roles" (prose label)
    resistance_modifier: str         # <- params §Proceeding Types "Resistance Mod" (prose label)
    adjudicator_type: str            # <- READ FROM modes.PROCEEDINGS["adjudicator"] (key into ADJUDICATORS_TABLE)
    track_start: float               # <- READ FROM modes.PROCEEDINGS["track_start"] (cited; §7 Church bias)
    tracker_mode: str                # <- READ FROM modes.PROCEEDINGS["tracker_mode"] (canonical tri-state)
    mechanical_key: str              # key into modes.PROCEEDINGS
    flavor: str                      # authored UI-card copy (locked decision 5; behaviorally honest)
    source: str

# Local prose labels + authored flavor ONLY. Every numeric field is pulled from modes.PROCEEDINGS below.
# `role_structure`/`resistance_modifier` are the verbatim params §Proceeding Types "Roles"/"Resistance
# Mod" column text; `flavor` is authored this stage (locked decision 5; behaviorally honest per Lens 6).
_PROCEEDING_PROSE = {
    "formal_contest": dict(
        name="Formal Contest", role_structure="Alternating", resistance_modifier="Standard",
        # Behaviorally honest: alternating exchanges before a Crowd (Charisma-primary, delivery-swayed),
        # standard resistance, tracked to the Persuasion band. A short, symmetric public bout. NB no
        # BALLOT here — a Formal Contest resolves on the Persuasion-Track band, not a vote (the vote
        # mechanic belongs to the Panel/VoteAtClose adjudicator + §10 BG Parliamentary Vote); the flavor
        # must not name a vote the primitive does not run (Lens-6 behavioral honesty, finding 5).
        flavor="Three rounds before the assembly. Take turns, win the room, and let the track fall where the argument lands."),
    "grand_contest": dict(
        name="Grand Contest", role_structure="Alternating", resistance_modifier="Standard",
        # Behaviorally honest: more exchanges than Formal, before a Crowd — the faction-defining bout; the
        # longer track and per-source Recall (ED-617) make it a war of attrition, not a sprint.
        flavor="Five rounds, and the faction's course rides on them. Pace yourself; a citation spent early cannot be spent again."),
    "royal_audience": dict(
        name="Royal Audience", role_structure="Crown objects throughout", resistance_modifier="Halved for petitioner",
        # Behaviorally honest: asymmetric — the Crown objects throughout (roles do NOT alternate, §7), an
        # Expert Judge weighs merits, and the petitioner's uphill fight is eased by HALVED resistance (§7).
        # NB adjudicator is a SINGLE Expert Judge (one authority), NOT a Panel — the flavor must not say
        # "bench"/"panel"/"judges" (those cue a deliberating multi-judge body, the reserved Panel term,
        # v30:37; Lens-6 adjudicator-cardinality honesty, finding 7). "The judge" names the one authority.
        flavor="You petition; the Crown objects at every turn. The judge is stern, but the throne's resistance is halved for the one who comes asking."),
    "church_tribunal": dict(
        name="Church Tribunal", role_structure="Inquisitor proposes throughout", resistance_modifier="Halved for accused",
        # Behaviorally honest: the Inquisitor sets the length and proposes throughout; the track starts
        # BIASED against the accused (§7), whose resistance is halved to compensate; the Church boosts
        # Obscuring, so the Inquisitor's foreclosing arguments carry institutional weight.
        flavor="The Inquisitor sets the terms and speaks first, and the room already leans against you. Halved resistance is the only mercy; every doubt they plant is meant to stick."),
    "guild_arbitration": dict(
        name="Guild Arbitration", role_structure="Symmetric before bench", resistance_modifier="Standard",
        # Behaviorally honest (Lens 6): symmetric (both sides equal before the arbiters — unlike the
        # asymmetric Royal Audience / Tribunal), standard resistance, and — ED-1059 REBIND (Gate B) — a
        # PANEL of guild masters (not a single Expert Judge). The verdict is the Panel's weighted-by-
        # standing ballot (ED-1057): each master weighs the case and the bench's weighted majority decides,
        # so the flavor NAMES the bench/masters honestly (the finding-7 no-bench guard is scoped to the
        # SEVEN single-authority/Crowd proceedings; Guild Arbitration is the one Panel-bearing proceeding
        # and may — must — name its bench). Canon flavor already said "Masters arbitrate" (plural).
        flavor="A fair table before a bench of guild masters. Both sides stand equal; three rounds, and the masters weigh the stronger case among themselves."),
    "casual_dispute": dict(
        name="Casual Dispute", role_structure="Initiator proposes", resistance_modifier="N/A",
        # Behaviorally honest: a single exchange, no adjudicator, NO tracker at all (§2:87 "no tracker") —
        # the single exchange's majority decides. The lightest possible proceeding.
        flavor="One exchange, no judge, no scorekeeping. Make your point, hear theirs, and the stronger showing settles it on the spot."),
    "private_negotiation": dict(
        name="Private Negotiation", role_structure="Symmetric", resistance_modifier="N/A",
        # Behaviorally honest: symmetric exchanges, no adjudicator; the tracker is OPTIONAL (§2:88) — a
        # build/venue setting (off by default → exchange-majority; opt-in for a scored bargain), NOT an
        # in-fiction pact between the two orators. Canon (v30:76) makes the tracker simply optional with NO
        # mutual-consent language — so the copy must NOT say "if you both agree to" (finding 2: that invents a
        # two-party consent gate on the Persuasion Track that does not exist; Lens-6 fabrication-class break).
        # Reading the counterpart (Attunement-primary) is everything; a stalled negotiation is itself a
        # consequential outcome (§2:76 "failure to agree IS a consequential outcome") — that honest note stays.
        flavor="Just the two of you, up to three rounds, no judge and no fixed scorekeeping. Read them well, because failing to agree is its own answer."),
    "personal_appeal": dict(
        name="Personal Appeal", role_structure="Appealer proposes", resistance_modifier="N/A",
        # Behaviorally honest: a single exchange, no adjudicator, tracker optional (§2:89). One plea to one
        # person; you read them (Attunement-primary) and make the case land in the one chance you get.
        flavor="One plea, one chance, no one to referee it. Read the person in front of you and make it count the first time."),
}

def _build_proceedings_table():
    """Assemble PROCEEDINGS_TABLE by READING every numeric structural field from the cited mechanical
       registry modes.PROCEEDINGS (no re-typed literals — anti-fabrication), joined with the local prose
       labels + authored flavor in _PROCEEDING_PROSE. Iterates modes.PROCEEDINGS so the typed surface can
       never omit or invent a proceeding."""
    table = {}
    for key, m in _modes.PROCEEDINGS.items():
        prose = _PROCEEDING_PROSE[key]
        table[key] = Proceeding(
            key=key, name=prose["name"],
            exchange_count=tuple(m["exchanges"]),          # <- modes.PROCEEDINGS (cited registry)
            role_structure=prose["role_structure"], resistance_modifier=prose["resistance_modifier"],
            adjudicator_type=m["adjudicator"],             # <- modes.PROCEEDINGS
            track_start=float(m["track_start"]),           # <- modes.PROCEEDINGS
            tracker_mode=m["tracker_mode"],                # <- modes.PROCEEDINGS
            mechanical_key=key, flavor=prose["flavor"],
            source="params/contest.md §Proceeding Types + social_contest_v30 §2 Step 5 "
                   "(numeric fields read from modes.PROCEEDINGS, the Stage-1c cited registry)")
    return table

PROCEEDINGS_TABLE = _build_proceedings_table()


# ── Cross-check helper: assert the typed surface agrees with the mechanical modes.PROCEEDINGS ──
def _crosscheck_proceedings():
    """Return a list of (proceeding_key, field, typed_value, mechanical_value) mismatches between
       PROCEEDINGS_TABLE (typed surface) and modes.PROCEEDINGS (mechanical registry). Empty list =>
       the surface and the substrate agree. Asserted by _kernel_tests.py so drift is a test failure."""
    out = []
    for k, p in PROCEEDINGS_TABLE.items():
        m = _modes.PROCEEDINGS.get(k)
        if m is None:
            out.append((k, "exists", "present", "MISSING")); continue
        if tuple(p.exchange_count) != tuple(m["exchanges"]):
            out.append((k, "exchange_count", p.exchange_count, m["exchanges"]))
        if p.adjudicator_type != m["adjudicator"]:
            out.append((k, "adjudicator_type", p.adjudicator_type, m["adjudicator"]))
        if float(p.track_start) != float(m["track_start"]):
            out.append((k, "track_start", p.track_start, m["track_start"]))
        if p.tracker_mode != m["tracker_mode"]:
            out.append((k, "tracker_mode", p.tracker_mode, m["tracker_mode"]))
    return out


# ══════════════════════════════════════════════════════════════════════════════════════════
# 5. PANEL CLOSURE — ED-137 ("Panel adjudicator mechanics not yet designed; use Expert Judge as
#    provisional") CLOSED (Gate B, 2026-07-01; ED-1057).
# ══════════════════════════════════════════════════════════════════════════════════════════
# WHAT ED-137 LEFT OPEN: social_contest_v30 §2 Step 1 defines Panel as "Multiple individual judges
# deliberating" but stubbed the mechanics as "[EDITORIAL: ED-137 — panel mechanics not yet designed.
# Use Expert Judge as provisional.]" So a Panel resolved IDENTICALLY to a single Expert Judge — the
# "multiple individual judges deliberating" was nominal, not realized.
#
# WHAT CLOSES IT: the groundup engine already ships the mechanism — `VoteAtClose` (resolver.py). A
# Panel is a `contract.Panel` (a tuple of individual `Adjudicator`s); VoteAtClose is a terminal
# win-condition that polls each member as a SEPARATE ballot and takes the majority. This realizes
# "multiple individual judges deliberating" literally:
#   - the running `adv` (the room's momentum) drives each juror's LEAN, but
#   - the VERDICT is a per-member ballot at close: juror i votes A iff (sharpness·gap + per-juror
#     noise) > 0, so a juror can cross AGAINST the room — a lopsided room is near-unanimous, a close
#     room is near a coin-flip. This is exactly the "deliberating bench" the ED-137 stub deferred:
#     the members are individuals with independent votes, not one fused scalar. Those ballots are
#     aggregated WEIGHTED-BY-STANDING (ED-1057, ratified — see below), each counted by its juror's
#     bench-weight. Panel is reached by SELECTING Guild Arbitration (ED-1059 rebind, ratified).
# The Panel character/discipline still drives the running momentum via the bench's MEAN disposition
# (contract.Panel.character()/discipline aggregate the members), so both halves — momentum AND the
# terminal deliberative ballot — are member-derived. This is real, promoted mechanics, not a re-skin
# of Expert Judge.
#
# AGGREGATION RULE — RATIFIED WEIGHTED-BY-STANDING (Jordan, Gate B, ED-1057):
# "Multiple judges deliberating" does not, by itself, settle HOW the individual votes aggregate into
# a verdict. The ratified corpus fixes no peer-bench rule, so Jordan chose. THE RATIFIED RULE is
# WEIGHTED-BY-STANDING: each juror's ballot counts in proportion to that juror's BENCH-WEIGHT — its
# institutional rank/rigor on THIS bench — not one-juror-one-vote.
#
# THE WEIGHT REUSES AN EXISTING PRIMITIVE (no invented per-juror state). A juror's bench-weight is its
# EXISTING Adjudicator.discipline (0–1) — the per-juror rigor field the groundup Adjudicator already
# carries (contract.Adjudicator.discipline; a trained theologian is high-discipline, a crowd member
# low). Correlating the legacy candidates first (session discipline: prefer an existing composite over a
# new proxy): discipline is the ONLY per-juror scalar that reads as institutional weight — the char_
# ethos/pathos/logos weights are the juror's proof-type TASTE (which appeal it credits), not its rank,
# and would mis-weight a bench by rhetorical preference rather than authority. So discipline is the
# legitimate reuse.
#
# NAMING (collision hazard, explicitly avoided): the contest kernel already has a contestant-side
# `Standing` primitive (primitives.Standing: 0–10, ethos-built, feeds Face — in-contest credibility). A
# JUROR'S standing/weight on the bench is a DIFFERENT concept (institutional rank on the panel, not
# in-contest credibility). This code NEVER reuses the class name `Standing` for it — the juror weight is
# named "bench-weight" and is sourced from Adjudicator.discipline, so the Persuasion/Piety-style name
# collision this corpus was burned by is not recreated.
#
# THE THRESHOLD (resolver.VoteAtClose weighted branch): A wins iff the summed BENCH-WEIGHT of the jurors
# who vote A > half the total bench weight; else draw. This keeps Panel NON-DOMINATED vs a single Expert
# Judge: a mixed-weight bench does not simply mirror its highest-weight juror — a low-weight juror
# crossing the room can still swing a near-even split, and the summed-weight threshold (not one dominant
# vote) decides, so a plausibly-mixed bench can go either way (asserted by the seeded kernel test).
#
# Alternatives (recorded, NOT chosen): (a) simple majority (one-juror-one-vote; the corpus offers the
# §7.2 Crown "majority Disposition" as the lone plain-majority-of-individuals analogue) and (c)
# unanimity-required (would make Panel strictly harder to win than Expert Judge — a dominance asymmetry).
# Jordan rejected simple-majority as the default and selected weighted-by-standing.

PANEL_AGGREGATION = "weighted_by_standing"   # RATIFIED (Jordan, Gate B, ED-1057). Alternatives recorded
                                             #   (not chosen): a) simple_majority | c) unanimity_required

# [SEED] deliberation parameters — how the bench's terminal ballot behaves. NOT canon (canon fixes
# only that Panel = deliberating individual judges + Cognition-primary); Jordan calibrates. They are
# the resolver.VoteAtClose CONSTRUCTOR DEFAULTS (sharpness/noise) — single-sourced there (already the
# cited groundup [SEED]s), NOT re-typed here as fresh literals (anti-fabrication). sharpness = how
# strongly the room's momentum pulls each juror's vote; noise = juror independence.
# PANEL_DEFAULT_JURORS: a Panel's default bench size when no paired contract.Panel supplies a member
# count. Read from the modes.panel() factory's own default (Panel(size=5)) rather than re-typed here,
# so the one bench-size literal lives once, in the cited modes.panel constructor.
import inspect as _inspect
PANEL_DEFAULT_JURORS = _inspect.signature(_modes.panel).parameters["size"].default  # <- modes.panel(size=…)

def panel_win_condition(jurors=None, aggregation=PANEL_AGGREGATION):
    """Build the terminal win-condition that closes ED-137 for the Panel adjudicator: a per-member
       deliberative ballot (VoteAtClose), aggregated by the RATIFIED weighted-by-standing rule (each
       juror's ballot counts by its bench-weight = its Adjudicator.discipline; A wins iff summed A-weight
       > half total weight, else draw). `jurors` is the bench size (default: the modes.panel() bench size
       PANEL_DEFAULT_JURORS; at resolve time VoteAtClose reads the paired contract.Panel's actual members
       for both the count AND the per-juror weights). sharpness/noise are left at VoteAtClose's own cited
       [SEED] defaults (not re-specified here). `aggregation` selects the rule (PANEL_AGGREGATION);
       'weighted_by_standing' (ratified) and 'simple_majority' are implemented; 'unanimity_required'
       raises (the sketched alternative Jordan did not select). RESOLVES NOTHING here — it returns the
       WinCondition the venue would carry."""
    if aggregation not in ("weighted_by_standing", "simple_majority"):
        raise NotImplementedError(
            f"Panel aggregation {aggregation!r} is not implemented; the ratified rule is "
            f"'weighted_by_standing' (Gate B, ED-1057), and 'simple_majority' is the recorded "
            f"alternative. 'unanimity_required' was sketched but not selected. See PANEL_CLOSURE.")
    n = PANEL_DEFAULT_JURORS if jurors is None else jurors
    # sharpness/noise left at VoteAtClose's own cited [SEED] defaults; aggregation is the ratified rule.
    return _VoteAtClose(jurors=n, aggregation=aggregation)

PANEL_CLOSURE = {
    "ed": "ED-137",
    "status": "CLOSED (Gate B 2026-07-01, ED-1057; ratified by Jordan)",
    "was": "Panel adjudicator mechanics not yet designed — use Expert Judge as provisional (ED-137).",
    "now": "Panel = a bench of individual Adjudicators deliberating to a terminal VoteAtClose "
           "per-member ballot; running momentum drives each juror's lean, the verdict is the "
           "weighted majority of independent ballots (each juror's ballot counts by its bench-weight "
           "= its Adjudicator.discipline). VoteAtClose is the promoted groundup mechanism.",
    "aggregation": PANEL_AGGREGATION,
    "aggregation_ratified": "WEIGHTED-BY-STANDING (Jordan, Gate B, ED-1057): each juror's ballot counts "
                            "by its bench-weight = its existing Adjudicator.discipline (institutional "
                            "rank/rigor on the bench — NOT the contestant-side Standing primitive); A "
                            "wins iff summed A-weight > half total bench weight, else draw. No invented "
                            "per-juror state; keeps Panel non-dominated vs a single Expert Judge. "
                            "Alternatives simple_majority / unanimity_required recorded, not chosen.",
    # REACHABILITY (finding 3, ED-1059) — RATIFIED REBIND (Jordan, Gate B): Guild Arbitration's
    # adjudicator_type is REBOUND from expert_judge to PANEL, so the closed Panel mechanic is now reached
    # by SELECTING an existing canonical proceeding (no longer dead-through-normal-play). This closes the
    # ORIGINAL ED-137 note ("Panel not yet designed; use Expert Judge as provisional") exactly as it always
    # pointed — Guild Arbitration's flavor already said "Masters arbitrate" (plural), i.e. a seated bench,
    # so this is a CLOSURE of the provisional stand-in, not a new invention. Jordan explicitly REJECTED an
    # appeal/escalation flag ("appeals should not be a thing — let the decision ride"). The 8-proceeding
    # roster is UNCHANGED: this is a one-field rebind on an existing proceeding, not a new proceeding or an
    # appeal step. The rebind lives in modes.PROCEEDINGS["guild_arbitration"]["adjudicator"] = "panel"; the
    # typed PROCEEDINGS_TABLE reads it through (no drift), so Guild Arbitration now routes to the Panel
    # VoteAtClose weighted ballot.
    "reachability_status": "PANEL-REACHABLE via Guild Arbitration (rebound expert_judge -> panel, Gate B, "
                           "ED-1059): selecting the Guild Arbitration proceeding now instantiates the Panel "
                           "adjudicator. No appeal mechanic; 8-proceeding roster unchanged.",
    "reachability_ratified": "REBIND Guild Arbitration expert_judge -> panel (Jordan, Gate B, ED-1059). "
                             "Appeal/escalation flag explicitly REJECTED ('let the decision ride'). One-field "
                             "rebind on an existing proceeding; closes the original ED-137 'use Expert Judge "
                             "as provisional' note ('Masters arbitrate' = a seated bench).",
    "mechanism": "resolver.VoteAtClose (per-member weighted ballot); contract.Panel (member aggregation "
                 "for momentum + per-juror bench-weight)",
    "source": "social_contest_v30 §2 Step 1 (Panel row) + §7.2 (institutional-body vote precedent); "
              "resolver.VoteAtClose (groundup, promoted); ED-1057 (aggregation) + ED-1059 (rebind)",
}

