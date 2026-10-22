"""v9 IN-23 (CARRY-STABILITY, `workplans/valoria_master_workplan_v9_part5.md`) -- legitimacy and
stability as Queries over ONE person's own stance and claims, no stored value (ruling R7):
`queries/person_q.py::legitimacy`, `stability`, `recent_claims`; read by the STORY-BAR instrument
(`harness/storybar.py::estimates`) only (H-224: a chooser consumer was built and reverted at B-U's
close, as wider than the plan's EDITS).

THE FALSIFIER (the plan's: *the Query read by nothing, or a value stored on `World` -> fail*), each arm
able to fail:
  (a) two persons holding different claims about one rung / one holder read different estimates, and
      the control -- identical ledgers -- reads identical ones;
  (b) the window: a claim one season inside it counts, one at its edge does not, both Queries;
  (c) asking writes nothing (hash, log, writes) and neither `World` nor any carrier has such a field;
  (d) the reader executes: the instrument calls both Queries in a seeded season.
MUTATION (run at IN-23): `legitimacy` and `stability` stubbed to a constant redden (a).
"""
from __future__ import annotations

import ast
import dataclasses

import pytest

from ..data import files
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.verbs import DEED_KINDS
from ..harness import storybar as SB
from ..queries import person_q as PQ
from ..state import carriers
from ..state.carriers import Claim, Person

RUNG, HOLDER = "r_in23", "p_in23_holder"
SEED, CAP = 0, 10


def _claim(cid, subject, predicate, when, value=True, chain=()):
    return Claim(cid, "h", subject, predicate, value, when, "firsthand", 100, "own", chain=chain)


def _person(pid, ledger=(), stance=()):
    p = Person(id=pid, name=pid)
    p.pursuits = dict(virtue=1.0)
    p.ledger = list(ledger)
    p.stance = list(stance)
    return p


def _leaning_kind(p) -> str:
    """An unpaired deed kind `p`'s pursuits judge non-zero, read off the tables."""
    axis_w = PQ.projected_axes(p)
    kinds = sorted(k for k in DEED_KINDS - PQ.PAIRED_KINDS if PQ._lean(axis_w, k))
    assert kinds, "no unpaired deed kind leans on these pursuits: nothing to judge"
    return kinds[0]


def test_in23_shipped_window_is_the_decay_life_of_a_claim():
    fx = DEFAULT_FIXTURES
    assert fx.get("estimate_window_seasons") == (
        fx.get("confidence_default") // fx.get("claim_decay_per_season"))


# (a) ---------------------------------------------------------------------------------------------

def test_in23_two_ledgers_read_two_estimates_and_one_ledger_reads_one():
    unrest = sorted(PQ.UNREST_KINDS)[0]
    kind = _leaning_kind(_person("probe"))
    ledger_a = [_claim("c1", RUNG, unrest, 3), _claim("c2", RUNG, f"{PQ.SHORTFALL_PREDICATE}:grain", 3, 4),
                _claim("c3", HOLDER, kind, 3), _claim("c4", "elsewhere", "seen", 3, None)]
    ledger_b = [_claim("c4", "elsewhere", "seen", 3, None)]
    stance = [(HOLDER, 1.0, 2.0)]
    a, b = _person("p_a", ledger_a, stance), _person("p_b", ledger_b, stance)
    twin = _person("p_twin", ledger_a, stance)
    checked = 0
    assert PQ.stability(a, RUNG, 20) == -2 and PQ.stability(b, RUNG, 20) == 0
    checked += 1
    la, lb = PQ.legitimacy(a, HOLDER, 20), PQ.legitimacy(b, HOLDER, 20)
    assert lb == PQ.stance_toward(b, HOLDER) == 2.0
    assert la == lb + PQ._lean(PQ.projected_axes(a), kind) and la != lb
    checked += 1
    # THE CONTROL: the same ledger and stance under another id read the same, both Queries
    assert PQ.stability(twin, RUNG, 20) == PQ.stability(a, RUNG, 20)
    assert PQ.legitimacy(twin, HOLDER, 20) == la
    checked += 1
    assert checked >= 3


def test_in23_a_ruler_reads_his_own_standing_by_his_own_ledger():
    """R7's *a ruler can be wrong about their own standing*: the holder and a subject who saw his deed
    read his legitimacy differently, and neither reads the other's."""
    kind = _leaning_kind(_person("probe"))
    ruler = _person(HOLDER)
    subject = _person("p_subject", [_claim("c1", HOLDER, kind, 0)])
    assert PQ.legitimacy(ruler, HOLDER, 20) == 0.0
    assert PQ.legitimacy(subject, HOLDER, 20) != 0.0


def test_in23_a_kind_outside_the_read_set_is_no_unrest():
    outside = sorted(k for k in DEED_KINDS if k not in PQ.UNREST_KINDS)[0]
    p = _person("p", [_claim("c1", RUNG, outside, 0),
                      _claim("c2", RUNG, sorted(PQ.UNREST_KINDS)[0], 0, value=False)])
    assert PQ.stability(p, RUNG, 20) == 0


# (b) ---------------------------------------------------------------------------------------------

def test_in23_the_window_counts_inside_and_drops_at_its_edge():
    kind = _leaning_kind(_person("probe"))
    unrest = sorted(PQ.UNREST_KINDS)[0]
    newest = _claim("c0", "elsewhere", "seen", 10, None)       # the anchor: the newest claim held
    lean = PQ._lean(PQ.projected_axes(_person("probe")), kind)
    checked = 0
    for when, counts in ((8, True), (7, False)):              # window 3: ages 0..2 count, 3 does not
        p = _person("p", [_claim("u", RUNG, unrest, when), _claim("d", HOLDER, kind, when), newest])
        assert PQ.stability(p, RUNG, 3) == (-1 if counts else 0), when
        assert PQ.legitimacy(p, HOLDER, 3) == (lean if counts else 0.0), when
        checked += 1
    assert checked == 2
    assert PQ.recent_claims([], 1) == []


@pytest.mark.parametrize("window", [0, -1, True, 1.5, float("nan"), None])
def test_in23_a_window_that_is_no_whole_number_of_seasons_raises(window):
    with pytest.raises(ValueError, match="H-224"):
        PQ.recent_claims([_claim("c", RUNG, "seen", 0, None)], window)


# (c) ---------------------------------------------------------------------------------------------

@pytest.fixture(scope="module")
def driven():
    return SB.drive(SEED, 1, "off", CAP)


def _snapshot(w):
    return w.content_hash(), len(w.log), len(w.writes), {k: len(p.ledger) for k, p in w.persons.items()}


def test_in23_asking_writes_nothing(driven):
    w, _d, _b = driven
    before = _snapshot(w)
    est = SB.estimates(w)
    for p in w.persons.values():
        for r in w.rungs:
            PQ.stability(p, r, 1)
        PQ.legitimacy(p, p.id, 1)
    after = _snapshot(w)
    assert est["legitimacy"]["pairs"] > 0 and est["stability"]["pairs"] > 0, est
    assert after == before


def test_in23_the_writes_nothing_snapshot_sees_a_write_planted_in_the_read_path(monkeypatch):
    """THE PLANTED CONTROL (`test_revolt_query.py`'s precedent): `storybar.stability`, bound by name, is
    replaced by a reader that also appends a claim to the asking person's ledger. The snapshot the
    writes-nothing test takes must MOVE, or that test could not have observed a write."""
    from ..harness import populated as POP
    w = POP.build_realm(SEED, CAP)
    fired = []

    def writing(p, rung, window):
        fired.append(rung)
        p.ledger.append(_claim(f"planted_{len(fired)}", rung, sorted(PQ.UNREST_KINDS)[0], 0))
        return PQ.stability(p, rung, window)
    monkeypatch.setattr(SB, "stability", writing)
    before = _snapshot(w)
    SB.estimates(w)
    assert fired, "the plant never ran: `estimates` does not read through `storybar.stability`"
    assert _snapshot(w) != before, "a planted ledger write left the writes-nothing snapshot unmoved"


def test_in23_no_carrier_and_no_world_attribute_holds_such_a_value(driven):
    names = ("legitimacy", "stability")
    tree = ast.parse((files.STATE_DIR / "world.py").read_text())
    world = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "World")
    attrs = {t.attr for n in ast.walk(world) if isinstance(n, (ast.Assign, ast.AnnAssign, ast.AugAssign))
             for t in (n.targets if isinstance(n, ast.Assign) else [n.target])
             if isinstance(t, ast.Attribute) and isinstance(t.value, ast.Name) and t.value.id == "self"}
    assert len(attrs) > 10, "the scan found no World attributes: it observes nothing"
    assert not [a for a in attrs if any(n in a for n in names)], attrs
    w, _d, _b = driven
    assert not [a for a in vars(w) if any(n in a for n in names)]
    fields = {f.name for c in vars(carriers).values() if dataclasses.is_dataclass(c) and isinstance(c, type)
              for f in dataclasses.fields(c)}
    assert "ledger" in fields and not [f for f in fields if any(n in f for n in names)]


# (d) ---------------------------------------------------------------------------------------------

def test_in23_the_instrument_reads_both_queries_in_a_seeded_season(monkeypatch):
    calls = {"legitimacy": 0, "stability": 0}

    def spy(name, real):
        def f(*a, **k):
            calls[name] += 1
            return real(*a, **k)
        return f
    monkeypatch.setattr(SB, "legitimacy", spy("legitimacy", PQ.legitimacy))
    monkeypatch.setattr(SB, "stability", spy("stability", PQ.stability))
    r = SB.run_seed(SEED, 1, "off", CAP)
    assert calls["legitimacy"] > 0 and calls["stability"] > 0, calls
    assert len(r["estimates"]) == 1 and r["estimates"][0]["legitimacy"]["pairs"] == calls["legitimacy"]
