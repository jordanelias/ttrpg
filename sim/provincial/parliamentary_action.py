"""
sim/provincial/parliamentary_action.py — Parliamentary Sanction proposal mechanism (faction scale)

Canon source: designs/provincial/faction_layer_v30.md §5.4 (Parliamentary Actions table) —
    the "Parliamentary Sanction" parameterized action (ED-FA-0006 DISTILL). This module implements
    the CENSURE tier only (the mildest sanction: Mandate-2 proposer min, Majority vote, target
    Stability −1 / Mandate −1, no proposer cost, one-time). The four heavier Sanction tiers
    (Embargo · Blockade · Combined · Outlawry) and the constructive motions (Subsidy · War
    Authorisation · Treaty Ratification · Recognition Challenge · Succession Endorsement) are
    deliberately NOT built here — see the module TODO for the future-extension surface.

Game Design constraints applicable: GD-3 (extra-parliamentary factions cannot propose or cast
    Parliamentary votes — enforced here at proposal time and again inside run_parliamentary_vote).

Status: [implemented: 2026-07-08 — ED-SC-0007 residual "parliamentary_vote-in-the-loop" MECHANISM
    (the proposer/target/declaration authoring that sim/personal/parliamentary_vote.py never had a
    caller for). WIRED (same session, ED-FA-0012): sim/provincial/faction_action.py's
    _try_faction_unique now calls propose_censure as a universal fallback in the existing
    faction-unique action slot, so this reaches every live campaign via faction_take_action — not a
    standalone unreachable mechanism. Not yet wired: scene_dispatch.py has no direct caller (the
    faction_action.py path supersedes that need for the Censure tier).]

[PRE-LPS-1 / PORT-BLOCKING — ED-FA-0004, 2026-07-07: this module reads Mandate as the scalar
 Faction.L (`proposer.L >= 2`), inheriting the SUPERSEDED pre-LPS-1 Mandate==Faction.L convention
 documented at the top of sim/personal/parliamentary_vote.py. LPS-1 relocates Legitimacy/Mandate
 per-settlement; do NOT port this scalar-L read as canon-conformant until ED-FA-0004 (Stratum B)
 closes. This is KNOWN inherited debt, not new debt introduced here.]

Dependencies:
  - sim/autoload/game_state           — Faction (Mandate == Faction.L), Faction.parliamentary, MULTS
  - sim/personal/parliamentary_vote   — run_parliamentary_vote (the §10 BG-vote resolver)

Entry points:
  - propose_censure(proposer, world, rng) -> str
  - select_censure_target(proposer, world) -> Faction | None   (exposed for targeting tests)
"""
from __future__ import annotations

from sim.autoload.game_state import MULTS
from sim.personal.parliamentary_vote import (
    Motion,
    VoteDeclaration,
    run_parliamentary_vote,
)

# ── §5.4 Censure-tier parameters (from the faction_layer_v30.md §5.4 table) ────────────────────
CENSURE_PROPOSER_MIN_MANDATE = 2      # [canonical: faction_layer_v30 §5.4 — Censure "Proposer min: Mandate 2"]
CENSURE_STABILITY_DELTA = -1          # [canonical: faction_layer_v30 §5.4 — Censure "Target effect: Stability −1"]
CENSURE_MANDATE_DELTA = -1            # [canonical: faction_layer_v30 §5.4 — Censure "Target effect: Mandate −1"]

# The motion's forensic/precedent-citing footing. [SEED: default to 'Memory' genre, mirroring how
# ED-SC-0006's Emergency Council bridge (sim/cross_scale/scene_dispatch.py) defaulted its contest to
# the Memory genre — both bridges only ever move on an Appeal.LOGOS-equivalent legalistic footing (a
# censure is a forensic charge against a record, not a projective proposal about the future). Kept
# consistent across the two bridges on purpose; revisable, not fabricated data.]
CENSURE_MOTION_GENRE = "Memory"       # [canonical: parliamentary_vote §10 GENRES = ("Memory","Projection")]

# Sentinel returned by the _try_* faction-action dispatch convention (see faction_action.py) when the
# action is unavailable and control should fall through to the next candidate action.
_NOOP = "invalid"


def select_censure_target(proposer, world):
    """[SEED — realist balance-of-power default, ED-SC-0007 residual] Pick the faction a Censure is
    aimed at.

    No grudge / hostility / inter-faction-relationship stat exists in game_state.Faction, so there is
    no fabricated relationship signal to key targeting off of (see ED-FA-0004: the Faction schema is
    L/Sta/W/I/Mil only). The simplest NON-FABRICATED signal already present is relative Mandate (L)
    standing. The defensible default, grounded in realist balance-of-power logic — weaker members of a
    deliberative body collectively move to check the strongest — is:

        target = the highest-L parliamentary-eligible faction OTHER than the proposer.

    [historical precedent: this is the institutional logic of Athenian *ostracism* — a standing
    procedure by which the assembly moves against its most prominent member precisely because of that
    prominence, not from an arbitrary personal quarrel. The Venetian constitution likewise engineered
    the whole magistracy to blunt any single house's ascendancy (Contarini, *De magistratibus et
    republica Venetorum*). Both are docket-attested: fa_se_historical_precedent_research_v1.md l.75
    ("Athenian kleroterion & ostracism"; Contarini in the same civic-humanism inventory). The signal
    is the target's own prominence, which the schema already stores.]

    Deterministic: ties on L break by faction name (ascending), so selection is a pure function of
    world state — no rng consumed here (targeting determinism is structural, not seeded).

    Returns the target Faction, or None if no eligible other faction exists (→ caller no-ops).
    """
    candidates = sorted(
        (f for name, f in world.factions.items()
         if f.parliamentary and name != proposer.name),
        key=lambda f: (-f.L, f.name),
    )
    return candidates[0] if candidates else None


def propose_censure(proposer, world, rng) -> str:
    """Propose a Censure motion (mildest Parliamentary Sanction tier, faction_layer_v30 §5.4).

    Flow: eligibility gate → target selection → declaration assembly → run_parliamentary_vote →
    apply the Censure-specific target effect on a pass. Returns a dispatch-style result string
    ('ParliamentarySanction_Censure:' + vote status) for a later wiring lane, or the '{_NOOP}'
    sentinel when the action is unavailable (ineligible proposer / no valid target).

    proposer: a game_state.Faction (must also be present in world.factions by name — the vote
              resolver looks declarations up by name).
    rng: passed straight through to run_parliamentary_vote's dice_engine.roll_pool for a
         campaign-deterministic ballot.
    """
    # ── Eligibility gate (GD-3 + §5.4 proposer minimum) ──────────────────────────────────────
    # [canonical: GD-3 — extra-parliamentary factions cannot propose Parliamentary motions]
    # [canonical: faction_layer_v30 §5.4 — Censure requires proposer Mandate >= 2; Mandate == L
    #  per the PRE-LPS-1 convention banner above]
    if not proposer.parliamentary or proposer.L < CENSURE_PROPOSER_MIN_MANDATE:
        return _NOOP

    target = select_censure_target(proposer, world)
    if target is None:
        return _NOOP

    # ── Declaration assembly ─────────────────────────────────────────────────────────────────
    # Only the two mechanically-necessary voices are declared explicitly; every other eligible
    # faction simply Abstains (run_parliamentary_vote treats eligible-but-undeclared factions as
    # abstainers). The proposer declares side A (for). The target — always parliamentary-eligible
    # by construction of select_censure_target — is the natural against-voice: a faction inherently
    # opposes a motion to sanction itself, so it declares side B. No fuller roster is fabricated.
    parties = [
        VoteDeclaration(faction_name=proposer.name, side="A", genre=CENSURE_MOTION_GENRE),
        VoteDeclaration(faction_name=target.name, side="B", genre=CENSURE_MOTION_GENRE),
    ]

    motion = Motion(
        motion_id=f"censure_{proposer.name}_vs_{target.name}_s{world.season}",
        primary_genre=CENSURE_MOTION_GENRE,
    )

    result = run_parliamentary_vote(motion, parties, world, rng=rng)

    # ── Apply the Censure-specific target effect (caller's job) ───────────────────────────────
    # run_parliamentary_vote self-applies ONLY the generic §10 Total-Victory Mandate −1 to the
    # losing coalition's dominant faction; it does NOT apply the per-motion-type §5.4 target effect.
    # That is the caller's responsibility per the design split (§10 = how the vote resolves; §5.4 =
    # what the passed motion does).
    #
    # [SEED / NEEDS-JORDAN — emergent composition, NOT settled canon]: on a TOTAL-VICTORY censure
    # pass these two rules compose to −2 Mandate on the target (−1 §10 TV rider + −1 §5.4 Censure).
    # Neither faction_layer_v30 §5.4 nor social_contest_v30 §10 explicitly states that the two
    # Mandate penalties compound on the same faction within one motion; that they STACK is the literal
    # result of applying both layers faithfully, and is the defensible default (a censure won by a
    # crushing margin is both a formal sanction AND a reputational rout). It is flagged here rather
    # than silently ratified — a human may instead choose to cap the target at −1 on a TV pass. The
    # narrow-edge golden in test_total_victory_pass_stacks_* pins the CURRENT composition, not a
    # ratified design intent.
    if result.status == "passed":
        # MULTS-multiplied granular_delta so .adjust() lands a full −1 point, matching
        # parliamentary_vote.py's own `adjust("L", DELTA * MULTS["L"])` convention.
        target.adjust("Sta", CENSURE_STABILITY_DELTA * MULTS["Sta"])  # [canonical: §5.4 Stability −1]
        target.adjust("L", CENSURE_MANDATE_DELTA * MULTS["L"])        # [canonical: §5.4 Mandate −1]

    return f"ParliamentarySanction_Censure:{result.status}"


# TODO(future extension, out of ED-SC-0007 scope): the other four Parliamentary Sanction tiers
# (Embargo · Blockade · Combined Embargo+Blockade · Outlawry) and the five constructive motions
# (Subsidy · War Authorisation · Treaty Ratification · Recognition Challenge · Succession
# Endorsement) from the faction_layer_v30.md §5.4 table. Per ED-FA-0006 the five punitive tiers are
# one parameterized "Parliamentary Sanction" action differing only in {proposer min, vote bar,
# penalty magnitude/duration} + two riders (Blockade Military-3 gate, Outlawry CB-to-all); a later
# lane can generalize propose_censure into propose_sanction(tier) once per-season/renewal duration
# plumbing (Embargo/Blockade "until lifted") and the Supermajority vote bar exist. Censure is the
# representative one-time-effect slice.
#
# Also NOT modeled here (in-scope omission, flagged for the future-extension tracker): the §5.5
# Target Rebuttal (faction_layer_v30.md §5.4/§5.5 — the target may Rebuttal a Censure at
# M = Mandate − 2, a Phase-4 Social action that can negate the motion's costs and, on an Overwhelming
# result, damage the proposer). This module models the target only as a side-B voter — the task's
# endorsed simplification ("the target naturally opposes a motion against itself"); the Rebuttal
# sub-contest is a separate later slice.
