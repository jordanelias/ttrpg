"""P-DEC-3 (ED-MB-0021): per-troop-type density cap — a mounted cell holds fewer troops, so cavalry
deploys over more cells (wider frontage) than the same infantry count. Ratified MECHANISM; the cavalry
cap VALUE is a calibration, so it ships GATED OFF (byte-exact) — asserted here."""
import importlib
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'sim'))

import pytest  # noqa: E402


def _reload(on):
    os.environ['PC_TROOP_DENSITY_CAP'] = '1' if on else '0'
    import mass_battle.config as C
    importlib.reload(C)
    import mass_battle.geometry as G
    importlib.reload(G)
    return C, G


def test_off_is_byte_exact_default():
    """DEFAULT (toggle OFF): cell_cap_for is CELL_CAP for every type -> footprints identical to pre-P-DEC-3
    -> byte-exact. A cavalry footprint equals the same infantry footprint."""
    C, G = _reload(on=False)
    assert C.cell_cap_for('cavalry') == C.CELL_CAP
    assert C.cell_cap_for('heavy_infantry') == C.CELL_CAP
    inf = G.footprint_for('Line', 1200, 200, 'heavy_infantry')
    cav = G.footprint_for('Line', 1200, 200, 'cavalry')
    assert len(cav) == len(inf), "OFF: cavalry footprint must equal infantry (byte-exact)"


def test_on_caps_mounted_types_lower():
    """ON: mounted types cap at half infantry density; foot types keep CELL_CAP."""
    C, _ = _reload(on=True)
    for mounted in ('cavalry', 'knights_templar', 'mounted_archers'):
        assert C.cell_cap_for(mounted) < C.CELL_CAP, f"{mounted} should cap below CELL_CAP"
        assert C.cell_cap_for(mounted) == C.TROOP_TYPE_DENSITY_CAP[mounted]
    for foot in ('heavy_infantry', 'levy', 'pike', 'archers'):
        assert C.cell_cap_for(foot) == C.CELL_CAP, f"{foot} keeps the full cap"


def test_on_cavalry_deploys_wider():
    """ON: at a density that would pack infantry tight, cavalry needs MORE cells (fewer horses/cell) ->
    a wider frontage for the same troop count."""
    _, G = _reload(on=True)
    inf = G.footprint_for('Line', 1200, 200, 'heavy_infantry')
    cav = G.footprint_for('Line', 1200, 200, 'cavalry')
    assert len(cav) > len(inf), f"cavalry ({len(cav)}) must deploy over more cells than infantry ({len(inf)})"


def test_on_none_troop_type_uses_full_cap():
    """A None troop_type (unspecified) keeps CELL_CAP even with the toggle on -> no accidental cap."""
    C, G = _reload(on=True)
    assert C.cell_cap_for(None) == C.CELL_CAP
    a = G.footprint_for('Line', 1200, 200, None)
    b = G.footprint_for('Line', 1200, 200, 'heavy_infantry')
    assert len(a) == len(b)


def teardown_module(module):
    os.environ.pop('PC_TROOP_DENSITY_CAP', None)
    import mass_battle.config as C
    importlib.reload(C)
    import mass_battle.geometry as G
    importlib.reload(G)
