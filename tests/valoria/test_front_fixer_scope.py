"""[ED-MB-0041 Tier-2] The atomized fixing-force relation must be scoped to the FULL tick.

`_front_fixers` answers "is this defender pinned frontally by some enemy OTHER than the one currently
hitting it?" — the fixing-force half of envelopment (the centre holds them, the wings take them in the
flank). It used to be computed inside `resolve_engagements` off whatever pair list that call received.
Under `CASCADING_ENABLED` that list is one cascade sub-phase GROUP, not the tick, so a defender fixed
by a body in group 0 and flanked by a detachment in group 1 saw an EMPTY fixer set in group 1 and was
treated as free to wheel. The mechanism was therefore dead in exactly the geometry it exists for.

It is now computed once per tick by `resolve_engagements_cascading` and threaded into every sub-phase.
These tests pin both halves: the relation itself, and the partition-dependence that motivated the hoist.
"""
import os, sys
_SIM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

import inspect
from mass_battle.orchestration import _compute_front_fixers, resolve_engagements
from mass_battle.engine import build_army, SIDE_A_START_ROW, SIDE_B_START_ROW


def _sub(faction, row, col, advance_dir):
    """One Line subunit at (row, col) advancing along `advance_dir` (+1 = increasing row)."""
    army = build_army([{'shape': 'Line', 'troop_type': 'infantry', 'troops': 300.0,
                        'concentration': 100.0, 'starting_position': (row, col)}],
                      faction, faction)
    su = army.subunits[0]
    su.advance_dir = advance_dir
    return su


def _pair(a, b):
    return {'atom_a': a, 'atom_b': b,
            'a_cells': list(a.cells()), 'b_cells': list(b.cells())}


def _scenario():
    """Defender D faces +row. E_front sits ahead of it (GREEN arc); E_flank sits to its side.

    That is the minimal Cannae shape: one body fixes the front, a second takes the flank.
    """
    D = _sub('A', SIDE_A_START_ROW, 20, +1)
    dr, dc = D.centroid()
    E_front = _sub('B', int(round(dr)) + 6, int(round(dc)), -1)     # dead ahead of D
    E_flank = _sub('B', int(round(dr)), int(round(dc)) + 12, -1)    # off D's shoulder
    return D, E_front, E_flank


def test_frontal_contact_registers_a_fixer_and_a_flank_contact_does_not():
    """The relation itself: only an enemy in the defender's GREEN (front) arc fixes it."""
    D, E_front, E_flank = _scenario()
    ff_front = _compute_front_fixers([_pair(E_front, D)])
    ff_flank = _compute_front_fixers([_pair(E_flank, D)])
    assert id(E_front) in ff_front.get(id(D), set()), \
        "an enemy dead ahead of the defender must register as a frontal fixer"
    assert id(E_flank) not in ff_flank.get(id(D), set()), \
        "an enemy off the defender's shoulder is not in its front arc and must not fix it"


def test_fixed_by_other_is_partition_dependent_so_scope_must_be_the_whole_tick():
    """The defect: evaluate the flank pair ALONE and the defender reads as unfixed.

    `a_fixed_other` is `fixers[D] - {the atom currently hitting D}`. With only the flank pair in scope
    that set is empty (D is 'free to wheel'); with the whole tick in scope the frontal fixer is present
    and the flank hit lands with the zone penalty. Same defender, same tick — different answer purely
    from how the pairs were partitioned. That is what makes per-group computation a bug rather than an
    optimisation.
    """
    D, E_front, E_flank = _scenario()
    flank_only = _compute_front_fixers([_pair(E_flank, D)])
    whole_tick = _compute_front_fixers([_pair(E_front, D), _pair(E_flank, D)])

    fixed_group_scoped = bool(flank_only.get(id(D), set()) - {id(E_flank)})
    fixed_tick_scoped = bool(whole_tick.get(id(D), set()) - {id(E_flank)})

    assert not fixed_group_scoped, "group-scoped view loses the frontal fixer (the old behaviour)"
    assert fixed_tick_scoped, "tick-scoped view must retain the frontal fixer"


def test_resolve_engagements_accepts_a_threaded_fixer_map():
    """The hoist is only useful if the value can actually be threaded in from the tick driver."""
    assert 'front_fixers' in inspect.signature(resolve_engagements).parameters, \
        "resolve_engagements must accept the precomputed full-tick fixer map"
