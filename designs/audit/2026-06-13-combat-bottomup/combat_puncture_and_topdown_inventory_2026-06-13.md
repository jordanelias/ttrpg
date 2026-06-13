# Combat engine — puncture model + top-down inventory

**2026-06-13 · status: PROPOSED, Jordan-vetoable · companion to `combat_residuals_pob_f5_findings_2026-06-13.md` (shares `percussion_authority.py`)**

Two requests, both bottom-up: (1) explore puncturing — thrust and the unbalanced pick — and the
hypothesis that puncture-vs-percussion comes down to head shape; (2) inventory every place the engine
is top-down. Nothing committed; the canon engine is unchanged.

`[SELF-AUTHORED — bias risk]` This audits and extends Claude-authored engine code. Findings are stated
against that interest; the §2 verdict names defects in work this project produced.

Built bottom-up against the live engine at HEAD:
`[READ: designs/scene/combat_engine_v1/{core,systems,combatant,wrapper,config,geometry,tradition}.py — all 7, full]`
· `[READ: tests/sim/v32-combat-balance/{damage_model,armour_axes}.py — docstrings + RATIFIED_TABLE]`
· computed per-weapon authority/concentration/gap/cut surfaces this session.

---

## §1 — Puncture: head shape splits it from percussion

### The mechanism (bottom-up)

Armour is defeated three ways, and head shape routes which one a blow uses:

- **Concussion** (percussion, broad blunt face — low `strike_concentration`): the metric is delivered
  *impulse*. A broad face transmits the swing's momentum through intact plate as blunt trauma. Driven by
  authority `√mass·pob_frac` (the §-PoB result); broad contact is fine. A mace.
- **Puncture / penetration** (concentrated blunt — high `strike_concentration`): the metric is
  *pressure* = force / area. The *same* swing authority delivered through a tiny contact (a beak / pick /
  spike) pierces plate. `pressure ∝ authority × concentration`. A poleaxe, bec de corbin, war-hammer
  spike — the "long-shafted pick" — and historically the premier plate-defeating arm.
- **Thrust-puncture** (point head): a *different delivery* — a body-driven push, not a swing — so the
  force is not `√mass·pob` but the lunge; the head shape that matters is `point_concentration × cross_section`
  rigidity (a fine, rigid point finds gaps; a whippy point deflects). Vs plate it finds *gaps*, it does
  not pierce the face. An estoc, spear, half-sword.

So the single head-shape variable separating impact-puncture from percussion is the **contact
concentration** — exactly the hypothesis. One authority source (`√mass·pob`), two outcomes, split by
whether the head is a broad face or a concentrated point.

### Validation (computed for the full roster)

A swung head delivers concussion `∝ authority` and a puncture term `∝ authority × concentration`:

| weapon | head | authority | `strike_conc` | concussion | **pierce** | mode |
|---|---|---|---|---|---|---|
| poleaxe | blunt | 8.00 | 0.85 | 8.00 | **6.80** | puncture |
| mace | blunt | 8.00 | 0.45 | 8.00 | **3.60** | concussion |
| staff | blunt | 4.11 | 0.15 | 4.11 | 0.62 | concussion |
| greatsword | straight_cut | 7.00 | 0.10 | — | 0.70 | cut |
| longsword | cut_thrust | 5.54 | 0.10 | — | 0.55 | gap-thrust/cut |
| rapier | point | 4.95 | 0.00 | — | 0.00 | gap-thrust |

Mace and poleaxe carry **identical authority** (8.00) — what separates them is head shape: the poleaxe's
beak pierces at **1.89× the mace** while both concuss equally. The pierce ranking (poleaxe ≫ mace ≫ all
edged ≈ 0) is the historical plate-defeat order. Edged weapons score ~0 pierce (an edge cannot punch
hardened plate — correct). Thrust-puncture (spear gap-find 0.72, rapier 0.52) is the gap-access sub-mode.

### What the engine does, and the gap

`core.coupling()` has head modes `blunt / point / cut_thrust / straight_cut / curved_cut` — **no pick /
puncture mode**. The poleaxe is `head='blunt'`, so it takes the *percussion* path (`RESIST['heavy']['blunt']`
+ `percussion/8`), identical to the mace. So the engine **cannot distinguish a poleaxe's piercing spike
from a mace's concussive face** — both "blunt," both concuss. The datum that separates them,
`strike_concentration` (mace 0.45 vs poleaxe 0.85), is derived in `geometry.percussion_concentration()`
as `perc_conc` but is **dangling** — `core` never reads it. Thrust-puncture is the one armour-defeat mode
already bottom-up *and* wired (the `gap` field, from `geometry.gap_precision`).

### The canon decision this surfaces

`RATIFIED_TABLE` (the ratified weapon-vs-armour table) has a **single** heavy-blunt row —
`blunt_heavy {none 5, light 5, medium 4, heavy 3}` — into which mace *and* poleaxe both map. The
bottom-up model predicts a pick should **out-defeat** a mace vs plate (pierce 6.80 vs 3.60), which the
table does not represent. Honouring that is a **Jordan canon decision**, not a Claude gap-fill: it
*refines* an authored canonical value (adds a pick-vs-plate distinction the ratified table flattens),
which is exactly the line where the project-owner contract stops me. The mechanism and the ranking are
derived and validated; whether a pick beats a mace through plate is yours to ratify.

### Scope / honesty

- The pierce term is a **relative ranking, not a calibrated damage number** — unlike `P_auth`, which
  reproduced three validated blunt anchors, there is *no ratified pick-vs-plate value to calibrate to*
  (the table flattens it). Turning pierce into damage needs a calibration constant **and** the canon
  decision above. `[CONFIDENCE: high]` on the mechanism and ranking; `[GAP: no ratified anchor for
  pick-vs-plate magnitude]`.
- Code: `percussion_authority.py` extended with `puncture_pressure()` (authority × concentration, blunt-
  gated) and `armour_defeat_mode()` (head→mode classifier); self-test green.
- Thrust-puncture needs nothing new — it is the wired `gap_precision` path.

---

## §2 — Top-down inventory

**Verdict.** The engine's *dynamics* are bottom-up: resolution (σ-pool), reach, tempo, stamina,
concentration, initiative, poise, bind, leverage, feint, and defence-selection are all derived from
stats and weapon geometry over tuning coefficients. Its **weapon-vs-armour damage interaction is almost
entirely top-down** — a stack of hand-set lookup tables that encode the historical outcomes by fiat. The
bottom-up replacements largely *exist* (the `geometry.py` layer; the v32 `armour_axes`/`damage_model`
modules) but are mostly **dangling or unwired** — of the weapon-vs-armour surface, only `gap` is live.
This is one coherent gap, not many scattered ones, and the §-PoB percussion work and the §1 puncture
work are two pieces of closing it.

### A — top-down outcome-encoding where a bottom-up derivation exists or is straightforward (findings, worst first)

| # | Instance | Location | Encodes by fiat | Bottom-up replacement | Sev |
|---|---|---|---|---|---|
| 1 | `RESIST` + `DELIVERY` | `core.py:20–24` | the whole weapon-vs-armour transmission (4 armour × 3 mode resistance fractions) + per-mode delivery multipliers | **built, unwired**: `v32/armour_axes.py` (material×coverage mitigation from resistance-per-mode) + `v32/damage_model.py` (coupling from material-resistance-per-mode), calibrated to `RATIFIED_TABLE` | **HIGH** |
| 2 | `percussion` 0–8 | `combatant.WEAPONS`; read at `core.damage` + `systems.armor_defeat_sigma` | per-weapon blunt authority assigned by hand | **derived this session**: `P_auth = f(√mass·pob)` (`percussion_authority.py`); reproduces 8/8/4 + 11/12 damage cells | MED |
| 3 | `HEFT {light:4, heavy:6}` | `core.py:18` | impact base from a binary weight class; **discards continuous `mass`** (sourced per-weapon, used nowhere else) | derive impact from continuous `mass` (data already present) | MED |
| 4 | puncture ≡ percussion collapse | `core` blunt branch + head taxonomy + `systems.armor_defeat_sigma` | a pick/beak is treated as a broad blunt; `strike_concentration` dangling (`perc_conc` unused) | **identified §1**: `puncture_pressure = authority × concentration`; needs calibration + canon call | MED |
| 5 | `GATE` defence caps | `systems.py` (~l.95) | per-weapon parry/dodge/wind caps (11×3, hand-set) | candidate derive from `blade_guard`/`hand_guard`/`leverage`/length (parry,wind) + weight/handling (dodge) — primitives exist, not yet derived | MED |
| 6 | `ADEF_*` defeat weights | `config` (`ADEF_W`, `ADEF_BLUNT/POINT/CUT`, `ADEF_THRESHOLD`) | armour-defeat σ by tier + per-mode caps; overlaps `RESIST`; blunt rides `percussion/8` | same as #1/#2 (folds into the continuous transmission model + `P_auth`) | MED |
| 7 | `HEAD_REACH` + `reach='long'/'short'` | `config.HEAD_REACH`; `combatant['reach']` | reach contribution by head category, atop continuous `head_len` (present) | derive reach from `head_len` continuously | LOW-MED |
| 8 | `spd` per-weapon | `combatant['spd']` → `weapon_tempo` | hand-set cadence; overlaps mass/HEFT (heavy→slow) | derive cadence from mass / swing inertia | LOW-MED |
| 9 | `hand` / `HANDLE_RANK` | `combatant['hand']`, `config` | categorical handling difficulty; overlaps first-moment `M₁` (head-heavy = demanding) | derive from `M₁ = mass·pob·L` (the §-PoB control-cost quantity) | LOW-MED |
| 10 | `QUAL` degree multipliers | `core.py:19` | degree→damage shape {.6/.35/1.0/1.5} | a conventional degree mapping; values hand-set (low benefit to deriving) | LOW |
| 11 | `head` mode classification | `combatant['head']` | categorical mode; derivable from geometry (edge/point/strike concentrations) | classify from `edge_keenness`/`point_concentration`/`strike_concentration` | LOW |

### B — legitimately top-down (NOT defects)

- **`RATIFIED_TABLE`** (`v32/armour_axes.py`) — the *canonical ratified* weapon-vs-armour outcome; the
  anchor every bottom-up model reproduces. Top-down **by design**, not a defect.
- **`WoundTracker`** (WI=End+6, MW=min(End/2+1,3) PP-717, Health=WI·(MW+1), −1D/wound) — ratified
  Class-A canon (`derived_stats §4.1`).
- **`TRADITIONS` / `ABILITIES` / `FAMILIARITY` / `ADJACENT`** (`tradition.py`) — cognitive-mode design
  content, grounded in the historical-precedents corpus. Cultural emphasis is an authored design choice,
  not derivable physics; correctly hand-authored.
- **`UPSET_FLOOR` 0.05** (`config`) — the deliberate 95% videogame cap.
- **The ~100 `config` coefficients** — calibration *scaling* bottom-up-derived relationships, not
  outcome-encoding (the config docstring itself: "Class-C — calibrated against the harness, not canon").
  A handful are load-bearing thresholds (`ACT_THRESHOLD`, `COMMIT_SIGMA`, `BURST_MAX`, the `core.degree`
  thresholds) — the resolution skeleton, hand-structured by design.
- **`blade_guard` / `hand_guard`** (`combatant`) — physical weapon features used as input data (like
  `mass`/`pob_frac`); hand-set *values*, but legitimately primitives, not outcome-encodings.

### The through-line

Every HIGH/MED finding in A is the same surface: the **weapon-vs-armour damage stack**
(`RESIST`/`DELIVERY`/`percussion`/`HEFT`/`ADEF`/`GATE`/the puncture collapse). The bottom-up substrate
to replace it is built at varying readiness — `gap` wired; `P_auth` derived (§-PoB); puncture identified
(§1); `armour_axes`/`damage_model` built-but-unwired; `geometry`'s `cut`/`thrust`/`perc_conc` derived
but dangling. **Wiring it is the single structural decision** already flagged as PoB decision (b): adopt
the continuous transmission model so the geometry+physics derivation *drives* damage, replacing the
hand-set lookups it currently only reproduces. That is a re-baseline, and it is yours to call.

---

## §3 — Honesty / scope

- `[CONFIDENCE: high]` on: the §1 puncture mechanism + ranking (computed from the live geometry); the §2
  inventory (every row cites a read location; the bottom-up status of each is verified — `gap` wired,
  `perc_conc`/`cut`/`thrust` dangling, `armour_axes`/`damage_model` unwired, `P_auth` derived).
- `[GAP: pick-vs-plate magnitude]` — §1 pierce is a validated ranking, not a calibrated number; no
  ratified anchor exists, and the magnitude (and whether pick > mace vs plate at all) is a canon decision.
- The A/B split is the honest discriminator Jordan named: a hand-set *table that encodes an outcome a
  primitive could derive* is a finding (A); a hand-set *design choice, canonical anchor, or tuning
  coefficient* is not (B). I have not inflated tuning constants into defects, nor called the ratified
  table or the tradition content "top-down problems" — they are top-down *by design*.
- Nothing committed. Canon engine unchanged. `percussion_authority.py` (extended) is a proposal module.
