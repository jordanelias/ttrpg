"""`queries/faction_q.py` -- `resolve, holdings, purview, superiors, subordinates, at_war, head`.

What each block proves, and the control that stops it passing vacuously:

  1. THE FIVE FIELDS, AND `proposition` IS THE INPUT ECHOED BACK -- not re-derived, not dropped.
  2. `members` IS THE SAME RULE AS `world_q.members`, NOT A SECOND DEFINITION OF MEMBERSHIP
     (`CLAUDE.md` §8, "every rule lives once"). Asserted by identity, not by equal output --
     two functions that happen to agree today can drift; the same object cannot.
  3. `holdings`/`seats` MATCH AN INDEPENDENTLY-COMPUTED SET, not merely "non-empty". The control
     re-derives membership DIRECTLY from `w.tenures` (`kind == "commit"`), not by calling
     `world_q.members` -- test 2 already proves `faction_q.members IS world_q.members`, so calling
     it again here would make the "independent" control share the exact function whose correctness
     is in question, and a misreading of §14.2 shared by both would cancel out rather than be seen.
  4. VARIATION ACROSS INPUT: two real factions with different membership return different
     `holdings`/`seats`, which a stub returning a fixed list could not do.
  5. `holdings(w, prop)` IS `resolve(w, prop).holdings` -- the standalone Query composes on the
     constructor rather than re-deriving the walk (`CLAUDE.md` §8).
  6. `purview(w, seat)` IS THE SET FORM OF `state/gate.py::purview_reaches` -- asserted as an
     IDENTITY over every rung in a real world, not merely "returns something": for every seat
     that carries a rung, `rung in purview(w, seat)` must equal `purview_reaches(w, off, rung)`
     for EVERY rung in the world, and the rungless/unknown-seat cases both answer `[]`.
  7. `superiors`/`subordinates` READ A HAND-BUILT `oblige` EDGE IN BOTH DIRECTIONS, and
     `subordinates` is asserted equal to `sorted(world_q.establishment_of(...))` -- an identity,
     not a coincidence, since the module composes on that function rather than re-deriving it.
  8. `head` -- F.4's first reader, `Tenure.degree`. FOUR claims, each with its own falsifier:
     (a) the CONTROL: no live `commit` Tenure in a real populated world carries a degree, so
         `head` returns `None` for every faction there -- checked by scanning `w.tenures`
         directly, not merely by calling `head` and trusting it.
     (b) hand-grading ONE live `commit` Tenure with a real `Degree` string makes `head` return
         that Tenure's subject -- the reader is real, not a literal.
     (c) a SECOND, LATER-appended graded `commit` makes `head` return ITS subject -- last write
         wins, `head`'s own documented tie-break (`state/containment.py::home_of`'s precedent).
     (d) closing the later edge (`until` set) drops it out of consideration -- `head` falls back
         to the earlier one, proving the filter is `t.live`, not merely `t.degree is not None`.
  9. `at_war` -- THROUGH THE REAL FOLD, NOT A HAND-PLANTED TENURE. A `utter` Act with
     `payload={"mood": "WAR", "subject": A, "value": B}` followed by a `commit` from the same
     actor to the Proposition it mints are BOTH SHIPPED, UNCONTESTED, `own`-eligible verbs
     (`loop/effects.py::_eff_utter`/`_eff_commit`) -- so this drives `SeasonDriver.resolve` twice,
     the same mechanism `test_governance_build.py`'s LB-1 tests use, rather than constructing a
     `Tenure`/`Proposition` by hand. FOUR observables: the control before the commit is `False`;
     after it, both `at_war(w, A, B)` and the symmetric `at_war(w, B, A)` are `True`; after
     `release`-ing the commit (peace, `T-m`'s own discretion) it is `False` again.
"""
from engine.season.harness.populated import build_realm
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.data.matrix import WriteClass
from engine.season.queries import faction_q, world_q
from engine.season.state.carriers import Act, Tenure
from engine.season.state import gate
from engine.season.state.containment import descendants


def test_resolve_returns_the_five_fields_with_proposition_echoed():
    w = build_realm(0)
    f = faction_q.resolve(w, "fac_crown")
    assert f.proposition == "fac_crown"
    assert set(vars(f)) == {"proposition", "members", "holdings", "seats", "head"}


def test_members_is_world_q_members_not_a_second_definition():
    # Identity, not equality -- `faction_q.py` imports the function object directly.
    assert faction_q.members is world_q.members


def test_holdings_and_seats_match_an_independently_computed_set():
    w = build_realm(0)
    f = faction_q.resolve(w, "fac_crown")
    # ⚠ RE-DERIVED FROM `w.tenures` DIRECTLY, NOT VIA `world_q.members` -- test 2 proves
    # `faction_q.members is world_q.members`, so calling it here would test the code against
    # itself. §14.2: "Membership is `commit`."
    inside = {t.subject for t in w.tenures
              if t.kind == "commit" and t.object == "fac_crown" and t.live
              and t.subject in w.persons}
    assert inside, "fac_crown has no live members in this corpus -- the fixture changed"

    held = [t for t in w.tenures if t.kind == "hold" and t.live and t.subject in inside]
    expect_holdings = sorted({t.object for t in held if t.object in w.rungs})
    expect_seats = sorted({t.object for t in held if t.object in w.offices})

    assert f.holdings == expect_holdings
    assert f.seats == expect_seats
    assert f.holdings, "control is vacuous if Crown holds no territory in this corpus"
    assert f.seats, "control is vacuous if Crown holds no seat in this corpus"


def test_holdings_and_seats_vary_with_membership_not_a_fixed_stub():
    w = build_realm(0)
    crown = faction_q.resolve(w, "fac_crown")
    guilds = faction_q.resolve(w, "fac_guilds")
    assert crown.members != guilds.members
    assert (crown.holdings, crown.seats) != (guilds.holdings, guilds.seats)


def test_holdings_standalone_is_resolve_dot_holdings():
    w = build_realm(0)
    assert faction_q.holdings(w, "fac_crown") == faction_q.resolve(w, "fac_crown").holdings
    assert faction_q.holdings(w, "fac_crown"), "control is vacuous if Crown holds no territory"


def test_purview_is_the_set_form_of_purview_reaches_over_every_seated_office():
    """Test 6. Every office in `build_realm(0)` that carries a rung -- there are three, per this
    corpus's own measured `16 of 19 seats have no rung` -- must agree with `state/gate.py::
    purview_reaches` for EVERY rung in the world, not merely return a non-empty list."""
    w = build_realm(0)
    seated = [(oid, off) for oid, off in w.offices.items() if off.rung is not None]
    assert seated, "no seated office carries a rung in this corpus -- the fixture changed"
    for oid, off in seated:
        pv = faction_q.purview(w, oid)
        expect = sorted({off.rung} | set(descendants(w, off.rung)))
        assert pv == expect, f"{oid}: purview(w, seat) is not `{{rung}} | descendants(rung)`, sorted"
        for rung_id in w.rungs:
            assert (rung_id in pv) == gate.purview_reaches(w, off, rung_id), (
                f"{oid}/{rung_id}: purview(w, seat) and state/gate.py::purview_reaches disagree")


def test_purview_of_a_rungless_or_unknown_seat_is_empty():
    w = build_realm(0)
    rungless = next(oid for oid, off in w.offices.items() if off.rung is None)
    assert faction_q.purview(w, rungless) == []
    assert faction_q.purview(w, "no_such_seat_in_this_world") == []


def test_superiors_and_subordinates_read_a_hand_built_oblige_in_both_directions():
    """Test 7. `H-101`/`§E.1.5`: subordination is an `oblige` edge, never a field. Plants ONE
    live edge directly on `Person.tenures` (the same shape `_eff_oblige` opens, without going
    through the fold, since neither function's own contract requires a computed act) and reads
    it back from BOTH ends."""
    w = build_realm(0)
    seat = next(iter(w.offices))
    person = "p_hand_built_subordinate"
    w.persons[person] = w.persons[next(iter(w.persons))].__class__(person, person)
    t = Tenure(id="hand_oblige_20ii", subject=person, object=seat, kind="oblige", since=0)
    w.persons[person].tenures.append(t)

    assert faction_q.superiors(w, person) == [seat]
    assert person in faction_q.subordinates(w, seat)
    assert faction_q.subordinates(w, seat) == sorted(world_q.establishment_of(w, seat)), (
        "subordinates(w, seat) is not composing on world_q.establishment_of")


def test_superiors_of_a_person_with_no_oblige_is_empty():
    w = build_realm(0)
    assert faction_q.superiors(w, "p_nobody_in_particular") == []


# ---------------------------------------------------------------------------------------------
# `head` -- F.4's first reader. Test 8, four claims, each with its own falsifier.
# ---------------------------------------------------------------------------------------------

def test_head_control_no_live_commit_carries_a_degree_in_a_real_world():
    """(a) THE CONTROL. Scans `w.tenures` directly rather than trusting `head`'s own return --
    `commit`'s row declares `contests: ""` (falsy), so no fold branch this tree ships ever writes
    `Tenure.degree` on one, and the world-builder's opener (`harness/populated.py:690`) mints every
    membership edge with the dataclass default. If this ever finds a graded live commit, `head`'s
    own docstring is wrong about why it is vacuous, which this test would catch first."""
    w = build_realm(0)
    live_commits = [t for t in w.tenures if t.kind == "commit" and t.live]
    assert live_commits, "fixture changed -- no live commit Tenure exists to check at all"
    assert not any(t.degree is not None for t in live_commits), (
        "a live `commit` Tenure now carries a degree -- `head`'s vacuity reasoning is stale")
    for prop in ("fac_crown", "fac_schoenland", "fac_guilds"):
        assert faction_q.resolve(w, prop).head is None
        assert faction_q.head(w, prop) is None


def test_head_reads_a_hand_graded_live_commit():
    """(b) A REAL READER, NOT A LITERAL. Grades ONE live `commit` Tenure to `fac_crown` with a
    real `Degree` string (`FELLED`, combat's own vocabulary -- `head`'s docstring: no cross-domain
    rank is invented, so any non-`None` string must be picked up) and checks `head` names its
    subject."""
    w = build_realm(0)
    t0 = next(t for t in w.tenures if t.kind == "commit" and t.object == "fac_crown" and t.live)
    t0.degree = "FELLED"
    assert faction_q.head(w, "fac_crown") == t0.subject


def test_head_last_write_wins_over_two_graded_live_commits():
    """(c) LAST WRITE WINS -- `head`'s own documented tie-break, `state/containment.py::home_of`'s
    precedent for the identical ambiguity. Grades the FIRST live commit, then appends a SECOND,
    later one for a different member; `head` must name the later one's subject."""
    w = build_realm(0)
    members = world_q.members(w, "fac_crown")
    t0 = next(t for t in w.tenures if t.kind == "commit" and t.object == "fac_crown" and t.live)
    t0.degree = "WON"
    other = next(m for m in members if m != t0.subject)
    t1 = Tenure(id="hand_second_commit_20ii", subject=other, object="fac_crown", kind="commit",
                since=0, degree="LOST")
    w.persons[other].tenures.append(t1)
    assert faction_q.head(w, "fac_crown") == t1.subject


def test_head_a_closed_graded_edge_does_not_count():
    """(d) `t.live` IS THE FILTER, NOT MERELY `degree is not None`. Closing the later edge
    (`until` set -- an owner's own discretion, `T-m`) must drop it, falling back to the earlier
    still-live graded edge."""
    w = build_realm(0)
    members = world_q.members(w, "fac_crown")
    t0 = next(t for t in w.tenures if t.kind == "commit" and t.object == "fac_crown" and t.live)
    t0.degree = "WON"
    other = next(m for m in members if m != t0.subject)
    t1 = Tenure(id="hand_second_commit_closed_20ii", subject=other, object="fac_crown",
                kind="commit", since=0, degree="LOST")
    w.persons[other].tenures.append(t1)
    assert faction_q.head(w, "fac_crown") == t1.subject   # control: still last-write-wins
    t1.until = 5
    assert not t1.live
    assert faction_q.head(w, "fac_crown") == t0.subject


# ---------------------------------------------------------------------------------------------
# `at_war` -- through the real fold. Test 9.
# ---------------------------------------------------------------------------------------------

def _resolve_one(w, d, act):
    out = d.resolve(mint_token(w, WriteClass.ACTS), [act],
                     contest_max_depth=w.fixtures.get("contest_max_depth"))
    return [e.kind for e in out]


def test_at_war_through_the_real_fold_utter_then_commit_then_release():
    w = build_realm(0)
    d = SeasonDriver(w)
    declarer = world_q.members(w, "fac_crown")[0]

    assert faction_q.at_war(w, "fac_crown", "fac_guilds") is False, (
        "control failed -- fac_crown/fac_guilds already read at_war before anything was uttered")

    kinds = _resolve_one(w, d, Act(id="c_20ii_atwar_utter", actor=declarer, verb="utter",
                                   payload={"mood": "WAR", "subject": "fac_crown",
                                            "value": "fac_guilds"}))
    assert kinds == ["proposition.uttered"], f"the WAR utterance did not mint cleanly: {kinds}"
    prop_id = "prop:c_20ii_atwar_utter"
    assert w.propositions[prop_id].mood == "WAR"

    # Not yet at war: the Proposition exists but nobody has committed to it.
    assert faction_q.at_war(w, "fac_crown", "fac_guilds") is False

    kinds = _resolve_one(w, d, Act(id="c_20ii_atwar_commit", actor=declarer, verb="commit",
                                   payload={"subject": prop_id}))
    assert kinds == ["commitment.made"], f"the declaring commit did not mint cleanly: {kinds}"

    assert faction_q.at_war(w, "fac_crown", "fac_guilds") is True
    assert faction_q.at_war(w, "fac_guilds", "fac_crown") is True, (
        "at_war is not symmetric -- {subject, value} must be compared as an unordered pair")

    kinds = _resolve_one(w, d, Act(id="c_20ii_atwar_release", actor=declarer, verb="release",
                                   payload={"subject": prop_id}))
    assert kinds == ["tenure.closed"], f"peace (release) did not close cleanly: {kinds}"

    assert faction_q.at_war(w, "fac_crown", "fac_guilds") is False, (
        "at_war stayed True after the declaring commit was released -- peace is not being read")
    assert faction_q.at_war(w, "fac_guilds", "fac_crown") is False
