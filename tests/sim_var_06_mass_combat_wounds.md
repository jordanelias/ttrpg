# SIM-VAR-06 — TTRPG: Mass Combat Wound Cascade → Faction Domain Echo Chain
## Mode: C (Full Scenario) + D (Edge Cases) + B (Interaction Chain)
## Date: 2026-04-08 | Multi-register cascade: mass combat → personal wound → faction stat Domain Echo

---

## FETCH LOG
canonical_sources.yaml: ✓ (156 lines)
params_mass_combat.md: ✓ (500 lines)
params_core.md: ✓ (161 lines)
params_factions.md: ✓ (517 lines)
params_threadwork.md: ✓ (613 lines)

---

## Scenario

**TTRPG campaign arc.** A battlefield confrontation between Church Templar forces and a Crown expeditionary unit near T14 (Ehrenfeld). Named characters involved:

- **Crown PC: General Maret Elstov** — Coordination 5, Endurance 4, Health 10, Spirit 3, Attunement 2, TS 0 (non-practitioner). Combat pool: Agi 4 + History 2 + 3 = **9D**.
- **Church: Cardinal Jarnstal** (NPC, Cardinal of Fortitude) — Coordination 3, Endurance 3, Health 9. Commands Templar unit. Conviction: "The Church Militant is the will of Solmund made manifest."
- **Crown unit:** Size 6, Command 5, Discipline 4, Power 2. H = min(4,5)+0 = 4. Total Health = 24.
- **Templar unit:** Size 4, Command 4 (Jarnstal commands), Discipline 5, Power 3. Fort 1 (field fortification). H = min(5,4)+1 = 5. Total Health = 20.

---

## Mass Combat Turn 1

**Phase 1 — Strategy:**
Crown: Advance (Aggressive). Church: Hold (Defensive + Fort 1 → +1D defence).

**Phase 5 — Engagement:**

*Crown attacks:* Pool = min(6,5)+5 = 5+5 = **10D** vs Ob = Church Discipline÷2 = 5÷2 = 3 (round up). 
Roll: 10D vs Ob 3. E(net) = 5.72. P(Success ≥ 3): ~93%.
Result: **Overwhelming** (net 7, ≥ 6 and ≥ 3). +1 Momentum. Damage = 7 × (1+2) = **21 damage**.
Church Health = 20 − 21 = −1 → 0. Church Size = ⌊0÷5⌋ = 0. **Templar unit destroyed.**

*Church counter-attack (simultaneous):* Pool = min(4,4)+4+1 Fort = 4+4+1 = **9D** vs Crown Ob = Crown Discipline÷2 = 4÷2 = 2.
Roll: 9D vs Ob 2. E(net) = 5.15. P(Success): ~99%.
Result: **Success** (net 5). Damage = 5 × (1+3) = **20 damage**.
Crown Health = 24 − 20 = 4. Size = ⌊4÷4⌋ = **1** (reduced from Size 6 to Size 1 — catastrophic attrition).

**Phase 6 — Cascade:**

**Step 1: Apply all damage simultaneously.** (Already applied above in simultaneous resolution.)

**Step 2: Discipline check — Crown unit (Size 1, significant loss from 6).**
Discipline check Ob = magnitude of loss. Crown lost 5 Size points. Ob = 5 (capped at "Structural" = Ob 5). Pool: Discipline 4D vs Ob 5. P(Success at 4D vs Ob 5): ~8%. P(Failure): ~92%.
Result: **Failure.** Discipline check failed — unit breaks. Breaking unit: all remaining Size units rout. Crown unit **routed** (removed from field).

**Step 3: Morale check — Church (Templar destroyed, no surviving unit):** N/A, unit gone.

**Step 4: General action — Jarnstal personal action.**
Jarnstal's unit is destroyed. He is exposed. He chooses: **Challenge Maret Elstov to personal combat** (dramatic narrative — Jarnstal won't retreat, he advances on the Crown general personally).

**Step 5: Crown General Maret Elstov action.**
Crown unit routed. Maret is the last standing combatant on Crown's side. She accepts Jarnstal's challenge.

---

## Personal Combat: Maret Elstov vs Cardinal Jarnstal

**Maret:** CP 9D. TN 7. Health 10. Armour: medium (DR 1). Wounds: 0.
**Jarnstal:** CP = Coordination 3 + History 1 (Church Militant) + 3 = **7D**. Health 9. Armour: heavy (DR 2). Wounds: 0.

**Round 1:**
Both declare attack (simultaneous in personal combat).

*Maret attacks Jarnstal:* 9D vs Ob = Jarnstal Endurance÷2 = 1.5 → Ob 2 (minimum 1, but Endurance 3÷2=1.5 rounds to 2).
Roll: 9D vs Ob 2. E(net) = 5.15. Result: **Success** (net 4). Raw damage = net 4. Minus Jarnstal DR 2 = **2 damage**. Jarnstal Health 9 → 7. No Wound (7 > Endurance 3... wait: Wound threshold = Health ≤ Endurance? Or Wound at specific Health values?

**Wound threshold (params_core.md):** Health formula: Endurance + 6. Wound threshold: checked separately. From prior simulations: at Health ≤ Endurance (3), Wound triggers (−1D). Jarnstal Health 7 > 3: no Wound.

*Jarnstal attacks Maret:* 7D vs Ob = Maret Endurance÷2 = 4÷2 = 2.
Roll: 7D vs Ob 2. E(net) = 4.0. Result: **Overwhelming** (net 8 — rolled well: ≥ 4 and ≥ 3). +1 Momentum. Raw damage = 8. Minus Maret DR 1 = **7 damage**. Maret Health 10 → 3. Wound threshold (Health ≤ Endurance 4): Health 3 ≤ 4 → **Maret takes Wound 1.** −1D to Maret's pool: 9D → 8D.

**Round 2:**
*Maret (8D) attacks Jarnstal:* 8D vs Ob 2. E(net) = 4.6. Result: **Success** (net 4). Damage = 4 − DR2 = 2. Jarnstal Health 7 → 5. Still > 3: no Wound.

*Jarnstal (7D, +1 Momentum from Round 1) attacks Maret:* 7D vs Ob 2. Spends Momentum (1 Momentum = 1 auto-success, non-Thread). Effective net = 7D roll + 1. E(net + 1) = 5.0. Result: **Success** (net 5, after Momentum). Damage = 5 − DR1 = 4. Maret Health 3 → **−1 = 0.** Maret at Health 0.

**Maret at Health 0 — character consequences:**
Health 0 = character incapacitated (cannot act). Must make Endurance check (Ob 2, TN 7) or fall unconscious.
4D vs Ob 2. P(Success): ~85%. Result: **Success.** Maret stays conscious but incapacitated (prone, cannot attack).

**Wound 2 triggered at Health 0:** Second Wound. −1D again: 8D → 7D. Wound 2: character is "badly wounded" — see params for consequences. Multiple Wounds: additional Ob penalties to non-combat actions.

**Jarnstal does not deliver killing blow.** Church NPCs (per NPC AI): Appease if Mandate ≥ 4 AND Stability ≤ 3. Jarnstal is a Cardinal — does he kill a downed enemy general? Ruling: Jarnstal plays for political value. He takes Maret prisoner rather than killing her. This is a major narrative event.

---

## Mode B: Wound Cascade → Domain Echo Chain

**Chain: Mass combat Crown rout → Maret captured → Domain Echo cascade**

**Step 1 — Military consequence:**
Crown unit routed (eliminated). BG-equivalent: Crown Military −1 (unit lost in battle).

**Step 2 — Named commander captured (Maret):**
No BG rule defines the captured general consequence. Gap:

**[EDITORIAL: ED-334 — Captured general rules: when a named PC General is captured in TTRPG mass combat, what is the BG-layer consequence? Options: (a) Faction Military −1 additional (no general = reduced command efficiency), (b) Crown loses ability to play Legionary card for 1 season (general absent), (c) Church/captor gains +1 Influence (political leverage). P2 — required for Hybrid mode cross-register resolution.]**

Gap-fill ruling: Crown loses Legionary card for 1 season (Maret is the commander, other officers don't have her authority). This means Crown cannot March or Muster for 1 season.

**Step 3 — Church captures a Crown general (Domain Echo candidate):**
Cardinal Jarnstal taking Maret prisoner is a political-scale event. Does this queue as a Domain Echo?

From state_transfer_spec.md: "PC Domain Action in scene → Queue as Domain Echo; fires at next Accounting." But Jarnstal's action (capturing Maret) is not Maret's Domain Action — it's an NPC action. Domain Echoes fire from PC Domain Actions, not NPC actions.

**Ruling:** Jarnstal capturing Maret is NOT a Domain Echo by strict interpretation. However, the narrative consequence (Crown general in Church custody) creates pressure events at next Accounting:
- Crown Mandate −1 (morale blow — general captured, unit destroyed).
- Church Influence +1 (political leverage — they hold a Crown general).

These fire as narrative Accounting consequences at Game Master discretion, not as Domain Echo mechanics. **No mechanical Domain Echo rule covers NPC-initiated capture events.**

**[EDITORIAL: ED-335 — NPC-initiated capture or assassination of a named PC should trigger a specific Accounting consequence (faction stat change) independent of the Domain Echo system. Currently no rule covers this. Recommend: "Command Event" — when a named PC of faction X is captured, incapacitated, or killed by another faction's NPC, apply at next Accounting: X Mandate −1, capturing faction Influence +1. P2.]**

**Step 4 — Maret's Wounds: long-term consequence**
Maret has 2 Wounds. From params_core / params_combat:
- Wound 1: −1D to all rolls.
- Wound 2: −1D additional (cumulative: −2D total) + Ob +1 to non-combat tasks (pain and impairment).
- Recovery: Wound 1 heals with rest (1 scene no combat). Wound 2 requires a healer (Cognition Ob 2) OR 1 full arc rest.

While Maret is Church prisoner: no access to Crown healers. Wound 2 persists until escape, negotiation, or ransom.

**Step 5 — Ransom chain (emerging scenario):**
Church holds Maret. Crown wants her back. Exchange options:
1. **Ransom:** Crown pays Wealth to Church. No defined ransom formula. **[GAP: No ransom mechanic defined. Gap-fill: Wealth equal to Maret's Mandate-contribution value — roughly 2 Wealth for a named general.]**
2. **Exchange:** Crown offers a political concession (TC −1, or Crown withdraws from T14). 
3. **Rescue mission:** PC-level operation. Tribune Investigate in Church territory to locate Maret (Ob 2+2 Inquisitor = Ob 4 in T9). Rescue is a full Zoom In scene.

The ransom/rescue creates a multi-session arc that emerged organically from the mass combat outcome. This is the intended Hybrid play pattern — battlefield outcomes cascade into political and personal arcs.

---

## Mode D: Edge Cases

**Edge 1: Crown unit reaches Size 0 but Maret survives.**
After unit destruction, does Maret take damage from the rout? No rule — ruling: she withdraws with the routing survivors. No additional personal damage from mass combat unit destruction (she was not directly targeted by unit attacks — unit vs unit is abstracted).

**Edge 2: Jarnstal killed instead of captured.**
If Maret had won personal combat (alternative scenario):
- Jarnstal Health 0, killed. Church loses Cardinal of Fortitude.
- Church Cardinal of Fortitude absent → Templar deployment requires Fortitude Focus each season (PP-430 Cardinal Focus: without Cardinal, focus unavailable; Templar deployment requirement changes).
- **[EDITORIAL: ED-336 — Cardinal death in personal combat during Zoom In: what happens to Cardinal-specific mechanics (Fortitude Templar, Justice Inquisitor, etc.) when a Cardinal is killed by PC action? Does the Holy See appoint a replacement? How long does the gap last? P2.]**

**Edge 3: Maret captured and tortured for Thread intelligence.**
If Church suspects Maret knows Thread-sensitive intelligence (she doesn't — TS 0): Inquisitor interrogation scenes. At TS 0, Maret has no Thread knowledge to extract. Inquisition Ob = 2 base vs Maret's Willpower (Spirit 3). Results in Composure damage (debate-adjacent). No Thread knowledge revealed (she doesn't have any). Church gains nothing but Maret takes psychological damage. **Correctly resolved by existing mechanics — no gap.**

---

## Findings Summary

| ID | Severity | Finding |
|----|----------|---------|
| F-MC-01 | P2 | Captured general consequence has no BG-layer rule. Gap-filled: Legionary card unavailable for 1 season. Formal rule required for Hybrid mode. |
| F-MC-02 | P2 | NPC-initiated capture/incapacitation of named PC has no Domain Echo equivalent. Narrative Accounting consequences (Mandate −1, captor Influence +1) are GM discretion, not mechanical. |
| F-MC-03 | P2 | No ransom mechanic defined. Gap-filled: 2 Wealth per named general. Formal rule needed for political negotiation arc. |
| F-MC-04 | P2 | Cardinal death in personal combat (Zoom In) has no defined succession rule or Cardinal-mechanic gap resolution. |
| F-MC-05 | P3 | Discipline check at Ob 5 (mass loss of 5 Size) produces ~8% success rate — routing is near-certain at this loss level. Correct (catastrophic loss → rout) but confirm Ob = loss magnitude is intended, not Ob = half loss magnitude. |
| F-MC-06 | P3 | Personal combat DR application (net minus DR) is clean and functional. No issues. |

