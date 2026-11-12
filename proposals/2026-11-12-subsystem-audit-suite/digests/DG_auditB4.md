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
