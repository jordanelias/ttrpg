"""IN-19 -- `harness/storybar.py`, the M2 instrument. These tests pin the INSTRUMENT, never its
numbers (the same stance as `test_aperture.py`): what a season's cause graph reads is the
measurement and it moves whenever the game does.

The falsifier the plan names, observed rather than assumed:
  * a planted severed antecedent edge DROPS the cross-person share -- on a real seeded run, against
    an unplanted copy of the same log that must read identically (so the planting path alone moves
    nothing);
  * forcing off, the two arms read EQUAL -- `--arms off off` is the only comparison this tree can
    run, since no forcing source is built, and an unbuilt arm is refused rather than invented.
"""

from __future__ import annotations

import dataclasses
from types import SimpleNamespace as NS

import pytest

from ..harness import storybar as SB

SEED, SEASONS, CAP = 0, 2, 10


@pytest.fixture(scope="module")
def driven():
    return SB.drive(SEED, SEASONS, "off", CAP)


def _copy_log(log, act_of, sever_aid=None, sever_from=None):
    """A copy of the log with fresh Event objects (and `act_of` re-keyed onto them). When
    `sever_aid` is given, every cause of that act's Events that names an Event of act `sever_from`
    is removed -- one severed antecedent edge."""
    events, new_act_of = [], {}
    for e in log:
        a = act_of.get(e.id)
        causes = list(e.causes)
        if sever_aid is not None and a is not None and a.id == sever_aid:
            causes = [c for c in causes
                      if getattr(act_of.get(c), "id", None) != sever_from]
        e2 = dataclasses.replace(e, causes=causes)
        events.append(e2)
        if a is not None:
            new_act_of[e2.id] = a
    return events, new_act_of


def test_a_severed_antecedent_edge_drops_the_cross_person_share(driven):
    w, d, bounds = driven
    base = SB.read(w.log, d.act_of, bounds)
    # one act with exactly one cross-person antecedent act, so severing that edge must reclassify it
    target = next((aid for aid, r in base["acts"].items() if len(r["cross"]) == 1), None)
    assert target is not None, (
        "no act in the run has exactly one cross-person antecedent; the falsifier observed nothing")
    severed_from = base["acts"][target]["cross"][0]

    control_log, control_act_of = _copy_log(w.log, d.act_of)
    control = SB.read(control_log, control_act_of, bounds)
    base_ps = SB.per_season(base["acts"].values(), SEASONS)
    assert SB.per_season(control["acts"].values(), SEASONS) == base_ps, (
        "copying the log moved the reading; the planted arm below would not isolate the edge")

    planted_log, planted_act_of = _copy_log(w.log, d.act_of, target, severed_from)
    planted = SB.read(planted_log, planted_act_of, bounds)
    assert planted["acts"][target]["cls"] != "cross"
    planted_ps = SB.per_season(planted["acts"].values(), SEASONS)

    checked = 0
    season = base["acts"][target]["season"]
    for s in range(SEASONS):
        b_this, b_cum = base_ps[s]
        p_this, p_cum = planted_ps[s]
        if s >= season:
            assert p_cum["cross_share"] < b_cum["cross_share"], (s, b_cum, p_cum)
            assert p_cum["classes"]["cross"] == b_cum["classes"]["cross"] - 1
            checked += 1
        if s == season:
            assert p_this["cross_share"] < b_this["cross_share"], (s, b_this, p_this)
            checked += 1
    assert checked >= 2, f"the drop was asserted {checked} time(s); expected at least 2"


def test_forcing_off_the_two_arms_read_equal():
    res = SB.compare(("off", "off"), [SEED], 1, CAP)
    a, b = res[0]["pooled"], res[1]["pooled"]
    assert a[0][0]["acts"] > 0, "the arms read no acts; their equality would be vacuous"
    assert a == b
    assert res[0]["seeds"] == res[1]["seeds"]


def test_an_unbuilt_forcing_arm_is_refused_not_invented():
    unbuilt = "no-such-forcing-arm"
    assert unbuilt not in SB.ARMS
    with pytest.raises(ValueError):
        SB.drive(SEED, 1, unbuilt, CAP)


def test_depth_runs_along_cross_person_edges_only():
    """A hand-built graph: p1's act -> p2's act -> p3's act is depth 3; p3's own follow-up is
    classed `own` and stays depth 1; an act caused only by an actorless Event is `world`."""
    acts = {k: NS(id=k, actor=p) for k, p in
            (("a1", "p1"), ("a2", "p2"), ("a3", "p3"), ("a4", "p3"), ("a5", "p1"))}
    ev = lambda i, causes: NS(id=i, causes=causes)
    log = [ev("m0", []),                      # an actorless Event (MATTER)
           ev("e1", ["a1"]),
           ev("e2", ["a2", "e1"]),
           ev("e3", ["a3", "e2"]),
           ev("e4", ["a4", "e3"]),
           ev("e5", ["a5", "m0"])]
    act_of = {"e1": acts["a1"], "e2": acts["a2"], "e3": acts["a3"], "e4": acts["a4"],
              "e5": acts["a5"]}
    r = SB.read(log, act_of, [0])["acts"]
    assert {k: (v["cls"], v["depth"]) for k, v in r.items()} == {
        "a1": ("none", 1), "a2": ("cross", 2), "a3": ("cross", 3),
        "a4": ("own", 1), "a5": ("world", 1)}


# -- REM-15: `--draw-seeds`, the chooser's draw varied alone on one built world ------------------
# These assert RELATIONS on a small fixture (the cap-10 cast), never a count from a realm run.

DRAWS = (0, 1, 2, 3)


def _small_world(**sweeps):
    from ..harness.populated import build_realm
    w = build_realm(SEED, CAP)
    for name, value in sweeps.items():
        w.fixtures = w.fixtures.sweep(name, value)
    return w


def test_the_same_draw_seed_twice_reads_identical():
    a = SB.draw_seed_arm(_small_world(), SEASONS, [1])["runs"][1]
    b = SB.draw_seed_arm(_small_world(), SEASONS, [1])["runs"][1]
    assert a["acts"] > 0 and sum(a["chains"].values()) > 0, "the run read no acts; equality is vacuous"
    assert a == b


def test_two_draw_seeds_give_at_least_one_differing_chain_and_the_world_is_untouched():
    base = _small_world()
    res = SB.draw_seed_arm(base, SEASONS, DRAWS)
    assert res["base_hash_before"] == res["base_hash_after"], "the arm mutated the base world"
    assert {r["start_hash"] for r in res["runs"].values()} == {res["base_hash_before"]}, (
        "the deep copies were not the same world at the start")
    runs = [res["runs"][d] for d in DRAWS]
    checked = differing = 0
    for i in range(len(runs)):
        for j in range(i + 1, len(runs)):
            checked += 1
            differing += SB.chain_difference(runs[i]["chains"], runs[j]["chains"]) > 0
    assert checked >= 6
    assert differing >= 1, "no two draw seeds differed at the shipped temperature; the arm varies nothing"


def test_a_chooser_that_ignores_its_draw_gives_no_difference_across_draw_seeds():
    """tau = 0 by fixture short-circuits the sampler to the score order, so the draw is never read;
    `declare_intents`' own draw is inert at `intent_disclosure` 0.0. Any difference left is a leak of
    the draw seed into something it must not reach (an id-keying leak): the plan's STOP-IF."""
    base = _small_world(choice_temperature=0)
    assert base.fixtures.get("intent_disclosure") == 0.0, (
        "the tau = 0 control holds only at intent_disclosure 0.0 (residue 2 of `draw_seed_arm`)")
    res = SB.draw_seed_arm(base, SEASONS, DRAWS)
    runs = [res["runs"][d] for d in DRAWS]
    assert runs[0]["acts"] > 0 and sum(runs[0]["chains"].values()) > 0
    checked = 0
    for r in runs[1:]:
        assert r["acts"] == runs[0]["acts"] and r["depth"] == runs[0]["depth"]
        assert SB.chain_difference(runs[0]["chains"], r["chains"]) == 0
        checked += 1
    assert checked >= 3


def test_the_draw_seed_arm_with_the_worlds_own_seed_is_the_default_run():
    """Plumbing control: `draw_seed=w.world_seed` is what `draw_seed=None` means, so the arm's run
    must read exactly as `drive` does by default."""
    w0 = _small_world()
    ref_w, ref_d, ref_b = SB.drive(SEED, SEASONS, "off", CAP)
    ref = SB.read(ref_w.log, ref_d.act_of, ref_b)
    got = SB.draw_seed_arm(w0, SEASONS, [w0.world_seed])["runs"][w0.world_seed]
    assert got["acts"] == len(ref["acts"]) > 0
    assert got["depth"] == SB.summarise(ref["acts"].values())["depth"]
    assert got["chains"] == SB.chains(ref["acts"], {a.id: a.verb for a in ref_d.act_of.values()})


def test_chains_run_forward_along_cross_person_edges_keyed_on_verbs():
    """Planted: a1 (talk) -> a2 (give) -> a3 (give) is one chain from a1; a1 -> a4 (talk) is shorter and
    loses; a5 is a first act with no consequent."""
    row = lambda cross, depth, cls: {"cross": cross, "depth": depth, "cls": cls}
    acts = {"a1": row([], 1, "none"), "a2": row(["a1"], 2, "cross"), "a3": row(["a2"], 3, "cross"),
            "a4": row(["a1"], 2, "cross"), "a5": row([], 1, "world")}
    verbs = {"a1": "talk", "a2": "give", "a3": "give", "a4": "talk", "a5": "move"}
    assert SB.chains(acts, verbs) == {("talk", "give", "give"): 1, ("move",): 1}


# -- CR-15: the executed reading, beside the current one -------------------------------------------
# These assert RELATIONS on a planted log and on the cap-10 fixture, never a count from a realm run.

def _planted_refused_edge():
    """p1's `a1` is REFUSED; p2's `a2` answers it (its only cross-person antecedent). p3's `a3` is
    executed and p4's `a4` answers it (a cross antecedent that stays)."""
    acts = {k: NS(id=k, actor=p) for k, p in (("a1", "p1"), ("a2", "p2"), ("a3", "p3"), ("a4", "p4"))}
    ev = lambda i, causes: NS(id=i, causes=causes)
    log = [ev("e1", ["a1"]), ev("e2", ["a2", "e1"]), ev("e3", ["a3"]), ev("e4", ["a4", "e3"])]
    act_of = {e.id: acts[e.causes[0]] for e in log}
    return log, act_of


def test_a_planted_act_whose_only_cross_antecedent_is_refused_reads_cross_by_default_and_not_executed():
    log, act_of = _planted_refused_edge()
    default = SB.read(log, act_of, [0])
    assert "executed" not in default, "the default return gained a key"
    assert default["acts"]["a2"]["cls"] == "cross" and default["acts"]["a2"]["depth"] == 2

    res = SB.read(log, act_of, [0], {"a1"})
    assert res["acts"] == default["acts"] and res["unread"] == default["unread"]   # beside, never instead
    ex = res["executed"]
    assert ex["a2"]["cross"] == [] and ex["a2"]["depth"] == 1, ex["a2"]   # not cross-person once a1 is cut
    assert "a1" not in ex                                   # a refused act is not an executed act
    assert ex["a4"]["cross"] == ["a3"] and ex["a4"]["depth"] == 2   # an executed edge is kept: the cut is not a wipe

    items = SB.executed_items(res["acts"], ex, {"a1"}, frozenset())
    summary = SB.executed_summary(items)
    assert (summary["executed"], summary["with_cross"], summary["refused"]) == (3, 1, 1)
    assert summary["cross"] == 2 and summary["refused_deep"] == 0       # default: a2 and a4 read cross
    # the mutation's control: with nothing refused the planted act reads cross-person in BOTH readings
    none = SB.read(log, act_of, [0], frozenset())["executed"]
    assert none["a2"]["cross"] == ["a1"] and none["a2"]["depth"] == 2


def test_a_refused_antecedent_is_cut_not_bridged_over():
    """a1 -> a2 (refused) -> a3: a3 answers a2 only, so a3 stands at depth 1 whatever lay behind a2."""
    acts = {k: NS(id=k, actor=p) for k, p in (("a1", "p1"), ("a2", "p2"), ("a3", "p3"))}
    ev = lambda i, causes: NS(id=i, causes=causes)
    log = [ev("e1", ["a1"]), ev("e2", ["a2", "e1"]), ev("e3", ["a3", "e2"])]
    act_of = {e.id: acts[e.causes[0]] for e in log}
    res = SB.read(log, act_of, [0], {"a2"})
    assert res["acts"]["a3"]["depth"] == 3
    assert res["executed"]["a3"]["depth"] == 1 and res["executed"]["a3"]["cross"] == []


def test_the_executed_reading_over_a_real_run_is_a_cut_of_the_default_and_the_default_is_untouched(driven):
    w, d, bounds = driven
    default = SB.read(w.log, d.act_of, bounds)
    refused, graded = SB.refusal_sets(w, len(bounds))
    assert graded <= refused, "a graded loss that is not refused"
    rows = default["acts"]
    assert refused & set(rows), "the run refused no act; the cut below observed nothing"
    before = w.content_hash()
    res = SB.read(w.log, d.act_of, bounds, refused)
    assert w.content_hash() == before
    assert res["acts"] == default["acts"]                  # the default keys are the default's, untouched
    ex = res["executed"]
    assert set(ex) == set(rows) - refused
    checked = 0
    for aid, r in ex.items():
        assert r["cross"] == [b for b in rows[aid]["cross"] if b not in refused]
        assert set(r["cross"]) <= set(ex)
        assert r["depth"] <= rows[aid]["depth"]
        checked += 1
    assert checked >= 1
    # with nothing refused the executed reading IS the default's cross and depth
    same = SB.read(w.log, d.act_of, bounds, frozenset())["executed"]
    assert {a: (r["cross"], r["depth"]) for a, r in same.items()} == {
        a: (r["cross"], r["depth"]) for a, r in rows.items()}


def test_the_executed_only_cli_prints_its_lines_beside_the_current_ones_and_the_arms_still_read_equal(capsys):
    args = ["--base-seed", str(SEED), "--n", "1", "--seasons", "1", "--arms", "off", "off", "--cap", str(CAP)]
    assert SB.main(args) == 0
    plain = capsys.readouterr().out
    assert SB.main(args + ["--executed-only"]) == 0
    both = capsys.readouterr().out
    kept = [l for l in both.splitlines() if "executed" not in l]
    assert kept == plain.splitlines(), "the current lines changed under --executed-only"
    execd = [l for l in both.splitlines() if "executed" in l]
    assert len(execd) >= 3, "no executed line was printed"
    assert any("executed seed=" in l and "total:" in l for l in execd)
    assert "arms off vs off: EQUAL" in both
