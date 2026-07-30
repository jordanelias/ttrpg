"""[ED-MB-0054 / plan v2 B1c] Formation drift must not leave per-cell containers holding dead ids.

`check_drift` re-keyed `cell_troops` and, on the node path, `_node_pos` — and nothing else. Measured
over the `bat.py` `cell` battery: 10 drift events, and SIX maps left holding dead ids in all ten.
Three more than the audit named, and the pair it missed is the worse one — `cell_offsets` is
accumulated displacement, so a missing entry snaps the body back to its SPAWN row mid-advance.

The guard is on the INVARIANT ("no per-cell container may hold a non-live id after drift"),
parameterized over the container list, so a container added later inherits it by being added to one
tuple — rather than one test per map, which is how the original three-map gap happened.
"""
import os
import sys

import pytest

_SIM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

import mass_battle.hierarchy.units as U                       # noqa: E402
from mass_battle.engine import build_army                     # noqa: E402

# Containers rekey_cells owns. cell_morale / cell_start_troops / cell_breakpoint are EXCLUDED on
# purpose: drift has no old->new bijection and their policy is a §6-class ruling (mean vs
# troop-weighted for morale; redraw vs inherit for a drawn breakpoint), not a derivation.
_REKEYED = ('cell_offsets', 'cell_offsets_c', 'halted_cells', 'cell_last_speed',
            'cell_facing_vec', '_cell_target', '_speed_accum', 'merged_cells')
_RULING_DEFERRED = ('cell_morale', 'cell_start_troops', 'cell_breakpoint')


def _drifting_subunit():
    """An Arrowhead below its MIN_DISCIPLINE, with every per-cell container populated."""
    u = build_army([{'shape': 'Arrowhead', 'tier': 3, 'troop_type': 'infantry'}], 'A', 'A',
                   anchor_col=12)
    a = u.subunits[0]
    ids = list(a.cell_troops)
    assert len(ids) >= 4, "fixture must have a multi-cell body to re-key"
    for i, pid in enumerate(ids):
        a.cell_offsets[pid] = 5 + i
        a.cell_offsets_c[pid] = 1
        a.cell_last_speed[pid] = 2
        a._speed_accum[pid] = 0.25
        a.cell_facing_vec[pid] = (-1.0, 0.2)
        a._cell_target[pid] = 100.0
    a.halted_cells = set(ids)
    a.merged_cells = set(ids[:1])
    a.discipline = 1                       # force drift: below MIN_DISCIPLINE['Arrowhead']
    return u, a, set(ids)


def test_drift_leaves_no_container_holding_a_dead_id():
    u, a, old_ids = _drifting_subunit()
    u.check_drift()
    assert a.shape == 'Line', "precondition: the fixture must actually drift"
    live = set(a.cell_troops)
    assert live and live != old_ids, "precondition: drift must change the id set"
    for name in _REKEYED:
        held = set(getattr(a, name, {}) or {})
        assert not (held - live), (
            f"{name} still holds {sorted(held - live)} after drift — the exact defect this exists "
            f"to prevent (a stale id means every lookup on a LIVE id falls through to a default)")


def test_displacement_is_preserved_not_reset_to_spawn():
    """The defect the audit missed. `.get(pid, 0)` puts a drifted body back at its spawn row."""
    u, a, _ = _drifting_subunit()
    before_mean = sum(a.cell_offsets.values()) / len(a.cell_offsets)
    assert before_mean > 0, "precondition: the body must have advanced"
    u.check_drift()
    after = list(a.cell_offsets.values())
    assert after and all(v == pytest.approx(before_mean) for v in after), (
        f"displacement lost: expected every new id at the body mean {before_mean}, got {after[:4]}")


def test_committed_facing_survives_a_reformation():
    """`_rekey_node_state`'s own rule, applied on the grid path: reorganizing is not re-facing."""
    u, a, _ = _drifting_subunit()
    u.check_drift()
    assert a.cell_facing_vec, "facing must not be emptied"
    fr, fc = next(iter(a.cell_facing_vec.values()))
    assert fc != 0.0, (
        "facing collapsed to the (advance_dir, 0) default — the committed lateral component was "
        "discarded, which is the silent reset this fix exists to stop")
    assert (fr * fr + fc * fc) == pytest.approx(1.0), "facing must stay a unit vector"


def test_transient_state_is_cleared_rather_than_carried():
    u, a, _ = _drifting_subunit()
    u.check_drift()
    assert a.halted_cells == set()
    assert a.merged_cells == set()
    assert a.cell_last_speed == {}
    assert a._speed_accum == {}


def test_ruling_deferred_maps_are_untouched_and_that_is_deliberate():
    """A guard on a NON-action, because silence would otherwise read as an oversight.

    If someone later re-keys cell_morale/cell_breakpoint without a ruling, this fails and points at
    the fork rather than letting a quiet design decision ship.
    """
    u, a, _ = _drifting_subunit()
    for name in _RULING_DEFERRED:
        setattr(a, name, {pid: 1.0 for pid in a.cell_troops})
    before = {n: dict(getattr(a, n)) for n in _RULING_DEFERRED}
    u.check_drift()
    for name in _RULING_DEFERRED:
        assert getattr(a, name) == before[name], (
            f"{name} was re-keyed by drift. Its policy is a §6-class RULING (mean vs troop-weighted "
            f"morale; redraw vs inherit for a drawn breakpoint), not a derivation — take it to the "
            f"fork, do not decide it in a refactor")
