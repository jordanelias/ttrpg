# Personal Combat — Adversarial Critique + NERS Audit (Consolidated Master)
**2026-06-23 · scope: `combat_engine_v1` (every module/mechanic/contributor) · status: PROPOSED working master**

`[SELF-AUTHORED — bias risk: the engine, the prior audit, and this critique are all Claude-authored. Every finding was produced bottom-up from the code, buttressed top-down by a cited precedent (game / historical manual / physics), and then independently ADVERSARIALLY VERIFIED by a separate agent (code-accuracy + precedent-accuracy + emergent-fidelity). Verify status is recorded per finding; do not trust an unverified row.]`

**Method (binding paradigm, applied at every step):** each component was critiqued **bottom-up** from its granular primitives (the formula, the weapon vector, the per-beat transition), then **validated top-down** against real-world precedent — acclaimed melee games, HEMA/koryū manuals, and physics. A proposed fix is only accepted if it **emerges from the existing primitives** rather than imposing a scripted/top-down rule; "bolt-on" fixes are flagged. Quantitative claims are Monte-Carlo or arithmetic, run against the live engine.

**Coverage:** 10 component clusters → **45 findings (9 critical · 19 high · 14 medium · 3 low)**. Adversarial verification: **33 confirmed · 8 revise · 4 unverified**.

---

## §1 — NERS VERDICT (rolling-engine resolution diagnostic)

Applied the `valoria-resolution-diagnostic` methodology. **In scope (the rolling engine):** `core.resolve` — the single sigma-leverage mu-shift draw (`net = roll_net_continuous(pool,TN7) + soft_cap(net_sigma)·sigma_n(pool)`, graded at fixed `DECISIVE_OB=3`, pool `max(5,History+6)`). **Instance A.** Recognize-and-excluded: the state-machine sequencing, the continuous resources (stamina/conc/poise/Vor/Health) as roll *inputs*, the damage ledger, weapon vectors → these route to the mechanic-audit / this critique, not the roll-property verdict.

| Property | Verdict | Note |
|---|---|---|
| **P-i** legible odds | partial | leverage axes readable, but the *rendered probability* is mis-stated (no continuity correction) |
| **P-ii** uniform leverage | **pass** | z-shift per `net_sigma` is pool-independent (0.248 at 5/9/13D) — the F1 fix holds; no flat-`+X` trap |
| **P-iii** bounded+monotonic | partial | monotone, soft-cap smooth, Ob-floor structurally avoided — but the ER-2 continuity term is **absent** |
| **P-iv** graded recoverable | **pass** | 4-degree ladder, `UPSET_FLOOR=0.05` underdog floor, smooth Overwhelming tail |
| **P-v** right engine | **pass** | 5–13D healthy pool + real setup axis → Instance A correctly selected |

**N: pass** · **E: pass** (one blemish) · **R: FAIL** · **S: FAIL** → **VERDICT: compliant-with-residuals.**

> **The single NERS-breaking defect (P2):** the **ER-2 continuity correction is in canon/spec but NOT in the engine code.** `core.degree`/`r1.degree_of_success` resolve continuous `net ≥ Ob`, while canon (`params/core.md §Continuous Engine`, "landed" 2026-06-22 `a3d3888`) and `engine_replacement_reconciled §2/§5` mandate `net ≥ Ob − 0.5`. Verified divergence across the **whole 5–13D band** (not a sub-5D edge case, because `Ob=3` sits high on these CDFs): P(success) runs **−5 to −9 pp** below the discrete/TTRPG odds (5D `0.288` vs `0.381`; 8D `0.535` vs `0.615`). The videogame engine disagrees with discrete mode *and with its own canon* on the same action's odds → **breaks R and S.** Fix: compare `net` against `Ob−0.5` (Success), `2·Ob−0.5` (Overwhelming bar), `>0.5` (Partial/Failure) — one constant per boundary; re-run the stress harness to confirm attacker odds rise ~5–9 pp at the low band. The commit `a3d3888` landed the correction in *text* but never propagated it into *code*.

Residual P3: the engine isn't repo-runnable (`/home/claude` hardcoded `sys.path`); and the out-of-roll-scope consistency defects (armor-defeat non-monotonicity, dead `DAMAGE_SCALE`, `wt` re-init, dead `seize` lever) route to the mechanic-audit.

---

## §2 — CROSS-CUTTING PATTERNS (the synthesis)

The 45 findings collapse into **five recurring defect classes** — naming them is more useful than the long list, because each fix-pattern clears several findings:

1. **Built-then-unwired substrate ("dead emergent primitives").** Whole subsystems are authored and then read by *zero* live sites: `grappling.py` (the entire clinch/throw/reach-inversion model), the `clinch` weapon rating, four of five `geometry.bake` outputs (`thrust`/`cut`/`perc_conc`/`halfsword`), the `seize` lever (`vorschlag`/`sen_no_sen`), `pool_penalty()`, `REACH_ADV_K`/`RESIDUAL_REACH_FRAC`, `DAMAGE_SCALE`/`CAP_END`. The engine repeatedly builds the right bottom-up primitive and then fails to consume it — so the emergent behaviour the substrate *could* produce never appears. **This is the dominant pattern (≥10 findings).**

2. **Sequenced-out-of-its-own-exchange.** The load-bearing tempo mechanic, **Indes**, mutates initiative *after* `net_sigma` is already baked, so the "in-the-moment" theft of the Vor has zero effect on the exchange it is stolen during (it's actually *go-no-sen*, after-the-fact). Same class: `disrupt_focus`/`sim` is **unreachable dead code** (the outcome map forces `hit` and `riposte` mutually exclusive), so Focus's combat role never executes — the bottom-up cause of Focus being the weakest attribute.

3. **Wrong-axis / sign-asymmetric application.** A competence weight multiplies a *signed* differential, so it *amplifies a deficit*: `bind_sigma` makes a German's *losing* bind 30% worse; the tempo bracket makes a slow fighter's initiative deficit deeper. And OOB is applied aggressor-only as a σ-shift while canon (and the ED-1041 wound fix) says impairment must be **bilateral** on the Ob axis.

4. **Inverted / non-monotonic physics.** `ADEF_THRESHOLD` makes **mail easier to defeat than padding** (medium 0.45 < light 0.70) — physically backwards and against the repo's own ACOUP/Williams sources. The wound model's death-spiral slope goes to **zero** in the terminal pre-felling zone (impairment plateaus while damage still accrues) — incapacitation curvature backwards vs Sekiro/forensics.

5. **Mass is invisible to the cut.** A swung weapon's cut energy ∝ moment-of-inertia, but `heft` for every non-blunt head is a binary `{light:0, heavy:3}` flag and `cut_factor` ignores mass entirely — a 0.9 kg sabre and 2.7 kg greatsword are indistinguishable on the cut. The `cut` coefficient that would fix this is **already baked by `geometry.py` and thrown away** (pattern 1).

**Reconciliation insight:** the stress matrix's three "inert" components are now mechanistically explained — `oob` is **unreachable** (stamina floors at ~12/20, never hits 0), `disrupt_focus` is **dead-code-unreachable** (`sim` is never True), and `push_shove` is **pre-empted** (reach already decides the fight before re-opening can matter). And the stress-matrix `leverage` sign anomaly (×1.5 → −10) is root-caused to **two real defects**: `leverage()` is a length-independent grip *fraction* (a dagger out-levers a longsword) and `bind_sigma` amplifies deficits (pattern 3). The bottom-up critique and the top-down empirical sweep agree.

---

## §3 — FINDINGS LEDGER (severity-sorted; V = verify status ✓confirmed / ~revise / ?unverified)

### CRITICAL (9)
| # | Component | Defect (bottom-up) | Top-down validator | Emergent fix | V |
|---|---|---|---|---|---|
| C1 | `core.resolve`/`degree` | **ER-2 continuity correction missing** — resolves `net≥Ob`, canon says `net≥Ob−0.5`; −5..−9pp across 5–13D | Normal-approx continuity (Wikipedia/PSU 414); the engine's own commit `a3d3888` | compare against `Ob−0.5` per boundary | ✓ |
| C2 | `armor_defeat_sigma` | **`ADEF_THRESHOLD` non-monotonic** (medium 0.45 < light 0.70) → mail easier than padding | ACOUP/Williams: penetration energy rises none<cloth<mail<plate | derive threshold from the monotone `RESIST[mat]['puncture']` table | ✓ |
| C3 | `reach_sigma` | **standing reach tax ignores measure-state** — dagger inside a spear still eats +1.35σ every beat → reach r=0.83 over-flat | M&B II (polearm useless in clinch); Italian misura stretta inverts reach | pass `measure_gap`; scale gap term by `m=measure_gap/REACH_FULL_GAP`; invert toward `clinch` at the close | ✓ |
| C4 | OOB stamina cliff | **unreachable** — drain≪recovery, stamina floors ~12/20; the endgame lever never fires | DS/KCD: the empty-bar cliff IS the central risk lever (regen paused) | re-tune cost/recovery so realized fatigue spans the axis; recovery only on clean disengage; couple to wounds | ✓ |
| C5 | Indes / single-time counter | **sequenced after `net_sigma`** → in-tempo Vor theft has zero effect on its own exchange (go-no-sen, not sen) | Liechtenauer Indes "on contact, same tempo"; koryū sen-no-sen; For Honor counters resolve in-window | move the steal above `net_sigma`, or let read-margin feed a defender σ in-line | ✓ |
| C6 | `grappling.py` / clinch | **entire grapple substrate orphaned** — built (throw/control/dagger-finish/reach-inversion), imported nowhere live | Fiore abrazare = foundation; Williams 3rd plate-counter = wrestle-then-rondel | wire at the displace-inside site, feeding existing poise/wound channels | ✓ |
| C7 | cut damage / `cut_factor` | **mass/MoI invisible to the cut** — 0.9kg sabre = 2.7kg greatsword on heft | HEMA sword dynamics (MoI = effective mass in rotation); M&B momentum-bonus; KE=½Iω² | bake `cut_heft ∝ √mass·f(pob)` into `geometry`, feed `damage` like `p_auth` feeds blunt | ✓ |
| C8 | `leverage`/`bind_sigma` | **Stärke-Schwäche has no blade-contact-point** — `leverage` is a frozen grip:head ratio; no forte/foible, no Winden | Liechtenauer "meet strong with weak"; torque = F×(contact-to-hand) | derive `contact_frac` from reach diff + commit; bind term = forte-fraction-at-contact difference | ~ |
| C9 | outcome-map / `disrupt_focus` | **`sim` is unreachable** → Focus's disruption-resistance is dead code (cause of Focus = weakest attribute) | Sekiro simultaneous-strike trade window; German Indes "within a sustained note" | un-exclude `hit`+`riposte` on the trade; let Focus(`DISRUPT_K`) decide the through-trade | ? |

### HIGH (19, condensed)
- **H1 continuity scoping claim** ("negligible >5D") is empirically false for the combat band (−5..−9pp at 5–13D) ✓ · **H2 "uniform leverage"** is true only at p=0.5; at fixed Ob=3 the same +0.5σ gives +18pp@5D vs +8pp@16D (2.2×) — the self-test masks it ✓
- **H3 Impact = Str + binary Heft** → near-one-shot tail, mass invisible (port the MoI authority) ~ · **H4 clinch dead primitive** (data present, zero reads) ✓ · **H5 approach-close tempo reset** gives the closer risk without reward (symmetric `ready=0`) ✓
- **H6 free defence** — stamina debited only for the aggressor's strike; parry/dodge/wind/riposte/bind all free → no "who gasses first" ✓ · **H7 disposition Vor drift** is a *standing* ±0.4 fixed-point bias (temperament ≠ initiative-state) ✓ · **H8 Indes→counter tier-collapse** — read forces the counter, can't choose bind/displace ~
- **H9 seize lever fully dead** — `vorschlag`/`sen_no_sen` (the two best-anchored traditions' signatures) are no-ops; doc says "live" ✓ · **H10 geometry bake 80% unconsumed** (`thrust`/`cut`/`perc_conc`/`halfsword` thrown away) ✓ · **H11 armor_defeat non-monotonic, now ×geometry-gap** (calibration stale) ✓
- **H12 leverage() length-independent** (dagger out-levers longsword) ✓ · **H13 bind_sigma signed×weight** amplifies a losing bind ✓ · **H14 pool_penalty dead** (−1D/wound canon severed from resolution) ✓ · **H15 wt re-init drops spirit/strength** (Health 57→50; corrupts multi-bout sims) ✓ · **H16 wound terminal plateau** (death-spiral slope→0 before felling) ✓
- **H17 half-sword form state-leak** — 88% of approaches start stuck in the carried-over short form ? · **H18 OOB unreachable** (state-graph view) ~ · **H19 tempo-bracket signed×weight** punishes the deficit case ✓

### MEDIUM (14) / LOW (3) — headlines
- M: stop-hit has no head gate (a blunt staff "stop-hits" like a spear point) ~ · reach-reopen+push_shove vestigial under reach dominance ✓ · parry degenerates out of the mode set (calibration: dodge always wins) ~ · mental fatigue penalises only the defender's read ✓ · OOB wrong-axis (aggressor-σ vs canonical bilateral pool/Ob) ✓ · single-time-counter steal non-conservative across the cap ✓ · linear fatigue curve (real PCr decline is convex) ✓ · undifferentiated scalar damage (no locality/wound-type; m9 decisive channel dropped) ~ · bilateral wound-Ob magnitude uncalibrated (~10–15pp/wound vs ~5pp target) ✓ · `pob_frac` physically incoherent (staff 0.05) — a reverse-fit percussion knob ✓ · tradition channel-ability docstrings mislabel live abilities as "pending" ? · dead `DAMAGE_SCALE`/`CAP_END` ✓ · engine not repo-runnable (`/home/claude` paths) + `_engine` fork drift ?
- L: dead `REACH_ADV_K`/`RESIDUAL_REACH_FRAC` ✓ · `hand_guard` rewards the guard but never strikes the bare hand ~ · superset assert-guards don't enforce the equality invariant they document ✓

*(Full per-finding critique/precedent/fix/verify text retained in the workflow output; this ledger is the navigable index.)*

---

## §4 — RECONCILIATION WITH PRIOR FINDINGS

Every prior-session finding is **re-confirmed and sharpened** by an independent agent here, and several are *root-caused*:
- **armor_defeat non-monotonic** (C2): confirmed exact; *new* — the Godot port (`combat_config.gd:53-58`) already fixed it to monotone `0.45/0.60/0.72`, so the canonical engine should adopt the port's values.
- **wt re-init bug** (H15): confirmed; magnitude updated to 57→50 (the register's 46→40 predates the 2026-06-18 D-A constant change) — same defect, live.
- **dead `DAMAGE_SCALE`** (M): confirmed empirically (`damage(scale=4.0)==damage(scale=999)`).
- **seize lever dead** (H9): confirmed; the casualties are specifically the German Vorschlag and Japanese Sen-no-sen.
- **stress-matrix "inert" trio**: mechanistically explained (C4/C9 + push_shove pre-emption) — *not* a panel artifact for `oob`/`disrupt_focus` (genuinely unreachable), *is* pre-emption for `push_shove`.
- **stress-matrix `leverage` sign anomaly**: root-caused to H12 + H13.
- **reach dominance r=0.83**: root-caused to C3 (standing tax) + H4 (dead clinch).
- **bilateral-Ob wounds (ED-1041)**: confirmed live and correct in form, but the magnitude (M) is uncalibrated and `pool_penalty` (H14) is the dead canonical counterpart.

---

## §5 — PRIORITIZED ROADMAP (emergent fixes, worst-first)

1. **C1 — wire the ER-2 continuity correction into `core.degree`/`r1.degree_of_success`.** One line per boundary; closes the only NERS-breaking defect (R+S), aligns engine↔canon↔discrete. Re-run the stress harness.
2. **C3 + H4 — make reach measure-relative.** Pass `measure_gap` into `reach_sigma`; decay the standing edge toward `RESIDUAL_REACH_FRAC` (a *dead knob revived*) and invert via the dead `clinch` rating at the close. Fixes over-flat reach AND revives push_shove/reopen value (no buffing needed).
3. **C2 — adopt the port's monotone `ADEF_THRESHOLD`** (or derive from `RESIST`); re-run r8 parity.
4. **C5 + C9 + H8 — re-sequence Indes** (steal before `net_sigma`; let the read fork among counter/bind/displace) and **un-exclude the simultaneous trade** so Focus(`DISRUPT_K`) becomes live.
5. **C7 + H10 — consume the already-baked `geo['cut']`** as continuous cut-heft (fixes "mass invisible" for free); route `geo['thrust']`/`perc_conc`/`halfsword` to their natural consumers.
6. **C4 + H6 + H18 — re-tune stamina** so OOB is reachable; charge a (smaller) defensive cost; couple `stamina_max` to wounds.
7. **C6 + C8 + H12/H13 — wire the grapple/clinch substrate** and re-derive `leverage` from absolute geometry + a bind contact-point.
8. **Cleanups (P3):** repo-relative `sys.path` (delete the `_engine` fork); fix `wt` re-init signature; delete dead `DAMAGE_SCALE`/`CAP_END`/`REACH_ADV_K`; re-home or retire `seize`/`vorschlag`/`sen_no_sen`; fix the mislabelled "pending" channel-ability docstrings; tighten the assert-guards.

Every fix above is sourced from a **primitive the engine already has** — none imposes a top-down scripted outcome.

---

## §6 — HONESTY BLOCK

`[VERIFY GAPS: 4 findings are unverified (C9 disrupt_focus, H17 half-sword leak, the sys.path/_engine finding, and the tradition-docstring finding) — the verifier output did not cover them; the critiques are code-grounded and several restate already-independently-confirmed prior findings, but treat the "?" rows as un-cross-checked. 8 "revise" findings carry a correction in the workflow output (e.g. H3's one-shot example is mis-attributed to the HEFT flag for blunt heads; the stop-hit precedent is slightly overstated; H8 overstates that the read "can't" bind — bind is set independently, just not by the read).]`
`[NULL: P-ii uniform-leverage genuinely PASSES — the engine correctly avoids the flat-`+X` trap; that strength survived adversarial attack.]`
`[CONFIDENCE: high on the 33 confirmed code-level findings (each re-derived against file:line + arithmetic/MC); medium on the design-judgement of the proposed fixes (form grounded, numbers are Jordan's to tune); the NERS verdict is high-confidence (the ER-2 divergence is reproduced quantitatively and is the engine's own canon).]`

*Source of truth: `combat_engine_v1` @ live HEAD + `tests/sim/v32-combat-balance/`. This consolidates the 2026-06-23 adversarial-critique + NERS workflow (21 agents), reconciled with the 2026-06-22 audit and the combat-stress-matrix.*
