"""B10.07 -- a scar is a wound: who can be scarred (`scar_hold`, `scar_primary_mass`, `scar_lean_floor`) and what takes a count
away (`scar_vindication`), on `loop/resolve.py::_scar_witnesses` and `queries/person_q.py`. Every arm ships at its control; these
tests plant a world and read the counts the real driver's fold writes at the swept arms.

FALSIFIER: a non-primary or mild violation is still counted at the live arms, or a witnessed honouring takes no count away.
"""
from __future__ import annotations

from ..data import affiliations as A
from ..data.pursuits import pursuit
from ..data.matrix import Step, WriteClass
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
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
