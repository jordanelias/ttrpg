# THREADWORK STRESS TEST — BATCH 4
## Session: d8b924fb834a398c | Date: 2026-04-16 | Effort: MAX
## No repeats from Batches 1–3.

---

# 1. SEQUENTIAL FAILURE EJECTION VS FOCUS INVESTMENT

## 1.1 Focus 5+ Practitioners Lose the Most From First-Op Failure [EMERGENT — DESIGN PROBLEM]

Params_threadwork: "A failed operation ejects the practitioner from the contact window and applies −1D to Thread Pool Score for the remainder of the scene."

Contact window table: Focus 5 = 5 contact rounds, 4 operation rounds. If the practitioner fails their FIRST operation (round 2): they are ejected with 3 unused operation rounds lost. Their entire Leap investment (Priority 5 full-round action, Coherence cost, −1D TPS for scene) yields exactly one failed operation.

**The asymmetry:** A Focus 1 practitioner who fails their only op loses: Leap action + Coherence + −1D TPS. A Focus 5 practitioner who fails their first op loses: Leap action + Coherence + −1D TPS + 3 unspent operation rounds. The higher the Focus, the more catastrophic a first-op failure. This creates a perverse relationship: investing in Focus (to get more operations) increases the penalty of failing the first operation.

**At first-op Ob 5 TN7, 17D pool: P(failure = net ≤ 0) ≈ 3%.** Low but nonzero. Over a campaign of 50 Leaps: E[first-op ejections] = 1.5. A Focus 5 practitioner will likely be ejected mid-contact once or twice across the campaign. Each ejection wastes 3 potential operation rounds plus full Leap cost.

**[GAP]** No mechanic compensates for the asymmetric Focus penalty on ejection. Proposed: "On ejection from contact window due to failed operation, recover half the unused Focus rounds (round down) as a Sustained Contact bonus — the practitioner retains partial substrate engagement. Sustained Contact round: no operations available; Diagnosis still active; +1D to next Leap roll in the same scene." This preserves the failure consequence while preventing total Focus investment loss.

## 1.2 Overweaving Across Full Focus 5 Window [EXPLOIT — INTERNAL COLLAPSE RISK]

Overweaving: each operation after the first in the same contact window: +1 Ob cumulative. Focus 5 practitioner, 4 operation rounds, all targeting the same configuration:
- Op 1: base Ob (e.g., 3 for Relational).
- Op 2: Ob 4.
- Op 3: Ob 5.
- Op 4: Ob 6.

Failed Op 4 (collapsed overweave): RS −3 and local Shifting Object risk. At Relational scale, Op 4 fails when: E[net] at 17D TN7 ≈ 5.1 < Ob 6. P(failure) ≈ 12%. Not unlikely.

**But ejection on fail cancels Op 4 anyway** — wait. Ejection fires on any failed operation, and Op 4 failure IS the ejection. The collapsed overweave consequence (RS −3) fires independently of ejection. So Op 4 failure = ejection (contact ends) AND RS −3 AND local Shifting Object risk. All four consequences stack.

**A Focus 5 practitioner who overweaves four times in one window risks: ejection + RS −3 + Shifting Object + −1D TPS for scene.** If the campaign has pushed RS to Fragile (59-40) or below, an RS −3 at that level drops closer to Fractured spontaneous Gap thresholds. This is a significant design risk for high-Focus practitioners trying to maximize operation efficiency. Worth surfacing explicitly: "Operating all Focus rounds on the same configuration maximizes Overweaving collapse risk. Best practice: distribute operations across configurations within one contact window."

---

# 2. MENDING IMMUNITY — THREADCUT BEING COUNTER-MENDING

## 2.1 Threadcut Being at Gap Site as Passive Counter-Mending [EMERGENT+]

Mending immunity: "Cannot be directly opposed." Indirect counter: "+Ob = being's Thread Sensitivity ÷ 20 (round up), maximum +4" when a threadcut being is present at the Gap site.

A threadcut being with TS 80 adds +4 Ob to all Mending at the Gap site. At Field-scale Mending (Depth Ob 4, age modifier 0): base Ob 4. With threadcut interference: Ob 8 — the ceiling. The threadcut being's mere presence makes Field-scale Mending as hard as Catastrophic Gap Mending.

**The threadcut being doesn't need to actively oppose Mending.** It just needs to be present. Its continuous self-rendering draws on the same substrate the Mending practitioner is trying to repair. The being's presence isn't a Thread operation — it's an ontological state. It cannot be countered with Opposing Operations rules (Mending is immune to opposition; and the being isn't performing an operation to oppose).

**Counter-Mending via threadcut presence: the ideal anti-Thread-repair strategy.** A faction that controls a threadcut being (or can deploy one) can station it at a critical Gap site. The practitioner faction cannot directly remove this obstacle through Thread operations — they must either:
1. Kill or De-Actualize the threadcut being (combat, or causing sufficient Wounds/Rendering Strain).
2. Move the being away from the site (social, persuasion — requires Disposition building with a non-human entity).
3. Accept the Ob ceiling and attempt Mending anyway.

**[EMERGENT+]** This is elegant counter-play that emerges from existing rules. It should be explicitly noted as a threadcut being tactical application, and the question of whether threadcut beings can be directed by factions to specific Gap sites should be resolved (currently undefined).

## 2.2 Threadcut Being Rendering Strain From Passive Gap Presence [EMERGENT — DESIGN DEPTH]

A threadcut being stationed at a Gap site (for the counter-Mending purpose above) is within a Gap — an absence of rendered substrate. The Gap is precisely the unintelligible ground exposed. The being's self-rendering in proximity to an active Gap may accelerate its own Rendering Strain.

**No rule addresses Rendering Strain accumulation from Gap proximity.** Standard Rendering Strain accrues from TS 0 observer exposure (§6.2 beyond-ceiling rendering) and from external Thread operations. At a Gap site: there are no TS 0 observers necessarily. But the substrate disruption itself — the Gap's active unintelligible ground — may stress the being's self-rendering even without external ops.

**[GAP]** Whether Gap proximity accelerates threadcut being Rendering Strain is undefined. Proposed: "A threadcut being present within a Gap site (active unintelligible substrate exposure) accumulates +1 Rendering Strain per scene at the site, regardless of observer count. The substrate disruption competes with the being's self-rendering intentionality." This makes stationing a threadcut being at a Gap site a trade-off: effective counter-Mending at the cost of accelerated De-Actualisation.

---

# 3. KNOT ANCHORING SCENES — COHERENCE RECOVERY DESTROYS THE RELATIONSHIP

## 3.1 Recovery Loop Strain Accumulation [EXPLOIT — STRUCTURAL]

§3.5 Coherence recovery: "A Close Knot voluntarily anchoring through a dedicated Anchoring Scene (Bonds check TN 7, Ob 2): +1 Coherence. Costs the Knot +1 strain."

A practitioner who hits Fragmented (Coherence 4) after intensive Thread work uses Anchoring Scenes to recover. Each Anchoring Scene: +1 Coherence, +1 Knot strain. To recover from Coherence 2 to Coherence 6: 4 Anchoring Scenes required. Cost: 4 Knot strain on the Close Knot.

**Knot strain threshold for rupture is undefined in params_threadwork** (batch 2 finding). But 4 strain events on one Knot is clearly significant. If the rupture threshold is 5 (by analogy with threadcut being self-maintenance strain: "at 5: rendering instability"), then 4 Anchoring Scenes bring the Knot one strain event from rupture. Rupture: Disposition →−4; Composure damage = 5 (Close tier cost).

**The recovery mechanic punishes the relationship it relies on.** Each recovery cycle consumes Knot health. A practitioner who regularly Threads deeply and recovers through Anchoring Scenes will exhaust their Close Knot within 5 recovery cycles — and then has no Anchoring path for future recovery.

**Required:** Define Knot strain accumulation threshold for rupture from Anchoring strain. Proposed: "Close Knot Anchoring strain threshold: 3 (not 5 — Anchoring is an act of sustained relational labor that taxes the bond differently from momentary uses). At strain 3: the Knot enters Strained state — Anchoring still possible but Ob increases to 3. At strain 5: Knot ruptures from exhaustion of relational labor." This makes Coherence recovery a genuine long-arc resource management problem.

## 3.2 Non-Practitioner Close Knot Strain Paradox [EMERGENT+]

The Anchoring Scene costs the Knot +1 strain AND requires the Close Knot to make a Bonds check (TN 7, Ob 2). The Bonds check is the Knot partner's roll — not the practitioner's. A non-practitioner Close Knot partner with Bonds 3: pool = (3×2)+3 = 9D. P(≥2) ≈ 87%. Usually succeeds.

But: the companion spec defines companion free actions as "Read, Converse, Connect." An Anchoring Scene is none of these — it's a dedicated recovery scene. Does an Anchoring Scene consume the companion's free action? Or is it a separate scene type with no action-economy cost for the companion?

**[GAP]** Anchoring Scene action economy for the companion partner is undefined. If it consumes the companion's free social action, the player faces a seasonal trade-off: companion free action used for Anchoring (Coherence +1 for player) vs companion free action used for social fieldwork (relationship development). If it doesn't consume the companion's free action, Anchoring Scenes are free for the companion — which makes the companion a frictionless Coherence recovery tool with only Knot strain as cost.

---

# 4. RENDERING CRISIS −1 TS ASYMMETRY

## 4.1 TS 30–31 Practitioners Lose Thread Access Permanently on Recovery [OK but critical to surface]

Rendering Crisis recovery (§3.7): "Overwhelming: Coherence → 4. Permanent −1 Thread Sensitivity. Success: Coherence → 3. Permanent −1 Thread Sensitivity."

At TS 30: −1 TS → TS 29. Below Leap minimum (30). Thread ops permanently unavailable.
At TS 31: −1 TS → TS 30. Still Leap-eligible. Thread access preserved.

**A TS 30 practitioner who enters Rendering Crisis must choose between:** (a) attempting recovery (likely Success or Overwhelming, given the pool construction) and permanently losing Thread access at TS 29, or (b) accepting NPC status at season end (Failure/no attempt) and remaining Thread-capable as an NPC.

**The counterintuitive choice:** For a TS 30 practitioner, recovery is worse than remaining an NPC. An NPC at TS 30 with Coherence 0 can still Leap (if the GM allows NPC Thread use) — the rules say "character becomes NPC (100% functional, player agency ends)." A recovered practitioner at TS 29 cannot Leap at all. Player agency is preserved by recovery, but Thread capability is destroyed.

**GM guidance (PP-206) requires disclosure before the arc begins.** This is correctly identified and patched. But the deeper issue: the Rendering Crisis mechanic at TS 30–31 creates a bifurcation between "recover and lose Thread" vs "remain NPC and keep Thread potential." This bifurcation needs to be a named design decision (intended? or should recovery at TS 30–31 be exempt from the −1 TS cost?).

## 4.2 TS 100 Practitioners — Rendering Crisis Resolution Is Trivially Costless [EMERGENT+]

At TS 100: −1 TS → TS 99. TPS still = floor(99/10) = 9. Thread operations: unchanged in every mechanical respect. The Rendering Crisis "permanent cost" at maximum TS is zero functional impact.

**For TS 90+ practitioners: Rendering Crisis recovery has no Thread-mechanical cost.** Coherence is restored to 3–4 (functional practitioner). TS drops by 1 (negligible at these levels). The only cost is the full-season withdrawal and three Anchoring Scenes — significant narrative investment, no mechanical Thread degradation.

**Combined with Batch 3 finding** (TS growth via Overwhelming Leaps): a master practitioner (TS 80+) can sustain aggressive Thread use, deplete Coherence to crisis, recover with trivial TS cost, and resume at nearly full capacity. The Rendering Crisis is a designed checkpoint — but for high-TS practitioners it is a speed bump, not a wall. The wall only exists at TS 30–31. This is a significant asymmetry that rewards TS investment beyond just Thread pool improvement.

---

# 5. HYBRID STRATEGIC PHASE — MODE ARBITRAGE ON RS ×3

## 5.1 Strategic Phase Thread Ops Pay No ×3 Multiplier [EXPLOIT — MODE DESIGN]

PP-192: "All RS costs from Thread ops in mass battle ×3." Mass battle = TTRPG/Hybrid mass combat (Part A of mass_battle_v30). Strategic Phase (Part B Board Game abstraction): "Board Game: Both succeed: SO + Co-Movement Card. One succeeds: resolves + Co-Movement Card."

The Strategic Phase resolves Thread orders without the ×3 multiplier — BG rules apply, not TTRPG mass battle rules. RS effects in BG mode follow the BG Thread operation tables (Weave/Mend: RS ±1 per order). These are not subject to ×3.

**Mode arbitrage:** A practitioner in Hybrid mode can choose WHEN to perform a major Thread operation:
- Personal Phase (TTRPG): standard RS costs. If the operation occurs during a mass battle scene: ×3 applies.
- Strategic Phase (BG): no ×3. Dissolution at Strategic Phase: RS −1 per BG order resolution table (not RS −5 × 3 = RS −15).

**A Structural Dissolution in Strategic Phase costs RS −1 (BG abstraction). The same Dissolution in Personal Phase mass battle costs RS −15.** The RS cost difference is 15×. Structuring major Thread operations as Strategic Phase declarations instead of Personal Phase actions is the most RS-efficient approach available.

**[EXPLOIT — MODE DESIGN]** This arbitrage is presumably unintended. The BG abstraction layer was designed for faction-scale operations (no personal Coherence cost etc.) but the RS savings are enormous. Required ruling: "Dissolution and Locking declared at Strategic Phase use the Hybrid RS table (not BG order table) — RS costs are per the TTRPG operation tables without the ×3 multiplier (Strategic Phase is not mass battle). Weave and Mend at Strategic Phase retain BG abstraction RS values."

## 5.2 Coherence Cost in Strategic Phase — Hybrid Asymmetry [GAP]

The Hybrid Coherence declaration rule (PP-198): "Coherence cost paid by the PC who declares leadership at Phase 1." The declaring PC pays Coherence per TTRPG rules for the operation type and scale.

**What scale is a Strategic Phase Thread operation?** BG Thread orders are faction-scale (abstracting all Thread work in a territory into a single order). The actual Thread scale of the underlying operation is unstated. A Weave BG order covers what TTRPG scale? Territorial? Structural? The Coherence cost depends on the answer. If BG Weave = Territorial scale: Coherence −1. If BG Weave = Structural: Coherence −2. Multiple Strategic Phase Thread declarations per season stack Coherence costs on the single declaring PC.

**[GAP]** BG Thread order → TTRPG scale mapping for Coherence purposes is unspecified. Proposed: "BG Weave order = Territorial scale (Coherence −1). BG Mend order = Territorial scale (Coherence −1). BG Dissolution/Lock order = Structural scale (Coherence −2 + FR surcharge). BG Investigate = Personal scale (Coherence 0)." This gives a deterministic Coherence mapping for Hybrid Strategic Phase declarations.

---

# 6. THREAD-READ EVIDENCE BEFORE NON-PRACTITIONER ADJUDICATOR

## 6.1 Thread-Derived Evidence Is Epistemically Inaccessible to TS 0 Judges [GAP — CRITICAL]

Thread-Read produces investigative evidence from Thread configurations. "TS ≥ 30 required." This evidence is Thread-perceptual — the practitioner perceives Thread configurations that TS 0 characters literally cannot render.

In a social contest before an Expert Judge (TS 0): "Judge evaluates logical structure" (Cognition primary attribute). A practitioner cites Thread-Read evidence: "I Diagnosed the configuration and perceived that the treaty's Thread actualization showed signs of prior Weaving — someone bound this agreement more tightly than its terms suggest."

**The Expert Judge with TS 0 cannot verify, refute, or evaluate this evidence.** The Inert Knowledge principle (P-08, PP-497): "A TS 0 consciousness cannot render Thread-level structure." The judge cannot even assess whether the practitioner is lying or confused — the evidence is genuinely beyond their rendering capacity.

**Three possible rulings, each with different implications:**
1. Thread-derived evidence is inadmissible before TS 0 adjudicators (it cannot be evaluated → it cannot change the Piety Track). Practitioners must translate Thread evidence into physical-world terms.
2. Thread-derived evidence gets automatic Overwhelming for the practitioner's argument (the judge cannot refute it = it stands). This is exploitable.
3. Thread-derived evidence is treated as an Authority resonance attack: "My perception, which you cannot verify but which I assert with complete epistemic confidence, says X." The judge's response depends on their Trust in the practitioner.

**[GAP — CRITICAL]** Required ruling before Thread-Read evidence appears in any contest design. The most defensible option: Thread-derived evidence is valid only before adjudicators with TS ≥ 30 OR when accompanied by physical corroboration (what physical evidence resulted from the Thread configuration?). Pure Thread perception with no physical correlate is inadmissible before TS 0 adjudicators.

---

# 7. PROVINCE CAPTURE WITH INHERITED ACTIVE LOCK

## 7.1 The New Faction Inherits the RS Drain [EMERGENT+]

A defender-faction practitioner, before their province Seat is captured, places a Relational Lock on the province's institutional loyalty configuration. The defender loses the province militarily. Lock persists — it is not removed by the defender's departure. The new controlling faction now:

1. Governs a province with a Lock on institutional loyalty (the population's loyalty is frozen at the configuration the defender set it at — which may be loyalty to the OLD faction).
2. Pays the Lock's chronic RS drain from Season 2: −1 RS/season (Seasons 1–3), −2 RS/season (Season 4+).
3. Faces +1 Ob to all Thread operations in the province from Season 2 (lock congestion).
4. Cannot pull the Lock without knowing the original practitioner's TS (Pull Ob = TS ÷ 10 − 2). If the defender's TS is unknown: the new faction doesn't know what Ob to expect.

**The Lock is a weapon that costs the defender Coherence (−1) and RS (−1 initial) but costs the ATTACKER continuous RS drain indefinitely.** The original practitioner absorbs a one-time cost; the inheriting faction absorbs the ongoing cost. This is a strategically rational defensive use of Locking — a scorched-substrate policy.

**[EMERGENT+]** This emergent defensive strategy should be named and noted. "Lock-and-cede" — place Locks on critical provincial configurations before military defeat, forcing the inheritor to either accept the RS drain or invest significant Thread resources to Pulling locks they didn't cause.

## 7.2 Lock Discovery — Inheriting Faction Doesn't Know It's There [EMERGENT+]

A Lock on an institutional configuration (loyalty, political structure) has no visible marker to non-practitioners. TS 0 faction leaders: "Nothing perceived." TS 10–29: "Vague unease; cannot locate source." TS 30–49: "Senses an operation in the scene; general direction identifiable" — but this is for ACTIVE operations, not persistent Locks.

**How does the new faction discover the Lock?** They would need a practitioner with TS ≥ 30 to Diagnose the province (Diagnosis: free during Thread contact, reveals Thread configuration type, approximate scale, RS signature). Without a practitioner Diagnosing the province, the Lock is invisible — the faction just sees mysteriously stubborn institutional resistance and unexplained RS drain.

The RS drain (−1/season from Season 2) is also not self-explaining. The new faction sees RS declining but has no obvious cause without Thread Sensitivity to Diagnose the source. This produces gameplay: "Why is our RS declining? We're not running any Thread operations here." The investigation to find the hidden Lock is a legitimate fieldwork arc.

---

# 8. LOCK ON GARRISON DISCIPLINE — ANTI-MILITARY THREAD OPERATION

## 8.1 Freezing a Garrison's Fighting Effectiveness [EMERGENT+]

Settlement spec §5.2: "effective Defense = settlement Defense + garrison Discipline." A garrison unit's Discipline (unit stat 1–7) adds directly to settlement Defense for assault checks.

A attacking practitioner could Lock the garrison's Discipline configuration — freezing the unit's cohesion and fighting effectiveness at its current (possibly degraded) value. After a garrison has been worn down (Discipline reduced from skirmishes or morale pressure): Lock it. The garrison cannot reform (recovery would change its Discipline configuration — "unable to become" prevents improvement).

- Ob: Depth 3 (Relational — the bonds of unit cohesion) + Breadth 2 (Formation — garrison of ~200-500 soldiers) + Distance 1 (Near, outside walls) = **Ob 6, TN 8**.
- TS 50+, pool 17D TN8: P(≥6) ≈ 62%.
- On Success: garrison Discipline locked. RS −1. Discipline cannot recover. Effective settlement Defense = base Defense + (locked) low Discipline permanently.
- Chronic drift: RS −1/season from Season 2.

**Combined with the Assault mechanic:** If garrison Discipline is Locked at 2 (damaged), settlement Defense = base + 2. A Fortress with base Defense 4: effective Defense 6. Much more manageable for an attacker than Defense 4 + Discipline 5 = effective Defense 9. The Lock transforms an impregnable fortress into an assaultable one.

**[EMERGENT+]** The anti-garrison Lock is an elegant tactical Thread operation that has military-layer consequences via the settlement spec's effective Defense formula. This should be an explicit tactical note in the Thread military application section: "A Relational Lock on a garrison's unit cohesion (Discipline) prevents Discipline recovery, degrading effective settlement Defense over time as the garrison cannot reform."

---

# 9. IP TRACK VS EXPEDITION OPPORTUNITY COST

## 9.1 The Strategic Tension is Mechanically Unmodeled [GAP — DESIGN PROBLEM]

WR decrease: "No expedition 3+ seasons −1 WR." WR/WC are the primary RS mitigation system (Batch 3). Southernmost expeditions maintain WR/WC. But:

- Each expedition consumes scene actions (travel to T15, crossing Forgetting boundary, fieldwork in Southernmost).
- At high IP (Year 20+, IP ~60–80), military crises demand player attention. Parliamentary sessions, military campaigns, faction diplomacy, siege defense all compete for scene actions.
- Scene actions are the primary resource in player_agency_v30's Scene Slate system.

**At IP 60+, the player likely cannot spare scene actions for expeditions.** They skip 3+ seasons of expeditions = WR −1. WC drops (WR gates WC). The RS buffer diminishes exactly when military activity (sieges, battles) maximizes RS drain. This is a designed squeeze: military pressure and RS buffer maintenance require the same limited resource (player time/scene actions) at the same moment.

**[EMERGENT+ — but unmodeled]** This strategic tension is the central design challenge of the mid-to-late game but no document articulates it. The settlement layer, IP recalibration, and WC system collectively create this tension — but they don't acknowledge each other. Required: a cross-reference note in both the IP recalibration section and the WC system noting the expedition opportunity cost tension. This is the mechanical spine of the "two simultaneous contests" design (who governs AND whether the world survives).

---

# 10. CONVICTION SCAR SYSTEM — THREAD OPERATIONS NOT LISTED AS TRIGGERS

## 10.1 Thread Operations as Missing Conviction Scar Events [GAP — CRITICAL]

Companion spec §5.3: "Their Conviction Scar accumulation rate may be higher because the player's actions constantly test their framework." The NPC behavior system defines Conviction Scars as accumulating from specific event types. From the NPC behavior doc (visible portion): Conviction Taxonomy and Resonant Style — but no explicit Conviction Scar trigger list in the skeleton.

**Inference from Batch 2 finding** (RO as Conviction trigger for departure): witnessing Dissolution or Lock used on living beings should count as a departure violation. But Conviction Scars are a deeper NPC system — they accumulate over time toward personality arc branches, permanent behavioral shifts. They are distinct from the 3-strike departure rule.

**Thread operations visible to companions include:**
- Weaving (cohering reality): morally ambiguous — Order companions may approve (stability), Equity companions may disapprove (power over substrate).
- Locking living configurations: Order companions may approve (preventing change), Equity companions may strongly disapprove (removing ability to become).
- Dissolution of non-living configurations: context-dependent.
- Dissolution of living beings: all non-Autonomy, non-Continuity companions should react strongly.
- Mending: universally positive — repair, restoration, maintenance.

**[GAP — CRITICAL]** Thread operations are not mapped to the Conviction Scar system. Without this mapping, companions who witness sustained Thread use (both constructive and destructive) have no systematic moral response beyond the 3-strike departure rule. For a game where Thread is central, this is a major behavioral design gap. Required: a Thread operation → Conviction Scar mapping table specifying which operations generate positive/negative Scar events for each Conviction type.

---

# 11. OPPOSING OPERATIONS SHIFTING OBJECT — COHERENCE DRAIN AFTEREFFECT

## 11.1 The Shifting Object Practitioners Created Now Costs Them [EMERGENT+]

PP-303: "When a Shifting Object is present in a territory: Practitioners within 50m: Coherence check TN 7 Ob 1 per scene. Failure: Coherence −1."

Two practitioners oppose each other → both meet Ob → Shifting Object forms at target's scale.

Both practitioners are within 50m (they were just opposing each other at the same configuration). End of the round: both face PP-303 Coherence check Ob 1. At Spirit 3–4 (typical), pool 6–8D TN7 Ob1: P(≥1) ≈ 80–93%. P(failure) ≈ 7–20%. Expected Coherence cost from PP-303 per practitioner per scene: 0.07–0.20 additional.

**Over a sustained confrontation (multiple scenes in same territory with active Shifting Object):** Both practitioners drain Coherence further. Each subsequent scene the Shifting Object persists: another check. The Shifting Object they created through conflict continues to cost them both.

**The confrontation is self-punishing beyond the immediate Knot strain.** After the opposing operations:
- Both pay Knot strain (+1 Ob next Thread op, 2 Composure).
- The Shifting Object lasts until Mended (Ob 2 = Micro-Gap level).
- Until Mended: both practitioners in the same territory drain Coherence every scene.
- The practitioner who Mends the Shifting Object pays Coherence −1 (Mending cost) — but ends the drain.

**[EMERGENT+]** Opposing operations leave an aftereffect that incentivizes one practitioner to Mend the Shifting Object (ending their own drain). But Mending costs Coherence too. The cheapest resolution: the WINNER Mends (lower Coherence loss than continued drain), because they have more Coherence remaining. The LOSER (more Knot strain, potentially lower Coherence) may be unable or unwilling to Mend. This creates a strategic dynamic: winners clean up after fights to stop ongoing drain; losers suffer continued attrition.

---

# 12. KNOT RUPTURE MID-CONTEST → COMPOSURE HIT → RATTLED

## 12.1 Knot Strain Cascade During High-Stakes Contest [EMERGENT+]

Knot strain can accumulate from:
- Opposing operations Knot strain (2 Composure per standard loss, 4 Composure per FR loss).
- Thread-Read relay strain.
- Anchoring scene strain.

If a Knot is already at strain 2–3 and the practitioner is in a high-stakes social contest where Thread operations are also firing (Batch 2 finding: Thread + social contest double layer):

- Thread opposing operations fire → Knot strain +1 → threshold reached → Rupture.
- Rupture: Composure damage = tier cost (Close = 5 Composure).
- Composure = Charisma + 6 (minimum 7). A practitioner with Charisma 3: Composure 9. Taking 5 Composure damage → Composure 4.
- "Rattled" threshold fires at Composure ≤ 3 (presumed — the social contest system defines Composure as the social damage buffer before Rattled).

**A Knot rupture mid-contest is unlikely to immediately Rattle the practitioner (they'd need to already be at Composure ≤ 8 to reach Rattled from a 5-Composure hit).** But it contributes to the contest's social damage in a scene where Thread operations are already costing Composure. Multiple sources of Composure drain in the same contest (Thread Knot strain + contest exchange damage + Knot rupture) can produce Rattled in a single session.

**[EMERGENT+]** The compound Composure drain from Thread-active social contests should be explicitly noted. In a high-stakes political scene where the practitioner is both contesting AND performing Thread operations, Composure is under simultaneous pressure from three directions: contest exchange damage, Thread Knot strain, and potential Knot rupture. Rattled is reachable faster than the individual mechanics suggest.

---

# 13. CHURCH THEOLOGICAL FORECLOSURE → NO BG MEND ORDERS

## 13.1 Church Cannot Issue Thread BG Orders [EMERGENT+ — FACTIONAL DESIGN]

Church faction leadership: "Thread Sensitivity 0. Theologically foreclosed (Foundations §9.1). Cannot develop without confrontation that shatters the prophylaxis."

BG Thread orders require TS ≥ 30 affiliation: "Available to any faction with an affiliated Thread Sensitivity 50+ character, or Revolution (via Community Mending)."

**Church has TS 0 leadership. Church cannot issue Mend, Weave, or Investigate Thread BG orders.** The Church is structurally unable to address RS degradation through the primary RS restoration mechanic. Its victory conditions don't require Thread engagement — but the Universal Victory Condition (Accord ≥ 2 all territories) is threatened by RS decay, which the Church cannot directly address.

**The Church is structurally blind to the RS crisis** (noted in victory_v30 "Core Frame"). This is confirmed by the BG Thread order gate: the Church cannot Mend. Its only RS-adjacent capability is the Co-Movement Card from BG opposing operations (if an enemy Thread op fires and the Church has a practitioner... which it doesn't by canon).

**Design validation:** The Church's inability to address RS is intentional. Their path to victory relies on political dominance (CI, Graduated Seizure) before RS becomes critical — they must win politically before the world becomes unlivable. The Mend BG order unavailability is the mechanical expression of this structural blindness. Worth stating explicitly.

---

# 14. VARIABLE RS DRIFT BY LOCK DOMAIN TYPE (R-63) — UNDEFINED FAST-CHANGE DOMAINS

## 14.1 R-63 Creates an Undefined Ob Variable in Every Lock Calculation [GAP]

R-63: "Replaces uniform −1 Mending Stability/season for locked institutions: Slow-change domain (seasonal/yearly evolution): −1 Mending Stability/season. Game Master determines domain type when Lock is applied."

The slow-change domain rate (−1/season) is defined. The fast-change domain rate is not stated. The rule says "Game Master determines domain type" — implying there are multiple domain types with different rates — but only slow-change is specified.

**Every RS calculation involving a Lock contains this undefined variable.** Locking a military deployment (fast-changing: forces move weekly) vs locking a dynastic claim (slow-changing: changes generationally) should produce different RS drain. But the rates for non-slow domains are absent.

**[GAP — CRITICAL to all Lock RS calculations]** Proposed domain table:
| Domain Type | RS Drift Rate | Examples |
|---|---|---|
| Slow-change (seasonal/yearly) | −1/season | Agricultural cycles, trade patterns, dynastic succession |
| Standard (monthly/quarterly) | −1.5/season | Political alignments, institutional loyalties, diplomatic agreements |
| Fast-change (weekly/daily) | −2/season | Military deployments, crisis responses, active negotiations |
| Inert (generational+) | −0.5/season | Cultural identities, deep historical claims, ethnic boundaries |

Without this table, GMs improvise Lock RS drain rates inconsistently across the campaign, making RS budget projections unreliable.

---

# 15. WOUND PENALTY STACKING FOR PRACTITIONERS

## 15.1 Same Wound Costs Thread AND Combat [EMERGENT — DESIGN VALIDATION]

Combat params: "Wounds: −1D per wound (cumulative)." Thread Leap: "+1 Ob per Wound."

A practitioner with 2 Wounds:
- Combat pool (Agi×2+History+3): −2D.
- Thread Leap: +2 Ob.
- Thread operation: +2 Ob (wound penalty applies to "all Thread operation rolls — Leap, Weaving, Pulling, Mending, FR").

**Every wound costs the practitioner simultaneously in combat AND Thread operations.** A practitioner with 3 Wounds is: −3D combat pool AND +3 Ob on every Thread operation. At Ob 3 (Relational scale), effective Ob = 6. At 18D − 3 = 15D TN7: P(≥6) ≈ 79%. Still functional. At 5 Wounds (near incapacitation): −5D combat, +5 Ob Thread → Relational op at effective Ob 8. 13D TN7 Ob8: P(≥8) ≈ 33%.

**Incapacitation threshold (ceiling(Health÷2)) at End 3: Health = (3+6)×(max wounds+1).** At Incapacitation: contact terminates. So a practitioner is incapacitated before they reach 5 wounds at End 3. The wound-Op penalty is bounded by incapacitation — you can't have so many wounds that Ob becomes infinite, because you'd be incapacitated.

**[OK — design validation]** The wound penalty on Thread operations is correctly calibrated: severe enough to create genuine risk for wounded practitioners attempting Thread ops, not so severe as to make it impossible until incapacitation. A wounded practitioner can still operate but at meaningfully degraded probability. No change needed — surfacing as validation.

---

# 16. BATTLE RS DRAIN FROM VICTORY DOC — UNINCORPORATED

## 16.1 RS −1 Per Battle on Valorian Soil Not In Any RS Budget [CONFLICT — OMISSION]

victory_v30 §0.4: "Each Battle on Valorian soil: RS −1 (Campaign/War scale: RS −2). Each season with inter-faction battle: IP +2, Strain +1."

This RS drain source is entirely separate from:
- Thread operation RS costs
- Lock chronic drift
- Gap persistence drain
- Winter annual drift
- Siege drain

**Every RS budget calculation in Batches 1–3 is missing this term.** In a 30-year game with the halved IP rate: battles still occur. At IP 80 (Year 30), Altonian invasion involves multiple Campaign/War scale battles: RS −2 per battle. If 5 major battles occur in the last decade (Year 20–30): RS −10 from battles alone, separate from all other sources.

Adding this to the Year 20–25 peak drain scenario (Batch 1):
- Original estimate: ~−9.25 RS/season at peak.
- Battle drain (2 battles/season at Campaign scale, Year 20–25): −4 RS/season additional.
- Revised peak: **~−13.25 RS/season** during peak military period.

From RS 45 (likely at Year 20): to RS 0 in ~3.4 seasons. **The endgame crisis is faster than Batch 1 calculated.** WC 2 (halves Gap/Lock drain) doesn't affect Battle RS drain. Battle drain is not in the Gap/Lock category. WC 2 is less helpful than Batch 3 suggested during peak military periods.

**[CONFLICT — CRITICAL]** Required: all RS budget calculations must include Battle RS drain term from victory_v30 §0.4. The 30-year game RS trajectory is more acute than all prior batches modeled.

---

# 17. COLLECTIVE OPERATION LATTICE FRACTURE THRESHOLD MATH

## 17.1 Fracture Threshold Is Harder to Trigger Than It Appears [EMERGENT+]

Thread §2.5: "if remaining pool drops below half the Anchor's solo pool: +1 Ob (lattice fractures)."

Threshold = ½ of Anchor's SOLO pool, not ½ of intended combined pool. Anchor solo pool: Spirit 5, History +8D, TPS 7 = 23D. Fracture threshold: <11.5D → ≤11D.

With 4 helpers each contributing +2D (floor(Cognition÷2) at Cog 4): combined pool = 23 + 8 = 31D. If 3 helpers drop: pool = 23 + 2 = 25D. Still >> 11D. If ALL helpers drop: pool = 23D. Still above threshold. The lattice never fractures from helper dropout at this Anchor pool size because the Anchor's solo pool IS already above half of itself.

**The lattice fracture rule is only relevant when the Anchor's solo pool is high AND helpers are contributing significantly AND a large fraction drop.** Specifically: fracture requires remaining pool < (Anchor solo ÷ 2). If all helpers drop, remaining = Anchor solo. Anchor solo < (Anchor solo ÷ 2) is mathematically impossible. **The lattice NEVER fractures from helper dropout alone.**

**[EXPLOIT — mathematical]** The lattice fracture condition "pool drops below half Anchor's solo pool" cannot be triggered by helpers dropping out, because removing helpers brings the pool toward the Anchor's solo pool, which is never below half of itself. The only way to trigger lattice fracture is if helpers are contributing NEGATIVE dice somehow (opposing beliefs removing dice beyond what they contributed), which is not a defined mechanic.

**Required ruling:** The lattice fracture threshold is probably intended as: "below half of the INTENDED combined pool" — not half of the Anchor's solo pool. "Intended combined pool" = Anchor solo + all declared helper contributions. If 3 of 4 helpers drop from an intended pool of 31D: remaining = 25D. Half of 31D = 15.5D. 25D > 15.5D: no fracture. If all 4 helpers drop: remaining = 23D. 23D > 15.5D: still no fracture. Even with this correction, fracture is very hard to trigger. Perhaps the intent is: "below half of the minimum viable collective pool," defined at context.

---

# 18. BG STARTING RS 72 VS TTRPG RS 60 — HYBRID TRANSITION

## 18.1 Mode Entry RS Value Is Undefined for Hybrid [GAP]

params_threadwork: "Starting: TTRPG default 60; BG default 72." Hybrid mode begins with... what? The Hybrid combines both modes. Does Hybrid start at 60 (TTRPG default), 72 (BG default), or an average (66)?

**The 12-point difference is significant.** At RS 72 vs RS 60: the BG starting position is 12% further from Rupture. In a 30-year game, this 12-point buffer represents roughly 1.5 years of baseline drift (−1 RS/year) — or one additional Dissolution Success's worth of RS.

**More critically:** If a campaign begins in BG mode (RS 72) and transitions to Hybrid (adding Personal Phase Thread operations), does RS carry forward from BG (at whatever RS BG has reached) or reset to TTRPG default (60)?

**[GAP]** Required ruling: "Hybrid mode inherits RS from whichever mode it transitions from. A campaign that begins in BG mode and transitions to Hybrid carries BG's accumulated RS value — it does not reset to 60. A campaign that begins in TTRPG mode and adds the BG layer (Hybrid introduction) carries TTRPG's accumulated RS." Starting RS for pure Hybrid play: 66 (midpoint, reflecting the dual nature of Hybrid mode from session 1).

---

# SUMMARY TABLE — BATCH 4

| Item | Finding | Severity | Action Required |
|------|---------|----------|----------------|
| Sequential ejection | Focus 5 practitioners lose 3 op rounds on first-op failure; Focus investment inversely penalizes ejection | **[EMERGENT — DESIGN PROBLEM]** | Proposed: partial recovery mechanic (Sustained Contact) on ejection |
| Overweaving | Focus 5 × 4 same-config ops → Op 4 at Ob 6, 12% collapse risk → ejection + RS −3 + Shifting Object + −1D TPS | **[EXPLOIT — INTERNAL]** | Surface as explicit player guidance against single-config overweaving |
| Threadcut counter-Mending | TS 80 threadcut being at Gap site: +4 Ob to all Mending, at Mending Ob ceiling | **[EMERGENT+]** | Note: passive presence is the ideal anti-Mending deployment |
| Threadcut Gap presence | Gap site proximity as additional Rendering Strain source — undefined | **[GAP]** | Rule: +1 Rendering Strain/scene at active Gap site |
| Anchoring recovery loop | 4 Anchoring Scenes to recover from Coherence 2 = 4 Knot strain; one event from rupture | **[EXPLOIT — STRUCTURAL]** | Define Knot Anchoring strain threshold (proposed: 3 = Strained, 5 = Rupture) |
| Anchoring action economy | Anchoring Scene companion cost undefined; potentially free for companion | **[GAP]** | Rule: Anchoring Scene consumes companion's free action OR define it as separate scene type |
| TS 30–31 Rendering Crisis | Recovery permanently removes Thread access; remaining as NPC is mechanically better | **[OK — critical to surface]** | PP-206 disclosure is correct; add design note on the TS 30–31 bifurcation choice |
| TS 100 Rendering Crisis | −1 TS at maximum = zero functional impact; crisis is a speed bump not a wall | **[EMERGENT+]** | Surface asymmetry: Rendering Crisis cost inversely proportional to TS |
| Strategic Phase ×3 arbitrage | Structural Dissolution at Strategic Phase: RS −1 (BG). Same op at Personal Phase mass battle: RS −15 | **[EXPLOIT — MODE DESIGN]** | Ruling: Strategic Phase Dissolution/Lock use TTRPG RS tables (without ×3) |
| BG Thread order → TTRPG scale | Coherence cost for Strategic Phase ops requires scale mapping; undefined | **[GAP]** | Proposed mapping: BG Weave/Mend = Territorial (Coh −1); BG Dissolution/Lock = Structural (Coh −2+FR) |
| Thread-Read evidence | Epistemically inaccessible to TS 0 adjudicators; three possible rulings, each with different game implications | **[GAP — CRITICAL]** | Ruling: Thread evidence valid only before TS ≥ 30 adjudicators OR with physical corroboration |
| Inherited Lock | Captured province carries predecessor's Lock: RS drain + Ob penalty + invisible to new faction | **[EMERGENT+]** | Name "Lock-and-cede" as a defensive strategy; surface discovery arc |
| Garrison Lock | Relational Lock on garrison Discipline: prevents reform, collapses effective settlement Defense | **[EMERGENT+]** | Surface as tactical Thread application in military layer notes |
| IP vs expedition opportunity | High IP demands player attention exactly when expedition (WC maintenance) is most needed | **[GAP — DESIGN PROBLEM]** | Cross-reference note in both IP recalibration and WC system: this is the spine of the two-contest design |
| Conviction Scar + Thread | Thread operations not mapped to Conviction Scar system; companion moral response to Thread is only the 3-strike departure rule | **[GAP — CRITICAL]** | Require: Thread op → Conviction Scar mapping table per Conviction type |
| Opposing ops aftereffect | Shifting Object from opposing ops → PP-303 Coherence checks → both practitioners drain Coherence per scene until Mended | **[EMERGENT+]** | Winner Mends to stop their own drain; loser suffers continued attrition |
| Knot rupture mid-contest | Compound Composure drain (contest exchange + Thread Knot strain + Knot rupture) → Rattled faster than individual mechanics suggest | **[EMERGENT+]** | Surface: Thread-active social contests have three simultaneous Composure drain vectors |
| Church Mend BG gate | Church cannot issue BG Thread orders; structurally unable to address RS; must win before RS crisis | **[EMERGENT+ — design validation]** | State explicitly in Church faction design notes |
| R-63 fast-change domains | Only slow-change rate defined; fast/standard/inert rates absent; all Lock RS calculations contain undefined variable | **[GAP — CRITICAL]** | Define complete domain rate table (proposed in text) |
| Wound + Thread stacking | Same wound costs −1D combat AND +1 Ob Thread; bounded by incapacitation threshold | **[OK — design validation]** | No change needed; confirm calibration is intentional |
| Battle RS drain | RS −1/battle on Valorian soil (−2 Campaign/War scale) not in any RS budget calculation across Batches 1–3 | **[CONFLICT — CRITICAL]** | Add Battle RS drain term to all RS calculations; peak drain revised to ~−13.25 RS/season |
| Lattice fracture math | Threshold "below half Anchor's solo pool" is mathematically impossible to trigger by helper dropout alone | **[EXPLOIT — mathematical]** | Clarify: threshold should be "below half of INTENDED combined pool" |
| Hybrid RS starting value | Hybrid transition RS: undefined; 12-point gap between BG (72) and TTRPG (60) defaults | **[GAP]** | Rule: Hybrid inherits from transitioning mode; pure Hybrid start = 66 |

---

## NEW CRITICAL ITEMS FROM BATCH 4

11. **R-63 fast-change domain rates** — undefined variable in every Lock RS calculation. All chronic Lock drift budgets are estimates at best. Must be defined before any Lock-RS modeling is reliable.

12. **Battle RS drain from victory_v30** — completely unincorporated into RS budget work. Peak RS drain in all prior batches is underestimated. The 30-year game RS endgame is more acute than modeled.

13. **Thread-Read evidence admissibility** — cannot finalize the social contest system or Thread-Read design until there is a ruling on what Thread-derived evidence means before a TS 0 adjudicator.

14. **Lattice fracture threshold wording** — the current wording makes the mechanic mathematically inert. Requires a rewrite to be functional.

15. **Conviction Scar + Thread operation mapping** — companion moral response system is incomplete without this. Thread is the most morally-loaded action type in the game and it has no Conviction Scar implications currently.

---

*End of document. Session d8b924fb834a398c.*
