#!/usr/bin/env python3
"""link_values_pointers.py — connect the typed values to the pointers (Repository State Armature
values layer, ED-IN-0079). Closes the loop back to the primitives the session started on.

The values (typed sim constants in engine/engine_params/sim_params.json) and the pointers (the
attribute/stat/track definitions in references/definitions/definitions.yaml + the name_collision
abbreviations) are linked by LITERAL TOKEN MATCH — a value is linked to a pointer only when the
pointer's canonical name or abbreviation literally appears in the value's constant-name or dict
keys. This is DERIVED, not fabricated: every link records the exact token that matched, so a human
can audit or dismiss it; the tool never asserts a semantic relationship the text doesn't show.

Guards against false positives (anti-fabrication):
  * authoring/dice-engine abbreviations (PP, ED, SIM, TN, Ob, EV) are excluded — not game pointers.
  * a token immediately followed by digits (PP_329, ED_865) is a cite ID, not a pointer reference.
  * proper-noun definitions (world entities) are excluded — they are not mechanical values.

Output: engine/engine_params/value_pointer_links.json — by_pointer (each pointer → the constants
that reference it) and by_value (each constant → the pointers it references), plus the flat link
list with method + matched token.

CLI:
  python3 tools/link_values_pointers.py --build     # regenerate the link map
  python3 tools/link_values_pointers.py --check      # drift gate (exit 1 on drift)
  python3 tools/link_values_pointers.py --pointer "Piety Track"   # values referencing a pointer
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SIM_PARAMS = ROOT / "engine" / "engine_params" / "sim_params.json"
DEFINITIONS = ROOT / "references" / "definitions" / "definitions.yaml"
NAME_COLLISION = ROOT / "references" / "name_collision_database.yaml"
OUT = ROOT / "engine" / "engine_params" / "value_pointer_links.json"

# Authoring / dice-engine abbreviations — infrastructure vocabulary, not game-state pointers.
_EXCLUDE_ABBR = {"pp", "ed", "sim", "tn", "ob", "ev"}
_EXCLUDE_SILOS = {"16A", "16B"}


def _pointer_vocab() -> dict:
    """token (lowercased, ≥2/3 chars) -> (pointer_display, pointer_key). Game pointers only."""
    vocab: dict[str, tuple] = {}
    defs = (yaml.safe_load(DEFINITIONS.read_text()) or {}).get("definitions", {})
    for key, rec in defs.items():
        if rec.get("category") == "proper_noun":
            continue
        for form in [rec.get("canonical")] + (rec.get("aliases") or []) + (rec.get("legacy") or []):
            for tok in re.split(r"[\s/()\-]+", str(form or "")):
                if len(tok) >= 3 and tok.lower() not in _EXCLUDE_ABBR:
                    vocab.setdefault(tok.lower(), (rec.get("canonical"), key))
    nc = yaml.safe_load(NAME_COLLISION.read_text()) or {}
    for abbr, info in (nc.get("abbreviations") or {}).items():
        if not isinstance(info, dict):
            continue
        if len(abbr) >= 2 and abbr.lower() not in _EXCLUDE_ABBR and str(info.get("silo")) not in _EXCLUDE_SILOS:
            vocab.setdefault(abbr.lower(), (info.get("term"), f"nc.{abbr}"))
    return vocab


def _name_tokens(name: str):
    """(token, followed_by_digit) for each alpha run — the digit flag skips cite IDs (PP_329)."""
    out = []
    for m in re.finditer(r"[A-Za-z]+", name):
        out.append((m.group(0), name[m.end():m.end() + 1].isdigit()))
    return out


def build() -> dict:
    vocab = _pointer_vocab()
    params = json.loads(SIM_PARAMS.read_text())["params"]
    links = []
    for r in params:
        seen = set()
        for tok, after_digit in _name_tokens(r["name"]):
            if after_digit:
                continue
            v = vocab.get(tok.lower())
            if v and (v[1], "name_token") not in seen:
                seen.add((v[1], "name_token"))
                links.append({"value": r["key"], "value_file": r["file"], "token": tok,
                              "pointer": v[0], "pointer_key": v[1], "method": "name_token"})
        if isinstance(r["value"], dict):
            for kk in r["value"]:
                v = vocab.get(str(kk).lower())
                if v and (v[1], "dict_key") not in seen:
                    seen.add((v[1], "dict_key"))
                    links.append({"value": r["key"], "value_file": r["file"], "token": str(kk),
                                  "pointer": v[0], "pointer_key": v[1], "method": "dict_key"})
    links.sort(key=lambda l: (l["pointer_key"], l["value"], l["method"]))
    by_pointer: dict[str, dict] = {}
    by_value: dict[str, list] = {}
    for l in links:
        p = by_pointer.setdefault(l["pointer_key"], {"pointer": l["pointer"], "values": []})
        if l["value"] not in p["values"]:
            p["values"].append(l["value"])
        by_value.setdefault(l["value"], [])
        if l["pointer_key"] not in by_value[l["value"]]:
            by_value[l["value"]].append(l["pointer_key"])
    return {
        "_generated": "GENERATED by tools/link_values_pointers.py — values<->pointers by LITERAL "
                      "token match (each link records the matched token; nothing semantic is invented). "
                      "Regenerate with --build; drift-gated by --check.",
        "schema_version": 1,
        "link_count": len(links),
        "linked_values": len(by_value),
        "linked_pointers": len(by_pointer),
        "links": links,
        "by_pointer": by_pointer,
        "by_value": by_value,
    }


def _serialize(state: dict) -> str:
    return json.dumps(state, indent=2, ensure_ascii=False) + "\n"


def write() -> Path:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(_serialize(build()), encoding="utf-8")
    return OUT


def check() -> tuple[bool, list[str]]:
    if not OUT.exists():
        return False, ["value_pointer_links.json missing — run `link_values_pointers.py --build`"]
    if OUT.read_text(encoding="utf-8") != _serialize(build()):
        return False, ["DRIFT: committed value_pointer_links.json != fresh build — run --build and commit"]
    return True, []


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--pointer", metavar="NAME")
    args = ap.parse_args(argv)
    if args.build:
        p = write()
        s = json.loads(p.read_text())
        print(f"wrote {p.relative_to(ROOT)} — {s['link_count']} links "
              f"({s['linked_values']} values ↔ {s['linked_pointers']} pointers)")
        return 0
    if args.check:
        ok, msgs = check()
        for m in msgs:
            print("  - " + m, file=sys.stderr)
        print("[VALUE-LINKS] current" if ok else "[VALUE-LINKS] FAILED", file=sys.stdout if ok else sys.stderr)
        return 0 if ok else 1
    if args.pointer:
        data = json.loads(OUT.read_text()) if OUT.exists() else {"by_pointer": {}}
        q = args.pointer.lower()
        for pk, blk in data["by_pointer"].items():
            if q in (blk["pointer"] or "").lower() or q in pk.lower():
                print(f"{blk['pointer']} ({pk}) ← {len(blk['values'])} value(s):")
                for v in blk["values"]:
                    print("   ", v)
        return 0
    print(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
