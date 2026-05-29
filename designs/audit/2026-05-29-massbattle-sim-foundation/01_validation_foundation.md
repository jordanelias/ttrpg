# Mass Battle Sim — Validation Foundation Is Broken: Findings + Rebuild Plan

**Date:** 2026-05-29
**Task:** simulation (gated; full-depth canonical reads + verification ledger; sim_gate passed)
**Status:** STOP-AND-DECIDE. Fixing engine mechanics is blocked on rebuilding the validation instrument first.
**Commit status:** nothing committed (B6); analysis only.

---

## Verdict

The mass-battle sim cannot be validly fixed in its current state. The validation instrument is broken, the "known-good" baseline is unreproducible, and as a result the binding constraint cannot be reliably diagnosed. The correct next action is **not** to patch Issue 4 — it is to **rebuild a historically-grounded validation instrument for the current engine**, after which every fix becomes falsifiable. Two findings make this unavoidable, and one names the systemic disease.

---

## Findings (all measured/read this session — SHA-fresh)

### F1 — The current battery is an invalid instrument (severity: blocking)
`battery_v22.py` reuses the v9 spec's **single-engagement** win-rate bands (45–55%, 50–65%, …) but runs them against **multi-turn** outcomes via `run_multi_turn_battle`. This is the audit's own **D-8** ("single-turn bands stale for multi-turn"). Any in-band/13 number it produces — including last turn's 3/13 from the LETHALITY_SCALE sweep — is measuring multi-turn results against single-engagement targets. **Invalid.**

### F2 — The "12/13 working baseline" is unreproducible (severity: high)
- The arc audit (`sim_audit_v5_to_v22.md`) repeatedly cites "v14 achieving 12/13" as the calibration high-water mark.
- I ran the grounded `sim_mb_06_v9_battery.py` against the **v9 engine** → **5/13** (mean turns 8.5–9.8, already above the 3–6 L1 band; H3 even labeled `[v8 OPEN]` in the battery). v9 is the *early* calibration state, not the 12/13 version.
- The **v14 engine** exists but renamed the core unit primitive (`Atom`→`Subunit`, per the v11 terminology change) and **no v14 battery was preserved**. Batteries exist only for v5–v10 and v22.
- **Consequence:** the canonical "this version was historically accurate" claim **cannot currently be verified**. It is folklore until a v14-compatible battery is reconstructed.

### F3 — The binding constraint cannot be reliably identified (severity: high)
The LETHALITY_SCALE sweep capped at 3/13 with the failure set dominated by **formation-geometry** matchups (Horseshoe/Arrowhead/RefusedFlank/Gapped blowouts), *suggesting* the v13+ cell machinery — not lethality — is the binding defect. **But that sweep ran on the F1-invalid instrument.** So whether lethality or geometry is binding is genuinely undetermined until a sound gauge exists. (Diagnosing on a broken gauge is how the lineage got here.)

### F4 — Issue 1 is a ratio break, and the spec forbids the multiplier fix
- v9 model: `h_per_size = min(disc,cmd)+dr ≈ 5` → `HP = Size × 5`, damage `(1+Power)−DR ≈ 3–4`/pair → decisive in 3–6 turns.
- v19 changed `HP = Size × BLOCK_SIZE (100)` (20× inflation) while leaving damage unchanged → single engagements can't resolve → multi-turn wrapper bolted on, never recalibrated.
- The real Issue 1 is the **broken HP:damage ratio**, not a missing multiplier. The historical spec explicitly says fix via "correctly modeling the formation counters, **not via ad-hoc damage multipliers**." My prior-turn LETHALITY_SCALE re-introduction was the forbidden multiplier, tuned to win-rate bands (conflating lethality with formation counters), on the F1-invalid instrument — triple-wrong. Retracted.

### F5 — Possible over-engineering (severity: medium; decision-relevant)
Issues 2/3/4 (equal-speed cell contention, displacement ripple, within-side formation-hold) are all **v13+ elaborations** added *after* the v9-era simpler geometry. v9's simpler geometry reached 5/13; v14 (more geometry) reached 12/13; v22 (most geometry) reached ~1/13. This is non-monotonic in apparatus — consistent with the v13+ machinery being **net-negative as currently implemented** (introduced degenerate-overlap bugs). The fix may be to **repair** that machinery (Issues 2/3/4) OR to **revert toward v14's sufficient geometry** (NERS-E / over-engineering-is-a-defect). Undetermined until the instrument is rebuilt.

### F6 — Systemic disease (the answer to "how do we stop wasting effort")
The lineage has **no maintained, version-portable, historically-grounded battery.** Batteries exist for v5–v10 and v22 only. Therefore:
- Every version v11→v25 re-broke formation accuracy **invisibly** (no test ran).
- The v16 multi-turn rewrite **silently invalidated** the validation bands (F1).
- Correctness claims ("12/13") became **unfalsifiable** (F2).
This is the institutionalized form of the duplicated-work / conflict / wasted-effort pattern. It is the same failure as reading the oldest-cited artifact and stopping — applied to validation: the gauge was never carried forward, so the work proceeded blind.

---

## Recommendation — rebuild the foundation before any engine fix

**Two-level validation instrument, built once, carried forward every version:**

1. **Single-engagement formation-counter battery** (current engine API). Reuse the grounded v9 spec bands *at the granularity they were built for* — single decisive engagement. Restore the HP:damage ratio (revert the v19 inflation, or set `run_battle` to be decisive in its 18-tick window) so formation differences are observable. This validates **who beats whom** (the formation counters) against Cannae/Pydna/Leuctra/etc. **No new band derivation needed.** I can build this now.

2. **Multi-turn dynamics validation** (separate). Validate **pacing, casualty rate, morale cascade, pursuit** against historical *rates* (loser casualties ~15–30%, catastrophic ~50–70%; rout/pursuit dynamics per Hastings/Cannae) rather than the single-engagement win-rate bands. Bands here are derived from `precedents_warfare.md`, not reused from v9.

Once both exist, fixes (Issue 1 ratio, Issues 2/3/4 geometry, ED-822 volley) become falsifiable, and F3/F5 resolve empirically.

---

## Decisions required (Jordan)

- **D-A — Battle model granularity.** Canon §A.7/§A.12 implies a **multi-turn** battle (rout/pursuit/reform across turns); the historical bands were built **single-engagement**. Recommend: keep multi-turn as canon, adopt the **two-level instrument** above (single-engagement validates counters; multi-turn validates dynamics). Confirm or redirect.
- **D-B — HP model.** `Size × h_per_size` (v9, abstract) vs `TroopCount/BLOCK_SIZE` (v19, soldier-count but incomplete — damage was never rescaled to soldiers). Your "bottom-up basis" reminder favors **completing the TroopCount model** (HP = soldiers, damage = soldiers killed, calibrated to historical casualty %). Recommend completing it. Your call — it changes the lethality calibration.
- **D-C — Over-engineering (deferred to post-baseline).** After the instrument is rebuilt and shows where the current engine actually stands: **repair** the v13+ cell machinery (Issues 2/3/4) or **revert toward v14's simpler-sufficient geometry**. Flagging now; decide on evidence.

---

## What I did NOT do, and why
- Did **not** blind-patch Issue 4: on the F1-invalid instrument the result would be meaningless (false-completion), and per F5 it may be wasted effort.
- Did **not** keep the prior LETHALITY_SCALE fix as-is: retracted per F4 (forbidden by spec; tuned on invalid instrument).
- Did **not** reconstruct the v14 battery this session (it's part of the foundation rebuild, and context budget was better spent confirming the diagnosis).

## Confidence
- `[CONFIDENCE: high]` F1 (band/granularity mismatch read directly from both battery files), F2 (5/13 measured; v14 API rename confirmed; battery absence confirmed by tree walk), F4 (HP models read from v9 + v22 engines), F6 (battery inventory from tree walk).
- `[CONFIDENCE: medium]` F3/F5 (binding-constraint and over-engineering reads are suggestive from the broken-instrument sweep + monotonicity, explicitly not proven — that's the point).
- Engine edits this session are local experimental controls only; main untouched (B6). Verification ledger at `/home/claude/sim_verification_ledger.json`.

## Supersession
This supersedes `massbattle_sim_issue1_status_2026-05-29.md`'s "fix Issue 1 then Issues 2–4" sequencing and `ed811_engagement_formula_resolution.md`'s R1–R4 fork. Both assumed a working validation instrument. There isn't one. The instrument is the prerequisite.
