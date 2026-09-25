"""`season.loop.predicates` — the six `requires:` cells the grammar does not type (five until
`establish` joined them at plan position `13f`, 2026-09-25; the count below is the older one).

EXTRACTED, step 5 of the decomposition (a PURE MOVE but for two call sites, named below). The
registry and its decorator travel with the functions they register, which is the rule step 3
established for `REQUIREMENT_TYPES` and step 5 applies unchanged: **a decorator-filled table lives
in the module that defines the decorated things**, or the table is empty at the moment the loader
reads it.

WHY FIVE AND NOT EIGHT. `W-A` retired `_req_transfer`, `_req_tell`, `_req_move` and `_req_work` on
2026-09-04 — each is a TYPED CELL in `verb_table.yaml` now, read by `evaluate()`. §8's rule is
that a rule lives once, and a verb carrying both a typed cell and a predicate here would be two
readings of one prose cell; that is exactly how `_req_confer` came to drop a disjunct and
`_req_revoke` an entire clause.
`test_wa_one_owner_a_verb_has_a_typed_cell_or_a_predicate_and_never_both` is the guard, and it is
unmoved by this carve — it reads `S.REQUIRES_PREDICATES`, which is this module's dict.

⚠ TWO LINES ARE NOT A BYTE-IDENTICAL MOVE, and they are declared rather than buried: the two
`Query.parent_of` calls are `world_q.parent_of` here. Same function object; a governance predicate
reaches a world query through the module that owns it rather than through a class that also holds
the person-side family.
"""

from __future__ import annotations

from typing import Optional

from ..data.rosters import RELEASABLE_KINDS, title_domain, title_rank
from ..gaps import Forbidden, Unowned, Unspecified
from ..queries import world_q
from ..state.carriers import Office, subject_of


# A `requires:` predicate. The table states preconditions in PROSE, which the fold cannot read --
# the same defect `resolve` had, one column along. A verb with a prose precondition and no
# predicate here REFUSES, naming what is missing, rather than silently succeeding.
REQUIRES_PREDICATES: dict = {}


def requires_predicate(verb: str):
    def deco(fn):
        REQUIRES_PREDICATES[verb] = fn
        return fn
    return deco


# ---------------------------------------------------------------------------
# THE GOVERNANCE SLICE. Jordan, 2026-09-02, asked for governance and management across scales of
# governing bodies. The verbs for it ALREADY EXIST -- all eight `binding_decision` rows -- and not
# one of them executed, because each states its precondition in PROSE. So `post_remit` and
# `chronicle`, two of `W6`'s five witness channels, could never fire: both need a binding decision
# and no binding decision could happen.
#
# ⚠ A FACTION DOES NOT ACT. `ARCHITECTURE_V2.md:93` puts *"a faction acting as an actor"* in its
# REFUSAL table at `L1`, with three corpus cases that wanted it, and `H-21` completes it -- *"a
# faction's treasury is matter at the rung or office that holds it"*. Governance at a scale above
# the person is A PERSON HOLDING AN OFFICE acting at a rung, which is what these four do.
# ---------------------------------------------------------------------------



def in_holdings(w: "World", actor: str, rung: Optional[str]) -> bool:
    """Is this rung one of the actor's HOLDINGS? A `hold` Tenure whose object is a RUNG.

    ⚠ HOLDINGS ARE NOT GOVERNING AUTHORITY, AND JORDAN RULED THE DIFFERENCE OPERATIONAL:
    *"King/Queen cannot revoke title of Duke/Duchess if they do not have duchy is in their
    holdings. King/Queen can revoke title of Duke/Duchess if the duchy is one of their
    holdings."* So a king with governing authority over the whole realm still cannot unmake a
    duke whose duchy he does not hold — which is the same ruling as *"they do not necessarily
    have all territories/provinces/duchies in their holdings"*, made mechanical.

    ⚠ NO NEW TENURE KIND, AND NOT EVEN A NEW OBJECT CLASS. `hold` is already polymorphic over an
    office and over a Record (§13) — and a `hold` WHOSE OBJECT IS A RUNG ALREADY EXISTED in the
    corpus before this function did: probe `F2` writes one at `probes.py:978` and `:985`, holding
    the settlement `S`. So this names a shape the tree was already using rather than adding one,
    and `tenure_kinds` does not move (§8).

    ⚠ THE ORIGINAL WORDING ALSO CITED *"a store"* AS AN EXISTING INSTANCE, AND THAT WAS
    UNSUPPORTED — no `hold` Tenure over a store is constructed anywhere in the instrument.
    Corrected rather than kept, because the sentence's whole job is to say what the tree already
    does. Found by the governance-canon adversarial pass. ⚠ **AND IT IS TRUE NO LONGER, AS OF
    `R8.4` (2026-09-07):** `test_r8_4_document_key_reaches_a_non_author_through_a_store` constructs
    a `hold` over the hearth `Hh`, a rung carrying `stores`, precisely to exercise Part E's own
    `hold:<store>` cell. The sentence is kept with its retraction attached rather than deleted,
    because it is the argument that produced the paragraph.

    ⚠ AND THE NARROW CLAIM WAS THE WRONG THING TO CHECK. *`tenure_kinds` does not move* is true
    and proves nothing about the READERS: `Query.budget` counts every live `hold` as an office, so
    a landholding buys scene actions, and `_ch_document_key` makes a landholder a witness. Both
    pre-date this function; registered as `H-92`.

    ⚠ **THAT SECOND READER MOVED UNDER `R8.4` AND THIS SENTENCE SAID THE OLD THING.** It read
    *"a witness of every Event whose subject is their rung"*, which was the pre-repair predicate —
    and that predicate could not fire on an act at all, because a fold Event's subject is the
    ACTOR. `_ch_document_key` now reads `changes[]`, so a landholder witnesses every Event that
    **changed** their rung, which is strictly wider and is the first form in which `H-92`'s concern
    is actually reachable: a `transfer` into a hearth now makes its holder a witness of an act they
    took no part in. `H-92` is not re-graded here — it is an `FI`/`IN` register row with its own
    owner, and this note exists so the next reader of it is not working from the retracted
    mechanism. Found by the `R8.4` adversarial pass."""
    if rung is None or rung not in w.rungs:
        return False
    return any(t.kind == "hold" and t.subject == actor and t.object == rung and t.live
               for t in w.tenures)


def under_purview(w: "World", actor: str, holding: Optional[str]) -> bool:
    """Is `holding` under the governing authority of a title `actor` holds?

    ⚠ JORDAN, 2026-09-02: *"a Duke can revoke office from any individual in that office so long as
    that office is for a holding under their purview."* So authority over a governance act is
    **RANK + CONTAINMENT** — the actor holds a title whose domain contains the holding — and NOT
    `remit:<act>` on the particular office. That is a different eligibility model from the one
    Part E states, and the difference is registered rather than resolved here (`H-90`).

    ⚠ GOVERNING AUTHORITY, NOT SOVEREIGNTY AND NOT OWNERSHIP. Jordan, same ruling: a King *"may
    have governing authority over the country"* yet hold neither sovereign power over it nor all
    of it in their holdings. This function answers the FIRST question only; the tree models
    neither of the other two."""
    if holding is None:
        return False
    # ⚠ EVERY SEAT, NOT THE FIRST. This read `next((... for t in w.tenures ...), None)` and took
    # whichever title-hold appeared first in an INSERTION-ORDERED list, which was wrong twice
    # over. `Office.rung` is Optional (the office-cluster case, S6.2), and the generator YIELDED
    # `None` as a value -- so a title office with a null rung ended the scan and returned False,
    # and a Duke who was also made a King LOST PURVIEW OVER HIS OWN DUCHY. And a person holding
    # two titles got whichever the tenure list happened to hold first: a Count of P who is also
    # Duke of D was refused purview over D, or over P, depending on insertion order.
    #
    # It is a DISJUNCTION over the seats: authority over a holding is authority from ANY title the
    # actor holds. Taking the highest-ranked seat instead would be the same bug wearing a better
    # argument -- a Duke of D who is also Count of an unrelated P would lose P. Found by the
    # governance-canon adversarial pass.
    for seat in [rung for _, rung in titles_held(w, actor) if rung is not None]:
        # containment walks UP from the holding: a duchy's province is under the duke, a duchy's
        # neighbour is not.
        seen, cur = set(), holding
        while cur is not None and cur not in seen:
            if cur == seat:
                return True
            seen.add(cur)
            cur = world_q.parent_of(w, cur)
    return False


def titles_held(w: "World", actor: str) -> list:
    """Every TITLE this person holds, as `(post, rung)`. THE SINGLE OWNER of the question *what
    does this person govern* -- `under_purview` reads it for containment and `highest_title_rank`
    for rank, so the two cannot drift into different answers about the same person (§8)."""
    out = []
    for t in w.tenures:
        if t.kind == "hold" and t.subject == actor and t.live and t.object in w.offices:
            o = w.offices[t.object]
            if title_domain(o.post) is not None:
                out.append((o.post, o.rung))
    return out


def highest_title_rank(w: "World", actor: str) -> int:
    """The best rank this person holds, or `-1` for someone holding no title at all.

    ⚠ THIS IS WHAT MAKES `title_rank` LOAD-BEARING. Until the governance-canon pass, `title_rank`
    had no caller outside its own test: the ladder was asserted and then decided nothing, which is
    §0.05's reference-wearing-mechanism's clothes. It decides a revocation now."""
    return max((title_rank(post) for post, _ in titles_held(w, actor)), default=-1)


def has_conferral_basis(off: "Office") -> bool:
    """THE BASIS TEST, ONCE: does this office declare how it is filled?

    `_req_confer` asks it of the office being conferred and `_req_establish` of the office being
    founded, so `13d-i` -- which rewrites this test on the rostered values `ED-IN-0256` rules
    (*appointed · elected · annex*) -- edits ONE function and both preconditions inherit it. Today
    the whole test is a non-empty `conferral` string, which is what `_req_confer` inlined."""
    return bool((off.conferral or "").strip())


@requires_predicate("confer")
def _req_confer(w: "World", a: "Act") -> bool:
    """Part E, IN FULL: *"the office's **conferral basis**, and 1-per-object: no live `hold` on the
    object, **or** the holder-Proposition has zero live `commit` (§54 it. 20)"*.

    ⚠ THE FIRST VERSION IMPLEMENTED HALF OF ONE OF TWO CLAUSES -- it dropped the conferral-basis
    conjunct entirely and the `or` disjunct with it, while its docstring claimed *"the cardinality
    rule stated structurally"*. Dropping a disjunct is an OVER-REFUSAL: an office whose
    holder-Proposition has no live commit was refused where Part E admits it. `G4` weighs that
    equally with an invention, and the docstring made it invisible. Found by the governance-slice
    adversarial pass."""
    d = (a.payload or {}) if isinstance(a.payload, dict) else {}
    obj = d.get("office")
    if not obj or obj not in w.offices:
        return False
    if not has_conferral_basis(w.offices[obj]):
        return False                       # no conferral basis: the office cannot be conferred
    if not any(t.kind == "hold" and t.object == obj and t.live for t in w.tenures):
        return True                        # 1-per-object satisfied
    # THE `or` DISJUNCT: a held office is still conferrable when the holder-Proposition carries
    # no live `commit`. §54 item 20.
    holder = next((t.subject for t in w.tenures
                   if t.kind == "hold" and t.object == obj and t.live), None)
    return holder is not None and not any(
        t.kind == "commit" and t.subject == holder and t.live for t in w.tenures)


def office_described_by(a: "Act") -> "Optional[Office]":
    """THE OFFICE AN `establish` ACT DESCRIBES, read once for the precondition and the effect.

    The operands are the office overlay's own keys (`corpus_run._check_office`,
    `populated.build_realm`): `office` (the id), `post`, `rung`, `remit`, `body` and/or `faction`,
    `conferral`, `revocation`. `None` when the id, post, rung or remit is absent, or any operand is
    not the shape the constructor takes -- which is every COMPUTED `establish` today, because the
    row is untyped and `operands_for` carries nothing (`15c` is what changes that).

    ⚠ OTHERWISE IT CONSTRUCTS THE `Office`, AND THE CONSTRUCTOR'S RAISES PROPAGATE. That is the
    point: `Office.__post_init__` is where a remit act is checked against `REMIT_ACTS` (`Unowned`),
    where `office_faction` refuses an unknown body or faction, a mismatch or an office belonging to
    nothing (`Unspecified`/`Forbidden`), and where a title seated in a body is refused
    (`Forbidden`). `corpus_run._check_office` validates an overlay the same way, for the reason it
    gives: *the validator is the constructor, not a second copy of its rules*. The object returned
    is held by nothing -- no `World` is read or written here."""
    d = a.payload if isinstance(a.payload, dict) else {}
    oid, post, rung, remit = d.get("office"), d.get("post"), d.get("rung"), d.get("remit")
    if not all(isinstance(x, str) and x.strip() for x in (oid, post, rung)):
        return None
    if not isinstance(remit, (list, tuple)) or not all(isinstance(x, str) for x in remit):
        return None
    body, faction = d.get("body"), d.get("faction")
    conferral, revocation = d.get("conferral"), d.get("revocation")
    if not all(x is None or isinstance(x, str) for x in (body, faction, conferral, revocation)):
        return None
    return Office(oid, post, rung, list(remit), conferral=conferral, revocation=revocation,
                  body=body, faction=faction)


@requires_predicate("establish")
def _req_establish(w: "World", a: "Act") -> bool:
    """W3's row: *"the establishing office's conferral basis, and a rung to establish it at"*.

    ⚠ THE READING, STATED BECAUSE THE PROSE ADMITS TWO: *the establishing office* is THE OFFICE
    THE ACT DESCRIBES -- the one being founded, or re-remitted on an id that already exists -- and
    NOT the office the actor sits in. The basis `_req_confer` tests is a property of the office
    being FILLED (*"the office's conferral basis"*), so read the same way here it asks whether the
    new seat declares how it is filled. The other reading makes the founder's own seat's basis
    decide whether ANY office may be founded, which nothing in the row motivates; and it would let
    an establish found a seat with no basis, which `_req_confer` then refuses forever -- an office
    that exists and can never be filled. Eligibility (`remit:confer`) already says who may act.

    FOUR CLAUSES, EACH A REFUSAL AND NONE A RAISE -- a raise from inside the effect's `apply()`
    escapes the fold, and `establish.refused` would never be emitted:
      1. the office resolves: `office_described_by` returns one, and the constructor's refusals
         (the three it raises) are translated to False HERE, so each rule still lives once, in the
         constructor. They remain the loud backstop inside the effect;
      2. its rung is one the world holds;
      3. it has a conferral basis, by the ONE basis test `_req_confer` also asks;
      4. its id is new -- held by no collection (a `hold` opened on it early is what the effect
         re-stamps) -- or it is an EXISTING office and the act changes its remit and nothing else.

    ⚠ CLAUSE 4's SECOND ARM IS A REMIT CHANGE, NOT A REFUSAL. `establish` is the only verb whose
    `writes:` name the office's remit, so refusing it on an existing id would leave no act able to
    change a remit. Any other difference -- a different post, rung, body, faction, conferral or
    revocation -- REFUSES: naming a different belonging for an existing id is re-founding, which
    `writes:` does not declare. The act restates the office in full; an operand it omits is read
    as the constructor reads it (`None`), never filled from the office it would replace.
    ⚠ SO AN OFFICE WITH NO RUNG (`Office.rung` is Optional, the office-cluster case §6.2) cannot
    have its remit changed by this verb: clause 2 requires a rung and clause 4 requires the same
    one. That is the row's prose, applied, not a choice made here."""
    try:
        off = office_described_by(a)
    except (Unowned, Unspecified, Forbidden):
        return False                       # the constructor refused it: translated, never filled
    if off is None:
        return False                       # an operand the office needs is not on the act
    if off.rung not in w.rungs:
        return False                       # "a rung to establish it at"
    if not has_conferral_basis(off):
        return False                       # "the establishing office's conferral basis"
    held_as = w.class_of(off.id)
    if held_as is None:
        return True                        # a new office
    if held_as != "Office":
        return False                       # the id is a person's, a rung's... -- `class_of` ambiguity
    cur = w.offices[off.id]
    return (off.post == cur.post and off.rung == cur.rung and off.body == cur.body
            and off.faction == cur.faction and off.conferral == cur.conferral
            and off.revocation == cur.revocation)


@requires_predicate("release")
def _req_release(w: "World", a: "Act") -> bool:
    """`04 §A.3` row 14: *one `release` verb, eligibility `own`, generic over kind*. Part E:
    *"a live tenure of a releasable kind, owned by the actor, toward the subject"*.

    THREE CLAUSES, AND THE FIRST IS THE ONE THE DESIGN IS ABOUT. `t.subject == a.actor` is
    eligibility `own` made real: `_eligible` returns True for every `own` verb without looking at
    anything (*"every person may attempt their own acts"*), so a verb whose whole point is that it
    acts on WHAT THE ACTOR HOLDS must check ownership in its precondition or it is a licence to
    close other people's edges. `_req_revoke` learned this the hard way one column along.

    ⚠ THIS CANNOT FABRICATE, AND THAT IS STRUCTURAL RATHER THAN CAREFUL. `_eff_oblige` was reverted
    (F8, `ED-IN-0211`) for opening a Tenure to `einhir_texts`, a bare string naming no entity,
    because an OPENER takes an id and asserts a relation into existence. A CLOSER scans relations
    that already exist: a subject naming nothing matches no Tenure, the effect touches nothing, and
    the fold emits `release.refused`. There is no path here that mints a fact about a thing nobody
    named -- which is why the antonym half of Jordan's ruling is buildable today while the opener
    half waits on distinct operands (`decision/options.py:307-312`).

    ⚠ `contain` IS EXCLUDED BY THE ROSTER, NOT BY A LITERAL HERE. See `RELEASABLE_KINDS`."""
    subj = subject_of(a)
    if not subj:
        return False
    return any(t.subject == a.actor and t.object == subj
               and t.kind in RELEASABLE_KINDS and t.live
               for t in w.tenures)


@requires_predicate("revoke")
def _req_revoke(w: "World", a: "Act") -> bool:
    """Part E: *"the office's **revocation basis**, and a live `hold` exists"*.

    ⚠ THE FIRST VERSION DROPPED THE OFFICE CLAUSE AND WAS AN OVER-ADMISSION -- it scanned for any
    live `hold` on the payload's object with no check that the object IS AN OFFICE, and §13 makes
    possession of a Record a `hold` Tenure. So a holder of `remit:revoke` could revoke a person's
    possession of a book, and `_eff_revoke` would close it. Asymmetric with `confer`, which did
    check. Found by the governance-slice adversarial pass."""
    d = (a.payload or {}) if isinstance(a.payload, dict) else {}
    obj = d.get("office")
    if not obj or obj not in w.offices:
        return False
    if not (w.offices[obj].revocation or "").strip():
        return False
    # ⚠ TWO RULES, AND WHICH ONE APPLIES TURNS ON WHETHER THE TARGET IS A TITLE.
    #
    # An ORDINARY office — a governor, a council seat — is revocable by GOVERNING AUTHORITY.
    # Jordan, 2026-09-02: *"a Duke can revoke office from any individual in that office so long as
    # that office is for a holding UNDER THEIR PURVIEW."* Rank plus containment.
    #
    # A TITLE is revocable only from HOLDINGS. Jordan, same exchange: *"King/Queen cannot revoke
    # title of Duke/Duchess if they do not have duchy is in their holdings. King/Queen can revoke
    # title of Duke/Duchess if the duchy is one of their holdings."* So a king with governing
    # authority over the entire realm STILL CANNOT unmake a duke whose duchy he does not hold.
    # This is the distinction he drew at the start — governing authority, sovereign power and
    # holdings are three different things — arriving as a branch rather than as prose.
    #
    # ⚠ AND PURVIEW ALONE WOULD HAVE BEEN WRONG HERE. The first version applied `under_purview` to
    # every revocation, so a king could strip any duke in his realm. That is exactly the reading
    # the ruling exists to forbid.
    target_is_title = title_domain(w.offices[obj].post) is not None
    domain = w.offices[obj].rung
    if target_is_title:
        # ⚠ A CONJUNCTION, AND THE FIRST VERSION WAS A SINGLE TERM. It tested `in_holdings`
        # ALONE, which makes holdings SUFFICIENT — so a Dicastery clerk who happened to hold a
        # duchy could unmake its Duke, and a Duke holding the realm could unmake the King. That is
        # the MIRROR of the defect it was written to fix: the version before it conflated governing
        # authority with holdings in one direction, and this conflated them in the other. Jordan's
        # message states a NECESSARY condition on someone who already has the authority —
        # *"King/Queen CANNOT revoke title of Duke/Duchess IF they do not have duchy is in their
        # holdings"* — and message 1 separates the two concepts on purpose. Both terms,
        # therefore, plus rank: the whole point of *"they do not necessarily have sovereign power"*
        # is that holding the land is not the same as outranking the person who governs it. Found
        # by the governance-canon adversarial pass.
        if not under_purview(w, a.actor, domain):
            return False                       # governing authority over the domain
        if not in_holdings(w, a.actor, domain):
            return False                       # AND the domain is one of the actor's holdings
        if highest_title_rank(w, a.actor) <= title_rank(w.offices[obj].post):
            # AND strictly higher rank — which also forbids revoking YOUR OWN title, an
            # equal-rank case nothing else in the branch excluded, and which a Duke who holds his
            # own duchy (the ordinary case) otherwise satisfied.
            return False
    elif not under_purview(w, a.actor, domain):
        return False
    #
    # ⚠ THIS IS A DIFFERENT ELIGIBILITY MODEL FROM THE ONE PART E STATES, AND CALLING IT A
    # COMPATIBLE NARROWING WAS WRONG — that is what this comment said, and it is false of
    # Jordan's text. *"a Duke can revoke office from any individual in that office SO LONG AS that
    # office is for a holding under their purview"* states a SUFFICIENT condition, so keeping Part
    # E's `remit:revoke` as a necessary one on top means a Duke whose office lacks the `revoke`
    # remit cannot revoke a governor inside his own duchy — an OVER-REFUSAL, which `G4` weighs
    # equally with an invention. It is a narrowing relative to PART E, never relative to the
    # ruling. The transcribed `eligibility:` column is not this item's to rewrite, so the conflict
    # is REGISTERED (`H-91`) and named here rather than resolved by a quiet table edit.
    return any(t.kind == "hold" and t.object == obj and t.live for t in w.tenures)


@requires_predicate("dispatch")
def _req_dispatch(w: "World", a: "Act") -> bool:
    """Part E: *the named person exists*."""
    d = (a.payload or {}) if isinstance(a.payload, dict) else {}
    return d.get("subject") in w.persons


@requires_predicate("convene")
def _req_convene(w: "World", a: "Act") -> bool:
    """Part E: *the venue's **container** resolves, or is NONE* (§6.2).

    ⚠ THE FIRST VERSION TESTED THE WRONG THING -- `venue in w.rungs` asks whether the venue IS a
    rung, not whether its CONTAINER resolves, so a top rung (which has no container) passed. And
    `Query.parent_of` already existed, so re-deriving a weaker test here was §8-adjacent. Found by
    the governance-slice adversarial pass."""
    d = (a.payload or {}) if isinstance(a.payload, dict) else {}
    venue = d.get("venue")
    if venue is None:
        return True                        # §6.2's carve-out
    return venue in w.rungs and world_q.parent_of(w, venue) is not None


# ---------------------------------------------------------------------------
# ⚠ FOUR PREDICATES WERE RETIRED HERE BY `W-A` (2026-09-04) -- `_req_transfer`, `_req_tell`,
# `_req_move` and `_req_work`. Each is now a TYPED CELL in `verb_table.yaml`'s `requires_typed:`
# column, read by `evaluate()`, and §8's rule is that the rule lives once: a verb with both would
# be two readings of one cell, which is exactly how `_req_confer` came to drop a disjunct and
# `_req_revoke` an entire clause.
# `test_wa_one_owner_a_verb_has_a_typed_cell_or_a_predicate_and_never_both` is the guard that
# fails on a recurrence.
#
# THE FIVE THAT REMAIN. Four -- `confer`, `revoke`, `dispatch`, `convene` -- are `remit:`-eligible,
# not `own`-eligible, and `W-A`'s scope is the `own` rows. Two of them need grammar forms with no
# `own` cell (`cardinality`, `basis`) and `confer` needs a DISJUNCTION, which no `own` cell has
# and which is therefore not built (`ID-13`: a combinator nothing uses is a dead carrier).
# ⚠ THE FIFTH IS `release` (2026-09-11) AND IT IS AN `own` ROW, WHICH THIS PARAGRAPH ONCE SAID
# COULD NOT HAPPEN. `W-A`'s scope IS the `own` rows, and a predicate on one would ordinarily be a
# cell somebody failed to type. It is not here, and the reason is the same DISJUNCTION that keeps
# `confer` out: `release`'s domain is a SET of six tenure kinds, `data/requires.py` carries `all`
# and no `any`, and §F.24a form 1 `existence` takes ONE `kind:` -- so `all` of the six would mean
# *a live edge of every kind at once*, which is the opposite requirement, and one `existence`
# would silently narrow the verb to one kind. Adding `any` is a GRAMMAR CHANGE (`REQUIRES_STEMS`
# is closed) and `04 §A.3` row 14 asks for a verb, not a form. The verb row states the same thing
# at its `requires_typed_note:` and closes with the condition under which this stops being true:
# *"IF AN `any` COMBINATOR IS EVER RULED, THIS CELL IS THE FIRST THING TO TYPE."*
# ⚠ THE SIXTH IS `establish` (`13f`, 2026-09-25), `remit:`-eligible like the first four. Its
# operands -- post, rung, remit, body/faction, conferral -- are not in `requires_operands`, and its
# clauses ask the `Office` constructor and `World.class_of`, neither of which is a grammar form.
# ---------------------------------------------------------------------------
