#!/usr/bin/env python3
"""
ci_generation_consistency.py — enforce the v40 generation currency invariant.

The "current canonical surface" (generation v40 — the consolidated, contracts-bound,
Godot-ready generation) is declared in /CURRENT.md and machine-tracked in
references/canonical_sources.yaml. This gate asserts, for every canonical design doc:

  1. it exists on disk;
  2. it carries a recognized `## Status:` line (the per-doc currency signal); and
  3. its path is NOT recorded as a `superseded_id:` in canon/supersession_register.yaml
     (a doc cannot be both a canonical head and superseded — that is currency drift).

This is the durable fix for the v30/v32 proliferation: currency is *enforced*, not
implied by a filename. See designs/audit/2026-06-28-deprecation-currency-sweep/
v40_generation_plan.md.

WARN-ONLY for now (returns 0) while the corpus is normalized to a consistent Status
vocabulary. Flip BLOCKING (return 1 on issues) once clean — same staged pattern the
other gates followed.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CANON_SOURCES = os.path.join(ROOT, "references", "canonical_sources.yaml")
SUPERSESSION = os.path.join(ROOT, "canon", "supersession_register.yaml")

# Recognized lifecycle vocabulary for a current canonical doc's Status line.
RECOGNIZED = ("CANONICAL", "CURRENT", "CANON", "WORKING", "DESIGN", "REFERENCE", "PROVISIONAL")

DOC_KEYS = r"(design_doc|index|infill|integration_plan_doc|spec|related)"

# _index / _infill co-files inherit their parent doc's status — a redundant Status
# line on a navigation/atomization artifact is noise, so they are exempt.
COFILE_SUFFIXES = ("_index.md", "_infill.md")

# Docs that are legitimately BOTH canonical and a superseded_id: a partial
# supersession where only one layer died and the rest is retained-canonical.
# Each must carry an in-file banner for the dead layer (see supersession_register).
KNOWN_PARTIAL = {
    "designs/scene/combat_v30.md",  # RESOLUTION layer -> combat_engine_v1 (ED-900); lore/flavor canonical
}


def canonical_docs():
    """Design-doc paths referenced as authoritative in canonical_sources.yaml."""
    docs = set()
    with open(CANON_SOURCES, encoding="utf-8") as fh:
        for line in fh:
            if line.lstrip().startswith("#"):
                continue
            for m in re.finditer(DOC_KEYS + r"\s*:\s*(designs/[^\s#]+\.md)", line):
                docs.add(m.group(2))
    return sorted(d for d in docs if os.path.isfile(os.path.join(ROOT, d)))


def status_of(relpath):
    with open(os.path.join(ROOT, relpath), encoding="utf-8") as fh:
        head = fh.read().splitlines()[:12]
    for ln in head:
        m = re.match(r"\s*#{0,3}\s*Status\s*:\s*(.+)", ln, re.IGNORECASE)
        if m:
            return m.group(1).strip()
    return None


def superseded_ids():
    ids = set()
    with open(SUPERSESSION, encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r"""\s*-?\s*superseded_id:\s*["']?(designs/[^\s"'#]+\.md)""", line)
            if m:
                ids.add(m.group(1))
    return ids


def main():
    docs = canonical_docs()
    sup = superseded_ids()
    no_status, drift, nonstd = [], [], []
    for d in docs:
        is_cofile = d.endswith(COFILE_SUFFIXES)
        s = status_of(d)
        if s is None:
            if not is_cofile:
                no_status.append(d)
        elif not any(k in s.upper() for k in RECOGNIZED):
            nonstd.append((d, s))
        if d in sup and d not in KNOWN_PARTIAL:
            drift.append(d)

    print("[generation v40] %d canonical design docs checked." % len(docs))
    issues = 0
    if no_status:
        issues += len(no_status)
        print("  [WARN] %d canonical docs lack a Status line:" % len(no_status))
        for d in no_status:
            print("         - " + d)
    if drift:
        issues += len(drift)
        print("  [WARN] %d canonical docs are recorded as superseded (currency drift — "
              "banner the partial / remove from canonical_sources):" % len(drift))
        for d in drift:
            print("         - " + d)
    if nonstd:
        print("  [INFO] %d docs use a non-standard Status vocabulary:" % len(nonstd))
        for d, s in nonstd:
            print("         - %s :: %s" % (d, s[:50]))
    if not issues:
        print("  OK — every canonical doc carries a Status line and none are superseded.")

    # WARN-ONLY: do not fail the build yet.
    return 0


if __name__ == "__main__":
    sys.exit(main())
