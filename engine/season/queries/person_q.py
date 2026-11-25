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
from fractions import Fraction
from dataclasses import dataclass
from typing import Any, Callable, NamedTuple, Optional

from engine.dice_engine.dice_engine import DEGREE_LABEL, Degree
from engine.dice_engine.fmath import ltr_sum
from engine.substrate.descriptors import (
    AFFILIATION_CONCERNS, HERITAGE_ENGAGES, HERITAGES, PURSUITS, about_mid, scale_of,
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
    UNKNOWN, WORLD_ONLY_STEMS, binding_of, evaluate,
)
from ..data.verbs import NO_PRECONDITION, VERB_TABLE
from ..data.rosters import (
    ABSENT_PREDICATE, AFFILIATIONS, CHANNEL_CLAIM_SOURCE, COVERT_KINDS, PERSON_PREDICATES, PROOF_KIND_OF_SOURCE, remove_distance, CRISIS_BANDS, DEGREE_STEP, DOMINANCE_KINDS, MATTERS, PERSON_DIED, PURSUIT_AXES, RECORD_CONTENT, REGARD_UNITS, SCAR_HOLDS, SEEN_PREDICATE, SELF_BELIEVED, capability_rows, require_use_site,
    roster, roster_map, task_share,
)
from ..state.carriers import Claim, Person, PersonInterior, Said, fade_of
from .inputs import SIDE_SIGN, Item
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
    ([ASSUMPTION, H-192]), told or not; a `PAIRED_KINDS` claim is `referent`'s when its
    `seen.who` pairing names him (`deed_doer`, IN-58) -- the paired kinds are the ones whose subject
    may be the PATIENT, so the doer is read off the sighting's `who`, never the subject. A told paired claim
    is paired with the sighting told on its own chain at its own deposit (B11.22), so a deed heard second-hand
    names a doer only where the telling carried the hand (`Fixtures.told_pairing` `on`). Person-side (AX-2)."""
    seen = functools.cache(lambda: _seen_index(ledger))
    for c in ledger:
        if not is_deed(c):
            continue
        if c.predicate in PAIRED_KINDS:
            if deed_doer(c, seen()) != referent:
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
    step 20's called bluff): the `PAIRED_KINDS` claims whose subject is `patient` and whose
    `seen.who` pairing names a doer (`deed_doer`, which never names the subject himself). Only a paired
    kind has a patient on its claim; an unpaired kind's subject is its doer (H-192), so it is never a
    deed suffered. A told copy names a doer only where its telling carried the hand (B11.22, `Fixtures.told_pairing` `on`):
    what a holder was only told of, with no hand, does not count. Person-side (AX-2)."""
    seen = functools.cache(lambda: _seen_index(ledger))
    for c in ledger:
        if (c.subject == patient and is_deed(c) and c.predicate in PAIRED_KINDS
                and deed_doer(c, seen()) is not None):
            yield c


def attackers_of(ledger, patient: str, kinds: frozenset, window: int = 1, strata=None) -> frozenset:
    """WHO THE HOLDER SAW DO A DEED OF ONE OF `kinds` TO `patient` IN THE NEWEST `window` SEASONS HIS LEDGER
    HOLDS (v11 CR-87, the DEFENCE context of `rosters.yaml: violence_contexts`): the doers `deed_doer` pairs to
    `suffered_deeds`' claims, kept when the claim is among `recent_claims(ledger, window)` (anchored on his newest
    claim, so `window == 1` is "this season" as he knows it) and its kind is in `kinds` (the caller's: the kinds an
    opponent-rule row emits). Person-side (AX-2); what he was only told of is not what he SAW: a told deed (`chain`) is skipped here, whatever hand its telling carried (B11.22).

    `strata`, where given, keeps a doer only if the holder saw him act at one of them ON THIS DEED'S SUBJECT in that deed's lap. A kind several rows emit
    (`capability.raised`: `fight` and `train`) pairs on any of its emitters' strata, so a benefit and a blow carry the same kind;
    the caller that asks for ATTACKERS passes the strata of its violent rows. B05.09 made `train` reach people who held no rank,
    and `p_npc_004`'s training of `p_npc_038` read as an attack."""
    if not kinds:
        return frozenset()
    recent = {id(c) for c in recent_claims(ledger, window)}
    seen, out = None, set()
    for c in suffered_deeds(ledger, patient):
        if id(c) in recent and c.predicate in kinds and not c.chain:
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
    `(who, when, lap) -> {(subject, stratum)}` -- what the holder saw each actor act on, the inverse of the first (B10.20: `deed_counterparty`);
    and a FIFTH, the TOLD sightings, `(subject, when, lap, chain) -> [seen]` (B11.22): the sighting a telling carried beside a deed, deposited with the
    deed's own `when`, `lap` and chain, so a told deed is paired with the sighting of its own telling and never with the holder's own."""
    by_subject: dict = {}
    acting: dict = {}
    hand: dict = {}
    acted_on: dict = {}
    told: dict = {}
    for s in ledger:
        if s.predicate == SEEN_PREDICATE and s.chain:
            told.setdefault((s.subject, s.when, s.lap, s.chain), []).append(s)
        elif s.predicate == HAND_PREDICATE and not s.chain:
            hand.setdefault((s.subject, s.when, s.lap), set()).add(s.value)
        elif s.predicate == SEEN_PREDICATE and not s.chain:
            by_subject.setdefault((s.subject, s.when, s.lap), []).append(s)
            who = getattr(s.value, "who", None)
            if who is not None:
                acting.setdefault((s.when, s.lap), set()).add((who, getattr(s.value, "stratum", None)))
                acted_on.setdefault((who, s.when, s.lap), set()).add((s.subject, getattr(s.value, "stratum", None)))
    return by_subject, acting, hand, acted_on, told


def deed_doer(c, seen: tuple):
    """v9 IN-58's PAIRING RULE: WHO DID THE DEED `c` TO ITS SUBJECT, as the holder saw it, or `None`.

    `c` is a deed claim `(s, kind, True)` of a `PAIRED_KINDS` kind; `seen` is
    `_seen_index` of the same ledger. A TOLD `c` (`chain`, B11.22) is paired with the sightings TOLD on its own chain at its own `when` and `lap`
    (`seen[4]`) and with nothing else -- never the holder's own sightings -- by the refusals below that apply to a sighting alone (a `who` withheld,
    two different `who`, a stratum the kind's rows do not carry); a telling that carried no pairing leaves nothing to pair, so it names nobody. For an
    untold `c`, a `seen` claim PAIRS with it when it has the same subject
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
    if not is_deed(c) or c.predicate not in PAIRED_KINDS:
        return None
    by_subject, acting, hand, _, told = seen
    strata = _KIND_STRATA[c.predicate]
    if c.chain:
        return _named_hand(told.get((c.subject, c.when, c.lap, c.chain), ()), c.subject, strata)
    if c.predicate == PERSON_DIED and (c.subject, c.when, c.lap) in hand:
        named = hand[(c.subject, c.when, c.lap)]
        return next(iter(named)) if len(named) == 1 else None
    if any(who == c.subject and st in strata for who, st in acting.get((c.when, c.lap), ())):
        return None
    return _named_hand(by_subject.get((c.subject, c.when, c.lap), ()), c.subject, strata)


def _named_hand(sightings, subject: str, strata: frozenset):
    """THE ONE `who` THE `sightings` OF A DEED ON `subject` NAME, or `None`: `deed_doer`'s two pairings (the holder's own, and a told deed's own telling) read it
    alike. A sighting that names no `who` makes the pairing ambiguous, so `None`: an unnamed hand may be the one that did it. A `who` that is the subject, or a
    stratum the kind's rows do not carry, names nobody; two different `who` are `None`."""
    whos = set()
    for s in sightings:
        who = getattr(s.value, "who", None)
        if who is None:
            return None             # an actorless sighting on the same key: ambiguous, never guess
        if who == subject or getattr(s.value, "stratum", None) not in strata:
            continue
        whos.add(who)
    return next(iter(whos)) if len(whos) == 1 else None


def paired_sighting(c, seen: tuple):
    """THE `Seen` VALUE THAT NAMES THE DOER `deed_doer` GIVES THE DEED `c`, as the holder holds it, or `None` (B11.22): the sighting a teller passes on beside the
    deed -- the holder's own for an untold `c`, the one told on `c`'s own chain for a told one (so a hand survives a retelling). `None` where the deed names no
    doer, or where the doer is named by a `fell_to_hand` claim, which is no sighting."""
    doer = deed_doer(c, seen)
    if doer is None:
        return None
    sightings = seen[4].get((c.subject, c.when, c.lap, c.chain), ()) if c.chain else seen[0].get((c.subject, c.when, c.lap), ())
    strata = _KIND_STRATA[c.predicate]
    return next((s.value for s in sightings
                 if getattr(s.value, "who", None) == doer and getattr(s.value, "stratum", None) in strata), None)


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
    out: list = []
    for _c, doer in _named_deeds(ledger, spec, holder, against):
        if doer not in out:
            out.append(doer)
    return tuple(out)


def _named_deeds(ledger, spec: dict, holder: str, against=()):
    """`(claim, doer)` FOR EACH DEED CLAIM `spec` SELECTS THAT NAMES A DOER OTHER THAN THE HOLDER, in ledger order -- `deed_doers`' one reading (its docstring is the
    rule), kept as a generator so a second reader asks the same question of the same claims and never re-derives it (B11.73's `_concluded`)."""
    form = next((f for f in roster_map("goal_object_kinds", "forms")["deed_doers"] if f in spec), None)
    if form is None or (form == "against" and not against):
        return
    kinds = frozenset(spec["kinds"]) if form == "kinds" else frozenset()
    seen = None
    engages: dict = {}                     # kind -> bool, per call: the tables are rebound by tests
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
        if doer is not None and doer != holder:
            yield c, doer


def _concluded(ledger, holder: str, kinds):
    """`(deed claim, the one it was done to, doer)` FOR EACH DEED OF `kinds` THE LEDGER LETS THE HOLDER CONCLUDE OF, in ledger order (B11.73, FRES §7 (1); `08_FI_03` §3 act 1):
    the value space of `reconstruct`'s conclusion (U-7). `deed_doers`' reading of `kinds` (`_named_deeds`: the doer his ledger names, never himself, never a guess), each
    filed under the one the deed was done to. A `PAIRED_KINDS` claim is about that one (its subject, the patient) and its doer is the sighting's; an unpaired deed of a
    Person-subject kind is filed under the counterparty `deed_counterparty` reads off his sightings. Any other unpaired kind names no one it was done to (its claim's subject
    is its doer, H-192) and concludes nothing here -- the pairing never guesses. Nothing wrong is deposited by a roll (K-37): a wrong name is a wrong ledger. Holder-side and
    World-free (AX-2). A generator, so the readers of a conclusion (`conclusion_cites`, `concluded_cells`) ask the same question of the same claims (B11.75)."""
    seen = None
    for c, doer in _named_deeds(ledger, {"kinds": kinds}, holder):
        if c.predicate in PAIRED_KINDS:
            to = c.subject
        elif c.predicate in PERSON_SUBJECT_KINDS:
            seen = _seen_index(ledger) if seen is None else seen
            to = deed_counterparty(c, seen)
        else:
            continue
        if to is not None:
            yield c, to, doer


def conclusion_cites(ledger, holder: str, kinds) -> dict:
    """`{(the one the deed was done to, deed kind, doer): (the ids of the deed claims that name him, in ledger order)}` -- what each conclusion `_concluded` reads rests on
    (B11.75, R-19-04's `cites`: the claims that name him). The claim cited is the DEED claim `_named_deeds` read the doer off (for a paired kind it is paired with the sighting
    that carries the hand, for an unpaired kind its subject is the doer): the holder holds it, so a later `utter` may cite it (`_held_cites`)."""
    out: dict = {}
    for c, to, doer in _concluded(ledger, holder, kinds):
        ids = out.setdefault((to, c.predicate, doer), [])
        if c.id not in ids:
            ids.append(c.id)
    return {k: tuple(ids) for k, ids in out.items()}


def cited_support(ledger, cites, weigh=None, *, tick: int = 0, decay: int = 0) -> float:
    """HOW WELL SUPPORTED A CONCLUSION IS BY THE CLAIMS IT CITES, in `[0, 1]`: `LedgerReader._support` over those claims -- `1 - PROD over distinct origins (1 - weigh(c))`, one
    origin counting once at its highest weight, so a doer named by two independent tellers stands higher than one named by a single one repeating himself (B11.75, R-19-04). `0.0`
    for a cite the ledger does not hold. `weigh` is `ledger_weigh`'s: `None` weighs every claim 1.0, so any held cite is support 1.0 (`_support` at `weigh == 1`). The cites
    of one conclusion share a predicate and a value (a deed kind, `True`), so they form one group and the first entry is the answer."""
    ids = set(cites)
    matches = [c for c in ledger if c.id in ids]
    if not matches:
        return 0.0
    if weigh is None:
        return 1.0
    return LedgerReader(ledger, weigh, tick=tick, decay=decay)._support(matches)[0]


def concluded_cells(ledger, holder: str, kinds) -> list:
    """THE HOLDER'S OWN READING OF WHO DID A DEED, AS THE CELL A CONCLUSION IS TOLD AS: one claim `(the one it was done to, concluded:<kind>, doer)` per resolved deed in
    `ledger` (`_concluded`; a `Claim` carrying the deed claim's own id, `when`, `source` and `confidence`), for `record`'s pairing of a told conclusion against what he saw
    (B11.75). The caller passes the holder's UNTOLD claims: a conclusion is checked against what he saw, never against what he was told. No claim is stored."""
    return [Claim(c.id, holder, to, f"{_verbs.CONCLUDED_STEM}:{c.predicate}", doer, c.when, c.source, c.confidence, "own", c.lap)
            for c, to, doer in _concluded(ledger, holder, kinds)]


def paired_deed_term(p: Person, axis_w: dict, c, seen_of) -> tuple:
    """`(doer, term)`: THE ONE SCORER OF A PAIRED DEED CLAIM (v9 IN-58, IN-72; `CLAUDE.md` §8, the rule
    lives once). `c` is a deed claim `p` holds; `axis_w` is `p`'s projected pursuits; `seen_of` is a
    zero-argument callable returning `_seen_index(p.ledger)` (called only when a pairing is read).
    `doer` is the one `deed_doer` names and `term = lean · bond` (`_lean`, `_bond`) is what the deed
    adds to `p`'s judgement of that doer; `world_q.attention_key`'s tier 2 ranks a claim by `|term|`
    (`deed_term` is the same number for `deeds_judged` and `world_q.reception`). `(None, 0.0)` for every claim that is not a paired deed, that `p`'s
    pursuits do not lean on, or whose pairing names no doer (no `seen`, `who`
    withheld, ambiguous; a told claim is paired with the sighting its telling carried, B11.22): an unpaired claim scores 0, so a hidden actor stays hidden. Person-side (AX-2)."""
    if c.predicate not in PAIRED_KINDS:
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


# THE FAMILY OF EVENT KINDS A QUESTIONING EMITS (`verb_table.yaml: interrogate`'s `emits`: `confession.full`, `.made`, `.partial`, `.withheld`): a deed claim
# of one is a confession, not testimony. A family prefix and not a list, so a kind the table adds to it is read as one without an edit here.
CONFESSION_FAMILY = "confession."

# THE BAND EACH CONFESSION KIND IS EMITTED AT, read off the `interrogate` row's `emits:` (one kind per band), so no kind is spelt twice and a band the table moves is followed.
_INTERROGATE = _verbs.VERB_TABLE.get("interrogate")
CONFESSION_BAND = {k: d for d, ks in (_INTERROGATE.emits_by_degree.items() if _INTERROGATE else ()) for k in ks if k.startswith(CONFESSION_FAMILY)}


def proof_weight(c) -> Fraction:
    """HOW MUCH OF A PROOF A HELD CLAIM IS (B24.23, CF-E8-4): `0` for a claim that is no proof (`proof_kind` is `None`), the share of its band
    (`rosters.yaml: task_fraction` through `task_share`) for a `confession.*` deed -- full and made 1, partial 0.5, withheld 0 -- and `1` for any other proof.
    [ASSUMPTION: the confession's weight by band is the case-file share table's (`task_fraction`: Overwhelming and Success 1, Partial 0.5), as
    `14_VERBS_SOCIAL2_C_case_question_confession.md` §5 weights the case-file entry; a `confession.*` kind the table emits at no band reads the full 1]. World-free."""
    if proof_kind(c) is None:
        return Fraction(0)
    return task_share(CONFESSION_BAND.get(c.predicate)) if c.predicate.startswith(CONFESSION_FAMILY) else Fraction(1)


def proof_kind(c) -> Optional[str]:
    """WHAT KIND OF PROOF A HELD CLAIM IS -- A `matters` MEMBER, DERIVED FROM THE CLAIM AND NEVER DECLARED (FI_05_B E-1; the one reader, World-free). A DEED CLAIM (`is_deed`, a `Claim`
    or a told `Said`) of the `confession.` family is `confession`; any other deed claim is `testimony`, told or not: how far it has travelled is `decision/options.py::teller_weight`'s
    WEIGHT (`told_weight ** hops`), never a kind. A claim that is no deed (a cell, a refusal kind, a value that is not `True`) is no proof: `None`.
    A CONFESSION THAT WAS WITHHELD IS NO PROOF EITHER (B24.23, H-311): a `confession.*` kind whose band's share is zero (`proof_weight`; `confession.withheld`, emitted at
    `Failure`) reads `None`, so a prisoner who gave nothing is not worse off than one never questioned. The kind is derived from the band's share, not from a spelt kind.
    A Record's kind (`record`) and an edge's (`oath`, cited by its Tenure id) are the host's hold check, not a claim's, so this reader never answers them.
    [ASSUMPTION: E-1's "about its own subject" is not tested -- the claim carries no second subject to compare, so a `confession.*` deed is `confession` wherever held; `world_q.proofs`
    already reads only the opponent's own deeds (`attributed_deeds`)]
    ⚠ `rosters.yaml: proof_kind_of_source` also names a kind per claim, by SOURCE (`world_q.proofs`' admission filter, `dossier`'s `proof_kind` column, `sigma._items_of`): the two disagree
    (a `told_by` claim is `record` there, `testimony` here). B24.25 DECIDED: a citing speech's admission (`world_q.filings`, and so the case file's exhibits) reads THIS reader, the one derived from the
    claim; `proof_kind_of_source` is the ledger arm's mapping (`Fixtures evidence_from: ledger`, the control) and is read by no filing."""
    if not is_deed(c):
        return None
    if not c.predicate.startswith(CONFESSION_FAMILY):
        return "testimony"
    return "confession" if task_share(CONFESSION_BAND.get(c.predicate)) else None


def impeaches(c, record_id: str) -> bool:
    """DOES A HELD CLAIM IMPEACH THE DOCUMENT `record_id`? A deed claim (`is_deed`) whose subject is the Record and whose kind is a `rosters.yaml: covert_kinds` member
    (today `record.forged`, which a finder who graded `Partial` or better deposits, `loop/witness.py::_found_claims`). World-free: it reads the claim and the id. The told
    copy keeps its subject (the kind is unpaired), so a hearer of the finder's telling impeaches too."""
    return is_deed(c) and c.subject == record_id and c.predicate in COVERT_KINDS


def deed_valence(axis_w: dict, c) -> float:
    """How a holder whose projected pursuits are `axis_w` judges one deed claim `c`:
    `Σ_axis axis_w[axis] · align_kind(c.predicate, axis)`; 0 for a claim that is no deed, and 0 for
    a `PAIRED_KINDS` claim, whose valence enters only for its doer through `deeds_judged`'s pairing
    (v9 IN-58) -- never for the claim's subject, who may be the patient. The one scoring of a deed,
    read by `deeds_judged` (G1), `said_of`'s slant (G3) and `world_q.attention_key` (IN-57)."""
    if not valenced_deed(c):
        return 0.0
    return _lean(axis_w, c.predicate)


def valenced_deed(c) -> bool:
    """A DEED CLAIM WHOSE VALENCE IS ITS OWN: a deed (`is_deed`) of a kind that is not `PAIRED_KINDS`. The one test `deed_valence` and `deed_align` ask."""
    return is_deed(c) and c.predicate not in PAIRED_KINDS


def deed_align(c, axis: str) -> float:
    """ONE AXIS OF `deed_valence`: `align_kind(c.predicate, axis)` for a valenced deed claim, else 0. `deed_valence(axis_w, c)` is `Σ_axis axis_w[axis] · deed_align(c, axis)`;
    the chooser scores the claim a telling passes on by it (v12 B11.10, `decision/choose.py::choice_lean`), through the same weights as any choice value."""
    return _verbs.align_kind(c.predicate, axis) if valenced_deed(c) else 0.0


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
    deliberate: `queries/person_q.py::teller_weight` asks for REGARD, so when the gains move, the
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
    -- firsthand and told alike, because R7's channel is the news: legitimacy falls where the news of a deed has
    reached. A paired kind (`person.died`, `body.changed`) told with its hand counts as the claim that names its doer does
    (`deed_doer`; B11.22). Each deed is scored by its one owner (`deed_term`; `attributed_deeds` decides
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
        -1, 1)` -- `regard`, the one owner, normalised exactly as `queries/person_q.py::teller_weight`
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
    (`queries/person_q.py::teller_weight`) and passes it in as a closure. With
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
        ledger to one cell (`person_q._pair`) and wants `read`'s ordering without reaching
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
    reading of the teller, `queries/person_q.py::ledger_weigh`, built by the caller and passed in) puts it at or above
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
TOLD_PAIRING_ARMS = roster("told_pairing_arms")


def told_pairing_on(fx) -> bool:
    """IS `Fixtures.told_pairing` `on` (B11.22, `H-495`), held to `rosters.yaml: told_pairing_arms`: an unknown arm raises, `_slant`'s rule."""
    arm = fx.get("told_pairing")
    if arm not in TOLD_PAIRING_ARMS:
        raise ValueError(f"told_pairing {arm!r} is not in rosters.yaml: told_pairing_arms {sorted(TOLD_PAIRING_ARMS)} (H-495)")
    return arm == "on"


def _slant(fx) -> str:
    """`Fixtures.said_slant`, held to `rosters.yaml: said_slants` (`H-196`): an unknown arm raises
    rather than silently reading the control. `ValueError` for this module's reason
    (`_check_intent_claim`'s: the AX-2 allow-list)."""
    arm = fx.get("said_slant")
    if arm not in SAID_SLANTS:
        raise ValueError(f"said_slant {arm!r} is not in rosters.yaml: said_slants "
                         f"{sorted(SAID_SLANTS)} (H-196)")
    return arm


#: THE TIERS an `unshared_first` pick reads, in the vocabulary `rosters.yaml: said_slants` `arms.<arm>.prefers` names them (v12 B11.09, `08_FI_02`
#: edit 2). Each is a test of one claim; the roster says their ORDER and a name not here refuses at import (`_load_slant_arms`). `deed` is `is_deed`
#: (what a witness of the act deposits: a kind some row emits and none emits on refusal, `DEED_KINDS`, derived); `quantity` is a claim on a stem of
#: `data/verbs.py: QUANTITY_STEMS` (v12 B11.52, `16_PESSIMIST_FI_A` edit 5: what a rumour may garble and a liar may move), so an existence reading
#: (`exists:*`, stored 0/1) is in no tier but `other`.
_SLANT_TIERS = {
    "told": lambda c: bool(c.chain),
    "inferred": lambda c: c.source == "inferred",
    "deed": is_deed,
    "quantity": lambda c: str(c.predicate).partition(":")[0] in _verbs.QUANTITY_STEMS,
    "other": lambda c: True,
}


def _load_slant_arms(arms: dict, values, verb_table, tiers) -> dict:
    """`rosters.yaml: said_slants` `arms:`, checked and resolved: `{arm: (excluded predicates, tier order)}`. REFUSED AT IMPORT (`ValueError`, this module's
    reason: `_check_intent_claim`'s) when an arm is not one of `values`, an `excludes_kinds_of` member is no verb of the table (`lie_verbs`' rule,
    `data/verbs.py::_load_lie_verbs`), or a `prefers` member is no tier. The excluded predicates are DERIVED: every kind those rows emit, on success or on
    refusal, so a row that gains a kind is excluded with it."""
    out = {}
    for arm, spec in arms.items():
        if arm not in values:
            raise ValueError(f"rosters.yaml: said_slants.arms names {arm!r}, which is not one of its values {sorted(values)}")
        excluded = set()
        for v in (spec or {}).get("excludes_kinds_of") or ():
            row = verb_table.get(v)
            if row is None:
                raise ValueError(f"rosters.yaml: said_slants.arms.{arm}.excludes_kinds_of names {v!r}, and the verb table carries no such verb")
            excluded |= {*row.emits, *row.emits_on_refusal}
        prefers = tuple((spec or {}).get("prefers") or ())
        bad = [t for t in prefers if t not in tiers]
        if bad:
            raise ValueError(f"rosters.yaml: said_slants.arms.{arm}.prefers names {bad}, which are no tier of `_SLANT_TIERS` {sorted(tiers)}")
        out[arm] = (frozenset(excluded), prefers)
    return out


SLANT_ARMS = _load_slant_arms(roster_map("said_slants", "arms"), SAID_SLANTS, _verbs.VERB_TABLE, _SLANT_TIERS)


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

    ⚠ SLANT `unshared` / `unshared_first` (v12 B11.09, `08_FI_02` edit 2-3, `rosters.yaml: said_slants` `arms:`): the pool first drops every claim whose
    predicate is a kind the `tell` or `lie` row emits (a telling is not passed on as news of itself), and `unshared_first` then narrows it to the first
    non-empty tier of its `prefers:` (`_SLANT_TIERS`) before the same comparator picks. Neither reads a ledger but the teller's or spends a draw.

    ⚠ B09.07 `weigh`: the closure the one comparator ranks by (`queries/person_q.py::ledger_weigh`, passed in by the caller), handed to `LedgerReader` as `epistemic.belief_contradicts` hands it, so a person
    passes on the belief he acts on. `None` (a hand-built read) is the plain comparator. ⚠ `LedgerReader._support`
    under a `weigh` ranks `latest_about` ACROSS predicates: a person passes on what he is SUREST of about a subject, not
    the newest thing he holds (decided at B09.07, `16_PESSIMIST_SC_B`).

    ⚠ B11.22 (`08_FI_06` edit 2, `Fixtures.told_pairing` `on`): the pool is also the deeds `subject` DID (`attributed_deeds`: a witness asked about K can say
    `(V, person.died, True)`), and a pick of a `PAIRED_KINDS` deed carries the sighting `deed_doer` pairs it with as `Said.pairing` (`paired_sighting`) -- his own, or
    the told one on the deed's own chain, so the hand survives a retelling. At `off` (the control) the pool and the `Said` are as they were."""
    # B10.65: A MAN'S OWN `self:<key>` CLAIM IS WHAT HE BELIEVES OF HIMSELF, NOT HEARSAY, so it is never offered as news about himself (the seeding would otherwise make every holder a teller of his
    # own motives). Only the claim he made himself is skipped (no chain, held by its subject): a `self:` claim he was TOLD (a chain) is deposited as any told claim and is still said.
    # B11.83 (`U5c_VERBS_residue` §3 step 3): AND A MAN'S `absent` CLAIM (what a refused `with` taught HIM, `rosters.yaml: absence_claim`) IS NEVER OFFERED: nobody
    # else learns it, so it is not news he passes on (a hearer holding it would be the second holder the deposit exists to forbid).
    pool = [c for c in claims if c.subject == subject and c.predicate != ABSENT_PREDICATE
            and not (c.predicate.startswith(_SELF_STEMS) and not c.chain and c.holder == subject)] if claims else []
    told_on = fx is not None and told_pairing_on(fx)
    if told_on and claims:
        # B11.22 (`08_FI_06` edit 2): AT `told_pairing` `on` THE POOL ALSO HOLDS THE DEEDS `subject` DID (`attributed_deeds`, the one owner), so a
        # witness asked about K can say the death of V that K's hand did. Ledger order is kept: the comparator's tie goes to the first found.
        kept = {id(c) for c in pool} | {id(c) for c in attributed_deeds(claims, subject)}
        pool = [c for c in claims if id(c) in kept]
    if teller is not None and fx is not None and pool and _slant(fx) == "valence":
        axis_w = projected_axes(teller, fx.get("scar_weight_shift"), hold=fx.get("scar_hold"), mass=fx.get("scar_primary_mass"))
        strength = {id(c): abs(deed_valence(axis_w, c)) for c in pool}
        top = max(strength.values())
        if top > 0:
            pool = [c for c in pool if strength[id(c)] == top]
    if fx is not None and pool and _slant(fx) in SLANT_ARMS:
        # `unshared` / `unshared_first` (v12 B11.09): the transport's own kinds leave the pool; then, at an arm with `prefers`, the pool is narrowed to the
        # first non-empty tier of the claims that are not a `seen` one (a `seen` claim stays the last resort below). No ledger but the teller's, no draw.
        excluded, prefers = SLANT_ARMS[_slant(fx)]
        pool = [c for c in pool if c.predicate not in excluded]
        live = [c for c in pool if c.predicate != SEEN_PREDICATE]
        for tier in prefers:
            hit = [c for c in live if _SLANT_TIERS[tier](c)]
            if hit:
                pool = hit
                break
    reader =LedgerReader(pool, weigh, tick=tick, decay=0 if fx is None else fx.claim_decay())
    # ABSENT: H-198 deception  (an `absent` hole row, read by harness/register.py; nothing reads this marker)
    # The pool holds the subject's claims, and at `told_pairing` `on` the deeds he did: its members are what is asked, so no second subject test is made.
    c = reader._best(lambda c: c.predicate != SEEN_PREDICATE) or reader.belief_among()
    if c is None:
        return None
    # B11.22 (`08_FI_06` edit 2): A PAIRED DEED CARRIES THE SIGHTING THE TELLER PAIRS WITH IT -- his own, or the one his telling carried to him.
    pairing = paired_sighting(c, _seen_index(claims)) if told_on and c.predicate in PAIRED_KINDS and is_deed(c) else None
    return Said(c.subject, c.predicate, c.value, reader.present(c), c.chain, pairing)


def said_set(claims, subject, fx, teller: "Person | None" = None, *, pick=None, tick: int = 0, weigh=None, choose: bool = True) -> tuple:
    """THE CLAIMS A TELLER MAY CHOOSE AMONG TO SAY ABOUT `subject`: the top `Fixtures.said_choices` of `pick`'s ranking (v12 B11.10, `08_FI_02` edit 7), best first.
    `pick` is `said_of` (the default) or `lie_said_of`, the one pick this repeats: it asks for the best, drops every claim of that predicate about the subject
    from what it reads, and asks again, until it has the number or the teller has nothing more to say (so each member is a different predicate). `said_choices` 1
    is `pick` asked once of the ledger itself, today's single pick exactly, with no copy of it. `lie_said_of` gives every false value of the claim it picks
    (v12 B11.54): the count is of claims, and each claim is said every way it has, best claim first. `()` is nothing to say. A value that is not a whole number of 1
    or more raises (`telling_privacy`'s rule). `choose` False (a row `rosters.yaml: choice_sourced` does not give `said`) is the single pick whatever the fixture."""
    n = fx.get("said_choices") if choose else 1
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError(f"said_choices {n!r} is not a whole number of 1 or more (B11.10)")
    pick = pick or said_of
    def picked(rest) -> tuple:
        # `said_of` gives the one `Said` or `None`; `lie_said_of` the tuple of every false value of the one claim it picked (v12 B11.54): both read as a tuple
        got = pick(rest, subject, fx, teller, tick=tick, weigh=weigh)
        return () if got is None else (got,) if isinstance(got, Said) else tuple(got)
    first = picked(claims)
    if not first:
        return ()
    out, rest, claims_said = list(first), claims, 1      # `n` counts CLAIMS; a claim may be said more than one way
    while claims_said < n:
        rest = [c for c in rest if not (c.subject == out[-1].subject and c.predicate == out[-1].predicate)]
        nxt = picked(rest)
        if not nxt:
            break
        out.extend(nxt)
        claims_said += 1
    return tuple(out)


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
    read by `lie_said_of` and `queries/person_q.py::record`'s pairing."""
    return str(c.predicate).partition(":")[0] in CELL_STEMS


def lie_said_of(claims, subject, fx, teller: "Person | None" = None, *, tick: int = 0, weigh=None) -> tuple:
    """WHAT THIS PERSON WOULD SAY FALSELY ABOUT `subject`: `said_of`'s pick, over the teller's CELL claims
    only, with its value made false -- a TUPLE of `Said`, every false value he may choose among, `()` where
    there is no false value to say (v11 CR-27, M9 taken (a), the cell lie; H-198 rule (i); v12 B11.54,
    `16_PESSIMIST_SC_E` edits 2-3: a lie about an amount is formed in both directions and the liar's own
    choice picks one). Asked of the LIAR'S OWN claims at CHOOSE
    (`decision/options.py::opening_set`, for a row named in `rosters.yaml: lie_verbs`) and carried on the
    Act's `payload["said"]`, so WITNESS deposits it through the one told channel and reads no ledger.

    THE FALSE-VALUE RULE [ASSUMPTION; medium; Jordan to correct; revert: a different false-value rule]:
      * an AMOUNT (a number on a stem of `data/verbs.py: QUANTITY_STEMS`) is moved one whole step of
        `told_drift_band`'s unit by `drifted`, in BOTH directions -- upward (`sel` 0) then downward (`sel` the
        step, `ceil(band * |held|)`, whose direction bit is the downward one): sign-preserving and never crossing
        zero, `_told_value`'s own clauses and not a copy of them. `drifted`'s clamp returns the upward value for
        a downward step that would reach zero, so the two collapse to one there (duplicates are dropped). A
        held 0, or a band of 0, has no false number to say: `()`.
      * any OTHER number (an existence reading stored as 0/1) is negated by truthiness, `0 if held else 1`:
        the one false thing to say of it (B11.51).
      * a TRUTH VALUE becomes the other member of its closed roster, `(False, True)`. No draw is spent: the
        roster of every non-numeric cell value a ledger holds today has two members, so the other member is
        the only one (a roster with several would be drawn on `draw(actor, 'lie:<act id>')`, and the act has
        no id at CHOOSE, so none is built; it would be a WITNESS-side change).
      * anything else -- a value that is neither -- has no roster: `()`.
    A claim that is no CELL (`data/requires.py: CELL_STEMS`: a deed kind, a `seen` sighting, a `content:` or
    `shortfall:` claim) is never lied about: the pool is cells only, so the DEED lie (H-198 rule (ii)) stays
    unbuilt. The chain is EMPTY: the liar is the origin of what he says, so the hearer's claim reads
    `(liar,)` and a falsehood is never fathered on whoever told the liar the truth.

    ⚠ A FALSE VALUE IS NEVER THE HELD ONE, so the hearer's exact-triple guard (`loop/witness.py`) does not
    drop the deposit for a hearer who holds the cell firsthand: his claim and the lie then DISAGREE, which
    is the pair `queries/person_q.py::record` counts against the liar (`H-183`).

    `weigh` (B09.07) is `said_of`'s: the one comparator the liar reads the cell he lies about by."""
    cells = [c for c in claims if c.subject == subject and is_cell(c)]
    said = said_of(cells, subject, fx, teller, tick=tick, weigh=weigh)
    if said is None:
        return ()
    held = said.value
    if isinstance(held, bool):
        falses = [not held]
    elif isinstance(held, (int, float)):
        if said.predicate.partition(":")[0] in _verbs.QUANTITY_STEMS:
            # an AMOUNT moves one whole step each way (v12 B11.54): `sel` 0 is upward, `sel` the step (`max_delta`) the downward selector
            band = fx.get("told_drift_band")
            step = math.ceil(band * abs(held))
            falses = [drifted(held, band, 0, whole_band=True), drifted(held, band, step, whole_band=True)]
        else:
            # an existence reading stored as 0/1 is negated by truthiness (v12 B11.51, `16_PESSIMIST_FI_A` edit 3)
            falses = [0 if held else 1]
    else:
        return ()
    out: list = []
    for false in falses:
        if false != held and false not in out:
            out.append(false)
    return tuple(Said(said.subject, said.predicate, false, said.confidence, ()) for false in out)


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


def content_value(subject_matter):
    """A `content:<kind>` CLAIM'S VALUE: the document's `subject_matter`, FROZEN -- a tuple of
    `(key, value)` pairs in the kind's own key order, every list a tuple, recursively. `dict(v)`
    gives the mapping back.

    ⚠ FROZEN AND HASHABLE ON `epistemic.Seen`'s PRECEDENT, AND FOR ITS REASON: claim values sit in
    the sets the corpus harness builds over `(subject, predicate, value)`
    (`harness/corpus_run.py`), and a `dict` there is a `TypeError`. Freezing is
    also what the deep copy was for: a belief that cannot be mutated cannot alias the Record it
    was read from, so nothing done to the document later reaches back into a ledger.

    B11.71: MOVED HERE FROM `loop/witness.py` (which imports it back, so `from ..loop.witness import content_value` still resolves) -- the
    fold's look at a Record (`world_q.WorldReader.look`, `content`) reads the same value a holder's deposit mints, and `queries/` may not import
    `loop/`. One owner, `content_said`'s neighbour."""
    if isinstance(subject_matter, dict):
        return tuple((k, content_value(v)) for k, v in subject_matter.items())
    if isinstance(subject_matter, (list, tuple)):
        return tuple(content_value(v) for v in subject_matter)
    return subject_matter


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


def ledger_range(claims, key: str) -> tuple:
    """THE IDS THIS HOLDER'S OWN CLAIMS PRESENT UNDER A CHOICE KEY, sorted (v12 B11.72, `rosters.yaml: choice_sourced`'s `ledger_ranges`: `site` for
    `examine`) -- the subjects of the claims whose predicate the key lists. A holder's own ledger and nothing else: no World, so an id is a Site
    here only as his claims say, and the fold's `existence` conjunct disposes of one that is not. The ONE reader of a ledger-sourced range, asked by
    `decision/options.py::opening_set`; never `known_persons`' sources (a claim about a person does not present a Site)."""
    preds = frozenset(_verbs.LEDGER_RANGES[key])
    return tuple(sorted({c.subject for c in claims if c.predicate in preds}))


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

    ⚠ THREE LIMITS, STATED; (1) AND (2) ARE OVER-INCLUSIONS THE FOLD CORRECTS, (3) IS AN UNDER-INCLUSION THE FOLD CANNOT. (3) Only the first two classes of `commands` are read (sworn men, holders of seats he may revoke), so `issue` and `dispatch` are never FORMED on an unseated, unsworn resident, A-22's third class, though the fold would admit one (`test_vb_d_orders.py` pins this). (1) An oath's claim names the man and never the seat he swore to
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


def _emitted_by(verbs) -> frozenset:
    """THE EVENT KINDS THE VERB ROWS `verbs` EMIT -- `data/verbs.py`'s own column, read, never spelt."""
    return frozenset(k for v in verbs for k in _verbs.VERB_TABLE[v].emits)


def _kinds_of_tenure(kind: str) -> tuple:
    """`(opened, exclusive)` FOR THE TENURE KIND `kind`: the kinds its DERIVED OPENERS emit (`data/verbs.py::
    _OPENERS_FROM_EFFECTS`, the one owner of *which verb opens which kind*), and those of them no verb outside
    the openers emits -- `confer` and `succeed` also emit the closing kind of the incumbent they displace, which
    `release` and `revoke` emit alone, so the closing kind is in the first set and not the second."""
    openers = frozenset(_verbs._OPENERS_FROM_EFFECTS.get(kind, ()))
    opened = _emitted_by(openers)
    return opened, opened - _emitted_by(frozenset(_verbs.VERB_TABLE) - openers)


#: THE KINDS A CLAIM ABOUT A SEAT OR RUNG CARRIES WHEN SOMEBODY CAME TO HOLD IT, and the one when he ceased to: the
#: `hold` openers' exclusive kinds, and the kinds a `hold` opener emits that a CLOSER also does -- a verb row that writes `Tenure.until` and opens no
#: tenure kind (`_OPENERS_FROM_EFFECTS`): `confer` and `succeed` emit the closing of the incumbent they displace (`tenure.closed`, which `release`,
#: `fight` and `accept` emit too). A death is `PERSON_DIED` (`data/rosters.py`). Derived, so a verb that opens a `hold` or closes one joins with no edit here.
_HOLD_EMITS, HOLD_OPEN_KINDS = _kinds_of_tenure("hold")
_OPENS_SOME = frozenset(v for vs in _verbs._OPENERS_FROM_EFFECTS.values() for v in vs)
HOLD_CLOSE_KINDS = _HOLD_EMITS & _emitted_by(v for v, r in _verbs.VERB_TABLE.items() if "Tenure.until" in r.writes and v not in _OPENS_SOME)
#: THE KINDS OF A PERSON'S OWN MOVEMENT, derived the same way from the `contain` openers (`move`, `march`, `migrate`, ...).
MOVE_KINDS = _kinds_of_tenure("contain")[1]


#: THE KINDS A SEAT'S FOUNDING EMITS (`rosters.yaml: seat_founding_kinds`): a claim of one about a seat says it exists with no holder, so `vacant_named` reads it as a
#: ceasing. Each must be a kind a verb that writes `Office.exists` emits, or the load refuses (a kind nothing emits would never be held).
SEAT_FOUNDING_KINDS = frozenset(roster("seat_founding_kinds"))
_FOUNDING_EMITS = _emitted_by(v for v, r in _verbs.VERB_TABLE.items() if "Office.exists" in r.writes)
if not SEAT_FOUNDING_KINDS or not SEAT_FOUNDING_KINDS <= _FOUNDING_EMITS:
    raise SystemExit(f"rosters.yaml: seat_founding_kinds {sorted(SEAT_FOUNDING_KINDS)} is empty or names kinds no verb writing `Office.exists` emits ({sorted(_FOUNDING_EMITS)})")


def _seat_news(ledger, obj) -> list:
    """`[(when, lap, predicate)]` OF EVERY CLAIM IN `ledger` ABOUT `obj` THAT SAYS SOMEBODY CAME TO HOLD IT OR CEASED
    TO, or THAT IT WAS FOUNDED EMPTY (`SEAT_FOUNDING_KINDS`), in ledger order. `vacant_named`'s read; `holders_named` reads its own."""
    return [(c.when, c.lap, c.predicate) for c in ledger
            if c.subject == obj and (c.predicate in HOLD_OPEN_KINDS or c.predicate in HOLD_CLOSE_KINDS or c.predicate in SEAT_FOUNDING_KINDS)]


def holders_named(ledger, obj) -> tuple:
    """THE PERSONS THE HOLDER'S OWN CLAIMS NAME AS HOLDING `obj` (a seat or a rung), newest first (v12 B11.08, `08_FI_01`
    edit 1; ED-IN-0292's last row: a fact about who holds a seat reaches a person as a claim through the channels, never as a
    world stamp). World-free: it reads `ledger` and the verb table's derived kinds, and nothing else.

    For each claim about `obj` whose predicate is a kind a `hold` opener emits (`HOLD_OPEN_KINDS`), the SUBJECTS of the claims of
    the same predicate deposited at the same `(when, lap)` -- the pairing key `deed_doer` and `_seen_index` use for a deed
    and its sighting, since WITNESS deposits every claim of one Event in one pass. A holder is dropped when a NEWER claim about
    `obj` carries a closing kind (`HOLD_CLOSE_KINDS`), a NEWER claim about him carries a death (`PERSON_DIED`), or a newer claim about him closes in
    the same `(when, lap)` as a closing claim about `obj` (one Event: his own release of it); a claim of the same key is not newer,
    so the seat's new holder survives the `tenure.closed` of the man he displaced.
    ⚠ OVER-INCLUSIVE, AND IT SAYS SO [ASSUMPTION; medium; Jordan to correct]: it cannot tell a person from another id by the
    ledger alone, so the seat itself is excluded and every other subject of the Event is named -- the conferrer beside the man
    conferred on (`claim_subjects`' `both`), and, when one person witnesses two seat changes in one lap, both holders. The reader
    that needs persons only (`world_q`'s call sites) drops the ids the world knows to be something else; it asks nothing of any
    person's state. Each holder once."""
    news = [c for c in ledger if c.predicate in HOLD_OPEN_KINDS or c.predicate in HOLD_CLOSE_KINDS or c.predicate == PERSON_DIED]
    # A closing claim ends the SEAT's holders at its `(when, lap)` (`seat_end`: the newest closing or death claim about `obj` itself -- the Event's one pass, the pairing key the
    # opener side uses; a witness of K's release of ANOTHER commitment holds `(K, tenure.closed, True)` at a newer key and says nothing of the seat). A holder's own closing claim
    # adds nothing the seat's does not (it ends his hold only at a key in `obj_close`, so never later than `seat_end`); only his DEATH ends it alone.
    seat_end = max({(c.when, c.lap) for c in news if c.subject == obj and (c.predicate in HOLD_CLOSE_KINDS or c.predicate == PERSON_DIED)}, default=None)
    ends: dict = {}
    for c in news:
        if c.predicate == PERSON_DIED and (c.when, c.lap) > ends.get(c.subject, (-1 << 60, 0)):
            ends[c.subject] = (c.when, c.lap)
    named: dict = {}
    for c in ledger:
        if c.subject != obj or c.predicate not in HOLD_OPEN_KINDS:
            continue
        key = (c.when, c.lap)
        if seat_end is not None and seat_end > key:
            continue
        for h in news:
            if h.predicate != c.predicate or (h.when, h.lap) != key or h.subject == obj:
                continue
            if ends.get(h.subject, (-1 << 60, 0)) > key:
                continue
            if h.subject not in named or key > named[h.subject]:
                named[h.subject] = key
    return tuple(sorted(named, key=lambda x: (-named[x][0], -named[x][1], x)))


def vacant_named(ledger, obj) -> bool:
    """WHETHER THE HOLDER'S OWN NEWEST CLAIM ABOUT `obj` THAT SAYS SOMEBODY CAME TO HOLD IT OR CEASED TO IS A CEASING (v12
    B11.08, `08_FI_01` edit 1's sibling): he has heard it empty. A seat he has heard nothing of is not named vacant, and at one
    `(when, lap)` an opening beside a closing reads occupied -- `confer` emits both when it displaces an incumbent."""
    news = _seat_news(ledger, obj)
    if not news:
        return False
    newest = max((w, l) for w, l, _ in news)
    return not any(p in HOLD_OPEN_KINDS for w, l, p in news if (w, l) == newest)


#: THE ARMS OF `Fixtures.telling_hearers` (`rosters.yaml: telling_hearer_arms`): who a teller offers a telling to.
TELLING_HEARER_ARMS = roster("telling_hearer_arms")


def present_persons(claims, actor) -> tuple:
    """THE PERSONS THIS HOLDER HAS SEEN SINCE HE LAST MOVED -- the subset of `known_persons` of whom he holds a FIRSTHAND `seen` claim
    naming (`Seen.who`) deposited at a `(when, lap)` no older than his own newest claim of a movement kind about himself
    (`MOVE_KINDS`), sorted ids, never `actor` (v12 B11.08, `08_FI_02` edit 5). The one reader of BELIEVED co-location: from his own
    ledger and nothing else, so a man who walked away this lap is still named and the fold refuses the telling (`tell`'s
    `hearer` conjunct). With no movement claim, every firsthand sighting counts. A told sighting never does: the person who
    was told where somebody is has not seen him.

    v12 B11.84 (`U5c_VERBS_residue` §3 step 2): A PERSON HIS NEWEST `absent` CLAIM SAYS IS NOT THERE IS LEFT OUT, until a NEWER firsthand
    sighting of him. The `absent` claim is the one a refusal on the `with` conjunct leaves its actor (`rosters.yaml: absence_claim`, deposited
    by `loop/witness.py`); the sighting must be strictly newer by `(when, lap)`, so a refusal read at the same moment as a sighting stands. A
    told claim never restores him (the line above: nothing told places a man here), and only the holder's own firsthand `absent` claim counts.
    The claim's value (the place) is not read: a sighting that counts here is already one since the holder last moved, so an `absent` claim
    older than the move is older than any sighting this reads."""
    term = KNOWN_PERSON_CLAIM.get("seen_term")
    moved = max(((c.when, c.lap) for c in claims if c.subject == actor and c.predicate in MOVE_KINDS and not c.chain), default=None)
    seen: dict = {}
    absent: dict = {}
    for c in claims:
        key = (c.when, c.lap)
        if c.predicate == SEEN_PREDICATE and c.source == "firsthand" and not c.chain and (moved is None or key >= moved):
            who = getattr(c.value, term, None)
            if key > seen.get(who, (-1 << 60, 0)):
                seen[who] = key
        elif c.predicate == ABSENT_PREDICATE and c.source == "firsthand" and not c.chain and key > absent.get(c.subject, (-1 << 60, 0)):
            absent[c.subject] = key
    return tuple(x for x in known_persons(claims, actor) if x in seen and seen[x] > absent.get(x, (-1 << 60, 0)))


def telling_hearers(claims, actor, fx) -> tuple:
    """THE PERSONS A TELLER OFFERS A TELLING TO, by `Fixtures.telling_hearers` (held to `rosters.yaml: telling_hearer_arms`; an unknown
    arm raises, `_slant`'s rule): `known` (the control, SHIPPED) is `known_persons`, `seen_since_move` is `present_persons`."""
    arm = fx.get("telling_hearers")
    if arm not in TELLING_HEARER_ARMS:
        raise ValueError(f"telling_hearers {arm!r} is not in rosters.yaml: telling_hearer_arms {sorted(TELLING_HEARER_ARMS)}")
    return present_persons(claims, actor) if arm == "seen_since_move" else known_persons(claims, actor)




# --- B11.21: moved byte for byte from `decision/options.py` (`agreement` .. `teller_weight`) and `epistemic.py` (`belief_contradicts`) ---
# `loop/witness.py` reads `ledger_weigh` and `refracted_confidence`, and `04` §C.3 has `decision/` import `person_q`, not the reverse: so the two
# functions and everything they call over a holder's own ledger live here, World-free (D-74, `08_FI_04` §6).

def belief_contradicts(p: Person, row: "VerbRow", subject: str, operands: dict,
                       via: "str | None" = None, weigh=None,
                       actor: "str | None" = None, tick: int = 0, decay: int = 0) -> bool:
    """§F1 clause 4 -- is `requires(verb)` KNOWN-FALSE from `p`'s OWN claims?

    ⚠ THE ASYMMETRY IS THE WHOLE POINT AND MUST NOT BE SOFTENED TO "requires holds". This returns
    True only when the person HOLDS A CLAIM THAT CONTRADICTS the requirement. Having no belief
    either way is NOT a contradiction, so the Candidate forms, the person acts on a false premise,
    and the fold refuses them -- which is §F1's "a person who *wrongly* believes the granary full
    still forms the Candidate ... That is T3 and L2 working."

    Jordan, 2026-09-02: *"we can't control how others perceive and interpret our words or
    actions"* and *"our understanding of all other words and actions is subjective and singular."*
    A filter on world truth would be `choose` reading the world; this reads one person's ledger.

    ⚠ `W-A`: IT ASKS THE VERB'S OWN TYPED CELL, NOT A ROSTER. A filter on
    `predicate in PERSON_PREDICATES and value is False` is a MEMBERSHIP TEST standing in for a
    requirement (`H-72`: the map from a requirement to a predicate), and the two vocabularies are
    DISJOINT, so clause 4 could not fire and the candidate set would be invariant with respect to
    everything that happened in the simulation (`H-116`). The predicate is DERIVED from the form
    (`stores:grain`, `condition`, `contain.path:D`), so there is one namespace and the write side
    has a name to aim at. `H-116`'s other half -- WITNESS depositing claims in that namespace -- is not this item.

    ⚠ AN UNTYPED VERB IS NOT CONTRADICTED. `evaluate(None, ...)` is UNKNOWN, and UNKNOWN is not
    False: a person cannot know a requirement fails when nothing states what the requirement is.
    That polarity is the OPPOSITE of the fold's, deliberately -- §F1 filters on belief and §42.2
    governs the resolver -- and the same `Verdict` carries both readings.

    ⚠ `W-C`: IT READS THE CANDIDATE'S OWN OPERANDS, WHICH IS WHAT MAKES THIS THE SAME QUESTION
    THE FOLD ASKS. `binding_from` would rebind `subject` onto whichever operand
    the cell called its entity -- so for `transfer` the person would ask *does the RECEIVER hold the
    grain*, and §54 item 7 asks about the GIVER's hearth: a different cell from the fold's and a
    defensible-looking answer to the wrong question. `operands` is the
    same bag the Act will carry, passed through the same `binding_of`, so the two sides differ
    only in WHAT THEY READ (one ledger, one world) and in POLARITY -- which is the difference
    that is supposed to be there.

    ⚠ PLAN POSITION `19`: AND THE SEAT, FOR THE SAME REASON. `via` is the seat the Candidate's act
    will be exercised through -- `decision/options.py::seat_of`, the value `pack_scenes` puts
    on `Act.via` -- and `binding_of` carries it exactly as `binding_from_act` does for the fold, so a
    `basis` conjunct (§F.24a form 7, `data/requires.py::Basis`) asks the person's ledger about THE
    SAME seat the fold will ask the world about. Omitted (`None`), the conjunct is UNKNOWN, which
    contradicts nothing.

    ⚠ TELLING WORKPLAN `T3a` (`ED-IN-0282`): `weigh` GRADES HEARSAY AS IT IS READ. `opening_set`
    passes `queries/person_q.py::teller_weight(p, fx)`, so a newer claim a teller passed on does
    not beat the person's own firsthand claim merely by being newer. The CLOSURE is passed in
    by the caller rather than built inside the reader, which keeps the reader one comparator. Omitted (`None`), the reader is unweighted.

    ⚠ v9 IN-15 / `H-201`: `actor` IS WHO THE CELL'S `actor` OPERAND BINDS TO, AND IT DEFAULTS TO `p`.
    The person choosing an act is its actor, so `opening_set` passes nothing. A WITNESS asking whether an act they saw could have happened is a
    different question -- *could THE ACTOR have done this, on what I hold* -- and answering it with
    `p.id` bound reads the witness's own granary instead of the actor's. The ledger stays `p`'s
    (the belief is the witness's); only the operand moves. `actor=None` is `p.id`, never "no
    actor": an empty binding would make every actor-bound form UNKNOWN, i.e. contradict nothing.

    ⚠ B09.01: `tick` AND `decay` ARE WHAT HE READS HIS CLAIMS AT (`LedgerReader`'s; `state/ledgers.py::present_confidence`):
    a stored `confidence` is what a claim was deposited at, and its fade is computed here, where it is read. Omitted, a
    hand-built ledger reads as deposited."""
    if (row.requires or "").strip() in NO_PRECONDITION:
        return False
    return evaluate(row.requires_typed, LedgerReader(p.ledger, weigh, tick=tick, decay=decay),
                    binding_of(p.id if actor is None else actor, operands, via)).value is False


def agreement(told: list[Claim], own: list[Claim], tick: int = 0, decay: int = 0) -> tuple:
    """§F4's `agreement`, DEFINED -- and defined over TWO CLAIM SETS, not over claims and
    convictions. Returns `(agreements, disagreements, paired_predicates)`.

    ⚠ V2 §F4 IS WRONG IN A WAY #353 NAMES AS ITS WORST FAILURE MODE. It writes
    `agreement(claims in p's own ledger where subject == p and source == told_by, p's own
    convictions)` -- the claim ledger against the convictions. #353 §9.3 is a table whose whole
    purpose is to keep those apart: the ledger holds what is **TRUE**, convictions hold what is
    **RIGHT**, evidence moves the first and argument moves the second, and *"WITNESS NEVER TOUCHES
    A BELIEF... This is the single most dangerous collision in the design."* A formula that scores
    agreement between them makes evidence bear on the moral layer, which is the collision itself.
    PLAN `W5` says as much: *"H-29's default is not injectable as written."*

    THE CORRECTION IS SMALL AND STAYS INSIDE §F4'S OWN ARGUMENT. §18.2 says standing is "the gap
    between what everyone reads off you and what you hold", and §F4 reads "what you hold" as
    convictions. Read it instead as WHAT YOU HOLD TRUE -- your own firsthand claims about yourself
    -- and both sides are the epistemic layer, the collision is gone, and all three properties §F4
    wanted survive: computable person-side, WRONG-ABLE (a liar moves your standing, which is T3),
    and no cross-holder read, so §20 is untouched.

    Claims are paired BY PREDICATE, on the `person_predicates` roster -- PLAN `W5`'s "defined
    predicate vocabulary". Without one, "pairing by predicate" is pairing on a free string."""
    agree, dis = _pair(told, own, lambda c: c.predicate, PERSON_PREDICATES, tick, decay)
    return agree, dis, agree + dis


def _pair(told: list[Claim], own: list[Claim], key: Callable[[Claim], Any],
          admit=None, tick: int = 0, decay: int = 0) -> tuple:
    """THE ONE PAIRING STEP: each `told` claim against `own`'s belief at the same `key`, `(agree, dis)`.

    `agreement` pairs by predicate on the `person_predicates` roster (`admit`); `record` pairs by
    `(subject, predicate)` over the cell predicates (`admit=None`, filtered by `record`). Both call
    this, so how a told claim is matched to what the hearer holds, and what counts as agreeing
    (`==`, whole-value), lives once.

    ⚠ THE MATE IS THE CLAIM `LedgerReader` CALLS THE BELIEF, NOT THE LAST ONE LISTED. Where `own`
    holds several claims at one `key`, the one paired against is `LedgerReader._best`'s -- most
    recent, then most confident -- because list order is the EVICTION sort (`state/ledgers.py`:
    `confidence x (when + 1)`), not an order of belief, and a second ladder here would score a
    truthful told claim against a belief the person no longer holds. A tie goes to the first
    listed, as `_best` has it."""
    by_key: dict = {}
    for c in own:
        if admit is None or key(c) in admit:
            by_key.setdefault(key(c), []).append(c)
    belief: dict = {}                   # key -> the claim `LedgerReader` would answer from
    agree = dis = 0
    for c in told:
        k = key(c)
        if k not in by_key:
            continue                    # nothing of your own to compare it against
        if k not in belief:
            belief[k] = LedgerReader(by_key[k], tick=tick, decay=decay).belief_among()
        mate = belief[k]
        (agree, dis) = (agree + 1, dis) if c.value == mate.value else (agree, dis + 1)
    return agree, dis


def contradicts(a: Claim, b: Claim) -> bool:
    """DO TWO CLAIMS CONTRADICT? THE PAIRING RULE'S ANSWER, EXPOSED ONCE: the same cell `(subject, predicate)` and a different value (`_pair`'s whole-value `==`, run on the cell key
    `record` and `dissents` pair a cell claim on). It is the one call of `_pair` the host (`dossier.against`, `world_q.contradicted_tellers`) and the modules ask, so none
    restates `==`. `decision/options.py` re-binds it by name (`options.contradicts`)."""
    return _pair([a], [b], lambda c: (c.subject, c.predicate), None)[1] == 1


@dataclass(frozen=True)
class DossierRow:
    """ONE CLAIM ON THE CASE BOARD (`11_GO_player_surface_contract_B.md` §5's fields). The rows that share `(subject, predicate, value)` are one GROUP and carry one `support`.
    `record` is the id of the document on his live `hold` this claim is the content of (a `content:<kind>` claim of a record he holds), else `None`; `proof_kind` is
    `rosters.yaml: proof_kind_of_source`'s kind for the claim's source (`""` where its way of holding is no kind of proof); `against` the ids of his other claims on
    the same cell that disagree with this one."""
    claim: Optional[Claim]
    record: Optional[str]
    proof_kind: str
    support: float
    against: tuple


def dossier(p: Person, subject: Optional[str] = None, fx: "Fixtures | None" = None) -> tuple:
    """WHAT HE HOLDS, GROUPED BY WHAT IT SAYS -- `DossierRow`s, the groups in the order each was first held, a group's claims in ledger order; `subject` keeps one subject's groups,
    `None` every group (`IS-B2-FI-04`, `08_FI_07` §3). EVERY CLAIM OF THE LEDGER IS IN EXACTLY ONE ROW. Reads his own ledger, `hold` Tenures and fade, never a World; writes nothing.

    `support` is `LedgerReader._support` over the group's claims, read under `ledger_weigh(p, fx, tick)` -- the closure clause 4 reads his ledger by -- so the board shows what his
    decisions weigh: `1 - PROD over distinct origins (1 - weigh(c))`, a doer named by two tellers standing above one named by a single teller repeating himself. With no `fx` (a
    hand-built read), or a ledger `ledger_weigh` takes the plain reader for, every claim weighs 1.0. `against` is `contradicts` over the claim's CELL (`is_cell`): a claim of any other
    shape (an event kind, a `seen` struct, a `content:` claim) names no cell and nothing it could disagree with."""
    tick, decay = fade_of(p)
    weigh = ledger_weigh(p, fx, tick) if fx is not None else None
    held = {t.object for t in p.tenures if t.kind == "hold" and t.live}
    groups: list = []                                   # [(subject, predicate, value), [claims]]; `==`, not hash: a value need not be hashable
    for c in p.ledger:
        if subject is not None and c.subject != subject:
            continue
        key = (c.subject, c.predicate, c.value)
        for g in groups:
            if g[0] == key:
                g[1].append(c)
                break
        else:
            groups.append((key, [c]))
    rows: list = []
    for _key, members in groups:
        support = 1.0 if weigh is None else LedgerReader(members, weigh, tick=tick, decay=decay)._support(members)[0]
        for c in members:
            rows.append(DossierRow(c, c.subject if content_kind(c) is not None and c.subject in held else None,
                                   PROOF_KIND_OF_SOURCE.get(c.source) or "", support,
                                   tuple(o.id for o in p.ledger if o is not c and is_cell(c) and contradicts(c, o))))
    return tuple(rows)


def deed_doer_claims(ledger, spec: dict, holder: str, against=()) -> dict:
    """`{doer: (the ids of the deed claims that name him, in ledger order)}`: `deed_doers`' answer, in its order, with what each rests on (`_named_deeds`, the one reading;
    B11.77's suspects line)."""
    out: dict = {}
    for c, doer in _named_deeds(ledger, spec, holder, against):
        ids = out.setdefault(doer, [])
        if c.id not in ids:
            ids.append(c.id)
    return {d: tuple(ids) for d, ids in out.items()}


# The ordinal is `data/rosters.py::REMOVE_ORDINAL`'s, built once there so the resolver-side `reception`
# reads the same ranks without importing decision code.


def channel_remove(channel: str) -> float:
    """HOW FAR FROM THE THING ITSELF A CHANNEL PUTS ITS WITNESS, in `[0, 1)`: `0` for presence, `(K-1)/K`
    for the most removed channel. REFRACTION's channel term (`refracted_confidence`, v9 IN-15).

        remove(ch) = k / K,         k = the place of `claim_source[ch]` in the ordinal of remove,
                                    K = how many distinct sources that ordinal holds

    ⚠ THE ORDINAL IS READ OFF THE ROSTER, NOT WRITTEN HERE. `rosters.yaml: witness_channels` is
    ordered strongest first and its note says the order follows `19_PLAN.md`'s ordinal of remove
    (*firsthand > knot-sourced > told > inferred*); the distinct `claim_source:` values in that order
    ARE the ordinal, so a channel's remove is its SOURCE's place. Two channels with one source
    (`document_key`, `chronicle`: both `told_by`) are equally removed, which keeps that note's
    *"the order decides only which channel is reported, never the source"* true of this term too.
    One spacing, `remove_distance`, read here and by `world_q.remove_weight` (`H-199`)."""
    return remove_distance(CHANNEL_CLAIM_SOURCE[channel])


def ledger_weigh(p: Person, fx: "Fixtures", tick: int = 0):
    """THE `weigh` `p` READS THEIR OWN LEDGER BY when asking `belief_contradicts` -- `teller_weight`,
    or `None` for a ledger holding no told claim AND no claim faded below `confidence_default` (`T3a`: such
    a ledger weighs 1.0 everywhere, which is the unweighted order exactly, tested, so it takes the plain
    reader; since B09.06 a ledger holding any faded claim gets the closure, told or not). One owner for both askers:
    `opening_set` (*may I do this*) and `dissents`' act-level term (*could the actor have done this*,
    `H-201`), so a person reads one ledger one way whichever question they put to it.

    ⚠ B09.06: AT `Fixtures.weigh_confidence` (`H-183`) THE CLOSURE ALSO WEIGHS HOW SURE HE STILL IS, so a ledger of his own
    claims takes it as soon as ANY claim has faded below `confidence_default` -- a ledger of fresh, full-confidence claims
    still weighs 1.0 everywhere and takes the plain reader, which reads as before. At `False` (the control, shipped until
    B09.08) the condition is today's: any told claim."""
    if any(c.chain for c in p.ledger):
        return teller_weight(p, fx, tick)
    if fx.get("weigh_confidence"):
        full, decay = fx.get("confidence_default"), fx.claim_decay()
        if any(present_confidence(c.confidence, c.when, tick, decay) < full for c in p.ledger):
            return teller_weight(p, fx, tick)
    return None


def dissents(p: Person, c: Claim, act=None, weigh=None, decay: int = 0) -> bool:
    """DOES WHAT `p` ALREADY HOLDS DISAGREE WITH `c`? REFRACTION's prior-belief term.

    `c` is a claim about to land in `p`'s ledger and not yet in it. Two priors, either of which
    dissents:

    1. ON THE CLAIM'S OWN KEY. The pairing is the tree's one pairing step, `_pair`, on the key the
       tree already pairs that kind of claim on -- no third key:
         * a claim ABOUT `p` on a `person_predicates` member: `agreement` -- §18.2's comparison of
           what others read off you against what you hold true of yourself, which is `AX-7`'s
           *"(2) IS REVISABLE BY (3)"* seen from the receiving end;
         * a claim on a CELL (`is_cell`): `record`'s pairing, `(subject, predicate)`;
         * anything else -- an event-kind claim (always `True`), a `seen` struct (each sighting a
           new value, so it would "disagree" with the sighting it reports), a `content:` claim --
           nothing, for the reason `record`'s docstring gives for not scoring those.
       FIRSTHAND only (empty chain, source `firsthand`), as in `agreement` and `record`: what you
       saw resists what you hear, and hearsay does not resist hearsay here.
    2. ON THE ACT IT REPORTS (`H-201`), when the caller passes `act` -- the act `c` says HAPPENED
       (`loop/witness.py` passes it for the event-kind and `seen` deposits of an act's own emission,
       never a refusal's). `p` dissents when their own ledger makes that act's `requires`
       KNOWN-FALSE FOR ITS ACTOR: `belief_contradicts` with `actor=act.actor`, on the act's own
       verb row, operands (its payload, as `binding_from_act` reads it) and seat (`act.via`) --
       the question `opening_set` asks of a Candidate, asked of somebody else's act, and never a
       second evaluation of `requires` against a ledger. The actor is BOUND, not defaulted: the
       default binds `p`, which asks *could I have done this* (a witness whose own granary is
       empty would doubt every transfer they saw). `weigh` is the reader's, `ledger_weigh`'s, as
       `opening_set` passes it -- so this prior reads the whole ledger, hearsay graded, unlike
       (1): it is the person's belief about the world, the one they choose by. [ASSUMPTION, `H-201`]"""
    own = [x for x in p.ledger if x.firsthand]
    tick = c.when                     # `c` lands now: the tick its holder reads his own claims at
    if c.subject == p.id and c.predicate in PERSON_PREDICATES:
        if agreement([c], [x for x in own if x.subject == p.id], tick, decay)[1] > 0:
            return True
    elif is_cell(c):
        if _pair([c], [x for x in own if is_cell(x)], lambda x: (x.subject, x.predicate), None, tick, decay)[1] > 0:
            return True
    if act is None:
        return False
    row = VERB_TABLE.get(act.verb)
    if row is None:
        return False
    pay = act.payload if isinstance(act.payload, dict) else {}
    return belief_contradicts(p, row, pay.get("subject"), pay, act.via, weigh=weigh,
                              actor=act.actor, tick=tick, decay=decay)


# v10 CR-19 / `H-200`: THE ATTRIBUTE `AX-7`'S COMPETENCE READS is a ROW, not a name here: `rosters.yaml: tables.capability_uses`'s
# `told_claim_credit` row (B04.06; `ED-IN-0327`: Attunement helps one judge whether someone is telling the truth), read by
# `_judgement_factor` through the substrate's `about_mid`. Nothing under `decision/` names an attribute or the scale's middle.
TOLD_CLAIM_CREDIT = require_use_site("told_claim_credit")


def _judgement_rows(use: str) -> list:
    """The `judgement` rows of site `use`, in table order."""
    return [r for r in capability_rows(use) if r.role == "judgement"]


def _judgement_factor(p: Person, rows: list, fx) -> Optional[float]:
    """THE `judgement` ROWS OF ONE SITE, as one factor about the scale's mid-point (B04.06; U1 §8), or `None` for NO CAPABILITY: `None` where
    there are no rows, or `p` holds no value at any row's key (a READ, never a default; the caller reads it as the factor 1). The value is
    `p.attributes` at the row's `key`, on `substrate.descriptors.scale_of(key)`; the form is `about_mid`, its `gain` the Fixture the row
    names (`fx.get(row.gain)`), so a sweep of that Fixture overrides the shipped value through `fx`. `side: actor` is the only side read:
    `p` is the actor (the loader refuses any other). A site with several rows multiplies them. Its three callers are `temper`, `nerve` (`decision/choose.py`) and `competence` (here), one per site."""
    factor = None
    for row in rows:
        held = (getattr(p, "attributes", None) or {}).get(row.key)
        if held is None:
            continue
        floor, ceiling = scale_of(row.key)
        one = about_mid(held, floor, ceiling, fx.get(row.gain))
        factor = one if factor is None else factor * one
    return factor


def competence(p: Person, fx) -> float:
    """`AX-7`'S THIRD INPUT, THE RECEIVER'S COMPETENCE, in `[0, 1]` (v10 CR-19; `H-200`).

        competence = min(1, 1 + g * (attunement - mid) / (mid - floor))      g = `fx.get(row.gain)`, the Fixture the
                                                                             `told_claim_credit` row names (`competence_gain`)

    `attunement` is the score `p.attributes` holds at the `told_claim_credit` row's key (`Person.attributes`, CR-20),
    `mid` the middle of that key's scale (`_judgement_factor`). MONOTONE in Attunement and exactly 1 at `mid`; a receiver who HOLDS no
    Attunement reads 1 (a READ, never a default). ⚠ The built realm (`boot/realm.py`) seats every key on every
    person (`cast_attributes=True`, drawn by `state/carriers.py::generated_attributes` where unauthored),
    so no realm receiver reaches that branch and each unauthored one reads the Attunement he drew, below `mid` for
    some. Harmless ONLY while `competence_gain`
    ships at 0: at `g = 0` it is 1 for everyone (THE CONTROL, and the shipped value); a live gain would lower
    the credit of every receiver drawn below `mid`.

    ⚠ CAPPED AT 1 ABOVE `mid` [ASSUMPTION; medium; Jordan to correct; revert: drop the `min` and clamp the
    product to a confidence ceiling, which no owner names]: the other two factors only ever LOWER a
    confidence (`refracted_confidence`'s docstring), and an uncapped factor would let a deposit land ABOVE
    the confidence it was told at, past any ceiling the tree defines. So a competent reader loses nothing
    and an incompetent one credits less.

    ⚠⚠ WHAT THIS FACTOR CANNOT DO, AND WHY IT SHIPS AT 0. `ED-IN-0327` (Jordan): *"attunement also helps
    you determine if someone is telling the truth"*. This factor scales EVERY told claim by the receiver's
    Attunement alone. A person-side reading cannot see whether a claim is true (`AX-7`: the performer's
    own understanding and everyone else's are separate objects, and a claim carries no truth value), and
    what `p` legitimately holds of the claim is only its channel, its teller, its confidence and `p`'s own
    prior (`dissents`) -- none of which separates a lie from a truth: a lie and a truth reach a receiver
    with no prior identically, and a receiver whose prior is wrong dissents from a truth exactly as one
    whose prior is right dissents from a lie. So a LIVE gain here would let a high-Attunement receiver
    hold a lie MORE firmly than a low one, the opposite of the ruling. Left to CR-27's `lie` (B10-13), which
    alone knows which told claims are false, and to CR-83's design, which must give the separator before the
    gain is flipped live (a declared hash mover scheduled by that design, not by this function). CR-27's
    second falsifier is the guard on that flip."""
    rows = _judgement_rows(TOLD_CLAIM_CREDIT)
    for row in rows:
        if not 0.0 <= fx.get(row.gain) <= 1.0:
            raise ValueError(f"{row.gain} {fx.get(row.gain)!r} is outside [0, 1] (H-200): a factor below 0 "
                             "would turn a deposit's confidence negative")
    factor = _judgement_factor(p, rows, fx)
    return 1.0 if factor is None else min(1.0, factor)


def refracted_confidence(p: Person, c: Claim, channel: str, gain: float,
                         act=None, weigh=None, fx=None) -> int:
    """REFRACTION -- `AX-7`'s divergence formula (v9 IN-15; `H-36`'s shape, `H-199`'s magnitude).
    How much `p` credits a claim landing in their ledger, from the channel it reached them by and
    what they already held:

        confidence' = floor( c.confidence * (1 - g * remove(channel))
                                          * (1 - g * dissent(p, c)) * competence + 1/2 )

    `g` is `refraction_gain`, in `[0, 1]`; `remove` is `channel_remove`; `dissent` is `dissents`, 0
    or 1 -- with `act` (the act `c` reports happening) and `weigh` passed through to its act-level
    term (`H-201`); `competence` is `competence(p, fx)` (CR-19, `H-200`: the receiver's Attunement, its gain the `told_claim_credit`
    row's Fixture, swept, 1 at the shipped gain 0; `fx=None`, a caller that hands no Fixtures, reads no row and the factor is 1). Each factor is in `[0, 1]`, so refraction only
    ever LOWERS a confidence, and at `g = 0` every factor is exactly 1: THE CONTROL, and the deposit
    is today's.

    ⚠ `H-36`'s SHAPE, KEPT: RECEIVER-SIDE, PER RECEIVER, AND NEVER THE EMISSION. Nothing here writes
    an Event or an Act; `act` is read only for `dissents`' act-level prior (H-201). It grades one
    person's copy as it lands, so two witnesses of one act hold it with different confidence and
    the act is untouched (`AX-7` layer (1)).
    ⚠ CONFIDENCE, NOT VALUE. `AX-7` allows either; what a copy may LOSE in its value is already
    owned (`loop/witness.py::_told_value`, r2 `02` §A.10), and a second value rule here would be a
    second owner of it. This is the axis no rule moved: every deposit took `confidence_default`, or
    the teller's own.
    ⚠ FROZEN AT DEPOSIT, UNLIKE `teller_weight`. CAT-3 grades a told claim WHEN READ because the
    hearer's relation to the teller can change later; the channel and the prior are facts of the
    moment the claim lands, and the carrier stores neither, so they are applied here, once. The two
    multiply into nothing shared: `teller_weight` never reads `confidence`.
    ⚠ THE PRODUCT IS THE SIBLINGS' METHOD (`teller_weight`'s `told_weight ** hops * relation *
    record`): the three inputs `AX-7` rules *"together"* each scale the credit independently."""
    if not 0.0 <= gain <= 1.0:
        raise ValueError(f"refraction_gain {gain!r} is outside [0, 1] (H-199): a factor below 0 "
                         "would turn a deposit's confidence negative")
    decay = 0 if fx is None else fx.claim_decay()
    factor = ((1.0 - gain * channel_remove(channel)) * (1.0 - gain * dissents(p, c, act, weigh, decay))
              * (1.0 if fx is None else competence(p, fx)))
    return int(c.confidence * factor + 0.5)


def _clamp(x: float, lo: float, hi: float) -> float:
    return lo if x < lo else hi if x > hi else x


def rank(p: Person, teller: str) -> int:
    """`+1` if `p`'s own claims say `teller` outranks `p`, `-1` if outranked, `0` if they say
    neither. ALWAYS `0` TODAY.

    The ordering itself exists -- `offices.yaml: titles` maps each title to a rung kind, and
    *"rank is the ordinal in `rung_kinds`"* -- but a hearer can only rank a teller off claims
    the HEARER holds, and no writer in the tree deposits an `office` claim (the `person_predicates`
    member is a vocabulary word with no producer), nor is an `office` claim's value typed as a title or a seat.
    Comparing values nobody writes, in a shape nobody declared, would be inventing the ruling."""
    # ABSENT: H-181 rank ordering  (an `absent` hole row, read by harness/register.py; nothing reads this marker)
    return 0


def _is_conclusion(c) -> bool:
    """A TOLD CONCLUSION THAT NAMES A DOER: a claim `(the one a deed was done to, concluded:<deed kind>, doer)` (`loop/witness.py`'s deposit; B11.73), its value a person -- the
    `Partial` band's claim has value `True` and names no hand, so it has nothing `record` can check (B11.75)."""
    return str(c.predicate).startswith(f"{_verbs.CONCLUDED_STEM}:") and c.value is not True


def record(p: Person, teller: str, fx: "Fixtures", tick: int = 0) -> float:
    """A TELLER'S RECORD WITH `p`: how often what `teller` told `p` matched what `p` holds firsthand
    (telling workplan `T6`, `ED-IN-0282`; E5).

        record = 1 + record_gain * (agree - dis) / (agree + dis)        agree + dis > 0
               = 1.0                                                    agree + dis == 0

    A PAIR is one claim of `p`'s own ledger whose `Claim.teller` is `teller`, against `p`'s own
    firsthand claim (empty chain, source `firsthand`) on the SAME `(subject, predicate)` cell: it
    agrees if the values are `==`, else it disagrees. The pairing step is `_pair`, the one
    `agreement` uses; only the key (a cell, not a predicate) and the roster differ. It reads
    `p.ledger` and nothing else, so another person's claims cannot move it (`p` never reads a
    ledger it does not hold).

    ⚠ ONLY CELL PREDICATES PAIR (`is_cell`, `data/requires.py: CELL_STEMS`), BOTH SIDES. A `seen`
    claim is not a cell -- each sighting is a distinct `Seen` value, so a told sighting would
    "disagree" with the very sighting it reports -- and an event-kind claim (`news.told` ...) is
    always `True`, so any pair of them agrees for free. The firsthand claim paired against is the
    one `LedgerReader` reads as the belief AMONG FIRSTHAND CLAIMS (`_pair`). A claim stores no time of
    observation, so a told claim that has itself since replaced that belief is still scored against
    the older firsthand one (recorded at `H-183`).

    ⚠ ZERO PAIRS IS NEUTRAL, 1.0 -- DELIBERATELY NOT `standing_of`'s POLARITY. `standing_of` maps
    zero pairs to the MAXIMUM gap because there the thing measured is a flattering reading, and
    no evidence must not flatter. Here the thing measured is a stranger's reliability, and copying
    that polarity would read every teller `p` has never been able to check as maximally unreliable,
    halving their word (at the shipped gain) before they have said anything wrong. A teller with no
    record is exactly as credible as `told_weight` and `relation` make them.

    ⚠ A TELLER'S OWN CONTRADICTION IS A PAIR, SO IT LOWERS THEIR RECORD: the claim being weighed is
    one of the pairs. That is intended -- a teller who contradicts what `p` saw is, by that, less
    credited on the next cell -- and it is also why `record_gain` 0 (the control) is the only arm on
    which a told claim's weight is independent of the firsthand claims it contradicts."""
    gain = fx.get("record_gain")
    told = [c for c in p.ledger if c.teller == teller and is_cell(c)]
    own = [c for c in p.ledger if c.firsthand and is_cell(c)]
    # B11.75 (R-19-05; `proposals/v12_B11_a_conclusion_acted_on.md` §2): A CONCLUDER IS A TELLER OF HIS OWN CONCLUSION. At `record_concluders` 1 the `told` set also admits what `teller`
    # told `p` as a conclusion that NAMES A DOER (`concluded:<kind>`, value a person -- the `Partial` deposit, value `True`, withholds the hand and says nothing to check), and `own`
    # gains `p`'s own reading of who did each such deed (`concluded_cells`, over his UNTOLD claims), so `_pair` grades it as it grades a told cell: the same agree/disagree rule,
    # no second arithmetic, no store. WHERE R-19-05 DEPARTS: it scores a holder "by WITNESS or by telling"; this scores the TOLD holder only (a witness of the bare utterance
    # holds nothing of what was asserted). At `0` (the control) the filter is the cell filter above, exactly, and the flag is read only for a teller who told a conclusion.
    told_concluded = [c for c in p.ledger if c.teller == teller and _is_conclusion(c)]
    if told_concluded and fx.get("record_concluders"):
        kinds = frozenset(c.predicate.partition(":")[2] for c in told_concluded)
        told = told + told_concluded
        own = own + concluded_cells([c for c in p.ledger if not c.chain], p.id, kinds)
    agree, dis = _pair(told, own, lambda c: (c.subject, c.predicate), None, tick, fx.claim_decay())
    # ABSENT: H-191 intent reconciliation  (an `absent` hole row, read by harness/register.py; nothing reads this marker)
    if agree + dis == 0:
        return 1.0
    return 1.0 + gain * (agree - dis) / (agree + dis)


def teller_weight(p: Person, fx: "Fixtures", tick: int = 0) -> Callable[[Claim], float]:
    """THE `weigh` CLOSURE `LedgerReader` RANKS `p`'S CLAIMS BY (telling workplan `T3a`,
    `ED-IN-0282`; the reader `H-157` recorded as missing for `Claim.teller`).

        weigh(c) = 1.0                                       if c.chain is empty
                 = clamp01(told_weight ** hops * relation * record)   otherwise
        hops     = len(c.chain)         teller = c.chain[-1]           (origin = c.chain[0])
        relation = 1 + rank_gain * rank(p, teller)
                     + regard_gain * clamp(regard(p, teller, fx) / STANCE_MAX, -1, 1)
                   (`regard` is G1's: stored stance plus the judged and told halves at their gains)
        record   = `record(p, teller, fx)`: 1.0 with no pair; else 1 + record_gain * balance (`T6`)
        stake    = `1 - rival_gain` when `p` holds a told `bond:rivalry` claim on `c.subject` whose origin (`chain[0]`) is the teller -- the teller's own
                   bond to the subject, which `boot/realm.py::seed_relations` deposits for its holder -- else 1.0 (`H-180`, B10.63). It depends on the
                   claim's SUBJECT, so it is not memoised per teller; the set of `(teller, subject)` pairs is read from `p`'s ledger once, on the
                   first told claim, and only at `rival_gain` > 0 (the shipped control reads no ledger for it).

    `RULINGS.yaml` CAT-3, closed: store the teller and grade the claim WHEN READ, by the hearer's
    belief about their relation to the teller -- so a revised regard re-grades every claim that
    teller ever passed on, and nothing is frozen at deposit. `hops` is read off `Claim.chain` (`T3b`):
    a retelling is a longer chain, so it weighs `told_weight` less again, and the `relation` is the
    hearer's to the one who told THEM, the last hop. A claim with an empty chain -- firsthand,
    seen, inferred, or a `told_by` deposit through a channel with no speaking actor -- weighs 1.0.

    ⚠ B09.06 `weigh_confidence` (`H-183`): AT `True` EVERY WEIGHT ABOVE IS MULTIPLIED BY HOW SURE HE STILL IS,
    `present_confidence(c) / confidence_default`, for a claim nobody told as for one somebody did (the empty-chain branch
    returns that share instead of 1.0), so a sighting he has half forgotten weighs half and a teller can outweigh it.
    Refraction sets the deposit-time `confidence`; this reads it once, here, at `tick`. At `False` (the control, shipped
    until B09.08) the closure is the one above, exactly, and reads neither `confidence` nor the decay rate.
    ⚠ THE TELLER FIXTURES (`told_weight`, `rank_gain`, `regard_gain`, `rival_gain`) ARE READ ON THE FIRST TOLD CLAIM, NOT AT BUILD. A
    ledger with no teller in it reads none of them. `weigh_confidence` and, when it is on, `confidence_default` and the
    decay rate are read once, at the closure's build.
    ⚠ AT THE CONTROL VALUES (`told_weight` 1.0, `rank_gain`, `regard_gain`, `rival_gain` and `record_gain` all
    0) EVERY CLAIM WEIGHS EXACTLY 1.0.
    ⚠ THE ONE-HOP BOUND. `told_weight` x `relation` x `record` is clamped at 1.0, and a one-hop claim
    at the shipped 0.5 stays strictly below a firsthand claim's 1.0 only while `relation` x `record`
    stays below 2. At NEUTRAL regard a good record ALONE gives 0.5 x 1 x 1.5 = 0.75 (< 1); 1.0 needs
    `relation` x `record` >= 2, i.e. at the best record (1.5) `relation` >= 4/3 -- regard >= 2/3 of
    `STANCE_MAX` at the shipped `regard_gain`. A regarded teller whose earlier hearsay was confirmed
    can therefore tie a firsthand claim on support and win on `when`; `rank` reads 0 (`H-181`) so it
    adds nothing yet. `record` is not independent of what it weighs: see `record`'s last warning.
    ⚠ `relation` AND `record` EACH DEPEND ON THE TELLER ALONE AND ON `p`'s LEDGER, WHICH DOES NOT
    CHANGE INSIDE ONE `opening_set`, so each is computed ONCE PER TELLER (except under `loop/witness.py`'s
    `ledger_weigh`, whose closure outlives deposits within one (witness, Event): its memo is the
    first-use ledger's)."""
    gains: list = []
    relation_of: dict = {}      # `relation` depends on the teller alone: one stance scan per teller
    record_of: dict = {}        # `record` too: one ledger scan per teller
    rivals: list = []           # H-180: ONE set of `(teller, subject)` the hearer holds a told `bond:rivalry` claim for, scanned on the first told claim at `rival_gain` > 0
    # B09.06: read ONCE per closure. At `False` (the control) `sure` is never called and every weight is the one above.
    on = fx.get("weigh_confidence")
    full = fx.get("confidence_default") if on else 0
    decay = fx.claim_decay() if on else 0

    def sure(c: Claim) -> float:
        """How sure he still is of `c`: its present confidence (`state/ledgers.py::present_confidence`, read at `tick`) as a
        share of `confidence_default`. The one factor `weigh_confidence` adds; refraction set the deposit-time value."""
        return present_confidence(c.confidence, c.when, tick, decay) / full

    def weigh(c: Claim) -> float:
        if not c.chain:
            return sure(c) if on else 1.0
        teller = c.teller
        if not gains:
            gains.extend((fx.get("told_weight"), fx.get("rank_gain"), fx.get("regard_gain"), fx.get("rival_gain")))
        told_weight, rank_gain, regard_gain, rival_gain = gains
        relation = relation_of.get(teller)
        if relation is None:
            relation = relation_of[teller] = (
                1.0
                + rank_gain * rank(p, teller)
                + regard_gain * _clamp(regard(p, teller, fx) / STANCE_MAX, -1.0, 1.0))
        # H-180 (B10.63): a rival's report is discounted as interested. Read from `p`'s own ledger only; at gain 0 the factor is exactly 1.0.
        stake = 1.0
        if rival_gain:
            if not rivals:
                rivals.append(set((b.chain[0], b.subject) for b in p.ledger
                                  if b.chain and b.predicate == BOND_STEM + "rivalry" and b.value is True))
            if (teller, c.subject) in rivals[0]:
                stake = _clamp(1.0 - rival_gain, 0.0, 1.0)
        rec = record_of.get(teller)
        if rec is None:
            rec = record_of[teller] = record(p, teller, fx, tick)
        w = _clamp(told_weight ** c.hops * relation * rec * stake, 0.0, 1.0)
        return w * sure(c) if on else w

    return weigh


# ---------------------------------------------------------------------------------------------------------------------
# B24p.06 -- THE BEARING READING AND WHAT A PERSON CARRIES IN (V2 p2 §A.2 to §A.4, §G; p4 §K B2, B6, D4, D6; §L R1, 2, 13, 19).
#
# What a matter, a person or a thing shown MEANS TO A PERSON: what he wants, what he holds, whom he stands with. ONE derivation, the
# same whatever his role (party, adjudicator, audience). Every function here reads the person's OWN interior (a `Person` or a
# `PersonInterior`) and the operands the host passes (his `oblige` edges, the factions of his seats and of the parties he shares,
# his office's duty, the matter's `bears`); none reads a `World`, another person's ledger or a true attribute of anyone else.
#
# `bears` is `{tag: signed weight}`: how the matter bears on a pursuit or an affiliation, toward `for` (+) or `against` (-). The
# two rosters share no name (`Person.scar`), so one map serves `want` (pursuits) and `hold` (convictions). It has no tree carrier
# (C(B24p) UNDECIDED (5): B27.05 owns "which pursuits a topic bears on"), so the HOST passes it and `{}` is a matter that bears on
# nothing -- stake and fit then fall to `bond` alone `[HOOK]`.
#
# `[HOOK]` (V2 p2 §A.3's rule: a layer with no carrier is one more term in a sum the day it has one, read as 0 until then): kin and
# patronage (`tie`), needs, ambitions and a person's own goals (`want`: `data/goals.py` authors goals for an ORGANISATION, and nothing
# reads one off a person), a forged `Record` (`false_items`). The office's duty enters as the operand `duty`, empty until a host
# builds it.
# ---------------------------------------------------------------------------------------------------------------------

SHARED_FACTION_TIE = 0.3   # [JUSTIFIED: V2 p4 §K C-faction -- a shared faction is a tie, 0.3; no document derives the size]  # [ASSUMPTION; Jordan to correct]
OBLIGE_TIE = 0.5           # [JUSTIFIED: V2 p2 §A.2 -- a debt he owes is a tie as kin and patronage are, 0.5; no document derives the size]  # [ASSUMPTION; Jordan to correct]
# THE ONE HOME OF THE FLOOR (V2 p4 §L 2; A-139: being a party is a stake): the literal the season driver's `_stake` used to patch
# (no such patch stands in this tree: nothing here reads a floor but `bearing`).
PARTY_STAKE = 0.2          # [JUSTIFIED: V2 p2 §A.2 -- a party's least stake in his own case, toward his side, 0.2]  # [ASSUMPTION; Jordan to correct]
BEARING_PARTS = 3          # [JUSTIFIED: V2 p2 §A.2 -- `(want, hold, bond)`: the three sums a stake, a conflict and a lean are the mean of]

if "testimony" not in MATTERS:
    raise ValueError("`false_items` brings a `testimony`, and `rosters.yaml: matters` has none (V2 p2 §G: a false item is his own "
                     "false word, brought as testimony)")


def _clip(x: float, lo: float = -1.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


def _mean(xs) -> float:
    xs = tuple(xs)
    return ltr_sum(xs) / len(xs)


def _debt(p, q: str, edges) -> float:
    """What he OWES `q`, from the `oblige` edges the host passes: each live, un-`imposed` oath he swore to `q` (his `subject`, `q` the
    `object`) is one `OBLIGE_TIE`. An oath sworn TO him is `q`'s debt (a patron's side of it is `[HOOK]`), and a sentence a determination
    imposed (`Tenure.imposed`) is no oath he swore."""
    return float(ltr_sum(OBLIGE_TIE for t in edges
                         if t.kind == "oblige" and t.live and not t.imposed and t.subject == p.id and t.object == q))


def tie(p, q: Optional[str], *, edges=(), shared_faction: bool = False) -> float:
    """HOW ANOTHER PERSON BEARS ON HIM, `-1..1`: `clip(stance toward q + debt[q] + 0.3 [a shared faction])` (V2 p2 §A.2). The stance
    is `stance_toward` over the row type's own bound (`STANCE_MAX`, as `regard_step` reads it), so a relationship is on `-1..1` as the
    sum is. Kin and patron or client are `[HOOK]` (no carrier), read as 0. `shared_faction` is the host's: whether `q` serves a
    faction he serves (a man cannot read another's faction, V2 p4 §K C-faction). Himself, and nobody, are 0."""
    if q is None or q == p.id:
        return 0.0
    x = stance_toward(p, q) / STANCE_MAX + _debt(p, q, edges) + (SHARED_FACTION_TIE if shared_faction else 0.0)
    return _clip(x)


def _duty_of(duty, bears) -> float:
    """His office's duty where it names what the matter bears on: `sum(duty[t] x bears[t])`, `duty` `((tag, weight), ...)`."""
    return float(ltr_sum(d * bears.get(t, 0.0) for t, d in duty))


def bearing(p, bears, *, for_party: Optional[str], against_party: Optional[str], edges=(), duty=(), shares=(),
            party: bool = True) -> tuple:
    """`(want, hold, bond)`, each `-1..1` toward `for`: how the matter bears on `p` (V2 p2 §A.2's three sums).

      * `want` -- his pursuits the matter bears on: `sum(pursuits[t] x bears[t])`. Needs, ambitions, goals `[HOOK]`;
      * `hold` -- his convictions over the roster's own ceiling (`AFFILIATION_CEILING`), and his office's `duty` (operand);
      * `bond` -- `tie(for) - tie(against)`; `shares`: the parties' ids who serve a faction he does.

    `party=True`: where `p` IS a party, his bond is raised as far as it goes until `mean(stake)` is at least `PARTY_STAKE` toward his own
    side -- being a party is a stake (A-139, V2 p4 §K B6, §L 2). This is the floor's one owner. `party=False` reads what the matter
    touches of his own beyond that."""
    want = _clip(float(ltr_sum(p.pursuits.get(t, 0.0) * w for t, w in bears.items())))
    hold = _clip(float(ltr_sum(p.conviction.get(t, 0) / AFFILIATION_CEILING * w for t, w in bears.items())) + _duty_of(duty, bears))
    bond = _clip(tie(p, for_party, edges=edges, shared_faction=for_party in shares)
                 - tie(p, against_party, edges=edges, shared_faction=against_party in shares))
    sign = 1.0 if p.id == for_party else -1.0 if p.id == against_party else 0.0
    if party and sign and sign * ltr_sum((want, hold, bond)) < BEARING_PARTS * PARTY_STAKE:
        bond = _clip(sign * BEARING_PARTS * PARTY_STAKE - want - hold)
    return (want, hold, bond)


def care(p) -> tuple:
    """`(want, hold, bond)` in `0..1`: how much each kind of thing moves him -- his strongest pursuit, his strongest held conviction over
    the ceiling, his strongest tie in either direction over the stance bound; each 0.5 where he holds none (V2 p2 §A.2)."""
    pursuits = [float(w) for w in p.pursuits.values() if w > 0]
    held = [c for c in p.conviction.values() if c > 0]
    ties = [abs(stance_toward(p, ref)) / STANCE_MAX for ref in {row[0] for row in p.stance if len(row) >= 3}]
    return (_clip(max(pursuits), 0.0, 1.0) if pursuits else 0.5,
            _clip(max(held) / AFFILIATION_CEILING, 0.0, 1.0) if held else 0.5,
            _clip(max(ties), 0.0, 1.0) if ties else 0.5)


def takes_side(stake: tuple) -> Optional[str]:
    """Which side a man not named by the matter takes: the sign of `mean(stake)`, `None` where nothing bears (V2 p4 §K D4)."""
    m = _mean(stake)
    return None if m == 0 else "for" if m > 0 else "against"


def conflict(p, bears, *, for_party: Optional[str], against_party: Optional[str], edges=(), duty=()) -> tuple:
    """`(conflict, lean)`: his PARTIALITY, how far the matter is his own business and which way that leans (V2 p2 §A.2; p4 §K B6).

        conflict = (|want| + |duty| + max(|bond|, min(1, |tie to for| + |tie to against|))) / 3        lean = (want + duty + bond) / 3

    It reads his PERSONS (stance, debts, and being a party: the party's own `bearing` bond, his floor) and his WANT, and his office's duty
    where it names what the matter bears on. Never a conviction (p4 §L 19: it moves how he hears) and never a shared faction (§L R1: it
    moves how he hears, `tie`'s 0.3, not whether he is partial), so `bearing` is read here with no faction and no `shares`. Interests and
    ties on both sides are a conflict, never a cancellation: `bond` nets opposed ties, so the sum of their magnitudes is the other reading
    (p4 §K B6, §L 13)."""
    want, _, bond = bearing(p, bears, for_party=for_party, against_party=against_party, edges=edges, duty=duty)
    tf, ta = tie(p, for_party, edges=edges), tie(p, against_party, edges=edges)
    if p.id not in (for_party, against_party):
        bond = _clip(tf - ta)
    d = _clip(_duty_of(duty, bears))
    return ((abs(want) + abs(d) + max(abs(bond), min(1.0, abs(tf) + abs(ta)))) / BEARING_PARTS,
            ltr_sum((want, d, bond)) / BEARING_PARTS)


def believes(p, matter: str, fx, tick: int) -> float:
    """What he KNOWS of the matter, `-1..1` toward `for`, read from his OWN ledger through `said_of` at `tick` (V2 p2 §A.3; p4 §F 37): the
    claim he would say of `matter` (the subject), a held truth value read as `+` (`for` asserts it true) or `-`, by how sure he is NOW
    (`present_confidence / Fixtures.confidence_default`: a claim nobody refreshed fades). Only a TRUTH-VALUED claim says which side he holds (the
    pool is the ledger's `bool` claims, as `lie_said_of`'s is its cells): a witnessed sitting about the man (`sitting:*`, a number or a name) is
    not what he believes of him, nor is a bond he holds of him (`bond:<ground>`, `True`: a relationship, `BOND_STEM`). Nothing held is 0 [ASSUMPTION: the matter's `for` side asserts its claim as held; Jordan to correct]."""
    said = said_of([c for c in p.ledger if isinstance(c.value, bool) and not c.predicate.startswith(BOND_STEM)], matter, fx, p, tick=tick)
    if said is None:
        return 0.0
    sure =_clip(said.confidence / fx.get("confidence_default"), 0.0, 1.0)
    return sure if said.value else -sure


def false_items(p, matter: str, side: str, fx, tick: int) -> tuple:
    """Where a false item comes from (V2 p2 §G; p4 §F 37, §K B2, D6): only HIS OWN FALSE WORD. Where `believes` runs against the `side` he
    speaks for and `lie_said_of` has a false value to say of what he holds, he can offer his own assertion of the contrary as one
    `testimony` he knows false (`sincere: False`), weighing as much as he is sure of what it contradicts; else `()`. Both read his claims at
    `tick`. A forged `Record` is `[HOOK]`: no act writes one."""
    b = believes(p, matter, fx, tick)
    if SIDE_SIGN[side] * b >= 0 or lie_said_of(p.ledger, matter, fx, p, tick=tick) is None:
        return ()
    return (Item(f"word:{p.id}:{matter}", "testimony", abs(b), source=p.id, about=matter, sincere=False),)


def strain_carried(rattles, fx) -> float:
    """What he carries in from earlier rattles (V2 p2 §A.4): `0.5 x` the sum, freshest first, of `max(0, 1 - strain_fade x scenes since)
    / 2^k` for the k-th freshest -- each rattle fades on its own clock and counts half the one before, so any number stays under 1.0 and
    nothing ratchets. `rattles` is the `(scenes since, ...)` the host counts from his acts' endings (B24p.20's reader)."""
    fades = sorted((max(0.0, 1.0 - fx.get("strain_fade") * s) for s in rattles), reverse=True)
    # The sum is under 1.0 for any count, but a float sum of more than 53 halvings rounds up to 2 x 0.5: clamp to the largest float below it.
    return min(0.5 * float(ltr_sum(f / 2 ** k for k, f in enumerate(fades))), math.nextafter(1.0, 0.0))
