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
  ⚠ v10 PC-10b RE-TOOK THE CONTROL (`BASE`, below): `accept` now binds a `challenge` Record and `challenge` mints one, so
  with `challenge`/`accept` offered the realm walks another trajectory from the pre-conjunct base. They are withheld from
  the chooser with `capture` (CP-T03-09's precedent), and the base is re-taken on the tree before CP-T03-01 (`778981ed~1`)
  under the same withholding: seeds 0 and 1 now refuse nothing on `individual` and end at it; seed 2 refuses one act and
  moves. The hand-built `accept` here binds a planted challenge whose challenger is the act's opponent (`to`).
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
from .test_cp_t03_02_band_ending_and_body import revert_cp_t03_02
from .test_cr85_faculty_replaces_history import revert_cr85
from .test_cp_t03_04_arms import revert_cp_t03_04
from .test_cp_t03_07_body_ceiling import revert_cp_t03_07
from .test_cp_t03_08_tend_on_the_wounded import revert_cp_t03_08
from .test_cp_t05_02_self_plea import revert_cp_t05_02
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

#: `build_realm(seed).content_hash()` after two seasons of the shipped chooser on the base before this position
#: (B10-10b's close). Re-take, do not edit: the control is that the realm still ends here wherever no cohort was a party.
#: ⚠ RE-TAKEN AT v10 PC-10b, on the tree before CP-T03-01 (`778981ed~1`), with `capture`, `challenge` and `accept` withheld from
#: the chooser (`WITHHELD`): was be2c7f0f... / 3010c440... / 6df7a66e... (taken with `challenge`/`accept` offered, which PC-10b
#: moves). The same withholding on the CP-T03-09 tree (`95f58adb`) and on PC-10b's reads the identical stripped hashes at all
#: three seeds (aa4cc67d... / 8ac99151... / 3cf9a0a6...), so PC-10b moves nothing where no duel verb is chosen.
#: ⚠ RE-TAKEN ONCE MORE by the B10-11b batch pin commit (`reading @4b334f2a`), seeds 0 and 1 (was aa4cc67d... / 8ac99151...):
#: PC-20 (1) (the head-weighted strike impact, `K_STR_HEAD`) moves a run that reaches `strike_impact`, and these two-season
#: realms reach it. `reads > 0` and `refused_on_it == 0` still hold, so the conjunct moved no realm; the hash is the trajectory's.
BASE = {0: "4704d8a6ba7fc84ff6801a2481823501",
        1: "b6f1c2939725849b51dad3af3791df25",
        2: "d1594dae7a962dc9bbe9e6a1de9abb91"}
#: The verbs this control's chooser never offers: `capture` (CP-T03-09) and the duel pair PC-10b re-shaped.
WITHHELD = frozenset({"capture", "challenge", "accept"})


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
        object.__setattr__(e, "observed", tuple(o for o in e.observed if o not in mine))
    return w.content_hash(), reads, refused_on_it


@pytest.mark.parametrize("seed", [0, 1])
def test_control_the_realm_ends_at_the_base_hash_wherever_no_cohort_was_a_party(seed, monkeypatch):
    """Seeds 0 and 1 (since PC-10b's re-take; 0 and 2 before it): no `fight`/`accept` was refused by the conjunct, so with its reads left off the realm ends at the
    base's hash. `reads` is asserted, so the equality cannot hold because the conjunct was never evaluated.
    ⚠ v11 CR-87 RE-TOOK IT ON THE WORLD IT WAS MEASURED ON: CR-87's contexts leave no `fight` formed in these realms, so the
    conjunct would never be read and the control would observe nothing; it is read with CR-87 at its revert
    (`test_cr87_violence_contexts.py::revert_cr87`, whose own control reproduces the pre-CR-87 hash), and `BASE` stands.
    ⚠ v10 CP-T03-02 (the band's `ending` and the body Observation, a later mover of every realm that fought) is reverted
    too (`revert_cp_t03_02`), the same way, so `BASE` stands rather than being re-taken.
    ⚠ v11 CR-85 (`faculty` replaces `history` in the pool and the Ob, a later mover of every realm that fought) is
    reverted too (`revert_cr85`), the same way.
    ⚠ v11 CP-T03-04 (`arms` in the vocation range, a formation mover of every realm) is reverted too
    (`revert_cp_t03_04`), the same way, and v11 CP-T03-07 (`body_ceiling`, a schema mover) by `revert_cp_t03_07`."""
    from .test_strife_credit import revert_cr79
    revert_cr79(monkeypatch)    # v11 CR-79 (the credit term, a later mover of the told deposit): reverted, so this pin reads its own item
    revert_cr87(monkeypatch)
    revert_cp_t03_02(monkeypatch)
    revert_cr85(monkeypatch)
    revert_cp_t03_04(monkeypatch)
    revert_cp_t03_07(monkeypatch)   # v11 CP-T03-07 (`body_ceiling`, a schema mover of every realm), the same way
    revert_cp_t03_08(monkeypatch)   # v11 CP-T03-08 (`tend` forms on the wounded, a formation mover of every season), the same way
    h, reads, refused_on_it = _realm_two_seasons(seed)
    assert reads > 0, "the conjunct was never read: the equality below observes nothing"
    assert refused_on_it == 0, f"{refused_on_it} Events were refused on `individual` at seed {seed}"
    assert h == BASE[seed], "the conjunct moved a realm in which no cohort was a party"


def test_where_a_cohort_was_a_party_the_realm_moves_and_the_refusals_are_the_conjuncts(monkeypatch):
    """Seed 2 (since PC-10b's re-take, under `WITHHELD`; seed 1 before it): a cohort was a party on the pre-conjunct base.
    The same seed now refuses that act on `individual`, and the realm ends elsewhere -- the mover the position declares.
    Read with CR-87 at its revert, for the control's reason above, and (v11) CP-T03-04's formation mover at its revert,
    so the seed forms the cohort-party act it was measured on."""
    revert_cr87(monkeypatch)
    revert_cp_t03_04(monkeypatch)
    # v11 CP-T03-08 (`tend` forms on the wounded, a formation mover of every season) moves seed 2's second season off the
    # cohort-party act (MEASURED: 0 refusals on `individual` with it live), so it is read at its revert too, the same way.
    revert_cp_t03_08(monkeypatch)
    # v10 CP-T05-02 (iii) (the self-plea, a formation mover wherever a docketed party is offered his own matter) moves this
    # reverted arm's seed-2 trajectory off the cohort-party act (MEASURED: 0 refusals on `individual` with it live), so it
    # is read at its revert too, the same way. The shipped realm's pins do not move (`test_season_weather.BASE_HASHES`).
    revert_cp_t05_02(monkeypatch)
    h, reads, refused_on_it = _realm_two_seasons(2)
    assert refused_on_it > 0, "no act was refused on `individual` at seed 2"
    assert h != BASE[2], ("the realm did not move off the pre-conjunct base at seed 2 (the refusal itself is observed "
                          "by `refused_on_it` above, not by this hash)")
