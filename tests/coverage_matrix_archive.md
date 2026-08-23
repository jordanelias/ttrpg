# Coverage Matrix — ARCHIVE (settled entries)

Live entries in `tests/coverage_matrix.md`. Nothing here is superseded — these are settled
coverage records moved out so the live file keeps room for the next one.

**RESTORED 2026-08-23.** This file existed until `cadf9c7` (2026-08-04), where the evacuation
deleted it while `coverage_matrix.md`'s own header still pointed here — so for nineteen days the
live file named an archive that did not exist, and its documented relief valve was unusable. That
is why it reached 94% of a BLOCKING cap with 883 tokens left, on a file the co-file rule
(`tools/ci_co_file_checker.py` rule 3) REQUIRES every simulation-output commit to append to. The
next such commit would have failed CI on size, not on content.

Sections dated **2026-07-25 and earlier** live here; **2026-07-29 and later** stay live. The
boundary is a date, not a judgement about which findings matter — several entries below were load
bearing, most of all the ED-MB-0042 RETRACTION, which is the worked example behind `CLAUDE.md`
§0.1's five measurement checks and is cited from there.

Sections marked *(archived — condensed)* or *(archived — verbatim)* are stubs whose full text was
moved to the previous incarnation of this file before it was deleted; that text is recoverable at
ref `cadf9c7`, not here.

---

## 2026-07-25 — ED-MB-0042 RETRACTED: the flip was measured against an arm that couldn't recover

**The flip below was made and then withdrawn the same day. Do not cite its numbers.**

`between_turn_recovery` and `reset_morale_between_battles` both write the morale **scalar**, which
`eff_morale` stops reading the moment cells are seeded — so with `PC_CELL_MORALE` ON they are **silent
no-ops**. Verified directly: knock a body's cells to 2.0, call both, and it is still at 2.0. The gauge's
multi mode runs multi-turn battles and resets morale between them, so **the ON arm fought with morale
that never recovered and the OFF arm's did.** "The loser breaks earlier" is exactly what a body that
cannot recover would also produce. The two arms were not comparable and I reported the gain without
checking that they were.

This is the **same defect class** as the `erode_morale` silent no-op caught earlier in this lane — a
scalar write shadowed by the cell aggregate. I fixed that one instance and never swept for the pattern,
so it recurred, in the same session, and this time it reached a shipped default and a golden re-record.
**The lesson is about scope of fix, not about morale:** when a defect's cause is "a representation
change orphaned its writers", the unit of repair is *every writer*, found by grep, not the one that
happened to fail.

Reverted: default back OFF, `_PINNED_OFF` back to `'0'`, both goldens back to their pre-flip digests
(`241f04e5…` / `dc3d3414…`), `test_default_is_gated_off` restored with the retraction reason.

**Two genuine defects were found by the failing suite and are KEPT** (both real bugs in the phase-1/2b
work, independent of the flip):

1. **Born-broken subunits.** `seed_cell_morale()` ran in `Subunit.__post_init__`, but a subunit whose
   morale is `None` inherits from its parent Unit and the `_unit` back-ref is not set until
   `Unit.__post_init__` — strictly later. So an inheriting subunit seeded every cell at `eff_morale`'s
   no-parent fallback of **0**, i.e. every cell broken at birth, emitting no combat weight and never
   recovering (once cells exist, `eff_morale` reads them and never falls back to the correct parent
   scalar). Now seeded from `Unit.__post_init__` for inheriting subunits. The gauge path passes morale
   explicitly, which is exactly why the targeted tests and the measurement were green while ten
   unrelated suite tests were not.
2. **A 1-ulp aggregate defeating an identity.** The troop-weighted mean of N *equal* values is that
   value mathematically but not in floats (15 cells at 6.0 → `5.999999999999999`). `_morale_sigma`
   divides by `morale_start`, so a body at full morale reported σ = −1.8e−16 instead of 0 — enough to
   cross a `DAMAGE_BY_DEGREE` boundary and turn a 6.0 exchange into a 0.0 one. A uniform body now
   returns its cells' value exactly. **My own test hid this**: it asserted the t=0 identity with
   `pytest.approx`, which is precisely the assertion that cannot see an ulp. Now `==`.

**Blocker for re-flipping** is not another gauge run — it is the scalar-write sweep. Known sites:
`between_turn_recovery` (unit + atom), `reset_morale_between_battles` (unit + atom), the rout write
`u.morale = 0.0`, `Unit.erode_morale`, and `core/state.py`'s `atom.morale = atom.eff_morale`.
## 2026-07-25 — ED-MB-0042 (RETRACTED, see above): PC_CELL_MORALE flipped ON (archived — condensed)

The same-day flip, retracted hours later — its ON/OFF arms were not comparable (scalar morale
writes the cell aggregate shadows). Do not cite its numbers. **Full detail:
`tests/coverage_matrix_archive_part2.md`** (moved 2026-07-29, ED-MB-0057).
## 2026-07-25 — ED-MB-0041 phase 2b: local break was UNREACHABLE; the missing symmetry (archived — condensed)

Phase 2 could not fire: bodies had erosion AND a break-point, cells had erosion only, so a cell had
to be destroyed twice over to break and the body always won that race by construction. An
asymmetry, not a magnitude. Cells given their own du Picq break-point; `check_cell_breaks` runs
before contagion and cohesion. **Full detail: `tests/coverage_matrix_archive_part2.md`** (moved
2026-07-29 under the register size cap, ED-MB-0052 — nothing dropped, only relocated).
## 2026-07-25 — ED-MB-0041 phase 2: local break, cell-scale contagion, and the half of phase 1 never wired (archived — condensed)

Cells got their OWN du Picq break-point (phase 2 was unreachable without it — bodies had erosion
AND a break-point, cells had erosion only, so a cell had to be destroyed twice over to break).
8-neighbourhood break contagion; `cohere_cells` wired (it had shipped with ZERO live call sites, so
the phase-1 measurement was of aggregate-up only). **Full detail:
`tests/coverage_matrix_archive_part2.md`** (moved 2026-07-29 under the register size cap,
ED-MB-0051 — nothing dropped, only relocated).
## 2026-07-25 — ED-MB-0041 phase 1 MEASURED: modest, as predicted; flag stays OFF (archived — condensed)

The phase-1 cell-morale measurement moved the gauge modestly and the flag stayed OFF. Superseded in
substance by the same-day RETRACTION above (its arms were confounded by scalar morale writes the
cell aggregate shadows) — do not cite its numbers. **Full detail:
`tests/coverage_matrix_archive_part2.md`** (moved 2026-07-29, ED-MB-0053).
## 2026-07-25 — ED-MB-0041 phase 1 FIXES: two defects in the per-cell morale wiring (archived — condensed)

Born-broken subunits (seed_cell_morale ran in Subunit.__post_init__ before the _unit back-ref was
set, so an inheriting subunit seeded every cell at eff_morale's no-parent 0) and the 1-ulp uniform
aggregate that crossed a DAMAGE_BY_DEGREE boundary via _morale_sigma. Both kept; both independent
of the retracted flip. **Full detail: `tests/coverage_matrix_archive_part2.md`** (moved 2026-07-29
under the register size cap, ED-MB-0053 — nothing dropped, only relocated).
## 2026-07-25 — ED-MB-0041 phase 1: the cell is the primitive for MORALE (archived — condensed)

Cells carry morale; the subunit's morale is the troop-weighted mean of its live cells (derived, not
stored); the aggregate pulls its own cells back at a discipline-gated rate. **Full detail:
`tests/coverage_matrix_archive_part2.md`** (moved 2026-07-29, ED-MB-0054).
## 2026-07-25 — ED-MB-0041: PC_STOCHASTIC_ROUT default flipped ON; contagion magnitude deliberately held

**Flipped, on the casualty scoreboard's evidence.** Loser 61-87% → 29-41%, winner 7.8-38% → 3.3-17%,
casualty realism 0/20 → 2/20 — while **win-share drops 10/20 → 7/20**. The count going down and the flip
still being right is the whole case for the second scoreboard. The reachability sweep had tested this
same flag hours earlier, found "passes C4, fails H9", and filed it as a wash; that was the wrong
instrument. Reversible with `PC_STOCHASTIC_ROUT=0`. Both grid goldens re-recorded (the break band
changes *when* a subunit routs, so the whole downstream casualty trajectory moves).

**`ROUT_CASCADE_FRAC` left inert at 1.0** despite measuring better: ⅔-of-line gives casualty 5/20 (and
fixes H6's 79.2% outlier → 29.7%), ⅓-of-line gives 7/20 but costs a win-share row and makes H6
*undershoot* at 14.1%. Held because (a) that is a real trade, not a clear win, and (b) per-cell state
redefines what a "section" is, so any value chosen now is fitted to a granularity about to change.

**Two methodological failures in my own experiment, recorded rather than quietly fixed:**
- **`0.34` and `0.5` returned byte-identical results — not robustness.** Three-subunit armies mean the
  broken share can only be 0, ⅓, ⅔ or 1, so both thresholds first fire at ⅔: I ran one experiment
  twice. Unexamined, "insensitive across a 47% range" would have entered the record as a robust
  plateau. A sweep over a continuous parameter must be checked against the DISCRETENESS of its target.
- **The rows that did not move were the informative ones.** H1/H2/H7/H8/H9 are identical to the decimal
  across every arm because `make_unit` builds them as a SINGLE subunit per side — broken share is 0 or
  1, so no threshold below 1.0 can fire. Inert by construction, not ineffective. An army of one subunit
  has no line to come apart, which is the sharpest argument yet for the per-cell directive: the residual
  30-33% sits on exactly those rows.
## 2026-07-25 — ED-MB-0041: the new instrument immediately overturns a default (PC_STOCHASTIC_ROUT)

**The casualty scoreboard's first act was to show that the win-share gauge has been penalising the
change that makes the engine historically correct.** `PC_STOCHASTIC_ROUT` implements the du Picq
15-30% break band (ED-MB-0031) and ships **OFF**; its own code comment says that without it "units
grind to ~58% before breaking". Measured across all 20 rows:

| | OFF (shipped) | ON |
|---|---|---|
| loser casualties | **61-87%** | **29-41%** (band 15-30) |
| winner casualties | 7.8-37.8% | **3.3-17.4%** (cap 15) |
| casualty realism | 0/20 | **2/20** |
| win-share | 10/20 | 7/20 |

One flag moves the loser from ~84% to ~31% — from annihilation to a few points outside the band — and
the win-share gauge scores it as a **three-row regression**. The reachability sweep had already found
`PC_STOCHASTIC_ROUT=1` "passes C4 and fails H9" and recorded it as a wash; that judgement was made on
the wrong instrument.

**Root cause of the residual, traced.** `Unit.derive_rout` breaks the army only when **every** subunit
has routed (`all(a.routed ...)`), and `run_battle` stops only when a UNIT routs. So sections break at
15-30% each, and then sit on the field absorbing casualties while their siblings fight on — the loser's
*total* climbs well past any individual section's break-point. Armies do not do this; they come apart
once a decisive portion of the line goes and the rest routs by contagion (du Picq: the end of a battle
is moral, not physical).

**New mechanism, gated inert:** `ROUT_CASCADE_FRAC` generalises `all(...)` to a fraction of a unit's
*starting* strength held in broken subunits. **Default 1.0 = exactly the old behaviour** (the share can
only reach 1.0 when no subunit is left unbroken), so goldens and gauge are untouched until the value is
moved. The magnitude is deliberately **unchosen** — the mechanism is du Picq-grounded, the number is
not, and picking one before measuring is the failure this whole audit has been about.
`tests/valoria/test_rout_contagion.py` (9 tests) pins the mechanism and — importantly — the *float
equality* of the inert default: `>= 1.0` on a computed ratio is exactly the kind of expression that
silently becomes 0.9999999 and changes when an army breaks.

**Two self-corrections while building it**, both caught by reading rather than by a failing test:
- My first `_broken_share` docstring said it weights by spawn strength "not the current one, which
  would shrink the numerator". That overstates: `troop_count` is *itself* a static nominal (it returns
  `self.troops`), so there was never a live alternative in play. The real reason to prefer
  `_start_troops` is that it is re-based per BATTLE, so a unit entering its third battle depleted
  measures collapse against what it started that battle with. Comment and test both corrected to the
  true property.
- Two of my own tests failed on harness errors, not engine defects (`troop_count` has no setter;
  5-7 subunits at 8-column spacing deploy off-field).
## 2026-07-25 — ED-MB-0041: the two gauge invariants that need no band (archived — condensed)

Two Jordan-approved gauge invariants that assert a RELATION rather than a historical band, so they
need no calibration: mirror symmetry (a matchup against itself must be ~50/50) and monotonicity in
force ratio. Both wired into the honest gauge; disclosed H3-vs-H10 slot asymmetry (61.0 vs 76.7,
summing to ~138 rather than ~100) surfaced by this pass and NOT diagnosed there.
**Full detail: `tests/coverage_matrix_archive.md`** (moved 2026-07-29 under the register size cap,
ED-MB-0050 — nothing dropped, only relocated).
## 2026-07-25 — ED-MB-0041 Tier-2: dead machinery wired or deleted + provenance retag (archived — condensed)

Seven Tier-2 items ("wire or delete, no third option"), each with a regression test verified to FAIL
against the pre-fix code. `dynamic_facings` deleted (write-only parallel facing store); `_front_fixers`
hoisted to full-tick scope; convergence merged_base made extensive; the charger-latch expiry made
explicit; provenance retagged off the bare-integer self-whitelist. Byte-exact goldens re-recorded where
noted in that section. **Full detail: `tests/coverage_matrix_archive.md`** (moved there 2026-07-29 under
the register size cap, ED-MB-0048 — nothing was dropped, only relocated).
## 2026-07-24 — ED-MB-0041 Tier-1: hp/cell dual-ledger reconciliation
- **Two ledgers fed DIFFERENT mechanics and could diverge permanently.** `hp` drives
  `_lanchester_strength`, `recalc_size` and the single-subunit cohesion fast path; `cell_troops` drives
  `pair_pool_contribution` and `troop_total()`'s `SUBUNIT_ROUT_FLOOR` check. Divergence sources fixed:
  (a) the **pursuit** and **freed-attacker** paths mutated `hp` with *no cell write at all* — so a unit
  ground down by pursuit still fought at full per-troop pool and could never hit the troop-floor rout;
  (b) `distribute_casualties`/`apply_to_subunit` open-coded a single clamped pass that **discarded** any
  share a cell could not absorb, while `hp` took the damage in full.
- **One owner:** new `_apply_with_spill` in `percell.py`; all three distributors now call it (the cellwise
  variant's inline copy deleted). Verified: hp/cell drift is **0.000000** through repeated pursuit damage.
- **CORRECTION to my own first framing.** I initially reported "4400 of 5000 discarded" from a uniform-weight
  probe. That was misleading: with **uniform** weights the old clamped pass and the spill agree (both empty
  everything, and the residual is genuine — nothing left to kill). The real divergence is under **NON-UNIFORM**
  weights — exactly the facing-weighted cellwise path and concentrated fire. Measured properly: two 100-troop
  cells weighted 10:1, 200 damage → **old absorbed 118.2, discarding 81.8; new absorbs 200.0**.
- Pinned by `tests/valoria/test_hp_cell_ledger.py` (3 tests, incl. the non-uniform case and a genuine-shortfall case).
## 2026-07-24 — ED-MB-0041 Tier-1: convergence partition-invariance + volley armour inversion
- **Convergence `factor = 1/N`.** `_convergence_scale`'s `merged_base` was a troop-weighted MEAN while
  `merged_troops` was a SUM, so N bodies converging on one target dealt the damage of **ONE** — firing on
  exactly Cannae/double-envelopment geometry. Made extensive (`sum`). Its premise (size-independent base,
  ED-899) is recorded as SUPERSEDED at `core/exchange.py:7`; under the live `POOL_QUALITY_MODEL` the
  correction now correctly becomes a no-op. **Measured honestly: side-swing 27.6 → 20.0pp (more symmetric),
  but average 38.8 → 35.0 — it does NOT move toward the band. A correctness fix, not a balance fix.**
- **Volley armour inversion (two compounding defects).** `volley_hp_scale` read the target's own
  `min(discipline,command)+dr`, so better armour/discipline/command **strictly increased** that unit's own
  missile casualties (a fossil of the retired `hp = size × h_per_size` model — `hp_max` is now raw troops).
  Separately, `net_after_dr` used a global `RANGED_DR_DEFAULT`, so real armour never protected at all.
  Now: flat `VOLLEY_LETHALITY_SCALE=3` (**exactly the prior gauge baseline** — inversion removed without
  silently re-tuning ranged lethality) + the target's own `eff_dr` routed into the volley.
  **Measured: casualties at dr 0/1/3 = 514.6 / 281.8 / 49.8 — armour is now monotonically protective.**
- **Regression tests, each verified to FAIL on the old code** (a test that passes both ways is worthless):
  `test_partition_invariance.py` (4 failures pre-fix), `test_volley_armour_direction.py` (2 failures pre-fix).
  Process note: my FIRST armour test passed against the buggy code — it measured total battle casualties,
  so melee DR protection masked the volley inversion; and the rewrite then deployed units 18 apart, outside
  `VOLLEY_MAX_RANGE=8`, asserting on all-zeros. Both corrected; it now drives `volley_phase` directly.
- **Goldens re-recorded (both CI-gated grid modes)** — deliberate, verified behaviour change in shared
  non-gated resolution code. `unit` 4c465e09 → c7a2eb3d, `cell` e5f09403 → 733c4547. Suite: 563 passed.
## 2026-07-24 — ED-MB-0041 remediation: Tier-0/Tier-1 execution (adversarial audit)
- **Reach gate silently disabled the braced-wall repel (biggest live defect).** `orchestration.py`'s comment
  claimed *"TROOP_TYPE_REACH is deliberately empty → this half of the gate is a no-op"*. It has **12 entries**
  (ED-MB-0014). The gate needs `reach_for(defender) >= reach_for(charger)`; `infantry 0.1 < cavalry 0.2`, so
  `PC_CHARGE_RECOIL` **never fired** for a braced generic-infantry wall — switching off the
  Courtrai/Bannockburn/Waterloo anchor and causing C2/C6 NOT-REPELLED. Comment corrected; C2/C6 defenders are
  now **pole-armed** (a brace IS a hedge of set poles; pike 0.3 ≥ 0.2 passes).
  **Measured honestly: 100.0 → 95.0 rawA.** The gate defect is confirmed and fixed, but unblocking it is
  **NOT sufficient** — the recoil now fires and is simply too weak (`PC_CHARGE_RECOIL=6 × SIGMA_PER_D=0.2`).
  The subagent's counterfactual of 0.0% did NOT reproduce at n=20. Residual gap is a magnitude problem.
- **C2 ≡ C6 duplicate broken.** They were bit-identical inputs with a fixed seed counted as two passes. C2 is
  now a genuinely DEEP block (3×6), C6 genuinely SHALLOW (6×1), both pole-armed.
- **`refuse_range` 3 → 10.** Measured minimum centroid-to-enemy approach is ~9.5, so the refused-flank release
  order NEVER fired in any caller (none overrides the default). Verified now firing (`_order_idx` 0 → 1), and
  the H6-style matchup produces casualties instead of the previous 0.0/0.0 freeze.
- **Anti-fabrication gate accepts honest provenance.** It recognised only `[canonical: ...]`, so the ONLY way
  to pass was to call a value canonical — a direct incentive for the false tags the audit found. It now also
  accepts `[GROUNDED: ]`, `[JUSTIFIED: ]`, `[DECLARED-DIVERGENCE: ]`, `[CALIBRATED-DEBT: ]` with equal force.
- **False citations corrected** (verified by hand): the 45° octagon boundary cited to `mass_battle_v30.md`
  (which contains **zero** occurrences of "octagon"); `PC_CAVALRY_SPEED_MULT` cited to a §A.7 that has no
  speed ratios; `K_LINEAR`/`LANCHESTER_STRENGTH_REF` cited to a doc whose §6 explicitly declines to supply
  magnitudes.
- **Declared divergences** (Jordan 2026-07-24: canon may be broken for tuning — it must be *visible*):
  `MORALE_EROSION_DAMP` makes the §A.4 cap −2.1 not −3 (comment previously asserted the cap was intact);
  `DISCIPLINE_LOSS_THRESHOLD` replaces canon's variable "> Discipline this turn" with a fixed cumulative 1.0.
- Deleted `tests/sim_verification_ledger.json` (26-entry bare-integer self-whitelist, `source=orchestration.py`).
## 2026-07-24 — ED-MB-0040: cell-primitive damage (the aggregate-smear bug) + historical Cannae oracle
- Jordan directive: "the cell is the primitive… each cell has its own octagon facing… its own capacity to
  receive and issue damage… flank/rear damage is supposed to be cellular… damage is done to cells."
  **BUG FOUND:** `_octagon_dmg_mod` evaluated each defender cell's own arc then **averaged** them into one
  subunit scalar; `distribute_casualties` then spread that total by **density only** — so a rear cell and a
  front cell in the SAME subunit lost identical troops, envelopment could not strip a formation
  shell-inward, and a monolith was near-unbreakable. **This is the upstream cause of BOTH the ED-MB-0038
  granularity workaround and the ED-MB-0039 "engine gap".**
- **FIX:** `_octagon_cell_mods` = the single owner of the per-cell arc; `_octagon_dmg_mod` = its mean
  (byte-identical). Gated **`PC_CELL_DAMAGE`** allocates each pair's casualties to defender **cells** by
  (troops × that cell's own facing mult) via `distribute_casualties_cellwise` (overflow-spilling, cells==hp
  holds under annihilation). Pair total unchanged — only placement. Volley keeps the aggregate spread.
- **Measured:** infantry envelop side-swing **41.0→15.5pp**, side-symmetric avg **43.8→57.8%** (into the
  55-72 band) — ED-MB-0039's "needs a new mechanic" was really this bug. **But** it re-bases the battery
  (gauge **8/20→4/20**: C4 93→71, H11 46→15) since bands were implicitly fitted to the smear → **ships
  GATED OFF**, byte-exactness verified vs the pre-change engine (identical winners + hp to 6dp).
- **HEADLINE (the real oracle):** the historical Cannae OOB (**5000 vs 8600**, real spread/subunit counts)
  yields **Carthage 0/20 both sides, flag ON or OFF** — the engine cannot reproduce history's defining
  envelopment. Missing: **per-cell morale** (local breaking), **a cost to useless depth**, **the elastic
  baiting centre**. Next: re-test all 20 precedents against their REAL orders of battle.
## 2026-07-24 — ED-MB-0038: matched command-granularity honest gauge (envelopment artifact fix)
- The honest gauge's composed enveloper/refused presets always faced a SINGLE-subunit opponent. A
  monolithic subunit is unbreakable by envelopment — flank/rear octagon mult + multi-side shock land on
  its cells but casualties DILUTE across one HP pool (`distribute_casualties`) and no section can rout
  independently, so the ED-1019 per-subunit rout cascade has nothing to bite. This pinned H3/H4/H6 (and
  reverses H10/H11) to 0% regardless of geometry: the density-matched gauge (ED-MB-0027) had unmasked a
  SECOND artifact one axis up — GRANULARITY. `granularity_probe.py`: H3 = 0% @ monolith, ~53% @ 3-command,
  ~95% @ 6-command.
- **FIX** (granularity analog of ED-MB-0027's density-constant): new `_command_army(shape, n_cmd=3)`
  deploys the composed side's opponent as a 3-command tripartite battle line (Polybius VI / triplex acies)
  at constant density, summing to GAUGE_TROOPS. Wired H3/H4/H6/H10/H11.
- **Result:** gauge multi **6 → 8/20** — H3 "full envelopment" flagship **0 → 70.7%** (band 55-72 OK),
  H11 **0 → 45.6** (band 38-55 OK); ZERO regressions (only all-failing envelop rows touched; H1/R1/C3/C4/
  C5/C7 untouched). Refuted en route: naive persistent defender reface (made it worse). Gauge-harness only
  (tests/sim/gauge_mb.py); no engine .py, byte-exact goldens unaffected.
- **Next:** side-asymmetry (H10 envelop-weak-as-B 83%), H4 wedge-centre-punch (0%), H5 refused-too-strong
  (100%), H6 stalemate; Cannae deep-baiting-centre + cavalry-rear; box-brace C2/C6.
## 2026-07-24 — ED-MB-0033 through ED-MB-0037 (archived — verbatim)

Moved to `tests/coverage_matrix_archive_2026-08-01.md` (cut 2026-08-01, ED-MB-0062) verbatim:
Fable logic audit Part-A remediation, field-coordinate unification (B1+B2+B3), `perimeter.py` +
cavalry orbital-wheel envelopment wiring, orphaned `MORALE_EROSION_DAMP`/`SUBUNIT_ROUT_FLOOR`
wiring, and superseded dead-mechanic constant removal.
## 2026-07-23 — ED-MB-0022 through ED-MB-0032 (archived — verbatim)
- Feigned Retreat (PP-256), Reserve Phase-3 commit (PP-MB-04), DG-2 fighting-withdrawal
  residuals, explicit subunit deployment primitives + frontage×depth, honest-gauge density
  integrity, cell closing-ranks, intent as an offence/defence axis, conditional orders, the
  stochastic-rout breakpoint at the historical 15-30% band, and the fractional combat pool.
  Full text: `tests/coverage_matrix_archive_2026-07-25b.md` (moved verbatim, not condensed).
## 2026-07-22/23 — ED-MB-0011 through ED-MB-0021 (archived — verbatim)
- spatial-model v2 Stages B-F (OBB contact / continuous frontage / weapon-class reach + pike /
  verification + golden re-record), DG-10 field-movement freeze, DG-6 per-battle combat
  effectiveness, multi-unit deployment geometry + envelopment pathing, the octagon
  damage-received multiplier + reaction delay + multi-side shock and its adversarial-review fix
  batch, the perimeter target-point/face-normal primitive, and the P-DEC-3 per-troop-type density
  cap. Full text: `tests/coverage_matrix_archive_2026-07-25.md` (moved verbatim, not condensed).
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
## Archived 2026-05-29 (pre-v32 sim rows; armature-reset coverage trim)
## 2026-07-08 — mass_battle: partition-invariance fix (ED-MB-0004) + RC-5 preliminary finding

**Jordan's rulings (AskUserQuestion, 2026-07-08):** the partition-invariance question left open by
ED-MB-0003 = **"genuine defect — fix it"** (not the historically-correct-mechanism reading); DG-2
(fighting-withdrawal/yield) = **"build it now"**; RC-5 triage = **start now, in parallel**.
