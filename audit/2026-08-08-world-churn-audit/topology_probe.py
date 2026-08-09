#!/usr/bin/env python3
"""Topology probe for the declared Key graph (ED-IN-0149).

Falsifier for every topology number quoted in 06_master_synthesis.md. Run:
    python audit/2026-08-08-world-churn-audit/topology_probe.py

It measures the DECLARED graph (references/key_graph.json), which is a paper
graph: a declaration here is not evidence of runtime traffic (00_findings D7).
Thresholds are stated in the output so a reader can see what each label means
rather than inferring it.

WILDCARD HANDLING — load-bearing, and the source of a correction. key_graph.json
carries 56 entries, one of which is the literal key `"*"`: a wildcard SUBSCRIPTION
pattern declared in module_contracts by articulation_layer and fieldwork_knots
(`well_formed: false`, no producers). It is not a key type. Counting it as one
inflates the key count 55->56, the consume-declaration total 125->127, and
articulation_layer's in-degree 43->44 -- and it flips fieldwork_knots from a pure
source into a bidirectional module, changing "16 of 27 modules consume nothing"
into 15. This probe EXCLUDES it by default and reports the inflated basis
alongside, so neither figure can be quoted without its basis.
"""
import collections
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]


def load():
    return json.loads((ROOT / "references" / "key_graph.json").read_text())


def name(entry):
    return entry if isinstance(entry, str) else entry.get("module")


WILDCARD = "*"


def main():
    graph = load()
    all_keys = graph["keys"]
    keys = {k: v for k, v in all_keys.items() if k != WILDCARD}
    producers = {k: {name(p) for p in (v.get("producers") or [])} for k, v in keys.items()}
    consumers = {k: {name(c) for c in (v.get("consumers") or [])} for k, v in keys.items()}

    out = collections.defaultdict(set)
    inp = collections.defaultdict(set)
    for kt in keys:
        for m in producers[kt]:
            out[m].add(kt)
        for m in consumers[kt]:
            inp[m].add(kt)
    modules = sorted({m for m in set(out) | set(inp) if m})

    pure_source = [m for m in modules if out[m] and not inp[m]]
    pure_sink = [m for m in modules if inp[m] and not out[m]]
    bidi = [m for m in modules if inp[m] and out[m]]

    print("== MODULE DEGREE ==")
    print(f"modules declared: {len(modules)}")
    print(f"pure sources (emit, consume nothing): {len(pure_source)}")
    print(f"pure sinks   (consume, emit nothing): {len(pure_sink)}")
    print(f"bidirectional:                        {len(bidi)}")
    print()
    print("pure sources:", ", ".join(sorted(pure_source)))
    print("pure sinks:  ", ", ".join(sorted(pure_sink)))
    print()
    print("bidirectional (module, in-degree, out-degree, ratio in:out):")
    for m in sorted(bidi, key=lambda m: -len(inp[m])):
        print(f"  {m:20s} in={len(inp[m]):3d} out={len(out[m]):3d}")

    total_consume = sum(len(consumers[k]) for k in keys)
    total_produce = sum(len(producers[k]) for k in keys)
    ranked = sorted(modules, key=lambda m: -len(inp[m]))
    top4 = ranked[:4]
    top4_share = sum(len(inp[m]) for m in top4)
    print()
    print("== CONCENTRATION ==")
    print(f"consume-declarations total: {total_consume}")
    print(f"produce-declarations total: {total_produce}")
    print(
        f"top 4 consumers hold {top4_share}/{total_consume} "
        f"({100 * top4_share / total_consume:.0f}%): "
        + ", ".join(f"{m}={len(inp[m])}" for m in top4)
    )

    # Key fan-out classification. Thresholds are declared, not assumed.
    THRESH = "orphan: 0 consumers | seam: exactly 1 | channel: 2-3 | nexus: >=4"
    buckets = collections.Counter()
    nexus = []
    for kt in keys:
        n = len(consumers[kt])
        b = "orphan" if n == 0 else "seam" if n == 1 else "channel" if n <= 3 else "nexus"
        buckets[b] += 1
        if b == "nexus":
            nexus.append((kt, n))
    print()
    print("== KEY FAN-OUT ==")
    print(f"key types: {len(keys)}   ({THRESH})")
    for b in ("orphan", "seam", "channel", "nexus"):
        print(f"  {b:8s} {buckets[b]:3d}")
    print("nexus keys:", ", ".join(f"{k}({n})" for k, n in sorted(nexus, key=lambda x: -x[1])))

    orphan_prod = [k for k in keys if not producers[k]]
    print()
    print("== PRODUCERLESS ==")
    print(f"key types with no declared producer: {len(orphan_prod)}/{len(keys)}")

    # The inflated basis, printed so a mismatch is diagnosable rather than mysterious.
    if WILDCARD in all_keys:
        w_cons = {name(c) for c in (all_keys[WILDCARD].get("consumers") or [])}
        print()
        print("== WILDCARD (excluded above) ==")
        print(f'the literal "{WILDCARD}" entry is a subscription pattern, not a key type; '
              f"consumers: {', '.join(sorted(w_cons))}")
        print(f"counting it would give: key types {len(all_keys)}, "
              f"consume-declarations {total_consume + len(w_cons)}, "
              f"and would move fieldwork_knots out of the pure-source set.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
