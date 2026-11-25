"""ONE DOOR (B14.11; `03_PC_typed_outcome_one_door` Part B, gate 3): the workbench calls the entry the loop calls.

A workbench trace (`workbench/fight_trace.py::run_traced_fight`) and an entry call (`modules.combat.fight:fight`) on the same
record at the same seed produce the identical event list; `workbench/balance.py::winrate` is the same fights through the
same entry; and no caller binds the engine's `wrapper._TRACE` any more (`wrapper.fight(..., trace=)` binds and restores it).

The workbench modules are loaded BY PATH under their own names, because `workbench/` is not a package and its
directory is kept off `sys.path` here (the former `trace.py`, which shadowed the standard library's `trace`, is `fight_trace.py` since B14.22). The record each entry call fights is built here by hand,
field by field, never through the workbench's own builder, so a builder that reads a Combatant wrongly is seen as a
different event list.
"""
from __future__ import annotations

import importlib.util
import os
import sys

import pytest

from engine.dice_engine import draw
from engine.season.queries.inputs import PersonalCombatInput
from modules.combat import fight as entry
from modules.combat import wrapper
from modules.combat.combatant import Combatant
from modules.combat.config import CFG

_WB = os.path.join(os.path.dirname(__file__), "..", "..", "systems", "combat", "combat_engine_v1", "workbench")
_QS = ("felled", "wounds", "max_wounds", "health_remaining", "health_full")


def _load(name: str, file: str):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_WB, file))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def wb_trace():
    return _load("workbench_trace_under_test", "fight_trace.py")


@pytest.fixture(scope="module")
def wb_balance():
    return _load("workbench_balance_under_test", "balance.py")


# Each matchup is one pair of fighters written twice: as the Combatants the workbench is handed, and as the record the
# entry is handed. `max_bouts`/`cfg`/`terms` ride beside, where the matchup uses them.
def _matchups():
    return [
        dict(name="defaults",
             A=dict(label="A"), B=dict(label="B"),
             rec=dict(claimants=("A", "B"), ends=(4, 4))),
        dict(name="kits, attributes, traditions",
             A=dict(label="A", weapon="spear", armor="medium", tradition="italian", strength=6),
             B=dict(label="B", weapon="dagger", armor="light", tradition="german", end=2),
             rec=dict(claimants=("A", "B"), ends=(4, 2),
                      kits=(("spear", "medium"), ("dagger", "light")), traditions=("italian", "german"),
                      attributes=({"attr.body.strength": 6}, {}))),
        dict(name="the four new fields and a score",
             A=dict(label="A", weapon="katana", tradition="japanese", equipped={"shinogi": 2.0},
                    skills={"grab": 0.5}, disp=6, score=5),
             B=dict(label="B", weapon="arming"),
             rec=dict(claimants=("A", "B"), ends=(4, 4),
                      kits=(("katana", "light"), ("arming", "light")), scores=(5, None),
                      traditions=("japanese", "none"), techniques=({"shinogi": 2.0}, None),
                      axes=({"grab": 0.5}, None), dispositions=(6, None))),
        dict(name="duel terms, a config overlay, a bout cap",
             A=dict(label="A", weapon="arming"), B=dict(label="B", weapon="sabre"),
             rec=dict(claimants=("A", "B"), ends=(4, 4), terms="blood", kits=(("arming", "light"), ("sabre", "light"))),
             terms="blood", cfg=dict(CFG, UPSET_FLOOR=0.5), max_bouts=5),
    ]


def _combatants(m):
    return Combatant(**m["A"]), Combatant(**m["B"])


def _record(m) -> PersonalCombatInput:
    return PersonalCombatInput(wound_quantities=_QS, **m["rec"])


def _raw_events(m, seed):
    """The oracle: the engine called directly on the Combatants, its own `_TRACE` hook set by the test."""
    A, B = _combatants(m)
    seen = []
    wrapper._TRACE = seen.append
    try:
        kw = dict(terms=m["terms"]) if "terms" in m else {}
        result = wrapper.fight(A, B, m.get("cfg"), draw.seeded(draw.H2("fight_trace", seed)), max_bouts=m.get("max_bouts", 12), **kw)
    finally:
        wrapper._TRACE = None
    return result, seen


def test_workbench_trace_and_entry_give_identical_events(wb_trace, monkeypatch):
    calls = []
    real = entry.fight
    monkeypatch.setattr(entry, "fight", lambda *a, **k: (calls.append(1), real(*a, **k))[1])
    checked = 0
    for m in _matchups():
        for seed in range(8):
            out = real(_record(m), draw.seeded(draw.H2("fight_trace", seed)), cfg=m.get("cfg"), max_bouts=m.get("max_bouts"))
            A, B = _combatants(m)
            kw = dict(terms=m["terms"]) if "terms" in m else {}
            result, events = wb_trace.run_traced_fight(A, B, cfg=m.get("cfg"), seed=seed,
                                                       max_bouts=m.get("max_bouts", 12), **kw)
            assert events == list(out.trace), f"{m['name']}: seed {seed}: the workbench's events differ from the entry's"
            raw_result, raw = _raw_events(m, seed)
            assert events == raw, f"{m['name']}: seed {seed}: the entry's events differ from the engine called directly"
            assert result == raw_result, (m["name"], seed, result, raw_result)
            assert len(events) > 0, (m["name"], seed)
            checked += 1
    assert checked >= 32, checked
    # the workbench reached the entry: once per trace, the entry calls here being `real`, which the spy does not see
    assert len(calls) == checked, f"the workbench called the entry {len(calls)} times in {checked} traces"


def test_winrate_is_the_same_fights_through_the_entry(wb_balance, monkeypatch):
    calls = []
    real = entry.fight
    monkeypatch.setattr(entry, "fight", lambda *a, **k: (calls.append(1), real(*a, **k))[1])
    specA, specB = {"weapon": "spear", "tradition": "italian", "strength": 5}, {"weapon": "dagger", "armor": "medium"}
    n = 10
    got = wb_balance.winrate(specA, specB, CFG, n, seed=3)
    assert len(calls) == n, f"winrate called the entry {len(calls)} times in {n} fights"
    # the old route, kept here as the oracle: Combatants fought by `wrapper.fight`, one rng for the sweep
    rng = draw.seeded(draw.H2("balance", 3))
    aw = dec = draws = 0
    for i in range(n):
        swap = i >= n // 2
        X = Combatant("?", **{k: v for k, v in (specB if swap else specA).items() if k not in ("weapon", "armor", "tradition")},
                      weapon=(specB if swap else specA).get("weapon", "arming"),
                      armor=(specB if swap else specA).get("armor", "light"),
                      tradition=(specB if swap else specA).get("tradition", "none"))
        Y = Combatant("?", **{k: v for k, v in (specA if swap else specB).items() if k not in ("weapon", "armor", "tradition")},
                      weapon=(specA if swap else specB).get("weapon", "arming"),
                      armor=(specA if swap else specB).get("armor", "light"),
                      tradition=(specA if swap else specB).get("tradition", "none"))
        r = wrapper.fight(X, Y, CFG, rng)
        r = -r if swap else r
        if r == 1:
            aw += 1; dec += 1
        elif r == -1:
            dec += 1
        else:
            draws += 1
    p, lo, hi = wb_balance._wilson(aw, dec)
    assert got == (p, lo, hi, dec, draws), (got, (p, lo, hi, dec, draws))
    assert dec + draws == n and dec > 0
