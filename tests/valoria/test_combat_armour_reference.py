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

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')

# Tolerance sized from the two regressions this gate is built from. Because seeds are deterministic per (weapon,
# tier), an unchanged engine reproduces the reference EXACTLY — the tolerance is absorbing legitimate small shifts in
# the RNG trajectory from unrelated changes, not sampling noise. 0.15 comfortably catches both historical misses
# (odachi −18pp and −23pp, naginata −25pp) while leaving room for incidental movement.
TOLERANCE = 0.15


def _instrument():
    pytest.importorskip("numpy")
    sys.path.insert(0, os.path.join(ENGINE, 'workbench'))
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
    sys.path.insert(0, ENGINE)
    from combatant import WEAPONS
    with open(AP.REFERENCE_PATH, encoding='utf-8') as f:
        ref = json.load(f)
    missing = sorted(set(WEAPONS) - set(ref['table']))
    assert not missing, (
        f"{len(missing)} weapon(s) absent from the armour reference table: {missing}. Every weapon in the roster is "
        f"covered by design — a partial table reintroduces the unwatched-weapon blind spot this gate was built for.")
    assert ref['n'] >= 40, f"reference generated at n={ref['n']}, too small to be a stable baseline"
    for tiers in ref['table'].values():
        assert set(tiers) == {'none', 'light', 'medium', 'heavy'}, "reference must cover all four armour tiers"
