# Stage 1 combat-engine reconciliation — balance re-validation
**2026-06-16 · ED-935 · reconciles `combat_engine_v1` per `combat_reconciliation_plan.md` §2 Stage 1 · status: COMMITTED (Jordan-ratified)**

## Changes (3 mechanical drop-ins)
1. **μ-shift resolution** (directives #8/#13) — `core.resolve()`: base Ob fixed at `DECISIVE_OB`; the σ-leverage boosts the ROLL (`boost = soft_cap(net_σ)·sigma_n(pool)`), it does not shift the Ob. Replaces the floored `effective_ob` Ob-shift at both wrapper resolve sites. `r1.effective_ob` is display-only per its own docstring. [sigma_leverage_handoff §1; M_MAX=1.5, SIGMA_N_COEFF=0.8 verbatim from m1]
2. **P_auth** (directives #3/#6a) — `core.p_auth()` = `min(8, 9.5·(√mass·pob_frac)^0.30)` replaces the hand-set per-weapon `percussion` in `core.strike`. `pob_frac`/`mass` were dead weapon inputs; this is their consumer. [combat_residuals_pob_f5 §2]
3. **atk_sig→Concentration** (directive #12) — the consistency term reads the depleting Concentration tracker (`conc/5`, `conc = 3·Focus+2·Spirit`) instead of the static Focus stat.

## Balance re-validation (baseline HEAD vs reconciled; N 700–1500/cell, ±~2–3pp)
- **MIRROR:** 51.3 → 52.6 (Δ+1.3, within noise) — fairness preserved.
- **STAT spans COMPRESSED, not widened:** att +80→+66, str +75→+65, focus +30→+15, agi/end −7; cog +86→+84, history +87→+86 (Cog/History dominance persists). The μ-shift's correct (harder) overwhelming band slightly compresses outcomes — the OPPOSITE of the flagged spread-widening risk.
- **WEAPON:** small shifts (±8pp); draws up slightly (sabre 13→25%). Blunt unchanged (mace 6→6) — P_auth reproduces.
- **ABILITY:** vorschlag 49.8→49.5 (dead — seize still cut), indes 53.1→52.4, mezzo_tempo 52.7→50.9.
- **P_AUTH REPRODUCE:** 11/12 blunt damage cells identical; staff/none 9→10 (the doc's predicted ±1 continuous refinement).

## Honesty
- `[CONFIDENCE: high]` mirror/spread/weapon/ability/P_auth measured this session.
- The μ-shift's net effect is spread COMPRESSION + slightly more draws (canonical overwhelming is harder than the floored band). Whether that compression is desirable is a balance judgment, ratified by Jordan.
- `[GAP: wound-handicap not re-measured this session]` — the Class-A `−1D` mechanism is untouched by these diffs; the pool-size behaviour the handicap depends on is transitively validated by the History stat sweep (pool 7→13). Recommend a dedicated wound-sweep re-confirm.
- **DEFERRED (not in this commit):** the dead `POOL_FLOOR` cleanup (no-op, lives in shared `r8`); the dead seize lever / `vorschlag`+`sen_no_sen` retire-or-repoint (authored ability content — Jordan micro-call).
- **Stages 2–4** (continuous transmission re-baseline, puncture, continuum degree/QUAL, pool recompute, disposition-as-selection) await Jordan's decisions.
