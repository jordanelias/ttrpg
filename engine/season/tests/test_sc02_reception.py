"""v9 SC-02 `22a`, piece 1 -- proceedings PHASE 3 steps 17, 18 and 20 (`19_PLAN.md`, intent only):
`reception` (the bench's ledgers about the speaker, resolver-side), `proofs` (weighed by remove, discounted
by the mirror) and route erosion (the single called bluff, inside reception).

WHAT IS BUILT, asked of the real host builder (`seam/wrappers/sigma.py`), the real module
(`modules/social_contest/roll.py::obstacle`) and the real fold on a HAND-BUILT world (`probes.tiny_world`
through `test_u7_remit._world`: `p_high` holds `off_duke`, whose bench sits over `Hh`; the speaker `p_low`
and his party `p_mid` live in `Hh`; `p_other` lives there and sits on no bench):
  * `world_q.reception(w, speaker, venue)` -- each bench member's own deed claims about the speaker,
    weighted by `remove_weight(source)` x decayed confidence x the member's valence (arm 1, the alignment
    table; arm 2 lost the sweep, `hole_register.yaml` H-215), summed; `reception_gain` scales it into
    the obstacle (`H-215`);
  * `world_q.proofs(w, speaker, opponent)` -- the speaker's deed claims about the opponent weighed by
    remove, zero for any the opponent mirrors (same subject and predicate); `proof_step` (`H-216`);
  * route erosion -- `rosters.yaml: standing_routes`: a hearer who saw a dominance-route deed done TO the
    speaker zeroes every dominance-route deed of his no newer than it.

THE FALSIFIERS (`19_PLAN.md` :537, :550, :578), each an assertion below that observes its failure:
  * step 17: a bench's obstacle invariant under a change to a member's ledger; the Query reachable from a
    decision -- `test_sc02_17_...`;
  * step 18: the mirrored proof moves the obstacle -- `test_sc02_18_...`;
  * step 20: a called bluff leaves the weight unchanged -- `test_sc02_20_...`.
"""

from __future__ import annotations

import ast
import math
import random
from pathlib import Path

from ..data.rosters import DOMINANCE_KINDS, REMOVE_ORDINAL, SEEN_PREDICATE
from ..data import verbs as _verbs
from ..epistemic import Seen
from ..queries import person_q, world_q
from ..seam.wrappers import sigma
from ..state.carriers import Act, Claim
from .test_u7_remit import _fold, _kinds, _open, _world
from engine.substrate import composition

SPEAKER, PARTY, HEARER, NOBODY = "p_low", "p_mid", "p_high", "p_other"
PRIZE = "a matter"
SEASON_DIR = Path(__file__).resolve().parents[1]

# The pursuit the hearer is given: the tiny world's persons hold none, so every valence reads 0 and
# reception would be zero BY CONSTRUCTION -- a fake control. One pursuit makes the hearer judge.
PURSUIT = "honour"


def _claim(cid, holder, subject, kind, *, source="firsthand", chain=(), when=0, rnd=0, conf=100):
    return Claim(cid, holder, subject, kind, True, when, source, conf, "own", rnd, chain=chain)


def _seen(cid, holder, subject, who, *, when=0, rnd=0):
    stratum = _verbs.VERB_TABLE["fight"].stratum
    return Claim(cid, holder, subject, SEEN_PREDICATE, Seen(stratum=stratum, marks=(), who=who),
                 when, "firsthand", 100, "own", rnd)


def _roll_module():
    """The `social_contest` module, found the way the host finds it: by the composition row's target
    string (`engine/` never imports module code by name; `test_sc01_obstacle_ceiling.py`'s precedent)."""
    import importlib
    return importlib.import_module(composition.ROLES["social_contest.roll"]["target"].split(":", 1)[0])


def _judging_world():
    w, d = _world()
    w.persons[HEARER].pursuits = {PURSUIT: 1.0}
    assert world_q.judging_set(w, world_q.place_of(w, SPEAKER)) == [HEARER]
    return w, d


def _lean(w, kind):
    axis_w = person_q.projected_axes(w.persons[HEARER])
    return person_q.deed_valence(axis_w, _claim("probe", HEARER, SPEAKER, kind))


def _kind_with_lean(w, sign=+1, among=None):
    """The unpaired deed kind the hearer leans on hardest in `sign`'s direction (ties by name)."""
    kinds = sorted((among or _verbs.DEED_KINDS) - person_q.PAIRED_KINDS)
    best = max(kinds, key=lambda k: (sign * _lean(w, k), k))
    assert sign * _lean(w, best) > 0, f"no kind leans {sign:+d} for {PURSUIT!r}: the fixture is inert"
    return best


def _ob(w, actor=SPEAKER, subject=PARTY):
    """The composed obstacle of one `speak`'s draw, through the real adapter and module entry."""
    out = sigma.resolve(w, [actor, subject], ["root"], PRIZE, verb="speak", subject=subject,
                        rng=random.Random(0), rung=world_q.place_of(w, actor))
    assert out["status"] == "RESOLVED", out
    return out["ob"]


def _input(w, actor=SPEAKER, subject=PARTY):
    return sigma.contest_input(w, [actor, subject], verb="speak", subject=subject,
                               room=world_q.place_of(w, actor))


# ================================================================================================
# STEP 17 -- RECEPTION
# ================================================================================================

def test_sc02_17_two_benches_differing_only_in_one_ledger_band_differently_for_the_same_draw():
    """`19_PLAN.md` step 17's artifact: identical seats and convictions, one member's ledger differs, and
    the same seeded `speak` resolves at different bands. FALSIFIER: the obstacle invariant under the
    ledger change (asserted on every draw, and on the band over the sweep)."""
    plain, d_plain = _judging_world()
    heard, d_heard = _judging_world()
    kind = _kind_with_lean(heard, +1)
    n = math.ceil(1.0 / _lean(heard, kind)) + 1        # enough favour to reach the Ob floor from 2
    for i in range(n):
        heard.persons[HEARER].ledger.append(_claim(f"fav{i}", HEARER, SPEAKER, kind))
    for w, d in ((plain, d_plain), (heard, d_heard)):
        assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]
    assert world_q.reception(plain, SPEAKER, "Hh") == 0.0
    assert world_q.reception(heard, SPEAKER, "Hh") > 0.0
    assert _ob(heard) < _ob(plain), (_ob(heard), _ob(plain))
    differ = checked = 0
    for i in range(40):
        a = _fold(plain, d_plain, Act(id=f"sp{i}", actor=SPEAKER, verb="speak", payload={"subject": PARTY}))
        b = _fold(heard, d_heard, Act(id=f"sp{i}", actor=SPEAKER, verb="speak", payload={"subject": PARTY}))
        assert len(a) == len(b) == 1 and a[0].degree and b[0].degree, (_kinds(a), _kinds(b))
        differ += a[0].degree != b[0].degree
        checked += 1
    assert checked == 40
    assert differ >= 1, "no draw banded differently: the bench's ledger did not reach the outcome"


def test_sc02_17_a_ledger_off_the_bench_moves_nothing():
    """THE CONTROL: the same claims in a person who sits on no bench over `Hh` leave reception at 0 and
    the obstacle at its base, so what moved it above is the BENCH's ledger, not any ledger."""
    w, _d = _judging_world()
    w.persons[NOBODY].pursuits = {PURSUIT: 1.0}
    kind = _kind_with_lean(w, +1)
    base = _ob(w)
    for i in range(5):
        w.persons[NOBODY].ledger.append(_claim(f"off{i}", NOBODY, SPEAKER, kind))
    assert world_q.reception(w, SPEAKER, "Hh") == 0.0
    assert _ob(w) == base


def test_sc02_17_a_told_claim_moves_the_obstacle_strictly_less_than_the_same_claim_firsthand():
    """Step 17's second artifact, over the ordinal of remove: firsthand > knot-sourced > told > inferred,
    each strictly, and every rank still counts (the obstacle below the no-claim base)."""
    obs = {}
    for source in REMOVE_ORDINAL:
        w, _d = _judging_world()
        kind = _kind_with_lean(w, +1)
        chain = ("p_king",) if source == "told_by" else ()
        w.persons[HEARER].ledger.append(_claim("c1", HEARER, SPEAKER, kind, source=source, chain=chain))
        obs[source] = _ob(w)
    w0, _d = _judging_world()
    base = _ob(w0)
    ranked = [obs[s] for s in REMOVE_ORDINAL]
    assert ranked == sorted(ranked) and len(set(ranked)) == len(ranked), obs
    assert obs["firsthand"] < obs["told_by"] < base, (obs, base)


def test_sc02_17_decayed_confidence_counts_less_and_a_hostile_bench_reads_negative():
    w, _d = _judging_world()
    kind = _kind_with_lean(w, +1)
    w.persons[HEARER].ledger.append(_claim("full", HEARER, SPEAKER, kind))
    full = world_q.reception(w, SPEAKER, "Hh")
    w.persons[HEARER].ledger[-1] = _claim("half", HEARER, SPEAKER, kind, conf=50)
    assert world_q.reception(w, SPEAKER, "Hh") == full / 2
    hostile = _kind_with_lean(w, -1)
    w.persons[HEARER].ledger[-1] = _claim("bad", HEARER, SPEAKER, hostile)
    assert world_q.reception(w, SPEAKER, "Hh") < 0.0
    # Under the shipped ceiling (`H-213`, 2 = `obstacle_default`) a hostile room cannot raise the
    # obstacle; one notch up it does. Stated in `roll.obstacle`'s docstring and in H-215.
    inp = _input(w)
    obstacle = _roll_module().obstacle
    assert obstacle(inp) == inp.obstacle_ceiling
    from dataclasses import replace
    assert obstacle(replace(inp, obstacle_ceiling=3.0)) > 2.0


def test_sc02_17_reception_and_proofs_take_the_world_first_and_no_decision_module_imports_them():
    """The AST half of step 17's artifact: both Queries take `w: World` first, and no module under
    `decision/` names them or the module they live in. FALSIFIER: the Query reachable from a decision."""
    tree = ast.parse((SEASON_DIR / "queries" / "world_q.py").read_text())
    found = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in ("reception", "proofs"):
            first = node.args.args[0]
            found[node.name] = (first.arg, ast.unparse(first.annotation) if first.annotation else None)
    assert found == {"reception": ("w", "World"), "proofs": ("w", "World")}, found
    scanned = 0
    for path in sorted((SEASON_DIR / "decision").rglob("*.py")):
        mod = ast.parse(path.read_text())
        scanned += 1
        for node in ast.walk(mod):
            if isinstance(node, ast.ImportFrom):
                names = {a.name for a in node.names}
                assert "world_q" not in (node.module or "") and "world_q" not in names, path
                assert not names & {"reception", "proofs"}, path
            elif isinstance(node, ast.Import):
                assert not any("world_q" in a.name for a in node.names), path
            elif isinstance(node, ast.Attribute):
                assert node.attr not in ("reception", "proofs") or not (
                    isinstance(node.value, ast.Name) and node.value.id == "world_q"), path
    assert scanned >= 5, scanned


def test_sc02_17_only_a_prize_a_room_hears_reads_the_room():
    """`heard_by: bench` is on `a matter` alone: a `tell` (`a standing`) or an inquiry by the same actor
    at the same rung carries the record's no-room defaults, so every other social roll is as it was."""
    w, _d = _judging_world()
    kind = _kind_with_lean(w, +1)
    w.persons[HEARER].ledger.append(_claim("c1", HEARER, SPEAKER, kind))
    seen = {}
    real = sigma.contest_input

    def spy(*a, **kw):
        inp = real(*a, **kw)
        seen[kw.get("verb")] = inp
        return inp
    sigma.contest_input = spy
    try:
        for prize, verb in ((PRIZE, "speak"), ("a standing", "tell")):
            sigma.resolve(w, [SPEAKER, PARTY], ["root"], prize, verb=verb, subject=PARTY,
                          rng=random.Random(0), rung="Hh")
    finally:
        sigma.contest_input = real
    assert seen["speak"].reception > 0.0
    assert seen["tell"].reception == 0.0 and seen["tell"].reception_gain == 0.0, seen["tell"]


def test_sc02_17_a_misspelled_room_refuses_at_boot_naming_the_row(monkeypatch):
    """`heard_by:` names a room the host reads (`manifest/registry.py::HEARD_BY_ROOMS`) or the boot check
    refuses, naming the row; the shipped rows are the control."""
    from ..data.rosters import roster_map
    from ..gaps import Unspecified
    from ..manifest import registry
    import pytest
    assert registry.check_rows()                         # the control: the shipped rows pass
    row = roster_map("contest_subsystems", "prizes")[PRIZE]
    assert row["heard_by"] == "bench"
    monkeypatch.setitem(row, "heard_by", "benchh")
    with pytest.raises(Unspecified, match=r"contest:'a matter' declares `heard_by: 'benchh'`"):
        registry.check_rows()


# ================================================================================================
# STEP 18 -- PROOFS, BY REMOVE AND THE MIRROR
# ================================================================================================

def test_sc02_18_a_mirrored_proof_moves_the_obstacle_by_exactly_zero_and_an_unmirrored_one_by_step_x_remove():
    """`19_PLAN.md` step 18's artifact. The speaker tells (holds) a deed claim about his opponent; the
    hearer holds nothing, so reception is 0 and only the proofs term moves the obstacle.
    FALSIFIER: the mirrored proof moves the obstacle (exact equality with the base, no tolerance)."""
    kind = sorted(_verbs.DEED_KINDS - person_q.PAIRED_KINDS)[0]
    checked = 0
    for source in REMOVE_ORDINAL:
        chain = ("p_king",) if source == "told_by" else ()
        w, _d = _judging_world()
        base = _ob(w)
        step = w.fixtures.get("proof_step")
        assert step > 0, "the shipped step is the control: the falsifier could not see a move"
        w.persons[SPEAKER].ledger.append(_claim("pf", SPEAKER, PARTY, kind, source=source, chain=chain))
        assert world_q.reception(w, SPEAKER, "Hh") == 0.0
        assert _ob(w) == base - step * world_q.remove_weight(source), (source, _ob(w), base)
        # THE MIRROR: the opponent holds a claim of the same subject and predicate -> exactly zero.
        w.persons[PARTY].ledger.append(_claim("mirror", PARTY, PARTY, kind))
        assert world_q.proofs(w, SPEAKER, PARTY) == 0.0
        assert _ob(w) == base, (source, _ob(w), base)
        checked += 1
    assert checked == len(REMOVE_ORDINAL)


def test_sc02_18_proofs_never_take_the_obstacle_below_the_floor_and_a_non_person_mirrors_nothing():
    w, _d = _judging_world()
    kind = sorted(_verbs.DEED_KINDS - person_q.PAIRED_KINDS)[0]
    for i in range(40):
        w.persons[SPEAKER].ledger.append(_claim(f"pf{i}", SPEAKER, PARTY, kind))
    assert _ob(w) == 1.0                                 # OB_MIN, never below
    assert world_q.proofs(w, SPEAKER, "Hh") == 0.0       # a rung: no deed claims about it here
    assert world_q.proofs(w, SPEAKER, None) == 0.0


# ================================================================================================
# STEP 20 -- ROUTE EROSION: THE SINGLE CALLED BLUFF
# ================================================================================================

def _feared_lord(w):
    """The speaker governs by fear in the hearer's eyes: dominance-route deeds the hearer saw (tick 0)."""
    kind = _kind_with_lean(w, +1, among=DOMINANCE_KINDS) if any(
        _lean(w, k) > 0 for k in DOMINANCE_KINDS - person_q.PAIRED_KINDS) else sorted(
        DOMINANCE_KINDS - person_q.PAIRED_KINDS)[0]
    assert _lean(w, kind) != 0.0, kind
    for i in range(3):
        w.persons[HEARER].ledger.append(_claim(f"dom{i}", HEARER, SPEAKER, kind, when=0))
    return kind


def test_sc02_20_the_nobodys_one_success_collapses_the_lord_and_his_failure_leaves_him_intact():
    """`19_PLAN.md` step 20's artifact. The lord (`p_low`) is challenged by a nobody (`p_other`) at tick 1.
      * SUCCESS: the hearer saw the nobody wound the lord -- `(p_low, body.changed)` paired by a sighting
        whose `who` is the nobody. Every dominance deed of the lord's no newer than it counts zero.
      * FAILURE: the hearer saw the lord wound the nobody -- `(p_other, body.changed)`, `who` the lord. His
        dominance weight stands, and the wound is one more deed of his.
    FALSIFIER: a called bluff leaves the weight unchanged (`success != before`, exactly 0 here)."""
    wound = "body.changed"
    assert wound in DOMINANCE_KINDS and wound in person_q.PAIRED_KINDS
    before_w, _ = _judging_world()
    _feared_lord(before_w)
    before = world_q.reception(before_w, SPEAKER, "Hh")
    assert before != 0.0

    won, _ = _judging_world()
    _feared_lord(won)
    won.persons[HEARER].ledger += [_claim("hit", HEARER, SPEAKER, wound, when=1),
                                   _seen("saw", HEARER, SPEAKER, NOBODY, when=1)]
    assert [c.id for c in person_q.suffered_deeds(won.persons[HEARER].ledger, SPEAKER)] == ["hit"]
    assert world_q.reception(won, SPEAKER, "Hh") == 0.0, "a called bluff left the dominance weight"

    lost, _ = _judging_world()
    _feared_lord(lost)
    lost.persons[HEARER].ledger += [_claim("hit", HEARER, NOBODY, wound, when=1),
                                    _seen("saw", HEARER, NOBODY, SPEAKER, when=1)]
    assert list(person_q.suffered_deeds(lost.persons[HEARER].ledger, SPEAKER)) == []
    only_new, _ = _judging_world()
    only_new.persons[HEARER].ledger += [_claim("hit", HEARER, NOBODY, wound, when=1),
                                        _seen("saw", HEARER, NOBODY, SPEAKER, when=1)]
    # Additive: the lord keeps his whole prior weight plus the new deed's (float sum order differs).
    assert math.isclose(world_q.reception(lost, SPEAKER, "Hh"),
                        before + world_q.reception(only_new, SPEAKER, "Hh"), rel_tol=1e-12)


def test_sc02_20_only_a_witness_is_moved_and_a_later_coercive_deed_counts_again():
    """A hearer only TOLD of the bluff holds no sighting, so no doer is named and nothing erodes; a
    dominance deed of the lord's AFTER the bluff counts again; a non-dominance deed is never eroded."""
    wound = "body.changed"
    told, _ = _judging_world()
    _feared_lord(told)
    before = world_q.reception(told, SPEAKER, "Hh")
    told.persons[HEARER].ledger.append(_claim("hit", HEARER, SPEAKER, wound, source="told_by",
                                              chain=(NOBODY,), when=1))
    assert world_q.reception(told, SPEAKER, "Hh") == before

    later, _ = _judging_world()
    kind = _feared_lord(later)
    later.persons[HEARER].ledger += [_claim("hit", HEARER, SPEAKER, wound, when=1),
                                     _seen("saw", HEARER, SPEAKER, NOBODY, when=1),
                                     _claim("again", HEARER, SPEAKER, kind, when=2)]
    # Only the re-earned deed counts: one firsthand claim at full confidence is its valence exactly.
    assert world_q.reception(later, SPEAKER, "Hh") == _lean(later, kind) != 0.0

    other, _ = _judging_world()
    gentle = _kind_with_lean(other, +1, among=_verbs.DEED_KINDS - DOMINANCE_KINDS)
    other.persons[HEARER].ledger += [_claim("g", HEARER, SPEAKER, gentle, when=0),
                                     _claim("hit", HEARER, SPEAKER, wound, when=1),
                                     _seen("saw", HEARER, SPEAKER, NOBODY, when=1)]
    assert world_q.reception(other, SPEAKER, "Hh") == _lean(other, gentle)


# ================================================================================================
# THE TWO MAGNITUDES' SWEEPS, EXECUTED (`H-215`, `H-216`; read off the register, not copied)
# ================================================================================================

def _sweep_of(hid):
    import yaml
    rows = yaml.safe_load((SEASON_DIR / "hole_register.yaml").read_text())["rows"]
    (row,) = [r for r in rows if r["id"] == hid]
    return row["sweep"], row["site"].split(",")[0].split()[-1]


def test_sc02_the_reception_gain_and_proof_step_sweeps_run_and_zero_is_the_control():
    """Each declared point is run through the real adapter: `0` reads the no-room obstacle exactly (the
    CONTROL), and each larger point lowers it at least as far, strictly at the first step."""
    kind = None
    for hid in ("H-215", "H-216"):
        points, fixture = _sweep_of(hid)
        assert len(points) == 3 and 0 in points, (hid, points)
        obs = []
        for point in sorted(points):
            w, _d = _world(**{fixture: point})
            w.persons[HEARER].pursuits = {PURSUIT: 1.0}
            kind = kind or _kind_with_lean(w, +1)
            w.persons[HEARER].ledger.append(_claim("fav", HEARER, SPEAKER, kind))
            w.persons[SPEAKER].ledger.append(_claim("pf", SPEAKER, PARTY, kind))
            other = "proof_step" if fixture == "reception_gain" else "reception_gain"
            w.fixtures = w.fixtures.sweep(other, 0)
            obs.append(_ob(w))
        assert obs[0] == w.fixtures.get("obstacle_default"), (hid, obs)
        assert obs[0] > obs[1] >= obs[2], (hid, obs)


def test_sc02_20_the_route_roster_names_only_deed_kinds():
    assert DOMINANCE_KINDS and DOMINANCE_KINDS <= _verbs.DEED_KINDS, sorted(DOMINANCE_KINDS)
    assert DOMINANCE_KINDS & person_q.PAIRED_KINDS, "no dominance kind has a patient: no bluff is callable"
