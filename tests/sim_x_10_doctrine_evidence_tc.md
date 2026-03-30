# SIM-X-10: Baralta — Sovereign Authority Doctrine + Olafsson Evidence Chain
## Mode: C (Full Scenario) + B (Interaction Chain: Domain Action × Evidence Chain × TC cascade × Zoom In to social scene)
## Mechanics: §6 Factions × §9 Social × §11 Domain Echo × §13 NPCs × Clock triggers
## Context: Season following SIM-X-05 (Debate loss). Baralta invokes the Sovereign Authority Doctrine — her signature Domain Action — despite the +1 Ob penalty from the Grand Debate loss. Simultaneously, players supply Solvind Brak's testimony corroborating Baralta's Olafsson-Niflhel evidence. Two Domain Actions chain in a single seasonal phase. Clock state: RS 28, TC 23 (post-X-08 +1), IP 21 (passive drift +1).

---

## Setup

### Current Clocks
RS: 28 (Stirring) | TC: 23 | IP: 21

### Baralta's State
- Mandate: 4 (starting value; not depleted yet)
- Social penalty: +1 Ob on all social/Domain actions vs Church this season (from Grand Debate loss in X-05)
- Sovereign Authority Doctrine available (once per campaign arc)
- Pool: Mandate 4 (faction pool) + Reach 5... 

Wait — re-read §13 Baralta: "pool: Mandate 7 + Reach 5." These are listed as pool values, not faction stat values. Cross-referencing §13: "The Sovereign Authority Doctrine. Usable once per campaign arc as a Domain action against Church Reach (Ob 4; pool: Mandate 7 + Reach 5)."

These appear to be fixed pool values, not the live faction stat. Treat as: Baralta's Domain Action pool = Mandate 7 + Reach 5 = 12D. With +1 Ob penalty: effective Ob = 4+1 = 5.

Doctrine roll: 12D TN7 vs Ob5. P(≥5 net) from reference ≈ 42%.

---

## Action A: Sovereign Authority Doctrine Domain Action

**Pool:** 12D TN7. **Ob:** 5 (4 base +1 from Debate loss penalty).

Expected net successes: 12×0.33 = 4.0. Ob5 requires ≥5 net.

| Degree | Result | P |
|--------|--------|---|
| Overwhelming (net ≥7) | TC −3, Church Mandate −1, Investigation blocked | ~12% |
| Success (net 5–6) | TC −2, Church Mandate −1, Investigation opens Ob4 | ~30% |
| Partial (net 3–4) | TC −1, Investigation opens immediately, Church Reach +1 | ~33% |
| Failure (net ≤2) | TC +1, Investigation opens, Baralta Mandate −1 | ~25% |

**Most likely outcome: Partial (33%).** TC −1, Investigation opens immediately, Church Reach +1.

### Applying Partial result:
TC: 23−1 = **22**. Church Reach effective +1 (domain modifier this season). Heresy Investigation opens immediately (Stage 1: File Building, Church Reach vs Ob3).

**Domain Echo check:** Doctrine invocation is a Domain Action that crosses from factional to institutional scope. Domain Echo: Baralta wins TC reduction — feeds into the parliamentary record. No further echo needed (it is already the top-level faction action).

---

## Action B: Olafsson-Niflhel Evidence Chain (simultaneous, same season)

Per §13 Baralta: "If players supply corroborating evidence (Solvind Brak's testimony or documentary records), Baralta launches a Domain action against Church Stability: Ob 3, pool Mandate 7 + Reach 5 + player evidence bonus."

**Assumption:** Players have obtained Brak's testimony this season (not simulated — assumed complete for this test).

Player evidence bonus: +2D (corroborating testimony, documentary records — standard investigative success at Ob2 produces +2D bonus per §11 Domain Actions).

Baralta pool: Mandate 7 + Reach 5 + 2D bonus = 14D TN7. Ob3. P(≥3 net from 14D) ≈ 98%.

**Most likely: Success or Overwhelming.**

| Degree | Result | P |
|--------|--------|---|
| Overwhelming (net ≥6) | Church Stability −2, TC −3, Olafsson suspended | ~72% |
| Success (net 3–5) | Church Stability −2, TC −3, Olafsson suspended | ~26% |

Wait — §13 combines Success and Overwhelming into same result: "Success: Church Stability −2, TC −3, Olafsson's Inquisitor operations suspended." No differentiation given. Overwhelming likely adds a bonus (GM discretion — possible Mandate damage or additional NPC consequence).

**Most likely outcome: Success/Overwhelming (98%).** Church Stability −2, TC −3, Olafsson suspended.

### Applying Evidence Chain:
Church Stability: 5−2 = **3**.
TC: 22−3 = **19**. (Two Domain Actions in same season; seasonal cap ±2 per faction attribute per season — but TC is a clock, not a faction attribute. Confirm: §11.5 "Faction attributes may not change by more than ±2 per season." TC is a clock, not a faction attribute. Cap does not apply to TC.)

TC drops from 22 to 19 in a single season. That is −3 in one action.

**Church Stability brake check:** "When Church Stability falls to 5 or below at seasonal accounting, TC generation ceases that season." Church Stability is now 3 — well below 5. TC generation ceases this season. All TC passive drift sources are suppressed.

TC passive drift (Church Mandate ≥7 condition check): Church Mandate = 5 currently; not ≥7. Passive drift suppressed anyway.

---

## Zoom In: Inquisitor Investigation Opens (from Partial Doctrine result)

Heresy Investigation Stage 1 (File Building) opens against [target TBD — likely Maret Uln or a practitioner in Baralta's circle]. Church Reach pool + Olafsson… except Olafsson is suspended.

**Olafsson suspended:** Inquisitor operations run by Olafsson are paused. The Investigation still opens (per the Doctrine's Partial result) but cannot be actively prosecuted while Olafsson is suspended. It sits as an open file.

**Who prosecutes?** Himlensendt could appoint a replacement. Jarnstal's Templars are the enforcement arm but lack the investigation apparatus. Klapp (now TS 50) could be tasked — but his TS development makes him an unreliable Inquisition instrument.

**Finding F-42 [P2]:** Two simultaneous Domain Actions (Doctrine + Evidence Chain) in the same season interact in non-trivial ways: the Doctrine opens an Investigation, the Evidence Chain suspends the primary Investigator. The result is a mechanically opened but effectively frozen Investigation. The rules do not define this interaction explicitly — it emerges from the sequence of outcomes rather than a named rule.

---

## Zoom Out: Seasonal Accounting

### Clock Summary After Action A + Action B
TC: 22 → 21 (Doctrine Partial −1) → 19 (Evidence −3) → **19**. Below 22 threshold.

Hmm — TC started this season at 23. After both actions:
TC: 23 −1 (Doctrine) −3 (Evidence) = **19**.

Check TC 20 threshold crossing: TC was 22 entering season; crossing below 20 crosses the lower bound of TC band 20–39 ("Ecclesiastical Consolidation"). TC is now 19 — entering "Institutional Pressure" band (0–19).

**TC threshold event:** TC drops from Ecclesiastical Consolidation (20–39) into Institutional Pressure (0–19). Per §7 threshold logic: "When RS crosses a threshold, the GM determines a narratively appropriate consequence from the current situation."

This is significant — TC crossing back below 20 means Church authority over marriage law, inheritance disputes, and educational standards is no longer mechanically entrenched. The institutional conquest is partially reversed.

**Finding F-43 [P1-flag — design concern]:** Two Domain Actions in a single season can move TC by −4 (Doctrine −1 + Evidence −3). Starting TC at 23, this collapses a threshold crossing in one season. The seasonal cap on faction attributes (±2) does not apply to clocks. TC has no seasonal cap. A motivated player coalition with the right evidence can drop TC by 4+ in a single season, potentially crossing multiple thresholds. This may be intended (political pivots should be dramatic) or may need a seasonal TC change cap. [Not proposing a patch — flagging for user decision.]

### Church Stability consequences
Church Stability 5→3. At Stability 3 (well below 5): TC brake activates. But also: internal Church crisis. Cardinals competing publicly. Olafsson's suspension is public — visible humiliation of the Cardinal of Justice.

Church Stability check for Leadership Deviation: Himlensendt acted against doctrine? No — the Doctrine invocation was external. Stability check does not fire for external faction damage. Stability simply sits at 3.

At Stability 3: the Church's internal cohesion is fractured. Any Domain Action against the Church gets reduced Ob (weaker target). Specifically: Church Reach effectively −1 for Domain Actions (destabilised institution). GM call.

---

## Zoom In: Himlensendt's Response — Emergency Appeal

Himlensendt (Presence 6, History Theology 3, Appeal pool: 6+6=12D) makes an emergency public Appeal to Parliament to preserve Church jurisdiction. This is a single-roll persuasion (no Debate structure). Disposition: Parliament is now Neutral (evidence of Niflhel connection has shifted them).

Appeal Ob: Parliament neutral → Ob2. Plus: Church Stability is 3 — Himlensendt is visibly weakened. GM applies +1 Ob (institutional weakness): Ob3.

12D TN7 vs Ob3. P(≥3 net) from 12D ≈ 87%. Most likely: Success.

**Domain Echo from Himlensendt's Appeal (success):** Parliament persuaded Church jurisdiction should be preserved in some domains. TC +1 (partial recovery from public legitimacy restoration).

TC: 19→20. Just crosses back over the threshold. Oscillation — Church barely holds institutional footing at TC 20.

**Finding F-44 [P3]:** A single successful Appeal by a high-pool NPC (12D) at Ob3 produces a Domain Echo that partially reverses a multi-action TC reduction. The TC clock can oscillate within a single season through chained Domain Actions from multiple actors. This is mechanically correct (the rules support it) but creates a bookkeeping challenge in fast-moving political seasons.

---

## Full Season Accounting (Combining X-09 and X-10)

| Clock | Start | X-09 | X-10 Actions | X-10 Himlensendt | End |
|-------|-------|------|-------------|-----------------|-----|
| RS | 28 | 28 | 28 | 28 | **28** |
| TC | 22 | 22 | 19 | 20 | **20** |
| IP | 20 | 20 | 20 | 20 | **20** (+1 passive drift pending) |

**Cross-clock check at accounting:**
RS 28 < 55: TC +1/season. TC: 20+1 = 21.
RS 28 < 40: TC +2/season (total, replaces above). TC: 20+2 = **22**.
IP: passive drift +1. IP: 20→21.
TC at 22 < 40: no TC→IP cross-clock effect.

Wait — "RS < 40: TC +2/season (total)." RS is 28 (< 40). Therefore TC gains +2 from passive drift due to RS state.

But Church Stability brake: Stability = 3 (< 5). "TC generation ceases that season." Does this brake apply to cross-clock passive drift from RS? The brake says "TC generation ceases that season regardless of Church Mandate." It specifically references Church Mandate as the source being suppressed. Cross-clock RS→TC drift is a structural clock mechanic, not Church-Mandate-driven generation.

**Finding F-45 [P1 — rules ambiguity]:** Church Stability brake ("TC generation ceases") — does it suppress RS-driven cross-clock TC increase? The text says "TC generation ceases that season regardless of Church Mandate" — the "regardless of Church Mandate" clause suggests it suppresses Mandate-based TC drift, but the RS→TC cross-clock entry is a separate mechanic. Ambiguous. Two interpretations: (a) brake suppresses ALL TC increase sources this season; (b) brake suppresses only Mandate-based TC generation. This is a rules gap requiring user decision.

**Taking interpretation (a) for now:** Church Stability brake suppresses all TC increase this season.

**Final clocks after full accounting:**
RS: 28 | TC: 20 (brake suppresses +2) | IP: 21

---

## Findings Summary (SIM-X-10)

| ID | Category | Severity | Description |
|----|----------|----------|-------------|
| F-42 | Interaction | P2 | Doctrine opens Investigation; Evidence Chain suspends Investigator — emergent frozen Investigation state, no explicit rule |
| F-43 | Design | P1 | Two Domain Actions can move TC by −4 in one season; no seasonal TC cap exists; may be intended but warrants user decision |
| F-44 | Design | P3 | High-pool NPC Appeal can partially reverse multi-action TC reduction in same season; clock oscillation possible |
| F-45 | Rules | P1 | Church Stability brake ambiguity: does it suppress RS-driven cross-clock TC increase or only Mandate-based TC generation? |
