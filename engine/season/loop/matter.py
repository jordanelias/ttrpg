"""`loop/matter.py` -- MATTER -- barrier 2. `04 §A.2`: owns the three motions and the maturation of declared terms; emits per matrix row; token MATTER.

⚠ **THE BODY IS THE DRIVER'S OWN, BOUND BACK ONTO THE CLASS -- NOT A DELEGATING STUB.**
`loop/driver.py` ends with `SeasonDriver.matter = matter`, so `SeasonDriver.matter` IS this
function and `inspect.getsource(SeasonDriver.matter)` returns THIS SOURCE. Eight tests read a
step's body that way -- three of them `witness`'s, one of those a pure NEGATIVE assertion --
and a stub would fail two and silently vacate the third, which is why step 9 of the
decomposition (ED-IN-0203) refused to delegate. Step 5 established the technique when
`class Query` bound module functions as staticmethods.

⚠ **THE TOKEN IS STILL A `WriteClass` PARAMETER AND THAT IS G2's, NOT THIS UNIT's.** `04 §A.3`
row 3 replaces the parameter with an unforgeable token type minted only by the driver; until
that lands, this step passes `WriteClass` exactly as it did inside the class. Unit L5
delivers the MODULE boundary `04 §A.2:134` requires; the write discipline is Arc 2.
"""

from __future__ import annotations

from typing import Optional
from ..data.fixtures import SITE_YIELD
from ..data.matrix import Step, WriteClass
from ..queries import world_q
from ..state.carriers import Event, StateChange
from ..state.ids import H, ROOT
from ..trace_log import TRACE



# -- MATTER -- barrier 2 -- THE WORLD FREEZES AT ITS END (S25) -----------
def matter(self, actorless: Optional[list[Event]] = None) -> list[Event]:
    w = self.w
    w.step = Step.MATTER
    TRACE.step("MATTER", "enter"); TRACE.barrier(2, "MATTER")
    w.discard_caches()
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
                                    "bodies, larders, yield, travel (S25's other rows)"])
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
            ev = Event(H(w.world_seed, w.tick, rid, f"matured:{label}"),
                       "term.matured", rid,
                       [StateChange(rid, "set", "MATTER", "stages", label)],
                       [prior], w.tick)
            w.log.append(ev); emitted.append(ev)
            TRACE.event(ev.id, ev.kind, ev.causes)

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
            w.write("confidence", WriteClass.MATTER,
                    lambda c=c, after=after: setattr(c, "confidence", after),
                    record_kind="Claim", fieldname="confidence", driver="Event",
                    emits="claim.decayed", subject=c.id, causes=[prior])

    # -- LARDERS, THEN YIELD (`W8`) -------------------------------------
    # #353 §25 fixes the ORDER and this code follows it rather than choosing one: *"Events
    # resolve FIRST, then bodies, larders, yield, travel, wear."* So a season's subsistence is
    # drawn against LAST season's stores and production replenishes afterwards, which is a
    # substantive difference — the reverse order would let a rung eat what it had not yet
    # produced, and no rung could ever run short. `test_w8_...order...` asserts it.
    #
    # ⚠ BODIES AND TRAVEL ARE STILL NOT BUILT. Naming them here would suggest otherwise; the
    # `not_implemented` list in this barrier's decision row is where they are recorded.
    weights = w.fixtures.get("subsistence_weight")
    factor = w.fixtures.get("season_factor")
    scale_ = w.fixtures.get("condition_scale")
    for rid in sorted(w.rungs):
        r = w.rungs[rid]
        eaters = world_q.presence(w, rid)
        if eaters and weights:
            # `H-11`: *draw from the containing rung's stores, scaled by weight.* A kind with
            # no weight RAISES rather than drawing nothing (see `rosters.yaml`), so the loop
            # is over the WEIGHTS, which is the registry, not over whatever the larder holds.
            draw = {k: wt * len(eaters) for k, wt in weights.items()}
            have = dict(r.stores or {})
            after = {k: max(0, have.get(k, 0) - amt) for k, amt in draw.items()}
            short = {k: amt - (have.get(k, 0) - after[k]) for k, amt in draw.items()
                     if amt > have.get(k, 0)}
            if short:
                # ⚠ A SHORTFALL EMITS NOTHING AND DECIDES NOTHING, on L5's rule: a threshold
                # crossing *"MAY NEVER PRODUCE AN OUTCOME"*. Inventing starvation here would
                # be the outcome L5 forbids, and it would be a social consequence written at
                # MATTER, which is L4. It is recorded so a run can be read.
                TRACE.note(f"{rid} could not meet subsistence for {len(eaters)} by {short} "
                           "-- recorded, not acted on (L5: a crossing produces no outcome)")
            if any(after[k] != have.get(k, 0) for k in after):
                prior = w.last_emission_of("stores.changed", rid)
                w.write("stores", WriteClass.MATTER,
                        lambda r=r, after=after: r.stores.update(after),
                        record_kind="Rung", fieldname="stores", driver="Event",
                        emits="stores.changed", subject=rid,
                        causes=[prior] if prior else [ROOT])
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
        w.write("yield", WriteClass.MATTER,
                lambda r=r, produced=produced: object.__setattr__(r, "yield", dict(produced)),
                record_kind="Rung", fieldname="yield", driver="Event",
                emits="yield.taken", subject=rid,
                causes=[prior_y] if prior_y else [ROOT])
        prior_s = w.last_emission_of("stores.changed", rid)
        credited = {k: (r.stores or {}).get(k, 0) + v for k, v in produced.items()}
        w.write("stores", WriteClass.MATTER,
                lambda r=r, credited=credited: r.stores.update(credited),
                record_kind="Rung", fieldname="stores", driver="Event",
                emits="stores.changed", subject=rid,
                causes=[prior_s] if prior_s else [ROOT])

    # S25: NO SOCIAL QUANTITY MOVES HERE. L4 at its sharpest.
    w._in_parallel_map = True
    scale = w.fixtures.get("condition_scale")
    floors_all = w.fixtures.get("band_floors")
    for s in w.sites.values():
        before = s.condition
        wear = w.fixtures.wear(s.kind)      # NO SILENT DEFAULT -- unregistered kind raises
        # `W4`. WEAR IS A LICENSED CLOCK, AND A CLOCK CHAINS TO ITSELF. `[ROOT]` is for the
        # campaign seed and a licensed clock's GENUINE FIRST emission (#353 `:682-685`); every
        # later tick of the same clock names the tick before it. So the number of `[ROOT]`
        # causes stops growing after season 1, which is `W4`'s stated proof and is asserted
        # rather than printed (`G3`). Handing every emission the root instead is what made the
        # `W9` artifact's entire log unwalkable.
        prior_wear = w.last_emission_of("condition.worn", s.id)
        _mark = len(w._emitted_by_write)
        w.write("condition", WriteClass.MATTER,
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
        floors = floors_all.get(s.kind, {})
        for verb, floor in sorted(floors.items()):
            if before >= floor > s.condition:
                # `W4`. THE CROSSING'S ANTECEDENT IS THE WEAR THAT CROSSED THE FLOOR, which is
                # `H-12`'s whole purpose -- *"MATTER emits an Event per write SO CROSSINGS HAVE
                # AN ANTECEDENT"*. It read `causes=[ROOT]`, so the one Event in this barrier
                # that exists to be walked back from was rooted at the seed and walked nowhere.
                ev = Event(
                    id=H(w.world_seed, w.tick, s.id, f"crossing:{verb}"),
                    kind="condition.band_crossed", subject=s.id, changes=[],
                    causes=[worn_ev.id] if worn_ev else [ROOT], emitted_at=w.tick)
                w.log.append(ev); emitted.append(ev)
                w.crossings.append((s.id, verb, before, s.condition, ev.id))
                TRACE.event(ev.id, ev.kind, ev.causes)
                TRACE.decision(f"{s.id} crossed the `{verb}` floor", "S12.1/S3-L5",
                               chose="EMIT a witnessable Event; write no social row; produce no outcome",
                               alternatives=["write the consequence directly (L5 forbids: a crossing MAY NEVER PRODUCE AN OUTCOME)",
                                             "silently drop the verb from the set (then nobody can witness it)"])
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
