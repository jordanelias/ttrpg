# Weapon-Physics NERS Reconciliation — Path B, Grounded

**Status:** Audit / reconciliation record. Class-C mechanical findings, Jordan-vetoable.
**Session:** 2026-06-06. **Scope:** personal combat (`designs/scene/combat_engine_v1/`) weapon-physics layer.
**Decision context:** Jordan directed **path B** (Valoria's combat gains a quantitative weapon-physics layer — a structural call, his) and "proceed all."

> **CORRECTION (2026-06-06, same session — supersedes the first commit of this file).** The earlier "broken-mirror showstopper" is a **MEASUREMENT ERROR and is WITHDRAWN.** The mirror is **fair.** The flawed win-rate metric divided A-wins by *total* fights including draws; sabre mirrors draw ~79% of the time, so "sabre A=10%" was misread as a 90% loss — in fact B also wins ~10% and ~79% draw, and **among *decided* fights it is 49.5% (symmetric).** Corrected mirror balance (A-of-decided): all weapons 48–52%. `[CORRECTION: §5/§6/§7 — A_wins/total vs A_wins/decided; draws not excluded]`

`[READ:]` provenance: `combat_engine_v1/{combatant,core,config,systems,geometry,wrapper}.py` (full); `designs/audit/2026-05-29-combat-armature/weapon_axes_v2.md` (full); `tests/sim/v32-combat-balance/` module set. Baseline, MoI bake, MoI→tempo wiring, mirror scan, and the corrected re-measurement were executed in-container this session.

---

## 1. Input semantics — GROUNDED (fixes the prior R-fail on inputs)

The physical fields (`mass`, `pob_frac`, `head_len`, `grip_len`) were added to `combatant.py` (e414098) with **no canonical definition** — `weapon_axes_v2` defines only categorical axes. Adopted semantics (mechanical-tier, **vetoable**), validated top-down against real weapons:

- **`mass` = kilograms.** · **`head_len`/`grip_len` = forward/rear lever arms, in FEET** (hand→tip ; hand→butt). · **`pob_frac` = (hand→balance) / head_len.**

Validation (balance = `pob_frac·head_len`, ft→cm vs real): spear 70=70 · mace 33=33 · rapier 10=10 · greatsword 24~18 · staff 4~2. `[CONFIDENCE: high — top-down validated]`

---

## 2. MoI model — unified, elegant ("three regimes" was a mislabel)

Two orthogonal axes: mass-distribution (sets `r_eff`) × delivery-mode. One law:

```
MoI = mass · r_eff²
  SWING      r_eff = pob_frac · head_len     (blade, mass at CG)
  POLE       r_eff = head_len / √3           (uniform rod about rear hand; spear, staff, poleaxe)
  HEAD-HEAVY r_eff = head_len                 (mass at the head, top-heavy; mace)   ← "centre" was wrong
```

Computed: rapier 0.13 · longsword 0.215 · greatsword 1.69 · spear **20.17** · staff 3.92 · **mace 3.89** (head-heavy; was 1.40 under CG — 2.78× more sluggish) · poleaxe 4.03. Spear polearm MoI = 24.0× the lumped sword proxy (matches the handoff's ~25× prediction). `[ASSUMPTION: regime classification POLE={spear,staff,poleaxe}, HEAD-HEAVY={mace} — vetoable]`

---

## 3. Baseline captured (live engine — prior sessions never ran it)

```
MIRROR (A-of-decided)     48–52% for ALL weapons — FAIR (see §5)
ARMOUR none vs heavy       heavy wins ~92% — directional ✓
no-one-shot               HOLDS for defender end≥2 (health 24–52 > 18); breaks only at end=1 floor (health 14)
max overwhelming hit      18 FLAT across strength 3→7   ← tanh-saturated; strength adds nothing at the top
reach                     GOVERNS the unarmoured tier (real; low-draw matchups)
```

---

## 4. The build, and why the layer is INERT

`MoI` baked behaviour-neutral (baseline byte-identical). `MoI→tempo` wired (replacing the binary `wt` mass term; `HANDS_COMMIT` unchanged; bounded by `MAX_TEMPO_PEN`; new `MOI_TEMPO_K=0.30`). It corrected a real cadence **inversion** — the spear (MoI 20.17) had tempo 2.0 with **zero** weight penalty while the mace (MoI 3.89) was penalised to 1.2; post-wiring spear→1.2, staff→1.41, mace→1.41.

But correcting cadence **did not change outcomes**:

```
mace vs staff      5.5% → 8.0%    (staff still wins ~92% on REACH; 0 draws)
longsword v spear 20.7% → 22.9%   (spear still wins ~80% on REACH)
```

Reach dominates; mass/cadence is ~outcome-irrelevant. The MoI→tempo wiring was **NOT committed** (fails NERS-N — corrects an inconsistency with no play consequence). The MoI bake is local-only, **not committed to engine** (unconsumed = dead data, fails NERS-E).

---

## 5. Mirror is FAIR; what varies is DECISIVENESS (draw rate) — [corrected]

Corrected measurement (n=1500, A/B/draw %, and A-among-decided):

```
weapon       A%    B%    draw%   A-of-decided
arming      46.0  46.3   7.7      49.8   ← the one weapon the prior claim checked
longsword   48.0  51.5   0.5      48.2
poleaxe     50.3  49.7   0.0      50.3
mace        49.6  49.1   1.3      50.2
spear       48.3  48.1   3.6      50.1
rapier      46.5  43.5  10.0      51.6
staff       46.2  42.1  11.7      52.3
greatsword  32.1  33.2  34.7      49.2
sabre       10.5  10.7  78.7      49.5   ← symmetric; the 79% draw rate, NOT a 90/10 loss
```

**The mirror invariant holds.** What is real and notable: **draw/decisiveness rate varies hugely by weapon** — two equal sabres reach the bout limit unresolved ~79% of the time, greatswords ~35%, vs longsword 0.5% / poleaxe 0%. This is a *decisiveness/feel* property (the engine explicitly allows unresolved as a legitimate outcome — `fight()` comment), **not** a fairness defect. Whether a ~79% undecided rate for equal fast curved-cutters is desirable is an open feel question, not a bug.

---

## 6. NERS verdict (objective, all directions — corrected)

```
SYSTEM: personal combat + weapon-physics layer (path B, grounded)
VERDICT: the ENGINE is sound; the weapon-physics LAYER is groundable + elegant but INERT.

N  FAIL    MoI→tempo moves outcomes ~2pts; reach governs. Layer corrects an inconsistency with no play consequence.
R  PASS    Mirror FAIR (corrected); armour directional; no-one-shot holds end≥2; 95% cap respected.
           Reach-dominance produces near-cap extremes (staff>mace 94.5%) but within the legal cap — a diversity
           question, not a defect. Draw-rate variation noted (§5), not a fairness fault.
S  PASS    Engine transitions cleanly; one-formula physics is smooth.
E  ~        Grounded substrate is one elegant formula; B's ontology expansion is consciously Jordan's.
           BUT the layer is inert — committing unconsumed MoI fields would be dead data (so it stays out of engine).
```

The earlier R-FAIL ("mirror invariant broken") is **withdrawn** — it was the §5 metric error.

---

## 7. Reframed priorities + open decisions (Jordan) — corrected

1. **Reach-dominance is the real structural issue** (not a broken mirror — that was my error). It is *why* the physics is inert and why some matchups are near-deterministic. If weapon mass/feel is to matter (the top-heavy-mace goal), the lever is **reach-balance** or the **damage `tanh` saturation** — not mass.
2. **Grounded MoI substrate** (§1–2) is correct and preserved here; inert until (1), so it stays out of engine code.
3. **Decisiveness/draw-rate** (§5) — open feel question: is a ~79% undecided sabre-mirror rate (and 35% greatsword) acceptable, or should the bout-resolution be tightened?

`[OPEN — Jordan] (a) canonize §1 input semantics into weapon_axes_v2 if/when the physics layer is activated; (b) reach-dominance vs tanh-saturation as the lever for weapon distinctiveness; (c) draw-rate/decisiveness target.`

---

Citations:
  - designs/scene/combat_engine_v1/combatant.py
  - designs/scene/combat_engine_v1/core.py
  - designs/scene/combat_engine_v1/config.py
  - designs/scene/combat_engine_v1/systems.py
  - designs/scene/combat_engine_v1/wrapper.py
  - designs/audit/2026-05-29-combat-armature/weapon_axes_v2.md
