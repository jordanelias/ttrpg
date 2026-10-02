"""Plan position `17-cast` -- a `cast:` entry's `office:` and `ought:`, and the refusal of `knows:`.

What each test proves, and the failure it can observe:

  (a) `office:` is SEATED: a cast entry's block builds an `Office` through `corpus_run._seat_office`
      (the one constructor of an overlay's office) and the person holds it; a case-level
      `scale: office:` goes through the same function and is unchanged. A MUTATION (the seater made
      a no-op) turns the assertion false, so the test can see an `office:` that reads nothing.
  (b) `ought:` is SEATED: `{about, predicate}` becomes THAT entry's OUGHT Proposition on the same
      id and the same `commit` edge the rotation default uses, so `person_q.ambitions` finds it with
      no new reader; entries without one keep the rotation default byte for byte. A MUTATION (the
      referent resolver pointed at the wrong seat) moves the subject, so the test sees an OUGHT
      about the wrong person. Q4 fires for more propositions on a 4-seat cast than on the floor's 3.
  (c) A MALFORMED entry refuses AT LOAD with a named error -- each shape alone, with a positive
      control (a good cast loads), so a loader that refused everything cannot pass.
  (d) `knows:` is REFUSED BY NAME: no builder here constructs a `Claim` (AX-7 limits the sites),
      so a parsed-and-ignored field would tell an author a belief was seated.
  (e) The REAL overlays: every authored `office:` is held and every authored `ought:` lands as a live
      ambition about the person it names, with `checked >= 1` so the loop cannot pass by being empty.
"""
import pytest
import yaml

from engine.season.harness import corpus_run as C
from engine.season.harness import run_cases as RC
from engine.season.queries import person_q, world_q
from engine.season.data.rosters import RUNG_KINDS, TITLE_DOMAINS
from engine.season.gaps import Forbidden

OFFICE = {"post": "surveyor", "body": "Guild", "remit": [],
          "why": "the case names the post and the institution"}


def _host_case() -> dict:
    """A representable NPC case with no overlay, other than `NPC-020` (the no-overlay control)."""
    for c in RC.load_cases("NPC"):
        c = C.apply_rescale(c)
        if (str(c.get("scale")) in set(RUNG_KINDS) and c["id"] not in C.CAST
                and c["id"] != "NPC-020"):
            return c
    raise AssertionError("no representable overlay-free NPC case")


def _cast(*extra: dict) -> list:
    """Four seated people, `who` = A..D, the extras merged into the entry of the same index."""
    es = [{"who": n, "role": "protagonist" if n == "A" else "ally"} for n in "ABCD"]
    for i, e in enumerate(extra):
        es[i].update(e)
    return es


def _build(monkeypatch, entries):
    case = _host_case()
    monkeypatch.setitem(C.CAST, case["id"], entries)
    return case, C.build_at(case, 0)


# ---------------------------------------------------------------------------
# (a) `office:`
# ---------------------------------------------------------------------------

def _held(w) -> dict:
    return {t.subject: w.offices[t.object] for t in w.tenures
            if t.kind == "hold" and t.object in w.offices}


def test_a_cast_entrys_office_is_held_by_that_person_and_by_no_other(monkeypatch):
    case, w = _build(monkeypatch, _cast({}, {"office": OFFICE}))
    held = _held(w)
    assert list(held) == ["p_b"], held
    o = held["p_b"]
    assert (o.post, o.body, o.faction, o.remit_acts) == ("surveyor", "Guild", "Guilds", [])
    assert o.id == f"off_{case['id']}_p_b"
    # CONTROL: the same cast with no `office:` seats none.
    _, w0 = _build(monkeypatch, _cast())
    assert w0.offices == {} and _held(w0) == {}


def test_a_mutation_making_office_read_nothing_is_seen(monkeypatch):
    _, honest = _build(monkeypatch, _cast({}, {"office": OFFICE}))
    monkeypatch.setattr(C, "_seat_office", lambda *a, **k: None)
    _, mutated = _build(monkeypatch, _cast({}, {"office": OFFICE}))
    assert _held(honest) and not _held(mutated)


def test_the_case_level_office_still_goes_through_the_same_seater(monkeypatch):
    case = dict(_host_case(), office=dict(OFFICE, post="chair"))
    monkeypatch.setitem(C.CAST, case["id"], _cast({}, {"office": OFFICE}))
    w = C.build_at(case, 0)
    assert {pid: o.post for pid, o in _held(w).items()} == {"p_a": "chair", "p_b": "surveyor"}
    assert sorted(w.offices) == [f"off_{case['id']}", f"off_{case['id']}_p_b"]


def test_the_first_cast_entry_may_not_carry_an_office_beside_a_case_level_one(monkeypatch):
    """The case-level `scale: office:` is held by `p_a`, who is the first SEATED entry, so an
    `office:` on that entry seats `p_a` twice -- and `exercised_seat` takes the first, so the second
    is inert while looking authored. Only a comment in `NPC-038.yaml` guarded it. The hand-built
    case below carries both; it must refuse, naming the case and the seat. CONTROLS, so a builder
    that refused every office-bearing cast cannot pass: the same entry with no case-level office
    seats it; and the case-level office with the entry's office on a LATER entry seats both."""
    host = _host_case()
    case = dict(host, office=dict(OFFICE, post="chair"))
    monkeypatch.setitem(C.CAST, host["id"], _cast({"office": OFFICE}))
    with pytest.raises(Forbidden) as red:
        C.build_at(case, 0)
    assert host["id"] in str(red.value) and "`p_a`" in str(red.value), str(red.value)

    assert {p: o.post for p, o in _held(C.build_at(host, 0)).items()} == {"p_a": "surveyor"}
    monkeypatch.setitem(C.CAST, host["id"], _cast({}, {"office": OFFICE}))
    assert {p: o.post for p, o in _held(C.build_at(case, 0)).items()} == {
        "p_a": "chair", "p_b": "surveyor"}


def _titled(post: str) -> dict:
    return {"post": post, "faction": "Crown", "why": "the case names the post"}


def test_a_titled_post_must_stand_at_the_rung_kind_its_title_governs(monkeypatch):
    """`populated.seat_anchor` refused a Duke at a hearth; the corpus builder of the same offices did
    not, so `office: {post: Duke, faction: Crown}` seated one. Both now ask
    `rosters.refuse_a_titled_post_off_its_rung`. Observed on BOTH callers (a cast entry's `office:`
    and a case-level one), over EVERY title the ladder has (counted, so a loop that never ran
    cannot pass), against the controls: the title that governs the rung it stands at seats, and a
    post that is no title (an organ) seats at any rung. ONE host case throughout: `_build` picks a
    fresh no-overlay case on every call once an earlier one is in `C.CAST`, and the rung kind an
    overlay's office stands at is the case's own scale."""
    host = _host_case()

    def cast_build(post):
        monkeypatch.setitem(C.CAST, host["id"], _cast({}, {"office": _titled(post)}))
        return C.build_at(host, 0)

    def case_build(post):
        monkeypatch.delitem(C.CAST, host["id"], raising=False)
        return C.build_at(dict(host, office=_titled(post)), 0)

    probe = C.build_at(dict(host, office=OFFICE), 0)         # a non-title: stands wherever it is put
    (office,) = probe.offices.values()
    kind = probe.rungs[office.rung].kind                     # the rung kind an overlay's office gets
    wrong = sorted(t for t, d in TITLE_DOMAINS.items() if d != kind)
    right = sorted(t for t, d in TITLE_DOMAINS.items() if d == kind)
    assert len(wrong) >= 5 and len(right) >= 1, (kind, wrong, right)

    refused = 0
    for post in wrong:
        for build in (cast_build, case_build):
            with pytest.raises(Forbidden) as red:
                build(post)
            assert post in str(red.value), str(red.value)
            assert f"title governs a {TITLE_DOMAINS[post]!r}" in str(red.value), str(red.value)
        refused += 1
    assert refused == len(wrong)

    for post in right + ["Dicastery"]:               # CONTROLS: the governed kind, and a non-title
        assert _held(cast_build(post))["p_b"].post == post, post
        assert _held(case_build(post))["p_a"].post == post, post


# ---------------------------------------------------------------------------
# (b) `ought:`
# ---------------------------------------------------------------------------

def _ambition(w, pid):
    ids = person_q.ambitions(w.persons[pid], w.propositions)
    assert len(ids) == 1, ids
    return w.propositions[ids[0]]


def test_an_authored_ought_replaces_the_rotation_default_for_that_entry_only(monkeypatch):
    case = _host_case()
    # A's default would be about B (the next seat); the author says D, so the two cannot be confused.
    _, w = _build(monkeypatch, _cast({"ought": {"about": "D", "predicate": "keeps faith"}}))
    mine = _ambition(w, "p_a")
    assert (mine.id, mine.mood, mine.subject, mine.predicate) == \
        ("prop_p_a", "OUGHT", "p_d", "keeps faith")
    # The edge is the rotation's own: one live `commit`, id and kind unchanged.
    assert [t.object for t in w.persons["p_a"].tenures if t.kind == "commit"] == ["prop_p_a"]
    # Every OTHER seat is the rotation default, with the case's own `wants_of`.
    for i, pid in enumerate(["p_b", "p_c", "p_d"], start=1):
        p = _ambition(w, pid)
        assert p.subject == ["p_c", "p_d", "p_a"][i - 1] and p.predicate == RC.wants_of(case), pid


def test_no_ought_anywhere_is_the_rotation_for_every_seat(monkeypatch):
    case, w = _build(monkeypatch, _cast())
    subjects = [_ambition(w, pid).subject for pid in ("p_a", "p_b", "p_c", "p_d")]
    assert subjects == ["p_b", "p_c", "p_d", "p_a"]
    assert {_ambition(w, pid).predicate for pid in w.persons} == {RC.wants_of(case)}


def test_a_mutation_pointing_the_referent_at_the_wrong_seat_is_seen(monkeypatch):
    ought = {"ought": {"about": "D", "predicate": "keeps faith"}}
    _, honest = _build(monkeypatch, _cast(ought))
    monkeypatch.setattr(C, "_referent", lambda seated, entry: 1)
    _, mutated = _build(monkeypatch, _cast(ought))
    assert _ambition(honest, "p_a").subject == "p_d" != _ambition(mutated, "p_a").subject


def test_q4_fires_for_more_propositions_on_a_four_seat_cast_than_on_the_floor(monkeypatch):
    def need(w):
        return {q.about for p in w.persons.values() for q in world_q.questions_for(w, p)
                if q.source == "need"}
    case = _host_case()
    pre = need(C.build_at(case, 0))
    _, w = _build(monkeypatch, _cast({"ought": {"about": "D", "predicate": "keeps faith"}}))
    post = need(w)
    assert pre == {"prop_p_a", "prop_p_b", "prop_p_c"}
    assert post == {"prop_p_a", "prop_p_b", "prop_p_c", "prop_p_d"} and len(post) > len(pre)
    # and the Question's referent is the AUTHORED person (`p_d`), not the rotation's (`p_b`).
    qs = [q for q in world_q.questions_for(w, w.persons["p_a"]) if q.source == "need"]
    assert [(q.about, q.referents) for q in qs] == [("prop_p_a", ("p_d",))]


# ---------------------------------------------------------------------------
# (c) a malformed entry refuses at load; (d) `knows:` is refused by name
# ---------------------------------------------------------------------------

def _load(tmp_path, monkeypatch, entries):
    monkeypatch.setattr(C.files, "EXERCISES_DIR", tmp_path)
    (tmp_path / "X-1.yaml").write_text(yaml.safe_dump({"case": "X-1", "cast": entries}),
                                       encoding="utf-8")
    return C.cast_overlay()


def test_a_good_cast_with_office_and_ought_loads(tmp_path, monkeypatch):
    es = _cast({"ought": {"about": "B", "predicate": "p"}}, {"office": OFFICE})
    es.append({"who": "the player", "role": "WAITS-ON-PLAYER"})
    assert _load(tmp_path, monkeypatch, es) == {"X-1": es}


REFUSALS = {
    "an unknown key": ({"colour": "red"}, "keys nothing reads"),
    "knows:": ({"knows": [{"subject": "x", "predicate": "y", "value": 1}]}, "knows"),
    "an ought that is not a mapping": ({"ought": "B"}, "`ought:` is exactly"),
    "an ought with an extra key": ({"ought": {"about": "B", "predicate": "p", "why": "z"}},
                                   "`ought:` is exactly"),
    "an ought with no predicate": ({"ought": {"about": "B"}}, "`ought:` is exactly"),
    "an ought with an empty about": ({"ought": {"about": " ", "predicate": "p"}},
                                     "`ought:` is exactly"),
    "an ought about oneself": ({"ought": {"about": "A", "predicate": "p"}}, "names 0 other"),
    "an ought about nobody in the cast": ({"ought": {"about": "Zed", "predicate": "p"}},
                                          "names 0 other"),
    "an ought about a player": ({"ought": {"about": "the player", "predicate": "p"}},
                                "names 0 other"),
    "an office with no why": ({"office": {"post": "p", "faction": "Crown"}}, "no `why:`"),
    "an office with no post": ({"office": {"why": "w", "faction": "Crown"}}, "no `post:`"),
    "an office naming neither body nor faction": ({"office": {"post": "p", "why": "w"}},
                                                  "neither a `body` nor a `faction`"),
    "an office whose faction contradicts its body": (
        {"office": {"post": "p", "why": "w", "body": "Cardinal of Justice", "faction": "Crown"}},
        "belongs to"),
    "an office remit act off the roster": (
        {"office": {"post": "p", "why": "w", "faction": "Crown", "remit": ["smite"]}},
        "remit acts not on the roster"),
}


@pytest.mark.parametrize("label", sorted(REFUSALS))
def test_each_malformed_entry_refuses_at_load_with_a_named_error(tmp_path, monkeypatch, label):
    bad, needle = REFUSALS[label]
    es = _cast(bad)
    with pytest.raises(SystemExit) as red:
        _load(tmp_path, monkeypatch, es)
    assert needle in str(red.value), (label, str(red.value))


def test_two_people_with_one_name_make_an_ought_about_it_refuse(tmp_path, monkeypatch):
    es = _cast({"ought": {"about": "C", "predicate": "p"}})
    es[3]["who"] = "C"
    with pytest.raises(SystemExit) as red:
        _load(tmp_path, monkeypatch, es)
    assert "names 2 other" in str(red.value)


def test_a_waiting_entry_cannot_carry_what_nothing_will_read(tmp_path, monkeypatch):
    # `capability` joined at the Batch C close: a WAITS-ON-PLAYER entry is never seated, so the
    # field would read nothing, exactly as `office:`/`ought:` would
    refused = 0
    for field, val in (("office", OFFICE), ("ought", {"about": "A", "predicate": "p"}),
                       ("capability", {"copying": 3})):
        es = _cast() + [{"who": "the player", "role": "WAITS-ON-PLAYER", field: val}]
        with pytest.raises(SystemExit) as red:
            _load(tmp_path, monkeypatch, es)
        assert "WAITS-ON-PLAYER" in str(red.value), field
        refused += 1
    assert refused == 3
    # POSITIVE CONTROL: the same `capability` on a SEATED entry loads, and so does a waiting entry
    # that carries nothing -- so the refusal above is the WAITS clause and not a blanket one
    seated = _cast()
    seated[0] = dict(seated[0], capability={"copying": 3})
    es = seated + [{"who": "the player", "role": "WAITS-ON-PLAYER"}]
    assert _load(tmp_path, monkeypatch, es) == {"X-1": es}


@pytest.mark.parametrize("shape", [{"who": "A", "role": "protagonist"}, None, "A"],
                         ids=["a mapping", "an empty key", "a string"])
def test_a_cast_that_is_not_a_list_refuses_at_load_instead_of_being_dropped(
        tmp_path, monkeypatch, shape):
    """A mapping (or a block missing its `- `, or an empty `cast:`) used to fall through the
    `isinstance(list)` filter and be DROPPED, so the case seated the three anonymous people it had
    a cast written to replace. It names the file and the type now."""
    with pytest.raises(SystemExit) as red:
        _load(tmp_path, monkeypatch, shape)
    assert "X-1.yaml" in str(red.value) and "not a list" in str(red.value), str(red.value)


def _write_files(tmp_path, monkeypatch, **docs):
    """`{file stem: doc}` written into a throwaway exercises directory the loader is pointed at."""
    monkeypatch.setattr(C.files, "EXERCISES_DIR", tmp_path)
    for stem, doc in docs.items():
        (tmp_path / f"{stem}.yaml").write_text(yaml.safe_dump(doc), encoding="utf-8")


@pytest.mark.parametrize("doc", [
    {"case": None, "cast": _cast()}, {"case": "", "cast": _cast()}, {"case": "  ", "cast": _cast()},
    {"case": 7, "cast": _cast()}, {"case": ["X-1"], "cast": _cast()}, {"cast": _cast()},
    {"cse": "X-1", "cast": _cast()}],
    ids=["null", "empty", "blank", "an int", "a list", "no case key", "a misspelled key"])
def test_a_cast_file_with_no_usable_case_refuses_at_load_instead_of_being_dropped(
        tmp_path, monkeypatch, doc):
    """`cast_overlay` used to read `if not doc.get("case") or "cast" not in doc: continue`, so a
    file whose `case:` was blank, missing or misspelled vanished and its case seated the three
    anonymous people its author had written a cast to replace."""
    _write_files(tmp_path, monkeypatch, **{"X-1": doc})
    with pytest.raises(SystemExit) as red:
        C.cast_overlay()
    assert "X-1.yaml" in str(red.value) and "no non-empty string `case:`" in str(red.value), \
        str(red.value)


def test_two_files_naming_one_case_refuse_at_load_instead_of_the_last_one_winning(
        tmp_path, monkeypatch):
    _write_files(tmp_path, monkeypatch, **{"A-1": {"case": "X-1", "cast": _cast()},
                                           "B-1": {"case": "X-1", "cast": _cast()}})
    with pytest.raises(SystemExit) as red:
        C.cast_overlay()
    assert "B-1.yaml" in str(red.value) and "already the case of A-1.yaml" in str(red.value), \
        str(red.value)


def test_the_case_refusals_have_their_positive_controls(tmp_path, monkeypatch):
    """Two files with two cases both load (so a loader that refused every multi-file directory
    cannot pass), and a file with no `cast:` is not a cast file whatever its `case:` -- the
    `scale:` overlays share the directory, and one may name a case a cast file also names."""
    _write_files(tmp_path, monkeypatch,
                 **{"A-1": {"case": "X-1", "cast": _cast()},
                    "B-1": {"case": "X-2", "cast": _cast({"role": "lead"})},
                    "C-1": {"case": "X-1", "scale": {"is": "hearth", "why": "w"}},
                    "D-1": {"note": "neither key"}})
    got = C.cast_overlay()
    assert sorted(got) == ["X-1", "X-2"] and got["X-2"][0]["role"] == "lead", sorted(got)


def test_the_real_overlays_all_still_load_and_a_good_file_is_not_refused(tmp_path, monkeypatch):
    """POSITIVE CONTROLS for the two refusals above: the checked-in overlays load unchanged, and an
    independent read of the same directory finds the same cases (so a loader that refused or dropped
    everything cannot pass), and a valid list-shaped file loads."""
    real = C.cast_overlay()
    independent = sorted(
        doc["case"] for f in sorted(C.files.EXERCISES_DIR.glob("*.yaml"))
        for doc in [yaml.safe_load(f.read_text(encoding="utf-8")) or {}]
        if doc.get("case") and isinstance(doc.get("cast"), list))
    assert sorted(real) == independent and len(real) >= 13, (sorted(real), independent)
    assert _load(tmp_path, monkeypatch, _cast()) == {"X-1": _cast()}


# ---------------------------------------------------------------------------
# (e) the real overlays
# ---------------------------------------------------------------------------

def test_every_authored_office_is_held_and_every_authored_ought_is_a_live_ambition():
    cases = {c["id"]: C.apply_rescale(c) for c in RC.load_cases("NPC")}
    offices = oughts = 0
    for cid, entries in C.CAST.items():
        seated, _ = C.seating(cases[cid])
        w = C.build_at(cases[cid], 0)
        for n, e in enumerate(seated):
            pid = C.seat_ids(len(seated))[n]
            if e.get("office"):
                offices += 1
                assert _held(w)[pid].post == e["office"]["post"], (cid, pid)
            if e.get("ought"):
                oughts += 1
                prop = _ambition(w, pid)
                other = C.seat_ids(len(seated))[C._referent(seated, e)]
                assert (prop.subject, prop.predicate) == (other, e["ought"]["predicate"]), (cid, pid)
                assert w.persons[other].name == e["ought"]["about"], (cid, pid)
    assert offices >= 1 and oughts >= 1, (offices, oughts)
