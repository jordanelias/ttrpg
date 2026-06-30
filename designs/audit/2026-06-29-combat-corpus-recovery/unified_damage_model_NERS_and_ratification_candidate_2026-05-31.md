# Unified Damage Model — NERS Audit + Ratification Candidate

**Date:** 2026-05-31
**Author session:** combat σ-leverage stress-test / damage redevelopment
**Skill:** valoria-resolution-diagnostic (Stages 1–5) + valoria-dice-model (calibration)
**Companion:** `ners_stress_test_combat_sigma_leverage_2026-05-31.md` (Parts 1–2 — the stress-test that surfaced findings D-F1…D-F5)
**Status:** **RATIFICATION CANDIDATE — validated, NERS-compliant, STAGED (not committed).** Jordan-vetoable.
**Authority basis:** Jordan directive 2026-05-31 — "ratify whatever works best, which is the newest stuff you're developing … we probably don't want one shot victories." Mechanical-tier development, built bottom-up + validated top-down, logged below.

---

## VERDICT (review discipline — verdict first)

> **NERS-COMPLIANT (candidate).** One unified damage model replaces the three divergent models now in the repo (r2 wired, D1 ratified-but-orphaned, m9 oracle-only) and resolves **all five Part-2 findings** — D-F1 (orphaning), D-F2 (two degree definitions), D-F3 (Strength-ratio inversion), D-F4 (one-shot tail), D-F5 (four armour representations).
>
> Two items remain before canon ratification:
> - **S-PARTIAL:** ratifying requires propagating the unified (Ob-scaled) degree definition into `combat_v30 §5` and `m3`, which still carry the flat `net≥3` form (P2 propagation — analogous to the prior audit's C2).
> - **R-confirmation pending:** the model is validated standalone (calibration + HEMA suite + duels); the equal-budget point-buy **parity sweep** (r3/r4) must be re-run after wiring before declaring full Robustness across the build space.
>
> Neither blocks the design decision; both are integration/propagation work (Lane A + Lane C). The model itself is sound.

```
N: PASS      R: PASS (1 confirmation pending)      S: PARTIAL (1 propagation)      E: PASS
```

---

## A. What this replaces (D-F1 — orphaning)

The repo currently holds **three** damage models that disagree:

| Model | File | Status | Defect |
|---|---|---|---|
| r2 | `r2_consequence_wounds.py` | **wired** into r1/r3/r4 | `net + STR×mult + weapon_mod`; crit doubles weapon_mod. Under-protects armour 2–4× vs the ratified design; war hammer ignores plate. |
| D1 | `damage_model.py` | **ratified 2026-05-30, ORPHANED** | `Impact×Coupling×Quality`. Imported by nothing in the resolution chain. Best armour physics, but Strength-ratio inversion (D-F3) and a multiplicative one-shot tail (D-F4). |
| m9 | `m9_wound_model_bottomup.py` | oracle-only | `net + bounded-Str − resist`. Good bounded-Str instinct, but never wired. |

The unified model is **one** model, intended to be the single runtime path — ending the ratification-vs-implementation split. It keeps D1's (historically validated) coupling grid and m9's bounded-Strength instinct, fixes both their pathologies, and adds the no-one-shot ceiling Jordan directed.

---

## B. The model (spec)

Built bottom-up from the canonical wound model + the params/core degree definition + D1's coupling physics. Each constant tagged with its basis. **Constants marked `[C-seed]` are Class-C sim-tunable calibration values — the *structure* is the design; the *numbers* are tuning.**

### B.1 Canonical wound model — UNCHANGED
Source: `derived_stats §4.1` (authoritative; PP-716/717).
```
WI(End)     = End + 6                       # wound interval (damage per wound)
MW(End)     = min(End//2 + 1, 3)            # max wounds before felled
Health(End) = WI · (MW + 1)
wounds(cum) = floor(cumulative_damage / WI) # cumulative; felled at MW+1 wounds
penalty     = −1D per wound (universal, PP-716; floored — Class-A pool floor 5)
```
Reference End 4 → WI 10, MW 3, Health 40. **This layer is not touched.** The unified model only shapes the per-blow damage that feeds `cumulative`.

### B.2 Degree — UNIFIED to Ob-scaled (fixes D-F2)
Source: `params/core §Degrees` (the form the σ-leverage resolution `r1` already uses).
```
Failure:       net ≤ 0
Partial:       0 < net < Ob
Success:       net ≥ Ob
Overwhelming:  net ≥ 2·Ob  AND  net ≥ 3
```
Adopting this retires the flat `net≥3` definition in `combat_v30 §5` / `m3` / `r2` (the D-F2 conflict). Rationale: "Overwhelming" should mean *decisively beating the obstacle*, which scales with the obstacle. Propagation is the S-PARTIAL item (§F).

### B.3 Coupling — KEPT from D1 (historically validated armour physics)
Source: `damage_model.py` (D1). Reproduces the arms-and-armour matrix (Stage 5).
```
HEAD_MODE:  blunt→percussion   point→puncture   cut/straight_cut/curved_cut→shear
DELIVERY:   blunt 1.6 · point 1.45 · cut_and_thrust 1.35 · straight_cut 1.5 · curved_cut 1.5
RESIST (fraction blocked, material × mode):
            none  : perc 0    · shear 0    · punc 0
            cloth : perc .10  · shear .35  · punc .15
            mail  : perc .20  · shear .80  · punc .45
            plate : perc .30  · shear .95  · punc .70     ← plate near-immune to shear, soft to percussion/puncture-at-gaps
GAP (coverage gaps): full 0.15 · partial 0.50
coupling(head, material, coverage):
    transmit = 1 − RESIST[material][mode]
    puncture     → max(transmit, GAP)                 # thrusts seek gaps
    cut/blunt on armour → transmit·(1−GAP) + 1.0·GAP  # a fraction lands on bare zones
    return DELIVERY[head] · transmit
```

### B.4 Impact — BOUNDED Strength (fixes D-F3)
Additive (Jordan's stated no-Str×weight-synergy preference), with a *tight* Strength range so Strength is a secondary edge, never the dominant lever (the M9 lesson; the HEMA "skill > strength" anchor).
```
HEFT_FORCE:  light 4 · heavy 6                         [C-seed]  heavy weapons carry more force
str_force(Str) = clamp( (Str−3)//2, −1, +2 )           [C-seed]  Str1→−1 · Str3/4→0 · Str5→+1 · Str7→+2
Impact = HEFT_FORCE[weight] + str_force(Str)
```

### B.5 Placement (Quality) — the σ-leverage → degree lever (L1)
```
QUALITY:  Partial 0.6 · Success 1.0 · Overwhelming 1.5  [C-seed]
```
This is where **skill** flows into damage: σ-leverage raises the net distribution → raises P(Overwhelming) → raises Quality. Skill dominates via *frequency* of good placement, not per-hit force.

### B.6 Delivery + the no-one-shot ceiling (fixes D-F4)
**Key structural choice: cap the delivered *force* with a smooth saturation, then apply Quality *outside* the cap.** This bounds magnitude (no one-shot) while keeping placement meaningful for high-Impact weapons (the failure mode of a naïve cap — see Stage 4).
```
SCALE        = 2.67            [C-seed]  anchors an even Success ≈ 1 WI
FORCE_CAP(End) = 1.2 · WI(End) [C-seed]  the force saturation level

force      = Impact · coupling(head,material,cov) · SCALE
delivered  = FORCE_CAP · tanh(force / FORCE_CAP)        # smooth; bounded force — NO runaway (L6-clean)
damage     = round( QUALITY[degree] · delivered )       # placement scales the bounded force (L1 preserved)
```
Maximum possible single blow = `1.5 · FORCE_CAP = 1.8 · WI`. For End 4 that is **18 damage = 1 wound = 45% of Health** — so a single blow can never fell a healthy fighter, and two maximal blows (36) still fall short of Health (40). **Earliest possible fell = the 3rd telling blow.** This is the no-one-shot guarantee, structural rather than a flag.

The saturation is the **same tanh idiom the resolution engine already uses** (the σ-leverage soft-cap `1.5·tanh(net_σ/1.5)`) — not a new subsystem.

> **Resolution-side seed used in the duel validation (not part of the damage model):** weapon speed → σ-tempo, `δσ = speed · TEMPO_K`, `TEMPO_K = 0.10` `[C-seed]`. This belongs to the armature's tempo channel (W2), feeding the σ-leverage *contest*; it is what gives fast weapons their duel edge. Listed here only because it is load-bearing for the duel/battlefield split below.

---

## C. Validation (top-down)

All numbers exact / Monte-Carlo from the calibrated model; End 4 (WI 10, Health 40); base Ob 2; duels N = 20 000.

### C.1 Calibration targets
| Target | Result | Verdict |
|---|---|---|
| **T1 anchor** — Str4 light-cut Success vs none ≈ 1 WI | **10 = 1.00 WI** | PASS |
| **T2 no-one-shot** — max blow & blows-to-fell | max blow **18 = 1.80 WI = 1 wound (45% Health)**; blows-to-fell maxOW **3**, Success **4**; structural minimum **3** | PASS |
| **T3 Str-uniformity** — Str7/Str1 dmg ratio (was 7.5× light / 2.5× heavy under raw D1) | arming **1.22×** · longsword **1.09×** · war hammer **1.09×** · estoc **1.33×** · staff **1.33×** | PASS |
| **placement preserved** — war hammer Partial/Success/OW vs none | **7 / 12 / 18** (spreads — cap does not flatten degree) | PASS |

### C.2 Historical suite (HEMA / arms-and-armour)
| # | Check | Result | Verdict |
|---|---|---|---|
| H1 | plate negates cuts | cut vs plate **3 = 0.30 WI** (≈0) | PASS |
| H2 | blunt defeats plate | blunt vs plate **11** > cut **3** | PASS |
| H3 | thrust-to-gaps beats cut vs plate | point **4** > cut **3** | PASS |
| H4 | rise of the thrust (vs mail) | point **7** > cut **4** | PASS |
| H5 | armour monotonic (per head) | none ≥ cloth ≥ mail ≥ plate, all heads | PASS |
| H6 | coverage (gaps) | partial-plate cut **6** > full-plate **3** | PASS |

### C.3 Duels — skill, the finesse/power axis, and the duel/battlefield split (C1)
σ-contest = skill setup + weapon-speed tempo. Bounded exchange (≤8 strikes), wound-tracker.
| Matchup | Result | Expected | Verdict |
|---|---|---|---|
| **(ii) DUEL, unarmoured** — skilled light fencer (Str3, σ+0.75, fast) vs strong war-hammer (Str7, σ−0.5, slow) | **fencer 93.8%** | fencer wins the duel (tempo + placement beat raw force unarmoured) | PASS |
| **(ii) BATTLEFIELD, both plate** — same two fighters | **war-hammer 99.6%** | war-hammer dominates (anti-plate Impact; the light cut is negated) — its niche | PASS |
| **(i) SAME longsword** — skilled+weak vs strong+unskilled | **skilled 88.1%** | skill > strength | PASS |
| **(iii) EQUAL skill** — weak vs strong | **strong 57.6%** | strength a *modest* tiebreaker, not dominant | PASS |

The duel/battlefield split is the historically correct weapon-role outcome: light/fast weapons own the unarmoured duel; the war hammer owns the armoured battlefield. Strength matters as a tiebreaker (iii) but never overrides skill (i, ii).

---

## D. NERS audit (Stages 1–5)

### Stage 1 — Diagnostic (Phase 0–6), damage layer
- **Phase 0 (decompose):** dice-resolved = σ-leverage strike (net, degree); deterministic-accounting = the damage formula (force→coupling→quality→bounded delivery, no roll); continuous resource = Health via the WI accumulator.
- **Phase 1 (stress point):** combat pool floors at 6D (above the sub-5D danger zone — see Part 1). Damage stress points = the maximal blow (Str7 heavy blunt OW unarmoured) and the armour extremes (cut vs plate). Exposure: max blow reached by strong heavy builds landing OW (moderate, not routine); cut-vs-plate routine.
- **Phase 2 (what it decides):** graded magnitude → wounds → −1D and (at MW+1) felling. Stakes recoverable (wounds clear at session end; no Stage 1/2 dying, ED-130). After the no-one-shot ceiling, the magnitude swing cannot flip a healthy fighter to felled in one blow → no H-Impact dimension on the damage layer.
- **Phase 3 (curves):** 3a impact uniformity — Strength impact uniform-ish (1.09–1.33×), saturation diminishes marginal Str *smoothly* → PASS. 3b cliffs — the force-cap is a smooth tanh saturation (no cliff); degree bands are discrete *outcome classes* (resolution side, intended/legible), the wound accumulator is a discrete accumulator (exempt per the three-category rule) → no accidental cliff. 3c role conflation — each variable one role (Impact=force, coupling=armour interaction, Quality=placement, degree=resolution outcome); the old STR-multiplier conflation is gone → PASS.
- **Phase 4/Lesson-5 (loops):** the only feedback is wound → −1D → pool (resolution layer), already damped (pool floor + session-end wound clearance + Trigger-5 three-condition gate on cross-scale leakage to faction Stability). The damage model adds **no new loop**; the no-one-shot ceiling *reduces* death-spiral risk (a blow cannot dump a target to felled, so −1D accrues gradually) → bounded.

### Stage 2 — Lesson mapping
| Finding (Part 2) | Lesson(s) | Remediation (this model) |
|---|---|---|
| D-F1 orphaning | L1 (one role) | collapse 3 models → 1 runtime path |
| D-F2 two degree definitions | L1 / L6 | unify to Ob-scaled; propagate (§F) |
| D-F3 Strength-ratio inversion | L2 (uniform impact) | bounded `str_force`; uniform-ish ratio |
| D-F4 one-shot tail | L5 (bound the magnitude) / L6 (smoothly) | force-cap saturation; max 1.8 WI/blow |
| D-F5 four armour reps | L1 | one coupling grid (RESIST × mode × coverage) |

### Stage 3 — NERS verdict
```
SYSTEM:     Personal combat — σ-leverage resolution + unified damage model (candidate)
COMPONENTS: dice (σ-leverage net) + deterministic (damage formula) + continuous (Health/WI)

VERDICT: NERS-COMPLIANT (candidate) — one model resolves D-F1…D-F5; S pending degree
         propagation; R pending the equal-budget parity sweep after wiring.

N: PASS    — Collapses three redundant damage models into one (D-F1). Removes the
             STR-multiplier conflation (the prior audit's open C6: "Heavy Blunt ×3"
             vs "Mace = 6") in favour of one bounded additive Strength rule (L1).
             The added apparatus is minimal and necessary: the force-cap is the
             smallest no-one-shot mechanism and reuses the engine's own tanh idiom
             (no new subsystem); the coupling grid replaces four armour reps with one.
             No over-engineering.

R: PASS    — Holds at extremes: max blow bounded (1.8 WI, structurally ≥3 blows to fell);
             cut-vs-plate ≈ 0; armour monotonic; the duels validate skill>strength, the
             duel/battlefield split, and strength-as-tiebreaker against historical
             precedent (Stage 5). One safeguard per loop, all damped.
             PENDING: wire into r1/r2 and re-run the equal-budget point-buy parity
             sweep (r3/r4) across the full build space — the standalone duels pass; the
             whole-build-space in-band check is the remaining R evidence.

S: PARTIAL — The model is internally smooth and consistent with its sibling (the
             resolution tanh): force-cap saturation is L6-clean (no cliff); Strength
             impact is uniform (L2); degree is unified to Ob-scaled (D-F2 closed in the
             model). BUT ratifying it requires propagating the Ob-scaled degree into
             combat_v30 §5 and m3 (which still carry the flat net≥3 form) and retiring
             r2's flat crit. Until propagated, the flat/Ob-scaled split persists in
             canon. P2 propagation (directly analogous to the prior audit's C2).

E: PASS    — Player-intuitable in one sentence: damage = how hard you hit (heft + a
             little strength) × how well it lands against their armour (mode vs material)
             × how cleanly it lands (placement) — with a natural ceiling so no single
             blow ends you from full health. One rule per concept; the STR-multiplier
             contradiction is gone; the duel/battlefield split is legible (light+fast =
             duel, heavy = battlefield). The force-cap is "invisible but real" like the
             resolution tanh — the felt promise "you can always take one more blow."

REMEDIATION (worst-first):
  P2  D-F2 degree propagation  → Lesson 1/6: update combat_v30 §5 + m3 to Ob-scaled
                                  degree; retire r2 flat net≥3 crit. (Lane A.)
  --  R-confirmation           → wire unified model into r1/r2; re-run r3/r4 equal-budget
                                  parity sweep; confirm all builds in-band. (Lane C.)
  --  D-F1/D-F3/D-F4/D-F5      → CLOSED by this model (no further remediation).
```

### Stage 4 — Re-test of the proposed fix (caught one new defect, resolved it)
The diagnostic's documented re-test trap fired exactly as warned — *"a Lesson-5 fix (add cap) creates a new threshold cliff (fails Lesson 6)."* The **first** cap design (saturate the *final damage*) compressed the Quality lever for high-Impact weapons: the war hammer's Partial and Overwhelming both pinned near the cap, so "poor placement blunts the heavy weapon" (L1) failed and the strong war-hammer beat the skilled fencer 83–17 *unarmoured* — a disguised L6/L1 failure.

**Resolved by restructuring:** cap the *delivered force*, apply Quality *outside* the cap. Placement spread restored (war hammer Partial 7 / Success 12 / OW 18), no cliff, no-one-shot retained, and the duel flipped to the historically correct fencer-favoured 93.8%. Re-tested clean against the full suite (§C). **RE-TEST: PASS.**

### Stage 5 — Historical precedent (the external R axis; reality, never genre convention)
- **Phenomenon modelled:** Renaissance hand-to-hand combat (HEMA / arms-and-armour). Validated: plate negates cuts; percussion and thrust-to-gaps defeat plate; the rise of the thrust vs mail; skill (measure/tempo/placement) over raw strength; the duel-vs-battlefield weapon split. All PASS (§C.2, §C.3).
- **On the no-one-shot constraint vs the skill's "never genre convention" rule:** the constraint is reconciled with reality, not imported from it. A real fight — even a lethal unarmoured one — is a short *bounded exchange* (measure → entry → the telling blow), not a single instantaneous kill from full readiness. "No single blow fells a healthy, ready fighter; a bout is 3+ telling blows" is therefore the *bounded-exchange* reality, **not** an HP-sponge or health-regen trope. It satisfies Jordan's videogame directive without contradicting historical precedent. **Stage 5: PASS.**

---

## E. Findings resolved + the no-one-shot guarantee

| Finding (Part 2) | Status |
|---|---|
| D-F1 — ratified D1 orphaned (runtime r2 under-protects armour) | **RESOLVED** — one model, intended single runtime path |
| D-F2 — degree defined two ways in one pipeline | **RESOLVED in model**; canon propagation = §F (P2) |
| D-F3 — Strength-ratio inversion (light 7.5× / heavy 2.5×) | **RESOLVED** — bounded str_force, ratio 1.09–1.33× |
| D-F4 — multiplicative one-shot tail (~92% Health max blow) | **RESOLVED** — force-cap; max blow 45% Health; ≥3 blows to fell |
| D-F5 — four armour representations | **RESOLVED** — one coupling grid |

**No-one-shot, stated as a guarantee (Jordan's directive):** maximum single blow = `1.5 · FORCE_CAP = 1.8 · WI`. Two maximal blows < Health for all End. Earliest possible fell = the 3rd telling blow. The ceiling is a smooth saturation (no dead-zone above it), so a stronger or better-placed blow always does *somewhat* more — up to the ceiling — preserving expressiveness.

---

## F. Integration plan (staged — not committed; lane discipline)

This session has not declared a lane and the three-lane window is active; `canon/**`, `params/**` are **Lane A**'s exclusive territory and `tests/sim/**` is **Lane C**. Ratification is therefore staged as lane-scoped actions, not committed here.

**Lane C (simulation):**
1. Implement the unified model as the single `strike_damage` path; have `r1` call it.
2. Retire `r2`'s `net + STR×mult` and the orphaned `D1` `Impact×Coupling×Quality` (both superseded).
3. Re-run the **equal-budget point-buy parity sweep** (r3/r4) across the full build space; confirm all builds in-band (the remaining R evidence).
4. Wire weapon-speed σ-tempo (`TEMPO_K`) into the contest if not already present (armature/W2).

**Lane A (canon / params):**
5. Propagate the **Ob-scaled degree** definition into `combat_v30 §5` and `m3`; retire the flat `net≥3` form (closes D-F2 in canon). — *the S-PARTIAL item.*
6. Land the unified damage model into `params/combat` as canon (replacing the r2/D1 split), citing this candidate.
7. File the editorial-ledger entries below, allocating ED IDs from Lane A's reserved block (890–939).

**Calibration note:** `SCALE`, `FORCE_CAP`, `HEFT_FORCE`, `str_force` bounds, `QUALITY` factors, and `TEMPO_K` are Class-C sim-tunable seeds. The *structure* (force → coupling → bounded delivery → placement; bounded additive Strength; one coupling grid; Ob-scaled degree) is the ratification target; the numbers may be retuned by the simulator without re-opening the design.

---

## G. Editorial-ledger candidates (DRAFTED — not appended; need Lane-A ID allocation)

Not written to the live `canon/editorial_ledger.jsonl` (append-shared; IDs must come from a lane's reserved block, and the known ED-ID reconciliation backlog is Lane-A-owned). Drafted here for Lane A to number and file:

```
[ED-####]  P1  Unify personal-combat damage to a single model (force→coupling→bounded
                delivery→placement). Supersede r2 (net+STR×mult) and orphaned D1
                (Impact×Coupling×Quality). Closes D-F1, D-F3, D-F4, D-F5.
                Basis: derived_stats §4.1 (wound model) + params/core (degree) + D1 coupling.
                Validation: this candidate §C (HEMA 6/6 + duels). No-one-shot guaranteed.

[ED-####]  P2  Unify the degree definition to Ob-scaled (params/core) across combat:
                update combat_v30 §5 and m3; retire flat net≥3 crit (incl. r2). Closes D-F2.

[ED-####]  P3  (Optional) Record weapon-speed σ-tempo (TEMPO_K) as the armature channel
                that produces the duel/battlefield weapon split (W2).
```

---

## Audit trail

```
[READ: skills/valoria-resolution-diagnostic/SKILL.md — full: three categories, Stage 1 Phase 0–6, six lessons, NERS format, Stages 4–5]
[READ: designs/audit/2026-05-28-resolution-diagnostic/ners_verdict_combat.md — prior combat verdict; C6 STR-multiplier contradiction; mandate to re-run on a restructured chassis]
[READ: references/lane_assignments.yaml — Lane A owns canon/params; ledger append-shared w/ reserved blocks; Lane C = sim]
[READ: designs/audit/2026-05-31-percell-combat/ (listing) — concurrent per-cell movement session; do not write into; cross-session reconciliation is not unilateral]
[ASSUMPTION: "ratify whatever works best, newest" grants mechanical-tier development authority per the project-owner contract — basis: Jordan directive 2026-05-31, verbatim]
[ASSUMPTION: no-one-shot = no single blow fells a healthy fighter (≥3 telling blows) — basis: Jordan "no one shot victories" + bounded-exchange historical reconciliation]
[DECISION: cap force then apply Quality outside the cap — basis: Stage-4 re-test caught placement-compression when capping final damage; restructure resolved it]
[CONFIDENCE: high — all magnitudes from canonical constants or the calibrated model (exact + N=20000 MC); HEMA 6/6 + 4 duels pass; framework read this session, not memory]
[DRIFT: ratification staged, not committed — reason: no declared lane + active 3-lane window; canon/params = Lane A, sim = Lane C. Candidate delivered; commit is a coordinated lane action.]
```
