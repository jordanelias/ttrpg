"""Plan position `19d` -- DEMAND · DELIVERY. `workplans/2026-09-28-the-plan-one-order-mc-v18-retired.md`
§3.2 row 11: *"the retirement plan's ADJACENT G3: `demanded` / `delivered`, plus the scarce test world.
Gate `15c` (its operands). Beside `24f`, whose territorial quantity it feeds"*. The retirement plan's G3:
*"No new verb: two new read-only queries (`demanded`, `delivered`) plus wiring the existing `transfer`
verb's operands from a shortfall claim."*

What the position built, each asked of the real MATTER barrier, the real WITNESS and the real fold:
  1. `world_q.subsistence_draw` -- the ONE owner of the larder draw's arithmetic, extracted from
     MATTER. MATTER derives its writes from it; the two Queries sum it.
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
    Observation, _check_shortfall_stem, _check_writ_sourced_subset,
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
from ..state.carriers import Claim, Person, Question, Rung, Tenure, View
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
    d.season(choose, question=question, subsistence=P.SUBSIST,
             contest_max_depth=w.fixtures.get("contest_max_depth"))
    return d


def _mass(w) -> int:
    return sum(sum((r.stores or {}).values()) for r in w.rungs.values())


# ======================================================================================
# 1 -- THE QUERIES: the need, and what the ladder delivers against it
# ======================================================================================

def test_19d_demanded_is_the_weighted_headcount_under_a_rung():
    w = S.build()
    cohort, steward = _want(S.COHORT_WEIGHT), _want(1)
    assert world_q.demanded(w, S.HUNGRY) == cohort
    assert world_q.demanded(w, S.GRANARY) == steward
    # AN R-1 AGGREGATE OVER THE SUBTREE: the territory and the realm hold both settlements' mouths.
    both = {k: cohort[k] + steward[k] for k in cohort}
    assert world_q.demanded(w, "terr_march") == both
    assert world_q.demanded(w, "r_realm") == both
    # `Person.weight` IS THE HEADCOUNT: one cohort of ten wants what ten people want.
    assert cohort == {k: v * S.COHORT_WEIGHT for k, v in steward.items()}


def test_19d_delivered_is_the_draw_against_the_stores_as_they_stand():
    w = S.build()
    stock = dict(w.rungs[S.HUNGRY].stores)
    got = world_q.delivered(w, S.HUNGRY)
    assert got == {k: min(v, stock.get(k, 0)) for k, v in _want(S.COHORT_WEIGHT).items()}
    assert world_q.delivered(w, S.GRANARY) == _want(1), "the stocked granary feeds its steward"
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
    # CONTROL: the granary was drawn too (its steward ate), met its mouth, and carries nothing.
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
    """WHY THE COMMITTED ARTIFACTS DO NOT MOVE. `tiny_world`'s hearth meets its mouths and its salt
    is never stocked anywhere (`source None`: silent); `headless` holds no dearth mid-draw. Measured
    out-of-band, because each costs minutes: the populated realm (its first draw precedes its first
    yield, and it is in surplus after), and the corpus's 178 built worlds (0 shortfalls recorded)."""
    w = build()
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
    w = S.build()
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
        _check_writ_sourced_subset(frozenset({"kind", "at"}), frozenset(REQUIRES_OPERANDS),
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
    treated, control = S.build(), S.build()
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
    treated = S.run(3)
    control = S.run(3, w=S.build(steward_holds=False))
    sent = [t for s in treated["seasons"] for t in s["transfers"]
            if t["claim_sourced"] and t["outcome"] == "transfer.made"]
    assert sent, treated["seasons"]
    t_after = treated["seasons"][2]["delivered"]
    c_after = control["seasons"][2]["delivered"]
    assert sum(t_after.values()) > sum(c_after.values()) == 0, (t_after, c_after)
    assert not [t for s in control["seasons"] for t in s["transfers"] if t["claim_sourced"]]
