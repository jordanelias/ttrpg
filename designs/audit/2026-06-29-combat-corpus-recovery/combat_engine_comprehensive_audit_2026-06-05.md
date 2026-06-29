# Valoria Combat Engine — Comprehensive Audit
**2026-06-05 · granularity / bottom-up · architecture · mechanic importance (empirical)**

`[SELF-AUTHORED — bias risk]` — I built much of this engine (the sigma architecture, the initiative layer); audited here as an outsider, with the empirical ablation as the discriminator so the verdict isn't my prior.

---

## VERDICT
**Architecturally sound and genuinely modular, but materially over-atomized.** Bout outcomes are carried by a load-bearing core of ~25–30 constants; **~22% of the 143-constant tuning surface (31 constants) moves <0.5% of outcomes**, and several named subsystems are inert or untested in play. Bottom-up grounding is strong in the spine (resolution math, damage, tempo, reach) and weak in the periphery, where TTRPG-era apparatus and skill-scaling sub-terms were added by analogy without an empirical check that they register. The win-rate harness is **blind to the initiative-seizure mechanic** (it randomizes the first mover), so part of the apparatus is *untested*, not proven dead — a finding about the test rig as much as the engine.

## 1. Method
Empirical ablation: zero each of the 143 scalar `CFG` constants, re-run a fixed 8-matchup, paired-seed bout set (60 seeds × 8 = **480 bouts/config**), measure the fraction of bouts whose outcome (A-win / draw / B-win) changes. **Impact = 2 × (flip fraction)**; 0 = no effect, ~2 = total. Matchups span weapon (longsword/rapier, mace/sabre, spear/dagger), attribute (str vs agi, focus vs disp), armour, and tradition contrasts, plus a mirror. Architecture/granularity from full engine reads this session. **Caveat (load-bearing):** impact is measured *on this matchup set* — a near-zero result means "no effect in these conditions," which per finding is one of: structurally dormant, harness-bypassed, trigger-frequency, or genuinely below the noise floor.

## 2. Granularity / degree of bottom-up
- **Spine — bottom-up.** The resolver (`Normal(μ·N, σ·√N)` from the dice model), the damage coupling, tempo, and reach are derived, not asserted. The sigma-leverage architecture is principled.
- **Physical layer — now bottom-up (data only).** Weapon mass/PoB/composite from sourced specimens (this session, committed `e414098`); the consuming physics is staged.
- **Periphery — pattern-extended.** The over-atomization (§5 P3) is the tell: coarse mechanics are load-bearing, but finer skill/attribute-scaling terms layered on by analogy ("History should scale initiative," "training should scale counters") sit below the noise floor. The engine is first-principles in its trunk and extrapolated at its twigs.

## 3. Architecture / modularity / data structure / code / ability
- **Modularity: strong.** Clean split — `wrapper` (state graph) · `systems` (S.* mechanics) · `core` (resolver + damage) · `combatant` (data) · `config` (CFG) · `geometry` (build-time bake) · `tradition`; leaf primitives (r1/r5/r2/m1) factored. **`cfg` is threaded as a parameter** — the engine's best feature; it made this audit possible (ablation by `cfg` override).
- **Data structure: mostly clean, real smells.** WEAPONS/ARMOR/TRADITION as data-driven axis-vector dicts — good. But **`CFG` is a flat 153-key dict with no subsystem grouping and no impact signal** — nothing structurally distinguishes the 25 load-bearing knobs from the 31 ornamental ones, which is *how* the atomization accumulated invisibly (§5 P6). Dead field: `Combatant.pool` (set, never read).
- **Code: solid, some dead weight.** Compiles; resolver and state graph readable. Dead/unread: baked `geo.{cut,thrust,perc_conc}` (computed every build, never consumed), the legacy `resolve_phrase` path (not live), the dormant grip levers.
- **Ability (capability).** *Apparent* capability is broad — multi-weapon, multi-tradition, multi-mode resolution, wounds/stamina/concentration/poise/initiative/bind/counter/feint. *Effective* (outcome-affecting) capability is the load-bearing core; the gap between the two **is** the inert apparatus (§5). The system can represent more than it currently *uses*.

## 4. Mechanic importance — empirical (the core)
Impact distribution across 143 scalars: **1 dominant** (`DAMAGE_SCALE` 1.93) · **13 high** (.15–.5) · **52 moderate** (.05–.15) · **30 small** (.02–.05) · **47 near-ornamental** (<.02), of which **31 are <0.01 and 28 are <0.005**.

- **Load-bearing core (drives outcomes):** `DAMAGE_SCALE`; the tempo/burst/close system (`BURST_MAX` .40, `CLOSE_TEMPO_COMPRESS` .35, `BASE_TEMPO`, `MAX_TEMPO_PEN` .18); `STOPHIT_CHANCE` .37; `RECOVERY_FRAC` .24; reach (`LONG` .22 / `HEADR` / `REACH_FRAC` .18); `ADEF_POINT` .20, `NEUTRALIZE_OVERWHELM_DROP` .19, `NEUTRALIZE_DODGE` .13; `WEIGHT_PEN` .18 (weapon weight); `CAP_END` .17 (the no-one-shot cap — confirmed load-bearing); `COUNTER_SUCCESS_BASE`/`COUNTER_SELECT_BASE`, `FEINT_P`/`FEINT_MAX_STREAK`; `ATTACKER_BIAS` .11; `REFLEX_AGI` .11.
- **Ornamental — "would not matter if removed" (impact <0.01):** see §5 P1–P4 for the grouped findings and their *distinct causes*.

## 5. Critical findings (adversarial, severity-ranked)
**P1 — the initiative-SEIZURE layer is untested by the harness (not proven dead).** All seizure constants (`INIT_SEIZE_K/READ/REACH/CONC`, `INIT_HISTORY_K`, `INIT_READING_K`, `INIT_LOSS_OVERCOMMIT`) ≈ 0. **Cause:** `fight()` assigns the first mover *randomly*, bypassing the seizure→first-mover path; the `init_edge`→`net_sigma` path (`INIT_SIGMA_K` .08) *does* register. Two consequences: (a) **every win-rate tuning done through this harness is blind to seizure** — a real test-rig gap; (b) whether the layer matters depends on the *game* using seizure for first-mover. **Action:** confirm how first-mover is set in the intended game; re-test with seizure-determined first; then wire it to register or cut it. (This is exactly the finding I was biased to miss.)
**P2 — OOB (out-of-breath) is inert in tested play.** Impact 0. **Cause:** feeds `net_sigma` directly (not first-mover), so this is *trigger-frequency* — stamina likely never reaches 0 in decision-length bouts. **Action:** verify in an attrition matchup; if it should bite, give it teeth (the −2D pool form) or a reachable trigger; else cut. (Confirms finding B empirically.)
**P3 — over-atomization: ~22% ornamental tuning surface.** 31 constants change <0.5% of outcomes. **Cause:** genuine below-noise net_sigma sub-terms — skill/attribute fine-scaling layered on load-bearing bases (`COUNTER_TRAIN_K` on counters, `BIND_TECH_K`/`BIND_STR_K` on bind, `DISP_INIT_K`/`DISP_COMMIT_K` on disposition, `HANDS_COMMIT`, `LEVER_REF`, `REACH_ADV_K`, `RESIDUAL_REACH_FRAC`, `TEMPO_FLOOR`, `PUSH_*`). NERS-E fail: overhead the player cannot perceive. **Action:** calibrate to register, or prune.
**P4 — concentration influence is ~nil today.** `DISRUPT_K` 0, `CONC_BASE_K`/`INIT_SEIZE_CONC` 0. Concentration barely touches outcomes (its initiative feed is in the bypassed seizure path; its disruption-resistance never fires). **This validates building the planned error-onset model** — but flags that the *current* concentration apparatus is ornamental.
**P5 — structurally dormant grip levers.** `CHOKE_TEMPO_PEN`, `LUNGE_TEMPO_PEN`, `CHOKE_BIND_K`, `LEGIB_LUNGE` = 0. **Cause:** grip never switches off 'normal' (genuine dormancy, not harness). Already slated to wake in the weapon-physics build.
**P6 — `CFG` is a flat 153-knob dict with no structure or impact signal.** The architectural smell that let P3 accumulate invisibly; group by subsystem and annotate load-bearing vs tuning.
**Note on "crashes when zeroed" (`INIT_SCALE`, `INIT_SEIZE_SCALE`, `POISE_SOLID_HIT`, `STAMINA_REF`, `STOPHIT_FULL_GAP`):** these are divisors the formula needs non-zero — *not* evidence of importance (`INIT_SEIZE_SCALE` is the divisor of the untested seizure layer).

## 6. Genuinely sound (evidence-grounded, not balance)
The `cfg`-as-parameter design (testability); the load-bearing core is *the right things* (damage, tempo, reach, the cap, counters, neutralize); data-driven axis-vectors; `CAP_END` confirmed load-bearing (no-one-shot holds); modular separation that let a 143-constant sweep run in 64 s.

## 7. Coverage / confidence
- **Ablated:** all 143 scalar `CFG` constants (paired-seed, 8 matchups, 480 bouts/config). **Not ablated:** dict-valued constants (`RESIST`/`QUAL`/`DELIVERY`/`HEAD_REACH` — structural), the wound penalty (lives in `r2`, not CFG; validated separately this session — draw 2.8→7.1%), and the attribute/skill/tradition *data* layers (only their CFG levers).
- **Caveats:** impact is on the tested matchup set; P1 is harness-bypassed, P2/P4 are trigger-frequency, P3 is genuine-below-noise, P5 is structural-dormant — distinct causes, distinct remedies.
- `[CONFIDENCE: high on the load-bearing core and the ornamental set (28 constants at <0.005); high on P1's harness-bypass (the random first-mover is in the source); medium on P2/P4 being intrinsically dead vs trigger-frequency — verify in attrition; architecture eval grounded in this session's full reads.]`
