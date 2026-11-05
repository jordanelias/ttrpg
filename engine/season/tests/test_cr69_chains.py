"""CR-69 -- `harness/chronicle.py::consequence_chains` (`--chains --min-depth D`), the story reading.

A READING, NEVER A GUARD: these tests pin the reader's contract on planted worlds (a known number of chains),
never a run's numbers. The falsifier and the control the plan names, observed rather than assumed:
  * a planted world with a KNOWN number of consequence chains reads that number, and moves with `--min-depth`;
  * the same world with its `causes` shuffled (`arc.shuffled_causes`, the one null; not a second) reads lower;
  * the same seed twice reads identically (the planted world, and a real seeded run);
  * PLANTED FAILURES redden the first: a predicate that counts every act, and a reader that ignores `min_depth`;
  * the kinds histogram is read off the log: a planted kind nobody listed appears, a kind of an act that is not a
    chain end or not a consequence Event does not;
  * `--chains` without `--min-depth` is refused (no default);
  * the reader writes nothing: content hash, log length and write list are unchanged by it.
"""

from __future__ import annotations

from types import SimpleNamespace as NS

import pytest

from ..harness import arc as ARC
from ..harness import chronicle as CH
from ..harness import storybar as SB
from ..state.carriers import Event, Receipt
from .test_in37_chronicle import _world

SEED, SEASONS, CAP = 0, 2, 10


def _rc(subject, field="capability"):
    return Receipt(subject=subject, mode="set", driver="plant", field=field, delta=1)


def _chain(tag, depth, first_actor, wrote=True, kinds=None):
    """`(events, act_of)`: act `<tag><i>` by person `p<first_actor + i>`, each answering the one before.
    `kinds[i]` is the Event kind of act i (default `<tag>.<i>`); `wrote` False = the Events carry no Receipt."""
    events, acts = [], {}
    for i in range(depth):
        aid = f"{tag}{i}"
        causes = [aid] + ([f"e{tag}{i - 1}"] if i else [])
        kind = kinds[i] if kinds else f"{tag}.{i}"
        events.append(Event(f"e{aid}", kind, [_rc(f"p{first_actor + i}")] if wrote else [], causes, 0))
        acts[aid] = NS(id=aid, actor=f"p{first_actor + i}", verb="speak")
    return events, {e.id: acts[e.causes[0]] for e in events}


def _plant():
    """Four writing chains of depth 3 (two end on `war.ended`, two on `heir.named`), a writing chain of depth
    2, and a NON-writing chain of depth 4 (it would outrank them all if every act counted)."""
    parts = [_chain("a", 3, 1, kinds=["x.a0", "x.a1", "war.ended"]),
             _chain("b", 3, 4, kinds=["x.b0", "x.b1", "war.ended"]),
             _chain("c", 3, 7, kinds=["x.c0", "x.c1", "heir.named"]),
             _chain("d", 3, 10, kinds=["x.d0", "x.d1", "heir.named"]),
             _chain("s", 2, 13),
             _chain("n", 4, 15, wrote=False)]
    return [e for ev, _ in parts for e in ev], {k: v for _, ao in parts for k, v in ao.items()}


def _read(min_depth, plant=_plant, log=None):
    events, act_of = plant()
    return CH.consequence_chains(_world(events), act_of, [0], min_depth, log=log)


KNOWN = 4        # the depth-3 chains planted above


def test_a_planted_world_reads_its_known_number_of_chains():
    res = _read(3)
    assert res["chain_ends"] == KNOWN, res
    assert res["consequence_acts"] == 3 * 4 + 2, res        # the non-writing chain is not one
    # depth moves the reading: the depth-2 chain joins at 2, and nothing is as deep as 4 among the writers
    assert _read(2)["chain_ends"] == KNOWN + 1
    assert _read(4)["chain_ends"] == 0
    # depth 1: every consequence act that no other consequence act answers is a chain end: still the five ends
    assert _read(1)["chain_ends"] == KNOWN + 1


def test_the_kinds_are_read_off_the_log_and_only_over_the_chain_ends():
    res = _read(3)
    assert res["kinds"] == {"heir.named": 2, "war.ended": 2}, res    # not x.a1 (a middle act), not the depth-2 end
    # a kind nobody listed appears once planted: the reader holds no roster
    events, act_of = _plant()
    events[2].kind = "grudge.sworn"                                  # chain a's end
    res2 = CH.consequence_chains(_world(events), act_of, [0], 3)
    assert res2["kinds"] == {"grudge.sworn": 1, "heir.named": 2, "war.ended": 1}, res2
    # a kind counts the Receipts that made the act a consequence act: an end act whose Event wrote nothing
    # but whose act wrote on another Event reads the writing Event's kind
    events, act_of = _plant()
    quiet = Event("equiet", "noise.only", [], ["a2", "ea1"], 0)
    events[2].changes = []                                           # chain a's end Event writes nothing now ...
    events.append(Event("ewrote", "late.write", [_rc("p3")], ["a2"], 0))  # ... its act writes on a second Event
    act_of["ewrote"] = act_of["ea2"]
    act_of["equiet"] = act_of["ea2"]
    events.append(quiet)
    res3 = CH.consequence_chains(_world(events), act_of, [0], 3)
    assert res3["chain_ends"] == KNOWN and res3["kinds"] == {"heir.named": 2, "late.write": 1, "war.ended": 1}, res3


def test_the_shuffled_causes_null_reads_below_the_linked_log():
    events, act_of = _plant()
    w = _world(events)
    real = CH.consequence_chains(w, act_of, [0], 3)["chain_ends"]
    assert real == KNOWN
    below = 0
    for seed in range(8):
        shuffled = ARC.shuffled_causes(events, seed)
        assert any(s.causes != e.causes for s, e in zip(shuffled, events))       # the null moved something
        null = CH.consequence_chains(w, act_of, [0], 3, log=shuffled)["chain_ends"]
        assert null < real, (seed, null)
        below += 1
    assert below == 8


def test_the_same_world_read_twice_reads_identically():
    assert _read(3) == _read(3)
    events, act_of = _plant()
    w = _world(events)
    a = CH.consequence_chains(w, act_of, [0], 3, log=ARC.shuffled_causes(events, 3))
    b = CH.consequence_chains(w, act_of, [0], 3, log=ARC.shuffled_causes(events, 3))
    assert a == b


# ---- PLANTED FAILURES: the checks above can fail ---------------------------------------------------------

def test_the_mutation_that_counts_every_act_a_consequence_act_misreads_the_plant(monkeypatch):
    """With the predicate returning every act (and every Event kind), the non-writing depth-4 chain joins and
    the known number is not read, so the first test can fail."""
    events, act_of = _plant()
    kinds = {}
    for e in events:
        kinds.setdefault(act_of[e.id].id, []).append(e.kind)
    monkeypatch.setattr(ARC, "consequence_kinds",
                        lambda w, act_of, log=None: {a: tuple(k) for a, k in kinds.items()})
    res = CH.consequence_chains(_world(events), act_of, [0], 3)
    assert res["chain_ends"] != KNOWN, res
    assert res["chain_ends"] == KNOWN + 1                           # the depth-4 chain of nothing


def test_the_mutation_that_ignores_min_depth_misreads_the_plant(monkeypatch):
    real = CH.chain_ends
    monkeypatch.setattr(CH, "chain_ends", lambda rows, min_depth: real(rows, 0))
    assert _read(3)["chain_ends"] != KNOWN
    assert _read(4)["chain_ends"] != 0


# ---- the CLI: no default for --min-depth ----------------------------------------------------------------

def _run_main(monkeypatch, capsys, *flags):
    events, act_of = _plant()
    monkeypatch.setattr(SB, "drive", lambda *a, **k: (_world(events), NS(act_of=act_of), [0]))
    assert CH.main(["--seed", "0", "--seasons", "1", *flags]) == 0
    return capsys.readouterr().out.splitlines()


def test_chains_prints_its_own_block_and_without_the_flag_nothing_is_added(monkeypatch, capsys):
    plain = _run_main(monkeypatch, capsys)
    out = _run_main(monkeypatch, capsys, "--chains", "--min-depth", "3")
    assert out[:len(plain)] == plain                                 # the render is untouched
    assert out[len(plain):] == [
        "chains seed=0 min_depth=3 consequence_acts=14 chain_ends=4",
        "kinds on the ends' consequence Events: heir.named=2, war.ended=2"], out[len(plain):]


def test_chains_without_min_depth_is_refused(monkeypatch, capsys):
    events, act_of = _plant()
    monkeypatch.setattr(SB, "drive", lambda *a, **k: (_world(events), NS(act_of=act_of), [0]))
    with pytest.raises(SystemExit) as e:
        CH.main(["--seed", "0", "--seasons", "1", "--chains"])
    assert e.value.code == 2 and "--min-depth" in capsys.readouterr().err


# ---- a real seeded run: reads identically twice, writes nothing ------------------------------------------

def test_the_reader_on_a_real_seed_writes_nothing_and_reads_identically():
    w, d, bounds = SB.drive(SEED, SEASONS, "off", CAP)
    before = (w.content_hash(), len(w.log), list(w.writes))
    a = CH.consequence_chains(w, d.act_of, bounds, 1)
    b = CH.consequence_chains(w, d.act_of, bounds, 1)
    null = CH.consequence_chains(w, d.act_of, bounds, 1, log=ARC.shuffled_causes(w.log, 0))
    after = (w.content_hash(), len(w.log), list(w.writes))
    assert a == b and before == after
    assert a["consequence_acts"] > 0 and a["chain_ends"] > 0, "the real run read no chain; the check is vacuous"
    assert null["chain_ends"] != a["chain_ends"] or null["kinds"] != a["kinds"], "the null moved nothing"
    # the consequence reader's own predicate is unchanged in result: the acts are the keys of the kinds
    assert ARC.consequence_acts(w, d.act_of) == frozenset(ARC.consequence_kinds(w, d.act_of))
