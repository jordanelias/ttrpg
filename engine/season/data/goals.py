"""`season.data.goals` -- THE GOALS CARRIER'S ONE LOADER (v9 IN-66, ED-IN-0293 (8)).

`engine/season/goals.yaml` authors the goals of the organizations -- a faction, a body, a seat -- as
rows; `harness/populated.py` will mint each as an OUGHT Proposition at world-gen (IN-68, the reader).
This module READS and VALIDATES; it translates nothing and guesses nothing. Every organization, kind
and referent a row names is resolved against the one owner of that fact, and a row that does not
resolve is REFUSED by name -- never skipped, never coerced to a plausible neighbour (`data/cast.py`'s
line, `data/pursuits.py` one layer down):

  * organization: a faction on `rosters.yaml: factions`, a body on `office_bodies.faction`, a seat on
    `offices.yaml: seats` (`rosters.OFFICES_SEATS`);
  * kind: a member of `goal_object_kinds`; a derivation kind a member of `goal_derivations`;
  * referent: a case id (`data/cast.py::row`), a seat id, an affiliation
    (`data/affiliations.py::affiliation`), a deed kind (`data/verbs.py::DEED_KINDS`), a goal id;
  * pursuit: `data/pursuits.py::pursuit`, the one owner of the canonical fifteen;
  * `derives`: dangling, cyclic, or from a goal whose organization is not an ANCESTOR of the row's
    (seat -> body -> faction; a faction goal derives from a faction goal -- the oath, not this data,
    makes one faction subordinate to another, A-30);
  * `stance` off {-1, +1}; no `pursuits:`; a repeated id;
  * CL-THRUST B2.1: an optional `axis:`, a member of `thrust_axes` (`rosters.yaml`), refused on an
    `orientation` row -- it mints no Proposition, so no one can be committed to it;
  * CL-THRUST B2.2: an optional top-level `goal_stages:` list (a missing key reads as `[]`, the shipped
    state), each row `{id, for, stages}` -- `for:` the goals it climbs (never an `orientation` goal, never
    one claimed by a second row), `stages:` at least two in order, each `{id, term, predicate, pursuits}`:
    `term` a `goal_stage_terms` member that never decreases along the row, `predicate` a
    `requires_typed` cell `data/requires.py::build_typed_requires` accepts (its `SystemExit` is wrapped
    into this loader's own refusal) that asks no `WORLD_ONLY_STEMS` and no `LEDGER_DERIVED_STEMS` stem,
    because the stage is read PERSON-SIDE off claims in the ledger, and `pursuits` through `data/pursuits.py::pursuit`. A key outside those is refused, not
    dropped. A row is attached to the goals it is `for:` (`Goal.stages`); nothing here reads it yet.

⚠ A RUNG REFERENT IS NOT CHECKED HERE. A rung exists only once the realm is built, so `rung:` is
validated at seeding (IN-68), where the rung index is. This loader asks only that it be a name.

⚠ LAZY, AS `data/cast.py` IS, AND FOR ITS REASON (`data/__init__.py` records it at length): nothing
here runs at import, so a module that wants only a path cannot `SystemExit` on a bad goals file. To
exercise the path resolution, patch `goals.GOALS_YAML`, clear `goals._CACHE` and re-call `goals()`.
`parse(doc)` is the same check over a document already in hand.
"""

from __future__ import annotations

import contextlib
from dataclasses import dataclass, replace
from typing import Optional

from . import files
from .rosters import (AFFILIATIONS, BODY_FACTION, FACTIONS, SEAT_ROW_BY_ID, load_yaml, office_faction,
                      require_member, roster, roster_map)
from ..gaps import Forbidden, Unspecified

GOALS_YAML = files.GOALS_YAML

_LAW = "v9 IN-66 (A-31, ED-IN-0293 (8)) -- a goal is authored in goals.yaml and every name it carries resolves"
_THRUST_LAW = ("CL-THRUST B2.1 -- a goal's axis is a member of the closed `thrust_axes` roster, and only a "
               "goal that mints a Proposition can be one a person is committed to")
_STAGES_LAW = ("CL-THRUST B2.2 -- a goal's stages are authored in goals.yaml and every name they carry "
               "resolves; a stage nobody can read, or that no one can be committed to, is refused, not carried")

# The top-level key (and the label a refusal names its row by) of the stage rows. NOT `ladders`: that word
# already means `LarderInput.ladders` and the degree ladder in this package.
_STAGES_KEY = "goal_stages"

# The two signs a stance row carries (`data/cast.py::stance_from_loyalty` returns exactly these).
_STANCE_SIGNS = (-1, 1)


@dataclass(frozen=True)
class Stage:
    """One stage of a `goal_stages` row (CL-THRUST B2.2). `term` is a `goal_stage_terms` member;
    `predicate` the `TypedRequires` `data/requires.py::build_typed_requires` built from the row's cell
    (read PERSON-SIDE: it asks no `WORLD_ONLY_STEMS` stem); `pursuits` the stage's own `{pursuit: weight}`."""
    id: str
    term: str
    predicate: object
    pursuits: dict


@dataclass(frozen=True)
class GoalStages:
    """One `goal_stages` row: `stages` in the order authored (at least two, terms never decreasing) and
    `for_goals` the ids of the goals it climbs for -- each goal is in at most one row."""
    id: str
    for_goals: tuple
    stages: tuple


@dataclass(frozen=True)
class Goal:
    """One validated `goals.yaml` row. `object` and `pursuits` are the row's own mappings -- a
    reader does not mutate them. `org_kind` is the one key `org:` carried (`faction`, `body` or
    `seat`) and `org` its name; `derives_from`/`derives_kind` are both `None` for an underived goal.
    `axis` is the row's optional `thrust_axes` member and `stages` the `goal_stages` row that names this
    goal in its `for:` (CL-THRUST B2.1/B2.2); both `None` for every shipped row."""
    id: str
    org_kind: str
    org: str
    text: str
    object: dict
    stance: Optional[int]
    pursuits: dict
    derives_from: Optional[str]
    derives_kind: Optional[str]
    source: str
    axis: Optional[str] = None
    stages: Optional[GoalStages] = None


def _where(gid, label: str) -> str:
    return f"goals.yaml -- {gid}" if label == "goal" else f"goals.yaml -- {label} {gid}"


def _refuse(cls, gid, what: str, needs: str, law: str = _LAW, label: str = "goal"):
    raise cls(f"{label} {gid!r}: {what}", _where(gid, label), needs=needs, law=law)


def _through(gid, check, value, label: str = "goal"):
    """Run an owner's own `Unspecified` check on `value`, re-raised NAMING THE ROW. The membership
    rule stays with its owner (`pursuit`, `affiliation`); only the occasion is added here."""
    try:
        return check(value)
    except Unspecified as exc:
        raise Unspecified(f"{label} {gid!r}: {exc.what}", _where(gid, label),
                          needs=exc.needs, law=exc.law) from exc


def _in(value, owner) -> bool:
    """`value` is a string the `owner` collection holds. A list or a number a hand-edited row put
    where a name belongs is not a member, rather than an unhashable `TypeError` naming nobody."""
    return isinstance(value, str) and value in owner


def _text(gid, row: dict, key: str) -> str:
    v = row.get(key)
    if not isinstance(v, str) or not v.strip():
        _refuse(Unspecified, gid, f"carries no `{key}:` string", f"a non-empty `{key}:`")
    return v


def _org(gid, raw, seats: dict) -> tuple:
    """`(org_kind, name)` from `org:`, refused unless it names exactly one real organization."""
    if not isinstance(raw, dict) or len(raw) != 1:
        _refuse(Unspecified, gid, f"`org:` is {raw!r}, not exactly one organization",
                "`org: {faction: <name>}`, `{body: <name>}` or `{seat: <seat id>}`")
    (kind, name), = raw.items()
    if kind == "faction":
        known = _in(name, FACTIONS)
    elif kind == "body":
        known = _in(name, BODY_FACTION)
    elif kind == "seat":
        known = _in(name, seats)
    else:
        _refuse(Unspecified, gid, f"org kind {kind!r} is not an organization",
                "one of faction, body, seat")
    if not known:
        _refuse(Unspecified, gid, f"{kind} {name!r} is not an organization of that kind",
                f"a {kind} the tree names (rosters.yaml: factions, office_bodies; offices.yaml: seats)")
    return kind, name


def _object(gid, raw, seats: dict, goal_ids: set) -> dict:
    """The row's `object:`, its kind rostered and its referent fields resolved."""
    from . import cast
    from .affiliations import affiliation
    from .verbs import DEED_KINDS
    if not isinstance(raw, dict):
        _refuse(Unspecified, gid, f"`object:` is {raw!r}, not a mapping", "`object: {kind: ..., ...}`")
    kind = str(raw.get("kind"))
    require_member(kind, roster("goal_object_kinds"), f"goal {gid!r}: object kind {kind!r} is not rostered",
                   f"goals.yaml -- {gid}", law=_LAW)
    if kind == "person":
        if cast.row(str(raw.get("case"))) is None:
            _refuse(Unspecified, gid, f"`case: {raw.get('case')!r}` is no row of the cast registry",
                    "a case id of references/npc_registry.yaml")
    elif kind == "seat_holders":
        named = raw.get("seats")
        if not isinstance(named, list) or not named:
            _refuse(Unspecified, gid, "`seat_holders` names no `seats:`", "a non-empty list of seat ids")
        for sid in named:
            if not _in(sid, seats):
                _refuse(Unspecified, gid, f"seat {sid!r} is not on offices.yaml",
                        "a seat id of offices.yaml: seats")
    elif kind == "rung":
        if not isinstance(raw.get("rung"), str) or not raw["rung"].strip():
            _refuse(Unspecified, gid, "`rung` names no `rung:` id",
                    "a rung id (checked at seeding, IN-68, once rungs exist)")
    elif kind == "deed_doers":
        forms = roster_map("goal_object_kinds", "forms")[kind]
        given = [f for f in forms if f in raw]
        if len(given) != 1:
            _refuse(Unspecified, gid, f"`deed_doers` names {len(given)} forms, not one",
                    f"exactly one of {list(forms)}")
        form = given[0]
        if form == "against":
            if not _in(raw[form], goal_ids):
                _refuse(Unspecified, gid, f"`against: {raw[form]!r}` is no goal of this file",
                        "the id of a goal row")
        elif form == "engaging":
            if not _in(raw[form], AFFILIATIONS):
                _refuse(Unspecified, gid, f"`engaging: {raw[form]!r}` is no affiliation",
                        "the name of a rostered affiliation")
            _through(gid, affiliation, raw[form])
        else:
            deeds = raw[form]
            if not isinstance(deeds, list) or not deeds:
                _refuse(Unspecified, gid, "`kinds:` names no deed kind", "a non-empty list of deed kinds")
            for d in deeds:
                if not _in(d, DEED_KINDS):
                    _refuse(Unspecified, gid, f"deed kind {d!r} is emitted by no verb row, or only on refusal",
                            "a member of data/verbs.py::DEED_KINDS")
    return dict(raw)


def _pursuits(gid, raw, law: str = _LAW, label: str = "goal") -> dict:
    """`{pursuit: weight}`, at least one, every name the canonical fifteen's and every weight > 0. A stage's
    `pursuits:` is read by this same check (`law` and `label` name the occasion), never a second one."""
    from .pursuits import pursuit
    if not isinstance(raw, dict) or not raw:
        _refuse(Unspecified, gid, "carries no `pursuits:`",
                "a mapping of at least one pursuit to a weight > 0 (the goal's lean over the fifteen)",
                law, label)
    out = {}
    for name, w in raw.items():
        _through(gid, pursuit, str(name), label)
        if isinstance(w, bool) or not isinstance(w, (int, float)) or not (w > 0) or w == float("inf"):
            _refuse(Unspecified, gid, f"pursuit {name!r} weighs {w!r}", "a finite number > 0", law, label)
        out[name] = w
    return out


def _is_orientation(obj: dict) -> bool:
    """The row mints NO Proposition (`goal_object_kinds`' note; `harness/populated.py::seed_goals` skips it),
    so no one can be committed to it."""
    return obj.get("kind") == "orientation"


def _thrust_axes() -> frozenset:
    """The `thrust_axes` roster, with its `opposes:` map checked against it: a pole that is not a member
    would be an axis a row could never carry, and the map would pair it with nothing. Read on every parse,
    so a defective roster refuses at the one entry rather than at the first row that names an axis."""
    axes = roster("thrust_axes")
    for axis, pole in roster_map("thrust_axes", "opposes").items():
        for named in (axis, pole):
            if not _in(named, axes):
                raise Unspecified(
                    f"rosters.yaml: thrust_axes.opposes pairs {axis!r} with {pole!r}, and {named!r} is "
                    f"not a `values:` member", "rosters.yaml -- thrust_axes",
                    needs="every axis and pole `opposes:` names is a `values:` member (add it, or drop the pair)",
                    law=_THRUST_LAW)
    return axes


def _axis(gid, row: dict, obj: dict, axes: frozenset) -> Optional[str]:
    """The row's optional `axis:`: a `thrust_axes` member, and never on an `orientation` row (it mints no
    Proposition, so nobody can be committed to it -- a thrust about nobody). `None` where the row has none."""
    if "axis" not in row:
        return None
    axis = str(row["axis"])
    require_member(axis, axes, f"goal {gid!r}: axis {axis!r} is not rostered", f"goals.yaml -- {gid}",
                   law=_THRUST_LAW)
    if _is_orientation(obj):
        _refuse(Forbidden, gid, f"an `orientation` goal carries `axis: {axis}`",
                "drop the `axis:`, or give the row an object kind that mints a Proposition", _THRUST_LAW)
    return axis


def _stance(gid, row: dict) -> Optional[int]:
    if "stance" not in row:
        return None
    s = row["stance"]
    if isinstance(s, bool) or not isinstance(s, int) or s not in _STANCE_SIGNS:
        _refuse(Unspecified, gid, f"`stance: {s!r}` is not a sign", f"one of {list(_STANCE_SIGNS)}")
    return s


def org_faction(org_kind: str, org: str) -> Optional[str]:
    """The faction an organization belongs to: a faction is its own, a body's is `office_bodies.faction`,
    a seat's is `rosters.office_faction(body, faction)`, the rule `Office.__post_init__` runs (body-first,
    a disagreement refuses). `None` where the tree names none (a seat with neither). The one caller of
    that rule on the data side: `_ancestors` and v9 IN-69's `expected` ask THIS, not a second walk."""
    if org_kind == "faction":
        return org
    if org_kind == "body":
        return BODY_FACTION.get(org)
    seat = SEAT_ROW_BY_ID.get(org) if org_kind == "seat" else None
    if seat is None:
        return None
    if seat.get("body") is None and seat.get("faction") is None:
        return None
    return office_faction(seat.get("body"), seat.get("faction"))


def expected(org_kind: str, org: str) -> dict:
    """WHAT AN ORGANIZATION EXPECTS OF ITS MEMBERS, as a pursuit-weight map (v9 IN-69, ED-IN-0293 (10)):
    its faction's role template (`rosters.yaml: role_templates`, through `verbs.ROLE_TEMPLATE_PURSUITS`;
    a body or a seat takes its faction's) plus the sum of the `pursuits:` of every goal of THIS
    organization -- orientation goals included, which mint no Proposition and are known only here. The
    weights add; `data/pursuits.py::pursuit_cosine` projects, and the projection is linear, so the sum is
    the same whether taken before or after. `{}` for a faction with no template and no goal."""
    from .verbs import ROLE_TEMPLATE_PURSUITS
    from .rosters import ROLE_TEMPLATE_OF
    out: dict = {}
    template = ROLE_TEMPLATE_OF.get(str(org_faction(org_kind, org) or ""))
    for name, w in (ROLE_TEMPLATE_PURSUITS.get(template) or {}).items():
        out[name] = out.get(name, 0.0) + float(w)
    for g in goals():
        if (g.org_kind, g.org) == (org_kind, org):
            for name, w in g.pursuits.items():
                out[name] = out.get(name, 0.0) + float(w)
    return out


def _ancestors(g: Goal, seats: dict) -> set:
    """The `(org_kind, name)` pairs above `g`'s organization: a seat's body and faction, a body's
    faction. A faction has none (a faction goal derives from a faction goal, A-30)."""
    if g.org_kind == "body":
        return {("faction", org_faction("body", g.org))}
    if g.org_kind != "seat":
        return set()
    above = set()
    if seats[g.org].get("body"):
        above.add(("body", seats[g.org]["body"]))
    fac = org_faction("seat", g.org)
    if fac:
        above.add(("faction", fac))
    return above


def _predicate(sid: str, cell):
    """A stage's `predicate:` as the `TypedRequires` the typed-requires builder makes of it. The builder
    refuses by `SystemExit` naming `verb_table.yaml` and a verb; that is wrapped here into THIS loader's
    own refusal naming the stage (its message is kept, whole). Refused too: a cell that builds to nothing
    (`none`), and any `WORLD_ONLY_STEMS` stem -- the stage is read person-side, where `with`, `audience`
    and the own-state stems always read UNKNOWN, so a stage over one could never be met. Any
    `LEDGER_DERIVED_STEMS` stem (`claim.held`, the `own_ledger` form) is refused for the same reason:
    `LedgerReader` answers a stem only from a claim whose predicate IS that stem and WITNESS deposits no
    `claim.held` claim, so it reads UNKNOWN for every person (found at the B10-05 close)."""
    from .requires import LEDGER_DERIVED_STEMS, WORLD_ONLY_STEMS, build_typed_requires
    try:
        req = build_typed_requires(sid, cell)
    except SystemExit as exc:
        _refuse(Unspecified, sid, f"`predicate:` is refused by the typed-requires builder: {exc}",
                "a cell in the `requires_typed` grammar (`of: subject`)", _STAGES_LAW, _STAGES_KEY)
    if req is None:
        _refuse(Unspecified, sid, f"`predicate:` is {cell!r}, which builds to no requirement",
                "a cell in the `requires_typed` grammar (`of: subject`)", _STAGES_LAW, _STAGES_KEY)
    world_only = sorted(set(req.stems()) & WORLD_ONLY_STEMS)
    if world_only:
        _refuse(Forbidden, sid, f"`predicate:` asks {world_only}, which only the world answers",
                "a cell over stems a person's own ledger can answer (not `WORLD_ONLY_STEMS`)",
                _STAGES_LAW, _STAGES_KEY)
    ledger_derived = sorted(set(req.stems()) & LEDGER_DERIVED_STEMS)
    if ledger_derived:
        _refuse(Forbidden, sid, f"`predicate:` asks {ledger_derived}, which no ledger claim answers person-side",
                "a cell over stems a claim in a person's ledger answers (not `LEDGER_DERIVED_STEMS`)",
                _STAGES_LAW, _STAGES_KEY)
    return req


def _stages(rid: str, raw) -> tuple:
    """A row's `stages:` as `Stage`s, in order: at least two, each `{id, term, predicate, pursuits}`, no
    key beyond those, terms along `goal_stage_terms`' order never decreasing, and no stage id twice."""
    if not isinstance(raw, list) or len(raw) < 2:
        _refuse(Unspecified, rid, f"`stages:` is {raw!r}, not a list of at least two stages",
                "an ordered list of two or more stages", _STAGES_LAW, _STAGES_KEY)
    terms = roster("goal_stage_terms", ordered=True)
    out, seen, last = [], set(), -1
    for i, s in enumerate(raw):
        if not isinstance(s, dict) or not isinstance(s.get("id"), str) or not s["id"].strip():
            _refuse(Unspecified, f"{rid}[{i}]", f"stage {i} carries no `id:` string", "a stage id",
                    _STAGES_LAW, _STAGES_KEY)
        sid = f"{rid}/{s['id']}"
        left = dict(s)
        left.pop("id")
        term, cell, pursuits = left.pop("term", None), left.pop("predicate", None), left.pop("pursuits", None)
        if left:
            _refuse(Forbidden, sid, f"carries {sorted(map(str, left))}, which a stage does not read",
                    "a stage is its id, term, predicate and pursuits and nothing else (a key the schema does "
                    "not read is refused, not dropped)", _STAGES_LAW, _STAGES_KEY)
        if s["id"] in seen:
            _refuse(Forbidden, sid, "more than one stage of the row carries this id", "one stage per `id`",
                    _STAGES_LAW, _STAGES_KEY)
        seen.add(s["id"])
        require_member(term, terms, f"{_STAGES_KEY} {sid!r}: term {term!r} is not rostered",
                       _where(sid, _STAGES_KEY), law=_STAGES_LAW)
        if terms.index(term) < last:
            _refuse(Forbidden, sid, f"term {term!r} is nearer than the stage before it",
                    f"terms that never decrease along {list(terms)}", _STAGES_LAW, _STAGES_KEY)
        last = terms.index(term)
        out.append(Stage(s["id"], term, _predicate(sid, cell),
                         _pursuits(sid, pursuits, _STAGES_LAW, _STAGES_KEY)))
    return tuple(out)


def _goal_stages(doc: dict, goals: tuple) -> tuple:
    """`goals`, each carrying the `goal_stages` row that names it in `for:` (`Goal.stages`). A missing key
    is `[]` and returns `goals` untouched: the shipped state. A row is refused for a repeated id; a `for:`
    that is empty, names no goal of this file, names an `orientation` goal, or names a goal another row
    already claims (one row per goal); `stages:` that fail `_stages`; or a key outside `{id, for, stages}`."""
    if _STAGES_KEY not in doc:
        return goals
    raw = doc[_STAGES_KEY]
    if not isinstance(raw, list):
        raise Unspecified(f"goals.yaml `{_STAGES_KEY}:` is {raw!r}, not a list", f"goals.yaml -- {_STAGES_KEY}",
                          needs=f"`{_STAGES_KEY}: []`, a list of rows, or no such key", law=_STAGES_LAW)
    ids = []
    for i, row in enumerate(raw):
        if not isinstance(row, dict) or not isinstance(row.get("id"), str) or not row["id"].strip():
            _refuse(Unspecified, f"[{i}]", f"row {i} carries no `id:` string", "a unique id",
                    _STAGES_LAW, _STAGES_KEY)
        ids.append(row["id"])
    for rid in ids:
        if ids.count(rid) > 1:
            _refuse(Forbidden, rid, "more than one row carries this id", "one row per `id`",
                    _STAGES_LAW, _STAGES_KEY)
    by_id = {g.id: g for g in goals}
    claimed, built = {}, []
    for row in raw:
        rid = row["id"]
        left = dict(row)
        left.pop("id")
        for_ids, stages = left.pop("for", None), left.pop("stages", None)
        if left:
            _refuse(Forbidden, rid, f"carries {sorted(map(str, left))}, which a row does not read",
                    "a row is its id, `for:` and `stages:` and nothing else (a key the schema does not "
                    "read is refused, not dropped)", _STAGES_LAW, _STAGES_KEY)
        if not isinstance(for_ids, list) or not for_ids:
            _refuse(Unspecified, rid, f"`for:` is {for_ids!r}, not a non-empty list of goal ids",
                    "the ids of the goals this row climbs for", _STAGES_LAW, _STAGES_KEY)
        for gid in for_ids:
            if not _in(gid, by_id):
                _refuse(Unspecified, rid, f"`for:` names {gid!r}, which is no goal of this file",
                        "the id of a goal row", _STAGES_LAW, _STAGES_KEY)
            if _is_orientation(by_id[gid].object):
                _refuse(Forbidden, rid, f"`for:` names {gid!r}, an `orientation` goal: it mints no "
                        f"Proposition, so no one can be committed to it", "a goal that mints a Proposition",
                        _STAGES_LAW, _STAGES_KEY)
            if gid in claimed:
                _refuse(Forbidden, rid, f"`for:` names {gid!r}, which row {claimed[gid]!r} already claims",
                        "one row per goal", _STAGES_LAW, _STAGES_KEY)
            claimed[gid] = rid
        built.append(GoalStages(rid, tuple(for_ids), _stages(rid, stages)))
    by_row = {gid: row for row in built for gid in row.for_goals}
    return tuple(replace(g, stages=by_row[g.id]) if g.id in by_row else g for g in goals)


def parse(doc) -> tuple:
    """`doc` (a parsed `goals.yaml`) as `Goal`s in file order; raise on the first row that breaks the
    schema. `goals: []` is the shipped state and loads to `()`; an absent `goal_stages:` is `[]`."""
    rows = doc.get("goals") if isinstance(doc, dict) else None
    if not isinstance(rows, list):
        raise Unspecified("goals.yaml has no `goals:` list", "goals.yaml",
                          needs="`goals: []` or a list of goal rows", law=_LAW)
    stray = sorted(str(k) for k in doc if k not in ("goals", _STAGES_KEY))
    if stray:
        raise Forbidden(f"goals.yaml carries the top-level key(s) {stray}", "goals.yaml",
                        needs=f"`goals:` and `{_STAGES_KEY}:` only (the stage rows are `{_STAGES_KEY}`, "
                              f"not `ladders`)", law=_STAGES_LAW)
    seats = SEAT_ROW_BY_ID
    axes = _thrust_axes()
    ids = []
    for i, row in enumerate(rows):
        if not isinstance(row, dict) or not isinstance(row.get("id"), str) or not row["id"].strip():
            _refuse(Unspecified, f"goals[{i}]", f"row {i} carries no `id:` string", "a unique id")
        ids.append(row["id"])
    for gid in ids:
        if ids.count(gid) > 1:
            _refuse(Forbidden, gid, "more than one row carries this id",
                    "one row per `id` (it is the Proposition id the row mints)")
    goal_ids = set(ids)
    out = []
    for row in rows:
        gid = row["id"]
        org_kind, org = _org(gid, row.get("org"), seats)
        derives_from = derives_kind = None
        if "derives" in row:
            d = row["derives"]
            if not isinstance(d, dict):
                _refuse(Unspecified, gid, f"`derives:` is {d!r}, not a mapping",
                        "`derives: {from: <goal id>, kind: <goal_derivations member>}`")
            derives_from, derives_kind = d.get("from"), str(d.get("kind"))
            require_member(derives_kind, roster("goal_derivations"),
                           f"goal {gid!r}: derivation kind {derives_kind!r} is not rostered",
                           f"goals.yaml -- {gid}", law=_LAW)
            if not _in(derives_from, goal_ids):
                _refuse(Unspecified, gid, f"`derives.from: {derives_from!r}` is no goal of this file",
                        "the id of a goal row")
        text = _text(gid, row, "text")
        obj = _object(gid, row.get("object"), seats, goal_ids)
        stance, pursuits = _stance(gid, row), _pursuits(gid, row.get("pursuits"))
        source = _text(gid, row, "source")
        out.append(Goal(
            id=gid, org_kind=org_kind, org=org, text=text, object=obj, stance=stance, pursuits=pursuits,
            derives_from=derives_from, derives_kind=derives_kind, source=source,
            axis=_axis(gid, row, obj, axes)))
    by_id = {g.id: g for g in out}
    for g in out:
        seen, cur = {g.id}, g
        while cur.derives_from is not None:
            if cur.derives_from in seen:
                _refuse(Forbidden, g.id, f"its `derives` chain returns to {cur.derives_from!r}",
                        "an acyclic chain of derivations")
            seen.add(cur.derives_from)
            cur = by_id[cur.derives_from]
        if g.derives_from is None:
            continue
        parent = by_id[g.derives_from]
        ok = ((parent.org_kind, parent.org) in _ancestors(g, seats)
              if g.org_kind != "faction" else parent.org_kind == "faction")
        if not ok:
            _refuse(Forbidden, g.id,
                    f"{g.org_kind} {g.org!r} derives from {parent.org_kind} {parent.org!r}, "
                    f"which is not above it",
                    "a parent goal of an ancestor organization (seat -> body -> faction); a "
                    "faction goal derives from a faction goal")
    return _goal_stages(doc, tuple(out))


_CACHE: Optional[tuple] = None


def goals() -> tuple:
    """Every goal, in file order, read once and kept.

    Raises `Unspecified` rather than returning `()` if the file is absent: a world built from a
    silently missing goals file is a world with no goals wearing a successful load's clothes."""
    global _CACHE
    if _CACHE is None:
        try:
            text = GOALS_YAML.read_text(encoding="utf-8")
        except FileNotFoundError as exc:
            raise Unspecified(
                f"the goals file at {GOALS_YAML}", "engine/season/goals.yaml",
                needs="`goals: []` or a list of goal rows",
                law="a goal set read from nothing cannot be told from a goal set authored empty") from exc
        _CACHE = parse(load_yaml(text) or {})
    return _CACHE


def load() -> tuple:
    """`data.load_all`'s handle on this loader: read the file now, so a malformed goal refuses at the one
    entry instead of at the first world that seeds goals. The same cache `goals()` fills."""
    return goals()


@contextlib.contextmanager
def rows_replaced(rows: tuple = ()):
    """The goals the reader sees, swapped for `rows` for the block and restored after: the one place that
    touches the cache (`harness/decision_spread.no_goals` reads the FILE as empty through it)."""
    global _CACHE
    saved, _CACHE = _CACHE, rows
    try:
        yield
    finally:
        _CACHE = saved


def goal(goal_id: str) -> Optional[Goal]:
    """The goal under `goal_id`, or `None` where the file carries none."""
    return next((g for g in goals() if g.id == goal_id), None)
