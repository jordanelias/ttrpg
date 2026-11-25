"""B05.23 -- T13 COMMIT 2: THE TUNING TABLES AT THEIR CALIBRATED VALUES, READ ON PLANTED WORLDS (`proposals/13_SC_tuning_tables.md` "Gate",
T1, T2, T4; `13_SC_calibration.md` §3 steps 1 and 2).

THE CLAIMS, AND WHAT WOULD SHOW EACH WRONG:
  * THE PLANTED GRID MOVES (T13's restated `planted_grid.py`): `interrogate` (a `demanding` row at commit 2) moves with the counterparty's
    skill score, by `opposition_rate` a point; `lie` moves with what the counterparty brings to it -- `lie` names no skill
    (`data/verbs.py::VERB_CAPABILITY` has no row), so every person's score there is the untrained score (`pool.untrained`) and what moves it
    is his opposing attribute (A-137), by `opposition_rate` a point; `speak` under a docketed matter moves with the row's `standard:` (T2),
    the term being the level's size (`difficulty_ob`) and the composed obstacle distinct at each of the four levels the nine rows name.
    NO CELL'S OBSTACLE IS MOVED BY TEMPERAMENT (T13 "What is deliberately not a table": temperament is leverage, CHAR's): the
    counterparty's pursuits -- the axes a territory's temperament is projected onto (`data/pursuits.py::temperament_pursuits`; no person field
    is named temperament) -- swapped for an opposite set leave every cell's obstacle where it was. FALSIFIER (T13): a table whose key
    changes value at the calibrated arm and whose reading changes in no cell is decoration.
  * A BENCH SEAT'S MODIFIER IS ONE LEVEL FOR ITS OWN BENCH ONLY (T4, A-12; T13 edit 5): the shipped `offices.yaml` rows carrying `modifier:`
    are exactly the bench seats -- the rows whose holders `world_q.judging_set` counts as the bench of a rung (a live `hold` Tenure granting
    `state/gate.py::BENCH_BASIS`, the seat's `scope_rung` its ground) -- each `minor`; in the built realm a `speak` through such a seat, in a
    room its bench sits over, carries one `minor` level more than the same speaker through no seat, and through the same seat in a room it
    does not sit over, none. FALSIFIER (T4): the holder's level before his own bench equal to his level before a foreign one; a seat in the
    pool or the opposition.
"""
from __future__ import annotations

import functools

from engine.dice_engine.sigma_leverage import LEVEL_SIGMA
from engine.substrate.descriptors import PURSUITS

from ..data import arrangements as ARR
from ..data import verbs as V
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import roster
from ..queries import world_q
from ..seam.wrappers import pool, sigma
from ..state.gate import BENCH_BASIS, sits_over
from . import test_obstacle_form as TOF
from . import test_sc02_reception as R
from .test_sc01_obstacle_ceiling import _module

#: T13 edit 2 (T2 "First values"), copied: one level per formal layer the row's `interposed:` names among `procedure`, `office`, `document`,
#: `ceremony` (`person`, an advocate, is help, not a layer).
T2_FIRST_VALUES = {"arbitration": "plain", "interrogation": "plain", "negotiation": "plain",
                   "parliamentary_debate": "routine", "council_of_state": "routine", "legal_trial": "routine",
                   "tribunal": "demanding", "excommunication_deliberation": "demanding", "inquisition_hearing": "hard"}
#: T1 row values at commit 2 (T13 edit 7): `interrogate` `demanding`, every other rolled row (the inquiries with them) `routine`.
COMMIT_2_DIFFICULTY = {verb: ("demanding" if verb in ("interrogate", "establish") else "routine") for verb in TOF.ROLLED}   # `establish`: B21.09
#: Two opposite temperaments, as the pursuits a person holds (the realm's projection target).
TEMPERAMENTS = ({PURSUITS[1]: 1.0, PURSUITS[3]: 0.8}, {PURSUITS[4]: 1.0, PURSUITS[5]: 0.9})


def _ob(w, parties, verb, subject, **kw):
    """`(ob, terms, opposition)` of one act's record, through the host builder and the module's own `obstacle`."""
    inp = sigma.contest_input(w, list(parties), verb=verb, subject=subject, **kw)
    ob, terms = _module().obstacle(inp)
    return ob, dict(terms), inp.opposition


def test_planted_grid_moves_lie_interrogate_and_speak():
    sizes = DEFAULT_FIXTURES.get("difficulty_ob")
    rate = float(DEFAULT_FIXTURES.get("opposition_rate"))
    assert {verb: V.VERB_TABLE[verb].difficulty for verb in TOF.ROLLED} == COMMIT_2_DIFFICULTY
    checked = 0

    # interrogate: the counterparty's skill score, from the untrained score up
    w = TOF._world()
    key = V.VERB_CAPABILITY["interrogate"]
    assert key is not None
    floor = pool.untrained(w.fixtures)
    read = []
    for rank in (floor, floor + 1, floor + 3):
        w.persons["p_other"].capability = {key: rank}
        ob, terms, _opp = _ob(w, ["p_low"], "interrogate", "p_other")
        assert terms["difficulty"] == sizes["demanding"], terms
        assert "ceiling" not in terms, (rank, terms)                            # the cap does not swallow the move
        read.append((rank, ob, terms["opposition"]))
        checked += 1
    for (r0, ob0, o0), (r1, ob1, o1) in zip(read, read[1:]):
        assert ob1 > ob0 and abs((o1 - o0) - rate * (r1 - r0)) < 1e-9, read

    # lie: no skill (every person's score is the untrained one), so the counterparty's opposing attribute moves it
    assert V.VERB_CAPABILITY.get("lie") is None and V.VERB_TABLE["lie"].opposed_attribute
    attr = V.VERB_TABLE["lie"].opposed_attribute
    w = TOF._world()
    read = []
    for held in (2, 4, 6):
        w.persons["p_other"].attributes = {attr: held}
        ob, terms, opposition = _ob(w, ["p_low"], "lie", "p_other")
        assert opposition == held + floor and "ceiling" not in terms, (held, opposition, terms)
        read.append((held, ob, terms["opposition"]))
        checked += 1
    for (a0, ob0, o0), (a1, ob1, o1) in zip(read, read[1:]):
        assert ob1 > ob0 and abs((o1 - o0) - rate * (a1 - a0)) < 1e-9, read
    w.persons["p_other"].capability = {"copying": 7, "argue": 7}                 # a held skill moves nothing on a verb that names none
    assert _ob(w, ["p_low"], "lie", "p_other")[0] == read[-1][1]

    # speak: under each of the nine rows, docketed; T2's standard is the row's level's size, and the four levels compose four obstacles
    assert {row: r["standard"] for row, r in ARR.ARRANGEMENTS.items()} == T2_FIRST_VALUES
    by_level: dict = {}
    for row, level in T2_FIRST_VALUES.items():
        h, _d = R._judging_world()
        TOF._docket(h, R.PARTY, row)
        ob, terms, _opp = _ob(h, [R.SPEAKER, R.PARTY], "speak", R.PARTY, room=world_q.place_of(h, R.SPEAKER))
        assert terms.get("standard", 0) == sizes[level], (row, level, terms)
        assert (level == "plain") == ("standard" not in terms), (row, terms)
        by_level.setdefault(level, set()).add(ob)
        checked += 1
    assert all(len(obs) == 1 for obs in by_level.values()), by_level              # one level, one obstacle: the row adds nothing else
    ladder = [by_level[lv].pop() for lv in roster("difficulty_levels", ordered=True)]
    assert ladder == sorted(set(ladder)), ladder                                  # four levels, four distinct obstacles, in order

    # temperament: the counterparty's pursuits move no cell's obstacle
    def cells(pursuits):
        w = TOF._world()
        w.persons["p_other"].pursuits = dict(pursuits)
        w.persons["p_other"].capability = {key: floor + 1}
        h, _d = R._judging_world()
        TOF._docket(h, R.PARTY, "tribunal")
        h.persons[R.PARTY].pursuits = dict(pursuits)
        return (_ob(w, ["p_low"], "interrogate", "p_other")[0], _ob(w, ["p_low"], "lie", "p_other")[0],
                _ob(h, [R.SPEAKER, R.PARTY], "speak", R.PARTY, room=world_q.place_of(h, R.SPEAKER))[0])
    assert cells(TEMPERAMENTS[0]) == cells(TEMPERAMENTS[1])
    checked += 1
    assert checked == 3 + 3 + 9 + 1, checked


@functools.lru_cache(maxsize=None)
def _realm():
    from ..boot.realm import build_realm
    return build_realm(0)


def _bench_seats(w) -> set:
    """The seats whose holders `world_q.judging_set` counts as the bench of a rung: a live `hold` Tenure granting `BENCH_BASIS`, on an Office
    with a ground (`scope_rung`) -- `sits_over` answers nothing for a seat without one."""
    return {t.object for t in w.tenures if t.kind == "hold" and t.live and BENCH_BASIS in t.granted_acts
            and w.offices[t.object].scope_rung is not None}


def test_a_bench_seat_modifier_is_one_level_for_its_own_bench_only():
    from ..data import rosters
    w = _realm()
    authored = {sid: row.get("modifier") for sid, row in rosters.SEAT_ROW_BY_ID.items() if row.get("modifier") is not None}
    benches = _bench_seats(w)
    # B21 left two departures from the rule, named so the pin stays exact: the three ducal seats gained `determine` (B21.53) and so sit a
    # bench with no `modifier:` authored, and the widow regent's remit was emptied (B21.16) so her `modifier:` names no bench. Authoring or
    # removing either moves the realm's content hash (an office's modifier is in it), so neither is done here.
    ducal = {"off_duke_valorsmark", "off_duchess_hafenmark", "off_duke_varfell"}
    assert benches and set(authored) == ((benches & set(rosters.SEAT_ROW_BY_ID)) - ducal) | {"off_widow_regent"}, (sorted(authored), sorted(benches))
    assert ducal <= benches and "off_widow_regent" not in benches, "a named departure ended: author or remove the modifier and drop it from this pin"
    assert set(authored.values()) == {"minor"}, authored
    assert all(w.offices[s].modifier == "minor" for s in authored)
    rungs = sorted({o.scope_rung for o in w.offices.values() if o.scope_rung} | {o.rung for o in w.offices.values() if o.rung})
    holder = {t.object: t.subject for t in w.tenures if t.kind == "hold" and t.live}
    checked = foreign = 0
    for seat in sorted(authored):
        speaker = holder[seat]
        party = next(p for p in sorted(w.persons) if p != speaker)
        own = w.offices[seat].scope_rung
        assert sits_over(w, w.offices[seat], own)
        here = sigma.contest_input(w, [speaker, party], verb="speak", subject=party, room=own, via=seat)
        bare = sigma.contest_input(w, [speaker, party], verb="speak", subject=party, room=own)
        assert abs((here.leverage - bare.leverage) - LEVEL_SIGMA["minor"]) < 1e-9, (seat, here.leverage, bare.leverage)
        assert (here.pool, here.opposition, here.obstacle_operands) == (bare.pool, bare.opposition, bare.obstacle_operands), seat
        checked += 1
        away = next((r for r in rungs if not sits_over(w, w.offices[seat], r)), None)
        if away is not None:                                                      # the realm's root seats sit over every rung it holds
            there = sigma.contest_input(w, [speaker, party], verb="speak", subject=party, room=away, via=seat)
            bare_there = sigma.contest_input(w, [speaker, party], verb="speak", subject=party, room=away)
            assert there.leverage == bare_there.leverage, (seat, away, there.leverage, bare_there.leverage)
            foreign += 1
    assert checked == len(authored) == 7 and foreign >= 5, (checked, foreign)
    other = next(s for s in sorted(rosters.SEAT_ROW_BY_ID) if s not in benches and s in holder)     # a seat that is no bench brings nothing
    speaker = holder[other]
    party = next(p for p in sorted(w.persons) if p != speaker)
    room = w.offices[other].scope_rung or w.offices[other].rung
    assert (sigma.contest_input(w, [speaker, party], verb="speak", subject=party, room=room, via=other).leverage
            == sigma.contest_input(w, [speaker, party], verb="speak", subject=party, room=room).leverage)
