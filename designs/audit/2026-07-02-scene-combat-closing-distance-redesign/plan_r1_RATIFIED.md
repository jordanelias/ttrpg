# Plan R1 (FINAL, reconciled + capstone-verified) — Circumstance-degradation redesign for scene-combat

> **Status: READY FOR JORDAN'S RATIFICATION.** This is the single clean plan. It supersedes the original
> `things-like-a-feather-compressed-rivest.md` draft and the four correction passes
> (`plan_corrected_r0…r3.md`). It keeps the original plan's sound spine — empty⇒identity discipline,
> primitive-law, L0–L3 layering, per-increment verify+commit, Jordan-gated re-baselines — and folds in
> every survived finding from six adversarial audits (the M-01…M-25 register) plus the four-pass
> agonist/antagonist loop. Every design decision, line reference, and number below was re-verified this
> pass by **direct code read against the live engine** at
> `C:/Github/ttrpg-morph-rearch/designs/scene/combat_engine_v1/` (`weapon_physics.py`, `systems.py`,
> `core.py`, `config.py`, `wrapper.py`, `weapons.py`, `state_graph.py`, `combatant.py`), with numpy
> present. **Where prose and code disagreed, code won.** House rules: `C:/Github/ttrpg-morph-rearch/CLAUDE.md`.
>
> **What the loop could not settle is not hidden.** After four producer passes, **8 residual
> BLOCKER/SERIOUS findings** remained live against the plan chain; each is folded below as either a
> concrete fix (with its acceptance gate) or an explicit **Jordan-decision**. The unresolved
> damage-model / `I_g` tension in particular is surfaced as JD-1, not silently resolved. The residual
> ledger and the register-closure ledger are the two tables immediately below.
>
> **A subsequent capstone verification pass (3 independent opus-max verifiers: dynamics/oscillator,
> emergence-gate, coherence+JD-integrity) found and closed 4 more items before this final version:**
> **1 new BLOCKER** — a genuinely new grip↔reach feedback oscillator that D3/I3 would otherwise introduce
> (now **JD-9**, with a recommended fix and an I3 convergence gate); **1 SERIOUS** — `pc_sel` was read in
> three places but never threaded (now sourced via a widened `sel_pc` field, D2b); and **2 MINOR**
> plan-text precision fixes (an unreachable acceptance-gate clause reworded; a mis-cited producer function
> corrected). The capstone's `coherence-jd` lens **passed clean** — the increment DAG, the orphan
> cross-check table, and all 8 original Jordan-decisions were independently confirmed sound and
> non-invented. Every JD below (1 through 9) carries its concrete evidence and the plan's reasoned default,
> not a bare menu of options.

---

## Residual-findings ledger (the 8 that survived 4 producer passes)

Each survived the final attack round; each is closed here as a **fix** (F) or a **Jordan-decision** (JD).

| # | Dimension | Finding (verified against code) | Resolution | Where |
|---|---|---|---|---|
| R-1 | kinematics | R2's I2 damage-ratio gate (`≤75/≤82/≤82%`) is **not reproducible** on the live `core.damage`; the additive `strength` floor + outer `int(round)` erode a multiplicative Φ **more at high STR**, so single-STR retention points are wrong. | **F** — restate every retention threshold as a **worst-case-across-STR (2/4/6/8) range**; gate against the highest-STR retention. | D2, I2 acc. #3 |
| R-2 | biomechanics-facticity | The same STR-dependence means the deltas must be **ranges**, not points; the gate must sit at the worst STR. | **F** — deltas measured & quoted as ranges (guandao 71–76%, voulge 81–88%, bardiche 77–88%); gate at worst column. | D2, I2 acc. #3 |
| R-3 | morphology-schema | `point_concentration` (pc) does **not** cleanly separate arc from thrust: whole-weapon thrust band `[0.55…0.99]` and cut band `[0.08…0.62]` **overlap in `[0.55,0.62]` in the WRONG order** (bear_spear pc=0.55 < greatsword pc=0.62). A whole-weapon-pc blend mis-degrades a broad-headed pure-thrust pole as ~45% swing. (And `orient_deg` cannot gate it either — cutters and thrusts both sit at 0/90.) | **F** — key thrust-protection and arc-vs-thrust on the **SELECTED element's head/mode**, never a whole-weapon pc or orient scalar. | D2, D5 |
| R-4 | biomechanics-facticity | Two "verified live" reach anchors are wrong, and the flagship weapon is one: live `reach_base` spear=**7.797**, glaive=**7.200** (R2 recorded 5.98/6.00 — those are the *geom* sub-terms, not reach). | **F** — correct the pre-floor anchors; the post-floor targets (spear 4.94, glaive 5.47) were already right and stand. | D1, I3 acc. #6 |
| R-5 | biomechanics-facticity | `bec_de_corbin` is a **broken** sel_gap anchor: it selects **blunt** at none/light, and its *point* is the top spike (gap 0.800), never the 0.57 beak R2 cited. | **F** — drop bec; **ji** alone is the sound sel_gap/sel_perc anchor (point 0.680 vs whole 0.560, diverges vs armour). | D5, I4 acc. #1 |
| R-6 | coupling-seq-orphan | The `er` REFRESH #1 contract **over-derives**: re-deriving `measure_gap`+`closed` from `er` every beat wipes the running approach decrement (wrapper.py:90) and un-latches `closed` (wrapper.py:93/:81). `measure_gap` (dynamic closing distance) and `er`/reach (standing reach) are **different quantities by design**. | **F** — scope Refresh #1 to re-derive **only `er`** (+ the longer/shorter labels, subject to JD-2). Both its consumers already read `er` directly. | D3, I3 acc. #3 |
| R-7 | coupling-seq-orphan | `select_mode`'s return `(dm, h)` is **too narrow**: it emits a head TOKEN, no element handle, and `afforded_heads` collapses per-element identity into a `token→(eff,dm)` union. The winning element's gap and percussion are never produced, so threading `c.sel_gap`/`c.sel_perc` is under-specified and reproduces the same-key-different-object bug across the half-sword swap window. | **F** — **widen `select_mode`'s return to a 5-tuple** `(dm, h, sel_gap, sel_perc, sel_pc)` (extended to a 5th field by the capstone's M2 fix, see D2b); carry the winning element's `(gap, perc, point_concentration, element_ref)` through `element_afforded`/`afforded_heads`; capture at **both** call sites. | D2b, I2 |
| R-8 | biomechanics | The greatsword's cramped-quarters cure via a heft-room term is a **genuine fork, not a settled ~8% cosmetic**. Re-measured, the greatsword *cannot gather* (g\*\_closed=0.045 → swing-Φ_grip=0.9996 — the real inertness), and a heft-room *multiply* is **not** negligible (a 0.5× room factor moves STR4 damage 24→17, ~29%) **and is monotone in lost room, violating C4**. | **JD** — keep Φ_room OFF the heft path (its direction/existence is a design fork; a monotone room→power ramp violates C4); route the cure through commit-window + legibility + D2b percussion; surface the heft-room question as **JD-1(d)**. | D2, D4, JD-1(d) |

**Two BLOCKER-class findings from the biomechanics antagonist are CLOSED (not residual), and stay closed
by construction:** (i) `Φ_grip = S_g(g)/S_g(0)` collapses the closed thrust to ~0 (yari 0.000, spear
0.135) — closed by keying thrust-protection on `sel_head=='point'` (Φ_thrust≡1.0), so no pure-thrust pole
reads a swing-moment ratio at all; (ii) a centre-balanced staff yields `Φ_grip = 0/0 = NaN` — closed by
the `ρ := 1.0 when S_g(0) ≤ ε` guard. Both are proven by the I2 acceptance gates (#2, #4).

**A ninth item was found by the subsequent capstone verification pass (below the register/loop, caught
independently): the grip↔reach oscillator.** See JD-9. It is orthogonal to R-6 (the two-recompute `er`
contract remains sound and unaffected).

---

## Register-closure ledger (M-01…M-25 — every BLOCKER closed or converted)

The master register consolidated 7 BLOCKER · 9 SERIOUS · 7 MINOR from six lenses. Every one is closed by a
decision below or converted to a named Jordan-decision. **No BLOCKER is left silently open.**

| ID | Sev | Closed by | Disposition |
|---|---|---|---|
| **M-01** | BLOCKER | D2 | Ill-posed `½·m_eff·ω_cap²` **abandoned**; `omega_cap`/`m_eff` never added; impact keeps the grounded static-moment ceiling degraded by a mode-split `Φ_grip`. No `I_g` in delivered energy → no reach re-manufacture; no ω² room collapse. Residual damage-model tension → **JD-1**. |
| **M-02** | BLOCKER | D2b, D5 | `sel_gap` = the SELECTED element's own `geo['gap']`, emitted by the widened `select_mode`, read in `core.strike`/`adef_cap`/comparator. Anchor **ji** (bec dropped, R-5). Lands in I2. |
| **M-03** | BLOCKER | D3 | Two-recompute `er` contract; `reach_sigma` reads refreshed `er`; single-beat reach coherence proven; label-flip is **JD-2**. |
| **M-05** | BLOCKER | D0, D5 | `element_ref` restored; `closed` consumed in close-efficacy; 7 zip composites authored-or-documented (**JD-5**); arc-vs-thrust keyed on the selected element's mode (R-3). |
| **M-07** | BLOCKER | D9 | `hook_affordance` **not built** — no primitive separates pull-hook from bind-lug (retracted honestly); grab = free-hand + leverage. Re-sourcing a drag primitive is **JD-7**. |
| **M-09** | BLOCKER | D2/D2b, I2 | The grip-threading of heft + **every** percussion consumer lands in ONE atomic increment (I2), never split; proven by an OLD-vs-NEW sweep + a grep-assertion no caller passes a non-default grip in the signature-widening step. |
| **M-11** | BLOCKER | D8 | A **real** `Contact` STATE + `'contact'` TRACE_KIND are **BUILT** (verified absent today); one insertion point reads a unified `opening_created` flag; the grab menu provably does not re-enter the bind `beats` mutation. |
| **M-04** | SERIOUS | D1, D3 | Slide folded into `geom` before `REACH_GEOM_SCALE` (same scaled units); floored; corrected anchors (R-4). |
| **M-06** | SERIOUS | D0, D6 | `orient_deg`/`type` restored — but used as **fore/aft only** (bands overlap at 0/90); arc-vs-thrust re-grounded on the selected element's mode. `material` restored inert. |
| **M-08** | SERIOUS | D2b | `percussion_authority` becomes circumstance-aware in the **same** increment as heft; per-element percussion distinguishes multi-blunt composites; deliberate grip-invariance is **JD-4**. |
| **M-10** | SERIOUS | D5 | `sel_head` routed consistently to `approach_displace`/wrapper displace gate/`reach_threat`; open-measure equivalence to native head asserted. |
| **M-12** | SERIOUS | D11 | `agility`→`at_grip(w,0)['I_g']` migration **proven** byte-identical (or annotated a re-baseline); all `derive['MoI']` dynamics-consumers read the same `I_g`. |
| **M-16** | SERIOUS | D12 | Per-weapon heft **and** percussion snapshot regression (all roster weapons) so a re-anchor is visible + Jordan-gated. |
| **M-18** | SERIOUS | D9 | `clinch` is a single forced disposition — **DELETED** from every record (not "retire OR residual"); a CI check that no resolver reads it. |
| **M-19** | SERIOUS | D1, D7 | `rear_clearance` computed from `_all_parts`, **never** `length_m`; half-sword forms exceed their base form. |
| **M-21** | SERIOUS | D7 | I7 **split** into I7a (rear_clearance, separable) + I7b (contact.py). |
| **M-13** | MINOR | D9 | Moot — no fresh hook sum is built; `hook_sword` crescent stays counted once (existing `_all_parts` exclusion). |
| **M-15** | MINOR | D4, I5 | `range_utilization` writer + `commit_depth` read land atomically; reshapes Beta params only; `betavariate` draw order/count unchanged. |
| **M-17** | MINOR | D12 | Every increment's verification runs pytest **with numpy present** and asserts a non-zero collected count; a skipped combat suite is a RED. |
| **M-20** | MINOR | D1, D7 | `geom_slide` decoupled from the CoM clamp so a centre-balanced staff's reach/rear-clearance still change though its `u`=0. |
| **M-22** | MINOR | D11 | Standing anti-orphan test (I8): every Combatant circumstance field has ≥1 live reader. |
| **M-24** | MINOR | D12 | `INJECTION_POINTS[...]['site']` line strings dropped, or a test asserts each line-range still holds the logic. |
| **M-25** | MINOR | this plan | The six-lens findings are folded in; the I3→I4→I5 chain + the I7 split are re-derived post-fold-in (this document). |

**Sound-and-kept (register Appendix A / Appendix B): D6, D10** (SOUND); **D1, D3, D4, D5, D7, D8, D9**
(SALVAGEABLE — repaired above); **D2** (was BROKEN — re-derived, not tuned). No decision is left in its
broken form.

---

## Context

Phase B derived every combat quantity from real located-part primitives — but for the **ideal**
circumstance (full extension, as-issued grip, unimpeded swing, linear approach). Nothing degrades them
under real circumstances, and a full-roster sweep shows spear/polearm-class weapons winning **84–96%** vs
an arming sword (re-verified this session; pre-dates Phase B). Jordan's diagnosis, confirmed by direct code
reads: *"we did a lot of work on weapon physics in terms of their use in ideal circumstances without
considering the implications of operating in increasingly less ideal circumstances."* The fix is
**primitive-level physics that degrades the ideal ceiling** — never a category nerf.

**PRIMITIVE LAW (the deepest rule, binding on every decision below).** A weapon NAME —"spear", "estoc",
"greatsword", "dagger"— is **not** a primitive; it is a label over an aggregate of located physical
primitives (masses at positions, point-of-balance, element geometry, haft length, point concentration).
The engine must **never** see or branch on a name/kind. Every behavior EMERGES from primitives. The
spear's 84–96% must fall out of correctly modeling its mass distribution / long haft / choke +
rear-clearance — **NOT** from anything that targets "reach weapons." Weapon names may appear **only** as
diagnostic labels for emergent roster outcomes; `test_no_weapon_name_literal_in_resolution` must stay
green. Concretely: an estoc (long stiff point-concentrated short-haft thrust) vs spear (long haft
half-staffable) vs greatsword (heavy, needs swing room) differentiate **because their primitives differ**,
never because of a class — and the thrust-protection below reads the **selected element's strike mode**,
not a weapon-class or even a whole-weapon pc scalar (which, as R-3 shows, mis-orders bear_spear below
greatsword).

**Layer discipline (binding).** L0 (`weapon_physics`/`geometry`/`weapons`) is **PURE** — weapon + scalar
circumstance params only, **no `Combatant` object**. L1 `core.py`. L2 `systems.py` (Combatant-aware,
contribution-out). L3 `wrapper.py` owns **ALL** mutation.

**FACTICITY.** Every constant traces to a real located primitive, a cited treatise, or a biomechanics
measurement — never a fiat 0–1 scalar dressed as grounded. First-principles claims are labelled
`[ASSERTED]`, not dressed as a measurement; calibration knobs carry `[SIM-CALIBRATE]`; data-absent choices
carry `[FIAT — …]`.

**R0 flags respected throughout.** **C1** (polearm facing UNRESOLVED → neutral default, `[FIAT — C1]`);
**C2** (facing per-guard/per-moment, **never** per-weapon-class); **C4** (force-vs-distance **non-monotone**,
interior optimum — Bolander/Neto/Bir 2009; **no lever falls monotonically or quadratically with lost room**);
**C5** (clinch resolved by **DERIVATION**, not data-editing — honest about what the primitives can and
cannot support).

### The load-bearing new numbers R1 re-measured about the engine damage path

`core.damage` (core.py:143-156): `impact = strength + heft`, with
`heft = 3.0·(perc/8) if blunt else HEFT_HEAVY(3.0)·heft_units`, then
`damage = int(round(impact · coupling · qf · DMG_SCALE))`, `DMG_SCALE=1.55`. **The additive `strength`
floor (default 4) plus the outer `int(round)` erode a multiplicative Φ on `heft_units` — MORE at high STR
(the Φ shrinks the heft term but not the strength term) and at the low-damage margin (rounding).** This is
the SAME mechanism that makes a Φ_room-on-heft a weak-and-forked lever; it applies equally to the retained
swing-`Φ_grip`, so **every retention threshold is quoted at its WORST (highest-STR) point, not its best**
(R-1/R-2).

Live `core.damage` retention (closed damage ÷ open damage), armour=none, degree=success, `Φ_grip` applied
as a `heft_units` multiply on the native cut/thrust/point path — **measured this pass**:

| weapon | pc | g\*\_closed | Φ_grip@g\* | STR2 | STR4 | STR6 | STR8 | worst (highest STR) |
|---|---|---|---|---|---|---|---|---|
| **guandao** | 0.30 | 1.000 | 0.650 | 0.705 | 0.714 | 0.741 | 0.759 | **0.759** |
| **voulge** | 0.55 | 1.000 | 0.775 | 0.808 | 0.839 | 0.857 | 0.875 | **0.875** |
| **bardiche** | 0.18 | 0.627 | 0.743 | 0.769 | 0.795 | 0.812 | 0.830 | **0.830** |
| **greatsword** | 0.62 | **0.045** | **0.9996** | ≈1.00 | ≈1.00 | ≈1.00 | ≈1.00 | ≈1.00 (cannot gather) |
| spear | 0.78 | 0.865 | 0.905 | — | — | — | — | thrust-protected (≥0.9) |
| yari | 0.88 | 1.000 | 0.940 | — | — | — | — | thrust-protected (≥0.9) |

- The swing-`Φ_grip` lever is **material** for the low-pc high-heft choppers that actually gather
  (guandao/voulge/bardiche) and **inert** for the greatsword (it cannot choke: `grip_choke_max=0.15` →
  g\*=0.045 → Φ=0.9996).
- Only **guandao** is unambiguously "material" (71–76%). **voulge (81–88%) and bardiche (77–88%) are
  borderline** — a ≤15% cut only at low STR. R1 treats voulge/bardiche as *borderline-retained,
  ablation-gated*, and surfaces the choice to Jordan (**JD-1**); it does **not** assert them as
  clean-material.

**⚠️ Convergence caveat (capstone, JD-9):** the `g*_closed` values in this table are the CONVERGED
fixed-point values under the chosen fix for the grip↔reach oscillator (JD-9, fix A: `grip_target`'s drive
input reads reach at a fixed grip=0.0). If a different JD-9 option is ratified (B or C), these numbers may
shift and this table must be re-measured before I2 is implemented.

### What R1 re-measured about the reach path

Live `reach_base = L0(4.0) + REACH_GEOM_SCALE(0.635)·(head_len + REACH_2H_K(0.4)·grip_len·[2H]) +
reach_adj` (systems.py:11-20), **grip-blind today** (verified). Measured:

| weapon | live `reach_base` (open) | floored max-choke (D1) | > L0? |
|---|---|---|---|
| **spear** | **7.797** | 4.940 | ✓ |
| **glaive** | **7.200** | 5.465 | ✓ |
| poleaxe | 6.617 | 5.347 | ✓ |
| staff | 6.489 | 5.346 | ✓ |
| guisarme | 7.095 | 5.535 | ✓ |
| yari | 8.185 | 4.879 | ✓ |
| bardiche | 7.441 | 4.715 | ✓ |

The "5.98/6.00" figures a prior pass recorded for spear/glaive are the *geom* sub-expressions
`(head_len + 0.4·grip_len)`, **not** reach (R-4). The **post-floor** targets are correct; the directional
invariant (reach stays > L0 after a full choke) holds for the whole roster.

### What R1 re-measured about mode selection anchors

Live `select_mode`/`afforded_heads` (systems.py:285-335, verified 2-tuple return + token-union) — measured:
- **bec_de_corbin** native head=`blunt`; `afforded_heads`={blunt:4.103, point:0.800}; selects **blunt** vs
  none/light, **point (the top spike, gap 0.800)** vs medium/heavy. So bec is NOT a point-selection anchor
  at unarmoured, and its point (when it fires) is 0.800, not 0.57 (the beak, which never wins). **Dropped as
  an anchor** (R-5).
- **ji** native head=`cut_thrust`; `afforded_heads`={point:0.680, curved_cut:1.140}; selects **curved_cut**
  vs none, **point (gap 0.680)** vs light/medium/heavy while `w['gap']=0.560`. **ji is the sound
  sel_gap/sel_perc anchor** — a live point-selection where the selected element's gap genuinely diverges
  from the whole-weapon gap.

### What R1 re-measured about thrust-protection (the pc-overlap defect, R-3)

Native-head bands (whole-weapon baked pc): THRUST-headed `[0.55…0.99]` (lowest bear_spear=0.55);
CUT-headed `[0.08…0.62]` (highest greatsword=0.62/katana=0.60). **They overlap in `[0.55,0.62]` in the
wrong order.** A whole-weapon-pc blend `Φ_grip = pc·1.0 + (1−pc)·Φ_swing` therefore assigns bear_spear
(head=`point`, its native + only strike a thrust) swing-degradation weight 0.45 → **Φ_grip@closed = 0.775**
(below spear 0.905 / yari 0.940 and below the ji floor 0.85); full `core.damage` drops it ~15–22%.
partisan (cut_thrust) Φ=0.750, spetum (cut_thrust) Φ=0.860. **Root cause is schema: pc is a WHOLE-WEAPON
geometry scalar and ≠ the SELECTED element's strike mode.** R1 keys thrust-protection on the selected
element's head (see D2/D5). Verified fix: with `sel_head=='point' → Φ_thrust=1.0`, bear_spear/spear/yari
all read **1.000** at the grip they adopt; partisan/spetum (which SELECT `cut_thrust` even vs heavy — a
genuinely part-swing versatile head) retain their pc-blended swing degradation, which is **correct** (a
cut_thrust weapon not committing its pure point genuinely swings — **JD-8**).

---

## Revised design decisions

Each states **the decision**, its **grounding cite**, and the **register finding(s) + residual(s) it
closes**.

### D0 — Schema restoration: re-ingest dropped located primitives; explicit `element_ref` (NEW; precedes all mode/facing work)
**Decision.** Before any mode/measure work, restore to `weapons.py` element/guard records the Phase-0
primitives that `weapons.py` dropped, and add an explicit per-mode position link:
- **`orient_deg`** on every `element` and `mode_element` — sign encodes **fore/aft only**. Source:
  `phase0_morphology_combined.json`. **⚠️ RETRACTION (binding):** `orient_deg` does **not** cleanly gate
  arc-vs-thrust (cutting blades and thrust spikes both sit at orient=0; goedendag's club and spike both at
  0; ~27 swords' cutting edges at 0). Restored only as a **fore/aft** signal for D6 and a supporting
  legibility cue — **never** the arc-vs-thrust discriminator.
- **`type`** on every guard (Phase-0 per-guard `type`). Restored for D6 fore/aft; **not** hook-vs-bind
  (`type='lug'` collides across pull and bind — verified: guandao(pull) + dangpa/bear_spear(bind)).
- **`element_ref`** (explicit integer index into `elements[]`) on **every** `mode_element` — NOT list
  order. Populated from Phase-0 per-element `label`+`x_m`.
- **`material`** on each part: restore but **mark inert** (no live reader in R1) — an explicitly declared
  inert-data exemption from the D11 anti-orphan check (flagged re-sourcing cost).
- **⚠️ `element_ref` is REQUIRED by D2b's per-element percussion (mass lookup: `x_m`/`mass_kg` live in
  `elements[]`, not in `mode_elements`) and by the emitted `sel_gap`/`sel_perc`/`sel_pc` (D5).** D0
  therefore precedes **I2** (where the widened return + per-element percussion land), not just I4.
- **The D0 build assertion:** every `mode_element` carries a valid `element_ref` into `elements[]`; every
  non-referenced `element` is a `dual_role`/catch element or explicitly annotated `mass-model-only`.
  **Voulge's cleaver/heel_spike mapping is resolved explicitly by `element_ref`** (voulge has 3 mass
  elements — cleaver_blade, thrusting_heel_spike, rear_fluke — but 2 mode_elements; the rear_fluke is a
  `dual_role`/catch element, cleaver→cut_thrust and heel_spike→point map explicitly; positional zip drops
  the rear_fluke — verified).
- The **7 silent-zip composites** (dangpa, spetum, partisan, guandao, fauchard, flamberge, hook_sword):
  each either gains authored `mode_elements` (with `element_ref`/`orient_deg`) OR is documented
  `mass-model-only by design` — a per-weapon authoring call recorded in the commit (**JD-5**).

**Grounding.** `phase0_morphology_combined.json` collected `orient_deg`/`type`/`geom_notes`/per-part
`material`/`label`/`x_m` on every element/guard; `weapons.py` grep returns 0 for
`orient_deg`/`material`/`type`/`element_ref` (verified). `_all_parts` already assembles parts about `x=0`.
FACTICITY: real located primitives, not fiat.

**Closes.** M-05 (positional half + voulge count + 7 zip composites), M-06 (orient_deg/material dropped →
restored for D6 fore/aft; arc-vs-thrust re-grounded on the selected element's mode, D5). **Provides
`element_ref` for D2b's per-element percussion (R-7) and D5's sel_* wiring.** Does **not** make D9's
pull-vs-bind gate buildable (the discriminator does not exist at this schema — D9 + JD-7).

---

### D1 — L0 circumstance bundle: `at_circumstance(w, grip=0.0, room=1.0)` (slide floored; reach anchors corrected)
**Decision.** Extend `at_grip(w,g)` → `at_circumstance(w, grip=0.0, room=1.0)`; keep `at_grip(w,g)` as a
thin alias so existing callers are byte-identical. Returns the existing `{I_g, S_g, d_g, u}` **PLUS**:
- **`rear_clearance`** — length trailing behind the working hand, from located parts:
  `rear_clearance(w,g) = −min over _all_parts(w) of (x − extent/2)`, then `+ u(g)`. **Never** from
  `derive()['length_m']` (the full length, wrong for exactly the composites/half-swords D7 targets — M-19).
  No new stored length field.
- **`geom_slide`** — a *geometric* forward hand-offset along the grippable length (metres), **decoupled
  from the CoM-bounded inertia slide `u`** (`u` stays CoM-clamped for `I_g`; `geom_slide` is a pure slide
  so a centre-balanced staff's reach/rear-clearance still change though its `u`=0 — M-20). **FLOORED
  (M-04 + underflow fix):** the forward head extent kept ahead of the working hand never drops below
  `GRIP_MIN_WORKING` (0.30 m). Formally the slide used by D3 is
  `min(grip_travel_max(w)/UNIT_M, head_len − GRIP_MIN_WORKING/UNIT_M)` in length-units. **⚠️ Verified live:**
  with the floor, every pole's max-choke reach stays > L0 with the **corrected** anchors — spear
  7.797→**4.940**, glaive 7.200→**5.465**, poleaxe 6.617→**5.347**, staff 6.489→**5.346**, guisarme
  7.095→**5.535**, yari 8.185→**4.879**, bardiche 7.441→**4.715** (R-4).

The two ill-posed R0-original members `omega_cap` and `m_eff` are **NOT added** (D2 does not rebuild
delivered swing energy — see D2/JD-1). L0 stays pure: a structural test asserts `at_circumstance`'s
signature contains no `Combatant`/`measure_gap` param.

**Grounding.** Parallel-axis theorem (already in `at_grip`). `_all_parts` carries
`haft.x_m`/`butt.x_m`/`pommel.x_m` about `x=0`. `GRIP_MIN_WORKING` is an existing primitive
(`weapon_physics.GRIP_MIN_WORKING = 0.30`, verified). Reach anchors measured live this pass.

**Closes.** M-04 (units + underflow floor), M-19 (rear_clearance from parts), M-20 (staff `geom_slide`
decouples geometric hand-position from the CoM clamp), and **R-4** (corrected reach anchors feed D3's I3
targets). Retires the `omega_cap`/`m_eff` members (M-01's D1 half).

---

### D2 — Circumstance-degraded IMPACT: thrust-protection on the SELECTED element's mode; swing-`Φ_grip` material ONLY where validated; Φ_room CUT from heft (re-derived; Jordan-gated)
**Decision.** The **ideal-circumstance impact ceiling is UNCHANGED**: `heft_base(w) = m_head ·
max(0, PoB_frac) / HEFT_REF` (verified ordering spear 0.892 < arming 0.934 < longsword 1.000 < greatsword
2.089). Grip enters impact ONLY through a **mode-split, thrust-protected, floored, NaN-guarded** `Φ_grip`,
and **only through the swing fraction** — the thrust path never reads a swing-moment ratio:

- **⚠️ Thrust-protection keyed on the SELECTED ELEMENT's strike mode, NOT a whole-weapon pc blend (R-3).**
  - **A strike whose SELECTED element head is `point` is grip-INVARIANT (Φ_thrust ≡ 1.0)** — the axial
    thrust mass is delivered independent of hand position on a rigid shaft. Verified: with this rule
    bear_spear/spear/yari all read **Φ_grip = 1.000** at the grip they adopt (bear_spear selects `point`
    at every armour tier — checked).
  - **A strike whose selected head is `cut_thrust`/`straight_cut`/`curved_cut`/`cut`/`blunt` degrades its
    swing fraction** by a FLOORED `S_g`-ratio: `Φ_swing(w,g) = SWING_FLOOR + (1 − SWING_FLOOR)·ρ(g)`,
    `ρ(g) = S_g(g)/S_g(0)` **guarded** (`ρ := 1.0` when `S_g(0) ≤ ε` — centre-balanced staff),
    `SWING_FLOOR ≈ 0.5` `[SIM-CALIBRATE]`.
  - **The within-mode thrust-ness blend uses the SELECTED element's own point_concentration, `pc_sel`
    (sourced via the new `c.sel_pc` field — D2b, I2; see the capstone M2 fix):** for a
    `cut_thrust`-selected strike, `Φ_grip = pc_sel·1.0 + (1 − pc_sel)·Φ_swing`, `pc_sel = c.sel_pc`, the
    winning `mode_element`'s own baked `geo['point_concentration']` (from `mode_elements`, not the
    whole-weapon geo). For a pure-`point` strike the blend collapses to 1.0. So partisan/spetum (which
    SELECT cut_thrust even vs heavy — verified) keep a genuine, honest swing degradation on their swing
    fraction (partisan Φ 0.750, spetum 0.860) — stated intent, not a silent mis-degrade (**JD-8**).
  - *Verified live at `grip_target`, `SWING_FLOOR=0.5`, under the selected-head rule:* bear_spear **1.00**,
    spear **1.00**, yari **1.00** (all select `point`); ji 0.87; mace/blunt floored; staff **1.0**
    (guarded). **No pure-thrust pole collapses; no NaN.** (Closes the two biomech BLOCKER-class findings.)

- **⚠️ `Φ_grip` is VALIDATED through `core.damage`, with WORST-CASE-across-STR gates (R-1/R-2).** The I2/I8
  acceptance measures the FULL-damage delta across STR **2/4/6/8** and sets the bar at the **highest-STR
  (worst) retention**. Measured this pass (armour=none, success), as ranges:
  - **guandao** (heft 5.71, pc 0.30, g\*=1.0, Φ 0.650) → **71–76%** of open (STR4 0.714, STR8 **0.759**).
    **Unambiguously material.** Gate: retention **≤ 76%** worst-case.
  - **voulge** (heft 3.24, pc 0.55, g\*=1.0, Φ 0.775) → **81–88%** (STR4 0.839, STR8 **0.875**).
    **Borderline.** Gate: **≤ 88%** worst-case, flagged borderline (**JD-1**).
  - **bardiche** (heft 4.92, pc 0.18, g\*=0.63, Φ 0.743) → **77–88%** (STR4 0.795, STR8 **0.830**).
    **Borderline.** Gate: **≤ 88%** worst-case, flagged borderline (**JD-1**).
  - **greatsword** — it CANNOT gather (`grip_choke_max=0.15`, g\*\_closed=0.045 → Φ_grip=**0.9996**), so
    swing-`Φ_grip` barely fires. Its cramped symptom does NOT route through heft.
  - **⚠️ `Φ_room` is CUT from the heft path (R-8).** A monotone room→power heft multiply violates C4 (and
    its direction/existence is itself a design fork — **JD-1(d)**); verified a 0.5× room factor moves
    greatsword STR4 damage 24→17 (≈29%, NOT "~8%"), so it is neither negligible NOR a clean lever — it is a
    **Jordan-decision**, not a settled cut. The greatsword's cramped-quarters symptom routes through **D4's
    swing-room commit-window + legibility** (non-monotone, interior-optimum, reaches the resolved roll)
    and, for armour matchups, **D2b percussion → armour-defeat/reach_threat** (the sigma path) — never a
    heft multiply. A code check asserts no `room` operand multiplies `WP.heft`.

**Grounding.** Static-moment impact (`m_head·PoB_frac`) is the existing grounded `heft`. **Thrust
grip-invariance:** `[ASSERTED — rigid-body first principles: axial thrust mass is delivered independent of
hand position on a rigid shaft, unlike a swing whose moment arm changes with grip]`. (⚠️ Provenance,
honest: the fencing-lunge PMC10203838 + Rinaldi 2018 cites measure whole-body kinetic-chain completion —
knee ROM, leg GRF, trunk sequencing — and never vary hand position on a shaft; the brief flags the transfer
as "an inference." They are demoted to what they support: force scales with the leg/trunk chain, orthogonal
to hand position — NOT a source grip-invariance is grounded *in*. The DECISION is separately defensible as
rigid-body physics; only the label is honest, matching `recoverability_factor`'s own `[ASSERTED —
first-principles]` docstring practice.) `SWING_FLOOR`/`r*`/`σ`/`floor` all carry `[SIM-CALIBRATE]`.

**Closes.** M-01 (no I_g in delivered energy → no reach re-manufacture; no ω² room collapse), the
physics/biomechanics BLOCKER-class findings on `Φ_grip` (thrust no longer reads a swing moment; staff NaN
guarded), M-08's cut/thrust half, and **R-1/R-2/R-3/R-8**. Ordering test is a hard unit gate BEFORE any
sweep. **Requires JD-1, JD-8.**

---

### D2b — `percussion_authority` circumstance-aware in the SAME increment as heft; widen `select_mode` to emit per-element gap+percussion+point_concentration; thread `sel_gap`/`sel_perc`/`sel_pc` (M-08 + BLOCKER-2 + R-7 + capstone M2/M4)
**Decision.** `percussion_authority(w)` → `percussion_authority(w, grip=0.0, room=1.0)`, degraded by the
same mode-split, floored, NaN-guarded `Φ_grip` as D2 (a blunt weapon is `pc≈0.02` → floored swing
degradation, never a collapse; staff guarded). `Φ_room` stays available on **percussion** (unlike heft:
the blunt armour-defeat path reaches the sigma channel, so a room term here is not cosmetic; ablation-gated
at I8). AND, in the **same atomic increment**, the threading + contract fixes:

1. **⚠️ Widen `select_mode`'s RETURN CONTRACT to emit the SELECTED element's `gap`, per-element
   `percussion`, and its `point_concentration` (R-7, extended by the capstone's M2 fix).** Verified
   defect: `select_mode` returns `(dm, h)` (systems.py:335) — a damage-mode + head TOKEN, no element
   handle; `afforded_heads` (systems.py:294-296) unions element results into `heads[tok]=(eff,dm)`,
   discarding which element won; `element_afforded`'s blunt branch reads whole-weapon
   `WP.percussion_authority(w)` (systems.py:281). So the winning element's gap, percussion, AND its own
   `point_concentration` are **never produced** — and `pc_sel` is load-bearing in three places downstream
   (D2's cut_thrust blend, D5's `close_efficacy`, the D4 swing-room legibility term) with no plumbing to
   supply it (capstone finding M2: `sel_gap` cannot recover it either, since `gap_precision(pc,cs)` is a
   nonlinear product of pc AND cross-section — pc is not recoverable from gap). Fix, all in this
   increment:
   - `element_afforded` computes and carries **per-element percussion** — a per-element application of the
     **`percussion_authority` FORM** (each blunt `mode_element`'s own `mass_kg` and its `x_m` as the moment
     arm, with the whole-weapon `energy_credit`; reached via the D0 `element_ref` → `elements[]`
     `x_m`/`mass_kg` — **not** "via `at_circumstance`", which returns `{I_g,S_g,d_g,u}` and computes no
     percussion value at all; corrected per capstone finding M4) — and the **winning element's identity**
     (`element_ref`), its `geo['gap']`, and its `geo['point_concentration']`.
   - `afforded_heads` carries the winning element's `(gap, perc, point_concentration, element_ref)`
     alongside `(eff, dm)`.
   - `select_mode` returns `(dm, h, sel_gap, sel_perc, sel_pc)` (a widened **5-tuple** — extended from the
     originally-specified 4-tuple by the capstone M2 fix; the three extra fields default to the
     whole-weapon `w['gap']` / `WP.percussion_authority(w)` / the whole-weapon `point_concentration` for a
     single-mode weapon, so a single-mode weapon is byte-identical).
2. **Thread `c.sel_gap`, `c.sel_perc`, and `c.sel_pc` onto the Combatant at BOTH `select_mode` call sites**
   — wrapper :69 (pre-swap) AND :123 (post-swap). Verified necessary: `c.w` is a live property
   (combatant.py `return WEAPONS[self.weapon]`) that flips the instant wrapper.py:120 mutates
   `self.weapon`; between :120 and the :123 re-select, any `sel_*` field still holds the PRE-swap element.
   Writing at only one site would resolve a post-swap `c.w` against a pre-swap-selected element — the
   identical same-key-different-object bug. So the wrapper writes all of
   `sel_dmg/sel_head/sel_gap/sel_perc/sel_pc` from the 5-tuple at BOTH :69 and :123.
3. **`sel_perc` read in `core.strike` (BLOCKER-2).** Verified: `core.strike` (core.py:169) sets
   `head=sel_head` but core.py:171 passes `WP.percussion_authority(attacker.w)` — the **whole-weapon**
   value — into `damage()`, which drives the ENTIRE blunt-strike damage (core.py:153). So a composite
   routed to a blunt sub-element (lucerne_hammer rear fluke vs hammer face — two blunt mode_elements, both
   reading whole-perc today) is *chosen* on the element's percussion but *damaged* on the whole-weapon
   percussion. **Fix:** `core.strike` reads `getattr(attacker,'sel_perc',None)` in place of
   `WP.percussion_authority(w)` (native fallback only when unset).
4. **`sel_gap` read** in `core.strike` (:171), `adef_cap` (:219-220), and the `select_mode` comparator
   (:326) — the canonical gap source, landed here so no reader is left on the whole-weapon `w['gap']`
   (this is the M-02 object-confusion unification; it lands in I2 because the widened return that produces
   `sel_gap` lands here).
5. **`sel_pc` — new field, capstone M2 fix.** `c.sel_pc` is the canonical source for `pc_sel` everywhere
   it is read downstream: D2's cut_thrust blend (I2), D5's `close_efficacy` (I4), and the D4 swing-room
   legibility term (I5). This is an **unthreaded existing primitive** (the winning `mode_element`'s own
   baked `geo['point_concentration']`, a passthrough value already computed per-element by `geometry.py`)
   — **not** a new fiat scalar; it closes the plumbing gap the arc-vs-thrust redesign hinges on.
6. **`puncture_pressure(w)` → `(w, grip, room)`**, passing grip/room to its internal
   `percussion_authority` call. Verified: `puncture_pressure` wraps `percussion_authority(w)`; `adef_cap`'s
   blunt branch (systems.py:217-218) reads BOTH, feeding `armor_defeat_sigma` (:345) and `reach_threat`
   (:357). Both summands plus `reach_threat` now resolve the SAME grip as the damage path.
- If percussion is deliberately kept grip-invariant for a component (a hammer's mass doesn't move on the
  haft), that is stated explicitly and the blunt/cut asymmetry proven intended so the I8 ablation gate does
  not read it as noise (**JD-4**).

**Grounding.** `core.damage` routes blunt through `percussion_authority`, cut/thrust through `heft`
(verified core.py:153). The blunt armour-defeat path fans out through `puncture_pressure` → `adef_cap` →
`armor_defeat_sigma`/`reach_threat` (verified call sites). Per-element mass exists in `elements[]`,
reachable via `element_ref` (D0); per-element `point_concentration` exists in each `mode_element`'s baked
`geo` (a passthrough, `geometry.py:74`). `select_mode`'s 2-tuple return + `afforded_heads`' token-union
verified this pass (systems.py:296/:335) as the reason the element identity — and its gap/perc/pc — is
lost.

**Closes.** M-08 (percussion coherence + multi-blunt distinguishability + within-beat consistency), the
`[PHASE-B6 PENDING]` note, the **BLOCKER-2 sel_perc orphan**, **R-7** (the select_mode return contract
widened to a 5-tuple; both call sites), and the **capstone M2 finding** (`pc_sel` now has a producer:
`c.sel_pc`) and **M4 finding** (per-element percussion correctly cited as a `percussion_authority`-form
application, not `at_circumstance`).

---

### D3 — Reach grip-aware, TWO-recompute `er` contract (NO hoist), Refresh #1 re-derives ONLY `er` (M-03 + BLOCKER-1 + R-6); `grip_target`'s drive input fixed to break a second, orthogonal feedback loop (capstone M1 / JD-9)
**Decision.** `reach_base` reads the **floored** `geom_slide` (D1) so a gathered pole reaches less, folded
into the geometry term in the SAME scaled units: `geom_eff = (head_len − geom_slide_units) +
REACH_2H_K·grip_len·[2H]` before `REACH_GEOM_SCALE` (**not** a raw metre subtraction — M-04). AND the
wrapper's frozen `er` dict is refreshed at TWO proven-consistent points per beat — the R1 hoist is
**rejected** — **and Refresh #1 re-derives ONLY `er`, never `measure_gap`/`closed` (R-6).** AND
`grip_target`'s own drive input is fixed to a constant grip so making `reach_base` grip-aware does not
create a NEW, second feedback loop (capstone finding M1, **JD-9**).

**Why the hoist is impossible (BLOCKER-1, verified).** The swap `halfsword_target(aggressor, closed,
defender.armor)` (wrapper.py:120-121) **requires** `aggressor`/`defender` (assigned :117), which require
`actors` (:111), which require `ready[]` (built :72 from `close_tempo`/`weapon_tempo` at :70-71). Hoisting
the swap above :72 requires relocating role determination; and `close_tempo` (:71) runs LIVE on the current
weapon and feeds the actor-selection gate, so any hoist above it changes WHO acts. R1 does **not** hoist.

**⚠️ Why Refresh #1 must re-derive ONLY `er` (R-6).** Verified in the wrapper: `measure_gap` is set from
`er` ONCE at engagement start (wrapper.py:38 `measure_gap=max(0.0, er[longer]-er[shorter])`), then during
the approach it is **DECREMENTED** by the closer's rate every beat (wrapper.py:90
`measure_gap=max(0.0, measure_gap-close_rate)`), and reset from `er` ONLY on a successful reopen
(wrapper.py:81) or to 0.0 on displace/separation. `closed` is likewise **LATCHED**: set True at :93
(the `just_closed` branch), set False only at :81. A `measure_gap`/`closed` re-derive INSIDE the per-beat
loop at top-of-beat would wipe the prior beat's line-90 decrement (**stalling the approach**) and un-latch
a closed engagement whose standing reach gap exceeds 0.3 (**un-closing every long-vs-short matchup**).
`measure_gap` (dynamic closing distance) and `er`/reach (standing reach) are DIFFERENT quantities by
design. **Fix:** Refresh #1 re-derives **only `er[c]`** (and the `longer/shorter` labels, subject to JD-2).
Both of Refresh #1's consumers already read `er` directly, not `measure_gap`: reopen (:79) computes
`base_gap = er[longer]−er[shorter]`, and tempo (:70-71) reads reach-derived `close_unwieldiness` — so
refreshing `er` alone is sufficient. An approach-progression invariant test (a long-vs-short matchup must
reach `closed` within N beats) catches any regression that stalls the approach.

**⚠️ Why `grip_target`'s drive input must NOT read the newly grip-aware `reach_base` (a second, orthogonal
defect — the grip↔reach oscillator; capstone finding M1, resolved as JD-9).** Making `reach_base`
grip-aware (above) closes a real per-beat feedback loop that **does not exist today**: `grip_target`'s
drive term reads `close_unwieldiness(c,cfg)` (systems.py:155), and `close_unwieldiness =
max(0, reach_base(c,cfg) − CLOSE_REACH_REF)` (systems.py:142). Today `reach_base` is grip-blind
(systems.py:18-20), so this is a one-way read. Once D3 makes `reach_base` read `grip_position`, the chain
becomes circular: `grip_target(beat n)` depends on `reach_base` evaluated with `grip_position(beat n-1)`,
which was itself the OUTPUT of the same recurrence one beat earlier. `grip_choke_max` (weapon_physics.py:448)
reads only `c.w`, so it does **not** break the cycle. Iterating the live recurrence
`g[n] = grip_choke_max(w)·min(1,(reach_base(w,g[n-1])−6.5)/CHOKE_DRIVE_REF)` against live CFG
(`CLOSE_REACH_REF=6.5` config.py:95; `CHOKE_DRIVE_REF=1.5` config.py:85; `L0=4.0`/`REACH_GEOM_SCALE=0.635`/
`REACH_2H_K=0.4` config.py:4,11) is a **hard 2-cycle** for every gathering pole — spear flips 0↔0.865
(reach 7.797↔5.326, a swing of ±2.47 reach-units) **every single beat, forever**; the same holds for
yari/guandao/voulge (0↔1.0), glaive (0↔0.467), guisarme (0↔0.396), bardiche (0↔0.627). This is not merely a
code bug: it describes a fighter whose grip and effective reach flicker between two states every beat,
which no real combatant does and which corrupts every downstream reach consumer
(`reach_sigma`/`str_demand`/`slip_inside`/`close_tempo`/reopen `base_gap`) each time it flips. **This
defect is ORTHOGONAL to the two-recompute `er` contract below** — the `er` plumbing is internally sound
(confirmed independently) and neither creates nor cures the oscillation; the loop-break is added
*alongside* it, not instead of it. **Chosen fix:** `grip_target`'s drive term reads `close_unwieldiness`
evaluated at a **FIXED grip=0.0** (open-measure reach) via a dedicated variant used *only* by
`grip_target` — a one-line change at systems.py:155 — so the input driving the gather decision no longer
depends on the gather decision's own output. Verified this yields STABLE (non-oscillating) fixed points
that exactly match the plan's own D2 `Φ_grip@g*` table: spear 0.865, yari 1.0, glaive 0.467, guisarme
0.396, bardiche 0.627 — meaning **none of D2's existing damage-retention numbers change** once this lands.
`reach_base` **stays grip-aware for its ~10 other consumers** (str_demand/slip_inside/reach_sigma/
close_tempo/reopen, all via `close_unwieldiness` at systems.py:64, which is unaffected — not part of this
cycle); only `grip_target`'s own drive input reverts to reading reach at g=0. **This choice is surfaced as
a new Jordan-decision, JD-9** (see JORDAN-DECISIONS below), since the fixed-input choice is
design-meaningful and its converged g* directly feeds the D2 damage numbers.

**Chosen resolution — the two-recompute `er` contract:**
```
per beat, for each combatant c in (A,B):            # roles NOT yet known — pre-swap FULL form
  grip_target                     (wrapper.py:66, unchanged)
    # grip_target's drive term reads reach_base(c, grip=0.0) — fixed input, breaks the D3
    # feedback loop described above; see JD-9. reach_base itself stays grip-aware for all
    # OTHER consumers below.
  select_mode -> sel_dmg/sel_head/sel_gap/sel_perc/sel_pc  (:69, widened 5-tuple — D2b)
  ── er REFRESH #1 (grip-aware reach_base on the current/full form) ──
     recompute er[c]; re-derive the longer/shorter LABELS ONLY (subject to JD-2).
     DO NOT re-derive measure_gap (it is the running approach decrement, :90).
     DO NOT re-derive closed (it is a latched flag, :93/:81).
  close_tempo / weapon_tempo      (:70-71 — reads the FRESH er via reach-derived close_unwieldiness)
  ready[c] += rate                (:72)
reopen check (:78)                # reads the FRESH er[longer]-er[shorter] as base_gap (:79)
approach decrement (:90)          # measure_gap = max(0, measure_gap - close_rate)   [UNCHANGED]
… actor/role determination (:111-117) …
half-sword form-swap              (:120-121, UNCHANGED position — role-gated, stays here)
select_mode re-run on swapped form -> sel_* (:123-124, widened 5-tuple — D2b, BOTH sites)
  ── er REFRESH #2 (grip+form-aware reach_base on the POST-SWAP form, aggressor & defender only) ──
     recompute er[aggressor], er[defender]; the closed-exchange measure reads consume the refreshed er.
closed-exchange sigma reads       (:141 reach_sigma, :163-164 str_demand, :230 slip_inside)
```
- **Refresh #1** feeds reopen(:78/:79) and tempo(:70-71) with grip-aware reach on the pre-swap form —
  correct, because at open/standing measure the fighter holds the full form (the half-sword is adopted only
  inside the committed close exchange). `close_tempo` and actor-selection are **untouched** by any swap
  movement.
- **Refresh #2** feeds the closed-exchange sigma with grip+form-aware reach on the post-swap form, so a
  longsword that half-swords reads its shorter 5.55 everywhere in the exchange, not its full 5.99 in
  `reach_sigma` while `slip_inside` reads live. Verified the split is real: today `reach_sigma` reads the
  frozen `er` (systems.py:141) while `slip_inside`/`str_demand`/`close_unwieldiness` call `reach_base`
  LIVE, and `er` is frozen once at wrapper.py:32-33 while grip mutates per beat at :66 and the form swaps at
  :120.
- **Consistency contract (proven, not asserted):** the two refreshes use the identical
  `reach_base(c, grip_position)`; they differ only in (a) which form `c.weapon` holds (full at #1, possibly
  half at #2) and (b) that #2 is aggressor/defender-scoped. Invariant test: at open measure (grip=0, no
  swap) Refresh #1 == today's frozen `er` **byte-identical** (verified `reach_base` is grip-blind today, so
  grip=0 reproduces it); and in the closed exchange every reach consumer resolves the SAME post-#2 reach.

`reach_sigma` is fixed to read the refreshed `er` (it already receives `er` — just refresh it before the
call). No intermediate state where `reach_sigma` uses frozen reach while `str_demand`/`slip_inside` use
live reach.

**Grounding.** `reach_base` ignores `grip_position` (verified systems.py:18-20); `grip_travel_max` metres
under-scale vs geometry ×0.635 (M-04); the frozen `er` computed once at wrapper.py:32-33; the swap at
:120-121 downstream of both (verified). Only longsword/estoc carry forms (verified `HALFSWORD_FORM`).
Corrected reach anchors (D1) feed the I3 targets. HEMA: gathering-in shrinks effective reach (Silver
short-staff; the engine's own `grip_target`/`can_choke` already model the gather). The grip↔reach
oscillator and its fix were independently re-derived and confirmed by a dedicated capstone verifier against
the live systems.py/config.py constants (finding M1).

**Closes.** M-03 (er-freeze half-switch + read-ordering + symmetric `measure_gap`), M-04 (units + sub-L0
underflow, floored via D1), the **BLOCKER-1 sequencing cycle** (rejected the impossible hoist), the
**actor-selection blast-radius** finding (close_tempo/actor gate untouched), **R-6** (Refresh #1
re-derives only `er`, not the running `measure_gap` / latched `closed`), and the **capstone M1 finding**
(the grip↔reach oscillator — via JD-9's fixed-grip drive input for `grip_target`, orthogonal to and
independent of the `er` contract above). Depends on D1's floored `geom_slide`.

**JORDAN-DECISIONS surfaced:** **JD-2** (may the `longer/shorter` LABEL flip mid-engagement?), **JD-6**
(ratify the two-recompute `er` contract — introduces **no tempo/actor-selection change at all**), and
**JD-9** (which reach drives `grip_target`'s own gather decision — a second, orthogonal fork found by the
capstone pass; pairs with JD-6 but fixes a different, independent problem).

---

### D4 — Range-utilization + commit coupling; swing-room is the greatsword's cramped-quarters cure
**Decision.** New `range_utilization(c, measure_gap, cfg)` → per-beat `c.range_avail` (L2, passes a bare
scalar into L0). Two consumers, both non-monotone, both reaching the roll (so the cramped symptom is cured
on paths `int(round)` cannot erase, unlike Φ_room-on-heft):
- **`commit_depth` reads `c.range_avail`** to **contract the Beta draw's upper support continuously** as
  room vanishes (a swing you cannot fully develop commits shallower) — with an **interior optimum** (C4):
  the contraction is a unimodal function of room peaking slightly inside full extension, not a monotone
  closer=weaker ramp. **`range_avail` only reshapes the Beta PARAMS — never adds or reorders a draw**
  (seeded determinism; verified `commit_depth` consumes exactly one `rng.betavariate`, systems.py:520).
- **A swing-room legibility term** (D5/`legibility`): a broad swing that cannot fully develop in cramped
  quarters is *more* constrained and reads easier (higher `legibility` for the defender), weighted by the
  SELECTED element's `(1 − pc_sel)`, where `pc_sel` is sourced from `c.sel_pc` (D2b, threaded I2; first
  read here at I5) so a thrust is unaffected. This is where the **greatsword's** "needs swing room" bites
  — through the read contest and the commit-window, both of which move `net_sigma` and hence the resolved
  outcome, rather than a heft multiply that rounds away.

The lever enters **damage** ONLY through the commit-window (which shifts the degree distribution) and, for
armour matchups, D2b percussion — **never** scaling `ω`, never a monotone room→power ramp (C4).

**Grounding.** `commit_depth`/`lunge_depth` decoupled from range (verified systems.py:511, driven by
disposition/wariness). Capoferro measure-gated actions; Meyer graduated commitment. Bolander, Neto & Bir
2009 interior optimum (C4). The swing-room legibility direction is `[SIM-CALIBRATE]` (the brief flags the
absence of a treatise passage for cut-arc truncation — `flags.json` weakly_grounded — so it ships small and
ablation-gated, not load-bearing).

**Closes.** M-01's D4 half (room reshapes the Beta window + a legibility read, not ω²), M-15 (atomic
write/read, draw order unchanged), and the **kinematics residual** (the greatsword's cramped-room cure
routes through reaching channels, not a heft multiply). **Carries the greatsword-cure Jordan-decision**
(JD-1(d): whether a heft-room term should exist at all, given it would be monotone/C4-violating — R-8).

---

### D5 — Mode selection reads the measure; arc-vs-thrust from the SELECTED element's mode (anchor corrected; object-confusion unified in I2)
**Decision.** Each afforded element's effectiveness is scaled by a **close-efficacy factor**. **⚠️ The
arc-vs-thrust discriminator is the SELECTED element's strike mode / per-element pc, NOT `|orient_deg|` and
NOT a whole-weapon pc blend (R-3).** A broad arc-requiring swing (a cut/cut_thrust-selected strike with low
per-element pc) collapses in tight quarters; a point-selected thrust barely degrades:
`close_efficacy = 1 − (1 − pc_sel)·f(measure_gap, range_avail)`, `pc_sel = c.sel_pc` (the SELECTED
element's own `point_concentration`, sourced from D2b's widened contract — threaded I2, first read here at
I4), `f` rising as room vanishes, floored, `~0 at open measure` so behavior is preserved until intended.
- *Why the selected element's mode, not whole-weapon pc (verified):* whole-weapon pc bands OVERLAP in the
  wrong order (bear_spear head=`point` pc=0.55 < greatsword cut pc=0.62), so a whole-weapon blend degrades a
  pure-thrust pole as part-swing. The SELECTED element's head (`point` → protected; cut/cut_thrust →
  degrades its swing fraction, weighted by that element's OWN pc) resolves it cleanly (bear_spear selects
  `point` → close_efficacy≈1; guandao/voulge select their cut/cut_thrust cleaver → degrade). `orient_deg`
  (once D0 lands) may enter only as a **fore/aft** cue, never the arc-vs-thrust gate.
- `select_mode` **actually consumes** `closed`/`measure_gap`/`range_avail` (today it receives `closed` and
  ignores it — verified systems.py:302). `SELECT_EPS` remains the affordance floor; the golden
  `test_combat_element_parity.py` fixture (5 tests) is regenerated deliberately.

**Object-confusion (M-02/M-10) — the canonical source-of-truth per quantity, unified (lands in I2 with the
widened return, not a separate wiring):**
- **`gap`:** the SELECTED element's own baked `geo['gap']` is the single source — emitted by the widened
  `select_mode` (D2b), threaded as `sel_gap`, and read in `core.strike` (:171), `adef_cap` (:219-220), and
  the comparator (:326) instead of whole-weapon `w['gap']`. **⚠️ Anchor correction:** **ji selects
  `curved_cut` vs none, `point` (gap 0.680) vs light/medium/heavy** while `w['gap']=0.560` — **ji is THE
  live sel_gap regression anchor.** **bec_de_corbin is DROPPED** (selects `blunt` at none/light; its point
  is the top spike gap 0.800, never the 0.57 beak) (R-5). goedendag is also NOT an anchor (stays blunt).
- **`head`:** the SELECTED mode-head (`sel_head`) is the single source — routed to `adef_cap` in
  `reach_threat` (:357) and read by `approach_displace` (:448) + the wrapper displace/slip gate (:232),
  instead of native `w['head']`. `sel_head` IS set every beat (wrapper.py:69), so this is an immediate
  approach change, native fallback only when genuinely unset.
- **`perc`:** the SELECTED element's percussion (`sel_perc`) is the single source in `core.strike` — see
  D2b/BLOCKER-2. Landed together with `sel_gap`/`sel_head` so no reader is left on the wrong object.
- **`pc` (point_concentration):** the SELECTED element's own `point_concentration` (`sel_pc`, `c.sel_pc`)
  is the single source for D2's cut_thrust blend and this decision's `close_efficacy` — see D2b/capstone
  M2. Landed together with `sel_gap`/`sel_perc` so the arc-vs-thrust discriminator is never read from the
  whole-weapon scalar.

**Grounding.** `mode_elements` carry no position pre-D0 (verified `{head, geo}` only), but each carries its
own baked `geo` incl. per-element `point_concentration` (verified — poleaxe/bec/ji/goedendag/etc.);
`select_mode` ignores `closed` (verified systems.py:302). Live gap/head divergence + the bec/ji anchor
facts measured this pass. HEMA: a thrust stays available in the close (half-swording is the norm); a full
swing needs room.

**Closes.** M-02 (canonical `sel_gap`, ji anchor), M-05 (`closed` consumed; arc-vs-thrust from the selected
element's mode), M-10 (`sel_head` routed consistently), the "no data edits" falsity (retracted), and
**R-3 + R-5**. Depends on D2b (widened return producing sel_gap/sel_perc/sel_pc) and D4 (range_avail); D0
supplies `element_ref` for the per-element mass lookup and the orphan cross-check.

---

### D6 — Facing = per-beat Combatant state, near-neutral (SOUND; orient use narrowed to fore/aft)
**Decision.** `facing` on the Combatant (like `grip_position`), written per beat by `facing_target(c,
closed, cfg)` keyed on stance/measure/grip — **never weapon class** (C2). Feeds a lateral-void component
into closing (Fiore fol. 39r) + a small profile term in `reach_sigma`/legibility. **Ships near-neutral**
so the unresolved C1 polearm-facing question is not load-bearing; the profile term is `[FIAT — C1]`. If ever
promoted to weapon-shaped, it keys on the D0-restored `orient_deg` as a **fore/aft** signal — **not** as an
arc-vs-thrust gate.

**Grounding.** Facing on the Combatant, wrapper as sole mutator — verified sound (register Appendix A). C1
unresolved (`flags.json`); C2 resolved "no clean per-class rule."

**Closes.** No BLOCKER/SERIOUS; latent M-06 dependency for D6 retired by D0's fore/aft `orient_deg`. Kept
per register verdict (D6 SOUND).

---

### D7 — Rear-clearance close penalty, split out of the contact bundle (separable)
**Decision.** `rear_clearance(w,g)` (D1) feeds a spatial footwork/close-quarters penalty into
`close_tempo`/`str_demand`, active in the close — the counterweight that makes choking up a real tradeoff.
Consumes only the D1 bundle, **no dependency on the grab subsystem**, so it lands in its own increment
(I7a), independently ablation-gated. Assert `rear_clearance(g) = rear_clearance(0) + u(g)` monotone
non-decreasing (verified sound for the roster because `u≥0`).

**Grounding.** Silver: the length behind the hands "will hinder him to strike, thrust, ward, or go back."
`rear_clearance` from parts (D1/M-19). Staff decoupling via `geom_slide` (D1/M-20).

**Closes.** M-19, M-20 (shared with D1), M-21 (I7 over-bundling — split I7a/I7b).

---

### D8 — Grab/pin = new L2 `contact.py`, wired through a REAL Contact state — a BUILD not an activation (hardware scope reduced)
**Decision.** `contact.py` (its own L2 module — verified sizing, `systems.py` ~660+ lines) holds
`grab_available` (the GATE: no prior opening → no grab; bind-gated for weapons, open-contact for
dagger/unarmed), `grab_sigma` (strength-dominant, **free-hand precondition + leverage** — NOT hook
hardware), and a BRANCHING `grab_outcome` menu (disarm/throw/pin/control/foot-pin/escape). Wiring is a
**BUILD, not an activation** (verified: `state_graph.STATES` has 15 nodes and **no `Contact`**;
`TRACE_KINDS` has **no `'contact'`**; `INJECTION_POINTS`/`STATES` are a DESCRIPTIVE post-hoc artifact — the
engine emits events, `state_graph` maps events→states). So "contact axis goes live" is a **BUILD**:
- Add a **real `Contact` node to `state_graph.STATES`** with explicit `to`/`emits` edges, a new
  `TRACE_KINDS` entry `'contact'` (verified absent), and a `wrapper._emit('contact', …)` call.
- Choose **ONE insertion point** in the outcome tail (after hit/bind/riposte resolves, ~wrapper.py:253)
  reading a **unified `opening_created` flag** set by all three precondition sites (bind :260, beaten-aside
  :229-240, deep-commit reopen :244) — NOT three parallel grab checks. Prove the branching menu
  **terminates without re-entering the bind inner loop's `beats+=1`** (:271).
- `capabilities.py` gains grab/disarm/pin affordance gates (alongside the existing
  `gap_thrust`/`percussive_blow`/`halfsword` gates — verified pattern; predicates verified against live
  behavior in its `__main__` self-test).

The "wrapper branches mirror bind/riposte" and "injection point goes live" framings are **dropped** — the
Contact node is BUILT.

**Grounding.** State graph descriptive (verified 0/15 STATES + no 'contact' TRACE_KIND). Grabs are
bind-gated (sword) / open-contact (dagger), branching (Fiore 2nd Remedy four-branch), opportunistic on a
prior opening (brief §5).

**Closes.** M-11 (no Contact state, three non-adjacent sites, bind mutates beats). Depends on I7a
(rear_clearance producer, separable). **No longer depends on D0's hook discriminator.**

---

### D9 — `clinch` DELETED; grab derives from free-hand + leverage ONLY; pull-hook hardware DROPPED (hardware claim retracted)
**Decision.** Grab affinity DERIVES from real primitives the schema **actually supports**: **free-hand
availability** and **leverage** (`systems.leverage`, already grounded). The inert `clinch` field is
**DELETED from every `weapons.py` record** — a single forced disposition, not "retire OR residual bias." If
a residual bias is ever genuinely wanted it must be a NAMED term with its own `[FIAT]`/`[SIM-CALIBRATE]` tag
and an ablation gate, never a fallback re-reading the old scalar. A CI check asserts no resolver reads
`clinch` after deletion.

**Pull-hook grab hardware is OUT OF SCOPE (the retraction).** No numeric primitive separates a pull-hook
from a bind-lug in the current schema: pull-hooks and bind-lugs interleave in `orient_deg` (guisarme +60 /
ji +90 / guandao +100 vs ranseur ±45 / spetum ±55 / bear_spear +90); `guard type='lug'` appears on both a
pull (guandao) and binds (dangpa/bear_spear); the distinction lives only in `geom_notes` prose, and even
the prose is fuzzy. A hand-authored `pull_capable`/`hook` boolean is **explicitly forbidden**: it is
morally identical to the `clinch` scalar D9 deletes and is **invisible to
`test_no_weapon_name_literal_in_resolution`** (verified: that test scans only weapon-NAME string literals in
resolution `.py` via AST, not data booleans), so the plan's own CI guard would be hollow against it.
**Deferred, not lost** (**JD-7**): re-sourcing a NEW grounded drag-capability primitive (a signed
hook-return/curl-back geometry per catch element) is a legitimate FUTURE increment, out of scope.

Consequently `hook_affordance` is **not built**. The `blade_guard` double-count concern (M-13) is moot for
grab (no fresh hook sum), and the hook_sword crescent stays counted once via the existing `_all_parts`
`dual_role_element` exclusion (verified).

**Grounding.** `clinch` is DEAD (1–10 on ~54 records, zero readers — verified `flags.json` C5 + code).
Free-hand + a leverage/torque action is the documented grab mechanism (brief §5).

**Closes.** M-07 (retracted honestly), M-13 (moot), M-18 (disjunction → forced delete). Removes the D0→D9
dependency.

---

### D10 — Shields/bucklers + full circular closing OUT OF SCOPE (SOUND)
No defect. A scoping decision. Circular/lateral closing beyond the D6 facing void-term also deferred.

---

### D11 — I1 identity increments proven not asserted; standing anti-orphan test (SOUND)
**Decision.** (a) The `agility` → `at_grip(w,0)['I_g']` migration is proven byte-identical across the FULL
roster (especially `longsword_halfsword`/`estoc_halfsword`, the shifted-origin records that trip the
`I_cm = max(0, I0 − m·PoB²)` clamp + float round-trip) by asserting EXACT float equality of `agility_OLD`
vs `agility_NEW`. If any weapon differs, I1 is annotated a **re-baseline**, not an identity. Every consumer
of `derive(w)['MoI']` on the dynamics path (`agility`, `defense_affinities.lever_norm`, `wield_heft`,
`_recovery_mode_commitment`) reads the SAME grip-adjusted `I_g`. (b) I8 adds a **standing structural
assertion** that every Combatant circumstance field (`facing`/`range_avail`/`sel_*`/…) has ≥1 live reader.

**Grounding.** `agility` reads `derive(w)['MoI']` (verified); `at_grip(w,0)['I_g']` reconstructs `I0` only
up to the clamp + round-trip. (Antagonist confirmed `at_grip(w,0)['I_g']==derive['MoI']` EXACT for both
half-sword forms — the migration holds; the proof gate makes it non-fragile.)

**Closes.** M-12, M-22.

---

### D12 — Verification-infra + drift hazards; accepted-red set ENUMERATED (SOUND)
**Decision.** (a) Every increment's verification runs pytest in an env **WITH numpy + the sim modules** and
asserts a **NON-ZERO collected/passed count** for the combat suite. The per-increment gate is "**no NEW red
beyond the enumerated Phase-C accepted-red set**," because the untouched tree already has **8 combat reds**
(a literal "full suite green" gate fails at I0). The **accepted-red set** (measured live):
  1–5. `test_combat_element_parity` (5 tests: `test_fixture_covers_full_roster`,
     `test_derive_mass_family_parity`, `test_downstream_dynamics_parity`, `test_afforded_heads_parity`,
     `test_select_mode_parity_all_tiers`) — **deliberately regenerated** at I4 (D5) with recorded reasons.
  6. `test_combat_invariants::test_gap_game_poleaxe_spikes_plate` — the poleaxe hammer/spike `[PHASE-C
     FLAG]` (**JD-3**), re-evaluated at I2/I8.
  7. `test_combat_recoverability::test_anchor_is_near_one` — longsword recoverability 1.29 vs asserted
     <0.03-from-1.0, a pre-existing `[PHASE-C FLAG]` from the Phase-B mass model — resolved by Phase-C's
     REC_I_REF/REC_S_REF re-tune, not a mass fudge.
  8. `test_combat_stance::test_lunge_quality_is_weapon_derived_continuous` — rapier q=0.963 vs asserted
     ==1.0, a pre-existing `[PHASE-C FLAG]` — resolved by Phase-C's MOMENT_MASS_EXP / cap-floor re-tune.
  Any red **outside** this enumerated set at any increment is a hard STOP. (7) and (8) are carried through
  and closed at I8's Phase-C re-calibration (or re-annotated with a recorded reason — never silently
  patched).
(b) The `INJECTION_POINTS[...]['site']` line-strings are **dropped** (keep node names) OR a test asserts
each `site` line-range still holds the described logic. (c) `I2`/`I8` add a **per-weapon heft AND
percussion snapshot regression** (all roster weapons) so a re-anchor's effect is visible and Jordan-gated.

**Grounding.** `test_combat_heft.py` pins only longsword==1.0 + ordering (verified); the 8
`INJECTION_POINTS` carry unread `site` strings; the suite `importorskip`s numpy (verified); the 8-red
baseline measured live.

**Closes.** M-16, M-17, M-24, M-25, and the self-contradictory "full suite green" gate (softened + red-set
enumerated).

---

## Re-staged increment sequence

Chain re-derived from the code: **`I0 → I1 → I2 → I3 → I4 → I5 → I6 → I7a → I7b → I8`**, with I3→I4→I5 an
explicit **dependent chain** and I7 **split**. Per-increment verify = `pytest tests/valoria -q` **with
numpy present, non-zero collected** + **no NEW red beyond the D12 accepted-red set** (D12a) + targeted unit
checks + `weapon_physics.py`/`capabilities.py`/`state_graph.py` self-tests clean + commit (`[scope]` format,
cite `PP-NNN`/`ED-NNN` where applicable).

> **Empty ⇒ identity remains the spine:** every new circumstance parameter defaults to ideal (grip=0,
> room=1, facing=neutral) so the added surface is byte-identical to today until a lever is turned on — but
> "byte-identical" is **proven by an OLD-vs-NEW equality sweep**, never asserted (the shifted-origin clamp
> at I1 and grip-already-`>0` at I2 break naive identity).

### I0 — Schema restoration (D0). *(NEW — precedes all mode/facing work.)*
- **Depends on:** nothing (pure data + build-time assertion).
- **Half-switch safety:** data-only; adds `orient_deg`/`type`/`element_ref`/`material` fields + a CI
  assertion. No resolver reads the new fields yet (`orient_deg` at I6 as fore/aft; **`element_ref` at I2**
  for the per-element percussion mass-lookup and the emitted sel_gap/sel_perc/sel_pc, and at I4 for the
  orphan cross-check) — a deliberate, short, tested orphan window closed by D11(b). Changes no derived
  number — `derive()`/`heft`/`select_mode` byte-identical.
- **Acceptance (falsifiable):** (1) `grep orient_deg weapons.py` > 0 (was 0); every `element`/`mode_element`
  carries `orient_deg`; every `mode_element` carries a valid `element_ref`; every guard carries `type`.
  (2) the build assertion passes: every `element_ref` indexes a real `element`; **voulge's cleaver/heel_spike
  mapping is explicit** (via `element_ref`, not list order; rear_fluke annotated `dual_role`/catch); every
  non-referenced element is `dual_role`/catch or annotated `mass-model-only`. (3) the 7 zip composites each
  have authored `mode_elements` OR a `mass-model-only` comment (JD-5). (4) all `test_combat_*`
  **byte-identical** (the 8 accepted reds stay exactly as-is, no new red). (5) `test_no_weapon_name_literal`
  green. (6) **no assertion anywhere that `orient_deg` gates arc-vs-thrust** (a doc/comment check).

### I1 — Proven-identity fixes + circumstance-state scaffold (D11a).
- **Depends on:** I0.
- **Half-switch safety:** the `agility` migration lands ONLY if the full-roster OLD-vs-NEW equality sweep
  passes; else re-labelled a re-baseline with the delta recorded. `facing`/`range_avail`/`sel_gap`/
  `sel_perc`/`sel_pc` default to ideal ⇒ identity; first readers I2/I4/I5/I6 (orphan window closed by D11b
  in I8).
- **Acceptance:** (1) `agility_OLD == agility_NEW` EXACT for all weapons, OR the differing set is listed and
  I1 tagged re-baseline. (2) every `derive(w)['MoI']` dynamics-consumer reads the same `I_g`. (3) combat
  suite byte-identical vs I0.

### I2 — L0 bundle + circumstance-degraded impact + widened select_mode return (D1, D2, D2b, D5's object-confusion), ONE atomic increment. *(Jordan-gated re-baseline.)*
- **Depends on:** I0 (`element_ref` for per-element percussion + emitted sel_gap/sel_perc/sel_pc), I1.
- **Half-switch safety — THE atomicity fix (M-09) + the sel_perc/sel_gap/sel_pc contract fix (BLOCKER-2 +
  R-7 + capstone M2):** `at_circumstance` added with defaults reproducing `at_grip` exactly (OLD-vs-NEW
  sweep + a grep-assertion that **no caller passes a non-default grip/room in the signature-widening
  step**). Then, in the **SAME commit**, ALL of: (a) `core.strike` → `heft_resp` grip/room-aware with
  thrust-protection keyed on `sel_head` (D2); (b) **`select_mode` widened to the 5-tuple** `(dm, h,
  sel_gap, sel_perc, sel_pc)` — `element_afforded` computes per-element percussion + carries the winning
  element's `(gap, perc, point_concentration, element_ref)`, `afforded_heads` carries them through; (c) the
  wrapper writes `sel_dmg/sel_head/sel_gap/sel_perc/sel_pc` at **BOTH** `select_mode` call sites (:69
  pre-swap AND :123 post-swap); (d) `core.strike` reads `sel_perc` (:171) and `sel_gap` (:171); (e)
  `adef_cap` (:219-220) reads `sel_gap`; the `select_mode` comparator (:326) reads `sel_gap`; (f) every
  `percussion_authority` consumer — `adef_cap` (:217), `puncture_pressure` (D2b) — grip/room-threaded; (g)
  `c.sel_pc` is written alongside `c.sel_gap`/`c.sel_perc` and becomes the source for D2's cut_thrust
  `pc_sel` blend (its first reader). **Never split**, because grip is already `>0` at strike (wrapper.py:66;
  `test_combat_stance.py:23` asserts spear `grip_target>0` closed), and `c.w` flips at :120 between the two
  select_mode sites, so a partial thread leaves a post-swap `c.w` resolved against a pre-swap-selected
  element.
- **Acceptance (falsifiable):**
  1. **Ordering gate (hard, pre-sweep):** `spear < arming < longsword < greatsword` at ideal (grip=0,
     room=r\*), greatsword not collapsed — computed, must pass.
  2. **Thrust-protection, keyed on the SELECTED element's mode (R-3):** for every pole whose SELECTED head
     is `point`, `Φ_grip@closed ≥ 0.9` — **specifically bear_spear ≥ 0.9, spear ≥ 0.9, yari ≥ 0.9**. For a
     `cut_thrust`-selected strike (e.g. partisan/spetum, which have no authored `mode_elements` and so can
     only ever select `cut_thrust`, never `point` — see M3), the swing fraction degrades by the SELECTED
     element's OWN `pc_sel` (partisan/spetum retain ~0.75/0.86 on their cut_thrust selection — stated
     intent, JD-8; this is NOT a POINT-selection case). A per-weapon `Φ_grip@closed` table over
     {bear_spear, partisan, spetum, spear, yari, ji} is recorded so the gate can catch a mis-degraded
     thrust. (Closes the biomech BLOCKER-class thrust-collapse + the false whole-weapon-pc guarantee.)
  3. **⚠️ FULL-damage delta through `core.damage`, WORST-CASE-across-STR (R-1/R-2):** measure `core.damage`
     at grip=0 vs g\*\_closed across STR **2/4/6/8**, armour=none, success, and set the bar at the
     **highest-STR** retention. **Material lever retained** iff the worst-case delta clears the I8
     ablation-noise floor:
       - guandao retention **≤ 0.76** worst-case (measured 0.71→0.759) — **unambiguously material.**
       - voulge retention **≤ 0.88** worst-case (measured 0.808→0.875) — **borderline, JD-1.**
       - bardiche retention **≤ 0.88** worst-case (measured 0.769→0.830) — **borderline, JD-1.**
     **Cosmetic/forked lever cut:** the greatsword CANNOT gather (Φ_grip=0.9996), so swing-Φ_grip is inert
     for it; and **Φ_room is NOT on the heft path** (a monotone heft-room multiply violates C4; its
     existence is JD-1(d), R-8). Assert `heft_resp(w, grip, room)` ignores `room`; a code check that no
     `room` operand multiplies `WP.heft`. If JD-1(e) selects a tighter `SWING_FLOOR`, re-measure and reset
     these gates against the new worst-case. **⚠️ These g\*\_closed values are the JD-9-converged fixed
     points; if a different JD-9 option is ratified, re-measure this whole table before implementing.**
  4. **NaN guard:** the staff (S_g(0)=0) yields `Φ_grip = 1.0`; a roster-wide finite-value assertion on
     heft/percussion after the Φ multiply passes.
  5. **BLOCKER-2 + contract equivalence:** at open measure, `select_mode`'s 5-tuple returns
     `sel_gap == w['gap']`, `sel_perc == WP.percussion_authority(w)`, and `sel_pc == w`'s whole-weapon
     `point_concentration` for **every single-mode weapon** (behavior-preserving until intended); a
     composite routed to a blunt sub-element (lucerne_hammer) uses that element's percussion end-to-end
     (selection AND damage), no sel-vs-native perc split; **both select_mode call sites (:69, :123) write
     all five sel_* fields**, and within the closed exchange every `sel_*` field and `c.w` resolve the SAME
     (post-swap) weapon/element in the SAME beat — an explicit test probing the
     `longsword→longsword_halfsword` swap window.
  6. **Room falsifiables (percussion + commit-window only):** a blunt weapon's percussion has an interior
     optimum in room (peaks room≈r\*, floored >0, monotone-down FORBIDDEN); a thrust (rapier pc=0.95) ≈ flat
     in room.
  7. at grip=0/room=r\*, heft AND percussion **byte-identical to today** for the whole roster (Φ=1).
  8. **per-weapon heft + percussion snapshot** (D12c) recorded and Jordan-gated.
  9. determinism + mirror hold; no new red beyond the 8 accepted; `test_gap_game_poleaxe_spikes_plate`
     re-evaluated (JD-3).
  10. `[SIM-CALIBRATE]` on `r*`/`σ`/`floor`/`SWING_FLOOR`; `Φ_grip` thrust-invariance documented
      `[ASSERTED — rigid-body first principles]` with the Rinaldi/PMC10203838 cites demoted. **Requires
      JD-1, JD-8.**

### I3 — Grip-aware reach + TWO-recompute `er` contract + fixed-grip `grip_target` drive (D3), ONE commit. *(Jordan-gated re-baseline; the primary lever.)*
- **Depends on:** I2 (`geom_slide` from I2's bundle). **The primary symptom lever.**
- **Half-switch safety — THE er-freeze fix via TWO recomputes (M-03 + BLOCKER-1 + R-6) AND the
  grip↔reach-oscillator fix (capstone M1 + JD-9):** land grip-aware `reach_base` (reading the **floored**
  `geom_slide`) AND **er REFRESH #1** (top-of-beat, per (A,B), pre-swap, re-derives **only `er`** + the
  longer/shorter labels; **NOT** `measure_gap`/`closed`) AND **er REFRESH #2** (post-swap,
  aggressor/defender, feeding the closed exchange) AND **`grip_target`'s drive term fixed to read
  `reach_base` at grip=0.0** (the JD-9 fix, breaking the second, orthogonal feedback loop) in ONE commit.
  **The half-sword swap STAYS at :120** (role-gated — the hoist is rejected; `close_tempo`/actor-selection
  untouched). Fix `reach_sigma` to read the refreshed `er`. No intermediate state where `reach_sigma` uses
  frozen reach while `str_demand`/`slip_inside`/`close_unwieldiness` use live reach.
- **Acceptance (falsifiable):**
  1. **Single-beat reach coherence (the invariant):** within one beat every reach consumer resolves the
     SAME grip+form-aware reach for a given combatant — pre-swap consumers (`close_tempo` :71, the
     longer/shorter labels, reopen :78/:79) via Refresh #1 AND post-swap consumers (`reach_sigma` :141,
     `str_demand` :163-164, `slip_inside` :230) via Refresh #2. No frozen/live split.
  2. **Byte-identity at open measure:** Refresh #1 at grip=0 (no swap) reproduces today's frozen `er`
     EXACTLY (verified: `reach_base` grip-blind today, so grip=0 == today).
  3. **⚠️ Approach-progression invariant (R-6 gate):** Refresh #1 re-derives ONLY `er` (+labels);
     `measure_gap` remains the running approach decrement (:90) and `closed` stays latched (:93/:81). A
     long-vs-short matchup **reaches `closed` within N beats** (no stall) and a closed engagement whose
     standing reach gap > 0.3 **stays closed** (no un-latch) — an explicit test.
  4. **Two-recompute consistency:** for a non-form weapon (no swap), #1 and #2 agree exactly; for
     longsword/estoc, #2 reflects the shorter half-sword reach (5.99→5.55 / 6.86→5.94) and every closed
     consumer reads it.
  5. `longer == argmax(er)` every beat (subject to JD-2); a mid-engagement choke **visibly shrinks `er`**
     next beat; the mirror `measure_gap` stays symmetric.
  6. **⚠️ units + underflow, CORRECTED anchors (R-4 gate):** a full choke reduces reach by exactly the
     forward geometry lost (`REACH_GEOM_SCALE`-scaled), and **reach stays > L0 for every pole at max
     realistic choke** with the **measured** post-floor targets: **spear 7.797→4.940, glaive 7.200→5.465,
     poleaxe 6.617→5.347, staff 6.489→5.346, guisarme 7.095→5.535** — all > 4.0.
  7. **actor-selection unchanged (blast-radius gate):** the per-beat actor/aggressor selection distribution
     under neutral inputs is **identical to today** (the swap did not move; Refresh #1's grip=0 open-measure
     reach == today) — an explicit distribution test.
  8. **⚠️ NEW — grip↔reach convergence gate (capstone M1 / JD-9):** for every gathering pole (any weapon
     with `grip_choke_max > 0`), the per-beat `grip_position` sequence **converges within N beats (no
     sustained 2-cycle)** once `grip_target`'s drive term is fixed to grip=0.0. Assert the converged values
     match the D2 `Φ_grip@g*` table: spear 0.865, yari 1.0, glaive 0.467, guisarme 0.396, bardiche 0.627.
     An explicit regression that iterates the per-beat recurrence and fails on any oscillation (period-2 or
     longer) beyond N beats.
  9. **balance:** polearm-vs-arming drops out of the 93–96% band; cut-short weapons rise off the floor;
     mirror 50±.
  10. I3's acceptance **re-run AFTER I5** (whose dynamic `range_avail` can re-open a measure I3 closed).
  **Requires JD-2, JD-6, JD-9.**

### I4 — Mode/measure coupling (D5's close-efficacy), ONE commit. *(Object-confusion already unified in I2.)*
- **Depends on:** I0 (`element_ref` for the orphan cross-check; `orient_deg` fore/aft), I2 (the widened
  `select_mode` 5-tuple + grip/room-aware percussion + `sel_gap`/`sel_perc`/`sel_pc` already wired), I3's
  measure semantics; precedes I5 in the dependent chain (I5's `range_avail` feeds D5's close-efficacy).
- **Half-switch safety — close-efficacy + arc-vs-thrust from the SELECTED element's mode:** `select_mode`
  now consumes `closed`/`measure_gap`/`range_avail` in the close-efficacy factor
  `close_efficacy = 1 − (1 − pc_sel)·f(measure_gap, range_avail)`, `pc_sel = c.sel_pc` (the SELECTED
  element's own point_concentration, sourced from I2's D2b threading). Route `sel_head` consistently: pass
  it to `adef_cap` in `reach_threat` (:357), and make `approach_displace` (:448) + the wrapper displace/slip
  gate (:232) read `sel_head`. (The `sel_gap`/`sel_pc` strike/adef/comparator reads already landed in I2; I4
  adds only the close-efficacy factor + the approach-path `sel_head` routing.)
- **Acceptance (falsifiable):**
  1. a composite's selected-element resolution uses that element's own precision (gap AND perc) end-to-end
     — **ji (point 0.680 vs whole 0.560) is the regression anchor**; **bec_de_corbin is NOT an anchor**
     (selects blunt at none/light; its point is the top spike gap 0.800, never the 0.57 beak — R-5);
     goedendag is NOT (stays blunt).
  2. at open measure (`closed=False`) `select_mode` returns the NATIVE head for every weapon except the
     documented poleaxe armour-conditional split, so the approach path is behavior-preserving until
     intended.
  3. the same weapon's armour-defeat is scored on the SAME head everywhere in a beat (no sel/native split
     between `reach_threat` and `armor_defeat_sigma`).
  4. **arc-vs-thrust from the selected element's mode (R-3):** a low-per-element-pc cutter (guandao cleaver,
     voulge cleaver) degrades in the close while a point-selected thrust (bear_spear/spear/yari) does not —
     the close-efficacy factor reads `c.sel_pc`, and a test asserts it does NOT read whole-weapon pc for a
     weapon whose SELECTED element's pc differs from its whole-weapon pc (bear_spear: whole-pc 0.55, but the
     selected point element's pc is high → close_efficacy≈1), and does NOT read `orient_deg` (orient may
     only enter as a fore/aft cue).
  5. `test_combat_element_parity.py` (5 tests) **regenerated deliberately** with reasons in the commit;
     `test_use_mode_selection_emerges…`'s hardcoded `expected` list updated to the new emergent set.
  6. close-efficacy factor ~1.0 at open measure; `test_no_weapon_name_literal` green; no new red beyond the
     8-minus-the-5-regenerated-parity set.

### I5 — Commit/measure coupling + swing-room (D4), ONE commit.
- **Depends on:** I4 (dependent chain — `range_avail` shapes `commit_depth`, D5's close-efficacy, and the
  swing-room legibility term, which reads `c.sel_pc` from I2).
- **Half-switch safety (M-15):** land the `range_utilization` writer (wrapper, before `commit_depth` at
  wrapper.py:128) AND `commit_depth`'s read AND the swing-room legibility term ATOMICALLY. `range_avail`
  reshapes the Beta PARAMS only — confirm the `betavariate` draw order/count unchanged (seeded determinism;
  verified one draw at systems.py:520).
- **Acceptance (falsifiable):** (1) with `range_avail` forced 1.0, I5 **byte-identical to I4** (ablation).
  (2) with real `range_utilization`, the commit distribution AND the greatsword's cramped-quarters outcome
  move beyond noise (else the lever is CUT) — the greatsword's cramped-symptom cure, validated at the ROLL
  (net_sigma/degree), NOT a heft multiply. (3) the commit-window contraction has an interior optimum in room
  (C4 — monotone-down FORBIDDEN). (4) the approach stop-hit gains a commitment-depth term. (5) determinism
  holds (no draw reorder). (6) **re-run I3's acceptance** (I5 can re-open a measure I3 closed).

### I6 — Facing state + lateral-void closing (D6).
- **Depends on:** I0 (`orient_deg` fore/aft, if the profile term is ever promoted — ships neutral so not
  strictly), I1 (facing field). Neutral default reproduces I1–I5 exactly.
- **Half-switch safety:** `facing_target` ships near-neutral so void/profile terms are ~0 ⇒ byte-identical
  to I5. `facing`'s first live reader is here (closes its orphan window from I1).
- **Acceptance:** (1) neutral facing ⇒ byte-identical to I5 (determinism + mirror). (2) the void-term is a
  real but small close contribution; the profile term is `[FIAT — C1]` and near-neutral. (3) no
  per-weapon-class facing (C2) — two weapons with identical stance/measure/grip get identical facing (a
  test). (4) if the profile term reads `orient_deg`, it reads it as **fore/aft only**, never arc-vs-thrust.

### I7a — Rear-clearance close penalty (D7), split from contact.
- **Depends on:** I2 (the D1 bundle's `rear_clearance`). **Landable as early as post-I2** — no grab dep.
- **Half-switch safety:** `rear_clearance` feeds `close_tempo`/`str_demand`; independently ablation-gated.
- **Acceptance:** (1) `rear_clearance(spear) < rear_clearance(guisarme)`; both half-sword forms exceed their
  base form. (2) `rear_clearance` computed from `_all_parts`, NOT `length_m` (a code assertion / no new
  length field). (3) the invariant `rear_clearance(g) = rear_clearance(0) + u(g)` monotone non-decreasing
  holds. (4) **staff (M-20):** the staff's reach/rear-clearance geometry changes with `geom_slide` even
  though its inertia `u` is CoM-clamped at 0. (5) ablation: penalty zeroed → byte-identical to I6; live →
  the choke tradeoff moves outcomes beyond noise (else CUT).

### I7b — Contact axis: contact.py + real Contact state (D8, D9). *(hook_affordance NOT built.)*
- **Depends on:** I7a (rear_clearance producer). **No longer depends on D0's hook discriminator.** The
  riskiest increment, now isolated and smaller.
- **Half-switch safety — BUILD not activation (M-11):** add the `Contact` STATE to `state_graph.STATES`
  (with `to`/`emits`), the `'contact'` TRACE_KIND (verified absent this pass), and the
  `wrapper._emit('contact', …)` call BEFORE wiring `contact.py`. One insertion point in the outcome tail
  (~wrapper.py:253) reading a unified `opening_created` flag set by all three precondition sites — NOT three
  parallel checks. The grab menu must terminate without re-entering the bind inner loop (`beats+=1` at
  :271). DELETE `clinch` from all records in this same commit.
- **Acceptance (falsifiable):** (1) **no grapple path from open measure** (grab_available false without a
  prior bind/beaten-aside/deep-commit opening; open-contact only for dagger/unarmed). (2) **branching
  outcomes fire across seeds** (disarm/throw/pin/control/foot-pin/escape reachable). (3) `grab_sigma`
  derives from **free-hand + leverage** (strength-dominant), **no hook-hardware term**. (4) **`clinch` is
  DELETED** from every `weapons.py` record (grep 0); a CI check that no resolver reads `clinch`. (5) the
  Contact node passes `state_graph.py`'s closure/reachability/emit-legality self-test; the grab menu
  provably does not re-enter the bind `beats` mutation. (6) `capabilities.py` grab/disarm/pin gates match
  live behavior (its `__main__` self-test green). (7) `test_no_weapon_name_literal` green; **no
  `pull_capable`/`hook` data boolean exists in `weapons.py`** (an explicit grep-assertion — the guard
  against the hollow workaround).

### I8 — Joint re-calibration + capstone audit (D11b, D12).
- **Depends on:** all prior.
- **Half-switch safety:** calibration-only + new standing tests; no new mechanic.
- **Acceptance (falsifiable):** (1) `balance.py` at high N + armour matrix: the **reach-class target is
  CONTESTED (~55–75% vs arming), not inverted** — reach still wins the approach; daggers become viable
  underdogs (~30–45%), not winners. (2) cross-cutting gates: mirror/no-one-shot/armour-arc/tradition-
  flatness. (3) **standing anti-orphan test** (D11b): every Combatant circumstance field
  (`facing`/`range_avail`/`sel_gap`/`sel_head`/`sel_perc`/`sel_pc`/…) has ≥1 live reader. (4) **per-weapon
  heft + percussion snapshot** (D12c) reviewed. (5) **every lever ablation-gated** — any lever that does not
  move outcomes beyond noise is CUT: the swing-`Φ_grip` degradation is retained ONLY where it clears the
  worst-case-STR bar (guandao clean-material; voulge/bardiche borderline — JD-1); the percussion-`Φ_room`,
  `range_avail`, the swing-room legibility, rear_clearance penalty, facing void are each ablation-gated.
  (6) full suite: **no NEW red beyond the enumerated accepted-red set** with numpy present, non-zero
  collected (D12a). (7) the `[PHASE-C FLAG]` reds — poleaxe-spike (JD-3), `test_anchor_is_near_one`,
  `test_lunge_quality…` — resolved by Phase-C's REC/MOMENT re-tune (or re-annotated with a recorded reason).
  (8) `INJECTION_POINTS` site strings dropped or tested (D12b).

**Cross-cutting discipline (binding every increment):** primitive-law (no weapon-name/kind branching;
`test_no_weapon_name_literal_in_resolution` green; **no data-boolean workaround for a name-branch**;
**thrust-protection keyed on the SELECTED element's strike mode, never on a weapon class or a whole-weapon
pc scalar**); L0 pure / L2 contribution-out / L3 sole mutator; empty⇒identity proven by OLD-vs-NEW sweep
(not asserted); every new gain `[SIM-CALIBRATE]` or `[FIAT — data absent]` (and every first-principles claim
`[ASSERTED]`, not dressed as a measurement); respect C1/C4/C5 (**no lever falls monotonically/quadratically
with lost room — the swing-room lever has an interior optimum**); mirror fairness + seeded determinism with
**no rng-draw reordering**; verification runs with numpy present, non-zero collected, no new red beyond the
enumerated 8.

---

## Orphan cross-check table

Every NEW field/function → its named consumer → the increment that wires it. Every RETIRED static path
(including clinch).

| New field / function | Layer | Named consumer(s) | Wired in | Notes |
|---|---|---|---|---|
| `orient_deg` (element/mode_element) | L0 data | D6 profile **fore/aft** (I6, if promoted); D5 fore/aft *cue* only (I4) | I0 adds; consumed I4/I6 | **⚠️ NOT the D5 arc-vs-thrust gate** (bands overlap at 0/90; that job is the SELECTED element's mode). NOT a D9 hook discriminator. Orphan window I0→I4/I6 closed by D11b |
| guard `type` | L0 data | D6 fore/aft (I6) | I0 adds; consumed I6 | **NOT** hook-vs-bind (type='lug' collides — verified) |
| `mode_element.element_ref` | L0 data | **D2b per-element percussion mass-lookup (I2)**; D0 build assertion (I0); D5 orphan cross-check (I4) | I0 adds; consumed **I2**/I4 | Explicit index into `elements[]` (voulge fix). **Consumed at I2** (per-element mass), not only I4 |
| `material` (parts) | L0 data | **none in R1** (inert) | I0 adds; **no reader** | Deliberately inert; flagged re-sourcing cost; exempt from anti-orphan (declared inert data) |
| `at_circumstance` `rear_clearance` | L0 | `close_tempo`/`str_demand` penalty (I7a); `contact.py` (I7b) | I2 adds; consumed I7a | From `_all_parts`, never `length_m` |
| `at_circumstance` `geom_slide` (FLOORED) | L0 | `reach_base` (I3); `rear_clearance` (I7a) | I2 adds; consumed I3 | Decoupled from CoM clamp; floored by `GRIP_MIN_WORKING`. Post-floor targets measured (spear 4.94, glaive 5.47) |
| `Φ_grip` (mode-split, SELECTED-head thrust-protection, floored, guarded) in `WP.heft` | L0 | `core.heft_resp`→`core.strike` **cut/thrust/point path ONLY** (I2) | I2 | **Thrust protection keyed on `sel_head=='point'` → Φ_thrust≡1.0** (bear_spear/spear/yari read 1.000); a cut_thrust/cut/blunt-selected strike degrades its swing fraction by the SELECTED element's `pc_sel` (sourced from `c.sel_pc`). **Validated MATERIAL worst-case-across-STR: guandao ≤0.76 (clean); voulge ≤0.88 / bardiche ≤0.88 (borderline — JD-1); inert for greatsword.** Does NOT touch the blunt-percussion path (core.damage:153) |
| **⚠️ `Φ_room` — NOT on the heft path (CUT; existence is JD-1(d))** | — | — | — | **A monotone heft-room multiply violates C4; a 0.5× factor moves greatsword STR4 24→17 (~29%, NOT "8% cosmetic"). REMOVED from `WP.heft`.** The room term lives on percussion (D2b) + commit-window/legibility (D4) |
| `Φ_grip`/`Φ_room` in `percussion_authority` | L0 | `core.damage` blunt path via `sel_perc` (I2); `adef_cap`/`puncture_pressure`/`reach_threat` (I2) | I2 | The blunt Impact degradation channel; Φ_room retained here (reaches the sigma path — not cosmetic); threaded through `puncture_pressure` atomically (D2b) |
| **widened `select_mode` return `(dm, h, sel_gap, sel_perc, sel_pc)`** | L2 | wrapper writes `c.sel_*` at BOTH :69 and :123 (I2) | I2 | **⚠️ R-7 contract fix, extended by capstone M2 to a 5-tuple**: `element_afforded` carries per-element (gap, perc, point_concentration, element_ref); `afforded_heads` carries them through; single-mode weapons default to whole-weapon values (byte-identical) |
| per-element percussion (`element_afforded` blunt) | L2 | widened `select_mode`/`afforded_heads` (I2) | I2 | Distinguishes multi-blunt composites (lucerne_hammer); consumes I0 `element_ref` for the mass lookup; computed as a per-element application of the `percussion_authority` FORM (mass_kg + x_m moment arm), **not** `at_circumstance` (capstone M4 correction) |
| **`c.sel_perc` field** | L3 state | **`core.strike` (:171) — BLOCKER-2 fix** (I2) | I2 | Selected element's percussion; canonical perc source in damage. Written at BOTH select_mode sites. Native fallback when unset. Anchors lucerne_hammer |
| **`c.sel_gap` field** | L3 state | `core.strike`, `adef_cap`, `select_mode` comparator (I2) | **I2** | **Lands with the widened return that produces it.** Canonical gap source (fixes M-02); **anchor = ji** (bec dropped). Written at BOTH select_mode sites |
| **`c.sel_pc` field (NEW — capstone M2 fix)** | L3 state | **D2's cut_thrust `pc_sel` blend (I2)**; D5's `close_efficacy` (I4); D4's swing-room legibility term (I5) | **I2** | The winning `mode_element`'s own `point_concentration` — an unthreaded existing primitive (not a new fiat scalar). Written at BOTH select_mode sites alongside `sel_gap`/`sel_perc`. Closes the plumbing gap the arc-vs-thrust redesign hinges on |
| `c.range_avail` field | L3 state | `commit_depth` (I5); D5 close-efficacy (I4); swing-room legibility (I5) | I1 scaffolds; consumed I4/I5 | Orphan window I1→I4/I5; closed by D11b |
| `range_utilization(c, measure_gap, cfg)` | L2 | writes `c.range_avail` (I5); `stophit_sigma` commit term (I5) | I5 | Reshapes Beta params only; no rng reorder; interior optimum (C4) |
| swing-room term in `legibility` | L2 | `read_contest`→`net_sigma` (I5) | I5 | The greatsword's cramped-quarters cure (reaches the roll); `(1−pc_sel)`-weighted, `pc_sel` from `c.sel_pc`; `[SIM-CALIBRATE]` |
| `c.facing` field | L3 state | `facing_target` writer + void/profile readers (I6) | I1 scaffolds; consumed I6 | Orphan window I1→I6; ships neutral |
| `facing_target(c, closed, cfg)` | L2 | writes `c.facing` (I6); void into close, profile into `reach_sigma`/legibility | I6 | Keys stance/measure/grip only (C2) |
| **er REFRESH #1 / #2** (two-recompute) | L3 orchestration | reopen/tempo (#1 — `er` only); `reach_sigma`/`str_demand`/`slip_inside` (#2) (I3) | I3 | **Replaces the hoist** (BLOCKER-1). **#1 re-derives ONLY `er` + labels, NOT `measure_gap`/`closed`** (R-6). #2 post-swap; consistency-proven. **Orthogonal to the grip↔reach oscillator (capstone M1)** — the `er` plumbing is internally sound and does not create or cure the oscillation; that is fixed separately by JD-9's fixed-grip `grip_target` drive input, landed in the SAME I3 commit |
| **`grip_target`'s fixed-grip drive input (NEW — capstone M1 / JD-9)** | L2 | `grip_target` (systems.py:155, wrapper.py:66) | I3 | Breaks the `grip_target → close_unwieldiness → reach_base → grip_position` feedback loop created by D3's grip-aware `reach_base`. `reach_base` stays grip-aware for its ~10 OTHER consumers; only `grip_target`'s own drive term reads it at a fixed grip=0.0 |
| `contact.py`: `grab_available`/`grab_sigma`/`grab_outcome` | L2 | wrapper outcome-tail `opening_created` branch (I7b) | I7b | `grab_sigma` = free-hand + leverage ONLY; single insertion point; no bind-loop re-entry |
| `state_graph` `Contact` STATE + `'contact'` TRACE_KIND | L3 | `wrapper._emit('contact',…)` (I7b); `state_graph` self-test | I7b | BUILT (not activated); real edges. Verified absent today (15 STATES, no 'contact' kind) |
| `capabilities` grab/disarm/pin gates | L2 | `capabilities.capability_table` + state-graph annotation | I7b | Verified vs live behavior |
| standing anti-orphan test | test | CI (I8) | I8 | Every circumstance field has ≥1 reader |
| per-weapon heft + percussion snapshot | test | CI (I2, I8) | I2 | Makes a re-anchor visible for all weapons |

| Retired / deleted static path | Was | Removed in | Replacement |
|---|---|---|---|
| `clinch` weapon field (~54 records) | dead 1–10 scalar, 0 readers | I7b (DELETE) | `grab_sigma` = free-hand + leverage (D9); **NOT** hook hardware |
| whole-weapon `w['gap']` in strike/adef/comparator | read from baked dict | **I2** | `c.sel_gap` (selected element's own `geo['gap']`, emitted by the widened select_mode) |
| **whole-weapon `WP.percussion_authority(w)` in `core.strike` (:171)** | **whole-weapon perc on a SELECTED element (BLOCKER-2)** | **I2** | **`c.sel_perc` (selected element's percussion); native fallback when unset** |
| **whole-weapon `point_concentration` implicitly assumed for the cut_thrust blend / close_efficacy (capstone M2)** | **no producer existed for `pc_sel`** | **I2** | **`c.sel_pc` (selected element's own point_concentration, sourced in `element_afforded`)** |
| **`select_mode` 2-tuple return `(dm, h)`** | **element identity lost; sel_gap/sel_perc/sel_pc unproducible (R-7 + capstone M2)** | **I2** | **5-tuple `(dm, h, sel_gap, sel_perc, sel_pc)`; both call sites capture** |
| native `w['head']` in `approach_displace`/wrapper displace gate/`reach_threat` | static head | I4 | `sel_head` (selected mode-head), native fallback only when unset |
| `omega_cap`/`m_eff` bundle members (R0-original) | ill-posed KE operands | never added | D2's mode-split `Φ_grip` on the static-moment ceiling |
| `Φ_grip = S_g(g)/S_g(0)` on the whole heft path | collapsed thrust to 0/NaN | never shipped | grip-invariant thrust (keyed on selected head) + floored, guarded swing `Φ_grip` |
| **whole-weapon-pc blend for thrust-protection** | **mis-orders bear_spear (pc 0.55) below greatsword (pc 0.62); degrades a pure-thrust pole ~22% (R-3)** | **retracted** | **SELECTED element's strike mode: `sel_head=='point'`→Φ≡1.0; cut_thrust degrades its own swing fraction, weighted by `c.sel_pc`** |
| **`Φ_room` on the heft path** | **monotone heft-room multiply violates C4; direction/existence is a fork (R-8)** | **never shipped (CUT; JD-1(d))** | **percussion-Φ_room (reaches sigma) + commit-window/legibility swing-room (D4, reaches the roll)** |
| `hook_affordance` from `orient_deg` sign | unbuildable — bands interleave | never built (dropped) | free-hand + leverage grab (D9); pull-hook hardware deferred (JD-7) |
| **the "hoist half-sword swap to top-of-beat" sequence** | **structurally impossible (swap is role-gated; hoist cycles — BLOCKER-1)** | **never shipped (rejected)** | **two-recompute `er` contract; swap stays at :120; close_tempo/actor-selection untouched** |
| **re-deriving `measure_gap`/`closed` from `er` every beat** | **stalls the running approach decrement (:90) + un-latches `closed` (:93/:81) (R-6)** | **corrected** | **Refresh #1 re-derives ONLY `er` + labels; `measure_gap` stays the :90 decrement, `closed` stays latched** |
| **"orient_deg cleanly gates arc-vs-thrust" / "pc separates cleanly"** | **BOTH false (cutting blades + thrusts at orient=0; pc bands overlap in the wrong order — R-3)** | **retracted** | **the SELECTED element's strike mode is the arc-vs-thrust discriminator (D5); orient_deg demoted to fore/aft (D6); whole-weapon pc not used for the gate** |
| **bec_de_corbin sel_gap anchor (point 0.57 vs whole 0.82)** | **bec selects BLUNT at none/light; its point is the spike 0.800, never 0.57 — never exercises the branch (R-5)** | **dropped** | **ji (point 0.680 vs whole 0.560, vs armour) is the sound sel_gap/sel_perc anchor** |
| **`grip_target`'s drive term reading the newly grip-aware `reach_base` (capstone M1)** | **would close an unlatched per-beat feedback loop — every gathering pole's grip/reach flips every beat, forever (spear 0↔0.865, reach 7.797↔5.326)** | **never shipped (fixed at I3, same commit as D3)** | **`grip_target`'s drive term reads `reach_base` at a FIXED grip=0.0; `reach_base` stays grip-aware for all other consumers (JD-9)** |
| `INJECTION_POINTS[...]['site']` line strings | hardcoded `wrapper.py:NN`, unread | I8 | dropped, or a test that the line-range still holds the logic (D12b) |
| `select_mode`'s ignored `closed` param | received, never read (systems.py:302) | I4 | consumed in the close-efficacy factor (D5) |

---

## JORDAN-DECISIONS

Items unresolvable without Jordan's call. Each states the fork, the evidence, and the plan's default. These
are the loop's (and the capstone pass's) genuine open forks — **not invented resolutions**.

### JD-1 — Grip-degradation of the THRUST, the retained-material set, AND the greatsword cramped-quarters cure (BLOCKER-class, D2/D4)
Jordan asked the damage side to read the same `I_g` bundle the cost side reads at the same grip.
**Interpretations tried, and the measured findings:**
- The **literal `½·I_g·ω²`** at fixed ω **re-manufactures reach dominance** (spear I_g largest → the exact
  84–96% symptom; verified spear 0.98 > poleaxe 0.73 > greatsword 0.51).
- The **first-correction `Φ_grip = S_g(g)/S_g(0)`** on the impact path **collapses the closed thrust to ~0**
  (yari 0.000, spear 0.135; staff NaN).
- **The default (grip-invariant thrust keyed on the SELECTED element's mode + floored swing-`Φ_grip`):**
  verified `Φ_grip@closed` bear_spear/spear/yari **1.000** (all select `point`), ji 0.87. **Measured through
  `core.damage` (worst-case across STR 2/4/6/8):** the swing lever is **material only for the low-pc
  high-heft choppers that gather** — **guandao 71–76% (clean-material)**, **voulge 81–88% and bardiche
  77–88% (BORDERLINE — a ≤15% cut only at low STR)** — and **inert for the greatsword** (cannot choke,
  g\*=0.045, Φ=0.9996) and for point-selected strikes (thrust-protected, by design).
- **Finding — the retained-material set is not as clean as earlier passes claimed.** Only guandao is
  unambiguously material. **Fork (JD-1a):** (i) retain guandao only as clean-material and accept
  voulge/bardiche as *borderline, ablation-gated*; (ii) drop voulge/bardiche from the retained set entirely
  (accept no material grip-damage for them); (iii) tighten `SWING_FLOOR` (JD-1e) so voulge/bardiche clear a
  real ≤15% threshold at STR8 too. **Plan default: (i)** — guandao clean, voulge/bardiche
  borderline+ablation-gated.
- **Finding — the greatsword cramped-quarters cure via a heft-room term is a genuine fork, not a settled
  cosmetic (JD-1d, R-8).** A Φ_room-on-heft is NOT "~8%, int-rounds away"; **measured, a 0.5× room heft
  factor moves greatsword STR4 damage 24→17 (~29%)** — so it is NOT negligible, but it is **monotone in lost
  room, which violates C4**, and its direction (does cramped space *reduce* a greatsword's delivered force?)
  is a design judgment. **Fork (JD-1d):** (i) keep Φ_room OFF heft; route the cure through the commit-window
  + legibility (non-monotone, C4-honest) + D2b percussion for armour [**plan default**]; (ii) put a
  heft-room term back on with an **interior optimum** (C4-compliant, not a monotone ramp) and Jordan sets the
  peak/shape; (iii) accept a near-invisible lever, or raise `DMG_SCALE` granularity.
- **Fork (JD-1, overall):** (a) ratify the selected-element-mode thrust-protection + "swing-`Φ_grip`
  material where validated (guandao clean, voulge/bardiche borderline), Φ_room off heft, greatsword cured
  via commit-window/legibility" [**plan default**]; (b) insist the thrust degrade in grip too — then it
  needs a **thrust-appropriate** degrading operand (`m_head` behind the point, floored well above 0), NOT
  `S_g`, and Jordan sets the floor; (c) accept the literal `I_g`-as-energy form with its documented roster
  inversion (re-opening M-01). The measured zero-collapse of variant 2, the ~71–88% (not ~71/77/74%)
  retentions, and the ~29% (not ~8%) greatsword heft-room delta are surfaced as the fork, not hidden.
- **(JD-1e)** — Optional: choose a tighter `SWING_FLOOR` so the swing lever clears a real threshold at STR8
  too; re-measure the I2 gate #3 worst-case column against the new floor.

### JD-2 — May the `longer/shorter` label flip mid-engagement? (BLOCKER, D3/I3)
The label is computed once from frozen `erA/erB` (wrapper.py:37) and drives `reopen_moment` + the whole
approach asymmetry. Grip-aware reach can make a choked long-weapon momentarily "shorter". **Fork:** (a)
recompute the label each beat from the refreshed `er` (mechanically consistent, but approach roles can swap
mid-engagement); (b) freeze the label at engagement start for role stability, refresh only `er` (Refresh #1
recomputes `er`; the label is held). **Plan default:** (b) — the smaller behavior delta, consistent with
"the longer weapon" being the engagement's structural aggressor identity; revisit if I8 balance shows the
frozen label mis-attributes reopen moments.

### JD-3 — Poleaxe hammer-vs-spike vs plate: which selection is canonical? (SERIOUS, I2/I4)
Two tests are RED by design today (`test_gap_game_poleaxe_spikes_plate`, `test_use_mode_selection_emerges…`)
because Phase B's more-accurate forward poleaxe mass lifted its percussion authority (7.48) above the mace's
(7.45), so it selects its **hammer** vs plate rather than its **spike**. The historically-correct armoured
kill is the thrust-to-gap (spike). **Fork:** (a) recalibrate the `[SIM-CALIBRATE]` engine-scale gains
(`PERC_SCALE`/`PERC_EXP`, `ADEF_BLUNT`/`ADEF_POINT`, `GAP_EXPOSURE['plate']`) in I2/I8 so the spike wins vs
plate under the now-accurate masses [plan default]; (b) accept the hammer selection as emergent truth and
update the two tests. Either way a **deliberate golden/expected update with a recorded reason**, never a
per-weapon mass fudge.

### JD-4 — Percussion grip-invariance for a hammer (SERIOUS, D2b)
A hammer's striking mass doesn't move on the haft, so its percussion could be grip-INVARIANT even while
cut/thrust becomes grip-aware. Note the repaired D2 already makes a blunt weapon's `Φ_grip` mild (mace
pc≈0.02 → floored swing degradation, never a collapse). **Fork:** (a) make percussion read the same
mode-split `Φ_grip`/`Φ_room` as the blunt Impact path [plan default — coherence, avoids the M-08 asymmetry];
(b) keep percussion grip-invariant and declare the blunt/cut asymmetry intended (in the config/docstring so
the I8 ablation gate does not read it as noise).

### JD-5 — The 7 silent-zip composites: author modes or document mass-only? (schema, I0/D0)
dangpa, spetum, partisan, guandao, fauchard, flamberge, hook_sword have >1 located part but 0
`mode_elements`. **Fork, per weapon:** (a) author explicit `mode_elements` (with `element_ref`/`orient_deg`),
or (b) document `mass-model-only by design`. **Plan default:** author modes for the ones whose extra element
is a genuine *strike* alternative (guandao rear hook-notch, fauchard back-hook, hook_sword crescent);
document mass-only for the pure bind/catch lugs (spetum/partisan/dangpa wings). Jordan may override any call.
(Orthogonal to the dropped grab-hardware question — JD-7.)

### JD-6 — Ratify the TWO-recompute `er` contract (D3/I3) — the hoist is REJECTED
A prior pass proposed hoisting the half-sword swap to top-of-beat; verified structurally impossible (the
swap needs aggressor/defender roles not known until :117, which depend on `close_tempo`/`ready` at :70-72,
so the swap cannot move above :72; and hoisting it above `close_tempo` would change WHO acts). The chosen
contract refreshes `er` at TWO points — **#1** at true top-of-beat per (A,B) pre-swap (**re-derives only
`er` + labels**, feeds reopen/tempo), **#2** after the role-gated swap for aggressor/defender (feeds the
closed exchange) — with the swap **staying at :120**. This introduces **NO tempo change and NO
actor-selection change** (both read the pre-swap Refresh #1, byte-identical to today at open measure).
**Fork:** (a) ratify the two-recompute contract [**plan default**]; (b) accept a single recompute AND
additionally hoist role/actor determination itself, then re-prove tempo/actor-selection against the mirror +
determinism [heavier]. Default (a). *(A materially smaller ask — no behavior change to ratify, only the
two-recompute plumbing; Refresh #1 re-derives only `er`, not the running `measure_gap`/latched `closed`.)*
**Note (capstone):** this contract was independently re-verified as internally consistent and sound, and is
confirmed ORTHOGONAL to JD-9 below — ratifying JD-6 does not resolve JD-9, and vice versa; they fix two
different, independent defects in the same D3/I3 increment.

### JD-7 — Defer or fund a NEW pull-vs-bind grab primitive? (schema, D9)
Pull-hook grab hardware is dropped because no primitive discriminates a pull-hook from a bind-lug
(orient_deg bands interleave; `type='lug'` collides; the distinction is prose-only and fuzzy). A
hand-authored `pull_capable` boolean is forbidden (a `clinch`-class scalar invisible to the name-literal CI
guard). **Fork:** (a) accept grab = free-hand + leverage only, and defer pull-hook grab affinity
indefinitely [plan default]; (b) fund a **future** morphology re-ingestion increment that re-sources a NEW
grounded, CI-checked drag-capability primitive (a signed hook-return/curl-back geometry per catch element,
distinct from orient_deg) from the Phase-0 `geom_notes`, and rewrites the grab derivation to read THAT.
Default (a).

### JD-8 — Is a versatile `cut_thrust` pole (partisan/spetum) genuinely part-swing in the close? (D2/D5)
The thrust-protection fix keys grip-invariance on the SELECTED element's head. A pure `point` weapon
(bear_spear/spear/yari) is fully protected (Φ=1.0). But partisan and spetum are `cut_thrust` and SELECT
`cut_thrust` even vs heavy (verified — and, unlike bear_spear/spear/yari, they have NO authored
`mode_elements` today, so `select_mode` can only ever return `cut_thrust` for them; see M3), so under the
fix their swing fraction still degrades (partisan Φ 0.750, spetum 0.860). **This is defensible** — a
cut_thrust weapon that is not committing its pure point genuinely swings, so its swing fraction *should*
degrade in the close. **Fork:** (a) accept partisan/spetum as genuinely part-swing → their cut_thrust
selection degrades its swing fraction (weighted by that element's own `pc_sel`, via `c.sel_pc`) [**plan
default** — physically honest; the alternative over-protects a broad blade]; (b) if Jordan judges these
ox-tongue/spetum blades are used point-first in the close (a thrust-primary reading), author their
`cut_thrust` mode_element to select `point` vs medium/heavy (a D0 authoring call, JD-5-adjacent) so they
gain full thrust-protection there. Default (a); the plan does NOT silently assert them fully
thrust-protected.

### JD-9 — Which reach drives `grip_target`'s gather decision? (BLOCKER-class, D3/I3 — pairs with JD-6, found by the capstone verification pass)
**The fork.** D3 makes `reach_base` grip-aware so a choked-up pole reads a shorter reach (the primary fix
for the 84–96% reach-dominance symptom). But `grip_target` — the function that DECIDES how much to
choke — itself reads `close_unwieldiness`, which is built from `reach_base` (systems.py:142/155). Once
`reach_base` depends on `grip_position`, and `grip_target` decides `grip_position` FROM `reach_base`, the
two become mutually dependent within the per-beat loop: `grip_position(beat n)` is computed from
`reach_base` evaluated at `grip_position(beat n-1)`, which was itself the prior beat's output of the exact
same computation. `grip_choke_max` (weapon_physics.py:448) reads only the static weapon record, so it
cannot break this cycle.

**Why this matters (the stake, not just the mechanism).** This is not a subtle numerical wobble — iterating
the live recurrence against the engine's real constants (`CLOSE_REACH_REF=6.5`, `CHOKE_DRIVE_REF=1.5`,
`L0=4.0`, `REACH_GEOM_SCALE=0.635`, `REACH_2H_K=0.4`) produces a **hard, permanent 2-cycle** for every
weapon that can gather at all: a closed-quarters spear would flip between `grip_position=0` (reach 7.797)
and `grip_position=0.865` (reach 5.326) **every single beat, forever** — a swing of ±2.47 reach-units each
beat. The same happens for yari/guandao/voulge (0↔1.0), glaive (0↔0.467), guisarme (0↔0.396), and bardiche
(0↔0.627). Concretely: this describes a fighter whose hand position and effective reach flicker between two
completely different states every beat of a fight, which no real combatant does, and which corrupts every
downstream reach-dependent quantity (`reach_sigma`, `str_demand`, `slip_inside`, `close_tempo`, the reopen
`base_gap`) each time it flips — a bug that would make the entire circumstance-degradation redesign produce
visibly nonsensical combat behavior for exactly the gathering-pole matchups it exists to fix.

**Options verified (with their concrete consequences):**
- **(A) RECOMMENDED — fix `grip_target`'s drive input to a constant grip=0.0.** `grip_target`'s own drive
  term reads `close_unwieldiness` evaluated at open-measure reach (grip=0) via a dedicated variant used only
  by `grip_target` — a one-line change at systems.py:155. This breaks the cycle because the value driving
  the gather decision no longer depends on the gather decision's own output. Verified: this converges to
  STABLE (non-oscillating) fixed points that **exactly match the plan's own existing D2 `Φ_grip@g*` table** —
  spear 0.865, yari 1.0, glaive 0.467, guisarme 0.396, bardiche 0.627. Practical consequence: **choosing (A)
  requires changing NO other number anywhere else in this plan** — every D2 damage-retention figure already
  quoted stands unchanged. `reach_base` itself STAYS grip-aware for its ~10 other consumers (that remains
  the entire point of D3) — only `grip_target`'s own input reverts to a fixed reference point.
- **(B) Under-relaxation.** `g[n] = 0.5·(g[n-1] + f(g[n-1]))` — verified convergent (spear converges to
  g*=0.298, roughly a third of option A's value), but converges to a **DIFFERENT** g*, which would ripple
  into different D2/D3 damage-retention numbers (the whole per-weapon table would need re-measuring), and it
  adds a new tuning knob (`[SIM-CALIBRATE]`) with no independent physical grounding for its relaxation
  constant.
- **(C) Latch `grip_position > 0` while `closed` holds.** Would need an explicit reset rule not yet
  specified — what resets it (reopen? displace? both?), and whether the latch itself needs its own
  convergence proof. More design surface, more edge cases, and not yet fully worked out.

**Plan default: (A).** It is the smallest, most mechanically targeted intervention — it fixes only the
specific feedback path (grip_target's drive input), leaves `reach_base`'s grip-awareness intact everywhere
else (the actual point of D3), and requires zero re-measurement of any number already in this plan. Options
B and C are live alternatives if Jordan judges the physical assumption behind (A) — that the gather decision
should be driven by the weapon's OPEN-MEASURE reach, not its currently-adopted grip — is wrong.

**Relationship to JD-6.** This is a **second, independent** fork from JD-6, even though both concern D3/I3's
per-beat reach mechanics. JD-6 is about the `er` dict refresh contract (a plumbing/staleness question,
verified internally sound and unaffected by this one). JD-9 is about a genuine feedback-stability defect
introduced BY making `reach_base` grip-aware in the first place. Ratifying JD-6 does not resolve JD-9, and
the two fixes land in the same I3 commit but are otherwise orthogonal — confirmed by an independent capstone
verifier tracing both mechanisms separately against the live code.

---

### Appendix — verified-sound decisions carried unchanged (register Appendix A)
L0 purity of `at_circumstance` (weapon + scalars, no Combatant); facing/range_avail as per-beat Combatant
state with the wrapper as sole mutator; `contact.py` as its own L2 module; grip bounds well-formed
(`grip_choke_max`/`grip_travel_max` clamp); `rear_clearance(g)=rear_clearance(0)+u(g)` monotone for the
roster; mirror-symmetry preserved by the pure L0 bundle; D6 facing near-neutral sound. **⚠️ Two earlier
"sound" claims are RETRACTED (both verified false this pass):** (1) the `orient_deg` re-ingestion does NOT
make D5's arc-vs-thrust gate buildable via a clean orient gate (bands overlap at 0/90); (2)
`point_concentration` does NOT separate arc from thrust cleanly either (whole-weapon bands overlap in
`[0.55,0.62]` in the wrong order — bear_spear pc=0.55 < greatsword pc=0.62). D5's arc-vs-thrust is
re-grounded on the **SELECTED element's strike mode / per-element pc** (bear_spear selects `point` →
protected), and `orient_deg` supports D6's fore/aft signal only. Each surviving sound decision keeps its
stated invariant (and gains the structural test the register recommends).

**Capstone verification record (3 independent opus-max verifiers, post-loop):** the `coherence-jd` lens
PASSED CLEAN — the increment dependency chain (I0→I1→…→I8), the orphan cross-check table, all 8 original
Jordan-decisions, and every sampled `[R-*]`/`[M-*]` closure claim were independently re-verified against
live code with zero additional findings. The `dynamics-oscillator` and `emergence-gate` lenses each found
exactly the items folded in above (JD-9 / the grip↔reach oscillator; the `sel_pc` plumbing gap; two wording
precision fixes) — nothing else. No further open items remain outside the 9 Jordan-decisions.

### Critical files
`weapon_physics.py` (at_circumstance/heft/percussion_authority/agility/rear_clearance) · `systems.py`
(reach_base/select_mode[+widened 5-tuple return]/element_afforded/afforded_heads/approach_displace/
commit_depth/range_utilization/facing helpers/adef_cap/reach_threat/puncture_pressure/grip_target[fixed-grip
drive input, JD-9]) · NEW `contact.py` (grab/pin) · `wrapper.py` (per-beat grip/select_mode at :69 + :123,
er REFRESH #1/#2, facing/range_avail writes, contact branch, mutation) · `core.py` (thread grip/room +
sel_gap/sel_perc into heft_resp/strike) · `combatant.py` (facing/range_avail/sel_gap/sel_perc/sel_pc fields)
· `config.py` (SWING_FLOOR/r*/σ/floor blocks, all `[SIM-CALIBRATE]`) · `state_graph.py` (Contact node +
'contact' TRACE_KIND) · `capabilities.py` (grab/disarm/pin gates) · `weapons.py` (I0 schema restore; I7b
clinch DELETE) · `tests/valoria/test_combat_*.py` · `workbench/balance.py`.
