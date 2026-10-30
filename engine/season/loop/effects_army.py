"""`season.loop.effects_army` -- the four verbs that change a faction's army record: `recruit`, `form_unit`,
`assign_troops` and `order_unit` (ED-IN-0304 phase 2).

Jordan ruled on 2026-10-28 that a faction's army is an order-of-battle RECORD (kind `army`, `rosters.yaml:
record_kinds`), not only `PersonId[] at weight`. The record's CONTENT -- what it says, every operation on it, and
the recruiting limit -- is `modules/mass_battle/armyrecord.py`'s, reached here by the `mass_battle.army` composition
row, so the four effects below are thin: read the world for the facts the rule needs, build one `ArmyCommand`, call
the entry, and write the `subject_matter` it returns back to the Record. A rule the entry breaks raises ValueError,
which is the verb's refusal (`NO_CHANGE` -> the row's `*.refused`).

THE ONE WRITE IS `(Record, subject_matter)`, a matrix row this position adds: every other Record kind is written
once, inside its mint. Each effect declines a Record that is not an `army`, so no other kind gains a mutable body.

WHAT THE COMMAND SAYS IS THE ACT'S PAYLOAD (a cohort, a troop type, a count, a subformation's name and tactics), not
an operand: the operand vocabulary is closed at eight and names none of these (`rosters.yaml: requires_operands`).
So these verbs are reached by a hand-built act -- what the menu builds -- and `Fixtures withheld_verbs` keeps
`decision/options.py::opening_set` from forming them for anybody.

G4 -- WHAT EACH NAMES: THE ARMY RECORD, whole, earning the row's one emitted kind. A command that leaves the record
as it was (the only way the named subject could fail to move) is declined, not written.
"""

from __future__ import annotations

from engine.substrate import composition

from ..queries import world_q
from ..queries.world_q import faction_holding
from ..queries.inputs import ArmyCommand
from ..state.gate import NO_CHANGE, Change, Subject
from .effects_shared import _operand, effect_for


def _army(w: "World", a: "Act"):
    """The `army` Record the act names (its `subject`), or `None` -- the subject exists and is held by the actor
    (the row's typed cell), and this reads what it IS, which no cell can."""
    rec = w.records.get(_operand(a, "subject"))
    if rec is None or rec.kind != "army" or not isinstance(rec.subject_matter, dict):
        return None
    # Holding the Record is not commanding the army (a Record can be handed on): the commander is committed to the
    # army's faction, as the minter had to be.
    return rec if faction_holding(w, a.actor) == rec.subject_matter["faction"] else None


def _payload(a: "Act", *names: str) -> dict:
    """The named keys the act's payload carries, those absent left out (an optional tactic is not set by silence)."""
    d = a.payload if isinstance(a.payload, dict) else {}
    return {n: d[n] for n in names if n in d}


def _apply(w: "World", a: "Act", op: str, args: dict, kind: str) -> Change:
    """Run `op` on the named army and write the result back, or decline. The one body of the four effects."""
    rec = _army(w, a)
    if rec is None:
        return NO_CHANGE
    try:
        new = composition.require(world_q.ARMY)(ArmyCommand(rec.subject_matter, op, args))
    except ValueError:
        return NO_CHANGE
    if new == rec.subject_matter:
        return NO_CHANGE

    def perform() -> None:
        rec.subject_matter = new
    return Change((Subject.entity("records", rec.id, kind),), perform)


@effect_for("recruit")
def _eff_recruit(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """RAISE TROOPS: `count` of `troop_type`, drawn from the cohort Person `cohort`, into the army's trained pool.

    The limit is the module's (`troop_types/recruitment.py::recruit_limit`): the cohort's weight bounds how many can
    be under arms, and the best Site of the troop type's own kind in the cohort's residence bounds how many of that
    type. This effect supplies those two facts and refuses what the cohort cannot be: no Person, not a cohort
    (`weight` of 1 is an individual, whose household is not an army's population), or not committed to the army's
    faction. [ASSUMPTION; medium; Jordan to correct; revert: any person in `world_q.members` is a cohort.]"""
    rec = _army(w, a)
    if rec is None:
        return NO_CHANGE
    args = _payload(a, "cohort", "troop_type", "count")
    cohort = w.persons.get(args.get("cohort")) if isinstance(args.get("cohort"), str) else None
    if (len(args) != 3 or cohort is None or not cohort.weight > 1
            or cohort.id not in world_q.members(w, rec.subject_matter["faction"])):
        return NO_CHANGE
    args = dict(args, weight=cohort.weight, sites=world_q.training_sites(w, cohort.id),
                full=w.fixtures.get("condition_scale"))
    return _apply(w, a, "recruit", args, "army.recruited")


@effect_for("form_unit")
def _eff_form_unit(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """FORM A SUBFORMATION: an empty, named one of `troop_type` (and optionally a `role` from the type's menu)."""
    return _apply(w, a, "form", _payload(a, "name", "troop_type", "role"), "army.formed")


@effect_for("assign_troops")
def _eff_assign_troops(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """ASSIGN TROOPS: move `count` trained troops of `cohort` into subformation `name`, or out of it when `count` is
    negative. No trooper is created or lost."""
    return _apply(w, a, "assign", _payload(a, "name", "cohort", "count"), "army.assigned")


@effect_for("order_unit")
def _eff_order_unit(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """ORDER A SUBFORMATION OR THE ARMY: set subformation `name`'s `role`, `stance`, `target` and `fall_back_at`
    (a field the payload leaves out is unchanged), or the army's `strategy` alone."""
    return _apply(w, a, "order", _payload(a, "name", "role", "stance", "target", "fall_back_at", "strategy"),
                  "army.ordered")
