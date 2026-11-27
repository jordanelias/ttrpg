"""`decision/` -- THE CHARACTER SHEET AS THREE SPACES (v10 REM-30, plan position IN-47): creation,
development, chronicling. Design: `proposals/2026-10-07-character-sheet-spaces.md` and its
`## Review at B-H` -- reference, RATIFIED (Jordan, 2026-11-05, ED-IN-0349); nothing here ratifies it.

A management space *"reads the player's own `View`/`Question`/`Candidate` and emits acts, owning no
game state"* (A-25). In code each space is at most a `choose` callable, or a part of the one handed
to `SeasonDriver.season(choose, ...)` for the player's person; DELIBERATE calls it inside a map that
holds no token (`loop/deliberate.py`), so it cannot write -- `04` §A.2: *"a module with no token
cannot write"*. **No space here writes a `Person` field.** Every carrier change the player causes is
an act's, folded at RESOLVE (and the fold's two post-outcome writes, `_scar_witnesses` and
`_conviction_crisis`, which move OTHER persons' `scar`/`conviction` too).

  CREATION (arm C1)  `creation_sheet(persons)` reads the persons the world builder ALREADY SEATED;
                     `seat(rows, person_id, space)` is the player's pick, returned as the `overrides`
                     mapping `harness/play_surface.py::dispatching_chooser` reads -- the playable
                     `choose` dispatches on `p.id`. **No act, no write.** There is no cast-entry arm:
                     the corpus cast shape is closed (`corpus_run.CAST_KEYS`, no `pursuits` key), so
                     C1 is the review's fallback. `person_id=None` is THE ARM SWITCHED OFF and ships:
                     the mapping is `{}` and the run is the automated run (the control).
                     Arm C2 (a mid-campaign person) is CENSUS's `(Person, exists)` and is not built here.
  DEVELOPMENT        `development_space(fx, mint, pick, ...)` is a play-surface callback. It shows the
                     player `DevelopmentSheet` -- his own fields, View, Question, and the candidate set
                     `make_ranker` orders for him -- and packs the INDICES he picks through `release`,
                     the automated chooser's own packing step. **It ranks and selects; it never forms**:
                     an index outside the set is refused, so there is no second option generator. A pick
                     of every index in order IS `make_chooser` (the control); any other pick is a mover.
  CHRONICLING        `chronicle(p, fx=None)` -- **no act, no write**: the person's own `ledger` as held, his belief
                     per subject through `LedgerReader` (its comparator, not a copy; weighed when `fx` is given, B09.07), his `threads`
                     (B09.17: each `seen` claim paired with the claim its `why` names, where he holds both), and the PRESENT
                     values of `scar` and `conviction`. **It shows a scar as no event of its own, and a crisis as none**:
                     `_scar_witnesses` records its write in one `scar.taken` Event, appended to the
                     log and kept out of the list WITNESS reads (so no deposit), and the `fight`
                     row still withholds `scar.taken` from its own `emits:`; `_conviction_crisis`
                     writes `conviction` with no Event at all. So the sheet reads the PRESENT
                     values, never a history: no `causes[]` edge or WITNESS deposit records when or
                     by whose act a count rose or a creed folded. Giving it that history is a
                     writer's change (`loop/resolve.py`), never a space's.

THE SHEET HOLDS COPIES, SHALLOW EXCEPT WHERE IT MATTERS. Every field a sheet carries is a read-only copy of the
person's own carrier (`MappingProxyType`, tuples), so a client's `pick` is never handed a `Person` and cannot reach
one. `DevelopmentSheet.candidates` are DEEP copies and `release` packs the originals by the picked indices, so a
`pick` that mutated a `Candidate` changes nothing that is packed. Two contents are still live objects:
`Chronicle.ledger` (the `Claim`s) and `DevelopmentSheet.view` (`View.odds` closes over the World; named at
`loop/deliberate.py`, a CONVENTION).
The space functions themselves do hold `p`; the falsifier for a space that writes it is the G2 spy
(`tests/test_g2_token.py::test_g2_deliberate_mutates_no_store_by_any_route`, its spaces arm).

AX-2 binds this file like every file under `decision/`: no `World`, as an import, a name, an
attribute or a string (`tests/test_season_shape.py`, by path).
"""
from __future__ import annotations

import copy
from dataclasses import dataclass
from typing import Any, Callable, Iterable, Mapping, Optional, Sequence

from ...substrate.descriptors import ATTRIBUTE_GLOSSES, CAPABILITIES, attribute_key
from ..data.rosters import AFFILIATIONS, SEEN_PREDICATE
from ..gaps import Forbidden
from ..queries.person_q import LedgerReader, _seen_index, decisiveness, deed_doer, is_deed, recognised
from ..state.carriers import Act, Candidate, Claim, Person, PersonInterior, Question, Scene, View, fade_of, frozen
from .choose import Ranked, _believed_chance, _payload_of, make_ranker, release
from .options import ledger_weigh, own_state_declines

def describe(key: str) -> str:
    """The gloss of a skill or an attribute: the leaf's text, no `World` (B04.02, DEF Edit 1). A skill is read by
    its name (`inquiry`), an attribute by its key, name or alias (`attr.mind.acuity`, `Reason`, `Cognition`).
    Raises `ValueError` for a name that is neither."""
    if key in CAPABILITIES:
        return CAPABILITIES[key].gloss
    attr = attribute_key(key)
    if attr is not None:
        return ATTRIBUTE_GLOSSES[attr]
    raise ValueError(f"{key!r} is neither a defined skill ({', '.join(CAPABILITIES)}) nor one of the ten attributes")


_LAW = ("IN-47 / A-25 -- a management space ranks and selects among the candidates the opening set "
        "formed and the persons the builder seated; it forms none and writes nothing")


# ---------------------------------------------------------------------------------------------------
# CREATION -- arm C1: the player picks a person the world builder already seated. No act, no write.
# ---------------------------------------------------------------------------------------------------

@dataclass(frozen=True)
class CreationRow:
    """One seated person as the creation sheet shows him: the person-side fields world-gen wrote once
    (`capability` by `build_at`; `pursuits` by `build_at` or the realm builder; `conviction` by the realm
    builder only, `{}` on shipped data; `attributes` by the realm builder: a cast row's `stats:` over the sheet
    `state/carriers.py::generated_attributes` draws, when its `cast_attributes` switch is on, `{}` otherwise -- CR-20, the ten registry keys). A copy: the player
    reads it and picks an `id`."""
    id: str
    name: str
    capability: Mapping
    pursuits: Mapping
    conviction: Mapping
    attributes: Mapping


def creation_sheet(persons: Iterable[Person]) -> tuple:
    """The creation sheet: one `CreationRow` per seated person, in id order (a pick list, not a ranking).
    `persons` is what the caller already holds (`w.persons.values()` before the first season); this
    function takes no `World` and writes nothing."""
    return tuple(CreationRow(p.id, p.name, frozen(p.capability), frozen(recognised(p, p.pursuits)),
                             frozen(p.conviction), frozen(p.attributes))
                 for p in sorted(persons, key=lambda q: q.id))


def seat(rows: Sequence[CreationRow], person_id: Optional[str], space: Callable[..., list]) -> dict:
    """THE CREATION ARM: the player's pick, as the `overrides` mapping `dispatching_chooser(auto, overrides)`
    reads -- `{person_id: space}`. `None` is the arm switched off (`{}`, the automated run).

    A `person_id` the creation sheet does not hold is REFUSED: C1 seats a person the builder already seated
    and mints none (a minted person is H-51's / CENSUS's, arm C2, and a cast entry has no shape to take)."""
    if person_id is None:
        return {}
    if person_id not in {r.id for r in rows}:
        raise Forbidden(f"creation seated {person_id!r}, which the world builder did not seat",
                        "IN-47 C1", law=_LAW)
    return {person_id: space}


# ---------------------------------------------------------------------------------------------------
# DEVELOPMENT -- the player's own View/Question/Candidate into the chooser slot.
# ---------------------------------------------------------------------------------------------------

@dataclass(frozen=True)
class DevelopmentSheet:
    """What the player sees for his person at one deliberation. `candidates` is `make_ranker`'s order --
    the shipped policy's ranking over his own candidate set -- shown, never imposed; `budget` is his
    season remainder (`ask_budget()`). The own-field copies are the inputs `make_chooser` admits
    (`pursuits`, `stance`, `conviction`, `scar`) plus `body` and `capability`, and (B04.13) `attributes`, `thread_sensitivity`, `heritage` and `tenures` (his live edges as
    `(kind, object)`: seats, oaths, commits, residence); derived lines
    (`confliction`, `crisis_weights`' shifted weights) stay derived and are not stored here, with one line SHOWN
    that the person does not hold: `decisiveness`, `person_q.decisiveness(p, scar_weight_shift)` read once when the
    sheet is built -- how firmly his pursuits point one way, the length of his projected pursuit vector, which the
    draw's temperature is read against. The person stores nothing."""
    person_id: str
    view: View
    question: Question
    candidates: tuple
    budget: int
    capability: Mapping
    pursuits: Mapping
    stance: tuple
    conviction: Mapping
    scar: Mapping
    body: int
    # B04.13 (CAP A8): the person's own state the play surface shows, copies only. No derived pool is stored: the play surface
    # asks `View.odds` per candidate, as the chooser does.
    attributes: Mapping
    thread_sensitivity: Optional[int]
    heritage: Optional[str]
    tenures: tuple
    decisiveness: float          # derived, B10.27: `person_q.decisiveness(p, fx.get("scar_weight_shift"))`


def development_space(fx: Any, mint: Callable[[str, str, str], str],
                      pick: Callable[[DevelopmentSheet], Sequence[int]],
                      verbs: Optional[frozenset] = None,
                      draw: Optional[Callable[[str, str], Any]] = None) -> Callable[..., list]:
    """A play-surface callback `(p, v, s, ask_budget, auto) -> list[Scene]` for the player's person; `p` is the
    `PersonInterior` DELIBERATE hands `choose` (B03.58), the same type, so the space cannot assign to the person.

    `pick(sheet)` returns INDICES into `sheet.candidates`, in the order the player would spend his
    budget. The space refuses an index out of range or repeated (`Forbidden`), then packs the picked
    candidates through `release` -- the same step, the same `fx`/`mint`/`draw` the automated chooser
    uses -- so a player's act has the automated act's shape. `auto` (the delegate) is not called: the
    sheet already carries what it would rank. Build it with the arguments the caller gave
    `make_chooser`; a different `verbs` or `draw` is a different candidate set, not this space's control."""
    rank = make_ranker(fx, verbs, draw)

    def space(p: PersonInterior, v: View, s: Any, ask_budget: Callable[[], int], auto: Any = None) -> list:
        q = getattr(v, "question", None)
        if q is None:
            return []
        cands = rank(p, v)
        n = ask_budget()
        sheet = DevelopmentSheet(p.id, v, q, tuple(copy.deepcopy(c) for c in cands), n, frozen(p.capability),
                                 frozen(recognised(p, p.pursuits)), tuple(p.stance), frozen(p.conviction),
                                 frozen(p.scar), p.body, frozen(p.attributes), p.thread_sensitivity, p.heritage,
                                 tuple((t.kind, t.object) for t in p.tenures if t.live),
                                 decisiveness(p, fx.get("scar_weight_shift"), hold=fx.get("scar_hold"), mass=fx.get("scar_primary_mass")))
        chosen = [int(i) for i in pick(sheet)]
        if len(set(chosen)) != len(chosen) or any(not 0 <= i < len(cands) for i in chosen):
            raise Forbidden(f"{p.id}'s pick {chosen} is not a selection from the {len(cands)} candidates "
                            f"his opening set formed", "IN-47 rule 1", law=_LAW)
        # The pick carries what the ranker's strike kept (`Ranked.forgone_of`, B10.24), so a Scene the player's pick packs names what his scruple struck as the
        # automated chooser's does; `decide` stays off (a pick is no sampled order, `Ranked`'s note).
        picked = Ranked(cands[i] for i in chosen)
        picked.forgone_of = getattr(cands, "forgone_of", None)
        return release(p, picked, n, fx, mint, q, draw)
    return space


def take_ranked(sheet: DevelopmentSheet) -> range:
    """The pick that takes the shipped ranking whole -- the development space's CONTROL: seated with it,
    the player's person decides exactly as `make_chooser` would (same scenes, same `content_hash`)."""
    return range(len(sheet.candidates))


# ---------------------------------------------------------------------------------------------------
# SITUATION AND OFFER (B34.02) -- what is in front of him and what he may do. Readers: no act, no write, no draw of their own.
# ---------------------------------------------------------------------------------------------------

@dataclass(frozen=True)
class AskedRow:
    """One question that demands his attention, as `View.questions` carries it (`questions_for`'s, in `attention_key` order), and the claim of HIS
    that its `about` names where that is one of his own (`None` otherwise: a seat, a record, a place)."""
    question: Question
    claim: Optional[Claim]


@dataclass(frozen=True)
class Situation:
    """WHAT IS IN FRONT OF HIM NOW: his budget, his own fields (copies, as `DevelopmentSheet`'s), what he holds, and the questions asked of him.
    `holdings` is `((tenure kind, object id), ...)` of his own live Tenures -- the same read `DevelopmentSheet.tenures` makes (`OwnStateReader` answers
    `held_by` of one object and enumerates nothing, so the person's own `tenures` are read here as they are there). `asked` is `View.questions`,
    which `questions_for` sorted by `attention_key`: no second generator. Lane 28's readings (who occupies him, which petitions wait) join in B28."""
    person_id: str
    budget: int
    body: int
    capability: Mapping
    pursuits: Mapping
    stance: tuple
    conviction: Mapping
    scar: Mapping
    holdings: tuple
    asked: tuple


def situation(p: Person, v: View, ask_budget: Callable[[], int]) -> Situation:
    """The `Situation` of `p` at the deliberation `v` was built for; `ask_budget()` is the season remainder, as the chooser asks it. Writes nothing."""
    mine = {c.id: c for c in p.ledger}
    return Situation(p.id, ask_budget(), p.body, frozen(p.capability), frozen(recognised(p, p.pursuits)), tuple(p.stance),
                     frozen(p.conviction), frozen(p.scar), tuple((t.kind, t.object) for t in p.tenures if t.live),
                     tuple(AskedRow(q, mine.get(q.about)) for q in v.questions))


@dataclass(frozen=True)
class OfferRow:
    """One candidate he may take, in `make_ranker`'s order. `candidate` is a deep copy; `occasion` the id of the first `asked` question that names
    `candidate.subject` among its referents (plain or classed), `None` for a standing candidate; `terms` the `score_terms` tuple the chooser summed
    (`make_ranker`'s `watch` hook is its one source); `odds` what he BELIEVES of the bands the verb writes in (`choose._believed_chance`, the one ask:
    a chance, or `None` where nothing prices the candidate), which may be wrong; `cost` in `Scene.cost`'s unit."""
    candidate: Candidate
    occasion: Optional[str]
    terms: tuple
    odds: Optional[float]
    cost: int


@dataclass(frozen=True)
class WithheldRow:
    """A verb his OWN state declined (`opening_set`'s own-state decline, shown): `unmet` names the own-state conjunct of its cell that read False."""
    verb: str
    subject: Optional[str]
    unmet: str


@dataclass(frozen=True)
class Offer:
    rows: tuple          # make_ranker's order
    withheld: tuple      # own-state declines only


def offer(p: Person, v: View, fx: Any, verbs: Optional[frozenset] = None,
          draw: Optional[Callable[[str, str], Any]] = None) -> Offer:
    """WHAT HE MAY DO: the rows `make_ranker(fx, verbs, draw)` orders for him, each with the terms its `watch` hook reported, his believed odds and its
    cost, and the verbs his own state withheld. `fx`, `verbs` and `draw` are the ones the chooser was built with (`rank` needs `fx`; a different `verbs`
    or `draw` is a different offer, as `development_space` says); the source's `offer(p, v)` has no way to reach them. Forms nothing, ranks nothing of its
    own, and writes nothing. A View with no question offers nothing."""
    q = getattr(v, "question", None)
    if q is None:
        return Offer((), ())
    watched: list = []
    order = make_ranker(fx, verbs, draw, lambda _p, _q, ranked, terms, sampled: watched.append((ranked, terms)))(p, v)
    terms_of = {id(c): t for c, t in zip(*watched[-1])} if watched else {}
    odds = getattr(v, "odds", None)
    extended = fx.get("extended_scene_cost")
    asked = tuple(v.questions)

    def occasion(subject: Optional[str]) -> Optional[str]:
        if subject is None:
            return None
        return next((a.id for a in asked if subject in a.referents or subject in {r for r, _ in a.classes}), None)

    def cost(c: Candidate) -> int:
        return Scene(f"offer:{c.verb}", p.id, [Act(f"offer:{c.verb}", p.id, c.verb, payload=_payload_of(c))]).cost(extended)

    rows = tuple(OfferRow(copy.deepcopy(c), occasion(c.subject), tuple(terms_of[id(c)]),
                          None if odds is None else _believed_chance(p, c, odds), cost(c)) for c in order)
    withheld = tuple(WithheldRow(*d) for d in dict.fromkeys(own_state_declines(p, v, q, fx)) if verbs is None or d[0] in verbs)
    return Offer(rows, withheld)


# ---------------------------------------------------------------------------------------------------
# ACCOUNT (B34.03) -- what he has learned since a point, from his own ledger and nothing else. No act, no write.
# ---------------------------------------------------------------------------------------------------

@dataclass(frozen=True)
class AccountRow:
    """One claim he holds that landed at or after `since`, as he holds it. `own` is `claim.doer == holder`, the echo of his own deed (WITNESS stamps `doer` only
    where the witness is the actor, so it leaks nothing a channel withholds). `prior` is the claim he holds on the same `(subject, predicate)` cell that landed
    latest before this one (a later `(when, lap)` than any other, a later place in his ledger on a tie), `None` where he holds none -- a quantity is trackable only for
    a person who holds claims about it. `unattributed` is a change he can see (`prior` differs in value, or the claim is an event-kind deposit, `person_q.is_deed`)
    for which no claim of his names a doer: no `doer` on it, no `Seen.who` on the sighting it landed with (his own, or the one its telling carried), no `deed_doer`
    answer. `claim.teller`, `claim.hops` and `claim.chain` say who told him, at how many removes."""
    claim: Claim
    own: bool
    prior: Optional[Claim]
    unattributed: bool


def account(p: Person, since: tuple) -> tuple:
    """THE PERSON'S OWN RECORD OF WHAT HE LEARNED SINCE `since` -- `(tick, lap)`, `world_q.landing_floor`'s own key: one `AccountRow` per claim of his ledger with
    `(when, lap) >= since`, in the order he holds them. Reads `p.ledger` and nothing else; writes nothing. ANOTHER PERSON'S REASONS ARE SHOWN EXACTLY HERE: as the claims
    he holds about that person's deeds, tellings and commitments, with their sources. A value no claim of his holds is in no row."""
    ledger = tuple(p.ledger)
    cells: dict = {}
    for i, c in enumerate(ledger):
        cells.setdefault((c.subject, c.predicate), []).append((c.when, c.lap, i, c))
    seen = _seen_index(ledger)

    def prior_of(c: Claim) -> Optional[Claim]:
        earlier = [(w, l, j, o) for w, l, j, o in cells[(c.subject, c.predicate)] if (w, l) < (c.when, c.lap)]
        return max(earlier, key=lambda t: t[:3])[3] if earlier else None

    def names_a_doer(c: Claim) -> bool:
        sighted = seen[4].get((c.subject, c.when, c.lap, c.chain), ()) if c.chain else seen[0].get((c.subject, c.when, c.lap), ())
        return (c.doer is not None or getattr(c.value, "who", None) is not None
                or any(getattr(s.value, "who", None) is not None for s in sighted) or deed_doer(c, seen) is not None)

    rows = []
    for c in ledger:
        if (c.when, c.lap) < tuple(since):
            continue
        prior = prior_of(c)
        changed = (prior is not None and prior.value != c.value) or is_deed(c)
        rows.append(AccountRow(c, c.doer == p.id, prior, changed and not names_a_doer(c)))
    return tuple(rows)


# ---------------------------------------------------------------------------------------------------
# CHRONICLING -- a reader of the person's own record. No act, no write.
# ---------------------------------------------------------------------------------------------------

@dataclass(frozen=True)
class Chronicle:
    """A person's own record as he holds it. `ledger` is his claims in the order he holds them (unknowns
    stay unknown, false beliefs stay believed); `beliefs` is, per subject he holds a claim on (first
    held first), the one claim `LedgerReader.latest_about` would offer -- recency then confidence, the
    reader's comparator, no salience.

    `scar` is split as the review's display rules require: (a) the pursuit side and the affiliation side
    are two rosters, never one list; (b) a count on a HELD affiliation is live, on an unheld one is
    history (a crisis rewrites only `conviction`). These are PRESENT values: no field records when, or by
    whose act, a count rose or a creed folded or was destroyed -- see the module docstring.

    B09.17: `threads` is, for each `seen` claim he holds whose `why` names a claim he still holds, the pair `(that claim's id,
    the id its `why` names)` -- the reader `Seen.why` lacked, what a person saw of one thing as the answer to another he saw. In
    ledger order. `()` wherever no `why` was deposited, which is every person at `Fixtures connection_chance` 0.0 (the control, shipped)."""
    person_id: str
    ledger: tuple
    beliefs: tuple
    conviction: Mapping
    scar_pursuits: Mapping
    scar_affiliations_held: Mapping
    scar_affiliations_history: Mapping
    threads: tuple


def chronicle(p: Person, fx: Any = None) -> Chronicle:
    """The chronicling space over one person. Reads `p`'s own `ledger`, `scar` and `conviction`; writes
    nothing, emits nothing, and leaves `content_hash` unchanged whether or not it is called.

    B09.07: given the `fx` the caller already holds, `beliefs` reads through the ONE comparator -- `LedgerReader` with
    `queries/person_q.py::ledger_weigh(p, fx, tick)`, the `weigh` `opening_set` and `belief_contradicts` read his ledger by --
    so the sheet shows what he acts on and says. Without `fx` (a hand-built read) it is the plain comparator, as before.
    B09.17: `threads` pairs each `seen` claim he holds with the claim its `why` names, where he still holds both."""
    tick, decay = fade_of(p)                        # B09.01: the claims he would offer are ranked as he holds them now
    reader = LedgerReader(p.ledger, ledger_weigh(p, fx, tick) if fx is not None else None, tick=tick, decay=decay)
    subjects = list(dict.fromkeys(c.subject for c in p.ledger))     # first held first, each once
    aff = {k: n for k, n in (p.scar or {}).items() if k in AFFILIATIONS}
    held = set(p.conviction or {})
    held_ids = {c.id for c in p.ledger}
    threads = tuple((c.id, c.value.why) for c in p.ledger
                    if c.predicate == SEEN_PREDICATE and getattr(c.value, "why", None) in held_ids)
    return Chronicle(
        p.id, tuple(p.ledger),
        tuple((subj, reader.latest_about(subj)) for subj in subjects),
        frozen(p.conviction),
        frozen(recognised(p, {k: n for k, n in (p.scar or {}).items() if k not in AFFILIATIONS})),
        frozen({k: n for k, n in aff.items() if k in held}),
        frozen({k: n for k, n in aff.items() if k not in held}),
        threads)
