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
    with systems.social_contest.sim.parliamentary_vote.run_parliamentary_vote (the ratified §10 impl). A resolved
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

OI-04 (ED-IN-0091 plan §3 Wave 2, 07-14 Tier-1 #2 / GAP-A1) — THE THIRD PARLIAMENTARY MOTION PATH:
  `systems.factions.sim.parliamentary_transfer.propose_transfer` had zero callers, making a
  faction's lost territory a one-way ratchet. This is a separate motion from the two-pole vote
  above (which composes only a Domain Echo) and from `parliamentary_action.propose_censure` (the
  Sanction sibling, wired at faction-action scale) — a CB-gated Territory Transfer, attempted every
  season alongside the vote, independent of it. `_derive_transfer` uses ONLY
  `parliamentary_transfer`'s own CB machinery (`_available_cb` / `_MODE_CB` /
  `PARL_LAST_TERRITORY_FLOOR`) — it never invents or seeds a `world.casus_belli` entry. Today the
  sole auto-populated CB is 'crown_constitutional_restoration' (Crown < 6 territories,
  parliamentary_transfer.py §3), which that module's own §2 table maps to 'adversarial' only; when
  no qualifying CB exists for any (initiator, holder) pair, `_run_transfer_motion` returns None and
  the season proceeds exactly as before OI-04 — no behaviour change. WAVE-2 addition (§1.1
  Frequency, "1 per arc per faction"): `_derive_transfer` also excludes any initiator whose
  `Faction.parl_transfer_used_this_arc` is already set (game_state.py, reset per arc boundary by
  season_manager.py's `advance_season`) — a gated-out season returns None exactly like a
  no-qualifying-CB season, so the frequency limit costs zero extra world.rng draws. Target-territory selection is
  NOT canon-determined (parliamentary_transfer_v30.md §1-§4 specify Pool/Ob/CB/vote mechanics, never
  a target rule), so it is a [SEED] narrowest-option default (§0.1 "narrowest option, recorded as
  [SEED]"): the largest current holder among eligible targets, mirroring the realist
  extremal-selection precedent `parliamentary_action.select_censure_target` already established
  (ED-SC-0006/0007) — no fabricated relationship signal, just the schema's own territory-count
  field.

Guardrails (holonic doctrine ED-1083 §2): local rule only; declared I/O only; no entity special-
casing; no scale-local dialect.
"""
from __future__ import annotations

from engine.cross_scale import echo_transport
from systems.factions.sim import parliamentary_transfer
from systems.social_contest.sim.parliamentary_vote import Motion, VoteDeclaration, run_parliamentary_vote
from systems.social_contest.sim.contest import (
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


def _derive_transfer(world):
    """[SEED — ED-SC-0006/0007 precedent; OI-04] Derive a Parliamentary Territory Transfer
    candidate (initiator, target_territory, mode), reusing ONLY
    `parliamentary_transfer._available_cb` / `_MODE_CB` / `PARL_LAST_TERRITORY_FLOOR` — never
    inventing or seeding a `world.casus_belli` entry. Returns None when no (initiator, holder)
    pair has a CB that qualifies for any mode.

    Search: every parliamentary faction NOT already arc-gated (§1.1 Frequency, Wave-2 fix — see
    module docstring's OI-04 note) as a candidate initiator, every OTHER faction above the §1.3
    last-territory floor as a candidate holder (propose_transfer would block a floor-violating
    holder anyway, so this mirrors the module's own gate rather than re-deriving a new one); for
    each pair, the mode is the first `parliamentary_transfer.MODES`-order mode any available CB
    source qualifies for (canon §2 `_MODE_CB`, not an invented mapping). Among all qualifying
    triples, [SEED]: prefer the largest current holder (most territories) — the narrowest
    non-fabricated tie-break available, matching `parliamentary_action.select_censure_target`'s
    realist-targeting precedent; ties broken by initiator name then holder name (both ascending).
    Within the chosen holder, the target territory is the alphabetically-first territory id, for
    full determinism (canon does not specify one — no per-territory signal exists to prefer).
    """
    candidates = []
    for initiator_name, initiator_fac in world.factions.items():
        if not getattr(initiator_fac, "parliamentary", False):
            continue
        # OI-04 Wave-2 canon gate (parliamentary_transfer_v30.md §1.1 Frequency, "1 per arc per
        # faction"): an initiator who already attempted this arc is excluded from candidate
        # derivation entirely, not merely blocked once selected -- this is what keeps a
        # gated-out season byte-identical to a no-qualifying-CB season (zero extra world.rng
        # draws), matching propose_transfer's own gate (parliamentary_transfer.py) rather than
        # re-deriving a second copy of the rule.
        if getattr(initiator_fac, "parl_transfer_used_this_arc", False):
            continue
        for holder_name, holder_fac in world.factions.items():
            if holder_name == initiator_name:
                continue
            if len(holder_fac.territories) <= parliamentary_transfer.PARL_LAST_TERRITORY_FLOOR:
                continue
            available = parliamentary_transfer._available_cb(initiator_name, holder_name, world)
            if not available:
                continue
            for mode in parliamentary_transfer.MODES:
                if any(cb in parliamentary_transfer._MODE_CB[mode] for cb in available):
                    candidates.append((initiator_name, holder_name, mode, len(holder_fac.territories)))
                    break
    if not candidates:
        return None
    candidates.sort(key=lambda c: (-c[3], c[0], c[1]))
    initiator, holder, mode, _ = candidates[0]
    target_territory = sorted(world.factions[holder].territories)[0]
    return initiator, target_territory, mode


def _run_transfer_motion(world, rng=None):
    """OI-04 — attempt the CB-gated Territory Transfer motion (see module docstring). A no-op
    (returns None) when `_derive_transfer` finds no qualifying CB — the season proceeds exactly as
    before OI-04 in that case. Never raises; never fabricates a CB."""
    derived = _derive_transfer(world)
    if derived is None:
        return None
    initiator, target_territory, mode = derived
    result = parliamentary_transfer.propose_transfer(initiator, target_territory, mode, world, rng=rng)
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

    # OI-04 — the THIRD Parliamentary motion path: independent of (and run after) the two-pole
    # vote above; never blocks it and is never blocked by it.
    transfer = _run_transfer_motion(world, rng)

    return {"resolved": True, "status": vr.status, "final_track": vr.final_track,
            "total_victory": vr.total_victory, "winner": winner, "degree": degree,
            "mandate_penalty": list(vr.mandate_penalty), "echo_fired": echo_fired,
            "transfer": transfer}
