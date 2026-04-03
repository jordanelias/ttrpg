# SIMULATION: BG FAIL FORWARD — COMPARATIVE ANALYSIS
## Test ID: SIM-FF-01
## Simulator Modes: A (isolation) + C (full scenario) + D (edge cases) + L (precedent)
## Date: 2026-04-02
## Status: WORKING SIMULATION — not yet committed

---

## SETUP

Two parallel 4-season runs of the same board state. Identical rolls (fixed seed). The only variable is whether Fail Forward (FF) complication table (PP-177) is active.

**Starting board state (Season 1, Year 1):**
- Crown: Mandate 5, Influence 5, Wealth 4, Military 4, Stability 4, Standing 5. Controls T1, T2, T4.
- Church: Mandate 5, Influence 6, Wealth 5, Military 4, Stability 5. Controls T3, T7. Theocracy Counter (TC) 28.
- Hafenmark: Mandate 4, Influence 4, Wealth 5, Military 3, Stability 4. Controls T6.
- Varfell: Mandate 4, Influence 4, Wealth 3, Military 3, Stability 4, Intel 4. Controls T9.
- Guilds: Mandate 3, Influence 4, Wealth 3, Military 3, Stability 4. Controls T8, T11.
- Rendering Stability (RS): 72. Public Instability (PI): 5. Institutional Pressure (IP): 20.

**Fixed roll sequence (d10, pre-rolled for all actions):**
S1: Crown Govern 1,4,8,3 → net 0 (Failure). Church Trade 7,9,2 → net 2 (Success Ob1). Hafenmark Diplomacy 6,1,8 → net 0 (Partial at Ob1? Net = +1-1 = 0 = Failure). Varfell Spy 7,7,3 → net 2 (Success Ob2: exact). Guilds Trade 4,4,6 → net 0 (Failure). Crown Military march 8,7,3,2 → net 2 (Success Ob2).
S2: Crown Govern T1 8,9,1,6 → net 1 (Partial Ob2). Church Decree 7,10,4 → net 3 (Overwhelming Ob2). Hafenmark Trade 7,8,7,5 → net 3 (Overwhelming Ob2). Varfell Investigate 6,4,2 → net 0 (Failure). Guilds Govern 9,7,3,1 → net 1 (Partial Ob2). Church Thread Op 8,7,9 → net 3 (Success Ob2).
S3: Crown Diplomacy 6,3,1,8 → net 0 (Failure Ob1? net = 0 = Failure). Church Govern 7,9,4,2 → net 2 (Success Ob2). Hafenmark Muster 4,4,7 → net 1 (Ob2 = Partial). Varfell Parliamentary Manoeuvre 7,10,1 → net 2 (Success Ob2). Guilds Community Organising 6,3,2 → net 0 (Failure). Varfell Thread Op 7,8,9 → net 3 (Success Ob2).
S4: Crown Decree 3,2,6,8 → net 1 (Partial Ob2). Church Muster Templar 10,7,3,2 → net 3 (Success Ob3). Hafenmark Parliamentary Manoeuvre 4,3,7 → net 1 (Partial Ob2). Crown Govern T2 9,8,7,1 → net 2 (Success Ob2). Guilds Trade 7,9,3,1 → net 1 (Partial Ob2). Church Diplomacy 7,7,6,4 → net 2 (Success Ob2).

---

## RUN A: WITHOUT FAIL FORWARD (Current Rules)

### Season 1

**Crown Govern (T1) — Failure (net 0, Ob 2):**
Result: Action wasted. No state change. Prosperity T1 unchanged.

**Church Trade — Success (net 2, Ob 1):**
Result: Wealth +1 → Church Wealth 6.

**Hafenmark Diplomacy (vs Guilds) — Failure (net 0, Ob 1):**
Result: Action wasted. No state change. Relations unchanged.

**Varfell Spy (on Church) — Success (net 2, Ob 2):**
Result: Intel on Church Mandate revealed.

**Guilds Trade — Failure (net 0, Ob 2):**
Result: Action wasted. No state change. Wealth unchanged.

**Crown Military March to T5 — Success (net 2, Ob 2):**
Result: Crown unit enters T5.

**S1 State changes (Run A):** Church Wealth 6, Varfell gains Church intel. Crown unit in T5. Everything else: static. Rendering Stability 72, Public Instability 5, Institutional Pressure 20.

---

### Season 2

**Crown Govern T1 — Partial (net 1, Ob 2):**
Result: Goal achieved with reduced effect. Prosperity +1 (Partial = reduced success only, no complication in current rules).
*Note: Current rules have no defined Partial effect for Govern — defaulting to "partial success = half effect" which is also undefined. Treating as Prosperity +1 (vs +2 on Success).*

**Church Decree — Overwhelming (net 3, Ob 2):**
Result: Crown Mandate −1 → Crown Mandate 4. Church gets bonus effect (Mandate +1 → Church Mandate 6? Overwhelming bonus undefined for Decree. Treating as standard Success effect only — gap noted.)

**Hafenmark Trade — Overwhelming (net 3, Ob 2):**
Result: Wealth +2 (Overwhelming) → Hafenmark Wealth 7 (ceiling). Surplus lost.

**Varfell Investigate — Failure (net 0, Ob 2):**
Result: Action wasted. No intel gained. No state change.

**Guilds Govern T8 — Partial (net 1, Ob 2):**
Result: Reduced success. Prosperity T8 +1.

**Church Thread Op — Success (net 3, Ob 2):**
Result: Rendering Stability −1 (Co-Movement). RS 71. Thread Debt token placed in T3.

**S2 State (Run A):** Crown Mandate 4, Church Wealth 6, Mandate 6, Hafenmark Wealth 7 (ceiling hit), RS 71, Varfell no intel from Investigate, Prosperity T1+1, T8+1.

---

### Season 3

**Crown Diplomacy (vs Church) — Failure (net 0, Ob 1):**
Result: Action wasted. No relations change.

**Church Govern T3 — Success (net 2, Ob 2):**
Result: Prosperity T3 +1.

**Hafenmark Muster — Partial (net 1, Ob 2):**
Result: Unit mustered at reduced Cohesion? Partial muster undefined. Treating as: unit mustered at Cohesion −1 (3 instead of 4 for Infantry).

**Varfell Parliamentary Manoeuvre — Success (net 2, Ob 2):**
Result: One Crown pending Domain Action delayed 1 season.

**Guilds Community Organising — Failure (net 0, Ob 2):**
Result: Action wasted. No progress.

**Varfell Thread Op — Success (net 3, Ob 2):**
Result: RS −1 → RS 70. Thread Debt in T9.

**S3 State (Run A):** RS 70. Hafenmark new unit (Cohesion 3). Crown action delayed. Prosperity T3+1. Everything else unchanged from S2.

---

### Season 4

**Crown Decree — Partial (net 1, Ob 2):**
Result: Reduced effect Decree (undefined; treating as half effect — which is meaningless for a Decree). Essentially nothing happens at Partial for Decree in current rules.

**Church Muster Templar — Success (net 3, Ob 3):**
Result: Templar unit mustered. Church Military effective strength +1 unit.

**Hafenmark Parliamentary Manoeuvre — Partial (net 1, Ob 2):**
Result: Current rules (PP-170): Partial = no effect.

**Crown Govern T2 — Success (net 2, Ob 2):**
Result: Prosperity T2 +1.

**Guilds Trade — Partial (net 1, Ob 2):**
Result: Partial Trade. Wealth +0 (reduced; undefined — treating as no Wealth gain since Partial in Trade is unclear).

**Church Diplomacy — Success (net 2, Ob 2):**
Result: Diplomatic agreement with Guilds. Guilds Standing +1.

**S4 Final State (Run A — No FF):**

| Faction | Mandate | Wealth | Military | Stability | Notes |
|---------|---------|--------|----------|-----------|-------|
| Crown | 4 (−1) | 4 | 4 + unit in T5 | 4 | Deed 1 at risk (Mandate <5) |
| Church | 6 (+1) | 6 (+1) | 4 + Templar | 5 | Theocracy Counter 28 (no advance) |
| Hafenmark | 4 | 7 (ceiling, +2) | 3 + new unit Coh3 | 4 | Wealth capped |
| Varfell | 4 | 3 | 3 | 4 | Intel on Church; Thread Debt T9 |
| Guilds | 3 | 3 | 3 | 4 | Standing +1 |

RS: 70 (−2). Public Instability: 5 (unchanged). Institutional Pressure: 20 (unchanged).

**Run A narrative assessment:** The board is relatively static. Three faction Failures (Crown Govern, Hafenmark Diplomacy, Varfell Investigate, Guilds Community Organising x2) produced zero state changes. The Partial outcomes also produced minimal change (undefined effects defaulted to zero or minimal). The Church is clearly ahead due to two clean successes (Trade, Decree, Thread Op, Diplomacy). The game has little inter-faction tension — most factions are doing their own thing independently, and Failure is a speed bump, not a consequence.

---

## RUN B: WITH FAIL FORWARD (PP-177 Active)

### Season 1

**Crown Govern (T1) — Failure (Moderate complication):**
Complication: Prosperity −1 in T1 (T1 was 4 → now 3).
Effect: Crown's economic base takes an immediate hit. This makes the Crown's next Trade or Govern action more urgent.

**Church Trade — Success (unchanged):**
Church Wealth 6. No complication.

**Hafenmark Diplomacy (vs Guilds) — Failure (Moderate complication):**
Complication: Guilds gain Casus Belli vs Hafenmark (failed diplomacy: insult perceived).
Effect: Guilds now have a legitimate military grievance. This creates a new strategic axis — Guilds vs Hafenmark — that didn't exist before.

**Varfell Spy — Success (unchanged):**
Church intel revealed.

**Guilds Trade — Failure (Moderate complication):**
Complication: Guilds Wealth −1 → Guilds Wealth 2. (Materials wasted on failed trade mission.)
Effect: Guilds are now financially strained, which makes the Casus Belli against Hafenmark more interesting — they have grievance but weakened military capacity.

**Crown Military March — Success (unchanged):**
Crown unit in T5.

**S1 State changes (Run B):** Church Wealth 6, Varfell gains Church intel, Crown unit T5. NEW: Prosperity T1 −1 (→3), Guilds gain Casus Belli vs Hafenmark, Guilds Wealth −1 (→2). Board has active tension between Guilds and Hafenmark that wasn't present before.

---

### Season 2

**Crown Govern T1 — Partial (Minor complication — player choice):**
Crown chooses: Public Instability +1 (prefers to protect Standing for Deed checks).
Effect: Public Instability 6. Parliament slightly energised. Prosperity T1 +1 (goal achieved despite complication).

**Church Decree — Overwhelming (unchanged):**
Crown Mandate −1 → 4. Overwhelming bonus: Mandate +1? See PP-177 gap for Overwhelming bonuses on Decree — defer to ED-063b. Apply Success effect only: Crown Mandate 4.

**Hafenmark Trade — Overwhelming (unchanged):**
Hafenmark Wealth 7 (ceiling). Same as Run A.

**Varfell Investigate — Failure (Moderate complication):**
Complication: Stability −1 → Varfell Stability 3. (Internal leaks suspected — investigation compromised.)
Effect: Varfell is now vulnerable. Stability 3 means one more hostile action puts them at risk. This creates pressure on Varfell to act defensively, changing their strategy.

**Guilds Govern T8 — Partial (Minor complication — player choice):**
Guilds chooses: Standing −1 (protects Public Instability — Guilds are watching Parliament closely given Casus Belli).
Guilds Standing: was 4 → now 3. Prosperity T8 +1 (goal achieved).

**Church Thread Op — Success (unchanged):**
RS 71. Thread Debt T3.

**S2 State (Run B):** Crown Mandate 4, PI 6, Church Wealth 6, Mandate 6, Hafenmark Wealth 7, Varfell Stability 3 (−1), Guilds Standing 3 (−1), RS 71. Much more active state.

---

### Season 3

**Crown Diplomacy (vs Church) — Failure (Moderate complication):**
Complication: Church gains Casus Belli vs Crown.
Effect: Church now has a formal grievance against Crown. Combined with Crown Mandate already reduced and Church Mandate at 6, this is a serious pressure point. Church may march on Crown territory next season.

**Church Govern T3 — Success (unchanged):**
Prosperity T3 +1.

**Hafenmark Muster — Partial (Minor complication — player choice):**
Hafenmark chooses: Unit mustered at Cohesion −1 (Cohesion 3). Accepts the reduced quality unit rather than risk Standing loss.

**Varfell Parliamentary Manoeuvre — Success (unchanged):**
Crown action delayed.

**Guilds Community Organising — Failure (Moderate complication):**
Complication: +1 Ob to next Community action in any Guilds territory.
Effect: Guilds are now blocked from Community Organising next season at standard Ob. This represents organised opposition to the Guilds' community efforts — possibly Church-backed given Theocracy Counter trajectory.

**Varfell Thread Op — Success (unchanged):**
RS 70. Thread Debt T9.

**S3 State (Run B):** Church Casus Belli vs Crown, RS 70, Varfell Stability 3, Guilds Community +1 Ob next, Hafenmark unit Coh 3. Crown is under growing pressure from two directions: Crown Mandate 4, Church Casus Belli, Crown action delayed.

---

### Season 4

**Crown Decree — Partial (Minor complication — player choice):**
Crown chooses: Public Instability +1 (PI now 7). Decree effect: partial (treated as reduced — half effect; Decree targets Church Influence: Influence −0.5 → treated as no Influence change; only narrative effect).
Effect: PI at 7 = Parliamentary Manoeuvre −1 Ob (PP-170). Hafenmark and Varfell now have easier access to Parliamentary actions. Crown's failed Decree has energised Parliament against them.

**Church Muster Templar — Success (unchanged):**
Templar unit. Church military strength +1.

**Hafenmark Parliamentary Manoeuvre — Partial (Minor complication — player choice):**
Under FF: Partial = no delay effect; Minor fires. Hafenmark chooses Standing −1 (Standing 4 → 3) as minor.
Effect: Hafenmark Standing reduced — this matters for Deed 1 check (Mandate ≥ 4 and no Heresy Investigation). They can absorb Standing loss but not Mandate loss.

**Crown Govern T2 — Success (unchanged):**
Prosperity T2 +1.

**Guilds Trade — Partial (Minor complication — player choice):**
Guilds choose Standing −1 (Standing 3 → 2). Wealth: Partial Trade = +1 Wealth (half of full +2 Overwhelming; or treat Partial as 0 gain with goal partially achieved = +1 Wealth narratively). Guilds Wealth 3 (from 2).
Effect: Guilds recovering financially, but Standing now at 2 — their credibility in Parliament is diminishing. Combined with Casus Belli vs Hafenmark, they're in a complicated position.

**Church Diplomacy — Success (unchanged):**
Guilds Standing +1 → Guilds Standing 3. Church-Guilds alignment forming.

**S4 Final State (Run B — With FF):**

| Faction | Mandate | Wealth | Military | Stability | Standing | Notes |
|---------|---------|--------|----------|-----------|----------|-------|
| Crown | 4 (−1) | 4 | 4 + T5 unit | 4 | 5 | PI 7; Church Casus Belli active; action delayed S3 |
| Church | 6 (+1) | 6 (+1) | 4 + Templar | 5 | — | Theocracy Counter 28; Casus Belli vs Crown |
| Hafenmark | 4 | 7 (ceiling) | 3 + Coh3 unit | 4 | 3 (−1) | Casus Belli from Guilds active |
| Varfell | 4 | 3 | 3 | 3 (−1) | — | Thread Debt T9; community +1Ob next |
| Guilds | 3 | 3 | 3 | 4 | 3 (−1) | Casus Belli vs Hafenmark; recovering from Wealth shock |

RS: 70 (−2). Public Instability: 7 (+2). Institutional Pressure: 20 (unchanged).

---

## COMPARATIVE ANALYSIS

### Board State Delta (Run A vs Run B after 4 seasons)

| Metric | Run A (No FF) | Run B (With FF) |
|--------|--------------|-----------------|
| Active Casus Belli | 0 | 2 (Church→Crown; Guilds→Hafenmark) |
| Stability changes | 0 | −1 (Varfell) |
| Standing changes | 0 | −2 (Hafenmark, Guilds) |
| Public Instability | 5 (unchanged) | 7 (+2) — Parliamentary pressure active |
| Prosperity changes | +3 (T1+1, T2+1, T8+1) | +3 (same) + T1 Prosperity temporarily dipped S1 |
| Faction positioning change | Crown/Church diverging; rest static | Active Church-Guilds axis forming; Crown under pressure; Guilds-Hafenmark tension |
| Decisions deferred by Failure | 5 (all failure=nothing) | 0 (all failures produce state change) |
| New strategic axes opened | 0 | 2 (Church-Crown; Guilds-Hafenmark) |
| Emergent narrative content | Minimal: Church ahead, others stagnant | Rich: 3-way tension (Church dominance vs Crown pressure vs Guilds-Hafenmark rivalry) |

---

## EMERGENT GAMEPLAY ASSESSMENT

### Run A (No FF) — Emergent Gameplay Score: LOW

- 5 Failure outcomes produced zero state changes. Players who failed simply "missed a turn." No consequences to navigate.
- Partial outcomes also produced minimal change (undefined effects, defaulted to zero or trivial).
- The game state after 4 seasons is a simple Church-ahead scenario with no active inter-faction tensions. 
- **Strategic depth:** Players with poor rolls have no interesting choices — they just lose initiative. Nothing forces re-evaluation of strategy.
- **Narrative content generated:** Church got stronger. Everyone else trod water. No stories emerged from the failed actions.
- **Replayability:** High similarity expected across runs — failures are informationally inert.

### Run B (With FF) — Emergent Gameplay Score: HIGH

- Every Failure produced a concrete consequence that changed the board. Players who failed still had to respond to the consequences.
- Partial choices created faction-character moments (Crown accepting PI increase to protect Standing; Guilds accepting Standing loss to protect PI).
- Two new inter-faction tensions emerged (Church-Crown; Guilds-Hafenmark) that will define the next 4 seasons — neither existed at game start.
- Varfell's Stability drop creates vulnerability that other factions can now exploit.
- Parliament is now at PI 7 — the Parliamentary Manoeuvre action is more available, which draws more factions into parliamentary play.
- **Strategic depth:** Players with poor rolls must respond to complications. The complication creates a new decision: address it, exploit a rival's complication, or push toward their own objectives. Richer decision set.
- **Narrative content generated:** A failed diplomacy created a military grievance. A failed govern created prosperity damage. A failed investigate created a security breach. Each maps onto a plausible in-world story.
- **Replayability:** High variance expected — different roll sequences create different tension axes.

### Verdict: FF is superior for emergent gameplay.

The comparison is unambiguous. Five zero-consequence Failures in Run A vs five state-changing complications in Run B. The complication choices (Minor Partial) also create faction-voice moments that BG currently lacks — a faction's decision about which Minor consequence to accept reveals its priorities.

One nuance: **FF increases the speed of board state degradation.** Rendering Stability is identical (both RS 70) but Stability, Standing, and PI all declined in Run B. In a 12-season game this compounds. The question is whether this creates appropriate pressure or accelerates the game unsatisfyingly. Assessment: appropriate — the complications are proportionate and recoverable. A Stability −1 is serious but not catastrophic; a Casus Belli can be managed diplomatically.

---

## EDGE CASE FINDINGS

### Edge Case 1: Multiple simultaneous Failures (S1)
Two Failures fire in S1 (Crown Govern, Guilds Trade). Both complications apply simultaneously. No interaction problem — they affect different stats/territories.

### Edge Case 2: Partial with undefined base effect (Govern)
Govern Partial: goal achieved = Prosperity +1. Complication = Minor. This requires defining what "Govern Partial" means as a base success. Current BG spec doesn't state this. Ruling: Govern Partial = Prosperity +1 (half of the Govern outcome — Prosperity was presumably +1 on Success, which is what's implied; Overwhelming = +2). [GAP: confirm Govern Success/Overwhelming distinction in BG — currently the Govern table doesn't differentiate.]

### Edge Case 3: Overwhelming bonuses for Domain Actions
Church Decree Overwhelming: bonus undefined. Current spec states Overwhelming = Ob+1 surplus only, no bonus action. Consistent — Decree Overwhelming produces Success effect plus narrative weight. No FF interaction.

### Edge Case 4: Casus Belli from Diplomacy Failure stacking
If two Diplomacy Failures target the same faction, do they each grant Casus Belli? Rule: One Casus Belli per faction at a time (existing rule). Second failure: existing Casus Belli is refreshed (expiry timer resets). No doubling.

### Edge Case 5: Varfell Stability 3 — not a crisis, but creates pressure
Stability 3 is not at the collapse threshold (0). But if Varfell takes one more hostile Domain Action targeting their Stability, and they have no counter, they could reach 2 which is within collapse range. This is exactly the intended pressure FF creates.

---

## FINDINGS SUMMARY

| Finding | Type | Action |
|---------|------|--------|
| FF produces significantly richer emergent gameplay | Design confirmation | Adopt PP-177 |
| Govern Partial base effect undefined in BG | GAP | [GAP: BG-FF-01 — Govern Partial base effect: Success = Prosperity +1; Partial = Prosperity +1 with Minor complication. Confirm.] |
| Overwhelming bonus for Domain Actions undefined | GAP | [GAP: BG-FF-02 — Domain Action Overwhelming bonus undefined. Treat as Success effect + narrative; no mechanical bonus beyond Partial complication waived.] |
| Partial choice adds faction-character voice | Design benefit | Retain player choice on Partial |
| 4-season compounding is acceptable | Balance confirmed | No adjustment needed |
| Parliamentary Manoeuvre Partial FF update conflicts with PP-170 "no effect" ruling | Conflict resolved | PP-177 supersedes PP-170 Partial clause; Partial now Minor complication (player choice) |

---

## EDITORIAL ITEMS (all self-resolved, flagged for review)

- [EDITORIAL: ED-085 — BG Govern Partial base effect: Prosperity +1 with Minor complication. Confirm Govern Success = Prosperity +1 (current spec implies +1 but not stated as the full-success value). PROVISIONAL — flagged for user review.]
- [EDITORIAL: ED-086 — Domain Action Overwhelming bonus undefined in BG. Provisional ruling: Success effect only; no additional mechanical bonus. Overwhelming = better margin, no extra effect unless explicitly stated per action. Flagged for user review.]
- [EDITORIAL: ED-087 — Parliamentary Manoeuvre Partial: PP-170 stated "no effect." PP-177 overrides to Minor complication (player choice of Standing −1 or no effect). Net result: player can still choose "no effect" at Partial — PP-170 is preserved as a menu option. No conflict. PROVISIONAL.]

