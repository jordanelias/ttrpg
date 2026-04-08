# SIM-NEW-01 — BG: Conviction Yield + TC Cascade
## Mode: A (Mechanic Isolation) + B (Interaction Chain) + D (Edge Cases)
## Date: 2026-04-08

---

## FETCH LOG
canonical_sources.yaml: ✓ (156 lines)
params_board_game.md: ✓ (1431 lines)
victory_architecture_v1.md: ✓ (412 lines)

---

## System Under Test

Conviction Yield (CV) is a secondary TC source: at each Accounting, for every territory where Church is Prominent (Church Mandate > controlling faction Mandate), add +1 if CV = 5, +0.5 if CV = 4. Total = floor(sum).

This has never been stress-tested. Key questions:
- How much TC does Conviction Yield realistically contribute per season?
- Does it interact with Hafenmark structural suppression in ways that were missed?
- Is there a scenario where CV accumulates faster than Church can advance, causing runaway TC?

---

## Mode A: Conviction Yield Magnitude at Game State

**Starting state:** TC 28. Church M 5. Controlling factions: Crown M5 (6 territories), Hafenmark M4 (4 territories), Varfell M4 (4 territories), Church M5 (T9 = self).

**Church Prominence check per territory (Church M5 > controller M):**
- T1–T6 (Crown, M5): 5 > 5 → NO (tie goes to defender per PP-417)
- T7–T8, T10, T17 (Hafenmark, M4): 5 > 4 → **YES** (4 territories)
- T4, T11–T13 (Varfell, M4): 5 > 4 → **YES** (4 territories)
- T9 (Church self): irrelevant (Church controls it)

**Prominent territories: 8 of 15.** Starting CV values (estimated from prior analysis): T7, T10, T17 ≈ CV 2; T8 (Hafenmark capital) ≈ CV 3; T4, T12 ≈ CV 2; T11 ≈ CV 3; T13 ≈ CV 2.

Conviction Yield at start:
- CV 5 territories among prominent 8: 0 → +0
- CV 4 territories among prominent 8: 0 → +0
- All 8 at CV 2–3 → +0

**Starting Conviction Yield: 0.** Church gets no bonus TC from CV at game start. All TC comes from institutional momentum (+1/season) and Assert.

**What changes Conviction Yield?**
Church must raise CV in Prominent territories to 4 or 5 via Piety Spread (PP-428). At CV 4 → +0.5 TC/season per territory. At CV 5 → +1 TC/season per territory.

**Scenario: Church spends 3 seasons Spreading Piety in all 8 Prominent territories.**
- 3 seasons × 8 territories = 24 Piety Spread uses. But CV action cap: 1 per territory per season. Church can only Spread in one territory per card play. With 1 Consul Inward card per season: max 1 Piety Spread per season (1 territory). After 8 seasons: 8 territories raised from CV 2 to CV 3. Another 8 seasons: CV 3 to CV 4.

**Finding P1 — Conviction Yield is slower than expected.** Church has 1 Consul Inward card per season (shared; also used for Govern, Trade). Piety Spread competes with all other Consul actions. At 1 Piety Spread per season, reaching CV 4 in all 8 Prominent territories takes 16 seasons (CV 2→3: 8, CV 3→4: 8). TC contribution from Conviction Yield at full CV 4: floor(8 × 0.5) = floor(4) = 4 additional TC/season.

**Corrected timeline:** Conviction Yield ramps slowly and only becomes meaningful at S16+. This is a late-game TC accelerator, not an early-game pressure tool. Combined with institutional momentum (+1/season) and Assert (+1 on Success), max realistic TC generation after S16: +6/season. From TC 28 starting, TC 75 reached around S28 — 10+ years of in-game time. Confirms the game arc: Church must persist for 2–3 full arcs.

---

## Mode B: Interaction Chain — Conviction Yield + Hafenmark Structural Suppression

AER ≥ 3 bypasses Hafenmark structural suppression (PP-203). If AER reaches 3, Baralta's −1 TC/season suppression no longer fires. Does Church have a path to AER 3?

**AER starting value: 2.** AER advances via: Crown Diplomatic Outreach to Schoenland (PP-437: AER +0.5 to +1 per use). Also: Church Temperance Cardinal Focus gives AER +1/season (PP-430). AER 3 is reachable by:
- S3: Temperance Focus → AER 3. (Church gains AER +1 via Cardinal Focus. No opposing faction can prevent this — it's a declarative action, no roll.)

**At AER 3:** Hafenmark structural suppression (TC −1/season) is bypassed. TC now advances at +1/season baseline instead of +0/season net. Combined with Conviction Yield (even minimal: +0.5 at S8 if Church has Piety Spread in one territory to CV 4): TC advances at +1.5/season. By S20 from AER 3 trigger: TC 28 + (17 × 1.5) = TC 53.5 → TC 54.

**Finding P2 — Temperance Cardinal Focus is a silent early-game enabler.** A single declarative action at S1 shifts TC baseline from 0/season to +1/season (bypassing Hafenmark structural suppression for the entire game). This is likely known but has never been explicitly modelled. Church player should always play Temperance Focus in S1 unless Fortitude or Justice is more urgently needed.

**Counter-play:** Hafenmark can choose Parliamentary Challenge instead of structural suppression (PP-431-COR: Challenge replaces structural). But if AER 3 has already bypassed structural, Hafenmark has already lost the automatic suppression — Challenge still works independently (it directly reduces TC −1 or −2 on Success/Overwhelming). Challenge is NOT bypassed by AER. AER only bypasses the automatic structural suppression.

**Finding P3 — AER 3 creates asymmetry: Hafenmark loses their free automatic action but retains their paid action (Challenge).** The paid action is stronger (TC −2 on Overwhelming) but costs a card play. Net effect of AER 3: Hafenmark must actively invest to suppress TC rather than getting free suppression.

---

## Mode D: Edge Cases

**Edge 1: Church Prominent in Crown territory, Crown plays Excommunication threat.**
Crown Mandate drops to 4 (via Hafenmark Decree). Church M5 > Crown M4 → Crown territories become Church Prominent. Church gains Conviction Yield from T1, T2, T5, T14 (all CV ~3 → no bonus yet). But the Prominence shift is immediate — Crown must recover Mandate above Church Mandate to restore non-Prominence.

**Implication:** A Decree chain targeting Crown Mandate below Church Mandate creates Conviction Yield opportunities. Church should not use Assert in the same season as gaining new Prominent territories (Conviction Yield from those territories fires at Accounting; Assert fires before Accounting — no interaction, but they're sequential).

**Edge 2: Conviction Yield when TC ≥ 75 (frozen).**
TC frozen at 75. Conviction Yield at Accounting: the formula still calculates. But TC is frozen — the value cannot increase. Does Conviction Yield fire against the frozen TC and get absorbed? Ruling (from params): "TC frozen at 75. Remaining TC 75→100 requires peninsula territorial conquest, not clock-based advance." Conviction Yield is a clock-based advance. At TC 75, Conviction Yield is effectively nullified — the TC cap absorbs it.

**Finding P4 — Church loses all Conviction Yield benefit the moment TC freezes.** This creates a use-it-or-lose-it dynamic: Church must choose whether to invest in Conviction Yield early (slow, eventual payoff) or in military/seizure positioning (post-TC 75 priority). If Church over-invests in Piety Spread and TC happens to reach 75 before Conviction Yield kicks in meaningfully, all that CV investment is wasted as a TC driver (though it still helps seizure Ob).

---

## Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-CY-01 | P1 | Conviction Yield is a late-game (S16+) TC accelerator requiring 16 seasons of dedicated Piety Spread investment. Not an early-game tool. |
| F-CY-02 | P2 | Temperance Cardinal Focus in S1 bypasses Hafenmark structural suppression via AER 3 with zero investment. Silent early-game TC enabler. |
| F-CY-03 | P2 | AER 3 creates asymmetry: structural suppression bypassed (automatic) but Parliamentary Challenge retained (paid action). |
| F-CY-04 | P2 | All Conviction Yield is nullified at TC 75 (frozen clock absorbs clock-based advances). Creates use-it-or-lose-it investment tension. |

