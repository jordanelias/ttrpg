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
  * `stance` off {-1, +1}; no `pursuits:`; a repeated id.

⚠ A RUNG REFERENT IS NOT CHECKED HERE. A rung exists only once the realm is built, so `rung:` is
validated at seeding (IN-68), where the rung index is. This loader asks only that it be a name.

⚠ LAZY, AS `data/cast.py` IS, AND FOR ITS REASON (`data/__init__.py` records it at length): nothing
here runs at import, so a module that wants only a path cannot `SystemExit` on a bad goals file. To
exercise the path resolution, patch `goals.GOALS_YAML`, clear `goals._CACHE` and re-call `goals()`.
`parse(doc)` is the same check over a document already in hand.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from . import files
from .rosters import (BODY_FACTION, FACTIONS, OFFICES_SEATS, load_yaml, require_member, roster,
                      roster_map)
from ..gaps import Forbidden, Unspecified

GOALS_YAML = files.GOALS_YAML

_LAW = "v9 IN-66 (A-31, ED-IN-0293 (8)) -- a goal is authored in goals.yaml and every name it carries resolves"

# The two signs a stance row carries (`data/cast.py::stance_from_loyalty` returns exactly these).
_STANCE_SIGNS = (-1, 1)


@dataclass(frozen=True)
class Goal:
    """One validated `goals.yaml` row. `object` and `pursuits` are the row's own mappings -- a
    reader does not mutate them. `org_kind` is the one key `org:` carried (`faction`, `body` or
    `seat`) and `org` its name; `derives_from`/`derives_kind` are both `None` for an underived goal."""
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


def _refuse(cls, gid, what: str, needs: str, law: str = _LAW):
    raise cls(f"goal {gid!r}: {what}", f"goals.yaml -- {gid}", needs=needs, law=law)


def _through(gid, check, value):
    """Run an owner's own `Unspecified` check on `value`, re-raised NAMING THE ROW. The membership
    rule stays with its owner (`pursuit`, `affiliation`); only the occasion is added here."""
    try:
        return check(value)
    except Unspecified as exc:
        raise Unspecified(f"goal {gid!r}: {exc.what}", f"goals.yaml -- {gid}",
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


def _pursuits(gid, raw) -> dict:
    """`{pursuit: weight}`, at least one, every name the canonical fifteen's and every weight > 0."""
    from .pursuits import pursuit
    if not isinstance(raw, dict) or not raw:
        _refuse(Unspecified, gid, "carries no `pursuits:`",
                "a mapping of at least one pursuit to a weight > 0 (the goal's lean over the fifteen)")
    out = {}
    for name, w in raw.items():
        _through(gid, pursuit, str(name))
        if isinstance(w, bool) or not isinstance(w, (int, float)) or w <= 0:
            _refuse(Unspecified, gid, f"pursuit {name!r} weighs {w!r}", "a number > 0")
        out[name] = w
    return out


def _stance(gid, row: dict) -> Optional[int]:
    if "stance" not in row:
        return None
    s = row["stance"]
    if isinstance(s, bool) or not isinstance(s, int) or s not in _STANCE_SIGNS:
        _refuse(Unspecified, gid, f"`stance: {s!r}` is not a sign", f"one of {list(_STANCE_SIGNS)}")
    return s


def org_faction(org_kind: str, org: str) -> Optional[str]:
    """The faction an organization belongs to: a faction is its own, a body's is `office_bodies.faction`,
    a seat's is its `faction:` or else its body's. `None` where the tree names none (a seat with
    neither). THE ONE OWNER of the org -> faction step (`_ancestors` and v9 IN-69's `expected` ask it)."""
    if org_kind == "faction":
        return org
    if org_kind == "body":
        return BODY_FACTION.get(org)
    seat = next((s for s in OFFICES_SEATS if s["id"] == org), None) if org_kind == "seat" else None
    if seat is None:
        return None
    return seat.get("faction") or BODY_FACTION.get(seat.get("body"))


def expected(org_kind: str, org: str) -> dict:
    """WHAT AN ORGANIZATION EXPECTS OF ITS MEMBERS, as a pursuit-weight map (v9 IN-69, ED-IN-0293 (10)):
    its faction's role template (`rosters.yaml: role_templates`, through `verbs.ROLE_TEMPLATE_PURSUITS`;
    a body or a seat takes its faction's) plus the sum of the `pursuits:` of every goal of THIS
    organization -- orientation goals included, which mint no Proposition and are known only here. The
    weights add; `data/pursuits.py::alignment` projects, and the projection is linear, so the sum is
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


def parse(doc) -> tuple:
    """`doc` (a parsed `goals.yaml`) as `Goal`s in file order; raise on the first row that breaks the
    schema. `goals: []` is the shipped state and loads to `()`."""
    rows = doc.get("goals") if isinstance(doc, dict) else None
    if not isinstance(rows, list):
        raise Unspecified("goals.yaml has no `goals:` list", "goals.yaml",
                          needs="`goals: []` or a list of goal rows", law=_LAW)
    seats = {s["id"]: s for s in OFFICES_SEATS}
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
        out.append(Goal(
            id=gid, org_kind=org_kind, org=org, text=_text(gid, row, "text"),
            object=_object(gid, row.get("object"), seats, goal_ids), stance=_stance(gid, row),
            pursuits=_pursuits(gid, row.get("pursuits")),
            derives_from=derives_from, derives_kind=derives_kind, source=_text(gid, row, "source")))
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
    return tuple(out)


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


def goal(goal_id: str) -> Optional[Goal]:
    """The goal under `goal_id`, or `None` where the file carries none."""
    return next((g for g in goals() if g.id == goal_id), None)
