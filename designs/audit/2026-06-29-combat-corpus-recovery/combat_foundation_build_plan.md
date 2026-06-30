# Personal-Combat Redesign — Build Plan & Handoff
**2026-06-12 · stage 1a COMPLETE (change-surface read + corrected) · stage 1b READY · Class-C, Jordan-vetoable**

`[SELF-AUTHORED — bias risk]` Grounded in code read this session; the re-baseline + re-ratification are the gates, not done here.

## 0 — Confirmed by "proceed" (taken as authorized; correct me if wrong)
- **F4 = option (ii): μ-shift** (genuine σ-leverage), not the (i) doc-fix.
- **F5 = three-target wound model**: wounds penalise **stamina · concentration · execution success-rate** (replacing flat −1D-to-pool).
- **`precommit` wiring = modulate-existing pre-contact reads only** (the safe option; does NOT re-introduce the ratified-cut seizure site).

## 1 — Corrected change surface (the stage-1a finding)
The canonical resolution atom is **NOT** in Lane-A `designs/scene/combat_engine_v1/` — that's a wrapper. It is:

| What | Where | Lane |
|---|---|---|
| **Ob-floor clip** `effective_ob = max(OB_FLOOR, eff_ob(base_ob,pool,net_sigma))` | `tests/sim/v32-combat-balance/r1_sigma_resolution.py:104` | **C** |
| roll, degree bands, `resolve_action` | same r1 module | **C** |
| `resolve_phrase` (the parity harness driving net_sigma from channels) | `tests/sim/v32-combat-balance/r8_parity_harness.py:126` | **C** |
| `eff_cw()` (defined, **unrouted**) + channel weights | `combat_engine_v1/tradition.py:131` | **A** |
| `effective_ob` wrapper | `combat_engine_v1/core.py:10` | **A** |

**Implication:** the foundation is **Lane-C-primary** (the r1/r8 math) with a Lane-A tail (tradition.py `eff_cw` routing + the m1 doc declaration). Write-disjoint → the Lane-C engine+re-baseline and the Lane-A doc land in separate sessions. The canonical resolver math living in the `v32-combat-balance` (dead-named) dir is itself a hygiene flag (the live r1/r8 are NOT dead despite the dir name) — note for the J-4 shadow/relocation discussion, do not relocate mid-change.

## 2 — F4 μ-shift implementation spec
**Goal:** apply σ-leverage as a shift in the *net* (μ-space) instead of shifting+flooring the *Ob*, so saturated advantage is no longer clipped (the −11pp forfeit at pool 6 σ=+3), while reproducing current behaviour at TN7 up to the floor.

**Still to read before editing** (do NOT implement from memory): `eff_ob`, `OB_FLOOR`, `roll_net_continuous`, `resolution_pool`, `state_gated_net_sigma`, and the m1 modifier spec (the Ob-shift definition to invert). All in r1 + `m1_*` under the same dir.

**Edit (r1):** replace `ob = max(OB_FLOOR, eff_ob(...))` / `net = roll_net_continuous(...)` with `ob = max(OB_FLOOR_BASE, base_ob)` / `net = roll_net_continuous(...) + mu_shift(net_sigma)`, where `mu_shift` is the net-space equivalent of the current `eff_ob` Ob-shift (derive by inversion so the two match at TN7). Keep a sanity floor on base Ob, drop the floor *on the advantage path*.

**Acceptance:** identical degree-distribution to current at non-saturated σ; at saturated advantage, no clip (the preserved +leverage); disadvantage path unchanged.

## 3 — F2 `eff_cw` lever-wiring (the "same pass" as F4)
The channel levers are *registered but inert until routed through `eff_cw()` (~21 sites)*. **Locate the 21 sites** (grep `channel_weight`/direct channel reads across `systems.py`, `r1`, `r8`) and route each through `tradition.eff_cw(c, channel)`. `precommit` routes into existing pre-contact reads only. This is what makes tradition weapon-affinity actually fire (and is where tradition σ-leverage becomes real → F4 and this are one plumbing pass).

## 4 — Re-baseline battery (must pass before re-ratification)
Assemble the full v32-combat-balance module set (r1, r8, m1, m5, r2, WoundTracker, stamina, strike_damage, …), `h.sim_gate()`, then re-run **under μ-shift + live channels**:
- r8 parity harness: mirror match → ~50/50 (the parity invariant).
- Probes A/B/C from the 2026-06-09 analysis (σ-monotonicity, the saturation curve now *without* clip, wound concavity).
- Degree-band floors + the 5% upset floor + MaxWounds≤3/felled caps.
- §3.2 invariant set generally.
Document any intended shift (the saturation path *should* change — that's the point); everything else must hold.

## 5 — Gates that remain (do NOT pass without Jordan)
- **Re-ratification:** the engine is CANONICAL (ED-900/904). The μ-shift + `eff_cw` changes need Jordan's re-ratification of the new baselines before any commit.
- **J-9 cross-check:** confirm this μ-shift matches the **mass-battle** μ-shift convention (cross-scale consistency); coordinate with the mass-battle owner (parallel-owned).
- **Still-open decisions (gate the LATER steps, not the foundation):** D-α (keep-8 / replace-6 / coexist), **PoB keep-or-cut**, the orthogonal second tradition-slot. These gate tradition tuning / the PoB axis / weapon instantiation — not stage 1b.

## 6 — Lane & ID discipline
- Lane C (r1/r8/systems μ-shift + `eff_cw` sites + re-baseline): commit scope `simulation`; EDs from 970–999, **verify against live ledger max 1012** (the `id_reservations.yaml` pointer is stale).
- Lane A (tradition.py `eff_cw` + m1 μ-shift declaration): separate session, scope `fix`/`editorial`.
- Ruling-record (the five rulings as ED entries, D-α/PoB flagged `[OPEN]`): a Lane-A editorial commit — recommend landing this as the documented foundation **once D-α/PoB are closed**, so it isn't a holey record.

## 7 — Next action (stage 1b)
Fresh focused session: fetch the full v32-combat-balance module set + m1 → `sim_gate` → prototype μ-shift + route `eff_cw` on **local copies** → run the §4 battery → present results for your re-ratification. No canonical commit until §5 clears.

## Citations
- `tests/sim/v32-combat-balance/r1_sigma_resolution.py` (effective_ob/OB_FLOOR/resolve_action), `r8_parity_harness.py` (resolve_phrase/channel net_sigma).
- `combat_engine_v1/core.py` (wrapper), `tradition.py` (eff_cw, inert levers), `systems.py`, `config.py`.
- `designs/audit/2026-06-09-personal-combat-comprehensive/comprehensive_analysis_personal_combat.md` (F4/F5/F7 + the probe battery).
