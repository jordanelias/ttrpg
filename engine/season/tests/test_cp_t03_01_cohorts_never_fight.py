"""CP-T03-01 -- A COHORT IS NEVER A PARTY TO A PERSONAL FIGHT (the `individual` stem and its two conjuncts).

`data/requires.py::REQUIRES_STEMS` gains `individual` (WORLD-ONLY, answered by `queries/world_q.py::WorldReader.read`
from `Person.is_cohort`, `weight > 1`), and `verb_table.yaml`'s `fight` and `accept` rows carry it as a typed
`relation` conjunct on BOTH parties (`of: subject`, `of: actor`), refused with the row's one kind (`kill.refused`,
`accept.refused`).

  FALSIFIER: a hand-built `fight` on a cohort, returned through `harness/play_surface.py::dispatching_chooser`, is
  refused with the row's kind and leaves the cohort's `weight`, `body` and tenures exactly as a season in which nobody
  chose anything leaves them; the same `fight` on a weight-1 person is admitted. `accept` is the same row, same cell.
  The cohort as the ACTOR is refused the same way (the conjunct is on both parties).
  MUTATION (run by hand at the build, reported in the commit body): drop the two `individual` conjuncts from `fight`
  and `accept` and the cohort is removed -- `test_a_cohort_..._is_refused_and_untouched` goes red on the first
  assertion that reads the refusal kind, and the `weight` / `Person.exists` reads follow.
  CONTROL: `build_realm(seed)`, two seasons, with `challenge`, `accept` and `capture` withheld from the chooser: at seed 2
  a cohort was a party (`p_npc_007` felled by one) and the conjunct refuses an act on `individual`. The realm's hash is
  `_realm_goldens.py`'s, the one owner: this file pins none. The hand-built `accept` here binds a planted challenge whose
  challenger is the act's opponent (`to`).
"""
from __future__ import annotations

import pytest

from ..harness import probes as P
from ..harness.play_surface import dispatching_chooser
from ..harness.populated import build_realm
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..data.requires import CELL_STEMS, REQUIRES_STEMS, WORLD_ONLY_STEMS, UNKNOWN
from ..data.verbs import VERB_TABLE
from ..decision import make_chooser
from ..queries import world_q
from ..state.carriers import Act, Record, Scene
from ..state.ids import H, draw_factory
from .test_cp_t03_04_arms import revert_cp_t03_04
from .test_cp_t03_08_tend_on_the_wounded import revert_cp_t03_08
from .test_cr87_violence_contexts import revert_cr87

CROWD, FIGHTER, FOE = "c_crowd", "p_low", "p_mid"       # `tiny_world`: p_low and p_mid live at the hearth `Hh`
KINDS = {"fight": "kill.refused", "accept": "accept.refused"}


def _world():
    """`tiny_world` with a cohort (weight 3) at the fighter's hearth, one pass per round (`probes._one_pass`)."""
    w = P.tiny_world()
    P.plant_cohort(w, CROWD, "Hh", weight=3)
    return P._one_pass(w)


def _state(w, pid):
    """What a fight could change of `pid`: whether he stands, his weight and body, and every edge naming him."""
    p = w.persons.get(pid)
    edges = tuple(sorted((t.id, t.kind, t.subject, t.object, t.since, t.until) for t in w.tenures
                         if t.subject == pid or t.object == pid))
    return (None if p is None else (p.weight, p.body)), edges


def _run_seasons(d, w, choose, n):
    """`n` seasons. An exception from the engine is turned into a FAILED ASSERTION naming it: a test here fails by
    assertion, never by a traceback out of the code under test."""
    try:
        for _ in range(n):
            d.season(choose, question=None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    except Exception as e:                                   # noqa: BLE001
        raise AssertionError(f"the season raised {type(e).__name__}: {e}") from None


def _season(verb=None, actor=FIGHTER, subject=FOE):
    """One season of `_world()` in which `actor` is handed ONE hand-built `verb` act on `subject` through
    `dispatching_chooser` (every other person chooses nothing). `verb=None` is the control: nobody chooses."""
    w = _world()
    d = SeasonDriver(w)

    def act(p, v, s, ask_budget, auto):
        if fired:
            return []
        fired.append(1)
        return [Scene(H(w.world_seed, w.tick, p.id, "scene:cp_t03_01"), p.id,
                      [Act(H(w.world_seed, w.tick, p.id, f"act:{verb}:{subject}"), p.id, verb,
                           payload=_payload(w, verb, actor, subject))])]

    fired: list = []
    choose = dispatching_chooser(P.NOCHOOSE, {actor: act} if verb else {})
    _run_seasons(d, w, choose, 1)
    if verb:
        assert fired, "the hand-built act was never asked for: the falsifier observed nothing"
    return w, d


def _payload(w, verb, actor, opponent):
    """The hand-built act's payload. `fight`: the opponent is `subject`. `accept` (v10 PC-10b): the act binds a
    `challenge` Record whose challenger is the opponent and whose `terms` is the actor -- planted here as a held
    document would stand -- and the opponent rides `to`, the row's counterparty."""
    if VERB_TABLE[verb].opponent_operand() == "subject":
        return {"subject": opponent}
    rid = f"rec:challenge:{opponent}:{actor}"
    w.records[rid] = Record(rid, "Hh", "challenge",
                            subject_matter={"terms": actor, "to": [actor], "stakes": None, "challenger": opponent})
    return {"subject": rid, "to": opponent}


def _kinds(w):
    return [e.kind for e in w.log]


@pytest.mark.parametrize("verb", sorted(KINDS))
def test_a_cohort_subject_is_refused_with_the_rows_kind_and_untouched(verb):
    ref = KINDS[verb]
    assert VERB_TABLE[verb].emits_on_refusal == (ref,)
    control, _ = _season(None)
    w, d = _season(verb, subject=CROWD)
    assert ref in _kinds(w), (verb, _kinds(w))
    assert f"{verb}.declared" not in _kinds(w), "the fight was declared on a cohort"
    assert not any(a.verb == verb for a in d.resolved), "a fight on a cohort reached the fold's resolved set"
    assert CROWD in w.persons, "the cohort was removed"
    for k in ("person.died", "body.changed"):       # the season's own MATTER writes the same in the control arm
        assert _kinds(w).count(k) == _kinds(control).count(k), (verb, k)
    assert _state(w, CROWD) == _state(control, CROWD), "a refused fight changed the cohort"
    assert getattr(w.persons.get(CROWD), "weight", None) == 3


@pytest.mark.parametrize("verb", sorted(KINDS))
def test_a_cohort_actor_is_refused_the_same_way(verb):
    """The conjunct is on BOTH parties: a cohort handed the act (the callback is bound to the cohort's id)."""
    ref = KINDS[verb]
    control, _ = _season(None)
    w, _d = _season(verb, actor=CROWD, subject=FOE)
    assert ref in _kinds(w) and f"{verb}.declared" not in _kinds(w), (verb, _kinds(w))
    assert _state(w, CROWD) == _state(control, CROWD) and _state(w, FOE) == _state(control, FOE)


@pytest.mark.parametrize("verb", sorted(KINDS))
def test_a_person_of_weight_one_is_admitted(verb):
    """The control of the two above: the same act, the same hearth, the same chooser, on a weight-1 person."""
    w, d = _season(verb, subject=FOE)
    before = _world()
    assert before.persons[FIGHTER].weight == 1 and before.persons[FOE].weight == 1
    assert f"{verb}.declared" in _kinds(w), (verb, _kinds(w))
    assert KINDS[verb] not in _kinds(w), (verb, _kinds(w))
    assert any(a.verb == verb for a in d.resolved)


def test_the_stem_is_answered_from_is_cohort_and_is_world_only():
    w = _world()
    assert "individual" in REQUIRES_STEMS and "individual" in WORLD_ONLY_STEMS
    assert "individual" not in CELL_STEMS, "a cell stem would be deposited into every witness's ledger"
    reader = world_q.WorldReader(w, FIGHTER)
    checked = 0
    for pid, p in w.persons.items():
        assert reader.read(pid, f"individual:{FIGHTER}") is (not p.is_cohort), pid
        checked += 1
    assert checked == len(w.persons) and w.persons[CROWD].is_cohort
    assert reader.read("no_such_person", f"individual:{FIGHTER}") is UNKNOWN
    for verb in KINDS:
        typed = VERB_TABLE[verb].requires_typed
        assert typed is not None and "individual" in typed.stems(), verb


# --- THE CONTROL ---------------------------------------------------------------------------------

#: The verbs this control's chooser never offers: `capture` (CP-T03-09) and the duel pair PC-10b re-shaped.
WITHHELD = frozenset({"capture", "challenge", "accept"})


def _individual_reads(e):
    return [o for o in (e.observed or ()) if str(o.predicate).startswith("individual:")]


def _realm_two_seasons(seed):
    """Two seasons of the shipped chooser on `build_realm(seed)`. Returns `(how many `individual` reads there were, how
    many Events a False one refused)`."""
    w = build_realm(seed)
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    # v10 CP-T03-09: `capture` is WITHHELD FROM THE CHOOSER HERE. It forms for the seats granting `dispatch` and moves every
    # realm (its own mover, declared in its commit), so with it offered the base below -- taken before `capture` existed --
    # would be compared against a different trajectory; the control is the `individual` conjunct's, and this keeps it so.
    # v10 PC-10b: `challenge` and `accept` too -- PC-10b re-shaped the duel pair (a Record, a new cell), a mover of its own.
    choose = make_chooser(w.fixtures, mint, verbs=resolvable_verbs() - WITHHELD,
                          draw=draw_factory(w.world_seed, lambda: w.tick))
    _run_seasons(d, w, choose, 2)
    reads = refused_on_it = 0
    for e in w.log:
        mine = _individual_reads(e)
        if not mine:
            continue
        reads += len(mine)
        refused_on_it += any(o.value is False for o in mine)
    return reads, refused_on_it


def test_where_a_cohort_was_a_party_the_realm_moves_and_the_refusals_are_the_conjuncts(monkeypatch):
    """Seed 2 (since PC-10b's re-take, under `WITHHELD`; seed 1 before it): a cohort was a party on the pre-conjunct base.
    The same seed now refuses that act on `individual` -- the mover the position declares; the realm's hash is
    `_realm_goldens.py`'s. Read with CR-87 at its revert (CR-87's contexts leave no `fight` formed in these realms, so the
    conjunct would never be read) and (v11) CP-T03-04's formation mover at its revert, so the seed forms the cohort-party
    act it was measured on."""
    revert_cr87(monkeypatch)
    revert_cp_t03_04(monkeypatch)
    # v11 CP-T03-08 (`tend` forms on the wounded, a formation mover of every season) moves seed 2's second season off the
    # cohort-party act (MEASURED: 0 refusals on `individual` with it live), so it is read at its revert too, the same way.
    revert_cp_t03_08(monkeypatch)
    from .test_b11a_duel_reach import revert_b11a
    revert_b11a(monkeypatch)   # B11 lane A (the duel chain's reach, a formation mover of every season), the same way
    from .test_b11a_scores_and_obstacle import revert_b11a_scores
    revert_b11a_scores(monkeypatch)   # B11 lane A (persons hold scores; the obstacle by task: a mover of the build and every season), the same way
    reads, refused_on_it = _realm_two_seasons(2)
    assert refused_on_it > 0, "no act was refused on `individual` at seed 2"
