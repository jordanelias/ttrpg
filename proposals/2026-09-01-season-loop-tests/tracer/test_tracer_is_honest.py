"""The instrument's own adversarial test. It exists because THE TRACER GATES EVERY FINDING
DOWNSTREAM: if the instrument flatters the shape, every verdict in both test sets is worth
nothing -- and flattery is the direction nobody notices.

Revision 1 of this instrument was attacked by a read-only antagonist that never saw the
producer's reasoning. THE FIDELITY CLAIM DID NOT SURVIVE. It found ten defects and EVERY ONE
FLATTERED THE SHAPE. Each is pinned below so a recurrence is caught BY A MACHINE RATHER THAN
BY LUCK -- `ARCHITECTURE.md` S0's own discipline, applied to the thing doing the measuring.

Run: python3 -m pytest test_tracer_is_honest.py -q
"""

from __future__ import annotations

import dataclasses
import contextlib
import inspect
import json
import re
import sys
from pathlib import Path

import pytest

import probes as P
import run_cases as R
import shape as S
from shape import (
    Event, Fixtures, Forbidden, Person, Proposition, Query, Rung, Site,
    Step, Tenure, Unspecified, View, World, WriteClass,
)

HERE = Path(__file__).parent
SHAPE_SRC = (HERE / "shape.py").read_text()
PROBES_SRC = (HERE / "probes.py").read_text()



def _code_only(src: str) -> str:
    """Strip comments and docstrings. These tests check CODE, not the prose that DESCRIBES the
    defect -- and this file's own retraction notes quote the defective lines verbatim, so a
    naive substring match fires on the retraction rather than on a recurrence."""
    import io, tokenize
    out, prev_end, prev_tok = [], (1, 0), tokenize.INDENT
    try:
        toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
    except tokenize.TokenError:
        return src
    for tok in toks:
        if tok.type == tokenize.COMMENT:
            continue
        if tok.type == tokenize.STRING and prev_tok in (
                tokenize.INDENT, tokenize.DEDENT, tokenize.NEWLINE, tokenize.NL):
            prev_tok = tok.type
            continue
        out.append(tok.string)
        if tok.type not in (tokenize.NL, tokenize.NEWLINE):
            prev_tok = tok.type
    return " ".join(out)


SHAPE_CODE = _code_only(SHAPE_SRC)
PROBES_CODE = _code_only(PROBES_SRC)

def _w() -> World:
    return P.tiny_world()


# ===========================================================================
# THE TEN REVISION-1 DEFECTS. Each test FAILS if that defect returns.
# ===========================================================================

def test_d1_the_partition_is_not_invented():
    """DEFECT 1. Rev 1 declared TWELVE `social:` rows. ARCHITECTURE.md states exactly ONE
    (S15.3) and declares two MISSING (S30.1). Two invented rows were the precise keys the
    in-chain instrument marks DELIBERATELY ABSENT -- adding them turns a real gap into a PASS."""
    # ⚠ REV 4. This pin ASSERTED THE WRONG NUMBER for three revisions and locked the error in.
    # The head states TWO rows, not one: S15.3's `(Tenure, until)` seam, and S54 item 21's
    # `(Person, scar[axis])`, "social: true, written at RESOLVE in the ACTS class by the outcome
    # that names the person". Omitting the second inverted the sign on a seven-arc finding --
    # the instrument reported the row itself as the thing that does not exist.
    # ⚠ W2 REPLACED THIS PIN, and G3 gives the replacement in as many words: *"the Partition pin
    # becomes 'every non-derived row carries a chain citation'"*. There is no derivation left --
    # Part D is loaded from `write_matrix.yaml`, every row is STATED, and every row carries a
    # `by:`. Pinning the old two-row list would now pin the absence of the ~30 rows Part D adds.
    #
    # `(Person, convictions)` and `(Person, beliefs)` NO LONGER RAISE, and that is Part D closing
    # the gap rather than the instrument flattering it: V2 §D3 gives each its own row -- RESOLVE
    # only, ACTS, `social: true`, DR-2 and §9.3. What must still raise is a field with NO row,
    # and it must not be able to ride on a neighbour's.
    assert S.MATRIX, "the write matrix loaded empty -- nothing was checked"
    for (kind, fname), row in S.MATRIX.items():
        assert row.by.strip(), f"({kind}, {fname}) carries no provenance"
    for kind, fname in (("Person", "convictions"), ("Person", "beliefs")):
        social, by = S.partition_lookup(kind, fname)
        assert social is True and by.strip(), f"({kind}, {fname}) has a row but no usable grade"


def test_d1b_a_field_cannot_ride_on_another_fields_matrix_row():
    """DEFECT 1, second form. The matrix names THINGS, not (kind, field) pairs. Keying the
    derivation on `thing` lets `(Person, convictions)` ride on `stance`'s row."""
    w = _w()
    w.step = Step.RESOLVE
    # W2: `convictions` has its own row now, so the ride-on has to be probed with a field Part D
    # genuinely does not carry. `(Person, mood)` is W2's own planted example, and the `thing`
    # argument is the parameter that CARRIED the defect -- passing `stance` for it must not help.
    with pytest.raises(Unspecified) as e:
        w.write("stance", WriteClass.ACTS, lambda: None,
                record_kind="Person", fieldname="mood", driver="Act")
    assert "Person" in str(e.value) and "mood" in str(e.value), (
        "the refusal did not NAME the pair, so a reader cannot tell which cell is unmarked")


def test_d2_witness_does_not_lie_about_its_driver():
    """DEFECT 2. Rev 1's WITNESS declared driver="Act" for a deposit caused by an Event -- the
    ONE site where the gate would otherwise have fired."""
    src = inspect.getsource(S.SeasonDriver.witness)
    assert 'driver="Event"' in src and 'driver="Act"' not in src


def test_d3_the_write_gate_cannot_be_silenced_by_omission():
    """DEFECT 3. S30.2: 'EITHER THE GATE APPLIES THE WRITE, OR DIRECT ASSIGNMENT IS MADE
    IMPOSSIBLE.' Rev 1 ran L4 only if two optional kwargs were supplied."""
    sig = inspect.signature(S.World.write)
    for name in ("record_kind", "fieldname", "driver"):
        assert sig.parameters[name].default is inspect.Parameter.empty, name


def test_d3b_the_gate_applies_the_write():
    w = _w()
    w.step = Step.MATTER
    site = w.sites["site_harbour"]
    before = site.condition
    # `W4`: a MATTER write on a row that declares an `emits:` kind must name one and must carry
    # an antecedent. `[ROOT]` is said EXPLICITLY here because this synthetic write is the first
    # emission in its world — which is exactly the carve-out, and saying it is the point.
    w.write("condition", WriteClass.MATTER, lambda: setattr(site, "condition", before - 7),
            record_kind="Site", fieldname="condition", driver="Event",
            emits="condition.worn", subject=site.id, causes=[S.ROOT])
    assert site.condition == before - 7
    assert w.log[-1].kind == "condition.worn" and w.log[-1].subject == site.id


def test_d4_contest_is_not_a_second_resolver():
    """DEFECT 4. Rev 1 hardcoded band="Partial" with no margin, guarded the demote-only veto
    with dead code, and named THE MOST RECENT UNRELATED EVENT as its cause -- worse than
    [ROOT], because it yields a plausible, wrong arc graph THAT WALKS."""
    src = _code_only(inspect.getsource(S.contest))
    assert 'band = "' not in src and "band = '" not in src
    assert "w.log [ - 1 ]" not in src and "w.log[-1]" not in src
    with pytest.raises(Unspecified):
        S.contest(_w(), "S", "a prize", ["p_low"], depth=0, max_depth=3, causes=["x"])


def test_d4b_contest_causes_must_be_supplied_and_non_empty():
    with pytest.raises(Forbidden):
        S.contest(_w(), "S", "a prize", ["p_low"], depth=0, max_depth=3, causes=[])


def test_d5_the_budget_is_the_persons_choice_not_an_engine_truncation():
    """DEFECT 5. S26 types budget as (Person, View) -> int with NO World, so `choose` can ask
    its own. Rev 1 gave it a World and then SILENTLY DISCARDED the tail -- an engine deciding
    a person's options, which is L1."""
    sig = inspect.signature(Query.budget)
    assert "w" not in sig.parameters and "world" not in sig.parameters
    w = _w()
    def over(p, v, s, ask_budget):
        return [P.Act_(w, p, f"v{i}") for i in range(ask_budget() + 2)] if p.id == "p_low" else []
    with pytest.raises(Forbidden):
        P._run(w, over)


def test_d6_no_invented_constant_sits_in_a_body():
    """DEFECT 6. Rev 1 had a wear rate uniform across every site kind, a //60, and
    confidence=1 -- all below Fixtures, all outside the sweep."""
    body = SHAPE_CODE.split("DEFAULT_FIXTURES = Fixtures (", 1)[1]
    for bad in ("// 100", "// 60", "confidence = 1 ,"):
        assert bad not in body, bad


def test_d6b_wear_has_no_silent_default():
    """S42.2.1: 'a wear table that returns 20 for an unregistered site kind DOES NOT FAIL --
    it answers, plausibly and wrongly, forever.'"""
    f = Fixtures(wear_per_season={"harbour": 10})
    assert f.wear("harbour") == 10
    with pytest.raises(S.Ungraded):
        f.wear("reliquary")


def test_d7_sense_does_not_return_a_constant_standing():
    """DEFECT 7. Rev 1 returned standing = 0 unconditionally, in the one function S18.2 calls
    the only bridge from world truth into `choose()`.

    ⚠ W5 REPOINTED THIS AT D7'S ACTUAL CLAIM. It had become `pytest.raises(Unspecified)` — which
    pins standing as HAVING NO FORMULA, not as being non-constant — so it went red the moment
    `H-29` supplied one. D7 is about a CONSTANT, and testing that directly is strictly stronger:
    a raise and a hardcoded 0 are both constants, and only one of them was ever the defect."""
    w = _w()
    p = w.persons["p_low"]
    seen = {S.sense(p, w, P.SUBSIST).standing}
    p.ledger.append(S.Claim("c_a", p.id, p.id, "grade", "warden", 0, "firsthand", 100, "own"))
    p.ledger.append(S.Claim("c_b", p.id, p.id, "grade", "warden", 0, "told_by", 100, "own"))
    seen.add(S.sense(p, w, P.SUBSIST).standing)
    assert len(seen) > 1, (
        f"standing returned {seen.pop()} for two materially different ledgers — it is a constant, "
        "which is D7 exactly, whether the constant is 0 or a raise")
    # and it is still the ONE bridge: `sense` computes it, nobody stores it.
    assert not any(f.name == "standing" for f in dataclasses.fields(S.Person)), (
        "`standing` became a field on Person — S18.2 makes it a computed scalar of Sensation, and "
        "a stored one is the aggregate-as-field shape §22.1 complains about")


def test_d8_one_doctrinal_condition_raises_one_kind():
    """DEFECT 8. An unmarked cell is ONE condition (S30/S30.1); rev 1 split it across
    Forbidden and Unspecified, making the kind histogram a measurement of the transcription."""
    w = _w()
    w.step = Step.RESOLVE
    # W2: `thing` no longer keys the gate, so a bogus `thing` with a REAL pair is now lawful --
    # correctly, because `(Rung, stores)` is on the table and `thing` is a trace label. The
    # unmarked cell has to be a real unmarked cell.
    with pytest.raises(Unspecified):
        w.write("stores", WriteClass.ACTS, lambda: None,
                record_kind="Rung", fieldname="no_such_field", driver="Act")
    with pytest.raises(Unspecified):
        S.partition_lookup("Record", "anything")


def test_d9_no_rule_is_written_and_switched_off():
    """DEFECT 9. Rev 1 wrote the knot-deposit rule and disabled it with `if False`."""
    assert "if False" not in SHAPE_CODE and "if False" not in PROBES_CODE


def test_d9b_eviction_ranks_on_the_product_not_lexicographically():
    """S20/S34: eviction ranks on `confidence_live × recency` ONLY. A tuple sort is a different
    comparator and degenerates to insertion order under a constant confidence.

    ⚠ ASSERTED ON THE BEHAVIOUR, NOT ON THE SOURCE TEXT. This read
    `assert "c.confidence * (c.when" in src`, which is `G3` exactly — a string match cannot
    observe a SEMANTIC change, and `W4` made one: before it, `confidence` was pinned at
    `confidence_default` for every claim, so the product was pure recency and the two comparators
    were indistinguishable. Now confidence decays, the product is non-monotonic in age, and a
    claim at confidence 0 is evicted first however recent it is. That is the difference the test
    is supposed to be about, and the string could not see it. Found by the `W4` adversarial pass."""
    ranked = lambda claims: sorted(claims, key=lambda c: c.confidence * (c.when + 1))
    old_and_confident = S.Claim("a", "p", "s", "k", True, when=0, source="f",
                                confidence=100, visibility="own")
    recent_and_spent = S.Claim("b", "p", "s", "k", True, when=9, source="f",
                               confidence=0, visibility="own")
    # THE DISCRIMINATING PAIR. Under the product, the spent claim goes first however recent it is.
    # Under a lexicographic `(confidence, when)` tuple it ALSO goes first — so that pair alone
    # proves nothing, and the second pair below is what separates the two comparators.
    assert ranked([old_and_confident, recent_and_spent])[0] is recent_and_spent
    low_but_ancient = S.Claim("c", "p", "s", "k", True, when=0, source="f",
                              confidence=40, visibility="own")
    high_but_ancient = S.Claim("d", "p", "s", "k", True, when=0, source="f",
                               confidence=41, visibility="own")
    recent_mid = S.Claim("e", "p", "s", "k", True, when=50, source="f",
                         confidence=39, visibility="own")
    got = ranked([recent_mid, high_but_ancient, low_but_ancient])
    assert [c.id for c in got] == ["c", "d", "e"], (
        f"the product ranks {[c.id for c in got]}; a lexicographic (confidence, when) sort would "
        "rank ['e', 'c', 'd'] — the recent mid-confidence claim first. That is the comparator this "
        "test exists to exclude, and it is now excluded by BEHAVIOUR")
    # AND THE LIVE COMPARATOR IS THE ONE MEASURED ABOVE, not a copy of it in this file.
    assert "c.confidence * (c.when" in inspect.getsource(S.SeasonDriver.witness)


def test_d9c_max_depth_has_no_default_anywhere():
    """S39.3: 'the depth cap has NO DEFAULT... a default is a number somebody made up and it
    will be cited later as though it were measured.'"""
    assert "caller_supplied_max_depth" not in SHAPE_CODE
    assert inspect.signature(S.contest).parameters["max_depth"].default is inspect.Parameter.empty
    w = _w()
    def fight(p, v, s, ask_budget):
        return [P.Act_(w, p, "fight", contests=["x"], payload="S")] if p.id == "p_low" else []
    with pytest.raises(Forbidden):
        P._run(w, fight)


def test_d9d_the_frozen_world_is_read_not_merely_written():
    """S32 rest 1 is the FIRST thing order-independence rests on. Rev 1 set w.frozen and
    nothing ever read it."""
    with pytest.raises(Forbidden):
        S.SeasonDriver(_w()).deliberate(lambda p, v, s, ask_budget: [], None, P.SUBSIST)


def test_d9e_the_rung_guard_is_a_whitelist_not_a_blacklist():
    """DEFECT 9. Rev 1 blacklisted six spellings, so r.morale and r.stability passed."""
    w = _w()
    for name in ("morale", "stability", "unrest_index", "cohesion", "vibe", "zzz"):
        with pytest.raises(Forbidden):
            setattr(w.rungs["S"], name, 1)


def test_d10_the_log_has_a_content_hash():
    """DEFECT 10. S33 names the content hash 'the artifact'; S66 makes it the done-condition
    of artifacts 1, 4 and 5. Rev 1 had none."""
    assert len(_w().content_hash()) == 32


def test_d10b_resolve_sums_then_clamps_once():
    src = inspect.getsource(S.SeasonDriver.resolve)
    assert "sum(deltas)" in src and "clamp ONCE" in src


def test_d10c_the_obstacle_refusal_gate_exists():
    """S27.4 / S34: 'an attempt at Ob > 2 x Pool is refused' -- 'mechanical in RESOLVE'."""
    assert "obstacle_refusal_multiple" in SHAPE_CODE
    assert "attempt.refused" in inspect.getsource(S.SeasonDriver.resolve)


# ===========================================================================
# STANDING INVARIANTS
# ===========================================================================

def test_event_never_grows_a_target_or_an_actor():
    """S19.3, and Part VIII lists the target field as a REFUSAL: 'an Event that knows who it
    is for is an Event that cannot be misattributed, AND MISATTRIBUTION IS A FEATURE.'"""
    fields = set(Event.__dataclass_fields__)
    for banned in ("target", "actor", "source_actor", "recipient", "to", "stat_deltas"):
        assert banned not in fields
    assert fields == {"id", "kind", "subject", "changes", "causes", "emitted_at", "degree"}


def test_causes_is_never_empty():
    with pytest.raises(Forbidden):
        Event("i", "a.b", "s", [], [], 0)
    assert Event("i", "a.b", "s", [], [S.ROOT], 0).causes == [S.ROOT]


def test_choose_receives_no_world():
    src = inspect.getsource(S.SeasonDriver.deliberate)
    # REV 3: `choose` receives the budget QUERY, not the answer -- S26.3's "the person chooses
    # what to leave undone". Pinning the literal 4-ary string was how rev 2 locked in a
    # deviation as an invariant, so this pins the PROPERTY instead.
    assert "choose(p, v, s, ask_budget)" in src and "choose(w" not in src
    assert "sense(p, w, subsistence)" in src, "DELIBERATE must be fed a Sensation, per S26"


def test_a_view_raises_on_any_world_collection():
    v = View("p", [], 5)
    for attr in ("persons", "rungs", "sites", "log", "tenures", "anything_at_all"):
        with pytest.raises(Forbidden):
            getattr(v, attr)


def test_a_view_is_capped_at_k():
    with pytest.raises(Forbidden):
        View("p", ["a", "b", "c"], 2)


def test_sensation_is_constructed_by_the_loop_and_standing_raises_on_read():
    """REV 3. Rev 2 made `sense()` raise outright, so `Sensation` was NEVER CONSTRUCTED IN ANY
    RUN and the driver fed DELIBERATE a bare int -- the type S26 puts in `choose`'s signature
    was routed around, and a test pinned the deviated call as the invariant. The type is now
    built every season and `standing` raises AT THE POINT OF USE."""
    w = _w()
    sn = S.sense(w.persons["p_low"], w, P.SUBSIST)
    assert isinstance(sn, S.Sensation) and isinstance(sn.subsistence, int)
    # BOTH scalars now (`H-29`). §18.2 says EXACTLY TWO, and the loop builds both.
    assert isinstance(sn.standing, int) and len(tuple(sn)) == 2, tuple(sn)
    # The refusal survives where it is still true: a Sensation built with ONE scalar is half a
    # Sensation, and reading the missing half must refuse rather than answer 0.
    with pytest.raises(Unspecified):
        _ = S.Sensation(5).standing
    with pytest.raises(AttributeError):
        sn.third = 3


def test_a_proposition_cannot_be_edited():
    with pytest.raises(Exception):
        Proposition("p", "OUGHT", "s", "pred", True, 0).value = False


def test_r1_aggregates_over_live_edges_only():
    """S22.4 clause 3. Ended Tenures persist as historical claim subjects, so an aggregate
    that walks them is monotone -- a ratchet built out of 'structural' edges."""
    w = _w()
    f = lambda r: w.rungs[r].stores.get("grain", 0) if r in w.rungs else 0
    base = Query.r1_aggregate(w, "S", f)
    w.rungs["Ghost"] = Rung("Ghost", "hearth", stores={"grain": 500})
    w.add_tenure(Tenure("t_end", "Ghost", "S", "contain", since=0, until=0))
    assert Query.r1_aggregate(w, "S", f) == base


def test_the_ratchet_guard_detects_rather_than_trusting_a_flag():
    with pytest.raises(Forbidden):
        Query.commit_count_guard(_w(), [Tenure("a", "p", "o", "commit", since=0, until=1)], "ever")


def test_a_cache_cannot_be_built_inside_a_parallel_map():
    w = _w()
    w._in_parallel_map = True
    with pytest.raises(Forbidden):
        w.cache_at_barrier("k", lambda: 1)


def test_witness_writes_no_belief_and_no_conviction():
    """S9.3: 'IF EVIDENCE CAN MOVE A CONVICTION, the moral layer has become a second epistemic
    layer and T2 is gone. This is the single most dangerous collision in the design.'"""
    src = inspect.getsource(S.SeasonDriver.witness)
    for banned in ("beliefs", "convictions"):
        assert f'fieldname="{banned}"' not in src


def test_hold_cardinality_is_one_per_object():
    w = _w()
    w.add_tenure(Tenure("t_dup", "p_mid", "off_duke", "hold", since=0))
    with pytest.raises(Forbidden):
        Query.hold_force(w, "off_duke")


def test_the_partition_seam_is_bounded_by_causation_not_by_the_column():
    """S15.3: 'a plague that kills the praefect ends his tenure THROUGH THE DEATH; A STORM
    CANNOT TOUCH IT.'"""
    w = _w()
    w.step = Step.MATTER
    t = next(x for x in w.tenures if x.kind == "hold")
    with pytest.raises(Forbidden):
        w.write("Tenure", WriteClass.MATTER, lambda: setattr(t, "until", 0),
                record_kind="Tenure", fieldname="until", driver="Event",
                emits="tenure.closed", subject=t.object, causes=[S.ROOT])
    w.write("Tenure", WriteClass.MATTER, lambda: setattr(t, "until", 0),
            record_kind="Tenure", fieldname="until", driver="Event",
            caused_person_exists="p_high",
            emits="tenure.closed", subject=t.object, causes=[S.ROOT])
    assert not t.live


def test_a_missing_provider_is_a_boot_failure():
    w = _w()
    w.boot(("contest",))
    with pytest.raises(S.NoProducer):
        w.boot(("contest", "no_such_role"))


# ===========================================================================
# THE INSTRUMENT'S REPORTING HONESTY
# ===========================================================================

def test_an_unfired_refusal_is_never_reported_as_a_pass():
    src = inspect.getsource(R.run_probe)
    assert "UNREACHABLE" in src and "NOT-REFUSED" in src


def test_no_probe_currently_returns_unreachable():
    R._VERDICTS.clear()
    bad = [pid for pid in P.PROBES if R.run_probe(pid)["verdict"] == "NOT-REFUSED"]
    assert not bad, f"refusals that did not fire: {bad}"


def test_no_probe_errors():
    R._VERDICTS.clear()
    bad = {pid: R.run_probe(pid)["detail"] for pid in P.PROBES
           if R.run_probe(pid)["verdict"] == "INSTRUMENT-ERROR"}
    assert not bad, bad


def test_every_probe_declares_how_its_verdict_was_reached():
    """S34: 'overstating this column is the failure mode.' Rev 1 had eleven probes that raised
    a gap BY HAND and reported it as though the shape had refused."""
    allowed = {"construction", "no-signature", "convention", "probe-model"}
    bad = {pid: s["by"] for pid, s in P.PROBES.items() if s["by"] not in allowed}
    assert not bad, bad


def test_a_hand_raised_gap_is_never_labelled_construction():
    offenders = []
    for pid, spec in P.PROBES.items():
        if spec["by"] != "construction":
            continue
        body = _code_only(inspect.getsource(spec["fn"]))
        raises = re.search(r"\braise (Forbidden|Unspecified|NoProducer|Collision|Unowned)\(", body)
        calls = re.search(r"(w\.write|Query\.|contest\(|sense\(|_run\(|Event\(|cache_at_barrier"
                          r"|boot\(|setattr\(|Rung\(|View\(|fixtures)", body)
        if raises and not calls:
            offenders.append(pid)
    assert not offenders, offenders


def test_unmapped_rows_are_never_silently_passed():
    src = inspect.getsource(R.grade)
    assert "unmapped" in src and "NOT-ASSESSED" in src


def test_an_unclear_row_is_not_counted_as_an_unrouted_one():
    """An `UNCLEAR:` row is the CASE SOURCE failing, not the shape failing."""
    assert "unclear" in inspect.getsource(R.grade)


@contextlib.contextmanager
def _declared(case_id: str, mapping: dict):
    """Temporarily bind needs to `exercises:` tokens for a synthetic case.

    ⚠ WITHOUT THIS, EVERY GRADING GUARD BELOW IS VACUOUS UNDER `W10`. A synthetic case invented
    in a test has no overlay file, so ALL of its rows are unmapped and it reaches NOT-ASSESSED by
    the widest branch there is -- which means the guard passes no matter which narrower rule you
    delete. Three tests were in that state when the `W10` pass read them. To observe a rule you
    have to build the input that ONLY that rule rejects, and that means declaring some rows and
    not others."""
    prev = R.OVERLAY.get(case_id)
    R.OVERLAY[case_id] = {EX.need_sha(n): {"need": n, "exercises": list(t)}
                          for n, t in mapping.items()}
    try:
        yield
    finally:
        if prev is None:
            R.OVERLAY.pop(case_id, None)
        else:
            R.OVERLAY[case_id] = prev


def _a_satisfied_token() -> str:
    """A register id whose grade PASSES, read off the register rather than typed here -- so a
    re-grade moves the fixture instead of silently turning these guards vacuous again."""
    for hid, row in sorted(R._register().items()):
        if row.get("grade") in ("ruled", "measured"):
            return hid
    raise AssertionError("no register row is `ruled` or `measured` -- fixture cannot be built")


def test_playable_requires_that_every_core_row_was_actually_aimed_at():
    """A case with ANY unmapped `core` row may not be graded PLAYABLE. Five of the twelve
    PLAYABLE verdicts in the first run rested on one or two routed core rows with other core
    rows sitting unmapped beside them -- one reached PLAYABLE on a SINGLE distinct probe with
    three rows unrouted. That is the instrument certifying a season it never aimed at.

    ⚠ REWRITTEN SO IT CAN OBSERVE ITS OWN FAILURE. The old body declared nothing, so both rows
    were unmapped and `not core_routed` decided it -- delete the clause this test names and the
    test still passed. The pair below is the discriminating input: identical cases differing
    ONLY in whether the second core row is declared, and the rule is the sole thing that
    separates PLAYABLE from NOT-ASSESSED."""
    ok = _a_satisfied_token()
    aimed = "a person with no office must be able to act"
    unaimed = "zzzz qqqq wwww vvvv"

    # CONTROL: both core rows declared -> the case is reachable at PLAYABLE.
    with _declared("T", {aimed: [ok], unaimed: [ok]}):
        both = R.grade({"id": "T", "season_requires": [
            {"need": aimed, "hardness": "core"}, {"need": unaimed, "hardness": "core"}]})
    assert both["verdict"] == "PLAYABLE", (
        f"the control does not reach PLAYABLE ({both['verdict']}), so the test below proves "
        "nothing about the rule -- it would pass for any reason at all")

    # THE RULE: one core row left undeclared, everything else identical.
    with _declared("T", {aimed: [ok]}):
        got = R.grade({"id": "T", "season_requires": [
            {"need": aimed, "hardness": "core"}, {"need": unaimed, "hardness": "core"}]})
    assert got["verdict"] == "NOT-ASSESSED", got["verdict"]
    assert got["core_routed"] == 1 and got["core_unmapped"] == 1, got


def test_a_case_with_no_core_rows_at_all_is_not_assessed():
    """The one input the strict clause cannot reach, and therefore the only reason the
    `not core_routed` branch still exists. `core_unmapped` is empty here, so nothing else would
    stop a case reaching PLAYABLE on its non-core rows alone.

    (`test_a_case_more_than_half_unrouted_on_core_is_not_assessed` was RETIRED with the rule it
    named. That rule's own predicate proved `core_unmapped` non-empty, so the strict clause
    returned the same verdict on every input reaching it: it was dead, and its guard passed by
    deleting it. §0.1 pt 2.)"""
    ok = _a_satisfied_token()
    soft = "a soft row nobody calls core"
    with _declared("T", {soft: [ok]}):
        got = R.grade({"id": "T", "season_requires": [{"need": soft, "hardness": "important"}]})
    assert got["verdict"] == "NOT-ASSESSED", got["verdict"]


def test_a_blocker_outranks_an_unaimed_row():
    """A core row that IS declared and DOES hit a gap is a fact about the SHAPE; a core row
    nobody declared is a fact about the AUTHORING. The first outranks the second.

    ⚠ REWRITTEN FOR `W10`. It used to plant two needs and rely on the regex router to reach a
    probe for one of them — so it tested the router as much as the grading rule. The rule is now
    stated over declarations, which is where it belongs and where it can be read."""
    planted = {"T": {EX.need_sha("a declared row that gaps"): {
        "need": "a declared row that gaps", "exercises": ["comply"]}}}
    saved, R.OVERLAY = R.OVERLAY, planted
    try:
        got = R.grade({"id": "T", "season_requires": [
            {"need": "a declared row that gaps", "hardness": "core"},
            {"need": "a row nobody declared", "hardness": "core"},
        ]})
    finally:
        R.OVERLAY = saved
    assert got["verdict"] == "BLOCKED", got
    assert got["core_unmapped"] == 1, got          # the undeclared row is still reported
    assert got["blockers"] == ["comply"], got["blockers"]


def test_no_playable_case_has_an_unmapped_core_row():
    """The standing invariant over the ACTUAL run, not a synthetic case."""
    R._VERDICTS.clear()
    rep = R.main()
    bad = [c["id"] for k in ("NPC", "ARC") for c in rep[k]
           if c["verdict"] == "PLAYABLE" and c["core_unmapped"]]
    assert not bad, f"PLAYABLE cases with unaimed core rows: {bad}"


def test_r3_the_a5_control_actually_fires():
    """REV 3, DEFECT C1 — the worst thing the second antagonist found, and it was mine. A5's
    float control computed `0.9 + d/1000.0`, got 0.902 == 0.902, PRINTED `differing=False`
    AND ASSERTED IN THE SAME SENTENCE THAT THE CONTROL HAD FIRED. §66 artifact 4: 'A float
    build must produce a DIFFERENT hash under a reordered fold, OR THE TEST CANNOT OBSERVE
    WHAT IT EXCLUDES.'"""
    src = _code_only(inspect.getsource(P.PROBES["A5"]["fn"]))
    assert "assert float_differs" in src, "the control must be ASSERTED, not merely computed"
    v = R.run_probe("A5")
    assert v["verdict"] == "PASS", v
    assert "DIFFERENT" in v["detail"] and "differing=False" not in v["detail"]


def test_r3_the_partition_is_stated_and_refuses_by_default():
    """REV 3, DEFECT C6, RE-EXPRESSED BY W2. The rev-2 derivation was a TWO-VALUED CLASSIFIER
    OVER A FIVE-VALUED DOMAIN whose uncovered cases fell through to the PERMISSIVE branch -- the
    silent default §42.2.1 refuses, at the opposite polarity to §42.2's rule that zero evidence
    maps to the verdict AGAINST the thing measured.

    ⚠ **THERE IS NO DERIVATION LEFT TO BE PARTIAL.** W2 loads Part D from `write_matrix.yaml`,
    where every row STATES its `social:` and carries a `by:` provenance, so the four cells the old
    classifier could not reach -- `Date`, `DocketItem`, `ConveningCondition`, `claim_ledger` -- are
    stated rows under §D2's `DR-3` rather than instrument assumptions. The defect this test was
    written for cannot recur in the same form; what CAN recur is the polarity, so that is what it
    now pins: an unstated cell REFUSES, and it refuses for every kind, not just the ones someone
    remembered."""
    for kind, fname in (("Date", "fired"), ("DocketItem", "matter"),
                        ("ConveningCondition", "attached"), ("Person", "claim_ledger")):
        social, by = S.partition_lookup(kind, fname)
        assert social is False, f"({kind}, {fname}) should be social:false under DR-3"
        assert "DR-3" in by, (
            f"({kind}, {fname}) is one of the four the old classifier could not reach; its row "
            f"must carry DR-3's provenance, not {by!r}")
    assert S.partition_lookup("Site", "condition")[0] is False
    assert S.partition_lookup("Person", "stance")[0] is True
    # THE POLARITY, which is the part that must never invert: an unstated cell refuses, for every
    # kind on the table and for a kind that is not.
    for kind in sorted({k for k, _ in S.MATRIX} | {"NoSuchKind"}):
        with pytest.raises(Unspecified):
            S.partition_lookup(kind, "a_field_nobody_ruled")


def test_r3_the_instrument_assumes_no_partition_row_at_all():
    """The three rows the instrument HAD to assume to run at all were §42.2.1's inject-declare-
    name pattern applied to a SCHEMA ROW, and they were declared, counted and reported.

    ⚠ **W2 EMPTIES THE SET, AND THAT IS ITS OWN STATED PROOF.** `(Person, claim_ledger)`,
    `(Date, fired)` and `(DocketItem, matter)` were assumptions only because the old two-clause
    derivation could not reach them; §D2's `DR-3` states all three. This is a REDUCTION in what
    the instrument supplies rather than an addition -- the direction that matters, since every
    assumed row was a piece of L4's enforcement resting on the instrument instead of the design.

    The disclosure hook stays and must keep reporting: an empty set that nothing reads would be
    the same false-disclosure defect in a quieter form."""
    assert S.PARTITION_ASSUMED == {}, (
        f"W2's proof is ZERO assumed Partition rows; found {sorted(S.PARTITION_ASSUMED)}")
    import report
    assert "PARTITION_ASSUMED" in inspect.getsource(report.emit), (
        "report.py stopped reading the disclosure hook, so a future assumption would go "
        "unreported -- which is exactly the false-disclosure defect rev 5 fixed")
    # AND THERE MUST BE A CODE PATH THAT POPULATES IT. The first draft planted a key directly into
    # the dict, which proves only that a dict is mutable -- an adversarial pass pointed out that no
    # path in `shape.py` could populate the channel at all, so "zero assumed rows" was satisfiable
    # BY DELETION. `assume_partition_row` is the path; this exercises it and checks the DISCLOSURE
    # side too, since a channel nothing reports through is the same defect one level along.
    try:
        S.assume_partition_row("Person", "planted", True, "planted by a test")
        assert ("Person", "planted") in S.PARTITION_ASSUMED, "the channel did not record the row"
        assert ("Person", "planted") in S.ASSUMPTIONS_USED, (
            "the row was declared and not marked EXERCISED -- `report.py` counts the intersection, "
            "so it would report an assumption nobody used")
    finally:
        S.PARTITION_ASSUMED.pop(("Person", "planted"), None)
        S.ASSUMPTIONS_USED.discard(("Person", "planted"))


def test_r3_the_l4_limb_is_actually_exercised():
    """DEFECT C6, second half. Rev 2's L4 branch NEVER RAN in the whole suite: the three probes
    that claimed to test it wrote `stance` at MATTER, where the step-matrix check stopped them
    one line earlier. A social:true row written by an Event at a PERMITTED step must raise."""
    w = _w()
    w.step = Step.RESOLVE
    with pytest.raises(Forbidden) as e:
        w.write("stance", WriteClass.ACTS, lambda: None,
                record_kind="Person", fieldname="stance", driver="Event")
    assert "social:true" in str(e.value)


def test_r3_the_l5_crossing_emits_a_witnessable_event():
    """DEFECT C5. Rev 2 appended a crossing row for EVERY site EVERY season regardless of any
    band, and never constructed an Event — so nothing was witnessable and nothing entered the
    log, while the probe claimed 'L5 exactly'. §12.1: 'A band edge crossing is an EMISSION.'"""
    # ⚠ NARROWED FAN-OUT, NOT A SEEDED SITE, AND THE FIRST ASSERTION IS WHY. This test grinds 23
    # seasons, and its opening control is that NO band has been crossed after three — which a site
    # seeded near a floor would break. Narrowing `H-33`'s arm is the fix that leaves every number
    # here identical, because a band crossing does not depend on who witnesses it. Without it this
    # single test took **213 seconds**, more than the rest of the suite combined, once `W4` made
    # MATTER emit per write and the default arm kept the fan-out total.
    w = P.tiny_world(S.DEFAULT_FIXTURES.sweep("fan_out_mode", "presence_only"))
    d = S.SeasonDriver(w)
    site = w.sites["site_harbour"]
    for _ in range(3):
        d.season(P.NOCHOOSE, None, P.SUBSIST)
    assert not [c for c in w.crossings if c[0] == site.id], "no band was crossed yet"
    for _ in range(20):
        d.season(P.NOCHOOSE, None, P.SUBSIST)
    mine = [c for c in w.crossings if c[0] == site.id]
    assert mine
    eid = mine[0][4]
    ev = next(e for e in w.log if e.id == eid)
    assert ev.kind == "condition.band_crossed" and not ev.changes and ev.degree is None


def test_r3_witness_fans_to_everyone_as_specified():
    """DEFECT C13. Rev 2 keyed observers on the Event's subject rung and fell back to THE
    SUBJECT ALONE, which — since every person has a person-kind Rung — made almost every Event
    private to itself. That is a SELF-WITNESS RULE THAT APPEARS NOWHERE IN THE CHAIN: the
    instrument supplied the privacy the design lacks, then reported the design's privacy gap
    in a probe that never touched the loop. §61: 'WITNESS as specified fans every Event to
    every person.'"""
    w = _w()
    d = S.SeasonDriver(w)
    def choose(p, v, s, ask_budget):
        return [P.Act_(w, p, "speak")] if p.id == "p_low" else []
    def effect(w, a):
        return [P.Ev(w, a.actor, "a.shout", a.actor, [S.ROOT])]
    r = d.season(choose, None, P.SUBSIST)
    assert r["deposits"] >= len(w.persons), (r["deposits"], len(w.persons))


def test_r3_choose_asks_its_own_budget():
    """DEFECT C11. §26.3: the PERSON chooses what to leave undone. Rev 2 computed the budget in
    the engine and handed the number down — the half of retraction 5 that never landed."""
    src = _code_only(inspect.getsource(S.SeasonDriver.deliberate))
    assert "ask_budget" in src
    asked = []
    w = _w()
    def choose(p, v, s, ask_budget):
        asked.append(ask_budget())
        return []
    S.SeasonDriver(w).season(choose, None, P.SUBSIST)
    assert asked, "no person was asked for a budget at all"
    # ⚠ W5 REPOINTED THIS ASSERTION, AND THE OLD ONE WAS THE DEFECT. It read
    # `all(n == w.fixtures.get("scene_budget") for n in asked)` — i.e. it PINNED A FLAT BUDGET,
    # which is the field S26.3 forbids, as an invariant. `budget` reading its own arguments is
    # what broke it, and a test that goes red when the specification is finally met was testing
    # the implementation. C11's claim is that the person is ASKED; that is what stays.
    base = w.fixtures.get("scene_budget")
    assert all(n >= 1 for n in asked), "a budget of 0 deletes a person from the season silently"
    assert any(n != base for n in asked), (
        f"every budget came back at the flat base {base} ({asked}) — `budget` is ignoring `p` "
        "again, which is #353 :912-913's 'a wounded duke gets fewer acts than a healthy one' "
        "unmet. This assertion is the falsifier for W5's person-side budget.")


def test_w5_budget_moves_with_the_persons_own_state_in_the_ruled_directions():
    """`H-28` / §F3. #353 `:912-913` rules the DIRECTION of all three modifier terms and no
    magnitude, so this tests directions and never a number.

    Three separate one-variable comparisons against the same person, because a single world with
    three differing people cannot tell you WHICH term moved the total — that is §0.1 point 4's
    control, applied to a formula rather than to a measurement."""
    w = _w()
    fx = w.fixtures
    p = next(iter(w.persons.values()))
    v = S.View(p.id, [], fx.get("view_k"))
    k = fx.get("scene_budget")
    base = S.Query.budget(p, v, k, fx)

    # office: a live `hold` Tenure the person OWNS. Routed through add_tenure, so the store is
    # the person's own — which is the whole reason budget can read it with no World.
    w.add_tenure(S.Tenure("t_b1", p.id, "off_x", "hold", since=0))
    assert S.Query.budget(p, v, k, fx) > base, "holding an office did not raise the budget"
    p.tenures = [t for t in p.tenures if t.id != "t_b1"]

    # body: falling a band. `band_floors["body"]` is the table the SITE gate already uses.
    floors = sorted(fx.get("band_floors")["body"].values(), reverse=True)
    p.body, was = floors[0] - 1, p.body
    assert S.Query.budget(p, v, k, fx) < base, "falling a body band did not lower the budget"
    lower = S.Query.budget(p, v, k, fx)
    p.body = floors[-1] - 1
    assert S.Query.budget(p, v, k, fx) < lower, "the narrowing is not monotone across bands"
    assert S.Query.budget(p, v, k, fx) >= 1, "a dying person must still get one scene, not zero"
    p.body = was

    # travel: a leg spent this season.
    p.travel_leg = ["leg_a"]
    assert S.Query.budget(p, v, k, fx) < base, "a travel leg did not lower the budget"


def test_r3_the_dead_code_is_reached():
    """DEFECT C8. An implemented rule no probe exercises is indistinguishable from an absent
    one, and reporting it as landed is the flattering direction. Rev 2 declared STRATA and
    never referenced it, and had an Ob>2xPool branch no probe could reach."""
    for pid in ("A37", "A38", "A39", "A31c"):
        assert pid in P.PROBES, pid
    assert R.run_probe("A37")["verdict"] == "PASS"
    assert R.run_probe("A38")["verdict"] == "PASS"


def test_r3_the_band_floors_are_swept():
    """DEFECT C14. §42.2.1 names 'three band edges' among the four constants a prior instrument
    invented. Rev 2 fixed the other three and left these as literals in probe bodies, so every
    pacing claim was a one-dimensional sweep of a two-parameter model."""
    assert "band_floors" in S.DEFAULT_FIXTURES._v
    body = PROBES_CODE.split("def tiny_world", 1)[1]
    assert "scale * 8 // 10" not in body, "a band edge is still a literal in a probe body"


def test_r3_a_working_mechanism_is_not_reported_as_a_blocker():
    """DEFECT C10. A1 provokes `causes=[]` to demonstrate the refusal; routing provenance rows
    to it graded them BLOCKED — reporting the design's causes[] rule as the thing that blocks
    causal reconstruction. A2 is the probe that DEMONSTRATES provenance, and it passes."""
    # ⚠ THE ROUTING HALF OF C10 IS NOW STRUCTURALLY IMPOSSIBLE, WHICH IS `W10`'S POINT. A
    # provenance row reached `A1` because a regex matched a common word; nothing can reach any
    # probe by accident now, because every binding is authored and named. What survives as a
    # testable claim is the MECHANISM half — that a probe demonstrating provenance exists and
    # passes, so an author has something true to point at.
    assert R.run_probe("A2")["verdict"] == "PASS"
    # A1 GAPS BY DESIGN — it PROVOKES the `causes=[]` refusal to show the rule fires — and that
    # is exactly why routing a provenance row to it graded the row BLOCKED. The two halves must
    # stay distinguishable: one demonstrates the refusal, the other demonstrates the mechanism.
    a1 = R.run_probe("A1")
    assert a1["verdict"] == "GAP" and a1["kind"] == "FORBIDDEN", a1
    assert R.run_probe("A2")["verdict"] == "PASS", "the mechanism half stopped demonstrating"


def test_r4_l3_clause_1_is_permitted_and_clause_2_is_refused():
    """REV 4. The head permits clause 1 in terms: a monotone counter per (Person, axis) is
    "legal, since every increment is in the holder's own ledger"; clause 2 bars only the
    CROSS-HOLDER sum. Revisions 1-3 raised clause 2 on single-holder needs and blocked 18
    cases on it -- THE INSTRUMENT MEASURING AGAINST THE DESIGN, which §0.1 pt 4 rules is no
    more acceptable than flattering it."""
    w = _w()
    with pytest.raises(Unspecified) as e:
        Query.single_holder_counter(w, "p_low", "suspicion", registry=set())
    assert "closed" in str(e.value)                      # the registry is the real gap
    assert Query.single_holder_counter(w, "p_low", "x", registry={"x"}) == 0
    with pytest.raises(Forbidden):
        Query.aggregate_guard(w, "cohort_unrest", per_person_tally=True)


def test_r4_the_l1_actor_identity_is_checked():
    """REV 4. `Act.actor` was a bare unchecked id, so `Act("x","the_church","excommunicate")`
    reached `resolve` intact — which made A6's and F3's "'The Church excommunicates' IS NOT
    SPELLABLE" false, while both were labelled on the strength of it."""
    w = _w()
    def impostor(p, v, s, ask_budget):
        from shape import Act
        return [Act("x", "the_church", "excommunicate")] if p.id == "p_low" else []
    with pytest.raises(Forbidden):
        P._run(w, impostor)


def test_r4_event_ids_are_unique_per_draw_and_reproducible():
    """REV 4, TWICE. `purpose` minted per KIND gave five Events one id (violating the invariant
    A28 certifies); a global monotonic counter made ids unique but NOT REPRODUCIBLE, which is
    the worse bug — it destroys §33's replay contract."""
    def run():
        w = _w()
        def choose(p, v, s, ask_budget):
            # W3: `m0`/`m1`/`m2` were invented verbs and the fold refuses them. `work` is the
            # table verb that writes `(Site, condition)`; the discriminator keeps the three acts
            # distinct, which is the property this test is about — one person, one tick, three
            # acts, three DIFFERENT Event ids.
            return ([P.Act_(w, p, "work", key=str(i),
                            changes=[S.StateChange("site_harbour", "alter", "Act",
                                                   "condition", i + 1)])
                     for i in range(3)] if p.id == "p_low" else [])
        P._run(w, choose)
        return w
    w1, w2 = run(), run()
    ids = [e.id for e in w1.log]
    assert len(ids) == len(set(ids)), "ids must be unique per draw"
    assert w1.content_hash() == w2.content_hash(), "and identical across runs of the same seed"


def test_the_corpus_defects_are_reported_not_hidden():
    """Six of the in-chain corpus's seven case files are committed inside a markdown fence
    with a transcript preamble, and one is TRUNCATED AT ITS HEAD. The instrument works around
    them at LOAD time and SAYS SO -- it does not edit the chain's evidence."""
    R.CORPUS_DEFECTS.clear()
    R.load_cases("ARC")
    assert R.CORPUS_DEFECTS and any("TRUNCATED" in d for d in R.CORPUS_DEFECTS)


# ===========================================================================
# W15 -- ONE WRITER PER ARTIFACT (guardrail G7)
#
# THE FAILURE THAT EARNED THESE TESTS: `run_cases.py.__main__` and `report.py.__main__` both
# wrote `results.json` and `TRACE.txt`, and `report.py` additionally wrote eight markdown files
# from ITS run. Whichever entrypoint ran last won, the committed markdown went stale by one fix,
# and FOUR ARC CASES WERE WRONG IN A MERGED PR -- a defect nothing could notice, because no
# artifact was ever checked against any other.
#
# THREE TESTS, AND THE MIDDLE ONE IS THE GUARD. An adversarial pass broke the first draft of
# this block, which had only the outer two, and both of its findings are fixed here rather than
# filed:
#
#   * the ENTRYPOINT test proves the silent entrypoint is silent. It proves nothing about the
#     loud one.
#   * the REPRODUCTION test proves the loud one is correct: it executes `report.py` and asserts
#     every committed artifact comes back byte-identical. That covers all ten artifacts and
#     every field rendered into them, and it is the test that would have caught all four wrong
#     ARC cases. W15's Proof says "running EITHER entrypoint", and this is the "either".
#   * the PER-CASE test is W15's Proof stated literally -- caselog verdict == `results.json` for
#     all 143. IT IS A DIAGNOSIS, NOT THE GUARD: it re-parses a markdown format `report.py` owns,
#     so a cosmetic change to that format fails it. The failure direction is safe (a false alarm,
#     never a false pass) and the reproduction test above is what actually enforces G7.
#
# The first draft of the per-case test compared ONLY `verdict` while claiming in its own
# docstring that it "would have caught the four wrong ARC cases". It would have caught ONE:
# `run_cases.py`'s grader short-circuits on `if core_blocked: verdict = "BLOCKED"`, so SCN-06's
# defect (blockers `A27` -> `A27, P17`) could not move a verdict at all, and EMG-C2/NSC-09 stay
# NOT-ASSESSED either way. A false claim of enforcement is worse than none, because it stops the
# next reader from checking (ARCHITECTURE.md S47). It now compares every field the caselog
# renders, which does catch SCN-06.
# ===========================================================================

PROPOSAL = HERE.parent


def _proposal_files():
    """Every tracked-shaped file under the proposal, not just `runs/`. The first draft
    fingerprinted `runs/` alone with a non-recursive `iterdir()`, so a restored write to
    `ROOT / "out"` -- a one-token edit -- or to `runs/sub/` passed it. The property is *this
    entrypoint does not write*, so the sweep has to be the tree, not one directory."""
    return sorted(f for f in PROPOSAL.rglob("*")
                  if f.is_file() and "__pycache__" not in f.parts and f.suffix != ".pyc")


def _fingerprint(with_mtime: bool) -> dict:
    """Content hash, and optionally mtime. THE HASH ALONE IS NOT ENOUGH and this is not
    hypothetical: the first version of this helper hashed only content, and the mutation that
    restored `TRACE.txt.write_text(...)` to `run_cases.py.__main__` PASSED IT, because the
    restored write produced byte-identical output. mtime is what separates *did not write* from
    *did not change anything*."""
    import hashlib
    out = {}
    for f in _proposal_files():
        h = hashlib.sha256(f.read_bytes()).hexdigest()
        out[str(f.relative_to(PROPOSAL))] = (h, f.stat().st_mtime_ns) if with_mtime else h
    return out


def _run(script: str):
    import subprocess
    proc = subprocess.run([sys.executable, str(HERE / script)],
                          capture_output=True, text=True, cwd=str(HERE))
    assert proc.returncode == 0, f"{script} failed:\n{proc.stderr[-3000:]}"
    return proc


def test_w15_the_run_cases_entrypoint_writes_nothing():
    """`report.py` is the sole emitter. Executed, not read: this runs `run_cases.py` as a script
    and fingerprints every file under the proposal before and after. A restored write fails here
    however it is spelled and wherever under the proposal it lands."""
    before = _fingerprint(with_mtime=True)
    # Assert that it asserted (CLAUDE.md S0.1 point 2): an empty tree would otherwise let this
    # pass having observed nothing, which is the exact vacuity its sibling test guards against.
    assert len(before) > 10, f"fingerprinted only {len(before)} files -- the sweep is broken"
    _run("run_cases.py")
    after = _fingerprint(with_mtime=True)
    changed = sorted(k for k in set(before) | set(after) if before.get(k) != after.get(k))
    assert not changed, f"run_cases.py wrote under the proposal: {changed}"


def test_w15_report_py_reproduces_every_committed_artifact_byte_for_byte():
    """**THE GUARD.** Executes the sole emitter and asserts every committed artifact comes back
    byte-identical. This is what makes a stale artifact impossible rather than merely unlikely:
    it covers `results.json`, `TRACE.txt` and all eight markdown files, and every field rendered
    into them -- not the one scalar the per-case test can reach. It subsumes the four wrong ARC
    cases, including the three a verdict comparison cannot see."""
    runs = PROPOSAL / "runs"
    before = {f.name: f.read_bytes() for f in sorted(runs.iterdir()) if f.is_file()}
    assert len(before) >= 10, f"expected the ten run artifacts, fingerprinted {sorted(before)}"
    try:
        _run("report.py")
        after = {f.name: f.read_bytes() for f in sorted(runs.iterdir()) if f.is_file()}
    finally:
        # PUT THE COMMITTED BYTES BACK. Without this the test HEALS the tree it is judging: a
        # stale artifact would fail once, be silently overwritten with the correct output, and
        # pass on the next run -- so the defect it exists to catch would be unreproducible and
        # would leave an uncommitted edit nobody asked for. A test does not repair its subject.
        for name, blob in before.items():
            f = runs / name
            if not f.exists() or f.read_bytes() != blob:
                f.write_bytes(blob)
    assert set(before) == set(after), (
        f"report.py changed WHICH artifacts exist: added {sorted(set(after) - set(before))}, "
        f"removed {sorted(set(before) - set(after))}")
    stale = sorted(k for k in before if before[k] != after[k])
    assert not stale, (
        f"committed artifacts do not match what report.py produces: {stale}. Either the run "
        "is non-deterministic or the artifacts were committed from a different run (W15/G7).")


_CASE_HEAD = re.compile(r"^## (\S+) .*?\*\*([A-Z-]+)\*\*\s*$")
_CASE_META = re.compile(
    r"^\*(?P<scale>.*?) · (?P<rows>\d+) rows, (?P<core>\d+) core · blockers: (?P<blockers>.*)\*$")


def _caselog_records(kind: str) -> dict:
    """Parse every field `report.py` renders per case out of the committed caselog -- the header
    line's id and verdict, and the meta line's scale, row counts and blockers. Comparing the
    verdict ALONE is what let SCN-06's defect through the first draft of this test."""
    lines = (PROPOSAL / "runs" / f"CASELOG_{kind}.md").read_text().splitlines()
    out, pending = {}, None
    for line in lines:
        h = _CASE_HEAD.match(line)
        if h:
            pending = h.group(1)
            out[pending] = {"verdict": h.group(2)}
            continue
        if pending:
            m = _CASE_META.match(line)
            if m:
                out[pending].update(scale=m.group("scale"), rows=int(m.group("rows")),
                                    core=int(m.group("core")), blockers=m.group("blockers"))
                pending = None
    return out


def test_w15_every_case_record_in_the_caselog_equals_results_json():
    """W15's Proof, stated literally: the caselog's per-case record equals `results.json`'s for
    all 143. A DIAGNOSIS rather than the guard -- see the block comment above -- but the one that
    names the case and the field when the reproduction test says only *CASELOG_ARC.md differs*."""
    import json as json_
    results = json_.loads((PROPOSAL / "runs" / "results.json").read_text())
    expected = sum(len(results[k]) for k in ("NPC", "ARC"))
    checked = 0
    for kind in ("NPC", "ARC"):
        logged = _caselog_records(kind)
        cases = {c["id"]: c for c in results[kind]}
        assert set(logged) == set(cases), (
            f"{kind}: caselog and results.json disagree on WHICH cases exist: "
            f"only in log {sorted(set(logged) - set(cases))}, "
            f"only in results {sorted(set(cases) - set(logged))}")
        for cid, c in sorted(cases.items()):
            got = logged[cid]
            want = {"verdict": c["verdict"], "scale": c.get("scale", ""),
                    "rows": c["rows"], "core": c["core"],
                    "blockers": ", ".join(c["blockers"]) or "none"}
            assert got == want, (
                f"{kind} {cid}: caselog says {got}, results.json says {want} -- the artifacts "
                "are from different runs (W15/G7)")
            checked += 1
    # Assert that it asserted (CLAUDE.md S0.1 point 2). The bound is derived from the corpus,
    # never a literal: a legitimate corpus addition must not fail as an artifact defect.
    assert checked == expected, f"compared {checked} of {expected} cases"
    # The corpus size is 143 today. Reproduce:
    #   python -c "import json;d=json.load(open('../runs/results.json'));print(len(d['NPC'])+len(d['ARC']))"
    assert expected > 0, "results.json carries no cases at all"


# ===========================================================================
# W0 -- THE HOLE REGISTER AS DATA
#
# THE FAILURE THAT EARNED THESE: `ARCHITECTURE_V2.md` §0.3 row 13 claims Part VII is "rows, not
# prose". It was a markdown table nothing read. Its counts did not reproduce from its own rows
# (39 claimed over 32 present; "Ten holes" over 12; grades summing to 34), not one row carried
# the `site:`/`sweep:`/`cite:` fields its own §G4 defines, and it could not report that
# twenty-two holes had no row at all. `hole_register.yaml` is the object; `register.py` reads it.
#
# WHAT THESE TESTS DO NOT DO: they do not assert the register is CLEAN. `--check` exits 1 today,
# on R2, R3 and G6, and that is the measurement -- W1 is the item that drives it down. They
# assert the CHECKER WORKS, which is the part a later session could break without noticing.
# ===========================================================================

import exercises as EX
import register as REG


def test_w0_the_register_transcription_still_matches_architecture_v2():
    """The 32 transcribed rows must still say what V2's Part VII tables say. Drift in EITHER
    direction is a defect: a row edited here silently, or a table edited there silently. Grade is
    deliberately NOT pinned -- W1 re-grades by design, and the re-grades are reported as notes."""
    drift = [b for b in REG.verify_transcription(REG.load()) if not b.startswith("NOTE ")]
    assert not drift, "register and ARCHITECTURE_V2.md Part VII have diverged:\n  " + "\n  ".join(drift)


def test_w0_every_part_b_defect_binds_to_a_row_or_a_section():
    """Guardrail G8. `D16` was the ONLY one of Part B's 26 defects with no Part VII row and no
    Part D-G discharge, and was claimed discharged anyway -- because the binding was prose. It is
    a map now, and the map is checked against Part B's ids as the document defines them.

    ⚠ The first draft of this test asserted only that the map is currently clean. It planted
    nothing, so the checker's REFUSAL was untested, and the section branch -- which today has zero
    live instances -- could accept anything at all."""
    reg = REG.load()
    assert REG.part_b_defects(), "Part B parsed to zero defect ids -- the check cannot run"
    assert not REG.rule_G8(reg), "G8: " + "; ".join(REG.rule_G8(reg))

    # A defect with no entry at all.
    dropped = REG.load()
    dropped["discharges"].pop("D16")
    assert any("D16" in b for b in REG.rule_G8(dropped)), "a dropped defect passed G8"

    # A row: target naming a row that does not exist.
    ghost = REG.load()
    ghost["discharges"]["D16"] = "row:H-999"
    assert any("H-999" in b for b in REG.rule_G8(ghost)), "a discharge to a ghost row passed G8"

    # THE SECTION BRANCH, which is the one that can reproduce D16's own failure. `§D9` does not
    # exist -- Part D ends at §D5 -- and the first draft accepted it silently.
    fake = REG.load()
    fake["discharges"]["D16"] = "§D9"
    assert any("D16" in b for b in REG.rule_G8(fake)), (
        "a discharge to a NON-EXISTENT section passed G8 -- D16 'claimed discharged anyway', again")
    real = REG.load()
    real["discharges"]["D16"] = "ARCHITECTURE_V2.md §VII.2 -- the seam"
    assert not [b for b in REG.rule_G8(real) if "D16" in b], (
        "a discharge to a section that DOES exist was rejected")


def test_w0_a_fabricated_row_cannot_wear_v2s_provenance():
    """The round trip walks BOTH directions. The first draft walked V2 -> register only, so a row
    invented here carrying `source: '...transcribed verbatim'` was undetectable: `--verify-
    transcription` said clean, `R0` said ok, and the counts still balanced. A hole V2 never
    carried would then be in the register wearing V2's provenance, and every instrument the plan
    builds on this file would inject from it."""
    reg = REG.load()
    reg["rows"].append(dict(REG.load()["rows"][0], id="H-13",
                            source="ARCHITECTURE_V2.md §VII.1, " + REG.TRANSCRIBED))
    bad = REG.verify_transcription(reg)
    assert any("H-13" in b and "fabricated" in b for b in bad), (
        "a fabricated row claiming V2's provenance passed the transcription check")


def test_w0_a_transcription_that_extracts_nothing_is_a_failure_not_a_pass():
    """§42.2's polarity rule, applied to this module. If Part VII's headings or row format change
    -- which `PLAN.md` §0.3 row 14 says is the PLAN -- the extractor returns nothing, and the first
    draft then reported `TRANSCRIPTION: clean` having compared zero rows, leaving every later
    register edit unpinned while the suite stayed green. `rule_G8` already applied this polarity
    to Part B; omitting it here was the asymmetry."""
    import unittest.mock as mock
    with mock.patch.object(REG, "v2_rows", lambda: {}):
        bad = REG.verify_transcription(REG.load())
    assert bad and "ZERO rows" in bad[0], "an empty extraction reported clean"


def test_w0_the_default_field_is_pinned_through_its_one_declared_normalisation():
    """`default` is the field an instrument injects FROM and the field R3 reads, and the first
    draft left it unpinned while the docstring named only `grade` as excluded. It is pinned now
    THROUGH `normalised_default`, which is the one editorial rule applied to it -- and that rule is
    load-bearing on a published number: transcribed literally, five `absent` rows would each fire
    R3 and R3 would read 7 rather than 2."""
    assert REG.normalised_default("none. ⚠ every contest is blocked") == "none"
    assert REG.normalised_default("none — §63.1 may accept it instead") == "none"
    assert REG.normalised_default("Part E's table") == "Part E's table", (
        "the normalisation swallowed a real default")
    drifted = REG.load()
    target = next(r for r in drifted["rows"] if r["id"] == "H-31")
    target["default"] = "four bands off the margin"
    assert any("H-31.default" in b for b in REG.verify_transcription(drifted)), (
        "a silently edited default passed the transcription check")


def test_w0_the_checker_fails_on_an_ungraded_row():
    """§42.2's polarity rule: *a row with no grade FAILS THE EXPORT*. Planted, not asserted about
    the source -- the property is that the checker REFUSES, not that a `grade` key is present."""
    reg = REG.load()
    reg["rows"][0]["grade"] = ""
    assert REG.rule_R1(reg), "an ungraded row passed R1"


def test_w0_the_checker_fails_on_a_default_for_an_absent_hole():
    """§42.2.1 in one line -- *the honest behaviour is to REFUSE, not to pick a plausible number*
    -- made mechanical. This is the rule that stops the register becoming a place to park
    plausible values under a refusal's name."""
    reg = REG.load()
    target = next(r for r in reg["rows"] if r["grade"] == "absent" and r["default"] == "none")
    before = len(REG.rule_R3(reg))
    target["default"] = "a plausible number"
    after = REG.rule_R3(reg)
    assert len(after) == before + 1 and any(target["id"] in b for b in after), (
        f"planting a default on absent row {target['id']} did not fail R3")


def test_w0_the_checker_fails_on_an_assumption_with_no_site_or_sweep():
    """§G's inject-declare-sweep doctrine is worthless if a default can be declared without
    saying WHERE it enters or WHAT ELSE was tried. H-10 is the one row V2 supplies a sweep for,
    so it is the one that can be broken in both directions."""
    reg = REG.load()
    h10 = next(r for r in reg["rows"] if r["id"] == "H-10")
    h10["site"], h10["sweep"] = "choose.budget", [2, 5, 9]
    assert not [b for b in REG.rule_R2(reg) if "H-10" in b], "a complete assumption row failed R2"
    h10["sweep"] = [5]
    assert [b for b in REG.rule_R2(reg) if "H-10" in b], "a one-point sweep passed R2"
    h10["sweep"], h10["site"] = [2, 5, 9], ""
    assert [b for b in REG.rule_R2(reg) if "H-10" in b], "an assumption with no site passed R2"


def test_w0_the_checker_fails_on_an_absent_row_with_no_cite():
    """Guardrail G6. `PLAN.md` §2.6: nobody ever ran `CLAUDE.md` §0's five tests over the twelve
    refusals, and run in chain eleven of twelve close or downgrade. A refusal nobody argued for
    is not a refusal, it is an omission wearing one."""
    reg = REG.load()
    target = next(r for r in reg["rows"] if r["grade"] == "absent")
    target["cite"] = "PLAN.md §3.1 -- test 4, precedent: #353 :927-930"
    assert not [b for b in REG.rule_G6(reg) if b.startswith(target["id"] + ":")], (
        "a cited absent row still failed G6")
    target["cite"] = "   "
    assert [b for b in REG.rule_G6(reg) if b.startswith(target["id"] + ":")], (
        "a whitespace-only cite passed G6")


def test_w0_the_row_shape_cannot_grow_quietly():
    """Rule R0. §G4 defines ten fields; this register declares two more in its header and no
    others. A shape nobody checks is a shape that grows, and the growth is always one useful
    field at a time."""
    reg = REG.load()
    assert not REG.rule_R0(reg), "R0: " + "; ".join(REG.rule_R0(reg))
    reg["rows"][0]["notes"] = "a useful extra field"
    assert REG.rule_R0(reg), "an undeclared key passed R0"


def test_w0_the_counts_are_computed_and_every_row_is_accounted_for():
    """G11: every number describing the register ships with the command that produces it, and the
    command is `python register.py --counts`. V2's hand-typed '39 holes / 13 assumption' over 32
    rows is why.

    ⚠ The first draft of this test asserted `sum(by_grade.values()) == rows` and claimed it
    reproduced V2's defect. IT CANNOT FAIL: `by_grade` is a `Counter` over exactly one value per
    row, so it sums to `len(rows)` for every possible register, including one where every grade is
    `None`. V2's defect was a HAND-TYPED tally diverging from computed rows; comparing a computed
    tally to itself is not that, and an assertion that cannot observe the failure it excludes is
    §0.1 point 2's named failure."""
    c = REG.counts(REG.load())
    # ⚠ W5 REPLACED A TWO-BUCKET ASSERTION THAT STOPPED BEING A PARTITION. It read
    # `rows == transcribed + added_by_plan`, which was true while every row came from V2 or from
    # PLAN §1.4 and became false the moment `W5` added rows found by EXECUTION. Two hardcoded
    # predicates cannot partition a set that grows a third member, so the buckets are derived
    # from the data and the partition is asserted over all of them — the same defect one level
    # up from the one this test's docstring already describes.
    assert sum(c["by_source"].values()) == c["rows"], (
        f"{c['rows']} rows but the source buckets sum to {sum(c['by_source'].values())}: "
        f"{c['by_source']}")
    assert "unattributed" not in c["by_source"], (
        f"a row carries no `source:` at all: {c['by_source']}")
    assert len(c["by_source"]) >= 3, (
        f"only {len(c['by_source'])} source(s) — this test cannot observe a bucket falling out "
        f"of the total if there is effectively one bucket: {c['by_source']}")
    # and the planted failure, so the partition assertion is known to be able to fail.
    planted = REG.load()
    planted["rows"][0] = dict(planted["rows"][0], source="")
    assert "unattributed" in REG.counts(planted)["by_source"], (
        "a row with an empty `source:` was silently folded into a real bucket")
    assert c["tier0"] + c["tier1"] == c["rows"], "a row sits in neither tier"
    # The grade tally must cover every row -- which is a real claim, because `rule_R1` admits only
    # four grades and a row could carry none. Planted, so the assertion is known to be able to
    # fail.
    graded = REG.load()
    assert sum(c["by_grade"].get(g, 0) for g in REG.GRADES) == c["rows"]
    graded["rows"][0]["grade"] = "unmeasured"
    broken = REG.counts(graded)
    assert sum(broken["by_grade"].get(g, 0) for g in REG.GRADES) != broken["rows"], (
        "a row graded outside the closed set still counted toward the tally")


def test_w0_artifact_0_is_computed_from_the_rows_rather_than_asserted():
    """Artifact 0 is *Part VII has no `absent` row in Tier 0*. This pins the COMPUTATION, not the
    answer.

    ⚠ The first draft asserted `c["tier0_absent"]` -- i.e. it pinned the register in its DEFECTIVE
    state, and would have gone red the moment `W1`/`W3` succeeded, which is their stated Proof.
    That is the same category error as a string test, with the sign reversed: it bound the state of
    the data instead of the behaviour of the checker. What is worth pinning is that the instrument
    DERIVES the verdict from the rows, so that closing a row moves it and deleting a row does
    not go unnoticed."""
    reg = REG.load()
    reported = set(REG.counts(reg)["tier0_absent"])
    truth = {r["id"] for r in reg["rows"] if r["tier"] == 0 and r["grade"] == "absent"}
    assert reported == truth, f"reported {sorted(reported)}, rows say {sorted(truth)}"
    # Close every one of them and artifact 0 must flip to MET -- so a future W1/W3 run turns this
    # green rather than red, and a DELETED row is caught by the transcription test instead.
    for r in reg["rows"]:
        if r["tier"] == 0 and r["grade"] == "absent":
            r["grade"], r["cite"] = "ruled", "planted"
    assert not REG.counts(reg)["tier0_absent"], (
        "artifact 0 still reports UNMET after every Tier 0 `absent` row was closed")


# ===========================================================================
# W1 -- THE FIVE TESTS, RUN AND WRITTEN INTO THE ROWS
#
# `PLAN.md` PART 9 gives the falsifier for this item in one line: *"a cited line that does not say
# what §3.1-§3.4 claims it says. Every citation is a file and a line; check them."* A closure
# resting on a line that does not say what the row claims is worse than an open hole -- the hole is
# visible and the false closure is not. `CLAUDE.md` §0 calls the repository's anti-fabrication gate
# leaky and says to verify provenance BY HAND against the cited source; these tests are that check
# mechanised, so it stops depending on anyone remembering.
# ===========================================================================

def test_w1_every_citation_in_the_register_resolves_in_353():
    """Every `:NNN` a `cite:` names exists in #353, and every verbatim quote is at the line cited.
    Fourteen rows were closed or re-graded on citations; this is what stops the fifteenth being
    closed on one nobody checked."""
    bad = REG.verify_citations(REG.load())
    assert not bad, "unresolved citations:\n  " + "\n  ".join(bad)


def test_w1_the_citation_gate_tells_a_fabrication_from_a_wrong_line_number():
    """They are DIFFERENT DEFECTS and collapsing them would be the same error as reporting a
    verified citation as fabricated -- which is what the first version of this gate did to all
    eight quotes it was given, because it compared typography instead of prose. A quote wrapped
    across lines, inside a blockquote, with `**emphasis**` mid-clause and an em-dash where the
    cite typed two hyphens, is the SAME CLAIM."""
    reg = REG.load()
    row = next(r for r in reg["rows"] if r["id"] == "H-23")
    kept = row["cite"]

    row["cite"] = '#353 :929-930 VERBATIM: "A petition costs standing when it is refused."'
    bad = REG.verify_citations(reg)
    assert any("FABRICATED" in b for b in bad), "a quote #353 does not contain passed"

    row["cite"] = '#353 :100 VERBATIM: "No cost clause is required"'
    bad = REG.verify_citations(reg)
    assert any("LINE NUMBER is wrong" in b for b in bad), (
        "a real quote at the wrong line was not distinguished from a fabrication")

    row["cite"] = "#353 :9999 -- see there"
    bad = REG.verify_citations(reg)
    assert any("lines" in b and "9999" in b for b in bad), (
        f"a line number past the end of the file passed: {bad}")

    row["cite"] = kept
    assert not REG.verify_citations(reg), "the restored citation stopped resolving"


def test_w1_a_register_whose_citations_carry_no_line_reference_fails():
    """§42.2's polarity rule again. A `cite:` field full of prose that names no line verifies
    nothing, and reporting `all resolve` over it would be the strongest possible false green."""
    reg = REG.load()
    for r in reg["rows"]:
        if r["cite"]:
            r["cite"] = "answered in chain, trust me"
    bad = REG.verify_citations(reg)
    assert bad and "nothing was verified" in bad[0], (
        "citations with no line references reported as resolving")


def test_w1_every_row_the_ladder_visited_carries_its_reasoning():
    """§3.1-§3.4 name fourteen rows. This asserts the PROPERTY that survives a re-grade -- each
    was visited and carries the reasoning -- not the grades themselves.

    ⚠ THE FIRST DRAFT PINNED THE GRADES, and an adversarial pass called it: a pin on
    `H-36 == "ruled"` breaks the moment the objection that commit OFFERED is accepted, which is
    the mechanism working, not a regression. It broke twice within the hour -- once when the pass
    overturned four closures, once when Jordan ruled H-36 -- and both times it failed for the
    RIGHT reason, which is the definition of a test that should not exist in that form. The
    grade-shaped properties are already asserted generically by `rule_R2` (an `assumption` has a
    site and three distinct sweep points) and `verify_citations` (every citation resolves)."""
    reg = {r["id"]: r for r in REG.load()["rows"]}
    LADDER = ("H-20", "H-23", "H-25", "H-26", "H-27", "H-28", "H-31",
              "H-32", "H-33", "H-36", "H-37", "H-38", "H-39", "H-60")
    for rid in LADDER:
        r = reg[rid]
        assert r["cite"].strip(), f"{rid} was visited by the ladder and carries no reasoning"
        assert "PLAN" in r["cite"] or "RULED BY JORDAN" in r["cite"], (
            f"{rid}'s cite does not say which ladder step or ruling put it there: {r['cite'][:80]}")
    assert reg["H-26"]["tier"] == 0, "H-26 was to move to Tier 0 (`yield` is the only matter source)"
    # H-33's sweep MUST retain total fan-out as an ARM -- it is #353's specified behaviour and
    # therefore the control any predicate is measured against (W6's guardrail). Asserted on the
    # arm, not on a substring: `"total fan-out removed"` contains "total".
    arms = [str(x).split("(")[0].strip().lower() for x in reg["H-33"]["sweep"]]
    assert any(a.startswith("total") for a in arms), (
        f"H-33's sweep dropped total fan-out, which is the control: {reg['H-33']['sweep']}")


# ===========================================================================
# W2 -- PART D AS DATA, AND `write()` READS IT
#
# THE DEFECT: #353 §30's matrix names THINGS -- `stance`, `condition`, `Tenure` -- and L4's rule is
# stated over `(kind, field)`. Keying the gate on the thing meant `(Person, convictions)` rode on
# `stance`'s row, so a real gap silently became a PASS. `MATRIX_FIELD_OF` existed only to say which
# fields were ALLOWED to ride on which rows: the defect, written down as a table.
#
# W2's stated Proof is an AST WALK, and the reason is `G3` in one line: *a test asserts the
# PROPERTY, never the string.* Grepping `shape.py` for `record_kind="..."` finds the sites someone
# spelled that way; walking the tree finds every site there is, and reports the ones it cannot
# resolve rather than skipping them.
# ===========================================================================

def _write_call_sites(*paths):
    """Every store-API `write(...)` call, from the syntax tree. Returns literal `(kind, field)`
    pairs and, separately, the sites whose arguments are not literals -- because a site the walk
    CANNOT resolve is a hole in the check and must be reported, not dropped."""
    import ast as ast_
    pairs, dynamic = {}, []
    for path in paths:
        tree = ast_.parse((HERE / path).read_text())
        for node in ast_.walk(tree):
            if not (isinstance(node, ast_.Call) and isinstance(node.func, ast_.Attribute)
                    and node.func.attr == "write"):
                continue
            recv = node.func.value
            if isinstance(recv, ast_.Name) and recv.id == "TRACE":
                continue                      # the trace channel, not the store API
            kw = {k.arg: k.value for k in node.keywords if k.arg}
            def lit(name, pos):
                v = kw.get(name)
                if v is None and len(node.args) > pos:
                    v = node.args[pos]
                return v.value if isinstance(v, ast_.Constant) and isinstance(v.value, str) else None
            rk, fn = lit("record_kind", 3), lit("fieldname", 4)
            if rk and fn:
                pairs.setdefault((rk, fn), []).append(f"{path}:{node.lineno}")
            else:
                dynamic.append(f"{path}:{node.lineno}")
    return pairs, dynamic


def test_w2_every_write_call_site_names_a_pair_on_the_matrix():
    """W2's Proof. Walk the tree, do not grep the string.

    ⚠ Sites whose `record_kind`/`fieldname` are not literals are reported as a HOLE IN THIS CHECK
    rather than skipped: a walk that silently ignores what it cannot read is a walk that reports
    `clean` over an unknown number of unchecked writes."""
    pairs, dynamic = _write_call_sites("shape.py", "probes.py")
    assert pairs, "the AST walk found no write call sites at all -- the walk is broken"
    # W3: THE FOLD'S WRITE IS GENERIC BY CONSTRUCTION -- `_apply_write` passes the pair as
    # variables, because one `resolve` serving 32 verbs cannot name a literal. Its coverage did
    # not vanish, it MOVED AND GOT STRONGER: `_load_verb_table` checks every `writes:` of every
    # verb against the matrix AT LOAD, which covers verbs no probe exercises, where this walk
    # covers only sites someone wrote. The exemption is declared, and the test asserts the
    # load-time check is really there rather than taking the comment's word for it.
    # ⚠ LEXICAL CONTAINMENT, NOT LINE PROXIMITY. This exempted a dynamic write site within 25
    # LINES of any line mentioning `_apply_write` — a distance heuristic, and adding eight lines
    # to that function's body pushed its own `w.write` call outside its own exemption. The
    # property is *"this call is inside `_apply_write`"*, and the AST answers it exactly. `G3`:
    # assert the property, never the proxy. Found while reconciling the governance-slice pass.
    import ast as _ast
    _tree = _ast.parse((HERE / "shape.py").read_text())
    fold_span = next(((n.lineno, n.end_lineno) for n in _ast.walk(_tree)
                      if isinstance(n, _ast.FunctionDef) and n.name == "_apply_write"), None)
    assert fold_span, "`_apply_write` is gone; the fold's declared exemption names nothing"
    unexplained = [d for d in dynamic
                   if not (fold_span[0] <= int(d.split(":")[1]) <= fold_span[1])]
    assert not unexplained, (
        "write call sites whose (record_kind, fieldname) are not literals and are not the fold: "
        f"{unexplained}")
    # ⚠ THE FIRST VERSION OF THIS ASSERTION WAS A SUBSTRING MATCH ON `shape.py`'s SOURCE — which
    # is G3's own worked example of what not to do, committed inside the exemption that invokes
    # G3. Delete the loader's check, leave the message in a comment, and it passed. The property
    # is exercised instead: a verb whose `writes:` names a pair off the matrix must make the
    # LOADER refuse, which is what the exemption claims covers the fold.
    import copy as _copy, yaml as _yaml
    doc = _yaml.safe_load((REG.ARCH_DIR / "verb_table.yaml").read_text())
    doc["verbs"][0] = dict(doc["verbs"][0], writes=["Person.no_such_field"])
    import unittest.mock as _mock, io as _io
    with _mock.patch.object(S, "VERB_TABLE_YAML") as fake:
        fake.exists.return_value = True
        fake.read_text.return_value = _yaml.safe_dump(doc)
        with pytest.raises(SystemExit) as e:
            S._load_verb_table()
    assert "no row of" in str(e.value), (
        "the verb-table loader no longer refuses a `writes:` off the matrix, so the fold's "
        f"generic write has NO coverage and the exemption above is void: {e.value}")
    off = {p: where for p, where in pairs.items()
           if p not in S.MATRIX and p not in S.MATRIX_RETIRED}
    assert not off, (
        "write call sites naming a `(kind, field)` on no row of write_matrix.yaml:\n  "
        + "\n  ".join(f"{k}: {v}" for k, v in sorted(off.items()))
        + "\nEither the row is missing from Part D, or the site is writing a field the design "
          "does not have. Rule the row first, then add it -- the reverse order invents the thing "
          "the rule prevents.")


def test_w2_a_planted_write_to_an_unruled_field_raises_and_names_the_pair():
    """`(Person, mood)` is W2's own planted example. The refusal must NAME the pair: a reader who
    cannot tell WHICH cell is unmarked cannot rule the row, and §42.2.1's whole point is that the
    honest behaviour is to refuse rather than to pick a plausible value."""
    w = _w()
    w.step = Step.RESOLVE
    with pytest.raises(Unspecified) as e:
        w.write("stance", WriteClass.ACTS, lambda: None,
                record_kind="Person", fieldname="mood", driver="Act")
    msg = str(e.value)
    assert "Person" in msg and "mood" in msg, f"the refusal did not name the pair: {msg}"
    assert "stance" not in msg, (
        "the refusal named the `thing` argument -- that is the parameter that carried defect D1 "
        "and it must not be able to stand in for the pair")


def test_w2_the_retired_rows_get_their_own_diagnosis():
    """A row that was RETIRED and a row that never existed are different facts about the design,
    and a reader deciding whether to add one needs to know which they are looking at. Two of the
    six come back at W3 WITH `establish`, their producer."""
    assert S.MATRIX_RETIRED, "nothing is recorded as retired -- the distinction is gone"
    for kind, fname in S.MATRIX_RETIRED:
        assert (kind, fname) not in S.MATRIX, f"({kind}, {fname}) is both retired and live"
        with pytest.raises(Unspecified) as e:
            S.partition_lookup(kind, fname)
        assert "RETIRED" in str(e.value), (
            f"({kind}, {fname}) is retired and its refusal does not say so")


def test_w2_the_class_column_is_derived_and_cross_checked():
    """`class:` is V2's prose and `STEP_CLASS` is this file's derivation. The loader raises if they
    disagree, so neither can drift into being trusted alone. CENSUS writes in the MATTER class --
    §30's reconciliation is a world write, not an act."""
    assert S.STEP_CLASS[Step.CENSUS] is WriteClass.MATTER
    assert S.STEP_CLASS[Step.WITNESS] is WriteClass.INTERIOR
    assert S.STEP_CLASS[Step.RESOLVE] is WriteClass.ACTS
    for (kind, fname), row in S.MATRIX.items():
        for st in row.steps:
            assert row.write_class(st) is S.STEP_CLASS[st], f"({kind}, {fname}) at {st}"


# ===========================================================================
# JORDAN'S 2026-09-02 RULING — DEFINITIONS ARE NOT HARDCODED
#
# Verbatim, across four messages: *"please note that convictions roster and axes etc may be
# modified in future"* … *"that goes for all"* … *"these must be easy to modify"* … *"I do not
# want definitions etc to be hardcoded."*
#
# THIS IS A GUARD ON THE GAME, NOT ON THE APPARATUS, which is what licenses it under `CLAUDE.md`
# §0.1 point 5 as amended: the artifact it protects is the set of definitions the loop RESOLVES
# FROM, so a defect here changes what the game does. It fails on a NEW hardcoded roster, which is
# the recurrence — not on the six that were moved, which is history.
# ===========================================================================

# Declared roster exemptions may shrink, never grow without an argument made here.
# 12 -> 13, W5: `_TenureView._MUTATORS` in `shape.py`. The argument, since the ceiling demands one:
# it is a list of PYTHON'S OWN mutator method names, fixed by the language and editable by nobody,
# so it fails rosters.yaml's test in the direction that exempts — changing it changes how the code
# works, never what the game is. It is the first exemption this guard has earned on its own author.
# 13 -> 14, W5: `View.__slots__`, for the same reason — a language construct naming the class's
# own attributes, which crossed the three-element threshold when the View gained `question`.
EXEMPT_CEILING = 14


def test_jordan_no_definition_is_hardcoded_in_a_body():
    """Walk the tree for a literal collection of strings — a roster, a taxonomy, a kind list.
    Every one must come from `rosters.yaml`.

    ⚠ THE FIRST DRAFT WAS EVADABLE BY EVERY ROUTE AN ADVERSARIAL PASS TRIED, and the list is worth
    keeping because each was a real hole: `frozenset([...])`, `set(...)`, `tuple(...)` and
    `"a b c".split()` are `Call` nodes and it only looked at `Tuple|List|Set`; a dict literal
    evaded it; anything not at module scope — function-local, class attribute, inside an `if` —
    evaded it because it walked `tree.body` rather than the whole tree; and IT READ `shape.py`
    ALONE while `probes.py`, `report.py` and `run_cases.py` went unscanned.

    Its docstring invoked `G2` — *forbid the shape, never enumerate the words* — while enumerating
    a syntactic shape, which is a router over AST node types, and routers miss. This version walks
    every node of every module and looks at the VALUE: a collection of three or more string
    constants, however it is spelled."""
    import ast as ast_
    # `shape.py` IS THE MODEL — where a game definition would live, and where Jordan's ruling
    # bites. The other three are the test corpus and the reporter: a fixture in a probe is test
    # data, not a definition the game resolves from, so flagging every one of them would bury the
    # signal. They are checked for the defect that DOES matter there — a roster DUPLICATED from
    # the data file, which is how a definition comes back after being moved.
    MODEL = "shape.py"
    # ⚠ THE CORPUS IS DISCOVERED, NOT LISTED, AND THE DIFFERENCE IS THIS TEST'S OWN LESSON. Its
    # docstring names the original defect as "IT READ `shape.py` ALONE while `probes.py`,
    # `report.py` and `run_cases.py` went unscanned" — and the fix was a hardcoded four-name
    # tuple, so `headless.py` and `delta.py`, added by `W9`, were unscanned BY CONSTRUCTION. A
    # filename roster is a router and `G2` forbids the shape: forbid it, never enumerate it.
    # Every module in the instrument directory except this file is the corpus.
    CORPUS = tuple(sorted(f.name for f in HERE.glob("*.py")
                          if f.name not in (MODEL, "test_tracer_is_honest.py")))
    assert {"probes.py", "report.py", "run_cases.py", "headless.py"} <= set(CORPUS), CORPUS
    FILES = (MODEL,) + CORPUS
    # ⚠ A ROSTER ROW NEED NOT CARRY `values:`. `witness_channel_predicates` carries only
    # `predicates:` — the five names live once, in `witness_channels`, and that row states what
    # each MEANS. Assuming the key existed made this guard raise a KeyError on a data shape the
    # file legitimately supports, which is a guard failing on correct data (`G4`).
    known = {frozenset(r["values"]) for r in S._ROSTERS.values() if "values" in r}
    offenders, exempted = [], []
    for fname in FILES:
        tree = ast_.parse((HERE / fname).read_text())
        for node in ast_.walk(tree):
            elts = None
            if isinstance(node, (ast_.Tuple, ast_.List, ast_.Set)):
                elts = node.elts
            elif isinstance(node, ast_.Call) and isinstance(node.func, ast_.Name) \
                    and node.func.id in ("frozenset", "set", "tuple", "list") and node.args:
                a = node.args[0]
                elts = a.elts if isinstance(a, (ast_.Tuple, ast_.List, ast_.Set)) else None
            elif (isinstance(node, ast_.Call) and isinstance(node.func, ast_.Attribute)
                  and node.func.attr == "split"
                  and isinstance(node.func.value, ast_.Constant)
                  and isinstance(node.func.value.value, str)):
                # `"a b c".split()` — a roster spelled as one string. Synthesise the constants so
                # the value test below sees the same thing it would see in a tuple.
                parts = node.func.value.value.split()
                elts = [ast_.Constant(value=x) for x in parts]
            elif isinstance(node, ast_.Dict) and node.keys:
                elts = [k for k in node.keys if k is not None]
            if not elts or len(elts) < 3:
                continue
            if not all(isinstance(e, ast_.Constant) and isinstance(e.value, str) for e in elts):
                continue
            vals = [e.value for e in elts]
            # A collection of IDENTIFIERS is a roster. A collection of SENTENCES is prose — an
            # error message, a docstring table, a list of alternatives for a TRACE decision — and
            # those are not definitions the game resolves from. The split is on the values, not on
            # a name list, so it cannot be spelled around.
            if not all(v and len(v) < 40 and " " not in v.strip() for v in vals):
                continue
            # AN EXEMPTION IS DECLARED AT THE SITE, WITH A REASON, on the line or the one above:
            #     # roster-exempt: <why this is mechanism and not a definition>
            # NOT a whitelist of names — G2 — because a name list is a router and this one would
            # need to grow every time a variable is renamed. The reason is visible where the
            # decision is made, and the COUNT IS PINNED below so exemptions cannot creep.
            src_lines = (HERE / fname).read_text().splitlines()
            # Look back far enough for a multi-line reason. A one-line window would force the
            # reason to be short, and a short reason is the one nobody can evaluate.
            ctx = " ".join(src_lines[max(0, node.lineno - 9):node.lineno])
            if "roster-exempt:" in ctx:
                exempted.append((fname, node.lineno))
                continue
            if fname != MODEL:
                # In the corpus, only a DUPLICATE of a roster that is already data is a defect:
                # the same closed set written out again, which is the definition coming back.
                if frozenset(vals) not in known:
                    continue
                offenders.append((fname, node.lineno, vals[:6]))
                continue
            offenders.append((fname, node.lineno, vals[:6]))
    # The ratchet. Exemptions are declared, counted, and may SHRINK but never grow without a
    # deliberate edit here — which is the point at which someone has to justify the growth.
    assert len(exempted) <= EXEMPT_CEILING, (
        f"{len(exempted)} roster-exempt sites, ceiling is {EXEMPT_CEILING}. An exemption is a "
        "definition someone decided the game does not resolve from; growing the count needs an "
        "argument, not a bump.")
    assert not offenders, (
        "literal rosters — Jordan 2026-09-02, definitions are not hardcoded. In `shape.py`, move "
        "it to `rosters.yaml` and read it with `roster()`; in the corpus, a hit is a roster "
        "DUPLICATED from the data file and must read it instead:\n  "
        + "\n  ".join(f"{f}:{ln} {v}" for f, ln, v in offenders))


def test_jordan_every_roster_comes_from_the_data_file_and_an_absent_one_refuses():
    """The six that moved must actually be READ, not merely copied — and a roster the file does
    not carry must RAISE. An empty set would make every membership test silently false and every
    closed-set guard vacuous, which is §42.2's polarity rule inverted."""
    for name, value in (("tenure_kinds", S.TENURE_KINDS), ("rung_kinds", S.RUNG_KINDS),
                        ("remit_acts", S.REMIT_ACTS), ("witness_channels", S.WITNESS_CHANNELS),
                        ("claim_sources", S.CLAIM_SOURCES), ("strata", S.STRATA)):
        assert set(value) == set(S._ROSTERS[name]["values"]), f"{name} diverged from the data"
        assert value, f"{name} loaded empty"
    with pytest.raises(Unspecified):
        S.roster("a_roster_nobody_declared")
    # Order is semantic for the strata — the fold resolves in sequence — so it must be a tuple
    # and must match the file's order, not a set's arbitrary one.
    assert isinstance(S.STRATA, tuple) and list(S.STRATA) == S._ROSTERS["strata"]["values"]


def test_jordan_a_roster_edit_is_a_data_edit_and_nothing_else():
    """The point of the ruling, made falsifiable: changing a roster must not require touching
    code. This edits the loaded data and asserts the change reaches the accessor the loop uses.

    ⚠ WHAT IT DOES NOT CLAIM, because a mutation showed the first draft overclaimed it. The six
    module constants (`S.STRATA` and friends) are bound ONCE AT IMPORT, so editing the YAML does
    not change them in a running process — you edit the file and start again, which is ordinary
    and is not what the ruling is about. The ruling is about WHERE THE DEFINITION LIVES. A test
    that failed on an import-time binding would be guarding a non-defect, and `CLAUDE.md` §0.1
    point 5 says a guard must earn its existence."""
    before = set(S.roster("tenure_kinds"))
    S._ROSTERS["tenure_kinds"]["values"].append("_planted_kind")
    try:
        assert "_planted_kind" in S.roster("tenure_kinds"), (
            "a roster edit did not reach the accessor — something cached or copied the values, "
            "which reintroduces the hardcoding one level down")
    finally:
        S._ROSTERS["tenure_kinds"]["values"].remove("_planted_kind")
    assert set(S.roster("tenure_kinds")) == before


def test_w3_the_fold_refuses_rather_than_filling_and_the_gap_is_countable():
    """The fold's three fills — eligibility, `requires`, effects — must REFUSE where they cannot
    evaluate, never admit. G1: a fill off the register is a red test, and §42.2 sends zero evidence
    to the verdict AGAINST the thing measured, so a predicate that cannot be evaluated must not
    return True.

    ⚠ TWO OF THE THREE GOT THIS WRONG IN THE FIRST DRAFT. `presence:` eligibility returned True
    unconditionally with the comment "the presence index is H-33; not resolvable here" — an
    unevaluable predicate admitting. And `_req_work` checked `condition >= 0`, which is EVERY
    possible condition: a predicate that cannot fail is a `return True` with a docstring."""
    prose = [v for v, r in S.VERB_TABLE.items()
             if r.requires.strip() not in S.NO_PRECONDITION]
    assert prose, "no verb carries a precondition -- the check is vacuous"
    # The gap is COUNTABLE, which is what stops it being forgotten: H-65's number.
    missing = [v for v in prose if v not in S.REQUIRES_PREDICATES]
    assert len(missing) == len(prose) - len(
        [v for v in prose if v in S.REQUIRES_PREDICATES])

    # A verb with a prose precondition and no predicate must REFUSE, not succeed.
    w = _w()
    w.step = Step.RESOLVE
    d = S.SeasonDriver(w)
    victim = next(v for v in missing)
    act = S.Act(id="a_x", actor="p_low", verb=victim)
    with pytest.raises(Unspecified) as e:
        d._fold(w, act)
    assert "precondition" in str(e.value) or "no row" in str(e.value)

    # `_req_work` must be able to FAIL. A site below every floor is unworkable.
    site = w.sites["site_harbour"]
    kept, site.condition = site.condition, 0
    try:
        ch = S.StateChange(site.id, "alter", "Act", "condition", -1)
        assert not S._req_work(w, S.Act(id="a_w", actor="p_low", verb="work", changes=[ch])), (
            "`work`'s precondition admitted a site at condition 0 -- it cannot observe the "
            "failure it excludes")
    finally:
        site.condition = kept


def test_w3_the_write_class_check_still_refuses_a_wrong_class():
    """§30.2: *the write class is a PARAMETER of the store API, checked PER WRITE SITE.*

    ⚠ HONEST LIMIT, NAMED RATHER THAN LEFT TO BE FOUND. For the FOLD's own writes the check is
    CIRCULAR: `_apply_write` passes `mrow.write_class(step)` and `World.write` computes the same
    expression from the same map, so `expect is wclass` always holds. That is not a defect to fix
    by contriving a second opinion — a table-driven fold and its gate necessarily read one table —
    but it does mean the per-site check no longer catches anything for the 32 table verbs, and the
    coverage claim must not be made for them.

    What the gate DOES still enforce is that a caller passing a WRONG class is refused, which is
    what the check is for. That is exercised here directly, since no fold write can exercise it."""
    w = _w()
    w.step = Step.RESOLVE
    # `(Rung, stores)` at RESOLVE is the ACTS class. MATTER must be refused.
    with pytest.raises(Forbidden) as e:
        w.write("stores", WriteClass.MATTER, lambda: None,
                record_kind="Rung", fieldname="stores", driver="Act")
    assert "class" in str(e.value).lower(), str(e.value)
    # And the right class is admitted, so the refusal above is about the CLASS and not the row.
    w.write("stores", WriteClass.ACTS, lambda: None,
            record_kind="Rung", fieldname="stores", driver="Act")


def test_w5_no_gap_is_an_instrument_defect():
    """No probe's GAP may be caused by the instrument being called wrong (`InstrumentDefect`).

    ⚠ THE DEFECT THIS PINS IS THE WORST ONE THIS TOOL CAN HAVE. Its whole output is the claim
    "here is what #353 does not specify". `W5` moved the Tenure store onto its subject, three
    probes kept writing `w.tenures += [...]`, and because `run_cases` files every `ShapeGap` as a
    GAP, three PROBE BUGS were reported as holes in the design — the gap count went 73 → 76 in
    the direction that flatters the instrument. §0.1 point 4: a number without a control is not a
    measurement, in EITHER direction.

    §0.1 point 2 — an assertion must be able to OBSERVE the failure it excludes — so the test
    plants the failure first and checks the plant was seen, rather than trusting a clean run."""
    # ---- the plant, ROUTED THROUGH THE REAL CLASSIFIER. ----
    # ⚠ THE FIRST VERSION NEVER TOUCHED IT. It read `RC._verdict_for(...) if hasattr(RC,
    # "_verdict_for") else None` — and `run_cases` has no `_verdict_for`, so the branch was dead
    # and the "plant" was graded by this test's own inline copy of `run_probe`'s try/except. A
    # falsifier that re-implements the thing it is falsifying tests nothing about it. The probe
    # is registered in `P.PROBES` and run by `R.run_probe`, which is the code that decides
    # whether a call-site bug lands in the GAP column.
    def called_wrong():
        w = _w()
        w.tenures.append(S.Tenure("t_plant", "p_mid", "off_x", "hold", since=0))

    P.PROBES["PLANT"] = dict(id="PLANT", title="planted", section="S15.1", by="probe-model",
                             tests="a call-site bug must not grade as a design hole",
                             fn=called_wrong)
    try:
        R._VERDICTS.pop("PLANT", None)
        planted = R.run_probe("PLANT")
    finally:
        P.PROBES.pop("PLANT", None)
        R._VERDICTS.pop("PLANT", None)
    assert planted["verdict"] == "INSTRUMENT-ERROR", (
        f"a call-site bug graded {planted['verdict']!r}, not INSTRUMENT-ERROR. If it grades GAP "
        "the instrument is counting its own bugs as holes in #353, which is the defect this test "
        "exists for — check `InstrumentDefect` is not a `ShapeGap`.")

    # ---- and the real corpus is clean of them. ----
    assert not issubclass(S.InstrumentDefect, S.ShapeGap), (
        "InstrumentDefect became a ShapeGap — every call-site bug is now reportable as a design "
        "hole again, and the plant above would stop catching it.")
    runs = HERE.parent / "runs"
    results = json.loads((runs / "results.json").read_text())
    errs = sorted(k for k, v in results["_probes"].items()
                  if v.get("verdict") == "INSTRUMENT-ERROR")
    assert not errs, (
        f"{len(errs)} probe(s) fail with an instrument defect rather than running: {errs}. "
        "These are bugs in the probe or in shape.py, not findings about #353, and they must be "
        "fixed rather than published.")


# ===========================================================================
# W5 — PART F. The four proofs PLAN.md names, plus the two defects found building it.
# ===========================================================================

def test_w5_opening_set_has_no_roster_and_is_computed_from_the_table():
    """PLAN `W5`'s first proof, and `D2` entire: `Query.opening_set` has NO `roster` parameter.

    Tests the PROPERTY as well as the name (G3) — a parameter renamed `options` would satisfy the
    name test and be the same defect — by checking the set MOVES with the verb table."""
    params = list(inspect.signature(S.Query.opening_set).parameters)
    assert "roster" not in params, f"the roster survived: {params}"
    assert params == ["p", "v", "q"], f"§F1 types it `opening_set(p, view, q)`; got {params}"

    w = P.tiny_world()
    p = w.persons["p_mid"]
    q = S.Question("q:t", "need", ("rec_writ", "S"))
    v = S.View(p.id, [], w.fixtures.get("view_k"), q)
    got = S.Query.opening_set(p, v, q)
    assert got, "the computed set is empty — nothing is derivable and the roster is only absent"
    assert all(c.verb in S.VERB_TABLE for c in got)

    # THE PROPERTY: it is derived from the table, so removing a table row removes its candidates.
    victim = sorted({c.verb for c in got})[0]
    saved = S.VERB_TABLE.pop(victim)
    try:
        after = {c.verb for c in S.Query.opening_set(p, v, q)}
    finally:
        S.VERB_TABLE[victim] = saved
    assert victim not in after, (
        f"{victim!r} survived being removed from the verb table — the set is not computed from it")


def test_w5_q_has_a_producer_across_all_four_sources():
    """PLAN `W5` / `H-04` / §61. Each of the four sources produces a question ON ITS OWN, tested
    one at a time so a source that never fires cannot hide behind one that does — §0.1 point 2.

    ⚠ V2 §F1 SAYS "EXACTLY THREE SOURCES, AND BY NOTHING ELSE". Q4 is the fourth and PLAN `W5`
    is why: without it "an NPC with a standing ambition and a quiet season forms no candidates at
    all", which is most of the NPC corpus."""
    seen = {}
    for src in S.QUESTION_SOURCES:
        w = P.tiny_world()
        p = w.persons["p_mid"]
        if src == "date_due":
            w.dates["d_t"] = dict(due_at=0, holder=p.id, fired=False)
            w.docket.append({"date": "d_t", "matter": "m_t"})
        elif src == "claim_landed":
            # ⚠ THE PREVIOUS SEASON'S DEPOSIT. §F1 Q2 is a claim landing AT WITNESS, which runs at
            # the END of a season, so DELIBERATE reads it one tick later. The first version
            # planted at `w.tick` and passed against a producer that tested the same tick — both
            # sides shared the off-by-one, so the test could not observe it. `headless.py` could:
            # every ledger filled and no question ever formed.
            w.tick = 1
            p.ledger.append(S.Claim("c_t", p.id, p.id, "office", "duke", 0,
                                    "told_by", 100, "own"))
        elif src == "band_crossed":
            # ⚠ REV 1 PLANTED A TUPLE THE WRITER NEVER PRODUCES, AND SO TESTED ITSELF. It wrote
            # `w.crossings.append((p.id, "subsistence", 0))` -- a PERSON-keyed 3-tuple. `matter()`
            # appends `(site_id, verb, before, after, event_id)`, a SITE-keyed 5-tuple, and the
            # reader compared element 0 to `p.id`, so Q3 produced ZERO questions in every real run
            # while this assertion stayed green. The test and the reader shared a wrong shape, the
            # same off-by-one failure the `claim_landed` arm above already records.
            #
            # ⚠ NOW DRIVEN THROUGH THE REAL WRITER. A site at the person's own rung is worn past a
            # floor by `matter()`, so the tuple under test is the one the loop actually emits, and
            # the question forms because the person is PRESENT to notice it.
            here = next((t.object for t in w.tenures
                         if t.subject == p.id and t.kind == "contain" and t.until is None), None)
            assert here is not None, "the fixture person is contained nowhere; Q3 needs a place"
            # The site kind and its floors are read from the fixture, never typed here -- the
            # floors are per-KIND (`band_floors: {harbour: ..., seam: ..., body: ...}`), so a kind
            # this table does not carry has no floor to cross and the arm would be vacuous again.
            floors_by_kind = w.fixtures.get("band_floors")
            kind = next(k for k in floors_by_kind if k != "body")
            top = max(floors_by_kind[kind].values())
            w.sites["s_q3"] = S.Site("s_q3", here, kind, top + 5, [])
            S.SeasonDriver(w).matter()
            assert w.crossings, "the fixture no longer crosses a floor -- Q3 has nothing to read"
            assert w.crossings[0][0] in w.sites, (
                "a crossing is keyed on something that is not a site; the writer changed shape")
        elif src == "need":
            pr = S.Proposition("pr_t", "OUGHT", "rec_writ", "it should stand", True, 0)
            w.propositions[pr.id] = pr
            w.add_tenure(S.Tenure("t_t", p.id, pr.id, "commit", since=0))
        else:
            pytest.fail(f"the roster grew a source this test does not exercise: {src!r}")
        qs = S.questions_for(w, p)
        seen[src] = [q.source for q in qs]
        assert src in seen[src], f"source {src!r} produced no question: {seen}"
    assert len(seen) == 4, seen


def test_w5_f2s_third_term_cannot_change_any_decision():
    """A DEFECT IN §F2, FOUND BY BUILDING IT, and reported rather than smoothed away.

    §F2 scores `Σ_axis conviction·alignment(c.verb, axis) + stance_toward(c.subject) +
    urgency(sensation.subsistence)`. The third term HAS NO `c` IN IT, so it is added identically
    to every candidate and cannot move a ranking `choose` then slices. It is inert BY
    CONSTRUCTION — the dead-carrier shape #353 `:739-744` names, arriving in a scoring function
    instead of in a field.

    This asserts the inertness rather than describing it, so if a later revision makes urgency
    candidate-dependent the test goes red and the finding is retired by evidence."""
    w = P.tiny_world()
    p = w.persons["p_mid"]
    pr = S.Proposition("pr_u", "OUGHT", "rec_writ", "x", True, 0)
    w.propositions[pr.id] = pr
    w.add_tenure(S.Tenure("t_u", p.id, pr.id, "commit", since=0))
    q = S.questions_for(w, p)[0]
    v = S.View(p.id, [], w.fixtures.get("view_k"), q)
    ch = S.make_chooser(w.fixtures, lambda a, b, c: f"{a}:{b}:{c}")
    # `W17`: scenes, so flatten to the interactions inside them.
    picks = {s: [a.verb for sc in ch(p, v, S.Sensation(s), lambda: 3) for a in sc.acts]
             for s in (0, 500, 1000, 10 ** 6)}
    distinct = {tuple(x) for x in picks.values()}
    assert len(distinct) == 1, (
        f"urgency moved the decision: {picks}. If that is now true the third term is no longer "
        "inert and this finding about §F2 should be retired — but check it is candidate-DEPENDENT "
        "and not merely numeric noise before doing so.")
    assert S.urgency(1000, w.fixtures) != S.urgency(0, w.fixtures), (
        "urgency returns a constant, which would make this test vacuous — it must actually vary "
        "with subsistence for the inertness claim to be about §F2 rather than about a stub")


def test_w5_sense_is_still_the_only_world_taking_non_decision_function():
    """PLAN `W5`'s fourth proof — *"asserted by AST over every person-side function's signature",
    never by reading the docstring*.

    #353 `:634`: `sense()` is "the ONE non-decision function permitted a `World`". V2 §F3 broke it
    by giving `budget` a World; PLAN §3.3's smaller amendment is what this checks held."""
    import ast as ast_
    tree = ast_.parse((HERE / "shape.py").read_text())

    def named(ann) -> str:
        """The type an annotation NAMES, however it is spelled.

        ⚠ THE FIRST VERSION READ ONLY `ann.id` AND `ann.value.value`, AND WAS THEREFORE BLIND TO
        A STRING ANNOTATION — `def f(p: Person, w: "World")` — WHICH IS THE SPELLING `shape.py`
        ITSELF PREFERS: it writes `"World"` in nine signatures, because the class is defined
        below its first use. So W5's fourth proof could not observe the regression it excludes,
        in the file's own dominant style. §0.1 point 2 exactly, in a test written to enforce it.
        Normalising here covers `World`, `"World"`, `Optional["World"]` and `w: World = None`."""
        if ann is None:
            return ""
        if isinstance(ann, ast_.Name):
            return ann.id
        if isinstance(ann, ast_.Constant) and isinstance(ann.value, str):
            return ann.value.strip().strip('"\'')
        if isinstance(ann, ast_.Subscript):          # Optional[...], list[...]
            return named(ann.slice)
        if isinstance(ann, ast_.Tuple) and ann.elts:  # Optional["World"] unparses to a tuple
            return named(ann.elts[0])
        if isinstance(ann, ast_.Attribute):
            return ann.attr
        return ""

    # Person-side = every function whose FIRST parameter names `Person`. Derived from the
    # signatures rather than from a name list, so a new person-side function is covered the day
    # it is written (G2 — forbid the shape, never enumerate the words).
    offenders = []
    for node in ast_.walk(tree):
        if not isinstance(node, (ast_.FunctionDef, ast_.AsyncFunctionDef)):
            continue
        args = [a for a in node.args.args if a.arg not in ("self", "cls")]
        if not args or named(args[0].annotation) != "Person":
            continue
        takes_world = [a.arg for a in args if named(a.annotation) == "World"]
        if takes_world and node.name != "sense":
            offenders.append((node.name, node.lineno, takes_world))
    assert not offenders, (
        "a person-side function takes a World, and #353 :634 permits exactly one:\n  "
        + "\n  ".join(f"{n} at shape.py:{ln} takes {w}" for n, ln, w in offenders))
    # And the control: the AST walk must actually be finding person-side functions, or it proves
    # nothing by finding no offenders among zero candidates (§0.1 point 2).
    found = [n.name for n in ast_.walk(tree)
             if isinstance(n, ast_.FunctionDef)
             and [a for a in n.args.args if a.arg not in ("self", "cls")]
             and named([a for a in n.args.args if a.arg not in ("self", "cls")][0].annotation)
             == "Person"]
    assert len(found) >= 5, f"the AST walk found only {found} — it is not seeing person-side code"
    assert "budget" in found and "opening_set" in found, found
    # AND THE PLANT: the detector must SEE a string-annotated World, which is the spelling that
    # defeated its first version. Without this the fix is unverified and the guard could regress
    # to the blind form while still passing.
    probe = ast_.parse('def planted(p: Person, w: "World") -> int: pass').body[0]
    pargs = [a for a in probe.args.args]
    assert named(pargs[0].annotation) == "Person" and named(pargs[1].annotation) == "World", (
        "the detector cannot see a string annotation — `shape.py` writes `\"World\"` in nine "
        "signatures, so this guard would miss a real regression in the file's own style")


def test_w5_the_alignment_table_is_swept_at_three_points_and_every_flip_is_printed():
    """PLAN `W5`'s third proof: *"the `alignment` table swept at three points with every flipped
    verdict printed"*. `H-66` is the row; `rosters.yaml` holds the default.

    ⚠ THE WEIGHTS ARE INVENTED AND THE ROW IS WHAT MAKES THAT LAWFUL — §G's declare · default ·
    sweep. This is the sweep half, and its output is a measurement whichever way it comes out:
    a flip says a verdict rests on a number nobody derived; no flip says the table is not
    deciding that verdict, which is equally worth knowing and is the null result §0.1 point 4
    asks for in the unflattering direction too."""
    affected = ["P31", "P36", "P11", "P12"]
    table = {}
    saved = S.ALIGNMENT

    def fresh(pid):
        # ⚠ `run_probe` MEMOISES IN `_VERDICTS`, so calling it in a loop returns the FIRST run's
        # answer for every later point and a sweep silently measures one arm three times. The
        # first version of this test did exactly that and printed "0 of 4 move" from three
        # identical reads. Evicting the entry is what makes the sweep a sweep.
        R._VERDICTS.pop(pid, None)
        return R.run_probe(pid)["verdict"]

    try:
        for point in S.ALIGNMENT_SWEEP:
            S.ALIGNMENT = S.alignment_at(point)
            table[point] = {pid: fresh(pid) for pid in affected}
    finally:
        S.ALIGNMENT = saved
        for pid in affected:
            fresh(pid)                           # restore the committed verdicts

    base = table["declared"]
    flips = {pid: {pt: table[pt][pid] for pt in S.ALIGNMENT_SWEEP}
             for pid in affected
             if len({table[pt][pid] for pt in S.ALIGNMENT_SWEEP}) > 1}
    print(f"\n  H-66 alignment sweep over {S.ALIGNMENT_SWEEP}:")
    for pid in affected:
        row = " · ".join(f"{pt}={table[pt][pid]}" for pt in S.ALIGNMENT_SWEEP)
        print(f"    {pid}: {row}{'   <-- FLIPPED' if pid in flips else ''}")
    print(f"  {len(flips)} of {len(affected)} verdicts move across the sweep."
          + ("  No verdict rests on an invented magnitude." if not flips else
             f"  These rest on H-66's default: {sorted(flips)}"))

    # The sweep must be able to OBSERVE a flip, or reporting "no flips" proves nothing (§0.1 pt 2).
    # P31 asserts that inverting a conviction changes the pick; under `uniform` the alignment
    # cannot discriminate, so P31 MUST break there. If it does not, the control is not a control.
    assert table["uniform"]["P31"] != "PASS", (
        "P31 passed under the UNIFORM control, where alignment cannot discriminate between verbs "
        "at all. Either P31 is not actually reading the table, or the control is not uniform — "
        "and either way this sweep cannot observe the failure it exists to exclude.")
    assert base["P31"] == "PASS", f"P31 does not pass at the declared default: {base}"
    # ⚠ THE `sign_only` ARM IS ASSERTED, NOT MERELY PRINTED. It was printed and discarded, while
    # the conclusion drawn FROM it — "the result rests on the directions, not on the invented
    # magnitudes" — was published. A printed arm is not a checked one (G3).
    assert table["sign_only"]["P31"] == "PASS", (
        f"P31 fails when the magnitudes are collapsed to their signs ({table['sign_only']}). The "
        "published claim that its result rests on the DIRECTIONS is then false, and the invented "
        "weights are load-bearing after all — which is a finding, not a failure to hide.")

    # ⚠ AND THE CONFOUND THE ARM ALONE CANNOT EXCLUDE. Under `sign_only` several verbs tie, and
    # `choose` breaks ties by verb name (`sorted(..., key=(-score, verb, subject))`). So "P31
    # passes at sign_only" is consistent with "the alphabetical tiebreak happens to agree with
    # the declared ordering" — a defect in the control's SETUP, which is the class §0.1 was
    # written for. This checks the property the arm was standing in for: the chosen verb is on
    # the SAME SIDE OF ZERO as the conviction, which a name-ordered tie cannot fake.
    w = P.tiny_world()
    p = w.persons["p_mid"]
    q = S.Question("q:sgn", "need", ("rec_writ",))
    v = S.View(p.id, [], w.fixtures.get("view_k"), q)
    saved2 = S.ALIGNMENT
    try:
        S.ALIGNMENT = S.alignment_at("sign_only")
        ch = S.make_chooser(w.fixtures, lambda a, b, c: "x")
        for sign in (0.9, -0.9):
            p.convictions = {"Precedent": sign}
            picked = ch(p, v, S.Sensation(0), lambda: 1)[0].acts[0].verb
            cell = S.align(picked, "Precedent")
            assert cell * sign >= 0, (
                f"at Precedent={sign} the person chose {picked!r}, whose Precedent alignment is "
                f"{cell} — the pick is on the WRONG side of zero, so the sweep's agreement with "
                "the declared arm is a tiebreak coincidence and not the directions working")
            assert cell != 0, (
                f"at Precedent={sign} the person chose {picked!r}, which the table does not "
                "score at all — the pick was decided entirely by the name tiebreak")
    finally:
        S.ALIGNMENT = saved2
        for pid in affected:
            fresh(pid)


def test_w5_a_tenure_added_before_its_subject_still_reaches_its_owner():
    """`_rehome`'s stated purpose, tested on the path that actually matters.

    ⚠ THE GUARD DID NOT COVER THE FUNCTIONS ITS OWN DOCSTRING NAMED. It ran only from the
    `w.tenures` getter, while `budget`, `person_side_eligible` and `questions_for` all read
    `p.tenures` DIRECTLY and `deliberate` never touches the aggregate — so a Tenure added before
    its subject existed was invisible to exactly the three readers the docstring listed, unless
    some unrelated code happened to read `w.tenures` first. It passed only because the fixture
    creates persons before tenures. This plants the reverse order, which is §0.1 point 2."""
    w = S.World(7)
    w.add_tenure(S.Tenure("t_early", "p_late", "off_x", "hold", since=0))   # subject first…
    assert w._unowned, "the plant did not land in _unowned — the ordering is not being tested"
    w.persons["p_late"] = S.Person("p_late", "Late")                     # …person second
    p = w.persons["p_late"]
    assert not p.tenures, "the fixture is not reproducing the defect; nothing to rehome"
    fx = w.fixtures
    base = S.Query.budget(S.Person("p_ctl", "Ctl"), S.View("p_ctl", [], 12),
                          fx.get("scene_budget"), fx)
    w._rehome()
    assert [t.id for t in p.tenures] == ["t_early"], (
        "the Tenure never reached its owner — `budget` would read zero offices for a person the "
        "world agrees holds one")
    assert S.Query.budget(p, S.View(p.id, [], 12), fx.get("scene_budget"), fx) > base, (
        "rehoming did not change what `budget` reads, so the office is still invisible to it")
    # and the barrier does it, so no caller has to remember.
    src = _code_only(inspect.getsource(S.SeasonDriver.deliberate))
    assert "_rehome" in src, (
        "DELIBERATE does not rehome — every person-side reader is back to depending on whether "
        "something else read `w.tenures` first")


def test_w5_the_reporting_guards_are_actually_called():
    """`matrix_rows_without_a_field` and `rows_without_a_producer` REPORT rather than raise — and
    a reporter with no caller reports to nobody.

    ⚠ BOTH HAD ZERO CALLERS. `shape.py`'s `Person` comment credits the first with finding that
    `(Person, body)` and `(Person, travel_leg)` named fields the class did not have, and a
    tree-wide grep for either name returned only the `def` and that comment. `CLAUDE.md` §0.1
    point 2 in its plainest form: an assertion nothing runs cannot observe anything. The
    file-level dead-code guard could not see it either — `test_d9_no_rule_is_written_and_switched
    _off` asserts `"if False" not in source`, a STRING where `G3` wants a property, and an
    uncalled function is a switched-off rule that string cannot see.

    This is the caller. It asserts the SHAPE of each report and prints the current numbers, so a
    row naming a field that does not exist stays visible instead of being rediscovered."""
    absent_field = S.matrix_rows_without_a_field()
    assert set(absent_field) == {"absent", "unmodelled"}, absent_field
    no_producer = S.rows_without_a_producer()
    assert isinstance(no_producer, dict)
    print(f"\n  matrix rows naming a field their kind does not have: {len(absent_field['absent'])}")
    for pair in absent_field["absent"]:
        print(f"    {pair}")
    print(f"  rows on dict-modelled kinds (uncheckable): {len(absent_field['unmodelled'])}")
    print(f"  `social: true` rows no verb writes: {len(no_producer)}")

    # The two W5 fields are the falsifier: they WERE in `absent` and the fix removed them, so if
    # either regresses out of `Person` this list grows and the assertion below names it.
    fields = {f.name for f in dataclasses.fields(S.Person)}
    assert {"body", "travel_leg", "tenures"} <= fields, sorted(fields)
    assert ("Person", "body") not in absent_field["absent"], (
        "`(Person, body)` is back in the absent list — the field it names has gone again")


def test_w5_every_new_assumption_rows_sweep_is_actually_executed():
    """`R2` checks that an `assumption` row DECLARES three sweep points. Nothing checks that any
    of them was ever RUN — so two thirds of §G's declare · default · sweep is satisfiable by
    editing YAML, which is the laundering this register exists to stop.

    This runs the sweeps W5's own rows declare and asserts each arm actually differs, so a row
    cannot claim a sweep whose points are the same experiment three times."""
    rows = {r["id"]: r for r in REG.load()["rows"]}

    # H-66 — the alignment table. Its three points must produce three DIFFERENT tables.
    def canon(tbl):
        # A CANONICAL VALUE, not a generator. The first version built a genexp inside `repr()`,
        # so all three arms hashed to the same "<generator object ...>" string and the assertion
        # compared three identical placeholders — it would have reported any table as a
        # non-arm. Caught by the test failing rather than passing, which is the direction to be
        # grateful for.
        return tuple(sorted((ax, tuple(sorted(row.items()))) for ax, row in tbl.items()))

    tables = {pt: canon(S.alignment_at(pt)) for pt in S.ALIGNMENT_SWEEP}
    assert len(set(tables.values())) == 3, (
        f"two of H-66's three sweep points produce the same table — an arm that is not an arm: "
        f"{ {pt: (t == tables[S.ALIGNMENT_SWEEP[0]]) for pt, t in tables.items()} }")

    # H-53 — the View-builder rule. Each rule must be able to select a DIFFERENT set of ids, or
    # `recent` is not a control, it is the only rule.
    p = S.Person("p_v", "V")
    for n in range(6):
        p.ledger.append(S.Claim(f"c{n}", p.id, f"s{n % 3}", "grade", n, n, "firsthand", n, "own"))
    q = S.Question("q_v", "need", ("s0",))
    got = {rule: tuple(S.view_ids(p, q, 3, rule)) for rule in sorted(S.VIEW_BUILDER_RULES)}
    assert len(set(got.values())) >= 2, (
        f"every view-builder rule returned the same ids: {got} — H-53's sweep cannot move a "
        "verdict, so declaring it proves nothing")
    assert set(rows["H-53"]["sweep"]) == set(S.VIEW_BUILDER_RULES), (
        f"H-53's declared sweep and the roster have drifted: {rows['H-53']['sweep']} vs "
        f"{sorted(S.VIEW_BUILDER_RULES)}")

    # H-70 — the budget floor. The row declares a floor of 1; exercise the case that REACHES it,
    # which the direction test does not (it stops at 2).
    w = _w()
    pp = next(iter(w.persons.values()))
    fx = w.fixtures
    pp.body = 0
    pp.travel_leg = ["a"] * 20
    assert S.Query.budget(pp, S.View(pp.id, [], 12), fx.get("scene_budget"), fx) == 1, (
        "the floor of 1 never fires — `max(1, b)` is unreachable, so H-70's stated floor is "
        "declared and untested")


# ===========================================================================
# W17 — THE SCENE CONTAINER. Jordan's 2026-09-02 ruling: the budgeted unit is the SCENE.
# ===========================================================================

def test_w17_the_budget_bounds_scenes_and_the_interaction_bound_is_separate():
    """`PLAN.md` `W17`'s Proof, first two clauses: a person with `budget = 5` returning 6 scenes
    raises, and a scene carrying too many interactions raises SEPARATELY.

    ⚠ THE SEPARATION IS THE RULING. Before it, `deliberate` refused *"p_king returned 8 acts
    against a budget of 5"* — and under the ruling that return is LAWFUL, because eight
    interactions can sit inside five scenes. Folding the two checks into one would make the
    distinction Jordan drew unobservable, which is why they are two `Forbidden`s with two laws."""
    w = _w()
    fx = w.fixtures
    b = fx.get("scene_budget")
    cap = fx.get("interactions_per_scene")

    def scenes(n, per):
        def choose(p, v, s, ask_budget):
            if p.id != "p_king":
                return []
            return [S.Scene(f"s{i}", p.id,
                            [P.Act_(w, p, "speak", key=f"{i}.{j}") for j in range(per)])
                    for i in range(n)]
        return choose

    # ---- over budget ON SCENES ----
    with pytest.raises(S.Forbidden) as over:
        S.SeasonDriver(_w()).season(scenes(b + 1, 1), None, P.SUBSIST)
    # THE PROPERTY, not the message (G3). `ShapeGap` stores `where`, so the two refusals are
    # distinguishable by their LAW rather than by a word in their prose — and a body that still
    # counted acts would print the word "scenes" just as happily.
    assert over.value.where == "S26.3", over.value.where
    assert "scene" in str(over.value).lower(), f"the message lost its unit: {over.value}"

    # ---- and the SAME NUMBER of interactions, packed into a lawful number of scenes, PASSES ----
    S.SeasonDriver(_w()).season(scenes(b, cap), None, P.SUBSIST)      # must not raise
    assert b * cap > b + 1, (
        f"the fixture cannot demonstrate the ruling: {b} scenes x {cap} interactions is not more "
        f"than the {b + 1} acts the first arm refused, so 'more interactions, fewer scenes' is "
        "not being shown")

    # ---- too many interactions IN ONE scene: a DIFFERENT refusal, with a different law ----
    with pytest.raises(S.Ungraded) as many:
        S.SeasonDriver(_w()).season(scenes(1, cap + 1), None, P.SUBSIST)
    assert isinstance(many.value, S.Ungraded) and not isinstance(over.value, S.Ungraded), (
        f"the two refusals are the same KIND ({type(over.value).__name__} / "
        f"{type(many.value).__name__}); a swept harness bound is `Ungraded` and a law is not")
    assert "interactions" in str(many.value), many.value
    assert str(over.value) != str(many.value), "the two refusals are indistinguishable"


def test_w17_the_interaction_bound_flips_across_its_sweep_and_the_flip_is_printed():
    """`PLAN.md` `W17`'s Proof, third clause: *a scene carrying 4 interactions raises at the swept
    bound of 3 and PASSES at the swept bound of `unbounded`, with the flip reported.*

    `unbounded` is `H-76`'s control: at it the per-scene check does not run at all, so a verdict
    that does not move between `3` and `unbounded` is a verdict this bound was never deciding."""
    def run_at(bound):
        w = _w()
        w.fixtures = w.fixtures.sweep("interactions_per_scene", bound)
        def choose(p, v, s, ask_budget):
            return ([S.Scene("s0", p.id, [P.Act_(w, p, "speak", key=str(j)) for j in range(4)])]
                    if p.id == "p_king" else [])
        try:
            S.SeasonDriver(w).season(choose, None, P.SUBSIST)
            return "ACCEPTED"
        except S.Ungraded as e:
            return "REFUSED" if "interactions" in str(e) else f"REFUSED-OTHER: {e}"
        except S.ShapeGap as e:
            return f"REFUSED-OTHER: {type(e).__name__}: {e}"

    got = {pt: run_at(None if pt == "unbounded" else pt) for pt in (1, 3, "unbounded")}
    print("\n  H-76 sweep — one scene carrying 4 interactions:")
    for pt, verdict in got.items():
        print(f"    interactions_per_scene={pt!r:11} -> {verdict}")
    flipped = len(set(got.values())) > 1
    print(f"  {'FLIPPED' if flipped else 'no movement'} across the sweep."
          + ("  The verdict rests on H-76's default." if flipped else
             "  H-76 is not deciding this verdict."))
    assert got[3] == "REFUSED", f"the declared default did not refuse 4 interactions: {got}"
    assert got["unbounded"] == "ACCEPTED", (
        f"the control still refused: {got}. `unbounded` must switch the check OFF entirely, or it "
        "is not a control and 'no movement' would prove nothing.")
    assert got[1] == "REFUSED", got
    assert flipped, "the sweep does not move the verdict — H-76 would be declared and inert"


def test_w17_the_packing_rule_and_the_extended_cost_are_both_live():
    """`H-78` and `H-77`, and both existed as declared-but-dead before the W17 adversarial pass.

    ⚠ `H-77` WAS INERT AND PASSED `R2` ANYWAY. Nothing anywhere set `Scene.extended`, so
    `Scene.cost()` returned 1 at every sweep point and the row's declared `1 · 2 · 3` could not
    move any verdict — a row satisfying the injectable rule by being WRITTEN, which is exactly the
    laundering `R2` exists to stop. A scene carrying more than one interaction is now the extended
    one, which is what the word means.

    ⚠ `H-78` WAS A COMMENT. `make_chooser` packed scenes greedily in score order with no row, and
    that decides how many interactions a season produces at all — `greedy` gives a five-scene
    person up to fifteen, `one_per_scene` gives five. No probe VERDICT observes that, which is why
    the "zero probe flips" control could not see it; the counter that moves is the act count, and
    this asserts it."""
    w = _w()
    fx = w.fixtures
    p = next(iter(w.persons.values()))
    pr = S.Proposition("pr_pk", "OUGHT", "rec_writ", "x", True, 0)
    w.propositions[pr.id] = pr
    w.add_tenure(S.Tenure("t_pk", p.id, pr.id, "commit", since=0))
    # ⚠ A MULTI-REFERENT QUESTION, DELIBERATELY. With ONE referent every candidate shares a
    # subject, so `by_subject` is a no-op and is indistinguishable from `greedy` — correctly, but
    # then the sweep cannot tell the two arms apart and would report a real rule as inert. The
    # produced Q4 question carries one referent, so this builds a wider one.
    assert len(S.questions_for(w, p)[0].referents) == 1, "the fixture changed; re-check the setup"
    q = S.Question("q_pack", "need", ("rec_writ", "S", "p_low"))
    v = S.View(p.id, [], fx.get("view_k"), q)
    mint = lambda a, b, c: f"{a}:{b}:{c}"

    # ---- H-78: the rule changes how many interactions a season produces. ----
    counts, shapes, grouping = {}, {}, {}
    for rule in sorted(S.SCENE_PACKING_RULES):
        f2 = fx.sweep("scene_packing_rule", rule)
        scenes = S.make_chooser(f2, mint)(p, v, S.Sensation(0), lambda: 5)
        counts[rule] = sum(len(sc.acts) for sc in scenes)
        shapes[rule] = [len(sc.acts) for sc in scenes]
        # ⚠ THE GROUPING, NOT THE SHAPE. `by_subject` and `greedy` produce the same SHAPE
        # whenever every scene fills to the bound — only WHICH interactions share a scene
        # differs, which is the whole of what H-78 decides. Comparing `[3,3,3]` to `[3,3,3]`
        # would report two different rules as one arm.
        grouping[rule] = tuple(tuple(a.verb for a in sc.acts) for sc in scenes)
    print(f"\n  H-78 packing sweep (budget 5): shapes={shapes}")
    print(f"    greedy      groups: {grouping['greedy']}")
    print(f"    by_subject  groups: {grouping['by_subject']}")
    assert counts["one_per_scene"] < counts["greedy"], (
        f"packing does not change the interaction count: {counts} — H-78 would be declared and "
        "inert, and the 'zero probe flips' control cannot observe it either")
    assert len(set(grouping.values())) == 3, (
        f"two of H-78's three rules group interactions identically, so one is not an arm: "
        f"{ {r: g for r, g in grouping.items()} }")

    # ---- H-77: `extended` is set, so the cost sweep can move the budget. ----
    f_greedy = fx.sweep("scene_packing_rule", "greedy")
    scenes = S.make_chooser(f_greedy, mint)(p, v, S.Sensation(0), lambda: 5)
    multi = [sc for sc in scenes if len(sc.acts) > 1]
    assert multi, f"no scene carries more than one interaction: {shapes} — `extended` can never " \
                  "be True and H-77's sweep is inert whatever the row says"
    assert all(sc.extended for sc in multi), "a multi-interaction scene is not marked extended"
    spend = {c: sum(sc.cost(c) for sc in scenes) for c in (1, 2, 3)}
    print(f"  H-77 cost sweep — total spend at extended_scene_cost 1/2/3: {spend}")
    assert len(set(spend.values())) == 3, (
        f"the extended-scene cost does not change what a season spends: {spend}. The row declares "
        "a three-point sweep and would pass R2 while being unexecutable.")


# ===========================================================================
# W9 — ARTIFACT 2. `PLAN.md` §6.3's six checks, ALL OF THEM EXECUTIONS.
#
# > THE TESTED VERSION RAN ZERO CASES END TO END. ONE IS AN INFINITE IMPROVEMENT OVER ZERO, AND
# > IT IS THE ONLY NUMBER THAT WOULD PROVE ANY OF THIS.
# ===========================================================================

def test_w9_check1_the_run_is_reproducible():
    """§6.3 check 1: *`headless.py --case NPC-088 --seasons 2 --seed 0` prints a content hash. Run
    twice: byte-identical.*"""
    import headless as HL
    a, b = HL.run(seasons=2, seed=0), HL.run(seasons=2, seed=0)
    assert a["hash"] == b["hash"], f"two runs of one seed diverged: {a['hash']} vs {b['hash']}"
    assert a["acts"] and a["events"], f"the season did nothing: {a['acts']} acts, {a['events']} events"
    # A DIFFERENT SEED MUST DIVERGE, or "reproducible" is indistinguishable from "constant".
    assert HL.run(seasons=2, seed=7)["hash"] != a["hash"], (
        "seed 7 produced seed 0's hash — the run is not seeded, it is fixed, and check 1 would "
        "pass on a stub")


def test_w9_check2_a_causal_chain_walks_from_her_act():
    """§6.3 check 2, *the one that cannot be faked*: **a chain of at least four Events walks from
    her act, with no `[ROOT]` after the seed.**

    #353 §19.4 on why this is the check: *"the design rests its narrative layer, audit trail and
    arc model on this edge — 'the arc itself' — and the measured state is that the specified loop
    emits `causes=[]`, so the substrate of the entire emergent-narrative claim is declared and
    never populated."* `[ROOT]` everywhere is `[]` wearing a marker."""
    import headless as HL
    # ⚠ §6.3'S OWN TWO CLAUSES CANNOT BOTH HOLD, AND THE ARITHMETIC IS STATED RATHER THAN THE
    # LONGER RUN QUIETLY SUBSTITUTED. Check 1 fixes the run at `--seasons 2`; check 2 demands a
    # chain of at least four Events. The only edge that chains is term maturation, one stage per
    # season (`H-80`: 3 stages at a term of 1), so the chain reaches depth `1 + seasons - 1`:
    # depth 2 at the published two seasons and depth 4 at four. The `W9` adversarial pass caught
    # the first version running check 2 at four seasons while the artifact published two, with
    # nothing saying so. Both are measured here and the shortfall is printed, not hidden.
    published = HL.run(seasons=2, seed=0)["world"]
    w = HL.run(seasons=4, seed=0)["world"]
    by_id = {e.id: e for e in w.log}

    def depth(e, seen=()):
        if e.id in seen:
            return 0
        return 1 + max([depth(by_id[c], seen + (e.id,)) for c in e.causes if c in by_id] or [0])

    # ⚠ THE LONGEST CHAIN THAT ORIGINATES AT ONE OF HER ACTS, NOT THE LONGEST CHAIN IN THE LOG.
    # §6.3 check 2 is *"a chain of at least four Events WALKS FROM HER ACT"*, and this took the
    # global maximum — which `W4` made be the WEAR CLOCK, four links of `condition.worn` on the
    # scriptorium that no person caused. The final assertion below (the chain must start at her
    # act, not at a clock) caught it, which is the assertion doing its job; the selection is what
    # was wrong. Same blindness as `H-80`'s control, one section over, and the same fix: measure
    # the chain the clause is about. Found by the `W4` adversarial pass.
    def origin_of(e):
        cur, seen = e, set()
        while cur.id not in seen:
            seen.add(cur.id)
            nxt = next((by_id[c] for c in cur.causes if c in by_id), None)
            if nxt is None:
                return cur
            cur = nxt
        return cur

    hers = [e for e in w.log
            if (lambda o: o.subject == HL.CARIN
                or any(c.subject == HL.CARIN for c in o.changes)
                or o.kind == "record.created")(origin_of(e))]
    assert hers, "no Event in the log traces back to an act of Carin's at all"
    best = max(hers, key=depth)
    d = depth(best)
    chain, cur = [], best
    while cur:
        chain.append(cur)
        cur = next((by_id[c] for c in cur.causes if c in by_id), None)
    print("\n  W9 check 2 — the longest causal chain:")
    for e in reversed(chain):
        print(f"    t{e.emitted_at} {e.kind:16} {e.subject[:26]:26} causes={[c[:8] for c in e.causes]}")
    pub_by_id = {e.id: e for e in published.log}

    def pub_depth(e, seen=()):
        if e.id in seen:
            return 0
        return 1 + max([pub_depth(pub_by_id[c], seen + (e.id,))
                        for c in e.causes if c in pub_by_id] or [0])

    pub_origin = {e.id: e for e in published.log}

    def pub_origin_of(e):
        cur, seen = e, set()
        while cur.id not in seen:
            seen.add(cur.id)
            nxt = next((pub_origin[c] for c in cur.causes if c in pub_origin), None)
            if nxt is None:
                return cur
            cur = nxt
        return cur

    pub_hers = [e for e in published.log
                if (lambda o: o.subject == HL.CARIN
                    or any(c.subject == HL.CARIN for c in o.changes)
                    or o.kind == "record.created")(pub_origin_of(e))]
    d_pub = max((pub_depth(e) for e in pub_hers), default=0)
    print(f"  at the PUBLISHED `--seasons 2`: longest chain {d_pub} Events")
    print(f"  at `--seasons 4`:               longest chain {d} Events")
    assert d >= 4, f"the longest chain is {d} Events; §6.3 check 2 requires at least 4"
    # ⚠ AMENDED BY `W4`, WHICH IS THE CONDITION THE PREVIOUS ASSERTION NAMED. This read
    # `assert d_pub < 4` with the note *"if that is now true the note above is stale and check 2
    # should be measured on the published run alone"*. `W4` gave the wear and claim-decay clocks
    # real `causes[]`, and the published two-season run now reaches 4 — so §6.3's DEPTH clause is
    # met on the artifact as published, not only at four seasons.
    #
    # ⚠ AND DEPTH IS NOT THE CLAUSE THAT WAS FAILING, so this is not check 2 closing. The `W9`
    # pass found that the chain is ONE MECHANISM REPEATING and that the chain §6.3 actually
    # describes — a claim reaching a SECOND PERSON's Q2 and moving THEIR act — is unreachable,
    # because nothing moves a Record to a second person. `W4` lengthens the repetition; it does
    # not make a second person act. That finding stands untouched and is the reason this PR does
    # not claim §6.3 is met.
    assert d_pub >= 4, (
        f"the published two-season run reaches only {d_pub} — `W4`'s clock chaining has regressed")
    late_root = [e for e in w.log if e.causes == ["ROOT"] and e.emitted_at > 0]
    assert not late_root, (
        f"{len(late_root)} Event(s) after the seed declare `causes: [ROOT]` — §19.4 reserves that "
        f"for an Event with NO antecedent: {[e.kind for e in late_root][:5]}")
    assert all(e.causes for e in w.log), "an Event carries an empty causes[] (§19.4)"
    # and the chain must START at one of HER acts, not at a clock.
    origin = chain[-1]
    assert origin.subject == HL.CARIN or any(c.subject == HL.CARIN for c in origin.changes) \
        or origin.kind == "record.created", f"the chain's origin is {origin.kind} on {origin.subject}"


def test_w9_check3_every_fixture_read_resolves_to_a_register_site():
    """§6.3 check 3: *the fixture-read log names only sites present on `hole_register.yaml`.*
    **Zero fills off the register** — `V2` §G's central claim, made falsifiable (`G1`).

    A fixture the run READS whose name appears in no row's `site:` is a number the instrument
    supplied and nobody declared."""
    import headless as HL
    # ⚠ THIS RUN'S READS, NOT THE PROCESS'S. `DEFAULT_FIXTURES` is a module-level singleton and
    # `reads` accumulates on it, so every earlier test in the session contributes — the first
    # version passed alone and failed in the suite, reporting other tests' fixtures as artifact
    # 2's fills. Snapshot and diff.
    before = dict(S.DEFAULT_FIXTURES.reads)
    w = HL.run(seasons=2, seed=0)["world"]
    read = sorted(k for k, n in w.fixtures.reads.items() if n > before.get(k, 0))
    assert read, "the run read no fixtures at all — this check cannot observe anything"
    sites = " ".join(str(r.get("site") or "") for r in REG.load()["rows"])
    missing = [n for n in read if n not in sites]
    print(f"\n  W9 check 3 — {len(read)} fixtures read, {len(missing)} off the register")
    for n in read:
        print(f"    {'OFF-REGISTER' if n in missing else 'on-register '}  {n}"
              f"  (x{w.fixtures.reads[n] - before.get(n, 0)})")
    assert not missing, (
        f"{len(missing)} fixture(s) the run reads name no `site:` on any register row: {missing}. "
        "Each is a number the instrument supplied and no row declared, which is `G1`.")


def test_w9_check4_no_effect_lambda_and_no_roster():
    """§6.3 check 4: *`resolve` was called with no `effect` lambda, and `opening_set` with no
    roster.* Asserted over the SIGNATURES, so a caller cannot smuggle either back in."""
    assert "roster" not in inspect.signature(S.Query.opening_set).parameters
    assert "effect" not in inspect.signature(S.SeasonDriver.resolve).parameters
    assert "effect" not in inspect.signature(S.SeasonDriver._fold).parameters
    src = _code_only((HERE / "headless.py").read_text())
    assert "effect" not in src and "roster" not in src, (
        "headless.py mentions an effect or a roster — artifact 2 must not author either")
    # and the run genuinely goes through the table.
    import headless as HL
    assert HL.run(seasons=1, seed=0)["acts"] > 0


def test_w9_check4b_she_returned_at_most_budget_scenes():
    """§6.3 check 4b *(added by Jordan's 2026-09-02 ruling)*: **Carin returned at most `budget`
    SCENES**, and each scene's interaction count was checked against the **swept** bound rather
    than a constant.

    The season completing is itself the assertion — `deliberate` raises on either violation — so
    this re-runs it at a TIGHTENED bound and requires the refusal, which is what makes the
    passing run evidence rather than an absence."""
    import headless as HL
    w = HL.build_world(0)
    b = w.fixtures.get("scene_budget")
    cap = w.fixtures.get("interactions_per_scene")
    assert HL.run(seasons=1, seed=0)["acts"] <= b * cap, "more interactions than budget x bound"
    # THE FALSIFIER: at a bound of 1 the same run must refuse, or the check is unobservable.
    # ⚠ THE FALSIFIER ASSERTS A REFUSAL, NOT AN INEQUALITY. The first version set the bound to 1
    # and asserted `n <= b` over `pack_scenes` — which cannot fail for any input, because at a
    # width of 1 the packer returns at most `n_scenes` scenes by construction. It observed
    # nothing. `deliberate` is where the two bounds are enforced, so the falsifier plants a
    # violation there and requires the raise.
    w2 = HL.build_world(0, S.DEFAULT_FIXTURES.sweep("interactions_per_scene", 1))

    def over(p, v, s, ask_budget):
        return ([S.Scene("s0", p.id, [P.Act_(w2, p, "speak", key=str(j)) for j in range(2)])]
                if p.id == HL.CARIN else [])

    with pytest.raises(S.Ungraded) as caught:
        S.SeasonDriver(w2).season(over, None, HL.subsistence)
    assert "interactions" in str(caught.value), caught.value


def test_w9_check6_the_float_control_still_fires():
    """§6.3 check 6: *the A5-style float control still fires.* `W11` may follow, but the float arm
    must not have been removed to make the run clean."""
    R._VERDICTS.pop("A5", None)
    v = R.run_probe("A5")
    assert v["verdict"] == "PASS", f"A5 is {v['verdict']}: {v.get('detail')}"
    assert "float" in str(v.get("detail", "")).lower(), (
        f"A5 passed without exercising its float arm: {v.get('detail')}")


def test_w9_check5_every_declared_exercises_verb_runs_or_is_recorded_not_assessed():
    """§6.3 check 5 — *the one that stops the author moving the goalposts after seeing the run.*

    Each of Carin's rows declares an `exercises:`. For every declared VERB, either its `emits:`
    kind appears in the log with `causes[]` walking back to one of her acts, or the row is
    reported NOT-ASSESSED WITH ITS REASON — never re-pointed at a verb that happens to fire.

    ⚠ THE BEFORE-THE-RUN GUARANTEE IS NOT CLAIMED AND THE FILE SAYS SO. It was authored after
    artifact 2 first ran; what replaces the ordering is that every row derives from a source
    OUTSIDE the run (#353 §13.1 and the case's own text) and cites the line. This test asserts
    that substitute is real — a row whose `from:` is missing fails."""
    import yaml as _y
    import headless as HL
    spec = _y.safe_load((HERE.parent / "cases" / "exercises" / "NPC-088.yaml").read_text())
    assert spec["authored_after_first_run"] is True, (
        "the provenance declaration was removed — check 5's substitute for the ordering guarantee "
        "is that the file DECLARES it was written late and cites an outside source for each row")
    rows = spec["rows"]
    assert len(rows) >= 6 and all(r.get("from", "").strip() for r in rows), (
        "a row carries no `from:` — an exercises row with no outside derivation is the author's "
        "own model, which is what this check exists to exclude")

    w = HL.run(seasons=4, seed=0)["world"]
    kinds = {e.kind for e in w.log}
    by_id = {e.id: e for e in w.log}
    # ⚠ THE ACTS, NOT THE EVENTS. The first version tested `e.id in {events whose subject is
    # Carin}` and returned True at step zero for every act-Event of hers — because the fold sets
    # EVERY act-Event's subject to its actor. It never traversed one `causes[]` edge, so the
    # clause "with `causes[]` walking back to her act" was never executed. Walking to an ACT id
    # is the thing the plan asks for and is now what this tests.
    hers = {c for e in w.log for c in e.causes
            if c not in by_id and c != "ROOT" and e.subject == HL.CARIN}

    def walks_back(e, seen=()):
        if any(c in hers for c in e.causes):
            return True
        return any(walks_back(by_id[c], seen + (e.id,))
                   for c in e.causes if c in by_id and c not in seen)

    ran, unassessed, non_verb = [], [], []
    for r in rows:
        for token in r["exercises"]:
            row = S.VERB_TABLE.get(token)
            if row is None:
                # ⚠ THIS BRANCH SAID `continue  # checked below` AND NOTHING BELOW CHECKED THEM,
                # so every row whose `exercises:` names only an H-id or an Event kind vanished
                # from BOTH columns — including row 3, "possessing the product must trigger
                # consequences for whoever holds it", which is the row `H-79` was created to
                # unblock and which the corpus still scores as an unmapped core row. A check that
                # silently drops the case it exists for is worse than one that fails.
                if token in kinds:
                    ran.append((token, [token]))
                elif token in {x["id"] for x in REG.load()["rows"]}:
                    non_verb.append(token)     # a hole id: reported, never counted as ran
                else:
                    unassessed.append((token, []))
                continue
            hit = [k for k in row.emits if k in kinds]
            (ran if hit else unassessed).append((token, hit))
    print(f"\n  W9 check 5 — declared tokens that RAN: {sorted({t for t, _ in ran})}")
    print(f"                  NOT-ASSESSED: {sorted({t for t, _ in unassessed})}")
    print(f"                  register rows cited (not executable): {sorted(set(non_verb))}")
    # EVERY ROW IS ACCOUNTED FOR IN ONE OF THE THREE COLUMNS. This is the assertion the dropped
    # branch made impossible, and it is check 5's actual claim.
    seen = {t for t, _ in ran} | {t for t, _ in unassessed} | set(non_verb)
    for r in rows:
        assert set(r["exercises"]) <= seen, (
            f"row {r['need'][:60]!r} declares {sorted(set(r['exercises']) - seen)}, which appears "
            "in no column — it is neither exercised nor recorded NOT-ASSESSED")
    assert non_verb, "no row cites a register hole — the H-id branch is unexercised"
    assert ran, "not one declared verb produced its `emits:` kind — the exercises describe a "\
                "season that did not happen"
    # Every kind that DID fire must walk back to one of her acts, or the log is disconnected.
    for _tok, hits in ran:
        for k in hits:
            e = next(x for x in w.log if x.kind == k)
            assert walks_back(e), f"{k} does not walk back to an act of Carin's"
    # And the honest half: what did NOT run is reported, not repointed.
    assert len(ran) + len(unassessed) >= 5, (ran, unassessed)


# ===========================================================================
# W4 — MATTER EMITS PER WRITE, WITH CAUSES. `H-12` is RULED that way; these are its proof.
# ===========================================================================

def _w4_run(seasons: int, seed: int = 0, condition: int | None = None):
    import headless as HL
    w = HL.build_world(seed)
    if condition is not None:
        list(w.sites.values())[0].condition = condition
    d = S.SeasonDriver(w)
    mint = lambda pid, verb, subj: S.H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    for _ in range(seasons):
        d.season(S.make_chooser(w.fixtures, mint, verbs=S.resolvable_verbs()),
                 None, HL.subsistence)
    return w


def test_w4_a_band_crossing_walks_back_to_the_wear_that_caused_it():
    """`PLAN.md` `W4`'s first Proof clause. `H-12` is RULED *"MATTER emits an Event per write SO
    CROSSINGS HAVE AN ANTECEDENT"*, and the crossing carried `causes=[ROOT]` — so the one Event in
    the barrier that exists to be walked back from was rooted at the campaign seed and walked
    nowhere. `P18` ASSERTED THAT, which is a probe pinning a defect.

    The site is seeded one season above a floor rather than run for twenty: wear is 10/season from
    990 and the first floor is 800, so a natural crossing needs 20 seasons. The seeding is a test
    fixture, not a design value — nothing about the crossing's mechanism depends on how the site
    got near the floor."""
    w = _w4_run(2, condition=805)
    by_id = {e.id: e for e in w.log}
    crossings = [e for e in w.log if e.kind == "condition.band_crossed"]
    assert crossings, "no band edge was crossed — the fixture no longer reaches a floor"
    for c in crossings:
        assert len(c.causes) == 1 and c.causes[0] != S.ROOT, (c.kind, c.causes)
        ante = by_id.get(c.causes[0])
        assert ante is not None and ante.kind == "condition.worn", (
            f"a crossing's antecedent is {ante.kind if ante else None!r}, not the wear")
        assert ante.subject == c.subject and ante.emitted_at == c.emitted_at, (
            "the crossing names a wear Event about a different site or a different season")


def test_w4_root_belongs_only_to_the_seed_and_a_clocks_genuine_first_emission():
    """`PLAN.md` `W4`'s second Proof clause, ASSERTED AND NOT PRINTED (`G3`): *"the count of
    `[ROOT]` after season 1 equals the number of declared roots and nothing else"*.

    ⚠ THIS IS THE CLAUSE THAT CAUGHT TWO REAL DEFECTS while `W4` was being built, which is why it
    is worth more than a count. (1) `write()` used the TRACE LABEL as the Event subject, so every
    site's wear emitted under the subject `"condition"`, `last_emission_of` never matched, and the
    clock re-rooted every season. (2) a claim's first decay rooted at the seed, because the deposit
    that created the claim emitted nothing — 63 spurious roots in a 3-season run. A claim is not a
    clock; it is a thing a witness deposited, and the deposit has an Event."""
    for seasons in (1, 2, 3, 4):
        w = _w4_run(seasons)
        rooted = [e for e in w.log if list(e.causes) == [S.ROOT]]
        kinds = sorted({e.kind for e in rooted})
        assert kinds == ["condition.worn"], (
            f"{seasons} season(s): {kinds} carry [ROOT]. Only a licensed clock's GENUINE FIRST "
            f"emission may, and wear is the only clock this world runs")
        assert all(e.emitted_at == 0 for e in rooted), (
            f"{seasons} season(s): a [ROOT] appears after season 0 — the clock is not chaining to "
            "its own previous tick")
        assert len(rooted) == len(w.sites), (
            f"{seasons} season(s): {len(rooted)} roots for {len(w.sites)} site(s)")


def test_w4_every_matter_write_on_a_declaring_row_emits_or_is_registered_as_conditional():
    """The gate itself, both directions. A MATTER write on a row Part D gives an `emits:` must name
    one of the declared kinds; a kind the row does not declare is refused.

    ⚠ THE GATE FOUND SIX SILENT MATTER WRITES THE MOMENT IT WAS TURNED ON — `(Record, matured)`,
    `(Person, exists)` twice, `(Tenure, until)`, `(Record, ttl)` and `(Rung, envelope)`, every one
    on a row whose `emits:` Part D declares. Five were fixed; the sixth is `H-86`."""
    import headless as HL
    w = HL.build_world(0)
    w.step = S.Step.MATTER
    site = list(w.sites.values())[0]

    with pytest.raises(Forbidden, match="emitted nothing"):
        w.write("condition", WriteClass.MATTER, lambda: setattr(site, "condition", 1),
                record_kind="Site", fieldname="condition", driver="Event")
    with pytest.raises(Forbidden, match="does not declare"):
        w.write("condition", WriteClass.MATTER, lambda: setattr(site, "condition", 1),
                record_kind="Site", fieldname="condition", driver="Event",
                emits="site.exploded", subject=site.id, causes=[S.ROOT])
    # S19.4's own guard, in `Event.__post_init__` — NOT a second copy in `write()`. The first
    # version of `W4` re-implemented it there, which is §8's rule broken one constructor apart.
    with pytest.raises(Forbidden, match="causes="):
        w.write("condition", WriteClass.MATTER, lambda: setattr(site, "condition", 1),
                record_kind="Site", fieldname="condition", driver="Event",
                emits="condition.worn", subject=site.id, causes=[])

    # AND THE REGISTERED EXEMPTION IS READ FROM DATA, NOT FROM A LITERAL (`H-86`).
    #
    # ⚠ THIS CLAUSE USED TO BE VACUOUS AND THE VACUITY WAS INVISIBLE. It read
    # `rec = next(iter(w.records.values()), None)` then `if rec is not None:` — and
    # `headless.build_world` creates NO Records, so `rec` was unconditionally `None` and the write
    # never ran. Deleting the exemption from `write()` left all four `w4` tests green. A Record is
    # built here rather than hoped for. Found by the `W4` adversarial pass.
    assert "Record.ttl" in S.roster("conditional_emission_rows")
    rec = S.Record("rec_w4", "S", "writ", ttl=2)
    w.records[rec.id] = rec
    w.write("ttl", WriteClass.MATTER, lambda: setattr(rec, "ttl", rec.ttl - 1),
            record_kind="Record", fieldname="ttl", driver="Event")
    assert rec.ttl == 1, "the exempt write did not apply"
    assert not [e for e in w.log if e.subject == rec.id], (
        "the exempt row emitted anyway — `record.expired` on a non-terminal decrement asserts an "
        "expiry that has not happened")
    # AND THE EXEMPTION IS NARROW: an UNDECLARED kind is still refused on the same row.
    with pytest.raises(Forbidden, match="does not declare"):
        w.write("ttl", WriteClass.MATTER, lambda: setattr(rec, "ttl", rec.ttl - 1),
                record_kind="Record", fieldname="ttl", driver="Event",
                emits="record.vanished", subject=rec.id, causes=[S.ROOT])
    # AND `subject=` IS MANDATORY WHEN EMITTING — the trace-label fallback was the value that
    # made every site's wear emit under the subject `"condition"`.
    with pytest.raises(Forbidden, match="no `subject="):
        w.write("condition", WriteClass.MATTER, lambda: setattr(site, "condition", 1),
                record_kind="Site", fieldname="condition", driver="Event",
                emits="condition.worn", causes=[S.ROOT])


def test_w4_a_claims_decay_walks_back_to_the_act_that_was_witnessed():
    """The third clock. `(Claim, confidence)` decays at MATTER and emits `claim.decayed`, chained
    to the claim's own previous decay and ultimately to the `claim.deposited` Event — which is
    chained to the Event that was witnessed. #353 §19.4 calls `causes[]` the substrate of the
    entire emergent-narrative claim; before `W4` a claim entered the world uncaused."""
    w = _w4_run(3)
    by_id = {e.id: e for e in w.log}
    decays = [e for e in w.log if e.kind == "claim.decayed"]
    assert decays, "no claim decayed — the third licensed clock is not running"
    walked = 0
    for d in decays:
        chain, cur = [], d
        while cur.causes and cur.causes[0] in by_id:
            cur = by_id[cur.causes[0]]
            chain.append(cur.kind)
            if len(chain) > 40:
                break
        assert "claim.deposited" in chain, (
            f"a decay's chain is {chain} — it never reaches the deposit that created the claim")
        if chain[chain.index("claim.deposited") + 1:]:
            walked += 1
    assert walked, "no decay chain reaches past its deposit to the Event that was witnessed"


def test_w4_a_refused_attempt_names_the_attempt_not_the_campaign_seed():
    """The `[ROOT]` clause, asserted where the FIXTURE CANNOT REACH.

    ⚠ THIS IS THE CASE THAT MADE `W4`'s HEADLINE CLAIM FALSE OF THE DESIGN while true of the run.
    `resolve`'s S27.4 branch emitted `attempt.refused` with `causes=[ROOT]`, and the rule against
    it is stated TWICE within sixteen lines of that line — the contest branch below it passes
    `causes=[a.id]`, and `_fold` carries a paragraph calling `[ROOT]` in an act-caused emission
    "`[]` wearing a marker". `Act.obstacle` defaults to `None` and the computed chooser never sets
    one, so no seeded run could reach the branch and the ROOT-count proof could not see it. An
    `Act` with an obstacle is built here directly. Found by the `W4` adversarial pass."""
    import headless as HL
    w = HL.build_world(0)
    d = S.SeasonDriver(w)
    pid = next(iter(w.persons))
    mult = w.fixtures.get("obstacle_refusal_multiple")
    a = S.Act(id="act_refused", actor=pid, verb="work")
    a.obstacle, a.pool = mult * 10 + 1, 1        # Ob > multiple x Pool -> S27.4 refuses
    d.matter([])
    out = d.resolve([a], contest_max_depth=2)
    refused = [e for e in out if e.kind == "attempt.refused"]
    assert refused, "S27.4 did not refuse the over-obstacle attempt; the fixture no longer reaches it"
    for e in refused:
        assert e.causes == [a.id], (
            f"a refused attempt names {e.causes} — the antecedent is THE ATTEMPT, and `[ROOT]` is "
            "for the campaign seed and a licensed clock's genuine first emission")


def test_w4_h40s_declared_sweep_is_executed_and_its_zero_arm_does_not_fabricate():
    """`H-40`'s sweep `[0, 5, 20]`, RUN — and the `0` arm is the control.

    ⚠ TWO DEFECTS THIS CATCHES, AND THE SECOND IS WORSE. (1) The sweep was declared in YAML and
    executed nowhere, which is the exact defect the `H-80` control had and that `W4` fixed one
    section earlier — re-introduced in the same commit. (2) At rate `0` the loop still emitted
    `claim.decayed` for every claim every season while `max(0, conf - 0)` changed nothing, so the
    CONTROL ARM published a decay that did not happen. The rule against that is enforced twice in
    `shape.py` already (`_fold`'s *"an effect that touched nothing did not do the thing"*, and
    `H-86`'s exemption argument). A sweep point that fabricates is worse than one nobody runs."""
    import headless as HL
    from collections import Counter
    seen = {}
    for rate in (0, 5, 20):
        w = HL.build_world(0, S.DEFAULT_FIXTURES.sweep("claim_decay_per_season", rate))
        d = S.SeasonDriver(w)
        mint = lambda pid, verb, subj: S.H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
        for _ in range(3):
            d.season(S.make_chooser(w.fixtures, mint, verbs=S.resolvable_verbs()),
                     None, HL.subsistence)
        confs = [c.confidence for p in w.persons.values() for c in p.ledger]
        seen[rate] = (Counter(e.kind for e in w.log)["claim.decayed"], min(confs), max(confs))
    print(f"\n  H-40 sweep — (decay events, min confidence, max) by rate: {seen}")
    assert seen[0][0] == 0, (
        f"the 0 arm emitted {seen[0][0]} `claim.decayed` Events — a decay that did not happen")
    assert seen[0][1] == seen[0][2], "confidence moved at rate 0"
    assert seen[5][0] and seen[20][0], "the live arms emitted no decay at all"
    assert seen[20][1] < seen[5][1] < seen[0][1], (
        f"confidence does not fall faster at a higher rate: {seen} — then the rate is inert and "
        "this sweep is measuring nothing")


# ===========================================================================
# W6 — WITNESS CHANNEL PREDICATES, AND LEDGER FLOOD CONTROL. `H-33`.
# ===========================================================================

def _w6_run(mode: str, seasons: int = 3, seed: int = 0):
    import headless as HL
    w = HL.build_world(seed, S.DEFAULT_FIXTURES.sweep("fan_out_mode", mode))
    d = S.SeasonDriver(w)
    mint = lambda pid, verb, subj: S.H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    dep = 0
    for _ in range(seasons):
        dep += d.season(S.make_chooser(w.fixtures, mint, verbs=S.resolvable_verbs()),
                        None, HL.subsistence)["deposits"]
    return w, dep


def test_w6_h33s_declared_sweep_runs_and_the_deposit_count_falls():
    """`PLAN.md` `W6`'s Proof: *"deposits per season fall from `N × E` to a number the sweep
    reports"*. `H-33`'s declared sweep is `total / presence-only / all five`, and `total` is BOTH
    the default and the control because it is #353's specified behaviour (`S61`).

    ⚠ THIS IS THE INTERACTION `PLAN.md` §1.4 HOLE 16 PREDICTED AS AN ARGUMENT. *"`D22` (MATTER
    emits per write) and `H-33` (`absent`, so fan-out is total) are individually fine and JOINTLY
    FATAL."* `W4` landed `D22` and the argument became a measurement: the run stopped finishing."""
    got = {}
    for mode in ("total", "presence_only", "all_five"):
        w, dep = _w6_run(mode)
        got[mode] = (len(w.log), dep, sorted(len(p.ledger) for p in w.persons.values()))
    print(f"\n  H-33 sweep — (events, deposits, ledgers) by fan-out mode: {got}")
    assert got["presence_only"][1] < got["total"][1], (
        f"narrowing the channels did not reduce deposits: {got} — then no predicate EXCLUDES and "
        "`S61`'s debt is not discharged")
    assert got["presence_only"][1] * 4 < got["total"][1], (
        f"the reduction is marginal: {got}. §1.4 hole 16 is about an order of magnitude, and a "
        "few percent would mean the predicates are not the thing bounding the fan-out")
    # AND THE TWO NARROW ARMS ARE NOT THE SAME ARM WEARING TWO NAMES. If `chronicle` matched
    # everyone, `all_five` would BE `total` and the sweep would have a redundant point.
    assert got["all_five"][1] > got["presence_only"][1], (
        f"`all_five` deposits no more than `presence_only`: {got} — the four other channels are "
        "inert and the sweep has two points measuring one thing")
    assert got["all_five"][1] < got["total"][1], (
        f"`all_five` is indistinguishable from `total`: {got} — `chronicle` is matching everyone, "
        "which is the degenerate reading `rosters.yaml` warns against")
    # ⚠ `==`, NOT `>=`. The cap fix (`if` -> `while`: one deposit can mint several claims, so a
    # single pop left the ledger at 203 against `L = 200`) had NO FALSIFIER, because `>=` passes
    # 203 exactly as it passes 200. One character. Found by the `W6` adversarial pass.
    assert max(got["total"][2]) == S.DEFAULT_FIXTURES.get("ledger_cap"), (
        f"the control arm's fullest ledger is {max(got['total'][2])}, not exactly the "
        f"`L = {S.DEFAULT_FIXTURES.get('ledger_cap')}` cap. Above it, the cap is not a cap; below "
        "it, the flood this item exists to bound has gone away and the item should be re-argued")


def test_w6_an_unrecognised_fan_out_mode_refuses_rather_than_falling_back():
    """§42.2's polarity rule applied to a sweep parameter. A mode outside `H-33`'s three points
    that silently fell back to `total` would make every reading of this sweep report THE CONTROL,
    which is the failure mode that makes a sweep worse than no sweep."""
    import headless as HL
    w = HL.build_world(0)
    e = next(iter(w.log), None) or S.Event(S.H(w.world_seed, 0, "x", "t"), "speech.made", "x",
                                           [], [S.ROOT], 0)
    with pytest.raises(S.Unspecified, match="not one of"):
        S.observers_for(w, e, "everyone_obviously", list(w.persons))


def test_w6_every_named_channel_has_a_predicate_and_they_are_data():
    """`S61`: *"WITNESS AS SPECIFIED FANS EVERY EVENT TO EVERY PERSON… a wrapper does not fix this
    and MUST NOT BE PRESENTED AS FIXING IT."* So this asserts two things at once — that every
    named channel resolves to a predicate, and that the predicates are DATA rather than a literal
    roster in a Python body (Jordan, 2026-09-02: definitions are not hardcoded)."""
    # ⚠ TWO ASSERTIONS RETIRED HERE, BOTH VACUOUS. `set(named) == set(WITNESS_CHANNELS)` guarded
    # a duplicate that no longer exists — the names live once, in `witness_channels`, and the
    # predicate row carries only meanings. `set(named) == set(CHANNEL_PREDICATES)` was true BY
    # CONSTRUCTION, because the map is built by iterating the roster and raising on a missing
    # function; the failure it named raises at IMPORT, collecting as an error in all 126 tests
    # rather than as a failure here. Found by the `W6` adversarial pass.
    meanings = S._ROSTERS["witness_channel_predicates"]["predicates"]
    assert set(meanings) == set(S.WITNESS_CHANNELS), (
        f"a channel is named without a stated meaning, or vice versa: "
        f"{set(meanings) ^ set(S.WITNESS_CHANNELS)}")
    # AND WHICH CHANNELS CAN ACTUALLY ADMIT ANYONE, WHICH IS THE THING THE FIRST VERSION ASSERTED
    # BY IMPLICATION AND NEVER MEASURED. Two of the five admit nobody in the world the fold can
    # currently drive, and that is published rather than left for a reader to discover.
    import headless as HL
    w = HL.build_world(0)
    d = S.SeasonDriver(w)
    mint = lambda pid, verb, subj: S.H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    for _ in range(2):
        d.season(S.make_chooser(w.fixtures, mint, verbs=S.resolvable_verbs()), None, HL.subsistence)
    everyone = list(w.persons)
    fires = {c: sum(1 for e in w.log if any(fn(w, e, pid) for pid in everyone))
             for c, fn in S.CHANNEL_PREDICATES.items()}
    print(f"\n  W6 — events on which each channel admits at least one person: {fires}")
    assert fires["co_located"], "the presence channel admits nobody — it is broken closed"
    inert = sorted(c for c, n in fires.items() if not n)
    assert inert == ["chronicle", "post_remit"], (
        f"the inert channels are {inert}, not the two this item published. `chronicle` fires only "
        "on a `binding_decision` verb and `post_remit` needs an office whose remit covers the "
        "emitting verb; NEITHER is reachable from the verbs the fold can execute, so the "
        "`all_five` arm is currently a measurement of THREE channels and the register says so. If "
        "this list has changed, the register's reading of `H-33` has to change with it")
    # AND THE INJECTION IS DECLARED AS ONE. `H-33` must not read `ruled` off the back of this.
    h33 = R._register()["H-33"]
    assert h33["grade"] == "assumption", (
        f"`H-33` is graded {h33['grade']!r}. The five predicates are an INJECTED default — #353 "
        "names the channels and supplies no predicate — and grading the row `ruled` on the back "
        "of this item would credit the design with an answer this session invented")
    assert len(h33["sweep"]) >= 3 and h33["site"], h33


# ===========================================================================
# THE GOVERNANCE SLICE — Jordan, 2026-09-02: strata that concern governance and management across
# scales of factions/governing bodies. The `scale:` axis, crossed with the five strata.
# ===========================================================================

def test_governance_scale_is_a_rung_kind_and_is_crossed_with_the_stratum():
    """`scale:` is a SEPARATE AXIS from `stratum`, not more strata. The stratum says what KIND of
    act this is and orders resolution; the scale says WHOSE BODY it reaches.

    ⚠ THE LADDER ALREADY EXISTED — `rung_kinds`, person through realm — so this reads that roster
    rather than minting a second one, which on this exact axis would be §8 broken.

    ⚠ AND A FACTION IS NOT A SCALE, WHICH IS A RULING AND NOT AN OMISSION.
    `ARCHITECTURE_V2.md:93` lists *"a faction acting as an actor"* in its REFUSAL table at `L1`,
    with three corpus cases that wanted it, and `H-21` completes it: *"a faction's treasury is
    matter at the rung or office that holds it."* Governance above the person is a PERSON HOLDING
    AN OFFICE acting at a rung."""
    scales = {r.scale for r in S.VERB_TABLE.values()}
    assert scales <= set(S.RUNG_KINDS), (
        f"a verb's scale is not a rung kind: {sorted(scales - set(S.RUNG_KINDS))}")
    assert "faction" not in S.RUNG_KINDS, (
        "`faction` has become a rung kind. `ARCHITECTURE_V2.md:93` REFUSES a faction acting as an "
        "actor at `L1`; if that has been overturned, this test is the wrong place to find out")
    # THE AXES ARE GENUINELY CROSSED: one stratum spans several scales, and one scale spans
    # several strata. Either alone would mean `scale` is just `stratum` under another name.
    by_stratum, by_scale = {}, {}
    for v, r in S.VERB_TABLE.items():
        by_stratum.setdefault(r.stratum, set()).add(r.scale)
        by_scale.setdefault(r.scale, set()).add(r.stratum)
    assert any(len(v) > 1 for v in by_stratum.values()), (
        f"every stratum sits at exactly one scale — then `scale` adds nothing: {by_stratum}")
    # ⚠ THE DEFAULT BUCKET IS EXCLUDED, AND WITHOUT THAT THIS CANNOT FAIL. Delete every `scale:`
    # line from `verb_table.yaml` and all 32 rows fall to the `"person"` default — `by_scale`
    # becomes `{"person": {all five strata}}` and `any(len(v) > 1)` PASSES, satisfied entirely by
    # the unauthored bucket. The property is about AUTHORED scales. Found by the governance-slice
    # adversarial pass.
    authored = {k: v for k, v in by_scale.items() if k != "person"}
    assert authored, "no verb carries an authored scale; the column is entirely default"
    assert any(len(v) > 1 for v in authored.values()), (
        f"every AUTHORED scale carries exactly one stratum — then the two are the same axis "
        f"under another name: {authored}")
    print(f"\n  scales in use: { {k: sorted(v) for k, v in sorted(by_scale.items())} }")


def test_the_governance_slice_executes_and_a_binding_decision_reaches_a_rung():
    """§0.2 — the slice is done when it RUNS. Four `binding_decision` verbs execute here, at
    settlement and territory scale, performed by the one person holding an office.

    ⚠ NOT ONE OF THE EIGHT GOVERNANCE VERBS EXECUTED BEFORE THIS. Each states its precondition in
    PROSE, so `resolvable_verbs()` excluded every one — which is also why `post_remit` and
    `chronicle`, two of `W6`'s five witness channels, could never fire: both need a binding
    decision, and no binding decision could happen."""
    w = P.tiny_world()
    d = S.SeasonDriver(w)
    duke = "p_high"
    assert any(t.subject == duke and t.object == "off_duke" and t.live for t in w.tenures)
    # ⚠ A HARNESS FIXTURE, AND A REAL GAP IT EXPOSES. Part E requires *"the office's CONFERRAL
    # basis"*, and NEITHER fixture office carries one — `conferral` is `None` on both — so the
    # clause refuses every conferral in `tiny_world`. That is the predicate working: before the
    # governance-slice pass dropped the conjunct, the clause was unenforced and this fixture's
    # incompleteness was invisible. The basis is supplied HERE rather than in `probes.py`, so no
    # other probe's world changes, and it is a fixture string rather than a design claim — Part E
    # says an office must HAVE a basis, not what any particular basis is.
    w.offices["off_dicastery"].conferral = "the duke's remit (harness fixture)"

    made = []

    def choose(p, v, s, ask_budget):
        if p.id != duke or made:
            return []
        # ⚠ `confer` ON `off_dicastery`, NOT `revoke` ON `off_duke`. The duke's remit is
        # `['issue','determine','confer','dispatch','convene']` — it does NOT carry `revoke`, so
        # a revoke by him is correctly INELIGIBLE, and using it here would have tested the
        # eligibility gate while claiming to test the slice. `off_dicastery` is unheld, which is
        # exactly what `confer`'s 1-per-object precondition requires.
        acts = [
            S.Act(id="g_confer", actor=duke, verb="confer",
                  payload={"office": "off_dicastery", "to": "p_mid"}),
            S.Act(id="g_convene", actor=duke, verb="convene",
                  payload={"venue": "S", "when": w.tick + 1}),
            S.Act(id="g_dispatch", actor=duke, verb="dispatch",
                  payload={"subject": "p_low"}),
        ]
        made.extend(acts)
        return acts

    d.matter([])
    out = d.resolve(made or choose(w.persons[duke], None, None, None),
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    kinds = {e.kind for e in out}
    assert "tenure.opened" in kinds, (
        f"`confer` seated nobody: {sorted(kinds)}")
    assert any(t.subject == "p_mid" and t.object == "off_dicastery" and t.live
               for t in w.tenures), "the conferral emitted but seated no live tenure"
    assert "date.scheduled" in kinds, f"`convene` scheduled no sitting: {sorted(kinds)}"
    assert "order.given" in kinds, f"`dispatch` gave no order: {sorted(kinds)}"
    # AND THE SCALE IS CARRIED, not merely declared: each of these reaches a rung above the person.
    for v in ("confer", "convene"):
        assert S.VERB_TABLE[v].scale == "settlement", S.VERB_TABLE[v].scale
    assert S.VERB_TABLE["dispatch"].scale == "territory"
    print(f"\n  governance slice — emitted {sorted(kinds)}; "
          f"{len(S.resolvable_verbs())} of {len(S.VERB_TABLE)} verbs now execute")


def _seat(w, person, office_id, post, rung, remit=("issue", "revoke"), first=False,
          faction: str = "Crown"):
    """Seat `person` on a new office. ONE OWNER for the fixture, because every governance test
    needs one and the governance-canon pass found the suite had built exactly TWO offices in the
    entire instrument — so the worlds it asserted about were not the worlds the ruling is about.

    `first=True` inserts the tenure at the head of `w.tenures`, which is how the insertion-order
    dependence in the old `under_purview` is made observable rather than argued about."""
    # `faction` defaults to Crown here because the governance fixtures model the REALM ladder
    # Jordan ruled on (king / duke / clerk), which is the Crown's. A test that needs a different
    # belonging passes one; `Office` refuses anything off the roster either way (`H-99`).
    w.offices[office_id] = S.Office(office_id, post, rung, list(remit), faction=faction)
    ten = S.Tenure(f"t_{office_id}_{person}", person, office_id, "hold", 0)
    w.add_tenure(ten)
    if first:
        # ⚠ THROUGH THE OWNER, NOT THROUGH `w.tenures`, WHICH IS A READ-ONLY VIEW (S15.1, `W5`).
        # The first draft of this helper mutated the view and raised `InstrumentDefect` — the
        # guard `W5` built for exactly this doing its job on the person who built it.
        own = w.persons[person].tenures
        own.remove(ten)
        own.insert(0, ten)
    return office_id


def test_the_title_ladder_is_total_over_the_rungs_and_rank_is_the_rung_ordinal():
    """`H-90`. Jordan, 2026-09-02: *"realm = king/queen, duchy = duke/duchess, province =
    count/countess, territory = lord, settlement = mayor, community = community leader, hearth =
    family head, person = own autonomous individual."*

    ⚠ RANK IS THE ORDINAL IN `rung_kinds`, NOT A SECOND SCALE. The ladder the tree already had is
    the ladder, so a title names the rung kind it governs and the ordering falls out; minting a
    separate rank number would be the `scale`-vs-`stratum` mistake one axis along.

    ⚠ AND THE LADDER IS TOTAL, which is the load-bearing half: every rung kind has a title, down
    to a person governing themselves. That bottom rung is why Part E's `own` eligibility is not a
    special kind of permission — it is this ladder at scale `person`.

    ⚠ MEMBERSHIP IS READ FROM `domains:`, WHICH IS NOW ITS ONLY HOME. This read a separate
    `values:` list while the MECHANISM read `domains:`, so the guard was asymmetric: a name in
    `values` but not `domains` went red, and a name in `domains` but not `values` was invisible
    here and live in `_req_revoke`. Adding `Steward: duchy` made an office posted `Steward` a
    title, flipping its revocation rule, with the whole suite green. Found by the governance-canon
    pass; `values:` is deleted and this reads the mapping the code reads."""
    domains = dict(S.TITLE_DOMAINS)
    assert domains and all(domains.values()), (
        f"a title governs no rung: {[t for t, d in domains.items() if not d]}")
    assert set(domains.values()) == set(S.RUNG_KINDS), (
        f"the ladder is not total — rungs with no title: "
        f"{sorted(set(S.RUNG_KINDS) - set(domains.values()))}")
    # rank IS the rung ordinal, in both directions
    for ttl, dom in domains.items():
        assert S.title_rank(ttl) == list(S.RUNG_KINDS).index(dom), (ttl, dom)
    assert S.title_rank("King") > S.title_rank("Duke") > S.title_rank("Count") \
        > S.title_rank("Lord") > S.title_rank("Mayor") > S.title_rank("Individual")
    assert S.title_domain("Dicastery") is None and S.title_rank("Dicastery") == -1, (
        "a non-title post reads as a rank; then an ordinary office confers governing authority")
    # ⚠ AND THE MAPPING MUST REFUSE WHEN ABSENT, NOT DEFAULT. `title_domain` read
    # `_ROSTERS.get("titles") or {}`, so deleting the roster returned `None` for every post and
    # `_req_revoke` fell back to purview-for-everything — a guard failing OPEN into the exact
    # behaviour Jordan's fourth message forbids. `roster_map` is the single owner of the refusal.
    with pytest.raises(S.Unspecified):
        S.roster_map("titles_that_do_not_exist", "domains")
    with pytest.raises(S.Unspecified):
        S.roster_map("titles", "a_key_that_is_not_there")


def test_purview_is_containment_and_stops_at_the_holders_own_domain():
    """`H-90`. Jordan: *"a Duke can revoke office from any individual in that office so long as
    that office is for a holding **under their purview**."*

    So authority over a governance act is RANK + CONTAINMENT — a property of the ACTOR's title and
    the containment tree — and NOT `remit:<act>`, which is a property of the target office.

    ⚠ AND PURVIEW IS DIRECTIONAL. A duke's purview reaches DOWN into the duchy and stops; the
    realm above him is not his.

    ⚠ THE RANK HALF WAS UNOBSERVED AND THIS IS WHERE IT IS OBSERVED. Deleting the title check from
    `under_purview` left all three governance tests green, because no test ever gave an actor a
    NON-TITLE office and asked for its purview — the operative rule as tested was containment
    alone, and `title_rank` had no caller outside its own assertion. The Dicastery case below is
    the discriminating one: mutate the title conjunct away and it goes red."""
    w = P.tiny_world()
    duke = "p_high"          # holds `off_duke`, whose `rung` is the duchy `D`
    assert w.offices["off_duke"].post == "Duke" and w.offices["off_duke"].rung == "D"
    assert w.rungs["D"].kind == "duchy" and w.rungs["R"].kind == "realm"
    for inside in ("D", "S", "Hh"):
        assert S.under_purview(w, duke, inside), (
            f"{inside} ({w.rungs[inside].kind}) is inside the duchy and is not under the duke")
    assert not S.under_purview(w, duke, "R"), (
        "the REALM is under the duke's purview — purview is reaching upward, so a duke could act "
        "on the king's domain")
    assert not S.under_purview(w, "p_low", "S"), (
        "a person holding no title has purview; then governing authority is not a title at all")

    # ⚠ THE RANK CONJUNCT, MADE OBSERVABLE. An ORDINARY office is not a title, so seating someone
    # on one at the duchy confers no purview over anything inside it. Without this case the title
    # check in `under_purview` is decorative and the suite cannot tell.
    _seat(w, "p_mid", "off_clerk", "Dicastery", "D")
    assert S.title_domain("Dicastery") is None, "the fixture stopped being a non-title"
    assert not S.under_purview(w, "p_mid", "S"), (
        "an ORDINARY office at the duchy confers purview over the settlement inside it — then "
        "rank is not part of the rule and any office-holder governs everything beneath them")

    # ⚠ TWO TITLES, AND THE OLD CODE TOOK WHICHEVER CAME FIRST IN AN INSERTION-ORDERED LIST.
    # `Office.rung` is Optional (the office-cluster case), the old generator yielded that `None`
    # as a value and stopped, so a Duke who was ALSO made a King lost purview over his own duchy.
    w2 = P.tiny_world()
    _seat(w2, "p_high", "off_king_cluster", "King", None, first=True)
    for inside in ("D", "S", "Hh"):
        assert S.under_purview(w2, "p_high", inside), (
            f"the duke lost purview over {inside} by ALSO being made a King with a null rung — "
            "the seat lookup is order-dependent and stops on the first title it meets")
    # and a second, non-null title must ADD purview rather than replace it
    w3 = P.tiny_world()
    w3.rungs["P2"] = S.Rung("P2", "province")
    w3.add_tenure(S.Tenure("t_p2", "P2", "R", "contain", 0))
    _seat(w3, "p_high", "off_count", "Count", "P2", first=True)
    assert S.under_purview(w3, "p_high", "P2") and S.under_purview(w3, "p_high", "S"), (
        "holding a county elsewhere cost the duke his duchy (or the reverse) — purview is a "
        "DISJUNCTION over every title held, not a lookup of one seat")

    # ⚠ GOVERNING AUTHORITY, SOVEREIGNTY AND OWNERSHIP ARE THREE THINGS, AND THIS ASSERTION USED
    # TO CHECK THE WRONG ONE. It read `not hasattr(w, "sovereign") and not hasattr(w, "holdings")`
    # — a test on ATTRIBUTE NAMES, which passed because the holdings relation was added as a
    # Tenure rather than as a field. Term-matching where the concept was meant, which is this
    # repository's signature error. The concept check: purview and holdings must be able to
    # DISAGREE, and here they do — the duke governs the settlement and owns none of it.
    assert S.under_purview(w, duke, "S") and not S.in_holdings(w, duke, "S"), (
        "governing authority and holdings answer alike here, so the two are one relation wearing "
        "two names and `H-90`'s distinction is not modelled")
    assert not hasattr(w, "sovereign"), (
        "the World has grown a sovereignty relation; `H-90` records sovereign power as RULED and "
        "NOT BUILT, and a silent one would make that row false")


def test_revoking_a_title_needs_holdings_and_revoking_an_office_needs_purview():
    """`H-90`. The two rules are different and which applies turns on whether the target is a
    TITLE. Jordan, 2026-09-02:

      · ordinary office — *"a Duke can revoke office from any individual in that office so long as
        that office is for a holding **under their purview**"*;
      · a title — *"King/Queen **cannot** revoke title of Duke/Duchess if they do not have duchy
        is in their holdings. King/Queen **can** revoke title of Duke/Duchess if the duchy is one
        of their holdings."*

    ⚠ THE NEGATIVE CASE IS THE WHOLE POINT, AND THE FIRST VERSION OF IT WAS VACUOUS. It asserted
    that a king could not revoke a duke's title without holding the duchy — in a world where
    `p_king` held NO OFFICE AT ALL, so he had no governing authority either and every rule refuses
    him. Mutating `_req_revoke` back to purview-for-everything left the assertion green: it could
    not observe the failure it excluded (§0.1 pt 2). The hazard Jordan's fourth message names — a
    King with realm-wide authority who does not hold the duchy — was constructed nowhere in the
    suite. It is constructed here, and the discriminator is asserted directly: purview says YES
    while the predicate says NO. Found by the governance-canon adversarial pass."""
    w = P.tiny_world()
    w.offices["off_duke"].revocation = "the crown's writ (harness fixture)"
    king, duke_office = "p_king", "off_duke"
    _seat(w, king, "off_king", "King", "R")
    assert S.title_domain(w.offices[duke_office].post) is not None, "the target is not a title"
    act = S.Act(id="k1", actor=king, verb="revoke", payload={"office": duke_office})

    # THE DISCRIMINATOR: he HAS the governing authority, and it is not enough.
    assert S.under_purview(w, king, "D") and S.highest_title_rank(w, king) > S.title_rank("Duke"), (
        "the king has no authority over the duchy in this world, so the negative below is vacuous "
        "— it would pass under the purview-only rule this ruling forbids")
    assert not S.in_holdings(w, king, "D")
    assert not S.REQUIRES_PREDICATES["revoke"](w, act), (
        "the king can revoke the duke's TITLE without holding the duchy — purview is standing in "
        "for holdings, which is the reading this ruling forbids")
    # THE POSITIVE: the same act, once the duchy is in his holdings.
    w.add_tenure(S.Tenure("t_land", king, "D", "hold", 0))
    assert S.in_holdings(w, king, "D") and not S.in_holdings(w, king, "S")
    assert S.REQUIRES_PREDICATES["revoke"](w, act), (
        "the duchy is in the king's holdings and he still cannot revoke the title")

    # ⚠ AND HOLDINGS ALONE MUST NOT BE ENOUGH EITHER — the mirror defect. The first conjunction
    # tested `in_holdings` and nothing else, so a clerk who happened to hold a duchy could unmake
    # its Duke. Governing authority and holdings are separate terms and BOTH are required.
    #
    # ⚠ THE DISCRIMINATING WORLD IS A FOREIGN KING, and the first version of this case was not it.
    # It used a Dicastery clerk, who has rank -1, so the RANK term refused him and dropping the
    # purview term changed nothing — the mutation ran green. A king of ANOTHER realm has the rank
    # and holds the duchy outright, and still has no governing authority over it: his seat is
    # `R2`, and walking up from `D` reaches `R` and stops. That is Jordan's separation of the
    # three concepts in one world, and it is what makes the purview term load-bearing.
    w4 = P.tiny_world()
    w4.offices["off_duke"].revocation = "the crown's writ (harness fixture)"
    w4.rungs["R2"] = S.Rung("R2", "realm")
    _seat(w4, "p_mid", "off_foreign_king", "King", "R2")
    w4.add_tenure(S.Tenure("t_foreign_land", "p_mid", "D", "hold", 0))
    assert S.in_holdings(w4, "p_mid", "D"), "the fixture does not hold the duchy; the case is moot"
    assert S.highest_title_rank(w4, "p_mid") > S.title_rank("Duke"), (
        "the foreign king does not outrank the duke, so RANK would refuse him and the purview "
        "term would again decide nothing — the same defect this case exists to close")
    assert not S.under_purview(w4, "p_mid", "D"), "the foreign king governs the duchy after all"
    assert not S.REQUIRES_PREDICATES["revoke"](
        w4, S.Act(id="c1", actor="p_mid", verb="revoke", payload={"office": "off_duke"})), (
        "a foreign king unmade a Duke by owning his duchy — holdings is standing in for governing "
        "authority, which is the same conflation in the opposite direction")

    # ⚠ AND NOBODY REVOKES THEIR OWN TITLE. A duke who holds his own duchy — the ordinary case,
    # and the one Jordan's *"do not necessarily have all … in their holdings"* presupposes is
    # common — satisfies purview and holdings on himself. Rank is what excludes it: strictly
    # higher, never equal.
    w5 = P.tiny_world()
    w5.offices["off_duke"].revocation = "the crown's writ (harness fixture)"
    w5.add_tenure(S.Tenure("t_selfland", "p_high", "D", "hold", 0))
    assert S.under_purview(w5, "p_high", "D") and S.in_holdings(w5, "p_high", "D")
    assert not S.REQUIRES_PREDICATES["revoke"](
        w5, S.Act(id="s1", actor="p_high", verb="revoke", payload={"office": "off_duke"})), (
        "the duke revoked his own title; equal rank is not excluded and the ladder decides nothing")

    # AND AN ORDINARY OFFICE TAKES THE OTHER RULE: purview, no holding required.
    w2 = P.tiny_world()
    w2.offices["off_dicastery"].revocation = "the duke's writ (harness fixture)"
    w2.offices["off_dicastery"].rung = "S"          # a settlement inside the duchy
    w2.add_tenure(S.Tenure("t_dic", "p_mid", "off_dicastery", "hold", 0))
    assert S.title_domain(w2.offices["off_dicastery"].post) is None, "the target IS a title"
    assert not S.in_holdings(w2, "p_high", "S"), "the duke holds the settlement; the test is moot"
    assert S.REQUIRES_PREDICATES["revoke"](
        w2, S.Act(id="d1", actor="p_high", verb="revoke",
                  payload={"office": "off_dicastery"})), (
        "the duke cannot revoke an ordinary office in his own duchy — the holdings rule has "
        "leaked onto offices, where the ruling asks only for purview")


def test_the_revocation_branch_executes_in_the_fold_and_not_only_as_a_predicate():
    """§0.2 — DONE MEANS IT RUNS. Every other assertion about `_req_revoke` calls the predicate
    DIRECTLY out of `REQUIRES_PREDICATES`, which is a claim about a function, not about a
    behaviour. The governance-canon pass established that in every world the suite builds, and in
    `headless.build_world` (which creates no offices at all), `_eligible` refuses `revoke` before
    the branch is ever reached — `off_duke`'s remit does not carry `revoke`. So the branch had
    never executed inside the resolver in any test or any run.

    This drives the fold. The office is given the `revoke` remit so Part E's `remit:revoke`
    eligibility is satisfied, and the act is resolved rather than asked about.

    ⚠ THE REMIT REQUIREMENT IS ITSELF `H-91`. Jordan's rule makes purview SUFFICIENT; Part E keeps
    `remit:revoke` necessary. This test satisfies both so the branch can be observed at all, and
    the conflict between them is registered rather than settled here."""
    w = P.tiny_world()
    w.offices["off_dicastery"].revocation = "the duke's writ (harness fixture)"
    w.offices["off_dicastery"].rung = "S"
    w.add_tenure(S.Tenure("t_dic", "p_mid", "off_dicastery", "hold", 0))
    w.offices["off_duke"].remit_acts = list(w.offices["off_duke"].remit_acts) + ["revoke"]
    act = S.Act(id="f1", actor="p_high", verb="revoke", payload={"office": "off_dicastery"})
    before = [t.id for t in w.tenures if t.kind == "hold" and t.object == "off_dicastery" and t.live]
    assert before, "the fixture office is unheld; the fold would have nothing to close"
    w.step = S.Step.RESOLVE
    events = S.SeasonDriver(w).resolve([act])
    kinds = [e.kind for e in events]
    assert "attempt.refused" not in kinds, (
        f"the fold refused a revocation whose preconditions all hold: {kinds}")
    assert "tenure.closed" in kinds, (
        f"the fold accepted the act and closed no tenure — the branch is reachable but inert: "
        f"{kinds}")
    assert not [t for t in w.tenures
                if t.kind == "hold" and t.object == "off_dicastery" and t.live], (
        "the tenure survived a revocation the fold accepted")



def test_the_corpus_cannot_reach_the_governance_branch_and_h71_is_not_the_reason():
    """§0.1 pt 4 — A NUMBER WITHOUT A CONTROL IS NOT A MEASUREMENT, IN EITHER DIRECTION, and
    `PROBE FLIPS 0` on the governance work is a TAUTOLOGY rather than a control.

    The governance commit published that zero as evidence with the reason *"a rule no corpus row
    reaches moves no verdict, and `H-71` is why it reaches none."* The zero is honest; **the
    reason is wrong**, and a wrong causal story is worse than none because it would survive the
    thing it blames being fixed. `H-71` governs `person_side_eligible`, which sits in `choose`.
    The probe corpus does not go through `choose` at all.

    The two ACTUAL reasons, asserted here so the claim is checkable rather than argued:

      1. **No probe mints a governance Act.** `F12`, the only probe about revocation, writes
         Tenure rows directly and never constructs `Act(verb="revoke")`.
      2. **`headless.build_world` creates no offices**, so the milestone run cannot reach a
         governance predicate whatever eligibility says.

    Either one alone makes the zero inevitable. This test goes red when a probe or the headless
    world starts reaching the branch — at which point `PROBE FLIPS 0` starts meaning something and
    the published sentence must be re-derived rather than reused. Found by the governance-canon
    adversarial pass."""
    import inspect
    gov = ("confer", "revoke", "dispatch", "convene")
    probe_src = inspect.getsource(P)
    minted = [v for v in gov if f'verb="{v}"' in probe_src or f"verb='{v}'" in probe_src]
    assert not minted, (
        f"a probe now mints {minted} — `PROBE FLIPS 0` may finally be a control rather than a "
        "tautology, and the reason published for it must be re-derived")
    # ⚠ UNCONDITIONAL, AND THE FIRST DRAFT WAS NOT. It read
    # `hw = HL.build_world(HL.load_case(...)) if hasattr(HL, "load_case") else None` and then
    # guarded on `hw is not None` — `load_case` does not exist, so the second half of the reason
    # was never asserted at all. §0.1 pt 2, inside the test written to enforce §0.1 pt 4, caught
    # by checking whether the branch ran rather than by reading it.
    import headless as HL
    hw = HL.build_world(seed=0)
    assert not hw.offices, (
        "the milestone world has offices now; the governance branch may be reachable in a run "
        "and the tautology above has become a measurement")


def _ten_seasons(w, seasons=10):
    """Run a world under the COMPUTED chooser and return per-season stores plus the acts minted.
    One owner, because three `W8` tests need the same run and a second copy would let them drift
    into describing different worlds."""
    d = S.SeasonDriver(w)
    mint = lambda pid, verb, subj: S.H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = S.make_chooser(w.fixtures, mint, verbs=S.resolvable_verbs())
    minted = []
    def spy(p, v, sc, ask):
        out = ch(p, v, sc, ask)
        for x in out:
            minted.extend(getattr(x, "acts", []) or [])
        return out
    hist = []
    for _ in range(seasons):
        d.season(spy, question=None, subsistence=P.SUBSIST)
        hist.append({r: dict(w.rungs[r].stores) for r in w.rungs})
    return hist, minted


def test_w8_matter_draws_before_it_produces_which_is_353s_stated_order():
    """#353 §25 VERBATIM: *"Events resolve FIRST, then bodies, larders, yield, travel, wear."*

    The order is SUBSTANTIVE, not cosmetic: drawing before producing means a season's subsistence
    comes out of LAST season's larder, so a rung CAN run short. Produce first and nothing ever
    does — every larder is topped up before anyone eats, and the starving world `W8`'s proof
    clause exists to catch becomes unreachable by construction.

    Asserted on the EMITTED ORDER rather than on the source, because the source is what a reader
    checks and the log is what ran."""
    w = P.tiny_world()
    d = S.SeasonDriver(w)
    w.step = S.Step.MATTER
    evs = d.matter([])
    order = [(e.kind, e.subject) for e in evs if e.kind in ("stores.changed", "yield.taken")]
    assert order, f"MATTER emitted no economy events at all: {[e.kind for e in evs]}"
    # `S` both draws (one person present) and produces (it owns both sites), so it is the one
    # rung where the order is observable at all.
    s_evs = [k for k, subj in order if subj == "S"]
    assert s_evs[:1] == ["stores.changed"], (
        f"`S` produced before it drew, or did not draw: {s_evs}. #353 §25 puts larders before "
        "yield, and reversing it means no rung can ever run short")
    assert "yield.taken" in s_evs, f"`S` owns two sites and produced nothing: {s_evs}"


def test_w8_a_worn_site_produces_less_and_a_dead_one_produces_nothing():
    """`H-93`'s scaling clause, which is the half that is NOT invented. Production is the base
    times `condition / condition_scale` times `season_factor`, so wear reaches the economy without
    a second wear concept being invented to make it do so.

    ⚠ THE CONTROL IS THE DEAD SITE. A test that only checked "a worn site yields less" would pass
    on any monotone function of condition including one that never reaches zero; a site AT zero
    must produce nothing at all, which is the clause that pins the shape."""
    def produced(cond):
        w = P.tiny_world()
        for st in w.sites.values():
            st.condition = cond
        d = S.SeasonDriver(w); w.step = S.Step.MATTER
        d.matter([])
        return sum(getattr(w.rungs["S"], "yield").values())
    full = produced(w0 := S.DEFAULT_FIXTURES.get("condition_scale"))
    half = produced(w0 // 2)
    dead = produced(0)
    assert full > half > 0, f"a worn site did not produce less: full={full} half={half}"
    assert dead == 0, f"a site at zero condition still produced {dead}"


def test_w8_the_none_arm_is_a_real_control_and_the_loader_refuses_it_as_a_default():
    """`H-93`'s `none` sweep arm. With every cell zero the economy has NO SOURCE, so every larder
    that anybody eats from falls monotonically — and `W8`'s proof clause must fail. A sweep whose
    control arm cannot break the claim is not a control (§0.1 pt 4).

    ⚠ AND THE CONTROL MUST NOT BE SHIPPABLE AS THE DEFAULT, which is why `_load_matter_tables`
    refuses an all-empty table: an economy with no source would otherwise pass every structural
    test in this file while meaning nothing, which is the dead-carrier defect one noun along."""
    w = P.tiny_world()
    d = S.SeasonDriver(w); w.step = S.Step.MATTER
    saved = dict(S.SITE_YIELD)
    try:
        for k in S.SITE_YIELD:
            S.SITE_YIELD[k] = {}
        d.matter([])
        assert not getattr(w.rungs["S"], "yield"), (
            "the `none` arm still produced; then the control cannot break the claim")
    finally:
        S.SITE_YIELD.clear(); S.SITE_YIELD.update(saved)
    assert sum(len(v) for v in S.SITE_YIELD.values()), "the restore lost the declared table"


def test_w8_the_proof_clause_is_not_met_and_h94_is_why():
    """⚠ `PLAN.md` `W8`'s PROOF IS **NOT MET**, AND THIS TEST RECORDS THAT RATHER THAN TUNING
    NUMBERS UNTIL IT IS. The clause asks for *"a 10-season seeded run in which stores neither
    monotonically deplete nor overflow — the control that catches a starving world"*. Measured on
    `tiny_world` under the computed chooser: the hearth's grain goes 2, 0, 0, 0, 0, 0, 0, 0, 0, 0
    (three people, no site, so it eats and cannot produce) while the settlement's goes 74 → 374,
    monotonically up. Both failure modes at once, in one world.

    THE CAUSE IS NOT THE ECONOMY'S NUMBERS. It is `H-94`: the computed chooser mints Acts with
    `payload: None` and `changes: []` — **0 of 56 over three seasons carry either** — so the two
    verbs that could move matter between the rungs cannot. `transfer` is refused on a precondition
    it has no operands to satisfy, and `work` emits `site.worked` while accumulating no delta, so
    site condition is a one-way ratchet and every producer eventually dies. A steady state needs a
    verb that MOVES something, and no minted act carries what to move.

    This test goes red when `H-94` closes, which is exactly when the proof clause becomes
    reachable and must be re-run rather than re-read."""
    hist, minted = _ten_seasons(P.tiny_world())
    hearth = [h["Hh"].get("grain", 0) for h in hist]
    settle = [h["S"].get("grain", 0) for h in hist]
    assert hearth == sorted(hearth, reverse=True) and hearth[-1] == 0, (
        f"the hearth no longer starves: {hearth}. `W8`'s proof clause may now be reachable — "
        "re-run it as a measurement instead of citing this test")
    assert settle == sorted(settle) and settle[-1] > settle[0], (
        f"the settlement no longer overflows: {settle}")
    assert minted, "the chooser minted nothing; this test cannot observe H-94"
    # ⚠ NARROWED: `H-94` IS HALF CLOSED AND THIS ASSERTION NOW PINS THE HALF THAT IS NOT. It read
    # `not [a for a in minted if a.payload or a.changes]` — no minted act carries anything — and
    # that stopped being true when `pack_scenes` began carrying the Candidate's SUBJECT into the
    # payload instead of folding it into the act id and discarding it. The subject was always
    # computed by `opening_set`; dropping it was a bug, and `_req_tell` reads exactly that key.
    #
    # What remains is the STRUCTURAL half: `Candidate := (verb, subject, why)` (S17) has no
    # operand field at all, so `transfer`'s `stores(hearth(giver), kind) >= amount` still has no
    # `kind` and no `amount` any part of the pipeline can carry. A minted act may therefore carry
    # a subject and NOTHING ELSE, and the day it carries a second key `H-94` has closed.
    extra = [a for a in minted if a.changes or set((a.payload or {})) - {"subject"}]
    assert not extra, (
        f"{len(extra)} of {len(minted)} minted acts now carry an operand beyond `subject` "
        f"({sorted({k for a in extra for k in (a.payload or {})} - {'subject'})}) — the structural "
        "half of `H-94` has closed, and `W8`'s proof clause is owed a fresh measurement")
    assert any((a.payload or {}).get("subject") for a in minted), (
        "no minted act carries a subject — `pack_scenes` has gone back to dropping the operand "
        "`opening_set` computed, and `tell` will be refused in every world again")


def test_w8_work_emits_a_success_while_repairing_nothing(): 
    """`H-94`'s worked case, and the sharpest single statement of it.

    §27.3 defers `work`'s delta to the fold's accumulator and clamps once — correct, and the
    reason `_eff_work` reports the site anyway is so the deferral does not read as a no-op. With
    NO DELTA DECLARED nothing is accumulated, so `site.worked` is an emitted success for a repair
    that did not happen. That is the rule this file states twice elsewhere (`_fold` refuses an
    effect that touched nothing; `conditional_emission_rows` exempts `(Record, ttl)` on the same
    argument) failing at the one place the fold cannot see it, because the effect DID report a
    subject."""
    w = P.tiny_world()
    site = w.sites["site_seam"]
    before = site.condition
    d = S.SeasonDriver(w); w.step = S.Step.RESOLVE
    evs = d.resolve([S.Act(id="wk", actor="p_low", verb="work", payload={"site": site.id})])
    assert [e.kind for e in evs] == ["site.worked"], [e.kind for e in evs]
    assert site.condition == before, (
        f"`work` moved condition {before} -> {site.condition} from an act declaring no delta; "
        "`H-94` has closed and this test is the record of a defect that no longer exists")


def test_no_person_can_choose_a_governance_verb_and_h71_is_why():
    """⚠ THE HALF THE SLICE DOES NOT BUILD, PINNED SO IT CANNOT BE ASSUMED AWAY.

    The four governance verbs execute when the fold is HANDED an Act. **No person can ever form
    one.** `person_side_eligible` declines every `remit:` alternative unconditionally — that is
    `H-71`, which the register already carried as `absent` and **tier 0**, with its `unblocks:`
    already reading *"9 of 32 verbs cannot be formed person-side — 8 remit-ONLY"*. All four
    governance verbs carry `remit:` as their ONLY eligibility, so `Query.opening_set` never offers
    them, in any world — including one where the actor genuinely holds the office whose remit
    names the act.

    So `resolvable_verbs()` moving 8 → 12 CANNOT AFFECT ANY RUN, and the claim *"the governance
    verbs now run"* is true of `resolve` and false of any person deliberating. This test is that
    sentence made mechanical: it goes red the day `H-71` closes, which is exactly when the claim
    becomes true. Found by the governance-slice adversarial pass."""
    w = P.tiny_world()
    duke = w.persons["p_high"]
    assert any(t.subject == "p_high" and t.object == "off_duke" and t.live for t in w.tenures)
    assert "confer" in w.offices["off_duke"].remit_acts
    # ⚠ SEVEN OF THE EIGHT, NOT ALL EIGHT. `succeed` is eligible by `own` and IS offerable — it
    # is the one governance verb a person can choose, and it is not in this slice (it has no
    # predicate and no effect). Scoping to the remit-only rows is what makes the assertion about
    # `H-71` rather than about `binding_decision`.
    gov = [v for v, r in S.VERB_TABLE.items()
           if r.stratum == "binding_decision"
           and all(alt.startswith("remit:") for alt in r.eligibility)]
    assert len(gov) >= 7, f"only {len(gov)} remit-only governance verbs; the roster has moved"
    offered = [v for v in gov if S.person_side_eligible(duke, S.VERB_TABLE[v])]
    assert not offered, (
        f"a person can now choose {offered} — `H-71` has closed, and the governance slice's claim "
        "that its verbs 'run' is finally true of a deliberating person rather than only of the "
        "fold. Re-read the slice's note and this test's docstring together before deleting either")
    # AND THE FOUR ARE IN THE FOLD'S SET, which is the half that DOES work — the two facts
    # together are the honest statement of where the slice stands.
    assert {"confer", "revoke", "dispatch", "convene"} <= S.resolvable_verbs(), (
        "the fold can no longer execute the governance verbs; the slice has regressed")


def test_a_binding_decision_lights_the_two_witness_channels_that_needed_one():
    """`W6`'s adversarial pass found `post_remit` and `chronicle` firing ZERO times, and traced it
    to the same cause: both need a `binding_decision`, and none was executable. This is the other
    half of that finding — with governance running, the channels are reachable.

    `chronicle` is an event-kind filter (it does not read `pid`) and `post_remit` needs the witness
    to hold an office whose remit covers the emitting verb, so the two admit different people."""
    # ⚠ THE EVENT COMES FROM A RUN, NOT FROM A CONSTRUCTOR. The first version built an
    # `S.Event(...)` by hand and called the predicates directly — and since neither predicate
    # consults `REQUIRES_PREDICATES`, `EFFECTS` or `resolvable_verbs()`, **it would have passed
    # unchanged on the tree before the governance slice existed**. It could not observe the change
    # it was offered as evidence for (§0.1 pt 2). The act is folded here, and the Event the fold
    # emitted is what the channels are asked about.
    w = P.tiny_world()
    duke = "p_high"
    # `confer`, not `revoke`: `off_duke`'s remit is `['issue','determine','confer','dispatch',
    # 'convene']` and carries no `revoke`, so a revoke by the duke is correctly INELIGIBLE — the
    # same trap the slice test fell into. The conferral basis is a harness fixture; Part E requires
    # an office to HAVE one and neither fixture office does.
    w.offices["off_dicastery"].conferral = "the duke's remit (harness fixture)"
    d = S.SeasonDriver(w)
    d.matter([])
    out = d.resolve([S.Act(id="g_conf", actor=duke, verb="confer",
                           payload={"office": "off_dicastery", "to": "p_mid"})],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    e = next((x for x in out if x.kind == "tenure.opened"), None)
    assert e is not None, (
        f"the fold emitted {[x.kind for x in out]} — no `tenure.closed` to test the channels with")
    everyone = list(w.persons)
    assert any(S.CHANNEL_PREDICATES["chronicle"](w, e, pid) for pid in everyone), (
        "`chronicle` does not fire on a binding decision's emission — then it can never fire at "
        "all, and `all_five` is permanently a measurement of fewer channels than it names")
    remit = [pid for pid in everyone if S.CHANNEL_PREDICATES["post_remit"](w, e, pid)]
    assert remit == [duke], (
        f"`post_remit` admits {remit}; it should admit exactly the holder of an office whose "
        "remit covers the verb that emitted this kind")


def test_w9_h80s_zero_control_is_executed_not_merely_described():
    """`H-80`'s cite says *"AT THE `0` SWEEP POINT NOTHING MATURES and the causal chain collapses
    to one link, which is the control"*. It said it in a YAML string and no test ran it.

    ⚠ THIS IS THE CONTROL FOR W9's HEADLINE RESULT. Chain depth is `1 + record_stages_default`
    when the run is long enough, so check 2's `>= 4` is met at the declared 3 with ZERO MARGIN and
    fails at 2. The four-Event chain rests on a number this session invented, and that is a fact
    about the milestone, not a reason to hide the sweep."""
    import headless as HL
    depths, matured = {}, {}
    for n in (0, 3, 6):
        w = HL.build_world(0, S.DEFAULT_FIXTURES.sweep("record_stages_default", n))
        d = S.SeasonDriver(w)
        mint = lambda pid, verb, subj: S.H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
        for _ in range(7):
            d.season(S.make_chooser(w.fixtures, mint, verbs=S.resolvable_verbs()),
                     None, HL.subsistence)
        by_id = {e.id: e for e in w.log}

        def depth(e, seen=()):
            if e.id in seen:
                return 0
            return 1 + max([depth(by_id[c], seen + (e.id,)) for c in e.causes if c in by_id] or [0])

        # ⚠ MEASURED OVER THE MATURATION CHAIN, NOT OVER THE WHOLE LOG. `W4` gave the wear and
        # claim-decay clocks real `causes[]`, so the global maximum is now dominated by them and
        # reads a flat 8 at EVERY sweep point — the control went BLIND to the thing it sweeps.
        # `H-80`'s cite is *"at the 0 sweep point NOTHING MATURES"*, and that clause is directly
        # checkable and survives `W4` intact; the *"collapses to one link"* clause was about a log
        # in which maturation was the only chain, and it is superseded rather than wrong.
        mats = [e for e in w.log if e.kind == "term.matured"]
        matured[n] = len(mats)
        depths[n] = max((depth(e) for e in mats), default=0)
    print(f"\n  H-80 sweep — maturations {matured}, longest maturation chain {depths}")
    assert matured[0] == 0 and depths[0] == 0, (
        f"at the 0 control {matured[0]} term.matured Events exist — `H-80`'s cite says "
        "NOTHING MATURES there, and if something does, that is a finding worth more than "
        "this control")
    assert depths[3] > depths[0] and depths[6] > depths[3], (
        f"the chain does not grow with the stage count: {depths} — then check 2's result does not "
        "rest on H-80 and this control is measuring nothing")
    assert depths[3] >= 4, depths


def test_w9_the_sweeps_the_register_declares_are_executed():
    """§G is declare · default · sweep, and `R2` checks only the first two. This runs the points
    `W9`'s own rows declare, because the previous pass added five sweeps and executed none — in
    the same session whose `test_w5_every_new_assumption_rows_sweep_is_actually_executed` names
    that exact laundering."""
    import headless as HL
    moved = {}

    # H-79 — the claim subject. `per_change` must change WHAT a ledger holds.
    subjects = {}
    for rule in sorted(S.CLAIM_SUBJECT_RULES):
        w = HL.build_world(0, S.DEFAULT_FIXTURES.sweep("claim_subject_rule", rule))
        d = S.SeasonDriver(w)
        mint = lambda pid, verb, subj: S.H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
        for _ in range(2):
            d.season(S.make_chooser(w.fixtures, mint, verbs=S.resolvable_verbs()),
                     None, HL.subsistence)
        subjects[rule] = len({c.subject for c in w.persons[HL.BAILIFF].ledger})
    moved["H-79 distinct claim subjects in the bailiff's ledger"] = subjects
    assert subjects["actor"] < subjects["per_change"], subjects

    # H-06 — the condition scale. Verdicts must be INVARIANT under an order of magnitude, because
    # every band is a fraction of the scale; a move would mean a band edge is read as an absolute.
    hashes = {}
    for scale in (100, 1000, 10000):
        fx = S.DEFAULT_FIXTURES.sweep("condition_scale", scale)
        fx = fx.sweep("band_floors", {k: {kk: vv * scale // 1000 for kk, vv in v.items()}
                                      for k, v in fx.get("band_floors").items()})
        fx = fx.sweep("wear_per_season", {k: max(1, v * scale // 1000)
                                          for k, v in fx.get("wear_per_season").items()})
        # BUILT FROM THE SWEPT FIXTURES, so the site's starting condition is on the same scale as
        # the floors it is compared against. Passing them to `build_world` is the fix; the first
        # version swept after building and compared a 1000-condition site to 10000-scale floors.
        w = HL.build_world(0, fx)
        # ⚠ EVERY CONDITION-UNIT FIXTURE SCALES TOGETHER, OR THE ARM IS CONFOUNDED. The first
        # version scaled the floors and left `wear_per_season` at 10 — so a site wore 10% of the
        # scale per season at 100 and 0.1% at 10000, and the sweep reported an event-count move
        # that was the confound, not a band edge read as an absolute. §0.1 point 1: the hazard is
        # changing a getter's source while a co-varying quantity still writes the old one.
        for p in w.persons.values():
            p.body = scale
        d = S.SeasonDriver(w)
        mint = lambda pid, verb, subj: S.H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
        for _ in range(2):
            d.season(S.make_chooser(w.fixtures, mint, verbs=S.resolvable_verbs()),
                     None, HL.subsistence)
        hashes[scale] = len(w.log)
    moved["H-06 events by condition_scale"] = hashes
    assert len(set(hashes.values())) == 1, (
        f"the event count moves with the condition scale: {hashes}. A band edge is being read as "
        "an absolute rather than as a fraction of the scale, which is what this sweep is for.")

    for k, v in moved.items():
        print(f"\n  {k}: {v}")


# ===========================================================================
# W10 — DECLARED ROUTING. Four router guards retired with the router; this is what replaces
# them, and it forbids the SHAPE rather than enumerating the words (`G2`).
# ===========================================================================

# --- the taint check that replaces the router guards ----------------------------------------
# `need` is the case corpus's PROSE. `W10`'s whole claim is that no verdict turns on it: the only
# thing the pipeline may do with a need is HASH it (`need_sha`, the binding) or STORE it. Anything
# else -- a regex, a substring test, a call whose result is used -- is the router, whatever it is
# called and wherever it lives.
#
# ⚠ THE THREE EVASIONS THIS REPLACES, all found by the `W10` adversarial pass, and each of which
# the ROUTER IT REPLACED WOULD HAVE WALKED THROUGH:
#   1. it was scoped to a function literally named `grade`, so a helper called BY grade was free;
#   2. it fired only on a receiver literally named `re`, so `import re as _re`, a precompiled
#      `rx.search(need)` -- WHICH IS WHAT `COMPILED` ACTUALLY DID -- or any third-party matcher
#      was free;
#   3. it forbade three names (`ROUTES`, `COMPILED`, `def route(`), so a rename was free.
# A roster of forbidden names is the same defect as a roster of routed words, one level up.
# `PLAN.md` `G2`: forbid the shape, never enumerate the words.

# The three declared sanitizers, read off `exercises.py` rather than retyped: `need_sha` BINDS a
# need to its declaration, `need_display` RENDERS one into an artifact cell, `need_terms`
# TOKENISES one for a printed table nothing reads back. Everything else done with a need's text
# is the router.
_SANITIZERS = ("need_sha", "need_display", "need_terms")

# Taint does not flow through an operation whose RESULT CANNOT BE A STRING. `len(core)` embeds a
# tainted name and yields an `int`; propagating through it tainted `report.py`'s entire output list
# and reported three offences in `"\n".join(out)` — rendering, not routing, and `G4` weighs an
# over-refusal equally with an invention.
#
# ⚠ THIS IS A STATEMENT ABOUT RETURN TYPES, NOT A ROSTER OF BLESSED FUNCTIONS, and the difference
# is the whole reason it is allowed to exist in a file that deletes routers for being rosters. A
# name belongs here only if it PROVABLY cannot return a `str`. `sorted`, `max` and `min` do not
# qualify — they return their inputs.
_NON_TEXT_BUILTINS = ("len", "sum", "abs", "round", "bool", "int", "float")


def _callee_name(call) -> str:
    import ast as ast_
    f = call.func
    if isinstance(f, ast_.Name):
        return f.id
    if isinstance(f, ast_.Attribute):
        return f.attr
    return ""


def _is_extraction(node) -> bool:
    """Where a need's TEXT enters an expression from a corpus row: `x["need"]`, `x.get("need")`.

    ⚠ NOT `Name("need")`. Keying on the identifier was the defect that made the first version a
    NAME TEST WEARING A DATAFLOW TEST'S CLOTHES: rename one variable and the retired router came
    back verbatim past all five plants. The extraction is the KEY, which the corpus owns and a
    rename cannot touch."""
    import ast as ast_
    if isinstance(node, ast_.Subscript) and isinstance(node.slice, ast_.Constant) \
            and node.slice.value == "need":
        return True
    if isinstance(node, ast_.Call) and isinstance(node.func, ast_.Attribute) \
            and node.func.attr == "get" and node.args \
            and isinstance(node.args[0], ast_.Constant) and node.args[0].value == "need":
        return True
    return False


def _summarise(tree) -> dict:
    """`id(node) -> (names, has_extraction)` for every subtree, computed ONCE, bottom-up, with the
    summary stopping at a declared sanitizer.

    ⚠ THIS EXISTS FOR SPEED AND THE SPEED IS LOAD-BEARING. Re-walking each subtree inside the
    taint fixpoint is quadratic, and on `shape.py` (3,193 lines) the first version of this dataflow
    did not finish in two minutes. A guard nobody can afford to run is a guard that gets deleted."""
    import ast as ast_
    out: dict = {}

    def visit(n):
        for c in ast_.iter_child_nodes(n):
            visit(c)
        if isinstance(n, ast_.Call) and (_callee_name(n) in _SANITIZERS
                                         or _callee_name(n) in _NON_TEXT_BUILTINS):
            out[id(n)] = (frozenset(), False)   # a sha, a cell, or a number — never prose
            return
        names, ex = set(), _is_extraction(n)
        if isinstance(n, ast_.Name):
            names.add(n.id)
        for c in ast_.iter_child_nodes(n):
            cn, ce = out[id(c)]
            names |= cn
            ex = ex or ce
        out[id(n)] = (frozenset(names), ex)

    visit(tree)
    return out


def _carries_need(node, tainted: set, summary: dict) -> bool:
    """Does this subtree carry raw need text? A sha is a binding key and an escaped cell is an
    artifact — neither is prose — so the three declared sanitizers stop it."""
    names, ex = summary[id(node)]
    return ex or bool(names & tainted)


def _scopes(tree) -> list:
    """`(name, nodes, params)` per LEXICAL SCOPE: the module with every function body removed, and
    each function or lambda body on its own.

    ⚠ TAINT IS A PROPERTY OF A NAME IN A SCOPE, and computing it module-wide is an over-refusal
    (`G4` weighs one equally with an invention). Pooling every name in the file let
    `need_display`'s local `out = need.replace(...)` taint the unrelated `out` in `load()` and
    `coverage()`, and the guard reported twenty offences in correct code. A guard that fires on
    lawful code pushes the fix toward deleting it."""
    import ast as ast_
    fn_t = (ast_.FunctionDef, ast_.AsyncFunctionDef, ast_.Lambda)

    def own(root):
        out, stack = [], [root]
        while stack:
            n = stack.pop()
            for c in ast_.iter_child_nodes(n):
                if isinstance(c, fn_t):
                    continue          # its own scope; visited separately
                out.append(c)
                stack.append(c)
        return out

    scopes = [("<module>", own(tree), [])]
    for f in ast_.walk(tree):
        if not isinstance(f, fn_t):
            continue
        # THE SANITIZERS' OWN BODIES ARE THE LAWFUL OPERATIONS, and scanning them reports the
        # binding itself as the router.
        if getattr(f, "name", None) in _SANITIZERS:
            continue
        a = f.args
        params = [x.arg for x in list(a.posonlyargs) + list(a.args) + list(a.kwonlyargs)]
        scopes.append((getattr(f, "name", "<lambda>"), own(f), params))
    return scopes


def _tainted_names(nodes, params, summary) -> set:
    """Every NAME in ONE SCOPE that can hold need text, to a fixpoint — through assignment,
    walrus, `for` targets, comprehension targets and `with ... as`.

    ⚠ THIS IS THE HALF THE FIRST VERSION DID NOT HAVE, and without it the check was a NAME TEST
    WEARING A DATAFLOW TEST'S CLOTHES. `text = r["need"]` laundered the taint in one statement, so
    the retired router came back verbatim with ONE IDENTIFIER RENAMED, past all five of its
    plants. Taint is seeded from the EXTRACTION KEY, which the corpus owns and a rename cannot
    reach."""
    import ast as ast_
    # ⚠ A PARAMETER NAMED `need` IS A SEED; A LOCAL NAMED `need` IS NOT. Seeding the bare name in
    # every scope was an over-refusal: `report.py`'s `need = EX.need_display(...)` holds a
    # SANITIZED cell, and treating it as prose reported eighteen offences in correct rendering
    # code. A local gets its taint from its assignment, which is the accurate rule; a parameter
    # has no assignment to read, so it is seeded by name.
    tainted = {p for p in params if p == "need"}
    # Only assignment-shaped nodes can move taint. Collect them once instead of re-filtering the
    # whole scope on every pass of the fixpoint.
    moves = []
    for n in nodes:
        targets, val = [], None
        if isinstance(n, ast_.Assign):
            targets, val = n.targets, n.value
        elif isinstance(n, ast_.AnnAssign) and n.value is not None:
            targets, val = [n.target], n.value
        elif isinstance(n, ast_.NamedExpr):
            targets, val = [n.target], n.value
        elif isinstance(n, (ast_.For, ast_.AsyncFor)):
            targets, val = [n.target], n.iter
        elif isinstance(n, ast_.comprehension):
            targets, val = [n.target], n.iter
        elif isinstance(n, ast_.withitem) and n.optional_vars is not None:
            targets, val = [n.optional_vars], n.context_expr
        if val is None:
            continue
        bound = {sub.id for tg in targets for sub in ast_.walk(tg) if isinstance(sub, ast_.Name)}
        if bound:
            moves.append((bound, val))
    changed = True
    while changed:
        changed = False
        for bound, val in moves:
            if not _carries_need(val, tainted, summary):
                continue
            fresh = bound - tainted
            if fresh:
                tainted |= fresh
                changed = True
    return tainted


def _is_unclear_marker(node) -> bool:
    """The ONE carve-out: the `UNCLEAR:` marker, which the CASE SOURCE writes ABOUT ITSELF — the
    source saying it does not know — and which is not a claim about what the row needs.

    ⚠ STRUCTURAL, NOT A SUBSTRING OF THE SOURCE TEXT. The first version skipped any node whose
    `get_source_segment` contained the word, so for a multi-line call a COMMENT INSIDE THE
    PARENTHESES exempted it — a general escape hatch rather than a carve-out. The pattern must now
    be a STRING LITERAL passed to the call."""
    import ast as ast_
    if not isinstance(node, ast_.Call):
        return False
    return any(isinstance(a, ast_.Constant) and isinstance(a.value, str) and "UNCLEAR" in a.value
               for a in node.args)


def _need_taint_offenders(src: str) -> list:
    """Every expression that turns a case's need TEXT into a value something else consumes.

    Three shapes are offences:
      * a CALL that carries need text and whose RESULT IS USED. A call whose result is discarded
        (a bare expression statement) stores; a call whose result feeds something else DECIDES.
      * a COMPARISON carrying need text — `if "threat" in need` is a router with no call in it.
      * an ATTRIBUTE on need text used as a VALUE — `max(ROUTES, key=need.count)` hides a router
        inside an exempt builtin, and a bound method is not a Call node.

    Lawful: the three declared sanitizers, a bare builtin callee (storage and display; a router
    nested inside one is a Call in its own right and is checked separately), and the `UNCLEAR`
    marker."""
    import ast as ast_
    import builtins as _b
    tree = ast_.parse(src)
    discarded = {id(n.value) for n in ast_.walk(tree)
                 if isinstance(n, ast_.Expr) and isinstance(n.value, ast_.Call)}
    # An Attribute that IS a call's `func` is covered by the Call rule; flagging it again fires on
    # `out.append(...)`, which is storage. The Attribute rule exists for a bound method used as a
    # VALUE — `max(ROUTES, key=need.count)` — which is never a call's func.
    call_funcs = {id(n.func) for n in ast_.walk(tree) if isinstance(n, ast_.Call)}
    offenders = []
    # ⚠ EVERY SCOPE, INCLUDING THE MODULE'S OWN. The first version descended only into
    # `FunctionDef` bodies, so a module-level comprehension or `route = lambda need:
    # PATTERNS.match(need)` was never visited — and the router this replaced was module-level
    # `ROUTES`/`COMPILED`.
    summary = _summarise(tree)
    for _scope, nodes, params in _scopes(tree):
        tainted = _tainted_names(nodes, params, summary)
        for node in nodes:
            if _is_extraction(node):
                continue          # the EXTRACTION of the need from its row — not a decision
            # ⚠ `get_source_segment` IS COMPUTED ONLY FOR AN OFFENDER. It re-splits the whole file
            # on every call, so calling it per node made the scan quadratic in file size: 2.3s on
            # a 237-line module and a two-minute timeout on `probes.py`.
            hit = False
            if isinstance(node, ast_.Call):
                hit = not (_callee_name(node) in _SANITIZERS or _is_unclear_marker(node)
                           or (isinstance(node.func, ast_.Name) and hasattr(_b, node.func.id))
                           or id(node) in discarded) and _carries_need(node, tainted, summary)
            elif isinstance(node, ast_.Compare):
                hit = _carries_need(node, tainted, summary)
            elif isinstance(node, ast_.Attribute) and id(node) not in call_funcs:
                hit = _carries_need(node.value, tainted, summary)
            if hit:
                offenders.append((node.lineno,
                                  (ast_.get_source_segment(src, node) or "")[:80]))
    return sorted(set(offenders))


def _pipeline_sources() -> list:
    """Every module that can move a verdict — which is every module here except the guards.

    ⚠ DERIVED, NOT LISTED. The first version scanned a two-name tuple, `("run_cases.py",
    "exercises.py")`, which left `report.py` — the SOLE EMITTER of every artifact — unscanned,
    and `report.py` had two inline need operations at the time. `test_jordan_no_definition_is_
    hardcoded_in_a_body` already settled this shape four hundred lines above: a filename roster is
    a router and `G2` forbids it. The `test_` prefix is pytest's own discovery rule, not one of
    mine."""
    return sorted(f for f in HERE.glob("*.py") if not f.name.startswith("test_"))


def test_w10_no_verdict_turns_on_the_text_of_a_need():
    r"""THE ROUTER CANNOT COME BACK BY ACCRETION, because the SHAPE is forbidden rather than its
    vocabulary policed.

    `PLAN.md` §7.4 is why it is worth a guard at all: the bare-token class recurred SIX times, and
    the whitelist built for the fourth did not catch the fifth (`age\w*` matching AGENT, AGENCY,
    AGENDA). A roster of words is a specification nobody ratified."""
    scanned, bound_here = 0, 0
    for f in _pipeline_sources():
        src = f.read_text()
        scanned += 1
        bad = _need_taint_offenders(src)
        assert not bad, (
            f"{f.name}: a need's TEXT reaches a decision:\n  "
            + "\n  ".join(f"{ln}  {sg}" for ln, sg in bad))
        bound_here += _sanitizer_calls_on_need(src)
    # ⚠ AND THE SCAN MUST BE ABLE TO SAY IT SCANNED SOMETHING. Without this the guard is green on
    # a corpus it never reached: rename the extraction key, or point `_pipeline_sources` at an
    # empty directory, and `not []` is trivially true. §0.1 pt 2 — the same reason the AST write
    # sweep asserts `assert pairs` and the gate walk asserts it found a gate.
    assert scanned >= 3, f"the taint scan visited only {scanned} module(s)"
    assert bound_here, (
        "no declared sanitizer is ever applied to an extracted need in the whole pipeline — "
        "either routing has moved somewhere this scan cannot see, or the extraction key changed "
        "and every taint source above is silently matching nothing")


def _sanitizer_calls_on_need(src: str) -> int:
    """How many times a declared sanitizer is applied to need text. The liveness half of the
    guard above: a positive count proves the taint sources match the real code."""
    import ast as ast_
    tree = ast_.parse(src)
    n = 0
    summary = _summarise(tree)
    for _scope, nodes, params in _scopes(tree):
        tainted = _tainted_names(nodes, params, summary)
        for node in nodes:
            if isinstance(node, ast_.Call) and _callee_name(node) in _SANITIZERS:
                if any(_carries_need(a, tainted, summary) for a in node.args):
                    n += 1
    return n


def test_the_taint_check_catches_the_router_it_replaced():
    """§0.1 pt 2. Each plant is a real evasion a previous version of this guard permitted; the
    first five defeated the version that shipped with `W10`, and the last four defeated the
    version that replaced it and were found by that stage's adversarial pass."""
    plants = {
        "the router as it actually was -- a precompiled pattern, no `re.` receiver":
            "COMPILED = []\ndef route(need):\n    for pid, rx in COMPILED:\n"
            "        if rx.search(need):\n            return pid\n",
        "an aliased module, so the receiver is not named `re`":
            "import re as _re\ndef grade(r):\n    need = r.get('need', '')\n"
            "    return _re.search('threat', need)\n",
        "a helper called BY grade, so function-name scoping misses it":
            "def _aim(need):\n    return PATTERNS.match(need)\n"
            "def grade(r):\n    return _aim(r['need'])\n",
        "no call at all -- a substring test":
            "def grade(r):\n    need = r.get('need', '')\n"
            "    if 'threat' in need:\n        return 'P22'\n    return None\n",
        "a method on the need itself":
            "def grade(r):\n    need = r['need']\n"
            "    return 'P22' if need.lower().startswith('an institution') else None\n",
        # --- the four the `W10` adversarial pass found in the version above ---
        "TAINT LAUNDERING: the retired router verbatim with ONE IDENTIFIER RENAMED":
            "COMPILED = []\ndef grade(case):\n    for r in case['season_requires']:\n"
            "        text = r['need']\n        for pid, rx in COMPILED:\n"
            "            if rx.search(text):\n                return pid\n",
        "MODULE SCOPE: a lambda router that is inside no function at all":
            "route = lambda need: PATTERNS.match(need)\n",
        "THE `UNCLEAR` ESCAPE HATCH: the word in a comment inside the call's own parentheses":
            "def grade(r):\n    need = r['need']\n    return _aim(\n        # UNCLEAR\n"
            "        need)\n",
        "A BOUND METHOD HANDED TO AN EXEMPT BUILTIN":
            "def grade(r):\n    need = r['need']\n    return max(ROUTES, key=need.count)\n",
    }
    for why, src in plants.items():
        assert _need_taint_offenders(src), f"the taint check does not catch: {why}"
    # AND IT DOES NOT FIRE ON THE LAWFUL USES, or it would push the fix toward deleting correct
    # code -- an over-refusal, which `PLAN.md` `G4` weighs EQUAL to an invention.
    lawful = (
        "def grade(r):\n"
        "    need = r.get('need', '')\n"
        "    if re.match(r'\\s*UNCLEAR\\b', need, re.I):\n        return None\n"
        "    entry = dict(need=need, title=need[:60])\n"
        "    log.append(str(need))\n"
        "    cell = EX.need_display(need, 190)\n"
        "    return OVERLAY.get(EX.need_sha(need), {})\n")
    assert not _need_taint_offenders(lawful), _need_taint_offenders(lawful)


def test_w10_the_deciding_path_is_the_authored_overlay():
    """The complement of the taint check: forbidding the old path proves nothing unless the new
    one is load-bearing. Asserted by EXECUTION rather than by reading `grade`'s source -- the
    previous version checked that the strings `OVERLAY` and `need_sha` appeared in the body,
    which a comment satisfies."""
    ok = _a_satisfied_token()
    need = "a wholly invented need that appears in no corpus file"
    bare = R.grade({"id": "T", "season_requires": [{"need": need, "hardness": "core"}]})
    assert bare["verdict"] == "NOT-ASSESSED" and bare["core_unmapped"] == 1, bare
    with _declared("T", {need: [ok]}):
        got = R.grade({"id": "T", "season_requires": [{"need": need, "hardness": "core"}]})
    assert got["verdict"] == "PLAYABLE" and got["core_routed"] == 1, got
    assert not (HERE / "route_precision.py").exists(), (
        "route_precision.py survives -- a guard for a thing that no longer exists is the "
        "apparatus §0.3 is about, and `PLAN.md` W10 retires it with the router")


def test_g12_a_cite_may_not_argue_for_a_grade_the_row_does_not_carry():
    """`H-46`'s cite was written from neighbouring `H-20`'s and kept its conclusion — *"THIS ROW
    THEREFORE STAYS `assumption`"* — on a row graded `absent`. It therefore satisfied `G6` (*a
    refusal nobody argued for is not a refusal*) on an argument for a DIFFERENT refusal.

    Not bookkeeping: `H-46` is `tier: 0`, so its grade is inside artifact 0's verdict, and
    `resolve()` turns a grade into a case verdict. Found by the `W10` adversarial pass."""
    import register as REG
    reg = REG.load()
    assert not REG.rule_G12(reg), REG.rule_G12(reg)
    # ⚠ AND IT CAN FIRE. A rule asserted only against a clean register is a rule nobody has seen
    # work — §0.1 pt 2, and the reason three guards in this file were rewritten this session.
    planted = dict(reg, rows=[dict(r) for r in reg["rows"]])
    victim = next(r for r in planted["rows"] if r.get("grade") == "absent")
    victim["cite"] = "PLAN §3.2. THIS ROW THEREFORE STAYS `assumption` and must not be closed."
    hits = REG.rule_G12(planted)
    assert hits and victim["id"] in hits[0], hits


def test_a_duplicate_yaml_key_is_refused_rather_than_silently_resolved():
    """`yaml.safe_load` keeps the LAST of two identical keys. `verb_table.yaml` declared
    `writes_note` twice on `issue` and twice on `petition` — once with Part E's transcribed cell
    and once with the `W3` audit's correction — so the transcription was discarded at load, in the
    one file whose whole purpose is to be a faithful capture of Part E.

    The same class already cost this instrument once at the ROW level (two `(Office, exists)` rows,
    gate behaviour depending on file order); that fix guarded rows only. `shape.load_yaml` guards
    every mapping in every file this instrument reads. Found by the `W10` adversarial pass."""
    # NOTE ON SEVERITY, because the first version of this docstring overstated it: `writes_note`
    # has no reader, so THAT instance lost transcribed text and not behaviour. See below.
    import pytest as _pt
    with _pt.raises(ValueError, match="duplicate key"):
        S.load_yaml("verbs:\n  - verb: x\n    note: a\n    note: b\n")
    # ⚠ AND THE SCOPE OF THAT PARTICULAR LOSS, STATED ACCURATELY RATHER THAN AT ITS MOST ALARMING:
    # `writes_note` is NOT a field of `VerbRow`, so nothing in the fold ever read either cell. What
    # was lost was TRANSCRIBED TEXT IN THE CAPTURE — bad in the file whose purpose is fidelity to
    # Part E, and not a behaviour change. The guard is still worth its existence, because the same
    # class DID change behaviour once at the row level (two `(Office, exists)` rows, gate behaviour
    # depending on file order). Asserted on the FILE, which is where the defect was.
    vt = S.load_yaml(S.VERB_TABLE_YAML.read_text())
    rows = {r["verb"]: r for r in (vt["verbs"] if isinstance(vt, dict) else vt)}
    for verb, cell in (("issue", "a Dispensation is not a state write"),
                       ("petition", "a Petition is created, not written")):
        note = rows[verb].get("writes_note") or ""
        assert cell in note, f"{verb}: Part E's transcribed cell is missing from `writes_note`"
        assert "W3, ON THE W2 AUDIT" in note, f"{verb}: the audit correction was lost instead"
    # every data file the instrument owns loads under the strict reader
    for f in (S.WRITE_MATRIX_YAML, S.ROSTERS_YAML, S.VERB_TABLE_YAML):
        S.load_yaml(f.read_text())


def test_w10_every_declared_token_resolves_and_every_binding_is_live():
    """An `exercises:` token must NAME something real, and every overlay entry must bind to a
    live corpus row.

    ⚠ ASSERTED ON `resolve`'s `bound` FLAG, NOT ON ITS MESSAGES. The first version matched THREE
    OF FOUR of `resolve`'s failure strings (`"no probe"`, `"no register row"`, `"on no verb-table
    row"`), so a token naming a nonexistent Event kind -- the fourth, `"on no emits: column"` --
    was unguarded, and rewording any of the other three would have silently disarmed the rest.
    `PLAN.md` `G3`: assert the PROPERTY, never the string. `bound` is that property, and it is
    deliberately NOT `ok`: a token may name a real thing that is `absent`, unexecutable or
    gapping, which is the instrument working rather than an authoring error.

    ⚠ AND THE BINDING CHECK IS THE ONE THE `W9` PASS ASKED FOR. The first overlay was keyed on
    nothing: it paraphrased each need, so an author could annotate a row that had been reworded --
    or that never existed -- and no one would know. Four of its seven entries in fact bound to
    nothing, and `need_sha` caught all four on its first run."""
    ov = EX.load()
    every = []
    for kind in ("NPC", "ARC"):
        cases = R.load_cases(kind)
        every += cases
        orphans = EX.unbound(ov, cases)
        assert not orphans, (
            f"{len(orphans)} overlay entr(ies) bind to no live {kind} row — a reworded corpus row "
            f"orphaned its annotation: {orphans[:4]}")
    # ⚠ AND THE HOLE `unbound` CANNOT SEE. It is called per lane and skips an id it does not
    # recognise, because in a single-lane call an id from the other lane is legitimately absent.
    # A file whose `case:` names a case in NEITHER lane therefore passed BOTH calls with every row
    # bound to nothing. Found by the `W10` adversarial pass.
    assert not EX.orphan_cases(ov, every), (
        f"overlay file(s) name a case that exists in neither lane, so every row in them is bound "
        f"to nothing: {EX.orphan_cases(ov, every)}")
    reg = R._register()
    unbound_tokens = []
    for cid, rows in ov.items():
        for sha, row in rows.items():
            for tok in row.get("exercises") or []:
                got = EX.resolve(tok, probes={p: R.run_probe(p) for p in P.PROBES},
                                 verb_table=S.VERB_TABLE, resolvable=S.resolvable_verbs(),
                                 register=reg, matrix=S.MATRIX)
                if not got.get("bound"):
                    unbound_tokens.append(f"{cid} declares {tok!r}: {got['detail']}")
    assert not unbound_tokens, "declared token(s) name nothing:\n  " + "\n  ".join(unbound_tokens)


def test_the_binding_guard_sees_all_four_ways_a_token_can_name_nothing():
    """§0.1 pt 2, and the reason the guard moved off the message strings: it must observe every
    branch, INCLUDING the Event-kind one it used to miss entirely. One plant per shape."""
    reg = R._register()
    kw = dict(probes={}, verb_table=S.VERB_TABLE, resolvable=S.resolvable_verbs(),
              register=reg, matrix=S.MATRIX)
    for token, shape in (("probe:P_NOT_A_PROBE", "probe"),
                         ("H-999", "hole"),
                         ("no.such.event.kind", "kind"),
                         ("verb_that_is_on_no_row", "verb")):
        got = EX.resolve(token, **kw)
        assert got["kind"] == shape and got["bound"] is False, (shape, got)
    # AND THE CONVERSE, which is the half an `ok`-based guard gets wrong: a token that names a
    # REAL thing whose verdict is bad is BOUND. Confusing the two would turn every design finding
    # into an authoring error and quietly empty the instrument.
    absent = next((h for h, r in sorted(reg.items()) if r.get("grade") == "absent"), None)
    assert absent, "no register row is `absent` -- the converse cannot be planted"
    got = EX.resolve(absent, **kw)
    assert got["bound"] is True and got["ok"] is False, got


def test_w10_no_playable_verdict_rests_on_an_undeclared_row():
    """`PLAN.md` `W10`'s third Proof clause, asserted over the whole corpus rather than sampled.

    ⚠ THE CORPUS CLAUSE IS VACUOUS TODAY AND SAYS SO. Nothing in either lane grades PLAYABLE, so
    a `for`-loop over the PLAYABLE verdicts iterates zero times and the assertion below is true of
    an empty set -- §42.2's polarity rule applied to a guard rather than to evidence: no PLAYABLE
    case is not the same fact as no BAD PLAYABLE case. It is kept because it is the clause that
    starts biting the moment authoring reaches a full case, and it is PAIRED with a constructed
    control so the mechanism it guards is exercised now rather than whenever that happens."""
    rep = json.loads((HERE.parent / "runs" / "results.json").read_text())
    bad = [c["id"] for sec in ("NPC", "ARC") for c in rep[sec]
           if c["verdict"] == "PLAYABLE" and c["core_unmapped"]]
    assert not bad, f"PLAYABLE with undeclared core rows: {bad}"
    live = [c["id"] for sec in ("NPC", "ARC") for c in rep[sec] if c["verdict"] == "PLAYABLE"]
    if not live:
        # THE CONTROL. PLAYABLE must be REACHABLE (or the clause above is unfalsifiable in a
        # second way -- a pipeline that graded nothing PLAYABLE ever would also pass), and adding
        # one undeclared core row to that same reachable case must take it away.
        ok = _a_satisfied_token()
        a, b = "a fully declared core need", "the same case, one core row undeclared"
        with _declared("T", {a: [ok]}):
            reach = R.grade({"id": "T", "season_requires": [{"need": a, "hardness": "core"}]})
            lose = R.grade({"id": "T", "season_requires": [
                {"need": a, "hardness": "core"}, {"need": b, "hardness": "core"}]})
        assert reach["verdict"] == "PLAYABLE", reach
        assert lose["verdict"] == "NOT-ASSESSED" and lose["core_unmapped"] == 1, lose
    authored = sum(len(c["routed"]) for sec in ("NPC", "ARC") for c in rep[sec])
    undeclared = sum(len(c["unmapped"]) for sec in ("NPC", "ARC") for c in rep[sec])
    print(f"\n  W10 — {authored} rows declared, {undeclared} awaiting an author. "
          "NOT-ASSESSED now means the second, which is a fact about authoring.")
    assert authored, "no row is declared at all — the overlay is not being read"


def test_the_corpus_runs_and_the_ranking_cannot_discriminate():
    """JORDAN, 2026-09-02: *"shouldn't we consider running all NPCs and all arcs in our test runs?
    a larger surface introduces more complexity, but given our goals, what solves one may solve
    another while providing more pushback as to whether something is the RIGHT solve."*

    `corpus_run.py` executes every case; `run_cases.py` grades them. Two different questions.

    ⚠ REV 2. THE FIRST VERSION OF THIS TEST NAMED THREE FALSIFIERS AND IMPLEMENTED ONE. It claimed
    to go red *"the day a fourth world becomes reachable"* while asserting `len(worlds) >= 3`,
    which a fourth world passes; and *"the day an eighth verb fires"* while asserting a nesting
    that holds for any count and a governance subset that survives `destroy_record` firing. §0.1
    pt 3 — name the falsifier or you have not attacked the result — so the counts are asserted
    EXACTLY here, and every one of them goes red on movement in either direction.

    ⚠ AND IT PINNED THE WRONG CLAIM. Rev 1 asserted *one verb set across three worlds* as evidence
    the rung ladder decides nothing. Its adversarial pass showed that was entailed: `View.__slots__`
    closes the rung channel by TYPE (L2), and the fixture made all three worlds identical
    person-side. The worlds now genuinely differ — per-case convictions, season counts 1..6,
    forced deadlines — and the executed set is STILL one, for the reason this test now pins:
    §F2's scoring separates 2..7 of 22 candidates and the rest tie (`H-96`)."""
    import corpus_run as C
    import run_cases as R
    rows = [C.run_case(c, 0, lane) for lane in ("NPC", "ARC") for c in R.load_cases(lane)]
    bad = [r for r in rows if r["status"] == "INSTRUMENT-DEFECT"]
    assert not bad, (f"the corpus runner has a call-site bug on {[(r['id'], r['why']) for r in bad][:3]}"
                     " — an instrument defect, which is NOT a finding about the design")
    # ⚠ KEYED ON `R1`, NOT ON A STATUS NAME. `W18` renamed the bar's statuses (`RAN` became
    # `RUNS-UNDECLARED` / `RUNS-ALONE-UNDECLARED`), and a filter naming the old ones silently
    # selects nothing — which is exactly what happened to `corpus_run.main` when `W18` landed: the
    # verb counts went to `0 of 32` and an empty set has no obvious tell. The property meant all
    # along is "the run completed", which is `R1`.
    live = [r for r in rows if r.get("checks", {}).get("R1") is True]
    unrep = [r for r in rows if r["status"] == "UNREPRESENTABLE"]

    # `H-95` — the two scale vocabularies, asserted EXACTLY. `faction` is refused by RULING
    # (ARCHITECTURE_V2.md:93, H-21); `world` is unruled. A change to either count is a change to
    # the corpus or to `rung_kinds` and must re-derive the row rather than reuse it.
    from collections import Counter
    census = Counter(r["scale"] for r in unrep)
    # ⚠ THE `faction` COUNT IS DERIVED FROM THE OVERLAYS, NOT PINNED — and the change is `W28`'s
    # doing. The first version asserted `{"faction": 47, "world": 10}` flat, and it FIRED correctly
    # on the first three re-scales: 47 -> 44. Re-pinning it to 44 would buy one commit and go stale
    # on the next overlay, and re-pinning is the uncontrolled path `CLAUDE.md` §7 names. So the
    # invariant is stated as the arithmetic it always was: the corpus holds 47 `faction` cases, an
    # overlay re-scales one each, and every one that remains is unrepresentable. A corpus change or
    # a `rung_kinds` change still fails this; only an overlay may move it, and only by exactly one.
    rescaled_from = Counter(sc["was"] for sc in C.RESCALES.values())
    expected = {"faction": 47 - rescaled_from.get("faction", 0),
                "world": 10 - rescaled_from.get("world", 0)}
    expected = {k: v for k, v in expected.items() if v}
    assert dict(census) == expected, (
        f"the unrepresentable census is {dict(census)}, and {len(C.RESCALES)} overlays re-scale "
        f"{dict(rescaled_from)} out of a corpus of 47 faction / 10 world, which predicts "
        f"{expected}. Either the corpus changed or `rung_kinds` grew — `H-95` must be re-derived")
    assert len(live) == 143 - sum(census.values()) and len(rows) == 143, (
        f"the corpus size moved: {len(live)} runnable of {len(rows)}")
    assert sum(census.values()) + len(live) == 143, "a case is neither runnable nor unrepresentable"

    # ⚠ THE EXECUTION MEASURE IS PART E's OWN COLUMNS, NOT `driver.resolved`. `resolved.append(a)`
    # is the FIRST statement of `_fold`, before eligibility and before the requires predicate, so
    # it counts acts that REACHED the fold. Rev 1 read it and published attempts as executions —
    # `tell` and `transfer` were among its "seven that execute" and both are always REFUSED.
    ever = {v for r in live for v in r["executed"]}
    refused_only = {v for r in live for v in r["refused"]} - ever
    foldable_all = set(S.resolvable_verbs())
    # ⚠ THE CROSS-CHECK THAT CAUGHT A FALSE POSITIVE IN THIS VERY MEASUREMENT, kept as a guard.
    # `corpus_run` first attributed an execution by EMISSION KIND, and `forge` and `create_record`
    # both emit `record.created` (as `confer` and `revoke` both emit `tenure.closed`) — so `forge`
    # was credited with every record `create_record` made, while having no predicate and no effect
    # and being unable to execute at all. A verb that EXECUTED must be a verb the fold CAN execute;
    # anything else is the instrument crediting the design with work it did not do, which is the
    # mis-attribution `G4` forbids. Attribution is now exact, via the fold's own id derivation.
    assert ever <= foldable_all, (
        f"{sorted(ever - foldable_all)} executed while the fold cannot execute them — the "
        "attribution has gone back to matching on emission kind, which two pairs of verbs share")
    # ⚠ 5, NOT 6, AND THE NUMBER WENT DOWN BECAUSE THE OLD ONE WAS WRONG (§0.1 point 4 -- a
    # number without a control is not a measurement in EITHER direction). `move` was counted as
    # executing in every world; the adversarial pass showed `_req_move` could not refuse anybody
    # (it ended `or here.kind == "person"`, true of every person) and `_eff_move` closed every live
    # `contain` while opening none, then returned `[a.actor]` regardless -- so `travel.moved` was
    # published for a state change that did not happen. Measured on NPC-088 at seed 0: live
    # `contain` edges 10 -> 7 in season 1, `Query.presence` empty for every rung thereafter, and
    # three more fabricated `travel.moved` in each of seasons 2 and 3. `move` has no destination to
    # move to -- that is `H-94` in a second verb -- so it now refuses alongside `transfer`, and the
    # honest count is 5.
    assert ever == {"create_record", "speak", "tell", "utter", "work"}, (
        f"the executed set moved to {sorted(ever)} — that is progress or regression and `H-96` "
        "must be re-measured rather than reused")
    # ⚠ `move` JOINED `transfer` HERE, AND IT IS THE SAME HOLE. Both are refused for want of an
    # OPERAND the Candidate cannot carry: `transfer` has no `kind`/`amount`, `move` has no `to`.
    # `Candidate := (verb, subject, why)` and a candidate's `subject` comes from the QUESTION's
    # referents -- a claim's subject or a Proposition -- never a destination rung, so there is no
    # route from the person's decision to a place. `move` used to "execute" by closing every
    # containment and opening none; see the executed-set note above.
    assert refused_only == {"move", "transfer"}, (
        f"the always-refused set moved to {sorted(refused_only)}. `transfer` is the STRUCTURAL "
        "half of `H-94`: `Candidate := (verb, subject, why)` has no operand field, so "
        "`stores(hearth(giver), kind) >= amount` has no `kind` and no `amount` to read. `tell` "
        "was the other half and it is fixed — `pack_scenes` now carries the Candidate's subject "
        "into the payload instead of folding it into the act id and discarding it")

    # `H-96` — the ranking cannot discriminate, which is WHY one executed set survives worlds that
    # genuinely differ. This is the load-bearing assertion; the identical set alone proves nothing.
    assert len({r["seasons"] for r in live}) > 1, (
        "every case ran for the same number of seasons — `temporal.span_seasons` is not being "
        "read, and the worlds are identical again for the reason rev 1 was overturned")
    # ⚠ THE WORLDS DISCRIMINATE NOW, AND EXACTLY ONCE. Two executed sets: the five cases the
    # corpus declares `span_seasons: 1` do not `tell`, because a claim is deposited at WITNESS at
    # the END of a season and a one-season life never holds one to tell. That is the corpus's own
    # data changing the outcome — the first behavioural difference the larger surface produced,
    # and it appeared only once `temporal.span_seasons` was read and the subject stopped being
    # dropped. `H-96` still holds for everything else: 2..7 of 22 candidates separate.
    by_sig = {}
    for r in live:
        by_sig.setdefault(tuple(r["executed"]), []).append(r)
    assert len(by_sig) == 2, (
        f"the number of distinct behaviours moved to {len(by_sig)}; `H-96` must be re-derived")
    small = min(by_sig.values(), key=len)
    assert {r["seasons"] for r in small} == {1} and len(small) == 5, (
        f"the divergent group is no longer the five one-season cases: "
        f"{sorted({r['seasons'] for r in small})}, n={len(small)}. The explanation on `H-96` "
        "(a claim lands at WITNESS, so a one-season life has none to tell) no longer holds")
    assert foldable_all - ever - refused_only == {"confer", "convene", "dispatch", "revoke",
                                              "destroy_record"}, (
        f"the never-attempted set moved to {sorted(foldable_all - ever - refused_only)}. Four of the "
        "five are the governance verbs and `H-71` is why; any movement means `H-71` has moved")




def test_the_seam_calls_personal_combat_rather_than_naming_it():
    """JORDAN, 2026-09-02: *"kill / wound points towards a seam that should be calling in the
    personal combat system."*

    Before this, `contest()` resolved the subsystem by name and then REFUSED — a pointer, not a
    call — on a scope note that ruling overrides. The seam calls now, and these are the properties
    that make the call honest rather than merely present."""
    import combat_seam as C
    w = P.tiny_world(); w.step = S.Step.RESOLVE
    if C.engine() is None:                     # a NAMED gap, never a silent skip
        assert C.load_error(), "the engine is unavailable and the seam reports no reason"
        pytest.skip(f"personal_combat engine unavailable: {C.load_error()}")

    out = S.contest(w, "S", "the body", ["p_low", "p_mid"], 0, 2, ["act1"])
    assert out["status"] == "RESOLVED" and out["module"] == "personal_combat", out
    assert out["resolver"] == "d_sigma", (
        "the seam is not using the resolver `module_contracts.yaml` declares for this prize")

    # ⚠ DETERMINISM, WHICH IS THE WHOLE REASON THE SEED IS DERIVED FROM THE WORLD'S CLOCK.
    # `wrapper.fight`'s own note says to pass `random.Random(seed)`; an unseeded call would make
    # every campaign unreproducible, which `W11` and `test_w9_check1` both rest on.
    again = S.contest(w, "S", "the body", ["p_low", "p_mid"], 0, 2, ["act1"])
    assert again["result"] == out["result"] and again["seed"] == out["seed"], (
        "the same contest in the same world gave a different answer — the seam is not seeded "
        "from the world clock and the instrument is no longer reproducible")

    # ⚠ THE SEAM MINTS NO DEGREE, AND THAT IS `H-98`. `contest()`'s contract reads a band off a
    # MARGIN; the engine returns a WINNER (+1/-1/0). Mapping one onto the other is the second
    # resolver §27.2 forbids, so the outcome is returned as the engine gave it.
    assert "degree" not in out and "band" not in out, (
        f"the seam has started reporting a degree ({ {k: out[k] for k in out if k in ('degree','band')} }) "
        "— it has become the second resolver, which is S27.2's highest-value refusal")
    assert out["result"] in (-1, 0, 1), out["result"]

    # ⚠ `0` IS A RULED OUTCOME. Jordan, 2026-06-02, in the engine: "an undecided fight is a
    # legitimate outcome." A seam that retried it into a decision would overwrite that ruling.
    assert out["unresolved"] == (out["result"] == 0)

    # A party it cannot derive is a GAP, never a fabricated side (`combat_bridge`'s rule).
    gap = C.resolve(w, ["p_low"], ["a"], "the body")
    assert gap["status"] == "PARTY-GAP" and "two parties" in gap["why"], gap


def test_the_combat_seam_derives_one_field_and_it_decides_something():
    """`H-97`. A tracer `Person` carries nothing combat-shaped except `body`, so the seam derives
    EXACTLY ONE `Combatant` field from it and leaves every other at the class's own default —
    `engine/cross_scale/combat_bridge.py`'s discipline, followed rather than reinvented.

    ⚠ AND IT INVENTS NO NUMBER. `body_band_penalty` already owns the body → bands reading (it is
    `H-38`'s closure spent), so the magnitude comes from `band_floors["body"]`, which is
    registered. The injected part is WHICH field the penalty lands on, and that is what `H-97`
    grades.

    ⚠ THE SECOND ASSERTION IS THE ONE THAT MATTERS. A derivation that reaches the engine and
    changes no outcome would be decoration — the `uniform` arm of its own sweep. Condition has to
    move the result, or the seam is passing a constant."""
    import combat_seam as C
    w = P.tiny_world()
    if C.engine() is None:
        pytest.skip(f"personal_combat engine unavailable: {C.load_error()}")
    scale = w.fixtures.get("condition_scale")
    ends = {}
    for body in (scale, 700, 400, 50):
        w.persons["p_low"].body = body
        ends[body] = C.derive_party(w.persons["p_low"], w.fixtures, "x").end
    assert ends[scale] > ends[700] > ends[400] > ends[50] >= 1, (
        f"the derived `end` is not monotone in body condition: {ends}. A dying fighter must not "
        "be as durable as a healthy one, and the floor of 1 is why a dying one still fights")

    def wins(body_a: int) -> int:
        w.persons["p_low"].body = body_a
        w.persons["p_mid"].body = scale
        n = 0
        for t in range(40):
            w.tick = t
            n += C.resolve(w, ["p_low", "p_mid"], ["a"], "the body")["winner"] == "p_low"
        return n
    healthy, dying = wins(scale), wins(50)
    assert healthy > dying, (
        f"condition does not reach the engine: healthy won {healthy}/40 and dying {dying}/40. "
        "The derived field is decoration, and the seam is handing the subsystem a constant")


def test_w18_the_run_instrument_and_its_control():
    """`W18`. `PLAN.md` Part 6's bar, as an instrument. Three clauses, and **the control is first
    because it is the only one that demonstrates sensitivity.**

    ⚠ "THE CONTROL IS THAT THE INSTRUMENT CAN SAY ZERO" IS NOT A CONTROL, and `W18`'s first draft
    said it was. Printing 0 on a corpus where 0 is entailed shows nothing (§0.1 pt 4). The planted
    cross-person edge is the control: it must flip `R3` false → true, and if it ever stops flipping,
    the instrument has gone blind and every zero it prints afterwards is worthless."""
    import corpus_run as C
    import run_cases as R

    # 1 — THE CONTROL.
    before, after = C.planted_control()
    assert before is False and after is True, (
        f"the planted cross-person edge did not flip R3 ({before} -> {after}). The detector is "
        "blind, and every `RUNS = 0` it prints is uninformative rather than true")

    rows = [C.run_case(c, 0, lane) for lane in ("NPC", "ARC") for c in R.load_cases(lane)]
    npc = [r for r in rows if r["id"] in {c["id"] for c in R.load_cases("NPC")}]
    arc = [r for r in rows if r not in npc]

    # 2 — the two counts, and they are zero today.
    assert sum(1 for r in npc if r["status"] == "RUNS") == 0, (
        "an NPC case reaches RUNS — that is PROGRESS and Part 6's count must be re-derived, not "
        "reused. `RUNS` needs `R2`, which `W18` declares NOT-COMPUTABLE, so this firing means "
        "either `W10-core` landed or a status is being scored that should not be")
    assert sum(1 for r in arc if r["status"] == "ENDS") == 0, (
        "an ARC case reaches ENDS — `W30` has landed or `A2` is being scored while NOT-COMPUTABLE")

    # ⚠ AND THE ZEROS MUST NOT BE VACUOUS. Cases have to be REACHING the checks for a zero to mean
    # anything; if nothing completes, `RUNS = 0` says only that the instrument fell over.
    completing = [r for r in rows if r.get("checks", {}).get("R1") is True]
    assert len(completing) >= 80, (
        f"only {len(completing)} cases complete a run; the two zeros are then a report about the "
        "harness, not about the design")
    assert all(r["checks"]["R4"] for r in completing), "a completing case is not reproducible"

    # 3 — NOT-COMPUTABLE is reported, non-empty, and every entry names the item that closes it.
    assert C.NOT_COMPUTABLE, "nothing is declared NOT-COMPUTABLE — R2/A2/A3 are being scored"
    assert set(C.NOT_COMPUTABLE) == {"R2", "A2", "A3"}, sorted(C.NOT_COMPUTABLE)
    for k, why in C.NOT_COMPUTABLE.items():
        assert "W" in why, f"{k} does not name the item that closes it: {why!r}"
    for r in completing:
        assert "R2" not in r["checks"] and "A2" not in r["checks"], (
            f"{r['id']} carries a score for a check declared NOT-COMPUTABLE — a number that cannot "
            "fail is not a measurement, and this is the exact defect the declaration exists to stop")

    # `A1` refuses a prose span rather than defaulting one — 25 ARC cases today.
    assert sum(1 for r in arc if r["status"] == "SPAN-UNAUTHORED") > 0, (
        "no arc is SPAN-UNAUTHORED; prose spans are being silently defaulted, and an arc reported "
        "as running its span would not have run it")


def test_h99_the_office_carries_its_three_canon_axes_and_a_misseating_refuses():
    """`H-99`. Jordan, 2026-09-02: *"does the office schema include faction belonging, scale of
    office, type of office, etc?"* It did not — the office block carried `post`, `remit`, `why`.

    ⚠ THE FALSIFIER IS THE MIS-SEATING, NOT THE HAPPY PATH (§0.1 point 2). Asserting that
    `Cardinal of Justice` derives `Church of Solmund` observes nothing: a schema that ignored the
    body entirely and returned the first faction alphabetically would also have to be caught. So
    every arm below MUTATES the input into the error a hand-authored re-scaling actually makes at
    volume — a real body under the wrong faction — and requires a refusal.

    ⚠ AND THE SOURCE PRECEDENCE IS ASSERTED AS DATA, because it is a RULING and prose cannot hold
    it (§0.05). Jordan, 2026-09-02: *"systems/world ... for the identity/names/organizations it is
    canon"*; *"systems/factions ... near-canon but superseded by anything in world."* The name that
    broke this rule once is `Ministry of the Peninsula`, and it must stay out by DATA."""
    # 1 — the three axes exist and resolve, and SCALE is not among them by design.
    assert S.FACTIONS and S.BODY_FACTION and S.BODY_FUNCTION
    assert S.office_faction("Cardinal of Justice", None) == "Church of Solmund"
    assert S.ROLE_TEMPLATE_OF["Church of Solmund"] == "ecclesiastical"
    assert "Judicial" in S.BODY_FUNCTION["Cardinal of Justice"]
    assert not (set(S.BODY_FACTION) & set(S.RUNG_KINDS)), (
        "a body is being used as a rung; an office's scale is its SEAT, not its organ")

    # 2 — THE MUTATION. Every canonical body, declared under a faction that is not its own,
    #     must refuse. Without this the derivation is decorative.
    checked = 0
    for body, owner in S.BODY_FACTION.items():
        for other in S.FACTIONS:
            if other == owner:
                continue
            with pytest.raises(S.Forbidden):
                S.office_faction(body, other)
            checked += 1
    assert checked >= 16 * 7, f"only {checked} mis-seatings were tried"

    # 3 — the two ways an office can name nothing at all.
    with pytest.raises(S.Unspecified):
        S.office_faction(None, None)
    with pytest.raises(S.Unspecified):
        S.office_faction("Ministry of Silly Walks", None)
    with pytest.raises(S.Unspecified):
        S.office_faction(None, "Niflhel")

    # 4 — THE PRECEDENCE RULING, AS DATA. Three names that a reasonable reader would have
    #     included and canon excludes. Each was in a draft of this roster or in circulation.
    for excluded, why in [
        ("Ministry of the Peninsula", "faction_canon_v30.md:374 — 'institutional infrastructure, "
                                      "not a faction'; absent from all of systems/world/"),
        ("People's Revolution", "the pre-ED-061 name for Restoration Movement"),
        ("Niflhel", "dissolved — worldbuilding_v30.md §3.2, §10"),
    ]:
        assert excluded not in S.FACTIONS, f"{excluded!r} is a member: {why}"
    assert "Restoration Movement" in S.FACTIONS and "Schoenland" in S.FACTIONS

    # 5 — the two factions with no role template RAISE rather than defaulting (§42.2 polarity).
    for f in ("Guilds", "Schoenland"):
        assert f in S.FACTIONS and f not in S.ROLE_TEMPLATE_OF, (
            f"{f} has a role template; §4's player-eligible column does not list it, so one was "
            "invented — the fabrication the precedence ruling exists to stop")

    # 6 — EVERY LOADED OVERLAY RESOLVES, and the loader refuses a mis-seated one.
    import corpus_run as C
    for cid, sc in C.RESCALES.items():
        off = sc.get("office") or {}
        assert S.office_faction(off.get("body"), off.get("faction")) in S.FACTIONS, cid
    with pytest.raises(SystemExit):
        C._check_office("mutant.yaml", {"post": "X", "why": "y",
                                        "body": "Cardinal of Justice", "faction": "Crown"})
    with pytest.raises(SystemExit):
        C._check_office("mutant.yaml", {"post": "X", "why": "y", "faction": "Crown",
                                        "remit": ["annex"]})
    with pytest.raises(SystemExit):
        C._check_office("mutant.yaml", {"post": "X", "faction": "Crown"})


# ---------------------------------------------------------------------------
# `N3` — THE OCCASION EDGE. The falsifier ships with the claim (`ID-11`).
#
# ⚠ WHAT WAS MEASURED BEFORE THIS EXISTED, so the number is re-runnable rather than remembered:
# `R3` — an act by one person caused by an act of another — scored **0 of 30** on the NPC lane and
# **0 of 59** on ARC, while `R1`, `R4` and `R5` passed every case. `PLAN.md`'s `N3` names the
# reason: *60 act-Events, 0 resolving to a question*. Two edges were missing and each hid the
# other, which is why fixing one alone moves nothing:
#   1. an act's Event cited only the act, so nothing said what OCCASIONED the act; and
#   2. a telling writes nothing, so its deposit was minted about THE TELLER — and §F1's Q2 admits
#      a claim about the holder or something they hold, so the news reached the listener in a form
#      their own deliberation could never pick up.
# ---------------------------------------------------------------------------


def test_n3_an_act_cites_what_occasioned_it_and_a_telling_is_about_what_was_told():
    import corpus_run as C
    import run_cases as R
    from collections import Counter

    case = next(c for c in R.load_cases("NPC") if str(c.get("scale")) in set(S.RUNG_KINDS))
    w = C.build_at(case, 0)
    d = S.SeasonDriver(w)
    mint = lambda pid, verb, subj: S.H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = S.make_chooser(w.fixtures, mint, verbs=S.resolvable_verbs())
    for _ in range(3):
        d.season(ch, question=None, subsistence=C.P.SUBSIST)

    # 1 — EVERY ACT THAT CAME THROUGH DELIBERATE NAMES ITS SCENE, and every scene its occasion.
    #     A bare Act built by hand has neither and is not asserted over.
    assert d.resolved, "no acts resolved — the rest of this test would pass vacuously"
    assert all(a.scene for a in d.resolved), "an act came out of DELIBERATE with no scene"
    assert all(sc.occasion is not None for sc in d.scenes.values()), "a scene carries no occasion"

    # 2 — THE WALK RETURNS AN ANTECEDENT FOR A `claim_landed` QUESTION, and the antecedent is a
    #     real Event id in the log. `occasioned_by` is callable without a driver, which is the
    #     property `ID-10` asks for: the check can observe the failure it excludes.
    ids = {e.id for e in w.log}
    landed = [sc.occasion for sc in d.scenes.values()
              if getattr(sc.occasion, "source", None) == "claim_landed"]
    assert landed, "no claim_landed question formed — the transport never reached anybody"
    walked = [x for q in landed for x in S.occasioned_by(w, q)]
    assert walked, "every claim_landed question walked back to nothing"
    assert all(x in ids for x in walked), "the walk returned an id that is not in the log"

    # 3 — `need` RETURNS EMPTY ON PURPOSE, and this asserts the refusal rather than assuming it.
    #     A standing ambition has no antecedent Event; `ID-5`'s polarity forbids inventing one.
    for q in (sc.occasion for sc in d.scenes.values()):
        if getattr(q, "source", None) == "need":
            assert S.occasioned_by(w, q) == [], "a `need` question was given a fabricated cause"

    # 4 — A TELLING'S DEPOSIT IS ABOUT WHAT WAS TOLD, NEVER ABOUT THE TELLER. This is the clause
    #     that makes the listener's Q2 reachable, and the one that was inverted.
    told = [e for e in w.log if e.kind == "news.told"]
    assert told, "no telling executed — clause 4 would pass vacuously"
    checked = 0
    for e in told:
        act = d.act_of.get(e.id)
        refs = S.act_refs(act)
        if not refs:
            continue
        subs = S.claim_subjects(e, w.fixtures.get("claim_subject_rule"), refs)
        assert act.actor not in subs or act.actor in refs, (
            f"a telling deposited a claim about the teller {act.actor!r}: {subs} — §F1's Q2 can "
            "never fire on it for the listener, which is what made `R3` zero")
        assert set(subs) <= set(refs), f"a telling's deposit named something the act did not: {subs}"
        checked += 1
    assert checked >= 1, "no telling carried a referent, so clause 4 asserted nothing"

    # 4a — AND IT CITES NOTHING ELSE. ⚠ THIS IS THE CLAUSE A CRITIC ASKED FOR AND THE FIRST
    #      WRITING OF THIS TEST DID NOT HAVE: every clause above passes just as well against an
    #      `_occasion_ids` that returned EVERY id in the log, and over-citation is exactly what
    #      would inflate `R3` into meaninglessness. An act-emitted Event may cite its own act and
    #      the antecedents of its occasion, and nothing else.
    checked_causes = 0
    for e in w.log:
        act = d.act_of.get(e.id)
        if act is None:
            continue
        sc = d.scenes.get(getattr(act, "scene", None) or "")
        allowed = {act.id} | set(S.occasioned_by(w, getattr(sc, "occasion", None)))
        assert set(e.causes) <= allowed, (
            f"{e.kind} cites {sorted(set(e.causes) - allowed)}, which is neither its act nor an "
            "antecedent of its occasion — causes[] is being padded, and a padded causes[] scores "
            "R3 for free")
        checked_causes += 1
    assert checked_causes >= 1, "no act-emitted Event was checked for over-citation"

    # 5 — AND THE WHOLE POINT: A REAL RUN PRODUCES A CROSS-PERSON CAUSAL EDGE. Not planted — this
    #     is the same `R3` the corpus scores, run over a world built from a corpus case.
    assert C._r3_propagates(w, d), (
        "no act by one person is caused by an act of another — `R3` is back to zero and the "
        "chain Reading 07 §4 calls 'the one that is actually the game' is severed again")

    # 6 — THE CONTROL, so a green clause 5 is not just the detector answering true to anything.
    #     A world with no acts cannot propagate, and the same call must say so.
    w2 = C.build_at(case, 0)
    assert not C._r3_propagates(w2, S.SeasonDriver(w2)), (
        "`_r3_propagates` returned true on a world where nobody has acted — it is not measuring "
        "propagation")


def test_id16_the_sign_column_has_a_reader_and_it_can_fail():
    """`G13` — the gate that makes `sign:` a mechanism rather than a note.

    ⚠ MUTATION-CHECKED, BECAUSE A GATE NOBODY HAS SEEN FAIL IS `ID-10`'s ABSENT CHECK. Three
    plants, one per clause. The clean register must pass, and each mutation must be named."""
    import copy
    import register as R

    reg = R.load()
    assert R.rule_G13(reg) == [], "the committed register does not satisfy its own loop gate"

    loops = [r for r in reg["rows"] if r.get("kind") == R.LOOP_KIND]
    assert loops, "no LOOP row exists, so every clause below would pass vacuously"
    assert all(r.get("sign") in R.LOOP_SIGNS for r in loops)
    assert any(r["sign"] == "+" for r in loops), (
        "every declared loop is damping — which is the state `ID-16` says converges, and if it "
        "is true it should be said, not left to be inferred from a table nobody signed")

    # 1 — a LOOP row with no sign.
    m = copy.deepcopy(reg)
    for r in m["rows"]:
        r.pop("sign", None)
    assert R.rule_G13(m), "a LOOP row with no sign passed"

    # 2 — an AMPLIFYING loop with nothing bounding it. This is the clause with teeth: `F.28` is
    #     the row that says nothing catches a spiral across seasons.
    m2 = copy.deepcopy(reg)
    for r in m2["rows"]:
        if r.get("sign") == "+":
            r["default"] = "none"
    assert R.rule_G13(m2), "an unbounded amplifying loop passed"

    # 3 — the column on a row it does not belong to.
    m3 = copy.deepcopy(reg)
    next(r for r in m3["rows"] if r.get("kind") != R.LOOP_KIND)["sign"] = "-"
    assert R.rule_G13(m3), "a `sign` on a non-LOOP row passed"
