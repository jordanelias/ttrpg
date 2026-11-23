"""B11.05 / B11.06 -- the scenario registry's one run loop (`harness/scenarios.py::run`), against the loop it claims to be,
and the first registered row, `season`.

THE FALSIFIERS: the runner's hash differs from `populated.run`'s / `headless.run`'s for the same seed (the loop is not the
shipped one); a scripted deviation leaves the hash unchanged (`plays` is false); a run that ignores `endings_reached`.
"""
import pytest

from engine.season.boot.realm import build_realm
from engine.season.data.matrix import Step, WriteClass
from engine.season.decision.sheet import take_ranked
from engine.season.harness import headless, populated, scenarios as SC
from engine.season.loop.driver import mint_token
from engine.season.loop.matter import _die


def _realm_row(**kw):
    return SC.Scenario(build=build_realm, seat=lambda w: sorted(w.persons)[0], ending=lambda w, pid, left: None, **kw)


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


# --- B11.06: the `season` row -------------------------------------------------------------------------------------

def _script(tmp_path, lines):
    f = tmp_path / "script.txt"
    f.write_text("\n".join(lines) + "\n")
    return SC._picker(SC._parse(["season", "--script", str(f)]))


def _recorded(seed, seasons):
    """The picks `take_ranked` makes at each lap, as the script lines that would echo them, and the run's result."""
    laps = []

    def pick(sheet):
        laps.append(list(take_ranked(sheet)))
        return laps[-1]
    out = SC.run("season", seed, seasons, pick=pick)
    return [" ".join(map(str, p)) for p in laps], out


@pytest.mark.parametrize("seed", [0, 1, 2])
def test_take_ranked_reproduces_the_automated_hash(seed):
    """THE CONTROL: the seat taking the ranking whole is `headless.run`'s own season (Carin's case, two seasons)."""
    out = SC.run("season", seed, 2)
    assert out["hash"] == headless.run(2, seed)["hash"]
    assert out["seat_deliberations"] >= 1, "the seated person was never asked; the equality shows nothing about the seat"
    assert (out["ending"], out["kind"], out["seasons"]) == ("time", "drawn", 2)


def test_a_scripted_deviation_moves_the_hash(tmp_path):
    """One pick changed at lap 1, seed 0. If the hash did not move the pick is not load-bearing and 'plays' is false."""
    lines, base = _recorded(0, 2)
    assert lines and len(lines[0].split()) >= 2, "lap 1 offered the seat fewer than two candidates; a deviation has nothing to drop"
    deviant = " ".join(lines[0].split()[:1])                          # lap 1: the first candidate only, the rest unpicked
    out = SC.run("season", 0, 2, pick=_script(tmp_path, [deviant]))      # once the script is spent the ranking is taken whole
    assert out["hash"] != base["hash"]


def test_a_played_season_replays_from_its_script(tmp_path):
    """The same script twice is one hash, and a script of `take_ranked`'s own picks is the echo of the automated run."""
    lines, base = _recorded(0, 2)
    deviant = [" ".join(lines[0].split()[:1])]
    a = SC.run("season", 0, 2, pick=_script(tmp_path, deviant))["hash"]
    b = SC.run("season", 0, 2, pick=_script(tmp_path, deviant))["hash"]
    assert a == b
    assert SC.run("season", 0, 2, pick=_script(tmp_path, lines))["hash"] == base["hash"]


def test_the_run_stops_on_an_ending_or_a_dead_seat_with_no_continuation(monkeypatch):
    """Two planted worlds. (1) The seat dies before the first season and the headless world holds no tie to carry his line on:
    `line_extinct`, after the one season. (2) `endings_reached` is non-empty at build: `realm_ended`, before any season."""
    row = SC.SCENARIOS["season"]
    dead = []

    def ending(w, pid, left):                      # the seat dies before the first season, as the matter step would kill him
        if not dead:
            dead.append(pid)
            w.step, w._emitted_by_write = Step.MATTER, []
            _die(w, mint_token(w, WriteClass.MATTER), pid)
        return row.ending(w, pid, left)
    monkeypatch.setitem(SC.SCENARIOS, "planted", SC.Scenario(build=row.build, seat=row.seat, ending=ending, kinds=row.kinds))
    out = SC.run("planted", 0, 2)
    assert dead and dead[0] not in out["world"].persons
    assert (out["ending"], out["kind"]) == ("line_extinct", "lost") and out["seasons"] == 1

    monkeypatch.setattr(SC.world_q, "endings_reached", lambda w: [object()])
    out = SC.run("season", 0, 2)
    assert (out["ending"], out["kind"], out["seasons"], out["seat_deliberations"]) == ("realm_ended", "drawn", 0, 0)


# --- the two per-row checks (B11.05 left them for the first registered row) ---------------------------------------------

def test_every_ending_name_a_reader_can_return_has_a_kind(monkeypatch):
    """Each registered row's `ending`, read on its own built world under every argument shape (the seat bound and a season
    left, the seat bound and none left, no seat, a realm already ended), returns only names its `kinds` holds."""
    checked = 0
    for name, row in SC.SCENARIOS.items():
        w = row.build(0)
        pid = row.seat(w)
        for planted in (False, True):
            if planted:
                monkeypatch.setattr(SC.world_q, "endings_reached", lambda w: [object()])
            for who, left in ((pid, 1), (pid, 0), (None, 1)):
                got = row.ending(w, who, left)
                if got is not None:
                    assert got in row.kinds, f"{name}: ending {got!r} has no `kinds` entry"
                    checked += 1
    assert checked >= 1
