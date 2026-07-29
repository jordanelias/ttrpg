"""[ED-MB-0042 sweep] Every absolute morale write must reach the cells.

This module exists because of a specific failure, and its job is to make that failure unrepeatable.

`eff_morale` reads the CELLS the moment they are seeded and never falls back to the scalar. So every
site that assigned `.morale` directly became a **silent no-op** under `PC_CELL_MORALE` — including
`between_turn_recovery` and `reset_morale_between_battles`. That is what confounded the flag's first
measurement: its ON arm fought with morale it could never recover, so "the loser breaks earlier" was
indistinguishable from "the loser never recovers", and the flip was retracted.

The deeper failure was the UNIT OF REPAIR. `erode_morale` had exactly this defect, was fixed as a single
instance, and the pattern was never swept — so the next writer reintroduced it within hours. Hence:

  * one owner for an absolute write (`set_morale`) and one for a relative write (`erode_morale` /
    `pull_morale`), and
  * `test_no_bare_morale_assignment_on_the_engine_path`, which fails when a NEW bare assignment appears.

Every test here runs with cells seeded explicitly, so it is meaningful whichever way the flag's default
points.
"""
import os
import pathlib
import re
import sys

import pytest

_SIM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

import mass_battle.orchestration as O  # noqa: E402
from mass_battle.engine import build_army  # noqa: E402


def _own_morale_unit():
    """A subunit carrying its OWN morale (`Subunit.morale is not None`), the gauge-body path.

    [ED-MB-0045 A4b, corrected 2026-07-29] This used to call `build_unit`, on the stated belief that
    "build_unit passes morale explicitly -> the subunit carries its OWN morale". **It does not.**
    `engine.build_unit` (engine.py:204-210) passes `morale=` to the **Unit** and constructs its
    `Subunit(...)` with no morale at all, so `su.morale` measured `None` — i.e. BOTH fixture params
    were exercising the *inheriting* branch and the own-morale branch had zero coverage here, while
    `build_army` (engine.py:344-347, `if kw.get('morale') is None: kw['morale'] = morale`, the DG-4
    per-subunit-morale ruling) puts every gauge body on it. Mirroring `build_army` is therefore not a
    contrivance: it is how every real multi-subunit army in this engine is built.
    """
    u = build_army([{'shape': 'Line', 'tier': 3}], 'A', 'A', anchor_col=20)
    su = u.subunits[0]
    assert su.morale is not None, \
        "fixture precondition: the 'own' param must exercise Subunit.morale is not None, not inheritance"
    su.seed_cell_morale()
    return u, su


def _inheriting_unit():
    """Subunit-then-Unit with morale=None -> the subunit INHERITS, and is seeded by Unit.__post_init__."""
    su = O.Subunit(shape='Line', troop_type='infantry', tier=2,
                   starting_position=(25, 12), advance_dir=-1)
    u = O.Unit(name='B', faction='B', power=4, command=4, discipline=5, discipline_start=5,
               morale=6, morale_start=6, subunits=[su], dr=1)
    assert su.morale is None, \
        "fixture precondition: the 'inheriting' param must exercise Subunit.morale is None"
    su.seed_cell_morale()
    return u, su


@pytest.fixture(params=['own', 'inheriting'])
def unit_and_atom(request):
    """Both ownership kinds — and each param now asserts WHICH branch it is on, because until
    2026-07-29 neither did and the 'own' param was silently a second copy of the inheriting one (see
    `_own_morale_unit`). The original defect hid in the inheriting branch, and a fixture that only
    built inheriting bodies would have missed it — which is exactly what happened, twice: once in the
    defect, and once in the fixture written to prevent it."""
    return _own_morale_unit() if request.param == 'own' else _inheriting_unit()


# ── the writes that were silently doing nothing ─────────────────────────────────────────────────

def test_battle_reset_restores_a_damaged_body(unit_and_atom):
    """`reset_morale_between_battles` is a genuine absolute: back to the nominal start, cells included."""
    u, a = unit_and_atom
    a.erode_morale(4.0)
    assert a.eff_morale == pytest.approx(2.0), "precondition: the body is damaged"
    O.reset_morale_between_battles(u)
    assert a.eff_morale == pytest.approx(a.eff_morale_start), \
        "a battle reset that cannot reach the cells leaves the body permanently shaken"


def test_between_turn_recovery_does_not_re_inflate_a_damaged_body(unit_and_atom):
    """The mirror hazard, and a defect I introduced while fixing the first one.

    Recovery is a bounded INCREMENT, not an absolute statement about the body. The unit-level morale
    pool goes STALE once cells own the state (erosion writes the cells and never updates the pool), so
    broadcasting that pool downward restores a damaged body to full strength. My first sweep did exactly
    that: a body knocked to 2.0 came back at 6.0 with the recovery constant set to 0.
    """
    u, a = unit_and_atom
    a.erode_morale(4.0)
    before = a.eff_morale
    O.between_turn_recovery(u)
    expected = min(a.eff_morale_start, before + O.BETWEEN_TURN_MORALE_RECOVERY)
    assert a.eff_morale == pytest.approx(expected), \
        f"recovery moved morale {before} -> {a.eff_morale}, expected {expected}"


def test_a_body_wide_hit_reaches_the_cells(unit_and_atom):
    """`cascade_morale_hit` was the third writer in the same family."""
    u, a = unit_and_atom
    before = a.eff_morale
    u.cascade_morale_hit(0.5)
    assert a.eff_morale == pytest.approx(before - 0.5), \
        "an army-wide contagion hit must move a cellular body by exactly its amount"


def test_unit_level_absolute_write_reaches_an_inheriting_body():
    """`Unit.set_morale` is what the Command=0 instant-rout depends on. If it cannot reach the cells the
    body reads as unshaken and never routs."""
    u, a = _inheriting_unit()
    u.set_morale(0.0)
    assert a.eff_morale == pytest.approx(0.0)


def test_subunit_absolute_write_reaches_the_cells(unit_and_atom):
    _, a = unit_and_atom
    a.set_morale(3.0)
    assert a.eff_morale == pytest.approx(3.0)
    assert all(m == pytest.approx(3.0) for m in a.cell_morale.values()), \
        "an absolute write is a body-wide statement — no cell may keep a stale value"


# ── the guard that makes the sweep durable ──────────────────────────────────────────────────────

_ENGINE_FILES = ['orchestration.py', 'core/state.py', 'core/exchange.py', 'hierarchy/units.py',
                 'percell.py', 'resolution.py']

# DELIBERATELY OUT OF SCOPE, and the reason is a rule rather than an oversight. `lanchester_signature.py`
# and `test_persubunit_stress.py` are measurement HARNESSES, not the engine path, and each contains one
# bare morale write. Both were swept in a first pass and then REVERTED: the anti-fabrication gate scans
# the changeset, so touching either file dragged ~100 pre-existing uncited constants (none of them mine)
# into a blocking gate. Widening a sweep past what the current task needs has a real cost, and that was
# it. They are recorded on the re-flip checklist in HANDOFF_MB instead, where they belong — under
# PC_CELL_MORALE=OFF they are inert, and they must be swept BEFORE the flag flips, because
# lanchester_signature pins morale high specifically to DISABLE rout: a silent no-op there would let
# bodies rout mid-signature and measure the Lanchester exponent on truncated battles.

# [ED-MB-0042] Field-parameterized ON PURPOSE. Jordan's directive moves stamina, discipline, quality,
# hp and armour onto the cell in phases 3 and 4, and EACH of them acquires this identical hazard the
# moment `eff_<field>` starts reading cells: every existing `.<field> =` in the engine silently stops
# working. Adding the field's name here is the whole of inheriting this guard — the alternative is
# re-deriving the same defect once per field, which is precisely the mistake (fixing an instance
# instead of the pattern) that caused the retraction this module exists to prevent.
#
# `allowed` holds the assignments that are CORRECT as bare writes, each with a stated reason. Anything
# not listed is a new bare write and fails, so adding one has to be a deliberate, annotated act.
_CELL_OWNED = {
    'morale': {
        'owners': 'set_morale (absolute) or erode_morale/pull_morale (relative)',
        'allowed': {
            # units.py: the unseeded fallback branches of erode_morale / pull_morale. Both `return`
            # before these lines whenever cells exist, so they are the scalar path by construction.
            'self.morale = new',
            'u.morale = new',
            # units.py: the owners themselves.
            'self.morale = value',
            'self.morale -= amount',
            # orchestration.py between_turn_recovery: the vestigial unit pool, kept current for the
            # unseeded path. Deliberately NOT broadcast downward — recovery is a bounded increment and
            # the pool is stale once cells own the state; see
            # test_between_turn_recovery_does_not_re_inflate_a_damaged_body.
            'unit.morale = min(unit.morale_start, unit.morale + BETWEEN_TURN_MORALE_RECOVERY)',
            # core/state.py: materializes the scalar so the stochastic-rout punch is local to one
            # subunit. The cells already hold this value; rewriting them would flatten genuine
            # per-cell divergence.
            'atom.morale = atom.eff_morale',
        },
    },
    # phase 3 adds: 'stamina', 'discipline', 'quality'   ← add the key when its cell_<field> is seeded
    # phase 4 adds: 'hp', 'armour'
}


def _assign_re(field):
    return re.compile(r'^\s*(?:if [^:]+:\s*)?([A-Za-z_][\w.]*\.' + field + r'\s*(?:=|-=|\+=)[^=].*?)\s*(?:#.*)?$')


@pytest.mark.parametrize('field', sorted(_CELL_OWNED))
def test_no_bare_assignment_to_a_cell_owned_field_on_the_engine_path(field):
    """A new bare `.<field> =` on the engine path is the defect that caused the retraction. Fail on it.

    A text guard is ordinarily a poor kind of test. It earns its place here because the failure mode is
    precisely *a write that looks correct and does nothing* — which no behavioural test catches until
    someone thinks to write one for that exact site. The sweep found five sites; nothing would have
    caught the sixth. The guard re-runs forever, which is also what makes grep's incompleteness
    (dynamic access, duck-typed doubles) tolerable rather than disqualifying.
    """
    spec = _CELL_OWNED[field]
    pattern = _assign_re(field)
    root = pathlib.Path(_SIM) / 'mass_battle'
    offenders = []
    for rel in _ENGINE_FILES:
        for n, line in enumerate((root / rel).read_text().splitlines(), 1):
            if line.lstrip().startswith('#'):
                continue
            m = pattern.match(line)
            if m and m.group(1).strip() not in spec['allowed']:
                offenders.append(f"{rel}:{n}: {m.group(1).strip()}")
    assert not offenders, (
        f"bare `{field}` assignment(s) on the engine path — route through {spec['owners']}, "
        f"or add to _CELL_OWNED['{field}']['allowed'] with the reason:\n  " + "\n  ".join(offenders))


def test_the_guard_itself_can_fail():
    """A guard that cannot fail is worse than no guard: it reports safety it does not provide.

    Verified by construction rather than by trust — the regex is run against a synthetic line that
    MUST be flagged. When phase 3 adds a field to _CELL_OWNED, this proves the new pattern is live
    without needing anyone to plant a real write and remember to remove it.
    """
    for field in _CELL_OWNED:
        planted = f"    atom.{field} = 1.0"
        m = _assign_re(field).match(planted)
        assert m, f"the guard for '{field}' would not flag a plain bare assignment"
        assert m.group(1).strip() not in _CELL_OWNED[field]['allowed'], \
            f"'{field}' exempts the very shape it is meant to catch"
