# Capstone punch-list — scene-combat redesign (`plan_corrected_r3.md`)

Aggregated from three capstone verifiers: **dynamics-oscillator** (NEEDS_FIX),
**emergence-gate** (NEEDS_FIX), **coherence-jd** (PASS). Act on §1 before transcribing the plan into
the live plan file. Every MUST-FIX below was **independently re-verified against live code**
(`C:/Github/ttrpg-morph-rearch/designs/scene/combat_engine_v1/`, house rule: trust code over prose) —
the three lenses' findings are **disjoint** (no cross-lens duplication to collapse); each is listed
once with the confirming file:line.

**Oscillator BLOCKER verdict: STILL OPEN.** The round-3 BLOCKER is genuinely live in the plan and is
*unaddressed, not damped*. It must be resolved (as a new Jordan-decision) before ratification.

---

## 1. MUST-FIX BEFORE RATIFICATION  (4 items — 1 BLOCKER, 1 SERIOUS, 2 MINOR)

### [BLOCKER] M1 — D3/I3 closes an un-latched grip↔reach oscillator; break the cycle
*Lens: dynamics-oscillator. Disposition: **NEW JORDAN-DECISION** (attach to JD-6) + plan-text edit (add I3 acceptance gate).*

**Defect (code-verified).** D3/I3 makes `reach_base` grip-aware. That closes a per-beat feedback loop
`grip_target → close_unwieldiness → reach_base → grip_position` that does **not exist today**:
- `grip_target` drive reads `close_unwieldiness(c,cfg)` — `systems.py:155`
- `close_unwieldiness = max(0, reach_base(c,cfg) − CLOSE_REACH_REF)` — `systems.py:142`
- `reach_base` is **grip-blind today** (reads only `head_len/grip_len/hands/reach_adj`) — `systems.py:18-20`
- `grip_choke_max` reads only `c.w`, so it does **not** break the cycle — `weapon_physics.py:448`

The recurrence `g[n] = grip_choke_max(w)·min(1,(reach_base(w,g[n-1])−6.5)/CHOKE_DRIVE_REF)` iterated
against live CFG (`CLOSE_REACH_REF=6.5` config.py:95; `CHOKE_DRIVE_REF=1.5` config.py:85;
`L0=4.0`/`REACH_GEOM_SCALE=0.635`/`REACH_2H_K=0.4` config.py:4,11) is a **hard 2-cycle** for every
gathering pole: spear 0↔0.865 (reach flips 7.797↔5.326, ±2.47 units/beat), yari/guandao/voulge 0↔1.0,
glaive 0↔0.467, guisarme 0↔0.396, bardiche 0↔0.627 — forever. Every closed-exchange reach consumer
(`reach_sigma`, `str_demand`, `slip_inside`, `close_tempo`, reopen `base_gap`) flips each beat.
Confirmed unaddressed: D3's sequence lists `grip_target (wrapper.py:66, unchanged)`
(`plan_corrected_r3.md:424`); the only `close_unwieldiness` mentions treat it as a reach *consumer*,
never as the grip *driver*. (Spear anchor re-derived by hand: `4.0+0.635·(5.5+0.4·1.2)=7.797` ✓,
drive `min(1,1.297/1.5)=0.865` ✓.)

**Required change.** Feed `grip_target`'s drive term a reach evaluated at a **fixed grip** so its input
no longer depends on its output. **RECOMMENDED (fix A):** drive `grip_target` from open-measure reach —
evaluate `reach_base` at `grip_position=0.0` inside a dedicated `close_unwieldiness` variant used *only*
by `grip_target` (one-line change at `systems.py:155`). Verified stable fixed points, no beat flip:
**spear 0.865, yari 1.0, glaive 0.467, guisarme 0.396, bardiche 0.627** — these **match the plan's own
D2 `Φ_grip@g*` table**, so the D2 damage-retention numbers stand once the loop is fixed. Keep
`reach_base` grip-aware for its ~10 other consumers (that is the point of D3); only `grip_target`'s
drive input reverts to g=0. The grip-aware `close_unwieldiness` used by `close_tempo` (`systems.py:64`,
multiplied by `(1−grip_position)`) stays live — not part of any cycle.
Alternatives, for the JD: **(B)** under-relaxation `g[n]=0.5·(g[n-1]+f(g[n-1]))` — verified convergent
(spear 0.298) but adds a knob and converges to a *different* g*; **(C)** latch `grip_position>0` while
`closed` holds — needs an explicit reset rule.

**Why a Jordan-decision, not a silent edit.** The drive-input choice is design-meaningful and its
converged g* directly feeds the D2 damage numbers. **Surface as a Jordan-decision attached to JD-6.**

**Also add (plan-text edit):** an **I3 acceptance gate** — the per-beat `grip_position` sequence for
every gathering pole converges (no sustained 2-cycle) within N beats — a direct regression against this
defect. Note (orthogonality, confirmed): this loop is *independent* of D3's two-recompute `er`
contract, which is internally sound; the `er` plumbing neither creates nor cures the oscillation, so
D3's `er` work is not wasted — the loop-break is added *alongside* it.

---

### [SERIOUS] M2 — `pc_sel` is load-bearing in 3 places but the data-flow never produces it
*Lens: emergence-gate. Disposition: **PLAN-TEXT EDIT** (widen the D2b carried contract + add orphan-table row / first-reader increments).*

**Defect (code-verified).** Three consumers read `pc_sel` = *the selected element's own*
`point_concentration`:
- D2 `cut_thrust` blend `Φ_grip = pc_sel·1.0 + (1−pc_sel)·Φ_swing` — `plan_corrected_r3.md:288-289`
- D5 `close_efficacy = 1−(1−pc_sel)·f()` — line 514
- swing-room legibility term `(1−pc_sel)`-weighted — line 489/970

But the widened `select_mode` return contract carries only `(dm,h,sel_gap,sel_perc)` (plan:341-354;
orphan table line 964) and `element_afforded` carries `(gap,perc,element_ref)` — **none is
point_concentration.** Verified: `select_mode` returns a **2-tuple `(dm,h)`** today (`systems.py:335`);
`element_afforded` returns a `(eff,dm)` heads dict (`systems.py:259+`). `sel_gap = gap_precision(pc,cs)`
is a **nonlinear product** of pc AND cross_section (`geometry.py:79`), so pc_sel is **not recoverable**
from `sel_gap`; `element_ref` indexes `elements[]` (mass/x_m only). The quantity **is** available on
the winning `mode_element`'s baked `geo['point_concentration']` (passthrough, `geometry.py:74`) but the
plan never threads it. So I2 gates #2/#3 and I4 gate #4 reference `pc_sel` while its plumbing is
unspecified — the arc-vs-thrust discriminator the redesign hinges on is under-plumbed. (Note: the
*keying* on the selected element is correct and confirmed; only the within-mode-blend *plumbing* is the
gap.)

**Required change.** Widen the carried contract to include `sel_pc` = the winning `mode_element`'s
`geo['point_concentration']` (source it in `element_afforded` alongside `sel_gap`/`sel_perc` — e.g. a
5-tuple `(dm,h,sel_gap,sel_perc,sel_pc)`, or carry the winning `element_ref` AND read that
`mode_element`'s baked geo). Add a `c.sel_pc` Combatant field + an orphan-table row + a first-reader
increment (**I2** for the D2 blend; **I4/I5** for close_efficacy / legibility). This is the exact
analogue of the `sel_gap` fix already specified — no new fiat scalar.

---

### [MINOR] M3 — I2 acceptance gate #2 asserts an unreachable partisan/spetum POINT selection
*Lens: emergence-gate. Disposition: **PLAN-TEXT EDIT** (reword the gate).*

**Defect (code-verified).** I2 acc #2 (plan:759-763) requires "partisan/spetum's POINT-selected strikes
≥ 0.9". But `partisan` (`weapons.py:279`) and `spetum` (`weapons.py:265`) carry `head='cut_thrust'` and
**no `mode_elements`** (only 8 weapons have them — poleaxe/kama_yari/voulge/guisarme/ji/bec_de_corbin/
lucerne_hammer/goedendag; verified exactly 8 `mode_elements=[` code blocks). So `_mode_elements`
synthesizes one `{head:'cut_thrust'}` element each and `select_mode` can only ever return
`h='cut_thrust'`, never `'point'`. The gate describes a case that cannot occur. Substance is handled
correctly elsewhere (JD-8: partisan/spetum are cut_thrust, swing fraction degrades, thrust-protection
would require *authoring* a point mode_element) — this is gate wording, not a design error.

**Required change.** Reword I2 acc #2 to drop the "partisan/spetum POINT-selected ≥ 0.9" clause and
instead assert their `cut_thrust` selection retains its `pc_sel`-weighted swing degradation
(~0.75/0.86) per the **JD-8 default** — consistent with the JD-8 disposition already in the plan.

---

### [MINOR] M4 — D2b names `at_circumstance` as the per-element percussion producer, but it computes no percussion
*Lens: emergence-gate. Disposition: **PLAN-TEXT EDIT** (correct the cited function).*

**Defect (code-verified).** D2b point 1 (plan:347-349) says `element_afforded` computes per-element
percussion "via `at_circumstance` on that element's located mass." But `at_circumstance`/`at_grip`
returns `{I_g,S_g,d_g,u}` (+ `rear_clearance`/`geom_slide`) — **none is a percussion value.** Percussion
is `percussion_authority(w) = min(PERC_CAP, PERC_SCALE·(√mass·pob·energy_credit)^PERC_EXP)`
(`weapon_physics.py:224`), needing the element's mass, its effective moment arm, and `energy_credit`.
The per-element mass+position **is** a real located primitive (so this is **not** an emergence
violation) — but naming `at_circumstance` as the producer would mislead the implementer.

**Required change.** Restate D2b's per-element percussion as a per-element application of the
**`percussion_authority` form** (element `mass_kg` + its `x_m` as the moment arm, whole-weapon
`energy_credit`), not "via `at_circumstance`". No new fiat scalar — just cite the right derivation so
the I2 implementer wires it correctly.

---

## 2. CONFIRMED SOUND  (ratification record — what was verified and passed)

### Oscillator lens — confirmations (dynamics-oscillator)
- The two-recompute `er` ordering is **internally consistent and sound**: within one beat, after
  `wrapper.py:66` writes `g[n]`, Refresh #1 (pre-swap) and #2 (post-swap) both recompute `er` from
  `reach_base(c,g[n])`; `str_demand`/`slip_inside`/`reach_sigma` resolve that same g[n]-reach; #1==#2
  for a non-form weapon. No frozen/live reach split *within* a beat. R-6 scoping (Refresh #1 re-derives
  only `er`, not the running `measure_gap`:90 / latched `closed`:93/:81) is correct and prevents the
  approach-stall / un-latch it targets.
- The oscillation defect is **orthogonal** to the two-recompute contract — it lives entirely in the
  `grip_target/reach_base` cycle; D3's `er` work is not wasted.
- **Weapons provably safe** from the loop: staff (reach@0=6.489<6.5 → never gathers), arming/longsword/
  dagger (`grip_choke_max=0` → grip always 0); poleaxe self-DAMPS (reach@0=6.617 → converges ~0.04),
  not a sustained oscillator.
- Map is a latched recurrence `g[n]=f(g[n-1])` (grip_target's RHS reads the PRIOR beat's grip; Refresh
  #1/#2 touch only `er`) — cannot diverge within a beat; failure mode is beat-to-beat oscillation,
  exactly as framed.

### Emergence-gate lens — confirmations
- **Constant enumeration clean:** every NEW numeric constant correctly bucketed. `SWING_FLOOR`, r*, σ,
  floor carry `[SIM-CALIBRATE]` + ablation-gated (bucket B); `close_efficacy f()` and swing-room
  legibility direction are `[SIM-CALIBRATE]`, small + ablation-gated, missing-treatise-grounding flagged
  (bucket B, honest); facing profile is `[FIAT — C1]`; `ρ(g)`, `rear_clearance`, `geom_slide` are
  primitive-derived (bucket A); `GRIP_MIN_WORKING=0.30` is an existing tagged `[FIAT]` reused. No
  primitive-derivable value silently picked; no fiat dressed as grounded.
- **Fork (i) — hook pull-vs-bind dropped the emergent way:** D9 forbids a `pull_capable/hook` clinch
  scalar; I7b acc #7 adds a grep-assertion that no such data boolean exists. Verified the guard is
  necessary + sound: `test_no_weapon_name_literal_in_resolution` scans only weapon-NAME literals and is
  blind to data booleans in `weapons.py` — the grep-assertion is the correct complementary guard.
- **Fork (ii) — thrust-damage grip-invariance keyed on the SELECTED ELEMENT** (`sel_head=='point'`),
  genuinely per-element, no name/class/whole-weapon-pc proxy. Verified `bear_spear` (whole-weapon
  pc=0.55) synthesizes `{head:'point'}` → `Φ_thrust=1.0`; the pc-overlap defect is real (bear_spear
  0.55 < greatsword 0.62), confirming a whole-weapon-pc blend would mis-degrade a pure-thrust pole — so
  keying on the selected element is the correct emergent fix. (Only the within-mode-blend *plumbing* is
  the SERIOUS gap M2 above.)
- `test_no_weapon_name_literal_in_resolution` stays green by construction: nothing branches on weapon
  name/kind; every discriminator is a located primitive or the derived selected-element mode token;
  names appear only as diagnostic labels. The `[ASSERTED — rigid-body first principles]` label on
  thrust grip-invariance honestly demotes the Rinaldi/PMC cites.
- **Layer discipline + C-flags respected:** `Φ_room` cut from the heft path (R-8/JD-1(d)) with a
  code-check acceptance (no room operand multiplies `WP.heft`); the ~29% greatsword heft-room delta +
  monotonicity (C4) surfaced as JD-1(d), not hidden; greatsword cure routed through commit-window +
  legibility (interior optimum) + D2b percussion. `grip_choke_max(greatsword)=0.15` verified by hand;
  reach anchor R-4 correction (spear=7.797) verified by hand.
- **Residual honesty intact:** poleaxe hammer-vs-spike red is a genuine Phase-C calibration red (JD-3 +
  accepted-red #6); retained-material set honestly downgraded (guandao clean; voulge/bardiche
  borderline + ablation-gated, JD-1); BLOCKER-2 (sel_perc orphan) + the 2-tuple `select_mode` contract
  both real and scoped into the atomic I2 increment. 8 residuals carried as explicit Jordan-decisions —
  no manufactured resolutions.

### Coherence-jd lens — confirmations (PASS, zero must-fix)
- **Increment chain coherent** (verified vs live code): I0→I1→I2→I3→I4→I5→I6→I7a→I7b→I8; every
  "Depends on" points strictly backward; I3→I4→I5 chain respected; I7 split respected (I7a rear_clearance
  deps I2; I7b contact.py deps I7a); D1's L0 bundle lands in I2 before both consumers. Satisfiable.
- **Orphan table complete + 3 samples confirmed:** (1) `sel_perc→core.strike:171` passes whole-weapon
  `WP.percussion_authority` — row 966 retires it; (2) clinch DELETE — 1-10 field on ~54 records, ZERO
  live readers — retired in I7b (row 982); (3) `select_mode` 4-tuple — live returns `(dm,h)`
  (systems.py:335), widened correctly (row 985). Every retired static path has a named replacement.
- **No latent clinch:** every new stored field/function (sel_gap, sel_perc, sel_head, range_avail,
  geom_slide, rear_clearance, range_utilization, facing_target, grab_*, opening_created, element_ref,
  orient_deg, material, Contact state, 'contact' TRACE_KIND, per-element percussion, er REFRESH #1/#2)
  has a consumer row; the two apparent gaps (sel_dmg, close_efficacy) are benign (pre-existing field /
  computed scalar with tracked inputs).
- **Reach anchors (R-4) exactly reproducible on the live engine:** ran `systems.reach_base` — spear
  7.797, glaive 7.200, poleaxe 6.617, staff 6.489, guisarme 7.095, yari 8.185, bardiche 7.441 — all
  match the plan table to 3dp; confirms the numbers are measured, not fabricated.
- **Damage-model mechanism (R-1) verified:** `core.py:143-156` — a multiplicative Φ on `heft_units`
  shrinks only the heft term, not the additive strength floor, so worst-case-at-high-STR gating (STR
  2/4/6/8 ranges gated at the highest-STR column) is the correct discipline.
- **`Φ_room` split principled, not contradictory:** cut from heft (int-rounds away + monotone → C4
  violation, JD-1(d)); retained on percussion (feeds an un-rounded σ channel → not cosmetic,
  interior-optimum-shaped, ablation-gated at I8). Rests on the verified fact that heft and percussion
  route to different downstream paths. `measure_gap`: D3 refuses to RE-DERIVE it while D4/D5 READ it —
  read ≠ re-derive, no conflict.
- **M-11 (Contact = BUILD not activation) verified:** `state_graph.py` has 13 TRACE_KINDS (no 'contact')
  and 15 STATES (no Contact node); contact.axis injection is `(WS-5, unbuilt)`. M-03 frozen/live split
  confirmed (reach_sigma reads frozen er systems.py:141; slip_inside reads reach_base live
  wrapper.py:230).
- **Schema/data claims confirmed:** orient_deg/element_ref/material = 0 matches in weapons.py (dropped;
  D0 must re-ingest); sel_perc/sel_gap = 0 matches (genuinely new); 8 authored mode_elements;
  lucerne_hammer has two blunt elements + one point; voulge 3 mass / 2 mode / rear_fluke dual-role;
  select_mode ignores its `closed` param (systems.py:302); parity test has the 5 named functions +
  importorskip numpy.
- **Jordan-decision integrity:** all 8 JDs are genuine forks tied to specific increments, each with an
  honest "plan default" not an invented resolution. JD-1 (BLOCKER-class) surfaces the damage/I_g tension
  with three tried interpretations and their MEASURED failures. Two biomech BLOCKER-class findings close
  the BUG "by construction" (NaN via ρ:=1.0 guard; zero-collapse via sel_head=='point'→Φ=1.0) while the
  POLICY question is correctly surfaced as JD-1(b). No BLOCKER quietly resolved in prose; no JD is an
  invented resolution.
- **Minor imprecisions (non-blocking, no change required):** (a) voulge rear_fluke is list-LAST
  (index 2), not "mid-list" — substance (element_ref needed) correct; (b) clinch is on ~54 records, not
  "~55". Neither affects soundness.

---

## Ratification gate summary
- **MUST-FIX total: 4** — **1 BLOCKER, 1 SERIOUS, 2 MINOR.**
- **Dispositions:** 1 new Jordan-decision (M1, attach to JD-6) + 3 plan-text edits (M2, M3, M4).
  M1 additionally requires a plan-text edit (the new I3 convergence acceptance gate).
- **Oscillator BLOCKER: STILL OPEN** — the round-3 grip↔reach oscillator is live and unaddressed in the
  plan; resolve M1 before transcribing to the live plan file.
- **coherence-jd PASSES clean** (increment DAG, orphan table, reach anchors, JD integrity all verified
  against live code) — no structural blocker to transcription once M1–M4 land.
