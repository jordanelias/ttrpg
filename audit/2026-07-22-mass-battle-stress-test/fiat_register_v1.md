# Mass-Battle Fiat Register v1 — every fiat that interferes with emergence

**Status: AUDIT (adversarial, 2026-07-23). Jordan-directed: "tune everything… nothing is sacred…
hunt for all fiats that interfere with emergence."** Produced by a 9-agent adversarial sweep (one per
engine layer) cross-referenced against a live `gauge_mb.py` run (6/20 multi) and direct empirical probes.

A **fiat** = any hardcoded value, table, special-case branch, clamp/floor/cap, sentinel, deterministic
threshold, or scripted recipe that **imposes** an outcome or behavior top-down, instead of letting it
**emerge** bottom-up from the cell → subunit → army primitives. Emergence is the stated design goal
(CLAUDE.md §0/§10: "small correct primitives, composed, not a bespoke top-level special case… if you
find yourself special-casing an entity or outcome, stop — that's scripting drift"). Every entry below is
the opposite of that goal.

---

## 0b. The biggest fiat of all — the game the player actually experiences

**The strategic engine the game calls is a disguised force-ratio dice roll with emergence disabled.**
`resolve_mass_battle` (the only battle entry point the campaign layer invokes, `systems/mass_battle/sim/
massbattle.py`) runs through `_faction_to_unit`, which collapses **every** faction into a *mechanically
identical* shell — `shape=Line, tier=2, command=4, discipline=5, morale=5, single subunit` — differing
**only** by `power = int(round(faction.Mil))`. Both sides always share shape/tier/subunit-count, so the
entire emergent apparatus (formation modifiers, octagon facing, encirclement, tip-support) is a symmetric
no-op *by construction*. It runs one 18-tick skirmish (the multi-turn/multi-unit orchestrators are dead
code), ignores `terrain` entirely, and buckets the result through hardcoded 0.75/0.50/0.25 cutoffs. **Net:
troop composition, formation, tactics, and terrain currently differentiate nothing — only `Mil` + dice.**
This is the *older integer engine* slated for Stage-G retirement; the cell-level field engine below is
real but **not wired to the game**. Everything else in this register is about making the field engine
worth wiring in — but this is the headline: today, none of it reaches the player.

---

## 0. The master finding

**The engine imposes outcomes at every layer.** The historical gauge saturates (100%/0%, never banded)
not because one knob is mistuned but because a *stack* of fiats each removes emergent variance or
double-counts an effect. The live gauge (6/20) confirms it: no asymmetric matchup lands inside its
history band — every one saturates to a near-certain win or loss.

**And the ruler itself is partly broken.** Before any engine tuning is trustworthy, the measurement
harness (`gauge_mb.py`) must be de-fiated — it currently injects the single largest distortion in the
whole system (§1).

---

## 1. MEASUREMENT-INTEGRITY FIATS (the broken ruler — fix FIRST)

These live in the gauge harness, not the engine. They must be fixed before engine numbers mean anything,
or the engine will be "corrected" to compensate for a rigged measurement.

| # | Fiat | Location | Empirically confirmed effect |
|---|---|---|---|
| **M1** | **Per-cell density mismatch between deployment paths** | `gauge_mb.py` `_envelop_army`/`_refused_army` (footprint_for path) vs `make_unit` (legacy tier path) | **CONFIRMED by probe:** single-subunit opponents = **16 troops/cell** (25 cells); envelop army = **133/cell** (3 cells, 8×); refused army = **200/cell** (2 cells, 12.5×) — *at identical total troops*. Since per-cell density drives combat power, H3/H4/H5/C4/C7's "envelopment over-decisiveness" is substantially a **density artifact**, not envelopment geometry. |
| **M2** | **`footprint_for` collapses to near-minimal cells** | `geometry.py:94` `target = round(troops/concentration)`; `concentration=100` → 133 troops → 1 cell; `CELL_FLOOR=40` caps a 133-troop subunit at ≤3 cells | The composed "army" is 3 dense point-masses, not a formation. |
| **M3** | **ANCHOR_MAP center-of-mass offset** | `gauge_mb.py:39-46` | **CONFIRMED by probe:** Line COM=col 11, GappedLine COM=col 11, **Arrowhead COM=col 12** (+1). The wedge apex — whose whole purpose is to concentrate on the enemy center — lands one file off-center in *every* Arrowhead row. Prime suspect for H2 (wedge loses 25%) + mirror H9 (77.6%). |
| **M4** | **Hand-placed wing offsets bypass the engine's own frontage-aware placement** | `gauge_mb.py:169-175` (`anchor±6`), `204-207` (`anchor±4`) | Explicit `starting_position` keys make `build_army` skip ED-MB-0017's footprint-aware spacing — the harness re-introduces the exact fixed-step defect the engine was fixed to remove. Self-tagged "CALIBRATED, not historically cited." |
| **M5** | **`pin_frac`/`strong_frac` composition ratios** | `gauge_mb.py:151` (1/3), `264,289` (2/3), `196` (0.5) | Scripted force-splits baked in before the battle runs, not emergent from command/allocation. |

**Legacy tier path itself violates `CELL_FLOOR`:** a tier-3 Line is 400 troops / 25 cells = 16/cell,
*below* the CELL_FLOOR=40 the continuous path enforces. So the two paths don't just differ — one breaks
the density invariant the other respects. This is the foundational inconsistency under M1.

**FALSIFIED (intellectual honesty — A/B'd, not assumed):** M3's stated cause was tested by aligning the
Arrowhead COM to the Line (anchor 8→7, COM 12→11) and re-running H2/H9. Result: H2 got **worse** (22.5 →
10.5 decA), not better. **The +1 offset is NOT why the wedge loses.** The wedge-loses-to-line problem is a
genuine *engine shape-mechanics* issue — the frontage model (`n_eng_cols`) rewards spreading and penalizes
the wedge's concentration into fewer engaged columns, with no emergent wedge-shock/breakthrough reward to
offset it. Lesson banked: **every fix hypothesis is A/B'd before code changes** — had M3 been "fixed"
blindly it would have regressed H2. (M1/M2/M4/M5 stand; M3 is re-scoped from "deployment offset" to
"engine shape-mechanics — concentration penalized, no breakthrough reward.")

---

## 2. VARIANCE-DESTROYING FIATS (why nothing bands — everything saturates)

The dominant *engine* failure class. Two independent determinism sources stack on the self-averaging
attrition core, so a force/tactic edge converts to a near-certain outcome.

| # | Fiat | Location | Class | Why it kills emergence |
|---|---|---|---|---|
| **V1** | **Rout is a hard deterministic cliff** — `agg_morale() <= 0`, fed by fixed **50%/25% cohesion** step triggers with flat −1.0 magnitudes and a −3.0/phase cap | `units.py:1781` (`derive_rout`); `core/state.py:55-56,71` | **Zero stochastic breakpoint.** A given casualty trajectory → identical rout tick every time. Every unit in the engine breaks at *exactly* 50%/25%, no per-unit dispersion. Directly contradicts the history the DG-6 doc itself cites (du Picq; Clark 1954; Dupuy "40% rule" — breakpoints are *distributed*, not hard lines). This is the **second determinism layer** the DG-6 CEV-friction work underweighted. |
| **V2** | **`compute_degree` hard tier thresholds** (net ≥ 1×ob → Success; ≥ 2×ob & ≥3 → Overwhelming) | `resolution.py:44-48` | Converts a continuous (and, at scale, self-averaging) net-ratio into a 4-bucket step function. Once army size makes `net_A/net_B` reliably land on one side, degree — and damage — is a near-deterministic step of the force ratio. |
| **V3** | **`DAMAGE_BY_DEGREE` flat buckets** — `Partial→1`, `Failure→0` discard all pool magnitude | `config.py:158-159` | A pool of 2 and a pool of 40 landing "Partial" deal identical damage; amplifies V2's discretization. |
| **V4** | **CEV friction built, grounded, but gated OFF** | `config.py:178` `PC_FRICTION_CEV=0`; `exchange.py:129` | The one variance layer that bands force-ratio outcomes (σ=1.1, Dupuy-DLEDB-calibrated) is inert by default — so nothing counteracts V1/V2. (This is an *absence-of-mitigation*, the remedy, not a fiat itself.) |
| **V5** | **`pen` discipline penalty capped at −2.0; `max(1, floor(raw))` pool floor** | `exchange.py:87,134`; `resolution.py:37` | Resurrects near-dead pools (raw 0.02 fights = raw 0.99 → a full die), and flattens the low-discipline regime — both remove variance exactly where a unit is near collapse (where emergence matters most). |

**Root remedy:** restore *force-independent* variance at the battle scale — un-gate V4 **and** add a
**distributed rout breakpoint** (V1), the du Picq/Dupuy-grounded fix. Soften V2/V3 discretization.

---

## 3. DOUBLE-COUNTING / OVER-CONCENTRATION FIATS (why envelopment = 100%)

Multiple mechanisms independently price the *same* physical fact (attacker on flank/rear), stacking
multiplicatively.

| # | Fiat | Location | Class | Why it kills emergence |
|---|---|---|---|---|
| **D1** | **`MULTI_SIDE_SHOCK=0.5` compounds UNCAPPED on top of the octagon 2× rear multiplier** | `config.py:108`; `orchestration.py:1140-1141` | 2 sides → ×1.5 *times* the arc's ~3× rear ⇒ ~4.5×; 3 sides → ×2.0; 4 → ×2.5, no ceiling. The single biggest lever turning "enveloped and losing" into "annihilated" (H3/H4/C4/C7=100). Magnitude is authored, not derived. |
| **D2** | **Two independent flank-zone classifiers feed two independent lethality channels** | `_octagon_dmg_mod` (casualty multiplier) vs `_per_cell_angle_mod` zone → `_charge_shock_sigma` (net-success reducer) | `orchestration.py` | The octagon zone (local-centroid facing) and the wrap/pocket/roll-up zone (different sensitivity) are two *different* readings of "I'm flanked," both multiplying lethality for the same pair in the same tick. In-code "no double-count" comments only prove it *within* each function, never across them. |
| **D3** | **`OCTAGON_DMG_MULT = {GREEN:1.0, YELLOW:1.5, RED:2.0}`** — fiat magnitudes on a discretized angle | `config.py:97`; `orchestration.py:1127-1141` | The arc computation is genuinely emergent (real `acos`); the *multiplier* is a 3-bucket authored table. The base every envelopment path routes through. |
| **D4** | **`ENCIRCLEMENT_PENALTY=1` double-count** | `config.py:46` | Correctly gated OFF under `PC_OCTAGON_DMG=1` (default) — but a live landmine: flip the flag and it fires *concurrently* with the wrap/pocket/roll-up bundle. |
| **D5** | **Wrap/pocket/roll-up flat penalty bundle** — `PC_ENVELOP_MOD=-1.0`, `PC_POCKET_MOD=-1.0`, `PC_ROLLUP_*` table | `config.py:239-242`; `orchestration.py:456-468,821-879` | Hand-tuned flat magnitudes stacked on a structural geometric trigger. |
| **D6** | **`SUPPORT_WEIGHTS={1:1.0,2:0.7,3:0.5}`, floor 0.3** | `config.py:49-50`; `exchange.py:198` | Hand-authored depth-falloff (why 0.7 not 0.6?); inflates deep/wing formations' pool by a fixed schedule; every depth ≥4 collapses to one flat 0.3. Live in default C-ii. |
| **D7** | **`FREED_ATTACKER_FLANK_PENALTY=1`, `REARGUARD_PENALTY=2`** — geometry-blind flat flank penalties | `orchestration.py:1980-2107` | Pure narrative-asserted "-1D because freed & adjacent" with zero geometric check. Quarantined in `run_multi_unit_battle` (not gauge-exercised) but a live double-count landmine for Stage G. |

**Root remedy:** one encirclement owner. Reconcile D1/D2/D3 into a single flank/rear-lethality
computation; cap multi-side; make envelopment *conjunctive* (center-holds × cavalry-sufficiency ×
terrain, each <1 — Goldsworthy/Sabin) so it usually *doesn't* annihilate, matching history.

### 3b. The confirmed damage double-count (sigma channel) — a falsifiable bug

The charge-shock sigma channel double-counts the *same* flank/rear fact the octagon multiplier prices:
- `_charge_shock_sigma(unit_b, …, zone)` lowers `b_net`; `compute_degree(a_net, max(1, b_net))` then uses
  the shrunk `b_net` as A's **opposition threshold**, making it structurally easier for A to reach
  Overwhelming — *and* the same zone directly multiplies `dmg_b` via `_b_dmg_mult`. One geometric fact
  inflates damage-to-the-flanked-defender **twice**, at two uncoordinated magnitudes (`PC_SHOCK_REAR/
  FRONT = 1.6/0.15 ≈ 10.7×` vs `OCTAGON RED/GREEN = 2×`). The in-code "no double-count" guard only zeros
  the *legacy flat penalty*, not the sigma channel — it slips through. (`orchestration.py:1021-1022,
  1087,1115-1116,1131,1158`; `resolution.py:104-135`)
- **`PC_CHARGE_SIGMA=0.55` is documented as the MAX but is not the cap:** real ceiling ≈ `0.55 × 1.6 ×
  1.0 × 2.0 = 1.76` (3.2×), caught only by the *shared* `_sigma_softcap(tanh, m=1.5)` that ALL sigma
  channels funnel through — so one oversized charge-shock **saturates the shared ceiling and crowds out
  every other emergent sigma contribution** (morale, fatigue, envelopment) in that tick. This is a fiat
  ceiling actively suppressing emergence. (`resolution.py:137-138`; `orchestration.py:1086-1087`)

### 3c. Per-cell density → power: the exact mechanism behind M1

`core/attrition.py:42`: `tpc = unit.hp / unit.ncells; strength = n_eng_cols · (min(tpc, CELL_CAP) /
LANCHESTER_DENSITY_REF) / LANCHESTER_STRENGTH_REF`. **Density feeds combat power LINEARLY.** With
`LANCHESTER_DENSITY_REF=100` the pivot, a composed subunit at 133-200/cell gets a **1.3-2.0×** coefficient
while a `build_unit` opponent at 16/cell gets **0.16×** — an ~8-12× per-column swing, *purely from which
constructor built it* (`build_unit` → legacy `CELL_PATTERN_FN` tables that never consult CELL_FLOOR/CAP;
`build_army`+troops/conc → density-bounded `footprint_for`). Also found: `unit.ncells` **frozen at
construction** (the "cell merges below CELL_FLOOR" lifecycle the config advertises **does not exist**);
`PC_ENVELOP_SIGMA=0.0` **zeros the entire envelopment-refusal mechanism** after it's fully computed;
`PC_ROTATE_FLOOR`/`PC_REFILL_FLOOR` are **dead** (zero consumers); two inconsistent frontage caps
(`n_eng_cols` uncapped vs `width_term` capped at 7).

---

## 4. SCRIPTING-DRIFT FIATS (behavior assigned, not emergent)

| # | Fiat | Location | Class | Why it kills emergence |
|---|---|---|---|---|
| **S1** | **Maneuver goals are hand-authored two-phase waypoint recipes** dispatched by `'envelop' in self.instructions` | `units.py` `_envelop_goal`/`_sweep_goal`/`_kite_goal`/`_yield_goal` (~797-919) | SCRIPTED-GOAL | ~90% scripted / ~10% emergent (only the TOI collision-cap is real perception). Flanking is *assigned by name*, not discovered. Rename the instruction ⇒ a different hardcoded recipe fires. The archetypal scripting drift. |
| **S2** | **Instruction-keyed speed multiplier** — `PC_ENVELOP_SPEED_MULT=2.0` applied `if 'envelop' in instructions` | `config.py:226`; `units.py:1003-1009` | SPECIAL-CASE | A cell moves faster *because it carries a maneuver's name* — a speed bonus granted to "win the timing race," not a stat consequence. |
| **S3** | **Named-troop-type speed/charge branches** — `PC_CAVALRY_SPEED_MULT=3.0` `if troop_type in ('cavalry','mounted_archers')`; `charge_pen` `if troop_type=='cavalry': return 3` | `config.py:217`; `units.py:628,1001-1020` | SPECIAL-CASE | Behavior keyed to a type *string*, not a stat (mass/mount) that would generalize. |
| **S4** | **`cell_speed` per-shape/per-row table** — Arrowhead apex row = 2, else 1 | `geometry.py:317-327` | FIAT-MAGNITUDE | Two identical cells move at different pre-baked rates purely by formation label + row index. |
| **S5** | **`_envelop_committed` latch + "+2" clearance literals** | `units.py:445-451,810-843` | SPECIAL-CASE | A sticky bit bolted on to stop the scripted goal oscillating — the fix for scripting jitter is *more* scripting. |

**Root remedy (largest, last):** replace scripted goals with per-cell local steering — each cell steers
by local force density / flank exposure / threat facing; flanking becomes the *statistical outcome* of
many cells preferring open flanks, not a named macro. Retire instruction-keyed speed.

---

## 5. SHAPE / ENTITY SPECIAL-CASE FIATS

| # | Fiat | Location | Why it kills emergence |
|---|---|---|---|
| **E1** | **`MIN_DISCIPLINE` keyed by shape name** (Line:1, Arrowhead:4, GappedLine:5, Column:3) | `config.py:79-85` | Directly contradicts the doctrine stated 3 lines above it ("formations grant NO flat per-shape bonuses… a SHAPE, not a bonus carrier"). This table *is* that carrier — a wedge drifts to Line if disc<4, degrading faster than a Line by fiat. |
| **E2** | **`TROOP_TYPE_DENSITY_CAP` / `TROOP_TYPE_ROLES` / `ROLE_SPEC` keyed by literal name** (incl. `knights_templar`) | `config.py:36-38,316-349` | Density/role/behavior looked up by troop-type string — the purest "special-case a named entity," rather than derived from that type's own stat record. |
| **E3** | **Per-shape aspect/tip-angle tables** — `LINE_ASPECT=1.4`, Arrowhead fixed 90° tip, GappedLine fixed 1:1 | `geometry.py:64-83`; `config.py:45` | Each shape's silhouette (frontage/depth trade-off — exactly what H2/H7/H8 measure) is a hand-picked constant, not derived. |
| **E4** | **`role_at_contact` shape-name branch** | `units.py:1476-1490` | Combat role from shape label, not live geometry. |

---

## 6. PACING / CALIBRATED-TO-OUTCOME FIATS

Constants explicitly reverse-engineered to hit a *desired result* — "calibrated-but-imposed is still a
fiat."

| # | Fiat | Location | The tell |
|---|---|---|---|
| **P1** | **`CASUALTY_SCALE`** | `config.py:57` | Self-labeled "TUNING": picked so "even units take ~3 turns to resolve (playable)" — a pacing target, not a weapon/armor derivation. |
| **P2** | **`PC_CHARGE_RECOIL=6`** | `config.py:231` | Calibrated to reproduce "~75% braced-wall win" — the target result decided first, constant fitted after. **And it's currently failing** (gauge C2/C6 = 60% cav win, NOT repelled). |
| **P3** | **Charge-shock coefficient table** — `PC_SHOCK_FRONT=0.15`, `PC_SHOCK_REAR=1.6` (10.7× baked-in), +6 more | `config.py:208-215` | An entire "physics" (charge shock) assembled from 8 independently hand-set multipliers. |
| **P4** | **`MORALE_SIBLING_PULL=0.15`, `MORALE_EROSION_DAMP=0.7`, `MORALE_SIGMA_SCALE=0.8`, `SIGMA_PER_D=0.2`** | `config.py:182-184` | Self-admitted "no existing primitive to derive the exact magnitude." |

---

## 7. Gauge failure → fiat cross-reference (live n=60 multi)

| Row | Result | Band | Verdict | Dominant fiats |
|---|---|---|---|---|
| H2 | 25.0 | 48-62 | wedge LOSES | M3 (COM offset), E1/E3/S4 (shape fiats) |
| H3/H4 | 100 | 55-72/45-62 | envelop WIN-OUT | **M1 (density 8×)**, D1/D2/D3, V1/V2 |
| H5 | 30 | 48-62 | refused LOSES | M1 (density 12.5×), D1/D2 |
| H7/H8 | 68.3 | 48-62/50-65 | gapped over-wins | D6 (support weights), E3 |
| H9 | 77.6 | 38-52 | line beats wedge (mirror of H2) | M3, E1/E3 |
| H10/H11 | 0 | 28-45/38-55 | mirror of H3/H4 | M1, D1/D2, V1 |
| R3 | draw 100% | 42-58 | ranged mirror never resolves | (ranged-hold stalemate — separate bug) |
| C1 | 22 | 35-55 | cav loses too hard | P2/P3 (charge underperforms) |
| C2/C6 | 60 rawA | 0-30 | braced NOT-REPELLED | **P2 (recoil fails)** |
| C4/C7 | 100 | 75-95/65-100 | cav envelop over | M1, D1/D2 |
| OK | H1 46.7, H6 53.4, R1 3.3, C3 46.7, C5 70 | | pass | (mirrors pass by symmetry, not banding) |

Note: H1/C3 "pass" only because they are mirrors centered at 50 — they pass by *symmetry*, not because
the engine bands. No asymmetric matchup bands.

---

## 8. Emergence-restoration plan (sequenced; each step A/B'd vs the gauge AND the independent Dupuy curve)

1. **Measurement integrity (§1):** unify deployment density so only geometry differs; align COM. Re-run
   the gauge on an honest ruler — several "failures" may evaporate before any engine change.
2. **Variance layers (§2):** un-gate CEV friction (V4) + **new distributed rout breakpoint** (V1);
   soften compute_degree/DAMAGE_BY_DEGREE (V2/V3). Turns saturation into bands.
3. **De-double-count encirclement (§3):** one flank/rear owner; cap multi-side (D1/D2); conjunctive
   envelopment gate (Goldsworthy/Sabin).
4. **Brace-repel (P2)** + **cavalry charge (C1)** grounded fixes.
5. **De-fiat shape behavior (§5):** derive MIN_DISCIPLINE / cell_speed / aspect from geometry.
6. **Emergent maneuvers (§4):** perception-driven local steering — the largest, last.

**North star:** replace fiats with grounded emergent primitives; calibrate magnitudes to **independent
history** (Dupuy DLEDB, Sabin bands), never to the 20 gauge rows — the gauge must stay an independent
validation surface, not a training target. "Nothing is sacred" applies to the fiats and the byte-exact
goldens (a regression oracle), NOT to overfitting the validator.

---

## 9. The integer strategic engine (`systems/mass_battle/sim/`) — the live game path

Separate, older engine; what the campaign actually calls today. Its fiats (ranked):

| # | Fiat | Location | Effect |
|---|---|---|---|
| **G1** | **`_faction_to_unit` collapses every faction to identical Line/tier-2 shells** (cmd4/disc5/morale5), differing only by `power=int(Mil)` | `massbattle.py:1867-1895` | The load-bearing fiat: neutralizes ALL emergent formation/geometry mechanics for every strategic battle. §0b. |
| **G2** | **Single 18-tick skirmish**; `run_multi_turn_battle`/`run_multi_unit_battle` are dead code | `massbattle.py:1824-1831` | The richer paths are bypassed at the only call site. |
| **G3** | **Flat degree buckets 0.75/0.50/0.25** | `massbattle.py:1836-1845` | Narrative labels via hardcoded percentages. |
| **G4** | **`terrain=None` ignored** | `massbattle.py:1801`; `faction_action.py:354` | A named primitive (troop/tactic/**terrain**) contributes nothing. |
| **G5** | **`_GarrisonStub Mil=1.5`** magic garrison; **`LETHALITY_SCALE=1.25`** pacing multiplier | `massbattle.py:1820,138` | Outcome-calibrated constants. |
| **G6** | **`FACTION_TACTIC_CARD_POOL_MODIFIERS={}`** empty stub (blocked); **`altonian_reinforcements`** `NotImplementedError` named-faction lock | `tactic_cards.py:33`; `altonian_reinforcements.py:20` | Inert today, but the *reserved shapes* are lookup-table/named-entity fiats waiting to be filled. |

This engine is slated for Stage-G retirement in favor of the field engine — but until that lands, the
field-engine de-fiat work below does **not reach the game**. Sequencing note: Stage G (wire the field
engine into `resolve_mass_battle`) is the multiplier on everything else here.

---

## 10. A/B measurements (hypotheses tested, not assumed)

| Hypothesis | Test | Result | Verdict |
|---|---|---|---|
| M3: Arrowhead COM +1 offset causes H2 wedge-loss | align COM (anchor 8→7), re-run H2/H9 n=40 | H2 22.5→**10.5** (worse) | **FALSIFIED** — re-scoped to engine shape-mechanics |
| M1: per-cell density mismatch drives envelopment=100% | envelop vs density-matched line (16→67/cell), n=40 | H3 **100.0 → 0.0** decA | **CONFIRMED** — density is the dominant lever; flipping opponent density inverts the outcome entirely |

**M1 confirmed + a subtlety:** with the opponent at 16/cell the envelop army wins 100%; at 67/cell it wins
**0%**. So (a) the envelopment rows are measuring density, not envelopment; and (b) the density artifact
was *masking* a real compositional weakness — the envelop army (3 small dense subunits) is actually
*weaker* than a comparable single body once density is fair. The fix is therefore **not** merely "equalize
density" — it is "equalize density **and** make the envelopment geometry deliver its historical benefit"
(else H3/H4 will swing from 100% to ~0%, still out of band, just the other way). This is why measurement
integrity must precede engine tuning: only on a fair ruler can we see whether the envelopment *mechanic*
works at all.
