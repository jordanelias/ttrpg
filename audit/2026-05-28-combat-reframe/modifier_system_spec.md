# Piece 2 — Modifier System Spec (σ-space + soft cap + state-gating)

**Purpose:** resolve F1 (non-uniform modifier impact) and F2 (compound modifier foreclosure) with a concrete, verified modifier system that lands on the bout-state-graph transitions defined in the reframe blueprint.

**Status:** all claims numerically verified (continuous engine, TN7: E[net/die]=0.40, SD/die=0.80). The system presents one genuine design choice (σ-space vs dice-space) — both specced; Jordan decides.

---

## 1. The problem (recap, quantified)

- **F1:** a flat Ob modifier has non-uniform impact across Pool scale. Verified: a flat +2 Ob swings **42.6pp at 3D but 21.2pp at 20D** — 2× variation. Cause: outcome ~ Normal(0.4N, 0.8√N); a constant shift is a bigger fraction of a smaller distribution.
- **F2:** modifiers sum into one Ob with no overall cap → compound foreclosure at small Pool. Verified: 5D + 6 Ob raw = **0% success** (foreclosure). A hard cap (±4) helps (1.3%) but is non-uniform across Pool and creates a dead-zone (RT-F2.1).

---

## 2. σ-space modifier application (fixes F1)

### 2.1 The transform

Express every modifier in **standard-deviation units (σ-units)** rather than raw Ob points. At resolution, a modifier `δσ` converts to a dice-space Ob shift of `δσ × σ_N`, where `σ_N = 0.8√N` is the outcome distribution's width at the relevant Pool size N.

```
effective Ob = base Ob − (net modifier in σ-units) × σ_N      [σ_N = 0.8·√Pool]
```

(Aggressor-favoring modifiers are negative σ — they lower the Ob to land.)

**Why this fixes F1:** a `δσ` modifier shifts the outcome's z-score by exactly `δσ` regardless of N. Verified: a `+0.7σ` modifier produces **identical 25.8pp impact across all Pool sizes (3D–20D)** at the 50% baseline. The √N source of non-uniformity is eliminated.

### 2.2 Honest residual (Source B)

σ-space removes the *big* (√N) source but not all non-uniformity. At fixed Pool, the same `+0.7σ` modifier still varies by **baseline difficulty**: 13.8pp at a 20%-baseline, 25.8pp at 50%, 27.3pp at 65%. This residual is **irreducible** — P is bounded [0,1], so ΔP must shrink near the extremes (the Φ-slope effect). No modifier scheme escapes it. σ-space is the cleanest available because the continuous engine is itself Gaussian, so "+0.5σ" is a natural, uniform-in-the-engine's-own-units statement.

### 2.3 Player-facing abstraction (the key to acceptability)

**The player never sees "σ".** Modifier sources emit **levels**; the engine maps levels → σ-units → Ob shifts:

| Level | σ-value | ≈ Ob at 12D ref (intuition only) |
|---|---|---|
| Minor | ±0.25σ | ±0.7 |
| Moderate | ±0.50σ | ±1.4 |
| Strong | ±0.75σ | ±2.1 |
| Major | ±1.00σ | ±2.8 |

The player reads "Forward-point vs Centered: **Strong advantage**" — not "+0.7σ." This makes the σ-space math an **engine-internal detail**; the player-facing experience is a clean level system that other Valoria systems could share. (Migration from current matrices: current ±1 Ob → Moderate; ±2 Ob → Strong. Level values sim-tunable.)

---

## 3. Soft cap (fixes F2, beats hard cap)

### 3.1 Saturating function

Sum the **net** live modifiers (aggressor-favoring minus defender-favoring) in σ-units, then pass through a smooth saturating cap before applying:

```
net_raw_σ  = Σ(aggressor-favoring σ) − Σ(defender-favoring σ)
effective_σ = M_max · tanh(net_raw_σ / M_max)        [M_max = 1.5σ, sim-tunable]
Ob_shift    = effective_σ × σ_N
```

**Why tanh:** for small sums, `tanh(x) ≈ x` (modifiers apply nearly fully); as the sum grows, it saturates smoothly toward `M_max`; there is **no hard ceiling and no dead-zone**. Verified marginal value always positive and diminishing: raw 0.5σ→0.48σ, 1.0σ→0.87σ, 2.0σ→1.31σ, 3.0σ→1.45σ.

### 3.2 F2 resolution verified

| Scheme | 5D worst case P(success) | Verdict |
|---|---|---|
| Uncapped (dice-space +6 Ob) | 0.0% | foreclosure (the F2 defect) |
| Hard cap ±4 (Stage 4 proposal) | 1.3% | better, but non-uniform + dead-zone |
| **Soft cap σ-space (raw 2.1σ → eff 1.33σ)** | **9.2%** | bounded, no foreclosure, no dead-zone |

### 3.3 σ-space makes the cap itself uniform

A `±1.5σ` soft cap means the **same maximum P-shift across all pools** (verified ~43.3pp at 3D–20D). A dice-space `±4` cap does not (36.8pp at 20D, 49.8pp at 3D, worsening toward extremes). This is a second reason σ-space and the soft cap belong together: σ-space is what makes the cap fair across Pool scale.

---

## 4. State-gating (reduces F2 raw sum + F6 per-state load)

Partition modifiers by which **bout state** they are live in. Each state surfaces only its physically-relevant modifiers.

| Modifier source | Out-of-contact | Closing | In-bind | Breaking |
|---|:---:|:---:|:---:|:---:|
| Stance Counter | · | live | · | · |
| Reaction-aspect | · | live | live | · |
| Reading-modifier | live | live | live | · |
| Set bonus (loadout) | live | live | live | live |
| Weapon phase-strength | live | live | live | live |
| Perception/Facing | live | live | · | live |
| Tactile (bind only) | · | · | live | · |
| Grip (bind only) | · | · | live | · |
| Approach-derived | live | · | · | · |
| Disengage-derived | · | · | · | live |
| **LIVE COUNT** | **5** | **6** | **6** | **4** |

vs **10** if ungated everywhere. State-gating roughly halves simultaneous modifiers, which (a) reduces the raw σ-sum feeding the soft cap — F2 attacked at the source — and (b) shrinks each state's decision — F6.

**Physical grounding:** Stance Counter dies once stances dissolve into a bind; Tactile reading only exists in contact; Perception/Facing is irrelevant in a locked bind (you feel, not see). The gating is verisimilitude, not arbitrary.

---

## 5. Combined system — worked transition

Ilse (Thrust Duelist set 5/5, Forward-point, depth-3 thrust, Pool 17D) vs Hugo (Centered, Hand-led), **Closing** state. Live modifiers (σ-units, + = Ilse-favoring):

| Live modifier (Closing) | σ |
|---|---|
| Stance Counter (Fwd-pt vs Centered) | +0.70 |
| Reaction-aspect (Hand-led vs depth-3) | +0.00 |
| Reading-modifier (Ilse read Hugo) | +0.50 |
| Set bonus (Thrust Duelist 5/5) | +0.35 |
| Weapon phase-strength (thrust @ closing) | +0.35 |
| Perception/Facing (square) | +0.00 |
| **Raw sum** | **+1.90σ** |
| **After soft cap (M_max=1.5)** | **+1.28σ** |

Ob shift = −1.28σ × σ₁₇ (=3.30) = −4.22 → effective Ob = 2.0 − 4.22 = −2.22 → **P(thrust Success) = 99.7%** (vs 92.7% with no modifiers).

**Sim-tuning flag (honest):** a strong pool + full setup yields near-certain basic sub-actions. This is the intended front-end-strategy payoff (good setup → reliable execution), and the bout's *variance* lives in its multiple transitions and damage/wound rolls, not single sub-actions. But if 99.7% feels degenerate, levers are: lower `M_max` to ~1.0–1.2σ, raise base Ob for sub-actions, or raise sub-action Ob with depth. Phase-11 sim decides. The point of Piece 2 is that the *small-pool* end no longer forecloses; the *large-pool* end's reliability is a separate tuning question.

---

## 6. The genuine design choice: σ-space (A) vs dice-space (B)

Both resolve F2 (soft cap + state-gating). They differ on F1 and on methodology consistency.

### Option A — σ-space + soft cap + state-gating
- **Resolves F1 fully** (uniform impact modulo irreducible baseline residual) and makes the cap uniform.
- **Cost:** combat modifier *math* differs from other Valoria d10 systems (social contest, fieldwork, mass combat — all dice-space). This is the S (smoothness) concern: "calculations consistent in methodology."
- **Mitigation:** the player-facing level abstraction (§2.3) makes σ-space invisible — the player sees advantage *levels* in combat exactly as they might elsewhere. The inconsistency is engine-internal only. And σ-space could be adopted Valoria-wide later if full consistency is wanted (separate decision).

### Option B — dice-space + soft cap + state-gating
- **Resolves F2** (soft cap + state-gating, same as A).
- **F1 only partially:** modifiers remain non-uniform by √N (the diagnostic's F1 stands as accepted substrate limitation); the cap value must be made pool-aware to be fair (verified: a flat dice cap gives 50pp@3D vs 37pp@20D max impact).
- **Benefit:** methodology identical to all other Valoria systems (S preserved); simpler engine (no σ transform).

### Honest recommendation
**Lean A**, because F1 is a real correctness-R defect and σ-space resolves it cleanly while the player-facing abstraction neutralizes the S cost at the experience layer. But **B is legitimate** — if Valoria values one uniform resolution methodology across all systems above resolving F1, B is the consistent choice and F1 stays a documented substrate limitation (which the diagnostic already accepted as the fallback). This is a Jordan call; both are specced and ready.

---

## 7. Cross-scale / cross-system consistency (per all-scales directive)

- **Mass combat:** uses canonical Martial/Discipline pools, not the bout state-graph. Under Option A, mass-combat modifiers would remain dice-space (or adopt σ-space if Valoria goes engine-wide). The *player-facing* level abstraction can be shared regardless, preserving experiential consistency. No mechanical coupling broken (§15.2 transitions preserved).
- **Social contest:** dice-space currently. Same as mass combat — Option A leaves it dice-space unless engine-wide adoption. The Concentration shared-pool (F3) is independent of the modifier system; unaffected.
- **Fieldwork:** deterministic five-filter chain (mostly no dice). σ-space modifiers don't apply to deterministic accounting; no conflict.
- **Scope:** Piece 2 governs *personal-combat bout-transition modifiers only*. It does not alter base Pool composition, damage formulas, Thread integration, or World Bridge.

---

## 8. How Piece 2 lands in the reframe

Per the blueprint state-graph: each **bout-state transition** computes its probability from the opposed Pool roll adjusted by the **state-gated** modifier set, summed in **σ-units**, **soft-capped**, converted to an Ob shift. Concretely, this replaces the old §12.3 "Effective Ob = base + Σ(all modifiers)" with:

```
For a sub-action transition in bout-state S:
  live = modifier sources gated live in S (§4 table)
  net_σ = Σ(aggressor-favoring levels→σ in live) − Σ(defender-favoring levels→σ in live)
  eff_σ = 1.5 · tanh(net_σ / 1.5)
  effective_Ob = base_Ob(sub-action) − eff_σ · 0.8·√Pool
  P(transition) from continuous engine at (Pool, effective_Ob)
```

This is the §12.3 rewrite for the implementation pass.

---

## 9. Verification log (this piece)

- F1 dice-space non-uniformity: +2 Ob = 42.6pp@3D vs 21.2pp@20D ✓
- σ-space uniformity: +0.7σ = 25.8pp at ALL pools (50% baseline) ✓
- Residual Source B characterized: 13.8–27.3pp across baselines, irreducible ✓
- Soft cap F2 resolution: 0% → 9.2% at worst case, no dead-zone ✓
- σ-space cap uniformity: ~43pp at all pools vs dice 37–50pp ✓
- State-gating: 10 sources → 4–6 per state ✓
- Worked transition computed end-to-end ✓

`[CONFIDENCE: high on all numerical claims (verified in-script); medium on M_max=1.5σ and level→σ values (sim-tunable, Phase-11); the σ-space-vs-dice-space recommendation is a genuine judgment call presented for Jordan, not pre-decided]`
`[SELF-AUTHORED — bias risk: I proposed σ-space as the F1 fix two turns ago; here I verified it works AND surfaced its honest residual (Source B), its S cost, and a legitimate simpler alternative (B) rather than presenting σ-space as the only answer]`
