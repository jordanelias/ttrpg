"""B10.07 -- a scar is a wound: who can be scarred (`scar_hold`, `scar_primary_mass`, `scar_lean_floor`) and what takes a count
away (`scar_vindication`), on `loop/resolve.py::_scar_witnesses` and `queries/person_q.py`. Every arm ships at its control; these
tests plant a world and read the counts the real driver's fold writes at the swept arms.

FALSIFIER: a non-primary or mild violation is still counted at the live arms, or a witnessed honouring takes no count away.
"""
from __future__ import annotations

import pytest

from ..data import affiliations as A
from ..data.pursuits import pursuit, to_axes
from ..decision.choose import _AXIS_W, deliberation_memo
from ..data.matrix import Step, WriteClass
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..queries import person_q as PQ
from ..state.carriers import Act
from ._scar_helpers import rebound, scars, wounded

LIVE = dict(scar_hold="primary", scar_lean_floor=0.2, scar_vindication="on")


def _world(pursuits, conviction=None, scar=None, **arms):
    """`tiny_world`, everyone an observer (`fan_out_mode: total`), each person holding `pursuits` and `conviction` and the planted `scar`."""
    w = P.tiny_world()
    w.step = Step.RESOLVE
    fx = w.fixtures.sweep("fan_out_mode", "total")
    for name, v in arms.items():
        fx = fx.sweep(name, v)
    w.fixtures = fx
    for p in w.persons.values():
        p.pursuits, p.conviction, p.scar = dict(pursuits), dict(conviction or {}), dict(scar or {})
    return w


def _fight(w, n=1, d=None):
    """The driver `d` (one per season: it holds the season's tally) folds `fight` (violates `justice`, `liberty`, `love`, `scholastics`;
    upholds `honour`, `reputation`) `n` times."""
    d = d or SeasonDriver(w)
    for _ in range(n):
        d._seen = getattr(d, "_seen", 0) + 1
        d._fold(w, mint_token(w, WriteClass.ACTS), Act(id=f"stock{d._seen}", actor="p_low", verb="fight", payload={"subject": "p_mid"}), wounded())
    return scars(w)


def test_only_what_a_person_chiefly_lives_for_can_be_scarred(monkeypatch):
    """Primary = the fewest top-weighted pursuits summing to `scar_primary_mass` (here justice .4 + liberty .3), and the affiliations
    he stands for (intensity 3 or more of 5); a violation under `scar_lean_floor` is not one. Each arm is read on the same planted people."""
    monkeypatch.setattr(A, "ENGAGEMENT", rebound(**{A.SHARED_COLUMN: {"fight": -0.3}}))   # `fight` has no shipped affiliation cell
    held = {pursuit("justice"): 0.4, pursuit("liberty"): 0.3, pursuit("love"): 0.2, pursuit("wealth"): 0.05}
    creed = {"thread_truth": 4, "inner_tradition": 2}
    got = {name: _fight(_world(held, creed, **arms)) for name, arms in {
        "control": {}, "primary": {"scar_hold": "primary"}, "floor": {"scar_lean_floor": 0.31}}.items()}
    every = {pursuit("justice"), pursuit("liberty"), pursuit("love"), pursuit("wealth"), "thread_truth", "inner_tradition"}
    assert got["control"] and all(set(c) == every and set(c.values()) == {1} for c in got["control"].values()), got["control"]
    assert all(set(c) == {pursuit("justice"), pursuit("liberty"), "thread_truth"} for c in got["primary"].values()) and len(got["primary"]) == 5, got["primary"]
    assert all(set(c) == {pursuit("liberty"), "thread_truth", "inner_tradition"} for c in got["floor"].values()) and len(got["floor"]) == 5, got["floor"]


def test_vindication_lowers_a_count_at_least_once():
    """A person with a primary at count 2 who sees an act honour it (`fight`, lean on `honour` above the floor) loses one count, in the
    same act that scars him on `justice`; once per person per season however often he sees it; never below 0, and a person with no
    count to lose keeps his allowance. Off, the count stays."""
    held = {pursuit("honour"): 0.5, pursuit("justice"): 0.3}
    off = _fight(_world(held, scar={pursuit("honour"): 2}, **{**LIVE, "scar_vindication": "off"}))
    assert all(c == {pursuit("honour"): 2, pursuit("justice"): 1} for c in off.values()) and len(off) == 5, off
    w = _world(held, scar={pursuit("honour"): 2}, **LIVE)
    w.persons["p_other"].scar = {}
    d = SeasonDriver(w)
    once = _fight(w, 1, d)
    assert all(c == {pursuit("honour"): 1, pursuit("justice"): 1} for pid, c in once.items() if pid != "p_other"), once
    assert once["p_other"] == {pursuit("justice"): 1}, "no count to lose, so none taken below 0"
    twice = _fight(w, 2, d)                                  # a second and third sight, the same season
    assert all(c == {pursuit("honour"): 1, pursuit("justice"): 3} for pid, c in twice.items() if pid != "p_other"), twice
    assert twice["p_other"] == {pursuit("justice"): 3}
    healed = [e for e in w.log if e.kind == "scar.healed"]
    assert len(healed) == 1 and len(healed[0].changes) == 4, [(e.kind, len(e.changes)) for e in w.log if e.kind.startswith("scar.")]


def test_the_most_scarred_man_is_not_the_least_changed():
    """B10.08: a person scarred to 5 on every held pursuit but one at 3 (all at the threshold) reads differently from his unscarred
    twin at `scar_weight_shift` 0.5: the weight goes from the most-scarred (ties by name) to the least-scarred, the total kept; at 0 the
    twins read alike. At `scar_hold` primary the set is the primaries, so the shift stays among them while a non-primary is unscarred."""
    p = P.tiny_world().persons["p_low"]
    j, l, v, h, wl = pursuit("justice"), pursuit("liberty"), pursuit("love"), pursuit("honour"), pursuit("wealth")
    p.conviction = {}
    p.pursuits = {j: 0.3, l: 0.25, v: 0.2, h: 0.15, wl: 0.1}
    p.scar = {j: 5, l: 5, v: 5, h: 5, wl: 3}
    twin = dict(p.pursuits)
    assert PQ.crisis_weights(p, 0.0) == twin, "at the control the scarred man reads as his twin"
    got = PQ.crisis_weights(p, 0.5)
    source = min((j, l, v, h))                                # the most-scarred, ties by name
    assert got != twin and got[source] == twin[source] * 0.5, got
    assert got[wl] == pytest.approx(twin[wl] + twin[source] * 0.5), "the least-scarred gains what the most-scarred gives up"
    assert {e: w for e, w in got.items() if e not in (source, wl)} == {e: w for e, w in twin.items() if e not in (source, wl)}, got
    assert abs(sum(got.values()) - sum(twin.values())) < 1e-12
    p.pursuits, p.scar = {j: 0.4, l: 0.3, v: 0.2, wl: 0.1}, {j: 4, l: 2, v: 0, wl: 0}      # primaries j, l (mass .6): both at the threshold
    assert PQ.crisis_weights(p, 0.5, hold="primary", mass=0.6) == pytest.approx({j: 0.2, l: 0.5, v: 0.2, wl: 0.1}), "within the primaries, not to the unscarred"
    assert PQ.crisis_weights(p, 0.5)[v] > 0.2, "at `any` the unscarred are the heirs, as before"


def test_the_chooser_reads_the_weights_the_scar_writer_scarred():
    """B10.07 / B10.08: at `scar_hold` primary the writer scars only a person's primaries, so the weights the chooser reads (`deliberation_memo`) keep the shift
    among them: his one primary (justice .7 of .7 + .3, mass .6) is at the threshold with nobody else in play, so its weight is not given to the unscarred
    pursuit; at `any` the unscarred is the heir and the same person reads shifted."""
    p = P.tiny_world().persons["p_low"]
    j, l = pursuit("justice"), pursuit("liberty")
    p.conviction, p.pursuits, p.scar = {}, {j: 0.7, l: 0.3}, {j: 3}
    fx = P.tiny_world().fixtures.sweep("scar_weight_shift", 0.5)
    read = lambda hold: deliberation_memo(p, fx.sweep("scar_hold", hold))[_AXIS_W]
    assert read("primary") == to_axes(p.pursuits), "the primary alone is at the threshold: no weight goes to the unscarred"
    assert read("any") != to_axes(p.pursuits) and read("any") == pytest.approx(to_axes({j: 0.35, l: 0.65}))
