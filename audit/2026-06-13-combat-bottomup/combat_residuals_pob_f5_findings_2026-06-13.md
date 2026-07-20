# Personal combat — PoB + F5 residuals (J-33): measured findings

**2026-06-13 · status: PROPOSED, Jordan-vetoable · design-gated J-33 residuals (ED-934)**

Both items are flagged "design-gated" / Jordan-open in ED-934. Nothing here is committed; the canon
engine is unchanged. Deliverable = measured worked proposals with explicit decision points. If
ratified, this lands under `designs/audit/2026-06-13-combat-residuals-pob-f5/` and the next Lane-A id
is **ED-935** (890–934 are taken; the `max+1 = 1013` heuristic is wrong for Lane A).

`[SELF-AUTHORED — bias risk]` This re-tests and partly contradicts prior Claude-authored analysis
(the 06-09 comprehensive audit's F5 framing, and this session's own PoB design hypothesis). Verdicts
are stated against that interest, not for it.

Built bottom-up against the live engine and substrate at HEAD:
`[READ: designs/scene/combat_engine_v1/{core,systems,combatant,wrapper,config,geometry,tradition}.py]`
· `[READ: tests/sim/v32-combat-balance/{r1_sigma_resolution,r2_consequence_wounds,r5_strength_stamina,m1_dice_sigma_core,r8_parity_harness,m9_wound_model_bottomup}.py + module_manifest + wound_model_resweep_results + m9_verification_ledger]`
· `[READ: designs/scene/derived_stats_v30.md §4 (via derived_stats_audit)]`
· `[READ: designs/audit/2026-06-09-personal-combat-comprehensive/comprehensive_analysis_personal_combat.md]`
· `[READ: canon/editorial_ledger.jsonl → ED-934]`

---

## §0 — Measurement frame (the gate) — VALIDATED

The 06-09 comprehensive audit uses two frames. The single-attribute parity numbers in ED-934
(mirror 49.9/50.0 · str6v4 59.5 · hist7v4 61.7 · agi6v4 65.6) are a **single decisive resolution**
(`P(net_A > net_B)`; hist7v4 → pool 13 vs 10 → Φ(1.2/3.83) ≈ 0.62 ✓ — an isolated σ-leverage
check). The F5/weapon invariants are **multi-turn `fight()`, "A-of-decided"** (draws excluded); the
.162-draw mirror rules out single-engagement.

F5 and PoB both live in the `fight()` frame. My assembled engine reproduces both `fight()`-frame
anchors (N=1500):

| Anchor | This run | Audit | Match |
|---|---|---|---|
| longsword mirror | .481 | .495 | ✓ (noise) |
| greatsword mirror | .492 | .510 | ✓ |
| spear mirror | .503 | .500 | ✓ |
| sabre mirror | .507 (9% draws) | .478 | ✓ (high-draw open Q, carried) |
| **wound handicap** 0w / 1w / 2w (longsword mirror, A pre-wounded) | **.490 / .329 / .215** | **.506 / .326 / .215** | ✓✓ near-exact |

`[NULL: assembly-fidelity check — engine @ HEAD reproduces the committed parity anchors; no drift]`.
The frame is canonical; deltas measured below are trustworthy. `[CONFIDENCE: high]` on the frame.

---

## §1 — F5: the wound-penalty model

### Canon constraint (load-bearing)

`WoundTracker.pool_penalty()` = `−1D per wound to all Pools`, cited **Class-A canonical**:
`[canonical: derived_stats_v30 §4.1 — each wound: -1D to Pools; no Ob penalty]` (PP-717). This is
ratified canon, **not** a Class-C wiring. ED-934's "wound model → stamina_max/conc_max/execution"
therefore cannot be read as *replace the −1D-to-pools* — that is a retcon of authored canon, which is
barred. The canon-safe readings are **augment** (keep the −1D, add channels) or, if Jordan wants the
−1D's weight reduced, a **derived_stats §4.1 canon amendment** (Jordan's call, not Claude's).

### The channels already exist in the engine's idiom

The three ED-934 channels map onto live wiring: `stamina_max` → fatigue (`TEMPO_FATIGUE_K`, act
costs) → tempo; `conc_max` → the consistency / disruption-resistance terms = **execution quality**.
So a wound→{stamina_max, conc_max} model covers all three named channels through existing couplings.

### Measured (longsword mirror, history 3 / pool 9, A pre-wounded, A-of-decided)

| Variant | 0w | 1w | 2w | Δ at 1w |
|---|---|---|---|---|
| baseline (canon −1D pool only) | .481 | .334 | .208 | **−14.7pp** |
| F5-A augment (−1D pool + smooth Ks .12 / Kc .10) | .481 | .292 | .140 | −18.9pp |
| F5-B redirect (pp 0 + smooth Ks .05 / Kc .035) | .487 | .319 | — | −16.8pp |

The smooth stamina/conc channels are **potent**: they compound over the multi-turn fight (less gas →
more fatigue → slower tempo → lose more exchanges → felled sooner), so adding them on top of the −1D
makes wounds bite *harder* (−18.9pp vs −14.7pp), and matching the canonical magnitude on smooth
channels alone needs *small* knobs (Ks ≈ .05).

### The key finding — the Lesson-2 non-uniformity washes out

The 06-09 audit flagged the wound −1D as a Lesson-2 candidate: its **per-single-roll** impact is
non-uniform (−9.7pp at pool 5→4 vs −3.5pp at pool 13→12, via 1/√N). Tested at the **win-rate** level,
at matched total handicap (N=1500):

| Variant | low pool (hist0=6) Δ1w | high pool (hist7=13) Δ1w | non-uniformity spread |
|---|---|---|---|
| baseline (canon −1D pool) | −17.0pp | −16.8pp | **0.2pp** |
| redirect (smooth, matched) | −17.7pp | −17.5pp | **0.2pp** |

The per-roll non-uniformity **does not produce a measurable build-dependent win-rate distortion** in
multi-turn combat — it averages out over the exchanges. (An earlier 4.2pp reading was Monte-Carlo
noise; spread noise floor ≈ ±5pp at N=1500.) `[CONFIDENCE: medium — point estimates 0.2–4.2pp, below
the noise floor; firming needs higher N, but the signal that it is small is robust]`.

So the redirect's **primary stated motivation (fixing the non-uniformity) is not supported** — the
canonical −1D-pool is already uniform enough where it matters. Mirror stays ~.50 throughout
(`[NULL: mirror fairness preserved under every F5 variant — .48–.52]`).

### F5 — NERS verdict

- **N**: the canonical −1D-pool is necessary and sufficient as the wound penalty. Adding stamina/conc/
  execution channels is **not necessary** on correctness grounds (the uniformity defect they were
  meant to fix is not present at the gameplay level). Adding them as *richness* is a legitimate but
  optional design choice.
- **R / S**: canonical model holds at its extremes (handicap monotone, uniform across pools, bounded
  by MaxWounds + felled). Augment makes wounds heavier (a balance lever, not a bug). Redirect amends
  Class-A canon.
- **E**: keeping one channel (−1D pool) is the elegant option; the augment adds two more channels —
  justified only if the richer wound model is wanted for its own sake.

**Recommendation (Jordan-vetoable):** *keep the canonical −1D-to-pools as-is.* Treat the
"→ stamina_max/conc_max/execution" redirect as **optional flavour** — a richer model where wounds sap
gas and focus, not only dice — to be adopted (as F5-A augment, canon-safe) only if Jordan wants wounds
more punishing and more textured; tuned **small** (Ks ≈ .05, Kc ≈ .035) and with total handicap held
near the canonical −15pp/wound unless heavier wounds are the intent. Do **not** amend derived_stats
§4.1 on uniformity grounds — the measurement does not justify it.

**Jordan decision points:** (a) keep canon-only (recommended) vs adopt F5-A augment for richness; (b)
if augment, target total wound handicap (hold ~−15pp/wound, or make wounds heavier); (c) the literal
"redirect" (reduce the −1D weight) requires a derived_stats §4.1 amendment — only if (a) chooses it.

---

## §2 — PoB: `pob_frac` as the bottom-up source for percussion authority

### Correction to this session's first PoB reading `[CORRECTION: §2 — "redundant, don't wire" retracted]`

My first pass concluded `pob_frac → strike_damage` is *redundant with `coupling`/percussion* and
recommended not wiring it. That was wrong-framed, and Jordan's challenge ("is coupling/percussion
bottom-up?") exposed why. `core.coupling()` is **top-down**: it scales a blunt strike by `perc/8.0`,
where `perc` is a per-weapon integer **assigned by hand** in `combatant.WEAPONS` (mace 8, poleaxe 8,
staff 4), on top of a hand-set `RESIST[armour][mode]` table and hand-set `DELIVERY` multipliers. So
the effect `pob_frac` was "redundant" with is a **hand-tuned placeholder**, not a physical model.
`core.py` itself calls 8 the "steel-hammer reference" and `geometry.percussion_concentration()` notes
it "multiplies the percussion **authority (mass) handled elsewhere**" — the authority was always
understood to be a mass phenomenon, but operationalised as a hand-set number. `pob_frac` (with `mass`,
both sourced in `combatant.py` and consumed nowhere) is exactly that missing physical source. Its
correct role is to **derive** percussion, not duplicate it.

### The derivation (bottom-up)

Pivot ≈ the hands; total length `L = grip_len + head_len`; centre of mass at `d_com = pob_frac · L`.
From an energy-limited committed swing (`½ I ω² = W`, with `I ≈ mass · d_com²`):

- **impact momentum** `p = √(2 W I)/r ∝ √mass · pob_frac` — the `L`'s cancel, so authority depends on
  mass and the *balance fraction*, not raw length;
- **effective striking mass** at the head `m_eff = I/r² ∝ mass · pob_frac²` ( = `p²` ) — a head-forward
  weapon presents more mass at contact, stays *planted*, and transfers impulse rather than bouncing,
  which is how a blunt weapon defeats armour;
- **first moment** `M₁ = mass · pob_frac · L` — the *static* head-heaviness = the handling/control cost.
  One mass distribution sets both the authority and the control cost: a single physical source, two
  consequences (Lesson-1 clean, now grounded rather than asserted).

Authority saturates (you cannot swing an ever-heavier head ever faster; armour either fails or it does
not). Fitting a saturating law to the three validated blunt anchors:

> **`P_auth = min(8, 9.5 · (√mass · pob_frac)^0.30)`** — applied to blunt heads only.

`[SOURCE: T0 — derived from combatant.WEAPONS mass/pob_frac + the energy-limited swing model; the two
constants (scale 9.5, exponent 0.30) calibrated to the validated blunt anchors]`. Bottom-up FORM,
top-down calibration — the same "reproduce the validated values, then refine" discipline as
`geometry.py`. Only three blunt weapons exist in canon, so the exponent is calibrated, not
independently cross-validated.

### Validation — reproduces the validated outcomes; percussion now derived

| weapon | `√mass·pob` | `P_auth` | hand-set | derived row |
|---|---|---|---|---|
| poleaxe | 0.712 | 8.00 | 8 | blunt_heavy |
| mace | 0.657 | 8.00 | 8 | blunt_heavy |
| staff | 0.061 | 4.11 | 4 | blunt_light |

The heavy/light blunt row (which `RATIFIED_TABLE` row a striking weapon reproduces) is **derived by a
threshold** on `P_auth`, not hand-drawn. Feeding `P_auth` into `core.damage` in place of the hand-set
`perc` reproduces the engine's blunt damage in **11/12 cells exactly** — mace and poleaxe identical at
every armour tier; the lone delta is staff-vs-unarmoured (10 vs 9), a continuous-model refinement.
Non-blunt heads gate to `P_auth = 0`, which is correct: `core` reads `perc` **only** in its blunt
branch, so the hand-set percussion of swords/spears/rapier (4/3/1/0) is **dead data** the derivation
harmlessly retires. `[NULL: blunt mirror + blunt damage parity preserved under the derived authority —
11/12 cells identical, 1 refined ±1]`. Module: `percussion_authority.py` (self-test green).

### What still stands from the inertness measurement (correctly scoped)

Two earlier results are unaffected and remain true — but they bound *what wiring `P_auth` buys*, not
whether `pob_frac` belongs in the model:

- **Strike-coupling is saturated.** The damage `tanh` (DAMAGE_SCALE 4, cap 12) is near-saturated for
  the head-heavy blunt weapons, so a *derived* authority **reproduces** outcomes — it does not *shift*
  them (mace/poleaxe damage identical off vs on; an unsaturated cut-vs-plate cell needed an absurd
  `imp_k ≈ 40` to move a point). Making `pob_frac` *move* damage — a more head-heavy mace hitting
  measurably harder — requires leaving the saturated `tanh` + hand-set `RESIST` lookup for a continuous
  transmission model.
- **The control-cost path is inert.** `M₁` is the clean physical source for the handling cost, but the
  engine's only entry point — `overcommit_exposure`, deep-commit only — is too narrow to register at
  the win-rate level across the full magnitude sweep (`expose_k` 0→1.5 flat, both armoured and not).
  Wiring `M₁` there changes nothing without first widening that path.

So the distinction the first pass missed: `pob_frac` is the right **source** for the authority
(necessary, principled); whether wiring it *changes* outcomes is a separate, structural question
governed by the saturated `tanh` and the narrow exposure path — both fixable, both Jordan's call.

### PoB — NERS verdict (revised)

- **N — PASS (as a source).** `pob_frac` (+ `mass`) is *necessary* as the bottom-up source for the
  percussion authority the engine currently hand-assigns. It is not redundant with a physical model —
  it *is* the physical model that the hand-set `perc` stands in for.
- **R — partial.** The derived `P_auth` reproduces the validated blunt tier-list, table, and damage
  robustly. It does not *by itself* expose a finer balance gradient to the player — the `tanh` is
  saturated and the control path is inert — which is what the structural options below would change.
- **E — PASS (it removes apparatus).** One derived quantity (`√mass·pob`) replaces 11 hand-set
  `percussion` integers *and* the hand-drawn heavy/light blunt assignment, and retires the dead
  non-blunt percussion data. Net simpler, and principled.

**Recommendation (Jordan-vetoable):** adopt `P_auth` as the **derived replacement** for the
hand-assigned `percussion`. Percussion becomes bottom-up (a new weapon's authority falls out of its
mass and balance — no hand-assignment), the heavy/light blunt row is derived, and `pob_frac`/`mass`
stop being dead inputs — all while reproducing the validated outcomes. This is the honest resolution
of the PoB residual: not "redundant — discard," but "the missing bottom-up source — derive it." The
first-pass "do not wire" verdict is **retracted**; it mistook a hand-tuned placeholder for the physics.

**Jordan decision points (each independent of adopting `P_auth`):**
- (a) **Wire `P_auth` now** as a drop-in — reproduces canon, makes percussion principled, low-risk
  (recommended); vs leave it as a documented derivation pending the larger questions below.
- (b) **Go continuous** so a derived authority *shifts* damage (head-heaviness as a live gradient, not
  a reproduced rating): adopt the continuous transmission model (`v32 damage_model`/`armour_axes`,
  currently calibrated to reproduce `RATIFIED_TABLE`). A structural choice implying a re-baseline.
- (c) **Wire the control-cost half** (`M₁` → handling/overcommit): requires widening the
  `overcommit_exposure` path so head-heaviness registers — a new mechanic, not just a wiring.

(b) and (c) are the genuine design/value calls; per the project-owner contract they are parked for
Jordan, not chosen by Claude. (a) is a mechanical drop-in that reproduces the validated table and can
be staged on request.

---

## §3 — Honesty block

- `[SELF-AUTHORED — bias risk]` Re-tested this session's own PoB hypothesis and the 06-09 F5 framing;
  both came back partly negative and are reported as measured.
- `[CONFIDENCE: high]` on: frame fidelity (§0); the canonical wound-handicap curve; the §2 structural
  results that still stand (the damage `tanh` is saturated for blunt weapons; the control-cost exposure
  path is inert); and the `P_auth` derivation reproducing the validated blunt ratings/table/damage.
- `[CORRECTION: §2 — the first-pass "pob_frac is redundant, do not wire" verdict is retracted.]`
  Mid-session it emerged that `coupling`/percussion is top-down (hand-set `RESIST`/`DELIVERY` + a
  hand-assigned `percussion` 0–8), so `pob_frac`'s role is to *derive* that authority, not duplicate
  it. The corrected resolution (adopt `P_auth`) is stated against this session's earlier interest.
- `[CONFIDENCE: medium]` on: the F5 uniformity-washout magnitude (spread below the ~5pp noise floor at
  N=1500; the *direction* — that it is small — is robust; the exact value is not).
- `[GAP: execution channel]` F5's third channel ("execution") was measured *through* conc_max (which
  drives the consistency/execution term), not as a separate net_sigma penalty; a distinct execution
  term was not independently wired. Does not change the verdict (keep canon).
- Magnitudes in §1 (Ks/Kc) and §2 (imp_k/expose_k) are **Class-C proposed, sim-tunable**, not canon.
- Nothing committed. Canon engine unchanged. `pob_frac` and the wound −1D remain exactly as at HEAD.
- Sim N = 1100–1500 (point estimates ± ~3pp per cell); adequate for the qualitative verdicts, not for
  fine calibration.
