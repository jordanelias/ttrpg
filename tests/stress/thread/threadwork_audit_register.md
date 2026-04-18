# VALORIA THREADWORK STRESS TEST — COMPREHENSIVE AUDIT
## Session: d8b924fb834a398c | Date: 2026-04-16
## Covers: Batches 1–7. Source docs: threadwork_v30.md, params_threadwork.md, settlement_layer_v30.md,
##   companion_specification_v30.md, mass_battle_v30.md, social_contest_v30.md, scale_transitions_v30.md,
##   npc_behavior_v30.md, faction_layer_v30.md, peninsular_strain_v1.md, fieldwork_v30.md,
##   params_core.md, params_combat.md, victory_v30.md, clock_registry_v30.md

---

## SEVERITY TIERS

- **P0 — BLOCKER**: Blocks system integration; ruling required before any work in adjacent area proceeds.
- **P1 — CRITICAL**: Significant design flaw, exploit, or contradiction. Must be resolved before final document.
- **P2 — IMPORTANT**: Gap or design concern. Should be resolved; won't block immediate work.
- **P3 — SURFACE**: Emergent finding, design note, or validation. Document for completeness.

---

# SECTION A — P0 BLOCKERS (28 items)
*These block integration, simulation, or finalization of dependent systems.*

| ID | Batch | Item | Blocking |
|----|-------|------|----------|
| P0-01 | B1 | **Settlement Order as Thread configuration undefined** — No ruling on whether governance stats (Order, Prosperity) are Thread-targetable. Required before: siege duration calibration, governance stat simulation, Thread-settlement interface | ED-SETT-01, ED-SETT-02, ED-SETT-04 |
| P0-02 | B1 | **RO (Dissolution/Lock) as Companion Conviction trigger missing** — No rule defines witnessing Restricted Operations on living beings as a Conviction-violation strike | ED-COMP-02, companion spec finalization |
| P0-03 | B2 | **POP during Memory-genre contest — no ruling** — Successful POP retroactively makes the practitioner's contest argument physically true; no counter-mechanic defined | Chain contest convergence simulation, social contest system |
| P0-04 | B2 | **Per-province vs per-settlement siege RS drain** — If per-settlement, Ehrenfeld (3 settlements) generates 3× the RS drain per siege season; all RS budget calculations depend on this ruling | IP recalibration, 30-year RS budget |
| P0-05 | B3 | **History Resonance risk die scope** — "Risk die shows 1: −1 Coherence" — does this mean one designated die per op (10%) or every History die showing 1 (27%+)? 3× difference in Coherence depletion rate | All Coherence depletion calculations |
| P0-06 | B3 | **Dissolution Residue Potency per-use cap** — Potency 5 + Structural + mass battle ×3 = RS −15 at 52% success; 3 uses ≈ Rupture from RS 60 | All Residue mechanics, mass battle Thread design |
| P0-07 | B3 | **WC state as variable in all RS budget calculations** — WC 2 halves Gap/Lock RS drain; all RS budgets across B1–B5 implicitly assume WC 0 | All RS calculations, IP recalibration, 30-year game |
| P0-08 | B4 | **R-63 fast-change Lock domain rates undefined** — Only slow-change Lock RS drift (−1/season) defined; fast/standard/inert rates absent; every Lock RS calculation contains hidden undefined variable | All Lock chronic drift calculations |
| P0-09 | B4 | **Battle RS drain missing from all budgets** — RS −1 per battle on Valorian soil (−2 Campaign/War scale) from victory_v30 §0.4 not included in any RS budget; peak drain revised upward ~40% | All RS calculations, endgame modeling |
| P0-10 | B4 | **Lattice fracture threshold mathematically inert** — "Below half Anchor's solo pool" is impossible via helper dropout; mechanic does not function as written | Collective Thread operation design |
| P0-11 | B4 | **Thread-Read evidence admissibility before TS 0 adjudicators** — Three possible rulings, each with different contest system implications; cannot finalize contest design without this | Social contest system, Thread-Read fieldwork |
| P0-12 | B4 | **Conviction Scar + Thread operation mapping absent** — Thread ops are the most morally extreme actions in the game; Conviction Scar system has zero Thread interaction defined | Companion arc design, NPC behavior |
| P0-13 | B5 | **PP-603 RS cap language still present in skeleton** — Cap was struck canonically (PP-603); three skeleton locations still reference ±10 cap; GMs will apply a non-existent cap | All GM-facing RS tracking, endgame |
| P0-14 | B5 | **Ceiral Ritual Failure = RS +8 — intent unverifiable** — Cannot be used in any RS calculation until designer confirms whether this is intentional (substrate reasserts on failure) or a typo (Overwhelming/Failure swap) | All Southernmost RS modeling |
| P0-15 | B5 | **Altonian Thread practitioner status** — RS budget for 30-year games assumes Valorian practitioner activity only; if Altonians have practitioners, all RS budgets are underestimated | 30-year RS calibration, IP recalibration |
| P0-16 | B5 | **Niflhel Harvest mechanics undefined** — BG Harvest order listed but undefined; Co-Movement card implies Niflhel collects Dissolution Residue; Niflhel's strategic interest may be controlled RS destabilization | Niflhel faction design, BG Thread orders |
| P0-17 | B5 | **POP minimum Thread Sensitivity scaling** — TS 30 practitioners can POP 2-season-old obligations at 75% success rate; no TS gate on POP by temporal depth | All POP design, obligation mechanics |
| P0-18 | B6 | **Lock after practitioner death** — Whether Lock dissolves (RS restoration), crystallizes Permanent, or degrades slowly determines whether assassination of locking practitioner is ever strategically correct | Political strategy, assassination design |
| P0-19 | B6 | **Knot with threadcut being** — "Any character" Knots = threadcut beings eligible; metaphysical consequences (remote Thread access, superior Anchoring) are profound and unruled | Threadcut being design, Knot mechanics |
| P0-20 | B6 | **Domain Echo for Thread operations has no mapping** — Thread → faction consequence requires GM improvisation every time; no Domain Action equivalents defined | Scale transitions, zoom-out coherence |
| P0-21 | B6 | **Recall-based rolls at Fragmented — is Thread included?** — Whether Fragmented −1D applies to Thread pools determines practitioner viability in Fragmented band | All Fragmented-band practitioner calculations |
| P0-22 | B6 | **NPC practitioner Thread AI undefined** — Autonomous NPC Thread use is entirely GM improvisation; no Coherence decision threshold, no scale priority, no recovery rule | Robust emergent play requirement |
| P0-23 | B7 | **Pool floor conflict: 1D (params_core) vs 5D (R-57 Pull)** — Two canonical documents specify different minimum pool sizes; scope of 5D floor must be explicitly stated | All degraded-practitioner calculations |
| P0-24 | B7 | **Isolation as prerequisite for Foundational Mending** — PP-609 requires isolation of Foundational gaps before Mending holds; isolation never defined as a Thread operation type | Endgame recovery path, Einhir framework |
| P0-25 | B7 | **Foundational OA consequence undefined** — OA table ends at Structural; Foundational Weaving OA consequence absent | Endgame Foundational Thread operations |
| P0-26 | B6 | **Warden Harvest BG order undefined** — PP-630 references ED-NEW Harvest; undefined; may resolve Sigurdshalm chokepoint as alternate Einhir Text source | Endgame Einhir access, WC system |
| P0-27 | B6 | **Companion Conviction post-Forgetting** — Companion Conviction without emotional core after Forgetting failure; departure tracking mechanism undefined | Southernmost companion design |
| P0-28 | B7 | **Isolation for Foundational Mending: Thread op or Einhir-framework exclusive?** — Definition of isolation determines whether endgame recovery is accessible to standard practitioners or Einhir-gated only | Endgame practitioner capability |

---

# SECTION B — P1 CRITICAL (Exploits, Major Gaps, Conflicts)

| ID | Batch | Item | Type | Ruling/Fix |
|----|-------|------|------|------------|
| P1-01 | B1 | Province Accord real-time vs Accounting derivation | EXPLOIT | Accord from Order computed at Accounting only; mid-season Weavings don't immediately change Accord |
| P1-02 | B1 | Relational Lock prevents siege Order decay indefinitely | EXPLOIT | Lock on loyalty blocks Order decay; attacker's counter is RS chronic drift exhaustion |
| P1-03 | B1 | Relational Pull on settlement Order collapses siege timeline | EXPLOIT | 3+ surplus successes Pull = seasonal siege pressure equivalent in one contact window; rule: settlement Order is Thread-eligible but Pull duration for governance configs uses truncated table |
| P1-04 | B2 | Field-scale Dissolution of fortification bypasses siege | EXPLOIT | Ruling: fortification physical structure is Relational-scale (function in military network), not Field-scale; Dissolution attempts reclassified |
| P1-05 | B2 | Mass battle ×3 + Dissolution Failure at RS < 48 = Rupture | EXPLOIT | PP-204 extended to settlement-layer fortress assaults; mandatory GM disclosure at RS < 48 before any Dissolution declaration |
| P1-06 | B2 | Permanent Lock (4+ seasons) makes province ungovernable for TCV | EXPLOIT | Lock-and-cede named as strategic option; TCV blocked at Accord < 2 while Permanent Lock holds |
| P1-07 | B3 | Strategic Phase Dissolution: RS −1 vs Personal Phase RS −15 | EXPLOIT | Ruling: Strategic Phase Dissolution/Lock use TTRPG RS tables without ×3 multiplier |
| P1-08 | B3 | Potency 5 Residue + Structural + mass battle ×3 = near-Rupture | EXPLOIT | Cap single-use Residue at Potency 3; Potency 4–5 requires two contact windows |
| P1-09 | B3 | N-way opposing ops in Parliament → automatic Relational Gap | EXPLOIT | Design note required; practitioners must Diagnose for active contact before Thread-intervening in political settings |
| P1-10 | B4 | Forgetting companion-carrying: 4 companions → Rendering Crisis in Round 2 | EXPLOIT | Design note: carrying 2+ companions at Focus 5 produces Rendering Crisis risk within crossing window; intentional sacrificial mechanic |
| P1-11 | B5 | TS 90+ Coherence 0: −1 RS per scene of existence | EXPLOIT | Design note: Resonant practitioner Rendering Crisis = campaign-level RS emergency; −30 RS/year fastest single-source drain |
| P1-12 | B7 | Dissolution of Thread contact window | EXPLOIT | Rule: contact window is not Thread-targetable; first-person mode of being cannot be accessed third-person |
| P1-13 | B4 | PP-261: TS 70 companion should not declare Binding Ops in mass battle | GAP | Add PP-261 as hard constraint in companion AI spec (ED-COMP-02) |
| P1-14 | B5 | Torben Loyalty manipulable via Personal-scale Weave/Pull (Ob 2) | EXPLOIT | Detection risk (Church AP, Inquisitor) is the primary constraint; note as lowest-Ob highest-consequence Thread operation |
| P1-15 | B4 | Hybrid RS starting value undefined | GAP | Ruling: Hybrid inherits from transitioning mode; pure Hybrid start = 66 (midpoint) |
| P1-16 | B6 | Thread-Read 2–3× more efficient at Evidence generation than mundane fieldwork | SMOOTH | Gate Thread-Read Evidence advances to Depth ≥ 4 questions only |
| P1-17 | B7 | Thread-Read Evidence Track contradiction during mass battle | CONFLICT | Evidence banked during mass battle suspension; applied at Accounting |
| P1-18 | B7 | Hybrid zoom-in Thread ops: ×3 for battlefield-scale targets, standard for personal | GAP | Rule: scale of operation target determines multiplier, not physical position of practitioner |
| P1-19 | B5 | POP first-mover paradox window immunity (1d3 scenes) | EMERGENT | Counter-POP blocked during paradox window; state explicitly as tactical first-mover advantage |
| P1-20 | B6 | Lattice fracture threshold rewrite needed | FIX | Threshold: below half of INTENDED combined pool (not Anchor's solo pool) |
| P1-21 | B7 | Focus 3 dead zone after halving = same as Focus 2 | ELEGANT | Fix: ceiling rounding for operation conversion after halving eliminates dead zone |
| P1-22 | B5 | Victory via Thread aggression advances Peninsular Strain > 6, blocking universal victory | EMERGENT | Design note: Thread-aggressive conquest is self-defeating for universal victory condition |
| P1-23 | B5 | Free agent practitioners carry Residue, Lock knowledge, Coherence state post-faction-elimination | EMERGENT | Design note: converting practitioners > killing them; TS 90+ free agent at Coherence 0 = immediate RS emergency |
| P1-24 | B7 | Isolation prerequisite for Foundational Mending: undefined action type | GAP (see P0-24) | |
| P1-25 | B7 | Foundational OA: −2 RS/season + global Ob +1 + crystallizes Permanent Lock after 3 seasons | GAP | Proposed consequence in Batch 7 text |

---

# SECTION C — P2 IMPORTANT (Gaps, Design Concerns, Unmodeled Interactions)

| ID | Batch | Item | Fix/Ruling |
|----|-------|------|------------|
| P2-01 | B1 | Single-settlement provinces have 1:1 Thread→Accord leverage | Design note: structural vulnerability asymmetry |
| P2-02 | B1 | S-011 Stillhelm Watch Order 2 likely miscalibrated (Calamity-adjacent, Warden active ops) | Recommend Order 1 |
| P2-03 | B1 | RM Thread ops at S-029 Grauwald Lodge detectable by Church agents with TS 30+ | NPC TS tracking for Church agents in T4 |
| P2-04 | B1 | Practitioner governor Coherence degradation → governance capability declining | Design note: surface as intended practitioner arc |
| P2-05 | B2 | RS Fractured → NPC inconsistent memory → social contest Recall check Ob 1 in Fractured territories | Add Accounting event: NPCs in Fractured RS make Certainty check Ob 1 |
| P2-06 | B2 | Certainty Track acceleration under Fractured RS from rendering failures | Add systematic Certainty decline at Accounting for Fractured RS territories |
| P2-07 | B2 | Higher-TS companion as Anchor contradicts "player tactical lead" | Rule: player declares op; companion has Conviction veto; veto = no collective op |
| P2-08 | B2 | Helper withdrawal mid-Leap undefined | Rule: commitment locked at Leap success; voluntary withdrawal = lattice fracture |
| P2-09 | B2 | Companion First Leap mid-travel fires as mandatory scene wherever they are | Add to companion spec: Approach Training check before First Leap; player can prep companion |
| P2-10 | B2 | OA 3+ practitioners stacking — PP-209 only specifies two | Rule: cap OA stacking at +2 regardless of practitioner count |
| P2-11 | B2 | Scale hierarchy rule not cross-referenced in settlement spec | Add: "Mending at scale X cannot hold while disruption at X+1+ persists — cross-reference to threadwork §params" |
| P2-12 | B2 | RS Critical + Fragmented Coherence = compound Ob +2 on all Thread ops | Add to RS Critical design note: endgame requires reserved fresh practitioners |
| P2-13 | B3 | Document RS Resonance (PP-258): Private Collection Einhir documents uncounted | Inventory Private Collection; quantify RS restoration capacity |
| P2-14 | B3 | Sigurdshalm Defense 2 = softest Thread-strategic asset on map | State Thread-strategic value explicitly |
| P2-15 | B3 | Military action at T15 collapses WC → Einhir framework inaccessible by force | Design note: Einhir knowledge cannot be conquered |
| P2-16 | B3 | WC 3 + Edeyja Mending (+2 RS/season) = intended endgame RS solution | Add WC to RS Critical design note as "narrow difficult path" |
| P2-17 | B3 | Audience resistance floor = 0 at Stability 1; Grand Contests resolve in 1–2 exchanges | Rule: minimum audience resistance = 1 regardless of faction Stability |
| P2-18 | B3 | Flashback Anchoring fire frequency undefined | Cap: maximum 1 Flashback Anchoring per session |
| P2-19 | B4 | Knot-mediated Thread-Read strain threshold undefined | Define: accumulated strain threshold for rupture from Thread-Read use |
| P2-20 | B4 | General Duel + Thread contact are mutually exclusive in Phase 5 | Rule: practitioner in Thread contact cannot initiate General Duel same Phase 5 |
| P2-21 | B4 | PP-233 companion Mender in mass battle = highest RS restoration value | Surface in ED-COMP-03 ruling |
| P2-22 | B4 | Companion Coherence depletion across battles → late-campaign degradation arc | Design note: late-campaign practitioner companions in Fragmented or worse |
| P2-23 | B4 | Opposing ops Shifting Object → PP-303 Coherence drain persists until Mended | Winner Mends to stop drain; loser suffers continued attrition |
| P2-24 | B4 | Church Cathedral management = Thread-operational foothold in every province | Rule: Thread ops in settlement governed by settlement manager, not Provincial Authority |
| P2-25 | B5 | Player's own Beliefs opposing their Leap: pre-Leap Belief check undefined | Rule: solo pre-Leap Belief check on directly opposing Beliefs |
| P2-26 | B5 | Faction Stability triggers don't include Structural Thread Dissolution | Add: Structural+ Dissolution of faction core config = Stability −2 |
| P2-27 | B5 | Church Inquisitor at S-003 detects Almud's First Leap; TC ratchets from capital Thread activity | Surface: Church Cathedral = automatic Thread detection asset in any province |
| P2-28 | B5 | Knot rupture mid-contest compound Composure drain (three simultaneous sources) | Surface: Thread-active social contests have three simultaneous Composure drain vectors |
| P2-29 | B6 | Believe Co-Authorship + Recall: does Fragmented −1D cascade to Thread pools? | Rule: Thread ops are Spirit-primary, not Recall-based; −1D does not apply |
| P2-30 | B6 | Concentration track has no Thread interaction | Rule: Thread contact precludes active orator participation; Corroboration only |
| P2-31 | B6 | Lock on Mended substrate: net RS +2/season vs re-Gap cost | Rule: post-Mending substrate is Lock-eligible; RS economics validated |
| P2-32 | B6 | PP-633 simultaneous Knot Loss in mass battle = uncapped Coherence drain | Design note: mass battle practitioner casualties produce uncapped Coherence drain on player Knot partners |
| P2-33 | B7 | Locked Zone Dissonance Factor undefined | Add to Dissonance table: 1/2/3 by Lock age; Askeheim = Factor 3 |
| P2-34 | B7 | Focus 3 dead zone after halving | Fix: ceiling rounding for operation-count conversion |
| P2-35 | B7 | Duty substitution by Thread operation | Rule: Thread does not substitute for Duty; preserves dual-track design |
| P2-36 | B7 | Solidarity attack adds Knot strain | Rule: Solidarity adds +1 Knot strain per use; can rupture Knot it requires |
| P2-37 | B7 | Fractured Fallout "History uncertain" is mechanically ambiguous | Rule: scene-scoped suspension of specified History points |
| P2-38 | B7 | Coherence 0 companion NPC: ontological transition not departure | Add to companion spec §3: Coherence 0 = companion slot lost; NPC persists as world-state actor |

---

# SECTION D — P3 SURFACE (Emergent+, Design Validations, Design Notes)

| ID | Batch | Item | Note |
|----|-------|------|------|
| P3-01 | B1 | Practitioner governor Coherence → governance degradation | Emergent arc: Thread-active governor becomes less capable over time; intentional design |
| P3-02 | B1 | Community Weaving OA seasonal reset | Elegant: Community Weaving seasonal cadence matches OA reset cycle; no exploit |
| P3-03 | B1 | W-33 interaction with Saturation Counter | Companion W-33 timing is real tactical decision; surface explicitly |
| P3-04 | B1 | Warden Mending at Askeheim resets under military pressure | Surface in NPC assignments: military conflict in Proximity 1–3 = all Warden isolation work resets |
| P3-05 | B2 | Lock on in-progress obligation | Emergent political application: Lock mid-execution freezes treaty state indefinitely |
| P3-06 | B2 | Compound Ob worst case (RS Critical + Fragmented + wounds + opposition = Ob 14) | Design validation: late-game Thread requires fresh practitioners; confirmed intentional |
| P3-07 | B3 | TS growth vs Coherence depletion: Overwhelming Leaps give +1 TS; Coherence depletes far faster | Surface practitioner arc: rapid TS growth + Coherence burnout cycles |
| P3-08 | B3 | Shared RS as mutual deterrent: enemy Dissolution Failure hurts all factions equally | Design note: Thread warfare = mutual destruction; "arms control" via shared RS |
| P3-09 | B3 | Thread brinksmanship: provoking enemy Dissolution near-critical RS | Viable but high-risk; surface as intentional strategic option |
| P3-10 | B3 | Residue-enhanced Mending as defensive RS recovery loop | Combat → Dissolution → Residue → Mending: destruction feeds repair at cost |
| P3-11 | B4 | Inherited Lock: capturing faction inherits RS drain + Ob penalty + invisible to new controllers | "Lock-and-cede" named defensive strategy; discovery arc as fieldwork |
| P3-12 | B4 | Garrison Lock: Relational Lock on garrison Discipline collapses effective settlement Defense | Tactical Thread application in military layer |
| P3-13 | B5 | Almud First Leap at S-001 → Church observer at S-003 → TC +1 | Note in NPC assignments: capital Thread activity automatically generates TC |
| P3-14 | B5 | RM Community Mending as Church RS proxy: RS crisis may force theological compromise | Surface as faction dilemma: principle vs pragmatism |
| P3-15 | B5 | Church structurally unable to issue Mend BG orders (TS 0 leadership) | Design validation: Church must win politically before RS crisis |
| P3-16 | B5 | Vaynard Thread Mastery (VTM) track: if gates Vaynard TS 40-50, Varfell becomes most Thread-capable faction | Fetch params_board_game §VTM; define Thread interactions |
| P3-17 | B5 | Parliament Integrity (PI) + Thread chaos: deliberate N-way collapse to force PI auto-resolve | Surface as constitutional destabilization option |
| P3-18 | B5 | Einhir site siege = double RS drain (−1 siege + −1 Einhir site stress) | Add design note to settlement spec |
| P3-19 | B5 | Church AP system is the systemic Thread detection bridge | Design note: Thread-active factions accelerate own Church persecution via AP |
| P3-20 | B6 | Threadcut being as settlement governor De-Actualises in one season | Surface constraint: threadcut beings cannot reside in populated settlements; outpost/wilderness only |
| P3-21 | B6 | Certainty → Thread → AP → TC → RS → Certainty complete feedback loop | Design validation: six-level smooth zoom chain; document as signature design feature |
| P3-22 | B6 | Opposing ops winner Mends to stop Shifting Object drain; loser suffers continued attrition | Emergent tactical incentive for winner cleanup |
| P3-23 | B6 | Church Tribunal: Mending during own Heresy trial has positive co-movement | Only viable Thread strategy in Tribunal context |
| P3-24 | B6 | POP paradox window: first-mover has 1d3-scene immunity to counter-POP | Surface as tactical first-mover advantage in temporal Thread warfare |
| P3-25 | B6 | Inquisitor TS 30 testimony: Reason attack on theological framework | Practitioner can use Inquisitor's perception as evidence against the Inquisition's own premises |
| P3-26 | B7 | Community Weaving ×4 in Focus 5 window is self-regulating (OA + Overweave) | Design note: RS +4 at Coherence −4 cost; ~12% collapse risk Round 5; maximum RS/window via Community Weaving |
| P3-27 | B7 | Solidarity attack depleting Knot it requires | Emergent: practitioner wins through Solidarity but loses the relationship |
| P3-28 | B7 | TS 100 Overwhelming Leap: +1 TS bonus disappears at cap | Elegant fix: Ob −2 on next operation as conversion |
| P3-29 | B7 | Almud TS 30 does not meet TS ≥ 50 Generational Shift exemption | Almud ages normally despite Thread awakening; narratively appropriate |
| P3-30 | B4 | Wound penalty on Thread ops bounded by incapacitation | Design validation: wound-Thread compound penalty correctly calibrated |

---

# SECTION E — ELEGANT/SMOOTH/ROBUST FAILURES (Design Debt)

| ID | Batch | Item | Lens | Fix Priority |
|----|-------|------|------|-------------|
| E-01 | B6 | Three-axis Ob: 3 table lookups per operation | ELEGANT FAILS | P2 — pre-calculation sheet section |
| E-02 | B6 | Mending Ob column redundantly tabulates Depth Ob −1 | ELEGANT FAILS | P3 — remove column; one-line rule |
| E-03 | B6 | Dissolution Residue: 4 tracking values + volatile dice separate resolution | ELEGANT FAILS | P2 — simplify volatile dice to chain-on-9-or-10 |
| E-04 | B6 | Thread concealment: Cognition-only pool (no ×2, no History) = only outlier in Thread system | ELEGANT FAILS | P2 — align to Cognition + concealment History |
| E-05 | B6 | Leap Priority 5 + multi-engaged: "reactive defence only" undefined vs PP-274 pool split | SMOOTH FAILS | P1 — explicit ruling: full pool to Defence (0 Offence) |
| E-06 | B6 | Domain Echo for Thread ops requires GM improvisation; no Domain Action mapping | SMOOTH FAILS | P0 — mapping table required (see P0-20) |
| E-07 | B6 | Thread-Read Evidence generation 2–3× faster than mundane fieldwork | SMOOTH / ROBUST | P1 — gate to Depth ≥ 4 questions |
| E-08 | B7 | Focus 3 dead zone after halving (= same as Focus 2) | ELEGANT FAILS | P1 — ceiling rounding fix |
| E-09 | B6 | Forgetting "round" time unit undefined in exploration context | SMOOTH FAILS | P2 — map to Contact Rounds |
| E-10 | B6 | NPC practitioner Thread AI: entirely GM improvisation | ROBUST FAILS | P0 — decision tree required (see P0-22) |
| E-11 | B3 | Generational Shift Spirit −3 at Year 30: Thread pool collapses at endgame | ROBUST CONCERN | P1 — lower TS exemption threshold or cap Spirit penalty |

---

# SECTION F — RS BUDGET RECONCILIATION

*Corrected peak RS drain estimate incorporating all batch findings.*

## Peak Military Period (Year 20–25, 30-year campaign, WC 0)

| Source | RS/Season | Notes |
|--------|-----------|-------|
| Gap persistence (3 active Gaps) | −12 | −4/season each |
| Lock chronic drift (2 active Locks, seasons 4+) | −4 | −2/season each |
| Siege drain (3 simultaneous province sieges) | −3 | Per-province ruling |
| Battle drain (2 Campaign-scale battles/season) | −4 | victory_v30 §0.4; MISSING FROM ALL PRIOR BUDGETS |
| Winter baseline drift | −0.25 | −1/year |
| **Peak drain (WC 0)** | **−23.25 RS/season** | |
| WC 2 offset (halves Gap + Lock) | +8 | Gap: −12→−6; Lock: −4→−2 |
| **Peak drain (WC 2)** | **−15.25 RS/season** | |
| WC 3 offset (+2 RS/season Edeyja) | +2 | |
| **Peak drain (WC 3)** | **−13.25 RS/season** | |

Starting RS at Year 20 (assuming moderate Thread activity): ~RS 45 (Fragile band).
- WC 0: RS 45 → 0 in **1.9 seasons** → Rupture in Year 21. Campaign ends.
- WC 2: RS 45 → 0 in **2.9 seasons** → Rupture ~Year 22 without additional Mending.
- WC 3: RS 45 → 0 in **3.4 seasons** without Mending; with mass battle Mending (PP-225 ×3): each Mending Overwhelming in mass battle = RS +6. Three successful Mendings/season offsets drain entirely.

**Conclusion:** WC 3 + concentrated mass battle Mending is the only viable endgame RS strategy. WC 2 buys 1 additional season but doesn't prevent Rupture. WC 0 means the campaign ends at Year 20–21 without extraordinary intervention.

---

# SECTION G — CRITICAL PATH FOR OPEN ITEMS

## ED-SETT-01/02 (Settlement Stat Simulation + Governance Calibration)
Blocked by: P0-01 (Order as Thread config), P0-04 (siege RS drain per-settlement), P0-07 (WC variable).
Once resolved: Simulate governance action probability curves at typical governor stats. Include Thread-priming interaction.

## ED-SETT-04 (Siege Duration)
Blocked by: P0-01 (Lock on Order blocks decay), P1-03 (Pull on Order compresses timeline).
Additional: Consider Lock-and-cede as deliberate defensive option (P1-06).

## ED-SETT-10 (NPC Home Settlement Assignments)
Clear to assign. Surface: Almud First Leap TC cascade (P3-13), RM Thread detection risk (P2-03), Warden isolation reset (P3-04).

## ED-COMP-01 (Companion Candidates)
Blocked by: P0-12 (Conviction Scar + Thread mapping), P0-02 (RO as Conviction trigger).
Surface asymmetry: practitioner companions categorically more valuable in Thread-heavy campaigns.

## ED-COMP-02 (Companion Combat AI)
Blocked by: P0-02 (RO trigger), P1-13 (PP-261 Binding Op constraint), P0-12 (Conviction Scar).
Add: Dissonance checks during player Thread contact (P2-09 adjacent), Coherence 0 companion protocol (P2-38).

## ED-COMP-03 (Companion Mass Combat)
Clear to rule with: Saturation Counter timing (P3-03), RS ×3 companion Mender value (P2-21), Coherence depletion arc (P2-22), Officer vs Personal designation per turn.

## ED-137 (Panel Adjudicator Type)
Blocked by: P0-11 (Thread-Read evidence admissibility).
Additional: pre-contest Weave on panel shifts primary attribute (P2-30 adjacent).

## Obligation Loop Simulation
Blocked by: P0-17 (POP minimum TS), P0-03 (POP during contest).
OA stacking cap (P2-10) resolved independently.

## Chain Contest Convergence Simulation
Blocked by: P0-03 (POP during Memory contest), P0-11 (Thread evidence admissibility), P2-17 (audience resistance floor).

## IP Recalibration (30-year games)
Blocked by: P0-07 (WC variable), P0-09 (battle RS drain), P0-15 (Altonian practitioners), P0-04 (per-settlement siege RS).
See Section F for corrected budget.

## Generational Shift Simulation
Blocked by: P0-07 (WC variable), P0-09 (battle RS drain).
Additional: E-11 (Spirit −3 Thread pool collapse at Year 30), P3-29 (Almud TS 30 aging interaction).

---

# SECTION H — RECOMMENDED PATCH SEQUENCE

*In dependency order — each patch enables subsequent patches.*

**Phase 1 (resolve P0 blockers with no dependencies):**
1. P0-01: Settlement Order as Thread config ruling
2. P0-04: Per-province siege RS drain ruling
3. P0-05: History Resonance risk die scope
4. P0-08: R-63 fast-change domain rate table
5. P0-09: Add battle RS drain to all budget calculations
6. P0-13: Purge PP-603 cap language from skeleton
7. P0-23: Pool floor conflict (1D vs 5D) scope statement
8. P0-10: Lattice fracture threshold rewrite
9. P0-14: Designer confirmation on Ceiral Ritual Failure

**Phase 2 (resolve P0 blockers that depend on Phase 1):**
10. P0-07: Add WC state to all RS calculations (depends on P0-08, P0-09)
11. P0-06: Dissolution Residue Potency cap (depends on RS budget corrections)
12. P0-17: POP minimum TS scaling
13. P0-03: POP during Memory contest ruling (depends on P0-17)
14. P0-11: Thread-Read evidence admissibility
15. P0-02: RO as Companion Conviction trigger
16. P0-12: Conviction Scar + Thread operation mapping (depends on P0-02)

**Phase 3 (remaining P0, then P1):**
17. P0-18: Lock after practitioner death ruling
18. P0-19: Knot with threadcut being ruling
19. P0-20: Domain Echo for Thread ops mapping (depends on P0-01)
20. P0-21: Recall-based rolls at Fragmented ruling
21. P0-22: NPC practitioner Thread AI decision tree
22. P0-24/P0-28: Isolation for Foundational Mending (Einhir-gated or standard)
23. P0-25: Foundational OA consequence table
24. P0-15: Altonian Thread practitioner status (designer decision)
25. P0-16: Niflhel Harvest mechanics
26. P0-26: Warden Harvest BG order
27. P0-27: Companion post-Forgetting Conviction ruling

**Phase 4 (P1 exploits and major gaps, in roughly priority order):**
P1-01 through P1-25 per Section B.

**Phase 5 (P2, P3, and design debt):**
P2, P3, E series per Sections C, D, E.

---

# SECTION I — TOTAL FINDINGS SUMMARY

| Category | Count |
|----------|-------|
| P0 Blockers | 28 |
| P1 Critical (exploits, major gaps, conflicts) | 25 |
| P2 Important (gaps, design concerns) | 38 |
| P3 Surface (emergent+, validations, design notes) | 30 |
| Elegant/Smooth/Robust failures | 11 |
| **Total distinct findings** | **132** |

| Finding Type | Count |
|---|---|
| Exploit (mechanically reachable degenerate state) | 22 |
| Gap (undefined interaction) | 51 |
| Conflict (contradicts another canon rule) | 9 |
| Emergent+ (unplanned good design to surface) | 31 |
| Design Validation (confirmed working as intended) | 8 |
| Elegant/Smooth/Robust failure (design debt) | 11 |

---

*End of audit. Session d8b924fb834a398c.*
