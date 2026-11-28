"""v12 B21d.05 (CR-88, the build; `proposals/v12_B21d_duty_of_office.md`): THE DUTY OF OFFICE AND THE COST OF BETRAYAL. Lane: faction actions (the
season loop's formation and score, on hand-built persons and ledgers).

Four parts, each read through the code that carries it:
  (1) the DUTY DECLINE (`decision/options.py::_opening_set`, beside `own_stance_declines`): a person holding a seat of faction F forms no
      opponent-rule verb (`subject_is_opponent`) on a man his own ledger names holding a seat of F (`person_q.officers_named`), unless his
      grievance against that man exceeds `Fixtures betrayal_band`; exempt only through a seat of F that outranks the man, down its chain;
  (2) the BETRAYAL READING, `person_q.grievance_against`: distinct deeds firmed by their distinct origins (`LedgerReader._support`), a grudge
      capped at one step, a rival creed one step;
  (3) DUTY'S POSITIVE HALF and the PRICE OF `accept`, `decision/choose.py::score_terms`' sixth element `duty`;
  (4) the DISPUTE re-pointed: `person_q.holds_dispute` reads the deed half of the grievance.

  CONTROL (recorded at the commit, not pinned here): `duty_weight` 0 and `betrayal_band` None reproduce the pre-item realm hash.
"""
from __future__ import annotations


import pytest

from ..data import goals as goals_data
from ..data import verbs as V
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.pursuits import to_axes
from ..data.rosters import CHANNEL_CLAIM_SOURCE, FACTION_BY_PROP, HEAD_SEAT, PURSUIT_AXES, RUNG_KINDS, SEAT_ROW_BY_ID
from ..decision import choose as CH
from ..decision import options as O
from ..decision.options import opening_set
from ..epistemic import Seen
from ..harness import probes as P
from ..queries import person_q
from ..queries.person_q import SEEN_PREDICATE
from ..state.carriers import Candidate, Claim, Person, Question, Tenure, View

A, B, C = "p_mid", "p_low", "p_other"      # `probes.tiny_world`'s persons: A the officer, B the man acted on, C a third
_REACH = CHANNEL_CLAIM_SOURCE["reach"]
_PROP_OF = {f: prop for prop, f in FACTION_BY_PROP.items()}


def _fx(band=2.0, weight=0.0, **more):
    fx = DEFAULT_FIXTURES.sweep("betrayal_band", band).sweep("duty_weight", weight).sweep("choice_temperature", 0)
    for k, v in more.items():
        fx = fx.sweep(k, v)
    return fx


def _seats(faction: str) -> list:
    """`faction`'s rostered seats, read off `offices.yaml` through `data/goals.py::org_faction`, never named here."""
    return sorted(s for s in SEAT_ROW_BY_ID if goals_data.org_faction("seat", s) == faction)


def _rank(seat: str) -> int:
    return RUNG_KINDS.index(next(iter(SEAT_ROW_BY_ID[seat]["rung"])))


def _seat(p, seat: str, grant=("issue",)) -> None:
    """`p` holds `seat`, its grant snapshot `grant` on the Tenure (`Tenure.granted_acts`' shape, `World._grant_remit`'s writer)."""
    p.tenures.append(Tenure(f"t_hold_{p.id}_{seat}", p.id, seat, "hold", 0, payload={"remit_acts": tuple(grant)}))


def _news(p, holder: str, seat: str) -> None:
    """What `boot/realm.py::seed_seat_news` deposits in `p`'s ledger for `holder` seated on `seat`: one `tenure.opened` claim on each of the
    Event's subjects at the seat's own `(when, lap)` (a lap of its own per seat, so seats do not name each other's holders)."""
    lap = 1 + sum(1 for c in p.ledger if c.predicate == "tenure.opened") // 2
    for n, subject in enumerate((holder, seat)):
        p.ledger.append(Claim(f"c_sn_{p.id}_{seat}_{n}", p.id, subject, "tenure.opened", 1, -1, _REACH, 100, "own", lap))


def _war_q(*on) -> Question:
    """A question whose referents are stamped `Enemy` (the war context), so `fight` and `capture` are formable on each."""
    return Question("q:cr88", "need", tuple(on), on[0], classes=tuple((r, cls) for r in on for cls in (V.ENEMY_CLASS, "Person", V.DETAINEE_CLASS)))


def _formed(p, q, fx, verb=None, subject=None) -> list:
    v = View(p.id, [], fx.get("view_k"), q)
    return [(c.verb, c.subject) for c in opening_set(p, v, q, fx)
            if (verb is None or c.verb == verb) and (subject is None or c.subject == subject)]


def _officer_and_head(faction: str):
    """A on a seat of `faction` that is not its head seat; A's ledger names B holding the head seat."""
    w = P.tiny_world()
    a = w.persons[A]
    _seat(a, min(set(_seats(faction)) - {HEAD_SEAT[faction]}))
    _news(a, B, HEAD_SEAT[faction])
    return w, a


_FACTIONS = sorted(f for f in HEAD_SEAT if set(_seats(f)) - {HEAD_SEAT[f]})


# ------------------------------------------------------------------------------------------------
# (1) THE DUTY DECLINE


@pytest.mark.parametrize("faction", _FACTIONS)
def test_an_office_holder_forms_no_fight_on_his_own_head_with_no_grievance(faction):
    """Over every faction with a head seat and another seat (the seat ids read off the roster, so a decline keyed on one name fails here): the war context
    forms `fight` on the head with the decline off (band None, the control) and not at the shipped band 2.0."""
    w, a = _officer_and_head(faction)
    q = _war_q(B)
    assert _formed(a, q, _fx(band=None), "fight", B), "the war context formed no `fight`: the decline would read nothing"
    assert not _formed(a, q, _fx(band=2.0), "fight", B)
    assert person_q.grievance_against(a, B, _fx()).total == 0.0


def test_the_decline_reads_his_seat_and_his_own_ledger_not_membership_or_another_faction():
    """A member holding no seat, an officer of another faction, and the officer whose ledger does not name the head's seat each form `fight` on him."""
    faction, rival = "Valorsmark", "Hafenmark"
    fx = _fx(band=2.0)
    q = _war_q(B)
    w = P.tiny_world()
    member = w.persons[A]
    member.tenures.append(Tenure("t_member", A, _PROP_OF[faction], "commit", 0))
    _news(member, B, HEAD_SEAT[faction])
    assert _formed(member, q, fx, "fight", B), "a member holding no seat is bound by no office"
    w = P.tiny_world()
    other = w.persons[A]
    _seat(other, min(set(_seats(rival)) - {HEAD_SEAT[rival]}))
    _news(other, B, HEAD_SEAT[faction])
    assert _formed(other, q, fx, "fight", B), "an officer of another faction is not bound toward this faction's head"
    w = P.tiny_world()
    unheard = w.persons[A]
    _seat(unheard, min(set(_seats(faction)) - {HEAD_SEAT[faction]}))
    assert _formed(unheard, q, fx, "fight", B), "an officer who has not heard who holds the head seat is not bound toward its holder"
    _news(unheard, B, HEAD_SEAT[faction])
    assert not _formed(unheard, q, fx, "fight", B)


def _down_the_chain():
    """A on a realm-rank seat of the faction (not its head seat) granting `dispatch` and `determine`; his ledger names B on a territory-rank seat of
    the faction and C on its head seat (realm rank: equal to his own)."""
    faction = "Valorsmark"
    seats = _seats(faction)
    high = min(s for s in seats if _rank(s) == RUNG_KINDS.index("realm") and s != HEAD_SEAT[faction])
    low = min(s for s in seats if _rank(s) == RUNG_KINDS.index("territory"))
    return faction, high, low


def test_the_office_acting_down_its_chain_is_exempt_and_never_up_it_nor_as_himself():
    faction, high, low = _down_the_chain()
    verbs = ("capture", "interrogate", "determine")
    w = P.tiny_world()
    a = w.persons[A]
    _seat(a, high, ("dispatch", "determine"))
    _news(a, B, low)
    _news(a, C, HEAD_SEAT[faction])
    q = _war_q(B, C)
    for verb in verbs:
        assert _formed(a, q, _fx(band=None), verb, B), f"{verb} formed nothing on B with the decline off: the exemption would read nothing"
        assert _formed(a, q, _fx(band=None), verb, C), f"{verb} formed nothing on C with the decline off"
        assert _formed(a, q, _fx(band=2.0), verb, B), f"{verb} through a higher seat of his faction on a lower officer is the office's own work"
        assert not _formed(a, q, _fx(band=2.0), verb, C), f"{verb} on his head (equal rank) is up or across the chain"
    assert _formed(a, q, _fx(band=None), "fight", B)
    assert not _formed(a, q, _fx(band=2.0), "fight", B), "an act done as himself is never exempt"


def test_the_exemption_reads_the_grant_on_his_tenure_not_the_seat_row():
    """The same high seat with `dispatch` dropped from the Tenure's grant snapshot (the `offices.yaml` row unchanged), and a seat of B's own rank granting
    it: `capture` still forms through the low seat with the decline off, and the decline removes it."""
    faction, high, low = _down_the_chain()
    w = P.tiny_world()
    a = w.persons[A]
    _seat(a, high, ("determine",))
    peer = min(s for s in _seats(faction) if _rank(s) == _rank(low) and s != low)
    _seat(a, peer, ("dispatch",))
    _news(a, B, low)
    q = _war_q(B)
    assert _formed(a, q, _fx(band=None), "capture", B), "capture formed nothing through the peer seat: the test would read nothing"
    assert not _formed(a, q, _fx(band=2.0), "capture", B)
    assert _formed(a, q, _fx(band=2.0), "determine", B), "determine still goes through the high seat's own grant"


def test_the_decline_narrows_no_row_that_is_not_an_opponent_row_a46():
    """A-46: leaving and every other act is never narrowed by duty -- the officer's candidates of every row that is NOT `subject_is_opponent` are
    identical at band 2.0 and at None."""
    w, a = _officer_and_head("Valorsmark")
    q = _war_q(B)
    on, off = _formed(a, q, _fx(band=2.0)), _formed(a, q, _fx(band=None))
    keep = lambda xs: sorted(x for x in xs if not O.subject_is_opponent(V.VERB_TABLE[x[0]]))
    assert keep(off), "no non-opponent candidate formed: the comparison would read nothing"
    assert keep(on) == keep(off)
    assert set(on) < set(off), "the decline removed nothing: the comparison is not of a decline"


def test_the_band_is_refused_below_what_his_build_time_state_can_carry():
    w, a = _officer_and_head("Valorsmark")
    for band in (1.99, float("nan")):
        with pytest.raises(ValueError):
            _formed(a, _war_q(B), _fx(band=band))


# ------------------------------------------------------------------------------------------------
# (2) THE BETRAYAL READING


def _judge() -> Person:
    """A person whose pursuits run opposite to the rows of `record.forged`, `exchange.made` and `transfer.made` (cosine below -0.8 each)."""
    p = Person(id="p_judge", name="judge")
    p.pursuits = {"doctrine": 5}
    return p


_WRONGS = ("record.forged", "exchange.made", "transfer.made")


def _told(p, n: int, kind: str, origin: str, confidence: int = 100, doer: str = "p_king") -> None:
    """`p` holds a told claim of `doer`'s deed `kind`, its chain rooted at `origin`."""
    p.ledger.append(Claim(f"c_{n}", p.id, doer, kind, True, 0, "told_by", confidence, "own", 0, chain=(origin,)))


def test_three_planted_deeds_by_the_king_from_three_origins_lift_the_decline():
    p = _judge()
    for n, kind in enumerate(_WRONGS):
        _told(p, n, kind, f"p_teller_{n}")
    g = person_q.grievance_against(p, "p_king", _fx())
    assert g.deeds > 2.0 and g.total > 2.0
    w, a = _officer_and_head("Valorsmark")
    a.pursuits = dict(p.pursuits)
    for n, kind in enumerate(_WRONGS):
        _told(a, n, kind, f"p_teller_{n}", doer=B)
    assert _formed(a, _war_q(B), _fx(band=2.0), "fight", B), "three distinct wrongs past the band lift the decline"


def test_one_origin_three_times_does_not_lift_it():
    p = _judge()
    for n in range(3):
        _told(p, n, _WRONGS[0], "p_teller_0")
    g = person_q.grievance_against(p, "p_king", _fx())
    assert 0.0 < g.deeds <= 1.0
    w, a = _officer_and_head("Valorsmark")
    a.pursuits = dict(p.pursuits)
    for n in range(3):
        _told(a, n, _WRONGS[0], "p_teller_0", doer=B)
    assert not _formed(a, _war_q(B), _fx(band=2.0), "fight", B)


def test_one_deed_from_three_origins_is_corroboration_not_a_series():
    p = _judge()
    for n in range(3):
        _told(p, n, _WRONGS[0], f"p_teller_{n}")
    assert 0.0 < person_q.grievance_against(p, "p_king", _fx()).deeds <= 1.0


def test_a_told_deed_reads_its_support_and_an_approved_deed_reads_nothing():
    p = _judge()
    step = -person_q.deed_steps(p, person_q.projected_axes(p), Claim("c", p.id, "p_king", _WRONGS[0], True, 0, "firsthand", 100, "own"))
    _told(p, 0, _WRONGS[0], "p_teller_0", confidence=50)
    assert person_q.grievance_against(p, "p_king", _fx()).deeds == pytest.approx(step * 0.5, abs=0)
    _told(p, 1, _WRONGS[0], "p_teller_1", confidence=50)
    assert person_q.grievance_against(p, "p_king", _fx()).deeds == step * (1 - 0.5 * 0.5)
    q = _judge()
    approved = max(sorted(V.DEED_KINDS - person_q.PAIRED_KINDS),
                   key=lambda k: person_q.deed_steps(q, person_q.projected_axes(q), Claim("c", q.id, "p_king", k, True, 0, "firsthand", 100, "own")))
    _told(q, 0, approved, "p_teller_0")
    assert person_q.grievance_against(q, "p_king", _fx()).deeds == 0.0


def test_a_build_time_stance_alone_does_not_clear_the_band():
    """A grudge reads at most one step and a rival creed one more: a stance of -25 and a commitment to a rival creed read 2.0, which does not exceed
    the floor band, so the decline holds; a -4 row reads 1.0 alone."""
    faction, rival = "Valorsmark", "Hafenmark"
    w, a = _officer_and_head(faction)
    a.stance.append((B, -4, 1))
    g = person_q.grievance_against(a, B, _fx())
    assert (g.deeds, g.stance, g.creed) == (0.0, 1.0, 0.0)
    a.stance.append((B, -5, 5))
    a.tenures.append(Tenure("t_rival", A, _PROP_OF[rival], "commit", 0))
    g = person_q.grievance_against(a, B, _fx())
    assert (g.stance, g.creed, g.total) == (1.0, 1.0, 2.0)
    assert not _formed(a, _war_q(B), _fx(band=2.0), "fight", B)
    assert _formed(a, _war_q(B), _fx(band=None), "fight", B)


def test_a_condemned_deed_done_to_what_he_holds_weighs_as_done_to_himself():
    """The holdings rule: a paired deed whose patient is an object of his own live `hold`, its doer named by his own sighting, is read with him as its
    patient (`_bond`'s self rule, a = 1), so a condemned one weighs `cos * 2`; on an object he does not hold, with no stance toward it, `cos` alone.
    Planted on a paired kind the tables value (`body.changed`): `tenure.closed`, the design's example, carries no `deed:` cell, so no closing is
    valenced today and the rule is reached by none in a realm (a limit of the tables, not of the rule)."""
    kind = "body.changed"
    p = _judge()
    held = "rec:his_charter"
    p.ledger.append(Claim("c_hurt", p.id, held, kind, True, 0, "firsthand", 100, "own"))
    p.ledger.append(Claim("c_seen", p.id, held, SEEN_PREDICATE, Seen(stratum="contested_physical", who="p_king"), 0, "firsthand", 100, "own"))
    cos = person_q.deed_steps(p, person_q.projected_axes(p), p.ledger[0])
    assert cos < 0, "the deed is not condemned by these pursuits: the test would read nothing"
    assert person_q.grievance_against(p, "p_king", _fx()).deeds == 0.0 - cos
    p.tenures.append(Tenure("t_hold_charter", p.id, held, "hold", 0))
    assert person_q.grievance_against(p, "p_king", _fx()).deeds == 0.0 - cos * 2


# ------------------------------------------------------------------------------------------------
# (3) DUTY'S POSITIVE HALF, AND THE PRICE OF `accept`


_SUBJECT = "p_duty_x"


def _aligned_goal():
    """A goal of a faction with seats, and two verbs its lean orders by a clear margin."""
    verbs = sorted(V.VERB_TABLE)
    for g in goals_data.goals():
        f = goals_data.org_faction(g.org_kind, g.org)
        if f is None or not _seats(f):
            continue
        pull = {v: sum(to_axes(g.pursuits)[ax] * V.align(v, ax) for ax in PURSUIT_AXES) for v in verbs}
        hi, lo = max(verbs, key=pull.get), min(verbs, key=pull.get)
        if pull[hi] - pull[lo] > 0.05:
            return g, f, hi, lo
    raise AssertionError("no faction goal leans two verbs apart: the tables moved under this test")


def _committed(pid, goal_id, seat=None) -> Person:
    p = Person(id=pid, name=pid)
    p.tenures.append(Tenure(f"t_{pid}_g", pid, goal_id, "commit", 0))
    if seat is not None:
        _seat(p, seat)
    return p


def _duty(p, q, fx, verbs) -> list:
    memo = CH.deliberation_memo(p, fx)
    return [CH.score_terms(p, Candidate(v, _SUBJECT), fx, memo, None, q)[CH.TERM_NAMES.index("duty")] for v in verbs]


def test_an_officer_leans_on_his_factions_goal_question_and_a_member_does_not():
    g, f, hi, lo = _aligned_goal()
    rival = next(x for x in sorted(HEAD_SEAT) if x != f and _seats(x))
    need = Question(f"q:need:{g.id}", "need", (_SUBJECT,), g.id)
    officers = [_committed("p_off_1", g.id, _seats(f)[0]), _committed("p_off_2", g.id, _seats(f)[-1])]
    member = _committed("p_member", g.id)
    stranger = _committed("p_stranger", g.id, _seats(rival)[0])
    fx = _fx(weight=1.0)
    for o in officers:
        d_hi, d_lo = _duty(o, need, fx, (hi, lo))
        assert d_hi > d_lo, "the officer's duty does not lean as the goal leans"
    assert _duty(member, need, fx, (hi, lo)) == [0.0, 0.0], "a member holding no seat carries no duty"
    assert _duty(stranger, need, fx, (hi, lo)) == [0.0, 0.0], "an officer of another faction carries no duty on this goal"
    assert _duty(officers[0], need, _fx(weight=0.0), (hi, lo)) == [0.0, 0.0]


def test_off_the_goals_question_the_officer_is_himself_at_every_weight():
    """The whole-vector objection's falsifier: handed a `claim_landed` question, the officers and the member score every candidate identically at
    every `duty_weight` (a term that moved the officer's vector toward the template fails here). A row that answers a challenge is the price's,
    the other half of the duty, read by its own test."""
    g, f, hi, lo = _aligned_goal()
    landed = Question("q:claim:duty", "claim_landed", (_SUBJECT,), "claim:duty")
    people = [_committed("p_off_1", g.id, _seats(f)[0]), _committed("p_member", g.id)]
    verbs = [v for v in sorted(V.VERB_TABLE) if not CH.answers_challenge(Candidate(v, _SUBJECT))]
    for weight in (0.0, 0.5, 1.0, 2.0):
        fx = _fx(weight=weight)
        scores = [[CH.score_total(CH.score_terms(p, Candidate(v, _SUBJECT), fx, CH.deliberation_memo(p, fx), None, landed)) for v in verbs]
                  for p in people]
        assert scores[0] == scores[1], weight


def _challenged(pid, seat=None) -> Person:
    """`pid` holds a challenge from `C` (`accept`'s candidate carries the challenger on `to`)."""
    p = Person(id=pid, name=pid)
    if seat is not None:
        _seat(p, seat)
    return p


def _accept_duty(p, q, fx) -> float:
    c = Candidate("accept", "rec:challenge", operands={"to": C})
    return CH.score_terms(p, c, fx, CH.deliberation_memo(p, fx), None, q)[CH.TERM_NAMES.index("duty")]


def test_accept_is_priced_by_the_station_of_his_office_and_waived_only_for_a_peer_enemy():
    faction = "Valorsmark"
    realm = HEAD_SEAT[faction]
    territory = min(s for s in _seats(faction) if _rank(s) == RUNG_KINDS.index("territory"))
    q = Question("q:accept", "need", ("rec:challenge",), "rec:challenge")
    fx = _fx(weight=1.0)
    k, t, plain = _challenged("p_k", realm), _challenged("p_t", territory), _challenged("p_p")
    top = len(RUNG_KINDS) - 1
    assert _accept_duty(plain, q, fx) == 0.0
    assert _accept_duty(t, q, fx) == -_rank(territory) / top
    assert _accept_duty(k, q, fx) == -_rank(realm) / top
    assert _accept_duty(plain, q, fx) > _accept_duty(t, q, fx) > _accept_duty(k, q, fx)
    war = Question("q:accept:war", "need", ("rec:challenge", C), "rec:challenge", classes=((C, V.ENEMY_CLASS),))
    _news(k, C, territory)
    assert _accept_duty(k, war, fx) < 0.0, "a lesser man's duel settles no realm's dispute"
    k2 = _challenged("p_k2", realm)
    _news(k2, C, min(s for s in _seats("Hafenmark") if _rank(s) == _rank(realm)) if any(_rank(s) == _rank(realm) for s in _seats("Hafenmark"))
          else min(s for s in SEAT_ROW_BY_ID if _rank(s) == _rank(realm) and s != realm))
    assert _accept_duty(k2, war, fx) == 0.0, "a peer enemy's duel could settle the realm's dispute: the price is waived"
    assert _accept_duty(k2, q, fx) == -_rank(realm) / top, "a peer with no enemy stamp (no war question) pays the price: the waiver needs the war"
    assert _accept_duty(k, q, _fx(weight=0.0)) == 0.0


# ------------------------------------------------------------------------------------------------
# (4) THE DISPUTE RE-POINTED


def test_the_dispute_reads_a_wrong_held_not_a_net_sum():
    """Three approved deeds and one condemned: the net sum (`deeds_judged`) reads no dispute; the grievance's deed half does, so `holds_dispute` is True.
    The condemned deed from one origin three times reads one wrong; a ledger of approved deeds only reads none."""
    p = _judge()
    axis_w = person_q.projected_axes(p)
    kinds = sorted(V.DEED_KINDS - person_q.PAIRED_KINDS)
    step = lambda k: person_q.deed_steps(p, axis_w, Claim("c", p.id, "p_king", k, True, 0, "firsthand", 100, "own"))
    approved = sorted(kinds, key=step, reverse=True)[:3]
    for n, kind in enumerate(approved):
        p.ledger.append(Claim(f"c_ok_{n}", p.id, "p_king", kind, True, 0, "firsthand", 100, "own"))
    assert not person_q.holds_dispute(p, "p_king")
    judged, told = person_q.deeds_judged(p, "p_king")
    p.ledger.append(Claim("c_wrong", p.id, "p_king", _WRONGS[1], True, 0, "firsthand", 100, "own"))
    judged, told = person_q.deeds_judged(p, "p_king")
    assert judged + told > 0, "the approvals no longer outweigh the wrong: the test would not part the two readings"
    assert person_q.holds_dispute(p, "p_king")
    once = person_q.grievance_against(p, "p_king", _fx()).deeds
    for n in range(2):
        p.ledger.append(Claim(f"c_wrong_again_{n}", p.id, "p_king", _WRONGS[1], True, 0, "firsthand", 100, "own"))
    assert person_q.grievance_against(p, "p_king", _fx()).deeds == once
