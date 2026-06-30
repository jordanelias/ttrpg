#!/usr/bin/env python3
"""
engine_params_check.py — round-trip validator for the typed engine-params layer (ED-1052).

WHY THIS EXISTS
---------------
All mechanical parameters live as PROSE markdown tables in params/*.md, which a Godot
importer cannot ingest, and references/values_master.yaml (auto-extracted) stores formulas
as free-text English and is partly stale/wrong. references/engine_params/*.json is the typed,
Godot-ingestible source: numeric operands, structured formulas, explicit clamps. This gate
keeps that typed layer HONEST — every entry must cite a prose `source` whose `quote` still
appears verbatim in the cited doc, so the typed values cannot silently drift from canon.

WHAT IT CHECKS (errors; exit 1 in CI)
-------------------------------------
  schema     — required keys present; scalars/formulas/tables well-formed.
  provenance — every entry's source.doc exists in the working tree.
  round-trip — every entry's source.quote (whitespace-normalized) appears in source.doc.
  clamp      — clamp.min <= clamp.max where both are given.
  formula    — expr present; declared inputs non-empty; identifiers in expr are either
               declared inputs, other formula keys, scalar keys, or a small math allowlist.

Reads the working tree only — no network, no PAT. The pure cores (validate_file / round-trip
helpers) are import-testable; see tests/valoria/test_engine_params_check.py.

Usage:
    python3 tools/engine_params_check.py
"""
import os
import re
import sys
import json
import glob

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
ENGINE_PARAMS_GLOB = "references/engine_params/*.json"

# Identifiers permitted in a formula expr beyond its declared inputs / other param keys.
_MATH_ALLOWLIST = {"min", "max", "floor", "ceil", "abs", "and", "or", "not"}
_IDENT_RE = re.compile(r'[A-Za-z_][A-Za-z0-9_]*')


def _norm_ws(s: str) -> str:
    """Collapse every run of whitespace (incl. newlines) to a single space, and strip.
    Lets a single-line `quote` match prose regardless of incidental spacing, while
    preserving unicode operators (×, −, ≥) which are load-bearing in the formulas."""
    return re.sub(r'\s+', ' ', s).strip()


def quote_in_doc(quote: str, doc_text: str) -> bool:
    """True if `quote` appears in `doc_text` under whitespace normalization."""
    return _norm_ws(quote) in _norm_ws(doc_text)


def _read_doc(path, _cache={}):
    if path not in _cache:
        full = os.path.join(REPO_ROOT, path)
        try:
            with open(full, encoding='utf-8') as f:
                _cache[path] = f.read()
        except OSError:
            _cache[path] = None
    return _cache[path]


def _check_source(label, src, doc_reader, errors):
    """Validate one `source` block: doc exists + quote round-trips."""
    if not isinstance(src, dict):
        errors.append(f"{label}: missing/invalid 'source'")
        return
    doc = src.get("doc")
    quote = src.get("quote")
    if not doc:
        errors.append(f"{label}: source.doc missing")
        return
    text = doc_reader(doc)
    if text is None:
        errors.append(f"{label}: source.doc '{doc}' not found in working tree")
        return
    if not quote:
        errors.append(f"{label}: source.quote missing")
        return
    if not quote_in_doc(quote, text):
        errors.append(f"{label}: quote not found in {doc} — {quote!r} (prose drift?)")


def _check_clamp(label, clamp, errors):
    if clamp is None:
        return
    if not isinstance(clamp, dict):
        errors.append(f"{label}: clamp must be an object")
        return
    lo, hi = clamp.get("min"), clamp.get("max")
    if lo is not None and hi is not None and lo > hi:
        errors.append(f"{label}: clamp.min ({lo}) > clamp.max ({hi})")


def validate_file(data, doc_reader=_read_doc):
    """Pure core: validate one parsed engine-params object. Returns a list of error strings."""
    errors = []
    if not isinstance(data, dict):
        return ["top-level value is not an object"]
    for req in ("schema_version", "subsystem"):
        if req not in data:
            errors.append(f"missing required top-level key '{req}'")
    sub = data.get("subsystem", "?")

    scalars = data.get("scalars", {}) or {}
    formulas = data.get("formulas", {}) or {}
    tables = data.get("tables", {}) or {}
    if not (scalars or formulas or tables):
        errors.append(f"[{sub}] file declares no scalars, formulas, or tables")

    # Known identifiers a formula may reference without declaring them as inputs.
    known_names = set(scalars) | set(formulas) | _MATH_ALLOWLIST

    for key, entry in scalars.items():
        label = f"[{sub}] scalar.{key}"
        if not isinstance(entry, dict):
            errors.append(f"{label}: not an object"); continue
        if not isinstance(entry.get("value"), (int, float)) or isinstance(entry.get("value"), bool):
            errors.append(f"{label}: 'value' must be a number")
        _check_clamp(label, entry.get("clamp"), errors)
        _check_source(label, entry.get("source"), doc_reader, errors)

    for key, entry in formulas.items():
        label = f"[{sub}] formula.{key}"
        if not isinstance(entry, dict):
            errors.append(f"{label}: not an object"); continue
        expr = entry.get("expr")
        inputs = entry.get("inputs")
        if not expr or not isinstance(expr, str):
            errors.append(f"{label}: 'expr' missing/invalid")
        if not inputs or not isinstance(inputs, list):
            errors.append(f"{label}: 'inputs' must be a non-empty list")
        if expr and isinstance(inputs, list):
            declared = set(inputs) | known_names
            for ident in _IDENT_RE.findall(expr):
                if ident not in declared:
                    errors.append(f"{label}: identifier '{ident}' in expr is not a declared "
                                  f"input, param key, or math function")
        _check_clamp(label, entry.get("clamp"), errors)
        _check_source(label, entry.get("source"), doc_reader, errors)

    for key, entry in tables.items():
        label = f"[{sub}] table.{key}"
        if not isinstance(entry, dict):
            errors.append(f"{label}: not an object"); continue
        if not isinstance(entry.get("rows"), dict) or not entry.get("rows"):
            errors.append(f"{label}: 'rows' must be a non-empty object")
        _check_source(label, entry.get("source"), doc_reader, errors)

    return errors


def main(argv):
    paths = sorted(glob.glob(os.path.join(REPO_ROOT, ENGINE_PARAMS_GLOB)))
    if not paths:
        print(f"[ENGINE-PARAMS OK] no files under {ENGINE_PARAMS_GLOB} — nothing to check.")
        return 0

    all_errors = []
    checked = 0
    for full in paths:
        rel = os.path.relpath(full, REPO_ROOT).replace(os.sep, '/')
        try:
            with open(full, encoding='utf-8') as f:
                data = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            all_errors.append(f"{rel}: cannot parse — {e}")
            continue
        checked += 1
        for err in validate_file(data):
            all_errors.append(f"{rel}: {err}")

    if all_errors:
        print("[ENGINE-PARAMS] typed engine-params validation failed:")
        for e in all_errors:
            print(f"[ENGINE-PARAMS]   {e}")
        print("[ENGINE-PARAMS] Every entry must cite a prose source whose quote still appears in "
              "the doc. Fix the typed value, repoint the source, or update the quote.")
        return 1

    print(f"[ENGINE-PARAMS OK] {checked} typed engine-params file(s) validated; "
          "all entries round-trip to their prose sources.")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
