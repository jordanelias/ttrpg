"""W-D, CHUNKED. Same measurement, split so no single process runs long enough to be reaped.

⚠ THIS IS A SCHEDULING SPLIT AND NOTHING ELSE. `sweep_arm` is `wd_acceptance.sweep_arm`, called on
a SLICE of the same case list in the same order with the same seed and the same fixtures; the
chunks are concatenated by `wd_collect.py`. Two full-corpus runs of `wd_acceptance.py` were killed
silently at ~18 minutes with no traceback and no output, which is why the work is now in pieces
small enough to finish. Nothing about the experiment changed.

Usage: python wd_chunk.py <mode> <default|narrow> <start> <end>
"""
from __future__ import annotations
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import wd_acceptance as W

if __name__ == "__main__":
    mode, slots, a, b = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    r = W.sweep_arm(mode, slots, cases=W.CASES[a:b])
    r["chunk"] = [a, b]
    out = Path(__file__).parent / "runs" / f"wd_chunk_{slots}_{mode}_{a}_{b}.json"
    json.dump(r, open(out, "w"), indent=1, default=str)
    print(f"{slots}/{mode}[{a}:{b}] cases {r['n_cases_ok']}/{r['n_cases_attempted']} "
          f"probed {r['probed']} nolive {r['no_live_window']} inert {r['inert']} "
          f"genuine {r['genuine']} diverged {r['diverged']} [{r['seconds']}s] -> {out.name}")
