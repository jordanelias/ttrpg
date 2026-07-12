# Deprecated skills

Skills retired from `skills/` but preserved for history.

- **valoria-orchestrator** — the session/bootstrap orchestrator from the retired `/home/claude`
  GraphQL harness (PAT management, `github_ops.py` downloads, `assert_bootstrap()`/`safe_commit`,
  `valoria_hooks.py`). Superseded by the Claude Code-native model (HANDOFF.md decision, 2026-06-24):
  enforcement now lives once in `tools/` and runs in CI + local hooks; the working tree is the source
  of truth, so session-start GitHub fetching and bespoke commit wrappers are no longer used. Kept
  here as a reference only — do not invoke; its scripts assume the dead sandbox.
- **valoria-combat-simulator** (retired 2026-07-12, ED-IN-0039) — the standalone personal-combat
  Monte-Carlo skill. Its bundled `scripts/combat_sim.py` was a hand-hardcoded 9-weapon model frozen
  2026-03-31 (Short/Long × Light/Heavy Cut/Blunt), fully superseded by the current combat engine's own
  balance harness, `designs/scene/combat_engine_v1/workbench/balance.py` — an actively-maintained,
  51-weapon (40 added in the 2026-07-02 morphology expansion, plus the original 11),
  Wilson-CI-validated instrument (weapon/attribute/tradition/armour sweeps) that reuses the canonical
  `fight()` resolver directly instead of a hand-maintained parallel model. The skill's own
  `## Input Validation` also pointed at `params/combat.md`, deprecated since 2026-06-04. Combat
  balance work now routes directly through `workbench/balance.py` (see its own docstring for CLI
  usage: `python workbench/balance.py [weapon|attr|tradition|all] [n]`) — no skill wrapper needed.
  **Known coverage gap (found by adversarial review, 2026-07-12):** `balance.py`'s CLI only exposes
  curated sweep modes (baseline-vs-field, marginal-attribute, tradition-field, armour-matrix); it has
  no mode for the retired skill's full pairwise cross-product (every valid build vs. every other
  valid build). The underlying `winrate(specA, specB, cfg, n)` function is trivially capable of an
  arbitrary two-build matchup — wiring a full-matrix CLI mode is a small follow-up if that comprehensive
  view is ever needed again; not built as part of this retirement.
  Kept here for reference only; do not invoke or resurrect `combat_sim.py`.
