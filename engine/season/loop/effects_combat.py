"""`season.loop.effects_combat` -- casualties and morale: fight (renamed from "kill / wound"), march.

EXTRACTED from `effects.py` at the per-subsystem split (Phase 4). Holds the two effects that read a
severity off a scene the seam already resolved rather than choosing one (Jordan, 2026-09-04: *"the
combat engine determines the result there. your code just has to accept the result."*) -- personal
combat's `fight` and mass battle's `march` -- and `_scar`, the moral-layer write both can trigger,
which stays local since no effect outside this file calls it. `_SCAR_DP`, the scar accumulator's
order-independence precision, moves here with its one reader rather than to `effects_shared.py`. See
`effects_shared.py` for `effect_for` and `_operand`, the one cross-file helper `march` calls.
"""

from __future__ import annotations

from ..data.rosters import (
    DECLARED, FELLED, FIELD_CASUALTY_MODELS, LOST, PURSUIT_AXES, UNOPPOSED, WOUND_HARM_MODELS,
    faction_prop_id, require_member,
)
from ..gaps import Unspecified
from ..queries.world_q import holder_faction_of
from ..state.gate import NO_CHANGE, Change, Subject

from .effects_shared import _operand, effect_for


# ⚠ THE SCAR ACCUMULATOR'S PRECISION, AND IT EXISTS TO MAKE THE FOLD ORDER-INDEPENDENT.
# `scar` accumulates across acts, and incremental IEEE addition is NON-ASSOCIATIVE -- the control
# `results.json`'s A5 row already records on this tree is exactly it (five float deltas summed in
# two orders give 0.30000000000000004 vs 0.3; the same five as integers are identical), and A5's
# own conclusion is that *"a one-ulp difference at a band floor is A VERB THAT EXISTS IN ONE
# ORDERING AND NOT ANOTHER"*. Because `scar` reaches `repr(Person)` -> `_entity_digest` ->
# `content_hash`, a one-ulp divergence moves the hash too. `S27.3`'s answer elsewhere is
# sum-then-clamp-once, which needs the whole set at once and this write does not have it;
# rounding each accumulation to a fixed place buys the same property -- `round(a+b) == round(b+a)`
# -- for a per-act writer.
# [JUSTIFIED: a PRECISION, not a game value -- six places is far below any magnitude `scar_step` can take and exists only to keep accumulation associative; nothing in the model reads it as a quantity]
_SCAR_DP = 6  # ED-IN-0249 / H-128 -- the scar accumulator's precision, order-independence only


def _scar(w: "World", p, verb: str) -> None:
    """`(Person, scar[axis])` -- THE MORAL LAYER'S MISSING MOTION, §54 item 21.

    ⚠ THE FORM IS THE CHAIN'S OWN AMENDMENT, NOT THE SOURCE DOCUMENT'S, AND THE DIFFERENCE IS THE
    WHOLE REASON THIS SITS AT RESOLVE. `conviction_track_v1.md` §2 -- the mechanic's design home,
    quarantined and REFERENCE under §0.05 -- has an NPC *"accumulate Conviction Scars from
    WITNESSING morally-loading events"*. `holonic_ARCHITECTURE.md:1901` folds that in AMENDED and
    says why in as many words: *"the source says written at WITNESS, which breaks two things --
    the moral layer's WITNESS row is nothing, and a scar written there is an Event writing a
    `(Person, ...)` social row, which is L4. Lawful form: a `(Person, scar[axis])` row,
    `social: true`, written at RESOLVE in the ACTS class BY THE OUTCOME THAT NAMES THE PERSON."*
    S9.3 is the law underneath (*"WITNESS NEVER TOUCHES A BELIEF"*), so the design document's own
    trigger table is the one part of it that may not be implemented.

    ⚠ THE AXES COME FROM `ALIGNMENT`, WHICH ALREADY OWNS *which axes a verb engages*. §8: find the
    single-owner primitive and compose on it. A second table mapping outcome -> axis would be a
    second owner of the same claim, free to disagree with the one `choose` scores against -- and
    it would have to be AUTHORED, on a basis `STR-2` is about to replace. Reading `ALIGNMENT`
    keyed by the live axis roster means this survives that rename by never having known the old
    names. `axis` on L3's closed registry, as item 21 requires.

    ⚠ WHAT IS ASSUMED HERE AND IS NOT THE CHAIN'S, STATED SO IT CAN BE ATTACKED: that the depth of
    the moral wound is PROPORTIONAL to how strongly the verb engages the axis. Item 21 gives the
    row, the step, the class and the keying; it does not give a formula. The alternative -- a flat
    scar on every engaged axis -- is the arm a sweep would compare, and `scar_step` is where it
    would be run from.

    ⚠ AND WHO IS SCARRED IS THE SUBJECT, WHICH IS A READING OF *"the outcome that names the
    person"* AND NOT A CERTAINTY. The outcome of `kill / wound` names the person wounded, so the
    wound is theirs. The competing reading -- that the ACTOR carries the moral wound of having
    done it -- is at least as defensible on the mechanic's own *moral wound* framing, and nothing
    in item 21 settles it. Left as the open question rather than decided in silence."""
    step = w.fixtures.get("scar_step")
    if not step:
        # THE CONTROL ARM, AND IT RETURNS BEFORE TOUCHING THE CARRIER. A zero-depth scar written
        # as a 0.0 cell would still put a key on the field, and `_entity_digest` reprs every
        # field -- which is the difference between an arm that is inert and one that looks it.
        return None
    # ⚠⚠ `decision.align`, NOT A LOCAL `ALIGNMENT` READ, AND THE LOCAL READ WAS A REAL DEFECT
    # RATHER THAN A STYLE SLIP. This computed the cell inline off THIS module's own `ALIGNMENT`
    # binding. `align()` reads the binding in `decision/options.py`, which is the one the `H-66`
    # alignment sweep REBINDS (`decision.options.ALIGNMENT = alignment_at(point)`) -- so the
    # sweep moved `choose`'s scoring and could not move the scar at all. MEASURED before the
    # fix: under the `uniform` arm `align('kill / wound','sacred')` read 1.0 while `_scar`
    # still wrote 3.0 off the unrebound 0.3. The docstring above promises exactly what the inline read broke: no
    # second table free to disagree with the one `choose` scores against. One owner, §8, and the
    # sweep now reaches both readers.
    from ..decision import align
    # ⚠ SIGNED, AND THE `abs()` THAT STOOD HERE COLLAPSED A DISTINCTION THE READER NEEDS.
    # 17 of the 52 populated `ALIGNMENT` cells are NEGATIVE, so a verb that VIOLATES an axis and
    # one that UPHOLDS it cut an identical wound under `abs()`. It is invisible today only
    # because `kill / wound`'s one cell is `+0.3`; it bites the moment a negative-cell verb is
    # wired, and the scar's named reader -- the Conviction crisis -- is about the DIRECTION of
    # the wound. The magnitude keeps the cell's sign and `scar` is a signed accumulator.
    for axis in PURSUIT_AXES:
        weight = float(align(verb, axis))
        if weight:
            p.scar[axis] = round(p.scar.get(axis, 0.0) + step * weight, _SCAR_DP)
    # ⚠ SORTED ON WRITE, BECAUSE A DICT'S INSERTION ORDER REACHES `World.content_hash()`.
    # `_entity_digest` digests a dataclass as `repr(obj)`, and `repr` of a dict is
    # insertion-ordered -- so two people scarred by the same verbs in opposite ORDERS held equal
    # values and produced different digests. `_entity_digest` already `sorted()`s PLAIN dicts for
    # this exact reason (`world.py:141`), but a dict FIELD inside a dataclass never reaches that
    # branch. `A5`/`S32` assert the content hash is order-independent; that survived only while
    # this dict could hold one key. Re-inserting in sorted order makes the field carry its own
    # canonical form rather than relying on nobody scarring twice.
    if len(p.scar) > 1:
        p.scar = {k: p.scar[k] for k in sorted(p.scar)}


@effect_for("fight")  # RENAMED from "kill / wound", 2026-09-29 (plan `FIGHT-RENAME`) -- same
# effect, same body; only the `EFFECTS` dict key (and its `verb_table.yaml` row) moved.
def _eff_kill(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§E3: writes `(Person, body)`, `(Person, exists)` and `(Tenure, until)`.

    ⚠⚠ G4 -- WHAT IT NAMES, AND THE ONE EFFECT THAT NARROWS ITS SUBJECT TO A FIELD. The subject is
    the person wounded, read as PRESENCE and `body` (`fields=("body",)`) -- the two cells the
    band's own kinds name (`person.died` is existence, `body.changed` is body). THREE THINGS THE
    SAME WRITE DOES ARE DELIBERATELY NOT PART OF WHAT THE GATE JUDGES:
      * `scar`. It is written by the OUTCOME, whatever the body did -- the comment at `_scar`'s
        call below says why it was moved ahead of the magnitude model: so that sweeping `H-123`
        (`wound_harm_model`) does not also sweep whether `H-128`'s scar runs. Judging the whole
        Person would re-couple them the other way: at `scar_step > 0` the `none` arm -- `H-123`'s
        control, whose whole job is to emit the REFUSAL -- would start emitting `body.changed`
        for a body nothing touched, and the control would measure `scar_step`. So a wound that
        moves only the scar is refused, and the scar stands, exactly as the `none` arm always
        behaved. At the shipped `scar_step = 0` the two readings cannot differ.
      * the CASCADE (`remove_person`'s closures). A consequence of the existence change, which IS
        judged; F3 admits each closure as `destroy's cascade`; never reported, so never named. If
        existence did not move the cascade did not run.
      * the dead person's own `person`-kind rung, popped by the same owner -- the same reasoning.
    THE NEW NO-OP THIS MAKES VISIBLE: a `Wounded` outcome under `scene_fraction` whose fraction
    rounds back to the body it started from (`max(1, body * left // full)` at `body == 1`, or a
    scene that took no health) used to emit `body.changed` over an unchanged body and is now
    `kill.refused`. MEASURED BEFORE THIS POSITION on `build_realm(0)`, four seasons: every
    `kill / wound` that reached this effect moved its subject, so no run moves.

    ⚠ AND THE TWO `Unspecified` RAISES NOW COME BEFORE ANYTHING IS WRITTEN. The no-scene raise
    always did; the no-health-scale raise came AFTER `_scar` had written, so a season that died on
    it died with the scar already moved. Both are read while the `Change` is built, which touches
    nothing.

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
    the band it is implementing. `max(1, ...)` is `combat_seam.derive_party`'s own floor
    (*"a dying person still fights"*), followed rather than reinvented."""
    d = a.payload if isinstance(a.payload, dict) else {}
    who = d.get("subject")
    p = w.persons.get(who)
    if p is None:
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
    st = (res.result.get("wound_state") or {}).get(who) or {}
    model = w.fixtures.get("wound_harm_model")
    require_member(
        model,
        WOUND_HARM_MODELS,
        f"wound-harm model {model!r} is not in the roster",
        "H-123",
        law="`observers_for`'s precedent and its reason -- *an unrecognised mode silently "
            "falling back would make every measurement of this sweep read the control*")
    # ⚠⚠ THE SCAR RUNS BEFORE THE HARM-MODEL BRANCH, AND IT USED TO RUN AFTER IT -- WHICH
    # CONFOUNDED TWO INDEPENDENT SWEEPS. `wound_harm_model == "none"` returns early (it is
    # `H-123`'s control, the arm that isolates *the band selected a different write set* from
    # *the band changed a value*), so with the call below that `return` a `Wounded` outcome at
    # `scar_step=10` silently wrote NO scar while `verb_table.yaml` declared `Person.scar` for
    # that band unconditionally. Sweeping `H-123` therefore also swept whether `H-128`'s
    # mechanism ran at all, so neither row measured what it says it measures. The moral wound
    # is a consequence of the OUTCOME, not of how much body the scene took, so it belongs
    # ahead of the magnitude model entirely. (G4: it is still the first thing `perform` writes;
    # the magnitude below is COMPUTED first only because computing it writes nothing.)
    if res.degree == FELLED:
        # The scene says this person went down, and the table says that is the kill. The body
        # goes to 0 on every arm: the arms grade a WOUND, and a felling is not one.
        body = 0
    elif model == "none":
        body = None                             # the control arm: the body is not written
    elif model == "total":
        body = 0
    else:                                       # `scene_fraction`
        full = int(st.get("health_full") or 0)
        left = int(st.get("health_remaining") or 0)
        if full <= 0:
            raise Unspecified(
                f"the scene reports no health scale for {who!r} ({st!r})", "S39.4/H-123",
                needs="`health_full` on the subject's wound state",
                law="the magnitude is READ from the scene; a scene that carries none cannot be "
                    "read, and choosing a number here is what this arm exists not to do")
        body = max(1, p.body * max(0, left) // full)

    def perform() -> None:
        _scar(w, p, a.verb)
        if body is None:
            return
        p.body = body
        if p.body > 0:
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
        w.remove_person(who)
    return Change((Subject.entity("persons", who, fields=("body",)),), perform)


@effect_for("march")
def _eff_march(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§E3 (M4, `ED-IN-0279` clause (a)): writes `(Person, body)` and `(Person, stance)` -- ON
    THE LOSING SIDE ONLY, on either band. Jordan's ruling on clause (b): a loss writes *"casualties
    only, decrease in morale, and a grudge token"* and nothing else -- the ruling is silent on the
    winner because it was never asked, and this does not invent an answer for it.

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
    -- applied to this magnitude too, not by a fresh measurement; `tools/balance_oracle.py` is
    `mc_v18`-only and cannot observe an `engine/season`-only mechanic (`rosters.yaml`'s
    `field_casualty_models` note).

    ⚠ THE STANCE ROWS FOLLOW THE SEEDED-LOYALTY SHAPE (`harness/data/cast.py`'s own
    `stance_from_loyalty`): a FIXED valence of `-1.0` (both are negative sentiments; the sign is
    not swept) and a WEIGHT that is (`field_morale_weight`/`field_grudge_weight`, `H-148`,
    swept `0`/`1`/`3`). The grudge targets the WINNING faction; the morale hit targets the
    LOSER'S OWN faction -- both re-derived from `a.via` (the office the act was exercised
    through, `exercised_seat`'s own field) and `world_q.holder_faction_of` on the target rung,
    exactly as `loop/sides.py::sides_of` derives them, because both are facts about the ACT and
    re-deriving them here is cheaper and safer than threading a third value through `Resolution`
    for one reader."""
    if res is None or not isinstance(res.result, dict):
        raise Unspecified(
            f"`march` on {_operand(a, 'subject')!r} was folded with no result to read a "
            f"casualty count from", "S39.4/H-98",
            needs="a Resolution from `resolve()`'s seam branch -- the mass_battle provider",
            law="M4 (`ED-IN-0279` clause (a)) -- the magnitude is READ from the engine's own "
                "survivor ratio, never invented here")
    if res.degree in (DECLARED, UNOPPOSED):
        return NO_CHANGE
    parties = res.result.get("parties") or {}
    attackers = list(parties.get("claimants") or [])
    defenders = list(parties.get("subject_members") or [])
    engine_result = res.result.get("result") or {}
    attacker_lost = res.degree == LOST
    losers = attackers if attacker_lost else defenders
    pct = engine_result.get("attacker_size_pct" if attacker_lost else "defender_size_pct")
    touched = [pid for pid in losers if pid in w.persons]
    if not touched:
        return NO_CHANGE
    model = w.fixtures.get("field_casualty_model")
    require_member(
        model, FIELD_CASUALTY_MODELS, f"field-casualty model {model!r} is not in the roster",
        "H-148", law="`wound_harm_model`'s own precedent -- an unrecognised mode silently "
        "falling back would make every measurement of this sweep read the control")
    target = _operand(a, "subject")
    office = w.offices.get(a.via)
    attacker_faction = (faction_prop_id(office.faction)
                        if office is not None and office.faction else None)
    defender_faction = holder_faction_of(w, target)
    winner_faction = defender_faction if attacker_lost else attacker_faction
    loser_faction = attacker_faction if attacker_lost else defender_faction
    if model == "none" and winner_faction is None and loser_faction is None:
        return NO_CHANGE
    morale_w = w.fixtures.get("field_morale_weight")
    grudge_w = w.fixtures.get("field_grudge_weight")

    def perform() -> None:
        for pid in touched:
            p = w.persons[pid]
            if model == "total":
                p.body = 0
            elif model == "scaled_by_degree":
                p.body = max(1, int(p.body * max(0.0, pct or 0.0)))
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
    fields = ("stance",) if model == "none" else ("body", "stance")
    return Change(tuple(Subject.entity("persons", pid, fields=fields) for pid in touched), perform)
