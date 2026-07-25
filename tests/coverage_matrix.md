# Coverage Matrix — Weapon System v2 (Active)

Archived entries in tests/coverage_matrix_archive.md

## 2026-07-25 — ED-MB-0041 phase 2b: local break was UNREACHABLE; the missing symmetry

**Phases 1+2 measured byte-identical to phase 1** — every one of 20 rows to the decimal, 1/20 casualty
and 8/20 win-share. Not a small effect: *zero*. Byte-identical is a far stronger signal than
disappointing, because a smaller-than-hoped number would have been absorbed as "phase 2 helps a little",
whereas identical across twenty rows can only mean the code never ran in a way that mattered.

**Instrumented: 72 of 144 cells "broken" at EXACTLY −1.0.** The uniformity was the diagnosis — local
damage produces a spread, so one repeated value means a single uniform write. It was the body-wide
stochastic-rout punch (`erode_morale(max(eff_morale + 1.0, 0))`, designed to land at −1.0), which phase
1 routes across all cells. **Cells were breaking as a CONSEQUENCE of the body routing**, strictly after
the event phase 2 exists to precede: `propagate_cell_breaks` only ever saw already-dead bodies, the
formation-break check is guarded by `not atom.routed`, and a routed subunit's emission is already zero.

**The cause was an asymmetry, not a magnitude** — which is why tuning would have been the wrong move:

| | gradual erosion | break-point short-circuit |
|---|---|---|
| body | yes | **yes** — `_stochastic_break`, du Picq 15–30% |
| cell | yes | **none** |

At `MORALE_PHASE_CAP=3` against a 6.0 pool a cell had to be **destroyed twice over** to break by erosion
alone, so the body always won that race by construction.

**Fix (`check_cell_breaks`)**: each cell draws its own break-point in the same historical band, skewed
by discipline, and breaks when its own casualty fraction crosses it — the body's mechanism at the
cell's scale, not a coefficient nudge. Morale values are now a genuine spread (−4.85, −2.79, −1.12,
−0.89, −0.47, +0.13 …) rather than every cell at −1.0.

**⚠ Early measurement shows OVER-FIRING**: single-mode draw rates of 76–100%. Bodies may now break so
early that nothing resolves. Recorded before the multi-mode scoreboard lands, so the concern is on the
record independent of how the final number reads. Flag remains OFF.

## 2026-07-25 — ED-MB-0041 phase 2: local break, cell-scale contagion, and the half of phase 1 I never wired

**First, a correction to phase 1.** `cohere_cells` shipped with **zero live call sites**. The
modulate-down half of the loop existed, was tested, and never ran in a battle — so the phase-1 gauge
measurement was of **aggregate-up only**. Same dead-machinery pattern this audit exists to find, built
into my own work while documenting the pattern. Now wired.

**Phase 2 mechanisms, all gated behind `PC_CELL_MORALE` (OFF):**
- **Local break** (`cell_broken`) — a cell whose morale reaches 0 stops FIGHTING. Implemented in
  `_pair_engaged_troops`, the single place per-cell troops become emitted combat weight, so no other
  emission path needs to know. `cell_troops` is untouched: the men are still there to be killed and
  still count as casualties. They have stopped being a fighting part of the line, which is what a local
  break *is* — zeroing them would make a break indistinguishable from annihilation.
- **Cell-scale contagion** (`propagate_cell_breaks`) — a broken cell shakes its lattice neighbours, so a
  gap spreads outward from where it opened. Neighbours are the 8-neighbourhood of pattern coordinates,
  so the spread follows the formation's actual shape with no shape-specific code.
- **Formation break** — a subunit whose broken cells hold `CELL_BREAK_ROUT_FRAC` of its live men has
  come apart as a body even with positive aggregate morale. Same shape as `ROUT_CASCADE_FRAC` one scale
  down; same deliberately **unchosen** magnitude.
- **Order matters**: contagion runs *before* cohesion each phase. Reversed, the body would paper over a
  break before it spread and contagion would never do anything.

**The emergent property — nothing says "disciplined units close gaps".** Contagion pushes down, cohesion
pulls toward the body's morale at a discipline-gated rate, and the behaviour falls out of the contest.
Measured over four phases from one broken cell:

| discipline | broken cell | outcome |
|---|---|---|
| 6 | **+3.08** | gap **closed**, broken share 0.00 |
| 1 | **−0.13** | still broken, share 0.11 |

**A test of mine asserted the wrong thing, and being wrong found the mechanism.** I expected cohesion to
lift the *shaken neighbours*. It doesn't — cohesion pulls toward the mean, and freshly-shaken neighbours
sit just *above* a mean the broken cell has dragged down, so they are pulled slightly further down. The
contest that matters is over the **broken** cell: whether the body can haul it back across zero. The
test now asserts that, with the wrong first version recorded in its docstring.

`test_cell_morale.py` now 16 tests. Not yet measured on the gauge — phases 1+2 will be measured together,
since phase 1's number was taken with half the mechanism dead.

## 2026-07-25 — ED-MB-0041 phase 1 MEASURED: modest, as predicted; flag stays OFF

Measured on corrected code (the first run measured the silent-no-op configuration and was discarded).

| | rout ON baseline | + `PC_CELL_MORALE=1` |
|---|---|---|
| casualty realism | 2/20 | **1/20** |
| win-share | 7/20 | **8/20** |
| loser casualties | 29-41% | 29.8-45.4% |
| **H6 specifically** | **79.2%** | **45.4%** |

**The 2/20 → 1/20 is NOT a regression.** One row crossed a sharp edge: R1 moved 29.9% → 30.2% against a
30.0% ceiling. Calling that "phase 1 lost a row" would be the band-edge artifact already flagged when it
ran the other way, and the caveat has to apply symmetrically or it is just advocacy.

**The real movement is H6, 79.2% → 45.4%** — the row no rout-contagion threshold could touch, because
H6's stubbornness is not at subunit granularity. Per-cell morale reaches it. Win-share also gained a row.

**Verdict: roughly neutral, one structural gain, flag STAYS OFF.** The reason is the one stated *before*
the measurement: **nothing consumes per-cell morale as a break condition yet.** Rout still evaluates the
whole-body aggregate — now better-informed, since it is derived from where damage actually landed, but
still whole-body. The map is populated and correct; nothing reads it to decide a SECTION has gone. That
is phase 2 (local break), and it is where the payoff should appear.

**The prediction is the point.** It was recorded before the first run and held across a discarded
measurement and a corrected one. Its first job was catching the silent no-op (a swing far larger than
predicted); its second is refusing to over-read a neutral result now that the direction is mildly
favourable. A prediction that only fires against bad news is not a control.

## 2026-07-25 — ED-MB-0041 phase 1 FIXES: two defects in the per-cell morale wiring

**1. A silent no-op I introduced — the exact pattern this audit exists to find.** With cell morale
seeded, `eff_morale` reads the CELL MAP and ignores the scalar; but `erode_morale`/`pull_morale` WRITE
the scalar. So enabling per-cell morale silently disabled: the canonical §A.4 casualty/exhaustion
erosion, the DG-4 sibling-coupling pull, and the stochastic-rout punch that drives morale ≤0 to force a
break — meaning **`PC_STOCHASTIC_ROUT`, ratified an hour earlier, stopped working whenever
`PC_CELL_MORALE` was on.** Measured: `erode_morale(4.0)` left the aggregate at 6.0 while writing 2.0 to
a field nobody read. Fixed by routing body-wide morale uniformly across cells: the aggregate is the
weighted mean, so subtracting `amount` from every cell lowers it by exactly `amount`. Scalar and
cellular models stay numerically identical for body-wide effects; cells diverge only through LOCAL
damage, which is the point.

**What caught it was a prediction made before looking.** I stated that phase 1 should move the gauge
*modestly* and that a large swing would be a warning sign rather than a win. H3 swinging ~66 → 40
tripped that immediately. Without the prediction there was a ready-made explanation — "per-cell break
makes bodies come apart earlier" — and a broken configuration would have been banked as a success.

**2. A coupling fault.** `_erode_cell_morale_from_damage` hangs off `_apply_with_spill`, the single
owner of casualty application, which is deliberately duck-typed. Reading `atom.cell_morale` directly
made a MORALE feature impose a structural requirement on the DAMAGE substrate. `getattr` now; the fault
was the coupling, not the test double that exposed it.

**Process note, recorded because it caused a bad push.** I ran `valoria_local --staged | tail -2 && git
commit`. The pipe means the chain sees `tail`'s exit status, not the gate's — so a FAILING co-file gate
was masked and the commit proceeded. Gate output must not be piped when its exit code is what gates the
next command.

## 2026-07-25 — ED-MB-0041 phase 1: the cell is the primitive for MORALE

Jordan's directive ("the cell needs to be the primitive for morale, discipline, quality, stamina,
route, health, armour, facing, damage, troops count") and its earlier statement of the mechanism:
*"cells get modulated by subunit holistic scoring, but the cells themselves are what aggregate into
those scorings in the first place, so a cell should be able to have worse morale than another cell in
same subunit."* **That last sentence was literally unrepresentable** — the cell was the primitive for
geometry only (position, facing, contact, casualty placement); every piece of STATE was a subunit
scalar, so a rear cell being cut down and a front cell holding shared one number.

**Two-way loop, not a broadcast:**
- **AGGREGATE UP** — `eff_morale` is now the troop-**weighted** mean of live cells, derived rather than
  stored. Weighted so a nearly-empty shattered cell cannot drag the body as hard as a full one; a flat
  mean would let a cell holding three men count as much as one holding a hundred, and a body would read
  as broken while nearly all its strength was still steady.
- **MODULATE DOWN** — `cohere_cells` pulls each cell toward the body's holistic value, **signed** (a
  steady body steadies a shaky corner; a disintegrating one drags a firm corner down) and
  discipline-gated, because holding when your neighbours are hit is what discipline names.

**Erosion rides on `_apply_with_spill`**, the single owner of casualty application, so *every* path that
kills men — melee, volley, pursuit, freed-attacker, cellwise facing-weighted — shakes the cells it
killed them in, with no caller needing to remember. Scaled by the FRACTION of the cell destroyed, not
the absolute count: losing 20 of 100 beside you is the same shock at any body size, and an absolute
scale would make dense cells look braver purely for being dense.

Demonstrated: concentrate damage on one cell of three and it holds **4.51 morale while its siblings
hold 5.94** — Jordan's test case, earned in play rather than injected.

`tests/valoria/test_cell_morale.py` (11 tests) pins the directive itself, both directions of the loop,
the troop-weighting, the discipline gate, the fraction-not-count erosion shape, and one invariant worth
calling out: **cohesion CONSERVES the aggregate** (`new_m = m + r(agg−m)` ⇒ weighted mean is unchanged).
If that ever fails, cohesion has become a free morale source and a body could steady itself forever.

Gated `PC_CELL_MORALE`, **default OFF** — verified inert: byte-exact goldens, stochastic-rout and
rout-contagion suites all green unchanged. Not yet measured on the gauge; that is the next step, and the
flag stays off until it is.

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

## 2026-07-25 — ED-MB-0041: the two gauge invariants that need no band (Jordan-approved)

The win-share gauge cannot tell a double envelopment from two lines colliding — both can produce the
same number, which is how the reachability sweep found a config that passes the Cannae row with
envelopment pathing switched OFF. Two properties close that gap from opposite directions, and neither
needs a band or a judgement call.

**1. Reverse-pair side symmetry** (`audit/.../reverse_pair_symmetry.py`). `decA(X vs Y) + decA(Y vs X)`
must be 100: which army occupies the engine's "side A" slot is bookkeeping, not physics. Distinct from
the pre-existing `symmetry_probe.py`, which tests MIRROR symmetry (identical armies → 50/50) and is
structurally blind to an interaction asymmetry. Measured at n=60:

| pair | fwd | rev | sum | deviation | sigma | verdict |
|---|---|---|---|---|---|---|
| H2/H9 | 49.2 | 65.0 | 114.2 | +14.2 | **+1.6** | OK — *not* a defect |
| H3/H10 | 61.0 | 76.7 | 137.7 | +37.7 | **+4.5** | ASYMMETRIC |
| H4/H11 | 6.7 | 55.0 | 61.7 | −38.3 | **−5.3** | ASYMMETRIC |

**This corrects my own earlier reporting.** I had described all three sums (114.2 / 137.7 / 61.7) as
evidence of a side-dependent mechanism. Reporting the deviation in units of its own standard error
shows H2/H9 is **+1.6σ — consistent with noise**. The defect is confined to the *envelopment* rows,
which localises it far more sharply and is consistent with ED-MB-0039's envelopment-stability
diagnosis. A raw percentage-point threshold would have hidden that distinction entirely.

**2. Casualty/duration realism** — a SECOND scoreboard in `gauge_mb`, reported beside the win-share
count and deliberately *not* folded into it, so the existing 10/20 figure stays comparable with every
number already in the ledger, handoff and PR bodies.
- `matchup()` previously averaged `a_cas`/`b_cas` over **all** seeds regardless of who won — the wrong
  quantity: the sources constrain what the LOSER lost and how much less the WINNER lost, and a near-even
  matchup washes that asymmetry out. Now conditioned on the outcome (`win_cas`/`lose_cas`), plus a
  `capped` rate (seeds that ran to the turn cap without resolving).
- Bands are in-repo or logical consequences of in-repo values, **not invented literature intervals**:
  loser 15–30% is the repo's own rout-onset band (ED-MB-0031); winner <15% is that band's
  *contrapositive* (the winner did not break, so it sits below the break floor); the cap rate is
  structural, not historical.
- **Duration is deliberately NOT banded absolutely.** An engine turn has no defensible mapping to real
  time, so any interval in turns would be fabricated to look grounded. Only the cap-hit rate is banded.
- `None` (not `0.0`) when nothing resolved — treating an absent measurement as "the winner lost
  nothing" would turn the engine's most broken rows into its cleanest passes.

**First result, and it is stark.** The H1 *mirror* passes win-share at 50.0 while killing **~85% of the
loser and ~26% of the winner** against a 15–30% / <15% expectation. Casualty-realism scores **0/20**.
The win-share gauge has been reporting a green mirror on a battle that annihilates both sides.

Pinned by `tests/valoria/test_gauge_invariants.py` (8 tests). Both invariants are currently RED and
marked **xfail, not skipped**: the assertion runs every time, does not redden CI for a known-open design
gap, and flips to XPASS the moment it is fixed. Sample size is documented as a **power** limitation
rather than glossed — H3/H10, a +4.5σ defect at n=60, XPASSed at n=24, so an XPASS at suite-n is a
prompt to re-measure at n=60, not evidence of a fix. Also single-sourced the 18/20 turn caps, which
were duplicated literals about to become four copies.

## 2026-07-25 — ED-MB-0041 Tier-2: dead machinery wired or deleted + provenance retag

Seven items from the deep adversarial audit's Tier-2 list ("wire or delete, no third option"). Every fix
carries a regression test verified to **fail** against the pre-fix code, not merely to pass after it.

- **`dynamic_facings` — DELETED.** A write-only parallel facing store: built by `run_battle`, passed into
  `resolve_engagements` (which never read it), written by `_rotate_defender_facing`; its only reader
  `_atom_avg_facing` had zero call sites in the corpus. The concept is live and better served by
  `Subunit.cell_facing_vec` (discipline-gated slew, rout flip, and what `_octagon_cell_mods` actually
  reads). Behaviour-preserving by construction — **byte-exact goldens confirmed unchanged**.
- **`_front_fixers` — SCOPE FIXED.** Computed inside `resolve_engagements` from that call's pair list,
  which under `CASCADING_ENABLED` is one cascade sub-phase *group*, not the tick. A defender pinned
  frontally in group 0 and flanked in group 1 saw an empty fixer set and wheeled freely — the Cannae
  shape exactly, so the mechanism was dead in the case it exists for. Hoisted to `_compute_front_fixers`,
  computed once per tick, threaded in like `eng_counts`/`atom_sides` already were.
  (`tests/valoria/test_front_fixer_scope.py`, 3 tests.)
- **`cell_last_speed` — MADE AN IMPULSE, plus a charger-role latch (and a correction to my own
  diagnosis).** Both paths `continue`d past a halted cell without touching the speed map, so a cell kept
  the speed it charged in for the rest of the battle — and a cell is halted exactly when it is in contact,
  so every melee cell scored its charge impetus on every tick of a grind. Halted cells (and bodies ordered
  to `hold`) now record 0; the impact tick is unaffected because `halted_cells` is rebuilt from
  *pre*-movement contacts, so the charge still lands once, at impact.
  - That alone collapsed the pike-vs-cavalry retention margin from >0.02 to **0.0035**. The modelling
    error was one level up: `a_mom > b_mom` identifies **who the charger is**, it is not the cause of the
    recoil — the cause is a mounted body pressed onto set poles, and a wall does not stop repelling after
    one tick. The charger role is now **latched at impact** (`atom._pressing`) and held while the pair
    stays in contact; brace, frontal zone, cavalry-only and the reach test are all still re-evaluated
    every tick, so the wall stops repelling the moment it is broken, flanked or out-reached. The latch
    expires when the bodies part and at the battle boundary.
  - **CORRECTION.** I first recorded this as a Tier-3 punt, on the reading that the impulse *cost* gauge
    row C1 (cavalry vs a steady unbraced line — the Burkholder/Sabin anchor), which I had measured at
    85-87%. Bisecting against a clean pre-Tier-2 tree showed the opposite: **C1 is 86.7% at the baseline**,
    and the impulse is what brings it to **48.3%, inside its 35-55 band**. I had attributed a pre-existing
    failure to my own change and written up a trade-off that did not exist. With the latch both anchors
    hold at once. (`tests/valoria/test_charge_momentum_impulse.py` for the impulse,
    `tests/valoria/test_charger_latch.py` for the latch's full lifecycle — set, survives the differential
    going flat, released when the bodies part, cleared at the battle boundary.)
- **`col_grid` — REBUILT FROM LIVE CELLS.** Built once in `Unit.__post_init__` from the spawn footprint;
  `sync_col_grid` refreshed only `density`, only for columns already in the list. Column membership was
  frozen at spawn, so a body that wheeled or drifted occupied columns absent from its own grid — at which
  point `_fatigue_sigma` found no live blocks and returned 0.0 and `_defender_depth` returned 0.0. **No
  fatigue and no depth-based charge absorption, for precisely the manoeuvring units.** Membership and
  per-column `depth` now track live cells (dead cells excluded so an emptied rank stops padding depth);
  stamina/start_density carry over for surviving columns. (`tests/valoria/test_col_grid_rebuild.py`, 3 tests.)
- **Rout triggers — PUT ON ONE CLOCK.** Morale collapse was checked per tick; annihilation
  (`troop_total < SUBUNIT_ROUT_FLOOR`) only at a phase boundary, every `TICKS_PER_PHASE`(=6) ticks, so a
  subunit ground below the floor kept fighting at full effectiveness for up to 5 more ticks.
  `rout_resolution` keeps its boundary check (idempotent), so §A.12 sequencing is untouched.
- **`PC_WHEEL` — PORTED TO THE LIVE PATH.** Shipped defaulting **ON** and was a no-op: its only consumer
  sat in legacy `advance_cells`, which returns early on the node path. Now a `_resolve_maneuver_goal`
  branch — a body whose whole footprint lies beyond the enemy's frontage turns in on the nearest enemy
  cell rather than marching its spawn file into empty air. Inert for any body with a file inside the enemy
  frontage. **This fixed the broken instrument at gauge row H6**, which read 0.0/0.0 casualties across
  60/60 seeds (audit §5.1) and now resolves.
- **`yielding` — CLEARED AT THE BATTLE BOUNDARY.** The one DG-2 transient `reset_morale_between_battles`
  missed; with rally off nothing else clears it, so a subunit that yielded once stayed flagged for the
  rest of the campaign.
- **Provenance: 24 dangling citations retagged.** Tier-0.1 deleted `tests/sim_verification_ledger.json`;
  24 constants across `config.py`/`bat.py`/`engine.py`/`workbench/server.py` still cited it as
  `[canonical: ...]` — a tag pointing at a file that no longer exists, the one state the audit calls
  unacceptable. All retagged **`[CALIBRATED-DEBT: … — magnitude fitted to engine behaviour, no external
  source]`**, naming the deleted whitelist so the history is not laundered either. `CALIBRATED-DEBT` is a
  fourth honest label beside GROUNDED / JUSTIFIED / DECLARED-DIVERGENCE and says what the others cannot:
  *this number has no source at all*. Twenty-four is the honest count of that debt today.

**Gauge (multi, the resolving mode): 5/20 → 10/20**, verified on the shipped tree. Not a tuning result —
no constant was touched. These fixes had been silently removing effects the model intended to have (or,
for momentum, silently *adding* one: a permanent shock bonus for standing still). Rows now in band: H1,
H2, H3, H7, H8, H11, C1, C3, C5, C7. Still out: H4, H5, H6, H9, H10, R1, R3, C2, C4, C6. The same caveat as Tier-1 applies: the bands were
implicitly fitted around distortions that are now gone, so movement in either direction is expected and
is not evidence about the bands.

**Open, surfaced by this pass:** H3 (Envelopment vs Line) reads 61.0 and its reverse H10 reads 76.7 —
the same physical matchup with the armies swapped between the A and B slots, which should sum to ~100
and sums to ~138. The mirrors (H1 50.0, C3 50.8) are clean, so this is matchup-specific, not a uniform
slot bias. Not diagnosed here.

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

## 2026-07-24 — ED-MB-0037: remove superseded dead-mechanic constants + zeroed _envelopment_sigma
- Wire-or-remove sweep, removal half (Jordan "obviously you can unwire a dead mechanic if it's useless").
  Removed constants that were defined+exported but read nowhere and superseded by live mechanics:
  **PC_ENVELOP_SIGMA** + its `_envelopment_sigma` (percell.py) Increment-6 term — dormant at 0.0, the
  unit-level col-grid "wider side" overhang mis-targeted a split envelop army; superseded by the octagon
  flank multiplier + multi-side shock (B6) + perimeter/orbital-wheel envelopment (ED-MB-0035).
  **ROUT_FLOOR_LOSS_PCT** / **ROUT_EXHAUSTION_MORALE_HIT** (superseded by ED-MB-0036 SUBUNIT_ROUT_FLOOR +
  stochastic rout), **PC_FLANK_DEPTH_RESIST** / **PC_FRONT_RANKS** / **PC_FLANK_CAP** (never-wired flank
  scaffolding, superseded by the octagon per-cell angle model), **REACH_LONG** (registry.py, unread).
- **Byte-exact:** every removed term was already 0.0 or unreferenced on the live path; the Increment-6
  `_envelopment_sigma` call added 0.0 and is replaced by a comment. Goldens unchanged (4 modes verified).
- Measured **PC_FACING_MODEL=1 → gauge 3/20** (regresses from 5/20) — confirms its "do not enable"
  calibration-debt (PC_FACING_SLEW_BASE unratified). Left OFF; flagged for Jordan. Gauge holds 5/20.

## 2026-07-24 — ED-MB-0036: wire orphaned MORALE_EROSION_DAMP + SUBUNIT_ROUT_FLOOR
- Wire-or-remove dead-mechanic sweep (Jordan directive). Both were defined+exported but never read.
  **MORALE_EROSION_DAMP** (0.7) → the §A.4 casualty/exhaustion morale erosion (`erode_morale(min(loss,3.0)*
  DAMP)`) — slows the bleed → longer, attritional battles; applied ONLY to gradual erosion, not the
  stochastic-rout punch. **SUBUNIT_ROUT_FLOOR** (80) → `rout_resolution`: a subunit also breaks when its
  troop total falls below the floor (too few to hold), independent of morale.
- Gauge unchanged (5/20, no regression); rout/morale tests green (22 passed). Goldens re-recorded (4 modes).
- Next: remove superseded constants (ROUT floors, PC_FLANK_DEPTH_RESIST, REACH_LONG, structural) + zeroed
  PC_ENVELOP_SIGMA; keep PC_ROTATE_FLOOR/REFILL_FLOOR (planned rotation T2/T3); measure PC_FACING_MODEL.

## 2026-07-24 — ED-MB-0035: wire perimeter.py + cavalry orbital-wheel envelopment + B6
- Orphan audit found **`perimeter.py`** (target-point/face-normal primitive, task #18) built but never
  wired. **Wired** into `_envelop_goal`: infantry enveloping wings turn onto the enemy's nearest FLANK
  face. **Cavalry orbital wheel** (`_envelop_wheel_goal`, Jordan "maintain distance = radius = wheeling"):
  a fast encircler holds a field-coordinate radius (enemy half-extent + `ENVELOP_STANDOFF=8`) and wheels to
  the enemy REAR, then closes — reaches the rear of a MOVING enemy. **B6**: multi-side shock now computed
  once on the full tick (`_compute_atom_sides`) and threaded through cascade sub-phases (was per-sub-phase
  → never fired for a front+rear body).
- **Result:** C4 cav-envelop-vs-Line **6 → 83** (into band 75-95); C7 holds 100; honest gauge **4 → 5 / 20**.
- `PC_ENVELOP_SIGMA` left 0.0 (Incr6 targeting mis-IDs the split army's thin wings; naive enable rewarded
  the defender). Full orphan inventory: `audit/2026-07-22-mass-battle-stress-test/orphaned_mechanics_audit_v1.md`.
- Goldens re-recorded 4 modes; `tests/valoria` maneuver/octagon/perimeter/reserve green (20 passed).

## 2026-07-24 — ED-MB-0034: field-coordinate unification (Fable-audit B1+B2+B3)
- Jordan directive ("nothing is golden"; "we're using field coordinates ... abandon [the spawn lattice]").
  Unified the cell-position accessors onto the live `_node_pos` field, off the dead `starting_position +
  cell_offsets` spawn lattice (not updated on the field path). **B1** `_oriented_abs_map` node branch →
  `_oriented(atom)`, skip absent ids (no `(0,0)` default): wedge contact cells stop collapsing to origin
  (**H2 decA 0.0 → 40.0**); grid branch also → `_oriented` (byte-identical for legacy). **B3** octagon
  `_octagon_dmg_mod`/`_per_cell_angle_mod` → `_oriented_abs_map` (live map; **H1 mirror → 52.5, in band**).
  **B2** `iter_cells` reads live `_node_pos` (feeds col-grid/fatigue/casualties). Added `width`/`depth` to
  gauge `make_unit`.
- **Goldens re-recorded all 4 modes** (nothing-is-golden): `unit`/`cell`/`unit_field`/`cell_field`;
  byte-exact test EXPECTED updated. `tests/valoria` green.
- Honest gauge still ~4/20: the prior 5/20 included FALSE C2/C6 passes (brace "repelling" off the broken
  contact map) — now honestly failing pending the box-brace. **Dominant remaining issue: envelopment
  delivers 0%** (H3–H6) — the split centre is crushed before the wings arrive; needs intent-on + B6 +
  wing timing + box-brace + B2b (col-grid per-tick rebuild). See `full_implementation_plan_v1.md` §1.5.

## 2026-07-24 — ED-MB-0033: Fable logic audit — Part A remediation (9 defects in this session's own work)
- Five Fable-tier read-only adversarial auditors (one per logical lane) traced ED-MB-0027..0032 and found
  9 defects; all fixed. A1 (CRITICAL): `make_unit`→`build_army` filled the §B.2 cavalry preset Power 5
  (spec never forwarded power/discipline) → gauge cavalry silently P4→P5, contaminating C-row verdicts;
  forward power/discipline explicitly. A2 (HIGH): `gauge_run.py` re-implemented the verdict and dropped
  both guards (`dec_n>0`, draw gate) → all-draw R3 false-passed on the `decA=50` sentinel → the reported
  "8/20" was inflated; delegate to `g.run()`. A3 (HIGH): ED-MB-0032's deterministic `frac·EV` mu-shift
  crossed the `net<=0` degree boundary (Jensen gap; sub-1 pools never Failed) → realise the fractional die
  STOCHASTICALLY (one extra die w.p. `frac`) — preserves EV+variance+Failure boundary. A4 (MED): frac-pool
  σ-boost read `sqrt(fractional)` → pass `floor(pool)`. A5 (HIGH): stochastic-break `erode_morale` on a
  None-morale subunit wrote the SHARED pool negative → routed every sibling; materialise own morale first.
  A6 (HIGH): `reset_morale_between_battles` never cleared `_rout_breakpoint` and loss was spawn-based →
  auto-rout on phase 1 of every later battle; clear breakpoint + re-base `_start_troops`. A7 (MED-HIGH):
  `erode_morale(eff+1)` with `eff<=-1` RAISED morale → clamp `max(eff+1,0)`. A8 (MED): `_rout_resilience`
  read LIVE discipline → `eff_discipline_start`. A9 (LOW-MED): `own_strength:FRAC` + numeric trigger
  payloads never range-checked → eager `(0,1)`-strict validation in `Order.__post_init__`.
- Honest re-measurement (A1+A2 corrected, n=20): baseline **5/20**; +`PC_STOCHASTIC_ROUT` **6/20** (R3 now
  correctly UNRESOLVED, not a false pass). Remaining 14 out-of-band rows are Part B pre-existing geometry
  bugs (B1-B4) — move goldens, filed for Jordan ratification.
- Byte-exact: every fix is `PC_*`-gated / campaign-boundary / validator-only → bat.py **4/4 modes**
  (unit, cell, unit_field, cell_field) byte-exact. `tests/valoria` green; `test_fractional_pool.py` updated
  (sub-1 pool now stochastic-EV + can-Fail, replacing the deterministic-EV assertions that codified A3).


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
