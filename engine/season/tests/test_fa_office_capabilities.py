"""B04.21 -- a seat row may name the skill its post calls on (`capability:`, row data, not a `Seat` field).

Created here because B04.19 is a POINTER (the social contest's V2 fold, ED-IN-0378); B04.22 and B04.23 add to it.
`data/rosters.py::_load_offices` refuses a `capability:` that is not a defined skill (`descriptors.CAPABILITIES`),
naming the row. The loader is pointed at a throwaway copy of the shipped file (as
`test_governance_build.py::test_8a_a_repeated_row_id_refuses_at_load_instead_of_being_collapsed` does); the unchanged
copy and a copy carrying a defined skill and a `null` are the positive controls, so a loader that refused every
file cannot pass.
"""
from __future__ import annotations

import pytest
import yaml

from engine.substrate.descriptors import CAPABILITIES

from ..data import files, rosters
from ..decision import assemble
from ..decision import choose as CH
from ..gaps import Unspecified
from ..queries import person_q, world_q
from ..seam.wrappers import sigma
from ..state.carriers import Claim
from .test_g3_not_yours import _gov_world


def _real() -> dict:
    return rosters.load_yaml(files.OFFICES_YAML.read_text(encoding="utf-8"))


def _load_with(tmp_path, monkeypatch, doc: dict) -> dict:
    path = tmp_path / "offices.yaml"
    path.write_text(yaml.safe_dump(doc), encoding="utf-8")
    monkeypatch.setattr(rosters, "OFFICES_YAML", path)
    return rosters._load_offices()


def test_a_seat_row_naming_an_undefined_capability_is_refused(tmp_path, monkeypatch):
    real = _real()
    n = len(real["seats"])
    assert len(_load_with(tmp_path, monkeypatch, real)["seats"]) == n  # control: the unchanged file loads

    row = real["seats"][0]
    assert "capability" not in row  # control: no shipped row names one (the first commit authors none)
    for bad in ("swordplay", "", 7, ["arms"]):
        doc = dict(real, seats=[dict(row, capability=bad), *real["seats"][1:]])
        with pytest.raises(Unspecified) as red:
            _load_with(tmp_path, monkeypatch, doc)
        assert row["id"] in str(red.value) and "capability" in str(red.value), str(red.value)

    # the same refusal over `foreign_seats:`, which shares the row shape
    if real.get("foreign_seats"):
        frow = real["foreign_seats"][0]
        doc = dict(real, foreign_seats=[dict(frow, capability="swordplay"), *real["foreign_seats"][1:]])
        with pytest.raises(Unspecified) as red:
            _load_with(tmp_path, monkeypatch, doc)
        assert frow["id"] in str(red.value)


def test_a_seat_row_may_name_a_defined_skill_or_null(tmp_path, monkeypatch):
    real = _real()
    row = real["seats"][0]
    checked = 0
    for ok in (*CAPABILITIES, None):
        doc = dict(real, seats=[dict(row, capability=ok), *real["seats"][1:]])
        loaded = _load_with(tmp_path, monkeypatch, doc)
        assert loaded["seats"][0]["capability"] == ok
        checked += 1
    assert checked == len(CAPABILITIES) + 1 and checked > 1


def test_the_shipped_offices_file_names_no_capability_yet():
    # B04.21 ships the key, not its content (D-19): the candidate rows are for Jordan, not authored.
    named = [r["id"] for r in (*rosters.OFFICES_SEATS, *rosters.FOREIGN_SEATS) if r.get("capability") is not None]
    assert named == [], named


# ======================================================================================
# B04.22 -- the conferrer weighs the candidate, behind `confer_fit_weight` (shipped 0.0)
# ======================================================================================
# `decision/choose.py::score_terms` gains a `fit` term over a seating row's `to` operand: the conferrer's regard for him
# (`person_q.regard`) and, where the seat's row names a skill, the skill his own ledger holds of the candidate
# (`person_q.believed_capability`, the claim read `sigma.believed_input` also makes). The weight is one fixture.

_OFFICE = "off_reeve"


def _vacancy_world():
    """`_gov_world`'s vacant `off_reeve`, and `p_king`, who may fill it, knowing `p_mid` and `p_low`; he holds a stance row
    of +4 weight 2 on `p_mid` and none on `p_low` (so he regards `p_mid` higher), and none on himself."""
    w, _ = _gov_world()
    king = w.persons["p_king"]
    for i, o in enumerate(("p_mid", "p_low")):
        king.ledger.append(Claim(f"c_k{i}", "p_king", o, "exists:Person", 1, 0, "firsthand", 100, "own"))
    king.stance.append(("p_mid", 4, 2))
    return w


def _conferees(w, weight):
    """The `to` of every `confer` on `off_reeve` the conferrer's real ranking orders, best first, at `confer_fit_weight`
    `weight` (`make_ranker`: formed, scored, sampled; nothing packed)."""
    fx = w.fixtures.sweep("confer_fit_weight", weight).sweep("choice_temperature", 0.0)   # the order is the score order, undrawn
    p = w.persons["p_king"]
    q = world_q.questions_for(w, p)[0]   # the first question carries the vacancies (`questions_for`)
    ranked = CH.make_ranker(fx, verbs=frozenset({"confer"}))(p, assemble(p, q, 12))
    tos = [c.operands["to"] for c in ranked if c.subject == _OFFICE]   # one per seat he may confer through (`via`)
    return list(dict.fromkeys(tos))


def test_confer_fit_weight_zero_is_positional():
    known = ["p_low", "p_mid"]
    zero = _conferees(_vacancy_world(), 0.0)
    assert sorted(zero) == ["p_king", *known], zero  # control: all three candidates form
    assert zero[0] == min(known), zero  # at 0.0 the lowest id he knows is seated (himself is formed last)

    # the control observes the failure it excludes: with no stance row at all the order is the same
    bare = _vacancy_world()
    bare.persons["p_king"].stance.clear()
    assert _conferees(bare, 0.0) == zero

    for weight in (0.5, 1.0):
        order = _conferees(_vacancy_world(), weight)
        assert order[0] == "p_mid" and order[0] != zero[0], (weight, order)  # the higher-regard candidate is seated


def test_the_fit_term_is_the_third_of_score_terms_and_is_exactly_zero_at_weight_zero():
    w = _vacancy_world()
    p = w.persons["p_king"]
    q = world_q.questions_for(w, p)[0]   # the first question carries the vacancies (`questions_for`)
    fx = w.fixtures.sweep("confer_fit_weight", 0.0)
    view = assemble(p, q, 12)
    cands = [c for c in CH.opening_set(p, view, q, fx) if c.verb == "confer" and c.subject == _OFFICE]
    memo = CH.deliberation_memo(p, fx)
    checked = 0
    for c in cands:
        terms = CH.score_terms(p, c, fx, memo)
        assert len(terms) == 3 and terms[2] == 0.0, terms
        checked += 1
    assert checked == 6     # three conferees through each of the conferrer's two seats
    # another verb's candidate reads no fit term even at weight 1.0: the term follows the row's shape, not a verb name
    fx1 = w.fixtures.sweep("confer_fit_weight", 1.0)
    other = [c for c in CH.opening_set(p, view, q, fx1) if c.verb != "confer" and c.operands.get("to")]
    assert other, "control: some other verb forms with a `to`"
    assert all(CH.score_terms(p, c, fx1, CH.deliberation_memo(p, fx1))[2] == 0.0 for c in other)


def test_believed_capability_reads_the_latest_held_claim_and_none_otherwise():
    king = _vacancy_world().persons["p_king"]
    assert person_q.believed_capability(king, "p_low", "law") is None  # no claim on `main` carries another's skill
    assert sigma.CAPABILITY_CLAIM == person_q.CAPABILITY_CLAIM  # one owner for the predicate stem

    def claim(i, subject, key, value, when, lap=0, confidence=100):
        return Claim(f"c_cap{i}", "p_king", subject, person_q.CAPABILITY_CLAIM + key, value, when, "told", confidence,
                     "own", lap)
    king.ledger.extend([claim(1, "p_low", "law", 2, when=0), claim(2, "p_low", "law", 5, when=1),
                        claim(3, "p_low", "law", 3, when=1, confidence=40),
                        claim(4, "p_low", "arms", 9, when=3), claim(5, "p_mid", "law", 7, when=3)])
    assert person_q.believed_capability(king, "p_low", "law") == 5   # the latest by (when, lap, confidence)
    assert person_q.believed_capability(king, "p_mid", "law") == 7
    assert person_q.believed_capability(king, "p_low", "arms") == 9
    assert person_q.believed_capability(king, "p_king", "law") is None


def test_a_seat_naming_a_skill_lifts_the_candidate_the_conferrer_believes_holds_it(monkeypatch):
    """The believed half, with a claim planted (nothing deposits one): a seat row naming `law`, the conferrer believing
    himself holds it at 30 and regarding `p_mid` higher. At weight 1.0 the believed skill outweighs the stance on
    `p_mid`; at 0.0 neither is read. Control: with no seat row naming the skill the same claim is not read."""
    w = _vacancy_world()
    w.persons["p_king"].ledger.append(Claim("c_cap", "p_king", "p_king", person_q.CAPABILITY_CLAIM + "law", 30, 0, "told",
                                            100, "own"))
    assert _conferees(w, 1.0)[0] == "p_mid"
    monkeypatch.setitem(rosters.SEAT_ROW_BY_ID, _OFFICE, {"id": _OFFICE, "capability": "law"})
    assert _conferees(w, 1.0)[0] == "p_king"
    assert _conferees(w, 0.0)[0] == "p_low"
