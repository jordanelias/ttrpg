# Valoria BG Stress Test — Full Mode Stress
## Date: 2026-04-08 | Session: 2026-04-08_SONNET_BG_STRESS_1
## Modes: A (Single Mechanic Isolation) + D (Edge Case Discovery)
## Source files: valoria_bg_v05_simulation_and_patches.md (734L), params_board_game.md (1348L), victory_architecture_v1.md (393L), canon/02_canon_constraints.md (25L)
## Canonical source: designs/board_game/valoria_bg_v05_simulation_and_patches.md + references/params_board_game.md

---

## FETCH LOG
canonical_sources.yaml: ✓ fetched (156 lines)
designs/board_game/valoria_bg_v05_simulation_and_patches.md: ✓ fetched (734 lines)
references/params_board_game.md: ✓ fetched (1348 lines)
designs/board_game/victory_architecture_v1.md: ✓ fetched (393 lines)
canon/02_canon_constraints.md: ✓ fetched (25 lines)
canon/editorial_ledger.yaml: ✓ fetched (1832 lines)
canon/patch_register.yaml: ✓ fetched (4231 lines)

---

## P1 FINDINGS (breaks game)

### P1-01 — Overwhelming Threshold Self-Contradiction
**Setup:** Any faction makes a roll. Applying the degree table.
**Mechanism:** Three incompatible statements in params_board_game.md:
- Degree table (PP-249): Overwhelming = "net ≥ 2×Ob AND ≥ 3"
- PP-281/PP-299/PP-262: Overwhelming = "Ob+1 surplus, floor 2"
- PP-322 (ED-142 resolution): "net ≥ 2×Ob AND net ≥ 3 (PP-179 canonical + PP-232 floor). ED-031 superseded."

At Ob 2 pool 4: 2×Ob threshold requires net ≥ 4 (P ≈ 7%). Ob+1 threshold requires net ≥ 3 (P ≈ 27%). A 4× frequency difference means faction combat outcomes, seizure success rates, and victory pacing all depend on which rule applies.

**At Ob 1 pool 3:** 2×Ob = net ≥ 2 (P ≈ 40%); Ob+1 = net ≥ 2 (same). No difference at Ob 1. At Ob 3+, divergence is severe.

**Severity:** P1 — every non-trivial roll is affected.
**Frequency:** Every roll in every season.
**[PROVISIONAL: Using 2×Ob AND floor 3 per PP-322 (highest-numbered definitive patch + degree table). Marks every simulation result below as provisional until confirmed.]**

---

### P1-02 — TCV Table Uses Stale Territory Numbering in victory_architecture_v1.md
**Setup:** Calculate victory feasibility or track TCV.
**Mechanism:** victory_architecture_v1.md §1 uses PP-199 territory numbering (T12=Valorsplatz TCV 5, T5=Gransol TCV 4, T14=Himmelenger TCV 3, etc.). params_board_game.md uses geography_design.md canonical numbering (T1=Valorsplatz TCV 5, T8=Gransol TCV 4, T9=Himmelenger TCV 3). Both files are canonical per canonical_sources.yaml.

**Resulting starting TCV conflicts:**
| Faction | params (geography_design) | victory_arch (PP-199) |
|---------|--------------------------|----------------------|
| Crown | 12 | 10 |
| Hafenmark | 8 | 9 |
| Varfell | 6 | 6 |
| Church | 3 | 3 |

Crown 12 vs 10: 2-point gap. Hafenmark 8 vs 9: 1-point gap. Victory gap calculations (and therefore win probability estimates in §10) are wrong in victory_architecture_v1.md.

**[EDITORIAL: ED-327 — victory_architecture_v1.md §1 must be renumbered to geography_design.md canonical territory numbers. This is a pure renumbering pass (no design decision required — territory names are canonical). Self-resolving: assign PP-443 to execute the renumber.]**
**[PROVISIONAL PP-443 applied below in simulation: using params_board_game.md TCV table as canonical.]**

---

### P1-03 — Crown Primary Victory TCV Threshold Conflict
**Setup:** Crown approaches victory.
**Mechanism:** Two canonical documents give different thresholds:
- params_board_game.md §Victory summary: "Crown: TCV ≥ 18"
- victory_architecture_v1.md §3.1 (using old TCV): "TCV ≥ 16"

Using params TCV values: Crown starts at 12. Gap to 18 = 6 (same gap as victory_arch: starts at 10, needs 16, gap 6). With geography_design renumbering, victory_arch §3.1 target of 16 would map to approximately 18 in params numbering (Crown's extra 2 starting TCV from T6/T5 which appear under different T-numbers). **The gap is the same (6) but the absolute threshold differs.**

For compilation purposes: the absolute threshold matters (victory check at Accounting fires on the absolute number, not the gap). Conflict needs resolution.

**Severity:** P1 — Crown can declare victory 2 TCV points earlier or later depending on which doc is used.
**[PROVISIONAL: TCV ≥ 16 per victory_architecture_v1.md §3.1, which is the canonical victory conditions document. The params summary is a secondary reference. If renumbering (ED-327/PP-443) is applied to victory_arch, the new threshold may be recalculated. Flagged as provisional.]**

---

### P1-04 — Torben Loyalty Starting Value and Range Conflict
**Setup:** Any player consults Torben Loyalty.
**Mechanism:** Two contradictory definitions in params_board_game.md:
- Starting Values table: Torben Loyalty = **10**, range = 0–10
- Torben Loyalty Track section: "Range 0–7. Starts at **3**."

These cannot coexist. Starting at 10 with a 0–10 range means Torben is at maximum loyalty from game start — no AER trigger applies, no gaining events matter until he drops. Starting at 3 with 0–7 range means typical political management is required.

**Severity:** P1 — Crown/Löwenritter Deed 5 condition (Torben Loyalty ≥ 5 or ≥ 6 depending on version) has different difficulty entirely.
**[EDITORIAL: ED-329 — Which Torben starting value is canonical? 3 (0–7 range) is the version consistent with the Patience Protocol narrative and prior design sessions. 10 (0–10) appears to be from a revision that extended the range but may not have changed the starting value correctly. Request designer confirmation before PP-444.]**
**[PROVISIONAL: Starting value 3, range 0–7, per Torben Loyalty Track section which gives full mechanical detail. Starting Values table is likely a copy error from range extension.]**

---

### P1-05 — Church Territorial Seizure Ob Formula Conflict
**Setup:** TC = 75. Church attempts seizure of T2 Kronmark (Fort 1, CV 2, Crown-controlled, Crown Mandate 5 → Church Prominent if Church Mandate > 5 — only if Church Mandate exceeds 5, impossible given ceiling 7 and starting 5, only 2 gain possible).
**Mechanism:** Two incompatible Ob formulas:
- PP-189 Final Corrections: "Church Mandate vs Ob = Fort + 1" → T2: Ob = 1+1 = 2
- victory_arch §7 + params §TC 75 Seizure: "Ob = 2 + Fort Level + max(0, 3−CV)" → T2 (CV 2): Ob = 2+1+max(0,1) = 4

Ob 2 vs Ob 4 at Church pool 5 (Mandate 5):
- At Ob 2: P(Success) ≈ 69%
- At Ob 4: P(Success) ≈ 27%

The Ob 4 formula makes post-TC 75 seizure extremely difficult for low-CV territories. The Ob 2 formula makes it routine. These produce completely different post-TC-75 phases.

**Severity:** P1 — Church's entire endgame is premised on seizure success rate.
**[PROVISIONAL: Using "Ob = 2 + Fort Level + max(0, 3−CV)" per victory_arch §7 and the dedicated §TC 75 Seizure section in params (both agree). PP-189 "Fort+1" appears to be a fragment from an earlier draft, not a current formula.]**

---

## MODE A — SINGLE MECHANIC ISOLATION

### A-01: Dice System (d10, TN7)

**Input space:**
| Variable | Range | Typical | Edge |
|----------|-------|---------|------|
| Pool size | 1–7 | 4–5 | 0 (impossible), 7 (ceiling) |
| Ob | 1–7 | 2–3 | 1 (floor), 10 (exception) |

**Net success formula:** (count 7-9) + 2×(count 10s) − (count 1s). Can be negative (= Failure).
**Majority-1s override:** STRUCK in v05. All rolls use degree table only.

**Probability table (exact binomial, P(success per die) = 0.4, P(subtract) = 0.1):**

E(net per die) = 0.4×1 + 0.1×2 − 0.1×1 = 0.4+0.2−0.1 = 0.5. Wait — re-checking: 10 gives 2 successes, 7-9 give 1 success, 1 gives −1.
P(10) = 0.1, P(7-9) = 0.3, P(1) = 0.1.
E(net per die) = 0.1×2 + 0.3×1 + 0.1×(−1) = 0.2+0.3−0.1 = 0.4.

**Corrected probability table:**
| Pool | E(net) | P(≥1) | P(≥2) | P(≥3) | P(≥4) |
|------|--------|--------|--------|--------|--------|
| 2 | 0.80 | ~58% | ~22% | ~5% | ~1% |
| 3 | 1.20 | ~74% | ~40% | ~15% | ~4% |
| 4 | 1.60 | ~85% | ~56% | ~27% | ~9% |
| 5 | 2.00 | ~91% | ~69% | ~42% | ~19% |
| 6 | 2.40 | ~95% | ~80% | ~57% | ~31% |
| 7 | 2.80 | ~97% | ~88% | ~69% | ~44% |

*Note: BG doc §Probability Summary matches these figures (confirming formula). Simulator skill reference is consistent.*

**Degree outcomes (using PROVISIONAL 2×Ob AND floor 3):**

At Ob 2, pool 4 (most common BG roll — medium faction pool, standard action):
- Overwhelming (net ≥ 4 AND ≥ 3): P ≈ 9%
- Success (2 ≤ net < 4): P ≈ 47%
- Partial (net = 1): P ≈ 29%
- Failure (net ≤ 0): P ≈ 15%

At Ob 1, pool 4 (easy roll):
- Overwhelming (net ≥ 2 AND ≥ 3 → net ≥ 3): P ≈ 27%
- Success (net ≥ 1, < 3): P ≈ 58%
- Partial (impossible — Partial requires 0 < net < Ob = 1, so net must be in (0,1) — no integer exists. Partial never fires at Ob 1 — next step below Ob 1 is Failure.)

**Finding — Degenerate case at Ob 1:** No Partial result possible. Ob 1 produces Overwhelming, Success, or Failure only. This eliminates partial success tension from all Ob-1 rolls. Many rolls hit Ob 1 (Action Ob floored at 1, VTM Bootstrapping Ob 1, NPC Diplomacy vs Stability 1). Designers should be aware that Ob 1 is a binary swing mechanic, not a graded outcome.

**Finding — Small pool fragility:** Pool 2 (Restoration at Military 0 using Wealth÷2 for Forgetting Check, or low-stat factions) has P(Failure) = 42%. Near coin-flip. Restoration cannot reliably pass any check requiring pool 2 at Ob 2.

---

### A-02: TC Generation Formula

**Input space:**
| Source | Value | Conditions |
|--------|-------|------------|
| Institutional Momentum | +1 | Always |
| Conviction Yield | 0–3 | Only in non-Church-controlled territories where Church Prominent |
| Assert | +1 | On success (Influence 6, Ob 2 → P ≈ 80%) |
| Hafenmark Structural Suppression | −1 | While Baralta Mandate ≥ 4 (AND no Parliamentary Challenge played) |
| Parliamentary Challenge | Variable | Replaces structural (PP-431-COR) |
| AER ≥ 3 bypass | Negates structural | PP-203 |

**Key isolation finding — Conviction Yield dead zone:**
"Church Prominent = Church global Mandate > controlling faction's global Mandate."
If Church CONTROLS a territory, the controlling faction IS Church. Church Mandate 5 > Church Mandate 5 = False. Church gets zero Conviction Yield from any territory it controls.

As Church seizes territories (post-TC 75), all seized territories leave the Conviction Yield pool. Seizure reduces TC income.

**TC Income projection (Season 1–20, no opposition):**
- Seasons 1–14 (TC 28→75 target): Institutional Momentum +1, Assert P×1 ≈ 0.8, Conviction Yield (Crown/Hafenmark/Varfell territories where Church Prominent — only possible if rival Mandate < Church Mandate 5, i.e., rival Mandate ≤ 4, which is possible if they've been politically suppressed).
- Without suppressed rivals: +1.8/season.
- With suppressed rivals (1 territory at CV 5 where rival Mandate ≤ 4): +2.3/season.
- Seasons to TC 75: 47 ÷ 1.8 = 26 seasons uncontested.

**With Hafenmark structural suppression (−1/season):** Net +0.8/season → 47 ÷ 0.8 = 59 seasons. Game typically ends around season 20. Church primary victory via TC route is inaccessible with sustained Hafenmark suppression.

**With AER ≥ 3 bypass (Church plays Cardinal Temperance Focus Season 1 for free AER+1):**
- Season 1: AER 2 → 3. Hafenmark structural bypassed from Season 1.
- Net without suppression: +1.8/season. 47 ÷ 1.8 = 26 seasons. Still barely within 20-season game.
- AER+1 per season via Temperance Focus: AER 5 by Season 3 (IP held at 50, Vanguard neutralized).

**P2 finding — Cardinal Temperance Focus dominant opening:**
Church can achieve AER 3 in Season 1 with zero card cost, zero roll. This neutralizes Hafenmark structural suppression. No faction has a counter to Cardinal Focus Phase 1 declarations. If intended, should be explicitly noted in the Church faction guide as a primary opening strategy.

---

### A-03: Hafenmark Parliamentary Challenge vs Structural Suppression

**PP-431-COR:** Challenge replaces structural suppression for any season it is played.

**Expected TC change per season (Mandate 4, no PI ≥ 5):**

*Without Challenge (structural fires):* TC −1 guaranteed.

*With Challenge (pool 4, Ob 2):*
- P(Overwhelming, net ≥ 4): ≈ 9% → TC −2, Church must Uphold/Appease
- P(Success, net 2–3): ≈ 47% → TC −1
- P(Partial, net 1): ≈ 29% → Stability −1, TC −0 (structural also gone)
- P(Failure, net ≤ 0): ≈ 15% → Stability −1, Church Mandate +1, TC −0

E(TC) from Challenge: 0.09×(−2) + 0.47×(−1) + 0.29×0 + 0.15×0 = −0.18 − 0.47 = −0.65

**Comparison:**
| Option | E(TC Δ) | Risk |
|--------|---------|------|
| Structural (no Challenge) | −1.0 | None |
| Challenge | −0.65 | 44% Stability −1, 15% Church Mandate +1 |

Challenge is strictly worse on expected TC suppression AND carries Stability risk. The only advantage is the Church Uphold/Appease trigger on Overwhelming, which is valuable for its secondary political effects.

**Finding (P2):** Hafenmark players will rationally never play Parliamentary Challenge for TC suppression. Challenge's value is entirely in the Uphold/Appease trigger on Overwhelming (9% chance), which is an expensive Senator slot usage for a <10% proc. The mechanic creates the illusion of agency while the optimal play is to never use it. Recommend reviewing whether Challenge should NOT replace structural, or whether Challenge should provide additional value on Success/Overwhelming to compensate.

---

### A-04: Community Weaving Ob Formula

**Conflict:** Two formulas in canonical docs.
- BG design doc (v05): "Ob 2, −1 Ob per Presence marker in territory" (floor 1)
- params_board_game.md action table: "Ob = (100−RS)÷20 round up, min 1; −1 per Presence marker"

**Comparison at key RS values (0 markers):**
| RS | v05 formula | params formula | Delta |
|----|-------------|----------------|-------|
| 72 (start) | Ob 2 | (28÷20)=1.4→2 | Same |
| 60 | Ob 2 | (40÷20)=2 | Same |
| 50 | Ob 2 | (50÷20)=2.5→3 | +1 Ob |
| 40 | Ob 2 | (60÷20)=3 | +1 Ob |
| 20 | Ob 2 | (80÷20)=4 | +2 Ob |

**The formulas diverge at RS ≤ 59.** As Rendering Stability degrades, Restoration's core action becomes harder precisely when Thread operations are more urgent. This is thematically coherent BUT is a new design element not reflected in the BG design doc. If intentional, the dynamic Ob formula should replace the static Ob 2 in v05.

**With 2 markers at RS 40:** params gives Ob 3 − 2 = 1; v05 gives Ob 2 − 2 = 0 → floor 1. Same result.
**With 1 marker at RS 40:** params gives 3 − 1 = 2; v05 gives 2 − 1 = 1. One Ob difference.

**[EDITORIAL: ED-330 — Which Community Weaving Ob formula is canonical? The dynamic RS-linked formula creates a meaningful tension (Restoration gets harder as world degrades, making them more urgent). If intended, v05 must be patched to match params. If not intended, params action table must revert to "Ob 2 −1 per marker."]**
**[PROVISIONAL: Using params action table formula as it is the more recently edited source and produces better design coherence.]**

---

## MODE D — EDGE CASE DISCOVERY (EXHAUSTIVE)

### Boundary: Track Threshold Behaviors

**D-01 — Ob 1 no Partial (documented above in A-01)**
Severity: P3 — known design feature, not a bug. Should be noted on faction reference cards.

**D-02 — TC 75 freeze interaction with fractional TC values**
PP-441-COR: TC fractional values accumulate. Counter-Narrative generates TC −0.5 on Overwhelming. 
Edge: TC at 74.5. Church plays Assert: Success = TC +1 → 75.5. TC ≥ 75 triggers freeze.
Does TC freeze at 75 or at the ceiling of the roll that crossed it?
**Ruling needed:** TC freezes at 75. Any TC ≥ 75 at Accounting step 4 = freeze. Fractional tracking must include 0.5 intervals. The freeze check is "floor(TC) ≥ 75" — but if TC is 74.5 at Accounting end, is the threshold crossed? If ceiling (75.5 rounds to 76 > 75), yes; if floor (74), no.
**[PROVISIONAL: TC freeze triggers when accumulated TC (including fractions) equals or exceeds 75.0 at Accounting step 4 clock advance. Partial and fractions below 75.0 do not trigger.]**
Severity: P2 — potential premature/delayed TC freeze at 0.5-point increments.

**D-03 — Total TCV sum is 29, not 30**
Summing from params TCV table: T1(5)+T2(1)+T3(2)+T4(1)+T5(1)+T6(1)+T7(1)+T8(4)+T9(3)+T10(2)+T11(1)+T12(3)+T13(1)+T14(2)+T15(0)+T17(1) = 29. Params states "Total TCV = 30."
**Total Domination requires TCV ≥ 28.** If total is 29, TCV ≥ 28 leaves 1 TCV uncaptured (any single TCV-1 territory). If total were 30, TCV ≥ 28 leaves 2. The 1-point discrepancy changes whether Total Domination allows one uncaptured TCV-1 territory or none.
Severity: P2 — Total Domination achievability slightly affected.
**[PATCH PP-444 needed: Recount TCV, correct stated total. Provisional total: 29.]**

---

### Cascade: Chain Reactions

**D-04 — Cardinal Temperance Focus → AER 5 in 3 seasons (dominant strategy)**
Documented in A-02. No counter available. Church neutralizes Altonian threat and Hafenmark suppression without card play by Season 3.
Severity: P2 — removes shared threat pressure if Church player always picks Temperance Focus early.

**D-05 — Reformed Settlement → AER −2 → Vanguard threshold drop**
If Hafenmark reaches RDT 2 (Reformed Settlement formal) while Church resists: TC +3, RDT +1. Church resists via Accommodate response: AER suspended 1 season (Accommodate) or AER unchanged (Resist). But per the BG doc Cascade Test 2: Reformed Settlement + Church Resist = TC +3, RDT +1, Hafenmark Standing +1, Deed Token.
The BG doc §Cascade Test 2 says Church Resist triggers AER −2. Params §ED-085 resolution (PP-298) does not mention AER change: "1. Resist: Mandate −1; TC gain continues; Hafenmark gains Deed. 2. Accommodate: TC gain suspended 1 season; PI +1. 3. Ignore: TC gain halved 1 season; no other effect."

**Conflict: BG doc says Reformed Settlement + Church Resist = AER −2. Params PP-298 says Resist = Mandate −1 with no AER change.**
Severity: P1 — AER −2 from Reformed Settlement could immediately drop Vanguard threshold, triggering an invasion chain.
**[PROVISIONAL: Using params PP-298 (no AER change from Reformed Settlement). AER is not affected by Reformed Settlement. The BG doc's Cascade Test 2 may have used a superseded version of the mechanic.]**

**D-06 — Seizure cascade post-TC 75: Accounting queue depth**
TC 75 seizure: Church attempts one seizure per season. Overwhelming seizure: CV +1 in territory (consequence, not capped). Success seizure: territory control changes. Each control change may trigger:
- Institutional Mandate Uphold/Appease from defending faction (if Mandate ≥ 4)
- PI −1 (Church territorial seizure per Accounting step 4b)
- Faction Stability check if ≥ 2 attribute losses (Accounting step 2)
- If faction Stability drops to 0: Faction Collapse (I-04/PATCH P-15)
All of these queue to Accounting, not Phase 4 (Cascade Depth Cap applies).
**Maximum immediate effects:** 3 (CV +1, territory control change, Uphold/Appease trigger). ✓ Cap satisfied.
**Accounting depth:** Seizure success → PI −1 → Hafenmark Parliamentary Manoeuvre may fire → PI recovery → TC step 5 → Hafenmark structural suppression (if no Challenge played) → This is already in the Accounting sequence. No chain overflow.
Severity: P3 — cascade is manageable.

---

### Deadlock: No Valid Actions

**D-07 — Faction at Military 0 with Muster as only unplayed card**
PP-039: "At Military 0, Muster actions produce no units and may not be taken. A Muster action at Military 0 is invalid and does not count as the faction's action for that season."
Restoration has Military 0 permanently. If Restoration's hand includes a Legionary card: "Muster action invalid." Legionary Inward = Muster (which is invalid). Is Legionary Outward (March) also invalid at Military 0? March requires a unit to move — if Restoration has no units, March cannot execute. Restoration cannot play Legionary at all.
**Ruling needed:** Restoration's Legionary card should be replaced with another card type in the starting hand. Alternatively, Legionary for Restoration should allow alternative use (organising civil patrols, etc.).
Starting hand: params shows Restoration has no Legionary card in hand (1× Pontifex, 2× Praetor, 1× Senator, 1× Tribune, 1× Recess). ✓ No conflict. Restoration never draws Legionary from the standard hand.
Severity: P3 — no actual deadlock risk for Restoration. If Restoration somehow acquires a Legionary card via Senate Market, the Military 0 restriction still applies. Note: Restoration should not be able to purchase Legionary cards from Senate Market. This is not explicitly stated.
**[PATCH PP-445: Add "Restoration may not purchase Legionary cards from Senate Market." to Restoration faction restrictions.]**

**D-08 — Ministry Collapse + Crown Emergency Powers concurrent**
If Ministry Mandate = 0 (collapsed) AND Crown is in Emergency Powers:
- Crown Policy unavailable (Ministry Mandate 0)
- Crown Emergency Powers already active
- Crown cannot issue Policy, Crown cannot end Emergency Powers via Mandate-based action (Ministry's block prevents Policy, not Emergency Powers revocation)
Is there a path out? Crown must raise Ministry Mandate. Ministry re-establishes at Mandate 1 via Hafenmark or Crown Govern in T13 (Ob 2). But Crown is in Emergency Powers = Stability crisis = Mandate may be degraded. 
**Potential deadlock:** Crown Emergency Powers + Ministry Collapse → Crown cannot issue Policy → Crown cannot maintain Mandate actions → potential spiral.
Not an absolute deadlock (Crown can still play Legionary, Consul, Senator actions). But Crown's unique power suite is entirely disabled.
Severity: P2 — severe political paralysis, not game-breaking but worth noting as a valid "losing state."

---

### Crunch Cascade: Calculation Overhead

**D-09 — Accounting steps per Season at game peak (Season 15)**
Steps 1-13 + 4b (Church Prominence) + optional Year-End (if Season 16 = Winter):
1. Pending attribute changes
2. Stability checks (need: count attribute losses ≥ 2 per faction = up to 6 pool rolls)
3. Cooldown Track (4 slots per faction = up to 24 slot updates)
4. Clock advances: RS drift, TC formula (5 sub-steps), IP, PI
4b. Church Prominence update (check all 15 territories)
5. Church Attention Pool resolve (1–5 threshold responses)
6. Thread Debt (count tokens, age > 1 season = RS −1/token)
7. Clear Thread Resonance markers
8. Threshold events (check all clocks, draw Event Cards)
8b. Milestone Bonus check
9. Warden Emergence check
9b. Vaynard-Edeyja same-season rule
10. Warden Cooperation check
10b. Torben/Elske Loyalty events
11. [Dissolved]
12. Victory condition check (all factions, all co-victory pairs, shared loss)
13. Season marker advance (+Year-End if applicable)

**At peak complexity (Season 15, all factions active, Church at TC 75+, IP at 65, WC active, Ministry operational):**
Accounting takes approximately 25–35 discrete checks/rolls. Year-End adds 10 more.
This matches the BG doc's own assessment: "Phase 5 is the most procedurally heavy part of the game." The doc recommends collapsing steps 8/8b/9/9b/10/10b into a single "Events and Emergence" step. This is the correct mitigation.
**[PATCH PP-446: Formally merge Accounting steps 8/8b/9/9b/10/10b into Step 8 "Events and Emergence" with a physical checklist card. Renumber steps 11→8, 12→9, 13→10, 14→11.]**
Severity: P2 — pacing risk, not mechanical failure. Fixable with reference cards.

---

### Ambiguity: Undefined Resolution Priority

**D-10 — Conviction Yield from Church-controlled territories = 0**
Church Prominence = Church Mandate > controlling faction's Mandate. In Church-controlled territories, controlling faction = Church. Church Mandate > Church Mandate = False. Church gets no Conviction Yield from its own territories.
**Implication for TC pacing:** Church's primary TC source (Conviction Yield) only fires in territories controlled by factions with Mandate below Church's. Church must either suppress rival Mandates or rely on Assert + Institutional Momentum alone.
**Implication for seizure strategy:** Seizing territories removes them from Conviction Yield eligibility. Church's TC income may DROP post-seizure if those territories were generating Conviction Yield under rival control.
Severity: P2 — structural constraint on Church TC income, not explicitly documented. Should appear in Church faction guide.
**[PATCH PP-447: Add explicit note to Church TC generation table: "Conviction Yield only applies to non-Church-controlled territories where Church is Prominent. Church-controlled territories contribute zero to Conviction Yield."]**

**D-11 — Parliamentary Challenge + AER ≥ 3 interaction undefined**
PP-203: "AER ≥ 3 bypasses Hafenmark structural suppression."
PP-431-COR: "Challenge replaces structural for any season it is played."
If AER = 3 AND Hafenmark plays Challenge:
- Does AER ≥ 3 still bypass the (already-replaced) structural suppression?
- Does Challenge still fire on top of AER bypass?
The question is: if structural suppression is already negated by AER ≥ 3, does playing Challenge produce TC-suppression effects from the roll, or does "Challenge replaces structural" still mean the roll fires but against an already-negated baseline?
**Ruling needed:** If AER ≥ 3 removes structural suppression, Challenge still fires (it's a card play, not a structural effect). Challenge produces TC change per the degree table independently. AER ≥ 3 and Challenge are not mutually exclusive.
**[PATCH PP-448: Clarify: "AER ≥ 3 bypasses Hafenmark Structural Suppression (the passive Mandate ≥ 4 −1/season). Parliamentary Challenge is a card action and fires independently of AER. If AER ≥ 3, structural does not fire in any season, including seasons when Challenge is played (since structural is already negated, Challenge's replacement clause has no practical effect — Challenge still fires and produces its degree-table result)."]**
Severity: P2 — ambiguity in Hafenmark's TC suppression toolkit.

**D-12 — Diplomatic Token removal on "military conflict with Hafenmark"**
"Diplomatic Token: Removed on military conflict with Hafenmark OR target faction elimination."
At TC 75+, Church seizures are Military actions (Legionary implicit). If Church holds a Diplomatic Token from Hafenmark AND Church seizes a Hafenmark territory: does token remove?
Seizure = Church military action targeting Hafenmark territory = "military conflict with Hafenmark" = Token removed.
Result: Hafenmark loses the Diplomatic Token precisely when they most need Parliamentary Session support (to manage TC crisis). This is probably intended design tension but should be confirmed.
Severity: P3 — notable interaction, design-consistent.

---

### Optimal Play: Dominant Strategies

**D-13 — Church Cardinal Temperance Focus AER ramp (documented in A-02, D-04)**
Dominant opening. Reaches AER 5 by Season 3 with zero card cost.
Severity: P2.

**D-14 — Crown Royal Guard cancels exactly one Intel per season**
"Royal Guard: Once per season, cancel one successful Intel action targeting Crown. No card cost."
At full Varfell Patience Protocol VTM 5: Varfell can attempt multiple Tribune actions per season? No — Varfell has 2× Tribune in starting hand, but normally plays one per Phase 4. At 4 PC: "Spy action in any territory regardless of adjacency" — this is from the Patience Protocol spend, not a separate Phase 4 action.
Actually the Patience Protocol PC spends are listed as Phase 4 or Phase 1 actions depending on type. 4 PC = Spy anywhere. This is a unique action replacing a Tribune play.
Royal Guard cancels "one successful Intel action targeting Crown." It cancels the first one. Varfell can play a Tribune Inward (Investigate Crown) and use 4 PC Spy in the same season — Royal Guard cancels one, the other lands.
**Dominant counter: Varfell always plays one sacrificial Tribune targeting Crown to burn Royal Guard before playing the 4 PC Spy for intelligence.** This costs Varfell one Patience Counter per season (the 4 PC Spy requires PC) to neutralize Royal Guard. Net cost: Varfell sacrifices one Tribune play result (intentionally fails or accepts its outcome) to unlock the more important Spy.
Severity: P2 — solvable with clever sequencing, but creates a known "Royal Guard burn" pattern that experienced Varfell players will always execute.

**D-15 — Total Domination: Submission mechanic creates permanent board state**
Submitted faction: "stats halved rounded down, no independent actions." If the submitting faction's Mandate drops to 0 (halved), they would trigger Faction Collapse (I-04). Faction Collapse at Mandate 0: "Mandate drops to 0 immediately... All OTHER attributes freeze at pre-collapse values."
But Submission already halved all stats including Mandate. If Mandate halved = 1 (from starting 2), no collapse. If Mandate halved = 0 (from starting 1): Collapse fires simultaneously with Submission.
**Gap: Submission + Mandate 0 interaction undefined.**
**[PATCH PP-449: "If a Submitting faction's halved Mandate = 0: the faction does not enter Faction Collapse. Submission supersedes Collapse. The faction remains as a vassal with Mandate 0, all other stats halved. Mandate 0 effects (Crown Policy unavailable, Ministry effects) still apply to that faction."]**
Severity: P2 — edge case in Total Domination endgame.

---

### Degenerate: Mechanics That Become Meaningless

**D-16 — Restoration Community Weaving at 2+ Presence markers (as documented in BG doc)**
At 2 markers, RS 72: Ob 2 − 2 = Ob 0 → floor 1. P(Success, pool 4) ≈ 85%. Restoration's core Thread action is near-reliable once they have 2 Presence markers. The challenge IS building and maintaining Presence, not the roll. This is documented in BG doc G-08 — confirmed as intentional design. No patch needed.
Severity: P3 — noted, intentional.

**D-17 — VTM Bootstrapping at Ob 1 (confirmed by BG doc G-07, PATCH P-27)**
Pool 4 at Ob 1: P(≥1 net) ≈ 85%. If Varfell fails (15%), they cannot retry — must use standard VTM methods (Tribune in Thread-active territory, requires prior VTM 0→1 somehow). This means failing Bootstrapping permanently locks Varfell out of their fastest VTM development path. 15% failure rate on a once-per-campaign roll is significant.
**Clarification: Is Bootstrapping a once-per-campaign action or once-per-game?** BG doc says "If not converted within 2 seasons, the token is lost" and "Failure: Bootstrapping fails. No retry this campaign." This implies once-per-campaign arc, not once-per-game (if the game runs multiple campaign arcs). If it's truly once-per-game, the 15% failure rate is severe for Varfell's Path A/B/C viability.
Severity: P2 — noted; acceptable design tension per BG doc's own analysis.

---

### Incoherence: Logically Impossible Results

**D-18 — Faction Collapse (Mandate 0) while in Reformed Settlement negotiations**
If Church is negotiating a Reformed Settlement response (Accommodate: Church Mandate −1) AND Church Mandate = 1 → Mandate drops to 0 → Faction Collapse fires.
But Faction Collapse = "Mandate drops to 0 immediately... other attributes freeze." Does Collapse suspend Church's Reform Settlement response? The Church player has already declared Accommodate. Accommodate fires before Collapse is assessed (it's a Phase 4 action; Collapse from attribute change queues to Accounting Step 2 per Cascade Depth Cap).
**Ruling: Accommodate fires (Mandate −1 declared in Phase 4); Collapse is assessed at Accounting Step 2. Church may Collapse after Accommodate takes effect. This produces: Reformed Settlement succeeds → Church Mandate 0 → Church Collapse next Accounting. Dramatic and coherent.**
Severity: P3 — rare but well-defined via existing cascade rules.

---

## MODE A CONTINUED — Victory Condition Feasibility

### A-05: Win Probability Assessment (using params TCV, PROVISIONAL PP-443 numbering)

**Starting TCV (canonical per params geography_design numbering):**
Crown 12 | Hafenmark 8 | Varfell 6 | Church 3

**Note: victory_architecture_v1.md §10 uses old TCV starting values (Crown 10, Hafenmark 9). These estimates are stale. Corrected below:**

| Faction | Path | Start TCV | Target TCV | Gap | Key Rate | Est. Seasons |
|---------|------|-----------|------------|-----|----------|-------------|
| Crown | Peninsula Sovereignty | 12 | 16 (PROV) | 4 | Military expansion 0.5 TCV/season | 8–12 seasons |
| Crown | Dominion | 12 | 22 | 10 | All rivals eliminated | 18–24 seasons |
| Church | Orthodoxy | 3 | 10 | 7 | TC 75 first (26 seasons uncontested), then seizure | 28+ seasons (unreachable solo) |
| Hafenmark | Parliamentary | 8 | 12 | 4 | Military 3 handicap; PI ≥ 5 | 10–14 seasons |
| Hafenmark | Dynastic | 8 | 12 + T1 | 4 + T1 | Requires Crown Mandate ≤ 1 | 14–18 seasons |
| Varfell A | Intel Hegemony | 6 | 10 | 4 | VTM 3 (S7–9) + reveals | 12–14 seasons |
| Varfell B | Southernmost | 6 | 8 | 2 | WR ≥ 2 requires 2+ successful Expeditions | 12–16 seasons |
| Varfell C | Thread Supremacy | 6 | 10 | 4 | VTM 5 (~S14+) | 14–18 seasons |
| Löwenritter | Regency | post-coup | 10 | variable | TC < 50 hard constraint | 8–12 post-coup |
| RM | Cultural Revolution | 0 | 5 terr. CV≤1 | — | Requires global Rendering Stability management | 14–20 seasons |

**P1 finding (balance) — Church primary victory unreachable:**
Church Holy State is unreachable in a standard 16-season campaign without all of: (a) no Hafenmark suppression, (b) multiple high-CV territories in rival hands, (c) sustained Assert success. Even then, reaching TC 75 takes ~26 seasons. Church needs the Altonian Theocracy alternate path or Partition co-victory with Hafenmark for a realistic win.
**This matches BG doc Part Eight analysis.** No new finding, but confirmed quantitatively.

**P2 finding — Crown TCV ≥ 4 gap is achievable extremely early:**
Crown starts at TCV 12. If target is 16 (PROVISIONAL), Crown needs TCV +4. Crown already controls T14 Ehrenfeld (TCV 2). Taking T9 Himmelenger (Church capital, TCV 3) = TCV 17 from just 2 territories. But Church capital has Fort 2 + Church Military 4 = defender pool 6, Crown attacker pool 4+2D (Offensive) = 6D vs Ob 2 (Church Defend). P(Crown wins battle by Ob margin) ≈ complex — see battle resolution.

**Simpler path:** T8 Gransol (Hafenmark capital, TCV 4). Crown taking Hafenmark's capital would meet TCV ≥ 16 with TCV 12+4 = 16. Requires Crown Military vs Hafenmark Military 3 + Fort 1. Crown Military 4, Offensive +2D = 6D. Hafenmark 3D + 1 fort = 4D. E(Crown net) = 6×0.4 = 2.4; E(Hafenmark net) = 4×0.4 = 1.6. Crown wins by 0.8 expected margin. Crown victory probability via T8 seizure is feasible as early as Season 2 if Crown opens militarily.

**Balance concern:** Crown can potentially meet primary TCV threshold in Season 2–3 via single military conquest of T8 or T9. The political suppression conditions (all factions Mandate ≤ 2) are the real gate, not TCV. This is likely intended but should be confirmed.

---

## EDITORIAL ITEMS FLAGGED THIS SESSION

| ED | Description | Status | Blocks |
|----|-------------|--------|--------|
| ED-327 | victory_architecture_v1.md TCV table requires renumbering to geography_design.md canonical T-numbers. Pure renumbering, no design decision. | [PROVISIONAL: PP-443 renumber scheduled] | BG compilation |
| ED-328 | Church Cardinal Focus Temperance → AER +1 free per season: does AER ≥ 3 bypass Hafenmark structural suppression from Season 1 without any card or roll cost? Is this intended? | flagged | Church balance |
| ED-329 | Torben Loyalty starting value: 3 (0–7 range per Torben Track section) vs 10 (0–10 per Starting Values table). Which is canonical? | flagged | Löwenritter/Crown win tracking |
| ED-330 | Community Weaving Ob formula: static "Ob 2 −1/marker" (v05) vs dynamic "(100−RS)÷20 −1/marker" (params). Which is canonical? | flagged | Restoration balance |

---

## PROVISIONAL DECISIONS (self-resolved per session instructions)

| ID | Decision | Rationale |
|----|----------|-----------|
| P1-01 prov | Overwhelming = 2×Ob AND floor 3 | PP-322 is highest patch number; matches degree table |
| P1-03 prov | Crown TCV target = 16 | victory_arch §3.1 is canonical victory conditions doc |
| P1-04 prov | Torben starting 3, range 0–7 | Torben Track section has full mechanical context |
| P1-05 prov | Seizure Ob = 2 + Fort + max(0, 3−CV) | Both victory_arch §7 and params §TC 75 agree; PP-189 fragment is vestigial |
| D-05 prov | Reformed Settlement does NOT change AER | PP-298 (params) is more recent than BG doc cascade test |
| D-10 prov | TC freeze at TC ≥ 75.0 (including fractions) at Accounting step 4 | Threshold check is ≥ 75.0 at moment of advance |
| D-11 prov | AER ≥ 3 and Parliamentary Challenge are independent | PP-448 clarification |
| D-15 prov | Submission supersedes Collapse if halved Mandate = 0 | PP-449 |

---

## PATCHES GENERATED THIS SIMULATION

| PP | Scope | Change |
|----|-------|--------|
| PP-443 | TCV | Schedule renumbering of victory_architecture_v1.md §1 TCV table to geography_design.md canonical T-numbers. [PROVISIONAL: execute next session with full renumber pass] |
| PP-444 | TCV | Correct stated Total TCV from 30 to 29 in params_board_game.md |
| PP-445 | Restoration | Restoration may not purchase Legionary cards from Senate Market |
| PP-446 | Accounting | Merge Accounting steps 8/8b/9/9b/10/10b into Step 8 "Events and Emergence" |
| PP-447 | Church TC | Add explicit note: Conviction Yield = 0 in Church-controlled territories |
| PP-448 | Hafenmark | Clarify AER ≥ 3 and Parliamentary Challenge are independent effects |
| PP-449 | Victory | Submission + Mandate 0: Submission supersedes Collapse |

---

## COVERAGE MATRIX UPDATE

| Mechanic | Mode A | Mode D | Status | Issues |
|----------|--------|--------|--------|--------|
| Dice system (d10) | ✓ | ✓ | Complete | Ob 1 no-Partial (P3, intentional) |
| Degree table | ✓ | ✓ | Issues found | P1-01 Overwhelming contradiction |
| TC generation | ✓ | ✓ | Issues found | P2 AER dominance, Conviction Yield dead zone |
| Parliamentary Challenge | ✓ | ✓ | Issues found | P2 Challenge worse than structural |
| Community Weaving | ✓ | ✗ | Issues found | P2 Ob formula conflict |
| Victory conditions — Crown | ✓ | ✗ | Issues found | P1-03 TCV threshold conflict |
| Victory conditions — Church | ✓ | ✗ | Issues found | Balance P2 unreachable primary |
| Victory conditions — Hafenmark | ✓ | ✗ | Complete | Feasible 10–14 seasons |
| Victory conditions — Varfell | ✓ | ✗ | Issues found | P2 Path B summary stale |
| Victory conditions — Total Domination | ✓ | ✓ | Issues found | P2 TCV total wrong, Submission+Collapse |
| TCV table | ✓ | — | Issues found | P1-02 numbering conflict |
| Torben Loyalty | ✓ | — | Issues found | P1-04 start/range conflict |
| Church Seizure Ob | ✓ | — | Issues found | P1-05 formula conflict |
| Cardinal Focus (Temperance) | ✓ | ✓ | Issues found | P2 dominant opening |
| Accounting procedure | — | ✓ | Issues found | P2 crunch, recommend merge |
| Battle resolution | — | ✗ | Not started | SIM-DEBT |
| Thread operations (full) | — | ✗ | Not started | SIM-DEBT |
| Faction Unique Actions (all) | — | ✗ | Not started | SIM-DEBT |
| Co-victory pairings | — | ✗ | Not started | SIM-DEBT |

---

## SIM-DEBT REGISTER (remaining simulation work)

| ID | Mechanic | Priority |
|----|----------|----------|
| SIM-DEBT-BG-01 | Full faction-AI battle resolution simulation (multi-faction, multi-season) | P1 |
| SIM-DEBT-BG-02 | Thread operation full sequence with Co-Movement deck distribution analysis | P2 |
| SIM-DEBT-BG-03 | Co-victory pairings reachability analysis (6 pairings) | P2 |
| SIM-DEBT-BG-04 | Faction Unique Actions balance across all 6 factions | P2 |
| SIM-DEBT-BG-05 | Ministry NPC AI interaction with Crown Policy + PI degradation | P2 |
| SIM-DEBT-BG-06 | RS decay rate simulation across 20-season campaign | P2 |

