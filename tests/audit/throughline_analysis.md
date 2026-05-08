# VALORIA — Cross-Batch Throughline Analysis
## Top-Down Audit: Robustness · Elegance · Smoothness
**Date:** 2026-04-17  
**Token:** dd9c7a6d24d3752e  
**Scope:** Batches 1–8 (ST-01 through ST-60), arc expansion v1, all design decisions this session  
**Method:** Synthesis across all simulation findings. Self-audit of simulation methodology included (§4).

---

## Preamble: What These Terms Mean Here

**Robust** — the system allows strategic thinking, meaningful customisation, player impact, and emergent narrative. A robust system responds to what players do and does not reduce to a single optimal path.

**Elegant** — the system is logically simple, internally consistent, and allows players to intuit complex outcomes from simple inputs. Elegance fails when a system requires exceptions to its own rules, or when its observable outputs surprise even its designers.

**Smooth** — the system integrates cleanly with adjacent systems. Transitions produce no friction. Calculations are consistent. Sequencing is unambiguous. The system does not stall at boundaries.

---

## §1 ROBUSTNESS

### §1.1 What Is Working

**Victory race convergence is correctly calibrated (ST-21).**  
Multiple factions reach their win conditions within 1–2 seasons of each other in standard play. Crown vs Varfell at Season 20 was separated by one OW Tribune Spy success. The conditions are neither trivially easy (single-faction dominance) nor unreachably hard (drag to Rupture). The game produces genuine endgame tension with several viable winners visible simultaneously. *Verdict: design intent achieved.*

**The CI/RS pyrrhic collision is the game's structural spine — and it works.**  
Batches 2, 5, 7, 8 all converge on this: Church advancing CI (getting stronger politically) while RS declines (the world gets weaker) produces the game's central irony at mechanical rather than narrative level. A Church that wins at CI 65+ has purchased its victory with the world's health. This is not a coincidence — it is the designed cost, and the simulation confirms it registers correctly. At CI 65, IP is elevated, RS is in Fragile or worse, and the Accord ≥ 3 condition (ED-590) now forces Church to also govern well, not just seize. *Verdict: structural spine confirmed working.*

**The Obligation system punches above its weight class.**  
Across batches 5 and 8, Obligations handle: NPC behavioral constraints, diplomatic commitments, cross-system arc conditioners, and consequence cascades from social contest outcomes — all through one mechanic. The 3-Obligation cascade in ST-28 produced 7 correctly targeted consequences with no conflicts. Obligations are doing more systemic work than any other single mechanic in the game. *Verdict: robust beyond its surface specification.*

**Investment competition for Torben's Conviction produces a correctly competitive early game.**  
The first-mover advantage (reaching Disposition ≥ +2 before Season 8) is real, measurable, and rewards attentive play. Each Conviction produces distinct Crown Priority Tree behavior (7 variants, ST-58). The faction that wins Torben literally rewrites what the largest faction does for the rest of the campaign — this is the correct level of consequence for 6–8 seasons of relationship investment. *Verdict: robust by design.*

**The Calamity reversal mechanic (4 practitioners, TS 50+) is a correctly gated late-game achievement.**  
The gate is inaccessible until Season 33+ even with optimal play (ST-37). It requires: sustained Thread practice across the full campaign, Edeyja's 2-season instruction, and a fourth TS 50+ practitioner that doesn't exist yet at Season 28. The goal is visible from mid-campaign; its achievement requires the whole campaign. *Verdict: correctly long-horizon.*

**Co-victory hold phases are robust to single-season spoiling (ST-26).**  
Once both conditions are at threshold and the 2-Accounting hold begins, no available single-season action disrupts it. This is intentional — cooperative paths should be durable once established. The spoiler window is meaningful in the earlier building phase, not the terminal hold. *Verdict: robust to disruption by design.*

**Elske as a strategic meta-game (ST-52).**  
The reveal that pre-coup diplomatic investment (Season 3–7) produces a Season 17 Regency is a genuinely robust insight: the optimal LR strategy operates under the cover of legitimate service, preparing a diplomatic resolution while publicly performing institutional loyalty. This subversive quality — the coup that was never needed — is correct for Ehrenwall's character and produces surprising strategic depth for a faction that appears to be purely military. *Verdict: elegant robustness emergent from NPC design.*

**Niflhel as an intelligence market (ST-51).**  
The Asset placement system creates a faction-agnostic service layer: any faction pays Wealth for Verified intelligence. This correctly models how covert organisations achieve political relevance without territory — they hold information, not land. The behavioral nudge (once/arc: Priority Tree override) is the correct power level for an occasional intervention rather than sustained control. *Verdict: robust strategic layer correctly specified.*

---

### §1.2 What Is Failing or Underperforming

**IP advancement rate was wrong for 8 batches.**  
The original rate (+2/battle-season, +1/season CI≥60) produces IP ~47 at Season 30 in a moderate campaign. The Altonian threat never fires in standard play. This is a robustness failure: a shared loss condition that never manifests is not a pressure, it is decoration. The revised rate (+3/battle-season, +2/season CI≥60) validated in ST-42 produces a Season 25 threshold crossing in moderate warfare — genuinely existential. **This finding is significant enough to flag as a design-level error in the original specification, not a simulation gap.**

**No Parliamentary mechanic blocks Church Tribunal filing (ED-631).**  
The Excommunication is effectively automatic once filed at CI 70+ (Track starts at 7 — near-decided before Exchange 1). The correct counter is preventing the filing, not defending at Tribunal. But there is no mechanic to prevent filing. The proposed Parliamentary Stay (CI < 55 only) addresses this, but creates a dependency: protect the Stay window by keeping CI below 55. This is the correct design — the window closes as Church grows — but the mechanic needs to exist to enable that strategy. **Gap in robustness: a major threat (Excommunication) has no viable counter once it becomes likely.**

**Guilds solo victory was missing (ED-612, resolved).**  
A faction with no solo victory condition is not a faction — it is a spoiler. The Merchant Hegemony design (ST-31) produces a viable ~Season 15 victory but one that was entirely absent from the game. **This is a robustness failure in the faction design, not the mechanical execution.**

---

## §2 ELEGANCE

### §2.1 What Is Working

**The CI reform (Assert→Pontifex, conditional passive) is an elegance success.**  
One change fixed three problems simultaneously: CI acceleration (no more 2-Senator Assert spam), Church's mid-game dominance (no more 4-season CI 40 arrival), and the dual Domain Expertise model (Pontifex/Senator each have distinct strategic profiles). The ripple confirmed correct in ST-05, and the CI 40 timeline now lands at Season 12 instead of Season 4 — exactly the spacing a mid-game political faction should occupy. *Verdict: elegant fix.*

**The Accord ≥ 3 governance condition on Church victory is elegant.**  
TCV 8 was achievable with 3 territories. The Accord condition silently requires 4 territories (3 non-capitals at Accord 3). The distinction between "having territories" and "governing them well" is exactly the right design pressure for a theocratic faction. Church must use Consul cards (Govern) rather than only Senator cards (Seize), creating a genuine action economy trade-off. The condition is elegant because it produces the right strategic pressure without being a separate victory track — it is an additional constraint on an existing track. *Verdict: elegant expansion of existing mechanic.*

**Feigned Retreat's dual utility is elegant.**  
The card has two completely different values depending on opponent Command: deception (vs low Command — ~60% chance the opponent follows the "retreat") vs strategic tax (vs high Command — the Overextended effect after a loss). A single card text produces two meaningfully different strategic situations. This is canonical elegance in game design: simple rule, contextually varying outcome. *Verdict: well-designed.*

**The Excommunication being an institutional fait accompli is elegant.**  
Track starting at 7 (near-decisive before Exchange 1) is not a balance problem — it is a statement about what the Inquisition is. The Catholic Church did not lose Inquisition trials through clever oratory. The correct counter (prevent filing) places the strategic challenge at the right moment: before Season 55 CI rather than during the Tribunal. The Tribunal is the consequence of failing politically; the Tribunal itself should not be contestable with sufficient rhetoric. *Verdict: historically accurate elegance.*

**Shield Wall perfectly countering Wedge at equal pools is elegant.**  
+2D Def exactly offsets +2D Off, producing a tie. No formation is universally dominant. Counter-formation awareness is a skill that materially changes expected outcomes without requiring extra mechanical complexity — the same pool, the same dice, a different outcome from the prior choice of formation card. *Verdict: elegant formation system.*

**Depth 5 (Unintelligible) is elegant.**  
It is non-investigative, provides TS +1 advancement, and gives experiential rather than informational content. The epistemic barrier is constitutive, not skill-based — even Edeyja (TS 75–80) cannot access it. This is the correct implementation of P-08: the limit is structural, not an obstacle to overcome with sufficient investment. *Verdict: philosophically consistent elegance.*

**The Obligation system's consequence distribution across time is elegant.**  
Obligations produced in Grand Contests persist for 4 seasons. Their violation cascades across NPCs and arc conditioners, but the cascade distributes across multiple Accountings rather than piling into one. The system is elegant because it produces sustained narrative consequence from a single decisive scene, rather than a one-time stat change. *Verdict: elegant durability.*

---

### §2.2 What Is Failing

**Grand Contest Recall is the single largest elegance failure across all 8 batches.**  
The Recall bonus (+2D per exchange per cited source) produces 1-exchange decisive wins in almost all pool-asymmetric matchups. In ST-22, Baralta at 20D vs Player at 15D collapses the Grand Contest in Exchange 1. The fundamental problem: at Ob 2 with large pools, expected net successes are ~8–12. The standard Piety Track (0–10, victory at ≥7 or ≤3) cannot absorb margins of this size across even 2 exchanges. The proposed fix (Recall once per cited source per contest, not per exchange) is correct and sufficient — it reduces the Baralta pool from a constant 20D to 18D (after first Recall), then 16D (second citation exhausted), producing typical margins of 1–3 and requiring 3–4 exchanges for decisive resolution. **This is the highest-priority unfixed elegance problem in the social contest system.**

**The two-scale territory system (Province Accord, Settlement Order) is elegant in design but invisible in play.**  
These are the right two scales. Province Accord governs TCV, sovereignty, and political legitimacy. Settlement Order governs local stability, garrison requirements, and civil unrest. They are independent, they can co-fire, and their interaction is consistent with historical governance models. But they are specified across 4 different documents and never clearly distinguished in a single canonical place. The simulation discovered the distinction itself rather than finding it in the rules. **An elegant mechanic that requires detective work to understand is not fully elegant.**

**The IP advancement formula was published in 4 documents at the wrong rate.**  
+2/battle-season is not wrong on its face, but it produces a threat that never materialises. A shared loss condition that players never encounter does not constrain their decisions. The revised rate needed to be the published rate. **An inelegant diagnostic: the simulation had to discover that the threat pressure was miscalibrated, which means 8 batches were run against a world where Altonian invasion wasn't a real constraint.**

**BG Parliamentary Vote lobby pre-determination (ED-621).**  
The lobby offset (±2) applied to a Piety Track with decisive win at 7 means a +2 lobby push starts the vote at 7 — decisive before a single die is rolled. This violates the mechanic's own logic: lobbying provides advantage, not predetermined outcome. **An elegant mechanic undermined by its interaction with the track's victory threshold.**

---

## §3 SMOOTHNESS

### §3.1 What Is Working

**Zoom In/Out: consistently clean across all 8 batches.**  
Every simulation involving a Zoom In transition (§9.4–§9.6 of board_game) produced clean results. Domain Echo batching to Cascade, PC Embedding stacking with Personal Phase actions, mandatory Zoom In triggers all fire at the correct phase. No friction at the transition point in any of 60 simulations. *Verdict: the transition architecture is the game's smoothest design achievement.*

**The 5-step Cascade sequence handles complexity without grinding (ST-28).**  
3 simultaneous Obligations producing 7 consequences in one Accounting resolved correctly. The sequence (Domain Echo → Thread clock changes → threshold events → board consequences → Accounting) provides a deterministic ordering that prevents conflicts. The Cascade is the game's load-bearing structure for complexity, and it holds. *Verdict: robust sequential resolution.*

**Co-movement fires once per collective operation (not per participant), producing clean RS accounting.**  
This was not formally specified before the simulation. It is the correct behavior — a collective operation is one Thread intervention, not N individual interventions. If it fired per participant, large collectives would draw multiple co-movement cards and produce compounding random effects that swamp the intentional result. *Verdict: correct and smooth.*

**Three-faction simultaneous territory contest as sequential bilaterals in Stability order (ST-56).**  
The resolution is completely deterministic: higher Stability acts first, the territory can only change hands once per resolution step. No ambiguity about simultaneous combat between three parties. The strategic implication ("Stabilise to act first") is a genuine, clean insight that emerges from the ordering rule. *Verdict: smooth but needs explicit documentation — this resolution behavior is not stated anywhere.*

**Mass battle tactic card interactions are universally smooth (ST-30).**  
All 6 shared tactic cards tested, all 3 counter-formation interactions confirmed. No edge cases or contradictions. The card-play timing (Phase 1 declaration, Phase 4 resolution) is consistent with BG resolution sequencing. *Verdict: smooth throughout.*

**Hybrid Coherence declaration (Cascade Phase 1 leadership declaration) is smooth.**  
The PP-198 resolution of "who pays Coherence for a Strategic Phase Thread order" (whoever declares leadership at Cascade Phase 1) is unambiguous, mechanical, and requires no GM judgment. *Verdict: clean specification.*

**Threadcut being perception is TS-gated and smooth.**  
Non-practitioners literally cannot engage physically (TS 0–9 = not perceivable). TS 30–49 = Ob +2 on combat targeting. TS 50+ = full combat. The perception table (§6.2) provides a smooth, graduated experience of encountering a threadcut being — the same being produces 6 different encounters depending on who is looking. *Verdict: ontologically consistent, mechanically smooth.*

**The RM Presence marker system integrates smoothly with Phase 1/Phase 2 distinction.**  
Presence markers are the T9 holding mechanic (post-Uprising). PT values are the Phase 1 mechanic. These operate in parallel without interfering. The OW Uprising auto-places +2 markers, creating holding infrastructure within the Uprising's resolution. Clean chain: Uprising OW → T9 PT −2 + 2 markers auto → 1 Weaving at Ob 1 → 3 markers → holding condition met in 1 season. *Verdict: smooth pipeline.*

---

### §3.2 What Is Creating Friction

**Province Accord 0 and Settlement Order 0 can co-fire simultaneously without specified resolution sequence (ED-632).**  
When both trigger in the same territory at the same Accounting, the existing rules don't specify which fires first. In ST-55, this was resolved by proposing Order 0 Uprising fires first (garrison fights), then Accord 0 consequence applies. But this sequencing is not in any document. Two independent mechanics can create a deadlock if their resolution order is ambiguous. *Friction point: needs a resolution sequencing rule.*

**Partition fires silently at Accounting, without a Phase 1 declaration requirement (ED-629, now resolved).**  
Before the fix, Church+Hafenmark could win the game with no visible warning to other players until Accounting confirmed the win. This violated the game's fundamental principle that victories should be legible. The Phase 1 declaration mechanic (now specified) creates the correct warning window. *Was friction; now resolved.*

**Siege mechanic is absent from the playable faction toolkit (ED-633).**  
Fort 3 is effectively impregnable against Military 4 through standard Battle (Fort gives +3D to defending pool). A playable faction that cannot reduce fort levels before assault has no answer to an entrenched opponent. The Siege action (designed in batch 7 and batch 8) needs to exist in military_layer_v30 as a formal mechanic. Without it, military strategy has a dead end that forces non-combat solutions even when the narrative calls for a siege. *Friction: missing mechanic creating a strategic wall.*

**The Parliamentary Vote lobby cap (ED-621) creates a pre-resolution friction point.**  
Starting at Track 7 with maximum lobbying means the vote is decided before dice are rolled, which creates player friction ("why are we rolling?"). The cap at 6 (compromise zone max) resolves this by ensuring that voting remains meaningful regardless of lobbying investment. *Was friction; now resolved.*

**No Parliamentary mechanic interrupts Church Tribunal filing (ED-631).**  
Once Church files an Excommunication, nothing in the existing Parliamentary toolkit can stop it. The Parliamentary Stay (now proposed) addresses this — but only while CI < 55. After CI 55, the Stay is effectively unpassable (Church's CI bonus makes blocking too expensive). This creates a timing dependency: protect the Stay window before CI 55 by keeping CI suppressed. This is the correct design, but the mechanic must exist to enable the strategy. *Friction: strategic option is implied but not actionable.*

---

## §4 SELF-AUDIT: SIMULATION METHODOLOGY ERRORS

The following errors were made during simulation work and should be noted before these findings are treated as canonical.

**§4.1 IP Rate Discrepancy**  
Batches 1–4 simulated IP advancement at the existing rate (+2/battle, +1/season CI≥60). Batch 5 only flagged this as a calibration problem. Batches 1–4 conclusions about Altonian threat timing are therefore wrong in absolute terms (the threat was modeled too mildly). The relative findings (coalition rebuff mechanics, AER firewall, Elske track) remain valid — the timing error doesn't invalidate the response mechanics.

**§4.2 Grand Contest CLASH Direction**  
In ST-22, the simulation initially concluded that Grand Contests should use CLASH always (simultaneous rolls, higher net wins). This is correct per the social contest rules (CLASH = same genre, opponent orientation). However, the batch 5 analysis did not check whether Baralta's contest orientation in that scenario was genuinely CLASH-eligible. The finding (Recall once-per-source) is correct independently of the CLASH question, but the intermediate analysis conflated the CLASH issue with the Recall issue.

**§4.3 Varfell Path C TCV Count**  
In ST-47, the TCV calculation for Varfell Path C included territories gained by Cultural Reformation (T6, T3) without checking whether those Reformations had actually succeeded in the simulation context. The conclusion (Path C achievable Season 14–15) is correct given the stated assumptions, but the calculation depended on ~27% probability events that were assumed to have succeeded. The conclusion should read "achievable with optimal Reformation success (~27% probability of the required 4 successes from 8 attempts)."

**§4.4 Collective Operation RS Accounting**  
In ST-57, the Community Weaving collective operation produced RS +2 from OW at Relational scale. The simulation did not check whether the seasonal cap (±10 net RS change per season) would interact with other RS sources in the same Accounting. This is unlikely to matter in practice (±10 is a large cap), but the RS accounting should be verified in the full campaign context, not just isolated operations.

**§4.5 Scale Transition Timing**  
Several simulations (ST-24, ST-28) tested arc conditioner effects at "Accounting" without specifying which Accounting step they fire in the 5-step Cascade sequence. Per board_game §9.8, arc conditioners that modify faction stats should fire at Step 5 (Accounting), not Step 3 (threshold events) or Step 4 (NPC board consequences). This distinction matters when a conditioner modifies a stat that feeds into another conditioner in the same Accounting. No conflicts were identified, but the sequencing within Accounting was not explicitly verified.

---

## §5 CONSOLIDATED THROUGHLINE TABLE

| Throughline | Category | Verdict | Action |
|-------------|----------|---------|--------|
| Victory race convergence (ST-21) | Robustness | ✓ Working | None |
| CI/RS pyrrhic collision | Robustness | ✓ Structural spine confirmed | None |
| Obligation cross-system cascade | Robustness | ✓ Over-performing, clean | None |
| Torben Conviction investment race | Robustness | ✓ Correct early-game competition | Propagate §1.8 Torben window |
| Calamity reversal gate (4 practitioners) | Robustness | ✓ Correctly late-game | None |
| Co-victory hold robustness | Robustness | ✓ Correct spoiler resistance | None |
| Elske pre-coup subversive strategy | Robustness | ✓ Emergent from NPC design | Propagate Elske track to victory_v30 |
| Niflhel intelligence market | Robustness | ✓ Correct faction-agnostic layer | Propagate asset mechanics |
| IP advancement rate | Robustness | ✗ Threat too mild — was miscalibrated | Propagate revised rate |
| No Parliamentary block on Excommunication | Robustness | ✗ Gap — counter unavailable | Propagate Parliamentary Stay |
| Missing Guilds solo victory | Robustness | ✗ Fixed (ED-612) | Confirmed resolved |
| CI Reform (Assert→Pontifex) | Elegance | ✓ Three-problem fix | Confirmed resolved |
| Church Accord ≥ 3 governance condition | Elegance | ✓ Elegant governance pressure | Confirmed resolved |
| Feigned Retreat dual utility | Elegance | ✓ Single card, contextual value | None |
| Excommunication fait accompli | Elegance | ✓ Historically correct | Propagate procedure |
| Shield Wall / Wedge counter | Elegance | ✓ No dominant formation | None |
| Depth 5 non-investigative | Elegance | ✓ Correct P-08 implementation | None |
| Grand Contest Recall (once-per-source) | Elegance | ✗ 1-exchange blowouts — critical fix | Propagate to social_contest §4 |
| Accord/Order invisibility | Elegance | ✗ Elegant mechanic, undocumented | Propagate clarification |
| IP published at wrong rate in 4 docs | Elegance | ✗ Miscalibration error | Propagate revised rate to all 4 |
| BG Parliament lobby pre-determination | Elegance | ✗ Fixed (ED-621) | Propagate cap to social_contest §10 |
| Zoom In/Out transitions | Smoothness | ✓ Best-designed system in the game | None |
| 5-step Cascade sequence | Smoothness | ✓ Load-bearing, holds under complexity | None |
| Collective co-movement (fires once) | Smoothness | ✓ Correct but undocumented | Propagate to threadwork |
| Three-faction sequential bilateral | Smoothness | ✓ Smooth but undocumented | Propagate sequencing rule |
| Mass battle tactic cards | Smoothness | ✓ Universal smooth | None |
| Accord 0 / Order 0 co-fire sequence | Smoothness | ✗ Resolution order missing | Propagate to peninsular_strain §2 |
| Partition silent Accounting win | Smoothness | ✗ Fixed (ED-629) | Propagate Phase 1 declaration |
| Missing Siege mechanic | Smoothness | ✗ Dead end in military strategy | Propagate §1.9 to military_layer |
| Parliament Vote lobby cap | Smoothness | ✗ Fixed (ED-621) | Propagate cap rule |
| No Parliamentary Stay for Tribunals | Smoothness | ✗ Strategic option unavailable | Propagate Parliamentary Stay |

---

## §6 PRIORITY PROPAGATION LIST

Ranked by impact (design-critical first, cleanup second):

### P0 — Propagate Immediately (correctness depends on it)

1. **Grand Contest Recall fix** → `social_contest_v30.md §4 Step 3` (ED-617)
2. **IP advancement revised rate** → `board_game_v30.md G-11/P-28`, `peninsular_strain_v1.md §4.2`, `victory_v30.md §5.3`, `npc_behavior_v30.md §7.8` (ED-623)
3. **BG Parliamentary Vote lobby cap** → `social_contest_v30.md §10` (ED-621)

### P1 — Propagate This Session (gap-filling)

4. **Battle consequences §E** → `mass_battle_v30.md` (ED-542)
5. **Siege mechanic §1.9** → `military_layer_v30.md` (ED-633)
6. **Partition Phase 1 declaration** → `victory_v30.md §3.2` (ED-629)
7. **RS Rupture Last Declaration scene** → `victory_v30.md §5` (ED-630)
8. **Parliamentary Stay** → `social_contest_v30.md` + `board_game_v30.md` (ED-631)
9. **Accord/Order distinction + co-fire sequence** → `peninsular_strain_v1.md §2` (ED-626 + ED-632)
10. **RM Presence marker mechanics + Phase 1 clarification** → `victory_v30.md §3.5` (ED-589)

### P2 — Propagate (documentation cleanup)

11. **Torben Conviction window S1–8** → `npc_behavior_v30.md §2.8` (ED-618)
12. **Constrained sub-arc state** → `npc_behavior_v30.md §5.1` (ED-586)
13. **Stability Crisis Zoom In** → `scale_transitions_v30.md §4.3.2` (ED-587)
14. **Three-faction sequential bilateral rule** → `board_game_v30.md I-07 / P-18` or `mass_battle_v30.md`
15. **Collective co-movement fires once** → `threadwork_v30.md §2.5` or `§4`
16. **Obligation 3-cap advisory** → `social_contest_v30.md §6.1` (ED-619)
17. **Varfell no-Senator note** → `tc_political_redesign_v30.md §5.1` (ED-622)
18. **Elske Loyalty track** → `victory_v30.md §3.6` or `npc_behavior_v30.md` (ED-624)
19. **Schoenland Treaty terms** → `victory_v30.md §3.1` or new §3.7 (ED-615)
20. **Excommunication procedure** → `social_contest_v30.md §7.x` (ED-625)

---

*End of throughline analysis. §6 propagation list drives all commit work below.*
