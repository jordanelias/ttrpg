#!/usr/bin/env python3
"""
audit_staleness.py — surface which corpus-wide audits have drifted since their last
committed refresh, git facts only, no network, no new hand-maintained registry.

Modeled directly on tools/workplan_status.py::staleness() (ED-IN-0010's proven pattern):
for an audit family, "last refreshed" = the git commit that last touched its committed
artifact (git log -1 -- <artifact_path>); "drift" = the count of distinct files matching
that family's scope that changed since (git log --name-only <sha>..HEAD -- <scope...>).
No fixed cadence is asserted — a family with a lot of unrelated corpus churn since its
last touch is exactly the "went stale and nobody noticed" pattern this exists to catch
(cf. the vector-audit case that motivated this file, ED-IN-0032 planning).

The audit-family scope table below is a short Python literal, not a YAML file — this
repo's audit/compliance tooling has a documented recurring failure mode of hand-maintained
registries silently drifting from reality (CLAUDE.md §8, references/ci_checks_registry.yaml).
Adding one more would be rot surface #4; the table lives here, next to the code that reads
it, and is expected to be edited in the same commit as any family's scope changing.

Honest limitation: freshness here is only observable for audits that leave a *committed*
artifact in this git history. An audit that ran but committed nothing is indistinguishable
from an audit that never ran — that is intentional, matching this repo's anti-fabrication
ethos (CLAUDE.md §7): we do not report "the audit is fresh" on the strength of an unverifiable
claim that someone ran it. A second, sharper limitation specific to this repo: the working
clone is shallow (see `git rev-parse --is-shallow-repository`), so `git log -1 -- <path>`
can bottom out at the shallow history boundary rather than the artifact's true origin commit.
When that happens the reported "last touched" commit is only a lower bound on freshness
(it can't be *more* stale than reported, only differently dated) — drift counts computed
from it remain meaningful because they only look forward to HEAD, never before the boundary.

Defensive by contract: every public function catches broadly and degrades to "no data"
rather than raising — this is imported by the SessionStart hook (tools/session_status.py)
and must never break session start.
"""
import os
import subprocess
import sys

# --- Audit-family scope table -----------------------------------------------------------
# One entry per family. `artifact_paths`: committed file(s)/dir(s) whose most recent git
# touch stands in for "this audit was last really refreshed". `scope_prefixes`: pathspecs
# (git will union multiple pathspecs) defining what corpus churn counts as "drift since."
# Scopes for decisions-digest / graph / lexicon are lifted from those generators' own
# stated source lists (their docstrings/header comments), not reinvented — "one rule, one
# home" (CLAUDE.md §8) applies to scope definitions too.
FAMILIES = [
    {
        "name": "vector-audit",
        # Repointed 2026-07-14 (ED-IN-0064) from the stale 2026-04-29 baseline to the fresh
        # gameplay-subsystem observatory run — the first real run since the pipeline dispatcher landed.
        "artifact_paths": ["designs/audit/2026-07-14-gameplay-subsystem-observatory/"],
        "scope_prefixes": ("designs/", "canon/", "engine/params/", "references/"),
    },
    {
        "name": "decisions-digest",
        "artifact_paths": ["tools/observability/decisions.json"],
        # per build_decisions.py's own header: "corpus sweep (designs/ canon/ engine/params/
        # references/ sim/) for explicit markers".
        "scope_prefixes": ("designs/", "canon/", "engine/params/", "references/", "sim/"),
    },
    {
        "name": "proposals-register",
        "artifact_paths": ["tools/observability/proposals.json"],
        # per build_proposals.py's sources: the editorial ledgers, audit registry,
        # proposals/ + Status-tagged design docs, and workplan §5.
        "scope_prefixes": ("designs/", "canon/", "references/audit_registry.jsonl",
                           "workplans/"),
    },
    {
        "name": "apparatus-registry",
        "artifact_paths": ["references/apparatus_registry.yaml"],
        # build_apparatus_registry.py scans tools/, skills/, .githooks/, .claude/,
        # .github/workflows/ for the output/format/orphan inventory.
        "scope_prefixes": ("tools/", "skills/", ".githooks/", ".github/workflows/"),
    },
    {
        "name": "graph-lexicon",
        # Tracked as one family (not two): build_graph.py and build_lexicon.py are
        # regenerated together in practice and their source scopes overlap heavily
        # (references/ + canon/); splitting them would double-count the same drift.
        "artifact_paths": [
            "tools/observability/graph.json",
            "tools/observability/lexicon.json",
        ],
        # union of build_graph.py's sources (references/module_contracts.yaml,
        # designs/architecture/key_type_registry_v30.md, registers/mechanics_index.yaml) and
        # build_lexicon.py's sources (references/*.yaml, references/glossary.md,
        # registers/placeholder_names.yaml, designs/architecture/scale_transitions_v30.md).
        "scope_prefixes": ("references/", "canon/", "designs/architecture/"),
    },
    {
        "name": "npc-audit",
        "artifact_paths": ["designs/audit/2026-06-22-npc-comprehensive-audit.md"],
        "scope_prefixes": ("designs/npcs/", "references/npc_registry.yaml"),
    },
    {
        "name": "mechanics-index",
        "artifact_paths": ["registers/mechanics_index.yaml"],
        # Broad designs/ scope (no cheaply-determinable mechanics-relevant subset).
        # Lower priority than the other families: since Phase 2 (commit 806aa63),
        # tools/mechanics_index_gen.py --strict runs in CI on every push and continuously
        # validates this file's *internal schema validity*. That is a different concern
        # from what this module tracks — whether the audit's *content* has fallen behind
        # corpus changes — and CI covers the former continuously, this covers the latter.
        "scope_prefixes": ("designs/",),
    },
]


def _sh(args):
    try:
        r = subprocess.run(["git"] + args, capture_output=True, text=True, timeout=30)
    except Exception:
        return None
    return r.stdout if r.returncode == 0 else None


def _last_touch(path):
    """Return (full_sha, short_sha, date) of the last commit touching `path`, or None."""
    out = _sh(["log", "-1", "--format=%H\x1f%h\x1f%ad", "--date=short", "--", path])
    if out is None:
        return None
    out = out.strip()
    if not out:
        return None
    parts = out.split("\x1f")
    if len(parts) != 3:
        return None
    return tuple(parts)  # (full_sha, short_sha, date)


def _family_base(family):
    """Pick the most-recently-touched of a family's artifact_paths as its refresh base."""
    best = None  # (unix_ts, full_sha, short_sha, date, path)
    for path in family["artifact_paths"]:
        if not os.path.exists(path):
            continue
        touch = _last_touch(path)
        if not touch:
            continue
        full_sha, short_sha, date = touch
        ts_out = _sh(["log", "-1", "--format=%ct", "--", path])
        try:
            ts = int((ts_out or "0").strip())
        except ValueError:
            ts = 0
        if best is None or ts > best[0]:
            best = (ts, full_sha, short_sha, date, path)
    return best


def _drift_count(base_sha, scope_prefixes, exclude):
    out = _sh(["log", "--name-only", "--pretty=format:", f"{base_sha}..HEAD", "--"]
              + list(scope_prefixes))
    if out is None:
        return None
    touched = {ln.strip() for ln in out.splitlines() if ln.strip()}
    touched -= set(exclude)
    return len(touched)


def _family_status(family):
    """Compute one family's staleness. Returns a dict, or None if it couldn't be computed."""
    try:
        base = _family_base(family)
        if base is None:
            return None
        _ts, full_sha, short_sha, date, base_path = base
        drift = _drift_count(full_sha, family["scope_prefixes"], family["artifact_paths"])
        if drift is None:
            return None
        return {
            "name": family["name"],
            "base_sha": short_sha,
            "base_date": date,
            "base_path": base_path,
            "drift": drift,
        }
    except Exception:
        return None


def report():
    """All families' status, best-effort — families that error out are simply omitted."""
    out = []
    for fam in FAMILIES:
        st = _family_status(fam)
        if st is not None:
            out.append(st)
    return out


def _warning_line(st):
    return (f"⚠ audit stale: {st['name']} — {st['drift']} in-scope file(s) changed since "
            f"last refresh ({st['base_sha']}, {st['base_date']}) — see "
            "tools/audit_staleness.py for detail")


def top_stale(n=2):
    """At most `n` one-line warnings for the stalest families (nonzero drift only),
    sorted by drift count descending. Never raises; returns [] on any failure.
    """
    try:
        rows = [st for st in report() if st["drift"] > 0]
        rows.sort(key=lambda st: st["drift"], reverse=True)
        return [_warning_line(st) for st in rows[:n]]
    except Exception:
        return []


def full():
    rows = report()
    if not rows:
        print("audit-staleness: (no family status available)")
        return
    rows_sorted = sorted(rows, key=lambda st: st["drift"], reverse=True)
    print("audit-staleness — per-family breakdown (stalest first):")
    for st in rows_sorted:
        flag = "STALE" if st["drift"] > 0 else "fresh"
        print(f"  {st['name']:16} {flag:5}  drift={st['drift']:>4}  "
              f"last refresh {st['base_sha']} ({st['base_date']})  "
              f"artifact={st['base_path']}")
    computed = {st["name"] for st in rows}
    missing = [fam["name"] for fam in FAMILIES if fam["name"] not in computed]
    if missing:
        print("  (no data for: " + ", ".join(missing) + ")")


def main():
    try:
        full()
        print()
        top = top_stale()
        if top:
            print("top-2 stalest (what session_status.py surfaces):")
            for line in top:
                print("  " + line)
        else:
            print("top-2 stalest: none — all tracked families read as fresh")
    except Exception as e:  # never break a hook or a manual run
        print(f"audit-staleness: (status unavailable: {e})")
    sys.exit(0)


if __name__ == "__main__":
    main()
