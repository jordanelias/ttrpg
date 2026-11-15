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

from ..harness import probes as P
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


def test_a_repeated_draw_seed_is_refused_before_any_world_is_built():
    """`draw_seed_arm` keys its runs by draw seed, so `--draw-seeds 1 1` would run one copy and print one:
    the CLI refuses it by name instead (no realm is built first, so the refusal is immediate)."""
    import pytest
    with pytest.raises(SystemExit) as e:
        SB.main(["--base-seed", str(SEED), "--seasons", "1", "--draw-seeds", "1", "1"])
    assert e.value.code == 2


# -- B02.14: the removal test, beside the draw-seed arm ----------------------------------------------
# These assert RELATIONS on the cap-10 fixture, never a count from a realm run.

WHEN = (0, 0)


def test_removal_replay_arm_reads_zero():
    """Nobody removed: two independent copies of one built world read the same acts (the wrapper
    perturbs nothing), the world the arm ran on is unmutated, and the stamping wrapper reproduces the
    unwrapped run's hash (the control: `wrap_chooser=None` is today's run)."""
    base = _small_world()
    before = base.content_hash()
    first = SB.removal_arm(base, SEASONS, None, WHEN)
    again = SB.removal_arm(base, SEASONS, None, WHEN)
    assert sum(first.values()) > 0, "the arm read no acts; a zero difference would be vacuous"
    assert SB.chain_difference(first, again) == 0
    assert base.content_hash() == before, "the arm mutated the base world"
    plain = SB.drive(SEED, SEASONS, "off", CAP)[0].content_hash()
    stamping = SB._removing(None, WHEN, {}, [])
    wrapped = SB.drive(SEED, SEASONS, "off", CAP, wrap_chooser=stamping)[0].content_hash()
    assert wrapped == plain
    assert SB.drive(SEED, SEASONS, "off", CAP, wrap_chooser=lambda ch: ch)[0].content_hash() == plain


def test_removing_a_person_at_the_first_lap_fires_and_leaves_that_person_out_of_the_reading():
    """The removal can be observed: the wrapper fires once for the person removed, and that person's acts
    are not in the multiset of the OTHERS (the control: the same person's acts ARE in the unperturbed
    copy's, so the exclusion is the arm's doing)."""
    base = _small_world()
    everyone, _f, _h = SB._removal_run(base, SEASONS, None, WHEN)
    acting = sorted({k[0] for k in everyone if k[1:3] == WHEN})
    assert acting, "nobody acted at the first lap; the removal below observed nothing"
    who = acting[0]
    assert any(k[0] == who for k in everyone)
    got, fired, _h = SB._removal_run(base, SEASONS, who, WHEN)
    assert fired == 1
    assert not any(k[0] == who and k[1:3] == WHEN for k in got), "the removed choice still acted"
    assert not any(k[0] == who for k in SB.removal_arm(base, SEASONS, who, WHEN))


def test_the_remove_cli_prints_a_replay_of_zero_and_refuses_an_unknown_person(capsys):
    args = ["--base-seed", str(SEED), "--seasons", "1", "--cap", str(CAP)]
    who = sorted(_small_world().persons)[0]
    assert SB.main(args + ["--remove", who]) == 0
    out = capsys.readouterr().out
    replay = next(l for l in out.splitlines() if l.startswith("[replay]"))
    assert "differing=0 " in replay and "(EQUAL to the unperturbed)" in replay
    assert "(unmutated)" in out
    control = next(l for l in out.splitlines() if l.startswith("[control: drive with no wrapper]"))
    assert "(EQUAL to the unperturbed;" in control
    with pytest.raises(SystemExit) as e:
        SB.main(args + ["--remove", "no_such_person"])
    assert e.value.code == 2


# -- B02.19: the removal test states what it expects, and whom it removes ---------------------------

def test_removal_changes_another_persons_later_act():
    """Seed 0, two seasons, the most-cited person removed at the first lap: others' acts differ (`n`),
    some of them at a later (season, lap) (`m`), the replay arm reads 0 (the control: were it above 0
    every figure would be void), and the removed person's own acts are not in `n`. The second control is
    a person removed at a lap in which the unperturbed copy shows him forming no scene: `n` reads 0."""
    base = _small_world()
    who, cited = SB.most_cited(base)
    assert who is not None and cited >= 1, "nobody is cited by another person; the removal observed nothing"
    res = SB.removal_report(base, SEASONS, who, WHEN, None)
    v = SB.removal_verdict(res, WHEN)
    assert v["replay"] == 0, "the replay arm moved: every figure below is void"
    assert res["unwrapped_hash"] == res["unperturbed"][1]
    assert res["arms"]["removed"]["fired"] == 1
    assert v["n"] >= 1 and v["m"] >= 1, v

    # `n` recomputed by hand over the two multisets, the removed person's keys left out; the same
    # difference with his keys left IN is larger (his own lap-0 acts are gone), so the exclusion is read
    everyone, _f, _h = SB._removal_run(base, SEASONS, None, WHEN)
    got, _f, _h = SB._removal_run(base, SEASONS, who, WHEN)
    diff = {k: abs(everyone.get(k, 0) - got.get(k, 0)) for k in set(everyone) | set(got)}
    assert v["n"] == sum(n for k, n in diff.items() if k[0] != who)
    assert sum(diff.values()) > v["n"], "the removed person's own acts did not differ; nothing was excluded"

    # control 2: a person who forms no scene at a lap, removed there, changes nothing
    laps = sorted({k[1:3] for k in everyone})
    quiet = next(((p, at) for at in laps for p in sorted({k[0] for k in everyone})
                  if not any(k[0] == p and k[1:3] == at for k in everyone)
                  and any(k[0] == p and k[1:3] > at for k in everyone)), None)
    assert quiet is not None, "every person acts at every lap; the quiet control observed nothing"
    p, at = quiet
    reference = SB._others(everyone, p)
    assert SB._removal_run(base, SEASONS, p, at)[1] == 1, "the quiet person's removal did not fire: the zero below would be a replay's"
    assert SB.chain_difference(reference, SB.removal_arm(base, SEASONS, p, at)) == 0


def test_the_most_cited_person_is_the_most_cited_with_ties_by_person_id():
    """Planted: p1's acts are cited by two acts of other persons, p2's by two, p3's by one; p3's own
    follow-up (no cross-person antecedent) counts for nobody. The tie between p1 and p2 goes to p1."""
    row = lambda actor, cross: {"actor": actor, "cross": cross}
    acts = {"a1": row("p1", []), "a2": row("p2", []), "a3": row("p3", []),
            "b1": row("p2", ["a1"]), "b2": row("p3", ["a1", "a2"]), "b3": row("p1", ["a2"]),
            "b4": row("p1", ["a3"]), "b5": row("p3", [])}
    counts = SB.citation_counts(acts)
    assert counts == {"p1": 2, "p2": 2, "p3": 1}
    assert min(counts, key=lambda p: (-counts[p], p)) == "p1"


def test_the_remove_cli_with_no_name_prints_the_name_and_a_verdict_pair_per_seed(capsys):
    args = ["--base-seed", "0", "1", "--seasons", "1", "--cap", str(CAP), "--remove"]
    assert SB.main(args) == 0
    lines = capsys.readouterr().out.splitlines()
    named = [l for l in lines if l.startswith("storybar --remove names ")]
    r01 = [l for l in lines if l.startswith("R-01.c  others' acts differing: ")]
    r02 = [l for l in lines if l.startswith("R-02.b  differing at a later (season, round): ")]
    assert len(named) == len(r01) == len(r02) == 2, (named, r01, r02)
    assert all(l.endswith("(replay 0)") for l in r01), r01
    with pytest.raises(SystemExit) as e:
        SB.main(["--base-seed", "0", "1", "--seasons", "1", "--n", "1", "--arms", "off", "off"])
    assert e.value.code == 2


# -- B02.20: the count of scenes that wrote nothing --------------------------------------------------
# A planted act on a real, witnessed season; relations, never a count from a realm run.

def _uttered(subject):
    """`tiny_world`, one season in which `p_low` utters about `subject`, the witness step run as a season
    runs it. Returns `(w, act)`: the one act of the store."""
    w = P.tiny_world()

    def choose(p, v, s, ask_budget):
        return [P.Act_(w, p, "utter", payload={"subject": subject})] if p.id == "p_low" else []
    P._run_d(w, P.once(choose), contest_max_depth=w.fixtures.get("contest_max_depth"))
    (act,) = list(w.acts)
    return w, act


def _leave_only(w, act, holders):
    """Empty the Receipts of every Event naming `act`, and of every claim deposit those Events caused except
    the ones into a ledger of `holders`. Returns how many deposits were left standing (the plant's size)."""
    held = {c.id: pid for pid, p in w.persons.items() for c in p.ledger}
    own = {e.id for e in w.log if act.id in e.causes}
    kept = 0
    for e in w.log:
        if e.id in own:
            e.changes = []
        elif e.kind == "claim.deposited" and any(c in own for c in e.causes):
            if held.get(e.changes[0].subject) in holders:
                kept += 1
            else:
                e.changes = []
    return kept


def test_null_scenes_sees_a_planted_act_that_writes_nothing(monkeypatch):
    """IS-A-07. The act as the season left it wrote (its Proposition, and claims in the ledgers of those who
    saw it): not null. The same act with every Receipt of its Events removed, and with the deposits of its
    own actor's and counterparty's ledgers removed, is null, class `made`. A deposit into a BYSTANDER's
    ledger alone does not save it; the same deposit into the actor's ledger, or into the counterparty's,
    does (the definition's clause). The control for that clause is the definition it replaced, any claim
    counts, which reads the bystander case as written.

    MUTATION (run 2026-11-15, reverted): `_seat_holders` made to answer every person, so that any claim
    counts -- the bystander arm reads 0 and this test reds."""
    w, act = _uttered("p_high")
    assert (r := SB.null_scenes(w, 1))["total"] == 1 and not r["null"], r      # it wrote: not null
    for holders, null in ((set(), True), ({"p_mid", "p_other"}, True), ({"p_low"}, False)):
        w, act = _uttered("p_high")
        kept = _leave_only(w, act, holders)
        assert (kept >= 1) == bool(holders), f"the plant left {kept} deposits for {holders}"
        got = SB.null_scenes(w, 1)
        assert got["total"] == 1
        assert got["null"] == ({("utter", "made"): 1} if null else {}), (holders, got)
    # the counterparty of the act, `p_mid`: his deposit saves it, a bystander's does not
    for holders, null in (({"p_mid"}, False), ({"p_other"}, True)):
        w, act = _uttered("p_mid")
        assert _leave_only(w, act, holders) >= 1
        assert bool(SB.null_scenes(w, 1)["null"]) is null, holders
    # the control: where any claim counts, the bystander arm is not null
    w, act = _uttered("p_high")
    _leave_only(w, act, {"p_mid", "p_other"})
    assert SB.null_scenes(w, 1)["null"], "the bystander arm is not null before the control"
    monkeypatch.setattr(SB, "_seat_holders", lambda w_, subject: frozenset(w_.persons))
    assert not SB.null_scenes(w, 1)["null"]
    # the scope narrows which acts are counted and nothing else
    assert SB.null_scenes(w, 1, scope=lambda attempt: False) == {"total": 0, "null": SB.Counter()}


def test_null_scenes_per_season_reads_the_whole_run_cut_by_the_acts_each_season_took():
    """`null_by_season`'s seasons add to its whole run (total and null, by verb and class) on the cap-10
    fixture, and the line prints the largest count first."""
    per, whole = SB.null_by_season(SEED, SEASONS, CAP)
    assert len(per) == SEASONS and whole["total"] >= 1
    assert sum(r["total"] for r in per) == whole["total"]
    assert sum((r["null"] for r in per), SB.Counter()) == whole["null"]
    assert SB.pool_null([whole, whole]) == {"total": 2 * whole["total"],
                                            "null": whole["null"] + whole["null"]}
    line = SB.null_line({"total": 9, "null": SB.Counter({("a", "made"): 1, ("b", "refused"): 3})})
    assert line == "null_scenes total=9 null=4 | b/refused=3, a/made=1"
    assert SB.null_line({"total": 2, "null": SB.Counter()}) == "null_scenes total=2 null=0 | none"
