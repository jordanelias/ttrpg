"""v10 PC-10b (RS-25; H-240 route (1)) -- A CHALLENGE IS A RECORD, `accept` BINDS TO IT, AND A DUEL MAY END IN A YIELD.

`challenge` mints a `challenge` Record (`rosters.yaml: record_kinds`: `terms` the challenged, `to` the same person as
addressee, `stakes` the duel's term, `challenger` the actor) through `_eff_challenge`. `accept` declares
`referent_class: Record`, `counterparty: to`, and a cell asking `exists:challenge` and the new `names:<operand>` stem
(`data/requires.py`, WORLD-ONLY): `names:to` -- the Record's `challenger` is the opponent -- and `names:actor` -- its
`terms` is the acceptor. The duel is fought under the Record's `stakes`, through CP-T03-09's ONE path
(`seam/wrappers/combat.py::combat_input` -> `PersonalCombatInput.terms`), `'death'` where it names none; the yield rides
the result (`surrender`), earning `duel.yielded` for the yielder alone, never a band (H-98).

  FALSIFIER: a seeded `blood` challenge resolves with `surrender` set; under `death` Felled stays reachable; the
  Record's `stakes` holds the term and `terms` the person (the key split); an `accept` with no challenge behind it is
  refused AT ITS CELL, before any draw; a hand-built `accept` on a challenge reaches the seam with two Person claimants;
  a `blood` duel whose first wound is not decisive emits `duel.yielded` and no `person.died` (seeds picked as
  `tests/valoria/test_combat_duel_terms.py::_blood_cases` picks them -- no universal is asserted); a yield read as a
  fourth band fails.
  PLANTED FAILURE: the `names` conjuncts deleted, a no-challenge `accept` executes.
  CONTROLS: no challenge Record -> `accept` refuses; `stakes: death` (and no stakes) builds today's duel exactly; an
  unchallenged `fight` between the same pair stays lethal; `challenge_terms` equals the engine's `DUEL_TERMS` (a test,
  never an import into `engine/season/data`).
"""
from __future__ import annotations

import dataclasses
import pathlib
import types
from unittest import mock

import pytest

from ..data import requires as REQ
from ..data.matrix import Step, WriteClass
from ..data.requires import CELL_STEMS, REQUIRES_STEMS, UNKNOWN, WORLD_ONLY_STEMS, Relation, build_typed_requires
from ..data.rosters import CHALLENGE_TERMS, COMBAT_BANDS
from ..data.verbs import KIND_VERB, RECORD_REFERENT_KINDS, VERB_TABLE
from ..gaps import Forbidden
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..queries import world_q
from ..seam.wrappers import combat
from ..state.carriers import Act, Office, Record, Tenure

ACC, CHAL, THIRD = "p_low", "p_mid", "p_other"     # tiny_world: all three live at the hearth `Hh`
TRIES = 80                                            # accept act ids scanned for a scene of a given shape


def _world():
    w = P.tiny_world()
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _run(w, d, *acts):
    """RESOLVE then ENCOUNTER (`the body` is fought at ENCOUNTER), logged as a season does."""
    depth = w.fixtures.get("contest_max_depth")
    w.step, w.frozen = Step.RESOLVE, False
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts), depth)
    out = out + d.encounter(mint_token(w, WriteClass.ACTS), out, depth)
    w.log.extend(out)
    return out


def _kinds(events):
    return [e.kind for e in events]


def _challenge(stakes=None, actor=CHAL, subject=ACC, aid="ch0"):
    payload = {"subject": subject} if stakes is None else {"subject": subject, "stakes": stakes}
    return Act(id=aid, actor=actor, verb="challenge", payload=payload)


def _accept(i, record="rec:ch0", to=CHAL, actor=ACC):
    return Act(id=f"acc{i}", actor=actor, verb="accept", payload={"subject": record, "to": to})


def _challenged(stakes=None):
    """A world in which `CHAL` has challenged `ACC` (a real `challenge` act through the fold)."""
    w, d = _world()
    out = _run(w, d, _challenge(stakes))
    assert _kinds(out) == ["challenge.issued"], _kinds(out)
    return w, d


class _Spy:
    """Records every scene the personal-combat entry fights: the typed input and the module's return. Wraps
    `combat.entry_for`, the module global `combat.resolve` reads at call time, so the fold's own path is observed."""

    def __init__(self):
        self.calls = []
        self._real = combat.entry_for

    def __call__(self, prize, module, *rest):
        entry, refusal = self._real(prize, module, *rest)
        if entry is None:
            return entry, refusal

        def fn(inp, rng, **kw):
            got = entry.fn(inp, rng, **kw)
            self.calls.append((inp, got))
            return got
        return types.SimpleNamespace(fn=fn), refusal

    def patch(self):
        return mock.patch.object(combat, "entry_for", self)


def _first_wound_not_decisive(trace) -> bool:
    """`_blood_cases`' test on the season's own scene: the lethal control's FIRST wound fells nobody and the fight runs
    at least one more turn after it -- so a duel stopped by `blood` there is observably a yield, not a felling."""
    k = next((i for i, e in enumerate(trace) if e.get("kind") == "wound"), None)
    if k is None or trace[k].get("felled"):
        return False
    return any(e.get("kind") == "turn_start" for e in trace[k + 1:])


# ---------------------------------------------------------------------------------------------------------------
# 1 -- THE ROSTER, THE STEM, THE ROW
# ---------------------------------------------------------------------------------------------------------------

def test_challenge_terms_equal_the_engines_duel_terms_by_test_and_no_season_data_module_imports_the_engine():
    engine = combat.engine()
    assert engine is not None, combat.load_error()
    assert set(CHALLENGE_TERMS) == set(engine[0].DUEL_TERMS), (CHALLENGE_TERMS, engine[0].DUEL_TERMS)
    data_dir = pathlib.Path(REQ.__file__).parent
    offenders = [p.name for p in data_dir.glob("*.py") if "DUEL_TERMS" in p.read_text()
                 and ("modules.combat" in p.read_text() or "import wrapper" in p.read_text())]
    assert offenders == [], offenders


def test_names_is_a_world_only_grammar_stem_and_not_a_cell():
    assert "names" in REQUIRES_STEMS and "names" in WORLD_ONLY_STEMS and "names" not in CELL_STEMS
    assert REQ.OPERAND_NAMED_STEMS == frozenset({"names"})


def test_the_operand_named_shape_is_closed_to_its_stems():
    rel = Relation("subject", "names:to")
    assert rel.operands() == ("subject", "to") and rel.stems() == ("names",)
    with pytest.raises(SystemExit):
        Relation("subject", "names")                 # the stem needs its operand
    with pytest.raises(SystemExit):
        Relation("to", "with:to")                    # a bare stem may not name one
    with pytest.raises(SystemExit):                  # an operand outside the closed roster refuses at load
        build_typed_requires("accept", {"form": "relation", "of": "subject", "relation": "names:nobody"})


def test_the_accept_row_binds_a_challenge_record_against_the_opponent_on_to():
    row = VERB_TABLE["accept"]
    assert row.referent_class == "Record" and row.referent_named and row.counterparty == "to"
    assert row.opponent_operand() == "to"
    assert set(row.requires_typed.stems()) == {"exists", "names", "with", "individual"}
    assert "accept" in resolvable_verbs()
    assert RECORD_REFERENT_KINDS == frozenset({"dispensation", "challenge"})
    assert VERB_TABLE["challenge"].writes == ("Record.exists",)
    assert KIND_VERB["duel.yielded"] == "accept"


def test_a_yield_is_not_a_fourth_band():
    """H-98: the yield rides the result. `accept`'s bands are `fight`'s, the band roster carries no yield, and only
    `Wounded` declares `duel.yielded` (a standing yielder reads his own tracker)."""
    acc, fgt = VERB_TABLE["accept"], VERB_TABLE["fight"]
    assert set(acc.emits_by_degree) == set(fgt.emits_by_degree) == set(acc.writes_by_degree)
    assert not any("yield" in b.lower() for b in COMBAT_BANDS), COMBAT_BANDS
    assert [b for b, ks in acc.emits_by_degree.items() if "duel.yielded" in ks] == ["Wounded"]


# ---------------------------------------------------------------------------------------------------------------
# 2 -- THE RECORD
# ---------------------------------------------------------------------------------------------------------------

def test_a_challenge_mints_a_record_whose_stakes_hold_the_term_and_whose_terms_hold_the_person():
    w, _ = _challenged("blood")
    rec = w.records["rec:ch0"]
    assert rec.kind == "challenge"
    assert rec.subject_matter == {"terms": ACC, "to": [ACC], "stakes": "blood", "challenger": CHAL}
    assert world_q.stakes_of(w, rec.id) == "blood" != rec.subject_matter["terms"]     # the key split
    assert any(t.kind == "hold" and t.subject == CHAL and t.object == rec.id and t.live for t in w.tenures)


def test_a_computed_challenge_names_no_stakes_and_its_duel_is_fought_at_death():
    w, _ = _challenged(None)
    assert w.records["rec:ch0"].subject_matter["stakes"] is None
    assert world_q.stakes_of(w, "rec:ch0") is None
    assert combat.combat_input(w, [ACC, CHAL], "accept", "rec:ch0").terms == "death"


def test_a_stakes_outside_the_roster_is_refused_naming_it():
    w, d = _world()
    with pytest.raises(Forbidden) as e:
        _run(w, d, _challenge("mercy"))
    assert "challenge_terms" in str(e.value)
    assert "rec:ch0" not in w.records


def test_writs_held_stamps_a_held_addressed_challenge_and_the_audience_limb_does_not_open_on_it():
    w, _ = _challenged("blood")
    w.add_tenure(Tenure("t_given", ACC, "rec:ch0", "hold", since=w.tick))        # as a `give` would leave it
    assert world_q.writs_held(w, w.persons[ACC]) == ("rec:ch0",)
    seat = "off_duke"                                                            # its purview reaches the hearth
    with mock.patch.object(world_q, "guard_weight", lambda *_: 1), \
            mock.patch.object(world_q, "governors_of", lambda *_: ()):
        with mock.patch.object(world_q, "_creating_act",
                               lambda *_: Act(id="x", actor=CHAL, verb="challenge", via=seat)):
            assert world_q.admits_audience(w, ACC, "Hh") is False
        # CONTROL: the same held Record read as minted by `issue` through that seat opens the limb
        with mock.patch.object(world_q, "_creating_act",
                               lambda *_: Act(id="x", actor=CHAL, verb="issue", via=seat)):
            assert world_q.admits_audience(w, ACC, "Hh") is True


# ---------------------------------------------------------------------------------------------------------------
# 3 -- THE REFUSALS, AT THE CELL, BEFORE ANY DRAW
# ---------------------------------------------------------------------------------------------------------------

def _refuses_before_any_scene(w, d, act):
    spy = _Spy()
    with spy.patch():
        out = _run(w, d, act)
    assert _kinds(out) == ["accept.refused"], _kinds(out)
    assert spy.calls == [], "a scene was fought for an accept the cell refuses"
    return out


def test_control_no_challenge_record_an_accept_is_refused_at_its_cell():
    w, d = _world()
    out = _refuses_before_any_scene(w, d, _accept(0, record="rec:none"))
    assert any(o.predicate == "exists:challenge" for o in out[0].observed)
    # the pre-PC-10b shape -- a PERSON as the subject -- is refused the same way
    _refuses_before_any_scene(w, d, Act(id="acc_old", actor=ACC, verb="accept", payload={"subject": CHAL, "to": CHAL}))
    assert ACC in w.persons and CHAL in w.persons


def test_an_accept_against_someone_who_never_challenged_is_refused_on_names_to():
    w, d = _challenged("blood")
    out = _refuses_before_any_scene(w, d, _accept(0, to=THIRD))
    assert any(o.predicate == f"names:to:{THIRD}" and o.value is False for o in out[0].observed)


def test_an_accept_by_someone_the_record_does_not_challenge_is_refused_on_names_actor():
    w, d = _challenged("blood")
    out = _refuses_before_any_scene(w, d, _accept(0, actor=THIRD))
    assert any(o.predicate == f"names:actor:{THIRD}" and o.value is False for o in out[0].observed)


def test_planted_failure_the_names_conjuncts_deleted_lets_a_no_challenge_accept_execute():
    """The mutant cell is `accept`'s less its two `names` conjuncts. The SAME no-challenge `accept` (the challenge is
    `CHAL`'s; the acceptor fights `THIRD`, who never challenged) is refused on the shipped cell and fought on the
    mutant -- so the stem is what refuses it."""
    row = VERB_TABLE["accept"]
    clauses = [c for c in row.requires_typed.requirement.clauses
               if not (isinstance(c, Relation) and c.stems() == ("names",))]
    assert len(clauses) == len(row.requires_typed.requirement.clauses) - 2
    mutant = dataclasses.replace(row, requires_typed=REQ.TypedRequires(REQ.AllOf(tuple(clauses))))
    w, d = _challenged("blood")
    _refuses_before_any_scene(w, d, _accept(0, to=THIRD))
    w, d = _challenged("blood")
    spy = _Spy()
    with mock.patch.dict(VERB_TABLE, {"accept": mutant}), spy.patch():
        out = _run(w, d, _accept(1, to=THIRD))
    assert "accept.refused" not in _kinds(out) and "accept.declared" in _kinds(out), _kinds(out)
    assert [inp.claimants for inp, _ in spy.calls] == [(ACC, THIRD)]


# ---------------------------------------------------------------------------------------------------------------
# 4 -- THE DUEL: TWO PERSONS, THE TERMS, THE YIELD
# ---------------------------------------------------------------------------------------------------------------

def test_a_hand_built_accept_on_a_challenge_reaches_the_seam_with_two_person_claimants():
    w, d = _challenged("blood")
    spy = _Spy()
    with spy.patch():
        out = _run(w, d, _accept(0))
    assert "accept.refused" not in _kinds(out) and "accept.declared" in _kinds(out), _kinds(out)
    assert len(spy.calls) == 1, "no scene, or more than one"
    inp, got = spy.calls[0]
    assert inp.claimants == (ACC, CHAL) and all(c in w.persons or c in (ACC, CHAL) for c in inp.claimants)
    assert got["status"] == "RESOLVED" and inp.terms == "blood"


def _scan(stakes):
    """`[(act index, scene input, scene return, events)]` for `TRIES` accepts, each on a fresh challenged world."""
    out = []
    for i in range(TRIES):
        w, d = _challenged(stakes)
        spy = _Spy()
        with spy.patch():
            evs = _run(w, d, _accept(i))
        assert len(spy.calls) == 1, (i, _kinds(evs))
        out.append((i, spy.calls[0][0], spy.calls[0][1], evs, w))
    return out


def test_a_seeded_blood_challenge_resolves_with_surrender_set():
    scenes = _scan("blood")
    assert all(inp.terms == "blood" for _, inp, _, _, _ in scenes)
    yielded = [i for i, _, got, _, _ in scenes if combat.surrender_of(got["trace"]) is not None]
    assert yielded, "no blood duel in the scan stopped on its term: the falsifier observed nothing"


def test_under_death_felled_stays_reachable_and_no_duel_yields():
    scenes = _scan("death")
    assert all(inp.terms == "death" for _, inp, _, _, _ in scenes)
    assert any("person.died" in _kinds(evs) for _, _, _, evs, _ in scenes), "no death under lethal terms"
    assert not any("duel.yielded" in _kinds(evs) for _, _, _, evs, _ in scenes)


def test_a_blood_duel_whose_first_wound_is_not_decisive_emits_duel_yielded_and_no_death():
    """Seeds picked on the LETHAL CONTROL of the same act (`stakes: death`, the same scene seed): its first wound fells
    nobody and the fight goes on. Under `blood` the same act then yields -- no universal is asserted for the rest."""
    lethal = {i: got for i, _, got, _, _ in _scan("death")}
    picked = [i for i, got in lethal.items() if _first_wound_not_decisive(got["trace"])]
    assert picked, "no scene with a non-decisive first wound in the scan: the falsifier observed nothing"
    checked = 0
    for i, inp, got, evs, w in _scan("blood"):
        if i not in picked:
            continue
        ks = _kinds(evs)
        assert "duel.yielded" in ks and "person.died" not in ks, (i, ks)
        assert ACC in w.persons and CHAL in w.persons
        yielder = combat.surrender_of(got["trace"])["by"]
        ev = next(e for e in evs if e.kind == "duel.yielded")
        assert ev.degree == "Wounded", ev.degree                                  # a band, not a fourth one
        assert {c.subject for c in ev.changes} == {yielder}, "the yield was earned by someone who did not yield"
        checked += 1
    assert checked == len(picked) >= 1


def test_control_stakes_death_and_no_stakes_build_todays_duel_exactly():
    """The record a death-stakes (or a stakes-less) challenge's `accept` builds is the record a lethal `fight` between
    the pair builds -- the input the scene is drawn from, so the duel is today's."""
    for stakes in ("death", None):
        w, _ = _challenged(stakes)
        assert (combat.combat_input(w, [ACC, CHAL], "accept", "rec:ch0")
                == combat.combat_input(w, [ACC, CHAL], "fight")), stakes


def test_control_an_unchallenged_fight_between_the_same_pair_stays_lethal():
    w, d = _challenged("blood")
    spy = _Spy()
    with spy.patch():
        _run(w, d, Act(id="f0", actor=ACC, verb="fight", payload={"subject": CHAL}))
    assert [inp.terms for inp, _ in spy.calls] == ["death"]


def test_the_names_reader_answers_off_the_one_map():
    w, _ = _challenged("yield")
    assert world_q.record_names(w, "rec:ch0", "to", CHAL) is True
    assert world_q.record_names(w, "rec:ch0", "to", ACC) is False
    assert world_q.record_names(w, "rec:ch0", "actor", ACC) is True
    assert world_q.record_names(w, "rec:ch0", "from", CHAL) is UNKNOWN             # the kind maps no `from`
    assert world_q.record_names(w, "rec:none", "to", CHAL) is UNKNOWN
    w.records["rec:writ"] = Record("rec:writ", "Hh", "dispensation",
                                   subject_matter={"terms": ACC, "to": [CHAL], "at": None})
    assert world_q.record_names(w, "rec:writ", "to", CHAL) is True                  # an addressee list names each
