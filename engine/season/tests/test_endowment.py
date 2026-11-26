"""B12a.51 (`07_SE_ground_and_granaries` §4 (a), (b), (c) site loop; CP-T08-02): PLACES ARE ENDOWED BY TERRITORY.

`rosters.yaml: site_endowment` says which producing Sites a settlement is given at the world's making, keyed on the geography's territory
(and, past it, on the settlement); `data/fixtures.py::endowment_for` is the one reader and `boot/realm.py::build_realm`'s site loop the one
minter. The fixture `endowment_mode` ships `uniform` (today's placement, `harbour` and `seam` everywhere, THE CONTROL); `ground` is the arm.

THE FALSIFIERS, each able to see what it excludes: a territory's row not reaching the mint (T5 without its fields, T17 with a field); the
`uniform` arm's ids moving (the digest of the realm's whole Site id set, read before the item); a table that lets a territory with a
settlement go unplaced, a kind no roster carries, or an empty list load; an endowment that does not reach `produce` (under `ground` the
settlements still share one hunger band, which is the failure the source plants).
"""

from __future__ import annotations

import hashlib

import pytest

from ..boot.realm import _slug, build_realm
from ..data import fixtures as FX
from ..data.fixtures import DEFAULT_FIXTURES, endowment_for
from ..data.geography import geography
from ..data.rosters import roster
from ..gaps import Forbidden, Ungraded, expect_refusal
from ..harness import populated as POP
from ..harness import probes as P
from ..harness.populated import run
from ..loop.driver import SeasonDriver
from ..queries import world_q

GROUND = DEFAULT_FIXTURES.sweep("endowment_mode", "ground")          # the shipped arm since B12a.54
UNIFORM = DEFAULT_FIXTURES.sweep("endowment_mode", "uniform")        # the control: pinned where a test asserts the uniform arm's placement
PRODUCING = ("harbour", "seam", "field")

# `uniform`'s whole Site id set (every kind, dwellings and garrisons too) as the realm built it BEFORE this item: 322 ids, their md5.
# `reading @198a6c76f`, `build_realm(0)`; the id set is seed-free (the cast moves, the map does not).
UNIFORM_SITE_COUNT, UNIFORM_SITE_DIGEST = 322, "be0fdc38627ca9363fdf146214a2dc36"


def _settlements(territory: str) -> list[str]:
    return [sid for sid, row in geography()["settlements"].items() if row["territory"] == territory]


def _producing_at(w, sid: str) -> list:
    return sorted((s for s in w.sites.values() if s.rung == f"set_{_slug(sid)}" and s.kind in PRODUCING), key=lambda s: s.id)


def test_ground_t5_holds_a_field_and_no_seam():
    w = build_realm(0, fixtures=GROUND)
    checked = 0
    for sid in _settlements("T5"):
        sites = _producing_at(w, sid)
        assert [s.kind for s in sites] == ["field", "field"], (sid, [s.id for s in sites])
        assert [s.id for s in sites] == [f"s_{_slug(sid)}_field", f"s_{_slug(sid)}_field_2"]
        checked += 1
    assert checked >= 3, "the loop asserted nothing: T5 holds no settlement"


def test_ground_t17_holds_a_seam_and_no_field():
    w = build_realm(0, fixtures=GROUND)
    checked = 0
    for sid in _settlements("T17"):
        kinds = [s.kind for s in _producing_at(w, sid)]
        assert kinds == ["seam", "seam"], (sid, kinds)
        checked += 1
    assert checked >= 3, "the loop asserted nothing: T17 holds no settlement"


def test_a_territory_with_a_settlement_and_no_row_refuses_at_load():
    kinds = set(roster("site_kinds"))
    settled = {sid: row["territory"] for sid, row in geography()["settlements"].items()}
    provinces = set(geography()["provinces"])
    ground = dict(FX.SITE_ENDOWMENT["ground"])
    FX._check_site_endowment(FX.SITE_ENDOWMENT["uniform"], ground, {}, kinds, settled, provinces)      # the shipped table loads
    refused = 0
    for name, (uniform, rows, over, exc) in {
        "no row for a territory holding a settlement": (["harbour", "seam"], {t: k for t, k in ground.items() if t != "T5"}, {}, Ungraded),
        "a kind outside site_kinds": (["harbour", "seam"], {**ground, "T5": ["orchard"]}, {}, Forbidden),
        "an empty list": (["harbour", "seam"], {**ground, "T5": []}, {}, Ungraded),
        "an empty uniform list": ([], ground, {}, Ungraded),
        "a territory the map does not carry": (["harbour", "seam"], {**ground, "T99": ["field"]}, {}, Forbidden),
        "a settlement the map does not carry": (["harbour", "seam"], ground, {"S-999": ["field"]}, Forbidden),
    }.items():
        with expect_refusal(), pytest.raises(exc):
            FX._check_site_endowment(uniform, rows, over, kinds, settled, provinces)
        refused += 1
    assert refused == 6


def test_uniform_mints_todays_site_ids():
    w = build_realm(0, fixtures=UNIFORM)
    ids = sorted(w.sites)
    assert (len(ids), hashlib.md5("\n".join(ids).encode()).hexdigest()) == (UNIFORM_SITE_COUNT, UNIFORM_SITE_DIGEST)
    checked = 0
    for sid in geography()["settlements"]:
        assert [s.id for s in _producing_at(w, sid)] == [f"s_{_slug(sid)}_harbour", f"s_{_slug(sid)}_seam"]
        checked += 1
    assert checked >= 37


def test_a_settlement_override_comes_before_its_territory_row(monkeypatch):
    sid = _settlements("T5")[0]
    assert endowment_for(GROUND, sid, "T5") == ("field", "field")
    assert endowment_for(UNIFORM, sid, "T5") == ("harbour", "seam")
    monkeypatch.setattr(FX, "SITE_ENDOWMENT", {**FX.SITE_ENDOWMENT, "settlement": {sid: ("seam",)}})
    assert endowment_for(GROUND, sid, "T5") == ("seam",)
    assert endowment_for(GROUND, _settlements("T5")[1], "T5") == ("field", "field")
    assert endowment_for(UNIFORM, sid, "T5") == ("harbour", "seam")          # the control reads no override


def _bands(w) -> dict:
    return POP.census(w)["hunger_by_settlement"]


def test_ground_reaches_produce_the_settlements_do_not_share_one_band():
    """THE SOURCE'S FALSIFIER: under `ground`, after the first yield, the realm's settlements sit in more than one hunger band (a
    territory of fields yields grain and a territory of seams yields none); under `uniform` they still share one."""
    ground, uniform = build_realm(0, fixtures=GROUND), build_realm(0, fixtures=UNIFORM)
    run(1, 0, w=ground)
    run(1, 0, w=uniform)
    g, u = _bands(ground), _bands(uniform)
    assert sum(g.values()) == sum(u.values()) >= 30
    assert len(g) >= 2, g
    assert len(u) == 1, u


# --- B12a.52: THE TREASURY IS THE GRANARY (`07_SE_treasury_granary_B` §4 (a), (b)) ------------------------------------------------------
def _ground_with(granary_seasons: int):
    # `hunger_severity_draw` False: "every seam cohort fell" would otherwise hold only if no keyed severity draw of the 10 or more is Overwhelming (multiple 0,
    # no fall; about 8% each at the shipped rows), green by luck of the draw; `test_territorial_subsistence.py` pins it the same way.
    return GROUND.sweep("granary_seasons", granary_seasons).sweep("hunger_severity_draw", False)


def _cohorts_by_settlement(w) -> dict:
    """`{set_<slug>: [cohort pid, ...]}` -- every cohort housed at or beneath each settlement rung, by the one reader of homes."""
    homes, out = world_q.home_of(w), {}
    for sid in geography()["settlements"]:
        srid = f"set_{_slug(sid)}"
        out[srid] = sorted(pid for pid, h in homes.items() if w.persons[pid].is_cohort and srid in world_q.ancestry(w, h))
    return out


def _season(w, d=None):
    d = d or SeasonDriver(w)
    d.season(P.NOCHOOSE, question=None)
    return d


def test_every_draw_source_above_a_settlement_is_a_seat_rung():
    """THE FLIP'S GATE (`07_SE_treasury_granary_B` §4 (c), B12a.55), on the SHIPPED realm (`ground`, `granary_seasons` 4; no fixture override), seeds
    0 to 2, two seasons, no acts: every draw cell whose `source` lies ABOVE its settlement names a rung at which an Office sits, and at each seed
    at least one such cell exists. (Red at `granary_seasons` 0: no stock above any settlement, so no cell is drawn from above one.)"""
    checked = 0
    for seed in range(3):
        w = build_realm(seed)
        d, seats, here = None, {o.rung for o in w.offices.values() if o.rung is not None}, 0
        for _ in range(2):
            for home, cells in world_q.subsistence_draw(w).values():      # the draw the stores as they stand give = MATTER's next one (no act writes between)
                chain = world_q.ancestry(w, home)
                above = chain[next(i for i, r in enumerate(chain) if w.rungs[r].kind == world_q.HUNGER_KIND) + 1:]
                for _kind, (_want, _take, src) in cells.items():
                    if src in above:
                        assert src in seats, (seed, home, src, sorted(seats))
                        here += 1
            d = _season(w, d)
        assert here >= 1, f"seed {seed}: no draw reached above its settlement"
        checked += here
    assert checked >= 3, "the loop asserted nothing"


def test_ground_granaries_feed_the_highlands_then_run_down():
    """`07_SE_ground_and_granaries` §5's named test at two seasons (A-114): `granary_seasons` 1 seeds exactly one season of the deficit, so the
    granary empties inside the cap. Seed 0, no acts, weather draw off. Season 0: no cohort under a seam territory is short while its treasury holds
    grain, and the treasury's grain falls; season 1: those cohorts' bodies fall. Control `granary_seasons` 0: they fall from season 0."""
    seam_towns = {f"set_{_slug(sid)}" for sid, row in geography()["settlements"].items()
                  if set(endowment_for(GROUND, sid, row["territory"])) == {"seam"}}
    assert len(seam_towns) >= 10
    w, control = build_realm(0, fixtures=_ground_with(1)), build_realm(0, fixtures=_ground_with(0))
    cohorts, full = _cohorts_by_settlement(w), {pid: p.body for pid, p in w.persons.items() if p.is_cohort}
    seam = {pid for srid in seam_towns for pid in cohorts[srid]}
    treasuries = {world_q.treasury_above(w, srid) for srid in seam_towns}
    grain0 = {t: (w.rungs[t].stores or {}).get("grain", 0) for t in treasuries}
    assert None not in treasuries and all(g > 0 for g in grain0.values()), grain0
    harbour = {pid for sid, row in geography()["settlements"].items() if "harbour" in endowment_for(GROUND, sid, row["territory"])
               for pid in cohorts[f"set_{_slug(sid)}"]}
    d = _season(w)
    assert all(w.persons[pid].body == full[pid] for pid in full) and len(seam) >= 10      # season 0: nobody in the realm is short
    assert all((w.rungs[t].stores or {}).get("grain", 0) < g for t, g in grain0.items()), "no treasury was drawn in season 0"
    _season(w, d)
    assert all(w.persons[pid].body < full[pid] for pid in seam), "the granary is empty and the highlands are still at full body"
    assert len(harbour) >= 15 and all(w.persons[pid].body == full[pid] for pid in harbour), "a harbour cohort fell: its own Sites cover both kinds"
    ccohorts = _cohorts_by_settlement(control)
    _season(control)
    assert all(control.persons[pid].body < full[pid] for srid in seam_towns for pid in ccohorts[srid])
