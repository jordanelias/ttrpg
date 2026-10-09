"""`season.loop.effects_combat` -- casualties and morale: fight (renamed from "kill / wound") and
the duel's `accept`, march.

EXTRACTED from `effects.py` at the per-subsystem split (Phase 4). Holds the two effects that read a
severity off a scene the seam already resolved rather than choosing one (Jordan, 2026-09-04: *"the
combat engine determines the result there. your code just has to accept the result."*) -- personal
combat's `fight` and mass battle's `march`. `_scar` and `_SCAR_DP` (the moral-layer write on the
wounded person) are RETIRED at IN-08 H3: the scar is now written by the fold on the act's OBSERVERS
(`loop/resolve.py::_scar_witnesses`), not by an effect. See `effects_shared.py` for `effect_for`
and `_operand`, the one cross-file helper `march` calls.
"""

from __future__ import annotations

from ..data.rosters import (
    DECLARED, FELLED, FIELD_CASUALTY_MODELS, LOST, UNOPPOSED, WOUND_HARM_MODELS,
    faction_prop_id, require_member,
)
from ..gaps import Unspecified
from ..queries.world_q import holder_faction_of
from ..state.gate import NO_CHANGE, Change, Subject

from .effects_shared import _operand, effect_for


# `accept` (the duel pair's second half) is the same contest over the same prize, `contests: "the
# body"`, with the same degree-keyed writes read off the same scene: one effect registered twice.
# The fold's scar reads `a.verb`, so a duel's moral layer reads `accept`'s own alignment cells. (`challenge`
# writes nothing and needs no effect: `VerbRow.effect_carried`.) `fight` was RENAMED from
# "kill / wound" (plan `FIGHT-RENAME`); only the `EFFECTS` key and its row moved.
@effect_for("fight")
@effect_for("accept")
def _eff_kill(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§E3: writes `(Person, body)`, `(Person, exists)` and `(Tenure, until)`.

    ⚠⚠ G4 -- WHAT IT NAMES, AND THE ONE EFFECT THAT NARROWS ITS SUBJECT TO A FIELD. The subject is
    the person wounded, read as PRESENCE and `body` (`fields=("body",)`) -- the two cells the
    band's own kinds name (`person.died` is existence, `body.changed` is body). TWO THINGS THE
    SAME WRITE DOES ARE DELIBERATELY NOT PART OF WHAT THE GATE JUDGES (a third, `scar`, left this
    effect at IN-08 H3: the fold writes it on the act's observers AFTER the outcome, as its own
    gated write, so a wound the gate refuses scars nobody):
      * the CASCADE (`remove_person`'s closures). A consequence of the existence change, which IS
        judged; F3 admits each closure as `destroy's cascade`; never reported, so never named. If
        existence did not move the cascade did not run.
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
    -- applied to this magnitude too, not by a fresh measurement; `tools/balance_oracle.py` was
    a campaign-driver instrument and could not observe an `engine/season`-only mechanic (`rosters.yaml`'s
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
