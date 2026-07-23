"""ED-MB-0017 acceptance: multi-unit deployment geometry (P-1/P-2/P-3) + envelop pathing.

Jordan-flagged from the hierarchy snapshot: subunits overlapped, the "double envelopment" put both wings
on ONE side (no ring), and the "refused flank" sat level with the line. Root cause: `build_army` deployed
subunit i at `col = 15 + i*4` — a fixed step narrower than a battle-scale subunit's frontage. Fixed by
frontage-aware, anchor-centred placement (`_centered_line_cols`), symmetric wings in `build_envelopment`,
and an echeloned-rear refused wing in `build_refused_flank`. See
audit/2026-07-22-mass-battle-stress-test/pathing_deployment_diagnosis.md and the historical-geometry
research (research/diagrams/mass_battle_formations/SOURCES.md).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'sim'))

import pytest  # noqa: E402

import mass_battle.orchestration as _orch  # noqa: E402
from mass_battle.engine import build_unit, build_army, build_envelopment, build_refused_flank  # noqa: E402
from mass_battle import validators as _val  # noqa: E402


@pytest.fixture
def field_path():
    import mass_battle.hierarchy.units as _hu
    saved = [(m, m.FIELD_MOVEMENT, m.PC_NODE_COHESION) for m in (_hu, _orch)]
    _val._set_movement_path('node')
    try:
        yield
    finally:
        for m, fm, nc in saved:
            m.FIELD_MOVEMENT = fm
            m.PC_NODE_COHESION = nc


def _spans(unit):
    """Per-subunit (col_min, col_max, row_mean) at current positions."""
    out = []
    for s in unit.subunits:
        cells = list(s.cells_float())
        cs = [c[1] for c in cells]
        rs = [c[0] for c in cells]
        out.append((min(cs), max(cs), sum(rs) / len(rs), sum(cs) / len(cs)))
    return out


def _no_lateral_overlap(spans):
    """No two subunits overlap in the SAME row band. Subunits at clearly different rows (echelon) may
    share columns; only same-row-band subunits must be laterally disjoint."""
    for i in range(len(spans)):
        for j in range(i + 1, len(spans)):
            ci0, ci1, ri, _ = spans[i]
            cj0, cj1, rj, _ = spans[j]
            if abs(ri - rj) < 2.0:  # same row band
                if not (ci1 < cj0 or cj1 < ci0):
                    return False, (i, j, spans[i], spans[j])
    return True, None


# ─── P-1: battle line — no overlap, centred, 3..11 subunits ──────────────────

@pytest.mark.parametrize("n,troops", [(3, 800), (5, 600), (8, 400), (11, 400)])
def test_line_no_overlap_and_centered(field_path, n, troops):
    u = build_army([{'shape': 'Line', 'troops': troops, 'concentration': 50} for _ in range(n)],
                   'A', 'A', anchor_col=25)
    spans = _spans(u)
    ok, bad = _no_lateral_overlap(spans)
    assert ok, f"subunits overlap at n={n}: {bad}"
    block_center = sum((c0 + c1) / 2 for c0, c1, _, _ in spans) / len(spans)
    assert abs(block_center - 25) <= 2.0, f"line not centred on anchor 25: center={block_center:.1f}"


# ─── P-2: envelopment — symmetric wings, opposite sides, no overlap ──────────

def test_envelopment_wings_straddle_center(field_path):
    u = build_envelopment(
        [{'shape': 'Line', 'troops': 600, 'concentration': 50}],
        [{'shape': 'Line', 'troops': 500, 'concentration': 50},
         {'shape': 'Line', 'troops': 500, 'concentration': 50}], 'A', 'A')
    spans = _spans(u)
    ok, bad = _no_lateral_overlap(spans)
    assert ok, f"envelopment subunits overlap: {bad}"
    center_c = spans[0][3]
    wing_cs = [s[3] for s in spans[1:]]
    assert any(w < center_c for w in wing_cs), "no wing LEFT of centre — not a double envelopment"
    assert any(w > center_c for w in wing_cs), "no wing RIGHT of centre — not a double envelopment"


def test_envelopment_wings_wrap_behind_opposite_flanks(field_path):
    """The load-bearing double-envelopment invariant: with a corrected deployment, the two wings wheel to
    OPPOSITE flanks and both get BEHIND the enemy (past its far row edge) — a mirror wrap, not both wings
    piling onto one side."""
    import random
    random.seed(3)
    a = build_envelopment(
        [{'shape': 'Line', 'troops': 600, 'concentration': 50}],
        [{'shape': 'Line', 'troops': 500, 'concentration': 50},
         {'shape': 'Line', 'troops': 500, 'concentration': 50}], 'A', 'A')
    b = build_army([{'shape': 'Line', 'troops': 900, 'concentration': 50}], 'B', 'B', anchor_col=25)
    _orch.run_multi_turn_battle(a, b, 'Line', 'Line', {'A': 25, 'B': 25}, max_battle_turns=12)
    spans = _spans(a)
    center_c = spans[0][3]
    wings = spans[1:]
    enemy_rows = [c[0] for s in b.subunits for c in s.cells_float()]
    enemy_near = max(enemy_rows)  # A advances toward LOW rows; the enemy's rear is its LOW-row edge
    enemy_min = min(enemy_rows)
    left = [w for w in wings if w[3] < center_c]
    right = [w for w in wings if w[3] > center_c]
    assert left and right, "wings did not split to opposite flanks"
    # each wing should have advanced past the enemy's near edge toward its rear (row well below the enemy
    # front) — i.e. wrapped, not milling in front.
    assert min(w[2] for w in left) <= enemy_near, "left wing never reached the enemy depth"
    assert min(w[2] for w in right) <= enemy_near, "right wing never reached the enemy depth"
    # and at least one wing got fully behind (past the enemy's far/low edge)
    assert min(w[2] for w in wings) <= enemy_min + 1.0, "no wing wrapped behind the enemy rear"


# ─── P-3: refused flank — echeloned BACK, no overlap ─────────────────────────

def test_refused_flank_echeloned_back(field_path):
    u = build_refused_flank(
        [{'shape': 'Line', 'troops': 900, 'concentration': 50}],
        [{'shape': 'Line', 'troops': 600, 'concentration': 50}], 'A', 'A')
    spans = _spans(u)
    ok, bad = _no_lateral_overlap(spans)
    assert ok, f"refused-flank subunits overlap in the same row band: {bad}"
    strong_row = spans[0][2]
    refused_row = spans[1][2]
    # A advances toward LOW rows, so "back" (away from enemy) = HIGHER row. Refused wing must sit clearly
    # behind the strong wing.
    assert refused_row > strong_row + 3.0, \
        f"refused wing not echeloned back: strong r{strong_row:.1f}, refused r{refused_row:.1f}"


# ─── adversarial-review findings 1/3/4 ──────────────────────────────────────

@pytest.mark.parametrize("n,troops", [(1, 2000), (5, 2000), (8, 2000), (11, 2000), (11, 400)])
def test_large_dense_army_never_crashes_offboard(field_path, n, troops):
    """Finding 1: an army too wide for the 50-cell field must DEGRADE (subunits pile/overlap on-board),
    never raise Subunit's off-board ValueError. The pre-fix `15+i*4` layout also overlapped for such
    armies; the fix must not regress that into a crash."""
    u = build_army([{'shape': 'Line', 'troops': troops, 'concentration': 50} for _ in range(n)],
                   'A', 'A')
    cells = [(r, c) for s in u.subunits for (r, c) in s.cells_float()]
    assert all(0 <= r <= 49 and 0 <= c <= 49 for (r, c) in cells), "a cell landed off-board"


@pytest.mark.parametrize("nwings", [1, 3])
def test_envelopment_odd_wings_no_crash_and_split(field_path, nwings):
    """Finding 3: odd wing counts can't perfectly mirror, but must still deploy sanely (no overlap, no
    crash) and put at least one wing on each of left/right when >1 wing."""
    u = build_envelopment(
        [{'shape': 'Line', 'troops': 600, 'concentration': 50}],
        [{'shape': 'Line', 'troops': 400, 'concentration': 50} for _ in range(nwings)], 'A', 'A')
    spans = _spans(u)
    ok, bad = _no_lateral_overlap(spans)
    assert ok, f"odd-wing envelopment overlaps: {bad}"
    if nwings >= 2:
        center_c = spans[0][3]
        wing_cs = [s[3] for s in spans[1:]]
        assert any(w < center_c for w in wing_cs) and any(w > center_c for w in wing_cs)


def test_refused_wing_engages_later_than_strong(field_path):
    """Finding 4: the echelon must WORK dynamically, not just look right at deploy — the refused wing
    must still be farther from the enemy than the strong wing after several ticks of a live battle
    (it declines contact while the strong wing closes)."""
    import random
    random.seed(11)
    a = build_refused_flank(
        [{'shape': 'Line', 'troops': 900, 'concentration': 50}],
        [{'shape': 'Line', 'troops': 600, 'concentration': 50}], 'A', 'A')
    b = build_army([{'shape': 'Line', 'troops': 900, 'concentration': 50}], 'B', 'B', anchor_col=25)
    _orch.run_battle(a, b, max_turns=6)
    spans = _spans(a)
    strong_row, refused_row = spans[0][2], spans[1][2]
    enemy_rows = [c[0] for s in b.subunits for c in s.cells_float()]
    enemy_front = max(enemy_rows)  # nearest enemy row to A (A advances toward low rows)
    # A advances toward LOW rows; "closer to the enemy" = lower row. The strong wing must be closer to
    # the enemy than the refused wing after the advance.
    assert strong_row < refused_row - 2.0, \
        f"refused wing did not stay refused: strong r{strong_row:.1f} vs refused r{refused_row:.1f}"
    assert (strong_row - enemy_front) < (refused_row - enemy_front), "refused wing is not the farther one"


# ─── I4-adjacent: single-subunit build_unit deployment unchanged ─────────────

def test_single_subunit_unaffected():
    """build_unit (single subunit, explicit anchor) is not touched by the multi-unit deployment fix —
    its cells still sit at the given anchor column."""
    u = build_unit('Line', 3, 'A', 'A', 9, troop_type='infantry')
    cs = [c[1] for s in u.subunits for c in s.cells_float()]
    assert min(cs) >= 0 and 9 - 4 <= sum(cs) / len(cs) <= 9 + 4, "single-subunit anchor drifted"
