# Coverage Matrix — dated archive overflow (2026-07-24)

Overflow from `tests/coverage_matrix_archive.md` per `references/atomization_rules.yaml`
("move closed-finding paragraphs to tests/coverage_matrix_archive_<date>.md and reset").

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


| Module | Commit | Canon | Verification |
|---|---|---|---|
| `sim/territory/settlement.py` | (T0-1) | `settlement_layer_v30.md §1.2-1.3` | SettlementState/ProvinceState derivation per §1.3 multipliers; smoke on T1 Seat + T9 Cathedral; 5 ledger entries with canon-verified quoted_text |
| `sim/thread/coherence.py` | (T0-2) | `threadwork_v30.md Part 3` | Coherence 10-0 track with §3.3 band transitions; smoke run through Stable→Dissonant→Fragmented→Fractured→Severed→Crisis; floor/ceiling clamps verified; just_transitioned fires once; 9 ledger entries with bold-marker-preserving quoted_text |
| `sim/cross_scale/handoff_rules.py` | (T0-3) | `scale_transitions_v30.md §3` | 8 handoff rules dispatched; TS-banded coherence cost (3 thresholds 30/50/70 verified); §3.9 fieldwork pass-through; invalid transition returns valid=False; 3 ledger entries |
| `sim/cross_scale/zoom_in_out.py` | (T0-12) | `scale_transitions_v30.md §4` | zoom_in valid/invalid phase routing; mid-Phase-5 deferral verified; board-degree Ob modifier 4-way table; zoom_out queues Domain Echoes + PC incap + Contested Figure wound; 8 mandatory triggers enumerated; 2 ledger entries |
| `sim/cross_scale/domain_echo.py` | (T0-13) | `scale_transitions_v30.md §5` | §5.2 amount-by-degree (4 cases); §5.5 Accord Echo (governance/destab/transfer/violence + invalid); §5.6 Thread Echo (Dissolution/Mending/Gap/Lock/PublicChurch/PublicVarfell + invalid); 5 ledger entries; PP-329 1-per-faction-per-scene cap documented |
| `sim/__init__.py` | (T0-4) | (declarations) | docstring updated to reflect Tier 0 progress |
| `sim/peninsular/ms_track.py` | (T0-5) | `params/core.md §MS Baseline Decay (PP-255)` | apply_ms_baseline_decay (-1/year) + apply_ms_delta; floor 0 / ceiling 100 clamp verified (100× -5 → 0; 100× +5 → 100); 6 ledger entries; DRIFT vs accounting._ms_decay logged |
| `sim/peninsular/season.py` | (T0-6) | `campaign_architecture_v30.md` | run_season composes advance_season → optional action_callback → run_accounting; 5-season smoke with arc boundary at 1 and 5; MS decay fires at season 4 via existing accounting; DRIFT vs mc_v18 inline logged |
| `sim/provincial/treaty.py` | (T0-7 partial) | `faction_balance_convergence_v12c §4.5 + §4.7` | process_treaty_expirations with TREATY_LAPSE_RATE_DEFAULT=0.90 verified (5/5 lapse at high rate); register_treaty + get_active_treaties helpers; propose_treaty raises (no canonized generic formation path; canon formation is Senator Outward per treaty_expiration_v30 §2); 2 ledger entries |
| `sim/world/insurgency_pipeline.py` | (T0-10) | `canon/02_canon_constraints.md §B GD-3` | GD-3 state machine: 2-season streak detection + formation event; L<3 promotion blocked; low-PT (avg=2) → extra-parliamentary RM variant; high-PT (avg=4) → parliamentary candidate; 6 ledger entries |
| `sim/world/npe.py` | (T0-11) | `designs/scene/investigation_systems_v30.md` SYSTEM 1 | Territory Social Ecology weights from prosperity/accord; NPC Genome 5-axis (stance/worldview/affiliation/compromise/volatility); Two-Tier Generation (archetype + d6 deviation, 5-6 flips axis); 10-NPC sample: 50% controlling-faction affiliation, 30% deviation 5+, arc-vector flagging works; 3 ledger entries |
| `sim/provincial/charter_liberties.py`, `sim/provincial/varfell_mandate_action.py`, `sim/autoload/npc_ai.py` | (T0-8/9/14 CANON-GATED) | (canon authoring required) | NOT IMPLEMENTED — Pass 2e (Hafenmark charter), Pass 2d (Varfell contamination audit), priority-stack contamination audit. Reclassified from Tier 0 to canon-gated bucket per stub_infill_plan §Canon-availability blockers. |
| `sim/autoload/game_state.py` (schema migration) | (post-Tier 0) | `stub_infill_plan Amendment 2026-05-19` | World gains 6 registries (practitioners/insurgencies/uncontrolled_streaks/npcs/npc_counter/treaties); 5 Tier 0 modules route through world stores with module-level fallback; 7-test integration smoke verifies cross-world isolation + module fallback + mc_v18 backward compat (battles_mean=31.8 at seed=42 N=5); serialize/restore unchanged (registries not yet in snapshot format) |
| `sim/territory/infrastructure.py` | (T1-1) | `settlement_layer_v30 §1.5-§1.7` | 4-axis Church infrastructure model. T9 seizure Ob smoke: Cathedral(-2)+Templar(-1)+Inquisitor(-1)+ChurchGov(-2)=-6 → capped to -4 per §1.5. Axis 1 mutual exclusion verified (Cathedral→Church removes Cathedral). Templar seed from Territory.templar preserved. 5 ledger entries. |
| `sim/territory/temperaments.py` | (T1-2) | `territory_temperaments_v30` | 17-territory temperament authoring (T1-T17 all assigned). 5-typology α/β coefficients per §1. Drift dynamics: strain_delta=3 on T1/T2 → drift=0.30 each, α shifts toward 0.9; strain_delta=10 accumulates to 1.0 clamp. Faction aggregates per §3 (Church α=0.2 strongly principled, Hafenmark α=0.55 mildly pragmatic). 4 ledger entries. |
| `sim/personal/conviction.py` | (T1-3a) | `conviction_track_v1.md §2-§3` (PP-718) | Per-Conviction Scar accumulation (Almud Order: 1→2→3 → crisis); Precedent independent (no cap collision); season cap suppresses same-season Thread re-Scar on same Conviction (mag=0); Certainty C5→mag+1, C0→mag-1 verified; 4 ledger entries |
| `sim/personal/beliefs.py` | (T1-3b) | `fieldwork_v30.md §5.5 + social_contest_v30.md §9.5` | add_belief/revise_belief/social_success; aligned win m=0→delta+1, m=4→delta=0 (cap); challenging win marks revision_pressure +1 and notifies conviction (pending_belief_revisions populated); cycle broken via late-import; 2 ledger entries |
| `sim/thread/operations.py` | (T1-4) | `threadwork_v30.md Part 2 + params/threadwork.md` | 7 operation entry points; Leap eligibility (TS<30 fail; TS=60 Ob=1); 9-operation smoke covers all degrees; FR Locking Object coh=-1 (FR surcharge only) verified; FR Locking Structural coh=-4 (-2 scale + -1 FR + -1 Partial); Mending Field coh=-2 always; POP recency table verified; coherence track erodes correctly across 8 ops to Crisis; 9 ledger entries |
| `sim/personal/combat.py` | (T1-5) | `combat_v30.md §1-§7 + PP-232` | Combat pool Agi×2+History+3 min 5 verified (Alice Agi=4 → pool=12); Heavy Blade short TN=6 verified; Light Blade vs Heavy armor +0 mod (net=0); Heavy Blunt vs Heavy armor +5 mod with PP-232 multiplicative STR×2×1.5=×3 (dmg=19 at net=2); Strike/Full Guard/Take a Breath/Dodge/Establish Distance resolve; Feint/Rescue/Disarm/Tie Up deferred Tier 2+; round-level resolution ordering per §4; 6 ledger entries |
| `sim/peninsular/ci_track.py` | (T2-1) | `conviction_track_v30 §3 PP-412` | PP-412 Step 1 +1 Momentum; Step 2 floor(Σ yield by PT) with PT5→+1, PT4→+0.5; Step 3 Assert; Step 4 Suppress cancels Momentum; Step 5 Hafenmark -1 at L≥4 (verified L=3 → 0); ceiling clamp at 100; 10-season smoke with Church L=6 produces +10/season prominent-territory yield; DRIFT vs accounting._ci_generation flat +2/Church-territory documented; 6 ledger entries |
| `sim/autoload/game_state.py` (helpers) | (bug fix 2026-05-19) | `PT_MAP / ACCORD_MAP` | canonical_pt(continuous_pt: float) -> int 0-5; canonical_accord(continuous_accord) -> int 0-4; nearest-neighbor at PT_MAP midpoints (1.75, 3.25, 4.75, 6.0, 6.75); round-trip verified on all PT_MAP / ACCORD_MAP entries + boundary cases; 1 ledger entry |
| `sim/peninsular/ci_track.py` (bug fix) | (re-verified) | `conviction_track_v30 §3 + victory_v30 §3.2 PP-534` | Step 2 yield re-bucketed via canonical_pt (was int(t.pt) drift); PP-534 Self-Control Rule added (Church auto-prominent in own territories); default state +1/season matches canon S1-S5 pacing; mid-game scenario +3/season matches canon mid-game pacing |
| `sim/world/npe.py` (bug fix) | (re-verified) | `investigation_systems_v30 §Ecology` | accord_int now via canonical_accord (was int+clamp drift); ecology weights now correctly: T2 canon=3 → high; T13 canon=1 → low; volatility offset works correctly (T13 NPCs avg 4.0 vs T2 avg 3.0) |
| `sim/provincial/mass_seizure.py` | (T2-2) | `victory_v30 §3.2 + campaign_architecture §1.3 + supersession 250715f` | Probabilistic declaration P=((CI-60)/40)^3.3 matches canon table exactly (1.0% at 70, 10.2% at 80, 38.7% at 90, 100% at 100); one-shot lifetime via world.clocks['MASS_SEIZURE_USED']; Pool=Influence+floor(CI/15), Ob=10-canonical_pt-infra_mod floor 1; PP-534 Self-Control via _church_is_prominent_for_seizure; T9 PT 5 + full Church infra → Ob 1 (max stack -4 cap) → seized at net=2; GD-1 conformant (world.winner unchanged); 7 ledger entries |
| `sim/personal/contest.py` | (T2-3) | `social_contest_v30 §1-§9` | Argue Pool (PA×2)+Hist-wound-fatigue (Alice 5*2+2=12, wounded 10, fatigued 11); resolve_exchange tracks Persuasion Track 1-9; tied exchanges +1 toward first-speak per §4; 3-exchange contest with Compromise outcome verified; 10-contest distribution 3A/3B/4 compromises; Belief alignment momentum integration via late-import (no cycle); 4 ledger entries |
| `sim/personal/knots.py` | (T2-4) | `knots_v30 (Pass 2g synthesis)` | Option A 2-tier (Distant/Close); formation prerequisites all checked (bonds<5 rejected, disposition<5 rejected, both TS<30 rejected, duplicate rejected); formation Spirit×2+History+0 vs Ob 2; tier from degree (Overwhelming→Close, Success→Distant); strain accumulation; capacity break at strain > tier_capacity; rupture trigger 'public_citation' → -1 Coherence via late-import (Alice 10→9); high-strain Close break → Conviction Scar via late-import; 7 ledger entries |
| `sim/thread/co_movement.py` | (T2-5) | `threadwork_v30 Part 4 + §4.3 ED-577` | 15 canonical cards CM-01 through CM-15 (Mending CM-16/17/18 deferred to §7.1); Object scale draw → unactualized (CM-09 ms_delta=-2 verified); Structural draw → actualized (CM-14 ms_delta=-3 verified); MS clock updates correctly (80 → 77); 16-draw test triggers reshuffle, all 15 unique IDs returned; 1 ledger entry |
| `sim/thread/collective.py` | (T2-6) | `threadwork_v30 §2.5` | Anchor selection by highest TS (Anchor TS=80 chosen over Helper1 TS=60, Helper2 TS=50); helper contribution floor(Cognition/2) (Helper1 cog=4 → +2 dice, Helper2 cog=4 → +2 dice); total pool 23+2+2=27 verified; lattice fracture threshold (remaining < expected/2) implemented; per-practitioner Coherence delta applied for Field scale (-1 per Leap survivor); operation degrades to Field Ob 5, Success at net=7 |
| `sim/thread/threadcut.py` | (T2-7) | `threadwork_v30 Part 6` | §6.1 Ontological Status canon body empty — flagged as canon gap (header only); §6.2 5-band perception (TS=0/25/45/65/100 all map correctly); mark_threadcut + is_threadcut registry; §6.3 +1 Rendering Strain per external op verified (1 op → strain 1; 6 ops → strain 7); §6.4 De-Actualisation triggered at strain ≥ max_wounds=6 (round=2 after 6 ops, triggered flag fires on first crossing); perception bands match canon §6.2 verbatim |
| `sim/thread/opposing.py` | (T2-8) | `threadwork_v30 §2.6` | opposing_engagement_modifier formula verified (B's TPS=6 → A's Ob +3; A's TPS=8 → B's Ob +4); 7-cell resolution matrix (Meets-Meets, Meets-Partial, Meets-Failure, Partial-Partial, Partial-Failure, Failure-Partial, Failure-Failure all coded); FR Lock vs Standard distinct (Composure 4 vs 2; knot Ob 2 vs 1); MS delta from worst-degree+1 rule for Shifting Object; Knot strain via late-import; apply_coherence_delta routes through coherence module |
| `sim/provincial/massbattle.py` (audit finding) | (non-determinism filing 2026-05-19c) | `stub_infill_plan Amendment 2026-05-19c` | mc_v18 non-determinism diagnosed: massbattle.py L630 roll_pool + L1053 volley_roll_pool call random.randint directly instead of using world.rng. Two consecutive run_batch(5, base_seed=42) diverge; random.seed(0) before run_batch produces deterministic output (battles_mean=32.8 both runs). Filed as follow-on; not fixed (would shift every mc_v18 batch result, requiring Phase 7 smoke re-baseline) |
| `sim/autoload/game_state.py` (schema migration #2) | (Tier 1/2 registries 2026-05-19) | `stub_infill_plan Amendment 2026-05-19` (extends migration #1 at 94dac72e) | World gains 8 fields: convictions, beliefs, knots, knot_id_counter, territory_infrastructure, npc_drift_state, threadcut_beings, comovement_deck; 6 consumer modules updated; cross-world isolation verified across 7 registries; module-level fallback preserved for world=None callers; mc_v18 backwards-compat verified |
| `sim/autoload/game_state.py` (per-record serializers) | (production save format 2026-05-20) | `stub_infill_plan Amendment 2026-05-19d` | 9 dataclasses gain to_dict/from_dict (CoherenceState+log, InsurgencyRecord, NPC, TreatyRecord, ConvictionState+log, Belief, Knot, InfrastructureState, ThreadcutState); serialize_world extended with 14 registries; restore_world reconstructs via late-imports; 26/26 round-trip checks pass; 14/14 old-schema tolerance checks pass (missing registries default empty); mc_v18 backwards-compat verified (battles_mean=38.0) |
| `sim/provincial/massbattle.py` (RNG fix) | (Deferred Migration Batch 2026-05-20, commit 54277ae) | `mass_battle_v30 §A.1 + params/mass_combat.md` | Closes 03ce9c79 non-determinism. 12 functions gain rng=None param (roll_pool, _roll_volley_pool, volley_phase, resolve_engagements, resolve_engagements_cascading, run_battle, run_multi_turn_battle, run_multi_unit_battle, pursuit_damage, recall_check, discipline_check_cascade, freed_attacker_damage); 21 internal callsites thread rng=rng; resolve_mass_battle passes world.rng. Pre-fix: same-seed batches diverged across runs and required random.seed() pin. Post-fix: byte-identical within process at same seed; module random.seed has no effect. Verified at N=5 base_seed=42 with global random.seed pollution between 3 runs; all identical. [GAP: hash-seed nondeterminism remains across Python processes — pin PYTHONHASHSEED=0 for cross-process reproducibility; filed for separate session] |
| `sim/peninsular/accounting.py`, `sim/mc_v18.py`, `sim/peninsular/season.py` (3-migration batch) | (Deferred Migration Batch 2026-05-20) | `conviction_track_v30 §3 PP-412; params/core.md §MS Baseline Decay PP-255; campaign_architecture_v30` | Deletes 3 legacy duplicates. accounting._ci_generation (+2 per Church-held territory, canon-violating) replaced with ci_track.apply_seasonal_ci. accounting._ms_decay replaced with ms_track.apply_ms_baseline_decay gated on world.season % SEASONS_PER_YEAR == 0. mc_v18 inline season block (L73-87) replaced with season.run_season(world, action_callback=_faction_actions_callback). Behavior shift: pre-batch Church CI gained +8/season at start; post-batch ≈ +1/season per PP-412 §3 Pacing canon. Authoritative re-baseline at PYTHONHASHSEED=0: N=10 base_seed=0 → battles_mean=35.5, win_share Crown:30/Varfell:70; N=10 base_seed=42 → battles_mean=33.4, Crown:40/Church:30/Varfell:30; N=5 base_seed=42 → battles_mean=37.6, Crown:20/Church:40/Varfell:40. Supersedes the 4 stale manifest figures (smoke 40.1; run_batch(10,42)=30.0; migration #1 baseline 31.8; migration #2 baseline 37.4 with random.seed(0) pin) |
| `sim/autoload/game_state.py`, `sim/provincial/faction_action.py` (hash-seed fix) | (Deferred Migration Batch follow-on 2026-05-20) | n/a — purely structural | Closes hash-seed-nondeterminism GAP filed in commit 105ae9e. Two leaks: (1) Faction.territories: set -> list (set str-key iteration depended on PYTHONHASHSEED); (2) _try_conquest candidate set wrapped in sorted() before rng.choice. Cross-process determinism verified across PYTHONHASHSEED in {0, 1, 7, 42, 99999} at N=10 base_seed=0 (battles_mean=34.1, Crown:4/Church:1/Varfell:5). PYTHONHASHSEED pin no longer required for reproducibility. Companion list-conversions: .discard() -> guarded remove; .add() -> guarded append |
| `params/bg/npc_priority_trees.md` (audit + dedup) | (Jordan-flagged 2026-05-17 priority-stack contamination audit) | n/a — canon-doc cleanup | Audit pre-implementation (consumer sim/autoload/npc_ai.py is NotImplementedError stub). Structural defects fixed: D-1 every tree duplicated L26-116 + L119-228 (byte-identical except whitespace), second block deleted; A-2 GD-2 mandatory-action precedence section added as §0 (mandatory pass before stochastic priority candidates per canon/02_canon_constraints.md §B); A-3 PP-NPC-04 initial state clarified (Collection flag = False at world creation). 8 stale-reference items (S-1..S-8: CI freeze threshold, Royal Decree canon, Löwenritter Autonomy survival, IP trigger, Warden Recognition, Cardinal mechanic, Crown T2/T4 hardcode, post-founding RM behavior under GD-3) require Jordan input — captured in designs/audit/2026-05-20-npc-priority-trees/audit_findings.md |
| `sim/thread/opposing.py`, `sim/thread/co_movement.py`, `sim/provincial/excommunication.py` (legacy-duplicate migration follow-on) | (sweep follow-on to commit 105ae9e) | `params/core.md PP-255 MS; ci_political_v30` | Three additional inline clock arithmetic sites found during post-batch sweep, migrated to dedicated track modules. opposing.py L229 (MS clamp), co_movement.py L142 (MS clamp), excommunication.py L165 (CI ceiling). All three now route through ms_track.apply_ms_delta / ci_track.apply_ci_delta — single canonical surface. Behavior verification: N=10 base_seed=0 produces battles_mean=34.1 (matches commit 3c2c428 baseline exactly; pure refactor) |
| `tools/index_gen.py`, `canon/editorial_ledger_summary.yaml` (M6 partial) | (Architecture V2.4 M6 gap) | `project-architecture-valoria-v2_4.md <completeness_enforcement> M6` | Closes two of three M6 defects: (1) HTML comment in YAML output replaced with YAML # comment; (2) generate_editorial_summary signature extended with archive_yamls so next_id is computed across active + archives (was archive-blind: old next_id=824, new=865 — 41 IDs the old code missed). Strict yaml.safe_load now passes on regenerated summary (210 total entries across 10 archives + active). Third M6 defect (regex-over-prior-summary fallback) remains as defensive path inside _collect_ed_entries — acceptable since yaml.safe_load is tried first. file_index_summary.md tree-walk integrity not in this scope (separate function family) |
| `sim/peninsular/accounting.py` (insurgency + NPE wire-up) | (Roadmap steps 2 + 3 from session 2026-05-20) | `canon/02_canon_constraints.md §B GD-3; designs/scene/investigation_systems_v30.md SYSTEM 1` | accounting.run_accounting extended: after CI+MS, invokes check_insurgency_triggers (GD-3 a-b emergence), iterates check_insurgency_promotion over existing insurgencies (GD-3 c-e), then simulate_npc_actions for territory-level NPC drift. Both modules T0-verified (T0-10, T0-11) but previously uninvoked from season loop. Behavior verification: N=10 base_seed=0 yields battles_mean=34.1 (matches pre-wire baseline; insurgencies don't form in short runs). Authoritative N=100 base_seed=0 captured: battles_mean=34.2, Crown 40 / Church 5 / Hafenmark 1 / Varfell 54 |
