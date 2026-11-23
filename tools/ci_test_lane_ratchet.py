#!/usr/bin/env python3
"""ci_test_lane_ratchet.py -- BLOCKING: no test lane, and not tools/, grows without a warrant.

Jordan, 2026-11-23: "Do NOT allow unwarranted accretion to happen." Every test belongs to one lane (conftest.py:
the season loop, the engine, or one subsystem). `references/test_lane_caps.yaml` holds each lane's floor (`base`) and
its `warrants`; this check counts the tests each lane collects (`pytest --collect-only -m <lane>`, nothing runs) and the
files git tracks under tools/, and fails when:

  * a test has no lane (the lanes' counts do not sum to the collection);
  * a lane or tools/ holds MORE than base + its warrants' `added`  (unwarranted growth);
  * a lane or tools/ holds FEWER (slack: a retirement not yet written down could be spent by someone else; run
    `--tighten` and commit the file, which folds the warrants into the new base);
  * a warrant is not substantive (a batch, a positive `added`, and a `behaviour` of at least 12 characters);
  * against origin/main, the cap rose by more than the NEW warrants add (an edited `base` is not a warrant).

It is a reader's rule made mechanical because Jordan ruled it so (CLAUDE.md section 0.1 pt 5: a Jordan decision
makes the artifact load-bearing). It reads the test collection and git; it runs no test.

Usage:  python tools/ci_test_lane_ratchet.py [--tighten] [--base-ref origin/main]
"""
import argparse
import os
import subprocess
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("pyyaml is required")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAPS = "references/test_lane_caps.yaml"
TREES = ["tests/valoria", "engine/season/tests", "engine/tests"]


def _run(*args):
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True)


def collected(marker=None):
    cmd = [sys.executable, "-m", "pytest", *TREES, "--collect-only", "-q", "-p", "no:cacheprovider"]
    if marker:
        cmd += ["-m", marker]
    r = _run(*cmd)
    return sum(1 for line in r.stdout.splitlines() if "::" in line)


def tracked_tools():
    return len([p for p in _run("git", "ls-files", "tools").stdout.splitlines() if p])


def cap_of(entry):
    return entry["base"] + sum(w.get("added", 0) for w in entry.get("warrants") or [])


def warrant_problems(name, entry, main_entry):
    out = []
    old = [w for w in (main_entry or {}).get("warrants") or []]
    for w in entry.get("warrants") or []:
        if w in old:
            continue
        if not (isinstance(w.get("added"), int) and w["added"] > 0 and w.get("batch")
                and len(str(w.get("behaviour", "")).strip()) >= 12):
            out.append(f"{name}: a new warrant needs batch, added > 0 and a behaviour (or caller) of 12+ characters: {w}")
    return out


def load_main(base_ref):
    r = _run("git", "show", f"{base_ref}:{CAPS}")
    if r.returncode != 0 or not r.stdout.strip():
        return None
    return yaml.safe_load(r.stdout)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--tighten", action="store_true", help="fold warrants into the base and set each base to its current count")
    ap.add_argument("--base-ref", default="origin/main")
    a = ap.parse_args(argv)
    path = os.path.join(ROOT, CAPS)
    caps = yaml.safe_load(open(path))
    main_caps = load_main(a.base_ref)
    counts = {lane: collected(lane) for lane in caps["lanes"]}
    total = collected()
    counts_tools = tracked_tools()
    problems = []
    if total != sum(counts.values()):
        problems.append(f"{total - sum(counts.values())} test(s) belong to no lane (collected {total}, lanes sum to "
                        f"{sum(counts.values())}): give each a lane in conftest.py")
    rows = [(lane, caps["lanes"][lane], counts[lane], ((main_caps or {}).get("lanes") or {}).get(lane)) for lane in caps["lanes"]]
    rows.append(("tools/", caps["tools"]["files"], counts_tools, (((main_caps or {}).get("tools") or {}).get("files"))))
    for name, entry, n, main_entry in rows:
        cap = cap_of(entry)
        problems += warrant_problems(name, entry, main_entry)
        if n > cap:
            problems.append(f"{name}: {n} > cap {cap}: unwarranted growth of {n - cap}. Retire {n - cap}, or add a warrant "
                            f"(batch, added, the game-state behaviour or caller) to {CAPS}")
        elif n < cap and not a.tighten:
            problems.append(f"{name}: {n} < cap {cap}: slack {cap - n}. Run `python tools/ci_test_lane_ratchet.py --tighten` "
                            f"and commit {CAPS}")
        if main_entry is not None:
            new_added = sum(w.get("added", 0) for w in entry.get("warrants") or [] if w not in (main_entry.get("warrants") or []))
            if cap > cap_of(main_entry) + new_added:
                problems.append(f"{name}: cap {cap} rose past main's {cap_of(main_entry)} by more than the new warrants add "
                                f"({new_added}); an edited base is not a warrant")
    print(f"{'lane':16s}{'tests':>7s}{'cap':>7s}")
    for name, entry, n, _ in rows:
        print(f"{name:16s}{n:7d}{cap_of(entry):7d}")
    if a.tighten:
        for lane in caps["lanes"]:
            caps["lanes"][lane] = {"base": counts[lane], "warrants": []}
        caps["tools"]["files"] = {"base": counts_tools, "warrants": []}
        with open(path) as fh:
            head = "".join(l for l in fh if l.startswith("#"))
        with open(path, "w") as fh:
            fh.write(head + yaml.safe_dump(caps, sort_keys=False, default_flow_style=None))
        print(f"tightened {CAPS}; commit it")
        problems = [p for p in problems if "slack" not in p]
    if problems:
        print("\nTEST-LANE RATCHET FAILED:")
        for p in problems:
            print("  - " + p)
        return 1
    print("test-lane ratchet: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
