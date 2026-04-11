# Baralta Crown Claim — BG Mechanic Design
## Status: DESIGN (editorial decision, flagged for review)
## Date: 2026-04-11
## Resolves: Mechanical gap — no BG path for Hafenmark to claim the Crown despite deed-logic supporting Baralta as strongest candidate
## Affects: params_board_game.md, worldbuilding_integration_v3.md (Named Character Event Cards)

---

## 1. The Gap

Current BG succession mechanics route Crown elimination exclusively to Löwenritter:
- Crown eliminated → Torben Loyalty transfers to Löwenritter (PP-494)
- Coup Counter 4 → coup fires (PP-194)
- Royal Deposition (PI ≥ 5 + Church Mandate ≥ 5 + Crown Mandate ≤ 1 + 2 Standing tokens) → Crown to Löwenritter or emergency Parliament

No mechanism exists for Hafenmark/Baralta to claim the Crown. The deed-monarchy's own logic (established 2026-04-11 session) says Baralta is the strongest succession candidate by governance metrics. The BG system should reflect this.

## 2. Design: Crown Succession Contest

**[EDITORIAL DECISION: ED-408 — Crown Succession Contest mechanic. Flagged for review.]**

### Trigger

Fires when ANY of the following occur:
- Crown faction is eliminated (Mandate 0 + Loyalty 0)
- Royal Deposition succeeds
- Ehrenwall Coup fires (Coup Counter 4) AND Ehrenwall does not claim the Crown for Löwenritter directly

### Contest Mechanics

When the trigger fires, a Succession Contest opens at the next Accounting. All major factions with Mandate ≥ 3 may stake a claim. Expected candidates:

| Candidate | Claim Basis | Pool | Condition |
|-----------|------------|------|-----------|
| Löwenritter | Military authority + institutional loyalty | Military 5 + Stability | Coup Counter ≥ 3 (has been building toward this) |
| Hafenmark | Deed-claim + parliamentary authority | Mandate + Influence | Baralta alive + Hafenmark Mandate ≥ 4 |
| Church | Consecration authority (refuse all candidates, claim regency) | Mandate + Influence | TC ≥ 40 (theocratic threshold — Church only claims if already dominant) |

**Resolution:** Each claiming faction rolls their pool vs Ob 3 (TN 7). Highest net successes wins. Ties: Löwenritter wins military ties (they have the army). Hafenmark wins political ties (they have parliamentary legitimacy).

**If Hafenmark wins: Consecration Crisis fires (see §3).**
**If Löwenritter wins: Standard coup outcome. Baralta remains Duchess. Ehrenwall's conditional support per ED-406 does not apply (she claimed the Crown herself).**
**If Church wins: Theocratic regency. TC +10. All factions face Stability check Ob 2.**

### Baralta Claim Precondition (Active Positioning)

**[EDITORIAL DECISION: ED-409 — Baralta Claim Precondition Domain Action. Flagged for review.]**

Hafenmark may take a Domain Action during any Council Phase: **Stake Claim** (Senator Outward targeting Crown).

- **Preconditions:** Crown Mandate ≤ 2 AND PI ≥ 5 AND Baralta alive
- **Pool:** Hafenmark Mandate + Influence (4 + 4 = 8D at game start)
- **Ob:** Crown Mandate + 1 (minimum Ob 2)
- **Success:** Hafenmark places a Claim Token on the Crown faction mat. This token does three things:
  1. When Crown Succession Contest fires, Hafenmark gets +2D on the contest roll (positioned claim)
  2. Ehrenwall's Coup Counter assessment now includes Baralta as a succession option (per ED-406 — Ehrenwall evaluates conditionally)
  3. Church becomes aware of Baralta's Crown ambition (if not already) — Himlensendt begins internal assessment
- **Failure:** Hafenmark Stability −1 (overreach exposed). Claim attempt cannot be repeated for 2 seasons.

**Design rationale:** The Stake Claim action makes Baralta's Crown ambition a BG-legible strategic move, not just a background characterisation. Hafenmark players can choose to pursue it or not. The preconditions (Crown Mandate ≤ 2, PI ≥ 5) ensure it only fires when Crown is genuinely weakened — Baralta does not move against a strong Crown.

## 3. Consecration Crisis Mechanic (BG Expression of ED-407)

**[EDITORIAL DECISION: ED-410 — Consecration Crisis as BG event. Flagged for review.]**

### Trigger
Hafenmark wins Crown Succession Contest.

### Resolution
Check Church Stability at the moment Hafenmark wins:

**Church Stability ≥ 4: Himlensendt Refuses Consecration.**
- TC +3 (Church overreach visible)
- Crown Mandate inherited by Hafenmark at −2 (unconsecrated ruler penalty)
- Baralta rules without theological blessing
- If Baralta governs successfully for 3 consecutive seasons without Church consecration (Mandate does not drop below 3): deed-logic is validated without Church blessing. Church legitimation role permanently diminished — TC passive advance reduced to +0.5/season (the population has seen that the Crown functions without Church sanction)
- If Baralta's Mandate drops below 3 during the 3-season window: unconsecrated rule fails. Succession Contest reopens. Baralta is excluded (deed-claim rebutted by performance failure).

**Church Stability ≤ 3: Himlensendt Consecrates Under Duress.**
- TC −5 (sovereign supremacy enacted)
- Church Stability −3 (institutional trauma)
- At Stability 0: Church anti-death-spiral floor applies — Stability cannot drop below 0, but at 0 the Church is functionally a subordinate institution for remainder of game
- Baralta takes Crown with full consecration. Crown Mandate inherited at full value.
- Baralta immediately gains the Sovereign Authority Doctrine as a Crown action (not just Hafenmark unique action) — usable once per season, not once per arc

**Override: Arc 11 Originary Lock Encounter.**
If Himlensendt has experienced the originary Lock encounter before the Succession Contest fires:
- GM discretion. Himlensendt's personal faith state determines the consecration outcome regardless of Church Stability.
- This override exists because a faith-fractured Himlensendt is a qualitatively different decision-maker than a faith-intact one. No mechanical formula can capture this.

## 4. Consecration Crisis Simulation

### Scenario A: Church Stability 5 (game start value), Hafenmark wins Succession Contest early (Season 3-4)

Early game. Church is confident. Himlensendt refuses. Baralta rules unconsecrated.

- Crown Mandate inherited at −2 = Crown Mandate 3 (if Crown was at 5 minus the erosion that caused the contest, probably 1-2, so Baralta inherits 1-2 minus 2 = floor of 1)
- Problem: Baralta starts with Mandate 1 as Queen. Her Hafenmark Mandate 4 does not transfer (she is now Crown, not Hafenmark). She needs 3 consecutive seasons above Mandate 3 to validate unconsecrated rule.
- At Mandate 1, this is nearly impossible without massive player support.
- **Assessment: early-game unconsecrated claim is a trap.** The deed-logic says Baralta should rule, but without consecration her starting position is catastrophically weak. This is balanced — the system punishes premature claims.

### Scenario B: Church Stability 3, Hafenmark wins Succession Contest mid-game (Season 8-10)

Mid-game. Church weakened by Olafsson exposure, Klapp fracture, or Jarnstal drift. Himlensendt consecrates under duress.

- TC −5. If TC was at 35-40 range, drops to 30-35. Significant reduction.
- Church Stability 3 → 0. Church functionally subordinated.
- Baralta takes Crown with full Mandate inheritance + Sovereign Authority Doctrine as Crown action.
- **Assessment: mid-game consecration is Baralta's optimal window.** Church is weakened enough to force consecration but still has enough institutional presence that consecration is meaningful. TC reduction is significant. Church subordination is permanent.

### Scenario C: Church Stability 4, Hafenmark wins Succession Contest late-game (Season 14+)

Late game. Church battered but holding floor. Himlensendt refuses.

- Baralta rules unconsecrated with higher Crown Mandate (Crown Mandate was probably 2-3 before contest, so she inherits 0-1 after penalty).
- But late-game, other factions are also weakened. Baralta at Mandate 1 in a field where everyone is at 2-3 is relatively less disadvantaged.
- 3-season validation window: at this stage, 3 seasons may be all that remains in the campaign. The unconsecrated rule either validates before game end (in which case Baralta wins on points) or fails to validate (in which case the succession reopens into endgame chaos).
- **Assessment: late-game unconsecrated claim is a gamble.** High risk, high reward. The deed-logic's ultimate test — can you prove you earned the throne by governing without any theological backing at all?

### Simulation Conclusion

The Church Stability threshold produces balanced outcomes:
- **Stability ≥ 4 (refusal):** Baralta faces a severe penalty that makes early claims unviable and late claims dramatic gambles. The system correctly punishes moves without proper preparation.
- **Stability ≤ 3 (consecration):** Baralta gets full legitimacy but only after the Church has been sufficiently weakened — meaning players invested significant effort to create the conditions. The reward is proportional to the investment.
- **The strategic sweet spot for Baralta:** weaken the Church to Stability 3 before claiming. This means Baralta-aligned players have an incentive to help degrade Church Stability — which puts them in tension with their own TC suppression interest (weakening the Church raises TC in the short term even though Baralta's eventual Crown claim would reduce it via sovereign supremacy).

This tension — needing the Church weak enough to force consecration but not wanting TC to spike in the interim — is good design. It creates a multi-season strategic calculation.

## 5. Hafenmark Succession After Baralta Takes Crown

**[EDITORIAL DECISION: ED-411 — Hafenmark faction status when Baralta takes Crown. Flagged for review.]**

If Baralta takes the Crown, what happens to Hafenmark?

Option A: **Hafenmark merges with Crown.** Baralta brings Hafenmark's institutional apparatus into the Crown faction. Hafenmark ceases to exist as a separate faction. Crown inherits Hafenmark's parliamentary apparatus, Wealth 5 (highest non-Guilds), and territorial control. But Crown also inherits Hafenmark's enemies and the PP-487 succession fragility — Hafenmark without Baralta fractures, and now Crown without Baralta fractures the same way.

Option B: **Hafenmark persists as a separate faction under institutional successor.** Baralta leaves Hafenmark to govern the Crown. Hafenmark's PP-487 PI-gated succession fires immediately. At PI ≥ 4: institutional successor takes over, Hafenmark continues as an NPC-controlled faction allied with Crown. At PI < 4: Hafenmark fractures, Crown loses the institutional base that produced Baralta.

**[EDITORIAL DECISION: Option B is mechanically richer.** It forces Baralta players to ensure Hafenmark PI ≥ 4 before claiming the Crown — otherwise their faction base collapses behind them. This creates another preparation requirement alongside the Church Stability targeting. Baralta's Crown claim is viable only when: Crown is weak (Mandate ≤ 2), PI ≥ 5 (Parliament functional), Church Stability ≤ 3 (consecration available), AND Hafenmark PI ≥ 4 (institutional succession stable). Four conditions, all achievable, none trivial.]

---

## 6. Editorial Items Created

| ID | Description | Priority | Status |
|----|-------------|----------|--------|
| ED-408 | Crown Succession Contest mechanic — multi-faction contest when Crown fails | P1 | Decision made, flagged for review |
| ED-409 | Baralta Claim Precondition (Stake Claim Domain Action) | P1 | Decision made, flagged for review |
| ED-410 | Consecration Crisis as BG event — Church Stability conditional | P1 | Decision made, flagged for review |
| ED-411 | Hafenmark faction status when Baralta takes Crown — Option B (Hafenmark persists, PP-487 fires) | P2 | Decision made, flagged for review |

---

*End of mechanic design. All decisions flagged for user review.*
