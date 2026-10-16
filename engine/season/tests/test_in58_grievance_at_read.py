"""v9 IN-58 (RS-23, RS-24) -- GRIEVANCE AT READ: a deed against someone I am bound to is judged by
that bond (`queries/person_q.py::deeds_judged`, `deed_doer`, `_bond`; the two authored cells
`deed:person.died` and `deed:body.changed` in `rosters.yaml`, RS-29).

  * EXIT -- a seeded kill through the real fold and the real WITNESS: two co-located witnesses with
    equal pursuits and opposite stored stance toward the victim read different `regard` for the
    killer (>= 1 such pair asserted); the control arm (the two cells unbound) reads the base: both
    equal to their stored half. MUTATION, run as a test: `_bond` returning 1.0 makes the pair equal.
  * FALSIFIERS (each an executable assertion, on hand-built ledgers): a `seen` with `who=None` moves
    nothing (a hidden actor stays hidden); anyone's regard FOR a wounded patient is unchanged by the
    cells; the killer is counted once (the killer-subject claim adds nothing to the pair); the
    pairing never guesses (two doers, the patient's own act, another stratum, a told copy).
  * The SWORN-TO half ships OFF (`person_q` reads a `PersonInterior` only): not tested here, not built.
"""
from __future__ import annotations

import functools

import pytest

from ..data import verbs as V
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import Step, WriteClass
from ..data.pursuits import to_axes
from ..data.rosters import PURSUITS, SEEN_PREDICATE
from ..epistemic import Seen
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..queries import person_q as PQ
from ..queries import world_q
from ..state.carriers import Act, Claim, Person, Rung, Tenure

KILLER, VICTIM = "p_near", "p_high"
ALLY, FOE = "p_ally", "p_foe"
CELLS = ("deed:person.died", "deed:body.changed")
FX = DEFAULT_FIXTURES                      # shipped: `judged_gain` 0.5 reads the judged half


def _unbound():
    """The CONTROL table: the shipped alignment with the two IN-58 cells removed (the revert)."""
    return {ax: {k: v for k, v in row.items() if k not in CELLS} for ax, row in V.ALIGNMENT.items()}


def _leaning_pursuit(kind="person.died"):
    """The first pursuit (sorted) whose projection leans non-zero on `kind` -- read off the shipped
    tables, nothing planted. Without one, no factor could show and every test here would be vacuous."""
    for e in sorted(PURSUITS):
        if PQ._lean(to_axes({e: 1.0}), kind):
            return e
    raise AssertionError(f"no pursuit leans on {kind!r}: the authored cells reach nobody")


# ---------------------------------------------------------------------------------------------------
# EXIT -- the seeded kill, through the real fold and the real WITNESS.
# ---------------------------------------------------------------------------------------------------

def _world(pursuit):
    """`tiny_world` (p_high, the victim, stands at `S`) plus the killer and two witnesses at `S`:
    equal pursuits, opposite stance toward the victim, none toward the killer."""
    w = P.tiny_world()
    for pid, stance in ((KILLER, None), (ALLY, (VICTIM, 5, 5)), (FOE, (VICTIM, -5, 5))):
        w.persons[pid] = Person(pid, pid)
        w.rungs[pid] = Rung(pid, "person")
        w.add_tenure(Tenure(f"t_{pid}_in", pid, "S", "contain", 0))
        w.add_tenure(Tenure(f"t_{pid}_home", pid, "S", world_q.RESIDE_KIND, 0))
        if stance is not None:
            w.persons[pid].pursuits = {pursuit: 1.0}
            w.persons[pid].stance = [stance]
    return w


def _kill(i, pursuit):
    """The real `fight` (a wound kills: `wound_harm_model = total`) as act `in58_<i>`, resolved and
    witnessed by ONE driver -- its `act_of` is what `seen.who` is read from. The world if it killed."""
    w = _world(pursuit)
    w.fixtures = w.fixtures.sweep("wound_harm_model", "total")
    w.step = Step.RESOLVE
    d = SeasonDriver(w)
    evs = d.resolve(mint_token(w, WriteClass.ACTS),
                    [Act(id=f"in58_{i}", actor=KILLER, verb="fight", payload={"subject": VICTIM})],
                    w.fixtures.get("contest_max_depth"))
    if VICTIM in w.persons:
        return None
    for ev in evs:
        w.log.append(ev)
    w.step = Step.WITNESS
    d.witness(mint_token(w, WriteClass.INTERIOR), evs)
    return w


@functools.lru_cache(maxsize=None)
def _killing_index(pursuit):
    from ..seam.wrappers import combat as C
    if C.engine() is None:
        pytest.skip(f"personal_combat engine unavailable: {C.load_error()}")
    return next((i for i in range(40) if _kill(i, pursuit) is not None), None)


def _seeded_kill():
    pursuit = _leaning_pursuit()
    i = _killing_index(pursuit)
    assert i is not None, "no act id in range killed the victim: the EXIT would be vacuous"
    return _kill(i, pursuit)


def _pair_regards(w):
    a, f = w.persons[ALLY], w.persons[FOE]
    return PQ.regard(a, KILLER, FX), PQ.regard(f, KILLER, FX)


def test_in58_exit_a_seeded_kill_is_judged_by_each_witness_bond_to_the_victim(monkeypatch):
    w = _seeded_kill()
    checked = 0
    for pid in (ALLY, FOE):
        p = w.persons[pid]
        seen = PQ._seen_index(p.ledger)
        paired = [c for c in p.ledger if c.predicate == "person.died" and PQ.deed_doer(c, seen) == KILLER]
        assert paired and all(c.subject == VICTIM for c in paired), (
            f"{pid} holds no `person.died` deed paired to the killer: {[(c.subject, c.predicate) for c in p.ledger]}")
        assert PQ.stance_toward(p, KILLER) == 0.0, "a stance toward the killer would confound the pair"
        checked += 1
    assert checked == 2
    ally, foe = _pair_regards(w)
    assert ally < foe, ("equal pursuits, opposite stance toward the victim, and the killer is "
                        f"regarded alike: {ally} vs {foe}")
    # CONTROL: the two cells unbound -- the base reading, which is the stored half (0 toward the killer).
    monkeypatch.setattr(V, "ALIGNMENT", _unbound())
    assert _pair_regards(w) == (0.0, 0.0)


def test_in58_mutation_with_the_bond_off_the_two_witnesses_read_alike(monkeypatch):
    """THE MUTATION, run as a test: `_bond` returning 1.0 (no allegiance factor). The EXIT's
    inequality must go red, which is what makes it an observation."""
    w = _seeded_kill()
    monkeypatch.setattr(PQ, "_bond", lambda p, patient, lean: 1.0)
    ally, foe = _pair_regards(w)
    assert ally == foe != 0.0, (ally, foe)


# ---------------------------------------------------------------------------------------------------
# FALSIFIERS -- hand-built ledgers, one witness pass's worth of claims.
# ---------------------------------------------------------------------------------------------------

def _judge(pursuit, stance=(), *claims):
    p = Person("p_judge", "a judge")
    p.pursuits = {pursuit: 1.0}
    # IN-71: `doctrine` reads scaled by religious conviction, so a judge with none reads it at 0 and the
    # pursuit loops below would observe nothing. Full conviction reads every pursuit unscaled.
    p.conviction = {PQ.AFFILIATION_CONCERNS[PQ.RELIGIOUS_CONCERNS[0]][0]: PQ.AFFILIATION_CEILING}
    p.stance = list(stance)
    p.ledger = list(claims)
    return p


def _deed(subject, kind="person.died", n=0, chain=(), when=0, rnd=0):
    return Claim(f"c_deed_{subject}_{kind}_{n}", "p_judge", subject, kind, True, when, "firsthand",
                 100, "own", rnd, chain=chain)


def _seen(subject, who, stratum="contested_physical", n=0, when=0, rnd=0):
    return Claim(f"c_seen_{subject}_{n}", "p_judge", subject, SEEN_PREDICATE,
                 Seen(stratum=stratum, marks=(), who=who), when, "firsthand", 100, "own", rnd)


def test_in58_a_seen_with_no_who_moves_nothing_a_hidden_actor_stays_hidden():
    e = _leaning_pursuit()
    shown = _judge(e, (), _deed("s"), _seen("s", "x"))
    hidden = _judge(e, (), _deed("s"), _seen("s", None))
    assert PQ.deeds_judged(shown, "x")[0] != 0.0, "the shown case does not score: the control is vacuous"
    assert PQ.deeds_judged(hidden, "x") == (0.0, 0.0)
    assert PQ.regard(hidden, "x", FX) == PQ.stance_toward(hidden, "x") == 0.0


def test_in58_a_wounded_patient_is_not_judged_by_the_new_cells(monkeypatch):
    """Anyone's regard FOR the patient is the same with the cells and without them, while the
    regard for the doer moves -- so the cells are live and reach the doer only."""
    e = _leaning_pursuit("body.changed")
    p = _judge(e, [("s", 3, 2)], _deed("s", "body.changed"), _seen("s", "x"))
    live_s, live_x = PQ.regard(p, "s", FX), PQ.regard(p, "x", FX)
    monkeypatch.setattr(V, "ALIGNMENT", _unbound())
    base_s, base_x = PQ.regard(p, "s", FX), PQ.regard(p, "x", FX)
    assert live_s == base_s == PQ.stance_toward(p, "s"), (live_s, base_s)
    assert live_x != base_x == 0.0, (live_x, base_x)


def test_in58_the_killer_is_counted_once():
    """A judge holding the killer-subject claim AND the paired patient-subject `seen` reads the same
    deed term as one holding the pair alone (`both` deposits both claims from one Event)."""
    e = _leaning_pursuit()
    pair = (_deed("s"), _seen("s", "x"))
    alone = PQ.deeds_judged(_judge(e, (), *pair), "x")
    both = PQ.deeds_judged(_judge(e, (), _deed("x"), *pair), "x")
    assert alone[0] != 0.0 and both == alone, (alone, both)


def test_in58_the_factor_falls_with_allegiance_whatever_the_pursuits_sign():
    """`lean · _bond` is monotone non-increasing in the stance toward the patient for either sign of
    the lean, and at no stance it is the pursuit judgement alone. Reads the stored half only:
    `regard` (which calls `deeds_judged`) is never asked."""
    signs = set()
    for e in sorted(PURSUITS):
        lean = PQ._lean(to_axes({e: 1.0}), "person.died")
        if not lean:
            continue
        signs.add(lean > 0)
        terms = [PQ.deeds_judged(_judge(e, [("s", v, 5)], _deed("s"), _seen("s", "x")), "x")[0]
                 for v in (-5, 0, 5)]
        assert terms[0] >= terms[1] >= terms[2] and terms[0] > terms[2], (e, lean, terms)
        assert terms[1] == lean, (e, lean, terms)
    assert signs == {True, False}, "the shipped cells lean one way for every pursuit: half untested"


def test_in58_a_judge_who_is_the_patient_never_warms_to_his_attacker():
    """A wounded survivor who witnessed his own wound holds `(self, kind)` paired to `x`. No stance
    row names oneself, so the stored half would read 0 and judge `x` as a stranger would -- for a
    pursuit leaning positive on the deed, RAISING his regard of his own attacker. `_bond` reads the
    judge who IS the patient as his own full ally: the term is never positive, and negative wherever
    the lean is. MUTATION (run): `_bond` reading `stance_toward(p, patient)` for the patient too
    turns this red on every positive-lean pursuit."""
    checked = negative = 0
    for kind in ("person.died", "body.changed"):
        for e in sorted(PURSUITS):
            lean = PQ._lean(to_axes({e: 1.0}), kind)
            if not lean:
                continue
            p = _judge(e, (), _deed("p_judge", kind), _seen("p_judge", "x"))
            term = PQ.deeds_judged(p, "x")[0]
            assert term <= 0.0, (kind, e, lean, term)
            if lean < 0:
                assert term < 0.0, (kind, e, lean, term)
                negative += 1
            checked += 1
    assert checked and negative, (checked, negative)


def test_in58_an_actorless_sighting_on_the_same_key_makes_the_pairing_ambiguous():
    """A `seen` naming `x` and a `seen` naming nobody on the same subject, `when` and `round`: the
    unnamed hand may be the doer, so the pairing names nobody."""
    d = _deed("s")
    idx = lambda *cs: PQ._seen_index(cs)
    assert PQ.deed_doer(d, idx(_seen("s", "x"))) == "x"                         # the control
    assert PQ.deed_doer(d, idx(_seen("s", "x", n=0), _seen("s", None, n=1))) is None


def test_in58_deeds_judged_never_asks_regard(monkeypatch):
    e = _leaning_pursuit()
    p = _judge(e, [("s", 5, 5)], _deed("s"), _seen("s", "x"))
    monkeypatch.setattr(PQ, "regard", lambda *a, **k: (_ for _ in ()).throw(AssertionError("recursed")))
    assert PQ.deeds_judged(p, "x")[0] != 0.0


def test_in58_the_pairing_never_guesses():
    """`deed_doer` names one `who` or nobody: two different doers, the patient's own act in the same
    round, a sighting of another stratum, another round, and a told copy all pair nobody."""
    d = _deed("s")
    idx = lambda *cs: PQ._seen_index(cs)
    assert PQ.deed_doer(d, idx(_seen("s", "x"))) == "x"                         # the control
    assert PQ.deed_doer(d, idx(_seen("s", "x", n=0), _seen("s", "y", n=1))) is None
    assert PQ.deed_doer(d, idx(_seen("s", "x", n=0), _seen("s", "x", n=1))) == "x"   # one doer, twice
    assert PQ.deed_doer(d, idx(_seen("s", "s", stratum="movement"), _seen("s", "x", n=1))) == "x"
    assert PQ.deed_doer(d, idx(_seen("s", "s"))) is None                        # his own act
    assert PQ.deed_doer(d, idx(_seen("s", "y", stratum="movement"))) is None    # another act
    assert PQ.deed_doer(d, idx(_seen("s", "x", rnd=1))) is None                 # another round
    assert PQ.deed_doer(_deed("s", chain=("p_teller",)), idx(_seen("s", "x"))) is None
    # the killer-subject claim: x killed s, and y struck x in the same round. `(x, person.died)` is
    # x's own deed's anchor claim, and must not read as "y killed x" (MEASURED once on the corpus).
    both = idx(_seen("s", "x", n=0), _seen("x", "y", n=1))
    assert PQ.deed_doer(_deed("x"), both) is None
    assert PQ.deed_doer(_deed("s"), both) == "x"
    # and a told copy scores nothing even beside a matching sighting
    e = _leaning_pursuit()
    assert PQ.deeds_judged(_judge(e, (), _deed("s", chain=("p_teller",)), _seen("s", "x")), "x") == (0.0, 0.0)
