"""Edge-count primitive — per-element edges={sides∈{0,1,2}, false_edge_frac} (U3 / ED-PC-0018).

consolidation_v1.md §2.1-2.3. A physical/attested blade fact landed as data (like edge_undulation), read by three
pure functions, each wired into ONE channel (no double-counts): edge_lines→legibility (read-difficulty), spine→
bind_sigma (spine-press), grab_hazard→contact.grab_sigma (grab-resist). All three downstream constants are K=0 until
the U9 recalibration, so the increment lands byte-identical. These tests pin (1) the reader FORMULAE, (2) the K=0
byte-identity guarantee, (3) the authored data's CI invariants, and (4) the grounded ordering of known blades.
"""
import os
import sys

import pytest

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)
pytest.importorskip("numpy")

import weapon_physics as WP  # noqa: E402
from combatant import WEAPONS  # noqa: E402
from config import CFG  # noqa: E402


def _w(*edge_dicts):
    """A minimal weapon dict carrying only blade elements with the given edges descriptors."""
    return {'elements': [{'edges': ed} for ed in edge_dicts]}


def test_reader_formulae():
    """The three readers compute the §2.3 formulae per element and MAX over blade elements."""
    double = {'sides': 2, 'false_edge_frac': 0.0}
    single = {'sides': 1, 'false_edge_frac': 0.0}
    clipped = {'sides': 1, 'false_edge_frac': 0.2}
    edgeless = {'sides': 0, 'false_edge_frac': 0.0}
    # edge_lines: double=1.0, clipped=false_frac, plain single=0, edgeless=0
    assert WP.edge_lines(_w(double)) == 1.0
    assert WP.edge_lines(_w(clipped)) == pytest.approx(0.2)
    assert WP.edge_lines(_w(single)) == 0.0
    assert WP.edge_lines(_w(edgeless)) == 0.0
    # spine: single=(1-false), double=0, edgeless=0
    assert WP.spine(_w(single)) == 1.0
    assert WP.spine(_w(clipped)) == pytest.approx(0.8)
    assert WP.spine(_w(double)) == 0.0
    assert WP.spine(_w(edgeless)) == 0.0
    # grab_hazard: (sides + single*false)/2 -> edgeless 0, plain single .5, clipped .6, double 1.0
    assert WP.grab_hazard(_w(edgeless)) == 0.0
    assert WP.grab_hazard(_w(single)) == 0.5
    assert WP.grab_hazard(_w(clipped)) == pytest.approx(0.6)
    assert WP.grab_hazard(_w(double)) == 1.0
    # MAX over elements (a composite point+blade takes the most extreme)
    assert WP.edge_lines(_w(single, double)) == 1.0
    # no edges data at all -> 0 (byte-identical default)
    assert WP.edge_lines({'elements': [{}]}) == 0.0 and WP.spine({}) == 0.0 and WP.grab_hazard({}) == 0.0


def test_k_zero_byte_identical():
    """The byte-identity guarantee: every edge-effect constant is 0.0 at landing, so the readers cannot move any
    outcome until the U9 recalibration flips them (ablation-gated)."""
    assert CFG['LEGIB_EDGELINE_K'] == 0.0
    assert CFG['BIND_SPINE_K'] == 0.0
    assert CFG['GRAB_EDGE_K'] == 0.0


def test_authored_data_conforms_invariants():
    """Every non-base weapon's authored edges satisfy the two CI invariants (§2.1 V14):
    (1) sides==0 ⇒ edge_keenness ≤ 0.1 (only genuinely edgeless elements are edgeless);
    (2) false_edge_frac>0 ⇒ sides==1 (a false/back edge exists only on a single-edged blade).
    The ek check uses the ELEMENT's own edge_keenness — for a single-element weapon that is the top-level
    geometry.edge_keenness; a MULTI-element composite's per-element ek lives in its mode_elements (a blended
    top-level ek would give a false answer — the edges_data_v1.md conflicts table documents each composite spike's
    own ≤0.1 mode-ek), so the ek check is applied only where the top-level value IS the element's. Invariant (2)
    needs no ek and is checked for every weapon."""
    for n, w in WEAPONS.items():
        if 'base' in w:
            continue
        single = len(w.get('elements', ())) == 1
        ek = w.get('geometry', {}).get('edge_keenness', 0.0)
        for e in w.get('elements', ()):
            ed = e.get('edges')
            if ed is None:
                continue
            sides = ed.get('sides')
            fef = ed.get('false_edge_frac', 0.0)
            assert sides in (0, 1, 2), (n, ed)
            if sides == 0 and single:
                assert ek <= 0.1 + 1e-9, f"{n}: sides==0 but edge_keenness {ek} > 0.1"
            if fef > 0:
                assert sides == 1, f"{n}: false_edge_frac {fef} > 0 but sides {sides} != 1"


def test_grounded_ordering_of_known_blades():
    """The authored data reproduces uncontested historical morphology: double-edged straight swords carry the full
    edge_lines return-ambiguity and no spine; single-edged blades carry a spine and half grab-hazard; the edgeless
    estoc carries none of the three."""
    # double-edged knightly swords: edge_lines 1.0 (return-cut ambiguity), spine 0 (no spine), grab_hazard 1.0
    for n in ('arming', 'longsword'):
        assert WP.edge_lines(WEAPONS[n]) == 1.0, n
        assert WP.spine(WEAPONS[n]) == 0.0, n
        assert WP.grab_hazard(WEAPONS[n]) == 1.0, n
    # single-edged blades: a real spine (>0), grab_hazard in [0.5, ~0.6]
    for n in ('katana', 'sabre', 'falchion'):
        assert WP.spine(WEAPONS[n]) > 0.0, n
        assert 0.5 <= WP.grab_hazard(WEAPONS[n]) <= 0.65, n
    # the edgeless estoc: none of the three (a needle armoured-thruster has no cutting edge)
    assert WP.edge_lines(WEAPONS['estoc']) == 0.0
    assert WP.spine(WEAPONS['estoc']) == 0.0
    assert WP.grab_hazard(WEAPONS['estoc']) == 0.0
