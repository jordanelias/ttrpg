"""`loop/witness.py` -- WITNESS -- barrier 4, the join. `04 §A.2`: owns claim deposits into each holder's OWN ledger; emits `claim.deposited`; token INTERIOR.

⚠ **THE BODY IS THE DRIVER'S OWN, BOUND BACK ONTO THE CLASS -- NOT A DELEGATING STUB.**
`loop/driver.py` ends with `SeasonDriver.witness = witness`, so `SeasonDriver.witness` IS this
function and `inspect.getsource(SeasonDriver.witness)` returns THIS SOURCE. Eight tests read a
step's body that way -- three of them `witness`'s, one of those a pure NEGATIVE assertion --
and a stub would fail two and silently vacate the third, which is why step 9 of the
decomposition (ED-IN-0203) refused to delegate. Step 5 established the technique when
`class Query` bound module functions as staticmethods.

⚠ **THE TOKEN IS HANDED IN BY THE DRIVER (G2).** `SeasonDriver.season` mints an INTERIOR `Token`
through `loop/driver.py::mint_token` and passes it as `token`, once per round; every gate write
below presents it. This module constructs none and calls no minter -- `tests/test_g2_token.py`
fails if it does.
"""

from __future__ import annotations

import math

from ..data.matrix import Step
from ..state.gate import Token
from ..data.requires import LEDGER_DERIVED_STEMS, UNKNOWN
from ..data.rosters import (
    CHANNEL_CLAIM_SOURCE, OBSERVATION_DEPOSIT_MODES, RECORD_CONTENT, WITNESS_CHANNELS,
    require_member,
)
from ..epistemic import (SEEN_PREDICATE, _hold_tenure_ends, act_refs, claim_subjects,
                         observers_for, seen_of, seen_subject)
from ..queries import cache
from ..queries.person_q import LedgerReader
from ..queries.world_q import hold_force
from ..state.attribution import actor_of
from ..state.carriers import Claim, Event
from ..state import ledgers
from ..state.ids import H
from ..trace_log import TRACE



def content_value(subject_matter):
    """A `content:<kind>` CLAIM'S VALUE: the document's `subject_matter`, FROZEN -- a tuple of
    `(key, value)` pairs in the kind's own key order, every list a tuple, recursively. `dict(v)`
    gives the mapping back.

    ⚠ FROZEN AND HASHABLE ON `epistemic.Seen`'s PRECEDENT, AND FOR ITS REASON: claim values sit in
    the sets the corpus harness builds over `(subject, predicate, value)`
    (`harness/corpus_run.py`), and a `dict` there is a `TypeError` -- MEASURED, the first writing of
    the deposit rule deposited the Record's mapping itself and `test_w18` died on it. Freezing is
    also what the deep copy was for: a belief that cannot be mutated cannot alias the Record it
    was read from, so nothing done to the document later reaches back into a ledger."""
    if isinstance(subject_matter, dict):
        return tuple((k, content_value(v)) for k, v in subject_matter.items())
    if isinstance(subject_matter, (list, tuple)):
        return tuple(content_value(v) for v in subject_matter)
    return subject_matter


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
    # ⚠ `R8.1`: A `seen` CLAIM IS PASSED ON ONLY WHEN IT IS ALL THE TELLER HOLDS ABOUT THE SUBJECT.
    # The `seen` deposit lands in every co-located witness -- the teller included -- with an
    # identical value, so without this the teller's NEWEST claim about a rung was almost always a
    # `seen` the hearer already held, the exact-triple guard below suppressed it, and the told
    # channel carried nothing: MEASURED at the `R8.1` commit, `build_world(0)`, four seasons, 0
    # `told_by` claims. `seen` is ruled BESIDE the existing deposits, not in place of what a telling
    # carries. Same comparator both times (`LedgerReader`'s one rule); only the pool differs, and
    # a rumour of a sighting still travels when a sighting is all the teller has.
    own = [c for c in teller.ledger if c.predicate != SEEN_PREDICATE]
    return (LedgerReader(own).latest_about(subj)
            or LedgerReader(teller.ledger).latest_about(subj))


def _told_value(w, pid: str, e: Event, held) -> object:
    """PLAN POSITION `15b` (r2 `02_THE_WRIT_AND_THE_WORD.md` §A.10, `ED-IN-0222`). WHAT A HEARER
    ACTUALLY RECEIVES, as opposed to what the teller holds: `held.value` unchanged at every band
    but `Partial`, where the copy may be lossy by exactly one of two mechanisms and never both.

    ⚠ THIS READS `held`; IT NEVER WRITES IT AND NEVER TOUCHES THE TELLER'S LEDGER. The caller
    deposits the RETURN VALUE into the HEARER's own ledger; `held` (the teller's own Claim, read
    by `_told_content`) is not mutated anywhere in this module, which is `RR-P`'s test satisfied
    as an assertion (r2 `02` §A.10.3's table row, verbatim: *"the teller's own ledger --
    `_told_content` READS it and the branch writes the HEARER's ... the draw decided what the
    listener took away, never what the teller meant"*).

    ⚠ TWO BRANCHES, KEYED ON SHAPE, BECAUSE `held.value` IS NOT ALWAYS ABOUT A DOCUMENT. r2 `02`
    §A.10.1/§A.10.2 write the loss function against a `content:<kind>` claim specifically -- one
    dropped `to` id (§A.10.1), or one drifted number "inside the terms" (§A.10.2). MEASURED
    against the live `record_kinds` roster (`rosters.yaml`): `dispensation`/`petition` carry
    `[terms, to, at]` / `[terms, to, from]`, and `terms` is a `PropositionId` -- a bare id string,
    and per §A.10.3 NEVER touched ("the rumour may misremember a number; it may not misremember
    WHICH OUGHT"); `at`/`from` are a rung/person id, also never touched, same row. So a content
    claim's ONLY droppable field is `to`, and there is no numeric field anywhere in this shape for
    the drift branch to act on -- a mismatch between r2's prose (written against a `terms`
    structure that carries a number) and the shipped carrier, said here rather than papered over.
    A content claim whose `to` cannot lose an id (absent, or down to its last remaining member --
    §A.10.1's own floor) is therefore deposited VERBATIM, not drifted: THE HONEST READING WHEN THE
    DESIGN NAMES A MECHANISM THE CARRIER HAS NO OPERAND FOR, rather than inventing one.

    ⚠ THE SECOND BRANCH IS WHERE A BARE NUMBER ACTUALLY LIVES: a claim whose `value` IS itself a
    plain number -- an observation claim's `stores:<kind>` or `condition`, never a `content:`
    claim -- has no `to` key and no document shape, but IS the numeric operand §A.10.2 names.
    Drifted within `told_drift_band` (`H-155`), sign-preserving, never crossing zero -- §A.10.2's
    three clauses, applied to the value directly since there is no `content:` wrapper to reach
    through.

    ⚠ ANYTHING ELSE -- a bare `True`/`False` from an event-kind claim, an `epistemic.Seen` struct,
    any value with neither an addressee key nor a plain number -- carries nothing either branch
    can act on and is deposited VERBATIM. MEASURED: the one told-channel candidate the live
    89-world corpus reaches at `Partial` (`ARC-13`, seed 0, a `finding.none` claim carrying `True`)
    is exactly this shape, so the honest default for the corpus AS IT STANDS TODAY is unchanged --
    a finding about what the corpus currently exercises, not a defect in the branch.

    ⚠ THE SELECTION IS DETERMINISTIC AND SPENDS NO DRAW (§A.10.4). `sel` reuses the SAME hash the
    deposit's own claim id mints from (`H(w.world_seed, w.tick, pid, f"told:{e.id}")`, below and
    at the `tc = Claim(...)` construction) rather than calling `w.draw()` or `draw_factory` --
    both would spend a per-tick ordinal or a fresh RNG stream, shifting every unrelated draw in
    the season, which §A.10.4 forbids in terms: *"the lossy copy must not perturb the stream."*
    Per HEARER, not per telling, because `pid` is in the mix -- two hearers of one telling lose
    different things (§A.10.4's own point: a rumour fans into disagreement, not into one shared
    distortion)."""
    if e.degree != "Partial":
        return held.value
    sel = int(H(w.world_seed, w.tick, pid, f"told:{e.id}"), 16)
    stem = str(held.predicate).partition(":")[0]
    if stem == RECORD_CONTENT.get("predicate") and isinstance(held.value, tuple):
        addressee = RECORD_CONTENT.get("addressee")
        mapping = dict(held.value)
        to_ids = mapping.get(addressee)
        # §A.10.1: exactly one dropped, never the last, never an id that is not there, never
        # THIS hearer's own id if they are named in `to` -- "a rumour can never relieve you of a
        # duty, only mislead you about whose company you are in."
        if isinstance(to_ids, tuple) and len(to_ids) > 1:
            candidates = [i for i, tid in enumerate(to_ids) if tid != pid]
            if candidates:
                drop = candidates[sel % len(candidates)]
                new_to = tuple(tid for i, tid in enumerate(to_ids) if i != drop)
                return tuple((k, new_to if k == addressee else v) for k, v in held.value)
        return held.value  # one addressee, or none at all -- §A.10.1's floor; nothing droppable
    if isinstance(held.value, (int, float)) and not isinstance(held.value, bool):
        before = held.value
        band = w.fixtures.get("told_drift_band")
        max_delta = math.ceil(band * abs(before))
        if before == 0 or max_delta < 1:
            return held.value   # no sign to preserve at 0, or the band drifts nothing (control)
        magnitude = 1 + sel % max_delta
        after = before + magnitude if (sel // max_delta) % 2 == 0 else before - magnitude
        # §A.10.2: bounded AND signed -- `after` never crosses zero and never flips sign. A draw
        # that would do either is clamped back to the same side rather than discarded, so the
        # selection still spends exactly one hash and never re-draws.
        if before > 0 and after <= 0:
            after = before + magnitude
        elif before < 0 and after >= 0:
            after = before - magnitude
        return after
    return held.value  # nothing either mechanism can act on -- deposited verbatim, honestly


# -- WITNESS -- barrier 4 -- THE JOIN (S28) -----------------------------
def witness(self, token: Token, events: list[Event]) -> int:
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
    # Plan position `15d`: the third term is THE CHANNEL that admitted `pid` -- the strongest, by
    # `WITNESS_CHANNELS`' declared precedence -- and no longer the mode, which is `mode` above.
    fan: list[tuple[str, Event, str]] = [
        (pid, e, ch) for e in events for pid, ch in observers_for(w, e, mode, everyone)]
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
    # ⚠⚠ AND IT IS FILLED HERE, BEFORE ANY DEPOSIT, NOT LAZILY AT THE FIRST HEARER (plan position
    # `15d`, found building `19_PLAN.md` step 4 (c)'s falsifier). Filled lazily it read the teller's
    # ledger PART-WAY THROUGH THIS BARRIER'S DEPOSITS, so the answer depended on whether the teller
    # sorted before the first hearer in `w.persons`. When it did, the teller had already received
    # this very telling's event-kind claim, `(subject, "news.told", True)` at `when = tick` --
    # NEWER than anything they held before -- and `latest_about` returned THAT: the telling
    # transmitted the fact of itself, which every hearer had just been given, and the exact-triple
    # guard dropped it. MEASURED on `tiny_world`, teller `p_low` sorted first, holding the subject
    # at confidence 37: no hearer was told anything; at 100 the held claim won only a `(when,
    # confidence)` tie on append order. The teller tells what they held WHEN THEY CHOSE TO TELL,
    # which is the ledger before WITNESS writes to it (RESOLVE writes no ledger).
    told_by_event: dict = {
        e.id: _told_content(w, self.act_of[e.id]) for e in events
        if e.kind == "news.told" and self.act_of.get(e.id) is not None}
    # `R8.1` -- WHAT EACH WITNESS SAW, RESOLVED HERE AND NOT IN THE LOOP BELOW, BECAUSE THE LOOP IS
    # A PARALLEL MAP. `seen_of` asks every live channel which of them admits the witness, and
    # `co_located` reads the barrier's presence index -- which `cache_at_barrier` refuses inside
    # `_in_parallel_map` even when it is already built. `None` means deposit nothing, and it has
    # ONE cause: the Event has no subject to be about. A struct whose every term is `None` IS
    # deposited -- *something happened here and I know nothing about it* is `R8.5`'s document
    # holder exactly.
    seen_by: dict = {}
    for pid, e, _ch in fan:
        subj = seen_subject(w, e, pid, mode)
        seen_by[(pid, e.id)] = (None if subj is None
                                else (subj, seen_of(w, e, self.act_of.get(e.id), pid, mode)))
    # THE DEPOSIT RULE'S TRIGGER (plan position `15`, r2 `02` §A.9): *a held document is a held
    # belief.* A person who COMES TO HOLD a Record this season -- the Record is named in an Event's
    # `changes[]` and its live `hold` opened at this tick -- learns what it says. Resolved per EVENT
    # and before the parallel map, for `seen_by`'s reason: the holder depends on the Event and the
    # world, never on which witness is being served, and `hold_force` reads `w.tenures`.
    # ⚠ `hold_force` IS THE ONE OWNER OF *who holds this*, AND IT RAISES ON TWO. `holonic §15`'s
    # `hold` is 1 PER OBJECT and nothing yet enforces it for Records (r2 `05`'s ⊕R14, position
    # `16`'s release-before-mint); a document with two holders would make *whose belief is this*
    # undecidable, and refusing loudly here is better than depositing into both.
    # ⚠ A `None` CONTENT IS NOT DEPOSITED -- the observation block's precedent below (*a deposit the
    # instrument cannot stand behind is not deposited*) and its cost argument: a claim that says
    # nothing still takes a `ledger_cap` slot the eviction takes from somebody else. Every `text`
    # Record carries `None`, so this rule deposits nothing for the Records the loop minted before
    # it existed -- which is also why it moves no hash on a world that mints only those.
    # ⚠ AND THE RECORD MAY BE NAMED THROUGH ITS `hold` (plan position `16`). `give`'s receipts name
    # the two custody EDGES, not the Record -- `_eff_confer`'s rule on what a receipt may assert --
    # so each change passes through `_hold_tenure_ends` first, the one owner of *a `hold` receipt
    # is about its holder and what it holds* that `claim_subjects` and `seen_subject` already read.
    # That is r2 `02` §A.9's own trigger, *a `hold`-on-Record appearing in `changes[]`*. A Record
    # named directly (`record.created`) passes through unchanged, and a `release` of a Record's
    # `hold` finds no live holder and deposits nothing -- so only a handover newly reaches here.
    content_stem = RECORD_CONTENT.get("predicate")
    newly_held: dict = {}
    for e in events:
        for c in e.changes:
            for named in (_hold_tenure_ends(w, c.subject) if c.subject else ()):
                rec = w.records.get(named)
                if rec is None or rec.subject_matter is None:
                    continue
                h = hold_force(w, rec.id)
                if h is not None and h.since == w.tick:
                    newly_held.setdefault(e.id, {})[rec.id] = (h.subject, rec)
    w._in_parallel_map = True
    for pid, e, channel in fan:
        p = w.persons.get(pid)
        if p is None:
            continue
        # PLAN POSITION `15d` (proceedings `19_PLAN.md` step 4 (b)). THE SOURCE IS THE ADMITTING
        # CHANNEL'S, read off `rosters.yaml: witness_channels.claim_source` -- presence gives
        # `firsthand`, a knot `firsthand_via_knot`, a document, a remit or the public record
        # `told_by`. `channel` is the ONE `observers_for` credited this person to, the strongest by
        # the roster's precedence, so a person in the room who also holds the changed thing is
        # never downgraded to hearsay (step 4's *breaks if wrong*).
        # ⚠ IT REPLACES A SECOND DERIVATION THAT DISAGREED WITH THE FIRST (§8). This line read
        # `any(t.kind == "knot" and t.live and pid in (t.subject, t.object) for t in w.tenures)` --
        # *is this person in ANY knot* -- while `_ch_witness_key`, the channel that admits by
        # knot, asks *are they knotted to THIS Event's anchor*. So a person knotted to anybody at
        # all took the knot source for every Event they saw, and the channel's own answer was
        # discarded one call earlier. MEASURED before the change, headless 3 seasons + the realm's
        # first season + the 143-case corpus at seed 0: the scan was False for every admitted
        # witness, so deleting it moves nothing there. What DOES move is the other direction, and
        # it is the channel's own definition: an anchor with no place, admitted only by
        # `witness_key`'s self clause, now takes the knot source (`rosters.yaml:
        # witness_channels`' note; probe `P21` is the one case that reaches it).
        # ⚠ AND THE TELLING'S SPECIAL CASE IS NOT HERE, DELIBERATELY. `19_PLAN.md` step 4: *"for a
        # telling event specifically, even co-located hearers get told_by -- they heard it told,
        # they did not see the thing."* The THING told is the told channel's claim below, which is
        # `told_by` for every hearer whatever channel admitted them. The event-kind claim this
        # source is for is `(subject, "news.told", True)` -- THAT a telling happened -- and a
        # co-located witness did see that; the same step's artifact is *"a witness who saw the
        # speech directly holds it firsthand"*. Downgrading it would be the downgrade the
        # precedence exists to prevent.
        src = CHANNEL_CLAIM_SOURCE[channel]
        # S28: A KNOT DEPOSIT REUSES THE EVENT ID. Rev 1 wrote the rule and switched it off
        # with `if False`. This is the rule, on -- keyed on the knot SOURCE, i.e. on `witness_key`
        # being the strongest channel, as `rosters.yaml: witness_channel_predicates` defines it.
        via_knot = src == "firsthand_via_knot"
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
            w.write("claim_ledger", token,
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
        # G1b. `actor_of` REPLACES `e.subject` here -- the SHIPPED default is
        # `observation_deposit_mode: actor`, so this branch is the one this unit's own
        # falsifier names: silently vacating it would starve every headless run's `W-B`
        # deposits rather than merely mis-scoping them. Measured equivalent to the field for
        # every act-caused Event (`test_g1b_attribution.py`); for an actorless Event (MATTER's
        # wear, a calendar crossing) `e.subject` held the record it concerned, never a person id,
        # so `pid == e.subject` was already always False there -- `actor_of` returning `None`
        # preserves that by construction rather than by an id-namespace coincidence.
        if obs_mode != "none" and (obs_mode == "total" or pid == actor_of(w, e)):
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
                w.write("claim_ledger", token,
                        lambda p=p, c=oc: p.ledger.append(c),
                        record_kind="Person", fieldname="claim_ledger", driver="Event",
                        emits="claim.deposited", subject=oc.id, causes=[e.id])
                TRACE.claim(pid, e.id, src)
                deposits += 1
        # `R8.1`. THE THIRD DEPOSIT: ONE `seen` CLAIM PER (WITNESS, EVENT), BESIDE THE TWO ABOVE.
        # Its value is `epistemic.Seen` -- `{stratum, marks, who, why}`, each `None` where the
        # admitting channels withhold it -- and its subject is the changed thing, else the RUNG,
        # which is what lets it raise Q2 for everyone standing there (`questions_for`'s
        # `c.subject in mine`). No verb token rides in it: that is the whole difference from the
        # event-kind claim, which still carries `e.kind` verbatim.
        # ⚠ NOT GATED BY `REQUIRES_STEMS`, AND IT SHOULD NOT BE ADDED THERE. That set closes what a
        # verb's `requires_typed:` cell may ASK, and `_require_known_stem` checks verb cells at
        # load, never a deposit; `seen` is declared in `rosters.yaml: observation_terms`, the row
        # `R8.3` names.
        _seen = seen_by.get((pid, e.id))
        if _seen is not None:
            sc = Claim(H(w.world_seed, w.tick, pid, f"seen:{e.id}"),
                       pid, _seen[0], SEEN_PREDICATE, _seen[1], w.tick, src, conf, "own",
                       self.round)   # `U2`: see the first deposit
            w.write("claim_ledger", token,
                    lambda p=p, c=sc: p.ledger.append(c),
                    record_kind="Person", fieldname="claim_ledger", driver="Event",
                    emits="claim.deposited", subject=sc.id, causes=[e.id])
            TRACE.claim(pid, e.id, src)
            deposits += 1
        # THE FOURTH DEPOSIT: THE CONTENT OF A DOCUMENT THIS WITNESS HAS COME TO HOLD (plan position
        # `15`). `(record, "content:<kind>", <subject_matter, frozen>)` -- `content_value` above:
        # the belief is what the document said when it reached this hand, and nothing done to the
        # Record later reaches back into a ledger. `src` like the deposits above -- the admitting
        # channel's source, `firsthand` for every new holder the tree reaches (measured at
        # position `15d`: every content claim the realm holds after one season and after three),
        # and it
        # carries NO attribution: it says *this document says X*, never *the Duke wrote X* (r2 `02`
        # §A.9 -- the separation is what makes a forgery playable). The exact-triple guard is the
        # told channel's, for its reason: one belief is stored once.
        for holder, rec in (newly_held.get(e.id) or {}).values():
            if holder != pid:
                continue
            pred = f"{content_stem}:{rec.kind}"
            said = content_value(rec.subject_matter)
            if any(c.subject == rec.id and c.predicate == pred and c.value == said
                   for c in p.ledger):
                continue
            dc = Claim(H(w.world_seed, w.tick, pid, f"content:{e.id}:{rec.id}"),
                       pid, rec.id, pred, said, w.tick, src, conf,
                       "own", self.round)   # `U2`: see the first deposit
            w.write("claim_ledger", token,
                    lambda p=p, c=dc: p.ledger.append(c),
                    record_kind="Person", fieldname="claim_ledger", driver="Event",
                    emits="claim.deposited", subject=dc.id, causes=[e.id])
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
            _held = told_by_event[e.id]   # resolved before the fan, above -- position `15d`
            # ⚠ `act_refs`, NOT A SECOND READ OF THE PAYLOAD. The first writing of this block
            # spelled `(_act.payload or {}).get("subject")` inline -- a copy of `epistemic`'s
            # own reader (`act_refs`, already imported at the top of this file and already
            # called forty lines up) that DROPPED its bare-string branch. Two owners of "what
            # is this act about", disagreeing on an input the tree already contains
            # (`probes.py` builds string payloads), which is §8 exactly. Caught by an
            # adversarial pass, not by a test, because no `tell` reaches that branch today --
            # latent, and latent is still two owners.
            if (_held is not None
                    and str(_held.predicate).partition(":")[0] not in LEDGER_DERIVED_STEMS):
                # PLAN POSITION `15b` (r2 `02` §A.10, `ED-IN-0222`). WHAT LANDS IN THE HEARER'S
                # LEDGER IS `_told_value`'s RETURN, NOT `_held.value` DIRECTLY -- verbatim at
                # every band but `Partial`, lossy by exactly one mechanism there. Computed here,
                # per (event, hearer), because the selection is keyed on `pid` (§A.10.4); `_held`
                # itself stays the teller's own, untouched, for the dedup guard below to compare
                # PREDICATE and SUBJECT against (those two never drift, §A.10.3) while comparing
                # VALUE against what is actually about to be deposited.
                _told_val = _told_value(w, pid, e, _held)
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
                # a claim a reader could not tell apart is suppressed -- and at `Partial`
                # "a claim a reader could not tell apart" means the LOSSY value, since that
                # is what this deposit is about to assert.
                if not any(c.subject == _held.subject and c.predicate == _held.predicate
                           and c.value == _told_val for c in p.ledger):
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
                               pid, _held.subject, _held.predicate, _told_val, w.tick,
                               "told_by", _held.confidence, "own", self.round)
                    w.write("claim_ledger", token,
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
            # The comparator's owner is `state/ledgers.py` (04 §A.2:149); this closure is the
            # gated write that applies it. ⚠ ONE CLAIM PER WRITE, MATCHING THE PRE-EXTRACTION
            # SEMANTICS -- an earlier wording of this closure called `evict_over_cap(p.ledger, cap)`
            # once, draining every excess claim in a single `w.write`. State-wise that is identical
            # (the sort key never changes between evictions within one call, so popping k off a
            # once-sorted list matches k separate sort-then-pop-one passes) but INSTRUMENTATION
            # is not: `World.write` mints one gate receipt, one `TRACE.write` row and one
            # `self.writes` entry per call, and `harness/report.py`'s "N writes through the gate"
            # plus `_trace_counts` (compared by `harness/delta.py` between two runs) both count
            # those -- so batching silently changed those counts whenever one deposit minted enough
            # claims to evict more than one at a time, which is exactly the case the `while` above
            # this loop exists for (one deposit can mint several claims; see the comment above).
            # Found by a read-only critic, layer-conformance pass, 2026-09-25.
            # ⚠ G2 (merge, 2026-09-27): the second positional argument to `w.write` is the driver's
            # own `Token` for this step, not a bare `WriteClass` -- this closure predates G2's
            # token discipline and is updated to it here rather than at G2's own close, since the
            # two landed on independent branches. `token` is this function's own parameter.
            def _evict(p=p):
                ledgers.evict_over_cap(p.ledger, len(p.ledger) - 1)
            w.write("claim_ledger", token, _evict,
                    record_kind="Person", fieldname="claim_ledger", driver="Event")
    w._in_parallel_map = False
    # S9.3/S28: WITNESS NEVER TOUCHES A BELIEF. Nothing above writes `pursuits` -- its row
    # admits RES only, so a WITNESS attempt would raise rather than be caught by inspection --
    # and `beliefs` is no longer a field (retired 2026-09-25; a belief is a `commit` to an OUGHT).
    TRACE.step("WITNESS", "leave")
    return deposits
