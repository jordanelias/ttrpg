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
H-215/H-216, not resolved here -- and freezes them into `queries/inputs.py::SocialContestInput`;
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
import random
import sys
from dataclasses import asdict
from types import SimpleNamespace
from typing import Any, Optional

from engine.dice_engine.dice_engine import DEGREE_LABEL, DEGREE_ORDINAL
from engine.dice_engine.sigma_leverage import levels_to_net_sigma, record_odds
from engine.substrate import composition, descriptors

from ...data.rosters import capability_rows, require_use_site, roster, when_holds
from ...data.verbs import SOCIAL_ROLL_PROVIDER, TASK_DIFFICULTY, VERB_CAPABILITY, VERB_TABLE
from ...gaps import InstrumentDefect, Unspecified
from ...loop.sides import _contests_of, sides_of
from ...queries.person_q import believed_capability
# ⚠ THE LEAF, NOT THE PACKAGE'S RE-EXPORT. `manifest/providers.py` imports nothing, so no import
# here closes a loop back into this package (`_entry.py` says the same of the entry lookup);
# `manifest/registry.py` imports only `data/` and `gaps` and `queries/` is below `seam/`, so the
# two imports below close none either.
from ...manifest.providers import provider
from ...manifest.registry import BENCH, call as _provider_for, resolve as _prize_row
from ...queries.inputs import Margin, SocialContestInput
# The room's two resolver-side reads. The host READS them; the module composes the obstacle they move.
from ...queries.world_q import proofs, reception
from ...state.carriers import EFFORT, effort_of
from ._entry import entry_for
from .pool import POOL_ADDENDS, _capability, faculty, governing_attribute, register_pool_addend, score, untrained  # noqa: F401  (moved: see pool.py)

# The prize rows' `provider:` string (`rosters.yaml` `contest_subsystems`): the module's one identity
# (A-25), so the row says the social contest module runs its own prizes. Reached by that string only.
_PROVIDER = SOCIAL_ROLL_PROVIDER   # B11 lane A: one owner of the name (`data/verbs.py`), which `task_difficulty`'s closure reads too
_RESOLVER = "d_sigma"


# `_capability`, `POOL_ADDENDS`, `register_pool_addend`, `governing_attribute` and `faculty` live in `pool.py` (the one pool reader),
# imported at the top of this module; see its docstring.


def _opposition_of(w: Any, subject: Optional[str], verb: str) -> Optional[float]:
    """The subject's SKILL SCORE for the verb, or `None` -- a READ, not an obstacle: `pool.score`, the held rank on the verb's
    skill (never below the untrained score, `pool_default`, where he holds none), and nothing else: no base dice, no practice
    addend, no seat, no attribute (B05.11, TWO Edit B, CAP B4: the attribute is a level, not a score, A-7). A PERSON SUBJECT
    ALWAYS HAS A SCORE, on every `obstacle_model` arm, so an unauthored hearer is no harder to move than one holding the skill
    at `pool_default` and a higher rank is harder (H-312's `interrogate`). `None` for nobody opposite (a record, a rung, a
    proposition, a person with no entry) and for a person with no score (a skill row saying `untrained: none` that he holds no
    rank in): the module's stand-in stands there.

    The obstacle is composed by `modules/social_contest/roll.py::obstacle` (ED-SC-0033 clause (3), *the
    obstacle has a single owner*). What is here is the half only the host can do: reading `World` for the
    score a PERSON subject brings."""
    if subject and subject in w.persons:
        opposing = score(w, w.persons[subject], verb)
        return None if opposing is None else float(opposing)
    return None


#: `Fixtures obstacle_model`'s shipped arm: the obstacle is the task's difficulty plus its named modifiers (B11 lane A,
#: H-368); `stand_in` is the control, the composition before.
OBSTACLE_MODEL_TASK = "task"


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


def _edge_rows() -> tuple:
    """The `social_roll` site's `edge` rows, in table order (none ship; a planted or authored row is read here)."""
    return tuple(r for r in capability_rows(SOCIAL_ROLL_SITE) if r.role == EDGE)


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
    """The side an `edge` row reads: the roller's (`actor`) or the person he acts on (`subject`). `each` is a fight's word."""
    if row.side not in ("actor", "subject"):
        raise Unspecified(f"an `edge` row at the social roll has side {row.side!r}", "rosters.yaml -- tables: capability_uses",
                          needs="`side: actor` or `side: subject`", law="U1 §3 item 3 -- a roll with one roller and one subject reads those two sheets")
    return row.side


def _edge_reads(verb: str, actor: Any, subject_read) -> Any:
    """`((row, key, value), ...)`: the `edge` rows this act brings, in table order, each with the value its side holds, a row whose
    `when` fails for that holder left out (`rosters.when_holds`, the one comparison). `subject_read(row, key)` answers the subject's
    side: `(holder, value)`, `None` where there is no one to read (not a person, or himself: nobody opposes himself), or `_UNKNOWN`
    (the believer holds no claim), which makes the whole answer `_UNKNOWN`."""
    out = []
    for row in _edge_rows():
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


# THE ADVANTAGE CHANNEL'S BINDING: each member of `rosters.yaml: advantage_sources` -> the function that
# returns the named levels it brings to an act, `fn(fixtures, operands) -> (levels for the roller, levels against him)`, each a
# list of level names. THE ROSTER IS
# THE CLOSED SET AND THIS IS ITS BINDING: refused at import if the two disagree, so a member with no function
# (it would silently add nothing) and a function with no member (it would silently never run) are both loud.
ADVANTAGE_SOURCES = {EFFORT: _effort_levels, CAPABILITY: _capability_levels}
if set(ADVANTAGE_SOURCES) != set(roster("advantage_sources")):
    raise Unspecified(
        f"`advantage_sources` members {sorted(roster('advantage_sources'))} and "
        f"`ADVANTAGE_SOURCES` functions {sorted(ADVANTAGE_SOURCES)} differ", "rosters.yaml",
        needs="a function for every member and a member for every function",
        law="CP-T01-05 -- the roster is the only door into the social roll's sigma term")


def advantage_sigma(fx: Any, operands: dict) -> float:
    """The social roll's net sigma, SIGNED: every `advantage_sources` member's named levels for this act, those that favour the roller
    and those that count against him, summed through `levels_to_net_sigma(for, against)` (a mu-shift the roll applies as `net_boost`;
    never a flat bonus on the net, never an Ob reduction). `operands` is what the act brings (`{"effort": e, "edge": rows}`); 0.0
    when nothing does."""
    for_, against = [], []
    for name in roster("advantage_sources", ordered=True):
        f, a = ADVANTAGE_SOURCES[name](fx, operands)
        for_.extend(f)
        against.extend(a)
    return levels_to_net_sigma(for_, against)


def contest_input(w: Any, claimants: list, *, verb: str = "",
                  subject: Optional[str] = None, room: Optional[str] = None,
                  examined: Optional[str] = None, effort: int = 0) -> SocialContestInput:
    """THE HOST INPUT BUILDER's record alone: `_read_social_roll`'s first return (see it for the body and for the
    rows' reads, which `resolve` takes from the same call)."""
    return _read_social_roll(w, claimants, verb=verb, subject=subject, room=room, examined=examined, effort=effort)[0]


def _read_social_roll(w: Any, claimants: list, *, verb: str = "",
                      subject: Optional[str] = None, room: Optional[str] = None,
                      examined: Optional[str] = None, effort: int = 0) -> tuple:
    """THE HOST INPUT BUILDER (plan position `31a`, A-25): `World` -> the frozen record the roll reads. Returns
    `(record, reads)`: the record `contest_input` hands out and, for each `social_roll` row of `tables.capability_uses`
    (table order), `(row, value)` -- the value the row's reader read, so the record `resolve` returns names what fed the
    roll and cannot disagree with what was rolled (CAP A6, MAP §D). `dice` reads the actor's score (`pool.score`, the base
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
    `effort` is the act's own (`state/carriers.py::effort_of`), passed by the adapter. The obstacle's operands are carried RAW (`opposition`, `obstacle_default`,
    `obstacle_ceiling`); the module composes them.

    `room` is the rung whose bench hears the contest, or `None`: the adapter passes the
    act's rung when the prize row says `heard_by: bench` (`manifest.resolve`), and nothing otherwise.
    With a room, the record carries the bench's `reception` of the actor and the actor's unmirrored
    `proofs` against the subject (`queries/world_q.py`, both read raw) and their two gains; without
    one they stay at the record's no-room defaults, so a `tell`, a `determine` or an inquiry rolls
    with no room terms.

    `examined` is the subject an INQUIRY examines, or `None`: the adapter passes
    the act's subject when there is no prize (an inquiry, `graded_inquiries`' route), and nothing
    otherwise. Where it names a Record, the record carries that Record's `forgery_quality` (read from
    `w.records`, the one read this builder adds), which the module adds to the obstacle; a site, a
    person, or a contest a prize names carries `0`."""
    fx = w.fixtures
    room_terms = {}
    if room is not None:
        room_terms = dict(reception=reception(w, claimants[0], room),
                          reception_gain=fx.get("reception_gain"),
                          proofs=proofs(w, claimants[0], subject, room),
                          proof_step=fx.get("proof_step"))
    doc = w.records.get(examined) if examined is not None else None
    # NOBODY OPPOSES HIMSELF (v10 CP-T05-02 (ii), AM-D-02): a subject who IS the actor (the self-plea,
    # `speak {subject: himself}`) brings no opposition -- his own score is not an obstacle to himself --
    # so the obstacle starts at `obstacle_default` on the control arm and at the task's difficulty alone on
    # the task arm (B11 lane A: a task no person opposes has no opposition term), the same at any capability he holds.
    #
    # THE ROLL READS ITS TERMS ONLY THROUGH THE SITE'S ROWS (CAP A6): a `dice` row's read gives the pool (and the score
    # it is built on), an `opposes` row's read gives the opposition; no `opposes` row means opposition `None`, as a
    # self-plea. A row the table omits is a term the roll does not read, so `fed_by` and the roll cannot disagree.
    actor = w.persons[claimants[0]]
    rows = _social_rows()
    roles = {r.role for r in rows}
    opposition = None
    if "opposes" in roles and subject != claimants[0]:
        opposition = _opposition_of(w, subject, verb)
    pool = faculty(w, actor, verb) if "dice" in roles else 0
    # THE `capability` SOURCE'S ROWS (B05.10): each `edge` row of the site whose `when` holds, with the value its side holds. A subject
    # who is the actor, or is no person, is read for nothing (nobody opposes himself).
    other = w.persons.get(subject) if subject and subject != claimants[0] else None
    edge = _edge_reads(verb, actor, lambda row, key: None if other is None else (other, _held_at(other, row, key, verb)))
    inp = _frame(fx, pool, opposition, doc.forgery_quality if doc is not None else 0.0, room_terms, effort, verb, edge)
    read = {"dice": score(w, actor, verb) if "dice" in roles else None, "opposes": opposition}
    chosen = {id(r): (value, levels_to_net_sigma(*_edge_levels(r, key, value))) for r, key, value in edge}
    return inp, tuple((r, *chosen[id(r)]) if id(r) in chosen else (r, read[r.role], None)
                      for r in capability_rows(SOCIAL_ROLL_SITE) if id(r) in chosen or r.role in read)


#: `rosters.yaml: capability_use_sites`' site whose one reader is `contest_input` (the single roll's dice and opposition).
SOCIAL_ROLL_SITE = require_use_site("social_roll")


def _social_rows() -> tuple:
    """The `social_roll` site's rows that give the roll a term (`dice`, `opposes`), in table order: the ONE place the roll's two
    builders -- the dealt roll (`_read_social_roll`) and the person's believed one (`believed_input`) -- ask which terms the table
    gives it, so they cannot compose different obstacles from one table (`_frame`). The loader pins each row's `key` and `side`
    and allows one of each role (`rosters.yaml: capability_site_reads`), so the role alone says what the reader reads."""
    return tuple(r for r in capability_rows(SOCIAL_ROLL_SITE) if r.role in ("dice", "opposes"))


def _fed_by(reads: tuple, inp: SocialContestInput, ob_terms: dict) -> tuple:
    """`((use, role, key, side, value, contributed), ...)` -- every row that fed the roll, in table order (MAP §D; the
    record is `resolve`'s, never an `Event` field, D-U1-06). `value` is what the row's reader read (`_read_social_roll`);
    `contributed` is what it added to the roll: the pool for `dice`, the module's own `opposition` term of the obstacle for
    `opposes` (`ob_terms`, read off the module that composed it, `0.0` where nobody opposed)."""
    contributed = {"dice": inp.pool, "opposes": ob_terms.get("opposition", 0.0)}
    return tuple((r.use, r.role, r.key, r.side, value, contributed[r.role] if own is None else own) for r, value, own in reads)


def _difficulty(fx: Any, verb: str) -> Optional[float]:
    """THE TASK'S DIFFICULTY for `verb` on the shipped arm (`rosters.yaml: task_difficulty`, closed over every verb the
    social roll deals, refused at import), `None` on the control arm. A verb the roll deals with no row cannot reach
    here (the import refused it); a hand call naming a verb the table does not carry is refused, naming it -- a task
    with no difficulty is a loud gap, never a default."""
    if fx.get("obstacle_model") != OBSTACLE_MODEL_TASK:
        return None
    if verb not in TASK_DIFFICULTY:
        raise Unspecified(f"the social roll was asked to deal {verb!r}, which `rosters.yaml: task_difficulty` gives no "
                          "difficulty", "rosters.yaml -- task_difficulty",
                          needs="a row for every verb the social roll deals",
                          law="B11 lane A -- an obstacle is the task's difficulty and its modifiers, never a stand-in")
    return TASK_DIFFICULTY[verb]


def _frame(fx: Any, pool: float, opposition: Optional[float], forgery_quality: float,
           room_terms: dict, effort: int, verb: str, edge: tuple = ()) -> SocialContestInput:
    """THE RECORD, FILLED THE ONE WAY: what `contest_input` (the true input) and `believed_input` (a
    person's) both hand the module. They differ in where the pool's opposition, the forgery quality
    and the room terms COME FROM; the fixtures and the record's shape are this
    function's alone, so the two modes cannot compose different obstacles from the same fields."""
    return SocialContestInput(
        pool=pool, opposition=opposition,
        obstacle_default=fx.get("obstacle_default"),
        obstacle_ceiling=fx.get("obstacle_ceiling"),
        ceiling_per_pool=fx.get("ceiling_per_pool"),
        obstacle_refusal_multiple=fx.get("obstacle_refusal_multiple"),
        leverage=advantage_sigma(fx, {EFFORT: effort, EDGE: edge}),      # the one place the operands are named
        forgery_quality=forgery_quality, difficulty=_difficulty(fx, verb), **room_terms)


# ---------------------------------------------------------------------------------------------
# EXACT ODDS (CP-T01-03): what a roll of this record would deal, read and never rolled.
# ---------------------------------------------------------------------------------------------
# The claim a person holds about another's capability, and its one reader (`believed_capability`), are
# `queries/person_q.py`'s (B04.22: the read the confer term also makes). NOTHING DEPOSITS ONE TODAY, so a believed
# opposition is `None` for every person in a built realm until a depositor exists; this is the reading, not the writer.
OBSTACLE_ROLE = "social_contest.obstacle"   # the composition row whose module composes the obstacle
QUERY_ENTRIES = ((OBSTACLE_ROLE, "query"),)  # the host's declared need, held at driver construction (`registrar.require_entries`)


def _composed_obstacle(inp: SocialContestInput) -> float:
    """The obstacle the module composes for `inp`, reached by the `social_contest.obstacle` composition row."""
    return composition.require(OBSTACLE_ROLE)(inp)


def _composed_terms(inp: SocialContestInput) -> dict:
    """The obstacle's named terms for `inp` (`roll.py::obstacle_terms`), read from the module the obstacle row's
    target names (loaded by `composition.require`), as `_composed_obstacle` reads the obstacle."""
    composition.require(OBSTACLE_ROLE)
    module = sys.modules[composition.ROLES[OBSTACLE_ROLE]["target"].partition(":")[0]]
    return module.obstacle_terms(inp)[1]


def _odds_of_input(inp: SocialContestInput) -> Optional[tuple]:
    """`record_odds` over one record: the module's obstacle, the record's pool and leverage (the owner
    derives the roll's boost from them). `None` where S27.4 refuses the attempt -- no dice are dealt, so there is no distribution
    (`resolve` refuses on the same pair, one rule: `ob > multiple x pool`)."""
    ob = _composed_obstacle(inp)
    if ob > inp.obstacle_refusal_multiple * max(inp.pool, 0):
        return None
    return record_odds(inp.pool, ob, inp.leverage)


def believed_input(p: Any, verb: str, subject: Optional[str], fx: Any, *,
                   pool: float, person_subject: bool, examined_record: bool = False,
                   room: Optional[dict] = None, heard: bool = False,
                   effort: int = 0) -> Optional[SocialContestInput]:
    """THE PERSON'S RECORD (mode (b)): the same `SocialContestInput`, filled only from what `p` holds.

    AX-2: it reads `p` (his own ledger) and the fixtures, never the World; the
    facts about the act's SHAPE that only a World can answer (`person_subject`: the subject is a person;
    `examined_record`: an inquiry examines a Record; `heard`: a bench hears the contest) are the
    caller's, not a belief. His pool is his own and held with certainty: the caller passes it as `pool`
    (`odds_of` computes it with `faculty(w, believer, verb)`, which reads the log of his OWN acts for the
    practice addend: the one World read mode (b) makes, and it is of himself), so `faculty` stays the one
    pool reader. Every other field is filled
    only from what he holds, and WHERE A FACTOR IS UNKNOWN TO HIM THE ANSWER IS `None`, never a figure:
      * the opposition of a person subject, on a verb that names a capability key: a claim in his
        ledger on that subject at `CAPABILITY_CLAIM + key` (the latest, then the most confident);
        none held -> unknown. A non-person subject has no opposition (the task's difficulty alone on the
        task arm, the module's stand-in on the control), and that is known. A person subject on a verb naming
        no key opposes at the untrained score on every arm (`pool.untrained`, every person's score on no
        vocation, so known; the dealt roll reads the same, B05.11).
      * an examined Record's forgery quality: a property of the Record, held by nobody's claim here
        -> unknown.
      * the room's terms (`reception`, `proofs`) read other persons' ledgers: unknown unless the caller
        passes his own believed `room` (`{"reception": .., "proofs": ..}`).
    His `effort` is his own act's, held with certainty like his pool (CP-T01-05)."""
    roles = {r.role for r in _social_rows()}
    key = VERB_CAPABILITY.get(verb)
    opposition = None
    # THE TABLE'S TERMS, as the dealt roll reads them (`_read_social_roll`): no `opposes` row, no opposition term (and none to
    # be unknown about); no `dice` row, a pool of 0.
    if "opposes" in roles and person_subject and key and subject != p.id:
        said = believed_capability(p, subject, key)
        if said is None:
            return None
        opposition = float(said)
    elif "opposes" in roles and person_subject and subject != p.id:
        # A VERB NAMING NO KEY (`lie`), ON EVERY ARM: the roll opposes a person with `pool.score`, which on such a verb is
        # the untrained score for EVERY person (`pool.untrained`; nothing can be held on no vocation), so it is known,
        # and the believed obstacle is the dealt one (B05.11: `_opposition_of` returns the score on every arm, so no arm
        # keeps a `None` here for the module's stand-in).
        opposition = float(untrained(fx))
    if examined_record:
        return None
    # THE `capability` SOURCE'S ROWS, as the believer can read them: his own side is his to know; the subject's is a claim of his
    # (`CAPABILITY_CLAIM` + the key), and where he holds none the answer is unknown, never a figure.
    def believed_subject(row, key):
        if not person_subject or subject == p.id:
            return None
        said = believed_capability(p, subject, key)
        return _UNKNOWN if said is None else (SimpleNamespace(capability={row.key: said}), said)
    edge = _edge_reads(verb, p, believed_subject)
    if edge is _UNKNOWN:
        return None
    room_terms = {}
    if heard:
        if room is None:
            return None
        room_terms = dict(reception=room["reception"], reception_gain=fx.get("reception_gain"),
                          proofs=room["proofs"], proof_step=fx.get("proof_step"))
    return _frame(fx, pool if "dice" in roles else 0, opposition, 0.0, room_terms, effort, verb, edge)


def _rolled_as(w: Any, act: Any, owner: str = _PROVIDER) -> Optional[tuple]:
    """`(claimants, subject, room, examined)` exactly as the fold hands the act to `resolve`, or `None`
    when `owner`'s roll does not deal it (an uncontested act, another provider's prize, a party
    gap; `owner` is the social roll's unless `odds_of` asks for combat's). The derivation is the fold's
    own: `loop/sides.py::_contests_of` and `::sides_of` and the prize row's `heard_by:` for a contest; the verb's `graded_inquiries` route for an inquiry. `loop.sides`
    imports nothing that imports `seam` (`loop/__init__.py` imports nothing), so this module imports it at module
    level; `loop.resolve` would close a cycle the census counts (`tests/valoria/test_import_cycle_game_state_npe.py`),
    which is why the contest-of-an-act helper lives in `sides.py`."""
    from ...data.rosters import GRADED_INQUIRIES
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
        return parties, subject, (rung if prize.get("heard_by") == BENCH else None), None
    route = GRADED_INQUIRIES.get(act.verb)
    if route is not None and route.get("provider") == owner:
        subject = payload.get("subject")
        return [act.actor], subject, None, subject
    return None


def _estimated(w: Any, act: Any) -> tuple:
    """`(True, odds)` when the provider of `act`'s prize registered an ESTIMATE (`@provider("estimate", <provider>)`:
    personal combat's `fight_estimate`, mass battle's `field_estimate`), `odds` being that provider's tuple or `None`;
    `(False, None)` when it did not (the social roll's case, `odds_of` below). The seam names the ROLE; which module
    answers is the prize row's `provider:`, so neither fight is named here (CP-T04-08). The act's parties are the fold's own derivation (`loop.sides`);
    none -> `None`, as the social roll's `_rolled_as` answers a party gap."""
    row = VERB_TABLE.get(act.verb)
    contests = _contests_of(act, row)
    prize = _prize_row("contest", contests[0]) if contests else None
    estimator = _provider_for("estimate", prize.get("provider")) if prize else None
    if estimator is None:
        return False, None
    payload = act.payload if isinstance(act.payload, dict) else {}
    target = payload.get(row.opponent_operand() if row is not None else "subject")
    claimants = sides_of(w, act, target, contests[0])[0]
    return True, (estimator(w, act, claimants, target) if claimants else None)


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
    MODE (b) IS NOT BUILT for a fight: a believer's call falls through to the social roll below, which does
    not deal the act, so `believed_chance` is `None` and the chooser's score is as it was (AQ-X1 (b)'s combat
    term is not proposed here). No loop caller reaches mode (a): the display is the player's.

    A ROW CONTESTING `a field` (CP-T04-08, MODE (a) ONLY, AQ-X1: no NPC reads it) IS MASS BATTLE'S: the answer is
    `mass_battle.field_estimate`'s shares as `(Won, Lost, Unopposed)` (`mass_battle.ESTIMATE_BANDS`), the field's three
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
    parties, subject, room, examined = called
    effort = effort_of(act)                 # the act's own, as the fold hands it to `resolve`
    if w.persons.get(parties[0]) is None:
        return None
    if believer is not None and believer.id != act.actor:
        return None                     # another's pool is not his own to know
    if believer is None:
        return _odds_of_input(contest_input(w, parties, verb=act.verb, subject=subject, room=room,
                                            examined=examined, effort=effort))
    inp = believed_input(believer, act.verb, subject, w.fixtures,
                         pool=faculty(w, believer, act.verb),
                         person_subject=bool(subject) and subject in w.persons,
                         examined_record=examined is not None and examined in w.records,
                         room=believed_room, heard=room is not None, effort=effort)
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

    A QUERY, NOT A STORE (`04` §A.2: the chooser asks, the host answers): `loop/deliberate.py` closes it over
    the frozen store and hands the chooser `View.odds`, so `decision/` holds a callable and never the store
    (AX-2). READ-ONLY, like `odds_of`. `believer` is the person choosing; another actor's act is `None`
    (`odds_of`'s own refusal)."""
    odds = odds_of(w, act, believer=believer)
    if odds is None:
        return None
    held = [_BAND_PLACE.get(b) for b in bands]
    if not held or None in held:
        return None
    return sum(odds[n] for n in held)


def believed_odds_query(w: Any, holder: Any):
    """THE QUERY THE CHOOSER IS HANDED (`View.odds`): `believed_chance` closed over `w` and BOUND TO `holder`, as
    `(act, bands) -> chance or None`. The query answers for its holder alone (`04` §20, the own-ledger rule: a
    person's View carries his own record): it takes no person, so nothing downstream can ask it for another's
    belief. The ONE place the closure is made -- `loop/deliberate.py` hands it to every person's View and the
    harness readings that score a person outside `choose` (`harness/decision_spread.py`,
    `harness/interactions.py`) take it from here, so the figure they read is the figure the chooser reads."""
    return lambda act, bands: believed_chance(w, holder, act, bands)


@provider("contest", _PROVIDER)
def resolve(w: Any, claimants: list, causes: list, prize: Any, *,
            verb: str = "", subject: Optional[str] = None,
            rng: Optional[random.Random] = None, rung: Optional[str] = None,
            module_entry: Optional[str] = None, effort: int = 0, host: Any = None) -> dict:
    """Roll for one contested act: build the record, call the module entry, hold its return to a
    `Margin`, refuse S27.4. Returns a net/ob pair, NEVER a band and never a winner.

    `host` (v10 REM-31) is accepted and NOT USED HERE: the seam's call is uniform, and only the
    personal-combat provider has a PLAYABLE mode (`seam/wrappers/combat.py::resolve`).

    `effort` is the act's own (CP-T01-05, `state/carriers.py::effort_of`, passed by `seam/contest.py`): it
    reaches only `contest_input`, where it becomes `leverage`; the act's draw is unchanged (one id, one draw).

    RESOLVED -> dict(status, module, resolver, pool, ob, net, leverage, settled_margin, ob_terms, fed_by)   # the entry's Margin + the record
                 # + the real margin `net - ob` the ladder quantises once (B05.02), the number `degree_of` grades
    REFUSED  -> dict(status, why, module, resolver, pool, ob, ob_terms, fed_by)   # S27.4: ob > obstacle_refusal_multiple x pool
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
    declaring `heard_by: bench` (`a matter`, `speak`'s) has the bench sitting over it read the speaker
    (`contest_input`'s `room`). Every other prize still derives its obstacle from the parties alone.

    ⚠ THE RNG IS A PARAMETER: THE DRIVER'S GENERATOR IS PASSED ON EVERY SHIPPED PATH (`loop/resolve.py`), AND A
    HAND CALL WITH NONE IS REFUSED (`InstrumentDefect`, naming the caller; never a fresh unseeded `random.Random()`,
    never the process-global stream, never a seeded one made here). THAT IS `04 §C.12`'s REJECTION 4:
    *"its generator must be constructed by the driver from the run seed and passed down exactly as `World` is."*
    ⚠ *"Threaded like `World`"* MEANS PASSED BY PARAMETER RATHER THAN REACHABLE BY A GLOBAL NAME —
    not one continuous stream. `04 PART D row 35` settles it: `H(seed, tick, subject, purpose)`, no
    counter, no service. A single stream threaded through a season would make every roll depend on
    the count of prior draws, so adding one contested verb would move every other verb's outcome.

    ⚠ S27.4 IS EVALUATED HERE, AFTER THE ENTRY, on the pair the entry RETURNS: the
    obstacle is the module's (`roll.py::obstacle`, ED-SC-0033 clause (3)), so the host has no pair
    until the entry has run. A refused act's roll is discarded; its generator is the act's own
    (`H(seed, tick, subject, purpose)` above), so no other act's draw moves. Under the shipped
    ceiling (`H-213`, 2 = the multiple x the 1D floor) a derived pair with a pool of 1 or more is
    never refused here; only a pool below the floor is.

    ⚠ `module_entry` IS THE INQUIRIES' ROUTE (`ED-FI-0009`, J-22 (A)): `seam/contest.py::grade`
    passes the role a `graded_inquiries` row names, with `prize=None`, and everything else here is the
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
    heard = rung if row is not None and row.get("heard_by") == BENCH else None
    # An inquiry (no prize) examines its subject; a Record's forgery quality
    # enters the obstacle (`contest_input`'s `examined`). A prize names a contest, which examines nothing.
    inp, reads = _read_social_roll(w, claimants, verb=verb, subject=subject, room=heard,
                                   examined=subject if prize is None else None, effort=effort)
    entry, refusal = entry_for(prize, _PROVIDER, module_entry)
    if entry is None:
        return refusal
    # ONE generator for the act's whole roll: the module's draw (`entry.fn`) is the only one. An absent `rng` is a caller that handed no generator -- an instrument defect, refused naming
    # that caller, never a fresh unseeded `random.Random()` and never the process-global stream (04 §C.12: the RNG
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
    # B11 lane A: every term of the obstacle, named, on the roll's record (`roll.py::obstacle_terms`).
    ob_terms = _composed_terms(inp)
    if margin.ob > inp.obstacle_refusal_multiple * max(inp.pool, 0):
        return dict(status="REFUSED", why="S27.4", module=_PROVIDER,
                    resolver=_RESOLVER, pool=inp.pool, ob=margin.ob, ob_terms=ob_terms,
                    fed_by=_fed_by(reads, inp, ob_terms))
    # B05.02: the margin is REAL -- `net` (the one sampler's draw plus the boost) less `ob` -- and the ladder quantises
    # it once (`degree_from_net`, `MARGIN_SCALE`). Nothing is settled here and no second draw is made: the act's stream
    # is the module's roll alone. The record keeps the name `settled_margin` (B05.18 reads it as a real margin).
    settled = margin.net - margin.ob
    # The margin's own fields, copied whole: the host reads the pair, it never computes one.
    return dict(status="RESOLVED", module=_PROVIDER, resolver=_RESOLVER, pool=inp.pool,
                **asdict(margin), leverage=inp.leverage, settled_margin=settled, ob_terms=ob_terms,
                fed_by=_fed_by(reads, inp, ob_terms))
