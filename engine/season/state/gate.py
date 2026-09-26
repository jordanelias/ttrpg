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
gate ask WHO wrote a Tenure, which every check before it -- row, step, class -- never did.**

⚠ THE AUTHORIZATION WINDOW, AND WHY IT IS NOT A PER-CALL RETURN VALUE. The obvious design is
`write() -> Receipt`, and it does not fit the one caller that matters. `loop/resolve.py`'s
`_apply_write` cannot know WHAT it changed until the effect has run: the effect reports touched
ids from inside the `apply()` closure, so the subjects of the receipts are discovered DURING the
write and read AFTER it returns. A mint that closed at `return` would therefore be unusable by
the fold -- which is every act in the game -- and the fold would go on hand-building changes,
leaving this file a decoration.

So the window opens when a gate write begins and stays open until the NEXT gate write opens its
own, or the step barrier closes it. `mint()` outside a window raises. The property that buys:
**you cannot mint a receipt without having just performed a real gate write**, which is the whole
of what `changes[]` needs to mean something. What it does not buy: a second receipt minted after
an unrelated later write would be attributed to that write. That is a narrower guarantee than
"one receipt per write" and it is the honest one -- stating it is cheaper than a guard that
implies it.
"""
from dataclasses import dataclass
from typing import Any, Optional

from ..data.matrix import MATRIX, WriteClass
from ..data.rosters import CONFERRAL_BASES, REVOCATION_BASES
from ..gaps import Forbidden, InstrumentDefect, Unspecified
from .carriers import Office, Receipt, Tenure
# ⚠ NO `World` IMPORT, NOT EVEN UNDER `TYPE_CHECKING`: `world` imports this module, and the tree's
# import-cycle instrument (`tests/valoria/test_import_cycle_game_state_npe.py`) reads a guarded
# import as an edge like any other. The functions below take the `World` they are handed and name
# its type as a string only.
from .containment import descendants, parent_of


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
# place the F3 branch is authored, so it is authored here, once, as the fifth basis.
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
CASCADE = "cascade"
CONFERRAL = "conferral"


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
    the same null. (`Office.scope_rung` is not it -- it has no reader in the game and `18a` deletes
    it.)

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


def tenure_write_basis(w: "World", t: Tenure, was: Optional[Tenure], actor: Optional[str],
                       via: Optional[str], gone: frozenset) -> Optional[str]:
    """F3's JUDGMENT FOR ONE CHANGED TENURE: the name of the basis that admits it, or `None`.

    `t` is the Tenure as it stands after the write; `was` is a detached copy of it from before, or
    `None` if the write OPENED it. `gone` is every id the same write removed from the world -- the
    existence changes THIS act caused, observed by the store rather than claimed by the caller.

    THE FIVE BASES, AND WHAT EACH MAY WRITE -- a basis admits a KIND of change, not any change:

      `T-m`       the actor IS the owner -- `was.subject` for an existing edge, `t.subject` for a
                  new one. Anything the owner does to their own edge (`release`, `move`'s legs,
                  `create_record`'s `hold`, a self-conferral's opening). ⚠ The owner is read from
                  BEFORE the write, so an effect cannot make itself the owner by rewriting
                  `subject` and then be admitted as it.
      `T-n`       ⚠ NOT BUILT, AND NOT BUILDABLE HERE: `Tenure` carries no `term` (`04 §B.8`'s
                  `term?` is unbuilt; `write_matrix.yaml` says `Tenure.payload` is to be
                  "REPLACED by `term?`"). No write can cite a term maturation, so this basis admits
                  nothing today; a branch testing a field that does not exist would be `ID-13`'s
                  dead carrier. It is the first thing to add when `term?` lands.
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

    ⚠ `give` (PLAN POSITION 16 ≡ `15a`) IS SETTLED HERE AND NOT BUILT HERE -- the plan's G3
    pre-flight asks for the decision, and the orchestrator scoped it to decision only. The giver's
    close is `T-m`. The RECEIVER'S open matches none of the five: it is not the receiver's act, no
    seat is exercised (`give` is `own`-eligible, `via` is `None`), and nothing ceased to exist. It
    needs ITS OWN basis, and the one that fits is CAUSATION-BOUND like the cascade, not
    authority-bound like T-o: *a `hold` opened on an object that is NOT a seat, of the same kind
    and object as an edge the actor OWNED, was live before, and closed under `T-m` in this same
    write*. The authority to open the receiver's edge is the giver's own edge, ended in the same
    act -- so *release-before-mint* (r2 `05` row 6, ⊕ R14) becomes the gate's condition rather than
    the effect's discipline, and a `give` that forgets the release is refused here before
    `hold_force` ever sees two holders. SEATS ARE EXCLUDED: a seat passes by its conferral basis,
    never by its holder handing it on. It does NOT compose with `via` (no seat is exercised), and it
    is NOT the receiver's own act (position 16 specifies one two-party verb by the giver). Position
    16 adds it as the sixth clause of this function, and nothing else here moves."""
    opened = was is None
    owner = t.subject if opened else was.subject
    if not opened and (t.subject, t.object, t.kind) != (was.subject, was.object, was.kind):
        return None
    if actor is not None and actor == owner:
        return T_M
    if opened:
        moved = None
    else:
        moved = {name for name, now, then in (
            ("since", t.since, was.since), ("until", t.until, was.until),
            ("degree", t.degree, was.degree), ("payload", t.payload, was.payload)) if now != then}
    closed = (not opened and was.until is None and t.until is not None and moved == {"until"})
    if closed and (t.subject in gone or t.object in gone):
        return CASCADE
    seat = w.offices.get(t.object) if t.kind == "hold" else None
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
    the edge it refused is as it was (`NotYours`' own raise is `World.write`'s, via `not_yours`)."""
    return [(t, was) for t, was in changes
            if tenure_write_basis(w, t, was, actor, via, gone) is None]


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
              f"that declares a conferral basis), or {CASCADE} (the edge names something this "
              f"same write removed). T-n is unbuilt: Tenure carries no term",
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
        """Called at a step barrier. A window left open across a barrier would let the next
        step's first hand-built change mint against the previous step's write."""
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
