"""v9 IN-72 (RS-23, RS-22; IN-12 step 5's second blocker) -- a death or wound claim reaches attention:
`world_q.attention_key`'s tier 2 scores a PAIRED claim (`person_q.PAIRED_KINDS`) by `|lean * bond|` for
the doer its `seen.who` pairing names, through `person_q.paired_deed_term` -- the ONE scorer
`deeds_judged` sums too.

FALSIFIERS (each an executable assertion; each is MUTATED once below and goes red):
  (a) a hand-built witness with no ambition about, and no purview over, the killer, holding a paired
      `person.died` claim and a `need` question, answers the death claim FIRST (tier 2). The `need`
      question first is the failure. Control inside: the claim is a tier-4 claim without the pairing.
  (b) the same claim with `who` withheld stays tier 4, behind the `need` question: a hidden actor
      stays hidden. A told copy and an ambiguous pairing stay tier 4 too.
  (c) tier 2's value for a paired claim IS the magnitude of `deeds_judged`'s term for that doer: a
      second formula in either place breaks the equality.
"""
from __future__ import annotations

import pytest

from ..data.rosters import PURSUITS, SEEN_PREDICATE
from ..data.pursuits import to_axes
from ..epistemic import Seen
from ..harness import probes as P
from ..queries import person_q as PQ
from ..queries import world_q
from ..state.carriers import Claim, Person, Proposition, Rung, Tenure

KILLER, VICTIM, WITNESS = "p_killer", "p_high", "p_witness"
NEED_TIER = 3


def _leaning_pursuit(kind="person.died"):
    for e in sorted(PURSUITS):
        if PQ._lean(to_axes({e: 1.0}), kind):
            return e
    raise AssertionError(f"no pursuit leans on {kind!r}: tier 2 could not show it")


def _deed(cid="c_died", subject=VICTIM, kind="person.died", chain=(), rnd=0):
    return Claim(cid, WITNESS, subject, kind, True, 0, "firsthand", 100, "own", rnd, chain=chain)


def _seen(who, subject=VICTIM, cid="c_seen", stratum="contested_physical"):
    return Claim(cid, WITNESS, subject, SEEN_PREDICATE, Seen(stratum=stratum, marks=(), who=who),
                 0, "firsthand", 100, "own", 0)


def _witness_world(*claims, pursuit=None):
    """`tiny_world`'s duke (`p_high`, the victim) stands at `S`; the witness lives at `S`, holds no
    tenure on the victim or the killer, and is committed to an OUGHT about `X` (his standing `need`
    question, tier 3). The victim's claims reach him by the PLACE clause (`questions_for` Q2)."""
    w = P.tiny_world()
    w.tick = 1
    pursuit = pursuit or _leaning_pursuit()
    p = Person(WITNESS, WITNESS)
    p.pursuits = {pursuit: 1.0}
    p.conviction = {PQ.AFFILIATION_CONCERNS[PQ.RELIGIOUS_CONCERNS[0]][0]: PQ.AFFILIATION_CEILING}
    w.persons[WITNESS] = p
    w.rungs[WITNESS] = Rung(WITNESS, "person")
    w.add_tenure(Tenure("t_w_in", WITNESS, "S", "contain", 0))
    w.add_tenure(Tenure("t_w_home", WITNESS, "S", world_q.RESIDE_KIND, 0))
    w.propositions["o_x"] = Proposition("o_x", "OUGHT", "X", "X ought to be so", True, 0)
    p.tenures.append(Tenure("t_w_o", WITNESS, "o_x", "commit", 0))
    p.ledger += list(claims)
    return w, p


def _tiers(w, p):
    key = world_q.attention_key(w, p)
    qs = world_q.questions_for(w, p)
    return [q.id for q in qs], {q.id: key(q) for q in qs}


def _check_paired_death_answers_first():
    """(a): the paired death claim is the witness's FIRST question, in tier 2, ahead of `need`."""
    w, p = _witness_world(_deed(), _seen(KILLER))
    ids, keys = _tiers(w, p)
    assert "q:need:o_x" in ids and "q:claim:c_died" in ids, ids
    assert keys["q:claim:c_died"][0] == 2 and keys["q:need:o_x"][0] == NEED_TIER, keys
    assert ids[0] == "q:claim:c_died", ids
    return w, p, keys["q:claim:c_died"]


def _check_hidden_actor_stays_tier_4():
    """(b): `who` withheld, no `seen`, a told copy, an ambiguous pairing: tier 4, behind `need`."""
    cases = {
        "who withheld": (_deed(), _seen(None)),
        "no seen": (_deed(),),
        "told copy": (_deed(chain=("p_teller",)), _seen(KILLER)),
        "ambiguous": (_deed(), _seen(KILLER, cid="c_s1"), _seen(None, cid="c_s2")),
        "two doers": (_deed(), _seen(KILLER, cid="c_s1"), _seen("p_other", cid="c_s2")),
    }
    for name, claims in cases.items():
        w, p = _witness_world(*claims)
        ids, keys = _tiers(w, p)
        assert keys["q:claim:c_died"] == (4, 0.0) + keys["q:claim:c_died"][2:], (name, keys)
        assert ids.index("q:need:o_x") < ids.index("q:claim:c_died"), (name, ids)


def _check_tier_2_value_is_the_deeds_judged_term():
    """(c): tier 2's value for the paired claim is `-|deeds_judged term for the doer|`, bit for bit,
    for both signs of the allegiance factor (the factor moves the value, so a second formula would
    miss one of them)."""
    nonzero = 0
    for stance in ((), [(VICTIM, 5, 5)], [(VICTIM, -5, 5)]):
        w, p = _witness_world(_deed(), _seen(KILLER))
        p.stance = list(stance)
        key = world_q.attention_key(w, p)
        q = next(q for q in world_q.questions_for(w, p) if q.id == "q:claim:c_died")
        judged, told = PQ.deeds_judged(p, KILLER, w.fixtures.get("scar_weight_shift"))
        assert told == 0.0, (stance, told)
        # full allegiance (or enmity) CANCELS a lean of one sign (`_bond`): that term is 0 and the
        # claim is tier 4 -- the same scorer says both, so the equality holds there too.
        want = (2, -abs(judged)) if judged else (4, 0.0)
        assert key(q) == want + key(q)[2:], (stance, key(q), judged)
        nonzero += bool(judged)
    assert nonzero >= 2, nonzero
    # the scorer itself is the one place the product is formed
    w, p = _witness_world(_deed(), _seen(KILLER))
    ax = PQ.projected_axes(p, w.fixtures.get("scar_weight_shift"))
    doer, term = PQ.paired_deed_term(p, ax, p.ledger[0], lambda: PQ._seen_index(p.ledger))
    assert doer == KILLER and term == PQ.deeds_judged(p, KILLER, w.fixtures.get("scar_weight_shift"))[0]


def test_a_witness_with_no_ambition_about_or_purview_over_the_killer_answers_the_death_first():
    w, p, key = _check_paired_death_answers_first()
    # nothing about the killer or the victim in his tenures: not tier 0, not tier 1
    assert KILLER not in world_q.own_purview(w, p) and VICTIM not in world_q.own_purview(w, p)
    assert key[1] < 0.0


def test_the_same_claim_with_who_withheld_stays_tier_4_a_hidden_actor_stays_hidden():
    _check_hidden_actor_stays_tier_4()


def test_tier_2_value_equals_the_magnitude_of_the_deeds_judged_term():
    _check_tier_2_value_is_the_deeds_judged_term()


def test_an_unpaired_deed_still_scores_by_deed_valence():
    """The unpaired arm is untouched: a kind with a `KIND_VERB` is scored by `deed_valence`, in tier 2."""
    from ..data import verbs as V
    kind = next(k for k in sorted(V.DEED_KINDS) if k not in PQ.PAIRED_KINDS
                and PQ._lean(to_axes({_leaning_pursuit(): 1.0}), k))
    w, p = _witness_world(_deed("c_u", subject=VICTIM, kind=kind))
    ids, keys = _tiers(w, p)
    assert keys["q:claim:c_u"][0] == 2, keys
    ax = PQ.projected_axes(p, w.fixtures.get("scar_weight_shift"))
    assert keys["q:claim:c_u"][1] == -abs(PQ.deed_valence(ax, p.ledger[0]))


# ---------------------------------------------------------------------------------------------------
# MUTATIONS -- each producer fault, once, must turn its assertion red.
# ---------------------------------------------------------------------------------------------------

def test_mutation_need_first_turns_the_first_falsifier_red(monkeypatch):
    """Tier 2 as built before IN-72: a paired claim scores 0 (`deed_valence` only)."""
    monkeypatch.setattr(world_q, "paired_deed_term", lambda p, ax, c, s: (None, 0.0))
    with pytest.raises(AssertionError):
        _check_paired_death_answers_first()


def test_mutation_a_hidden_actor_leaking_into_tier_2_turns_the_second_red(monkeypatch):
    """A scorer that scores the lean without asking the pairing who did it."""
    def leaky(p, ax, c, seen_of):
        if c.predicate not in PQ.PAIRED_KINDS:
            return None, 0.0
        return None, PQ._lean(ax, c.predicate)
    monkeypatch.setattr(world_q, "paired_deed_term", leaky)
    with pytest.raises(AssertionError):
        _check_hidden_actor_stays_tier_4()


def test_mutation_a_second_formula_for_the_paired_value_turns_the_third_red(monkeypatch):
    """Tier 2 forming `|lean|` itself (no allegiance factor) instead of calling the shared scorer."""
    real = PQ.paired_deed_term

    def second(p, ax, c, seen_of):
        doer, _ = real(p, ax, c, seen_of)
        return doer, PQ._lean(ax, c.predicate) if doer else 0.0
    monkeypatch.setattr(world_q, "paired_deed_term", second)
    with pytest.raises(AssertionError):
        _check_tier_2_value_is_the_deeds_judged_term()
