"""[ED-MB-0048 / plan v2 §3 A3] The `MAX_SUB_PHASES` bound must never drop engagements silently.

`resolve_engagements_cascading` sorts contact pairs by attacker depth, buckets them into 1-row
depth groups, and resolves at most `MAX_SUB_PHASES` of them. Groups past the bound used to hit a
**bare `break`**: zero damage that tick, nothing recorded, no trace. The measured incidence is zero
on every shipped workload (see the artifact below), which is why A3's severity dropped from 1 —
but a silent drop must not STAY silent, because the only reason anyone knows it is zero is that
somebody wrote a bespoke probe.

Two tests, and they do different jobs:

  1. **The counter can observe a truncation.** §0.1 #2 — an assertion that cannot observe the
     failure it excludes is not a weak test, it is an absent one. So this drives the bound DOWN
     until truncation is forced and asserts the counters see it, including a strictly positive
     engaged-troop WEIGHT. Without this, test 2's zero would be indistinguishable from a counter
     that is wired to nothing.

  2. **At the shipped bound, a genuinely cascading workload truncates nothing** — and asserts its
     own non-vacuity (`checked >= 1` multi-group calls actually occurred), so it cannot pass by
     never cascading.

Why weight and not a fire-count: truncation drops the DEEPEST-sorted groups, so its bias is
systematic against deep formations. A count of ticks-that-truncated cannot express that.

**Orchestrator-measured artifact (2026-07-29, this session), all four bat.py modes at the CI pin
vector plus the honest gauge in each mode — 64,273 resolver calls, 0 truncations, max depth-group
count 3 against a bound of 5:**

    workload                     calls    trunc   max groups   histogram
    bat.py [unit]               11,139        0            2   {0:6122, 1:4849, 2:168}
    bat.py [unit_field]          7,198        0            3   {0:1944, 1:3993, 2:1181, 3:80}
    bat.py [cell_field]          8,946        0            3   {0:1512, 1:6513, 2:784, 3:137}
    bat.py [cell]               20,010        0            2   {0:9037, 1:10781, 2:192}
    gauge multi (n=4) x4 modes  16,980        0            3   —

Every one of those four battery runs reproduced its golden digest byte-exactly with the probe
attached, which is also the evidence that the instrument does not perturb the thing it measures.
This CONFIRMS the audit's lead (0 truncations, max group 3 vs bound 5), which until now had been
produced by a single agent and never re-derived (plan §0 marks it UNVERIFIED, G12). The agent's
larger-N call count (102,260) is NOT replicated here and remains unverified; the direction and the
conclusion are.
"""
import os
import sys

_SIM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

import mass_battle.orchestration as O                                  # noqa: E402
from mass_battle.engine import build_army, SIDE_A_START_ROW            # noqa: E402


def _sub(faction, row, col, advance_dir):
    army = build_army([{'shape': 'Line', 'troop_type': 'infantry', 'troops': 300.0,
                        'concentration': 100.0, 'starting_position': (row, col)}],
                      faction, faction)
    su = army.subunits[0]
    su.advance_dir = advance_dir
    return su, army


def _staircase(n_groups):
    """n_groups attacker subunits at depths 4 rows apart, each paired with its own defender.

    `_cascade_depth_key` buckets by 1-row proximity, so a 4-row stride guarantees exactly one
    depth group per attacker — the minimal shape that exercises the sub-phase split at all.
    """
    unit_a = None
    unit_b = None
    pairs = []
    attackers, defenders = [], []
    for i in range(n_groups):
        a, army_a = _sub('A', SIDE_A_START_ROW + 4 * i, 10 + 2 * i, +1)
        b, army_b = _sub('B', SIDE_A_START_ROW + 4 * i + 1, 10 + 2 * i, -1)
        attackers.append((a, army_a))
        defenders.append((b, army_b))
    # One Unit per side carrying every subunit, so unit-level gates see a live body.
    unit_a = attackers[0][1]
    unit_b = defenders[0][1]
    unit_a.subunits = [a for a, _ in attackers]
    unit_b.subunits = [b for b, _ in defenders]
    for (a, _), (b, _) in zip(attackers, defenders):
        a._unit = unit_a
        b._unit = unit_b
        pairs.append({'atom_a': a, 'atom_b': b,
                      'a_cells': list(a.cells()), 'b_cells': list(b.cells())})
    return unit_a, unit_b, pairs


def _group_count(pairs):
    """Reproduce the resolver's own bucketing, to know how many groups a fixture really makes."""
    sp = sorted(pairs, key=O._cascade_depth_key)
    groups, cur, depth = [], [sp[0]], O._cascade_depth_key(sp[0])
    for p in sp[1:]:
        d = O._cascade_depth_key(p)
        if abs(d - depth) <= 1:
            cur.append(p)
        else:
            groups.append(cur)
            cur, depth = [p], d
    groups.append(cur)
    return len(groups)


def test_counter_observes_a_truncation_when_the_bound_bites(monkeypatch):
    """Force truncation by lowering the bound, and assert every counter sees it.

    MUTATION (this is the artifact §0.1 #3 asks for): restore the bare `break` in
    `resolve_engagements_cascading` and this test fails on `truncated_groups == 0`. Drop only the
    `truncated_troops` accumulation and it still fails, on the weight assertion — the two are
    independently observable, which is the point of asserting the weight rather than a flag.
    """
    unit_a, unit_b, pairs = _staircase(4)
    n = _group_count(pairs)
    assert n == 4, f"fixture must produce 4 depth groups, produced {n}"

    monkeypatch.setattr(O, 'MAX_SUB_PHASES', 2)
    res = O.resolve_engagements_cascading(unit_a, unit_b, pairs, t=1)

    assert res['n_groups'] == 4
    assert res['truncated_groups'] == 2, res
    assert res['truncated_pairs'] == 2, res
    assert res['truncated_troops'] > 0.0, (
        "engaged-troop weight of the dropped pairs must be strictly positive — a zero here means "
        "the weight is not actually being computed, and the counter degrades to a fire-count")


def test_counter_is_silent_when_the_bound_does_not_bite(monkeypatch):
    """The same fixture, with headroom: every group resolves and nothing is reported dropped."""
    unit_a, unit_b, pairs = _staircase(4)
    monkeypatch.setattr(O, 'MAX_SUB_PHASES', 9)
    res = O.resolve_engagements_cascading(unit_a, unit_b, pairs, t=1)
    assert res['n_groups'] == 4
    assert res['truncated_groups'] == 0
    assert res['truncated_pairs'] == 0
    assert res['truncated_troops'] == 0.0


def test_shipped_bound_truncates_nothing_on_a_cascading_workload():
    """Incidence zero at the SHIPPED bound — with a non-vacuity assertion attached.

    A run in which nothing ever cascades would report zero truncations while proving nothing at
    all (§0.1 #4: a number without a control is not a measurement). So this counts how many
    resolver calls produced more than one depth group and requires that count to be non-zero
    before the zero-truncation claim is allowed to mean anything.
    """
    from mass_battle.config import MAX_SUB_PHASES
    multi_group_calls = 0
    truncated = 0
    max_groups = 0
    # Bounds chosen to stay under the shipped bound of 5 while genuinely splitting: this asserts
    # the SHIPPED value has headroom over fixtures that really do cascade, which is the claim.
    for n in (2, 3, 4):
        unit_a, unit_b, pairs = _staircase(n)
        res = O.resolve_engagements_cascading(unit_a, unit_b, pairs, t=1)
        if res['n_groups'] > 1:
            multi_group_calls += 1
        max_groups = max(max_groups, res['n_groups'])
        truncated += res['truncated_groups']

    assert multi_group_calls >= 3, (
        f"non-vacuity: only {multi_group_calls} call(s) cascaded, so a zero-truncation result "
        f"says nothing about the bound")
    assert max_groups < MAX_SUB_PHASES, (
        f"observed {max_groups} depth groups against MAX_SUB_PHASES={MAX_SUB_PHASES} — the "
        f"headroom this test asserts is gone; re-measure before changing the bound (it is "
        f"CALIBRATED-DEBT and moving it moves goldens)")
    assert truncated == 0
