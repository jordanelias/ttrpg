# Weapon-Physics NERS Reconciliation — Path B, Grounded

**Status:** Audit / reconciliation record. Class-C mechanical findings, Jordan-vetoable.
**Session:** 2026-06-06. **Scope:** personal combat (`designs/scene/combat_engine_v1/`) weapon-physics layer.
**Decision context:** Jordan directed **path B** (Valoria's combat gains a quantitative weapon-physics layer — a structural/ontological call, his) and "proceed all." This records the executed build, its empirical verdict, and a showstopper the re-baseline uncovered.

`[READ:]` provenance: `combat_engine_v1/{combatant,core,config,systems,geometry,wrapper}.py` (full); `designs/audit/2026-05-29-combat-armature/weapon_axes_v2.md` (full); `tests/sim/v32-combat-balance/` module set (engine deps). Baseline, MoI bake, MoI→tempo wiring, and mirror scan were executed in-container against the live engine this session.

---

## 1. Input semantics — GROUNDED (fixes the prior R-fail)

The physical fields (`mass`, `pob_frac`, `head_len`, `grip_len`) were added to `combatant.py` (e414098) with **no canonical definition** — `weapon_axes_v2` defines only categorical axes (reach/weight/hands/head/speed/handling). The following semantics are adopted (mechanical-tier, **vetoable**), validated top-down against real weapons:

- **`mass` = kilograms.**
- **`head_len` / `grip_len` = forward / rear lever arms, in FEET** (hand→tip ; hand→butt).
- **`pob_frac` = (hand→balance distance) / head_len.**

Validation (balance = `pob_frac·head_len`, ft→cm vs real balance-ahead-of-hand):

| weapon | model balance | real balance |
|---|---|---|
| spear | 70 cm | 70 cm |
| mace | 33 cm | 33 cm |
| rapier | 10 cm | 10 cm |
| greatsword | 24 cm | 18 cm |
| staff | 4 cm | 2 cm |

Several reproduce exactly. `[CONFIDENCE: high — top-down validated against real weapon dimensions]`

---

## 2. MoI model — unified, elegant (corrected from the inherited "three regimes")

The handoff's "three regimes" was an unaudited mislabel — it is **two orthogonal axes**: mass-distribution (sets `r_eff` in one MoI law) × delivery-mode (cut/thrust/blunt). One formula:

```
MoI = mass · r_eff²
  SWING      r_eff = pob_frac · head_len     (blade, mass at CG; rapier…halfsword)
  POLE       r_eff = head_len / √3           (uniform rod about rear hand; spear, staff, poleaxe)
  HEAD-HEAVY r_eff = head_len                 (mass at the head, top-heavy; mace)   ← "centre" was wrong; a mace is head-heavy
```

`[ASSUMPTION: regime classification POLE={spear,staff,poleaxe}, HEAD-HEAVY={mace}, else SWING — vetoable]`

Computed MoI (selected): rapier 0.13 · arming 0.10 · longsword 0.215 · greatsword 1.69 · sabre 0.20 · dagger 0.009 · spear **20.17** · staff 3.92 · **mace 3.89** (head-heavy; was 1.40 under the CG model — 2.78× more sluggish) · poleaxe 4.03 · halfsword 0.04.

Polearm cross-check: `(1/3)·m·head_len²` for the spear is 24.0× the lumped sword proxy — matching the handoff's independent ~25× prediction.

---

## 3. Baseline captured (live engine, this session — prior sessions never ran it)

```
MIRROR arming v arming    45.7%   ~holds
ARMOUR none vs heavy       8.3%   directional ✓
no-one-shot               HOLDS for defender end≥2 (health 24–52 > 18); breaks only at end=1 floor (health 14)
max overwhelming hit      18 FLAT across strength 3→7   ← tanh-saturated; strength adds nothing at the top
95% cap                   3/66 unarmoured matchups at the boundary — cap doing its job
reach                     GOVERNS the unarmoured tier
```

Correction to the handoff's "no-one-shot holds": it holds for normal stats; the only breach is the end=1 floor.

---

## 4. The build, and why the layer is INERT

`MoI` baked behaviour-neutral (baseline byte-identical). `MoI→tempo` wired (replacing the binary `wt` mass term; `HANDS_COMMIT` unchanged; bounded by `MAX_TEMPO_PEN`; new `MOI_TEMPO_K=0.30`). It corrected the cadence **inversion** — the spear (MoI 20.17) had tempo 2.0 with **zero** weight penalty while the mace (MoI 3.89) was penalised to 1.2; post-wiring spear→1.2, staff→1.41, mace→1.41.

But correcting cadence **did not change outcomes**:

```
mace vs staff      5.7% → 8.0%    (staff slowed 2.0→1.41, mace sped 1.2→1.41; staff still wins ~92% on REACH)
longsword v spear 20.7% → 22.9%   (spear slowed 2.0→1.20; spear still wins ~77% on REACH)
```

Reach dominates; mass/cadence is ~outcome-irrelevant. **The MoI→tempo wiring was NOT committed** (it fails NERS-N — corrects an inconsistency with no play consequence). The MoI bake is local-only, **not committed to engine code** (committing inert, unconsumed fields would be dead data — fails NERS-E).

---

## 5. SHOWSTOPPER — the mirror invariant is broken

A same-weapon fight must be ~50/50. It is not (A% over seeds 1–4):

```
rapier      47.8 44.8 46.0 47.2    ~OK
arming      45.5 45.0 48.2 44.2    ~OK   ← the ONLY weapon the prior "mirror=50 holds" claim checked
longsword   46.0 50.2 48.2 45.2    ~OK
dagger / spear / staff / mace      ~OK
greatsword  31.2 28.0 34.2 32.0    SKEWED   (B wins ~68%)
sabre       10.2  9.5 13.2 12.2    BROKEN   (B wins ~90%)
poleaxe     54.0 51.5 53.8 55.5    mild skew (A favoured)
```

A sabre fighting an identical sabre loses ~90% of the time depending only on which slot it occupies. This is a structural attacker/defender asymmetry in `fight()` (weapon × initiative). **Pre-existing, not from the wiring** — proof: greatsword tempo is capped at 0.8 both before and after the patch (identical), yet its mirror is 30%; a symmetric tempo change cannot cause an A/B asymmetry.

`[OPEN — Jordan / investigation] Mirror break in fight() — sabre 10/90, greatsword 30/70. Priority defect. Trace fight() initiative/turn-order. Confirm whether mirror≈50 is the intended invariant for all weapons (a 90/10 same-weapon result is a defect under any reading).`

---

## 6. NERS verdict (objective, all directions)

```
SYSTEM: personal combat + weapon-physics layer (path B, grounded)
VERDICT: layer is groundable + elegant but INERT; the ENGINE beneath it fails R.

N  FAIL    MoI→tempo moves outcomes ~2pts; reach governs. Corrects an inconsistency with no play consequence.
R  FAIL    Not the physics — the ENGINE: mirror invariant broken (sabre 10/90, greatsword 30/70);
           + reach so dominant no other axis affects outcomes (collapsed strategic space).
S  ~OK     Physics model smooth (one formula); engine has the initiative asymmetry.
E  PASS    Grounded substrate is one elegant formula; B's ontology expansion is consciously Jordan's.
```

---

## 7. Reframed priorities + open decisions (Jordan)

1. **Broken mirror is the priority** — perfecting weapon physics on an engine where the sabre has a 90/10 slot-bias is wasted. Trace `fight()`.
2. **Reach-dominance** is the structural reason the physics is inert — if weapon mass/feel is to matter (the top-heavy-mace goal), reach's grip on outcomes must loosen, or the damage `tanh` saturation must be addressed.
3. **Grounded MoI substrate** (§1–2) is correct and preserved here; it is inert until 1 and 2 are resolved, so it stays out of engine code for now.

`[OPEN — Jordan] (a) canonize the §1 input semantics into weapon_axes_v2 when/if the physics layer is activated; (b) direction on reach-dominance vs tanh-saturation as the lever for weapon distinctiveness.`

---

Citations:
  - designs/scene/combat_engine_v1/combatant.py
  - designs/scene/combat_engine_v1/core.py
  - designs/scene/combat_engine_v1/config.py
  - designs/scene/combat_engine_v1/systems.py
  - designs/scene/combat_engine_v1/geometry.py
  - designs/audit/2026-05-29-combat-armature/weapon_axes_v2.md
  - tests/sim/v32-combat-balance/ (engine resolution deps)
