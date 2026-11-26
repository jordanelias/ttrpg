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
from engine.season.queries import world_q
from engine.season.state.carriers import Claim






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
        pid = sorted(w.persons)[0] if row.seat is None else row.seat(w)       # a row with no default seat is read at a person of its world
        for planted in (False, True):
            with monkeypatch.context() as mp:      # undone before the next row: a planted pass must not reach the rows after it
                if planted:
                    mp.setattr(SC.world_q, "endings_reached", lambda w: [object()])
                for who, left in ((pid, 1), (pid, 0), (None, 1)):
                    got = row.ending(w, who, left)
                    if got is not None:
                        assert got in row.kinds, f"{name}: ending {got!r} has no `kinds` entry"
                        checked += 1
    assert checked >= 1


# --- B11.79: the `life` row (`IS-B2-CHAR-01`) ----------------------------------------------------------------------------
# The seat is a person of the realm; the realm is built once per test (about 8 s) and a season is played only where the test says so.
GATE = "goal_varfell_oastad_gate"          # the realm's one rung goal whose rung is held at build (`test_fi_referents.py`'s met aim)


def _life_seat(w):
    """A seat that reads `open` at build: the first person in id order, asserted not to be the rung's governing holder."""
    pid = sorted(w.persons)[0]
    assert SC.life_ending(w, pid, 1) is None, f"{pid} already holds a met ambition; pick another seat"
    return pid


def test_life_with_take_ranked_reproduces_the_realm_hash():
    """GAME-STATE, lane season_loop. The realm at seed 0, one season, the seat taking the ranking whole: `populated.run`'s content hash. The
    seat was asked, and the run played its season, or the equality shows nothing about the row."""
    w = build_realm(0)
    pid = _life_seat(w)
    populated.run(1, 0, w=w)
    out = SC.run("life", 0, 1, person=pid)
    assert out["hash"] == w.content_hash()
    assert out["seat_deliberations"] >= 1 and out["seasons"] == 1
    assert (out["ending"], out["kind"]) == ("unfinished", "drawn") and out["passed"] == (pid,)


def test_a_scripted_pick_moves_the_realm_hash():
    """GAME-STATE, lane season_loop. One pick changed at lap 1: the seat's first candidate only. The hash moves, so the seat's pick is load-bearing in this row."""
    w = build_realm(0)
    pid = _life_seat(w)
    laps = []

    def ranked(sheet):
        laps.append(list(take_ranked(sheet)))
        return laps[-1]
    base = SC.run("life", 0, 1, person=pid, pick=ranked)
    assert laps and len(laps[0]) >= 2, "lap 1 offered the seat fewer than two picks; a deviation has nothing to drop"
    first = []

    def deviating(sheet):
        first.append(1)
        return laps[0][:1] if len(first) == 1 else take_ranked(sheet)
    deviant = SC.run("life", 0, 1, person=pid, pick=deviating)
    assert deviant["hash"] != base["hash"]


def test_a_met_ambition_ends_the_life_as_fulfilled():
    """GAME-STATE, lane season_loop. PLANTED: a committed man of the realm's met rung goal who has heard who holds the rung reads `met` (`aim_state`), and the run
    ends `fulfilled` (`won`) at once. CONTROL: the same man, nothing planted, runs on (zero seasons asked of him, so `unfinished`, the clock's name)."""
    def committed_other(w):
        governing = world_q.governing_hold(w, "terr_T13")
        return governing, next(t.subject for t in w.tenures if t.kind == "commit" and t.live and t.object == GATE and t.subject != governing.subject)

    def plant(w):
        governing, other = committed_other(w)
        for n, subject in enumerate((governing.subject, governing.object)):          # the two claims a witness of the hold deposits (test_fi_referents.hears_of)
            w.persons[other].ledger.append(Claim(f"c_heard_{other}_{n}", other, subject, "tenure.opened", True, 0, "told_by", 100, "own", 0))
    w = build_realm(0)
    _, other = committed_other(w)
    control = SC.run("life", 0, 0, person=other)
    assert (control["ending"], control["kind"], control["seasons"]) == ("unfinished", "drawn", 0)
    planted = SC.run("life", 0, 0, person=other, on_build=plant)
    assert (planted["ending"], planted["kind"], planted["seasons"]) == ("fulfilled", "won", 0)
    assert SC.life_reading(planted["world"], other).endswith(GATE)


def test_a_dead_seat_is_offered_its_ties_and_an_empty_offer_ends_the_line(monkeypatch):
    """GAME-STATE, lane season_loop. The seat dies after the first reading of his ties (planted through the row's `ending`, as the matter step would kill him).
    (1) His living ties are OFFERED, in `continuation_ties` order, and the pick taken is the one the seat becomes (`passed`). (2) The same death with every tie dead too:
    the offer is empty, `line_extinct` (`lost`)."""
    w = build_realm(0)
    pid = next(p for p in sorted(w.persons) if len(world_q.continuations(w, w.persons[p])) >= 2)
    ties = world_q.continuations(w, w.persons[pid])
    row = SC.SCENARIOS["life"]
    state = {}

    def kill(world, who, doomed):
        world.step, world._emitted_by_write = Step.MATTER, []
        for victim in doomed:
            if victim in world.persons:
                _die(world, mint_token(world, WriteClass.MATTER), victim)

    def planted(doomed):
        def ending(world, who, left):
            if not state.get("done"):
                state["done"] = True
                kill(world, who, doomed)
            return row.ending(world, who, left)
        return SC.Scenario(build=lambda seed: build_realm(seed), seat=None, ending=ending, kinds=row.kinds)

    monkeypatch.setitem(SC.SCENARIOS, "life_dying", planted([pid]))
    offers = []
    out = SC.run("life_dying", 0, 1, person=pid, tie=lambda offer: (offers.append(offer), offer[-1])[1])
    assert len(offers) == 1 and [c.person for c in offers[0]] == [c.person for c in ties if c.person in out["world"].persons]
    assert out["passed"] == (pid, ties[-1].person) and out["seat"] == ties[-1].person and pid not in out["world"].persons

    state.clear()
    monkeypatch.setitem(SC.SCENARIOS, "life_dying", planted([pid] + [c.person for c in ties]))
    out = SC.run("life_dying", 0, 1, person=pid)
    assert (out["ending"], out["kind"], out["seat"], out["passed"]) == ("line_extinct", "lost", None, (pid,))
