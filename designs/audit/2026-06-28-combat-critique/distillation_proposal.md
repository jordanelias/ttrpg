<!-- STATUS: AUDIT — analytic instrument output, not canon. -->
# Combat Engine v1 — Distillation Proposal
**Date:** 2026-06-28 · **Source:** wf_1fd6d183-bde (11 modules, resolution diagnostic, 5 corpora, 30 adversarial verdicts)

## Headline

The engine's resolution spine is proven sound: mu-shift sigma_N-scaled leverage is pool-uniform by construction (validated +25.8pp flat across pools 3-20), the global soft_cap (1.5*tanh) bounds the entire additive lever pile in-band, ER-2 continuity is correct in core.degree() for the [5,13]D band, and every feedback loop (Vor, poise, bind, burst, outer) is both damped (<1) and hard-capped. The dominant debt pattern is not architectural failure but dead data and orphan emissions — mechanics that are computed, stored, or documented as live but produce zero churn. The three highest-leverage moves are: (1) kill the dead 'seize' lever and its two flagship abilities (vorschlag, sen_no_sen) that silently do nothing, repairing the doc that falsely claims they are live; (2) unify the two competing percussion sources (p_auth vs hand-set w['percussion']) into one physics model, wiring the dead baked geo perc_conc coefficient in the same pass; (3) propagate the balance channel weight to all five balance_eff call sites so Spanish/Filipino tradition identity is not 80% suppressed.

## CUT (dead data / inert levers / resolved findings — remove from codebase)

**config.py:**
- `REACH_ADV_K=0.12` — defined, never consumed anywhere (sibling REACH_DISADV_K is live). Dead config.
- `RESIDUAL_REACH_FRAC=0.3` — defined, zero consumers in entire repo. Dead config.
- `CONC_BASE_K=4.0` — defined, no consumer anywhere in the engine. Dead config.

**combatant.py:**
- `clinch` field on all 12 weapon dicts (lines 14-27) — stored, never read by any module. Remove until a grapple mechanic exists to consume it.
- `WEAPONS[w]['geo']` sub-keys `thrust`, `cut`, `halfsword` — baked at import by geometry.bake(), stored in the geo dict, never read downstream. Only `gap` is consumed. Remove these three from bake() output and the stored dict. (Retain `perc_conc` only if WP-1/WP-3 consolidation proceeds — see CONSOLIDATE.)

**core.py:**
- `QUAL['partial']=0.5` — defined but unreachable (damage() returns 0 for deg not in graze/success/overwhelming; wrapper never sends deg='partial'). Remove or comment as deferred.
- `close` parameter in damage() (6th positional) — accepted, never read inside the function body. Remove from signature and all call sites.
- `p_auth()` computed for non-blunt weapons — strike() always calls p_auth() but damage() ignores perc for non-blunt heads. Guard the call: only compute for blunt.

**tradition.py:**
- Comment at lines 89-90 claiming channel levers are "INERT pending eff_cw routing (~21 sites)" — **false**: all 7 channels have live eff_cw call sites. This dead documentation blocks ability deployment on a false prerequisite. Update to reflect wired status.

**ability_armature.md:**
- §7 and §2c: remove 'seize' from the 'Live levers' list. Mark vorschlag and sen_no_sen as 'registered, consumer cut 2026-06-05, reroute pending'. The doc currently asserts the exact opposite of the code.
- §2c/§7: mark staerke_schwaeche, misura, atajo as 'registered and reachable (channel wired); calibrate value before deploying' — not 'pending channel wiring'.

**combat_engine_flow_and_state_map.md:**
- §4A A5: remove DAMAGE_SCALE=4.0 and CAP_END=4 (deleted from config per commit 793f1a62). Note DMG_SCALE=1.55 is now an inline constant in core.py:51.
- §A3: update to note precommit IS consumed in feint_eval (systems.py:203), not zero sites.
- Add a last-verified date/SHA stamp to the header.

**RESOLVED (already fixed — do not include in work plan):**
- ~~W-01 (sandbox /home/claude imports)~~ — fixed by commit 0846b5be; __file__-relative imports now used.
- ~~W-02 (WoundTracker reset losing spirit/strength)~~ — fixed by commit a07bafae.
- ~~DA-10 (extreme one-shot risk)~~ — adversarial verdict: real=false; linear model deliberately ratified 2026-06-17.
- ~~CD-1 (OOB binary cliff)~~ — adversarial verdict: real=false; graded degradation already present.
- ~~RF-01 (feint_streak accumulation bug)~~ — adversarial verdict: real=false (P1->P3 demote; no loop-break).

## CONSOLIDATE (two-into-one merges that reduce lever count without losing churn)

**1. Unify percussion sources (WP-1 + WP-3 partial)**
- BEFORE: blunt damage heft reads `core.p_auth(mass, pob_frac)` (derived from weapon dynamics); blunt armour-defeat reads hand-set `w['percussion']` (legacy integer). Two physics models for one physical quantity. 2 input channels, 2 independent calibration surfaces.
- AFTER: route `systems.armor_defeat_sigma` (systems.py:124) through `core.p_auth(aggressor.w)/8.0` instead of `aggressor.w.get('percussion',8)/8.0`. Multiply by baked `geo['perc_conc']` so war-pick (perc_conc=0.93) out-defeats flat mace (perc_conc=0.75). Remove hand-set `percussion` field from all WEAPONS dicts once validated. 1 input channel, 1 calibration surface.
- LEVER COUNT: 13 weapon fields -> 12 (percussion removed); 1 dead baked coeff (perc_conc) -> live.
- NERS: N+ (one quantity, one owner), S+ (damage-heft and armour-defeat move together monotonically).
- GATE: requires mirror=50 + armour-tier re-sweep before commit. Do WP-1 and perc_conc wiring together or not at all.

**2. Seize lever retirement (or reroute)**
- BEFORE: 2 ABILITIES entries (vorschlag, sen_no_sen) targeting lever='seize'; 0 consumers; 3 doc sites falsely claiming 'live'. The German and Japanese flagship abilities produce zero mechanical effect.
- AFTER (option A — retire): remove both abilities from ABILITIES dict or mark explicitly as '(cut 2026-06-05; pending replacement)'. Fix tradition.py:87 comment, ability_armature.md §2c and §7. 0 dead entries, 0 false doc claims.
- AFTER (option B — reroute): re-point both abilities at a surviving initiative lever (e.g. additive bonus to init_steal_factor, or a bounded one-time initiative grant at engagement start). Must clear an ablation bar showing non-zero outcome impact, since the original pre-contact seizure was cut for empirically washing out.
- LEVER COUNT: 2 dead abilities -> 0 (option A) or 2 live (option B).
- NERS: N+ (dead lever removed), E+ (doc matches code).
- RECOMMENDATION: option A (retire) is the disciplined default. Option B only if a NEW consumer (not the cut pre-contact contest) is designed AND simmed to non-zero impact.

**3. Balance channel propagation**
- BEFORE: `TR.eff_cw(c, 'balance')` applied at 1 of 5 balance_eff call sites (only reach_sigma foot_meas). Spanish destreza (balance=1.30) and Filipino compas (balance=1.25) tradition advantage is ~80% suppressed at dodge, anti_overcommit, stance_stability, close_rate, reopen_prob.
- AFTER: apply `TR.eff_cw(c, 'balance')` inside balance_eff() itself (systems.py:65-69) so all downstream consumers inherit it uniformly.
- LEVER COUNT: unchanged (no new lever; existing lever made coherent).
- NERS: S+ (balance channel consistently represents the competence it names across all phases), R+ (tradition identity no longer phase-inconsistent).

**4. Hardcoded normalization constant**
- BEFORE: reopen_prob (systems.py:224) hardcodes `/0.62` as normalization divisor, duplicating `cfg['REACH_W']['none']`.
- AFTER: replace with `/cfg['REACH_W']['none']`.
- LEVER COUNT: unchanged.
- NERS: R+ (robust to config retuning).

## KEEP CORE (the minimal NERS-clean load-bearing set — DO NOT TOUCH)

**Resolution spine (NERS RRRR — the engine's strongest property):**
- `core.resolve()`: `roll_net(pool, rng) + soft_cap(net_sigma) * sigma_n(pool)` — mu-shift sigma_N-scaled leverage, pool-uniform by construction.
- `m1.sigma_n()`: `0.8 * sqrt(pool)` — the sqrt(N) that makes leverage uniform.
- `m1.soft_cap()`: `1.5 * tanh(x/1.5)` — global ceiling bounds the entire lever pile to +/-1.5 sigma_N.
- `core.degree()` with ER-2 continuity: `k-0.5` thresholds for the 4-band degree ladder.
- `resolution_pool(history)`: `max(5, history+6)` — pool in [5,13], the band ER-2 was calibrated for.

**Damage chain (NERS clean at the formula level):**
- `Impact x Coupling x Quality x DMG_SCALE` — legible, minimal, correct.
- `p_auth(mass, pob_frac)` for blunt heft — continuous, physics-derived.
- `OW quality tail`: `q = 1.5 + (OW_MAX-1.5) * tanh(z/OW_Z)` — tanh-bounded severity linking roll margin to wound magnitude.
- WoundTracker: bilateral Ob wounds (WOUND_DEF_OB, WOUND_ATK_OB) degrade via net_sigma, NOT pool reduction — wounded fighters never drop into a fragile sub-5D regime.

**Feedback loops (all pass damper<1 AND cap):**
- Vor/initiative: INIT_DECAY=0.75 (geometric damper) + INIT_CAP=1.5 (hard clamp) + tanh sigma conversion.
- Poise/kuzushi: recovery toward 1.0 with POISE_FLOOR=0.5.
- Bind: fixed 3-iteration ceiling.
- Burst: BURST_MAX=4 + clean-resolve exit.
- Outer engagement: beats strictly monotonic, ceiling soft*3=24, stamina abort, fell/separation exits.

**Tradition substrate (NERS clean at the architecture level — strongest external validation in the 5-corpus set):**
- Cognitive-mode channel weights (7 channels: tempo, visual, tactile, leverage, measure, precommit, balance) as multiplicative biases over a shared physical substrate — modulate, never unlock.
- `eff_cw()` wired at 9+ live sites. The tradition-as-bias-not-rule-set philosophy is the correct architecture.
- Familiarity (tradition.py:50-67): bounded [0.85, 1.0], symmetric, applied to the read contest.
- **Convergence validation (corpus 5):** the weapon-typologies differential independently concludes that "the common ground is the physics, and the traditions are dialects of it" — the same sentence as tradition.py's docstring ("a way of reading the same physics, NOT a separate rule-set"). The document's 9 interface axes map to engine primitives at 7/9; its contact-decision spectrum (German fühlen = pro-contact vs Fabris rapier = anti-contact) maps directly to tactile channel weights (German 1.35 vs Italian 1.00). This is external confirmation that the substrate-bias architecture is the right abstraction.

**Key churn-positive mechanics (branch narrative state, not just tune):**
- Riposte role-flip: failed attack -> immediate role reversal, seeding exchange chains.
- Indes steal on read_win + commit>=4: high-stakes branch with asymmetric miss punishment.
- Single-time counter: counter_attempt is a genuine gamble (void the attack vs eat it undefended).
- Commit-depth / overcommit_exposure: deep commit -> exposure -> raised riposte probability -> role flip.
- Mode selection (parry/dodge/wind): commit-depth reactive flip (parry->dodge at commit>=4) is clean.
- Measure/approach/close phase: longer/shorter assignment gates stop-hit, reopen, approach phase — true path branches.
- REACH_W[armor] rotation: armor-vs-reach strategic tradeoff is genuine churn.

## ADD ONLY IF (corpus improvements that survived adversarial review, each gated on a stated condition)

**1. Decategoricalise non-blunt HEFT cliff (WP-2)** — severity: low (adversarial downgrade)
- The `wt='heavy'` boolean is a real cliff: greatsword (mass=2.7) and longsword (mass=1.4) both pay identical WEIGHT_PEN/ACT_WEIGHT/D_WT. But the adversarial verdict notes it affects only 1 weapon pair and is masked by 4 other axes.
- GATE: adopt only as a 3-tier HEFT (not continuous mass; not the full MoI/pommel machinery). One calibrated gain per site, preserving current heavy-value at current heavy-mass. Sim showing the 3-tier changes any matchup outcome.
- Adversarial note: "cliff real but affects only 1 weapon pair, masked by 4 other axes, not NERS-Necessary."

**2. Wariness as commit-depth bias (ENG-1)** — severity: low
- Commit-caution vs unreadable traditions: scale commit skew by `WARINESS_K*(1-familiarity())`.
- GATE: must ship WITH a hard spread-floor so combined disposition+wariness cannot collapse the {2,3,4,5} distribution to all-{2}. Must be logged as a deliberate 4th familiarity-consumer (familiarity already drives read accuracy, bind dominance, and the main read contest). Worst-case spread test is a hard gate.
- Adversarial note: "defensible but NOT clearly necessary; disposition+familiarity already cover the behaviour emergently."

**3. Wire precommit channel to main read contest (RF-05, INI-04, TL-05)** — severity: P2
- Japanese precommit=1.35 currently fires only in feint_eval (~30% of exchanges). Adding `TR.eff_cw(defender, 'precommit')` to the main read_d computation (wrapper.py:131) makes the "finest initiative tier" live in all exchanges.
- GATE: sim confirming the Japanese win-rate delta is non-zero and bounded. The channel label must match the consumer: if it stays feint-only, rename to 'feint_read'.
- Adversarial note: confirmed real across multiple modules. The channel name and its documented role are mismatched with its sole consumer.

**4. Counter_select probability clamp (INI-01)** — severity: P2 (adversarial downgrade from P1)
- Italian (tempo=1.30) + mezzo_tempo (x1.40) + cautious disposition yields counter_select probability 1.229, silently bypassing the probabilistic gate.
- GATE: add `min(1.0, ...)` to the counter_select product at wrapper.py:158. Pure correctness fix. No sim needed.
- Adversarial note: "verified true; the attack made it broader, not weaker."

**5. Close_rate fatigue=0 bug (TA-02)** — severity: P2 (adversarial downgrade from P1)
- `balance_eff(shorter, 0, cfg)` at wrapper.py:68 hardcodes fatigue=0. A fatigued fighter closes at the same rate as a fresh one.
- GATE: change to `balance_eff(shorter, ffat[shorter], cfg)`. One-character fix. No design decision required.
- Adversarial note: "structural core of the claim survives."

**6. Reopen_prob fatigue=0 bug (RR-02)** — severity: P2
- Same pattern: `balance_eff(longer, 0, cfg)` in reopen_prob (systems.py:223). Fatigue is dead input for reopen probability.
- GATE: add `fat_longer` parameter to reopen_prob() and pass `ffat[longer]` from wrapper.py:60.

**7. Push_avail stale carry-over (RR-01)** — severity: P2
- `push_avail` is not reset on failed reopen attempt, contaminating beat N+1 with beat N's shove bonus.
- GATE: reset `push_avail=False` on both success and failure of the reopen check.

**REJECTED by adversarial review (do NOT implement):**
- ~~Reach rewrite (K_REACH*fwd_extent_m)~~ — reach is already parametric and blade-length-grounded (r=+0.87). Regression risk.
- ~~Full 5-gain K_* set~~ — five uncalibrated knobs replacing exact tuned constants. Lever-pile.
- ~~pommel_kg as a live primitive~~ — pob_frac already suffices. Correct its values offline if needed.
- ~~Traditions-must-route imposition gate~~ — fights the substrate-bias philosophy (modulate, never unlock).
- ~~Roster expansions (short-blunt, 2H pole-blade, messer)~~ — out of scope; combat_analysis shows roster is reach-saturated.
- ~~Pre-contact seizure revival~~ — cut after ablation showed ~0 impact. Reviving the identical mechanism rebuilds proven-inert code.
- ~~14-dimension martial-morphology scheme~~ — the corpus's own distillation (F9) proves it outran the few variables that carry weight.
- ~~9 governing-analogues as mechanical taxonomy~~ — tradition.py already keeps exactly the concept (mode= flavour string) over one shared substrate.
- ~~Aliveness axis (D14) as PC lever~~ — pinned at 'alive' for every PC; redundant with history/skill. At most an NPC-flavour tag.
- ~~[B]/[L] mystical mechanics~~ — vol3 tags every one physically null; engine correctly has zero of them.
- ~~Shared resolver across combat+social~~ — the two engines correctly diverge at the resolution atom (zero-sum vs mixed-motive).
- ~~Argument-is-war/game conceptual-metaphor~~ — no lever follows from it.
- ~~OOB binary cliff fix~~ — adversarial verdict: real=false; graded degradation already present.
- ~~Feint_streak accumulation bug~~ — adversarial verdict: real=false; P1->P3.
- ~~One-shot extreme damage~~ — adversarial verdict: real=false; linear model deliberately ratified.
- ~~Flexible weapon class (kusarigama, whip-sword)~~ — corpus 5 self-notes "brutal weakness-profile" and rare historical use; no tradition support; would require new physics model. Out of scope.
- ~~Shield as separate mechanical item~~ — requires off-hand subsystem; paired_short partially covers dual-item. Out of scope.
- ~~Active hand-targeting ("defanging the snake")~~ — hand_guard already passively models protection differential (systems.py:99); active targeting would require new action type + damage pathway. Scope expansion.
- ~~Empty hand / grappling weapon entry~~ — engine already models the close/grapple as engagement terminus. Adding an 'unarmed' WEAPONS entry is redundant.
- ~~Poleaxe head reclassification (WTD-01)~~ — head='blunt' is a simplification but mechanically correct (gap=0.85 already models the spike thrust). Head-type proliferation risk outweighs cosmetic gain.

## SEQUENCING (ordered plan)

### Phase 1: Immediate (dead-data cull + doc repair — no sim needed)

1. **CUT dead config constants** from config.py: REACH_ADV_K, RESIDUAL_REACH_FRAC, CONC_BASE_K.
2. **CUT dead weapon field** `clinch` from all 12 WEAPONS dicts in combatant.py.
3. **CUT dead baked geo keys** `thrust`, `cut`, `halfsword` from geometry.bake() output and WEAPONS[w]['geo'] storage. Retain `perc_conc` only if Phase 2 percussion unification proceeds.
4. **CUT dead damage parameters**: remove `close` from damage()/strike() signature; remove QUAL['partial']; guard p_auth() call for blunt-only.
5. **FIX doc drift** in ability_armature.md: mark 'seize' as dead/cut, update channel-ability status to reflect wired eff_cw, fix staerke_schwaeche/misura/atajo status.
6. **FIX doc drift** in tradition.py:87-90 comment: channels are wired, not pending.
7. **FIX doc drift** in combat_engine_flow_and_state_map.md: remove DAMAGE_SCALE/CAP_END, update precommit status, add last-verified stamp.
8. **Retire or formally mark seize** lever + vorschlag + sen_no_sen (option A: mark as cut; option B deferred to Phase 3 if a new consumer is designed).

### Phase 2: Structural (consolidation — requires targeted validation)

9. **Counter_select clamp**: add `min(1.0, ...)` at wrapper.py:158. Verify with the mirror=50 invariant.
10. **Close_rate fatigue fix**: `balance_eff(shorter, ffat[shorter], cfg)` at wrapper.py:68. Mirror invariant.
11. **Reopen_prob fatigue fix**: add fat_longer parameter. Mirror invariant.
12. **Push_avail reset**: reset on both success and failure of reopen check.
13. **Hardcoded /0.62**: replace with `cfg['REACH_W']['none']` in systems.py:224.
14. **Balance channel propagation**: apply `TR.eff_cw(c, 'balance')` inside balance_eff() itself. Run mirror=50 + tradition-differentiation validation.
15. **Percussion unification** (WP-1 + perc_conc wiring): route armor_defeat_sigma through p_auth, multiply by geo['perc_conc'], remove hand-set `percussion` field. Requires mirror=50 + armour-tier re-sweep.

### Phase 3: Gated (additions requiring sim/calibration/Jordan call)

16. **Precommit channel widening**: add eff_cw('precommit') to main read_d at wrapper.py:131. Sim gate: Japanese win-rate delta non-zero and bounded.
17. **Seize reroute** (option B): only if a new consumer is designed AND simmed to non-zero impact. Jordan call on whether to rebuild vs permanently retire.
18. **HEFT decategoricalisation** (WP-2): 3-tier HEFT replacing the binary wt='heavy'. Sim gate: at least one matchup outcome changes.
19. **Wariness commit bias** (ENG-1): only with the spread-floor. Sim gate: worst-case compound-collapse test passes (cautious+unfamiliar cannot produce all-{2} commits).

## NERS SCORECARD

| Module | N | R | S | E | Notes |
|---|---|---|---|---|---|
| tempo_approach | partial | partial | fail | partial | S-fail: weapon_tempo dual-role (action-freq + close speed). Grip state branches dead. AGI_TEMPO_K inert. |
| read_feint | partial | partial | partial | partial | Feint triple-hit undocumented. Precommit channel isolated to feint-only (~30% beats). |
| reopen_recovery | partial | partial | partial | pass | Path (c) freed-hand shove is churn-inert (unconditional 22% passive). Fatigue=0 in reopen_prob. |
| commit_disposition | partial | partial | partial | partial | Commit depth is not a per-action player decision. DISP_INIT_K signal sub-attacker-bias. |
| defence_modes | partial | partial | partial | partial | CHOKE_BIND_K dead (hardcoded 0). fat_d dead parameter. GATE cap squashes cognitive base. |
| measure_reach | partial | pass | partial | pass | Lunge grip has no reach benefit (all-cost state). reach_adj inflates str_demand. |
| outcome_map / post-strike | partial | partial | partial | partial | Triple coin-flip on success+wind. Poise 12% range is churn-inert. |
| initiative_vor | partial | pass | partial | partial | Core Vor substrate robust. Counter_select overflow (>1.0). Dead seize abilities. |
| tradition_layer | partial | partial | fail | partial | S-fail: seize lever severed, balance channel 80% suppressed, precommit role-mislabeled. |
| damage_armour | partial | partial | partial | partial | Two-percussion-source role-conflation. Dead close/gap/QUAL parameters. |
| wrapper_structure | partial | partial | partial | pass | Dead clinch/CONC_BASE_K. ATTACKER_BIAS duplicates Vor. (Sandbox + WoundTracker: resolved.) |

**Resolution Diagnostic:** P-i pass, P-ii pass, P-iii partial (0.5 severity-anchor seam, P3), P-iv pass, P-v pass. Overall: **PARTIAL PASS.** Defects are at the periphery and in docs, not the resolver.

**Overall Engine Verdict:** The resolution spine is **sound** — sigma_N-scaled leverage is the right engine for this regime, ER-2 continuity is correctly applied, all feedback loops are bounded. The debt is dead data and orphan emissions at the periphery. The engine needs a cleanup pass (Phase 1-2), not a redesign. Phase 3 additions are optional polish gated on simulation evidence.
