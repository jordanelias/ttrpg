# Collapse-Loop Bound Reachability — Results (confirms the precedent matrix)

**Date:** 2026-05-29
**Sim:** `sim_collapse_recovery.py` (this folder)
**Relation to prior work:** this **confirms and quantifies** the `ners_historical_precedent_matrix.md` (2026-05-28) entry 3, which already **retracted** the diagnostic's "faction collapse loop is unbounded — no cap short of extinction → Lesson 5" finding on the strength of **Tainter, *Collapse of Complex Societies*** (collapse = simplification + reconstitution, not annihilation). It does **not** re-derive that verdict; it tests the sub-clause the matrix did not quantify — *is the bound reachable, or merely nominal?*
**Bias:** `[SELF-AUTHORED — bias risk]`. I initially built this as a fresh "re-examination" of ED-868 before checking the matrix; the matrix had already settled the existence question. This doc is re-scoped to the reachability question, which is genuinely additive.

---

## §0 — Headline

**The matrix's retraction holds: the collapse loop is bounded (Tainter-validated).** My sim confirms the bounds are *reachable* — but adds a finding the matrix did not surface: **the bound's reachability is resolver-dependent.** Under the current bare-stat dice, faction reconstitution is near-unreachable for a weakened collapsed faction (P ≈ 0.004 at Influence 3); under the deterministic+stochastic resolver candidate (ED-865/874) it becomes meaningfully reachable. **This links the two work streams: adopting deterministic+stochastic is also what makes the ED-868 collapse bound adequate rather than nominal.**

---

## §1 — What the matrix established (top-down, precedent)

Per `ners_historical_precedent_matrix.md` entry 3, citing **Tainter**: collapse is "a return to a lower sustainable level of complexity, not annihilation"; collapsed societies become smaller/simpler and frequently **reconstitute as successor polities.** Tainter's **peer-polity simultaneity** ("no polity can withdraw from the spiral or it is absorbed by a neighbor") also validates the cross-faction cascade coupling. The matrix's bottom-up basis: Stability recovery +1/clean season (§1.3 Institutional Consolidation), Survival Exception 1×/campaign (§1.5), reconstitution, sticky Military. **Verdict: loop bounded; Lesson 5 retracted.** I accept this in full.

---

## §2 — What this sim adds (reachability quantification)

The bounds **exist**; the question Lesson 5's sub-clause demands is whether they are **reachable** (a bound you cannot reach is not an adequate safeguard). Tested across the collapsed faction's available Influence (Reconstitute = Influence Ob 4, **3 consecutive** successes, requires ≥1 territory), 8k MC:

| Influence | bare dice: P(recover ≤ 40s) | dice median seasons | **d+s: P(recover ≤ 40s)** | d+s median seasons |
|---|---|---|---|---|
| 1 | 0.000 | — | 0.003 | 20 |
| 2 | 0.000 | — | 0.035 | 20 |
| 3 | 0.004 | 20 | 0.229 | 20 |
| 4 | 0.051 | 21 | **0.543** | 18 |
| 5 | 0.217 | 19 | 0.825 | 14 |
| 6 | 0.474 | 19 | 0.962 | 10 |
| 7 | 0.727 | 15 | 0.996 | 7 |

**Three findings:**

1. **The territory precondition is the *binding* constraint, not the roll.** With no territory held or recaptured, P(recover) = 0.000 regardless of Influence — Reconstitute cannot even begin. This matches the canon (Reconstitute "requires at least 1 territory held or recaptured") and is the correct, realistic gate: a polity with zero territorial base does not reconstitute (Tainter — reconstitution is by *successor polities* that retain a local resource base).

2. **"Within 4 seasons" is the minimum, not the expectation.** The matrix's bottom-up note cited "reconstitution within 4 seasons." That is the theoretical floor (3 consecutive successes = 3 seasons minimum). The *expected* time is far longer — median 7–20 seasons depending on Influence and resolver — because the 3-consecutive-success clause is demanding. Not a contradiction of the matrix's *verdict* (the loop is still bounded), but a correction to the *timescale*: reconstitution is slow, not prompt.

3. **Reachability is resolver-dependent — the key cross-finding.** Under **bare dice**, a collapsed faction at low Influence (1–3, the likely state after attributes freeze at 50%) has **near-zero** reconstitution probability (0.000–0.004) — *effectively extinction despite a paper recovery path.* Under the **deterministic+stochastic** resolver, the same faction recovers with meaningful probability (Influence 4 → 0.54). **So the bound that makes the collapse loop adequate (Lesson 5) is only genuinely reachable under the resolver Jordan selected.** Bare dice make the bound nominal; d+s makes it real.

The Survival Exception (one-time Stability-1 floor vs an Accounting Stability Check) is a **deterministic** cap — always reachable by definition when the faction is at Stability 1 and has not yet used it. It is not resolver-dependent and is unconditionally adequate as a one-shot.

---

## §3 — Reconciled ED-868 verdict

| Question | Verdict | Basis |
|---|---|---|
| Is the collapse loop unbounded (diagnostic Finding-4 / "no cap short of extinction")? | **No — retracted** | Matrix (Tainter): collapse = simplification + reconstitution. |
| Are the bounds reachable, or nominal? | **Reachable — but resolver-dependent** | This sim: territory is the binding gate; reconstitution near-unreachable at low Influence under bare dice, reachable under d+s. |
| Is Lesson 5 (add a bound) needed? | **No** | The bounds exist (matrix) and are reachable (this sim, under d+s). |
| Residual? | **Adopt d+s to make the bound adequate**, and a *separate* GD-3 gap (below). | Cross-finding + matrix entry 4. |

**ED-868 status: resolved-bounded (per matrix), with the reachability of the bound contingent on the ED-865/874 resolver decision.** Not a standalone defect requiring a new safeguard.

---

## §4 — The genuine residual the matrix surfaced (not ED-868)

The matrix's entry 4 identifies a *different*, real gap my session did not address: **GD-3 (Revolt → Insurgency → Faction) has no down-path.** Per **RAND, *How Insurgencies End* (89 cases)**, insurgent defeat is the **modal** outcome and loss of sanctuary/sponsorship is the strongest predictor — yet GD-3 can only escalate, never dissolve. The matrix rates this **R FAIL** (no recovery/dissolution path) and recommends an owner-authored multi-path dissolution (military / sponsor-withdrawal / amnesty / persist). **This is higher-value than further faction-collapse work** and is the natural next target. It is *not* ED-868 (collapse is bounded; the insurgency down-path is a distinct missing mechanic).

---

## §5 — Ledger impact

- **ED-868:** annotate **resolved-bounded** (matrix/Tainter), with the reachability cross-finding: the bound is adequate **only under the d+s resolver** — bare dice make reconstitution near-unreachable at low Influence. This is a second, independent justification for adopting ED-865/874.
- **No new safeguard / no Lesson-5 apparatus** — explicitly do not add one (the matrix retraction + this reachability confirmation close it).
- **New residual (owner-authored):** GD-3 insurgency down-path (matrix entry 4, RAND-grounded) — file/track as the next design target.
- Recorded in `ledger_candidates_consolidated.json`; not appended to the live ledger (JSONL migration owns it).

`[CONFIDENCE: high]` — the reachability quantification and the resolver-dependence cross-finding (MC, recovery-mechanic and Reconstitute rules read from canon this session; precedent linkage attributed to the matrix). `[CONFIDENCE: medium]` — the exact recovery timescale (sensitive to the Ob-4→difficulty mapping and the 50%-frozen-Influence assumption).
