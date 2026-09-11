"""`season.loop.effects` — the resolver's BODY. One effect per verb that writes.

EXTRACTED, step 5 of the decomposition (a PURE MOVE). `EFFECTS`, its decorator, the ONE operand
reader (`_operand`) and the ten `_eff_*` move together and must: §8's *"THE OWNER OF THE RULE, AND
THREE EFFECTS HAD THEIR OWN COPY"* is about `_operand` specifically, and the decorator-filled
table has to be defined where the decorated functions are or it is empty when the fold reads it.

WHAT THIS MODULE IS AGAINST, which is the reason it exists at all (§27.2). The fold once took an
`effect` parameter — a CALLER-SUPPLIED LAMBDA that inspected `a.verb` and returned Events, and
every probe wrote its own. That is a resolver per caller, each free to disagree about what a verb
does. A verb-keyed effect registered here is one implementation for every caller, and a verb with
a `writes:` column and no effect REFUSES rather than silently writing nothing. Register row H-63.

⚠ NOTHING HERE TAKES A WRITE TOKEN, AND NO EFFECT CALLS `w.write`. The first version of this
docstring said every effect writes THROUGH `w.write(...)`, which is the exact inversion
`_eff_confer`'s own docstring refutes seventy lines below — *"AN EFFECT MUTATES AND RETURNS THE
IDS IT TOUCHED; IT DOES NOT CALL `w.write` … My first version did both, and the fold correctly
refused."* An effect mutates directly (`w.add_tenure`, `w.records[...] =`, `src.stores[kind] =`)
and returns the ids; the FOLD passes those ids through the gate. Caught by a read-only critic,
and it is §47's failure exactly: a false claim of enforcement stops the next reader checking.
"""

from __future__ import annotations

from ..data.rosters import FELLED, WOUND_HARM_MODELS
from ..gaps import InstrumentDefect, Unspecified
from ..state.carriers import Proposition, Record, Tenure
from ..state.ids import H
from ..trace_log import TRACE
from .predicates import RELEASABLE_KINDS


# ---------------------------------------------------------------------------
# THE EFFECTS. One per verb, OWNED BY THE RESOLVER.
#
# ⚠ PART E's `writes:` COLUMN NAMES THE CELL AND NEVER THE VALUE. `transfer` writes
# `(Rung, stores)` -- it does not say BY HOW MUCH, or that the giver's store goes DOWN. Without
# that the fold checks a precondition, emits, and changes nothing, so `transfer` twice from a
# one-unit larder succeeds twice: the scarcity §27.1 rests on never happens.
#
# THE DISTINCTION FROM THE `effect` PARAMETER W3 REMOVED IS THE WHOLE POINT, and it is §27.2's.
# A CALLER-supplied lambda is a second resolver: every caller may disagree about what a verb does,
# and each probe did. A VERB-KEYED effect registered here is the resolver's BODY -- one
# implementation, the same for every caller, and a verb with a `writes:` and no effect REFUSES
# rather than silently writing nothing.
#
# This gap is register row H-63.
# ---------------------------------------------------------------------------
EFFECTS: dict = {}


def effect_for(verb: str):
    def deco(fn):
        EFFECTS[verb] = fn
        return fn
    return deco


def _operand(a: "Act", name: str):
    """THE FOLD'S ONE READ OF A CARRIED OPERAND. A missing one RAISES.

    ⚠ AN ABSENT OPERAND AT RESOLVE IS AN `InstrumentDefect`, NOT A REFUSAL, AND THE DISTINCTION
    IS THE WHOLE OF `W-C`'s SECOND HALF. A refusal says *the world would not permit this*; a
    caller minting a `transfer` that names no receiver is saying nothing about the world at all.
    Filing it as a refusal would emit `emits_on_refusal`, `W-B` would deposit that at WITNESS, and
    every witness would end the season holding a belief about a granary the act never named --
    the instrument's own gap, laundered into the game as evidence. `operands_for` is what makes
    this unreachable from a COMPUTED act: a Candidate whose operands cannot be derived is never
    formed, so an act arriving here without one came from a hand-written call site.

    ⚠ IT IS THE OWNER OF THE RULE, AND THREE EFFECTS HAD THEIR OWN COPY. `_eff_move` raised on a
    missing `to` and `_eff_work` on a missing `site` -- both correct, both written twice -- while
    `_eff_transfer` DEFAULTED four operands (`from`/`to` to `""`, `kind` to `"grain"`, `amount` to
    `1`) and `_eff_confer` defaulted `to` to the actor, i.e. conferred an office on whoever
    happened to be acting when the act named nobody. Same situation, four verbs, three answers.
    §8: the rule lives once."""
    d = a.payload if isinstance(getattr(a, "payload", None), dict) else {}
    if d.get(name) is None:
        raise InstrumentDefect(
            f"a {a.verb!r} reached its effect with no {name!r} operand. The fold binds operands "
            f"from the act's payload and `operands_for` forms NO Candidate whose operands it "
            f"cannot derive, so an act minted without one is a CALLER defect and not a design "
            f"gap -- and fabricating a value here would name a thing nobody chose. Payload: "
            f"{sorted(d)}")
    return d[name]


# --- THE GOVERNANCE SLICE'S EFFECTS. `dispatch` needs none: Part E gives it `writes: []`, so an
# order is an EMISSION and nothing else, which is `L1` in one row -- a dispatch does not move a
# person, it tells one, and whether they go is their own act next season.

@effect_for("confer")
def _eff_confer(w: "World", a: "Act", res: "Resolution | None" = None) -> list:
    """Seats an office: a new `hold` Tenure opens, and any prior holder's closes.

    ⚠ AN EFFECT MUTATES AND RETURNS THE IDS IT TOUCHED; IT DOES NOT CALL `w.write`. The fold
    calls it INSIDE the gate's `apply()`, once, for all of the row's `writes:` — so a nested
    `w.write` is a write inside a write, and returning `None` tells the fold nothing was touched,
    which makes it emit the REFUSAL. My first version did both, and the fold correctly refused an
    act whose state change had in fact happened. `_apply_write`'s docstring states the contract."""
    d = (a.payload or {}) if isinstance(a.payload, dict) else {}
    # ⚠ `to` WAS `d.get("to") or a.actor` -- a silent default that seated the ACTOR whenever the
    # act named nobody, which is the same class as `_eff_transfer`'s four and is deleted with
    # them. A conferral onto nobody is a malformed act, not a self-conferral.
    # ⚠ THIS CHANGE IS A DELIBERATE EXTRA AND NOT A PATH `H-94` MADE REACHABLE; RECLASSIFIED BY
    # THE `W-C` ADVERSARIAL PASS, because filing it as a consequence overstates what closing the
    # operand channel did. NO COMPUTED ACT CAN REACH THIS EFFECT: `confer` is untyped, `office`
    # is not in `rosters.yaml: requires_operands` so `operands_for` can never derive one, and
    # `_req_confer` returns False when the payload names none -- `corpus_run`'s own output lists
    # `confer` among the verbs "foldable but never even attempted". The improvement is real (a
    # silent self-conferral becomes a loud `InstrumentDefect`) and nothing measurable moved.
    obj, to = d.get("office"), _operand(a, "to")
    if not obj or obj not in w.offices:
        return []
    closed = []
    for t in w.tenures:
        if t.kind == "hold" and t.object == obj and t.live:
            t.until = w.tick
            closed.append(t.id)
    nt = Tenure(H(w.world_seed, w.tick, to, f"hold:{obj}"), to, obj, "hold", w.tick)
    w.add_tenure(nt)
    # ⚠ PER-KIND. Conferring onto an UNHELD office closes nothing, and returning a flat list made
    # the fold publish `tenure.closed` anyway -- a state change that did not happen, which is the
    # fabricated-`person.died` class committed inside the fix for it. The mapping's empty entry is
    # dropped by `_apply_write`.
    return {"tenure.opened": [nt.id], "tenure.closed": closed}


@effect_for("release")
def _eff_release(w: "World", a: "Act", res: "Resolution | None" = None) -> list:
    """`04 §A.3` row 14's generic closer: the actor ends a live edge they own.

    THE MIRROR OF EVERY OPENER AT ONCE, which is the point -- `04 §A.3` row 14 replaces *four
    closing verbs missing* with one, so `oblige`, `commit`, `tie`, `knot`, `succeed` and `hold`
    all end here rather than growing an antonym apiece. `01_AXIOMS.md:1121-1136` refuses the
    per-verb framing by name: *"Asking which verb ends an `oblige` is the wrong question… one
    sentence rather than four verbs."*

    ⚠ **A PERSON CAN NOW RESIGN AN OFFICE, AND THAT WAS A `T-m` VIOLATION IN THE TABLE, NOT THE
    DESIGN.** `hold` was closable only by `revoke`, which is `remit:revoke` -- so a seat could be
    taken from someone and never laid down. `architecture/meta/HANDOFF_NEXT.md` §2a: *"The design
    says a person may resign; the verb table does not let them. Fix the table, and do not re-open
    the design."* `hold` is in the domain for exactly this reason.

    ⚠ NO `w.write` HERE. An effect MUTATES AND RETURNS THE IDS IT TOUCHED; the fold calls it inside
    the gate's `apply()` for the row's `writes:`. Returning an empty list is how the fold learns
    nothing was closed, and that is what emits `release.refused` -- so the refusal channel is the
    return value, not a raise (§E2: *failure emits, never raises*)."""
    subj = _operand(a, "subject")
    touched = []
    for t in w.tenures:
        if (t.subject == a.actor and t.object == subj
                and t.kind in RELEASABLE_KINDS and t.live):
            t.until = w.tick
            touched.append(t.id)
    return touched


@effect_for("revoke")
def _eff_revoke(w: "World", a: "Act", res: "Resolution | None" = None) -> list:
    """Unseats an office: the live `hold` closes. The mirror of `confer`, which is why the two are
    the pair that proves the slice — one opens what the other closes, on the same row."""
    d = (a.payload or {}) if isinstance(a.payload, dict) else {}
    obj = d.get("office")
    touched = []
    for t in w.tenures:
        if t.kind == "hold" and t.object == obj and t.live:
            t.until = w.tick
            touched.append(t.id)
    return touched


@effect_for("convene")
def _eff_convene(w: "World", a: "Act", res: "Resolution | None" = None) -> list:
    """Schedules a sitting: a Date comes due, with a ConveningCondition attached — Part E's two
    writes, both done by this one effect because the fold calls it once for the row.

    ⚠ A DATE IS A DICT HERE, not a class: `w.dates` is read as `d.get("due_at")` / `d.get("fired")`
    at CALENDAR. The first version built a `Date(...)` that does not exist.

    ⚠ WHAT THE SITTING THEN DECIDES IS `H-32` AND IS NOT HERE. `convene` puts a date on the
    calendar and stops, which is `L5`: a clock may not produce an outcome. `W7` is the item that
    makes the sitting decide."""
    d = (a.payload or {}) if isinstance(a.payload, dict) else {}
    when = int(d.get("when", w.tick + 1))
    did = H(w.world_seed, w.tick, a.actor, f"convene:{d.get('venue') or '-'}")
    date = w.dates.setdefault(did, {"id": did, "venue": d.get("venue")})
    date["due_at"] = when
    date["convening_attached"] = True
    return [did]


@effect_for("move")
def _eff_move(w: "World", a: "Act", res: "Resolution | None" = None) -> None:
    """§D4 / #353 §15.1: travel is a TENURE ALTER, owned by the traveller as the Tenure's subject.
    The old leg closes and a new one opens; the destination rides on the payload where the act
    names one. ⚠ This is `H-63`: Part E's `writes:` names the three cells and never the values, so
    what a `move` DOES is stated here rather than in the table — one implementation owned by the
    resolver, which is the distinction §27.2 draws against a caller-supplied lambda."""
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
        TRACE.decision(f"a move's destination is not up the §10 ladder -> {a.actor} into {dest!r}",
                       "S10/E3", chose="change nothing, so the fold emits the refusal",
                       alternatives=["write the edge anyway (add_tenure raises and the season "
                                     "dies)", "let the precondition admit it and crash later"])
        return []
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
    return [a.actor]


@effect_for("work")
def _eff_work(w: "World", a: "Act", res: "Resolution | None" = None) -> None:
    """`work` alters `(Site, condition)` by the act's declared delta. The DELTA IS NOT APPLIED
    HERE -- §27.3 sums every delta across the fold and clamps ONCE, so applying it per act would
    make the clamp arrival-order dependent, which §32 forbids. The write goes through the gate so
    the class and Partition are checked; the value lands in the accumulator.

    ⚠ IT REPORTS THE SITE ANYWAY. The fold now refuses an act whose effect touched nothing, and
    `work`'s DELTA is deferred while its SUBJECT is not: the act is about that site, and saying
    so is what keeps the deferral from reading as a no-op."""
    # ⚠ NO FALLBACK. This read `or next((x for x in sorted(w.sites)), None)` -- the alphabetically
    # FIRST site in the world -- so a `work` with no site named one nobody chose. `_eff_move`
    # refused the identical situation and this did not; found by the W-A adversarial pass, which
    # noted the two are the same defect one verb along. `W-C` gave that answer ONE owner
    # (`_operand`) rather than two copies of it.
    return [_operand(a, "site")]


@effect_for("create_record")
def _eff_create_record(w: "World", a: "Act", res: "Resolution | None" = None) -> None:
    """§E3: `create_record` writes `(Record, exists)` and `(Record, stages)`. `H-63` is why the
    VALUES are here and not in the table.

    ⚠ THE STAGES COME FROM THE ACT, NOT FROM A DEFAULT. #353 `:1043` (§54 item 14) makes the
    stage list ACT-DECLARED -- "the act DECLARES the stages and their terms" -- so an act that
    names none creates a record with none, and the instrument does not invent a ladder. That is
    what makes Carin's season the case `PLAN.md` §6.1 chose: a Record with act-declared stages is
    the largest ruled row in the corpus and nothing about it needs a default."""
    d = a.payload if isinstance(a.payload, dict) else {}
    rid = d.get("record") or f"rec:{a.id}"
    stages = list(d.get("stages") or [])
    if not stages:
        # `H-80`, DECLARED AND SWEPT. The act SHOULD declare these (#353 §13.1) and a computed
        # act cannot: §F1's Candidate is `(verb, subject, why)` with no operand channel. Refusing
        # instead would make `(Record, stages)` -- a Part D row -- unreachable from any person's
        # decision, so the honest form is §G's declare-default-sweep rather than either an
        # invention or a blocker. Each stage is `(due_tick, label, the act that wound the clock)`.
        n = w.fixtures.get("record_stages_default")
        term = w.fixtures.get("record_stage_term")
        stages = [(w.tick + (i + 1) * term, f"stage{i + 1}", a.id) for i in range(n)]
    w.records[rid] = Record(rid, d.get("rung") or a.actor, d.get("kind") or "text",
                            subject_matter=d.get("subject_matter"), stages=stages)
    # S13: possession is a `hold` Tenure owned by the holder, never a field on the Record. The
    # maker holds what they made until they part with it.
    w.add_tenure(Tenure(H(w.world_seed, w.tick, a.actor, f"hold:{rid}"),
                        a.actor, rid, "hold", since=w.tick))
    return [rid]


@effect_for("destroy_record")
def _eff_destroy_record(w: "World", a: "Act", res: "Resolution | None" = None) -> None:
    """§E3: writes `(Record, exists)`. The Record goes, and every `hold` on it ends -- S15.3's
    rule that a tenure dies THROUGH the death of what it is over, never beside it."""
    d = a.payload if isinstance(a.payload, dict) else {}
    rid = d.get("record")
    if rid is None or rid not in w.records:
        return None
    del w.records[rid]
    for t in w.tenures:
        if t.object == rid and t.live:
            t.until = w.tick
    return [rid]


@effect_for("kill / wound")
def _eff_kill(w: "World", a: "Act", res: "Resolution | None" = None) -> None:
    """§E3: writes `(Person, body)`, `(Person, exists)` and `(Tenure, until)`.

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

    THE THREE ARMS (`wound_harm_model`, registered at `H-125`, injected at `DEFAULT_FIXTURES`):
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
        return None
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
    if model not in WOUND_HARM_MODELS:
        raise Unspecified(
            f"wound-harm model {model!r} is not in the roster", "H-125",
            needs=f"one of {sorted(WOUND_HARM_MODELS)}",
            law="`observers_for`'s precedent and its reason -- *an unrecognised mode silently "
                "falling back would make every measurement of this sweep read the control*")
    if res.degree == FELLED:
        # The scene says this person went down, and the table says that is the kill. The body
        # goes to 0 on every arm: the arms grade a WOUND, and a felling is not one.
        p.body = 0
    elif model == "none":
        return None
    elif model == "total":
        p.body = 0
    else:                                       # `scene_fraction`
        full = int(st.get("health_full") or 0)
        left = int(st.get("health_remaining") or 0)
        if full <= 0:
            raise Unspecified(
                f"the scene reports no health scale for {who!r} ({st!r})", "S39.4/H-125",
                needs="`health_full` on the subject's wound state",
                law="the magnitude is READ from the scene; a scene that carries none cannot be "
                    "read, and choosing a number here is what this arm exists not to do")
        p.body = max(1, p.body * max(0, left) // full)
    if p.body > 0:
        return [who]
    # ⚠ `w.tenures`, NOT `p.tenures + w._unowned`, AND THAT IS A FIX `W-E`'s OWN TEST FOUND.
    # `p.tenures` is the tenures this person is the SUBJECT of (§15.1 -- a Tenure is owned by its
    # subject), so the old scan could not see an edge ANOTHER PERSON owns that names the dead one
    # as its OBJECT. Measured in `tiny_world`: `t10`, a live `tie` from `p_low` to `p_mid`,
    # survived `p_mid`'s death and then DANGLED, because `del w.persons[who]` had already removed
    # the person it pointed at. §15.3 is explicit that the tenure ends THROUGH THE DEATH; this is
    # the write the `Felled` branch declares (`Tenure.until`) actually reaching every edge it
    # names. `w.tenures` is owner-first over every person plus `_unowned`, so it is a WIDENING of
    # the same scan and not a second rule.
    for t in list(w.tenures):
        if (t.subject == who or t.object == who) and t.live:
            t.until = w.tick
    del w.persons[who]
    return [who]


@effect_for("utter")
def _eff_utter(w: "World", a: "Act", res: "Resolution | None" = None) -> None:
    """§E3: writes `(Proposition, exists)`. §14: a Proposition is IDENTITY-BEARING AND IMMUTABLE,
    fixed at utterance and never destroyed -- `Proposition` is a frozen dataclass, so that is
    structural here rather than asserted."""
    d = a.payload if isinstance(a.payload, dict) else {}
    pid = d.get("proposition") or f"prop:{a.id}"
    if pid in w.propositions:
        return None                       # immutable: an utterance never overwrites one
    w.propositions[pid] = Proposition(pid, d.get("mood") or "OUGHT",
                                      d.get("subject") or a.actor,
                                      d.get("predicate") or "", d.get("value"), w.tick)
    return [pid]


@effect_for("transfer")
def _eff_transfer(w: "World", a: "Act", res: "Resolution | None" = None) -> None:
    """§54 item 7's mirror: the giver's store goes DOWN and the receiver's goes UP.

    ⚠ THE FIRST VERSION ONLY DECREMENTED, and §E3 says `transfer` writes `(Rung, stores)` **×2**,
    one per side. A one-sided transfer ANNIHILATES MATTER -- six grain left the world and arrived
    nowhere, in an economy where `yield` is the only source (#353 `:856`). The scarcity proof still
    passed, because it only watched the giver: a run can be right about the thing it looks at and
    wrong about the world."""
    # ⚠ FOUR SILENT DEFAULTS STOOD HERE AND `W-C` DELETED ALL FOUR: `from`/`to` defaulted to
    # `""`, `kind` to `"grain"` and `amount` to `1`. Each was §0.05's literal-in-a-body, and
    # together they made an operand-less `transfer` a WELL-FORMED act about a granary nobody
    # named. They are `_operand` reads now, and their two open values are fixtures with a register
    # row and a sweep (`H-94`).
    src = w.rungs.get(_operand(a, "from"))
    dst = w.rungs.get(_operand(a, "to"))
    kind, amount = _operand(a, "kind"), _operand(a, "amount")
    # ⚠ A SIDE THAT IS NOT A RUNG MEANS THE TRANSFER DID NOT HAPPEN, and returning nothing is what
    # makes the fold emit the refusal. This branch became reachable FROM A COMPUTED ACT the moment
    # operands became real: a person names a receiver from their question's referents and may name
    # something that is no rung at all. The old shape moved the giver's side anyway, which is the
    # matter ANNIHILATION this effect's own docstring records -- grain leaving the world and
    # arriving nowhere. §42.2's polarity: an unperformable transfer refuses; it does not
    # half-happen.
    # ⚠ *"IT SURVIVED ONLY BECAUSE NO COMPUTED ACT EVER BOUND `from` TO BEGIN WITH"* STOOD HERE
    # AND IS FALSE; STRUCK BY THE `W-C` ADVERSARIAL PASS. No COMPUTED act bound `from` -- but
    # probe `F10` did, in its payload, and omitted `to`, so the old effect decremented `Hh` and
    # delivered nowhere: `F10` DESTROYED 6 GRAIN ON EVERY PROBE RUN, in an economy where `yield`
    # is the only source. Measured by weighing every rung across the probe's own season: total
    # store mass ends at 107 on the pre-`W-C` tree (`45a537c`) and at 113 here, and the difference
    # is exactly the 6. The path was reachable AND REACHED; only the computed path was closed, and
    # `F10`'s payload edit is a BUG FIX in a live probe rather than a signature accommodation.
    # `F10` now asserts conservation, because its old assertion set could not observe the failure
    # it was sitting on (§0.1 point 2).
    if src is None or dst is None:
        TRACE.decision(f"transfer names a side that is no rung -> from "
                       f"{_operand(a, 'from')!r} to {_operand(a, 'to')!r}", "E3/S27.1",
                       chose="change nothing, so the fold emits the refusal",
                       alternatives=["move the giver's side anyway (matter leaves the world)"])
        return []
    src.stores = dict(src.stores or {})
    src.stores[kind] = src.stores.get(kind, 0) - amount
    dst.stores = dict(dst.stores or {})
    dst.stores[kind] = dst.stores.get(kind, 0) + amount
    # BOTH SIDES, because §E3 says `transfer` writes `(Rung, stores)` twice -- one per side -- and
    # a one-sided report would make the Event name half of what it did. The `if r is not None`
    # filter that stood here is gone with the branch above that made it necessary.
    return [src.id, dst.id]
