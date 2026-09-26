"""`season.harness` — what RUNS the model: probes, the case runner, the corpus sweep, the register
gate, the sole emitter, and the before-and-after command.

The model itself (`state/`, `loop/` and `decision/` — `shape.py` was decomposed away at step 9),
the seam it dispatches through (`seam/`, not only `seam/wrappers/combat.py`) and the channel it
records on (`trace_log`) stay one level up: this package depends on those and nothing there
depends on anything here.
"""
