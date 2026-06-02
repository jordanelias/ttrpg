"""sim_mb_sigma.py — SHIM. The mass-battle engine is now the mass_battle/ package.
This file re-exports the package's public API so existing callers (gauge_mb.py, which
exec()s this file) keep working unchanged. See mass_battle/engine.py for the MECHANICS
registry and module map. Behaviour-frozen refactor P-A (stages 1-5)."""
from mass_battle.engine import *
