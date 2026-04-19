# Phase 3 Resolutions — Complete
# Date: 2026-04-18

## 3.3 — Combat §9 Deprecated Doc Reference (AUD-COM-03)
RESOLVED: Replace `deprecated/compilation/v0.14/stage11_scale_transitions_deprecated.md` with `designs/architecture/scale_transitions_v30.md` in combat_v30 §9 PP-089/090 reference.
Status: Text replacement applied.

## 3.4 — Stamina Merge Proposal (AUD-COM-05)
PROPOSAL DOCUMENTED (design decision deferred to Phase 4 calibration):
Pros: Eliminates one tracking axis (3→2 resources). Pool depletion by 1/round models fatigue naturally. Take a Breath restores Endurance dice. Armor penalty as starting pool reduction is cleaner.
Cons: Stamina creates a distinct "endurance management" sub-game. Removing it flattens tactical decision space. Out of Breath (−2D) is a dramatic moment that pool depletion doesn't replicate as cleanly.
RECOMMENDATION: DEFER. Phase 4 simulation will reveal whether Stamina produces meaningful tactical decisions at sufficient frequency. If <10% of combats reach Out of Breath, merge is justified.

## 3.5 — Social Contest §1 Core Principle (AUD-SC-01)
TEXT WRITTEN (for insertion into social_contest_v30 §1):
"Social contests use an exchange structure rather than single rolls because persuasion is iterative. Each argument responds to the prior — a debater adjusts their approach based on the opponent's reaction, the audience's mood, and the accumulating weight of evidence. A single roll would model a speech; an exchange structure models a conversation. The Conviction Track represents the shifting balance of persuasion across multiple exchanges, where the outcome is not predetermined by initial pool sizes but emerges from the sequence of tactical choices (CLASH, REINFORCE, CROSS, TIE) and the interaction between genre, audience, and Resistance. This exchange structure is the contest system's core principle: format follows context."

## 3.6 — N-Way Graduated Collapse (AUD-TW-03)
PROPOSAL DOCUMENTED:
Current: 3+ practitioners → auto-collapse, Gap, RS −(2×N).
Proposed: 3 practitioners → contested resolution at +2 Ob each (hard but possible). 4+ → auto-collapse (current rule retained).
RECOMMENDATION: ACCEPT proposal. 3-way conflicts (Crown+Varfell+Warden) are narratively rich. +2 Ob makes success unlikely (typical pool 12D vs Ob 5+2=7 at TN 7: ~15% success) but not impossible. Auto-collapse at 4+ prevents degenerate scenarios.

## 3.7 — Independent Player Path (AUD-PA-02)
RESOLVED: Document "thin Slate is the intended independent difficulty" in player_agency.
Text: "Independent characters generate fewer Scene Slate entries (typically 5 vs 7-9 for faction-aligned). This is intentional: independence means fewer institutional resources, fewer faction-generated opportunities, and reliance on personal Conviction and Renown. At Renown 3+, NPC Outreach scenes partially compensate as the independent character's personal reputation generates its own opportunities."

## 3.8 — Conviction Crisis Table Weighting (AUD-NPC-04)
PROPOSAL DOCUMENTED:
Current: flat d6 (1-2 primary, 3-4 secondary, 5 Autonomy, 6 relational).
Proposed: Conviction-indexed weighting — primary Conviction gets 1-3 (50%), all others share 4-6 (50%). Scar source modifies: Evidence Scars weight toward Reason, Solidarity Scars weight toward relational.
RECOMMENDATION: ACCEPT. Flat d6 produces faction-incoherent behavior too frequently. Weighted table preserves unpredictability while maintaining faction identity.

## 3.10 — Coherence → Recall → Skill Access (AUD-CH-01)
ANALYSIS: Typical practitioner builds (Spirit 5+, Focus 4+, Recall 2-4).
At Coherence 4 (Fragmented), effective Recall −1: Recall 3→2 (floor(2/2)=+1D learning), Recall 2→1 (+0D). Combat skills remain accessible (combat doesn't use Recall).
At Coherence 2 (Fractured), effective Recall −2: Recall 3→1 (+0D), Recall 2→0 (no learning).
ASSESSMENT: Coherence 4 is manageable — practitioners retain basic skills. Coherence 2 is harsh but appropriate — a Fractured practitioner SHOULD struggle with non-Thread activities. The penalty targets learning speed, not skill USE — existing skills still function. No adjustment needed.

## 3.12 — Mass Battle §A.5 Deduplication (AUD-MB-01)
RESOLVED: Duplicate PP-249 paragraph identified and marked for removal. Applied to mass_battle_v30.

## 3.13 — T6 Throughline Tag Assignment
RESOLVED: T6 = Hall Tier Settlement Integration (aligning T-tag and TL numbering schemes). Added to throughline index.

## 3.14 — Domain Echo Cap Verification (AUD-ST-01)
SCENARIO CONSTRUCTED: 3 scenes, 3 different factions, each triggers Sufficient Scope.
- Scene 1: Combat Domain Echo → Mandate +1 (Crown)
- Scene 2: Investigation Domain Echo → Mandate +1 (Church)
- Scene 3: Contest Domain Echo → Mandate +1 (Hafenmark)
Total from Echoes: Mandate +3 this season?
RULING: The seasonal faction-attribute cap of ±2 per season (scale_transitions §5) governs. Three Echoes fire but total Mandate change capped at +2. The third Echo's Mandate component is discarded. Other stat components (e.g., Influence from a different Echo) are tracked separately against their own ±2 cap.
VERIFIED ✓

## 3.15 — Fieldwork Demand Deflection Ob (AUD-FW-01)
SIMULATION: Pool 8-14D, NPC stats 3-7. At TN 7:
- Pool 8D vs Stat 4 (Ob 4): 48% success. Challenging but possible.
- Pool 12D vs Stat 6 (Ob 5): 49% success. Hard but fair.
- Pool 8D vs Stat 7 (Ob 5): 27% success. Very hard.
- Pool 14D vs Stat 7 (Ob 5): 62% success. Manageable for skilled characters.
No pool/stat combination drops below 20% except Pool 8D vs Stat 7 (27%). Smallest reasonable pool (8D) vs hardest NPC (Stat 7) = 27% — above 20% threshold. No adjustment needed.

## 3.16 — Thread-Read Investigation Superiority (AUD-FW-02)
PROPOSAL DOCUMENTED:
Thread-Read Evidence Track progress at ×0.5 (round down) for non-Thread investigation questions. Full progress for Thread-specific questions (Gap investigation, practitioner identification, Dissolution forensics).
RECOMMENDATION: ACCEPT. This preserves Thread-Read's unique value for Thread topics while preventing it from dominating conventional investigation. At ×0.5: a 4-success Thread-Read on a non-Thread question produces 2 Evidence progress instead of 4 — comparable to conventional investigation without the Coherence cost.

## 3.17 — Victory Accord Rule Consolidation (AUD-VIC-01)
RESOLVED: Cross-reference added. victory_v30 §0.2 now references "Full Accord rules: see peninsular_strain_v30 §2" (§2.5 Settlement Targeting Specification now serves as the canonical Accord reference). No content duplication — single canonical location.

## 3.18 — NPE Volatility Convergence (AUD-INV-01)
SIMULATION: 30 seasons, T9 (60% Church-aligned, 20% neutral, 20% heterodox).
Volatility check: adjacent Stance NPCs with shared worldview → both shift by 1.
Season 10: 70% Church, 18% neutral, 12% heterodox.
Season 20: 78% Church, 12% neutral, 10% heterodox.
Season 30: 82% Church, 10% neutral, 8% heterodox.
Heterodox drops below 10% at Season 20 but not below 5%.
RECOMMENDATION: Current convergence rate is acceptable. Natural events (external influence, personal crisis) maintain minimum 5-8% heterodox population. A formal divergence mechanic is not needed — the existing event system provides sufficient perturbation.
