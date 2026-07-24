"""Full honest-gauge runner with configurable flags (validation-loop closure). Runs the 20-row
history-grounded battery (gauge_mb) in multi mode and reports pass/OUT per row, so we can see how
far toward the Dupuy/Sabin bands the grounded mechanics move us. Flags via env (import-time)."""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_SIM = os.path.abspath(os.path.join(_HERE, '..', '..', 'tests', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

import gauge_mb as g  # noqa: E402
import mass_battle.config as c  # noqa: E402

if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    flags = f"STOCH_ROUT={c.PC_STOCHASTIC_ROUT} INTENT={c.PC_INTENT_RESOLUTION} CLOSE_RANKS={c.PC_CLOSE_RANKS}"
    print(f"=== honest gauge (multi, n={n}) — {flags} ===", flush=True)
    tests = g.TESTS + (g.CAV_TESTS if c.PER_CELL else [])
    npass = 0
    for t in tests:
        tid, label, sa, sb, ka, kb, lo, hi, dexp, *rest = t
        metric = rest[0] if rest else 'decA'
        r = g.matchup(sa, sb, ka, kb, 'multi', n=n)
        val = r['a'] if metric == 'rawA' else r['decA']
        inband = lo <= val <= hi
        npass += inband
        print(f"  {tid:4} {label[:30]:30} A%={r['a']:5.1f} B%={r['b']:5.1f} D%={r['d']:5.1f} "
              f"{metric}={val:5.1f} band={lo}-{hi} {'OK ' if inband else 'OUT'} t={r['t']:4.1f}", flush=True)
    print(f"  => PASS {npass}/{len(tests)}", flush=True)
