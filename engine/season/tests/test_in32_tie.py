"""v9 IN-32 (H-182) -- `tie / knot` gets an effect, a reader and a partner operand.

Built host-side on the B-S re-review of IN-06's design (`proposals/2026-10-07-unplugged-systems-replug.md`
§3.1, §6 items 1-2): `_eff_tie` (`loop/effects_information.py`) opens the actor's own `tie` to the act's
`subject`; the reader is `decision/options.py::teller_weight`'s `relation` term (`tied`, `Fixtures
tie_gain`). `systems/fieldwork/sim/knots.py` is not called. Every world here is hand-built
(`harness/probes.py::tiny_world`: `p_low`, `p_mid` and `p_other` stand at the hearth `Hh`, `p_high` at
the settlement `S`; `p_low` already holds a `tie` to `p_mid`).

  (a) THE EFFECT: an executed tie opens exactly one edge, actor -> subject, kind `tie`, `since` the tick,
      and its one Event is `bond.formed` naming only `since`.
  (b) THE `knot` KIND STAYS DECLINED: no `knot` opens, and `epistemic._ch_witness_key` (the live `knot`
      reader) admits nobody new. CONTROL: a planted `knot` makes the same call admit, so the assertion
      can observe the failure it excludes.
  (c) THE READER: the `relation` term weighs a teller the hearer is tied to above one he is not. CONTROL:
      the TELLER's tie to the hearer (the reverse directed edge, 04 §A.3 row 9) moves nothing, and
      `tie_gain` 0 moves nothing.
  (d) THE REFUSALS: no such person, a non-person, oneself, an absent partner and a second tie to the same
      partner are each `bond.refused` and open nothing; the loop asserts it asserted.

FALSIFIERS, by mutation: `_eff_tie` opening `knot` -> (b) red; `tied` reading the teller's own edges ->
(c)'s control red; dropping the cell's `with` conjunct -> (d)'s absent case red.
"""

from __future__ import annotations

from ..data.matrix import WriteClass
from ..data.verbs import _OPENERS_FROM_EFFECTS, VERB_TABLE
from ..decision import assemble
from ..decision import options as OPT
from ..decision.options import opening_set
from ..epistemic import _ch_witness_key
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..state.carriers import Act, Claim, Question, Tenure
from .test_in10_record_operands import _resolve

VERB = "tie / knot"
ACTOR, PARTNER = "p_mid", "p_other"          # both at the hearth `Hh`


def _world():
    w = P.tiny_world()
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _tie(w, d, subject, actor=ACTOR, aid="tie_1"):
    return _resolve(w, d, Act(id=aid, actor=actor, verb=VERB, payload={"subject": subject}))


def _edges(w, kind):
    return sorted((t.subject, t.object, t.since, t.live) for t in w.tenures if t.kind == kind)


def _told(holder, teller, cid="c_told"):
    return Claim(cid, holder, "S", "stores:grain", 3, 0, "told_by", 50, "own", chain=(teller,))


# ======================================================================================
# 0 -- THE ROW
# ======================================================================================

def test_in32_the_row_is_resolvable_and_opens_tie_only():
    assert VERB in resolvable_verbs()
    row = VERB_TABLE[VERB]
    assert row.counterparty == "subject" and row.emits == ("bond.formed",)
    assert row.emits_on_refusal == ("bond.refused",) and row.writes == ("Tenure.since",)
    # the AST-derived opener roster: this row opens `tie`, and nothing opens `knot`
    assert _OPENERS_FROM_EFFECTS["tie"] == [VERB], _OPENERS_FROM_EFFECTS["tie"]
    assert _OPENERS_FROM_EFFECTS["knot"] == [], _OPENERS_FROM_EFFECTS["knot"]


# ======================================================================================
# (a) -- THE EFFECT
# ======================================================================================

def test_in32_a_an_executed_tie_opens_the_actors_tie_to_the_subject_and_writes_only_since():
    w, d = _world()
    before_tie, before_knot = _edges(w, "tie"), _edges(w, "knot")
    out = _tie(w, d, PARTNER)
    assert [e.kind for e in out] == ["bond.formed"], [e.kind for e in out]
    (ev,) = out
    assert [c.field for c in ev.changes] == ["since"], [(c.subject, c.field) for c in ev.changes]
    new = sorted(set(_edges(w, "tie")) - set(before_tie))
    assert new == [(ACTOR, PARTNER, w.tick, True)], new
    assert _edges(w, "knot") == before_knot
    # DIRECTED: the partner gains no edge of his own
    assert not [t for t in w.tenures if t.kind == "tie" and t.subject == PARTNER]


def test_in32_a_the_person_forms_it_on_a_present_person_and_not_on_himself():
    w, _ = _world()
    p = w.persons[ACTOR]

    def formed(ref):
        q = Question(f"q:{ref}", "claim_landed", (ref,), None)
        return [c.subject for c in opening_set(p, assemble(p, q, 12), q, w.fixtures) if c.verb == VERB]

    assert formed(PARTNER) == [PARTNER]
    assert formed(ACTOR) == [], "a tie to oneself must be declined person-side (`counterparty: subject`)"


# ======================================================================================
# (b) -- `knot` IS NOT OPENED, AND THE KNOT READER READS NOTHING NEW
# ======================================================================================

def test_in32_b_no_knot_opens_and_the_witness_key_admits_nobody_new():
    w, d = _world()
    (ev,) = _tie(w, d, PARTNER)
    assert ev.kind == "bond.formed"
    assert _edges(w, "knot") == []
    # the bond.formed Event anchors on its actor; the partner is not admitted by key. The knot index
    # is a per-barrier cache (`queries/cache.py`), so a direct caller discards before each ask.
    w.discard_caches()
    assert _ch_witness_key(w, ev, ACTOR) is True           # the anchor himself, as ever
    assert _ch_witness_key(w, ev, PARTNER) is False
    # CONTROL: a knot between the two makes the same call admit -- the assertion can see a knot
    w.add_tenure(Tenure("t_knot_planted", ACTOR, PARTNER, "knot", since=w.tick))
    w.discard_caches()
    assert _ch_witness_key(w, ev, PARTNER) is True


# ======================================================================================
# (c) -- THE READER, AND ITS DIRECTION
# ======================================================================================

def test_in32_c_the_relation_term_credits_a_teller_the_hearer_is_tied_to():
    w, d = _world()
    hearer = w.persons[ACTOR]
    c = _told(ACTOR, PARTNER)
    fx = w.fixtures
    assert fx.get("tie_gain") > 0, "the shipped gain is the control: the reader would move nothing"
    untied = OPT.teller_weight(hearer, fx)(c)
    assert OPT.tied(hearer, PARTNER) == 0
    _tie(w, d, PARTNER)                                     # through the real fold
    assert OPT.tied(hearer, PARTNER) == 1
    tied = OPT.teller_weight(hearer, fx)(c)
    assert tied > untied, (untied, tied)
    told_weight = fx.get("told_weight")
    assert abs((tied - untied) - told_weight * fx.get("tie_gain")) < 1e-9, (untied, tied)
    # CONTROL 1: `tie_gain` 0 -- the tie moves no weight (the pre-IN-32 reader)
    off = fx.sweep("tie_gain", 0.0)
    assert OPT.teller_weight(hearer, off)(c) == untied


def test_in32_c_control_the_tellers_tie_to_the_hearer_moves_nothing():
    w, d = _world()
    hearer = w.persons[PARTNER]
    c = _told(PARTNER, ACTOR)
    before = OPT.teller_weight(hearer, w.fixtures)(c)
    (ev,) = _tie(w, d, PARTNER)                             # ACTOR -> PARTNER: the TELLER's edge
    assert ev.kind == "bond.formed"
    assert OPT.tied(hearer, ACTOR) == 0
    assert OPT.teller_weight(hearer, w.fixtures)(c) == before, "a tie the hearer does not own moved his weight"
    # and a released tie stops counting (`release`'s domain holds `tie`)
    me = w.persons[ACTOR]
    assert OPT.tied(me, PARTNER) == 1
    for t in me.tenures:
        if t.kind == "tie" and t.object == PARTNER:
            t.until = w.tick
    assert OPT.tied(me, PARTNER) == 0


# ======================================================================================
# (d) -- THE REFUSALS
# ======================================================================================

def test_in32_d_each_refusal_opens_nothing():
    w, d = _world()
    (ok,) = _tie(w, d, PARTNER, aid="tie_first")
    assert ok.kind == "bond.formed"
    cases = {
        "no such person": "nobody",
        "a non-person": "S",
        "oneself": ACTOR,
        "absent (p_high stands at S)": "p_high",
        "already tied": PARTNER,
    }
    checked = 0
    for n, (why, subject) in enumerate(cases.items()):
        ties = _edges(w, "tie")
        out = _tie(w, d, subject, aid=f"tie_refused_{n}")
        assert [e.kind for e in out] == ["bond.refused"], (why, [e.kind for e in out])
        assert _edges(w, "tie") == ties, why
        checked += 1
    assert checked == len(cases) == 5
    assert _edges(w, "knot") == []
