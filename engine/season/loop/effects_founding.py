"""`season.loop.effects_founding` -- minting works: found, build; and their closer, raze.

EXTRACTED from `effects.py` at the per-subsystem split (Phase 4). Holds the pair that grows the
world rather than only wearing it down (`ARCH` F.20): `found` mints a Rung of whatever kind a works
plans, `build` mints a Site at condition 0. `_works_named` (what a works names, plans and is placed
at) and `_made_by` (the one id scheme so one works makes one thing) are this pair's own reading of
their operand and stay local -- nothing outside `found`/`build` calls either; so does `_cost` (v9
IN-28, `H-166`: what a plan costs the works' rung, `rosters.yaml: works_cost`). See `effects_shared.py`
for `effect_for`, `_operand` and the shared §10-ladder refusal `_decline_ascent`. v9 IN-12 step 11
adds `raze`, the closer of `H-166` limit 3: the one verb that ends a Rung (`w.rungs` shrinks).
"""

from __future__ import annotations

from ..data.rosters import RAZE_TARGET_KINDS, RUNG_KINDS, SITE_KINDS
from ..queries.world_q import mustered, works_target
from ..state.carriers import Rung, Site, Tenure
from ..state.gate import NO_CHANGE, Change, Subject
from ..state.ids import H
from ..state.world import rung_kind_ascends
from ..trace_log import TRACE

from .effects_shared import _debit, _decline_ascent, _operand, _shift, effect_for, occupying_faction


def _works_named(w: "World", a: "Act") -> tuple:
    """`(works, plan, rung)` -- the works the act names (its `subject`), what it plans, and the RUNG
    it plans it at -- or `(None, None, None)` if the subject is no works, or its `at` names no rung.
    `found`'s and `build`'s one reading of their operand: each then asks whether the plan is a kind
    IT makes. The precondition has already asked that the works exists and that the actor holds it
    (`verb_table.yaml`'s typed cells); this reads what the works SAYS, which no cell can.

    ⚠ THE MADE THING'S ID IS DERIVED FROM THE WORKS, NOT FROM THE TARGET (`_made_by`), so ONE works
    makes ONE thing: a second `found`/`build` from the same works finds its id taken and declines.
    r2's `f"{at}:{plan}"` is not taken -- it would collide across two successive works for one
    target (a second dwelling at one hearth, after the first works ended) and refuse the second as
    already made."""
    rec = w.records.get(_operand(a, "subject"))
    plan, at = works_target(rec.kind, rec.subject_matter) if rec is not None else (None, None)
    if plan is None or at not in w.rungs:
        return (None, None, None)
    return (rec, plan, w.rungs[at])


def _made_by(rec, plan: str) -> str:
    """The id of what the works `rec` makes -- `<plan>:<works id>`, readable in a trace as *the
    hearth of works rec:…*, and one owner for `found` and `build` (see `_works_named`)."""
    return f"{plan}:{rec.id}"


def _cost(w: "World", rec, plan: str):
    """v9 IN-28 (`H-166` limit 1) -- `(the rung that pays, {matter kind: amount})` for a works of
    `plan`, or `None` with the reason TRACEd when it cannot be paid. `found`'s and `build`'s one
    reading of the price, so the two verbs cannot come to disagree about what a plan costs.

    THE PAYER IS THE WORKS' RUNG, `Record.rung` -- where the works is kept, and where a `transfer`
    delivers matter to it (r2 `04` §A.6.6, intent: *"the cost is paid by `transfer` into the works'
    rung"*). Not the actor's own hearth: whoever gathers matter at the works pays for it, which is
    what lets several hands stock one works. THE PRICE is `rosters.yaml: works_cost`, read through
    the fixture so `H-166`'s sweep reaches it.

    DECLINES, each a refusal that emits (`found.refused` / `build.refused`), never a free place:
      * the plan has NO PRICE (no `works_cost` row -- `body`, `person`, `settlement` and above:
        the roster's note says why each); a missing row is not a cost of zero;
      * the works' rung is no rung;
      * the rung cannot meet every kind of the price -- r2 §A.6.6's MATTER-STALL, *"a scaffolding
        standing empty"*, refused at the act that would have raised it.
    ⚠ NOT A TYPED CELL: the threshold is `works_cost[plan]` read off the works' CONTENT and the
    store is the works' RUNG, neither of which a `requires_forms` stem reaches from `subject`; so it
    is the effect's decline, as strict ascent is (`_eff_move`'s precedent)."""
    price = (w.fixtures.get("works_cost") or {}).get(plan)
    payer = w.rungs.get(rec.rung)
    why = None
    if not price:
        why = f"no `works_cost` row prices a {plan!r}, so nobody can pay for one"
    elif payer is None:
        why = f"the works' rung {rec.rung!r} is no rung, so nothing can pay its price"
    else:
        short = {k: n for k, n in sorted(price.items()) if (payer.stores or {}).get(k, 0) < n}
        if short:
            why = (f"{payer.id!r} holds {dict(sorted((payer.stores or {}).items()))} and the "
                   f"{plan} costs {dict(sorted(price.items()))}: short of {short}")
    if why is not None:
        TRACE.decision(f"{rec.id} cannot pay: {why}", "H-166",
                       chose="change nothing, so the fold emits the refusal",
                       alternatives=["raise the place for free (H-166: paid for by nobody)",
                                     "raise it and leave the store negative (matter from nowhere)"])
        return None
    return payer, dict(price)


@effect_for("found")
def _eff_found(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """PLAN POSITION `24e` -- A WORKS IS FOUNDED: a Rung of the works' `plan` kind is minted and
    placed in the rung its `at` names by a `contain` edge through `World.add_tenure`, the one
    writer, which enforces strict ascent. `ARCH` F.20 -- *"the world only decays -- nothing is ever
    founded or built"* -- is this effect's reason to exist, and `(Rung, exists)` its first producer
    (`H-41`'s first cell).

    WHAT IT MAKES, each choice with the reading it rejects:
      * A RUNG OF WHATEVER KIND THE WORKS PLANS, not a `hearth` written here. The plan's `24e`
        speaks of *"minting a `hearth` Rung"*, which is its example: a kind in a body is a
        definition the roster owns (`test_jordan_no_definition_is_hardcoded_in_a_body`), and strict
        ascent -- not a literal -- is what decides which kinds may be founded under which. A hearth
        under a settlement, a community under a territory; never a duchy under a hearth.
      * ITS PARENT IS THE WORKS' `at`, the one rung id the works carries. The act carries only its
        `subject` (the works) -- a person-side act can name no second rung (`H-94`), and `at` is
        not and must not become a `requires_operands` member (r2 `02`: *"I do not coin a ninth
        operand"*); `15c`'s reader left `found` exactly this place to read it from.
      * NO SITES: a founded hearth has no dwelling until one is BUILT (`build`, plan `24e`: *"A
        founded hearth has no dwelling until one is BUILT"*).
      * PAID FOR (v9 IN-28, `H-166` limit 1): the plan's `works_cost` STAKE moves two-sided out of
        the works' rung INTO the new Rung (`_cost`, `_shift`), so the place starts with what was
        staked on it and no matter leaves the world. A works whose rung cannot pay is refused.
      * HELD BY ITS FOUNDER (v9 IN-28, `H-166` limit 2): the actor's `hold` on the new Rung, opened
        in the same write. ⚠ This read *"no `hold` is minted on it -- a `hold` written here would be
        a claim of ownership nobody made"*. The founding IS the claim: CLAUDE.md §0's ladder step 4,
        the maker's-hold precedent `create_record` and `utter` both carry. The holder is the person
        who acted, never a seat: a seat whose rung contains `at` already reaches the new Rung through
        purview, and minting a seat's `hold` would be a grant (`conferral`) nobody conferred.
        [ASSUMPTION; medium; Jordan to correct; revert: delete `held`, and `H-166` limit 2 reopens].
      * NO CAPACITY REFUSAL (the plan's CORRECTION of 2026-09-25, verbatim in substance): `found`
        and `build` are how capacity GROWS, and refusing a `found` at a rung at capacity would
        deadlock -- a full rung could never add the housing that raises its own ceiling. `found`
        keeps only its own preconditions (well-formed operands, the maker's standing, strict
        ascent). The refusal for a full rung is `19c`'s `migrate`'s.

    DECLINES (`NO_CHANGE` -> `found.refused`), each a clause the grammar cannot spell: the subject is
    no works or its `at` is no rung (`_works_named`); the plan is not a `rung_kinds` member (a works
    to build a Site is `build`'s); the works has already founded (`_made_by`'s id is taken); and the
    plan does not strictly ascend into `at` -- declined HERE, on `_eff_move`'s precedent, because
    `add_tenure` RAISES on it and a person attempting a founding the ladder will not seat is a
    refusal, not a crash. The rule is not re-implemented: `rung_kind_ascends` is the one owner
    `World.contain_ascends` reads too.

    G3 -- THE EDGE IS NOBODY'S, AND ITS BASIS IS `founding` (`state/gate.py`, the NINTH): a `contain`
    whose subject is a Rung is in no person's store (S15.1), so `T-m` cannot admit it; the gate
    admits it because the SAME write brought its subject into existence and it is that subject's only
    parent -- the mirror of `cascade`. Without it the gate raises `NotYours` and puts the edge back.

    G4 -- WHAT IT NAMES: THE RUNG, whole, earning `rung.founded` -- it always moves (absent ->
    present). The `contain` edge rides on the Rung's receipt as `create_record`'s maker's `hold`
    rides on the Record's (r2 §A.7.1: *"the `contain` edge rides inside `(Rung, exists)`"*), F3
    still judges it, and a refused write puts it back. The row declares `Tenure.since` beside
    `Rung.exists` all the same (`establish`'s `Tenure.payload` precedent: the fold gates exactly the
    pairs a verb declares), so the edge's pair is checked for class, step and partition."""
    rec, plan, parent = _works_named(w, a)
    if rec is None or plan not in RUNG_KINDS:
        return NO_CHANGE
    rid = _made_by(rec, plan)
    if rid in w.rungs:
        return NO_CHANGE
    if not rung_kind_ascends(plan, parent.kind):
        return _decline_ascent(
            f"a founding does not ascend the §10 ladder -> a {plan} under the "
            f"{parent.kind} {parent.id!r}")
    paid = _cost(w, rec, plan)
    if paid is None:
        return NO_CHANGE
    payer, price = paid
    rung = Rung(rid, plan)
    placed = Tenure(H(w.world_seed, w.tick, rid, f"contain:{parent.id}:{a.id}"), rid, parent.id,
                    "contain", since=w.tick)
    # THE FOUNDER'S `hold` (v9 IN-28, `H-166` limit 2): the maker's-hold shape `create_record` and
    # `utter` already open (`effects_information.py::_makers_hold`, S13: *"the maker holds what
    # they made until they part with it"*), with that helper's id scheme. ⚠ CONSTRUCTED HERE, NOT
    # CALLED: `data/verbs.py::_derive_openers_from_effects` reads a `hold` opener off a `Tenure(...)`
    # literal; since v9 B-M it also follows a helper imported from a sibling effects file, so a call
    # would now keep `found` in `hold`'s openers. The literal stays: it costs nothing.
    held = Tenure(H(w.world_seed, w.tick, a.actor, f"hold:{rid}"), a.actor, rid, "hold",
                  since=w.tick)

    def perform() -> None:
        w.rungs[rid] = rung
        w.add_tenure(placed)
        w.add_tenure(held)
        for kind, amount in sorted(price.items()):
            _shift(payer, rung, kind, amount)
    # The PAYER is named so the gate reads its store either side (G4): a stake that did not leave it
    # is a write that did not happen. It earns the row's one kind, as both sides of a `transfer` do.
    return Change((Subject.entity("rungs", rid, "rung.founded"),
                   Subject.entity("rungs", payer.id, "rung.founded")), perform)


@effect_for("build")
def _eff_build(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """PLAN POSITION `24e` -- A WORKS IS BUILT: a Site of the works' `plan` kind (a `site_kinds`
    member) stands at the rung its `at` names, AT CONDITION 0. `(Site, exists)`'s first producer
    (`H-41`'s third cell) and the other half of `ARCH` F.20: *"nothing is ever founded OR BUILT"*.
    The plan's `24e`: *"A founded hearth has no dwelling until one is BUILT ... at runtime a
    dwelling exists because someone built it, which is what makes `found`/`build` the throttle"*.

    ⚠ AT CONDITION 0, AND THAT IS r2 `04` §A.7.1's DECISION, NOT A DEFAULT: *"a fabric that appeared
    at full condition would make `restore` pointless and would be a built thing nobody built.
    Condition 0 with a rising ceiling is 'raising the first courses'"*. So `build` stakes the
    fabric and `restore`/`work` raise it, as far as the SAME works' ripened terms allow -- the works
    names every `<plan>` at `<at>` (`queries/world_q.py::works_for`), so the Site it builds is the
    Site its `ceiling` bounds, with no second matching rule. A Site's yield scales with its
    condition (`loop/matter.py`), so a new producer produces nothing until it is raised.

    NO CAPACITY REFUSAL: building a dwelling at a full rung is how the rung's capacity grows (the
    plan's correction of 2026-09-25; `found`'s docstring). And NO EDGE: `Site.rung` is a field of the
    Site (S12), written in the same construction -- there is no Tenure to judge, so no gate basis is
    asked beyond the matrix row's own.

    PAID FOR (v9 IN-28, `H-166` limit 1): the plan's `works_cost` is CONSUMED out of the works'
    rung, one-sided -- the timber goes into the fabric (`_cost`, `found`'s one reading of the price).

    HELD THROUGH ITS RUNG, NOT BY A `hold` OF ITS OWN: a `hold` never reaches a Site
    (`rosters.yaml: hold_object_kinds` is `[Office, Rung, Record, Proposition]`; r2 §A.10.1, intent:
    *"`hold` must not reach a `Site`"*, the commons), so a built fabric belongs to whoever holds the
    rung it stands at (`queries/world_q.py::hold_force(w, site.rung)`) -- a dwelling built in a
    founded hearth is its founder's. Nothing is minted here for it.

    DECLINES (`NO_CHANGE` -> `build.refused`): the subject is no works or its `at` is no rung
    (`_works_named`, `found`'s one reading); the plan is not a `site_kinds` member (a works to found
    a Rung is `found`'s); the works has already built (`_made_by`'s id is taken); the plan has no
    price or its rung cannot pay it (`_cost`). ⚠ `site_kinds` CARRIES `body`, WHICH ITS OWN NOTE SAYS
    *"IS NOT A SITE"*: since v9 IN-28 a works planning a `body` is refused because `works_cost`
    prices none -- the ROSTER refusing it, not a kind literal here (`H-166` limit 4, narrowed; the
    `body` row stays in `site_kinds` for `band_floors`).

    G4 -- WHAT IT NAMES: THE SITE, whole, earning `site.built`; it always moves (absent -> present)."""
    rec, plan, rung = _works_named(w, a)
    if rec is None or plan not in SITE_KINDS:
        return NO_CHANGE
    sid = _made_by(rec, plan)
    if sid in w.sites:
        return NO_CHANGE
    paid = _cost(w, rec, plan)
    if paid is None:
        return NO_CHANGE
    payer, price = paid
    site = Site(sid, rung.id, plan, condition=0)

    def perform() -> None:
        w.sites[sid] = site
        # CONSUMED, ONE-SIDED: the cost goes into the fabric and is not credited anywhere
        # ([ASSUMPTION; medium; Jordan to correct], rosters.yaml `works_cost`).
        for kind, amount in sorted(price.items()):
            _debit(payer, kind, amount)
    return Change((Subject.entity("sites", sid, "site.built"),
                   Subject.entity("rungs", payer.id, "site.built")), perform)


@effect_for("raze")
def _eff_raze(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """v9 IN-12 step 11 (#453 §9.2 `raze`, §10.4 step 11) -- AN OCCUPIED SETTLEMENT IS RAZED: the Rung
    ends (`(Rung, exists)` -> absent) and every live Tenure naming it closes in the same write. The
    closer of `H-166` limit 3 (*"`w.rungs` now grows and nothing shrinks it"*), built after that row's
    own order: the cost (limit 1) and the holder (limit 2) landed at v9 IN-28.

    THE LICENCE IS OCCUPATION, READ AS `seize`'s RUNG HALF READS IT (`loop/effects_information.py::
    _seize_rung`, whose inlined read this copies, the entry's instruction): the exercised seat's FACTION
    (`seat_faction`) occupying the settlement (`world_q.occupies`, the one reading of that), the
    settlement held by ANOTHER faction (`holder_faction_of`). DECLINES (`NO_CHANGE` ->
    `raze.refused`), each one change from an admitted razing:
      * the subject is no Rung, or not a `raze_target_kinds` kind (a settlement: a territory is marched on
        and seized and never razed; occupation is defined only at the places a march arrives at) [ASSUMPTION; medium; Jordan to
        correct; revert: any Rung kind, the licence still occupation];
      * the exercised seat has no faction;
      * nobody holds the settlement (H-166: who holds an unheld place is unruled, `_seize_rung`'s
        reading) or the seat's own faction does -- a faction does not raze its own town;
      * the seat's faction is not mustered there (NO ARMY: the entry's falsifier).
    ⚠ NOT COPIED FROM `_seize_rung`: its decline on an actor not committed to the seat's faction. Its
    stated reason is that `seize` writes the ACTOR'S OWN `hold`; `raze` writes no title, so the reason
    does not reach it. The seat's authority to act at all is the fold's (eligibility `remit:dispatch`
    via `seat_hold`, the row's `existence` conjunct).

    THE CASCADE IS LAYER 1's, AND IT IS ALL OF IT (`architecture/meta/04_CODE_ARCHITECTURE.md` §B.8's
    row *subject or object ceases to exist*: *"`destroy` sets `until` on every Tenure naming the id
    and nothing else"*): every live edge whose subject or object is the Rung -- its own `contain` in
    its parent, the `contain`/`reside` of what stands in it, any `hold` on it -- closes, and the gate
    admits each closure under `cascade` (`state/gate.py`: the Rung is in the write's `gone`), save the razer's
    own `contain` there, which closes under `T-m` first (`test_in12_raze.py`).
    `_eff_destroy_record`'s body, on the Rung store (it closes every live edge naming the Rung, subject or object; `destroy_record`'s closes the object only). ⚠ NOTHING IS RE-HOMED, AND THAT IS #453's OWN
    RECORDED GAP (*"persons contained in a razed Rung are left placeless by the cascade"*) and `H-228`'s:
    a quarter or hearth in the town becomes a root of its own, a person or cohort standing in it is
    placeless, and a Site or Record whose `rung` field names it keeps naming an id the world no
    longer holds (a field, not a Tenure, so the cascade does not reach it). Ending the Sites with
    their Rung, or re-homing what stood in it, is a write Layer 1 does not license here.

    G4 -- WHAT IT NAMES: THE RUNG, whole, earning `rung.razed`; it always moves (present -> absent).
    The closed edges are the cascade and are not named, as `destroy_record`'s are not."""
    rid = _operand(a, "subject")
    # ED-IN-0306 phase 4: a territory is marched on and occupied now, and still not razed (`raze_target_kinds`).
    mine = occupying_faction(w, a.via, rid) if rid in w.rungs and w.rungs[rid].kind in RAZE_TARGET_KINDS else None
    # Razing stays the act of the army that is IN the town: a territory's occupation carries a settlement's
    # SEIZURE (the title), not its destruction.
    if mine is None or not mustered(w, rid, mine):
        return NO_CHANGE

    def perform() -> None:
        del w.rungs[rid]
        for t in w.tenures:
            if t.live and (t.subject == rid or t.object == rid):
                t.until = w.tick
    return Change((Subject.entity("rungs", rid, "rung.razed"),), perform)
