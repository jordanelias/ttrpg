# SIM-NEW-02 — BG: Partition Victory (Church + Hafenmark)
## Mode: C (Full Scenario) + A (Isolation) + J (Precedent)
## Date: 2026-04-08

---

## FETCH LOG
canonical_sources.yaml: ✓ (156 lines)
params_board_game.md: ✓ (1431 lines)
victory_architecture_v1.md: ✓ (412 lines)

---

## Partition Conditions (§3.2)

Fires immediately on mutual declaration at Accounting (no 2-step hold):
- Crown Mandate ≤ 1
- TC ≥ 50
- Church controls ≥ 2 territories
- Hafenmark controls ≥ 3 territories
- No active military conflict between Church and Hafenmark this season

**Partition outcome:** Mutual conditional victory. Both factions score. Game ends.

---

## Mode A: Condition Reachability

**Starting state:** Crown M5, TC 28.

**Crown Mandate → ≤ 1 pathway:**
- Royal Deposition mechanic (PP-194): fires if PI ≥ 5, Church M ≥ 5, Crown M ≤ 1, and ≥ 2 factions have Standing tokens against Crown. But Crown Mandate reaching ≤ 1 is itself required — so Deposition accelerates the endgame but doesn't create Mandate reduction on its own.
- Decree chain: Hafenmark plays Decree targeting Crown Mandate. Crown M 5 → 4 → 3 → 2 → 1. At consecutive Ob penalties (Ob 2→3→4→5): takes 4–6 seasons with success probabilities ~85%, ~69%, ~42%, ~27%. Expected seasons to Crown M ≤ 1: ~5–7 seasons if Hafenmark dedicates Decree chain.
- Church assists: Church plays Excommunication (Crown Mandate −1 on success). Combined Hafenmark Decree + Church Excommunication: Crown M drops 2 per season at peak, reaching ≤ 1 within 3 seasons.

**TC → ≥ 50 pathway:**
TC starts at 28. From baseline: +1/season passive. If AER 3 bypasses structural suppression: +1/season. If Church Asserts: +2/season replacing passive. 
Seasons to TC 50 from 28: (50-28)÷1 = 22 seasons at +1/season. At +2/season (Assert): 11 seasons.

**Finding P1 — TC ≥ 50 is the binding constraint.** Crown Mandate ≤ 1 can be achieved in 3–7 seasons with Church+Hafenmark coordination, but TC 50 takes 11–22 seasons depending on Assert frequency. Partition is a mid-to-late-game win condition, not an early rush.

**Simultaneous bottleneck:** Hafenmark needs TC ≥ 50 to fire Partition, but they also suppress TC to prevent Church winning via Theocracy. Strategic contradiction: Hafenmark must choose between suppressing TC (prevents Church primary win) and letting TC rise (enables Partition). The optimal Hafenmark strategy is: suppress TC until Crown is eliminated below M ≤ 1, then stop suppressing and let TC climb toward 50.

---

## Mode C: Full Scenario — Partition Race

### Seasons 1–8: Setup Phase

Church and Hafenmark operate as a loose coalition without explicit coordination (no rule allows a coalition declaration — this is emergent behaviour).

**Church:** Plays Assert every season (TC +2 replacing passive). At AER 3 (Temperance Focus): structural suppression bypassed. TC: 28 + (8 × 2) = **TC 44**.

**Hafenmark:** Does NOT play Parliamentary Challenge (structural suppression inactive due to AER 3, Challenge would be wasted on a mechanism already bypassed). Instead: Plays Decree targeting Crown M every season. After 4 Decree successes at degrading Ob: Crown M 5 → 4 → 3 → 2 → 1. Crown M ≤ 1 by **S5**.

**Varfell:** Building VTM, not suppressing TC (aligned with Church incidentally — Varfell benefits from TC pressure on Crown).

**Crown:** Playing Royal Decree against Church M, and Formal Crown Treaty to satisfy rivalry conditions. But with M collapsing, Crown Treaty attempts fail (Treaty Ob = target Mandate; Church M 5 = Ob 5 for Crown with M 4D: ~8% success).

**Hmm — problem:** Partition requires Church to control ≥ 2 territories. Church starts with T9 (1 territory). Church must seize a second territory BEFORE TC 75 triggers seizure mode. TC 44 at S8 — Church not yet in seizure mode. Church can still March normally. Church marches into T2 (Kronmark, Crown M ≤ 1 = can't resist). Church M 4D vs Crown M 1D. P(Church wins): >99%. T2 secured. Church TCV: 3+1 = 4, **controls 2 territories.**

**Hafenmark:** Controls T5 (Gransol ★), T7, T8, T10, T17 = 5 territories. ≥ 3 ✓.

**S8 state check:**
- Crown M ≤ 1: ✓ (M 1 by S5)
- TC ≥ 50: ✗ (TC 44 — need 6 more)
- Church ≥ 2 territories: ✓ (S8)
- Hafenmark ≥ 3 territories: ✓
- No Church/Hafenmark military conflict: ✓ (no overlap in expansion targets)

**TC gap:** 6 more TC needed. At +2/season (Assert): 3 more seasons.

### Seasons 9–11: Partition Window

**S9:** Assert → TC 46. All other conditions hold. No Partition yet.
**S10:** Assert → TC 48. No Partition.
**S11:** Assert → TC 50. **All conditions met.**

Church and Hafenmark declare Partition at S11 Accounting. Game ends. Church conditional victory (Theocratic control of southern territories). Hafenmark conditional victory (Parliamentary sovereignty of northern territories).

**Total game duration: 11 seasons.** Earliest possible Partition win.

---

## Mode A: What Blocks Partition

**Crown's counter-play:** Crown must stay above M ≤ 1 OR prevent TC ≥ 50 OR disrupt Church/Hafenmark territorial control.

Counter-play effectiveness:
1. **Stay above M ≤ 1:** Crown invests all Decrees in self-recovery (Mandate +1 requires Govern Overwhelming in own capital). Govern Ob = capital Prosperity ÷ 2 = T1 Prosperity 6 ÷ 2 = 3. Crown M 5D vs Ob 3: ~60% Overwhelming chance... but Overwhelming is required. At pool 5D Ob 3: P(Overwhelming ≥ 2×3 AND ≥3) = P(net ≥ 6 AND ≥ 3) ≈ 30%. Not reliable — Crown can barely recover Mandate while being Decree'd down.

2. **Suppress TC:** Crown plays Suppress (Mandate vs Ob = Church M = 5). Crown M 4D vs Ob 5: P(Success) ≈ 8%. Effectively impossible for weakened Crown.

3. **Disrupt Hafenmark territories:** Crown marches into Hafenmark territory. But Crown Military is weakened (Mandate-linked) and Hafenmark Military 3 + Fort in T5. Not viable with M ≤ 2.

**Finding P2 — Once Crown Mandate falls below 3, no viable counter-play for Crown remains.** Partition becomes unstoppable. The game effectively ends when Crown Mandate hits 3 (not 1), because below M 3, Crown cannot suppress TC, cannot recover Mandate reliably, and cannot project military force. The Partition win condition is achieved 2–3 seasons after M 3, not M 1.

---

## Mode J: Precedent and Gaps

**Gap 1 — No Partition notification mechanic.** Neither Church nor Hafenmark is required to declare intent to pursue Partition. Other players may not know Partition is being pursued. At S11 Accounting, the conditions fire and the game ends without warning. Other factions had no opportunity to disrupt.

**[EDITORIAL: ED-338 — Partition should have a public signal mechanic: when all conditions except TC ≥ 50 are met, a "Partition Pressure" marker is placed publicly. All factions know Partition fires next time TC reaches 50. This gives other factions 1 season to disrupt (raise Crown Mandate, lower TC, disrupt territorial control). Without this, Partition is invisible until it fires. P2.]**

**Gap 2 — Varfell and RM in Partition.** When Partition fires, Varfell and RM lose unconditionally. No consolation mechanic. Varfell has been building VTM for 11 seasons and gets nothing. Is this the intended outcome for the 5-player game?

**[EDITORIAL: ED-339 — Clarify non-Partition faction outcome: do Varfell/RM receive a consolation score, a narrative win condition, or simply lose outright? P3 — narrative question, not mechanical blocker.]**

---

## Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-PT-01 | P1 | TC ≥ 50 is the binding Partition constraint (11–22 seasons). Crown Mandate ≤ 1 achievable in 3–7. |
| F-PT-02 | P2 | Crown becomes unable to counter Partition at M ≤ 3, not M ≤ 1 — effective game end is 2–3 seasons earlier than the condition states. |
| F-PT-03 | P2 | Partition has no advance signal — fires invisibly at Accounting when conditions converge. Other factions get no warning. |
| F-PT-04 | P3 | Varfell and RM lose unconditionally under Partition with no consolation mechanic. |

