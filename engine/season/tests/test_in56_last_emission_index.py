"""IN-56 -- `World.last_emission_of` as a lookup over two maps kept on append, and `EventLog.append`
resolving causes by membership instead of building `_ids | act ids | {ROOT}` on every append.

What each clause observes:

  (a) `test_the_lookup_answers_every_call_as_the_scan_did` -- over `populated.build_realm(0)`'s first
      two seasons, EVERY call `last_emission_of` receives is also put to the scan it used to be
      (`scan_last_emission_of`, copied below as the oracle), in both modes, and the answers are equal.
      Then the end state: for EVERY `(kind, key)` the finished log can be asked about, plus absent
      keys, lookup == scan in both modes. It asserts it compared (>= `MIN_CHECKS`), that some answers
      were not None, that some `written=True` answers were not None, and that the two modes are not
      the same answer everywhere (else the second map is untested). The same run counts the events
      the method iterates: 0.
  (b) `test_a_planted_stale_entry_in_either_map_is_seen` -- the comparison, handed a map with a
      stale id, reports a disagreement (the oracle can observe the failure it excludes).
  (c) The unit clauses: a multi-change Event registers each subject; a later Event with another
      anchor moves only its own key; a probe's direct `w.log.append` is indexed; a deep copy's hook
      is the COPY's; the maps are not folded into `content_hash`.
  (d) The log: an unresolvable cause still refuses (same `Forbidden`, same message); an act id, a
      prior Event id and ROOT pass; the act-id thunk is not evaluated when every cause is already
      resolved (the saving), and is when one is not.

The H-129 falsifier is `test_h206_a_death_at_matter_is_witnessed.py::test_h129_...` and the W4
falsifier is `test_season_shape.py::test_w4_a_claims_decay_walks_back_to_the_act_that_was_witnessed`:
neither is restated here.
"""

from __future__ import annotations

import copy

import pytest

from ..gaps import Forbidden
from ..harness import populated as POP
from ..state.attribution import anchor_of
from ..state.carriers import Act, Event, StateChange
from ..state.gate import Gate
from ..state.ids import ROOT
from ..state.log import EventLog
from ..state.world import World

MIN_CHECKS = 1000


def scan_last_emission_of(w, kind, subject, written=False):
    """THE ORACLE: `World.last_emission_of`'s body before IN-56, verbatim."""
    for e in reversed(w.log):
        if e.kind != kind:
            continue
        if (any(c.subject == subject for c in e.changes) if written
                else anchor_of(w, e) == subject):
            return e.id
    return None


@pytest.fixture(scope="module")
def run():
    """Two seasons of `build_realm(0)` with every call compared to the oracle and the events the
    method iterates counted. Returns the world and the tallies."""
    w = POP.build_realm(0)
    tally = {"calls": 0, "disagreed": [], "nonnull": 0, "nonnull_written": 0,
             "examined": 0, "inside": False}
    real = World.last_emission_of
    oi, orv, og = EventLog.__iter__, EventLog.__reversed__, EventLog.__getitem__

    def counted(it):
        for x in it:
            tally["examined"] += 1
            yield x

    def spy(self, kind, subject, *, written=False):
        tally["inside"] = True
        try:
            got = real(self, kind, subject, written=written)
        finally:
            tally["inside"] = False
        tally["calls"] += 1
        want = scan_last_emission_of(self, kind, subject, written)
        if got != want:
            tally["disagreed"].append((kind, subject, written, got, want))
        tally["nonnull"] += got is not None
        tally["nonnull_written"] += (got is not None and written)
        return got

    def getitem(self, i):
        if tally["inside"]:
            tally["examined"] += 1
        return og(self, i)

    World.last_emission_of = spy
    EventLog.__iter__ = lambda s: counted(oi(s)) if tally["inside"] else oi(s)
    EventLog.__reversed__ = lambda s: counted(orv(s)) if tally["inside"] else orv(s)
    EventLog.__getitem__ = getitem
    try:
        POP.run(2, 0, w=w)
    finally:
        World.last_emission_of = real
        EventLog.__iter__, EventLog.__reversed__, EventLog.__getitem__ = oi, orv, og
    return w, tally


def test_the_lookup_answers_every_call_as_the_scan_did(run):
    w, t = run
    assert t["calls"] >= MIN_CHECKS, f"only {t['calls']} calls compared"
    assert not t["disagreed"], t["disagreed"][:5]
    assert t["nonnull"] > 0, "every answer was None: a comparison of two constants"
    # ⚠ `written=True` finds NOTHING in the realm's two seasons (its only caller is MATTER's death
    # writer and the realm has no MATTER death), so that arm is observed by the end-state keys below
    # and by the H-129 scenario, not here: asserting it here would be a claim this run cannot satisfy.
    # the scan length: the lookup iterates the log not at all
    assert t["examined"] == 0, f"last_emission_of still walked {t['examined']} events"


def test_the_end_state_agrees_for_the_keys_the_log_can_be_asked_about(run):
    """Every key either map holds (a stride over them, the scan being the old cost) plus absent
    keys, in both modes; and the two modes are not the same answer everywhere."""
    w, _ = run
    keys = sorted(set(w._last_by_anchor) | set(w._last_by_subject), key=repr)
    keys = keys[::max(1, len(keys) // 120)] + [("no.such.kind", "x"), ("k", None)]
    keys += [(k, "no_such_subject") for k, _ in keys[:5]]
    compared = differ = nonnull = nonnull_written = 0
    for kind, subj in keys:
        got = {wr: w.last_emission_of(kind, subj, written=wr) for wr in (False, True)}
        for wr in (False, True):
            assert got[wr] == scan_last_emission_of(w, kind, subj, wr), (kind, subj, wr)
            compared += 1
        differ += got[False] != got[True]
        nonnull += any(v is not None for v in got.values())
        nonnull_written += got[True] is not None
    assert compared >= 200 and nonnull > 0
    assert nonnull_written > 0, "no `written=True` answer was an Event: the second map is unobserved"
    assert differ > 0, "the two modes never disagreed: the second map cannot be told from the first"


def test_a_planted_stale_entry_in_either_map_is_seen(run):
    w, _ = run
    w2 = copy.deepcopy(w)
    for mapname, written in (("_last_by_anchor", False), ("_last_by_subject", True)):
        m = getattr(w2, mapname)
        key = next(k for k, v in m.items() if v != w2.log[0].id)
        was = m[key]
        m[key] = w2.log[0].id                                   # the planted stale entry
        assert w2.last_emission_of(key[0], key[1], written=written) != \
            scan_last_emission_of(w2, key[0], key[1], written), \
            f"a stale entry in {mapname} is invisible to the oracle comparison"
        m[key] = was
        assert w2.last_emission_of(key[0], key[1], written=written) == \
            scan_last_emission_of(w2, key[0], key[1], written)


def test_the_h129_scenario_every_call_agrees_and_a_written_answer_is_found():
    """The real fold kills p_high (anchor: his killer), then the killer dies at MATTER. Every
    `last_emission_of` call MATTER makes is compared to the scan, and the victim's death is then
    found by `written=True` (non-None) while the default read of the same key is None."""
    from .test_h206_a_death_at_matter_is_witnessed import _fight_until_he_dies
    from ..data.matrix import Step, WriteClass
    from ..loop.driver import SeasonDriver, mint_token
    got = _fight_until_he_dies()
    assert got is not None, "no act id in range killed p_high; the scenario would be vacuous"
    w, evs = got
    victim_death = next(e for e in evs if e.kind == "person.died")
    seen = []
    real = World.last_emission_of

    def spy(self, kind, subject, *, written=False):
        r = real(self, kind, subject, written=written)
        assert r == scan_last_emission_of(self, kind, subject, written), (kind, subject, written)
        seen.append(r)
        return r

    World.last_emission_of = spy
    try:
        w.step = Step.MATTER
        w.fixtures = w.fixtures.sweep("illness_rate", 1.0)
        SeasonDriver(w).matter(mint_token(w, WriteClass.MATTER), [])
        assert seen, "MATTER asked nothing; the comparison was vacuous"
        assert w.last_emission_of("person.died", "p_high", written=True) == victim_death.id
        assert w.last_emission_of("person.died", "p_high") is None      # anchored on the killer
    finally:
        World.last_emission_of = real


# -- the unit clauses ---------------------------------------------------------------------------

def _w():
    return World(0)


def _ev(w, eid, kind, subjects, causes=(ROOT,)):
    """An Event whose changes name `subjects`, bare `StateChange`s (the log admits them)."""
    return Event(id=eid, kind=kind,
                 changes=[StateChange(s, "set", "MATTER", "f") for s in subjects],
                 causes=list(causes), emitted_at=0)


def test_an_event_with_several_changes_registers_each_subject_and_a_later_one_moves_only_its_key():
    w = _w()
    w.log.append(_ev(w, "e1", "k", ["a", "b"]))
    assert w.last_emission_of("k", "a", written=True) == "e1"
    assert w.last_emission_of("k", "b", written=True) == "e1"
    # the anchor is the FIRST change's subject, as `anchor_of` says, so `b` is not an anchor
    assert w.last_emission_of("k", "a") == "e1" and w.last_emission_of("k", "b") is None
    w.log.append(_ev(w, "e2", "k", ["b"], causes=["e1"]))
    assert w.last_emission_of("k", "b", written=True) == "e2"
    assert w.last_emission_of("k", "a", written=True) == "e1"     # untouched
    assert w.last_emission_of("k", "b") == "e2" and w.last_emission_of("k", "a") == "e1"
    for kind, subj, wr in (("k", "a", True), ("k", "b", True), ("k", "a", False), ("k", "b", False)):
        assert w.last_emission_of(kind, subj, written=wr) == scan_last_emission_of(w, kind, subj, wr)


def test_an_act_caused_event_is_indexed_by_its_actor_and_written_by_what_it_changed():
    """H-129's shape in miniature: the fold-style Event anchors on the ACTOR (tier 1) but WROTE the
    victim. The default read finds the actor; `written=True` finds the victim."""
    w = _w()
    w.acts.append(Act(id="act1", actor="killer", verb="fight"))
    w.log.append(_ev(w, "d1", "person.died", ["victim"], causes=["act1"]))
    assert w.last_emission_of("person.died", "killer") == "d1"
    assert w.last_emission_of("person.died", "victim") is None
    assert w.last_emission_of("person.died", "victim", written=True) == "d1"
    assert w.last_emission_of("person.died", "killer", written=True) is None


def test_a_direct_log_append_is_indexed_as_a_write_would_be():
    """The probes' and the barriers' `w.log.append` / `extend` do not pass through a World method."""
    w = _w()
    w.log.extend([_ev(w, "x1", "k", ["s"]), _ev(w, "x2", "k", ["s"], causes=["x1"])])
    assert w.last_emission_of("k", "s") == "x2" and w.last_emission_of("k", "s", written=True) == "x2"


def test_a_deep_copy_indexes_into_the_copy_not_the_original():
    w = _w()
    w.log.append(_ev(w, "e1", "k", ["s"]))
    c = copy.deepcopy(w)
    c.log.append(_ev(c, "e2", "k", ["s"], causes=["e1"]))
    assert c.last_emission_of("k", "s") == "e2"
    assert w.last_emission_of("k", "s") == "e1", "a deep copy's append wrote the ORIGINAL's index"


def test_the_maps_are_not_folded_into_the_content_hash():
    a, b = _w(), _w()
    a.log.append(_ev(a, "e1", "k", ["s"]))
    b.log.append(_ev(b, "e1", "k", ["s"]))
    b._last_by_anchor[("junk", "junk")] = "junk"
    b._last_by_subject[("junk", "junk")] = "junk"
    assert a.content_hash() == b.content_hash()


# -- the log: membership, not a union -------------------------------------------------------------

def _lev(eid, causes):
    return Event(id=eid, kind="k", changes=[], causes=list(causes), emitted_at=0)


def test_an_unresolvable_cause_still_refuses_with_the_same_forbidden_and_message():
    log = EventLog(Gate(), lambda: frozenset({"act_1"}))
    log.append(_lev("e1", [ROOT]))
    with pytest.raises(Forbidden) as ei:
        log.append(_lev("e2", ["e1", "act_1", "ghost", ROOT, "ghost2"]))
    assert "names cause(s) that resolve to nothing: ['ghost', 'ghost2']" in str(ei.value)
    assert len(log) == 1


def test_act_id_prior_event_and_root_each_pass():
    log = EventLog(Gate(), lambda: frozenset({"act_1"}))
    log.append(_lev("e1", ["act_1"]))
    log.append(_lev("e2", ["e1"]))
    log.append(_lev("e3", [ROOT]))
    assert [e.id for e in log] == ["e1", "e2", "e3"]


def test_the_act_id_thunk_is_read_only_when_a_cause_is_not_already_resolved():
    calls = []
    log = EventLog(Gate(), lambda: calls.append(1) or frozenset({"act_1"}))
    log.append(_lev("e1", [ROOT]))
    log.append(_lev("e2", ["e1", ROOT]))
    assert calls == [], "the thunk was evaluated for causes that were ROOT or prior ids"
    log.append(_lev("e3", ["act_1"]))
    assert calls == [1]


def test_the_on_append_hook_runs_after_each_admitted_append_and_not_after_a_refusal():
    seen = []
    log = EventLog(Gate(), None, seen.append)
    log.append(_lev("e1", [ROOT]))
    with pytest.raises(Forbidden):
        log.append(_lev("e2", ["ghost"]))
    assert [e.id for e in seen] == ["e1"]
