# Mass-Battle Gauge Synthesis: Why 7/20, and What To Do About It

**Prepared for Jordan. Scope:** synthesis of 7 producer+critic surface investigations into `tests/sim/gauge_mb.py`'s stuck-at-7/20 divergence, under the live defaults (PER_CELL=1, POOL_QUALITY_MODEL=1, seed_base=1,000,000, n=60). Every claim below survived independent adversarial critique; I flag where it did not, and I discard what was refuted.

---

## 0. Bottom line up front

**7/20 is not one bug. It is roughly five distinct mechanisms plus two rows of pure sampling noise.** The instruction to "identify ALL issues, not just one dominant cause" is correct: there is no single villain, and any writeup that names one is wrong. The failing rows partition cleanly by mechanism, and the mechanisms live at different layers (geometry, resolution architecture, movement, rout timing, and the measuring instrument itself).

Two results dominate everything else in confidence, because they are **causally proven by reversal ablations that two independent critics reproduced from scratch**, not merely correlated:

1. **A cell-count/density plumbing defect** (`footprint_for` collapse → static `unit.ncells` → Lanchester density term) single-handedly decides the outcome of the five composed-army infantry rows. Patching the density term to be representation-invariant *flips* H3 from 100%/0% to 0%/100% and H10 the other way.
2. **A super-linear resolution architecture** (melee exponent p≈3.2 under the live path, vs the historical-target ≤1.4) turns *any* residual edge into a near-deterministic snap. This is why even a density-corrected H3 does not land in its 55–72% band — it flips to a *B* win-out instead. The bias-generator and the amplifier compound; **no single fix lands a row in-band.**

The most important framing correction for you: **your "granularity" directive bundles two axes with opposite relevance to this gauge.** The per-cell *quality* half (veteran-front/levy-rear, `cell_power` dicts) is *provably inert* for all 20 current rows — worth doing for future fidelity, but it cannot move the score. The *number-of-cells / density* half is exactly where the dominant bug lives. Your instinct that "everything should be grounded by the number of troops per cell" is pointing straight at the #1 root cause — just not at the part (per-cell quality) that the architecture-proposal surface was drafting.

And a caution that reframes the whole remediation: **the engine currently snaps everything to near-total. The gauge *wants* some rows near-total (the cavalry shock rows C4/C5/C7) and others modest (the H-series infantry).** So the fix is not "reduce snappiness globally" — that would break the passing cavalry rows. The fix is "make the outcome scale with the *size* of the edge," which is precisely what a melee exponent of ≤1.4 (the Lanchester Linear Law) gives you: small edge → modest result, large edge → near-total result. That exponent target is the north star, and it is the hardest, least-tractable finding in the whole investigation.

---

## 1. Ranked root causes (confirmed only)

### #1 — Footprint/`ncells` Lanchester-density artifact  *(engine defect; dominant for 5 rows; causally proven)*

**Rows:** H3, H5, H6\*, H10, H11 directly; contributes to H4; latent risk to C4/C7.
**Convergence — the strongest signal in the investigation:** the *deployment-geometry* and *envelopment-composition* surfaces found this **independently**, and both critics ran the **same reversal ablation and got the same flip.** The *pool-granularity* surface (finding 5) and *degree-snap*'s critic point at the identical code from a third and fourth angle. Four surfaces, one mechanism.

**Mechanism.** `geometry.py` has two unreconciled cell-count generators. The legacy tier-table path (`CELL_PATTERN_FN`, used by every plain single-shape unit) always yields ~25 cells for a T3 body regardless of troop count. The continuous `footprint_for` path (used *only* by the composed `_envelop_army`/`_refused_army` presets) derives cell count from troops/density — but its `LINE_ASPECT=1.4` stepping is so coarse that a 133–200-troop subunit collapses to **1 cell**. So a composed army of 400 troops becomes 2–3 fat cells (density ~133) while its equal-troop single-shape opponent stays at 25 cells (density ~16) — an **~8× density ratio**. That density feeds `core/attrition.py`'s `_lanchester_strength` via `tpc = unit.hp / unit.ncells` (`ncells` is a *static* sum computed once in `Unit.__post_init__`, `units.py:1555`, never recomputed), and `orchestration.py:963–971` applies it as a direct casualty multiplier.

**Why it's #1.** The critic patched `_lanchester_strength` to a representation-invariant density and, holding *everything else fixed* (wings engaging normally, all toggles default), **H3 reversed 100%→0% and H10 reversed 0%→100%** at n=20. Running H3 with PER_CELL=0 (which disables envelopment-sigma, charge-shock and fatigue entirely) *still* gave 100%/0% — so the fancy envelopment machinery is not even necessary to produce the overshoot; **this defect alone is sufficient.** This directly **updates ED-MB-0004's working theory**, which had blamed "envelopment/charge-shock morale collapse" for these rows — that theory is at best incomplete under the current defaults.

**Corroborating correlation** (envelopment-composition critic): the two cavalry rows that *pass* (C4, C7) are exactly the ones where the majority center (266 troops, pin_frac=2/3) escapes full collapse to 6 cells while only the minority wings collapse; every *failing* composed row uses symmetric splits that collapse *every* subunit. Collapse severity tracks pass/fail almost perfectly.

**A second amplification channel** (envelopment-composition critic, new): the identical footprint collapse also inflates power through `core/exchange.py`'s `pair_pool_contribution` — a 1-cell subunit commits its *entire* base pool to a single contact (`weighted_troops == cur_troops` by construction), whereas a 25-cell formation commits only its front rank plus depth-weighted support. So the collapse hurts twice.

\***H6 is the exception that proves the rule:** RefusedFlank-vs-Line, A *loses* (11.9%) despite refused-flank having the *higher* inflated density — the direction is wrong for this defect. H6 is instead driven by the refused wing sitting out via `hold` until its release trigger, so only ~half of A's troops engage the full-strength enemy early. H6 belongs with the amplifier + a hold-timing issue, not this defect. (Correctly ruled out by the producer.)

**Correction to fold into any ledger entry:** deployment-geometry F1 wrongly listed **C5** among the `_envelop_army` rows. C5 uses a plain `'Arrowhead'` shape via the legacy path; it is *not* affected by this defect. (Critic-verified against `gauge_mb.py`'s CAV_TESTS.)

### #2 — Super-linear resolution architecture / resolve-to-absorption amplifier  *(design tradeoff; broadest reach; deepest and hardest)*

**Rows:** all asymmetric rows, as the amplification layer. Owns the plain-row snaps (H2, H7, H8) and rides on top of every composed row.
**Convergence:** *degree-snap* (finding 1) and the *lanchester_signature* exponent re-fit (*degree-snap* F5, corroborated qualitatively by *pool-granularity* F3) are the same phenomenon measured two ways.

**Mechanism.** A battle resolves ~100–175 independent stochastic per-pair contests to a fixed ~30% cumulative-loss rout threshold (critic reproduced the event counts digit-for-digit: 115–175 events over 7–11 turns for H2). By gambler's-ruin/CLT concentration, *any* persistent per-tick bias concentrates toward certainty as rounds-to-absorption grow. The critic confirmed this **survives stripping degree-tiering out entirely** (pure linear damage was *more* extreme), so it is architecture-general, not a `compute_degree` artifact. Measured as a conserved-quantity exponent, melee sits at **p≈3.2 under the live PER_CELL=1 path** (critic's independent wide-grid fit: p≈3.15) — far above the Lanchester Linear-Law target of ≤1.4, and materially worse than the previously-disclosed p~1.65–2.5, which was measured under the *wrong* code path (`lanchester_signature.py:24` hardcodes `PER_CELL=0` via `setdefault`, but the gauge runs PER_CELL=1).

**Why it's #2 not #1, but load-bearing.** It is necessary-but-not-sufficient. Removing the #1 density artifact from H3 does not land it in-band; it flips to a B win-out — the amplifier is still snapping the residual edge. So **both #1 and #2 must be addressed for the composed rows to land**, and #2 alone owns the plain rows. Its own critic flagged the honest gap: the surface never measured H2's *actual* per-pair pool ratio, which runs ~1.33× (4 vs 3 dice) — **not obviously "modest."** So the causal chain has two links: (a) something hands the resolver an outsized per-pair edge (geometry/composition — see #1 and #3), and (b) this architecture amplifies whatever it gets to near-certainty. The "modest historical edge → unfair snap" story overstates link (a)'s innocence; the edge reaching the resolver is often already large for reasons that belong to other surfaces.

**The critical calibration coupling:** because the engine has *one* global snappiness that is too high for infantry but happens to be right for the deliberately-near-total cavalry rows (C4/C5/C7), you cannot de-snap globally. The exponent-to-≤1.4 target is the right frame precisely because it makes the outcome *scale with the edge*: it de-snaps modest infantry edges while preserving near-total cavalry edges. **Acceptance test for any amplifier fix: `check_law_exponents()` passing at p≤1.4 under PER_CELL=1** — noting the disclosed residual that scale-sweeping `POOL_QUALITY_SCALE` never reached ≤1.4 (plateau ~1.65–1.7 even under PER_CELL=0), so this needs a *structural* change, not a constant tweak.

### #3 — Side-dependent Arrowhead asymmetry  *(engine defect, presumed; dominant for H2; root cause UNTRACED — the biggest open lead)*

**Rows:** H2 (dominant), H9 (contributes).
The exact same Arrowhead-vs-Line matchup gives **100/0/0 in ~8.9 turns when Arrowhead is on side A, but 43/43/13 (near-coinflip) in ~15.8 turns when Arrowhead is on side B** — reproduced to the decimal by the critic. A GappedLine control rules out a generic side bias (GappedLine dominates Line on *both* sides), so this is specific to Arrowhead, the one shape whose per-row width tapers. The producer ruled out four static-geometry candidates (placement, cell_speed tip-detection, envelopment-sigma column comparison, per-cell troop distribution) by direct code reading, narrowing the cause to the **dynamic movement/momentum/charge-shock path** — but **nobody found the offending line.** This is the single most important untraced lead: it is a dominant cause of the worst plain-row overshoot (H2), and it silently contaminates confidence in *every* cavalry row, since Arrowhead sits on side A in all of C1–C7. H9 (Line vs Arrowhead, Arrowhead-as-B-weakness) is partly explained by the same asymmetry, on top of being harness noise (#6).

### #4 — `hold`-stance non-engagement  *(engine defect; clean, contained; fully explains R3)*

**Rows:** R3 (fully), R1 (partially).
**Convergence — three surfaces:** *degree-snap* F3, *harness-construction* F4, and *deployment-geometry* F5 all land here, and *degree-snap* F4 shows it also silently breaks the `lanchester_signature` `check_square` test.
Both sides in R3 deploy 19 rows apart (`SIDE_A_START_ROW=34`, `SIDE_B_START_ROW=15`) while `VOLLEY_MAX_RANGE=8`, and `hold` stance is an unconditional no-advance early-return (`units.py:826` / `engine.py:307`, `STANCE_SPEED_MOD['hold']=-99`). With both sides holding, they **never close into weapon range — literally zero casualties, zero volleys, guaranteed draw at the 20-turn cap** (critic: `a_cas=b_cas=0.0` exactly). `hold` conflates "don't close to melee" (correct for a braced line) with "never move even to enter firing range" (wrong for a ranged unit). R1 engages because only one side holds; its 66.1% overshoot (band 0–30) is partly this asymmetric-closing dynamic.

### #5 — `recalc_size` aggregate-floor force-rout cascade  *(engine defect; contributes to the H4 anomaly and H5)*

**Rows:** H4 (candidate primary driver), H5.
`Unit.recalc_size()` (`units.py:1603–1611`) marks **every** subunit routed the instant the *whole-unit aggregate* troop total floors to `size==0` — with no `len(subunits)==1` guard, unlike `cohesion`/`eff_size` in the same class, and in direct contradiction of the `Subunit` dataclass's own stated principle ("a heavily-hit subunit can break while a fresh sibling holds — Cannae/Hastings"). The *pool-granularity* critic **upgraded this from structural-only to empirically confirmed**: it fires in **55/60 H5 seeds** (two siblings holding 44–56 troops each are force-routed anyway) and **15/60 H4 seeds** (both wings holding ~49–51 healthy troops force-routed alongside the dead center), and traced it to the battle-terminating `if unit_a.routed or unit_b.routed: break`. This is the same event the *envelopment-composition* surface saw as "center dies → whole army routs" — **the two surfaces describe one mechanism** (the pool critic explicitly flagged the dedup). For H4 specifically it is a strong candidate for the "attacker loses badly" anomaly.

### #6 — Harness sampling noise (n=60, no confidence intervals)  *(harness artifact; removes ~2 rows from the real divergence)*

**Rows:** C3, H9.
At n=60, decA has SE ≈ 6–7pp. C3 (60.0 vs band 42–58) sits 0.32 SE from the edge and **passes in 3 of 4 alternate seed_bases** (critic reproduced: 60.0/56.7/51.7/48.3). H9 sits 0.72 SE out and passes in 2 of 4. **These are not robust failures.** Under a CI-reporting harness they would read UNDECIDED, not FAIL — so the *real* engine-divergence count is closer to **11/20, not 13/20.** This also settles an internal conflict (see §6): C3 is *not* evidence that the amplifier reaches a near-mirror; it is noise, and C3 is Arrowhead-vs-Arrowhead where the slot asymmetries cancel by construction.

### Secondary / contributing / latent (all confirmed, none load-bearing on the score)

- **`compute_degree` adaptive-Ob convexity** *(demoted; already-disclosed)* — real but secondary, and its magnitude is pool-size-dependent in a way the surface under-disclosed. At the *actual* per-pair regime (3–4 dice, critic-traced), it is small (matches the producer's numbers); at large pools (16–100) it is 2–6×. It rides on #2, it doesn't drive it. The long-open question "is the relative-Ob construction what turns a modest edge into a snap?" is now answered: **mostly no** — the concentration is architecture-general.
- **`Unit._agg` static-weight staleness** *(engine defect; directionally ambiguous)* — aggregates weight by static nominal `troop_count`, not live `cur_troops` (`units.py:1570–1573`), and `agg_morale()<=0` is a live rout trigger. Real defect, cheap fix — **but the critic's caution is important: the directional story is possibly backwards** (over-weighting a decimated, usually-lower-morale subunit biases toward *earlier* rout, not "stays artificially healthy"). Do not build a causal argument on it.
- **Two uncoordinated stamina systems** *(design tradeoff)* — `Subunit.stamina` (feeds `stam_pen`) and `percell.py`'s per-column `_ColBlock.stamina` (feeds `_fatigue_sigma` directly into net successes) run simultaneously under PER_CELL=1, neither reading the other. Must be reconciled before any per-cell stamina work.
- **Dead morale constants** *(engine defect; safe)* — `MORALE_EROSION_DAMP`, `ROUT_FLOOR_LOSS_PCT`, `SUBUNIT_ROUT_FLOOR` are defined/exported/provenance-tracked but **never consumed anywhere**; `MORALE_PHASE_CAP` is shadowed by a hardcoded `3.0` in `core/state.py:60`. These are exactly the levers that would soften the collapse if wired.
- **`build_army` silent key-drop** *(engine defect; latent footgun)* — unrecognized spec-dict keys (e.g. a typo `'stamnia'`) are silently ignored, not rejected. No live row affected today.
- **TROOP_TYPE_STATS incompleteness** *(gap in your own directive, subunit level)* — flagged by two critics. `troop_types/registry.py` derives only power/discipline/morale from `troop_type`; **`dr`, `stamina`, and `speed` are not type-derived at any granularity.** `Subunit` has no `speed` field at all; `Unit.speed` is a plain kwarg. You explicitly named "speed" in the directive — the coarsest layer isn't finished.
- **Doc-currency debt** *(a fifth bucket — see §2)* — `mass_battle_v30.md:627` still says "no intra-unit cascade," superseded three weeks later by `MORALE_SIBLING_PULL` (DG-4/ED-MB-0002); `core/state.py`'s morale docstring is stale; the false "already generalizes… no change needed" comment at `exchange.py:100–109`; the `ROUT_EXHAUSTION_MORALE_HIT` name/formula mismatch.

### Explicitly demoted or refuted (do not resume these as live theories)

- **Morale/rout as an independent amplifier** — **REFUTED by its own surface's critic.** With `rout_resolution` monkeypatched to a no-op (morale/rout can never end a battle), H2 *still* resolves A=20/B=0 with the loser taking ~70% casualties before dying outright. Morale/rout is a **downstream finisher riding on an already-decided casualty trajectory**, not a driver. The producer's "dominant-cause" severity tags contradicted their own hedge; the mechanistic and empirical claims are solid, the severity is not.
- **`MORALE_SIBLING_PULL` as the H4 cause** — **REFUTED.** Ablation (0.15 vs 0.0) gives virtually identical H4 results (0% decA both ways). The contagion is real and measurable (undamaged wings drop 6.00→4.33) but it is *not* what loses H4 for the attacker. H4 is composition (#1/#5) + slot asymmetry, not morale contagion — a conclusion two surfaces reached independently.
- **Post-rout pursuit** — architecturally unreachable for all 20 rows (only wired into `run_multi_unit_battle`, which the gauge never calls). Confirmed non-factor.

---

## 2. The H4 "Cannae" anomaly, on its own

H4 is the one failure that does *not* fit "the edge-holder win-outs" — the historically-favored envelopment attacker *loses badly* (2.5% vs band 45–62). It has its own compound story, now well-supported:

1. **Composition:** the symmetric-thirds force-parity split (DG-1) gives the pinning center only 1/3 of the troops (133) against a full-strength 400-troop Arrowhead that *also* carries the wedge edge already saturating H2. The center dies fast.
2. **Slot asymmetry (#3-adjacent, RC-5):** H4 and H11 are the same matchup mirrored, yet the wing-release mechanic is *inert* in H4's slot (freeze-wings ablation is byte-identical — center annihilated before wings matter) and *decisive* in H11's slot (freeze-wings flips the distribution). Confirmed by matched-seed ablation.
3. **`recalc_size` cascade (#5):** once the center floors, the whole army is force-routed including two healthy wings, ending the battle B-win.

**This is a genuinely different failure mode and should be tracked separately.** It is *not* morale contagion. Note the harness surface's separate confirmation that H4's 33% *draw* rate is a turn-cap artifact (extending the cap 20→40 collapses draws 30%→5%) — **but decA stays flat at 0.0 in both**, so the "attacker loses" verdict is real engine behavior, not truncation.

---

## 3. The 13 "failing" rows, attributed

| Row | Result vs band | Primary mechanism(s) | Bucket(s) |
|---|---|---|---|
| **H2** | 100 vs 48–62 | **#3** Arrowhead side-asymmetry (untraced) + **#2** amplifier | defect (open) + tradeoff |
| **H3** | 100 vs 55–72 | **#1** footprint/ncells density (reversal-proven) + **#2** amplifier | defect + tradeoff |
| **H4** | 2.5 vs 45–62 | composition (1/3 center) + slot-asymmetry + **#5** cascade; **not** sibling-pull | defect + tradeoff |
| **H5** | 98.2 vs 48–62 | **#1** density + **#5** cascade (55/60 seeds) | defect |
| **H6** | 11.9 vs 48–60 | refused-flank hold/release (half army sits out) + **#2**; density ruled OUT | defect + tradeoff |
| **H7** | 88.3 vs 48–62 | **#2** amplifier on a real GappedLine edge | tradeoff |
| **H8** | 33.9 vs 50–65 | **#2** + Arrowhead/GappedLine shape interaction (not individually traced) | tradeoff + open |
| **H9** | 57.1 vs 38–52 | **#6** harness noise + **#3** Arrowhead-as-B weakness | harness + defect |
| **H10** | 0 vs 28–45 | **#1** density (reversal-proven) | defect |
| **H11** | 0 vs 38–55 | **#1** density + slot asymmetry | defect |
| **R1** | 66.1 vs 0–30 | **#4** hold-stance (only one side closes) | defect |
| **R3** | draw vs 42–58 | **#4** hold-stance non-engagement (3-surface convergence) | defect |
| **C3** | 60 vs 42–58 | **#6** harness noise (mirror; flips across seeds) | harness |

Passing rows for reference: H1 (mirror), C1/C2/C6 (contested/braced-repel), C4/C5/C7 (near-total by grounding — **C4/C7 flagged [CALIBRATED-DEBT]**: may pass partly on residual density inflation, see §6).

---

## 4. Bucket discipline

Your four buckets, plus a fifth that two critics correctly noted doesn't fit any of the four:

**Engine defects (genuinely wrong, safe to fix behind an ablation toggle):**
- #1 footprint/`ncells` density plumbing (the Lanchester-density-reading defect; the generator *choice* has a design tail — see §5).
- #4 `hold`-stance non-engagement for ranged units.
- #5 `recalc_size` force-rout cascade (violates the class's own stated principle).
- `Unit._agg` static-weight staleness; dead morale constants + hardcoded `3.0`; `build_army` silent key-drop; `ROUT_EXHAUSTION_MORALE_HIT` mismatch.
- (Presumed) #3 Arrowhead asymmetry — *once traced*; today it's a defect whose location is unknown.

**Design-tradeoff / canon-structure calls (need an explicit Jordan ruling — see §6):**
- #2 the resolve-to-absorption architecture / exponent target (the deepest call).
- Which cell-count generator is canonical (`footprint_for` vs legacy tier-table).
- Morale floor-of-1-while-general-present (canon vs code).
- Cavalry-vs-infantry envelopment differentiation.
- Per-cell quality architecture scope + stamina-granularity reconciliation.
- Extending TROOP_TYPE_STATS to dr/stamina/speed.

**Harness-construction artifacts (the engine may be more correct than the raw count suggests):**
- #6 n=60 with no CIs → C3, H9 are noise, not fails. **The real divergence is ~11/20.**
- `lanchester_signature.py`'s `check_square`/volley leg is a degenerate false-positive (the same hold-stance bug), so the square-law signature has apparently never been genuinely measured.
- `make_mixed_unit` is dead code w.r.t. the battery → **zero gauge coverage of your granularity directive** (nothing could detect a regression in that machinery).

**Already-disclosed residuals, now confirmed / deepened / demoted:**
- `attrition.py` static `ncells` / whole-unit density: **confirmed and promoted from "flagged residual" to "proven-decisive by reversal ablation."** The biggest deepening in the investigation.
- Lanchester exponent >1.4: **confirmed and worse than disclosed** (p≈3.2 under the live PER_CELL=1 path; the disclosed 1.65–2.5 measured the wrong path).
- `compute_degree` adaptive-Ob: investigated and **demoted** to secondary/pool-size-dependent.
- RC-5 / ANCHOR_MAP slot asymmetry: **confirmed and split into three sub-parts** — the H4/H11 slot flip (large, live), the front-anchor-depth convention (real but currently inert — no shallower shape on side B), and a 1-cell ANCHOR_MAP column drift (minor). The live, dominant slot asymmetry (#3) is a *separate, untraced* thing.

**Doc-currency / editorial debt (the fifth category — neither engine, gauge, tradeoff, nor prior residual):**
- `mass_battle_v30.md:627` supersession note (MORALE_SIBLING_PULL reverses "no intra-unit cascade"); stale `core/state.py` docstring; the false `exchange.py:100–109` "already generalizes" comment.

---

## 5. The granular per-cell troop-stat architecture — verdict

**Verdict: effectively (c) both — but only because your one word "granularity" bundles two axes with *opposite* relevance, and the entire value of this answer is in un-bundling them.**

**The per-cell QUALITY axis (the architecture-proposal draft: `cell_power`/`cell_discipline`/`cell_dr` dicts, veteran-front/levy-rear) → (b): good for other reasons, NOT driving 7/20.** This is *provably inert* for all 20 rows — a conclusion three surfaces reached independently (architecture-proposal, pool-granularity, degree-snap F6). No gauge builder (`make_unit`, `_envelop_army`, `_refused_army`, and even the purpose-built-but-dead `make_mixed_unit`) populates any per-cell override, and the proposal is backward-compat-inert-by-design (empty dict → collapses to today's scalar, byte-exact). It would touch **none** of the confirmed root causes #1–#6: #1 operates on cell *count*, not quality; #2 operates on the aggregate scalar bias regardless of how it's internally decomposed. **Do not expect it to move the score.** It is a legitimate future capability (hoplite/pike "best men in front," mixed-composition subunits) and it matches your directive — pursue it on its own merits, scoped as its own lane-block, and *add a gauge row that actually exercises it* (via `make_mixed_unit` against a historically-grounded band) so the machinery isn't untested.

**The NUMBER-of-cells / DENSITY axis → (a): directly necessary, and it is the #1 root cause.** Your instinct that a subunit's power/health should be grounded by "the number of troops per cell and the number of cells" is *correct and load-bearing* — because the dominant bug is precisely that cell *count* is derived two incompatible ways and the density flowing from it decides battles through a stale static field. This half of your directive isn't orthogonal busywork; it's the highest-leverage fix in the report.

**Caveat on the QUALITY axis's own foundations:** even the *subunit-level* type-derivation is incomplete. TROOP_TYPE_STATS derives only power/discipline/morale — not `dr`, not `stamina`, and not `speed` (which you named explicitly). Establishing base per-type values for those is a **prerequisite** before a per-cell override layer for them is meaningful.

One demotion to note honestly: the degree-snap surface's *specific empirical* argument for orthogonality (a FEEDBACK-vs-FROZEN toy showing ~1pp difference) was **refuted** by its critic (13–15pp, sign-flipping under trivial floor-vs-round choices). The *structural* argument (aggregate bias is one scalar regardless of decomposition) stands on its own logic and is independently confirmed by the "provably inert" finding — so the conclusion holds, but not on that toy model's numbers.

---

## 6. Recommended next actions

### (a) Safe to fix now — contained, ablation-toggle-able, byte-exact-preservable

Ordered by leverage. Each fits the repo's toggle discipline (new default-off env var; current behavior stays selectable; validate byte-exact-where-applicable via `bat.py`'s digest harness).

1. **Make the Lanchester density term invariant to the cell-count-representation mismatch** (`core/attrition.py:12–28`). This is #1, the highest-leverage lever. Two candidate implementations — *the direction is validated by the reversal ablation, the implementation is a design choice (see 6b#2)*: (i) give `footprint_for` finer stepping so a composed subunit doesn't jump 1→6 cells (`geometry.py:77–104`, `config.py:25–29`), or (ii) normalize `_lanchester_strength` by physical frontage/troops rather than by static `unit.ncells`. **Acceptance test: the ncells-equalization reversal (H3 flips) no longer occurs — i.e. the result is invariant to how many cells a body is represented with.** Also recompute `ncells` live (it's stale by construction, `units.py:1555`). *Warning: this will move C4/C7 and may drop them out of their bands — pair with the amplifier work, don't ship alone.*
2. **Guard the `recalc_size` cascade** (`units.py:1603–1611`) so only subunits whose *own* size floors get routed, matching the class's stated principle and the `len(subunits)==1` fast-path idiom already used by `cohesion`/`eff_size`. Toggle-gated. (#5; H4/H5.)
3. **A ranged `hold` variant that closes to volley band then stops** (`units.py:826`), distinct from melee brace-hold. Gate behind e.g. `RANGED_HOLD_CLOSES_TO_RANGE` defaulting to the corrected behavior. (#4; R1/R3.) Fix the twin bug in `lanchester_signature.py`'s `_mk()`/`_sweep()` so `check_square` measures something real, and make that file test *both* PER_CELL settings instead of hardcoding 0 (`line 24`).
4. **Harness hygiene** (`gauge_mb.py`): restore a larger `n` for band-straddling rows or report a confidence interval and treat a band-crossing CI as UNDECIDED rather than FAIL. This alone reclassifies C3 and H9. Add a per-row seed offset (defense-in-depth). Add a standing **shape-and-side-swap diagnostic** (run every asymmetric row mirrored A↔B and flag any row that doesn't roughly mirror) — this would have caught #3 directly.
5. **Wire or retire the dead morale constants** (`config.py:27,47,48,49`; replace the hardcoded `3.0` at `core/state.py:60` with `MORALE_PHASE_CAP` — zero behavior change today, closes a silent-tuning trap). `MORALE_EROSION_DAMP` as a per-phase multiplier is the natural softening lever. Flag `ROUT_FLOOR_LOSS_PCT`/`SUBUNIT_ROUT_FLOOR` as [CALIBRATED-DEBT] pending 6b.
6. **Fix `Unit._agg` to weight by live `cur_troops`** (`units.py:1570–1573`) — small, independently correct. (Present it as a correctness fix, *not* with a causal claim about which row it moves — the direction is ambiguous.)
7. **`build_army` whitelist validation** (`engine.py:243–246`) — raise on unrecognized spec keys, mirroring the existing `role_allowed()` fail-loud precedent. Additive, ablation-irrelevant.
8. **Editorial/doc fixes** (5th bucket, no behavior change): correct the false `exchange.py:100–109` comment (it generalizes for *density* only, not quality); add the `mass_battle_v30.md:627` supersession note; update the stale `core/state.py` morale docstring.

### (b) Genuine Jordan-ruling decision points

Phrased as this session's DG-/RC- rulings have been:

> **DG-A — The resolution-architecture calibration (the deep one).** The engine resolves ~100–175 independent contests to a fixed ~30% rout threshold, giving a melee exponent p≈3.2 vs the Linear-Law target ≤1.4. This makes *any* edge snap to near-total, which is right for the cavalry-shock rows (C4/C5/C7) but wrong for modest infantry edges — the engine has one global snappiness serving two masters. Do you want to: **(i)** treat p≤1.4 as a hard structural target and re-architect damage accumulation so outcome scales with edge size (fixes modest rows *and* preserves large-edge rows, but is the hardest change and constant-tuning demonstrably won't get there); **(ii)** reduce rounds-to-rout so per-tick variance still dominates a modest edge at resolution (simpler, but risks flattening the cavalry rows that *should* be near-total); or **(iii)** reinterpret what statistic the historical bands constrain (note: the `single`-mode alternative is separately broken by the tick cap, so this is not a free lunch)? *This is the ruling with the widest blast radius; the fixes in 6a#1 and 6a#5 are partial and interact with whichever way this goes.*

> **DG-B — Which cell-count generator is canonical?** `footprint_for` (continuous, troops/density-driven — the one that satisfies your bottom-up directive) vs the legacy tier-table `CELL_PATTERN_FN` (troop-count-blind, but what every plain gauge row still uses). Unifying on `footprint_for` requires fixing its coarse stepping (6a#1); keeping the legacy path means accepting that density isn't truly bottom-up. Which is the future of record?

> **DG-C — Morale floor of 1 while the general is present** (`mass_battle_v30.md:294` vs no floor implemented). A *literal* floor-of-1 makes morale-rout unreachable while any general lives — which would break the currently-passing H1 mirror and every row decided by morale-driven rout. Does the canonical floor apply to **all** erosion channels, or **only** the exhaustion-pressure channel the surrounding §A.4 paragraph is actually about (in which case the code is still wrong but the fix is much narrower)? *Do not implement either reading without this ruling.*

> **DG-D — Cavalry vs infantry envelopment.** The flank/rear shock machinery is troop-type-agnostic (du Picq: any unfaceable rear attack is devastating regardless of who delivers it), so infantry envelopment saturates to the same ceiling as cavalry, erasing the historically-required gap (infantry 45–72% vs cavalry 75–100%). Is the type-agnostic shock **correct** — with the real bug being that infantry envelopment shouldn't saturate in the first place (i.e. the fix is DG-A/#1, not here) — or do you want an **explicit** cavalry differentiator on the flank bonus itself? *The investigation leans toward the former.*

> **DG-E — Per-cell granularity scope + the stamina fork.** Confirm scoping the near-term per-cell work to *quality tiers* (same `troop_type`, different power/discipline/dr preset per cell/rank — captures veteran-front/levy-rear) and treating literal per-cell *type* mixing as a separate, larger future decision. And rule on which of the **two live stamina systems** (subunit-scalar vs per-column `_ColBlock`) is canonical — reconcile to one before adding a third cell-level layer. Also: do you want dr/stamina/**speed** added to TROOP_TYPE_STATS (subunit-level completion of your own three-item directive) as a prerequisite?

### (c) Needs more investigation before anyone acts

1. **Trace the side-dependent Arrowhead asymmetry (#3) to a specific line.** This is the top open lead — dominant for H2, contaminating all of C1–C7. Requires a tick-by-tick trace of the *same* matchup mirrored A↔B, instrumenting movement/momentum/`_charge_shock_sigma` to catch the divergence point. Explicitly beyond a quick probe; scope it as a focused task.
2. **Confirm whether guarding `recalc_size` (6a#2) actually rescues H4/H5** at n=60, not just that the cascade *fires*. The cascade is confirmed to fire; its *causal* contribution to the win-rate is not yet measured by ablation.
3. **Decompose H2's causal split:** how much of the outcome is the ~1.33× geometry-driven per-pair edge (#3) vs the architecture amplification (#2)? The two links need apportioning before "just reduce rounds-to-rout" is treated as the H2 fix.
4. **Individually ablate H7 and H8**, which were assumed (not tested) to be amplifier-driven; H8's GappedLine-vs-Arrowhead interaction is genuinely unexplained (GappedLine dominates Line on both sides yet *loses* to Arrowhead-as-B).
5. **The curative gap — state this plainly to manage expectations:** the investigation is *diagnostic, not curative.* Every ablation proved which lever *moves* a row (often reversing it to the opposite win-out); **no one has demonstrated a combination of fixes that lands any row in its band, let alone yields a specific N/20.** Removing #1 from H3 flips it to a B win-out, not into 55–72%. Expect an iterate-and-re-gauge loop, not a one-shot fix, and expect the amplifier (DG-A) to be the rate-limiting step.

---

## 7. Honest disclosure of disagreement and unresolved tension

Per house style, the false-consensus risks I am explicitly *not* papering over:

- **A surface refuted its own headline.** The morale-rout-cascade surface tagged its findings "dominant-cause"; its critic's ablation (no-op `rout_resolution` → H2 still 100/0) refuted that. I side with the critic: **morale/rout is a finisher, not a driver.** The mechanistic findings are gold; the severity was wrong.
- **The two "dominant" surfaces are not actually in conflict — but they *look* like they compete.** Degree-snap claims a general amplifier is *the* cause; deployment/envelopment prove a density artifact *reverses* the composed rows. Adjudication: **they are multiplicative, not competing** — the density artifact is the bias-generator for composed rows, the amplifier concentrates whatever bias it's fed, and removing *either* de-snaps a row. For plain rows only the amplifier + a geometry-driven edge apply. Where they genuinely disagree is emphasis: degree-snap's "modest historical edge" framing understates that the edge reaching the resolver is often already large (its own critic measured H2 at 1.33×). I weight the geometry/composition bias-generators as the more *actionable* levers and the amplifier as the deeper, harder ceiling.
- **A cross-surface evidence conflict, adjudicated:** degree-snap cited C3's 60% as proof the amplifier reaches a near-mirror; the harness surface showed C3 flips across seed_bases and is a true mirror where slot asymmetries cancel. **C3 is noise, not amplifier evidence.** I removed it from the amplifier's support.
- **A confirmed defect with a possibly-backwards causal story:** `Unit._agg` staleness is real, but the "healthy-forever" narrative is an artifact of a test that bypassed erosion; live, it may bias toward *earlier* rout. Fix the code, distrust the story.
- **The single biggest thing nobody found:** the root line of the Arrowhead side-asymmetry (#3). It is a *dominant* cause of H2 and a confidence-contaminant for every cavalry row, and it remains a black box narrowed to "somewhere in the dynamic movement/charge-shock path." Treat H2 (and any C-row pass) as provisional until this is traced.
- **A calibration trap that could make things look worse before better:** fixing #1 or #2 in isolation risks knocking the currently-passing C4/C7 (and possibly C5) out of their near-total bands, because they may be passing partly on the same density inflation ([CALIBRATED-DEBT], anti-fabrication flag: I cannot independently confirm they'd stay in-band post-fix). The pass count is not monotonic in the number of fixes applied.
- **Count-level sloppiness, disclosed:** the architecture surface's "~20 troop_type sites / ~46 eff_* sites" were ~30% inflated (critic: 15 / 37). Qualitative claims hold; don't cite the magnitudes.

**Net:** the mechanistic and file:line findings across all seven surfaces held up unusually well under adversarial re-verification — nearly every citation and reproduced number was exact. What did *not* survive was a subset of *severity/causal* framings (morale as driver, sibling-pull as H4 cause, the amplifier's "modest edge" story, the granularity toy-model's ~1pp null). The engine is genuinely more correct than "7/20" suggests — ~2 of the 13 fails are instrument noise, and R3 is a scenario no historical band may even intend the engine to resolve — but the ~11 real divergences are driven by concrete, largely-fixable mechanisms, gated behind one deep architectural ruling (DG-A) that no amount of constant-tuning will resolve.