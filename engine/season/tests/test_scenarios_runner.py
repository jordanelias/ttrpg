"""B11.05 -- the scenario registry's one run loop (`harness/scenarios.py::run`), against the loop it claims to be.

THE FALSIFIER: the runner's hash differs from `populated.run`'s for the same seed, i.e. the loop is not the shipped one.
The registry is empty in this commit (B11.06 registers the first row), so the realm row is registered test-locally. The
per-row checks (every ending name has a kind; a role declared unreached reads zero) are B11.06's: they observe nothing
until a row exists.
"""
from engine.season.boot.realm import build_realm
from engine.season.harness import populated, scenarios as SC


def _realm_row(**kw):
    return SC.Scenario(build=build_realm, seat=lambda w: sorted(w.persons)[0], ending=lambda w: None, **kw)


def test_the_runner_and_populated_run_agree(monkeypatch):
    """The realm at seed 0, one season: `run` with `pick=None` (the seat takes the shipped ranking whole) returns
    `populated.run`'s content hash. The seated space was called, or the equality shows nothing about the seat."""
    monkeypatch.setitem(SC.SCENARIOS, "realm", _realm_row())
    w = build_realm(0)
    populated.run(1, 0, w=w)
    out = SC.run("realm", 0, 1)
    assert out["hash"] == w.content_hash()
    assert out["seat_deliberations"] >= 1, "the seated person was never asked; the control proves nothing"
    assert out["ending"] is None and out["kind"] is None
