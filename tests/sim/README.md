# tests/sim/ — frozen historical sim-run output archive

**Not the `sim/` package.** This directory holds frozen output (reports + one-off scripts) from
specific past simulation runs, e.g. `sim_mass_battle_SIM-MB-05.md`. It predates `sim/` — it once held
the monolithic `mc_v17.py` orchestrator that `sim/` replaced.

Treat files here as historical record, not executable specs or a place to add new sim code — new sim
development goes in `sim/`. This path is load-bearing for tooling: `ci_sim_fabrication_check.py`,
`atomization_rules.yaml`, and `lane_assignments.yaml` all path-match on the literal `tests/sim/` prefix,
so don't rename files here without checking those first.

See `sim/README.md` for the full disambiguation against `sim/` and `tests/sim_framework/`.
