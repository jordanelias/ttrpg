# Combat corpus recovery — 2026-06-29

**Provenance.** Recovered from five archives Jordan provided (`files.zip`…`files5.zip`) plus
`weapon-typologies-differential-reference.md`, on 2026-06-29. 41 files total; the 22 already present in the
repo (the 2026-06-13 `combat-bottomup` set, `loose_ends_register`, `combat_decision_docket`, etc.) were left in
place. The **16 genuinely-missing** documents + the **canonical composite `weapon_physics.py`** are preserved
here — this was real design work that never made it into the working tree ("where did the month of work go").
The three large generated HTML visualizations (`combat_legibility`, `combat_tick_by_tick`, `combat_flatten`)
were left in `~/Downloads/zipscan/` (regenerable workbench output; ~320KB).

## The canonical pieces (drive the re-architecture)

- **`weapon_physics_RECOVERED_composite_2026-06-22.py`** — the REAL bottom-up weapon model: composite iron-on-wood
  mass, pommel back-solve, `PoB`/`MoI`/`static_moment` derived from primitives `{mass, head_len, grip_len,
  pommel_kg, wclass, hilt}`, with the five §5 consumer replacements (`reach_term`, `heft_term`, `tempo_penalty`,
  `strdemand_term`). **Supersedes** the thin `designs/scene/combat_engine_v1/weapon_physics.py` written 2026-06-29.
- **`weapon_physics_preliminary_pob_2026-06-22.md` / `weapon_physics_calibration_and_wiring_2026-06-22.md`** — the
  PoB derivation + the calibration/wiring plan the module needs (the `pommel_kg` back-solve and sourced PoB).
- **`weapon_tradition_state_analytical_ledger_2026-06-22.md`** (37KB) — the analytical ledger.
- **`martial_morphology{,_distilled,_vol2,_vol3_efficacy}.md`** (~130KB) — the morphology corpus (foundational).
- **`combat_traditions_{integration_spec,morphology_critique,ners_distillation}.md`** — tradition↔engine wiring.
- **`combat_engagement_{engine_proposal,psychology_findings}.md`** — the psychology layer (mostly already live).
- **`percussion_authority.py`** — derived blunt authority (its `P_auth` core is already live in `core.py`).

## Still missing (not in any archive)

- **`weapon_calibrated_final.json`** — the per-weapon `pommel_kg` + expected `PoB_cm` the composite module's
  self-test loads (`/home/claude/cb/...`). The derivation is recoverable from
  `weapon_physics_preliminary_pob_2026-06-22.md`; the numeric singletons may need re-sourcing.

## Status

Salvaged for the combat-engine **re-architecture** (in progress 2026-06-29): a clean core engine + an
orchestrating wrapper + a single weapon-primitives source + weapon-gated subsystems + an abilities layer, then
every hand-authored top-down table derived from primitives. See `HANDOFF.md`.
