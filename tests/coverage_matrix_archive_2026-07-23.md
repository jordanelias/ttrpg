# Valoria Simulation Coverage Matrix — archive part (oldest sections, split off 2026-07-23 for the 50k cap)
# Chains before coverage_matrix_archive.md.

## Archived 2026-05-20 (weapon-system v2 trials + Pass 2k checkpoint)


|-----|-----------|--------|
| Linear HP (End×6+16) | Reduces End dominance | Tested ✓ |
| Pool Softcap (Agi >4 → +1D) | Compresses Agi advantage | Tested ✓ |
| 1H commit bonus (+2D) | Specialist viability | Tested ✓ |
| Wrong def +2 dmg | Simplified triangle | Tested ✓ |
| **Combined result** | **None: PASS (63%). Heavy: PASS at 75% (Strong 75%)** | **Iteration complete** |

### Iterations 5-6 (2026-05-14)
| Finding | Status |
|---------|--------|
| Crit rate 60% at canonical >= 3 | P1 — threshold needs raising to >= 4 or >= 5 |
| Mace-only commit bonus (+2D for TN > 7.0, 1H) | Tested ✓ — best specialist fix |
| HP End×5+20 | Tested ✓ — Tough drops to 62% unarmoured |
| **Best config unarmoured PASS (62%)** | **Iteration 6 final** |

### v23 Complete Audit (2026-05-14)
| Phase | Tests | Status |
|-------|-------|--------|
| 1. Half-point TN | T1.1-T1.3 | 3 PASS |
| 2. Weapon-armour | T2.1-T2.4 | 1 PASS, 3 PARTIAL |
| 3. Multi-attack | T3.1-T3.3 | 2 PASS, 1 PARTIAL |
| 4. Defense triangle | T4.1-T4.4 | 4 FAIL → simplified |
| 5. Distance | T5.1-T5.3 | 1 PASS, 2 PARTIAL |
| 6. 2H/Longsword | T6.1-T6.3 | 2 PARTIAL, 1 FAIL |
| 7. Equal-budget | T7.1-T7.2 | 2 PASS (arena 3+5 unarmoured), 4 FAIL |
| 8. Crits | T8.1-T8.3 | 2 PASS, 1 P1 |
| 9. Integration | T9.1 | 1 PASS |
| **TOTAL** | **26 tests** | **12 PASS, 8 PARTIAL, 10 FAIL** |
| **Open decisions** | **12** | **D1-D12 in audit** |

### D6/D8 Tests (v24, 2026-05-15)
| Decision | Status |
|----------|--------|
| D6 Shield +3D/+4D | DEFERRED — amplifies Tough dominance, needs loadout system design |
| D8 Bash table +4→+3 | REJECTED — barely changes results (75→74%), gap is STR×3 not table |
| D1-D5 ratifiable package confirmed | HP, Pool Softcap, Crit, Mace, Triangle — all tested ✓ |

### All-Directions Audit (v25, 2026-05-15)
| Finding | Status |
|---------|--------|
| End ROI +34-48pp per point (P1) | Wound snowball root cause. D15 proposed (wound cap −2D) |
| Dagger overperformance (P1) | D14 short −2D vs Med/Heavy fixes it (79%→65%) ✓ |
| Arming sword fails N without shield (P2) | D6 deferred to loadout |
| Liechtenauer Vor/Nach | +7-14pp init advantage ✓ |
| Harnischfechten attack selection | Correct (Cut→Thrust at Medium) ✓ |

### P0: Stamina Quantization Cliff (v25, 2026-05-15)
| Finding | Root Cause | Fix |
|---------|-----------|-----|
| End +42.5pp/point | Stamina 24→25 cliff (4.0→4.17 rounds at cost 6) | Stam=20+End |
| HP contribution only +10.5pp | HP is not the dominant factor | D1 (End×5+20) helps but secondary |
| Wound cap has no effect | Fights end by yield, not wounds | D15 unnecessary |

### PP-717 NERS Audit (v26, 2026-05-15)
| Assessment | Result |
|------------|--------|
| Mode A (formula validation) | PASS — no boundary issues |
| Mode C (interaction chains) | PASS — 2 downstream flags (mass combat TC, Pool Softcap × crit double reduction) |
| D1 MW Cap NERS | N✓ E✓ R~ S✓ |
| D2 Pool Softcap NERS | N✓ E~ R✓ S✓ |
| D3 Crit ≥4 NERS | N✓ E✓ R✓ S~ |
| D4 Mace +2D NERS | N~ E✗ R✓ S~ — recommend redesign (remove Blunt TN penalty) |
| D5 Wrong def +2 NERS | N~ E✓ R~ S✓ — too small to matter (5% HP/duel) |
| All-directions | Top-down ✓, Bottom-up ✓, Vertical ✓, Diagonal ✓ (init×triangle weak), Lateral ~ (Pool Softcap combat-only), Horizontal ~ (Heavy arena 0 still fails) |


_v25 section (2026-05-15) archived to `tests/coverage_matrix_archive.md` 2026-05-18 (Step 4.2 commit) per pre_commit_gate size discipline. Section covered: Geometry expansion + dynamic wide-wing pathing + sightline. Recover via git or archive file._

## Phase 11 (2026-05-17) — Scene combat C4 (M1+M2+M3) empirical test

| Field | Value |
|---|---|
| Scope | Personal-scale combat. Test M1 (reach gate) + M2 (4-stance counter) + M3 (init preempt) atop Phase 10 baseline. |
| Sim | tests/sim/scripts/phase11_c4_v0.py |
| Writeup | tests/sim/phase11_c4_v0_2026-05-17.md |
| Trials | N=3000 per matchup; symmetric calibrations 49.9% and 48.5% (~50/50 ✓) |
| Coverage | Light/light (incl. Mighty-light F3 gap), light/heavy, light/polearm, M3 preempt, balanced-vs-Fast |
| Findings | M1 dominant; M2/M3 secondary. Dominance redistributed not eliminated: light-vs-light 94% Fast; light-vs-heavy 22% Fast (inverted). Polearm vs Fast 56/44 cleanest. F3 gap mostly persists. Balanced non-viable. |
| Provisional assumptions | M2 counter magnitudes empirical (−3D Decisive-v-Patience, degree-cap-1.0 Cautious-v-Pressure); M3 preempt heuristics (HP<0.6, init gap >= 2); STARTING_DISTANCE=2; closing-action 1-stam per band |
| Dependencies | Phase 10 baseline (params/combat.md ED-694 stamina; STR-strong bonus dice; 1/End Ob wound; Disarm) |
| Status | Implemented + run. Reframing 2 verdict deferred pending Phase 12 mass-battle archetype test. |
| Open | Tune M1 softer vs accept Reframing 2 vs add C2 hybrid — decision after Phase 12. |


## Phase 12 (2026-05-17) — Mass-battle archetype test (Reframing 2 verification)

| Field | Value |
|---|---|
| Scope | Mass-battle scale. Test whether Heavy/Strong archetypes dominate at mass scale at comparable or greater magnitude to scene-scale Agi dominance. Cross-scale balance check for Reframing 2. |
| Sim | tests/sim/scripts/phase12_mass_archetype_v0.py |
| Writeup | tests/sim/phase12_mass_archetype_v0_2026-05-17.md |
| Trials | N=2000 per matchup; Levy vs Levy calibration 46.7%/48.5% cond |
| Coverage | Light/Heavy archetype matchups; weapon-class penetration; Power-tier diffs; HeavyBlunt anti-armor |
| Findings | Mass-battle dominance is CATEGORICAL (100/0) when weapon-class fails to penetrate armor-class, not statistical. Light vs Heavy: 0/100. Heavy vs Heavy: 100% draw (canonical stalemate without tactical levers). HeavyBlunt (Knights Templar): 100/0 vs everything — anti-armor universal. Reframing 2 supported with asymmetric magnitudes. |
| Provisional assumptions | Default pool split ½/½; H baseline +2 per worked example; max_rounds=40; draw threshold ratio 1.2x; tactic cards / flanking / Command / terrain UNMODELED |
| Dependencies | params/mass_combat.md Core Formula PP-233; DR Table PP-104; Weapon Effectiveness table |
| Status | Implemented + run. Reframing 2 ratified. Two audit flags surfaced: HeavyBlunt universal anti-armor; Heavy-vs-Heavy stalemate needs tactical levers to produce interesting resolution. |
| Open | Verify Heavy-vs-Heavy resolves interestingly via tactic cards / flanking / Command in M3-engine sim (deferred). HeavyBlunt audit deferred. |

## Phase 7 (2026-05-18) — v18 mass-battle bare port (Mode G manifest)

| Field | Value |
|---|---|
| Scope | Infrastructure: Mode G module manifest for Phase 7 mass-battle port. Scope C2 narrow — canon §4.1 Step 1 + §4.10 sub-step 3. Steps 2–9 deferred. |
| Sim | tests/sim/v18-integration/module_manifest.md (this commit); subsequent port commits land in sim/provincial/{massbattle,units,tactic_cards,faction_action}.py + sim/mc_v18.py |
| Writeup | This manifest + designs/provincial/mass_battle_integration_v30.md §4 |
| Trials | None — manifest only. Battery (tests/sim/battery_v22.py) deferred to Step 5 of canon §4.1, not in C2. |
| Coverage | Phase 7 modules declared; tactic_cards.py stub remains BLOCKED on contamination audit per integration_plan_v18 §1.4. |
| Findings | Source-engine is sim_mb_06_v22.py (per canon §4.1), not m3_mass_battle.py. v22 dataclass extraction needs late-binding to avoid circular import (units.py ↔ massbattle.py constants). |
| Provisional assumptions | Bare-port flex acceptable per canon §4.1 PROVISIONAL clause (signatures may shift if statistical equivalence holds on Mirror Cmd 4v4 p>0.05). |
| Dependencies | designs/provincial/mass_battle_v30.md; designs/provincial/mass_battle_integration_v30.md; designs/provincial/military_layer_v30.md; designs/scene/derived_stats_v30.md; params/mass_combat.md; params/core.md. |
| Status | Manifest committed. Port commit follows. |
| Open | Verification ledger (per sim_gate) deferred — bare-port replicates v22 constants verbatim. Phase 8 strategic AI successor. |

## Phase 7 C2 (2026-05-18) — regression fix: Subunit.__eq__ recursion

| Field | Value |
|---|---|
| Scope | Surgical regression fix for c6ecb5b9 (Phase 7 C2 bare port). RecursionError in Subunit.__eq__ via target_atom cycle after assign_targets blocked every Conquest battle silently (mc_v18.faction_take_action's try/except Exception:pass masked the raise). |
| Sim | mc_v18.run_batch(10, base_seed=42) — direct invocation smoke against resolve_mass_battle(Crown Mil=5, Church Mil=4.5). |
| Writeup | tests/sim/v18-integration/module_manifest.md (status updates) + commit body. |
| Trials | 10 batch runs (n=10). Pre-fix: battles_mean=0 (silent fail). Post-fix: battles_mean=30.0. Direct invocation returns degree dict {'attacker_wins': True, 'degree': 'Success', 'attacker_size_pct': 0.89, 'defender_size_pct': 0.775}. |
| Coverage | sim/provincial/units.py: @dataclass(eq=False) on Subunit + Unit. Falls back to object identity __eq__/__hash__. Zero call-site changes. |
| Findings | Cycle source: assign_targets (massbattle.py L619/622/627/630) sets atom.target_atom as direct Subunit reference on both sides; A.target_atom→B and B.target_atom→A form a cycle. Literal trigger: list.remove of tuple-of-Unit at massbattle.py L1488/1494/1511/1537 (pursuit/rout tracking). Audited: zero `subunit == subunit` value-equality sites; existing set/dict keys already use id() (L749-750). |
| Provisional assumptions | Identity-eq does not change observable mass-battle outcomes — basis: canon §4.1 PROVISIONAL flex clause; target_atom set-by-reference throughout the engine, never compared by value. win_share spread Crown 40 / Varfell 50 / Church 10 (no pathological degenerate state) confirms _faction_to_unit MV-defaults are tolerable for C2; GAP-1 not escalated. |
| Dependencies | designs/provincial/mass_battle_integration_v30.md §4.1 PROVISIONAL clause; canon/02_canon_constraints.md §B GD-1. |
| Status | Verified end-to-end. Conquest path unblocked. |
| Open | Phase 7 follow-on splits into separate handoffs (Step 4.2 LETHALITY; Steps 4.3-4.6 flanking/ripple/tiebreakers; Steps 4.7-4.9 phase hooks/collision/cleanup; Step 10.1 domain_echo; Step 10.2 accounting + faction→unit richening — resolves GAP-1). |

## Phase 7 Step 4.2 (2026-05-18) — LETHALITY restoration + PP-233 formula correction

| Field | Value |
|---|---|
| Scope | Step 4.2 of canon §4.2 (designs/provincial/mass_battle_integration_v30.md §3.1, Audit Issue 1 highest severity). Restore LETHALITY_SCALE per §3.1 PROVISIONAL clause; calibration sweep at T3 mirror per §3.1 spec; commit calibrated value. Patch surface: 3 HP-damage sites in sim/provincial/massbattle.py (engagement, pursuit_damage, freed_attacker_damage). |
| Sim | mc_v18.run_batch(10, base_seed=42) smoke + multi-turn calibration sweep at L = [0.02, ..., 10.0] across N=40-60 mirror T3 Line vs Line runs. |
| Writeup | sim_verification_ledger.json (new); module_manifest.md (status updates); commit body (full diagnosis). |
| Trials | Sweep N=40-60 per LETHALITY value; robustness check N=40 across 5 seed batches (1000-5000); asymmetric matchup spot-check N=20 each. |
| Coverage | sim/provincial/massbattle.py — (1) PP-233 continuous net_successes formula replaces discrete DAMAGE_BY_DEGREE buckets at engagement L915-922 + freed_attacker L1475-1481. Pursuit already used PP-233 form; only LETHALITY wrap added. (2) LETHALITY_SCALE = 1.25 declared at L122. (3) DAMAGE_BY_DEGREE dict retained as narrative degree label for downstream logging. DR-as-reduction subtractor preserved (HP/H/DR architecture rationalization deferred). |
| Findings | **Root cause diagnosis deeper than §3.1**: §3.1 attributed lethality collapse to 20× HP inflation from v19 BLOCK_SIZE change. True diagnosis is TWO compounding defects: (a) HP inflation (per §3.1); (b) discrete DAMAGE_BY_DEGREE buckets cap damage at (1+power) regardless of net_successes, violating PP-233 canon "Damage dealt = successes × (1+Power)". PP-233 worked example: 4 successes × 4 = 16 damage; bucket model yields max 4. Bucket cap dominates (4× loss at typical net). Required formula rewrite, not just multiplier restoration. Spec §3.1 PROVISIONAL range 0.05-0.20 was a v17-era assumption; with PP-233 correction, LETHALITY=1.25 fine-tunes near baseline rather than gross compensation. |
| Calibration | Target: 14-16% per-turn casualties at T3 mirror Line vs Line P4/C4/D5/M6. Calibrated LETHALITY_SCALE=1.25: mean 14.48% / median 16.45% per-turn at N=60; battle-turns mean 1.9; winners 26A/32B/2draw (balanced). Robustness across 5 seed batches: 14.25-16.03% — all in band. Asymmetric matchups behave correctly (Power advantage → win share; Discipline edge → casualty asymmetry). mc_v18 smoke: battles_mean=40.1 (was 30.0 pre-Step-4.2). |
| Provisional assumptions | DR retained as damage-reduction subtractor — PP-233 originally folded DR into H (Health per Size = min(Disc,Cmd) + DR), but v22 HP model uses Size×BLOCK_SIZE and drops H entirely. Keeping DR-as-reduction preserves DR's defensive role; HP/H/DR architecture rationalization deferred to separate audit. |
| Dependencies | designs/provincial/mass_battle_integration_v30.md §3.1; params/mass_combat.md PP-233 Core Formula. |
| Status | Landed. Calibration in band. |
| Open | (1) Church win-share dropped 10% → 0% at L=1.25 vs b0185f05 baseline (n=10 too small, re-test in Step 4.2b). (2) T2 outperforms T3 at equal stats in spot-check — likely morale-erosion pathology (bigger units accumulate damage→morale faster); not introduced by Step 4.2, flagged for separate audit. (3) tests/sim/battery_v22.py existence unverified; battery validation gate (§3.2) deferred to Step 4.2b. (4) sim_verification_ledger.json created for v18-integration; future sim_gate calls must use this ledger. |

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

