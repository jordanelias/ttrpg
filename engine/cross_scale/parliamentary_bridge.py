"""
sim/cross_scale/parliamentary_bridge.py — Parliamentary vote → live-loop contest + composed echo
                                          (ED-SC-0006 / ED-SC-0007 / ED-SC-0002, flag-gated)

Activates the Key & Echo transport in the LIVE campaign loop via the canonical §10 Parliamentary
Vote (Jordan ruling 2026-07-08: "wire the canonical Parliamentary vote"). The parliamentary vote is
FACTION-SCALE — it consumes aggregate faction state (Faction.L as Mandate) directly, so it sidesteps
the still-open personal-scale CONTEXT-DERIVATION gap (deriving personal contest actors from aggregate
state) that keeps scene_dispatch's personal contest path deferred (ED-SC-0006 items 1-2 for the
personal path remain future work; this activates contest resolution via the faction-scale vote).

WHAT LANDS HERE (all behind ECHO_TRANSPORT — default OFF is byte-exact):
  - ED-SC-0006 (derivation): each season, derive a two-pole motion from world state and resolve it
    with the ratified §10 vote implementation — resolved through the `parliamentary_vote` role, not
    imported (see COMPOSITION below). A resolved vote counts as a resolved contest
    (world.scenes_resolved) — closing N-1 (the kernel/vote was unreachable from the loop) and the
    F7 scenes_resolved==0 gap.
  - ED-SC-0007 (outcome → world): the §10 Total-Victory Mandate penalty is applied by
    run_parliamentary_vote itself; the WINNER-side Domain Echo is composed here and emitted through
    the substrate (echo_transport) as a deferred faction stat write at the accounting boundary.
  - ED-SC-0002 (COMPOSED keying, Jordan ruling 2026-07-08): band gates MAGNITUDE, genre selects the
    STAT/CHANNEL. Band = the §10 Persuasion-Track band → domain_echo degree (Total→Overwhelming ±2,
    Decisive→Success ±1, Committee→Partial = no echo, which is ED-SC-0002's agreed "Compromise fires
    nothing"). Genre = the winning side's genre → stat: Memory→L (Mandate, canon-direct per
    social_contest SS6), Projection→I (the outward-initiative channel; SS6's "+1D first Domain Action"
    mapped onto the aggregate Influence stat — the concrete composed-scheme realization, easily retuned).

PROVISIONAL derivation (the concrete realization of the ruled parliamentary-vote approach; the
two-pole shape is canon §10, the specific proposer/establishment/genre assignment is the sim's
deterministic instantiation, flagged for retune — NOT a new canonical mechanic):
  proposer (Side A, genre Projection) = the eligible faction lowest in Stability (crisis-leaning);
  establishment (Side B, genre Memory) = the highest-Mandate (L) eligible faction other than the
  proposer; every other eligible faction ABSTAINS (supplying §10 resistance when Stability ≥ 6).
  Deterministic in world state (the only randomness is the §10 dice roll on world.rng).

COMPOSITION — THIS MODULE NAMES NO SUBSYSTEM (plan step S5a, 2026-08-22).
  It held the last three top-level `systems` imports in `engine/`. All three are gone: the §10 vote
  and its two record types resolve through `engine.substrate.composition`, and
  `references/module_contracts.yaml` names the providers (roles `parliamentary_vote`,
  `parliamentary_motion`, `parliamentary_vote_declaration`, `territory_transfer_candidate`,
  `territory_transfer_proposal`). Every target is imported and resolved at EXPORT time behind a
  blocking gate, so the indirection cannot fail late in a campaign.

  The same seam was owned twice — `systems/factions/sim/parliamentary_transfer.py` imported the
  vote by name as well. Both now resolve the one declaration.

OI-04 (ED-IN-0091 plan §3 Wave 2, 07-14 Tier-1 #2 / GAP-A1) — THE THIRD PARLIAMENTARY MOTION PATH:
  `parliamentary_transfer.propose_transfer` had zero callers, making a faction's lost territory a
  one-way ratchet. This is a separate motion from the two-pole vote above (which composes only a
  Domain Echo) and from `parliamentary_action.propose_censure` (the Sanction sibling, wired at
  faction-action scale) — a CB-gated Territory Transfer, attempted every season alongside the vote,
  independent of it.

  ⚠ THE DERIVATION MOVED OUT OF THIS FILE AT S5a. `_derive_transfer` lived here and read four
  members private to `parliamentary_transfer` (`_available_cb`, `_MODE_CB`,
  `PARL_LAST_TERRITORY_FLOOR`, `MODES`) — the engine reaching into a subsystem to re-derive a rule
  that lives in that subsystem. It is now `parliamentary_transfer.derive_transfer_candidate`, in
  its owner, resolved here as the `territory_transfer_candidate` role; its canon notes travelled
  with it. Behaviour is unchanged — it is a pure function of world state, and the seeded goldens
  are the control.

  Today the sole auto-populated CB is 'crown_constitutional_restoration' (Crown < 6 territories,
  parliamentary_transfer.py §3), which that module's own §2 table maps to 'adversarial' only; when
  no qualifying CB exists for any (initiator, holder) pair, `_run_transfer_motion` returns None and
  the season proceeds exactly as before OI-04 — no behaviour change. The §1.1 Frequency gate ("1
  per arc per faction") excludes an initiator whose `Faction.parl_transfer_used_this_arc` is
  already set (game_state.py, reset per arc boundary by season_manager.py's `advance_season`) — a
  gated-out season returns None exactly like a no-qualifying-CB season, so the frequency limit
  costs zero extra world.rng draws.

Guardrails (holonic doctrine ED-1083 §2): local rule only; declared I/O only; no entity special-
casing; no scale-local dialect.
"""
from __future__ import annotations

from engine.cross_scale import echo_transport
from engine.substrate import composition

# ED-SC-0002 COMPOSED keying — genre → aggregate stat channel (Jordan ruling 2026-07-08).
# Memory→L is canon-direct (SS6 Memory→Mandate; Mandate==Faction.L pre-LPS-1). Projection→I realizes
# SS6's "+1D first Domain Action" as the outward-initiative Influence channel on the aggregate stat set.
COMPOSED_GENRE_STAT = {"Memory": "L", "Projection": "I"}

# Side genres (the two-pole instantiation): proposer argues Projection (a forward measure), the
# establishment argues Memory (precedent/legitimacy).
_SIDE_A_GENRE = "Projection"
_SIDE_B_GENRE = "Memory"


def _derive_vote(world):
    """Derive a two-pole §10 motion from aggregate faction state. Returns (motion, declarations,
    proposer_name, establishment_name) or None when fewer than two eligible factions exist."""
    eligible = [name for name, f in world.factions.items()
                if getattr(f, "parliamentary", False) and getattr(f, "territories", None)]
    if len(eligible) < 2:
        return None
    proposer = min(eligible, key=lambda n: world.factions[n].Sta)       # crisis-leaning (lowest Stability)
    establishment = max((n for n in eligible if n != proposer),
                        key=lambda n: world.factions[n].L)              # highest Mandate defender
    season = int(getattr(world, "season", 0))
    Motion = composition.require("parliamentary_motion")
    VoteDeclaration = composition.require("parliamentary_vote_declaration")
    motion = Motion(motion_id=f"parl_s{season}", primary_genre=_SIDE_A_GENRE,
                    parliament_dominant_genre=None, lobbying_offset=0)
    decls = [VoteDeclaration(proposer, "A", _SIDE_A_GENRE),
             VoteDeclaration(establishment, "B", _SIDE_B_GENRE)]
    return motion, decls, proposer, establishment


def _winner_and_degree(vr):
    """Map the §10 VoteResult band → (winning_side, domain_echo degree). Committee (compromise) →
    (None, 'Partial') = no echo, per ED-SC-0002's agreed 'Compromise fires nothing'.

    READS THE VERDICT, DOES NOT RE-DERIVE IT (S5a). This used to compare `vr.final_track` against
    `PERSUASION_TOTAL_VICTORY` / `PERSUASION_TOTAL_DEFEAT`, imported from `systems.social_contest`
    — the engine recomputing, from the raw track, a classification the vote module had already made
    and recorded on the result object. `vr.status` already names the winning side ('passed' = Side
    A carried the motion, 'failed' = Side B did) and `vr.total_victory` already names the band.

    Value-identical, and `engine/tests/test_parliamentary_bridge.py::
    test_winner_and_degree_is_identical_to_the_threshold_derivation_it_replaced` proves it
    exhaustively over every reachable track rather than by argument. The ONE assumption it rests on
    is canon's own ordering — TOTAL_VICTORY (9) >= WIN_THRESHOLD (7) and TOTAL_DEFEAT (1) <=
    LOSS_THRESHOLD (3) — so a total victory always also passes or fails. That test fails loudly if
    a retune ever breaks it, which is why it reads the real constants instead of hardcoding them.
    """
    if vr.status == "passed":
        return "A", "Overwhelming" if vr.total_victory else "Success"
    if vr.status == "failed":
        return "B", "Overwhelming" if vr.total_victory else "Success"
    return None, "Partial"


def _run_transfer_motion(world, rng=None):
    """OI-04 — attempt the CB-gated Territory Transfer motion (see module docstring). A no-op
    (returns None) when the derivation finds no qualifying CB — the season proceeds exactly as
    before OI-04 in that case. Never raises; never fabricates a CB."""
    derived = composition.require("territory_transfer_candidate")(world)
    if derived is None:
        return None
    initiator, target_territory, mode = derived
    result = composition.require("territory_transfer_proposal")(
        initiator, target_territory, mode, world, rng=rng)
    return {
        "initiator": initiator, "target_territory": target_territory, "mode": mode,
        "cb_used": result.cb_used, "status": result.status,
    }


def run_parliamentary_scene(world, rng=None):
    """Resolve one season's parliamentary vote and compose its winner-side Domain Echo, then
    (OI-04) independently attempt the CB-gated Territory Transfer motion.

    Fires ONLY when world.echo_scheduler is attached (ECHO_TRANSPORT on). The §10 loser Mandate
    penalty is applied inside run_parliamentary_vote; the winner echo is emitted (deferred) here.
    Returns a summary dict; {'resolved': False} when no two-pole vote can be derived — the
    'transfer' key is present either way (None when no CB qualifies), since the Transfer motion
    does not depend on the two-pole vote's own eligibility (OI-04 module docstring).
    """
    if getattr(world, "echo_scheduler", None) is None:
        return {"resolved": False, "reason": "ECHO_TRANSPORT off"}
    derived = _derive_vote(world)
    if derived is None:
        transfer = _run_transfer_motion(world, rng)
        return {"resolved": False, "reason": "fewer than two eligible parliamentary factions",
                "transfer": transfer}
    motion, decls, proposer, establishment = derived

    # applies the §10 loser Mandate penalty
    vr = composition.require("parliamentary_vote")(motion, decls, world, rng)

    side, degree = _winner_and_degree(vr)
    winner = proposer if side == "A" else (establishment if side == "B" else None)
    winner_genre = _SIDE_A_GENRE if side == "A" else (_SIDE_B_GENRE if side == "B" else None)

    echo_fired = False
    if winner is not None and degree in ("Overwhelming", "Success"):
        ctx = {"echo": {
            "actor_faction": winner, "target_faction": winner,
            "most_relevant_stat": COMPOSED_GENRE_STAT[winner_genre],
            "degree": degree, "scope_met": True, "scene_id": motion.motion_id,
        }}
        out = echo_transport.emit_scene_echo("contest", {"vote_status": vr.status}, ctx, world)
        echo_fired = bool(out.get("other_echoes"))

    # OI-04 — the THIRD Parliamentary motion path: independent of (and run after) the two-pole
    # vote above; never blocks it and is never blocked by it.
    transfer = _run_transfer_motion(world, rng)

    return {"resolved": True, "status": vr.status, "final_track": vr.final_track,
            "total_victory": vr.total_victory, "winner": winner, "degree": degree,
            "mandate_penalty": list(vr.mandate_penalty), "echo_fired": echo_fired,
            "transfer": transfer}
