# Coverage Matrix — Weapon System v2 (Active)

Archived entries in tests/coverage_matrix_archive.md

## 2026-07-23 — ED-MB-0030: conditional orders (own_strength trigger + locked distance-conditional)
- Jordan directive: "conditionals — a unit only starts retreating when the opponent is within X /
  advancing then withdrawing when X." **Verified** the existing `Order` primitive already covers the
  DISTANCE case: `Order(trigger='enemy_range:D', behavior={'stance':'retreat'|'yielding':True})` fires
  when the subunit closes within D; `stance`/`yielding` are both `_ORDER_SAFE_FIELDS`; `build_army`
  forwards the spec `orders` key. Locked in with `test_conditional_orders.py` (fires on close; does not
  fire out of range) — no redundant knob added (bottom-up reuse).
- **Added** the missing `own_strength:FRAC` trigger: fires once `troop_total()/_start_troops <= FRAC` —
  a unit reacting to its OWN attrition (withdraw a spent body, commit a weakened one, brace when
  thinned). Wired in `units.py` Order validation + `_ORDER_TRIGGER_KINDS` + `contact.py` `check_orders`;
  reuses the `_start_troops` spawn denominator (no new state).
- Byte-exact (orders default `()`; goldens carry none; bat.py EXIT=0). Tests: 8 in
  `test_conditional_orders.py`.

## 2026-07-23 — ED-MB-0029: intent as an offence/defence resolution axis
- Jordan directive: "hold-and-defend vs rout-the-other resolve differently — intent makes a big
  difference." `stance` (was movement-speed only) is now a signed offence/defence **commitment** in the
  exchange: `cX` ∈ {aggressive +1, balanced 0, hold/retreat −1} enters the sigma head as delta-sigma net
  `ns_a += (cA·OFF + cB·DEF)·SIGMA_PER_D` (own press + enemy exposure/blunting), symmetric for B —
  uniform-impact like the octagon/puncture terms, **not** a raw damage multiplier.
- Anchored to the §A tactic-card **asymmetry** (Disciplined Defence +1D; Standard Advance no effect) →
  `DEF=1.0 > OFF=0.5`: a holding pin **survives** a pressing foe (buys time, Cannae centre); aggression
  is punished vs a steady wall.
- Effect (intent_probe, OFF→ON): hold-vs-balanced holder casualties 67→57 & win 35%→50%;
  aggressive-vs-hold holder wins 65/35.
- Gated `PC_INTENT_RESOLUTION` (default OFF; balanced=0 → inert; byte-exact, bat.py EXIT=0). Tests:
  `test_intent_resolution.py` (8). Detail: `rotation_model_v1.md`.

## 2026-07-23 — ED-MB-0028: cell-level closing-ranks lifecycle (T1 Phase 1a)
- Foundational primitive for Jordan's rotation directive: `Subunit.close_ranks()` reflows a subunit's
  **living** troops front-rank-first (`orig_r` asc) toward each cell's spawn density (`_cell_target`),
  depleting the rear. A **deep** formation holds full front-cell density — hence full front combat pool
  (`_pair_engaged_troops` weights by engaged-front-cell troops) — until depth is spent; a shallow one
  thins at the front immediately. Makes literal the reserve the depth machinery only abstracted;
  `PC_REFILL_FLOOR` was never wired.
- Conservation exact; relational (troops close toward the front, no scattered holes); emptied cells keep
  key at 0.0 (functional coverage-shrink, no cell-set mutation — Phase 1b handles literal dissolution).
- Wired into the tick **after** both units' casualties (stays simultaneous) + col-grid resync.
- Gated `PC_CLOSE_RANKS` (default OFF → byte-exact; bat.py 4 modes EXIT=0). Effect: DEEP(3×4) vs
  SEMI(6×2) **81%→94%** ON. Tests: `test_close_ranks.py` (7). Detail: `rotation_model_v1.md`.

## 2026-07-23 — ED-MB-0027: honest-gauge measurement integrity (density held at 100/cell)
- Fixed the confirmed #1 gauge distortion (fiat register M1): the per-cell **density mismatch** between
  `make_unit→build_unit` (legacy tier footprint, ~16/cell) and the composed presets (`concentration=100`).
  Density enters `_lanchester_strength` **linearly**, so the ~8× gap — not flanking geometry — drove
  H3/H4/C4 to a fiat 100% (null test: dense-vs-thin, zero envelopment, already 100%).
- **Fix:** hold density constant at `GAUGE_CONC=100` across every gauge unit by building single AND
  composed units from the same explicit troops/concentration path (`build_army→footprint_for`);
  `GAUGE_TROOPS=600` divides evenly under every split (1/3,2/3,1/2) → exact quantization. Verified all
  unit types build at exactly 100.0/cell, hp_max=600.
- **Fair-ruler result:** H1 mirror 50/50 (was 44/56); envelop/refused/wedge **flip to ~0%** (force-
  splitting is pure downside — geometry converts to no outcome); 15/20 rows flag real engine divergence
  (brace P2 not repelling C2/C6=57 raw; cav mirror C3=71 asym; GappedLine H7/H8 over-strong).
- Bands NOT re-fit (§8 north star). Gauge is a manual harness (no `test_` funcs → not CI); `bat.py` has
  its own `make_unit` → byte-exact goldens unaffected. Detail: `honest_gauge_readout.md`.

## 2026-07-23 — ED-MB-0026: explicit frontage×depth (columns×rows) + gradient-forwarding fix
- `Subunit.width`/`depth`: both set → `footprint_for` builds an exact width×depth rectangular grid
  (density = troops/(w·d) follows) — the coupled tactical axes (wide-shallow = frontage/envelopment;
  narrow-deep = breakthrough/depth). Threaded through `_oriented`, `_spec_span`, `build_army` forwarding;
  Subunit validation now accepts troops + (concentration OR width×depth).
- Closes an ED-MB-0025 gap: `build_army` never forwarded `distribution` (gradient) nor width/depth from the
  spec dict — now all forwarded, so the full deployment-primitive set is reachable via the army-builder.
- Byte-exact unaffected (all inert in tier mode; bat.py uses tier). Tests: `test_deployment_primitives.py`
  (+2 = 9); 138-test mass-battle sweep green.

## 2026-07-23 — ED-MB-0025: explicit subunit deployment primitives + build_envelopment wing fix
- **Explicit density honored:** `footprint_for` now interprets `concentration` as target troops/cell and
  builds the exact implied cell count via `_build_shape_n` (arbitrary-N shape builders) — fixes the M2 bug
  where a 133-troop Line collapsed to 1 cell at every concentration (density silently inert), the root of
  the 8–12× composed-vs-single per-cell density mismatch.
- **Density gradient:** new `Subunit.distribution` ∈ {uniform, front, rear} weights `cell_troops` across
  ranks (front = shock/leading-rank-heavy, rear = depth/Leuctra deep wing), conserving `troop_count`.
- **build_envelopment wing fix:** wings placed relative to the center's *actual* column (honors a pre-set
  `starting_position`) instead of a phantom field-center anchor — pre-fix wings landed at 21/27 while the
  center sat at col 9 (never wrapped); now they straddle it. Explicit wing positions also honored.
- **Verified:** mirror-symmetry (n=120 × 4 seed bases) ~50/50, no bias → combat/movement already Jacobi.
  Honest gauge (matched-density explicit blocks): envelopment 100% → ~40% → density artifact gone, mechanic
  under-performs (real work remains). All 4 bat.py goldens re-recorded (deliberate composed-row change;
  tier mode → density/gradient inert there): unit b70a9348, cell d46c8808, unit_field 3cc40104, cell_field f9c6dea1.
- **Adversarial-review fix:** `build_refused_flank` had the *same* phantom-anchor bug (5th-critic finding) —
  refused wing placed against the field-center, ignoring an explicitly-placed strong wing. Same fix applied
  (honor pre-set positions; place the refused wing on the strong wing's actual span). Latent (the gauge sets
  both positions explicitly → byte-exact unchanged), was uncovered by tests; now covered.
- Tests: `tests/valoria/test_deployment_primitives.py` (7 — incl. refused-flank sibling-fix).

## 2026-07-23 — ED-MB-0024: DG-2 fighting-withdrawal residuals (emergent entry + rally + pocket exits)
- Completes the three parts ED-MB-0005 deferred after shipping the yield state + commanded entry
  (`proposals/mass_battle_fighting_withdrawal_v1.md` §2.2/§2.4):
  - **Emergent auto-entry** (§2.2, `morale_check_phase`): a disciplined subunit (`eff_discipline >=
    D_YIELD`, `command>0`, non-ranged) crossing the §A.4 `frac<0.50` casualty trigger **enters yielding**
    instead of only eroding. Sets state only — the erosion-brake calibration stays deferred (`needs_jordan`).
  - **Rally exit** (§2.4, `between_turn_recovery`): at the turn-break lull a yielding subunit whose morale
    recovered to `>= YIELD_RALLY_MORALE_FRAC` (0.75) of start reverts to normal combat.
  - **Pocket exit** (§2.4, new `Subunit.pocketed` via `_yield_pocketed`): rearward motion blocked (flee
    vector off-map, or an enemy within `YIELD_POCKET_REACH` in the retreat path) → yielding holds with the
    combat malus **removed** (Cannae's pinned-and-annihilated kill condition). Reuses only `enemy_cells` +
    `BATTLEFIELD_SIZE`, no new collision code.
- **All three gated OFF** (`PC_YIELD_EMERGENT` / `PC_YIELD_RALLY` / `PC_YIELD_POCKET`) → yielding never
  auto-set, rally never fires, `pocketed` never set + the exchange guard reduces to the ED-MB-0005 malus →
  **byte-exact** (bat.py all 4 digests byte-identical). `pocketed` cleared at the battle boundary.
  `needs_jordan` on the three flips, the emergent path's blast radius (§4.3), and both CALIBRATED-DEBT
  magnitudes.
- Tests: `tests/valoria/test_dg2_yield_residuals.py` (10) — emergent on/skip-low-disc/off-inert, rally
  revert/keep/off-inert, pocket map-edge/enemy-behind/open/malus-removed.

## 2026-07-23 — ED-MB-0023: Reserve formation Phase-3-commit rule (PP-MB-04 / §A.6)
- Wires the previously-inert `reserve` instruction (config `ROLE_SPEC` "Reserve"/"Support", zero code
  consumed it) into `run_multi_unit_battle`. A unit held in Reserve (`unit_in_reserve` — any subunit
  carries `reserve`) is **benched turn 1** and its pairing **commits** (re-activates) at
  `RESERVE_COMMIT_TURN`=2 (Phase 3 of the next turn), engaging from Phase 5 of that turn — canonical
  "declare turn N → commit Phase 3 turn N+1 → engage Phase 5 turn N+1", not delayed to N+2. First
  engagement uses the default equal Off/Def split (no Phase 1 window) — already this path's behaviour.
- Termination guard extended so a battle whose only pair is a still-benched reserve doesn't break early.
- **Gated OFF** (`PC_RESERVE_COMMIT`, default 0) → reserve inert, all pairs active turn 1 → byte-exact;
  `run_multi_unit_battle` isn't in the bat.py golden battery → double-safe. `needs_jordan` on the flip +
  the battle-turn-granularity modeling (whole engagements per turn, so "commit P3 / engage P5" collapses
  to "engages from turn 2").
- Tests: `tests/valoria/test_reserve_commit.py` (4) — predicate, ON bench-then-commit-turn-2, OFF inert,
  no-reserve battle unaffected.

## 2026-07-23 — ED-MB-0022: Feigned Retreat tactic (PP-256)
- Wires the previously-inert Feigned Retreat dice-modifier row (mass_battle_v30 §A.12 / §B.4) into the
  field engine's pursuit path. A unit that declares a Feigned Retreat (`Unit.feigned`) withdraws as if
  routing to bait a pursuer; when a Fast victor pursues it, `resolve_feigned_retreat` runs the two-stage
  resolution — (1) pursuing general rolls Command Ob 2 to **recognise** the feint (success → no effect);
  (2) if deceived, a Discipline **Ob 1** check (PP-256). Failing (2) marks the pursuer `overextended`,
  cutting its next engagement pool by `OVEREXTEND_PENALTY` (=2) via a gated branch in `base_combat_pool`.
- **Convention (verified, not a bug):** the checks use the shared `roll_pool` net-successes convention
  (botch die included) that every §A check uses. Realized hold rates: Disc-1 ~40% (matches PP-256 exactly),
  Disc-4 ~74.5% vs the doc's no-botch binomial ~87%. A bespoke botch-free counter was rejected (scale-local
  dialect = CLAUDE.md §10 guardrail).
- **Gated OFF** (`PC_FEIGNED_RETREAT`, default 0) → flags never set + pool branch inert → byte-exact;
  additionally the pursuit path is in `run_multi_unit_battle`, NOT the bat.py single-pair golden battery →
  double-safe. Transient flags cleared at `reset_morale_between_battles`. `needs_jordan` on the default-flip
  + the `OVEREXTEND_PENALTY` magnitude (reuses the §B.4 strategic −2D at field scale — confirm transfer).
- Tests: `tests/valoria/test_feigned_retreat.py` (6) — Disc-rate band + monotonicity, recognise rises with
  Command, overextend only when deceived+failed, non-feigning no-op, gate-OFF inert, pool-penalty ON vs OFF.

## 2026-07-23 — ED-MB-0021: P-DEC-3 per-troop-type density cap
- Jordan-ratified mechanism (spatial_model_v2_plan §9 P-DEC-3): a cavalry cell holds fewer troops than an
  infantry cell ("fewer horses than men fit per unit area") — a per-troop-type density cap, NOT a larger box.
- `cell_cap_for(troop_type)` (config): mounted types (cavalry/knights_templar/mounted_archers) cap at 100
  (half of `CELL_CAP=200`); foot types keep the full cap. Threaded into `footprint_for(…, troop_type)` +
  its two callers. A mounted body deploys over MORE cells (wider frontage); the combat density factor drops
  naturally via the higher `ncells` (no attrition edit).
- **Gated OFF** (`PC_TROOP_DENSITY_CAP`, default 0) → byte-exact (cell_cap_for → CELL_CAP; and the byte-exact
  cavalry rows use tier mode, not footprint_for). The cavalry cap **value** (100) is a calibration →
  `needs_jordan` on the value + default-flip (mirrors ED-MB-0016).
- Tests: `tests/valoria/test_troop_density_cap.py` (4) — OFF byte-exact, ON caps mounted lower, cavalry
  deploys wider, None-type uses full cap.

## 2026-07-23 — perimeter target-point / face-normal geometry primitive (Jordan ruling 2026-07-23)
- New `tests/sim/mass_battle/perimeter.py`: pure-geometry primitive from `perimeter_targeting_geometry_v1.md`.
  A subunit's perimeter carries TARGET POINTS an attacker aims at, each with an outward NORMAL (the
  required approach angle): **major** = face midpoints (normal ⊥ face), **minor** = corners (bisector
  normal), sharp vertex (interior angle ≤ `SHARP_TIP_DEG=60`) flagged (the pointed-formation exception).
  Faces from the convex hull (clean straight + diagonal faces; matches Jordan's drawing). `target_points`,
  `perimeter_faces`, `nearest_target` (the face an attacker engages), `approach_alignment` (how square-on
  a heading is vs the inward normal — the signal a future alignment gate/bonus consumes).
- **Pure geometry, no engine wiring** → zero golden/regression impact. The behavioural wiring
  (approach-along-normal pathing, alignment gate, interception) is the Jordan-gated next step.
- Tests: `tests/valoria/test_perimeter_geometry.py` (7) — Line=4-face rectangle, cardinal face normals,
  Arrowhead sharp-tip flagging, nearest-face targeting, square-on alignment=1.0, degenerate fallback,
  determinism. Known limitation: convex hull bridges a concave gap (GappedLine's lane) — concave/internal-
  face handling is a documented follow-up.

## 2026-07-23 — ED-MB-0019: ED-MB-0018 adversarial-review fix batch
- Jordan directive: "comprehensive max effort adversarial review." Ran 5 structurally-independent read-only
  critics (arc-math, reaction-clock, byte-exact/determinism, multi-side/balance, test-quality) + an
  architectural cell-up audit + a full-campaign gauge A/B (n=60).
- **Reaction-clock lifecycle (R1/R2):** `_react_since` was per-engagement transient state stamped with the
  per-turn tick but stored on the persistent Subunit and never reset → asymmetric re-engagement mis-scored.
  Fixed with a frame-independent, per-tick-idempotent consecutive-tick counter + reset at
  `reset_positions`/`reset_morale_between_battles` (field continuous engagements keep it via the node-skip).
- **Multi-side shock re-triggered (A1/A1-gap, arch #1):** was `eng_counts≥2` (arc-blind pair count) — two
  attackers both in front wrongly shocked (1.75×), one wide wrapping body missed. Now a **nearest-perimeter-
  FACE** bearing model (distinct faces struck), **graded** `×(1+shock·(nsides−1))`.
- **Double-count (arch #2):** `ENCIRCLEMENT_PENALTY` fired on the same trigger, ungated → gated
  `if not PC_OCTAGON_DMG`. **t=None footgun** guarded. **CI `_PINNED_OFF`** now pins `PC_OCTAGON_DMG=1`.
- **Tests strengthened:** T2/T4/T5 tested inputs/stamps not effects → now measure the actual effect; added
  face-model + reaction-reset regressions (6 green). Legacy `PC_OCTAGON_DMG=0` proven byte-identical 240/240
  vs parent. **All 4 bat.py goldens re-recorded under CORRECT envs** (the first cut recorded grid under a
  bare env — wrong digest; grid oracle needs full `_PINNED_OFF` incl `PC_NODE_COHESION=0`).
- **Gauge A/B:** mirror byte-identical; moved rows shift TOWARD bands (H2/H5/H6); no row more over-decisive;
  H3/H4 already 100%-decisive under both flags → octagon deepens the casualty exchange ratio (DG-6 caveat).
- Disclosure: `octagon_damage_model.md` adversarial-review addendum; geometry spec
  `perimeter_targeting_geometry_v1.md`; readiness synthesis `historical_fidelity_readiness.md`.

## 2026-07-23 — ED-MB-0018: octagon facing = damage-received multiplier + reaction delay + multi-side shock
- Jordan directive: "the facing octagon is a **damage-received multiplier** — attacks from behind do ~**2×**
  the damage of from the front; cells **cannot turn instantaneously** (needs a couple-tick reaction); attacked
  from **multiple sides** is **extra bad**, not just a divide-by-two." Replaces the legacy `-2`-dice octagon
  **pool** penalty (too weak — legacy rear was only 1.25× front, flank often 1.00× after `round()`).
- **(1) Arc = damage multiplier.** New `_octagon_dmg_mod` (orchestration.py) computes the pure per-cell
  facing arc — front GREEN **1.0×** / flank YELLOW **1.5×** / rear RED **2.0×** (`mult = 1 − arc·(RED−1)/2`),
  multiplying the **defender's** casualties; the pool/sigma angle-penalty is zeroed under the flag (no
  double-count). Reads the arc against the **LOCAL** attacker centroid (cells within `OCTAGON_LOCAL_REACH=2.0`)
  so a **wide** line's wing cell in a head-on clash stays GREEN instead of mis-reading the enemy centre as an
  oblique flank — verified **front→1.00×, rear→2.00× exactly per-seed**. Compounds with frontal-brace/charge-
  shock stripping → a braced front that parries to 0 is annihilated from behind (Cannae).
- **(2) Reaction delay.** A cell hit outside its front arc keeps its exposed facing until
  `FACING_REACTION_TICKS=2` elapse, and only refuses if it can **see** the threat (≤`FOV_HALF_DEG`=105°) and
  is not frontally **pinned**. A **rear** strike is in the blind arc → never perceived → the 2× persists the
  whole engagement (du Picq: reaction time under surprise).
- **(3) Multi-side shock.** `eng_counts≥2` → extra `×(1+MULTI_SIDE_SHOCK=0.5)` **compounding** (rank-relief
  collapse under encirclement) — worse than a halving.
- **Supersession (deliberate):** under `PC_OCTAGON_DMG=1` (**default ON**) the legacy wrapper/pocket/roll-up
  pool-penalty envelopment machinery goes dormant (wrap→rear arc 2×, pocket→multi-side shock; roll-up dropped,
  depth still tells via Lanchester). Legacy path preserved **verbatim** under `PC_OCTAGON_DMG=0`.
- **I4:** the multiplier runs on both grid+field paths (else field≠grid). Head-on single-subunit rows are
  all-GREEN→mult 1.0→byte-identical; the 3 flanking rows (envelop/cannae/oblique) move. **All 4 `bat.py`
  goldens re-recorded** (ED-909 re-baseline precedent). No constant tuned to the gauge (anchors are Jordan's
  stated design values).
- **Tests:** `tests/valoria/test_octagon_damage.py` (5) — 2.0× rear ratio, front never > rear (local-centroid
  fix), rear penalty persists across the reaction window, seen-flank stamps the reaction clock, multi-side
  shock present. Full `tests/valoria` green.
- **Disclosure:** `audit/2026-07-22-mass-battle-stress-test/octagon_damage_model.md`.
- **Follow-on:** graded ≥2/3/4-side escalation; full-campaign A/B of the default-ON flip once ED-MB-0016
  friction + the conjunctive-envelopment gate land (all three interact on the envelopment rows).

## 2026-07-22 — ED-MB-0017: multi-unit deployment geometry + envelopment pathing fix
- Jordan-flagged from the hierarchy snapshot (overlapping subunits; "double envelopment" with both wings
  on one side; refused flank level with the line). Root cause: `build_army` deployed subunit i at
  `col=15+i*4` (fixed step < subunit frontage).
- **Fix (P-1/P-2/P-3):** `_spec_span` + `_centered_line_cols` (frontage-aware, anchor-centred, provably
  non-overlapping 1–11 subunits, fit-to-field so over-wide armies degrade to overlap instead of crashing
  off-board); `build_envelopment` symmetric opposite-flank wings (mirror double envelopment);
  `build_refused_flank` echeloned-back refused wing.
- **Speed (P-4, Jordan):** envelopers must be fast or they arrive piecemeal. `PC_ENVELOP_SPEED_MULT=2.0`
  (envelop/sweep maneuver = rapid flanking march) + `PC_CAVALRY_SPEED_MULT` 2.0→3.0 (cavalry ~3× an
  infantry march). Measured infantry 1.0 / cavalry 3.0 / cavalry-envelop ~6.0 cells/tick → cavalry double
  envelopment wraps behind by ~t6–8 (was t16–20). Both inert for line-vs-line battles.
- **Adversarial critic (independent):** F1 over-wide-army crash FIXED (fit-to-field, 0/200 fuzz crashes) +
  F2 `gauge_mb.make_mixed_unit` same defect FIXED + F3 odd-wings tested + F4 refused-dynamic tested; F5/F7
  nits follow-on; F8 no-overlap verified sound by construction.
- **Machine-vision comparison:** `research/diagrams/mass_battle_formations/` (schematic vs sim tick-by-tick,
  rendered PNGs + sources).
- **Tests:** `tests/valoria/test_deployment_geometry.py` (16). **I4:** 7 single-subunit byte-exact rows
  unchanged; 3 multi-subunit rows re-baselined in every mode (ED-909 precedent); all 4 goldens re-recorded;
  byte-exact grid oracle green. **Still open:** horseshoe-not-ring (no cavalry rear-transit), single line
  (no triplex depth-lines), envelopment-not-rewarded outcome (DG-6 / ED-MB-0016). Full detail: ED-MB-0017.


## 2026-07-22 — ED-MB-0016: DG-6 grounded partial resolution — per-battle combat-effectiveness (CEV) friction
- Root cause of DG-6 over-decisiveness confirmed: melee pool sums N independent dice → CV self-averages
  ~1/√N → `compute_degree` deterministic from force ratio → 100%/0% vs historical bands. Fix (grounded in
  two research passes; `dg6_friction_resolution.md`): a per-battle, per-side CEV factor `M ~ LogNormal(0,
  σ²)` drawn ONCE per battle (`orchestration._draw_friction_cev`, lazy) multiplying the subunit combat
  pool (`core/exchange`). Law of total variance → scale-invariant outcome variance (Dupuy CEV / Clausewitz
  friction / stochastic-Lanchester). **σ=1.1 calibrated gauge-INDEPENDENTLY** to the Dupuy DLEDB force-
  ratio curve (57/62/70/82% at 1.2/1.5/2/3:1 vs targets 55/62/70/80). `config.PC_FRICTION_CEV`, **default
  OFF** (byte-exact / I4-safe).
- **Verified** (`test_friction_cev.py`, 7): inert-when-off; drawn once/battle not per-turn; large-force
  2:1 collapses ≥95% without friction, stays banded <90% with it (the fix); I1/I2 hold.
- **HONEST FINDING — necessary but NOT sufficient (ships OFF):** uniform friction moves the 20-row gauge
  6/20 → 4/20 — envelopment (H3/H4) stays ~100% (structural, needs a conjunctive gate) and friction
  BREAKS the Stage E brace repel (C2/C6 REPELLED→NOT-REPELLED). Complete DG-6 resolution = friction +
  conjunctive-envelopment gate + brace-repel preservation (follow-on; ED-MB-0016 needs_jordan). No
  constant tuned to the gauge. Full detail: `dg6_friction_resolution.md`.

## 2026-07-22 — ED-MB-0015: spatial-model v2 Stage F — verification + golden re-record + historical revalidation
- Full verification of Stages D+E (no new mechanics). **I1–I7 all hold**: I1 conservation 0 violations /
  300-battle field fuzz; I2/I6 stress-harness S5 (determinism PASS, mirror |skew|=0/48); I3 no live-path
  position integer; I4 byte-exact grid oracle green; I7 facing-away→0 reach. **Stress harness S0–S5 all
  green** (30 mechanics WIRED, 0 engine failures, all off-by-default gates SAFE). Lanchester exponent
  p=2.50 + depth-2 experiment byte-identical (preserved).
- **Field goldens re-recorded** (grid unchanged, I4): `unit_field 2da5183…` (`--check` verified),
  `cell_field 5f5db96…`.
- **P-DEC-4 historical revalidation** (`gauge_mb.py`, history-grounded bands): pre-D baseline (A–C) =
  **10/20**, v2 (A–E) = **6/20** multi — D+E moved the gauge down 4 rows (authorized re-baseline, but
  material). Dominant failure = **DG-6 over-decisiveness**; root cause confirmed: melee pool sums N
  independent dice → CV collapses ~1/√N (measured 0.89→0.06, N=4→1024) → `compute_degree` deterministic
  from force ratio → 100%/0% vs bands. Stage E win: C2/C6 (Cav vs BRACED) REPEL, matching history.
  Per Jordan directive 2026-07-22, the DG-6 grounded resolution (scale-invariant variance) is **underway**
  as a follow-on ED-MB. Full detail: `stage_F_verification.md` + ED-MB-0015.

## 2026-07-22 — ED-MB-0014: spatial-model v2 Stage E — weapon-class reach + pike troop type
- Stage E of `spatial_model_v2_plan.md` (Jordan P-DEC-1). The flat `REACH_SHORT=0.5` placeholder →
  per-troop-type **front-face reach** (`reach_for`/`TROOP_TYPE_REACH`): non-pole melee 0.1, pole/spear
  0.2, **pike 0.3**, cavalry/knights lance 0.2, ranged 0.1 melee sidearm (projectile band stays
  `VOLLEY_MAX_RANGE`). Feeds `cell_boxes_for → obb_front_reach_overlap` (contact) + `resolve_toi_and_commit`
  (TOI halt).
- **Authored the `pike` troop type** end-to-end: `TROOP_TYPE_STATS['pike']` mirrors heavy_infantry (reach
  0.3 the sole differentiator; provisional-by-analogy — §B.2 has no pike row), a `pike` weapon
  (pole/pierce/heavy, anti_cavalry) in `equipment.weapons`, `('pike','medium')` loadout, ShieldWall/Hold/
  Anvil roles.
- **Reach advantage — MEASURED (the gate):** emerges via the already-wired charge-recoil reach gate
  (`PC_RECOIL_CHARGER_GATE`). Braced pike (0.3) / spear-heavy (0.2) repel a cavalry lance (0.2) — defender
  keeps ~96.7% hp, cavalry recoils to ~88.3% — while braced levy (0.1 < 0.2) is run down (~90.7%). The
  anti-cavalry pike role, emergent from the reach data (before Stage E all reaches were 0.5, so the gate
  fired for everyone).
- **Disclosed finding:** reach differentiation does NOT change symmetric standing melee (pike-vs-levy
  standing == levy-vs-levy) — the exchange is mutual once contact fires; reach only shifts contact timing.
  Reach is a charge/brace lever here, not a standing-melee one. A directional-reach exchange term is a
  possible future increment (pike-pins-forever hazard under halt-on-contact) — flagged for Jordan, not
  introduced.
- **Tests:** `tests/valoria/test_reach_weapon_class.py` (10) — reach map, pike authored, reach-advantage
  emergence, standing-melee independence, I7 facing gate, ranged independence, I1×3 seeds + I2 with pike.
- **I4:** `reach_for` reaches the grid path only via the `'kite'` block; the byte-exact battery fields no
  kite units → grid oracle byte-exact green. **[DG-6, not tuned]** standing-melee A/B (Stage D→E)
  negligible (only rotated Arrowhead shifts). PP-290 meter-scale reconciliation flagged for Stage F. No
  balance constant tuned. Full detail: ED-MB-0014.

## 2026-07-22 — ED-MB-0013: spatial-model v2 Stage D — continuous frontage (last live integer removed)
- Stage D of `spatial_model_v2_plan.md`. The melee Lanchester frontage term `len(set(int_col))` (the
  only integer left on the live position/contact path, per `backwards_analysis.md`) → a **continuous
  OBB front-overlap width**. New `geometry.engaged_frontage(a_boxes, b_boxes, heading)` = the union
  length, along a side's frontage axis (⊥ facing), of each engaged cell body's width-interval clipped
  to the enemy's covered meeting span (pure float projection + interval merge; helpers
  `_project_interval`/`_merge_intervals`/`_interval_union_length`). `_find_contacts_standoff` threads
  `a_front`/`b_front` onto each contact pair; `_lanchester_strength` gains `front_width` that replaces
  the integer count when supplied.
- **Scoping:** the snapped `(rank,file)` cell identities are KEPT — they key the formation-lattice
  casualty/density/stamina substrate (`distribute_casualties`/`col_grid`/`_defender_depth`/
  `_fatigue_sigma`), a discrete troop-block identity (I3 defensible-quantization carve-out), NOT a
  live-position integer. Only the frontage MAGNITUDE moved to continuous.
- **I4:** grid/OFF pairs carry no `*_front` key → `orchestration` passes `p.get(...)=None` →
  `_lanchester_strength` falls back to the integer count byte-exact. **Byte-exact grid oracle green (30
  passed).**
- **Tests:** `tests/valoria/test_frontage_conservation.py` (15) — integer-limit reduction,
  fractional-on-offset, **depth-invariant** (depth-2 no longer collapses/inflates), **frontage-capped**
  (Lanchester stays linear), I1 conservation ×5 seeds, I2 determinism, grid-fallback byte-exact.
  maneuvers/movement/yield: 20 passed / 1 xpassed (pre-existing).
- **[DG-6 DISCLOSURE, not tuned]** A/B (12-seed field battery, stash vs current): axis-aligned symmetric
  meetings **byte-identical**; shift only on offset/rotated/width-asymmetric meetings — Line4-vs-Line2
  wide-attacker overkill softens (A_win 12→10/12, defender hp-retained .452→.487) as its frontage caps to
  the narrow defender's meeting width. Lanchester melee exponent **unchanged** (p=2.50 before/after — the
  pre-existing DG-6 pool-variance artifact is frontage-independent). Field goldens NOT re-recorded (Stage
  F, per plan §7). No balance constant tuned. Full detail: `audit/2026-07-22-mass-battle-stress-test/` +
  ED-MB-0013.

## 2026-07-22 — ED-MB-0012: spatial-model v2 Stage B+C — CIRCLE→OBB contact + collide-not-decelerate
- Stage B+C of `spatial_model_v2_plan.md` (Jordan "Euclidean motion, boxed footprint"). (1) **Analytic
  swept-SAT TOI**: replaced the parked scan+bisection (~200k SAT calls/battle, field path 20–60× slow)
  with a closed-form `_swept_first_overlap_s` — each ≤4 SAT axes is a linear-in-`s` overlap band,
  intersect, first-touch = left edge; O(4)/pair, ~15µs. Verified vs the bisection oracle to **1.7e-15
  over 700 seeded fuzzed pairs** (281 touches, 0 mismatches). (2) **Collide-not-decelerate correction**
  (Jordan in-session: "why decelerate instead of collide? / wouldn't that break charging?"). The plan
  made the TOI **halt** surface == the **contact** surface (reach box) — that DEADLOCKS: cells park on
  the `obb_front_reach_overlap` touch boundary where the strict contact predicate is False, so contact
  never fires (head-on Line-vs-Line froze at gap 1.5, 0 casualties). Fix: hard stop = **BODY vs BODY**
  (unit squares, reach 0); contact stays on the reach box (strictly outside the body), so contact fires
  as bodies close through the reach band. Bodies collide; weapons reach across the gap. Reach throttle
  retired (symmetric body-touch cap). **Charging restored** (`_momentum_speed` reads the pre-cap step;
  under the old reach-stop contact never fired so charge shock never triggered). Verified: head-on closes
  to body-touch and trades casualties; Fast cavalry charge reaches contact, deals more than it takes on
  impact (INF −21 vs CAV −10). Tests: `test_obb_contact_toi.py`(7)+`test_obb_primitive.py`(21)=28 passed;
  mass_battle/field subset 57 passed/0 failed. **I4 grid oracle byte-exact 2 passed** (code runs only
  under `if FIELD_MOVEMENT`, orchestration.py:1405). FIELD goldens re-recorded (`unit_field a73237df`,
  `cell_field 9d0b63b9`) — moves the DG-6-gated Cannae gauge (units that froze at range now engage),
  disclosed, no constant tuned. Departs from the plan's shared-surface premise → Stage C + R1 amended,
  flagged for merge-ratification. Full detail: `audit/2026-07-22-mass-battle-stress-test/` + ED-MB-0012.
## 2026-07-22 — ED-MB-0011: DG-10 field-movement freeze fix + field-based stress test (condensed)
- DG-10 (ED-MB-0007) fixed: `_node_advance` floored sub-Discipline-5 velocity to 0
  (`floor(1*0.7)=0`) → most §B.2 troop types (all disc<5) never closed on the live field path. The
  continuous-velocity accumulator meant to prevent it sat dead in the legacy grid `advance_cells`. Fix
  (Jordan-ruled "fields, not grids. no grids."): FIELD-path `step` is the real velocity (no floor, no
  accumulator; anchor/pos already float, consumer uses `min(step,mag)`); whole velocities stay int so
  disc≥5 is byte-exact, fractions advance at true rate. GRID path untouched (`if FIELD_MOVEMENT`) → CI
  byte-exact still 2 passed; FIELD goldens re-recorded (mirror/ranged byte-identical, 8 decisive rows
  move because units degrading below disc-5 mid-battle used to freeze). maneuvers+yield 12 passed/1
  xpassed. MOVEMENT-only; shifts the DG-6-gated Cannae gauge, no balance constant tuned. Full detail:
  `audit/2026-07-22-mass-battle-stress-test/` + ED-MB-0011.
## 2026-06-15/20 — ED-1013 through ED-1032 (archived — condensed)
- Smooth command-sigma pool + continuous discipline penalty (ED-1013); gauge recalibration (ED-1014);
  cavalry-construction gauge fix, not an engine defect (ED-1015); per-subunit stat/stamina/troop-type/
  rout-morale-discipline lifecycle (ED-1016-1019); a string of bugfixes/wiring closeouts (ED-1020-1027,
  1032) culminating in the formation-drift cell-orphaning fix (ED-1032, first post-baseline digest
  change, Jordan-approved); PP-683 intentionally left unwired (would double-count encirclement lethality
  already delivered via PC_ENVELOP_SHOCK + Lanchester overlap). Full detail: tests/coverage_matrix_archive.md.

## 2026-06-30/07-01 — Re-architecture Stages 1-2 + coordinate-migration DEBT-0/S2/C0-P (archived — condensed)
- Provenance registry seed (ED-1043); bat.py byte-exact digest gate committed (baseline unit=7be8499b/
  cell=1c5b2851); Stage 1a-1g wrapper/core split complete (byte-exact); Stage 2 standalone equipment/
  package (not yet wired into resolution); FIELD_MOVEMENT continuous-speed toggle; abs→orig reverse-
  lookup centralized; Migration DEBT-0 (fabrication-debt resolved honestly, no fabrication); Migration
  S2 (Euclidean distance on the field); Migration C0+COL+G+H+F2+P (the full coordinate-field sequence,
  byte-exact OFF throughout). Full detail: `tests/coverage_matrix_archive.md`.

## 2026-07-01 — gauge_mb.py LIVE port + n=60 + tick-by-tick trace-capture backend (archived — condensed)
- gauge_mb.py ported off the dead exec-shim onto live engine.build_unit/resolve_battle (byte-exact
  reproduces prior OFF baseline 5/13); n=120->60 (Jordan directive, verified identical pass-set);
  fabrication-debt resolved; tick-by-tick trace-capture backend added (zero-cost when off). G5
  byte-exact both modes unchanged. Full detail: `tests/coverage_matrix_archive.md`.

## 2026-07-01 — mass_battle workbench + Stage A: visualizer + true-adjacency stand-off halt (archived — condensed)
- Tick-by-tick visualizer (server + frontend, workbench/) verified live in both grid and field modes;
  Stage A fixed the coordinate-field co-location bug with a new `standoff()` primitive + synchronized
  snapshot (a first-mover-bias bug found and fixed mid-implementation); wired `bat.py`'s golden-digest
  gate into CI. G5 byte-exact both grid modes unchanged throughout. Full detail: `tests/coverage_matrix_archive.md`.

## 2026-07-01/02 — mass_battle Stage B + bias fix + Stage C (archived — condensed)
- Stage B ported facing-slew to the field path; a mirror-matchup first-mover bias was found and fixed
  (synchronized snapshot + halved closing distance); Stage C landed `engine.build_army`, `Order`/
  `check_orders` timed sequencing, and escort/formation-relative positioning (Cannae acceptance test
  verified real lateral wheel movement, zero new flanking mechanics). G5 byte-exact both grid modes
  unchanged throughout. Full detail: `tests/coverage_matrix_archive.md`.

## 2026-07-02 — mass_battle: TOI refactor (archived — condensed)
- Jordan-directed replacement of Stage A/B's halving hack with exact time-of-impact collision solving
  (`resolve_toi_and_commit`) plus reach/facing-gated throttling; 5 real bugs found+fixed. G5 byte-exact
  both grid modes unchanged; mirror cav-vs-cav fully balanced (0-0-30). Full detail:
  `tests/coverage_matrix_archive.md`.

## 2026-07-04 — mass_battle: Cannae gauge audit (ED-MB-0002) ratified; DG-3/DG-4 implemented (archived — condensed)
- ED-MB-0002 ratified (PR #73 merge = ratification, ED-1094 convention). Two bug fixes landed first
  (validators.py ghost-cell construction; orchestration.py float-epsilon pool-floor). Root-cause audit
  (RC-1 through RC-5) found composition-coupling defects in the pool/morale accounting layer explained
  the H3-H6 Cannae-pattern gauge collapse, not the "two racing clocks" theory. Jordan ruled DG-3
  ("intensive, per-troop, bottom-up" pool -- combat pool per cell as per troop type/quality/density,
  not a flat subunit-level split) and DG-4 (per-subunit + whole-unit morale blend, wiring already-
  existing agg_morale/derive_rout/cascade_morale_hit machinery, no new state). Both implemented
  (new `pair_pool_contribution` in core/exchange.py; sibling-morale pull in core/state.py +
  hierarchy/units.py). All 4 `bat.py` digest modes re-recorded (shared, non-gated code). DG-5
  (racing-clocks) closed: a frozen-vs-wheeling-wings ablation showed byte-identical outcomes, refuting
  the theory outright. **Honest result: draws GONE (100%→resolves decisively) but H3-H6/C4 now
  OVERSHOOT their bands in the attacker's favor** instead of landing in them -- not a clean fix, a
  change in failure mode. `tests/valoria` green throughout. Full detail: `tests/coverage_matrix_archive.md`.

## 2026-07-05 — mass_battle: Cannae follow-up audit (ED-MB-0003) — 4 defects fixed, DG-1/DG-3 completed, DG-2 captured as workplan

A fresh Fable-5-led adversarial audit of the already-shipped DG-3/DG-4 fix (ED-MB-0002) found the
"RC-1 is fully fixed, remaining gap is pure DG-1/DG-2" story was **false** — 4 concrete engine defects
survived that fix, plus a harness composition bug. Jordan ruled the 3 open decision gates
(AskUserQuestion) the same session; all fixes + ratified decisions implemented, then independently
adversarially reviewed (2 more real bugs found+fixed in that pass).

**Defects found+fixed:**
- **D1** — `orchestration.py`'s `POOL_VARIANT=="C-ii"` branch applied an outer `a_troops_frac`
  (`troop_count/unit.total_troops()`) multiplier to `a_base` BEFORE `pair_pool_contribution`'s own
  internal per-troop normalization — double-diluting a composed subunit's pool by army-size share on
  top of its own troop density. **Fixed per Jordan's ratified "intensive" pool semantics: removed
  entirely** (still computed/used by the untouched `baseline` variant).
- **D2** — `hierarchy/units.py`'s `_envelop_goal` shared one threshold for its phase-1/phase-2
  transition (no hysteresis) — a wing wheeling to its rear waypoint immediately re-crossed the same
  threshold turning in, yanked back to phase 1, forever. **Fixed** with a one-shot `_envelop_committed`
  latch. A second, related bug (**D2b**) in `_node_advance`'s step formula could freeze a body forever
  within 0.5 combined units of ANY goal (a fixed step overshoots when close, and the old code took no
  action below that threshold) — **fixed** by capping the step at `min(step, mag)`.
- **D3** — `orchestration.py`'s `max(1, math.floor(a_pool_raw+1e-9))` floor resurrected a
  routed/broken atom's pool to 1, letting it keep dealing damage post-rout (§A.12 violation). First-pass
  fix (zeroing `a_pool`/`b_pool` for a dead atom) was **found to be a no-op by adversarial review** —
  `roll_pool`/`_sigma_net_boost` (resolution.py) both independently re-floor their own `pool` arg to a
  minimum of 1 internally, so the zeroed input never reached the actual dice math (confirmed by a
  revert-and-diff test: byte-identical digest with/without the first-pass fix). **Corrected fix** forces
  `a_net`/`b_net` to exactly 0 directly for a dead atom (both SIGMA_HEAD and legacy branches).
- **D4** — `percell.py`'s `distribute_casualties` tracked engaged columns as ONE union across a whole
  Unit, letting an uninvolved subunit (e.g. a wide-placed wing 20+ rows from any enemy) absorb a share
  of a DIFFERENT subunit's (the center's) casualties purely by column coincidence. **Fixed** — engagement
  now tracked per-subunit (`eng_by_sub`), with an `any_engaged` whole-unit fallback preserving the
  original degenerate-case semantics.
- **Harness composition bug** (not an engine defect) — `gauge_mb.py`'s `_envelop_army`/`_refused_army`
  fielded a FULL tier's troops per subunit via the legacy tier path, so a 3-subunit envelopment army
  silently fielded 3x (2x for `_refused_army`) its single-subunit opponent's troops — a side effect of
  the LC-8 migration, making every DG-1 composition question untestable. **Fixed**: both now take a
  `total_troops` param (default = the single-subunit baseline) split via the continuous-scale
  troops/concentration path.

**Jordan's rulings (AskUserQuestion, 2026-07-05), implemented:**
- **DG-3 completion = "Intensive (per-troop, partition-invariant)"** — see D1 above.
- **DG-1 = "symmetric at parity + majority pin cavalry wing so long as bottom-up emergent primitives
  approach"** — `_envelop_army`/`_refused_army` rebuilt at force parity (§ above); infantry rows
  (H3/H5/H6) keep the symmetric center+2-wings shape at parity (`pin_frac=1/3` default); cavalry rows
  (C4/C7) rebuilt as majority (2/3) infantry pin + minority cavalry wings via `wing_troop_type`/
  `pin_frac=2/3`, matching Polybius/Livy order of battle, built entirely from `engine.build_envelopment`
  unmodified.
- **DG-2 = "create as workplan"** — NOT implemented. Captured as
  `proposals/mass_battle_fighting_withdrawal_v1.md` (status PROPOSED): a per-subunit `yielding`
  state, facing preserved toward the enemy (unlike rout), commanded-entry first via a discipline-gated
  `'yield'` order, emergent auto-entry flagged default-off pending measurement, reuses `_kite_goal`'s
  reflect vector + the TOI/halt substrate + ED-MB-0001 §6's path-budget formula (NOT the audit's
  originally-proposed "recoil/knock-back idiom," confirmed to not exist as a displacement primitive).

**Adversarial-review pass (independent) — 2 real bugs found+fixed, rest checked out clean:**
1. D3's no-op (above).
2. `wing_speed`/`speed` kwargs in `_envelop_army`/`_refused_army` never reached `Unit.speed` —
   `Subunit` has no `speed` field at all (per-subunit `'speed'` spec keys were pure dead decoration,
   silently dropped by `build_army`), and the Unit-level `speed` was never forwarded to
   `build_envelopment`/`build_refused_flank`. Fixed: per-subunit `'speed'` keys removed (cleanup); real
   `speed=` now forwarded at the Unit level (the only granularity the engine's pursuit-check logic,
   `orchestration.py`'s `routing_unit.speed`/`victor.speed` checks, actually reads).
3. Everything else checked out clean (D2/D2b, D4, Step-4/5's arithmetic, all 4 digests independently
   re-verified).

**Verification:** all 4 `bat.py` digest modes re-recorded across the sequence of fixes (this touches
shared, non-gated combat-resolution code — same as ED-MB-0002's own landing); `unit`/`cell`/`unit_field`
stayed byte-identical through D2/D3(part 2)/D4 (this battery doesn't happen to exercise those bugs on
those 3 modes); only `cell_field` moved at each PER_CELL-gated step, plus `unit`+`cell`+`unit_field`+
`cell_field` ALL moved once at the Step-4 pool-semantics change (shared, non-gated code). `tests/valoria`:
88 passed, 16 skipped (all pre-existing `numpy`-unavailable skips, unrelated to this change), 1 xfailed
(`test_envelop_reaches_rear_node` — its xfail reason/docstring rewritten to retract the now-falsified
"steering mechanism proven correct" claim and record this session's findings).

**Honest gauge result (multi mode, n=30, final/corrected numbers):**

| Row | Before (ED-MB-0002 baseline) | After (this session) | Band | Verdict |
|---|---|---|---|---|
| H3 | 100% draws | 100/0/0 | 55-72 | WIN-OUT |
| H4 | 90% draws | 86.7/6.7/6.7 (val 92.9) | 45-62 | WIN-OUT |
| H5 | 100% draws | 83.3/0/16.7 (val 100) | 48-62 | WIN-OUT |
| H6 | 100% draws | 96.7/3.3/0 | 48-60 | WIN-OUT |
| C4 | 66.7% (val) | 100/0/0 | 75-95 | WIN-OUT |
| C7 | passing (100) | 100/0/0 | 65-100 | OK |

Draws are **entirely gone** — a real, dramatic change from the 100%-draw lock. But every row now
**overshoots decisively in the attacker's favor** instead of landing in-band (except C7, unaffected by
the composition change, which continues to pass). Full 20-row gauge aggregate: **4/20 → 5/20** passing
(H1,C1,C2,C6,C7 — C1 newly passes; every other previously-failing row, including RC-5's 9 untouched
single-subunit rows, remains failing, now mostly via the same overshoot signature rather than draws or
mixed results). **Not a clean net win or loss — a change in which rows fail and how.**

**New, unresolved finding (not decided, disclosed not chased):** a controlled experiment (co-located vs.
spatially-separated equal-troop subunit splits, both vs. an identical single-subunit opponent) suggests
why: `subunit_combat_pool`'s Command-driven score does not scale by a subunit's own troop share, so
multiple SPATIALLY-SEPARATED attacking fronts (center + 2 wings hitting one defender from different
angles) each roll close to a full, independent combat score at once, tempered only by a small
`ENCIRCLEMENT_PENALTY` tax that falls on the *defender*, not the attacker. Co-located splits stayed
roughly partition-invariant (13-16-1 vs a 14-16-0 mirror baseline); spatially-separated splits did not.
Whether this is a genuine partition-invariance defect or the historically-correct mechanism for why real
encirclements are devastating (bands needing reconsideration instead) is **explicitly left open** — a
new architecture question beyond DG-1/DG-3's scope, needing its own Jordan ruling, not a silent tweak.
**DG-5 correction:** the frozen-vs-wheeling ablation's "no race" null result is RE-CONFIRMED for a
DIFFERENT reason — both configurations' wings never reached contact at all (the now-fixed D2 bug), not
because there was genuinely no race.

Branch `claude/mass-battle-cannae-gauge-dg-rulings`. Next: Jordan's ruling on the partition-invariance
question and on DG-2's build sequencing (workplan doc §4).

## 2026-07-08 — mass_battle: partition-invariance fix (ED-MB-0004) + RC-5 preliminary finding

**Jordan's rulings (AskUserQuestion, 2026-07-08):** the partition-invariance question left open by
ED-MB-0003 = **"genuine defect — fix it"** (not the historically-correct-mechanism reading); DG-2
(fighting-withdrawal/yield) = **"build it now"**; RC-5 triage = **start now, in parallel**.

## 2026-07-08 — mass_battle: DG-2 fighting-withdrawal/yield mechanic, commanded-entry slice built

Jordan ruled DG-2 = **"build it now"**. Built exactly the proposal doc's (`proposals/
mass_battle_fighting_withdrawal_v1.md`) own §4 step 1, the "lowest-risk slice": **state +
commanded-entry only** — no emergent auto-entry (§2.2's second bullet), no "rally"/"pocket" exits
(§2.4, beyond the free "collapse to routed" which needed no new code). Disclosed, not silently
narrowed: whoever continues this should treat emergent-entry/rally/pocket as still open, not covered.

**Built:**
- `Subunit.yielding: bool = False` (new field, default-inert) + a `yield_active` property — the
  single shared gate every consumption site reads: `yielding and eff_discipline >= D_YIELD and
  unit_type != 'ranged'` (discipline-gated + melee-only, per §2.5's anti-abuse requirements; one
  property, not five repeated inline conditions, so the gate can't drift between call sites).
- `'yielding'` added to `_ORDER_SAFE_FIELDS` — a `'yield'` order (`Order('immediate',
  {'yielding': True})`) composes with the EXISTING Stage-C `Order`/`check_orders` machinery with
  zero new order-primitive code, exactly as the doc's §3 table says it should.
- Movement: new `Subunit._yield_goal` (reuses `_kite_goal`'s reflect-through-anchor flee vector,
  always active rather than standoff-band-gated) wired into `_resolve_maneuver_goal` behind
  `yield_active`; step magnitude capped at 1 cell/tick (§2.5's anti-abuse ceiling) at the same site
  `_node_advance` already computes its per-tick step. **Node/field path only** (`_resolve_maneuver_
  goal` is only called from `_node_advance`) — same scope boundary 'envelop'/'sweep' already have;
  the legacy grid `advance_cells` path has its own separate inline dispatch, untouched.
- Facing: a bespoke `yield_active`-gated override at BOTH `cell_facing_vec` write sites (node path
  and legacy grid path), firing **regardless of `PC_FACING_MODEL`** (which defaults OFF) — locks
  facing toward `target_atom`'s centroid even while the anchor moves away. This is the doc's
  "mechanically load-bearing" distinction from rout (which turns away); without this override a
  yielding body would inherit the default raw-movement-vector facing and point in its flee
  direction, reproducing rout's problem.
- Combat pool: `core/exchange.py`'s `subunit_combat_pool` multiplies by `YIELD_POOL_MULT` when
  `yield_active` — "traded ground at a cost", reduced but never zero.
- Anti-abuse: `orchestration.py`'s volley `fire()` refuses to fire for a `yield_active` atom
  (matches the existing 'kite' precedent — already redundant with the melee-only gate, kept for
  defence-in-depth).
- **Both new magnitudes explicitly flagged [CALIBRATED-DEBT]**, per the proposal doc's own §5 (not
  independently derived, reused from the nearest existing precedent, disclosed as such):
  `D_YIELD=3` reuses this file's own `disc_mult` tier break (disc≥5 full speed / disc≥3 0.7x / else
  0.4x — a subunit needs enough order to give ground at all, not the severely-degraded tier);
  `YIELD_POOL_MULT` reuses `PC_SHOCK_HOLD_BRACE` (0.35) verbatim, exactly as the doc's §5 suggested.

**Verification:** all 4 `bat.py` digests confirmed BYTE-IDENTICAL (no re-record needed — `yielding`
defaults False everywhere in the battery, so this is genuinely inert-by-default, not just claimed
to be). New `tests/valoria/test_mass_battle_yield.py` (9 tests): default-inert, discipline gate,
melee-only gate, `_yield_goal`'s flee-vector math, order-safety, pool malus (present/absent), and an
integration test running a real short battle confirming the yielding attacker actually moves AND its
facing vector keeps a non-negative dot product toward its target (stays roughly pointed at the enemy,
not away). Full `tests/valoria` suite: all green, no regressions (see this file's own 2026-07-08
entry above for the exact pass/skip/fail counts, unchanged by this addition).

**Honest measurement (§4 step 2's ask — center-yields-from-tick-0 vs no-yield, n=20, node path,
`build_envelopment` center+2-wings vs a single-subunit Line defender):**

| Configuration | Center hp retained (mean) | Battle turns (mean) | A wins / B wins / draws |
|---|---|---|---|
| No yield (baseline) | 35.8% | 15.65 | 14/0/6 |
| Center orders 'yield' from tick 0 | 40.6% | 16.5 | 0/19/1 |

The center DOES survive marginally better yielding (+4.8pp hp retained) — the mechanism works as
built. But ordering it to yield **unconditionally from the very first tick, for the whole battle**,
collapses the attacking army's win rate from 70% to essentially 0%: a permanently-backpedaling,
pool-discounted center contributes far less offense than the wings' encirclement gains back within
this scenario's timeframe. **This is not evidence the mechanic is broken** — it's the expected cost
of the crudest possible commanded-entry policy (always-on, no timing). Historically, Cannae's yield
was timed to buy exactly enough time for the wings to close, not sustained for the whole battle; this
session did not build or measure a timed/conditional entry (e.g. an `Order` with a `tick:N` trigger,
or an emergent entry keyed to encirclement progress) — flagged as the natural next experiment, not
attempted here. Reported honestly per the doc's own §4 step 2 instruction ("reported honestly
regardless of outcome"), not oversold as "DG-2 helps."

**Not built this pass (disclosed, matching the doc's own staged rollout):** emergent auto-entry
(§2.2), "rally" exit (§2.4's first bullet — morale-recovery-triggered reversion), "pocket" exit
(§2.4's third bullet — blocked-retreat malus removal). The "collapse to routed" exit needed no new
code (existing `derive_rout` fires regardless of `yielding`) and is therefore the only exit path
this build actually has.

## 2026-07-08 — mass_battle: pool abandons Command entirely (ED-MB-0006) — troop type/quality/numbers

Jordan directive (verbatim): "consider abandoning combat pools being related to the commander, and
instead being solely derived from the subunit troop type, quality and numbers." New
`POOL_QUALITY_MODEL` (default ON, `config.py`): base pool = `eff_power x eff_size x
POOL_QUALITY_SCALE` — `eff_power` is the troop-TYPE quality stat (`TROOP_TYPE_STATS`/§B.2, §A.1's
own "Power... determines dice rolled"), `eff_size` is NUMBERS (troops/BLOCK_SIZE, continuously
degrading with casualties), `POOL_QUALITY_SCALE=0.5` renormalizes the product to the historical
T3-baseline magnitude (~8, matching the old command=4/full-cohesion baseline). Discipline/stamina
penalties (`pen`/`stam_pen`) are unchanged. Command is absent from the pool entirely — it still
governs morale, formation-hold speed, order-issuing, and `derive_rout`'s Command-0 condition.
`COMMAND_SIGMA_ENABLED` branches remain selectable (`POOL_QUALITY_MODEL=0`) for A/B. Applied to
both `core/exchange.py:subunit_combat_pool` and `hierarchy/units.py:Unit.base_combat_pool` (the
pursuit/rout path) for consistency. Per Jordan's follow-up ("subunit power is the aggregate or
derivation of cell power"): `eff_power x eff_size` is already exactly that aggregate whenever a
subunit's cells share one troop type (true today — no per-cell troop_type exists yet); documented
as such rather than adding a redundant cell loop, since `pair_pool_contribution`/
`_pair_engaged_troops` already do the real per-cell redistribution for pair-scoped resolution and
will pick up true per-cell power the moment that data exists, no change needed there.

**Verification — all 4 `bat.py` digests re-recorded** (shared, non-gated code): `unit`
d9ca7c7e→444afdd4 is now `d9ca7c7e`, `cell`→`88481bbd`, `unit_field`→`40649feb`, `cell_field`→
`7b3b0a8d` (full hashes in `bat.py`). `tests/valoria`: 121 passed/57 skipped/1 xpassed/7 failed (6
pre-existing `test_names.py` + the expected digest-drift failure now fixed by the re-record) — see
`test_mass_battle_maneuvers.py`'s updated xfail note for the 1 xpass (unexpectedly passing once,
not re-verified across seeds, marker left in place).

**Gauge (multi, n=60): 6/20 → 7/20.** Newly passing: C4 (cavalry envelopment, WIN-OUT before,
now 83.3% — inside its 75-95 band), C5 (shaken-line exploit, now 95%, inside 65-98). Newly
failing/changed: **H4 (the actual Cannae matchup) flips from attacker WIN-OUT to attacker LOSING
badly** (1.7% A / 65% B / 33% draws, was 96.6% A before) — a genuinely mixed, not uniformly
positive, result: giving Size direct pool weight helps the SINGLE-large-subunit cavalry rows
(bigger force = bigger pool, working as intended) but hurts the multi-subunit envelopment-army
rows where the composed army's PER-ATOM numbers are now smaller than the single consolidated
defender's. H1/C1/C3 stay OK-band with mild reshuffled percentages. Single-mode stays 2/20
(structurally uninformative, unaffected).

**Honest, disclosed residual — `lanchester_signature.py`'s law-exponent check.** Melee should
conserve p≤1.4 (linear law); this was tested extensively before landing:
- The PRE-EXISTING Command-driven baseline (`POOL_QUALITY_MODEL=0`, i.e. what was in production
  before today) already **fails this exact check** (p≈1.55) — a previously-undetected gap,
  confirmed unrelated to this session (reproduces identically on the pre-session commit). The
  same baseline's `check_linear` (a 2:1 melee army should win decisively) ALSO fails today
  (big_win=3.0%, i.e. the bigger army loses 97% of the time) — flagged, not chased: a quick trace
  showed this specific check calls `run_battle` for a single 18-tick engagement, which usually
  ends in a draw at this troop ratio (mild ~10-15% casualties either way), so the 3%/97% split may
  be measuring decisive-outcome noise in a rarely-decisive sample rather than a structural defect;
  not confirmed either way, left for whoever next touches this test.
- Under the new model, `check_linear`'s win-rate check now correctly **PASSES** (100% big-army
  win, cas_diff +53.7) — the qualitative "bigger army should win" property is restored. But the
  stricter trajectory-fit exponent check gets WORSE (p≈2.50, not better) — swept extensively
  (sqrt-of-size variant: p≈2.35, barely moved; uniform pool-magnitude scale in
  {1, 0.5, 0.25, 0.2, 0.15, 0.1, 0.0625, 0.03}: plateaus at p≈1.65-1.7 below ~0.15, never reaching
  ≤1.4). Confirmed NOT a Lanchester double-count (disabling `LANCHESTER_ENABLED` entirely leaves
  the exponent completely unchanged at p=2.5) — the amplification is internal to the
  pool→net-successes→`compute_degree` tier→`DAMAGE_BY_DEGREE` pipeline: larger absolute pools have
  proportionally lower variance, so which discrete degree tier (Partial/Success/Overwhelming) each
  side lands in becomes near-deterministic from the pool ratio alone, and that tier assignment
  compounds the ratio rather than passing it through linearly. **Not silently patched** — a uniform
  scale provably cannot fix it (it doesn't change the win/loss ratio the test measures), and fixing
  it for real likely means revisiting `compute_degree`'s threshold logic or the degree/damage
  mapping, not the pool formula alone. Flagged as an open follow-up in `designs/provincial/
  mass_battle_v30.md`'s ED-MB-0006 note and here.

Filed as ED-MB-0006 (supersedes ED-899's Command-only base for the pool term).

