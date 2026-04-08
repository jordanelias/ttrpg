# SIM-VAR-04 — Board Game: Löwenritter Post-Coup Arc
## Mode: C (Full Scenario) + A (Isolation) + J (Precedent) + L (Cognitive Load)
## Date: 2026-04-08 | First simulation of conditional faction post-coup play

---

## FETCH LOG
canonical_sources.yaml: ✓ (156 lines)
params_board_game.md: ✓ (1375 lines)
params_factions.md: ✓ (517 lines)
designs/board_game/victory_architecture_v1.md: ✓ (393 lines)

---

## Scenario: Coup Fires at Season 8

**Pre-coup state (S8 trigger):**
Four-player game. Coup Counter reached 4 via: Crown Mandate dropped to 2 (Church Decree chain + Hafenmark Parliamentary Manoeuvre), PI dropped to 2 (two Crown Emergency Powers uses), Church Mandate ≥ 5, two other factions have active Standing tokens against Crown. Royal Deposition trigger fires (PP-194 Parliament Deposition mechanic). Crown fails emergency Parliamentary Session (5D vs Ob 3: ~68% success, assume failure). Crown eliminated. Löwenritter Coup Counter set to 4 → coup fires.

**Coup fires at Season 8 Accounting.** Effects (PP-194 + Löwenritter Canonical Structure):
- Crown faction eliminated (player exits).
- Löwenritter becomes a playable faction.
- Löwenritter takes T14 (Ehrenfeld, existing garrison), Crown territories default: T1 (Valorsplatz), T2 (Kronmark), T3 (Lowenskyst), T5 (Feldmark), T6 (Stillhelm) — all become contested (not automatically Löwenritter controlled).
- PI: −3 (standard coup effect). PI was 2 → PI −1 (can't go below 0): **PI = 0** (Parliament non-functional).
- Ministry: AP-tokens in T1 and T2 removed. Ministry Mandate −2 → Ministry Mandate 1.
- Ministry Stabilisation: suspended 1 season.
- Torben Loyalty: coup shifts Torben. Torben was at Crown Loyalty 10 — but Crown is gone. Torben becomes an NPC contested between Löwenritter and Church (both want to legitimise their authority through Torben's dynastic claim).
- Elske Loyalty: starts at 4, unaffected immediately by coup.

**Post-coup starting state:**

| Faction | Mandate | Influence | Wealth | Military | Stability | TCV |
|---------|---------|-----------|--------|----------|-----------|-----|
| Löwenritter | 3 | 2 | 3 | 6 | 5 | 0 |
| Church | 5 | 6 | 5 | 4 | 5 | 3 |
| Hafenmark | 4 | 4 | 5 | 3 | 4 | 9 |
| Varfell | 4 | 4 | 4 | 4 | 4 | 6 |

TC: 41 (8 seasons of advance: 28 + 8 passive + 2 Church Assert − 1 Hafenmark Structural × 4 ≈ 41). RS: 69.
PI: 0. IP: 24. Coup Counter: 4 (coup fired, counter stays at 4 post-coup).

**Löwenritter controls T14 only (TCV 3).** Crown's 6 territories are now contested. Löwenritter must seize them.

---

## Mode A: Löwenritter Action Economy

**Löwenritter card hand:** 4 shared + 2 faction cards. Faction cards: unique Löwenritter mechanics from canonical structure.
- **Lions' Table** (Legionary action): Military 6D. Löwenritter's dominant resource.
- **Riskbreakers** (Tribune action): once per season, execute one Priority Tree action at no card cost.

**Faction stats:** M3, I2, W3, Mil6, Sta5. Unique advantages:
- Military 6 = highest on board. Attack pool is massive.
- Knights of the Peace: one territory per season has March Ob −1 (pacified roads).
- Royal Guard: cancel one Intel action targeting Löwenritter per season.

**Victory conditions:**
- **Primary (Regency Establishment):** TCV ≥ 10, TC < 50, IP < 60, RS > 40, PI ≥ 4, Successor confirmed (Elske confirmed OR Torben Loyalty ≥ 6). Held 2 consecutive Accounting steps.
- **Alternate (Military Consolidation, only after 8 Löwenritter seasons):** TCV ≥ 16, Military ≥ 5, RS > 35, TC < 60.

**Analysis — Primary victory bottleneck: PI ≥ 4.** PI is currently 0 (coup destroyed parliament). Löwenritter cannot win Regency until PI recovers to 4. PI recovery sources:
- Ministry Stabilisation: +1 PI/season when Ministry AP-token in T1 (suspended this season).
- Hafenmark Parliamentary Manoeuvre: PI +1 per success.
- Hafenmark Parliamentary Session: PI +1 on Majority Support.
- Ministry Legislative Record: PI +1 at Year-End if parliamentary ruling recorded.

**PI recovery from 0 to 4: minimum 4 seasons** (if Ministry restored in S9 + Hafenmark cooperates). That's 4 seasons before Regency victory is mathematically possible — 2 more to hold it. Earliest Regency win: **S14**.

**Alternate — Military Consolidation at S16+** (8 Löwenritter seasons from S8 = S16). Requires TCV ≥ 16 which means seizing 5+ territories beyond T14 (TCV 3 currently; need 13 more TCV).

---

## Mode C: Post-Coup Arc — Seasons 9–14

### Season 9 — Löwenritter expands

**Strategic priority:** Secure Crown territories before other factions claim them. T1 (Valorsplatz, TCV 5, Parliament seat) is the most critical — it controls Ministry function and PI recovery.

**Löwenritter actions:**
1. **March into T1 (Valorsplatz):** Military 6D vs Ob 0 (uncontested entry, no defender). Entry is automatic (no Battle roll for uncontested March). **T1 secured.** TCV: 0+5 = 5.
2. **March into T5 (Feldmark):** Uncontested. **T5 secured.** TCV: 5+1 = 6.

**Other factions' opportunism:**
- Church: sees Crown's collapse as a TC opportunity. Plays Assert (TC +2). TC: 41+2 = 43. Church also moves to seize T13 (Oastad, Varfell — Church Prominence opportunity if Varfell Mandate ≤ Church Mandate). Church M5 > Varfell M4 → Church prominent in T13. Church plays Active Inquisition in T13 (AP +2, below threshold 3).
- Hafenmark: plays Parliamentary Manoeuvre. PI 0 → there's no PI to recover to. Parliamentary Manoeuvre requires PI > 0? **[GAP: Parliamentary Manoeuvre at PI = 0 — does it fail, produce PI 0 → 1, or require PI floor ≥ 1?]** Ruling (gap-fill): PI 0 means Parliament non-functional. Parliamentary Manoeuvre cannot fire. PI must reach 1 first (Ministry must act). Hafenmark action wasted.
- Varfell: builds VTM. VTM was at 2 (8 seasons). Plays Tribune Intel in T13.

**Ministry (NPC):**
Ministry Stabilisation suspended this season (post-coup). Ministry AI Priority 2: no AP-token in T1 → Ministry plays Consul Inward in T1. Mandate 1D vs Ob 1. P(Success) ≈ 45%. 
Result: Success. Ministry AP-token placed in T1.

**Accounting S9:**
- Ministry Stabilisation: AP-token in T1, Mandate ≥ 1 → Emergency Powers PI loss −1 (reduces losses). But PI is 0 — no current Emergency Powers. PI: 0. Ministry gives PI +0 this season.
- TC: 43 + 1 passive = 44 (Hafenmark Structural suppression: Baralta M4 ≥ 4 → TC −1). TC: 44 − 1 = **43** net.

**Löwenritter TCV after S9:** T14 (3) + T1 (5) + T5 (1) = **9 TCV**. One territory shy of Regency threshold (≥ 10).

### Season 10 — Löwenritter secures Regency TCV base

**Löwenritter actions:**
1. **March into T2 (Kronmark, TCV 1):** Uncontested. T2 secured. TCV: 9+1 = **10.**
2. **Stabilise T1:** Ministry AP-token present — no action needed. Löwenritter plays Govern T1 (Consul Inward, Ob = T1 Prosperity ÷ 2 = 6÷2 = 3). 3D vs Ob 3. P(Success): ~40%. Result: Failure. Stability −1 (PP-403). Löwenritter Stability: 5→4.

**PI check:** PI still 0. Ministry in T1 → Ministry Stabilisation fires at Step 4b (Accounting). Emergency Powers PI loss −1: no Emergency Powers active, no PI loss to negate. Ministry Legislative Record: no Hafenmark Parliamentary Ruling this year (Parliamentary Manoeuvre blocked at PI 0). PI: 0 → 0.

**PI recovery problem:** Without Hafenmark's Parliamentary Manoeuvre (blocked at PI 0) and without PI events, Ministry Stabilisation does nothing (it negates losses, not generates gains). PI is stuck at 0 until a PI-generating event fires.

**What generates PI from 0?**
- Hafenmark Parliamentary Manoeuvre: requires PI > 0 (blocked).
- Year-End Legislative Record: requires a Hafenmark Parliamentary Ruling (requires Parliamentary Manoeuvre success — blocked).
- Crown Parliamentary Session (emergency): Crown is gone.
- Löwenritter emergency Parliamentary Session (from Deposition mechanic): Löwenritter can play Senator Inward (Ob 3) to restore legitimacy. Success: PI recovery?

**[GAP: No rule defines what PI recovery from 0 looks like without Parliamentary Manoeuvre. The only PI-from-0 mechanism that exists is the Löwenritter emergency session (Ob 3) — but its PI effect is undefined.]**

**[EDITORIAL: ED-331 — PI recovery from 0: define a Löwenritter Reconstitution action (Senator Inward, Ob 3) that, on Success, restores PI to 1 and re-enables Parliamentary mechanics. Without this, PI = 0 is a permanent lock — Löwenritter can never achieve Regency. P1 — blocks Löwenritter primary victory path.]**

**Interim — PI frozen at 0, Regency blocked. Löwenritter must pursue Alternate (Military Consolidation) or wait for PI-gen mechanic.**

### Seasons 11–16 — Military path (Alternate win condition)

With PI blocked, Löwenritter pivots to Military Consolidation (available at S16, 8 seasons post-coup). Requirements: TCV ≥ 16, Military ≥ 5, RS > 35, TC < 60.

**TCV trajectory:** At S10, TCV 10. Need TCV 16. Must seize 6 more TCV. Available Crown territories: T3 (Lowenskyst, TCV 1), T6 (Stillhelm, TCV 1). Other targets require military conquest: T8 (Gransol, Hafenmark★, TCV 5) or T9 (Himmelenger, Church★, TCV 3).

**Military conquest pace:** Löwenritter Military 6 is overwhelming. At Ob 2 (March into defended territory), Löwenritter 6D attack vs defender pool.

Against Hafenmark (Military 3 + Fort 1 = 4D defending T8): 6D vs 4D. P(Löwenritter wins) ≈ 72%.
Against Church (Military 4 + Fort 2 = 6D defending T9): 6D vs 6D. P(Löwenritter wins) ≈ 50%.

**S11–S13:** Löwenritter secures T3, T6 (uncontested), then presses T7 (Rendstad, Hafenmark, TCV 1, Fort 0 → 6D vs 3D, ~83% win). TCV: 10+1+1+1 = 13.

**S14:** Assault T8 (Gransol, Hafenmark★, TCV 5). 6D vs 4D → P(win) 72%. Assuming success. TCV: 13+5 = **18**.

**S16 Alternate check:** TCV 18 ≥ 16 ✓. Military 6 ≥ 5 ✓. RS ~66 > 35 ✓ (RS decay at −1/year over 4 years from S12 ≈ −4 from 69 = 65). TC: 44 (S10) + 6 seasons passive +1 − Hafenmark structural −1/season = 44 + 0/season net = **TC ~44 < 60** ✓.

**Military Consolidation available at S16.** But must hold for 2 consecutive Accounting steps = **earliest win S17.**

---

## Mode J: Precedent and Rules Gaps

**Gap 1 — PI recovery from 0 (ED-331, P1):** No defined mechanism to recover PI from 0 to 1 after Löwenritter coup destroys Parliament. Parliamentary Manoeuvre is gated at PI > 0, creating a circular lock.

**Gap 2 — Successor confirmation mechanic:** Regency requires "Elske confirmed OR Torben Loyalty ≥ 6." Elske confirmation: undefined procedure. Torben Loyalty at coup: was 10 (Crown-loyal) but Crown is gone. Torben without a Crown has undefined Loyalty state. **[EDITORIAL: ED-332 — Torben Loyalty post-Crown-elimination: define whether Torben Loyalty resets, transfers to Löwenritter, or becomes a contested track (Löwenritter vs Church vs Hafenmark each trying to claim the dynastic heir). P2.]**

**Gap 3 — Contested Crown territories:** After Crown elimination, Crown's 6 territories are "contested" — but no rule defines what "contested" means mechanically. Do they immediately become uncontrolled (any faction can March in freely)? Do they stay under some administrative ghost? **Ruling (gap-fill):** Crown elimination → all Crown territories become uncontrolled (no faction token, no Fort bonus, no Garrison modifier). First March into an uncontrolled territory succeeds automatically. **[EDITORIAL: ED-333 — Confirm faction-elimination territory status: uncontrolled (any faction Marches freely) vs contested (requires a contested entry roll). P2.]**

---

## Mode L: Cognitive Load

**Löwenritter post-coup cognitive requirements:**
1. Track TCV (expanding rapidly through March actions).
2. Track 8-season Military Consolidation countdown (separate counter).
3. Track PI (recovery from 0 — complex rules gap).
4. Track Successor status (Elske/Torben — two separate NPC tracks).
5. Track Riskbreaker resource (once per season free action).
6. Track Coup Counter (stays at 4 post-coup — no further function but confusingly occupies a track).

**Load rating: HIGH.** The conditional faction trigger, combined with PI recovery complexity and dual successor tracks, makes Löwenritter the most mechanically complex faction. The 8-season Military Consolidation countdown adds a unique meta-timer not present for other factions.

---

## Findings Summary

| ID | Severity | Finding |
|----|----------|---------|
| F-LW-01 | P1 | PI recovery from 0 is impossible without a Löwenritter-specific Reconstitution action. Parliamentary Manoeuvre (gated at PI > 0) cannot generate PI from 0. Regency victory permanently blocked unless ED-331 resolved. |
| F-LW-02 | P2 | Torben Loyalty state after Crown elimination undefined. Post-coup dynastic legitimacy contest has no mechanical framework. |
| F-LW-03 | P2 | Contested Crown territories on faction-elimination have no defined status. Gap-filled as uncontrolled. |
| F-LW-04 | P2 | Parliamentary Manoeuvre at PI = 0 has no defined outcome. Gap-filled as blocked. |
| F-LW-05 | P2 | Military Consolidation is reachable by S16 in this scenario. Regency is blocked without ED-331. Löwenritter's primary victory path requires designer input. |
| F-LW-06 | P3 | Coup Counter stays at 4 post-coup with no defined function. Cosmetically confusing. Consider resetting to 0 post-coup (coup fired; counter no longer meaningful). |

