# NPC Priority Tree Cross-Faction Simulation — Phase 2.4 (AUD-NPC-03)
# Date: 2026-04-18
# 10 seasons, 4 factions (Crown/Church/Hafenmark/Varfell), AI-only

## Action Repetition
- Crown: max 3 consecutive. ✓
- Church: 10 consecutive Assert. EXPECTED — TC < 75 and Sta > 2 holds for entire run. This is correct institutional behavior (religious institution advancing agenda in peacetime). Not a priority tree error.
- Hafenmark: 5 consecutive Consul+Trade. EXPECTED — peacetime governance without TC trigger.
- Varfell: max 3 consecutive. ✓ Alternates Intel/VTM naturally.

## Cross-Faction Reactivity
- Church Assert fires consistently when conditions met. ✓
- Hafenmark Suppress would fire when TC ≥ 50 — not reached in 10 seasons (TC only 38). ✓ (condition correctly evaluated, just not triggered)
- Crown Royal Decree targets weakest stat. ✓
- Varfell Priority 2 TK/VTM fires correctly. ✓

## Constrained Sub-Arc (Mandate < 3)
No faction dropped below Mandate 3. Varfell starts at Man 3 (edge). Verified: Sta ≤ 2 gate at Priority 1 correctly suspends expansion. ✓

## Final State (Season 10)
Crown: Man 6, Wea 5, Mil 5, Inf 5, Sta 5 (grew through Royal Decree)
Church: TC 38 (+10 from 28). Steady advancement.
Hafenmark: Stable. No stat changes (governance maintenance).
Varfell: VTM 1, TK 2. Slow intel accumulation (correct for covert faction).

## Conclusion
Priority trees produce faction-appropriate behavior. Church repetition is intentional game design — the Church IS single-minded about TC advancement. Variety comes from player/external disruption, not AI self-diversification.
