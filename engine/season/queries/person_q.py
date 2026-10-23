"""`queries/person_q.py` -- the ASKER-FIRST Query family, `04_CODE_ARCHITECTURE.md` §A.1's AX-2
row and §A.2's table.

> `queries/`  ownerless functions: world_q (World first) · **person_q (asker first)** · cache
>
> `queries/person_q` | owns **nothing** | may read **a `PersonInterior` snapshot only** | -- | --

⚠ **ONE MEMBER, AND THE SMALLNESS IS A MEASUREMENT RATHER THAN A STUB.** Unit L3 adjudicated every
candidate against `04` per symbol instead of executing `ED-IN-0206` item (2) literally, which would
have been wrong. That row reads *"§A.1's AX-2 row assigns the person-side family to
`queries/person_q`; step 7 put budget/opening_set/assemble/entrenchment in `decision.py` instead."*
Measured:

- **`budget` and `opening_set` are named BY `04:133` as `decision/`'s OWN members** -- *"`decision/`
  AX-2's island: questions · opening_set · choose · budget"*. Moving them here would BREAK
  conformance, not restore it. ED-IN-0206 item (2) is wrong about them and says so now.
- **`assemble` is the `questions` member**, same line.
- **`entrenchment` is the only one of the four `04` does not name**, and it is person-first in
  signature and self-declares as a person Query at its own first statement --
  `TRACE.query("entrenchment", "person")`. It reads a `Person` and three ints and touches nothing
  else, which is exactly the *"`PersonInterior` snapshot only"* the table allows. So it is here.
- **Nearly every function in `world_q.py` takes `w: World` first**; the helpers `named` and
  `_stamped` do not (04:116 splits the two families by module, not by first parameter), and no
  check enforces the first-parameter rule. There is no misfiled person-first Query hiding in the
  world-side module: the person-side scan below is what holds the line.

⚠ **§A.3 ROW 2's PROPERTY IS THE POINT, NOT THE FILE COUNT.** *"one `Query` class holding both
families"* becomes *"two modules; the second cannot import the first"*, forced by T-f: *"in one
class, a person-side function calls a resolver-side one with no import to scan."* Splitting by
module makes that checkable, and **nothing checked it until this unit** --
`test_person_q_cannot_reach_the_world_side` is the scan.

`decision/` MAY import this module (`04 §C.3`: *"`decision/` imports `person_q` and `data/`"*), and
does: `choose` and `options` read `stance_toward` and `said_of` from here. The AX-2 by-path scan
(`test_decision_package_never_names_world_anywhere_under_it`) is an allow-list: it forbids
`queries` from `decision/` and admits `queries.person_q` only; this module's own scan
(`test_person_q_cannot_reach_the_world_side`) still forbids `decision`, so the edge runs one way.
"""

from __future__ import annotations

import functools
from typing import Optional

from engine.substrate.descriptors import AFFILIATION_CONCERNS, PURSUITS

from ..data import requires as _requires
from ..data import verbs as _verbs
from ..data import affiliations as _aff
from ..data.affiliations import AFFILIATION_CEILING, conviction_map, engagement
from ..data.cast import STANCE_MAX
from ..data.pursuits import pursuit_cosine_axes, to_axes
from ..data.requires import (
    KNOWN_PERSON_CLAIM, OWN_STATE_STEMS, REQUIRES_OPERANDS, REQUIRES_STEMS, SHORTFALL_PREDICATE,
    UNKNOWN, WORLD_ONLY_STEMS,
)
from ..data.rosters import (
    AFFILIATIONS, DEGREE_STEP, DOMINANCE_KINDS, PURSUIT_AXES, RECORD_CONTENT, SEEN_PREDICATE, roster,
    roster_map,
)
from ..state.carriers import Person, Said
from ..trace_log import TRACE


def entrenchment(p: Person, seasons_held: int, scale: int, span: int) -> int:
    TRACE.query("entrenchment", "person")
    return min(scale, (seasons_held * scale) // span)


def stance_toward(p: Person, referent: str) -> float:
    """§F2's second term, from `p`'s OWN stance rows. #353 `:333`: `(referent, valence -5..+5,
    weight 0..5)`. Valence times weight, summed over the rows naming this referent -- weight is
    what `:333` supplies it for, and dropping it would make a 5-weight conviction and a 0-weight
    one count alike."""
    total = 0.0
    for row in p.stance:
        if len(row) >= 3 and row[0] == referent:
            total += float(row[1]) * float(row[2])
    return total


def held_against(p: Person, referent: str) -> tuple:
    """THE ROWS `p` HOLDS AGAINST `referent`: his OWN stance rows naming it with a valence below zero,
    in order (v9 IN-12 step 13, #453 §9.4 `forgive`). A stance row is `(referent, valence, weight)` and
    carries no kind (K-49), so a field's grudge, a lost field's morale row toward one's own faction and a
    seeded disloyalty are alike here. One owner for two readers: `forgive`'s effect
    (`loop/effects_combat.py::_eff_forgive`, which removes exactly these rows) and its person-side
    decline (`decision/options.py::opening_set`, `rosters.yaml: own_stance_declines`, which forms the verb
    only where this is non-empty)."""
    return tuple(row for row in p.stance
                 if len(row) >= 3 and row[0] == referent and float(row[1]) < 0)


def deeds_judged(p: Person, referent: str, scar_shift: float = 0.0) -> tuple:
    """`(judged, told)`: WHAT `p` MAKES OF THE DEEDS THEY HOLD ABOUT `referent`, by `p`'s OWN
    pursuits (v9 IN-18 `G1`, telling workplan §3's `regard` row). A deed claim is an event-kind
    claim `(referent, <kind>, True)` -- WITNESS's first deposit, or a told copy of one -- with
    `<kind>` in `data/verbs.py::EMITTED_KINDS`. Each is scored as `choose`'s score term 1 scores a
    verb, one owner per factor: `Σ_axis to_axes(crisis_weights(p, scar_shift))[axis] ·
    align_kind(kind, axis)`, so a deed that leans the way `p`'s pursuits point reads positive and
    one that leans against them negative. `judged` sums the deed claims `p` holds FIRSTHAND
    (an empty `chain`, source `firsthand`); `told` sums every other deed claim -- the told valence. Neither weighs the teller
    (§3: *"`judged` has no relation factor, so regard never calls weigh"*), so `regard` cannot
    recurse through `teller_weight`.

    ⚠ A KIND SEVERAL ROWS EMIT (`PAIRED_KINDS`: no `KIND_VERB`) IS NEVER JUDGED BY ITS CLAIM'S
    SUBJECT: `person.died`, `body.changed`, `contest.undecided` among them. Those are exactly the
    kinds whose claim subject may be the PATIENT (WITNESS's `both` rule deposits one claim per changed
    subject), so a victim is not judged for dying. v9 IN-58 (RS-23, RS-24) judges such a deed ONCE,
    FOR ITS DOER, through the `seen.who` pairing (`deed_doer`): a deed claim `(s, kind, True)` whose
    pairing names `x` adds `lean · bond` to `p`'s judgement of `x` -- `lean` the deed's pursuit
    valence (`_lean`, read off the authored `deed:<kind>` cells, RS-29) and `bond` the judge's
    allegiance to the patient `s` (`_bond`, the STORED half `stance_toward(p, s)` only; never
    `regard`, which calls this function). The killer-subject claim of such a kind scores nothing, so
    the killer is counted once; an unpaired claim (no `seen`, `who` withheld, ambiguous) scores
    nothing, so a hidden actor stays hidden. A paired deed lands in `judged` or `told` by the deed
    claim's own `firsthand`, as every deed does.
    ⚠ THE SWORN-TO HALF SHIPS OFF (IN-58): `oblige` is a `World` Tenure read by a `world_q` reader and
    this module reads a `PersonInterior` only. FACTION-LEVEL grievance is v9 IN-70's: `opinion` here,
    its World half and its referents in `world_q` (`opinion_of`, `opinion_referents`).
    [ASSUMPTION, H-192: a deed's claim subject is read as its doer for every other kind; the sum is
    unnormalised.] Person-side, no World (AX-2).
    ⚠ v9 SC-02 `22a`: WHICH claims are `referent`'s deeds is `attributed_deeds`' and WHAT each is worth
    is `deed_term`'s; this function sums them by `firsthand`, and `world_q.reception` sums the same two
    by remove and confidence, so the two readers cannot disagree on either."""
    axis_w = None
    judged = told = 0.0
    for c in attributed_deeds(p.ledger, referent):
        if axis_w is None:
            axis_w = projected_axes(p, scar_shift)
        v = deed_term(p, axis_w, c)
        # FIRSTHAND only is judged (`dissents`' and `record`'s precedent, `decision/options.py`):
        # a `told_by` claim whose chain is empty is still hearsay, and lands in `told`.
        if c.firsthand:
            judged += v
        else:
            told += v
    return judged, told


def attributed_deeds(ledger, referent: str):
    """THE DEED CLAIMS IN `ledger` THAT RECORD AN ACT OF `referent`'s, in ledger order -- the one owner
    of *which of a holder's claims are about what this person did* (v9 SC-02 `22a`, split out of
    `deeds_judged` unchanged). An unpaired kind's claim is `referent`'s when its subject is
    ([ASSUMPTION, H-192]), told or not; a `PAIRED_KINDS` claim is `referent`'s when it is untold and its
    `seen.who` pairing names him (`deed_doer`, IN-58) -- the paired kinds are the ones whose subject
    may be the PATIENT, so the doer is read off the sighting's `who`, never the subject. A told copy
    carries no `seen`, so a paired claim heard second-hand names nobody. Person-side (AX-2)."""
    seen = functools.cache(lambda: _seen_index(ledger))
    for c in ledger:
        if not is_deed(c):
            continue
        if c.predicate in PAIRED_KINDS:
            if c.chain or deed_doer(c, seen()) != referent:
                continue
        elif c.subject != referent:
            continue
        yield c


def deed_term(p: Person, axis_w: dict, c) -> float:
    """WHAT ONE OF `attributed_deeds`' CLAIMS IS WORTH TO `p`, whose projected pursuits are `axis_w`:
    a paired deed `lean · bond` (`_lean`, `_bond` on the claim's patient, IN-58), any other
    `deed_valence`. The same numbers `paired_deed_term` and `deed_valence` give; `deeds_judged` and
    `world_q.reception` both read it here. Person-side (AX-2)."""
    if c.predicate in PAIRED_KINDS:
        lean = _lean(axis_w, c.predicate)
        return _paired_weight(p, c, lean) if lean else 0.0
    return deed_valence(axis_w, c)


def suffered_deeds(ledger, patient: str):
    """THE DEEDS `ledger` RECORDS AS DONE TO `patient` BY SOMEBODY ELSE, in ledger order (v9 SC-02 `22a`,
    step 20's called bluff): the untold `PAIRED_KINDS` claims whose subject is `patient` and whose
    `seen.who` pairing names a doer (`deed_doer`, which never names the subject himself). Only a paired
    kind has a patient on its claim; an unpaired kind's subject is its doer (H-192), so it is never a
    deed suffered. A told copy has no sighting and so names no doer: what a holder was only told of
    does not count. Person-side (AX-2)."""
    seen = functools.cache(lambda: _seen_index(ledger))
    for c in ledger:
        if (c.subject == patient and not c.chain and is_deed(c) and c.predicate in PAIRED_KINDS
                and deed_doer(c, seen()) is not None):
            yield c


# v9 IN-58: THE DEED KINDS JUDGED ONLY THROUGH THE `seen.who` PAIRING -- every DEED kind no single
# row emits (`KIND_VERB` names no verb for it), read off the table, no kind listed. Such a kind's
# claim subject may be the doer OR the patient (`both`), and no verb says which, so its valence
# (an authored `deed:<kind>` cell, `align_kind`) enters for the doer a `seen` claim names.
PAIRED_KINDS = frozenset(k for k in _verbs.DEED_KINDS if k not in _verbs.KIND_VERB)
# The strata of the rows that emit each paired kind: a `seen` claim pairs with a deed of that kind
# only if what the witness saw was an act of one of them (`Seen.stratum`). Every channel showing
# `who` shows `stratum` (`rosters.yaml: observation_terms.supplied_by`), so the test never drops a
# pairing that `who` alone would have made; it refuses a third party's DIFFERENT act on the patient in
# the same round being read as the deed's doer.
_KIND_STRATA = {k: frozenset(r.stratum for r in _verbs.VERB_TABLE.values() if k in r.emits)
                for k in PAIRED_KINDS}


def _seen_index(ledger) -> tuple:
    """A holder's own, untold `seen` claims, indexed twice: `(subject, when, round) -> [seen]`, and
    `(when, round) -> {(who, stratum)}` -- who the holder saw acting, and at what, in each round."""
    by_subject: dict = {}
    acting: dict = {}
    for s in ledger:
        if s.predicate == SEEN_PREDICATE and not s.chain:
            by_subject.setdefault((s.subject, s.when, s.round), []).append(s)
            who = getattr(s.value, "who", None)
            if who is not None:
                acting.setdefault((s.when, s.round), set()).add((who, getattr(s.value, "stratum", None)))
    return by_subject, acting


def deed_doer(c, seen: tuple):
    """v9 IN-58's PAIRING RULE: WHO DID THE DEED `c` TO ITS SUBJECT, as the holder saw it, or `None`.

    `c` is an untold deed claim `(s, kind, True)` of a `PAIRED_KINDS` kind; `seen` is
    `_seen_index` of the same ledger. A `seen` claim PAIRS with it when it has the same subject
    `s`, `when` and `round` (WITNESS deposits both from one Event in one pass), names a `who`, that
    `who` is not `s` (a deed done TO `s` -- `s`'s own act in the same round is not it), and its
    `stratum` is the stratum of a row emitting `kind`. The doer is the ONE `who` the pairing
    names; none, or two different, is `None` -- the pairing never guesses, so a channel that
    withheld `who` leaves the actor hidden.
    ⚠ AND `s` MUST NOT HAVE BEEN SEEN DOING SUCH AN ACT IN THAT ROUND: then `c` may be the claim
    `both` anchors on the ACTOR (`(x, person.died)` for x's kill), and a third party's sighting on
    `s` would name the wrong doer of the wrong death. MEASURED at IN-58 on the corpus before this
    clause: 1 of 61 killer-subject `person.died` claims paired, to the witness's own attack on the
    killer in the same round. The price, stated: a person who both struck and was struck in one
    round is judged a patient by nobody that round.
    LIMIT, stated: where the ACTOR died attacking, the sighting names him as `who` of his own death,
    so no killer is named. A `seen` on the same subject, `when` and `round` that names NO `who` (a
    channel that withheld the actor) makes the pairing ambiguous, so `None`: an unnamed hand may be
    the one that did it. Holder-side and World-free: `Seen` is read by its fields, never imported
    (AX-2)."""
    if c.chain or not is_deed(c) or c.predicate not in PAIRED_KINDS:
        return None
    by_subject, acting = seen
    strata = _KIND_STRATA[c.predicate]
    if any(who == c.subject and st in strata for who, st in acting.get((c.when, c.round), ())):
        return None
    whos = set()
    for s in by_subject.get((c.subject, c.when, c.round), ()):
        who = getattr(s.value, "who", None)
        if who is None:
            return None             # an actorless sighting on the same key: ambiguous, never guess
        if who == c.subject or getattr(s.value, "stratum", None) not in strata:
            continue
        whos.add(who)
    return next(iter(whos)) if len(whos) == 1 else None


def _kind_engages(kind: str, affiliation: str) -> bool:
    """A DEED KIND ENGAGES AN AFFILIATION when every verb row emitting it has a nonzero
    `data/affiliations.py::engagement` cell for it -- for the one verb a kind names (`KIND_VERB`) that
    is the verb's cell; for a `PAIRED_KINDS` kind (several rows emit it) ALL the emitters must engage,
    because the claim does not say which row made it and the reading never guesses. The cell's SIGN is
    not asked: an act the affiliation condemns and one it holds sacred both engage it (v9 IN-67
    [ASSUMPTION; medium; Jordan to correct -- revert: the form takes a sign and matches that sign's cells
    only]). ⚠ `engagement(verb, name)` falls back to the shared `sacred` column for an affiliation with no
    column of its own (`einhir_restoration` has none), so `engaging: einhir_restoration` (FA-05, FA-06)
    names the doers of any vow-shaped deed, KEEPING a vow included."""
    verbs = [v for v, r in _verbs.VERB_TABLE.items() if kind in r.emits]
    return bool(verbs) and all(engagement(v, affiliation) for v in verbs)


def deed_doers(ledger, spec: dict, holder: str, against=()) -> tuple:
    """WHO THE HOLDER'S OWN LEDGER NAMES AS THE DOER OF A DECLARED CLASS OF DEED (v9 IN-67, A-31's
    `deed_doers` goal object: "threats", "heretical activity", "corruption"), in ledger order, each
    once. `spec` is the goal's `object:` mapping and names EXACTLY ONE form of
    `rosters.yaml: goal_object_kinds.forms.deed_doers` (a mapping that names none, or `against` with
    nobody in `against`, names nobody):

      * `kinds: [<deed kind>, ...]` -- a deed claim of one of those kinds;
      * `engaging: <affiliation>` -- a deed claim of a kind that engages that affiliation
        (`_kind_engages`);
      * `against: <goal id>` -- a deed claim whose PATIENT is among `against`, the named goal's
        referents, which the caller (`world_q.goal_referents`, a World read) resolves and passes in.
        Only a `PAIRED_KINDS` claim has a patient (its subject); an unpaired kind's subject is its
        doer (below), so no patient is named and it never matches this form.

    `is_deed` is the one owner of what a deed claim is. ⚠ THE DOER IS NEVER READ OFF A PAIRED CLAIM'S
    SUBJECT: a `PAIRED_KINDS` claim's subject may be the PATIENT (`person.died` of a victim), so in
    EVERY form such a claim is routed through `deed_doer` (the `seen.who` pairing, IN-58) and a claim
    the pairing cannot resolve names no doer -- `kinds: [person.died]` names the killer, never the
    victim. Any other deed kind reads its subject as its doer ([ASSUMPTION; H-192], `deeds_judged`'s).
    NEVER THE HOLDER HIMSELF: a claim recording his own act (`Claim.doer == holder`, ED-IN-0294, the
    second reader of that field beside `world_q.attention_key`) is skipped whatever its subject -- else
    the patient of his own deed would be named as the doer of it -- and `holder` is dropped from the
    answer, so a told copy of his own deed does not make him a referent either.

    Reads the holder's OWN ledger only: a deed he was not told of and did not see names nobody, however
    plain it is in the world (AX-2; a `World` is never asked). Person-side."""
    form = next((f for f in roster_map("goal_object_kinds", "forms")["deed_doers"] if f in spec), None)
    if form is None or (form == "against" and not against):
        return ()
    kinds = frozenset(spec["kinds"]) if form == "kinds" else frozenset()
    seen = None
    engages: dict = {}                     # kind -> bool, per call: the tables are rebound by tests
    out: list = []
    for c in ledger:
        if not is_deed(c) or c.doer == holder:
            continue
        if form == "kinds":
            hit = c.predicate in kinds
        elif form == "engaging":
            if c.predicate not in engages:
                engages[c.predicate] = _kind_engages(c.predicate, spec["engaging"])
            hit = engages[c.predicate]
        else:
            hit = c.predicate in PAIRED_KINDS and c.subject in against
        if not hit:
            continue
        if c.predicate in PAIRED_KINDS:
            if seen is None:
                seen = _seen_index(ledger)
            doer = deed_doer(c, seen)
        else:
            doer = c.subject
        if doer is not None and doer != holder and doer not in out:
            out.append(doer)
    return tuple(out)


def paired_deed_term(p: Person, axis_w: dict, c, seen_of) -> tuple:
    """`(doer, term)`: THE ONE SCORER OF A PAIRED DEED CLAIM (v9 IN-58, IN-72; `CLAUDE.md` §8, the rule
    lives once). `c` is a deed claim `p` holds; `axis_w` is `p`'s projected pursuits; `seen_of` is a
    zero-argument callable returning `_seen_index(p.ledger)` (called only when a pairing is read).
    `doer` is the one `deed_doer` names and `term = lean · bond` (`_lean`, `_bond`) is what the deed
    adds to `p`'s judgement of that doer; `world_q.attention_key`'s tier 2 ranks a claim by `|term|`
    (`deed_term` is the same number for `deeds_judged` and `world_q.reception`). `(None, 0.0)` for every claim that is not a paired deed, that `p`'s
    pursuits do not lean on, that is told (`chain`), or whose pairing names no doer (no `seen`, `who`
    withheld, ambiguous): an unpaired claim scores 0, so a hidden actor stays hidden. Person-side (AX-2)."""
    if c.predicate not in PAIRED_KINDS or c.chain:
        return None, 0.0
    lean = _lean(axis_w, c.predicate)
    if not lean:
        return None, 0.0            # no authored lean on `p`'s axes: nothing to weigh, no pairing read
    doer = deed_doer(c, seen_of())
    if doer is None:
        return None, 0.0
    return doer, _paired_weight(p, c, lean)


def _paired_weight(p: Person, c, lean: float) -> float:
    """A paired deed's term, `lean · bond` on the claim's patient: the one formula `deed_term` and
    `paired_deed_term` share (`CLAUDE.md` §8, the rule lives once)."""
    return lean * _bond(p, c.subject, lean)


def _bond(p: Person, patient: str, lean: float) -> float:
    """v9 IN-58's FACTOR: how `p`'s allegiance to the deed's PATIENT weighs the deed,
    `1 - a · sign(lean)`, `a = clamp(stance_toward(p, patient) / STANCE_MAX, -1, 1)` -- the stored
    half only, normalised as `teller_weight` normalises regard. In `[0, 2]`, and the deed term
    `lean · _bond` FALLS as `a` rises whatever the pursuits' sign: full allegiance doubles a
    condemnation and cancels an approval; full enmity doubles an approval and cancels a
    condemnation; no stance (`a = 0`) judges the deed by pursuits alone. The judge who IS the
    patient is his own full ally (`a = 1`): no stance row names oneself, and reading it would judge
    his own attacker as a stranger's. [ASSUMPTION; medium;
    Jordan to correct -- the form of the factor; revert: no factor and the two cells unauthored.]"""
    a = 1.0 if patient == p.id else max(-1.0, min(1.0, stance_toward(p, patient) / STANCE_MAX))
    return 1.0 - a if lean > 0 else 1.0 + a


def is_deed(c) -> bool:
    """A DEED CLAIM: an event-kind claim `(x, <kind>, True)`, `<kind>` in `EMITTED_KINDS` -- what
    WITNESS's first deposit writes, or a told copy of it (a `Claim` or a `Said`). A kind some row
    emits on refusal (`REFUSAL_KINDS`) is no deed: it reports an act that did not happen."""
    return c.value is True and c.predicate in _verbs.DEED_KINDS


def deed_valence(axis_w: dict, c) -> float:
    """How a holder whose projected pursuits are `axis_w` judges one deed claim `c`:
    `Σ_axis axis_w[axis] · align_kind(c.predicate, axis)`; 0 for a claim that is no deed, and 0 for
    a `PAIRED_KINDS` claim, whose valence enters only for its doer through `deeds_judged`'s pairing
    (v9 IN-58) -- never for the claim's subject, who may be the patient. The one scoring of a deed,
    read by `deeds_judged` (G1), `said_of`'s slant (G3) and `world_q.attention_key` (IN-57)."""
    if not is_deed(c) or c.predicate in PAIRED_KINDS:
        return 0.0
    return _lean(axis_w, c.predicate)


def _lean(axis_w: dict, kind: str) -> float:
    """`Σ_axis axis_w[axis] · align_kind(kind, axis)`: how pursuits projected to `axis_w` lean on a
    deed of `kind`. One owner for the unpaired (`deed_valence`) and the paired (IN-58) scoring."""
    return sum(axis_w[ax] * _verbs.align_kind(kind, ax) for ax in _AXES)


# sorted: PURSUIT_AXES is a frozenset, and a float sum's order would move with PYTHONHASHSEED
# while callers test the result for exact zero.
_AXES = tuple(sorted(PURSUIT_AXES))


def regard(p: Person, referent: str, fx=None) -> float:
    """HOW `p` REGARDS `referent`, computed when read and never written (telling workplan §1's
    spine):

        regard = stance_toward(p, x) + judged_gain · judged + told_valence_gain · told

    the stored half (`stance_toward`, the person's own stance rows) plus `deeds_judged`'s two
    halves (v9 IN-18 `G1`). With no `fx`, or with both gains 0 -- the CONTROL (both ship live at 0.5,
    `H-192`/`H-193`) -- it is the stored half exactly and reads no ledger. ⚠ `judged_gain` IS NOT
    `regard_gain`: the shape row spells `regard_gain · judged`, but `regard_gain` is `teller_weight`'s
    relation gain (`H-179`, shipped 0.5), and zeroing it for G1's control would move every told
    claim's weight -- two decisions on one fixture, `H-121`'s defect. A second name for one sum is
    deliberate: `decision/options.py::teller_weight` asks for REGARD, so when the gains move, the
    reader does not."""
    stored = stance_toward(p, referent)
    if fx is None:
        return stored
    jg = float(fx.get("judged_gain"))
    tg = float(fx.get("told_valence_gain"))
    if not (jg >= 0 and tg >= 0):
        raise ValueError(f"judged_gain {jg} / told_valence_gain {tg} must be >= 0 (H-192/H-193)")
    if not jg and not tg:
        return stored
    judged, told = deeds_judged(p, referent, fx.get("scar_weight_shift"))
    return stored + jg * judged + tg * told


# ---------------------------------------------------------------------------
# v9 IN-23 (CARRY-STABILITY): LEGITIMACY AND STABILITY AS ONE PERSON'S OWN WINDOWED ESTIMATE.
# Ruling R7 (`references/design_rulings_2026-09-06.md`, reference): *"no magnitude carrier is admitted at
# any scale"*, and *"there is no single faction-legitimacy number ... a ruler can be wrong about their
# own standing"*. So neither is a field, a cache or a world-level sum: each is asked of ONE person's
# own stance rows and claims, and two persons holding different ledgers read different values.
# ---------------------------------------------------------------------------

#: THE DEED KINDS `stability` COUNTS AS UNREST AT ITS SUBJECT: the coercive kinds of
#: `rosters.yaml: standing_routes.kinds.dominance` (a death, a wound, a field won, a seizure of a rung
#: or a record, a requisition), read off that roster and listing no kind here. With the shortfall
#: claim's stem (`SHORTFALL_PREDICATE`) they are the whole of what `stability` reads.
UNREST_KINDS = DOMINANCE_KINDS


def recent_claims(ledger, window) -> list:
    """THE CLAIMS IN `ledger` FROM ITS HOLDER'S LAST `window` SEASONS, in ledger order: those whose
    `when` is less than `window` seasons before the NEWEST claim the ledger holds (so `window == 1` is
    the newest season alone). An empty ledger has no recent claims.

    ⚠ ANCHORED ON THE HOLDER'S NEWEST CLAIM, NOT ON THE CLOCK. `choose` receives no tick (S18.2: two
    scalars), and an estimate is recent only against what else its holder knows: a person who has
    heard nothing for seasons reads his last news as current, which is R7's *a ruler can be wrong
    about their own standing* in time as well as in content [ASSUMPTION; medium; Jordan to correct;
    revert: the caller passes `World.tick` as the anchor]. `window` is a whole number of seasons
    >= 1 (`Fixtures.estimate_window_seasons`, H-224); anything else raises."""
    if isinstance(window, bool) or not isinstance(window, int) or window < 1:
        raise ValueError(f"estimate window {window!r} is not a whole number of seasons >= 1 (H-224)")
    newest = max((c.when for c in ledger), default=0)
    return [c for c in ledger if newest - c.when < window]


def legitimacy(p: Person, holder: str, window, scar_shift: float = 0.0) -> float:
    """HOW `p` READS `holder`'s STANDING -- the legitimacy of a seat-holder as one person estimates it
    (R7: a Query over stance; v9 IN-23). Computed when read and never written:

        legitimacy = stance_toward(p, holder) + Σ deed_term(p, axis_w, c)
                     over c in attributed_deeds(recent_claims(p.ledger, window), holder)

    `p`'s own stance rows toward the holder (a stance row has no `when`, so the window does not cut
    it) plus what `p`'s own pursuits make of the holder's deeds `p` holds claims of from the window
    -- firsthand and told alike FOR THE UNPAIRED KINDS ONLY, because R7's channel is the news:
    legitimacy falls where the news of a deed has reached. ⚠ The PAIRED kinds (`person.died`,
    `body.changed`) count firsthand only: `attributed_deeds` drops a told copy of one (it carries no
    `seen`, so it names no doer), so second-hand news of a killing or a wound never moves legitimacy.
    Each deed is scored by its one owner (`deed_term`; `attributed_deeds` decides
    which claims are the holder's, the paired kinds through `seen.who`), so this is `regard`'s two
    halves read over the window at unit weight, not a second scoring of a deed. Which seat the holder
    holds is the CALLER's: `p` holds no claim of who sits where (`H-195`: no `held_by` claim), so
    `holder` is passed. Person-side, no World (AX-2)."""
    TRACE.query("legitimacy", "person")
    total = stance_toward(p, holder)
    deeds = attributed_deeds(recent_claims(p.ledger, window), holder)
    if not deeds:
        return total
    axis_w = projected_axes(p, scar_shift)
    for c in deeds:
        total += deed_term(p, axis_w, c)
    return total


def stability(p: Person, rung: str, window) -> int:
    """HOW STABLE `p` READS `rung` -- minus the number of signs of unrest `p` holds about it from the
    window (R7; v9 IN-23). `0` is *no unrest I know of*: a person who holds nothing about a place is
    owed nothing (`04_CODE_ARCHITECTURE.md` §C.11), and reads it as stable.

    A sign is a claim in `recent_claims(p.ledger, window)` whose SUBJECT is `rung` and that is either
      * a deed claim (`is_deed`) of an `UNREST_KINDS` kind: `person.died`, `body.changed`,
        `field.won`, `rung.seized`, `record.seized`, `requisition.taken` (the dominance roster's
        members at IN-23), or
      * a shortfall claim, `(rung, "shortfall:<kind>", units)` (`SHORTFALL_PREDICATE`, deposited by
        WITNESS from MATTER's larder write).
    Firsthand and told count alike, one each [ASSUMPTION; medium; Jordan to correct -- unweighted by
    confidence or by teller; one deed can count twice, but only where `loop/witness.py`'s `T5` guard
    lets a second copy in -- told first and seen after, or told from two different origins (a told
    copy of a deed already held firsthand, or of the same origin, is skipped at deposit); revert:
    grade each sign by `Claim.confidence`]. NOT read, though they exist: `tenure.closed` (it also closes a
    `contain`, so a person moving house would read as a fallen seat), `march.declared` (an intent, not
    yet coercion), and the `seen` claims (they carry a stratum, not a kind). Only claims whose subject
    IS the rung count: a person does not know what a rung contains (containment is the world's).
    Person-side, no World (AX-2)."""
    TRACE.query("stability", "person")
    return -sum(1 for c in recent_claims(p.ledger, window)
                if c.subject == rung and (
                    (is_deed(c) and c.predicate in UNREST_KINDS)
                    or str(c.predicate).partition(":")[0] == SHORTFALL_PREDICATE))

def opinion_terms(p: Person, expected: dict, engaged: tuple, regarded: tuple, fx=None) -> tuple:
    """`(pursuit, affiliation, regard)`: THE THREE TERMS OF `p`'s OPINION OF A FACTION, each on `[-1, +1]`
    (v9 IN-70; RS-23, RS-24; ED-IN-0293 (6): *"a sympathy for a faction is an OPINION, computed at read
    from convictions and allegiances"*). One ladder per quantity (`CLAUDE.md` §0.06 S): every term is
    normalised by the owner that already normalises it, before the sum.

      * `pursuit` -- `data/pursuits.py::pursuit_cosine_axes` of `p`'s projected pursuits
        (`projected_axes`, the vector `world_q.attention_key`'s salience reads, at the same
        `scar_weight_shift`) against `to_axes(expected)`, the faction's expected pursuit map
        (`data/goals.py::expected`, IN-69's owner). Already a cosine. `None` -- a side with no
        direction -- reads `0.0`, the salience precedent.
      * `affiliation` -- the mean, over the `(affiliation, sign)` pairs in `engaged` (the poles the
        faction's own goals engage, and the side each takes; the caller reads them), of
        `sign * intensity / AFFILIATION_CEILING`: `p`'s held intensity on that pole (a held 0 and an
        absent pole read alike, 0) over the spine's ceiling. `0.0` for no pole. A
        MEAN, not a sum, so the term stays on `[-1, +1]` however many poles a faction engages.
      * `regard` -- the mean, over the persons in `regarded` (the faction's head and the doers `p`'s
        own ledger names who are live members of it; the caller reads them, and membership is world truth), of `clamp(regard(p, x, fx) / STANCE_MAX,
        -1, 1)` -- `regard`, the one owner, normalised exactly as `decision/options.py::teller_weight`
        normalises it. `0.0` for nobody.

    PERSON-SIDE, NO WORLD (`04` §A.2: `person_q` reads a `PersonInterior` only): WHO the faction's head
    and members are, what it expects and which poles its goals engage are the caller's to read
    (`world_q.opinion_of`), and arrive here as plain values. Nothing is stored (A-29, T-a)."""
    shift = fx.get("scar_weight_shift") if fx is not None else 0.0
    cosine = pursuit_cosine_axes(projected_axes(p, shift), to_axes(expected or {}))
    held = p.conviction or {}
    aff = (sum(sign * held.get(name, 0) / AFFILIATION_CEILING for name, sign in engaged) / len(engaged)
           if engaged else 0.0)
    reg = (sum(max(-1.0, min(1.0, regard(p, x, fx) / STANCE_MAX)) for x in regarded) / len(regarded)
           if regarded else 0.0)
    return (0.0 if cosine is None else cosine), aff, reg


def opinion(p: Person, expected: dict, engaged: tuple, regarded: tuple, fx=None) -> float:
    """`p`'s OPINION OF A FACTION, on `[-3, +3]`: the sum of `opinion_terms` (v9 IN-70). `0` is
    indifference -- each term's own midpoint -- so the sign is the side. Computed when asked, never
    written (A-29, T-a). Person-side; the World half is `world_q.opinion_of`. Added left to right, not
    by `sum()`, whose float summation is compensated since Python 3.12: one order, one number. (The
    means inside `opinion_terms` use `sum()`; the value is consumed only as `< 0`, so a last-ulp
    difference between Python versions matters only at exact cancellation.)"""
    pursuit, affiliation, reg = opinion_terms(p, expected, engaged, regarded, fx)
    return pursuit + affiliation + reg


def violated_pursuits(p: Person, verb: str) -> tuple:
    """WHICH OF `p`'s OWN PURSUITS AN ACT OF `verb` VIOLATES -- the per-element half of the scar
    (IN-08 H3, `ED-IN-0261`'s scar model: a COUNT per element, accrued by WITNESSING).

    A pursuit `e` that `p` holds (weight > 0) is violated when `Σ_axis projection[e][axis] ·
    alignment(verb, axis) < 0` -- the verb leans against where the pursuit points. ⚠ THAT SIGN TEST
    IS A CANDIDATE READING RECORDED FOR REVIEW, NOT A RULING (`workplans/valoria_master_workplan_v9_part5.md`,
    IN-08 H3): no source states the violation predicate; this is the plainest one the two owned
    tables admit. It composes on the two owners and copies neither: `data/pursuits.py::to_axes`
    (pursuit -> axes, one owner) and `data/verbs.py::align` (the one binding the alignment sweep
    rebinds). A verb with no celled axis violates nothing, by construction. Person-side, no World
    (AX-2). Sorted, so a caller writing counts in this order writes a canonical dict.

    NO PRODUCTION CALLER: `loop/resolve.py::_scar_witnesses` asks `elements_violated_by` once per act
    and `broken_by` per person, which compose the same `_pursuits_violated_by` below. This wrapper
    is the per-person reading kept for tests (`test_h11_affiliation_scar.py` asserts it equals
    the production scar; `test_h3_scar_by_observation.py` computes its own), so a change to the sign test is made in `_pursuits_violated_by`."""
    return _held(p.pursuits, _pursuits_violated_by(verb))


def violated_affiliations(p: Person, verb: str) -> tuple:
    """WHICH OF `p`'s OWN RELIGIOUS AFFILIATIONS AN ACT OF `verb` VIOLATES -- IN-08 H11, H3's
    mechanism over the affiliation table (J-5's C4).

    An affiliation `a` that `p` holds (intensity > 0) is violated when `data/affiliations.py::
    engagement(verb, a) < 0`: the verb's cell for that affiliation, which is the shared column's
    cell when the affiliation has none of its own (R-C4.1: the vow-shaped verbs engage every creed
    alike). A sign test, as `violated_pursuits` is; the intensity does not enter it, because the
    scar is a COUNT per element and an act is witnessed or not. It is `violated_pursuits`'
    sibling and not a second scar path: `loop/resolve.py::_scar_witnesses` asks for both through
    `elements_violated_by` + `broken_by` and writes once, so this wrapper has no production caller
    (it is a test oracle, as `violated_pursuits` is). Person-side, no World (AX-2). Sorted, as
    `violated_pursuits` is."""
    return _held(p.conviction, _affiliations_violated_by(verb))


def _pursuits_violated_by(verb: str) -> frozenset:
    """The pursuits an act of `verb` violates, whoever holds them: `violated_pursuits`' sign test,
    which reads only `(verb, element)`. The candidates are `data/verbs.py::PURSUIT_PROJECTION`'s
    keys, read through the module at call time so a rebound projection is what is asked; a pursuit
    the projection does not list projects to the zero vector and violates nothing."""
    row = {ax: _verbs.align(verb, ax) for ax in PURSUIT_AXES}
    if not any(row.values()):
        return frozenset()
    return frozenset(e for e in _verbs.PURSUIT_PROJECTION if pursuit_lean(verb, e, row) < 0)


def pursuit_lean(verb: str, e: str, row: Optional[dict] = None) -> float:
    """HOW FAR AN ACT OF `verb` POINTS THE WAY PURSUIT `e` DOES: `Σ_axis to_axes({e: 1})[axis] *
    align(verb, axis)` -- the pursuit's unit projection dotted with the verb's alignment row (`row`,
    when the caller holds it already: `{axis: align(verb, axis)}`). THE OWNER of that dot for the sign
    test (`_pursuits_violated_by`) and the consequence (`consequence_pursuits`). It is also the
    derivative of `decision/choose.py::score_terms`' pursuit term with respect to the weight on `e`,
    so moving `e` by `+lean` makes the verb score higher for its holder; that term computes the same
    dot at the holder's weights itself (its hot loop's `align` volume is profiled there), so the dot
    has a second copy by design. Reads `ALIGNMENT` and `PURSUIT_PROJECTION` at call time, through the
    modules a sweep rebinds."""
    proj = to_axes({e: 1.0})
    if row is None:
        return sum(proj[ax] * _verbs.align(verb, ax) for ax in PURSUIT_AXES)
    return sum(proj[ax] * row[ax] for ax in PURSUIT_AXES)


def consequence_pursuits(p: Person, verb: str, degree, gain: float):
    """v9 SC-02 `22b` step 24 -- `p`'s pursuits after HIS OWN act of `verb` resolved at `degree`, or
    `None` when nothing moves. A READER: it computes the new map and writes nothing; the act's effect
    writes it at RESOLVE (`loop/effects_information.py::_eff_determine`), so the write is the actor's own
    act and never a witness's (#353 §9.3: *moved by argument and consequence, never by evidence*).

    Each pursuit `p` already holds moves by `gain * DEGREE_STEP[degree] * pursuit_lean(verb, e)`:
    the ladder's own ordinal measured from the held band (`data/rosters.py::DEGREE_STEP`), so the top
    band moves twice as far as a success, a held matter (`Partial`) not at all, and a failure moves him
    AGAINST the way the act points. `gain` is the swept `Fixtures.pursuit_shift` (`H-221`; `0` the
    control). ONLY HELD KEYS MOVE: "held" is `_held`'s sense, a weight above zero (the scar's precedent),
    so a pursuit he does not hold -- absent, or at zero or below -- is neither minted nor moved by a
    consequence, and a man with no pursuits is unmoved. No clamp: a weight may cross zero, as an
    authored one may (`harness/probes.py` P31) [ASSUMPTION; medium; Jordan to correct; revert: floor at
    0]. Keys keep `p.pursuits`' order, which `to_axes` sums in. Person-side, no World (AX-2)."""
    step = DEGREE_STEP.get(degree, 0)
    held = {e: float(w) for e, w in (p.pursuits or {}).items()}
    if not gain or not step or not held:
        return None
    moved = {e: w + float(gain) * step * pursuit_lean(verb, e) if w > 0 else w for e, w in held.items()}
    return None if moved == held else moved


def argued_pursuits(hearer: Person, arguer: Person, degree, gain: float):
    """v9 IN-12 step 9 (#453 §9.4, `argue`) -- `hearer`'s pursuits after `arguer` WON an argument with him
    at `degree`, or `None` when nothing moves. A READER, `consequence_pursuits`' sibling: it computes the
    new map and writes nothing; `loop/effects_information.py::_eff_argue` writes it at RESOLVE, the arguer's
    act (#353 §9.3: *moved by argument and consequence, never by evidence*; AX-3).

    #453 leaves the direction a [GAP] (*'which weight moves, and toward what'*). The narrowest reading on the
    tree's own primitives [ASSUMPTION; medium; Jordan to correct; revert: Jordan names the direction]: each
    pursuit the hearer HOLDS moves TOWARD THE ARGUER'S OWN WEIGHT on it by `gain * DEGREE_STEP[degree]` of
    the gap -- the swept `Fixtures.pursuit_shift` (`H-221`) and the one degree ladder `consequence_pursuits`
    reads, so the field's two movers share one methodology. ONLY HELD KEYS MOVE (`consequence_pursuits`'
    rule: a weight above zero), so an argument mints no pursuit the hearer did not hold; a pursuit the
    arguer does not hold pulls toward 0. `Partial` (step 0) and below move nothing (the row writes `[]`
    there). Person-side, no World (AX-2)."""
    step = DEGREE_STEP.get(degree, 0)
    held = {e: float(w) for e, w in (hearer.pursuits or {}).items()}
    if not gain or step <= 0 or not held:
        return None
    pull = {e: float(w) for e, w in (arguer.pursuits or {}).items()}
    moved = {e: w + float(gain) * step * (pull.get(e, 0.0) - w) if w > 0 else w for e, w in held.items()}
    return None if moved == held else moved


def _affiliations_violated_by(verb: str) -> frozenset:
    """The rostered affiliations an act of `verb` violates, whoever holds them:
    `violated_affiliations`' sign test, `engagement(verb, a) < 0`. The candidates are
    `rosters.AFFILIATIONS`, the roster `data/affiliations.py::conviction_map` holds every
    `Person.conviction` key to."""
    return frozenset(a for a in AFFILIATIONS if engagement(verb, a) < 0)


def elements_violated_by(verb: str) -> tuple:
    """`(pursuits, affiliations)` an act of `verb` violates, as two frozensets -- the person-free
    half of `violated_pursuits` and `violated_affiliations`. Whether an element is violated is a
    property of `(verb, element)` alone, so `loop/resolve.py::_scar_witnesses` asks this once per
    act and intersects each person's holdings with it (`broken_by`) instead of re-deriving the sign
    test per person. Reads `ALIGNMENT` and `PURSUIT_PROJECTION` at call time: never cache it
    across a sweep's rebind."""
    return _pursuits_violated_by(verb), _affiliations_violated_by(verb)


def _held(weights, violated: frozenset) -> tuple:
    """The elements of `weights` held above zero and in `violated`, sorted by name."""
    weights = weights or {}
    return tuple(e for e in sorted(weights) if float(weights[e]) > 0 and e in violated)


def broken_by(p: Person, violated: tuple) -> tuple:
    """The elements `p` holds that `violated` (an `elements_violated_by` answer) names: the held
    pursuits, then the held affiliations, each sorted -- `violated_pursuits(p, verb) +
    violated_affiliations(p, verb)` without re-asking the sign test."""
    pursuits, affiliations = violated
    return _held(p.pursuits, pursuits) + _held(p.conviction, affiliations)


def confliction(p: Person) -> int:
    """HOW FAR `p`'s RELIGIOUS AFFILIATIONS STRAIN AGAINST EACH OTHER -- IN-08 H10, `12b`'s derived
    Query (ED-IN-0251 R1: *confliction is DERIVED from an `incompatible` relation and never stored*).

    `Σ over the incompatible pairs {a, b} of min(conviction[a], conviction[b])`: a pair strains as
    far as the WEAKER of its two holdings, so it is 0 unless both are held, and a person holding
    both at full intensity is in confliction at the ceiling. [ASSUMPTION; Jordan to correct] No source
    states the magnitude -- the draft gives only *"holding BOTH at high intensity"*; `min` is chosen
    because it stays an int on the intensity's own 0-5 spine (the alternative the draft names, a
    product of the two, leaves the scale). Composes on `data/affiliations.py::INCOMPATIBLE`, the one
    loaded relation. Person-side, no World (AX-2).

    Its caller is IN-08 6f: `decision/choose.py`'s `make_chooser` damps the pursuit dot by it, at
    the swept `confliction_weight` arm (H-188; control 0, shipped)."""
    held = p.conviction or {}
    return sum(min(held.get(a, 0), held.get(b, 0)) for a, b in _aff.INCOMPATIBLE)


# `ED-IN-0261`'s scar thresholds are 1 (destabilise), 2 (weight shifts, the others gain
# proportionally) and 3+ (crisis, terminal). IN-08 H9 reads THRESHOLD 2 ONLY: threshold 1 has no
# mechanism anywhere, and 3 is H13's (G-Q6, `conviction_after_crisis` below). Each count is the
# ruled threshold, not a swept value.
SCAR_WEIGHT_SHIFT_AT = 2  # [JUSTIFIED: the ruled threshold, not a swept value -- `ED-IN-0261` rules 2 as the weight shift; the fraction shifted is the swept `scar_weight_shift`]
SCAR_CRISIS_AT = 3  # [JUSTIFIED: the ruled threshold, not a swept value -- `ED-IN-0261` rules 3+ as the terminal crisis; the draft's G-Q6 gives the mechanism]


#: v9 IN-71 (H-188, Jordan 2026-09-27: *"faith as a pursuit is strongly modulated by religious
#: conviction"*): THE PURSUIT THE CONVICTION SCALES (`faith` is `doctrine`, RS-2) and THE CONCERNS
#: WHOSE MEMBERS ARE RELIGIOUS (`AFFILIATION_CONCERNS`, IN-64's key; `altonia` is civic, not a
#: theology, ED-IN-0293). Names of a pursuit and of two concerns -- each checked against its roster
#: below -- not figures: the intensity bound is the spine's own ceiling.
#: [ASSUMPTION; medium; Jordan to correct -- v9 IN-71, builder and dismantler alike; revert: the Church's
#: members only, or a swept gain rather than a straight scaling]. A person with NO `Person.conviction`
#: (the corpus builder `build_at`'s worlds) is read unscaled by `crisis_weights`, not as intensity 0.
DOCTRINE_PURSUIT = "doctrine"
RELIGIOUS_CONCERNS = ("church", "einhir")
if DOCTRINE_PURSUIT not in PURSUITS or not set(RELIGIOUS_CONCERNS) <= set(AFFILIATION_CONCERNS):
    raise ValueError(f"IN-71 names pursuit {DOCTRINE_PURSUIT!r} and concerns {RELIGIOUS_CONCERNS}; "
                     f"the rosters hold {sorted(PURSUITS)} and {sorted(AFFILIATION_CONCERNS)}")


def religious_intensity(p: Person) -> float:
    """`p`'s highest intensity on any member of a religious concern (`RELIGIOUS_CONCERNS`), as a
    fraction of the spine's ceiling: 0.0 for a person at 0 on every such member (IN-63: a stored 0
    is a rejection, not a gap) and 1.0 at full intensity. The builder and the dismantler alike --
    the MAX over both sides, never a sum or a signed difference. Person-side (AX-2)."""
    held = p.conviction or {}
    top = max((held.get(m, 0) for c in RELIGIOUS_CONCERNS for m in AFFILIATION_CONCERNS[c]), default=0)
    return top / AFFILIATION_CEILING


def crisis_weights(p: Person, shift: float = 0.0) -> dict:
    """`p`'s pursuit weights as the chooser should read them: the threshold-2 scar shift below, THEN
    `doctrine` scaled by religious conviction (v9 IN-71, H-188; the one site every reader projects).
    `choose`'s pursuit dot, `deeds_judged` and the telling weights all read this vector.

    `doctrine` is multiplied by `religious_intensity(p)` -- `w_doctrine * intensity * row_doctrine`
    once `to_axes` applies the row, MULTIPLICATIVELY and not as a second additive term. A weight of
    0, a person at full intensity, no `doctrine` key, or NO `conviction` AT ALL returns the shift's
    result itself; any other person reads a copy with that one weight scaled, `Person.pursuits`
    untouched. A person whose `conviction` is `{}` has no religious content recorded -- ABSENT IS NOT
    HELD, never 0 (IN-63) -- so his `doctrine` is read unscaled, as before IN-71 [ASSUMPTION; medium;
    Jordan to correct -- found at the v9 B-X close: as first built, `{}` read intensity 0 and ZEROED
    `doctrine` for every corpus (`build_at`) world, the very hazard H-188's `cite:` named; revert: scale
    a conviction-less person by 0]. A STORED 0 on every religious member is a held rejection and does
    zero it.
    """
    out = _scar_shifted(p, shift)
    w = out.get(DOCTRINE_PURSUIT)
    if not w or not p.conviction:
        return out
    k = religious_intensity(p)
    if k == 1.0:
        return out
    return {**out, DOCTRINE_PURSUIT: w * k}


def _scar_shifted(p: Person, shift: float) -> dict:
    """`p`'s pursuit weights as the chooser should read them once scars have reached threshold 2
    (IN-08 H9, `ED-IN-0261`: *"WEIGHT SHIFTS, others gain proportionally"*) -- A READER, it writes
    nothing and `Person.pursuits` is untouched.

    A held pursuit `e` with `p.scar[e] >= SCAR_WEIGHT_SHIFT_AT` gives up the fraction `shift` of
    its weight (downward: `conviction_track_v1.md` §2, reference for intent), and the mass given up
    is shared among the held pursuits that have NOT reached the threshold in proportion to their
    own weights, so a person's total weight is conserved. Where every held pursuit is at the
    threshold there is nobody to gain and the weights are returned unshifted rather than lose mass.
    `shift` is `Fixtures.scar_weight_shift`; `0` -- the shipped control -- returns `p.pursuits`
    itself, so the arm at its control is the unmodified read by construction.

    Person-side, no World (AX-2). Keys keep `p.pursuits`' own order, which `to_axes` sums in."""
    # `shift` is a FRACTION of a weight: past 1 a crisis pursuit's weight goes negative and the
    # heirs gain more than was given up. `not 0 <= shift <= 1` also refuses a NaN (cf. the
    # `confliction_weight` check in `decision/choose.py::make_chooser`).
    if not 0 <= shift <= 1:
        raise ValueError(f"scar_weight_shift {shift} is not in [0, 1]: it is the fraction of a "
                         f"weight given up, and outside that range a weight goes negative (H-187)")
    base = p.pursuits or {}
    if not shift or not p.scar:
        return base
    held = {e: float(w) for e, w in base.items() if float(w) > 0}
    # A LIST IN `held`'s ORDER, not a set: `given` sums over it, and a set's order is
    # PYTHONHASHSEED's, so the float sum would not be reproducible across processes.
    crisis = [e for e in held if p.scar.get(e, 0) >= SCAR_WEIGHT_SHIFT_AT]
    heirs = {e: w for e, w in held.items() if e not in crisis}
    if not crisis or not heirs:
        return base
    given = sum(held[e] * shift for e in crisis)
    pool = sum(heirs.values())
    out = dict(base)
    for e in crisis:
        out[e] = held[e] * (1.0 - shift)
    for e, w in heirs.items():
        out[e] = w + given * w / pool
    return out


def projected_axes(p: Person, shift: float = 0.0) -> dict:
    """`p`'s pursuits projected to the axes, `to_axes(crisis_weights(p, shift))`: person-side (AX-2)."""
    return to_axes(crisis_weights(p, shift))


def conviction_after_crisis(p: Person, among: frozenset | None = None) -> dict:
    """`p.conviction` as the crisis at scar threshold 3 leaves it -- IN-08 `12e` H13, G-Q6 as the
    affiliation draft recommends (folded into the build by Jordan's 2026-10-06 ruling, `ED-IN-0261`'s
    superseding row): THE ENGINE CHOOSES PER CASE, BY A RULE OVER STATE THE CRISIS ALREADY READS, AND
    ROLLS NOTHING (the crisis rewrites the vector, never an outcome). A READER: it returns a new
    vector and writes nothing; the write is `loop/resolve.py::_conviction_crisis`'s, by an act.

    A held affiliation is IN CRISIS when `p.scar` for it is `>= SCAR_CRISIS_AT`. ONE CRISIS AT A
    TIME: where several are, the one taken is the highest-held, ties to the first by name -- the
    design's own multi-crisis rule (`conviction_track_v1.md` §2 `:62`, quarantined, reference for
    intent: *"the most recent Scar event ... ties resolve to highest-weighted primary"*) with its
    first key dropped, because a count carries no time and one act scars every holding it violates
    at once [ASSUMPTION; Jordan to correct]. For that one, `x`, the first branch that applies:
      * FOLD -- `x` is co-held with an affiliation `y` it is `incompatible` with
        (`data/affiliations.py::INCOMPATIBLE`, the one loaded relation): `x`'s intensity transfers
        to `y` and `x` drops. With several such `y`, the highest-held takes it, ties to the first
        by name (the draft's *"highest-weighted other element"*; the name order is only the tie
        rule). The sum is clamped to the intensity's ceiling [ASSUMPTION: the spine is closed,
        `conviction_map` refuses past it].
      * RESTABILISE -- `x` is co-held with nothing it is incompatible with, and something else is
        held: the draft's branch is "the threshold-2 mechanism continuing". NOT BUILT -- the vector
        is left as it is. The threshold-2 mechanism is a reader over PURSUIT weights (H9's
        `crisis_weights`, a float fraction); `conviction` is an int on the 0-5 spine, so moving it
        by that fraction needs a rounding rule nobody has chosen.
      * DESTROYED -- nothing else is held: `x` drops, leaving the zero vector (no affiliation
        held, a real state).
    "Held" is an intensity ABOVE 0 (IN-63): `conviction_map` keeps an explicit 0, a considered
    rejection, so a present key is not a held one. A rejected pole is never in crisis, never an heir
    a fold lands on, and never counts as "something else is held" for the destroyed branch; a fold
    or a destruction leaves the other rejected poles as they were. [ASSUMPTION: the draft's "held
    above threshold" is read as held at all, i.e. above 0.]

    ⚠ UNDER THE SHARED COLUMN THE FOLD'S DIRECTION IS INTENSITY'S, NOT CONTENT'S. The draft gives
    the direction as *"which affiliation was scarred"*, but `affiliation_engagement`'s shared column
    (R-C4.1) violates every held creed alike, so co-held creeds accrue equal counts and reach the
    threshold in the same act; the selector above then folds the HIGHER-held creed into the lower.
    Only a per-affiliation cell (R-C4.2) scars one creed alone, and of those only `thread_read`'s
    exists, which writes nothing at RESOLVE. The heir keeps its own count, already at the
    threshold, so the heir's next scar ON THAT AFFILIATION breaks it.

    `among` is the set of elements the calling act has just scarred `p` on: only an affiliation in
    it can be in crisis, because a crisis follows THAT affiliation's count moving -- a person held
    at the threshold on one creed and scarred on a pursuit alone is not in crisis.
    `loop/resolve.py::_conviction_crisis` passes it; `None` (a direct caller) considers every held
    affiliation at the threshold.

    Re-evaluated at every count at or over the threshold, not only the one that reaches it: a
    folded or destroyed affiliation is no longer held, so it is never violated (hence never
    counted) again, and a restabilised one is left unwritten. CONVICTION TRACK ONLY: the pursuit
    track has no `incompatible` relation to fold along and `Person.pursuits` has no writer (H-62;
    its first is SC-02 `22b`). Person-side, no World (AX-2). With no held affiliation in crisis it
    returns `p.conviction` unchanged."""
    if not p.conviction:
        return p.conviction
    held = dict(p.conviction)
    scar = p.scar or {}
    # "Held" is above 0 (IN-63): a stored 0 is a rejection, which no count can crisis.
    crisis = [x for x in sorted(held) if held[x] > 0 and scar.get(x, 0) >= SCAR_CRISIS_AT
              and (among is None or x in among)]
    if not crisis:
        return p.conviction
    # `crisis` and `heirs` are in name order and `max` keeps the FIRST of equal keys, so a tie on
    # intensity goes to the lowest name.
    x = max(crisis, key=held.__getitem__)
    heirs = [y for y in sorted(held)
             if y != x and held[y] > 0 and frozenset((x, y)) in _aff.INCOMPATIBLE]
    if heirs:
        y = max(heirs, key=held.__getitem__)
        held[y] = min(AFFILIATION_CEILING, held[y] + held[x])
        del held[x]
    elif not any(v > 0 for k, v in held.items() if k != x):
        del held[x]
    else:                            # RESTABILISE -- not built (above)
        return p.conviction
    return conviction_map(held, where=f"{p.id}: conviction after crisis")


# ---------------------------------------------------------------------------
# `LedgerReader` -- MOVED HERE FROM `queries/readers.py` AT UNIT L3 (ED-IN-0206). It asks ONE
# PERSON'S OWN CLAIMS and nothing else: it takes neither a `World` nor even a `Person`, only the
# claims themselves, which is the asker-first family exactly and the `§A.2` table's *"may read a
# `PersonInterior` snapshot only"* row it now sits under.
#
# ⚠ THE TWO READERS ARE STILL THE SAME QUESTION ASKED OF TWO SOURCES, and splitting them by source
# is what makes that symmetry checkable instead of merely stated -- `test_person_q_cannot_reach_the
# _world_side` can now assert that this side cannot reach the other. The pointer note that stood
# between them in `readers.py` travels here because it is about what BOTH `.read` methods dispatch
# on, and this is the module a reader of the person-side half meets first:
# `REQUIRES_STEMS` and `LEDGER_DERIVED_STEMS` -- the stems `WorldReader.read`/`LedgerReader.read`
# dispatch on, above and below -- now live in `season.data.requires` (step 3), imported back at
# the top of this file. See that module for the two roster-exempt notes that used to stand here.
# ---------------------------------------------------------------------------


class LedgerReader:
    """THE SAME QUESTIONS ASKED OF ONE PERSON'S OWN CLAIMS, AND OF NOTHING ELSE.

    ⚠ IT TAKES CLAIMS, NOT A WORLD, AND NOT A PERSON. `#353 :634` permits `sense()` exactly one
    World among the non-decision functions, and §F1 clause 4 runs person-side; handing this a
    World would make `belief_contradicts` read the world, which is the filter §F1 spends two
    paragraphs forbidding (*"a filter on world truth would be `choose` reading the world"*).

    THE MOST RECENT, THEN THE MOST CONFIDENT. A ledger may hold two claims about one
    `(subject, predicate)` -- that is what a ledger IS -- and answering with the first found would
    make the verdict depend on append order. No matching claim is UNKNOWN, never False: §F1's
    asymmetry is that absence of a belief is not a belief in the negative.

    ⚠ `weigh` (telling workplan `T3a`, `ED-IN-0282`, `H-157`): HEARSAY IS GRADED WHEN READ, NEVER
    AT DEPOSIT. `weigh(c) -> [0, 1]` is how far this holder credits one claim; the caller builds it
    (`decision/options.py::teller_weight`) because this module may not import `decision/`. With
    a `weigh`, the comparator ranks a claim by `(support, when, confidence)`, where `support` is
    the noisy-OR over the DISTINCT ORIGINS asserting the same value (below). `None` is today's
    comparator, unchanged, and every caller but `epistemic.belief_contradicts` passes `None`.
    `confidence` is read RAW either way: weighing never rewrites a claim."""

    def __init__(self, claims, weigh=None):
        self._claims = list(claims or [])
        self._weigh = weigh

    def _support(self, matches) -> list:
        """`support(v) = 1 - PROD over distinct origins (1 - weigh(c))`, one entry per match, in
        match order. Grouped by `(predicate, value)` -- `read`'s matches share one predicate, so
        for `read` that is grouping by value. Under a `weigh`, `latest_about` therefore ranks
        ACROSS predicates by support, so a firsthand claim on any predicate outranks hearsay on
        another; no caller weighs `latest_about` today, and the position that weighs `said_of`
        (G3) decides it. An origin is `c.chain[0]` for a told claim and the holder for
        anything else; one origin counts once per value, at its highest
        weight, so a teller repeating himself adds nothing. Grouped by `==`, not by hash: a
        claim's `value` need not be hashable.

        ⚠ AT `weigh == 1` FOR EVERY CLAIM, EVERY GROUP'S SUPPORT IS EXACTLY `1.0` (`1 - 0.0`), so
        the key collapses to `(when, confidence)` -- today's order, by arithmetic rather than by a
        branch. `test_t3_weigh_none_and_weigh_one_order_a_ledger_as_today` checks it over
        randomised ledgers."""
        groups: list = []       # [key, {origin: weight}]
        idx: list = []
        for c in matches:
            key = (c.predicate, c.value)
            for i, g in enumerate(groups):
                if g[0] == key:
                    break
            else:
                groups.append([key, {}])
                i = len(groups) - 1
            origin = c.chain[0] if c.chain else c.holder
            wt = self._weigh(c)
            g = groups[i][1]
            g[origin] = max(g.get(origin, 0.0), wt)
            idx.append(i)
        support = []
        for _key, origins in groups:
            miss = 1.0
            for wt in origins.values():
                miss *= 1.0 - wt
            support.append(1.0 - miss)
        return [support[i] for i in idx]

    def _best(self, match):
        """THE COMPARATOR, ONCE. *Most recent, then most confident*, over whatever `match` admits
        -- and, under a `weigh`, *best supported* first (`_support`). Strict `>`, so the first
        found wins a tie, in both forms.

        ⚠ IT EXISTS BECAUSE THE DOCSTRING BELOW CLAIMED IT ALREADY DID. `latest_about` was added
        asserting it *"reuses `read`'s comparator rather than restating it"* while carrying its own
        copy of the identical loop -- a single-owner claim made in the act of breaking it, which is
        the anti-pattern `ci_common.load_yaml`'s own docstring records against itself
        (*"a single-owner comment asserting a property the tree lacks is worse than no comment"*).
        Extracting it makes the sentence true."""
        if self._weigh is None:
            best = None
            for c in self._claims:
                if match(c) and (best is None
                                 or (c.when, c.confidence) > (best.when, best.confidence)):
                    best = c
            return best
        matches = [c for c in self._claims if match(c)]
        best, best_key = None, None
        for c, s in zip(matches, self._support(matches)):
            key = (s, c.when, c.confidence)
            if best is None or key > best_key:
                best, best_key = c, key
        return best

    def read(self, subject, predicate: str):
        # `T4`: where another person is NOW is the world's to answer, never a ledger's
        # (`data/requires.py: WORLD_ONLY_STEMS`) -- UNKNOWN, so clause 4 never declines on it.
        if str(predicate).partition(":")[0] in WORLD_ONLY_STEMS:
            return UNKNOWN
        best = self._best(lambda c: c.subject == subject and c.predicate == predicate)
        return UNKNOWN if best is None else best.value

    def latest_about(self, subject):
        """THE ONE CLAIM THIS PERSON WOULD OFFER ABOUT `subject`, or `None` for no claim.

        ⚠ IT RETURNS THE CLAIM, NOT THE VALUE, AND THAT IS THE ONLY DIFFERENCE FROM `read`.
        A teller transmits a `(subject, predicate, value)` triple; `read` answers a value for a
        predicate the caller already knows, and a telling does not know one -- `tell`'s `requires`
        cell is *the teller holds a claim on the subject*, with no predicate in it.

        ⚠ AND IT REUSES `read`'s COMPARATOR RATHER THAN RESTATING IT -- through `_best`, which
        both methods now call. `CLAUDE.md` §8: the rule lives once. MOST RECENT, THEN MOST
        CONFIDENT is this class's answer to *a ledger may hold two claims about one thing*, and a
        second copy of that key anywhere would be a second owner of which belief a person holds --
        free to drift, and drifting silently, because both orderings agree until the day two
        claims tie on `when`."""
        return self._best(lambda c: c.subject == subject)

    def belief_among(self):
        """THE ONE CLAIM THIS READER WOULD ANSWER FROM, over every claim it holds -- `_best`'s
        comparator with no subject or predicate filter. For a caller that has already narrowed the
        ledger to one cell (`decision/options._pair`) and wants `read`'s ordering without reaching
        into a private name."""
        return self._best(lambda _c: True)


class OwnStateReader:
    """THE QUESTIONS A PERSON ANSWERS OF HIMSELF (v9 PC-06 K-3, `H-85`) -- `OWN_STATE_STEMS`, and
    nothing else: every other predicate is UNKNOWN here.

    ⚠ THE ONE ANSWERER OF BOTH STEMS, FOR BOTH SIDES. The fold's `queries/world_q.py::WorldReader`
    delegates to it for the person the act names, and `decision/options.py::opening_set` asks it of
    the person forming, so the gate and the person's own reading of it are one read, not two copies.
    It takes the PERSON and the fixtures and no World and no ledger: a person's sensitivity is his
    own state (`Person.thread_sensitivity`), not a belief about the world (§F1's asymmetry is about
    the world, as `opening_set`'s self-contest decline is about being alone in a room).

      * `thread_sensitivity` -- the subject's own value, and ONLY when the subject is this person: a
        person reads nobody else's. `None` (nothing authored) is UNKNOWN, never 0, so it refuses at
        the fold and does not pass a gate swept to 0.
      * `thread_sensitivity.gate` -- `Fixtures thread_sensitivity_gate`, the SECOND READ the value
        is held against (`work`'s `floor`, `determine`'s `quorum`), the same for every subject."""

    def __init__(self, p: Person, fx):
        self._p, self._fx = p, fx

    def read(self, subject, predicate: str):
        stem = str(predicate).partition(":")[0]
        if stem == "thread_sensitivity":
            v = self._p.thread_sensitivity if subject == self._p.id else None
            return UNKNOWN if v is None else v
        if stem == "thread_sensitivity.gate":
            return self._fx.get("thread_sensitivity_gate")
        return UNKNOWN


if OWN_STATE_STEMS != {"thread_sensitivity", "thread_sensitivity.gate"}:
    raise SystemExit(f"`data/requires.py: OWN_STATE_STEMS` is {sorted(OWN_STATE_STEMS)}, and "
                     "`OwnStateReader.read` answers only `thread_sensitivity` and its gate: a stem "
                     "added there with no branch here would read UNKNOWN for everybody")


SAID_SLANTS = roster("said_slants")


def _slant(fx) -> str:
    """`Fixtures.said_slant`, held to `rosters.yaml: said_slants` (`H-196`): an unknown arm raises
    rather than silently reading the control. `ValueError` for this module's reason
    (`_check_intent_claim`'s: the AX-2 allow-list)."""
    arm = fx.get("said_slant")
    if arm not in SAID_SLANTS:
        raise ValueError(f"said_slant {arm!r} is not in rosters.yaml: said_slants "
                         f"{sorted(SAID_SLANTS)} (H-196)")
    return arm


def said_of(claims, subject, fx, teller: "Person | None" = None) -> "Said | None":
    """WHAT THIS PERSON WOULD SAY ABOUT `subject`, as the `Said` a telling carries -- or `None` for
    nothing to say. Asked of the TELLER'S OWN claims at CHOOSE (`decision/options.py::opening_set`),
    never at WITNESS: what a telling passes on is decided when it is chosen, and rides the Act.

    ⚠ A `seen` CLAIM IS PASSED ON ONLY WHEN IT IS ALL THE TELLER HOLDS ABOUT THE SUBJECT (`R8.1`,
    moved here from `loop/witness.py::_told_content` unchanged). The `seen` deposit lands in every
    co-located witness -- the teller included -- with an identical value, so without this the
    teller's NEWEST claim about a rung was almost always a `seen` the hearer already held, the
    exact-triple guard at the told deposit suppressed it, and the told channel carried nothing:
    MEASURED at the `R8.1` commit, `build_world(0)`, four seasons, 0 `told_by` claims. A rumour of
    a sighting still travels when a sighting is all the teller has.

    ⚠ THE COMPARATOR IS `LedgerReader`'s, BOTH TIMES. *Most recent, then most confident* lives once
    (`_best`); only the pool differs.

    ⚠ SLANT (v9 IN-18 `G3`, `H-196`): at `Fixtures.said_slant == "valence"`, with the `teller`
    given, the pool is first narrowed to the claims the teller judges MOST STRONGLY -- the largest
    `|deed_valence|` by the teller's own projected pursuits -- and the comparator picks among those;
    where no claim carries valence (every one 0) the pick is the unslanted one exactly. A teller
    passes on the deed that matters most to THEM, not the newest thing they hold. At `newest` (the
    CONTROL, shipped), with no `teller`, or with no `fx`, it is the pre-G3 pick and reads no
    pursuits."""
    pool = [c for c in claims if c.subject == subject] if claims else []
    if teller is not None and fx is not None and pool and _slant(fx) == "valence":
        axis_w = projected_axes(teller, fx.get("scar_weight_shift"))
        strength = {id(c): abs(deed_valence(axis_w, c)) for c in pool}
        top = max(strength.values())
        if top > 0:
            pool = [c for c in pool if strength[id(c)] == top]
    reader = LedgerReader(pool)
    # ABSENT: H-198 deception  (an `absent` hole row, read by harness/register.py; nothing reads this marker)
    c = (reader._best(lambda c: c.subject == subject and c.predicate != SEEN_PREDICATE)
         or reader.latest_about(subject))
    if c is None:
        return None
    return Said(c.subject, c.predicate, c.value, c.confidence, c.chain)


def confided_outside(claims, said: "Said", hearer: str) -> bool:
    """v9 IN-18 `G6`: DOES A COPY OF `said` IN `claims` HOLD A CONFIDENCE CIRCLE `hearer` IS OUTSIDE?
    The copy is the claim with the said `(subject, predicate, value, chain)` -- the four fields
    `said_of` copies out of it above, so the match lives beside the copy it inverts. A circle is a
    tuple `Claim.visibility` (a confided telling's deposit, `loop/witness.py::_circle_of`); `"own"`
    is none. `claims` is the TELLER'S OWN ledger, passed by the fold (`loop/resolve.py::
    _confidence_broken`). Asker-less like its sibling `said_of`; `PersonInterior` does not exist;
    graded CONVENTION either way."""
    key = (said.subject, said.predicate, said.value, tuple(said.chain))
    return any(isinstance(c.visibility, tuple) and hearer not in c.visibility
               and (c.subject, c.predicate, c.value, c.chain) == key
               for c in claims)


# ---------------------------------------------------------------------------
# A DECLARED INTENT -- telling `T7` (G9; v9 IN-16, `ED-IN-0282`). The claim kind
# `rosters.yaml: intent_claim` declares: `(actor, <stem>:<verb>, ((name, id), ...))`, an act the actor
# has CHOSEN and not yet done. Minted at CHOOSE by `decision/choose.py::declare_intents` onto a
# telling's `said`, so the told deposit (`loop/witness.py`) lands it in each hearer's ledger with the
# teller as the chain; read back by `queries/world_q.py::named` (`intent_named`). Both halves of the
# value's shape live here, once.
# ---------------------------------------------------------------------------
INTENT_STEM = roster_map("intent_claim", "claim").get("predicate")
INTENT_NAMES = roster("intent_claim", ordered=True)


def _check_intent_claim(stem, names, requires_stems, requires_operands, taken) -> None:
    """Refuse, at import, an intent stem that another reader already answers, and a carried name
    that is no operand. A `requires` grammar stem would read the intent as a WORLD FACT
    (`WorldReader.read`) and make it a cell `record` pairs; the `seen` or `content:` predicate, or an
    emitted event kind, would give one predicate two meanings. `ValueError`, not `gaps.Unspecified`:
    this module may reach `data/`, the carriers and the trace sink only (the AX-2 allow-list)."""
    if not stem or ":" in str(stem):
        raise ValueError(f"rosters.yaml: intent_claim.claim.predicate is {stem!r}; it is a bare stem "
                         f"and the intended verb is its argument")
    if stem in requires_stems or stem in taken:
        raise ValueError(f"rosters.yaml: intent_claim.claim.predicate {stem!r} is already a "
                         f"predicate another reader answers; an intent is not a world fact or an event")
    bad = [n for n in names if n not in requires_operands]
    if bad:
        raise ValueError(f"rosters.yaml: intent_claim names {bad}, which are not `requires_operands` "
                         f"members; an intent carries the ids its act's operands bind")


_check_intent_claim(INTENT_STEM, INTENT_NAMES, REQUIRES_STEMS, REQUIRES_OPERANDS,
                    {SEEN_PREDICATE, RECORD_CONTENT.get("predicate")} | set(_verbs.EMITTED_KINDS))


def intent_said(actor: str, verb: str, operands, confidence: int) -> Said:
    """WHAT A TELLER SAYS WHEN THEY DECLARE AN INTENT: `actor` will do `verb`, on the ids `operands`
    binds under `INTENT_NAMES` (a non-string operand -- a list of addressees -- is not carried). A
    `Said` with an empty chain: the actor's own intent is no hearsay. Person-side; reads no ledger."""
    ops = operands if isinstance(operands, dict) else {}
    value = tuple((n, ops[n]) for n in INTENT_NAMES if isinstance(ops.get(n), str))
    return Said(actor, f"{INTENT_STEM}:{verb}", value, confidence, ())


def intent_named(c) -> tuple:
    """The ids a declared-intent claim (or `Said`) names -- `intent_said`'s value read back; `()` for
    any other predicate. `queries/world_q.py::named`'s intent branch."""
    stem, sep, _ = str(c.predicate).partition(":")
    if not sep or stem != INTENT_STEM or not isinstance(c.value, tuple):
        return ()
    return tuple(v for _n, v in c.value)


def content_said(c) -> "dict | None":
    """WHAT A HELD DOCUMENT'S CONTENT CLAIM SAYS: the value of a `content:<kind>` claim (or `Said`)
    as a key -> value dict (`rosters.yaml: record_kinds.content`), `None` for any other predicate or
    a claim with no value. `intent_named`'s shape for the other content-bearing stem: the one reader
    of that claim's shape that `ledger_names`, `world_q.named` and `decision/options.py::
    _from_content_claim` share (batch B-I close, layer-conformance: the three had each parsed it;
    `loop/witness.py`'s Partial-telling rewrite still guards it its own way, on a tuple value)."""
    stem, sep, _ = str(c.predicate).partition(":")
    if not sep or stem != RECORD_CONTENT.get("predicate") or c.value is None:
        return None
    return dict(c.value)


def content_kind(c) -> "str | None":
    """THE `<kind>` OF A `content:<kind>` CLAIM (`rosters.yaml: record_kinds.content.predicate`),
    `None` for any other predicate. `content_said`'s sibling: the one reader of the stem's argument
    (B-K close, ARC 2: `decision/options.py` had parsed it twice)."""
    stem, sep, kind = str(c.predicate).partition(":")
    if not sep or stem != RECORD_CONTENT.get("predicate"):
        return None
    return kind or None


#: THE CONTENT KEY THAT SAYS WHAT A DOCUMENT IS ABOUT, PER RECORD KIND -- the key `rosters.yaml:
#: record_sourced_operands` maps `subject` to for that kind (`terms` for a dispensation or petition,
#: `proposition` for a faction sheet). B-K close (ARC 5): the ONE owner of "what a document is
#: about", which `decision/options.py::_content_answer` reads for `subject` too; it was derived from
#: `record_kinds.content.read_from` and disagreed with it for `faction_sheet` (no `read_from` row).
ABOUT_KEYS = {kind: m["subject"] for kind, m in _requires.RECORD_SOURCED_OPERANDS.items()
              if "subject" in m}


def ledger_names(claims) -> frozenset:
    """EVERY ID THIS HOLDER HAS BEEN TOLD OF, from their OWN claims only (IN-10 (a), AX-2): the
    subject of every claim they hold -- a deposit, chiefly a witness's `tenure.opened` claim about a
    seat (#453 K-25) -- and what every document they hold is ABOUT (`ABOUT_KEYS[<kind>]` in a
    `content:<kind>` claim's value: a held writ's `terms`, a sheet's `proposition`). An addressee is not what a document is
    about, so a writ's `to` is not read. The ONE owner of "named by a held Record or a deposit":
    `world_q.seats_named` keeps the seats among it, and `decision/options.py::opening_set` asks it of
    a row declaring `referent_named` -- one rule for the source and the formation."""
    out = set()
    for c in claims:
        out.add(c.subject)
        said = content_said(c)
        if said is not None:
            v = said.get(ABOUT_KEYS.get(content_kind(c)))
            if isinstance(v, str):
                out.add(v)
    return frozenset(out)


def known_persons(claims, actor) -> tuple:
    """THE PERSONS THIS HOLDER KNOWS OF, from their OWN claims only -- sorted ids, never `actor`
    (telling workplan `T4`, `ED-IN-0282`). Three sources, and no other:

      * a truthy existence reading of a person -- `rosters.yaml: known_person_operands.claim.
        predicate`, deposited where a fold asked whether somebody exists;
      * who was SEEN doing something -- the `seen` claim's `seen_term` (`Seen.who`);
      * who TOLD them something -- a told claim's last teller, `chain[-1]`.

    A person is never known from the world: no presence read, no roster of acquaintances (`AX-2`).
    WHETHER the person is present to hear is the fold's question (`tell`'s `hearer` conjunct, the
    `with` stem), so a known person who has walked away is still named and the telling is refused
    -- and the person does NOT learn it from the refusal (`news.untold` is one kind for both
    conjuncts and the `with` read is never deposited, `witness.py`). The actor is excluded because a
    person does not tell themselves (`opening_set`'s counterparty rule declines it too).
    ⚠ THE TOPIC IS NOT EXCLUDED (v9 IN-18 step 2a, #453): a telling names its topic on `subject`
    and its hearer on `to`, and they MAY be one person -- B, knowing C and holding `(C, x)`, may tell
    C what B holds about C. Until step 2a the topic was discarded here, so that telling never formed.

    ⚠ `exists:Person` DEPOSITS ARE RARE AND `Seen.who` CARRIES THE LOAD: measured at T0 (scratch
    `t0/m0_summary.md`, M0d), every realm hit came from `seen`. The told source is empty until a
    told claim lands, which T4 itself is what makes possible."""
    predicate = KNOWN_PERSON_CLAIM.get("predicate")
    term = KNOWN_PERSON_CLAIM.get("seen_term")
    out = set()
    for c in claims or ():
        if c.predicate == predicate and c.value:
            out.add(c.subject)
        elif c.predicate == SEEN_PREDICATE:
            who = getattr(c.value, term, None)
            if who:
                out.add(who)
        if c.chain:
            out.add(c.chain[-1])
    out.discard(actor)
    out.discard(None)
    return tuple(sorted(out))
