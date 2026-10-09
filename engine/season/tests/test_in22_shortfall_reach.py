"""v9 IN-22 · CARRY-SHORTFALL, THE REACH HALF (#457 `:162`; `H-160` limit 2): a shortfall reaches the
governors whose seat's purview contains the drained larder.

EXIT (#457, verbatim): *a governor's `questions_for` holds the claim and a candidate forms in
`harness/scarce.py`'s world.* FALSIFIER: *the claim held by a governor outside the shortfall's reach and
purview, or by none -> fail.*

The world is `scarce.governed`: `scarce.build` plus two reeves, each seated on a territory and living
there, so neither stands at `set_hungry` nor holds it. One seat's rung contains the hungry town, the
other's is a sibling territory. Everything else is the shipped loop: MATTER's draw records the
shortfall on the drained larder's write, WITNESS deposits it, `questions_for` admits it through
`reach`, `opening_set` forms the `transfer`.

Each assertion below is paired with the arm that would show it wrong: the far reeve (outside purview),
`observation_deposit_mode: none`, `fan_out_mode: presence_only` (the seat channel off), and an ACT's
reads (which stay the actor's). Every loop that asserts per item asserts that it asserted.

THE PAYING HALF (`H-160` limit 1, through `H-158`'s seat alternative) is the last block: `transfer`'s
first eligibility alternative is `remit:issue`, so a holder of a seat granting `issue` exercises it
(`Act.via`) and gives from the SEAT'S rung, its treasury (`decision/options.py::treasury_of`, the
snapshot the hold carries) rather than from his own home. In `scarce.governed` the reeve lives in a
hearth with no larder and his seat's rung, `terr_march`, holds the treasury, so the two readings of
`from` lead to different outcomes. FALSIFIER: the reeve's computed `transfer` EXECUTES out of
`terr_march` to the hungry town, `via` his seat, carrying the claim's kind and amount, with matter
conserved against a twin whose reeve does not act. CONTROLS: the far reeve forms no transfer to the
town; an unseated giver (the steward) still mints `via=None` from his own containing rung.
[ASSUMPTION; medium; Jordan to correct; revert: a ruling that an `own` verb may be exercised through a
seat] -- `H-158`'s two remedies, and this is the eligibility one.
"""

from __future__ import annotations

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.requires import SHORTFALL_PREDICATE
from ..data.rosters import CHANNEL_CLAIM_SOURCE
from ..data.verbs import VERB_TABLE
from ..decision import make_chooser
from ..decision.options import (containing_rung_of, exercised_seat, opening_set, operands_for,
                                treasury_of)
from ..harness import scarce as S
from ..loop.driver import resolvable_verbs
from ..loop.witness import SEAT_CHANNEL
from ..queries import world_q
from ..state.carriers import View
from ..state.ids import H, draw_factory
from .test_demand_delivery import _season

GOVERNORS = (S.REEVE, S.FAR_REEVE)


def _recorded(w) -> dict:
    """What MATTER recorded at the hungry larder: `{predicate: units}`, off the log."""
    return {o.predicate: o.value for e in w.log for o in e.observed
            if o.subject == S.HUNGRY and str(o.predicate).partition(":")[0] == SHORTFALL_PREDICATE}


def _held(w, pid) -> dict:
    return {c.predicate: (c.value, c.source) for c in w.persons[pid].ledger
            if c.subject == S.HUNGRY and str(c.predicate).partition(":")[0] == SHORTFALL_PREDICATE}


def _one_season(fixtures=DEFAULT_FIXTURES):
    # `steward_holds=False`: nobody HOLDS the hungry town, so the document channel admits nobody to
    # its larder write and the only route left to a person not standing there is the one under test.
    w = S.governed(fixtures=fixtures, steward_holds=False)
    _season(w)
    return w


def test_in22_the_world_isolates_purview_as_the_only_difference():
    """THE PRECONDITION, ASSERTED SO THE FALSIFIER CANNOT PASS FOR ANOTHER REASON: neither reeve
    stands at the hungry town or holds it, both hold a live seat with a rung, and exactly one seat's
    purview contains the town."""
    w = S.governed(steward_holds=False)
    assert S.HUNGRY not in {world_q.place_of(w, g) for g in GOVERNORS}
    assert not [t for t in w.tenures if t.live and t.object == S.HUNGRY and t.kind == "hold"]
    for g, seat in ((S.REEVE, S.REEVE_SEAT), (S.FAR_REEVE, S.FAR_SEAT)):
        assert w.offices[seat].rung is not None
        assert any(t.kind == "hold" and t.live and t.object == seat for t in w.persons[g].tenures)
    assert world_q.governors_of(w, S.HUNGRY) == [S.REEVE]
    assert S.HUNGRY in world_q.reach(w, w.persons[S.REEVE])
    assert S.HUNGRY not in world_q.reach(w, w.persons[S.FAR_REEVE])


def test_in22_the_governor_inside_purview_holds_the_claim_and_the_one_outside_does_not():
    """THE FALSIFIER, BOTH WAYS. The reeve whose seat contains the town holds every shortfall MATTER
    recorded there, at the recorded units, with the seat channel's source; the far reeve holds none.
    Checked per recorded kind, and the count is asserted so an empty record cannot pass."""
    w = _one_season()
    recorded = _recorded(w)
    assert recorded, "MATTER recorded no shortfall at the hungry larder; nothing below is observed"
    inside, outside = _held(w, S.REEVE), _held(w, S.FAR_REEVE)
    checked = 0
    for pred, units in sorted(recorded.items()):
        assert inside.get(pred) == (units, CHANNEL_CLAIM_SOURCE[SEAT_CHANNEL]), (pred, inside)
        assert pred not in outside, (pred, outside)
        checked += 1
    assert checked >= 1
    assert outside == {}, "a governor outside the shortfall's purview holds it"
    assert inside, "no governor holds the shortfall"


def test_in22_the_governor_learns_the_reads_and_not_the_write():
    """A REPORT, NOT A WITNESSING: the reeve holds no event-kind or `seen` claim about the larder's
    write -- only what MATTER recorded. The hungry cohort, standing there, holds both (CONTROL that
    the write was witnessed at all)."""
    w = _one_season()
    reeve_other = [c for c in w.persons[S.REEVE].ledger
                   if c.subject == S.HUNGRY and c.predicate not in _held(w, S.REEVE)]
    assert reeve_other == [], [(c.predicate, c.source) for c in reeve_other]
    people = {c.predicate for c in w.persons[S.POPULACE].ledger if c.subject == S.HUNGRY}
    assert "stores.changed" in people and set(_recorded(w)) <= people, people


def test_in22_the_governors_questions_for_holds_the_claim_and_a_transfer_forms_from_it():
    """THE EXIT: the reeve's `questions_for` holds a `claim_landed` question about a shortfall claim,
    and `opening_set` on it forms a `transfer` to the hungry town carrying the claim's own kind and
    amount. The far reeve has no such question."""
    w = _one_season()
    reeve = w.persons[S.REEVE]
    q = S.shortfall_question(w, S.REEVE)
    assert q is not None and q.source == "claim_landed", [x.about for x in world_q.questions_for(w, reeve)]
    claim = next(c for c in reeve.ledger if c.id == q.about)
    (cand,) = [c for c in opening_set(reeve, View(reeve.id, [], 99, q), q, w.fixtures)
               if c.verb == "transfer"]
    ops = cand.operands
    assert ops["to"] == S.HUNGRY
    assert (f"{SHORTFALL_PREDICATE}:{ops['kind']}", ops["amount"]) == (claim.predicate, claim.value)
    assert S.shortfall_question(w, S.FAR_REEVE) is None


def test_in22_control_the_none_arm_deposits_nothing_to_a_governor():
    w = _one_season(DEFAULT_FIXTURES.sweep("observation_deposit_mode", "none"))
    assert _recorded(w), "the record was still made; only its deposit is the arm's"
    assert _held(w, S.REEVE) == {} and _held(w, S.FAR_REEVE) == {}


def test_in22_control_the_route_rides_the_seat_channel_and_is_off_under_presence_only():
    w = _one_season(DEFAULT_FIXTURES.sweep("fan_out_mode", "presence_only"))
    assert _recorded(w)
    assert _held(w, S.REEVE) == {}
    assert _held(w, S.POPULACE), "presence still admits the people standing at the larder"


def test_in22_an_acts_reads_do_not_reach_a_governor():
    """ACTORLESS ONLY. The steward's executed `transfer` out of the granary carries the fold's reads of
    the granary's stores, and the granary lies inside the reeve's purview -- yet those reads stay the
    steward's (`H-122`'s `actor` arm). Asserted that the transfer EXECUTED, or the absence is vacuous."""
    w = S.governed()
    d = _season(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    real = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                        draw=draw_factory(w.world_seed, lambda: w.tick))
    only_steward = lambda p, v, s, b: real(p, v, s, b) if p.id == S.STEWARD else []
    n = len(d.resolved)
    _season(w, only_steward, S.shortfall_question(w, S.STEWARD), d)
    made = {e.causes[0] for e in w.log if e.kind == "transfer.made"}
    assert [a for a in d.resolved[n:] if a.verb == "transfer" and a.id in made], "no transfer executed"
    assert S.GRANARY in [r for r in world_q.reach(w, w.persons[S.REEVE])]
    steward = [c for c in w.persons[S.STEWARD].ledger
               if c.subject == S.GRANARY and str(c.predicate).startswith("stores:")]
    reeve = [c for c in w.persons[S.REEVE].ledger
             if c.subject == S.GRANARY and str(c.predicate).startswith("stores:")]
    assert steward and not reeve, (len(steward), [(c.predicate, c.source) for c in reeve])


# ======================================================================================
# THE PAYING HALF -- `H-160` limit 1, through `H-158`'s seat alternative
# ======================================================================================


def _paying_run(acting=(S.REEVE,), between=None):
    """Season 1 with nobody choosing: MATTER drains the hungry larder and the reeve's seat receives
    the record. Season 2 with the REAL chooser and fold serving only `acting`, with TWO instrument
    choices, each the driver's or the chooser's own probe seam and each stated: every deliberation
    is on the reeve's shortfall question (the driver's override -- `scarce.run`'s `H-54` reason:
    which landed question a person answers is not this position's), and the chooser's `verbs=` is
    narrowed to `transfer`. MEASURED without the second: under the full roster the reeve's formed
    `transfer` (from `terr_march`, the claim's kind and amount) is outscored in that season by
    `levy`, `work`, `examine` and others -- which verb a person prefers is the chooser's score, not
    this position's, and the falsifier is that the candidate EXECUTES once chosen. `acting=()` is
    the CONTROL twin: the same world and the same two barriers, nobody acting. `between(w)`, if
    given, runs after the question is read and before season 2. Returns `(world, question,
    season-2 acts, season-2 Events)`."""
    w = S.governed(steward_holds=False)
    d = _season(w)
    q = S.shortfall_question(w, S.REEVE)
    assert q is not None, "the reeve holds no shortfall question; nothing below is observed"
    if between is not None:
        between(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    real = make_chooser(w.fixtures, mint, verbs=resolvable_verbs() & {"transfer"},
                        draw=draw_factory(w.world_seed, lambda: w.tick))
    only = lambda p, v, s, b: real(p, v, s, b) if p.id in acting else []
    n, n_log = len(d.resolved), len(w.log)
    _season(w, only, q, d)
    return w, q, d.resolved[n:], w.log[n_log:]


def test_in22_the_governor_pays_the_shortfall_out_of_his_seats_rung_through_his_seat():
    """THE FALSIFIER OF THE PAYING HALF, in a seeded run of the shipped chooser and fold: the reeve's
    computed `transfer` EXECUTES (`transfer.made`), exercised through his seat (`Act.via`), out of the
    seat's rung -- NOT his home, which holds nothing -- to the hungry town, carrying the claim's own
    kind and amount; and the matter it moved is exactly the difference against the control twin."""
    w, q, acts, events = _paying_run()
    claim = next(c for c in w.persons[S.REEVE].ledger if c.id == q.about)
    made = {e.causes[0] for e in events if e.kind == "transfer.made" and e.causes}
    paid = [a for a in acts if a.actor == S.REEVE and a.verb == "transfer" and a.id in made]
    assert len(paid) == 1, [(a.verb, a.via, a.payload, a.id in made) for a in acts]
    (a,) = paid
    op = dict(a.payload)
    seat_rung = w.offices[S.REEVE_SEAT].rung
    assert a.via == S.REEVE_SEAT, a.via
    assert op["from"] == seat_rung == S.MARCH, op
    assert op["from"] != world_q.place_of(w, S.REEVE) == S.REEVE_HEARTH
    assert op["to"] == S.HUNGRY
    assert (f"{SHORTFALL_PREDICATE}:{op['kind']}", op["amount"]) == (claim.predicate, claim.value)
    # CONSERVED, AGAINST THE TWIN: the same two barriers with nobody acting. Every other draw is
    # identical between the two, so the only difference is the payment.
    c, _, _, _ = _paying_run(acting=())
    kind, amount = op["kind"], op["amount"]
    moved = {r: w.rungs[r].stores.get(kind, 0) - c.rungs[r].stores.get(kind, 0)
             for r in (S.MARCH, S.HUNGRY)}
    assert moved == {S.MARCH: -amount, S.HUNGRY: amount}, moved


def test_in22_the_governor_outside_purview_forms_no_transfer_to_the_town():
    """CONTROL: the far reeve's seat is the same kind of seat with the same grant (so his `transfer`
    would go through it too), and its purview does not contain the town -- so no question he holds
    forms a `transfer` to it. The same sweep over the reeve's questions DOES form one, which is what
    keeps the far reeve's empty result from being vacuous."""
    w = _one_season()

    def to_town(pid):
        p = w.persons[pid]
        return [(q.about, c.operands) for q in world_q.questions_for(w, p)
                for c in opening_set(p, View(p.id, [], 99, q), q, w.fixtures)
                if c.verb == "transfer" and c.operands.get("to") == S.HUNGRY]

    assert exercised_seat(w.persons[S.FAR_REEVE], VERB_TABLE["transfer"]) == S.FAR_SEAT
    assert to_town(S.FAR_REEVE) == []
    assert to_town(S.REEVE), "the reeve forms no transfer to the town either; the control is vacuous"


def test_in22_control_an_unseated_giver_still_gives_from_where_he_stands_with_no_seat():
    """CONTROL: the alternative names a seat, so a person holding none falls through to `own` exactly as
    before -- `exercised_seat` is `None` and `from` is his own containing rung. The steward (no seat)
    in `scarce.build`, against the reeve (seated) in `scarce.governed`, on the same verb row."""
    row = VERB_TABLE["transfer"]
    w = S.build()
    steward = w.persons[S.STEWARD]
    assert exercised_seat(steward, row) is None
    _season(w)
    q = S.shortfall_question(w, S.STEWARD)
    assert q is not None
    (cand,) = [c for c in opening_set(steward, View(steward.id, [], 99, q), q, w.fixtures)
               if c.verb == "transfer"]
    assert cand.operands["from"] == S.GRANARY, cand.operands
    g = S.governed()
    reeve = g.persons[S.REEVE]
    assert exercised_seat(reeve, row) == S.REEVE_SEAT
    assert treasury_of(reeve, S.REEVE_SEAT) == g.offices[S.REEVE_SEAT].rung == S.MARCH


def test_in22_a_seat_granting_no_issue_exercises_nothing_and_its_holder_gives_as_himself(monkeypatch):
    """CONTROL ON THE GRANT: the alternative is `remit:issue`, read off the hold's own grant, so a seat
    whose remit lacks `issue` admits nothing through it, and its holder's transfer mints `via=None`
    from his own home. Built by removing the cause -- the builder's remit, before seating stamps the
    grant -- not by editing the result."""
    monkeypatch.setattr(S, "REEVE_REMIT", [])
    w = S.governed(steward_holds=False)
    reeve = w.persons[S.REEVE]
    assert exercised_seat(reeve, VERB_TABLE["transfer"]) is None
    _season(w)
    q = S.shortfall_question(w, S.REEVE)
    assert q is not None, "the seat channel no longer reaches him; the control observes nothing"
    (cand,) = [c for c in opening_set(reeve, View(reeve.id, [], 99, q), q, w.fixtures)
               if c.verb == "transfer"]
    assert cand.operands["from"] == S.REEVE_HEARTH, cand.operands


def _seat_hold(w, pid, seat):
    (t,) = [t for t in w.persons[pid].tenures if t.kind == "hold" and t.live and t.object == seat]
    return t


def _rungless(w):
    """The reeve's seat loses its rung and the grant's one writer re-stamps the sitting holder
    (`World._grant_remit(force=True)`, `establish`'s path): the grant still carries `issue`, and no
    treasury."""
    w.offices[S.REEVE_SEAT].rung = None
    t = _seat_hold(w, S.REEVE, S.REEVE_SEAT)
    assert w._grant_remit(t, force=True)
    assert "issue" in t.granted_acts and t.seat_rung is None


def _partial_grant(w):
    """A HAND-BUILT partial grant: the hold carries `remit_acts` and no `seat_rung` key at all."""
    t = _seat_hold(w, S.REEVE, S.REEVE_SEAT)
    del t.payload["seat_rung"]
    assert "issue" in t.granted_acts and t.seat_rung is None


def _gives_as_himself(w, q):
    """The three readers of the seat agree for a holder whose `issue` seat has no treasury:
    `exercised_seat` names none, `operands_for`'s `from` is where he stands, and the formed
    Candidate's `from` is the same. A row that binds no `from` (`issue`, `levy`) still goes
    through the seat -- the filter is the treasury's, not the grant's."""
    reeve = w.persons[S.REEVE]
    row = VERB_TABLE["transfer"]
    assert exercised_seat(reeve, row) is None
    ops = operands_for(reeve, row, q, S.HUNGRY, w.fixtures)
    assert ops is not None and ops["from"] == containing_rung_of(reeve) == S.REEVE_HEARTH, ops
    (cand,) = [c for c in opening_set(reeve, View(reeve.id, [], 99, q), q, w.fixtures)
               if c.verb == "transfer"]
    assert cand.operands["from"] == S.REEVE_HEARTH, cand.operands
    checked = 0
    for verb in ("issue", "levy"):
        assert "from" not in VERB_TABLE[verb].requires_typed.operands()
        assert exercised_seat(reeve, VERB_TABLE[verb]) == S.REEVE_SEAT, verb
        checked += 1
    assert checked == 2


def test_in22_a_rungless_issue_seat_is_passed_over_and_via_and_from_agree():
    """A SEAT WITH NO TREASURY EXERCISES NO `transfer`: its holder falls through to `own`, so the
    act mints `via=None` from his own home -- the seat, `from` and `via` all agree. CONTROL: the
    same holder with the rung intact exercises the seat (the paying-half tests above)."""
    w = _one_season()
    q = S.shortfall_question(w, S.REEVE)
    assert q is not None
    assert exercised_seat(w.persons[S.REEVE], VERB_TABLE["transfer"]) == S.REEVE_SEAT
    _rungless(w)
    _gives_as_himself(w, q)
    # THE ACT `pack_scenes` MINTS, in the seeded run of the shipped chooser and fold.
    w2, _, acts, _ = _paying_run(between=_rungless)
    mine = [a for a in acts if a.actor == S.REEVE and a.verb == "transfer"]
    assert mine, "the reeve minted no transfer; nothing is observed"
    for a in mine:
        assert a.via is None and dict(a.payload)["from"] == S.REEVE_HEARTH, (a.via, a.payload)


def test_in22_a_partial_grant_without_a_seat_rung_is_passed_over_too():
    w = _one_season()
    q = S.shortfall_question(w, S.REEVE)
    assert q is not None
    _partial_grant(w)
    _gives_as_himself(w, q)


def test_in22_the_governors_shortfall_claim_is_refracted_by_the_gain():
    """THE PURVIEW DEPOSIT PASSES THROUGH REFRACTION (`loop/witness.py::_refract`, `H-199`): the
    reeve's shortfall claim is sourced `inferred`, one remove, so its confidence is 100 at the
    control gain 0 and 50 at the shipped 0.5. Asserted per held claim, and that one was held."""
    got = {}
    for gain in (0.0, 0.5):
        w = _one_season(DEFAULT_FIXTURES.sweep("refraction_gain", gain))
        held = [c for c in w.persons[S.REEVE].ledger if c.subject == S.HUNGRY
                and str(c.predicate).partition(":")[0] == SHORTFALL_PREDICATE]
        assert held, f"the reeve holds no shortfall claim at gain {gain}; nothing is observed"
        assert {c.source for c in held} == {CHANNEL_CLAIM_SOURCE[SEAT_CHANNEL]} == {"inferred"}
        got[gain] = {c.confidence for c in held}
    assert got == {0.0: {100}, 0.5: {50}}, got
