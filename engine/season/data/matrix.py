"""`season.data.matrix` -- S23/S30's write matrix, extracted from `shape.py` (step 2 of the
decomposition, a PURE MOVE: no behaviour changed, only where the code lives).

Owns the six-step loop's `Step`/`WriteClass` enums, the STEP -> WRITE CLASS relation, and the
`(kind, field)` table loaded from `write_matrix.yaml` that says which step may write which record
field, and how (S30's own rule: ANY UNMARKED CELL IS A WRITE-CLASS VIOLATION).

⚠ TWO THINGS THIS MODULE DELIBERATELY DOES NOT OWN, BOTH ADJUDICATED AT THE SAME TIME AS THE MOVE:
`MATRIX_REFUSAL_LAW` stays in `shape.py`, with its only reader -- the gate in `World`. It is a
loop over a fix, not a definition, and moving it here would invite editing it as one.
`rows_without_a_producer` also stays in `shape.py`: it reads `VERB_TABLE`, which belongs to the
verb table this module does not load, and moves with it in a later step.

`load_yaml` -- the one YAML reader every loader in this package shares -- lives in
`season.data.rosters`, not here, which is why `season/data/__init__.py` loads `rosters` before
this module: `_load_write_matrix` below imports it from there rather than owning a second copy.
"""

from __future__ import annotations

import enum
from dataclasses import dataclass
from typing import Optional

from . import files
from ..gaps import Unspecified
from .rosters import load_yaml


# ===========================================================================
# S23 -- THE SIX STEPS; S30 -- THE FOUR WRITE CLASSES
# ===========================================================================

class Step(enum.Enum):
    CALENDAR = "CALENDAR"
    MATTER = "MATTER"
    DELIBERATE = "DELIBERATE"
    RESOLVE = "RESOLVE"
    WITNESS = "WITNESS"
    CENSUS = "CENSUS"


class WriteClass(enum.Enum):
    CALENDAR = "CALENDAR"
    MATTER = "MATTER"
    ACTS = "ACTS"
    INTERIOR = "INTERIOR"


# THE STEP -> WRITE CLASS MAP, and it is the single owner of that relation. CENSUS writes in the
# MATTER class (§30's reconciliation is a world write), DELIBERATE in ACTS -- it returns an act
# array and writes nothing else.
# roster-exempt: MECHANISM, and the distinction is the one rosters.yaml states. The STEP NAMES
# are `Step`'s own members — the six-step loop is the engine's shape, not the game's vocabulary —
# and this maps each to its write class, which is a RELATION the code owns. Moving it would invite
# someone to edit how the engine works while believing they were editing the game.
_STEP_CLASS = {
    "CALENDAR": WriteClass.CALENDAR,
    "MATTER": WriteClass.MATTER,
    "DELIBERATE": WriteClass.ACTS,
    "RESOLVE": WriteClass.ACTS,
    "WITNESS": WriteClass.INTERIOR,
    "CENSUS": WriteClass.MATTER,
}


# ===========================================================================
# PART D, LOADED FROM DATA -- W2.
#
# WHAT WAS HERE, AND WHY IT WENT. Six hand-maintained structures -- `WRITE_MATRIX`,
# `WRITE_CLASS_OF`, `PARTITION`, `PARTITION_ASSUMED`, `MATRIX_FIELD_OF` and `PARTITION_MISSING`
# -- plus a derivation loop that reconstructed the Partition from the matrix at import time.
# Every one of them was keyed on a THING (`stance`, `condition`, `Tenure`) because #353 §30's
# matrix is, and that keying IS defect `D1`: `(Person, convictions)` rode on `stance`'s row, so a
# real gap silently became a PASS. `MATRIX_FIELD_OF` existed only to paper over the mismatch, and
# it was a hand-written map of which fields were allowed to ride on which rows -- i.e. the defect,
# written down.
#
# `write_matrix.yaml` is keyed on `(kind, field)`, which is how §30's own rule is stated. The
# rule -- ANY UNMARKED CELL IS A WRITE-CLASS VIOLATION -- is applicable now rather than
# aspirational, and there is nothing left to ride on.
#
# THE THREE `PARTITION_ASSUMED` ROWS ARE GONE AS ASSUMPTIONS. `(Person, claim_ledger)`,
# `(Date, fired)` and `(DocketItem, matter)` were instrument assumptions because the old
# two-clause derivation could not reach them. §D2's `DR-3` states them, so they are rows with a
# provenance now and `ASSUMPTIONS.md` regenerates with ZERO assumed Partition rows -- which is
# W2's own proof, and it is a REDUCTION in what the instrument supplies, not an addition.
# ===========================================================================

WRITE_MATRIX_YAML = files.WRITE_MATRIX_YAML

# A step determines its write class exactly. ONE OWNER: the YAML's `class:` column carries V2's
# own string and the loader CHECKS it against this map rather than trusting either alone.
STEP_CLASS: dict = {Step[k]: v for k, v in _STEP_CLASS.items()}

# roster-exempt: MECHANISM. The abbreviations `write_matrix.yaml`'s `steps:` column uses, mapped
# to `Step`'s names. This is the FILE FORMAT, not a definition the game resolves from.
_STEP_OF = {"CAL": "CALENDAR", "MAT": "MATTER", "DEL": "DELIBERATE",
            "RES": "RESOLVE", "WIT": "WITNESS", "CEN": "CENSUS"}


@dataclass(frozen=True)
class MatrixRow:
    kind: str
    field: str
    steps: frozenset
    social: Optional[bool]      # None == `n/a`
    by: str
    emits: tuple

    def write_class(self, step: "Step") -> "WriteClass":
        return STEP_CLASS[step]


def _load_write_matrix() -> dict:
    import yaml as _yaml
    if not WRITE_MATRIX_YAML.exists():
        raise SystemExit(f"write_matrix.yaml not found at {WRITE_MATRIX_YAML}")
    doc = load_yaml(WRITE_MATRIX_YAML.read_text())
    out = {}
    for r in doc["rows"]:
        steps = frozenset(Step[_STEP_OF[s]] for s in r["steps"])
        # roster-exempt: MECHANISM. This parses §G4's three `social:` values into Python; it
        # is the file format, not a definition the game resolves from.
        social = {"true": True, "false": False, "n/a": None}[r["social"].strip()]
        # THE CROSS-CHECK. `class:` is V2's prose; the derivation is this file's. If they
        # disagree, one of them is wrong and neither may be trusted silently.
        derived = "/".join(sorted({STEP_CLASS[st].value for st in steps},
                                  key=lambda v: [s.value for s in Step].index(v)
                                  # [JUSTIFIED: a SORT SENTINEL, not a game value -- it orders a class outside `Step` last, and any value above len(Step) is equivalent]
                                  if v in [s.value for s in Step] else 99))
        stated = r["class"].strip()
        if steps and stated != "—":
            want = set(stated.split("/"))
            got = {STEP_CLASS[st].value for st in steps}
            if want != got:
                raise SystemExit(
                    f"write_matrix.yaml ({r['kind']}, {r['field']}): `class:` says {stated!r} and "
                    f"the step->class derivation gives {sorted(got)}. One is wrong; fix the row "
                    "or fix STEP_CLASS -- do not let them disagree.")
        emits = tuple(e.strip(" `") for e in r["emits"].split("·") if e.strip(" `—"))
        key = (r["kind"], r["field"])
        if key in out:
            # A DUPLICATE ROW SILENTLY OVERWROTE ITS TWIN and the only symptom was two counts
            # disagreeing -- 41 rows in the file, 40 in the map. Which of the two survives is
            # dict-insertion order, so the gate's behaviour would depend on where in the file
            # someone happened to add a row. That is precisely the class of defect this register
            # exists to end.
            raise SystemExit(
                f"write_matrix.yaml: ({r['kind']}, {r['field']}) appears more than once. "
                "One row per (kind, field) -- a duplicate makes the gate's behaviour depend on "
                "file order.")
        out[key] = MatrixRow(
            r["kind"], r["field"], steps, social, r["by"], emits)
    return out


# Filled at the bottom of this block, once Step/WriteClass exist.
MATRIX: dict[tuple[str, str], MatrixRow] = _load_write_matrix()

# Rows W2 RETIRED, kept so a write to one gets its own diagnosis rather than the generic
# "no row" -- a retired row and a row that never existed are different facts about the design.
import yaml as _yaml_boot
MATRIX_RETIRED: dict = {
    tuple(x.split(".", 1)): "retired by W2 -- its `emits:` kind is produced by no Part E verb "
                            "and written at no MATTER site"
    for x in (_yaml_boot.safe_load(WRITE_MATRIX_YAML.read_text()).get("retired") or [])
}

# S320's disclosure hook. W2 empties it BY CONSTRUCTION -- the three rows it used to carry were
# instrument assumptions only because the old two-clause derivation could not reach them, and
# S D2's DR-3 states all three. `report.py` still reads it, and it now reports zero.
PARTITION_ASSUMED: dict[tuple[str, str], tuple[bool, str]] = {}


def assume_partition_row(record_kind: str, fieldname: str, social: bool, why: str) -> None:
    """THE CHANNEL, kept live so its emptiness means something.

    ⚠ W2 emptied `PARTITION_ASSUMED` and reported "ZERO exercised assumptions" as its proof. An
    adversarial pass observed that the dict had become a LITERAL NO CODE PATH COULD POPULATE, so
    the claim was satisfiable BY DELETION and `ASSUMPTIONS.md` read "0 of 0" rather than "0 of 3".
    That is §0.1 point 2 in its purest form: an assertion that cannot observe the failure it
    excludes. This function is the path, so zero is now a measurement rather than an absence.

    An instrument that must assume a schema row calls this. It should never need to — §D2's DR-3
    states the three rows that used to be assumed — and if it ever does, `report.py` says so."""
    PARTITION_ASSUMED[(record_kind, fieldname)] = (social, why)
    ASSUMPTIONS_USED.add((record_kind, fieldname))


# ⚠ REV 5. This set was WRITTEN AND NEVER READ for two revisions, while S320's comment promised
# the assumed rows were "REPORTED IN THE OUTPUT, so a reader can see exactly how much of L4's
# enforcement rests on the instrument". Under this file's own fidelity rule 6 that was a false
# claim of a disclosure mechanism. `report.py` now reads it.
ASSUMPTIONS_USED: set[tuple[str, str]] = set()


def matrix_row(record_kind: str, fieldname: str) -> MatrixRow:
    """THE ONE LOOKUP. Six structures and a derivation loop collapsed into this, because they
    were six answers to one question that #353 §30 asks once: is `(kind, field)` on the table?"""
    row = MATRIX.get((record_kind, fieldname))
    if row is not None:
        return row
    if (record_kind, fieldname) in MATRIX_RETIRED:
        raise Unspecified(
            f"({record_kind}, {fieldname}) was RETIRED from the write matrix", "S30.1",
            needs="a Part E verb that produces its `emits:` kind, added in the same commit as "
                  "the row",
            law=MATRIX_RETIRED[(record_kind, fieldname)])
    raise Unspecified(
        f"({record_kind}, {fieldname}) is on no row of the write matrix", "S30.1",
        needs="rule the row first, then add it; the reverse order invents the thing the rule prevents",
        law="S30 -- ANY UNMARKED CELL IS A WRITE-CLASS VIOLATION. L4's membership test is a "
            "STATIC SCHEMA COLUMN, not a judgement; S42.3 -- configuring an unspecified thing "
            "invents it")


def partition_lookup(record_kind: str, fieldname: str, thing: str = "") -> tuple[bool, str]:
    """L4's `social:` for a pair. Kept as a name because probes call it; it is a thin read of
    `matrix_row` now, and `thing` is ignored -- IT IS THE PARAMETER THAT CARRIED THE DEFECT."""
    row = matrix_row(record_kind, fieldname)
    if row.social is None:
        raise Unspecified(
            f"({record_kind}, {fieldname}) is `social: n/a` -- the row admits no write of this "
            "kind", "S30.1", needs="a `social:` column entry, ruled", law=row.by)
    return row.social, row.by
