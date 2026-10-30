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
"""

from __future__ import annotations

import ast
import re
from pathlib import Path
from types import SimpleNamespace as NS

import pytest

from ..harness import chronicle as CH
from ..harness import storybar as SB

SEED, SEASONS, CAP = 0, 2, 10


@pytest.fixture(scope="module")
def driven():
    return SB.drive(SEED, SEASONS, "off", CAP)


# ---- (1) the render writes nothing to the World --------------------------------------------------

def test_the_render_changes_nothing_in_the_world(driven):
    w, d, bounds = driven
    before = (w.content_hash(), len(w.log), list(w.writes))
    res = SB.read(w.log, d.act_of, bounds)
    text = CH.render(w.log, d.act_of, res["acts"], w.persons)
    after = (w.content_hash(), len(w.log), list(w.writes))
    assert text and "nothing to chronicle" not in text, "the render read no acts; the check is vacuous"
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


def _planted_through_a_refused_act():
    """The deepest default chain is `c1 -> c2 -> c3 -> c4` and runs through `c2`, a REFUSED act. A
    shorter rival `r1 -> r2 -> r3`, all executed, is logged after it. Cut at `c2`, `c3` is a first act and
    `c4` stands at depth 2, so the deepest EXECUTED chain is the rival (3)."""
    acts = {i: NS(id=i, actor=p, verb="speak") for i, p in
            (("c1", "p1"), ("c2", "p2"), ("c3", "p3"), ("c4", "p4"),
             ("r1", "p5"), ("r2", "p6"), ("r3", "p7"))}
    ev = lambda i, kind, causes: NS(id=i, kind=kind, causes=causes)
    log = [ev("ec1", "k.c1", ["c1"]), ev("ec2", "k.c2.refused", ["c2", "ec1"]),
           ev("ec3", "k.c3", ["c3", "ec2"]), ev("ec4", "k.c4", ["c4", "ec3"]),
           ev("er1", "k.r1", ["r1"]), ev("er2", "k.r2", ["r2", "er1"]), ev("er3", "k.r3", ["r3", "er2"])]
    act_of = {e.id: acts[e.causes[0]] for e in log}
    return log, act_of


def _run_main_over_the_plant(monkeypatch, capsys, refused, *flags):
    """`chronicle.main` over the planted log: `drive` and `refusal_sets` are replaced, nothing else."""
    log, act_of = _planted_through_a_refused_act()
    world = NS(log=log, persons={})
    monkeypatch.setattr(SB, "drive", lambda *a, **k: (world, NS(act_of=act_of), [0]))
    monkeypatch.setattr(SB, "refusal_sets", lambda w, n: (frozenset(refused), frozenset()))
    assert CH.main(["--seed", "0", "--seasons", "1", *flags]) == 0
    return capsys.readouterr().out.splitlines()


def test_a_deepest_chain_through_a_refused_act_picks_a_shorter_executed_chain(monkeypatch, capsys):
    default = _run_main_over_the_plant(monkeypatch, capsys, {"c2"})
    assert "executed-only" not in default[0]
    assert default[0].split(" PYTHONHASHSEED=")[0].endswith("acts=7 depth=4")
    assert [l.split("|")[1].strip() for l in default[1:]] == [
        "p1 speak", "p2 speak", "p3 speak", "p4 speak"]

    ex = _run_main_over_the_plant(monkeypatch, capsys, {"c2"}, "--executed-only")
    assert ex[0].startswith(default[0].split(" PYTHONHASHSEED=")[0]), "the header lost its fields"
    assert "default_chain_refused=1 executed_acts=6 executed_depth=3" in ex[0], ex[0]
    assert [l.split("|")[1].strip() for l in ex[1:]] == ["p5 speak", "p6 speak", "p7 speak"]
    assert len(ex) - 1 < len(default) - 1                  # a shorter chain, and not through c2


def test_with_nothing_refused_the_executed_pick_is_the_default_pick(monkeypatch, capsys):
    """The mutation's control: `refused` empty, and `--executed-only` renders the default chain."""
    default = _run_main_over_the_plant(monkeypatch, capsys, ())
    ex = _run_main_over_the_plant(monkeypatch, capsys, (), "--executed-only")
    assert len(default) == 5 and ex[1:] == default[1:]
    assert "default_chain_refused=0" in ex[0] and "executed_depth=4" in ex[0]


def test_with_no_cross_person_answer_the_first_logged_act_is_rendered_alone():
    a = NS(id="a1", actor="p1", verb="speak")
    log = [NS(id="e1", kind="k", causes=["a1"])]
    rows = SB.read(log, {"e1": a}, [0])["acts"]
    text = CH.render(log, {"e1": a}, rows, {})
    assert text.splitlines()[0].startswith("no act answered another person's act")
    assert "1. season 0 | p1 speak | emitted k | opens the chain" in text
    assert CH.render([], {}, {}, {}) == "no acts in the log; nothing to chronicle"
