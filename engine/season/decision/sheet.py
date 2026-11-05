"""`decision/` -- THE CHARACTER SHEET AS THREE SPACES (v10 REM-30, plan position IN-47): creation,
development, chronicling. Design: `proposals/2026-10-07-character-sheet-spaces.md` and its
`## Review at B-H` -- reference, PROPOSED and HELD BACK (ED-1094); nothing here ratifies it.

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
  CHRONICLING        `chronicle(p)` -- **no act, no write**: the person's own `ledger` as held, his belief
                     per subject through `LedgerReader` (its comparator, not a copy), and the PRESENT
                     values of `scar` and `conviction`. **It shows no scar or crisis as an event**: both
                     writers call `World.write` without `emits` (`loop/resolve.py::_scar_witnesses`,
                     `_conviction_crisis`), and `verb_table.yaml`'s `fight` row withholds `scar.taken`
                     on purpose -- so no `Event`, `causes[]` edge or WITNESS deposit records when or by
                     whose act a count rose or a creed folded. Giving it that history is a writer's
                     change (the row's `emits:`), never a space's.

THE SHEET HOLDS COPIES. Every field a sheet carries is a read-only copy of the person's own carrier
(`MappingProxyType`, tuples), so a client's `pick` is never handed a `Person` and cannot reach one.
The space functions themselves do hold `p`; the falsifier for a space that writes it is the G2 spy
(`tests/test_g2_token.py::test_g2_deliberate_mutates_no_store_by_any_route`, its spaces arm).

AX-2 binds this file like every file under `decision/`: no `World`, as an import, a name, an
attribute or a string (`tests/test_season_shape.py`, by path).
"""
from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Any, Callable, Iterable, Mapping, Optional, Sequence

from ..data.rosters import AFFILIATIONS
from ..gaps import Forbidden
from ..queries.person_q import LedgerReader
from ..state.carriers import Person, Question, View
from .choose import make_ranker, release

_LAW = ("IN-47 / A-25 -- a management space ranks and selects among the candidates the opening set "
        "formed and the persons the builder seated; it forms none and writes nothing")


def _frozen(d: Mapping) -> Mapping:
    return MappingProxyType(dict(d or {}))


# ---------------------------------------------------------------------------------------------------
# CREATION -- arm C1: the player picks a person the world builder already seated. No act, no write.
# ---------------------------------------------------------------------------------------------------

@dataclass(frozen=True)
class CreationRow:
    """One seated person as the creation sheet shows him: the person-side fields world-gen wrote once
    (`capability` by `build_at`; `pursuits` by `build_at` or the realm builder; `conviction` by the realm
    builder only, `{}` on shipped data). A copy: the player reads it and picks an `id`."""
    id: str
    name: str
    capability: Mapping
    pursuits: Mapping
    conviction: Mapping


def creation_sheet(persons: Iterable[Person]) -> tuple:
    """The creation sheet: one `CreationRow` per seated person, in id order (a pick list, not a ranking).
    `persons` is what the caller already holds (`w.persons.values()` before the first season); this
    function takes no `World` and writes nothing."""
    return tuple(CreationRow(p.id, p.name, _frozen(p.capability), _frozen(p.pursuits),
                             _frozen(p.conviction))
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
    (`pursuits`, `stance`, `conviction`, `scar`) plus `body` and `capability`; derived lines
    (`confliction`, `crisis_weights`' shifted weights) stay derived and are not stored here."""
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


def development_space(fx: Any, mint: Callable[[str, str, str], str],
                      pick: Callable[[DevelopmentSheet], Sequence[int]],
                      verbs: Optional[frozenset] = None,
                      draw: Optional[Callable[[str, str], Any]] = None) -> Callable[..., list]:
    """A play-surface callback `(p, v, s, ask_budget, auto) -> list[Scene]` for the player's person.

    `pick(sheet)` returns INDICES into `sheet.candidates`, in the order the player would spend his
    budget. The space refuses an index out of range or repeated (`Forbidden`), then packs the picked
    candidates through `release` -- the same step, the same `fx`/`mint`/`draw` the automated chooser
    uses -- so a player's act has the automated act's shape. `auto` (the delegate) is not called: the
    sheet already carries what it would rank. Build it with the arguments the caller gave
    `make_chooser`; a different `verbs` or `draw` is a different candidate set, not this space's control."""
    rank = make_ranker(fx, verbs, draw)

    def space(p: Person, v: View, s: Any, ask_budget: Callable[[], int], auto: Any = None) -> list:
        q = getattr(v, "question", None)
        if q is None:
            return []
        cands = rank(p, v)
        n = ask_budget()
        sheet = DevelopmentSheet(p.id, v, q, tuple(cands), n, _frozen(p.capability),
                                 _frozen(p.pursuits), tuple(p.stance), _frozen(p.conviction),
                                 _frozen(p.scar), p.body)
        chosen = [int(i) for i in pick(sheet)]
        if len(set(chosen)) != len(chosen) or any(not 0 <= i < len(cands) for i in chosen):
            raise Forbidden(f"{p.id}'s pick {chosen} is not a selection from the {len(cands)} candidates "
                            f"his opening set formed", "IN-47 rule 1", law=_LAW)
        return release(p, [cands[i] for i in chosen], n, fx, mint, q, draw)
    return space


def take_ranked(sheet: DevelopmentSheet) -> range:
    """The pick that takes the shipped ranking whole -- the development space's CONTROL: seated with it,
    the player's person decides exactly as `make_chooser` would (same scenes, same `content_hash`)."""
    return range(len(sheet.candidates))


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
    whose act, a count rose or a creed folded or was destroyed -- see the module docstring."""
    person_id: str
    ledger: tuple
    beliefs: tuple
    conviction: Mapping
    scar_pursuits: Mapping
    scar_affiliations_held: Mapping
    scar_affiliations_history: Mapping


def chronicle(p: Person) -> Chronicle:
    """The chronicling space over one person. Reads `p`'s own `ledger`, `scar` and `conviction`; writes
    nothing, emits nothing, and leaves `content_hash` unchanged whether or not it is called."""
    reader = LedgerReader(p.ledger)
    subjects: list = []
    for c in p.ledger:
        if c.subject not in subjects:
            subjects.append(c.subject)
    aff = {k: n for k, n in (p.scar or {}).items() if k in AFFILIATIONS}
    held = set(p.conviction or {})
    return Chronicle(
        p.id, tuple(p.ledger),
        tuple((subj, reader.latest_about(subj)) for subj in subjects),
        _frozen(p.conviction),
        _frozen({k: n for k, n in (p.scar or {}).items() if k not in AFFILIATIONS}),
        _frozen({k: n for k, n in aff.items() if k in held}),
        _frozen({k: n for k, n in aff.items() if k not in held}))
