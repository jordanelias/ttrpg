# SIM-WARDEN-TC-RECLAIM — Warden Emergence + Uncontrolled Reclaim + TC→CI Propagation
## Date: 2026-04-19
## Scope: 3 scenarios testing blocking mechanics identified in session log

---

## Scenario A: Warden Emergence via Varfell Expedition (Season 8–12)

**Setup:** 4-player (Crown, Church, Hafenmark, Varfell). Season 8. Varfell VTM 2, WR 0.
- Varfell controls T4 (Grauwald), T11 (Halvardshelm), T12 (Sigurdshelm), T13 (Oastad).
- T15 (Askeheim) Uncontrolled. Proximity Rating 0.
- RS 58 (59–40 band: +2 Ob non-Thread at Proximity 0; Shifting Objects active).
- Varfell Influence 4, Intel 4.

**Season 8 — Varfell Survey of T15 (Askeheim)**

Varfell plays Consul Inward (Survey) targeting T15.
- Pool: Influence = 4d10.
- Ob: (5 − 0) + 1 = **Ob 6**. T15 is Proximity 0 — hardest survey in the game.
- Roll 4d10: 10(+2), 8(+1), 7(+1), 3(0) = 4 net. Ob 6, net 4. **Failure.**
- Effect: No POI found. +1 Church Attention Pool (Depth ≥ 3 content at Askeheim).
- **Note:** Varfell has only 4D vs Ob 6. Expected net successes with 4d10: ~1.6. P(Success) ≈ 3%. This action is essentially impossible without pool augmentation.

**Gap identified:** Varfell cannot Survey Askeheim with base Influence 4. The Expedition action that triggers Warden Emergence requires a Forgetting Check, which is separate from Survey. Forgetting Check pool (P-26): Influence + VTM level (Varfell) = 4 + 2 = 6d10, Ob 1.

**Season 9 — Varfell Expedition to T15 (Forgetting Check)**

Precondition: Varfell must have a military unit march to T15 (free march — Uncontrolled territory, no Battle). Requires Legionary Outward card.

Season 8 revised: Varfell plays Legionary Outward → March unit from T13 (Oastad) to T15 (Askeheim). Free march (Uncontrolled). Unit arrives.

Season 9: Forgetting Check fires at Phase 5 Step 9.
- Pool: Influence (4) + VTM (2) = 6d10.
- Ob: 1 (floor). Thread-qualified (VTM 2+): may reroll one die.
- Roll 6d10: 5, 2, 9(+1), 7(+1), 4, 10(+2) = 4 net. Ob 1. **Overwhelming** (net ≥ 2×Ob AND ≥ 3).
- **Warden Emergence triggers.**
- Warden Token placed at position 0.
- WC track activates at 0.
- Edeyja NPC AI activates.
- **WR +1** (Overwhelming Forgetting Check → WR +1 per npcs_special). WR: 0 → 1.

**Verdict:** Forgetting Check at Ob 1 with 6d10 is near-guaranteed (~97% Success, ~85% Overwhelming). The gate is not the check itself — it's having a unit in T15 and VTM ≥ 2. Varfell must spend a Legionary card to march to T15, which costs military action tempo. The real cost is opportunity cost, not difficulty.

**Season 10 — WC Advancement**

WC starts at 0. WC advancement requires WR ≥ 2 (PP-605). WR is at 1.
- Varfell needs another Overwhelming Forgetting Check OR two consecutive Successes to reach WR 2.
- Season 10: Forgetting Check again (unit still in T15). Pool 6d10, Ob 1.
- Roll: 8(+1), 7(+1), 1(−1), 10(+2), 6(0), 9(+1) = 4 net. **Overwhelming.** WR: 1 → 2.
- WR ≥ 2: WC can now advance.
- **WC +1.** WC: 0 → 1. Effect: +1D to all Thread operations peninsula-wide.

**Season 11 — WC 2**

Forgetting Check: 6d10 vs Ob 1. Again near-certain.
- Roll: 7(+1), 3, 9(+1), 10(+2), 2, 8(+1) = 5 net. **Overwhelming.** WR: 2 → 3.
- WR 3: Active cooperation. WC +1. WC: 1 → 2. Effect: RS decay rate halved.

**Season 12 — WC 3**

- Roll: 10(+2), 7(+1), 4, 1(−1), 9(+1), 8(+1) = 4 net. **Overwhelming.** WR: 3 → 4 (Edeyja substantive contact).
- WC +1. WC: 2 → 3. Effect: RS +2/season at Accounting.

**Assessment:**
- Once Varfell gets a unit to T15 with VTM ≥ 2, Warden emergence is near-certain.
- WC progresses to 3 in ~4 seasons (Seasons 9–12).
- **The blocking issue is not the mechanics — it's the NPC priority tree.** Varfell NPC tree P5 says "VTM/WR advancement conditions met → Pursue VTM or Warden Recognition." But the tree never explicitly says "March to T15 for Forgetting Check." The priority tree needs an explicit trigger: **when VTM ≥ 2 AND no unit in T15, March to T15 as P2 or P3 priority.**
- **Engine gap:** Forgetting Check fires at Phase 5 Step 9, but only if a faction has a unit in T15. The engine needs to track "unit in Askeheim" as a precondition.

---

## Scenario B: Uncontrolled Territory Reclaim (Post-Collapse)

**Setup:** Season 14. Hafenmark collapsed (Stability 0 at Season 13 Accounting). §1.5 Collapse Exit Procedure fires.

**State after collapse:**
- Hafenmark territories (T7 Rendstad, T8 Gransol, T10 Spartfell): → Uncontrolled, Accord 0 (Revolt state).
- Hafenmark units: Masterless — hold position, take no orders.
- Hafenmark officers: Independent status.

**Season 14 — Crown Reclaim of T8 (Gransol)**

Crown plays Legionary Outward: March from T1 (Valorsplatz) to T8.
- T8 is Uncontrolled. Per §2.6 faction_layer_v30: "Uncontrolled territories may be claimed (free march, no Battle roll)."
- Crown unit enters T8. Crown claims control.
- **Accord starts at 0 (Revolt).** Per Accounting Step 4c: Accord 0 = Revolt. Garrison fights Popular Uprising (Military vs Ob 2).
- Crown Military 5. Roll 5d10: 8(+1), 10(+2), 3, 7(+1), 1(−1) = 3 net. Ob 2. **Success.**
- Revolt suppressed. Territory under Crown control. Accord remains 0 until next Accounting normalisation.
- Next Accounting: garrison present + no hostile action → Accord +1 (0 → 1). Requires 2 more peaceful seasons to reach Accord 2 (TCV-eligible).

**Season 14 — Church Seizure of T7 (Rendstad)**

T7 is Uncontrolled, Accord 0. Church Mandate 5 > no controlling faction.
- Per §2.7 faction_layer_v30: Church Seizure is a political act, distinct from military occupation.
- **But Seizure requires a controlling faction to compare Prominence against.** Uncontrolled territory has no controlling faction.
- **Gap:** Can Church Seize an Uncontrolled territory? The Seizure Ob formula (7 − PT) and Prominence requirement (Church Mandate > controlling faction Mandate) are undefined for Uncontrolled territories.

**Resolution options:**
1. Church can Seize Uncontrolled territories with Ob = 7 − PT (no Prominence comparison needed — there's no rival). Auto-Prominent.
2. Seizure only works against controlled territories. Church must first claim (free march) then Seize from itself (nonsensical).
3. Church claims via free march like any faction. No Seizure needed for Uncontrolled.

**Recommendation:** Option 3 is cleanest. All factions including Church use free march for Uncontrolled territories. Seizure is specifically for territories controlled by a *rival*. Church uses Seizure against Crown/Hafenmark/Varfell-controlled territories, not vacuums.

**ED flag: ED-NEW-008 — Confirm Seizure does not apply to Uncontrolled territories. Church uses free march.**

**Season 15 — Varfell Claim of T10 (Spartfell)**

T10 is Uncontrolled. Varfell plays Legionary Outward: March from T4 to T10.
- Free march. Varfell claims T10. Accord 0.
- Varfell must garrison and wait for normalisation (2 peaceful seasons to Accord 2).

**Season 15 — Masterless Unit Claim**

Crown plays Domain Action to Claim Masterless Hafenmark unit in T8.
- Per §1.5: Military Domain Action, Ob 2. Success: units transfer. Failure: units disband.
- Crown Military 5. Roll 5d10: 9(+1), 7(+1), 2, 10(+2), 4 = 4 net. Ob 2. **Overwhelming.**
- Masterless unit transfers to Crown at current strength.

**Assessment:**
- Uncontrolled territory reclaim is mechanically clean via free march (no roll).
- The cost is action tempo (Legionary card) + Accord recovery time (2–3 seasons to reach Accord 2).
- Post-collapse territory grab is a race: whoever marches first claims.
- **The Seizure/Uncontrolled gap needs editorial resolution** (ED-NEW-008).
- **Masterless unit claiming works** — Ob 2 Military check, standard degree table.

---

## Scenario C: TC→CI Propagation and TC Formula Consistency Check

**Purpose:** Verify TC formula (§9 faction_layer_v30) propagates consistently to all downstream references.

**TC Formula (canonical, faction_layer_v30 §9):**
1. Institutional Momentum: TC +1 (passive, always)
2. Piety Yield: per Prominent territory, PT 5 = +1, PT 4 = +0.5 (floored at Year-End). Others = 0.
3. Assert (optional Church action): Influence vs Ob 2. Success: TC +1. Failure: Stability −1.
4. Suppress (optional opponent action): Mandate vs Ob = floor(Church M / 2) + 1. Success: negate Step 1. Failure: Stability −1.
5. Hafenmark Structural Suppression: while Baralta Mandate ≥ 4, TC −1/season.
6. Seasonal cap: ±3 from player DAs, ±5 from all sources.

**Cross-reference check — victory_v30 §7:**
1. ✓ Institutional Momentum: TC +1.
2. ✓ Piety Yield: same formula. Refs "Church Mandate > controlling faction Mandate."
3. ✓ Assert: Influence vs Ob 2. Success: TC +1. **Discrepancy:** victory_v30 says Failure = "Cohesion −15 (derived_stats_v1)" vs faction_layer §9 says Failure = "Church Stability −1." **These may both apply** — Stability −1 is the faction-layer effect, Cohesion −15 is the derived stat consequence. Not a conflict if both fire.
4. ✓ Suppress: Same Ob formula. **Same discrepancy pattern** — victory_v30 says "Cohesion −15" vs faction_layer says "Stability −1."
5. ✓ Hafenmark Structural: TC −1/season when Baralta Mandate ≥ 4.
6. ✓ Seasonal cap: ±5 from all sources.

**Discrepancy resolution:** Cohesion is a derived stat (derived_stats_v1). Stability −1 feeds into the Cohesion formula. Both references are correct at different abstraction layers. No propagation fix needed — just confirm Cohesion = f(Stability, ...) and the −15 is the downstream calculated impact of Stability −1. **Flag for verification: ED-NEW-009 — confirm Cohesion −15 is the derived consequence of Stability −1, not an independent penalty.**

**TC ceiling:**
- faction_layer_v30 §9: No ceiling stated (implicit 75 freeze from legacy).
- victory_v30 §7: "TC freezes at 75. Phase transition."
- tc_political_v30 §7.1: "New ceiling: 100 (replacing 75 freeze)."
- **Conflict:** victory_v30 says TC freezes at 75. tc_political says ceiling is 100.
- **Resolution:** tc_political_v30 is the newer, more complete design. It supersedes the victory_v30 75 freeze. But victory_v30 has not been updated.
- **Propagation needed:** Update victory_v30 §7 to reflect TC ceiling = 100 per tc_political_v30 §7.1.

**CI terminology:**
- victory_v30 §3.2 uses "CI=100" (Church Influence = 100). This appears to be TC under a renamed label.
- tc_political_v30 never defines "CI" separately.
- **Assessment:** CI = TC. The "CI" label in victory_v30 is either: (a) a renamed version of TC per the tc_political redesign, or (b) a typo/stale reference. Since TC ceiling is now 100 per tc_political, and CI=100 triggers Mass Seizure, CI=TC.
- **Propagation needed:** Either rename TC→CI globally (major change) or replace "CI" with "TC" in victory_v30 §3.2 (minimal change). Recommend the latter — TC is established terminology everywhere else.

**TCV→PV:**
- "PV" (Peninsular Value) does not appear in any fetched canonical file. victory_v30 uses "TCV" throughout.
- **Assessment:** Session log reference to "TCV→PV propagation" may refer to a planned rename that hasn't been implemented, or to how TCV contributes to the universal victory calculation (Peninsular Sovereignty). No propagation work found.
- **Flag: GAP — PV is not defined in any canonical source. Session log reference may be stale or forward-looking.**

---

## Summary of Findings

| Item | Status | Action |
|------|--------|--------|
| Warden Emergence mechanic | **Exists and works.** Forgetting Check Ob 1 is near-trivial with VTM ≥ 2. | NPC priority tree needs explicit "March to T15" trigger for AI. Engine needs "unit in T15" precondition check. |
| WC advancement | **Works.** WR gates WC. WR advances via Forgetting Check. WC 0→3 in ~4 seasons once unit in T15. | No fix needed. |
| Uncontrolled territory reclaim | **Works** via free march. | **ED-NEW-008:** Confirm Seizure does not apply to Uncontrolled territories. |
| Masterless unit claim | **Works.** Military DA, Ob 2. | No fix needed. |
| TC formula | **Consistent** across faction_layer §9 and victory_v30 §7. | **ED-NEW-009:** Confirm Cohesion −15 = derived consequence of Stability −1. |
| TC ceiling | **Conflict:** victory_v30 says 75 freeze, tc_political says 100. | **Propagation required:** Update victory_v30 §7 TC ceiling to 100. |
| CI terminology | CI = TC in victory_v30. | Replace "CI" with "TC" in victory_v30 §3.2 (or rename globally). |
| TCV→PV | PV not defined anywhere. | **GAP.** Stale or forward-looking reference. No action. |

## Blocking Issues for Engine v3

1. **Varfell NPC AI does not trigger March to T15.** Without this, Warden Emergence never fires in NPC-driven play.
2. **TC ceiling mismatch** between victory_v30 (75) and tc_political (100) will cause engine to use wrong cap.
3. **CI=TC rename** not propagated — engine may look for "CI" as a separate variable.
