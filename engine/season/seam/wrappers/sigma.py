"""THE SOCIAL CONTEST SCENE'S CONTEST PROVIDER — the host adapter and the host INPUT BUILDER for the
`social_contest` module's σ-leverage roll (plan position `31a`, A-25; registered as
`@provider("contest", "social_contest")`, which the prize rows `a standing`, `a proposition` and `a matter`
name, ED-SC-0033 clause (2)). The file keeps its name because its automated mode is the σ-leverage roll
(`modules/social_contest/roll.py`'s docstring).

`04_CODE_ARCHITECTURE.md` §A.2:182 types `seam/wrappers/*` as writing *"nothing, ever"*, reading
*"the projection"*, returning *"a `Margin`"*, holding token *"none"*. This module is that row. It
DECIDES NOTHING: `contest_input` (the host input builder) derives a pool and reads the obstacle's raw
operands from what the actor and the subject genuinely have -- for a prize a room hears (`heard_by:`),
that includes the bench's and the opponent's LEDGERS through `queries/world_q.py`'s `reception` and
`proofs`, a read `04_CODE_ARCHITECTURE.md` §B.2:250 (F8) words for the fold's own ledger query and
§A.2:168 permits `world_q` ("any store, via World"): the tension is recorded in `hole_register.yaml`
H-215/H-216, not resolved here -- and freezes them into `queries/inputs.py::SocialContestInput` (the hostile half as the obstacle's
`reception` term, what the speaker brings -- `proofs`, a friendly bench's `favour` -- as leverage, B05.17);
`resolve` (the adapter) calls the module entry the prize row names (`module_entry:`, registered in
`manifest.MODULE_ENTRIES` from its composition row), keeps S27.4's refusal on the pair it returns, and
otherwise returns what it returned -- the net/ob pair as a dict, the shape `combat_seam` already returns
and `degree_of` already grades. It NEVER returns a band; `seam/ladder.py` reads one by calling
`degree_from_net`, which is the single owner. The roll itself is `modules/social_contest/roll.py`,
reached by string.

⚠ THIS DOCSTRING NAMES NO BAND, ON PURPOSE.
`tests/valoria/test_degree_ladder_single_owner.py`'s `_PRODUCES_BAND` scan reads raw file TEXT
INCLUDING DOCSTRINGS and flags any file where two or more band names appear in a produce-shape. Keep it
band-free.

RULED, ED-SC-0037. JORDAN, 2026-09-09, VERBATIM: *"we have the sigma leverage d10 resolver in
engine to use."*

The σ layer is `net_boost`, the μ-shift ED-884 / ED-934 ruled, *"base_ob untouched, Ob floor never
breached"*; `roll_net_continuous` alone applies zero σ-leverage. The composition lives in the module
(`modules/social_contest/roll.py`).

THE HOST DERIVES NO OBSTACLE: it is composed by the social contest module
(`modules/social_contest/roll.py::obstacle`, ceiling included, `H-213`), ED-SC-0033 clause (3)'s single
owner.

⚠ PLACEMENT: `04 §A.2` reads *"one wrapper per **deferred subsystem**"* (amended, ED-IN-0284 and
ED-IN-0285; see 04:147-151), and `sigma_leverage` is an in-engine resolver under `engine/dice_engine/`.
This module is a wrapper BY ROLE -- it writes nothing, returns a margin, holds no token, which is the
`04:182` row, and a module satisfying that contract IS that row whatever supplies the margin.
⚠ COLUMN 3, *"a `Margin`"*, IS MET AT THE MODULE BOUNDARY AND NOT AT THE SEAM'S. The module entry
returns `queries/inputs.py::Margin` and `resolve` refuses any other return, naming the entry -- so a
winner (the kernel's `((band, reason), bout)`, or a dict carrying one) cannot cross. What `resolve`
hands the SEAM is the dict every provider returns: typing the seam's return across all three providers
is a `seam/` item of its own, and `combat`/`mass_battle` return a scene and a field, not a margin.
Column 2 is *"the projection"* and the signature takes `w`, a World -- the ADAPTER's does; the MODULE
reads only the typed record `contest_input` builds. `combat.resolve(w, …)` is the precedent **for the
deviation, not for conformance.**

⚠ THE PRECEDENT IS `seam/wrappers/combat.py`: derive exactly what the actor genuinely has, leave every
other operand at its registered fixture, and return a typed gap rather than fabricate a party.

⚠ THIS MODULE IMPORTS NOTHING FROM `systems/` OR `modules/` AND INSERTS NO `sys.path`. The roll is
reached by STRING: the composition row `social_contest.roll` names it, the registrar resolves it at
driver construction into `MODULE_ENTRIES`, and `resolve` below looks it up there by the role its
prize row names. NO entry is added to
`tests/valoria/test_engine_does_not_import_systems.py::PATH_SEAM_ALLOWED`. That set is shrink-only.
"""
from __future__ import annotations

import copy
import functools
import math
import sys
from dataclasses import asdict
from types import MappingProxyType, SimpleNamespace
from typing import Any, Mapping, NamedTuple, Optional

from engine.dice_engine.dice_engine import BAND_FLOORS, DEGREE_LABEL, DEGREE_ORDINAL, MARGIN_SCALE, Degree
from engine.dice_engine.draw import Draw
from engine.dice_engine import fmath
from engine.dice_engine.fmath import ltr_sum
from engine.dice_engine.sigma_leverage import level as sigma_level, levels_to_net_sigma, record_odds
from engine.substrate import composition, descriptors

from ...data.affiliations import AFFILIATION_CEILING
from ...data.arrangements import ARRANGEMENTS, CONTEXT, DISPOSAL, RITES, abridged
from ...data.rosters import STANCE_MAX
from ...data.rosters import (AUTHORITY_BY_FACTION, DIFFICULTY_LEVELS, GROUNDS, ISSUE_RUNGS, MATTERS, PROCEEDING_ENDS, PROCEEDING_MOVES,
                             PROOF_KIND_OF_SOURCE, RUNG_KINDS)
from ...data.rosters import capability_rows, obstacle_bound, require_use_site, roster, when_holds
from ...data.verbs import SOCIAL_ROLL_PROVIDER, VERB_CAPABILITY, VERB_TABLE, _OPENERS_FROM_EFFECTS
from ...gaps import InstrumentDefect, Unspecified
from ...loop.sides import _contests_of, sides_of
from ...queries.person_q import (BEARING_PARTS, believed_capability, believes, bearing, conflict, false_items, stance_toward, strain_carried,
                                 takes_side, tie)
from ...queries.person_q import care as person_care
# ⚠ THE LEAF, NOT THE PACKAGE'S RE-EXPORT. `manifest/providers.py` imports nothing, so no import
# here closes a loop back into this package (`_entry.py` says the same of the entry lookup);
# `manifest/registry.py` imports only `data/` and `gaps` and `queries/` is below `seam/`, so the
# two imports below close none either.
from ...manifest.providers import provider
from ...manifest.registry import (BELIEVED_ESTIMATE_ROLE, BENCH, HEARD_BY_ROOMS, RESIDENTS, SEAT_BODY, TOWARD_TO, call as _provider_for,
                                  resolve as _prize_row)
from ...queries import world_q as _world_q
from ...queries.inputs import Card, Input, Item, Margin, Outcome, Point, Present, Rite, SocialContestInput
# The room's two resolver-side reads. The host READS them; the module composes the obstacle they move.
from ...queries.world_q import docketed_under, faction_holding, hold_force, judging_set, place_of, presence, proofs, reception, residence_of
from ...state.carriers import EFFORT, effort_of
from ...state.gate import BENCH_BASIS, UNDECLARED_DISPOSAL, sits_over
from ._entry import entry_for
from .pool import (POOL_ADDENDS, _capability, faculty, governing_attribute, governing_score, rank, opposing_attribute, pool_pair, register_pool_addend,  # noqa: F401  (moved: see pool.py)
                   score, untrained)
from .pool import attribute_midpoint

# The prize rows' `provider:` string (`rosters.yaml` `contest_subsystems`): the module's one identity
# (A-25), so the row says the social contest module runs its own prizes. Reached by that string only.
_PROVIDER = SOCIAL_ROLL_PROVIDER   # one owner of the name (`data/verbs.py`), which the loader's `difficulty:` refusal reads too
_RESOLVER = "d_sigma"


# `_capability`, `POOL_ADDENDS`, `register_pool_addend`, `governing_attribute` and `faculty` live in `pool.py` (the one pool reader),
# imported at the top of this module; see its docstring.


def _opposition_of(w: Any, subject: Optional[str], verb: str) -> Optional[float]:
    """The subject's SKILL SCORE for the verb, or `None` -- a READ, not an obstacle: `pool.score`, the held rank on the verb's
    skill (never below the untrained score, `pool_default`, where he holds none), and nothing else: no base dice, no practice
    addend, no seat, no attribute (B05.11, TWO Edit B, CAP B4: the attribute is a level, not a score, A-7). A PERSON SUBJECT
    ALWAYS HAS A SCORE, so an unauthored hearer is no harder to move than one holding the skill
    at `pool_default` and a higher rank is harder (H-312's `interrogate`). `None` for nobody opposite (a record, a rung, a
    proposition, a person with no entry) and for a person with no score (a skill row saying `untrained: none` that he holds no
    rank in): the module's `opposed_ob(pool_default)` stands there.

    The obstacle is composed by `modules/social_contest/roll.py::obstacle` (ED-SC-0033 clause (3), *the
    obstacle has a single owner*). What is here is the half only the host can do: reading `World` for the
    score a PERSON subject brings. What the record carries as his `opposition` is this PLUS his opposing attribute (`_opposing`)."""
    if subject and subject in w.persons:
        opposing = score(w, w.persons[subject], verb)
        return None if opposing is None else float(opposing)
    return None


def _opposing(w: Any, subject: Optional[str], verb: str) -> Optional[float]:
    """WHAT A PERSON OPPOSITE BRINGS to the act (A-79, A-137: the resisting attribute mirrors the attribute in the dice): his skill
    score (`_opposition_of`) PLUS his opposing attribute (`pool.opposing_attribute`, the verb row's `opposed_attribute:` as he holds
    it, the scale's mid-point where he holds none (B05.16), nothing where the row names none). `None` where nobody is opposite. THE OPERAND of
    the obstacle's `opposition` member: `roll.py::obstacle` reads it at `opposed_ob(.., opposition_rate)`."""
    skill = _opposition_of(w, subject, verb)
    if skill is None:
        return None
    attribute = opposing_attribute(w.fixtures, w.persons[subject], verb)
    return skill + (0.0 if attribute is None else float(attribute))


def _effort_levels(fx: Any, operands: dict) -> tuple:
    """`effort`'s levels (CP-T01-05): an act at effort `e` brings `e` copies of the `effort_level` fixture
    (a `sigma_leverage.LEVEL_SIGMA` name, shipped `moderate`) -- one named level per slot of effort, all FOR the roller:
    `(levels, [])`. None at effort 0, so the shipped chooser, which forms no effort, adds nothing."""
    return [fx.get("effort_level")] * int(operands.get(EFFORT, 0)), []


# ---------------------------------------------------------------------------------------------
# THE `capability` SOURCE (B05.10, ADV Edit A, MAP §G edit 6): the `edge` rows of the act's site, ONE function for every skill, attribute and
# trait a row names, so none needs a function of its own. A row's `key` is read off the person its `side` names (`actor`: the roller,
# his own to know; `subject`: the person he acts on); its `per` counts the held value into steps; its `level` is one `LEVEL_SIGMA` name a
# step; `against: true` flips the sign, so a count counts AGAINST the roller. `contest_input` and `believed_input` choose the rows that
# apply (`when`) and read each one's value, and hand them to the source as the `edge` operand: `((row, key, value), ...)`.
# ---------------------------------------------------------------------------------------------
EDGE = "edge"                      # the operand key of the selected `edge` rows, beside `EFFORT`
CAPABILITY = "capability"          # the roster member (`rosters.yaml: advantage_sources`)
_UNKNOWN = object()                # a value the believer cannot read: `believed_input` answers `None`, never a guess


CIRCUMSTANCE = "circumstance"      # the role whose rows the obstacle's member `capability` reads (B05.15), selected and read as `edge`'s are


def _site_rows(role: str) -> tuple:
    """The `social_roll` site's rows of `role` (`edge`, `circumstance`), in table order (none ship; a planted or authored row is read here)."""
    return tuple(r for r in capability_rows(SOCIAL_ROLL_SITE) if r.role == role)


def _edge_key(row: Any, verb: str):
    """The key `row` reads for `verb`: `verb` is the skill the verb names, `verb.base` the first attribute the verb row governs by
    (`pool.governing_attribute`'s read); any other key is its own. `None` where the verb names none (the row then reads nothing)."""
    if row.key == "verb":
        return VERB_CAPABILITY.get(verb) or None
    if row.key == "verb.base":
        v = VERB_TABLE.get(verb)
        return v.governing[0] if v is not None and v.governing else None
    return row.key


def _held_at(person: Any, row: Any, key: str, verb: str):
    """What `person` HOLDS at `key`: a skill's rank (`None` where he holds none), an attribute's score (`None` where unauthored),
    a trait as 1 if held else 0 (A-107). `verb.base` reads through `pool.governing_attribute`."""
    if row.key == "verb.base":
        return governing_attribute(person, verb)
    if key in descriptors.TRAITS:
        return 1 if key in (getattr(person, "traits", None) or ()) else 0
    if key in descriptors.CAPABILITIES:
        return (getattr(person, "capability", None) or {}).get(key)
    if key in descriptors.ATTRIBUTES:
        return (getattr(person, "attributes", None) or {}).get(key)
    raise Unspecified(f"an `edge` row at the social roll keys {key!r}, which no person holds on this tree (not a skill, an attribute or a trait)",
                      "rosters.yaml -- tables: capability_uses", needs="a skill, an attribute or a trait key",
                      law="B05.10 -- the `capability` source reads what a person holds; a practitioner stat has no reader here")


def _edge_side(row: Any) -> str:
    """The side an `edge` or `circumstance` row reads: the roller's (`actor`) or the person he acts on (`subject`). `each` is a fight's word."""
    if row.side not in ("actor", "subject"):
        raise Unspecified(f"a `{row.role}` row at the social roll has side {row.side!r}", "rosters.yaml -- tables: capability_uses",
                          needs="`side: actor` or `side: subject`", law="U1 §3 item 3 -- a roll with one roller and one subject reads those two sheets")
    return row.side


def _edge_reads(verb: str, actor: Any, subject_read, role: str = EDGE) -> Any:
    """`((row, key, value), ...)`: the rows of `role` (`edge`; `circumstance`, B05.15) this act brings, in table order, each with the value its side holds, a row whose
    `when` fails for that holder left out (`rosters.when_holds`, the one comparison). `subject_read(row, key)` answers the subject's
    side: `(holder, value)`, `None` where there is no one to read (not a person, or himself: nobody opposes himself), or `_UNKNOWN`
    (the believer holds no claim), which makes the whole answer `_UNKNOWN`."""
    out = []
    for row in _site_rows(role):
        key = _edge_key(row, verb)
        if key is None:
            continue
        if _edge_side(row) == "actor":
            holder, value = actor, _held_at(actor, row, key, verb)
        else:
            got = subject_read(row, key)
            if got is _UNKNOWN:
                return _UNKNOWN
            if got is None:
                continue
            holder, value = got
        if when_holds(row, holder):
            out.append((row, key, value))
    return tuple(out)


def _edge_scale(key: str) -> tuple:
    """`(floor, ceiling)` of the scale `key`'s value lives on: an attribute's or a practitioner stat's (`descriptors.scale_of`), a skill's own."""
    if key in descriptors.CAPABILITIES:
        row = descriptors.CAPABILITIES[key]
        return row.floor, row.ceiling
    return descriptors.scale_of(key)


def _edge_levels(row: Any, key: str, value: Any) -> tuple:
    """`(levels for the roller, levels against him)` of one selected row. The count is `per: held` 1 if held, `per: rank` the held rank,
    `per: mid` the signed WHOLE steps of the value from its scale's mid-point (an unauthored value IS the mid-point: zero steps; a
    half step is no step); `against: true` negates it; a positive count is that many copies of the row's `level` FOR the roller, a
    negative one that many AGAINST him."""
    if row.per == "held":
        n = 1 if value else 0
    elif row.per == "rank":
        n = int(value or 0)
    elif row.per == "mid":
        floor, ceiling = _edge_scale(key)
        mid = (floor + ceiling) / 2
        n = math.trunc((mid if value is None else value) - mid)
    else:
        raise Unspecified(f"an `edge` row at the social roll ({row.key!r}) has per {row.per!r}", "rosters.yaml -- tables: capability_uses",
                          needs="`per: held`, `per: rank` or `per: mid`", law="U1 §3 item 2 -- an edge row counts its held value one of three ways")
    n = -n if row.against else n
    return ([row.level] * n, []) if n > 0 else ([], [row.level] * -n)


def _capability_levels(fx: Any, operands: dict) -> tuple:
    """THE `capability` SOURCE: `(levels for the roller, levels against him)` summed over the act's selected `edge` rows
    (`operands[EDGE]`, chosen and read by the input builders). `([], [])` where the act brings none -- the shipped case."""
    for_, against = [], []
    for row, key, value in operands.get(EDGE, ()):
        f, a = _edge_levels(row, key, value)
        for_.extend(f)
        against.extend(a)
    return for_, against


def _circumstance_ob(fx: Any, row: Any, value: Any) -> float:
    """What one selected `circumstance` row adds to the obstacle: the value its side holds times the row's `gain` (a fixture, successes per
    point held). A value not held (`None`) is 0: a circumstance punishes a want of nothing the holder lacks to count. The loader refuses a
    negative gain (A-25, B04.05), so a row never lowers the obstacle; the module refuses a negative term all the same."""
    return float(value or 0) * float(fx.get(row.gain))


# ---------------------------------------------------------------------------------------------
# THE `proofs` AND `favour` SOURCES (B05.17, PES-A edits 1 to 3; OBS §3): what the speaker BRINGS is leverage, never an obstacle reduction (`ED-884`,
# `ED-934`; P-232 holds by construction, not by a clamp). `proofs` is `world_q.proofs` (the remove-weighted, unmirrored sum), `favour` the bench's
# favourable `reception_gain x reception`; each is rounded half up to whole units, one named level a unit, all FOR the roller. The other side's
# standing items (the `proofs` defender list) wait on B24's cited items (U3 §4.1 row 20). A fixture of `None` is the control: no level.
# ---------------------------------------------------------------------------------------------
def _units(x: float) -> int:
    """Whole units of a quantity, rounded half up (OBS §3: "units round half up"); a negative quantity is no unit."""
    return int(max(0.0, x) + 0.5)


def _proof_levels(fx: Any, operands: dict) -> tuple:
    """`proofs`' levels: one `proof_level` per whole unit of `operands["proofs"]` -- FOR the roller: `(levels, [])`. Empty where the fixture is `None`."""
    level = fx.get("proof_level")
    return ([] if level is None else [level] * _units(operands.get("proofs", 0.0))), []


def _favour_levels(fx: Any, operands: dict) -> tuple:
    """`favour`'s levels: one `favour_level` per whole unit of `reception_gain x reception` where that is positive, and one per whole unit of the
    counterparty's favourable stance, `regard_step x clamp(stance_toward / STANCE_MAX, 0, 1)` (`operands["regard"]`, the signed clamp, B05.21; OBS §3
    names both quantities and each counts its own units) -- FOR the roller: `(levels, [])`. Empty where the fixture is `None`, and the stance half is
    empty at `regard_step` 0. The bench's and the counterparty's hostile halves are the obstacle's `reception` and `regard` members, never a level
    against him."""
    level = fx.get("favour_level")
    if level is None:
        return [], []
    units = _units(float(fx.get("reception_gain")) * operands.get("reception", 0.0))
    units += _units(float(fx.get("regard_step")) * max(0.0, operands.get("regard") or 0.0))
    return [level] * units, []


# ---------------------------------------------------------------------------------------------
# THE AUDIENCE A ROOM MEANS (B07.04, `U5c_VERBS_residue` §2 edit 2): ONE TABLE KEYED BY ROOM AND NOTHING ELSE. A prize row's `heard_by:` names a
# room (`manifest/registry.py::HEARD_BY_ROOMS`); `audience_of` answers the persons who hear an act in it, and `world_q.reception` and `proofs` take
# that tuple. No row of the table, and no branch around it, names a verb: the room is the prize row's, the act supplies only who acts, through
# which seat, and where.
# ---------------------------------------------------------------------------------------------
class HeardAct(NamedTuple):
    """The act as a room reads it: its actor, the seat it is exercised through (`Act.via`) and its place (the rung the seam hands the
    provider: the actor's own, or the venue a hand-built roll names)."""
    actor: str
    via: Optional[str]
    place: Optional[str]


def _bench(w: Any, act: HeardAct) -> tuple:
    """`bench`: who sits over the act's place -- `world_q.judging_set`, today's read."""
    return tuple(judging_set(w, act.place))


def _seat_body(w: Any, act: HeardAct) -> tuple:
    """`seat_body`: the seated persons of the body the act's seat belongs to (`Office.body`); a seat of no body, the seated persons at that
    seat's rung. A seat the world lacks, or no seat, hears nobody."""
    seat = w.offices.get(act.via) if act.via is not None else None
    if seat is None:
        return ()
    peers = [oid for oid, o in w.offices.items()
             if (o.body == seat.body if seat.body is not None else seat.rung is not None and o.rung == seat.rung)]
    held = (hold_force(w, oid) for oid in peers)
    return tuple(dict.fromkeys(t.subject for t in held if t is not None and t.subject in w.persons))


def _residents(w: Any, act: HeardAct) -> tuple:
    """`residents`: the persons whose live `reside` edge is the act's place (`world_q.residence_of`, RESIDENTS, not persons present)."""
    return () if act.place is None else tuple(p for p, at in residence_of(w).items() if at == act.place)


_AUDIENCES = {BENCH: _bench, SEAT_BODY: _seat_body, RESIDENTS: _residents}
if set(_AUDIENCES) != HEARD_BY_ROOMS:
    raise Unspecified(
        f"`audience_of`'s table keys {sorted(_AUDIENCES)} are not `HEARD_BY_ROOMS` {sorted(HEARD_BY_ROOMS)}", "04 PART E step 10",
        needs="one row of the table for each room a prize row may name",
        law="a room `_check_heard_by` admits and no reader answers would hear nobody, silently")


def audience_of(w: Any, act: HeardAct, room: str) -> tuple:
    """The persons who hear `act` in `room`: the one reader of what a room name means, by room alone."""
    return _AUDIENCES[room](w, act)


# ---------------------------------------------------------------------------------------------
# THE `office` SOURCE (B05.20, U1-D, D-U1-01 and D-U1-01a; OBS §3): a seat's `modifier:` is ONE named level for an act exercised THROUGH that seat
# (`Act.via`), in a room its bench sits over. `_seat_modifier` is the one reader of the seat's row value: it answers only where the
# prize row names a room (`heard_by:`; `room` is the act's rung, else `None`) and `state/gate.py::sits_over` holds (the bench's own containment
# test, the one `world_q.judging_set` asks). It is FOR the roller only (OBS §3: the defender column is struck) and enters the sigma
# term alone: never a die in the pool, never a term of the opposition. A seat declaring none (`None`), an act through no seat and a
# prize no bench hears bring no level, so the roll is as it was.
# ---------------------------------------------------------------------------------------------
OFFICE = "office"                  # the roster member (`rosters.yaml: advantage_sources`) and its operand key


def _seat_modifier(w: Any, via: Optional[str], room: Optional[str]) -> Optional[str]:
    """The `LEVEL_SIGMA` name the seat `via` brings to a roll heard in `room`, or `None`: the seat's `Office.modifier` where the
    seat sits over the room; `None` for no seat, a seat that is not in the world, a seat declaring none or no room."""
    seat = w.offices.get(via) if via is not None and room is not None else None
    return seat.modifier if seat is not None and seat.modifier is not None and sits_over(w, seat, room) else None


def _office_levels(fx: Any, operands: dict) -> tuple:
    """`office`'s levels: the one level of `operands["office"]` (a `_seat_modifier`'s answer) -- FOR the roller: `([level], [])`; `([], [])` where
    there is none. The defender column is struck (D-U1-01, OBS §3)."""
    level = operands.get(OFFICE)
    return ([] if level is None else [level]), []


# ---------------------------------------------------------------------------------------------
# THE `wounds` SOURCE (B05.60, ADV Edits B to D; `29_DICE` item 29-4 step 5; A-8): a wound is a NAMED LEVEL on the roll its bearer makes, never an obstacle
# term and never a die. One `wound_level` AGAINST the roller per `wound_step` of body his person has lost below his ceiling, one FOR him per
# `wound_step` the person he acts on has lost (the bearer's wound helps the roller when the bearer defends), each side at most `wound_levels_max`.
# The operands are the persons' own `body` and `body_ceiling` (`_advantage_operands`); a `wound_level` of None is the control and brings none.
# ---------------------------------------------------------------------------------------------
WOUNDS = "wounds"                  # the roster member (`rosters.yaml: advantage_sources`)


def _wound_count(fx: Any, body: Any, ceiling: Any) -> int:
    """Whole `wound_step`s of body lost below the ceiling, at most `wound_levels_max`: 0 where none is lost (or the ceiling is not stated)."""
    lost = int(ceiling) - int(body)
    if lost <= 0:
        return 0
    return min(int(fx.get("wound_levels_max")), lost // int(fx.get("wound_step")))


def _wound_levels(fx: Any, operands: dict) -> tuple:
    """THE `wounds` SOURCE: `(levels for the roller, levels against him)`. One named level AGAINST the actor per `wound_step` of body he has
    lost below his ceiling, and one level FOR the actor per `wound_step` his person subject has lost, each capped at `wound_levels_max`
    (A-8: bilateral). `([], [])` when `wound_level` is None (the control)."""
    level = fx.get("wound_level")
    if level is None:
        return [], []
    n_actor = _wound_count(fx, operands.get("body", 0), operands.get("body_ceiling", 0))
    n_subject = _wound_count(fx, operands.get("subject_body", 0), operands.get("subject_body_ceiling", 0))
    return [level] * n_subject, [level] * n_actor


# THE ADVANTAGE CHANNEL'S BINDING: each member of `rosters.yaml: advantage_sources` -> the function that
# returns the named levels it brings to an act, `fn(fixtures, operands) -> (levels for the roller, levels against him)`, each a
# list of level names. THE ROSTER IS
# THE CLOSED SET AND THIS IS ITS BINDING: refused at import if the two disagree, so a member with no function
# (it would silently add nothing) and a function with no member (it would silently never run) are both loud.
def _bound_to(binding: dict, roster_name: str, law: str = "OBS §1 -- the roster is the closed set and the binding is its only reader",
              members: Optional[tuple] = None) -> dict:
    """`binding` (member -> host function) checked against `rosters.yaml: <roster_name>`, both ways: a member
    with no function would silently add nothing, a function with no member would silently never run. Returns the binding in the
    roster's order. `members` narrows the roster to the part this host reads (`obstacle_bound("host")`, B24p.05: the module-bound
    members have no host function and must not)."""
    members = roster(roster_name, ordered=True) if members is None else members
    if set(binding) != set(members):
        raise Unspecified(
            f"`{roster_name}` members {list(members)} and their host functions {sorted(binding)} differ", "rosters.yaml",
            needs="a function for every member and a member for every function",
            law=law)
    return {name: binding[name] for name in members}


ADVANTAGE_SOURCES = _bound_to({EFFORT: _effort_levels, CAPABILITY: _capability_levels, "proofs": _proof_levels, "favour": _favour_levels,
                               OFFICE: _office_levels, WOUNDS: _wound_levels}, "advantage_sources",
                              law="CP-T01-05 -- the roster is the only door into the social roll's sigma term")


def advantage_levels(fx: Any, operands: dict) -> tuple:
    """`((source, levels for the roller, levels against him), ...)`: every `advantage_sources` member's named levels for this act, in roster order
    (a source with nothing to say carries two empty lists). THE ONE CALL OF EVERY SOURCE: `advantage_sigma` sums these and `resolve`'s `levels` counts
    them (OBS §5), so the sigma rolled and the levels recorded cannot disagree."""
    return tuple((name, *ADVANTAGE_SOURCES[name](fx, operands)) for name in roster("advantage_sources", ordered=True))


def advantage_sigma(fx: Any, operands: dict) -> float:
    """The social roll's net sigma, SIGNED: every `advantage_sources` member's named levels for this act, those that favour the roller
    and those that count against him, summed through `levels_to_net_sigma(for, against)` (a mu-shift the roll applies as `net_boost`;
    never a flat bonus on the net, never an Ob reduction). `operands` is what the act brings (`_advantage_operands`: effort, the `edge`
    rows, the room's `proofs` and `reception`); 0.0 when nothing does."""
    for_, against = [], []
    for _name, f, a in advantage_levels(fx, operands):
        for_.extend(f)
        against.extend(a)
    return levels_to_net_sigma(for_, against)


def _advantage_operands(effort: int, edge: tuple, room_terms: dict, office: Optional[str] = None, regard: Optional[float] = None,
                        body: Optional[tuple] = None, subject_body: Optional[tuple] = None) -> dict:
    """WHAT THE ACT BRINGS, named once: `contest_input` and `believed_input` both reach the sources through here, so they cannot diverge.
    `office` is `_seat_modifier`'s answer for the seat the act is exercised through (B05.20), the host's own read, `None` for none. `regard` is
    `_regard_of`'s answer (B05.21), the counterparty's signed stance in the clamp unit, `None` where no one person stands alone opposite.
    `body` is `(body, body_ceiling)` of the actor and `subject_body` the same of a person subject (B05.60, the `wounds` source's operands); a
    subject whose body is not the reader's to know (`believed_input`) is `None`, which reads as nothing lost."""
    body_op = {} if body is None else {"body": body[0], "body_ceiling": body[1]}
    subject_op = {} if subject_body is None else {"subject_body": subject_body[0], "subject_body_ceiling": subject_body[1]}
    return {EFFORT: effort, EDGE: edge, "proofs": room_terms.get("proofs", 0.0), "reception": room_terms.get("reception", 0.0), OFFICE: office,
            "regard": regard, **body_op, **subject_op}


def _body_of(person: Any) -> Optional[tuple]:
    """`(body, body_ceiling)` of a person, the `wounds` source's operand pair; `None` for no person."""
    return None if person is None else (person.body, person.body_ceiling)


def _levels_count(levels: tuple) -> tuple:
    """`((source, aggressor n, defender n), ...)`: `advantage_levels`' lists as counts (OBS §5; SC-P1 reads them in B05.18)."""
    return tuple((name, len(f), len(a)) for name, f, a in levels)


def contest_input(w: Any, claimants: list, *, verb: str = "",
                  subject: Optional[str] = None, room: Optional[str] = None,
                  examined: Optional[str] = None, effort: int = 0, via: Optional[str] = None,
                  heard_by: str = BENCH, toward: Optional[str] = None) -> SocialContestInput:
    """THE HOST INPUT BUILDER's record alone: `_read_social_roll`'s first return (see it for the body, for the
    rows' reads and for the levels, which `resolve` takes from the same call)."""
    return _read_social_roll(w, claimants, verb=verb, subject=subject, room=room, examined=examined, effort=effort, via=via,
                             heard_by=heard_by, toward=toward)[0]


def _read_social_roll(w: Any, claimants: list, *, verb: str = "",
                      subject: Optional[str] = None, room: Optional[str] = None,
                      examined: Optional[str] = None, effort: int = 0, via: Optional[str] = None,
                      heard_by: str = BENCH, toward: Optional[str] = None) -> tuple:
    """THE HOST INPUT BUILDER (plan position `31a`, A-25): `World` -> the frozen record the roll reads. Returns
    `(record, reads, levels)`: the record `contest_input` hands out, for each `social_roll` row of `tables.capability_uses`
    (table order), `(row, value)` -- the value the row's reader read, so the record `resolve` returns names what fed the
    roll and cannot disagree with what was rolled (CAP A6, MAP §D) -- and `levels`, `((source, aggressor n, defender n), ...)`,
    the count of the named levels each `advantage_sources` member brought, from the same calls `leverage` sums (OBS §5). `dice` reads the actor's score (`pool.score`, the base
    `faculty` adds its addends to) and gives the pool; `opposes` reads the opposition (`_opposition_of`, `None` for nobody
    opposing). The roll reads each term ONLY through its row: a table with no `opposes` row rolls with opposition `None`,
    and with no `dice` row a pool of 0 (nothing read the actor's score).

    Reads `w.persons` (the actor, `claimants[0]`, and a person subject), `w.fixtures`, `w.records` (the
    Record an inquiry examines) and, for a prize a room hears, the bench's and the opponent's ledgers
    through `queries/world_q.py::reception` and `proofs`; the module that consumes the record never sees
    `World`. §A.2's wrapper row types the column *"the projection"*: this builder reads `World`, the
    deviation named above (`combat.resolve` is its precedent), CONVENTION. Its precondition is the adapter's
    PARTY-GAP checks (`resolve`, below): at least one claimant, and the first a person.
    `leverage` is the sum of the named levels the `advantage_sources` roster brings to the act
    (`advantage_sigma`; CP-T01-05's `effort` is the first member) and is 0.0 when nothing does -- the
    honest form while nothing supplies it: a fabricated leverage would be a number nobody chose.
    `effort` is the act's own (`state/carriers.py::effort_of`), passed by the adapter. `via` is the seat the act is exercised through
    (`Act.via`), passed by the adapter: the `office` source reads its `modifier` where the room's bench is over it (`_seat_modifier`).
    The obstacle's operands are carried RAW (`even`'s `pool_add`,
    `difficulty`, `opposition` with `pool_default` and `opposition_rate`, `obstacle_ceiling`: `obstacle_operands` below); the module composes them.

    `room` is the act's rung where a room hears the contest, or `None`: the adapter passes the
    act's rung when the prize row names a `heard_by:` (`manifest.resolve`), and nothing otherwise. `heard_by` is that room's name
    (a hand-built roll that names a rung and no room is heard by the bench, as before) and `toward` the prize row's `toward:`; the audience
    is `audience_of`'s answer for the room, never a branch on the verb.
    With a room, the record carries the audience's `reception` of the actor (of the receiver, `toward: to`) and the actor's unmirrored
    `proofs` against the subject (`queries/world_q.py`, both read raw) and their two gains; without
    one they stay at the record's no-room defaults, so a `tell`, a `determine` or an inquiry rolls
    with no room terms.

    `examined` is the subject an INQUIRY examines, or `None`: the adapter passes
    the act's subject when there is no prize (an inquiry or a task, `graded_tasks`' route), and nothing
    otherwise. Where it names a Record, the record carries that Record's `forgery_quality` (read from
    `w.records`, the one read this builder adds), which the module adds to the obstacle; a site, a
    person, or a contest a prize names carries `0`."""
    fx = w.fixtures
    docketed = _docketed_row(w, subject)                                        # the arrangement row the act's matter is heard under, if one is docketed (B05.21)
    room_terms = {}
    if room is not None:
        audience = audience_of(w, HeardAct(claimants[0], via, room), heard_by)
        # `toward: to` (U5c §2 edit 4): the room is asked about the receiver, here the act's person counterparty [ASSUMPTION: `to` is the roll's `subject`; no row declares it until `a holding`'s verb lands].
        room_terms = dict(reception=reception(w, subject if toward == TOWARD_TO else claimants[0], audience),
                          reception_gain=fx.get("reception_gain"),
                          proofs=proofs(w, claimants[0], subject, audience, admitted=_admitted_proofs(fx, docketed)))
    doc = w.records.get(examined) if examined is not None else None
    # NOBODY OPPOSES HIMSELF (v10 CP-T05-02 (ii), AM-D-02): a subject who IS the actor (the self-plea,
    # `speak {subject: himself}`) brings no opposition -- his own score is not an obstacle to himself --
    # so his opposition is `None` and the module opposes him at `opposed_ob(pool_default)` (B05.14: never absent), the same at any capability he holds.
    #
    # THE ROLL READS ITS TERMS ONLY THROUGH THE SITE'S ROWS (CAP A6): a `dice` row's read gives the pool (and the score
    # it is built on), an `opposes` row's read gives the opposition; no `opposes` row means opposition `None`, as a
    # self-plea. A row the table omits is a term the roll does not read, so `fed_by` and the roll cannot disagree.
    actor = w.persons[claimants[0]]
    rows = _social_rows()
    roles = {r.role for r in rows}
    opposition = None
    if "opposes" in roles and subject != claimants[0]:
        opposition = _opposing(w, subject, verb)
    pool = faculty(w, actor, verb) if "dice" in roles else 0
    # THE `capability` SOURCE'S ROWS (B05.10): each `edge` row of the site whose `when` holds, with the value its side holds. A subject
    # who is the actor, or is no person, is read for nothing (nobody opposes himself).
    other = w.persons.get(subject) if subject and subject != claimants[0] else None
    subject_read = lambda row, key: None if other is None else (other, _held_at(other, row, key, verb))
    edge = _edge_reads(verb, actor, subject_read)
    circumstance = _edge_reads(verb, actor, subject_read, CIRCUMSTANCE)         # the `capability` obstacle term's rows (B05.15)
    office = _seat_modifier(w, via, room)                                       # the seat's own level, where its bench is over the room (B05.20)
    regard = _regard_of(w, claimants[0], subject, room)                         # the counterparty's stance toward the actor, signed, in the clamp unit (B05.21)
    bodies = (_body_of(actor), _body_of(other))                                 # the `wounds` source's operands: his own body, and a person subject's (B05.60)
    inp = _frame(fx, pool, opposition, doc.forgery_quality if doc is not None else 0.0, room_terms, effort, verb, edge, circumstance, office,
                 docketed=docketed, heard=room is not None, regard=regard, bodies=bodies)
    levels = _levels_count(advantage_levels(fx, _advantage_operands(effort, edge, room_terms, office, regard, *bodies)))     # the same sources `leverage` summed (OBS §5)
    read = {"dice": governing_score(w, actor, verb) + rank(actor, verb) if "dice" in roles else None, "opposes": opposition}   # the pool's own base (B05.25), not `score`
    chosen = {id(r): (value, levels_to_net_sigma(*_edge_levels(r, key, value))) for r, key, value in edge}
    chosen.update({id(r): (value, _circumstance_ob(fx, r, value)) for r, key, value in circumstance})
    return inp, tuple((r, *chosen[id(r)]) if id(r) in chosen else (r, read[r.role], None)
                      for r in capability_rows(SOCIAL_ROLL_SITE) if id(r) in chosen or r.role in read), levels


#: `rosters.yaml: capability_use_sites`' site whose one reader is `contest_input` (the single roll's dice and opposition).
SOCIAL_ROLL_SITE = require_use_site("social_roll")


def _social_rows() -> tuple:
    """The `social_roll` site's rows that give the roll a term (`dice`, `opposes`), in table order: the ONE place the roll's two
    builders -- the dealt roll (`_read_social_roll`) and the person's believed one (`believed_input`) -- ask which terms the table
    gives it, so they cannot compose different obstacles from one table (`_frame`). The loader pins each row's `key` and `side`
    and allows one of each role (`rosters.yaml: capability_site_reads`), so the role alone says what the reader reads."""
    return tuple(r for r in capability_rows(SOCIAL_ROLL_SITE) if r.role in ("dice", "opposes"))


def _fed_by(reads: tuple, inp: SocialContestInput, terms: tuple) -> tuple:
    """`((use, role, key, side, value, contributed), ...)` -- every row that fed the roll, in table order (MAP §D; the
    record is `resolve`'s, never an `Event` field, D-U1-06). `value` is what the row's reader read (`_read_social_roll`);
    `contributed` is what it added to the roll: the pool for `dice`, the module's own `opposition` term of the obstacle for
    `opposes` (read off `Margin.terms`, the module that composed it; `0.0` where nobody was opposite, though the term then stands
    at `opposed_ob(pool_default)`: the row read nothing, so it fed nothing)."""
    contributed = {"dice": inp.pool, "opposes": dict(terms).get("opposition", 0.0) if inp.opposition is not None else 0.0}
    return tuple((r.use, r.role, r.key, r.side, value, contributed[r.role] if own is None else own) for r, value, own in reads)


# ---------------------------------------------------------------------------------------------
# THE OBSTACLE'S OPERANDS (B05.14; OBS §1): each member of `rosters.yaml: obstacle_terms` is read by ONE host function.
# ---------------------------------------------------------------------------------------------


def _even_term(fx: Any, facts: dict) -> dict:
    """`even`: the pool's base, `pool_add`, as the `social_roll` site's `dice` row names it (`pool.pool_pair`) -- the base that makes
    the pool is the base whose even line (`MU_PER_DIE x pool_add`) the obstacle starts at. The module derives the line."""
    return {"pool_add": pool_pair(fx)[0]}


def _difficulty_term(fx: Any, facts: dict) -> dict:
    """`difficulty`: the size (`Fixtures.difficulty_ob`) of the level the verb's row names. A verb the table does not carry, or a row
    with no level (a row nothing rolls), is refused naming it: a task with no difficulty is a loud gap, never a default."""
    row = VERB_TABLE.get(facts["verb"])
    if row is None or row.difficulty is None:
        raise Unspecified(f"the social roll was asked to deal {facts['verb']!r}, which `verb_table.yaml` gives no `difficulty:`",
                          "verb_table.yaml -- difficulty", needs="a verb row the social roll deals, with its level",
                          law="B05.14 -- an obstacle is the act's difficulty and its terms, never a stand-in")
    return {"difficulty": fx.get("difficulty_ob")[row.difficulty]}


def _opposition_term(fx: Any, facts: dict) -> dict:
    """`opposition`: what a person opposite brings (`facts["opposition"]`: his skill score plus his opposing attribute, `_opposing`;
    `None` for nobody), with the untrained score the module stands in with where nobody is, and the rate it opposes at."""
    return dict(opposition=facts["opposition"], pool_default=untrained(fx), opposition_rate=fx.get("opposition_rate"))


def _reception_term(fx: Any, facts: dict) -> dict:
    """`reception`: the audience's hostility (OBS §2 member 8; B05.17, PES-A edit 4): the bench's signed regard for the speaker
    (`facts["reception"]`, `world_q.reception` over the room the prize row names; 0 where no room hears the act) read at its hostile half and
    scaled by `reception_gain`. ONE operand `("reception", max(0, -reception), reception_gain)`, always, so the member stands in the module's
    terms at 0.0 where the bench is neutral or friendly (the friendly half is `advantage_sources: favour`, never a lower obstacle)."""
    return {"obstacle_operands": (("reception", max(0.0, -float(facts.get("reception", 0.0))), fx.get("reception_gain")),)}


def _capability_term(fx: Any, facts: dict) -> dict:
    """`capability`: a circumstance that punishes a want (MAP §G edit 6; OBS §2 member 9): ONE function over the table's rows for the act's
    operands -- the `circumstance` rows of the act's site whose `when` holds (`facts["circumstance"]`, chosen and read by the input
    builders as the `edge` rows are), each its held value times its gain (`_circumstance_ob`), summed. ONE operand `("capability", sum,
    1.0)`, always, so the member stands in the module's terms at 0.0 where no row applies (the shipped case). [ASSUMPTION: the
    (raw, step) split -- the sum is the raw operand and the step is 1.0, the gain being already inside each row's term]"""
    return {"obstacle_operands": (("capability", ltr_sum(_circumstance_ob(fx, r, v) for r, _, v in facts.get("circumstance", ())), 1.0),)}


# ---------------------------------------------------------------------------------------------
# THE TUNING TABLES' THREE MEMBERS (B05.21; T13 T2, T3, T4; OBS §2 members 3, 5, 7). Each is a raw operand times a step, listed in the act's
# terms ONLY WHERE IT WEIGHS (`_weighing`): the terms are folded into the Event's `ending` and so into the content hash, and at their control
# sizes (every `standard` `plain`, `stakes_ob` 0, `regard_step` 0) these members must leave a world's terms as they were.
# ---------------------------------------------------------------------------------------------
def _weighing(name: str, raw: float, step: float) -> dict:
    """`{"obstacle_operands": ((name, raw, step),)}` where `raw x step` is above 0, else `{}` -- a member that weighs nothing is not listed."""
    return {"obstacle_operands": ((name, raw, step),)} if raw * step > 0 else {}


def _docketed_row(w: Any, subject: Optional[str]) -> Optional[dict]:
    """The `arrangements.yaml` row the act's matter (its `subject`) is docketed under, or `None`: nothing docketed, an item naming no row (every
    computed `open_case`, H-80), or more than one row on one matter (a hand-planted docket, which `_eff_determine` declines rather than choosing
    between: absence refuses, never a guessed row)."""
    rows = docketed_under(w, subject)
    (row,) = rows if len(rows) == 1 else (None,)
    return ARRANGEMENTS.get(row) if isinstance(row, str) else None


def _admitted_proofs(fx: Any, docketed: Optional[dict]) -> Optional[tuple]:
    """The proof kinds the docketed row admits, for `world_q.proofs`' filter -- or `None` for no filter: nothing docketed, or `proof_admission` `off`."""
    return tuple(docketed["admits"]) if docketed is not None and fx.get("proof_admission") == "on" else None


def _regard_of(w: Any, actor: str, subject: Optional[str], room: Optional[str]) -> Optional[float]:
    """THE COUNTERPARTY'S STANCE TOWARD THE ACTOR, SIGNED, IN THE CLAMP UNIT (T13 edit 6, C-03): `clamp(stance_toward(counterparty, actor) /
    STANCE_MAX, -1, 1)` -- his interior (his own stance rows naming the actor), not his ledger. `None` where the term does not apply: it is for ONE
    PERSON COUNTERPARTY AND NO AUDIENCE (an act a bench hears reads `reception` instead, never both), and nobody is his own counterparty."""
    other = w.persons.get(subject) if subject and subject != actor and room is None else None
    return None if other is None else max(-1.0, min(1.0, stance_toward(other, actor) / STANCE_MAX))


def _standard_term(fx: Any, facts: dict) -> dict:
    """`standard`: what the room demands (OBS §2 member 3; T13 T2): for an act a bench hears on a docketed matter, the size (`Fixtures.difficulty_ob`,
    the one ladder) of the `standard:` level of the row the matter is docketed under. Not listed where nothing is docketed, no bench hears the act or
    the level is `plain` (0). ⚠ THIS IS THE SINGLE ROLL'S FLAT TERM: inside a proceeding the same cell is the Grace the occasion asks, reached through
    Grace's `esteem` on the leverage and never an obstacle term (B24p.13): since B24p.19 an act that proceeds (`VerbRow.proceeds`) never reaches this
    composer at all (`proceeding_input` builds the rite's own `standard`, and `pool.governing_score` refuses the verb), so the term is the single
    roll's alone."""
    row = facts.get("docketed")
    return _weighing("standard", float(fx.get("difficulty_ob")[row["standard"]]) if row is not None and facts.get("heard") else 0.0, 1.0)


def _stakes_kind(fx: Any, verb: str, docketed: Optional[dict]) -> Optional[str]:
    """The Tenure kind `verb` would open, for `stakes_ob` -- read off the effects, never off a verb's name (`data/verbs.py::_OPENERS_FROM_EFFECTS`,
    which verbs open which kind): the one kind of `stakes_ob` the verb opens, or where it opens several, the kind a disposal opens -- the docketed row's
    `disposes:`, or `gate.UNDECLARED_DISPOSAL` where none is docketed (`_eff_determine`'s own reading) -- if that is among them. `None` otherwise."""
    opened = [k for k in fx.get("stakes_ob") if verb in _OPENERS_FROM_EFFECTS.get(k, ())]
    if len(opened) == 1:
        return opened[0]
    disposed = docketed["disposes"] if docketed is not None else UNDECLARED_DISPOSAL
    return disposed if disposed in opened else None


def _stakes_term(fx: Any, facts: dict) -> dict:
    """`stakes`: the weight of what the act would take or impose (OBS §2 member 5; T13 T4): `Fixtures.stakes_ob` of the Tenure kind the act opens
    (`_stakes_kind`: `arrest` opens `detain`; `determine` the kind its docketed row `disposes:`). Not listed where the act opens no such kind or the
    kind is sized 0."""
    kind = _stakes_kind(fx, facts["verb"], facts.get("docketed"))
    return _weighing("stakes", float(fx.get("stakes_ob")[kind]) if kind is not None else 0.0, 1.0)


def _regard_term(fx: Any, facts: dict) -> dict:
    """`regard`: the counterparty's hostility to the actor (OBS §2 member 7; T13 T3): `regard_step x clamp(-stance / STANCE_MAX, 0, 1)`, the hostile half
    of `facts["regard"]` (`_regard_of`, signed; `None` where there is no one person counterparty or a bench hears the act). Its favourable half is the
    `favour` source, never a lower obstacle (A-25). Not listed at `regard_step` 0 or for a hearer who is not hostile."""
    x = facts.get("regard")
    return _weighing("regard", max(0.0, -x) if x is not None else 0.0, fx.get("regard_step"))


#: Each member of `rosters.yaml: obstacle_terms` -> the ONE function that reads it: `fn(fixtures, facts) -> {record field: value}`. A member
#: that is a raw operand times a step returns `{"obstacle_operands": ((name, raw, step),)}` instead. Refused at import, both ways.
OBSTACLE_TERMS = _bound_to({fn.__name__[1:-len("_term")]: fn for fn in (
    _even_term, _difficulty_term, _opposition_term, _standard_term, _stakes_term, _regard_term, _reception_term, _capability_term)},
                           "obstacle_terms", members=obstacle_bound("host"))

PROCEEDING_ROLE = "social_contest.proceeding"   # the composition row whose module supplies the `bound: module` members (registered at B24p.12)


@functools.lru_cache(maxsize=None)
def _module_terms_checked() -> bool:
    """The `bound: module` members of `obstacle_terms` against the proceeding module's `TERMS` (B24p.05), once per process: refused if they
    differ (a module term that is no roster member would reach `Margin.terms` unnamed; a member the module never supplies would silently weigh 0).
    The row is registered (B24p.12) and this half is asserted there; the `False` return is for a tree whose `composition.json` carries no
    such row."""
    if PROCEEDING_ROLE not in composition.ROLES:
        return False
    terms = getattr(sys.modules[composition.require(PROCEEDING_ROLE).__module__], "TERMS")
    want = obstacle_bound("module")
    if set(terms) != set(want):
        raise Unspecified(f"`obstacle_terms` module-bound members {list(want)} and the proceeding module's `TERMS` {sorted(terms)} differ",
                          "modules/social_contest/proceeding.py -- TERMS",
                          needs="a `TERMS` key for every `bound: module` member and a member for every key",
                          law="B24p.05 -- the roster is the only door into the obstacle, for the module's terms as for the host's")
    return True


def check_module_terms() -> bool:
    """`True` once the module's `TERMS` have been read against the roster's `bound: module` members, `False` while the module is not registered."""
    return _module_terms_checked()


def obstacle_operands(fx: Any, facts: dict) -> dict:
    """THE OBSTACLE'S FIELDS OF THE RECORD, every roster member's function asked in roster order: `difficulty`, `pool_default`,
    `pool_add`, `opposition`, `opposition_rate` and `obstacle_operands` (the `(name, raw, step)` triples of the members that are an
    operand times a step, in roster order). `facts` is what the act is: its `verb`, the `opposition` its builder read (`None`
    for nobody), the room's `reception` and the `circumstance` rows it selected and read, and (B05.21) the `docketed` arrangement row (or `None`),
    whether a bench `heard` the act, and the counterparty's signed `regard` (or `None`). `contest_input` and `believed_input` reach it through `_frame` alone, so they cannot compose different obstacles."""
    check_module_terms()                       # the module's half of the roster, read at the first record built (B24p.05; `False` until it registers)
    fields: dict = {}
    operands: list = []
    for name, read in OBSTACLE_TERMS.items():
        got = dict(read(fx, facts))
        operands.extend(got.pop("obstacle_operands", ()))
        fields.update(got)
    return {**fields, "obstacle_operands": tuple(operands)}


def _frame(fx: Any, pool: float, opposition: Optional[float], forgery_quality: float,
           room_terms: dict, effort: int, verb: str, edge: tuple = (), circumstance: tuple = (),
           office: Optional[str] = None, docketed: Optional[dict] = None, heard: bool = False,
           regard: Optional[float] = None, bodies: tuple = (None, None)) -> SocialContestInput:
    """THE RECORD, FILLED THE ONE WAY: what `contest_input` (the true input) and `believed_input` (a
    person's) both hand the module. They differ in where the pool's opposition, the forgery quality
    and the room terms COME FROM; the fixtures and the record's shape are this
    function's alone, so the two modes cannot compose different obstacles from the same fields. THE ACT'S DIFFICULTY IS ALWAYS KNOWN to a
    believer (it is the verb row's, public), as are the fixtures' rate and base; only the opposition can be unknown to him
    (`believed_input` answers `None` for that, never a figure)."""
    return SocialContestInput(
        pool=pool,
        obstacle_ceiling=fx.get("obstacle_ceiling"),
        ceiling_per_pool=fx.get("ceiling_per_pool"),
        ceiling_form=fx.get("ceiling_form"),
        obstacle_refusal_multiple=fx.get("obstacle_refusal_multiple"),
        leverage=advantage_sigma(fx, _advantage_operands(effort, edge, room_terms, office, regard, *bodies)),      # the one place the operands are named
        forgery_quality=forgery_quality,
        **obstacle_operands(fx, dict(verb=verb, opposition=opposition, circumstance=circumstance,
                                     reception=room_terms.get("reception", 0.0), docketed=docketed, heard=heard, regard=regard)),
        **room_terms)


# ---------------------------------------------------------------------------------------------
# EXACT ODDS (CP-T01-03): what a roll of this record would deal, read and never rolled.
# ---------------------------------------------------------------------------------------------
# The claim a person holds about another's capability, and its one reader (`believed_capability`), are
# `queries/person_q.py`'s (B04.22: the read the confer term also makes). NOTHING DEPOSITS ONE TODAY, so a believed
# opposition is `None` for every person in a built realm until a depositor exists; this is the reading, not the writer.
OBSTACLE_ROLE = "social_contest.obstacle"   # the composition row whose module composes the obstacle
QUERY_ENTRIES = ((OBSTACLE_ROLE, "query"),)  # the host's declared need, held at driver construction (`registrar.require_entries`)


def _composed_obstacle(inp: SocialContestInput) -> float:
    """The obstacle the module composes for `inp`, reached by the `social_contest.obstacle` composition row (its pair's first)."""
    return composition.require(OBSTACLE_ROLE)(inp)[0]


def _composed_terms(inp: SocialContestInput) -> tuple:
    """The obstacle's named terms for `inp` (`roll.py::obstacle`'s pair's second), reached by the same row as `_composed_obstacle`."""
    return composition.require(OBSTACLE_ROLE)(inp)[1]


def _odds_of_input(inp: SocialContestInput) -> Optional[tuple]:
    """`record_odds` over one record: the module's obstacle, the record's pool and leverage (the owner
    derives the roll's boost from them). `None` where S27.4 refuses the attempt -- no dice are dealt, so there is no distribution
    (`resolve` refuses on the same pair, one rule: `ob > multiple x pool`)."""
    ob = _composed_obstacle(inp)
    if ob > inp.obstacle_refusal_multiple * max(inp.pool, 0):
        return None
    return record_odds(inp.pool, ob, inp.leverage)


_ORDINARY = SimpleNamespace(capability={}, attributes={}, traits=())    # AN ORDINARY PERSON, the one `believed_prior` `ordinary` takes an unknown opponent for: he holds nothing (B05.62)


def _ordinary_score(fx: Any, verb: str) -> Optional[float]:
    """THE SKILL SCORE OF AN ORDINARY PERSON for `verb`, read by the dealt roll's own reader (`pool.score`, which takes only `w.fixtures` of the
    world): the untrained score, or `None` where the skill's row says `untrained: none` (the module's stand-in then opposes)."""
    held = score(SimpleNamespace(fixtures=fx), _ORDINARY, verb)
    return None if held is None else float(held)


def believed_input(p: Any, verb: str, subject: Optional[str], fx: Any, *,
                   pool: float, person_subject: bool, examined_record: bool = False,
                   room: Optional[dict] = None, heard: bool = False,
                   effort: int = 0, office: Optional[str] = None, docketed: Optional[dict] = None,
                   tick: int = 0) -> Optional[SocialContestInput]:
    """THE PERSON'S RECORD (mode (b)): the same `SocialContestInput`, filled only from what `p` holds.

    AX-2: it reads `p` (his own ledger) and the fixtures, never the World; the
    facts about the act's SHAPE that only a World can answer (`person_subject`: the subject is a person;
    `examined_record`: an inquiry examines a Record; `heard`: a bench hears the contest) are the
    caller's, not a belief. His pool is his own and held with certainty: the caller passes it as `pool`
    (`odds_of` computes it with `faculty(w, believer, verb)`, which reads the log of his OWN acts for the
    practice addend: the one World read mode (b) makes, and it is of himself), so `faculty` stays the one
    pool reader. Every other field is filled
    only from what he holds, and WHERE A FACTOR IS UNKNOWN TO HIM THE ANSWER IS `None`, never a figure:
      * the opposition of a person subject: his skill score, a claim in the believer's ledger on that subject at
        `CAPABILITY_CLAIM + key` (the latest, then the most confident; a verb naming no key opposes at the untrained
        score, `pool.untrained`, every person's score on no vocation, so known) PLUS his opposing attribute, a claim at
        `CAPABILITY_CLAIM + the row's opposed_attribute` (B05.14); either not held -> unknown, UNLESS THE PRIOR HOLDS (`Fixtures
        believed_prior`, B05.62, H-435): at `ordinary` a part he holds no claim on is an ordinary person's, as a dealt roll against a person
        holding nothing composes it (the untrained skill score, the attribute scale's mid-point), his own guess and never a read of the
        World, and his stance toward the actor is taken as neutral (below). A non-person subject
        has no opposition, the module opposes it at `opposed_ob(pool_default)`, and that is known; so is the act's
        difficulty (the verb row's, public).
      * an examined Record's forgery quality: a property of the Record, held by nobody's claim here
        -> unknown.
      * the room's terms (`reception`, `proofs`) read other persons' ledgers: unknown unless the caller
        passes his own believed `room` (`{"reception": .., "proofs": ..}`).
    His `effort` is his own act's, held with certainty like his pool (CP-T01-05), and so is the level of the seat he acts through
    (`office`, B05.20): the caller's, read off the seat's own row (`_seat_modifier`), as `person_subject` is the caller's. So is the arrangement
    row the matter is docketed under (`docketed`, B05.21): the docket is public, the caller reads it. THE COUNTERPARTY'S STANCE TOWARD THE ACTOR IS
    HIS INTERIOR, held in no claim of the believer's: where `regard_step` is not 0 and one person stands alone opposite, it is unknown to him (`None`),
    never a figure; at 0 the term reads nothing, so the answer is as it was; AT THE `ordinary` PRIOR it is read neutral (regard 0, an ordinary
    person's), so he gets a figure."""
    roles = {r.role for r in _social_rows()}
    decay = fx.claim_decay()        # B09.01: his claims are read at `tick`, faded (`state/ledgers.py::present_confidence`), never as stored
    ordinary = fx.get("believed_prior") == "ordinary"        # B05.62 (H-435): a person he holds no claim about is taken for an ordinary one
    key = VERB_CAPABILITY.get(verb)
    opposition = None
    # THE TABLE'S TERMS, as the dealt roll reads them (`_read_social_roll`): no `opposes` row, no opposition term (and none to
    # be unknown about); no `dice` row, a pool of 0. A PERSON OPPOSITE BRINGS HIS SKILL SCORE PLUS HIS OPPOSING ATTRIBUTE (`_opposing`), and
    # BOTH ARE HIS TO KNOW ONLY BY A CLAIM IN THE BELIEVER'S OWN LEDGER: the skill's where the verb names one (a verb naming none, `lie`,
    # opposes at the untrained score for EVERY person, `pool.untrained`, which he knows without asking), the attribute's where the row
    # names one -- and the attribute is a trait of THAT person, never every person's, so with no claim the answer is unknown (`None`),
    # never a figure (B05.14; before it the keyless verb's believed obstacle was known and the dealt one).
    if "opposes" in roles and person_subject and subject != p.id:
        if key:
            said = believed_capability(p, subject, key, tick, decay)
            if said is None and not ordinary:
                return None
            skill = float(said) if said is not None else _ordinary_score(fx, verb)
        else:
            skill = float(untrained(fx))
        attribute = 0.0
        resisted = VERB_TABLE[verb].opposed_attribute if verb in VERB_TABLE else None
        if resisted and skill is not None:
            said = believed_capability(p, subject, resisted, tick, decay)
            if said is None and not ordinary:
                return None
            attribute = float(opposing_attribute(fx, _ORDINARY, verb) if said is None else said)     # an ordinary person's: the scale's mid-point
        opposition = None if skill is None else skill + attribute      # `None`: the module's `opposed_ob(pool_default)` stands, as in `_opposing`
    if examined_record:
        return None
    # THE `capability` SOURCE'S ROWS, as the believer can read them: his own side is his to know; the subject's is a claim of his
    # (`CAPABILITY_CLAIM` + the key), and where he holds none the answer is unknown, never a figure.
    def believed_subject(row, key):
        if not person_subject or subject == p.id:
            return None
        said = believed_capability(p, subject, key, tick, decay)
        if said is None:
            return (_ORDINARY, _held_at(_ORDINARY, row, key, verb)) if ordinary else _UNKNOWN      # an ordinary person holds nothing
        return SimpleNamespace(capability={row.key: said}), said
    edge = _edge_reads(verb, p, believed_subject)
    circumstance = _edge_reads(verb, p, believed_subject, CIRCUMSTANCE)
    if edge is _UNKNOWN or circumstance is _UNKNOWN:
        return None
    if person_subject and subject != p.id and not heard and fx.get("regard_step") and not ordinary:
        return None                                                     # his interior is not the believer's to know (B05.21)
    room_terms = {}
    if heard:
        if room is None:
            return None
        room_terms = dict(reception=room["reception"], reception_gain=fx.get("reception_gain"), proofs=room["proofs"])
    return _frame(fx, pool if "dice" in roles else 0, opposition, 0.0, room_terms, effort, verb, edge, circumstance, office,
                  docketed=docketed, heard=heard, bodies=(_body_of(p), None))      # his own body is his to know; another person's is not without a claim (B05.60)


def _rolled_as(w: Any, act: Any, owner: str = _PROVIDER) -> Optional[tuple]:
    """`(claimants, subject, room, examined, prize)` exactly as the fold hands the act to `resolve` (`prize` the contested prize's row, or `None`), or `None`
    when `owner`'s roll does not deal it (an uncontested act, another provider's prize, a party
    gap; `owner` is the social roll's unless `odds_of` asks for combat's). The derivation is the fold's
    own: `loop/sides.py::_contests_of` and `::sides_of` and the prize row's `heard_by:` for a contest; the verb's `graded_tasks` route (`data/rosters.py::graded_route`: `None` for a route armed by a fixture that reads `off`) for an inquiry or a task. `loop.sides`
    imports nothing that imports `seam` (`loop/__init__.py` imports nothing), so this module imports it at module
    level; `loop.resolve` would close a cycle the census counts (`tests/valoria/test_import_cycle_game_state_npe.py`),
    which is why the contest-of-an-act helper lives in `sides.py`."""
    from ...data.rosters import graded_route
    row = VERB_TABLE.get(act.verb)
    payload = act.payload if isinstance(act.payload, dict) else {}
    contests = _contests_of(act, row)
    if contests:
        prize = _prize_row("contest", contests[0])
        if prize is None or prize.get("provider") != owner:
            return None
        target = payload.get(row.opponent_operand() if row is not None else "subject")
        parties, subject, rung = sides_of(w, act, target, contests[0])
        if not parties:
            return None
        return parties, subject, (rung if prize.get("heard_by") else None), None, prize
    route = graded_route(act.verb, w.fixtures)          # B07.01: the fold's own reading of the route (`task_draw_arm`)
    if route is not None and route.get("provider") == owner:
        subject = payload.get("subject")
        return [act.actor], subject, None, subject, None
    return None


def _estimated(w: Any, act: Any) -> tuple:
    """`(True, odds)` when the provider of `act`'s prize registered an ESTIMATE (`@provider("estimate", <provider>)`:
    personal combat's `fight_estimate`, mass battle's `field_estimate`), `odds` being that provider's tuple or `None`;
    `(False, None)` when it did not (the social roll's case, `odds_of` below). The seam names the ROLE; which module
    answers is the prize row's `provider:`, so neither fight is named here (CP-T04-08). The act's parties are the fold's own derivation (`loop.sides`);
    none -> `None`, as the social roll's `_rolled_as` answers a party gap."""
    estimator, claimants, target = _estimating(w, act, "estimate")
    if estimator is None:
        return False, None
    return True, (estimator(w, act, claimants, target) if claimants else None)


def _estimating(w: Any, act: Any, role: str) -> tuple:
    """`(callable, claimants, target)` for the provider of `act`'s prize registered under `role` (`estimate`, or B14.24's `believed_estimate`), the act's
    parties the fold's own derivation (`loop.sides`); `(None, None, None)` where the act contests nothing or its prize's provider registered none."""
    row = VERB_TABLE.get(act.verb)
    contests = _contests_of(act, row)
    prize = _prize_row("contest", contests[0]) if contests else None
    fn = _provider_for(role, prize.get("provider")) if prize else None
    if fn is None:
        return None, None, None
    payload = act.payload if isinstance(act.payload, dict) else {}
    target = payload.get(row.opponent_operand() if row is not None else "subject")
    return fn, sides_of(w, act, target, contests[0])[0], target


def odds_of(w: Any, act: Any, *, believer: Any = None,
            believed_room: Optional[dict] = None) -> Optional[tuple]:
    """`(F, P, S, O)` for the social roll `act` would deal, or, for a row whose prize provider is personal combat
    (CP-T03-05), `(actor felled, subject felled, yielded, undecided)`; or `None`. READ-ONLY; no season draw and no write (a combat row's shares are SAMPLED, on a private rng).

    MODE (a), `believer=None`: the TRUE input -- `contest_input` over the act as the fold would hand it
    to `resolve`, the module's obstacle and `band_odds`. The shown number is the number the roll deals
    GIVEN THAT THE FOLD DEALS IT: the same record, the same obstacle function and the same roll
    composition. It does not say the fold will deal the act: eligibility and `requires` (`_admits`) and a
    deferred prize's step are the fold's gates, and a World that moves between the choice and the roll
    (`_eff_train` writes capability mid-RESOLVE; a `speak` earlier in the barrier moves reception) moves the
    dealt odds, not the shown ones. It answers "the odds of this roll, if made, on this World."

    MODE (b), `believer=<Person>`: the SAME function over `believed_input(believer, ...)`, the person's
    own record. It reads the believer's own ledger and nothing else of the true state (the World answers
    only the act's shape), and returns `None` where a factor is unknown to him -- never a guessed figure.
    ONE STATED EXCEPTION, his own pool: `faculty(w, believer, verb)` sums the registered addends, and the
    practice addend derives from `w.log` the results of HIS OWN acts. His own results are his to know, but
    this departs from 04 (§A.2 table, `loop/deliberate`: frozen `World` for `sense` only; §A.3 row 13: `Act`
    persists resolver-side, unreachable from a person-side surface), so the chooser (`decision/`) never calls
    this: it asks the QUERY `believed_chance` below, which `loop/deliberate.py` hands it on the View (CR-17).
    A ledger route for the pool exists (WITNESS stamps `doer?` on a holder's deposits about his own acts,
    §B.9) and would take the one World read out of mode (b); it is not built here [ASSUMPTION; medium;
    Jordan to correct; revert: none needed, the read is read-only and of himself].
    `None` is also the answer where the social roll deals no dice for the act (see `_rolled_as`) or
    S27.4 refuses it.

    Mode (b)'s one caller is `believed_chance` (CR-17): the chooser's pursuit term for a contested candidate.

    A ROW CONTESTING `the body` (CP-T03-05, MODE (a) ONLY) IS COMBAT'S, NOT THE SOCIAL ROLL'S: the answer is
    `combat.fight_estimate`'s shares as `(actor felled, subject felled, yielded, undecided)`, sampled live on a
    private rng (no season draw, nothing written), `None` for a refusal. They are the shares of the scene's
    four endings, not the social roll's four bands, and the caller knows which it asked by the act's prize.
    `odds_of`'S MODE (b) IS NOT BUILT for a fight: a believer's call here falls through to the social roll below,
    which does not deal the act, so it is `None`. THE BELIEVER'S FIGURE FOR A FIGHT IS `believed_chance`'s (B14.24):
    it reaches the prize provider's `believed_estimate` before ever asking this function. No loop caller reaches
    mode (a): the display is the player's.

    A ROW CONTESTING `a field` (CP-T04-08, MODE (a) ONLY, AQ-X1: no NPC reads it) IS MASS BATTLE'S: the answer is
    `mass_battle.field_estimate`'s shares as `(Won, Lost, Drawn, Unopposed)` (`mass_battle.ESTIMATE_BANDS`), the field's four
    graded bands. BOTH FIGHTS ARE REACHED THE SAME WAY, through the provider each prize row names, registered under the
    ESTIMATE role (`@provider("estimate", <provider>)`, `_estimated`): this function imports neither wrapper and holds
    no second odds function."""
    if believer is None:
        answered, odds = _estimated(w, act)
        if answered:
            return odds
    called = _rolled_as(w, act)
    if called is None:
        return None
    parties, subject, room, examined, prize = called
    effort = effort_of(act)                 # the act's own, as the fold hands it to `resolve`
    if w.persons.get(parties[0]) is None:
        return None
    if believer is not None and believer.id != act.actor:
        return None                     # another's pool is not his own to know
    if believer is None:
        hearing = {} if prize is None else dict(heard_by=prize.get("heard_by") or BENCH, toward=prize.get("toward"))
        return _odds_of_input(contest_input(w, parties, verb=act.verb, subject=subject, room=room,
                                            examined=examined, effort=effort, via=act.via, **hearing))
    inp = believed_input(believer, act.verb, subject, w.fixtures,
                         pool=faculty(w, believer, act.verb),
                         person_subject=bool(subject) and subject in w.persons,
                         examined_record=examined is not None and examined in w.records,
                         room=believed_room, heard=room is not None, effort=effort, office=_seat_modifier(w, act.via, room),
                         docketed=_docketed_row(w, subject), tick=w.tick)
    return None if inp is None else _odds_of_input(inp)


# band label -> its place in `band_odds`' tuple, both owned by `dice_engine` (neither spelt here)
_BAND_PLACE = {DEGREE_LABEL[d]: n for d, n in DEGREE_ORDINAL.items()}


def believed_chance(w: Any, believer: Any, act: Any, bands: Any) -> Optional[float]:
    """THE PERSON'S BELIEVED CHANCE THAT THE ROLL OF `act` LANDS IN ANY OF `bands`: the sum of mode (b)'s
    `odds_of` over those bands, or `None` where he cannot say (CR-17). `bands` are the labels the verb
    table's `writes:` map keys by (`dice_engine.DEGREE_LABEL`'s values); a label the social roll's ladder
    does not carry (another module's band) is `None` too, since no figure here speaks for it. The band
    order is the owner's (`DEGREE_ORDINAL`, the tuple `band_odds` returns): neither the labels nor their
    places are spelt here.

    A ROW WHOSE PRIZE BINDS A PROVIDER THAT REGISTERED A `believed_estimate` (B14.24: `personal_combat`'s) IS ANSWERED BY IT, not by `odds_of`: the
    provider's own resolver sampled on a private stream, on the believer's picture of the opponent (`combat.believed_picture`: his kit and wounds as the
    believer's ledger gives them, the world's where he has seen him, the default kit where he knows nothing), summed over the bands asked. No closed
    form and no table; the seam names the ROLE, never the wrapper. `None` for another's act, for a band that provider's ladder does not carry, and for a
    refusal. A provider with no such role (mass battle) falls through to `odds_of`, as before.

    A QUERY, NOT A STORE (`04` §A.2: the chooser asks, the host answers): `loop/deliberate.py` closes it over
    the frozen store and hands the chooser `View.odds`, so `decision/` holds a callable and never the store
    (AX-2). READ-ONLY, like `odds_of`. `believer` is the person choosing; another actor's act is `None`
    (`odds_of`'s own refusal).

    A ROW THAT PROCEEDS (B24p.14; `VerbRow.proceeds`, which B24p.16 gives the table) IS ANSWERED BY `_believed_proceeding_chance`, the chooser's
    own odds that the proceeding carries (`view_odds` on a room of himself and ordinary men): the believed odds follow the roll the act actually
    takes, and since B24p.19 a row that proceeds is dispatched to the proceeding by the seam and pools nothing."""
    row = VERB_TABLE.get(act.verb)
    if getattr(row, "proceeds", ()):
        return _believed_proceeding_chance(w, believer, act, bands)
    believed, claimants, _target = _estimating(w, act, BELIEVED_ESTIMATE_ROLE)
    if believed is not None:                # a fight: the believer's own estimate, the resolver sampled over the bands asked (B14.24)
        return believed(w, believer, act, claimants, tuple(bands)) if claimants and believer.id == act.actor else None
    odds = odds_of(w, act, believer=believer)
    if odds is None:
        return None
    held = [_BAND_PLACE.get(b) for b in bands]
    if not held or None in held:
        return None
    return ltr_sum(odds[n] for n in held)


def believed_odds_query(w: Any, holder: Any):
    """THE QUERY THE CHOOSER IS HANDED (`View.odds`): `believed_chance` closed over `w` and BOUND TO `holder`, as
    `(act, bands) -> chance or None` (a `_BelievedQuery`, which also answers `arranged`). The query answers for its holder alone (`04` §20, the own-ledger rule: a
    person's View carries his own record): it takes no person, so nothing downstream can ask it for another's
    belief. The ONE place the closure is made -- `loop/deliberate.py` hands it to every person's View and the
    harness readings that score a person outside `choose` (`harness/decision_spread.py`,
    `harness/interactions.py`) take it from here, so the figure they read is the figure the chooser reads."""
    return _BelievedQuery(w, holder)


@provider("contest", _PROVIDER)
def resolve(w: Any, claimants: list, causes: list, prize: Any, *, rng: Draw,
            verb: str = "", subject: Optional[str] = None,
            rung: Optional[str] = None,
            module_entry: Optional[str] = None, effort: int = 0, host: Any = None, via: Optional[str] = None,
            proceeds: Optional[tuple] = None, topic: Optional[str] = None, arranger: Optional[str] = None, rig: float = 0.0) -> dict:
    """Roll for one contested act: build the record, call the module entry, hold its return to a
    `Margin`, refuse S27.4. Returns a net/ob pair, NEVER a band and never a winner.

    `proceeds` (B24p.14) is `(row dict, form, move, item)`, the verb row's cell as the seam resolves it (B24p.19), and `None` for every act
    that does not proceed: the body below is then what it was. `topic` is the matter the proceeding is about (the act's `subject` where its
    opponent is another operand, the docket's matter where the opponent is the `subject`). Given, the act is a PROCEEDING instead: `_resolve_proceeding` builds the
    room (`proceeding_input`), calls the entry the composition row `social_contest.proceeding` names, holds its return to an `Outcome` of
    `Margin` verdicts and reads the act's record off it (`act_band`). `prize`, `rung`, `module_entry` and `via` are not read on that path.
    `arranger` and `rig` (B24p.24) are the arrangement the docket gave the sitting (`arranged_by`), read by the builder on that path alone.

    `host` (v10 REM-31) is accepted and NOT USED HERE: the seam's call is uniform, and only the
    personal-combat provider has a PLAYABLE mode (`seam/wrappers/combat.py::resolve`).

    `effort` is the act's own (CP-T01-05, `state/carriers.py::effort_of`, passed by `seam/contest.py`): it
    reaches only `contest_input`, where it becomes `leverage`; the act's draw is unchanged (one id, one draw).
    `via` is the seat the act is exercised through (`Act.via`, B05.20), passed the same way: its `modifier` is one level of that
    `leverage` where the prize's bench sits over the room (`_seat_modifier`); the other providers accept and ignore it.

    RESOLVED -> dict(status, module, resolver, pool, ob, net, terms, leverage, settled_margin, levels, fed_by)   # the entry's Margin + the record
                 # + the real margin `net - ob` the ladder quantises once (B05.02), the number `degree_of` grades
    REFUSED  -> dict(status, why, module, resolver, pool, ob, terms, levels, fed_by)   # S27.4: ob > obstacle_refusal_multiple x pool
    `levels` (B05.17, OBS §5): `((source, aggressor n, defender n), ...)`, one per `advantage_sources` member in roster order, the
    count of the named levels each brought -- the levels `leverage` is the sum of (`advantage_levels`, one call of every source).
    `fed_by` (B04.08): a tuple of `(use, role, key, side, value, contributed)`, one per `social_roll` row that fed the roll
    (`_fed_by`); read by no caller yet, carried on the dict and on no `Event` (D-U1-06).

    ⚠ A RETURN THAT IS NOT A `Margin` RAISES, NAMING THE ENTRY (*the provider returns a Margin*). It is a
    software defect in the module -- a winner where a margin belongs is the second resolver S27.2 refuses --
    so it is loud, never a refusal the fold would read as a game outcome.

    ⚠ THE ENTRY IS LOOKED UP BY THE ROLE THE PRIZE ROW NAMES (`module_entry:`), IN `MODULE_ENTRIES`.
    The registrar fills that table at driver construction from the composition row, and
    `manifest.check_contest_prizes` refuses construction when the two rows disagree; a call reaching
    here with the role unregistered (no driver constructed in the process) is `ENGINE-UNAVAILABLE`,
    `combat.py`'s typed refusal, never a direct import of the module.

    ⚠ `rung` IS READ FOR A PRIZE A ROOM HEARS, AND ONLY THERE. The seam passes the actor's place
    (`loop/sides.py`, `world_q.place_of`), so the venue is the act's own; a prize row
    declaring `heard_by:` (`a matter`, `speak`'s: the bench) has the room it names read the speaker
    (`audience_of`, by the room alone; `contest_input`'s `room`). Every other prize still derives its obstacle from the parties alone.

    ⚠ THE RNG IS A REQUIRED PARAMETER: THE DRIVER'S GENERATOR IS PASSED ON EVERY SHIPPED PATH (`loop/resolve.py`), A
    HAND CALL WITH NO `rng` IS A `TypeError` AT THE CALL (the parameter has no default), AND ONE PASSING NONE IS
    REFUSED (`InstrumentDefect`, naming the caller; never a fresh unseeded stream, never the process-global stream,
    never a seeded one made here). THAT IS `04 §C.12`'s REJECTION 4:
    *"A draw is a function of its key (`H(seed, tick, subject, purpose)`, the index `n` part of the key): the driver
    constructs no generator object and passes none down"* (04:953, as amended by A-30), AND A `Draw` IS A KEY AND AN
    INDEX, NOT A HIDDEN-STATE GENERATOR. ⚠ *Threaded* (superseded) MEANT PASSED BY PARAMETER RATHER THAN REACHABLE BY A
    GLOBAL NAME — not one continuous stream. `04 PART D row 35` settles it: `H(seed, tick, subject, purpose)`, no
    counter, no service. A single stream threaded through a season would make every roll depend on
    the count of prior draws, so adding one contested verb would move every other verb's outcome.

    ⚠ S27.4 IS EVALUATED HERE, AFTER THE ENTRY, on the pair the entry RETURNS: the
    obstacle is the module's (`roll.py::obstacle`, ED-SC-0033 clause (3)), so the host has no pair
    until the entry has run. A refused act's roll is discarded; its generator is the act's own
    (`H(seed, tick, subject, purpose)` above), so no other act's draw moves. Under the shipped
    ceiling (`H-213`, 2 = the multiple x the 1D floor) a derived pair with a pool of 1 or more is
    never refused here; only a pool below the floor is.

    ⚠ `module_entry` IS THE INQUIRIES' ROUTE (`ED-FI-0009`, J-22 (A)): `seam/contest.py::grade`
    passes the role a `graded_tasks` row names, with `prize=None`, and everything else here is the
    same body -- the same input builder, the same entry table, the same `Margin` hold and the same
    S27.4 -- so an inquiry is rolled by the one owner and graded on the one ladder, with no prize."""
    if not claimants:
        return dict(status="PARTY-GAP", why="a contest needs at least one claimant",
                    module=_PROVIDER)
    if w.persons.get(claimants[0]) is None:
        return dict(status="PARTY-GAP", why=f"claimant is not a person: {claimants[0]!r}",
                    module=_PROVIDER)
    if proceeds is not None:
        if rng is None:
            caller = sys._getframe(1)
            raise InstrumentDefect(f"{__name__}.resolve was handed no `rng` by {caller.f_globals.get('__name__', '?')}.{caller.f_code.co_name}: "
                                   f"a proceeding is drawn on the act's own generator, passed down by parameter (04 §C.12)")
        return _resolve_proceeding(w, claimants, rng, verb=verb, subject=subject, topic=topic, effort=effort, proceeds=proceeds,
                                   arranger=arranger, rig=rig)
    # The room that hears this prize, off its row (`heard_by:`); an inquiry has no prize
    # and so no room. `rung` is the act's place (`loop/sides.py`), which the bench sits over.
    row = _prize_row("contest", prize) if prize is not None else None
    heard = rung if row is not None and row.get("heard_by") else None
    # An inquiry (no prize) examines its subject; a Record's forgery quality
    # enters the obstacle (`contest_input`'s `examined`). A prize names a contest, which examines nothing.
    inp, reads, levels = _read_social_roll(w, claimants, verb=verb, subject=subject, room=heard,
                                   examined=subject if prize is None else None, effort=effort, via=via,
                                   heard_by=(row or {}).get("heard_by") or BENCH, toward=(row or {}).get("toward"))
    entry, refusal = entry_for(prize, _PROVIDER, module_entry)
    if entry is None:
        return refusal
    # ONE generator for the act's whole roll: the module's draw (`entry.fn`) is the only one. An absent `rng` is a caller that handed no generator -- an instrument defect, refused naming
    # that caller, never a fresh unseeded stream and never the process-global stream (04 §C.12: the RNG
    # is threaded, never global).
    if rng is None:
        caller = sys._getframe(1)
        raise InstrumentDefect(
            f"{__name__}.resolve was handed no `rng` by {caller.f_globals.get('__name__', '?')}."
            f"{caller.f_code.co_name}: the act's generator is the driver's, passed down by parameter (04 §C.12)")
    margin = entry.fn(inp, rng)
    if not isinstance(margin, Margin):
        raise Unspecified(
            f"module entry {entry.role!r} ({entry.target}) returned {type(margin).__name__} "
            f"{margin!r:.120}, which is not a `Margin`", "S39.4",
            needs="the entry returning `queries.inputs.Margin(net, ob)`",
            law="08_SEAM provider rule (intent) and S27.2 -- a contest provider returns a MARGIN, never "
                "a winner; the band is the one ladder's reading of the margin, so a winner here is a "
                "second resolver")
    # B05.14: every term of the obstacle, named, on the roll's record -- `Margin.terms`, the entry's own (`roll.py::obstacle`); it replaces
    # lane A's `ob_terms` dict (C3-L5). A stub entry's `()` is a margin with no composition behind it.
    terms = margin.terms
    if margin.ob > inp.obstacle_refusal_multiple * max(inp.pool, 0):
        return dict(status="REFUSED", why="S27.4", module=_PROVIDER,
                    resolver=_RESOLVER, pool=inp.pool, ob=margin.ob, terms=terms,
                    levels=levels, fed_by=_fed_by(reads, inp, terms))
    # B05.02: the margin is REAL -- `net` (the one sampler's draw plus the boost) less `ob` -- and the ladder quantises
    # it once (`degree_from_net`, `MARGIN_SCALE`). Nothing is settled here and no second draw is made: the act's stream
    # is the module's roll alone. The record keeps the name `settled_margin` (B05.18 reads it as a real margin).
    settled = margin.net - margin.ob
    # The margin's own fields, copied whole: the host reads the pair, it never computes one.
    return dict(status="RESOLVED", module=_PROVIDER, resolver=_RESOLVER, pool=inp.pool,
                **asdict(margin), leverage=inp.leverage, settled_margin=settled,
                levels=levels, fed_by=_fed_by(reads, inp, terms))


#: THE PROCEEDING'S OWN FIFTY-FOUR SETTINGS (V2 p2 §K, B24p.04), by group, each a `Fixtures` field with a `hole_register.yaml` row
#: (`H-861` to `H-914`). `yield_track` and `sympathy_step` are cut (V2 p4 §L 3) and are not names. The fold's table (`fold_*`, 24) is
#: not here: the module never reads it, the host's fold does (B24p.24, B27.28, B33.51).
PROCEEDING_SETTINGS = (
    # the speech
    "fit_level", "answer_level", "repeat_step", "sense_step", "involve", "esteem_step", "show", "off_step", "admit_step",
    "contempt_step", "ploy_step", "grain_strain", "heard_step", "heard_floor", "gap_step", "weary_step", "stay_base",
    "stay_per_will", "awe_step", "comfort_step", "rel_gain", "flop", "invite",
    # the press
    "press_ob", "press_pull", "rattle_pull", "wear", "rattle_gain", "rebound", "reactance", "room_level", "heckle",
    # conceding
    "concede_step", "consent_at",
    # the room and the reading
    "crowd_at", "crowd_lean", "mood_scale", "read_scale", "read_blur", "read_noise", "bias_step", "relevance",
    # the close
    "track_step",
    # the NPC's temper
    "temper_step", "temper_break", "temper_cool", "grain", "grudge", "pride",
    # the host
    "start_step", "presume_step", "power_scale", "strain_fade", "recuse_at",
)


def proceeding_dials(fx: Any) -> Any:
    """THE ONE PLACE THE PROCEEDING'S SETTINGS ARE NAMED FOR THE MODULE (B24p.04): the fifty-four `PROCEEDING_SETTINGS` read off `fx`,
    beside the dice settings the proceeding shares with the single roll -- `pool_add` and `pool_floor` (`pool_pair`, the one reader of
    the `social_roll` site's `dice` row), `pool_default` and `opposition_rate` -- and the attribute scale's three numbers
    (`descriptors.ATTRIBUTE_FLOOR` and `ATTRIBUTE_CEILING`, and `pool.attribute_midpoint()`, the one mid-point), sixty-one names in all,
    as a read-only mapping. The fold's `fold_*` coefficients are not in it. `proceeding_input` (B24p.13) reads it and adds the two rosters
    the module is handed (`moves`, `reads`), which are not settings."""
    pool_add, pool_floor = pool_pair(fx)
    d = {name: fx.get(name) for name in PROCEEDING_SETTINGS}
    d.update(pool_add=pool_add, pool_floor=pool_floor, pool_default=fx.get("pool_default"), opposition_rate=fx.get("opposition_rate"),
             attribute_mid=attribute_midpoint(), attribute_floor=descriptors.ATTRIBUTE_FLOOR, attribute_ceiling=descriptors.ATTRIBUTE_CEILING)
    return MappingProxyType(d)


# ---------------------------------------------------------------------------------------------------------------------
# B24p.13 -- THE HOST BUILDER AND THE CARD (V2 p2 §A, §H, §I; p1 §E). The one place `World` is read for a proceeding: it turns an
# arrangement row, a matter and the people into the typed `Input` the entry reads (`modules/social_contest/proceeding.py`) and derives the
# `Card` every participant reads. It writes nothing and holds no token; of ledgers it reads only each person's own, for his own `Present`
# (the precedent `contest_input` sets: F8). `resolve(proceeds=...)` calls it, for a verb row that carries `proceeds:` (B24p.19).
# ---------------------------------------------------------------------------------------------------------------------

#: `[HOOK]` THE CONTEXT'S THREE CARRIERS (V2 p2 §A.3's rule: a layer with no carrier is a key of the context table read as its control
#: until one exists). No tree field names an era of faith or trade, the regime in force, or the kind of an open strife flow
#: (`world_q.open_era` names the flow, not its kind `[UNVERIFIED]`), so each reads its plain row; `arrangements.yaml: context` holds the rest.
ERA, REGIME, STRIFE = "plain", "crown", "peace"

_SIDES = ("for", "against")
_SIX = ("focus", "reason", "attunement", "presence", "grace", "will")      # the six attributes a `Present` carries, by the module's names
_OTHER_SIDE = {"for": "against", "against": "for"}
_SIGN = {"for": 1.0, "against": -1.0}
#: The Record kinds a `matters` row names by its carrier (`Record:decree` is a `law`), read off the roster and never restated.
_RECORD_MATTER = {m["carrier"].partition(":")[2]: mid for mid, m in MATTERS.items() if m["carrier"].startswith("Record:")}


class Arrangement(NamedTuple):
    """What the builder decided about the forum that the `Input` does not carry whole (p2 §H): who arranged it, how far the tilt works,
    against which side, and which seats stepped down. `card` reads it with the built `Input`."""
    arranger: Optional[str]
    tilt: float
    tilted_against: Optional[str]
    recused: tuple


class _Sitting(NamedTuple):
    """The operands every `Present` of one proceeding is built with."""
    fx: Any
    regime: dict
    strife: dict
    topic: Optional[str]
    admits: tuple
    bears: dict
    for_id: str
    against_id: Optional[str]
    room: tuple
    factions: dict
    presume: float
    rank_key: Optional[str]


def _refuse(key: str, why: str) -> None:
    raise ValueError(f"refused[{key}]: {why}")


def _proceeding_module() -> Any:
    """The proceeding module, reached by its composition row (the host never names it: A-25), for the closed forms the card prints."""
    return sys.modules[composition.require(PROCEEDING_ROLE).__module__]


def _clip01(x: float) -> float:
    return min(1.0, max(0.0, x))


def _seats_held(w: Any, pid: str) -> list:
    """The offices `pid` holds now, from his own live `hold` edges."""
    return [w.offices[t.object] for t in w.persons[pid].tenures if t.kind == "hold" and t.live and t.object in w.offices]


def _rung_ordinal(w: Any, office: Any) -> int:
    rung = w.rungs.get(office.rung) if office.rung is not None else None
    return RUNG_KINDS.index(rung.kind) if rung is not None else 0


def _power(w: Any, pid: str, regime: dict) -> tuple:
    """`(power, precedence)` of a person (V2 p2 §H): his highest seat's rung ordinal, plus twice the level of its `modifier`, plus the
    regime's weight for the authority of its faction. A man with no seat has none (0, 0)."""
    seats = _seats_held(w, pid)
    if not seats:
        return 0.0, 0
    top = max(seats, key=lambda o: (_rung_ordinal(w, o), o.id))
    rank = _rung_ordinal(w, top)
    modifier = 2.0 * sigma_level(top.modifier) if top.modifier else 0.0
    return rank + modifier + regime["power"].get(AUTHORITY_BY_FACTION.get(top.faction), 0.0), rank


def _lawful(regime: dict, row: dict) -> bool:
    """A regime's `unlawful` names rites or rows; it is keyed on the row requested, and a rite it names stays lawful in a row of the regime's
    own authority (the one it weighs most; none where it weighs two alike) (V2 p4 §L 12)."""
    top = max(regime["power"].values())
    own = [a for a, x in regime["power"].items() if x == top]
    return row["id"] not in regime["unlawful"] and not (row["rite"] in regime["unlawful"] and row["authority"] != (own[0] if len(own) == 1 else None))


def _rite_of(fx: Any, verb: str, row: dict, effort: int, regime: dict, strife: dict) -> Rite:
    """The rite's cells with the row's, then the context's deltas (V2 p2 §B, §I). Every number here is a cell of a table or a setting."""
    cells, (lo, hi) = RITES[row["rite"]], row["turns"]
    silence = cells["silence"]
    if regime["silence"] is not None and not (silence == "free" and "must" not in cells["reply"].values()):
        silence = regime["silence"]
    if silence == "free" and "must" in cells["reply"].values():
        silence = "refusal"                                   # never free where an answer is owed (A-145; V2 p4 §L 6)
    admits = tuple(dict.fromkeys(k for k in (*row["admits"], *regime["admits_add"]) if k not in regime["admits_drop"]))
    moves = row.get("moves") or cells["moves"]
    return Rite(id=cells["id"], live=cells["live"], bears=cells["bears"], reply=tuple(cells["reply"].items()), silence=silence,
                issues=tuple(cells["issues"]), concede=cells["concede"], moves=tuple((s, tuple(ms)) for s, ms in moves.items()),
                weighs=tuple((i, tuple(ISSUE_RUNGS[i]["weighs"].items())) for i in cells["issues"] if ISSUE_RUNGS[i]["weighs"]),
                close=row["close"], turns=max(lo, min(hi, effort + 1 + strife["turns"])), quorum=row.get("quorum"),
                standard=attribute_midpoint() + DIFFICULTY_LEVELS.index(row["standard"]) + regime["standard"],     # [ASSUMPTION; Jordan to correct: mid plus the level's ordinal -- basis: V2's model reads plain 4, formal 5, solemn 6]
                reason_lean=row["reason_lean"] + regime["reason_lean"], admits=admits,
                difficulty=_difficulty_term(fx, {"verb": verb})["difficulty"], gravity=strife["gravity"] + regime["gravity"],
                unrest=strife["unrest"])


def _bench_of(w: Any, venue: Optional[str], topic: Optional[str], authority: str) -> list:
    """Who may sit at `venue`: `judging_set`'s holders, each kept where a seat he holds that sits over the venue (the grant and the containment
    `judging_set` asks) has a faction the authority maps from (`AUTHORITY_BY_FACTION`: the office's own faction, never the seat's proposition
    id); `parties` and `none` seat nobody by office. A holder who is gone sits empty."""
    ids = [p for p in dict.fromkeys(judging_set(w, venue, topic)) if p in w.persons]
    if authority in ("parties", "none"):
        return ids
    return [p for p in ids if any(t.kind == "hold" and t.live and BENCH_BASIS in t.granted_acts and t.object in w.offices
                                  and sits_over(w, w.offices[t.object], venue)
                                  and AUTHORITY_BY_FACTION.get(w.offices[t.object].faction) == authority for t in w.persons[p].tenures)]


def _watchers(w: Any, venue: Optional[str], floor: str, basis: Optional[str]) -> list:
    """Those present at `venue` the row's floor lets watch: `open` all, `closed` none, `admitted` the holders of a seat (of one granting `basis`
    where the row names one) `[ASSUMPTION; Jordan to correct: the model admits the holders of an office]`."""
    if venue is None or floor == "closed":
        return []
    here = [x for x in dict.fromkeys(presence(w, venue)) if x in w.persons]
    if floor == "open":
        return here
    return [x for x in here if any(t.kind == "hold" and t.live and t.object in w.offices and (basis is None or basis in t.granted_acts)
                                   for t in w.persons[x].tenures)]


def _holds(p: Any, bears: dict) -> tuple:
    """What he wants and holds, tag by tag, and how the matter bears on each: `((channel, tag, weight, bears), ...)`, the channels the grounds read
    (`want`: his pursuits; `hold`: his convictions over the roster's ceiling). Needs, goals and ambitions have no carrier `[HOOK]`."""
    want = tuple(("want", t, _clip01(float(v)), max(-1.0, min(1.0, bears.get(t, 0.0)))) for t, v in p.pursuits.items())
    held = tuple(("hold", t, _clip01(c / AFFILIATION_CEILING), max(-1.0, min(1.0, bears.get(t, 0.0)))) for t, c in p.conviction.items() if c > 0)
    return want + held


def _items_of(w: Any, p: Any, ctx: _Sitting, side: Optional[str]) -> tuple:
    """The things he holds of the kinds the rite admits (V2 p2 §G), from his own edges and his own ledger: the `Record`s he holds (a kind a
    `matters` row names by its carrier, else `record`), the seats he holds (`title`), the oaths he swore, the claims he holds on the matter (by
    the kind of their source, `PROOF_KIND_OF_SOURCE`), and, for a speaker, his own false word (`false_items`). `debt` (an oath owed to him is on
    the debtor's side) and `precedent`, `confession` and `state_of_realm` (the case file and the strife reading) have no carrier he holds `[HOOK]`."""
    out = []
    for t in p.tenures:
        if not t.live:
            continue
        if t.kind == "hold" and t.object in w.records:
            rec = w.records[t.object]
            out.append(Item(rec.id, _RECORD_MATTER.get(rec.kind, "record"), 1.0, source=p.id))
        elif t.kind == "hold" and t.object in w.offices:
            out.append(Item(t.id, "title", 1.0, source=p.id, about=t.object))
        elif t.kind == "oblige" and not t.imposed and t.subject == p.id:
            out.append(Item(t.id, "oath", 1.0, source=p.id, about=t.object))
    if ctx.topic is not None:
        full = ctx.fx.get("confidence_default")
        for c in p.ledger:
            kind = PROOF_KIND_OF_SOURCE.get(c.source)
            if c.subject == ctx.topic and kind is not None:
                out.append(Item(c.id, kind, _clip01(c.confidence / full), source=p.id, about=c.subject))
        if side is not None:
            out.extend(false_items(p, ctx.topic, side, ctx.fx))
    return tuple(it for it in out if it.kind in ctx.admits)


def _present(w: Any, p: Any, side: Optional[str], decides: bool, ctx: _Sitting) -> Present:
    """One person of the room, built from his OWN interior (his attributes, pursuits, convictions, stance, edges and ledger) and the
    operands `ctx` carries: never another person's ledger or true values (F8)."""
    fx, mid = ctx.fx, attribute_midpoint()
    if isinstance(p.weight, bool) or not isinstance(p.weight, (int, float)) or p.weight != int(p.weight):
        _refuse("bad_weight", f"{p.id} weighs {p.weight!r}: a weight is a whole number of heads")
    attr = {k: float(mid if (v := (p.attributes or {}).get(descriptors.ATTRIBUTE_NAMES[k])) is None else v)
            for k in _SIX}
    shares = tuple(x for x in (ctx.for_id, ctx.against_id) if x is not None and ctx.factions[x] is not None and ctx.factions[x] == ctx.factions[p.id])
    stake = bearing(p, ctx.bears, for_party=ctx.for_id, against_party=ctx.against_id, edges=p.tenures, shares=shares)
    care = person_care(p)
    care = (_clip01(care[0] + ctx.strife["care_want"]) if p.pursuits else care[0], care[1], care[2])
    bonds = tuple((q, b) for q in ctx.room if q != p.id
                  and (b := tie(p, q, edges=p.tenures, shared_faction=ctx.factions[q] is not None and ctx.factions[q] == ctx.factions[p.id])))
    start = fx.get("start_step") * (ltr_sum(stake) / BEARING_PARTS) + (ctx.presume if decides and side is None else 0.0)
    power, precedence = _power(w, p.id, ctx.regime)
    return Present(id=p.id, weight=int(p.weight), side=side, decides=decides, **attr,
                   rank=float((p.capability or {}).get(ctx.rank_key) or 0) if ctx.rank_key else 0.0,
                   care=care, stake=stake, bonds=bonds, start=start, holds=_holds(p, ctx.bears),
                   believes=believes(p, ctx.topic, fx) if ctx.topic is not None else 0.0,
                   bias=0.0,                                  # [HOOK: his stable misjudgement has no carrier]
                   power=power, precedence=precedence, items=_items_of(w, p, ctx, side),
                   strain=strain_carried((), fx))             # [HOOK: B24p.20's reader gives his rattles this season]


def _rank_key() -> Optional[str]:
    """The one skill whose rank joins the dice of a drawing move (`rosters.yaml: proceeding_moves`' `capability`; V2 p2 §A.1: `rank` is one
    number, his rank in the proceeding's skill), read as `pool._capability` reads a verb's skill: off the person's `capability`."""
    keys = {m.get("capability") for m in PROCEEDING_MOVES.values() if m["draw"]} - {None}
    if len(keys) > 1:
        raise Unspecified(f"the drawing moves name {sorted(keys)} as their skill", "rosters.yaml -- proceeding_moves", needs="one skill",
                          law="V2 p2 §A.1 -- `Present.rank` is his rank in the proceeding's skill, one number")
    return next(iter(keys), None)


def proceeding_input(w: Any, claimants: list, *, verb: str, subject: Optional[str], topic: Optional[str], effort: int, row: dict,
                     arranger: Optional[str] = None, rig: float = 0.0, form: str = "auto", state: Any = None,
                     seen: Optional[Mapping] = None) -> tuple:
    """`(Input, Card)`: THE HOST BUILDER OF A PROCEEDING (V2 p2 §A, §H, §I; B24p.13). `claimants[0]` is the bearer (`for`); the other party is the
    next claimant, else `subject` where he is a person other than the bearer, else (where the rite gives the other side moves) the most opposed
    man on the floor. `row` is an arrangement row (a seeded one, or `abridged(row)`'s); `form` is `full`, `abridged` or `auto` (abridged where
    the act's `effort` is 0 and nobody watches). `arranger` and `rig` are the arrangement (p2 §H); `topic` is the matter argued.

    Refused, each a `ValueError` whose message begins `refused[<key>]`: `unlawful`, `absent`, `both_parties`, `no_seat`, `short_bench`,
    `bad_weight`, and (from `Input`) the sitting's own invariants. It reads `w.persons`, `w.offices`, `w.fixtures`, seats, Tenures, and each
    person's own interior and ledger; never `proofs` or `reception`, and never one person's ledger for another's values. It writes nothing.

    `seen` (B24p.14) is the persons as a READER sees them, `{id: Person}`, each `Present` built from his entry where it has one and from the
    world's otherwise: who sits, who is a party and what is public (seats, ties, weight) are the world's either way; the believed odds
    (`believed_proceeding_odds`) pass the chooser's picture of the others."""
    fx = w.fixtures
    era, regime, strife = CONTEXT["eras"][ERA], CONTEXT["regimes"][REGIME], CONTEXT["strife"][STRIFE]
    if not claimants:
        _refuse("absent", "a proceeding needs a bearer")
    fid = claimants[0]
    aid = next((c for c in claimants[1:] if c != fid), None)
    if len(claimants) > 1 and claimants[1] == fid:
        _refuse("both_parties", f"the two parties to the matter are one character ({fid})")
    if aid is None and subject in w.persons and subject != fid:
        aid = subject
    gone = [x for x in (fid, aid, arranger) if x is not None and x not in w.persons]
    if gone:
        _refuse("absent", f"{gone[0]} is not in the world (a party or arranger who is gone)")
    if not _lawful(regime, row):
        _refuse("unlawful", f"{row['id']} is not lawful under {REGIME}")
    venue = place_of(w, topic) or place_of(w, fid)
    floor = row["floor"] if regime["floor"] is None else regime["floor"]
    here = [x for x in dict.fromkeys(presence(w, venue)) if x in w.persons] if venue is not None else []
    watchers = [x for x in _watchers(w, venue, floor, row["floor_basis"] if regime["floor"] is None else None) if x not in (fid, aid)]
    if form == "abridged" or (form == "auto" and effort <= 0 and not watchers):
        row = abridged(row) if row["close"] != "exchange" else row
    rite = _rite_of(fx, verb, row, effort, regime, strife)
    moves, close = dict(rite.moves), rite.close
    bench = _bench_of(w, venue, topic, row["authority"]) if close in ("bench", "declared") else []
    # a speech put to no man (`speak` at a sitting, a self-plea) is put to the presiding seat of the row's own bench, who is the one addressed
    # [ASSUMPTION; Jordan to correct: B24p.19 -- the abridged row (`abridged()`) keeps its authority but no bench, so the speaker would sit alone (`refused[one_character]`)]
    if aid is None and close == "exchange":
        sitting = sorted(_bench_of(w, venue, topic, row["authority"]), key=lambda x: (-_power(w, x, regime)[1], x))
        aid = next((x for x in sitting if x != fid), None)
    # the other party: where the rite gives the other side moves and the matter names nobody, the most opposed man on the floor (p4 §K D4)
    if aid is None and moves.get("against"):
        opposed = [x for x in here if x != fid and x not in bench
                   and takes_side(bearing(w.persons[x], {}, for_party=fid, against_party=None, edges=w.persons[x].tenures)) == "against"]
        if opposed:
            aid = min(opposed, key=lambda x: (ltr_sum(bearing(w.persons[x], {}, for_party=fid, against_party=None, edges=w.persons[x].tenures)), x))
            watchers = [x for x in watchers if x != aid]
    bears: dict = {}                                          # [HOOK: what tags the matter bears on has no carrier; B27.05 owns it (C(B24p) UNDECIDED (5))]
    precedence = {x: _power(w, x, regime)[1] for x in bench}
    # who sits: the authority's seats, the presiding seat first; a conflicted non-party steps down where another can sit (a party who sits does not)
    seats, recused = sorted(bench, key=lambda x: (-precedence[x], x)), []
    if close in ("bench", "declared"):
        need = 1 if close == "bench" else (rite.quorum or 1)
        for x in list(seats):
            partial, _ = conflict(w.persons[x], bears, for_party=fid, against_party=aid, edges=w.persons[x].tenures)
            if x not in (fid, aid) and partial >= fx.get("recuse_at") and len(seats) > need:
                seats.remove(x)
                recused.append(x)
        if close == "bench" and aid is None and len(seats) > 1 and seats[0] == fid:
            seats = seats[1:] + seats[:1]                     # the sole speaker is not his own only listener: the next seat presides (§L 16)
        if not seats:
            _refuse("no_seat", f"{row['id']}: no seat of authority {row['authority']} at {venue}")
        if len(seats) < need:
            _refuse("short_bench", f"{row['id']}: {len(seats)} seat(s) offered for a quorum of {need}")
    seated = seats if close == "declared" else seats[:1] if close == "bench" else []
    # the room: who is a side and who decides are two cells; one person may hold both
    cells: dict = {}

    def add(pid: str, side: Optional[str], decides: bool) -> None:
        if pid not in cells:
            cells[pid] = [side, decides]
        elif decides:
            cells[pid][1] = True
    add(fid, "for", False)
    if aid is not None:
        add(aid, "against" if moves.get("against") else None, close in ("exchange", "hearers"))
    for x in seated:
        add(x, None, True)
    for x in watchers:
        add(x, None, close == "hearers")
    # the arrangement (p2 §H): the arranger's side is his own where he is a party, else the side his ties favour; one lever, the seats' start
    arr = arranger if arranger is not None else (fid if rig > 0 else None)
    factions = {x: faction_holding(w, x) for x in dict.fromkeys([*cells, *([arr] if arr else [])])}
    tilt, arr_side = 0.0, None
    if arr is not None:
        if arr in (fid, aid):
            arr_side = "for" if arr == fid else "against"
        else:
            a = w.persons[arr]
            lean = tie(a, fid, edges=a.tenures, shared_faction=factions[fid] is not None and factions[fid] == factions[arr]) \
                - (tie(a, aid, edges=a.tenures, shared_faction=factions[aid] is not None and factions[aid] == factions[arr]) if aid else 0.0)
            arr_side = "for" if lean > 0 else "against" if lean < 0 else None
        weak = None if arr_side is None else (aid if arr_side == "for" else fid)
        if weak is not None:
            tilt = rig * max(0.0, fmath.tanh((_power(w, arr, regime)[0] - _power(w, weak, regime)[0]) / fx.get("power_scale")))
    if tilt > 0 and not [x for x, (side, decides) in cells.items() if decides and x not in (fid, aid)]:
        tilt = 0.0                                            # only a party decides (a conversation, a questioning, a negotiation): nothing to tilt
    ctx = _Sitting(fx=fx, regime=regime, strife=strife, topic=topic, admits=rite.admits, bears=bears, for_id=fid, against_id=aid,
                   room=tuple(cells), factions=factions, presume=fx.get("presume_step") * tilt * _SIGN[arr_side] if tilt > 0 else 0.0,
                   rank_key=_rank_key())
    room = tuple(_present(w, (seen or {}).get(x, w.persons[x]), side, decides, ctx) for x, (side, decides) in cells.items())
    dials = dict(proceeding_dials(fx))
    dials["moves"] = {m: (r["effect"], r["draw"]) for m, r in PROCEEDING_MOVES.items()}      # the two rosters the module is handed (its head)
    dials["reads"] = {g: r["reads"] for g, r in GROUNDS.items()}
    inp = Input(rite=rite, matter=topic if topic is not None else (subject or ""), room=room,
                grounds=tuple((g, r["reason"], era[g]) for g, r in GROUNDS.items()), dials=MappingProxyType(dials), state=state,
                frames=tuple(sorted({(c, t) for p in room for c, t, _, _ in p.holds})))
    return inp, card(inp, row, Arrangement(arr if tilt > 0 else None, tilt, None if tilt <= 0 else _OTHER_SIDE[arr_side], tuple(recused)))


def card(inp: Input, row: dict, arrangement: Arrangement) -> Card:
    """THE CARD (V2 p1 §E; pure): what the proceeding IS, derived from the built rite and room and never authored. It holds no true attribute and
    no true start; its `odds` is the close itself where nobody speaks (`card_odds`), `None` where nothing is drawn."""
    mod, rite, D = _proceeding_module(), inp.rite, inp.dials
    moves, ds = dict(rite.moves), [p for p in inp.room if p.decides]
    bearer = mod._lead(inp, rite.bears)
    owed = dict(rite.reply).get(_OTHER_SIDE[rite.bears]) == "must" and rite.silence != "free"
    unmoved = fmath.ltr_sum(mod.silence_cost(inp, d, None, bearer) for d in ds) / len(ds) if (owed and bearer is not None and ds) else 0.0
    if rite.silence == "free":
        silence = "free: nothing here must be answered, and silence costs nothing"
    else:
        side = "against" if dict(rite.reply).get("against") == "must" else rite.bears
        owes = mod._lead(inp, side) or (ds[0] if ds else None)
        pt = Point(-1, _OTHER_SIDE[side], "", "", None, "", ())
        cost = fmath.ltr_sum(mod.silence_cost(inp, d, pt, owes) for d in ds) / len(ds) if (ds and owes is not None) else 0.0
        silence = f"{rite.silence}: a point owed an answer and left standing costs {cost:.2f} with each who decides" \
            + (" (he decides himself, and answers to the contempt of those present)" if ds == [owes] else "") \
            + (", and counts with him again as tacitly admitted" if rite.silence == "admits" else "")
    crowd = mod._crowd(inp)
    return Card(kind=row["id"], genre=RITES[row["rite"]]["genre"], arranged_by=arrangement.arranger, tilt=round(arrangement.tilt, 2),
                tilted_against=arrangement.tilted_against, stake=row["disposes"], outcomes=tuple(DISPOSAL[row["disposes"]].items()),
                room=tuple((p.id, ("speaks " + p.side + (" and judges" if p.decides else "")) if p.side else ("judges" if p.decides else "attends"),
                            round(p.power, 1)) for p in inp.room),
                live=rite.live, bears=rite.bears, reply=rite.reply, moves=rite.moves,
                barred=tuple((s, m) for s in _SIDES for m in PROCEEDING_MOVES if moves.get(s) and m not in moves[s]),
                admits=rite.admits, close=rite.close, decided_by=tuple(p.id for p in ds), turns=rite.turns, issues=rite.issues,
                silence=silence,
                unargued=(f"it lapses: the bearer must put it, and his rest is priced as silence ({unmoved:.2f} with those who decide)" if owed and unmoved
                          else "it stands where the room starts: the bearer decides it himself" if owed
                          else "it stands where the room starts"),
                ends="/".join(PROCEEDING_ENDS), standard=rite.standard, unrest=rite.unrest, gravity=rite.gravity,
                reason_weight=tuple((g, min(10, max(0, round(10 * (reason + rite.reason_lean - D["crowd_lean"] * crowd)))) / 10)
                                    for g, reason, _ in inp.grounds),
                recused=arrangement.recused, odds=mod.card_odds(inp))


# ---------------------------------------------------------------------------------------------------------------------
# B24p.14 -- THE PROVIDER PATH AND THE BELIEVED ODDS (V2 p2 §C.5, §D, §E; p4 §F 8, 13, 21). `resolve(proceeds=...)` runs a proceeding and
# `act_band` reads the act's record off what the entry returned; `believed_proceeding_odds` is what a chooser prices an act by before he
# makes it. The module returns margins; every band is read here, on the one ladder (`seam/ladder.py::degree_of`). The seam dispatches on a verb
# row's `proceeds:` cell from B24p.19 (`seam/contest.py::contest`).
# ---------------------------------------------------------------------------------------------------------------------

#: Who yields decides what a yield is (V2 p2 §C.5): the bearer drops the matter, the other side's party gives way. A band, never a side.
_YIELDS = {"bearer": Degree.FAILURE, "other": Degree.SUCCESS}


def _band_margin(band: Degree) -> float:
    """The margin AT `band`'s floor, read from the ladder's own edges (`BAND_FLOORS` in `MARGIN_SCALE` milli-units, which `degree_from_net`
    compares): a result carrying it as `settled_margin` is graded as `band` by `degree_of`, first and with no edit to it. The lowest band has
    no floor, so it is the highest margin that still reads as it, one milli-unit under the next band's edge."""
    floors = dict(BAND_FLOORS)
    return floors.get(band.value, min(floors.values()) - 1) / MARGIN_SCALE   # [canonical: one milli-unit, the ladder's own unit of account (MARGIN_SCALE)]


def _decided(band: Degree) -> dict:
    """A band the sitting settled by itself (a yield): its record is the margin at the band's floor, no draw behind it."""
    m = _band_margin(band)
    return dict(status="RESOLVED", net=m, ob=0.0, terms=(), settled_margin=m, read=())


def act_band(outcome: Outcome, rite: Rite, weights: Optional[Mapping] = None) -> dict:
    """THE ACT'S RECORD, read off a sitting by its close and by who yielded (V2 p2 §C.5, §D): `dict(status, net, ob, terms, settled_margin,
    read)`, `read` the verdicts the margin came from (`()` for a band a yield decided), or `dict(status="IMPASSE", read=(), terms=())`
    where there is none (`consent` and nobody accepted). Never a band or a side: a decided band is `settled_margin` at its floor
    (`_band_margin`) and `degree_of` grades it. Pure.

      * `exchange`, `bench` -- the one verdict; `declared` -- the quorum-th best seat's margin (a majority carries, the presiding seat is
        one vote, no veto); `hearers` -- the weight-mean of the nets and of the obstacles (`weights`: `{person: heads}`, from the room);
      * a yield: the bearer's is his dropping the matter; a party whose verdict ALONE is the close gives way (one seat, one vote: on a close
        other seats share, his yield is priced and the close is drawn as any party's, p4 §F 11); under `consent` an accept by the other
        side and the bearer's withdrawal are the two bands, and neither is an impasse."""
    yielder = next((b.side for b in reversed(outcome.beats) if b.mover == outcome.ended_by), None) if outcome.ended == "yielded" else None
    who = None if yielder is None else "bearer" if yielder == rite.bears else "other"
    verdicts = tuple(outcome.verdicts)
    if rite.close == "consent":
        return _decided(_YIELDS[who]) if who is not None else dict(status="IMPASSE", read=(), terms=())
    if who == "bearer" or (who == "other" and len(verdicts) == 1 and verdicts[0][0] == outcome.ended_by):
        return _decided(_YIELDS[who])
    if not verdicts:
        raise Unspecified(f"a sitting of close {rite.close!r} returned no verdict", "modules/social_contest/proceeding.py -- _close",
                          needs="a verdict for each seat that decides", law="V2 p2 §D -- every close but `consent` is drawn")
    if rite.close in ("exchange", "bench"):
        who_id, m = verdicts[0]
        net, ob, terms, read = m.net, m.ob, m.terms, (who_id,)
    elif rite.close == "declared":
        who_id, m = sorted(verdicts, key=lambda v: (-(v[1].net - v[1].ob), v[0]))[min(len(verdicts), rite.quorum or 1) - 1]
        net, ob, terms, read = m.net, m.ob, m.terms, (who_id,)
    elif rite.close == "hearers":
        if len(verdicts) > 1 and weights is None:
            raise Unspecified("a `hearers` close of several verdicts is read without the room's weights", "seam/wrappers/sigma.py -- act_band",
                              needs="`weights`, `{person: heads}`", law="V2 p2 §D -- the weight-mean of those who hear")
        heads = [1 if weights is None else weights[i] for i, _ in verdicts]
        W = ltr_sum(heads)
        net, ob = (ltr_sum(h * getattr(m, f) for h, (_, m) in zip(heads, verdicts)) / W for f in ("net", "ob"))
        terms, read = verdicts[0][1].terms, tuple(i for i, _ in verdicts)         # one obstacle drew every seat's close: its terms are the same
    else:
        raise Unspecified(f"act_band was handed the close {rite.close!r}", "rosters.yaml -- proceeding closes", needs="a close it reads",
                          law="V2 p2 §D -- the host reads each close")
    return dict(status="RESOLVED", net=net, ob=ob, terms=terms, settled_margin=net - ob, read=read)


def _draw_of(inp: Input, out: Outcome, band: dict, weights: Mapping) -> tuple:
    """`(pool, leverage)` of the draw the act's band came from: the speech's (an `exchange` close: his pool, whose leverage is not on the
    beat, so `None`) or the verdicts read (the ordinary bench's pool and each seat's own track as leverage, the weight-mean over several);
    `(None, None)` for a band a yield decided."""
    mod, read = _proceeding_module(), band["read"]
    if not read:
        return None, None
    if inp.rite.close == "exchange":
        beat = out.beats[-1]
        return (None if beat.ground is None else mod.case_pool(inp, mod._who(inp, beat.voice), beat.ground)), None
    tracks = dict(out.state.tracks)
    drawn = [mod._close_record(inp, tracks[i]) for i in read]
    heads = [weights[i] for i in read]
    return drawn[0][0], ltr_sum(h * rec.leverage for h, (_, rec) in zip(heads, drawn)) / ltr_sum(heads)


_DATA_DEFECTS = ("refused[bad_weight]", "refused[no_weight]")


def _resolve_proceeding(w: Any, claimants: list, rng: Draw, *, verb: str, subject: Optional[str], effort: int, proceeds: tuple,
                        topic: Optional[str] = None, arranger: Optional[str] = None, rig: float = 0.0) -> dict:
    """`resolve`'s path for an act that proceeds: build the room, call the entry the composition row names (every sitting of this batch is
    automatic: no callback is handed in), hold the return to an `Outcome` of `Margin` verdicts (a winner, a band or a side cannot cross
    the module boundary), read the act's record (`act_band`) and refuse S27.4 on an `exchange` close's pair only (a close is an adjudicator's
    draw and is never refused). RESOLVED -> `dict(status, module, resolver, pool, net, ob, leverage, terms, settled_margin, proceeding, card)`.
    `move` and `item` of `proceeds` are read by no caller yet (the automatic policy chooses the speech). `claimants` are the persons
    of the act's two sides (`loop/sides.py`: where the opponent operand is the matter itself, as `speak`'s, the second is the matter and no
    party: the builder reads parties off persons only, the matter as `topic`). A proceeding the builder refuses (`refused[<key>]`: no seat,
    a party gone, one man as both parties, ...) is the game's refusal, never a raise: `REFUSED`, which the fold takes as the verb's refusal kind."""
    row, form, _move, _item = proceeds
    try:
        inp, card_ = proceeding_input(w, [c for c in claimants if c in w.persons], verb=verb, subject=subject,
                                      topic=subject if topic is None else topic, effort=effort, row=row, form=form,
                                      arranger=arranger, rig=rig)
    except ValueError as refused:
        if not str(refused).startswith("refused[") or str(refused).startswith(_DATA_DEFECTS):
            raise                                # a weight that is no whole head count is a data defect, not a room the game refuses
        return dict(status="REFUSED", why=str(refused), module=_PROVIDER, resolver=_RESOLVER, pool=None, terms=())
    entry = composition.require(PROCEEDING_ROLE)
    out = entry(inp, rng)
    if not isinstance(out, Outcome) or not all(isinstance(v, tuple) and len(v) == 2 and isinstance(v[1], Margin) for v in out.verdicts):
        raise Unspecified(
            f"module entry {PROCEEDING_ROLE!r} ({entry.__module__}.{getattr(entry, '__qualname__', '?')}) returned {type(out).__name__} "
            f"{out!r:.120}, which is not an `Outcome` of `Margin` verdicts", "V2 p2 §M",
            needs="the entry returning `queries.inputs.Outcome`, each verdict a `Margin`",
            law="08_SEAM provider rule (intent) and S27.2 -- a provider returns MARGINS, never a winner; the band is the one ladder's reading")
    weights = {p.id: p.weight for p in inp.room}
    band = act_band(out, inp.rite, weights)
    held = dict(module=_PROVIDER, resolver=_RESOLVER, proceeding=out, card=card_)
    if band["status"] == "IMPASSE":
        return dict(status="IMPASSE", pool=None, terms=(), **held)
    pool, leverage = _draw_of(inp, out, band, weights)
    if inp.rite.close == "exchange" and pool is not None and band["ob"] > w.fixtures.get("obstacle_refusal_multiple") * max(pool, 0):
        return dict(status="REFUSED", why="S27.4", pool=pool, ob=band["ob"], terms=band["terms"], **held)
    return dict(status="RESOLVED", pool=pool, net=band["net"], ob=band["ob"], leverage=leverage, terms=band["terms"],
                settled_margin=band["settled_margin"], **held)


class _NoNoise:
    """The generator of a reading made without luck: every normal is its mean, counted as the module counts a normal (two uniforms). What
    a chooser expects of his own reading; no season draw and nothing keyed."""
    __slots__ = ("n",)

    def __init__(self):
        self.n = 0

    def normal(self, mu: float, sigma: float) -> float:
        self.n += 2
        return mu


class _Believed:
    """The persons as a chooser sees them (`proceeding_input`'s `seen`): himself at his own true values, every other person an ordinary man
    (B05.62): the scale's middle in each of the six attributes, no pursuit, conviction, stance or ledger of his own, drawn from the middle by
    the share of a claim the chooser holds that his accuracy `acc` reaches. What is public (his seats, his ties, his weight) is the world's.
    Built on first ask: a room is a handful of a realm's persons."""

    def __init__(self, w: Any, believer: Any, acc: float):
        self.w, self.believer, self.acc, self.shells = w, believer, acc, {}

    def get(self, pid: str, default: Any = None) -> Any:
        if pid == self.believer.id:
            return self.believer
        if pid not in self.w.persons:
            return default
        if pid not in self.shells:
            mid, decay, held = attribute_midpoint(), self.w.fixtures.claim_decay(), {}
            for name in dict.fromkeys(descriptors.ATTRIBUTE_NAMES[k] for k in _SIX):
                said = believed_capability(self.believer, pid, name, self.w.tick, decay)
                if said is not None:
                    held[name] = mid + self.acc * (float(said) - mid)
            shell = copy.copy(self.w.persons[pid])
            shell.attributes, shell.pursuits, shell.conviction, shell.stance, shell.ledger = held, {}, {}, [], []
            self.shells[pid] = shell
        return self.shells[pid]


def topic_of(act: Any, subject: Optional[str]) -> Optional[str]:
    """THE MATTER A PROCEEDING IS ABOUT (INT C.1), the one owner of the rule: where the verb row's opponent operand is another than `subject`
    (`tell`, `lie`, `argue`: their hearer, `to`) the matter is the act's `subject`; where the opponent IS the subject (`speak`: the docketed
    matter; `interrogate`: the man questioned) it is that same operand, `subject` as `sides_of` read it. The fold (`loop/resolve.py::_contest`)
    and the chooser's odds (`_believed_proceeding_chance`) both read it here, so what is priced is the sitting that is rolled."""
    row = VERB_TABLE.get(act.verb)
    if row is not None and row.opponent_operand() != "subject":
        return (act.payload or {}).get("subject") if isinstance(act.payload, dict) else None
    return subject


def believed_proceeding_odds(w: Any, believer: Any, claimants: list, *, verb: str, subject: Optional[str], effort: int,
                             proceeds: tuple, topic: Optional[str] = None, arranger: Optional[str] = None, rig: float = 0.0) -> Optional[float]:
    """THE CHOOSER'S OWN ODDS that the proceeding `proceeds` names carries (V2 p2 §E; B05.62): `view_odds` on an `Input` built from what
    he holds, read as his own view reads it, without luck. Himself at his true values, every other person an ordinary man (`_Believed`),
    so the odds are the close before an unmoved ordinary bench at the starts he believes `[ASSUMPTION: the chooser prices a full
    proceeding by the card's own odds as he reads them, and an abridged one by the same close on its one addressed man -- basis: V2 p2 §E,
    "the card's odds is the close before an unmoved ordinary bench"]`. His accuracy is the view's own (`View.acc`, read off a first pass).
    `None` where nothing is drawn (`consent`) or the proceeding is refused him (`refused[...]`); read-only, no draw. `arranger` and `rig`
    are the arrangement the sitting is held under (B24p.24), as `proceeding_input` reads them."""
    read = believed_proceeding(w, believer, claimants, verb=verb, subject=subject, effort=effort, proceeds=proceeds, topic=topic,
                               arranger=arranger, rig=rig)
    return None if read is None else read[0]


def believed_proceeding(w: Any, believer: Any, claimants: list, *, verb: str, subject: Optional[str], effort: int, proceeds: tuple,
                        topic: Optional[str] = None, arranger: Optional[str] = None, rig: float = 0.0) -> Optional[tuple]:
    """`(odds, tilt)` as `believed_proceeding_odds` reads the odds, with the tilt the same build gave the forum (B24p.24: the chooser prices a
    rig on the odds it buys and the tilt it costs, from one room). `None` where `believed_proceeding_odds` is."""
    row, form, _move, _item = proceeds
    mod = _proceeding_module()

    def read(acc: float) -> tuple:
        inp, card_ = proceeding_input(w, list(claimants), verb=verb, subject=subject, topic=subject if topic is None else topic, effort=effort,
                                      row=row, form=form, arranger=arranger, rig=rig, seen=_Believed(w, believer, acc))
        return inp, card_, mod.view(inp, mod._start(inp), mod._who(inp, believer.id), _NoNoise())
    try:
        inp, _, first = read(1.0)
        inp, card_, seen = read(first.acc)
    except ValueError as refused:
        if str(refused).startswith("refused["):
            return None
        raise
    return None if inp.rite.close == "consent" else (seen.odds, card_.tilt)


def arranged_by(w: Any, act: Any, topic: Optional[str]) -> tuple:
    """`(arranger, rig)` THE DOCKET GIVES THE SITTING AN ACT HEARS (B24p.24): for a verb whose `proceeds:` cell names the docket's row, the first
    item `docketed` lists for the matter says who arranged its sitting and how hard (`_docket_item`). The arranger is named only where there is a
    rig to work (`rig > 0`): at rig 0 he arranges nothing, and a builder asked to find him would refuse the sitting if he were gone. Any other
    act, and a matter on no docket, has none."""
    row = VERB_TABLE.get(act.verb)
    if not any(entry[1] == "docket" for entry in getattr(row, "proceeds", ())):
        return None, 0.0
    items = _world_q.docketed(w, topic)
    if not items:
        return None, 0.0
    rig = float(items[0].get(_world_q.DOCKET_RIG) or 0.0)
    return (items[0].get(_world_q.DOCKET_ARRANGER) if rig > 0 else None), rig


def _hearing(w: Any) -> Optional[tuple]:
    """`(verb, proceeds)` of the hearing a case just opened will have (B24p.24): the verb whose `proceeds:` cell names the docket's row, and
    its last entry's proceeding (`(row dict, form, move, item)`) -- the one that holds for a matter no row was named for (a computed case:
    `_eff_open_case` derives no arrangement), which is what `world_q.proceeding_row` falls through to. `None` where no verb hears a docket."""
    for verb, row in sorted(VERB_TABLE.items()):
        entries = getattr(row, "proceeds", ())
        if any(entry[1] == "docket" for entry in entries):
            _when, rid, form, move, item = entries[-1]
            arrangement = ARRANGEMENTS[rid]
            return verb, ((abridged(arrangement) if form == "abridged" else arrangement), form, move, item)
    return None


class _BelievedQuery:
    """`View.odds`: `believed_chance` closed over `w` and bound to `holder` (`believed_odds_query`), called as `(act, bands) -> chance or None`;
    and `arranged(act, rig)`, what an opener reads of the hearing of the case he would open (B24p.24): `(odds, tilt)` for the sitting
    held under his arrangement at `rig`, from the same believed picture of the room. It answers for its holder alone, as the call does."""
    __slots__ = ("w", "holder")

    def __init__(self, w: Any, holder: Any):
        self.w, self.holder = w, holder

    def __call__(self, act: Any, bands: Any) -> Optional[float]:
        return believed_chance(self.w, self.holder, act, bands)

    def arranged(self, act: Any, rig: float) -> Optional[tuple]:
        """`(odds that the matter carries for him, the tilt his rig gives the forum)`, or `None` where he cannot say (no hearing, no matter, a
        room the builder refuses him). At `rig` 0 he arranges nothing."""
        hearing, matter = _hearing(self.w), (act.payload or {}).get("subject") if isinstance(act.payload, dict) else None
        if hearing is None or act.actor != self.holder.id or matter not in self.w.persons:
            return None
        verb, proceeds = hearing
        return believed_proceeding(self.w, self.holder, [self.holder.id, matter], verb=verb, subject=matter, effort=0, proceeds=proceeds,
                                   topic=matter, arranger=self.holder.id if rig > 0 else None, rig=rig)


def _believed_proceeding_chance(w: Any, believer: Any, act: Any, bands: Any) -> Optional[float]:
    """`believed_chance` for an act whose verb row proceeds: the chooser's odds that it CARRIES (`believed_proceeding_odds`), for the bands
    that carry, and one less that for the bands that do not; any other set of bands is one no figure here speaks for (`None`)."""
    called = _rolled_as(w, act)
    if called is None or believer.id != act.actor or w.persons.get(called[0][0]) is None:
        return None
    mod = _proceeding_module()
    try:
        row = _world_q.proceeding_row(w, act)
    except Unspecified as no_row:               # a matter on no docket: no room is priced for it (the fold refuses it the same way)
        if no_row.where != "world_q.proceeding_row":
            raise
        return None
    topic = topic_of(act, called[1])
    arranger, rig = arranged_by(w, act, topic)
    p = believed_proceeding_odds(w, believer, called[0], verb=act.verb, subject=called[1], effort=effort_of(act), proceeds=row, topic=topic,
                                 arranger=arranger, rig=rig)
    carried = {DEGREE_LABEL[d] for d, n in DEGREE_ORDINAL.items() if n >= mod._CARRIED}
    held = set(bands)
    return None if p is None else p if held == carried else 1.0 - p if held == set(DEGREE_LABEL.values()) - carried else None
