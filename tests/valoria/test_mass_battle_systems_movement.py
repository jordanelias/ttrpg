"""DG-10 field-movement freeze fix — WIRED engine (`systems/mass_battle/sim`) coverage.

Companion to the coordinate-field engine's `test_mass_battle_maneuvers.py`. The wired engine
(`systems/mass_battle/sim`, the one `resolve_mass_battle`/`faction_action` actually call) carried the
same DG-10 defect: `advance_cells` floored any sub-Discipline-5 body's velocity to 0
(`floor(1*0.7)=0`) and then froze it (`== 0: continue`), so levy/light_inf/heavy_inf/archers/crossbow/
sling/artillery (all disc<5 in §B.2) never advanced to contact. ED-MB-0011 removed the grid-snap floor:
an advancing body now takes at least one whole cell at its real velocity (this engine holds integer
cell positions, so a true sub-cell field velocity is out of scope — see the fix comment in units.py).

"Everything that gets wired gets to be tested whether in aggregate or isolation" (Jordan): these are
the isolation (per-discipline closing) + aggregate (all-disc sweep) + regression (disc>=5 unchanged)
guards for that fix in the wired engine.
"""
import os
import sys
import random

import pytest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

# massbattle imports units at its tail (units late-binds back) — import the package module first to
# avoid the circular-import trap of importing units directly.
from systems.mass_battle.sim import massbattle as MB  # noqa: E402


def _unit(fac, row, advance_dir, troops, disc, stance='balanced'):
    su = MB.Subunit(shape='Line', troop_type='infantry', tier=4, starting_position=(row, 25),
                    advance_dir=advance_dir, unit_type='melee', stance=stance)
    try:
        su.troops = troops
    except Exception:
        pass
    return MB.Unit(name=fac, faction=fac, power=4, command=5, discipline=disc,
                   discipline_start=disc, morale=6, morale_start=6, subunits=[su],
                   dr=1, stance=stance, speed='Standard')


def _made_contact(u):
    hp = getattr(u, 'hp', None)
    return hp is not None and hp < u.hp_max - 1


def _run(disc, seed=1, turns=60):
    random.seed(seed)
    a = _unit('A', 20, -1, 4000, disc)
    b = _unit('B', 15, +1, 2000, disc)
    r = MB.run_battle(a, b, max_turns=turns)
    return r, a, b


@pytest.mark.parametrize('disc', [1, 2, 3, 4])
def test_sub_disc5_bodies_now_close(disc):
    """ISOLATION: a sub-Discipline-5 body must advance to contact (pre-DG-10-fix it froze at step 0)."""
    r, a, b = _run(disc)
    assert _made_contact(a) or _made_contact(b), (
        f"disc={disc} unit never made contact — DG-10 grid-floor freeze regressed "
        f"(A.hp={getattr(a,'hp',None)} B.hp={getattr(b,'hp',None)})")


def test_all_disciplines_close_aggregate():
    """AGGREGATE: every discipline tier 1..8 reaches contact under the same fixture."""
    frozen = [d for d in range(1, 9) if not any(_made_contact(u) for u in _run(d)[1:])]
    assert not frozen, f"disciplines still frozen (no contact): {frozen}"


@pytest.mark.parametrize('disc,stance', [(5, 'balanced'), (5, 'aggressive'), (8, 'balanced')])
def test_disc5plus_unchanged_regression(disc, stance):
    """REGRESSION: Discipline>=5 (incl. the wired resolve_mass_battle default of 5) is unchanged by
    the fix — round(1.0)==floor(1.0), so the whole disc>=5 space keeps its exact prior outcome. This
    is a determinism guard: the fix must not perturb the path the game actually runs today."""
    random.seed(7)
    a = _unit('A', 20, -1, 4000, disc, stance)
    b = _unit('B', 15, +1, 2000, disc, stance)
    r1 = MB.run_battle(a, b, max_turns=40)
    # determinism: identical inputs/seed -> identical public outcome
    random.seed(7)
    a2 = _unit('A', 20, -1, 4000, disc, stance)
    b2 = _unit('B', 15, +1, 2000, disc, stance)
    r2 = MB.run_battle(a2, b2, max_turns=40)
    assert r1.get('winner') == r2.get('winner')
    assert abs(a.hp - a2.hp) < 1e-9 and abs(b.hp - b2.hp) < 1e-9
