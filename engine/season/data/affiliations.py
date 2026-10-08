"""IN-08 H10 -- RELIGIOUS AFFILIATIONS: a name checked, an intensity checked, and the `incompatible`
half-matrix loaded and refused at import (ED-IN-0251 R1/R2).

`Person.conviction` is `{affiliation: intensity}`: a VECTOR over `references/descriptor_registry.yaml:
affiliation_roster`, each intensity an int on that block's `scale:` (the ceiling is full intensity).
Two affiliations can be held at full intensity at once -- that is R2's point, the old Truth pole's two
ends become two holdings -- and whether that strains the person is `rosters.yaml: tables.incompatible`,
read here once. The strain itself is DERIVED where it is asked (`queries/person_q.py::confliction`),
never stored (R1).

⚠ ONE OWNER PER RULE, COMPOSED RATHER THAN COPIED (`CLAUDE.md` §8): membership is
`rosters.require_member` over `rosters.AFFILIATIONS` (the leaf's names through `from_descriptor:`),
the bounds are the leaf's (`engine.substrate.descriptors`, validated by the exporter's `--check`), and
the table's three sparse-table checks are `data/verbs.py::_check_sparse_table`'s. Only the two
checks a HALF-matrix adds over a sparse table live here: no self-pair, and no pair keyed twice.
"""
from __future__ import annotations

from typing import Optional

from engine.substrate.descriptors import AFFILIATION_CEILING, AFFILIATION_FLOOR

from ..gaps import Forbidden, Unspecified
from .rosters import AFFILIATIONS, require_member, table

_ROSTER_LAW = ("references/descriptor_registry.yaml: affiliation_roster single-owns the affiliations "
               "`Person.conviction` is keyed on (IN-08 H10); a name outside it is a holding no table "
               "can read")


def affiliation(name) -> str:
    """`name` if it is a rostered affiliation; refuse naming the roster if it is not."""
    require_member(name, AFFILIATIONS, f"{name!r} is not a rostered affiliation",
                   "descriptor_registry.yaml: affiliation_roster", law=_ROSTER_LAW)
    return name


def conviction_map(raw, where: str = "Person.conviction") -> dict:
    """A validated `{affiliation: intensity}` from `raw` (a mapping, or `None` for none held).

    Every key must be rostered and every value an int inside `[AFFILIATION_FLOOR,
    AFFILIATION_CEILING]` -- a float or a bool is refused, not rounded, because an intensity is a
    held fixed-point int on the ruled 0-5 spine. A zero intensity is DROPPED: an affiliation nobody
    holds is absent, not 0 (the `Person.scar` precedent), so an unaffiliated person's `repr` carries
    `conviction={}` whatever its source wrote. Keys are sorted, so two sources holding the same
    vector produce the same `repr` and the same `World.content_hash`."""
    if raw is None:
        return {}
    if not isinstance(raw, dict):
        raise Unspecified(
            f"{where} is a {type(raw).__name__}, not a mapping of affiliation -> intensity", where,
            needs="`{<affiliation>: <int>}`", law=_ROSTER_LAW)
    out = {}
    for name in sorted(raw, key=str):
        affiliation(name)
        val = raw[name]
        if isinstance(val, bool) or not isinstance(val, int) or not (
                AFFILIATION_FLOOR <= val <= AFFILIATION_CEILING):
            raise Unspecified(
                f"{where}[{name!r}] = {val!r} is not an intensity", where,
                needs=f"an int in [{AFFILIATION_FLOOR}, {AFFILIATION_CEILING}]",
                law="references/descriptor_registry.yaml: affiliation_roster.scale -- the intensity "
                    "spine is the absorbed Truth track's 0-5 (ED-IN-0075), held as an int")
        if val:
            out[name] = val
    return out


def _load_incompatible(cells: Optional[dict] = None) -> frozenset:
    """`tables.incompatible` as the set of pairs that strain: `frozenset({frozenset({a, b}), ...})`.

    `cells` defaults to the shipped table; a caller may pass a planted one to exercise the refusals
    without touching the file. Refused, each because the failure would otherwise be SILENT:
      * an unrostered affiliation on either side -- a pair no person can hold, read by nothing
        (`_check_sparse_table`);
      * a table with no `true` cell -- every confliction is 0 and the mechanism is inert while
        passing every test (`_check_sparse_table`'s all-zero check);
      * a self-pair -- an affiliation cannot strain against itself;
      * a pair keyed under both orders -- a half-matrix keys each pair once, and two cells for one
        pair could disagree with no rule for which wins;
      * a value other than `true`, `false` or `null`."""
    from .verbs import _check_sparse_table
    if cells is None:
        cells = table("incompatible")
    _check_sparse_table(
        "incompatible", cells, AFFILIATIONS, "affiliation", AFFILIATIONS, "affiliation",
        row_law=_ROSTER_LAW, col_law=_ROSTER_LAW)
    seen: dict = {}
    for a, row in cells.items():
        for b, val in row.items():
            if a == b:
                raise Forbidden(
                    f"incompatible[{a}][{b}] pairs an affiliation with itself", "rosters.yaml",
                    needs="drop the cell", law="ED-IN-0251 R1 -- confliction is between two holdings")
            pair = frozenset((a, b))
            if pair in seen:
                raise Forbidden(
                    f"incompatible keys the pair {sorted(pair)} twice", "rosters.yaml",
                    needs="key each unordered pair once, under either order",
                    law="IN-08 H10 -- `incompatible` is a HALF-matrix; two cells for one pair can "
                        "disagree with no rule for which wins")
            if val is not None and not isinstance(val, bool):
                raise Forbidden(
                    f"incompatible[{a}][{b}] = {val!r} is not true, false or null", "rosters.yaml",
                    needs="`true` (strains), `false` (compatible) or `null` (no source)",
                    law="ED-IN-0251 R1 -- the relation is boolean")
            seen[pair] = val
    return frozenset(p for p, v in seen.items() if v is True)


INCOMPATIBLE = _load_incompatible()


# ---------------------------------------------------------------------------
# IN-08 H11 -- THE VERB x AFFILIATION TABLE (J-5's C4, the draft's R-C4), `rosters.yaml:
# tables.affiliation_engagement`. One shared column every held affiliation reads identically
# (R-C4.1), plus per-affiliation SIGN cells where canon names what an affiliation condemns
# (R-C4.2). R-C4.3's content-keyed half is not a cell and is not built (the table's own note).
# ---------------------------------------------------------------------------

_ENGAGEMENT_LAW = ("IN-08 H11 (J-5's C4, R-C4) -- `affiliation_engagement`'s columns are the one "
                   "shared column and the rostered affiliations; its rows are verb-table verbs")


def _load_engagement(cells: Optional[dict] = None, shared: Optional[str] = None) -> tuple:
    """`(shared_column, cells)` from `tables.affiliation_engagement`, checked at import.

    `cells`/`shared` default to the shipped table; a caller may pass planted ones to exercise the
    refusals. Refused, each because the failure would otherwise be SILENT:
      * no `shared_column:`, or one that is also an affiliation's name -- a column read for every
        holding and for one holding at once has no single meaning;
      * a column that is neither, or a verb outside `verb_table.yaml`, or an all-null table
        (`data/verbs.py::_check_sparse_table`, the one owner of those three checks);
      * a per-affiliation cell other than `-1`, `1` or `null` -- those cells are graded "sign only",
        and a magnitude there would be a number nobody chose that a later reader takes for one;
      * a verb carrying both a shared cell and a per-affiliation cell -- no source says how the two
        compose, so neither order of precedence is chosen here;
      * an affiliation spelled like a pursuit -- `Person.scar` keys both, so one name for two
        elements would merge two counts into one."""
    from .rosters import PURSUITS, table_meta
    from .verbs import VERB_TABLE, _check_sparse_table
    if shared is None:
        shared = table_meta("affiliation_engagement").get("shared_column")
    if cells is None:
        cells = table("affiliation_engagement")
    if not shared or shared in AFFILIATIONS:
        raise Unspecified(
            f"affiliation_engagement's shared column is {shared!r}", "rosters.yaml",
            needs="a `shared_column:` naming a column that is not a rostered affiliation",
            law=_ENGAGEMENT_LAW)
    _check_sparse_table(
        "affiliation_engagement", cells, set(AFFILIATIONS) | {shared}, "column",
        set(VERB_TABLE), "verb", row_law=_ENGAGEMENT_LAW,
        col_law="verb_table.yaml -- a cell on a verb nobody can perform is read by nothing")
    shared_verbs = {v for v, val in (cells.get(shared) or {}).items() if val is not None}
    for name, row in cells.items():
        if name == shared:
            continue
        for verb, val in row.items():
            if val is None:
                continue
            if isinstance(val, bool) or val not in (-1, 1):
                raise Forbidden(
                    f"affiliation_engagement[{name}][{verb}] = {val!r} is not a sign",
                    "rosters.yaml", needs="`-1`, `1` or `null`",
                    law="candidate C4 R-C4.2 -- the per-affiliation cells are derived, SIGN ONLY")
            if verb in shared_verbs:
                raise Forbidden(
                    f"`{verb}` carries a shared cell and a cell under {name!r}", "rosters.yaml",
                    needs="one or the other", law=_ENGAGEMENT_LAW + "; no source composes the two")
    clash = sorted(set(AFFILIATIONS) & set(PURSUITS))
    if clash:
        raise Forbidden(
            f"{clash} name both an affiliation and a pursuit", "descriptor_registry.yaml",
            needs="distinct names", law="IN-08 H11 -- `Person.scar` is keyed on both rosters at once")
    return shared, {name: {v: float(x) for v, x in row.items() if x is not None}
                    for name, row in cells.items()}


SHARED_COLUMN, ENGAGEMENT = _load_engagement()


def engagement(verb: str, name: str) -> float:
    """The table's cell for an act of `verb` on a holder of affiliation `name`: that affiliation's
    own cell where it has one, else the shared column's, else `0.0` (no source -- not "compatible").
    The loader refuses a verb in both, so the fallback never hides a cell. Reads the module-level
    binding at call time, so a planted table (`ENGAGEMENT` rebound) is what is read."""
    own = (ENGAGEMENT.get(name) or {}).get(verb)
    if own is not None:
        return own
    return (ENGAGEMENT.get(SHARED_COLUMN) or {}).get(verb, 0.0)
