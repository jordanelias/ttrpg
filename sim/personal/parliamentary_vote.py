"""
sim/personal/parliamentary_vote.py — Parliamentary Vote (faction scale)

Canon source: designs/scene/social_contest_v30.md §10 (Parliamentary Vote)
Game Design constraints applicable: GD-3 (extra-parliamentary factions cannot cast
    Parliamentary votes — canon/02_canon_constraints.md §B GD-3)
Status: [implemented: 2026-05-31 — §10 BG vote against social_contest_v30. Faction-scale
    Mandate-pool resolution (NOT the §1-9 personal argue-pool contest); reuses the shared
    Persuasion-Track threshold constants from sim.personal.contest §6.]

Dependencies:
  - sim/autoload/dice_engine — d10 pool roll (TN 7)
  - sim/autoload/game_state   — Faction (Mandate == Faction.L), Faction.parliamentary
                                (GD-3 eligibility), Faction.adjust, MULTS
  - sim/personal/contest      — shared Persuasion-Track threshold constants (§6)

Entry points:
  - run_parliamentary_vote(motion: Motion, parties: list[VoteDeclaration], world, rng=None) -> VoteResult

[PRE-LPS-1 / PORT-BLOCKING — ED-FA-0004, 2026-07-07: Mandate is stored as the scalar Faction.L
 (basis: crown_initiative.py Great Work pool `int(crown.L)`). LPS-1 IS ratified and DOES relocate
 Legitimacy/Mandate per-settlement — so this Faction.L-as-Mandate-pool convention is the pre-LPS-1
 SUPERSEDED scalar and must NOT be ported as canon-conformant until ED-FA-0004 closes (Stratum B).
 (Upgrades the prior hedged [ASSUMPTION] note, which predated ED-FA-0004's ruling.)]
[ASSUMPTION: GD-3 'extra-parliamentary' == Faction.parliamentary is False — basis: game_state
 Faction has a `parliamentary: bool`, no `parliamentary_status` string; canon GD-3 names a
 `parliamentary_status: extra` flag. Mapping is 1:1.]
[ASSUMPTION: Parliament dominant-genre, per-side genre, and lobbying offset are carried on the
 Motion / declarations — basis: game_state has no Parliament/boost/genre/lobby fields (the
 plan's 'canon assumes a richer game_state than exists' workaround); duck-typed inputs.]
[FLAG: int(L) Mandate bucketing mirrors crown_initiative; per Amendment 2026-05-19b, canon-keyed
 categorical lookups should bucket via canonical_* helpers — Mandate-as-pool-size is not a table
 lookup, and int(L) preserves sibling consistency. Revisit if a canonical_mandate helper lands.]
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field

from sim.autoload import dice_engine
from sim.autoload.game_state import MULTS

# Shared Persuasion-Track thresholds (§6) — single source of truth, do NOT redefine:
from sim.personal.contest import (
    PERSUASION_WIN_THRESHOLD,        # 7  [canonical: social_contest_v30 §6/§10]
    PERSUASION_LOSS_THRESHOLD,       # 3
    PERSUASION_TOTAL_VICTORY,        # 9
    PERSUASION_TOTAL_DEFEAT,         # 1
    PERSUASION_TRACK_START_DEFAULT,  # 5
)

# ── §10-specific constants (ledgered in tests/sim/v18-integration/sim_verification_ledger.json) ──
BG_VOTE_TN = 7                              # [canonical: §10 — "Roll combined pool TN 7"]
BG_VOTE_GENRE_BONUS = 1                     # [canonical: §10 — "+1D if the side's genre matches the primary genre"]
BG_VOTE_AUDIENCE_BONUS = 1                  # [canonical: §10 — "+1D if the side's genre matches the Parliament's dominant faction boost"]
# [CP-3 / ED-FA-0016, 2026-07-08 — historical precedent for the abstention-resistance + committee
#  mechanism (grounds the MECHANISM, never the magnitude — CLAUDE.md §5/§7)]: the Venetian ballot
#  distinguished the *non sinceri* — formal uncommitted / spoiled ballots — from the sincere yes/no
#  count. A high non-sinceri tally was not noise but a recognised institutional signal: it withheld
#  assent without opposing, and measures drawing many uncommitted ballots were sent back for
#  redrafting rather than decided. That is exactly the shape modelled here: a high-Stability abstainer
#  does not vote a side but raises the bar the active sides must clear (BG_VOTE_ABSTAIN_* resistance),
#  and a field that fails to clear it is referred to committee (the §10 zero-zero branch below) — the
#  Renaissance "committee referral" as institutional fact, composing with the *broglio* material mined
#  by the 2026-06-28 social-contest deliberation source-research.
BG_VOTE_ABSTAIN_STABILITY_THRESHOLD = 6    # [canonical: §10 — "If a faction with Stability >= 6 Abstains"]
BG_VOTE_ABSTAIN_RESISTANCE_PER = 1         # [canonical: §10 — "+1 resistance"]
BG_VOTE_RESISTANCE_MAX = 2                  # [canonical: §10 — "(max +2)"]
BG_VOTE_LOBBY_OFFSET_MAX = 2               # [canonical: §10 — "+1 toward lobbying side (max ±2)"]
BG_VOTE_LOBBY_START_MAX = 6                # [canonical: §10 ED-621 — "Maximum starting Persuasion Track: 6"]
BG_VOTE_LOBBY_START_MIN = 4                # [canonical: §10 ED-621 — "Minimum starting track: 4"]
BG_VOTE_TOTAL_VICTORY_MANDATE_DELTA = -1   # [canonical: §10 — "losing coalition's dominant faction takes Mandate -1 for one season"]
_TRACK_FLOOR, _TRACK_CEIL = 0, 10          # [ASSUMPTION: clamp per contest.py §6 convention; §10 states no explicit bound]

GENRES = ("Memory", "Projection")          # [canonical: §10 step 2 — "one genre (Memory or Projection)"]


@dataclass
class Motion:
    """A Parliamentary motion put to a BG-scale vote."""
    motion_id: str
    primary_genre: str                            # 'Memory' | 'Projection' — the question's primary genre
    parliament_dominant_genre: str | None = None  # for the §10 audience boost
    lobbying_offset: int = 0                       # net prior-Diplomacy offset toward Side A (signed); pre-cap


@dataclass
class VoteDeclaration:
    """One faction declaring participation. Side 'A' = for the motion, 'B' = against."""
    faction_name: str
    side: str            # 'A' | 'B'
    genre: str           # 'Memory' | 'Projection'


@dataclass
class VoteResult:
    status: str                       # 'passed' | 'failed' | 'committee'
    final_track: int
    starting_track: int = 5
    resistance: int = 0
    side_a_pool: int = 0
    side_b_pool: int = 0
    side_a_net: int = 0
    side_b_net: int = 0
    movement_a: int = 0
    movement_b: int = 0
    total_victory: bool = False
    mandate_penalty: list = field(default_factory=list)   # faction(s) taking Mandate -1
    abstainers: list = field(default_factory=list)
    ineligible: list = field(default_factory=list)        # GD-3-excluded (parliamentary == False)
    rolls_a: list = field(default_factory=list)
    rolls_b: list = field(default_factory=list)
    notes: list = field(default_factory=list)


def _side_genre(decls: list) -> str | None:
    """§10 step 2: each side declares one genre. Derive it from the side's declarations
    (most common; first-seen on tie). None for an empty side."""
    if not decls:
        return None
    return Counter(d.genre for d in decls).most_common(1)[0][0]


def run_parliamentary_vote(motion: Motion, parties: list, world, rng=None) -> VoteResult:
    """Resolve a Parliamentary Vote per social_contest_v30 §10.

    parties: list of VoteDeclaration. Eligible factions not listed Abstain. GD-3: factions
    with parliamentary == False are ineligible (excluded from the vote entirely).
    """
    res = VoteResult(status="committee", final_track=PERSUASION_TRACK_START_DEFAULT)

    # Resolve declarations against the world; enforce GD-3 eligibility.
    side_a, side_b = [], []
    declared = set()
    for d in parties:
        f = world.factions.get(d.faction_name)
        if f is None:
            res.notes.append(f"declaration for unknown faction '{d.faction_name}' ignored")
            continue
        if not f.parliamentary:                       # [canonical: GD-3 — extra-parliamentary cannot cast votes]
            res.ineligible.append(d.faction_name)
            res.notes.append(f"GD-3: '{d.faction_name}' extra-parliamentary (parliamentary=False) — excluded")
            continue
        declared.add(d.faction_name)
        (side_a if d.side == "A" else side_b).append(d)

    # Abstainers = eligible factions that did not declare.
    for name, f in world.factions.items():
        if f.parliamentary and name not in declared and name not in res.ineligible:
            res.abstainers.append(name)

    # §10 step 3 — resistance: +1 per abstaining Stability>=6 faction, cap +2.
    resistance = 0
    for name in res.abstainers:
        if world.factions[name].Sta >= BG_VOTE_ABSTAIN_STABILITY_THRESHOLD:
            resistance += BG_VOTE_ABSTAIN_RESISTANCE_PER
    res.resistance = resistance = min(resistance, BG_VOTE_RESISTANCE_MAX)

    # §10 step 4 + ED-621 — starting track = 5 ± lobbying (offset capped ±2), start clamped to [4,6].
    offset = max(-BG_VOTE_LOBBY_OFFSET_MAX, min(BG_VOTE_LOBBY_OFFSET_MAX, motion.lobbying_offset))
    start = max(BG_VOTE_LOBBY_START_MIN, min(BG_VOTE_LOBBY_START_MAX, PERSUASION_TRACK_START_DEFAULT + offset))
    res.starting_track = start

    # Resolution: per-side Mandate pool (sum of L) + genre/audience bonuses; roll TN 7.
    def _resolve(decls):
        if not decls:
            return 0, 0, []
        mandate = sum(int(world.factions[d.faction_name].L) for d in decls)  # [canonical: §10 "sum of Mandate"; Mandate==Faction.L]
        genre = _side_genre(decls)
        pool = mandate
        if genre == motion.primary_genre:
            pool += BG_VOTE_GENRE_BONUS                                      # [canonical: §10 — genre match +1D]
        if motion.parliament_dominant_genre and genre == motion.parliament_dominant_genre:
            pool += BG_VOTE_AUDIENCE_BONUS                                   # [canonical: §10 — audience boost +1D]
        if pool <= 0:
            return 0, 0, []
        roll = dice_engine.roll_pool(pool_size=pool, tn=BG_VOTE_TN, rng=rng)
        return pool, roll.net, list(roll.rolls)

    res.side_a_pool, res.side_a_net, res.rolls_a = _resolve(side_a)
    res.side_b_pool, res.side_b_net, res.rolls_b = _resolve(side_b)

    # §10 — each side movement = max(0, net - resistance).
    res.movement_a = max(0, res.side_a_net - resistance)
    res.movement_b = max(0, res.side_b_net - resistance)

    # §10 zero-zero — both fail to exceed resistance -> committee.
    if res.movement_a == 0 and res.movement_b == 0:
        res.final_track = start
        res.status = "committee"
        res.notes.append("§10 zero-zero: neither side exceeded resistance -> referred to committee")
        return res

    # Net track movement = difference, toward the larger side (A=up / B=down).
    track = max(_TRACK_FLOOR, min(_TRACK_CEIL, start + (res.movement_a - res.movement_b)))
    res.final_track = track

    # §10 thresholds (shared §6 constants).
    if track >= PERSUASION_WIN_THRESHOLD:
        res.status = "passed"
    elif track <= PERSUASION_LOSS_THRESHOLD:
        res.status = "failed"
    else:
        res.status = "committee"

    # §10 Total Victory — track >= 9 or <= 1 -> losing coalition's dominant faction Mandate -1.
    if track >= PERSUASION_TOTAL_VICTORY or track <= PERSUASION_TOTAL_DEFEAT:
        res.total_victory = True
        losing = side_b if track >= PERSUASION_TOTAL_VICTORY else side_a
        losing_names = [d.faction_name for d in losing]
        if losing_names:
            dominant = max(losing_names, key=lambda n: world.factions[n].L)   # dominant = highest Mandate (L)
            world.factions[dominant].adjust("L", BG_VOTE_TOTAL_VICTORY_MANDATE_DELTA * MULTS["L"])
            res.mandate_penalty.append(dominant)
            res.notes.append(
                f"§10 Total Victory: '{dominant}' (losing dominant) takes Mandate -1 "
                "[one-season penalty; temporary-modifier restoration deferred to season_manager]"
            )
    return res
