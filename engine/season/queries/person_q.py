"""`queries/person_q.py` -- the ASKER-FIRST Query family, `04_CODE_ARCHITECTURE.md` §A.1's AX-2
row and §A.2's table.

> `queries/`  ownerless functions: world_q (World first) · **person_q (asker first)** · cache
>
> `queries/person_q` | owns **nothing** | may read **a `PersonInterior` snapshot only** | -- | --

⚠ **WHICH FUNCTIONS ARE HERE.** `budget` and `opening_set` are named BY `04:133` as `decision/`'s OWN
members -- *"`decision/` AX-2's island: questions · opening_set · choose · budget"* -- and `assemble` is
the `questions` member, same line. `entrenchment` is the one of the four `04` does not name, and it is
person-first in signature and self-declares as a person Query at its own first statement --
`TRACE.query("entrenchment", "person")`. It reads a `Person` and three ints and touches nothing else,
which is exactly the *"`PersonInterior` snapshot only"* the table allows. Nearly every function in
`world_q.py` takes `w: World` first; the helpers `named` and `_stamped` do not (04:116 splits the two
families by module, not by first parameter), and no check enforces the first-parameter rule: there is
no misfiled person-first Query in the world-side module, and the person-side scan below is what holds
the line.

⚠ **§A.3 ROW 2's PROPERTY IS THE POINT, NOT THE FILE COUNT.** *"one `Query` class holding both
families"* becomes *"two modules; the second cannot import the first"*, forced by T-f: *"in one
class, a person-side function calls a resolver-side one with no import to scan."* Splitting by
module makes that checkable: `test_person_q_cannot_reach_the_world_side` is the scan.

`decision/` MAY import this module (`04 §C.3`: *"`decision/` imports `person_q` and `data/`"*), and
does: `choose` and `options` read `stance_toward` and `said_of` from here. The AX-2 by-path scan
(`test_decision_package_never_names_world_anywhere_under_it`) is an allow-list: it forbids
`queries` from `decision/` and admits `queries.person_q` only; this module's own scan
(`test_person_q_cannot_reach_the_world_side`) still forbids `decision`, so the edge runs one way.
"""

from __future__ import annotations

import functools
import math
from typing import NamedTuple, Optional

from engine.dice_engine.dice_engine import DEGREE_LABEL, Degree
from engine.dice_engine.fmath import ltr_sum
from engine.substrate.descriptors import (
    AFFILIATION_CONCERNS, HERITAGE_ENGAGES, HERITAGES, PURSUITS,
)

from ..data import requires as _requires
from ..data import verbs as _verbs
from ..data import affiliations as _aff
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.affiliations import AFFILIATION_CEILING, AFFILIATION_FLOOR, conviction_map, engagement
from ..data.rosters import STANCE_MAX
from ..data.pursuits import _AXES, pursuit_cosine_axes, to_axes   # `_AXES`: the sorted axis order, owned once
from ..data.requires import (
    CELL_STEMS, KNOWN_PERSON_CLAIM, OWN_STATE_STEMS, Observation, REQUIRES_OPERANDS, REQUIRES_STEMS, SHORTFALL_PREDICATE,
    UNKNOWN, WORLD_ONLY_STEMS,
)
from ..data.rosters import (
    AFFILIATIONS, CRISIS_BANDS, DEGREE_STEP, DOMINANCE_KINDS, PERSON_DIED, PURSUIT_AXES, RECORD_CONTENT, REGARD_UNITS, SCAR_HOLDS, SEEN_PREDICATE, SELF_BELIEVED, capability_rows, require_use_site,
    roster, roster_map,
)
from ..state.carriers import Person, PersonInterior, Said
from ..state.ledgers import present_confidence
from ..trace_log import TRACE

# B14.16: THE OBSERVATION THAT NAMES THE HAND OF A FELLED ACTOR'S DEATH. `loop/effects_combat.py::hand_observed` puts
# `(actor, "fell_to_hand", <standing party>)` on the actor's `person.died` Event; WITNESS deposits it as an ordinary claim,
# and `deed_doer` reads it. The one spelling; the writer imports it from here.
HAND_PREDICATE = "fell_to_hand"


# THE READERS' CONTROL for `scar_hold` and `scar_primary_mass`, read off the one owner (`DEFAULT_FIXTURES`), never a literal here. A reader that holds the
# fixtures (`fx`, `w.fixtures`) passes its own; a hand-built read with none gets the control, as `scar_shift`'s `0.0` does.
_CONTROL_SCAR_HOLD = DEFAULT_FIXTURES.get("scar_hold")                 # [canonical: engine/season/data/fixtures.py §scar_hold (H-466)]
_CONTROL_SCAR_MASS = DEFAULT_FIXTURES.get("scar_primary_mass")         # [canonical: engine/season/data/fixtures.py §scar_primary_mass (H-469)]


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


def deeds_judged(p: Person, referent: str, scar_shift: float = 0.0, sworn_bond: float = 0.0, counterparty_arm: Optional[str] = None,
                 hold: str = _CONTROL_SCAR_HOLD, mass: float = _CONTROL_SCAR_MASS) -> tuple:
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
    THE SWORN-TO HALF IS BUILT, AT CONTROL (IN-58, B09.20; `sworn_bond`, H-459, shipped 0.0: "it ships OFF").
    A judge's own live, un-`imposed` `oblige` to a seat `S` is in `p.tenures` and outlives the victim, and
    the PAIRING that was missing -- a claim saying the victim sat in `S` -- is B09.22's: a seat closed by a
    death reaches the ledger of whoever WITNESS deposits it to (`observation_deposit_mode`) as `(S, hold,
    <the dead holder>)` (`state/gate.py::Subject.seat`), beside `(S, tenure.closed, True)` and `(victim,
    person.died, True)`. That claim is the pairing, never the two claims' shared `when` and `lap`, which this
    module does not read as one (`deed_doer`: it does not guess). `_bond` adds `sworn_bond` to the allegiance
    `a` for a patient the judge is so sworn to (`sworn_to_holder`), and only for the paired-deed term
    (`lean · bond`), so it scales a pursuit's lean and nothing else; a caller that holds `fx` passes
    `fx.get("sworn_bond")`, one holding none reads the control. At the shipped `actor` mode only the killer
    holds `(S, hold, victim)`, so the arm is reached by few judges until another mode or a telling carries the
    claim. FACTION-LEVEL grievance is v9 IN-70's: `opinion` here, its World half and its referents in
    `world_q` (`opinion_of`, `opinion_referents`).
    [ASSUMPTION, H-192: a deed's claim subject is read as its doer for every other kind; the sum is
    unnormalised.] Person-side, no World (AX-2).
    ⚠ v9 SC-02 `22a`: WHICH claims are `referent`'s deeds is `attributed_deeds`' and WHAT each is worth
    is `deed_term`'s; this function sums them by `firsthand`, and `world_q.reception` sums the same two
    by remove and confidence, so the two readers cannot disagree on either at the shipped `sworn_bond` 0.0
    (`deed_term` itself reads the control: `reception` and this sum part when it is non-zero).
    `counterparty_arm` is `Fixtures deed_counterparty` (B10.20, H-474; `None` is the control, `paired_only`): at `person_subject` a deed
    whose verb row takes a Person as its subject is weighed by the judge's bond to the one it was done to (`deed_term`)."""
    return _split_deeds(p, referent, scar_shift, sworn_bond, deed_term, counterparty_arm, hold, mass)


def _split_deeds(p: Person, referent: str, scar_shift: float, sworn_bond: float, worth, counterparty_arm: Optional[str] = None,
                 hold: str = _CONTROL_SCAR_HOLD, mass: float = _CONTROL_SCAR_MASS) -> tuple:
    """`(judged, told)` OF `attributed_deeds(p.ledger, referent)`, each claim worth `worth(p, axis_w, c, sworn_bond, counterparty_arm, seen_of)` and split by
    `firsthand`: the one walk `deeds_judged` (`worth` = `deed_term`, the raw sum) and `regard_steps` (`worth` = `deed_steps`, stance steps) share.
    `seen_of` is the holder's `_seen_index`, built once for the walk and only if a worth asks for it (B10.20)."""
    axis_w = None
    seen_of = functools.cache(lambda: _seen_index(p.ledger))
    judged = told = 0.0
    for c in attributed_deeds(p.ledger, referent):
        if axis_w is None:
            axis_w = projected_axes(p, scar_shift, hold=hold, mass=mass)
        v = worth(p, axis_w, c, sworn_bond, counterparty_arm, seen_of)
        # FIRSTHAND only is judged (`dissents`' and `record`'s precedent, `decision/options.py`):
        # a `told_by` claim whose chain is empty is still hearsay, and lands in `told`.
        if c.firsthand:
            judged += v
        else:
            told += v
    return judged, told


def deeds_judged_steps(p: Person, referent: str, scar_shift: float = 0.0, sworn_bond: float = 0.0, counterparty_arm: Optional[str] = None,
                       hold: str = _CONTROL_SCAR_HOLD, mass: float = _CONTROL_SCAR_MASS) -> tuple:
    """`deeds_judged`' `(judged, told)` IN STANCE STEPS (`deed_steps` for `deed_term`; B10.09, `Fixtures regard_unit` `stance`): the same
    claims, the same `firsthand` split, each deed worth a cosine. `regard`'s `stance` arm is the one reader; `deeds_judged` is unchanged."""
    return _split_deeds(p, referent, scar_shift, sworn_bond, deed_steps, counterparty_arm, hold, mass)


def holds_dispute(p: Person, referent: str, scar_shift: float = 0.0, sworn_bond: float = 0.0, counterparty_arm: Optional[str] = None,
                  hold: str = _CONTROL_SCAR_HOLD, mass: float = _CONTROL_SCAR_MASS) -> bool:
    """v11 CR-87 (the DISPUTE, `challenge`'s conjunct; `data/requires.py`'s `dispute` stem): DOES `p` HOLD A DEED CLAIM
    OF `referent`'s THAT HIS OWN JUDGEMENT SCORES AGAINST HIM -- `deeds_judged`' two parts summed below zero (what he
    saw and what he was told, each by his own pursuits). Person-side; the fold asks it of the actor's own ledger.
    CR-88 re-points the conjunct to `grievance_against`. [ASSUMPTION; medium; Jordan to correct; revert: drop the
    conjunct from `challenge`'s cell.] `counterparty_arm` is `Fixtures deed_counterparty`, passed as `regard` passes it, so the dispute and the regard weigh the
    same deeds by one rule (B10.20, H-474; `None` is the control)."""
    judged, told = deeds_judged(p, referent, scar_shift, sworn_bond, counterparty_arm, hold, mass)
    return judged + told < 0


def attributed_deeds(ledger, referent: str):
    """THE DEED CLAIMS IN `ledger` THAT RECORD AN ACT OF `referent`'s, in ledger order -- the one owner
    of *which of a holder's claims are about what this person did* (v9 SC-02 `22a`). An unpaired kind's claim is `referent`'s when its subject is
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


def deed_term(p: Person, axis_w: dict, c, sworn_bond: float = 0.0, counterparty_arm: Optional[str] = None, seen_of=None) -> float:
    """WHAT ONE OF `attributed_deeds`' CLAIMS IS WORTH TO `p`, whose projected pursuits are `axis_w`:
    a paired deed `lean · bond` (`_lean`, `_bond` on the claim's patient, IN-58), any other
    `deed_valence`. The same numbers `paired_deed_term` and `deed_valence` give; `deeds_judged` and
    `world_q.reception` both read it here. `sworn_bond` (B09.20, the control 0.0) is `deeds_judged`'s and reaches
    only a paired deed; `reception` and `legitimacy` read the control. Person-side (AX-2).
    `counterparty_arm` (B10.20, `Fixtures deed_counterparty`, H-474; `None` and `paired_only` are the control: the branch is today's, byte for
    byte) at `person_subject` multiplies an unpaired deed whose verb row takes a Person as its subject (`PERSON_SUBJECT_KINDS`) by
    `_bond(p, <the one it was done to>, lean)`, the factor a paired deed already carries (`_toward_counterparty`); a deed whose counterparty
    `p`'s ledger does not name reads `deed_valence` alone. `reception` and `legitimacy` read the control, as they do `sworn_bond`.
    `seen_of` is a zero-argument callable answering `_seen_index(p.ledger)`, called only where a counterparty is read."""
    if c.predicate in PAIRED_KINDS:
        lean = _lean(axis_w, c.predicate)
        return _paired_weight(p, c, lean, sworn_bond) if lean else 0.0
    lean = deed_valence(axis_w, c)
    return lean * _toward_counterparty(p, c, lean, counterparty_arm, seen_of) if lean else lean


def deed_steps(p: Person, axis_w: dict, c, sworn_bond: float = 0.0, counterparty_arm: Optional[str] = None, seen_of=None) -> float:
    """WHAT ONE OF `attributed_deeds`' CLAIMS IS WORTH TO `p` IN STANCE STEPS (B10.09, `Fixtures regard_unit` `stance`): `deed_term`'s
    sibling, the deed's alignment as a cosine -- `pursuit_cosine_axes` of the holder's projected pursuits `axis_w` against the deed
    kind's row on the axes (`align_kind`), in `[-1, +1]` -- so an unpaired deed is at most one valence step, the unit of a stance
    row. A paired deed (`PAIRED_KINDS`) is that cosine times `_bond` on the claim's patient (in `[0, 2]`, so at most two steps),
    read off the cosine's sign as `deed_term` reads `lean`'s. `0.0` where either vector is zero (`pursuit_cosine_axes` answers
    `None`: no direction to compare), and for a claim that is no deed. `sworn_bond`, `counterparty_arm` and `seen_of` are `deed_term`'s: at
    `person_subject` an unpaired deed of a Person-subject kind is that cosine times `_bond` on the one it was done to. Person-side (AX-2)."""
    if not is_deed(c):
        return 0.0
    cos = pursuit_cosine_axes(axis_w, {ax: _verbs.align_kind(c.predicate, ax) for ax in _AXES})
    if not cos:
        return 0.0
    if c.predicate in PAIRED_KINDS:
        return cos * _bond(p, c.subject, cos, sworn_bond)
    return cos * _toward_counterparty(p, c, cos, counterparty_arm, seen_of)


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


def attackers_of(ledger, patient: str, kinds: frozenset, window: int = 1, strata=None) -> frozenset:
    """WHO THE HOLDER SAW DO A DEED OF ONE OF `kinds` TO `patient` IN THE NEWEST `window` SEASONS HIS LEDGER
    HOLDS (v11 CR-87, the DEFENCE context of `rosters.yaml: violence_contexts`): the doers `deed_doer` pairs to
    `suffered_deeds`' claims, kept when the claim is among `recent_claims(ledger, window)` (anchored on his newest
    claim, so `window == 1` is "this season" as he knows it) and its kind is in `kinds` (the caller's: the kinds an
    opponent-rule row emits). Person-side (AX-2); what he was only told of names nobody, as in `suffered_deeds`.

    `strata`, where given, keeps a doer only if the holder saw him act at one of them ON THIS DEED'S SUBJECT in that deed's lap. A kind several rows emit
    (`capability.raised`: `fight` and `train`) pairs on any of its emitters' strata, so a benefit and a blow carry the same kind;
    the caller that asks for ATTACKERS passes the strata of its violent rows. B05.09 made `train` reach people who held no rank,
    and `p_npc_004`'s training of `p_npc_038` read as an attack."""
    if not kinds:
        return frozenset()
    recent = {id(c) for c in recent_claims(ledger, window)}
    seen, out = None, set()
    for c in suffered_deeds(ledger, patient):
        if id(c) in recent and c.predicate in kinds:
            seen = _seen_index(ledger) if seen is None else seen      # built only when a claim qualifies
            d = deed_doer(c, seen)
            if d is not None and (strata is None or any(getattr(x.value, "who", None) == d and getattr(x.value, "stratum", None) in strata
                                                         for x in seen[0].get((c.subject, c.when, c.lap), ()))):
                out.add(d)
    return frozenset(out)


# v9 IN-58: THE DEED KINDS JUDGED ONLY THROUGH THE `seen.who` PAIRING -- every DEED kind no single
# row emits (`KIND_VERB` names no verb for it), read off the table, no kind listed. Such a kind's
# claim subject may be the doer OR the patient (`both`), and no verb says which, so its valence
# (an authored `deed:<kind>` cell, `align_kind`) enters for the doer a `seen` claim names.
PAIRED_KINDS = frozenset(k for k in _verbs.DEED_KINDS if k not in _verbs.KIND_VERB)
# The strata of the rows that emit each paired kind: a `seen` claim pairs with a deed of that kind
# only if what the witness saw was an act of one of them (`Seen.stratum`). Every channel showing
# `who` shows `stratum` (`rosters.yaml: observation_terms.supplied_by`), so the test never drops a
# pairing that `who` alone would have made; it refuses a third party's DIFFERENT act on the patient in
# the same lap being read as the deed's doer.
# B10.20 (H-474): THE UNPAIRED DEED KINDS WHOSE VERB ROW TAKES A PERSON AS ITS SUBJECT -- the kinds the single row emitting them
# (`KIND_VERB`) declares `referent_class: Person`, read off the table, no verb listed. The one acted on is the row's subject, and the claim
# (subject = its doer, H-192) names no one else, so `deed_counterparty` reads him off the holder's `seen` claims.
_PERSON_CLASS = "Person"      # [canonical: engine/season/rosters.yaml §referent_classes]
PERSON_SUBJECT_KINDS = frozenset(k for k in _verbs.DEED_KINDS
                                 if k in _verbs.KIND_VERB and _verbs.VERB_TABLE[_verbs.KIND_VERB[k]].referent_class == _PERSON_CLASS)
# `Fixtures deed_counterparty`'s arms (`rosters.yaml: deed_counterparties`), checked where `regard` reads the fixture.
DEED_COUNTERPARTIES = roster("deed_counterparties")
_KIND_STRATA = {k: frozenset(r.stratum for r in _verbs.VERB_TABLE.values() if k in r.emits)
                for k in PAIRED_KINDS | PERSON_SUBJECT_KINDS}


def _seen_index(ledger) -> tuple:
    """A holder's own, untold claims, indexed four times: `(subject, when, lap) -> [seen]` and
    `(when, lap) -> {(who, stratum)}` -- who the holder saw acting, and at what, in each lap -- and
    `(subject, when, lap) -> {value}` for a `fell_to_hand` claim (B14.16: who stood when `subject`, the actor, fell), and
    `(who, when, lap) -> {(subject, stratum)}` -- what the holder saw each actor act on, the inverse of the first (B10.20: `deed_counterparty`)."""
    by_subject: dict = {}
    acting: dict = {}
    hand: dict = {}
    acted_on: dict = {}
    for s in ledger:
        if s.predicate == HAND_PREDICATE and not s.chain:
            hand.setdefault((s.subject, s.when, s.lap), set()).add(s.value)
        elif s.predicate == SEEN_PREDICATE and not s.chain:
            by_subject.setdefault((s.subject, s.when, s.lap), []).append(s)
            who = getattr(s.value, "who", None)
            if who is not None:
                acting.setdefault((s.when, s.lap), set()).add((who, getattr(s.value, "stratum", None)))
                acted_on.setdefault((who, s.when, s.lap), set()).add((s.subject, getattr(s.value, "stratum", None)))
    return by_subject, acting, hand, acted_on


def deed_doer(c, seen: tuple):
    """v9 IN-58's PAIRING RULE: WHO DID THE DEED `c` TO ITS SUBJECT, as the holder saw it, or `None`.

    `c` is an untold deed claim `(s, kind, True)` of a `PAIRED_KINDS` kind; `seen` is
    `_seen_index` of the same ledger. A `seen` claim PAIRS with it when it has the same subject
    `s`, `when` and `lap` (WITNESS deposits both from one Event in one pass), names a `who`, that
    `who` is not `s` (a deed done TO `s` -- `s`'s own act in the same lap is not it), and its
    `stratum` is the stratum of a row emitting `kind`. The doer is the ONE `who` the pairing
    names; none, or two different, is `None` -- the pairing never guesses, so a channel that
    withheld `who` leaves the actor hidden.
    ⚠ AND `s` MUST NOT HAVE BEEN SEEN DOING SUCH AN ACT IN THAT LAP: then `c` may be the claim
    `both` anchors on the ACTOR (`(x, person.died)` for x's kill), and a third party's sighting on
    `s` would name the wrong doer of the wrong death. The price, stated: a person who both struck and was struck in one
    lap is judged a patient by nobody that lap.
    THE ACTOR WHO DIED ATTACKING (B14.16; was this note's LIMIT, stated): the sighting names him as `who` of his
    own death, so the pairing below names no killer. A `person.died` claim is therefore read FIRST against the
    holder's own `fell_to_hand` claim on the same subject, `when` and `lap` (`HAND_PREDICATE`, deposited from the
    felled actor's death Event by `loop/effects_combat.py::hand_observed`), and that value is the answer; the
    pairing stands for every other case. CLOSED: for a holder who holds that claim, the standing party is named.
    NOT CLOSED: a holder who does not hold it -- WITNESS deposits an Event's `observed` under
    `observation_deposit_mode`, and the shipped `actor` deposits to the act's actor alone, a felled actor being
    no longer a person to receive it, so under the shipped mode no ledger holds it and the limit stands in
    every ledger; a fight with no standing party (both felled, a yield) carries none; a told copy has none.
    Two different names held for one death are ambiguous, so `None`.
    A `seen` on the same subject, `when` and `lap` that names NO `who` (a
    channel that withheld the actor) makes the pairing ambiguous, so `None`: an unnamed hand may be
    the one that did it. Holder-side and World-free: `Seen` is read by its fields, never imported
    (AX-2)."""
    if c.chain or not is_deed(c) or c.predicate not in PAIRED_KINDS:
        return None
    by_subject, acting, hand, _ = seen
    if c.predicate == PERSON_DIED and (c.subject, c.when, c.lap) in hand:
        named = hand[(c.subject, c.when, c.lap)]
        return next(iter(named)) if len(named) == 1 else None
    strata = _KIND_STRATA[c.predicate]
    if any(who == c.subject and st in strata for who, st in acting.get((c.when, c.lap), ())):
        return None
    whos = set()
    for s in by_subject.get((c.subject, c.when, c.lap), ()):
        who = getattr(s.value, "who", None)
        if who is None:
            return None             # an actorless sighting on the same key: ambiguous, never guess
        if who == c.subject or getattr(s.value, "stratum", None) not in strata:
            continue
        whos.add(who)
    return next(iter(whos)) if len(whos) == 1 else None


def deed_counterparty(c, seen: tuple):
    """WHO THE DOER OF THE DEED `c` ACTED ON, as the holder saw it, or `None` (B10.20; `deed_doer`'s inverse).

    `c` is an untold deed claim `(doer, kind, True)` of a `PERSON_SUBJECT_KINDS` kind (an unpaired kind: its claim's subject is its doer, H-192,
    so the claim names no one else); `seen` is `_seen_index` of the same ledger. A `seen` claim names the counterparty when it was deposited in the
    claim's own `when` and `lap`, its `who` is the doer and its `stratum` is the kind's row's (`_KIND_STRATA`): its subject is what the doer was seen
    to act on. The ONE such subject is the answer; none, or two, is `None` -- the pairing never guesses, as `deed_doer` does not, so a channel
    that withheld `who`, a told copy (it carries no sighting) and an act seen on two things name nobody. The subject is not checked to be a person
    (a person-side reader holds no World): a rung or a Record names nobody the judge holds a stance toward, so `_bond` reads it as no stance.
    Holder-side and World-free (AX-2)."""
    if c.chain or not is_deed(c) or c.predicate not in PERSON_SUBJECT_KINDS:
        return None
    strata = _KIND_STRATA[c.predicate]
    named = {s for s, st in seen[3].get((c.subject, c.when, c.lap), ()) if s != c.subject and st in strata}
    return next(iter(named)) if len(named) == 1 else None


def _toward_counterparty(p: Person, c, lean: float, counterparty_arm: Optional[str], seen_of=None) -> float:
    """THE FACTOR AN UNPAIRED DEED OF A PERSON-SUBJECT KIND CARRIES FOR WHO IT WAS DONE TO (B10.20, `Fixtures deed_counterparty`): `_bond(p,
    <the counterparty>, lean)`, the one factor a paired deed carries (`_paired_weight`), at `person_subject`; `1.0` everywhere else -- at the control
    (`None`, `paired_only`), for a kind no Person-subject row emits, and for a deed whose counterparty `p`'s ledger does not name. `seen_of` answers
    `_seen_index(p.ledger)`; omitted, it is built here."""
    if counterparty_arm != "person_subject" or c.predicate not in PERSON_SUBJECT_KINDS:
        return 1.0
    who = deed_counterparty(c, seen_of() if seen_of is not None else _seen_index(p.ledger))
    return 1.0 if who is None else _bond(p, who, lean)


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


def _paired_weight(p: Person, c, lean: float, sworn_bond: float = 0.0) -> float:
    """A paired deed's term, `lean · bond` on the claim's patient: the one formula `deed_term` and
    `paired_deed_term` share (`CLAUDE.md` §8, the rule lives once)."""
    return lean * _bond(p, c.subject, lean, sworn_bond)


def sworn_to_holder(p: Person, patient: str) -> bool:
    """IS `p` SWORN TO THE SEAT `patient` HELD (B09.20, IN-58's sworn-to half): does `p` hold a live, un-`imposed`
    `oblige` Tenure whose object is a seat `S`, AND hold the claim `(S, hold, patient)` that B09.22's seat writes when
    a death closes the hold (`state/gate.py::Subject.seat`)? The CLAIM is the pairing: a `tenure.closed` claim on `S`
    and a `person.died` claim on `patient` that merely share a `when` and `lap` pair nothing (`deed_doer` does not
    guess), and an oath `p` does not hold a claim for names no victim. An `imposed` oblige is a sentence, not an
    oath (`Tenure.imposed`). Person-side, `p.tenures` and `p.ledger` only (AX-2)."""
    seats = {t.object for t in p.tenures if t.kind == "oblige" and t.live and not t.imposed}
    return bool(seats) and any(c.predicate == "hold" and c.value == patient and c.subject in seats
                               for c in p.ledger)


def _bond(p: Person, counterparty: str, lean: float, sworn_bond: float = 0.0) -> float:
    """v9 IN-58's FACTOR: how `p`'s allegiance to the deed's COUNTERPARTY (the one it was done to: a paired deed's patient, or at `deed_counterparty: person_subject` the Person an unpaired deed's row takes as subject) weighs the deed,
    `1 - a · sign(lean)`, `a = clamp(stance_toward(p, counterparty) / STANCE_MAX, -1, 1)` -- the stored
    half only, normalised as `teller_weight` normalises regard. In `[0, 2]`, and the deed term
    `lean · _bond` FALLS as `a` rises whatever the pursuits' sign: full allegiance doubles a
    condemnation and cancels an approval; full enmity doubles an approval and cancels a
    condemnation; no stance (`a = 0`) judges the deed by pursuits alone. The judge who IS the
    counterparty is his own full ally (`a = 1`): no stance row names oneself, and reading it would judge
    his own attacker as a stranger's. [ASSUMPTION; medium;
    Jordan to correct -- the form of the factor; revert: no factor and the two cells unauthored.]
    THE SWORN-TO ARM (B09.20, `sworn_bond`, H-459): for a judge `sworn_to_holder` of the counterparty, `sworn_bond` is
    ADDED to `a` before the clamp, so an oath binds on the stance's own scale and a full stance plus an oath is
    still `a = 1`. `0.0` (the control, and every caller holding no `fx`) reads no ledger and no tenure: the stored
    half exactly."""
    if counterparty == p.id:
        a = 1.0
    else:
        a = stance_toward(p, counterparty) / STANCE_MAX
        if sworn_bond and sworn_to_holder(p, counterparty):
            a += sworn_bond
        a = max(-1.0, min(1.0, a))
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
    return ltr_sum(axis_w[ax] * _verbs.align_kind(kind, ax) for ax in _AXES)


class RegardParts(NamedTuple):
    """THE FOUR ADDENDS OF `regard`, in its addition order: `stored` (his own stance rows), `judged` and `told` (`deeds_judged`'s two halves, each
    at its own gain) and `heritage` (the caste estimate). `regard` is their sum, `((stored + judged) + told) + heritage`, and nothing else."""
    stored: float
    judged: float
    told: float
    heritage: float


def regard_parts(p: Person, referent: str, fx=None) -> RegardParts:
    """THE ADDENDS OF `regard`, which is their sum (`regard`'s docstring has the formula and the controls; this is its one owner, `CLAUDE.md` §8).
    With no `fx`, or with the gains at 0, the `judged` and `told` addends are `0.0` and no ledger is read; a `heritage_gain` of 0 makes `heritage`
    `0.0` and reads none."""
    stored = stance_toward(p, referent)
    if fx is None:
        return RegardParts(stored, 0.0, 0.0, 0.0)
    jg = float(fx.get("judged_gain"))
    tg = float(fx.get("told_valence_gain"))
    if not (jg >= 0 and tg >= 0):
        raise ValueError(f"judged_gain {jg} / told_valence_gain {tg} must be >= 0 (H-192/H-193)")
    judged = told = 0.0
    if jg or tg:
        unit = fx.get("regard_unit")
        if unit not in REGARD_UNITS:
            raise ValueError(f"regard_unit {unit!r} is not in rosters.yaml: regard_units {sorted(REGARD_UNITS)} (H-470)")
        arm = fx.get("deed_counterparty")
        if arm not in DEED_COUNTERPARTIES:
            raise ValueError(f"deed_counterparty {arm!r} is not in rosters.yaml: deed_counterparties {sorted(DEED_COUNTERPARTIES)} (H-474)")
        raw_judged, raw_told = (deeds_judged_steps if unit == "stance" else deeds_judged)(
            p, referent, fx.get("scar_weight_shift"), fx.get("sworn_bond"), arm, fx.get("scar_hold"), fx.get("scar_primary_mass"))
        judged, told = jg * raw_judged, tg * raw_told
    # v11 CR-31: the caste estimate, `heritage_regard`, a third term at its own gain (0 reads nothing: the control). It reads `p`'s own ledger and
    # own convictions only.
    return RegardParts(stored, judged, told, heritage_regard(p, referent, fx))


def regard(p: Person, referent: str, fx=None) -> float:
    """HOW `p` REGARDS `referent`, computed when read and never written (telling workplan §1's
    spine):

        regard = stance_toward(p, x) + judged_gain · judged + told_valence_gain · told
                 + heritage_regard(p, x)

    the stored half (`stance_toward`, the person's own stance rows) plus `deeds_judged`'s two
    halves (v9 IN-18 `G1`) plus the caste estimate (v11 CR-31, `heritage_regard`, at `heritage_gain`).
    With no `fx`, or with all three gains 0 -- the CONTROL (the first two ship live at 0.5,
    `H-192`/`H-193`) -- it is the stored half exactly and reads no ledger. ⚠ `judged_gain` IS NOT
    `regard_gain`: the shape row spells `regard_gain · judged`, but `regard_gain` is `teller_weight`'s
    relation gain (`H-179`, shipped 0.5), and zeroing it for G1's control would move every told
    claim's weight -- two decisions on one fixture, `H-121`'s defect. A second name for one sum is
    deliberate: `decision/options.py::teller_weight` asks for REGARD, so when the gains move, the
    reader does not.
    THE SUM OF `regard_parts`, left to right (B10.55): the four addends live there once, so the split a player's surface or the chronicle reads
    cannot disagree with the number a choice scores."""
    stored, judged, told, h = regard_parts(p, referent, fx)
    total = stored + judged + told
    return total + h if h else total


# B10.55: THE CLAIMS A PERSON HOLDS OF A PERSON'S BOND TO HIM, `Claim(subject=<that person>, predicate=BOND_STEM + <ground>, value=True)`: his own
# knowledge of what the other is to him. B10.62's `boot/realm.py::seed_relations` deposits one for each authored relation (the rows `cast.relations_of` reads author one, so `room_as_held`'s `bond` reads nonzero on those holders).
BOND_STEM = "bond:"


def room_as_held(p: PersonInterior, event_id: str, fx, deposited=()) -> tuple:
    """THE ROOM `p` BELIEVES HE STOOD IN WHEN HE ACTED (B10.55): for each person `p`'s OWN ledger names as present at the Event `event_id`, `(id,
    {"told", "seen", "bond"})`, sorted by id -- counts of what `p` holds of him, never what he holds of `p` (that is `chronicle.witness_regard`, the
    chronicle's, which no decision or surface reads). Person-side, asker first, no World (AX-2): nothing about anyone else's ledger.

    `deposited` is the ids of the claims deposited from `event_id`, the host's `queries/cache.py::deposit_index` answer (ids only, holder-blind):
    the person-side reader holds no log, and a `Claim` carries no Event, so `p` is asked which of those he holds, as `epistemic._antecedent_claim` asks
    it. The ones he holds are his anchors (his own `when` and `lap`), and he names no one while he holds none. A person is NAMED by:

      * `seen`: his own untold `seen` claims, in an anchor's `when` and `lap`, whose `who` is that person (whom he saw acting there);
      * `told`: his claims of the SAME subject and predicate as an anchor, deposited from then on, whose teller (`Claim.teller`) is that person.

    `bond` is the count of `bond:<ground>` claims `p` holds of a person so named (`BOND_STEM`); it names no one by itself, since a bond is not a
    presence. `fx` is the entry's signature and is read by nothing here (`CLAUDE.md` §8: no second copy of any gain)."""
    ids = frozenset(deposited)
    anchors = [c for c in p.ledger if c.id in ids]
    if not anchors:
        return ()
    spots = {(c.when, c.lap) for c in anchors}
    since: dict = {}
    for a in anchors:
        key = (a.subject, a.predicate)
        since[key] = min(a.when, since.get(key, a.when))
    seen: dict = {}
    told: dict = {}
    for c in p.ledger:
        who = getattr(c.value, "who", None)
        if c.predicate == SEEN_PREDICATE and not c.chain and who is not None and who != p.id and (c.when, c.lap) in spots:
            seen[who] = seen.get(who, 0) + 1
        elif c.chain and c.teller != p.id and (c.subject, c.predicate) in since and c.when >= since[(c.subject, c.predicate)]:
            told[c.teller] = told.get(c.teller, 0) + 1
    return tuple((x, {"told": told.get(x, 0), "seen": seen.get(x, 0),
                      "bond": sum(1 for c in p.ledger if c.subject == x and c.predicate.startswith(BOND_STEM) and c.value is True)})
                 for x in sorted(seen.keys() | told.keys()))


# The claim a person holds about another's skill: `Claim(subject=<that person>, predicate=CAPABILITY_CLAIM + <the skill>,
# value=<the score he believes>)`. NOTHING DEPOSITS ONE TODAY (the told, seen and inferred channels carry no capability),
# so `believed_capability` answers `None` for every person in a built realm until a depositor exists: this is the reading,
# not the writer. Its two readers -- `seam/wrappers/sigma.py::believed_input` (the opposition of a contest) and
# `decision/choose.py::score_terms`' `fit` term (B04.22) -- both call the one function below.
CAPABILITY_CLAIM = "capability:"


def believed_capability(p: Person, other: str, capability: str, tick: int = 0, decay: int = 0):
    """WHAT `p` BELIEVES `other`'s SCORE IN `capability` IS, from his OWN ledger alone: the value of his latest claim
    about `other` at `CAPABILITY_CLAIM + capability` (latest by `(when, lap, confidence)`), else `None` -- unknown, never a
    figure. Person-side (AX-2): it reads `p`'s ledger and nothing else. `tick` and `decay` are the reader's (`LedgerReader`'s):
    two claims of one `(when, lap)` are ranked by the confidence each is held at now."""
    return _latest_claim(p, other, CAPABILITY_CLAIM + capability, tick, decay)


# B14.24: THE CLAIMS A PERSON HOLDS ABOUT ANOTHER'S ARMS AND WOUNDS, the capability claim's own shape (`Claim(subject=<that person>,
# predicate=<stem> + <key>, value=<what he believes>)`) and, like it, a READING: NOTHING DEPOSITS ONE TODAY (the told, seen and inferred
# channels carry neither), so `believed_kit` and `believed_body` answer `None` for every person in a built realm until a depositor exists.
# `KIT_CLAIM + <a Combatant field>` (`weapon`, `armor`; `engine/substrate/combat_kit.py::FIELDS`) holds the key he believes the person carries
# in that field; `BODY_CLAIM` holds the condition (the `Person.body` scale) he believes the person is at. Both readers are `believed_capability`'s.
KIT_CLAIM = "kit:"
BODY_CLAIM = "condition:body"


def _latest_claim(p: Person, other: str, predicate: str, tick: int = 0, decay: int = 0):
    """The value of `p`'s latest claim about `other` at `predicate` (latest by `(when, lap, present confidence)`), else `None`; `p`'s ledger alone."""
    held = [c for c in p.ledger if c.subject == other and c.predicate == predicate]
    return max(held, key=lambda c: (c.when, c.lap, present_confidence(c.confidence, c.when, tick, decay))).value if held else None


def believed_kit(p: Person, other: str, field: str, tick: int = 0, decay: int = 0):
    """The key `p` believes `other` carries in the Combatant `field` (`weapon` or `armor`), from his OWN ledger alone: the value of his latest claim
    at `KIT_CLAIM + field`, else `None` -- unknown, never a figure. Person-side (AX-2)."""
    return _latest_claim(p, other, KIT_CLAIM + field, tick, decay)


def believed_body(p: Person, other: str, tick: int = 0, decay: int = 0):
    """The condition `p` believes `other`'s body is at, from his OWN ledger alone: the value of his latest `BODY_CLAIM` about `other`, else `None`.
    Person-side (AX-2)."""
    return _latest_claim(p, other, BODY_CLAIM, tick, decay)


def has_seen(p: Person, other: str) -> bool:
    """Has `p` SEEN `other`: does his ledger hold an untold `seen` claim whose `who` is `other` (`heritage_regard` reads the same deposit)? The
    reading of a person he has laid eyes on; a person known only by report or not at all is not seen. Person-side (AX-2)."""
    return any(c.predicate == SEEN_PREDICATE and not c.chain and getattr(c.value, "who", None) == other for c in p.ledger)


def refused_before(p: Person, kinds: tuple, subject: str, tick: int = 0, decay: int = 0) -> int:
    """THE PRESENT CONFIDENCE (`0..confidence_default`) OF THE NEWEST CLAIM IN WHICH `p` WAS HIMSELF REFUSED THIS OPPORTUNITY, else `0`.

    The claim is one `p` holds firsthand in his OWN ledger -- untold, `doer == p.id` -- whose predicate is in `kinds` (the verb row's
    `emits_on_refusal`) and whose subject is `subject`. The newest is the greatest `(when, lap, present confidence)`, the order
    `_latest_claim` ranks by. It is `0` when there is none, or when `p` holds ANY claim about `subject` NEWER than it by `(when, lap)`: news of the
    subject supersedes the memory, the thing may have changed. A claim at the refusal's own `(when, lap)` is not newer (the refusal's own
    deposits share it).

    ⚠ IT TAKES THE PERSON, NOT A LEDGER AND A HOLDER: the holder cannot differ from the asker (AX-2; `04` §B.2's own-ledger carve-out), and no
    World is read. Confidence is read through `state/ledgers.py::present_confidence` at the `tick` and `decay` given -- the one owner of fading
    -- never the stored deposit value; with neither given (a hand-built ledger) the stored value is read, as `LedgerReader` does."""
    refused = [c for c in p.ledger if c.subject == subject and c.predicate in kinds and c.doer == p.id and c.firsthand]
    if not refused:
        return 0
    newest = max(refused, key=lambda c: (c.when, c.lap, present_confidence(c.confidence, c.when, tick, decay)))
    if any(c.subject == subject and (c.when, c.lap) > (newest.when, newest.lap) for c in p.ledger):
        return 0
    return present_confidence(newest.confidence, newest.when, tick, decay)


def conviction_stand(p: Person, affiliation: str) -> float:
    """HOW FAR `p` STANDS FOR (+1) OR AGAINST (-1) ONE AFFILIATION, on `[-1, +1]`: `p.conviction[affiliation]`
    centred on the affiliation scale's midpoint and scaled by its half-range, `(v - mid) / half`. An ABSENT key
    is 0 -- never considered, which is not held, and stands neither way -- while a STORED 0 is a considered
    rejection and reads `-1`, the farthest the scale goes (v9 IN-63; `conviction_map`). Person-side (AX-2)."""
    v = (p.conviction or {}).get(affiliation)
    if v is None:
        return 0.0
    half = (AFFILIATION_CEILING - AFFILIATION_FLOOR) / 2
    return (v - (AFFILIATION_FLOOR + half)) / half


def stands_for(p: Person, reading: str) -> tuple:
    """THE AFFILIATIONS `p` STANDS FOR, sorted by name: those of `p.conviction` with `conviction_stand(p, a) > 0`, so above the scale's
    midpoint (intensity 3 or more of 5; an absent key stands neither way, a stored 0 stands against). The one owner of what "stands for"
    means (B10.07 writes the `"stands"` reading only; `20_NARRATIVE_A_stands_for` edit 1 adds the others), composed on
    `conviction_stand`, so no second threshold is written beside it. Any other `reading` is refused, not read as `"stands"`. Person-side (AX-2)."""
    if reading != "stands":
        raise ValueError(f"stands_for reading {reading!r} is not built: only \"stands\" is")
    return tuple(a for a in sorted(p.conviction or {}) if conviction_stand(p, a) > 0)


def heritage_regard(p: Person, q: str, fx) -> float:
    """THE CASTE ESTIMATE (v11 CR-31; ED-IN-0301): how `p`'s OWN creed colours his regard for `q`, through
    what `p` BELIEVES of `q`'s descent -- never through what `q` is (another person's `Person.heritage` is world
    truth and is not read here; `p`'s own reaches his sheet through `PersonInterior.heritage`, B04.13).

        heritage_regard = heritage_gain · STANCE_MAX · mean over the affiliations a in the concern
                          `HERITAGE_ENGAGES[h]` of `conviction_stand(p, a)`

    `h` is the heritage named in `p`'s NEWEST own untold `seen` claim whose `who` is `q` and whose `marks`
    names a heritage (newest by `(when, lap)`, a later deposit winning a tie). Each affiliation of the
    engaged concern contributes `conviction_stand`, an absent key 0 and still counted in the mean. In
    `regard`'s own units, so `teller_weight` reads it through `regard / STANCE_MAX` as it reads any stance.
    `0.0` where `p` holds no such `seen` claim, where the heritage engages no concern, or at `heritage_gain` 0
    -- the CONTROL, which reads no ledger. Reads `p`'s ledger and conviction only: no other person's, and no
    World (AX-2). [ASSUMPTION; medium; Jordan to correct; revert: `heritage_gain` 0]"""
    gain = float(fx.get("heritage_gain"))
    if not gain >= 0:                # `not >=`, so a NaN is refused too
        raise ValueError(f"heritage_gain {gain} must be >= 0 (H-358)")
    if not gain:
        return 0.0
    best, best_key = None, None
    for c in p.ledger:
        if c.predicate != SEEN_PREDICATE or c.chain or getattr(c.value, "who", None) != q:
            continue
        named = next((m for m in (getattr(c.value, "marks", None) or ()) if m in HERITAGES), None)
        if named is None:
            continue
        key = (c.when, c.lap)
        if best_key is None or key >= best_key:
            best, best_key = named, key
    concern = HERITAGE_ENGAGES.get(best)
    if concern is None:
        return 0.0
    members = AFFILIATION_CONCERNS[concern]
    return gain * STANCE_MAX * (ltr_sum(conviction_stand(p, a) for a in members) / len(members))


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


def legitimacy(p: Person, holder: str, window, scar_shift: float = 0.0, hold: str = _CONTROL_SCAR_HOLD, mass: float = _CONTROL_SCAR_MASS) -> float:
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
    axis_w = projected_axes(p, scar_shift, hold=hold, mass=mass)
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
    hold, mass = (fx.get("scar_hold"), fx.get("scar_primary_mass")) if fx is not None else (_CONTROL_SCAR_HOLD, _CONTROL_SCAR_MASS)
    cosine = pursuit_cosine_axes(projected_axes(p, shift, hold=hold, mass=mass), to_axes(expected or {}))
    held = p.conviction or {}
    aff = (ltr_sum(sign * held.get(name, 0) / AFFILIATION_CEILING for name, sign in engaged) / len(engaged)
           if engaged else 0.0)
    reg = (ltr_sum(max(-1.0, min(1.0, regard(p, x, fx) / STANCE_MAX)) for x in regarded) / len(regarded)
           if regarded else 0.0)
    return (0.0 if cosine is None else cosine), aff, reg


def opinion(p: Person, expected: dict, engaged: tuple, regarded: tuple, fx=None) -> float:
    """`p`'s OPINION OF A FACTION, on `[-3, +3]`: the sum of `opinion_terms` (v9 IN-70). `0` is
    indifference -- each term's own midpoint -- so the sign is the side. Computed when asked, never
    written (A-29, T-a). Person-side; the World half is `world_q.opinion_of`. Added left to right, not
    by `sum()`, whose float summation is compensated since Python 3.12: one order, one number (`fmath.ltr_sum`'s
    rule; the means inside `opinion_terms` go through it too)."""
    pursuit, affiliation, reg = opinion_terms(p, expected, engaged, regarded, fx)
    return pursuit + affiliation + reg


def _pursuits_violated_by(verb: str, floor: float = 0.0) -> frozenset:
    """The pursuits an act of `verb` violates, whoever holds them: `elements_violated_by`' pursuit
    half, which reads only `(verb, element)`. The candidates are `data/verbs.py::PURSUIT_PROJECTION`'s
    keys, read through the module at call time so a rebound projection is what is asked; a pursuit
    the projection does not list projects to the zero vector and violates nothing. A pursuit is violated when
    `pursuit_lean(verb, e) < -floor` (`Fixtures.scar_lean_floor`, `H-467`; `0.0` is the sign test)."""
    row = {ax: _verbs.align(verb, ax) for ax in PURSUIT_AXES}
    if not any(row.values()):
        return frozenset()
    return frozenset(e for e in _verbs.PURSUIT_PROJECTION if pursuit_lean(verb, e, row) < -floor)


def _pursuits_upheld_by(verb: str, floor: float = 0.0) -> frozenset:
    """`_pursuits_violated_by`' twin: the pursuits an act of `verb` honours, whoever holds them, those whose `pursuit_lean(verb, e)` is
    above `+floor` (`Fixtures.scar_lean_floor`). An act can uphold and violate no pursuit at once (`floor >= 0`)."""
    row = {ax: _verbs.align(verb, ax) for ax in PURSUIT_AXES}
    if not any(row.values()):
        return frozenset()
    return frozenset(e for e in _verbs.PURSUIT_PROJECTION if pursuit_lean(verb, e, row) > floor)


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
        return ltr_sum(proj[ax] * _verbs.align(verb, ax) for ax in _AXES)
    return ltr_sum(proj[ax] * row[ax] for ax in _AXES)


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
    `elements_violated_by`' affiliation half, `engagement(verb, a) < 0`. The candidates are
    `rosters.AFFILIATIONS`, the roster `data/affiliations.py::conviction_map` holds every
    `Person.conviction` key to."""
    return frozenset(a for a in AFFILIATIONS if engagement(verb, a) < 0)


def elements_violated_by(verb: str, floor: float = 0.0) -> tuple:
    """WHICH ELEMENTS AN ACT OF `verb` VIOLATES -- `(pursuits, affiliations)`, as two frozensets, the
    person-free reading under the scar (IN-08 H3, `ED-IN-0261`'s scar model: a COUNT per element,
    accrued by WITNESSING; H11 over the affiliation table, J-5's C4).

    A pursuit `e` is violated when `Σ_axis projection[e][axis] · alignment(verb, axis) < 0` -- the
    verb leans against where the pursuit points. ⚠ THAT SIGN TEST IS A CANDIDATE READING RECORDED FOR
    REVIEW, NOT A RULING (IN-08 H3): no source states
    the violation predicate; this is the plainest one the two owned tables admit. It composes on the
    two owners and copies neither: `data/pursuits.py::to_axes` (pursuit -> axes, one owner) and
    `data/verbs.py::align` (the one binding the alignment sweep rebinds). A verb with no celled axis
    violates nothing, by construction.

    An affiliation `a` is violated when `data/affiliations.py::engagement(verb, a) < 0`: the verb's
    cell for that affiliation, which is the shared column's cell when the affiliation has none of
    its own (R-C4.1: the vow-shaped verbs engage every creed alike). Both halves are a sign test:
    the intensity or weight a person holds does not enter it, because the scar is a COUNT per element
    and an act is witnessed or not.

    Whether an element is violated is a property of `(verb, element)` alone, so
    `loop/resolve.py::_scar_witnesses` asks this once per act and intersects each person's holdings
    with it (`broken_by`) instead of re-deriving the sign test per person; a change to either sign
    test is made in `_pursuits_violated_by` or `_affiliations_violated_by`. Person-side, no World
    (AX-2). Reads `ALIGNMENT` and `PURSUIT_PROJECTION` at call time: never cache it across a sweep's
    rebind."""
    return _pursuits_violated_by(verb, floor), _affiliations_violated_by(verb)


def _held(weights, violated: frozenset, only: Optional[frozenset] = None) -> tuple:
    """The elements of `weights` held above zero and in `violated`, sorted by name; with `only` (a person's primary set), those in it too."""
    weights = weights or {}
    return tuple(e for e in sorted(weights) if float(weights[e]) > 0 and e in violated and (only is None or e in only))


def primary_pursuits(pursuits, mass: float) -> frozenset:
    """A PERSON'S PRIMARY PURSUITS: the fewest top-weighted held pursuits whose weights sum to at least `mass`
    (`Fixtures.scar_primary_mass`), taken by weight descending, ties by name ascending, the sum added left to right. A person
    whose held weights never reach `mass` has every held pursuit primary."""
    ranked = sorted(((e, float(w)) for e, w in (pursuits or {}).items() if float(w) > 0), key=lambda ew: (-ew[1], ew[0]))
    out, total = [], 0.0
    for e, w in ranked:
        if total >= mass:
            break
        out.append(e)
        total += w
    return frozenset(out)


def _primary_of(p: Person, hold: str, mass: float) -> Optional[frozenset]:
    """THE ELEMENTS `p` MAY BE SCARRED ON under `hold` (`Fixtures.scar_hold`): `None` (no restriction) at `any`; at `primary`
    his primary pursuits and the affiliations he stands for (`stands_for`), computed once per call. An unknown `hold` is refused."""
    if hold not in SCAR_HOLDS:
        raise ValueError(f"scar_hold {hold!r} is not in rosters.yaml: scar_holds {sorted(SCAR_HOLDS)} (H-466)")
    if hold == "any":
        return None
    return primary_pursuits(p.pursuits, mass) | frozenset(stands_for(p, "stands"))


def broken_by(p: Person, violated: tuple, hold: str, mass: float) -> tuple:
    """The elements `p` holds that `violated` (an `elements_violated_by` answer) names: the held
    pursuits, then the held affiliations, each sorted. "Held" is `_held`'s sense (a weight above
    zero); the sign test is not re-asked, `violated` already carries it. `hold` and `mass` are
    `Fixtures.scar_hold` and `scar_primary_mass`, REQUIRED (no default is held here, so no second copy of `scar_primary_mass` exists):
    at `primary` only his primary elements count (`_primary_of`)."""
    only = _primary_of(p, hold, mass)
    pursuits, affiliations = violated
    return _held(p.pursuits, pursuits, only) + _held(p.conviction, affiliations, only)


def upheld_by(p: Person, upheld: frozenset, hold: str, mass: float) -> tuple:
    """The pursuits `p` holds that `upheld` (a `_pursuits_upheld_by` answer) names, sorted: the elements an act honours that he lives
    for, the vindication's candidates. `hold` and `mass` as `broken_by`: at `primary` only his primary pursuits. Pursuits only (an
    affiliation has a sign and no lean, so no floor to honour past)."""
    return _held(p.pursuits, upheld, _primary_of(p, hold, mass))


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


def crisis_weights(p: Person, shift: float = 0.0, hold: str = _CONTROL_SCAR_HOLD, mass: float = _CONTROL_SCAR_MASS) -> dict:
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
    out = _scar_shifted(p, shift, hold, mass)
    w = out.get(DOCTRINE_PURSUIT)
    if not w or not p.conviction:
        return out
    k = religious_intensity(p)
    if k == 1.0:
        return out
    return {**out, DOCTRINE_PURSUIT: w * k}


def _most_to_least_scarred(p: Person, base: dict, held: dict, among: list, shift: float) -> dict:
    """`base` with the fraction `shift` of the MOST-scarred of `among` (highest count, ties by name) given to the LEAST-scarred of it
    (lowest count, shared in proportion to their weights, the source never its own heir): a person's total is kept. One member: `base`."""
    ranked = sorted(among, key=lambda e: (-p.scar.get(e, 0), e))
    source = ranked[0]
    low = min(p.scar.get(e, 0) for e in ranked)
    heirs = {e: held[e] for e in ranked[1:] if p.scar.get(e, 0) == low}
    if not heirs:
        return base
    given, pool = held[source] * shift, ltr_sum(heirs.values())
    out = dict(base)
    out[source] = held[source] * (1.0 - shift)
    for e, w in heirs.items():
        out[e] = w + given * w / pool
    return out


def _scar_shifted(p: Person, shift: float, hold: str = _CONTROL_SCAR_HOLD, mass: float = _CONTROL_SCAR_MASS) -> dict:
    """`p`'s pursuit weights as the chooser should read them once scars have reached threshold 2
    (IN-08 H9, `ED-IN-0261`: *"WEIGHT SHIFTS, others gain proportionally"*) -- A READER, it writes
    nothing and `Person.pursuits` is untouched.

    A held pursuit `e` with `p.scar[e] >= SCAR_WEIGHT_SHIFT_AT` gives up the fraction `shift` of
    its weight (downward: `conviction_track_v1.md` §2, reference for intent), and the mass given up
    is shared among the held pursuits that have NOT reached the threshold in proportion to their
    own weights, so a person's total weight is conserved. Where every held pursuit (at `hold` `primary`, every primary) is at the
    threshold, the most-scarred gives its share to the least-scarred (`_most_to_least_scarred`), not skipped.
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
    if not crisis:
        return base
    # EVERY HELD (`_held`'s sense, at `hold` his primary) PURSUIT AT THE THRESHOLD: nobody is below it to gain, so the shift runs from the
    # most-scarred (count descending, ties by name) to the least-scarred, by count, not skipped (B10.08, F-PES-CHAR-11).
    among = _held(held, frozenset(held), _primary_of(p, hold, mass))
    if among and all(p.scar.get(e, 0) >= SCAR_WEIGHT_SHIFT_AT for e in among):
        return _most_to_least_scarred(p, base, held, among, shift)
    heirs = {e: w for e, w in held.items() if e not in crisis}
    if not heirs:
        return base
    given = ltr_sum(held[e] * shift for e in crisis)
    pool = ltr_sum(heirs.values())
    out = dict(base)
    for e in crisis:
        out[e] = held[e] * (1.0 - shift)
    for e, w in heirs.items():
        out[e] = w + given * w / pool
    return out


def projected_axes(p: Person, shift: float = 0.0, manner: bool = True, hold: str = _CONTROL_SCAR_HOLD, mass: float = _CONTROL_SCAR_MASS) -> dict:
    """`p`'s pursuits projected to the axes, `to_axes(crisis_weights(p, shift))`, plus his own stored manner offset on each axis he holds one
    (B10.58, A-108; `Person.manner_offset`): person-side (AX-2). THE ONE READER OF THE OFFSET. An axis he holds none on is exactly his pursuits'
    projection (nothing is added, so a person with no offset projects as he did before the offset existed).

    ⚠ `manner=False` IS THE PROJECTION FROM HIS PURSUITS ALONE, AND THE REFUSAL GATE'S ONE ASK (`decision/options.py::refusal_tolerance`): M37 --
    no manner axis feeds the gate (`proposals/2026-10-24-character-layers-v2.md` section 11.5), and the armed axis, `deontological_instrumental`, is one
    of the three the offset sits on. Every other reader takes the default and gets the offset.

    `hold` and `mass` are `Fixtures.scar_hold` and `scar_primary_mass` (B10.07): a reader that holds the fixtures passes both, so the weights it reads are shifted among the
    elements the writer (`loop/resolve.py::_scar_witnesses`) scars; a hand-built read with none gets the fixtures' control."""
    axes = to_axes(crisis_weights(p, shift, hold, mass))
    if manner:
        for axis, offset in p.manner_offset.items():
            axes[axis] += offset
    return axes


def decisiveness(p: PersonInterior, shift: float = 0.0, manner: bool = True, hold: str = _CONTROL_SCAR_HOLD, mass: float = _CONTROL_SCAR_MASS) -> float:
    """HOW FIRMLY `p`'s PURSUITS POINT ONE WAY: the length of `projected_axes(p, shift, manner)`. The draw in
    `decision/choose.py::_sample_order` is read against score margins, which scale with this, so it is
    the person's decisiveness at a given `choice_temperature`. Person-side (AX-2); stores nothing.
    Summed in `_AXES` order by `ltr_sum`, the order of `pursuit_cosine_axes`'s norm."""
    v = projected_axes(p, shift, manner, hold, mass)
    return math.sqrt(ltr_sum(v[a] ** 2 for a in _AXES))


# B10.14: the names a `tables.crisis_bands` row may use that are the READER's (`data/rosters.py::_load_crisis_bands` keeps the table's shape only).
_FAILURE_BRANCH = "fold_else_destroy_else_minus_two"  # [canonical: engine/season/rosters.yaml §tables.crisis_bands (Failure `branch`)]
_FAILURE_STEP = 2   # [canonical: engine/season/rosters.yaml §tables.crisis_bands (the branch's name: `minus_two`)]
# `scar` setting name -> the count it sets on the creed in crisis.
_CRISIS_SCAR_SETTINGS = {"zero": 0, "threshold_less_one": SCAR_CRISIS_AT - 1}  # [canonical: engine/season/rosters.yaml §tables.crisis_bands (`scar` names); the threshold is SCAR_CRISIS_AT]


def _step(held: dict, x: str, steps: int) -> None:
    """Move `held[x]` by `steps` whole steps, clamped to the intensity spine (`AFFILIATION_FLOOR`..`AFFILIATION_CEILING`). A creed already gone is left."""
    if x in held:
        held[x] = max(AFFILIATION_FLOOR, min(AFFILIATION_CEILING, held[x] + steps))


def _fold_or_destroy(held: dict, x: str) -> bool:
    """TODAY'S TWO BUILT BRANCHES for the creed `x` in crisis, applied to `held` in place: FOLD into the highest-held incompatible co-held creed
    (ties to the first by name), else DESTROYED where nothing else is held. False, `held` untouched, where neither applies (RESTABILISE, not built)."""
    heirs = [y for y in sorted(held)
             if y != x and held[y] > 0 and frozenset((x, y)) in _aff.INCOMPATIBLE]
    if heirs:
        y = max(heirs, key=held.__getitem__)
        held[y] = min(AFFILIATION_CEILING, held[y] + held[x])
        del held[x]
        return True
    if not any(v > 0 for k, v in held.items() if k != x):
        del held[x]
        return True
    return False


def conviction_after_crisis(p: Person, among: frozenset | None = None, band: str | None = None, shared: bool = False,
                            reading: str = "any") -> tuple:
    """`(conviction, scar_delta)`: `p.conviction` as the crisis at scar threshold 3 leaves it -- IN-08 `12e` H13, G-Q6 as the
    affiliation draft recommends (folded into the build by Jordan's 2026-10-06 ruling, `ED-IN-0261`'s
    superseding row): THE ENGINE CHOOSES PER CASE, BY A RULE OVER STATE THE CRISIS ALREADY READS, AND
    ROLLS NOTHING (the crisis rewrites the vector, never an outcome). A READER: it returns a new
    vector and writes nothing; the write is `loop/resolve.py::_conviction_crisis`'s, by an act.

    A held affiliation is IN CRISIS when `p.scar` for it is `>= SCAR_CRISIS_AT`. ONE CRISIS AT A
    TIME: where several are, the one taken is the highest-held (the lowest-held where `shared`, below), ties to the first by name -- the
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
    returns `p.conviction` unchanged and no scar delta.

    B10.14 -- ONE COMPOSED SIGNATURE (C3-K2), `(p, among=None, band=None, shared=False, reading="any")`, returning `(conviction, scar_delta)`:
      * `band=None` is TODAY'S FUNCTION EXACTLY (the control, `Fixtures.crisis_arm: rule`): the branches above, no table read, `scar_delta` `{}`.
      * `band` (a degree band the one ladder names) applies that band's writes from `rosters.yaml: tables.crisis_bands` (`CRISIS_BANDS`), in order, to the
        creed `x` in crisis: `intensity` moves it a whole number of steps, clamped to the spine (a creed at 1 stepping down is a held 0, not a drop);
        `scar` names the count `x` is set to; `branch` names the Failure band's composite (fold, else destroyed, else `intensity` less
        `_FAILURE_STEP`, floored). A band or a write name this reader does not know is refused, never read as nothing.
      * `scar_delta` is `{creed: signed change to that creed's count}`, `{}` where the band moves no count: THE READER WRITES NOTHING, so the
        count is the caller's to set (B10.15). [ASSUMPTION; Jordan to correct: a dict and not the bare int the plan names, because the caller does
        not know which creed was taken; revert: an int, the caller re-deriving `x`.]
      * `shared` takes the LOWEST-held creed as the one in crisis (ties to the first by name) where the violation came from the shared column of
        `affiliation_engagement` and so scarred every co-held creed alike; a per-affiliation cell is `shared=False`, the highest-held, unchanged. This
        reverses `max` to `min` for the shared column and for nothing else. [ASSUMPTION; medium; Jordan to correct: the lowest-intensity creed is the
        one a blanket wound breaks first, folding into the creed he holds hardest; revert: `shared=False`.]
      * `reading` is which held creeds a fold may land on. `"any"` is every creed held above 0, today's reading; `"stands"` (the creeds he stands
        for, `stands_for`) is `20_NARRATIVE_A` edit 4b's and is refused here, as `stands_for` refuses a reading it has not built."""
    if reading != "any":
        raise ValueError(f"conviction_after_crisis reading {reading!r} is not built: only \"any\" is")
    if band is not None and band not in CRISIS_BANDS:
        raise ValueError(f"conviction_after_crisis band {band!r} is not a row of `tables.crisis_bands` {sorted(CRISIS_BANDS)}")
    if not p.conviction:
        return p.conviction, {}
    held = dict(p.conviction)
    scar = p.scar or {}
    # "Held" is above 0 (IN-63): a stored 0 is a rejection, which no count can crisis.
    crisis = [x for x in sorted(held) if held[x] > 0 and scar.get(x, 0) >= SCAR_CRISIS_AT
              and (among is None or x in among)]
    if not crisis:
        return p.conviction, {}
    # `crisis` is in name order and `max` / `min` keep the FIRST of equal keys, so a tie on
    # intensity goes to the lowest name.
    x = (min if shared else max)(crisis, key=held.__getitem__)
    where = f"{p.id}: conviction after crisis"
    if band is None:
        if not _fold_or_destroy(held, x):          # RESTABILISE -- not built (above)
            return p.conviction, {}
        return conviction_map(held, where=where), {}
    delta: dict = {}
    for kind, value in CRISIS_BANDS[band]:
        if kind == "intensity":
            _step(held, x, value)
        elif kind == "scar":
            if value not in _CRISIS_SCAR_SETTINGS:
                raise ValueError(f"crisis band {band!r}: scar setting {value!r} is not one of {sorted(_CRISIS_SCAR_SETTINGS)}")
            if _CRISIS_SCAR_SETTINGS[value] != scar.get(x, 0):
                delta[x] = _CRISIS_SCAR_SETTINGS[value] - scar.get(x, 0)
        elif kind == "branch" and value == _FAILURE_BRANCH:
            if not _fold_or_destroy(held, x):      # the third arm, where today's RESTABILISE was not built: no person in crisis is a no-op
                _step(held, x, -_FAILURE_STEP)
        else:
            raise ValueError(f"crisis band {band!r}: write {kind}: {value!r} is not one this reader knows")
    return (p.conviction if held == p.conviction else conviction_map(held, where=where)), delta


# ---------------------------------------------------------------------------
# `LedgerReader` (ED-IN-0206). It asks ONE PERSON'S OWN CLAIMS and nothing else: it takes neither a
# `World` nor even a `Person`, only the claims themselves, which is the asker-first family exactly and
# the `§A.2` table's *"may read a `PersonInterior` snapshot only"* row it sits under.
#
# ⚠ THE TWO READERS ARE THE SAME QUESTION ASKED OF TWO SOURCES, and splitting them by source is what
# makes that symmetry checkable instead of merely stated -- `test_person_q_cannot_reach_the
# _world_side` asserts that this side cannot reach the other. `REQUIRES_STEMS` and
# `LEDGER_DERIVED_STEMS` -- the stems `WorldReader.read`/`LedgerReader.read` dispatch on -- live in
# `season.data.requires`, imported at the top of this file.
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
    comparator, unchanged; B09.07's callers (`belief_contradicts`, `said_of`, `lie_said_of`, `decision/sheet.py::chronicle`) pass
    `ledger_weigh`'s closure. `world_q.current_stage` takes the parameter and NO CALLER SUPPLIES IT YET (`open_stages`' callers
    pass none; `world_q.py`'s `current_stage` docstring says the reader is dormant), so a stage is still read by the plain comparator.
    `confidence` is read at the reader's `tick` and `decay` (`present`) either way: a claim stores what it was
    deposited at and fading is computed here, where it is read (`state/ledgers.py::present_confidence`);
    weighing never rewrites a claim."""

    def __init__(self, claims, weigh=None, *, tick: int = 0, decay: int = 0):
        self._claims = list(claims or [])
        self._weigh = weigh
        self._tick = tick
        self._decay = decay

    def present(self, c) -> int:
        """`c`'s confidence AS THIS READER HOLDS IT, at the `tick` it was constructed with: the deposit less
        `decay` per season elapsed (`state/ledgers.py::present_confidence`, the one owner of the fade). A
        claim's stored `confidence` is what it was deposited at and is never rewritten, so every
        comparison below reads here. A reader built with no `tick` and no `decay` (a hand-built ledger in
        a test) reads the stored value, which is the present one at the deposit's own tick."""
        return present_confidence(c.confidence, c.when, self._tick, self._decay)

    def _support(self, matches) -> list:
        """`support(v) = 1 - PROD over distinct origins (1 - weigh(c))`, one entry per match, in
        match order. Grouped by `(predicate, value)` -- `read`'s matches share one predicate, so
        for `read` that is grouping by value. Under a `weigh`, `latest_about` therefore ranks
        ACROSS predicates by support, so a firsthand claim on any predicate outranks hearsay on
        another; `said_of` and `chronicle` weigh `latest_about` since B09.07, which decided it
        (a person passes on what he is surest of). An origin is `c.chain[0]` for a told claim and the holder for
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

        ⚠ ONE OWNER: `read` and `latest_about` both call it, so neither carries its own copy of the
        loop (`ci_common.load_yaml`'s docstring records the anti-pattern: *"a single-owner comment
        asserting a property the tree lacks is worse than no comment"*)."""
        if self._weigh is None:
            best = None
            for c in self._claims:
                if match(c) and (best is None
                                 or (c.when, self.present(c)) > (best.when, self.present(best))):
                    best = c
            return best
        matches = [c for c in self._claims if match(c)]
        best, best_key = None, None
        for c, s in zip(matches, self._support(matches)):
            key = (s, c.when, self.present(c))
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
        both methods call. `CLAUDE.md` §8: the rule lives once. MOST RECENT, THEN MOST
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


#: The site whose `gate` row names the held value and the threshold fixture the Thread gate reads (B04.06; U1 §8). It is the one
#: site `capability_use_sites` registers to `OwnStateReader`; `told_retain`, the other gate site, has no reader on this tree.
OWN_STATE_GATE = require_use_site("own_state_gate")


def _gate_row(use: str):
    """The one `gate` row of site `use`, or `None`: a site with no row reads NO CAPABILITY, never a default."""
    rows = [r for r in capability_rows(use) if r.role == "gate"]
    return rows[0] if rows else None


def _held_at(p: Person, key: str):
    """The value `p` holds at a practitioner stat's registry key (`prac.thread_sensitivity`): the `Person` field of that name."""
    return getattr(p, key.rpartition(".")[2], None)


# B10.64 (`U5a_CHAR_self_knowledge_is_a_belief` edits 2, 4, 5): WHAT A PERSON BELIEVES OF HIMSELF. The claim a person holds of himself under a key of
# `data/rosters.py::SELF_BELIEVED` is `Claim(subject=<himself>, predicate=SELF_STEM + <key>, value=True)`, his own; the spelling beside `BOND_STEM`'s.
SELF_STEM = "self:"


def holds_self_key(p, key: str) -> bool:
    """WHETHER `p` HOLDS `key`, a member of `data/rosters.py::SELF_BELIEVED`: a pursuit he has a weight on, or the gated gift's field authored (not `None`).
    The one test `boot/realm.py::seed_self_knowledge` asks of a person, so the keys it seeds are the keys `knows_self` is asked of."""
    if key in PURSUITS:
        return key in (p.pursuits or {})
    return _held_at(p, key) is not None


# B10.66 (`U5a` edit 6 (b)): A SKILL SHOWN AT OVERWHELMING TELLS ITS HOLDER HE HAS IT. The Observation `(himself, "skill_shown:<key>", True)` rides the act's Event (`Event.observed`,
# D-U1-06), a named predicate beside `BODY_STEM` and `BROKE_STEM` and no member of `rosters.yaml: observation_terms`, which is `epistemic.Seen`'s field list. WITNESS deposits it
# as written, to the actor alone at the shipped `observation_deposit_mode: actor` (no channel rule is written here), and `knows_self` reads it as his own `self:<key>`.
SKILL_SHOWN_STEM = "skill_shown:"
_SELF_STEMS = (SELF_STEM, SKILL_SHOWN_STEM)


def _firsthand_self(p, key: str) -> bool:
    """WHETHER `p` already holds, of himself, a claim he made of it himself (no chain) for `key`: the seeded `self:<key>` or an earlier shown deposit."""
    return any(c.subject == p.id and c.value is True and not c.chain and c.predicate in (s + key for s in _SELF_STEMS) for c in p.ledger)


def skill_shown_observed(p, fed_by: tuple, degree) -> tuple:
    """THE OBSERVATIONS A GRADED ACT OF `p`'S CARRIES FOR WHAT IT SHOWED OF HIM: one `(p.id, "skill_shown:<key>", True)` per distinct `key` that a row of the act's
    `fed_by` (`seam/wrappers/sigma.py::_fed_by`: `(use, role, key, side, value, contributed)`) names on his own side with a contribution, where the act's own band is Overwhelming
    (`DEGREE_LABEL`; no second draw), the key is one he can be unaware of (`SELF_BELIEVED`) and holds (`holds_self_key`), and he does not already hold a claim of it he made himself
    (`_firsthand_self`: a man seeded with `self:<key>`, or shown it before, is told nothing, so no claim is stored twice and none contradicts the seeded one). `()` otherwise.
    [ASSUMPTION; medium; Jordan to correct -- basis: `U5a` edit 6 (b); revert: the Observation is emitted on every Overwhelming act that names the key, a repeat included.]"""
    if degree != DEGREE_LABEL[Degree.OVERWHELMING]:
        return ()
    keys = dict.fromkeys(key for _use, _role, key, side, _value, contributed in fed_by
                         if side != "subject" and contributed and key in SELF_BELIEVED and holds_self_key(p, key) and not _firsthand_self(p, key))
    return tuple(Observation(p.id, SKILL_SHOWN_STEM + key, True) for key in keys)


def knows_self(p, key: str, weigh=None, fx=None) -> bool:
    """THE ONE READER OF WHETHER A PERSON RECOGNISES `key` IN HIMSELF: True for a key outside `data/rosters.py::SELF_BELIEVED` (known by construction), and for a member
    where his own ledger holds `self:<key>` as True (the best-supported, then latest claim, `LedgerReader`'s comparator), and False where it holds none -- a person marked `unaware:` at build is seeded none (`boot/realm.py::seed_self_knowledge`).
    Person-side (AX-2): his ledger and his id, nothing else.

    A claim he made of himself (firsthand, no chain) is believed as it stands, so it never fades out of him. A claim he was TOLD is believed only where `weigh` (his
    reading of the teller, `decision/options.py::ledger_weigh`, built by the caller because this module may not import `decision/`) puts it at or above
    `Fixtures.self_told_floor` (H-483; read only here, only for a told claim, and `0.0` at the control believes every one). Without a `weigh` a told claim is read as it stands."""
    if key not in SELF_BELIEVED:        # a key outside the roster is known by construction, as it always was
        return True
    if _firsthand_self(p, key):         # B10.66: what he made of himself stands against a teller he disregards
        return True
    mine = [c for c in p.ledger if c.subject == p.id and c.predicate in (s + key for s in _SELF_STEMS)]    # B10.66: a skill shown is his `self:<key>`
    best = LedgerReader(mine, weigh).belief_among()
    if best is None or best.value is not True:
        return False
    if best.chain and weigh is not None and fx is not None:
        return weigh(best) >= fx.get("self_told_floor")
    return True


def recognised(p, mapping) -> dict:
    """`mapping` (a pursuit-keyed map: his weights, his scar counts) with the keys he does not recognise in himself taken out -- the one filter his sheet
    reads (`decision/sheet.py`). A key outside `SELF_BELIEVED` is always recognised (`knows_self`)."""
    return {k: v for k, v in dict(mapping or {}).items() if knows_self(p, k)}


class OwnStateReader:
    """THE QUESTIONS A PERSON ANSWERS OF HIMSELF (v9 PC-06 K-3, `H-85`) -- `OWN_STATE_STEMS`, and
    nothing else: every other predicate is UNKNOWN here.

    ⚠ THE ONE ANSWERER OF BOTH STEMS, FOR BOTH SIDES. The fold's `queries/world_q.py::WorldReader`
    delegates to it for the person the act names, and `decision/options.py::opening_set` asks it of
    the person forming, so the gate and the person's own reading of it are one read, not two copies.
    It takes the PERSON and the fixtures and no World (and reads his own ledger only under `believes`, below): a person's sensitivity is his
    own state (`Person.thread_sensitivity`), not a belief about the world (§F1's asymmetry is about
    the world, as `opening_set`'s self-contest decline is about being alone in a room).

      * `thread_sensitivity` -- the subject's own value, and ONLY when the subject is this person: a
        person reads nobody else's. `None` (nothing authored) is UNKNOWN, never 0, so it refuses at
        the fold and does not pass a gate swept to 0.
      * `thread_sensitivity.gate` -- the Fixture the gate row names (`thread_sensitivity_gate`), the SECOND READ
        the value is held against (`work`'s `floor`, `determine`'s `quorum`), the same for every subject.

      * `held_by`, `dispute`, `individual` (B10.59) -- what he holds, whom his own judgement scores against him, and whether he
        is an individual, each of HIMSELF: `held_by` and `dispute` asked of the actor, `individual` of the actor's own id.
        UNKNOWN for anybody else, so a conjunct this reader cannot answer never declines (`opening_set` declines on False).

      * `believes=True` (B10.64, B10.65; the PERSON'S side only: `decision/options.py::opening_set` passes it with his `weigh`, the fold's `WorldReader` does
        not) -- the gated gift is answered from his own claim `self:<key>` (`knows_self`) for EVERY person: held, the field's value; not held (a mark at build,
        or a told claim from a teller he disregards, `Fixtures.self_told_floor`), UNKNOWN. The fold's read of the field is unchanged, so a hand-built act still folds.

    ⚠ THE KEY AND THE FIXTURE ARE THE `own_state_gate` ROW'S (`rosters.yaml: tables.capability_uses`, B04.06); the two stems
    are the verb table's grammar and stay. A site with no row answers UNKNOWN to both."""

    def __init__(self, p: Person, fx, *, believes: bool = False, weigh=None):
        self._p, self._fx, self._believes, self._weigh = p, fx, believes, weigh

    def read(self, subject, predicate: str):
        stem, _, arg = str(predicate).partition(":")
        me = self._p.id
        # B10.59 (`02_CHAR_offer_what_can_be_done` edits 1-2): THE THREE STEMS THE WORLD'S READER ANSWERS TOO, which a person
        # answers of himself from `self._p` alone -- never a ledger, never a World, and only where he is the actor (`arg`, the
        # relation's second side) or the subject is himself, so the person-side and fold answers cannot differ. Anything
        # else is UNKNOWN: a belief about the world forms the Candidate and the fold refuses it (clause 4, R-07).
        if stem == "held_by":       # his own live `hold` Tenures (an edge is owned by its subject, `_held_objects`'s reading)
            return (any(t.kind == "hold" and t.object == subject and t.live for t in self._p.tenures)
                    if arg == me else UNKNOWN)
        if stem == "dispute":       # `WorldReader.read`'s own call, from the same `Fixtures`
            return (holds_dispute(self._p, subject, self._fx.get("scar_weight_shift"), self._fx.get("sworn_bond"),
                                  self._fx.get("deed_counterparty"), self._fx.get("scar_hold"), self._fx.get("scar_primary_mass"))
                    if arg == me else UNKNOWN)
        if stem == "individual":    # `Person.is_cohort`, the carrier's own predicate, asked of the actor
            return (not self._p.is_cohort) if subject == me else UNKNOWN
        row = _gate_row(OWN_STATE_GATE)
        if row is None:
            return UNKNOWN
        if stem == "thread_sensitivity":
            v = _held_at(self._p, row.key) if subject == me else None
            if self._believes and not knows_self(self._p, row.key, self._weigh, self._fx):     # B10.64: HIS OWN CLAIM, NOT THE FIELD (the fold's reader is built without `believes`)
                return UNKNOWN
            return UNKNOWN if v is None else v
        if stem == "thread_sensitivity.gate":
            return self._fx.get(row.gain)
        return UNKNOWN


if OWN_STATE_STEMS != {"thread_sensitivity", "thread_sensitivity.gate", "held_by", "dispute", "individual"}:
    raise SystemExit(f"`data/requires.py: OWN_STATE_STEMS` is {sorted(OWN_STATE_STEMS)}, and "
                     "`OwnStateReader.read` answers only `held_by`, `dispute`, `individual`, `thread_sensitivity` and its "
                     "gate: a stem added there with no branch here would read UNKNOWN for everybody")


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


def said_of(claims, subject, fx, teller: "Person | None" = None, *, tick: int = 0, weigh=None) -> "Said | None":
    """WHAT THIS PERSON WOULD SAY ABOUT `subject`, as the `Said` a telling carries -- or `None` for
    nothing to say. Asked of the TELLER'S OWN claims at CHOOSE (`decision/options.py::opening_set`),
    never at WITNESS: what a telling passes on is decided when it is chosen, and rides the Act.

    ⚠ A `seen` CLAIM IS PASSED ON ONLY WHEN IT IS ALL THE TELLER HOLDS ABOUT THE SUBJECT (`R8.1`).
    The `seen` deposit lands in every co-located witness -- the teller included -- with an
    identical value, so without this the teller's NEWEST claim about a rung is almost always a
    `seen` the hearer already holds, the exact-triple guard at the told deposit suppresses it, and
    the told channel carries nothing. A rumour of
    a sighting still travels when a sighting is all the teller has.

    ⚠ THE COMPARATOR IS `LedgerReader`'s, BOTH TIMES. *Most recent, then most confident* lives once
    (`_best`); only the pool differs.

    ⚠ SLANT (v9 IN-18 `G3`, `H-196`): at `Fixtures.said_slant == "valence"`, with the `teller`
    given, the pool is first narrowed to the claims the teller judges MOST STRONGLY -- the largest
    `|deed_valence|` by the teller's own projected pursuits -- and the comparator picks among those;
    where no claim carries valence (every one 0) the pick is the unslanted one exactly. A teller
    passes on the deed that matters most to THEM, not the newest thing they hold. At `newest` (the
    CONTROL, shipped), with no `teller`, or with no `fx`, it is the unslanted pick and reads no
    pursuits.

    ⚠ B09.07 `weigh`: the closure the one comparator ranks by (`decision/options.py::ledger_weigh`, passed in because this
    module may not import `decision/`), handed to `LedgerReader` as `epistemic.belief_contradicts` hands it, so a person
    passes on the belief he acts on. `None` (a hand-built read) is the plain comparator. ⚠ `LedgerReader._support`
    under a `weigh` ranks `latest_about` ACROSS predicates: a person passes on what he is SUREST of about a subject, not
    the newest thing he holds (decided at B09.07, `16_PESSIMIST_SC_B`)."""
    # B10.65: A MAN'S OWN `self:<key>` CLAIM IS WHAT HE BELIEVES OF HIMSELF, NOT HEARSAY, so it is never offered as news about himself (the seeding would otherwise make every holder a teller of his
    # own motives). Only the claim he made himself is skipped (no chain, held by its subject): a `self:` claim he was TOLD (a chain) is deposited as any told claim and is still said.
    pool = [c for c in claims if c.subject == subject and not (c.predicate.startswith(_SELF_STEMS) and not c.chain and c.holder == subject)] if claims else []
    if teller is not None and fx is not None and pool and _slant(fx) == "valence":
        axis_w = projected_axes(teller, fx.get("scar_weight_shift"), hold=fx.get("scar_hold"), mass=fx.get("scar_primary_mass"))
        strength = {id(c): abs(deed_valence(axis_w, c)) for c in pool}
        top = max(strength.values())
        if top > 0:
            pool = [c for c in pool if strength[id(c)] == top]
    reader = LedgerReader(pool, weigh, tick=tick, decay=0 if fx is None else fx.claim_decay())
    # ABSENT: H-198 deception  (an `absent` hole row, read by harness/register.py; nothing reads this marker)
    c = (reader._best(lambda c: c.subject == subject and c.predicate != SEEN_PREDICATE)
         or reader.latest_about(subject))
    if c is None:
        return None
    return Said(c.subject, c.predicate, c.value, reader.present(c), c.chain)


def drifted(before, band: float, sel: int, whole_band: bool = False):
    """A HELD NUMBER MOVED WITHIN `band`, SIGN-PRESERVING AND NEVER CROSSING ZERO -- `loop/witness.py::
    _told_value`'s numeric branch (v10 `15b`, r2 `02` §A.10.2's three clauses), shared so the
    liar's false number (`lie_said_of`) and the channel's lossy copy are ONE rule and not two. The three
    clauses: (1) `before` of 0, or a band that moves nothing (`ceil(band * |before|) < 1`, the control),
    comes back as it was; (2) otherwise a magnitude of `1 + sel % max_delta` and a direction from the next
    bit of `sel`; (3) a result that would reach or cross zero is clamped back to `before`'s own side.

    `whole_band` is the liar's reading of (2): the magnitude is the band's whole unit, `max_delta`, one step
    of `told_drift_band`'s size, not a draw within it. `sel` then only picks the direction (0: upward,
    clamped to the far side where upward would cross zero). No draw is spent by the caller either way."""
    max_delta = math.ceil(band * abs(before))
    if before == 0 or max_delta < 1:
        return before   # no sign to preserve at 0, or the band drifts nothing (control)
    magnitude = max_delta if whole_band else 1 + sel % max_delta
    after = before + magnitude if (sel // max_delta) % 2 == 0 else before - magnitude
    # §A.10.2: bounded AND signed -- `after` never crosses zero and never flips sign. A draw
    # that would do either is clamped back to the same side rather than discarded, so the
    # selection still spends exactly one hash and never re-draws.
    if before > 0 and after <= 0:
        after = before + magnitude
    elif before < 0 and after >= 0:
        after = before - magnitude
    return after


def is_cell(c) -> bool:
    """Is `c` a claim on a CELL -- a slot that holds one value (`data/requires.py: CELL_STEMS`)? The one owner,
    read by `lie_said_of` and `decision/options.py::record`'s pairing."""
    return str(c.predicate).partition(":")[0] in CELL_STEMS


def lie_said_of(claims, subject, fx, teller: "Person | None" = None, *, tick: int = 0, weigh=None) -> "Said | None":
    """WHAT THIS PERSON WOULD SAY FALSELY ABOUT `subject`: `said_of`'s pick, over the teller's CELL claims
    only, with its value made false -- or `None` where there is no false value to say (v11 CR-27, M9 taken
    (a), the cell lie; H-198 rule (i)). Asked of the LIAR'S OWN claims at CHOOSE
    (`decision/options.py::opening_set`, for a row named in `rosters.yaml: lie_verbs`) and carried on the
    Act's `payload["said"]`, so WITNESS deposits it through the one told channel and reads no ledger.

    THE FALSE-VALUE RULE [ASSUMPTION; medium; Jordan to correct; revert: a different false-value rule]:
      * a NUMBER is moved one whole step of `told_drift_band`'s unit by `drifted` -- sign-preserving and
        never crossing zero, `_told_value`'s own clauses and not a copy of them. A held 0, or a band of 0,
        has no false number to say: `None`.
      * a TRUTH VALUE becomes the other member of its closed roster, `(False, True)`. No draw is spent: the
        roster of every non-numeric cell value a ledger holds today has two members, so the other member is
        the only one (a roster with several would be drawn on `draw(actor, 'lie:<act id>')`, and the act has
        no id at CHOOSE, so none is built; it would be a WITNESS-side change).
      * anything else -- a value that is neither -- has no roster: `None`.
    A claim that is no CELL (`data/requires.py: CELL_STEMS`: a deed kind, a `seen` sighting, a `content:` or
    `shortfall:` claim) is never lied about: the pool is cells only, so the DEED lie (H-198 rule (ii)) stays
    unbuilt. The chain is EMPTY: the liar is the origin of what he says, so the hearer's claim reads
    `(liar,)` and a falsehood is never fathered on whoever told the liar the truth.

    ⚠ A FALSE VALUE IS NEVER THE HELD ONE, so the hearer's exact-triple guard (`loop/witness.py`) does not
    drop the deposit for a hearer who holds the cell firsthand: his claim and the lie then DISAGREE, which
    is the pair `decision/options.py::record` counts against the liar (`H-183`).

    `weigh` (B09.07) is `said_of`'s: the one comparator the liar reads the cell he lies about by."""
    cells = [c for c in claims if c.subject == subject and is_cell(c)]
    said = said_of(cells, subject, fx, teller, tick=tick, weigh=weigh)
    if said is None:
        return None
    held = said.value
    if isinstance(held, bool):
        false = not held
    elif isinstance(held, (int, float)):
        false = drifted(held, fx.get("told_drift_band"), 0, whole_band=True)
    else:
        return None
    if false == held:
        return None
    return Said(said.subject, said.predicate, false, said.confidence, ())


def confided_outside(claims, said: "Said", hearer: str) -> bool:
    """v9 IN-18 `G6`: DOES A COPY OF `said` IN `claims` HOLD A CONFIDENCE CIRCLE `hearer` IS OUTSIDE?
    The copy is the claim with the said `(subject, predicate, value, chain)` -- the four fields
    `said_of` copies out of it above, so the match lives beside the copy it inverts. A circle is a
    tuple `Claim.visibility` (a confided telling's deposit, `loop/witness.py::_circle_of`); `"own"`
    is none. `claims` is the TELLER'S OWN ledger, passed by the fold (`loop/resolve.py::
    _confidence_broken`). Asker-less like its sibling `said_of`; a `PersonInterior` exists
    (`state/carriers.py`) but no act carries one to the fold, so `claims` is the live ledger;
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
    _from_content_claim` share (`loop/witness.py`'s Partial-telling rewrite guards it its own way, on a tuple value)."""
    stem, sep, _ = str(c.predicate).partition(":")
    if not sep or stem != RECORD_CONTENT.get("predicate") or c.value is None:
        return None
    return dict(c.value)


def content_kind(c) -> "str | None":
    """THE `<kind>` OF A `content:<kind>` CLAIM (`rosters.yaml: record_kinds.content.predicate`),
    `None` for any other predicate. `content_said`'s sibling: the one reader of the stem's argument."""
    stem, sep, kind = str(c.predicate).partition(":")
    if not sep or stem != RECORD_CONTENT.get("predicate"):
        return None
    return kind or None


def addressees_of(said) -> tuple:
    """THE ADDRESSEE IDS OF A DOCUMENT SAYING `said` -- the list under the addressee key (`rosters.yaml: record_kinds.content.addressee`, `to`) as a
    tuple; `()` for anything that is not a dict or carries no list there. The one reader of that value's shape: `addressed_to` and `suspicions` ask it."""
    v = said.get(RECORD_CONTENT.get("addressee")) if isinstance(said, dict) else None
    return tuple(v) if isinstance(v, (list, tuple)) else ()


def addressed_to(said, pid) -> bool:
    """IS `pid` AMONG THE ADDRESSEES OF A DOCUMENT SAYING `said` -- the id list under the addressee key
    (`rosters.yaml: record_kinds.content.addressee`, `to`), which the mint stores as a list
    (`loop/effects_information.py::_addressed`). v10 IN-12 step 5a: the ONE owner of the addressee test,
    lifted out of `world_q.writs_held` (which asks it of a Record's `subject_matter`) so
    `decision/options.py::opening_set`'s terms-sourced reader asks the same rule of the holder's own
    content claim (`content_said`), World-free. `False` for anything that is not a dict."""
    return pid in addressees_of(said)


#: THE TWO ANSWERS TO A WRIT, as the kinds `comply` and `evade / defy` emit (the claims a witness of the answer holds). The one home:
#: `world_q.WRIT_ANSWERED_KINDS` is these two.
COMPLIANCE_GIVEN, COMPLIANCE_WITHHELD = "compliance.given", "compliance.withheld"


def suspicions(p: Person, admit=None) -> dict:
    """SUSPICION AS A FOLD (B21.23, `06_FA_decree_binds` edit 4; D5 ED-IN-0046, D6 ED-IN-0047, E11; ED-IN-0343 to ED-IN-0345 --
    a quantity that accumulates from events is a fold of them, not a stored value): `{other: suspicion}` for every person whose
    answer to a writ `p` MADE `p`'s own ledger holds a claim of. Nothing is written, nothing is carried between reads.

    A writ `p` made is one on which his ledger holds a content claim of his own doing (`Claim.doer`, stamped by WITNESS on the
    maker's own deposits) naming exactly ONE addressee: the answer claim (`compliance.given` / `.withheld`) names the writ and not
    its answerer, so a writ to several is attributed to no one (the pairing never guesses, `deed_doer`'s rule). Per person, over
    SEASONS (`Claim.when`): plus one for each season in which he holds a claim that the person withheld compliance (at most one a
    season, the ruled cap of D5), minus one for each season in which he holds a claim that the person complied and none that he
    withheld (E11: *"a way to reduce suspicion by over-compliance"*), the sum floored at zero.
    ONE ANSWER IS ONE EVENT, WHOEVER REPEATS IT (ED-IN-0322, *"one origin repeating itself doesn't carry more weight"*, read at the
    count): claims of one writ's one answer from several origins (his own sighting, a told copy) are one answer, at the earliest
    season he holds it [ASSUMPTION; medium; Jordan to correct; revert: count each origin's claim, `chain[0]` or the holder].
    `admit(other, writ_id) -> bool`, when given, drops an answer it refuses: `world_q.recalls` passes the command basis, so a writ to
    someone the issuing seat does not command enters no count (A-22; the Reconciled line of `06_FA_decree_binds`). Person-side
    and World-free (AX-2), so the caller that holds a World supplies it; omitted, every answer counts."""
    made = {}
    for c in p.ledger:
        if c.doer == p.id:
            to = addressees_of(content_said(c))
            if len(to) == 1:
                made[c.subject] = to[0]
    if not made:
        return {}
    answered: dict = {}          # (writ, kind) -> the earliest season he holds the answer from
    for c in p.ledger:
        if c.subject in made and c.predicate in (COMPLIANCE_GIVEN, COMPLIANCE_WITHHELD) and c.doer != p.id:
            key = (c.subject, c.predicate)
            answered[key] = min(answered.get(key, c.when), c.when)
    given: dict = {}
    withheld: dict = {}
    for (writ, kind), when in answered.items():
        other = made[writ]
        if admit is None or admit(other, writ):
            (withheld if kind == COMPLIANCE_WITHHELD else given).setdefault(other, set()).add(when)
    return {o: max(0, len(withheld.get(o, ())) - len(given.get(o, set()) - withheld.get(o, set())))
            for o in sorted(set(given) | set(withheld))}


#: THE CONTENT KEY THAT SAYS WHAT A DOCUMENT IS ABOUT, PER RECORD KIND -- the key `rosters.yaml:
#: record_sourced_operands` maps `subject` to for that kind (`terms` for a dispensation or petition,
#: `proposition` for a faction sheet). The ONE owner of "what a document is
#: about", which `decision/options.py::_content_answer` reads for `subject` too (not
#: `record_kinds.content.read_from`, which has no `faction_sheet` row).
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


#: THE OATH'S KIND, as `oblige`'s row emits it (`(sworn man, duty.taken, True)` is the claim a witness of an oath holds). The one
#: spelling `commanded_read` reads and `boot/realm.py::seed_command_knowledge` writes, read off the row so a renamed emit moves both.
DUTY_TAKEN, = _verbs.VERB_TABLE["oblige"].emits


def commanded_read(p: Person) -> frozenset:
    """WHOM `p` CAN READ AS COMMANDED -- the persons a seat of his may order, as his OWN state names them (B21.55, A-22; the
    formation half of `queries/world_q.py::commands`, which decides at the fold). Person-side, `p.tenures` and `p.ledger` only (AX-2).

    Empty for a person who holds no live `hold` (no seat, no one to order). Otherwise two readings, each over a claim he holds that
    was not told him (`chain` empty: a retelling is a rumour, not what he saw):

      * THE MEN SWORN -- a `(x, duty.taken, True)` claim: the oath's Event is anchored on the man who swore, so the claim names him;
      * THE HOLDERS HE NAMES OF OTHER SEATS -- a `(S, hold, x)` claim (the shape `sworn_to_holder` and the gate's `Subject.seat` write),
        for a seat `S` that is not one he sits in.

    ⚠ TWO LIMITS, STATED, BOTH OVER-INCLUSIONS THE FOLD CORRECTS. (1) An oath's claim names the man and never the seat he swore to
    (the Event's one change is the Tenure edge, whose id a person cannot read), so a man seen swearing to ANOTHER seat is read as
    sworn here. (2) *Beneath his* is the rung's containment, the World's (`may_revoke`'s rule), so every other seat's named holder is
    read, and an order up the chain is refused at the fold (`commands` is False for it) and not declined here. Neither widens the
    fold: it narrows who is OFFERED an order. [ASSUMPTION; medium; Jordan to correct; revert: drop this reader and
    `rosters.yaml: command_declines`, and `operand_bags` fans over every known person again.] A person is never his own man."""
    seats = {t.object for t in p.tenures if t.kind == "hold" and t.live}
    if not seats:
        return frozenset()
    out = set()
    for c in p.ledger:
        if c.chain:
            continue
        if c.predicate == DUTY_TAKEN and c.value is True:
            out.add(c.subject)
        elif c.predicate == "hold" and c.subject not in seats and isinstance(c.value, str):
            out.add(c.value)
    out.discard(p.id)
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
    -- and the person does NOT learn it from the refusal (`tell.refused` is one kind for both
    conjuncts and the `with` read is never deposited, `witness.py`). The actor is excluded because a
    person does not tell themselves (`opening_set`'s counterparty rule declines it too).
    ⚠ THE TOPIC IS NOT EXCLUDED (v9 IN-18 step 2a, #453): a telling names its topic on `subject`
    and its hearer on `to`, and they MAY be one person -- B, knowing C and holding `(C, x)`, may tell
    C what B holds about C.

    ⚠ `exists:Person` DEPOSITS ARE RARE AND `Seen.who` CARRIES THE LOAD. The told source is empty
    until a told claim lands, which T4 itself is what makes possible."""
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
