#!/usr/bin/env python3
"""campaign_output_probe.py — the byte-identity control for a behaviour-neutral change.

WHY THIS EXISTS, AND WHY IT IS A TOOL RATHER THAN A SCRATCH FILE. Three commits on 2026-08-27
claimed to be output-neutral — ED-IN-0199 (engine_clock re-siting), ED-SC-0032 (the ladder
extension seam), and the intermediate injection step. Each claim was CHECKED, by running this
probe before and after and diffing. It lived in `/tmp` for the whole session, which means the
instrument that licensed three commits was one `rm` from gone and unreproducible by the next
reader. Jordan asked for the scratchpad to be committed; this is the half of it that is an
instrument rather than a record.

WHAT IT DOES. Runs five seeded campaigns (0/1/7/13/42) and both pinned batches (n=2 seed-0, n=8
seed-42), and dumps EVERY field of each result as sorted JSON — including `key_log_hash`, the
sha256 over the campaign's canonical KeyLog. `keys_emitted` runs 164-229 per campaign, so that
hash is a live signal here rather than a vacuous one: any change that perturbs the Key stream
moves it.

HOW TO USE IT, which is the whole contract:

    python tools/campaign_output_probe.py > /tmp/before.json     # on the unchanged tree
    ...make the change...
    python tools/campaign_output_probe.py > /tmp/after.json
    diff /tmp/before.json /tmp/after.json                        # empty == byte-identical

⚠ IT IS NOT A GATE AND MUST NOT BECOME ONE. Seven campaigns take ~80 seconds, and the goldens
that belong in CI already exist (`engine/tests/test_mc_v18_regression.py`,
`test_f7_smoke_oracle.py`, `test_parliamentary_bridge.py`, run by the `sim-regression` job).
This is the instrument for the question those goldens cannot answer on their own — "did MY change
move anything, at all, anywhere" — asked before the change is committed rather than after CI
reports which three goldens moved.

⚠ AND IT IS NOT A BALANCE CONTROL. An output diff tells you the RNG stream diverged; it says
nothing about whether balance shifted. For that the instrument is `tools/balance_oracle.py` at
n>=120 per arm, which is a different question and a different tool. Using this one to argue "no
balance change" would be the confounded-measurement failure CLAUDE.md §0.1 exists for.

⚠ ONE CAUTION LEARNED THE HARD WAY. Do not run this concurrently with an edit to the tree. A
capture taken while a source file changes underneath it measures neither state, and a diff
against it is worthless.
"""
from __future__ import annotations

import argparse
import dataclasses
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine.mc_v18 import run_campaign, run_batch  # noqa: E402

#: The seeds and batches captured. Chosen, not arbitrary: 0 and 42 are the two seeds CI's own
#: goldens pin, so a move here is traceable to a named golden; 1, 7 and 13 widen the sample past
#: the pinned pair so a change that happens to leave the pinned seeds alone still shows.
CAMPAIGN_SEEDS = (0, 1, 7, 13, 42)
BATCHES = (("batch_0_2", 2, 0), ("batch_42_8", 8, 42))
SEASONS = 50


def capture() -> dict:
    out = {}
    for seed in CAMPAIGN_SEEDS:
        out[f"campaign_{seed}"] = dataclasses.asdict(
            run_campaign(seed=seed, max_seasons=SEASONS))
    for label, n, base in BATCHES:
        out[label] = dataclasses.asdict(run_batch(n=n, base_seed=base))
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--compare', metavar='PATH',
                    help='diff against a previous capture instead of printing one; '
                         'exits 1 if anything moved')
    args = ap.parse_args(argv)

    now = capture()
    if not args.compare:
        json.dump(now, sys.stdout, indent=1, sort_keys=True, default=str)
        print()
        return 0

    with open(args.compare) as fh:
        before = json.load(fh)
    moved = [k for k in sorted(set(before) | set(now))
             if json.dumps(before.get(k), sort_keys=True, default=str)
             != json.dumps(now.get(k), sort_keys=True, default=str)]
    if not moved:
        print(f"[probe] IDENTICAL — {len(now)} captures, every field including key_log_hash")
        return 0
    print(f"[probe] MOVED: {', '.join(moved)}")
    for k in moved:
        b, a = before.get(k, {}), now.get(k, {})
        if isinstance(b, dict) and isinstance(a, dict):
            for f in sorted(set(b) | set(a)):
                if b.get(f) != a.get(f):
                    print(f"    {k}.{f}: {b.get(f)!r} -> {a.get(f)!r}")
    return 1


if __name__ == '__main__':
    sys.exit(main())
