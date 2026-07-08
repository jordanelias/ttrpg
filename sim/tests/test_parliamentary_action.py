"""
sim/tests/test_parliamentary_action.py — Parliamentary Sanction (Censure tier) mechanism oracle

Guards sim/provincial/parliamentary_action.py — the ED-SC-0007 residual "parliamentary_vote-in-the-
loop" MECHANISM (proposer/target/declaration authoring for the §10 BG-vote resolver, which shipped
tested but caller-less). Scope is the CENSURE tier only (faction_layer_v30.md §5.4: Mandate-2
proposer min, Majority vote, target Stability −1 / Mandate −1, no proposer cost).

Conventions (matching sim/tests/test_echo_transport.py / test_mc_v18_regression.py):
  - pinned seeds, no unseeded randomness; every roll goes through a random.Random(seed).
  - the passing/committee/failing seeds below are pinned goldens over sim.provincial.parliamentary_action
    on a fixed 4-faction strong-proposer world; a surprise failure means the proposal mechanism or the
    §10 resolver changed — investigate before repinning.
"""
import os
import sys
import random

import pytest

# Make the repo root importable so `import sim.*` resolves when pytest runs from anywhere.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from sim.autoload import game_state
from sim.provincial import parliamentary_action as pa


# ── Fixtures ──────────────────────────────────────────────────────────────────

def _strong_proposer_world(seed):
    """Crown (proposer) strong at Mandate 7, the other three eligible factions weak at Mandate 2.

    This makes side A (proposer) the larger Mandate pool so the vote can actually pass, and pins the
    target: select_censure_target picks the highest-L OTHER faction — a three-way tie at L=2.0 that
    breaks by name ascending → 'Church'."""
    w = game_state.create_world(seed=seed)
    w.factions['Crown'].L = 7.0
    w.factions['Church'].L = 2.0
    w.factions['Hafenmark'].L = 2.0
    w.factions['Varfell'].L = 2.0
    return w


def _faction_snapshot(world):
    return {n: (round(f.L, 6), round(f.Sta, 6)) for n, f in world.factions.items()}


# ── Targeting selection (deterministic, no rng) ────────────────────────────────

def test_targeting_selects_highest_L_other_faction():
    """[SEED realist balance-of-power default] target = highest-Mandate parliamentary-eligible faction
    OTHER than the proposer."""
    w = game_state.create_world(seed=0)
    w.factions['Crown'].L = 3.0
    w.factions['Church'].L = 6.0        # the strongest OTHER faction
    w.factions['Hafenmark'].L = 4.0
    w.factions['Varfell'].L = 2.0
    target = pa.select_censure_target(w.factions['Crown'], w)
    assert target is not None and target.name == 'Church'


def test_targeting_excludes_proposer_even_if_proposer_is_strongest():
    """The proposer is never its own target: with Crown the strongest overall, the target is the
    strongest of the REMAINING factions."""
    w = game_state.create_world(seed=0)
    w.factions['Crown'].L = 7.0         # strongest overall — must be excluded
    w.factions['Church'].L = 5.0        # strongest OTHER
    w.factions['Hafenmark'].L = 4.0
    w.factions['Varfell'].L = 3.0
    target = pa.select_censure_target(w.factions['Crown'], w)
    assert target.name == 'Church'


def test_targeting_tie_breaks_by_name_ascending_deterministically():
    """Ties on Mandate break by faction name ascending, so targeting is a pure, rng-free function of
    world state (deterministic on replay)."""
    w = game_state.create_world(seed=0)
    w.factions['Crown'].L = 3.0
    w.factions['Church'].L = 5.0
    w.factions['Hafenmark'].L = 5.0     # tie with Church at 5.0
    w.factions['Varfell'].L = 5.0       # tie too
    # candidates other than Crown: Church, Hafenmark, Varfell all at 5.0 → 'Church' wins on name.
    for _ in range(3):
        assert pa.select_censure_target(w.factions['Crown'], w).name == 'Church'


def test_targeting_excludes_extra_parliamentary_factions():
    """GD-3: an extra-parliamentary faction is not an eligible target even if highest-L."""
    w = game_state.create_world(seed=0)
    w.factions['Crown'].L = 3.0
    w.factions['Church'].L = 9.0
    w.factions['Church'].parliamentary = False   # highest-L but excluded by GD-3
    w.factions['Hafenmark'].L = 4.0
    w.factions['Varfell'].L = 2.0
    target = pa.select_censure_target(w.factions['Crown'], w)
    assert target.name == 'Hafenmark'


def test_targeting_returns_none_when_no_eligible_other():
    """No other parliamentary-eligible faction → no target."""
    w = game_state.create_world(seed=0)
    for n in ('Church', 'Hafenmark', 'Varfell'):
        w.factions[n].parliamentary = False
    assert pa.select_censure_target(w.factions['Crown'], w) is None


# ── Eligibility gating (no-op) ─────────────────────────────────────────────────

def test_below_mandate_2_is_a_noop():
    """§5.4: Censure requires proposer Mandate >= 2. Below that → sentinel no-op, no vote, no state
    change anywhere in the world."""
    w = _strong_proposer_world(seed=5)
    w.factions['Crown'].L = 1.5          # below the Mandate-2 proposer minimum
    before = _faction_snapshot(w)
    result = pa.propose_censure(w.factions['Crown'], w, random.Random(5))
    assert result == 'invalid'
    assert _faction_snapshot(w) == before, "an ineligible proposal must not mutate any faction"


def test_extra_parliamentary_proposer_is_a_noop():
    """GD-3: an extra-parliamentary faction cannot propose, even with ample Mandate."""
    w = _strong_proposer_world(seed=5)
    w.factions['Crown'].parliamentary = False
    before = _faction_snapshot(w)
    result = pa.propose_censure(w.factions['Crown'], w, random.Random(5))
    assert result == 'invalid'
    assert _faction_snapshot(w) == before


def test_no_valid_target_is_a_noop():
    """Eligible proposer but no eligible OTHER faction → no-op (nothing to censure)."""
    w = _strong_proposer_world(seed=5)
    for n in ('Church', 'Hafenmark', 'Varfell'):
        w.factions[n].parliamentary = False
    before = _faction_snapshot(w)
    result = pa.propose_censure(w.factions['Crown'], w, random.Random(5))
    assert result == 'invalid'
    assert _faction_snapshot(w) == before


# ── Passing vote applies the §5.4 target effect ────────────────────────────────

def test_passing_vote_applies_censure_target_effect():
    """Pinned seed 5 → an ORDINARY (non-total-victory) pass: the target (Church) takes exactly
    Stability −1 and Mandate −1 per faction_layer_v30 §5.4; the proposer pays no cost (one-time,
    no proposer cost). No OTHER faction is touched."""
    w = _strong_proposer_world(seed=5)
    target = pa.select_censure_target(w.factions['Crown'], w)
    assert target.name == 'Church'
    sta_before, l_before = target.Sta, target.L
    proposer_before = (w.factions['Crown'].Sta, w.factions['Crown'].L)

    result = pa.propose_censure(w.factions['Crown'], w, random.Random(5))

    assert result == 'ParliamentarySanction_Censure:passed'
    assert target.Sta == pytest.approx(sta_before - 1.0), "§5.4 Stability −1 to target"
    assert target.L == pytest.approx(l_before - 1.0), "§5.4 Mandate −1 to target"
    # Proposer bears no cost (Censure "Proposer cost: None").
    assert (w.factions['Crown'].Sta, w.factions['Crown'].L) == proposer_before
    # Untouched bystanders.
    assert w.factions['Hafenmark'].L == pytest.approx(2.0)
    assert w.factions['Varfell'].L == pytest.approx(2.0)


def test_total_victory_pass_stacks_section10_rider_and_section5_4_effect():
    """Pinned seed 1 → a TOTAL-VICTORY pass. run_parliamentary_vote self-applies the generic §10
    Total-Victory Mandate −1 to the losing dominant faction (the target), AND propose_censure applies
    the §5.4 Censure Mandate −1. This pins the CURRENT composition of the two rules (−2 total on a TV
    pass); whether they SHOULD stack on the same faction is an emergent [SEED] composition flagged
    NEEDS-JORDAN in parliamentary_action.py, not settled canon — if a human caps it at −1 on a TV
    pass, this golden is expected to change. Church starts Mandate 2.0; −1 (§10 TV) −1 (§5.4) = 0.0,
    clamped to the Faction floor 0.5."""
    w = _strong_proposer_world(seed=1)
    target = pa.select_censure_target(w.factions['Crown'], w)
    assert target.name == 'Church'
    sta_before = target.Sta

    result = pa.propose_censure(w.factions['Crown'], w, random.Random(1))

    assert result == 'ParliamentarySanction_Censure:passed'
    # Mandate: −2 total (−1 §10 TV rider + −1 §5.4), clamped to Faction floor 0.5.
    assert target.L == pytest.approx(0.5), "stacked −2 Mandate clamps at the 0.5 Faction floor"
    # Stability: only the §5.4 −1 (the §10 TV rider is Mandate-only).
    assert target.Sta == pytest.approx(sta_before - 1.0)


# ── Non-passing votes apply nothing beyond run_parliamentary_vote's own effects ─

def test_committee_result_applies_no_censure_effect():
    """Pinned seed 0 → committee (neither side clears the bar). No §5.4 target effect is applied; the
    target's Stability and Mandate are untouched by propose_censure."""
    w = _strong_proposer_world(seed=0)
    target = pa.select_censure_target(w.factions['Crown'], w)
    before = _faction_snapshot(w)

    result = pa.propose_censure(w.factions['Crown'], w, random.Random(0))

    assert result == 'ParliamentarySanction_Censure:committee'
    # A committee (non-total) outcome triggers neither the §5.4 effect nor the §10 TV rider.
    assert _faction_snapshot(w) == before, "committee must leave all faction stats unchanged"


def test_failed_result_applies_no_censure_effect():
    """Pinned seed 9 → failed (motion voted down without total defeat). No §5.4 target effect."""
    w = _strong_proposer_world(seed=9)
    before = _faction_snapshot(w)

    result = pa.propose_censure(w.factions['Crown'], w, random.Random(9))

    assert result == 'ParliamentarySanction_Censure:failed'
    assert _faction_snapshot(w) == before, "a failed vote leaves all faction stats unchanged"


# ── Determinism ────────────────────────────────────────────────────────────────

def test_same_seed_same_outcome():
    """Determinism: identical seed → identical result string AND identical resulting world stats."""
    runs = []
    for _ in range(2):
        w = _strong_proposer_world(seed=5)
        r = pa.propose_censure(w.factions['Crown'], w, random.Random(5))
        runs.append((r, _faction_snapshot(w)))
    assert runs[0] == runs[1]


def test_distinct_seeds_can_diverge():
    """Sanity that the pinned seeds are genuinely exercising the resolver's randomness, not a
    constant: the committee seed (0) and the passing seed (5) reach different Censure outcomes."""
    w0 = _strong_proposer_world(seed=0)
    r0 = pa.propose_censure(w0.factions['Crown'], w0, random.Random(0))
    w5 = _strong_proposer_world(seed=5)
    r5 = pa.propose_censure(w5.factions['Crown'], w5, random.Random(5))
    assert r0 == 'ParliamentarySanction_Censure:committee'
    assert r5 == 'ParliamentarySanction_Censure:passed'
    assert r0 != r5
