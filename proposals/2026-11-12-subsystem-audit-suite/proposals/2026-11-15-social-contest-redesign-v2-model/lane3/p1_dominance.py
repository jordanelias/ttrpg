"""P1 dominance: strategy x strategy matrix of P(for carried), per row, symmetric mid people.
    PYTHONHASHSEED=0 python lane3/p1_dominance.py [n] [row ...]"""
import sys
from harness import run, person

n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
rows = sys.argv[2:] or ["conversation", "legal_trial", "arbitration"]
S = ["auto", "argue_best", "argue_true", "argue_evidence", "argue_solidarity", "press_always", "press_behind",
     "press_first", "divert", "divert_alt", "concede_early", "argue_once_rest", "rest", "mixed"]
A = person("a", pursuits={"x": 0.6}, convictions={"faith": 2})
B = person("b", pursuits={"y": 0.3}, convictions={"crown": 4})
for row in rows:
    M = {}
    for sf in S:
        for sa in S:
            r = run(row, A, B, sf, sa, n=n, label=f"p1:{sf}:{sa}")
            M[(sf, sa)] = r
    print(f"\n== {row} n={n}: P(for carried) rows=for strategy, cols=against strategy; SE<= {max(r['se'] for r in M.values()):.3f}")
    print(" " * 16 + " ".join(f"{s[:7]:>7}" for s in S))
    for sf in S:
        print(f"{sf:>16}" + " ".join(f"{M[(sf, sa)]['carry']:7.3f}" for sa in S))
    # dominance
    for sf in S:
        others = [o for o in S if o != sf]
        if all(all(M[(sf, sa)]['carry'] >= M[(o, sa)]['carry'] for sa in S) for o in others):
            print("  FOR strictly-weakly DOMINANT:", sf)
    for sa in S:
        others = [o for o in S if o != sa]
        if all(all(M[(sf, sa)]['carry'] <= M[(sf, o)]['carry'] for sf in S) for o in others):
            print("  AGAINST DOMINANT:", sa)
    # dominated: some other strategy beats it in every column by > 2SE
    for sf in S:
        for o in S:
            if o != sf and all(M[(o, sa)]['carry'] - M[(sf, sa)]['carry'] > 2 * (M[(o, sa)]['se'] + M[(sf, sa)]['se']) / 1.414 for sa in S):
                print(f"  FOR {sf} dominated by {o}")
                break
    for sa in S:
        for o in S:
            if o != sa and all(M[(sf, sa)]['carry'] - M[(sf, o)]['carry'] > 2 * (M[(sf, sa)]['se'] + M[(sf, o)]['se']) / 1.414 for sf in S):
                print(f"  AGAINST {sa} dominated by {o}")
                break
    # best responses to auto
    br_f = max(S, key=lambda s: M[(s, 'auto')]['carry'])
    br_a = min(S, key=lambda s: M[('auto', s)]['carry'])
    print(f"  best FOR vs auto: {br_f} {M[(br_f,'auto')]['carry']:.3f} (auto-auto {M[('auto','auto')]['carry']:.3f}); "
          f"best AGAINST vs auto: {br_a} {M[('auto',br_a)]['carry']:.3f}")
    aa = M[('auto', 'auto')]
    print(f"  auto-auto ends={dict(aa['ends'])} endside={dict(aa['endside'])} nx={aa['nx']:.2f} marks={aa['marks']}")
    for k in [("rest", "auto"), ("auto", "rest"), ("press_always", "auto"), ("auto", "press_always"), ("divert", "auto"), ("auto", "divert"), ("concede_early", "auto"), ("auto", "concede_early")]:
        r = M[k]
        print(f"  {k}: carry={r['carry']:.3f} ends={dict(r['ends'])} endside={dict(r['endside'])} marks={r['marks']}")
