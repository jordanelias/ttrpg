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
    # [Fable-audit A2 fix, 2026-07-24] Delegate to gauge_mb.run() — the AUTHORITATIVE verdict. The prior
    # inline `inband = lo<=val<=hi` re-implemented the check and DROPPED both of run()'s guards: the
    # `dec_n>0` gate and the `draw_exp=='low' -> draw<30%` gate. Since matchup() returns the sentinel
    # decA=50.0 when dec_n==0, any all-draw row (e.g. R3) scored a FALSE pass (10 of 20 bands contain 50),
    # inflating the count. "One rule lives once" (CLAUDE.md §8): the verdict must live only in gauge_mb.run.
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    flags = f"STOCH_ROUT={c.PC_STOCHASTIC_ROUT} INTENT={c.PC_INTENT_RESOLUTION} CLOSE_RANKS={c.PC_CLOSE_RANKS} FRAC_POOL={c.PC_FRACTIONAL_POOL}"
    print(f"=== honest gauge (multi, n={n}) — {flags} ===", flush=True)
    tests = g.TESTS + (g.CAV_TESTS if c.PER_CELL else [])
    npass = g.run('multi', tests, n=n)   # prints per-row with the correct flag + guards; returns pass count
    print(f"  => (authoritative) PASS {npass}/{len(tests)}", flush=True)
