# VALORIA — Warden Cooperation as Survival Spine
## ED-669 | Status: CANONICAL
## Date: 2026-04-17
## Scope: Documents WC's role as the mechanism of the "second contest" (survival vs. sovereignty)
## Cross-references: victory_v30.md §6, references/ms_budget.md, clock_registry_v30.md, arc_register.md §II (ARC-S15, S32, S34)
## Canon compliance: A1 (Thread as constitutive ground — WC measures collective recognition of substrate dependency)

---

## The Two Contests

Valoria's campaign structure presents two simultaneous contests:

**Contest 1 — Political Sovereignty:** Which faction governs the peninsula? Resolved through territorial control, diplomacy, military action, and institutional maneuvering. Multiple solutions. Multiple factions can win.

**Contest 2 — World Survival:** Does the world survive? Resolved through RS maintenance. One solution: WC 3. RS 0 = Rupture = all factions lose.

These contests compete for the same resources: player time, faction actions, military assets. High IP forces military attention exactly when Southernmost expedition maintenance is most needed. This resource tension IS the game's strategic architecture.

---

## WC Track (0–3)

| WC | Effect | WR Gate | What It Means |
|---|---|---|---|
| 0 | No effect | — | The peninsula has not recognized its constitutive dependency on the substrate. Factions treat Thread as irrelevant to governance. |
| 1 | +1D all Thread operations peninsula-wide | WR ≥ 2 | Partial recognition. Some factions engage with Askeheim. Thread practice becomes slightly more effective. |
| 2 | All RS drain from Gaps and Locks halved | WR ≥ 2 | Meaningful investment. The factions are investing in substrate maintenance. Gap/Lock drain reduced from ~−9.5 to ~−4.75/season. |
| 3 | RS +2/season at Accounting (Edeyja active Mending) | WR 3 | Full recognition. Active Edeyja Mending. The peninsula has accepted its constitutive nature. The only viable endgame RS path (see ms_budget.md Scenario C). |

---

## Why WC 3 Functions as a Budget Enabler

Per ms_budget.md (revised 2026-04-24 — see Conclusion section):

**The Scenario B peak-drain figures describe the un-disciplined Thread-aggressive profile.** A faction running 4 Dissolutions/year, 2 active Locks, sustained Thread warfare in mass battle, and no Gap-closure discipline produces ~−21 to −23/season drain at WC 0. Against this profile, WC 3's +2/season + halved Gap/Lock drain + community Mending recovery is necessary.

**A faction operating with substrate discipline produces a different drain profile entirely.** Self-mitigation via Dissolution restraint, active Gap closure, Lock cleanup, battle Thread minimization, ≤2 ops/turn in mass battle, and TS 90+ practitioner management produces drain ~−2 to −4/season — recoverable by 2–3 active Menders without WC.

**This produces three viable late-game paths** (full spec in ms_budget §Conclusion):
1. **Disciplined non-Warden play** — Path 1 substrate discipline alone.
2. **WC 3 with substrate discipline** — Path 1 plus Warden cooperation. Maximum survivability margin.
3. **WC 3 with successful Wager** — npc_behavior §5.2 Edeyja Arc E. Active Knot + Grand Contest using Projection-Consequence-Solidarity + verifiable future commitment. The "staked credit" path that allows Scenario B operational profile while WC 3 provides the budget.

**WC 3 does not remove substrate discipline; it shifts the discipline target.** The Path-2 player operates within Continuity-aligned bounds and Edeyja cooperates by default. The Path-3 player commits to a future restoration outcome and Edeyja extends present trust against that commitment. The Path-4 player (WC 3 without discipline, without wager) walks into Edeyja Arc D Confrontation and loses the alliance — the trap state.

**WC decay clause** (§victory_v30 §6 + npc_behavior §3.4 cross-reference): WC decreases when the player performs operations Edeyja's Continuity Conviction registers as disruptive — Dissolution of living being (−1 WC), Lock on being without consent (−1 WC), POP that disrupts substrate-stable configurations (−1 WC), unmitigated Gap creation persisting >2 seasons (−1 WC), Substrate Saturation events involving player practitioner (−1 WC). Cap −2 WC per season from these sources. WC reaching 0 from this path: Arc D Confrontation fires; Warden Outpost Outreach ceases; Mending Community recovery suspended for 2 seasons.

[EDITORIAL: ED-741 — WC reframed from "singular endgame survival path" to "budget enabler with three-path late-game architecture." Source: 2026-04-24 audit conversation. Prior framing implied WC 3 was a survival floor; the underlying ontology supports three viable paths (disciplined non-Warden, cooperative WC 3, wagered WC 3). Adds WC decay clause that was previously implicit but unspecified.]

---

## The IP/Expedition Tension

The mechanism that makes the two contests feel simultaneous:

| Resource | Contest 1 (Sovereignty) Demands | Contest 2 (Survival) Demands |
|---|---|---|
| Military assets | Defense against rival factions, Altonian Vanguard | Expedition escort, Southernmost protection |
| Faction actions | Domain Actions for territorial control | Expedition support, Warden cooperation |
| Player time (scenes) | Political maneuvering, combat, investigation | Expedition participation, Mending operations |
| Practitioner Coherence | Battlefield Thread operations (Lock, Dissolution), intelligence gathering | Non-Mending Thread ops at Southernmost; aggressive substrate work. Mending does not cost Coherence but competes for scene slots and incurs fatigue. |

As IP rises (driven by civil war — peninsular_strain §3.2: IP +3/season during inter-faction battles), military attention must shift to border defense. But Southernmost expeditions require military escort. A faction fighting a war and mounting expeditions simultaneously must split resources.

This tension is not a design flaw — it is the game's central strategic question: how much sovereignty do you sacrifice for survival?

---

## WC State as Primary UI Indicator

**For videogame implementation:** WC must have equal UI real estate to RS. These are the survival contest's two axes:
- **RS** = how damaged is the substrate (the problem)
- **WC** = how much are you doing about it (the response)

Every other track (Mandate, Influence, Wealth, Military, Stability, TC, IP, PT, Strain) is the political contest. RS and WC are the survival contest.

Proposed UI placement: RS and WC displayed alongside each other in the persistent world-state HUD. Not in a faction sidebar. Not in a secondary menu. On the main screen, always visible, updated at Accounting.

---

## Faction Relationships to WC

| Faction | WC Orientation | Strategic Implication |
|---|---|---|
| Varfell | Primary WC driver (WR gates WC) | Varfell's engagement with Askeheim is the prerequisite for WC advancement. Path B (Southernmost Dominion) makes WC Varfell's primary strategic objective. |
| Wardens/Edeyja | WC beneficiary and executor | WC 3 activates Edeyja's Mending. Edeyja Burnout (ARC-S34) is the hidden fail state: if Edeyja reaches Coherence 0, WC 3's +2/season stops. |
| Crown | WC enabler (Thread Liaison PP-436) | Crown can designate Thread Liaison, crediting allied Thread ops. Crown's political interest may align with WC if RS threatens sovereignty. |
| Church | WC resistor (institutional) | Church's Certainty framework opposes Thread engagement. TC advancement competes with WC investment. But at RS Critical, even Church factions face the survival question. |
| Hafenmark | WC pragmatist | Hafenmark's consequentialist framework supports WC investment when RS threatens trade infrastructure. |
| Niflhel | WC adversary (structural) | If Harvest = Dissolution Residue collection, Niflhel's strategic interest diverges from RS preservation. Niflhel is structurally incentivized to maximize Dissolution activity just short of Rupture — the only faction whose interest opposes WC. |

---

## Arc Register Cross-References

| Vector | WC Relevance |
|---|---|
| ARC-S15 (Southernmost Spiral) | RS ≤ 50 cracking timeline. WC engagement prevents cracking. |
| ARC-S32 (Mending Trap) | Individual heroism insufficient. WC = collective response. |
| ARC-S33 (Lattice of Enemies) | Belief conflicts block collective Thread operations. WC requires cross-faction cooperation that Beliefs may prevent. |
| ARC-S34 (Edeyja Burnout) | WC 3's +2/season depends on Edeyja. Edeyja Burnout terminates WC 3 benefit. |
| COLLISION C (Tutoring + Southernmost) | Torben loss + Ritual failure = RS +8, cascading crises. WC state determines recovery capacity. |

---

## Editorial Resolution — Open Questions

Per thread_constitutive_integration_analysis_v2.md:

1. **Niflhel Harvest = Dissolution Residue collection:** Resolved YES. The Quiet One arc (arc_expansion_v1) designs Thread extraction behavior. Niflhel is the game's accelerationist faction — structurally opposed to the Wardens. NPC Niflhel AI must have an RS-monitoring subroutine that gates Harvest intensity (see arc_expansion_v1 Quiet One Arc B/C for thresholds).

2. **WC documentation approach:** Resolved as this document (centralized) plus in-place cross-references from victory_v30, params_board_game, and UI/UX reference.

---

*This document explicitly states what the game's design implies: WC 3 is the singular endgame survival path. The survival contest has one answer.*
