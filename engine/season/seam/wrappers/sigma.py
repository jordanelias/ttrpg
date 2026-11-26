"""THE SOCIAL CONTEST SCENE'S CONTEST PROVIDER — the host adapter and the host INPUT BUILDER for the
`social_contest` module's σ-leverage roll (plan position `31a`, A-25; registered as
`@provider("contest", "social_contest")`, which the prize rows `a standing`, `a proposition` and `a matter`
name, ED-SC-0033 clause (2)). The file keeps its name because its automated mode is the σ-leverage roll
(`modules/social_contest/roll.py`'s docstring).

`04_CODE_ARCHITECTURE.md` §A.2:182 types `seam/wrappers/*` as writing *"nothing, ever"*, reading
*"the projection"*, returning *"a `Margin`"*, holding token *"none"*. This module is that row. It
DECIDES NOTHING: `contest_input` (the host input builder) derives a pool and reads the obstacle's raw
operands from what the actor and the subject genuinely have -- for a prize a room hears (`heard_by:`),
that includes the room's reading of the actor and the actor's unmirrored proofs through `queries/world_q.py`'s `reception` and
`proofs`. F8 HOLDS for both (`04_CODE_ARCHITECTURE.md` §B.2:250; B24.02, option B): each reads the ACTOR'S OWN ledger (`claimants[0]`, passed as `actor`) and
no other, and what the rest of the bench and the opponent have said in public is read off their live `commit` edges, which are World edges
and in no ledger (`hole_register.yaml` H-215 (7), H-216 (7)) -- and freezes them into `queries/inputs.py::SocialContestInput` (the hostile half as the obstacle's
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
import sys
from dataclasses import asdict, dataclass, replace
from types import MappingProxyType, SimpleNamespace
from typing import Any, Mapping, NamedTuple, Optional

from engine.dice_engine.dice_engine import BAND_FLOORS, DEGREE_LABEL, DEGREE_ORDINAL, MARGIN_SCALE, Degree
from engine.dice_engine.draw import Draw
from engine.dice_engine import fmath
from engine.dice_engine.fmath import ltr_sum
from engine.dice_engine.sigma_leverage import level as sigma_level, levels_to_net_sigma, record_odds
from engine.substrate import composition, descriptors

from ...data.affiliations import AFFILIATION_CEILING
from ...decision.decider import decides_for, make_decider
from ...data.arrangements import ARRANGEMENTS, CONTEXT, DISPOSAL, RITES, abridged, in_form
from ...data.rosters import GRADED_TASKS, STANCE_MAX
from ...data.rosters import (AUTHORITY_BY_FACTION, DIFFICULTY_LEVELS, GROUNDS, ISSUE_RUNGS, MATTERS, PROCEEDING_ENDS, PROCEEDING_MOVES,
                             RUNG_KINDS, matter_of_record)
from ...data.rosters import ACT_WHEN_KEYS, FACTION_BY_PROP, capability_rows, obstacle_bound, require_use_site, roster, when_holds
from ...data.verbs import BACKED_VERBS, FORM_INQUIRY, PROCEEDS_DOCKET, SOCIAL_ROLL_PROVIDER, VERB_CAPABILITY, VERB_TABLE, _OPENERS_FROM_EFFECTS
from ...epistemic import trail_concealment
from .edge import CAPABILITY, EDGE, _capability_levels, _edge_levels  # (moved: see edge.py)
from ...gaps import InstrumentDefect, Unspecified
from ...loop.sides import _contests_of, seat_named_by, sides_of
from ...queries.person_q import (BEARING_PARTS, believed_capability, believes, bearing, claim_origin, conflict, contradicts, false_items, holds_dispute, proof_kind, stance_toward,
                                 strain_carried, takes_side, tie)
from ...queries.person_q import care as person_care
# ⚠ THE LEAF, NOT THE PACKAGE'S RE-EXPORT. `manifest/providers.py` imports nothing, so no import
# here closes a loop back into this package (`_entry.py` says the same of the entry lookup);
# `manifest/registry.py` imports only `data/` and `gaps` and `queries/` is below `seam/`, so the
# two imports below close none either.
from ...manifest.providers import provider
from ...manifest.registry import (BELIEVED_ESTIMATE_ROLE, BENCH, HEARD_BY_ROOMS, RESIDENTS, SEAT_BODY, TOWARD_TO, call as _provider_for,
                                  resolve as _prize_row)
from ...queries import world_q as _world_q
from ...queries.inputs import (SIDE_SIGN, SIDES, Card, Choice, Input, Item, Margin, Outcome, Point, Present, Rite, SocialContestInput,
                               is_answered, is_filed, is_first, other_side)
# The room's two resolver-side reads. The host READS them; the module composes the obstacle they move.
from ...queries.faction_q import weight as faction_weight
from ...queries.world_q import admitted_kinds, ambitions, case_file_for, declared_votes_by_member, docketed_row, faction_holding, faction_of, hold_force, judging_set, place_of, presence, proofs, rattled_since, reception, residence_of, side_of
from ...state.carriers import EFFORT, Said, effort_of
from ...state.gate import BENCH_BASIS, UNDECLARED_DISPOSAL, across_chains, seat_faction, sits_over
from ...state.ids import draw_factory
from ...state.ledgers import present_confidence
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
# `EDGE`, `CAPABILITY`, `_edge_levels` and `_capability_levels` are `edge.py`'s (the leaf `queries/cache.py` and `loop/resolve.py` read a site's net sigma through, which
# may not import this module: it imports `epistemic`); bound here by name for this module and its importers.
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
    """`proofs`' levels: one `proof_level` per whole unit of `operands["proofs"]` -- FOR the roller: `(levels, [])`. Empty where the fixture is `None`.
    B24.21: THE LEDGER'S LEVELS ONLY. For a docketed matter whose case file is the source (`evidence_from: case_file`) `_read_social_roll` hands it `proofs` 0.0, so it brings nothing, and the case file's
    exhibits bring theirs through the roll (`roll.proof_levels`, counted onto `resolve`'s `levels` by `_with_exhibits`): one matter's proofs are never read from both."""
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


# ---------------------------------------------------------------------------------------------
# THE FOUR CONDITIONS OF AN ACT (B24.35, WGM edit 2): the `capability_when_keys` members a uses row's reader does not read (`data/rosters.py::ROW_WHEN_KEYS`).
# Each is the host-side function of one key, `fn(w, ctx, hearer, arg) -> bool`, over `ctx` (the sitting's operands: its arguer `for_id`, its matter `topic`
# and the kinds the act cites, `cited`) and the HEARER (a `Person`, his interior only): it reads the act's payload, the ARGUER'S OWN ledger and the hearer's
# interior fields -- his stance, pursuits and live edges -- and never the hearer's ledger (`04` §B.2 F8). `arg` is the ground's `backed_by` value
# (`rosters.yaml: grounds`). They decide which grounds BACK an act with a hearer (`_backed`, `Present.backed`), where `fit_level` alone sizes what a ground is worth.
# ---------------------------------------------------------------------------------------------
def _when_cites(w: Any, ctx: Any, hearer: Any, kind: str) -> bool:
    """`cites: <matters member>`: the act cites at least one held item of `kind` (`world_q.cited_kinds`, carried as `ctx.cited`)."""
    return kind in ctx.cited


def _matter_subject(w: Any, topic: Optional[str]) -> Optional[str]:
    """Whom the argued matter is about: the subject of the Proposition `topic` names, else `topic` itself (a matter that is a person or a case)."""
    prop = w.propositions.get(topic) if topic is not None else None
    return topic if prop is None else prop.subject


def _when_consequence_held(w: Any, ctx: Any, hearer: Any, want: bool) -> bool:
    """`consequence_held: true`: the ARGUER'S own ledger holds a deed claim about the matter's subject that the HEARER'S own pursuits score against (`person_q.holds_dispute`,
    the one owner of that judgement, asked of a copy of the hearer carrying the arguer's ledger: his pursuits, stance and scars judge, and his own ledger is never opened)."""
    arguer, subject = w.persons.get(ctx.for_id), _matter_subject(w, ctx.topic)
    if arguer is None or subject is None or arguer is hearer:
        return not want
    judge = copy.copy(hearer)
    judge.ledger = arguer.ledger
    fx = w.fixtures
    return holds_dispute(judge, subject, fx.get("scar_weight_shift"), fx.get("sworn_bond"), fx.get("deed_counterparty"), fx.get("scar_hold"),
                         fx.get("scar_primary_mass")) == want


def _when_creed_committed(w: Any, ctx: Any, hearer: Any, want: bool) -> bool:
    """`creed_committed: true`: the matter is a faction's creed Proposition (`FACTION_BY_PROP`) and the hearer holds a live `commit` to it (`world_q.ambitions`, the one owner of
    a live commit to an OUGHT; his own edges, never a ledger) [ASSUMPTION: the creed half of the design's Authority, kept; basis: the hearer's live Tenures are interior fields]."""
    return (ctx.topic in FACTION_BY_PROP and ctx.topic in ambitions(w, hearer)) == want


def _when_regard_at_least(w: Any, ctx: Any, hearer: Any, n: float) -> bool:
    """`regard_at_least: n`: the hearer's stance toward the arguer, clamped at `STANCE_MAX` (`person_q.stance_toward`, his own rows), is at least `n`."""
    return min(stance_toward(hearer, ctx.for_id), STANCE_MAX) >= n


#: THE CONDITIONS' BINDING (`_bound_to`: refused at import if `capability_when_keys` and these functions differ either way; `rank_at_least` is a row's, not bound here).
WHEN_BACKING = _bound_to({"cites": _when_cites, "consequence_held": _when_consequence_held, "creed_committed": _when_creed_committed,
                          "regard_at_least": _when_regard_at_least}, "capability_when_keys",
                         members=ACT_WHEN_KEYS,
                         law="WGM edit 2 -- a `when` key is evaluated by one function, and a ground names only keys that have one")
for _ground, _row in GROUNDS.items():
    if (_kind := (_row.get("backed_by") or {}).get("cites")) is not None and _kind not in MATTERS:
        raise Unspecified(f"ground {_ground!r} is backed by `cites: {_kind!r}`, which is no `matters` member", "rosters.yaml -- grounds",
                          needs=f"one of {sorted(MATTERS)}", law="a cited kind is a proof kind (`matters`); any other would back nothing, silently")


def _backed(w: Any, hearer: Any, ctx: Any) -> Optional[tuple]:
    """`Present.backed` OF `hearer` FOR THIS ACT (B24.35, WGM edits 2-3): `None` (every ground) for an act whose verb is not a `rosters.yaml: backed_verbs` member, for the arguer
    himself and for a hearer who holds no trait that a ground seats (`descriptors.TRAITS[*].seated_by`, the grounds that move him); else the tuple of THOSE grounds whose `backed_by` holds -- each of its conditions (`WHEN_BACKING`), the ground's
    own cell. So a ground must be chosen (the speaker's) AND backed (the act's), and `fit_level` alone sizes what it is worth. [ASSUMPTION; medium; Jordan to correct: the act's arguer
    is the bearer, `claimants[0]`, for every speech of the sitting; revert: `return None`.]"""
    held = {descriptors.TRAITS[t].seated_by for t in (hearer.traits or ()) if t in descriptors.TRAITS}
    moved_by = tuple(g for g in GROUNDS if g in held)
    if not moved_by or hearer.id == ctx.for_id or ctx.verb not in BACKED_VERBS:
        return None
    return tuple(g for g in moved_by if all(WHEN_BACKING[k](w, ctx, hearer, v) for k, v in (GROUNDS[g].get("backed_by") or {}).items()))


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
    Record an inquiry examines) and, for a prize a room hears, the actor's own ledger and the bench's and the opponent's live commits
    through `queries/world_q.py::reception` and `proofs` (the actor, `claimants[0]`, is the one whose ledger they may read); the module that consumes the record never sees
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
    person, or a contest a prize names carries `0`. B11.68: an INQUIRY (a `graded_tasks` row of `form: inquiry`) also carries the strongest live cover
    among the doers of the trail it can uncover (`epistemic.trail_concealment`), the larger of the two, so a covered doer's deed is harder to find."""
    fx = w.fixtures
    docketed = _docketed_row(w, subject)                                        # the arrangement row the act's matter is heard under, if one is docketed (B05.21)
    room_terms = {}
    # B24.21 (EVID_B edit 5): WHERE THE PROOFS COME FROM. At `evidence_from: case_file` a matter whose docket item names a case file in the world has its exhibits filed there as its proofs, so the ledger is read for
    # it by nothing (`proofs` 0.0: `_proof_levels` brings no level, and the exhibits' levels are the roll's own, `roll.proof_levels`); at `ledger` (the control) and for a matter with no case file, `world_q.proofs` as before.
    case = _filed_case(w, room, subject)
    if room is not None:
        audience = audience_of(w, HeardAct(claimants[0], via, room), heard_by)
        # `toward: to` (U5c §2 edit 4): the room is asked about the receiver, here the act's person counterparty [ASSUMPTION: `to` is the roll's `subject`; no row declares it until `a holding`'s verb lands].
        room_terms = dict(reception=reception(w, subject if toward == TOWARD_TO else claimants[0], audience, claimants[0]),
                          reception_gain=fx.get("reception_gain"),
                          proofs=0.0 if case is not None else proofs(w, claimants[0], subject, audience, admitted=_admitted_proofs(fx, docketed)))
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
    counts = dict(rank_gap=_rank_gap_of(w, via, subject),                       # the subject's rank above the exercised seat (B21.09)
                  cross_chain=int(across_chains(w, via, seat)),                 # the named seat is of another chain than the exercised one (B21.61)
                  faction_power=_faction_power_of(w, via, subject) if seat is not None else 0)     # the holder's faction against the host's, where the act names a seat (B21.69)
    # B11.68 (`IS-B2-FI-07` (3)): an INQUIRY about a trail meets its doers' covers -- the strongest, once, beside the examined Record's own quality (the larger of the two).
    concealed = max(doc.forgery_quality if doc is not None else 0.0,
                    trail_concealment(w, examined, claimants[0]) if examined is not None and (GRADED_TASKS.get(verb) or {}).get("form") == FORM_INQUIRY else 0.0)
    inp = _frame(fx, pool, opposition, concealed, room_terms, effort, verb, edge, circumstance, office,
                 docketed=docketed, heard=room is not None, regard=regard, bodies=bodies, counts=counts,
                 exhibits=_exhibits_of(w, case) if case is not None else (), side=_side_of(claimants[0], subject))
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


# `_docketed_row` and `_admitted_proofs` are `world_q.docketed_row` and `world_q.admitted_kinds` (B24.25: the speech that files an item and this host read the one row and the one admission).
_docketed_row, _admitted_proofs = docketed_row, admitted_kinds


# ---------------------------------------------------------------------------------------------
# THE CASE FILE'S EXHIBITS (B24.21; EVID_B "Exact edits" 5). Where `Fixtures.evidence_from` is `case_file`, the `proofs` a docketed matter's act brings are the exhibits filed on the matter's
# case file, not the speaker's ledger: this reader turns the file's `filed` stages into the `Item`s `SocialContestInput.exhibits` carries, each with its relation to the others, and
# nothing else. The host does NOT call `standing` and imports nothing of the evidence module: the roll counts them (`roll.proof_levels`, reached by its composition row, `_with_exhibits`),
# and a sitting's close counts them (`proceeding._lever`, on `Input.exhibits`, which `proceeding_input` builds by this same reader: B24's close, R1).
# ---------------------------------------------------------------------------------------------
# THE STAGES ARE `queries/inputs.py`'s (`is_filed`, `is_answered`: the ONE owner of their shapes; `_eff_speak` writes them, this reads them).
_CONTRADICTS, _AGREES = "contradicts", "agrees"       # the two relations `Item.pairs` names; the module reads the words, the host does not import it


def _filed_case(w: Any, room: Optional[str], subject: Optional[str]) -> Optional[str]:
    """THE CASE FILE A HEARD ACT'S `proofs` ARE READ FROM, or `None` (B24.21, B24.43): at `evidence_from: case_file`, the file a matter's docket item names where a room hears the act; else `None`, and the ledger
    is read (`world_q.proofs`). The ONE reader of the arm for the single roll, the dealt record (`_read_social_roll`) and the believed one (`odds_of`), so the two cannot read one matter's proofs
    from two places. A verb that proceeds never reaches either: its sitting reads the same file by `case_file_for` (`proceeding_input`; a sitting has no room operand)."""
    return case_file_for(w, subject) if room is not None and w.fixtures.get("evidence_from") == "case_file" else None


def _knows(p: Any, ref: Any) -> bool:
    """DOES `p` KNOW OF A FILED ITEM (B24.43): a claim `ref` where his own ledger holds that cell (his own claim, or the copy a citation told him, B24.24), a Record `ref` where he holds it or holds a claim
    about it (the content claim a citation of it tells). What he knows was filed is what he heard cited or filed himself. [ASSUMPTION; Jordan to correct; revert: the full case file]"""
    if isinstance(ref, Said):
        return any((c.subject, c.predicate, c.value) == (ref.subject, ref.predicate, ref.value) for c in p.ledger)
    return any(t.kind == "hold" and t.live and t.object == ref for t in p.tenures) or any(c.subject == ref for c in p.ledger)


def _relation(a: Said, b: Said) -> Optional[str]:
    """How two filed claims stand: `contradicts` where the pairing rule's owner says so (`person_q.contradicts`, the one call of `_pair`), `agrees` where they are of the same cell and do
    not, else `None` (another cell). The same cell is `(subject, predicate)`, the key the owner pairs on."""
    if (a.subject, a.predicate) != (b.subject, b.predicate):
        return None
    return _CONTRADICTS if contradicts(a, b) else _AGREES


def _exhibits_of(w: Any, case: str, known: Optional[Any] = None) -> tuple:
    """THE EXHIBITS OF A CASE FILE, in the order filed: one `Item` for each `filed` stage, its id the stage's place on the file (`<case>#<index>`, the index an answer names), its `side`, `rung`,
    `weight` and `origin` the stage's, its `kind` what the claim is as proof (`person_q.proof_kind`; a Record's is the kind its `matters` carrier names, as `_items_of`), its `cell` the claim's own, and
    its `pairs` the relation to every other filed claim (`_relation`). EVERY FILED STAGE IS AN EXHIBIT: the filing admitted it (B24.25 refuses a kind the row does not admit before the draw), so a
    claim `proof_kind` has no kind for (a cell, which the hearing's gates file) is a `testimony`, the kind of a claim a person holds and tells [ASSUMPTION; Jordan to correct; revert: drop such a stage;
    basis: `kind` is read by the sitting's admission and by neither the roll nor `standing`]. `answered_band` is the BEST band among the `answered` stages that name the exhibit
    (the sitting keeps the best, B24.19) and `forged_found` whether any of them cited a finding that the Record is forged (`inputs.ANSWERED_STAGE`, written by `_eff_speak`). `first` is
    the stage's first-heard mark (`inputs.is_first`, B24.26): an `answer` to the exhibit meets the `first_heard` term.
    `known` (B24.43) is the believer, a `Person`, or `None` for the dealt record (the whole file): the file as HE knows it (`_knows`), a stage he knows nothing of no exhibit, and no relation
    to or from it (he cannot see a clash with what he has not heard), the stage places and the answers the file's own."""
    items = []
    stages = w.records[case].stages
    by_target: dict = {}                                    # the `answered` stages by the exhibit they name, in the file's order
    for sa in stages:
        if is_answered(sa):
            by_target.setdefault(sa[2], []).append(sa)
    for i, st in enumerate(stages):
        if not is_filed(st) or (known is not None and not _knows(known, st[4])):
            continue
        _, _, side, rung, ref, weight, origin, *_ = st
        rec = None if isinstance(ref, Said) else w.records.get(ref)
        kind = (proof_kind(ref) or "testimony") if isinstance(ref, Said) else matter_of_record(rec.kind) if rec is not None else "record"
        iid = f"{case}#{i}"
        answers = [(_BAND_PLACE[sa[3]], sa[3], sa[4]) for sa in by_target.get(i, ())]      # the answers drawn against this exhibit
        best = max(answers)[1] if answers else None                                                                                   # the best band, as the sitting keeps it (B24.19)
        items.append(Item(iid, kind, float(weight), about=ref.subject if isinstance(ref, Said) else ref, side=side, rung=rung, origin=origin,
                          cell=(ref.subject, ref.predicate, ref.value) if isinstance(ref, Said) else (), answered_band=best,
                          forged_found=any(imp for _, _, imp in answers), first=is_first(st)))
    return _paired(items)


def _paired(items) -> tuple:
    """EACH `Item` WITH ITS `pairs` (B24.19's cell): `(other id, _relation of the two cells)` for every other item of `items` that has a `cell`, the relation the pairing rule's
    owner gives (`person_q.contradicts`, through `_relation`). THE ONE PASS the host computes `Item.pairs` by: a case file's exhibits (`_exhibits_of`) and a sitting's hands with
    the matter's exhibits together (`proceeding_input`, B24's close R2), so a sitting's `answer`, agreement and corroboration read the same relation as the case file's. An item
    with no cell (a Record, a seat, an oath, a false word) is paired with nothing."""
    said = [Said(*it.cell, 0) if it.cell else None for it in items]
    return tuple(replace(it, pairs=tuple((o.id, how) for o, b in zip(items, said) if o.id != it.id and a is not None and b is not None and (how := _relation(a, b)) is not None))
                 for it, a in zip(items, said))


def _heard_on_docket(verb: str) -> bool:
    """IS `verb` A HEARING OF A DOCKETED MATTER: its `proceeds:` cell names the docket's row (`speak`, `determine`). The one reading of the cell for the arrangement the docket
    gives a sitting (`arranged_by`) and for the case file a sitting reads its exhibits from (`proceeding_input`)."""
    return any(entry[1] == PROCEEDS_DOCKET for entry in getattr(VERB_TABLE.get(verb), "proceeds", ()))


def _filed_exhibits(w: Any, verb: str, topic: Optional[str], knower: Any = None) -> tuple:
    """THE EXHIBITS A SITTING OF `verb` ON `topic` READS FROM THE CASE FILE (`proceeding_input`): `_exhibits_of` of the file the matter's docket item names, as `knower` knows it
    (`None`: the whole file), at `evidence_from: case_file` for a verb heard on the docket; else `()`."""
    case = case_file_for(w, topic) if w.fixtures.get("evidence_from") == "case_file" and _heard_on_docket(verb) else None
    return _exhibits_of(w, case, known=knower) if case is not None else ()


def _sitting_items(w: Any, room: tuple, exhibits: tuple) -> tuple:
    """`(room, exhibits)` OF ONE SITTING, PAIRED (B24's close, R1 and R2): every item in a hand and every filed exhibit, each with its relation to all the others (`_paired`, one
    pass), so an item filed and also held is the same cell to `evidence.standing` (the same origin corroborates once, the other side's same cell counts for neither). A Record
    filed on the case file has no cell to pair by, so it leaves its holder's hand: it is before the room already, and shown twice it would count twice."""
    filed = {e.about for e in exhibits if not e.cell and e.about in w.records}
    hands = [tuple(it for it in p.items if it.id not in filed) for p in room]
    paired = _paired((*exhibits, *(it for h in hands for it in h)))
    out, k = [], len(exhibits)
    for p, h in zip(room, hands):
        out.append(replace(p, items=paired[k:k + len(h)]))
        k += len(h)
    return tuple(out), paired[:len(exhibits)]


def _on_axis(exhibits: tuple, bearer_side: str) -> tuple:
    """THE EXHIBITS ON A SITTING'S AXIS: a filed stage's `side` is the case's (`world_q.side_of`: `for` the accusation, `against` the accused's own plea), a sitting's is the
    bearer's (`for` is `claimants[0]`, `proceeding_input`). Where the bearer is on the case's `against` (the accused speaking to his own matter) every side turns over; else
    they are the same axis and nothing changes."""
    if bearer_side == "for":
        return exhibits
    return tuple(replace(e, side=None if e.side is None else other_side(e.side)) for e in exhibits)


_side_of = side_of     # `world_q.side_of`: the side a speech to a matter is on, read by the host's roller and by the speech that files his exhibits (B24.25)


PROOF_LEVELS_ROLE = "social_contest.proof_levels"   # the composition row whose module counts the filed exhibits' levels (`roll.proof_levels`)


def _with_exhibits(inp: SocialContestInput, levels: tuple) -> tuple:
    """`(levels, leverage)` AS ROLLED: the record's own `levels` (`_levels_count`) and `leverage` with the filed exhibits' levels added, the counts the roll's own reader gives (`roll.proof_levels`,
    by role) put on the `proofs` member and one `proof_level` each through the one level table -- exactly what `roll.leverage` applies, so the record names what was rolled. Unchanged where nothing is
    filed or `proof_level` names no level (the control)."""
    n_for, n_against = composition.require(PROOF_LEVELS_ROLE)(inp) if inp.exhibits and inp.proof_level is not None else (0, 0)
    if not (n_for or n_against):
        return levels, inp.leverage
    return (tuple((name, f + n_for, a + n_against) if name == "proofs" else (name, f, a) for name, f, a in levels),
            inp.leverage + levels_to_net_sigma([inp.proof_level] * n_for, [inp.proof_level] * n_against))


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
        theirs = max((_rung_rank(w, w.offices[t.object].rung) or 0 for t in w.seat_holds(subject)), default=0)
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
           regard: Optional[float] = None, bodies: tuple = (None, None), counts: Optional[dict] = None,
           exhibits: tuple = (), side: str = "for") -> SocialContestInput:
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
        exhibits=exhibits, proof_level=fx.get("proof_level"), side=side, evidence_cap=fx.get("evidence_cap"),     # B24.21: the four the roll's `proof_levels` reads, carried RAW; leverage, never an obstacle operand
        **obstacle_operands(fx, dict(verb=verb, opposition=opposition, circumstance=circumstance,
                                     reception=room_terms.get("reception", 0.0), docketed=docketed, heard=heard, regard=regard,
                                     **(counts or {}))),
        **room_terms)


# ---------------------------------------------------------------------------------------------
# EXACT ODDS (CP-T01-03): what a roll of this record would deal, read and never rolled.
# ---------------------------------------------------------------------------------------------
# The claim a person holds about another's capability, and its one reader (`believed_capability`), are
# `queries/person_q.py`'s (B04.22: the read the confer term also makes). NOTHING DEPOSITS ONE TODAY, so a believed
# opposition is `None` for every person in a built realm until a depositor exists; this is the reading, not the writer.
OBSTACLE_ROLE = "social_contest.obstacle"   # the composition row whose module composes the obstacle
QUERY_ENTRIES = ((OBSTACLE_ROLE, "query"), (PROOF_LEVELS_ROLE, "query"))  # the host's declared need, held at driver construction (`registrar.require_entries`)


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
                   tick: int = 0, exhibits: tuple = ()) -> Optional[SocialContestInput]:
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
      * the room's terms (`reception`, `proofs`) read the bench's and the opponent's public commits, which are not the believer's own
        claims: unknown unless the caller passes his own believed `room` (`{"reception": .., "proofs": ..}`).
    His `effort` is his own act's, held with certainty like his pool (CP-T01-05), and so is the level of the seat he acts through
    (`office`, B05.20): the caller's, read off the seat's own row (`_seat_modifier`), as `person_subject` is the caller's. So is the arrangement
    row the matter is docketed under (`docketed`, B05.21): the docket is public, the caller reads it. THE COUNTERPARTY'S STANCE TOWARD THE ACTOR IS
    HIS INTERIOR, held in no claim of the believer's: where `regard_step` is not 0 and one person stands alone opposite, it is unknown to him (`None`),
    never a figure; at 0 the term reads nothing, so the answer is as it was; AT THE `ordinary` PRIOR it is read neutral (regard 0, an ordinary
    person's), so he gets a figure.
    `exhibits` (B24.43) are the items of the matter's case file that HE knows were filed (`_exhibits_of(w, case, known=him)`, which `odds_of` reads: the file is public, the docket's), at
    `evidence_from: case_file`; they reach the record through `_frame` as the dealt record's do, and the `proofs` of `room` are then zero (`odds_of` hands them so), as the dealt record's are:
    one matter's proofs are never read from both. `()` at `ledger`, where nothing is filed to know."""
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
                  docketed=docketed, heard=heard, bodies=(_body_of(p), None), exhibits=exhibits, side=_side_of(p.id, subject))      # his own body is his to know; another person's is not without a claim (B05.60)


def _rolled_as(w: Any, act: Any, owner: str = _PROVIDER) -> Optional[tuple]:
    """`(claimants, subject, room, examined, prize, seat)` exactly as the fold hands the act to `resolve` (`prize` the contested prize's row, or `None`; `seat` the
    seat the act names where its prize says one does, `loop/sides.py::seat_named_by`, else `None`), or `None`
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
        return parties, subject, (rung if prize.get("heard_by") else None), None, prize, seat_named_by(w, act, contests[0])
    route = graded_route(act.verb, w.fixtures)          # B07.01: the fold's own reading of the route (`task_draw_arm`)
    if route is not None and route.get("provider") == owner:
        subject = payload.get("subject")
        return [act.actor], subject, None, subject, None, None
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
    if called is None or getattr(VERB_TABLE.get(act.verb), "proceeds", ()):
        return None                     # a verb that proceeds is dealt by the sitting, not the social roll (`_believed_proceeding_chance` is its odds, `_rolled_as` its room)
    parties, subject, room, examined, prize, seat = called
    effort = effort_of(act)                 # the act's own, as the fold hands it to `resolve`
    if w.persons.get(parties[0]) is None:
        return None
    if believer is not None and believer.id != act.actor:
        return None                     # another's pool is not his own to know
    if believer is None:
        hearing = {} if prize is None else dict(heard_by=prize.get("heard_by") or BENCH, toward=prize.get("toward"))
        return _odds_of_input(contest_input(w, parties, verb=act.verb, subject=subject, room=room,
                                            examined=examined, effort=effort, via=act.via,
                                            seat=seat,
                                            **hearing))
    case = _filed_case(w, room, subject)        # B24.43: the dealt record's own reading of where the proofs come from
    inp = believed_input(believer, act.verb, subject, w.fixtures,
                         pool=faculty(w, believer, act.verb),
                         person_subject=bool(subject) and subject in w.persons,
                         examined_record=examined is not None and examined in w.records,
                         room=believed_room if case is None or believed_room is None else {**believed_room, "proofs": 0.0},
                         heard=room is not None, effort=effort, office=_seat_modifier(w, act.via, room),
                         docketed=_docketed_row(w, subject), tick=w.tick,
                         exhibits=_exhibits_of(w, case, known=believer) if case is not None else ())
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
            proceeds: Optional[tuple] = None, topic: Optional[str] = None, arranger: Optional[str] = None, rig: float = 0.0,
            seat: Optional[str] = None, first_heard: bool = False, cited: tuple = (), answered_over: Optional[float] = None) -> dict:
    """Roll for one contested act: build the record, call the module entry, hold its return to a
    `Margin`, refuse S27.4. Returns a net/ob pair, NEVER a band and never a winner.

    `proceeds` (B24p.14) is `(row dict, form, move, item)`, the verb row's cell as the seam resolves it (B24p.19), and `None` for every act
    that does not proceed: the body below is then what it was. `topic` is the matter the proceeding is about (the act's `subject` where its
    opponent is another operand, the docket's matter where the opponent is the `subject`). Given, the act is a PROCEEDING instead: `_resolve_proceeding` builds the
    room (`proceeding_input`), calls the entry the composition row `social_contest.proceeding` names, holds its return to an `Outcome` of
    `Margin` verdicts and reads the act's record off it (`act_band`). `prize`, `rung`, `module_entry` and `via` are not read on that path.
    `arranger` and `rig` (B24p.24) are the arrangement the docket gave the sitting (`arranged_by`), read by the builder on that path alone. `first_heard` (B24.26) is
    `world_q.answers_first` of the act, read on that path alone. `cited` (B24.35) is `world_q.cited_kinds` of the act, read on that path alone. `answered_over` (B24.43) is `world_q.answered_over` of the act, read on that path alone.

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
                                   arranger=arranger, rig=rig, host=host, first_heard=first_heard, cited=cited, answered_over=answered_over)
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
    levels, leverage = _with_exhibits(inp, levels)      # B24.21: the filed exhibits' levels the roll applied (`roll.proof_levels`), named on the record beside the host's own sources
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
                **asdict(margin), leverage=leverage, settled_margin=settled,
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
#: THE SIX SETTINGS THE HEARING'S BOARD READS (B24.06, HEAR_B edit 10; `H-216`, `H-662` to `H-664`; B24.19, `H-666`; B24.26, `H-668`), beside the fifty-four: the closing draw's
#: `proof_level` (one per whole unit of net standing weight) and `fault_step` (one per level owed), an `answer`'s `answer_ob` (its difficulty) and `answer_step`
#: (the weight term), `evidence_cap` (what corroboration may gain, read by `evidence.standing`) and `first_heard_ob` (what an answer to an item first heard adds).
#: Not V2's settings, so not in `PROCEEDING_SETTINGS`; `proceeding_dials` names both tuples.
HEARING_SETTINGS = ("proof_level", "fault_step", "answer_ob", "answer_step", "evidence_cap", "first_heard_ob")


def proceeding_dials(fx: Any) -> Any:
    """THE ONE PLACE THE PROCEEDING'S SETTINGS ARE NAMED FOR THE MODULE (B24p.04): the fifty-four `PROCEEDING_SETTINGS` read off `fx`,
    beside the dice settings the proceeding shares with the single roll -- `pool_add` and `pool_floor` (`pool_pair`, the one reader of
    the `social_roll` site's `dice` row), `pool_default` and `opposition_rate` -- and the attribute scale's three numbers
    (`descriptors.ATTRIBUTE_FLOOR` and `ATTRIBUTE_CEILING`, and `pool.attribute_midpoint()`, the one mid-point), sixty-one names in all,
    as a read-only mapping (sixty-five with B24.06's four). The fold's `fold_*` coefficients are not in it. `proceeding_input` (B24p.13) reads it and adds the two rosters
    the module is handed (`moves`, `reads`), which are not settings. B24.06 adds the four `HEARING_SETTINGS` the board reads (`Input.dials`, B24.05)."""
    pool_add, pool_floor = pool_pair(fx)
    d = {name: fx.get(name) for name in PROCEEDING_SETTINGS + HEARING_SETTINGS}
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

_SIX = ("focus", "reason", "attunement", "presence", "grace", "will")      # the six attributes a `Present` carries, by the module's names


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
    lean: Optional[tuple] = None     # B24.11: `((member, signed live commits on the motion), ...)` of a `declared` sitting (`world_q.declared_votes_by_member`), else `None`
    cited: tuple = ()                # B24.35: the `matters` kinds the act's cited items are (`world_q.cited_kinds`), what `cites` reads
    verb: str = ""                   # B24.35: the act's verb, which `_backed` asks `rosters.yaml: backed_verbs`


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


def _top_seat(w: Any, pid: str) -> Optional[Any]:
    """His highest seat (by rung ordinal, then id), or `None` for a man with none: the one seat `_power` and the declared ballot (`_ballot_start`) read."""
    seats = _seats_held(w, pid)
    return max(seats, key=lambda o: (_rung_ordinal(w, o), o.id)) if seats else None


def _power(w: Any, pid: str, regime: dict) -> tuple:
    """`(power, precedence)` of a person (V2 p2 §H): his highest seat's rung ordinal, plus twice the level of its `modifier`, plus the
    regime's weight for the authority of its faction. A man with no seat has none (0, 0)."""
    top = _top_seat(w, pid)
    if top is None:
        return 0.0, 0
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
    """The rite's cells with the row's, then the context's deltas (V2 p2 §B, §I). Every number here is a cell of a table or a setting.

    B24.10 (HEAR_B edit 6; `IS-B2-SC-03` step 3): THE RITE IS READ OFF THE ARRANGEMENT ROW (`row["rite"]`), with the hearing's cells it carries (the bench's own
    moves beside the two sides', `faults`, `disclosed`, `bears_by_rung`). THE SWITCH: a BENCH'S OWN SITTING (a row whose `close` is `bench` or `declared`, in the full
    form: `abridged` is a speech, whose close is `exchange`) spends no exchange at `Fixtures.sitting_exchanges` 0 (the control): its turns are `(0, 0)`, so
    nobody speaks and the close is the one draw it was before the hearing, through the same `roll` (HEAR_B gate 1)."""
    cells, (lo, hi) = RITES[row["rite"]], row["turns"]
    if row["close"] in ("bench", "declared") and not fx.get("sitting_exchanges"):
        lo = hi = 0
    silence = cells["silence"]
    if regime["silence"] is not None and not (silence == "free" and "must" not in cells["reply"].values()):
        silence = regime["silence"]
    if silence == "free" and "must" in cells["reply"].values():
        silence = "refusal"                                   # never free where an answer is owed (A-145; V2 p4 §L 6)
    admits = tuple(dict.fromkeys(k for k in (*row["admits"], *regime["admits_add"]) if k not in regime["admits_drop"]))
    moves = row.get("moves") or {**cells["moves"], **({"bench": cells["bench"]} if cells["bench"] else {})}
    return Rite(id=cells["id"], live=cells["live"], bears=cells["bears"], reply=tuple(cells["reply"].items()), silence=silence,
                issues=tuple(cells["issues"]), concede=cells["concede"], moves=tuple((s, tuple(ms)) for s, ms in moves.items()),
                faults=tuple(cells["faults"]), disclosed=cells["disclosed"], bears_by_rung=tuple(cells["bears_by_rung"].items()),
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


def _watchers(w: Any, here: list, floor: str, basis: Optional[str]) -> list:
    """Those of `here` (who is present at the venue, none where there is none) the row's floor lets watch: `open` all, `closed` none, `admitted`
    the holders of a seat (of one granting `basis` where the row names one) `[ASSUMPTION; Jordan to correct: the model admits the holders of an office]`."""
    if floor == "closed":
        return []
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
    the kind of proof each is, `person_q.proof_kind`: a cell or a withheld confession is none and is no item), and, for a speaker, his own false word (`false_items`). `debt` (an oath owed to him is on
    the debtor's side) and `precedent`, `confession` and `state_of_realm` (the case file and the strife reading) have no carrier he holds `[HOOK]`."""
    out = []
    for t in p.tenures:
        if not t.live:
            continue
        if t.kind == "hold" and t.object in w.records:
            rec = w.records[t.object]
            out.append(Item(rec.id, matter_of_record(rec.kind), 1.0, source=p.id, origin=rec.id))     # a Record's origin is itself (`world_q.filings`' rule)
        elif t.kind == "hold" and t.object in w.offices:
            out.append(Item(t.id, "title", 1.0, source=p.id, about=t.object))
        elif t.kind == "oblige" and not t.imposed and t.subject == p.id:
            out.append(Item(t.id, "oath", 1.0, source=p.id, about=t.object))
    if ctx.topic is not None:
        full, decay = ctx.fx.get("confidence_default"), ctx.fx.claim_decay()
        for c in p.ledger:
            if c.subject == ctx.topic and (kind := proof_kind(c)) is not None:
                out.append(Item(c.id, kind, _clip01(present_confidence(c.confidence, c.when, w.tick, decay) / full), source=p.id, about=c.subject,
                                cell=(c.subject, c.predicate, c.value),      # the cell as held, the shape `_exhibits_of` gives a filed claim (B24.21)
                                origin=claim_origin(c.chain, p.id)))     # the root of its chain, else his own (`world_q.filings`' rule): what `impugn` halves by (R2)
        if side is not None:
            out.extend(false_items(p, ctx.topic, side, ctx.fx, w.tick))
    return tuple(it for it in out if it.kind in ctx.admits)


def _ballot_start(fx: Any, signed: int, modifier: Optional[str]) -> float:
    """B24.11 (`U5c_SC_proceedings_residue.md` §6 items 2 and 3): WHERE A SEAT'S TRACK STARTS AT A `declared` SITTING, in track units, the close's own slope (`track_step`) turning each
    level into the start that closes on it: `signed` (his live commits for the motion less those against, `world_q.declared_votes_by_member`) times one `lean_level` a commit, plus
    the one level his seat row's `modifier:` names (his help on his own ballot, D-U1-01; none where the row names none), each read through `level`. A seat's commits are where his
    track starts, never a leverage source at the close (V2 p1 §B D8; `lean` is not an `advantage_sources` member). `0.0` for a `track_step` of 0, and no commit moves him at a
    `lean_level` of `None` (the control) [ASSUMPTION; medium; Jordan to correct; revert: drop the `modifier` term -- the seat's help enters his start in the same units as a
    commit because the module has no per-seat leverage channel; `_power` already reads the modifier for his station]."""
    step, lean = fx.get("track_step"), fx.get("lean_level")
    if not step:
        return 0.0
    return ((signed * sigma_level(lean) if signed and lean is not None else 0.0) + (sigma_level(modifier) if modifier else 0.0)) / step


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
    if decides and ctx.lean is not None:
        top = _top_seat(w, p.id)
        start += _ballot_start(fx, dict(ctx.lean).get(p.id, 0), top.modifier if top is not None else None)      # B24.11: a declared seat's commits and his seat's help
    power, precedence = _power(w, p.id, ctx.regime)
    return Present(id=p.id, weight=int(p.weight), side=side, decides=decides, **attr,
                   rank=float((p.capability or {}).get(ctx.rank_key) or 0) if ctx.rank_key else 0.0,
                   care=care, stake=stake, bonds=bonds, start=start, holds=_holds(p, ctx.bears),
                   believes=believes(p, ctx.topic, fx, w.tick) if ctx.topic is not None else 0.0,
                   bias=0.0,                                  # [HOOK: his stable misjudgement has no carrier]
                   power=power, precedence=precedence, items=_items_of(w, p, ctx, side), backed=_backed(w, p, ctx),
                   # what he carries in is the rattles of this season's sittings (`world_q.rattled_since`, B24p.20), his OWN: a person a chooser pictures
                   # (`_Believed`'s shell, an ordinary man) is no world's person and carries none
                   strain=strain_carried(rattled_since(w, p.id) if w.persons.get(p.id) is p else (), fx))


def _rank_key(issue: Optional[str] = None) -> Optional[str]:
    """The one skill whose rank joins the dice of a drawing move (`rosters.yaml: proceeding_moves`' `capability`; V2 p2 §A.1: `rank` is one
    number, his rank in the proceeding's skill), read as `pool._capability` reads a verb's skill: off the person's `capability`.
    B24.10 (HEAR_B edit 6; HCAP edit 6): a `capability:` cell is a skill id or a MAP by issue rung (B24.04), read AT `issue`, the rung the sitting opens on
    (the first of its rite's issues); a sitting with no issue ladder (a speech) has no rung to key a map, so only a single-id cell names its skill.
    Every drawing move must name the same skill at that rung, since `Present.rank` is one number a sitting: a rung where two moves name two (`argue` on
    `law` at a definition, `press` on `argue`) is a sitting the module must read `rank` per rung for, which this reader refuses rather than choose."""
    keys = {k for m in PROCEEDING_MOVES.values() if m["draw"]
            for k in ((m["capability"],) if isinstance(m["capability"], str) else (m["capability"].get(issue),)) if k is not None}
    if len(keys) > 1:
        raise Unspecified(f"the drawing moves name {sorted(keys)} as their skill at {issue or 'a sitting with no issue ladder'}",
                          "rosters.yaml -- proceeding_moves", needs="one skill",
                          law="V2 p2 §A.1 -- `Present.rank` is his rank in the proceeding's skill, one number")
    return next(iter(keys), None)


def public_lean(w: Any, close: str, topic: Optional[str], row: dict) -> Optional[tuple]:
    """B24.29: `((member, signed live commits on the motion), ...)` of a `declared` sitting (`world_q.declared_votes_by_member`: a commit is public), else `None`. The one
    reader of the bench's public lean: `proceeding_input` starts each seat's track on it, `_resolve_proceeding` writes its signs on the sitting."""
    return tuple(declared_votes_by_member(w, topic, row).items()) if close == "declared" and topic is not None else None


def bench_reading(w: Any, viewer: str, seat: str, sign: int) -> int:
    """B24.29 (V2 p2 §C.6; A-30): THE SIGN OF `seat`'s LEAN AS `viewer` READS IT, `sign` (+1 or -1) the sign the sitting wrote of it. A KEYED DRAW, `H(seed, tick, viewer,
    "bench_read:<seat>")`, ONE STREAM A READING (`draw_factory`): his accuracy `acc` is the module's own (`accuracy`: his Attunement alone, opposed by nothing, with the stream's
    first normal for luck), and the sign he holds is the true one with chance `(1 + acc) / 2` -- the share of the truth `acc` reaches, the rest a guess (`_Believed`'s reading
    of a claim) -- the stream's next uniform. So a wrong sign is possible at every Attunement and a truer one is likelier at a higher. It reads his own Attunement (`w.persons[viewer]`)
    and the sign given and nothing of the seat; it writes nothing (`loop/witness.py::_sitting_claims` deposits it in his own ledger).
    [ASSUMPTION; medium; Jordan to correct; basis: the entry's chance `acc` for a two-valued sign; read so, a man below the scale's middle would be wrong more often than right,
    and the gate asks a share above 0.5 at Attunement 2; revert: `d.random() < acc`]"""
    d = draw_factory(w.world_seed, lambda: w.tick)(viewer, f"bench_read:{seat}")
    mid = attribute_midpoint()
    attunement = (w.persons[viewer].attributes or {}).get(descriptors.ATTRIBUTE_NAMES["attunement"])
    acc = _proceeding_module().accuracy(proceeding_dials(w.fixtures), mid if attunement is None else attunement, d.normal(0.0, 1.0))
    return sign if d.random() < (1.0 + acc) / 2.0 else -sign


def proceeding_input(w: Any, claimants: list, *, verb: str, subject: Optional[str], topic: Optional[str], effort: int, row: dict,
                     arranger: Optional[str] = None, rig: float = 0.0, form: str = "auto", state: Any = None,
                     seen: Optional[Mapping] = None, first_heard: bool = False, cited: tuple = (), answered_over: Optional[float] = None,
                     knower: Any = None, exhibits: Optional[tuple] = None) -> tuple:
    """`(Input, Card)`: THE HOST BUILDER OF A PROCEEDING (V2 p2 §A, §H, §I; B24p.13). `claimants[0]` is the bearer (`for`); the other party is the
    next claimant, else `subject` where he is a person other than the bearer, else (where the rite gives the other side moves) the most opposed
    man on the floor. `row` is an arrangement row (a seeded one, or `abridged(row)`'s); `form` is `full`, `abridged` or `auto` (abridged where
    the act's `effort` is 0 and nobody watches). `arranger` and `rig` are the arrangement (p2 §H); `topic` is the matter argued.

    Refused, each a `ValueError` whose message begins `refused[<key>]`: `unlawful`, `absent`, `both_parties`, `no_seat`, `short_bench`,
    `bad_weight`, and (from `Input`) the sitting's own invariants. It reads `w.persons`, `w.offices`, `w.fixtures`, seats, Tenures, and each
    person's own interior and ledger; never `proofs` or `reception`, and never one person's ledger for another's values. It writes nothing.

    `seen` (B24p.14) is the persons as a READER sees them, `{id: Person}`, each `Present` built from his entry where it has one and from the
    world's otherwise: who sits, who is a party and what is public (seats, ties, weight) are the world's either way; the believed odds
    (`believed_proceeding_odds`) pass the chooser's picture of the others. `first_heard` (B24.26) is `world_q.answers_first` of the act: the speech answers an item the room heard first,
    and meets the `first_heard` term (`Input.first_heard`). `cited` (B24.35) is `world_q.cited_kinds` of the act: the proof kinds it cites, which `cites` (`WHEN_BACKING`) reads
    into each hearer's `Present.backed`; the arguer of every speech of the sitting is the bearer, `claimants[0]`. `answered_over` (B24.43) is `world_q.answered_over` of the act: the weight the item it answers
    holds over its answer (`Input.answered_over`), which makes the abridged speech the sitting's `answer` (difficulty `answer_ob`, the `answer` term on this weight).
    THE CASE FILE (B24's close, R1; B24.20, B24.21): for a verb heard on the docket (`_heard_on_docket`) at `evidence_from: case_file`, the matter's filed exhibits
    (`_exhibits_of` of `case_file_for(topic)`, the file as `knower` knows it where a reader's odds are built, `believed_proceeding`) are `Input.exhibits`, on the sitting's
    axis (`_on_axis`), paired with every item in a hand (`_sitting_items`); the module counts them on the close (`proceeding._lever`). Never the board. `exhibits` is that
    file's `_filed_exhibits` where the caller built it already (`believed_proceeding`, which builds two sittings of one file), else read here.
    """
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
    venue = place_of(w, topic) or place_of(w, fid)         # [ASSUMPTION; Jordan to correct: the matter's place, not the actor's (the seam's own rule is the act's venue: loop/sides.py); basis: B24p.13's builder reads the matter's venue]
    floor = row["floor"] if regime["floor"] is None else regime["floor"]
    # B24.10, the engagement read (HEAR_B edit 6): until Batch B28 (`28_CORE_scene_access_A`) lands it, every attendee at the venue is present and free to
    # sit ("at its control the sitting assumes attendees free", NEG's Depends line); `presence` is that read, and B28's engagement filter composes here
    here = [x for x in dict.fromkeys(presence(w, venue)) if x in w.persons] if venue is not None else []
    watchers = [x for x in _watchers(w, here, floor, row["floor_basis"] if regime["floor"] is None else None) if x not in (fid, aid)]
    if form == "abridged" or (form == "auto" and effort <= 0 and not watchers):
        row = abridged(row) if row["close"] != "exchange" else row
    rite = _rite_of(fx, verb, row, effort, regime, strife)
    moves, close = dict(rite.moves), rite.close
    bench = _bench_of(w, venue, topic, row["authority"]) if close in ("bench", "declared") else []
    # a speech put to no man (`speak` at a sitting, a self-plea) is put to the presiding seat of the row's own bench, who is the one addressed
    # [ASSUMPTION; Jordan to correct: B24p.19 -- the abridged row (`abridged()`) keeps its authority but no bench, so the speaker would sit alone (`refused[one_character]`)]
    # he is the one addressed and decides, but he is NOT a party (no side, never `against_id`): a party's stake floor is the party's, not his (V2 p4 §L 2)
    addressed = None
    if aid is None and close == "exchange":
        sitting = sorted(_bench_of(w, venue, topic, row["authority"]), key=lambda x: (-_power(w, x, regime)[1], x))
        addressed = next((x for x in sitting if x != fid), None)
    # the other party: where the rite gives the other side moves and the matter names nobody, the most opposed man on the floor (p4 §K D4)
    if aid is None and addressed is None and moves.get("against"):
        stakes = {x: bearing(w.persons[x], {}, for_party=fid, against_party=None, edges=w.persons[x].tenures)
                  for x in here if x != fid and x not in bench}
        opposed = [x for x, stake in stakes.items() if takes_side(stake) == "against"]
        if opposed:
            aid = min(opposed, key=lambda x: (ltr_sum(stakes[x]), x))
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
    if addressed is not None:
        add(addressed, None, True)
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
                   room=tuple(cells), factions=factions, presume=fx.get("presume_step") * tilt * SIDE_SIGN[arr_side] if tilt > 0 else 0.0,
                   rank_key=_rank_key(rite.issues[0] if rite.issues else None),
                   lean=public_lean(w, close, topic, row), cited=tuple(cited), verb=verb)
    room = tuple(_present(w, (seen or {}).get(x, w.persons[x]), side, decides, ctx) for x, (side, decides) in cells.items())
    filed = _filed_exhibits(w, verb, topic, knower) if exhibits is None else exhibits
    room, exhibits = _sitting_items(w, room, _on_axis(filed, _side_of(fid, subject)))
    dials = dict(proceeding_dials(fx))
    dials["moves"] = {m: (r["effect"], r["draw"]) for m, r in PROCEEDING_MOVES.items()}      # the two rosters the module is handed (its head)
    dials["reads"] = {g: r["reads"] for g, r in GROUNDS.items()}
    inp = Input(rite=rite, matter=topic if topic is not None else (subject or ""), room=room,
                grounds=tuple((g, r["reason"], era[g]) for g, r in GROUNDS.items()), dials=MappingProxyType(dials), state=state,
                frames=tuple(sorted({(c, t) for p in room for c, t, _, _ in p.holds})), first_heard=first_heard, answered_over=answered_over, exhibits=exhibits)
    return inp, card(inp, row, Arrangement(arr if tilt > 0 else None, tilt, None if tilt <= 0 else other_side(arr_side), tuple(recused)))


def card(inp: Input, row: dict, arrangement: Arrangement) -> Card:
    """THE CARD (V2 p1 §E; pure): what the proceeding IS, derived from the built rite and room and never authored. It holds no true attribute and
    no true start; its `odds` is the close itself where nobody speaks (`card_odds`), `None` where nothing is drawn."""
    mod, rite = _proceeding_module(), inp.rite
    moves, ds = dict(rite.moves), [p for p in inp.room if p.decides]
    bearer = mod.lead(inp, rite.bears)
    owed = dict(rite.reply).get(other_side(rite.bears)) == "must" and rite.silence != "free"
    unmoved = fmath.ltr_sum(mod.silence_cost(inp, d, None, bearer) for d in ds) / len(ds) if (owed and bearer is not None and ds) else 0.0
    if rite.silence == "free":
        silence = "free: nothing here must be answered, and silence costs nothing"
    else:
        side = "against" if dict(rite.reply).get("against") == "must" else rite.bears
        owes = mod.lead(inp, side) or (ds[0] if ds else None)
        pt = Point(-1, other_side(side), "", "", None, "", ())
        cost = fmath.ltr_sum(mod.silence_cost(inp, d, pt, owes) for d in ds) / len(ds) if (ds and owes is not None) else 0.0
        silence = f"{rite.silence}: a point owed an answer and left standing costs {cost:.2f} with each who decides" \
            + (" (he decides himself, and answers to the contempt of those present)" if ds == [owes] else "") \
            + (", and counts with him again as tacitly admitted" if rite.silence == "admits" else "")
    return Card(kind=row["id"], genre=RITES[row["rite"]]["genre"], arranged_by=arrangement.arranger, tilt=round(arrangement.tilt, 2),
                tilted_against=arrangement.tilted_against, stake=row["disposes"], outcomes=tuple(DISPOSAL[row["disposes"]].items()),
                room=tuple((p.id, ("speaks " + p.side + (" and judges" if p.decides else "")) if p.side else ("judges" if p.decides else "attends"),
                            round(p.power, 1)) for p in inp.room),
                live=rite.live, bears=rite.bears, reply=rite.reply, moves=rite.moves,
                barred=tuple((s, m) for s in SIDES for m in PROCEEDING_MOVES if moves.get(s) and m not in moves[s]),
                admits=rite.admits, close=rite.close, decided_by=tuple(p.id for p in ds), turns=rite.turns, issues=rite.issues,
                silence=silence,
                unargued=(f"it lapses: the bearer must put it, and his rest is priced as silence ({unmoved:.2f} with those who decide)" if owed and unmoved
                          else "it stands where the room starts: the bearer decides it himself" if owed
                          else "it stands where the room starts"),
                ends="/".join(PROCEEDING_ENDS), standard=rite.standard, unrest=rite.unrest, gravity=rite.gravity,
                reason_weight=tuple((g, mod.reason_tenths(inp, g) / 10) for g, _, _ in inp.grounds),
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
        return (None if beat.ground is None else mod.case_pool(inp, mod.who(inp, beat.voice), beat.ground)), None
    tracks = dict(out.state.tracks)
    drawn = [mod.close_record(inp, tracks[i]) for i in read]
    heads = [weights[i] for i in read]
    return drawn[0][0], ltr_sum(h * rec.leverage for h, (_, rec) in zip(heads, drawn)) / ltr_sum(heads)


_DATA_DEFECTS = ("refused[bad_weight]", "refused[no_weight]")


HEARING_MOVE_KEY, ARGUMENT_GROUND_KEY = "hearing_move", "argument_ground"   # the two choice keys of a hearing: values `proceeding_moves` and `rosters.yaml: grounds`


@dataclass(frozen=True)
class _Pick:
    """What `make_decider` is handed: the `legal` values, which are the `View`'s own `Option`s, and the `View` they are read from, which the pick's `odds` reads."""
    legal: tuple
    view: Any


def _believed_chance(inp: Input, pick: _Pick, option: Any) -> Optional[float]:
    """`odds=` OF THE PICK (B24.13): the chance the matter goes the mover's way on the room as HE reads it after `option`. `Option.ev` is the option's PERCEIVED worth to
    the mover in track units (it carries what the option costs him, which is how the Class S costs of B24.12 reach the believed verdict), so the believed track it
    leaves, toward `for`, is `t + _sg(side) * ev` with `t = _sg(side) * view.mood * mood_scale` (`view_odds`' reading). `p_carried` is P(carried) toward `for` (the module's
    pure closed form), so the chance is it for a `for` mover and `1 - it` for an `against` mover, on the board's leverage the view carries (`View.lever`, the close's own
    `_lever`: one ladder with `view_odds` and the close, R12). Nothing true enters it. `None` where nothing is drawn (a `consent` close)."""
    if inp.rite.close == "consent":
        return None
    v = pick.view
    sg = SIDE_SIGN.get(v.side, -1.0)                     # the module's `_sg`: a side that is not `for` reads as `against`
    carried = _proceeding_module().p_carried(inp, sg * (v.mood * inp.dials["mood_scale"] + option.ev), v.lever)
    return carried if sg > 0 else 1.0 - carried


def _npc_decider(w: Any, inp: Input) -> Any:
    """THE NPC'S DECIDER OF A HEARING (B24.13; HEAR_B "Who decides"; `IS-B2-CHAR-02`): `(view, me) -> Choice`, the `decide=` callback the entry takes. ONE
    `make_decider` pick OVER THE VIEW'S OPTIONS (an item exposed and a person struck are properties of the option, so a move chosen blind first could not avoid a damning
    item): each `Option` is one value whose choice operands are its `hearing_move` (`proceeding_moves`) and its `argument_ground` (`rosters.yaml: grounds`), their cells summed
    into its pursuit, priced by the believed chance after it (`_believed_chance`, on the option's PERCEIVED worth). The stream is `draw_factory(seed, tick)(person,
    f"hearing:{matter}:{n}")`, `n` the exchange's number. The person is his own, `w.persons[me.id]`, read when he is asked; nothing is written. THE COST TERMS (B24.12)
    ARE NOT HERE. ⚠ FOR A PERSON THIS DECIDES, IT SUPERSEDES `policy`'s `grudge` term (`D["grudge"] * (-_bond(me, foe))`): the automatic policy is not run for him."""
    fx, base = w.fixtures, draw_factory(w.world_seed, lambda: w.tick)

    def decide(view: Any, me: Any) -> Choice:
        scoped = lambda pid, purpose: base(pid, f"hearing:{inp.matter}:{view.n}:{purpose}")
        o = make_decider(w.persons[me.id], fx, scoped, key=(HEARING_MOVE_KEY, ARGUMENT_GROUND_KEY), of=lambda o: (o.move, o.ground),
                         odds=lambda pick, o: _believed_chance(inp, pick, o))(_Pick(tuple(view.options), view))
        return Choice(o.move, o.ground, o.item, o.relation)
    return decide


def _played_by(w: Any, host: Any, inp: Input) -> dict:
    """THE DECIDER PASS (B24.10, B24.13; `PlayHost.deciders`, B24.05): the keyword the entry takes for the persons of THIS room who decide their own moves,
    `{"deciders": {person: callback}}`, else `{}` (the sitting is automatic, as it was). A person the host plays takes the host's decider for the role
    (`decide(view) -> choice`; the entry's callback is `(view, person)`, so it is the host's closed over), and none where the host has none for it; any other
    speaker takes the NPC decider (`_npc_decider`) where `Fixtures npc_decider_roles` names this role (`decider.decides_for`), else the automatic policy."""
    decide = getattr(host, "deciders", {}).get(PROCEEDING_ROLE)
    plays = getattr(host, "persons", frozenset())
    npc = None
    mine = {}
    for p in inp.room:
        if p.id in plays:
            if decide is not None:
                mine[p.id] = lambda view, me, d=decide: d(view)
        elif inp.rite.close != "exchange" and p.side and p.id in w.persons and decides_for(w.fixtures, PROCEEDING_ROLE, False):   # an abridged close asks no callback
            npc = npc or _npc_decider(w, inp)
            mine[p.id] = npc
    return {"deciders": mine} if mine else {}


def _resolve_proceeding(w: Any, claimants: list, rng: Draw, *, verb: str, subject: Optional[str], effort: int, proceeds: tuple,
                        topic: Optional[str] = None, arranger: Optional[str] = None, rig: float = 0.0, host: Any = None, first_heard: bool = False,
                        cited: tuple = (), answered_over: Optional[float] = None) -> dict:
    """`resolve`'s path for an act that proceeds: build the room, call the entry the composition row names (the persons a `host` plays are handed their
    decider, B24.10 `_played_by`; every other speaker takes `_npc_decider` where `Fixtures npc_decider_roles` names the role, B24.13, else the automatic policy), hold the return to an `Outcome` of `Margin` verdicts (a winner, a band or a side cannot cross
    the module boundary), read the act's record (`act_band`) and refuse S27.4 on an `exchange` close's pair only (a close is an adjudicator's
    draw and is never refused). RESOLVED -> `dict(status, module, resolver, pool, net, ob, leverage, terms, settled_margin, proceeding, card, arrangement, form, topic, read, starts)`
    (the last five are what `loop/resolve.py::_proceeding_ending` writes and `loop/effects_information.py::_eff_argue` reads, B24p.20).
    `move` and `item` of `proceeds` are read by no caller yet (the automatic policy chooses the speech). `claimants` are the persons
    of the act's two sides (`loop/sides.py`: where the opponent operand is the matter itself, as `speak`'s, the second is the matter and no
    party: the builder reads parties off persons only, the matter as `topic`). A proceeding the builder refuses (`refused[<key>]`: no seat,
    a party gone, one man as both parties, ...) is the game's refusal, never a raise: `REFUSED`, which the fold takes as the verb's refusal kind."""
    row, form, _move, _item = proceeds
    try:
        inp, card_ = proceeding_input(w, [c for c in claimants if c in w.persons], verb=verb, subject=subject,
                                      topic=subject if topic is None else topic, effort=effort, row=row, form=form,
                                      arranger=arranger, rig=rig, first_heard=first_heard, cited=cited, answered_over=answered_over)
    except ValueError as refused:
        if not str(refused).startswith("refused[") or str(refused).startswith(_DATA_DEFECTS):
            raise                                # a weight that is no whole head count is a data defect, not a room the game refuses
        return dict(status="REFUSED", why=str(refused), module=_PROVIDER, resolver=_RESOLVER, pool=None, terms=())
    entry = composition.require(PROCEEDING_ROLE)
    out = entry(inp, rng, **_played_by(w, host, inp))
    if not isinstance(out, Outcome) or not all(isinstance(v, tuple) and len(v) == 2 and isinstance(v[1], Margin) for v in out.verdicts):
        raise Unspecified(
            f"module entry {PROCEEDING_ROLE!r} ({entry.__module__}.{getattr(entry, '__qualname__', '?')}) returned {type(out).__name__} "
            f"{out!r:.120}, which is not an `Outcome` of `Margin` verdicts", "V2 p2 §M",
            needs="the entry returning `queries.inputs.Outcome`, each verdict a `Margin`",
            law="08_SEAM provider rule (intent) and S27.2 -- a provider returns MARGINS, never a winner; the band is the one ladder's reading")
    weights = {p.id: p.weight for p in inp.room}
    band = act_band(out, inp.rite, weights)
    # What the fold writes of this sitting (B24p.20): the arrangement and form it was held under, the matter, the verdicts the act's margin was read from
    # (`()` where a yield decided) and each person's track as the sitting began (a given `state`'s, else his `start`), which the fold's written tracks are asserted against.
    begun = dict(inp.state.tracks) if inp.state is not None else {p.id: p.start for p in inp.room}
    # B24.29: what the bench's public commits show of each seat who decides here, `(seat, sign)`; the signs are written on the sitting for each witness to read in his own way (`bench_reading`)
    deciding = {p.id for p in inp.room if p.decides}
    bench = tuple((m, 1 if n > 0 else -1) for m, n in (public_lean(w, inp.rite.close, inp.matter, row) or ()) if m in deciding)
    held = dict(module=_PROVIDER, resolver=_RESOLVER, proceeding=out, card=card_, arrangement=row["id"], form=form, topic=inp.matter,
                read=band["read"], starts=tuple(begun.items()), bench=bench)
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
            shell.traits = frozenset()               # B24.35: what moves him is no more known than his pursuits (WGM edit 5, the arguer's own knowledge of it, is not built)
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
                             proceeds: tuple, topic: Optional[str] = None, arranger: Optional[str] = None, rig: float = 0.0,
                             first_heard: bool = False, cited: tuple = (), answered_over: Optional[float] = None) -> Optional[float]:
    """THE CHOOSER'S OWN ODDS that the proceeding `proceeds` names carries (V2 p2 §E; B05.62): `view_odds` on an `Input` built from what
    he holds, read as his own view reads it, without luck. Himself at his true values, every other person an ordinary man (`_Believed`),
    so the odds are the close before an unmoved ordinary bench at the starts he believes `[ASSUMPTION: the chooser prices a full
    proceeding by the card's own odds as he reads them, and an abridged one by the same close on its one addressed man -- basis: V2 p2 §E,
    "the card's odds is the close before an unmoved ordinary bench"]`. His accuracy is the view's own (`View.acc`, read off a first pass).
    `None` where nothing is drawn (`consent`) or the proceeding is refused him (`refused[...]`); read-only, no draw. `arranger` and `rig`
    are the arrangement the sitting is held under (B24p.24), as `proceeding_input` reads them."""
    read = believed_proceeding(w, believer, claimants, verb=verb, subject=subject, effort=effort, proceeds=proceeds, topic=topic,
                               arranger=arranger, rig=rig, first_heard=first_heard, cited=cited, answered_over=answered_over)
    return None if read is None else read[0]


def believed_proceeding(w: Any, believer: Any, claimants: list, *, verb: str, subject: Optional[str], effort: int, proceeds: tuple,
                        topic: Optional[str] = None, arranger: Optional[str] = None, rig: float = 0.0, first_heard: bool = False,
                        cited: tuple = (), answered_over: Optional[float] = None) -> Optional[tuple]:
    """`(odds, tilt)` as `believed_proceeding_odds` reads the odds, with the tilt the same build gave the forum (B24p.24: the chooser prices a
    rig on the odds it buys and the tilt it costs, from one room). `None` where `believed_proceeding_odds` is."""
    row, form, _move, _item = proceeds
    mod = _proceeding_module()
    topic = subject if topic is None else topic
    filed = _filed_exhibits(w, verb, topic, believer)      # the case file as he knows it (B24.43's `_knows`), read once for the two passes below

    def read(acc: float) -> tuple:
        inp, card_ = proceeding_input(w, [c for c in claimants if c in w.persons], verb=verb, subject=subject, topic=topic,
                                      effort=effort, row=row, form=form, arranger=arranger, rig=rig, seen=_Believed(w, believer, acc), first_heard=first_heard,
                                      cited=cited, answered_over=answered_over, knower=believer, exhibits=filed)
        return inp, card_, mod.view(inp, mod.start(inp), mod.who(inp, believer.id), _NoNoise())
    try:
        inp, _, first = read(1.0)
        inp, card_, seen = read(first.acc)
    except ValueError as refused:
        if not str(refused).startswith("refused[") or str(refused).startswith(_DATA_DEFECTS):
            raise                                # the fold's own reading (`_resolve_proceeding`): a data defect is raised, a room the game refuses has no odds
        return None
    return None if inp.rite.close == "consent" else (seen.odds, card_.tilt)


def arranged_by(w: Any, act: Any, topic: Optional[str]) -> tuple:
    """`(arranger, rig)` THE DOCKET GIVES THE SITTING AN ACT HEARS (B24p.24): for a verb whose `proceeds:` cell names the docket's row, the first
    item `docketed` lists for the matter says who arranged its sitting and how hard (`_docket_item`). The arranger is named only where there is a
    rig to work (`rig > 0`): at rig 0 he arranges nothing, and a builder asked to find him would refuse the sitting if he were gone. Any other
    act, and a matter on no docket, has none."""
    if not _heard_on_docket(act.verb):
        return None, 0.0
    items = _world_q.docketed(w, topic)
    if not items:
        return None, 0.0
    rig = float(items[0].get(_world_q.DOCKET_RIG) or 0.0)
    return (items[0].get(_world_q.DOCKET_ARRANGER) if rig > 0 else None), rig


def _hearing(w: Any) -> Optional[tuple]:
    """`(verb, proceeds)` of the hearing a case just opened will have (B24p.24): the verb whose `proceeds:` cell names the docket's row, and
    its last entry's proceeding (`(row dict, form, move, item)`) -- the one that holds for a matter no row was named for (a computed case:
    `_eff_open_case` derives no arrangement), which is what `world_q.proceeding_row` falls through to. `None` where no verb hears a docket.
    It reads no `World`: the tables are fixed at load, so `_docket_hearing` reads them once."""
    return _docket_hearing()


@functools.lru_cache(maxsize=None)
def _docket_hearing() -> Optional[tuple]:
    for verb, row in sorted(VERB_TABLE.items()):
        entries = getattr(row, "proceeds", ())
        # B24.08, B24.10: the hearing an OPENER reads is a SPEECH at the sitting he files for (`speak`: the docket's row, abridged, and the seat's `audience`
        # where the item names none), never the bench's own close (`determine`: the docket's row in the full form, which the bench alone makes): a verb
        # whose docket entry is the full form is the judge's, so it is not the one an opener prices.
        if any(entry[1] == PROCEEDS_DOCKET and entry[2] == "abridged" for entry in entries):
            _when, rid, form, move, item = entries[-1]
            arrangement = ARRANGEMENTS[rid]
            return verb, (in_form(arrangement, form), form, move, item)
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
    first_heard, cited, over = _world_q.hearing_terms(w, act)
    p = believed_proceeding_odds(w, believer, called[0], verb=act.verb, subject=called[1], effort=effort_of(act), proceeds=row, topic=topic,
                                 arranger=arranger, rig=rig, first_heard=first_heard, cited=cited, answered_over=over)
    carried = {DEGREE_LABEL[d] for d, n in DEGREE_ORDINAL.items() if n >= mod.CARRIED}
    held = set(bands)
    return None if p is None else p if held == carried else 1.0 - p if held == set(DEGREE_LABEL.values()) - carried else None
