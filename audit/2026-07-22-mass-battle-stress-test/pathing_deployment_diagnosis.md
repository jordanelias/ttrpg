# Pathing & deployment diagnosis — multi-unit formations are geometrically wrong

**2026-07-22, Jordan-flagged from the hierarchy snapshot** ("the Cannae envelopment wheels weird and
units aren't trying to get behind the enemy; some subunits overlap; the refused flank makes no sense").
Confirmed by direct measurement — these are real deployment/pathing bugs, not rendering artifacts.

---

## 1. Root cause: `build_army`'s deployment is a rightward column-of-columns

`engine.build_army` places subunit `i` at `starting_position = (start_row, 15 + i*4)` — every subunit at
the **same row**, marching **rightward** in 4-column steps from an arbitrary column 15. This single
default poisons all three army builders:

**Envelopment (`build_envelopment`, center + 2 wings), measured:**
```
sub0 (center) centroid c16.5  col-span [15,18]
sub1 (wing)   centroid c20.5  col-span [19,22]
sub2 (wing)   centroid c24.5  col-span [23,26]
```
- **Both wings are to the RIGHT of the center** — there is no left wing. A Cannae *double* envelopment
  needs wings on **opposite** flanks (one left, one right) that mirror each other and close from both
  sides. Here both "wings" pile onto the same (right) side, so `_envelop_goal` sends both around the
  *same* flank -> the weird wheel, and no ring ever forms.
- Col-spans are near-adjacent (gaps of 1); once subunit width grows past the 4-col step, **they
  overlap**.

**Refused flank (`build_refused_flank`, strong + refused), measured:**
```
sub0 (strong)  centroid r35.5 c17.5  col-span [15,20]
sub1 (refused) centroid r35.0 c20.5  col-span [19,22]
```
- Both subunits at **the same row (~35)** — the refused wing is **not echeloned back** at all. A refused
  flank *is* an echelon: the refused wing sits **rearward** and at an angle. Here it's level with the
  strong wing.
- Col-spans **[15,20] and [19,22] overlap at cols 19-20** — the two subunits are physically
  interpenetrating. This is the "makes no sense" the snapshot showed.

## 2. The three concrete bugs

| # | bug | cause | correct behaviour |
|---|---|---|---|
| **P-1** | subunits **overlap** | deployment step (4 cols) < subunit frontage (6+ cols at battle scale) | space subunits by **their own frontage + a gap**, never a fixed step |
| **P-2** | envelopment wings on the **same side** | `col = 15 + i*4` marches one direction; no notion of center vs flanks | center on the anchor; wings placed **symmetrically left & right**, wide of the center's frontage |
| **P-3** | refused flank **not refused** (same row, overlapping) | `build_refused_flank` only sets stance/orders, never moves the refused wing back | deploy the refused wing **echeloned rearward** (and to one flank), out of the initial line of contact |

Downstream of P-2, `_envelop_goal` (the two-phase wrap-to-rear) is *itself* plausibly correct — it
steers wide of the nearer flank (`ac < cen_c ? left : right`) and past the enemy depth, then turns in —
but it is fed a **broken starting geometry** (both wings on one side, cramped), so it cannot produce a
symmetric double envelopment. **Fix the deployment first, then re-verify the pathing** (P-2 may largely
resolve the "weird wheel" on its own; P-1/P-3 are independent deployment fixes).

## 3. What "correct" must look like (to be grounded by the historical research, then encoded)

- **Battle line (3-11 subunits):** subunits spread across a frontage **centered on the army anchor**,
  each separated from its neighbour by a gap that is a fixed fraction of unit frontage (the Roman
  *quincunx* used gaps ~= one maniple-frontage; a solid hoplite line used near-zero gaps). Reserve
  subunits sit in a **second line**, offset rearward.
- **Envelopment (Cannae):** a center that holds/gives ground, flanked by **symmetric** wing forces on
  **both** flanks, initially slightly forward (the convex crescent) then closing inward; cavalry sweeps
  around to the rear. The two wings' wrap paths **mirror**.
- **Refused flank (Leuctra / Leuthen):** a strong wing forward + leading, the rest of the line
  **echeloned back** at an offset, declining contact until the strong wing has decided its flank.

## 4. Test coverage gap

Current presets and the gauge test almost entirely at **1 subunit per side** (the byte-exact battery)
or **3** (envelopment/refused). Jordan's directive: test at **minimum 3 subunits, up to 11**. The
deployment fix must be verified across that range (spacing must not overlap at 11 subunits; the
envelopment must stay symmetric; the line must stay centered).

## 5. Fix plan

1. **Frontage-aware deployment in `build_army`** — replace `15 + i*4` with a layout that measures each
   subunit's frontage and lays them out centered on the anchor with a proportional gap (no overlap at
   any subunit count). *(P-1)*
2. **Symmetric wings in `build_envelopment`** — center on anchor; distribute wings alternately left/right
   of center, wide of its frontage. *(P-2)*
3. **Echeloned refused wing in `build_refused_flank`** — deploy the refused specs **rearward** (row
   offset) and to a flank, non-overlapping. *(P-3)*
4. **Re-verify `_envelop_goal`/refused pathing** tick-by-tick with the corrected deployment across 3-11
   subunits. *(P-2 follow-through)*
5. **Historical comparison** — schematic (grounded in the geometry research) vs sim output, tick-by-tick,
   in `research/diagrams/mass_battle_formations/`.

All deployment changes are additive geometry; the byte-exact grid oracle (single-subunit, explicit
`starting_position` path) must stay green (I4).

## 6. RESOLVED (ED-MB-0017)

**P-1/P-2/P-3 fixed + machine-vision-verified** (`research/diagrams/mass_battle_formations/` — schematics
vs sim, tick-by-tick; `test_deployment_geometry.py`, 16 cases): frontage-aware centred line (no overlap,
1–11 subunits, provably by construction), symmetric envelopment wings wheeling opposite senses, echeloned
refused wing.

**P-4 — envelopers must be FAST (Jordan 2026-07-22):** "if you aren't applying speed to these units the
envelopment will always be worse — it's just units being assaulted on their own for way too long."
Without speed the enveloping wings arrive piecemeal and are defeated in detail. Two grounded speed
levers: `PC_ENVELOP_SPEED_MULT` (2×, the envelop/sweep *maneuver* — a rapid flanking march, out of
contact; envelopment is a timing race, du Picq / Crécy-Leuctra) and `PC_CAVALRY_SPEED_MULT` 2.0→**3.0**
(cavalry march ~3× infantry — "infantry marched to keep formation, cavalry did not"). Measured: infantry
1.0 cells/tick, cavalry 3.0, cavalry envelop ~6 → a cavalry double envelopment now wraps *behind* by
~t6–8 (was t16–20 for slow infantry wings). Both levers are INERT for line-vs-line battles (no
envelop/sweep instruction, not cavalry) → the gauge/signature line battles stay byte-exact.

**Adversarial critic pass (independent review) — findings resolved:**
- **F1 (crash on over-wide armies): FIXED.** `_centered_line_cols` now fits the block to the field
  (gap-collapse → linear compression → per-subunit on-board clamp); degrades to overlap, never the
  off-board `ValueError` (0 crashes / 200 fuzzed configs incl. 11×2500-troop).
- **F2 (`gauge_mb.make_mixed_unit` had the same `10+i*4` defect): FIXED** (routed through
  `_centered_line_cols`; no live gauge row hit it — they set explicit positions — so no gauge-result
  change).
- **F3 (odd wing counts asymmetric): tested** — no crash, wings still split L/R; a lopsided wing mass for
  odd counts is the honest geometry (you can't perfectly double-envelop with an odd wing count).
- **F4 (refused echelon only statically tested): dynamic test added** — the refused wing stays farther
  from the enemy than the strong wing through a live battle.
- **F5/F7 (nits, follow-on):** `_spec_span` falls back to `Line` for an unknown role (unreachable today —
  `build_army` validates first); `build_envelopment`/`build_refused_flank` hardcode field-centre 25 (no
  `anchor_col` param of their own). Low priority.

**Still open (follow-on, not this fix):** the wrap seals to a *horseshoe*, not a full ring (no cavalry
rear-transit phase); single line only (no reserve/triplex depth-lines); and envelopment still often
*loses* the battle outcome — the DG-6 "envelopment not rewarded" issue (ED-MB-0016 friction + a
still-needed conjunctive envelopment gate). This structurally-correct, fast wrap is the *precondition*
for rewarding envelopment; the reward calibration is the next step.
