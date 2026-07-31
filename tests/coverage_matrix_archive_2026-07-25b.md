# Coverage Matrix — archive slice, cut 2026-07-25 (second cut)

Sections moved out of `tests/coverage_matrix.md` to keep it under the 15,000-token register cap
(`tools/ci_register_size_check.py`). Verbatim; nothing condensed or dropped. Covers the
ED-MB-0022..ED-MB-0032 span (Feigned Retreat, Reserve commit, DG-2 yield residuals, deployment
primitives, honest-gauge density, closing ranks, intent-as-resolution, conditional orders, the
stochastic-rout breakpoint and the fractional pool).

## 2026-07-23 — ED-MB-0032: fractional combat pool ("pool must be fractional")
- Jordan directive: the continuous pool was floored to an integer die count before `roll_pool`,
  discarding the fractional remainder. `roll_pool_fractional`: integer part rolls real d10s, fractional
  remainder contributes its EV (`PER_DIE_NET_EV=0.4`, the TN-7 face-rule EV); sub-1 pool contributes only
  its fractional EV (no floor to a guaranteed die). Sigma-boost reads the fractional pool. Wired into the
  sigma-head `a_net`/`b_net`.
- Verified: pool 3.0 vs 3.7 differ in mean net by ~0.7·0.4; integer pools reduce to `roll_pool`; monotone
  across integer gaps. Gated `PC_FRACTIONAL_POOL` (default OFF → byte-exact, bat.py EXIT=0). Tests:
  `test_fractional_pool.py` (6).
- Gauge ~neutral (correctness/precision fix, not band-optimizer); fair fractional ruler needs its own
  calibration pass. (Archived the 2026-07-02/04/05 blocks to `coverage_matrix_archive_2026-07-23.md`.)

## 2026-07-23 — ED-MB-0031: stochastic rout breakpoint at the historical 15-30% casualty band
- Jordan historical research: "routs occur as early as 15% losses with 30% the upper hand." The canonical
  §A.4 casualty→morale steps don't fire until 50% losses, so units grind to ~90% before breaking. Models
  du Picq will-to-fight collapse: each subunit draws a **fractional** break-point in [ROUT_ONSET=0.15,
  ROUT_CAP=0.30], skewed by resilience (discipline + starting morale) — a steady body holds toward 30%, a
  shaken one breaks toward 15% — and routs when its casualty fraction crosses it.
- Result (rout_probe OFF→ON): loser casualty-at-rout **91.7%→31.8%** (even), 88.8%→30.3% (disc5v3);
  winner ~20%→~10%; length 2.5→1.1 turns.
- Fractional throughout (random draw + fractional band + fractional loss), reproducible under the seeded
  RNG. Gated `PC_STOCHASTIC_ROUT` (default OFF → no draw → **byte-exact**, bat.py EXIT=0; NOT inert when
  on — moves goldens, needs_jordan). Tests: `test_stochastic_rout.py` (7).
- **Coupled next:** lower per-tick lethality (battles now end at ~30% but in ~1.1 turns; casualty chunks
  overshoot the break-point) + fractional dice, then re-gauge vs Dupuy/Sabin.

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

---

<!-- [ED-MB-0061, 2026-07-30] Relocated VERBATIM from tests/coverage_matrix.md to keep that
     register under its 15,000-token cap. Nothing condensed, nothing dropped. -->

## 2026-07-29 — ED-MB-0045 plan-v2 A1a: field goldens bisected + re-recorded after 5 days red

Both `bat.py` field goldens (`unit_field`, `cell_field`) had been RED since PRs #235/#236
(2026-07-24/25) re-recorded only the grid modes — undetected because nothing runs the field
`--check` (the gap A1b's CI job closes). Bisected in a worktree across `4b80ad5..584c683`, pins
fixed (the `_PINNED_OFF` vector with the two field toggles inverted, `PC_STOCHASTIC_ROUT` explicit
per axis): **two movers, commit-level** — (1) #235 `fbc93b0`'s change set at fixed rout=0
(`unit_field` `d44f211f…→27aa9ee0…`, `cell_field` `a1a97940…→3a5807fb…`; NOT decomposed to a single
mechanism on the field arm — `PC_WHEEL`'s node-path port is an unmeasured second candidate beside
impulse momentum); (2) #236 `584c683`'s `PC_STOCHASTIC_ROUT` default flip 0→1 as a **pure config
effect** (#236's code alone byte-identical at rout=0 — the identity its `set_morale` sweep predicts
at `PC_CELL_MORALE=0`). #233/#234 verified byte-exact on both field modes at rout=0. Closure by two
instruments: `584c683`@rout=1 reproduces HEAD's digests exactly, and
`git diff 584c683..cd7f0d0 -- tests/sim/mass_battle/` is empty. Controls: base@rout=0 reproduced
BOTH prior goldens byte-exactly (positive control for environment + pin vector); all four modes
`--check` green ×2 consecutively post-re-record (8/8); `PYTHONHASHSEED` unset ⇒ every process drew
a fresh hash seed and digests still agreed (hash-order independence, empirical). Recorded on
Linux/Python 3.11.15; reference-env confirmation = A1b's first CI run. Opus critic pass applied
(commit-level attribution honesty; source-diff closure). No engine `.py` touched; no constant
tuned; goldens moved = the disclosed re-record itself.

**The sweep.** `eff_morale` reads the cells once seeded and never falls back to the scalar, so every
`.morale =` in the engine was a silent no-op under the flag — which is what confounded the retracted
measurement. Two owners now: `Subunit.set_morale` / `Unit.set_morale` (absolute), with
`erode_morale`/`pull_morale` already owning the relative write. Routed: `between_turn_recovery`,
`reset_morale_between_battles`, the Command=0 rout write, `Unit.cascade_morale_hit`. One site stays
bare and annotated — `core/state.py` materialises the scalar so the stochastic-rout punch stays local
to one subunit; rewriting the cells there would flatten genuine divergence.

**A defect in the sweep, found by probing rather than assuming.** Routing `between_turn_recovery`'s
*unit-level* line through `set_morale` **re-inflated damaged bodies**: recovery is a bounded increment,
not an absolute statement, and the unit pool is stale once cells own the state. A body knocked to 2.0
came back at 6.0 with the recovery constant at 0. That line stays bare; inheriting subunits recover via
`pull_morale`.

**The guard is field-parameterized on purpose.** `test_morale_write_sweep.py`'s `_CELL_OWNED` registry
means phases 3/4 (stamina, discipline, quality, hp, armour) inherit the same protection by adding a
key. Re-deriving the guard per field would repeat the exact mistake — fixing an instance instead of the
pattern — that caused the retraction. `test_the_guard_itself_can_fail` proves each registered pattern
still flags a planted write, because a guard that cannot fail reports safety it does not provide.

**Deliberately NOT swept, and recorded as a re-flip pre-condition:** the two harness writers in
`lanchester_signature.py` and `test_persubunit_stress.py`. They were swept, then reverted — the
anti-fabrication gate scans the changeset, so touching either file dragged ~100 pre-existing uncited
constants into a blocking gate. Inert while the flag is OFF; **must be swept before it flips**, because
`lanchester_signature` pins morale high specifically to *disable* rout. This is the cost that CLAUDE.md
§0.1's "sweep only what the task is load-bearing on, file the rest" exists to respect, and it showed up
within an hour of the rule being written.

**CLAUDE.md §0.1** records the five checks distilled from the retraction. The load-bearing observation:
§0 *already* demanded an adversarial pass, and one was performed — on the result's statistics, never on
its setup. Restating principles does nothing; the fix is naming what to attack and requiring an
artifact that proves it happened.
