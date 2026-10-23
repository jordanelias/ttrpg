"""`loop/matter.py` -- MATTER -- barrier 2. `04 §A.2`: owns the three motions and the maturation of declared terms; emits per matrix row; token MATTER. (A Record's act-declared stages, and -- since plan position `17b` -- a Tenure's declared `term`.)

⚠ **THE BODY IS THE DRIVER'S OWN, BOUND BACK ONTO THE CLASS -- NOT A DELEGATING STUB.**
`loop/driver.py` ends with `SeasonDriver.matter = matter`, so `SeasonDriver.matter` IS this
function and `inspect.getsource(SeasonDriver.matter)` returns THIS SOURCE. Eight tests read a
step's body that way -- three of them `witness`'s, one of those a pure NEGATIVE assertion --
and a stub would fail two and silently vacate the third, which is why step 9 of the
decomposition (ED-IN-0203) refused to delegate. Step 5 established the technique when
`class Query` bound module functions as staticmethods.

⚠ **THE TOKEN IS HANDED IN BY THE DRIVER (G2).** `SeasonDriver.season` mints a MATTER `Token`
through `loop/driver.py::mint_token` and passes it as `token`; every gate write below presents
it. This module constructs none and calls no minter -- `tests/test_g2_token.py` fails if it does.

⚠ **AND THIS BARRIER NOW OWNS `World._rehome()` (G2's disposition of `ED-IN-0206`'s finding).** It
ran at the head of DELIBERATE and on every `w.tenures` read; it runs here, once a season, and
nowhere else. See the call below and `_rehome`'s own docstring for why here and not licensed there.
"""

from __future__ import annotations

from typing import NamedTuple, Optional
from ..data.fixtures import SITE_YIELD
from ..data.geography import adjacent_territories
from ..data.matrix import Step
from ..data.requires import SHORTFALL_PREDICATE, Observation
from ..data.rosters import STANDING_CROSSED
from ..decision import agreement, standing_of
from ..decision.budget import bands_below
from ..queries import world_q
from ..queries.person_q import LedgerReader
from ..state.carriers import Event
from ..state.gate import Token
from ..state.ids import H, ROOT, draw_factory
from ..trace_log import TRACE



# -- MATTER -- barrier 2 -- THE WORLD FREEZES AT ITS END (S25) -----------
def _crossings(w: "World", subject_id: str, floors: dict, before, after,
               cause: "str | None") -> list:
    """S12.1 / L5: A BAND EDGE CROSSING IS AN EMISSION, NOT A WRITE. One rule, two carriers.

    ⚠⚠ FACTORED OUT OF THE SITE LOOP BY ITEM 3b, BECAUSE PERSONS NOW CROSS BANDS TOO. `04
    §A.3.3` asks for exactly this — *"the crossing block factors into `_crossings(...)` called for
    sites AND for persons, both reading `band_floors`"* — and the reason is `CLAUDE.md` §8 rather
    than tidiness: a second copy of *what counts as crossing a floor* would let a site and a body
    disagree about it, and `band_floors` is one table with a key per kind.

    ⚠ NO NEW BAND TABLE, AND THAT IS `H-38`'s CLOSURE BEING SPENT. `band_floors["body"]` already
    exists and `decision.budget` already reads it; a `band_floors.person` would have been the
    second scheme `H-38` closed to avoid. The caller passes the row it wants.

    ⚠ IT EMITS AND WRITES NOTHING. L5: a threshold crossing *"MAY NEVER PRODUCE AN OUTCOME"*. The
    Event is witnessable and the consequence, if any, is somebody's later act.

    ⚠ THE ANTECEDENT IS THE WRITE THAT CROSSED THE FLOOR (`W4` / `H-12` — *"MATTER emits an Event
    per write SO CROSSINGS HAVE AN ANTECEDENT"*). Passing `None` roots it at the seed, which is
    what made the one Event in this barrier that exists to be walked back from walk nowhere.

    ⚠ THE EVENT IS THE ONLY CARRIER, SINCE POSITION `11a`. A second one, `w.crossings` (a
    `(subject_id, verb, before, after, ev.id)` tuple, never pruned), used to be appended here too
    -- `01_ATTENTION_AND_REACH.md` §A.1.3 pt 3 named it a violation of `AX-4`'s protected property
    in the thing it protects: *"two readers of one fact, and they disagree about what the fact
    is"* (the tuple named the site; `questions_for`'s old `band_crossed` source named the VERB,
    `H-110`). Deleted rather than kept in step: `anchor_of(w, ev)` (tier 3, via `ev.causes[0]`)
    answers the same subject the tuple did, with one owner instead of two."""
    out: list = []
    for verb, floor in sorted(floors.items()):
        if before >= floor > after:
            # G1b: NO `subject=` -- the field is deleted. The crossing is ABOUT whatever the
            # write that crossed the floor was about, and `anchor_of` reads that through
            # `causes[0]` (tier 3). Both callers pass the gate emission they just made, so the
            # `[ROOT]` arm is unreachable today; were it reached, the crossing would anchor on
            # nothing and nobody would witness it -- which `test_g1b_attribution.py`'s planted
            # anchorless Event pins as the observable consequence.
            ev = Event(id=H(w.world_seed, w.tick, subject_id, f"crossing:{verb}"),
                       kind="condition.band_crossed", changes=[],
                       causes=[cause] if cause else [ROOT], emitted_at=w.tick)
            w.log.append(ev)
            out.append(ev)
            TRACE.event(ev.id, ev.kind, ev.causes)
            TRACE.decision(f"{subject_id} crossed the `{verb}` floor", "S12.1/S3-L5",
                           chose="EMIT a witnessable Event; write no social row; produce no outcome",
                           alternatives=["write the consequence directly (L5 forbids: a crossing MAY NEVER PRODUCE AN OUTCOME)",
                                         "silently drop the verb from the set (then nobody can witness it)"])
    return out


def _lattice_strain(w: "World", scale: int) -> dict:
    """v9 IN-35 FORCE-HAZARD -- THE CALAMITY RE-EXPRESSED AS A COUPLING RULE (#457 `:123-143`): `{site
    id: the extra wear this season}`, which the wear loop below adds to the Site's kind's rate. ONE
    RULE, NO SOURCE AND NO SCALAR: a Site loses `lattice_coupling / condition_scale` of its gap down to
    the WEAKEST Site of its own territory or a bordering one (`world_q.enclosing_territory`,
    `data/geography.py::adjacent_territories`), so a worn place drags the fabric beside it down, and
    that fabric the next ring out, one border a season at most. Nothing else moves the lattice.

    * READ FROM THE BARRIER'S OPENING CONDITIONS, ALL OF THEM, BEFORE ANY WEAR IS WRITTEN. The wear
      loop is a parallel map (S31.2: `_in_parallel_map`), so a Site may not read a neighbour's write
      of this same barrier; a front therefore advances one ring per season, never across the realm in
      one sorted pass. That is what makes *"reach territories in order of distance"* a property of
      the rule rather than of `w.sites`' order.
    * A `+` LOOP (`H-235`): the lower the neighbour, the more this Site falls, and so on outward.
      BOUNDED BY MENDING -- persons' `restore` acts (`loop/effects_economy.py::_eff_restore`,
      ungraded, its `_rise` unchanged) raise a fabric toward its ceiling at RESOLVE, which the driver
      runs AFTER this season's MATTER and before the next one's. So holding a ring stops the front at
      that ring (a ring restored each RESOLVE opens every MATTER whole and passes no gap on); a mend
      at the source does not recall a ring MATTER has already pulled, which pulls the next ring
      itself (`test_in35_lattice_coupling.py`, both arms, in driver order). No new verb, role or module: the
      threadwork module stays unplugged (`proposals/2026-10-07-unplugged-systems-replug.md` §3.4,
      §6 items 3 and 5), and `systems/overview/sim/ms_track.py`'s stored 0-100 scalar and yearly
      rate have no place here -- a world track that moved by itself would be a fourth clock
      (`loop/census.py`: NO CLOCK GENERATES ANYTHING). This is matter wearing, the licensed clock.
    * NEVER BELOW THE WEAKEST NEIGHBOUR: the share is at most the whole gap (`0 <= weight <= scale`,
      refused otherwise), so the coupling alone cannot overshoot, and `max(0, ...)` below still floors
      the write.
    * EVERY SITE, WHATEVER ITS KIND -- the lattice is the territories' fabric, not a kind, so nothing
      is special-cased; a Site with no territory above it couples to nothing and nothing to it.

    ⚠ THE CONTROL TAKES NOTHING: at weight 0 (shipped) this returns `{}` before reading a Site or
    tracing a line, and the season is today's byte for byte. ⚠ WHAT IT DOES NOT BUILD: the SOURCE.
    No act yet strains the lattice AT ASKEHEIM (thread operations as a carrier, `H-85`, plan `33`) and
    Askeheim (T15) holds no Site in the built realm, so on `build_realm` a non-zero weight couples
    ordinary wear, `sabotage` (which lowers any present fabric it reaches) and repair, not a Calamity
    (`H-236`)."""
    weight = w.fixtures.get("lattice_coupling")
    if not weight:
        return {}
    if not 0 <= weight <= scale:            # `not ... <=`, so a NaN is refused too
        raise ValueError(f"lattice_coupling {weight} is not a share in [0, {scale}] (H-235)")
    borders = adjacent_territories()
    where = {sid: world_q.enclosing_territory(w, w.sites[sid].rung) for sid in sorted(w.sites)}
    by_terr: dict = {}
    for sid, t in where.items():
        if t is not None:
            by_terr.setdefault(t, []).append(sid)
    out: dict = {}
    for sid, t in where.items():
        if t is None:
            continue
        near = [n for u in (t, *sorted(borders.get(t, ()))) for n in by_terr.get(u, ()) if n != sid]
        if not near:
            continue
        gap = max(0, w.sites[sid].condition) - max(0, min(w.sites[n].condition for n in near))
        if gap > 0 and (weight * gap) // scale:
            out[sid] = (weight * gap) // scale
    TRACE.decision(f"the lattice coupling pulls {len(out)} Site(s) toward their weakest neighbour",
                   "v9 IN-35 / #457 FORCE-HAZARD",
                   chose="add the pull to the Site's kind's wear, read from the barrier's opening conditions",
                   alternatives=["a stored Mending Stability scalar decaying a year at a time (a fourth clock)",
                                 "read a neighbour's write of this barrier (a sorted pass, not a parallel map)"])
    return out


class _HeldBefore(NamedTuple):
    """A person's ledger CUT AT A FLOOR, in the one shape `standing_of` reads (`p.id`, `p.ledger`) --
    so the gap over the past claims is `standing_of`'s own formula, never a second copy of it."""
    id: str
    ledger: list


def _standing_crossings(w: "World") -> list:
    """v9 SC-02 `22b` STEP 23 (`19_PLAN.md`): PRESSURE IS A PERSON-KEYED BAND CROSSING OF THE STANDING GAP.

    For each person: the gap (`decision/options.py::standing_of`, D-4: *pressure is the gap*) over the
    claims that had landed BEFORE last season's WITNESS (`world_q.landing_floor`, the boundary
    `questions_for` reads as *new*) against the gap over all of them. Where the two fall in different
    bands (`H-223`'s floors), one Event records the crossing, its causes THE DEPOSITS THAT COMPOSED
    THE GAP: the `claim.deposited` of every told claim about him that pairs (`agreement`, the owner of
    *pairs*) and of the claim of his own each was paired against (`LedgerReader.belief_among`, `_pair`'s
    mate). A claim with no deposit in the log (planted at build) contributes no cause.

    ⚠ IT EMITS AND WRITES NOTHING (L5, and the step's falsifier: *"a crossing produces a write rather
    than a question"*). No `changes`, no gate write; the consequence is the person's own later choice,
    through the question `world_q.questions_for` raises from this record, whose referents are the
    people whose claims made the gap. ⚠ AND IT IS NOT FANNED OUT AT WITNESS: it is returned to nobody.
    A standing is person-side (computed at sensing, stored nowhere); the person reads his own crossing
    from the record, and no channel would admit anyone else to it.

    ⚠ EITHER DIRECTION, UNLIKE `_crossings`. A site's band gates verbs and only a fall closes one; the
    step says *"if the band differs"*, and from `H-29`'s maximum-gap default a first pairing can only
    NARROW the gap, so a downward-only rule could never fire on the step's own artifact. Not composed
    on `_crossings` for that reason, and because these floors key no verb."""
    floors = tuple(w.fixtures.get("standing_band_floors"))
    out: list = []
    if not floors:
        return out                        # the control arm: one band, nothing can cross
    floor = world_q.landing_floor(w)
    for pid in sorted(w.persons):
        p = w.persons[pid]
        if not any(c.subject == pid for c in p.ledger):
            continue                      # `standing_of` reads only claims about himself: no gap to move
        past = [c for c in p.ledger if (c.when, c.round) < floor]
        if len(past) == len(p.ledger):
            continue                      # nothing landed since: the same claims, the same gap
        before = standing_of(_HeldBefore(pid, past), w.fixtures)
        after = standing_of(p, w.fixtures)
        if bands_below(before, floors) == bands_below(after, floors):
            continue
        own = [c for c in p.ledger if c.subject == pid and c.source == "firsthand"]
        made: list = []
        for c in p.ledger:
            if c.subject == pid and c.source == "told_by" and agreement([c], own)[2]:
                mate = LedgerReader([o for o in own if o.predicate == c.predicate]).belief_among()
                made.extend(x for x in (c, mate) if x not in made)
        causes = [d for d in (w.last_emission_of("claim.deposited", c.id) for c in made) if d]
        ev = Event(id=world_q.standing_crossing_id(w, pid), kind=STANDING_CROSSED, changes=[],
                   causes=causes or [ROOT], emitted_at=w.tick)
        w.log.append(ev)
        out.append(ev)
        TRACE.event(ev.id, ev.kind, ev.causes)
        TRACE.decision(f"{pid}'s standing gap crossed a band ({before} -> {after})", "19_PLAN step 23/S3-L5",
                       chose="RECORD the crossing; raise a question about the tellers; write nothing",
                       alternatives=["write a stress or a consequence (L5: a crossing MAY NEVER PRODUCE AN OUTCOME)"])
    return out


def _die(w: "World", token: Token, pid: str) -> None:
    """DEATH THROUGH THE ONE OWNER, written once for both MATTER callers (hunger, the bodies pass).
    `World.remove_person` is `_eff_kill`'s cascade, factored. Chained to the death WRITTEN about
    `pid` (`written=True`, H-129): a RESOLVE `person.died` anchors on the killer, so the anchor read
    would hand a killer who later dies here his victim's death as his cause."""
    prior_d = w.last_emission_of("person.died", pid, written=True)
    w.write("exists", token,
            lambda pid=pid: w.remove_person(pid),
            record_kind="Person", fieldname="exists", driver="Event",
            emits="person.died", subject=pid,
            causes=[prior_d] if prior_d else [ROOT])


def matter(self, token: Token, actorless: Optional[list[Event]] = None) -> list[Event]:
    w = self.w
    w.step = Step.MATTER
    TRACE.step("MATTER", "enter"); TRACE.barrier(2, "MATTER")
    w.discard_caches()
    # G2. THE TENURE STORE IS REHOMED HERE, AT THE LAST BARRIER BEFORE THE FREEZE, AND ONLY HERE.
    # `_rehome` routes a Tenure added before its subject Person existed onto that Person's own
    # list, so `budget`, `person_side_eligible` and `questions_for` -- which read `p.tenures`
    # directly -- see it. It ran at the head of DELIBERATE, a barrier that owns nothing and holds
    # no token (`04 §A.2`), which the Fable gate on Arc 1 found and `ED-IN-0206` filed; G2 was
    # told to dispose of it and moved it. Here is sufficient because nothing between this line and
    # any DELIBERATE round can create a Person -- no step does, full stop, checked by grepping
    # every `Person(` construction in the tree (`harness/` only; nothing in `loop/` or an effect
    # constructs one). ⚠ CORRECTED 2026-09-26, ANTAGONIST PASS ON G2: this comment previously
    # also cited "the world is frozen from the end of this barrier" as a second reason. That is
    # false for U2's multi-round seasons -- RESOLVE thaws the world every round (`w.frozen = False`,
    # `loop/resolve.py`), so a season's second and later DELIBERATE rounds run on an UNFROZEN
    # world. The freeze protects nothing here; the no-Person-construction fact does the whole of
    # the work, alone. MEASURED 2026-09-26 at
    # `build_realm(0)`, one season: it moves ZERO Tenures in every builder in the tree
    # (`build_realm`, `headless.build_world`, `tiny_world`, `governance_spine.build`,
    # `corpus_run.build_at` all create persons first); it moves one only in the planted ordering
    # `test_w5_a_tenure_added_before_its_subject_still_reaches_its_owner` builds. Hash-neutral.
    w._rehome()
    emitted: list[Event] = []

    # S31.2: the EVENT CHANNEL and the DEATH CASCADE run SERIALLY, BEFORE the parallel
    # section, because both CROSS OWNERS (S31.1). S31.1 exception 3: an actorless event is
    # ONE Event spanning many rungs -- sharding it per rung BREAKS causes[], because ONE
    # CAUSE IS ONE ID.
    # ⚠ REV 5. This row previously read "serial: event channel, then death cascade; then
    # parallel over Sites and bodies" and was recorded 194 times -- describing TWO BRANCHES
    # THAT DO NOT EXIST IN THIS CODE. A decision register whose most frequent row names code
    # never written is worse than no register: it is the "every decision made" claim made
    # false at its highest-volume site.
    TRACE.decision("MATTER's cross-owner operations", "S31.1",
                   chose="serial: the actorless event channel; then parallel over Sites",
                   alternatives=["shard the event channel per rung (breaks causes[]: one cause is one id)"],
                   not_implemented=["the death cascade (S31.1 exception 2)",
                                    "bodies, larders, yield (S25's other rows)"])
    for e in (actorless or []):
        w.log.append(e); emitted.append(e)
        TRACE.event(e.id, e.kind, e.causes)

    # -- TERM MATURATION (#353 `:491-492`) ------------------------------
    # "MATTER matures terms; each maturation is A PERSON'S PAST ACT RIPENING, with `causes[]`
    # pointing at the act that wound the clock." This is the second link of `PLAN.md` §6.3's
    # chain and the only mechanism in the design by which one season's act reaches into a
    # later one WITHOUT anybody acting again.
    #
    # ⚠ AND IT STOPS IF THE MAKER IS GONE, which #353 gives as the reason the lawful version
    # beats the clock-driven one: "a half-made copy now correctly STOPS if the copyist is
    # jailed, which the MATTER-driven version gets wrong: A COPY THAT FINISHES ITSELF." The
    # check is on the winder still existing, not on a clock.
    for rid in sorted(w.records):
        rec = w.records[rid]
        for n, st in enumerate(list(rec.stages)):
            if not (isinstance(st, tuple) and len(st) >= 3):
                continue
            due, label, wound_by = st[0], st[1], st[2]
            if due != w.tick:
                continue
            holder = next((t.subject for t in w.tenures
                           if t.object == rid and t.kind == "hold" and t.live), None)
            if holder is None or holder not in w.persons:
                TRACE.note(f"{rid} stage {label!r} did not mature: its winder is gone "
                           "(#353 :496 -- a half-made copy STOPS rather than finishing itself)")
                continue
            # `causes[]` names the EVENT that created the record where there is one, so the
            # chain WALKS; #353 says "the act that wound the clock" and the act's own
            # emission already names that act, so pointing at the emission preserves the
            # provenance and adds a link rather than restating one.
            prior = next((e.id for e in reversed(w.log)
                          if any(c.subject == rid for c in e.changes)), wound_by)
            # ⚠⚠ **THROUGH THE GATE, RULED BY JORDAN 2026-09-10, AND WHAT IT REPLACES WAS `ID-9`
            # LIVE.** This built the Event by hand and appended it:
            #     Event(H(..., f"matured:{label}"), "term.matured", rid,
            #           [StateChange(rid, "set", "MATTER", "stages", label)], [prior], w.tick)
            # — an Event REPORTING A CHANGE THAT DID NOT HAPPEN. Nothing in the package mutated
            # `rec.stages`; `matter.py` read it (`list(rec.stages)`) and `probes.py` read it, and
            # that was every occurrence. Worse, `(Record, stages)` is `steps: [RES]`, `class: ACTS`,
            # *"terms are act-declared, never MATTER-advanced"* — so a MATTER-step Event claimed a
            # change to the one field the matrix forbids MATTER to touch. The row it SHOULD name,
            # `(Record, matured)`, named a field that existed nowhere on the carrier.
            # ⚠ THE GATE EMITS, AND THAT IS THIS FILE'S OWN PRECEDENT RATHER THAN AN INVENTION:
            # `claim.decayed` (:131) and `stores.changed` (:169) already route this way, `H-12` is
            # `ruled` that *"MATTER emits an Event per write so crossings have an antecedent"*, and
            # `04 §C.2` has the gate apply the write and emit. A hand-built Event beside a gate that
            # emits is a second emitter.
            # ⚠ NO `emitted.append` AND NO `TRACE.event` HERE, AND BOTH OMISSIONS ARE LOAD-BEARING.
            # The gate traces (`world.py:461`) and buffers, and this function DRAINS the buffer at
            # its end (`emitted.extend(w._emitted_by_write)`), so appending here would put the
            # maturation in `emitted` TWICE — once by hand and once by the drain — and WITNESS fans
            # out whatever it is given. The hand-built version had to do both because it never
            # crossed the gate.
            w.write("matured", token,
                    lambda rec=rec: setattr(rec, "matured", True),
                    record_kind="Record", fieldname="matured", driver="Event",
                    emits="term.matured", subject=rid, causes=[prior])

    # -- A TENURE'S DECLARED TERM MATURES (`T-n`, plan position `17b`) ---------------------
    # `04 §A.2` gives this barrier *"the maturation of declared terms"* and `04 F.3` names the
    # carrier and the writer: *"`Tenure.term`; MATTER matures it; the causation rule generalises to
    # two causes"*. So every LIVE edge whose `term.matures_at` has come is closed here, one gate write
    # each, with `causes = [term.declared_by]` -- `04 §B.8`: *"a `matures_at` MATTER matures with
    # `causes[] = term.declared_by`"*; AX-5: *"a matured term cites the act that wound it"*. That act
    # is the `oblige` that opened the edge, or the last `transfer` that paid its upkeep, so a lapse is
    # a story with an author, walkable back to the hand that last wound the clock.
    #
    # ⚠ THROUGH CALENDAR WAS REJECTED BY LAYER 1 BY NAME, AND IT WAS THE OBVIOUS SIBLING. `Date.due_at`
    # vs `w.tick` is structurally the same comparison, but `04 §B.8`'s synthesis call: *"Rejected:
    # routing term expiry through CALENDAR, which makes a term un-endable when nobody acts -- the
    # exact ratchet `T-n` exists to forbid."* A term is matter's clock (AX-5), not the calendar's.
    #
    # ⚠ THE OPPOSITE POLARITY FROM THE RECORD BRANCH ABOVE, AND DELIBERATELY. A half-made copy STOPS
    # when its copyist is gone, because PRODUCTION needs a maker. A term of service LAPSES whether or
    # not anyone is left to pay it, because a lapse needs nobody -- that is its whole point: an
    # interregnum that leaves nobody seated to pay dissolves the household, with nobody acting.
    #
    # ⚠ THE GATE, NOT THIS LOOP, DECIDES THAT IT IS LAWFUL. `matured_term` is S15.3's pre-check
    # generalised to its second cause (`World.write`); F3 then observes the write and admits it only
    # as `T-n` -- actorless, a pure closure, of an edge whose own term (read from BEFORE the write)
    # has `matures_at <= w.tick` (`state/gate.py::tenure_write_basis`). `<=` and not `==`: a term
    # that should have matured at a barrier this world skipped (a hand-driven fold, a builder that
    # starts mid-campaign) still lapses at the next one rather than living forever.
    # ⚠ ORDER: SORTED BY EDGE ID (subject, then object, breaking ties), so the emission order -- and
    # with it every emission id's draw ordinal -- is a property of the world, not of store order (R4).
    # Since IN-10 (a) a computed `oblige` forms and executes, and `_eff_oblige` opens it with the
    # term `w.tick + oblige_term` (`17a`), so this branch moves a realm run once such a term
    # matures; a `confer`'s seat-hold carries a term only when the act declares one
    # (`effects_governance._declared_term`, IN-10 (b)), which no computed act does.
    for t in sorted((t for t in w.tenures if t.live and t.term is not None
                     and t.term.matures_at <= w.tick),
                    key=lambda t: (t.id, t.subject, t.object)):
        w.write("until", token,
                lambda t=t: setattr(t, "until", w.tick),
                record_kind="Tenure", fieldname="until", driver="Event",
                emits="tenure.closed", subject=t.id, causes=[t.term.declared_by],
                matured_term=t.id)

    # -- CLAIM CONFIDENCE DECAY (`W4` / `H-40`) --------------------------
    # THE THIRD LICENSED CLOCK (#353 `:864`), and until now the only one of the three with no
    # implementation at all — Part D had no `Claim` row, so Part D was not total for a clock
    # #353 licenses. `W2` added the row; this is the other half.
    #
    # ⚠ L4 IS NOT VIOLATED AND THE REASON IS WORTH STATING: a Claim's confidence is
    # `social:false` in Part D, so the world may move it. What the world may NOT do is decide
    # anything with it — the decay emits and stops, exactly as a band crossing does.
    #
    # THE ANTECEDENT IS THE CLAIM'S OWN PREVIOUS DECAY, chaining to `[ROOT]` on the first one,
    # for the same reason wear does: a licensed clock's genuine first emission is the only
    # place `[ROOT]` belongs.
    decay = w.fixtures.claim_decay()
    for pid in sorted(w.persons):
        p_ = w.persons[pid]
        for c in list(p_.ledger):
            if c.confidence <= 0:
                continue
            # The claim's own previous decay, else the deposit that created it. NEVER
            # `[ROOT]`: a claim is not a clock, it is a thing a witness deposited, and the
            # deposit has an Event. `[ROOT]` here would say the campaign seed caused it.
            prior = (w.last_emission_of("claim.decayed", c.id)
                     or w.last_emission_of("claim.deposited", c.id))
            if prior is None:
                TRACE.note(f"{c.id} has no deposit Event to chain its decay to; skipped "
                           "rather than rooted at the campaign seed")
                continue
            # ⚠ AN EFFECT THAT TOUCHED NOTHING DID NOT DO THE THING, AND MUST NOT EMIT THE
            # SUCCESS. That rule is already enforced twice in this file -- `_fold` applies it
            # to a verb whose effect wrote nothing, and `rosters.yaml`'s
            # `conditional_emission_rows` uses the same argument to exempt `(Record, ttl)`.
            # It was violated here, at `H-40`'s OWN DECLARED `0` SWEEP POINT: at
            # `claim_decay_per_season = 0` every claim still emitted `claim.decayed` every
            # season while `max(0, c.confidence - 0)` changed nothing, so the control arm of
            # the sweep published a decay that did not happen. A sweep point that fabricates
            # is worse than one that is unexecuted. Found by the `W4` adversarial pass.
            after = max(0, c.confidence - decay)
            if after == c.confidence:
                continue
            w.write("confidence", token,
                    lambda c=c, after=after: setattr(c, "confidence", after),
                    record_kind="Claim", fieldname="confidence", driver="Event",
                    emits="claim.decayed", subject=c.id, causes=[prior])

    # -- PRESSURE: A PERSON'S STANDING CROSSES A BAND (v9 SC-02 `22b` step 23) ----
    # Logged and kept out of `emitted` (nobody witnesses another's standing): see the docstring.
    _standing_crossings(w)

    # -- LARDERS, THEN YIELD (`W8`) -------------------------------------
    # #353 §25 fixes the ORDER and this code follows it rather than choosing one: *"Events
    # resolve FIRST, then bodies, larders, yield, travel, wear."* So a season's subsistence is
    # drawn against LAST season's stores and production replenishes afterwards, which is a
    # substantive difference — the reverse order would let a rung eat what it had not yet
    # produced, and no rung could ever run short. `test_w8_...order...` asserts it.
    #
    # ⚠ BODIES AND TRAVEL WERE NOT BUILT WHEN THIS WAS WRITTEN; BOTH ARE NOW (item 3b below, and
    # the travel pass after the yield loop, plan position `19c`), each in #353's order.
    # v9 IN-21 / `H-26`: ONE draw per season, keyed on the clock, owned by `world_q.season_factor_of`.
    # With `season_factor_draw` empty (the shipped control) this is the bare `season_factor`.
    factor = world_q.season_factor_of(w)
    scale_ = w.fixtures.get("condition_scale")

    # -- THE DRAW IS PER EATER, UP THE LARDER LADDER (item 3a) -------------------
    #
    # ⚠⚠ ~~PER RUNG, AGAINST THAT RUNG'S OWN STORES~~ -> PER EATER, AT `nearest_store`. Struck
    # and kept, because the old shape was not wrong so much as UNREACHABLE. `H-11` says *draw
    # from the containing rung's stores, scaled by weight*, and that is still exactly what this
    # does — for a rung that HAS stores. MEASURED on `build_realm(0)` after one season, before
    # this change: **4,810 units, all 4,810 at the 37 settlement rungs, 0 at the 211 hearths**,
    # 46 persons in 26 hearths, and **0 rungs with both eaters and stores**. So the old
    # `draw = {k: wt * len(eaters)}` counted zero eaters wherever there was anything to eat, and
    # the whole subsistence step was inert on the world that ships.
    #
    # ⚠ `p.weight`, NOT `len(eaters)`, AND THE OLD LOOP DROPPED IT. `Person.weight` is the cohort
    # multiplier — *"A COHORT IS A PERSON AT weight > 1"* (`state/carriers.py`) — so counting
    # heads makes a cohort of two hundred eat like one man. Every person in the shipped corpus was
    # at weight 1, which is exactly why this was invisible and why it was fixed while it cost
    # nothing to fix.
    #
    # ⚠⚠ AND SINCE PLAN POSITION `24f` ONLY A COHORT EATS (`ED-IN-0255`: subsistence is *"a
    # territorial issue"*, carried by *"NPC synecdoches"*, and *"lords and guild members"* do not
    # worry about it). The exemption is `world_q.subsistence_draw`'s, the one owner, so nothing
    # below changes: a `weight == 1` person is simply absent from `record`, so he is never in
    # `draws`, never in `short_by_person`, and item 3b below never falls his body for dearth. The
    # eaters are `cohorts.yaml`'s authored rows, one per populated rung, seated at world-gen by
    # `harness/populated.py::build_realm`. `tests/test_territorial_subsistence.py` holds the
    # falsifier on the built realm: under a non-zero `body_step`, an office-holder under a
    # settlement in dearth keeps his body while that settlement's cohort draws and its body falls.
    #
    # ⚠ THE PRE-PASS EXISTS TO KEEP THE EMISSION ORDER, not because the arithmetic needs it. The
    # draw could be hoisted into its own pass over persons, and that would reorder every
    # `stores.changed` relative to its rung's `yield.taken` across the whole season — a golden
    # move for a reason that has nothing to do with this change. Accumulating per SOURCE rung and
    # applying it inside the existing per-rung loop leaves `test_w8_matter_draws_before_it_
    # produces_which_is_353s_stated_order` measuring what it was written to measure.
    #
    # ⚠ AND THE RUNNING VIEW IS WHAT MAKES SCARCITY BIND. The writes are deferred to the gate, so
    # without `left` every eater would be shown the FULL larder and two of them could spend the
    # same unit — `loop/effects.py`'s own header names that defect for `transfer`.
    # `band_floors["body"]` — the SAME table the site gate and `decision.budget` already read.
    # `H-38` closed with *"`Site.condition` is the model"*, and this spends that closure rather
    # than minting a `band_floors.person` second scheme.
    floors_body = (w.fixtures.get("band_floors") or {}).get("body", {})
    # ⚠ PLAN POSITION `19d`: THE ARITHMETIC ABOVE NOW LIVES IN ONE OWNER, `world_q.subsistence_draw`,
    # and this pass derives its writes from the record it returns. The inline loop that stood here
    # (per housed eater, sorted; per weighted kind, sorted; `nearest_store` over the running `left`
    # view; `take = min(want, held)`) moved there VERBATIM, because `demanded`/`delivered` need the
    # same arithmetic. A second copy would let MATTER feed a person the Queries call hungry. Since
    # v9 IN-07 E1 the arithmetic is the `settlements.larder_draw` module entry's
    # (`modules/settlements/larder.py`; the walk was `nearest_store`), and `subsistence_draw` is
    # its host projection, keeping the record's shape and order. The derivation below reproduces `draws` and `short_by_person` exactly, in the same insertion
    # order. That order reaches `r.stores.update(...)`'s key order, and with it the content hash.
    record = world_q.subsistence_draw(w)
    draws: dict = {}          # source rung -> {kind: units it gives up}
    short_by_person: dict = {}
    drained: dict = {}        # source rung -> {kinds it RAN OUT OF with a mouth still unfed}
    for pid, (_home, row) in record.items():
        for k, (want, take, src) in row.items():
            if src is not None:
                draws.setdefault(src, {})[k] = draws.setdefault(src, {}).get(k, 0) + take
            if take < want:
                short_by_person.setdefault(pid, {})[k] = want - take
                if src is not None:
                    drained.setdefault(src, set()).add(k)
    # -- THE SHORTFALL RIDES ON THE DRAINED LARDER'S OWN WRITE (plan position `19d`) -------------
    #
    # A larder that runs dry while a mouth is still unfed is the one moment the gap between
    # `demanded` and `delivered` becomes a fact at a PLACE. This records it there as an
    # `Observation` on the `stores.changed` Event that the same write already emits:
    # `(rung, "shortfall:<kind>", demanded - delivered)`. WITNESS deposits it into whoever witnesses
    # that write: anyone standing at the rung (`co_located`) and anyone holding it
    # (`document_key`). `decision/options.py::_from_shortfall_claim` then reads `kind` and `amount`
    # off the claim, so a `transfer` formed from the question the claim raises carries both, and its
    # `to` is the drained rung itself (the question's referent).
    #
    # ⚠ NO NEW EVENT, NO NEW KIND, NO NEW WRITE, AND EACH IS REFUSED FOR A REASON. A shortfall is not
    # a state change (L3: an aggregate is never a field, so there is nothing to write), and a
    # hand-built `subsistence.short` Event would need an anchor that `anchor_of` can reach. `_crossings`
    # anchors on the write that crossed; a rung with no write has no receipt to name. The larder
    # write DOES exist at exactly this moment. A drained source was drawn (`take >= 1`: the larder walk
    # only returns a rung holding `> 0`), so the gate emits `stores.changed` there, and
    # `Event.observed` is the field for *what was read to reach this Event* (`W-B`). Only its
    # writer is new, here at MATTER.
    #
    # ⚠ L5 HOLDS: THE OBSERVATION DECIDES NOTHING. Nobody is starved into an act here. A witness holds
    # a claim, the claim may raise a `claim_landed` question, and any transfer is that person's own
    # choice (S36.1: *"every arrow is a person's act"*).
    #
    # ⚠ WHAT THIS DOES NOT REPORT, and it is registered, not hidden (`H-160`):
    #   * A LARDER THAT WAS NEVER STOCKED. An eater whose walk finds nothing (`source None`) drains
    #     no rung, so no write carries the gap. The emission is the CROSSING into dearth, not the
    #     state: once a place has run dry and been reported, its next empty season is silent, like a
    #     band that is crossed once.
    #   * (LIFTED at v9 IN-22; `world_q.governors_of`, `witness.py::SEAT_CHANNEL`.) A GOVERNOR WHO
    #     NEITHER STANDS AT THE RUNG NOR HOLDS IT: WITNESS now deposits this record into every live seat whose purview contains it.
    # The value is the SUBTREE's gap (`demanded(w, S) - delivered(w, S)`), not only the part owed by
    # eaters whose walk ended at `S`. It counts people under `S` fed short by a larder below `S`,
    # and so NESTS: a hearth larder and its settlement's can both report one hungry household. That
    # is the Query's own meaning, and it is stated here rather than hidden.
    #
    # ⚠ MEASURED ON THE SHIPPED WORLDS (2026-09-29): none drains a larder with a mouth unfed. The
    # populated realm holds nothing before its first yield (every eater's `source` is `None`) and is
    # in surplus after it. `tiny_world` never runs its hearth dry mid-take. The corpus's 178 built
    # worlds hold stock (234 `transfer.made` among them) and record 0 shortfalls. So every
    # committed artifact is byte-identical, and the mechanism fires only where the world is
    # actually scarce (`harness/scarce.py`).
    short_seen: dict = {}     # drained rung -> (Observation, ...), sorted by kind
    for src in sorted(drained):
        need, got = world_q.demanded(w, src, record), world_q.delivered(w, src, record)
        short_seen[src] = tuple(
            Observation(src, f"{SHORTFALL_PREDICATE}:{k}", need[k] - got.get(k, 0))
            for k in sorted(drained[src]) if need.get(k, 0) > got.get(k, 0))
    if short_by_person:
        # ⚠ A SHORTFALL EMITS NOTHING AND DECIDES NOTHING, on L5's rule: a threshold crossing
        # *"MAY NEVER PRODUCE AN OUTCOME"*. Inventing starvation here would be the outcome L5
        # forbids, and it would be a social consequence written at MATTER, which is L4. It is
        # recorded so a run can be read. ⚠ IT IS NOW KEYED ON THE PERSON RATHER THAN THE RUNG,
        # which is the shape item 3b needs — the shortfall is what falls a BODY, and a body
        # belongs to a person. Since `24f` that person is always a cohort: the territorial
        # population's body, never a lord's.
        sample = dict(sorted(short_by_person.items())[:5])
        TRACE.note(
            f"{len(short_by_person)} eater(s) could not meet subsistence; "
            f"{'first 5 of them' if len(short_by_person) > 5 else 'all of them'}: {sample}"
            f" -- recorded, not acted on (L5: a crossing produces no outcome). The FULL set is "
            f"`World._subsistence_shortfall`, which `census` counts")
    # Reported by `census`, never read by the loop — the same treatment `_tie_census` gets. It is
    # what makes the shortfall MEASURABLE rather than only traceable, and it is item 3b's input.
    w._subsistence_shortfall = short_by_person

    # -- THE SHORTFALL FALLS A BODY (item 3b) -----------------------------------
    #
    # ⚠⚠ `AX-5` NAMES THREE SELF-MOTIONS AND BODIES IS THE ONE WITH NO WRITER. Matter wears,
    # memory decays, and a body did nothing at all — so an empty larder was a number in a trace
    # and never a fact about anybody. The write matrix has licensed `(Person, body)` at
    # `[MAT, RES]` (`social: false`, emitting `body.changed` / `person.died`) the whole time; what
    # was missing was a producer at MATTER.
    #
    # ⚠ IT IS STILL NOT AN OUTCOME, AND L5 IS WHY. A body falling and a band being crossed are
    # EMISSIONS. Nobody is starved into an act here; the crossing becomes a `Question` through
    # REACH and the consequence is somebody's own later choice. The one thing that follows
    # mechanically is death at zero, and that is `(Person, exists)`'s own licensed cell rather
    # than a social consequence written at MATTER.
    #
    # ⚠ THE READ/WRITE ASYMMETRY `CLAUDE.md` §0.1 pt 1 IS ABOUT, AND IT IS WHY THIS WRITES
    # `w.persons[pid]` RATHER THAN A LOCAL. `decision.budget` reads `p.body` TODAY, through the
    # `_TenureView`-backed person the world holds. A write landing on a copy — or on a `Person`
    # the rehome replaced — leaves every reader seeing the full body forever, with every test
    # still green. `LB-3b` asserts the crossing AND the budget drop for exactly that reason:
    # either half alone is satisfiable by a write nobody reads.
    step = w.fixtures.get("body_step")
    for pid in sorted(short_by_person):
        person = w.persons.get(pid)
        if person is None:
            continue
        lost = step * sum(short_by_person[pid].values())
        if lost <= 0:
            continue                      # the `body_step = 0` control arm: nothing moves
        was = person.body
        prior_b = w.last_emission_of("body.changed", pid)
        _m = len(w._emitted_by_write)
        w.write("body", token,
                lambda person=person, lost=lost: setattr(person, "body", max(0, person.body - lost)),
                record_kind="Person", fieldname="body", driver="Event",
                emits="body.changed", subject=pid,
                causes=[prior_b] if prior_b else [ROOT])
        fell = w._emitted_by_write[_m] if len(w._emitted_by_write) > _m else None
        emitted.extend(_crossings(w, pid, floors_body, was, person.body,
                                  fell.id if fell else None))
        if person.body <= 0:
            # death through the one owner: see _die
            _die(w, token, pid)

    # -- THE BODIES CLOCK: AGEING AND ILLNESS (v9 IN-34, FORCE-BODIES) ------------
    #
    # #457 D2 answered [medium; Jordan to correct]: ageing and illness are in scope, a HAZARD READER
    # only, rates swept. The hazard is `world_q.body_hazard` -- a Query over `Person.born` -- and
    # this pass is its one writer: ONE KEYED DRAW per living person (`draw_factory`, keyed on
    # (world_seed, tick, pid, purpose), so the same seed gives one death and no other stream moves).
    # Read AFTER the hunger pass, so a person who starved this barrier is already gone and cannot
    # die twice.
    # ⚠ THE CONTROL TAKES NO DRAW: both rates ship at 0 and the pass is skipped at the `if` below, so
    # the season is today's. A NaN or negative rate is truthy, enters, and `body_hazard` refuses it.
    # ⚠ WHAT THE DEATH REACHES: an actorless `person.died` is placed where `remove_person` took him
    # out (`world_q.event_place`, H-206), so persons standing there hold claims naming the dead
    # holder. NOT BUILT: claims naming his OFFICE or closed HOLD (H-206's NOT DONE).
    if float(w.fixtures.get("age_step")) or float(w.fixtures.get("illness_rate")):
        keyed = draw_factory(w.world_seed, lambda: w.tick)
        for pid in sorted(w.persons):
            hazard = world_q.body_hazard(w, pid)
            if hazard > 0 and keyed(pid, "body_hazard").random() < hazard:
                _die(w, token, pid)

    for rid in sorted(w.rungs):
        r = w.rungs[rid]
        draw = draws.get(rid)
        if draw:
            have = dict(r.stores or {})
            # The pre-pass already capped every take at what was there, so this cannot go
            # negative and `max(0, ...)` would only hide an arithmetic error.
            after = {k: have.get(k, 0) - amt for k, amt in draw.items()}
            if any(after[k] != have.get(k, 0) for k in after):
                prior = w.last_emission_of("stores.changed", rid)
                # `observed=`: the shortfall this draw left at `rid` if it ran dry here (`19d`,
                # above). Empty for every larder that met its mouths, which is every one the
                # shipped worlds draw.
                w.write("stores", token,
                        lambda r=r, after=after: r.stores.update(after),
                        record_kind="Rung", fieldname="stores", driver="Event",
                        emits="stores.changed", subject=rid,
                        causes=[prior] if prior else [ROOT],
                        observed=short_seen.get(rid, ()))
        # `yield` — #353 §25's *"only here"* row. The base is the SITE's, scaled by its
        # condition and then by `season_factor`, so a worn place produces less without a
        # second wear concept (`H-93`, and `rosters.yaml: site_yield` for why).
        produced: dict = {}
        # ⚠ THE SITE'S OWN `rung`, NOT THE RUNG'S `sites` LIST. The first version read
        # `r.sites`, and that list is a BACK-REFERENCE NOTHING MAINTAINS — it is empty for
        # every rung in the corpus, so the whole yield step was INERT and would have shipped
        # as an unreachable barrier stage. `Site.rung` is the maintained side (S12), and
        # reading the side that is actually written is the difference between a step that
        # runs and a step that merely exists (§0.2). Caught by `F10` failing for a different
        # reason and then looking at the fixture.
        for site in sorted(w.sites.values(), key=lambda x: x.id):
            if site.rung != rid:
                continue
            for k, base in (SITE_YIELD.get(site.kind) or {}).items():
                produced[k] = produced.get(k, 0) + int(
                    base * (max(0, site.condition) / scale_) * factor)
        produced = {k: v for k, v in produced.items() if v}
        if not produced:
            continue
        prior_y = w.last_emission_of("yield.taken", rid)
        w.write("yield", token,
                lambda r=r, produced=produced: object.__setattr__(r, "yield", dict(produced)),
                record_kind="Rung", fieldname="yield", driver="Event",
                emits="yield.taken", subject=rid,
                causes=[prior_y] if prior_y else [ROOT])
        prior_s = w.last_emission_of("stores.changed", rid)
        credited = {k: (r.stores or {}).get(k, 0) + v for k, v in produced.items()}
        w.write("stores", token,
                lambda r=r, credited=credited: r.stores.update(credited),
                record_kind="Rung", fieldname="stores", driver="Event",
                emits="stores.changed", subject=rid,
                causes=[prior_s] if prior_s else [ROOT])

    # -- TRAVEL: A LEG ENDS HERE (plan position `19c`, the ride-along) --------------------------
    #
    # ⚠⚠ THE MATTER HALF OF `(Person, travel_leg)`'s `steps: [MAT, RES]`, AND ITS ABSENCE WAS A
    # LIVE DEFECT, NOT A MISSING FEATURE. `_eff_move` appends every destination to
    # `Person.travel_leg` at RESOLVE and nothing ever emptied it (the only other writer was a probe),
    # while `decision/budget.py` subtracts `len(p.travel_leg) * budget_leg_penalty` from EVERY
    # season's budget. So a person who had moved N times in their life was N scenes short in every
    # season after -- MEASURED before this pass on `build_realm(0)`: 14 legs held after two seasons,
    # 14 moves executed, and none ever returned. `ARCHITECTURE_V2.md` §D4 names the field *"the
    # movement in progress"* and gives arrival to the `contain` edge, which `_eff_move` already
    # re-homes at RESOLVE; what was never written is the end of the movement. #353 §25 names
    # TRAVEL as one of MATTER's motions, in this order: *"Events resolve FIRST, then bodies,
    # larders, yield, travel, wear"* -- so it sits after the larder/yield loop above and before
    # the wear loop below, which is where it is.
    #
    # WHAT THE PENALTY NOW MEANS. A `move` in season t adds a leg at RESOLVE; the rounds after it in
    # season t read the leg (`deliberate.py`'s queue key carries `travel_leg`, so the smaller budget
    # re-opens the traveller's triage), and season t+1's MATTER ends it. The distance penalty is a
    # cost of THE SEASON YOU TRAVEL IN, and nothing after it.
    #
    # ⚠ ONE WRITE PER TRAVELLER, AND IT EMITS, BECAUSE `H-12` IS RULED: *"MATTER emits an Event per
    # write so crossings have an antecedent"*, and `World.write` refuses a MATTER write on a row that
    # declares `emits:` without naming one. `travel.moved` would report a move that did not happen,
    # so the row declares a second kind, `travel.ended` (`write_matrix.yaml`). It is witnessed like
    # every MATTER emission -- the traveller and whoever stands where they arrived learn that the
    # journey is over. Its cause is the move that laid the last leg, so the walk is
    # `travel.ended -> travel.moved -> the act`; a leg no act laid (a probe's hand-set list) roots
    # at `[ROOT]`, as a licensed clock's genuine first emission does.
    #
    # REJECTED, each for a reason: ending the leg at the traveller's NEXT act (it would never end for
    # a person who then does nothing, which is the defect with a delay); a per-leg tick so `budget`
    # counts only this season's legs (the list would still grow without bound, and `budget` is
    # person-side and reads no clock); a guard over `travel_leg` (`CLAUDE.md` §0.1 pt 5 -- a one-off
    # defect, fixed at its one missing writer; the plan says *"No guard"*).
    for pid in sorted(w.persons):
        traveller = w.persons[pid]
        if not traveller.travel_leg:
            continue
        # `written=True`: `travel.moved` is act-caused, so its anchor is its actor -- or, for a covered
        # mover (v9 IN-12 step 10), the cover's id -- and the lookup by anchor missed it; the Event's
        # own receipt names the mover either way.
        prior_leg = w.last_emission_of("travel.moved", pid, written=True)
        w.write("travel_leg", token,
                lambda traveller=traveller: setattr(traveller, "travel_leg", []),
                record_kind="Person", fieldname="travel_leg", driver="Event",
                emits="travel.ended", subject=pid,
                causes=[prior_leg] if prior_leg else [ROOT])

    # S25: NO SOCIAL QUANTITY MOVES HERE. L4 at its sharpest.
    scale = w.fixtures.get("condition_scale")
    # v9 IN-35: the lattice coupling, read off every Site's opening condition BEFORE the parallel map
    # writes one (`_lattice_strain`). `{}` at the shipped weight 0, so `wear` below is today's.
    pull = _lattice_strain(w, scale)
    w._in_parallel_map = True
    floors_all = w.fixtures.get("band_floors")
    for s in w.sites.values():
        before = s.condition
        # NO SILENT DEFAULT -- unregistered kind raises. Plus the coupling's pull: ONE wear write, so
        # one `condition.worn` and one crossing check per Site whatever moved it.
        wear = w.fixtures.wear(s.kind) + pull.get(s.id, 0)
        # `W4`. WEAR IS A LICENSED CLOCK, AND A CLOCK CHAINS TO ITSELF. `[ROOT]` is for the
        # campaign seed and a licensed clock's GENUINE FIRST emission (#353 `:682-685`); every
        # later tick of the same clock names the tick before it. So the number of `[ROOT]`
        # causes stops growing after season 1, which is `W4`'s stated proof and is asserted
        # rather than printed (`G3`). Handing every emission the root instead is what made the
        # `W9` artifact's entire log unwalkable.
        prior_wear = w.last_emission_of("condition.worn", s.id)
        _mark = len(w._emitted_by_write)
        w.write("condition", token,
                lambda s=s, wear=wear: setattr(s, "condition", max(0, s.condition - wear)),
                record_kind="Site", fieldname="condition", driver="Event",
                emits="condition.worn", subject=s.id,
                causes=[prior_wear] if prior_wear else [ROOT])
        # ⚠ THE TAIL SINCE THIS WRITE, NOT THE WHOLE BUFFER. The first version CLEARED the
        # buffer before each site so `[-1]` would be this site's wear — which also threw away
        # every earlier emission of the barrier, and the barrier's emissions are what MATTER
        # must return so they can be witnessed. Marking the position keeps both.
        worn_ev = w._emitted_by_write[_mark] if len(w._emitted_by_write) > _mark else None
        # S12.1 / L5: A BAND EDGE CROSSING IS AN EMISSION, NOT A WRITE.
        #
        # ⚠ REV 3. Rev 2 appended a row for EVERY site EVERY season regardless of whether
        # any band was crossed, and NEVER CONSTRUCTED AN EVENT -- so nothing was
        # witnessable and nothing entered the log, while the probe that read it claimed
        # "L5 exactly... THE COUNTER COMPELS SOMEONE TO ACT". Half of L5 was missing and
        # the other half was a filter on "did the number change at all", which wear
        # guarantees. A crossing now fires only on a REAL band edge and EMITS.
        emitted.extend(_crossings(w, s.id, floors_all.get(s.kind, {}), before, s.condition,
                                  worn_ev.id if worn_ev else None))
    w._in_parallel_map = False
    # ⚠ THE EMISSIONS `write()` MADE ARE PART OF WHAT MATTER PRODUCED, AND LEAVING THEM OUT
    # MADE THEM UNWITNESSABLE. `emitted` is built by hand from explicit `append`s; `W4` moved
    # emission into `write()`, which appends to `w.log` and to this buffer but not to the list
    # `season()` hands to WITNESS. The measurable consequence: `condition.worn` and
    # `claim.decayed` were the ONLY kinds in the log that reached NO ledger — about a hundred
    # events a season that existed and that nobody could witness, in a design whose §61
    # fan-out is TOTAL. Found by measuring W6's starting state, not by reading.
    #
    # ⚠ AND `claim.deposited` IS DELIBERATELY NOT HERE. It is emitted during WITNESS, about a
    # person's own interior ledger. Fanning it would mean everyone learns what everyone else
    # remembers, AND it would close a loop — a deposit emits, the emission is witnessed, that
    # deposit emits — growing without bound. MATTER's barrier ends here; WITNESS's own
    # emissions are not MATTER's output.
    emitted.extend(w._emitted_by_write)
    w._emitted_by_write.clear()
    TRACE.step("MATTER", "leave")
    w.frozen = True     # S26.2 -- frozen from END OF MATTER to START OF RESOLVE
    return emitted
