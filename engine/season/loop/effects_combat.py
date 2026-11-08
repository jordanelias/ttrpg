"""`season.loop.effects_combat` -- casualties and morale: fight (renamed from "kill / wound") and
the duel's `accept`, march; and the person raised (v9 IN-12 step 9, G15): tend, train; and the
grudge's closer (v9 IN-12 step 13, G15): forgive.

EXTRACTED from `effects.py` at the per-subsystem split (Phase 4). Holds the two effects that read a
severity off a scene the seam already resolved rather than choosing one (Jordan, 2026-09-04: *"the
combat engine determines the result there. your code just has to accept the result."*) -- personal
combat's `fight` and mass battle's `march`. `_scar` and `_SCAR_DP` (the moral-layer write on the
wounded person) are RETIRED at IN-08 H3: the scar is now written by the fold on the act's OBSERVERS
(`loop/resolve.py::_scar_witnesses`), not by an effect. See `effects_shared.py` for `effect_for`
and `_operand`, the helpers `march` takes from `effects_shared.py`; its arrival also calls
`effects_migration.py::_relocate`, the journey `move` shares (v9 IN-13).
"""

from __future__ import annotations

from dataclasses import replace

from ..data.rosters import (
    DECLARED, ENDING_FELLED, ENDING_UNDECIDED, ENDING_YIELDED, FELLED, FIELD_CASUALTY_MODELS, FIELD_WINNER_CASUALTY_ARMS, INVESTED, LOST, SUBTREE_OCCUPATION_KINDS, UNOPPOSED, UNTOUCHED, WON,
    VERB_CAPABILITY, WOUND_HARM_MODELS, BODY_MARK_MODELS, require_member,
)
from ..data.matrix import matrix_row
from ..data.requires import Observation
from ..data.verbs import VERB_TABLE, VOCATION_SOURCED, VOCATIONS
from ..gaps import Unspecified
from ..queries.person_q import held_against
from ..queries.world_q import BODY_STEM, DETAIN_KIND, ancestry, garrison_sites, holder_faction_of, home_of, restrained
from ..seam.ladder import party_degree
from ..state.carriers import Tenure
from ..state.gate import (
    NO_CHANGE, PERSON_DIED, Change, Subject, death_subjects, may_muster, may_warrant, own_kinds, seat_faction,
)
from ..state.ids import H

from .effects_economy import _fall
from .effects_information import _may_close_custody
from .effects_migration import _relocate
from .effects_shared import _debit, _operand, effect_for


# `accept` (the duel pair's second half) is the same contest over the same prize, `contests: "the
# body"`, with the same degree-keyed writes read off the same scene: one effect registered twice.
# The fold's scar reads `a.verb`, so a duel's moral layer reads `accept`'s own alignment cells. (`challenge`
# writes nothing and needs no effect: `VerbRow.effect_carried`.) `fight` was RENAMED from
# "kill / wound" (plan `FIGHT-RENAME`); only the `EFFECTS` key and its row moved.
CAPTURED = "person.captured"        # the one kind `capture`'s opened `detain` earns (`verb_table.yaml`'s `capture` row)
DUEL_YIELDED = "duel.yielded"       # v10 PC-10b: the kind a duel's yielder earns (`verb_table.yaml`'s `accept` row)
CEILING = "body_ceiling"          # v11 CP-T03-07: the cell the lasting mark writes (`write_matrix.yaml`)


def _yielder(res: "Resolution") -> "str | None":
    """THE PARTY THE SCENE'S `surrender` NAMES (`seam/wrappers/combat.py::surrender_of`, lifted onto the result), or
    `None`. The one reader both effects ask. `_eff_kill` refuses a `res` with no dict result only AFTER its
    opponent-not-a-person early return, so `_eff_capture` reaches this with such a `res` in a hand call: `None`."""
    if res is None or not isinstance(res.result, dict):
        return None
    return (res.result.get("surrender") or {}).get("by")


@effect_for("fight")
@effect_for("accept")
def _eff_kill(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§E3: writes `(Person, body)`, `(Person, exists)` and `(Tenure, until)` -- ON EACH PARTY, by his
    own band (CP-T03-00, `-08` AM-C-01): the actor as well as the subject. Where this docstring says
    "the subject" below, read "each party"; the rules are unchanged, and each runs per party.

    ⚠⚠ G4 -- WHAT IT NAMES, AND THE ONE EFFECT THAT NARROWS ITS SUBJECT TO A FIELD. The subject is
    the person wounded, read as PRESENCE and `body` (`fields=("body",)`) -- the two cells the
    band's own kinds name (`person.died` is existence, `body.changed` is body). TWO THINGS THE
    SAME WRITE DOES ARE DELIBERATELY NOT PART OF WHAT THE GATE JUDGES (a third, `scar`, left this
    effect at IN-08 H3: the fold writes it on the act's observers AFTER the outcome, as its own
    gated write, so a wound the gate refuses scars nobody):
      * the CASCADE (`remove_person`'s closures). A consequence of the existence change, which IS
        judged; F3 admits each closure as `destroy's cascade`. If existence did not move the cascade
        did not run. ⚠ CP-T02-01: ONE PART OF IT IS NOW NAMED -- each SEAT `hold` the death closes,
        as a `Subject.seat` earning `tenure.closed` and receipted under the Office's id
        (`state/gate.py::death_subjects`), so the death names the seats it empties. The other edges
        are still not named.
      * the dead person's own `person`-kind rung, popped by the same owner -- the same reasoning.
    THE NEW NO-OP THIS MAKES VISIBLE: a `Wounded` outcome under `scene_fraction` whose fraction
    rounds back to the body it started from (`max(1, body * left // full)` at `body == 1`, or a
    scene that took no health) used to emit `body.changed` over an unchanged body and is now
    `kill.refused`. MEASURED BEFORE THIS POSITION on `build_realm(0)`, four seasons: every
    `kill / wound` that reached this effect moved its subject, so no run moves.

    ⚠ AND THE TWO `Unspecified` RAISES COME BEFORE ANYTHING IS WRITTEN: both are read while the
    `Change` is built, which touches nothing.

    ⚠ THE TENURE ENDS THROUGH THE DEATH, which is §15.3's rule and the reason this is ONE effect
    rather than three writes a caller sequences: "a plague that kills the praefect ends his
    tenure THROUGH THE DEATH; A STORM CANNOT TOUCH IT." A wound that does not kill writes only
    the band, so the same verb covers both -- which is why the table's row is `kill / wound`.

    ⚠ `W-E`, 2026-09-04. THE EFFECT NOW TAKES THE RESOLUTION, AND `harm` IS GONE. Register row
    `H-114` measured what the old signature cost: the effect could not honour the branch
    `writes_at` had just selected, and the payload's `harm` key was read with the person's ENTIRE
    body as its fallback -- so a fold at degree `Wounded` reached `p.body == 0`, passed
    `if p.body > 0`, and DELETED THE PERSON. Both halves are closed here, and the `W-C` carve-out
    that named `harm` as `W-E`'s to own is retired with its subject rather than widened.
    ⚠ THE OLD SPELLING IS DELIBERATELY NOT QUOTED IN THIS DOCSTRING. `W-C`'s guard
    (`test_wc_no_operand_is_defaulted_by_a_get_or_setdefault_in_shape_py_outside_eff_kill`) scans
    RAW SOURCE TEXT, so quoting the deleted line here would keep its carve-out "used" and leave
    an open licence on the name `harm` -- the exact staleness that test's own `used == EXEMPT`
    assertion exists to catch, satisfied by prose describing the defect rather than by the defect.
    Found while running that test against this change.

    WHERE THE MAGNITUDE COMES FROM NOW, AND WHY IT IS NOT INVENTED. JORDAN, 2026-09-04, VERBATIM:
    *"the combat engine determines the result there. your code just has to accept the result."*
    So the harm is not a number this file chooses: it is the LOSS THE SCENE ALREADY COMPUTED, on
    the engine's own `WoundTracker`, read as the fraction of the subject's health the fight left
    standing. No constant is introduced by the default arm -- a fraction needs none, which is
    exactly why it is the default and the other two arms are the sweep.

    THE THREE ARMS (`wound_harm_model`, registered at `H-123`, injected at `DEFAULT_FIXTURES`):
      `scene_fraction`  body <- body x health_remaining / health_full. The scene decides.
      `total`           any wound is lethal. ⚠ THIS IS THE CONTROL AND IT IS THE BEHAVIOUR THIS
                        FUNCTION HAD BEFORE `W-E` (`harm` defaulting to full body), so the arm
                        that shows what the degree is worth is the code as it stood.
      `none`            a wound writes nothing. The fold's own write-nothing guard then emits the
                        REFUSAL rather than the success -- the second control, and it isolates
                        "the band selected a different write set" from "the band changed a value".

    ⚠ AND THIS SUPERSEDES ONE HARNESS TECHNIQUE, WHICH IS SAID HERE SO ITS OUTPUT IS NOT
    MISREAD. `proposals/2026-09-04-degree-sweep/arm3_tree.py` injects a degree by monkeypatching
    `VerbRow.writes_at` / `emits_at` and then calls `_fold` bare. That reached the effect while
    the effect took no degree; it cannot now, because the degree travels on the `Resolution` the
    SEAM returns and a patched READER is invisible from here. Re-run after `W-E`, its `Felled` and
    `Wounded` nodes report REFUSED with the message below. That is the closure of `H-114` seen
    from the probe's side -- the probe measured a world in which the degree could not reach the
    effect -- and not a new defect.

    ⚠ A WOUND CANNOT KILL, AND THE FLOOR IS STRUCTURAL RATHER THAN NUMERIC. The `Wounded` band
    means the engine did NOT fell this person; a model that took their body to 0 would contradict
    the band it is implementing. `max(1, ...)` is `seam/wrappers/combat.py::party_end`'s own floor
    (*"a dying person still fights"*), followed rather than reinvented."""
    d = a.payload if isinstance(a.payload, dict) else {}
    # THE OPPONENT IS THE ROW'S OWN (`VerbRow.opponent_operand`, the fold's `_target` rule): `subject` for
    # `fight` and `capture`, `to` for `accept` since v10 PC-10b (its `subject` is the challenge Record).
    row = VERB_TABLE[a.verb]
    who = d.get(row.opponent_operand())
    if who not in w.persons:
        return NO_CHANGE
    # ⚠ NO SCENE, NO HARM -- AND THIS IS A REFUSAL TO INVENT, NOT A MISSING FEATURE. `kill / wound`
    # declares `contests: the body`, so the only lawful route into this effect is through the
    # seam; an act folded without one has no scene to read a severity off, and the pre-`W-E`
    # answer to that was to kill. `writes_at(None)` already refuses one line earlier for the same
    # reason, so this is the second gate on the same road rather than a new rule.
    if res is None or not isinstance(res.result, dict):
        raise Unspecified(
            f"`kill / wound` on {who!r} was folded with no scene to read a severity from",
            "S39.4/H-98",
            needs="a Resolution from `resolve()`'s seam branch -- the personal-combat scene",
            law="Jordan 2026-09-03 -- kill/wound degrees are taken directly from scene combat. A "
                "harm this function chose would be the number `H-114` measured: the old default "
                "was the person's whole body, so an act naming no harm killed")
    states = res.result.get("wound_state") or {}
    model = w.fixtures.get("wound_harm_model")
    require_member(
        model,
        WOUND_HARM_MODELS,
        f"wound-harm model {model!r} is not in the roster",
        "H-123",
        law="`observers_for`'s precedent and its reason -- *an unrecognised mode silently "
            "falling back would make every measurement of this sweep read the control*")
    # CP-T03-00 (`-08` AM-C-01): BOTH PARTIES TAKE THEIR BAND. The actor and the subject are each read
    # off the scene by his OWN band (`seam/ladder.py::party_degree`, the walk `combat_degree` takes the
    # worst of) and written by it: `Felled` -> body 0 and `World.remove_person`; `Wounded` ->
    # `wound_harm_model`; `Untouched` -> nothing. Before this item only the subject was read, so an
    # attacker his target felled walked away and `person.died` was never his. A party who is no
    # longer a person is not written (the subject's case is the `NO_CHANGE` above).
    above = w.fixtures.get("combat_wounded_above")
    bands = {}
    for pid in dict.fromkeys((a.actor, who)):
        if pid in w.persons:
            band = party_degree(states.get(pid), above)
            if band != UNTOUCHED:
                bands[pid] = band
    bodies = {pid: _harm(w.persons[pid], band, model, states[pid])
              for pid, band in bands.items()}
    # v11 CP-T03-07: THE LASTING MARK, and the written body held under the ceiling it leaves (a body is never above
    # its ceiling; the Observation below reports the body as written).
    marks = _marks(w, bodies, states)
    for pid, ceiling in marks.items():
        bodies[pid] = min(bodies[pid], ceiling)
    grown = _grown(w, a, (a.actor, who), bands, bodies)

    def perform() -> None:
        for pid, ceiling in marks.items():
            w.persons[pid].body_ceiling = ceiling
        for pid, body in bodies.items():
            if body is not None:
                _wound(pid, body)
        for pid, raised in grown.items():
            w.persons[pid].capability = raised

    def _wound(pid: str, body: int) -> None:
        w.persons[pid].body = body
        if body > 0:
            return
        # ⚠ `w.tenures`, NOT `p.tenures + w._unowned`, AND THAT IS A FIX `W-E`'s OWN TEST FOUND.
        # `p.tenures` is the tenures this person is the SUBJECT of (§15.1 -- a Tenure is owned by
        # its subject), so the old scan could not see an edge ANOTHER PERSON owns that names the
        # dead one as its OBJECT. Measured in `tiny_world`: `t10`, a live `tie` from `p_low` to
        # `p_mid`, survived `p_mid`'s death and then DANGLED, because `del w.persons[who]` had
        # already removed the person it pointed at. §15.3 is explicit that the tenure ends THROUGH
        # THE DEATH; this is the write the `Felled` branch declares (`Tenure.until`) actually
        # reaching every edge it names. `w.tenures` is owner-first over every person plus
        # `_unowned`, so it is a WIDENING of the same scan and not a second rule.
        # ⚠ THE CASCADE MOVED TO `World.remove_person` (item 3b) AND THE COMMENT ABOVE IS ITS
        # PROVENANCE. It is unchanged in behaviour — the same `w.tenures` scan, for the same `W-E`
        # reason — and it moved because MATTER is now a SECOND way to die (a body reaching 0 from
        # an empty larder), and two sites closing tenures by hand is how the two drift apart (§8).
        # ⚠ G3: THESE CLOSURES ARE `destroy's cascade`, AND THE GATE RECOGNISES THEM BY
        # OBSERVATION. They run inside this act's own gated write (the `(Person, body)` pair, the
        # first in the `Felled` band), `remove_person` takes `who` out of `w.persons` in the same
        # `apply()`, and the gate admits a closure of an edge naming an id THE SAME WRITE removed
        # -- and nothing else. A cascade that closed the edges and left the person standing would
        # be refused and put back.
        w.remove_person(pid)
    # CP-T02-01 / HR-1: EVERY SUBJECT NAMES ITS KINDS. Each party earns HIS band's own kinds
    # (`own_kinds`: `body.changed` on `Wounded`), plus `person.died` where this write takes his body to
    # 0; each seat his death empties earns `tenure.closed`, its receipt naming the Office
    # (`death_subjects`). A band that does not declare a kind still does not emit it (`_fold`).
    # CP-T03-00: A FELLED PARTY EARNS THE DEATH'S KINDS ALONE, as before this item. The `Felled` cell's
    # `body.changed` is there for the OTHER party of a mixed fight -- the cell is the ACT's band, the
    # worst over both, so it must license what a Wounded party earns beside a felled one -- and is not
    # the felled man's own kind. And because `_fold` gives each kind's Event only its earners' changes,
    # the person.died Event of a felled actor names him, never the standing subject.
    # v10 PC-10b: `duel.yielded` IS EARNED BY THE YIELDER ALONE -- the party the scene's `surrender`
    # (`seam/wrappers/combat.py::surrender_of`, lifted off the trace) names. A band declaring it (`accept`'s
    # `Wounded`) would otherwise hand it to every wounded party, a yield nobody made (ID-9). Read off the
    # result, never the verb: a row whose band does not declare the kind emits nothing of it (`_fold`).
    yielder = _yielder(res)
    named: tuple = ()
    for pid, band in bands.items():
        own = () if band == FELLED else own_kinds(row.emits_at(band))
        own = tuple(k for k in own if (k != DUEL_YIELDED or pid == yielder) and k not in GROWN_KINDS)
        if bodies[pid] == 0:
            named += death_subjects(w, pid, own, fields=("body",))
            continue
        # CP-T03-02 (ii): A WOUNDED PARTY'S SUBJECT CARRIES WHAT HIS BODY NOW IS -- `(pid, "body", v)`, `v` the
        # value `perform` WRITES (`bodies`), never `w.persons[pid].body` read here, which is the pre-fight body
        # (the item's mutation). It rides each Event this subject earns (`body.changed`; a yielder's
        # `duel.yielded`), so WITNESS deposits it as it deposits `stores:<kind>` and `condition`: by the shipped
        # `observation_deposit_mode` (`actor`: the act's actor alone), no new channel. A `none`-model party
        # (`bodies[pid] is None`) writes nothing and observes nothing.
        # [ASSUMPTION; medium; Jordan to correct; revert: the field and the Observation]
        named += (Subject.entity("persons", pid, earns=own, fields=(BODY_STEM, CEILING),
                                 observed=body_observed(pid, bodies[pid])),)
    # CP-T03-04 (iv): EACH GROWN PARTY IS ITS OWN SUBJECT ON `capability`, earning the `(Person, capability)` cell's
    # kind alone -- never a body subject's kind, and never on a party who did not grow (the filter above).
    named += tuple(Subject.entity("persons", pid, earns=GROWN_KINDS, fields=("capability",)) for pid in grown)
    return Change(named, perform, fight_ending(w, (a.actor, who), res, above))


# CP-T03-04 (iv): THE KINDS A GROWN PARTY EARNS -- the `(Person, capability)` matrix row's own `emits:`
# (`write_matrix.yaml`), `train`'s kind, read off its owner rather than spelt.
GROWN_KINDS = matrix_row("Person", "capability").emits


def raised_capability(p: "Person", key: str) -> "dict | None":
    """`p.capability` with `key` raised by ONE whole point, the unit of a dice count -- `_eff_train`'s write and
    `_grown`'s, one body. `None` where `p` does not already hold `key`: a key is NEVER MINTED, because a minted
    `{arms: 1}` would replace `pool_default` in `faculty` and LOWER the pool of the man it meant to reward."""
    if key not in (p.capability or {}):
        return None
    return {**p.capability, key: int(p.capability[key]) + 1}


def _grown(w: "World", a: "Act", parties, bands: dict, bodies: dict) -> dict:
    """v11 CP-T03-04 (iv), BUILD-BY-DOING: `{pid: raised capability}` for each party of a fight THAT DREW BLOOD (some
    party `Wounded` or `Felled`, i.e. `bands` is not empty) who SURVIVES it (his written body is not 0) and ALREADY
    HOLDS the key the verb draws on (`VERB_CAPABILITY[a.verb]`, `rosters.yaml: verb_capability` -- `arms` for the
    three verbs contesting `the body`; the name is read there, never spelt here). Raised by ONE whole point,
    `_eff_train`'s unit.

    ⚠ NEVER MINTED (`_eff_train`'s rule and its reason): a minted `{arms: 1}` would replace `pool_default` 2 in
    `faculty` and LOWER the pool of the man it meant to reward. A party holding no key gains nothing.
    ⚠ ONLY WHERE BLOOD WAS DRAWN, AND THE REASON IS THE FOLD, NOT TASTE: `fight`'s and `accept`'s `Untouched` band
    writes nothing, so the fold never runs this effect there (`loop/resolve.py`, `_pairs`); declaring a
    `Person.capability` write on it would turn every untouched fight between non-holders into `kill.refused`
    (the gate's no-op refusal) where it emits `contest.undecided`. `capture` runs this effect at `Untouched` (its
    `Tenure.since`), and the same rule (`bands` empty) holds it to the same answer.
    [ASSUMPTION; medium; Jordan to correct; revert: return `{}` here, and the three bands' `Person.capability`
    write and `capability.raised` kind in `verb_table.yaml`]."""
    key = VERB_CAPABILITY.get(a.verb)
    if not key or not bands:
        return {}
    out = {}
    for pid in dict.fromkeys(parties):
        p = w.persons.get(pid)
        raised = None if p is None or bodies.get(pid) == 0 else raised_capability(p, key)
        if raised is not None:
            out[pid] = raised
    return out


def body_observed(pid: str, body: "int | None") -> tuple:
    """CP-T03-02 (ii): the Observation a wounded party's write carries -- `(pid, "body", v)`, `v` the WRITTEN body
    -- or `()` where the write writes nothing (`wound_harm_model: none`)."""
    return (Observation(pid, BODY_STEM, body),) if body is not None else ()


BROKE_STEM = "broke"


def broke_observed(pid: str, broke: "str | None") -> tuple:
    """CP-T04-01: the Observation the loser whose subunit BROKE FIRST carries on the field's band Event --
    `(pid, "broke", True)` -- or `()` for every other loser and for a field that names nobody (the `side` arm, or a
    side whose subunits did not break on their own account). An Event carries no payload (`Event.ending`'s note), so the
    cause rides `Event.observed`, deposited by WITNESS as `body_observed` is. [ASSUMPTION; medium; Jordan to correct;
    revert: the Observation, and the field's cause is unnamed]"""
    return (Observation(pid, BROKE_STEM, True),) if pid == broke else ()


def fight_ending(w: "World", parties, res: "Resolution", above) -> tuple:
    """CP-T03-02 (i): `Event.ending` -- `(pid, felled | yielded | undecided)` for each party still a person, in
    party order, read off the scene's lifted `wound_state` (`party_degree`, the walk `_eff_kill` writes by) and
    `surrender` (`_yielder`). Read BEFORE the write, which is right: it reports the scene, not the world.
    [ASSUMPTION; medium; Jordan to correct; revert: the field and the Observation]"""
    states = res.result.get("wound_state") or {}
    yielder = _yielder(res)
    out = []
    for pid in dict.fromkeys(parties):
        if pid not in w.persons:
            continue
        out.append((pid, ENDING_FELLED if party_degree(states.get(pid), above) == FELLED
                    else ENDING_YIELDED if pid == yielder else ENDING_UNDECIDED))
    return tuple(out)


@effect_for("capture")
def _eff_capture(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """CP-T03-09 (`-08` AM-C-03): `fight`'s WOUNDS, AND THE BEATEN MAN TAKEN INTO A SEAT'S CUSTODY WHERE THE SCENE
    ENDED IN HIS YIELD. A named fold of `fight`, not a second fight: `_eff_kill` is called and its `Change` is the
    base (each party written by his own band, `seam/ladder.py::party_degree`), to which ONE `detain` EDGE is added,
    the captive (the act's `subject`) -> THE SEAT THE ACT IS EXERCISED THROUGH (`Act.via`) -- the seat is `via`
    itself, not an issuing seat, because no warrant is behind a capture (`_eff_arrest` reads one; PC-10b's challenge
    Record is `accept`'s, not `capture`'s).

    WHAT LICENSES THE EDGE, EACH ONE OWNER OF ITS RULE (`_eff_arrest`'s tests, minus the warrant): (1) the scene's
    `surrender` (`seam/wrappers/combat.py::surrender_of`, lifted off the trace) names the SUBJECT as the one who
    yielded -- a yield by the actor, or none, opens nothing, and a scene in which either party was felled opens
    nothing (a felled actor holds no seat to take him into); (2) the subject is a person other than the actor and
    not already in custody (`restrained`, one live `detain` per prisoner); (3) the exercised seat may take him
    (`may_warrant`, the gate's own predicate) AND its live holder could close the custody (`_may_close_custody`,
    `pardon`'s basis), so an act the precondition admitted is never killed at the gate and a custody nothing could
    release is never opened. The gate is UNCHANGED: its `warrant` clause admits an opened `detain` whose object is
    a seat under `may_warrant`. Anything else leaves the base: the wounds `fight` would have dealt, or, where
    nobody was written, `NO_CHANGE` and `capture.refused` (the write clause) -- not `contest.undecided`.

    The kind is a LITERAL and the effect is registered for `capture` ALONE, so `data/verbs.py::
    _derive_openers_from_effects` reads `capture` (not `fight` or `accept`, which share `_eff_kill`) as a
    `detain` opener beside `arrest`. G4 -- WHAT IT NAMES: the edge, which always moves (absent -> present), earning
    `person.captured` alone."""
    base = _eff_kill(w, a, res)
    # ⚠ THE WOUNDED PARTY DOES NOT EARN THE CAPTURE. `_eff_kill` names each party with his band's declared kinds
    # (`own_kinds`), and `Wounded` declares `person.captured` so a wounded yielder's Event can be emitted; left
    # on the party, a wounded scene with NO yield would report a capture nobody made (ID-9). Only the edge earns it.
    base = replace(base, subjects=tuple(replace(s, earns=tuple(k for k in s.kinds if k != CAPTURED))
                                        if CAPTURED in s.kinds else s for s in base.subjects))
    prisoner = _operand(a, "subject")
    if _yielder(res) != prisoner or prisoner not in w.persons or prisoner == a.actor:
        return base
    # A PARTY THE BASE REMOVES CANNOT BE HELD OR HOLD. `person.died` is the base's own record of it: a felled party
    # (every arm), and a WOUNDED one under `wound_harm_model: total` (`_harm` writes body 0 there, so `_wound`
    # removes him). Read off the base's subjects, the one owner, never recomputed from the band: an edge on a man
    # the same write removes -- or opened by a seat whose holder it removes -- is refused at the gate
    # (`NotYours`), and nothing in the fold catches that, so the season would end.
    if any(PERSON_DIED in s.kinds for s in base.subjects) or restrained(w, prisoner, DETAIN_KIND):
        return base
    if a.via is None or not may_warrant(w, a.actor, a.via, prisoner) or not _may_close_custody(w, a.via, prisoner):
        return base
    nt = Tenure(H(w.world_seed, w.tick, prisoner, f"detain:{a.via}:{a.id}"), prisoner, a.via, "detain",
                since=w.tick)

    def perform() -> None:
        base.apply()
        w.add_tenure(nt)
    return replace(base, subjects=base.subjects + (Subject.edge(nt, earns=CAPTURED),), apply=perform)


def marked_ceiling(ceiling: int, floors) -> int:
    """v11 CP-T03-07 (P32): THE CEILING A MARK LEAVES -- one below the highest body band floor at or beneath `ceiling`
    (`band_floors["body"]`, the floors `decision/budget.py::body_band_penalty` counts): 1000 -> 799 -> 499 -> 99 on the
    shipped floors. With no floor at or beneath it, `ceiling` unchanged: the marks are as many as the body has floors,
    and no count is spelt here."""
    # a floor of 1 or less would leave a ceiling of 0 or below, which `_wound` reads as a death: only floors above 1 mark
    below = [int(f) for f in floors if 1 < int(f) <= ceiling]
    return max(below) - 1 if below else ceiling


def _marks(w: "World", bodies: dict, states: dict) -> dict:
    """v11 CP-T03-07: `{pid: new body_ceiling}` for each party of a fight who SURVIVES it (his written body is above 0;
    a `none`-arm party, written nothing, is not marked) at the engine's DEEPEST GATE SHORT OF FELLING -- `wounds >=
    max_wounds` on his lifted tracker (`rosters.yaml: wound_quantities`) -- and whose ceiling the mark lowers
    (`marked_ceiling`). `body_mark_model: none` (`H-258`, the control) marks nobody.
    [ASSUMPTION; medium; Jordan to correct; revert: `body_mark_model: none`]"""
    mode = w.fixtures.get("body_mark_model")
    require_member(
        mode, BODY_MARK_MODELS, f"body-mark model {mode!r} is not in the roster", "H-258",
        law="`wound_harm_model`'s precedent -- an unrecognised mode silently falling back would make every "
            "measurement of the sweep read the control")
    if mode == "none":
        return {}
    floors = w.fixtures.get("band_floors")["body"].values()
    out = {}
    for pid, body in bodies.items():
        if not body:
            continue
        st = states[pid]
        if st.get("wounds") is None or st.get("max_wounds") is None:
            raise Unspecified(
                f"the scene reports no wound gate for {pid!r} ({st!r})", "S39.4/H-258",
                needs="`wounds` and `max_wounds` on the party's wound state",
                law="the mark is READ off the scene's tracker; a scene that carries no gate cannot be read")
        if int(st["wounds"]) < int(st["max_wounds"]):
            continue
        p = w.persons[pid]
        after = marked_ceiling(p.body_ceiling, floors)
        if after != p.body_ceiling:
            out[pid] = after
    return out


def _harm(p: "Person", band: str, model: str, st: dict) -> "int | None":
    """THE BODY ONE PARTY OF A FIGHT IS LEFT WITH, by his own band (CP-T03-00; `_eff_kill`'s three arms,
    unchanged): `0` on `Felled` (every arm -- the arms grade a WOUND, and a felling is not one); on
    `Wounded`, `None` (not written) under `none`, `0` under `total`, else the scene's fraction
    `max(1, body x health_remaining // health_full)`."""
    if band == FELLED:
        # The scene says this person went down, and the table says that is the kill.
        return 0
    if model == "none":
        return None                             # the control arm: the body is not written
    if model == "total":
        return 0
    full = int(st.get("health_full") or 0)      # `scene_fraction`
    left = int(st.get("health_remaining") or 0)
    if full <= 0:
        raise Unspecified(
            f"the scene reports no health scale for {p.id!r} ({st!r})", "S39.4/H-123",
            needs="`health_full` on the party's wound state",
            law="the magnitude is READ from the scene; a scene that carries none cannot be "
                "read, and choosing a number here is what this arm exists not to do")
    return max(1, p.body * max(0, left) // full)


@effect_for("march")
def _eff_march(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§E3 (M4, `ED-IN-0279` clause (a)): writes `(Person, body)` and `(Person, stance)` -- ON
    THE LOSING SIDE, on either band. Jordan's ruling on clause (b): a loss writes *"casualties
    only, decrease in morale, and a grudge token"* and nothing else -- the ruling specifies nothing
    for the winner.

    ⚠ CR-24 (`field_winner_casualties`, `H-360`, M4 Ask B (b)): UNDER `engine` (SHIPPED) THE WINNERS TAKE THEIR OWN
    ENGINE CASUALTIES, ON `body` ONLY -- each winner at his own side's survivor ratio (`attacker_size_pct` /
    `defender_size_pct`) or, under `field_subunits: person`, his own subunit's (CP-T04-01's `subunits` record), never
    the loser's, and never above 1 (a winner is not raised). A winner is NOT a loser: he is not appended to `touched`,
    so he earns no grudge against his own faction and no morale hit, and he gets no stance row. A winner who also
    marches is one Subject (the mover's). Under `field_casualty_model: total` ("any wound is lethal") a winner who took a
    casualty (his ratio below 1) takes the loser's body-to-0 and the same death write (`death_subjects`,
    `remove_person`) -- no death edge the losers do not have -- and, being dead, does not arrive; a winner at ratio 1
    took none and is untouched. [ASSUMPTION; medium; the entry says "the same engine death rule" and the arm's own rule
    is that a casualty is lethal; killing every winner whatever his ratio would annihilate both sides; revert: every
    winner dies under `total`.] `off` is the field as it was.

    ⚠ v9 IN-13 (#453 §10.4 step 8, THE ARRIVAL): ONE WRITE IS ADDED, AND IT IS PRESENCE, NOT TITLE. On
    `Won` and `Unopposed` every claimant is relocated to the destination (`_relocate`'s pair, keyed on
    the mover: his live `contain` closes, one opens to the target, the target is appended to his
    `travel_leg`), emitting `army.arrived` beside the band's kind; the gate admits another person's
    legs under its `muster` basis (`state/gate.py::may_muster`). The winner's STANCE is
    never written (his BODY is, under CR-24's `engine` arm, above), and no `hold` moves (R-6, β: title moves by `seize`, `give`, `release` or
    death). `Lost` is unchanged: a routed army stays at its origin (R-7).

    ⚠ `Won`/`Lost` NAME THE ATTACKER'S OWN OUTCOME (`seam/ladder.py::field_degree`), NOT WHICH
    SIDE THIS WRITE LANDS ON. `Won` means the DEFENDERS lost; `Lost` means the ATTACKER'S OWN
    claimants lost. Reading both sides off `res.result["parties"]` and picking the loser by
    `res.degree` is the whole of that translation. This is NOT `kill / wound`'s *"the band is
    read off the ACT'S SUBJECT, never off `the loser` as a fixed party"* correction reapplied --
    that correction was about a payload naming ONE person; a field battle genuinely has two
    candidate losing SIDES and `res.degree` already names which one.

    ⚠ THE MAGNITUDE IS READ FROM THE ENGINE, NOT INVENTED, ON `wound_harm_model`'s OWN PRECEDENT.
    `field_casualty_model` (`H-148`) names three arms: `scaled_by_degree` (the default -- each
    loser's body scales by the SAME survivor fraction the engine computed for their whole side,
    `attacker_size_pct`/`defender_size_pct`), `total` (every loser's body to 0 -- the control,
    re-running "losing costs everything" deliberately), `none` (body is not written at all -- the
    second control, isolating the write from the band). The default is settled by Jordan's
    2026-09-04 ruling on `wound_harm_model` -- *"the combat engine determines the result there"*
    -- applied to this magnitude too, not by a fresh measurement; `tools/balance_oracle.py` was
    a campaign-driver instrument and could not observe an `engine/season`-only mechanic (`rosters.yaml`'s
    `field_casualty_models` note).

    ⚠ THE STANCE ROWS FOLLOW THE SEEDED-LOYALTY SHAPE (`harness/data/cast.py`'s own
    `stance_from_loyalty`): a FIXED valence of `-1.0` (both are negative sentiments; the sign is
    not swept) and a WEIGHT that is (`field_morale_weight`/`field_grudge_weight`, `H-148`,
    swept `0`/`1`/`3`). The grudge targets the WINNING faction; the morale hit targets the
    LOSER'S OWN faction -- both re-derived from `a.via` (the office the act was exercised
    through, `seat_of`'s own field) and `world_q.holder_faction_of` on the target rung,
    exactly as `loop/sides.py::sides_of` derives them, because both are facts about the ACT and
    re-deriving them here is cheaper and safer than threading a third value through `Resolution`
    for one reader.

    ⚠ v9 IN-52 (the levy-to-field feed, [ASSUMPTION LF-3]): on `Won` and `Lost` each side's treasury is
    debited by what its field ate (`_ration_debits`, the provider's `provision` key), after the casualties
    and the arrival. The treasuries are NOT re-derived here: they are what the provider bounded the troops
    by, and the debit must land on the store that was read. Empty while `field_provisioning` is off."""
    if res is None or not isinstance(res.result, dict):
        raise Unspecified(
            f"`march` on {_operand(a, 'subject')!r} was folded with no result to read a "
            f"casualty count from", "S39.4/H-98",
            needs="a Resolution from `resolve()`'s seam branch -- the mass_battle provider",
            law="M4 (`ED-IN-0279` clause (a)) -- the magnitude is READ from the engine's own "
                "survivor ratio, never invented here")
    if res.degree == DECLARED:
        return NO_CHANGE
    if res.degree == INVESTED:
        return _siege(w, _operand(a, "subject"))
    parties = res.result.get("parties") or {}
    attackers = list(parties.get("claimants") or [])
    defenders = list(parties.get("subject_members") or [])
    engine_result = res.result.get("result") or {}
    target = _operand(a, "subject")
    # v9 IN-13 (#453 §9.6, THE ARRIVAL): on `Won` and `Unopposed` every claimant is relocated to the
    # destination through `move`'s one journey body (`_relocate`, keyed on the mover), and the band
    # emits `army.arrived` beside its own kind. A claimant ALREADY PRESENT under the destination (an
    # army marching on the settlement it stands in) makes no journey [ASSUMPTION; medium; Jordan to
    # correct; revert: relocate him onto the settlement rung anyway]; a band whose army moves nobody
    # and fells nobody declines (`march.refused`), never a fabricated `army.arrived`.
    # ⚠ `Lost` IS UNCHANGED -- #453 R-7 [ASSUMPTION; medium; Jordan to correct; revert: Jordan
    # states that a routed army arrives, and `test_march.py`'s exit (i) Lost arm is re-pinned]: A
    # ROUTED ARMY STAYS AT ITS ORIGIN. And R-6, carried: a won field writes PRESENCE, never title --
    # β, occupation then `seize` (`_eff_seize`'s Rung half), not α (a won field transferring the
    # hold) [ASSUMPTION; medium; Jordan to correct; revert: Jordan states α, and title moves here].
    arrive = res.degree in (WON, UNOPPOSED)
    # ⚠ THE MOVERS ARE THE CLAIMANTS THE GATE'S `muster` BASIS WILL ADMIT (`state/gate.py::may_muster`
    # and `refuse_unauthored`'s `rehomed`), asked HERE so an act the precondition admitted is never
    # killed at the gate -- `_eff_seize`'s precedent (`may_seize` inside the effect). DEFENSIVE: in the
    # fold `_admits` re-runs at ENCOUNTER and `mustered` is live commit ∩ live contain, so a claimant
    # the seat may not muster, or one with no home to re-home from, is reachable only through a
    # hand-built `Resolution`; he stays where he is. The actor's own legs are `T-m`'s.
    movers = (_not_yet_under(w, attackers, target, a.actor, a.via) if arrive else [])
    attacker_lost = res.degree == LOST
    losers = [] if res.degree == UNOPPOSED else (attackers if attacker_lost else defenders)
    # ED-IN-0306: a side that fought as an order of battle bleeds only where it fought -- the cohorts its troops were
    # drawn from (`parties["fielded"]`, the provider's) -- not everybody who happened to be mustered beside them. A
    # side that fought as a headcount (None) loses all its mustered people, as before.
    drawn = (parties.get("fielded") or (None, None))[0 if attacker_lost else 1]
    if drawn is not None and res.degree != UNOPPOSED:
        losers = list(drawn)             # cohorts do not stand beside their army: they are the people at home
    pct = engine_result.get("attacker_size_pct" if attacker_lost else "defender_size_pct")
    # CP-T04-01 (`field_subunits: person`): the module's record then carries each person's own subunit ratio, and a
    # loser is scaled by HIS, not the side's. A person it does not name (a side fought as an order of battle, or the
    # `side` arm, which carries no `subunits` at all) keeps the side's `pct`, so the `side` arm is today's write.
    per_person = engine_result.get("subunits") or {}
    broke = (engine_result.get("broke_first") or (None, None))[0 if attacker_lost else 1]
    touched = [pid for pid in losers if pid in w.persons]
    model = w.fixtures.get("field_casualty_model")
    require_member(
        model, FIELD_CASUALTY_MODELS, f"field-casualty model {model!r} is not in the roster",
        "H-148", law="`wound_harm_model`'s own precedent -- an unrecognised mode silently "
        "falling back would make every measurement of this sweep read the control")
    winner_arm = w.fixtures.get("field_winner_casualties")
    require_member(
        winner_arm, FIELD_WINNER_CASUALTY_ARMS, f"field-winner-casualties arm {winner_arm!r} is not in the roster",
        "H-360", law="`field_casualty_model`'s own precedent -- an unrecognised arm silently falling back would "
        "make every measurement of this switch read the control")
    # CR-24: THE WINNERS, A SEPARATE LIST -- NEVER `touched` (which feeds the stance rows below), so a winner earns no
    # grudge against his own faction and no morale hit. The winning side is the one `losers` is not; a side that fought as
    # an order of battle bleeds only its drawn cohorts (`fielded`), as the loser does. Each carries his own ratio: his
    # subunit's under `person`, else his side's, capped at 1 (the casualty can only lower a body). A winner with no ratio
    # to read (a hand-built result that carries none) is left unwritten; under `total` only a winner below 1 dies.
    win_ratio: dict = {}                     # winner pid -> his ratio; its keys ARE the winners, in win_side order
    if winner_arm == "engine" and model != "none" and res.degree != UNOPPOSED:
        win_drawn = (parties.get("fielded") or (None, None))[1 if attacker_lost else 0]
        win_side = win_drawn if win_drawn is not None else (defenders if attacker_lost else attackers)
        win_pct = engine_result.get("defender_size_pct" if attacker_lost else "attacker_size_pct")
        loser_set = set(losers)
        for pid in win_side:
            if pid not in w.persons or pid in loser_set or pid in win_ratio:
                continue
            mine = per_person[pid][0] if pid in per_person else win_pct
            if mine is None or (model == "total" and mine >= 1.0):
                continue            # no ratio, no write; under `total` only a winner who took a casualty dies
            win_ratio[pid] = min(1.0, max(0.0, mine))
        if model == "total":
            movers = [pid for pid in movers if pid not in win_ratio]     # a winner the arm kills does not arrive
    debits = _ration_debits(w, res)
    if not touched and not movers and not debits and not win_ratio:
        return NO_CHANGE
    attacker_faction = seat_faction(w, a.via)
    defender_faction = holder_faction_of(w, target)
    winner_faction = defender_faction if attacker_lost else attacker_faction
    loser_faction = attacker_faction if attacker_lost else defender_faction
    if model == "none" and winner_faction is None and loser_faction is None:
        touched = []
        if not movers and not debits:
            return NO_CHANGE
    morale_w = w.fixtures.get("field_morale_weight")
    grudge_w = w.fixtures.get("field_grudge_weight")
    # The fold emits the kinds its subjects EARN (`loop/resolve.py`: an empty `earned` set means
    # *every* declared kind, a non-empty one means *only* those). So the kinds are earned as a whole:
    # with an army that moves, the band publishes both its kind and the arrival; with nobody moving
    # (`Lost`, or a `Won` whose army already stood there), the losers earn the band's own kind alone and
    # no arrival is published. Before CP-T02-01 every subject earned `None` beside a moving army.
    # CP-T02-01 / HR-1: THE SAME RULE WITH EVERY SUBJECT'S KINDS NAMED. `Won` and `Lost` declare
    # `person.died` and `tenure.closed` too, so a subject earning `None` (every declared kind) would
    # publish a death on every fought field; and a dead loser naming `person.died` beside subjects
    # earning `None` would silence the band's kind and the arrival (`_fold` keeps only named kinds once
    # any is named). So a mover earns the band's own kinds (`own_kinds`: the band's kind and the
    # arrival), a loser and a treasury the same beside a moving army and the band's kind alone when
    # nobody moves -- the kinds `None` and `_band_kind` earned before -- and a loser the `total` arm
    # kills earns `person.died` beside them, his seats `tenure.closed` (`death_subjects`).
    own = own_kinds(VERB_TABLE["march"].emits_at(res.degree))
    loser_earns = own if movers else (_band_kind(res.degree),)
    dies = model == "total"

    def perform() -> None:
        _casualties()
        # THE ARRIVAL, AFTER THE CASUALTIES: on `Won` the losers are the defenders, never a mover.
        for pid in movers:
            _relocate(w, a, target, mover=pid)
        # v9 IN-52 [LF-3]: THE FIELD EATS ITS RATION from each side's treasury, last.
        for rid, consumed in debits:
            for kind, units in consumed:
                _debit(w.rungs[rid], kind, units)

    def _casualties() -> None:
        for pid in touched:
            p = w.persons[pid]
            if model == "total":
                p.body = 0
            elif model == "scaled_by_degree":
                mine = per_person[pid][0] if pid in per_person else pct
                p.body = max(1, int(p.body * max(0.0, mine or 0.0)))
            # `none`: the control arm -- body is not written at all.
            rows = list(p.stance or [])
            if winner_faction:
                rows.append((winner_faction, -1.0, grudge_w))
            if loser_faction:
                rows.append((loser_faction, -1.0, morale_w))
            p.stance = rows
            # ⚠ `remove_person` ON THE `total` ARM'S OWN body==0, `_eff_kill`'s PRECEDENT
            # (`_eff_kill` above: "the body goes to 0 ... `w.remove_person(who)`" whenever a write
            # leaves `p.body <= 0`) -- found missing by `/code-review` on the M4 diff. Without it,
            # `total` left a living person recorded at body 0, a state no other path in this
            # engine produces (`_eff_kill` never does), and ED-IN-0279's own first row named
            # `Person.exists` on participants as the recommended option this omitted.
            # `scaled_by_degree` floors at 1 and never reaches this, on `wound_harm_model`'s own
            # precedent that a wound (never total) cannot kill.
            if p.body <= 0:
                w.remove_person(pid)
        # CR-24: the winners' casualty is `body` ONLY -- no stance row (the loop above is the only place one is written).
        for pid in win_ratio:
            p = w.persons[pid]
            p.body = 0 if model == "total" else max(1, int(p.body * win_ratio[pid]))
            if p.body <= 0:
                w.remove_person(pid)       # the `total` arm's own death rule, as the loser's above
    fields = ("stance",) if model == "none" else ("body", "stance")
    # G4 -- WHAT IT NAMES: the losers by the fields the casualty writes (earning as above); the movers
    # WHOLE, `move`'s reason (a `contain` leg is stored on its Person, so his digest carries the legs
    # and `travel_leg`).
    # v9 IN-52: each debited treasury is a subject by its `stores`, earning what the losers earn
    # (`loser_earns`): the band's own kinds beside a moving army, the band's kind alone when nobody
    # moves.
    losers_named = tuple(
        s for pid in touched
        for s in (death_subjects(w, pid, loser_earns, fields=fields) if dies
                  else (Subject.entity("persons", pid, earns=loser_earns, fields=fields,
                                       observed=broke_observed(pid, broke)),)))
    # CR-24: a winner who also moves is ONE Subject -- the mover's, whole-entity -- so only a winner who stays is named
    # here, by `body` alone (the field he is written by); under `total` a dying winner is named by his death.
    movers_set = set(movers)
    winners_named = tuple(
        s for pid in win_ratio if pid not in movers_set
        for s in (death_subjects(w, pid, loser_earns, fields=("body",)) if dies
                  else (Subject.entity("persons", pid, earns=loser_earns, fields=("body",)),)))
    return Change(losers_named + winners_named
                  + tuple(Subject.entity("persons", pid, earns=own) for pid in movers)
                  + tuple(Subject.entity("rungs", rid, earns=loser_earns, fields=("stores",))
                          for rid in dict.fromkeys(rid for rid, _ in debits)), perform)


def _siege(w: "World", target: str) -> Change:
    """CP-T04-06 (`besiege`, AM-C-11): THE `Invested` BAND. Each `garrison` Site in `target`'s subtree loses `_fall(w, site)`
    of its condition -- `sabotage`'s one formula (`loop/effects_economy.py::_fall`: the footroom, taken at the commons'
    share), so a siege and a saboteur are one quantity with one owner. WRITTEN DIRECTLY through the gate, in `perform`: wear
    staged through `World.stage` at ENCOUNTER is never applied (`loop/encounter.py` has no `take_staged`; the accumulator is
    RESOLVE-scoped, `World.stage`). No accumulator, no fixture and no ratio, and nobody is hurt or relocated: no `Person` and
    no `travel_leg` is written. Every fall is read before any is applied, and each Site is its own Subject.

    A SITE THAT WOULD NOT FALL IS NOT NAMED (no condition to lose, or a share that rounds the fall to 0); a subtree with none
    that would declines `NO_CHANGE`, so the band's act is `march.refused`, as a band that moves nobody always has been.
    [ASSUMPTION; medium; Jordan to correct; revert: name every garrison and let the gate's no-op refusal decline it.]"""
    falls = [(s, n) for s in garrison_sites(w, target) if (n := _fall(w, s)) > 0]
    if not falls:
        return NO_CHANGE
    kind = _band_kind(INVESTED)

    def perform() -> None:
        for s, n in falls:
            s.condition = max(0, s.condition - n)
    return Change(tuple(Subject.entity("sites", s.id, earns=kind, fields=("condition",)) for s, _ in falls), perform)


def _ration_debits(w: "World", res: "Resolution") -> list:
    """v9 IN-52 [ASSUMPTION LF-3, delegated-ruled]: WHAT THE FIELD EATS, `[(treasury rung, consumed), ...]`,
    attacker then defender -- the provider's `provision` key (`seam/wrappers/mass_battle.py::resolve`), the
    `settlements.provision` entry's `consumed` beside the treasury it was bounded by. A side with no
    treasury rung, or nothing consumed, is left out. EMPTY WHILE `field_provisioning` IS OFF (shipped): the
    entry consumes nothing on the control arm, so this reads no fixture of its own and the arm has one
    owner. An `Unopposed` march fought no field and its result carries no `provision`."""
    return [(rid, tuple(consumed)) for rid, consumed in (res.result.get("provision") or ())
            if rid is not None and consumed and rid in w.rungs]


def _band_kind(degree: str) -> str:
    """The kind a band names for its OWN outcome: the FIRST of `march`'s `emits[degree]`, by the
    row's declared order (`verb_table.yaml`, `march`'s `emits_note`: the band's kind first, then the
    arrival). Read off the table, so no kind is spelt here."""
    return VERB_TABLE["march"].emits_at(degree)[0]


def _not_yet_under(w: "World", pids: list, target: str, actor: "str | None" = None,
                   via: "str | None" = None) -> list:
    """The claimants in `pids` (in order) who are persons, are NOT already present under `target`, and
    whose journey the gate will admit: present = his live `contain` target and everything above it
    (`world_q.home_of` + `ancestry`, the two owners), and a march on a rung in that chain is no
    journey. `home_of` is read ONCE for the whole band, and only if some claimant is a person; the
    chain is walked once per distinct home.

    ADMITTED = the actor (his own legs are `T-m`'s, home or none), or another person the seat may
    muster (`may_muster`) who HAS a home: the gate's `muster` basis admits only a re-home, a `contain`
    closed AND opened (`refuse_unauthored`'s `rehomed`), so a claimant with no live `contain` has
    nothing to close and the gate would refuse his opening alone. He is left where he is."""
    live = [pid for pid in pids if pid in w.persons]
    if not live:
        return []
    homes = home_of(w)
    chains: dict = {}
    out = []
    # ED-IN-0306 phase 4: what "already there" means is `world_q.occupies`'s, so the two cannot disagree. Beneath a
    # settlement is there; a territory is occupied only AT it, so an army housed in one of its towns still arrives.
    by_subtree = w.rungs[target].kind in SUBTREE_OCCUPATION_KINDS if target in w.rungs else True
    for pid in live:
        here = homes.get(pid)
        if here not in chains:
            chains[here] = ancestry(w, here)
        if target in chains[here] and (by_subtree or here == target):
            continue
        if pid != actor and not (here is not None and may_muster(w, actor, via, pid)):
            continue
        out.append(pid)
    return out


# =================================================================================================
# v9 IN-12 step 9 (#453 §9.4, G15 *the person*): THE TWO ACTS THAT RAISE A PERSON'S OWN STATE --
# `tend` (the body) and `train` (a capability). Here, beside the body's other writers, because `tend`
# is the first path that raises what `fight`, `march` and MATTER only lower, and `train` is its sibling
# on the same G15 row (#453: *'`train` -- axis: field (body vs capability)'*).
# =================================================================================================

@effect_for("tend")
def _eff_tend(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """v9 IN-12 step 9 (#453 §9.4) -- `tend` RAISES THE SUBJECT'S `Person.body` TO THE BODY'S SCALE.

    THE MAGNITUDE IS `restore`'s FORMULA READ ON A BODY (`loop/effects_economy.py::_rise`): the headroom
    to the ceiling -- the person's own `Person.body_ceiling` (v11 CP-T03-07), built at `condition_scale` and lowered
    only by a fight's lasting mark (`_marks`) -- taken whole, because the `share` term is the commons of a fabric and a body has none, and `f(degree)`
    is the identity on an uncontested row (`H-164`). So one tender restores a person whole in one act, as
    one hand raises a fabric to its ceiling [ASSUMPTION; medium; Jordan to correct; revert: a swept
    fixture fraction of the headroom -- #453's *'fast partial and slow full form'*, C-48].

    DECLINES: a subject that is no person (dead, or never one) is `NO_CHANGE` -> `tend.refused`; a body
    already whole is written to itself, which the gate reads as no change (`NoOpReceipt`) -> `tend.refused`.
    Two tenders on one person in one fold: the first restores him, the second moves nothing and is refused
    -- the outcome is the same whichever arrives first."""
    who = _operand(a, "subject")
    p = w.persons.get(who)
    if p is None:
        return NO_CHANGE
    # v11 CP-T03-07: HEALS TOWARD THE PERSON'S OWN CEILING, never `condition_scale`: a marked man is restored to his mark.
    whole = max(p.body, p.body_ceiling)

    def perform() -> None:
        p.body = whole
    return Change((Subject.entity("persons", who, fields=("body",)),), perform)


@effect_for("train")
def _eff_train(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """v9 IN-12 step 9 (#453 §9.4; K-20, K-21) -- `train` RAISES ONE CAPABILITY OF THE SUBJECT BY ONE.

    THE CAPABILITY IS THE VOCATION THE ACT CARRIES on the operand `rosters.yaml: vocation_sourced` names
    for its verb (`kind` for `train`), one Candidate per vocation in `verb_capability`'s range
    (`decision/options.py::opening_set`). ⚠ J-13 ANSWERED (iii) AS THE INTERIM [medium; Jordan to
    correct]: it writes `Person.capability` ONLY WHERE A CASE NAMES A VOCATION -- so the key must be a
    `verb_capability` value (K-20's range: Thread Sensitivity has no carrier, H-85, P-08) and the SUBJECT
    must ALREADY hold it: a key is never minted, because a minted `{copying: 1}` would replace
    `pool_default` and LOWER his pool (`seam/wrappers/sigma.py::faculty`). The ACTOR's own capability is
    NOT read: capability gates nothing (#353 §9.2), here as at formation. ONE whole point, the unit of a
    dice count [ASSUMPTION; medium; Jordan to correct; revert: a swept fixture step].

    DECLINES (`NO_CHANGE` -> `train.refused`): no such subject; a key that is no vocation; a subject who
    holds none in it (a pupil whose case names no vocation)."""
    who = _operand(a, "subject")
    key = _operand(a, VOCATION_SOURCED[a.verb])
    p = w.persons.get(who)
    raised = raised_capability(p, key) if p is not None and key in VOCATIONS else None
    if raised is None:
        return NO_CHANGE

    def perform() -> None:
        p.capability = raised
    return Change((Subject.entity("persons", who, fields=("capability",)),), perform)


# =================================================================================================
# v9 IN-12 step 13 (#453 §9.4, G15 *the person*): `forgive`, THE CLOSER OF WHAT `march` WRITES -- here,
# beside `_eff_march`, the only other runtime writer of `Person.stance`. It shares `march`'s write row and nothing
# else (#453 §9.5): an `own` social act on the actor's own rows, not a contested act on the losers'.
# =================================================================================================

@effect_for("forgive")
def _eff_forgive(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """v9 IN-12 step 13 (#453 §9.4; K-41, K-49) -- `forgive` REMOVES THE ACTOR'S OWN ROWS AGAINST `subject`.

    The rows are `queries/person_q.py::held_against`'s (his own stance rows naming the referent with a
    valence below zero); every other row he holds stays, in order, so `stance_toward(actor, subject)` reads
    0.0 afterwards wherever no positive row names the referent. He writes only his own field (`Person.stance`, by `Subject.entity`; no Tenure is touched, so
    `T-m` is not in play), never another's.

    DECLINES (`NO_CHANGE` -> `forgive.refused`): an actor who is no person; nothing held against the
    referent (#453: *'no negative row -> `NO_CHANGE`'*)."""
    p = w.persons.get(a.actor)
    who = _operand(a, "subject")
    against = held_against(p, who) if p is not None else ()
    if not against:
        return NO_CHANGE
    kept = [row for row in p.stance if row not in against]

    def perform() -> None:
        p.stance = kept
    return Change((Subject.entity("persons", a.actor, fields=("stance",)),), perform)
