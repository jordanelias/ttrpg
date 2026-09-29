"""`season.state.gate` -- THE RECEIPT MINT AND THE WRITE TOKEN. Where a `Receipt` comes from, and
the type a write must present.

`04:1024` step 3 names *"the gate · the four tokens · the receipt mint · the log"* as one unit of
the critical path. The mint is `Gate`; the tokens are `Token` (G2, below).

WHAT THIS FILE OWNS AND WHAT IT DOES NOT. It owns **the authority to say a write happened**, and
the TYPE of the authority to ask for one. It does NOT own the matrix check, the step check, the
emission rule or the `(kind, field)` keying -- those are still `World.write`, which is ~160 lines
of Layer-2 policy welded to `World`'s own state. G2 changed WHAT `World.write` is handed (a
`Token`, not a bare `WriteClass`) and left WHERE the checks live alone: moving them out of `World`
is not a signature change and no plan position asks for it. **G1a made the receipt unforgeable;
G2 made the write class something only the driver can hand out; G3 (below, `NotYours`) made the
gate ask WHO wrote a Tenure, which every check before it -- row, step, class -- never did; G4
(below, `NoOpReceipt`) made the gate ask WHETHER the write changed anything, and refuse the
receipt when it did not.**

⚠ THE AUTHORIZATION WINDOW, AND WHY IT WAS NOT A PER-CALL RETURN VALUE (G1a) -- AND WHAT G4 CHANGED
ABOUT THAT. The obvious design is `write() -> Receipt`, and G1a found it did not fit the one caller
that matters: `loop/resolve.py`'s `_apply_write` could not know WHAT it changed until the effect
had run, because the effect reported touched ids from inside the `apply()` closure. So the window
opens when a gate write begins and, AT THE TIME G1a/G4 SHIPPED, stayed open until the NEXT gate
write opened its own, or the step barrier closed it; `mint()` outside a window raises. The property
that buys: **you cannot mint a receipt without having just performed a real gate write.** What it
does not buy: a second receipt minted after an unrelated later write would be attributed to that
write.

G4 makes the obvious design fit. An effect now hands the gate a `Change` that NAMES ITS SUBJECTS
BEFORE IT RUNS, so `World.write` reads each subject before and after applying it and mints the
receipts itself, for the subjects that moved and no others (`04 §C.2`: *"before = get();
store._set(); after = get() / before == after or raise NoOpReceipt / r = Receipt(...)"*). The fold
mints nothing any more. The window's open-past-the-write property therefore had no production
consumer left at the time G4 shipped; it was unchanged BY G4 because closing it was `H-131`'s
barrier question, not G4's.

⚠ CORRECTED (methodology close, terminal critique, 2026-09-29): THE LIFETIME DESCRIBED ABOVE IS
STALE. `H-131` was answered, in two passes the same day, by `World.write` wrapping its whole body
in `try`/`finally: self.gate.close()` — so the window no longer survives past the write that opened
it AT ALL: it closes unconditionally at the end of every `World.write` call, success or exception,
never carrying open into a next write or a step barrier. The paragraph above is kept as the
history of why the window shape existed and what G4 did to it; it does not describe `opening()`'s
current lifetime, which is `World.write`'s docstring and `close()`'s own docstring below."""
from collections import Counter
from dataclasses import dataclass
from typing import Any, Callable, Optional

from ..data.matrix import MATRIX, WriteClass
from ..data.rosters import CONFERRAL_BASES, REVOCATION_BASES
from ..gaps import Forbidden, InstrumentDefect, Unspecified
from .carriers import Office, Receipt, Tenure
# ⚠ NO `World` IMPORT, NOT EVEN UNDER `TYPE_CHECKING`: `world` imports this module, and the tree's
# import-cycle instrument (`tests/valoria/test_import_cycle_game_state_npe.py`) reads a guarded
# import as an edge like any other. The functions below take the `World` they are handed and name
# its type as a string only.
from .containment import ancestry, descendants, home_of, parent_of


@dataclass(frozen=True)
class Token:
    """`04:199` -- *"`Token := (write_class, tick)` -- constructed by loop/driver and NOWHERE
    ELSE"*. What `World.write` takes where it used to take a bare `WriteClass`.

    WHY A TYPE AND NOT THE ENUM. `04 §A.3` row 3: *"A parameter can be passed by anyone; a token
    only by whoever was handed it."* `WriteClass.ACTS` is a module constant, so any function that
    can import `data.matrix` could write in any class. A `Token` has one constructor call site,
    `loop/driver.py::mint_token`, and every step receives its token as a PARAMETER from
    `SeasonDriver.season` -- so a step writes in the class the driver handed it, and DELIBERATE,
    which is handed none, has nothing to present at the gate.

    ⚠ WHAT HOLDS THAT, AND IT IS A SCAN, NOT THE LANGUAGE. Python has no private constructor, so
    `04:206` grades this MECHANICAL: `tests/test_g2_token.py` walks the AST of every module under
    `engine/season/` and fails on a `Token(` call anywhere but `loop/driver.py`, and on a
    `mint_token(` call from any game module other than the driver. What the scan CANNOT see is
    named rather than implied away: `type(t)(...)`, `dataclasses.replace(t, ...)` and
    `copy.copy(t)` all produce a token without spelling `Token(`. ⚠ `frozen=True` IS THE ONE
    STRUCTURAL PART: a MATTER token cannot be rewritten into an ACTS token in place.

    ⚠ THE TICK IS READ, NOT CARRIED. `World.write` refuses a token whose `tick` is not the world's
    current tick, so a token kept past its season -- the §C.1 pseudocode's `drop` not happening --
    is refused at the gate rather than silently authorizing a write a season late. Without that
    check the second field would be a carrier nothing reads."""

    write_class: WriteClass
    tick: int


class NoToken(InstrumentDefect):
    """`World.write` was called without a token for the world's current tick.

    ⚠ AN `InstrumentDefect`, NOT A `Forbidden`, and the distinction is the one `gaps.py` states at
    length: a missing token is a CALL-SITE BUG -- whoever wrote was never handed authority -- and
    not the design refusing a case. Filing it as a `ShapeGap` would let `run_cases` count a probe
    that forgot its token as a hole in the design.

    ⚠ ITS OWN CLASS, SO A TEST CAN ASSERT *WHICH* REFUSAL FIRED. The gate's other refusals are
    `Unspecified` (no matrix row) and `Forbidden` (wrong step, wrong class, L4, S15.3, D22); this
    check runs BEFORE all of them, so a write with no token fails for want of a token even when
    its row, step and class would all have been admitted. `test_g2_token.py` asserts exactly that."""


# =================================================================================================
# G3 -- F3 AT THE GATE. `04 §C.2`, verbatim:
#
#     -- ⚠ F3 · AX-4 CLAUSE 2, ENFORCED HERE FOR THE FIRST TIME
#     kind is Tenure => one of:
#         actor == subject(id)                                   -- T-m, the owner's discretion
#         cause is this Tenure's declared `term` maturation       -- T-n
#         via is a Seat whose `revocation` basis reaches it       -- T-o, and `via` MUST be present
#         cause is an existence change this same act caused       -- destroy's cascade
#       otherwise                                                 raise NotYours
#
# plus the clause `04 §C.2` does not carry and `proposals/2026-09-05-proceedings-subsystem/
# 04_VERBS.md` (the `determine` row's correction ⑴) found missing: *"a conferral-basis opener
# matches none of the four. So does `confer`, today"*. The plan (position 6) makes this the ONLY
# place the F3 branch is authored, so it is authored here, once, as the fifth basis. The SIXTH,
# `handover`, was settled by G3's pre-flight and built at plan position 16 with `give` -- see
# `tenure_write_basis` and `refuse_unauthored`, which is where the one judgment that spans two
# Tenures of the same write is made.
#
# ⚠ PLAN POSITION `17b` (TERM · UPKEEP) BUILT `T-n`, THE ONE CLAUSE ABOVE THAT ADMITTED NOTHING,
# AND ADDED A SEVENTH, `renewal`. `T-n` needed `Tenure.term`, which did not exist until `17b` added
# it (`state/carriers.py::Term`). `renewal` is the write `T-n`'s own rule cannot cover: a seat's
# holder PAYING an obligee's `upkeep` (`_eff_transfer`) winds the clock on an `oblige` edge the
# OBLIGEE owns, which is no maturation, no revocation, no conferral and not the owner's act. Both
# are in `04 §C.2`'s enumeration now, amended inline the same day with the plan position cited.
#
# ⚠ PLAN POSITION `19` (U7-remit) ADDED AN EIGHTH, `determination`, AND THE QUESTION IT ANSWERS IS
# THE ONE THE PLAN'S OWN `19` ENTRY SAID IT COULD NOT ADD ITSELF -- *"a determination that opens a
# Tenure on another's subject needs that fourth case, and position 6 is the only place the gate's F3
# branch is written"*. Position 6 wrote it for `confer` (`conferral`), and `19` re-derived whether
# `determine`'s write is that shape: it is NOT, on all three of `conferral`'s terms at once -- the
# edge is an `oblige`, not a `hold`; its object is the seat EXERCISED (`via`), which `may_fill`
# refuses by name (*"exclusive on the SEAT"*); and what licenses it is a BENCH's jurisdiction over
# the person bound, not a seat's purview over another seat. A reading of `conferral` wide enough to
# admit it would have to flip its reflexivity, which is a different rule wearing the old name. So it
# is written here, once, as `may_determine`, and `04 §C.2`'s enumeration is amended inline the same
# day, with the plan position cited (`conferral`/`handover`/`renewal`'s route).
#
# WHAT IS HERE AND WHAT IS NOT. This module owns the JUDGMENT -- which basis, if any, admits one
# Tenure change -- and the seat-authority rules the judgment composes on (ruling (3)'s revocation
# rule, ruling (4)'s purview, the conferral-basis test). `World.write` owns the OBSERVATION: it
# snapshots the tenure store around `apply()`, hands every changed Tenure here, and rolls the store
# back before raising. The split is the one `Gate`/`World.write` already had -- the gate says what
# is lawful, the store says what happened.
#
# ⚠ `loop/predicates.py` ASKS THESE SAME FUNCTIONS, AND THAT IS §8 RATHER THAN CONVENIENCE.
# `_req_revoke` asks `may_revoke` and `_req_confer` asks `may_fill` -- the precondition refuses
# (and EMITS, `§E2`) exactly what the gate would refuse (and RAISE), because both read one owner.
# A precondition with its own copy of the rule is how the two would come to disagree, and the
# disagreement would surface as a season killed by `NotYours` on an act the fold admitted.
# =================================================================================================


class NotYours(Forbidden):
    """`04 §C.2` F3 / AX-4 clause 2: a `Tenure` was written by someone no admitted basis licenses.

    ⚠ A `Forbidden`, NOT AN `InstrumentDefect` -- AND THE OPPOSITE CHOICE FROM `NoToken`, FOR THE
    REASON `gaps.py` GIVES. `NoToken` says *you called me wrong*: a write with no token was never
    handed authority, which is a call-site bug. This says *the design forbids it*: the call was
    well-formed, the row, step and class all admitted it, and AX-4 -- *the owner is the value's ONLY
    writer* -- refuses it anyway. That is a law refusing, which is what `Forbidden` means, and a
    probe that meets it (`F2`) is reporting a finding about the design, not a bug in the probe.

    ⚠ ITS OWN CLASS, SO A TEST CAN ASSERT *WHICH* REFUSAL FIRED, on `NoToken`'s precedent: the
    falsifiers here must distinguish *the gate asked who* from every other `Forbidden` the same
    write could raise (S30, S30.2, L4, S15.3, D22)."""


# THE BASES' NAMES -- what `tenure_write_basis` returns, and what a refusal message lists. `T-m`,
# `T-o` and `T-n` are `04 §B.8`'s own names (Stage 1 `§E.1.2`); `cascade` is `04 §C.2`'s *destroy's
# cascade*; `conferral` is the fifth basis, named for the thing that licenses it -- the seat's
# declared conferral basis -- rather than coined.
T_M = "T-m"
T_O = "T-o"
# `04 §B.8`'s own name, BUILT at plan position `17b`: the actorless closure of an edge whose declared
# `term` has matured -- MATTER's write, the second cause `04 §B.8`'s synthesis call licenses.
T_N = "T-n"
CASCADE = "cascade"
CONFERRAL = "conferral"
# THE SEVENTH BASIS (plan position `17b`): a seat's seated holder, exercising that very seat,
# extending the `term` of an `oblige` edge on it -- the post paying its establishment (`04 §B.7`'s
# `upkeep`; `F.18`: *"the repair is a verb"*). Named, like `conferral`, in the ordinary word for
# the change it admits. See `may_renew` and the block in `tenure_write_basis`.
RENEWAL = "renewal"
# THE SIXTH BASIS (plan position 16, `give`): a `hold` on something that is not a seat, opened in
# the same write that ended the actor's own live `hold` on it under `T-m`. Named, like `cascade`
# and `conferral`, for the thing that licenses it -- the giver's own edge, handed over -- and in
# the ordinary word for passing a thing into another's keeping. ⚠ NOT A `T-` LETTER: `T-a`..`T-o`
# are `architecture/meta/01_AXIOMS.md`'s theorem labels, of which only `T-m`/`T-n`/`T-o` are
# tenure bases, and the obvious next letter for a GIVE, `T-g`, is already that file's OBSTRUCTION.
HANDOVER = "handover"
# THE EIGHTH BASIS (plan position `19`, U7-remit): a judging seat's seated holder, exercising that
# very seat, OPENING an `oblige` on it for the person a determination binds. Named, like `conferral`,
# for the thing that licenses it -- confer is to `conferral` as determine is to `determination` --
# and NOT `disposal`, the unratified proceedings design's word for the edge (`21_RECONCILIATION.md`
# C-1): read cold, *"the disposal basis"* is a licence to throw an edge away, which is the opposite of
# what it admits (`CLAUDE.md` §4's idempotence test). See `may_determine`.
DETERMINATION = "determination"

# THE REMIT ACT THAT MAKES A SEAT A JUDGING SEAT -- `H-32`'s swept default, and the `bench_basis` of
# every seeded `arrangements.yaml` row. ONE OWNER, read by `queries/world_q.py::judging_set` (which
# carried it as a local literal until `19`) and by `may_determine` below, so *who sits in judgment*
# cannot mean one thing to the bench and another to the gate. A per-arrangement basis
# (`judging_set`'s `bench_basis_of(w, matter)`, not built) would narrow it HERE.
BENCH_BASIS = "determine"


def seat_hold(w: "World", actor: Optional[str], via: Optional[str]) -> Optional[Tenure]:
    """THE SEAT EXERCISED, OR NOTHING: the live `hold` by which `actor` occupies the seat `via`.

    `04 §B.8`'s T-o row: the seat's basis is *"exercised through `Act.via`, refused the instant the
    occupant is not seated"*. So `via` names a seat and this asks whether the actor SITS in it --
    a `via` naming a seat the actor does not hold exercises nothing, which is what stops `Act.via`
    being a string anyone may write. `None` for a missing actor, a missing `via`, a `via` that is
    not an office, and an actor with no live `hold` on it.

    ⚠ A `hold` AND NOTHING ELSE SEATS A PERSON TODAY. `04:332` says *"a regent has the seat's
    purview"*, and no relation in the tree makes a person a seat's regent (`oblige`, `04 §B.7`
    call 2's council membership, has no effect and no reader here). So a regent is expressible only
    as a holder; delegation without a `hold` is `H-108`'s, still open, and this does not close it.
    Returned as the Tenure, not the Office, because `_eligible`'s remit branch reads the GRANT the
    holder has (`Tenure.granted_acts`, the `13e` snapshot), not the office's live remit."""
    if not actor or not via or via not in w.offices:
        return None
    for t in w.tenures:
        if t.kind == "hold" and t.subject == actor and t.object == via and t.live:
            return t
    return None


def purview_reaches(w: "World", seat: Office, rung: Optional[str]) -> bool:
    """`ED-IN-0256` RULING (4), PURVIEW -- *"owner of highest rung in chain of ownership, eg
    territory is owned by Duke if it's within boundaries of duchy"* -- ASKED OF THE SEAT, per
    `04:332`: *"purview is asked of the seat exercised, not the actor ... every purview walk uses
    `via.scope`"*.

    True iff `rung` is the seat's own rung or lies inside it -- `descendants(w, seat.rung)`, the
    walk the plan names for this ruling (part 2 `18a`, r2 `05:450-451`). `Office.rung` IS `via.scope`:
    `04 §B.7`'s `scope? (null = a cluster)` is the field this tree spells `rung: Optional[str]`, with
    the same null. `Office.scope_rung` is a DIFFERENT field, this one, from a DIFFERENT purview
    question (a bench's, `judging_set`'s `H-32` containment test) -- CORRECTED (methodology close,
    antagonist pass, 2026-09-29): this docstring said `scope_rung` "has no reader in the game and
    `18a` deletes it", true when written (`13d-i`, 2026-09-26) and false since `queries/world_q.py
    ::judging_set` (position `18`/PROC-A, 2026-09-29) made it that mechanism's only containment
    check. `18a` MAY NOT delete it as things stand; see `carriers.py`'s matching correction.

    ⚠ THE READING OF "HIGHEST", STATED BECAUSE THE RULING ADMITS TWO. (a) ADOPTED: every seat on
    the chain above a rung has purview over it -- the Duke over a territory in his duchy, and the
    King over it too, the King being the owner of the HIGHEST rung in that chain. (b) REJECTED:
    ONLY the single highest owner has purview. The ruling's own example refutes (b): it names the
    DUKE as owning a territory inside his duchy, and in any realm a duchy is not the highest rung.
    A walk that returned only the top would make the example false.

    ⚠ REFLEXIVE ON THE RUNG. A seat reaches its own rung -- `descendants` is PROPER, so without the
    first disjunct a Duke would not reach the chancellor seated beside him at the duchy (r2 `03`
    §A.6 measured the one-rung difference). EXCLUSIVE ON THE SEAT is not decided here: that is a
    property of what is being done (`may_fill` refuses `via == the seat filled`), not of purview.

    ⚠ A SEAT WITH NO RUNG REACHES NOTHING, and a rung of `None` is reached by nothing. The cluster
    seat (`Office.rung is None`, S6.2) has no ground, so it has purview nowhere -- a CONTENT fact
    about such a seat, not a permission failure. ⚠ AND IT DOES NOT ASK DIRECTION UPWARD: a Duke has
    no purview over the realm above him. Upward reach is petition, never purview."""
    if seat.rung is None or rung is None:
        return False
    return rung == seat.rung or rung in descendants(w, seat.rung)


def seated_on_the_rung_above(w: "World", seat: Office, off: Office) -> bool:
    """`ED-IN-0256` ruling (3), verbatim: *"rung above of same faction"* -- WHO MAY STRIP A SEAT.

    ⚠ RE-POINTED BY G3 FROM THE ACTOR TO THE SEAT EXERCISED, AND THAT IS THE WHOLE CHANGE. Built at
    `13d-i` (in `loop/predicates.py`) as `(w, actor, off)`: *does the actor hold ANY live `hold` on a
    seat on the rung directly above, of the same faction*. `04:332` says purview is asked of the
    seat exercised, not the actor, and `04 §B.8` says T-o is *"the Seat's `revocation` basis,
    exercised through `Act.via`"* -- so it now asks of ONE seat, the one the act names: is `seat` on
    the rung directly above `off`'s rung (`parent_of`, the one owner of the containment edge), in
    `off`'s faction. Whether the actor SITS in that seat is `seat_hold`'s question, asked by
    `may_revoke` before this is. Moved here from `loop/predicates.py` because the gate's T-o clause
    evaluates it and the gate may not import the loop.

    ⚠ THE RULE ITSELF IS UNCHANGED, and the `13d-i` reading stands (its docstring, kept verbatim in
    substance): GENERAL over every seat and every depth -- no post is read and no rung kind named;
    the rung above means the PARENT, not any ancestor, so a King does not reach past an empty duchy
    to a Lord (`test_13d_i_an_empty_parent_refuses_even_a_same_faction_grandparent` pins it); a
    rungless seat has no rung above it, so NOBODY may strip it, nor may a rungless seat strip
    anyone; a seat on a TOP rung is strippable by nobody. Two readings REJECTED at `13d-i` stay
    rejected: LAND (`in_holdings` -- who owns the parent rung) and THE NEAREST SAME-FACTION SEAT
    ABOVE (a walk, which is ruling (4)'s verb, `purview_reaches`, not ruling (3)'s)."""
    if off.rung is None or off.rung not in w.rungs or seat.rung is None:
        return False
    above = parent_of(w, off.rung)
    if above is None:
        return False
    # `Office.faction` is the RESOLVED faction -- `__post_init__` writes `office_faction`'s answer
    # back, deriving it from `body` where there is one -- so it is compared as held.
    return seat.rung == above and seat.faction == off.faction


# THE REVOCATION BASES, DISPATCHED BY VALUE -- `H-109`'s shape: *"two VALUES of a seat's declared
# `revocation` basis instead of two code paths"*. The members are DATA (`rosters.yaml:
# revocation_bases`); the rule each names is BEHAVIOUR and lives here, the `fan_out_modes` split.
# Moved from `loop/predicates.py` with `seated_on_the_rung_above` (G3); `predicates` imports it.
REVOCATION_RULES = {"rung_above_same_faction": seated_on_the_rung_above}
# ⚠ REFUSED AT IMPORT, NOT IN THE FOLD. A member with no rule, or a rule for no member, is drift
# between data and code; raised from inside `_req_revoke` it would escape the fold (the `13f`
# lesson), and dispatched by fall-through it would run a new basis as some other one.
if set(REVOCATION_RULES) != set(REVOCATION_BASES):
    raise Unspecified(
        f"revocation bases {sorted(REVOCATION_BASES)} and revocation rules "
        f"{sorted(REVOCATION_RULES)} disagree", "rosters.yaml -- revocation_bases",
        needs="give every rostered basis its rule in `state/gate.py::REVOCATION_RULES`, "
              "and every rule a rostered basis",
        law="`04 §B.13` ID-12 -- a declared row that reaches no code is the defect the loader's "
            "cross-validation exists to catch; ED-IN-0256 (3) is the one rule ruled")


def has_conferral_basis(off: Office) -> bool:
    """THE BASIS TEST, ONCE: does this office declare HOW IT IS FILLED, from the ruled set?

    `_req_confer` asks it of the office being conferred, `_req_establish` of the office being
    founded, and the gate's `conferral` basis of the seat an opened `hold` is on -- three readers,
    one test. It is ROSTER MEMBERSHIP (`13d-i`): `conferral` must be one of `rosters.yaml:
    conferral_bases`, `ED-IN-0256` ruling (2) -- *appointed · elected · annex*. `None` refuses; so
    does a string off the roster, which `Office.__post_init__` refuses to construct, so that arm is
    reached only by a hand-mutated office. Moved here from `loop/predicates.py` (G3), because the
    gate asks it and the gate may not import the loop; `predicates` imports the name, so a
    `monkeypatch` of `predicates.has_conferral_basis` still reaches both preconditions.

    ⚠ MEMBERSHIP ONLY: every rostered basis passes. Which act fills an `elected` or an `annex` seat
    is not ruled, and `confer` is the only act that fills any seat (`rosters.yaml`'s note)."""
    return off.conferral in CONFERRAL_BASES


def may_revoke(w: "World", actor: Optional[str], via: Optional[str], off: Office) -> bool:
    """T-o, AS ONE PREDICATE: may `actor`, exercising `via`, close a `hold` on the seat `off`?

    Three conjuncts, in `04 §B.8`'s own order: `via` is PRESENT and the actor SITS in it
    (`seat_hold` -- *"`via` MUST be present"*, *"refused the instant the occupant is not seated"*);
    `off` declares a basis on `rosters.yaml: revocation_bases` (`None` -- a seat declaring none --
    is strippable by nobody); and the rule that basis names admits `via`. Asked by the gate for
    every closed `hold` on a seat, and by `_req_revoke` / `_req_confer` before their effects run."""
    if seat_hold(w, actor, via) is None:
        return False
    if off.revocation not in REVOCATION_BASES:
        return False
    return REVOCATION_RULES[off.revocation](w, w.offices[via], off)


def may_fill(w: "World", actor: Optional[str], via: Optional[str], off: Office) -> bool:
    """THE CONFERRAL BASIS, AS ONE PREDICATE: may `actor`, exercising `via`, open (or re-grant) a
    `hold` on the seat `off` FOR SOMEBODY ELSE?

    The fifth F3 clause (`04_VERBS.md`'s *"conferral-basis opener"*). What licenses writing an edge
    another person will own is not the actor's ownership but THE SEAT'S BASIS: `off` declares how
    it is filled (`has_conferral_basis`), and the seat exercised has PURVIEW over it
    (`purview_reaches`, ruling (4) on `via.scope`) -- r2 `03` §A.4's *"a superior names the holder.
    A seat whose ground lies inside another seat's ground, filled by that seat's exercise"*. And
    `via` is not `off` itself: reflexive on the RUNG, exclusive on the SEAT, so a holder does not
    fill the seat he is exercising (r2 `03` §A.6).

    ⚠ WHAT IT DOES NOT DECIDE: WHICH conferral basis each act may exercise. `appointed`, `elected`
    and `annex` all pass today, because the mapping from basis to act is unruled (`13d-i`'s open
    question: should `confer` narrow to `appointed`?). If that is ruled, it narrows HERE, and the
    precondition inherits it by asking this."""
    if seat_hold(w, actor, via) is None or via == off.id:
        return False
    if not has_conferral_basis(off):
        return False
    return purview_reaches(w, w.offices[via], off.rung)


def may_renew(w: "World", actor: Optional[str], via: Optional[str], off: Office) -> bool:
    """THE RENEWAL BASIS, AS ONE PREDICATE (plan position `17b`): may `actor`, exercising `via`,
    wind the `term` of somebody's `oblige` edge on the seat `off`?

    Two conjuncts: `via` IS `off` -- the seat pays its OWN establishment, *"what the post pays its
    establishment out of the office's stake"* (`holonic_ARCHITECTURE.md:428`), so a renewal is the
    seat's act and is asked of the seat exercised (`04 §B.7`'s purview invariant) -- and the actor SITS in it
    (`seat_hold`, *"refused the instant the occupant is not seated"*). Asked by the gate for every
    extended `oblige` term, and by `_eff_transfer` before it names one, so the effect never writes a
    renewal the gate would refuse (a `NotYours` out of the fold would end the season, not refuse the
    act): one owner, two readers, `may_fill`'s shape.

    ⚠ REFLEXIVE ON THE SEAT, THE OPPOSITE OF `may_fill`, AND FOR THE REASON THAT FUNCTION GIVES.
    `may_fill` refuses `via == off` because a holder filling the seat he exercises is authority over
    himself. Paying the seat's own obligees is authority over nothing but the seat's own treasury;
    it is the only seat that may. ⚠ THREE READINGS REJECTED, each with the reason:
      * PURVIEW (`purview_reaches`, a superior seat paying a subordinate's establishment). `04
        §B.7`'s upkeep is what the seat pays ITS establishment; a Duke paying his reeve's men is a
        gift to them, and gifts renew no one's service.
      * NO SEAT AT ALL -- whoever moves matter from the treasury to an obligee's home renews. That
        is causation-bound, `handover`'s shape, and it would need the gate to observe STORES, which
        it does not (it observes Tenures; `World.write` owns the only before/after read of a rung).
        And it would make paying a man's wages something a thief can do for you.
      * THE OBLIGEE'S OWN ACT (`T-m`). A term the servant can extend for himself is not a term.

    ⚠ WHAT IT DOES NOT DECIDE: whether the payment was ENOUGH, or from the right store. Those are
    `_eff_transfer`'s (with `queries/world_q.py::upkeep_of`), because the gate observes Tenures and
    never a rung's stores -- the split `may_fill` already has with `_req_confer`."""
    return via == off.id and seat_hold(w, actor, via) is not None


def sits_over(w: "World", seat: Office, rung: Optional[str]) -> bool:
    """THE BENCH'S CONTAINMENT TEST, ONCE: does `seat` sit in judgment over `rung`?

    `H-32`'s ruled default, verbatim in substance: *"an Office ... whose `scope_rung` contains the
    sitting's rung"* -- `seat.scope_rung` is `rung` itself or one of its ancestors (`ancestry`, the
    one owner of the walk up), so a seat scoped one rung above still finds it (`21_RECONCILIATION.md`
    PHASE 2 step 7's own falsifier). Extracted at plan position `19` from `queries/world_q.py::
    judging_set`'s loop, which now asks it, so the bench `judging_set` lists and the bench the write
    gate's `determination` basis admits are ONE test (`CLAUDE.md` §8).

    ⚠ `scope_rung`, NOT `rung` -- AND SO NOT `purview_reaches`, AND THE DIFFERENCE IS KEPT, NOT
    PAPERED OVER. `purview_reaches` asks ruling (4)'s purview of `Office.rung` (`04:330`'s `via.scope`);
    `judging_set` reads `scope_rung` by `H-32`'s own default, which its methodology-close correction
    (`judging_set`'s docstring, 2026-09-29) declined to reopen. The two agree on every TITLED seat
    (`Office.__post_init__` sets `scope_rung = rung` for a titled post) and differ on a ranked,
    untitled seat with no authored `scope_rung`, which purview reaches and no bench seats. Whether a
    bench's ground IS its purview is `H-32`'s sweep (*"remit+scope · remit only · scope only"*), not
    this function's to decide. A rung of `None` is judged by nobody."""
    if seat.scope_rung is None or rung is None:
        return False
    return seat.scope_rung in ancestry(w, rung)


def may_determine(w: "World", actor: Optional[str], via: Optional[str], party: Optional[str]) -> bool:
    """THE DETERMINATION BASIS, AS ONE PREDICATE (plan position `19`): may `actor`, exercising
    `via`, open an `oblige` on that seat that `party` will own -- bind `party` to the bench?

    Three conjuncts, each the ONE owner of its rule:
      1. `via` is a JUDGING seat the actor SITS in: `seat_hold` (*"refused the instant the occupant
         is not seated"*, `04 §B.8`) and its GRANT carries `BENCH_BASIS` -- the snapshot on the
         hold (`Tenure.granted_acts`, `13e`), exactly what `judging_set` and the fold's `remit:`
         eligibility read, never the office's live field.
      2. `party` is a PERSON other than the actor. Only a person owns an `oblige` (`holonic §15`;
         `_req_oblige` clause 1's lesson from `ED-IN-0211`), and a judge does not bind himself --
         the occupant is not his own seat's obligee (`_req_oblige` clause 3's rule, one step over).
      3. the bench's ground holds the party: `sits_over(w, via, <party's home>)`, the SAME test
         `judging_set` lists a bench by, asked of where the person bound actually lives (`home_of`,
         the one owner of *where a person is*, moved to `state/` for this) -- `04:330`'s *"purview is
         asked of the seat, never the actor"*, with the bench's ground as the seat's reach.

    ⚠ WHY A NEW BASIS AND NOT A WIDER READING OF `conferral` -- the question plan position `19`
    carried in from its own entry (*"a conferral-basis opener"*), re-derived rather than taken on
    trust. `conferral` admits an opening of a `hold` ON A SEAT OTHER THAN `via`, by `via`'s
    purview over that seat. This admits an opening of an `oblige` ON `via` ITSELF, by the bench's
    ground over a PERSON. Kind, object and authority all differ, and `may_fill` refuses the object
    case by name (*"exclusive on the SEAT"*). Its nearest sibling is `renewal` -- an `oblige` on the
    seat exercised, by its seated holder -- which may only push an existing term later and never
    open; this is the opening `renewal` refuses, licensed by judgment rather than by payment.

    ⚠ WHAT IT DOES NOT DECIDE, AND WHERE THAT LIVES -- `may_fill`/`_req_confer`'s split. The DOCKET
    (was the matter put before the room?) and the QUORUM (is the bench large enough to sit?) are
    the precondition's (`verb_table.yaml`'s `determine` cell), because the gate observes Tenures and
    the determination takes the matter off the docket IN THE SAME WRITE -- a licence the write
    consumes cannot be read after it (`handover`'s problem, which that basis solves only because
    its licence IS a Tenure). The bench conjunct of the precondition is this function, asked early
    through `WorldReader`'s `bench` stem, so the fold refuses (and emits) exactly what this refuses
    (and raises): a precondition with its own copy would surface as `NotYours` killing a season.

    ⚠ `oblige` ONLY, AND NOT `hold`, `commit` OR A `Record`. `arrangements.yaml`'s one seeded
    `disposes:` that is a Tenure kind is `arbitration`'s `oblige`; the two others dispose a `Record`,
    which is minted under `T-m` and needs no basis. A disposal of another kind arrives with its row
    and widens THIS predicate, not the gate's chain."""
    t = seat_hold(w, actor, via)
    if t is None or BENCH_BASIS not in t.granted_acts:
        return False
    if party is None or party == actor or party not in w.persons:
        return False
    return sits_over(w, w.offices[via], home_of(w).get(party))


def _moved(t: Tenure, was: Optional[Tenure]) -> Optional[set]:
    """Which of an existing edge's five non-end fields the write changed; `None` for an edge the
    write OPENED. The ends (`subject`, `object`, `kind`) are not listed: rewriting them is refused
    before this is read (`tenure_write_basis`'s *nothing admits rewriting an edge's ends*).

    ⚠ `term` IS THE FIFTH (plan position `17b`), AND LEAVING IT OUT WOULD HAVE ADMITTED A TERM
    REWRITE UNDER EVERY BASIS THAT TESTS `moved`: a `T-o` closure that also shortened the edge's
    term would read as `{"until"}`, a pure closure, and a `conferral` re-grant that also wound a
    term would read as `{"payload"}`. Each basis now sees the term as the change it is."""
    if was is None:
        return None
    return {name for name, now, then in (
        ("since", t.since, was.since), ("until", t.until, was.until),
        ("degree", t.degree, was.degree), ("payload", t.payload, was.payload),
        ("term", t.term, was.term)) if now != then}


def _closes(t: Tenure, was: Optional[Tenure], moved: Optional[set] = None) -> bool:
    """A PURE CLOSURE: an edge that was live before the write, has `until` set after it, and had
    nothing else moved. The one change `cascade` and `T-o` may make -- and, since position 16, the
    change on the giver's side that licenses a `handover` on the receiver's. One test for all
    three, so what counts as *ended in this write* cannot differ between them.

    `moved` is the caller's own `_moved(t, was)`, when it already has one -- `tenure_write_basis`
    computes it the line above its own `_closes` call (BATCH-CLOSE, methodology-close Phase 2,
    SIMPLIFICATION/EFFICIENCY findings: this recomputed it internally on every call). `None`
    derives it here exactly as before, so every other caller is unaffected."""
    if moved is None:
        moved = _moved(t, was)
    return (was is not None and was.until is None and t.until is not None and moved == {"until"})


def tenure_write_basis(w: "World", t: Tenure, was: Optional[Tenure], actor: Optional[str],
                       via: Optional[str], gone: frozenset,
                       released: frozenset = frozenset()) -> Optional[str]:
    """F3's JUDGMENT FOR ONE CHANGED TENURE: the name of the basis that admits it, or `None`.

    `t` is the Tenure as it stands after the write; `was` is a detached copy of it from before, or
    `None` if the write OPENED it. `gone` is every id the same write removed from the world -- the
    existence changes THIS act caused, observed by the store rather than claimed by the caller.
    `released` is every OBJECT on which the same write ended the actor's own live `hold` under
    `T-m` and has not yet handed it on -- computed by `refuse_unauthored` from the batch it holds,
    because this function sees one Tenure and cannot (see `handover` below). Empty by default, so a
    caller judging a Tenure alone gets the answer of every basis but `handover` (seven, since `19`
    added `determination`; six since `17b` built `T-n` and added `renewal`; five before).

    THE EIGHT BASES, AND WHAT EACH MAY WRITE -- a basis admits a KIND of change, not any change:

      `T-m`       the actor IS the owner -- `was.subject` for an existing edge, `t.subject` for a
                  new one. Anything the owner does to their own edge (`release`, `move`'s legs,
                  `create_record`'s `hold`, a self-conferral's opening). ⚠ The owner is read from
                  BEFORE the write, so an effect cannot make itself the owner by rewriting
                  `subject` and then be admitted as it.
      `T-n`       an ACTORLESS CLOSURE (`until` set, nothing else, no actor) of an edge whose OWN
                  declared `term` -- read from BEFORE the write -- has `matures_at <= w.tick`.
                  BUILT AT PLAN POSITION `17b`, which added `Tenure.term`; until then this entry
                  read *"NOT BUILT, AND NOT BUILDABLE HERE: `Tenure` carries no `term`"*, and it
                  was right to admit nothing rather than test a field that did not exist. The
                  cause is the term itself, so it is CAUSATION-BOUND like `cascade` and reads no
                  seat: `04 §B.8`, *"an actorless row may write `until` only where its cause is
                  the existence change it also caused, OR the maturation of a term declared by
                  the act that opened this Tenure"*. MATTER is its one writer
                  (`loop/matter.py`'s tenure-term branch). ⚠ ACTORLESS ONLY: an ACT closing an
                  edge whose term has come is that actor's act and needs that actor's basis
                  (`T-m`, `T-o`); a term that matured licenses its own lapse, never a stranger's
                  hand. ⚠ The term is read from `was`, so a write cannot shorten a term and then
                  be admitted as its maturation -- and `_moved` lists `term`, so such a write is
                  not a pure closure anyway.
      `cascade`   a CLOSURE (`until` set, nothing else) of an edge whose subject or object is in
                  `gone`. `04 §B.8`: *"`destroy` sets `until` on every Tenure naming the id AND
                  NOTHING ELSE"* -- so the cascade may close and may not open, grade or re-grant.
                  The one basis an ACTORLESS write can meet (S15.3's causation rule), which is how
                  MATTER's death reaches it.
      `T-o`       a CLOSURE of a `hold` on a SEAT, by `may_revoke` -- `via` present, the actor
                  seated in it, and the seat's revocation basis admitting it.
      `conferral` an OPENING of a `hold` on a SEAT, or a change to that `hold`'s grant (`payload`)
                  alone, by `may_fill`. The re-grant is `establish`'s re-stamp (`13f`): the grant a
                  seat confers on its holder, written by the authority that may fill the seat.
      `handover`  an OPENING of a `hold` on something that is NOT a seat, whose object is in
                  `released` -- the actor ended their own live `hold` on that object under `T-m`
                  in this same write. `give` (plan position 16) is the verb; the basis is general
                  over every non-seat `hold` object. See the block below.
      `renewal`   a change to `term` ALONE on a LIVE `oblige` edge, that pushes a term the edge
                  already carried LATER, by `may_renew` -- `via` IS the seat the edge is on and the
                  actor sits in it. Plan position `17b`: the post paying its establishment's
                  `upkeep` (`_eff_transfer`) winds each paid obligee's clock. AUTHORITY-BOUND like
                  `T-o` (a seat's act through `Act.via`), and NARROWER than every other basis in
                  what it may write: it cannot open, close, grade or re-grant, cannot ADD a term
                  to an edge that had none (payment renews a term; it does not impose one), and
                  cannot SHORTEN one (an earlier `matures_at` is a revocation wearing a receipt,
                  and revocation is `T-o`'s). `oblige` ONLY, because upkeep is what the seat pays
                  those obliged to it (`04 §B.7` call 2: *"the size is whatever the holder admits
                  and the upkeep pays"*); a `hold` on the seat is its holder's own seat and a term
                  on it is not this position's.
      `determination` an OPENING of an `oblige` whose OBJECT is `via` itself and whose owner is
                  someone other than the actor, by `may_determine` -- `via` is a judging seat the
                  actor sits in and its bench's ground holds the owner's home. Plan position `19`:
                  `determine`'s disposal, *"a determination opens the disposal Tenure on its
                  subject via the seat"* (`21_RECONCILIATION.md:575`). AUTHORITY-BOUND like `T-o`
                  and `renewal`, and OPENING ONLY: it cannot close, grade, re-grant or touch a term
                  on an edge that exists (a second sentence on a bound man is a new edge, and the
                  effect declines one -- one `oblige` per person and seat, `_req_oblige`'s rule).
                  The term the opening carries is the opening act's declaration (T-n), as
                  `_eff_oblige`'s is, so it is the edge's own and not a write this basis judges.

    ⚠ JUDGED ON THE WORLD THE WRITE LEAVES. `World.write` asks this after `apply()`, so `T-o` and
    `conferral` read `seat_hold` -- is the actor seated in `via`? -- AFTER the effect ran. `04 §B.8`'s
    *"refused the instant the occupant is not seated"*, read literally: an act that vacates the seat
    it exercises (conferring that very seat closes every `hold` on it, his own included) writes
    nothing else through it. No effect today both vacates its `via` and writes another's edge
    through it, so the reading moves no run; it is stated because the other reading -- occupancy as
    the act FOUND the world -- is defensible and would need `seat_hold` captured before `apply()`.

    ⚠ NOTHING ADMITS REWRITING AN EDGE'S ENDS. A change to `subject`, `object` or `kind` of an
    existing Tenure is a different edge wearing this one's id, and no basis licenses it -- not even
    `T-m`, because the new subject is somebody else's store.

    ⚠ `handover` -- `give` (PLAN POSITION 16 ≡ `15a`) -- SETTLED BY G3's PRE-FLIGHT (`ED-IN-0277`),
    BUILT AT POSITION 16. The giver's close is `T-m`. The RECEIVER'S open matches none of the other
    five (nor `17b`'s `renewal`, which admits no opening): it is not the receiver's act, no seat is exercised (`give` is `own`-eligible, `via` is
    `None`), and nothing ceased to exist. So it has its own basis, CAUSATION-BOUND like the cascade
    rather than authority-bound like T-o: *a `hold` opened on an object that is NOT a seat, of the
    same kind and object as an edge the actor OWNED, was live before, and closed under `T-m` in this
    same write*. The authority to open the receiver's edge is the giver's own edge, ended in the
    same act -- so *release-before-mint* (r2 `05` row 6, ⊕ R14) is the GATE'S condition rather than
    the effect's discipline, and a `give` that forgets the release is refused here (`NotYours`,
    store put back) before `hold_force` ever sees two holders. SEATS ARE EXCLUDED: a seat passes by
    its conferral basis, never by its holder handing it on. It does NOT read `via` (no seat is
    exercised), and it is NOT the receiver's own act (position 16 specifies one two-party verb, by
    the giver). ⚠ `hold` ONLY, as the settled rule says: `hold` is the custody edge, one per object
    (`holonic §15`), and so the one edge there is something to hand on; a `commit` or a `tie` is the
    holder's own relation and an ending of one licenses nobody else's opening.
    ⚠ THE CLAUSE IS JUDGED HERE, THE LICENCE IS COMPUTED IN `refuse_unauthored` -- CORRECTED
    2026-09-26 (antagonist pass on G3) and built that way at position 16. This function judges ONE
    changed Tenure and cannot see what the same write did to any OTHER; `gone` carries existence
    removals only, and `until == w.tick` cannot tell this write's closure from an earlier write's in
    the same tick. So `refuse_unauthored`, which holds the whole batch, judges every change first,
    collects the objects of the `hold`s this actor ended under `T-m` (`_closes` -- the same closure
    test `cascade` and `T-o` use), and passes the ones not yet handed on in as `released`. ⚠ ONE
    ENDING HANDS ON ONE EDGE: a write that ends one `hold` and opens two on the same object gets one
    `handover`, and the second opening is refused -- otherwise the gate would admit the two holders
    the basis exists to prevent."""
    opened = was is None
    owner = t.subject if opened else was.subject
    if not opened and (t.subject, t.object, t.kind) != (was.subject, was.object, was.kind):
        return None
    moved = _moved(t, was)
    closed = _closes(t, was, moved)
    seat = w.offices.get(t.object) if t.kind == "hold" else None
    # ⚠ T-M NEVER ADMITS OPENING OR RE-GRANTING A SEAT-HOLD, EVEN THE ACTOR'S OWN (found by the
    # antagonist pass, 2026-09-26: "the wrong answer is a quietly permissive gate" was exactly
    # this). `owner` on an OPENED edge is read from the write itself (`t.subject`), so "the actor
    # IS the owner" is self-fulfilling for any actor who names themselves the new holder --
    # measured: a bare gate write let an UNRELATED actor with no via and no purview open a hold on
    # ANY seat naming themselves subject, and let a sole holder re-stamp their own seat's remit
    # (`establish`'s re-grant) the same way. `04:330` -- purview is asked of the SEAT exercised,
    # never the actor -- and a seat's authority over itself is never personal, not even to its own
    # sitting holder: a duke does not grant himself new powers by re-founding his own duchy. A
    # PURE CLOSURE is unaffected -- voluntary resignation of one's own seat (`release`) is still
    # T-m, because closing what you hold is not an act of authority over the seat, it is giving it
    # up. Only `closed` distinguishes the two; `is_seat_hold` alone would also refuse `release`.
    if actor is not None and actor == owner and not (seat is not None and not closed):
        return T_M
    if closed and (t.subject in gone or t.object in gone):
        return CASCADE
    if (closed and actor is None and was.term is not None
            and was.term.matures_at <= w.tick):
        return T_N
    if opened and t.kind == "hold" and seat is None and t.object in released:
        return HANDOVER
    if (not opened and t.kind == "oblige" and t.live and moved == {"term"}
            and was.term is not None and t.term is not None
            and t.term.matures_at > was.term.matures_at):
        served = w.offices.get(t.object)
        if served is not None and may_renew(w, actor, via, served):
            return RENEWAL
    # `19`: THE BENCH'S DISPOSAL. Asked only of an OPENED `oblige` ON THE SEAT EXERCISED -- the one
    # shape `may_determine` licenses -- so no existing edge, no other kind and no other seat reaches
    # it. `via is not None` is `may_determine`'s own first conjunct too (`seat_hold`); it is written
    # here as well so the object test cannot match a `None` object on a malformed edge.
    if (opened and t.kind == "oblige" and via is not None and t.object == via
            and may_determine(w, actor, via, t.subject)):
        return DETERMINATION
    if seat is None:
        return None
    if closed and may_revoke(w, actor, via, seat):
        return T_O
    if (opened or moved == {"payload"}) and may_fill(w, actor, via, seat):
        return CONFERRAL
    return None


def refuse_unauthored(w: "World", changes: list, actor: Optional[str], via: Optional[str],
                      gone: frozenset) -> list:
    """Every `(t, was)` in `changes` that NO basis admits, as `(t, was)` pairs -- `[]` admits all.

    Asked by `World.write` after `apply()` and before anything is traced as written. It returns
    rather than raises so the store can put the tenures back FIRST: the refusal is only honest if
    the edge it refused is as it was (`NotYours`' own raise is `World.write`'s, via `not_yours`).

    TWO PASSES, BECAUSE ONE BASIS SPANS TWO TENURES (position 16). The first judges every change
    on its own -- the seven bases that need nothing but the change, the actor, `via` and `gone`
    (five until plan position `17b` built `T-n` and added `renewal`, six until `19` added
    `determination`; none of the three reads another Tenure of the batch).
    From those verdicts it takes the `handover` licence: the object of every `hold` this actor
    ENDED under `T-m` in this write, counted. The second re-judges only what the first refused,
    now with the licence, and spends one unit of it per `handover` it admits. The two passes are
    exact rather than approximate: `handover` admits only an OPENED edge, which `T-m` never admits
    for anyone but the actor, and the licence is read off `T-m` closures, which never depend on it.
    ⚠ THE LICENCE IS COMPUTED HERE AND NOT IN `World.write`, which is why `World.write`'s call did
    not change: *which change was a `T-m` closure* is a judgment, and the store observes changes
    and never judges them -- the split this module's G3 header states.

    ⚠ `closes` IS A NAMED LIST, NOT AN EFFICIENCY FIX -- CORRECTED (BATCH-CLOSE, methodology-close
    Phase 3 terminal critique, F5): the Phase 2 EFFICIENCY finding this replaced claimed it removed
    "the second pass through `_moved`/`_closes`," and that claim was false. `_closes(t, was)` is
    still called exactly once per change here (now via this list comprehension, before it was
    inline in the `released` Counter's own generator) -- the SAME count as before, only relocated
    -- and `tenure_write_basis` still computes its own `_moved`/`_closes` internally, one call per
    change, inside the `bases` comprehension two lines up. The two calls per change (one inside
    `tenure_write_basis`, one here) are UNCHANGED by this list; eliminating that pair would need
    `tenure_write_basis` to return `closed` alongside its basis, a signature change to the write
    gate's own judgment function not attempted here. What this list actually buys: `closed` is a
    named, reused value inside the `zip` loop below rather than re-spelled inline -- a readability
    change, not a performance one, and the docstring saying otherwise was the defect."""
    bases = [tenure_write_basis(w, t, was, actor, via, gone) for t, was in changes]
    closes = [_closes(t, was) for t, was in changes]
    released = Counter(was.object for (t, was), basis, closed in zip(changes, bases, closes)
                       if closed and basis == T_M and was.kind == "hold")
    refused = []
    for (t, was), basis in zip(changes, bases):
        # `+released` is the Counter with its spent (zero) entries dropped: what is left to hand on.
        if basis is None and +released:
            basis = tenure_write_basis(w, t, was, actor, via, gone, frozenset(+released))
            if basis == HANDOVER:
                released[t.object] -= 1
        if basis is None:
            refused.append((t, was))
    return refused


# [JUSTIFIED: a MESSAGE LENGTH, not a game value -- how many refused edges a `NotYours` names before it counts the rest; nothing in the model reads it]
_NAMED_IN_MESSAGE = 4


def not_yours(refused: list, actor: Optional[str], via: Optional[str], record_kind: str,
              fieldname: str) -> NotYours:
    """The `NotYours` for a write whose `refused` changes no basis admitted -- built here so the
    message and the law live once."""
    shown = ", ".join(
        f"{t.id} ({t.kind} {('owned by ' + (was.subject if was is not None else t.subject))}"
        f" on {t.object}, {'opened' if was is None else 'changed'})"
        for t, was in refused[:_NAMED_IN_MESSAGE])
    more = (f" and {len(refused) - _NAMED_IN_MESSAGE} more"
            if len(refused) > _NAMED_IN_MESSAGE else "")
    return NotYours(
        f"a ({record_kind}, {fieldname}) write by {actor or 'no actor'} "
        f"{('exercising ' + via) if via else 'exercising no seat'} wrote Tenures it has no basis "
        f"for: {shown}{more}", "F3",
        needs=f"{T_M} (the actor owns the edge), {T_O} (via present, the actor seated in it, the "
              f"seat's revocation basis reaching it), {CONFERRAL} (via's purview over a seat "
              f"that declares a conferral basis), {CASCADE} (the edge names something this "
              f"same write removed), {HANDOVER} (a `hold` on something that is not a seat, "
              f"opened in the same write that ended the actor's own live `hold` on it -- one "
              f"opening per ending), {T_N} (an actorless closure of an edge whose own declared "
              f"term has matured), {RENEWAL} (a live `oblige` edge's term pushed later, by "
              f"its seat's own seated holder exercising it), or {DETERMINATION} (an `oblige` "
              f"opened on the judging seat exercised, for a person its bench's ground holds)",
        law="04 §C.2 F3 / AX-4 clause 2 -- the owner is the value's ONLY writer, and a non-owner "
            "writes only under a declared basis. Per-verb eligibility enforced this by "
            "CONVENTION until G3; a revocation with no seat in Act.via is refused here, so 'a "
            "superior may revoke' cannot degrade into 'anyone with a remit string'")


# The write classes in which ANY `Tenure` row may be written, DERIVED from the matrix rather than
# listed: `World.write` observes the tenure store around `apply()` only for a write in one of these.
# A write in any other class cannot LAWFULLY write a Tenure at all -- that is S30's matrix refusing,
# not F3 -- so F3 is not asked of it. ⚠ THE BOUND, STATED: a Tenure mutated INSIDE a CALENDAR or
# INTERIOR write is outside this observation. It is also outside the matrix's, because the matrix
# checks the pair a write DECLARES, not what its closure touches -- no step does that today (every
# CALENDAR closure fires a Date or forms a docket item, every WITNESS closure appends a claim to a
# ledger; `loop/calendar.py`, `loop/witness.py`), and the day one does, this set is
# where to widen F3's watch. The cost of widening, measured on `build_realm(0)` over one season: 532
# writes observed today (359 MATTER, 173 ACTS) against 2,688 in all -- the 2,156 WITNESS deposits
# are the difference, so watching every class would snapshot the tenure store ~5x as often.
TENURE_WRITE_CLASSES = frozenset(
    row.write_class(step) for (kind, _f), row in MATRIX.items() if kind == "Tenure"
    for step in row.steps)


# =================================================================================================
# G4 -- F9 AT THE GATE. `04 §C.2`, verbatim:
#
#     before = get(); store._set(); after = get()               -- THE GATE APPLIES THE WRITE
#     before == after                     or raise NoOpReceipt  -- ⚠ F9 · see PART D row 5
#
# ⚠ THE SECOND LINE'S `or` READS INVERTED, AND WHAT IS BUILT IS WHAT ITS PROSE SAYS. `04:559-564`
# and PART D row 5 both state it the one way: *"The gate now refuses `before == after` at the
# write, so the receipt is never minted"*. EQUAL raises.
#
# WHAT CHANGED, AND IT IS THE CONTRACT OF EVERY EFFECT IN `loop/effects.py`. Before G4 an effect
# MUTATED inside an opaque `apply()` and RETURNED the ids it touched, and the fold minted a receipt
# for every id it was told -- so an effect that named an id it never changed produced a success
# Event carrying a gate-minted receipt, and `state/log.py`'s provenance check (which asks only
# WHO minted it) admitted it. That is `ID-9`'s own worked example surviving PART D row 5 (F9):
# `work` emitted `site.worked` over a condition nothing wrote. Now an effect returns a `Change`:
# the SUBJECTS it writes, named before it runs, and the write. `World.write` reads every subject,
# applies the write, reads them again, and mints a receipt for each subject that moved and for no
# other. None moved: `NoOpReceipt`, and the fold turns it into the row's refusal.
#
# WHAT `get()` READS -- ONE RULE, THREE SUBJECT SHAPES, OWNED BY `World.state_of`:
#
#   `entity`  an id in one of `World._STATE_COLLECTIONS`: present-or-absent, and the entity's
#             `_entity_digest` -- THE SAME per-entity string `World.content_hash` folds, so a
#             subject has moved exactly when the content hash can see that it moved. `fields=`
#             narrows the read to named attributes; ONE effect uses it (`kill / wound`, whose
#             docstring says why).
#   `edge`    a Tenure, by IDENTITY. Not read here at all: it has moved iff G3's observation of the
#             tenure store (`World._tenure_changes`) lists it -- changed or opened. The snapshot G3
#             already takes is reused rather than a second one taken (the plan's own conflict
#             note: G4 composes with F3's observation, it does not duplicate it).
#   `staged`  a cell of `S27.3`'s sum-then-clamp-once accumulator (`World.stage`): the net
#             delta staged on it so far. An act's `work` moves it iff its delta is non-zero; the
#             accumulator's own write at the end of RESOLVE then moves the SITE, and that is where
#             the clamp can turn a staged delta into no change at all.
# =================================================================================================


class NoOpReceipt(Forbidden):
    """`04 §C.2` F9 / PART D row 5: a write whose every subject reads the same after it as before.

    ⚠ A `Forbidden`, ON `NotYours`' PRECEDENT AND FOR ITS REASON. The call was well-formed and the
    row, step, class and F3 all admitted it; what refuses it is `ID-9` -- *a success Event for a
    write that did not happen* -- made a property of the write rather than of the append. That is a
    law refusing. `loop/resolve.py` catches it at the fold boundary and emits the row's own
    `emits_on_refusal` (the same refusal an effect that declined has always produced), so in a
    season it is never seen as an exception; a probe that writes a `Change` by hand meets it raw.

    ⚠ ITS OWN CLASS, SO A TEST CAN TELL IT FROM `NotYours`. Both are raised after `apply()`, and
    F3 is asked FIRST: an unauthorized Tenure write is refused and PUT BACK as `NotYours` even when
    no declared subject moved, so an effect cannot launder an unlawful edge write as a mere no-op
    (a no-op refusal would otherwise leave the unlawful edge standing)."""


# `Subject.ref`'s three tags. What each reads is `World.state_of`'s; the block above says why.
ENTITY = "entity"
EDGE = "edge"
STAGED = "staged"


@dataclass(frozen=True, eq=False)
class Subject:
    """ONE THING A WRITE NAMES: what a receipt will name (`id`), what the gate reads before and
    after (`ref`), and which of the row's `emits:` kinds it earns if it moves (`earns`).

    `earns=None` is the plain-list contract every effect had before per-kind earning existed: the
    subject earns EVERY kind the row declares. A named kind earns only that one -- `confer` opens
    one edge (`tenure.opened`) and closes another (`tenure.closed`), and conferring onto an unheld
    office must not publish a closure that did not happen.

    `eq=False`: a subject holding a Tenure compares by identity, as the Tenure store does (two
    Tenures may share an `id`; `World._tenure_changes` says so)."""

    id: str
    ref: tuple
    earns: Optional[str] = None

    @classmethod
    def entity(cls, store: str, eid: str, earns: Optional[str] = None,
               fields: Optional[tuple] = None) -> "Subject":
        return cls(eid, (ENTITY, store, eid, tuple(fields) if fields else None), earns)

    @classmethod
    def edge(cls, t: Tenure, earns: Optional[str] = None) -> "Subject":
        return cls(t.id, (EDGE, t), earns)

    @classmethod
    def staged(cls, record_kind: str, eid: str, fieldname: str) -> "Subject":
        return cls(eid, (STAGED, (record_kind, eid, fieldname)), None)


@dataclass(frozen=True, eq=False)
class Change:
    """WHAT AN EFFECT HANDS THE GATE: the subjects it writes, NAMED BEFORE IT RUNS, and the write.

    The gate calls `apply()` between its two reads -- *"the gate applies the write"* (S30.2) is now
    literal for the fold. `apply` still mutates through the store's own methods (`add_tenure`,
    `remove_person`, `_grant_remit`), because those are the one owners of their rules; what moved
    is WHO DECIDES WHETHER IT HAPPENED. An effect says what it will write; the gate says whether it
    did.

    ⚠ THE BOUND, STATED RATHER THAN IMPLIED. `apply` is still a closure, so an effect can mutate
    something it did not name. The gate sees two things it did not declare: every Tenure (G3's
    observation, which F3 judges and a no-op refusal PUTS BACK), and nothing else. An undeclared
    mutation of a non-Tenure entity is as invisible to F9 as it was to everything before it;
    `H-130` is the same class one step over.

    ⚠⚠ AND THE BOUND ITSELF HAS A BOUND -- CORRECTED (antagonist pass, 2026-09-27, `H-137`). "The
    gate sees ... every Tenure" is true only of what runs INSIDE `apply`. The effect that BUILDS
    this `Change` runs earlier, before `World.write` (and its tenure snapshot) is ever reached
    (`loop/resolve.py::_apply_write`) -- a mutation made there, before this object is even
    constructed, is invisible to F3 as well as F9, not merely to F9. Every shipped effect defers
    its mutation into `apply`; nothing enforces that the next one must."""

    subjects: tuple
    apply: Callable[[], None]


def _nothing() -> None:
    return None


# AN EFFECT THAT DECLINES WRITES NOTHING: no subjects, nothing applied. The gate raises
# `NoOpReceipt` on it like on any other write that moved nothing, so "the effect declined" and "the
# effect ran and changed nothing" reach the fold through ONE channel and emit ONE refusal. Before G4
# they were two (a falsy return, and -- for `work` -- nothing at all).
NO_CHANGE = Change((), _nothing)


def no_op(still: list, actor: Optional[str], record_kind: str, fieldname: str) -> NoOpReceipt:
    """The `NoOpReceipt` for a write none of whose `still` subjects moved -- built here so the
    message and the law live once, on `not_yours`' pattern."""
    shown = ", ".join(s.id for s in still[:_NAMED_IN_MESSAGE])
    more = f" and {len(still) - _NAMED_IN_MESSAGE} more" if len(still) > _NAMED_IN_MESSAGE else ""
    return NoOpReceipt(
        f"a ({record_kind}, {fieldname}) write by {actor or 'no actor'} changed nothing: "
        f"{('every subject it named reads the same after it -- ' + shown + more) if still else 'it named no subject'}",
        "F9",
        needs="a write that moves at least one subject it names",
        law="04 §C.2 / PART D row 5 (F9) -- `before == after` is refused AT THE WRITE, so the "
            "receipt is never minted: a success Event for a write that did not happen is ID-9, "
            "and a receipt minted by the gate for it passes every append-side check")


class _Window:
    """The write currently authorized to mint. Not a `Token` -- a token is the authority to ASK for
    a write; this is the record that one was granted, and it is what `mint` checks."""

    # roster-exempt: MECHANISM -- `__slots__` names THIS CLASS'S OWN ATTRIBUTES, as on
    # `carriers.Sensation` and `View`. It is a Python language construct, not a definition of
    # anything in the game, and moving it to `rosters.yaml` would make the attribute list of a
    # private helper into game data.
    __slots__ = ("record_kind", "fieldname", "wclass", "tick")

    def __init__(self, record_kind: str, fieldname: str, wclass: str, tick: int) -> None:
        self.record_kind, self.fieldname = record_kind, fieldname
        self.wclass, self.tick = wclass, tick

    def __repr__(self) -> str:
        return f"({self.record_kind}, {self.fieldname}) {self.wclass} @t{self.tick}"


class Gate:
    """Mints receipts, and remembers which ones it minted."""

    # roster-exempt: MECHANISM -- as above; these are the gate's own private attributes.
    __slots__ = ("_serial", "_minted", "_open")

    def __init__(self) -> None:
        self._serial = 0
        # serial -> the EXACT object handed out. The log checks identity against this, so a
        # forged receipt carrying a real serial is a different object and does not match.
        self._minted: dict[int, Receipt] = {}
        self._open: Optional[_Window] = None

    # -- the window -----------------------------------------------------------------------
    def opening(self, record_kind: str, fieldname: str, wclass: str, tick: int) -> None:
        """Called by `World.write` as it begins an authorized write."""
        self._open = _Window(record_kind, fieldname, wclass, tick)

    def close(self) -> None:
        """Called by `World.write`'s own `finally`, unconditionally, at the end of every write --
        not only at a step barrier (CORRECTED, methodology close, terminal critique, 2026-09-29;
        this docstring described the pre-`H-131`-fix lifetime). A window left open past its own
        write would let a LATER write's first hand-built change mint against this one's instead."""
        self._open = None

    @property
    def is_open(self) -> bool:
        return self._open is not None

    # -- the mint -------------------------------------------------------------------------
    def mint(self, subject: str, mode: str, driver: str,
             field: Optional[str] = None, delta: Any = None, spec: Any = None) -> Receipt:
        """Issue a receipt for the write currently open. Raises outside a window."""
        if self._open is None:
            raise Forbidden(
                f"no gate write is open, so there is nothing to issue a receipt for "
                f"(subject {subject!r}, field {field!r})", "S16",
                needs="a `World.write(...)` that has begun",
                law="a Receipt asserts THE GATE WROTE THIS. Minting one with no write behind it "
                    "is the ID-9 fabrication the type exists to prevent, committed at the mint")
        self._serial += 1
        r = Receipt(subject, mode, driver, field, delta, spec, serial=self._serial)
        self._minted[self._serial] = r
        return r

    def issued(self, change: Any) -> bool:
        """True only for a receipt THIS gate handed out -- identity, never equality.

        ⚠ `is`, NOT `==`. `Receipt` is a dataclass, so `==` compares the six fields, and a forged
        receipt copying a real one's serial and values would compare equal to it. The object is
        the credential; a copy of a credential is not one.
        """
        if not isinstance(change, Receipt):
            return False
        return self._minted.get(change.serial) is change

    def __repr__(self) -> str:
        return f"Gate({self._serial} minted, window={self._open!r})"
