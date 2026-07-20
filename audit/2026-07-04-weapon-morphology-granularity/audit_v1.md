# Weapon-morphology granularity audit — more granular morphological characteristics for fidelity and variability

## Status: RATIFIED-by-merge (PR #74, ED-1094) · T1–T5 SUPERSEDED-IN-PART

> **Superseded-in-part (2026-07-04):** this audit's analysis (P1–P4, the gap ranking, the anti-fabrication
> discipline) stands and is ratified by the merge of PR #74. Its **T1–T5 tranche plan is reconciled into the
> unified PC-lane sequence in `consolidation_v1.md` §4** (Fable-adjudicated against the post-R2 tree, which
> re-scoped P4's guard-axis rename — F2). Implement from `consolidation_v1.md`; read this doc for the P1–P4
> primitive rationale it supplies. (Original status line below, kept as provenance.)
>
> _Original: PROPOSED (Jordan-vetoable throughout; nothing here edits canon)._

**Date:** 2026-07-04 · **Lane:** PC (personal combat) · **Authored at the Fable synthesis tier** (CLAUDE.md §10
canonical-contract authorship node). ED-PC IDs are **not yet allocated** — see §8's allocation step; this doc
deliberately cites no specific new ED numbers (`references/id_reservations.yaml` protocol: read `next_free`,
allocate, bump, co-commit — never fabricate).

**Question answered:** how do we extend the bottom-up weapon-morphology model — located parts + whole-weapon
geometry scalars in `designs/scene/combat_engine_v1/weapons.py`, derived through `weapon_physics.py` /
`geometry.py` — with more granular morphological characteristics, improving *fidelity* (the model matches real
weapons) and *variability* (the design space expresses more distinct viable weapons), **without violating
aggregate-based emergence** (behaviour rises from primitives, never from a per-weapon behaviour table).

**Triggering evidence (this session's silhouette-reconstruction exercise,** scratchpad `render_weapons.py`**):**
a renderer reading only the real primitives could faithfully reconstruct length, part positions, masses,
curvature, and the derived point of balance for all 53 weapons — but had to *invent* two things the model does
not store: (1) blade transverse width, stylized as `mass ÷ extent × edge_keenness`; and (2) edge symmetry
(single- vs double-edged), hand-authored as a 21-weapon `SINGLE_EDGE` name set — **exactly the per-weapon-table
shape this model exists to abolish.** Anything a faithful renderer must hand-author is, by construction, a
missing primitive.

**Verdict:** the model is structurally sound and needs no re-architecture. The located-part mass model
(Phase B, 2026-07-02) already carries position/extent/mass at part granularity; what is missing is a small set
of **transverse and edge-topology facts** that today are either absent (edge symmetry, blade width/thickness)
or smuggled in through fiat 0–1 scalars (`cross_section` standing in for a computable bending stiffness). Four
primitive additions (P1–P4 below), landed in the order given in §8, close the renderer's two invented
quantities, convert one fiat scalar into a derived-and-checked quantity, retire one residual name-keyed
behaviour table (`HALFSWORD_FORM`), and open a genuinely continuous design space for procedural/player-authored
weapons — all with **"absent ⇒ identity"** defaults so un-migrated records are byte-identical.

---

## 1. Inventory — the current morphology primitive surface

### 1.1 Stored primitives (per record, `weapons.py` schema)

| Primitive | Type / units | Axis semantics | Consumed by (function → derived quantity) |
|---|---|---|---|
| `elements[] {x_m, extent_m, mass_kg}` | m, m, kg | `x_m` along working-hand axis (x=0 at hand, + toward tip); `extent_m` **axial** (length along the axis) | `weapon_physics._all_parts` → `derive()` (PoB, MoI, `m_head`, static moment); `heft()` (= m_head × PoB_frac / anchor); `at_grip()` (re-pivoted I_g/S_g) |
| `elements[].edge_undulation {amplitude_mm, period_mm}` | mm | edge-normal | `edge_vibration()` → `systems.bind_sigma` tactile degrade, `init_steal_factor` (1 weapon: flamberge; absent ⇒ 0 ⇒ identity) |
| `guards[] {x_m, mass_kg, extent_m, [dual_role_element]}` | m, kg, m | `extent_m` **transverse** (quillon span / bar length) — ⚠ same field name as elements', different axis (§4 G4) | `_all_parts` (MoI/PoB); `_guard_catch_raw` → `hand_guard()` (proximity-decayed) and `blade_guard()` (position-free), baked over the record literals; → `defense_affinities.parry/wind`, `systems.mode_sigma`, `bind_sigma` catch |
| `haft {x_m, mass_kg, extent_m}` | m, kg, m | axial | `_all_parts`; `grip_len`-adjacent gather physics |
| `pommel` / `butt {x_m, mass_kg}` | m, kg | point mass | `_all_parts` (counterweight → PoB/MoI) |
| `adornments[] {count, extent_m}` | — , m | — | `distraction()` → `systems.legibility` (3 weapons; absent ⇒ 0 ⇒ identity) |
| `mass, head_len, grip_len, hands` | kg, length-units (`UNIT_M`=0.30 m), 1/2 | axial | `reach_base`, `energy_credit`, `leverage`, `grip_choke_max`/`_gather_len`, `str_demand`, fallback mass model |
| `head` token (+ `mode_elements[] {head, geometry}`) | categorical | — | `systems._mode_elements` → `element_afforded`/`afforded_heads`/`select_mode`; `core.HEAD_MODE`/`DELIVERY` |
| `wclass, hilt, clinch, reach_adj` | categorical / scalar | — | `_gather_len` (grippability), `HILT_CATCH_MULT`, clinch affinity, reach residual |

### 1.2 Whole-weapon geometry scalars (`geometry.bake`, per weapon and per mode-element)

| Scalar | Fiat 0–1 meaning | Derives (geometry.py) | Downstream |
|---|---|---|---|
| `curvature` | straight → strongly curved | `cut_factor` (draw-cut gain), `thrust_factor` (point-offset penalty), `can_halfsword_thrust` | cut/thrust coefficients; select_mode; legibility (via mode) |
| `point_concentration` | spatulate → needle | `gap_precision`, `thrust_factor` | `w['gap']` → `core.coupling` gap game, `adef_cap`; `_recovery_mode_commitment` swing/thrust blend; `lunge_quality` |
| `cross_section` | whippy → rigid | `gap_precision` (rigidity gate), `thrust_factor` | `defense_affinities` rigidity (`0.30+0.70·cs`) → wind |
| `edge_keenness` | blunt → razor | `cut_factor` | cut coefficient → `element_afforded`/`adef_cap` |
| `strike_concentration` | broad face → beak | `percussion_concentration` | `puncture_pressure`, `armour_defeat_mode` |

### 1.3 Baseline expressive range (what the current surface CAN already say)

Axial mass distribution at part granularity (any PoB/MoI/heft/agility/recovery ordering is expressible);
per-element fight modes for composites (8 weapons); guard catch as located hardware; grip as a continuous
position (`at_grip`); one edge-texture fact (undulation) and one visual-clutter fact (adornments); five
whole-weapon shape scalars driving cut/thrust/gap/percussion coefficients. That is a real, validated
substrate — the heft acceptance ordering (spear < arming < longsword < greatsword) and the poleaxe
spike-vs-plate selection both emerge from it.

**What it cannot say** is anything **transverse or topological about the blade itself**: how broad, how thick,
tapering how, edged on which side(s). Those facts are currently either invisible or impersonated by the fiat
scalars — which is precisely where the renderer had to start inventing.

---

## 2. Gap analysis — missing morphological degrees of freedom, ranked

Ranked by (mechanical consequence × breadth of weapons mis-distinguished × what it unlocks beyond the roster).

### G1 — Edge topology: single/double/edgeless + false-edge fraction  *(rank 1: behavioural, cheap, zero-risk)*

**Absent entirely.** No record field, no geometry scalar, no consumer. Today it is only *correlated* with
`curvature` (curved ≈ single-edged in the roster), and the correlation demonstrably breaks **inside the
current 53**: falchion (single-edged, `curvature=0.15` — nearly straight), flamberge (double-edged, wavy),
estoc (edgeless, expressed only as `edge_keenness=0.05`), nandao/changdao (single, modest curvature), and it
would break instantly on a messer (single, straight) or spadroon. Edgelessness is *partially* expressible via
`edge_keenness≈0` (estoc/stiletto/rondel do this), but 1-vs-2 edges is not expressible at all.

**Real mechanical consequences it fails to model:**
- **Cut-line availability.** A double edge (or a sharpened false edge) affords back-edge cuts — reversals and
  line-changes off the same hand position — which raises the attack-line entropy a defender must read. A
  single-edged blade telegraphs its cutting side.
- **The spine as equipment.** A single-edged blade carries a rigid, non-cutting bearing surface (mune / back)
  used for parries, binds, and leverage without edge-on-edge damage or edge instability — a real, documented
  practice (mune-uke; German flat/short-edge bind mechanics distinguish which surface bears).
- **Thrust trueness.** A single-edged profile puts the point off the mid-axis (chisel/kissaki geometry): a
  straight falchion still thrusts less true than a jian of the same length — today only curvature can express
  point offset, and the falchion's is nearly zero.
- **Section form.** Wedge (single) vs lens/diamond (double) distribute stiffness and mass differently across
  the width — currently baked invisibly into the fiat `cross_section`.

**Variability unlocked:** a third-ish discrete axis (0/1/2 edges) × a continuous false-edge fraction across
every bladed weapon — the single cheapest multiplier on roster distinctiveness, and mandatory for any
procedural blade generator that wants falchion-vs-arming to be a *choice* rather than a name.

### G2 — Transverse blade geometry: width & thickness profile (+ section fill)  *(rank 2: the fidelity keystone)*

**Absent.** `extent_m` is axial only; a blade's breadth and thickness exist nowhere. The renderer's width is
a labelled stylization (`mass ÷ extent × edge_keenness`); an ox-tongue partisan blade and a narrow estoc
blade of equal mass/length/position are **indistinguishable** to the mass model, and are separated only by
hand-set `cross_section`/`point_concentration` scalars asserting what geometry should be deriving.

**Real weapons it fails to distinguish:** partisan (broad thin cutter) vs bear_spear (narrow thick thruster)
at similar head masses; rapier (narrow, deep-section, still whippy at length) vs sabre (broad, thin); the
cinquedea's defining five-finger breadth is literally invisible; distal taper (a longsword's blade halving in
thickness toward the tip) is not representable independent of `point_concentration`, though it — not the
point — is what governs where stiffness dies and how the last third of the blade behaves in the bind.

**What it unlocks:**
- **Derive rigidity instead of asserting it.** Bending stiffness goes as `E·I/L³` with `I ≈ k·w·t³/12` — with
  width/thickness stored, `cross_section` becomes a **derived-and-checked** quantity (the same
  authored→derived shift `hand_guard`/`blade_guard` already made in Phase B4), and "whippy rapier vs stiff
  estoc" becomes physics, not adjective.
- **A second mass-closure audit loop.** `ρ_steel · fill · mean(w·t) · extent ≈ mass_kg` is checkable per
  element, exactly like Phase-0's ±10% whole-weapon mass budget — a fabricated width cannot hide.
- **Faithful rendering / Godot art pipeline.** Silhouettes and eventual in-game weapon meshes read real
  breadth instead of a stylization.
- **True variability axis.** Same mass, same length: broad-thin vs narrow-thick becomes a live design
  trade-off (cut presence & light structure vs thrust stiffness) for procedural and player-authored weapons —
  today that trade-off literally cannot be expressed.

### G3 — Grippable-element affordance (ricasso / half-sword) — retires a residual name table  *(rank 3)*

`HALFSWORD_FORM = {'longsword': …, 'estoc': …}` in `weapons.py` is a **name-keyed behaviour whitelist** — the
exact shape the primitive-law forbids, surviving because half-sword affordance has no primitive to derive
from. The physical fact is: *does the weapon offer a safe forward gripping zone* (ricasso, blunt forte,
documented hand-on-blade practice)? The flamberge record already stores a ricasso **as a mass element** but
the engine cannot see it as grippable; `geometry.can_halfsword_thrust` exists but only gates, never grants.
Failure case inside the roster: flamberge (ricasso + Parierhaken, straight, `point_concentration=0.62` —
historically half-sworded as a two-hander) can never adopt a half-sword form; nor could any new
player-authored greatsword without editing engine data.

### G4 — Guard geometry beyond one ambiguous scalar  *(rank 4: hygiene + one honest derivation)*

Two sub-issues: **(a) axis ambiguity** — `guards[].extent_m` means *transverse span* while `elements[].extent_m`
means *axial length*, one field name with two meanings. Numerically this is nearly immaterial for MoI (for a
thin rod swung about the perpendicular hand-axis, the own-centre term is `m·L²/12` for both orientations;
guard masses ~0.1 kg make the residual error ≲2×10⁻⁴ kg·m²), but it is a semantic trap for every exporter,
renderer, and future derivation that needs to know *which way the hardware points*. **(b) form flattening** —
`HILT_CATCH_MULT {'compound': 3.0}` is a fiat multiplier standing in for real coverage geometry (a basket's
cup depth and wrap vs a bare cross of equal bar length). Real weapons under-distinguished: main_gauche's
shell-and-ring complex vs szabla's knucklebow; a swept hilt vs a full basket (not yet in roster).

### G5 — Flexibility / whippiness as a first-class derived quantity  *(rank 5: pure payoff of G2, no new field)*

Today whippiness is only the low end of fiat `cross_section`. With G2 stored, flexibility derives; beyond
replacing the scalar, it opens later refinements (thrust energy lost to flex on deep lunges, bind compliance)
**without any further schema change**. Listed separately so the plan is explicit that no new stored primitive
is needed — G5 must never become an independent fiat scalar.

### G6 — Distal taper independent of `point_concentration`  *(folded into G2)*

`width_tip/width_base` and `thickness_tip/thickness_base` ARE the distal/profile taper; G2's fields carry it.
Noted separately only to flag the double-count hazard: `point_concentration` must remain *tip force-area*
(the last few cm), while taper governs *stiffness/mass distribution along the blade* — two different physical
facts that today share one scalar's duties.

**Judged NOT load-bearing now:** grip section shape (round/oval — negligible consumer), blade balance-vs-width
independence (already achieved: mass is located independently of any width), tip profile curves beyond
concentration + taper, wood species of haft (mass already located; density constants exist).

---

## 3. Proposed primitives

All four follow the established landing pattern (Phase B5's `adornments`/`edge_undulation`): **absent field ⇒
every new derivation returns its identity value ⇒ un-migrated records byte-identical.** All are *physical
facts a museum caliper or a treatise can attest*, S1/S2/S3-gradeable under the Phase-0 discipline — never a
behaviour dial. No proposed constant below is asserted as canonical: each is `[SIM-CALIBRATE]` (fit in a
balance pass) or `[FIAT]`-labelled with its basis; example magnitudes are **illustrative only**.

### P1 — `elements[].edges = dict(sides, false_edge_frac)`  *(closes G1)*

| Field | Type / range | Physical meaning | Grounding |
|---|---|---|---|
| `sides` | int ∈ {0,1,2} | count of sharpened longitudinal boundaries (0 = edgeless estoc/rondel/stiletto; 1 = single; 2 = double) | countable on any specimen or period illustration — S1-grade for essentially the whole roster |
| `false_edge_frac` | float ∈ [0,1] | fraction of the spine sharpened, measured from the tip back (sabre yelman ~0.2–0.3 **illustrative**; 0 for a plain back) | measurable on specimens; attested in cutting treatises |

**Identity default:** key absent ⇒ all three consumers below contribute exactly 0 / ×1.0. (Explicitly NOT
"default sides=2": absence means *unspecified*, and unspecified must change nothing.)

**Derivations (new, additive — none modifies an existing formula's existing terms):**

1. **Cut-line entropy → legibility.** New pure `WP.edge_lines(w)` ∈ [0,1]: max over blade elements of
   `(sides==2) ? 1.0 : false_edge_frac` (0 when `edges` absent, 0 for `sides<=1` plain-backed, 0 for
   edgeless). Consumed as `legib -= LEGIB_EDGELINE_K * edge_lines(w)` in `systems.legibility` — structurally
   identical to the existing `LEGIB_DISTRACT_K` wiring. A double edge's line-change repertoire makes intent
   harder to read; gain `[SIM-CALIBRATE]`, deliberately small (same restraint as `DISTRACT_K`), and the
   legibility floor must be audited since distraction + edge-lines + thrust can now stack.
2. **Spine-parry / bind bearing-surface credit → wind (and optionally parry).** New pure `WP.has_spine(w)`
   (1 iff any blade element has `sides==1` and `false_edge_frac < ~0.5`, else 0; 0 when absent). Consumed as
   a `(1 + SPINE_WIND_K · has_spine)` multiplier inside `defense_affinities.wind` — the physical fact is a
   rigid non-cutting bearing surface for static contact (mune-uke), which is a *contact-surface* fact, NOT a
   section-stiffness fact (see double-count audit). `[SIM-CALIBRATE]`. Note the honest asymmetry: this lands
   as a bonus-only term for attested single edges, so the roster-wide wind band shifts slightly up for
   singles until the Phase-C-style renormalisation pass (§5) re-centres the `_band` window — same
   renormalise-after pattern as the agility re-anchor.
3. **Thrust-trueness offset (interlocks with P2; deferred until P2 lands).** A single-edged point rides off
   the mid-axis by ~`width_tip/2`. Wire as a small additive offset penalty in `geometry.thrust_factor` **only
   where curvature does not already carry the offset** (the falchion case: straight AND single). Deferred:
   without P2's `width_tip` there is no physical operand, and a fiat stand-in would be exactly the smuggled
   scalar this model forbids.

**Validation (CI-shaped, behaviour-free):** `sides==0` ⇒ `edge_keenness ≤ 0.1` (an edgeless blade cannot be
keen — estoc 0.05, rondel 0.05, stiletto 0.02, misericorde 0.1 all already conform); `false_edge_frac>0` ⇒
`sides==1`. Add to the co-file/record validators, report-only first.

**Double-count audit:** does NOT touch `cut_factor` (a second edge does not make a single swing cut better —
`edge_keenness` keeps that duty, and modifying cut would double-count keenness). Does NOT touch
`cross_section` (wedge-vs-lens stiffness is P2/G5's derived-rigidity job; if P1's spine credit encoded
stiffness too, single edges would get counted twice once P2 lands — hence spine credit is scoped to
*bearing-surface* only, documented in the function docstring). Independent of `edge_vibration` (texture, not
topology) and `distraction` (visual clutter) — all three legibility/bind modifiers remain separately
falsifiable.

**Emergence check:** the renderer's hand-authored 21-name `SINGLE_EDGE` set is replaced by a per-record
physical fact; no consumer branches on weapon name; a new weapon gets cut-lines/spine behaviour by declaring
its topology, not by being enrolled in a table.

### P2 — `elements[].profile = dict(width_base_m, width_tip_m, thickness_base_m, thickness_tip_m, section_fill)`  *(closes G2/G6, enables G5)*

| Field | Type / units | Physical meaning | Grounding |
|---|---|---|---|
| `width_base_m` / `width_tip_m` | m | blade breadth at the element's base / at the start of the point | caliper-measurable; ubiquitously published for museum specimens (S1/S2) |
| `thickness_base_m` / `thickness_tip_m` | m | spine/section thickness at base / near tip (distal taper) | published for many specimens (Oakeshott records, HEMA specimen surveys); S2 typical, S3 by typology |
| `section_fill` | float ∈ (0,1] | steel-area fraction of the `w×t` bounding box at a representative station | **computable from the section shape, not fiat**: a diamond section is exactly 0.5 by geometry; a fullered or hollow-ground section's fill follows from its drawing. Grade like any Phase-0 fact. |

**Identity default:** key absent ⇒ (a) the mass model is untouched (mass_kg stays authoritative — profile
NEVER re-derives mass); (b) `cross_section` remains the operative rigidity source; (c) renderer falls back to
its labelled stylization. Nothing changes until a record opts in.

**Derivations, deliberately staged (this is the primitive with real balance surface):**

- **Stage P2-a (data + closure only, zero engine consumption).** Populate profiles via a Phase-0-style
  specimen campaign (per-cluster fan-out, S-graded, adversarially checked — reuse the Phase-0 report format).
  Add a **report-only** closure check: `ρ_iron(7860, existing sourced constant) · fill · mean_station(w·t) ·
  extent_m` vs `mass_kg`, tolerance band generous (blades taper in both axes and carry tangs; propose ±20%
  report-only until the estimator is validated against the best-S1 specimens — band `[SIM-CALIBRATE]`, and
  its final value must be justified from the S1 subset, not asserted). This is the anti-fabrication loop:
  **a width that closes against an independently sourced mass cannot be invented freely.**
- **Stage P2-b (parity report, still zero behaviour change).** Pure `WP.rigidity_derived(w)`:
  `I ≈ k_shape · w_mid · t_mid³ / 12` with `w_mid,t_mid` linearly interpolated at mid-element, stiffness
  `∝ E·I / extent³`, normalised to the roster. `k_shape` from `section_fill` (the cubic-thickness dominance
  means fullers cost little stiffness while costing mass — that asymmetry is the *point* of a fuller, and it
  falls out of the formula rather than being asserted). Emit a standing parity table: derived rank vs fiat
  `cross_section` rank, ED-1050-style (**never** hand-correct the fiat scalar to match — disagreements are
  findings). Falsifiable expectation at this stage: estoc stiffest; shamshir near the floor; rapier's
  long-blade whippiness reproduced *despite* its deep section (the `/L³` term — this is the case fiat
  `cross_section=0.52` currently encodes by assertion).
- **Stage P2-c (the swap — Jordan-gated re-baseline).** `geometry.bake` sources `cross_section` from
  `rigidity_derived` where a profile exists (fiat fallback where not). This moves `gap_precision` →
  `w['gap']` → `adef_cap`/`core.coupling`'s **armour-defeat tier list** — the single sharpest balance surface
  in the engine (§5). Must ride with or behind the already-pending Phase-C percussion recalibration, never
  ahead of it.
- **Renderer/Godot:** width becomes faithful immediately at P2-a (fidelity win with zero engine risk).

**Double-count audit:** profile does not feed PoB/MoI/heft (mass stays the located-part source — width is a
*shape* fact; letting it also scale mass would double-count against `mass_kg`). `point_concentration` keeps
tip force-area duty; `width_tip` informs the *thrust-trueness offset* (P1-3) and rendering, not `gap` directly.
`edge_keenness` (grind sharpness) stays independent of wedge angle for now; folding `t/w` into cut physics is
flagged as a **candidate refinement only** — it would need its own parity stage because keenness was
calibrated to reproduce the §4-grounded cut tier-list.

### P3 — `elements[].grippable = True`  *(closes G3)*

**Field:** boolean on a blade/haft element whose zone is attested as a safe forward grip (ricasso; documented
hand-on-blade practice — gauntleted half-swording is attested for sharp longsword blades, so this is an
*attested-practice* fact, S-graded from treatises, not merely "is it blunt").

**Identity default:** absent ⇒ not grippable ⇒ nothing changes.

**Derivations:**
1. **Half-sword affordance becomes emergent.** `affords_halfsword(w)` = (∃ grippable forward element) ∧
   `geometry.can_halfsword_thrust(curvature, point_concentration)`. The wrapper's form-switch consults this
   predicate; **`HALFSWORD_FORM`/`HALFSWORD_BASE` retire as behaviour gates** (the *derived form records*
   — the shifted-origin part lists — remain data, now generated/validated rather than whitelist-keyed).
   Acceptance: on the un-extended roster the derived set must equal exactly {longsword, estoc} — i.e. land
   with only those records marked, byte-identical behaviour; **whether flamberge's attested ricasso then
   grants it a half-sword form is a Jordan roster decision, surfaced loudly, never auto-granted.**
2. **Gather length honesty.** `_gather_len` currently grants forward regrip by `wclass=='hafted_tip'`
   wholesale; a grippable element lets a future refinement read *which zones* a hand may occupy instead of a
   class token. Flagged as follow-up, not wired in the first pass (grip physics is freshly calibrated; do not
   perturb it in the same tranche).

**Emergence check:** removes the model's last name-keyed weapon-behaviour mapping in `weapons.py`.

### P4 — Guard axis disambiguation + coverage depth  *(closes G4)*

**Fields:** `guards[].span_m` (transverse bar/ring span — what `extent_m` currently means for guards) and
optional `guards[].depth_m` (axial coverage length of a cup/basket/shell). Migration: mechanical rename
`extent_m→span_m` on guard entries (values unchanged — MoI/PoB/catch sums numerically identical; keep a
one-release compatibility read of `extent_m` with a deprecation note so external readers don't silently
break). `depth_m` default 0 ⇒ identity.

**Derivation (second pass, Jordan-gated):** `hand_guard` coverage from `span_m × f(depth_m)` instead of
`HILT_CATCH_MULT['compound']=3.0` — the fiat multiplier becomes a derived solid-coverage fact (the same
authored→derived shift as Phase B4 itself). Parity-report first against the current baked `hand_guard`
values; the multiplier retires only when the derived ranking reproduces the calibrated one. Constants
`[SIM-CALIBRATE]`.

**Double-count audit:** none — same physical quantities, better-typed; first pass is a pure schema fix.

---

## 4. Mechanical wiring map (primitive → engine effect → recalibration exposure)

| Primitive | Feeds (stage/function) | Emergent behaviour | Recalibration / risk |
|---|---|---|---|
| P1 `edges.sides/false_edge_frac` | NEW `WP.edge_lines` → `systems.legibility`; NEW `WP.has_spine` → `defense_affinities.wind` | double/false edges read harder (feint/line-change richness); single edges wind/parry on the spine with a stable bearing surface; falchion ≠ arming beyond scalars | LOW. Additive terms, `[SIM-CALIBRATE]` gains start small; wind `_band` window re-centre after (same pattern as the dodge/parry renormalisation); audit stacked legibility floor |
| P1-3 thrust-trueness (needs P2) | `geometry.thrust_factor` offset term | straight single-edged thrust less true (falchion, messer-class) without abusing curvature | MEDIUM. Touches baked `thrust`; gate on P2; verify no double-count with the curvature penalty on curved singles |
| P2-a profile data + closure | CI report only; renderer | faithful widths; fabricated geometry becomes detectable | NONE (no engine read) |
| P2-b `rigidity_derived` | standing parity report vs fiat `cross_section` | whippy-vs-stiff becomes checkable physics | NONE (report-only) |
| P2-c cross_section swap | `geometry.bake` → `gap_precision`/`thrust_factor` → `w['gap']` → `adef_cap`, `core.coupling` gap game; `defense_affinities` rigidity | armour-defeat and wind emerge from measured sections | **HIGH — the key balance risk.** `w['gap']` drives the plate-defeat tier list and `select_mode`'s spike-vs-hammer choices; `ADEF_THRESHOLD`/`GAP_EXPOSURE` were fit to fiat values. Sequence strictly behind Phase-C percussion recalibration; expect deliberate red tests, Phase-C-style, never per-weapon fudges |
| P3 `grippable` | NEW `affords_halfsword` → wrapper form-switch (replaces `HALFSWORD_FORM` gate) | half-sword affordance from morphology; roster-extension (flamberge?) becomes a data decision | LOW at parity (derived set == current set); any *expansion* is a Jordan call with real balance effect (a new anti-plate form) |
| P4 `span_m`/`depth_m` | schema first; later `hand_guard` coverage replaces `HILT_CATCH_MULT` | basket-vs-cross protection from measured coverage | LOW (rename), MEDIUM (multiplier retirement — parity-gated like B4) |

**Oracle/port note (CLAUDE.md §6/§7):** `combat_engine_v1` Python is the oracle for the GDScript port. Every
primitive here lands oracle-side first; after ratification the affected exports (`weapon_resource.gd`,
`strike_module.gd`, `combat_config.gd`) are **re-exported from the oracle** — never port-side edits (the
ED-1050 rule). None of this work should touch the port before P-stage ratification.

---

## 5. Fidelity vs variability ledger

| Item | Fidelity gain (matches real weapons better) | Variability gain (expresses more distinct weapons) |
|---|---|---|
| P1 edges | falchion/estoc/katana/flamberge stop being scalar-coincidences; renderer's `SINGLE_EDGE` table dies | 3 topology states × continuous false-edge over every bladed record; a whole procedural axis |
| P2 profile | silhouettes/meshes faithful; rigidity measured not asserted; a second closure audit catches fabrication | broad-thin vs narrow-thick at equal mass — a trade-off currently *inexpressible*; the core of any player-authored blade designer |
| P3 grippable | half-swording modelled as the attested practice it is | any qualifying new weapon can afford the form without engine edits |
| P4 guard axis | exporters/renderers stop guessing axes; basket coverage real | finer hilt design space (span × depth) for authored weapons |
| Renderer effect | width/edge stand-ins become **derived-and-checked**: the SVG becomes a *diagnostic* (a wrong silhouette = a wrong record), not an illustration | the same reconstruction pipeline can preview procedural weapons before they enter play |

The deep pattern: every fiat 0–1 scalar this proposal touches moves the same direction `hand_guard`,
`blade_guard`, `wt`, `spd`, `hand`, `pob_frac` already moved — **authored scalar → located/measured physical
fact → derived, parity-checked coefficient.** That is the model's own trajectory, extended, not amended.

---

## 6. Sequenced implementation plan

**Process wrapper for every tranche:** allocate one `ED-PC-NNNN` from `references/id_reservations.yaml`
(read `next_free`, allocate, bump, co-commit — IDs deliberately not pre-cited here); work lands PROPOSED;
merging the PR ratifies per ED-1094 **except** items marked Jordan-gated below, which must be called out as
*held back* in the PR body, loudly; commits `[design]`/`[patch]` scoped to the PC lane; run
`pytest tests/valoria` + relevant `tools/` validators before commit; capture pauses in
`handoffs/HANDOFF_PC.md`.

### T1 — P1 `edges` (land first)
**Why first:** smallest schema delta; identity-default proven pattern (B5's `adornments`/`edge_undulation`
landed exactly this way); the attesting facts (which weapons are single-edged) are trivially sourceable at
S1 for nearly the whole roster — no research campaign needed; immediate roster differentiation; zero
interaction with the pending Phase-C percussion recalibration.
**Steps:** schema + migration of all bladed records (S-graded source note per record, Phase-0 style) → the
two identity-default derivations (`edge_lines`, `has_spine`) with `[SIM-CALIBRATE]` gains → CI consistency
checks (report-only) → wind/legibility band audit.
**Acceptance (falsifiable, heft-style):** with fields present and gains at their initial values —
`edge_lines`: arming(1.0) > sabre(false-edge, frac) > falchion(0) = estoc(0); `has_spine`: katana=falchion=1,
arming=flamberge=estoc=0; **estoc byte-identical** on every derived quantity except the (zero) new terms;
any record left un-migrated byte-identical everywhere. Wind ordering sanity: the spine credit must not, by
itself, push falchion.wind above longsword.wind (guard/leverage/rigidity still dominate).

### T2 — P2-a/b profile data campaign + parity (no engine consumption)
**Why second:** the big fidelity win at zero balance risk; it is a *research* tranche (per-cluster specimen
fan-out mirroring Phase 0 — Haiku/Sonnet extraction lanes, Opus adversarial check per CLAUDE.md §10), so it
parallelises cleanly behind T1's small code change. Also unblocks P1-3 (thrust trueness) and G5.
**Acceptance:** all migrated elements close mass within the report band; parity report exists in CI output;
the falsifiable rigidity orderings of §3/P2-b hold (estoc > longsword > arming > sabre > shamshir; rapier
below arming despite section depth); renderer switched to profile-first width with stylization fallback and
the two paths visibly labelled.

### T3 — P3 `grippable` + retire `HALFSWORD_FORM` gating
**Acceptance:** derived half-sword set == {longsword, estoc} exactly; full-roster behavioural
byte-identity; the flamberge (and any other candidate) expansion question surfaced to Jordan as an explicit
held-back item, with the balance note that a new half-sword form is a new anti-plate capability.

### T4 — P4 guard axis rename (+ `depth_m` schema only)
**Acceptance:** numeric byte-identity of every baked `hand_guard`/`blade_guard`/`_derived` value across the
rename; exporter/renderer reads the typed axis. (The `HILT_CATCH_MULT` retirement parity work is a separate,
later, Jordan-gated item.)

### T5 — the Jordan-gated re-baselines (strictly after Phase-C percussion recalibration)
P2-c `cross_section` swap; P1-3 thrust-trueness; P4's coverage-derived `hand_guard`. Each: parity report →
Jordan sign-off → swap → recalibrate the `[SIM-CALIBRATE]` gains against the balance harness → re-export to
the GDScript port. Expect the Phase-C pattern: some tests go deliberately red between physics-landing and
recalibration — leave them red and documented, never patch a weapon's data to force old numbers back.

**Dependency spine:** T1 ⊣ nothing; T2 ⊣ nothing (parallel to T1); T3, T4 ⊣ nothing (small, after T1 for
review bandwidth); P1-3 ⊣ T1+T2; T5 ⊣ T2 + Phase-C. **First-to-land: T1.**

---

## 7. Anti-fabrication register (every number this audit introduces)

| Constant | Status | Basis |
|---|---|---|
| `LEGIB_EDGELINE_K` | `[SIM-CALIBRATE]` | start small, ≤ `DISTRACT_K`-effect scale; fit in balance pass; legibility floor audit |
| `SPINE_WIND_K` | `[SIM-CALIBRATE]` | bonus-only multiplier; wind `_band` re-centre after |
| thrust-trueness offset gain | `[SIM-CALIBRATE]` | operand is physical (`width_tip/2` point offset); gain fitted |
| mass-closure tolerance (±20% initial) | `[SIM-CALIBRATE]`, report-only | to be justified against the S1-best specimens before ever blocking |
| `k_shape` (section stiffness coefficient) | derived-per-shape (beam theory) + `[SIM-CALIBRATE]` residual | `w·t³/12` structure is textbook; the shape coefficient family must be documented per section form |
| `section_fill` values | **computed facts, not fiat** (diamond = 0.5 exactly; others from section drawings) | S-graded per record like any Phase-0 fact |
| ρ_iron 7860, `UNIT_M` 0.30 | existing sourced constants (`weapon_physics.py`) | reused, not re-asserted |
| all example magnitudes in prose above (yelman ~0.2–0.3, etc.) | **illustrative only** | must be sourced per-record at migration time |

No new numeric constant in this audit is proposed as canonical. Per CLAUDE.md §7, do not trust
`ci_sim_fabrication_check` to catch a smuggled value — the closure checks in P2-a are this proposal's own,
stronger, guard.

## 8. Open questions for Jordan (the loud list)

1. **T5 sequencing:** confirm the `cross_section` swap rides behind Phase-C percussion recalibration (this
   audit's recommendation), or fold both into one combined re-baseline pass.
2. **Flamberge half-sword:** once P3 lands, does the attested ricasso grant it a half-sword form (a new
   anti-plate capability for a roster weapon)?
3. **Scope of the P2 campaign:** all 53 weapons, or blades-first (the ~30 bladed records) with polearm heads
   deferred?
4. **Renderer's home:** promote the reconstruction script from scratchpad into `tools/` (as the P2 diagnostic
   surface) or keep it session-local until P2-a lands?
