# Comprehensive Analysis — Personal Combat (`combat_engine_v1`)

**Status:** Audit record (resolution-diagnostic pipeline, Stages 1–4 + comprehensive dimensions). Class-C mechanical findings, Jordan-vetoable.
**Session:** 2026-06-09. **Task type:** audit (gate passed; token 9c2bb1fa486d579c).
**Scope:** all workings and all dimensions of personal combat — architecture, canonical status, resolution mathematics, live-engine behaviour, balance, loops, constraints, coverage, implementability.

`[READ:]` provenance (all this session): `designs/scene/combat_engine_v1/{README.md, config.py, core.py, geometry.py, systems.py, combatant.py, tradition.py, wrapper.py, ability_armature.md}` (full); `tests/sim/v32-combat-balance/{m1_dice_sigma_core, r1_sigma_resolution, r2_consequence_wounds, r5_strength_stamina, r8_parity_harness, m3_weapon_class_layer, m7_facing_fov, m5_stance_reaction_coherence}.py` (full); `canon/02_canon_constraints.md` (full); `canon/editorial_ledger.jsonl` (ED-900–910 trail + live tail re-fetch); `designs/scene/combat_v30.md` (index + RANGED/ARMOUR/WOUNDS/GROUP/THREAD sections); `designs/scene/derived_stats_v30.md` (§4.1, §4.2, §5.2, §12, §14.1); prior audits `2026-06-02-combat-engine/ratification_and_deprecation_proposal.md`, `2026-05-28-resolution-diagnostic/ners_verdict_combat.md`, `2026-05-31-percell-combat/ners_verdict_percell_resolution.md`, `2026-06-06-weapon-physics-ners/weapon_physics_ners_reconciliation.md`, `2026-05-29-combat-armature/{armour_validation_result.md, RATIFIED_addendum_2026-05-30_leverage_gating.md}` (full). All probes executed in-container this session (engine assembled from canonical module text; import + fight smoke PASS).

---

## VERDICT

```
SYSTEM: personal combat            COMPONENTS (Phase 0): dice (exchange resolution) +
                                   deterministic (damage/armour/geometry/stamina accounting) +
                                   state machine (engagement wrapper) — composite
VERDICT: NON-COMPLIANT at system scope — coverage gap (ranged / group / thread have no engine
         resolution) + tradition-layer imbalance + two canonical-doc contradictions.
         The 1v1 MELEE RESOLUTION CORE in isolation is COMPLIANT: every prior live baseline
         reproduces, loops are damped and bounded, floors are clean, gradients are sane.

N: fail (component scope) — dead apparatus: `precommit` channel (0 consumption sites), 5/8
   equipped abilities inert, weapon mass/pob_frac fields unconsumed. Removable today without
   worsening play, or must be wired to earn their place. Live core itself: nothing redundant.
R: fail (system scope) — F1: personal combat as a whole cannot resolve ranged, group (>2), or
   thread-in-combat (no engine replacement for the superseded combat_v30 resolution layer).
   F2: hidden tradition tier list (~11pp field spread at equal channel budget).
   The melee core passes R: invariants reproduce, no fragile small-pool binaries, wound loop
   concave and bounded.
S: fail — F3: engine stamina cost model contradicts canonical derived_stats §4.2 (action costs,
   armour drain, Take-a-Breath). F4: declared resolution method (μ-shift, m1) ≠ implemented
   method (Ob-shift floored at 1, core.py); mass battle standardized on μ-shift → cross-scale seam.
E: pass for the live core (reach governs, mastery dominates, armour monotonic, aggression
   modest — outcomes are intuitable); fails for the tradition/ability layer (a player cannot
   intuit that japanese's signature channel and 5 of 8 abilities do nothing).
```

---

## FINDINGS (severity-ranked, worst first)

| # | Sev | Finding | Component | Evidence | Lesson(s) |
|---|-----|---------|-----------|----------|-----------|
| F1 | **P1** | Supersession-scope gap: ranged combat, group combat (>2 combatants), thread-in-combat live only in the superseded `combat_v30` resolution layer; engine is strictly 1v1 melee. Canonical_sources wording ("supersedes the RESOLUTION layer") vs ratification-proposal wording diverge on whether these are retained or orphaned. | system scope | combat_v30 §5 Ranged (LP/HP/sling TN 7/6/8, ranged DR, PP-720 FF), §8 Group (zone collapse, Fibonacci, rescue), §10 Thread; no engine counterpart in any module | — (coverage, not curve) → ED-911 |
| F2 | **P2** | Tradition channel-consumption imbalance + dead ability set. `precommit` channel: **zero** consumption sites (japanese's signature 1.35 weight inert). Equal-budget field spread ~11pp, stable across weapon contexts (not weapon-fit). 5/8 abilities inert: `seize` lever cut (vorschlag, sen_no_sen), `leverage`/`measure` levers never wired (staerke_schwaeche, misura, atajo). | tradition layer | Probe B3 (paired-seed deltas exactly 0.0pp for the five), B4 matrix (filipino .566/.557 field vs italian .452/.476 on longsword/rapier), call-site census | 2 (non-uniform impact of equal investment); N/E (dead apparatus) |
| F3 | **P2** | Stamina cost-model contradiction. Canonical `derived_stats §4.2` specifies action costs 5/8, armour per-action drain (heavy +2 / med +1), Take-a-Breath; engine implements `act_cost=(2+1·heavy+0.4·commit)·0.5`, geometric recovery, **no** armour drain, no Take-a-Breath. Same class as the ED-901/902/903 reconciliations. | stamina accounting | wrapper.py act_cost vs derived_stats §4.2; armour-drain absence adjudicated S-drift (not R-fail) by 2026-05-29 armour validation (fatigue-erodes-plate falsified) | 6-adjacent (doc/engine seam) |
| F4 | **P2** | Method discrepancy: `m1` declares μ-shift the resolution path and `eff_ob` display-only; `core.py`/`r8` resolve via Ob-shift floored at 1. Identical at TN7 until the floor clips; clip costs up to ~10–11pp at saturated advantage (pool 6, σ=+3: 76.3% vs 87.3%; pool 8, σ=+1.5: 83.5% vs 89.1%). Asymmetric: advantage clipped, disadvantage only soft-capped. Mass battle (2026-05-31 remediation) standardized on μ-shift. | dice resolution | Probe A analytic tables; m1 docstrings vs core.py | goal-over-form (declared ≠ implemented); S cross-scale |
| F5 | P3 | Post-ED-904 unratified commits: `deb405b944` (wound −1D wired into Combat Pool — mechanically significant; measured −18pp first wound in mirror), `e414098767` (weapon mass/pob_frac data — unconsumed, dead per 2026-06-06 audit), `2315b7d91e` (comment). Handoff blocker "ratify combat_engine_v1 (3 commits)". | ledger | commit dates vs ED-904; Probe C1 | — (ratification hygiene) |
| F6 | P3 | Doc-drift set: README still "canonical-candidate"; r1 Class-C pool label (ED-901/903 flip never landed in the substrate file); derived_stats §5.2 Concentration table still Focus×3 (ED-902 corrected form carried in §12/§14.1 only); combat_v30 §7 Stamina/MW prose (deferral-protected); ability_armature.md §2c/§7 lists the cut `seize` lever as live. | docs | file reads this session | — (drift) |
| F7 | P3 | Crit saturation at high pool + advantage: pool 12, σ=+1.0 → 74.2% overwhelming. Buffered by neutralize −0.45 and the tanh damage cap (max blow 18); combat lacks the ED-906 pool-gated Overwhelming bar applied to the social contest engine. Cross-scale S question, not a live defect (consequence bounded). | degree band | Probe A | observation → Jordan question |

Observations carried (not defects): sabre mirror draws 80% (open feel question, carried from 2026-06-06); per-roll wound −1D impact non-uniform (−9.7pp at pool 5→4 vs −3.5pp at 13→12 — Lesson-2 candidate; deliberate re-introduction `deb405b944`, intent rides on F5 ratification); max overwhelming hit 18 flat across Str 3→7 (tanh-saturated, carried); upset floor behaving (history+3 observed .938 ≈ .95·raw .99); one-shot boundary live only at End 1 (health 14 < max blow 18; felled-in-one-ENGAGEMENT 72.6%/46.7%/17.3% at End 1/2/4 — multi-blow engagements, not single blows, drive the End≥2 numbers).

---

## 1. SYSTEM INVENTORY & CANONICAL STATUS

**Canonical resolver:** `designs/scene/combat_engine_v1/` — ratified ED-900 (2026-06-04), re-ratified ED-904 ("all 2026-06 work approved as canon"; module SHAs: wrapper 6719ec2796, systems c4b609af63, core 3689c748d7, config 7d51446c18, combatant ea5a8faba9, geometry a1c085d588, tradition 308281a3be). Supersedes the RESOLUTION layer of `designs/scene/combat_v30.md` (lore/flavour retained). `config.py` is the live Class-C parameter source.

**Ledger trail:** ED-900 (ratify), ED-901 (Pool: strike (Agi×2)+Hist+3 → max(5, History+6)), ED-902 (Concentration = (3×Focus)+(2×Spirit); engine Cog→Focus fixed), ED-903 (params/combat.md → deprecated/), ED-904 (re-ratify all June work), ED-905 (mass battle), ED-906 (contest-engine de-saturation — **social engine only**, not combat). Post-ED-904 delta: the three F5 commits; `44dcc54ef2` (pre-contact seizure cut) self-declares Jordan-ratified.

**Architecture (Phase 0 decomposition):**
- **Dice-resolved:** exchange rolls — pool = max(5, History+6) (6–13D), d10 net engine (1→−1, 10→+2, ≥TN7→+1; μ=0.4/die, σ=0.8/die; continuous Normal canonical for Godot per params/core Decision E); degree band fail/partial/success(≥Ob)/overwhelming(≥2·Ob AND ≥3).
- **Deterministic accounting:** D1 damage (Impact×Coupling×Quality, tanh-capped at 12/blow); armour RESIST matrix with best-mode cut_thrust (removes the light→medium cliff); geometry-baked weapon coefficients; stamina/concentration economies; wound tracker (WI=End+6, MaxWounds=min(⌊End/2⌋+1,3), −1D/wound).
- **State machine:** engagement wrapper — approach + stop-hits → tempo-gated closed bursts (BURST_MAX=4) → read contest → mode → degree → outcome shapes (neutralize −0.45σ), single-time counter, bind ≤3 iters, riposte role-flip, reopen; fight() ≤12 engagements, no tiebreak (unresolved legitimate), 5% upset floor on decided fights; initiative substrate Vor/Nach/Indes with INIT_DECAY=0.75 damper + INIT_CAP=1.5 bound; poise/kuzushi.
- **Modulation layer:** 7 traditions as channel-weight profiles over 7 substrate channels (visual/tactile/precommit/leverage/tempo/measure/balance), familiarity 1.0/0.93/0.85; ABILITIES scaffold (8 entries, 3 wired).

## 2. STAGE 1 DIAGNOSTIC (Phases 1–6, condensed)

**Phase 1 — stress points.** Dice: design floor pool 6 (History 0); degradation floor max(1, pool − wounds − OOB) — e.g. pool 6 with 4 wounds → 2D per-roll. Exposure: routine for low-History actors; deep wound stacks rare (MaxWounds ≤ 3 + felled terminates). Deterministic: armour-matrix extremes (heavy vs none) and End-1 health floor. State machine: BURST_MAX and max_bouts caps are the designed bounds.

**Phase 2 — what the floor decides.** Exchange outcomes are graded (degree + magnitude→damage), routed through the wound clock (depth 2–4 wounds ≈ multi-segment) — not a disguised binary. Stakes recoverable within a fight until felled; felled persists to session end (r2). Risk profile at the floor: (M impact — single exchange swings one wound segment; M exposure; L–M irreversibility) — no three-high cell.

**Phase 3 — curves.** 3a: wound −1D is absolute → per-roll impact non-uniform (peak −9.7pp at pool 5→4; −3.5pp at 13→12); deliberate re-introduction (F5; intent gate pending its ratification). σ-leverage modifiers (the engine idiom) are uniform-impact by construction. 3b: the historical light→medium armour cliff is removed by best-mode cut_thrust; armour ladder measured monotonic (56/50/35/11). Wound curve smooth by design (derived_stats §4.1 table). No stacked accidental cliffs found. 3c: no live role conflation found in the core; `precommit` is the inverse defect (role with no carrier — F2). `[NULL: Phase-3b cliff scan across armour/wound/stamina boundaries — examined via ladder + analytic curves, nothing stacked found]`

**Phase 4 — loops.** Wound→pool→wound: concave (Probe C1: −18pp at 1 pre-wound, −11pp marginal at 2), damped by the 5% upset floor, capped by MaxWounds + felled + max_bouts. Initiative: INIT_DECAY=0.75 (gain<1 per engagement) + INIT_CAP=1.5; observed |max| 1.311 ≤ 1.5 with visible decay-to-zero in trajectories. Poise: bounded (min .84 observed). Stamina: floored at 0 in play; the ≤−4 abort never fired in 2000 heavy-greatsword fights (dead defensive code, harmless). Cross-system edge: felled persists to session end → downstream scene/faction effects are out of engine scope (by design; consumed elsewhere). **No undamped+unbounded loop.** `[NULL: Lesson-5 scan — examined, all loops carry damper AND cap]`

**Phase 5 — intent gates applied:** seizure cut (Jordan-ratified) → the two seize abilities' inertness is *intended-by-consequence*, but the undocumented `precommit` channel inertness and the field imbalance are accidental → F2 true. Wound −1D absolute: deliberate (deb405b944) but unratified → rides F5. No-tiebreak unresolved fights: explicit Jordan 2026-06-02 decision → pass. Upset floor: explicit videogame rule → pass. Armour (plate) dominance: intended + historically validated (2026-05-29) → pass.

**Phase 6 — triage:** F1 (H exposure at system scope, H irreversibility as a coverage hole) > F2 (M/H — every fight with traditions) > F3/F4 (M — doc/method seams) > F5–F7.

---

## 3. QUANTITATIVE RESULTS

### 3.1 Probe A — analytic resolution mathematics (no engine; m1 closed forms)

**Floor-clip divergence (Ob-shift-floored vs μ-shift), P(success), Ob 3, TN 7:** identical until the shifted Ob hits the floor at 1; beyond that the implemented path forfeits advantage. Worst measured: pool 6, σ=+3.0 → 76.3% vs 87.3% (−11.0pp); pool 8, σ=+1.5 → 83.5% vs 89.1% (−5.6pp). Disadvantage side diverges only via the 1.5·tanh soft cap (mild). → F4.

**Degree scaling (σ=0, Ob 3), overwhelming%:** pool 5/6/8/10/12/13 → 1.3 / 3.3 / 10.8 / 21.5 / 33.3 / 39.1%. At σ=+1.0, pool 12 → **74.2%** overwhelming (crit saturation; buffered by neutralize −0.45σ and the 12-point damage cap). → F7.

**Wound −1D per-roll impact, ΔP(net≥3):** −3.5pp at pool 13→12; −9.7pp at 5→4 (peak pool 4–6). Stacked at pool 6 with 0–4 wounds: 38.0 / 28.8 / 19.1 / 9.7 / 2.6%. Non-uniform in probability (Lesson-2 candidate); compounded in-fight magnitude measured at C1.

### 3.2 Probes B1–B2 — live invariants (n=2000/cell unless noted)

```
MIRRORS (A-of-decided)   longsword .495 · sabre .478 · greatsword .510 · spear .500
                         · dagger .522 · arming .508          — all in 48–52 band ✓
DRAW RATES               sabre .803 (prior 79%) · greatsword .331 (35%) · longsword .006 (0.5%)
                         · arming .089 (7.7%)                  — reproduce prior baseline ✓
ARMOUR LADDER (A light)  vs none .562 · light .499 · medium .351 · heavy .106
                         (prior 59/49/34/11; monotonic, ≤3pp)  ✓
HEAVY vs NONE            .922 (prior ~92%)                     ✓
MASTERY                  history +1 → .798 (prior 77) · +3 → .938 (at .95 upset ceiling;
                         raw ≈ .99) · cog +3 → .927 · agi +3 → .902
REACH                    spear v dagger .931 (prior 94)        ✓
STR (greatsword) +3      .761 (draw .145)
DISPOSITION              disp 7 v 1 → .570 · 7 v 4 → .538      (bounded +5–7pp)
POOL FLOOR               history-0 mirror .499 (draw .162)     — clean ✓
ONE-SHOT BOUNDARY        felled-in-one-ENGAGEMENT: End1 .726 · End2 .467 · End4 .173
                         (single-blow one-shot possible only at End 1: health 14 < max 18) ✓
```
`[NULL: regression scan vs the 2026-06-06 live baseline — examined across 11 B1 cells + 12 B2 cells, no regressions]`

### 3.3 Probes B3–B4 — abilities and traditions

Paired-seed ability deltas (n=3000, longsword mirror): **indes +0.6pp · mezzo_tempo +0.1pp · true_times +1.3pp** (the three wired levers; weak but live) — **vorschlag, sen_no_sen, staerke_schwaeche, misura, atajo all exactly 0.0pp** (identical RNG trajectories: the equip is never read). Call-site census confirms: only `counter_success`, `counter_select`, `anti_overcommit` consumed.

Full tradition matrix (28 pairs × 1200, field = mean win-rate-of-decided vs all others):

```
                 longsword field    rapier field    channel budget (Σ weights)
filipino              .566              .557              7.75
chinese               .542              .519              7.85
german                .534              .510              7.75
japanese              .507              .496              8.00   ← precommit 1.35 inert
english               .507              .503              7.60
spanish               .474              .508              7.75
italian               .452              .476              7.75
none                  .417              .431              7.00
corr(budget, field)   .649              .694
```

Equal-budget spread ~11pp, ranking stable across a bind weapon and a thrust weapon → **not** weapon-fit texture. Mechanism: (a) `precommit` has zero consumption sites; (b) consulted channels differ in loop heat — tactile/balance sit raw in per-exchange paths while defender `visual` is attenuated by familiarity×legibility×fatigue×feint (wrapper.py:132). `[ASSUMPTION: precommit's consumption site was the pre-contact seizure path cut 2026-06-05 — basis: the channel description names sen-sen-no-sen, the exact idiom of the cut seize-lever abilities; not verified against pre-cut source]` → F2.

### 3.4 Probe C — loops and stress

```
WOUND HANDICAP (longsword mirror, A pre-wounded)   0w .506 · 1w .326 · 2w .215
   → −18pp first wound, −11pp marginal second: CONCAVE, damped (upset floor), capped (MaxWounds)
INITIATIVE   |max| observed 1.311 ≤ INIT_CAP 1.5; trajectories decay to 0 (INIT_DECAY .75) ✓
POISE        min observed .84 (bounded) ✓
TURN COUNTS  arming mean 6.94, p50 7, p90 12, decided ≥3 turns .969 (prior anchor 94%) ✓
             longsword mean 4.42, decided ≥3 turns .844 (faster idiom)
STAMINA      min observed 0.0 across 2000 heavy-greatsword fights; ≤−4 abort never fired
```

---

## 4. STAGE 2 — LESSON MAPPING & REMEDIATION (worst-first)

```
P1 F1 (coverage)        → Jordan decision ED-911: (a) declare ranged/group/thread RETAINED-canonical
                          on the combat_v30 dice chassis pending engine extension (annotate
                          canonical_sources + combat_v30 header), or (b) scope engine extension.
P2 F2 (tradition layer) → Lesson 2 + N/E: wire or cut. Wire `precommit` by folding into the existing
                          pre-contact read paths (NOT by resurrecting seizure — see re-test); wire or
                          cut the three never-wired levers per the open D-α…δ tradition decisions;
                          then re-balance profiles against MEASURED field parity, not nominal budget.
P2 F3 (stamina docs)    → annotate derived_stats §4.2 cost-model paragraphs with engine supersession
                          (ED-901/902/903 precedent). §4.2's Stamina formula itself (3·End+2·Spirit)
                          matches the engine (r5 RATIFIED S1) — only the action-cost/armour-drain/
                          Take-a-Breath prose needs the annotation.
P2 F4 (method seam)     → either (i) doc-fix: re-declare Ob-shift-floored-at-1 as the canonical
                          resolution path in m1 (zero behavioural risk), or (ii) adopt μ-shift in
                          core.py to unify with mass battle (changes saturated-advantage outcomes up
                          to ~11pp; requires re-baselining §3.2). Recommend (i) unless cross-scale
                          unification is wanted.
P3 F5 (ratification)    → ED entry ratifying or reverting the three post-ED-904 commits; the wound
                          −1D wiring is measured, bounded, and working (C1) — ratify-recommend.
P3 F6 (doc sweep)       → one cleanup commit: README status line; r1 pool-label flip; derived_stats
                          §5.2 table; ability_armature §2c/§7 seize references.
P3 F7 (crit saturation) → Jordan question: adopt the ED-906 pool-gated Overwhelming bar in combat,
                          or accept (consequence already bounded by neutralize + damage cap)?
```

## 5. STAGE 4 — RE-TEST OF PROPOSED FIXES

- **F1(a)** retained-canonical: creates a two-resolver seam (old d10-allocation chassis + new engine co-live for different sub-modes) — an accepted-interim S cost; flag in canonical_sources so the seam is declared, not silent. F1(b): work, no new defect by construction.
- **F2** wiring `precommit`: **must not resurrect the ratified seizure cut.** Folding precommit into the existing read/initiative-steal paths adds no new state and no new lever. `[OPEN TRADE-OFF: a precommit consumption site that is faithful to sen-sen-no-sen (pre-contact intent read) vs the ratified removal of pre-contact seizure — needs Jordan's read on whether precommit modulates EXISTING pre-contact reads (safe) or re-introduces a seize site (barred)]`. Re-balancing to measured parity risks over-fitting to the longsword/rapier contexts measured here — validate on a third idiom (spear or mace) before ratifying weights.
- **F3** doc annotation: pure documentation; no behavioural surface. No new defect.
- **F4(i)** doc-fix: no behavioural surface. F4(ii) μ-shift adoption: re-opens every §3.2 invariant — full re-baseline required; do not combine with F2 re-balancing in one change (confounded attribution).
- **F5/F6**: ledger + doc hygiene; no behavioural surface.

RE-TEST: pass — no remediation introduces an undamped loop, a new cliff, or a role conflation; the two flagged trade-offs ([OPEN TRADE-OFF] above) are design decisions, not defects.

---

## 6. CONSTRAINT COMPLIANCE (canon/02_canon_constraints.md)

Combat-relevant checks: **P-06** (threadcut beings have no layer 2; self-maintenance is layer-three deliberate threadwork) — the engine treats all combatants uniformly through attributes and carries no layer-2 dependency in wounds or recovery; no conflict. **P-10/P-15** (Coherence) — the engine does not consume Coherence; thread-in-combat resolution is exactly the F1 coverage gap, so the interaction surface is currently undefined rather than non-compliant. **GD-1–3** (victory/faction-level rules) — not combat-binding; no combat mechanism registers a victory function. `[NULL: constraint sweep P-01–P-15 + GD-1–3 against engine mechanisms — examined, no violation; one undefined surface (thread-in-combat) already carried as F1]`

## 7. COVERAGE GAPS (F1 detail)

The engine resolves exactly: two combatants, melee, one weapon each (with halfsword form-switching). No engine path exists for: **ranged** (combat_v30 §5: LP TN7 / HP TN6 / sling TN8, ranged DR table, PP-720 friendly fire), **group** (>2: §8 zone collapse, Fibonacci offence bonus per PP-216, rescue, multi-engagement), **thread-in-combat** (§10). These remain written only in the superseded-resolution-layer document. Either they are retained-canonical (then the supersession wording over-claims and the two-resolver seam must be declared) or orphaned (then personal combat is incomplete at system scope). → ED-911, Jordan adjudication.

## 8. PRIOR-VERDICT RECONCILIATION

- **2026-05-28 chassis verdict** (non-compliant: OOB-vs-floor C3, allocation binaries): historical — its subject was the OLD chassis; the engine's σ-space OOB (−1.0σ) and graded exchange resolution resolve C3 by construction. Superseded.
- **2026-05-31 percell** (mass scale): its remediation standardized μ-shift at small N — the cross-scale half of F4.
- **2026-06-06 weapon-physics**: live baseline source; every number re-measured here reproduces (§3.2). Its MoI layer stays uncommitted (NERS-N/E) — unchanged; the e414098767 mass/pob fields remain dead data (F5).
- **2026-05-29 armour validation**: plate dominance intended + historically validated; fatigue-erodes-plate falsified → the missing armour drain is S-drift (F3), not R-fail. Confirmed and inherited.

## 9. GODOT IMPLEMENTABILITY

The engine is already the implementation idiom: pure-Python modules with a single RNG seam (`roll_net_continuous` — Normal(μ=0.4N, σ=0.8√N), canonical for Godot per params/core Decision E), deterministic accounting, geometry baked at build time, config-dict tunables (`config.py` as the live Class-C source), no GM arbitration anywhere (the F1 gap's PP-720 "Game Master arbitration" line is one of the TTRPG residues that an engine extension would have to replace with a deterministic rule). State machine maps to per-turn engagement calls ("the GAME calls one engagement per turn" — wrapper.py comment); fight() is sim-harness-only. Player-visible surface: weapon/armour/tradition/ability picks, disposition, grip — all UI-selectable; the substrate (channels, σ-leverage) is invisible engine logic. No blocking implementability defect found. `[NULL: Godot-translatability scan across modules — examined, none blocking]`

## 10. OPEN JORDAN DECISIONS (consolidated)

1. **ED-911 / F1**: ranged + group + thread — retained-canonical on the old chassis (declare the seam) or engine-extension scope?
2. **F2**: wire-or-cut for `precommit` and the three never-wired ability levers; re-balance traditions to measured parity? (Interacts with the open martial_traditions D-α replace/coexist, D-β count-6, D-γ grade-V, D-δ naming.)
3. **F4**: declare Ob-shift-floored canonical (doc-fix) or unify on μ-shift cross-scale (re-baseline)?
4. **F5**: ratify or revert the three post-ED-904 commits (wound −1D wiring measured working).
5. **F7**: adopt the ED-906 pool-gated Overwhelming bar in combat, or accept saturation as bounded?
6. Carried: sabre 80% draw rate (feel); max-hit 18 flat across Str (tanh saturation).

---

## AUDIT TRAIL (session tags, condensed)

`[READ:]` set as headed above. `[FIXED: missing m5_stance_reaction_coherence.py — fetched; engine import chain restored]`. `[NULL: B1/B2 regression scan — no regressions]`, `[NULL: Phase-3b stacked-cliff scan]`, `[NULL: Lesson-5 loop scan — all damped+capped]`, `[NULL: constraint sweep]`, `[NULL: Godot-translatability scan]`. `[ASSUMPTION: precommit↔seizure-cut causal link — flagged §3.3, unverified against pre-cut source]`. `[ASSUMPTION: the three F5 commits are the handoff's "3 commits" — basis: dates + ratified-marker on the seizure cut]`. Probe artifacts: `/home/claude/probe_b{1,2,3,4}.json`, `probe_b4_rapier.json`, `probe_c.json` (session-local). `[CONFIDENCE: high on all live measurements (n≥1200/cell, paired seeds for ability deltas); medium on the precommit causal mechanism (assumption flagged); high on documentary findings (full-file reads)]`
