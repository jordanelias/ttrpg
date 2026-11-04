"""`season.data.strife` -- THE ONE LOADER for `strife_moves.yaml`.

The file reads the 40 move codes of the strife study against what the season loop can produce.
This module refuses a row naming a verb that is not in `verb_table.yaml`, an Event kind the loop
does not declare, a key the row does not define, or a code listed twice. It resolves nothing and
no step of the loop reads it; `harness/strife.py` is its reader.
"""

from __future__ import annotations

from .files import STRIFE_MOVES_YAML
from .matrix import MATRIX
from .rosters import load_yaml
from .verbs import EMITTED_KINDS, VERB_TABLE


def declared_kinds() -> frozenset:
    """Every Event kind the loop declares: the verb rows' `emits:` columns and the write matrix's."""
    return frozenset(EMITTED_KINDS) | {k for m in MATRIX.values() for k in m.emits}


def load_moves() -> tuple:
    """The rows of `strife_moves.yaml`, validated, in file order."""
    doc = load_yaml(STRIFE_MOVES_YAML.read_text(encoding="utf-8"))
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
    return tuple(rows)


MOVES = load_moves()
