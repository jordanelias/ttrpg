# Fable Logic Audit — mass-battle engine (2026-07-24)

Five Fable-tier read-only adversarial auditors, one per logical lane (resolution, rout/morale,
cell/frontage/geometry, orders/movement, gauge/harness). Every finding below was verified by the
auditor via direct code trace + arithmetic, and several by **live ablation**. Findings are split into
**Part A — defects I introduced this session (ED-MB-0027..0032), fixable now** and **Part B — deep
pre-existing engine bugs (ratification/decision needed)**. Severity in caps.

---

## Part A — MY defects (this session's ED-MB work) — ✅ ALL FIXED (ED-MB-0033, 2026-07-24)

All nine A-findings are remediated and committed under **ED-MB-0033**. Byte-exact preserved (all fixes
live in `PC_*`-gated branches, the campaign-boundary `reset_morale_between_battles`, or a construction-time
validator; bat.py 4/4 modes byte-exact). Honest re-measurement after A1+A2: baseline **5/20**, +stochastic
rout **6/20** (the earlier "8/20" was inflated by A2's dropped guards + A1's P5-cavalry contamination). The
per-finding detail below is retained as the fix record.

Several **contaminated conclusions I already reported** — flagged ⚠ (now corrected in `honest_gauge_readout.md`).

### A1 ⚠ CRITICAL — ED-MB-0027 silently changed gauge cavalry Power 4→5 (gauge lane F1)
Routing `make_unit` through `build_army` sends canonical troop types through `Subunit.of_type`, which
fills the §B.2 preset (`cavalry` power=5) because the spec never carries `power`. The old `build_unit`
path left power=None → inherited unit P4. So the "only density is now matched" claim is **false** — gauge
cavalry became P5 (a chimera: P5/D5/M6). **This contaminates the honest-gauge C-row verdicts** (C1/C2/C5/C6
flip between P4 and P5). Measured (n=60): with P5 C1=45.6 IN / C2=48.3 OUT; with P4 C1=11.7 OUT / C2=3.3 IN.
**Fix:** forward `'power'`/`'discipline'` explicitly in `make_unit`'s spec dict (no-op for infantry;
restores P4 for cavalry). Then re-run the C-battery.

### A2 ⚠ HIGH — `gauge_run.py` re-implements the verdict and drops both guards (gauge lane F2)
My full-gauge runner (`inband = lo<=val<=hi`) omits `gauge_mb.run()`'s `dec_n>0` gate and the
`draw_exp=='low' → draw<30%` gate, and `matchup` returns the sentinel `decA=50.0` when `dec_n==0`. So the
all-draw R3 row (and any draw-flooded row) scores a **false PASS**. **My "5/20 → 8/20" number is inflated.**
**Fix:** call `g.run(...)` or share one verdict function; re-measure.

### A3 HIGH — ED-MB-0032 fractional-pool EV crosses the `net<=0` degree boundary (resolution lane F4)
Adding deterministic `frac·0.4` ahead of the *thresholded* `compute_degree` is a Jensen-gap error:
`P(Failure)` jumps 31.8%→10% between pool 3.0 and 3.000001, and **sub-1 pools can never Fail** (a near-dead
sliver becomes a guaranteed chip-damage machine). **Fix:** realize the fractional die *stochastically* —
roll one extra die with probability `frac` — preserving EV **and** variance **and** the Failure boundary.

### A4 MEDIUM — ED-MB-0032 σ-boost uses `sqrt(pool)` on the fractional pool (resolution lane F5)
The fractional die contributes zero variance, but `_sigma_net_boost` reads `sqrt(pool)` → advantages
over-stated ~38% just below each integer; sub-1 pools get a full one-die σ-conversion. **Fix:** pass
`floor(pool)` (or a smooth sub-1 ramp) to the σ-boost on the fractional path.

### A5 HIGH — ED-MB-0031 stochastic break routs the WHOLE unit via the shared morale pool (rout lane F1)
For a multi-subunit unit whose subunits inherit `unit.morale` (morale=None), `atom.erode_morale(eff+1)`
writes the shared pool negative → in `rout_resolution` every sibling (incl. 0%-loss ones) reads morale≤0
→ all rout. Defeats per-subunit rout. **Fix:** materialize own morale before the punch (`if atom.morale is
None: atom.morale = atom.eff_morale`), then set it ≤0.

### A6 HIGH — ED-MB-0031 cached `_rout_breakpoint` never reset + loss measured from spawn (rout lane F2)
`reset_morale_between_battles` clears `routed`/`broken` but not `_rout_breakpoint`, and the per-subunit
survival fraction uses spawn denominators — so a unit ending battle 1 past ~15% losses auto-routs on the first phase of **every
subsequent battle** with zero new casualties. **Fix:** clear `_rout_breakpoint` (and re-base loss to
battle-start strength) in `reset_morale_between_battles`.

### A7 MED-HIGH — ED-MB-0031 sign error: `erode_morale(eff+1)` with `eff≤−1` RAISES morale (rout lane F3)
When `eff_morale` is already ≤ −1 (reachable via §A.4 stacking), the amount is negative → `erode_morale`
adds → can cancel a unit rout canon already earned. **Fix:** `atom.erode_morale(max(eff+1.0, 0.0))` or set
morale to a small negative directly.

### A8 MEDIUM — ED-MB-0031 `_rout_resilience` reads LIVE discipline, not starting (rout lane F4)
Contradicts its own "stable quality" docstring; the lazy draw happens after phase-1 discipline
degradation, so identical-quality units get different break-point distributions by casualty *timing*.
**Fix:** use `atom.eff_discipline_start`.

### A9 LOW-MED — ED-MB-0030 `own_strength:FRAC` edge cases (orders lane F8/F9)
`FRAC≥1.0` fires at spawn (full strength); `start==0` makes it permanently unfireable AND dams the whole
order queue; the numeric payload is never validated (a typo raises mid-battle, defeating eager
validation). **Fix:** parse+range-check `FRAC` (and other numeric trigger payloads) in `Order.__post_init__`;
guard `start>0`; use strictly-`<`-1 semantics.

**Cleared (my code, verified sound):** ED-MB-0028 `close_ranks` — conservation exact, front-first fill,
emptied cells inert, no frontage inflation. ED-MB-0029 intent term — sign & symmetry correct. Density-match
arithmetic exact (every unit 100/cell). Mirrors unbiased (H1 47.7, C3 48.7 at n=200). `bat.py` genuinely
independent of the gauge. σ constants (`PER_DIE_NET_EV=0.4`, `_SIG`) exact.

---

## Part B — deep PRE-EXISTING bugs (not mine) — need a ratification/decision

Ranked. These predate this session; several are the **root cause of the out-of-band gauge rows**.

### B1 CRITICAL — wedge loses because `_oriented_abs_map` iterates the legacy TIER pattern, not the atom's continuous footprint (geometry lane F1)
`geometry.py:249-257` node branch iterates `oriented_pattern(shape,tier)` while `_node_pos` is keyed by the
continuous `_oriented`/`_build_shape_n` ids. For Arrowhead only **1/6** ids match → contact cells resolve to
`[]` → pool floored (mean 3.14 vs Line 10.9) → wedge 0/100. **Ablation: iterating `_oriented(atom)` moves H2
0/100 → 33/67.** Also corrupts `support_engage_frac`, facing, rotation for any shape whose continuous ids
drift from the tier pattern. **Fix:** iterate `_oriented(atom)` in both branches; skip ids absent from
`_node_pos` (don't default to `(0,0)`).

### B2 CRITICAL — GappedLine over-strong: `col_grid` frozen at SPAWN columns vs live contact files → one-sided fatigue immunity (geometry lane F2)
`build_column_grid`/`_fatigue_sigma`/`update_stamina` key `b.col` by spawn columns; engaged sets are live
node files. Lateral drift (ANCHOR_MAP calibrated for legacy footprints) makes GappedLine's live files ∩
spawn cols = ∅ → its stamina never drains, `_fatigue_sigma≡0` while the Line fatigues to −1.5σ. **Ablation:
zeroing fatigue-sigma flips H7 87/13 → 27/70 and H1 → exactly 50/50.** The "gap advantage" is a frame
artifact. Same drift also (B2b) defeats `distribute_casualties`' engaged-front filter asymmetrically
(geometry F3) and zeroes `_defender_depth`. **Fix:** key column blocks + engaged filters by pattern file
identity through the same live snapping the contact layer uses (rebuild col grid from live file bins per
tick); re-center ANCHOR_MAP for the 6-cell footprints.

### B3 HIGH — the whole octagon/facing damage layer runs on a DEAD spawn-lattice map for every moved unit (geometry lane F6)
`_per_cell_angle_mod`/`_octagon_dmg_mod` open-code abs→orig from `starting_position + cell_offsets`, but
`cell_offsets` are never updated on the field path (movement lives in `_node_pos`). After 2 turns a unit's
spawn map has **zero overlap** with its live cells → every cell falls back to nominal `(advance_dir,0)`
facing → with `PC_OCTAGON_DMG=1` (default) the flank/rear multiplier silently degrades to nominal for
moved units — muting genuine wedge/envelopment geometry (contributes to H2/H4/C-row flatness).

### B4 HIGH — numbers enter casualties twice (superlinear numbers edge) (resolution lane F7)
`casualties = K_LINEAR·lin_b·f(b_deg)` with `lin_b` = engaged frontage×density **and** `b_deg` from a pool
that already scales with `eff_size` (numbers). Same "strength in contact" multiplies damage directly and
improves the degree — contradicts `_lanchester_strength`'s "numerical superiority is a LINEAR edge" claim
(the 2026-07-08 `POOL_QUALITY_MODEL` directive put `eff_size` back in the pool; never reconciled). **Likely
the root of the density over-power the honest gauge flagged.** Decision: which channel owns numbers.

### B5 HIGH — charge-shock/recoil zone reads a non-octagon signal under `PC_REFUSE=1` (default) (resolution lane F1)
`_zb = "GREEN" if b_angle_mod > -0.5` re-bins a bundle that, under `PC_REFUSE=1`, only carries
wrapper/pocket penalties — a plain rear charge yields `b_angle_mod=0` → rear moral-shock ~10× too small,
AND a rear-charged braced wall still recoils the charger (violates ED-1091 `PC_RECOIL_FRONTAL`). **Fix:**
derive the shock/recoil zone from the true arc (`a_arc`/`b_arc`).

### B6 HIGH — multi-side shock / encirclement / fixing computed per cascade SUB-PHASE, not per tick (resolution lane F3)
`resolve_engagements_cascading` splits pairs by depth and calls `resolve_engagements` per group; only
`conv_scale` is precomputed on the full tick. So a front+rear engaged body has 1 face per sub-call →
**multi-side shock never fires** in the encirclement scenarios ED-MB-0018 built it for. **Fix:** compute
`eng_counts`/`_atom_sides`/`_front_fixers` once on the full tick's pairs (as done for `conv_scale`).

### B7 HIGH — `assign_targets 'weakest'` has no liveness filter → locks onto 0-troop corpses (orders lane F3)
Destroyed subunits stay in `unit.subunits` at 0 troops; `'weakest'` returns the corpse every tick →
attackers march to and halt against a dead formation. **Fix:** filter to `troop_total()>0 and not
routed/broken`.

### B8 HIGH — `stance:'hold'` order leaves `_moved_this_turn`/`_prev_offsets` stale → teleport/phantom speed (orders lane F2)
The hold early-return skips the per-tick movement-state reset; `resolve_cross_side_contention` then credits
the holder its last moving tick's speed or reverts it to a stale snapshot (backward teleport). Contradicts
`_ORDER_SAFE_FIELDS`' "no cached state" claim. **Fix:** reset `_moved_this_turn`/`_prev_*` at tick top
before the hold return.

### B9 HIGH — DG-2 yielding is structurally inert: engaged front can't give ground but always pays the malus (orders lane F1)
`halted_cells` freezes every contacting cell before movement with no `yield_active` carve-out, while the
0.35 pool malus applies unconditionally-on-yield → a yielding front fights forever at 35% pool and gives
zero ground (strictly worse than not yielding); `pocketed` never fires. **Fix:** exempt `yield_active`
cells from the halt (or gate the malus on the front actually moving).

### B10 MED-HIGH — retreat/yield-from-contact frozen by a direction-agnostic step cap (orders lane F4)
`step = min(step, dmin-1)` caps by distance-to-enemy even for *separating* motion → an engaged unit ordered
to retreat can't move (node path). **Fix:** apply the cap only to closing motion.

### B11..B## MEDIUM/LOW (catalogued, lower priority)
- Octagon reaction clock is pair-order-dependent + pin check pair-local (Cannae fix-and-flank degenerates) — resolution F2.
- Routed/broken atoms still populate `_atom_sides`/`_front_fixers`/`eng_counts` → a fleeing enemy amplifies allies' damage & "fixes" defenders — resolution F6.
- `_pair_engaged_troops` measures support along formation ROWS regardless of attack direction (flank contact draws spurious support) — resolution F8.
- `enemy_range:D` uses centroid→cell Euclidean, inconsistent with movement/contact Chebyshev → brace/withdraw triggers fire late/never — orders F5.
- `_envelop_committed` / `_escort_engaged` / `pocketed` latches never reset on re-order → stale maneuver state — orders F6/F7/F10.
- `Order` validates field *names* not *values* (`stance:'charg'` KeyErrors mid-battle; `order_target_idx=-1` silently targets last enemy; `instructions` accepts a substring-matching string) — orders F9.
- `distribute_casualties` overkill discards residual → `sum(cell_troops) > hp` — geometry F4 / units.
- hp vs cell_troops ledgers diverge on pursuit + freed-attacker paths (single- vs multi-subunit loss fraction inconsistent) — rout F5.
- "troop-weighted" aggregation + sibling pull weight by STATIC spawn count; `derive_rout` includes routed subunits at frozen negative morale — rout F6.
- §A.4 −3/phase morale cap is per-atom → a homogeneous multi-subunit inherited-morale unit loses up to 3N/phase — rout F7.
- `C6` is a byte-identical clone of `C2` (braced-shallow control doesn't exist); `R3` ranged mirror never fires (hold at 18 rows, volley range 8); explicit wing placements suppress the echelon/apex geometry the H5/H6 rows cite — gauge F3/F4/F6.
- Dead rout/morale config constants (`MORALE_PHASE_CAP`, `ROUT_FLOOR_LOSS_PCT`, `SUBUNIT_ROUT_FLOOR` unenforced) — rout F8.

---

## Recommended fix order
1. **A1 + A2** (honesty — they contaminate the honest-gauge conclusions): forward power/discipline in
   `make_unit`; fix `gauge_run` verdict; re-measure the gauge.
2. **A3 + A4** (fractional pool correctness): stochastic fractional die + σ-boost pool.
3. **A5–A8** (stochastic rout): own-morale materialize, breakpoint reset, sign, discipline_start.
4. **A9** (own_strength validation).
5. **B1 + B2 + B3** (the geometry/octagon frame-mismatch trio) — the real root of the out-of-band rows;
   larger, move goldens, need a ratification call. B4 (numbers double-count) is the density-over-power root.
</content>
