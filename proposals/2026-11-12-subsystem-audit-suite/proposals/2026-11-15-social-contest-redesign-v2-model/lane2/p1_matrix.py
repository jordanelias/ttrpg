"""P1: the matrix. 13 rows x {full, abridged} x effort {0,1,3,7} x bench {0,1,2,5,cohort,short,filtered} x hearers
{0,1,12} x addressed {b, None, cohort} x 5 attribute profiles x seeds. Records refusals/crashes, ends, mover legality,
outcome typing, act_margin per disposal.
    PYTHONHASHSEED=0 python lane2/p1_matrix.py [seeds]
"""
import sys, itertools, traceback
from collections import Counter, defaultdict
from common import *

SEEDS = int(sys.argv[1]) if len(sys.argv) > 1 else 2
D = dials.shipped()
prof = [("mid", "mid", "mid"), ("lo", "lo", "lo"), ("hi", "hi", "hi"), ("hi", "lo", "mid"), ("lo", "hi", "mid")]
errs = Counter(); err_ex = {}
ends = defaultdict(Counter); illegal = 0; untyped = 0; am_kind = defaultdict(Counter); n_ok = 0
bands = defaultdict(Counter); nexch = defaultdict(Counter)
am_none_cells = Counter()
for row, form, eff, bk, hk, addr, pr in itertools.product(data.ROW_IDS, ("full", "abridged"), (0, 1, 3, 7),
                                                         (0, 1, 2, 5, "cohort", "short", "filtered"), (0, 1, 12),
                                                         ("b", None, "cohort"), prof):
    P = people(*pr)
    key = (row, form)
    for s in range(SEEDS):
        try:
            inp = build_input(P, row, form, "argue", actor="a", addressed=addr, bench=bench_for(row, bk),
                              present=HEARERS[hk], effort=eff, dials=D)
        except Exception as e:
            sig = (row, form, type(e).__name__, str(e).split(":")[0] if isinstance(e, ValueError) else str(e)[:60])
            errs[("build",) + sig] += 1
            err_ex.setdefault(("build",) + sig, (row, form, eff, bk, hk, addr, pr))
            break
        try:
            out = proceed(inp, draw((row, form, eff, bk, hk, addr, pr, s), "a", "p1"), None)
            m, veto = act_margin(out, inp.type, inp)
        except Exception as e:
            sig = (row, form, type(e).__name__, str(e)[:80])
            errs[("run",) + sig] += 1
            err_ex.setdefault(("run",) + sig, (row, form, eff, bk, hk, addr, pr, traceback.format_exc().splitlines()[-3:]))
            continue
        n_ok += 1
        ends[key][out.ended] += 1
        nexch[key][len(out.exchanges)] += 1
        illegal += sum(1 for x in out.exchanges if not legal_move(inp, x))
        untyped += sum(1 for _, v in out.verdicts if not isinstance(v, Margin))
        am_kind[inp.type.disposal][type(m).__name__] += 1
        if m is None:
            am_none_cells[(row, form, inp.type.disposal, len(inp.speakers))] += 1
        b = None if m is None else degree(m)
        if veto and b in ("success", "overwhelming"):
            b = "failure(veto)"
        bands[key][b] += 1
print(f"ok runs {n_ok}; illegal movers {illegal}; non-Margin verdicts {untyped}")
print("\nREFUSALS / CRASHES (count = cells):")
for k, v in sorted(errs.items(), key=lambda kv: -kv[1]):
    print(f"  {v:6d} {k}\n         e.g. {err_ex[k]}")
print("\nact_margin type by disposal:", {k: dict(v) for k, v in am_kind.items()})
print("act_margin None cells:", dict(am_none_cells))
print("\nENDS / EXCHANGES / BANDS per (row, form):")
for key in sorted(ends):
    print(f"  {key}: ends={dict(ends[key])} nx={dict(sorted(nexch[key].items()))}\n      bands={dict(bands[key])}")
