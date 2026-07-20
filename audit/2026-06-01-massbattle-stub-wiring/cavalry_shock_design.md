# Cavalry Shock as a Moral Primitive — Phase 3 Design (PROPOSAL)

**Date:** 2026-06-01 · **Engine:** `tests/sim/sim_mb_sigma.py` @ `8b50144c` · **Gate:** PER_CELL=1 only
`[SELF-AUTHORED — bias risk]` engine is largely my own work this session; design stated as an independent reviewer; magnitudes are Jordan-vetoable.

This answers the Phase-3 Jordan gate (delegated under the project-owner mechanical-tier grant 2026-06-01): **(1)** the speed-differential morale-shock magnitude and exactly which defender states negate vs amplify it; **(2)** whether facing→deals-less stays emergent or needs an explicit gate. Built bottom-up from the engine + canon; validated top-down against military scholarship.

---

## PART 1 — THE TOP-DOWN ANCHOR (what reality says)

**Primary source — Ardant du Picq, *Battle Studies* (the engine's stated morale anchor):**
- "There is no shock of infantry on infantry. There is but a moral impulse." Combat is decided by which side's **cohesion fails first**, not by physical collision.
- He distinguishes **mechanical (physical) shock** from **moral shock**. Cavalry's weapon is overwhelmingly the *moral* one: a body of horse bearing down breaks the defender's nerve, or it does not — and "mounted, to flee is so easy."
- The unit's chief enemy is **terror**; tactics is the art of maintaining cohesion despite it. Cohesion is a function of **order, depth, discipline, and not being taken from a direction you cannot face.**

**Quantified historical cases (the gate, with numbers):**
- **Waterloo 1815** — Ney's ~4,500 cuirassiers charged steady Allied squares for an hour and broke *none*: "virtually impossible for cavalry to break a well-disciplined infantry square without support from artillery or friendly infantry." Squares were "generally impenetrable to cavalry." A formed, disciplined, deep formation ≈ **shock-immune**.
- **Albuera 1811 (Colborne's brigade)** — the *same era's* cavalry caught infantry **in line** (not square) and destroyed it: **1,250 of 1,650 men lost (~76%)**. Identical weapon, opposite outcome — the only variable is the defender's formation/order.
- **Hastings 1066** — Norman cavalry could **not** break the Saxon shield wall frontally; only after the feigned retreat broke the wall's *discipline* did the same cavalry annihilate the now-disordered pursuers. (Repo `precedents_warfare.md §1.1`.)
- **Cannae 216 BC / Adrianople 378** — cavalry shock from the **rear/flank** on a pinned or disordered mass was catastrophic; the encircled body could not face the threat. (Canon A.4 Encirclement exception removes the morale cap for exactly this — Cannae/Trasimene.)
- **Swiss pike (Grandson/Morat 1476)** — disciplined deep pike repelled Burgundian heavy horse through **cohesion**, not equipment. (Repo §3.1.)

**The regularity (not a design choice — the dominant historical pattern):** cavalry shock is a **moral-channel** effect whose magnitude is **highly nonlinear in the defender's preparedness** — near-zero against braced + deep + disciplined infantry facing the charge; catastrophic against in-line / shallow / disordered / flanked / already-shaken infantry.

---

## PART 2 — THE BOTTOM-UP PRIMITIVES (what the engine already has)

Every gate input below is **existing engine state** — nothing invented:

| Anchor concept | Engine primitive | Location |
|---|---|---|
| charge fired (fast body bears down, penetration survived) | `a_pen > 0` after depth absorption | L1731 puncture block |
| "moral, not physical" channel | the σ-leverage **morale** channel `_morale_sigma` | L1320 / applied L1739 |
| braced / "cannot advance" (Shield Wall) | `stance == "hold"` (hold ⇒ cannot advance) | L733 / L809 |
| disciplined (holds formation) | `discipline` tiers (≥5 / ≥3 / ≥1 ⇒ mult 1.0/0.7/0.4) | L821 |
| deep (ranks absorb) | `_defender_depth(unit, cells)` mean engaged-column depth | L1501 |
| facing — can it face the charge? | octagon `GREEN<45° / YELLOW 45–90° / RED≥90°` | L526 / L1582 |
| already shaken (amplifier) | `morale / morale_start` fraction | (same as `_morale_sigma`) |
| dangling magnitude + window | `PC_CHARGE_SIGMA=0.55`, `PC_CHARGE_TICKS=3` | L1356–57 (UNUSED) |

**Key bottom-up correction.** The dangling `PC_CHARGE_SIGMA` comment reads "per-rank-of-unabsorbed-penetration δσ a charger gets on impact" — i.e. a **charger-offense** boost. But the puncture path (L1733: `ns_a += min(PUNCTURE_CAP,int(a_pen))*SIGMA_PER_D`) **already** gives the charger an offense boost scaled by exactly that penetration. Wiring the constant as first described would **double-count** the puncture — the same NERS-N/E defect that disabled `_envelopment_sigma` (L1353). The historically-correct primitive is the **defender-side moral shock**, a *different channel*: it lowers the **defender's** effectiveness (morale-σ), is **gated by discipline/stance/facing** (not absorbed by depth alone the way puncture is), and **decays** once the charge stalls into mêlée. So the constant is **repurposed to its correct role**, which also retires the dead apparatus (NERS-N).

---

## PART 3 — THE DESIGN

### 3.1 The primitive
On a tick where a charge fires against a defender column-group (`pen > 0` after absorption — a faster body out-momentumed the defender and penetration survived depth), apply a **defender morale-shock δσ**:

```
shock_σ(defender) = − PC_CHARGE_SIGMA × G_face × G_brace × A_shaken      (≤ 0)
```

applied to the **defender's** offensive net successes that exchange (it fights worse — the moral impulse), via the existing morale channel so it composes with `_morale_sigma` rather than forming a parallel one (**Lesson 1: one variable, one role**).

### 3.2 The gate (this is the whole design — the magnitude is secondary to the gate shape)

**`G_face` — can the defender face the charge?** (octagon zone of the charger vs the defender cell)
- GREEN (frontal, <45°): `G_face = G_FRONT` (small — a faced charge is mostly absorbed by the formation)
- YELLOW (flank, 45–90°): `G_face = 1.0`
- RED (rear, ≥90°): `G_face = G_REAR` (>1 — Cannae/Adrianople; you cannot brace a direction you cannot see)

**`G_brace` — is the defender a prepared formation?** (the Waterloo-square gate; multiplicative so a *fully* prepared defender drives the shock toward zero)
```
G_brace = clamp( B_stance × B_disc × B_depth , G_BRACE_FLOOR , 1.0 )
  B_stance = HOLD_BRACE if stance=='hold' else 1.0        # hold = Shield Wall "cannot advance"
  B_disc   = lerp from DISC_BRACE_FULL (disc>=5) .. 1.0 (disc<=2)   # disciplined holds formation
  B_depth  = lerp from DEPTH_BRACE_FULL (depth>=DEPTH_REF) .. 1.0 (depth<=1)  # deep absorbs
```
A `hold` + disc≥5 + deep defender ⇒ `G_brace → G_BRACE_FLOOR` (≈0): the square Ney could not break. A `balanced`, disc-5, shallow line ⇒ `G_brace ≈ 1`: Albuera.

**`A_shaken` — is the defender already wavering?** (Hastings-after-the-feint; panic compounds)
```
A_shaken = 1.0 + SHAKEN_GAIN × (1 − morale/morale_start)     # 1.0 fresh .. up to 1+SHAKEN_GAIN routing
```

### 3.3 The decay window (`PC_CHARGE_TICKS`)
Historically the moral impulse is **at the moment of impact**; if the defender survives it, the cavalry is now a stalled body in mêlée (blown horses, no momentum) and the edge is spent (du Picq). The engine gives this **for free**: the charge only fires while there is a *speed/momentum differential* (`a_mom > b_mom`, L1724) — once both bodies are locked and stationary the differential vanishes and the shock stops firing **emergently**. So `PC_CHARGE_TICKS` is **not needed as a separate counter** — modelling it would be redundant apparatus (NERS-E). *Decision: retire `PC_CHARGE_TICKS`* (the momentum differential already bounds the window); keep only `PC_CHARGE_SIGMA`.

### 3.4 Why this is not double-counting (the live risk)
- **Puncture** (`charge_pen`→`a_pen`→charger ns): *physical* penetration, gated by **depth**, boosts the **charger**. Unchanged.
- **Shock** (this primitive): *moral* collapse, gated by **discipline/stance/facing**, lowers the **defender**. New.
Different sign, different target, different gate. They co-vary (both keyed on the charge) but measure different things — *provided* the empirical re-test shows adding shock doesn't blow C1/C4 out of band (Stage-4 validation). If it does, the magnitude is too high and gets cut.

---

## PART 4 — TOP-DOWN VALIDATION PLAN (how much fidelity the emergent system has)

The C1–C4 gauge rows (committed `b7116bc4`) are the historical bands. New rows isolate the **gate** specifically:

| New row | Setup | Historical target | What it measures |
|---|---|---|---|
| **C5** | cav Arrowhead → **shaken** Line (morale 2/6, balanced) | charge breaks a wavering line — HIGH (Hastings-after-feint, Albuera) | `A_shaken` amplifier |
| **C6** | cav Arrowhead → **braced shallow** Line (hold+disc8, depth≈1) | bracing alone (no depth) still repels frontally — LOW/contested (square mechanic is formation+discipline, not just mass) | `B_stance×B_disc` vs depth |
| **C7** | cav **rear/flank** vs braced Line (hold+disc8, deep) | bracing **bypassed** from the rear — HIGH (Cannae/Adrianople: you can't face what's behind you) | `G_face` RED overrides `G_brace` |

**Fidelity acceptance:**
1. C1–C4 stay in band (no double-count regression).
2. C5 ≫ C1 (shaken amplifies); C6 stays repelled (frontal brace holds without depth); C7 ≫ C2 (rear bypasses brace).
3. PER_CELL=0 byte-exact (shock is PER_CELL-gated).
4. Monotonicity: `frontal-braced-deep < frontal-braced-shallow < frontal-unbraced < flank < rear`, and `fresh < shaken` — the emergent ordering must reproduce the historical ordering. **Fidelity = how cleanly the emergent win-rates reproduce that ordering and the C1–C7 bands.**

If the emergent octagon already produces C7≫C2 and the facing ordering **without** an explicit attacker-output gate, then **gate question (2) is answered: keep facing emergent** (the octagon is sufficient; adding an explicit gate would be redundant — NERS-E). The C-row measurements decide it, not assertion.

---

## PART 5 — CONSTANTS (all Class-B sim-tunable; Jordan-vetoable; calibrated against the bands, not invented)

| Constant | Proposed | Rationale (tuned in Stage 4) |
|---|---|---|
| `PC_CHARGE_SIGMA` | 0.55 (existing) | max shock ≈ 2.75 die-equiv (SIGMA_PER_D=0.2); same order as 2–3 canonical morale triggers; the **cap**, reached only at rear/shaken |
| `PC_SHOCK_FRONT` (`G_FRONT`) | 0.15 | faced charge mostly absorbed — square holds frontally |
| `PC_SHOCK_REAR` (`G_REAR`) | 1.6 | rear bypass (octagon RED already −2D; shock amplifies) |
| `PC_SHOCK_BRACE_FLOOR` | 0.05 | braced+disc+deep ⇒ ≈0 shock (Ney's failure) |
| `PC_SHOCK_HOLD_BRACE` | 0.35 | hold stance alone cuts shock to ~⅓ (Shield Wall) |
| `PC_SHOCK_DISC_FULL` | 0.35 | disc≥5 cuts shock to ~⅓ (steady troops) |
| `PC_SHOCK_DEPTH_FULL` | 0.5 | deep (≥DEPTH_REF) halves shock |
| `PC_SHOCK_DEPTH_REF` | 4.0 | "deep" threshold (ranks) |
| `PC_SHOCK_SHAKEN_GAIN` | 1.0 | routing-adjacent defender takes up to 2× shock |

These are **starting values**; Stage 4 tunes them so C1–C7 sit in their historical bands, then reports the residual as the fidelity measurement. Final committed values may differ from the table above.
