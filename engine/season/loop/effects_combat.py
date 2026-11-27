"""`season.loop.effects_combat` -- casualties and morale: fight (renamed from "kill / wound") and
the duel's `accept`, capture, march; and the person raised (v9 IN-12 step 9, G15): tend, train; and the
grudge's closer (v9 IN-12 step 13, G15): forgive.

Holds the two effects that read a
severity off a scene the seam already resolved rather than choosing one (Jordan, 2026-09-04: *"the
combat engine determines the result there. your code just has to accept the result."*) -- personal
combat's `fight` and mass battle's `march`. The moral-layer scar is written by the fold on the
act's OBSERVERS (`loop/resolve.py::_scar_witnesses`), not by an effect. See `effects_shared.py` for `effect_for`
and `_operand`, the helpers `march` takes from `effects_shared.py`; its arrival also calls
`effects_migration.py::_relocate`, the journey `move` shares (v9 IN-13).
"""

from __future__ import annotations

from dataclasses import replace

from engine.dice_engine.dice_engine import Degree, degree_from_net
from engine.dice_engine.sigma_leverage import levels_to_net_sigma, pool_of
from engine.substrate import composition, descriptors

from ..data.rosters import (
    DECLARED, DRAWN, ENDING_FELLED, ENDING_PREVAILED, ENDING_UNDECIDED, ENDING_YIELDED, FELLED, FIELD_CASUALTY_MODELS, FIELD_WINNER_CASUALTY_ARMS, INVESTED, LOST, SUBTREE_OCCUPATION_KINDS, UNOPPOSED, UNTOUCHED, WON,
    WOUND_HARM_MODELS, BODY_MARK_MODELS, require_member,
)
from ..data.matrix import matrix_row
from ..data.requires import Observation
from ..data.verbs import VERB_CAPABILITY, VERB_TABLE, VOCATION_SOURCED, VOCATIONS
from ..gaps import Unspecified
from ..queries.person_q import HAND_PREDICATE, held_against
from ..queries.world_q import (
    BODY_STEM, DETAIN_KIND, ancestry, garrison_sites, holder_faction_of, home_of, issuing_seat, restrained, warrants_for,
)
from ..seam.ladder import party_degree
from ..seam.wrappers.pool import pool_pair, untrained
from ..seam.wrappers.sigma import ADVANTAGE_SOURCES, WOUNDS
from ..state.carriers import Tenure
from ..state.gate import (
    NO_CHANGE, PERSON_DIED, Change, Subject, death_subjects, may_muster, may_warrant, own_kinds, seat_faction,
)
from ..state.ids import H, draw_factory

from .effects_economy import _fall
from .effects_information import _may_close_custody
from .effects_migration import _relocate
from .effects_shared import _debit, _operand, _scaled, effect_for


# `accept` (the duel pair's second half) is the same contest over the same prize, `contests: "the
# body"`, with the same degree-keyed writes read off the same scene: one effect registered twice.
# The fold's scar reads `a.verb`, so a duel's moral layer reads `accept`'s own alignment cells. (`challenge`
# writes nothing and needs no effect: `VerbRow.effect_carried`.) `fight` was RENAMED from
# "kill / wound" (plan `FIGHT-RENAME`); only the `EFFECTS` key and its row moved.
CAPTURED = "person.captured"        # the one kind `capture`'s opened `detain` earns (`verb_table.yaml`'s `capture` row)
DUEL_YIELDED = "duel.yielded"       # v10 PC-10b: the kind a duel's yielder earns (`verb_table.yaml`'s `accept` row)
CEILING = "body_ceiling"          # v11 CP-T03-07: the cell the lasting mark writes (`write_matrix.yaml`)


def _yielder(res: "Resolution") -> "str | None":
    """THE PARTY THE SCENE'S `surrender` NAMES (`modules/combat/fight.py::_surrender`, lifted onto the result), or
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
    THE NO-OP THIS MAKES VISIBLE: a `Wounded` outcome under `scene_fraction` whose fraction
    rounds back to the body it started from (`max(1, body * left // full)` at `body == 1`, or a
    scene that took no health) is `kill.refused`, not `body.changed` over an unchanged body.

    ⚠ AND THE TWO `Unspecified` RAISES COME BEFORE ANYTHING IS WRITTEN: both are read while the
    `Change` is built, which touches nothing.

    ⚠ THE TENURE ENDS THROUGH THE DEATH, which is §15.3's rule and the reason this is ONE effect
    rather than three writes a caller sequences: "a plague that kills the praefect ends his
    tenure THROUGH THE DEATH; A STORM CANNOT TOUCH IT." A wound that does not kill writes only
    the band, so the same verb covers both -- which is why the table's row is `kill / wound`.

    ⚠ `W-E`: THE EFFECT TAKES THE RESOLUTION, AND THERE IS NO `harm` OPERAND (`H-114`): an effect
    that read `harm` with the person's ENTIRE body as its fallback would, at degree `Wounded`,
    reach `p.body == 0`, pass `if p.body > 0`, and DELETE THE PERSON.
    ⚠ THE `harm` SPELLING IS DELIBERATELY NOT QUOTED IN THIS DOCSTRING: `W-C`'s guard
    (`test_wc_no_operand_is_defaulted_by_a_get_or_setdefault_in_shape_py_outside_eff_kill`) scans
    RAW SOURCE TEXT, so quoting it would keep a carve-out "used" and leave an open licence on the
    name `harm`.

    WHERE THE MAGNITUDE COMES FROM NOW, AND WHY IT IS NOT INVENTED. JORDAN, 2026-09-04, VERBATIM:
    *"the combat engine determines the result there. your code just has to accept the result."*
    So the harm is not a number this file chooses: it is the LOSS THE SCENE ALREADY COMPUTED, on
    the engine's own `WoundTracker`, read as the fraction of the subject's health the fight left
    standing. No constant is introduced by the default arm -- a fraction needs none, which is
    exactly why it is the default and the other two arms are the sweep.

    THE THREE ARMS (`wound_harm_model`, registered at `H-123`, injected at `DEFAULT_FIXTURES`):
      `scene_fraction`  body <- body x health_remaining / health_full. The scene decides.
      `total`           any wound is lethal. ⚠ THIS IS THE CONTROL: it is the arm that shows what
                        the degree is worth.
      `none`            a wound writes nothing. The fold's own write-nothing guard then emits the
                        REFUSAL rather than the success -- the second control, and it isolates
                        "the band selected a different write set" from "the band changed a value".

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
    # seam; an act folded without one has no scene to read a severity off, and killing would invent one.
    # `writes_at(None)` already refuses one line earlier for the same
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
    # `wound_harm_model`; `Untouched` -> nothing. A party who is no
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
        # ⚠ `w.tenures`, NOT `p.tenures + w._unowned`: `p.tenures` is the tenures this person is the
        # SUBJECT of (§15.1 -- a Tenure is owned by its subject), so a scan of it cannot see an edge
        # ANOTHER PERSON owns that names the dead one as its OBJECT, which would DANGLE once
        # `remove_person` deletes the person it points at. §15.3: the tenure ends THROUGH THE
        # DEATH. `w.tenures` is owner-first over every person plus `_unowned`. The cascade lives in
        # `World.remove_person` because MATTER is a SECOND way to die (a body reaching 0 from an
        # empty larder), and two sites closing tenures by hand is how the two drift apart (§8).
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
    # CP-T03-00: A FELLED PARTY EARNS THE DEATH'S KINDS ALONE. The `Felled` cell's
    # `body.changed` is there for the OTHER party of a mixed fight -- the cell is the ACT's band, the
    # worst over both, so it must license what a Wounded party earns beside a felled one -- and is not
    # the felled man's own kind. And because `_fold` gives each kind's Event only its earners' changes,
    # the person.died Event of a felled actor names him, never the standing subject.
    # v10 PC-10b: `duel.yielded` IS EARNED BY THE YIELDER ALONE -- the party the scene's `surrender`
    # (`modules/combat/fight.py::_surrender`, lifted off the trace) names. A band declaring it (`accept`'s
    # `Wounded`) would otherwise hand it to every wounded party, a yield nobody made (ID-9). Read off the
    # result, never the verb: a row whose band does not declare the kind emits nothing of it (`_fold`).
    yielder = _yielder(res)
    ending = fight_ending(w, (a.actor, who), res, above)      # read once, before the write: the Change's and `hand_observed`'s
    named: tuple = ()
    for pid, band in bands.items():
        own = () if band == FELLED else own_kinds(row.emits_at(band))
        own = tuple(k for k in own if (k != DUEL_YIELDED or pid == yielder) and k not in GROWN_KINDS)
        if bodies[pid] == 0:
            # B14.03: THE FELLED PARTY'S OWN SUBJECT (the first `death_subjects` names; the seats follow) carries the
            # wound that felled him, a source and a weapon and no doer, on the death Event WITNESS deposits.
            dead = death_subjects(w, pid, own, fields=("body",))
            # B14.16: A FELLED ACTOR'S death also names the party left standing (`hand_observed`).
            named += (replace(dead[0], observed=fell_observed(pid, res.result.get("beat"))
                              + hand_observed(pid, a.actor, ending)),) + dead[1:]
            continue
        # CP-T03-02 (ii): A WOUNDED PARTY'S SUBJECT CARRIES WHAT HIS BODY NOW IS -- `(pid, "body", v)`, `v` the
        # value `perform` WRITES (`bodies`), never `w.persons[pid].body` read here, which is the pre-fight body
        # (the item's mutation). It rides each Event this subject earns (`body.changed`; a yielder's
        # `duel.yielded`), so WITNESS deposits it as it deposits `stores:<kind>` and `condition`: by the shipped
        # `observation_deposit_mode` (`actor`: the act's actor alone), no new channel. A `none`-model party
        # (`bodies[pid] is None`) writes nothing and observes nothing.
        # [ASSUMPTION; medium; Jordan to correct; revert: the field and the Observation]
        named += (Subject.entity("persons", pid, earns=own, fields=(BODY_STEM, CEILING),
                                 observed=body_observed(pid, bodies[pid]) + marked_observed(w, pid, marks)),)
    # CP-T03-04 (iv): EACH GROWN PARTY IS ITS OWN SUBJECT ON `capability`, earning the `(Person, capability)` cell's
    # kind alone -- never a body subject's kind, and never on a party who did not grow (the filter above).
    named += tuple(Subject.entity("persons", pid, earns=GROWN_KINDS, fields=("capability",)) for pid in grown)
    # B14.15: THE SCENE'S SHAPE rides each success Event once (`scene_observed`, `carry_scene`).
    named = carry_scene(named, scene_observed(tuple(dict.fromkeys((a.actor, who))), res.result.get("shape")))
    return Change(named, perform, ending)


# CP-T03-04 (iv): THE KINDS A GROWN PARTY EARNS -- the `(Person, capability)` matrix row's own `emits:`
# (`write_matrix.yaml`), `train`'s kind, read off its owner rather than spelt.
GROWN_KINDS = matrix_row("Person", "capability").emits


def raised_capability(p: "Person", key: str) -> "dict | None":
    """`p.capability` with `key` raised by ONE whole point, the unit of a dice count -- `_eff_train`'s write and
    `_grown`'s, one body.

    B05.09 (CORE Edit 9) -- A FIRST RANK IS MINTED: a person who holds no `key` is written `{key: 1}`, and his opposition
    and his fight score do not move, because `pool.score` is `max(untrained score, rank)`: a rank below `pool_default` gives no dice and takes
    none there. HIS SOCIAL POOL DOES GAIN A DIE (`pool.faculty` adds the raw rank: "a first rank always adds a die"; B05 close, K4). The rule that kept
    a key from being minted, `{arms: 1}` replacing `pool_default`, no longer holds. [ASSUMPTION; medium; Jordan
    to correct; revert: restore the never-minted rule, `None` for a key `p` does not hold].

    B04.15 -- A RANK NEVER PASSES ITS ROW'S CEILING: `None` where the raised rank would pass
    `descriptors.capability(key).ceiling`, the ceiling of the skill row's `scale` (7 for every row shipped); a rank at its
    ceiling is not raised, by `train` or by `_grown`."""
    held = p.capability or {}
    raised = int(held[key]) + 1 if key in held else 1
    if raised > descriptors.capability(key).ceiling:
        return None
    return {**p.capability, key: raised}


def _grown(w: "World", a: "Act", parties, bands: dict, bodies: dict) -> dict:
    """v11 CP-T03-04 (iv), BUILD-BY-DOING: `{pid: raised capability}` for each party of a fight THAT DREW BLOOD (some
    party `Wounded` or `Felled`, i.e. `bands` is not empty) who SURVIVES it (his written body is not 0), for the key the verb draws on (`VERB_CAPABILITY[a.verb]`, derived from the verb table's `capability:` column over `descriptors.CAPABILITIES` -- `arms` for the
    three verbs contesting `the body`; the name is read there, never spelt here). Raised by ONE whole point,
    `_eff_train`'s unit.

    ⚠ A FIRST RANK IS MINTED (B05.09, `raised_capability`): a surviving party who holds no `arms` key is written `{arms: 1}`,
    and his opposition and fight score do not move (`pool.score` is `max(untrained score, rank)`); his social pool gains a die (`pool.faculty` adds the raw rank).
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
    """CP-T04-01, B17.03: the Observation the person whose part BROKE FIRST on his side carries on the field's band Event --
    `(pid, "broke", True)` -- or `()` for every other person and for a side that names nobody (the `side` arm, or a side
    whose units did not break on their own account). Written for BOTH sides (`SideOutcome.broke_first`), the winning side's too.
    An Event carries no payload (`Event.ending`'s note), so the cause rides `Event.observed`, deposited by WITNESS as
    `body_observed` is. It is a named predicate (`BROKE_STEM`), NOT a member of `rosters.yaml: observation_terms`, which is
    `epistemic.Seen`'s field list (`FELL_TO_STEM`'s precedent below). [ASSUMPTION; medium; Jordan to correct;
    revert: the Observation, and the field's cause is unnamed]"""
    return (Observation(pid, BROKE_STEM, True),) if pid == broke else ()


FELL_TO_STEM = "fell_to"


def fell_observed(pid: str, beat: "dict | None") -> tuple:
    """B14.03 (D-U1-06, C3-L5): the Observation a felled party's Subject carries -- `(pid, "fell_to", "<source>:<weapon>")`,
    read off the scene's `DecisiveBeat` (lifted onto the result as a dict) -- or `()` where the scene names no beat or the
    beat's victim is another party. It names the engine's site of the wound and the weapon, NEVER the striker (`beat["by"]`
    is not read): a deed others can hold without a doer. An Event carries no payload, so the cause rides `Event.observed`
    as `broke_observed`'s does. [ASSUMPTION; medium; Jordan to correct; revert: drop the Observation]"""
    if not beat or beat.get("victim") != pid:
        return ()
    return (Observation(pid, FELL_TO_STEM, f"{beat['source']}:{beat['weapon']}"),)


def hand_observed(pid: str, actor: str, ending: tuple) -> tuple:
    """B14.16 (D-U1-06; `16_PESSIMIST_PC_C` 2): the Observation a felled party's Subject carries where he is the act's ACTOR --
    `(pid, "fell_to_hand", <the party left standing>)` -- or `()` for a felled subject (the `seen.who` pairing names the actor his
    killer there), and where no party prevailed (both felled; a yield). `ending` is `fight_ending`'s `(party, ending)` pairs;
    the standing party is the one it reads `prevailed`, the scene's own verdict, so no second reading of the bands is made here.
    Unlike `fell_to` it NAMES A PERSON: `queries/person_q.py::deed_doer` reads it before the pairing, which cannot name the
    killer of an attacker felled by his target (it sees the attacker as `who` of his own death). It rides `Event.observed` as
    `fell_to` does, and which witness holds it is WITNESS's mode, not a filter here. [ASSUMPTION; medium; Jordan to correct;
    revert: drop the Observation and `deed_doer`'s read]"""
    if pid != actor:
        return ()
    standing = [p for p, e in ending if e == ENDING_PREVAILED and p != pid]
    return (Observation(pid, HAND_PREDICATE, standing[0]),) if len(standing) == 1 else ()


# B14.15's four scene predicates, spelt once here (the writer) and read by `harness/chronicle.py`; none is an `observation_terms` member.
BLOWS_LANDED, FIGHT_ROUNDS, FIRST_BLOOD, LEAD_CHANGES = "blows_landed", "fight_rounds", "first_blood", "lead_changes"


def scene_observed(parties: tuple, shape: "dict | None") -> tuple:
    """B14.15 (D-U1-06; `16_PESSIMIST_PC_C` 1): the Observations a fight's success Events carry of the scene's course, read off
    the `shape` the seam lifted onto the result (`SceneShape` as a dict), or `()` where the result carries none. For each party
    `p`, `(p, "blows_landed", n)`; once per scene, `(actor, "fight_rounds", n)`, `(first_blood, "first_blood", True)` where a
    blow landed, and `(actor, "lead_changes", n)` -- `parties[0]` the actor. Numbers and one name, never a doer of a killing:
    `first_blood` names who struck first, which is not who prevailed. They ride `Event.observed` as `fell_to` does (the
    predicates are not `observation_terms` members, B14.03's reading). [ASSUMPTION; medium; Jordan to correct; revert: drop
    the Observations]"""
    if not shape:
        return ()
    blows = shape.get("blows") or {}
    actor = parties[0]
    out = [Observation(p, BLOWS_LANDED, blows[p]) for p in parties if p in blows]
    out.append(Observation(actor, FIGHT_ROUNDS, shape["rounds"]))
    if shape.get("first_blood") is not None:
        out.append(Observation(shape["first_blood"], FIRST_BLOOD, True))
    out.append(Observation(actor, LEAD_CHANGES, shape["lead_changes"]))
    return tuple(out)


def carry_scene(named: tuple, obs: tuple) -> tuple:
    """`named` with `obs` placed on the subjects so that each success Event carries them ONCE. `_fold` gives a kind's Event the
    `observed` of every subject riding it, and a subject rides the kinds it earns (every kind, where it names none), so `obs` goes
    to a subject only if none of its kinds is already ridden by an earlier one that carries them: a kind two subjects earn
    (both parties wounded) carries them once, and a subject that would double a covered kind is passed over (its other kind
    is left without them, for the sake of no repeated Observation)."""
    if not obs:
        return named
    everything, covered, out = object(), set(), []
    for s in named:
        kinds = set(s.kinds) or {everything}
        fresh = not (covered & kinds) and everything not in covered and (everything not in kinds or not covered)
        out.append(replace(s, observed=tuple(s.observed) + obs) if fresh else s)
        covered |= kinds
    return tuple(out)


def fight_ending(w: "World", parties, res: "Resolution", above) -> tuple:
    """CP-T03-02 (i): `Event.ending` -- `(pid, felled | yielded | prevailed | undecided)` for each party still a person,
    in party order, read off the scene's lifted `wound_state` (`party_degree`, the walk `_eff_kill` writes by) and
    `surrender` (`_yielder`). Read BEFORE the write, which is right: it reports the scene, not the world.

    B14.02 (A-81, D-U1-11a): a party who is neither felled nor the yielder is `prevailed` where the OTHER party is felled or
    the yielder -- the one left standing -- and `undecided` only where neither is. A party is read down from the scene
    whether or not he is still a person, so a felled opponent already removed from the world still makes the survivor
    `prevailed`. [ASSUMPTION; medium; Jordan to correct; revert: the field and the Observation]"""
    states = res.result.get("wound_state") or {}
    yielder = _yielder(res)
    held = tuple(dict.fromkeys(parties))
    felled = {pid: party_degree(states.get(pid), above) == FELLED for pid in held}
    down = {pid: felled[pid] or pid == yielder for pid in held}
    out = []
    for pid in held:
        if pid not in w.persons:
            continue
        out.append((pid, ENDING_FELLED if felled[pid]
                    else ENDING_YIELDED if pid == yielder
                    else ENDING_PREVAILED if any(down[o] for o in held if o != pid) else ENDING_UNDECIDED))
    return tuple(out)


@effect_for("capture")
def _eff_capture(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """CP-T03-09 (`-08` AM-C-03): `fight`'s WOUNDS, AND THE BEATEN MAN TAKEN INTO A SEAT'S CUSTODY WHERE THE SCENE
    ENDED IN HIS YIELD. A named fold of `fight`, not a second fight: `_eff_kill` is called and its `Change` is the
    base (each party written by his own band, `seam/ladder.py::party_degree`), to which ONE `detain` EDGE is added,
    the captive (the act's `subject`) -> THE COURT WHOSE WARRANT IT IS: custody goes to the court whose warrant it is,
    `arrest`'s rule, one owner (B29.02, `14_VERBS_PHYSICAL_A` A2): the issuing seat (`issuing_seat`) of the first warrant
    the actor holds or was addressed and heard of (`world_q.warrants_for`) naming him whose seat's holder could close the
    custody (`_may_close_custody`). Where no such warrant stands -- a capture in war, or on a man no warrant names -- it is the
    seat the act is exercised through (`Act.via`), as before (PC-10b's challenge Record is `accept`'s, not `capture`'s).

    WHAT LICENSES THE EDGE, EACH ONE OWNER OF ITS RULE (`_eff_arrest`'s tests, minus the warrant): (1) the scene's
    `surrender` (`modules/combat/fight.py::_surrender`, lifted off the trace) names the SUBJECT as the one who
    yielded -- a yield by the actor, or none, opens nothing, and a scene in which either party was felled opens
    nothing (a felled actor holds no seat to take him into); (2) the subject is a person other than the actor and
    not already in custody (`restrained`, one live `detain` per prisoner); (3) the exercised seat may take him
    (`may_warrant`, the gate's own predicate) AND the seat the custody goes to (above) has a live holder who could close it
    (`_may_close_custody`, `pardon`'s basis), so an act the precondition admitted is never killed at the gate and a custody nothing could
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
    # (`NotYours`); the fold catches that and emits the row's refusal (B03.76), which would refuse the whole
    # act; returning `base` keeps the capture.
    if any(PERSON_DIED in s.kinds for s in base.subjects) or restrained(w, prisoner, DETAIN_KIND):
        return base
    if a.via is None or not may_warrant(w, a.actor, a.via, prisoner):
        return base
    # B29.02 (`14_VERBS_PHYSICAL_A` A2 [ASSUMPTION; medium; Jordan to correct; revert: `seat = a.via`]): CUSTODY GOES TO THE COURT WHOSE WARRANT IT IS --
    # `_eff_arrest`'s rule (the issuing seat of the first warrant `warrants_for` reads whose holder could close the custody), read here and not
    # re-decided; with no such warrant it is the seat the act is exercised through, as before.
    seat = next((s for s in (issuing_seat(w, rid) for rid in warrants_for(w, a.actor, prisoner))
                 if s is not None and _may_close_custody(w, s, prisoner)), None)
    if seat is None:
        seat = a.via
        if not _may_close_custody(w, seat, prisoner):
            return base
    nt = Tenure(H(w.world_seed, w.tick, prisoner, f"detain:{seat}:{a.id}"), prisoner, seat, "detain",
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


MARKED_STEM = "marked"
MARK_ROLE = "combat.resolve"                    # the composition row whose module rolls the mark: `roll_net + net_boost`, one owner
QUERY_ENTRIES = ((MARK_ROLE, "query"),)         # the host's declared need, held at driver construction (`registrar.require_entries`)


def marked_observed(w: "World", pid: str, marks: dict) -> tuple:
    """B14.23: the Observation a DRAWN mark carries -- `(pid, "marked", the ceiling it left)` -- or `()` where no mark fell on `pid`, and at every arm but
    `drawn` (`deepest_gate` and `none` tell no mark, so the shipped arm's Events are the pre-item ones). Rides `Event.observed` as `broke` and
    `fell_to` do: an Observation predicate is not a member of `rosters.yaml: observation_terms`, which is `epistemic.Seen`'s field list."""
    if pid not in marks or w.fixtures.get("body_mark_model") != "drawn":
        return ()
    return (Observation(pid, MARKED_STEM, marks[pid]),)


def _mark_degree(w: "World", pid: str, body: int, ceiling: int) -> Degree:
    """B14.23 (`U5b_PC_residue` section 7; A-5 to A-8, A-30): THE BAND OF ONE SURVIVOR'S MARK ROLL. The pool is the one pool rule on the
    untrained default -- `pool_of(pool_default, 0, pool_add, pool_floor)`, no skill being authored for mending clean -- and his body band enters as
    LEVELS through the `wounds` source (`ADVANTAGE_SOURCES[WOUNDS]`, the roller's own wound against him, as `combat._carried_of` reads it), summed by
    `levels_to_net_sigma` and applied as `net_boost`, never a die and never an obstacle term. The roll is the module's (`combat.resolve`, reached by role: `roll_net_continuous` plus `net_boost`, the one sampler); the
    obstacle is the fixture `mark_ob`, graded on the one ladder (`degree_from_net`). The stream is the survivor's own, keyed
    `(world_seed, tick, victim, "fight.mark")` (`state.ids.draw_factory`, A-30): never a position in the scene's stream and never the season's draw,
    so the roll reads `World` and writes nothing. [ASSUMPTION; medium; Jordan to correct; revert: `body_mark_model: deepest_gate`]"""
    fx = w.fixtures
    add, floor = pool_pair(fx)
    pool = pool_of(untrained(fx), 0, add, floor)
    _for, against = ADVANTAGE_SOURCES[WOUNDS](fx, {"body": body, "body_ceiling": ceiling})
    sigma = levels_to_net_sigma(_for, against)
    rng = draw_factory(w.world_seed, lambda: w.tick)(pid, "fight.mark")
    ob = fx.get("mark_ob")
    return degree_from_net(composition.require(MARK_ROLE)(pool, sigma, rng, ob)[1], ob)


def _marks(w: "World", bodies: dict, states: dict) -> dict:
    """v11 CP-T03-07: `{pid: new body_ceiling}` for each party of a fight who SURVIVES it (his written body is above 0;
    a `none`-arm party, written nothing, is not marked) at the engine's DEEPEST GATE SHORT OF FELLING -- `wounds >=
    max_wounds` on his lifted tracker (`rosters.yaml: wound_quantities`) -- and whose ceiling the mark lowers
    (`marked_ceiling`). `body_mark_model: none` (`H-258`, the control) marks nobody.
    `drawn` (B14.23, `H-567`; not shipped): each such survivor rolls ONCE (`_mark_degree`, keyed `fight.mark`) and Failure lowers the ceiling
    twice (`marked_ceiling` applied twice), Partial once as `deepest_gate` does, Success and better not at all.
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
        if mode == "drawn":
            degree = _mark_degree(w, pid, body, p.body_ceiling)
            if degree in (Degree.SUCCESS, Degree.OVERWHELMING):
                continue
            if degree is Degree.FAILURE:
                after = marked_ceiling(after, floors)
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

    ⚠ B17.03 (THE FIELD'S TYPED OUTCOME): the magnitude is read off the module's frozen `FieldOutcome` (`res.result["result"]`), each
    share an integer on `condition_scale` (a body is cut `body x share // scale`, exact: a side the battle never touched reads the
    scale and loses nothing). A person the side's `parts` name -- a member of the `person` arm, a cohort of an army -- is cut by HIS
    part's share, anyone else by the side's; `broke_observed` rides the part that broke first on each side, winners' too.

    ⚠ CR-24 (`field_winner_casualties`, `H-360`, M4 Ask B (b)): UNDER `engine` (SHIPPED) THE WINNERS TAKE THEIR OWN
    ENGINE CASUALTIES, ON `body` ONLY -- each winner at his own side's share (`SideOutcome.share`) or, where the side's `parts`
    name him, his own part's, never the loser's, and never above the scale (a winner is not raised). A winner is NOT a loser: he is not appended to `touched`,
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

    ⚠ B17.01 (A-67, A-68, A-70, A-80, A-81), `Drawn`: A FIELD IN WHICH BOTH SIDES ARE OUT OR NEITHER IS HAS NO LOSER. Every member
    of both sides (or the drawn cohorts of a side that fought as an order of battle) has his `body` scaled by his own side's, or
    his own subunit's, share under `field_casualty_model` exactly as a winner's is above (`win_share` holds them), and the ration is debited
    as on `Won` and `Lost`. No stance row is written, and nobody is relocated: a drawn army stands at its station, the
    aggressor where the march began and the defender at its own base, so there is no journey for `_relocate` to write (it
    would only close a `contain` edge and open another at the same place). The winners' arm `field_winner_casualties` is the
    winner's switch and a drawn field has none, so it does not gate this write. The fatigue half of A-69 is `27_MB_E`'s (B22).

    ⚠ THE MAGNITUDE IS READ FROM THE ENGINE, NOT INVENTED, ON `wound_harm_model`'s OWN PRECEDENT.
    `field_casualty_model` (`H-148`) names three arms: `scaled_by_degree` (the default -- each
    loser's body scales by the survivor fraction the engine computed for his part, else for his whole side,
    `SideOutcome.share` over `condition_scale`), `total` (every loser's body to 0 -- the control,
    re-running "losing costs everything" deliberately), `none` (body is not written at all -- the
    second control, isolating the write from the band). The default is settled by Jordan's
    2026-09-04 ruling on `wound_harm_model` -- *"the combat engine determines the result there"*
    -- applied to this magnitude too, not by a fresh measurement (`rosters.yaml`'s
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
    # B17.03: the module's frozen `FieldOutcome`, `None` where no field was fought (`Unopposed`; `Invested` returned above).
    outcome = res.result.get("result")
    if outcome is None and res.degree != UNOPPOSED:
        raise Unspecified(
            f"`march` on {_operand(a, 'subject')!r} was folded as {res.degree!r} with no field outcome to read a casualty from",
            "S39.4/H-98", needs="a `FieldOutcome` under `Resolution.result['result']` (the mass_battle provider's)",
            law="B17.03 -- the magnitude is READ from the engine's own outcome, never invented here")
    sides = (None, None) if outcome is None else (outcome.attacker, outcome.defender)
    scale = w.fixtures.get("condition_scale")
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
    drawn_field = res.degree == DRAWN
    losers = [] if res.degree in (UNOPPOSED, DRAWN) else (attackers if attacker_lost else defenders)
    # ED-IN-0306: a side that fought as an order of battle bleeds only where it fought -- the cohorts its troops were
    # drawn from (`parties["fielded"]`, the provider's) -- not everybody who happened to be mustered beside them. A
    # side that fought as a headcount (None) loses all its mustered people, as before.
    drawn = (parties.get("fielded") or (None, None))[0 if attacker_lost else 1]
    if drawn is not None and res.degree not in (UNOPPOSED, DRAWN):
        losers = list(drawn)             # cohorts do not stand beside their army: they are the people at home
    loser_side = 0 if attacker_lost else 1

    def share_of(side_ix: int, pid: str) -> int:
        """B17.03: the share (an integer on `scale`) a person is cut by -- his own part's where his side's `parts` name him (a
        member of the `person` arm, a cohort of an army), else his side's. The `side` arm names no part, so it is the side's
        one share for everyone, as it was."""
        side = sides[side_ix]
        return next((part.share for part in side.parts if part.id == pid), side.share)

    # B17.03: the part that broke first on EACH side (`SideOutcome.broke_first`), whichever side lost: `broke_observed` rides it.
    side_broke = tuple(None if side is None else side.broke_first for side in sides)
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
    # an order of battle bleeds only its drawn cohorts (`fielded`), as the loser does. Each carries his own share: his part's
    # (a person the side names, or a cohort), else his side's, an integer on `scale` so a winner is never raised. Under `total`
    # only a winner who took a casualty (his share below the scale) dies.
    win_share: dict = {}                     # pid -> his share; its keys ARE the winners (both sides, on `Drawn`), in side order
    win_side: dict = {}                      # pid -> which side he is on (0 the attacker's, 1 the defender's), for `broke_observed`
    fielded = parties.get("fielded") or (None, None)
    if drawn_field:
        # B17.01: nobody lost, so both sides are written as a winner is, each by its own share.
        take = ((0, fielded[0] if fielded[0] is not None else attackers),
                (1, fielded[1] if fielded[1] is not None else defenders))
    elif winner_arm == "engine" and res.degree != UNOPPOSED:
        win_ix = 1 - loser_side
        win_drawn = fielded[win_ix]
        take = ((win_ix, win_drawn if win_drawn is not None else (attackers if win_ix == 0 else defenders)),)
    else:
        take = ()
    if model != "none":
        loser_set = set(losers)
        for side_ix, win_side_pids in take:
            for pid in win_side_pids:
                if pid not in w.persons or pid in loser_set or pid in win_share:
                    continue
                mine = share_of(side_ix, pid)
                if model == "total" and mine >= scale:
                    continue            # under `total` only a winner who took a casualty dies
                win_share[pid], win_side[pid] = min(scale, max(0, mine)), side_ix
    if model == "total":
        movers = [pid for pid in movers if pid not in win_share]     # a winner the arm kills does not arrive
    debits = _ration_debits(w, res)
    if not touched and not movers and not debits and not win_share:
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
    # no arrival is published.
    # CP-T02-01 / HR-1: THE SAME RULE WITH EVERY SUBJECT'S KINDS NAMED. `Won` and `Lost` declare
    # `person.died` and `tenure.closed` too, so a subject earning `None` (every declared kind) would
    # publish a death on every fought field; and a dead loser naming `person.died` beside subjects
    # earning `None` would silence the band's kind and the arrival (`_fold` keeps only named kinds once
    # any is named). So a mover earns the band's own kinds (`own_kinds`: the band's kind and the
    # arrival), a loser and a treasury the same beside a moving army and the band's kind alone when
    # nobody moves, and a loser the `total` arm
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
                # B17.01: capped as the winner's is, a loss never raises; B17.03: exact integer arithmetic on the body scale
                p.body = max(1, int(p.body) * min(scale, max(0, share_of(loser_side, pid))) // scale)
            # `none`: the control arm -- body is not written at all.
            rows = list(p.stance or [])
            if winner_faction:
                rows.append((winner_faction, -1.0, grudge_w))
            if loser_faction:
                rows.append((loser_faction, -1.0, morale_w))
            p.stance = rows
            # ⚠ `remove_person` ON THE `total` ARM'S OWN body==0, `_eff_kill`'s PRECEDENT (whenever a
            # write leaves `p.body <= 0`): without it `total` would leave a living person recorded at
            # body 0, a state no other path in this engine produces, and ED-IN-0279's own first row
            # named `Person.exists` on participants. `scaled_by_degree` floors at 1 and never reaches
            # this, on `wound_harm_model`'s own precedent that a wound (never total) cannot kill.
            if p.body <= 0:
                w.remove_person(pid)
        # CR-24: the winners' casualty is `body` ONLY -- no stance row (the loop above is the only place one is written).
        for pid in win_share:
            p = w.persons[pid]
            p.body = 0 if model == "total" else max(1, int(p.body) * win_share[pid] // scale)
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
                                       observed=broke_observed(pid, side_broke[loser_side])),)))
    # CR-24: a winner who also moves is ONE Subject -- the mover's, whole-entity -- so only a winner who stays is named
    # here, by `body` alone (the field he is written by); under `total` a dying winner is named by his death.
    movers_set = set(movers)
    winners_named = tuple(
        s for pid in win_share if pid not in movers_set
        for s in (death_subjects(w, pid, loser_earns, fields=("body",)) if dies
                  else (Subject.entity("persons", pid, earns=loser_earns, fields=("body",),
                                       observed=broke_observed(pid, side_broke[win_side[pid]])),)))
    return Change(losers_named + winners_named
                  + tuple(Subject.entity("persons", pid, earns=own, observed=broke_observed(pid, side_broke[0]))
                          for pid in movers)
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
    only by a fight's lasting mark (`_marks`) -- taken whole at a full band, because the `share` term is the commons of a fabric and a body has none, and
    `f(degree)` is `rosters.yaml: task_fraction`'s share of it (B07.02, `H-164`; the identity with no band, share 1; a share whose floored headroom is
    nothing writes the body to itself, which the gate reads as no change -> `tend.refused`). So one tender restores a person whole in one act, as
    one hand raises a fabric to its ceiling [ASSUMPTION; medium; Jordan to correct; revert: a swept
    fixture fraction of the headroom -- #453's *'fast partial and slow full form'*, C-48].

    DECLINES: a subject that is no person (dead, or never one) is `NO_CHANGE` -> `tend.refused`; a body
    already whole is written to itself, which the gate reads as no change (`NoOpReceipt`) -> `tend.refused`.
    Two tenders on one person in one fold: the first restores him, the second moves nothing and is refused
    -- the outcome is the same whichever arrives first.

    B12a.69 (U5d_WR §3, F-WR-23) -- A TEND IS WITNESSED: its subject carries the `(who, "body", v)` Observation `_eff_kill` writes (`body_observed`),
    `v` the MENDED body written (`whole`, a marked man's ceiling), never `p.body` read here (the pre-tend body). It rides the
    `body.tended` Event, which WITNESS deposits to the tender, so his claim of the wound is superseded by a claim of the mended
    body (`world_q.wounded_with`: newest claim wins) and the healed man stops drawing `tend`. A refused tend (no person; a body already
    whole, `NoOpReceipt`) writes nothing and so deposits nothing. MATTER's recovery writes none yet (CP-T10-04)."""
    who = _operand(a, "subject")
    p = w.persons.get(who)
    if p is None:
        return NO_CHANGE
    # v11 CP-T03-07: HEALS TOWARD THE PERSON'S OWN CEILING, never `condition_scale`: a marked man is restored to his mark.
    # B07.02 (18-A edit 5, D-05): the band lets a share of the headroom land (`_scaled`; share 1, or no band, is the whole).
    whole = p.body + _scaled(max(p.body, p.body_ceiling) - p.body, res)

    def perform() -> None:
        p.body = whole
    return Change((Subject.entity("persons", who, fields=("body",), observed=body_observed(who, whole)),), perform)


@effect_for("train")
def _eff_train(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """v9 IN-12 step 9 (#453 §9.4; K-20, K-21) -- `train` RAISES ONE CAPABILITY OF THE SUBJECT BY ONE.

    THE CAPABILITY IS THE VOCATION THE ACT CARRIES on the operand `rosters.yaml: vocation_sourced` names
    for its verb (`kind` for `train`), one Candidate per vocation in `VOCATIONS` (the skills the verb table's `capability:` column names)
    (`decision/options.py::opening_set`). ⚠ J-13 ANSWERED (iii) AS THE INTERIM [medium; Jordan to
    correct]: it writes `Person.capability` ONLY WHERE A CASE NAMES A VOCATION -- so the key must be a
    `VOCATIONS` member (K-20's range: Thread Sensitivity has no carrier, H-85, P-08) and the SUBJECT
    need not hold it: a non-holder is minted `{key: 1}` (B05.09, `raised_capability`), his opposition and fight score unchanged until the rank
    passes `pool_default` (`seam/wrappers/pool.py::score`), his social pool one die up (`::faculty`). The ACTOR's own capability is
    NOT read: capability gates nothing (#353 §9.2), here as at formation. ONE whole point, the unit of a
    dice count [ASSUMPTION; medium; Jordan to correct; revert: a swept fixture step].

    DECLINES (`NO_CHANGE` -> `train.refused`): no such subject; a key that is no vocation; a rank at its
    row's ceiling."""
    who = _operand(a, "subject")
    key = _operand(a, VOCATION_SOURCED[a.verb])
    p = w.persons.get(who)
    raised = raised_capability(p, key) if p is not None and key in VOCATIONS else None
    # B07.02: the ONE whole point is `_scaled` by the band, so a band short of the full effect lands no point (floor of one half is
    # nothing). [ASSUMPTION: 18-A's "a `practice` mark the practice addend already reads" is not written -- `train` names no skill
    # (`capability: none`), so `world_q.practice` keys nothing on it; basis: `VERB_CAPABILITY['train']` is empty]
    if raised is None or not _scaled(1, res):
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
