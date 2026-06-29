"""Run the historically-grounded mass-battle GAUGE (gauge_mb.py: TESTS H1-H11 + CAV C1-C7)
against the CURRENT modular engine, all components wired. Reuses the gauge's history-derived
win-rate bands (references/historical/mass_battle_gauge_grounding.md) verbatim — the engine is
validated AGAINST history; a fail flags ENGINE divergence, not a band to lower.

Sample size via env GAUGE_N (default 60; gauge default is 120 @ SE~5pp).

Run (from repo root):
  PER_CELL=1 LANCHESTER_ENABLED=1 COMMAND_SIGMA_ENABLED=1 PC_BRACE_ENABLED=1 GAUGE_N=60 \
    python tests/sim/massbattle_battery/run_gauge.py
"""
import os, sys

for _k in ('PER_CELL', 'LANCHESTER_ENABLED', 'COMMAND_SIGMA_ENABLED', 'PC_BRACE_ENABLED'):
    os.environ.setdefault(_k, '1')

HERE = os.path.dirname(os.path.abspath(__file__))
SIM = os.path.join(HERE, '..')               # tests/sim — holds the mass_battle pkg AND gauge_mb.py
sys.path.insert(0, SIM)

# gauge_mb.py runs `exec(open(sys.argv[1]).read())` at import — point it at our package shim.
sys.argv = ['gauge_mb.py', os.path.join(HERE, 'engine_shim.py')]
import gauge_mb  # noqa: E402  (import triggers the engine exec into gauge_mb's namespace)

N = int(os.environ.get('GAUGE_N', '60'))
tests = gauge_mb.TESTS + gauge_mb.CAV_TESTS
print(f"### GAUGE against modular engine — N={N}, {len(tests)} scenarios (H1-H11 formation + C1-C7 cavalry)")
s = gauge_mb.run('single', tests, n=N)
m = gauge_mb.run('multi', tests, n=N)
print(f"\n==== modular-engine: single={s}/{len(tests)}  multi={m}/{len(tests)}  (N={N}; multi is the resolving mode) ====")
