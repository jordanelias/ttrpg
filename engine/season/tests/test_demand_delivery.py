"""Plan position `19d` -- DEMAND · DELIVERY. `workplans/2026-09-28-the-plan-one-order-mc-v18-retired.md`
§3.2 row 11: *"the retirement plan's ADJACENT G3: `demanded` / `delivered`, plus the scarce test world.
Gate `15c` (its operands). Beside `24f`, whose territorial quantity it feeds"*. The retirement plan's G3:
*"No new verb: two new read-only queries (`demanded`, `delivered`) plus wiring the existing `transfer`
verb's operands from a shortfall claim."*

What the position built, each asked of the real MATTER barrier, the real WITNESS and the real fold:
  1. `world_q.subsistence_draw` -- the host projection of the larder draw, extracted from MATTER; the
     arithmetic's one owner is `settlements.larder_draw` (`modules/settlements/larder.py`). MATTER runs
     the same draw through `settlements.subsist` (`world_q.subsist_input`); the two Queries sum it.
  2. `world_q.demanded` / `world_q.delivered` -- the need, and what the larder ladder delivers against
     it, over a rung's containment subtree. `demanded - delivered` is the shortfall.
  3. MATTER records that shortfall as an `Observation` on the `stores.changed` Event of a larder the
     draw ran dry with a mouth unfed, and WITNESS deposits it into whoever saw that write. An Event no
     person acted has no actor to keep its reads private to.
  4. `decision/options.py::_from_shortfall_claim` -- `kind` and `amount` read off a held shortfall
     claim, ahead of `store_kind_of` and the fixtures (`rosters.yaml: shortfall_sourced_operands`).
  5. `harness/scarce.py` -- the world where a larder actually runs dry, and a person who can see it
     stands in a stocked one.

THE FALSIFIERS, and the control each carries:
  * the arithmetic: the numbers are recomputed from the fixtures' own `subsistence_weight`, never
    copied, and MATTER's draw removes exactly what `delivered` said it would;
  * the record: exactly the drained larder's write carries the shortfall; the stocked larder's does
    not, and no shipped world carries one at all;
  * the deposit: the holder who was elsewhere receives it (`told_by`). CONTROL: the same world
    without the `hold` edge, where he does not. The `none` arm deposits nothing, and an ACT's reads
    still reach only its actor;
  * the operands: the same person, the same referent, the same season. The shortfall question gives
    the claim's kind and amount; the neighbouring event-kind question gives the fixtures';
  * the chain: the real chooser and the real fold EXECUTE the claim-sourced transfer, matter is
    conserved against a control, and the next season's `delivered` at the hungry town rises against
    the no-`hold` control.

The behaviour-equivalence of the extraction (MATTER's draw moved into `subsistence_draw`) is not
re-proved here, because a test inside the tree cannot run the code it replaced. It was measured
out-of-band as byte-identical content hashes for `headless.run(3)`, `governance_spine` (3 seasons),
`tiny_world` (4) and `populated.build_realm(0)` (2) before and after. `test_season_shape`'s
`test_w15_report_py_reproduces_every_committed_artifact_byte_for_byte` is the in-tree control: the
committed `runs/` did not move.
"""

from __future__ import annotations

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import Step, WriteClass
from ..data.requires import (
    REQUIRES_OPERANDS, REQUIRES_STEMS, SHORTFALL_PREDICATE, SHORTFALL_SOURCED_OPERANDS,
    Observation, _check_shortfall_stem, _check_operand_subset,
)
from ..data.rosters import RECORD_CONTENT
from ..decision import make_chooser
from ..decision.options import _derive_operand, _from_shortfall_claim, opening_set
from ..gaps import InstrumentDefect, Unspecified
from ..harness import headless as HL
from ..harness import probes as P
from ..harness import scarce as S
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..queries import world_q
from ..state.carriers import Act, Claim, Person, Question, Rung, Tenure, View
from ..state.ids import H, draw_factory

WEIGHTS = DEFAULT_FIXTURES.get("subsistence_weight")


def _want(weight: int) -> dict:
    """What a person of this weight eats a season, recomputed from the fixture rather than copied."""
    return {k: wt * weight for k, wt in sorted(WEIGHTS.items()) if wt * weight > 0}


def _matter(w):
    d = SeasonDriver(w)
    return d, d.matter(mint_token(w, WriteClass.MATTER), [])


def _shortfalls(events) -> list:
    return [(o.subject, o.predicate, o.value) for e in events for o in e.observed
            if str(o.predicate).partition(":")[0] == SHORTFALL_PREDICATE]


def _season(w, choose=P.NOCHOOSE, question=None, d=None):
    d = d or SeasonDriver(w)
    d.season(choose, question=question,
             contest_max_depth=w.fixtures.get("contest_max_depth"))
    return d


def _mass(w) -> int:
    return sum(sum((r.stores or {}).values()) for r in w.rungs.values())


# ======================================================================================
# 1 -- THE QUERIES: the need, and what the ladder delivers against it
# ======================================================================================

def test_19d_demanded_is_the_weighted_headcount_under_a_rung():
    w = S.build()
    cohort, one = _want(S.COHORT_WEIGHT), _want(1)
    assert world_q.demanded(w, S.HUNGRY) == cohort
    # ⚠ `24f` (`ED-IN-0255`): THE STEWARD IS AN INDIVIDUAL AND IS EXEMPT FROM THE DRAW, so the
    # granary, housing only him, demands nothing. Until `24f` it demanded his one-person want.
    assert world_q.demanded(w, S.GRANARY) == {}
    # AN R-1 AGGREGATE OVER THE SUBTREE: the territory and the realm hold both settlements' mouths,
    # which since `24f` are the cohort's alone.
    assert world_q.demanded(w, "terr_march") == cohort
    assert world_q.demanded(w, "r_realm") == cohort
    # `Person.weight` IS THE HEADCOUNT: one cohort of ten wants what ten people want.
    assert cohort == {k: v * S.COHORT_WEIGHT for k, v in one.items()}


def test_19d_delivered_is_the_draw_against_the_stores_as_they_stand():
    w = S.build()
    stock = dict(w.rungs[S.HUNGRY].stores)
    got = world_q.delivered(w, S.HUNGRY)
    assert got == {k: min(v, stock.get(k, 0)) for k, v in _want(S.COHORT_WEIGHT).items()}
    # `24f`: the stocked granary feeds nobody -- its steward does not eat from it (`ED-IN-0255`).
    assert world_q.delivered(w, S.GRANARY) == {}, "the steward, an individual, drew on the granary"
    # THE SAME KEYS AS `demanded`, so `demanded - delivered` needs no `.get` default at a caller.
    assert set(got) == set(world_q.demanded(w, S.HUNGRY))


def test_19d_a_rung_with_nothing_in_its_larder_still_demands():
    """THE REJECTED READING'S FALSIFIER: *the eaters whose walk ENDS at the rung*. Under that
    reading an empty larder demands nothing, so the need vanishes exactly where it is unmet."""
    w = S.build()
    w.rungs[S.HUNGRY].stores = {}
    assert world_q.demanded(w, S.HUNGRY) == _want(S.COHORT_WEIGHT)
    assert world_q.delivered(w, S.HUNGRY) == {k: 0 for k in _want(S.COHORT_WEIGHT)}


def test_19d_matter_removes_exactly_what_delivered_said_and_leaves_the_rest_short():
    w = S.build()
    before = dict(w.rungs[S.HUNGRY].stores)
    need, got = world_q.demanded(w, S.HUNGRY), world_q.delivered(w, S.HUNGRY)
    record = world_q.subsistence_draw(w)
    _matter(w)
    # `set_hungry` produces nothing, so MATTER's only write to it is the draw.
    after = w.rungs[S.HUNGRY].stores
    assert {k: before.get(k, 0) - after.get(k, 0) for k in got} == got
    assert w._subsistence_shortfall[S.POPULACE] == {k: need[k] - got[k] for k in need}
    # AND THE QUERIES READ MATTER'S OWN RECORD THE SAME WAY THEY READ THE STORES BEFORE IT.
    assert world_q.delivered(w, S.HUNGRY, record) == got
    assert world_q.demanded(w, S.HUNGRY, record) == need


# ======================================================================================
# 2 -- THE RECORD: the shortfall rides on the drained larder's own write
# ======================================================================================

def test_19d_a_drained_larder_carries_its_shortfall_on_its_own_write_and_nothing_else_does():
    w = S.build()
    need, got = world_q.demanded(w, S.HUNGRY), world_q.delivered(w, S.HUNGRY)
    _, emitted = _matter(w)
    carriers = [e for e in emitted if _shortfalls([e])]
    assert len(carriers) == 1, [(e.kind, e.changes) for e in carriers]
    (e,) = carriers
    assert e.kind == "stores.changed" and world_q.place_of(w, e.changes[0].subject) == S.HUNGRY
    assert _shortfalls([e]) == [(S.HUNGRY, f"{SHORTFALL_PREDICATE}:{k}", need[k] - got[k])
                                for k in sorted(need) if need[k] > got[k]]
    assert all(v > 0 for _, _, v in _shortfalls([e]))
    # CONTROL: the granary's own larder write -- since `24f` its harbour's yield credit, because its
    # steward is exempt and nobody draws on it -- carries nothing.
    granary = [x for x in emitted if x.kind == "stores.changed"
               and x.changes and x.changes[0].subject == S.GRANARY]
    assert granary and not _shortfalls(granary)


def test_19d_a_larder_that_was_never_stocked_reports_nothing_and_is_still_short():
    """THE CROSSING, NOT THE STATE (`loop/matter.py`, `H-160`). An empty larder is not drawn, so no
    write carries the gap. The person is still short, and `_subsistence_shortfall` still says so.
    Pinned so that a later reading which reports the state instead is a deliberate edit, not a
    drift."""
    w = S.build()
    w.rungs[S.HUNGRY].stores = {}
    _, emitted = _matter(w)
    assert _shortfalls(emitted) == []
    assert w._subsistence_shortfall[S.POPULACE] == _want(S.COHORT_WEIGHT)


@pytest.mark.parametrize("build,seasons", [(P.tiny_world, 3), (lambda: HL.build_world(0), 3)])
def test_19d_the_shipped_worlds_record_no_shortfall(build, seasons):
    """WHY THE COMMITTED ARTIFACTS DO NOT MOVE ON THIS MECHANISM. ⚠ SINCE `24f` THESE TWO HAVE NO
    EATER AT ALL: neither seats a cohort, and only a cohort draws (`ED-IN-0255`, `H-171` limit 1),
    so no larder of theirs is ever drawn and nothing can be recorded -- asserted first, so this test
    says WHY it is green rather than being green by an accident it cannot see. (Before `24f`,
    `tiny_world`'s hearth met its mouths and `headless` held no dearth mid-draw.) The world that DOES
    eat is the populated realm, and its no-shortfall half is asserted in
    `tests/test_territorial_subsistence.py`'s drain guard: its first draw finds no stock (silent)
    and its second is in surplus."""
    w = build()
    assert world_q.subsistence_draw(w) == {}, (
        "this world has an eater now; the reason given above is stale and the no-shortfall claim "
        "below has become a measurement again")
    for _ in range(seasons):
        _season(w)
    assert _shortfalls(w.log) == []


def test_19d_an_observation_with_no_emission_is_refused_not_dropped():
    w = S.build()
    w.step = Step.MATTER
    r = w.rungs[S.HUNGRY]
    with pytest.raises(InstrumentDefect, match="no `emits=`"):
        w.write("stores", mint_token(w, WriteClass.MATTER), lambda: r.stores.update({"grain": 4}),
                record_kind="Rung", fieldname="stores", driver="Event",
                observed=(Observation(S.HUNGRY, f"{SHORTFALL_PREDICATE}:grain", 1),))


# ======================================================================================
# 3 -- THE DEPOSIT: whoever saw the write holds it
# ======================================================================================

def _held(w, pid, subject=S.HUNGRY) -> dict:
    return {c.predicate: (c.value, c.source) for c in w.persons[pid].ledger
            if c.subject == subject and str(c.predicate).startswith(f"{SHORTFALL_PREDICATE}:")}


def test_19d_the_holder_who_was_elsewhere_holds_the_shortfall_and_so_do_the_hungry():
    w = S.build()
    need, got = world_q.demanded(w, S.HUNGRY), world_q.delivered(w, S.HUNGRY)
    _season(w)
    want = {f"{SHORTFALL_PREDICATE}:{k}": need[k] - got[k] for k in need if need[k] > got[k]}
    steward, people = _held(w, S.STEWARD), _held(w, S.POPULACE)
    assert {k: v for k, (v, _) in steward.items()} == want
    assert {src for _, src in steward.values()} == {"told_by"}, (
        "the steward was not at the larder; he holds it through the document channel")
    assert {k: v for k, (v, _) in people.items()} == want
    assert {src for _, src in people.values()} == {"firsthand"}


def test_19d_control_without_the_hold_the_steward_learns_nothing():
    w = S.build(steward_holds=False)
    _season(w)
    assert _held(w, S.STEWARD) == {}
    assert not [c for c in w.persons[S.STEWARD].ledger if c.subject == S.HUNGRY], (
        "with no `hold` on the hungry town and no presence there, nothing about it reaches him")
    assert _held(w, S.POPULACE), "the shortfall was still recorded and seen where it happened"


def test_19d_the_none_arm_deposits_no_shortfall():
    w = S.build(fixtures=DEFAULT_FIXTURES.sweep("observation_deposit_mode", "none"))
    _season(w)
    assert _held(w, S.STEWARD) == {} and _held(w, S.POPULACE) == {}
    assert _shortfalls(w.log), "the record was still made; only its deposit is the arm's"


def test_19d_an_acts_reads_still_reach_only_its_actor():
    """THE ACTORLESS CLAUSE DID NOT WIDEN AN ACT'S DEPOSIT. A clerk standing in the granary witnesses
    the steward's `transfer.made` (`co_located`) and must NOT receive the fold's reads, which are the
    steward's (`H-122`'s `actor` arm). The same clerk DOES receive what MATTER read at his own
    larder, had it run dry; here it does not, so only the act half is asked."""
    w = S.build(seed=4)   # seed re-picked at B06.99: the stream changed (was 0; seeds 1..8 scanned, 4 is the first where the steward transfers)
    w.persons["p_clerk"] = Person("p_clerk", "a clerk")
    w.rungs["p_clerk"] = Rung("p_clerk", "person")
    w.add_tenure(Tenure("t_clerk_in", "p_clerk", S.GRANARY, "contain", 0))
    d = _season(w)
    real = _chooser(w)
    only_steward = lambda p, v, s, b: real(p, v, s, b) if p.id == S.STEWARD else []
    q = S.shortfall_question(w, S.STEWARD)
    n = len(d.resolved)
    _season(w, only_steward, q, d)
    made = [a for a in d.resolved[n:] if a.verb == "transfer" and a.actor == S.STEWARD]
    assert made, "the steward did not transfer; the clause below would be vacuous"
    stem = "stores:"
    steward_reads = [c for c in w.persons[S.STEWARD].ledger
                     if c.subject == S.GRANARY and str(c.predicate).startswith(stem)]
    clerk_reads = [c for c in w.persons["p_clerk"].ledger
                   if c.subject == S.GRANARY and str(c.predicate).startswith(stem)]
    assert steward_reads and not clerk_reads, (steward_reads, clerk_reads)
    assert any(c.predicate == "transfer.made" for c in w.persons["p_clerk"].ledger), (
        "the clerk must have WITNESSED the act, or the absence above proves nothing")


# ======================================================================================
# 4 -- THE OPERANDS: `kind` and `amount` read off the claim
# ======================================================================================

def _claim(pid, predicate, value, subject=S.HUNGRY, cid="c_short"):
    return Claim(cid, pid, subject, predicate, value, 0, "told_by", 100, "own")


def _asked(w, pid, predicate, value, cid="c_short"):
    p = w.persons[pid]
    p.ledger.append(_claim(pid, predicate, value, cid=cid))
    return p, Question(f"q:claim:{cid}", "claim_landed", (S.HUNGRY,), cid)


def test_19d_kind_and_amount_are_read_off_a_held_shortfall_claim():
    w = S.build()
    p, q = _asked(w, S.STEWARD, f"{SHORTFALL_PREDICATE}:salt", 8)
    assert _derive_operand(p, "kind", q, S.HUNGRY, w.fixtures) == "salt"
    assert _derive_operand(p, "amount", q, S.HUNGRY, w.fixtures) == 8
    # `to` is the referent -- the claim's own subject -- and `from` is where he stands.
    assert _derive_operand(p, "to", q, S.HUNGRY, w.fixtures) == S.HUNGRY
    assert _derive_operand(p, "from", q, S.HUNGRY, w.fixtures) == S.GRANARY


def test_19d_the_claim_answers_only_the_two_names_its_roster_declares():
    assert SHORTFALL_SOURCED_OPERANDS == frozenset({"kind", "amount"})
    assert SHORTFALL_SOURCED_OPERANDS <= REQUIRES_OPERANDS
    w = S.build()
    p, q = _asked(w, S.STEWARD, f"{SHORTFALL_PREDICATE}:grain", 15)
    for name in sorted(REQUIRES_OPERANDS - SHORTFALL_SOURCED_OPERANDS):
        assert _from_shortfall_claim(p, q, name) is None, name


@pytest.mark.parametrize("bad", [0, -3, True, 2.5, "8", None])
def test_19d_an_amount_that_is_not_a_positive_whole_number_falls_back_to_the_fixture(bad):
    w = S.build()
    p, q = _asked(w, S.STEWARD, f"{SHORTFALL_PREDICATE}:grain", bad)
    assert _derive_operand(p, "amount", q, S.HUNGRY, w.fixtures) == w.fixtures.get(
        "default_transfer_amount")
    assert _derive_operand(p, "kind", q, S.HUNGRY, w.fixtures) == "grain", (
        "a bad amount does not unmake the kind the claim names")


@pytest.mark.parametrize("predicate", ["stores:salt", "stores.changed", SHORTFALL_PREDICATE,
                                       f"{RECORD_CONTENT['predicate']}:petition"])
def test_19d_a_claim_that_is_not_a_shortfall_reads_nothing(predicate):
    w = S.build()
    p, q = _asked(w, S.STEWARD, predicate, 8)
    assert _from_shortfall_claim(p, q, "kind") is None
    assert _from_shortfall_claim(p, q, "amount") is None


def test_19d_the_rosters_refuse_a_second_vocabulary():
    with pytest.raises(Unspecified, match="shortfall_sourced_operands"):
        _check_operand_subset(frozenset({"kind", "at"}), frozenset(REQUIRES_OPERANDS),
                              "shortfall_sourced_operands")
    content = RECORD_CONTENT["predicate"]
    for stem in ("stores", content, None, "", "short:fall"):
        with pytest.raises(Unspecified):
            _check_shortfall_stem(stem, REQUIRES_STEMS, content)
    _check_shortfall_stem(SHORTFALL_PREDICATE, REQUIRES_STEMS, content)   # the shipped stem passes


# ======================================================================================
# 5 -- THE CHAIN: the real chooser and the real fold execute the claim-sourced transfer
# ======================================================================================

def _chooser(w):
    """The shipped decision policy, built as every harness builds it."""
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    return make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                        draw=draw_factory(w.world_seed, lambda: w.tick))


def test_19d_the_shortfall_question_forms_the_transfer_the_claim_describes_and_its_neighbour_does_not():
    """THE CONTROL FOR *the claim, not the fixture, set the operands*: the same person, the same
    referent, the same season. The question about the shortfall claim gives its kind and amount; the
    question about the event-kind `stores.changed` claim on the same rung gives the fixtures'."""
    w = S.build()
    _season(w)
    st = w.persons[S.STEWARD]
    by_id = {c.id: c for c in st.ledger}
    qs = world_q.questions_for(w, st)
    shortfall_qs = [q for q in qs if str(by_id[q.about].predicate).startswith(
        f"{SHORTFALL_PREDICATE}:")]
    neighbour = [q for q in qs if by_id[q.about].predicate == "stores.changed"
                 and by_id[q.about].subject == S.HUNGRY]
    assert len(shortfall_qs) == 2 and neighbour, [(q.about, by_id[q.about].predicate) for q in qs]

    def transfer_ops(q):
        (c,) = [c for c in opening_set(st, View(st.id, [], 99, q), q, w.fixtures)
                if c.verb == "transfer"]
        return c.operands

    for q in shortfall_qs:
        claim = by_id[q.about]
        ops = transfer_ops(q)
        assert (ops["to"], ops["from"]) == (S.HUNGRY, S.GRANARY)
        assert (f"{SHORTFALL_PREDICATE}:{ops['kind']}", ops["amount"]) == (claim.predicate,
                                                                          claim.value)
    ops = transfer_ops(neighbour[0])
    assert (ops["kind"], ops["amount"]) == (w.fixtures.get("default_store_kind"),
                                            w.fixtures.get("default_transfer_amount"))


def test_19d_the_real_chooser_executes_the_claim_sourced_transfer_and_matter_is_conserved():
    """The season's question is named (the driver's probe override); everything else is shipped:
    `make_chooser`'s score and packing, the fold, the gate. WHICH question a person answers is
    `H-54`'s open rule, and `harness/scarce.py::run` states what happens when it is not named."""
    treated, control = S.build(seed=4), S.build(seed=4)   # seed re-picked at B06.99: the stream changed (was 0)
    d_t, d_c = _season(treated), _season(control)
    q = S.shortfall_question(treated, S.STEWARD)
    claim = next(c for c in treated.persons[S.STEWARD].ledger if c.id == q.about)
    n = len(d_t.resolved)
    _season(treated, _chooser(treated), q, d_t)
    _season(control, P.NOCHOOSE, None, d_c)
    made = [a for a in d_t.resolved[n:] if a.verb == "transfer" and a.actor == S.STEWARD]
    assert made, "the steward, deliberating the shortfall, chose no transfer"
    ok = {e.causes[0] for e in treated.log if e.kind == "transfer.made"}
    fed = [a for a in made if a.id in ok and a.payload["to"] == S.HUNGRY]
    assert len(fed) == 1, [(a.payload, a.id in ok) for a in made]
    ops = fed[0].payload
    assert ops["from"] == S.GRANARY
    assert (f"{SHORTFALL_PREDICATE}:{ops['kind']}", ops["amount"]) == (claim.predicate, claim.value)
    # THE MATTER ARRIVED AND NONE WAS MINTED: the hungry larder holds what was sent, and the world's
    # total is the no-act control's (both ran the identical MATTER; RESOLVE is the only difference).
    assert treated.rungs[S.HUNGRY].stores.get(ops["kind"], 0) == ops["amount"]
    assert _mass(treated) == _mass(control)


def test_19d_the_next_season_delivers_more_where_the_steward_holds_the_town():
    """THE OBSERVABLE G3 IS FOR: `delivered` at the hungry town rises the season after a shortfall is
    seen by someone who can answer it. CONTROL: the same world without the `hold` edge. Nobody who
    can give ever learns of the dearth, and nothing arrives."""
    treated = S.run(3, seed=4)   # seed re-picked at B06.99: the stream changed (was 0)
    control = S.run(3, w=S.build(seed=4, steward_holds=False))
    sent = [t for s in treated["seasons"] for t in s["transfers"]
            if t["claim_sourced"] and t["outcome"] == "transfer.made"]
    assert sent, treated["seasons"]
    t_after = treated["seasons"][2]["delivered"]
    c_after = control["seasons"][2]["delivered"]
    assert sum(t_after.values()) > sum(c_after.values()) == 0, (t_after, c_after)
    assert not [t for s in control["seasons"] for t in s["transfers"] if t["claim_sourced"]]


# ======================================================================================
# AN AMOUNT IS A POSITIVE WHOLE NUMBER (H-306; 07_SE_kernel_repairs A)
# ======================================================================================

@pytest.mark.parametrize("value", [-5, 0, 1, 2.5, True])
def test_h306_only_a_whole_positive_transfer_amount_moves_stock(value):
    """Through the real fold on `scarce.build`: only `1` moves stock; every other value emits
    `transfer.refused` and leaves every rung's stores and the content hash equal to the no-act arm.
    Today `-5`, `2.5` and `True` move stock (H-306)."""
    def at_resolve():
        w = S.build()
        d = SeasonDriver(w)
        d.matter(mint_token(w, WriteClass.MATTER), [])
        w.step = Step.RESOLVE
        return w, d

    control, _ = at_resolve()
    w, d = at_resolve()
    out = d._fold(w, mint_token(w, WriteClass.ACTS), Act(
        id="tr_whole", actor=S.STEWARD, verb="transfer",
        payload={"subject": S.GRANARY, "from": S.GRANARY, "to": S.HUNGRY, "kind": "grain",
                 "amount": value}))
    kinds = [e.kind for e in out]
    stores = {r: dict(w.rungs[r].stores) for r in (S.GRANARY, S.HUNGRY)}
    before = {r: dict(control.rungs[r].stores) for r in stores}
    if value == 1 and value is not True:
        assert "transfer.made" in kinds and "transfer.refused" not in kinds, kinds
        assert stores != before
    else:
        assert "transfer.refused" in kinds and "transfer.made" not in kinds, (value, kinds)
        assert stores == before, value
        assert w.content_hash() == control.content_hash(), value


# ======================================================================================
# 4 -- THE WALK (B12a.53, H-303): the remainder goes on up the ladder under `larder_walk` `through`
# ======================================================================================

def _h303_world(walk: str):
    """H-303's pair: a cohort of 6 wanting one grain each, 1 grain at home, 1,000 on the rung above."""
    w = S.build(fixtures=DEFAULT_FIXTURES.sweep("subsistence_weight", {"grain": 1}).sweep("larder_walk", walk))
    w.persons[S.POPULACE].weight = 6
    w.rungs[S.HUNGRY].stores = {"grain": 1}
    w.rungs["terr_march"].stores = {"grain": 1000}
    return w


def test_h303_first_takes_one_through_takes_six_and_splits_the_debit():
    for walk, take, home_left, above_left in (("first", 1, 0, 1000), ("through", 6, 0, 995)):
        w = _h303_world(walk)
        (_, cells), = world_q.subsistence_draw(w).values()
        assert cells["grain"] == (6, take, S.HUNGRY), (walk, cells)
        assert world_q.delivered(w, S.HUNGRY) == {"grain": take}
        _matter(w)
        assert w.rungs[S.HUNGRY].stores.get("grain", 0) == home_left, walk
        assert w.rungs["terr_march"].stores["grain"] == above_left, walk
        # the two debits sum to the take: no matter made or lost by the split
        assert 1001 - w.rungs[S.HUNGRY].stores.get("grain", 0) - w.rungs["terr_march"].stores["grain"] == take, walk


def test_takes_sum_to_what_was_held():
    """B12b.39: three cohorts of weight 6 want 6 grain each on a rung holding 7: the shares and the drawn remainder hand out exactly 7 and MATTER leaves the
    rung at zero; on a rung holding 30 they take their 18 and 12 stays. Nothing is made or lost by the split."""
    from ..boot.realm import place_person
    for held, taken, left in ((7, 7, 0), (30, 18, 12)):
        w = S.build(fixtures=DEFAULT_FIXTURES.sweep("subsistence_weight", {"grain": 1}))
        w.persons[S.POPULACE].weight = 6
        for pid in ("p_b", "p_c"):
            place_person(w, pid, pid, S.HUNGRY, weight=6)
        w.rungs[S.HUNGRY].stores = {"grain": held}
        draw = world_q.subsistence_draw(w)
        assert len(draw) == 3, "the plant holds fewer than three eating cohorts"
        assert sum(cells["grain"][1] for _, cells in draw.values()) == taken, draw
        _matter(w)
        assert w.rungs[S.HUNGRY].stores.get("grain", 0) == left


# ======================================================================================
# THE SHARE A STORE MOVE TAKES (B12b.19; `07_SE_arc_needs` (b); A-56, A-81)
# ======================================================================================

def _requisitions_of(w, claim_stock=None):
    """The Duke's computed `requisition` candidates on the larder world, through the real `opening_set`. `claim_stock` plants the `stores:grain` claim the
    share reads (CR-23's report of the giving rung's level, held in his own ledger); `None` plants none."""
    from .test_u7_remit import DUKE
    p = w.persons[DUKE]
    if claim_stock is not None:
        p.ledger.append(Claim("c_stock_s", DUKE, "S", "stores:grain", claim_stock, w.tick, "firsthand", 100, "own"))
    out = []
    for q in world_q.questions_for(w, p, since=(w.tick, 0)):
        out += [c for c in opening_set(p, View(p.id, [], 12, q), q, w.fixtures) if c.verb == "requisition"]
    return out


def test_amount_shares_one_member_is_not_fanned():
    """THE CONTROL: the shipped roster has one member, so no `requisition` candidate carries an `amount_share`, the amount is the fixtures' and the act's id is
    what it was -- even with the giving rung's stock claim held (the share is read only where it was chosen)."""
    from ..data.verbs import CHOICE_RANGES
    from .test_u7_remit import _larder_world
    assert len(CHOICE_RANGES["amount_share"]) == 1
    w, _d = _larder_world()
    cands = _requisitions_of(w, claim_stock=40)
    assert cands and all("amount_share" not in c.operands for c in cands), [c.operands for c in cands]
    assert {c.operands["amount"] for c in cands} == {w.fixtures.get("default_transfer_amount")}


def test_two_members_fan_two_candidates_differing_only_in_amount(monkeypatch):
    """TWO MEMBERS (`250`, `1000`): the one requisition becomes two, each carrying its share, differing only in `amount` (and the key that names the share): a quarter and
    the whole of the stock he holds a claim of, `max(1, stock x share // 1000)`. With no stock claim held the amount falls back to the fixtures' on both."""
    from ..data.verbs import CHOICE_RANGES, act_key
    from .test_u7_remit import STOCK, _larder_world
    monkeypatch.setitem(CHOICE_RANGES, "amount_share", ("250", "1000"))
    w, _d = _larder_world()
    cands = _requisitions_of(w, claim_stock=STOCK)
    by_share = {c.operands["amount_share"]: c for c in cands}
    assert sorted(by_share) == ["1000", "250"] and len(cands) == 2, [c.operands for c in cands]
    assert by_share["250"].operands["amount"] == STOCK // 4 and by_share["1000"].operands["amount"] == STOCK
    rest = [{k: v for k, v in c.operands.items() if k not in ("amount", "amount_share")} for c in cands]
    assert rest[0] == rest[1] and len({act_key("requisition", c.operands["subject"], c.operands) for c in cands}) == 2     # two acts, two ids
    w2, _d2 = _larder_world()
    bare = _requisitions_of(w2)
    assert len(bare) == 2 and {c.operands["amount"] for c in bare} == {w2.fixtures.get("default_transfer_amount")}


def test_a_refused_requisition_leaves_a_claim_of_the_refusal():
    """A-81: a requisition asking more than the larder holds is refused at `stores`, and WITNESS leaves the requisitioner a firsthand claim `(larder, requisition.refused,
    doer = himself)`: the carrier `a_refusal_is_remembered` reads. CONTROL: a requisition within the stock is taken and leaves no such claim."""
    from .test_u7_remit import DUKE, STOCK, _fold, _kinds, _larder_world, _requisition

    def after(amount, key="rq"):
        w, d = _larder_world()
        out = _fold(w, d, _requisition(key, subject="S", amount=amount))
        d.witness(mint_token(w, WriteClass.INTERIOR), out)
        return _kinds(out), [c for c in w.persons[DUKE].ledger if c.subject == "S" and c.predicate == "requisition.refused"]

    kinds, claims = after(STOCK + 1)
    assert kinds == ["requisition.refused"] and len(claims) == 1 and claims[0].doer == DUKE and claims[0].source == "firsthand", (kinds, claims)
    for n in range(40):     # the task draw (`task_draw_arm`) may lose a requisition that is within the stock; sweep the act's key to one it wins
        kinds, claims = after(5, f"rq{n}")
        if kinds == ["requisition.taken"]:
            break
    assert kinds == ["requisition.taken"] and claims == []


def test_build_leaves_no_zero_key_in_the_payer_stores():
    """B12b.28 (U5d_SE §9 d): a `build`'s debit drops a kind it brings to 0 from the payer's stores, as `provision.py`
    leaves a zero out. The payer's stock is planted at exactly the price (every priced kind emptied) and at the price plus
    one (CONTROL: the kind stays, at one). The rest of the stores are read as before."""
    from .test_works_founding import HEARTH, _build, _declare, _fold, _kinds, _stock, _world
    price = DEFAULT_FIXTURES.get("works_cost")["dwelling"]
    after = {}
    for extra in (0, 1):
        w, d = _world()
        _declare(w, d, "wb", "dwelling", HEARTH)
        _stock(w, HEARTH, "dwelling")
        for kind in price:
            w.rungs[HEARTH].stores[kind] += extra
        rest = {k: v for k, v in w.rungs[HEARTH].stores.items() if k not in price}
        assert _kinds(_fold(w, d, _build("b1", "wb"))) == ["site.built"]
        stores = w.rungs[HEARTH].stores
        assert {k: v for k, v in stores.items() if k not in price} == rest
        after[extra] = {k: stores.get(k) for k in price}
    assert all(v is None for v in after[0].values()), after[0]
    assert after[1] == {k: 1 for k in price}, after[1]
