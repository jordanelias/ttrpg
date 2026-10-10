"""The covering test file for the governance/settlements/decisions build programme.

WHY A SECOND FILE RATHER THAN A 11,187th LINE IN `test_season_shape.py`. `CLAUDE.md` §0.4
clause 2 -- *"mid-session, run only the file covering what you touched"* -- is only cheap when
that file is small. `test_season_shape.py` is the INSTRUMENT'S OWN adversarial test: its subject
is whether the tracer flatters the shape. The subject here is different -- whether an item of
`proposals/2026-09-17-governance-and-behaviour/01_THE_BUILD_ORDER.md` actually executes -- so the
two are not the same object, and §4's split test (*can a reader work with it*) answers the rest.

EVERY TEST HERE CARRIES ITS ITEM'S FALSIFIER ID from that build order's sheet (`LB-n`), and each
observes BOTH halves of its item's claim. A test that observes only the write is the half-wiring
this programme is full of.

Run: python -m pytest engine/season/tests/test_governance_build.py -q
"""

from __future__ import annotations

import ast
import dataclasses

import pytest

from collections import Counter

from ..data import files
from ..data.matrix import MATRIX, Step, WriteClass
from ..data.rosters import CONFERRAL_BASES, REVOCATION_BASES, RUNG_KINDS, TITLE_DOMAINS, title_domain
from ..data.verbs import VERB_TABLE, align
from ..epistemic import CHANNEL_PREDICATES, observers_for
from ..gaps import Forbidden, Unowned, Unspecified
from ..data.cast import faction_leader
from ..harness.populated import build_realm
from ..loop import predicates as _preds
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..loop.predicates import in_holdings, office_described_by
from ..queries import world_q
from ..harness import probes as P
from ..state.attribution import anchor_of
from ..decision import budget as _budget
from ..decision import operands_for, person_side_eligible
from ..state.carriers import (
    Act, Claim, Office, Person, Proposition, Rung, Site, Tenure, View,
    matrix_rows_without_a_field, refuse_a_title_in_a_body,
)


# ---------------------------------------------------------------------------
# ITEM 1 (plan position `7a`) -- `@effect_for("commit")`, SHIPPED at G4 after BO-10's gate
# (`15`/`15c`/`15b`). Falsifier LB-1, in two halves: the mechanism, isolated on a hand-built world
# where a Proposition referent genuinely exists; and BO-9/BO-10's own re-measurement on the
# populated corpus, reported HONESTLY rather than repaired.
# ---------------------------------------------------------------------------


def test_lb1_commit_opens_a_tenure_and_q4_then_sees_it():
    """**LB-1, half one — THE MECHANISM.** `commit`'s row (`verb_table.yaml`) is `own`-eligible,
    `beneficiary: actor`, typed `existence(of: subject, kind: Proposition)`,
    `writes: ["Tenure.since"]`, `emits: ["commitment.made"]`. Given a genuine Proposition referent
    (which BO-9/BO-10 found no live question source supplies, below), the effect must open a live
    `commit` Tenure -- subject the actor, object the Proposition -- AND a downstream reader must
    then see it: Q4 (`queries/world_q.py::questions_for`) raises a standing "need" question from
    every live `commit` to an OUGHT. A test observing only the write is the half-wiring this file
    exists to refuse."""
    w = P.tiny_world()
    w.propositions["prop_want"] = Proposition("prop_want", "OUGHT", "p_mid", "wants a raise",
                                              None, 0)
    d = SeasonDriver(w)
    out = d.resolve(mint_token(w, WriteClass.ACTS),
                    [Act(id="c_lb1", actor="p_mid", verb="commit",
                         payload={"subject": "prop_want"})],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert [e.kind for e in out] == ["commitment.made"], (
        f"commit on a live Proposition did not report a clean success: {[e.kind for e in out]}")
    nt = next((t for t in w.tenures if t.kind == "commit" and t.object == "prop_want"), None)
    assert nt is not None and nt.subject == "p_mid" and nt.live, (
        "no live `commit` Tenure opened naming the actor as subject and the Proposition as object")

    w.tick = 1
    qs = world_q.questions_for(w, w.persons["p_mid"])
    assert any(q.source == "need" and q.about == "prop_want" for q in qs), (
        f"Q4 did not raise a standing question from the new `commit` Tenure: "
        f"{[(q.source, q.about) for q in qs]}")


def test_lb1_commit_refuses_a_proposition_that_does_not_exist():
    """**LB-1, the refusal path.** The row's own `refusal_note`: *the Proposition does not exist
    (§14 -- immutable, must be uttered first)*. This is the typed precondition's, asked before the
    effect ever runs (`loop/resolve.py::_admits`) -- so a `commit` naming an id that names no
    Proposition never reaches `_eff_commit` at all and opens nothing."""
    w = P.tiny_world()
    d = SeasonDriver(w)
    out = d.resolve(mint_token(w, WriteClass.ACTS),
                    [Act(id="c_lb1r", actor="p_mid", verb="commit",
                         payload={"subject": "prop_nonexistent"})],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert [e.kind for e in out] == ["commitment.refused"], (
        f"commit on a nonexistent Proposition did not refuse cleanly: {[e.kind for e in out]}")
    assert not any(t.kind == "commit" for t in w.tenures), (
        "a refused `commit` still opened a Tenure")


def test_lb1_removing_the_effects_body_mints_no_tenure(monkeypatch):
    """**LB-1's own control, isolating the effect as the producer.** With `EFFECTS["commit"]`
    replaced by a stub returning `NO_CHANGE` -- "the effect with its body removed" -- the IDENTICAL
    act that opens a Tenure in the mechanism test above must not. Without this, the Tenure seen
    there could in principle come from `add_tenure` being reached some other way; this confirms it
    comes from `_eff_commit` and nothing else."""
    from ..loop.effects import EFFECTS
    from ..state.gate import NO_CHANGE
    w = P.tiny_world()
    w.propositions["prop_want"] = Proposition("prop_want", "OUGHT", "p_mid", "wants a raise",
                                              None, 0)
    monkeypatch.setitem(EFFECTS, "commit", lambda w, a, res=None: NO_CHANGE)
    d = SeasonDriver(w)
    out = d.resolve(mint_token(w, WriteClass.ACTS),
                    [Act(id="c_lb1c", actor="p_mid", verb="commit",
                         payload={"subject": "prop_want"})],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert [e.kind for e in out] == ["commitment.refused"], (
        f"a no-op effect body did not read as the fold's own no-op refusal: {[e.kind for e in out]}")
    assert not any(t.kind == "commit" for t in w.tenures), (
        "a stubbed-out effect still minted a Tenure -- something else is opening it")


def test_lb1_bo10_gate_closed_by_in11_the_utterers_hold_report_not_repair():
    """**LB-1, half two — BO-9/BO-10's OWN RE-MEASUREMENT, HONEST RATHER THAN REPAIRED.**
    `01_THE_BUILD_ORDER.md` §7.2 measured `commitment.made: 0 / commitment.refused: 42` on one
    populated season before this effect shipped, diagnosed as structural: no source in
    `questions_for` offers a Proposition as a REFERENT (`decision/options.py::_REFERENT_OPERANDS`
    binds `commit`'s `subject` to the question's referent, and every live referent today is a
    person id), and BO-10 named items 5/7/8 (`15`/`15c`/`15b`) as what would open that channel.

    ⚠ HISTORY, SUPERSEDED BY THE v9 IN-11 PARAGRAPH BELOW -- this paragraph records the state
    BEFORE IN-11 and no longer describes what the test asserts. THEY WERE ALL DONE, AND THE GATE WAS
    STILL SHUT. `15c`'s operand-widening
    (`decision/options.py::_derive_operand`) answers `to`/`kind`/`amount` from a held writ's
    content; `15b`/`15`'s content-claim/deposit machinery widens which `claim_landed` questions
    REACH a person (`world_q.questions_for`'s clause 3, `named(c)`). Neither touches `subject`,
    which stays a bare `_REFERENT_OPERANDS` bind to the question's own referent. So `commit`'s
    typed cell (`existence(of: subject, kind: Proposition)`) still asks about a person id and
    still refused, every time, on this corpus. **This test then asserted that gap was still open, on
    purpose** — the falsifier this position's brief named explicitly refuses to invent a repair
    (widening Q4 was tried and refused in §7.2, with its own measurement: 1 made / 57 refused,
    because a standing question cannot be the producer of the commitment that raises it). The one
    thing that DID move is `resolvable_verbs()`, which is asserted moving the other way.

    ⚠⚠ v9 IN-11 (#453 §10.4 step 2) CLOSED THE GATE, AND THIS TEST NOW ASSERTS THE CLOSURE -- UPDATED
    AS ITS OWN MESSAGE ASKED, NOT RE-PINNED SILENTLY. The producer is not a widened Q4 (the refused
    repair above) and not a new operand: `_eff_utter` opens the utterer's `hold` on the Proposition,
    so it is in his `reach` (limb 2) and Q2 raises his own claim about it as a question whose
    referent IS the Proposition -- `subject` still binds to the referent, unchanged. MEASURED, this
    season: `commitment.made` 2 where it was 0, `commitment.refused` 38 where it was 35 (the old
    person-id referents still form and refuse; `H-156`'s (a)/(b) stays registered). The full
    falsifier is `test_in11_utter_hold_commit.py`."""
    from collections import Counter
    from ..decision import make_chooser
    from ..state.ids import H, draw_factory
    w = build_realm(0)
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    chooser = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                           draw=draw_factory(w.world_seed, lambda: w.tick))
    d.season(chooser, question=None, subsistence=P.SUBSIST,
             contest_max_depth=w.fixtures.get("contest_max_depth"))
    kinds = Counter(e.kind for e in w.log)

    assert "commit" in resolvable_verbs(), (
        "`commit` dropped back out of `resolvable_verbs()` -- the effect registration regressed")
    commit_acts = [a for a in d.resolved if a.verb == "commit"]
    assert commit_acts, "no `commit` act formed at all on this corpus -- the gate moved further"
    referents_seen = {(a.payload or {}).get("subject") for a in commit_acts}
    assert referents_seen & set(w.propositions), (
        f"no `commit` act named a real Proposition as its subject -- IN-11's utterer's hold no "
        f"longer reaches a question: {referents_seen}")
    assert kinds.get("commitment.made", 0) >= 1, (
        f"commitment.made is {kinds.get('commitment.made', 0)} -- BO-10's gate re-opened; IN-11's "
        "closure regressed")
    assert kinds.get("commitment.refused", 0) > 0, (
        "no `commit` refusals at all -- the verb stopped being attempted, which is a different "
        "regression from the one this test documents")


# ---------------------------------------------------------------------------
# ITEM 2 (position `11a`) -- `reach`, `place_of`, the two-source `questions_for` fold.
# r2 `01_ATTENTION_AND_REACH.md` §A.3-§A.4, `05_LEDGER_AND_BUILD.md` §A.4.1 item 2.
# Falsifiers LB-2b (the flood test) and LB-2e (the inclusive walk).
# ---------------------------------------------------------------------------

def test_lb2e_reach_includes_the_seats_own_rung_not_only_descendants():
    """**LB-2e — THE INCLUSIVE-WALK TEST** (`05` §A.4.1 item 2). `descendants(w, rung)` EXCLUDES
    `rung` itself (`state/containment.py`), so a `reach` limb written as a bare
    `descendants(seat.rung)` would silently lose the seat's own rung — a Duke seated at his own
    duchy would never be reached by a claim about the duchy itself. Limb 4 is
    `{seat.rung} | descendants(seat.rung)`, and this asserts both the set and the consequence: the
    duke is actually asked."""
    w = P.tiny_world()
    duke = w.persons["p_high"]
    assert w.offices["off_duke"].rung == "D", (
        "the fixture no longer seats the duke over D; the rest of this test assumes it")
    assert "D" not in world_q.descendants(w, "D"), (
        "the fixture assumption changed: `descendants` now includes its own rung, which would "
        "make the rest of this test vacuous")

    R = world_q.reach(w, duke)
    assert "D" in R, (
        "reach() lost the seat's own rung -- a bare `descendants(seat.rung)` form regressed")

    # AND THE CONSEQUENCE: a claim landing about the duke's own duchy rung raises Q2 for him.
    w.tick = 1
    duke.ledger.append(Claim("c_lb2e", duke.id, "D", "condition.worn", True, 0,
                              "firsthand", 100, "own"))
    qs = world_q.questions_for(w, duke)
    assert any(q.source == "claim_landed" and q.referents == ("D",) for q in qs), (
        f"the duke was not asked about a claim landing on his own duchy rung: "
        f"{[(q.source, q.referents) for q in qs]}")


def test_lb2b_a_duke_is_not_reached_by_a_crossing_in_his_purview_that_nobody_witnessed():
    """**LB-2b — THE FLOOD TEST, AND IT IS THE ONE THAT MATTERS** (`05` §A.4.1 item 2). `reach`
    must FILTER claims that already landed by a witness channel and never widen the fan: a crossing
    at the duke's OWN seat rung -- squarely inside his `reach`, per LB-2e above -- that nobody is
    present to witness must reach nobody's ledger, and therefore raise no question for him, no
    matter how wide his purview is. `01` §A.4.4: `reach` is applied to `p.ledger` and nothing else,
    and `observers_for` is untouched -- unaware `reach` exists at all."""
    w = P.tiny_world()
    duke = w.persons["p_high"]
    assert w.offices["off_duke"].rung == "D"
    assert "D" in world_q.reach(w, duke), (
        "the fixture no longer seats the duke's purview over D; the rest of this test assumes it")
    # Nobody in `tiny_world()` has a `contain` edge to `D` itself (`p_high` is at `S`, `p_king` at
    # `R`) -- a site placed directly at `D` is a crossing nobody is present to see.
    assert not world_q.presence(w, "D"), (
        "the fixture now puts somebody at D; this site would then be witnessed and the test would "
        "not be exercising the unwitnessed case")
    floor = w.fixtures.get("band_floors")["seam"]["surface_gleaning"]
    w.sites["s_lb2b"] = Site("s_lb2b", "D", "seam", condition=floor + 5)

    w.step = Step.MATTER
    evs = SeasonDriver(w).matter(mint_token(w, WriteClass.MATTER), [])
    crossing = next((e for e in evs if e.kind == "condition.band_crossed"
                     and anchor_of(w, e) == "s_lb2b"), None)
    assert crossing is not None, (
        "the seeded site did not cross its floor in one season; the fixture's wear rate or "
        "starting condition no longer matches this test's arithmetic")

    everyone = list(w.persons)
    for mode in ("presence_only", "all_five"):
        assert observers_for(w, crossing, mode, everyone) == [], (
            f"[{mode}] a crossing nobody was present for was witnessed by somebody -- `reach` "
            "must never be able to widen the WITNESS fan (`01` §A.4.4 clause 1)")
    assert not any(c.subject == "s_lb2b" for c in duke.ledger), (
        "a claim about the unwitnessed crossing reached the duke's ledger regardless")

    w.tick = 1
    qs = world_q.questions_for(w, duke)
    assert not any(q.about == crossing.id or "s_lb2b" in q.referents for q in qs), (
        "the duke was asked about a crossing nobody witnessed, even though it sits at his own "
        f"seat rung -- reach widened who is ASKED beyond who was TOLD: {qs}")


# ---------------------------------------------------------------------------
# ITEM 16 -- `add_tenure`'s hold domain/codomain guard (⊕ R13) + the faction holds
# re-homed to persons. Falsifier LB-16.
# ---------------------------------------------------------------------------

def test_lb16_a_faction_can_no_longer_hold_a_rung():
    """⊕ R13's DOMAIN half. `holonic §15`: *"`hold` | Person → Office | Rung | Record |
    Proposition"* -- a faction is a `Proposition`, so it is not in the domain.

    THE SHAPE THIS REFUSES RAN FOR MONTHS AND LOOKED FINE. It is the exact construction
    `harness/populated.py` used for every province in canon's starting-control table."""
    w = P.tiny_world()
    w.propositions["fac_x"] = Proposition("fac_x", "HOLDS", "X", "is a faction", True, 0)
    with pytest.raises(Forbidden):
        w.add_tenure(Tenure("t_bad", "fac_x", "D", "hold", 0))


def test_lb16_a_hold_may_not_reach_a_site():
    """⊕ R13's CODOMAIN half, and `05_LEDGER_AND_BUILD.md`'s own row for it: *"a `hold` never
    reaches a `Site` | **NOTHING today**"*. `Site` is the one class `holonic §15`'s row excludes
    that the world actually holds, so it is the only codomain violation that can be constructed."""
    w = P.tiny_world()
    with pytest.raises(Forbidden):
        w.add_tenure(Tenure("t_site", "p_low", "site_harbour", "hold", 0))


def test_lb16_an_unresolvable_id_still_passes_so_rehoming_still_works():
    """THE CONTROL, AND IT IS THE ONE THAT KEEPS THE GUARD FROM BEING TOO WIDE.

    `_rehome` exists because a Tenure may be added BEFORE its subject is a person. A guard
    refusing every unknown id would refuse the store's own construction sequence, so `class_of`
    returns `None` for "not yet" and `_refuse_bad_hold` reads that as PERMITTED. Without this
    test the guard could tighten to `subject in w.persons` and every ordering-tolerant fixture in
    the tree would start raising -- which is a real regression wearing a stricter rule's clothes."""
    w = P.tiny_world()
    w.add_tenure(Tenure("t_early", "p_not_yet", "off_x", "hold", 0))
    assert w._unowned, "the plant did not land in _unowned; the guard refused an ordering it should tolerate"


def test_lb16_build_realm_has_no_faction_holds_and_holdings_is_satisfiable():
    """**LB-16**, and BOTH halves, because either alone is the half-wiring.

    Half one: `build_realm` builds with **0** faction-subject holds -- the artifact the build
    order names. Half two, which is the one that matters: `in_holdings` is TRUE for at least one
    (person, rung) pair, so a seat declaring `revocation: "holdings"` can finally execute to True.
    Before this item it was **false for every person over every rung in the world**, forever,
    while looking exactly like a working precondition.

    ⚠ IT ASSERTS THAT IT ASSERTED (`CLAUDE.md` §0.1 pt 2). A loop over candidate (person, rung)
    pairs that finds none is indistinguishable from a loop whose body never ran, and `LB-10c` is
    named in the build order as the live case of exactly that."""
    w = build_realm(0)

    holds = [t for t in w.tenures if t.kind == "hold"]
    assert holds, "no hold Tenures at all -- the fixture changed and this test is measuring nothing"
    faction_held = [t for t in holds if w.class_of(t.subject) != "Person"]
    assert faction_held == [], f"{len(faction_held)} holds still have a non-person subject"

    checked = 0
    true_pairs = []
    for pid in w.persons:
        for rid in w.rungs:
            checked += 1
            if in_holdings(w, pid, rid):
                true_pairs.append((pid, rid))
    # ⚠ THE FLOOR IS DERIVED, NOT A NUMBER. An earlier draft asserted `checked > 1000` — a
    # magnitude nobody chose, which `tools/ci_sim_fabrication_check.py` correctly refused. The
    # exact product is stronger AND literal-free: it observes that the loop ran to COMPLETION
    # rather than merely that it ran a lot, so a sweep truncated by an early `break` fails here.
    assert checked == len(w.persons) * len(w.rungs), (
        f"the sweep examined {checked} of {len(w.persons) * len(w.rungs)} pairs; it did not run "
        "to completion, so an empty result below would be indistinguishable from a skipped body")
    assert true_pairs, (
        "`in_holdings` is false for every person over every rung -- item 16 did not land, and "
        "every `revocation: \"holdings\"` basis refuses forever")


def test_lb16_a_faction_with_no_authored_head_holds_nothing_and_it_is_counted():
    """THE COST OF THE RE-HOME, STATED RATHER THAN SWALLOWED.

    `Guilds` and `Schoenland` have no `leader:` in canon, so there is no person to re-home their
    provinces to and inventing one would put somebody canon does not name in charge of a
    territory. MEASURED: 16 provinces held before, **15 after**, and the one that drops is
    Schoenland's. The world reports it (`_unheld_for_want_of_a_head`) so an unheld province is a
    fact a reader can find rather than an arithmetic discrepancy they have to chase."""
    w = build_realm(0)
    assert hasattr(w, "_unheld_for_want_of_a_head")
    dropped = w._unheld_for_want_of_a_head
    assert dropped, (
        "nothing was dropped -- either canon grew the missing leaders, in which case delete this "
        "test, or the re-home silently invented a holder")
    assert all(fac for _, fac in dropped)
    # ⚠ THE ARITHMETIC IS A PARTITION, NOT A TOTAL. An earlier draft asserted `== 16` — the count
    # measured before the re-home, pinned into a test as a literal, which is the hard-coding
    # `tools/ci_sim_fabrication_check.py` exists to refuse and which would go stale the day canon
    # assigns one more province. The INVARIANT is what matters and it needs no number: the held
    # and the dropped are disjoint, and every drop is a faction canon genuinely gives no head.
    rung_holds = [t for t in w.tenures if t.kind == "hold" and w.class_of(t.object) == "Rung"]
    held_rungs = {t.object for t in rung_holds}
    dropped_rungs = {r for r, _ in dropped}
    assert held_rungs.isdisjoint(dropped_rungs), (
        f"a territory is both held and recorded as unheld: {held_rungs & dropped_rungs}")
    assert all(faction_leader(fac) is None for _, fac in dropped), (
        "a province was dropped for a faction that DOES have an authored head — the re-home "
        f"lost a holding it could have placed: {dropped}")


# ---------------------------------------------------------------------------
# ITEM 3a -- `nearest_store` and the per-eater draw. Falsifier LB-3a.
# ---------------------------------------------------------------------------

def _matter_once(w, *, keep_yield=False):
    """Run MATTER alone and return its Events.

    ⚠⚠ THE SITES ARE CLEARED UNLESS A CALLER ASKS OTHERWISE, AND THE FIRST WRITING OF THESE TESTS
    DID NOT DO THAT — every one of them failed, reporting a settlement that GAINED where a draw
    should have taken. The cause is `#353 §25`'s own barrier order: MATTER draws larders and THEN
    takes yield, in one call, so a bare `matter()` measures the NET of two steps and an assertion
    about the draw is reading a number the draw does not own.

    Removing the yield source is what makes the assertion observe the thing it names
    (`CLAUDE.md` §0.1 pt 2). The alternative — a paired no-eater control run, subtracting its
    yield — measures the same quantity at twice the runtime and puts a second run's arithmetic
    between the reader and the claim. `test_w8_matter_draws_before_it_produces_which_is_353s_
    stated_order` already owns the interaction of the two steps; these own the draw."""
    if not keep_yield:
        w.sites.clear()
    d = SeasonDriver(w)
    w.step = Step.MATTER
    return d.matter(mint_token(d.w, WriteClass.MATTER), [])


def _eaters_at(w, rung_id):
    """The EATERS standing at `rung_id` -- since plan position `24f`, its COHORTS only: a person at
    `weight == 1` is exempt from the larder draw (`world_q.subsistence_draw`, `ED-IN-0255`)."""
    return [pid for pid, home in world_q.home_of(w).items()
            if home == rung_id and w.persons[pid].is_cohort]


# The cohort planted at `S` by `_cohort_tiny_world`: `tiny_world` seats only its duke there.
S_COHORT = "c_people_of_s"


def _cohort_tiny_world():
    """`tiny_world`, RE-PLANTED FOR `24f`. Every LB-3 test below was written when every housed person
    ate, and `tiny_world` holds nobody at `weight > 1`, so under `24f` it has no eater at all
    (`H-171`). The ladder, the running view, the body write and the death cascade are unchanged, so
    the tests keep their subjects and move their eaters onto cohorts, the carrier the ruling names:
      * the three hearth residents at `Hh` become the smallest cohort (weight 2) -- the hearth's
        people, which is what three anonymous `p_low`/`p_mid`/`p_other` stood for;
      * one cohort is planted at `S` (`P.plant_cohort`), since its only resident is the duke, whom
        `24f` exempts.
    `p_high` (the duke) and `p_king` stay individuals and are the exemption's control here."""
    w = P.tiny_world()
    for pid, home in world_q.home_of(w).items():
        if home == "Hh":
            w.persons[pid].weight = 2
    P.plant_cohort(w, S_COHORT, "S")
    return w


def _heads(w, eaters):
    """Weight, not head count — `Person.weight` is the cohort multiplier."""
    return sum(w.persons[e].weight for e in eaters)


def decision_budget(w, pid):
    """What `decision.budget` gives this person right now — the READ side of `Person.body`."""
    p = w.persons[pid]
    return _budget(p, View(pid, [], w.fixtures.get("view_k")), w.fixtures.get("scene_budget"),
                   w.fixtures)


def _need(w, eaters):
    """Exactly what these eaters draw in one season, per kind, from the shipped weights.

    ⚠ EVERY LARDER IN THIS FILE IS STOCKED FROM THIS, never from a round number. A fixture stock
    of `40` is a magnitude nobody chose (and `tools/ci_sim_fabrication_check.py` refuses it), and
    it is the weaker assertion besides: *the settlement fell by the right amount* is satisfied by
    a range, while *the settlement is empty* is satisfied by one value."""
    return {k: wt * _heads(w, eaters) for k, wt in w.fixtures.get("subsistence_weight").items()}


def test_lb3a_a_hearth_with_no_larder_eats_from_its_settlement():
    """**LB-3a**, and it observes BOTH halves: the settlement's stores fall, AND the eaters are
    not short. Either alone is satisfiable by a half-wiring — a draw that takes nothing leaves
    nobody short only because nobody ate.

    THE DEFECT THIS CLOSES, measured on `build_realm(0)` before the change: **4,810 units, all of
    them at the 37 settlement rungs and none at the 211 hearths**, 46 persons in 26 hearths, and
    **0 rungs with both eaters and stores** — so the per-rung draw counted zero eaters wherever
    there was anything to eat, and the subsistence step was inert on the world that ships."""
    w = _cohort_tiny_world()
    w.rungs["Hh"].stores = {}                      # the hearth's own larder is bare
    eaters = _eaters_at(w, "Hh") + _eaters_at(w, "S")
    assert _eaters_at(w, "Hh"), "nobody lives in the hearth; this test would pass vacuously"
    # ⚠ STOCKED TO EXACTLY WHAT THESE EATERS NEED, never to a comfortable round number. An earlier
    # draft wrote `{"grain": 40, "salt": 30}` — magnitudes nobody chose, which
    # `tools/ci_sim_fabrication_check.py` correctly refused. Exact stock is also a STRONGER test:
    # it pins the draw to the unit instead of asserting it landed somewhere below 40.
    need = _need(w, eaters)
    w.rungs["S"].stores = dict(need)

    _matter_once(w)

    for k in need:
        assert w.rungs["S"].stores[k] == 0, (
            f"{k}: settlement kept {w.rungs['S'].stores[k]} of exactly the {need[k]} its people "
            "needed. The hearth-dwellers did not reach up the ladder, or drew the wrong amount")
    assert not [e for e in eaters if e in w._subsistence_shortfall], (
        f"an eater is short beside a settlement stocked to their exact need: "
        f"{w._subsistence_shortfall}")


def test_lb3a_control_a_hearth_with_its_own_larder_eats_locally_and_unchanged():
    """THE PAIRED CONTROL, and it is what makes the walk a GENERALISATION rather than a change.

    `nearest_store` returns the rung ITSELF where that rung has stock, so a hearth with a larder
    feeds its own people exactly as the per-rung loop did. **If this arm moves, the walk is not a
    generalisation** — it is a new rule wearing one's clothes, and every reading of the populated
    world would then be confounded by a second change nobody asked for."""
    w = _cohort_tiny_world()
    at_hh, at_s = _eaters_at(w, "Hh"), _eaters_at(w, "S")
    assert at_hh and at_s, "the fixture needs eaters at both rungs for the control to mean anything"
    # Each rung stocked to exactly ITS OWN eaters' need. If the walk reached past a stocked hearth,
    # or reached DOWN from the settlement, one of the two would end nonzero and the other short.
    w.rungs["Hh"].stores = dict(_need(w, at_hh))
    w.rungs["S"].stores = dict(_need(w, at_s))

    _matter_once(w)

    for k in _need(w, at_hh):
        assert w.rungs["Hh"].stores[k] == 0, (
            f"{k}: the hearth-dwellers did not eat locally from a larder they have")
        assert w.rungs["S"].stores[k] == 0, (
            f"{k}: the settlement fed somebody it should not have — the walk is reaching DOWN, "
            "or the hearth's own larder was skipped")
    assert not w._subsistence_shortfall.keys() & set(at_hh + at_s), (
        f"an eater is short where their own rung held exactly their need: "
        f"{w._subsistence_shortfall}")


def test_lb3a_the_root_larder_at_zero_feeds_nobody_and_raises_nothing():
    """A person under a realm that holds nothing goes hungry, and hunger is a fact about the
    world — not a `KeyError`, and not an `Unspecified`.

    `nearest_store` returns `None` at the root and the caller records a shortfall. Raising here
    would make an empty larder an instrument defect, and a season that dies on a bare world is a
    season nobody can run the starving case in."""
    w = _cohort_tiny_world()
    for rid in ("R", "D", "S", "Hh"):
        w.rungs[rid].stores = {}

    evs = _matter_once(w)                      # must not raise

    assert w._subsistence_shortfall, "nobody is short on a world with no food anywhere"
    # Since `24f` the eaters are the cohorts; the duke and the king, individuals, are neither fed
    # nor short -- they are not in the draw at all (`ED-IN-0255`).
    cohorts = {pid for pid in world_q.home_of(w) if w.persons[pid].is_cohort}
    assert set(w._subsistence_shortfall) == cohorts, (
        "some eater is neither fed nor recorded short — the loop skipped them silently — or an "
        "individual was counted short, which `24f` exempts")
    assert not {"p_high", "p_king"} & set(w._subsistence_shortfall)
    assert not [e for e in evs if e.kind == "stores.changed"], (
        f"a store changed on a world that holds nothing: {[anchor_of(w, e) for e in evs]}")


def test_lb3a_a_cohort_eats_by_its_weight_and_not_by_its_head_count():
    """`Person.weight` IS THE COHORT MULTIPLIER AND THE OLD LOOP DROPPED IT.

    `state/carriers.py`: *"A COHORT IS A PERSON AT weight > 1"*. The per-rung draw was
    `wt * len(eaters)`, so two hundred people eat like one man. Every person in the shipped corpus
    is at weight 1 — which is exactly why this was invisible, and why a test has to plant the
    cohort rather than wait for the corpus to grow one. (Since `24f` the realm's cohorts are
    `cohorts.yaml`'s; this test's cohort is still planted, one weight above its neighbours.)"""
    w = _cohort_tiny_world()
    w.rungs["Hh"].stores = {}
    eaters = _eaters_at(w, "Hh") + _eaters_at(w, "S")
    cohort = _eaters_at(w, "Hh")[0]
    w.persons[cohort].weight = len(eaters) + 1   # a cohort, distinguishable from any head count
    # Stocked to exactly the WEIGHTED need. A loop counting heads would draw strictly less and
    # leave a surplus, so the assertion below fails loudly rather than by a margin.
    need = _need(w, eaters)
    w.rungs["S"].stores = dict(need)

    _matter_once(w)

    assert w.rungs["S"].stores["grain"] == 0, (
        f"a cohort of {w.persons[cohort].weight} ate like one person: the settlement kept "
        f"{w.rungs['S'].stores['grain']} of the {need['grain']} its people needed by WEIGHT")


def test_lb3a_two_eaters_cannot_spend_the_same_unit():
    """SCARCITY BINDS, and it binds because `nearest_store` is given the caller's running view.

    The writes are deferred to the gate, so a loop reading `w.rungs[...].stores` directly would
    show every eater the FULL larder — the defect `loop/effects.py`'s own header names for
    `transfer` (*"`transfer` twice from a one-unit larder succeeds twice"*). With one grain
    between three eaters, exactly one grain may leave the larder and the rest must be short."""
    w = _cohort_tiny_world()
    w.rungs["Hh"].stores = {"grain": 1}
    for rid in ("R", "D", "S"):
        w.rungs[rid].stores = {}
    eaters = _eaters_at(w, "Hh")
    assert len(eaters) > 1, "the fixture needs at least two eaters for this to mean anything"

    _matter_once(w)

    assert w.rungs["Hh"].stores["grain"] == 0, (
        f"the larder went to {w.rungs['Hh'].stores['grain']}; a deferred write let two eaters "
        "spend the same unit, or the draw took more than was there")
    # ⚠ SUMMED OVER THE HEARTH'S EATERS ONLY. The first writing summed every person in the world
    # and read 9 where it wanted 5, because `p_high` and `p_king` are ALSO short on this bare
    # fixture — a test that attributes other people's hunger to this larder.
    short_grain = sum(w._subsistence_shortfall.get(e, {}).get("grain", 0) for e in eaters)
    wt = w.fixtures.get("subsistence_weight")["grain"]
    want = wt * _heads(w, eaters)
    assert short_grain == want - 1, (
        f"shortfall {short_grain} != {want} wanted - 1 available; the arithmetic does not close")


# ---------------------------------------------------------------------------
# ITEM 3b -- the body write, the shared `_crossings`, `remove_person`.
# Falsifiers LB-3b and LB-3c.
# ---------------------------------------------------------------------------

def _starving_world(body_step=10):
    """`tiny_world` with every larder bare and no site to produce one — the empty-root arm.

    ⚠ `body_step` IS SET EXPLICITLY AND THE SHIPPED DEFAULT IS `0`. `H-125` parks the magnitude at
    the control arm because all 86 buildable corpus worlds hold zero stores, so any nonzero
    default starves 258 people in worlds that model a scene rather than an economy. The MECHANISM
    is exercised here at a live arm — which is what keeps it a built behaviour rather than a
    branch nothing reaches (§0.2) — and `test_lb3b_the_zero_arm_...` pins the shipped one.
    ⚠ ON `_cohort_tiny_world` SINCE `24f`: only a cohort eats, so only a cohort can starve."""
    w = _cohort_tiny_world()
    for rid in ("R", "D", "S", "Hh"):
        w.rungs[rid].stores = {}
    w.sites.clear()
    w.fixtures = w.fixtures.sweep("body_step", body_step)
    return w


def test_lb3b_a_short_larder_falls_a_body_a_band_and_narrows_the_season():
    """**LB-3b**, and it asserts the crossing **AND** the budget drop, because either alone is
    half-wiring.

    ⚠ THIS IS THE READ/WRITE ASYMMETRY TEST (`CLAUDE.md` §0.1 pt 1). `decision.budget` reads
    `p.body` TODAY. A MATTER write that landed on a copy — or on a `Person` the rehome replaced —
    would fall a body that no reader ever sees, and a test asserting only *the body fell* would
    stay green through it. So the budget is asserted to move IN THE SAME SEASON the band is
    crossed: the band is what `body_band_penalty` counts, so the two are the same fact observed
    from the write side and from the read side."""
    w = _starving_world()
    fx, k = w.fixtures, w.fixtures.get("scene_budget")
    d = SeasonDriver(w)
    who = "p_low"
    start_body = w.persons[who].body
    start_budget = decision_budget(w, who)
    floor = max(f for f in fx.get("band_floors")["body"].values() if f <= start_body)

    crossed_at = None
    for season in range(1, 40):
        w.step = Step.MATTER
        evs = d.matter(mint_token(d.w, WriteClass.MATTER), [])
        w.tick += 1
        if [e for e in evs if e.kind == "condition.band_crossed" and anchor_of(w, e) == who]:
            crossed_at = season
            break
    assert crossed_at is not None, (
        f"{who}'s body never crossed a band in 39 starving seasons; it is at "
        f"{w.persons[who].body} from {start_body}")
    assert w.persons[who].body < floor <= start_body, (
        f"the crossing fired without the body passing the {floor} floor")
    assert decision_budget(w, who) < start_budget, (
        f"the band was crossed and the budget did not move ({start_budget} -> "
        f"{decision_budget(w, who)}). The MATTER write landed somewhere `decision.budget` does "
        "not read — which is the read/write asymmetry this test exists for")
    # `24f`, AT THIS WORLD'S SCALE: the duke starved beside the hearth's people for as many seasons
    # and his body never moved (`ED-IN-0255`). The realm-scale falsifier is
    # `tests/test_territorial_subsistence.py`.
    assert w.persons["p_high"].body == start_body, "the duke worried about subsistence"


def test_lb3b_control_a_stocked_world_moves_no_body_and_no_budget():
    """THE CONTROL. Same fixture, same seed, larders full — bodies constant, budgets unchanged,
    and `_crossings` fires for SITES only.

    `CLAUDE.md` §0.1 pt 4: a number without a control is not a measurement. Without this arm, a
    body write that fired unconditionally — on the fed as well as the starving — would pass every
    assertion in the test above."""
    w = _cohort_tiny_world()
    at = {rid: _eaters_at(w, rid) for rid in ("R", "D", "S", "Hh")}
    for rid, eaters in at.items():
        w.rungs[rid].stores = dict(_need(w, eaters)) if eaters else {}
    before_bodies = {pid: p.body for pid, p in w.persons.items()}
    before_budgets = {pid: decision_budget(w, pid) for pid in w.persons}

    d = SeasonDriver(w)
    w.step = Step.MATTER
    evs = d.matter(mint_token(d.w, WriteClass.MATTER), [])

    assert {pid: p.body for pid, p in w.persons.items()} == before_bodies, (
        "a fed person's body moved")
    assert {pid: decision_budget(w, pid) for pid in w.persons} == before_budgets, (
        "a fed person's season narrowed")
    person_crossings = [e for e in evs if e.kind == "condition.band_crossed"
                        and anchor_of(w, e) in w.persons]
    assert not person_crossings, f"a fed person crossed a band: {person_crossings}"


def test_lb3b_the_zero_arm_is_the_pre_item_tree_exactly():
    """`body_step = 0` IS THE CONTROL ARM OF THE SWEEP, and it must reproduce the day before this
    landed: nothing moves, nothing is emitted, nobody dies.

    A sweep arm that merely varies the magnitude cannot flip a verdict. This one can — it removes
    the cause rather than adjusting the result, which is the arm `harness/populated.py`'s own
    `creed_sweep` docstring calls the point of a control."""
    w = _starving_world(body_step=0)          # the SHIPPED arm, set explicitly
    assert P.DEFAULT_FIXTURES.get("body_step") == 0, (
        "the shipped `body_step` is no longer the control arm; `H-125` and this test disagree")
    before = {pid: p.body for pid, p in w.persons.items()}

    d = SeasonDriver(w)
    w.step = Step.MATTER
    evs = d.matter(mint_token(d.w, WriteClass.MATTER), [])

    assert w._subsistence_shortfall, "nobody is short on a bare world; the arm proves nothing"
    assert {pid: p.body for pid, p in w.persons.items()} == before, (
        "a body moved at `body_step = 0` — the control arm is not the pre-item tree")
    assert not [e for e in evs if e.kind in ("body.changed", "person.died")], (
        f"the zero arm emitted a body event: {[e.kind for e in evs]}")


def test_lb3c_death_at_body_zero_closes_every_tenure_through_the_same_owner_as_kill():
    """**LB-3c.** A body reaching 0 at MATTER must end every live edge NAMING that person — the
    same cascade `fight` runs at RESOLVE, through the same owner.

    ⚠ IT PLANTS THE EDGE `W-E` MEASURED DANGLING: a `tie` **another person owns** that names the
    dying one as its OBJECT. `p.tenures` is the edges this person is the SUBJECT of (§15.1), so a
    cascade scanning only that list cannot see it, and §15.3 is explicit that the tenure ends
    THROUGH the death. This is why `World.remove_person` scans `w.tenures`.

    ⚠ THE LITERAL FORM OF `LB-3c` IS NOT USED, AND THE REASON IS RECORDED RATHER THAN THE CHECK
    QUIETLY SOFTENED. `05_LEDGER_AND_BUILD.md` writes it as *"`grep -c "t.until = w.tick"
    engine/season` must be 1"*. That count is **5** on this tree and each of the five is a
    DIFFERENT closure — `confer` ending a prior hold, `release` ending what the actor owns,
    `revoke`, and so on — none of them the death cascade. Taking the grep literally would require
    deleting four legitimate per-verb closers. What the falsifier is ABOUT is that there is one
    DEATH cascade, and that is asserted directly below, on behaviour rather than on a line
    count."""
    w = _starving_world()
    w.add_tenure(Tenure("t_tie", "p_low", "p_mid", "tie", since=0))
    w.persons["p_mid"].body = 1

    d = SeasonDriver(w)
    w.step = Step.MATTER
    evs = d.matter(mint_token(d.w, WriteClass.MATTER), [])

    assert "p_mid" not in w.persons, "a body reached 0 and the person is still in the world"
    assert [anchor_of(w, e) for e in evs if e.kind == "person.died"] == ["p_mid"]
    assert [t.live for t in w.tenures if t.id == "t_tie"] == [False], (
        "the `tie` another person OWNS, naming the dead one, survived the death and now dangles")
    assert not [t for t in w.tenures if t.live and "p_mid" in (t.subject, t.object)], (
        "a live edge still names a dead person")

    # ONE OWNER, asserted on the source: `_eff_kill` must not carry its own copy of the cascade.
    import inspect
    from ..loop import effects as _effects
    body = inspect.getsource(_effects._eff_kill)
    assert "remove_person" in body, "`_eff_kill` no longer routes through the one owner"
    assert "t.until = w.tick" not in body, (
        "`_eff_kill` has grown its own cascade again — two sites closing tenures by hand is how "
        "MATTER's death and RESOLVE's drift apart (§8)")


# =================================================================================================
# LB-6d -- THE BENEFICIARY COLUMN (`CAT-2`, phase-6 item `6d`)
#
# What these assert, and the order matters: the column is DECLARED on every row (and the loader
# refuses a row without one), the declaration is CARRIABLE by the row that makes it, and the
# resolution RUNS on candidates the engine actually forms. The third is the one that could have
# been vacuous -- a column that resolves to nothing is CAT-2's dead option 1 relocated, and
# `benefits_me` would read 0.0 forever with every test green.
# =================================================================================================


def _verb_table_text() -> str:
    from ..data import files
    return files.VERB_TABLE_YAML.read_text()


def _load_with(table_text: str):
    """Reload the verb table from SUBSTITUTED text, pointing the loader at a TEMPORARY FILE.

    ⚠⚠ THIS USED TO WRITE THE TRACKED `engine/season/verb_table.yaml` AND RESTORE IT IN A
    `finally`, AND THAT WAS UNSAFE IN THE ONE CONFIGURATION CI ACTUALLY RUNS.
    `valoria-ci.yml`'s `season-tests` job (`unit-tests` until 2026-10-02) runs
    `pytest engine/season/tests -q -n auto`, and
    xdist's default `--dist load` spreads one file's tests across workers. Two failures follow
    from writing the real path:
      * ANOTHER worker reading the table mid-arm (`test_season_shape.py` reads it directly in
        three places) sees a deliberately broken table and goes red for a reason unrelated to
        what it tests;
      * two `_load_with` calls OVERLAPPING leave the repo file corrupted for good — B snapshots
        A's broken arm as its `original`, A restores the real text, then B's `finally` writes
        A's broken arm back. A process killed between the write and the `finally` does the same
        with one worker.
    A test that can leave a tracked source file broken is not a strong test with a caveat; it is
    a test that edits the repository. The substituted table now lives in a `tmp` file and only
    the MODULE-LEVEL binding moves, so nothing outside this process can observe the arm and
    there is no path that mutates the working tree."""
    import importlib
    import tempfile
    from pathlib import Path
    from ..data import files, verbs as _verbs
    real = files.VERB_TABLE_YAML
    with tempfile.TemporaryDirectory() as d:
        arm = Path(d) / "verb_table.yaml"
        arm.write_text(table_text)
        files.VERB_TABLE_YAML = arm
        try:
            importlib.reload(_verbs)
        finally:
            files.VERB_TABLE_YAML = real
            importlib.reload(_verbs)


_LEVY_ROW = (
    '  - verb:        "levy"\n'
    '    scale:   "settlement"\n'
    '    scale_note: "a levy moves a Rung\'s stores -- the rung IS the subject"\n'
    '    stratum:     "uncontested_material"\n'
    '    eligibility: ["remit:issue", "presence:<rung>"]\n'
    '    beneficiary: "actor"\n'
)

# ⚠ PLAN POSITION `19` TYPED `levy` (`transfer`'s form-2 cell plus a `basis` conjunct), and a typed
# cell's `needs:` ADMITS `to` -- so `beneficiary: to` on `levy` became CARRIABLE and stopped being the
# dead reference `test_lb6d_an_operand_beneficiary_the_row_cannot_carry_is_refused_at_load` plants.
# That test needs an UNTYPED row, and `forge` is one (`requires: —`, no cell). The two tests above keep
# `levy`: a missing or off-roster beneficiary is refused whatever the row's cell.
_FORGE_ROW = (
    '  - verb:        "forge"\n'
    '    stratum:     "uncontested_material"\n'
    '    eligibility: ["own"]\n'
    '    beneficiary: "actor"\n'
)


def test_lb6d_every_verb_declares_a_rostered_beneficiary():
    """**LB-6d.** `CAT-2`: *"DECLARE IT -- and declare it as a STATIC COLUMN ON `verb_table.yaml`
    resolving to a carrier a Candidate ALREADY holds."* Every row, no exceptions, from the
    roster."""
    from ..data.verbs import BENEFICIARY_KINDS, VERB_TABLE

    # Same control as `test_season_shape.py`'s own `len(_load_verb_table()) == 39`: it is here so
    # that a table which SHRANK cannot let this census pass while examining a handful of rows.
    # ⚠ 38 -> 39, `march` (M4, `ED-IN-0279` clause (a)), 2026-09-28; 39 -> 40, `give` (plan
    # position 16, `H-84`), 2026-09-29 -- `beneficiary: none`, so `kinds["none"]` grows by one;
    # 40 -> 42, `found` and `build` (plan position `24e`), 2026-09-29 -- both `beneficiary: none`;
    # 42 -> 43, `migrate` (plan position `19c`), 2026-09-30 -- `beneficiary: actor`, `move`'s;
    # 43 -> 44, `survey` (plan position `20-iii`), 2026-09-30 -- `beneficiary: actor`, the
    # investigation acts' (the sheet and its content land in the surveyor's hand and ledger);
    # 44 -> 46, `challenge` and `accept` (IN-08's cells commit, the duel pair) -- both
    # `beneficiary: actor`, `fight`'s (a re-record, said so here); 46 -> 45, `repudiate` CUT
    # (v9 IN-11, #453 R-3 (b)) -- `beneficiary: actor`, so `kinds["actor"]` shrinks by one.
    # [JUSTIFIED: the verb count is READ from verb_table.yaml, never chosen -- the control that stops this census passing over a loader that returned a subset]
    assert len(VERB_TABLE) == 45, "the verb count moved; this row's census is stale"
    undeclared = [v for v, r in VERB_TABLE.items() if not r.beneficiary]
    assert not undeclared, f"verbs with no `beneficiary:`: {undeclared}"
    off_roster = [(v, r.beneficiary) for v, r in VERB_TABLE.items()
                  if r.beneficiary not in BENEFICIARY_KINDS]
    assert not off_roster, f"beneficiaries outside `beneficiary_kinds`: {off_roster}"
    # ⚠ WHAT STOOD HERE WAS TAUTOLOGICAL AND CLAIMED NOT TO BE. It rebuilt `declared` with the
    # NEGATION of the `off_roster` predicate asserted empty one line above, so
    # `len(declared) == len(VERB_TABLE)` held unconditionally, and the empty-table case its
    # comment invoked is already excluded by the `== 38` assertion at the top. A comment claiming
    # a §0.1 pt 2 vacuity guard that the code does not provide is worse than no guard.
    # The real vacuity risk is the OTHER direction -- a census that examined rows carrying no
    # column at all -- so it is the DISTRIBUTION that is pinned, which a broken loader cannot fake.
    kinds = Counter(r.beneficiary for r in VERB_TABLE.values())
    assert set(kinds) <= set(BENEFICIARY_KINDS) and sum(kinds.values()) == len(VERB_TABLE)
    assert kinds["none"] < len(VERB_TABLE), (
        f"every row declares `none` ({kinds}) -- the column is present and says nothing, which "
        "this census would otherwise report as full coverage")


def test_lb6d_a_row_without_the_column_is_refused_at_load():
    """The column is REQUIRED, so a new verb cannot arrive carrying no declaration. An absent
    column would read as `benefits nobody` for that verb -- the UNKNOWN/False collapse."""
    src = _verb_table_text()
    dropped = src.replace(_LEVY_ROW, _LEVY_ROW.replace('    beneficiary: "actor"\n', ""), 1)
    assert dropped != src, "the substitution did not apply -- this test is asserting nothing"
    with pytest.raises(SystemExit, match="declares no `beneficiary:`"):
        _load_with(dropped)


def test_lb6d_an_off_roster_beneficiary_is_refused_at_load():
    """`beneficiary_kinds` is the closed set. A fifth carrier is argued for in `rosters.yaml`,
    never spelled into a cell.

    ⚠ IT EXPECTS `SystemExit`, AND IT EXPECTED `Unspecified` UNTIL 2026-09-18. The check went
    through `require_member`, which raises the PER-ACT gap type -- so a broken table imported
    inside `corpus_run.run_case`'s try block was caught there and reported as one case's
    DESIGN-GAP. `H-115`'s split is that load-time refusals are fatal `SystemExit`; this row is
    load-time, so it raises that now and this assertion follows it."""
    src = _verb_table_text()
    bogus = src.replace(_LEVY_ROW, _LEVY_ROW.replace('"actor"', '"treasury"'), 1)
    assert bogus != src, "the substitution did not apply -- this test is asserting nothing"
    with pytest.raises(SystemExit, match="not in `beneficiary_kinds`"):
        _load_with(bogus)


def test_lb6d_an_operand_beneficiary_the_row_cannot_carry_is_refused_at_load():
    """⚠ THE CHECK THAT KEEPS THE COLUMN HONEST, AND THE REASON `CAT-2` CLOSED THE WAY IT DID.

    Option 1 -- derive the beneficiary from the operand binding -- died on a measurement: 24 of 38
    verbs are UNTYPED and carry no operand at all. A static column escapes that only while it
    declares carriers the row can actually hold. `beneficiary: to` on an untyped verb is the SAME
    dead reference wearing the new column, and it would resolve to `None` for every candidate ever
    formed, silently, forever."""
    src = _verb_table_text()
    unbindable = src.replace(
        _FORGE_ROW, _FORGE_ROW.replace('beneficiary: "actor"', 'beneficiary: "to"'), 1)
    assert unbindable != src, "the substitution did not apply -- this test is asserting nothing"
    with pytest.raises(SystemExit, match="neither binds nor admits"):
        _load_with(unbindable)


def test_lb6d_kill_is_declared_to_benefit_the_actor_not_the_person_it_writes_on():
    """⚠ THE ROW THAT PROVES THE COLUMN CANNOT BE DERIVED FROM `writes:`.

    `fight` writes `Person.body` and `Person.exists` ON THE SUBJECT. A rule reading the
    write column would name the victim as the beneficiary of their own killing, because A WRITE
    CAN BE A HARM. This is the falsifier for the claim that the declaration is load-bearing: if
    someone later derives this column, THIS is the assertion that goes red."""
    from ..data.verbs import VERB_TABLE

    row = VERB_TABLE["fight"]
    assert "Person.body" in row.writes and "Person.exists" in row.writes, (
        "the row no longer writes on its subject, so this test's premise is gone")
    assert row.beneficiary == "actor", (
        "`fight`'s beneficiary was derived from `writes:` and now names the victim")


def test_lb6d_none_and_an_unbound_carrier_are_different_answers():
    """`beneficiary_of` returns `None` twice over and the two are NOT the same claim. `none` is
    the verb's answer; an unbound carrier is a hole. The ROW discriminates them, which is why the
    resolver returns an id rather than a tri-state."""
    from ..data.verbs import VERB_TABLE
    from ..decision.choose import beneficiary_of, benefits_me
    from ..state.carriers import Candidate, Person

    p = Person(id="p1")
    declared_none = Candidate(verb="create_record", subject="rec1")
    assert VERB_TABLE["create_record"].beneficiary == "none"
    assert beneficiary_of(p, declared_none) is None

    hole = Candidate(verb="transfer", subject="r1", operands={})
    assert VERB_TABLE["transfer"].beneficiary == "to"
    assert beneficiary_of(p, hole) is None, "an unbound `to` resolved to something"

    bound = Candidate(verb="transfer", subject="r1", operands={"to": "p3"})
    assert beneficiary_of(p, bound) == "p3"
    assert benefits_me(p, bound) == 0.0
    assert benefits_me(p, Candidate(verb="levy", subject="r1")) == 1.0


def test_lb6d_the_column_resolves_on_candidates_the_engine_actually_forms():
    """⚠⚠ THE ONE THAT IS NOT SATISFIABLE BY DECLARING ANYTHING (`CLAUDE.md` §0.2).

    Every test above reads the table or a hand-built Candidate. This one runs a season, takes
    every Candidate the deliberation ACTUALLY forms, and resolves each against its row. The
    failure it excludes is the one that matters: a column that declares carriers real candidates
    never hold resolves to `None` throughout, `benefits_me` reads 0.0 for everybody, and every
    other assertion in this block still passes.

    IT ASSERTS THAT IT ASSERTED (§0.1 pt 2) -- the examined count is asserted non-trivial, so a
    run that formed no candidates fails here instead of passing vacuously.

    ⚠ THE CONTROL ON ITS OWN HEADLINE, because a number without one is not a measurement (§0.1
    pt 4): roughly HALF of all candidates carry THE ACTOR AS THEIR OWN SUBJECT -- `opening_set`
    offers every person themselves as a referent for every verb. So the count of candidates
    reading `benefits_me == 1.0` is inflated by the aperture's shape and must not be read as
    *"persons are self-interested two thirds of the time"*. That is a property of the candidate
    former, which this item does not touch and this test does not assert a bound on."""
    from ..data.verbs import VERB_TABLE
    from ..decision import choose as _choose
    from ..harness import populated

    seen: list = []
    inner = _choose.opening_set

    def spy(person, view, question, fx):
        cands = inner(person, view, question, fx)
        seen.extend((person, c) for c in cands)
        return cands

    _choose.opening_set = spy
    try:
        populated.run(seasons=1, seed=0)
    finally:
        _choose.opening_set = inner

    # A FLOOR, not a measurement. The season forms 5,345 candidates at this seed (§7.3e, re-taken
    # by `probe_execution_pass.py`), so this sits far below the observed figure and is deliberately
    # NOT pinned to 5,345 -- pinning it would reland every unrelated aperture change here as a
    # false failure, which is how a guard stops being read.
    # [JUSTIFIED: a floor far below the 5,345 measured at this seed, chosen only to fail a sweep that ran thinly or not at all -- the vacuous pass this test exists to exclude]
    assert len(seen) > 1000, (
        f"only {len(seen)} candidates were formed; this sweep cannot observe what it is for")

    # ⚠⚠ THIS ZERO IS STRUCTURAL, NOT MEASURED, AND THE ITEM PRESENTED IT AS ITS RESULT.
    # Traced end to end after the fact: `actor` -> `p.id`, never None. `subject` -> `c.subject`,
    # and `opening_set` only ever builds a Candidate from `q.referents`, so it is never falsy.
    # `to` is declared by ONE row (`transfer`) whose form lists `to` in `needs:`, and
    # `_derive_operand` answers `to` with `return subject` (`options.py:309`) -- so it cannot be
    # None either. `holes` is therefore 0 for reasons in the CODE, not in the data, and the
    # assertion below cannot fail while that holds. Kept because it is a real regression guard on
    # those three paths, but it is NOT evidence that the column was declared well, and the
    # records that read it that way are corrected. The measurement that would bear on THAT is the
    # coverage line beneath it: 10 of the 38 rows (every `remit:`-gated verb, `confer` among
    # them) form zero candidates, so their declarations are never exercised here at all.
    holes = [(p.id, c.verb) for p, c in seen
             if VERB_TABLE[c.verb].beneficiary != "none"
             and _choose.beneficiary_of(p, c) is None]
    assert not holes, (
        f"{len(holes)} candidates declare a beneficiary that did not resolve, e.g. {holes[:5]}. "
        "A declared carrier that never binds is CAT-2's dead option 1 inside the new column")

    resolved = sum(1 for p, c in seen if _choose.beneficiary_of(p, c) is not None)
    assert resolved > len(seen) // 4, (
        f"only {resolved} of {len(seen)} candidates resolve any beneficiary -- the column is "
        "declared but inert, which is the failure this test exists to see")

    # The term SPANS its codomain. A `benefits_me` that is constant across candidates is inert by
    # construction (`urgency`'s own note: "a term constant across candidates is INERT BY
    # CONSTRUCTION -- the dead-carrier complaint"), whatever `orient` later multiplies it by.
    values = {_choose.benefits_me(p, c) for p, c in seen}
    assert values == {0.0, 1.0}, f"`benefits_me` never varied across a season: {values}"

# LB-6e -- `(Person, scar[axis])`, THE MORAL LAYER'S MISSING MOTION (§54 item 21, `H-128`)
#
# `04 §F.20a`: *no verb writes any `Person` interior field at all*, so every interior consequence
# is inert and a person leaves a season morally identical to the one who entered it. This is the
# one interior row whose TRIGGER the chain actually specifies, so it is the one that can be built
# without inventing the condition.
#
# ⚠ RE-SHAPED AT IN-08 H3 (`ED-IN-0261`'s scar model). LB-6e built the scar as a signed float per
# AXIS on the wounded person (`_scar`, magnitude `scar_step`), and three tests here pinned that
# mechanism: `..._a_wound_scars_and_the_axes_come_from_the_alignment_table` (keys == the axes
# `fight` engages), `..._the_zero_arm_writes_no_scar_and_reports_none` (`scar_step = 0` inert) and
# `..._a_verb_that_engages_no_axis_scars_nothing` (called `_scar` directly). H3 RETIRES `_scar` and
# `scar_step`, so all three are RETIRED with their subject, not re-pointed: the scar is now
# `{pursuit: count}` on the act's OBSERVERS, and its falsifiers -- including the no-celled-axis
# control -- are `test_h3_scar_by_observation.py`. The field test below survives: the row still
# has its carrier.
# =================================================================================================


def test_lb6e_the_matrix_row_finally_has_a_field():
    """`formal_analysis.md` C3 measured it: *"`matrix_rows_without_a_field()['absent']` lists
    `(Person, scar)`"*. A Part D row naming a field that does not exist is a licence pointing at
    nothing."""
    from ..state.carriers import Person

    p = Person(id="p1")
    assert hasattr(p, "scar"), "`(Person, scar)` still names a field the carrier does not have"
    assert p.scar == {}, (
        "`scar` ships pre-seeded. It is keyed on the PURSUIT ROSTER as a count, and a pursuit "
        "nobody has been scarred on is absent rather than 0 -- seeding the keys here would put a "
        "copy of the roster into a carrier (§0.05 clause 3)")


# =================================================================================================
# PLAN POSITION `13f` -- `establish` HAS AN EFFECT.
# `workplans/2026-09-18-governance-settlement-behaviour-plan_part2.md`, position `13f`, which is a
# later plan than this file's `LB-n` sheet; the tests carry the position id instead. Its FALSIFIER,
# observed in both halves: a planted `establish` on an EXISTING id changes a sitting holder's
# `granted_acts` and publishes a `tenure.payload_set` naming that holder's Tenure, while a
# hand-mutation of the office reaches nobody (`test_h71_the_grant_is_a_snapshot_not_a_mirror`,
# `test_season_shape.py`, is that half); and an `establish` naming no belonging, or an unknown one,
# emits `establish.refused`, constructs nothing and lets no exception escape the fold.
# =================================================================================================

def _establish_world():
    """`tiny_world`, unchanged. Its duke `p_high` holds `off_duke`, whose remit grants `confer` --
    the eligibility `establish` declares -- and `p_mid` holds no office."""
    w = P.tiny_world()
    d = SeasonDriver(w)
    d.matter(mint_token(d.w, WriteClass.MATTER), [])
    return w, d


def _founding(**over) -> dict:
    """A well-formed `establish` payload for an office `tiny_world` does not have. `appointed` is
    one of the three conferral values `ED-IN-0256` rules, and since `13d-i` rostered them the
    basis test passes nothing else."""
    p = dict(office="off_reeve", post="Reeve", rung="S", remit=["issue", "dispatch"],
             faction="Crown", conferral="appointed")
    p.update(over)
    return p


def _establish(w, d, aid: str, payload, actor: str = "p_high", via: str = "off_duke") -> list:
    """G3 (plan position 6): the act names the seat it is exercised through. `establish` is
    `remit:confer`-eligible, and `off_duke` -- a Crown seat at `D`, over every rung `_founding` uses
    -- is the duke's seat whose grant carries `confer`; since G3 `_eligible` asks THAT seat, and the
    write gate asks its purview before a sitting holder's grant may be re-stamped."""
    return d.resolve(mint_token(d.w, WriteClass.ACTS),
                     [Act(id=aid, actor=actor, verb="establish", payload=payload, via=via)],
                     contest_max_depth=w.fixtures.get("contest_max_depth"))


def _seat_reeve(w, remit):
    """An EXISTING office with a conferral basis and a sitting holder, seated through
    `add_tenure` so the holder's grant is the snapshot `_grant_remit` takes at seating. The
    payload carries a key of another writer's, so the re-stamp is seen to be key-scoped."""
    w.offices["off_reeve"] = Office("off_reeve", "Reeve", "S", list(remit),
                                    conferral="appointed", faction="Crown")
    w.add_tenure(Tenure("t_reeve", "p_mid", "off_reeve", "hold", 0, payload={"note": "kept"}))
    [t] = [t for t in w.tenures if t.id == "t_reeve"]
    return t


def test_13f_the_remit_row_is_keyed_on_the_field_the_office_has():
    """Instruction (1). Part D's `(Office, remit)` named a field `Office` does not have, so the gate
    licensed a cell nothing could write and `matrix_rows_without_a_field()` listed it. The ROW is
    renamed at its owner, to the field the constructor validates and every remit check reads."""
    fields = {f.name for f in dataclasses.fields(Office)}
    assert "remit_acts" in fields and "remit" not in fields, sorted(fields)
    assert ("Office", "remit_acts") in MATRIX and ("Office", "remit") not in MATRIX
    assert ("Office", "remit_acts") not in matrix_rows_without_a_field()["absent"]
    assert not [k for k in matrix_rows_without_a_field()["absent"] if k[0] == "Office"], (
        "an `Office` row still names a field the carrier does not have")
    assert "Office.remit_acts" in VERB_TABLE["establish"].writes
    assert "remit.changed" in MATRIX[("Office", "remit_acts")].emits


def test_13f_a_planted_establish_founds_the_office_and_grants_a_hold_opened_before_it():
    """THE CONCRETE CASE THE POSITION NAMES: a `hold` opened on an office id before the office
    exists gets no grant (`_grant_remit` traces and stamps nothing), and `establish` then creates
    the office. The act re-stamps that holder in the same act, and the person-side reader sees it."""
    w, d = _establish_world()
    w.add_tenure(Tenure("t_early", "p_mid", "off_reeve", "hold", 0))
    [t] = [t for t in w.tenures if t.id == "t_early"]
    mid = w.persons["p_mid"]
    assert "off_reeve" not in w.offices and t.granted_acts == (), "fixture: not the early-hold case"
    assert not person_side_eligible(mid, VERB_TABLE["dispatch"]), "fixture: p_mid can dispatch"

    out = _establish(w, d, "e_found", _founding())
    kinds = [e.kind for e in out]
    assert kinds == ["office.established", "tenure.payload_set"], kinds
    off = w.offices["off_reeve"]
    assert (off.post, off.rung, off.remit_acts, off.faction, off.conferral) == (
        "Reeve", "S", ["issue", "dispatch"], "Crown", "appointed"), off
    assert not hasattr(off, "establishment") and world_q.establishment_of(w, off.id) == [], (
        "`17a` deleted `Office.establishment`; a founding obliges nobody, so the Query is empty")
    assert t.granted_acts == ("issue", "dispatch"), (
        f"the early holder's grant is {t.granted_acts} -- the act did not re-stamp it")
    assert person_side_eligible(mid, VERB_TABLE["dispatch"]), (
        "the grant is on the Tenure and the person-side reader still refuses the remit verb")
    ps = next(e for e in out if e.kind == "tenure.payload_set")
    assert t.id in {c.subject for c in ps.changes}, [c.subject for c in ps.changes]


def test_13f_an_office_nobody_holds_publishes_no_payload_set():
    """`tenure.payload_set` is EARNED by a re-stamped holder, never published for one that is not
    there -- the fabricated-emission class `_fold`'s own comments name. The success is still
    published: the office was founded."""
    w, d = _establish_world()
    out = _establish(w, d, "e_bare", _founding())
    assert [e.kind for e in out] == ["office.established"], [e.kind for e in out]
    assert "off_reeve" in w.offices


def test_13f_an_establish_on_an_existing_id_changes_the_remit_and_reaches_the_sitting_holder():
    """**THE POSITION'S FALSIFIER.** Both halves, in one world and in order, so neither can pass
    for the other's reason:

      * SNAPSHOT: a hand-mutation of `w.offices[x].remit_acts` does NOT reach the sitting holder;
      * MIRROR'S OBSERVABLE, BY AN ACT: a planted `establish` on the EXISTING id rewrites the
        remit in place, emits `remit.changed` and NOT `office.established`, changes the sitting
        holder's `granted_acts`, and publishes a `tenure.payload_set` naming that holder's Tenure.

    And the act that changes nothing is refused rather than reported: re-running it writes
    nothing, so the fold emits `establish.refused`."""
    w, d = _establish_world()
    t = _seat_reeve(w, ["issue"])
    mid = w.persons["p_mid"]
    assert t.granted_acts == ("issue",), f"fixture: seating stamped {t.granted_acts}"

    # SNAPSHOT: the hand-mutation reaches nobody.
    w.offices["off_reeve"].remit_acts = ["issue", "convene"]
    assert t.granted_acts == ("issue",), "a hand-mutation re-granted a sitting holder"
    assert not person_side_eligible(mid, VERB_TABLE["convene"])

    office = w.offices["off_reeve"]
    out = _establish(w, d, "e_remit", _founding(remit=["issue", "dispatch"]))
    kinds = [e.kind for e in out]
    assert kinds == ["remit.changed", "tenure.payload_set"], kinds
    assert w.offices["off_reeve"] is office, "the office was re-founded, not re-remitted in place"
    assert office.remit_acts == ["issue", "dispatch"], office.remit_acts
    assert t.granted_acts == ("issue", "dispatch"), (
        f"the sitting holder's grant is {t.granted_acts}: the act changed the office and did not "
        "reach the holder -- `_grant_remit(force=True)` is not being called, or is still a setdefault")
    assert t.payload.get("note") == "kept", "the re-stamp overwrote a key it does not own"
    assert person_side_eligible(mid, VERB_TABLE["dispatch"])
    assert not person_side_eligible(mid, VERB_TABLE["convene"]), (
        "the hand-mutation's `convene` survived -- the grant is the ACT's remit, not a union")
    ps = next(e for e in out if e.kind == "tenure.payload_set")
    assert t.id in {c.subject for c in ps.changes}, [c.subject for c in ps.changes]

    again = _establish(w, d, "e_again", _founding(remit=["issue", "dispatch"]))
    assert [e.kind for e in again] == ["establish.refused"], [e.kind for e in again]


def test_13f_a_sole_holder_re_stamping_their_own_office_refuses_and_does_not_crash(monkeypatch):
    """FOUND BY A `/code-review` PASS ON THE ACCUMULATED PHASE ALPHA+BETA DIFF, 2026-09-27, AND
    REPRODUCED DIRECTLY BEFORE THIS FIX: `_req_establish`'s clause 5 excluded the ACTOR from its
    `others` check -- "another person's needs the seat" -- so a SOLE holder re-stamping their own
    office's remit skipped `may_fill` entirely and the precondition admitted the act. `state/
    gate.py::tenure_write_basis`'s T-m (G3's own antagonist-pass fix) never admits re-granting a
    seat-hold, not even the actor's own, so the gate then raised `NotYours` -- UNCAUGHT by `_fold`,
    which only catches `NoOpReceipt` -- and the season would have died instead of the row's own
    `establish.refused` firing. `_req_establish`'s `held` now asks `may_fill` whenever ANY live
    holder exists, self included -- the fix is `not held or may_fill(...)`, replacing `not others`.

    `p_mid` is the SOLE holder here, exercising `off_reeve` itself as `via` (self-referential,
    which `may_fill` refuses on its own terms too: `via == off.id`) -- the worst case, since it
    was ALSO the case `_req_establish`'s old code admitted unconditionally whenever `others` was
    empty. `p_mid` is seated WITH `confer` in the grant -- without it `_eligible`
    (`loop/resolve.py`, `establish` is `remit:confer`-eligible) refuses the act before
    `_req_establish` is ever reached, which is exactly the mistake this test's own first writing
    made: it seated `p_mid` with `["issue"]` only, so `_eligible` refused first and the test passed
    identically whether or not `_req_establish`'s clause 5 was fixed -- a citation-free assertion
    that could not observe the failure it excluded (`CLAUDE.md` section 0.1 pt 2), found by a
    holistic antagonist pass over this same sweep and corrected here.

    THE MUTATION IS THE REAL OLD CODE, RUN THROUGH THE FULL `resolve()` PIPELINE -- not a
    reimplementation trusted to match it, and not a check that some OTHER clause refuses first
    (`monkeypatch.setattr(PR, "may_fill", ...)` alone does not prove this, since `_eligible` gates
    the act before `_req_establish` ever runs: patching `may_fill` without also fixing the seeded
    remit would still pass for the wrong reason). `PR.REQUIRES_PREDICATES["establish"]` -- the
    registry `@requires_predicate` populates at decoration time, which `_admits` actually calls --
    is patched directly, because patching the bare module attribute `PR._req_establish` does NOT
    reach the caller (the registry holds the original function object, captured before any
    monkeypatch of the module-level name)."""
    w, d = _establish_world()
    _seat_reeve(w, ["confer"])
    out = _establish(w, d, "e_self", _founding(remit=["confer", "dispatch"]),
                     actor="p_mid", via="off_reeve")
    assert [e.kind for e in out] == ["establish.refused"], [e.kind for e in out]
    assert w.offices["off_reeve"].remit_acts == ["confer"], (
        "the refused act still re-stamped the remit")

    # MUTATION: the retired precondition, run through the SAME pipeline on a FRESH world --
    # reproduces the uncaught crash this fix closes. `others` (not `held`) is the retired name.
    import engine.season.loop.predicates as PR
    from ..state.gate import NotYours

    def retired_req_establish(w, a):
        off = PR.office_described_by(a)
        if off is None or off.rung not in w.rungs or not PR.has_conferral_basis(off):
            return False
        held_as = w.class_of(off.id)
        if held_as is not None:
            if held_as != "Office":
                return False
            cur = w.offices[off.id]
            if not (off.post == cur.post and off.rung == cur.rung and off.body == cur.body
                    and off.faction == cur.faction and off.conferral == cur.conferral
                    and off.revocation == cur.revocation):
                return False
        others = any(t.kind == "hold" and t.object == off.id and t.live and t.subject != a.actor
                    for t in w.tenures)
        return not others or PR.may_fill(w, a.actor, a.via, off)

    monkeypatch.setitem(PR.REQUIRES_PREDICATES, "establish", retired_req_establish)
    w2, d2 = _establish_world()
    _seat_reeve(w2, ["confer"])
    with pytest.raises(NotYours):
        _establish(w2, d2, "e_self_retired", _founding(remit=["confer", "dispatch"]),
                  actor="p_mid", via="off_reeve")


@pytest.mark.parametrize("change", [
    dict(faction="Church of Solmund"),
    dict(post="Warden"),
    dict(rung="Hh"),
    dict(conferral="elected"),
    # ⚠ (`13d-i`) WAS `revocation="purview"`, r2's superseded value. Off the roster it now raises
    # in the constructor, so the act would refuse for THAT reason and this case would stop
    # observing a basis DIFFERENCE. The rostered value differs from the seat's `None` and constructs.
    dict(revocation="rung_above_same_faction"),
], ids=lambda c: next(iter(c)))
def test_13f_an_existing_id_refuses_any_change_but_the_remit(change):
    """Re-founding -- a different belonging, post, rung or basis on an id that exists -- is not a
    write `establish` declares, so it REFUSES and touches neither the office nor the holder. The
    control is in the same world: the same act without the change is admitted.

    ⚠ **ASSERTS THE OFFICE STILL CONSTRUCTS (added 2026-09-26, antagonist finding).** Without this,
    a future off-roster `change` value would refuse for the WRONG reason -- the constructor raising
    inside `office_described_by`, translated to `False` before clause 4's basis-difference check
    ever runs -- and this test would keep passing while testing nothing about re-founding. Each
    `change` here must still be a WELL-FORMED office, differing from the seated one by exactly the
    one declared field, or the case is not exercising what its `id` claims."""
    w, d = _establish_world()
    t = _seat_reeve(w, ["issue"])
    plain = _founding(remit=["issue", "dispatch"])
    assert _preds._req_establish(w, Act(id="ctl", actor="p_high", verb="establish",
                                        payload=plain, via="off_duke")), (
        "control: the unchanged act is refused")

    changed_payload = {**plain, **change}
    changed_act = Act(id="check_constructs", actor="p_high", verb="establish",
                      payload=changed_payload, via="off_duke")
    changed_office = office_described_by(changed_act)  # raises if this `change` is off-roster/malformed
    assert changed_office is not None, (
        f"{change}: the payload did not describe a constructible Office at all")

    out = _establish(w, d, "e_refound", changed_payload)
    assert [e.kind for e in out] == ["establish.refused"], [e.kind for e in out]
    assert w.offices["off_reeve"].remit_acts == ["issue"]
    assert t.granted_acts == ("issue",)


# `raises` marks the payloads the CONSTRUCTOR itself rejects, so each refusal below is shown to
# have intercepted a real raise rather than to have been a no-op nothing would have tripped.
@pytest.mark.parametrize("payload,raises", [
    ({}, False),
    (_founding(faction=None), True),                                   # belongs to nothing
    (_founding(faction="Nowhere Brotherhood"), True),                  # an unknown faction
    (_founding(faction=None, body="Office of Nothing"), True),         # an unknown body
    (_founding(body="Imperial Court", faction="Church of Solmund"), True),   # a mismatch
    (_founding(remit=["issue", "levy"]), True),                        # off `REMIT_ACTS`
    (_founding(post="Duke", faction=None, body="Imperial Court"), True),     # a title in a body
    (_founding(rung="nowhere"), False),                                # a rung the world lacks
    (_founding(conferral=None), False),                                # no conferral basis
    (_founding(office="p_low"), False),                                # an id a person holds
], ids=["empty", "no-belonging", "unknown-faction", "unknown-body", "mismatch", "off-roster-remit",
        "title-in-body", "unknown-rung", "no-basis", "person-id"])
def test_13f_an_unfoundable_establish_refuses_constructs_nothing_and_raises_nothing(payload, raises):
    """The fold's FIRST refusal path: the precondition returns False and the fold emits
    `emits_on_refusal`. Asserted on the Event -- the fold is called bare, so a raise escaping it
    fails this test as an error rather than passing silently."""
    w, d = _establish_world()
    before = dict(w.offices)
    # G3: through the duke's seat, so the refusal is the PRECONDITION's -- without `via` the act
    # would be refused one step earlier, at eligibility, and this would observe nothing about it.
    act = Act(id="e_bad", actor="p_high", verb="establish", payload=payload, via="off_duke")
    if raises:
        with pytest.raises((Unowned, Unspecified, Forbidden)):
            office_described_by(act)
    out = d.resolve(mint_token(d.w, WriteClass.ACTS), [act], contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert [e.kind for e in out] == ["establish.refused"], [e.kind for e in out]
    assert w.offices == before, f"an office was constructed: {sorted(set(w.offices) - set(before))}"


def test_13f_a_computed_establish_carries_no_operands_and_refuses():
    """The row is resolvable now and still untyped, so a COMPUTED `establish` forms with NO
    operands -- `operands_for` returns `{}` -- and must refuse until `15c` widens the operand
    vocabulary. What the chooser puts on its payload is the question's referent as `subject`, and
    that founds nothing."""
    row = VERB_TABLE["establish"]
    assert "establish" in resolvable_verbs()
    assert row.requires_typed is None
    w, d = _establish_world()
    duke = w.persons["p_high"]
    assert person_side_eligible(duke, row), "fixture: the duke cannot form `establish` at all"
    assert operands_for(duke, row, None, "p_low", w.fixtures) == {}
    out = _establish(w, d, "e_computed", {"subject": "p_low"})
    assert [e.kind for e in out] == ["establish.refused"], [e.kind for e in out]


def test_13f_confer_and_establish_ask_one_basis_test(monkeypatch):
    """Instruction (2): the basis test is FACTORED ONCE, so `13d-i` rewrites one function and both
    preconditions inherit it. Observed by behaviour, not by reading source: with the ONE function
    patched to refuse, both predicates refuse an act each admits unpatched. A predicate carrying
    its own copy of the test would go on admitting."""
    w, d = _establish_world()
    w.offices["off_dicastery"].conferral = "appointed"
    # G3: the conferred seat needs GROUND inside the duke's purview (a rungless seat is reached by
    # no purview, so nobody may confer it), and both acts name the duke's seat.
    w.offices["off_dicastery"].rung = "S"
    conf = Act(id="c_basis", actor="p_high", verb="confer",
               payload={"office": "off_dicastery", "to": "p_mid"}, via="off_duke")
    est = Act(id="e_basis", actor="p_high", verb="establish", payload=_founding(), via="off_duke")
    assert _preds._req_confer(w, conf) and _preds._req_establish(w, est), "control: not admitted"
    monkeypatch.setattr(_preds, "has_conferral_basis", lambda off: False)
    assert not _preds._req_confer(w, conf), "`_req_confer` does not ask the shared basis test"
    assert not _preds._req_establish(w, est), "`_req_establish` does not ask the shared basis test"


def test_13f_a_planted_establish_founds_an_office_by_body_not_only_by_faction():
    """`office_described_by`'s `body` branch, otherwise unexercised -- every other test in this
    section founds through `faction`. `Imperial Court` is a body that DERIVES to faction `Crown`
    (`data/rosters.py::office_faction`, `rosters.yaml:1096`), so the constructed `Office` carries
    both: the body as given, and the faction `office_faction` resolved it to."""
    w, d = _establish_world()
    out = _establish(w, d, "e_by_body", _founding(faction=None, body="Imperial Court"))
    assert [e.kind for e in out] == ["office.established"], [e.kind for e in out]
    off = w.offices["off_reeve"]
    assert (off.body, off.faction) == ("Imperial Court", "Crown"), (off.body, off.faction)


def test_13f_the_restamp_skips_a_non_hold_tenure_and_a_dead_hold_on_the_same_office():
    """The re-stamp's filter, `t.kind == "hold" and t.object == off.id and t.live`
    (`loop/effects.py`), is never exercised by the other tests: they seat exactly one live `hold`.
    Plants three tenures on the SAME office -- a live `hold` (re-stamped on every remit change), a
    `commit` naming the office as its object (a different kind, `add_tenure` never grants it), and
    a `hold` that is already closed at seating (`until` set, so `.live` is False from the start) --
    and asserts the re-stamp at `establish` time touches only the first.

    `add_tenure` calls `_grant_remit` for every `hold`, live or not -- the grant is a SNAPSHOT taken
    AT SEATING, not gated on liveness -- so the closed hold IS granted once, to the office's remit
    as it stood when it was seated. What this test isolates is `_eff_establish`'s re-stamp on a
    LATER remit change, which the `.live` filter excludes it from: its grant stays frozen."""
    w, d = _establish_world()
    t_live = _seat_reeve(w, ["issue"])
    w.add_tenure(Tenure("t_commit", "p_low", "off_reeve", "commit", 0))
    w.add_tenure(Tenure("t_dead", "p_low", "off_reeve", "hold", 0, until=1))
    [t_commit] = [t for t in w.tenures if t.id == "t_commit"]
    [t_dead] = [t for t in w.tenures if t.id == "t_dead"]
    assert t_commit.granted_acts == (), "fixture: a `commit` Tenure should never be granted"
    assert t_dead.granted_acts == ("issue",), (
        f"fixture: a `hold`, even dead on arrival, is granted the snapshot AT SEATING -- got "
        f"{t_dead.granted_acts}")

    out = _establish(w, d, "e_restamp_filter", _founding(remit=["issue", "dispatch"]))
    ps = next(e for e in out if e.kind == "tenure.payload_set")
    touched = {c.subject for c in ps.changes}
    # `t_live.id` is in there; `off_reeve` rides along too -- `_apply_write` unions every earned
    # kind's touched ids onto every Event this act produces (the pre-existing `Receipt.field`
    # imprecision `hole_register.yaml`'s `H-71` `source:` already names), not this filter's concern.
    assert t_live.id in touched, touched
    assert t_commit.id not in touched and t_dead.id not in touched, touched
    assert t_live.granted_acts == ("issue", "dispatch"), t_live.granted_acts
    assert t_commit.granted_acts == (), "a `commit` Tenure was re-stamped as though it were a `hold`"
    assert t_dead.granted_acts == ("issue",), (
        f"a CLOSED `hold`'s grant moved off its seating-time snapshot: {t_dead.granted_acts}")


# =================================================================================================
# PLAN POSITION `13e` -- ONE READING OF THE REMIT.
# `workplans/2026-09-18-governance-settlement-behaviour-plan_part2.md`, position `13e`. Routes
# `loop/resolve.py`'s `_eligible` and `epistemic.py`'s `_ch_post_remit` (a remit reader until `17a`
# re-based it onto obligees) off the live
# `w.offices[...].remit_acts` and onto the Tenure's own `t.granted_acts` -- the same store
# `decision/options.py` already read, closing the THREE-readings-over-two-stores gap
# `epistemic.py`'s `_ch_post_remit` docstring tracked. FALSIFIER, both arms in one world: a `hold`
# opened before its office exists, then the office HAND-CREATED (no act) -> the resolver now
# REFUSES the remit verb it admitted before this position; the same shape but the office FOUNDED
# BY `establish` -> the resolver ADMITS, because `13f`'s re-stamp reaches the sitting holder. AND
# an AST scan: no `Office.remit_acts` attribute read anywhere in the non-test package outside
# `_grant_remit`, `Office.__post_init__` and `_eff_establish`.
# =================================================================================================


def test_13e_hand_created_office_refuses_act_established_office_admits():
    """**THE POSITION'S FALSIFIER, BOTH ARMS, ONE WORLD.** Two holders, each seated on an office
    id BEFORE that office exists, so each Tenure's `granted_acts` snapshot opens at `()`:

      * `p_mid` on `off_hand` -- the office is then HAND-CREATED (`w.offices[x] = Office(...)`, no
        act). Pre-`13e`, `_eligible` read `w.offices.get(t.object)` live and admitted the moment
        the dict held the id, regardless of the Tenure's own grant. Post-`13e` it reads
        `t.granted_acts`, which a hand-mutation never reaches -- REFUSED.
      * `p_low` on `off_act` -- the office is then FOUNDED BY A PLANTED `establish`. `13f`'s
        effect re-stamps every live `hold` on the id it wrote, so `t.granted_acts` picks up the
        grant in the same act -- ADMITTED.

    Both arms exercise the RESOLVER (`_eligible`, `loop/resolve.py`), not `person_side_eligible`:
    the person-side reading (`decision/options.py`) already read `t.granted_acts` before this
    position and was never the bug -- `13f`'s own falsifier
    (`test_13f_a_planted_establish_founds_the_office_and_grants_a_hold_opened_before_it`) pins the
    ADMIT arm through that reading already. This pins the WORLD-side half `13e` closes, and its
    REFUSE arm is the one no earlier test observes: before this position the resolver admitted it."""
    w, d = _establish_world()
    w.add_tenure(Tenure("t_hand", "p_mid", "off_hand", "hold", 0))
    w.add_tenure(Tenure("t_act", "p_low", "off_act", "hold", 0))
    [t_hand] = [t for t in w.tenures if t.id == "t_hand"]
    [t_act] = [t for t in w.tenures if t.id == "t_act"]
    assert "off_hand" not in w.offices and "off_act" not in w.offices, "fixture: neither exists yet"
    early_holders = [t for t in (t_hand, t_act) if t.granted_acts == ()]
    assert len(early_holders) >= 1, (
        "fixture: no hold was opened before its office existed -- the falsifier is vacuous")

    dispatch = VERB_TABLE["dispatch"]

    # ARM 1 -- HAND-CREATED: no act, so no re-stamp reaches `t_hand`. REFUSE.
    w.offices["off_hand"] = Office("off_hand", "Reeve", "S", ["issue", "dispatch"],
                                    conferral="appointed", faction="Crown")
    assert t_hand.granted_acts == (), "a hand-mutation re-granted a sitting holder"
    # G3: each act names the seat it is exercised through -- the holder's own. Without `via` the
    # REFUSE arm would pass for the wrong reason (no seat exercised at all) and observe nothing
    # about the snapshot; with it, the grant on THAT seat's `hold` is what decides.
    act_hand = Act(id="a_hand", actor="p_mid", verb="dispatch", payload={}, via="off_hand")
    assert not d._eligible(w, act_hand, dispatch), (
        "the resolver admitted `p_mid`'s `dispatch` off a hand-created office -- `_eligible` is "
        "still reading `w.offices[...].remit_acts` live instead of `t.granted_acts`")
    assert not person_side_eligible(w.persons["p_mid"], dispatch), (
        "control: the person-side reading was already correct before this position")

    # ARM 2 -- FOUNDED BY ACT: `establish`'s effect re-stamps `t_act` in the same act. ADMIT.
    out = _establish(w, d, "e_act", _founding(office="off_act"))
    kinds = [e.kind for e in out]
    assert kinds == ["office.established", "tenure.payload_set"], kinds
    assert t_act.granted_acts == ("issue", "dispatch"), (
        f"the act did not reach the sitting holder: {t_act.granted_acts}")
    act_act = Act(id="a_act", actor="p_low", verb="dispatch", payload={}, via="off_act")
    assert d._eligible(w, act_act, dispatch), (
        "the resolver refused `p_low`'s `dispatch` after a planted `establish` re-stamped the "
        "grant -- `13f`'s own falsifier and this position's complement")
    assert person_side_eligible(w.persons["p_low"], dispatch)


# ⚠ `test_13e_the_witness_channel_also_reads_the_snapshot_not_the_live_office` STOOD HERE AND IS
# DELETED WITH ITS SUBJECT (plan position `17a`). It pinned `epistemic._ch_post_remit`'s half of
# `13e`: a remit-holding witness admitted off `t.granted_acts`, never the live office. `17a` retired
# that predicate outright -- r2 item 9 re-bases the channel onto the OBLIGEES of the seat an act was
# exercised through, which reads no remit at all -- so there is no longer a remit reading at that
# site to hold to the snapshot. `13e`'s resolver half is still pinned above, and its AST clause below
# still guards every `Office.remit_acts` read. The obligee channel's own falsifiers are in
# `tests/test_obligees.py`.


def _remit_acts_attribute_reads_outside_allowlist() -> list:
    """Every `Attribute` node named `remit_acts` anywhere under the package's NON-TEST sources,
    outside `_grant_remit`, `Office.__post_init__` and `_eff_establish` -- the allow-list the
    position's own falsifier names. `tests/` is excluded on purpose: a fixture asserting
    `office.remit_acts == [...]` or hand-mutating one to build the SNAPSHOT-vs-mirror scenario is
    the test's job, not a consumer of the fact through the eligibility path this scan protects.
    A dict-key string (`t.payload["remit_acts"]`) is a `Subscript`/`Constant`, never an
    `Attribute`, so `Tenure.granted_acts`'s own storage never matches this scan by construction."""
    violations = []
    for path in sorted(files.PACKAGE_DIR.rglob("*.py")):
        rel = path.relative_to(files.PACKAGE_DIR)
        if rel.parts[0] == "tests":
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        allowed_spans = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name in ("_grant_remit", "_eff_establish"):
                allowed_spans.append((node.lineno, node.end_lineno))
            elif isinstance(node, ast.ClassDef) and node.name == "Office":
                allowed_spans += [(sub.lineno, sub.end_lineno) for sub in node.body
                                   if isinstance(sub, ast.FunctionDef) and sub.name == "__post_init__"]
        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute) and node.attr == "remit_acts":
                if not any(a <= node.lineno <= b for a, b in allowed_spans):
                    violations.append(f"{rel.as_posix()}:{node.lineno}")
    return violations


def test_13e_no_remit_acts_attribute_read_outside_the_three_allow_listed_sites():
    """**THE POSITION'S FALSIFIER, AST CLAUSE.** Before this position, `loop/resolve.py`'s
    `_eligible` and `epistemic.py`'s `_ch_post_remit` were a fourth and fifth reader of
    `Office.remit_acts`, beyond the three this scan allow-lists; this test observes their absence
    now that both read `t.granted_acts` instead. A fourth reader is PLANNED
    (`budget()` counting `t.granted_acts`, not `Office.remit_acts` -- not this position's job), so
    this pins the CURRENT set to catch a future regression back onto the office-side field rather
    than to block anything today."""
    violations = _remit_acts_attribute_reads_outside_allowlist()
    assert violations == [], (
        f"`Office.remit_acts` read as an attribute outside `_grant_remit`/`Office.__post_init__`/"
        f"`_eff_establish` at {violations} -- position `13e` consolidated every consumer onto "
        f"`Tenure.granted_acts`")


# =================================================================================================
# PLAN POSITION `13d-i` -- OFFICES AS DATA (items 1-4; item 5, `offices.yaml`, is a later unit).
# `workplans/2026-09-18-governance-settlement-behaviour-plan_part2.md`, position `13d-i`. The two
# bases are rostered values (`rosters.yaml: conferral_bases`, `revocation_bases`) carrying
# `ED-IN-0256` rulings (2) and (3); `_req_confer` / `_req_establish` share a membership test and
# `_req_revoke` dispatches on the seat's declared basis, with no `is_title` branch (`H-109`).
# FALSIFIER `LB-10c`, re-pointed by ruling (3): a titled seat is revocable ONLY by the holder of a
# seat on the rung directly above it, in its faction -- every candidate iterated and counted.
# =================================================================================================

_RUNG_ABOVE = "rung_above_same_faction"       # `revocation_bases`' one member, ruling (3)


def _person(w, pid):
    """A bare person, placed the way `tiny_world` places its own."""
    w.persons[pid] = Person(pid, pid)
    w.rungs[pid] = Rung(pid, "person")
    w.add_tenure(Tenure(f"t_in_{pid}", pid, "Hh", "contain", 0))


def _seat_on(w, pid, oid, post, rung, faction, remit=("issue",)):
    """Seat `pid` on a new office, the office constructed FIRST so the grant is correct at seating."""
    if pid not in w.persons:
        _person(w, pid)
    w.offices[oid] = Office(oid, post, rung, list(remit), faction=faction)
    w.add_tenure(Tenure(f"t_{oid}", pid, oid, "hold", 0))


def _ladder_world():
    """`tiny_world` (R ⊃ D ⊃ S ⊃ Hh; `p_high` holds `off_duke`, a Crown `Duke` at `D`), plus a
    SIBLING duchy `D2` under `R` and a SECOND realm `R2` containing nothing of `R`'s. The duke's
    seat declares the rostered revocation basis."""
    w, d = _establish_world()
    w.rungs["D2"] = Rung("D2", "duchy")
    w.add_tenure(Tenure("t_d2_in_r", "D2", "R", "contain", 0))
    w.rungs["R2"] = Rung("R2", "realm")
    w.offices["off_duke"].revocation = _RUNG_ABOVE
    return w, d


def _seat_of(w, actor):
    """The one seat `actor` holds, or `None` -- what a candidate revoker EXERCISES since G3, when
    `_req_revoke` asks ruling (3) of `Act.via` and not of every seat the actor holds. Refuses a
    fixture that seats one candidate twice, because then WHICH seat is the question under test."""
    seats = sorted(t.object for t in w.tenures
                   if t.kind == "hold" and t.subject == actor and t.live and t.object in w.offices)
    assert len(seats) <= 1, f"fixture: {actor} holds {seats} -- name the seat it exercises"
    return seats[0] if seats else None


def _may_revoke(w, actor, office) -> bool:
    return _preds._req_revoke(w, Act(id=f"r_{actor}_{office}", actor=actor, verb="revoke",
                                     payload={"office": office}, via=_seat_of(w, actor)))


def test_13d_i_lb10c_a_titled_seat_is_revocable_only_by_the_seat_above_in_its_faction():
    """**`LB-10c`, AS RULING (3) RE-POINTS IT.** r2 named it `..._revocable_only_by_a_holder_of_its_
    domain` and priced it on a three-conjunct `holdings` rule; both predate `ED-IN-0256`, so this
    asserts the ruling. The target is TITLED (`Duke`, on `titles.domains`), because that is the case
    the deleted `is_title` branch treated specially.

    Ten candidates, each isolating one way to be WRONG about "rung above of same faction" -- the
    faction, the rank, the rung, the land, the seat itself -- and EXACTLY ONE is admitted. The loop
    asserts it ran to completion (`CLAUDE.md` §0.1 pt 2).

    ⚠ **DOES NOT ISOLATE "PARENT" FROM "NEAREST SAME-FACTION ANCESTOR" (corrected 2026-09-26,
    found by an antagonist pass).** In THIS world the target's only ancestor at any distance is
    also its immediate parent (`R` sits directly above `D`), so a mutant that walked past an empty
    or foreign parent to find the nearest same-faction seat would still pass every candidate here.
    `test_13d_i_an_empty_parent_refuses_even_a_same_faction_grandparent` is the test that isolates
    it, with a chain long enough for the two readings to disagree."""
    w, _ = _ladder_world()
    assert title_domain(w.offices["off_duke"].post) == "duchy", "fixture: the target is not a title"
    _seat_on(w, "c_king", "off_king", "King", "R", "Crown")                  # above, same faction
    _seat_on(w, "c_rival_king", "off_rival_king", "King", "R", "Hafenmark")  # above, OTHER faction
    _seat_on(w, "c_far_king", "off_far_king", "King", "R2", "Crown")         # outranks, not above
    _seat_on(w, "c_peer_duke", "off_peer_duke", "Duke", "D2", "Crown")       # sibling rung
    _seat_on(w, "c_chancellor", "off_chancellor", "Chancellor", "D", "Crown")  # the SAME rung
    _seat_on(w, "c_mayor", "off_mayor", "Mayor", "S", "Crown")               # below
    _seat_on(w, "c_councillor", "off_privy", "Privy Councillor", None, "Crown")  # no rung at all
    _person(w, "c_landholder")
    w.add_tenure(Tenure("t_land_r", "c_landholder", "R", "hold", 0))         # HOLDS the rung above
    candidates = {
        "c_king": True, "c_rival_king": False, "c_far_king": False, "c_peer_duke": False,
        "c_chancellor": False, "c_mayor": False, "c_councillor": False, "c_landholder": False,
        "p_high": False,                                         # the target's own holder
        "p_other": False,                                        # holds nothing
    }
    assert in_holdings(w, "c_landholder", "R"), "fixture: the landholder does not hold the rung"
    checked, admitted = 0, []
    for pid, expected in candidates.items():
        got = _may_revoke(w, pid, "off_duke")
        assert got is expected, f"{pid}: `_req_revoke` answered {got}, ruling (3) says {expected}"
        checked += 1
        admitted += [pid] if got else []
    assert checked == len(candidates) and checked >= 10, f"the sweep checked {checked}"
    assert admitted == ["c_king"], admitted


def test_13d_i_the_seat_above_of_another_faction_refuses_though_it_meets_the_old_title_rule():
    """**THE DIFFERENT-FACTION CASE, BUILT TO SATISFY EVERYTHING THE DELETED RULE ASKED.** The
    rival King sits on the rung above the duchy (so the old containment purview held), OUTRANKS a
    duke (realm over duchy in `rung_kinds`), and HOLDS THE DUCHY (`in_holdings`) -- the 2026-09-02
    title rule's three conjuncts, all true. Ruling (3) refuses him on the one thing that differs:
    his faction. The control is his Crown twin in the same world, identical but for the faction."""
    w, _ = _ladder_world()
    for pid, oid, fac in (("c_rival_king", "off_rival_king", "Hafenmark"),
                          ("c_king", "off_king", "Crown")):
        _seat_on(w, pid, oid, "King", "R", fac)
        w.add_tenure(Tenure(f"t_land_d_{pid}", pid, "D", "hold", 0))
        assert in_holdings(w, pid, "D"), f"fixture: {pid} does not hold the duchy"
    assert RUNG_KINDS.index(w.rungs["R"].kind) > RUNG_KINDS.index(w.rungs["D"].kind)
    assert world_q.parent_of(w, "D") == "R", "fixture: the King's rung is not above the duchy"
    assert w.offices["off_rival_king"].faction != w.offices["off_duke"].faction
    assert not _may_revoke(w, "c_rival_king", "off_duke"), (
        "a higher-ranked seat of ANOTHER faction, on the rung above and holding the duchy, stripped "
        "the duke -- the rewrite is still the purview/holdings/rank conjunction")
    assert _may_revoke(w, "c_king", "off_duke"), "control: the same-faction twin is refused"


def test_13d_i_an_empty_parent_refuses_even_a_same_faction_grandparent():
    """**PINS "PARENT" AGAINST "NEAREST SAME-FACTION SEAT ABOVE."** Every other `13d-i` fixture
    seats someone at the target's immediate parent rung, so the two readings never disagree there
    -- an antagonist pass found this gap directly: with only those fixtures, a mutant that walks
    PAST an empty or foreign-faction parent to the nearest same-faction seat passes every existing
    test. This builds the one world where the readings diverge: `off_reeve_hh` sits at `Hh`, whose
    parent `S` holds NO seat at all, while its grandparent `D` holds `off_duke`, Crown -- the same
    faction. Under `seated_on_the_rung_above`'s own reading (the ADJACENT rung only), the duke's
    holder must REFUSE; under a nearest-same-faction-ancestor reading he would be admitted. Ruling
    (3)'s words are "rung above", not a walk -- that verb belongs to ruling (4)'s purview clause
    ("owner of highest rung in CHAIN of ownership"), a different mechanism this position does not
    build."""
    w, _ = _ladder_world()
    assert world_q.parent_of(w, "S") == "D" and world_q.parent_of(w, "Hh") == "S", (
        "fixture: the chain is not Hh -> S -> D as assumed")
    assert not any(t.kind == "hold" and t.object in w.rungs and w.rungs[t.object].kind == "S"
                   for t in w.tenures), "fixture: someone already sits at S"
    _seat_on(w, "p_reeve", "off_reeve_hh", "Reeve", "Hh", "Crown", remit=("issue",))
    w.offices["off_reeve_hh"].revocation = _RUNG_ABOVE
    assert w.offices["off_duke"].faction == w.offices["off_reeve_hh"].faction == "Crown", (
        "fixture: the duke and the reeve are not the same faction")
    assert not _may_revoke(w, "p_high", "off_reeve_hh"), (
        "the Crown duke, two rungs above an empty parent, revoked a Crown reeve -- "
        "seated_on_the_rung_above walked PAST the empty parent instead of refusing at it")


def test_13d_i_one_rule_at_every_depth_and_no_title_branch():
    """GENERAL OVER ANY SEAT AND ANY DEPTH (`CLAUDE.md` §0 -- never special-case). Three depths --
    a duchy under a realm, a settlement under a duchy, a hearth under a settlement -- and at the
    settlement a TITLED seat (`Mayor`) and an UNTITLED one (`Reeve`) side by side. Each is
    revocable by the seat on its parent rung and by nothing further up; the titled and untitled
    seats answer identically, which is `H-109` closed as a behaviour, not as a grep."""
    w, _ = _ladder_world()
    _seat_on(w, "c_king", "off_king", "King", "R", "Crown")
    _seat_on(w, "c_mayor", "off_mayor_s", "Mayor", "S", "Crown")
    _seat_on(w, "p_mid", "off_reeve_s", "Reeve", "S", "Crown")
    _seat_on(w, "p_low", "off_head_hh", "Family Head", "Hh", "Crown")
    for oid in ("off_mayor_s", "off_reeve_s", "off_head_hh"):
        w.offices[oid].revocation = _RUNG_ABOVE
    assert title_domain("Mayor") and title_domain("Reeve") is None, "fixture: titled/untitled pair"
    cases = [
        ("off_duke", "c_king", True), ("off_duke", "c_mayor", False),
        ("off_mayor_s", "p_high", True), ("off_mayor_s", "c_king", False),   # grandparent
        ("off_reeve_s", "p_high", True), ("off_reeve_s", "c_king", False),
        ("off_head_hh", "c_mayor", True), ("off_head_hh", "p_high", False),  # grandparent
    ]
    checked = 0
    for oid, pid, expected in cases:
        assert _may_revoke(w, pid, oid) is expected, (oid, pid, expected)
        checked += 1
    assert checked == len(cases) >= 8
    assert [_may_revoke(w, p, "off_mayor_s") for p in ("p_high", "c_king")] == \
        [_may_revoke(w, p, "off_reeve_s") for p in ("p_high", "c_king")], (
            "a titled and an untitled seat on the same rung answer differently -- an is_title branch")


def test_13d_i_the_revocation_basis_is_a_rostered_value_and_gates_the_rule():
    """The right revoker is refused unless the seat DECLARES a rostered basis: `None` (strippable by
    nobody, r2's `none`), r2's superseded `purview` (hand-mutated past the constructor), and the
    rostered value, in that order, on one seat and one actor. And the constructor refuses to build
    a seat declaring the off-roster value -- the `remit_acts` refusal's shape, one field along."""
    w, _ = _ladder_world()
    _seat_on(w, "c_king", "off_king", "King", "R", "Crown")
    seat = w.offices["off_duke"]
    seen = []
    for basis, expected in ((None, False), ("purview", False), (_RUNG_ABOVE, True)):
        seat.revocation = basis
        seen.append(_may_revoke(w, "c_king", "off_duke"))
        assert seen[-1] is expected, (basis, seen[-1])
    assert seen == [False, False, True], seen
    assert set(REVOCATION_BASES) == {_RUNG_ABOVE}, sorted(REVOCATION_BASES)
    with pytest.raises(Unspecified):
        Office("off_x", "Reeve", "S", [], faction="Crown", revocation="purview")
    assert Office("off_y", "Reeve", "S", [], faction="Crown", revocation=_RUNG_ABOVE).revocation


def test_13d_i_the_conferral_basis_is_roster_membership_not_a_nonempty_string():
    """**THE BEHAVIOUR CHANGE, STATED.** Before `13d-i` `has_conferral_basis` admitted any non-empty
    string -- including the free fixture string `test_season_shape.py` used, which is asserted
    REFUSED here. Now: every member of `conferral_bases` passes (all three iterated, not one
    sampled), an off-roster string and `None` refuse, through `has_conferral_basis` AND through
    `_req_confer` on an unheld office. The constructor refuses to BUILD the off-roster value, so
    that arm is reached by hand-mutation -- the predicate is tested on what it reads."""
    w, _ = _establish_world()
    off = w.offices["off_dicastery"]
    off.rung = "S"               # G3: ground inside the duke's purview, or nobody may confer it
    conf = Act(id="c_b", actor="p_high", verb="confer",
               payload={"office": "off_dicastery", "to": "p_mid"}, via="off_duke")
    checked = 0
    for basis in sorted(CONFERRAL_BASES):
        off.conferral = basis
        assert _preds.has_conferral_basis(off) and _preds._req_confer(w, conf), basis
        checked += 1
    assert checked == len(CONFERRAL_BASES) >= 3, checked
    for basis in (None, "something-not-on-the-roster", "the duke's remit (harness fixture)", ""):
        off.conferral = basis
        assert not _preds.has_conferral_basis(off), f"{basis!r} passed the basis test"
        assert not _preds._req_confer(w, conf), f"`_req_confer` admitted {basis!r}"
    with pytest.raises(Unspecified):
        Office("off_x", "Reeve", "S", [], faction="Crown", conferral="something-not-on-the-roster")


def test_13d_i_an_off_roster_conferral_on_establish_refuses_and_raises_nothing():
    """`13f`'s contract under the new test: `_req_establish` translates the constructor's new
    refusal to False, so an `establish` naming an off-roster basis emits `establish.refused`,
    constructs nothing, and lets no exception escape the fold. Every rostered basis founds."""
    w, d = _establish_world()
    act = Act(id="e_offroster", actor="p_high", verb="establish",
              payload=_founding(conferral="something-not-on-the-roster"), via="off_duke")
    with pytest.raises(Unspecified):
        office_described_by(act)
    out = d.resolve(mint_token(d.w, WriteClass.ACTS), [act], contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert [e.kind for e in out] == ["establish.refused"], [e.kind for e in out]
    assert "off_reeve" not in w.offices
    founded = 0
    for i, basis in enumerate(sorted(CONFERRAL_BASES)):
        out = _establish(w, d, f"e_ok_{i}", _founding(office=f"off_reeve_{i}", conferral=basis))
        assert [e.kind for e in out] == ["office.established"], (basis, [e.kind for e in out])
        founded += 1
    assert founded == len(CONFERRAL_BASES) >= 3


def test_13d_i_the_title_in_a_body_refusal_is_rehomed_not_dropped():
    """Item (4), r2 `03` SC-5: *"deleting the title helpers loses no constructor invariant"*. The
    refusal is now a function of its own (`state/carriers.py::refuse_a_title_in_a_body`), which
    the constructor still calls and `offices.yaml`'s loader will. Asserted on BOTH routes, for EVERY
    title on the roster (counted), with the message naming the title AND the body; and the two
    non-cases -- a title with no body, a non-title in a body -- pass."""
    checked = 0
    for ttl in sorted(TITLE_DOMAINS):
        with pytest.raises(Forbidden) as direct:
            refuse_a_title_in_a_body("off_t", ttl, "Imperial Court")
        with pytest.raises(Forbidden) as built:
            Office("off_t", ttl, None, [], body="Imperial Court")
        for exc in (direct.value, built.value):
            assert repr(ttl) in str(exc) and "'Imperial Court'" in str(exc), str(exc)
        checked += 1
    assert checked == len(TITLE_DOMAINS) >= 11, checked
    refuse_a_title_in_a_body("off_t", "King", None)                  # a title held at a rung
    refuse_a_title_in_a_body("off_t", "Chancellor", "Imperial Court")  # an office in an organ
    assert Office("off_t", "Chancellor", None, [], body="Imperial Court").faction == "Crown"


def test_13d_i_revoke_executes_in_the_fold_for_the_seat_above_and_refuses_the_other_faction():
    """§0.2 -- DONE MEANS IT RUNS. Planted `revoke` acts through the resolver, both revokers seated
    with `revoke` in their grant so eligibility passes and the PREDICATE decides: the other
    faction's King first (`revoke.refused`; the duke's `hold` survives), then the Crown King
    (`tenure.closed`; it does not). Asserted on the Events."""
    w, d = _ladder_world()
    _seat_on(w, "c_rival_king", "off_rival_king", "King", "R", "Hafenmark", remit=("revoke",))
    _seat_on(w, "c_king", "off_king", "King", "R", "Crown", remit=("revoke",))
    held = lambda: [t for t in w.tenures if t.kind == "hold" and t.object == "off_duke" and t.live]
    assert held(), "fixture: nobody holds the duke's seat"

    def run(aid, actor):
        # G3: each King revokes through his own seat (`Act.via`), which is what eligibility,
        # ruling (3) and the write gate's T-o clause now ask.
        return [e.kind for e in d.resolve(mint_token(d.w, WriteClass.ACTS),
            [Act(id=aid, actor=actor, verb="revoke", payload={"office": "off_duke"},
                 via=_seat_of(w, actor))],
            contest_max_depth=w.fixtures.get("contest_max_depth"))]

    assert run("rv_rival", "c_rival_king") == ["revoke.refused"]
    assert held(), "the other faction's King closed the duke's hold"
    kinds = run("rv_king", "c_king")
    assert "tenure.closed" in kinds and "revoke.refused" not in kinds, kinds
    assert not held(), "the fold accepted the revocation and the duke's hold survived"


# =================================================================================================
# PLAN POSITION `8a` -- `13d-i` ITEM 5, THE LAST OPEN ITEM OF THE UNIT ABOVE: `offices.yaml` AND
# ITS `harness/populated.py` WIRING. `workplans/2026-09-28-the-plan-one-order-mc-v18-retired.md`,
# position `8a`. Two folds, neither Jordan's: `title_domain`/`TITLE_DOMAINS` now read
# `engine/season/offices.yaml: titles: domains:` rather than `rosters.yaml: titles` (Layer 1 §B.7/
# §E.1, r2 `05_LEDGER_AND_BUILD.md` RULED (c)); and `offices.yaml`'s 29 authored seats carry
# `conferral`/`revocation` recomputed against `ED-IN-0256` (r2 `03`'s own value sets are superseded
# -- see `offices.yaml`'s own header for the row-by-row translation). FALSIFIERS: the fold changes
# no answer `title_domain` gives; every authored seat constructs against the live rosters; the 19
# seats this loop already seats before this position carry a REAL basis afterward, not the
# dataclass default; and a full season still executes end to end (§0.2).
# =================================================================================================

def test_8a_title_domain_now_reads_offices_yaml_and_answers_identically():
    """THE FOLD CHANGED WHERE, NOT WHAT. `rosters.yaml: titles` was left in place for one session
    as orphaned residue (a concurrent plan position owned that file -- `offices.yaml`'s own header
    names the scope decision) and is now physically deleted (Phase-1 methodology close, 2026-09-29,
    `/simplify` ALTITUDE lens) -- nothing read it through `title_domain` even before the deletion:
    `TITLE_DOMAINS` is bound from `engine/season/offices.yaml` at import. `PINNED` is the byte-exact
    reading of `rosters.yaml: titles: domains:` taken at the fold (position `8a`) and verified
    against it there; with the source roster gone, this is now the record the fold stays honest
    against, not a second live copy (the same declared-literal shape `harness/arms.py`'s retired
    arm pairs use for the same reason)."""
    from ..data import files
    from ..data.rosters import load_yaml

    # roster-exempt: PINNED HISTORY, not the game's vocabulary -- `rosters.yaml: titles: domains:`,
    # byte-identical to what it read before its physical deletion (verified at that deletion).
    PINNED = {
        "King": "realm", "Queen": "realm", "Duke": "duchy", "Duchess": "duchy",
        "Count": "province", "Countess": "province", "Lord": "territory",
        "Mayor": "settlement", "Community Leader": "community",
        "Family Head": "hearth", "Individual": "person",
    }
    assert dict(TITLE_DOMAINS) == PINNED, (
        "offices.yaml: titles: domains: disagrees with the pinned reading of the roster it folded "
        f"from: {TITLE_DOMAINS} != {PINNED}")
    assert set(TITLE_DOMAINS.values()) == set(RUNG_KINDS), (
        "the ladder is no longer total over the rungs after the fold")
    for post, dom in TITLE_DOMAINS.items():
        assert title_domain(post) == dom, f"title_domain({post!r}) disagrees with the mapping it reads"
    assert title_domain("Dicastery") is None, "a non-title post reads as a title after the fold"

    doc = load_yaml(files.OFFICES_YAML.read_text(encoding="utf-8"))
    assert doc["titles"]["domains"] == PINNED, "offices.yaml's own file text disagrees with the pinned fold"


def test_8a_every_authored_seat_constructs_against_the_live_rosters():
    """`offices.yaml`'s 29 seats are a REAL content file, not documentation -- every row must build
    a lawful `Office` against today's `office_bodies`/`factions`/`remit_acts`/`conferral_bases`/
    `revocation_bases`, the same construction-time proof r2 `03` §A.13 ran against
    `offices_draft.yaml` (which found 15 of 25 draft rows COULD NOT construct). `rung` is passed as
    a placeholder string: this test is about `body`/`faction`/`remit_acts`/`conferral`/`revocation`
    membership, not about anchor resolution (the `13d-iii` section below resolves every anchor
    against a built realm)."""
    from ..data import files
    from ..data.rosters import load_yaml

    doc = load_yaml(files.OFFICES_YAML.read_text(encoding="utf-8"))
    seats = doc["seats"]
    assert len(seats) == 29, f"expected 29 authored seats, found {len(seats)}"
    ids = [s["id"] for s in seats]
    assert len(ids) == len(set(ids)), f"duplicate seat id(s): {sorted(i for i in ids if ids.count(i) > 1)}"
    for s in seats:
        Office(s["id"], s["post"], "PLACEHOLDER_RUNG", list(s["remit_acts"]),
               body=s.get("body"), faction=s.get("faction"),
               conferral=s.get("conferral"), revocation=s.get("revocation"))
    # `03` §A.15's own distribution counts, re-derived here rather than trusted: seven bases must
    # sum to 29 or a count in this file's header is wrong, exactly the defect `CLAUDE.md` §0.1 pt 4
    # names (a distribution that does not sum to the table's own row count).
    cnf = Counter(s["conferral"] for s in seats)
    rvk = Counter(s["revocation"] for s in seats)
    assert sum(cnf.values()) == 29 and sum(rvk.values()) == 29
    assert cnf == Counter({"appointed": 15, "elected": 8, None: 6}), cnf
    assert rvk == Counter({"rung_above_same_faction": 22, None: 7}), rvk


def test_8a_a_repeated_row_id_refuses_at_load_instead_of_being_collapsed(tmp_path, monkeypatch):
    """`_load_offices` checked no row id for uniqueness: `build_realm` keys the seats it matched by
    row id and skips a row already in that dict, so a second row under one id was collapsed without a
    sound (the test above asserts uniqueness of the CHECKED-IN file, which a loader refusal does not
    depend on). The loader is pointed at a throwaway copy; the unchanged copy is the positive control
    (it loads, all 29 rows), so a loader that refused every file cannot pass."""
    import yaml
    from ..data import rosters

    real = rosters.load_yaml(files.OFFICES_YAML.read_text(encoding="utf-8"))
    path = tmp_path / "offices.yaml"
    monkeypatch.setattr(rosters, "OFFICES_YAML", path)

    path.write_text(yaml.safe_dump(real), encoding="utf-8")
    assert len(rosters._load_offices()["seats"]) == 29

    first = real["seats"][0]
    for twin in (dict(first), dict(first, holder="NPC-999", post="Somebody Else")):
        dup = dict(real, seats=list(real["seats"]) + [twin])
        path.write_text(yaml.safe_dump(dup), encoding="utf-8")
        with pytest.raises(Unspecified) as red:
            rosters._load_offices()
        assert first["id"] in str(red.value) and "more than one row" in str(red.value), str(red.value)


def test_8a_every_authored_seat_carries_its_authored_basis_after_the_overlay():
    """`harness/populated.py` lays `offices.yaml`'s `conferral`/`revocation` on every authored seat,
    matched to the one its per-case loop built or minted from the row (`13d-iii`). Before `8a` every
    seat carried `conferral=None, revocation=None`, the dataclass default, regardless of what
    `ED-IN-0256` says of it. This asserts the overlay actually ran: each seat matches its row, the
    four hereditary/no-revoker seats (King, Queen, Heir, Princess) correctly keep `None`, and --
    a passing test that could not tell 'overlaid with None' from 'never overlaid' would not
    observe the failure it excludes (`CLAUDE.md` §0.1 pt 2) -- a NON-None seat on each axis is
    checked too. (Was nineteen seats and skipped the `[NEW]` rows; four of those are seated by the
    loop and six are minted, so the census names the Office each row stands for.)"""
    from ..data import files
    from ..data.rosters import load_yaml

    doc = load_yaml(files.OFFICES_YAML.read_text(encoding="utf-8"))
    w = build_realm(seed=0)
    stands_for = w._office_census["authored"]
    checked = 0
    checked_a_real_conferral = checked_a_real_revocation = False
    for s in doc["seats"]:
        oid = stands_for.get(s["id"])
        off = w.offices.get(oid)
        assert off is not None, f"{s['holder']} ({s['post']!r}) built no office"
        assert off.conferral == s["conferral"], (
            f"{oid} ({off.post!r}): conferral={off.conferral!r}, offices.yaml says {s['conferral']!r}")
        assert off.revocation == s["revocation"], (
            f"{oid} ({off.post!r}): revocation={off.revocation!r}, offices.yaml says {s['revocation']!r}")
        checked += 1
        checked_a_real_conferral = checked_a_real_conferral or off.conferral is not None
        checked_a_real_revocation = checked_a_real_revocation or off.revocation is not None
    assert checked == len(doc["seats"]) == 29, checked
    assert checked_a_real_conferral and checked_a_real_revocation, (
        "every seat checked had a None basis -- this test cannot tell the overlay ran")


def test_8a_a_season_still_executes_end_to_end_with_the_overlay_wired():
    """§0.2 -- DONE MEANS IT RUNS. The overlay changes what nineteen live offices declare; this
    confirms a full season over the populated world still resolves rather than raising, which a
    construction-only check (the two tests above) cannot show."""
    from ..harness import populated
    out = populated.run(seasons=1, seed=0)
    assert out.get("acts", 0) > 0, "a populated season formed no acts with the overlay wired"


# =================================================================================================
# PLAN POSITION `13d-iii` -- RUNG ANCHORS FOR SEATS, THE `[NEW]` SEATS, THE REMIT OVERLAY (H-163
# limit 1). `harness/populated.py::resolve_anchor` is ONE resolver over r2 `03`'s four anchor forms;
# `build_realm` gives every authored seat its resolved rung (`Office.rung` AND `scope_rung`), mints
# the six rows no loop-built seat stands for, and overlays `remit_acts` (`dispatch` left where it
# is -- J-8, `offices.yaml: meta: remit_unruled`). FALSIFIERS: every row's anchor resolves to one
# live rung of its own kind, checked against an INDEPENDENT derivation of each rung; the resolver
# refuses what names no single rung and a broken form turns the build red; no seat but the one
# declared exception is rungless; a season executes a `levy`/`issue` through a seat (`Act.via`
# set) where the same seed refused 18 of 19 four-season levies on `authority` before (`aperture 4 0`,
# the parent tree `5519cf52`, as `H-163` limit 1 and the `13d-iii` commit record it).
# =================================================================================================

@pytest.fixture(scope="module")
def _realm13():
    return build_realm(seed=0)


def _seat_rows():
    from ..data.rosters import OFFICES_SEATS
    return OFFICES_SEATS


def _geography():
    from ..harness import populated
    return populated._load(populated.GEOGRAPHY)


def test_13d_iii_every_authored_anchor_resolves_to_one_live_rung_of_its_own_kind(_realm13):
    """THE INDEPENDENT CHECK. The resolver reads an index `build_realm` fills as it mints; this asks
    each rung of the world it should have been. A realm is the one; a duchy is the parent of the
    territories its FACTION holds (`contain`, read off the geography -- not off `duchy_of`, which
    is what filled the index); a territory is `territory_rung_id`, the id relation's one owner. A
    row that resolved to a rung of another kind, or to a neighbour, fails here. The `[NEW]` rows are
    counted separately because the position's falsifier names them."""
    from ..data.rosters import territory_rung_id
    from ..state.containment import parent_of

    w = _realm13
    geo = _geography()
    stands_for = w._office_census["authored"]
    by_kind, new_resolved = Counter(), 0
    for row in _seat_rows():
        (kind, key), = row["rung"].items()
        off = w.offices[stands_for[row["id"]]]
        assert off.rung in w.rungs, f"{row['id']}: {off.rung!r} is not a rung of this world"
        assert w.rungs[off.rung].kind == kind, (
            f"{row['id']} anchors a {kind}, resolved to a {w.rungs[off.rung].kind}: {off.rung!r}")
        if kind == "realm":
            expect = {r for r, x in w.rungs.items() if x.kind == "realm"}
        elif kind == "duchy":
            expect = {parent_of(w, territory_rung_id(tid)) for tid, terr in geo["provinces"].items()
                      if terr.get("faction") == key}
        else:
            expect = {territory_rung_id(key)}
        assert expect == {off.rung}, (
            f"{row['id']} {row['rung']}: the world's own structure says {sorted(expect)}, the seat "
            f"stands at {off.rung!r}")
        by_kind[kind] += 1
        new_resolved += row["note"].startswith("[NEW]")
    assert sum(by_kind.values()) == len(_seat_rows()) == 29, by_kind
    assert set(by_kind) == {"realm", "duchy", "territory"}, (
        f"{by_kind}: a form no row uses is not observed here -- the settlement form has its own test")
    assert new_resolved == 10, f"{new_resolved} `[NEW]`-marked rows resolved; r2 `03` marks ten"


def test_13d_iii_the_settlement_form_resolves_and_the_resolver_refuses_what_names_no_single_rung(_realm13):
    """The fourth form no row authors, and EVERY refusal the resolver owes. `{settlement: <code>}`
    must land on the settlement rung inside the territory the geography says holds it; each bad
    form must raise `Unspecified` (counted -- a loop of `pytest.raises` that never ran is silent)."""
    from ..data.rosters import territory_rung_id
    from ..harness.populated import resolve_anchor
    from ..state.containment import parent_of

    w, geo = _realm13, _geography()
    code, srow = next(iter(geo["settlements"].items()))
    rid = resolve_anchor(w, w._anchors, {"settlement": code})
    assert w.rungs[rid].kind == "settlement"
    assert parent_of(w, rid) == territory_rung_id(srow["territory"]), (
        f"{{settlement: {code!r}}} resolved to {rid!r}, which is not inside the territory the "
        "geography gives that settlement")
    refused = 0
    for bad in ({}, {"realm": True, "duchy": "Crown"}, "realm", None, {"realm": "r_valoria"},
                {"duchy": "Nobody"}, {"province": "P1"}, {"territory": "T99"}, {"settlement": True}):
        with pytest.raises(Unspecified):
            resolve_anchor(w, w._anchors, bad, "a probe")
        refused += 1
    assert refused == 9


def test_13d_iii_a_key_of_the_wrong_type_is_refused_not_resolved_or_raised(_realm13):
    """`True == 1` and the two hash alike, so `{realm: 1}` used to resolve to `{realm: true}`'s rung,
    and an unhashable key (`{duchy: ["Crown"]}`) raised `TypeError` out of the dict lookup instead of
    the `Unspecified` every other malformed form raises. POSITIVE CONTROL: `{realm: true}` still
    resolves, to the one realm rung, so a resolver that refused every bool cannot pass."""
    from ..harness.populated import resolve_anchor

    w = _realm13
    realm_rung = next(r for r, x in w.rungs.items() if x.kind == "realm")
    assert resolve_anchor(w, w._anchors, {"realm": True}) == realm_rung
    refused = 0
    for bad in ({"realm": 1}, {"duchy": ["Crown"]}, {"territory": 9}, {"realm": {"x": 1}}, {1: "x"}):
        with pytest.raises(Unspecified):
            resolve_anchor(w, w._anchors, bad, "a probe")
        refused += 1
    assert refused == 5


def test_13d_iii_a_stale_index_entry_is_refused_not_trusted(_realm13):
    """The staleness clause, `rid not in w.rungs or w.rungs[rid].kind != kind`: an index entry that
    names a rung the world does not have, or one of ANOTHER kind, is refused rather than resolved.
    Both arms are reached by corrupting a COPY of the index, and each arm is asserted separately so
    a mutation deleting either disjunct turns one of them red; the uncorrupted copy is the control."""
    from ..harness.populated import resolve_anchor

    w = _realm13
    realm_rung = next(r for r, x in w.rungs.items() if x.kind == "realm")
    duchy_rung = next(r for r, x in w.rungs.items() if x.kind == "duchy")
    assert resolve_anchor(w, dict(w._anchors), {"realm": True}) == realm_rung
    ghost = dict(w._anchors)
    ghost[("realm", True)] = "r_no_such_rung"
    assert "r_no_such_rung" not in w.rungs
    with pytest.raises(Unspecified):
        resolve_anchor(w, ghost, {"realm": True}, "a probe")
    wrong_kind = dict(w._anchors)
    wrong_kind[("realm", True)] = duchy_rung
    with pytest.raises(Unspecified):
        resolve_anchor(w, wrong_kind, {"realm": True}, "a probe")


def test_13d_iii_a_minted_row_may_not_reuse_a_standing_seat_id(_realm13, monkeypatch):
    """A MINTED seat is one no loop-built seat stands for, so its id must be fresh. A row carrying
    the id of a seat the loop already built used to REPLACE that seat without a sound. The probe
    renames the first minted row to the id of the loop-built `off_npc_031` (the seat NPC-031's
    `off_heir` row overlays); the realm must refuse, naming the id. The build with the real rows
    is the control (`_realm13`, and every other test here, build it)."""
    from ..harness import populated

    real = populated.OFFICES_SEATS
    minted_id = _realm13._office_census["minted"][0]
    rows = [dict(r, id="off_npc_031") if r["id"] == minted_id else r for r in real]
    assert sum(r["id"] == "off_npc_031" for r in rows) == 1
    monkeypatch.setattr(populated, "OFFICES_SEATS", rows)
    with pytest.raises(Forbidden) as red:
        build_realm(seed=0)
    assert "off_npc_031" in str(red.value) and "minted" in str(red.value), str(red.value)


def test_13d_iii_a_seat_may_not_list_its_own_holder_among_its_obligees(monkeypatch):
    """`_req_oblige` clause 3's rule at world-gen: the occupant is not his own seat's obligee. The
    one row that authors obligees is given its own holder as one; the realm must refuse, naming the
    seat. (The real file's obligee is another person -- `_realm13` builds it.)"""
    from ..harness import populated

    real = populated.OFFICES_SEATS
    withs = [r for r in real if r.get("obligees")]
    assert len(withs) == 1, [r["id"] for r in withs]
    row = withs[0]
    assert row["holder"] not in row["obligees"], "the real row already lists its holder"
    rows = [dict(r, obligees=list(r["obligees"]) + [r["holder"]]) if r is row else r for r in real]
    monkeypatch.setattr(populated, "OFFICES_SEATS", rows)
    with pytest.raises(Forbidden) as red:
        build_realm(seed=0)
    assert row["id"] in str(red.value) and "own holder" in str(red.value), str(red.value)


# --- `build_realm`'s loud-failure branches and its `cap` skips, each driven to its own test. A branch
# with no test that reaches it is a refusal nobody has seen fire; each of these was run with the
# branch DELETED and turns red (the mutation is named in each docstring's last line).

def _populated_rows(monkeypatch, rows=None, by_holder=None):
    """Point `build_realm` at a replacement roster of authored rows (and, where given, its by-holder
    index) through the two module globals it reads, and return the module."""
    from ..harness import populated
    if rows is not None:
        monkeypatch.setattr(populated, "OFFICES_SEATS", rows)
    if by_holder is not None:
        monkeypatch.setattr(populated, "OFFICES_BY_HOLDER", by_holder)
    return populated


def test_13d_iii_a_titled_loop_built_holder_with_no_row_refuses_instead_of_standing_rungless(
        _realm13, monkeypatch):
    """`elif governs is not None: raise Unspecified`. A titled holder the loop seats and no row
    names would be seated rungless, silently (the one derivation that gave a titled seat its rung is
    gone). The probe removes one titled single-row holder's row from both the roster and the by-holder
    index; the realm must refuse, naming the holder. CONTROL: the same holder WITH its row stands at
    a rung (the shared `_realm13`). Mutation: delete the `elif governs is not None:` branch."""
    from ..harness import populated

    w = _realm13
    stands_for, minted = w._office_census["authored"], set(w._office_census["minted"])
    titled = [r for r in populated.OFFICES_SEATS
              if r["id"] not in minted and len(populated.OFFICES_BY_HOLDER[r["holder"]]) == 1
              and title_domain(w.offices[stands_for[r["id"]]].post) is not None]
    assert titled, "no titled, loop-built, single-row holder: this probe has nothing to remove"
    row = titled[0]
    assert w.offices[stands_for[row["id"]]].rung is not None, "the control seat is rungless"
    _populated_rows(monkeypatch,
                    [r for r in populated.OFFICES_SEATS if r is not row],
                    {h: v for h, v in populated.OFFICES_BY_HOLDER.items() if h != row["holder"]})
    with pytest.raises(Unspecified) as red:
        build_realm(seed=0)
    assert row["holder"] in str(red.value) and "has no row for the seat" in str(red.value), \
        str(red.value)


def _ghost_of(real, row_id, **over):
    """A copy of a real authored row under a new id, for a probe to add to the roster."""
    src = next(r for r in real if r["id"] == row_id)
    return dict(src, **over)


def test_13d_iii_a_minted_row_whose_holder_is_not_in_the_cast_refuses_and_a_cap_skips_it(
        _realm13, monkeypatch):
    """`if pid not in w.persons: raise` (the minted pass) and its `cap is not None: continue` skip.
    A row naming a holder no case carries is a ghost in `leaders`: the full cast refuses it, naming
    the holder; the SAME roster under `build_realm(0, cap=10)` drops it without a sound, because a
    deliberately partial cast drops the seats whose holders it dropped (so it must not raise, and
    the ghost must not stand). Mutations: delete the raise (the full-cast arm turns red); delete the
    `cap` skip (the capped arm turns red)."""
    from ..harness import populated

    real = populated.OFFICES_SEATS
    ghost = _ghost_of(real, _realm13._office_census["minted"][0], id="off_probe_ghost",
                      holder="NPC-998", obligees=[])
    _populated_rows(monkeypatch, list(real) + [ghost])
    with pytest.raises(Unspecified) as red:
        build_realm(seed=0)
    assert "off_probe_ghost" in str(red.value) and "who is not in the cast this realm built" in str(
        red.value), str(red.value)
    w = build_realm(seed=0, cap=10)
    assert "off_probe_ghost" not in w.offices and "p_npc_998" not in w.persons
    assert len(w.persons) < len(_realm13.persons), "`cap=10` did not shrink the cast"


def test_13d_iii_a_cap_keeps_exactly_the_seats_whose_holders_it_kept():
    """The `cap` skips on the REAL roster, both of them. `cap` keeps the first N cases in load order;
    N is chosen so that the one authored `oblige` row (`off_restoration_leader`, held by NPC-003,
    obliging NPC-041) keeps its holder and loses its obligee. Then a row stands iff its holder is in
    the cast (`0 < kept < 29`, so neither arm is vacuous), and the seat keeps standing while its
    obligee's `oblige` is dropped -- the obligee skip. Mutations: delete the minted-pass skip or the
    obligee skip and the capped build raises instead."""
    from ..data.rosters import OFFICES_SEATS
    from ..harness.run_cases import load_cases

    row = next(r for r in OFFICES_SEATS if r.get("obligees"))
    (obligee,) = row["obligees"]
    ids = [c["id"] for c in load_cases("NPC")]
    cap = ids.index(row["holder"]) + 1
    assert ids.index(obligee) >= cap, "the obligee is inside the cap: this probe cannot drop it"
    w = build_realm(seed=0, cap=cap)
    kept = {r["id"] for r in OFFICES_SEATS if f"p_{r['holder'].lower().replace('-', '_')}" in w.persons}
    assert 0 < len(kept) < len(OFFICES_SEATS) == 29, len(kept)
    assert set(w._office_census["authored"]) == kept, sorted(set(w._office_census["authored"]) ^ kept)
    assert row["id"] in w._office_census["authored"]
    assert f"p_{obligee.lower().replace('-', '_')}" not in w.persons
    assert world_q.establishment_of(w, row["id"]) == []


def test_13d_iii_an_obligee_not_in_the_cast_refuses_and_a_cap_skips_it(_realm13, monkeypatch):
    """`if opid not in w.persons: raise` (the obligee pass). The one row that authors obligees is
    given one no case carries; the full cast refuses it, naming the obligee. (The capped arm, where
    the same shape is a silent skip, is `test_13d_iii_a_cap_keeps_exactly_the_seats...` above.)
    CONTROL: the real obligee builds in `_realm13`. Mutation: delete the raise."""
    from ..harness import populated

    real = populated.OFFICES_SEATS
    row = next(r for r in real if r.get("obligees"))
    assert world_q.establishment_of(_realm13, row["id"]) == ["p_npc_041"]
    _populated_rows(monkeypatch, [dict(r, obligees=["NPC-998"]) if r is row else r for r in real])
    with pytest.raises(Unspecified) as red:
        build_realm(seed=0)
    assert row["id"] in str(red.value) and "names the obligee 'NPC-998'" in str(red.value), \
        str(red.value)


def test_13d_iii_a_minted_holder_the_registry_has_no_row_for_refuses_by_name(_realm13, monkeypatch):
    """`cast.row(row["holder"])` is `None` for a person the cast built from a case the registry does
    not carry (`build_realm` builds persons from the CASES, and the per-case seating loop skips
    `r is None`). The minted pass read `.get("status")` off it unguarded, so such a holder raised
    `AttributeError` mid-build; it now raises the named `Unspecified`. The probe adds an NPC case no
    registry row names and a minted row held by it. CONTROL: every real minted holder has a row
    (`_realm13` builds). Mutation: turn the `holder_row is None` guard off (an `AttributeError`)."""
    from ..harness import populated

    real_cases = list(populated.load_cases("NPC"))
    ghost_case = dict(real_cases[0], id="NPC-997", name="Probe Holder")
    real_loader = populated.load_cases
    monkeypatch.setattr(populated, "load_cases",
                        lambda kind: real_cases + [ghost_case] if kind == "NPC" else real_loader(kind))
    real = populated.OFFICES_SEATS
    ghost = _ghost_of(real, _realm13._office_census["minted"][0], id="off_probe_unregistered",
                      holder="NPC-997", obligees=[])
    _populated_rows(monkeypatch, list(real) + [ghost])
    with pytest.raises(Unspecified) as red:
        build_realm(seed=0)
    assert "off_probe_unregistered" in str(red.value) and "no `npc_registry.yaml` row" in str(
        red.value), str(red.value)


def test_13d_iii_one_anchor_naming_two_rungs_is_refused_not_shadowed(_realm13):
    from ..harness.populated import _index_anchor

    w = _realm13
    anchors = dict(w._anchors)
    with pytest.raises(Forbidden):
        _index_anchor(w, anchors, True, "r_valoria")   # the realm's anchor, a second time


def test_13d_iii_a_titled_seat_must_stand_at_the_rung_kind_its_title_governs(_realm13):
    from ..harness.populated import seat_anchor

    w = _realm13
    duke_at_the_realm = {"id": "off_probe", "post": "Duke", "rung": {"realm": True}}
    with pytest.raises(Forbidden):
        seat_anchor(w, w._anchors, duke_at_the_realm)
    ok = seat_anchor(w, w._anchors, {**duke_at_the_realm, "rung": {"duchy": "Varfell"}})
    assert w.rungs[ok].kind == title_domain("Duke")


@pytest.mark.parametrize("kind", ["realm", "duchy", "territory"])
def test_13d_iii_a_resolver_broken_for_one_form_turns_the_realm_build_red(monkeypatch, kind):
    """MUTATION (`CLAUDE.md` §0.1 pt 2): the index forgets every rung of ONE kind -- the resolver
    for that form is broken -- and the realm must refuse to build, naming the kind. Run per form so
    the resolver cannot be kind-blind, and so a form that passes unbroken is shown to be the one
    doing the work. (The settlement form, which no row uses, is the test above's.)"""
    from ..harness import populated

    real = populated._index_anchor

    def broken(w, anchors, key, rid):
        if w.rungs[rid].kind == kind:
            return None
        return real(w, anchors, key, rid)

    monkeypatch.setattr(populated, "_index_anchor", broken)
    with pytest.raises(Unspecified) as e:
        build_realm(seed=0)
    assert f"{{{kind}:" in str(e.value), str(e.value)


def test_13d_iii_every_seat_the_realm_builds_has_a_rung_but_the_one_declared_exception(_realm13):
    """`H-163` limit 1 was *16 of 19 seats carry no rung*; measured at this position's start, 21 of
    the 24 the loop builds. Now every seat stands at its row's rung, `scope_rung` the same one (a
    bench's ground, `H-32`), save the seat the registry derives and no row authors: NPC-084's
    `guild leader`, which has no anchor and is given none."""
    w = _realm13
    cen = w._office_census
    assert cen["unauthored"] == ["off_npc_084"], cen["unauthored"]
    assert len(w.offices) == cen["seated"] == 30
    anchored = 0
    for oid, off in w.offices.items():
        if oid in cen["unauthored"]:
            assert off.rung is None and off.scope_rung is None, oid
            continue
        assert off.rung is not None and off.scope_rung == off.rung, (
            f"{oid} ({off.post!r}): rung {off.rung!r}, scope {off.scope_rung!r}")
        anchored += 1
    assert anchored == 29 == len(cen["authored"]), anchored


def test_13d_iii_the_six_rows_no_loop_seat_stands_for_are_minted_from_the_row_alone(_realm13):
    """The `[NEW]` seats: the King's second seat and five people the registry gives no seat. Each
    carries the row's own id, post, body, faction, bases and remit, and its holder sits in it under
    a live `hold` granting exactly that remit. (Four more `[NEW]`-marked holders -- NPC-007, 013,
    021, 070 -- are seated by the loop already, so they are overlaid and are NOT in this list.)"""
    w = _realm13
    rows = {r["id"]: r for r in _seat_rows()}
    minted = w._office_census["minted"]
    assert set(minted) == {"off_duke_valorsmark", "off_lord_steward", "off_cardinal_fortitude",
                           "off_cardinal_temperance", "off_senior_inquisitor",
                           "off_restoration_leader"}, minted
    checked = 0
    for rid in minted:
        row, off = rows[rid], w.offices[rid]
        assert (off.post, off.body, off.conferral, off.revocation) == (
            row["post"], row.get("body"), row["conferral"], row["revocation"]), rid
        assert off.remit_acts == sorted(row["remit_acts"]), (
            f"{rid}: a minted seat holds nothing before the overlay, so nothing is kept: {off.remit_acts}")
        holds = [t for t in w.tenures if t.kind == "hold" and t.object == rid and t.live]
        assert [t.subject for t in holds] == [f"p_{row['holder'].lower().replace('-', '_')}"], rid
        assert holds[0].granted_acts == tuple(off.remit_acts), rid
        checked += 1
    assert checked == 6


def test_13d_iii_an_authored_obligee_serves_the_seat_with_no_term(_realm13):
    """`offices.yaml`'s one non-empty `obligees` (`off_restoration_leader` -> NPC-041) is an `oblige`
    Tenure, so `establishment_of` -- the Query that replaced the `establishment` field -- answers
    it. No term: a seed has no opening act to declare one (`04 §B.8`'s `term?`, lawful null)."""
    w = _realm13
    withs = [r for r in _seat_rows() if r.get("obligees")]
    assert [r["id"] for r in withs] == ["off_restoration_leader"], withs
    assert world_q.establishment_of(w, "off_restoration_leader") == ["p_npc_041"]
    t = next(t for t in w.tenures if t.kind == "oblige" and t.object == "off_restoration_leader")
    assert t.term is None and t.live


def test_13d_iii_the_remit_overlay_replaces_the_default_and_leaves_only_the_unruled_act(_realm13):
    """The row's `remit_acts` IS a seat's remit, `[]` included: an authored empty list is NOT filled
    by `rosters.yaml: remit_default` (a testing fixture). The one thing a seat keeps beyond its row
    is an act `offices.yaml: meta: remit_unruled` names (`dispatch`, J-8) -- and only if it held it
    before. The unauthored seat is the control: with no row, the default still fills."""
    from ..data.rosters import OFFICES_REMIT_UNRULED, REMIT_DEFAULT

    w = _realm13
    assert OFFICES_REMIT_UNRULED, "the unruled set is empty: the overlay below would strip J-8's act"
    cen = w._office_census
    empty_rows = checked = 0
    for row in _seat_rows():
        off = w.offices[cen["authored"][row["id"]]]
        have, authored = set(off.remit_acts), set(row["remit_acts"])
        assert authored <= have, f"{row['id']}: authored {sorted(authored)} not all granted {sorted(have)}"
        assert have - authored <= OFFICES_REMIT_UNRULED, (
            f"{row['id']} holds {sorted(have - authored)} beyond its row: the testing default leaked "
            "past the overlay")
        if not authored:
            empty_rows += 1
        checked += 1
    assert checked == 29 and empty_rows >= 1, (checked, empty_rows)
    assert set(w.offices["off_npc_084"].remit_acts) == set(REMIT_DEFAULT), (
        "the seat no row authors lost the testing default -- the fill path the overlay replaces "
        "only where a row exists")


@pytest.fixture(scope="module")
def _season13():
    from ..decision import make_chooser
    from ..harness.corpus_run import attribute
    from ..state.ids import H, draw_factory

    w = build_realm(seed=0)
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick))
    d.season(ch, question=None, subsistence=P.SUBSIST,
             contest_max_depth=w.fixtures.get("contest_max_depth"))
    return w, attribute(w, d, 1)


def test_13d_iii_a_season_executes_an_issue_or_levy_through_a_seat_with_a_rung(_season13):
    """U9's own acceptance text, on the shipped realm at seed 0: a `levy` or `issue` EXECUTES with
    `Act.via` set, naming a seat whose rung gave it the purview. Before this position the same seed
    refused 18 of 19 four-season levies on `authority` (`aperture 4 0` on the parent tree
    `5519cf52`; `H-163` limit 1) and executed none. The seat check is the
    point: an act whose `via` names a rungless seat would have refused, so this also shows `via`
    and the rung are one fact. (`levy` itself still mostly refuses as `levy.refused` -- the `stores`/
    `write` conjuncts, `H-163` limit 3 -- which is not this position's to lift.)"""
    w, att = _season13
    executed = [a for a, made, _ in att if a.verb in ("levy", "issue") and made]
    assert executed, "no levy or issue executed in a season: the cap `13d-iii` lifts is still on"
    for a in executed:
        assert a.via in w.offices, f"{a.verb} by {a.actor} executed with via={a.via!r}"
        assert w.offices[a.via].rung is not None, (a.verb, a.via)
    levies = [(a, refused) for a, _, refused in att if a.verb == "levy"]
    assert levies, "no levy was attempted -- the share below would be vacuous"
    unauthorized = sum("levy.unauthorized" in refused for _, refused in levies)
    assert unauthorized < len(levies), (
        f"{unauthorized} of {len(levies)} levies refused on `authority`: every seat that levies is "
        "still outside its purview")


# =================================================================================================
# PLAN POSITION `24d-i` -- THE DWELLING SUBSTRATE (`ED-SE-0055`).
# `workplans/2026-09-18-governance-settlement-behaviour-plan_part2.md`, position `24d-i`. `dwelling`
# joins `site_kinds` with the two rows the loader forces, both at the CONTROL arm
# (`wear_per_season.dwelling: 0`, `band_floors.dwelling: {}`), and `build_realm` mints one dwelling
# Site per `hearth` rung. FALSIFIERS: exactly one dwelling on every hearth and none elsewhere, with
# a hearth floor so an empty world cannot pass; the loader's refusal, planted; and the control arm
# over one populated season, with no dwelling band crossing while the wear loop visited every one.
#
# ⚠ WHICH OTHER HEARTH BUILDERS MINT, AND WHY. The ruling names `build_realm` only; the rest is
# this position's architecture call (`CLAUDE.md` §0, step 5).
#   * `governance_spine.build` MINTS. The spine is the template the realm is fine-tuned FROM, and
#     `19c`'s `migrate` runs its observable on the spine's two disjoint chains. With a dwelling per
#     hearth, `capacity` counts 2 at the realm and 1 down each chain. Without, every rung reads the
#     floor. Cost: two Sites on a world no test runs a season on today.
#   * `corpus_run.build_at` DOES NOT. Every corpus world is ONE chain wide. Measured over every
#     buildable case, a corpus world has 0 or 1 hearth, so a dwelling there would be counted by
#     every rung of the chain alike, and `capacity` would still be one number per world. Minting
#     would buy no variation for `R-05` to score. It would still add a wear Event, co-located with
#     all three persons, to every hearth-scaled world.
#   * `probes.tiny_world` DOES NOT. It isolates mechanisms. A dwelling at `Hh` would sit with three
#     of its five persons and hand each a witnessed wear claim every season, in every probe and
#     every test built on it. It would also trip probe `F10`'s assert that `Hh` carries no Site;
#     that assert guards against PRODUCTION and would fire on a dwelling that produces nothing. A
#     probe that needs a dwelling plants one, as `site_odd` is planted.
#   * `headless.build_world` DOES NOT. The spec's list omits this fourth builder (`hearth_ostvik`).
#     It is Carin's single worked case and `m1_acceptance`'s probe world. A dwelling there would
#     add a wear claim to Carin's and the bailiff's ledgers, and nothing in either world reads
#     housing.
# =================================================================================================

def _dwellings(w):
    return [s for s in w.sites.values() if s.kind == "dwelling"]


def _hearths(w):
    return sorted(rid for rid, r in w.rungs.items() if r.kind == "hearth")


def _spine():
    from ..harness import governance_spine
    return governance_spine.build(0)


@pytest.mark.parametrize("build", [lambda: build_realm(0), _spine], ids=["build_realm", "spine"])
def test_24d_i_every_hearth_carries_exactly_one_dwelling_and_no_other_rung_carries_any(build):
    """FALSIFIER (a), on both builders that mint. Exactly one per hearth and none elsewhere is ONE
    comparison: the dwellings counted per rung must equal each hearth counted once. A dwelling on
    a settlement, a hearth with two, or a hearth with none all fail it."""
    w = build()
    hearths = _hearths(w)
    assert len(hearths) >= 1, "the world builds no hearth; everything below would pass vacuously"
    dw = _dwellings(w)
    per_rung = Counter(s.rung for s in dw)
    assert per_rung == Counter(hearths), (
        f"dwellings per rung != one per hearth. Off-hearth (first 10): "
        f"{sorted(set(per_rung) - set(hearths))[:10]}; hearths without exactly one (first 10): "
        f"{sorted(h for h in hearths if per_rung[h] != 1)[:10]}")
    scale = w.fixtures.get("condition_scale")
    checked = 0
    for s in dw:
        assert s.condition == scale, (
            f"{s.id} starts at {s.condition}, not at `condition_scale`, which is how the producing "
            "Sites are built")
        checked += 1
    assert checked == len(hearths) >= 1, checked


def test_24d_i_the_realm_mint_adds_sites_and_displaces_no_producing_site():
    """The OBSERVABLE's census, derived rather than pinned. The producing Sites are still one per
    producing kind per settlement, and the total is those plus one per hearth, plus one garrison
    per settlement (M4, `ED-IN-0279` clause (a), build step 11 -- joined the same non-producing
    shape `dwelling` already has: one per unit, `SITE_YIELD` never keys it, `wear_per_season`/
    `band_floors` both ship it a control-arm `0`/`{}}`). A dwelling or garrison id that collided
    with a producing Site's would overwrite it, and the first count would drop."""
    from ..data.fixtures import SITE_YIELD
    w = build_realm(0)
    settlements = [r for r in w.rungs.values() if r.kind == "settlement"]
    producing = [k for k in sorted(SITE_YIELD) if SITE_YIELD[k]]
    assert settlements and producing, "fixture: no settlement or no producing kind"
    others = Counter(s.kind for s in w.sites.values() if s.kind not in ("dwelling", "garrison"))
    assert others == Counter({k: len(settlements) for k in producing}), others
    garrisons = [s for s in w.sites.values() if s.kind == "garrison"]
    assert len(garrisons) == len(settlements), (
        f"{len(garrisons)} garrison Sites for {len(settlements)} settlements -- not one each")
    assert len(w.sites) == (len(settlements) * len(producing) + len(_hearths(w))
                             + len(settlements)), len(w.sites)
    assert not [s.id for s in w.sites.values() if s.id in w.rungs], "a Site id shadows a rung id"


def test_24d_i_the_loader_refuses_dwelling_without_its_wear_or_floor_row(monkeypatch):
    """FALSIFIER (b), the loader's own refusal, planted and reverted by `monkeypatch`. The
    `dwelling` key is deleted from the loaded table the loader reads, and `_load_matter_tables`
    must raise `Ungraded` NAMING `dwelling`. That is the refusal for a kind with no row, and not
    some other failure. The unplanted arm must load, with the control-arm values."""
    from ..data import rosters as _R
    from ..data.fixtures import DEFAULT_FIXTURES, _load_matter_tables
    from ..gaps import Ungraded

    rates, floors, _w, _y = _load_matter_tables()
    assert rates["dwelling"] == 0 and floors["dwelling"] == {}, (rates, floors)
    assert DEFAULT_FIXTURES.wear("dwelling") == 0

    checked = 0
    for table, cell in (("wear_per_season", _R._ROSTERS["wear_per_season"]["rates"]),
                        ("band_floors", _R._TABLES["band_floors"]["cells"])):
        with monkeypatch.context() as m:
            m.delitem(cell, "dwelling")
            with pytest.raises(Ungraded) as got:
                _load_matter_tables()
            assert table in str(got.value) and "dwelling" in str(got.value), str(got.value)
        assert "dwelling" in cell, f"the plant on {table} was not reverted"
        checked += 1
    assert checked == 2, checked


def test_24d_i_dwelling_wear_stops_being_inert_at_11a(monkeypatch):
    """FALSIFIER (c) -- AND `24d-i`'s `DONE·INERT` MEASUREMENT DOES NOT SURVIVE POSITION `11a`,
    WHICH IS RECORDED HERE RATHER THAN HIDDEN. The name and the back half of this test changed;
    the front half -- what `24d-i` actually built -- did not.

    HISTORY, KEPT FOR THE RECORD. `24d-i` measured TREATMENT (`build_realm(0)`) against CONTROL
    (the same world, dwellings deleted before the season) as byte-identical except for the
    dwellings' own wear: build hash `fa6ea34ceeb85cb2d64f3d6bbf0fefc5`, one-season hash
    `65823840d82e1051cfaab49ce3e6f432`, both matching the pre-`24d-i` checkout (`bcc9a1f`) exactly.
    That identity is what `DONE·INERT` meant, and it held because NOTHING could turn a dwelling's
    `condition.worn` claim into a Question: `band_crossed` (Q3) never carried a site id (`H-110`),
    and Q2's admission test read only `c.subject == p.id or c.subject in mine`, which a dwelling id
    is neither.

    WHAT `11a` CHANGES, AND WHY THE OLD COMPARISON CANNOT SURVIVE IT. `reach`/`place_of`
    (`queries/world_q.py`) give Q2 a PLACE clause: a claim is now also admitted when
    `place_of(c.subject) in reach(w, p)`. A dwelling sits AT a hearth, and a resident's own home
    RUNG (`home_of`) is that hearth -- limb 3 of `reach` starts there -- so every resident's own
    dwelling wear claim is now `place_of(dwelling) == hearth == home_of(resident) ∈ R`: ADMITTED.
    That is not a dwelling-specific channel; it is `01_ATTENTION_AND_REACH.md` §0.2(d)'s own
    headline (561 → 1632 questions on `build_realm(0)`) landing on a concrete case this suite
    already built a control arm for. MEASURED, same seed, one season: 132 of 3,710 questions now
    name a dwelling; the treatment and control Question-id sets no longer overlap enough to compare
    ("same Questions by id" -- FALSE); the resolved act COUNT differs (387 vs 378) and so does the
    act-subject distribution; 230 control claims are gone from the treatment arm and 570 are added
    (not a small, dwelling-shaped diff — `24d-i`'s old `added`/`control <= claims` bookkeeping no
    longer describes a coherent set). `24d-i`'s own claim-displacement note already said dwellings
    are "NOT SILENT" past season one; `11a` is what makes season ONE say so too.

    ⚠ THIS IS THE DESIGN'S OWN INTENDED CONSEQUENCE, NOT A REGRESSION `11a` INTRODUCED BY ACCIDENT
    (`CLAUDE.md` §0's five-step gate, step 3): `01`'s own headline number is exactly this effect,
    general rather than dwelling-specific, and the position's OBSERVABLE section declares a golden
    re-record necessary on exactly this ground. What THIS test polices from here is narrower and
    still true: the wear mechanism itself (visits every dwelling once, crosses no band, moves no
    condition) is UNCHANGED, and the new dwelling questions are the ORDINARY `claim_landed` shape,
    sourced from a real resident's real ledger claim about their own hearth's dwelling -- not a
    new channel, a new referent kind, or a broadcast."""
    from ..harness import populated
    from ..loop import driver

    def season(strip):
        w = build_realm(0)
        if strip:
            for s in _dwellings(w):
                del w.sites[s.id]
        dw = {s.id: s.rung for s in _dwellings(w)}
        qs = []
        inner = driver.questions_for

        def spy(w_, p, since=None):
            out = inner(w_, p, since)
            qs.extend(out)
            return out
        with monkeypatch.context() as m:
            # ⚠ MERGE, 2026-09-27 (ED-IN-0206, main): the reader moved from `loop.deliberate` back
            # to `loop.driver` -- the driver now builds the per-person question projection at
            # barrier 2 (`SeasonDriver._questions_at_barrier`) rather than `deliberate` calling
            # `questions_for` itself. The spy must name the module the reader actually lives in
            # (the same lesson `wd_extra.py`'s own history records), or it patches a name nothing
            # reads and the counts below come back silently empty.
            m.setattr(driver, "questions_for", spy)
            out = populated.run(seasons=1, w=w)
        return w, dw, qs, out

    w, dw, qs, out = season(strip=False)
    scale = w.fixtures.get("condition_scale")
    assert len(dw) >= 1, "no dwelling was built; the zeros below would describe nothing"
    assert qs, "the questions_for spy saw no deliberation; the zero below would be unobserved"
    worn = Counter(anchor_of(w, e) for e in w.log
                   if e.kind == "condition.worn" and anchor_of(w, e) in dw)
    assert worn == Counter(list(dw)), (
        f"the wear loop did not visit every dwelling exactly once: "
        f"{len(worn)} of {len(dw)} worn, {sum(worn.values())} Events")
    # `band_crossed` is no longer a question source at all (position `11a` folded it into
    # `claim_landed`, and `w.crossings` is deleted with it -- `AX-4`, one owner). This premise
    # survives the fold unchanged, because it was never about the deleted source's SHAPE: a
    # dwelling's `wear_per_season` is 0 and its `band_floors` are `{}` (`24d-i`), so its condition
    # never moves and `_crossings` never fires for one AT ALL -- direct evidence off the Event log.
    assert not [e for e in w.log if e.kind == "condition.band_crossed" and anchor_of(w, e) in dw]
    assert all(w.sites[sid].condition == scale for sid in dw), "a dwelling's condition moved at wear 0"

    # ⚠ THE ASSERTION THIS REPLACES USED TO BE `assert not [...]` -- "no question names a
    # dwelling". `11a` makes that FALSE by design (see the docstring); what is asserted now is
    # that dwelling questions, where they exist, are the ORDINARY shape: `claim_landed`, and each
    # one resolves to a real claim in ITS OWN ASKEE's ledger whose subject is a dwelling that
    # askee actually lives beside.
    dwelling_qs = [q for q in qs if {q.about, *q.referents} & set(dw)]
    assert dwelling_qs, (
        "no question named a dwelling -- if that is now true, `reach`/`place_of`'s place clause "
        "regressed, or this world no longer witnesses a dwelling's own wear co-located")
    assert {q.source for q in dwelling_qs} == {"claim_landed"}, (
        f"a dwelling question came from a source other than claim_landed: "
        f"{sorted({q.source for q in dwelling_qs})}")
    at = {rung: sid for sid, rung in dw.items()}
    home = world_q.home_of(w)
    by_id = {c.id: c for p in w.persons.values() for c in p.ledger}
    for p in w.persons.values():
        for q in dwelling_qs:
            if q.id not in {f"q:claim:{c.id}" for c in p.ledger}:
                continue
            c = by_id.get(q.about)
            assert c is not None and c.subject == at.get(home.get(p.id)), (
                f"{q.id} for {p.id} does not resolve to that person's own hearth's dwelling: {c}")

    # ⚠ `24d-i`'s TREATMENT == CONTROL IDENTITY DOES NOT SURVIVE `11a`, AND IS NOT RE-ASSERTED.
    # What is asserted instead is the honest negation, so a future change that silently restores
    # dwelling-inertness (narrowing `reach` back down, or breaking the co-located witness) is
    # caught here rather than read as a quiet improvement.
    cw, cdw, cqs, cout = season(strip=True)
    assert cdw == {}, "the control still has dwellings"
    assert sorted(q.id for q in qs) != sorted(q.id for q in cqs), (
        "the two arms' Question sets are identical again -- dwellings are DONE·INERT once more; "
        "either relabel this test back to `24d-i`'s or find what silently narrowed `reach`")
    assert out["acts"] != cout["acts"], (
        f"both arms resolved {out['acts']} acts -- dwellings no longer move the act count, which "
        "is the same regression the Question-id check above would also have caught")
# H2 -- `ED-IN-0261`'s DEONTOLOGICAL GATE, `H-146`. A refusal at `opening_set`, not a score term:
# the person's projected weight on the gating axis IS the threshold, and a verb that axis engages
# past it never forms a Candidate. Roster-generic: the axis is whatever `Fixtures refusal_axis`
# names, so these tests take a rostered axis by position and name none.
#
# Falsifier (`proposals/2026-09-26-decision-layer-execution-plan/PROPOSAL.md` §3.2): a synthetic
# projection/alignment injected through the rebinds the readers actually resolve --
# `data.verbs.ALIGNMENT` (the `H-66` sweep's own, `alignment_at`) and
# `data.verbs.PURSUIT_PROJECTION` (read bare by `data.pursuits.to_axes`) -- must stop the refused
# Candidate forming and leave every survivor's score untouched.
# =================================================================================================


def _h2_setup():
    from ..state.carriers import Question
    w = P.tiny_world()
    p = w.persons["p_mid"]
    q = Question("q:h2", "need", ("rec_writ",))
    v = View(p.id, [], w.fixtures.get("view_k"), q)
    return w, p, q, v


def _h2_base(min_verbs=3):
    """`_h2_setup` plus the option set it forms today, ungated -- shared by every `test_h2_*` so a
    change to `opening_set`'s call shape or the minimum-verb guard is edited once, not per test."""
    from ..decision import options as _options
    w, p, q, v = _h2_setup()
    base = {(c.verb, c.subject) for c in _options.opening_set(p, v, q, w.fixtures)}
    verbs = sorted({vb for vb, _ in base})
    assert len(verbs) >= min_verbs, (
        f"only {verbs} form here; the H-146 gate tests need >= {min_verbs}")
    return w, p, q, v, base, verbs


def _h2_inject(p, axis, weight, cells):
    """Rebind the projection and the alignment to synthetic tables; return a restore callable."""
    from ..data import verbs as _verbs
    saved = (_verbs.PURSUIT_PROJECTION, _verbs.ALIGNMENT, dict(p.pursuits))
    _verbs.PURSUIT_PROJECTION = {"h2_synthetic": {axis: weight}}
    _verbs.ALIGNMENT = {axis: dict(cells)}
    p.pursuits = {"h2_synthetic": 1.0}

    def restore():
        _verbs.PURSUIT_PROJECTION, _verbs.ALIGNMENT, p.pursuits = saved
    return restore


def test_h2_the_shipped_arm_is_the_control_and_refuses_nothing():
    """`refusal_axis` ships unset, and unset is a no-op: the same synthetic tables that make the
    gate refuse below form the full set here. Without this arm the refusal test cannot tell the
    gate from some other change to `opening_set`."""
    from ..data.fixtures import DEFAULT_FIXTURES
    from ..data.rosters import PURSUIT_AXES
    from ..decision import options as _options
    assert DEFAULT_FIXTURES.get("refusal_axis") is None, (
        "the shipped arm is no longer the control; `H-146` and this test disagree")

    w, p, q, v, base, verbs = _h2_base()
    restore = _h2_inject(p, sorted(PURSUIT_AXES)[0], -0.4, {vb: 0.9 for vb in verbs})
    try:
        got = {(c.verb, c.subject) for c in _options.opening_set(p, v, q, w.fixtures)}
    finally:
        restore()
    assert got == base, f"the unset gate changed the option set: {sorted(base ^ got)}"


def test_h2_a_verb_past_the_persons_weight_never_forms():
    """THE FALSIFIER. Person weight `-0.4` on the axis (the NEG, refusing pole). Three engaged
    verbs: `+0.3` and `-0.2` sit past `-0.4` toward the POS pole and are refused; `-0.6` does not
    and survives. Every verb the axis does not engage survives -- only *certain actions* gate."""
    from ..data.rosters import PURSUIT_AXES
    from ..decision import options as _options

    w, p, q, v, base, verbs = _h2_base()
    refused_pos, refused_neg, tolerated = verbs[0], verbs[1], verbs[2]
    axis = sorted(PURSUIT_AXES)[-1]
    fx = w.fixtures.sweep("refusal_axis", axis)
    restore = _h2_inject(p, axis, -0.4,
                         {refused_pos: 0.3, refused_neg: -0.2, tolerated: -0.6})
    try:
        got = {(c.verb, c.subject) for c in _options.opening_set(p, v, q, fx)}
    finally:
        restore()

    formed = {vb for vb, _ in got}
    assert refused_pos not in formed and refused_neg not in formed, (
        f"a verb whose `{axis}` cell exceeds the person's weight still formed: {sorted(formed)}")
    assert tolerated in formed, f"{tolerated!r} sits below the weight and was refused anyway"
    expected = {(vb, s) for vb, s in base if vb not in (refused_pos, refused_neg)}
    assert got == expected, (
        f"the gate moved candidates it does not govern: {sorted(expected ^ got)}")


def test_h2_survivors_score_exactly_as_they_did_ungated():
    """The gate filters and never re-weights: every Candidate that survives it reaches the score
    with the value it had with the gate unset. Observed through `_sample_order`, the one place
    `make_chooser` hands the scores on, so this reads the chooser's own numbers."""
    from ..data.rosters import PURSUIT_AXES
    from ..decision import choose as _choose
    from ..decision import options as _options
    from ..state.carriers import Sensation

    w, p, q, v, base, verbs = _h2_base()
    refused, tolerated = verbs[0], verbs[1]
    axis = sorted(PURSUIT_AXES)[0]
    fx0 = w.fixtures.sweep("choice_temperature", 0)

    def scores(fx):
        seen = {}
        inner = _choose._sample_order

        def spy(ranked, score, person, fx_, draw):
            seen.update({(c.verb, c.subject): score(c) for c in ranked})
            return inner(ranked, score, person, fx_, draw)
        _choose._sample_order = spy
        try:
            _choose.make_chooser(fx, lambda a, b, c: f"{a}:{b}:{c}")(
                p, v, Sensation(0), lambda: 1)
        finally:
            _choose._sample_order = inner
        return seen

    restore = _h2_inject(p, axis, -0.4, {refused: 0.5, tolerated: -0.9})
    try:
        ungated = scores(fx0)
        gated = scores(fx0.sweep("refusal_axis", axis))
    finally:
        restore()
    assert ungated and any(vb == refused for vb, _ in ungated), (
        "the ungated arm scored nothing, or never scored the verb the gate should refuse")
    assert not any(vb == refused for vb, _ in gated), f"{refused!r} reached the score gated"
    assert set(gated) == {k for k in ungated if k[0] != refused}
    moved = {k: (ungated[k], gated[k]) for k in gated if gated[k] != ungated[k]}
    assert not moved, f"the gate changed survivors' scores: {moved}"
    assert any(ungated[k] for k in gated), "every survivor scored 0; unchanged proves nothing"


def test_h2_an_unrostered_axis_refuses_rather_than_gating_on_nothing():
    """A name off `pursuit_axes` must raise `Unspecified`, not silently answer. (Without
    `require_member` this would raise a bare `KeyError` inside `to_axes` instead -- still a raise,
    just an unnamed one -- so this test also pins that the failure is the NAMED hole, not any
    exception.)"""
    from ..decision import options as _options
    from ..gaps import Unspecified

    w, p, q, v = _h2_setup()
    with pytest.raises(Unspecified):
        _options.opening_set(p, v, q, w.fixtures.sweep("refusal_axis", "h2_not_an_axis"))
