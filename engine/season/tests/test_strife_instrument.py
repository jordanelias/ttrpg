"""`harness.strife` -- the side-aware classifier and the static route check.

What each block proves, and the control that stops it passing vacuously:

  1. THE REGISTRY LOADS 40 CODES AND REFUSES A BAD SIGNATURE. A signature naming an unknown verb, an
     undeclared kind, a code with no row, an unknown key or a bad attacker side is refused: each is
     planted in a temporary copy of the file and the load must raise (the loader is the only guard).
  2. DEATH IS TOLD BY ITS CAUSE. The same `person.died` kind classifies DN with no causing act and KL
     with a `fight` or a `march`. CONTROL: an unrelated verb classifies as neither.
  3. A FIELD IS TOLD BY WHO MARCHED. `field.won` is WA when the attacker is the authority and WR when
     it is a challenger, and the two codes SWAP for `field.lost`. FALSIFIER: swapping the side swaps
     the code, so a classifier that ignored side could not pass; and a side that cannot be told
     (`None`) yields no code, so nothing is guessed.
  4. `side_against`: the nearest governor and a governor above it are the authority; a faction in
     the chain nowhere is a challenger; no governor, or no attacker, is `None`.
  5. THE ROUTE CHECK IS REAL. `petition` reaches PT by a resolvable verb that emits a kind PT names;
     XE and CH have no route (planted gap); a verb that is not resolvable gives no route even when its
     row emits the kind. CONTROL: removing a verb from `resolvable` removes its route.

NOT COVERED, AND SAYING SO: the wiring from a real `World` (`readers_for`, `governors`) is exercised
only by the observed arm of the instrument (`python -m engine.season.harness.strife 4 0 1`), not here.
"""
from types import SimpleNamespace

import pytest

from engine.season.harness import strife as H
from engine.season.harness import strife_data as data
from engine.season.harness.strife_data import STRIFE_MOVES_YAML


def ev(kind):
    return SimpleNamespace(kind=kind)


def readers(verb=None, side=None, held=False):
    return H.Readers(lambda e: verb, lambda e: side, lambda e: held)


def codes(e, rd):
    return sorted(c for c, _ in H.classify(e, rd))


def test_registry_loads_forty_codes_and_signatures():
    rows, sigs, foreign = data.load_moves()
    assert foreign and len(foreign) == 2
    assert len(rows) == 40 and len({r["code"] for r in rows}) == 40
    assert len(sigs) >= 1


@pytest.mark.parametrize("bad", [
    "  - {kind: person.died, cause_verb: nonesuch, code: KL}",
    "  - {kind: nonesuch.kind, cause_verb: fight, code: KL}",
    "  - {kind: person.died, cause_verb: fight, code: ZZ}",
    "  - {kind: person.died, cause_verb: fight, code: KL, colour: red}",
    "  - {kind: field.won, attacker: Q, code: WA}",
])
def test_loader_refuses_a_bad_signature(tmp_path, bad):
    text = STRIFE_MOVES_YAML.read_text(encoding="utf-8").replace("signatures:\n", "signatures:\n" + bad + "\n", 1)
    p = tmp_path / "strife_moves.yaml"
    p.write_text(text, encoding="utf-8")
    with pytest.raises(ValueError):
        data.load_moves(p)


def test_a_death_is_told_by_its_cause():
    assert codes(ev("person.died"), readers(verb=None)) == ["DN"]
    assert codes(ev("person.died"), readers(verb="fight")) == ["KL"]
    assert codes(ev("person.died"), readers(verb="fight", held=True)) == ["XE"]   # a held person killed by a fight is executed
    assert codes(ev("person.died"), readers(verb=None, held=True)) == ["DN"]       # held, but no act of anyone: died, not executed
    assert codes(ev("person.died"), readers(verb="march")) == ["KL"]
    assert codes(ev("person.died"), readers(verb="tell")) == []      # control: another verb is neither


def test_a_field_is_told_by_who_marched_and_the_codes_swap_on_a_loss():
    assert codes(ev("field.won"), readers(side="A")) == ["WA"]
    assert codes(ev("field.won"), readers(side="R")) == ["WR"]
    assert codes(ev("field.lost"), readers(side="A")) == ["WR"]
    assert codes(ev("field.lost"), readers(side="R")) == ["WA"]
    assert codes(ev("field.won"), readers(side=None)) == []           # a side that cannot be told is not guessed
    assert codes(ev("march.declared"), readers(side="A")) == ["FR"]
    assert codes(ev("march.declared"), readers(side="R")) == ["WN"]
    assert codes(ev("march.declared"), readers(side="O")) == ["OW"]             # an invasion by a foreign nation


def test_an_event_matching_no_signature_is_left_alone():
    assert H.classify(ev("petition.filed"), readers(verb="petition", side="A")) == []


def test_side_against_the_governors():
    assert H.side_against("f_crown", ["f_crown", "f_realm"]) == "A"   # the nearest governor
    assert H.side_against("f_realm", ["f_crown", "f_realm"]) == "A"   # a governor above it, sending force down
    assert H.side_against("f_rebel", ["f_crown", "f_realm"]) == "R"
    assert H.side_against("f_rebel", []) is None                       # nobody governs: no authority to compare
    assert H.side_against(None, ["f_crown"]) is None
    assert H.side_against("f_altonia", ["f_crown"], {"f_altonia"}) == "O"       # a foreign faction is an outside power
    assert H.side_against("f_altonia", [], {"f_altonia"}) == "O"                 # whether or not anything governs the rung
    assert H.side_against("f_rebel", ["f_crown"], {"f_altonia"}) == "R"          # control: a non-foreign challenger stays R


def test_the_route_check_finds_a_route_and_a_planted_gap():
    rows = {r["code"]: r for r in data.MOVES}
    assert [v for v, _ in H.route(rows["PT"])] and "petition" in [v for v, _ in H.route(rows["PT"])]
    assert H.route(rows["CH"]) == []                                    # no verb and no kind: a gap
    assert "fight" in [v for v, _ in H.route(rows["XE"])]               # XE composes on `fight`; formation on a held party is open
    only = {"carry"}                                                    # CONTROL: drop `petition` from the resolvable set
    assert "petition" not in [v for v, _ in H.route(rows["PT"], resolvable=only)]
    assert "carry" in [v for v, _ in H.route(rows["PT"], resolvable=only)]


def test_grade_cases():
    from collections import Counter
    rows = {r["code"]: r for r in data.MOVES}
    act = Counter({("KL", None): 3})
    assert H.grade(rows["KL"], Counter(), act, True) == ("OBSERVED", 3)
    assert H.grade(rows["DN"], Counter(), act, True) == ("UNOBSERVED", 0)
    assert H.grade(rows["OW"], Counter({"march.declared": 99}), Counter(), False)[0] == "DARK"   # kinds shared: not readable
    assert H.grade(rows["CH"], Counter(), Counter(), False)[0] == "GAP"
    assert H.grade(rows["PT"], Counter({"petition.filed": 2}), Counter(), False) == ("OBSERVED", 2)


def test_endings_total_the_study_and_yield_24_terminal_codes():
    rows = data.MOVES
    assert sum(r.get("ends", 0) for r in rows) == 102
    terminal = {r["code"] for r in rows if r.get("ends", 0) > 0 and r.get("terminal", True)}
    assert len(terminal) == 24 and "XP" not in terminal and {"PC", "CO", "WA", "XE"} <= terminal
    assert all(r.get("ends", 0) == 0 for r in rows if r["code"] in {"SH", "DR", "BR", "MO", "OP", "RU", "VI", "SZ"})


def test_loader_refuses_ends_that_do_not_total_102(tmp_path):
    text = STRIFE_MOVES_YAML.read_text(encoding="utf-8").replace("ends: 20", "ends: 21", 1)
    p = tmp_path / "strife_moves.yaml"
    p.write_text(text, encoding="utf-8")
    with pytest.raises(ValueError):
        data.load_moves(p)


def test_the_foreign_nations_are_altonia_and_schoenland():
    from engine.season.data.rosters import faction_prop_id
    assert data.FOREIGN == {faction_prop_id("Altonia"), faction_prop_id("Schoenland")}
