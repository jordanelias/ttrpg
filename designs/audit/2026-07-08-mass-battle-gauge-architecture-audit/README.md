# Mass-Battle Gauge — Why 7/20, and What To Do About It
## Final combined engineering audit (third-level synthesis of two Workflow waves, 11 surfaces)

**Prepared for Jordan. Repo:** `jordanelias/ttrpg`, `tests/sim/mass_battle/` + `tests/sim/gauge_mb.py`. **Live defaults:** `PER_CELL=1`, `POOL_QUALITY_MODEL=1` (ED-MB-0006), `seed_base=1,000,000`, `n=60`, multi mode. **Lane:** MB / RC-5. **Provenance:** Wave 1 (7 surfaces: combat-pool granularity, degree/damage-tier discretization, morale/rout cascade, deployment/geometry/ANCHOR_MAP, envelopment/composed-army, the gauge harness, granular-architecture proposal) + Wave 2 (4 surfaces: movement/pathing/routes, stances/tactics/orders/roles, reach/targeting, ranged/volley). Each surface ran producer → isolated adversarial critic (relay, read-only critic) → per-wave opus-4.8-max synthesis; ~24 subagents, ~1288 tool calls, ~4.5M subagent tokens. **Every claim below survived independent adversarial re-verification; where a wave's own critic corrected it, I resolve to the corrected number and say so.**

**Method note:** every stage of this investigation — both wave syntheses and this final combination — ran at Opus 4.8 with `effort: max`, per Jordan's explicit request. The final combination agent independently re-read `handoffs/HANDOFF_MB.md`, the git log, and `canon/editorial_ledger.jsonl` to ground its reconciliation, and caught that an earlier draft's DG renumbering collided with the already-ratified DG-1..DG-5 namespace from this session's own ED-MB-0002/0003/0005 rulings — corrected here to a clean DG-6..DG-16 sequence. Full per-surface producer findings and critic verdicts, plus both waves' complete synthesis text, are preserved alongside this README (`01_wave1_synthesis.md`, `02_wave2_synthesis.md`).

---

## 0. Bottom line up front

**7/20 is not one bug. It is roughly five distinct engine mechanisms, plus two rows of pure sampling noise, plus two rows that are harness-construction failures.** Any writeup that names a single villain is wrong; the failing rows partition cleanly by mechanism, and the mechanisms live at different layers (geometry, resolution architecture, movement, rout timing, and the measuring instrument itself).

Two mechanisms dominate everything else in confidence, because they were **causally proven by reversal ablations that two independent critics reproduced from scratch** — not merely correlated:

1. **A cell-count/density plumbing defect** (two unreconciled geometry generators → a static, never-recomputed `unit.ncells` → the Lanchester density term). Patching the density term to be representation-invariant, holding everything else fixed, **flips H3 from 100%/0% to 0%/100%, and H10 the other way.** This single-handedly decides the composed-army infantry rows.
2. **A super-linear resolution architecture** (melee exponent **p≈3.2** under the live `PER_CELL=1` path vs the Lanchester Linear-Law target **≤1.4**) that concentrates *any* residual edge toward a near-deterministic snap. This is why even a density-corrected H3 does not land in its 55–72% band — it flips to the *other* side's win-out.

**These two are multiplicative, not competing:** the density defect is the bias-generator for composed rows; the amplifier concentrates whatever bias it is fed. Removing *either* de-snaps a composed row (which is why the reversal ablations work), but **no single fix lands any row inside its band.** This investigation is therefore **diagnostic, not yet curative** — a point I refuse to soften (see §8).

**The framing correction that matters most for the granularity directive:** the word "granularity" bundles two axes with *opposite* relevance to this gauge. The per-cell **quality** half (veteran-front/levy-rear, `cell_power` dicts) is *provably inert* for all 20 current rows — a legitimate future-fidelity capability, but it cannot move the score. The **cell-count / density** half is exactly where the #1 defect lives. The instinct that "everything should be grounded by the number of troops per cell and the number of cells" points straight at the top root cause — just not at the axis the architecture-proposal draft was writing. And two named pieces of the directive — **troop-grounded speed, and the entire ranged/volley pool** — were left behind by ED-MB-0006's melee work and are still ungrounded (§5).

**The single most decision-relevant NEW result of this session** (Wave 2's own empirical probe, verified here): the "obvious" cheap fixes for the two ranged rows are **mutually incompatible** until a third, previously-latent movement bug is fixed. See §2 — it changes the safe-fix list.

And the caution that reframes remediation: **the engine snaps everything to near-total, but the gauge *wants* the cavalry-shock rows (C4/C5/C7) near-total and the infantry rows modest.** There is one global snappiness serving two masters. So the fix is not "de-snap globally" (that breaks the passing cavalry rows) — it is "make the outcome scale with the *size* of the edge," which is what a melee exponent ≤1.4 buys. That exponent is the north star and the hardest, least-tractable finding here.

---

## 1. The failing rows, and an honest count

Passing (7): **H1** (mirror), **C1**, **C2**, **C4**, **C5**, **C6**, **C7**. Failing (13): **H2–H11** (ten rows), **R1**, **R3**, **C3**.

The raw "13 failures" over-counts real engine divergence. Peeling back the instrument:

- **13 nominal failures**
- **→ ~11 real engine divergences** once **C3** and **H9** are recognized as n=60 sampling noise (§3, harness bucket).
- **→ ~9 genuinely-deep engine divergences** once **R1** (a one-parameter harness bug — the "ranged" side is built as infantry) and **R3** (a deployment/stance construction failure) are also set aside as harness-flavored. The nine deep rows are **H2, H3, H4, H5, H6, H7, H8, H10, H11.**

Wave 1 stated "~11"; Wave 2's reclassification of R1 as a harness artifact lets us go one layer further to ~9. All three numbers are carried because each is true at a different definition of "failure," and the lower two are the honest denominator for "how badly is the *engine* miscalibrated."

Full attribution table (result vs band; primary mechanism; bucket). Mechanism codes are defined in §2–§3.

| Row | Result vs band | Primary mechanism(s) | Bucket(s) |
|---|---|---|---|
| **H2** | 100 vs 48–62 | **E2** Arrowhead side-asymmetry (untraced) + **D1** amplifier | engine (open) + tradeoff |
| **H3** | 100 vs 55–72 | **E1** density (reversal-proven) + **D1** amplifier | engine + tradeoff |
| **H4** | 1.7 vs 45–62 | composition (⅓ center) + RC-5 slot asymmetry + **E4** cascade; ED-MB-0006 trigger; **not** sibling-pull | engine + tradeoff |
| **H5** | 98.2 vs 48–62 | **E1** density + **E4** cascade (fires 55/60 seeds) | engine |
| **H6** | 11.9 vs 48–60 | refused-flank hold/release (half the army sits out) + **D1**; density ruled **OUT** (direction wrong) | engine + tradeoff |
| **H7** | 88.3 vs 48–62 | **D1** amplifier on a real GappedLine edge | tradeoff |
| **H8** | 33.9 vs 50–65 | **D1** + GappedLine/Arrowhead shape interaction (untraced) | tradeoff + open |
| **H9** | 57.1 vs 38–52 | **H-noise** (n=60) + **E2** Arrowhead-as-B weakness | harness + engine |
| **H10** | 0 vs 28–45 | **E1** density (reversal-proven) | engine |
| **H11** | 0 vs 38–55 | **E1** density + RC-5 slot asymmetry | engine |
| **R1** | 66.1 vs 0–30 | **H-R1** built `troop_type='infantry'` (the flipper) + **E6** volley collision (contributor) | harness + engine |
| **R3** | 100% draw vs 42–58 | **H-R3** hold + out-of-range deployment; clean fix **gated on E5** (see §2) | harness (engine-gated) |
| **C3** | 60 vs 42–58 | **H-noise** (mirror; flips across seed_bases) | harness |

The three near-total cavalry rows that pass — **C4, C7** (composed) and **C5** (plain Arrowhead) — are flagged **[CALIBRATED-DEBT]**: they may be passing *partly on the same artifacts* being removed elsewhere. C4/C7 via **E1** density inflation + **D1** amplifier; C5 via **D1**/the **E2** Arrowhead-side-A advantage (C5 is *not* a composed-army row — see the E1 correction in §3). Fixing E1 or D1 in isolation could knock any of them out of band. **The pass count is not monotonic in the number of fixes applied** (§8).

---

## 2. The one new empirical result — the R1 and R3 fixes collide (Wave 2 probe, verified)

This is the finding to not lose. None of the four movement/ranged surfaces ran the combination a *fully corrected* R1/R3 would use — each tested its own fix in isolation:

- The R3 "kite fix" was validated with **default** stats (discipline 5).
- The R1 "archers fix" uses discipline 3 but with **`hold`** (so the unit never needs to move).
- The node-path speed floor was verified in isolation but never connected to the kite fix.

Wave 2 ran the missing combination (`tests/sim/mass_battle`, live defaults, n=10/variant):

```
node-path step (cells/tick) for a Line body:
    disc=5 balanced   -> step=1     disc=3 balanced   -> step=0
    disc=5 aggressive -> step=2     disc=3 aggressive -> step=1
    disc=5 retreat    -> step=1     disc=3 retreat    -> step=0

R3 variants (n=10):
  (A) hold + default stats            A=0  B=0  draw=10   (frozen — reproduces R3 failure)
  (B) kite + DEFAULT stats (disc=5)   A=8  B=2  draw=0    (resolves — reproduces critic's fix)
  (C) kite + CORRECT archers (disc=3) A=0  B=0  draw=10   (RE-FROZEN)
```

**Mechanism** (confirmed at `hierarchy/units.py:836`): `step = max(0, floor(base × disc_mult) + stance_mod)`. For a Line (`base=1`), discipline 3 (`disc_mult=0.7`), balanced (`stance_mod=0`): `floor(0.7) = 0`. Live `_node_advance` has **no fractional-velocity accumulator** — that carry (`_speed_accum`) exists only in the dead legacy path (`units.py:1109-1111`). So a *correctly-statted* archer (disc 3) under `balanced` computes step 0 and **can never close from spawn to firing range.** `kite` cannot help a unit that physically cannot move.

**Consequence:** "fix R1 by making it archers" and "fix R3 with kite" cannot both be done *with historically-correct stats* until the node-path speed floor (**E5**) is fixed. This promotes a bug all four producers rated "latent / currently invisible" into a **fix-blocking prerequisite** — and it directly overrides an earlier read that had listed a "ranged `hold` variant" among its *safe* fixes. R3's fix is **not** safe-to-ship; it is gated on **DG-10** (§7b). This is exactly the class of "looked safe in isolation, now known blocked" item flagged in §7a.

---

## 3. Ranked root causes and full bucket table

### Tier 1 — Dominant, causally proven

**E1 — Footprint/`ncells` Lanchester-density artifact** — *engine defect; dominant for 5 rows; reversal-proven.* `geometry.py` has two unreconciled cell-count generators. The legacy tier-table (`CELL_PATTERN_FN`, used by every plain single-shape unit) always yields ~25 cells for a T3 body regardless of troop count. The continuous `footprint_for` (used *only* by composed `_envelop_army`/`_refused_army`) derives cell count from troops/density, but its coarse `LINE_ASPECT` stepping (`geometry.py:77-104`, `config.py:25-29`) collapses a 133–200-troop subunit to **1 cell**. A 400-troop composed army becomes 2–3 fat cells (density ~133) against an equal-troop single-shape opponent's 25 cells (density ~16) — an **~8× density ratio**. That feeds `core/attrition.py`'s `_lanchester_strength` via `tpc = unit.hp / unit.ncells` — where `ncells` is a *static* sum computed once in `Unit.__post_init__` (`units.py:1555`) and **never recomputed** — and `orchestration.py:963-971` applies it as a direct casualty multiplier. **Causal proof:** patching `_lanchester_strength` to a representation-invariant density, everything else fixed, reversed **H3 100%→0%** and **H10 0%→100%** (n=20); H3 with `PER_CELL=0` (envelopment-sigma/charge-shock/fatigue all off) *still* resolved 100%/0%, so **this defect alone is sufficient** — the envelopment machinery is not even necessary. **Second amplification channel** (same collapse): a 1-cell subunit commits its *entire* base pool to a single contact via `core/exchange.py`'s `pair_pool_contribution` (`weighted_troops == cur_troops` by construction), vs a 25-cell formation committing only front rank + depth-weighted support. The collapse hurts twice. **Correlation with pass/fail:** the passing cavalry rows (C4, C7) are exactly the ones where the majority center (266 troops, pin_frac 2/3) escapes full collapse to 6 cells while only minority wings collapse; every failing composed row uses symmetric splits collapsing *every* subunit. **This updates ED-MB-0004's working theory** ("envelopment/charge-shock morale collapse dominates") — that theory is at best incomplete under the live defaults. **Corrections:** H6 is the exception — refused-flank *loses* (11.9%) despite the *higher* inflated density, so the direction is wrong for E1; H6 is driven by its refused wing sitting out via `hold` until release, not by density (correctly ruled out). And **C5 is not an `_envelop_army` row** — it uses a plain `'Arrowhead'` via the legacy path (`gauge_mb.py:263`), so E1 does not touch it (an earlier pass wrongly listed it here).

**D1 — Super-linear resolution architecture / resolve-to-absorption amplifier** — *design tradeoff (→ DG-6); broadest reach; deepest and hardest.* A battle resolves ~100–175 independent stochastic per-pair contests to a fixed ~30% cumulative-loss rout threshold (H2: **115–175 events over 7–11 turns**, reproduced digit-for-digit). By gambler's-ruin/CLT concentration, *any* persistent per-tick bias concentrates toward certainty as rounds-to-absorption grow (concentration toy, critic-reproduced: **5% edge → 85% win, 10% → 98%, 15% → 100%**; threshold sweep at fixed 10% edge monotone **76%→99%**). It **survives stripping degree-tiering entirely** (pure linear damage was *more* extreme), so it is architecture-general, **not** a `compute_degree` artifact. Measured as a conserved-quantity exponent, melee sits at **p≈3.2 under the live `PER_CELL=1` path** (critic's independent wide-grid fit **p≈3.15**), far above the Linear-Law target **≤1.4**. **Exponent reconciliation (a genuine deepening of ED-MB-0006):** ED-MB-0006 disclosed **p≈2.50** (new model), **p≈1.55** (old-model baseline), and a scale-sweep plateau **p≈1.65–1.7** (including a sqrt-numbers variant and an 8-point sweep), confirming it is **not** a Lanchester double-count (disabling `LANCHESTER_ENABLED` doesn't move it). But those figures were measured by `lanchester_signature.py`, which hardcodes `PER_CELL=0` via `setdefault` at **line 24** — the *wrong* path. Under the actual live gauge path the exponent is **worse (≈3.2)** than the ≈2.50 on record. ED-MB-0006 also tentatively attributed the amplification to `compute_degree`'s discrete tiering going near-deterministic; **this investigation corrects that** — the concentration is architecture-general (survives with tiering removed), so degree-tiering is a *rider*, not the driver. **Necessary but not sufficient:** removing E1 from H3 doesn't land it in-band; it flips to a B win-out because D1 still snaps the residual edge. Its honest gap: H2's *actual* per-pair pool ratio runs **~1.33× (4 vs 3 dice)** — not obviously "modest," so the "modest historical edge → unfair snap" story overstates how innocent the incoming edge is. **Acceptance test for any amplifier fix:** `check_law_exponents()` passing at **p≤1.4 under `PER_CELL=1`** — noting constant/scale tuning *provably* can't get there (plateau 1.65–1.7), so a *structural* change is required. This is precisely ED-MB-0006's own recorded "next action."

### Tier 2 — Confirmed engine defects, contained (but one is the biggest open lead)

- **E2 — Side-dependent Arrowhead asymmetry** — *engine defect; root cause UNTRACED; dominant for H2; the single biggest open lead.* The same Arrowhead-vs-Line matchup gives **100/0/0 in ~8.9 turns with Arrowhead on side A**, but **43/43/13 (near-coinflip) in ~15.8 turns with Arrowhead on side B** (reproduced to the decimal). A GappedLine control (dominant on *both* sides) rules out a generic side bias, so this is specific to Arrowhead. Four static-geometry candidates were ruled out by code reading, narrowing the cause to the **dynamic movement/momentum/charge-shock path** — but **nobody found the offending line.** It is a dominant cause of the worst plain-row overshoot (H2) and silently contaminates confidence in *every* cavalry row (Arrowhead sits on side A in all of C1–C7). **Distinct from the already-disclosed ANCHOR_MAP column drift** (ED-MB-0004, per-shape deployment column Line=9/Arrowhead=8/GappedLine=7) — that drift is minor and known; this is a separate, larger, untraced thing.
- **E4 — `recalc_size` aggregate-floor force-rout cascade** — *engine defect; the H4/H5 finisher.* `Unit.recalc_size()` (`units.py:1603-1611`) marks **every** subunit routed the instant the *whole-unit aggregate* floors to `size==0`, with **no `len(subunits)==1` guard** — unlike `cohesion`/`eff_size` in the same class, and in direct contradiction of the `Subunit` dataclass's own stated principle (`units.py:294-299`: "a heavily-hit subunit can break while a fresh sibling holds — Cannae/Hastings"). Empirically confirmed (upgraded from structural-only): fires in **55/60 H5 seeds** (two siblings holding 44–56 troops each force-routed) and **15/60 H4 seeds** (both wings holding ~49–51 healthy troops force-routed alongside the dead center), terminating via `orchestration.py:1251`'s `if unit_a.routed or unit_b.routed: break`.
- **E5 — Node-path speed floor** — *engine defect; the fix-blocker (§2).* `_node_advance` lacks the fractional-velocity accumulator that exists only in the dead legacy path (`units.py:1109-1111`), so any disc∈[3,5) unit floors to step 0 under `balanced`/`retreat` (`units.py:836`). Latent for the current gauge, **but blocks the correct fix for R1+R3** and for any graded speed (DG-11).
- **E3 — `hold`-stance mutual non-engagement** — *engine defect (semantics), bucket-adjacent to harness; fully explains R3, partly R1.* Both R3 sides deploy 19 rows apart (`SIDE_A_START_ROW=34`, `SIDE_B_START_ROW=15`) while `VOLLEY_MAX_RANGE=8`, and `hold` is an unconditional no-advance early-return (`units.py:826`/`engine.py:307`, `STANCE_SPEED_MOD['hold']=-99`). With both holding they never close — **`a_cas=b_cas=0.0` exactly, guaranteed 20-turn draw.** `hold` conflates "don't close to melee" (correct for a braced line) with "never move even to enter firing range" (wrong for a ranged unit). The *row failure* is harness-construction (pitting two immobile out-of-range lines); the *semantics conflation* is an engine defect and a ruling (DG-14).
- **E6 — Volley/melee standoff-floor collision** — *engine defect; R1 contributor, not the flipper.* `VOLLEY_MIN_RANGE=2` equals the melee standoff `2.0`, so a ranged unit locked in melee fires a full **unreciprocated** volley every tick. Critic found it **~3× worse than the producer stated: 15–36% of max HP, not 5–12%.** It inflates R1 but does not flip it (archers still lose 0/40 with it live).
- **E7 — Frozen momentum / non-decaying `charge_pen`** — *engine defect; cavalry rows; magnitude UNQUANTIFIED.* `cell_last_speed` freezes at the nominal step and never decays; a flat `charge_pen=3` is applied every tick rather than as a one-shot impulse (constant 2.0/1.0 momentum reproduced). Contributes to C1–C7; nobody quantified its effect on the specific percentages.

### Tier 3 — Secondary / latent engine defects (confirmed, not load-bearing on the score)

- **E8 — `Unit._agg` static-weight staleness** (`units.py:1570-1573`): aggregates weight by static `troop_count`, not live `cur_troops`, while `agg_morale()<=0` is a live rout trigger. Real, cheap — **but the directional story is possibly backwards** (over-weighting a decimated, lower-morale subunit may bias toward *earlier* rout). Fix the code; make **no** causal claim about which row it moves.
- **E9 — Dead morale constants:** `MORALE_EROSION_DAMP`, `ROUT_FLOOR_LOSS_PCT`, `SUBUNIT_ROUT_FLOOR` are defined/exported/provenance-tracked but **never consumed**; `MORALE_PHASE_CAP` is shadowed by a hardcoded `3.0` (`core/state.py:60`). These are exactly the levers that would soften the collapse if wired. (`ROUT_EXHAUSTION_MORALE_HIT` also has a name/formula mismatch.)
- **E10 — `build_army` silent key-drop** (`engine.py:243-246`): unrecognized spec-dict keys (e.g. a typo `'stamnia'`) are silently ignored. Latent footgun; no live row affected.

### Tier 4 — Harness artifacts (the engine is more correct than 7/20 suggests)

- **H-noise — n=60 with no confidence intervals → C3 and H9 are noise, not fails.** decA has SE ≈ 6–7pp at n=60. **C3** (60.0 vs band 42–58) sits **0.32 SE** from the edge and passes in **3 of 4** alternate seed_bases (60.0/56.7/51.7/48.3). **H9** (57.1 vs 38–52) sits **0.72 SE** out and passes in **2 of 4** (57.1/53.7/48.0/45.1). Under a CI-reporting harness both read UNDECIDED, not FAIL.
- **H-R1 — R1 built `troop_type='infantry'`, not `'archers'`** (`gauge_mb.py`, `make_unit` at :82-114): `build_unit` constructs `Subunit` directly, bypassing the only `TROOP_TYPE_STATS`-reading constructor, so the "ranged" side inherits full infantry stats (4/5/6) instead of archers' (3/3/3). Setting `troop_type='archers'` flips R1 **66.1% → 0%** (inside band) — the true row-flipper (the volley collision E6 alone leaves R1 near 50%).
- **H-R3 — R3 hold + out-of-range deployment → literal zero-engagement** (see E3). Harness row failure; clean fix gated on E5/DG-10.
- **H-lanchester — `lanchester_signature.py` false-positive PASS:** the same `hold`-non-engagement makes `check_square` a degenerate zero-division PASS (hp constant for all ticks, `Aᵖ−Bᵖ` trivially conserved, "PASS ratio=inf" is the code's own fallback). Combined with the `PER_CELL=0` hardcode (line 24), the square-law signature has apparently **never been genuinely measured.**
- **H-mixed — `make_mixed_unit` is dead code** w.r.t. the battery → **zero gauge coverage of the granularity directive**; nothing could detect a regression in that machinery.
- **H-dup — C2 and C6 are the same scenario constructed twice** (a minor harness-quality wrinkle surfaced by the reach surface).
- **H-cap — H4's 33% draw rate is a turn-cap artifact:** extending the cap 20→40 collapses draws **30%→5%** while **decA stays flat at 0.0** — so the "attacker loses" verdict is real engine behavior, not truncation (see §4).

### Tier 5 — Already-disclosed residuals (now confirmed / deepened / demoted / mislabeled)

- **`attrition.py` static `ncells` / whole-unit density:** promoted from "flagged residual" to **proven-decisive by reversal ablation** (this is E1). The biggest deepening.
- **Lanchester exponent >1.4:** confirmed and **worse than disclosed** — p≈3.2 live vs the ≈2.50/1.55/1.65–1.7 on record (measurement-path bug; this is D1).
- **`compute_degree` adaptive-Ob convexity:** investigated and **demoted** to secondary/pool-size-dependent (small at 3–4 dice; 2–6× at pools of 16–100). Rides on D1; doesn't drive it. The long-open "is the relative-Ob construction what turns a modest edge into a snap?" is now answered: **mostly no.**
- **RC-5 / ANCHOR_MAP slot asymmetry:** confirmed and split into three parts — (a) the **H4/H11 slot flip** (large, live; §4), (b) the front-anchor-depth convention (real but currently inert — no shallower shape on side B), (c) the **1-cell ANCHOR_MAP column drift** (minor, already disclosed ED-MB-0004). Note the "two racing clocks" theory stays **closed/refuted** — no maneuver-timing race exists.
- **Partition-invariance / convergence-scale (ED-MB-0004):** already landed; a real defect closed, but **never the dominant lever** for these rows (bit-for-bit identical win/loss/draw split post-fix) — consistent with E1 being the actual driver.
- **Also cite, don't re-litigate** (Wave-2 already-disclosed set): reach-table emptiness, `resolve_cross_side_contention` no-op (no live speed-priority successor), the unbuilt path-length budget, legacy/node divergence, legacy maneuver code being unreachable.
- **Mislabel corrections (Wave-2 critics):** two items producers filed as "already-disclosed" are actually **new** — the Order-substrate 2-of-4-trigger-kinds coverage gap, and the `ROLE_SPEC` caller-gating observation; and the `config.py`/`orchestration.py` comments calling `ROLE_SPEC`/`TROOP_TYPE_ROLES` **"INERT" are stale/wrong** (Stage D wired the construction-time gate — correcting these is a safe editorial fix, §7a).

### Tier 6 — Demoted / refuted (do not resume as live theories)

- **Morale/rout as an independent amplifier — REFUTED** by its own critic: with `rout_resolution` monkeypatched to a no-op, H2 *still* resolves A=100/B=0 with the loser taking ~70% casualties before dying. Morale/rout is a **downstream finisher on an already-decided casualty trajectory**, not a driver. (The mechanistic findings are solid; the "dominant-cause" severity tags were wrong.)
- **`MORALE_SIBLING_PULL` as the H4 cause — REFUTED:** ablation (0.15 vs 0.0) gives virtually identical H4 (0% decA both ways). The contagion is real and measurable (undamaged wings drop **6.00→4.33**) but is *not* what loses H4.
- **Post-rout pursuit — non-factor:** architecturally unreachable for all 20 rows (only wired into `run_multi_unit_battle`, which the gauge never calls).
- **The granularity "orthogonality" toy (FEEDBACK-vs-FROZEN ~1pp) — REFUTED** by its critic (13–15pp, sign-flipping on a floor-vs-round choice). The *structural* orthogonality argument stands on its own logic (see §5); don't cite the toy numbers.
- **Movement surface's envelop "commitment never fires" — REFUTED:** it fires; the stall is one phase later (post-commitment).
- **Stances surface's R1 aggressive-stance figures (18/30→9/30) — do not reproduce** (~9–10/30 both ways, flat); only the qualitative "aggressive doesn't fix R1" survives.
- **Count-level magnitudes — do not cite:** the architecture surface's "~20 troop_type / ~46 eff_* sites" were ~30% inflated (critic: 15 / 37); the movement surface's volley-damage magnitude skipped a ×3 factor (bug is *larger*). Qualitative claims hold.

---

## 4. The H4 "Cannae" anomaly — its own section (per instruction)

H4 is the one failure that does *not* fit "the edge-holder wins out": the historically-favored envelopment **attacker loses badly** — **1.7% win / 65% loss / 33% draw** (ED-MB-0006's own n=60 gauge run; the earlier wave-1 re-synthesis logged the win rate as **2.5%** — a small-sample seed difference, both far below the 45–62% band). It is a distinct, compound failure mode:

1. **Proximate trigger — ED-MB-0006.** This is not an ancient mystery: the ledger shows H4 **flipped from attacker-WIN-OUT to attacker-LOSING at ED-MB-0006** (2026-07-08), when the combat pool abandoned Command for `POOL_QUALITY_MODEL` (`eff_power × eff_size × scale`). Making per-atom *numbers* load-bearing is what turned the composition problem lethal.
2. **Composition.** The symmetric-thirds force-parity split (DG-1, ratified) gives the pinning center only ⅓ of the troops (**133**) against a full-strength **400-troop Arrowhead** that *also* carries the wedge edge saturating H2 (E2). Under numbers-in-pool, the ⅓ center under-rolls and dies fast.
3. **Slot asymmetry (RC-5, distinct from E2's root cause).** H4 and H11 are the same matchup mirrored, yet the wing-release mechanic is **inert in H4's slot** (freeze-wings ablation is byte-identical — center annihilated before wings matter) and **decisive in H11's slot** (freeze-wings flips the distribution). Confirmed by matched-seed ablation. This refines, but does not reopen, DG-5 (which stays closed: no maneuver-timing *race* exists).
4. **`recalc_size` cascade (E4).** Once the center floors, the whole army is force-routed — including two healthy wings — ending the battle a B-win.
5. **Draw-rate is a separate cap artifact (H-cap).** The 33% draws all land at turn 20; cap 20→40 collapses them 30%→5%, but **decA stays flat at 0.0** — the loss is real engine behavior.

**H4's bottom line:** an emergent consequence of the DG-1 symmetric-thirds ruling *interacting with* the ED-MB-0006 pool change and the E4 termination bug — **not** morale contagion, and **not** a bug in the DG-1 ruling itself. Track it separately from the general edge-holder-win-out pattern. Whether guarding E4 (§7a) actually *rescues* H4 (vs merely stopping the cascade from *ending* the battle) is unconfirmed — the cascade is proven to *fire*; its causal contribution to the win rate is not yet measured (§7c).

---

## 5. The granularity directive — one unified verdict

The directive — *every subunit stat derives bottom-up from (troop type × density-per-cell × cell count)* — is **right, and roughly half-done.** Its whole value here is in un-bundling four axes with opposite relevance:

- **Cell-COUNT / density axis → directly necessary; it is the #1 root cause (E1).** The instinct that a subunit's power/health should be grounded by "the number of troops per cell and the number of cells" is *load-bearing*, because the dominant bug is precisely that cell count is derived two incompatible ways and the density flowing from it decides battles through a stale static field. This is the highest-leverage fix in the report. But the fix is **reconciling the two generators (DG-7)**, not adding per-cell quality fields.
- **Per-cell QUALITY axis** (the architecture-proposal draft: `cell_power`/`cell_discipline`/`cell_dr` dicts, veteran-front/levy-rear) **→ good for other reasons, but PROVABLY INERT for all 20 rows.** Three surfaces reached this independently: no gauge builder populates any per-cell override; the design is backward-compat-inert (empty dict → today's scalar, byte-exact); and D1 operates on the aggregate scalar bias regardless of internal decomposition (`eff_power × eff_size` is *exactly*, not approximately, the cell-sum form today, since every subunit is quality-homogeneous). It touches **none** of E1–E7. It is a legitimate future capability (hoplite/pike "best men in front," mixed-composition subunits) — pursue it on its own merits, scope it as its own lane-block, and **add a gauge row that actually exercises it** (via `make_mixed_unit`, currently dead) so the machinery is not untested. **Do not expect it to move the score.**
- **Speed grounding → STILL MISSING.** There is no `speed` in `TROOP_TYPE_STATS`; only a hardcoded binary `troop_type in ('cavalry','mounted_archers') → PC_CAVALRY_SPEED_MULT=2.0`. `Subunit` has no `speed` field; `Unit.speed` is a plain kwarg. This is the direct, nameable sibling of the melee grounding ED-MB-0006 already shipped — and it is **doubly blocked**: graded speeds are meaningless until the E5 node-path floor is fixed (a disc-3 unit floors to step 0 regardless of its multiplier). → **DG-11**, gated on **DG-10**.
- **Ranged/volley pool grounding → STILL MISSING.** ED-MB-0006's entire `POOL_QUALITY_MODEL` investment went into melee's `subunit_combat_pool` (`exchange.py:110`: `raw = eff_power × eff_size × scale + …`, numbers *inside* the dice pool); `fire()` was never touched. Volley's pool is `max(1, eff_power − _vpen)` (`orchestration.py:1154-1166`) — **`eff_size` is absent from the pool**; numbers enter only *after* the roll, as a linear `K_SQUARE × eff_size` multiplier. Confirmed by trace: a shrinking archer's melee pool visibly shrinks (5→4→3→2→1) while its volley pool stays essentially flat (4→3). So numbers scale melee's *roll* but only volley's *outcome magnitude*, post-hoc — the directive is half-applied. → **DG-13** (with a live catch: folding `eff_size` into the base pool *and* keeping the post-roll `K_SQUARE × eff_size` would double-count numbers).
- **Subunit-level dr / stamina → deferred (ED-1018), not type-derived.** Establishing base per-type dr/stamina/speed at the subunit level is a **prerequisite** before any per-cell override layer for them is meaningful. → **DG-11**.

**Net verdict on "will the granularity directive close the gap?"** The cell-count half is *necessary* (it is the dominant defect). The per-cell quality half will *not* move the score (future fidelity only). Finishing speed/dr/stamina/volley grounding is *correctness-completing but not by itself curative* — the D1 amplifier (DG-6) still gates whether any row can land in-band. The directive is pointing at the right layer; it is not a one-shot cure.

---

## 6. Is "strategy" (tactics / stances / roles / orders) real? — one unified verdict

**Troop type now grounds STATS; it does not yet ground BEHAVIOR. The tactical layer exists as architecture but is ~80% decorative in the surface the gauge exercises.** Corroborated across three surfaces and every critic who checked:

- **The role scaffold is genuinely wired but 0% exercised.** `TROOP_TYPE_ROLES` + `ROLE_SPEC` + `role_allowed` form a real construction-time gate (a `ValueError` on a troop-type/tactic mismatch, plus shape/instruction defaulting) — but it only fires when a caller passes `role=`, and **no builder in the 20-row battery does.** The apparent historical fitness (cavalry envelop, ranged hold) is the **test author's own discipline, not an engine-enforced constraint.** (The config/orchestration comments calling this "INERT" are stale — the gate *is* wired; correcting them is a safe fix.)
- **~11–12 of ~15 instruction strings are inert.** Two independent sweeps (`pursue/harass/loose/screen/advance/lure/shoot_move/reserve/pin/charge` vs nothing) produced **byte-identical** winner/turn sequences. Only `brace`, `envelop`, `sweep`, `kite`, `yield` gate real behavior. The two most name-suggestive tags — **`hold` and `volley` — do nothing as instructions**; their apparent effect comes from *separate* fields (`stance`, `unit_type`). So `role='VolleyLine'` yields `stance='balanced'` with an inert `('volley','hold')` tuple — it does *not* produce a static shooter.
- **The orders substrate is real but barely used.** `check_orders` implements 4 trigger kinds with working logic, but `Order()` is constructed in exactly **2 places**, using only **2 of the 4 kinds** (`tick:`, `enemy_range:`), never chained. Multi-step battle plans are entirely unvalidated surface area.
- **Stance:** 4 values exist; only `hold`/`balanced` are used. `retreat`/`aggressive` are behaviorally real but unexercised — and under troop-grounded discipline, `retreat` *also* floors to step 0 (E5 again), so it is not the clean "differs in direction only" story a producer claimed.

**Verdict:** a cavalry subunit and an infantry subunit given identical instructions today **fight with different dice but make identical maneuver decisions.** Strategy is real *scaffolding*, largely unexercised — the behavioral sibling of the stat-grounding gap, half-finished. → **DG-16**.

---

## 7. Recommended next actions

### (a) Safe to fix now — contained, ablation-toggle-able, byte-exact-preservable

Ordered by leverage. Each fits the repo's toggle discipline (new default-off env var where behavior changes; validate byte-exact via `bat.py`'s digest harness).

1. **Make the Lanchester density term invariant to the cell-count representation** (`core/attrition.py`) — highest leverage (E1). Also recompute `ncells` live (`units.py:1555`). **Acceptance:** the ncells-equalization reversal (H3 flips) no longer occurs. **Direction validated by reversal ablation; implementation is a design choice — see DG-7.** *Warning:* this will move C4/C7 and may drop them out of band — pair it with the amplifier work (DG-6), do not ship alone.
2. **R1: set `troop_type='archers'` on the ranged side** (`gauge_mb.py`, R1 row ~229-232). One parameter; empirically flips R1 66.1%→0%. Pure harness fix (H-R1). Feeds RC-5's R1 triage.
3. **Gate volley on true melee contact** (`d > standoff_from_reach(shooter, target)`, not merely `≥ VOLLEY_MIN_RANGE`) so a locked-in-melee archer stops firing — mirrors the existing "no volleying while yielding" precedent (E6). Genuine engine bug worth fixing regardless of R1; the exact new floor is a small magnitude (confirm under DG-13).
4. **Guard the `recalc_size` cascade** (`units.py:1603-1611`) with the `len(subunits)==1`/own-size guard that `cohesion`/`eff_size` already use, so only subunits whose *own* size floors get routed (E4). Toggle-gated. *(Whether this rescues H4/H5 is unconfirmed — see §7c.)*
5. **Harness hygiene** (`gauge_mb.py`): report confidence intervals and treat a band-crossing CI as **UNDECIDED** rather than FAIL — this alone reclassifies **C3** and **H9**. Add a per-row seed offset. Add a standing **shape-and-side-swap diagnostic** (run every asymmetric row mirrored A↔B, flag any that doesn't roughly mirror) — this would have caught E2 directly.
6. **Fix `lanchester_signature.py`:** remove the `PER_CELL=0` `setdefault` (line 24) so it tests both paths, and fix `_mk()`/`_sweep()` so `check_square` measures something real instead of a zero-division false PASS.
7. **Wire or retire the dead morale constants** (E9): replace the hardcoded `3.0` (`core/state.py:60`) with `MORALE_PHASE_CAP` (zero behavior change; closes a silent-tuning trap); `MORALE_EROSION_DAMP` as a per-phase multiplier is the natural softening lever. Flag `ROUT_FLOOR_LOSS_PCT`/`SUBUNIT_ROUT_FLOOR` **[CALIBRATED-DEBT]** pending DG-8.
8. **Fix `Unit._agg` to weight by live `cur_troops`** (`units.py:1570-1573`) — present as a correctness fix only, with **no** causal claim about which row it moves (direction ambiguous).
9. **`build_army` whitelist validation** (`engine.py:243-246`) — raise on unrecognized spec keys, mirroring the `role_allowed()` fail-loud precedent (E10). Additive.
10. **Editorial/doc fixes:** correct the false `exchange.py:100-109` "already generalizes… no change needed" comment (it generalizes for *density* only); correct the stale `config.py`/`orchestration.py` "INERT" comments on `ROLE_SPEC`/`TROOP_TYPE_ROLES`; add the `mass_battle_v30.md:627` supersession note (MORALE_SIBLING_PULL reversed "no intra-unit cascade" — DG-4/ED-MB-0002); update the stale `core/state.py` morale docstring.

**[BLOCKED — looked safe in isolation, now known gated]** **Do NOT ship an R3 fix as a safe item.** An earlier pass listed a "ranged `hold` variant that closes to volley range" among safe fixes; §2's probe supersedes that. Fixing R3 *correctly* (archers, disc 3, + `kite`) **re-freezes** because the node-path speed floor (E5) floors disc-3 movement to step 0. The R1-archers fix and the R3-kite fix are **mutually incompatible with historically-correct stats** until E5 is fixed. R3's fix is therefore gated on **DG-10**, not a contained change.

### (b) Jordan-ruling decision points — DG-6 … DG-16

**Renumbering note.** DG-1…DG-5 are **already ruled** and must not be reused (DG-1 = symmetric-at-parity / majority-pin composition; DG-2 = fighting-withdrawal/yield; DG-3 = intensive bottom-up pool; DG-4 = blended sibling-pull morale; DG-5 = "racing-clocks" — closed/refuted). New gates therefore continue as flat integers from DG-6, matching the MB-lane house style. Crosswalk from the wave labels is in the Appendix.

> **DG-6 — The resolution-architecture calibration (the deep one; widest blast radius).** The engine resolves ~100–175 per-pair contests to a fixed ~30% rout threshold, giving a melee exponent **p≈3.2** (live `PER_CELL=1`; critic **p≈3.15**) vs the Linear-Law target **≤1.4**. Any edge snaps to near-total — right for the cavalry-shock rows (C4/C5/C7), wrong for modest infantry edges. One global snappiness serves two masters. Options: **(i)** treat p≤1.4 as a hard structural target and re-architect damage accumulation so outcome scales with edge size (fixes modest rows *and* preserves large-edge rows — the hardest change; scale/constant tuning *provably* can't get there, plateau p≈1.65–1.7); **(ii)** sharply reduce rounds-to-rout so per-tick variance still dominates a modest edge (simpler, but risks flattening the cavalry rows that *should* be near-total); **(iii)** reinterpret what statistic the historical bands constrain (note: `single` mode is separately broken by the tick cap, so this is not a free lunch). *This directly executes ED-MB-0006's own recorded next action ("reconsider the degree/damage-tier discretization or the Lanchester interaction — not another pool-formula scale tweak").* The fixes in §7a #1 and #7 are partial and interact with whichever way this goes.

> **DG-7 — Which cell-count generator is canonical?** `footprint_for` (continuous, troops/density-driven — the one that satisfies the bottom-up directive) vs the legacy tier-table `CELL_PATTERN_FN` (troop-count-blind, but what every plain gauge row uses). Composed subunits collapse to 1 cell under `footprint_for` while single-shape opponents keep 25 legacy cells — the ~8× density artifact (E1). Options: **(i)** unify on `footprint_for` for everything (fixing its coarse stepping; requires porting single-shape rows and re-gauging); **(ii)** reconcile both to comparable cell-counts at equal troops (least disruptive); **(iii)** keep both, add a parity assertion. This gates §7a #1.

> **DG-8 — Morale floor of 1 while the general is present** (`mass_battle_v30.md:294` vs no floor implemented; morale reaches −0.66 from casualties alone). A *literal* floor-of-1 makes morale-rout unreachable while any general lives — breaking the passing H1 mirror and every morale-decided row. Options: **(i)** floor applies to **all** erosion channels; **(ii)** floor applies **only** to the exhaustion-pressure channel the surrounding §A.4 paragraph is about (code still wrong, fix much narrower). Do not implement either reading without this ruling.

> **DG-9 — Cavalry vs infantry envelopment differentiation.** The flank/rear shock is troop-type-agnostic (du Picq: any unfaceable rear attack is devastating), so infantry envelopment saturates to the same ceiling as cavalry, erasing the required gap (infantry 45–72% vs cavalry 75–100%). Options: **(i)** keep type-agnostic shock — the real bug is that infantry envelopment shouldn't *saturate* in the first place (i.e. the fix is DG-6/E1, not here) *(investigation leans this way)*; **(ii)** add an explicit cavalry differentiator on the flank bonus itself.

> **DG-10 — Node-path speed floor (the fix-blocker).** Fixing R1 (archers, disc 3) and R3 (kite) with historically-correct stats is impossible while `_node_advance` floors disc-3 movement to 0 (E5, proven §2). Options: **(i)** port the legacy fractional-velocity accumulator (`_speed_accum`) into `_node_advance` so disc-3 troops move at a realized ~0.7 cells/tick *(recommended — unblocks correct-stats rows and is where the grounding directive points)*; **(ii)** require `aggressive` stance / disc≥5 for any moving non-cavalry row *(a hack — `aggressive` doing accidental work)*; **(iii)** keep R3 on default disc-5 stats *(accepts a permanent stat-correctness inconsistency between R1 and R3)*. **This gates DG-11 and DG-14.**

> **DG-11 — Troop-type-derived speed, and completion of dr/stamina** *(merges two waves' asks into one question from two angles).* `TROOP_TYPE_STATS` derives only power/discipline/morale (ED-MB-0006); `dr` and `stamina` are deferred (ED-1018) and `speed` is never type-derived (only a hardcoded binary `PC_CAVALRY_SPEED_MULT=2.0`). Establish base per-type dr/stamina/speed at the subunit level, retiring the binary cavalry check — the direct sibling of the melee pool grounding already shipped. Options: **(i)** add per-type speed multipliers (+ dr/stamina) now *(anti-fabrication: needs cited magnitudes, do not invent numbers)*; **(ii)** keep the binary flag, defer *(status quo)*; **(iii)** minimal — at least wire the dead `tier`/`Unit.speed` into movement so quality has *some* effect. **Sequence after DG-10, or graded speeds still floor to 0.**

> **DG-12 — Per-cell granularity scope + the two-stamina-systems fork.** Confirm scoping near-term per-cell work to *quality tiers* (same `troop_type`, different power/discipline/dr per cell/rank — captures veteran-front/levy-rear) and treating literal per-cell *type* mixing as a separate, larger future decision. And rule on which of the **two live stamina systems** is canonical — `Subunit.stamina` (feeds `stam_pen`) vs `percell.py`'s per-column `_ColBlock.stamina` (feeds `_fatigue_sigma` directly into net successes) — they run simultaneously under `PER_CELL=1`, neither reading the other. Reconcile to one **before** adding a third cell-level layer. *(Lower urgency for the score — the per-cell quality axis is inert — but the stamina reconciliation is a correctness prerequisite.)*

> **DG-13 — Volley pool troop-grounding + the Square-Law double-count.** Should volley's base pool fold in `eff_size` to match melee's `POOL_QUALITY_MODEL`? Volley *already* has a post-roll numbers term (`K_SQUARE × eff_size`). Options: **(i)** `eff_size` in the base pool **and drop** the post-roll multiplier *(single-counts numbers)*; **(ii)** keep the post-roll multiplier, leave the base pool as-is *(status quo — accepts the melee/ranged asymmetry)*; **(iii)** both *(double-counts — likely wrong)*. Whichever, gate behind a default-off env var, byte-exact validated. (Related lower-priority axis: `VOLLEY_TN=6` and `RANGED_DR_DEFAULT=2` are single global constants; per-weapon `ARSENAL` distinctions are disclosed as "NOT YET WIRED.")

> **DG-14 — `hold`-stance semantics for ranged units.** Should `stance='hold'` on a ranged body permit a one-time advance to its own effective range, then hold (distinct from melee brace-hold)? Options: **(i)** yes — add advance-to-range-then-hold *(changes `hold` engine-wide)*; **(ii)** no — keep `hold` literal, require `kite` for closing *(then R3 must be rebuilt via kite — depends on DG-10)*; **(iii)** add a distinct `VolleyLine`-style primitive. **Depends on DG-10.**

> **DG-15 — Reach ratification (before filling `TROOP_TYPE_REACH`).** The table is empty, making the recoil gate's reach-half a no-op; filling it is a **live behavioral lever, not inert data entry** — it flips currently-**passing** C2/C6. Options: **(i)** infantry-polearms get `REACH_LONG`, cavalry stays `SHORT` *(preserves the C2/C6 repel for the right historical reason — Courtrai/Swiss precedent)*; **(ii)** cavalry lance = `REACH_LONG` *(defensible for the charge instant, but flips C2/C6 to cavalry-wins and disables the reciprocal recoil)*; **(iii)** leave empty pending a dedicated reach pass. *(Severity demoted: affects **zero** currently-failing rows — a future-ratification landmine, not a current-divergence cause.)*

> **DG-16 — Is the tactical/role layer aspirational or committed?** ~11–12 of ~15 instruction strings are inert; `role_allowed`/`ROLE_SPEC` are 0% exercised; the Orders substrate uses 2 of 4 trigger kinds, never chained. Options: **(i)** wire the historically-real ones (`screen`/`pursue`/`harass`) and route gauge rows through `role=` (exercising the gate); **(ii)** de-scope `ROLE_SPEC` as aspirational, correct the docstrings, stop advertising inert tags; **(iii)** status quo (raw kwargs, ungrounded tactics).

### (c) Needs more investigation before anyone acts

1. **Trace the side-dependent Arrowhead asymmetry (E2) to a specific line** — the top open lead: dominant for H2, contaminating all of C1–C7. Tick-by-tick trace of the same matchup mirrored A↔B, instrumenting movement/momentum/`_charge_shock_sigma`. Beyond a quick probe; scope as a focused task. Treat H2 and every C-row pass as *provisional* until traced.
2. **Confirm whether guarding `recalc_size` (§7a #4) actually rescues H4/H5** at n=60 — the cascade is proven to *fire*, its *causal contribution to the win rate* is not yet measured by ablation.
3. **Decompose H2's causal split:** how much is the ~1.33× geometry-driven per-pair edge (E2) vs the D1 amplification? Apportion before treating "reduce rounds-to-rout" as the H2 fix.
4. **Individually ablate H7 and H8** (assumed, not tested, to be amplifier-driven); H8's GappedLine-vs-Arrowhead interaction is genuinely unexplained (GappedLine dominates Line on both sides yet *loses* to Arrowhead-as-B).
5. **Quantify E7** (frozen momentum/`charge_pen`) contribution to the specific C1–C7 percentages — every surface left it unquantified.
6. **C3's 60/40 mirror asymmetry** — unresolved by the movement producer and its critic; likely wave-1 cascade-ordering, not a movement cause.
7. **The `sweep` maneuver's transit behavior** — under-investigated relative to `envelop`.
8. **Confirm §7a #2/#3 are `bat.py` byte-exact clean** and don't ripple into the other 18 rows — required before landing.
9. **The curative gap (state plainly to set expectations):** the investigation is **diagnostic, not curative.** Every ablation proved which lever *moves* a row (often reversing it to the opposite win-out); **no one has demonstrated a combination of fixes that lands any row in its band, let alone yields a specific N/20.** Expect an iterate-and-re-gauge loop with DG-6 as the rate-limiting step.

---

## 8. Honest disclosure of disagreement and residual uncertainty

Preserved deliberately, not smoothed into false consensus:

- **This whole investigation is diagnostic, not yet curative.** Removing the #1 density defect (E1) from H3 does **not** land it in the 55–72% band — it flips H3 to a *B* win-out. Proving a lever *reverses* a row is not proving a fix *calibrates* it. No net pass-count prediction is defensible until a full re-gauge after each toggle.
- **[CALIBRATED-DEBT] — the pass count is not monotonic in fixes applied.** Fixing E1 or D1 in isolation could knock the **currently-passing C4/C7** (and possibly **C5**) out of their near-total bands, because they may be passing *partly on the same artifacts* being removed elsewhere (C4/C7 on E1 density inflation + D1; C5 on D1 / the E2 Arrowhead-side-A advantage). Anti-fabrication flag: I cannot independently confirm they'd stay in-band post-fix. Things may look worse before better.
- **A surface refuted its own headline.** The morale-rout-cascade surface tagged its findings "dominant-cause"; its critic's ablation (no-op `rout_resolution` → H2 still 100/0) refuted that. Side with the critic: morale/rout is a **finisher, not a driver.** The mechanistic findings are gold; the severity was wrong.
- **The two dominant mechanisms look like they compete but do not.** Degree-snap claimed a general amplifier is *the* cause; deployment/envelopment proved a density artifact *reverses* the composed rows. They are **multiplicative** — E1 is the bias-generator for composed rows, D1 concentrates whatever it is fed, and removing *either* de-snaps a composed row. For plain rows, only D1 + a geometry-driven edge apply. Where they genuinely disagree is *emphasis*: degree-snap's "modest historical edge" framing understates that the edge reaching the resolver is often already large (its own critic measured H2 at ~1.33×). Weight the geometry/composition bias-generators as the more *actionable* levers and the amplifier as the deeper, harder ceiling.
- **Exponent discrepancy, adjudicated.** The live-path exponent (**p≈3.2** / critic **p≈3.15**) is *worse* than ED-MB-0006's on-record **p≈2.50** (and its **1.55** baseline, **1.65–1.7** plateau) — because ED-MB-0006's measuring tool hardcodes `PER_CELL=0`, the wrong path. And ED-MB-0006 tentatively blamed `compute_degree`'s tiering; this investigation shows the concentration survives with tiering stripped (architecture-general), so degree-tiering is a rider, not the driver. Carry all figures; trust the live-path number for the acceptance test.
- **H4's win-rate number:** 1.7% (ED-MB-0006 ledger + early re-synthesis) vs 2.5% (a later max-effort re-synthesis). Small-sample seed variance at n=60; both far below the 45–62% band. Do not treat the 0.8pp gap as meaningful.
- **A confirmed defect with a possibly-backwards causal story:** `Unit._agg` staleness (E8) is real, but the "stays artificially healthy" narrative may be backwards (it may bias toward *earlier* rout). Fix the code; distrust the story.
- **R3's classification is subtle:** it is a **harness-artifact whose clean fix is gated on an engine ruling (DG-10)** — the instinct that "something engine-level is missing" was directionally right, for the wrong reason. R1's flipper is the **troop_type harness bug**, not the volley collision (which is real, ~3× larger than stated, but leaves R1 near 50% alone).
- **Reach severity demoted:** producer rated it "dominant-cause"; it affects **zero currently-failing rows**, and C2==C6 are the same scenario built twice. A future-ratification landmine, not a current cause.
- **The single biggest thing nobody found:** the root line of the Arrowhead side-asymmetry (E2). It is a *dominant* cause of H2 and a confidence-contaminant for every cavalry row, and it remains narrowed only to "somewhere in the dynamic movement/charge-shock path."
- **Do not cite the shaky magnitudes:** the troop_type/eff_* site counts (~30% inflated), the refuted ~1pp orthogonality toy, and the non-reproducing R1 aggressive-stance figures. The qualitative conclusions they supported still hold on independent grounds.

**Net:** the mechanistic and file:line findings across all 11 surfaces held up unusually well under adversarial re-verification — nearly every citation and reproduced number was exact. What did *not* survive was a subset of *severity/causal* framings (morale as driver, sibling-pull as H4 cause, the amplifier's "modest edge" story, reach as dominant, the granularity toy's null). The engine is genuinely more correct than "7/20" suggests — 2 of the 13 fails are instrument noise and 2 more (R1, R3) are harness-construction, leaving ~9 real engine divergences — but those ~9 are driven by concrete, largely-fixable mechanisms gated behind one deep architectural ruling (DG-6) that no amount of constant-tuning will resolve.

---

## Appendix

### DG crosswalk (wave labels → final numbering)

| Final | Wave-1 label | Wave-2 label | Topic |
|---|---|---|---|
| **DG-6** | DG-A | — | Resolution-architecture calibration (exponent → ≤1.4) |
| **DG-7** | DG-B | — | Which cell-count generator is canonical |
| **DG-8** | DG-C | — | Morale floor of 1 while general present |
| **DG-9** | DG-D | — | Cavalry vs infantry envelopment differentiation |
| **DG-10** | — | DG-6a | Node-path speed floor (the fix-blocker) |
| **DG-11** | DG-E (stats part) | DG-6b | **Merged:** troop-type speed + dr/stamina completion |
| **DG-12** | DG-E (scope part) | — | Per-cell quality scope + two-stamina-systems fork |
| **DG-13** | — | DG-6c | Volley pool troop-grounding + Square-Law double-count |
| **DG-14** | — | DG-6e | `hold`-stance semantics for ranged |
| **DG-15** | — | DG-6d | Reach ratification (fill `TROOP_TYPE_REACH`) |
| **DG-16** | — | DG-6f | Tactics/role-layer grounding |

*Renumbering rationale:* DG-1..DG-5 are ruled (per `handoffs/HANDOFF_MB.md`, ED-MB-0002/0003/0005). An earlier combination draft reused DG-1..DG-5 for these *new* gates, colliding with the ruled namespace; this sequence corrects that to flat integers continuing from DG-5, per MB-lane house style.

### Key file:line index (carried from both waves, adversarially verified)

- **E1 density:** `geometry.py:77-104` (`footprint_for` stepping), `config.py:25-29` (`LINE_ASPECT`), `units.py:1555` (static `ncells`), `core/attrition.py:12-28` (`_lanchester_strength`, `tpc = hp/ncells`), `orchestration.py:963-971` (casualty multiplier), `core/exchange.py` `pair_pool_contribution` (second channel).
- **D1 amplifier:** resolution loop; exponent probe `lanchester_signature.py:24` (`PER_CELL=0` hardcode).
- **E2 Arrowhead asymmetry:** untraced — dynamic movement/momentum/`_charge_shock_sigma` path.
- **E3 hold / E5 floor:** `units.py:826` (hold early-return), `:836` (step floor), `:1109-1111` (dead legacy `_speed_accum`), `:753-786` (`_kite_goal`), `engine.py:307`; `config.py` (`STANCE_SPEED_MOD['hold']=-99`, `SIDE_A_START_ROW=34`, `SIDE_B_START_ROW=15`, `VOLLEY_MAX_RANGE=8`, `VOLLEY_MIN_RANGE=2`, `PC_CAVALRY_SPEED_MULT=2.0`).
- **E4 cascade:** `units.py:1603-1611` (`recalc_size`), `:294-299` (Subunit principle), `orchestration.py:1251` (terminating break).
- **E6 volley / E7 momentum:** `orchestration.py:1154-1166` (volley pool `max(1, eff_power − _vpen)`) vs `core/exchange.py:110` (melee pool `eff_power × eff_size × scale`).
- **E8/E9/E10:** `units.py:1570-1573` (`_agg`), `core/state.py:60` (hardcoded `3.0` shadowing `MORALE_PHASE_CAP`), `engine.py:243-246` (`build_army`).
- **Harness:** `gauge_mb.py:82-114` (`make_unit`), R1/R3 rows ~229-232, `:263` (C5 plain Arrowhead), `:289` (n=120→60 comment), `make_mixed_unit` (dead).
- **Grounding gaps:** `troop_types/registry.py` (`TROOP_TYPE_STATS` has no speed; `TROOP_TYPE_REACH={}`).
- **Canon/doc:** `designs/provincial/mass_battle_v30.md:294` (morale floor), `:627` (intra-unit-cascade supersession); stale `core/state.py` docstring; false `exchange.py:100-109` comment.
