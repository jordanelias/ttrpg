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

from ..data.rosters import (
    DECLARED, FELLED, FIELD_CASUALTY_MODELS, LOST, UNOPPOSED, WON, WOUND_HARM_MODELS,
    require_member,
)
from ..data.verbs import VERB_TABLE, VOCATION_SOURCED, VOCATIONS
from ..gaps import Unspecified
from ..queries.person_q import held_against
from ..queries.world_q import ancestry, holder_faction_of, home_of
from ..state.gate import NO_CHANGE, Change, Subject, may_muster, seat_faction

from .effects_migration import _relocate
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
    the band it is implementing. `max(1, ...)` is `seam/wrappers/combat.py::party_end`'s own floor
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

    ⚠ v9 IN-13 (#453 §10.4 step 8, THE ARRIVAL): ONE WRITE IS ADDED, AND IT IS PRESENCE, NOT TITLE. On
    `Won` and `Unopposed` every claimant is relocated to the destination (`_relocate`'s pair, keyed on
    the mover: his live `contain` closes, one opens to the target, the target is appended to his
    `travel_leg`), emitting `army.arrived` beside the band's kind; the gate admits another person's
    legs under its `muster` basis (`state/gate.py::may_muster`). The winner's BODY and STANCE are
    still never written, and no `hold` moves (R-6, β: title moves by `seize`, `give`, `release` or
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
    for one reader."""
    if res is None or not isinstance(res.result, dict):
        raise Unspecified(
            f"`march` on {_operand(a, 'subject')!r} was folded with no result to read a "
            f"casualty count from", "S39.4/H-98",
            needs="a Resolution from `resolve()`'s seam branch -- the mass_battle provider",
            law="M4 (`ED-IN-0279` clause (a)) -- the magnitude is READ from the engine's own "
                "survivor ratio, never invented here")
    if res.degree == DECLARED:
        return NO_CHANGE
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
    pct = engine_result.get("attacker_size_pct" if attacker_lost else "defender_size_pct")
    touched = [pid for pid in losers if pid in w.persons]
    if not touched and not movers:
        return NO_CHANGE
    model = w.fixtures.get("field_casualty_model")
    require_member(
        model, FIELD_CASUALTY_MODELS, f"field-casualty model {model!r} is not in the roster",
        "H-148", law="`wound_harm_model`'s own precedent -- an unrecognised mode silently "
        "falling back would make every measurement of this sweep read the control")
    attacker_faction = seat_faction(w, a.via)
    defender_faction = holder_faction_of(w, target)
    winner_faction = defender_faction if attacker_lost else attacker_faction
    loser_faction = attacker_faction if attacker_lost else defender_faction
    if model == "none" and winner_faction is None and loser_faction is None:
        touched = []
        if not movers:
            return NO_CHANGE
    morale_w = w.fixtures.get("field_morale_weight")
    grudge_w = w.fixtures.get("field_grudge_weight")
    # The fold emits the kinds its subjects EARN, and a subject earning `None` earns nothing on its
    # own (`loop/resolve.py`: an empty `earned` set means *every* declared kind, a non-empty one means
    # *only* those). So the kinds are earned as a whole: with an army that moves, every subject earns
    # `None` and the band publishes both its kind and the arrival; with nobody moving (`Lost`, or a
    # `Won` whose army already stood there), the losers earn the band's own kind alone and no arrival
    # is published.
    loser_earns = None if movers else _band_kind(res.degree)

    def perform() -> None:
        _casualties()
        # THE ARRIVAL, AFTER THE CASUALTIES: on `Won` the losers are the defenders, never a mover.
        for pid in movers:
            _relocate(w, a, target, mover=pid)

    def _casualties() -> None:
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
    # G4 -- WHAT IT NAMES: the losers by the fields the casualty writes (earning as above); the movers
    # WHOLE, `move`'s reason (a `contain` leg is stored on its Person, so his digest carries the legs
    # and `travel_leg`).
    return Change(tuple(Subject.entity("persons", pid, earns=loser_earns, fields=fields)
                        for pid in touched)
                  + tuple(Subject.entity("persons", pid) for pid in movers), perform)


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
    for pid in live:
        here = homes.get(pid)
        if here not in chains:
            chains[here] = ancestry(w, here)
        if target in chains[here]:
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
    to the ceiling -- here `condition_scale`, the scale a person is built at (`Person.body`'s default) --
    taken whole, because the `share` term is the commons of a fabric and a body has none, and `f(degree)`
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
    whole = max(p.body, int(w.fixtures.get("condition_scale")))

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
    `pool_default` and LOWER his pool (`seam/wrappers/sigma.py::_pool_of`). The ACTOR's own capability is
    NOT read: capability gates nothing (#353 §9.2), here as at formation. ONE whole point, the unit of a
    dice count [ASSUMPTION; medium; Jordan to correct; revert: a swept fixture step].

    DECLINES (`NO_CHANGE` -> `train.refused`): no such subject; a key that is no vocation; a subject who
    holds none in it (a pupil whose case names no vocation)."""
    who = _operand(a, "subject")
    key = _operand(a, VOCATION_SOURCED[a.verb])
    p = w.persons.get(who)
    if p is None or key not in VOCATIONS or key not in (p.capability or {}):
        return NO_CHANGE
    raised = {**p.capability, key: int(p.capability[key]) + 1}

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
    0.0 afterwards wherever no positive row names the referent. He writes only his own field (`T-m`'s
    sense: the owner ending what he holds), never another's.

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
