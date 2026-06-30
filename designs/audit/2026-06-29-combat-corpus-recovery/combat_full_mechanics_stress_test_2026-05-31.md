# Full Combat Simulation — Stress Test (All Mechanics)

**Date:** 2026-05-31
**Scope:** Personal combat, full σ-leverage armature as wired in the **R8 parity harness** (the project's trustworthy, defect-immune integration oracle): resolution (r1) + wounds (r2) + Strength/Stamina (r5) + dice core (m1) + facing (m7) + weapons (m3) + the decisive-phrase model. Run with **both** the ratified damage model (R2: `net + STR×mult`, Heavy-Blunt ×3) **and** the unified damage candidate (this session).
**Method:** real verified modules run locally; harness budgets asserted == 18; N = 2000–6000 per cell; Wilson CI. Nothing reimplemented from memory.
**Status:** stress-test findings — **STAGED** (no canon/params/sim file written; Lane A/C own those).

---

## VERDICT (verdict first)

> **The full combat simulation is NOT yet balance-compliant, and the ratified damage model violates the no-one-shot directive.**
>
> 1. **The ratified Heavy-Blunt ×3 (W4) produces one-shots in 28.4% of decisive bouts** (earliest at strike 1) — a direct, frequent breach of the 2026-05-31 no-one-shot directive. The unified damage model eliminates it (**0.0%** one/two-shots; earliest fell at strike 5; structural — two maximal blows < Health). **[P1]**
> 2. **The equal-budget field is out of band under *both* damage models** — ratified `Str 85 / Spirit 12`; unified `Str 77 / Reading 69 / Spirit 8`. The damage model rebalances *which* build dominates but does not fix parity. The residual imbalance is **σ-leverage channel calibration** (the r5 Str-channel seeds, the Reading seed, Spirit's single thin channel) — not the damage model. This reproduces and extends R8's standing finding. **[P1]**
>
> The **resolution chassis itself is robust** — small-pool floor, death-spiral, and bounded-exchange all PASS. The outstanding work is Class-C channel calibration + one design gap (Spirit's 2nd channel) + adopting the unified damage model. None of the field imbalance is the damage model's fault; the damage model's job (kill the one-shot) is done.

```
N: PARTIAL    R: PARTIAL (field out-of-band)    S: PASS (unified) / PARTIAL (ratified D-F2)    E: PARTIAL (Str channel stack)
```

---

## A. What was exercised (and what was not)

**Exercised (the ratified σ-leverage armature, R8 harness):** History-driven Combat Pool (`max(5, History+6)`, R1); Agility as σ-tempo + facing leverage (R1/M7); Reading (Cog/Att) → net_σ; Strength leverage channels — bind, stagger, physical-pressure, wield gate, heavy-weapon access (R5/ST1); Stamina = `3·End + 2·Spirit` with per-action drain + out-of-breath penalty (S1/R5); initiative (Agi); the 5-subaction **decisive phrase** with closing/in-bind/breaking states (R2 decisive-exchange); Ob-scaled degree (R1); the wound-gate tracker (derived_stats §4.1); weapon-vs-armour (W1/W5) and the unified coupling grid (candidate).

**NOT exercised by this harness (honest coverage gap):** the **stance/reaction RPS layer (m5)** is imported transitively but R8's `resolve_phrase` builds net_σ explicitly without a stance term — so the active stance-choice loop is not stress-tested here. **Grappling** (the third plate-counter) is a separate system, not in the parity oracle. The old attrition bout/subaction/dual-resource modules (m4a/m4b/m6) are superseded by the decisive phrase and were not run. A full-mechanics test of stance-RPS and grappling needs a separate harness; they are not yet in the trustworthy parity oracle.

---

## B. Findings (severity-ranked)

### [P1] One-shot under the ratified damage model — fixed by the unified model
The decisive-phrase felling distribution, worst-case matchup (Str war-hammer build vs the squishiest build), N = 6000:

| Damage model | fells | earliest fell strike | **one/two-shot (≤2 strikes)** | median strike-to-fell |
|---|---|---|---|---|
| **Ratified** (`net+STR×mult`, Heavy-Blunt ×3) | 5729/6000 | **strike 1** | **28.4%** | 5 |
| **Unified** (bounded Str + coupling + force-cap) | 4232/6000 | **strike 5** | **0.0%** | 10 |

Across the *whole field* the unified one/two-shot rate is **0.00%** (7145 resolved bouts). The ratified ×3 Heavy-Blunt (W4) + crit-doubles-weapon-mod is the one-shot source. **The unified damage model is the fix, and it is decisive.**

### [P1] Field out of band under both models — a leverage-channel calibration problem
Equal-budget archetypes (each plays its best loadout, asymmetric, Wilson CI), identical chassis, **only the damage model swapped**:

| Build | Ratified field | Unified field | band 40–60 |
|---|---|---|---|
| Agi | 58% | 58% | ok |
| **Str** | **85%** | **77%** | **over (both)** |
| End | 43% | 40% | ok / low-edge |
| **Reading** | 50% | **69%** | ratified ok → **unified over** |
| **Spirit** | **12%** | **8%** | **dead (both)** |

- Swapping the damage model **moves the dominance**, it does not remove it: Str 85→77 (still over), Reading 50→69 (now over). The unified model routes damage through **placement/Quality (L1)**, so the high-net **Reading** build gains — *and the longer, no-one-shot fights give the placement edge more strikes to compound.*
- **Root cause is the σ-leverage channel seeds, not the damage model.** Strength's channels *stack* (bind + stagger + pressure + wield-access + armour-defeat); Reading's seed is now too strong under Quality-routing; Spirit's single channel (stamina reserves) is too thin to decide a short phrase. This is **Class-C calibration + one design gap**, exactly as R8 concluded — confirmed here from two damage models.

### [P2] Unified model over-rewards placement (Reading 50→69)
The Quality lever (0.6/1.0/1.5 = 2.5× range) is the unified model's dominant damage multiplier, and Reading maximizes the net_σ that sets the degree. L1 ("σ-leverage gates Quality") is working — *too strongly* in the field. → Calibration: dial the unified **QUALITY** factors and/or the **Reading→net_σ seed** so placement is a strong-but-bounded lever, not field-dominant. (Both are Class-C seeds.)

### [OPEN — Jordan] The no-one-shot ceiling trades phrase lethality
Under the unified model, fights are longer (median strike-to-fell 8 across the field vs ratified 5) and **only 64% of decisive phrases actually fell** — the other 36% resolve by wound-count (advantage, not a kill). The decisive phrase becomes "usually-but-not-always lethal." That is a design choice, not a defect:
- (a) **accept** — a phrase is a decisive *exchange*, often but not always a kill (historically realistic; bouts were sometimes "first blood / yield");
- (b) **lengthen** the phrase (more subactions → higher fell-rate, still no one-shot);
- (c) **raise** the per-blow ceiling slightly (more lethal, but watch the one-shot boundary).
Your call. The no-one-shot guarantee holds for (a) and (b); (c) trades into the one-shot region if pushed too far.

### PASS dimensions (robust — no remediation)
| Dimension | Test | Result |
|---|---|---|
| **No death spiral (L5)** | −1D/wound penalty into the pool, even matchup | field shifts only 45→41%; earliest fell stays strike 5; no runaway, no new one-shot — **damped** by phrase length + per-blow cap |
| **Small-pool robust (L3)** | History floor (pool 6); floor-mirror; high-vs-low | floor-mirror **exactly 50%** (no instability); high-skill (pool 10) vs low (pool 6) a **smooth 88%** (decisive, not a fragile binary) |
| **Bounded decisive exchange** | strike-to-fell distribution (field) | min 3 · p25 6 · median 8 · p90 10 · max 10; **0.00% one/two-shot**; no attrition |
| **Weapon roles / duel-vs-battlefield (C1)** | prior session duels + R10 context | preserved under the unified model (fencer wins duel 93.8%; war hammer wins armoured battlefield 99.6%) |

---

## C. NERS-fitness verdict (full system)

```
SYSTEM: Personal combat — full σ-leverage armature (R8 chassis) + damage layer
COMPONENTS: dice (σ-leverage resolution) + deterministic (damage) + continuous (Health, Stamina)
            + the decisive-phrase frame

VERDICT: NOT YET COMPLIANT — field out-of-band (channel calibration) + ratified damage
         breaches no-one-shot. Resolution chassis robust; damage layer fixed by the unified model.

N: PARTIAL — Most mechanics are necessary. BUT Strength carries FIVE stacked channels
             (bind + stagger + pressure + wield-access + armour-defeat); the 85→77 residual
             after the damage fix suggests Str is over-provisioned for its role. Trim toward
             the channels that are load-bearing (L1: do not keep apparatus that isn't needed).

R: PARTIAL — Robust at the small-pool floor and against the death spiral (both PASS). But the
             BUILD SPACE is not robust: a dead stat (Spirit 8–12%) and over-tuned stats
             (Str 77–85%, Reading 69% under the unified model) fail the 40–60% band. Not robust
             across builds until channel calibration + Spirit's 2nd channel land.

S: PASS (unified) / PARTIAL (ratified) — The unified damage model is smooth: the force-cap
             saturation removed the one-shot cliff, and degree is unified to Ob-scaled. The
             ratified path retains the D-F2 inconsistency (flat net≥3 crit in r2 vs Ob-scaled
             resolution) and the one-shot. Adopt unified → S passes.

E: PARTIAL — The chassis is intuitable, but (1) the five-channel Strength stack is complexity
             beyond Strength's needed role (E pressure), and (2) the no-one-shot lethality trade
             (a phrase that doesn't always kill) is a legibility question for players.
```

---

## D. The W4 tension (flag — requires your confirmation)
W4 (2026-05-29) ratified **keeping the Heavy-Blunt ×3 multiplier** as the war hammer's identity. The stress-test evidence shows that exact mechanism produces **28.4% one-shots**, which the 2026-05-31 directive ("no one-shot victories") rules out. The newer directive supersedes W4's *mechanism*; the unified model **preserves W4's *intent*** — the war hammer still dominates the armoured battlefield (99.6%) via coupling, not via a one-shotting multiplier. This is a **supersession of a ratified decision** — recorded here for your explicit confirmation, justified by the newer directive + the evidence. (Canonical/structural authority is yours; I am surfacing the conflict, not overruling it.)

---

## E. What's needed to reach in-band (none of it is the damage model)
1. **Adopt the unified damage model** (kills the one-shot; the correct damage layer). Supersedes W4's ×3 mechanism, intent preserved. — *Lane A (params) + Lane C (wire into r1/r2).*
2. **Calibrate the σ-leverage channel seeds against the R8 oracle:** dial **Str** channels down (still over at 77%); dial the unified **QUALITY** / **Reading** seed down (Reading over at 69%). Iterate vs R8 — it converges quickly now that the oracle is reliable. — *Class-C, your calibration call.*
3. **Give Spirit a 2nd combat channel** (8–12% dead under both models). Candidates (R8): Composure/will resisting stagger; a threshold "second wind"; resisting the out-of-breath penalty. Each is a new mechanic (design decision). — *your design call.*
4. **Decide phrase lethality** (the 64%-fell trade) — accept / lengthen / raise ceiling. — *your design call.*
5. **Extend coverage:** the stance/reaction RPS layer (m5) and grappling are not in the parity oracle; a full-mechanics balance claim needs them wired and swept too.

The resolution chassis (small-pool, death-spiral, bounded exchange) needs no remediation.

---

## Audit trail

```
[READ: tests/sim/v32-combat-balance/module_manifest.md — full module map; m4a/m4b/m6 = superseded attrition chassis]
[READ: designs/audit/2026-05-29-combat-armature/RATIFIED_2026-05-29.md + 4 addenda — R1/R2/S1/S2/ST1/W1–W5/C1/A1/A2/L1; W4 keeps Heavy-Blunt ×3]
[READ: r8_parity_harness.py + r8_result.md — trustworthy oracle; standing finding Str 85 / Spirit 12]
[READ (run): r1, r2, r5, m1, m3, m5, m7, m9 — fetched + executed locally; R8 reproduced Str 85/Agi 58/End 43/Reading 49/Spirit 12 exactly]
[ASSUMPTION: scope = personal combat, σ-leverage chassis as wired in R8 — basis: this session's through-line; mass battle is separate]
[ASSUMPTION: tier→(material,coverage) map none→(none,full) light→(cloth,full) medium→(mail,full) heavy→(plate,full) for the unified coupling — basis: A2 presets]
[CONFIDENCE: high — real verified modules run locally; R8 reproduced to the point; A/B and felling distributions are direct MC, N up to 6000]
[DRIFT: staged, not committed — Lane A owns canon/params, Lane C owns tests/sim; channel calibration + Spirit channel are Jordan-gated]
```
