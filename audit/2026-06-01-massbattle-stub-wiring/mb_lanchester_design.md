# P-L — Lanchester Attrition Substrate · Design Spec
**Date:** 2026-06-01 · **Engine:** `tests/sim/mass_battle/` (post-P-A modular) · **Directive:** D-D (Jordan), confirmed linear/square split.
**Status:** DESIGN (no engine code changed in this doc). Implementation is the next step, gauge-gated.
`[SELF-AUTHORED — bias risk]` I proposed this; magnitudes/coefficients are Class-B sim-tunable and Jordan-vetoable.

---

## 1. THE GAP (bottom-up, from the current engine)

Current melee casualty term — `mass_battle/orchestration.py` `resolve_engagements` (per engagement pair):
```
dmg_a += CASUALTY_SCALE * max(0, DAMAGE_BY_DEGREE[b_deg](unit_b.power) - unit_a.dr)
dmg_b += CASUALTY_SCALE * max(0, DAMAGE_BY_DEGREE[a_deg](unit_a.power) - unit_b.dr)
```
`DAMAGE_BY_DEGREE = {Overwhelming: 1+p, Success: p, Partial: 1, Failure: 0}` (config).

Casualties are a function of **roll-degree × Power − enemy DR**. Numbers enter combat **only** through the pool (continuous `effective_size` → fewer dice when depleted). There is **no force-on-force attrition term**: the casualty rate a unit inflicts does not depend on how many enemy it faces. That is the missing Lanchester substrate.

Volley is a **separate** term (`volley_phase`, `_roll_volley_pool`) — the clean square-law seam.

## 2. WHICH LAW (top-down, grounded — Lanchester literature)

- **Linear Law = ancient/melee.** One fighter engages one fighter; casualty rate capped by **troops-in-contact / frontage**; numerical superiority is a *linear* edge only. Mechanism (verbatim from OR lit): casualties "proportional to combatants in direct physical contact... limited by terrain or formation frontage."
- **Square Law = ranged/aimed fire.** Any unit engages any enemy; combat power ∝ N². Requires the frontage cap to be *lifted* (firearms/artillery; here, **volley**).
- Real battles sit **between** (empirically ~1.5 exponent; Willard 1618–1905). Jordan confirmed the **split** (linear melee / square volley), not a blended 1.5.

**Valoria already has the Linear Law's frontage mechanism** — `_engaged_cols` + `distribute_casualties` restrict fighting to engaged columns (per-cell layer). P-L adds the **attrition term** on top of that existing frontage cap.

## 3. THE DESIGN — two terms, composing with σ (no double-count)

**Role separation (Lesson 1 — one variable, one job):**
- **σ-leverage head** sets *who is winning the exchange* — the kill-ratio asymmetry (degree, morale, facing, fatigue, charge-shock all feed σ). Unchanged.
- **Lanchester term** sets *the casualty magnitude scale from numbers-in-contact*. New.
- **Per-cell frontage** (`_engaged_cols`) sets *how many are in contact*. Unchanged — it is the linear law's cap.

### 3a. Melee — Linear Law
Replace the constant `CASUALTY_SCALE` magnitude with a strength-proportional, frontage-capped factor. Conceptually:
```
casualties_to_X  ∝  k_linear × (enemy effective strength IN CONTACT) × (degree/Power term) − DR_floor
```
where "enemy effective strength in contact" = the engaged-column troop count the per-cell layer already computes (frontage-capped). The `DAMAGE_BY_DEGREE[deg](power)` term is retained as the **per-soldier lethality / exchange quality** (set by roll degree + equipment), and the Linear-Law factor scales it by *how many contacting troops are doing the killing*. Net: a unit that fields more troops *along the contact frontage* inflicts proportionally more — but width beyond frontage does **not** (linear, not square). This is exactly the linear-law signature: equal-quality forces → survivors ≈ difference of sizes.

**Implementation seam:** the term lives in `resolve_engagements` (orchestration) reading the engaged-strength from percell; `CASUALTY_SCALE` becomes the linear coefficient `k_linear` (re-tuned). When `PER_CELL=0` (no column grid), fall back to a frontage proxy from `effective_size` so the non-per-cell path still behaves (and the gauge's PER_CELL=0 battery re-tunes to hold its bands).

### 3b. Volley — Square Law
In `volley_phase`, aimed fire lifts the frontage cap: every shooter can engage the target area, so effectiveness scales with **shooter count** (toward N²-type concentration). The volley loss term becomes proportional to *shooter strength* (not frontage-capped), with `k_square` coefficient. This makes massed archers/crossbows concentrate fire — the historically-correct ranged behaviour, and distinct from melee.

### 3c. Feeds morale — does NOT replace it (critical guard)
Battles end by **rout at ~30% casualties** (du Picq; the morale/rout system). Lanchester governs the **casualty-accrual rate** feeding the morale triggers and rout — it is **not** a new victory condition and must not produce annihilation battles. Re-tuning target: the same win-rate + casualty% bands the gauge already enforces (H1–R3 + C1–C7), now produced by a principled attrition law instead of a flat scale. If the law pushes casualty% out of band, tune `k_linear`/`k_square`, not the morale system.

## 4. VALIDATION PLAN (gauge-gated; this is a behaviour CHANGE)

1. **Re-tune to hold existing bands.** `CASUALTY_SCALE`→`k_linear` (+ `k_square` for volley) tuned so H1–R3 multi win-rates and casualty% stay in their current bands and C1–C7 stay in the ratified charge bands. The refactor's byte-exact baseline is the *behavioural* reference; P-L is allowed to change numbers but must re-land the bands.
2. **Linear-law signature test (new gauge row).** Equal-quality melee, unequal sizes (e.g. 7 vs 5 effective) → larger force's survivors ≈ size difference (the classic linear result), within tolerance. Asserts the melee term is genuinely linear.
3. **Square-law signature test (new gauge row).** Pure volley, unequal shooter counts → casualty ratio reflects N²-type concentration advantage (larger force disproportionately favoured), distinct from the melee row. Asserts volley is genuinely square.
4. **No-annihilation invariant.** Confirm battles still terminate by rout ~30%, not by Size→0, across the battery (morale system still dominant).
5. **PER_CELL=0 AND PER_CELL=1** both re-validated (the term has a per-cell-aware path and a fallback).

## 5. CONSTANTS (new; ledgered + Class-B)
- `k_linear` (replaces/rescopes `CASUALTY_SCALE` for melee) — linear attrition coefficient.
- `k_square` — volley attrition coefficient (square-law).
- `LANCHESTER_ENABLED` env toggle (default ON once validated; OFF reproduces the pre-P-L flat-scale term for A/B).
Each ledgered with its canonical/precedent anchor (Lanchester linear=melee, square=ranged) and marked Class-B sim-tunable.

## 6. OPEN CONFIRM
- Coefficient *values* are sim-tuned at implementation (Class-B) — surfaced for veto, not pre-decided here.
- Exponent: **linear melee / square volley** per Jordan's confirm (not blended 1.5). Locked.

## 7. SEQUENCE
Implement in `resolution.py`/`orchestration.py` (melee term) + `orchestration.py` `volley_phase` (square term), behind `LANCHESTER_ENABLED`; add the two signature gauge rows; re-tune `k_linear`/`k_square` to hold all bands; verify PER_CELL=0 and =1; commit `[simulation]` with the new ledger entries. Then P-C (FM formations).
