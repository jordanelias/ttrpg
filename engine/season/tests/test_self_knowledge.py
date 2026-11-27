"""B10.64, B10.65 (`U5a_CHAR_self_knowledge_is_a_belief`) -- WHAT A PERSON BELIEVES OF HIMSELF, READ FROM HIS OWN LEDGER FOR THE KEYS
`rosters.yaml: self_believed` NAMES. `boot/realm.py::seed_self_knowledge` writes one firsthand `self:<key>` claim for every key a person holds that his cast
row does not mark `unaware:`; a mark is the ABSENCE of the claim. Lane: the season loop.

Planted persons and a planted mark throughout: the planted marks are the test's own; the shipped registry marks NPC-004 and NPC-012 (BA1.12) and these tests stay green with them.
THE FALSIFIER: a person with no `self:` claim forming `thread_read` (the reader answered from the field); a person with the claim ceasing to (the seeder missed a held
key); a pursuit he holds no claim for changing any `score_terms` term (the score was touched) or still on his sheet; a told claim from a teller he disregards admitting
the act at the floor (the teller's weight was not read).
"""
from __future__ import annotations

import pytest

from engine.substrate.descriptors import PURSUITS

from ..boot.realm import seed_self_knowledge
from ..data import cast
from ..data.rosters import STANCE_VALENCE_SCALE
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.pursuits import pursuit
from ..data.matrix import Step, WriteClass
from ..data.verbs import VERB_TABLE
from ..decision import choose as CH
from ..decision import score_parts as SP
from ..decision.options import opening_set
from ..decision.sheet import creation_sheet, development_space, take_ranked
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..seam.contest import Resolution
from ..seam.wrappers import sigma
from ..queries.person_q import SELF_STEM, OwnStateReader
from ..state.carriers import Candidate, Claim, Person, Question, View, interior_of
from ..state.ids import draw_factory
from .test_in12_step9 import _argue, _argue_world

pytestmark = pytest.mark.flat_fold

ACTOR, TWIN, KEY = "p_low", "p_mid", "prac.thread_sensitivity"
GATE = P.DEFAULT_FIXTURES.get("thread_sensitivity_gate")


def _formed(w, pid) -> bool:
    p = w.persons[pid]
    cands = opening_set(p, View(pid, [], w.fixtures.get("view_k")), Question("q:sk", "need", ("Hh",)), w.fixtures)
    return any(c.verb == "thread_read" for c in cands)


def test_an_unaware_holder_forms_no_thread_read_and_his_twin_does():
    """The same sensitivity on two persons, one marked by a planted cast row, both seated by the one seeder: only the twin holds `self:<key>` and forms
    `thread_read`. The marked one reads UNKNOWN of himself until his own ledger holds the claim, and then the field's value; the fold's reader answers the field
    either way, so a hand-built act still folds. A person holding no sensitivity is given no claim for it."""
    w = P.tiny_world()
    row = {"id": "NPC-T", "ts": GATE + 10, "unaware": [KEY]}
    for pid in (ACTOR, TWIN):
        w.persons[pid].thread_sensitivity = GATE + 10
    written = seed_self_knowledge(w, {ACTOR: cast.unaware_of(row)})
    assert cast.unaware_of({**row, "unaware": None}) == frozenset()
    assert written == [f"c_self_{TWIN}_{KEY}"] and not w.persons[ACTOR].ledger and not w.persons["p_high"].ledger
    assert _formed(w, TWIN) is True, "the seeder missed a key he holds"
    assert _formed(w, ACTOR) is False, "a person with no claim formed the Thread read from a field he does not know he holds"
    me = w.persons[ACTOR]
    assert OwnStateReader(me, w.fixtures).read(ACTOR, "thread_sensitivity") == GATE + 10, "the fold's answer must stay the field's"
    me.ledger.append(Claim("c_self", ACTOR, ACTOR, SELF_STEM + KEY, True, 0, "firsthand", 100, "own"))
    assert _formed(w, ACTOR) is True, "the claim he holds of himself did not admit the act"
    me.ledger.clear()
    assert _formed(w, ACTOR) is False


def _holder():
    """Fifteen pursuits at distinct weights, one of them to be left unrecognised."""
    p = Person(id="p_sk", name="p_sk", pursuits={e: 1.0 + 0.1 * i for i, e in enumerate(sorted(PURSUITS))})
    return p, pursuit("honour")


def test_an_unrecognised_pursuit_moves_no_score_and_leaves_the_sheet():
    """Seated by the one seeder with a claim for every pursuit he holds, then one claim taken away: the pursuit still biases every candidate exactly as before (each
    `score_terms` term equal), its voice is attributed `unrecognised` with the owner withheld, and it is listed on neither the development sheet nor the creation row."""
    p, e = _holder()
    fx = P.DEFAULT_FIXTURES
    w = P.tiny_world()
    w.persons["p_sk"] = p
    seed_self_knowledge(w, {})
    assert len([c for c in p.ledger if c.predicate.startswith(SELF_STEM)]) == len(PURSUITS), "the seeder missed a pursuit he holds"
    cands = [Candidate(v, "p_other") for v in sorted(VERB_TABLE)]
    base = [CH.score_terms(p, c, fx, CH.deliberation_memo(p, fx), None, None) for c in cands]
    parts_base = [SP.score_parts(p, c, fx, CH.deliberation_memo(p, fx)) for c in cands]
    claim = next(c for c in p.ledger if c.predicate == SELF_STEM + e)
    p.ledger.remove(claim)
    memo = CH.deliberation_memo(p, fx)
    assert [CH.score_terms(p, c, fx, memo, None, None) for c in cands] == base, "a pursuit he does not recognise moved a score"
    checked = 0
    for c, was in zip(cands, parts_base):
        now = SP.score_parts(p, c, fx, memo)
        assert sorted(x.pull for x in now) == sorted(x.pull for x in was), c.verb
        assert all(x.owner != e for x in now), c.verb
        if any(x.owner == e for x in was):
            assert any(x.kind == "pursuit" and x.owner == SP.UNRECOGNISED for x in now), c.verb
            checked += 1
    assert checked, "no candidate carried a voice for the pursuit: the attribution was not observed"
    assert e not in creation_sheet([p], lambda pid: ())[0].pursuits and len(creation_sheet([p], lambda pid: ())[0].pursuits) == len(PURSUITS) - 1
    seen = []
    space = development_space(fx, lambda who, verb, subj: f"{who}:{verb}:{subj}", lambda sheet: (seen.append(sheet), take_ranked(sheet))[1],
                              draw=draw_factory(w.world_seed, lambda: w.tick))
    space(interior_of(p, 0, 0), View("p_sk", [], fx.get("view_k"), question=Question("q:sk", "need", ("p_other",))), None, lambda: 1)
    assert seen and e not in seen[0].pursuits and len(seen[0].pursuits) == len(PURSUITS) - 1
    p.ledger.append(claim)
    assert e in creation_sheet([p], lambda pid: ())[0].pursuits


def test_a_told_self_claim_is_weighed_by_regard_for_the_teller():
    """A person holding no claim of his own gift is TOLD he has it (`(him, self:<key>, True)`, deposited as any told claim). At a planted `self_told_floor` the
    reader weighs it by his regard for the teller: from one he disregards it leaves his reader at UNKNOWN and he forms no `thread_read`; from one he trusts the
    act forms. At the shipped floor (0, the control) no teller is weighed and the disregarded one is believed, so the floor is what refuses it."""
    friend, foe = TWIN, "p_high"

    def formed_with(teller, floor, shown=False):
        w = P.tiny_world(DEFAULT_FIXTURES.sweep("self_told_floor", floor))
        me = w.persons[ACTOR]
        me.thread_sensitivity = GATE + 10
        me.stance = [(friend, STANCE_VALENCE_SCALE, STANCE_VALENCE_SCALE), (foe, -STANCE_VALENCE_SCALE, STANCE_VALENCE_SCALE)]
        me.ledger.append(Claim("c_told", ACTOR, ACTOR, SELF_STEM + KEY, True, 0, "told_by", 100, "own", chain=(teller,)))
        if shown:       # B10.66: his own act showed it (WITNESS's deposit to him), which no teller's weight can overrule
            me.ledger.append(Claim("c_shown", ACTOR, ACTOR, "skill_shown:" + KEY, True, 1, "firsthand", 50, "own"))
        return _formed(w, ACTOR)

    assert formed_with(friend, 0.5) is True, "a claim from a teller he trusts did not admit the act"
    assert formed_with(foe, 0.5) is False, "a claim from a teller he disregards admitted the act"
    assert formed_with(foe, 0.5, shown=True) is True, "a skill shown to him was weighed against the teller he disregards"
    assert formed_with(foe, 0.0) is True, "the shipped floor refused a told claim"


def test_a_mans_own_self_claim_is_never_offered_as_news_about_himself_and_a_told_one_is():
    """`said_of` is what a person passes on about a subject. His own `self:<key>` claim (firsthand, held by its subject) is not hearsay and is skipped, so a person
    seated by the seeder has nothing to say of himself; the same predicate TOLD to him (a chain) is deposited as any told claim and is still said."""
    from ..queries.person_q import said_of
    w = P.tiny_world()
    w.persons[ACTOR].thread_sensitivity = GATE + 10
    seed_self_knowledge(w)
    me = w.persons[ACTOR]
    assert me.ledger and said_of(me.ledger, ACTOR, w.fixtures, me) is None, "his own self-claim was offered as news about himself"
    me.ledger.append(Claim("c_told", ACTOR, ACTOR, SELF_STEM + KEY, True, 0, "told_by", 90, "own", chain=(TWIN,)))
    said = said_of(me.ledger, ACTOR, w.fixtures, me)
    assert said is not None and said.chain == (TWIN,), "a told self-claim was withheld"


# -- B10.66: a skill shown at Overwhelming tells its holder he has it (`U5a` edit 6 (b)) ---------------------------------------------------------------------------
SHOWN = "skill_shown:"


def _fold_shown(w, d, act_id, band, *rows):
    """One `argue` of the arguer's through the real fold at `band`, the roll's record naming `rows` in `fed_by` (the shape `sigma._fed_by` returns)."""
    w.step = Step.RESOLVE
    w.frozen = False
    out = d._fold(w, mint_token(w, WriteClass.ACTS), _argue(w.proposition, act_id), Resolution(band, {"fed_by": rows}))
    w.log.extend(out)
    return out


def _witness(w, d, out):
    w.step = Step.WITNESS
    d.witness(mint_token(w, WriteClass.INTERIOR), out)


def _argued_world():
    w, d, w.proposition, _ = _argue_world()
    w.persons[ACTOR].thread_sensitivity = GATE + 10
    return w, d


def _own(w, pid, stem):
    return [c for c in w.persons[pid].ledger if c.predicate.startswith(stem)]


def _fed(key, side="actor"):
    return (sigma.SOCIAL_ROLL_SITE, "edge", key, side, 3, 3.0)


def test_a_shown_skill_is_deposited_to_the_actor_alone():
    """He holds the gift and no claim of it; his argument reaches Overwhelming with a use row keyed on it in the roll's `fed_by`. WITNESS deposits ONE
    `skill_shown:<key>` claim (firsthand, about himself) to him and to nobody else, though the others witnessed the same Event (the shipped
    `observation_deposit_mode: actor`), and he now recognises the gift (`thread_read` forms). A second such act adds no second claim; a man seeded
    with `self:<key>` is not told what he holds, so his ledger gains nothing and no Event carries the Observation."""
    w, d = _argued_world()
    assert not _formed(w, ACTOR)
    _witness(w, d, _fold_shown(w, d, "sk_1", "Overwhelming", _fed(KEY)))
    mine = _own(w, ACTOR, SHOWN)
    assert [(c.subject, c.predicate, c.value, c.source) for c in mine] == [(ACTOR, SHOWN + KEY, True, "firsthand")], mine
    others = [p for p in w.persons if p != ACTOR]
    assert all(not _own(w, p, SHOWN) and not _own(w, p, SELF_STEM) for p in others), "a person other than the holder was told"
    assert w.persons[TWIN].ledger, "the others witnessed nothing: 'alone' was not observed"
    assert _formed(w, ACTOR) is True, "the shown skill did not tell him he has it"
    _witness(w, d, _fold_shown(w, d, "sk_2", "Overwhelming", _fed(KEY)))
    assert len(_own(w, ACTOR, SHOWN)) == 1, "a repeat deposited a second claim"
    w2, d2 = _argued_world()
    seed_self_knowledge(w2)
    out = _fold_shown(w2, d2, "sk_3", "Overwhelming", _fed(KEY))
    assert not any(o.predicate.startswith(SHOWN) for e in out for o in e.observed), "a man who knows his skill was shown it"
    _witness(w2, d2, out)
    assert not _own(w2, ACTOR, SHOWN) and len(_own(w2, ACTOR, SELF_STEM + KEY)) == 1


def test_an_act_below_overwhelming_adds_no_skill_shown_observation():
    """The control: the same roll record at Success, a row of the SUBJECT's side at Overwhelming, and a row keyed on something he cannot be unaware of
    (`verb`, the dice row's key) add no Observation and no claim."""
    w, d = _argued_world()
    outs = [_fold_shown(w, d, "ct_1", "Success", _fed(KEY)), _fold_shown(w, d, "ct_2", "Overwhelming", _fed(KEY, "subject")),
            _fold_shown(w, d, "ct_3", "Overwhelming", _fed("verb"))]
    assert {e.degree for out in outs for e in out} == {"Success", "Overwhelming"}, "the bands were not folded"
    assert not any(o.predicate.startswith(SHOWN) for out in outs for e in out for o in e.observed)
    for out in outs:
        _witness(w, d, out)
    assert not _own(w, ACTOR, SHOWN) and not _formed(w, ACTOR)
