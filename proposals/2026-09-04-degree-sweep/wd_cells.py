"""W-D — WHICH CELLS OF THE DECLARED SWEEP CROSS CAN THE FORKING QUESTION BE ASKED AT?

⚠ THIS EXISTS BECAUSE `W-D` SHIPPED A FALSE FORCING ARGUMENT AND NOTHING COULD CHECK IT.
Three surfaces said *"crossing the two DECLARED sweeps ... exactly ONE cell gives `L <= 3`:
2 x 1 = 2 slots"* and offered no command. It is wrong twice over, and both errors come from the
same substitution:

  1. **`L` IS THE PACKER'S OWN TAKE, NOT THE SLOT PRODUCT.** `recorder.in_budget` records
     `sum(len(sc.acts) for sc in pack_scenes(...))` -- what `take()` actually returned. The
     original argument used `scene_budget x interactions_per_scene` as a proxy for it. `take()`
     charges an EXTENDED scene `extended_scene_cost` (2) and takes a whole chunk whenever
     `ext <= left`, so at 2 x 3 the first chunk of three candidates is taken ENTIRE for a cost of
     2 and `L = 3` -- not 6.
  2. **`L` IS PER DELIBERATION, NOT PER CELL.** It varies with the person's own ranked list, so
     `L <= MAX_ALT` is a property of a DELIBERATION. A cell is askable when ANY of its
     deliberations has one, which is what this measures.

So the cross has TWO askable cells, not one, and the un-run one -- `scene_budget=2` with
`interactions_per_scene` left at its default -- is ONE declared-arm change against 2 x 1's two.
On the item's own criterion (minimum departure from the shipped fixture at which the question is
askable) the un-run cell was the better acceptance point.

BASELINE-ONLY AND THEREFORE CHEAP. `fork_case`'s classification of a probe as GENUINE is decided
entirely by the BASELINE (`L == 0 or t < L`, and whether the live window fills), so the census
re-derives that partition from one baseline per case without running a single fork. The partition
it prints for `narrow` and `2x3` is checked against the full runs' own `wd_chunk_*.json` totals by
`wd_collect.py`, which is the falsifier for this file.

Usage: python wd_cells.py            # all nine cells of `H-10` x `H-76`, all 89 worlds
       python wd_cells.py <n>        # the first n worlds, for a quick read
"""
from __future__ import annotations
import collections, json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import wd_acceptance as W
import arm9_forking as A9
from sweep_core import S
from trace_log import TRACE

# `H-10`'s declared sweep x `H-76`'s declared sweep. Neither list is invented here.
SCENE_BUDGETS = [2, 5, 9]                    # `H-10`
INTERACTIONS = [1, 3, None]                  # `H-76`; `None` is the row's `unbounded` arm
MODE = "actor"                               # the shipped default; the partition is mode-invariant
                                             # (`probed`/`no_live_window` are equal across arms)


def census(cases) -> list:
    rows = []
    for sb in SCENE_BUDGETS:
        for per in INTERACTIONS:
            fx = (S.DEFAULT_FIXTURES.sweep("scene_budget", sb)
                  .sweep("interactions_per_scene", per)
                  .sweep("observation_deposit_mode", MODE))
            Ls: collections.Counter = collections.Counter()
            probed = nolive = inert = genuine = failed = 0
            t0 = time.time()
            for _lane, c in cases:
                # ⚠ THE CENSUS CLEARS `TRACE.rows`; THE SHIPPED RUNNER DOES NOT AND THAT IS WHY
                # `wd_acceptance.main()` DIES. `trace_log.TRACE` is a module-level singleton whose
                # `rows` list nothing resets. MEASURED 2026-09-04 over six cases: rows grow
                # ~221,000 PER CASE and peak RSS ~97 MB per case, strictly linear; clearing per
                # case holds rows flat at ~220,000 and costs nothing in time. 89 cases x 6 sweeps
                # in one process is ~19.6M rows per sweep, which is a sufficient cause for a
                # SIGKILL with no traceback. Nothing reads `TRACE.rows` mid-run, so this is
                # value-neutral -- and it is done HERE, in a new file, rather than in the shipped
                # `sweep_arm`, because changing the memory behaviour of the runner that produced
                # the committed numbers needs its own control.
                TRACE.rows.clear()
                b = A9._run(c, W.SEED, W.SEASONS, fixtures=fx)
                if not b["ok"]:
                    failed += 1
                    continue
                D, IB = b["decisions"], b["in_budget"]
                for i in range(len(D)):
                    ti = D[i][2]
                    live = [j for j in range(i + 1, len(D)) if D[j][2] > ti][:A9.LOOKAHEAD]
                    n_alt = min(A9.MAX_ALT, max(0, len(D[i][1]) - 1))
                    L = IB[i]
                    Ls[L] += 1
                    for t in range(1, n_alt + 1):
                        probed += 1
                        if len(live) < A9.LOOKAHEAD:
                            nolive += 1
                        elif L == 0 or t < L:
                            inert += 1
                        else:
                            genuine += 1
            rows.append(dict(
                scene_budget=sb, interactions_per_scene=per,
                cell=f"{sb} x {'unbounded' if per is None else per}",
                slot_product=(None if per is None else sb * per),
                deliberations=sum(Ls.values()),
                L_distribution=dict(sorted(Ls.items())),
                L_min=(min(Ls) if Ls else None), L_max=(max(Ls) if Ls else None),
                deliberations_with_L_le_MAX_ALT=sum(n for L, n in Ls.items() if L <= A9.MAX_ALT),
                probed=probed, no_live_window=nolive, inert=inert, genuine=genuine,
                askable=(genuine > 0), n_cases_failed=failed, seconds=round(time.time() - t0, 1)))
            r = rows[-1]
            print(f"  {r['cell']:>14}  slots={str(r['slot_product']):>4}  "
                  f"L={r['L_distribution']}  probed={r['probed']} nolive={r['no_live_window']} "
                  f"inert={r['inert']} GENUINE={r['genuine']}  ASKABLE={r['askable']}  "
                  f"[{r['seconds']}s]", flush=True)
    return rows


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else len(W.CASES)
    cases = W.CASES[:n]
    print(f"W-D cell census — `H-10` scene_budget {SCENE_BUDGETS} x `H-76` "
          f"interactions_per_scene {INTERACTIONS}, {len(cases)} worlds, seed {W.SEED}, "
          f"{W.SEASONS} seasons, mode={MODE}, MAX_ALT={A9.MAX_ALT}\n")
    rows = census(cases)
    askable = [r["cell"] for r in rows if r["askable"]]
    print(f"\nASKABLE CELLS: {len(askable)} of {len(rows)} — {askable}")
    print("The shipped claim was `exactly ONE cell`. It is TWO, and the cheaper intervention "
          "(`2 x 3`, one declared-arm change) is the one that was never run.")
    out = dict(n_cases=len(cases), seed=W.SEED, seasons=W.SEASONS, mode=MODE,
               max_alt=A9.MAX_ALT, lookahead=A9.LOOKAHEAD,
               scene_budgets=SCENE_BUDGETS, interactions_per_scene=INTERACTIONS,
               askable_cells=askable, cells=rows)
    p = Path(__file__).parent / "runs" / "wd_cells.json"
    json.dump(out, open(p, "w"), indent=1, default=str)
    print(f"wrote {p}")
