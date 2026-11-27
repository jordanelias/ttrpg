"""B34.05 -- `queries/person_q.py::explain(p, v) -> Derivation`: why a value is what it is, from what the person holds and nothing else.

Four tests, one lane (the season loop: `explain` is read by the season's person-side surface). Written red first: `explain` did not exist.

  * `test_explain_takes_no_world` -- the signature is `(p, v)`, `p` a `PersonInterior`: a world cannot be passed, so a resolver-side fact cannot reach a
    derivation by accident (`04` §C.11). Reads the code's shape, not game state; it is the plan's named test and the precedent is `choose`'s.
  * `test_a_fact_held_by_no_claim_appears_in_no_derivation` -- the falsifier of B34.05: a fact the world holds, that no claim in HIS ledger holds, is in no
    `Derivation.terms` of any value he asks about; the CONTROL is the person who does hold it, whose derivation does name it.
  * `test_each_first_value_is_derived_from_his_own_claims` -- the five first values (an offer's `pursuit` and `stance`, a belief, his `body`, a rung's `stores`).
  * `test_unattributed_is_a_change_no_claim_of_his_names_a_doer` -- `Derivation.unattributed`.
"""
import inspect

from engine.season.decision.choose import TERM_NAMES
from engine.season.decision.sheet import OfferRow
from engine.season.harness.probes import tiny_world
from engine.season.queries import person_q
from engine.season.queries.person_q import Derivation, Value, deed_term, explain, projected_axes
from engine.season.state.carriers import Candidate, Claim, Person, PersonInterior, interior_of


def _claim(cid, holder, subject, predicate, value=True, when=1, source="firsthand", conf=5, **kw):
    return Claim(cid, holder, subject, predicate, value, when, source, conf, "own", **kw)


def _person(pid, *claims):
    p = Person(pid, pid)
    p.ledger.extend(claims)
    return p


def _interior(p, tick=1, decay=0):
    return interior_of(p, tick, decay)


def test_explain_takes_no_world():
    sig = inspect.signature(person_q.explain)
    assert list(sig.parameters) == ["p", "v"], list(sig.parameters)
    assert sig.parameters["p"].annotation in (PersonInterior, "PersonInterior"), sig.parameters["p"].annotation


def test_a_fact_held_by_no_claim_appears_in_no_derivation():
    w = tiny_world()
    # The world holds a fact about p_low that p_mid's ledger holds no claim of: p_other saw it, p_mid did not.
    secret = _claim("c_world_only", "p_other", "p_low", "challenge.issued", doer="p_other")
    known = _claim("c_known", "p_mid", "p_low", "challenge.issued", doer="p_low", when=1)
    w.persons["p_other"].ledger.append(secret)
    w.persons["p_mid"].ledger.append(known)
    asks = [Value("stance", "p_low"), Value("belief", "p_low"), Value("body", "p_low"), Value("stores", "S"),
            Value("pursuit", "p_low", "fight")]

    def ids(person):
        out = set()
        for v in asks:
            out |= {t[0] for t in explain(_interior(w.persons[person]), v).terms}
        return out
    mine, theirs = ids("p_mid"), ids("p_other")
    assert "c_known" in mine, "the claim he does hold is not in his derivations: the reader observed nothing"
    assert "c_world_only" not in mine, mine
    assert "c_world_only" in theirs, "the control: the holder's own derivation does name the claim, so the test can observe the leak it excludes"
    assert "c_known" not in theirs


def test_each_first_value_is_derived_from_his_own_claims():
    deed = _claim("c_deed", "p_me", "p_foe", "challenge.issued", doer="p_foe", when=1, conf=4)
    told = _claim("c_told", "p_me", "p_foe", "challenge.issued", doer="p_foe", when=1, source="told", conf=3, chain=("p_friend",))
    refusal = _claim("c_refused", "p_me", "p_foe", "argument.refused", doer="p_me", when=1, conf=5)
    older, newer = _claim("c_b0", "p_me", "p_foe", "at", "hall", when=0), _claim("c_b1", "p_me", "p_foe", "at", "yard", when=1)
    hurt = _claim("c_hurt", "p_me", "p_me", "body.changed", doer="p_foe", when=1)
    larder = _claim("c_larder", "p_me", "terr_T9", "stores.changed", when=1, source="told", chain=("p_friend",))
    elsewhere = _claim("c_other", "p_me", "terr_T8", "stores.changed", when=1)
    p = _person("p_me", deed, told, refusal, older, newer, hurt, larder, elsewhere)
    ix = _interior(p, tick=1, decay=0)

    def by_id(d):
        return {t[0]: t for t in d.terms}
    # a belief: every claim he holds on that cell, as he holds it (id, source, confidence, when, contribution)
    d = explain(ix, Value("belief", "p_foe", "at"))
    assert isinstance(d, Derivation) and d.value == Value("belief", "p_foe", "at")
    assert [t[0] for t in d.terms] == ["c_b0", "c_b1"] and by_id(d)["c_b1"][1:4] == ("firsthand", 5, 1)
    # his own body and a rung's stores: the claims of that kind about that subject, no other subject's
    assert [t[0] for t in explain(ix, Value("body", "p_me")).terms] == ["c_hurt"]
    assert [t[0] for t in explain(ix, Value("stores", "terr_T9")).terms] == ["c_larder"]
    # stance toward a person: the deeds he holds of him, each worth what `deed_term` says, the firsthand and the told alike
    d = explain(ix, Value("stance", "p_foe"))
    axis_w = projected_axes(ix)
    assert [t[0] for t in d.terms] == ["c_deed", "c_told"]
    assert by_id(d)["c_deed"][4] == deed_term(ix, axis_w, deed) and by_id(d)["c_told"][4] == deed_term(ix, axis_w, told)
    # a pursuit: the one claim a remembered refusal reads (`refused_before`'s own), by the verb's `emits_on_refusal`
    d = explain(ix, Value("pursuit", "p_foe", "argue"))
    assert [t[0] for t in d.terms] == ["c_refused"] and d.terms[0][4] == person_q.refused_before(ix, ("argument.refused",), "p_foe", 1, 0)
    assert explain(ix, Value("pursuit", "p_foe", "fight")).terms == (), "he holds no claim of a refusal of that verb to name"
    # an offer's two terms are the first two of `TERM_NAMES`, and `Value.of_offer` carries the figure the player met
    assert TERM_NAMES[:2] == ("pursuit", "stance")
    row = OfferRow(Candidate("argue", "p_foe", {}), None, (0.5, -1.25, 0.0, 0.0, 0.0), None, 1)
    assert Value.of_offer(row, "pursuit") == Value("pursuit", "p_foe", "argue", 0.5)
    assert Value.of_offer(row, "stance") == Value("stance", "p_foe", "argue", -1.25)
    # the closed set refuses what is not a first value
    for bad in (Value("mood", "p_foe"), Value("stance", None)):
        try:
            explain(ix, bad)
        except ValueError:
            continue
        raise AssertionError(f"{bad} was explained")


def test_unattributed_is_a_change_no_claim_of_his_names_a_doer():
    bare = _claim("c_bare", "p_me", "terr_T9", "stores.changed")                       # the larder fell; nothing he holds says by whom
    doer = _claim("c_doer", "p_me", "p_me", "body.changed", doer="p_foe")              # his own wound, the hand named
    moved = [_claim("c_a", "p_me", "p_x", "at", "hall", when=0), _claim("c_b", "p_me", "p_x", "at", "yard", when=1)]   # a belief that moved, no doer on a place
    steady = [_claim("c_s", "p_me", "p_y", "at", "hall", when=0)]
    ix = _interior(_person("p_me", bare, doer, *moved, *steady), tick=1)
    assert explain(ix, Value("stores", "terr_T9")).unattributed is True
    assert explain(ix, Value("body", "p_me")).unattributed is False
    assert explain(ix, Value("belief", "p_x", "at")).unattributed is True
    assert explain(ix, Value("belief", "p_y", "at")).unattributed is False, "a value that did not move has no missing author"
