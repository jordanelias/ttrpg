"""B05.20 (U1 §11 Batch U1-D; D-U1-01, D-U1-01a) -- a seat's `modifier:` is ONE LEVEL for acts through that seat.

`offices.yaml` rows may carry `modifier: <a `sigma_leverage.LEVEL_SIGMA` name>` (absent = none); `state/carriers.py::Office.modifier`
holds it; `seam/wrappers/sigma.py::ADVANTAGE_SOURCES["office"]` reads it for an act exercised `via` that seat, where the act's prize
row says `heard_by: bench` and the seat sits over the room (`state/gate.py::sits_over`, the bench's own containment test). It is
FOR the roller only (OBS §3: the defender column is struck), and is neither a die in the pool nor a term of the opposition.

THE FALSIFIER (U1-D): *a pool or an `opposition` value that moves with a seat.* Each assertion below observes it. No shipped row
authors `modifier:` (the bench seats' first values land with B05.23), so the shipped world is the control.

The hand-built world is `test_u7_remit._world`: `off_duke` (a Duke at `D`) sits over `Hh`; the speaker `p_low` lives in `Hh`.
"""

from __future__ import annotations

import random

import pytest
import yaml

from engine.dice_engine.sigma_leverage import LEVEL_SIGMA, levels_to_net_sigma

from ..data import files, rosters
from ..gaps import Unspecified
from ..queries import world_q
from ..seam.wrappers import sigma
from ..state.carriers import Office
from .test_u7_remit import _world

SPEAKER, PARTY = "p_low", "p_mid"
SEAT = "off_duke"                 # the tiny world's Duke: scope `D`, which contains `Hh`
PRIZE = "a matter"


def _plant(w, level, seat=SEAT):
    """The seat's `modifier`, set on the carrier the world holds (the loader's job in a built realm; a test's here)."""
    w.offices[seat].modifier = level
    return w


def _roll(w, via, room="Hh"):
    """`(pool, opposition, ob, leverage, levels)` of one `speak` roll the way the fold's provider call reaches it."""
    out = sigma.resolve(w, [SPEAKER, PARTY], ["root"], PRIZE, verb="speak", subject=PARTY,
                        rng=random.Random(0), rung=room, via=via)
    assert out["status"] == "RESOLVED", out
    inp = sigma.contest_input(w, [SPEAKER, PARTY], verb="speak", subject=PARTY, room=room, via=via)
    return out["pool"], inp.opposition, out["ob"], out["leverage"], dict((n, (f, a)) for n, f, a in out["levels"])


def test_a_seat_modifier_reaches_only_acts_through_that_seat():
    w, _d = _world()
    assert world_q.place_of(w, SPEAKER) == "Hh"
    base = _roll(w, via=None)                                  # the control: nobody authors `modifier:`
    assert base[3] == 0.0 and base[4]["office"] == (0, 0), base
    assert _roll(w, via=SEAT) == base                          # a seat declaring none behaves as today (D-U1-01a)

    _plant(w, "minor")
    checked = 0
    # (1) through the seat, in the room its bench sits over: one level FOR the roller, and nothing else moves
    got = _roll(w, via=SEAT)
    assert got[4]["office"] == (1, 0), got
    assert got[3] == pytest.approx(levels_to_net_sigma(["minor"], [])) == pytest.approx(LEVEL_SIGMA["minor"])
    assert got[:3] == base[:3], (got, base)
    checked += 1
    # (2) the same speaker through no seat is the control: the modifier is for ACTS THROUGH THE SEAT, not for the seat's holder
    assert _roll(w, via=None) == base
    checked += 1
    # (3) through a seat of the same world that declares none, and that is another seat altogether
    assert _roll(w, via="off_dicastery") == base
    checked += 1
    # (4) U1-D "Check": the modifier moves THAT BENCH's rolls only -- the same seat in a room it does not sit over reads none
    outside = _roll(w, via=SEAT, room="R")                     # `R` is above `D`: the Duke's bench does not sit over it
    assert outside[4]["office"] == (0, 0) and outside[3] == 0.0, outside
    checked += 1
    # (5) a prize no bench hears reads no room, so no seat sits over it: `heard` is `None`, the source is silent
    out = sigma.resolve(w, [SPEAKER, PARTY], ["root"], PRIZE, verb="speak", subject=PARTY,
                        rng=random.Random(0), rung=None, via=SEAT)
    assert dict((n, (f, a)) for n, f, a in out["levels"])["office"] == (0, 0) and out["leverage"] == 0.0
    checked += 1
    assert checked == 5


def test_a_seat_is_never_in_the_pool_or_the_opposition():
    """THE FALSIFIER: a pool or an `opposition` value that moves with a seat. Every level of the ladder, through the seat and
    in its room, with the pool, the opposition and the composed obstacle read against the no-modifier control."""
    w, _d = _world()
    base = _roll(w, via=SEAT)
    moved = checked = 0
    for level in LEVEL_SIGMA:
        _plant(w, level)
        pool, opposition, ob, leverage, levels = _roll(w, via=SEAT)
        assert (pool, opposition, ob) == base[:3], (level, (pool, opposition, ob), base[:3])
        assert levels["office"] == (1, 0), (level, levels)             # FOR the roller, never against him (the defender column is struck)
        assert leverage == pytest.approx(LEVEL_SIGMA[level])
        moved += leverage != base[3]
        checked += 1
    assert checked == len(LEVEL_SIGMA) and moved == checked
    # the believer's own mode reads the same operand: his shown chance is the dealt one's input (`odds_of` mode (b) is built the same way)
    _plant(w, "strong")
    inp = sigma.contest_input(w, [SPEAKER, PARTY], verb="speak", subject=PARTY, room="Hh", via=SEAT)
    plain = sigma.contest_input(w, [SPEAKER, PARTY], verb="speak", subject=PARTY, room="Hh")
    assert (inp.pool, inp.opposition, inp.obstacle_operands) == (plain.pool, plain.opposition, plain.obstacle_operands)
    assert inp.leverage > plain.leverage == 0.0


def test_an_unknown_level_name_is_refused(tmp_path, monkeypatch):
    real = rosters.load_yaml(files.OFFICES_YAML.read_text(encoding="utf-8"))

    def load(doc):
        path = tmp_path / "offices.yaml"
        path.write_text(yaml.safe_dump(doc), encoding="utf-8")
        monkeypatch.setattr(rosters, "OFFICES_YAML", path)
        return rosters._load_offices()

    assert len(load(real)["seats"]) == len(real["seats"])                # control: the unchanged file loads
    row = real["seats"][0]
    assert "modifier" not in row                                         # control: no shipped row authors one at landing
    checked = 0
    for ok in (*LEVEL_SIGMA, None):                                      # a level name or `null` (= none) loads, so a loader refusing all cannot pass
        assert load(dict(real, seats=[dict(row, modifier=ok), *real["seats"][1:]]))["seats"][0]["modifier"] == ok
        checked += 1
    for bad in ("bench die", "Minor", "", 1, ["minor"]):
        with pytest.raises(Unspecified) as red:
            load(dict(real, seats=[dict(row, modifier=bad), *real["seats"][1:]]))
        assert row["id"] in str(red.value) and "modifier" in str(red.value), str(red.value)
        checked += 1
    if real.get("foreign_seats"):                                        # the same refusal over `foreign_seats:`, which shares the row shape
        frow = real["foreign_seats"][0]
        with pytest.raises(Unspecified) as red:
            load(dict(real, foreign_seats=[dict(frow, modifier="bench die"), *real["foreign_seats"][1:]]))
        assert frow["id"] in str(red.value)
        checked += 1
    assert checked >= len(LEVEL_SIGMA) + 6


def test_the_carrier_holds_the_row_value_and_defaults_to_none(monkeypatch):
    from ..boot.realm import build_realm
    assert Office("o", "Duke", "D", [], faction="Valorsmark").modifier is None
    realm = build_realm(0)
    assert all(o.modifier is None for o in realm.offices.values())      # nobody authors one at landing: the control
    seat = next(iter(rosters.SEAT_ROW_BY_ID))
    monkeypatch.setitem(rosters.SEAT_ROW_BY_ID[seat], "modifier", "minor")
    planted = build_realm(0)
    assert planted.offices[seat].modifier == "minor"
    assert [o.id for o in planted.offices.values() if o.modifier is not None] == [seat]
