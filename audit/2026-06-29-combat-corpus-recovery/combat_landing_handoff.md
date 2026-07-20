# Combat μ-shift + eff_cw — LANDING HANDOFF
**2026-06-12 · step 1 (commit + re-ratification) staged · steps 2–3 queued · Jordan-authorized ("proceed in order")**

## STATE: wiring DONE + validated; only the canonical commit remains
All edits are on **local copies in `/home/claude/ew/`** (uncommitted). Validated:
- **μ-shift** (F4) — atom proof (MC ≡ canonical `p_success`; −6…−10pp advantage-clip removed) + **parity re-baseline CLEAN**: mirror 49.9/50.0, strength 6v4 59.5/40.5, history 7v4 61.7/38.2, agility 6v4 65.6/34.4 (reproduces prior baseline exactly → invariants hold downstream).
- **eff_cw routing** (F2) — 17/17 channel sites in `systems.py` → `eff_cw`; invariant-safe (no-ability ≡ `channel_weight`, PASS); activates the 3 channel abilities (Stärke-Schwäche leverage 1.30→1.56).
- **precommit** — 1 co-modulator in `feint_eval` defender intent-read (sen-sen-no-sen); modulate-existing.

## THE THREE EDITS (apply to canonical files; local copies already hold them)
1. `tests/sim/v32-combat-balance/r1_sigma_resolution.py` — import `net_boost`; `resolve_action`: `ob = base_ob` (was `effective_ob(...)`), `net = roll_net_continuous(...) + net_boost(net_sigma, pool, tn)`.
2. `tests/sim/v32-combat-balance/r8_parity_harness.py` — import `net_boost`; `resolve_phrase`: drop `effective_ob`, `net += net_boost(net_sigma, pool, TN_STANDARD)`, `deg = degree_of_success(net, DECISIVE_OB)`.
3. `designs/scene/combat_engine_v1/systems.py` — 17× `TR.channel_weight(X.tradition, ch)` → `TR.eff_cw(X, ch)`; in `feint_eval`, `def_read` gains `*TR.eff_cw(defender,'precommit')`.

## COMMIT PLAN — two write-disjoint commits
**Commit 1 — Lane C (clear):** files 1+2.
- scope `[simulation]` (or `[fix]`); message `^[(scope)] desc — ED-NNN` (`commit_message_gate`).
- **Required co-file: sim → matrix.** Schema (`sim_verification_ledger*.json`): `{sim_file, scope, entries:[…]}`. Append an entry for the r1/r8 μ-shift verification (mirror parity + monotonicity figures above).

**Commit 2 — Lane A (`designs/scene`, owns-gapped + Jordan-authorized):** file 3.
- scope `[patch]` (or `[fix]`).
- **Required co-file: patch → register.** Locate the patch register schema (read a recent `[patch]` commit's co-file) before constructing.

**Mechanism:** `h.task_gate('simulation')` (or appropriate) → `adds = h.pre_commit_gate_mutating(additions, deletions)` (auto-applies compliance fixes, returns augmented list) → `h.safe_commit(adds, deletions, message)`. `safe_commit(additions, deletions, message, repo=None)`; additions = `[{'path','content'}]`.

## BLOCKER (the only one): ED reservation
`canon/editorial_ledger.jsonl` — 675 entries, **max ED 1012, tail ED-933** (non-monotonic; per-lane ranges A 890–939 / C 970–999 possibly overflowed; **reservation pointer flagged stale**). **Do not guess.** Resolve the authoritative next-ED via the orchestrator reservation logic / pointer, then:
- File **re-ratification ED entry** in `canon/editorial_ledger.jsonl`: μ-shift = **convergence-to-canon** (the analytic `p_success` was already μ-shift; `eff_ob` is DISPLAY-ONLY; r1/r8 corrected to match — a confirm, not new behaviour). Reference the re-baseline figures.
- Same entry (or adjacent) records the **D-α** flag (8 live traditions vs 6 synthesis-native — Jordan-open) and **PoB keep** (ratified, wiring pending).

## STEP 2 (queued) — PoB + F5 coupling specs, then wire
Machinery exists; write the spec (bottom-up + top-down, Jordan-vetoable), then wire:
- **PoB / `pob_frac`** → `anti_overcommit` · `init_overcommit_loss(exposure)` · `poise_factor` (recovery/exposure) + `strike_damage` (swing-weight, **compose with `mass`, no double-count**). `pob_frac` is the only dead weapon-vector field.
- **F5 wound model** → `stamina_max` · `conc_max` · resolution `net` (execution). **NOTE: `m9_wound_model_bottomup.py` already exists** — read it first; F5 likely builds on/replaces it + the deb405b944 −1D-pool path. Per-wound penalty curve to the three targets.

## STEP 3 (queued) — F1 grid/facing (largest)
Extends **`m7_facing_fov.emergent_facing_advantage`** (already a module). Build: square grid, facing logic (shared with mass-battle cells), flank/surround bonus, side-rear reaction penalty, ally-adjacent occupied bonus, projectile **physics-distance → hit + crit**. Coordinate with the J-9 mass-battle owner (facing shared).

## ALSO PENDING
- **F7** must be **re-measured under μ-shift** (the 06-09 crit-saturation numbers were on the buggy Ob-floor path; Overwhelming threshold is now base-relative `net ≥ 2·base_ob`).
- Build the `reopen`/`disengage` **levers** (unbuilt), then wire those abilities.
- D-α / orthogonal second tradition-slot / D-δ naming — Jordan decisions (gate later tuning, not the foundation).

## Local artifacts
`/home/claude/ew/`: edited `r1_sigma_resolution.py`, `r8_parity_harness.py`, `systems.py` (+ full module set: m1/m3/m5/m7/m9/r1/r2/r5/r8 assembled for the re-baseline).
Outputs: `combat_component_wiring_ledger.md`, `weapon_taxonomy_framework_v2.md`, `combat_foundation_build_plan.md`.
