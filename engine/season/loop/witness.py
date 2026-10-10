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
from dataclasses import replace

from ..data.matrix import Step
from ..state.gate import Token
from ..data.requires import LEDGER_DERIVED_STEMS, UNKNOWN, WORLD_ONLY_STEMS
from ..data.rosters import (
    CHANNEL_CLAIM_SOURCE, OBSERVATION_DEPOSIT_MODES, RECORD_CONTENT, WITNESS_CHANNELS,
    require_member,
)
from ..data.verbs import VERB_TABLE
# ⚠ `04:178` lists WITNESS's reads as the log, the presence cache, the channel predicates and the act
# store, and `04:142` keeps `decision/` an island; this is the first non-DELIBERATE step to import it.
# Refraction (v9 IN-15, H-201) is asker-first -- it grades what THIS holder believes -- so its rule lives
# beside `teller_weight`/`record`, which `queries/person_q.py` cannot host (it may not reach
# `epistemic`, test_season_shape's allow-list); it reads the verb table (`_happened`, `dissents`) and the
# holder's own stance (`regard`). `04:178` is exceeded on those two reads. Layer-conformance, B-E close:
# CONVENTION, no scan reads this step's imports; the spec is ambiguous, `decision/` chosen.
from ..decision.options import ledger_weigh, refracted_confidence
from ..epistemic import (SEEN_PREDICATE, _hold_tenure_ends, act_refs, claim_subjects,
                         live_channels, observers_for, seen_of, seen_subject)
from ..queries import cache, world_q
from ..queries.world_q import hold_force
from ..state.attribution import actor_of
from ..state.carriers import Claim, Event
from ..state import ledgers
from ..state.ids import H, draw_factory
from ..trace_log import TRACE

# v9 IN-22: THE SEAT CHANNEL -- the obligee channel (`epistemic._ch_post_remit`), borrowed for its
# `inferred` source and its live/off switch; this route's recipients are seat holders
# (`world_q.governors_of`), not obligees. The purview deposit in `witness` below
# rides it: its claim source is this channel's roster `claim_source:`, and it is live exactly when
# this channel is. Named once here and refused at import if the roster stops carrying it, so a
# renamed channel cannot leave the route silently dead (`RESIDE_KIND`'s shape, `world_q`).
SEAT_CHANNEL = "post_remit"
require_member(SEAT_CHANNEL, WITNESS_CHANNELS,
               f"seat channel {SEAT_CHANNEL!r} is not a `witness_channels` member",
               "rosters.yaml -- witness_channels",
               law="v9 IN-22 -- the purview deposit takes the seat channel's source and switch; a "
                   "name the roster does not carry would leave it dead or unsourced")


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


def _told_content(act):
    """WHAT A TELLING PASSES ON: the `Said` the act carries, or `None`.

    ⚠ IT READS THE ACT AND NOTHING ELSE. What a person will say is decided at CHOOSE --
    `decision/options.py::opening_set` copies `queries/person_q.py::said_of(own ledger, subject)`
    onto `Act.payload["said"]` -- so WITNESS never opens the teller's ledger. It used to: this
    function took the teller's LIVE ledger at the barrier, which is a ledger read by someone who is
    not its holder (`04_CODE_ARCHITECTURE.md` §B.2:245's STRUCTURAL row, `F8` carve-out: *"the ACTOR'S
    OWN ledger ... and no other"*). Moving the read to the Act closes that, and it also fixes WHEN:
    what a hearer receives is what the teller held when they chose to tell, not whatever landed in
    the teller's ledger between CHOOSE and WITNESS (`test_t1_what_hearers_receive_is_decided_at_
    choose_not_at_witness`).

    ⚠ `None` FOR A HAND-BUILT `tell` THAT CARRIES NO `said` -- a telling with nothing on it passes
    nothing on, which is the polarity this channel already has for an empty-handed teller.

    ⚠ `act.payload` IS NOT ALWAYS A DICT (`probes.py` builds bare-string payloads), hence the shape
    test. `act_refs` still owns *what is this act about* (§8); this reads the one other key."""
    pay = getattr(act, "payload", None)
    return pay.get("said") if isinstance(pay, dict) else None


def _circle_of(w, act, rate: float):
    """v9 IN-18 `G6` (`H-197`, confidences): THE CIRCLE A TELLING IS MADE IN, or `None` when it is
    not made in confidence. With chance `telling_privacy` (one draw keyed by the telling's own id, so
    every hearer of one telling agrees and no other stream moves) the circle is `(teller, addressee)`
    -- the act's actor and the value its row's `counterparty:` column names on the payload -- and the
    told deposit stores it as `Claim.visibility` in place of `own`.

    ⚠ IT BINDS WHAT A HEARER MAY RETELL, NEVER WHO HEARS (§10 decision 1: private whispers are not
    built). WITNESS still decides recipiency by presence, so a bystander who overhears a confided
    telling holds the claim under the same circle, and is outside it. Who BREAKS a confidence is
    read at the fold (`loop/resolve.py::_confidence_broken`), off the retelling actor's own ledger.

    ⚠ `0` (the control, shipped) RETURNS `None` AND TAKES NO DRAW, so every deposit is `own` exactly
    as before `G6`. A telling that names no addressee (a hand-built act; a row with no counterparty)
    has no circle of two and is never private. `rate` is `telling_privacy`, read and range-checked
    ONCE PER BARRIER by `witness` beside `refraction_gain` (a value outside [0, 1] raises there,
    `H-190`'s rule, whether or not any telling is deposited)."""
    if rate == 0:
        return None
    row = VERB_TABLE.get(getattr(act, "verb", None))
    pay = getattr(act, "payload", None)
    hearer = pay.get(row.counterparty) if (row is not None and row.counterparty
                                           and isinstance(pay, dict)) else None
    if not isinstance(hearer, str) or hearer == act.actor:
        return None
    if draw_factory(w.world_seed, lambda: w.tick)(act.actor, f"confide:{act.id}").random() < rate:
        return (act.actor, hearer)
    return None


def _told_value(w, pid: str, e: Event, held, told_hash: str = None, stem: str = None) -> object:
    """PLAN POSITION `15b` (r2 `02_THE_WRIT_AND_THE_WORD.md` §A.10, `ED-IN-0222`). WHAT A HEARER
    ACTUALLY RECEIVES, as opposed to what the teller holds: `held.value` unchanged at every band
    but `Partial`, where the copy may be lossy by exactly one of two mechanisms and never both.

    ⚠ THIS READS `held`; IT NEVER WRITES IT AND NEVER TOUCHES THE TELLER'S LEDGER. The caller
    deposits the RETURN VALUE into the HEARER's own ledger; `held` (the `Said` the act carries,
    read by `_told_content`) is not mutated anywhere in this module, which is `RR-P`'s test satisfied
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
    distortion).

    `told_hash`/`stem` are the caller's own precomputed values, when it has them -- BATCH-CLOSE
    FINDING (methodology-close Phase 2, EFFICIENCY): `witness()`'s call site already derives this
    same hash (to mint the Claim id, `f"told:{e.id}"` unchanged) and this same stem (its
    `LEDGER_DERIVED_STEMS` guard, one statement above the call) before ever reaching here, so
    recomputing either a second time was two extra ops -- one a blake2b digest, not a builtin
    `hash()` -- on every hearer x telling deposit at `Partial`. Both default to `None` and are
    derived exactly as before when omitted, so a caller with no precomputed value (the direct-call
    test in `test_season_shape.py`) is unaffected."""
    if e.degree != "Partial":
        return held.value
    if told_hash is None:
        told_hash = H(w.world_seed, w.tick, pid, f"told:{e.id}")
    sel = int(told_hash, 16)
    if stem is None:
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


def _refract(c: Claim, p, channel: str, gain: float, act=None, weigh=None) -> Claim:
    """`c` AS THIS WITNESS RECEIVES IT: `c` with `decision/options.py::refracted_confidence`'s
    confidence (v9 IN-15, `AX-7`'s divergence formula; `H-199`). The one place every deposit below
    passes through, so the five `Claim` constructions share one rule rather than five. The caller
    decides WHETHER to refract (the gain is live and the witness is not the act's own actor); this
    decides HOW MUCH, and only the confidence moves -- id, value, source and chain are `c`'s.
    `act`/`weigh` reach `dissents`' act-level term (`H-201`): passed by the two deposits that report
    an act happening (event-kind and `seen`), `None` from the other three."""
    return replace(c, confidence=refracted_confidence(p, c, channel, gain, act, weigh))


def _happened(act, e: Event):
    """THE ACT `e` REPORTS HAPPENING, or `None` -- what `dissents`' act-level prior (`H-201`) is asked
    of. `e` must be one of the act's verb row's `emits:` and none of its `emits_on_refusal:` (this ROW's
    column, the test `loop/driver.py` applies to *this Event is a refusal*; `verbs.REFUSAL_KINDS` is the
    cross-row union `is_deed` uses, and the two agree today): a witness
    who believed the act could not happen and saw it refused has nothing to doubt. A kind on both
    columns (`tell`'s `news.untold`) cannot say which, and takes no prior. An Event no act caused
    (MATTER, CALENDAR) and an act whose verb has no row report no act."""
    row = VERB_TABLE.get(getattr(act, "verb", None)) if act is not None else None
    if row is None or e.kind not in (row.emits or ()) or e.kind in (row.emits_on_refusal or ()):
        return None
    return act


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
    # (this count is the FAN alone: IN-22's purview extension below appends after it)
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
    # v9 IN-15 / `H-199`: REFRACTION'S GAIN, read once per barrier for the reason `obs_mode` below
    # is. `0` is the control (0.5 ships, H-199): no deposit is refracted and the barrier is the
    # pre-IN-15 one exactly (no `actor_of` call, no ledger scan).
    gain = w.fixtures.get("refraction_gain")
    # v9 IN-18 `G6` / `H-197`: THE CONFIDENCE CHANCE, read and range-checked once per barrier
    # beside `gain`, for the same reason, and handed to `_circle_of` at each told deposit. `0` is
    # the control (shipped): `_circle_of` takes no draw and every told deposit is `own`.
    privacy = float(w.fixtures.get("telling_privacy"))
    if not 0 <= privacy <= 1:        # `not ... <=`, so a NaN is refused too
        raise ValueError(f"telling_privacy {privacy} is not a chance in [0, 1] (H-197)")
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
    # WHAT A TELLING CONTAINED is `Act.payload["said"]`, fixed at CHOOSE (`_told_content`): nothing is
    # resolved per event here any more, and the teller's ledger is not read at this barrier -- so
    # the old order-dependence on whether the teller sorted before the first hearer (plan position
    # `15d`) cannot arise, and no per-event memo is needed.
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
    # ⚠⚠ `hold_force(w, rec.id)` ANSWERS THE RECORD'S FINAL HOLDER FOR THE WHOLE BARRIER, NOT WHO
    # THIS EVENT'S OWN CHANGE INSTALLED (BATCH-CLOSE, methodology-close Phase 1, LOGIC lens). If
    # the same Record changes hold TWICE within one `witness()` call's `events` (e.g. two chained
    # `give`s in one round, A->B then B->C), both events' entries here resolve to the SAME final
    # holder (C) -- so B, who genuinely held the Record however briefly and is the one who received
    # it at their own event, never gets listed as a holder anywhere and mints no `content:<kind>`
    # claim for it; the later dedup (below) then suppresses even the eventual C-side deposit if C
    # also witnessed the first event. UNREACHABLE ON THE CURRENT TREE: `give` is the only verb this
    # loop's `_hold_tenure_ends` scan reaches (`oblige` opens no `hold`, so it never enters
    # `newly_held` at all), and `give` is chooser-unreachable (untyped, `operands_for` never derives
    # it) -- no hand-built test exercises two gives of one Record in one round either. A real fix
    # keys this off the CHANGE's own before/after Tenure diff (`_hold_tenure_ends` already walks
    # it) rather than a fresh `hold_force` read; not taken here, since nothing on the tree reaches
    # this branch to verify a fix against.
    for e in events:
        for c in e.changes:
            for named in (_hold_tenure_ends(w, c.subject) if c.subject else ()):
                rec = w.records.get(named)
                if rec is None or rec.subject_matter is None:
                    continue
                h = hold_force(w, rec.id)
                if h is not None and h.since == w.tick:
                    newly_held.setdefault(e.id, {})[rec.id] = (h.subject, rec)
    # v9 IN-22 (#457 `CARRY-SHORTFALL`, `H-160` limit 2): AN ACTORLESS EVENT'S READS REACH THE SEATS
    # WHOSE PURVIEW CONTAINS WHAT WAS READ. MATTER's larder pass is the one actorless writer of
    # `observed` (`loop/matter.py`, `19d`): a drained larder's `(rung, "shortfall:<kind>", units)`.
    # Before this, that record reached only those standing at the rung or holding it, so a lord
    # whose seat covers the town but who neither holds it nor stands in it never learned -- `reach`'s
    # purview limb admits a claim about the town, and there was never a claim to admit.
    # ⚠ THE READS, NOT THE EVENT. A governor here gets the OBSERVATION deposit only: no event-kind
    # claim, no `seen` claim, no document content -- he did not witness the write, he learns what
    # MATTER recorded about a place under his seat. So no `stores.changed` of any larder anywhere
    # becomes a seat-holder's news; only a read that MATTER actually recorded does.
    # ⚠ PLACE-BOUND, NOT THE BROADCAST r2 `01`/`02` §A.7 RETIRED. The recipients are
    # `world_q.governors_of` -- `state/gate.py::purview_reaches`, the one owner of *is this rung
    # within this seat*, the relation `reach`'s limb 4 is -- per observation subject, so a seat whose
    # rung does not contain the read rung (a sibling territory, a rungless cluster seat) receives
    # nothing. `reach` itself is still not called from here (`01` §A.4.4).
    # ⚠ IT RIDES THE SEAT CHANNEL, AND THAT IS ITS SOURCE AND ITS SWITCH. `SEAT_CHANNEL`'s claim
    # source is the roster's (`inferred`, `ARCH §C.6`: known from the business of the office, not
    # seen), and the route is live exactly when that channel is (`live_channels`): `all_five` (the
    # shipped mode) yes, `presence_only` no; under `total` everyone is already in the fan. Under
    # `observation_deposit_mode: none` nothing is deposited, as for every other witness.
    # ⚠ APPENDED AFTER THE FAN, so every deposit the fan makes lands in the same order as before and
    # a world with no actorless read deposits exactly what it did (a person the fan already admitted
    # to the Event is skipped: the fan's deposit is the stronger source).
    reported: dict = {}
    if obs_mode != "none" and SEAT_CHANNEL in live_channels(mode):
        admitted = {(pid, e.id) for pid, e, _ch in fan}
        for e in events:
            if not e.observed or actor_of(w, e) is not None:
                continue
            for o in e.observed:
                for pid in world_q.governors_of(w, o.subject):
                    if (pid, e.id) not in admitted:
                        reported.setdefault((pid, e.id), set()).add(o.subject)
        by_id = {e.id: e for e in events}
        fan = fan + [(pid, by_id[eid], SEAT_CHANNEL) for pid, eid in sorted(reported)]
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
        # v9 IN-15: `AX-7` -- WHAT EVERYONE ELSE HOLDS OF AN ACT IS A READING, BY CHANNEL, COMPETENCE
        # AND PRIOR BELIEF. Every deposit below passes through `_refract` when this is true. ⚠ NOT
        # FOR THE ACT'S OWN ACTOR: `AX-7`'s layer (2), the performer's understanding of their own
        # act, *"may be wrong ... by its OWN mechanism -- a person does not witness themselves"*,
        # and this formula is layer (3)'s. An Event no person acted (`actor_of` is `None`) has no
        # performer, so every witness of it refracts.
        refracting = bool(gain) and actor_of(w, e) != pid
        # `H-201`: THE ACT THE EVENT-KIND AND `seen` DEPOSITS REPORT, AND HOW THIS WITNESS WEIGHS
        # THEIR OWN LEDGER -- `dissents`' act-level prior, *could the actor have done this, on what
        # I hold*. Read once per (witness, Event), only when refracting, so the control reads
        # neither. `weigh` is taken before this Event's own deposits land: the ones between it and
        # the `seen` deposit (the observation reads) carry no chain and weigh 1.0 under any closure.
        prior_act = prior_weigh = None
        if refracting:
            prior_act = _happened(self.act_of.get(e.id), e)
            if prior_act is not None:
                prior_weigh = ledger_weigh(p, w.fixtures)
        # v9 IN-22: a governor reached by purview (above) receives only the reads about the rungs
        # his seat contains, and none of the other deposits. `None` for every fan witness.
        only = reported.get((pid, e.id)) if channel == SEAT_CHANNEL else None
        # S28: A KNOT DEPOSIT REUSES THE EVENT ID. Rev 1 wrote the rule and switched it off
        # with `if False`. This is the rule, on -- keyed on the knot SOURCE, i.e. on `witness_key`
        # being the strongest channel, as `rosters.yaml: witness_channel_predicates` defines it.
        via_knot = src == "firsthand_via_knot"
        # `H-79`: WHAT A DEPOSIT IS ABOUT. #353 §20 types `Claim.subject` and never says what
        # it is for a WITNESS deposit; the instrument used `e.subject`, the ACTOR, which made
        # §F1's Q2 clause "a claim whose subject is SOMETHING THEY HOLD" unreachable and left
        # the narrative substrate empty. `changes[]` already names what an act touched, so
        # this reads the Event the design has rather than adding a field to it (§8.1).
        for n, subj in enumerate(() if only is not None else
                                 claim_subjects(w, e, claim_rule,
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
            if refracting:
                c = _refract(c, p, channel, gain, prior_act, prior_weigh)
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
        # ⚠ PLAN POSITION `19d`: AN EVENT NO PERSON ACTED HAS NO ACTOR TO KEEP ITS READS PRIVATE TO,
        # SO ITS WITNESSES RECEIVE THEM. `H-122`'s `actor` arm deposits *an act's* reads to the
        # actor alone because the fold reads FROM THE ACTOR'S POSITION: `from` is their own rung,
        # so the value is theirs. MATTER's larder pass is now the one actorless writer of
        # `observed` (`loop/matter.py`, `19d`). What it records is a named rung's shortfall,
        # relative to no holder, and it is what anyone standing at the drained larder or holding it
        # saw. Before `19d`, no actorless Event carried an observation (MATTER's and CALENDAR's
        # emitted `()`), so this clause changed no deposit on any world that existed. The
        # `e.observed` test comes first only to skip `actor_of` for the common empty case. `none`
        # is still the control and deposits nothing.
        if (obs_mode != "none" and e.observed
                and (obs_mode == "total" or (who := actor_of(w, e)) is None or pid == who)):
            seen_obs = seen_obs_by_pid.setdefault(pid, set())
            # `e.observed`, NOT `getattr(e, "observed", ())`. The field is on `Event` now, so
            # a default here would be a guard for a case that cannot arise -- and it would
            # SWALLOW the one case worth failing on, an object that is not an Event reaching
            # this barrier. `content_hash`'s `getattr` is a different matter: it is the
            # forward-compatibility fold `W-B` was written against and predates the field.
            for o in e.observed:
                if o.value is UNKNOWN or o.value is None:
                    continue
                if only is not None and o.subject not in only:
                    continue      # v9 IN-22: a read about a rung outside this governor's seat
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
                # ⚠ AND A READ ONLY THE WORLD ANSWERS IS OBSERVED, NEVER DEPOSITED (`ED-IN-0282`,
                # telling workplan `T4`, batch-2 close `F1`). `WORLD_ONLY_STEMS` is `with` -- where
                # another person is NOW. The person side never reads it back (`LedgerReader`'s early
                # UNKNOWN), but a claim in a ledger is read by everyone who does not ask by stem:
                # `claim.held` accepts any claim on the subject (`world_q`), Q2 raises a question on
                # the hearer for a claim landing about them and `opening_set` forms a `tell` from it,
                # and `said_of` picks the newest non-`seen` claim on a subject whatever its
                # predicate, so a stale `with:` claim could be the content a teller passes on. The
                # same "it fed itself" shape as the `LEDGER_DERIVED_STEMS` guard above, one stem over.
                # Only the LEDGER APPEND is skipped: `Event.observed` still carries the read (the
                # hash-bearing Event is unchanged) and the T4 refusal is the WorldReader's.
                if str(o.predicate).partition(":")[0] in WORLD_ONLY_STEMS:
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
                if refracting:
                    oc = _refract(oc, p, channel, gain)
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
            if refracting:
                sc = _refract(sc, p, channel, gain, prior_act, prior_weigh)
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
        for holder, rec in ((newly_held.get(e.id) or {}) if only is None else {}).values():
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
            if refracting:
                dc = _refract(dc, p, channel, gain)
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
        # ⚠ THE TELLER'S EXCLUSION (`pid != _act.actor`) IS LOAD-BEARING SINCE `T1`. Before it,
        # the redundancy guard below subsumed it (the telling read the teller's LIVE ledger, so a
        # teller could never pass "does the hearer already hold this"). `_held` is now the `Said`
        # fixed at CHOOSE, and at `Partial` the dedup compares the lossy copy, so the teller can pass
        # the guard and must be excluded here; it also skips the ledger scan for the common case.
        #
        # ⚠ CONFIDENCE IS THE TELLER'S OWN, THEN REFRACTED (v9 IN-15): the hearer's copy starts at
        # what the teller held and `_refract` lowers it by the channel the hearer heard the speech
        # through and by what they already held firsthand -- at `refraction_gain` 0 it is the
        # teller's own exactly. The hop itself is still graded at READ
        # (`teller_weight`), never here. The text below is why the start point is the teller's own:
        # Nothing in the chain states how much a hearing costs a belief, and
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
        if e.kind == "news.told" and _act is not None and pid != _act.actor and only is None:
            # A `_teller = w.persons.get(_act.actor)` stood here until 2026-09-16 and was never
            # read -- a per-(hearer, telling) dict lookup left from the draft that scanned the
            # teller's ledger inline, before `_told_content` became its one owner. Removed rather
            # than kept: it read as though the teller were still consulted at this point.
            _held = _told_content(_act)   # the `Said` the act carries -- fixed at CHOOSE
            # ⚠ `act_refs`, NOT A SECOND READ OF THE PAYLOAD. The first writing of this block
            # spelled `(_act.payload or {}).get("subject")` inline -- a copy of `epistemic`'s
            # own reader (`act_refs`, already imported at the top of this file and already
            # called forty lines up) that DROPPED its bare-string branch. Two owners of "what
            # is this act about", disagreeing on an input the tree already contains
            # (`probes.py` builds string payloads), which is §8 exactly. Caught by an
            # adversarial pass, not by a test, because no `tell` reaches that branch today --
            # latent, and latent is still two owners.
            _held_stem = str(_held.predicate).partition(":")[0] if _held is not None else None
            if (_held is not None
                    and _held_stem not in LEDGER_DERIVED_STEMS):
                # PLAN POSITION `15b` (r2 `02` §A.10, `ED-IN-0222`). WHAT LANDS IN THE HEARER'S
                # LEDGER IS `_told_value`'s RETURN, NOT `_held.value` DIRECTLY -- verbatim at
                # every band but `Partial`, lossy by exactly one mechanism there. Computed here,
                # per (event, hearer), because the selection is keyed on `pid` (§A.10.4); `_held`
                # itself stays the teller's own, untouched, for the dedup guard below to compare
                # PREDICATE and SUBJECT against (those two never drift, §A.10.3) while comparing
                # VALUE against what is actually about to be deposited.
                # `_told_hash`/`_held_stem` are handed down rather than recomputed inside
                # `_told_value` -- the same hash mints the Claim id below and the same stem was
                # already derived for the `LEDGER_DERIVED_STEMS` guard above (BATCH-CLOSE, Phase 2
                # EFFICIENCY finding; see `_told_value`'s own docstring).
                # ⚠ COMPUTED ONLY AT `Partial`, NOT UNCONDITIONALLY -- CORRECTED (BATCH-CLOSE,
                # methodology-close Phase 3 terminal critique, F5): the first writing of this line
                # computed the hash for every degree, before the dedup guard below -- but
                # `_told_value` never touches it outside `Partial` (its own first line: `if
                # e.degree != "Partial": return held.value`), and the dedup guard drops most
                # tellings regardless of degree (measured: 175 of 180 corpus-wide). So the
                # unconditional version PAID a blake2b digest on every non-Partial telling this
                # channel reaches, a cost neither the pre-fix code nor `_told_value` itself ever
                # incurred there -- the opposite of the efficiency this fix claimed. Deferred to the
                # Claim-id site below for any degree that is not `Partial`, matching what the
                # pre-fix code actually did.
                _told_hash = (H(w.world_seed, w.tick, pid, f"told:{e.id}")
                              if e.degree == "Partial" else None)
                _told_val = _told_value(w, pid, e, _held, _told_hash, _held_stem)
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
                # ⚠⚠ `T5` (`ED-IN-0282`): THE GUARD SKIPS ONLY A CLAIM THE HEARER HOLDS ON THE SAME
                # ORIGIN. A held copy with an EMPTY chain (firsthand, seen, inferred -- anything not
                # told) always skips: that is the 175-of-180 fix above and it is unchanged. A held
                # TOLD copy skips only when its `chain[0]` is the incoming claim's, because one
                # origin heard by two routes is one witness (`LedgerReader._support` counts an
                # origin once per value anyway, so a second copy of an EQUAL or LONGER chain would
                # only cost a `ledger_cap` slot). ⚠ NOT TRUE OF A SHORTER ONE: a direct copy `(O,)`
                # arriving after a held two-hop copy `(O, X)` of the same origin is skipped here,
                # though `_support` takes the per-origin MAX weight and the direct copy weighs more.
                # Dormant at the shipped defaults, where no two-hop copy forms. A told copy from a
                # DIFFERENT origin does not skip: the second claim is how
                # two independent tellers come to outweigh one. The incoming chain is
                # `_held.chain + (_act.actor,)`, so its origin is `_held.chain[0]`, else the teller.
                _origin = _held.chain[0] if _held.chain else _act.actor
                if not any(c.subject == _held.subject and c.predicate == _held.predicate
                           and c.value == _told_val
                           and (not c.chain or c.chain[0] == _origin) for c in p.ledger):
                    # ⚠ NO SECOND DEDUP SET HERE, AND THE REASON IS THE ONE THAT RETIRED THE TELLER
                    # EXCLUSION TWO SCREENS UP. A `seen_told_by_pid` stood here, mirroring
                    # `seen_obs_by_pid`. But `World.write` applies synchronously (`world.py:408`),
                    # so a deposit made earlier in this barrier is ALREADY in `p.ledger` and the
                    # exact-triple guard above catches it. The set only added cover for a
                    # DIFFERENT-VALUED retelling of one `(subject, predicate)` inside one barrier --
                    # and unlike `seen_obs_by_pid`, which earned its place with a measured 27
                    # differing-value collisions, no such case was ever measured here (the channel
                    # deposited 8 claims across the whole 89-world corpus when this was measured;
                    # T0, 2026-10-01, counted none deposited in `corpus_run` or the realm). Two guards where one
                    # observes the failure is the defect §0.1 pt 2 names.
                    # BATCH-CLOSE FINDING (methodology-close Phase 1, FIDELITY TO PLAN lens):
                    # `RULINGS.yaml` CAT-3 -- store the teller, "one argument, not a lookup" --
                    # was ruled and CLOSED before this position and was missed on a search that
                    # did not reach `proposals/2026-09-17-governance-and-behaviour/`, this
                    # channel's own content-owner directory. `_act.actor` is already in scope
                    # (bound above, this same guard), so this is exactly the one-argument edit
                    # the ruling names -- not a lookup. `T3b` (`ED-IN-0282`): the argument is the
                    # CHAIN, `Claim.chain`, `state/carriers.py` -- the teller's own chain, which
                    # `said_of` copied onto the Act at CHOOSE, then the teller; `Claim.teller` is
                    # its last element, derived. A KEYWORD, never a positional: `chain` sits where
                    # the removed `teller` field did, so a stray string in that slot would be
                    # read as a chain of one-character hops.
                    # `G6` (`H-197`): THE CIRCLE LINE. A telling made in confidence deposits
                    # `visibility == (teller, addressee)` instead of `own`; `_circle_of` owns the
                    # chance (control 0, shipped: `own`, no draw) and the fold reads the circle back
                    # when this holder retells the claim (`loop/resolve.py::_confidence_broken`).
                    _circle = _circle_of(w, _act, privacy)
                    tc = Claim(_told_hash or H(w.world_seed, w.tick, pid, f"told:{e.id}"),
                               pid, _held.subject, _held.predicate, _told_val, w.tick,
                               "told_by", _held.confidence, _circle or "own", self.round,
                               chain=_held.chain + (_act.actor,))
                    if refracting:
                        tc = _refract(tc, p, channel, gain)
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
