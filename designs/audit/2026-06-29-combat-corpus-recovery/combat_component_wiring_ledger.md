# Combat Engine — Component Wiring Ledger
**2026-06-12 · grounded in code read this session · "ensure ALL components wired" accounting · Class-C, Jordan-vetoable**

`[SELF-AUTHORED — bias risk]` Status is from running/reading canonical code this session. Local-copy edits (`/home/claude/ew/`), **not committed** — engine is ED-900/904 canonical, re-ratification pending.

## A — WIRED THIS TURN (local copies, validated)

| Component | Was | Now | Validation | Lane |
|---|---|---|---|---|
| Resolution `r1.resolve_action` / `r8.resolve_phrase` | Ob-floor clip: display-only `eff_ob` + plain roll | **μ-shift**: `roll + net_boost(net_sigma,…)` vs **base Ob** | atom proof: MC ≡ canonical `p_success` ±0.1pp; the −6…−10pp saturation clip removed | C |
| 6 channel levers (`balance·measure·tempo·visual·leverage·tactile`) in `systems.py` | `TR.channel_weight(c.tradition,ch)` (eff_cw unrouted → abilities inert) | `TR.eff_cw(c,ch)` — **17/17 sites routed, 0 residual** | invariant-safe: no-ability ≡ `channel_weight` (PASS) | C* |
| 3 channel abilities (`staerke_schwaeche·misura·atajo`) | inert (no consumption site) | **LIVE** (fire through `eff_cw`) | activation proof: leverage 1.30→1.56 with Stärke-Schwäche equipped | C* |
| `precommit` channel | **no site at all** (fully inert) | 1 co-modulator in the defender intent-read (`feint_eval`, sen-sen-no-sen) | modulate-existing per your ruling; **attachment point flagged for veto** | C* |

`*` the channel sites live in `systems.py` (`designs/scene/combat_engine_v1/` = Lane **A**); the resolution atom is in `tests/sim/v32-combat-balance/` = Lane **C**. The wiring spans both — separate commits.

## B — ALREADY LIVE (no wiring needed)
Live levers `seize·counter_success·counter_select·anti_overcommit`; `mass`→percussion (`geometry`); `stamina_max`·`conc_max`·`act_cost`; `m7_facing_fov.emergent_facing_advantage` (facing/FoV exists); the state machine — initiative (Vor/Nach), `poise` (kuzushi), `bind_sigma`·`reach_sigma`·`mode_sigma`, half-sword switch, guard/`gap`/`clinch` primitives.

## C — DESIGN-GATED (machinery exists; a coupling spec is required before wiring)
These cannot be "wired" yet — they need a small mechanics spec (bottom-up from the existing machinery + top-down anchor), which is the next design step.

| Component | Existing machinery to couple into | The spec that's missing |
|---|---|---|
| **PoB / `pob_frac`** (your ruling: recovery + overcommit + swing) | `anti_overcommit`, `init_overcommit_loss`, `poise_factor` (recovery/exposure); `strike_damage` (swing) | how `pob_frac` maps to: commit-depth/overcommit exposure · recovery rate after a swing · swing-weight (composing with `mass`, not double-counting) |
| **F5 wound model** (your ruling: stamina · concentration · execution) | `stamina_max`, `conc_max`, the resolution `net` | the per-wound penalty curve to each target (replacing the deb405b944 −1D-pool path) |

## D — DESIGN + BUILD (new)
| Component | Hook that exists | What's unbuilt |
|---|---|---|
| **F1 grid / facing** | `m7_facing_fov` (emergent facing advantage) + `init_overcommit_loss(exposure)` | the square grid, facing rules, flank/surround bonus, side-rear reaction penalty, ally-adjacent occupied bonus, projectile **physics-distance → hit + crit**. Largest piece. |

## E — BLOCKED ON UNBUILT LEVERS
`reopen` / `disengage` abilities target levers that **do not exist** (`ability_armature §7`). Cannot be wired until those levers are built — a separate gap from the eff_cw pass.

## F — STAGED (validation + landing)
1. **Full phrase-level parity re-baseline** — mirror symmetry + strength/history monotonicity + weapon-matchup acceptance band (0.40–0.60). Needs the full module tree (`m5_stance_reaction_coherence` + transitive) and `sim_gate('combat')`'s canonical reads (`core_engine`, params/core). A clean combat-sim session.
2. **Commit + re-ratification** — Lane C (`r1`/`r8`/`systems` if counted there) + Lane A (`systems.py` channel sites; m1 μ-shift doc declaration). Engine is ED-900/904 → **your re-ratification** before any commit. μ-shift is convergence-to-canon (the analytic was already μ-shift), so it's a confirm, not new behaviour.

## G — Sequence to "ALL wired"
1. **Now done:** A (resolution + channels + 3 abilities + precommit), validated at atom/unit level.
2. **Next (validation):** F.1 parity re-baseline in a clean `sim_gate('combat')` session → then F.2 commit + re-ratify.
3. **Then (design→wire):** C — write the PoB and F5 coupling specs, then wire into the existing machinery.
4. **Then (build):** D — F1 grid/facing.
5. **Gap:** E — build `reopen`/`disengage` levers, then wire their abilities.

## Citations
- `combat_engine_v1/tradition.py` (`eff_cw`, `ability_factor`, `channel_weight`, the wiring-path docstring), `systems.py` (the 17 channel sites; `anti_overcommit`/`init_overcommit_loss`/`poise_factor`/`stamina_max`/`conc_max`), `core.py`, `geometry.py`.
- `tests/sim/v32-combat-balance/r1_sigma_resolution.py` + `r8_parity_harness.py` (resolution atom; r8 dep tree r2/r5/m1/m7/m3), `m1_dice_sigma_core.py` (`eff_ob` DISPLAY-ONLY, `p_success`/`net_boost` μ-shift).
- `designs/audit/2026-06-09-personal-combat-comprehensive/comprehensive_analysis_personal_combat.md` (F2/F4/F5/F7).
