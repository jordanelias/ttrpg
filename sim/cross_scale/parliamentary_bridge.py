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
    with sim.personal.parliamentary_vote.run_parliamentary_vote (the ratified §10 impl). A resolved
    vote counts as a resolved contest (world.scenes_resolved) — closing N-1 (the kernel/vote was
    unreachable from the loop) and the F7 scenes_resolved==0 gap.
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

Guardrails (holonic doctrine ED-1083 §2): local rule only; declared I/O only; no entity special-
casing; no scale-local dialect.
"""
from __future__ import annotations

from sim.cross_scale import echo_transport
from sim.personal.parliamentary_vote import Motion, VoteDeclaration, run_parliamentary_vote
from sim.personal.contest import (
    PERSUASION_TOTAL_VICTORY,   # 9
    PERSUASION_TOTAL_DEFEAT,    # 1
)

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
    motion = Motion(motion_id=f"parl_s{season}", primary_genre=_SIDE_A_GENRE,
                    parliament_dominant_genre=None, lobbying_offset=0)
    decls = [VoteDeclaration(proposer, "A", _SIDE_A_GENRE),
             VoteDeclaration(establishment, "B", _SIDE_B_GENRE)]
    return motion, decls, proposer, establishment


def _winner_and_degree(vr):
    """Map the §10 VoteResult band → (winning_side, domain_echo degree). Committee (compromise) →
    (None, 'Partial') = no echo, per ED-SC-0002's agreed 'Compromise fires nothing'."""
    if vr.total_victory and vr.final_track >= PERSUASION_TOTAL_VICTORY:
        return "A", "Overwhelming"
    if vr.total_victory and vr.final_track <= PERSUASION_TOTAL_DEFEAT:
        return "B", "Overwhelming"
    if vr.status == "passed":
        return "A", "Success"
    if vr.status == "failed":
        return "B", "Success"
    return None, "Partial"


def run_parliamentary_scene(world, rng=None):
    """Resolve one season's parliamentary vote and compose its winner-side Domain Echo.

    Fires ONLY when world.echo_scheduler is attached (ECHO_TRANSPORT on). The §10 loser Mandate
    penalty is applied inside run_parliamentary_vote; the winner echo is emitted (deferred) here.
    Returns a summary dict; {'resolved': False} when no two-pole vote can be derived.
    """
    if getattr(world, "echo_scheduler", None) is None:
        return {"resolved": False, "reason": "ECHO_TRANSPORT off"}
    derived = _derive_vote(world)
    if derived is None:
        return {"resolved": False, "reason": "fewer than two eligible parliamentary factions"}
    motion, decls, proposer, establishment = derived

    vr = run_parliamentary_vote(motion, decls, world, rng)   # applies the §10 loser Mandate penalty

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

    return {"resolved": True, "status": vr.status, "final_track": vr.final_track,
            "total_victory": vr.total_victory, "winner": winner, "degree": degree,
            "mandate_penalty": list(vr.mandate_penalty), "echo_fired": echo_fired}
