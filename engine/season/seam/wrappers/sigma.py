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

import math
import sys
from dataclasses import asdict
from types import SimpleNamespace
from typing import Any, NamedTuple, Optional

from engine.dice_engine.dice_engine import DEGREE_LABEL, DEGREE_ORDINAL
from engine.dice_engine.draw import Draw
from engine.dice_engine.fmath import ltr_sum
from engine.dice_engine.sigma_leverage import levels_to_net_sigma, record_odds
from engine.substrate import composition, descriptors

from ...data.arrangements import ARRANGEMENTS
from ...data.rosters import RUNG_KINDS, STANCE_MAX
from ...data.rosters import capability_rows, require_use_site, roster, when_holds
from ...data.verbs import SOCIAL_ROLL_PROVIDER, VERB_CAPABILITY, VERB_TABLE, _OPENERS_FROM_EFFECTS
from ...gaps import InstrumentDefect, Unspecified
from ...loop.sides import _contests_of, seat_named_by, sides_of
from ...queries.person_q import believed_capability, stance_toward
# ⚠ THE LEAF, NOT THE PACKAGE'S RE-EXPORT. `manifest/providers.py` imports nothing, so no import
# here closes a loop back into this package (`_entry.py` says the same of the entry lookup);
# `manifest/registry.py` imports only `data/` and `gaps` and `queries/` is below `seam/`, so the
# two imports below close none either.
from ...manifest.providers import provider
from ...manifest.registry import (BELIEVED_ESTIMATE_ROLE, BENCH, HEARD_BY_ROOMS, RESIDENTS, SEAT_BODY, TOWARD_TO, call as _provider_for,
                                  resolve as _prize_row)
from ...queries.inputs import Margin, SocialContestInput
# The room's two resolver-side reads. The host READS them; the module composes the obstacle they move.
from ...queries.faction_q import weight as faction_weight
from ...queries.world_q import docketed_under, faction_of, hold_force, judging_set, proofs, reception, residence_of
from ...state.carriers import EFFORT, effort_of
from ...state.containment import edges_of
from ...state.gate import UNDECLARED_DISPOSAL, across_chains, seat_faction, sits_over
from ._entry import entry_for
from .pool import (POOL_ADDENDS, _capability, faculty, governing_attribute, governing_score, rank, opposing_attribute, pool_pair, register_pool_addend,  # noqa: F401  (moved: see pool.py)
                   score, untrained)

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
def _bound_to(binding: dict, roster_name: str, law: str = "OBS §1 -- the roster is the closed set and the binding is its only reader") -> dict:
    """`binding` (member -> host function) checked against `rosters.yaml: <roster_name>`, both ways: a member
    with no function would silently add nothing, a function with no member would silently never run. Returns the binding in the
    roster's order."""
    members = roster(roster_name, ordered=True)
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
                  heard_by: str = BENCH, toward: Optional[str] = None, seat: Optional[str] = None) -> SocialContestInput:
    """THE HOST INPUT BUILDER's record alone: `_read_social_roll`'s first return (see it for the body, for the
    rows' reads and for the levels, which `resolve` takes from the same call)."""
    return _read_social_roll(w, claimants, verb=verb, subject=subject, room=room, examined=examined, effort=effort, via=via,
                             heard_by=heard_by, toward=toward, seat=seat)[0]


def _read_social_roll(w: Any, claimants: list, *, verb: str = "",
                      subject: Optional[str] = None, room: Optional[str] = None,
                      examined: Optional[str] = None, effort: int = 0, via: Optional[str] = None,
                      heard_by: str = BENCH, toward: Optional[str] = None, seat: Optional[str] = None) -> tuple:
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
    `seat` is the seat the act names where its prize says an act names one (`loop/sides.py::seat_named_by`; B21.61): the `cross_chain` term
    prices the act where it and `via` are of different chains of seats (`gate.across_chains`).
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
                 docketed=docketed, heard=room is not None, regard=regard, bodies=bodies,
                 rank_gap=_rank_gap_of(w, via, subject),                         # the subject's rank above the exercised seat (B21.09)
                 cross_chain=int(via is not None and seat is not None and across_chains(w, via, seat)),     # the named seat is of another chain than the exercised one (B21.61)
                 faction_power=_faction_power_of(w, via, subject) if seat is not None else 0)     # the holder's faction against the host's, where the act names a seat (B21.69)
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
    return tuple(docketed["proofs"]) if docketed is not None and fx.get("proof_admission") == "on" else None


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
    Grace's `esteem` on the leverage and never an obstacle term (B24p.13), so the host omits `standard` for an act resolving through that path
    (B24p.05, B24p.19) -- which is not built; until it is, every bench-heard act on a docketed matter reads it here."""
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


def _rung_rank(w: Any, rung: Optional[str]) -> Optional[int]:
    """A rung's rank: its kind's ordinal in the ordered `rung_kinds` roster (`person` first, rank 0) -- the reading the gate's `rank` stem
    makes (`queries/world_q.py`, the `rank` stem). `None` for no rung or one the world does not hold."""
    r = w.rungs.get(rung) if rung is not None else None
    return None if r is None else RUNG_KINDS.index(r.kind)


def _rank_gap_of(w: Any, via: Optional[str], subject: Optional[str]) -> int:
    """HOW FAR THE ONE ACTED ON OR FOR STANDS ABOVE THE ACTOR'S EXERCISED SEAT (OBS §2 member 6; B21.09), in `rung_kinds` steps, never below 0.
    The actor's side is the rung of the seat `Act.via` names (rank 0 where he exercises none: he acts as a person). The subject's side is a
    rung's own rank where the subject is a rung (`establish`'s holding), and the highest rank among the rungs of the seats a person subject
    holds (rank 0 for a person holding none). 0 for no subject, or one that is neither. Read by `_rank_gap_term` through `rank_step`."""
    seat = w.offices.get(via) if via is not None else None
    own = (_rung_rank(w, seat.rung) or 0) if seat is not None else 0
    if subject in w.persons:
        theirs = max((_rung_rank(w, w.offices[t.object].rung) or 0 for t in edges_of(w, "hold", subject)
                      if t.live and t.object in w.offices), default=0)
    else:
        theirs = _rung_rank(w, subject) or 0
    return max(0, theirs - own)


def _rank_gap_term(fx: Any, facts: dict) -> dict:
    """`rank_gap`: how far the one acted on or for stands above the actor's exercised seat (OBS §2 member 6; B21.09, landed with its first reader,
    `establish`): `rank_step x` the gap `_rank_gap_of` counts (`facts["rank_gap"]`; 0 where the record's builder read none). Not listed at
    `rank_step` 0 (the control: "equal at control", OBS §4 step 6+) or where the subject stands at or below the seat."""
    return _weighing("rank_gap", float(facts.get("rank_gap") or 0), fx.get("rank_step"))


def _cross_chain_term(fx: Any, facts: dict) -> dict:
    """`cross_chain`: a conferral across chains of seats is a step harder (OBS §2 member 29; B21.61, `16_PESSIMIST_FA_B` edit 2, A-105):
    `cross_chain_step x` 1 where the seat the act names and the seat it is exercised through are of different factions (`facts["cross_chain"]`,
    `gate.across_chains`; 0 where the record's builder read none). Not listed at `cross_chain_step` 0 (the control: "equal at control", OBS §4
    step 6+) or inside one chain. A foreign holder stays uncommon by this price; a conferrer seating HIMSELF across chains is refused outright
    (`loop/predicates.py::_req_confer`, `self_across_chains`)."""
    return _weighing("cross_chain", float(facts.get("cross_chain") or 0), fx.get("cross_chain_step"))


def _faction_power_of(w: Any, via: Optional[str], holder: Optional[str]) -> int:
    """THE BAND OF THE HOLDER'S FACTION'S WEIGHT AGAINST THE HOST'S (B21.69, `IS-B3-FA-07`, A-105): `+1` where the faction the
    holder (the roll's subject, the live holder `sides_of` stood opposite) coheres under outweighs the faction of the seat the act is exercised
    through (`gate.seat_faction`), `0` where they weigh the same or are the SAME faction, `-1` where it weighs less. The weights are
    `faction_q.weight`, the one owner (political weight, not armed strength: A-105, `U5d_FA` §4). THE RATIO'S BAND IS READ AS THE COMPARISON OF THE TWO
    WEIGHTS, never their quotient, so a host faction with no members (weight 0.0, B21.68) reads as outweighed by any faction with some, and two
    empty ones as equal, and nothing divides by zero. `0` for no holder, a holder committed to no faction, or a seat carrying none."""
    host = seat_faction(w, via)
    theirs = faction_of(w, holder) if holder is not None and holder in w.persons else None
    if host is None or theirs is None or theirs == host:
        return 0
    mine, yours = faction_weight(w, host), faction_weight(w, theirs)
    return (yours > mine) - (yours < mine)


def _faction_power_term(fx: Any, facts: dict) -> dict:
    """`faction_power`: how far the power of the holder's faction stands over the host's against the act (B21.69, A-105: *"the
    amount of power over the foreign officer is determined by the power dynamics between the foreign faction and the host faction"*):
    `faction_power_step x` the signed band `_faction_power_of` read (`facts["faction_power"]`; 0 where the record's builder read none). Nothing
    lowers an obstacle (`roll.py::obstacle`), so only the stronger holder's side is listed, as harder: where the holder's faction is the weaker
    the member reads nothing, as where it is the same, and the host's own faction is never priced. Not listed at `faction_power_step` 0 (the
    control: "equal at control", OBS §4 step 6+)."""
    return _weighing("faction_power", float(max(0, facts.get("faction_power") or 0)), fx.get("faction_power_step"))


#: Each member of `rosters.yaml: obstacle_terms` -> the ONE function that reads it: `fn(fixtures, facts) -> {record field: value}`. A member
#: that is a raw operand times a step returns `{"obstacle_operands": ((name, raw, step),)}` instead. Refused at import, both ways.
OBSTACLE_TERMS = _bound_to({fn.__name__[1:-len("_term")]: fn for fn in (
    _even_term, _difficulty_term, _opposition_term, _standard_term, _stakes_term, _rank_gap_term, _regard_term, _reception_term,
    _capability_term, _cross_chain_term, _faction_power_term)},
                           "obstacle_terms")


def obstacle_operands(fx: Any, facts: dict) -> dict:
    """THE OBSTACLE'S FIELDS OF THE RECORD, every roster member's function asked in roster order: `difficulty`, `pool_default`,
    `pool_add`, `opposition`, `opposition_rate` and `obstacle_operands` (the `(name, raw, step)` triples of the members that are an
    operand times a step, in roster order). `facts` is what the act is: its `verb`, the `opposition` its builder read (`None`
    for nobody), the room's `reception` and the `circumstance` rows it selected and read, and (B05.21) the `docketed` arrangement row (or `None`),
    whether a bench `heard` the act, and the counterparty's signed `regard` (or `None`). `contest_input` and `believed_input` reach it through `_frame` alone, so they cannot compose different obstacles."""
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
           regard: Optional[float] = None, bodies: tuple = (None, None), rank_gap: int = 0, cross_chain: int = 0,
           faction_power: int = 0) -> SocialContestInput:
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
                                     reception=room_terms.get("reception", 0.0), docketed=docketed, heard=heard, regard=regard,
                                     rank_gap=rank_gap, cross_chain=cross_chain, faction_power=faction_power)),
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
                                            examined=examined, effort=effort, via=act.via,
                                            seat=None if prize is None else seat_named_by(w, act, _contests_of(act, VERB_TABLE.get(act.verb))[0]),
                                            **hearing))
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
    (`odds_of`'s own refusal)."""
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
    `(act, bands) -> chance or None`. The query answers for its holder alone (`04` §20, the own-ledger rule: a
    person's View carries his own record): it takes no person, so nothing downstream can ask it for another's
    belief. The ONE place the closure is made -- `loop/deliberate.py` hands it to every person's View and the
    harness readings that score a person outside `choose` (`harness/decision_spread.py`,
    `harness/interactions.py`) take it from here, so the figure they read is the figure the chooser reads."""
    return lambda act, bands: believed_chance(w, holder, act, bands)


@provider("contest", _PROVIDER)
def resolve(w: Any, claimants: list, causes: list, prize: Any, *, rng: Draw,
            verb: str = "", subject: Optional[str] = None,
            rung: Optional[str] = None,
            module_entry: Optional[str] = None, effort: int = 0, host: Any = None, via: Optional[str] = None,
            seat: Optional[str] = None) -> dict:
    """Roll for one contested act: build the record, call the module entry, hold its return to a
    `Margin`, refuse S27.4. Returns a net/ob pair, NEVER a band and never a winner.

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
    # The room that hears this prize, off its row (`heard_by:`); an inquiry has no prize
    # and so no room. `rung` is the act's place (`loop/sides.py`), which the bench sits over.
    row = _prize_row("contest", prize) if prize is not None else None
    heard = rung if row is not None and row.get("heard_by") else None
    # An inquiry (no prize) examines its subject; a Record's forgery quality
    # enters the obstacle (`contest_input`'s `examined`). A prize names a contest, which examines nothing.
    inp, reads, levels = _read_social_roll(w, claimants, verb=verb, subject=subject, room=heard,
                                   examined=subject if prize is None else None, effort=effort, via=via,
                                   heard_by=(row or {}).get("heard_by") or BENCH, toward=(row or {}).get("toward"), seat=seat)
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
