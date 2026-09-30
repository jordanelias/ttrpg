"""`season.loop.effects_founding` -- minting works: found, build.

EXTRACTED from `effects.py` at the per-subsystem split (Phase 4). Holds the pair that grows the
world rather than only wearing it down (`ARCH` F.20): `found` mints a Rung of whatever kind a works
plans, `build` mints a Site at condition 0. `_works_named` (what a works names, plans and is placed
at) and `_made_by` (the one id scheme so one works makes one thing) are this pair's own reading of
their operand and stay local -- nothing outside `found`/`build` calls either. See `effects_shared.py`
for `effect_for`, `_operand` and the shared §10-ladder refusal `_decline_ascent`.
"""

from __future__ import annotations

from ..data.rosters import RUNG_KINDS, SITE_KINDS
from ..queries.world_q import works_target
from ..state.carriers import Rung, Site, Tenure
from ..state.gate import NO_CHANGE, Change, Subject
from ..state.ids import H
from ..state.world import rung_kind_ascends

from .effects_shared import _decline_ascent, _operand, effect_for


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
      * EMPTY: no stores, no sites, no holder. A founded hearth has no dwelling until one is BUILT
        (`build`, plan `24e`: *"A founded hearth has no dwelling until one is BUILT"*), and no
        `hold` is minted on it -- who holds a founded place is not this position's, and a `hold`
        written here would be a claim of ownership nobody made (`H-166`).
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
    rung = Rung(rid, plan)
    placed = Tenure(H(w.world_seed, w.tick, rid, f"contain:{parent.id}:{a.id}"), rid, parent.id,
                    "contain", since=w.tick)

    def perform() -> None:
        w.rungs[rid] = rung
        w.add_tenure(placed)
    return Change((Subject.entity("rungs", rid, "rung.founded"),), perform)


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

    DECLINES (`NO_CHANGE` -> `build.refused`): the subject is no works or its `at` is no rung
    (`_works_named`, `found`'s one reading); the plan is not a `site_kinds` member (a works to found
    a Rung is `found`'s); the works has already built (`_made_by`'s id is taken). ⚠ `site_kinds`
    CARRIES `body`, WHICH ITS OWN NOTE SAYS *"IS NOT A SITE"*: a works planning a `body` would build
    one. Refusing it here would be a kind literal in a body standing in for a roster defect; it is
    `H-166`'s, and no computed act can declare a works to reach it.

    G4 -- WHAT IT NAMES: THE SITE, whole, earning `site.built`; it always moves (absent -> present)."""
    rec, plan, rung = _works_named(w, a)
    if rec is None or plan not in SITE_KINDS:
        return NO_CHANGE
    sid = _made_by(rec, plan)
    if sid in w.sites:
        return NO_CHANGE
    site = Site(sid, rung.id, plan, condition=0)
    return Change((Subject.entity("sites", sid, "site.built"),),
                  lambda: w.sites.__setitem__(sid, site))
