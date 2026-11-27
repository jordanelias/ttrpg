"""B12b.20 (`07_SE_arc_needs` (c)): a `FOREIGN_CAST` settlement entry may carry `stores:`, the foreign rung's builder seed.

B12b.21 adds the case-world overlay's tests to this file.
"""
from __future__ import annotations

from engine.season.boot.realm import build_realm
from engine.season.data.rosters import FOREIGN_CAST, settlement_rung_id

EMPIRE = "Altonia"
SEED = {"grain": 40, "coin": 7}


def _foreign_rung(w):
    return w.rungs[settlement_rung_id(FOREIGN_CAST[EMPIRE]["settlement"]["code"])]


def test_foreign_stores_key_seeds_the_foreign_rung(monkeypatch):
    monkeypatch.setitem(FOREIGN_CAST[EMPIRE]["settlement"], "stores", dict(SEED))
    w = build_realm(0, foreign=True)
    assert _foreign_rung(w).stores == SEED
    # the seed lands on the foreign rung alone: no realm settlement is handed it
    others = [r for r in w.rungs.values() if r.kind == "settlement" and r is not _foreign_rung(w) and (r.stores or {}).get("coin") == 7]
    assert not others


def test_foreign_cast_without_stores_builds_as_before(monkeypatch):
    shipped = build_realm(0, foreign=True)
    assert not _foreign_rung(shipped).stores            # the shipped row carries no key: nothing is seeded
    monkeypatch.setitem(FOREIGN_CAST[EMPIRE]["settlement"], "stores", dict(SEED))
    planted = build_realm(0, foreign=True)
    assert planted.content_hash() != shipped.content_hash()          # the key is read (the control can see a difference)
    _foreign_rung(planted).stores = _foreign_rung(shipped).stores
    assert planted.content_hash() == shipped.content_hash()          # and it writes nothing but that rung's stores
