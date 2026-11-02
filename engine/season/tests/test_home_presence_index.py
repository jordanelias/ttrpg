"""The barrier's HOME index and PRESENCE index (`queries/cache.py::home_index`, `presence_index`) answer
as the live scans they replaced (the IN-54 pattern, `test_in54_tenure_index.py`).

WHY THEY EXIST. One season of `build_realm(0)` called `home_of(w)` (via `place_of`, from WITNESS's co-located
channel) 80,158 times, each call rebuilding the whole map from every Tenure, and built the presence index
with one full `w.tenures` scan per rung. Measured: a season fell from 15.0 s to 6.5 s with the same content
hash (`056584ed...`, the one-season pin) and a byte-identical trace stream (209,999 rows).

What each clause observes, and what it is the falsifier of:

  (a) the home index equals `home_of(w)` on a realm, including a person with TWO live `contain` edges
      (last write wins, as `home_of` says), and `place_of(w, x, homes)` equals `place_of(w, x)` for every
      kind of id (person, site, record, date, rung, and an unknown id).
  (b) `presence_map(w)` equals `{r: presence(w, r)}` rung for rung, list order included.
  (c) a Tenure written between two asks is NOT seen without `discard_caches()` and IS seen after one (the
      index is a per-barrier cache; the barrier is the invalidation). MUTATION (run): make `home_index`
      skip `cache_at_barrier` -> the "stale" half goes red.
  (d) the trace is unchanged: `place_of(w, p, homes)` writes the one `home_of` row `place_of(w, p)` wrote,
      and building `presence_index` writes one `presence` row per rung.

Each loop asserts it checked something (CLAUDE.md 0.1 pt 2).
"""

from __future__ import annotations

from ..harness import populated as POP
from ..queries import cache, world_q
from ..state.carriers import Tenure
from ..trace_log import TRACE


def _rows(name):
    return sum(1 for r in TRACE.rows if r.channel == "QUERY" and r.what == name)


def test_the_home_index_is_home_of_and_place_of_agrees_with_and_without_it():
    w = POP.build_realm(0)
    persons = sorted(w.persons)
    # a person with two live `contain` edges: the later one wins in `home_of`, so it must in the index
    a, rung_a, rung_b = persons[0], sorted(w.rungs)[0], sorted(w.rungs)[1]
    w.add_tenure(Tenure("t_home_idx_a", a, rung_a, "contain", since=0))
    w.add_tenure(Tenure("t_home_idx_b", a, rung_b, "contain", since=0))
    w.discard_caches()
    homes = cache.home_index(w)
    assert homes == world_q.home_of(w), "the home index is not home_of"
    ids = persons + sorted(w.sites) + sorted(w.records) + sorted(w.dates) + sorted(w.rungs)[:50] + ["no_such_id", None]
    checked = 0
    for x in ids:
        assert world_q.place_of(w, x, homes) == world_q.place_of(w, x), f"place_of differs for {x!r}"
        checked += 1
    assert checked >= 100, "the comparison barely ran"
    assert any(world_q.place_of(w, p) is not None for p in persons), "every place was None: a comparison of constants"


def test_the_presence_map_is_presence_per_rung_in_the_same_order():
    w = POP.build_realm(0)
    index = world_q.presence_map(w)
    assert set(index) == set(w.rungs)
    populated = 0
    for r in w.rungs:
        assert index[r] == world_q.presence(w, r), f"presence differs at {r!r}"
        populated += bool(index[r])
    assert populated >= 5, "no rung held anyone: a comparison of empty lists"


def test_a_tenure_written_between_two_asks_is_seen_only_after_a_discard():
    w = POP.build_realm(0)
    p = sorted(w.persons)[0]
    before = cache.home_index(w).get(p)
    target = next(r for r in sorted(w.rungs) if r != before)
    w.add_tenure(Tenure("t_home_idx_move", p, target, "contain", since=0))
    assert cache.home_index(w).get(p) == before, "the index was rebuilt without a barrier: it is not a barrier cache"
    w.discard_caches()
    assert cache.home_index(w).get(p) == target, "after discard_caches() the new edge was not seen"
    assert cache.home_index(w).get(p) == world_q.home_of(w).get(p)


def test_the_trace_stream_is_the_one_the_scans_wrote():
    w = POP.build_realm(0)
    p = sorted(w.persons)[0]
    homes = cache.home_index(w)
    n0 = _rows("home_of")
    world_q.place_of(w, p, homes)
    assert _rows("home_of") - n0 == 1, "place_of(.., homes) must write the one home_of row place_of(..) wrote"
    n0 = _rows("home_of")
    world_q.place_of(w, p)
    assert _rows("home_of") - n0 == 1
    w.discard_caches()
    n1 = _rows("presence")
    cache.presence_index(w)
    assert _rows("presence") - n1 == len(w.rungs), "presence_index must write one presence row per rung"
