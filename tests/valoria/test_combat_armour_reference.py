"""Armour-interaction DRIFT GATE (ED-PC-0040) — collateral balance damage must be deliberate, never silent.

WHY THIS FILE EXISTS. The four-dimension audit's remediation arc shipped two undisclosed tier regressions in
consecutive batches. ED-PC-0038 aimed at the plate tier and moved MAIL (odachi −23pp, naginata −25pp, staff −12pp),
shipping a ledger entry that called mail "a tier the fix was never meant to touch". ED-PC-0039 then moved the odachi
a further −18pp, also undisclosed. Neither was caught by a test. Both were caught, batches later, by a human reading
numbers off an ad-hoc script — which is to say, by luck and by an expensive adversarial review.

WHAT THIS GATE DOES. `tests/valoria/data/combat_armour_reference.json` records the full weapon roster across all four
armour tiers, deterministically seeded. This test recomputes it and fails on any cell that moved beyond tolerance.

WHAT IT IS NOT. It is not a balance freeze, and it must never be argued with as though it were. Balance *should*
change. The gate exists so that a change is VISIBLE AND ATTRIBUTED rather than discovered three batches later:

    intended change  ->  `python workbench/armour_participation.py --update`, commit the regenerated table,
                         and the diff is the disclosure. State in the ledger entry what moved and why.
    unintended change ->  the gate just told you your fix has a blast radius you did not know about.

The failure mode to guard against in this file itself is regenerating the reference reflexively to make a red build
green. If you find yourself doing that without reading the diff, the gate has been defeated and the exact failure it
was built to prevent is back.
"""
import os
import sys

import pytest

# Tolerance sized from the two regressions this gate is built from. Because seeds are deterministic per (weapon,
# tier), an unchanged engine reproduces the reference EXACTLY — the tolerance is absorbing legitimate small shifts in
# the RNG trajectory from unrelated changes, not sampling noise. 0.15 comfortably catches both historical misses
# (odachi −18pp and −23pp, naginata −25pp) while leaving room for incidental movement.
TOLERANCE = 0.15


def _instrument():
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1', 'workbench'))   # the workbench stayed at plan position `31b`
    import armour_participation
    return armour_participation


@pytest.mark.slow
def test_armour_interaction_matches_the_committed_reference():
    AP = _instrument()
    if not os.path.exists(AP.REFERENCE_PATH):
        pytest.fail("the committed armour reference table is missing — regenerate it with "
                    "`python workbench/armour_participation.py --update` and commit it; this gate is inert without it")
    moved, added, removed = AP.drift(tolerance=TOLERANCE)

    if added or removed:
        pytest.fail(
            f"the weapon roster changed without the reference table being regenerated "
            f"(added: {added or 'none'}; removed: {removed or 'none'}). Run "
            f"`python workbench/armour_participation.py --update` and commit the result, so the new weapons' "
            f"armour behaviour is on the record from the start.")

    if moved:
        lines = "\n".join(
            f"    {w:22s} {t:7s} {field:8s} {was} -> {now}   (delta {abs((now or 0) - (was or 0)):+.2f})"
            for w, t, field, was, now in moved[:25])
        more = f"\n    ... and {len(moved) - 25} more" if len(moved) > 25 else ""
        pytest.fail(
            f"{len(moved)} armour-interaction cell(s) moved beyond {TOLERANCE:.2f} from the committed reference:\n"
            f"{lines}{more}\n\n"
            f"  If this is INTENDED: regenerate with `python workbench/armour_participation.py --update`, commit the\n"
            f"  table, and say in the ledger entry which tiers moved and why. The diff is the disclosure.\n"
            f"  If this is NOT intended: your change has a blast radius you did not know about — this is exactly the\n"
            f"  ED-PC-0038/0039 failure (a plate fix that silently moved mail), caught this time before it shipped.")


def test_reference_table_covers_the_whole_roster():
    """The reference must cover EVERY weapon, not a watched subset.

    Restricting it would recreate the original blind spot: the regressions this gate exists for landed on the
    odachi, naginata and staff — none of which any guard in the corpus was watching."""
    import json
    AP = _instrument()
    from modules.combat.combatant import WEAPONS
    with open(AP.REFERENCE_PATH, encoding='utf-8') as f:
        ref = json.load(f)
    missing = sorted(set(WEAPONS) - set(ref['table']))
    assert not missing, (
        f"{len(missing)} weapon(s) absent from the armour reference table: {missing}. Every weapon in the roster is "
        f"covered by design — a partial table reintroduces the unwatched-weapon blind spot this gate was built for.")
    assert ref['n'] >= 40, f"reference generated at n={ref['n']}, too small to be a stable baseline"
    for tiers in ref['table'].values():
        assert set(tiers) == {'none', 'light', 'medium', 'heavy'}, "reference must cover all four armour tiers"


# ── PC_D (B15.05): armour turns a blade by a draw ──────────────────────────────────────────────────────────────────
# The coverage gap is a chance at the one damage call, not an average inside it. The four tests below read it off fights
# (the trace seam and a spy on `core.strike`), never off the helper that draws it.

def _fight(a_armor, b_armor, seed, weapon='arming', trace=None):
    from engine.dice_engine import draw
    from modules.combat import wrapper
    from modules.combat.combatant import Combatant
    from modules.combat.config import CFG
    A, B = Combatant('A', weapon=weapon, armor=a_armor), Combatant('B', weapon=weapon, armor=b_armor)
    wrapper.fight(A, B, CFG, draw.seeded(draw.H2('armour_gap', seed)), trace=(trace.append if trace is not None else None))


def _success_blows(armor, fights):
    """The damage of every Success struck against a defender in `armor` (light armour on the other side), by value."""
    from modules.combat import core
    seen, orig = [], core.strike

    def spy(attacker, defender, deg, cfg, *a, **k):
        v = orig(attacker, defender, deg, cfg, *a, **k)
        if deg == 'success' and defender.armor == armor:
            seen.append(v)
        return v

    core.strike = spy
    try:
        for s in range(fights):
            _fight('light' if armor != 'none' else 'none', armor, s)
    finally:
        core.strike = orig
    return seen


def test_success_against_heavy_has_more_than_one_damage_value():
    """Gate 1: a Success against plate is not one number, and the share of landed blows that draw no blood is higher
    against plate than against bare skin by more than the interval (it was one value, and nothing but the defence coin)."""
    heavy, bare = _success_blows('heavy', 250), _success_blows('none', 250)   # 250 fights: a yield ends a lethal fight early (B15.10), so 150 held fewer than 100 Successes
    assert len(heavy) >= 100 and len(bare) >= 100
    assert len(set(heavy)) > 1, sorted(set(heavy))
    p_heavy, p_bare = sum(v == 0 for v in heavy) / len(heavy), sum(v == 0 for v in bare) / len(bare)
    interval = 3.0 * (p_heavy * (1 - p_heavy) / len(heavy) + p_bare * (1 - p_bare) / len(bare)) ** 0.5
    assert p_heavy - p_bare > interval, (p_heavy, p_bare, interval)


def test_light_against_heavy_plated_man_felled_sometimes():
    """Gate 2: 1,500 arming-sword fights, light against heavy: the plated man is felled a share strictly above 0."""
    felled = 0
    for s in range(1500):
        tr = []
        _fight('light', 'heavy', s, trace=tr)
        felled += any(e['kind'] == 'engagement_end' and e['felled'] == 'B' for e in tr)
    assert felled > 0, "the plated man was felled in 0 of 1500: plate is an immunity"


def _bare_share(armor, fights):
    """(blows struck at a defender in `armor`, those that reached a bare zone, `wound` events missing the `bare` flag) over `fights` mirrors."""
    from modules.combat import core
    blows = [0, 0]
    orig = core.strike

    def spy(attacker, defender, deg, cfg, *a, **k):
        if defender.armor == armor:
            blows[0] += 1
            blows[1] += bool(k.get('bare'))
        return orig(attacker, defender, deg, cfg, *a, **k)

    unflagged = 0
    core.strike = spy
    try:
        for s in range(fights):
            tr = []
            _fight(armor, armor, s, trace=tr)
            unflagged += sum('bare' not in e for e in tr if e['kind'] == 'wound')
    finally:
        core.strike = orig
    return blows[0], blows[1], unflagged


def test_coverage_gap_zero_gives_no_bare_zone_blows():
    """Gate 3: at the shipped gap the share of blows on armour that reach a bare zone is near COVERAGE_GAP; at 0 none does."""
    from modules.combat import core
    n, bare, unflagged = _bare_share('heavy', 60)
    assert n >= 200 and unflagged == 0, (n, unflagged)
    assert 0.6 * core.COVERAGE_GAP < bare / n < 1.4 * core.COVERAGE_GAP, bare / n
    was, core.COVERAGE_GAP = core.COVERAGE_GAP, 0.0
    try:
        n0, bare0, unflagged0 = _bare_share('heavy', 60)
    finally:
        core.COVERAGE_GAP = was
    assert n0 >= 200 and bare0 == 0 and unflagged0 == 0, (n0, bare0, unflagged0)


def test_no_turned_event_between_unarmoured_men():
    """The falsifier's second clause: a blade is turned only by a harness. Bare men turn nothing; plate does (the observer sees it)."""
    turned = {}
    for armor in ('none', 'heavy'):
        count = rounds = 0
        for s in range(100):
            tr = []
            _fight(armor, armor, s, trace=tr)
            count += sum(e['kind'] == 'turned' for e in tr)
            rounds += sum(e['kind'] == 'engagement_end' for e in tr)
        assert rounds >= 100
        turned[armor] = count
    assert turned['none'] == 0 and turned['heavy'] > 0, turned
