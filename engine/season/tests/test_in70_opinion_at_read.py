"""v9 IN-70 (RS-23, RS-24; ED-IN-0293 (6)) -- a person's opinion of a faction, computed at read, reaching
choice as the REFERENTS of a question.

`person_q.opinion` sums three terms, each on `[-1, +1]` (`opinion_terms`): the pursuit cosine against the
faction's expected vector, the affiliation term (intensity on the poles its goals engage, signed, over the
ceiling) and the regard term (`clamp(regard / STANCE_MAX)`, averaged over its head and the doers the person
believes are its members). `world_q.opinion_of` reads the World half; `world_q.opinion_referents` turns a
paired deed (a death, a wound) into the doer's faction's members where the opinion is below indifference,
and `questions_for` adds them to the question the deed's claim already raised.

FALSIFIERS (the entry's three, each an executable assertion):
  (1) two hearers with EQUAL pursuits and DIFFERENT allegiance (one the victim's ally, one his enemy)
      read the SAME faction-level referents -> fail.
  (2) two hearers equal in all but their intensity on the pole the faction's goals engage read the SAME
      opinion -> fail.
  (3) a STORED opinion value (a carrier field, or a read that writes) -> fail (A-29, T-a).
And the EXIT's attention conjunct on a hand-built world, with H-209's limit stated as a test: a claim
`reach` refuses (a dead victim's) raises no faction either -- this position admits nothing.
"""
from __future__ import annotations

import dataclasses

from ..data import goals as G
from ..data.cast import STANCE_MAX
from ..data.pursuits import pursuit_cosine_axes, to_axes
from ..data.rosters import PURSUITS, SEEN_PREDICATE
from ..epistemic import Seen
from ..harness import probes as P
from ..queries import person_q as PQ
from ..queries import world_q
from ..state.carriers import Claim, Person, Rung, Tenure
from ..state.world import World

KILLER, MATE, VICTIM = "p_killer", "p_killer_mate", "p_high"
# Schoenland expects nothing (no template, no goal): its cosine and affiliation terms read 0, so the
# regard term -- where allegiance enters -- is the whole opinion. The Church engages a pole (its heresy goal).
SCHOENLAND, CHURCH = "fac_schoenland", "fac_church_of_solmund"
POLE = "einhir_restoration"


def _condemning_pursuit(kind="person.died"):
    """A pursuit whose lean on `kind` is NEGATIVE: an ally of the patient condemns the deed twice over
    (`_bond` = 2), an enemy of the patient not at all (`_bond` = 0)."""
    for e in sorted(PURSUITS):
        if PQ._lean(to_axes({e: 1.0}), kind) < 0:
            return e
    raise AssertionError(f"no pursuit condemns {kind!r}: allegiance could not be shown to matter")


def _deed(holder, cid="c_died", subject=VICTIM, kind="person.died", chain=()):
    return Claim(cid, holder, subject, kind, True, 0, "firsthand", 100, "own", 0, chain=chain)


def _seen(holder, who=KILLER, subject=VICTIM, cid="c_seen"):
    return Claim(cid, holder, subject, SEEN_PREDICATE,
                 Seen(stratum="contested_physical", marks=(), who=who), 0, "firsthand", 100, "own", 0)


def _commit(w, pid, faction):
    w.add_tenure(Tenure(f"t_{pid}_{faction}", pid, faction, "commit", 0))   # routes to the person's list


def _person(w, pid, at="S"):
    w.persons[pid] = Person(pid, pid)
    w.rungs[pid] = Rung(pid, "person")
    w.add_tenure(Tenure(f"t_{pid}_in", pid, at, "contain", 0))
    w.add_tenure(Tenure(f"t_{pid}_home", pid, at, world_q.RESIDE_KIND, 0))
    return w.persons[pid]


def _world(hearers: dict, killer_faction=SCHOENLAND):
    """`tiny_world`'s duke (`p_high`, the victim) stands at `S`, a Crown member; the killer and his mate
    are of `killer_faction`. Each hearer lives at `S` (so the victim's claims reach him by `reach`'s
    place clause), holds the paired death claim and the sighting naming the killer, and carries the
    attributes `hearers[h]` gives (`pursuits`, `stance`, `conviction`)."""
    w = P.tiny_world()
    w.tick = 1
    _commit(w, VICTIM, "fac_crown")
    for pid in (KILLER, MATE):
        _person(w, pid, at="Hh")
        _commit(w, pid, killer_faction)
    for h, attrs in hearers.items():
        p = _person(w, h)
        _commit(w, h, "fac_crown")
        for k, v in attrs.items():
            setattr(p, k, v)
        p.ledger += [_deed(h, cid=f"c_died_{h}"), _seen(h, cid=f"c_seen_{h}")]
    return w


def _claim_question(w, h):
    return next(q for q in world_q.questions_for(w, w.persons[h]) if q.about == f"c_died_{h}")


# --- FALSIFIER (1): allegiance, not pursuits, decides the faction-level referents ----------------------

def test_equal_pursuits_different_allegiance_read_different_faction_referents():
    e = _condemning_pursuit()
    w = _world({"h_ally": {"pursuits": {e: 1.0}, "stance": [(VICTIM, 5, 5)]},
                "h_enemy": {"pursuits": {e: 1.0}, "stance": [(VICTIM, -5, 5)]}})
    ally, enemy = w.persons["h_ally"], w.persons["h_enemy"]
    assert ally.pursuits == enemy.pursuits
    # the ally's opinion of the killer's faction falls below indifference; the enemy's does not
    assert world_q.opinion_of(w, ally, SCHOENLAND) < 0 <= world_q.opinion_of(w, enemy, SCHOENLAND)
    ref_ally = world_q.opinion_referents(w, ally, ally.ledger[0])
    ref_enemy = world_q.opinion_referents(w, enemy, enemy.ledger[0])
    assert ref_ally == (KILLER, MATE) and ref_enemy == (), (ref_ally, ref_enemy)
    # and through `questions_for`: the deed's own question carries the faction for the ally only
    assert _claim_question(w, "h_ally").referents == (VICTIM, KILLER, MATE)
    assert _claim_question(w, "h_enemy").referents == (VICTIM,)


def test_a_hidden_hand_or_a_told_copy_raises_no_faction():
    """The pairing never guesses (IN-58): `who` withheld, or a told copy, names no doer and no faction."""
    e = _condemning_pursuit()
    w = _world({"h": {"pursuits": {e: 1.0}, "stance": [(VICTIM, 5, 5)]}})
    p = w.persons["h"]
    p.ledger = [_deed("h", cid="c_died_h"), _seen("h", who=None, cid="c_seen_h")]
    assert world_q.opinion_referents(w, p, p.ledger[0]) == ()
    p.ledger = [_deed("h", cid="c_died_h", chain=("p_teller",)), _seen("h", cid="c_seen_h")]
    assert world_q.opinion_referents(w, p, p.ledger[0]) == ()
    # a deed he does not judge (no pursuit leans on it: `paired_deed_term` names no doer) raises none
    p.ledger = [_deed("h", cid="c_died_h"), _seen("h", cid="c_seen_h")]
    assert world_q.opinion_referents(w, p, p.ledger[0]) == (KILLER, MATE)
    p.pursuits = {}
    assert world_q.opinion_referents(w, p, p.ledger[0]) == ()


# --- FALSIFIER (2): the affiliation term reads the engaged pole's intensity --------------------------

def test_equal_but_for_the_engaged_pole_read_different_opinion():
    engaged = world_q.engaged_poles("Church of Solmund")
    assert engaged and all(name == POLE for name, _ in engaged), engaged
    base = {"pursuits": {"honour": 1.0}, "stance": []}
    w = _world({"h_devout": {**base, "conviction": {POLE: PQ.AFFILIATION_CEILING}},
                "h_cold": {**base, "conviction": {POLE: 0}}}, killer_faction=CHURCH)
    hot, cold = w.persons["h_devout"], w.persons["h_cold"]
    o_hot, o_cold = world_q.opinion_of(w, hot, CHURCH), world_q.opinion_of(w, cold, CHURCH)
    assert o_hot != o_cold, (o_hot, o_cold)
    # the whole difference is the affiliation term, at full intensity one full step of the ladder
    sign = engaged[0][1]
    assert abs((o_hot - o_cold) - sign * 1.0) < 1e-12, (o_hot, o_cold, sign)


def test_the_engaged_side_is_the_goals_own_stance_where_authored():
    """A planted faction goal engaging the pole with `stance: +1` flips the term's sign: the side is read
    off the row, never fixed in code where a row says otherwise."""
    rows = tuple(G.goals()) + (dataclasses.replace(
        next(g for g in G.goals() if g.object.get("engaging") == POLE and g.org_kind == "faction"),
        id="goal_planted_for_the_pole", org="Schoenland", stance=1),)
    with G.rows_replaced(rows):
        assert world_q.engaged_poles("Schoenland") == ((POLE, 1),)
        w = _world({"h": {"pursuits": {"honour": 1.0}, "conviction": {POLE: PQ.AFFILIATION_CEILING}}})
        _cos, aff, _reg = PQ.opinion_terms(w.persons["h"], G.expected("faction", "Schoenland"),
                                           world_q.engaged_poles("Schoenland"), ())
        assert aff == 1.0, aff


# --- the three terms: one owner each, each on [-1, +1] -----------------------------------------------

def test_the_terms_are_their_owners_numbers():
    e = _condemning_pursuit()
    w = _world({"h": {"pursuits": {e: 1.0, "doctrine": 0.5}, "stance": [(VICTIM, 5, 5), (KILLER, -3, 4)],
                      "conviction": {POLE: 3}}}, killer_faction=CHURCH)
    p, fx = w.persons["h"], w.fixtures
    expected = G.expected("faction", "Church of Solmund")
    regarded = (KILLER,)
    cos, aff, reg = PQ.opinion_terms(p, expected, world_q.engaged_poles("Church of Solmund"), regarded, fx)
    assert cos == pursuit_cosine_axes(PQ.projected_axes(p, fx.get("scar_weight_shift")), to_axes(expected))
    assert aff == -3 / PQ.AFFILIATION_CEILING
    assert reg == max(-1.0, min(1.0, PQ.regard(p, KILLER, fx) / STANCE_MAX))
    assert all(-1.0 <= t <= 1.0 for t in (cos, aff, reg))
    assert PQ.opinion(p, expected, world_q.engaged_poles("Church of Solmund"), regarded, fx) == cos + aff + reg


def test_a_faction_expecting_nothing_engaging_nothing_and_nobody_known_is_indifference():
    w = _world({"h": {"pursuits": {"honour": 1.0}}})
    p = w.persons["h"]
    p.ledger = []
    assert world_q.opinion_of(w, p, SCHOENLAND) == 0.0


# --- FALSIFIER (3): nothing is stored --------------------------------------------------------------

def test_no_stored_opinion():
    e = _condemning_pursuit()
    w = _world({"h_ally": {"pursuits": {e: 1.0}, "stance": [(VICTIM, 5, 5)]}})
    p = w.persons["h_ally"]
    before = w.content_hash()
    o1 = world_q.opinion_of(w, p, SCHOENLAND)
    world_q.questions_for(w, p)
    world_q.opinion_referents(w, p, p.ledger[0])
    assert w.content_hash() == before, "reading an opinion wrote to the World"
    # no carrier holds one: neither Person nor World has a field for it
    names = {f.name for f in dataclasses.fields(Person)} | set(vars(World(0)))
    assert not {n for n in names if "opinion" in n or "sympath" in n}, names
    # computed at read: a deed claim landing moves it with nothing written in between
    p.ledger = [c for c in p.ledger if c.predicate != "person.died"]
    o0 = world_q.opinion_of(w, p, SCHOENLAND)
    assert o0 == 0.0 and o1 < 0.0, (o0, o1)


# --- the EXIT's attention conjunct, hand-built; and the H-209 limit --------------------------------

def test_a_victim_faction_member_attends_to_the_killers_faction():
    """A Crown member who saw a Crown man struck by a Schoenland man holds a question OCCASIONED BY THE
    DEED whose referents are Schoenland's members (>= 1). Control: without the sighting (a hidden hand)
    the same question carries the patient only."""
    e = _condemning_pursuit()
    w = _world({"h": {"pursuits": {e: 1.0}, "stance": [(VICTIM, 5, 5)]}})
    q = _claim_question(w, "h")
    assert world_q.faction_holding(w, VICTIM) == world_q.faction_holding(w, "h") == "fac_crown"
    hits = set(q.referents) & set(world_q.members(w, SCHOENLAND))
    assert len(hits) >= 1, q.referents
    w.persons["h"].ledger = [c for c in w.persons["h"].ledger if c.predicate != SEEN_PREDICATE]
    assert _claim_question(w, "h").referents == (VICTIM,)


def test_a_claim_reach_refuses_raises_no_faction_h209():
    """H-209 (owner: IN-12 step 5): a DEAD victim has no place, so his death claim is never a question,
    and this position does not widen admission -- the faction referents ride only a question `reach`
    admitted. The victim removed from the world (as a death removes him), the claim raises nothing,
    though `opinion_referents` still reads the faction off it."""
    e = _condemning_pursuit()
    w = _world({"h": {"pursuits": {e: 1.0}, "stance": [(VICTIM, 5, 5)]}})
    p = w.persons["h"]
    assert world_q.opinion_referents(w, p, p.ledger[0]) == (KILLER, MATE)
    del w.persons[VICTIM]
    assert not any(q.about == "c_died_h" for q in world_q.questions_for(w, p))
