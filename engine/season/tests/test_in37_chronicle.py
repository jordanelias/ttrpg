"""IN-37 -- `harness/chronicle.py`, a chronicle render OUTSIDE the simulation. These tests pin the
OBSERVER's contract, never a run's numbers (those move whenever the game does).

The falsifier the plan names -- *the render writes to `World`, or a carrier for arcs appears inside
the simulation* -- observed rather than assumed:
  * the World's content hash, log length and write list are identical before and after a render;
  * the module's AST imports no write-token constructor and calls no `write`/`add_tenure`/
    `mint_token` -- and the same checker is run over a planted source that DOES, to show it can fail;
  * a real seeded render names >= 2 distinct actors and each non-first line cites an antecedent that
    is an earlier line AND a real cross-person antecedent in the cause graph;
  * a hand-made log with a known 3-act cross-person chain, a shallower decoy logged FIRST and an
    equal-depth rival logged LATER renders the chain, in causal order, first-logged on the tie.

CR-68 (the default pick is over CONSEQUENCE ACTS, `arc.consequence_acts`; `--all-acts` is the old pick):
  * a planted depth-3 chain of acts that wrote outranks a planted depth-5 chain of acts that wrote nothing,
    through `chronicle.main`; the same predicate returning every act (the mutation) puts the depth-5 chain
    back, so the check can fail;
  * a planted graded loss that writes is a consequence act and a planted refusal that writes nothing is not;
  * an act that wrote nothing in the middle of a chain is cut, its edges with it, and depth is recomputed;
  * `--all-acts` over the same plant reproduces the old default (body lines and the header's old fields);
  * the no-write test calls the consequence reader and the cut as well as the render.
"""

from __future__ import annotations

import ast
import re
from pathlib import Path
from types import SimpleNamespace as NS

import pytest

from ..harness import arc as ARC
from ..harness import chronicle as CH
from ..harness import storybar as SB
from ..state.carriers import Receipt

SEED, SEASONS, CAP = 0, 2, 10


@pytest.fixture(scope="module")
def driven():
    return SB.drive(SEED, SEASONS, "off", CAP)


# ---- (1) the render writes nothing to the World --------------------------------------------------

def test_the_render_changes_nothing_in_the_world(driven):
    """The render AND its selection (CR-68: `arc.consequence_acts`, the cut handed to `storybar.read`, the
    pick over the cut rows) change nothing: content hash, log length and write list are equal after."""
    w, d, bounds = driven
    before = (w.content_hash(), len(w.log), list(w.writes))
    res = SB.read(w.log, d.act_of, bounds)
    text = CH.render(w.log, d.act_of, res["acts"], w.persons)
    consequence = ARC.consequence_acts(w, d.act_of)
    cut = frozenset(a for a in res["acts"] if a not in consequence)
    cres = SB.read(w.log, d.act_of, bounds, cut)
    ctext = CH.render(w.log, d.act_of, cres["executed"], w.persons)
    after = (w.content_hash(), len(w.log), list(w.writes))
    assert text and "nothing to chronicle" not in text, "the render read no acts; the check is vacuous"
    assert consequence and cut and ctext and "nothing to chronicle" not in ctext, \
        "the consequence reader and the cut read nothing; the check is vacuous"
    assert before == after


# ---- (2) the module is a reader: no write call, no token constructor -----------------------------

_FORBIDDEN = {"write", "add_tenure", "mint_token", "Token"}


def _writes_found(source: str) -> list:
    """Every forbidden call or import in `source`."""
    found = []
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Call):
            f = node.func
            name = f.id if isinstance(f, ast.Name) else f.attr if isinstance(f, ast.Attribute) else None
            if name in _FORBIDDEN:
                found.append(("call", name))
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            mod = getattr(node, "module", None) or ""
            for a in node.names:
                if a.name.split(".")[-1] in _FORBIDDEN or mod.split(".")[-1] in ("gate",):
                    found.append(("import", a.name))
    return found


def test_the_module_imports_no_write_constructor_and_calls_no_write():
    planted = "from ..state.gate import Token\nw.write('x', Token(), None)\nw.add_tenure(t)\n"
    assert len(_writes_found(planted)) >= 3, "the checker cannot see a planted write; it is absent"
    src = Path(CH.__file__).read_text(encoding="utf-8")
    assert _writes_found(src) == []


# ---- (3) a real seeded render is followable ------------------------------------------------------

_LINE = re.compile(r"^(\d+)\. season (\d+) \| (.+?) (\S+) \| emitted (.+?) \| (opens the chain|"
                   r"answers (\d+)\. (.+?) (\S+))$")


def test_a_real_render_names_distinct_actors_and_every_answer_is_a_real_earlier_antecedent(driven):
    w, d, bounds = driven
    res = SB.read(w.log, d.act_of, bounds)
    rows = res["acts"]
    ls = CH.lines(w.log, d.act_of, rows, w.persons)
    text = CH.render(w.log, d.act_of, rows, w.persons)
    out = text.splitlines()
    assert len(ls) >= 2, "the seeded run holds no cross-person chain; nothing to follow"
    assert len(out) == len(ls)
    assert len({l["actor"] for l in ls}) >= 2

    chain = CH.deepest_chain(rows)
    assert [rows[a]["depth"] for a in chain] == list(range(1, len(chain) + 1)), "a step skipped a depth"
    checked = 0
    for i, (l, line) in enumerate(zip(ls, out)):
        m = _LINE.match(line)
        assert m, f"line does not parse: {line!r}"
        assert int(m.group(1)) == i + 1
        if i == 0:
            assert m.group(6) == "opens the chain"
            continue
        cited = int(m.group(7))
        assert cited < i + 1, line                       # an antecedent appears EARLIER in the output
        assert ls[cited - 1]["act"] in rows[l["act"]]["cross"], line   # and is a real cross edge
        # a verb may hold spaces (`evade / defy`, `tie / knot`), which `_LINE` cannot split from the actor, so the
        # cited antecedent is compared as the joined `<actor> <verb>` text, which a wrong antecedent still fails
        assert f"{m.group(8)} {m.group(9)}" == f'{ls[cited - 1]["actor"]} {ls[cited - 1]["verb"]}'
        checked += 1
    assert checked >= 1, "no non-first line was checked"


# ---- (4) PLANT: a known chain, a shallower decoy before it, an equal rival after it ---------------

def _planted():
    chain = [("a1", "p1", "speak"), ("a2", "p2", "answer"), ("a3", "p3", "accept")]
    decoy = [("d1", "p4", "speak"), ("d2", "p5", "answer")]
    rival = [("r1", "p6", "speak"), ("r2", "p7", "answer"), ("r3", "p8", "accept")]
    acts = {i: NS(id=i, actor=p, verb=v) for grp in (decoy, chain, rival) for i, p, v in grp}
    ev = lambda i, kind, causes: NS(id=i, kind=kind, causes=causes)
    log = [ev("ed1", "k.d1", ["d1"]), ev("ed2", "k.d2", ["d2", "ed1"]),                  # decoy, first
           ev("e1", "k.one", ["a1"]), ev("e2", "k.two", ["a2", "e1"]),
           ev("e2b", "k.two_b", ["a2", "e1"]), ev("e3", "k.three", ["a3", "e2"]),       # the chain
           ev("er1", "k.r1", ["r1"]), ev("er2", "k.r2", ["r2", "er1"]),
           ev("er3", "k.r3", ["r3", "er2"])]                                             # rival, later
    act_of = {e.id: acts[e.causes[0]] for e in log}
    persons = {"p1": NS(name="Ada"), "p2": NS(name="Bo"), "p3": NS(name=""), "p4": NS(name="Dee")}
    return log, act_of, persons


def test_the_render_picks_the_deepest_chain_and_orders_it():
    log, act_of, persons = _planted()
    rows = SB.read(log, act_of, [0])["acts"]
    assert rows["d2"]["depth"] == 2 and rows["a3"]["depth"] == 3 and rows["r3"]["depth"] == 3
    assert CH.deepest_chain(rows) == ["a1", "a2", "a3"]            # not the decoy, not the later rival
    assert CH.render(log, act_of, rows, persons).splitlines() == [
        "1. season 0 | Ada speak | emitted k.one | opens the chain",
        "2. season 0 | Bo answer | emitted k.two, k.two_b | answers 1. Ada speak",
        "3. season 0 | p3 accept | emitted k.three | answers 2. Bo answer",    # no name -> the id
    ]


def test_the_walk_back_takes_the_antecedent_one_level_shallower_not_the_first_sorted():
    """An end act with TWO cross antecedents: `b0` (depth 1) sorts before `c2` (depth 2). The walk back
    must take `c2`, the one at depth d - 1, so the chain is three acts long and not two."""
    acts = {i: NS(id=i, actor=p, verb="speak") for i, p in
            (("c1", "p1"), ("c2", "p2"), ("b0", "p3"), ("x", "p4"))}
    ev = lambda i, causes: NS(id=i, kind=f"k.{i}", causes=causes)
    log = [ev("eb0", ["b0"]), ev("ec1", ["c1"]), ev("ec2", ["c2", "ec1"]), ev("ex", ["x", "eb0", "ec2"])]
    act_of = {e.id: acts[e.causes[0]] for e in log}
    rows = SB.read(log, act_of, [0])["acts"]
    assert rows["x"]["cross"] == ["b0", "c2"] and rows["x"]["depth"] == 3, rows["x"]   # the shallower sorts first
    assert CH.deepest_chain(rows) == ["c1", "c2", "x"]


def test_the_cli_runs_and_prints_its_header(capsys):
    assert CH.main(["--seed", "0", "--seasons", "1", "--cap", "5"]) == 0
    head = capsys.readouterr().out.splitlines()[0]
    assert head.startswith("chronicle seed=0 seasons=1 arm=off cap=5 ") and "PYTHONHASHSEED=" in head, head
    assert " acts=" in head and head.rsplit(" ", 1)[1].startswith("consequence_acts="), head


def _rc(subject, field="capability"):
    """A Receipt writing `(Person, field)`; `capability` is in `ARC_SELF`, `body` in `ARC_WORLD`."""
    return Receipt(subject=subject, mode="set", driver="plant", field=field, delta=1)


def _world(log):
    """The slice of `World` that `arc.consequence_acts` and `chronicle.main` read."""
    return NS(log=log, persons={}, tenures=[], offices={},
              class_of=lambda sub: "Person" if sub.startswith("p") else None)


def _chain(ids, wrote, first_actor, kind="k"):
    """`(events, act_of)` for one chain: act `ids[i]` by person `p<first_actor + i>`, each answering the one
    before. `wrote[i]` False = the act's Event carries no Receipt (an act that wrote nothing)."""
    events = []
    for i, aid in enumerate(ids):
        causes = [aid] + ([f"e{ids[i - 1]}"] if i else [])
        events.append(NS(id=f"e{aid}", kind=f"{kind}.{aid}", causes=causes,
                         changes=[_rc(f"p{first_actor + i}")] if wrote[i] else []))
    acts = {aid: NS(id=aid, actor=f"p{first_actor + i}", verb="speak") for i, aid in enumerate(ids)}
    return events, {e.id: acts[e.causes[0]] for e in events}


def _joined(*chains):
    return [e for ev, _ in chains for e in ev], {k: v for _, ao in chains for k, v in ao.items()}


def _depth5_refusals_then_depth3_writes():
    """A depth-5 chain whose acts wrote nothing, logged FIRST; a depth-3 chain whose acts wrote, after it."""
    return _joined(_chain(["f1", "f2", "f3", "f4", "f5"], [False] * 5, 1, "refused"),
                   _chain(["w1", "w2", "w3"], [True] * 3, 6))


def _through_a_nothing_writing_act():
    """The deepest ALL-ACTS chain is `c1 -> c2 -> c3 -> c4` and runs through `c2`, an act that wrote
    nothing. A shorter rival `r1 -> r2 -> r3`, all writing, is logged after it. Cut at `c2`, `c3` is a first
    act and `c4` stands at depth 2, so the deepest consequence chain is the rival (3)."""
    return _joined(_chain(["c1", "c2", "c3", "c4"], [True, False, True, True], 1),
                   _chain(["r1", "r2", "r3"], [True] * 3, 5))


def _run_main_over(monkeypatch, capsys, plant, *flags):
    """`chronicle.main` over a planted log: `drive` is replaced, nothing else (the consequence reader is real)."""
    log, act_of = plant()
    monkeypatch.setattr(SB, "drive", lambda *a, **k: (_world(log), NS(act_of=act_of), [0]))
    assert CH.main(["--seed", "0", "--seasons", "1", *flags]) == 0
    return capsys.readouterr().out.splitlines()


def _actors(lines):
    return [l.split("|")[1].strip().split()[0] for l in lines]


def test_a_depth_3_consequence_chain_outranks_a_depth_5_chain_of_refusals(monkeypatch, capsys):
    out = _run_main_over(monkeypatch, capsys, _depth5_refusals_then_depth3_writes)
    assert " acts=8 depth=3 " in out[0] and out[0].endswith("consequence_acts=3"), out[0]
    assert _actors(out[1:]) == ["p6", "p7", "p8"]                  # the writers, not the deeper refusals
    allacts = _run_main_over(monkeypatch, capsys, _depth5_refusals_then_depth3_writes, "--all-acts")
    assert " depth=5 " in allacts[0] and _actors(allacts[1:]) == ["p1", "p2", "p3", "p4", "p5"]


def test_the_mutation_that_counts_every_act_a_consequence_act_puts_the_deeper_refusals_back(monkeypatch, capsys):
    """PLANTED FAILURE for the test above: with `consequence_acts` returning every act (the mutation), the
    depth-5 chain of refusals is picked again, so the assertion of the test above can fail."""
    monkeypatch.setattr(ARC, "consequence_acts",
                        lambda w, act_of, log=None: frozenset(a.id for a in act_of.values()))
    out = _run_main_over(monkeypatch, capsys, _depth5_refusals_then_depth3_writes)
    assert _actors(out[1:]) == ["p1", "p2", "p3", "p4", "p5"], out
    assert not (" acts=8 depth=3 " in out[0] and _actors(out[1:]) == ["p6", "p7", "p8"])


def test_a_graded_loss_that_writes_counts_and_a_refusal_that_writes_nothing_does_not():
    loss = NS(id="el", kind="field.lost", causes=["loss"], changes=[_rc("p2", "body")])   # ARC_WORLD
    refusal = NS(id="er", kind="act.refused", causes=["refusal"], changes=[])
    noise = NS(id="en", kind="claim.deposited", causes=["noise"],
               changes=[_rc("p3", "claim_ledger"), _rc("p3", "travel_leg")])   # neither is on a roster
    log = [loss, refusal, noise]
    act_of = {e.id: NS(id=e.causes[0], actor=f"p{i + 1}", verb="fight") for i, e in enumerate(log)}
    assert ("Person", "body") in ARC.ARC_WORLD and ("Person", "claim_ledger") not in ARC.ARC_WORLD
    assert ARC.consequence_acts(_world(log), act_of) == frozenset({"loss"})
    # the control: the same refusal given a roster write becomes a consequence act, so the reader can say yes
    refusal.changes = [_rc("p2")]
    assert ARC.consequence_acts(_world(log), act_of) == frozenset({"loss", "refusal"})


def test_the_seat_receipt_a_death_mints_is_no_write_of_a_record():
    seat = NS(id="et", kind=ARC.TENURE_CLOSED, causes=["slay"], changes=[_rc("office1")])
    world = _world([seat])
    world.offices = {"office1": object()}
    act_of = {"et": NS(id="slay", actor="p1", verb="fight")}
    assert ARC.consequence_acts(world, act_of) == frozenset()
    world.offices = {}                                       # the control: not an Office, the same Receipt counts
    assert ARC.consequence_acts(world, act_of) == frozenset({"slay"})


def test_an_act_that_wrote_nothing_is_cut_with_its_edges_and_depth_is_recomputed(monkeypatch, capsys):
    """RE-RECORDED PIN (CR-68). OLD default: header `acts=7 depth=4`, the chain p1..p4 through the refused
    `c2`, no `executed-only`. NEW default: `acts=7 depth=3 ... consequence_acts=6`, the rival p5..p7 (`c2` is
    cut, `c3` is a first act, `c4` depth 2). `--all-acts` reproduces the OLD default's body and fields."""
    default = _run_main_over(monkeypatch, capsys, _through_a_nothing_writing_act)
    assert default[0].split(" PYTHONHASHSEED=")[0].endswith("acts=7 depth=3")
    assert default[0].endswith("consequence_acts=6") and "executed-only" not in default[0]
    assert _actors(default[1:]) == ["p5", "p6", "p7"]

    old = _run_main_over(monkeypatch, capsys, _through_a_nothing_writing_act, "--all-acts")
    assert old[0].split(" PYTHONHASHSEED=")[0].endswith("acts=7 depth=4")           # the old pin
    assert _actors(old[1:]) == ["p1", "p2", "p3", "p4"]
    assert old[0].endswith("consequence_acts=6"), "the header lost its added field under --all-acts"


def test_with_every_act_writing_the_consequence_pick_is_the_all_acts_pick(monkeypatch, capsys):
    """The cut's control: nothing cut, and the default renders exactly what `--all-acts` does."""
    plant = lambda: _joined(_chain(["c1", "c2", "c3", "c4"], [True] * 4, 1))
    default = _run_main_over(monkeypatch, capsys, plant)
    allacts = _run_main_over(monkeypatch, capsys, plant, "--all-acts")
    assert default == allacts and len(default) == 5 and default[0].endswith("consequence_acts=4")


def test_a_log_with_no_consequence_act_says_so_and_does_not_fall_back(monkeypatch, capsys):
    plant = lambda: _joined(_chain(["f1", "f2"], [False, False], 1))
    out = _run_main_over(monkeypatch, capsys, plant)
    assert out[0].endswith("consequence_acts=0") and " depth=0 " in out[0]
    assert out[1:] == ["no consequence act in the log; --all-acts renders over every act"]


def test_with_no_cross_person_answer_the_first_logged_act_is_rendered_alone():
    a = NS(id="a1", actor="p1", verb="speak")
    log = [NS(id="e1", kind="k", causes=["a1"])]
    rows = SB.read(log, {"e1": a}, [0])["acts"]
    text = CH.render(log, {"e1": a}, rows, {})
    assert text.splitlines()[0].startswith("no act answered another person's act")
    assert "1. season 0 | p1 speak | emitted k | opens the chain" in text
    assert CH.render([], {}, {}, {}) == "no acts in the log; nothing to chronicle"
