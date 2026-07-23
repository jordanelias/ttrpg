"""Explicit subunit deployment primitives (ED-MB-0025) — the subunit as a fully-configurable entity:
explicit placement, troop_type, troops, DENSITY (troops/cell, which bounds the cell count), and a depth
DISTRIBUTION gradient (front/rear/uniform). Plus the build_envelopment explicit-placement fix."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'sim'))

import pytest  # noqa: E402
from mass_battle.geometry import footprint_for  # noqa: E402
from mass_battle.hierarchy.units import Subunit  # noqa: E402
from mass_battle.engine import build_army, build_envelopment  # noqa: E402
from mass_battle.config import SIDE_A_START_ROW  # noqa: E402


def test_density_bounds_cell_count():
    """Explicit density (troops/cell) now truly BOUNDS cell count, for any troop count — the M2 bug
    (a 133-troop Line collapsing to 1 cell at every concentration) is fixed."""
    for troops in (133, 200, 400, 1200):
        for density in (40, 50, 67, 100):
            cells = footprint_for('Line', troops, density, None)
            per = troops / len(cells)
            # achieved per-cell density is within the [CELL_FLOOR, CELL_CAP] band and near the target
            assert 40 <= per <= 200, f"{troops}@{density}: {per:.0f}/cell out of band"
    # the specific regression: 133 troops must now spread beyond 1 cell at a low density
    assert len(footprint_for('Line', 133, 40, None)) >= 3, "133 troops @ 40/cell must span >=3 cells"


def test_density_monotonic_in_cells():
    """Lower density -> more cells (wider spread) for the same troops; higher density -> fewer."""
    sparse = len(footprint_for('Line', 400, 40, None))
    dense = len(footprint_for('Line', 400, 200, None))
    assert sparse > dense, f"lower density must use more cells ({sparse} vs {dense})"


def test_shapes_build_requested_cell_count():
    """Every shape builds ~the density-implied cell count (not a sparse fixed set)."""
    for shape in ('Line', 'Arrowhead', 'GappedLine', 'Column'):
        cells = footprint_for(shape, 400, 50, None)
        assert 6 <= len(cells) <= 10, f"{shape}: {len(cells)} cells off target ~8"


def test_gradient_front_loads_leading_ranks():
    """distribution='front' puts more troops in the leading ranks (r small); 'rear' the reverse;
    'uniform' equal. All conserve troop_count exactly."""
    from collections import defaultdict

    def rowsum(dist):
        su = Subunit(shape='Line', troop_type='infantry', tier=3, starting_position=(10, 10),
                     troops=400, concentration=50, distribution=dist)
        by = defaultdict(float)
        for (r, _c), t in su.cell_troops.items():
            by[r] += t
        assert abs(sum(su.cell_troops.values()) - 400) < 1e-6, "conservation"
        return by
    front = rowsum('front'); rear = rowsum('rear'); uni = rowsum('uniform')
    assert front[0] > front[max(front)], "front-heavy: leading rank denser than trailing"
    assert rear[0] < rear[max(rear)], "rear-heavy: trailing rank denser than leading"
    rows = sorted(uni)
    assert abs(uni[rows[0]] - uni[rows[-1]]) < 1e-6, "uniform: equal across ranks"


def test_build_envelopment_wings_flank_the_center():
    """The build_envelopment fix: with an explicitly-placed center, the wings flank it (straddle its
    column) instead of the pre-fix phantom-anchor placement that put both wings far to one side."""
    row = SIDE_A_START_ROW
    center = [{'shape': 'Line', 'troop_type': 'infantry', 'troops': 133, 'concentration': 100,
               'starting_position': (row, 11)}]
    wings = [{'shape': 'Line', 'troop_type': 'infantry', 'troops': 133, 'concentration': 100},
             {'shape': 'Line', 'troop_type': 'infantry', 'troops': 133, 'concentration': 100}]
    u = build_envelopment(center, wings, 'A', 'A')
    coms = []
    for a in u.subunits:
        cols = [c for _r, c in a.cells()]
        coms.append(sum(cols) / len(cols))
    center_com = coms[0]
    wing_coms = sorted(coms[1:])
    assert wing_coms[0] < center_com < wing_coms[1], \
        f"wings must straddle the center: wings {wing_coms}, center {center_com}"


def test_build_envelopment_honors_explicit_wing_positions():
    """Explicit-placement directive: an explicitly-placed wing keeps its column (no longer silently
    overridden by the auto flank-split)."""
    row = SIDE_A_START_ROW
    center = [{'shape': 'Line', 'troop_type': 'infantry', 'troops': 133, 'concentration': 100,
               'starting_position': (row, 11)}]
    wings = [{'shape': 'Line', 'troop_type': 'infantry', 'troops': 133, 'concentration': 100,
              'starting_position': (row, 2)},
             {'shape': 'Line', 'troop_type': 'infantry', 'troops': 133, 'concentration': 100,
              'starting_position': (row, 20)}]
    u = build_envelopment(center, wings, 'A', 'A')
    wing_cols = sorted(min(c for _r, c in a.cells()) for a in u.subunits[1:])
    assert wing_cols == [2, 20], f"explicit wing columns must be honored, got {wing_cols}"


def test_build_refused_flank_honors_strong_position():
    """build_refused_flank sibling fix: with the strong wing explicitly placed and the refused wing
    auto-placed, the refused wing sits adjacent to the strong wing's ACTUAL span (echeloned back), not
    against a phantom field-center."""
    from mass_battle.engine import build_refused_flank  # noqa: E402
    row = SIDE_A_START_ROW
    strong = [{'shape': 'Line', 'troop_type': 'infantry', 'troops': 133, 'concentration': 100,
               'starting_position': (row, 9)}]
    refused = [{'shape': 'Line', 'troop_type': 'infantry', 'troops': 133, 'concentration': 100}]
    u = build_refused_flank(strong, refused, 'A', 'A')
    strong_col = sum(c for _r, c in u.subunits[0].cells()) / len(u.subunits[0].cells())
    refused_col = sum(c for _r, c in u.subunits[1].cells()) / len(u.subunits[1].cells())
    # refused wing must be near the strong wing (to its right), not off at the phantom field-center (~26)
    assert refused_col - strong_col <= 8, \
        f"refused wing must be adjacent to the strong wing at col {strong_col:.0f}, got {refused_col:.0f}"
    # and echeloned BACK (different row from the strong wing)
    strong_row = sum(r for r, _c in u.subunits[0].cells()) / len(u.subunits[0].cells())
    refused_row = sum(r for r, _c in u.subunits[1].cells()) / len(u.subunits[1].cells())
    assert strong_row != refused_row, "refused wing must be echeloned back (different row)"
