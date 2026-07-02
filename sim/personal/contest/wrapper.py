"""
sim/personal/contest/wrapper.py — public API wrapper for the social-contest engine.

Mirrors tests/sim/mass_battle/engine.py: the wrapper ADAPTS + ROUTES; it RESOLVES NOTHING.
  • build_contest(...)  — the side→Contestant + proceeding→Venue/Adjudicator ADAPTER (the P1 seam:
    turns world/faction inputs into the kernel's Contestant/Venue/Adjudicator specs; no outcome logic).
  • resolve_contest(...) — the game-type ROUTER: dispatches to the kernel resolution path for the
    named game. game='agon' routes to the canonical Persuasion-Track path (the promoted kernel Bout).
    The other three games (consensus/negotiation/inquiry) are registered STUB rows for later stages.
  • MECHANICS — a registry of canonical mechanic -> implementing symbol + toggle + canonical source +
    status, with a mechanics_selftest asserting every WIRED mechanic resolves.

GM-REMOVAL: canon §2 is titled "GM SETUP", but Valoria has no GM — the engine resolves. Every §2
setup choice (adjudicator type, exchange count, resistance modifier, track start) is folded into the
named proceeding (modes.PROCEEDINGS) and set HERE from the proceeding, never by a GM.

Stage: 1c (designs/audit/2026-06-30-contest-stage0-reconciliation/DECISIONS.md — Stage-1 entry criterion 3).
No number crosses into this file un-cited; every venue/adjudicator parameter traces to modes.py, which
traces to params/contest.md + social_contest_v30.md §2/§3.
"""
from __future__ import annotations

from .contract import A, B, Adjudicator, Panel
from .primitives import Stasis, Standing, Face, Dossier, EvidenceItem, TRACKERS, RETIRED_TRACKERS
from .resolver import (Bout, Contestant, Venue, run, PersuasionTrack, TallyAtClose,
                       ThresholdRace, ProofBar, GraceThreshold, VoteAtClose)
from .modes import (ContestedMode, PROCEEDINGS, CANONICAL_PROCEEDINGS, CANONICAL_ADJUDICATORS,
                    ADJUDICATOR_PRIMARY, proceeding_venue, proceeding_mode,
                    CANONICAL_TRACK_START)
from .policy import POLICIES, logos_spammer

__all__ = ["build_contest", "resolve_contest", "Contest", "MECHANICS", "mechanics_selftest", "GAMES"]


# ─── Resistance derivation (params/contest.md §Persuasion Track) ──────────────────────────────────
# "Audience resistance: average Stability of factions (round up) − 1, minimum 0." The proceeding's
# resistance MODIFIER scales it: Standard = ×1, Halved (Royal Audience / Church Tribunal) = ÷2 for the
# advantaged party, N/A = 0 (untracked proceedings). Numeric resistance is derived from WORLD Stability
# passed in at build time — never fabricated. Returns None when the proceeding has no tracker.
def _derive_resistance(proc_name, world):
    spec = PROCEEDINGS[proc_name]
    if not spec["tracker"] or spec["resistance"] == "none":
        return None
    stabilities = (world or {}).get("stabilities") if isinstance(world, dict) else None
    if not stabilities:
        return 0  # no world Stability supplied → canonical minimum (params/contest.md: "minimum 0")
    import math
    base = max(0, math.ceil(sum(stabilities) / len(stabilities)) - 1)  # §Persuasion Track formula
    if spec["resistance"].startswith("halved"):
        # social_contest_v30 §7:320 verbatim: "halved resistance (round up)". Use ceil, NOT floor:
        # base=3 -> 2 (not 1); base=1 -> 1 (not 0). floor() is an off-by-one for odd base.
        base = math.ceil(base / 2)  # "Halved for petitioner/accused (round up)" (social_contest_v30 §7)
    return base


class Contest:
    """The ADAPTER's output: a fully-built, not-yet-resolved contest. Holds the kernel specs
       (Contestant a/b, Venue, Adjudicator) + the canonical metadata the router/consumers read
       (game, proceeding, adjudicator type + its primary attribute, derived resistance, track start).
       RESOLVES NOTHING — resolve_contest(contest) runs it."""
    def __init__(self, *, side_a, side_b, venue, adjudicator, game, proceeding,
                 adjudicator_type, primary_attribute, resistance, track_start, stakes=None):
        self.side_a = side_a
        self.side_b = side_b
        self.venue = venue
        self.adjudicator = adjudicator
        self.game = game
        self.proceeding = proceeding
        self.adjudicator_type = adjudicator_type
        self.primary_attribute = primary_attribute   # §3 Argue Pool: which attribute (PrimaryAttr×2)+H doubles
        self.resistance = resistance                  # §Persuasion Track derived audience resistance (or None).
                                                       # METADATA-ONLY this stage (F10): carried for display/authoring
                                                       # but NOT plumbed into resolution — the resolver reads no
                                                       # resistance and Venue.base_ob is not set from it. Wiring it is
                                                       # the reserved ED stub (contest_rebuild, ED-1055..1079).
        self.track_start = track_start                # §2 Step 4 Persuasion-Track start
        self.stakes = stakes or {}


def _as_contestant(side):
    """Coerce a side spec into a kernel Contestant. Accepts a Contestant (pass-through), an int/float
       faculty, or a dict {faculty, standing_start, evidence:[(ground,weight),...] | dossier}. The
       ADAPTER's only shaping duty; no resolution."""
    if isinstance(side, Contestant):
        return side
    if isinstance(side, (int, float)):
        return Contestant(int(side))
    if isinstance(side, dict):
        faculty = int(side.get("faculty", 4))
        standing = float(side.get("standing_start", Standing.START))
        dossier = side.get("dossier")
        if dossier is None and side.get("evidence"):
            dossier = Dossier([EvidenceItem(g, w) for (g, w) in side["evidence"]])
        return Contestant(faculty, standing_start=standing, dossier=dossier)
    raise TypeError(f"build_contest: cannot adapt side spec {side!r} "
                    f"(expected Contestant | int | dict)")


def build_contest(side_a, side_b, *, venue, adjudicator=None, stakes=None, world=None,
                  use_tracker=None):
    """Faction/side → Contest ADAPTER (the wrapper's adapter duty). `venue` names a canonical proceeding
       (a key of modes.PROCEEDINGS, e.g. 'formal_contest') OR is a prebuilt Venue. `adjudicator` names a
       canonical adjudicator type (a key of CANONICAL_ADJUDICATORS) OR is a prebuilt Adjudicator/Panel OR
       None (defaults to the proceeding's canonical adjudicator). A prebuilt contract.Panel that is NOT
       already bound to a proceeding's canonical adjudicator is treated as the 'panel' type, so it too
       closes ED-137 via the VoteAtClose ballot (a named proceeding's own adjudicator is never
       overridden). `use_tracker` is the tracker tri-state
       opt-in (social_contest_v30 §2:88-89): None keeps the proceeding's canonical default (Private
       Negotiation / Personal Appeal default to exchange-majority TallyAtClose); True opts an "optional"
       proceeding IN to the Persuasion Track. Derives audience resistance from `world` Stability per
       params/contest.md §Persuasion Track. Builds the kernel specs; RESOLVES NOTHING — hand the result
       to resolve_contest."""
    ca = _as_contestant(side_a)
    cb = _as_contestant(side_b)

    if isinstance(venue, str):
        proc_name = venue
        if proc_name not in PROCEEDINGS:
            raise ValueError(f"build_contest: unknown proceeding {proc_name!r}; "
                             f"valid: {sorted(PROCEEDINGS)}")
        spec = PROCEEDINGS[proc_name]
        the_venue = proceeding_venue(proc_name, use_tracker=use_tracker)
        adj_type = spec["adjudicator"]
        track_start = spec["track_start"]
    else:
        if use_tracker is not None:
            raise ValueError("build_contest: use_tracker only applies to a named canonical proceeding "
                             "(the tracker tri-state lives on the proceeding); a prebuilt Venue already "
                             "fixes its own win-condition.")
        proc_name = None
        the_venue = venue
        adj_type = None
        track_start = getattr(getattr(venue, "win", None), "start", CANONICAL_TRACK_START)

    # Adjudicator: explicit type name / explicit object / proceeding default.
    if adjudicator is None:
        if adj_type is None:
            the_adj = Adjudicator()
        else:
            the_adj = CANONICAL_ADJUDICATORS[adj_type]()
    elif isinstance(adjudicator, str):
        if adjudicator not in CANONICAL_ADJUDICATORS:
            raise ValueError(f"build_contest: unknown adjudicator type {adjudicator!r}; "
                             f"valid: {sorted(CANONICAL_ADJUDICATORS)}")
        adj_type = adjudicator
        the_adj = CANONICAL_ADJUDICATORS[adjudicator]()
    else:
        the_adj = adjudicator  # prebuilt Adjudicator | Panel
        # A caller may pass a prebuilt contract.Panel object instead of the string 'panel'. Tag it so
        # the ED-137 closure below fires — but ONLY when adj_type is still None (a proceeding that
        # already carries a canonical adjudicator, e.g. the crowd-proceeding path, keeps its type).
        # NB crowd is itself a Panel subtype (isinstance(crowd, Panel) is True), so guarding on
        # adj_type is None is what keeps a Crowd proceeding on PersuasionTrack rather than VoteAtClose.
        if isinstance(adjudicator, Panel) and adj_type is None:
            adj_type = "panel"

    primary = ADJUDICATOR_PRIMARY.get(adj_type) if adj_type else None
    resistance = _derive_resistance(proc_name, world) if proc_name else None

    # ── ED-137 CLOSURE (Gate B, ED-1057): a Panel adjudicator deliberates to a terminal per-member
    # VoteAtClose ballot (dictionaries.panel_win_condition), NOT the flat single-judge track. This is
    # the promoted groundup mechanism realizing "multiple individual judges deliberating"
    # (social_contest_v30 §2 Step 1). ADDITIVE: none of the 8 canonical PROCEEDINGS map to the `panel`
    # adjudicator, so this fires ONLY when a caller selects the Panel adjudicator — either by
    # adjudicator='panel' (string), or by passing a prebuilt contract.Panel object that isn't already
    # bound to a proceeding's canonical adjudicator (the adj_type-is-None tag set above). A named
    # proceeding's own adjudicator (e.g. crowd, which is itself a Panel subtype) is NOT overridden, so
    # no existing proceeding's win-condition changes. The aggregation rule (weighted-by-standing) is
    # RATIFIED (Jordan, Gate B, ED-1057); see dictionaries.PANEL_CLOSURE.
    if adj_type == "panel":
        from .dictionaries import panel_win_condition
        import dataclasses as _dc
        # Bench size = the paired Panel's actual member count; None => panel_win_condition falls back to
        # its cited default (modes.panel bench size). No re-typed literal here.
        n_jurors = len(the_adj.members) if isinstance(the_adj, Panel) else None
        # Rebuild the venue with the VoteAtClose deliberation win-condition (a Venue is a dataclass;
        # replace only `win`, leaving every other venue parameter — proof/temporal weights, budget,
        # faults — as the proceeding/prebuilt venue set them).
        the_venue = _dc.replace(the_venue, win=panel_win_condition(jurors=n_jurors))

    return Contest(side_a=ca, side_b=cb, venue=the_venue, adjudicator=the_adj,
                   game="agon", proceeding=proc_name, adjudicator_type=adj_type,
                   primary_attribute=primary, resistance=resistance,
                   track_start=track_start, stakes=stakes)


# ─── GAMES ROUTER TABLE ───────────────────────────────────────────────────────────────────────────
# game -> {resolve, status, source}. status: WIRED | STUB. Only 'agon' is WIRED this stage (the
# canonical Persuasion-Track path). The other three games are registered STUB rows for later stages
# (Stage 4 Consensus is largely promote-existing per faction.py; Negotiation/Inquiry author-new).
def _resolve_agon(contest, *, policy_a, policy_b, record=False):
    """Route game='agon' to the canonical agôn path: the promoted-kernel Bout on the proceeding's Venue
       + Adjudicator, resolving on the Persuasion-Track banding (or exchange-majority for untracked
       proceedings). Transparent pass-through — the outcome is computed by the kernel, not here."""
    bout = Bout(contest.side_a, contest.side_b, contest.venue, contest.adjudicator, record=record)
    return bout.resolve(policy_a, policy_b), bout


def _stub(game):
    def _f(contest, **kw):
        raise NotImplementedError(
            f"resolve_contest: game={game!r} is a registered STUB (Stage 1c) — not yet wired. "
            f"Only game='agon' resolves this stage (see DECISIONS.md Stage-1 entry criteria).")
    return _f

GAMES = {
    "agon":        {"resolve": _resolve_agon,          "status": "WIRED",
                    "source": "social_contest_v30 §2-§6 (Persuasion Track); DECISIONS.md D0-1/Stage-1"},
    "consensus":   {"resolve": _stub("consensus"),     "status": "STUB",
                    "source": "social_contest_v30 §10 BG-Vote / §7.2 (largely in faction.py — Stage 4)"},
    "negotiation": {"resolve": _stub("negotiation"),   "status": "STUB",
                    "source": "social_contest_v30 §2 Private Negotiation (author-new — later stage)"},
    "inquiry":     {"resolve": _stub("inquiry"),       "status": "STUB",
                    "source": "social_contest_v30 §7 Church Tribunal / Inquisition (author-new — later stage)"},
}


def resolve_contest(contest, *, game="agon", policy_a=logos_spammer, policy_b=logos_spammer,
                    record=False):
    """Game-type ROUTER (the wrapper's routing duty). Dispatches to GAMES[game]['resolve']; it computes
       no outcome itself. game='agon' resolves the canonical Persuasion-Track contest; the other three
       games are STUBs (raise NotImplementedError) pending later stages. `policy_a`/`policy_b` name a
       key of modes/policy.POLICIES or are policy callables. Returns ((winner_band, reason), bout)."""
    if game not in GAMES:
        raise ValueError(f"resolve_contest: unknown game {game!r}; valid: {sorted(GAMES)}")
    pa = POLICIES[policy_a] if isinstance(policy_a, str) else policy_a
    pb = POLICIES[policy_b] if isinstance(policy_b, str) else policy_b
    return GAMES[game]["resolve"](contest, policy_a=pa, policy_b=pb, record=record)


# ─── MECHANICS registry — name -> {fn, toggle, source, status} ────────────────────────────────────
# status: WIRED | PARTIAL | STUB. Mirrors mass_battle.engine.MECHANICS. Every WIRED row's `fn` must
# resolve to a real symbol in this package (mechanics_selftest asserts it). `source` cites the
# canonical prose/param head the mechanic implements.
_SYMBOLS = {
    "build_contest": build_contest, "resolve_contest": resolve_contest,
    "proceeding_venue": proceeding_venue, "proceeding_mode": proceeding_mode,
    "PROCEEDINGS": PROCEEDINGS, "CANONICAL_ADJUDICATORS": CANONICAL_ADJUDICATORS,
    "ADJUDICATOR_PRIMARY": ADJUDICATOR_PRIMARY,
    "PersuasionTrack": PersuasionTrack, "TallyAtClose": TallyAtClose,
    "ProofBar": ProofBar, "GraceThreshold": GraceThreshold, "VoteAtClose": VoteAtClose,
    "Bout": Bout, "_derive_resistance": _derive_resistance,
    # CR3 three-tracker model (RATIFIED_2026-06-01.md CR3)
    "Face": Face, "TRACKERS": TRACKERS,
}
# Stage 2 / Gate B typed dictionaries (imported lazily to avoid a cycle: dictionaries imports modes,
# which the wrapper already imports; the dictionaries import resolver, already imported above).
from . import dictionaries as _dict
_SYMBOLS.update({
    "STYLES_TABLE": _dict.STYLES_TABLE, "INTERACTIONS_TABLE": _dict.INTERACTIONS_TABLE,
    "derive_interaction": _dict.derive_interaction, "ADJUDICATORS_TABLE": _dict.ADJUDICATORS_TABLE,
    "FACTION_BOOSTS": _dict.FACTION_BOOSTS, "PROCEEDINGS_TABLE": _dict.PROCEEDINGS_TABLE,
    "panel_win_condition": _dict.panel_win_condition, "PANEL_CLOSURE": _dict.PANEL_CLOSURE,
})
def _resolve(sym):
    return _SYMBOLS.get(sym)

MECHANICS = {
    # adapter / router (the wrapper's own duties)
    "build_contest":       {"fn":"build_contest",    "toggle":None, "source":"social_contest_v30 §2 (GM setup -> venue-intrinsic; GM-removed)", "status":"WIRED"},
    "resolve_contest":     {"fn":"resolve_contest",  "toggle":None, "source":"DECISIONS.md Stage-1 entry #3 (mirrors mass_battle.engine)", "status":"WIRED"},
    # canonical proceeding re-skin (params/contest.md §Proceeding Types)
    "proceeding_venue":    {"fn":"proceeding_venue", "toggle":None, "source":"params/contest.md §Proceeding Types + social_contest_v30 §2 Step 5", "status":"WIRED"},
    "proceeding_registry": {"fn":"PROCEEDINGS",      "toggle":None, "source":"params/contest.md §Proceeding Types (8 canonical proceedings)", "status":"WIRED"},
    # canonical adjudicator re-skin (social_contest_v30 §2 Step 1 / §3)
    "adjudicator_types":   {"fn":"CANONICAL_ADJUDICATORS", "toggle":None, "source":"social_contest_v30 §2 Step 1 (Expert/Crowd/No-adj/Panel)", "status":"WIRED"},
    "adjudicator_primary": {"fn":"ADJUDICATOR_PRIMARY",    "toggle":None, "source":"social_contest_v30 §3 Argue Pool (Cognition/Charisma/Attunement)", "status":"WIRED"},
    # persuasion-track banding + resistance
    "persuasion_track":    {"fn":"PersuasionTrack",  "toggle":None, "source":"params/contest.md §Persuasion Track (>=9/>=7/4-6/<=3/<=1 bands)", "status":"WIRED"},
    # CR3 three-tracker model: Concentration (stamina) + Face (contest-local ethos) + Persuasion (merits).
    # Composure retired -> split into Concentration+Face (RATIFIED_2026-06-01.md CR3; DECISIONS.md reconc row).
    # `Face` is the canonical CR3 name bound to the kernel Standing primitive (built by ethos moves; feeds
    # Readiness+leak). WIRED is scope-honest: it resolves to a real symbol AND the underlying Standing is
    # live in resolution (Standing drives readiness/leak in _advance). SCOPE (Stage 1d, judge-upheld
    # honesty): the Face NAME + three-tracker registry are established as a tracked primitive + test surface;
    # what is NOT wired is the STRIP/STRAIN half — Standing.strip() is never called in the contest kernel
    # (Face is monotonic-up), so the prose "strain -> Rattled -> -1D Argue pool" and the RATIFIED line-20
    # stamina/standing/merits two-sided tradeoff / CR5 Face-attack are Stage-3 scope, NOT realized here. The
    # WIRED status vouches for the live-Standing half only. See social_contest_v30 §8 honesty note + ED-1056.
    # Persuasion+Concentration are the persuasion_track + agon_bout rows above.
    "face_tracker":        {"fn":"Face",             "toggle":None, "source":"social_contest_v30 §4/§8 (CR3: Composure retired -> Concentration+Face); binds kernel Standing", "status":"WIRED"},
    "three_trackers":      {"fn":"TRACKERS",         "toggle":None, "source":"RATIFIED_2026-06-01.md CR3 (Concentration+Face+Persuasion; Composure retired)", "status":"WIRED"},
    # F10 (judge-upheld): the derived value is computed and carried on Contest.resistance but is NOT yet
    # plumbed into resolution (the resolver has zero 'resistance' references; Venue.base_ob is never set
    # from it). It is metadata-only this stage. Downgraded WIRED->PARTIAL so mechanics_selftest does not
    # over-claim a live mechanic. Wiring it into the tracker/Venue.base_ob is the reserved ED stub
    # (contest_rebuild block, ED-1055..1079). fn still resolves (the DERIVATION is real), but PARTIAL is
    # excluded from the WIRED self-test's liveness assertion.
    "audience_resistance": {"fn":"_derive_resistance","toggle":None, "source":"params/contest.md §Persuasion Track (avg Stability round up −1, min 0) — DERIVED but not yet plumbed into resolution (ED-1055..1079)", "status":"PARTIAL"},
    "exchange_majority":   {"fn":"TallyAtClose",     "toggle":None, "source":"social_contest_v30 §2 Step 4 (untracked -> exchange majority)", "status":"WIRED"},
    # ── Stage 2 / Gate B: typed dictionaries (dataclasses; NO Godot YAML per locked decision 3) ──
    "styles_table":        {"fn":"STYLES_TABLE",       "toggle":None, "source":"params/contest.md §Argument Styles (PP-235) — Style×4 + flavor (locked decision 5)", "status":"WIRED"},
    "interaction_types":   {"fn":"INTERACTIONS_TABLE", "toggle":None, "source":"params/contest.md §Interaction Types; social_contest_v30 §4 Step 4 — InteractionType×4", "status":"WIRED"},
    "derive_interaction":  {"fn":"derive_interaction", "toggle":None, "source":"social_contest_v30 §4 Step 4 (genre/orientation -> CLASH/REINFORCE/CROSS) — canonical typed lookup", "status":"WIRED"},
    "adjudicators_table":  {"fn":"ADJUDICATORS_TABLE", "toggle":None, "source":"social_contest_v30 §2 Step 1 / §3 Argue Pool — AdjudicatorType×4 (typed surface)", "status":"WIRED"},
    "faction_boosts":      {"fn":"FACTION_BOOSTS",     "toggle":None, "source":"params/contest.md §Faction Boosts — 6 core factions + Löwenritter (conditional)", "status":"WIRED"},
    "proceedings_table":   {"fn":"PROCEEDINGS_TABLE",  "toggle":None, "source":"params/contest.md §Proceeding Types — Proceeding×8 + flavor (locked decision 5); cross-checked vs modes.PROCEEDINGS", "status":"WIRED"},
    # ── Stage 2 / Gate B: ED-137 Panel closure (VoteAtClose per-member ballot) ──
    "panel_deliberation":  {"fn":"panel_win_condition","toggle":None, "source":"social_contest_v30 §2 Step 1 (Panel) — ED-137 CLOSED (ED-1057): VoteAtClose per-member ballot", "status":"WIRED"},
    # resolution core (the promoted kernel this wrapper routes to)
    "agon_bout":           {"fn":"Bout",             "toggle":None, "source":"promoted groundup kernel (Persuasion-Track agôn path)", "status":"WIRED"},
    # other games — registered STUB rows for later stages
    "consensus_game":      {"fn":None,               "toggle":None, "source":"social_contest_v30 §10 BG-Vote / §7.2 (faction.py — Stage 4)", "status":"STUB"},
    "negotiation_game":    {"fn":None,               "toggle":None, "source":"social_contest_v30 §2 Private Negotiation (author-new — later stage)", "status":"STUB"},
    "inquiry_game":        {"fn":None,               "toggle":None, "source":"social_contest_v30 §7 Church Tribunal (author-new — later stage)", "status":"STUB"},
}

def mechanics_selftest():
    """Assert every WIRED mechanic resolves to a real symbol. STUB rows (fn=None) and PARTIAL rows
       (derived-but-not-plumbed, e.g. audience_resistance per F10) are excluded — the self-test only
       vouches for mechanics that are live in resolution. Returns (ok, missing)."""
    missing = [name for name, spec in MECHANICS.items()
               if spec["status"] == "WIRED" and _resolve(spec["fn"]) is None]
    return (len(missing) == 0, missing)
