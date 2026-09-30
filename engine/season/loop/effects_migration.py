"""`season.loop.effects_migration` -- travel and settlement: move, migrate.

EXTRACTED from `effects.py` at the per-subsystem split (Phase 4). Holds the presence/residence pair:
`move` re-homes `contain` alone, `migrate` re-homes `contain` AND `reside` in one write. `_relocate`,
the journey the two share (the traveller's live `contain` legs close, a new one opens, and `dest` is
appended to `Person.travel_leg`), stays local here -- only this pair calls it. See `effects_shared.py`
for `effect_for`, `_operand` and the shared §10-ladder refusal `_decline_ascent`.
"""

from __future__ import annotations

from ..queries.world_q import RESIDE_KIND, ancestry, capacity, population, residence_of
from ..state.carriers import Tenure
from ..state.gate import NO_CHANGE, Change, Subject
from ..state.ids import H
from ..trace_log import TRACE

from .effects_shared import _decline_ascent, _operand, effect_for


@effect_for("move")
def _eff_move(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§D4 / #353 §15.1: travel is a TENURE ALTER, owned by the traveller as the Tenure's subject.
    The old leg closes and a new one opens; the destination rides on the payload where the act
    names one. ⚠ This is `H-63`: Part E's `writes:` names the three cells and never the values, so
    what a `move` DOES is stated here rather than in the table — one implementation owned by the
    resolver, which is the distinction §27.2 draws against a caller-supplied lambda.

    G4 -- WHAT IT NAMES: THE TRAVELLER, WHOLE -- and only the traveller, which is what it always
    reported. That is not an omission of the legs: a `contain` leg is owned by its subject and
    stored on the Person (S15.1), so the Person's digest -- the string the content hash folds for
    them -- carries the legs AND `travel_leg`, and a move moves it. Naming the two legs as well
    would put two receipts on every `travel.moved` that has always carried one, which moves a hash
    for a reason that is not a no-op. A traveller who is not a Person (a hand-built act; RESOLVE
    never folds one, `act.ineligible` stops it first) names an absent subject that stays absent,
    so the move is refused and the legs it opened are put back -- where before G4 it published
    `travel.moved` about a mover that does not exist."""
    dest = _operand(a, "to")
    # ⚠ THE GUARD MOVED TO `_operand` AND ITS HISTORY IS KEPT HERE, because the history is what
    # makes the guard's shape legible. Rev 1 fell through on a missing destination, closed every
    # live leg and STILL returned `[a.actor]`, so `_fold` saw a non-empty `changed` and published
    # `travel.moved` for a move that did not happen. Returning `[]` would be quieter and just as
    # wrong: the caller would report a no-op as a legitimate nothing. §42.2's polarity rule -- no
    # destination is a refusal, never a silent success. The version of this guard that lived here
    # was found to pass `needs=`/`law=` to `InstrumentDefect`, which takes no keywords, so it
    # would have raised `TypeError` if it had ever fired -- a guard that crashes instead of
    # reporting, unfired because the precondition refuses first. One owner is also one place for
    # that mistake to be made.
    # ⚠ A DESTINATION THE LADDER WILL NOT SEAT THE MOVER IN IS A BLOCKED TRAVEL, NOT A CRASH, and
    # this branch is `W-C`'s doing: once `move` carries a real `to`, a person can name any rung
    # their containment path reaches, and `contain.path` asks for a SHARED ANCESTOR -- which a
    # sibling has. So `move p_low -> p_mid` passed the precondition, `add_tenure` raised
    # `Forbidden` on the §10 ladder, and the season died. Declining here returns nothing changed,
    # so the fold emits `move`'s own `emits_on_refusal`. The rule itself is not re-implemented:
    # `World.contain_ascends` is the one owner and `add_tenure` still RAISES on it, because a
    # caller writing the edge directly is a bug where a person attempting the journey is not.
    if not w.contain_ascends(a.actor, dest):
        # ⚠ THE INSTANCE DETAIL SITS AFTER ` -> `, WHICH IS `report.py`'s CLUSTER KEY
        # (`d.what.split(" -> ")[0]`). Putting the actor and the destination in the prefix would
        # mint one register entry per pair and leave the label reading mid-sentence.
        return _decline_ascent(
            f"a move's destination is not up the §10 ladder -> {a.actor} into {dest!r}")
    # ⚠ PLAN POSITION `19c`: WHAT A `move` LEAVES BEHIND IS THE MOVER'S `reside` EDGE -- it is not
    # touched here, so a traveller still lives where he lived (`_eff_migrate`'s docstring).
    return Change((Subject.entity("persons", a.actor),), lambda: _relocate(w, a, dest))


def _relocate(w: "World", a: "Act", dest: str) -> None:
    """THE JOURNEY, `move`'s and `migrate`'s one body: the actor's live `contain` legs close, a new
    one opens to `dest`, and `dest` is appended to `Person.travel_leg` -- the movement in progress
    (`ARCHITECTURE_V2.md` §D4) that `loop/matter.py`'s travel pass ends at the next MATTER. Called
    inside an effect's `perform`, so the gate observes every edge it writes. Extracted UNCHANGED from
    `_eff_move` at plan position `19c` because `migrate` is a journey too (a settler travels to his new
    home and pays the same distance penalty the season he goes), and a second copy of *what a journey
    writes* would let the two verbs disagree about it (§8). The leg's id is `move`'s, byte for byte,
    so every run that only moves is unmoved by the extraction."""
    for t in w.tenures:
        if t.subject == a.actor and t.kind == "contain" and t.until is None:
            t.until = w.tick
    w.add_tenure(Tenure(H(w.world_seed, w.tick, a.actor, f"leg:{a.id}"),
                        a.actor, dest, "contain", since=w.tick))
    # ⚠ THE DECLARED WRITE, NOW ACTUALLY WRITTEN. `verb_table.yaml`'s `move` row names
    # `(Person, travel_leg)` as its FIRST write and rev 1 never touched the field, so
    # `Query.budget`'s distance penalty read `len(p.travel_leg)` == 0 in every run and the only
    # test of it set the field by hand. A declared write that no effect performs is a lie the
    # write matrix cannot catch, because the matrix gates writes that HAPPEN.
    mover = w.persons.get(a.actor)
    if mover is not None:
        mover.travel_leg = list(mover.travel_leg) + [dest]


@effect_for("migrate")
def _eff_migrate(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """`RULINGS.yaml` RR-2 -- *"must be able to build hearths and accept people who move
    settlements"*; *"migration is a verb persons take"*. The migrant makes the journey (`_relocate`,
    `move`'s own body) AND settles at its end: his live `reside` edge closes and a new one opens to the
    destination, in one write.

    ⚠⚠ THE PRESENCE/RESIDENCE SPLIT, DECIDED HERE (plan position `19c`; `CLAUDE.md` §0 step 5 -- part
    1 `§5` routes it to architecture, not to Jordan). The tree had ONE edge for where you are and where
    you live, and `move` re-homed it. The split keeps `contain` as PRESENCE and adds `reside` as
    RESIDENCE, and `move` is defined by what it leaves behind: the `reside` edge.
      * WHY `contain` STAYS PRESENCE. It is ratified: `04_CODE_ARCHITECTURE.md` §B, *"LOCATION: ... its
        contain edge is where they are"*, and `ARCHITECTURE_V2.md` §D4, *"A person's location IS their
        contain Tenure"*. Every presence consumer reads it -- WITNESS's co-location, `share`, the larder
        ladder, `place_of` -- and `move` has executed as a re-homing across the corpus since `W-C`.
        Making `contain` the residence instead (and `travel_leg` the presence) reverses two ratified
        sentences and re-reads every one of those consumers.
      * WHY A TENURE AND NOT A CLAIM. The plan offered *"a WITNESS-side deposit rule or a Tenure kind"*.
        The throttle decides it: RR-2's capacity bounds POPULATION, the fold must count the people who
        LIVE under a rung, and the fold reads the world, never a ledger (AX-2, bar the actor's own). A
        residence held only in ledgers cannot be counted; a population counted by presence would make
        the throttle bypassable by one `move`, which reaches the same `contain` edge unthrottled.
      * WHY A TENURE AND NOT A `Person` FIELD. A person's relation to a place is an edge (`04` §B names
        LOCATION by its edge; `ID-2`, one home per fact), owned by its subject and judged by the gate's
        F3 like every other; `Person.marks`, which once listed *residence*, was deleted for having no
        reader or writer (`ED-IN-0261`). NOT a flag on `contain` either: `Tenure.payload` is the remit
        grant's (`H-71`), and the home edge ENDS when its owner travels, so residence would be read off
        an ended edge.
      * WHY EVERY BUILDER MINTS ONE, rather than residence defaulting to presence for a person with no
        `reside`. With the default, every writer of `contain` would be a silent writer of residence
        (`CLAUDE.md` §0.1 pt 1), and the next effect that re-homes a person would re-home his house.
        So `world_q.residence_of` reads one edge kind and nothing else.
    `move`, `migrate` and MATTER then state the whole of the split: a `move` re-homes `contain` and
    leaves `reside`; a `migrate` re-homes both; neither is a return, and a leg ends at MATTER either way.

    G3 -- EVERY EDGE IS THE ACTOR'S OWN (`T-m`): the `contain` legs and the `reside` edges are the
    migrant's, as subject, so the gate admits all four writes with no seat and NO NEW BASIS -- checked
    against `tenure_write_basis`'s nine rather than assumed: the closures are the owner's discretion,
    and an opening whose subject is the actor is `T-m`'s own case (it excludes only a SEAT-hold).

    G4 -- WHAT IT NAMES: THE MIGRANT, WHOLE, `move`'s reason: both edges are stored on the Person, so
    his digest carries them and his `travel_leg`, and one receipt says a migration happened.

    DECLINES (`NO_CHANGE` -> the `write` clause's `migrate.refused`):
      * a destination the §10 ladder will not seat him in (`move`'s decline, the same owner);
      * a destination he ALREADY LIVES IN -- a migration that changes no residence is none, and
        re-opening the same residence under a new id would be a digest move F9 publishes as a
        migration (`H-140`'s shape, answered for this verb rather than left open);
      * A DESTINATION AT CAPACITY -- RR-2's throttle, and `capacity`'s first caller (plan `24d-ii`,
        which lands here). A NEWCOMER is refused where `population(dest) + his weight` would pass
        `capacity(dest)`; the refusal is the destination's, read at the destination only, as the
        plan instructs (*"throttled by `capacity` at the destination"*). A migrant who ALREADY lives
        under `dest` (settling from his hearth into its settlement) is no newcomer to it: he is in
        its population before and after, so the move grows nothing and nothing throttles it.
        REJECTED: checking every ancestor too -- a newcomer to a hearth is a newcomer to its
        settlement, but a settlement's room is its hearths' room summed, and refusing a hearth
        with space because the town above is crowded would make the throttle a second, coarser
        census the ruling did not ask for; and throttling a `move` -- presence fills no house.
    REJECTED: settling without travelling (no leg) -- a settler makes the journey a traveller makes,
    and the distance penalty is the journey's, so two verbs pricing one journey two ways would be the
    S defect (*calculations consistent in methodology*)."""
    dest = _operand(a, "to")
    if not w.contain_ascends(a.actor, dest):
        return _decline_ascent(
            f"a migration's destination is not up the §10 ladder -> {a.actor} into {dest!r}")
    residence = residence_of(w)
    home = residence.get(a.actor)
    if home == dest:
        TRACE.decision(f"a migration to where the migrant already lives -> {a.actor} into {dest!r}",
                       "19c", chose="change nothing, so the fold emits the refusal",
                       alternatives=["re-open the same residence under a new id (a digest move "
                                     "published as a migration)", "treat it as a move"])
        return NO_CHANGE
    migrant = w.persons.get(a.actor)
    if migrant is None:
        # Not a person: `act.ineligible` stops it before the fold, so only a hand-built act lands
        # here, and it has no weight to house -- `move`'s reading of the same case.
        return NO_CHANGE
    newcomer = home is None or dest not in ancestry(w, home)
    if newcomer and population(w, dest, residence) + migrant.weight > capacity(w, dest):
        TRACE.decision(f"a migration into a rung at capacity -> {a.actor} into {dest!r}",
                       "RR-2/24d-ii", chose="change nothing, so the fold emits the refusal",
                       alternatives=["admit him anyway (capacity bounds nothing)",
                                     "refuse at every ancestor as well (a second, coarser census)"])
        return NO_CHANGE
    settled = [t for t in w.tenures if t.subject == a.actor and t.kind == RESIDE_KIND and t.live]

    def perform() -> None:
        _relocate(w, a, dest)
        for t in settled:
            t.until = w.tick
        w.add_tenure(Tenure(H(w.world_seed, w.tick, a.actor, f"reside:{a.id}"),
                            a.actor, dest, "reside", since=w.tick))
    return Change((Subject.entity("persons", a.actor),), perform)
