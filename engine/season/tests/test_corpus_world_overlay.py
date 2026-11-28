"""B12b.20 (`07_SE_arc_needs` (c)): a `FOREIGN_CAST` settlement entry may carry `stores:`, the foreign rung's builder seed.

B12b.21 (`07_SE_arc_needs` (a)): a case file's `world:` block seats a cohort, stocks a larder and mints Sites.
"""
from __future__ import annotations

import pytest
import yaml

from engine.season.boot.realm import COHORT_PREFIX, build_realm
from engine.season.data import files
from engine.season.data.fixtures import SITE_ENDOWMENT
from engine.season.data.rosters import ARMS_KINDS, FOREIGN_CAST, settlement_rung_id
from engine.season.gaps import Forbidden
from engine.season.harness import corpus_run as C
from engine.season.harness import probes as P
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.queries.world_q import capacity

EMPIRE = "Altonia"
SEED = {"grain": 40, "coin": 7}


def _foreign_rung(w):
    return w.rungs[settlement_rung_id(FOREIGN_CAST[EMPIRE]["settlement"]["code"])]


def _authored(rung):
    """The rung's stores less the arms kinds `rosters.yaml: arms_at_build` seeds on every settlement (B18.04): this file reads the `stores:` key, which the
    armoury does not touch."""
    return {k: v for k, v in (rung.stores or {}).items() if k not in ARMS_KINDS}


def test_foreign_stores_key_seeds_the_foreign_rung(monkeypatch):
    monkeypatch.setitem(FOREIGN_CAST[EMPIRE]["settlement"], "stores", dict(SEED))
    w = build_realm(0, foreign=True)
    assert _authored(_foreign_rung(w)) == SEED
    # the seed lands on the foreign rung alone: no realm settlement is handed it
    others = [r for r in w.rungs.values() if r.kind == "settlement" and r is not _foreign_rung(w) and (r.stores or {}).get("coin") == 7]
    assert not others


def test_foreign_cast_without_stores_builds_as_before(monkeypatch):
    shipped = build_realm(0, foreign=True)
    assert not _authored(_foreign_rung(shipped))        # the shipped row carries no key: nothing is seeded
    monkeypatch.setitem(FOREIGN_CAST[EMPIRE]["settlement"], "stores", dict(SEED))
    planted = build_realm(0, foreign=True)
    assert planted.content_hash() != shipped.content_hash()          # the key is read (the control can see a difference)
    _foreign_rung(planted).stores = _foreign_rung(shipped).stores
    assert planted.content_hash() == shipped.content_hash()          # and it writes nothing but that rung's stores


# ---------------------------------------------------------------------------
# B12b.21: a case file's `world:` block
# ---------------------------------------------------------------------------

HOST = {"id": "X-1", "scale": "settlement"}
BLOCK = {"cohort": {"weight": 6}, "stores": {"grain": 8, "salt": 4},
         "sites": ["harbour", {"kind": "dwelling", "count": 6}]}
SETTLEMENT = "r_settlement"


def _build(monkeypatch, block, case=HOST):
    if block is not None:
        monkeypatch.setitem(C.WORLD, case["id"], block)
    return C.build_at(case, 0)


def _load(tmp_path, monkeypatch, block):
    monkeypatch.setattr(files, "EXERCISES_DIR", tmp_path)
    (tmp_path / "X-1.yaml").write_text(yaml.safe_dump({"case": "X-1", "world": block}), encoding="utf-8")
    return C.world_overlay()


def test_world_block_seats_a_cohort_stocks_a_larder_and_mints_sites(monkeypatch):
    w = _build(monkeypatch, BLOCK)
    cohort = w.persons[f"{COHORT_PREFIX}{SETTLEMENT}"]
    assert cohort.weight == 6                                        # seated by `seat_cohorts`, at the settlement rung
    assert w.rungs[SETTLEMENT].stores == {"grain": 8, "salt": 4}     # the larder, a builder's write
    kinds = sorted(s.kind for s in w.sites.values())
    assert kinds == ["dwelling"] * 6 + ["harbour"]                   # `sites:` replaces the uniform endowment: no `seam`
    assert len({s.id for s in w.sites.values()}) == 7                # one id each
    assert capacity(w, SETTLEMENT) == 6                              # the ceiling the cohort was checked against is the dwellings minted
    # played one season, the cohort draws a larder that cannot feed six heads and the shortfall is a claim in someone's ledger
    d = SeasonDriver(w)
    d.season(P.chooser(w, verbs=resolvable_verbs()), question=None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert any(e.kind == "stores.changed" for e in w.log)
    assert any("shortfall" in str(c) for p in w.persons.values() for c in p.ledger)


def test_case_without_world_block_hashes_as_before(monkeypatch):
    plain = C.build_at(HOST, 0)
    assert sorted(plain.sites) == sorted(f"s_{k}" for k in SITE_ENDOWMENT["uniform"])
    assert not any(p.startswith(COHORT_PREFIX) for p in plain.persons) and not plain.rungs[SETTLEMENT].stores
    # naming the endowment's own kinds once each is the world it already was
    same = _build(monkeypatch, {"sites": list(SITE_ENDOWMENT["uniform"])})
    assert same.content_hash() == plain.content_hash()
    # and `stores:` writes that rung's stores and nothing else
    stocked = _build(monkeypatch, {"stores": {"grain": 8}})
    assert stocked.content_hash() != plain.content_hash()
    stocked.rungs[SETTLEMENT].stores = plain.rungs[SETTLEMENT].stores
    assert stocked.content_hash() == plain.content_hash()


REFUSALS = {
    "an unknown key": ({"colour": "red"}, "nothing reads"),
    "a weight of 1": ({"cohort": {"weight": 1}}, "weight"),
    "a float weight": ({"cohort": {"weight": 6.0}}, "weight"),
    "a boolean weight": ({"cohort": {"weight": True}}, "weight"),
    "a cohort with no weight": ({"cohort": {}}, "weight"),
    "a site kind outside site_kinds": ({"sites": ["moat"]}, "site_kinds"),
    "a counted kind outside site_kinds": ({"sites": [{"kind": "moat", "count": 2}]}, "site_kinds"),
    "a zero count": ({"sites": [{"kind": "dwelling", "count": 0}]}, "count"),
    "a float count": ({"sites": [{"kind": "dwelling", "count": 2.5}]}, "count"),
    "a boolean count": ({"sites": [{"kind": "dwelling", "count": True}]}, "count"),
    "a count entry with a stray key": ({"sites": [{"kind": "dwelling", "count": 2, "x": 1}]}, "count"),
    "a kind named twice": ({"sites": ["harbour", {"kind": "harbour", "count": 2}]}, "twice"),
    "stores that are not a mapping": ({"stores": ["grain"]}, "stores"),
    "a stores kind outside matter_kinds": ({"stores": {"unobtainium": 3}}, "matter_kinds"),
    "a negative stores amount": ({"stores": {"grain": -1}}, "stores"),
}


def test_world_block_refuses_an_unknown_key_a_bad_weight_a_bad_kind_a_bad_count_and_a_person_scale_case(tmp_path, monkeypatch):
    assert _load(tmp_path, monkeypatch, BLOCK) == {"X-1": BLOCK}          # the control: a good block loads, so a refusal below is the block's fault
    refused = 0
    for name, (block, words) in REFUSALS.items():
        with pytest.raises(SystemExit, match=words):
            _load(tmp_path, monkeypatch, block)
        refused += 1
    assert refused == len(REFUSALS) >= 10
    monkeypatch.setitem(C.WORLD, "X-1", BLOCK)
    with pytest.raises(SystemExit, match="person"):
        C.build_at({"id": "X-1", "scale": "person"}, 0)
    # the cohort's weight is still checked against the dwellings the block mints: `seat_cohorts` is not bypassed
    monkeypatch.setitem(C.WORLD, "X-1", {"cohort": {"weight": 6}, "sites": [{"kind": "dwelling", "count": 5}]})
    with pytest.raises(Forbidden):
        C.build_at(HOST, 0)
