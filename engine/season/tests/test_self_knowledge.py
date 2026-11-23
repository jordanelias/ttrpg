"""B10.64 (`U5a_CHAR_self_knowledge_is_a_belief` edits 1, 2, 4, 5) -- WHAT A PERSON BELIEVES OF HIMSELF, READ FROM HIS OWN LEDGER FOR THE KEYS
`rosters.yaml: self_believed` NAMES, where his cast row marks him `unaware:`. Lane: the season loop.

Planted persons and a planted cast row throughout: the shipped registry marks nobody (the content is BA1's), and `B10.65` seeds the `self:` claims.
THE FALSIFIER: a marked person forming `thread_read` (the reader answered from the field); an unmarked person ceasing to (the arm reached him); a marked
pursuit changing any `score_terms` term (the score was touched); or the pursuit still on his sheet.
"""
from __future__ import annotations

import pytest

from engine.substrate.descriptors import PURSUITS

from ..data import cast
from ..data.pursuits import pursuit
from ..data.verbs import VERB_TABLE
from ..decision import choose as CH
from ..decision import score_parts as SP
from ..decision.options import opening_set
from ..decision.sheet import creation_sheet, development_space, take_ranked
from ..harness import probes as P
from ..queries.person_q import OwnStateReader
from ..state.carriers import Candidate, Claim, Person, Question, View, interior_of
from ..state.ids import draw_factory

pytestmark = pytest.mark.flat_fold

ACTOR, TWIN, KEY = "p_low", "p_mid", "prac.thread_sensitivity"
GATE = P.DEFAULT_FIXTURES.get("thread_sensitivity_gate")


def _formed(w, pid) -> bool:
    p = w.persons[pid]
    cands = opening_set(p, View(pid, [], w.fixtures.get("view_k")), Question("q:sk", "need", ("Hh",)), w.fixtures)
    return any(c.verb == "thread_read" for c in cands)


def test_an_unaware_holder_forms_no_thread_read_and_his_twin_does():
    """The same sensitivity on two persons, one marked by a planted cast row: only the twin forms `thread_read`. The marked one reads UNKNOWN of himself
    until his own ledger holds `self:<key>`, and then the field's value; the fold's reader answers the field either way, so a hand-built act still folds."""
    w = P.tiny_world()
    row = {"id": "NPC-T", "ts": GATE + 10, "unaware": [KEY]}
    for pid in (ACTOR, TWIN):
        w.persons[pid].thread_sensitivity = GATE + 10
    w.persons[ACTOR].unaware = cast.unaware_of(row)
    assert cast.unaware_of({**row, "unaware": None}) == frozenset() and w.persons[TWIN].unaware == frozenset()
    assert _formed(w, TWIN) is True
    assert _formed(w, ACTOR) is False, "a marked person formed the Thread read from a field he does not know he holds"
    me = w.persons[ACTOR]
    assert OwnStateReader(me, w.fixtures).read(ACTOR, "thread_sensitivity") == GATE + 10, "the fold's answer must stay the field's"
    me.ledger.append(Claim("c_self", ACTOR, ACTOR, "self:" + KEY, True, 0, "firsthand", 100, "own"))
    assert _formed(w, ACTOR) is True, "the claim he holds of himself did not admit the act"
    me.ledger.clear()
    assert _formed(w, ACTOR) is False


def _holder():
    """Fifteen pursuits at distinct weights, one of them marked unaware."""
    p = Person(id="p_sk", name="p_sk", pursuits={e: 1.0 + 0.1 * i for i, e in enumerate(sorted(PURSUITS))})
    return p, pursuit("honour")


def test_an_unrecognised_pursuit_moves_no_score_and_leaves_the_sheet():
    """The marked pursuit still biases every candidate exactly as before (each `score_terms` term equal), its voice is attributed `unrecognised` with
    the owner withheld, and it is listed on neither the development sheet nor the creation row."""
    p, e = _holder()
    fx = P.DEFAULT_FIXTURES
    cands = [Candidate(v, "p_other") for v in sorted(VERB_TABLE)]
    base = [CH.score_terms(p, c, fx, CH.deliberation_memo(p, fx), None, None) for c in cands]
    parts_base = [SP.score_parts(p, c, fx, CH.deliberation_memo(p, fx)) for c in cands]
    p.unaware = frozenset({e})
    memo = CH.deliberation_memo(p, fx)
    assert [CH.score_terms(p, c, fx, memo, None, None) for c in cands] == base, "a marked pursuit moved a score"
    checked = 0
    for c, was in zip(cands, parts_base):
        now = SP.score_parts(p, c, fx, memo)
        assert sorted(x.pull for x in now) == sorted(x.pull for x in was), c.verb
        assert all(x.owner != e for x in now), c.verb
        if any(x.owner == e for x in was):
            assert any(x.kind == "pursuit" and x.owner == SP.UNRECOGNISED for x in now), c.verb
            checked += 1
    assert checked, "no candidate carried a voice for the marked pursuit: the attribution was not observed"
    assert e not in creation_sheet([p])[0].pursuits and len(creation_sheet([p])[0].pursuits) == len(PURSUITS) - 1
    w = P.tiny_world()
    w.persons["p_sk"] = p
    seen = []
    space = development_space(fx, lambda who, verb, subj: f"{who}:{verb}:{subj}", lambda sheet: (seen.append(sheet), take_ranked(sheet))[1],
                              draw=draw_factory(w.world_seed, lambda: w.tick))
    space(interior_of(p, 0, 0), View("p_sk", [], fx.get("view_k"), question=Question("q:sk", "need", ("p_other",))), None, lambda: 1)
    assert seen and e not in seen[0].pursuits and len(seen[0].pursuits) == len(PURSUITS) - 1
    p.unaware = frozenset()
    assert e in creation_sheet([p])[0].pursuits
