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
    w.write("condition", WriteClass.MATTER, lambda: setattr(site, "condition", before - 7),
            record_kind="Site", fieldname="condition", driver="Event")
    assert site.condition == before - 7


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
    the only bridge from world truth into choose()."""
    w = _w()
    with pytest.raises(Unspecified):
        _ = S.sense(w.persons["p_low"], w, P.SUBSIST).standing


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
    """S20/S34: eviction ranks on confidence_live x recency ONLY. A tuple sort is a different
    comparator and degenerates to insertion order under a constant confidence."""
    src = inspect.getsource(S.SeasonDriver.witness)
    assert "c.confidence * (c.when" in src and "(c.confidence, c.when)" not in src


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
        S.SeasonDriver(_w()).deliberate(lambda p, v, s, ask_budget: [], "q", P.SUBSIST)


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
    with pytest.raises(Unspecified):
        _ = sn.standing
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
                record_kind="Tenure", fieldname="until", driver="Event")
    w.write("Tenure", WriteClass.MATTER, lambda: setattr(t, "until", 0),
            record_kind="Tenure", fieldname="until", driver="Event",
            caused_person_exists="p_high")
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


def test_the_router_guards_the_known_substring_traps():
    """The in-chain run's two most expensive corrections were a bare `ambient` (8 arcs -> 3)
    and a bare `counter` matching inside 'counter-productive' (10 -> 8). This instrument
    reproduced the class a THIRD time with a bare `standing` (18 core rows) before it was
    guarded. The class recurs; the guard is what stops it."""
    assert R.route("a counter-productive policy must be able to be reversed") != "A3"
    assert R.route("an ambient environmental quantity must be able to worsen") != "W3"
    assert R.route("a standing armed institution must be able to reassess its loyalty") != "P14"
    assert R.route("a person with no tracked standing must still be able to act") != "P14"


def test_unmapped_rows_are_never_silently_passed():
    src = inspect.getsource(R.grade)
    assert "unmapped" in src and "NOT-ASSESSED" in src


def test_an_unclear_row_is_not_counted_as_an_unrouted_one():
    """An `UNCLEAR:` row is the CASE SOURCE failing, not the shape failing."""
    assert "unclear" in inspect.getsource(R.grade)


def test_a_case_more_than_half_unrouted_on_core_is_not_assessed():
    got = R.grade({"id": "T", "season_requires": [
        {"need": "zzzz qqqq wwww", "hardness": "core"},
        {"need": "yyyy pppp vvvv", "hardness": "core"},
        {"need": "a person with no office must be able to act", "hardness": "core"},
    ]})
    assert got["verdict"] == "NOT-ASSESSED"


def test_playable_requires_that_every_core_row_was_actually_aimed_at():
    """A case with ANY unmapped `core` row may not be graded PLAYABLE. Five of the twelve
    PLAYABLE verdicts in the first run rested on one or two routed core rows with other core
    rows sitting unmapped beside them -- one reached PLAYABLE on a SINGLE distinct probe with
    three rows unrouted. That is the instrument certifying a season it never aimed at."""
    got = R.grade({"id": "T", "season_requires": [
        {"need": "a person with no office must be able to act", "hardness": "core"},
        {"need": "zzzz qqqq wwww vvvv", "hardness": "core"},
    ]})
    assert got["verdict"] == "NOT-ASSESSED", got["verdict"]


def test_a_blocker_outranks_an_unaimed_row():
    """A core row that DID route and DID hit a gap is a fact about the SHAPE; a core row that
    failed to route is a fact about the AIM. The first outranks the second."""
    got = R.grade({"id": "T", "season_requires": [
        {"need": "a settlement unrest level must be able to rise and fall", "hardness": "core"},
        {"need": "zzzz qqqq wwww vvvv", "hardness": "core"},
    ]})
    assert got["verdict"] == "BLOCKED", got["verdict"]


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
    w = _w()
    d = S.SeasonDriver(w)
    site = w.sites["site_harbour"]
    for _ in range(3):
        d.season(P.NOCHOOSE, "q", P.SUBSIST)
    assert not [c for c in w.crossings if c[0] == site.id], "no band was crossed yet"
    for _ in range(20):
        d.season(P.NOCHOOSE, "q", P.SUBSIST)
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
    r = d.season(choose, "q", P.SUBSIST)
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
    S.SeasonDriver(w).season(choose, "q", P.SUBSIST)
    assert asked, "no person was asked for a budget at all"
    # ⚠ W5 REPOINTED THIS ASSERTION, AND THE OLD ONE WAS THE DEFECT. It read
    # `all(n == w.fixtures.get("act_budget") for n in asked)` — i.e. it PINNED A FLAT BUDGET,
    # which is the field S26.3 forbids, as an invariant. `budget` reading its own arguments is
    # what broke it, and a test that goes red when the specification is finally met was testing
    # the implementation. C11's claim is that the person is ASKED; that is what stays.
    base = w.fixtures.get("act_budget")
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
    k = fx.get("act_budget")
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


def test_r3_no_bare_token_route_is_decisive():
    """DEFECT C3 — the class has now recurred FOUR times in this chain: `ambient` (8 arcs -> 3),
    `counter` inside 'counter-productive' (10 -> 8), adjectival `standing` (18 core rows), and
    `standing condition` escaping the whitelist built for the third. A whitelist was the wrong
    shape; these are the specific escapes, pinned."""
    checks = [
        ("a persistent, standing condition of being rich but politically powerless", "P14"),
        ("a compound set of prerequisites must be assembled", "A15"),
        ("must produce a different and better outcome for the world", "W5"),
        ("the cause of the sea-route blockage must be discoverable", "P8"),
        ("an emergency power applying everywhere in the territory", "F5"),
        ("a hidden personal quantity must accumulate at a fixed increment per use", "P5"),
        ("which of several competing internal loyalties is appealed to", "F7"),
        ("independent fieldwork must be able to investigate the claim", "F12"),
    ]
    bad = [(txt, got) for txt, banned in checks
           if (got := R.route(txt)) == banned]
    assert not bad, f"bare-token routes still decisive: {bad}"


def test_r3_a_working_mechanism_is_not_reported_as_a_blocker():
    """DEFECT C10. A1 provokes `causes=[]` to demonstrate the refusal; routing provenance rows
    to it graded them BLOCKED — reporting the design's causes[] rule as the thing that blocks
    causal reconstruction. A2 is the probe that DEMONSTRATES provenance, and it passes."""
    assert R.route("the story must be able to be reconstructed from what caused what") == "A2"
    assert R.route("an accumulated change must be attributable back to which actor caused it") == "A2"
    assert R.run_probe("A2")["verdict"] == "PASS"


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


def test_r4_no_route_is_decisive_on_a_single_common_word():
    """THE STRUCTURAL ANSWER TO A CLASS THAT HAS RECURRED FIVE TIMES.

    `ambient` (8 arcs -> 3) · `counter` inside "counter-productive" (10 -> 8) · adjectival
    `standing` (18 core rows) · `standing condition` escaping the whitelist built for the third ·
    and `age\\w*` matching AGENT/AGENTS/AGENCY/AGENDA, which produced the arc corpus's ONLY
    PLAYABLE verdict on rows about "two AGENTS belonging to rival powers".

    Four of the five were caught one at a time, by a reader, AFTER the verdict was published. A
    whitelist of guarded tokens cannot work -- the fourth recurrence IS that whitelist failing,
    and the fifth was not on it. This forbids the SHAPE instead: no route may be claimable by one
    ordinary English word in a neutral carrier."""
    import route_precision
    offenders = route_precision.audit()
    assert not offenders, (
        "routes decisive on a single common word: " +
        "; ".join(f"{pid} fires on {w!r}" for pid, w, _ in offenders))


def test_r4_every_probe_is_reachable_or_declared_unroutable():
    """S44.4's in-chain ruling names "ELEVEN UNREACHABLE PROBES and a 46% miss rate" as the
    symptom of a router reconstructing what the author knew. A probe no route reaches is either
    a coverage hole or an instrument self-check -- and an UNDECLARED self-check is
    indistinguishable from the hole."""
    import route_precision
    un = route_precision.unreachable()
    assert not un, f"probes no route reaches and no declaration covers: {un}"


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
    assert c["rows"] == c["transcribed"] + c["added_by_plan"], (
        f"{c['rows']} rows but {c['transcribed']} + {c['added_by_plan']} accounted for -- a row "
        "whose `source:` claims neither provenance has appeared")
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
    FOLD_SITE = "_apply_write"
    fold_lines = {n for n, ln in enumerate((HERE / "shape.py").read_text().splitlines(), 1)
                  if FOLD_SITE in ln}
    unexplained = [d for d in dynamic
                   if not any(abs(int(d.split(":")[1]) - fl) < 25 for fl in fold_lines)]
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
EXEMPT_CEILING = 13


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
    CORPUS = ("probes.py", "report.py", "run_cases.py")
    FILES = (MODEL,) + CORPUS
    known = {frozenset(r["values"]) for r in S._ROSTERS.values()}
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
    RC = R

    # ---- the plant. A probe body that calls the instrument wrong must NOT read as a GAP. ----
    spec = dict(title="planted", section="S15.1", by="probe-model", tests="the plant")
    def called_wrong():
        w = _w()
        w.tenures.append(S.Tenure("t_plant", "p_mid", "off_x", "hold", since=0))
    planted = RC._verdict_for("PLANT", spec, called_wrong) if hasattr(RC, "_verdict_for") else None
    if planted is None:                       # the runner's entry point is private; do it directly
        try:
            called_wrong()
            planted = {"verdict": "PASS"}
        except S.ShapeGap as g:
            planted = {"verdict": "GAP", "kind": g.kind}
        except Exception as e:                                            # noqa: BLE001
            planted = {"verdict": "INSTRUMENT-ERROR", "detail": f"{type(e).__name__}: {e}"}
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
