"""engine/ — Valoria executable-model primary (ED-IN-0071 P3).

Python package holding the engine CORE (substrate, autoload, cross_scale, mc_v18)
moved from sim/ (Phase A), beside the typed engine_params/ export and the prose
params/ tables (data dirs, not subpackages). Per-subsystem sims live under
sim/ (-> systems/<subsystem>/sim/ in P4) and depend UPWARD on this core.
"""
