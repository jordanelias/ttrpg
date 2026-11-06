"""`harness.strife_data` -- THE ONE LOADER for `strife_moves.yaml`.

The file reads the 40 move codes of the strife study against what the season loop can produce.
This module refuses a row naming a verb that is not in `verb_table.yaml`, an Event kind the loop
does not declare, a key the row does not define, a code listed twice, or per-code ending counts that
do not total the study's 102 cases. It resolves nothing and no step of the loop reads it;
`harness/strife.py` is its reader.

WHY IT LIVES UNDER `harness/` AND NOT `data/`. The port gate (plan position GO-09) exports every
file `data/files.py` names that a loader reads. A registry only the harness reads must not reach the
port, so its path is anchored here from `HARNESS_DIR` and `files.py` does not name it.
"""

from __future__ import annotations

from ..data.files import HARNESS_DIR
from ..data.rosters import load_yaml
from ..queries.world_q import FOREIGN_FACTION_IDS
from ..data.verbs import EVENT_KINDS, VERB_TABLE

STRIFE_MOVES_YAML = HARNESS_DIR / "strife_moves.yaml"


def declared_kinds() -> frozenset:
    """Every Event kind the loop declares: `data/verbs.py::EVENT_KINDS`, the one owner (loader invariant 7).

    A STRICT SUPERSET OF THE ROSTER THIS FUNCTION USED TO BUILD. That one (`EMITTED_KINDS` and the write matrix's
    `emits:`) already held the per-degree and per-clause emission columns, since `VerbRow.emits` and
    `emits_on_refusal` are flat unions over them. What `EVENT_KINDS` adds is `fold_kinds` and `logged_kinds`
    (`act.ineligible`, `act.refused`, `attempt.refused`, `standing.band_crossed`), so the loader now accepts
    those four; no kind it accepted is refused, and none of the four is named in the registry."""
    return EVENT_KINDS


def load_moves(path=STRIFE_MOVES_YAML) -> tuple:
    """`(rows, signatures, foreign)` of `strife_moves.yaml`, validated, in file order. `foreign` is the set of
    faction Proposition ids of `rosters.yaml: foreign_factions` (CR-75 moved the list there from this file, so
    `queries/world_q.py`, which may not import the harness, can read it; an unknown name is refused at load)."""
    doc = load_yaml(path.read_text(encoding="utf-8"))
    rows, row_keys, needs_vocabulary = doc["moves"], set(doc["row_keys"]), set(doc["needs_vocabulary"])
    kinds, seen = declared_kinds(), set()
    for r in rows:
        code = r.get("code")
        unknown = set(r) - row_keys
        if unknown:
            raise ValueError(f"strife_moves.yaml: {code!r} carries unknown key(s) {sorted(unknown)}")
        if code in seen:
            raise ValueError(f"strife_moves.yaml: code {code!r} listed twice")
        seen.add(code)
        bad_verbs = [v for v in r["verbs"] if v not in VERB_TABLE]
        if bad_verbs:
            raise ValueError(f"strife_moves.yaml: {code} names verb(s) {bad_verbs} not in verb_table.yaml")
        bad_kinds = [k for k in r["kinds"] if k not in kinds]
        if bad_kinds:
            raise ValueError(f"strife_moves.yaml: {code} names Event kind(s) {bad_kinds} the loop does not declare")
        bad_needs = set(r.get("needs", ())) - needs_vocabulary
        if bad_needs:
            raise ValueError(f"strife_moves.yaml: {code} has needs {sorted(bad_needs)} outside side/office/context")
        if not r["kinds"] and not r.get("gap"):
            raise ValueError(f"strife_moves.yaml: {code} has no kinds and states no gap")
        if not isinstance(r.get("ends", 0), int) or r.get("ends", 0) < 0:
            raise ValueError(f"strife_moves.yaml: {code} has `ends` that is not a count")
    total = sum(r.get("ends", 0) for r in rows)
    if total != doc["study_cases"]:
        raise ValueError(f"strife_moves.yaml: per-code `ends` total {total}, not the study's {doc['study_cases']} cases")
    sig_keys, sides = set(doc["signature_keys"]), set(doc["attacker_values"])
    sigs = doc.get("signatures", [])
    for g in sigs:
        unknown = set(g) - sig_keys
        if unknown:
            raise ValueError(f"strife_moves.yaml: signature {g} carries unknown key(s) {sorted(unknown)}")
        if g["code"] not in seen:
            raise ValueError(f"strife_moves.yaml: signature {g} names code {g['code']!r} that has no row")
        if g["kind"] not in kinds:
            raise ValueError(f"strife_moves.yaml: signature {g} names Event kind {g['kind']!r} the loop does not declare")
        cv = g.get("cause_verb")
        if cv is not None and cv != "none" and cv not in VERB_TABLE:
            raise ValueError(f"strife_moves.yaml: signature {g} names verb {cv!r} not in verb_table.yaml")
        if "victim_held" in g and not isinstance(g["victim_held"], bool):
            raise ValueError(f"strife_moves.yaml: signature {g} has `victim_held` that is not a boolean")
        if "attacker" in g and g["attacker"] not in sides:
            raise ValueError(f"strife_moves.yaml: signature {g} has attacker outside {sorted(sides)}")
    return tuple(rows), tuple(sigs), FOREIGN_FACTION_IDS


MOVES, SIGNATURES, FOREIGN = load_moves()
