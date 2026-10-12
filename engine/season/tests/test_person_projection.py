"""v9 PC-06 `S-2` / `L-1` (#445 `03` S-2, `01` L-1): one person's projection (`queries/world_q.py`).

FALSIFIER (the plan's):
  * S-2 -- a claim planted in ANOTHER person's ledger is absent from the projection (and present in
    that other person's, so the plant is observable);
  * L-1 -- the read equals `w.log` filtered by witness. "Witness" is taken from an instrument the
    read does not consult: WITNESS's own `TRACE.claim(holder, event id, source)` row, written at
    every deposit (`loop/witness.py`), so a read that reconstructs the relation wrongly from the log
    disagrees with what the barrier recorded as it happened.
Plus the boundary property S-2 names, *never a `World`*: the projection is a read (the hash does not
move) and a copy (mutating it does not move the hash either).
"""
from __future__ import annotations

import copy

import pytest

from engine.season.gaps import Unspecified
from engine.season.harness import headless
from engine.season.queries.world_q import PersonProjection, projection, witnessed
from engine.season.trace_log import TRACE

SEED, SEASONS = 0, 2


@pytest.fixture(scope="module")
def run():
    """A seeded `headless` run and, per person, the Event ids WITNESS recorded depositing for them."""
    n0 = len(TRACE.rows)
    out = headless.run(SEASONS, SEED)
    by_holder: dict = {}
    for r in TRACE.rows[n0:]:
        if r.channel == "CLAIM":
            holder, _, eid = r.what.partition(" <- ")
            by_holder.setdefault(holder, set()).add(eid)
    return out["world"], by_holder


def test_l1_the_read_equals_the_log_filtered_by_witness(run):
    w, by_holder = run
    cap = w.fixtures.get("ledger_cap")
    # The read is what a person still HOLDS evidence of (eviction emits nothing); the comparison is
    # exact only while no ledger was evicted from, which this seed must satisfy for it to mean anything.
    assert all(len(p.ledger) < cap for p in w.persons.values()), (
        {pid: len(p.ledger) for pid, p in w.persons.items()}, cap)
    reads = {}
    for pid in w.persons:
        want = [e.id for e in w.log if e.id in by_holder.get(pid, set())]
        reads[pid] = [e.id for e in witnessed(w, pid)]
        assert reads[pid] == want, (pid, len(reads[pid]), len(want))
    # §0.1 pt 2: non-vacuous, and PER PERSON -- someone witnessed something, and two persons'
    # reads differ, so a read that ignored the holder (the whole log, or everyone's union) fails.
    assert any(reads.values()), reads
    assert len({tuple(v) for v in reads.values()}) >= 2, {k: len(v) for k, v in reads.items()}
    # The originating Event, never the transport (`occasioned_by`'s rule).
    assert not any(e.kind == "claim.deposited" for pid in w.persons for e in witnessed(w, pid))


def test_s2_a_claim_planted_in_another_ledger_is_absent_from_the_projection(run):
    w0, _ = run
    w = copy.deepcopy(w0)
    me, other = headless.CARIN, headless.BAILIFF
    template = w.persons[other].ledger[0]
    planted = copy.copy(template)
    planted.id, planted.holder, planted.subject = "planted_claim", other, "planted_subject"
    w.persons[other].ledger.append(planted)

    mine = projection(w, me)
    assert isinstance(mine, PersonProjection) and mine.holder == me
    assert [c.id for c in mine.claims] == [c.id for c in w.persons[me].ledger]   # own ledger, in order
    assert mine.claims, "the person holds nothing; absence below would be vacuous"
    assert "planted_claim" not in {c.id for c in mine.claims}
    assert "planted_subject" not in {c.subject for c in mine.claims}
    assert all(c.holder == me for c in mine.claims)
    # The plant is observable: it IS in the projection of the person whose ledger holds it.
    assert "planted_claim" in {c.id for c in projection(w, other).claims}
    assert [e.id for e in mine.witnessed] == [e.id for e in witnessed(w, me)]


def test_s2_the_projection_is_a_read_and_a_copy(run):
    w0, _ = run
    w = copy.deepcopy(w0)
    before = w.content_hash()
    views = [projection(w, pid) for pid in w.persons]
    assert w.content_hash() == before
    mine = next(v for v in views if v.claims and v.witnessed)
    mine.claims[0].value = "mutated by a client"
    mine.claims[0].confidence = -1
    mine.witnessed[0].causes.append("mutated by a client")
    assert w.content_hash() == before, "a client's edit to its projection reached the World"


def test_s2_an_unknown_person_refuses():
    w = headless.build_world(SEED)
    with pytest.raises(Unspecified):
        projection(w, "no_such_person")
