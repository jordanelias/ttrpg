"""`loop/witness.py` -- WITNESS -- barrier 4, the join. `04 §A.2`: owns claim deposits into each holder's OWN ledger; emits `claim.deposited`; token INTERIOR.

⚠ **THE BODY IS THE DRIVER'S OWN, BOUND BACK ONTO THE CLASS -- NOT A DELEGATING STUB.**
`loop/driver.py` ends with `SeasonDriver.witness = witness`, so `SeasonDriver.witness` IS this
function and `inspect.getsource(SeasonDriver.witness)` returns THIS SOURCE. Eight tests read a
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

from ..data.matrix import Step, WriteClass
from ..data.requires import LEDGER_DERIVED_STEMS, UNKNOWN
from ..data.rosters import OBSERVATION_DEPOSIT_MODES, WITNESS_CHANNELS, require_member
from ..epistemic import act_refs, claim_subjects, observers_for
from ..queries import cache
from ..queries.person_q import LedgerReader
from ..state.carriers import Claim, Event
from ..state.ids import H
from ..trace_log import TRACE



def _told_content(w, act):
    """WHAT A TELLING PASSES ON: the teller's own claim about the act's subject, or `None`.

    A FUNCTION OF THE EVENT ALONE, which is the whole reason it is not inlined in the fan loop:
    the teller and the told-about subject come off the Act, so re-deriving them per HEARER
    repeats a full `LedgerReader` ledger copy and linear scan for every observer of one telling.
    `witness` memoises the result per `e.id`.

    ⚠ `act_refs`, NOT A SECOND READ OF THE PAYLOAD. `epistemic` owns "what is this act about"
    and its reader carries a bare-string branch this file must not re-derive (§8).

    ⚠ `latest_about`, NOT A COMPARATOR WRITTEN HERE. `LedgerReader` owns *the most recent, then
    the most confident*, and `tell`'s `requires` cell names no predicate to read by.

    ⚠⚠ **THIS READS A LEDGER THAT IS NOT THE DEPOSITING PERSON'S, AND `04_CODE_ARCHITECTURE.md`
    §B.2:230 SAYS THAT DOES NOT EXIST.** The row is *"the ledger is never read by ANOTHER person |
    **STRUCTURAL by signature**"*, and its `F8` carve-out is exact: *"the fold may ask the ACTOR'S
    OWN ledger, through the `PersonInterior` snapshot the act carries, and no other. A Query taking
    a ledger and an asker who is not its holder still does not exist."* It does now -- this
    function, called in the WITNESS fan for a HEARER, over the TELLER's live ledger. Measured: it
    is the only such site in the tree; the other production construction (`epistemic.py:99`) passes
    the actor's own claims.

    NOT A GAP IN THE ROW, AND NOT DEFENSIBLE AS SHIPPED -- it is a known non-conformance carried
    deliberately, named here because a `04`-STRUCTURAL row must not go on asserting a property the
    code has stopped having. **The conformant shape is that the told triple RIDES ON THE ACT**, so
    WITNESS reads what the telling carried instead of fetching it: either the resolve-side
    `Observation` channel (`Event.observed`, `W-B`) carrying the claim's own predicate and value
    rather than today's bare `("claim.held", True)`, or the actor's `PersonInterior` supplying it
    at option-build time. Both are grammar work in `data/requires.py` or `decision/options.py`, and
    the second decides at CHOOSE time what a person will say -- a game decision, not a cleanup. So
    it is not taken in the commit that found it, and this note is the record rather than a ledger
    row: `CLAUDE.md` §0's five-step test answers it at step 3 (the design document says which shape
    is right), which makes it work, not an escalation."""
    teller = w.persons.get(act.actor)
    refs = act_refs(act)
    subj = refs[0] if refs else None
    if teller is None or subj is None:
        return None
    return LedgerReader(teller.ledger).latest_about(subj)


# -- WITNESS -- barrier 4 -- THE JOIN (S28) -----------------------------
def witness(self, events: list[Event]) -> int:
    w = self.w
    w.step = Step.WITNESS
    TRACE.step("WITNESS", "enter"); TRACE.barrier(4, "WITNESS")
    w.discard_caches()

    # S28 stage 1: FAN-OUT IS GLOBAL AND ONE PASS, computed from THE PRESENCE INDEX and the
    # five channels. No signals, no subscription table. DO NOT SHARD IT -- the design's
    # predecessor loop was retired precisely because its WITNESS was not global, which made
    # its parallelism claim UNSOUND rather than merely unproven.
    # ⚠ REV 3. Rev 2 keyed the observer set on the Event's subject rung and fell back to
    # THE SUBJECT ALONE when that was empty -- which, because every person has a
    # `person`-kind Rung, made almost every Event private to its own subject. That is a
    # SELF-WITNESS RULE THAT APPEARS NOWHERE IN THE CHAIN: the instrument invented the
    # privacy the design lacks, and then reported the design's privacy gap in a probe
    # that never touched the loop.
    #
    # S61 is explicit about the specified behaviour and this now implements it:
    #   "WITNESS AS SPECIFIED FANS EVERY EVENT TO EVERY PERSON. Nothing said in private
    #    is private. A wrapper does not fix this and must not be presented as fixing it."
    # ⚠ THE SENTENCE THAT STOOD HERE IS FALSE AND WAS CONTRADICTED SIX LINES BELOW IT (corrected
    # 2026-09-20, `ED-IN-0261`). It read: *the five channels are NAMED (S20) and NONE of their
    # predicates is given, so there is no predicate by which anyone could be EXCLUDED; the fan-out
    # is therefore total.* `W6`/`H-33` gave the channels predicates, `rosters.yaml:
    # witness_channel_predicates` carries them, and `fan_out_mode` ships at `all_five` -- the ruled
    # default since 2026-09-07 (R7). S61's total fan is the CONTROL ARM, not the behaviour. A reader
    # taking the old sentence at its word concludes witnessing is unselective, which is how the scar
    # mechanic came to be written against participants instead of observers.
    # Seeds the cache `_ch_co_located` reads. Before `W6`'s adversarial pass this was built
    # here and read NOWHERE -- the predicate rebuilt it per (event, person).
    cache.presence_index(w)
    everyone = list(w.persons)
    # `W6` / `H-33`. THE CHANNELS HAVE PREDICATES NOW, and the mode says which are live.
    # `total` is the specified behaviour and the sweep's control; the presence index this
    # barrier has always built was UNUSED until this line.
    mode = w.fixtures.get("fan_out_mode")
    fan: list[tuple[str, Event, str]] = [
        (pid, e, mode) for e in events for pid in observers_for(w, e, mode, everyone)]
    TRACE.decision(f"fan-out over {len(events)} events -> {len(fan)} deposits", "S28/S61",
                   chose=f"mode={mode} over {len(everyone)} persons "
                         f"({'#353 S61 as specified, and H-33 control' if mode == 'total' else 'H-33 arm; `all_five` is the ruled default since 2026-09-07, R7'})",
                   alternatives=[
                       "shard per rung (retired: made the parallelism claim unsound)",
                       "total (S61's specified behaviour, and H-33's control arm)",
                       f"the five channels {list(WITNESS_CHANNELS)}, each with the predicate "
                       "`rosters.yaml: witness_channel_predicates` injects"])

    # S28 stage 2: DEPOSIT IS PER-PERSON, into that person's OWN ledger and no other.
    cap = w.fixtures.get("ledger_cap")
    conf = w.fixtures.get("confidence_default")
    claim_rule = w.fixtures.get("claim_subject_rule")
    # `W-B` / `H-122`. WHO RECEIVES A CLAIM MINTED FROM WHAT THE FOLD READ. `none` is the
    # CONTROL -- the behaviour before `W-B`, so every measurement of this item has a baseline
    # (§0.1 point 4). Read here rather than inside the loop so the fixture is consulted once
    # per barrier and `Fixtures.reads` counts a barrier, not a deposit.
    obs_mode = w.fixtures.get("observation_deposit_mode")
    require_member(
        obs_mode,
        OBSERVATION_DEPOSIT_MODES,
        f"observation-deposit mode {obs_mode!r} is not in the roster",
        "H-122",
        law="`observers_for`'s precedent, and for its reason: *'an unrecognised mode "
            "silently falling back would make every measurement of this sweep read the "
            "control'*. Here the control is `none`, i.e. depositing nothing, so a silent "
            "fallback would report `W-B` as having changed nothing")
    deposits = 0
    # ⚠ PASS-SCOPED, KEYED BY PERSON -- NOT PER (PERSON, EVENT), WHICH IS WHERE IT WAS BUILT
    # AND WHAT MADE THE DE-DUPLICATION BELOW A CLAIM THE CODE DID NOT DELIVER. `LedgerReader`
    # matches on `(subject, predicate)` and resolves on `(when, confidence)` with a STRICT `>`,
    # so two claims deposited in the SAME barrier with the same `confidence_default` tie on
    # both keys and the FIRST APPENDED wins -- which is the append-order dependence
    # `LedgerReader`'s own docstring says it exists to prevent (*"answering with the first
    # found would make the verdict depend on append order"*). A `seen_obs` created inside the
    # fan loop cannot see a collision across two Events, and `_eff_transfer` mutates
    # `Rung.stores` during RESOLVE, so two transfers on one rung in one season read 8 then 7
    # (`test_wb_two_reads_of_one_cell_in_one_barrier_deposit_exactly_one_claim` builds it).
    # MEASURED over the 86 corpus worlds (`W-B` adversarial pass, 2026-09-04): at `total`,
    # **651 surviving tied groups, 27 of them holding DIFFERENT values** -- e.g. `ARC-01`,
    # `p_a`, `('r_realm','stores:grain',when=4,conf=100)` holding `[168, 167, 167]`. At
    # `actor` it is 0, because one actor rarely acts twice on one rung in one season; the
    # defect is reachable in the shipped grammar and lives in the arm the row also measures.
    # ⚠ WHICH READ SURVIVES IS NOW STATED RATHER THAN LEFT TO A COMPARATOR IN ANOTHER CLASS.
    # Within one barrier every read is equally recent BY `when`, so `LedgerReader` cannot rank
    # them and something must: the first read the fan reaches -- i.e. the earliest Event in
    # RESOLVE order -- is kept, which is the answer `LedgerReader`'s strict `>` already gave.
    # This fix removes the TIE, not the answer.
    seen_obs_by_pid: dict = {}
    # ⚠ WHAT A TELLING CONTAINED, RESOLVED ONCE PER EVENT RATHER THAN ONCE PER HEARER.
    # `_act`, the teller, the told-about subject and the claim being passed on depend ONLY on
    # the Event -- never on `pid` -- but the fan loop below is per `(person, event)`, so the
    # first cut re-derived all four for every observer of the same telling, and
    # `LedgerReader.__init__` COPIES the teller's whole ledger (`list(claims)`) before
    # `latest_about` linear-scans it, up to `ledger_cap` = 200. In a three-person corpus world
    # that is a 2x repeat and invisible. In `harness/populated`'s world it is not: the Church's
    # 25 cases share one building, so one telling repeated a 200-entry copy-and-scan 25 times.
    # A plain local dict fixes it. ⚠ NOT `w.cache()` -- `cache_at_barrier` is `Forbidden` inside
    # `_in_parallel_map` (`state/world.py:474-476`), which is this whole region.
    told_by_event: dict = {}
    w._in_parallel_map = True
    for pid, e, channel in fan:
        p = w.persons.get(pid)
        if p is None:
            continue
        # S28: A KNOT DEPOSIT REUSES THE EVENT ID. Rev 1 wrote the rule and switched it off
        # with `if False`. This is the rule, on.
        via_knot = any(t.kind == "knot" and t.live and pid in (t.subject, t.object)
                       for t in w.tenures)
        src = "firsthand_via_knot" if via_knot else "firsthand"
        # `H-79`: WHAT A DEPOSIT IS ABOUT. #353 §20 types `Claim.subject` and never says what
        # it is for a WITNESS deposit; the instrument used `e.subject`, the ACTOR, which made
        # §F1's Q2 clause "a claim whose subject is SOMETHING THEY HOLD" unreachable and left
        # the narrative substrate empty. `changes[]` already names what an act touched, so
        # this reads the Event the design has rather than adding a field to it (§8.1).
        for n, subj in enumerate(claim_subjects(w, e, claim_rule,
                                                act_refs(self.act_of.get(e.id)))):
            cid = (e.id if via_knot and n == 0
                   else H(w.world_seed, w.tick, pid, f"claim:{e.id}:{n}"))
            # ⚠ `self.round` IS THE LAST ARGUMENT AND `U2` IS WHY. §F1 Q2 is *a claim LANDING in
            # the holder's ledger*, and a season is now several rounds: a claim deposited in round
            # 3 is NEW to a person who last deliberated in round 3, and `when` alone cannot say so
            # because it is the same tick. `questions_for(w, p, since=(tick, round))` compares the
            # pair. Unstamped, every claim would read `round = 0` and a later round's deposit would
            # sort BEFORE the deliberation that should see it — Q2 dead inside the season, which is
            # the exact shape of the bug that kept Q2 dead across seasons before the `tick - 1` fix.
            c = Claim(cid, pid, subj, e.kind, True, w.tick, src, conf, "own", self.round)
            # `W4`. THE DEPOSIT EMITS, AND THAT IS WHAT GIVES A DECAY AN ANTECEDENT.
            # Part D declares `claim.deposited` on this row and NOTHING EMITTED IT, so a
            # claim entered the world uncaused — and every later `claim.decayed` would have
            # had to root at `[ROOT]`, which put 63 spurious roots in a 3-season run and made
            # `W4`'s own ROOT-count proof unsatisfiable. Chained to the witnessed Event, the
            # walk is `decayed -> ... -> deposited -> the act that was witnessed`, which is
            # what #353 §19.4 means by the substrate of the emergent-narrative claim.
            w.write("claim_ledger", WriteClass.INTERIOR,
                    lambda p=p, c=c: p.ledger.append(c),
                    record_kind="Person", fieldname="claim_ledger", driver="Event",
                    emits="claim.deposited", subject=c.id, causes=[e.id])
            TRACE.claim(pid, e.id, src)
            deposits += 1
        # `W-B`. THE SECOND DEPOSIT: ONE CLAIM PER READ THE FOLD MADE, IN THE `requires`
        # VOCABULARY. `Observation` is `(subject, predicate, value)` and so is `Claim`; its
        # own docstring says an Observation *"is what a Claim would be if the reader wrote
        # one"*, and this is the writer.
        #
        # ⚠ WHY THIS IS A SECOND LOOP AND NOT A RULE INSIDE `claim_subjects`. That function
        # answers *what is this deposit ABOUT* for the EVENT-KIND claim, and its
        # `actor`/`per_change`/`both` roster is `H-79`'s, already swept and already measured.
        # An observation-claim's subject is not a choice -- it is the entity the reader read,
        # and the Observation carries it. Overloading `H-79`'s rule would put two decisions on
        # one fixture, which is exactly the defect `H-121` was minted to repair.
        #
        # ⚠ AND THE PREDICATE IS NOT `e.kind`. That is the whole point. The event-kind claim
        # above carries `predicate = e.kind, value = True` -- `travel.blocked`, `act.refused`
        # -- and `belief_contradicts` evaluates `requires_typed` against `LedgerReader`, whose
        # vocabulary is `stores:<kind>` / `condition` / `contain.path:<to>` / `claim.held` /
        # `exists:<kind>` / a relation stem. The two vocabularies are DISJOINT, and `True` can
        # never make a comparator return False, so the belief channel was closed by a theorem
        # rather than by a bug (`H-116`, measured: 0 claims in the derived namespace over a
        # 3-season NPC-088 run before this line existed). These claims are in that namespace
        # by construction, because the Observation's predicate is derived from the cell.
        #
        # ⚠ UNKNOWN IS NOT DEPOSITED, AND THE REASON IS `H-94`'s. A read the world could not
        # answer is the INSTRUMENT'S GAP, and `operands_for` already refuses to mint an act
        # with a hole precisely so that *"the instrument's own gap would become a FALSE BELIEF
        # held by every witness, about a granary nobody named."* Depositing UNKNOWN would
        # reintroduce that from the other end. It is also inert-but-costly: `LedgerReader`
        # returns the stored value, `_as_number(UNKNOWN)` is UNKNOWN, and the clause returns
        # UNKNOWN -- so the claim can never contradict anything while still consuming a slot
        # the cap evicts somebody else for.
        #
        # ⚠ DE-DUPLICATED ON `(subject, predicate)`, WHICH IS THE KEY `LedgerReader.read`
        # MATCHES ON -- AND ACROSS THE WHOLE BARRIER, WHICH IS THE SCOPE THAT READER OPERATES
        # AT. Two claims a reader cannot tell apart are one belief stored twice, and
        # `claim_subjects` gives the same reason for its own de-duplication: a person holding
        # two identical claims would double-count in every eviction comparison. The set is
        # `seen_obs_by_pid` above; the first writing of this scoped it inside the fan loop, so
        # the sentence was true of one Event and false of the pass. See that comment for the
        # measurement.
        if obs_mode != "none" and (obs_mode == "total" or pid == e.subject):
            seen_obs = seen_obs_by_pid.setdefault(pid, set())
            # `e.observed`, NOT `getattr(e, "observed", ())`. The field is on `Event` now, so
            # a default here would be a guard for a case that cannot arise -- and it would
            # SWALLOW the one case worth failing on, an object that is not an Event reaching
            # this barrier. `content_hash`'s `getattr` is a different matter: it is the
            # forward-compatibility fold `W-B` was written against and predates the field.
            for o in e.observed:
                if o.value is UNKNOWN or o.value is None:
                    continue
                # ⚠ AND A READ COMPUTED FROM THE LEDGER IS NEVER DEPOSITED INTO IT. See
                # `LEDGER_DERIVED_STEMS` for the measurement and for the alternative that was
                # rejected. In one line: `WorldReader.read(X, "claim.held")` answers from
                # LEDGER MEMBERSHIP, so storing `(X, "claim.held", False)` puts a claim about
                # `X` in the ledger and makes that read True -- the deposit falsifies its own
                # content, and the person then declines an act the fold would admit. This is
                # the same prohibition as the UNKNOWN guard above, one predicate over: a
                # deposit the instrument cannot stand behind is not deposited.
                if str(o.predicate).partition(":")[0] in LEDGER_DERIVED_STEMS:
                    continue
                key = (o.subject, o.predicate)
                if key in seen_obs:
                    continue
                seen_obs.add(key)
                # `e.id` is in the digest, so the per-person counter need only separate
                # two reads OF ONE EVENT; it spans the pass now and is still strictly
                # increasing, so no two ids collide.
                oc = Claim(H(w.world_seed, w.tick, pid, f"obs:{e.id}:{len(seen_obs)}"),
                           pid, o.subject, o.predicate, o.value, w.tick, src, conf, "own",
                           self.round)   # `U2`: see the deposit above
                w.write("claim_ledger", WriteClass.INTERIOR,
                        lambda p=p, c=oc: p.ledger.append(c),
                        record_kind="Person", fieldname="claim_ledger", driver="Event",
                        emits="claim.deposited", subject=oc.id, causes=[e.id])
                TRACE.claim(pid, e.id, src)
                deposits += 1
        # THE TOLD CHANNEL -- `claim_sources`' `told_by`, WHICH NOTHING WROTE.
        #
        # ⚠ WHAT WAS TOLD, NOT MERELY THAT A TELLING HAPPENED. The event-kind deposit above
        # gives a witness `(subject, "news.told", True)` -- they learn a telling OCCURRED. The
        # content of the telling reached nobody, so `rosters.yaml: claim_sources` declared four
        # sources and the corpus wrote one: MEASURED over the 89 corpus worlds, 23,855 claims,
        # every one `firsthand`, and `standing_of` returning the maximum gap for 267 of 267
        # person-instances because its `told` set is empty by construction. `tell` is the one
        # verb whose entire purpose is transmission and it transmitted nothing.
        #
        # ⚠ THIS IS A WITNESS RULE AND NOT AN EFFECT, AND THE REASON IS `CLAUDE.md` §8. An
        # effect body would have to recompute WHO HEARD IT, and the fan is this barrier's --
        # `observers_for` with the mode. A second owner of the observer set is exactly the
        # divergence `04 §A.2` gives this step the ledger for. `tell` keeps `writes: []`,
        # correctly: a telling changes no cell in the world, it changes what people hold.
        #
        # ⚠ THE TELLER NEEDS NO SEPARATE EXCLUSION AND HAD ONE, WHICH IS ONE RULE WITH TWO
        # OWNERS. `pid != _act.actor` stood here; the redundancy guard below SUBSUMES it, because
        # `_held` is by construction a claim the teller holds, so a teller can never pass "does
        # the hearer already hold this". Mutation-testing found it: removing the exclusion alone
        # reddened nothing, which is §0.1 pt 2 saying the second guard could not observe a failure
        # the first did not already exclude. The condition is kept as the CHEAP one — it skips the
        # ledger scan for the common case — and is no longer stated as an independent rule.
        #
        # ⚠ CONFIDENCE IS THE TELLER'S OWN, NOT A DEGRADED ONE, AND THAT IS A DEFERRAL RATHER
        # THAN A CHOICE. Nothing in the chain states how much a hearing costs a belief, and
        # `probes.py` builds every hand-written `told_by` claim at full confidence (`:380`,
        # `:568`, `:650`, `:861`) -- so precedent carries it and inventing a ladder here would
        # author a number the design has not. The DEGREE already decides the thing the design
        # DOES state: `Failure` emits `news.untold`, which is not this kind, so a failed
        # telling transmits nothing.
        #
        # ⚠ AND A LEDGER-DERIVED PREDICATE IS STILL NEVER DEPOSITED, for the reason the
        # observation block gives one screen up: `claim.held` answers from ledger MEMBERSHIP,
        # so storing it makes its own content true.
        _act = self.act_of.get(e.id)
        if e.kind == "news.told" and _act is not None and pid != _act.actor:
            # A `_teller = w.persons.get(_act.actor)` stood here until 2026-09-16 and was never
            # read -- a per-(hearer, telling) dict lookup left from the draft that scanned the
            # teller's ledger inline, before `_told_content` became its one owner. Removed rather
            # than kept: it read as though the teller were still consulted at this point.
            if e.id not in told_by_event:
                told_by_event[e.id] = _told_content(w, _act)
            _held = told_by_event[e.id]
            # ⚠ `act_refs`, NOT A SECOND READ OF THE PAYLOAD. The first writing of this block
            # spelled `(_act.payload or {}).get("subject")` inline -- a copy of `epistemic`'s
            # own reader (`act_refs`, already imported at the top of this file and already
            # called forty lines up) that DROPPED its bare-string branch. Two owners of "what
            # is this act about", disagreeing on an input the tree already contains
            # (`probes.py` builds string payloads), which is §8 exactly. Caught by an
            # adversarial pass, not by a test, because no `tell` reaches that branch today --
            # latent, and latent is still two owners.
            if (_held is not None
                    and str(_held.predicate).partition(":")[0] not in LEDGER_DERIVED_STEMS
                    # ⚠⚠ **A TELLING THAT TELLS SOMEBODY WHAT THEY ALREADY SAW DEPOSITS
                    # NOTHING, AND WITHOUT THIS LINE THE CHANNEL IS ALMOST ENTIRELY THAT.**
                    # MEASURED over the 89 corpus worlds before this guard: 180 `told_by`
                    # claims, of which **175 were a triple the hearer ALREADY HELD
                    # FIRSTHAND** -- one belief stored twice, which is the defect the
                    # observation block forbids in those words one screen up, and it
                    # consumes a `ledger_cap` slot the eviction then takes from somebody
                    # else. The cause is not the mechanism: `corpus_run.build_at` seats all
                    # three persons in ONE rung, so under `all_five` every observer already
                    # witnessed everything the teller witnessed and there is no asymmetry
                    # left to transmit. The honest figure with this guard is **5**.
                    # ⚠ EXACT TRIPLE, NOT `(subject, predicate)`. A hearer who holds a
                    # DIFFERENT value for the same cell is being contradicted, and that is
                    # the epistemic layer working -- `agreement` pairs precisely those. Only
                    # a claim a reader could not tell apart is suppressed.
                    and not any(c.subject == _held.subject and c.predicate == _held.predicate
                                and c.value == _held.value for c in p.ledger)):
                # ⚠ NO SECOND DEDUP SET HERE, AND THE REASON IS THE ONE THAT RETIRED THE TELLER
                # EXCLUSION TWO SCREENS UP. A `seen_told_by_pid` stood here, mirroring
                # `seen_obs_by_pid`. But `World.write` applies synchronously (`world.py:408`),
                # so a deposit made earlier in this barrier is ALREADY in `p.ledger` and the
                # exact-triple guard above catches it. The set only added cover for a
                # DIFFERENT-VALUED retelling of one `(subject, predicate)` inside one barrier --
                # and unlike `seen_obs_by_pid`, which earned its place with a measured 27
                # differing-value collisions, no such case was ever measured here (the channel
                # deposits 8 claims across the whole 89-world corpus). Two guards where one
                # observes the failure is the defect §0.1 pt 2 names.
                tc = Claim(H(w.world_seed, w.tick, pid, f"told:{e.id}"),
                           pid, _held.subject, _held.predicate, _held.value, w.tick,
                           "told_by", _held.confidence, "own", self.round)
                w.write("claim_ledger", WriteClass.INTERIOR,
                        lambda p=p, c=tc: p.ledger.append(c),
                        record_kind="Person", fieldname="claim_ledger", driver="Event",
                        emits="claim.deposited", subject=tc.id, causes=[e.id])
                TRACE.claim(pid, e.id, "told_by")
                deposits += 1
        # ⚠ `while`, NOT `if`. THE CAP WAS NOT A CAP. One deposit can mint SEVERAL claims --
        # `claim_subjects` returns one per `StateChange` under the `per_change` rule -- and a
        # single `if` pops exactly one, so the ledger settled at 203 against `L = 200`. A cap
        # that is exceeded by however many subjects the last Event carried is not the bound
        # `H-09` declares, and every eviction measurement reads off it.
        while len(p.ledger) > cap:
            # S20/S34: EVICTION RANKS ON `confidence_live x recency` ONLY, NEVER SALIENCE.
            # Rev 1 sorted lexicographically on (confidence, when), which is a different
            # comparator and degenerated to insertion order under a constant confidence.
            # ⚠ THROUGH THE GATE. This sorted and popped `p.ledger` DIRECTLY — no `write()`
            # call, on the row `W4` had just made an emitting row. #353 `:1061-1064` is
            # explicit: *"either the gate applies the write, or direct assignment is made
            # impossible"*, and eviction was the second half of that sentence going
            # unenforced. The gate requires an emission only at MATTER, so an INTERIOR
            # eviction passes without one — which is correct here and is also a finding worth
            # naming rather than papering over: **a claim leaving a ledger is a real state
            # change that Part D gives no kind, so nobody can witness a forgetting.** That is
            # `(Person, claim_ledger)`'s version of `H-86` and is recorded on that row.
            # Found by the `W4` adversarial pass.
            p.ledger.sort(key=lambda c: c.confidence * (c.when + 1))
            w.write("claim_ledger", WriteClass.INTERIOR,
                    lambda p=p: p.ledger.pop(0),
                    record_kind="Person", fieldname="claim_ledger", driver="Event")
    w._in_parallel_map = False
    # S9.3/S28: WITNESS NEVER TOUCHES A BELIEF. Nothing above writes `beliefs` or
    # `convictions` -- and under rev 2's Partition both are MISSING rows, so an attempt would
    # raise rather than be caught by inspection.
    TRACE.step("WITNESS", "leave")
    return deposits
