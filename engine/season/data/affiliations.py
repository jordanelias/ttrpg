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
