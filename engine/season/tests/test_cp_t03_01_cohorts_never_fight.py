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
  CONTROL: `build_realm(seed)`, two seasons, shipped chooser: at seeds 0 and 2 no act was refused on `individual`, and
  the realm ends at the base's `content_hash` once the conjunct's own reads are left off `Event.observed` (they are
  hashed: the raw hash moves wherever a `fight`/`accept` cleared the clauses before it). At seed 1 a cohort was a party
  on the base (`p_npc_007` felled by one), the conjunct refuses it, and the realm moves.
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
from ..state.carriers import Act, Scene
from ..state.ids import H, draw_factory

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
                           payload={"subject": subject})])]

    fired: list = []
    choose = dispatching_chooser(P.NOCHOOSE, {actor: act} if verb else {})
    _run_seasons(d, w, choose, 1)
    if verb:
        assert fired, "the hand-built act was never asked for: the falsifier observed nothing"
    return w, d


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

#: `build_realm(seed).content_hash()` after two seasons of the shipped chooser on the base before this position
#: (B10-10b's close). Re-take, do not edit: the control is that the realm still ends here wherever no cohort was a party.
BASE = {0: "be2c7f0f1d82d8f785a43f14b1273c2c",
        1: "3010c440922c4d899f9533446ae38431",
        2: "6df7a66eedb89b806763cd1ab903d1dd"}


def _individual_reads(e):
    return [o for o in (e.observed or ()) if str(o.predicate).startswith("individual:")]


def _realm_two_seasons(seed):
    """Two seasons of the shipped chooser on `build_realm(seed)`. Returns `(content_hash with the `individual` reads left
    off every Event's `observed`, how many such reads there were, how many Events a False one refused)`.

    ⚠ WHY THE READS ARE LEFT OFF: `World.content_hash` folds `Event.observed`, and the new conjunct is READ (True) by
    every `fight`/`accept` that clears the clauses before it, so the raw hash moves in a realm where nothing else did.
    The reads are the only thing that moves it there; the control strips them and compares the rest."""
    w = build_realm(seed)
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    choose = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw_factory(w.world_seed, lambda: w.tick))
    _run_seasons(d, w, choose, 2)
    reads = refused_on_it = 0
    for e in w.log:
        mine = _individual_reads(e)
        if not mine:
            continue
        reads += len(mine)
        refused_on_it += any(o.value is False for o in mine)
        object.__setattr__(e, "observed", tuple(o for o in e.observed if o not in mine))
    return w.content_hash(), reads, refused_on_it


@pytest.mark.parametrize("seed", [0, 2])
def test_control_the_realm_ends_at_the_base_hash_wherever_no_cohort_was_a_party(seed):
    """Seeds 0 and 2: no `fight`/`accept` was refused by the conjunct, so with its reads left off the realm ends at the
    base's hash. `reads` is asserted, so the equality cannot hold because the conjunct was never evaluated."""
    h, reads, refused_on_it = _realm_two_seasons(seed)
    assert reads > 0, "the conjunct was never read: the equality below observes nothing"
    assert refused_on_it == 0, f"{refused_on_it} Events were refused on `individual` at seed {seed}"
    assert h == BASE[seed], "the conjunct moved a realm in which no cohort was a party"


def test_where_a_cohort_was_a_party_the_realm_moves_and_the_refusals_are_the_conjuncts():
    """Seed 1: `p_npc_007` fought (and was felled by) a cohort on the base. The same seed now refuses that act on
    `individual`, and the realm ends elsewhere -- the mover the position declares."""
    h, reads, refused_on_it = _realm_two_seasons(1)
    assert refused_on_it > 0, "no act was refused on `individual` at seed 1"
    assert h != BASE[1], "a cohort-party fight was refused and the realm did not move"
