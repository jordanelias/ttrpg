## Torben Loyalty Track (v04 B2 + B5 — PP-188 correction)
Range 0–7. Starts at **7** (PP-599). Visible to all. Active from game start.
Decay on Altonian Court residence: −1 immediately on departure + −1/Year-End while abroad.

**Gaining:**
- Senator Outward targeting Torben: Overwhelming +2; Success +1.
- Crown holds PI ≥ 5 at Year-End: +1.
- Crown upholds Institutional Mandate 2+ consecutive seasons: +1/Year-End.

**Losing:**
- Crown Compromises Institutional Mandate: −1.
- Crown issues Emergency Powers: −1.
- Löwenritter Coup fires: reset to 1.
- TC crosses 60: −1.
- Torben sent to Altonia (comply with tutoring demand): −2 immediately.

[STRUCK — Deed system dissolved PP-424. Torben Loyalty conditions now per victory_v30.md §3.6 Löwenritter.]
Altonian Tutoring Demand triggers at IP ≥ **40** (v04 B2: "Torben Tutoring Demand (IP ≥ 40 Event)") (not 30 — v04 B2: "Torben Tutoring Demand (IP ≥ 40 Event)").


## Elske Off-Board Card (v04 B2)
Princess Elske Almqvist is in Altonia (not on the board). Married to Doux Alexios Laskaris, province borders T4.
Elske Loyalty: 0–7, starts 4. Tracked on off-board card near T4.

Contact: Crown or Löwenritter Senator Outward in T4 (Ob 2 at IP < 60; Ob 3 at IP ≥ 60).
Return: Elske Loyalty ≥ 6 + IP < 60 + Crown/Löwenritter unit in T4: Military vs Ob 2. IP +5 on success.


## Patience Protocol (Varfell, v04 B5)
Patience Counters (PC): 0–4 at VTM 0–3; 0–6 at VTM 4+. Private to Varfell player.
Gaining: +1 PC per season Tribune available but played differently; +1 PC per season pass on Senate purchase when Wealth ≥ 3. Max +2/season.
[Full spend table in v04 B5 — key: 4 PC = Spy anywhere on board; 6 PC at VTM 4+ = VTM +1]


## Riskbreakers (NPC, v04 B13 — reconciled with amendment2)
3 tokens per year. Priority tree evaluated at Phase 4 start.
[v04 B13 priority tree is authoritative — differs from amendment2 which was a proposal. v04 applies.]


## Warden Recognition Track (PP-425 — Varfell Path B)
Range 0–4. Varfell-only private track. Advances through successful Expeditions into T15 (Askeheim).

| WR | State |
|----|-------|
| 0 | Wardens unaware or indifferent. |
| 1 | Wardens have observed Vaynard (≥ 1 successful Expedition). |
| 2 | Wardens recognise Vaynard as steward. Varfell Path B unlocked. |
| 3 | Active cooperation (+1D Thread ops, equivalent to WC ≥ 1). |
| 4 | Edeyja has made substantive contact (Overwhelming Forgetting Check). |

**Advancing:** Overwhelming Forgetting Check → WR +1. Two consecutive Successes → WR +1. **Decreasing:** RM emergence (WA ≤ −2) → WR −2. No Expedition attempted for 3+ consecutive seasons → WR −1. If WR returns to 0 after advancing past 1: Varfell Path B permanently blocked this game.


## Warden Emergence (v04 B2/B13)
Condition: any faction's Southernmost Expedition passes Forgetting Check (Phase 5 Step 9).
On Emergence: Warden Token placed at position 0. Warden Cooperation Track activates.
Edeyja/Wardens NPC AI activates (B13: contain entity; investigate Niflhel; work alongside; emergency Mend).



## Warden Cooperation Track (WC)
**Canonical source: `designs/board_game/victory_v30.md` §6**

Range: 0–3. Starts at 0.

| WC Level | Effect |
|----------|--------|
| ≥ 1 | +1D to all Thread operations peninsula-wide |
| ≥ 2 | RS decay rate halved |
| ≥ 3 | RS +2/season at Accounting |

WC advances via successful Southernmost Expedition and Warden engagement actions. Multiple victory conditions require RS thresholds; WC is the primary tool to arrest RS decline.


## Warden's Accord (WA)
**Canonical source: `designs/board_game/victory_v30.md` §8**

Range: −3 to +3. Starts at 0.

RM Emergence triple condition: WA ≤ −2 AND ≥ 3 territories PT ≤ 1 AND RS ≤ 50. One-shot.
RM Suppression: WA ≥ 0 OR all territories PT ≥ 2 OR RM Stability 0.
Varfell Path B blocked if RM has emerged (WA ≤ −2).

See victory_v30.md §8 for WA movement rules and full RM stat block.


## Intel Advancement Counter (PP-180 revised)
Intel Advancement Counter (0–3) on faction mat.
Each season with ≥1 successful Intel or Quiet Network order: Counter +1.
At Counter 4: Intel stat +1 (max 7); Counter resets to 0.
Note: Intel stat advancement is valid for NPC factions (Niflhel). Varfell victory paths do NOT require Intel stat advancement — they use VTM and territorial control.


## Command Event — Captured or Killed General (ED-334 + ED-335 resolved)
When a named PC General is captured or killed during a Zoom In personal scene (Hybrid) or TTRPG mass combat:

**Immediate BG consequence (fires at Zoom Out / next Accounting):**
- Captured general's faction: Legionary card unavailable for **1 season** (no Muster or March orders — the command structure is disrupted).
- Capturing/killing faction: **Influence +1** (political leverage or military prestige).
- Captured general's faction: **Mandate −1** at next Accounting (morale blow — general lost).

**Ransom:** Capturing faction may offer ransom. Base: **2 Wealth** per named general. Both factions must agree. Ransom paid → general returns next season, Legionary card restored.

**Rescue:** Tribune Investigate (Ob 4 in secure enemy territory) to locate, then a Zoom In rescue scene. Success returns general; Failure may result in execution (Mandate −2 instead of −1).

**NPC-initiated kills only:** When an NPC kills a PC General (not captured), the Influence +1 and Mandate −1 still apply. No ransom is possible. The general is dead; the faction loses their named commander permanently (all Command bonuses from that general cease).

**Does not trigger a Domain Echo** (this is an Accounting consequence, not a Domain Echo — Domain Echoes apply to PC-initiated Domain Actions only).

<!-- patch_history: references/params_board_game_history.md -->
<!-- canonical_sources: references/canonical_sources.yaml -->
