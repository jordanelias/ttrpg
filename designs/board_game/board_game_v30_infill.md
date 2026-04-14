<!-- INFILL — prose/rationale extracted from board_game_v30.md -->
<!-- Skeleton: board_game_v30.md -->

# VALORIA: THE BOARD GAME
## Institutional Mandate — Uphold / Appease (PP-189)
## Version: v0.6 (ST-BG/INT + P-12–P-32 applied in-place; PART THIRTEEN and PART TEN/ELEVEN eliminated; pure mechanical spec)
## Status: WORKING DESIGN — read straight through. No appendix sections.
## v0.4 → v0.5 → v0.6 Transition Document
**Scope:** Full system coherence, legibility, cognitive load, mechanical cascade crunch, inconsistencies and contradictions, gaps and ambiguities, emergent scenario simulations with branching dice rolls, precedent game comparisons, equity and balance analysis, hybrid mode intersection.
# PART ONE: CRITICAL SYSTEM CORRECTIONS
## CORRECTION 1 — Dice System (d10, supersedes all d6 language)
**Net successes** = (count of 7-9) + (2 × count of 10s) − (count of 1s). Net successes can be negative; negative net = 0 for degree purposes, treated as Failure (see Correction 3).
**Majority-1s override (updated language):** If dice showing 1 outnumber dice showing 7-10 in the same roll, the result is **Critical Failure** regardless of net success count: apply Failure consequences plus one additional consequence at Game Master discretion (a Standing loss, a stat −1, or a triggered faction instability).
*Rationale for preserving the override: the subtraction already degrades outcomes, but the override captures the feel of something going profoundly wrong — multiple omen dice firing when the hand is weak. On d10 this is rare (P(1) = 10%, P(7-10) = 40% per die), which is appropriate: catastrophic outcomes should be uncommon, not endemic.*
## CORRECTION 2 — Ob Minimum = 1 (Ob0 is impossible)
Every action retains at least one point of resistance. This changes the effective ceiling of modifier stacking. Factions with multiple simultaneous bonuses (e.g., Church in T3 at Theocracy Counter 30–49: doctrine-aligned −1 Ob, Church-held territory −1 Ob, Ethical Framework −1 Ob) previously could theoretically reach Ob 0 on certain actions. With the Ob1 floor, those three stacked modifiers on an Ob 3 action = Ob 1 (not Ob 0), which still has a 74% success rate for a pool of 3. The floor prevents guaranteed success while preserving strong advantages.
> **Clarification (PP-042):** "Military victory alone produces no Theocracy Counter or Rendering Stability change. Thread operations performed during a battle produce standard Rendering Stability changes per §A.10 regardless of battle outcome. A Church army using Thread-enhanced soldiers (e.g., Weaving unit Discipline) generates Rendering Stability drift from those specific Thread operations — not from the act of winning."
## CORRECTION 3 — Degree Table Update (incorporating d10 and negative net successes)
> **P-32:** **Victory condition clarification:** BG victory = reach declared VP total OR opponent faction eliminated. Hybrid victory = BG victory PLUS personal arc resolution. A BG-only win with unresolved personal arc = Hollow Victory (valid but narratively incomplete).
# PART TWO: INCONSISTENCIES AND CONTRADICTIONS
## I-01 — Majority 1s Rule uses d6 language
## I-02 — Patience Protocol body vs P-07 Patch (Cap contradiction)
## I-03 — Casus Belli Expiration vs "Permanent Until Used"
**Error:** The Treaty Betrayal table lists "Free Casus Belli vs betrayer — Immediate, **permanent until used**." The Casus Belli rules (BG-E-NEW-02) state: "Casus Belli Expiration: **2 seasons after acquisition if unused** for a Military action." These directly contradict each other.
**Decision (PATCH P-14):** Treaty-based Casus Belli (earned from pledge betrayal) is permanent until used. All other Casus Belli (earned from Brutal disposition, fabricated Heresy Investigation) expire after 3 seasons unused. Varfell's Patience Protocol Casus Belli expires on Riskbreaker exposure. **The distinction is that treaty betrayal creates a permanent grievance; other acquisition routes are tactical windows.**
## I-04 — Faction Collapse: "Attributes Freeze" Contradicted by "Mandate Drops to 0"
## I-05 — Battle Resolution: Both Sides Roll, No Clear Victory Determination
## I-06 — Restoration Victory Rendering Stability ≥ 50 vs Rendering Stability Starting at 72
## I-07 — Phase 4 Tiebreaking Contradiction (Simultaneous vs Sequential for 3+)
## I-08 — Parliamentary Manoeuvre Free Interrupt Scope
> **P-17:** **Hafenmark Decree scope:** Decrees affect only Varfell Territory factions. Cross-territory Decrees are invalid — they are not issued.
## I-09 — Information Asymmetry Boundary Roll uses d6 while Main System is d10
**Concern:** "A stat at exactly 4: roll **1d6** at point of observation. 1–3 = Poor; 4–6 = Good." This is correct to use d6 here — it's a 50/50 meta-mechanism that doesn't feed into success-counting. However, the document should explicitly note this as a d6 exception.
**Correction (PATCH P-20):** Add "(This roll uses a d6, not the standard d10 — it is a coin-flip mechanism, not a success-count roll.)" to the boundary ambiguity rule.
# PART THREE: GAPS AND AMBIGUITIES
## G-01 — Standard Action Obs Not Stated in B3
## G-02 — Prosperity: Undefined Track
**Location:** B3 (Govern outcomes), B2 Territory Map (T11: "+1 Prosperity/season uncontested"), B9 (Community Projects table).
## G-03 — VTM "Thread-active territory" Undefined
**Gap:** "Tribune in **Thread-active territory** while in Thread Resonance: +1 VTM." The term "Thread-active territory" appears only here. It could mean: (a) the specific territory where a Thread operation occurred this season, (b) any territory in Thread Resonance, or (c) any Einhir site (T9, T12, T13, T14).
**Correction (PATCH P-23):** "'Thread-active territory' means any territory in which a Thread operation was performed this season (not merely adjacent territories). Varfell must have a Tribune card played IN that territory (Inward or Outward) to gain VTM — not merely nearby. This requires Varfell to place intelligence operations where Thread activity is occurring." Add: "Exception: T9 (Varfell) counts as permanently Thread-active for VTM purposes at VTM 2+ (per the 'always in Thread Resonance' benefit). Bootstrapping VTM in Season 1 counts as Varfell being Thread-active in T9 regardless of VTM level."
## G-04 — Thread Operation Step 3 "−1 Ob to THIS operation" Ambiguity
**Gap:** "If any [against temporal flow] conditions apply: incur Thread Debt token (placed in territory, **−1 Ob to THIS operation** as substrate resistance)." The phrase "−1 Ob to THIS operation" is genuinely ambiguous. It could mean: (a) the Thread Debt makes this operation EASIER (Ob reduced by 1) because the substrate is already stressed; or (b) this is a formatting error and should be +1 Ob. A reduced Ob on an operation that's causing world damage is counterintuitive.
## G-05 — Heresy Investigation with No Valid Target
**Gap:** Church can open a Heresy Investigation (free from Overwhelming Decree) against a territory with no Restoration Presence and no visible Thread activity. The investigation has no one to investigate. Does it close immediately? Does it open and remain dormant?
**Correction (PATCH P-25):** "A Heresy Investigation requires a named target: a faction active in that territory this season, a specific Non-Player Character, or a practitioner with Thread Sensitivity > 0. If no valid target exists in the territory, the Investigation cannot be opened. Church must choose an alternate valid territory. If Non-Player Character artificial intelligence selects an invalid territory, Game Master redirects to the territory with highest aggregate Church-concerning activity (Thread operations, Restoration Presence, or Varfell Tribune)."
## G-06 — Forgetting Check "Spirit Proxy" in Board Game Mode
- Varfell: VTM level (roll VTM dice, e.g., VTM 3 = 3d10).
- Any other faction: Wealth ÷ 2 (rounded up) — resources sustain cognitive continuity through unfamiliar substrate strain.
## G-07 — VTM Bootstrapping Success Rate on d10
- Partial: Varfell gains a **'Latent VTM' token.** On any subsequent successful Tribune Inward in T9 within the next 2 seasons, the Latent VTM converts to VTM +1. If not converted within 2 seasons, the token is lost.
## G-08 — Restoration Community Weaving with Multiple Presence Markers and Ob1 Floor
**Flag (no patch required):** Note this explicitly in the Restoration faction sheet as a design goal. "At 2+ Presence markers in a territory, Community Weaving is reliable. The challenge is building and maintaining that Presence, not the roll itself."
## G-09 — Standard Muster Ob Not Stated
## G-10 — Varfell Starting Stats: Mandate and Wealth Discrepancy
**This is a canonical decision required from the designer.** The board game intentionally represents factions' political starting positions, which may differ from their "natural" stats. Varfell is politically outmaneuvered at game start (isolated, low mandate legitimacy) while the timeline's stats represent their fuller potential. Both values have narrative justification.
## G-11 — Incomplete Institutional Pressure Pressure Advancement Table
> **P-28:** **Invasion Pressure (Institutional Pressure) Advancement Formula (applied at Accounting Step 4):**
## G-12 — Battle Resolution: No Comparison Mechanic When Both Sides Roll
# PART FOUR: COGNITIVE LOAD ANALYSIS
## Load Assessment by System
- Card hand management: intuitive. Five cards, one Recess. New players understand this within two seasons.
- Degree table: clean four-outcome system. Overwhelming/Success/Partial/Failure maps directly to player intuition.
- Thread Operation Procedure (8 steps): the laminated card is essential and sufficient. Load drops from 7/10 to 3/10 with physical card.
- Co-Movement Cards (three simultaneous effects): the three-column format is readable. Risk is cognitive overload when multiple Thread operations fire in the same season (multiple draws, each with 3 effects). Load ≈ 5/10 per draw, cumulative.
- Elske/Torben tracking: two off-board cards with ~6 conditions each. Manageable on dedicated reference cards. Load ≈ 4/10.
- Phase 4 priority order (7 tiers): the priority ladder is long but the within-tier resolution is clear. Physical tracker card recommended. Load ≈ 5/10.
> **P-31:** **Co-Movement deck refresh:** Deck reshuffles when empty (no permanent depletion). Each card drawn: practitioner resolves the stated effect plus the three-dimensional auto-effect. Cards cannot be held between seasons — draw, resolve, discard.
- Klapp Trajectory: three-branching decision tree with conditional activation, cooldown states, multi-season consequences. This is the single most complex new system in v0.4. Load ≈ 7/10.
- Cascade Phase (Hybrid only): 5 sequential steps with ledger tracking from personal scenes. Load ≈ 7/10 in hybrid, 0/10 in board game.
- Phase 5 Accounting (13+ steps): at 13 steps with sub-steps (8b, 9b, 10b), this is the most procedurally heavy part of the game. **This is a pacing risk.** At 3-5 seasons per session, accounting fires 3-5 times per session plus Year-End. Experienced players manage this in 5-10 minutes; new players may need 20+.
1. **Collapse Accounting Steps 8, 8b, 9, 9b, 10, 10b into a single "Events and Emergence" step** with a checklist. These all happen in the same window and separating them adds procedural friction without clarity benefit.
2. **Theocracy Counter advancement tracking:** The Theocracy Counter formula has 9 input sources. A dedicated Church-player Theocracy Counter tracker card (each season, tick boxes for applicable sources) prevents recount errors.
3. **Cascade Phase ledger:** In hybrid mode, a physical "Cascade Ledger" card (Game Master holds it throughout the Personal phase, records consequences as they fire, applies in bulk) is essential. Without it, the 5-step Cascade accumulates undocumented debts.
**Overall cognitive load estimate (board game only):** 6.5/10 with full reference card set. 8.5/10 without.
# PART FIVE: MECHANICAL CASCADE CRUNCH
## Cascade Test 1: Church Overwhelming Decree Chain (Season 7, Theocracy Counter 36)
3. Non-Player Character artificial intelligence PATCH P-10 fires: Church opens free Heresy Investigation (using PATCH P-25 to verify valid target — T14 has Restoration Presence this season). HI opened against T14.
5. Theocracy Counter +1 from T3 control (accounting step, not immediate). Theocracy Counter: 36 → 37.
## Cascade Test 2: Reformed Settlement Chain (Hafenmark, RDT 5, Season 12)
**Setup:** Theocracy Counter 52 (Assert/Suppress active). Hafenmark RDT 5. Hafenmark declares Reformed Settlement in Phase 2.
**Church artificial intelligence Priority at Theocracy Counter 52:** Priority 1: Assert (fires this season). Church Asserts: Theocracy Counter +1 at accounting.
**Church chooses Resist (Game Master determines; consistent with Church conviction and Theocracy Counter > 50 assertive posture):**
7. Hafenmark holds 4+ Deed Tokens (if Deed 3 = Reformed Settlement, they now hold it). Hafenmark also holds Deed 2 (Public Instability ≥ 3 — current Public Instability 5). Check all three Path A deeds: RDT ≥ 4 (RDT 6 ✓), Public Instability ≥ 3 (Public Instability 5 ✓), Reformed Settlement (✓). **Hafenmark has all three Path A Deeds simultaneously.**
## Cascade Test 3: Varfell VTM 5 + Co-Movement + Rendering Stability Trigger
7. CM-19 Epistemic: "Acting faction must reveal which Thread operation type was used." Varfell must reveal: Weaving. CM-19 Temporal: "If this operation was Dissolution FR: additional check fires." Not Dissolution — no additional fire.
## Cascade Test 4: Church Theocracy Counter 80 Territorial Seizure
> **P-30:** **Theocracy Counter 80 Territorial Seizure Partial result:** Territory is not seized. Church places 1 Templar Staging Token in the territory (the Templars have moved to the border). The controlling faction may contest this deployment: any Military card play in that territory next season removes the Staging Token a
**Setup:** Theocracy Counter 80 crosses this season. Per batch_ad_resolutions.md: per-territory roll at Theocracy Counter 80, not blanket takeover.
**Gap:** Theocracy Counter 80 seizure Partial resolution not defined. Per batch_ad_resolutions.md: "per-territory roll at Theocracy Counter 80, not blanket takeover. Integration into event deck confirmed." But Partial outcome for the seizure roll is not specified in the document.
**Correction (PATCH P-30):** "Theocracy Counter 80 Territorial Seizure Partial: Territory not seized, but Church establishes Presence (places 1 Templar Staging Token in territory). Controlling faction may contest this Templar deployment at their next Military card play."
# PART SIX: EMERGENT SCENARIOS (Branching Dice Rolls)
## SCENARIO A: The Klapp Awakening — Church-Varfell-Wardens Triangle
**Preconditions:** Varfell VTM 3 (publicly visible). Varfell has a Tribune Inward in T9, adjacent to T3. This season, Restoration Community Weaving fires in T9 (adjacent to T3). Klapp Event Card draw conditions met: Thread operation within 1 territory of T3, Theocracy Counter ≥ 30, no Heresy Investigation opened this season.
- **No mechanical change beyond Theocracy Counter +1.** The investigation dies. Restoration's Thread work in T9 continues undetected at the deepest level.
    - **Season 12:** Second Klapp Discovery Roll. Roll: 5d10: 4, 2, 1, 6, 3 → -1 net. Catastrophic: majority 1s? Count: one 1, zero 7-10s. One 1 > zero hits. **Critical Failure / Majority 1s.** Heresy Protocol fires.
    - Non-Player Character artificial intelligence: Church Priority 1 is Assert (Theocracy Counter 37 < 50 — no mandatory Assert yet). Priority 3: Govern T3. Protecting Klapp doesn't conflict with either. Non-Player Character artificial intelligence protects. Himmensendt Renown −1.
    - Season 13: Third Discovery Roll. 5d10: 9, 7, 7, 5, 10 → 1+1+2 = 4 net. Overwhelming. Klapp has independently awakened to Thread sensitivity. **Klapp's Thread Sensitivity is now canonically Stirring.** This is a major narrative event. Game Master records: Klapp joins the world's covert practitioners.
  - Roll B (alternative failure): 5d10: 2, 3, 5, 1, 4 → -1 net. Critical Failure immediately at Season 11. Heresy Protocol fires early.
**BRANCH C: Church chooses Trajectory C (Collaborate — only if Varfell VTM ≥ 4 OR Warden Cooperation ≥ 2)**
- **This is an institutional tipping point.** Church just enabled the very thing it has been suppressing.
- Downstream: Riskbreaker Priority 3 fires next season (Theocracy Counter 36 > 50? No — Theocracy Counter 36 < 50, so Riskbreaker Priority 3 condition not met). Riskbreakers do not respond.
**EMERGENT CONCLUSION:** Trajectory C creates a two-faction alliance (Varfell-Restoration + covertly-aligned Church) that the ruleset rewards. The Klapp event card is excellently designed — all three trajectories are narratively coherent and mechanically distinctive. The branching paths produce genuinely different game states.
## SCENARIO B: Varfell Patience Protocol Climax — Season 14, VTM 4+
This happens at the start of Phase 1 (Patience Counter declaration). VTM 5 is publicly revealed (already visible since VTM 3). VTM 5 grants: "Once/game: choose the Actualized dimension outcome of one Co-Movement card draw."
**This season: Varfell plays Tribune Outward in T1 (Spy — 4 Player Character ability: "Execute one Spy action in any territory regardless of adjacency").**
Actually, 4 Player Character was spent last season. This season Varfell uses 6 Player Character for VTM advancement, then also plays a regular Tribune action.
Condition: Tribune in Thread-active territory (T14, Restoration Weaving occurred) while in Thread Resonance (Varfell is in Thread Resonance from T14 operation in adjacent T9). VTM +1 check... wait, VTM is already being advanced via Player Character spend. Can VTM advance twice in one season? **Gap identified.**
**PATCH NEEDED (P-31):** VTM can only advance once per season regardless of source. If Player Character spend (6 Player Character → VTM +1) and Tribune-in-Thread-active-territory both trigger in the same season, only one advancement applies. Player Character spend takes priority (it was declared first at Phase 1).
**Varfell now holds complete intelligence on Restoration.** Varfell Patience Protocol tone: "This faction sees everything and acts rarely."
**EMERGENT CONCLUSION:** The Patience Protocol creates a faction that wins by being a power broker rather than a direct aggressor. The intelligence gathered through sustained inaction is more valuable than any single Tribune Investigate. The system is working as designed.
## SCENARIO C: Institutional Pressure Crisis Triple Response — Season 11, Institutional Pressure 68
- Löwenritter: Legionary Outward T4 (March to T4). Legionary Outward T5 (reinforcement toward border). Tribune Inward T4 (Requisition Order — wrong card; Tribune Requisition is Inward in Church territory only).
Institutional Pressure advances: from where? No explicit Institutional Pressure formula seen. Applying PATCH P-28: Institutional Pressure advances +2/season when Institutional Pressure > 60. Institutional Pressure: 68 → 70.
- If Löwenritter successfully holds T4 (Overwhelming March established control): Vanguard must fight through T4 to advance. Löwenritter Military 6 vs Altonian Vanguard Military 5 Discipline 5: contested battle.
# PART SEVEN: COMPARISON TO PRECEDENT GAMES
## Terra Mystica / Gaia Project
**Comparison:** Faction asymmetry and resource conversion chains. Valoria exceeds both in narrative depth and faction distinctiveness but carries similar risks: analysis paralysis from asymmetric options, and faction A/B comparisons feeling unfair before experience reveals the balance. **Recommendation:** Like Terra Mystica, Valoria needs a "first session faction guide" — simplified recommended opening plays per faction to prevent new players from building into corners.
## Root
**Comparison:** Highly asymmetric faction design with an interconnected political board. Root's faction design principle — each faction has a different win condition that requires different interaction patterns — is fully present in Valoria. Root achieves lower cognitive load through simpler individual mechanics; Valoria trades that simplicity for thematic richness.
**Key lesson from Root:** Root's Vagabond is divisive in competitive play because it scores independently of board control. Valoria's Restoration Movement occupies a similar design space (scores through Presence, not control). The Restoration player must have strong guidelines for how to participate meaningfully without purely disrupting others — the co-victory pairings in B15 are the correct mechanism, but they should be emphasised more prominently in faction setup.
## A Feast for Odin / Feast Games
## Here I Stand / Virgin Queen
**Comparison:** Multi-faction historical political games with intersecting win conditions. Valoria's closest precedent in structure. Key lessons:
- HIS manages faction asymmetry by making faction interaction the primary game (you win by dealing with other factions, not by executing your faction's plan independently). Valoria achieves this through the clock system (Theocracy Counter and Institutional Pressure threaten everyone, requiring collective response) but could strengthen it through clearer "collective loss conditions" that force even winning factions to cooperate.
## Twilight Imperium 4th Edition
**Comparison:** Political factions, strategic autonomy, emergent narrative. Valoria is more focused and has better fiction integration than TI4 but serves a similar desire: "play a political-historical faction through a complete arc." TI4's biggest design success is that every player has a meaningful story to tell at the end of the game regardless of victory. Valoria achieves this through Hollow Victory and the Deed Token system — even a player who fails their primary victory path can have played a meaningful political role. This is commendable.
# PART EIGHT: EQUITY AND BALANCE ANALYSIS
## Church Holy State Victory — Pace Analysis
**Without active opposition:** Average ~2/season before Theocracy Counter 50, ~3/season after. Estimated victory: Season 25–30.
**Assessment: Church Holy State Victory is NOT achievable in a standard 12–20 season campaign without significant opponent assistance or Hafenmark's complete failure.** The Dual Theocracy alternate victory (Theocracy Counter ≥ 60, AER 5, Institutional Pressure ≤ 30) is slightly more achievable but requires Institutional Pressure suppression simultaneous with Theocracy Counter expansion — a tension the design correctly builds, but the win condition may be too hard.
**PATCH P-32 (balance):** Reduce Church Holy State Theocracy Counter requirement from 70 to 65, OR increase starting Theocracy Counter from 22 to 28 (giving Church 6 seasons of head start). The latter is preferred — it matches the narrative (Church predated independence; it should enter the game closer to full institutional power). At Theocracy Counter 28 vs. target 65: gap 37 points. At 2-3/season: 12-18 seasons. Achievable within campaign length.
## Löwenritter Post-Coup Victory — Structural Assessment
**Regency Resolution requires:** All 5 Deeds + legitimate succession. Deed 5 (succession candidate) requires Elske or Torben Loyalty ≥ 6.
**Elske starts at Loyalty 4, Torben at 3.** Elske needs +2. But she can only return when Loyalty ≥ 6 AND Institutional Pressure < 60. Institutional Pressure starts at 20 and rises. By the time Löwenritter is active (coup fires), Institutional Pressure has typically risen to 40-60. Getting Elske back requires both Loyalty management AND Institutional Pressure management — two parallel tracks that the Löwenritter has limited tools to influence (restricted hand with no Diplomat, no Senator for Diplomacy).
**The Löwenritter depends on other factions (especially Crown and Hafenmark) managing Institutional Pressure and Elske's Loyalty.** This creates genuine dependency and co-victory incentive (Löwenritter + Hafenmark: Regency Alliance). But as a solo win path, Regency Resolution may be nearly inaccessible without cooperation. The Military Consolidation alternate path (8 territories + military conditions) may be the de facto primary path for a solo Löwenritter player.
**Balance note:** This design is intentional — Löwenritter is a regency faction, not a conquest faction. Its legitimacy comes from restoration, not domination. But solo players choosing Löwenritter should be warned: the Regency Resolution path almost requires a co-victory declaration. If playing without a cooperative partner, Military Consolidation is the realistic win condition.
## Restoration Movement at 5 Players Only
**The restriction is sound.** Restoration with Military 0 in a 3-4 player game would be a pure spoiler. At 5 players, the faction adds Thread-narrative value without being unable to win (5 Presence markers requires more board space, which 5-player games provide through increased territorial contestation). **No change recommended.**
## Starting Stat Assessment (all factions)
**Church is point-rich.** 25 starting points vs Varfell's 18. This is offset by Church's structural constraints (no Thread, no Intel, Theocracy Counter advancement requiring constant management). The Varfell/Restoration point disadvantage is compensated by asymmetric mechanics (Patience Protocol, Presence/Weaving) that don't appear on the stat line.
**Recommendation:** No rebalancing needed. The asymmetry is intentional and mechanically compensated. Flag for first playtest: observe whether Church consistently outperforms in early seasons before Theocracy Counter management becomes taxing.
# PART NINE: HYBRID MODE INTERSECTION
> **Pool size note (PP-038):** "BG battle resolution uses an aggregated pool (sum of all engaged unit Martial values). TTRPG mass battle uses per-unit pools (Effective CP = min(CP, current Strength)) applied individually to each engagement. These systems are not statistically equivalent and will produce different expected outcomes for the same force. This is the intended distinction: BG mode is a strategic abstraction (one faction roll represents the whole force). TTRPG mode is a tactical simulation (each unit engages separately, each with its own roll and damage calculation). Neither system is 'more correct' — they model different scopes of play. When a Player Character faction leader arrives mid-battle and triggers the BG→TTRPG handoff, the outcome distribution will change. This is expected: PCs introduce tactical granularity that the board game abstraction cannot represent."
## Handoff Points Stress-Tested
- Cascade Personal-to-Board Effects table (B14): clear, well-defined. Each personal scene outcome maps to a single board consequence. No ambiguity.
- Fog of War stat display: the qualitative display states are clean and the boundary roll (d6, now noted as a d6 exception per PATCH P-20) is fast to execute.
- Zoom-In triggers: the list of 14 trigger conditions is comprehensive and covers all major board events that have personal-scale consequences.
- **Forgetting Check "Spirit proxy":** Already addressed in G-06/PATCH P-26. This is the most significant hybrid gap remaining.
- **Co-Movement Cards for personal Thread operations:** TTRPG operations that batch to Cascade (Thread consequences step) generate Co-Movement card draws in Cascade, not during the personal scene. The card effects (particularly Temporal effects — Non-Player Character relationship changes) must be retroactively applied to the scene that just finished, which can feel narratively discontinuous. Recommendation: Game Master draws the Co-Movement card for a batched personal Thread operation at the END of the personal scene in which it occurred, records its effects, then applies them at Cascade. The narrative flavoring is immediate; the mechanical application is deferred.
## Missed Coalition Opportunity Penalty (PP-404)
At Accounting, if **all** of the following conditions were met this season and the coalition was not triggered:
1. Both factions' relevant stat was observably above the coalition floor — i.e., both showed "Good" (not the ambiguous d6-boundary band) or higher at point of observation.
**Tracking:** A single binary "Missed Window" flag per coalition pair, set during Accounting, cleared next Accounting. No additional counter needed.
