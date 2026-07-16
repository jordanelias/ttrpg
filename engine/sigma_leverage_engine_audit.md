# σ-Leverage Engine — Granular Audit & Logic-Pipeline Test

`[SELF-AUTHORED — bias risk]` This audits an engine + armature I produced and committed this session. I ran an **independent** harness (`engine_audit_harness.py` — own `Φ`, own exact-discrete convolution; imports the reference impl only to cross-check it, not as the test of record) and deliberately hunted the claim I am most motivated to confirm — that "uniform impact / no foreclosure" holds for the real engine at the small pools the resolution-diagnostic flags as the danger zone.

> **POST-AUDIT UPDATE (after this report was written).** Fork (b) — the **μ-shift** — was implemented and committed: advantage now boosts the roll (`mean += eff_σ·σ·√N`) instead of reducing Ob, so canon P-232 is never triggered. This resolved **F1** and **F3** together (M1 self-test 6/6). Commit `df146f44d5f691b04039ca0e7ceacbb9722fcdd2`; logged **ED-884** (`488d446c…`). F2/F4 were doc-scoped in `engine/sigma_leverage_engine_armature.md`. The "open-jordan-fork" status below is therefore the *audit-time* state; the μ-shift remains Jordan-vetoable (the P-232-exemption alternative is still available but strictly worse).

---

## VERDICT (worst-first; no false balance)

The engine's **math is internally exact and the reference implementation matches its own continuous spec to 1.1e-16** (T1) — there is no code-vs-spec defect, the soft cap is well-behaved, and the prior-session number corrections hold. **But it is not "no issues."** Two real findings, one substantive:

- **F1 [P1] — canon conflict.** The engine reduces *Ob* to deliver advantage, and routinely drives Effective Ob **below 1 (and below 0)**, which Class-A constraint **P-232** ("Ob minimum 1; no modifier may reduce Ob below 1") forbids. Neither the engine (no clamp) nor the armature doc (floors at the wrong value, **0**) handles it. Enforcing the canon floor *reintroduces* pool-dependent non-uniformity and caps the favoured side ~19pp lower — i.e. it partially defeats the property the engine exists for. **Resolution is a Jordan design fork; cannot be invented.**
- **F2 [P2] — overstated scope.** Uniform impact is a **continuous-engine** property. It is *exactly* uniform at all pools incl. 1D in the continuous model (T2) but **erratically non-uniform under discrete resolution** at small pools (T3), which canon itself flags (ED-836/WS-D-1: equivalence validated 5–17D only; bare 1–7D "shaky"). The armature asserts uniformity "at the small-pool extreme" with no such scope. Doc fix.
- **F3 [P3] — confirmed prior (PORT-1).** `SIGMA_N_COEFF = 0.8` is the TN7 σ; uniform-across-pool holds at every TN, only the magnitude is off-nominal at TN≠7 (T5). Already in armature §D; audit confirms the numbers.
- **F4 [P3 / nuance] — saturation framing.** Stacking saturates steeply (T6): the 4th stacked "major" is worth +0.5pp. The soft cap is working as intended (not a defect), but the doc's flat "no dead-zone" is rosy — a player cannot intuit the 4th advantage is worthless. Elegance note.

**Clean (explicitly):** code==spec (T1); soft cap monotone, odd-symmetric, bounded ±1.5, C¹ with slope 1 at origin (T6); the *modifier* never forecloses — P strictly in (0,1) (T6); sign convention symmetric; pool floor 1D consistent; every §C number reproduced; both prior-session drift corrections (+0.7σ↔25.8pp; δσ=1.0 = 34.1/30.9pp) confirmed.

---

## THE LOGIC PIPELINE UNDER TEST

```
levels (signed)  →  net_σ = Σadv − Σadv'  →  eff_σ = 1.5·tanh(net_σ/1.5)
                 →  Effective Ob = base_Ob − eff_σ·σ_N(pool),  σ_N = 0.8·√N
                 →  P = Φ((μN − Eff_Ob)/(σ√N))         [continuous engine]
```
Reference: `tests/sim/v32-combat-balance/m1_dice_sigma_core.py`. Substrate: `params/core.md`.

| Test | What it checks | Result |
|---|---|---|
| **T1** | reference impl == its own continuous spec | **MATCH**, max diff `1.1e-16` |
| **T2** | uniform impact, continuous model, all pools | spread **0.000pp**; exact +25.8pp at **1D–20D** |
| **T3** | discrete-vs-continuous ΔP at small pools | **diverges** (see below) |
| **T4** | Ob-floor P-232 vs engine | engine produces **Ob<1**; clamp **breaks uniformity** |
| **T5** | TN miscalibration from hardcoded 0.8 | TN6 25.64 / TN7 25.80 / TN8 26.33 pp |
| **T6** | soft-cap props · marginal stacking · P-range | all props pass; steep saturation; P∈(0,1) |

### T2 — the property holds *exactly* where it is claimed (continuous)
+0.7σ, 50% baseline: every pool 1D→20D returns **+25.8pp**, spread 0.000pp. The √N and per-die σ cancel algebraically, so this is an identity, not an approximation — and it holds at 1D **in the continuous model.**

### T3 — …but discrete resolution is not uniform at small pools
Same +0.7σ shift, `base_Ob = μN`, exact discrete net distribution:

| pool | continuous ΔP | discrete ΔP | gap |
|---|---|---|---|
| 1D | 25.8pp | **50.0pp** | 24.2 |
| 2D | 25.8pp | **0.0pp** | 25.8 |
| 3D | 25.8pp | 28.2pp | 2.4 |
| 5D | 25.8pp | 19.8pp | 6.0 |
| 8D | 25.8pp | 33.3pp | 7.5 |
| 12D | 25.8pp | 25.9pp | 0.1 |
| 20D | 25.8pp | 20.5pp | 5.3 |

A fractional Eff_Ob shift against an integer-valued net is lumpy — worst at small N, but a discrete-lattice artifact even at 20D. **For the shipped Godot game (continuous canonical, ED-833) this never bites.** It bites for any system resolved on the literal discrete dice (canon keeps the discrete engine for TTRPG-mode) at small pools. The armature must say "uniform under the continuous engine; degrades under discrete at 1–7D per ED-836" — it currently does not.

### T4 — the Ob-floor (P-232) collision, in numbers
**(a) The engine produces Ob<1 routinely.** base_Ob 2, favourable stacks:

| pool | net_σ | Eff_Ob |
|---|---|---|
| 8D | +0.5 | **+0.909** |
| 6D | +1.0 | **+0.287** |
| 6D | +1.5 | **−0.239** |
| 12D | +1.5 | **−1.166** |

P-232: "no modifier may reduce Ob below 1." The reference `eff_ob` applies no floor → **violation across ordinary stacks.**

**(b) Enforcing the canon floor breaks uniformity** (favourable +0.7σ, base_Ob 2):

| pool | ΔP unclamped | ΔP clamped@1 |
|---|---|---|
| 6D | 22.35 | 18.16 |
| 8D | 17.97 | 13.25 |
| 12D | 10.81 | 7.10 |

The clamp engages more where Eff_Ob would go lower, so the suppression is **pool-dependent** — reintroducing the exact non-uniformity the engine removes.

**(c) Favoured-side ceiling moves ~19pp** (max favourable, eff_σ=+1.5, base_Ob 2):

| pool | unclamped P | clamped@1 P |
|---|---|---|
| 6D | 95.6% | **76.3%** |
| 12D | 99.4% | **91.5%** |

So the design question is live and large: does maximal strategic advantage make you ~96% or ~76% on the pivotal action? The engine says ~96%; canon (Ob≥1) says ~76%.

### T5 — PORT-1 confirmed
+0.7σ, 50% base: TN6 **25.64** / TN7 **25.80** (exact) / TN8 **26.33** pp with hardcoded 0.8; all **25.80** with per-TN σ. Uniform-across-pool holds at every TN (√N cancels); only the magnitude is off-nominal off-TN7. Matches armature §D (TN8 26.3). Fix = `σ_N(pool,TN)=σ_per_die[TN]·√pool` — no new values.

### T6 — soft cap & saturation
Monotone ✓, odd-symmetric ✓, bounded ±1.5 ✓, slope at 0 = 1.0000 (small modifiers apply ~fully) ✓. Marginal ΔP per added "major" (50% base, capped): **30.9 → 9.5 → 2.2 → 0.5 → 0.14 pp.** "No dead-zone" is literally true (slope > 0 everywhere) but the practical saturation past ~2 stacks is severe (intended Lesson-5 bound). P-range: most-adverse 1D = 0.023%, most-favourable 20D = 99.93% — the *modifier* never forecloses to 0/1 (those extremes are base-difficulty driven, not modifier driven).

---

## RESOLUTION-DIAGNOSTIC / NERS VERDICT

Phase 0: dice-resolved continuous success-pool + deterministic modifier transform (no clock, no accumulator, no internal loop — the soft cap is the Lesson-5 bound by construction). Stress point = small pool; exposure depends on the porting target (routine for a bare-stat faction port; floor-under-degradation for combat).

```
SYSTEM: σ-leverage engine (kernel)   COMPONENTS: dice + deterministic transform
VERDICT: NOT canon-clean — sound math, but a Class-A constraint conflict (F1) unresolved.

N: pass — removes pool-dominance; nothing redundant. (Watch over-porting, §G.)
R: FAIL (pending F1, F2) — holds at extremes in the continuous model, but
     F1: Ob-reduction violates P-232 and the canon floor reintroduces non-uniformity;
     F2: discrete small-pool non-uniformity is real and unscoped.
S: pass w/ caveat — transform is smooth and C¹, integrates with the continuous
     engine; the Ob-floor interaction (F1) is a friction point at the substrate boundary.
E: pass w/ notes — one hidden transform, elegant; blemishes are the F1 "floored to 0"
     doc error and F4's rosy "no dead-zone".

REMEDIATION (worst-first):
  P1 F1  → Jordan fork: (a) exempt the σ-transform from P-232 in continuous mode
            [declare Eff_Ob may range < 1; transform ≠ Ob-setting modifier]; OR
            (b) reformulate advantage as a μ-shift (move outcome mean) not an
            Ob-reduction → P-232 never triggers, uniformity preserved; OR
            (c) accept the floor and lose the favourable extreme [not recommended].
            No canonical text exists either way — modifier_system_spec.md (the
            expected home) is absent (this session's DRIFT-1). Jordan must decide.
  P2 F2  → doc: scope uniform impact to the continuous engine; cite ED-836; note
            discrete small-pool degradation. (Engine unchanged.)
  P3 F3  → PORT-1: per-TN σ_N. (Already in §D; combat at TN7 unaffected.)
  --  F4 → doc: temper "no dead-zone" with the saturation table. (Not a defect.)

RE-TEST of fix (b): a μ-shift of δσ·σ adds exactly δσ to the z-argument with no Ob
  term, so it preserves T2 uniformity, never touches P-232, and keeps the tanh bound —
  clean on the continuous model. (Discrete small-pool divergence per F2 persists under
  any formulation — it is a property of the substrate, not the transform.)
```

---

## IMPACT ON THE PENDING CANONIZATION DECISION (§I-1)

Last turn's load-bearing question — "canonize the armature as the engine spec?" — now has an audit answer: **not yet.** F1 must be resolved first (it is a Class-A conflict and a Jordan fork), and F2 must be corrected in the doc. Canonizing as-is would enshrine an engine that violates P-232 and a uniform-impact claim that is unscoped. Sequence: Jordan picks the F1 fork → apply F2/F4 doc fixes → re-run this harness on the chosen formulation → then canonize + Omega-vet (§H).

---

## PROPOSED EDITORIAL-LEDGER ENTRY (staged — not committed)

The `audit` task-gate states P1 findings append to `registers/editorial_ledger.jsonl`. I am **staging** rather than auto-appending: F1's resolution is a design fork (owner contract → Jordan), and self-assigning an `ED-NNN` risks collision against the open 94-ID backlog. On your word I append via the ledger primitive with an ID you confirm.

```json
{"id": "ED-PENDING", "type": "audit_finding", "severity": "P1", "status": "open-jordan-fork",
 "system": "sigma-leverage-engine",
 "finding": "Engine Ob-reduction (eff_ob = base_Ob - eff_σ·σ_N) drives Effective Ob below 1, violating P-232 (Ob minimum 1). Reference impl applies no floor; armature doc floors at 0 (wrong value).",
 "impact": "Enforcing P-232 reintroduces pool-dependent non-uniformity (T4b) and lowers favoured-side ceiling ~19pp at 6D (T4c).",
 "fork": ["exempt σ-transform from P-232 (continuous)", "reformulate as μ-shift", "accept floor, lose favourable extreme"],
 "evidence": "engine_audit_harness.py T4; params/core.md P-232; m1_dice_sigma_core.py eff_ob",
 "note": "modifier_system_spec.md (expected home) absent — no canonical text binds or exempts the transform."}
```

---

## PROVENANCE

- `[READ: tests/sim/v32-combat-balance/m1_dice_sigma_core.py — full, fetched this session]`
- `[READ: params/core.md — full; P-232 Ob-floor, ED-833/836 continuous engine, per-die μ/σ, pool floor]`
- `[READ: engine/sigma_leverage_engine_armature.md — §C leverage layer + worked example, this session's commit 4e6df85]`
- `[VERIFIED: T1–T6 via independent harness (own Φ + exact-discrete convolution); reference impl cross-checked, agrees to 1.1e-16]`
- `[CONFIDENCE: high — every finding is reproduced numerically and tied to a canon cite or a code line; F1 severity (P1) rests on P-232 being unqualified in canon, which it is as written.]`
- `[ASSUMPTION: P-232 applies to the σ-transform — basis: P-232 is stated with no continuous-mode/transform carve-out and is restated in the Pool-Floor section; the carve-out, if intended, would live in modifier_system_spec.md, which does not exist. Flagged as the F1 fork rather than assumed away.]`
```
