# Digest auditB4

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Scope: 73 files under `.audit/2026-07-22-mass-battle-stress-test/`, `.audit/2026-07-23-*`, `.audit/2026-07-24-*`, `.audit/2026-07-26-*`, `.audit/2026-07-29-*`, `.audit/2026-08-06-*`. Lesser-weight context corpus (CLAUDE.md §3: `.audit/` is hidden, archived-not-canon). Standing orientation, verified once at the working tree: the "field engine" these audits call `tests/sim/mass_battle/` no longer exists there (`tests/sim/` now holds only `gauge_mb.py`, `reverse_pair_symmetry.py`, `v32-combat-balance/`); its code lives in `modules/mass_battle/` (`hierarchy/`, `core/`, `config.py`, `orchestration.py`, `percell.py`, `perimeter.py`). `systems/mass_battle/sim/` still exists (the old wired/grid engine). So paths cited in these audits are mostly stale as paths; the findings must be re-checked against `modules/mass_battle/`.

### .audit/2026-07-22-mass-battle-stress-test/README.md
- **What it is:** Stress-test report for mass battle (field-based engine), 2026-07-22, MB lane, ED-MB-0011 (DG-10 movement-freeze fix) and ED-MB-0012 (spatial-model v2 Stage B+C).
- **Status:** none stated (a report); reading: historical (landed work, PRs #207 etc.); its harness paths are stale.
- **Bears on:** MB
- **Content that matters:**
  - Two mass-battle engines existed and were "unreconciled" (ED-IN-0074 D5): wired `systems/mass_battle/sim/massbattle.py` (no field flags) and the active field engine `tests/sim/mass_battle/` (all flags) :16-26.
  - DG-10: `_node_advance` computed `step = max(0, floor(base*disc_mult)+stance_mod)`; `floor(1*0.7)=0` froze every discipline<5 body (levy, archers, heavy infantry) :46-66. Fix: on the field path, step is the real float velocity; grid oracle (`FIELD_MOVEMENT=0`) untouched :70-86.
  - Wired-engine fix is only a clamp-to-1-cell (`max(1,round(vel))`) that flattens disc 1-4 to the same speed; README admits "stopgap" :28-44, :192-197.
  - S0-S5 harness: 30/30 `MECHANICS` resolve; 0 engine failures over 197 fuzz battles; 77.7% contact; mirror symmetry |skew|=0/48; 12/16 flags WIRED, 4 inert-on-scenario (`PC_BRACE_SETUP_DELAY`, `MORALE_FIX`, `PC_RECOIL_FRONTAL`, `PC_WHEEL`) :134-150 (later audit shows `PC_WHEEL` was a true no-op, see adversarial_deep_audit §5.3).
  - Stage B+C bug: halt surface == contact surface deadlocked head-on lines at gap 1.5, 0 casualties; fix: hard stop is BODY-vs-BODY, contact on the reach-extended box, reach throttle retired :214-244. Swept-SAT TOI closed form verified to 1.7e-15 over 700 pairs :205-212.
  - Remaining v2 stages D (continuous frontage), E (weapon-class reach + pike troop type), F (historical revalidation), G (retire integer engine, route `resolve_mass_battle` onto field engine) :265-267.
- **Conflicts / stale:** `tests/sim/mass_battle/` is gone (verified by `ls`); the two-engine split may or may not still exist (`systems/mass_battle/sim/` is still on disk) [UNVERIFIED which one `resolve_mass_battle` calls today]. Tests it cites exist: `test_body_contact_toi.py`, `test_reach_weapon_class.py` (renamed from `test_obb_contact_toi.py`).
- **Open items:** Stages D-G; 1/197 cell!=hp drift (seed 40) unexplained.

### .audit/2026-07-22-mass-battle-stress-test/adversarial_deep_audit_v1.md
- **What it is:** Deep adversarial audit of the MB engine, five independent critics plus hand verification; 2026-07-24 with later sections to 2026-07-25 (MB lane, ED-MB-0041/0042).
- **Status:** none stated; reading: historical record, partly executed (Tier 0-2 executed in §6-7), Tier 3 listed as Jordan calls.
- **Bears on:** MB, DICE, PROCESS
- **Content that matters:**
  - Dominant failure mode: "machinery that documents itself as working and does not" on a self-referential provenance layer; only 17 of ~92 mechanical magnitudes survive hand verification :1-11, :136-146.
  - Verified defects: `K_LINEAR=12` (all melee casualties) is a fit to superseded output :30-34; discipline degradation fires per 1 cumulative Size lost vs canon "> Discipline this turn" :36-40; converging bodies divided by 1/N (`PC_CONVERGENCE_NORM`) :47-61; Feigned Retreat can never be True (`unit.feigned` only set False) :63-68; gauge runs `kind='multi'` which breaks on first rout so pursuit never exists in measured bands :70-76; C2 and C6 gauge rows are bit-identical experiments :78-83; better armour increases arrow casualties via `volley_hp_scale` :85-89.
  - Reachability: H6 RefusedFlank vs Line produces ZERO combat (60/60 seeds) because file-holding pins subunits to spawn column :201-213; `refuse_range=3` default never fires (needs ~10) :215-220; `PC_WHEEL` defaulted ON and was a no-op :222-225; cascade never forms more than one group so `MAX_SUB_PHASES` never binds :227-231.
  - Jordan ruling 2026-07-24: "we are allowed to break canon values in the pursuit of balancing/tuning" -> a divergence is legitimate if declared; only false `[canonical: ...]` tags are unacceptable; labels GROUNDED / JUSTIFIED / DECLARED-DIVERGENCE / CALIBRATED-DEBT :249-272, :325-337.
  - Tier-2 executed (seven items wired or deleted: `dynamic_facings` deleted, `_front_fixers` hoisted per tick, `cell_last_speed` impulse + charger latch `atom._pressing`, `col_grid` live rebuild, per-tick rout trigger, `PC_WHEEL` wired, `yielding` cleared at battle boundary) :283-345.
  - Reachability sweep: of 10 failing gauge rows, 2 legitimately reachable, 2 only illegitimately (H4 passes Cannae with envelopment pathing OFF; H9 by `K_LINEAR=24`), 6 unreachable by any constants (H6, H10, R1, R3, C2, C6) -> honest constants-only ceiling 12/20 :349-414. C2/C6 braced-wall is a MECHANISM gap (need all-around-brace square), not a magnitude :416-436. Win-share gauge is near-unfalsifiable; casualty/duration banding is the recommended next instrument :407-414.
  - `PC_STOCHASTIC_ROUT` flipped ON (loser casualties 61-87% -> 29-41%) :445-459; `ROUT_CASCADE_FRAC` left inert at 1.0 then (config now holds 0.6, see below) :461-477; per-cell morale flip (`PC_CELL_MORALE`) RETRACTED in §10.5 because `between_turn_recovery`/`reset_morale_between_battles` wrote the scalar that cells stop reading; blocker "scalar-write sweep" :590-632.
  - Methodology lessons recorded: a null result on a gated mechanic means the harness probably never reached it :148-151; sweep over a continuous parameter must be checked against discreteness of what it acts on (0.34 and 0.5 identical, armies have 3 subunits) :479-493; assert identities with `==` not `approx` (1-ulp morale sigma) :625-630.
- **Conflicts / stale:** `tests/sim_verification_ledger.json` deleted as stated (§6); `modules/mass_battle/config.py` now tags those constants `[CALIBRATED-DEBT ... ED-MB-0041 Tier-0.1]` (verified by grep). `ROUT_CASCADE_FRAC` is now 0.6 (ED-MB-0067/0071), no longer inert. `K_LINEAR` still carries a `[canonical: mb_lanchester_design.md ...]` tag at `modules/mass_battle/config.py:512` -- the very false-tag state §6 says is unacceptable, still live (one grep). `DISCIPLINE_LOSS_THRESHOLD = 1.0` still tagged `[canonical: params/mass_combat.md ...]` at config.py:185 (the "Jordan's call" shape divergence of §6 table); `MORALE_EROSION_DAMP = 0.7` at config.py:332 still present.
- **Open items:** Tier 3 design calls (depth cap on support stack, envelopment as morale not damage, cavalry charge refusal, Command sigma ceiling, yield pool split, disengage-and-recharge cycle) :177-187; casualty-banded gauge; scalar-write sweep for per-cell morale.

### .audit/2026-07-22-mass-battle-stress-test/backwards_analysis.md
- **What it is:** Backwards trace of a mass-battle outcome through 128 consumed primitives to inputs, with an integer-snap census, 2026-07-22 (MB lane).
- **Status:** none stated; reading: historical (the contact grid ban was later worked through spatial-model v2).
- **Bears on:** MB, DICE
- **Content that matters:**
  - Layer chain L0 winner <- L1 rout+attrition <- L2 degree x damage (`DAMAGE_BY_DEGREE`, `CASUALTY_SCALE`/`K_LINEAR`) <- L3 pool roll + sigma-leverage <- L4 contact detection <- L5 positions <- L6 inputs :9-72.
  - Contact detection snapped float positions to integer cells (`contact.py:175,292-294`, `units.py:631,1017`); `FIELD_CONTACT=1` is byte-identical to OFF at `CONTACT_REACH=0.0` (earlier claim it was float-native retracted) :37-58.
  - Census separates banned POSITION grids from defensible magnitude floors (casualties, pool, dice) :76-91.
  - Depth-2 test: DG-10 float velocity makes ranks drift so `int(round)` collapses a 2-rank formation to 1 at tick 7; `round(.1)` preserves it :107-127. Lists all sites that must change together and the exact-collision contention site that needs distance co-location :129-137.
- **Conflicts / stale:** line refs are to `tests/sim/mass_battle/` (gone). Superseded by README §7 (OBB + body-stop) for contact; whether `int(round)` snaps still exist in `modules/mass_battle/core/contact.py` [UNVERIFIED].
- **Open items:** "ban grids" refactor steps 1-2 (float contact; route wired engine onto field engine).

### .audit/2026-07-22-mass-battle-stress-test/cannae_bait.py
- **What it is:** Probe script: historical Cannae with a commanded `yielding` Order on the 3 crescent maniples (ED-MB-0041).
- **Status:** none; reading: historical probe, depends on removed `tests/sim/mass_battle.engine` import path.
- **Bears on:** MB
- **Content that matters:**
  - `check_orders` measures subunit CENTROID to nearest enemy cell; `enemy_range:3` never fires, `enemy_range:6` does :1-8.
  - Orders set behavior via generic setattr: `Order(trigger, {'yielding': True})` :22.
  - Runs 25-turn `kind='multi'` battles over seeds 1_000_000+s via `gauge_mb.resolve_battle` :26-36.
- **Conflicts / stale:** imports `mass_battle.engine` via `tests/sim` sys.path; `tests/sim/mass_battle` no longer exists, so it cannot run as is.
- **Open items:** none (result in cell_primitive_damage_v1: bit-identical to baseline).

### .audit/2026-07-22-mass-battle-stress-test/cannae_calib.py
- **What it is:** Calibration script for matched-granularity Cannae compositions against gauge row H3 (band decA 55-72).
- **Status:** none; reading: historical probe.
- **Bears on:** MB
- **Content that matters:**
  - `granular_line` and `cannae` builders (centre + infantry/cavalry wings, force and density parity, 600 troops at concentration 100) :17-54.
  - Compares thin enveloper vs 5/6/7-line and Cannae compositions vs 6-line :71-80.
  - `granular_line_wd` adds explicit width x depth :83-98.
- **Conflicts / stale:** same dead import path as above.
- **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/cannae_historical.py
- **What it is:** Historical-OOB Cannae scenario: 5000 Carthage vs 8600 Rome (1.72:1), Jordan's directive.
- **Status:** none; reading: historical fixture; the best concrete encoding of "match real OOB" in this corpus.
- **Bears on:** MB
- **Content that matters:**
  - Carthage: 3 baiting crescent maniples (600 each, 3x2, hold), 2 African columns (1000, 2x5, envelop), heavy cavalry left 800, Numidian right 400, released by `Order('tick:4', ...)` :19-36.
  - Rome: 3x3 grid of maniples (8000 total) plus two 300 cavalry :38-53; subunit cap 11 per side :4.
  - Acceptance criterion: engine reproduces a Carthaginian win while outnumbered :5-6.
- **Conflicts / stale:** dead import path.
- **Open items:** result reported in cell_primitive_damage_v1 (0% default, 37.5% with all flags ON).

### .audit/2026-07-22-mass-battle-stress-test/cell_primitive_damage_v1.md
- **What it is:** ED-MB-0040 report on the aggregate-smear bug and per-cell damage, with Cannae findings, 2026-07-24.
- **Status:** "BUILT + GATED OFF (`PC_CELL_DAMAGE=1`), byte-exact when off. Measured, not yet default."; reading: historical (later default state [UNVERIFIED]).
- **Bears on:** MB
- **Content that matters:**
  - Bug: `_octagon_dmg_mod` averaged per-cell arcs into one scalar then `distribute_casualties` spread losses by density only, so envelopment could not strip a formation shell-inward :9-22.
  - Fix: `_octagon_cell_mods` single owner; per-cell allocation weights; pair total unchanged :24-34. Envelop-vs-3-command-line side-symmetric avg 43.8% -> 57.8% (in 55-72 band); full gauge 8/20 -> 4/20 because bands were fitted to the smear :36-53.
  - Historical Cannae: 0/20 with defaults; 12 of 33 boolean flags defaulted OFF; with ALL flags ON 37.5% (A 20 / B 55); `PC_FRICTION_CEV` is the only flag with resolvable effect (41.7% vs 2.5%) :142-191. Leave-one-out ablation: seven flags exact zeros :193-221.
  - Jordan's Cannae spec: centre defensive, advance-bait-withdraw, cavalry must be fast; "pathing timing is huge"; win iff `t_cavalry_reaches_rear < t_centre_routs` :112-135.
  - CORRECTION: DG-10/ED-MB-0024 `yielding` already is the deliberate fighting withdrawal; entry is commanded-only; auto entry at `frac<0.50` too late :236-261. Bait A/B bit-identical; unit test shows yield pool malus `YIELD_POOL_MULT` 0.35 makes the yielding centre 3x WEAKER (pool 12->4), backwards for Cannae; proposal: split into offence malus and survivability term >= 1.0 :275-337. `PC_FEIGNED_RETREAT` only call site is post-rout pursuit :209-217, :270-273.
- **Conflicts / stale:** `YIELD_POOL_MULT` is still `[CALIBRATED-DEBT]` in `modules/mass_battle/core/exchange.py:29` (verified), i.e. the split proposal appears unexecuted [UNVERIFIED beyond that line].
- **Open items:** "re-baseline with full-kit profile vs byte-exact legacy profile" separation; re-test all 20 precedents against real OOBs; yield pool split.

### .audit/2026-07-22-mass-battle-stress-test/close_ranks_probe.py
- **What it is:** ED-MB-0028 probe: does cell-level close-ranks change outcomes (deep column vs wide-shallow line at equal troops and density), flag off vs on via subprocess.
- **Status:** none; reading: historical probe, import path dead.
- **Bears on:** MB
- **Content that matters:**
  - Flag `MB_CLOSE_RANKS` is import-time so the probe spawns a subprocess per value :43-46.
  - Matchups DEEP(4x3) vs WIDE(12x1), DEEP(3x4) vs SEMI(6x2), mirror(6x2), n seeds from 1_000_000 :35.
- **Conflicts / stale:** `MB_CLOSE_RANKS` env name vs later `PC_CLOSE_RANKS` naming [UNVERIFIED which survives]; `tests/sim/mass_battle` import gone.
- **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/cluster_probe.py
- **What it is:** Envelop-cluster measurement with matched 3-command (wing-centre-wing) defenders at constant density, bands H1-H6/H10/H11.
- **Status:** none; reading: historical probe.
- **Bears on:** MB
- **Content that matters:**
  - Gauge rows and bands used: H3 55-72, H4 45-62, H6 48-60, H10 28-45, H11 38-55, H5 48-62, H1 42-58, H2 48-62 :46-54.
  - `tri_line` builds a shape as 3 equal subunits at `GAUGE_CONC`/`GAUGE_TROOPS` :12-27.
- **Conflicts / stale:** dead import path; needs `tests/sim/gauge_mb.py` (exists) plus `mass_battle.engine` (gone).
- **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/depth_factorial.py
- **What it is:** Factorial probe: thin enveloper vs Line built as 1/3/6 subunits x depth 1/2/3, band 55-72.
- **Status:** none; reading: historical probe.
- **Bears on:** MB
- **Content that matters:**
  - Uses `cannae_calib.granular_line_wd`; width=1 required together with depth for depth to take effect :23.
- **Conflicts / stale:** dead import path.
- **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/depth_probe.py
- **What it is:** Depth-vs-width probe: does depth confer reserve/staying power or is frontage pure width (equal troops, 100/cell).
- **Status:** none; reading: historical probe; answer recorded elsewhere (depth gives no holding power without frontage).
- **Bears on:** MB
- **Content that matters:**
  - Reads `MB_FRONTAGE_BLEND`, `MB_FRONTAGE_REF`, `MB_DEPTH_ROTATE`, `PC_FRONT_RANKS` config knobs :45.
  - Cases: 6x4 vs 24x1, 4x6 vs 24x1, 3x8 vs 24x1, plus mirror controls, 2400 troops each :47-51.
- **Conflicts / stale:** dead import path; flag names may have changed.
- **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/dg6_friction_resolution.md
- **What it is:** ED-MB-0016 design/validation doc: scale-invariant per-battle combat friction (lognormal CEV) to fix mass-battle over-decisiveness (DG-6), Jordan-directed 2026-07-22.
- **Status:** "PROPOSED (grounded + calibrated + gauge-validated). ED-MB-0016."; reading: historical, mechanism built gated OFF (`PC_FRICTION_CEV`); the main finding is later re-used (cell_primitive_damage: CEV is the only resolvable flag for Cannae).
- **Bears on:** MB, DICE
- **Content that matters:**
  - Root cause: summing N i.i.d. per-soldier dice self-averages (CV 0.89 at N=4 to 0.06 at N=1024), so large battles resolve to a fixed tier from force ratio :14-31.
  - Model: `M_side ~ LogNormal(0, sigma^2)` drawn once per battle per side, multiplies the combat pool (Dupuy CEV); law of total variance keeps outcome banded :33-53.
  - Calibration against independent Dupuy DLEDB attacker win rates (55/62/70/80% at 1.2/1.5/2/3:1): `PC_FRICTION_SIGMA=1.1` reproduces 57/62/70/82 :94-114.
  - Implementation: `_draw_friction_cev(unit)` once per battle lazily, multiplies `subunit_combat_pool` `raw *= unit._friction_cev`; grid oracle pins it 0 :116-127.
  - Gauge A/B 6/20 -> 4/20; friction breaks near-deterministic brace repel (C2/C6 attacker win ~5% -> ~35%) and leaves envelopment ~100%; follow-ons: conjunctive envelopment gate, brace-repel exemption :129-160.
- **Conflicts / stale:** cites `test_friction_cev.py::test_variance_does_not_collapse_at_scale` [UNVERIFIED present]. Cell_primitive_damage later shows friction ON is the key Cannae lever; the "ships OFF" status may have changed [UNVERIFIED].
- **Open items:** conjunctive envelopment gate; brace-repel preservation under CEV.

### .audit/2026-07-22-mass-battle-stress-test/envelop_probe.py
- **What it is:** Diagnostic: monkeypatches `resolve_engagements_cascading` to record which faces of a defender atom are struck and whether multi-side shock eligibility (>=2 faces/tick) occurs in H3.
- **Status:** none; reading: historical probe.
- **Bears on:** MB
- **Content that matters:**
  - Re-derives nearest face (F/B/L/R) of the defender from attacker centroid :13-24; counts ticks with non-front contact and with >=2 faces :36-61.
- **Conflicts / stale:** dead import path.
- **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/envelopment_stability_diagnosis_v1.md
- **What it is:** ED-MB-0039 diagnosis of the H3/H10 side asymmetry after matched command granularity (ED-MB-0038), 2026-07-24.
- **Status:** "DIAGNOSTIC + engine-design fork flagged for Jordan."; reading: partially superseded by cell_primitive_damage_v1 (the smear bug was the cause; "engine gap" reframed).
- **Bears on:** MB
- **Content that matters:**
  - Same armies, sides swapped: enveloper wins ~71% as A, ~17% as B (54pp swing); mirrors symmetric; cause is deployment-parity knife edge amplified by Lanchester feedback; side-symmetric avg ~44% :13-30.
  - Three regimes: pure infantry (chaotic ~44% avg), deep-narrow centre (stable but loses, ~15%), combined arms with cavalry orbital wheel (stable ~93-100%) :32-52.
  - Fork: (A) reframe H3/H4 as combined-arms, or (B) add moderate-envelopment seal-failure/breakout variance (recommended) :63-81.
  - `width`/`depth` take effect only when BOTH keys set (width alone silently ignored) :40-41.
- **Conflicts / stale:** the "engine gap" conclusion was overturned by ED-MB-0040 (cell-primitive damage) per cell_primitive_damage_v1 :61-64.
- **Open items:** the fork (A vs B) was never answered in this file; a moderate-envelopment mechanism.

### .audit/2026-07-22-mass-battle-stress-test/envelopment_stability_probe.py
- **What it is:** Script behind the diagnosis: pure-infantry vs deep-narrow-centre vs combined-arms enveloper, env-A vs env-B swing.
- **Status:** none; reading: historical probe.
- **Bears on:** MB
- **Content that matters:**
  - Docstring restates the three conclusions :1-14; `deep_env` builder with `Order('tick:N', ...)` wing release :23-36.
- **Conflicts / stale:** dead import path.
- **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/fable_logic_audit_v1.md
- **What it is:** Five Fable-tier read-only logic audits (resolution, rout/morale, cell/frontage geometry, orders/movement, gauge/harness), 2026-07-24; Part A own defects (fixed under ED-MB-0033) and Part B pre-existing bugs.
- **Status:** Part A "ALL FIXED (ED-MB-0033, 2026-07-24)"; Part B open at time; reading: historical, partly executed.
- **Bears on:** MB, DICE
- **Content that matters:**
  - A1: routing `make_unit` through `build_army` silently made gauge cavalry Power 5 instead of 4; C-row verdicts flip with it (C1 45.6 IN at P5 vs 11.7 OUT at P4) :21-28. A2: `gauge_run.py` re-implemented the verdict dropping `dec_n>0` and draw gates, falsely passing all-draw R3 :30-34.
  - A3 fractional pool EV crossing the `net<=0` Failure boundary (Jensen gap; sub-1 pools never Fail) :36-40; A5 stochastic break routed the WHOLE unit via shared morale pool; A6 `_rout_breakpoint` never reset :47-58.
  - B1 CRITICAL: wedge loses because `_oriented_abs_map` iterates the legacy tier pattern not the continuous footprint (1/6 ids match for Arrowhead; fix moves H2 0/100 to 33/67) :86-92. B2 CRITICAL: `col_grid` frozen at spawn columns gives GappedLine one-sided fatigue immunity; zeroing fatigue sigma flips H7 87/13 -> 27/70 :94-102. B3: octagon/facing layer reads a dead spawn-lattice map for moved units :104-109.
  - B4: numbers enter casualties twice (frontage x density AND pool by `eff_size`) -- likely root of density over-power; B5 charge-shock zone uses non-octagon signal under `PC_REFUSE=1` :111-122. B6 multi-side shock computed per cascade sub-phase (later fixed per adversarial_deep_audit §7). B7 `assign_targets 'weakest'` locks onto 0-troop corpses; B8 `stance:'hold'` leaves stale movement state; B9 yielding structurally inert (halted cells never give ground, pool malus applies) :124-146.
  - Lower items: `Order` validates names not values; `enemy_range:D` uses centroid Euclidean vs Chebyshev contact; dead constants `MORALE_PHASE_CAP`, `ROUT_FLOOR_LOSS_PCT`, `SUBUNIT_ROUT_FLOOR` :151-163.
- **Conflicts / stale:** B6, B2 (col_grid) fixed by adversarial_deep_audit Tier-2; status of B1, B3, B4, B7-B10 at the working tree [UNVERIFIED; each needs a grep in `modules/mass_battle/`].
- **Open items:** B1/B3/B4/B7/B8/B9/B10 ratification calls not recorded as resolved in this file.

### .audit/2026-07-22-mass-battle-stress-test/fiat_register_v1.md
- **What it is:** Nine-agent adversarial register of every "fiat" (hard-coded imposition against emergence) in the MB engines plus measurement-harness fiats, 2026-07-23, Jordan-directed.
- **Status:** "AUDIT (adversarial, 2026-07-23)"; reading: historical register; several items fixed since, the headline G1 may still be live.
- **Bears on:** MB, CORE, SE, DICE
- **Content that matters:**
  - Headline §0b/§9: campaign-called `resolve_mass_battle` (integer engine, `systems/mass_battle/sim/massbattle.py`) collapses every faction into an identical Line/tier-2/cmd4/disc5/morale5 single-subunit shell differing only by `power=int(Mil)`; one 18-tick skirmish; terrain ignored; results bucketed at 0.75/0.50/0.25; `_GarrisonStub Mil=1.5`, `LETHALITY_SCALE=1.25` :16-29, :244-259.
  - M1 (CONFIRMED): per-cell density mismatch between constructors (16/cell vs 133-200/cell at equal troops) drove H3/H4/H5/C4/C7 over-decisiveness; dense-vs-thin line, no envelopment, wins 100% :53, :287-302. `_lanchester_strength` makes density linear in power (`core/attrition.py:42`) :130-141.
  - Variance fiats: rout deterministic cliff at 50%/25% triggers, hard `compute_degree` tiers, flat `DAMAGE_BY_DEGREE`, pool floors :74-88. Double-counts: `MULTI_SIDE_SHOCK=0.5` uncapped on top of octagon 2x; charge-shock sigma ceiling really 1.76 vs documented 0.55 and crowds out other sigma channels (shared softcap suppresses co-occurring channels 77-91%) :92-129, :298-303.
  - Scripting drift: maneuver goals as two-phase waypoint recipes keyed by `'envelop' in instructions`; `PC_ENVELOP_SPEED_MULT=2.0`; `PC_CAVALRY_SPEED_MULT=3.0` keyed on type strings; `MIN_DISCIPLINE` by shape name :145-168.
  - False positives not to fix (would fork canon): `compute_degree` tiers (PP-232), octagon 1.0/1.5/2.0 + `MULTI_SIDE_SHOCK` (Jordan's directive ED-MB-0018), 50/25% morale triggers (canon §A.4 ED-1019), `CELL_FLOOR/CELL_CAP` values :332-341. M3 (Arrowhead COM offset) FALSIFIED by A/B :63-70.
  - New bug: `build_envelopment` wings positioned relative to a phantom centre column (wings land 12-18 columns from centre) :317-323. Sequencing: do not stack CEV friction and a distributed rout breakpoint at once :343-348.
- **Conflicts / stale:** G1/G2 (faction-blind integer engine) is the key claim to re-check at the working tree: does the season loop still call `systems/mass_battle/sim/massbattle.py` via `modules/mass_battle/massbattle.py`? [UNVERIFIED]; `resolve_mass_battle`/`_faction_to_unit` grep owed. Later work (rout, per-cell) overtook V1.
- **Open items:** all of §8 steps 4-7 (continuous `DAMAGE_BY_DEGREE`, brace-repel, de-fiat scripted maneuvers, Stage G wiring).

### .audit/2026-07-22-mass-battle-stress-test/flag_ablation.py
- **What it is:** Leave-one-out flag ablation on historical Cannae OOB with `MB_FRICTION_CEV` pinned ON.
- **Status:** none; reading: historical probe.
- **Bears on:** MB
- **Content that matters:**
  - Flag roster: `MB_CELL_DAMAGE, MB_CLOSE_RANKS, MB_FEIGNED_RETREAT, MB_FRACTIONAL_POOL, MB_FRICTION_CEV, MB_INTENT_RESOLUTION, MB_RESERVE_COMMIT, MB_STOCHASTIC_ROUT, MB_TROOP_DENSITY_CAP, MB_YIELD_EMERGENT, MB_YIELD_POCKET, MB_YIELD_RALLY` :8-10.
  - Tags rows LOAD-BEARING / COSTLY / neutral by +-1pp, which at n=12/side is under one-battle resolution (4.2pp) :59.
- **Conflicts / stale:** env names `MB_*` differ from `PC_*` used in the narrative [UNVERIFIED which config reads]; dead import path.
- **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/gauge_run.py
- **What it is:** Full honest-gauge runner delegating to `gauge_mb.run()` (A2 fix).
- **Status:** none; reading: historical helper.
- **Bears on:** MB
- **Content that matters:**
  - Documents that an inline `inband = lo<=val<=hi` dropped `dec_n>0` and draw gates so all-draw rows scored a false pass (10 of 20 bands contain 50) :16-20; "one rule lives once" -> verdict lives only in `gauge_mb.run` :20.
- **Conflicts / stale:** dead `mass_battle.config` import.
- **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/granularity_probe.py
- **What it is:** Probe: is the H3/H4 envelopment inversion a defender-granularity artifact (monolithic 600-troop line vs split into 3/6/9 subunits).
- **Status:** none; reading: historical; its hypothesis was confirmed (ED-MB-0038).
- **Bears on:** MB
- **Content that matters:**
  - Hypothesis: flank/rear damage dilutes across a monolithic subunit's whole pool so it never routs :1-4.
- **Conflicts / stale:** dead import path.
- **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/full_implementation_plan_v1.md
- **What it is:** Steering plan for the multi-stage MB fix effort (Part-A flips, Part-B fixes, per-troop damage model), Jordan directive 2026-07-24 "implement all proposals. nothing is golden here."
- **Status:** "PROPOSED (steering surface for the multi-stage effort)"; reading: historical plan (one of several superseded by the 2026-07-26 plans below).
- **Bears on:** MB, DICE
- **Content that matters:**
  - Regime inversion: the 20-row Dupuy/Sabin gauge is the primary oracle; goldens (`bat.py`) become re-recorded snapshots; every `PC_*` flag kept for A/B :8-18.
  - Per-troop damage primitive: `per_troop_emission = f(weapon, quality, intent, morale)`; degree channel carries quality (sigma head), magnitude channel carries count (density x engaged frontage) LINEARLY; count must not enter the degree (resolves B4) :20-46.
  - Phase order: 0 repair the ruler, 1 geometry frame (B1+B2+B3+B5 must land together: B1 alone regresses the braced-wall C-rows because brace repel relied on the broken (0,0)-collapsed contact map), 1.5 systemic finding (wings reach flanks L/R but NEVER rear B face; envelopment delivers 0% at matched density), 2 damage model + lethality re-baseline ("far too much damage too quickly"; target 30-90 min battles, rout across 15-30%), 3 orders/charge/movement, 4 flag flips one at a time, 5 rotation deferred, 6 validation :48-140.
  - Decisions locked: B4 numbers -> casualties-only linear behind toggle `MB_NUMBERS_MODEL` (default `linear`); `PC_*` flags kept; rotation deferred :142-145.
- **Conflicts / stale:** the Phase-1.5 "envelopment 0%" reading was before cell-primitive damage (ED-MB-0040); superseded in sequence by 2026-07-26 plans (execution plan, completion plan v4) [UNVERIFIED which is the last word].
- **Open items:** `MB_NUMBERS_MODEL` toggle and the B4 numbers-model decision.

### .audit/2026-07-22-mass-battle-stress-test/geometric_contact_proposal_v1.md
- **What it is:** Proposal to de-grid the field engine: weapon-based melee reach, geometric contention, geometric engaged-cell recording (2026-07-22, Jordan design).
- **Status:** "PROPOSED (Jordan design, live)"; reading: partly superseded (README §7 landed OBB body-stop; weapon reach landed as `test_reach_weapon_class.py`).
- **Bears on:** MB
- **Content that matters:**
  - `CELL_RADIUS = 0.5` (circular cell, Jordan-confirmed), `standoff = (CELL_RADIUS+reach_a)+(CELL_RADIUS+reach_b)`; contention already geometric via TOI halt on the field path (contention resolved 0 over 30 ticks, TOI 30x) :8-30.
  - Only remaining live integer on the field path: engaged-cell recording (`contact.py:292-293`), consumed by casualty columns and Lanchester frontage :22-25.
  - Proposed weapon reach: non-pole melee 0.1, pole 0.2, pike 0.3, ranged = projectile range; replaces coarse `REACH_SHORT=0.5 / REACH_LONG=1.5` :51-65.
  - Kinematics: standard travel/tick = one cell diameter = one lattice pitch; area 1, density = troops :31-42.
- **Conflicts / stale:** README §7 changed circle to OBB boxes; the Jordan "circular cell" ruling here was overtaken by the "Euclidean motion, boxed footprint" direction (spatial_model_v2_plan). Reach nit vs PP-290 meter grounding noted in historical_fidelity_readiness.
- **Open items:** weapon-reach table adoption confirmation [UNVERIFIED in `modules/mass_battle/config.py`].

### .audit/2026-07-22-mass-battle-stress-test/hierarchical_units_investigation.md
- **What it is:** Jordan-directed investigation (2026-07-22) mapping cell -> subunit -> army onto the Football Manager / Total War paradigm.
- **Status:** none (investigation); reading: historical but accurate on structure.
- **Bears on:** MB, CHAR, GO
- **Content that matters:**
  - Three levels: `Subunit` cells with `cell_troops`/`cell_facing_vec`, `hierarchy.units.Unit` army; `footprint_for(shape, troops, concentration)`, `CELL_FLOOR(40)..CELL_CAP(200)` :14-27.
  - Armies are emergent compositions (ED-909/LC-8): only Line/Arrowhead/GappedLine/Column are subunit shapes; `build_army`, `build_envelopment`, `build_refused_flank` :29-42.
  - Three instruction layers: army stance, subunit `instructions` (brace, hold, charge, advance, envelop, pin, screen, pursue, yield, kite, loose, harass, lure, volley, shoot_move) + `role`, timed `Order` triggers (`immediate|tick:N|enemy_range:D|ally_at:D`) :44-61.
  - Gaps: legibility needs many cells (150-200 troops = 1-2 cells); cells homogeneous (no per-cell type/power/discipline, "per-cell type doesn't exist yet"); no named army formation object; subunit cap 11 (ED-1090) vs Command clamp 1-7 implies an unbuilt subordinate-officer mechanism :78-99.
- **Conflicts / stale:** `modules/mass_battle/hierarchy/units.py` now holds the classes; officers exist now (`test_mass_battle_officers.py`) so gap 4 may be closed [UNVERIFIED].
- **Open items:** min cells per subunit or sub-cell rendering; named army formation authoring/UI.

### .audit/2026-07-22-mass-battle-stress-test/historical_fidelity_readiness.md
- **What it is:** Consolidated audit and roadmap on whether the field engine can reproduce Cannae/Leuctra/Gaugamela/Zama, 2026-07-23.
- **Status:** none; reading: historical snapshot with a still-useful capability-gap list.
- **Bears on:** MB, WR
- **Content that matters:**
  - Verdict: primitives and aggregation spine sound and cell-up; fidelity ceiling is three missing capability layers plus DG-6 variance structure :9-15.
  - Architecture table: maneuver goals (`_envelop_goal`/`_sweep_goal`) are the one SCRIPTING-DRIFT debt; `perimeter_targeting_geometry_v1` would retire it :17-31.
  - Capability gaps: (1) concurrent multi-body engagement and cavalry rear transit (`proposals/multiunit_envelopment_plan.md`, Path B, never started), (2) multi-line depth / triplex acies reserves, (3) elephants and chariots with lane channeling :54-62.
  - Granularity adequate: DG-6 is a variance-structure problem, discrete and continuous engines distribution-equivalent; puncture `int()`-floor is a leak :33-44.
  - Roadmap P0 CEV friction + conjunctive envelopment gate + exchange-ratio band; P3 Stage G route `resolve_mass_battle` + `faction_action` onto the field engine (P-DEC-2) "until this lands none of the above is live in the game path" :88-109.
- **Conflicts / stale:** check whether `proposals/multiunit_envelopment_plan.md` exists [UNVERIFIED]; Stage G status at the working tree needs a grep of the season loop's mass-battle seam.
- **Open items:** the three capability layers; reach 0.1/0.2/0.3 vs PP-290 meter-grounding reconciliation; command clamp vs cap.

### .audit/2026-07-22-mass-battle-stress-test/honest_gauge_readout.md
- **What it is:** Readout of the 20-row historical gauge after measurement-integrity fixes (ED-MB-0027 density constant, ED-MB-0031 stochastic rout, ED-MB-0033 corrections, ED-MB-0038 matched granularity, ED-MB-0039 caveat), 2026-07-23 to 07-24.
- **Status:** "DIAGNOSTIC (the gauge now flags engine divergence honestly; bands NOT re-fit)"; reading: historical, layered corrections.
- **Bears on:** MB, DICE
- **Content that matters:**
  - Fix: hold per-cell density constant at `GAUGE_CONC=100`, `GAUGE_TROOPS=600` so splits divide evenly; the gauge (`tests/sim/gauge_mb.py`) is a manual harness, not a pytest/CI gate :16-27.
  - Honest gauge baseline 5/20 (H1, R1, R3, C5, C7); with `PC_STOCHASTIC_ROUT` 6/20 after Fable A1/A2 corrections (earlier "8/20" inflated by P5-cavalry and the all-draw R3 false pass) :54, :141-171.
  - Depth-reserve works: narrow-deep column beats wide-shallow 24x1 100% at equal troops/density (later contradicted by the adversarial audit §2 on unbounded depth killing power) :63-72.
  - Matched command-granularity: defender with 1 command (monolith) 0%, 3 commands ~53-71%, 6 ~95%, 9 100% -- a monolith is unbreakable by envelopment because casualties dilute over its HP pool; `_command_army(shape, n_cmd=3)` is "triplex acies" :173-196 (adversarial audit §2 notes `n_cmd=3` is a free parameter and triplex acies is a depth, not abreast, arrangement).
  - Intent as first-class resolution axis (Jordan 2026-07-23): `stance` only changes movement speed (`STANCE_SPEED_MOD`), not trade quality :87-93; Cannae needs deep holding centre, backward pathing as an order :94-100; wide-mirror asymmetry 55-57% A at width>=12 :104-106.
  - Naive persistent defender reface refuted (95 -> 100) :199-202.
- **Conflicts / stale:** contradicted/qualified by adversarial_deep_audit_v1 §2 (n_cmd=3 free parameter) and cell_primitive_damage (smear, not engine gap).
- **Open items:** side asymmetry in reverse rows; H4/H5/H6 misses; box brace for C2/C6.

### .audit/2026-07-22-mass-battle-stress-test/intent_probe.py
- **What it is:** ED-MB-0029 probe: stance pairings (hold/balanced/aggressive) under `MB_INTENT_RESOLUTION` off vs on, measuring win split, casualties, tempo.
- **Status:** none; reading: historical probe.
- **Bears on:** MB
- **Content that matters:**
  - Expected with intent ON: hold-vs-hold slow low-casualty standoff; aggressive-vs-aggressive fast and bloody; aggressive-vs-hold the holder survives longer :1-7.
  - Config knobs `MB_INTENT_RESOLUTION`, `INTENT_OFFENSE_D`, `INTENT_DEFENSE_D` :43.
- **Conflicts / stale:** dead import path; later finding says `PC_INTENT_RESOLUTION` is "a small sigma nudge, not a survivability mode" (cell_primitive_damage_v1 :218-222).
- **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/octagon_damage_model.md
- **What it is:** ED-MB-0018 note: facing octagon as a damage-received multiplier with non-instant reaction and multi-side shock, 2026-07-23, with adversarial-review corrections.
- **Status:** "implemented, DEFAULT ON, field goldens re-recorded"; reading: live design (config `PC_OCTAGON_DMG`), values still referenced.
- **Bears on:** MB, PC, DICE
- **Content that matters:**
  - Jordan directive: "-2D is not a good penalty"; octagon is a damage-received multiplier, rear about 2x; cells need >= a couple ticks to turn; multi-side attack is "extra bad, not just divide-by-two" :5-16.
  - Anchors: front (GREEN) 1.0x, flank (YELLOW) 1.5x, rear (RED) 2.0x; `mult = 1 - arc*(RED-1)/2`; local attacker centroid within `OCTAGON_LOCAL_REACH=2.0` :39-66.
  - Reaction: `FACING_REACTION_TICKS=2`, `FOV_HALF_DEG=105`, frontal pin via `PC_PIN_REACH` prevents turning; rear strike never perceived so 2x persists :70-84.
  - Multi-side shock `MULTI_SIDE_SHOCK=0.5` graded by distinct faces: 2 sides 1.5x, 3 2.0x, 4 2.5x; rear pair on a 2-sided body reaches ~3.0x :87-89, :140-150, :151-157.
  - Supersession: pool-penalty envelopment machinery (wrapper/pocket/roll-up) goes dormant under the flag; `ENCIRCLEMENT_PENALTY` gated off to avoid double-count :94-104, :144-147.
  - `t=None` footgun fixed; reaction clock made frame-independent and idempotent per tick :129-143.
- **Conflicts / stale:** fiat_register D2/3b says a second zone classifier (`_charge_shock_sigma` zone) double-counts on top of this; cell_primitive_damage says averaging per-cell arcs into a pair scalar was the smear bug (since fixed under gate `PC_CELL_DAMAGE`).
- **Open items:** default-ON flip and exchange-ratio characterization were `needs_jordan`; full-campaign A/B after CEV friction.

### .audit/2026-07-22-mass-battle-stress-test/orphaned_mechanics_audit_v1.md
- **What it is:** Inventory of built-but-dead MB code and disabled mechanics, 2026-07-24; Jordan directive "built work is ratified and wired by default".
- **Status:** none; reading: historical inventory, partly wired since (ED-MB-0035).
- **Bears on:** MB
- **Content that matters:**
  - Never-imported modules: `perimeter.py` (WIRED ED-MB-0035 into `_envelop_goal`), `provenance.py` (dead seed), `lanchester_signature.py`, `validators.py`, `workbench/` :7-15.
  - Dead mechanics: `PC_ENVELOP_SIGMA=0.0` (computed then multiplied by zero; naive enable rewards the DEFENDER, C7 100->20), `PC_FACING_MODEL` family (`PC_FACING_SLEW_BASE` "NOT ratified, do not enable"), `PC_WHEEL` (never fires on node path) :17-31.
  - Dead constants: `PC_FLANK_DEPTH_RESIST`, `PC_REFILL_FLOOR`, `PC_ROTATE_FLOOR`, `MORALE_EROSION_DAMP`, `ROUT_EXHAUSTION_MORALE_HIT`, `ROUT_FLOOR_LOSS_PCT`, `SUBUNIT_ROUT_FLOOR`, `MAX_TROOPS_PER_UNIT`, `BUFFER_CELLS`, `UNIT_GRID_SIZE`, `REACH_LONG` :35-40 (note `MORALE_EROSION_DAMP` is live in `core/state.py:111` per adversarial audit, so this list is partly wrong).
  - ED-MB-0035: orbital wheel `_envelop_wheel_goal` keeps `ENVELOP_STANDOFF` radius then wheels to rear; C4 cavalry envelop 6 -> 83 :42-47.
- **Conflicts / stale:** `MORALE_EROSION_DAMP` listed dead here but live at `modules/mass_battle/config.py:332` (verified present; reader `core/state.py` per adversarial audit) -- an internal audit disagreement.
- **Open items:** triage of the dead constants into rotation model T1-T3 or deletion.

### .audit/2026-07-22-mass-battle-stress-test/pathing_deployment_diagnosis.md
- **What it is:** Diagnosis of multi-unit deployment/pathing bugs flagged by Jordan from a hierarchy snapshot, 2026-07-22; resolved section added (ED-MB-0017).
- **Status:** "RESOLVED (ED-MB-0017)" in §6; reading: historical, fixed.
- **Bears on:** MB
- **Content that matters:**
  - `build_army` placed subunit i at `(start_row, 15 + i*4)`: envelopment wings both on the right, refused wing level with strong wing and overlapping cols 19-20 (P-1 overlap, P-2 same-side wings, P-3 refused flank not refused) :9-45.
  - Fix: frontage-aware centred line (`_centered_line_cols`), symmetric wings, echeloned refused wing; `test_deployment_geometry.py` (16 cases) :89-93.
  - P-4 (Jordan): envelopers must be fast; `PC_ENVELOP_SPEED_MULT`=2x for the maneuver, `PC_CAVALRY_SPEED_MULT` 2.0 -> 3.0 ("cavalry march ~3x infantry"); cavalry envelop wraps behind by ~t6-8 :95-105.
  - Critic found `_centered_line_cols` crash for over-wide armies (fixed, 0 crashes over 200 fuzzed configs) and `gauge_mb.make_mixed_unit` same `10+i*4` defect :106-117. Test min 3 and up to 11 subunits (Jordan) :65-70.
  - Still open: horseshoe not full ring; single line only; `build_envelopment`/`build_refused_flank` hardcode field centre 25 :119-125.
- **Conflicts / stale:** fiat_register_v1 later found a new wing mis-placement (phantom centre column) in `build_envelopment`, i.e. P-2 was only partly fixed.
- **Open items:** full ring, reserve lines.

### .audit/2026-07-22-mass-battle-stress-test/perimeter_targeting_geometry_v1.md
- **What it is:** Spec for perimeter target-points and face normals as the approach/targeting backbone (Jordan hand-drawn model, 2026-07-23).
- **Status:** "SPEC / PROPOSED (un-built)" at writing; reading: partially built (`perimeter.py` wired into `_envelop_goal` by ED-MB-0035, see orphaned_mechanics_audit).
- **Bears on:** MB
- **Content that matters:**
  - Major target points = face midpoints (normal perpendicular), minor = corners (bisector normal); attacker aligns body along the normal before contact; interceptable en route :8-22.
  - Pointed-formation exception: interior tip angle <= ~60 degrees (Arrowhead apex, cavalry rhomboid) treated as one vertex target :24-29.
  - Replaces centroid reference (which gave spurious flank on wide lines hit head-on) :31-39.
  - Integration plan: perimeter extraction, face/point targeting in `assign_targets`, approach-along-normal goal replacing hardcoded `_envelop_goal` waypoint, interception, octagon refinement :41-66.
- **Conflicts / stale:** spec still says un-built; ratified_but_unbuilt_backlog says "entirely unbuilt" on 07-23, orphaned audit says `perimeter.py` wired 07-24. `modules/mass_battle/perimeter.py` exists (verified).
- **Open items:** corners secondary vs primary; 60 degree tip threshold; hard gate vs soft bonus for alignment.

### .audit/2026-07-22-mass-battle-stress-test/ratified_but_unbuilt_backlog.md
- **What it is:** Exhaustive classification of ratified-but-unbuilt, built-not-ratified, and proposed-not-ruled MB items, 2026-07-23.
- **Status:** none; reading: historical backlog; some items since moved (see below).
- **Bears on:** MB, FA, CORE
- **Content that matters:**
  - A1 waypoint primitive + path-length budget `0.5 x speed x max-ticks` (ED-1096) never built; A2 Stage G route `resolve_mass_battle`+`faction_action` onto field engine, retire integer engine (P-DEC-2, "nothing else is live until this") :20-21.
  - A3 multi-unit Path B (`multiunit_envelopment_plan.md`, Phase 1 never started); A4 DG-2 emergent auto-yield/rally/pocket; A5 Faction Tactic Cards §B.4 (PP-283) with `FACTION_TACTIC_CARD_POOL_MODIFIERS = {}` blocked since 2026-05-17; A6 Reserve formation Phase-3-commit rule (PP-MB-04/PP-499) zero code; A7 Feigned Retreat (PP-256, Ob-1 pursuit Discipline check) zero code :22-26.
  - A8 P-DEC-3 cavalry density cap (< infantry) deferred; A9 triplex acies depth lines and full-ring closure :27-28.
  - Open decision queue DG-7..DG-16 (cell-count generator, morale floor, cav/inf envelopment differentiation, troop-type speed/dr/stamina, per-cell scope, volley-pool grounding, hold-stance semantics, reach ratification, tactics/role grounding) opened 2026-07-08 never revisited :42-47.
  - ED-MB-0008: two contradictory ranged/volley DR tables, both live (~2x apart) `open, needs_jordan` :47-49; ED-MB-0009 dangling `stage5_clocks.md` citation; ED-MB-0010 fabricated Key-type in `module_contracts.yaml` (the Key substrate is since retired) :67-69.
- **Conflicts / stale:** `proposals/multiunit_envelopment_plan.md` exists (verified); A7 "grep feigned in the sim -> zero hits" contradicts adversarial_deep_audit §1.7 (feigned exists but can never be True); officers/tactic cards/reserve may have been built since (`test_mass_battle_officers.py`, `test_mass_battle_order_of_battle.py` exist) [UNVERIFIED].
- **Open items:** all of §C is a decision queue that this suite may want to answer by precedent (CLAUDE.md §0 needs_jordan rule).

### .audit/2026-07-22-mass-battle-stress-test/rotation_model_v1.md
- **What it is:** Parse-back and build plan for Jordan's two-tier troop rotation + recovery directive (T1 intra-subunit backfill, T2 inter-subunit blended rotation, T3 troop recovery), plus ED-MB-0029 intent axis, 2026-07-23.
- **Status:** none; reading: historical; T1 phase 1a and intent landed gated OFF; T2/T3 unbuilt at writing.
- **Bears on:** MB
- **Content that matters:**
  - Jordan's directive text: unengaged troops fill engaged cells to keep prescribed density; coverage shrinks as minimums fail; subunits rotate by blended relational cell exchange; not all losses are deaths so a subunit must recover some troop count :5-20.
  - Landed: `Subunit.close_ranks()` front-rank-first reflow toward `_cell_target`, gated `PC_CLOSE_RANKS` (default OFF), `tests/valoria/test_close_ranks.py` (7) :43-61; DEEP(3x4) vs SEMI(6x2) 81% -> 94% with it ON :60-61.
  - Intent: `STANCE_COMMITMENT` aggressive +1 / balanced 0 / hold,retreat -1 into sigma net: `ns_a += (cA*INTENT_OFFENSE_D + cB*INTENT_DEFENSE_D)*SIGMA_PER_D`; `INTENT_DEFENSE_D=1.0 > INTENT_OFFENSE_D=0.5` per tactic-card asymmetry (Disciplined Defence +1D) :77-106.
  - Remaining: T1 phase 1b (dissolve sub-`CELL_FLOOR` cells, lateral close-up), T2, T3 (bounded decaying recovery; must not heal to full) :63-75.
- **Conflicts / stale:** `tests/valoria/test_close_ranks.py` is not in the `tests/valoria` listing grep for mass_battle (the file name does not contain "mass_battle"); [UNVERIFIED present].
- **Open items:** T1b, T2, T3.

### .audit/2026-07-22-mass-battle-stress-test/mb_fieldbased_stress.py
- **What it is:** Field-based stress harness library (S0-S5): invariant checker, random army fuzz, movement census, scenario probes, `--emit` flag-A/B runner (2026-07-22).
- **Status:** none; reading: historical harness, dead imports (`mass_battle.engine`).
- **Bears on:** MB
- **Content that matters:**
  - Invariants: winner in A/B/draw, hp fraction in [0,1], no NaN morale, cell==hp conservation tolerant to max(2, 2% hp_max) and EXEMPT when any subunit routed/broken :63-103.
  - Fuzz covers 10 troop types plus `infantry` fallback, 4 valid shapes (Horseshoe/RefusedFlank retired, LC-8/ED-1088), roles, instructions brace/envelop/sweep/kite ("the instrs the engine actually consumes"), timed orders, `SUBUNIT_CAP`=11 :54-57, :109-170.
  - Scenarios: mirror, charge_vs_brace, envelop, ranged_dense, big_vs_small; seeds 1000+s :243-284.
  - Reads `C.MB_NODE_COHESION`, `C.PER_CELL`, `HU.FIELD_MOVEMENT` (names that later became `PC_NODE_COHESION`) :320.
- **Conflicts / stale:** modules moved to `modules/mass_battle/`; `engine.py` facade (`mass_battle.engine`) with `MECHANICS`/`mechanics_selftest` is not in `modules/mass_battle/` listing (no `engine.py`) [UNVERIFIED where it went].
- **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/reachability_sweep.py
- **What it is:** ED-MB-0041 per-row reachability sweep tool: one subprocess per (row, config), 33 booleans both ways + 6 magnitudes, optional greedy `--stack`.
- **Status:** none; reading: historical tool, method still instructive.
- **Bears on:** MB, PROCESS
- **Content that matters:**
  - Method note: negative verdicts valid at low n, positives must be re-verified at n=60 (R1 baseline reads 26.7/OK at n=16 and 44.1/WIN-OUT at n=60) :13-26.
  - Toggle list uses `MB_*` env names (MB_CELL_DAMAGE ... TIP_SUPPORT_ENABLED) and magnitudes `MB_CHARGE_RECOIL`, `SIGMA_PER_D`, `K_LINEAR`, `MULTI_SIDE_SHOCK`, `FACING_REACTION_TICKS`, `ENCIRCLEMENT_PENALTY` :42-62.
  - Band parser anchored on the `dexp` token (rows are ragged: braced-repel rows have a 10th `'rawA'` field), asserts C2 == (0,30), H1 == (42,58) :175-192.
  - All-draw rows reported UNRESOLVED not "out of band" because 50.0 sits inside 42-58 :238-243.
- **Conflicts / stale:** docstring path `audit/2026-07-22-...` is pre-rename (now `.audit/`); depends on `tests/sim/gauge_mb.py` (exists).
- **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/reface_probe.py
- **What it is:** Probe testing the persistent-defender-reface hypothesis for envelopment over-decisiveness (monkeypatches `resolve_engagements_cascading`).
- **Status:** none; reading: historical; hypothesis refuted (95 -> 100, per honest_gauge_readout).
- **Bears on:** MB
- **Content that matters:**
  - Variants: full reface, rear-guard reface (threat >110 degrees behind cannot be turned to) :34-41; compares H3 thin-envelop vs 6-line and C4-like cavalry envelop :73-74.
- **Conflicts / stale:** dead import path.
- **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/reverse_pair_symmetry.py
- **What it is:** ED-MB-0041 reverse-pair symmetry instrument: `decA(X vs Y)+decA(Y vs X)` must equal 100, deviation in sigma on DECISIVE counts. A same-named copy also lives at `tests/sim/reverse_pair_symmetry.py` (verified present).
- **Status:** none; reading: live idea (copy in `tests/sim/`), here a historical duplicate.
- **Bears on:** MB, PROCESS, DICE
- **Content that matters:**
  - Invariant needs no history or band; a global symmetric constant cannot change the sum, so deviations localize to side-dependent mechanisms (deployment, resolution order) :9-23.
  - SE = `100*sqrt(p_f(1-p_f)/k_f + p_r(1-p_r)/k_r)` on decisive counts, ~9pp at n=60, so ~18pp to be 2-sigma; `SIGMA_GATE=2.0`; `sigma None` when an orientation has no decisive results ("not a pass") :25-31, :46, :56-82.
  - Pairs checked: H2/H9, H3/H10, H4/H11 :87.
- **Conflicts / stale:** duplicated in `tests/sim/` (two owners of one instrument).
- **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/results.json
- **What it is:** Machine record of the 2026-07-22 stress run (S0-S5 results), generated by `run.py --json`.
- **Status:** none; reading: historical data.
- **Bears on:** MB
- **Content that matters:**
  - S1 fuzz outcomes `{A: 6, B: 3, draw: 188}` of 197 built, mean turns 39.5 (near `max_turns=40`) :47-52, :72 -- i.e. ~95% of fuzz battles were draws, so "0 engine failures" and "77.7% contact" coexist with near-total non-resolution (README does not call this out).
  - S3 and S4 vectors show `draw: 12` of 12 seeds in nearly every scenario/arm (`winA=winB=0`), so "WIRED/INERT" verdicts rest on mean retained-hp differences, and S4 "SAFE" is invariant-only; the exception is `K_LINEAR` flipped to 24 which yields `winA: 12` :516-541.
  - S5 mirror symmetry |skew| = 0 over 48 trials with 44 draws (aw 2, bw 2) :621-631 -- symmetry control nearly vacuous.
  - Verdict dict: S1, S2, S3 flagged FAIL/ATTN (`"S1 fuzz": false, "S2 validators": false, "S3 flag A/B": false`) :632-640, while README summary reads "robust".
  - S2: V-CANNAE, V-SHOCK, V-BRACE false :139-150.
- **Conflicts / stale:** README table calls S1 "robust" and S5 PASS; the data shows both ran on mostly-draw battles (a measurement-validity caveat in the same spirit as adversarial_deep_audit §3 "null result = harness never reached it").
- **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/rout_probe.py
- **What it is:** ED-MB-0031 probe: casualty-at-rout and battle length with `MB_STOCHASTIC_ROUT` off vs on; target loser breaks ~15-30% not ~58%.
- **Status:** none; reading: historical probe.
- **Bears on:** MB
- **Content that matters:**
  - Config names `ROUT_ONSET_FRAC`, `ROUT_CAP_FRAC`; scenarios even disc5 v disc5 and disc5 vs disc3, 1200 troops 6x2 :17-43.
- **Conflicts / stale:** dead import path.
- **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/run.py
- **What it is:** Driver for the S0-S5 field stress test; shells out to `mb_fieldbased_stress.py --emit` per flag value in clean subprocesses.
- **Status:** none; reading: historical driver.
- **Bears on:** MB, PROCESS
- **Content that matters:**
  - Flags are import-time `os.environ` reads, hence one subprocess per env (same reason the byte-exact CI test spawns `bat.py` per mode) :1-9.
  - `FLAG_AB` roster of 16 (PER_CELL ... POOL_QUALITY_SCALE) with scenario per flag :176-194; S5 mirror skew tolerance `max(4, 25% of tot)` which accepts a result of mostly draws :296.
  - "WIRED" = outcome vector (winA/winB/draw/meanA/meanB to 1e-4) differs :51-56.
- **Conflicts / stale:** dead imports (`mass_battle.engine`, `mass_battle.validators`); names `MB_*` vs `PC_*` mixed in the same file (`PC_NODE_COHESION` in results.json, `MB_NODE_COHESION` in code) -- a rename mid-stream.
- **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/run_log.txt
- **What it is:** Console transcript of `run.py` (2026-07-22).
- **Status:** none; reading: historical log.
- **Bears on:** MB
- **Content that matters:**
  - 30 registered MECHANICS all WIRED, gates on under field defaults; `PC_FACING_SLEW_BASE=60.0` left off :1-45.
  - Movement census: knights_templar kills defender fully (hp left 0), levy 1709 of 2000 left (disc 1 barely damages) :64-76.
  - V-CANNAE measured 0.0079, V-SHOCK 0.0, V-BRACE (0.0, 0.0) FAIL :85-88.
  - S3 INERT list: MORALE_FIX, PC_RECOIL_FRONTAL, PC_BRACE_SETUP_DELAY, PC_WHEEL :105-111.
- **Conflicts / stale:** none new beyond results.json notes.
- **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/side_face_probe.py
- **What it is:** Probe: does the enveloper's wing wrap work in both orientations (side A vs B); records defender-struck faces.
- **Status:** none; reading: historical probe.
- **Bears on:** MB
- **Content that matters:**
  - Hypothesis "if as B the defender is only struck FRONT, the wing wheel has a directional pathing bug"; monkeypatches `resolve_engagements_cascading` and filters defender by `faction` :1-3, :28-37.
- **Conflicts / stale:** dead import path.
- **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/side_probe.py
- **What it is:** Isolates the envelopment side asymmetry: same armies, A/B swapped, same seeds, enveloper decisive-win rate.
- **Status:** none; reading: historical probe (result in envelopment_stability_diagnosis: ~71% as A, ~17% as B).
- **Bears on:** MB
- **Content that matters:**
  - Uses `g._envelop_army` vs `g._command_army('Line')`, 20 turns, seed base 1_000_000 :8-22.
- **Conflicts / stale:** dead import path.
- **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/symmetry_probe.py
- **What it is:** Wide-mirror symmetry probe: width scaling of side bias in identical Lines (widths 2-24, three seed bases).
- **Status:** none; reading: historical probe (honest_gauge_readout: fair at width <=6, ~55-57% A at >=12).
- **Bears on:** MB
- **Content that matters:**
  - Mirror `unit(width, depth=1, conc=100)` at x=25, `max_battle_turns=30`; reads `MB_FRONTAGE_BLEND` :20-36.
  - Distinct from `reverse_pair_symmetry.py`, which tests asymmetric pair complement (that docstring says mirror passes and reverse pairs fail).
- **Conflicts / stale:** dead import path.
- **Open items:** the wide-mirror drift at width >=12 was never root-caused in this corpus.

### .audit/2026-07-22-mass-battle-stress-test/spatial_model_v2_plan.md
- **What it is:** Staged plan for spatial model v2 (Euclidean motion, OBB footprints, honest facing/frontage/depth/reach), Jordan-directed 2026-07-22, with stage status updates A-F and P-DEC rulings.
- **Status:** "PROPOSED (max-effort implementation plan)"; reading: executed through Stage F; Stage G done later (see below).
- **Bears on:** MB, CORE
- **Content that matters:**
  - Model: cell = rigid oriented rectangle (OBB), centre float, facing heading, 1x1 standard, density = troops/area, reach extends the FRONT face only (anisotropic); motion Euclidean, collision box (two metrics on purpose) :12-34.
  - Invariants I1 conservation, I2 determinism, I3 no integers on live field path, I4 grid oracle untouched, I5 no silent balance tuning, I6 mirror symmetry, I7 reach implies facing :38-53.
  - Stage C correction: halt on BODY box, contact on reach box (README §7.2); Stage D `geometry.engaged_frontage` continuous frontage (ED-MB-0013); Stage E per-type reach 0.1/0.2/0.3 + authored `pike` troop type (ED-MB-0014) and reach is a charge/brace lever, not a standing-melee one :110-195.
  - P-DEC rulings: reach map (lance 0.2, ranged 0.1 sidearm); P-DEC-2 RETIRE THE INTEGER ENGINE (Stage G go); P-DEC-3 every cell 1x1, cavalry lower MAX density cap (not a bigger box); P-DEC-4 gauge re-baseline authorized and re-validate against history :262-284.
- **Conflicts / stale:** Stage G executed: `modules/mass_battle/massbattle.py` header says `resolve_mass_battle`, `_faction_to_unit` and the garrison stub were DELETED 2026-10-01 (plan position 29b); the season-facing path is now `resolve_field` -> `run_battle` (verified by grep). `pike` appears in `modules/mass_battle/troop_types/presets.py` (verified). P-DEC-3 density-cap and PP-290 reach reconciliation status unknown [UNVERIFIED].
- **Open items:** cavalry density cap; PP-290 reach reconciliation; historical-revalidation sub-pass.

### .audit/2026-07-22-mass-battle-stress-test/stageBC_test_obb_contact_toi.py
- **What it is:** Acceptance test (copied into `tests/valoria` as the OBB contact/TOI test): contact fires at OBB touch, no interpenetration, no stall, cavalry charge reaches contact, grid path never calls OBB, conservation, determinism.
- **Status:** none; reading: historical copy of a test whose live form is `tests/valoria/test_body_contact_toi.py` (verified present).
- **Bears on:** MB
- **Content that matters:**
  - Head-on contact fires at gap 1.49 and not at 1.51 or 1.9 (old circle standoff 2.0) :140-158; `_CommitProbe` wraps `resolve_toi_and_commit` to record body interpenetration and deep reach overlap (EPS 1e-6) :101-131; grid oracle guarded by poisoning `obb_front_reach_overlap` :199-217.
- **Conflicts / stale:** imports `mass_battle.*` (gone); live test file is named differently.
- **Open items:** none.

### .audit/2026-07-22-mass-battle-stress-test/stage_F_verification.md
- **What it is:** Stage F verification report for spatial model v2 Stages D+E (ED-MB-0015), 2026-07-22.
- **Status:** "DONE 2026-07-22 (ED-MB-0015)"; reading: historical, closed.
- **Bears on:** MB
- **Content that matters:**
  - I1-I7 all hold: 300-battle fuzz 0 violations; field goldens re-recorded (`unit_field` 2da5183a..., `cell_field` 5f5db965...), grid goldens unchanged :8-30.
  - Gauge under OBB: pre-D baseline 10/20 multi -> v2 6/20; honest reading "authorized re-baseline", either honest geometry exposed divergences or bands need re-grounding; dominant failure DG-6 over-decisiveness (CV 0.89 -> 0.06 over N=4..1024); C2/C6 REPEL (attacker ~5%) at this point, contradicting later readings that C2/C6 NOT-REPELLED :54-84.
  - Full `tests/valoria` at that time: 447 passed / 60 skipped / 1 xpassed :52.
  - Deferred: PP-290 reach-scale reconciliation, P-DEC-3 density cap, DG-6 :97-103.
- **Conflicts / stale:** its C2/C6 REPEL claim (attacker ~5%) is contradicted by honest_gauge_readout (57% raw) and adversarial_deep_audit §8.4 (43.8-100% span) one to two days later -- the 10/20 -> 6/20 numbers pre-date the density fix (ED-MB-0027) that revealed the real baseline 5/20.
- **Open items:** none beyond deferred list.

### .audit/2026-07-23-combat-combinatorial-audit/findings_v1.md
- **What it is:** PC combinatorial/isolation audit and all-node state-graph interrogation (ED-PC-0025, 2026-07-23): every lever toggled alone and pairwise.
- **Status:** "RATIFIED (audit conclusions + the two fixes below; ED-PC-0025, 2026-07-23)"; reading: historical, fixes landed (`core.logistic` exists at `modules/combat/core.py:36`, verified).
- **Bears on:** PC, DICE, CHAR
- **Content that matters:**
  - Verdict "NO DEAD WIRES": WIRED-LIVE levers skill(bind) +33pp, agility +40pp, skill(dodge) +31pp, skill(parry) +25pp, strength +24pp; morphology levers (edge_read, spine_press, edge_grab, choke, facing_regime) are per-event situational, ~0 aggregate :18-24.
  - Strong channels sub-additive toward the hard 95% ceiling (`UPSET_FLOOR=0.05`); one genuine synergy aggression x bind-skill (+30.6 vs +20.9 expected) :26-28.
  - Pipeline node firing rates; separation reasons `collapse` and `beat_exhaustion` never fire (pre-existing dead-branch, HANDOFF_PC) :30-32.
  - Fix: single-source overflow-safe `core.logistic()` (was open-coded 5 ways; out-of-contract attributes 50000 crashed 99/300 fights -> 0/300), clamp +-500, legal builds |arg| <= ~2.4 so byte-identical :43.
  - Frequency-gating: morphology levers are gated by their enabling skill (`mode_sigma` wind branch adds `defender.skill('bind')`), default builds don't invest so ~0 aggregate :40.
  - DEFERRED: mode-exposure `T_vuln` model (select_mode is exposure-blind), HEMA grounding corrections (`guardia`->facing_regime wrong, `atajo`->measure wrong, `zwerchhau`->edge_read wrong-leaning), no tradition gate on `equipped`, 9 pre-existing intentional-red failures :46-50.
- **Conflicts / stale:** "ED-PC-0025 ratified" status but DEFERRED list was surfaced only; whether `T_vuln` or the equipped-tradition gate were built since is [UNVERIFIED].
- **Open items:** all DEFERRED items (T_vuln, grounding corrections, build-legality gate, 9 red tests).

### .audit/2026-07-23-combat-combinatorial-audit/harness.py
- **What it is:** Isolation sweep script: each factor on-alone vs off, event-divergence (fires%) and win-share delta, classified DEAD / WIRED-SITUATIONAL / WIRED-LIVE.
- **Status:** none; reading: historical script.
- **Bears on:** PC
- **Content that matters:**
  - Factor table grouped by state-graph node (Exchange.read, Bind, Contact, Approach.facing, Riposte.counter, Exchange.commit/mode, Damage, Tempo) :53-78; class thresholds fires <3% and |dw|<2pp = DEAD; |dw|>=5pp LIVE :86-88.
  - Control row "tradition=german ALONE (no ability, post-imposition-retire)" expected DEAD :77.
  - Path hard-coded: `systems/combat/combat_engine_v1` plus its `workbench/trace.py` :5-10.
- **Conflicts / stale:** live PC code is `modules/combat/` (files `fight.py`, `core.py`, `wrapper.py`); `systems/combat/combat_engine_v1` still exists on disk (verified `ls systems/combat`), so the script may or may not run [UNVERIFIED].
- **Open items:** none.

### .audit/2026-07-23-combat-combinatorial-audit/interaction.py
- **What it is:** Pairwise interaction matrix per state-graph node: INDEPENDENT / MASKING / SYNERGY / ANTAGONISM / PARTIAL.
- **Status:** none; reading: historical script.
- **Bears on:** PC
- **Content that matters:**
  - Classification: |dxy - (dx+dy)| <= 2pp independent; super-additive SYNERGY flagged as "degeneracy risk" :1-4, :29-36.
  - Nodes: Bind (katana vs arming), Contact (dagger vs arming), Exchange (arming mirror) with factor lists (shinogi L1/L3, skill_bind2, staerke, ringen, skill_grab2, strength, parry, agi6, disp_agg) :40-59.
- **Conflicts / stale:** same hard-coded `systems/combat/combat_engine_v1` path.
- **Open items:** none.

### .audit/2026-07-23-combat-fiat-audit/fiat_audit_v1.md
- **What it is:** PC fiat / broken-logic audit (ED-PC-0023, 2026-07-23): four passes incl. three blind read-only hunters plus author's `[FIAT]`/`[ASSERTED]` inventory (18 tagged sites).
- **Status:** "RATIFIED (by merge of PR #226, 2026-07-23, ED-1094)"; reading: historical, mostly executed.
- **Bears on:** PC, DICE
- **Content that matters:**
  - Grip-invariant thrust (`weapon_physics.phi_grip('point')==1.0`) interrogated and kept: axial force is grip-invariant; real costs of choking up already live in `choke_counterbalance -> CHOKE_ACCURACY_K` and reach/lunge/commit systems, a `phi_grip` force term would double-count :15-28.
  - Fixed: `THRUST_LEVER_FLOOR` 0.30 -> 0.24 (was flat-topping 7 polearms; verified `modules/combat/core.py:408` shows 0.24); `GAP_EXPOSURE` reordered `{cloth:0.97, mail:0.95, plate:0.90}`; dead `Combatant.pool` removed; stale WIRING-STATUS prose struck :30-37.
  - Deferred (evidenced): `MAX_TEMPO_PEN=0.8` flat-tops 38 of 53 weapons to one 0.80 ("single largest emergence-suppressor found"); fix = over-cap tail saturation but needs `tests/valoria/r3_identity_golden.json` regenerated and no generator exists; `PERC_EXP=0.30` low-mass compression; `PERC_TRANSMIT_FLOOR=0.35` flat-tops 11 Mordhau ratios :39-52. Still live: `MAX_TEMPO_PEN=0.8` at `modules/combat/config.py:21` and `PERC_TRANSMIT_FLOOR=0.35` at `core.py:302` (verified).
  - Jordan ruling 2026-07-23: `impose_node` (tradition forces its preferred node) retired as fiat; build investment (bind-skill 1.0/2.0/3.0 -> 61.3/71.1/74.7%; parry 57.2/65.6%) carries differentiation :53-62; deleted under ED-PC-0035 (config comment confirms) :294.
  - Design principle: "each combatant should have their own feel, emergent from their full stack ... every build should be available"; tradition gates ACCESS, investment drives EFFICACY; target = per-fight texture with outcome preservation, not aggregate win-rate parity :86-114.
  - CLAUDE.md §5 "combat pool defined three ways" overstated: `max(5, History+6)` everywhere except stale `values_master.yaml` (since dissolved) :73-76.
- **Conflicts / stale:** `values_master.yaml` is in the dissolved list (CLAUDE.md §3); `adef_cap` blunt-branch latent bug [UNVERIFIED fixed].
- **Open items:** tempo-penalty saturation; PERC calibrations; graded investment levels for abilities ("levels of investment for techniques", scoped as next increment).
