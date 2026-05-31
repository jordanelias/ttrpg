"""
sim/personal/parliamentary_stay.py — Parliamentary Stay procedure (§10.1, ED-631)

Canon source: designs/scene/social_contest_v30.md §10.1 Parliamentary Stay (ED-631)
Status: [implemented: 2026-05-31 — §10.1. A Senator Inward motion halting an active Church
    Tribunal filing for 1 season via the §10 BG Parliamentary Vote. Available only while CI < 55.]

Dependencies:
  - sim/personal/parliamentary_vote — §10 BG vote (run_parliamentary_vote, Motion, VoteDeclaration)
  - sim/autoload/game_state         — world.clocks['CI'], world.factions, world.season

Entry points:
  - invoke_stay(motion, invoker_id, world, supporters=None, church_id='Church',
                side_a_genre=None, side_b_genre=None, rng=None) -> StayResult
  - resolve_stay_lift(stay: StayResult, world) -> bool

[ASSUMPTION: world has no tribunal-filing registry or suspension field (verified — tribunal.py
 returns a TribunalResult, "consequences applied by the caller"). Following that convention,
 invoke_stay RETURNS the suspension (StayResult.suspended + resume_season) for the caller to
 apply; resolve_stay_lift reports when the suspension season has elapsed. No invented world mutation.]
[ASSUMPTION: the armature signature invoke_stay(motion, invoker_id, world) cannot supply the
 §10-required Side-A coalition; extended with supporters/church_id/genre params (defaults keep the
 3-arg call valid — it returns 'invalid' when Side A < 2, which is faithful). Mechanical-tier, Jordan-vetoable.]
[FLAG: §10.1 cites "the Church's CI political pool bonus (floor(CI/20))" as the reason CI>=55 makes a
 Stay unpassable. The CI<55 availability gate (implemented, faithful to "Availability: Only while CI < 55")
 subsumes it — at CI>=55 the Stay is unavailable, so the bonus is moot. NOT wiring a floor(CI/20) Side-B
 vote bonus for CI<55 (cross-referenced Church mechanic; general-vs-stay scope not pinned in §10/§10.1).
 Flag for Jordan if it should apply to CI<55 stay votes.]
"""
from __future__ import annotations

from dataclasses import dataclass, field

from sim.personal.parliamentary_vote import run_parliamentary_vote, Motion, VoteDeclaration

# ── §10.1 constants (ledgered) ──
STAY_CI_AVAILABILITY_MAX = 55   # [canonical: §10.1 — "Only while CI < 55"]
STAY_MIN_SIDE_A_FACTIONS = 2    # [canonical: §10.1 — "2+ factions on Side A (the filing-suspension side)"]
STAY_SUSPENSION_SEASONS = 1     # [canonical: §10.1 — "halts an active Church Tribunal filing for 1 season"]


@dataclass
class StayResult:
    status: str                       # 'granted' | 'denied' | 'unavailable' | 'invalid'
    invoker_id: str
    ci_at_invocation: float
    suspended: bool = False
    resume_season: int | None = None
    side_a: list = field(default_factory=list)
    vote: object | None = None        # the §10 VoteResult
    notes: list = field(default_factory=list)


def invoke_stay(motion, invoker_id, world, supporters=None, church_id="Church",
                side_a_genre=None, side_b_genre=None, rng=None) -> StayResult:
    """§10.1: invoke a Parliamentary Stay to suspend an active Church Tribunal filing for 1
    season, via the §10 BG vote. Side A = invoker + supporters (>= 2 required); Side B = Church.
    Available only while CI < 55."""
    ci = float(world.clocks.get("CI", 0.0))
    res = StayResult(status="invalid", invoker_id=invoker_id, ci_at_invocation=ci)

    # §10.1 availability gate.
    if ci >= STAY_CI_AVAILABILITY_MAX:
        res.status = "unavailable"
        res.notes.append(f"§10.1: CI {ci:.0f} >= {STAY_CI_AVAILABILITY_MAX} — Stay window closed "
                         "(Church institutional authority exceeds Parliamentary reach).")
        return res

    # Side A = invoker + supporters (deduped); Church on Side B.
    side_a_ids = list(dict.fromkeys([invoker_id] + list(supporters or [])))
    res.side_a = side_a_ids
    eligible_a = [n for n in side_a_ids if n in world.factions and world.factions[n].parliamentary]
    if len(eligible_a) < STAY_MIN_SIDE_A_FACTIONS:
        res.status = "invalid"
        res.notes.append(f"§10.1: Side A has {len(eligible_a)} eligible faction(s); requires >= {STAY_MIN_SIDE_A_FACTIONS}.")
        return res
    if church_id not in world.factions:
        res.status = "invalid"
        res.notes.append(f"§10.1: Church faction '{church_id}' not found — Church must be Side B.")
        return res

    ga = side_a_genre or motion.primary_genre
    gb = side_b_genre or motion.primary_genre
    parties = [VoteDeclaration(n, "A", ga) for n in eligible_a] + [VoteDeclaration(church_id, "B", gb)]
    vote = run_parliamentary_vote(motion, parties, world, rng=rng)
    res.vote = vote

    if vote.status == "passed":
        res.status = "granted"
        res.suspended = True
        res.resume_season = world.season + STAY_SUSPENSION_SEASONS
        res.notes.append(f"§10.1 success: Church Tribunal suspended {STAY_SUSPENSION_SEASONS} season "
                         f"(resume/re-file season {res.resume_season}).")
    else:
        res.status = "denied"
        res.notes.append(f"§10.1 failure (vote {vote.status}): Tribunal proceeds immediately; "
                         "the motion cannot be appealed or re-filed this season.")
    return res


def resolve_stay_lift(stay: StayResult, world) -> bool:
    """§10.1: a granted Stay lifts after its suspension season — the Church may re-file in the
    following season. Returns True once the suspension has elapsed (tribunal may resume/re-file)."""
    if not stay.suspended or stay.resume_season is None:
        return True
    return world.season >= stay.resume_season
