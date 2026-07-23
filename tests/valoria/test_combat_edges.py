"""Edge-count primitive — per-element edges={sides∈{0,1,2}, false_edge_frac} (U3 / ED-PC-0018).

consolidation_v1.md §2.1-2.3. A physical/attested blade fact landed as data (like edge_undulation), read by three
pure functions, each wired into ONE channel (no double-counts): edge_lines→legibility (read-difficulty), spine→
bind_sigma (spine-press), grab_hazard→contact.grab_sigma (grab-resist). The three downstream constants were K=0 at
landing and were ACTIVATED to small grounded baselines in U10/ED-PC-0022 (routed through the tradition surface).
These tests pin (1) the reader FORMULAE, (2) that the constants are now active + tradition-modulable, (3) the
authored data's CI invariants, and (4) the grounded ordering of known blades.
"""
import os
import sys

import pytest

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)
pytest.importorskip("numpy")

import weapon_physics as WP  # noqa: E402
import combat_systems as S  # noqa: E402
import ability_primitives as ABIL  # noqa: E402
import tradition as TR  # noqa: E402
from combatant import WEAPONS, Combatant  # noqa: E402
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


def test_edge_levers_activated_and_grounded():
    """U10/ED-PC-0022: the three edge-effect constants are now ACTIVATED (>0) to small grounded baselines. The U9
    capstone found no lever moves aggregate FIELD winrate — correct, because flat physics cancels in a mirror-ish
    field, not evidence of inertness. Efficacy comes from the tradition-modulation surface (below)."""
    assert CFG['LEGIB_EDGELINE_K'] > 0.0
    assert CFG['BIND_SPINE_K'] > 0.0
    assert CFG['GRAB_EDGE_K'] > 0.0


def test_edge_read_lever_live_from_geometry():
    """edge_lines -> legibility is live PURELY FROM WEAPON GEOMETRY (isolated by toggling LEGIB_EDGELINE_K, so no
    cross-weapon confound): for a double-edged blade (edge_lines 1.0) the lever makes it read HARDER (lower
    legibility) than with the lever off; an edgeless weapon (edge_lines 0) is unaffected either way. edge_read is a
    BARE morphology lever — ED-PC-0026 re-homed the German zwerchhau ability off it to counter_select (its real
    function is tempo-interception, not false-edge unreadability, per the adversarial HEMA critic), leaving no
    grounded edge_read amplifier: an honest gap. The lever's liveness does not depend on any ability."""
    off = dict(CFG); off['LEGIB_EDGELINE_K'] = 0.0
    double = Combatant('A', weapon='arming')                                 # double-edged: edge_lines 1.0
    assert S.legibility(double, 3, CFG) < S.legibility(double, 3, off), \
        "the edge_read lever should make a double-edge weapon read HARDER (lower legibility) than with the lever off"
    edgeless = Combatant('A', weapon='estoc')                                # edgeless point: edge_lines 0
    assert S.legibility(edgeless, 3, CFG) == S.legibility(edgeless, 3, off), \
        "an edgeless weapon has no edge_lines -> the lever is inert on it"


def test_spine_press_lever_live_and_amplified_by_shinogi():
    """spine -> bind_sigma is live (a single-edged rigid spine wins the bind bearing-surface vs a spineless double
    edge), and the Japanese shinogi ('spine_press', grounded to the katana that actually HAS a spine) amplifies the
    wielder's own spine term. (Retag from the mis-grounded 'winden' — a double-edged LONGSWORD technique inert on the
    single-edge lever — per the ED-PC-0023 adversarial review.)"""
    katana = Combatant('A', weapon='katana')                                 # spine > 0
    katana_s = Combatant('A', weapon='katana', tradition='japanese', equipped=['shinogi'])
    arming = Combatant('B', weapon='arming')                                 # spine 0 (double-edged)
    b_plain = S.bind_sigma(katana, arming, CFG, TR)
    b_shinogi = S.bind_sigma(katana_s, arming, CFG, TR)
    assert b_plain > 0, "a single-edge rigid spine should win the bind vs a spineless double edge"
    assert b_shinogi > b_plain, "shinogi should amplify the spine-press bind edge"


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
