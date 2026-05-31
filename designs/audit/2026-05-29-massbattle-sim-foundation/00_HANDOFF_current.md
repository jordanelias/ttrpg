# ⚠️ CURRENT MASS-BATTLE HANDOFF (authoritative)
**This supersedes `tests/sim/HANDOFF_massbattle_foundation_M3.md`, which is STALE** (it still directs the refuted D-C/v14/counter-tuning path). Read THIS file. The stale one is left only for git history; do not follow it.

---

# HANDOFF — Mass Battle Sim (M3 COMPLETE → primitive-build phase)

**Updated:** 2026-05-29 (supersedes the prior M1/M2-done version — that version's D-C/v14/counter-tuning direction is REFUTED, see below)
**Status:** M3 (counter investigation) DONE. Next: bottom-up primitive build (workplan doc 13), pending Jordan scope.
**Authoritative record:** `designs/audit/2026-05-29-massbattle-sim-foundation/` docs **07–14** (committed). This handoff is the pointer; the docs are the detail.

---

## WHERE WE ACTUALLY ARE (read this first — the prior handoff was stale)

The prior version of this handoff said "M3 next; D-C leaning (v14 geometry is the path); 3c tune counters in-band." **All of that is refuted/retired.** What M3 actually found:

1. **Counters do NOT emerge at realistic casualties on the v9–v25 lineage.** Formation counters only separated at *catastrophic* casualties (~60–100% loser); at the historical ~26%/side, every matchup is ~5/11. (doc 07)
2. **Top-down counter mechanisms are RETIRED.** Damage-multiplier counters (v26/v30), δσ counter tables (v31/v32), and the GappedLine geometry change were all **top-down crutches** — encoding the answer, not deriving it. Jordan's standing rule: **counters emerge from bottom-up primitives ONLY; history is the validation gate, never an input.** No counter tables, no per-matchup δσ, no shape-keyed damage multipliers. (docs 08/09/10, retired)
3. **Evaluation method corrected:** all win-rates must use **Wilson 95% CI** (n≥300 pooled ≥3 seed banks), not bare Monte-Carlo frequencies. Under CIs, the best damage-mult engine is **6/11**, not the 9–10 earlier claimed by point estimate. (doc 10)
4. **Architecture (Jordan, 2026-05-29):** *σ-leverage is the exchange-probability substrate; attrition→rout is the outcome spine; they compose.* doc 10's σ-leverage 2/11 was an injection-location error (δσ at contested Ob collided with geometry pool-asymmetry), NOT an architecture failure. Fix: inject δσ on the *exchange win-probability*, KEEP the attrition→morale→rout spine (it is historically correct and already in the engine). (doc 13 §0)
5. **A mechanical bug:** the `unit_b` (second positional arg) wins ~55% of *tied rout-threshold* ticks — a pure order-of-evaluation artifact in the erosion/rout loop, manifesting on Line/GappedLine (full-width contact). Deterministic fix (pre-tick morale snapshot → simultaneous rout) VERIFIED (45→49/51%, CI-symmetric). NOT yet applied to a committed engine. (doc 11)

## THE DIAGNOSIS (doc 12) — why ~5/11, and what's missing

Two root gaps prevent bottom-up counter emergence:
- **Root Gap A — weapon×armour×reach×mount collapsed to flat scalars.** Canon (§A.2 + DR tables) specifies a full LC/HC/LB/HB weapon × None/Light/Medium/Heavy armour matrix, reach, cavalry +5. The sim reduces all to flat `power`/`dr`. **Cavalry is a stub** (`troop_type='cavalry'` never branched) → **Cannae is unmodellable bottom-up**; **reach is absent** → Pydna's phalanx physics missing.
- **Root Gap B — spatial primitives too coarse.** Octagon facing is 3-zone *averaged* over contact cells; speed is integer 0/1/2; formation-break-under-pressure (`resolve_internal_collisions`) is implemented but NOT invoked. Fine local advantages (wedge tip, oblique angle, flank buckling) wash out.

**Cross-scale key:** the weapon/armour/reach matrix + a wound-gate tracker (the rout isomorph) **already exist, validated, at personal scale** (`tests/sim/v32-combat-balance/` M3 `WEAPON_ARMOR_MOD`, M9 `armor_resist`/`reach_ob_shift`/`WoundTracker`). §A.2 says mass battle inherits them. The gap is an unbuilt scale-bridge — lift, don't rebuild. This couples to the σ-leverage architecture (the personal layer IS σ-leverage).

## THE PLAN (doc 13) — phased, bottom-up, validate each vs historical bands, stop when met

- **Phase 0 (SAFE NOW, no decision):** apply the doc-11 simultaneous-rout fix + lock the Wilson-CI validation protocol.
- **Phase 1:** σ-leverage exchange head on the attrition spine (the corrected doc-10 — δσ on exchange win-probability).
- **Phase 2:** inherit weapon×armour×reach from the personal layer (Root Gap A).
- **Phase 3:** cavalry (Root Gap A; unlocks Cannae bottom-up).
- **Phase 4:** finer facing/velocity + invoke formation-break (Root Gap B).
- **Phase 5:** terrain (history-pervasive — Pydna/Cannae/Leuctra/Hastings all hinge on ground).
- **Phase 6:** command radius / reserves / fatigue / full rout-contagion.
- **Phase 7 (parallel):** campaign supply / service duration.
- Critical path **0→1→2→3** delivers the showpiece counters from physics. This IS the σ-leverage migration, primitive-first.

## OPEN JORDAN DECISIONS (blocking Phase 1+)
- Confirm the phase plan + critical path; whether to build Phases 1–3 in **σ-leverage form** (couples to the architecture decision in doc 10 §6).
- Authorize the personal→mass primitive lift.
- Whether to promote any session findings to ED/PP entries (deferred — canon-authority; the bug, the corrections, the primitive gaps are candidates).
- The §A.6 counter values proposed in 08/09 are NOT committed to `mass_battle_v30.md` (owner contract) and may be moot if Phase 1+ proceeds (counters will emerge, not be tabled).

## ARTIFACTS
- **Committed** (`designs/audit/2026-05-29-massbattle-sim-foundation/`): docs **07–14**.
- **Committed engines** (`tests/sim/`): `sim_mb_06_v22_DB.py` (pure-geometry D-B baseline, ~5/11, casualty-realistic — the bottom-up anchor), and prototypes `v26_counters` / `v30_counters_geom` / `v31_sigma` / `v32_sigma_geom` (top-down counter approaches, RETIRED — kept only as referenced prototypes; do NOT extend them, they violate the bottom-up rule).
- **Gauge:** `tests/sim/gauge_mb.py` (11 melee matchups H1–H11, n=60, seed_base=1e6; bands from `precedents_warfare.md`).
- **Local-only scratch** (not committed, intermediate): `v22_DB_ck/cm`, `v27/v28/v29_geom`, `v23_3a*`.

## VALIDATION PROTOCOL (canonical for this work)
- Wilson 95% CI (`WILSON_Z=1.96`), n≥300 pooled across ≥3 seed banks. Bare frequencies retired.
- Bands: `references/historical/precedents_warfare.md` (Western ancient/medieval; casualty ~15–30% typical; NOTE its evidence-base gaps — no steppe/naval/gunpowder — before modelling those).
- σ-engine: `tests/sim/v32-combat-balance/m1_dice_sigma_core.py` (`σ_N=0.8√pool`, `eff_ob`, `tanh` cap M=1.5, `p_success=Φ(z)`, levels Minor .25/Moderate .5/Strong .75).
- Army Morale (§10.2): `floor(avg morale)+Cmd_mod+Disc_mod`, wired in v31/v32.

## INFRA
- Bootstrap: `cp github_ops_main.py github_ops.py` then `from github_ops import quick_bootstrap` (B6-fixed version with PR-merge fallback). PAT at `/home/claude/.valoria_pat`.
- Gates: `task_gate('simulation')` + `sim_gate('custom', systems=['mass_combat'])` — need canonical sources fetched (canon_constraints, SKILL.md, mass_battle_v30 force_full, params/mass_combat) + valid ledger.
- **B6 RESOLVED** on main (commit f051d911 PR-merge fallback in atomic_commit). Commits land via `safe_commit(additions=[(path,content),...], deletions, message)` — additions are TUPLES.
- Editorial ledger frontier ED-883; 94 ID-conflicts pending Jordan (incl. ED-865/866/867); do not mint ED/PP unilaterally.
