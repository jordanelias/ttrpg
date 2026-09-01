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
import re
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
    stated = [k for k in S.PARTITION if k[0] != "*matrix*"]
    assert stated == [("Tenure", "until")], stated
    for kind, fname in (("Person", "convictions"), ("Person", "beliefs"), ("Person", "scar")):
        with pytest.raises(Unspecified):
            S.partition_lookup(kind, fname, "stance")


def test_d1b_a_field_cannot_ride_on_another_fields_matrix_row():
    """DEFECT 1, second form. The matrix names THINGS, not (kind, field) pairs. Keying the
    derivation on `thing` lets `(Person, convictions)` ride on `stance`'s row."""
    w = _w()
    w.step = Step.RESOLVE
    with pytest.raises(Unspecified):
        w.write("stance", WriteClass.ACTS, lambda: None,
                record_kind="Person", fieldname="convictions", driver="Act")


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
    def over(p, v, s, b):
        return [P.Act_(w, p, f"v{i}") for i in range(b + 2)] if p.id == "p_low" else []
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
    with pytest.raises(Unspecified):
        S.sense(_w().persons["p_low"], _w())


def test_d8_one_doctrinal_condition_raises_one_kind():
    """DEFECT 8. An unmarked cell is ONE condition (S30/S30.1); rev 1 split it across
    Forbidden and Unspecified, making the kind histogram a measurement of the transcription."""
    w = _w()
    w.step = Step.RESOLVE
    with pytest.raises(Unspecified):
        w.write("a_thing_with_no_row", WriteClass.ACTS, lambda: None,
                record_kind="Rung", fieldname="stores", driver="Act")
    with pytest.raises(Unspecified):
        S.partition_lookup("Record", "anything", "condition")


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
    def fight(p, v, s, b):
        return [P.Act_(w, p, "fight", contests=["x"], payload="S")] if p.id == "p_low" else []
    with pytest.raises(Forbidden):
        P._run(w, fight)


def test_d9d_the_frozen_world_is_read_not_merely_written():
    """S32 rest 1 is the FIRST thing order-independence rests on. Rev 1 set w.frozen and
    nothing ever read it."""
    with pytest.raises(Forbidden):
        S.SeasonDriver(_w()).deliberate(lambda p, v, s, b: [], "q", P.SUBSIST)


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
    assert "choose(p, v, s, b)" in src and "choose(w" not in src


def test_a_view_raises_on_any_world_collection():
    v = View("p", [], 5)
    for attr in ("persons", "rungs", "sites", "log", "tenures", "anything_at_all"):
        with pytest.raises(Forbidden):
            getattr(v, attr)


def test_a_view_is_capped_at_k():
    with pytest.raises(Forbidden):
        View("p", ["a", "b", "c"], 2)


def test_sensation_is_exactly_two_scalars():
    assert S.Sensation.__slots__ == ("subsistence", "standing")
    with pytest.raises(AttributeError):
        S.Sensation(1, 2).third = 3


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
    w.tenures.append(Tenure("t_end", "Ghost", "S", "contain", since=0, until=0))
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
    w.tenures.append(Tenure("t_dup", "p_mid", "off_duke", "hold", since=0))
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


def test_the_corpus_defects_are_reported_not_hidden():
    """Six of the in-chain corpus's seven case files are committed inside a markdown fence
    with a transcript preamble, and one is TRUNCATED AT ITS HEAD. The instrument works around
    them at LOAD time and SAYS SO -- it does not edit the chain's evidence."""
    R.CORPUS_DEFECTS.clear()
    R.load_cases("ARC")
    assert R.CORPUS_DEFECTS and any("TRUNCATED" in d for d in R.CORPUS_DEFECTS)
