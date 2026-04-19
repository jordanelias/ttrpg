# Valoria — Arc Test Batch 4 Results

**Date:** 2026-04-19  
**Simulation:** `arc_test_batch4.py`  
**Systems:** PP-431-COR fix, PI track, RDT/TD cascade, Accord revolt, Löwenritter Coup  
**Canonical sources:** `params/bg/parliament.md`, `params/bg/tracks.md`, `params/bg/core.md`, `params/bg/phases.md`, `params/bg/ci_seizure.md`

---

## B4-1: PP-431-COR Fix — Challenge Replaces Structural Suppression

**The corrected model produces meaningful variance that the wrong model did not.**

| Config | Seizure season range (5 seeds) | Note |
|--------|-------------------------------|------|
| Structural only | S12–S14 | Baseline, fully deterministic at Δ+5/season |
| PP-431-COR corrected | S12–S18 | +0 to +4 season delay, genuine seed variance |

**Key finding:** The B3-5 model (Challenge supplements structural) produced the same result as structural-only because the +5/season CI cap was already hit every season regardless. With PP-431-COR correct model: Challenge *replaces* structural, so in seasons where Challenge fires, CI loses the guaranteed −1 from structural but gains a stochastic −1 or −2 from a successful Challenge roll, and gains +1 from Assert that structural suppression's Suppress roll would have negated.

The net effect: in good Challenge rolls (Overwhelming, CI−2), CI gains only +3 that season instead of +4. In bad rolls (Partial/Failure), CI gains +5 because structural is suppressed AND Challenge failed, making those seasons worse for Hafenmark than structural-only. This creates genuine variance — seeds range from S12 (same as baseline) to S18 (Challenge repeatedly Overwhelming + stochastic CI−2 fires).

**PP-431-COR confirmed correct and worth modeling.** The strategic trade-off is real: aggressive Challenge use risks Partial/Failure seasons where Hafenmark sacrifices reliable suppression for unreliable CI spikes. The decision to play Challenge should be situational (play when CI is near a threshold, not every season).

**Confirmed B3-5 bug was real.** The Piety Yield issue (cap hit regardless) is still present — corrected PT values from core.md make it even more severe: T9 starts PT=5 (not PT=1 as B3-1 incorrectly assumed). Piety Yield at T9 full PT = 5×5/5 = 5/season, hitting the cap immediately. All other CI sources become noise once T9 PT is maxed from game start. **T9 starts at PT=5 in canon — Church doesn't need to build it up. This changes B3-1's findings substantially.**

---

## B4-2: PI Track Dynamics

**PI is highly stable and difficult to collapse.**

| Config | PI final (30 seasons, seed 42) | PI≤2 seasons |
|--------|-------------------------------|--------------|
| HF manoeuvre every season | 16 | none |
| HF manoeuvre every other | 11 | none |
| Crown Emergency Powers q5 | 10 | none |
| Church seizes 3×/10 seasons | 11 | none |

PI starts at 7, gains from successful Manoeuvre (+1), and loses from Crown Emergency Powers (−1), Church seizure (−1), and Coup (−3). With Hafenmark manoeuvring every season, PI reaches 15–19 over 30 seasons — far into "Full Parliament" territory. Even with Crown Emergency Powers firing every 5 seasons and Church seizing 3× per decade, PI only reaches ~10.

**Key findings:**

1. **PI never enters the NonFunctional state (≤2) under any tested configuration without the Coup.** PI is structurally net-positive under normal play: Hafenmark Manoeuvre (Mandate 4 vs Ob 2) succeeds roughly 70% of the time (Success/Overwhelming), yielding +1 PI on most attempts. The combined PI loss from Crown EPs + Church seizures is ~−0.4/season, well below the +0.6/season from manoeuvring.

2. **PI drifts upward throughout the game under Hafenmark pressure.** This is counterintuitive — PI is supposed to represent parliamentary tension, but the mechanic as modeled has Hafenmark continuously building PI rather than fighting to maintain it. By S24, PI is 15+ in all configs, far above the threshold effects. **Design gap:** the PI track's upper bound (20) is never approached as a meaningful limit, and the upper bands (8–10: Full Parliament) produce Crown Policy requiring Mandate ≥4 — a mild constraint that Crown at M=5 trivially meets. The PI track needs either higher-frequency PI loss sources or more meaningful PI ceiling effects.

3. **Crown Emergency Powers at q5 barely move PI.** −1 PI every 5 seasons = −0.2/season against Hafenmark's +0.6/season Manoeuvre rate. Emergency Powers are not a viable Crown counter to Hafenmark's parliamentary strategy. **The canonical Crown lever against Hafenmark is NOT Emergency Powers — it's direct military threat (Coup Counter advancing) or the Royal Decree/Mandate suppression path.**

4. **Overwhelming Manoeuvre (CI−1 + PI+1) is rare but impactful.** In seed 42 with EPs, two Overwhelming Manoeuvres fire (S21, S24), each dropping CI by 1 in addition to PI+1. These are the only moments where Church CI takes meaningful damage from parliamentary action. **Overwhelming Manoeuvre is the primary Hafenmark tool against CI, not the structural suppression.**

---

## B4-3: RDT/TD Track — Reformed Doctrine Cascade

**Critical finding: RDT/TD cannot prevent Seizure. It can make Seizure survivable.**

| Config | CI60 season | RDT final | TD final | Seizure season | Seizure Ob bonus |
|--------|------------|-----------|---------|---------------|-----------------|
| No RDT | S8 | 0 | 0 | S10–S18 | 0 |
| RDT pursuit | S8 | 5 | 5 | S10–S18 | +2 (TD4) |

CI reaches 60 at S8 in every seed regardless of RDT pursuit. RDT advances once per arc (4 seasons), so by S8 (arc 2), RDT=2 and TD=1. **TD4 (Seizure Ob+2 in Hafenmark territories) is not reached until S20 — after CI60 at S8 and likely after first Seizure attempt.**

However: in seed 42, first Seizure fires at S15 (a Failure — Church rolls 11d vs Ob 7). TD is 2 at that point, providing 0 Ob bonus (TD4 not yet reached). Church then tries again later; by then TD4 is active. **The RDT/TD path makes late Seizure attempts dramatically harder, not early ones.**

**Ob at T8 Gransol (Hafenmark capital) analysis:**
- Base Ob: `10 − PT(3) = 7`
- At TD4: Ob 9
- At TD5: T8 permanently unseizable
- Church pool at CI 80: `6 + floor(80/15) = 11d`
- 11d vs Ob 9: expected net ≈ −2 (Failure). **TD4 makes T8 functionally unseizable even before TD5.**

**RDT5/TD5 permanence: T8 becomes permanently unseizable at TD5 (S24 in the simulation).** This is the most significant defensive mechanic for Hafenmark's capital. The race: can Hafenmark reach TD5 before Church seizes T8? At the current pace, TD5 fires at S24. First Seizure attempt against T8 occurs at S15. If Church rolls well at S15 (before TD4), T8 falls. If Church fails at S15, by S20 TD4 makes T8 Ob 9 (nearly impossible), and by S24 TD5 makes it permanent.

**Design implication: the RDT/TD path is a coherent long-game defensive strategy for Hafenmark.** The first ~12 seasons are exposed; after S20 Hafenmark is highly resistant. Whether players can survive the exposed window is the game's tension. **This is robust design.**

**Gap:** Seizure at S15 in seed 42 is a Failure (pool 11 vs Ob 7, bad rolls). The Failure costs Church Stability −1 and grants Crown a Casus Belli. This interaction — Seizure Failure consequences — is not tracked in any simulation yet. It needs to be modeled in engine_v4 Phase 3 (political layer).

---

## B4-4: Accord Revolt Cascade

**Critical finding: Strain reaches Collapse (10) in 4–5 seasons under active warfare. Once at Collapse, the system has no recovery path in the current model.**

| Config | Strain final | Uncontrolled territories | Seasons to Collapse |
|--------|-------------|------------------------|---------------------|
| 6 garrisoned, 1 bps | 10 (battles, not revolts) | none | S5 |
| 4 garrisoned, 1 bps | 10 | T6, T14 | S4 |
| 4 garrisoned, 2 bps | 10 | T6, T14 | S4 |
| 2 garrisoned, 2 bps | 10 | T3, T5, T6, T14 | S4 |

**Key findings:**

1. **Strain hits 10 (Collapse) by S4–5 in every active-warfare scenario.** At 2 battles/season: Strain +2/season, reaching 10 in 5 seasons. At Collapse, Accord caps at 2 in non-capital territories, Mandate checks fire Ob 3 each Accounting, and RS −1/season extra. **The system maxes out almost immediately under sustained conflict** — Strain 10 is not a late-game state, it's an early-game state.

2. **Ungarrisoned territories at Accord 1 revolt within the first 3–4 seasons.** T6 Stillhelm and T14 Ehrenfeld (the last two in garrison priority) fall to Uncontrolled at S4 in the 4-garrisoned scenario. Once Uncontrolled, they generate Strain+1 each from the revolt itself, pushing Strain from 8→10. **The cascade is fast and deterministic.**

3. **Strain has no recovery mechanism under sustained warfare.** Strain decays −1/peaceful season, but in the simulation every season has battles. Once at Collapse, the game is in perpetual crisis with no exit without ceasing all conflict for multiple seasons. **This is correct design** — it's the forcing function for resolution. But the Collapse state persisting for 15+ seasons with no change is a design smell: the game needs either (a) a way to reduce Strain even during conflict (treaties partially do this per phases.md), or (b) Collapse being terminal (triggering shared loss) rather than an indefinitely stable state.

4. **The two-scenario comparison (1 bps vs 2 bps, same garrison) produces identical outcomes.** Both produce the same uncontrolled territories at the same season. This is because the Accord cascade is driven by the ungarrisoned Accord 1→0 rule, not by the number of battles. **The battle count affects when Strain crosses bands (and triggers Accord drops from Crisis), but not which territories ultimately revolt.** The structural fragility is garrison coverage, not battle intensity.

5. **Critical gap: Strain has a static model in this sim.** In canon, treaties reduce Strain (−1 from diplomatic resolution, phases.md 4d). The absence of any treaty mechanism means the sim overstates how long Collapse persists. In real play, Strain 10 is an emergency that incentivizes treaty-making. **[GAP: treaty mechanic interaction with Strain not modeled — required for engine_v4 Phase 4 political AI]**

---

## B4-5: Löwenritter Coup — Timing and Aftermath

**The Coup fires early and produces a permanent PI=0 state that accelerates Church victory.**

| Pressure | Coup season range | PI final | CI bonus from PI≤2 |
|---------|------------------|---------|-------------------|
| Low (0.25/s) | S8–S23 | 0 | +2/season for ~20 seasons |
| Moderate (0.5/s) | S4–S8 | 0 | +2/season for ~22 seasons |
| High (0.75/s) | S4–S5 | 0 | +2/season for ~25 seasons |

**Key findings:**

1. **PI collapses to 0 immediately after the Coup in every seed.** The Coup fires PI−3. At moderate/high pressure, PI is 4–7 when the Coup fires (still Standard/Degraded band). PI−3 drops it to 1–4. At band 3–4 (Degraded), PI continues decaying from Church seizures and no Hafenmark Manoeuvre (which is unavailable at PI≤2). **PI reaches 0 within 1–2 seasons post-coup and stays there.** The post-coup state is permanent non-functional Parliament for the remainder of the game.

2. **PI=0 (NonFunctional) means CI+2/season every season post-coup.** Over 20+ seasons at +2 bonus CI, Church gains 40+ extra CI beyond normal Piety Yield growth. CI reaches 100 and stays there. **The Coup accelerates Church victory — paradoxically, the Löwenritter Coup is Church's strongest ally.** A Crown player who allows the Coup fires enables Church to win faster. This is a major design interaction worth documenting.

3. **Coup Counter advancement rules are a gap.** The sim models Coup Counter as a stochastic ≈0.5/season under moderate pressure, reaching 4 in 4–8 seasons. But the canonical advancement sources are not fully specified in any doc read. From `params/bg/core.md`: "Threshold 4 = coup eligible." From `params/bg/parliament.md`: Coup fires PI−3 and gives Löwenritter T14. **The advancement trigger events (which specific actions increment the counter) are in docs not yet read** — likely `designs/npcs/npc_character_analyses_v30.md` or a separate Löwenritter doc. `[GAP: Coup Counter advancement sources not canonical — advancement events not specified in read docs]`

4. **Crown Mandate doesn't drop at Coup.** The sim applies Crown M−1 at Coup as a modeling assumption, but no canonical source confirms this. The coup gives T14 to Löwenritter — Crown loses the territory's strategic value but not necessarily Mandate from the coup itself. Mandate loss would come from subsequent Stability checks due to PI=0 Mandate checks Ob3. **[GAP: Coup effect on Crown Mandate — not specified in read docs]**

5. **The post-coup board is Löwenritter at T14 (Fort3, Mil6) + PI=0 + CI accelerating.** Löwenritter at T14 with Mil6 is nearly impregnable (Battle Ob = `3+3=6` for any attacker; only Varfell at Mil7+ or Church Templars could challenge). This creates a three-way late game: Löwenritter holds the peninsula's key fortress, Church races to Seizure with accelerated CI, and Crown must recover from a crippled parliament. **This board state is rich with player decision points.** It's one of the most interesting late-game scenarios in the design.

---

## Cross-System Observations

**Campaign arc with Coup (moderate pressure):**

| Season | Event |
|--------|-------|
| S4–S8 | Coup fires. T14 → Löwenritter. PI collapses to 0. |
| S8 | CI already at 60 (Piety Yield from T9 at canonical PT=5). Seizure available immediately. |
| S8–S15 | Seizure probability building. RDT/TD track at 2/1 — Hafenmark capitals not yet protected. |
| S15 | Mass Seizure likely fires (CI 80–90). First attempt against T9 or T1. |
| S20 | TD4 active — T8 Gransol Ob+2. Hafenmark capital now defensible. |
| S24 | TD5 — T8 permanently unseizable. |

The Coup and Church Seizure are temporally close: if Coup fires at S8 and Seizure fires at S15, they're 7 seasons apart. The PI=0 CI bonus (+2/season from S8) is largely wasted because CI is already racing to 100 via Piety Yield. **The CI bonus from PI=0 is irrelevant past CI 80.** The real coup consequence is not CI acceleration — it's the permanent loss of Parliament as a Hafenmark tool, and the strategic value of T14 Fort3 transferring to a faction that doesn't press political victory conditions.

---

## Gap Flags

```
[GAP: T9 PT=5 at game start (canonical) — B3-1 used wrong PT values; Piety Yield hits +5/season immediately; Assert is irrelevant from turn 1, not after PT buildup; B3-1 seizure timing results need revision]
[GAP: Coup Counter advancement sources — which specific events increment the counter not found in any read doc; sim used stochastic model]
[GAP: Coup effect on Crown Mandate — not specified whether Coup itself drops Crown M; only PI−3 confirmed canonical]
[GAP: Seizure Failure consequences — Stability−1 + Casus Belli granted to controlling faction; not tracked in any simulation; relevant for Church strategy post-S15 failed attempts]
[GAP: Strain recovery under conflict — treaty mechanic (−1 Strain from diplomatic resolution) not modeled; Strain Collapse may be less permanent in real play]
[GAP: PI track upper-bound effects — Full Parliament (PI 8–10) effects (Crown Policy M≥4) are trivially met by Crown M=5; band effects need review for gameplay meaningfulness]
```
