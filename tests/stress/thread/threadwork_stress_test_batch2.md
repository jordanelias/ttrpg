# THREADWORK STRESS TEST — BATCH 2
## Session: d8b924fb834a398c | Date: 2026-04-16 | Effort: MAX
## No repeats from Batch 1. New angles only.

---

# 1. PROVINCE ACCORD MANIPULATION VIA SINGLE-SETTLEMENT ORDER WEAVE

## 1.1 The Exploit Setup [EXPLOIT — MAJOR]

Settlement spec §1.3: "Province Accord = floor(average Order across all settlements, rounded down)."

T8 Gransol: 3 settlements — S-015 Parliament (Order 4), S-016 Harbor (Order 3), S-017 Market Quarter (Order 3). Province Accord = floor((4+3+3)/3) = floor(3.33) = 3.

A practitioner targets S-015 Gransol Parliament specifically with a Relational Weave on the Parliament's institutional cohesion:
- Ob: Depth 3 + Breadth 2 (Formation — parliamentary staff, guards, civil servants ~200 people) + Distance 0 = **Ob 5, TN 7**.
- Success: per Batch 1 proposed ruling, Order +1 at S-015. Parliament Order → 5.
- New Province Accord: floor((5+3+3)/3) = floor(3.67) = **3**. No change.

One more Weave on S-016 Harbor (Order 3 → 4):
- New Province Accord: floor((5+4+3)/3) = floor(4) = **4**. Province Accord increments.

**The exploit:** A practitioner with two contact windows (two separate seasons or two Focus rounds) can raise Province Accord by 1 by Weaving two settlements sequentially. Accord is the primary win condition (Universal victory requires Accord ≥ 2 all provinces; faction-specific conditions include Accord thresholds). A practitioner governor can Thread-force province Accord advancement without any political groundwork.

**The cost check:** Two Relational Weavings = Coherence −2. RS from degree tables: Success (×2) = 0 RS change. Partial (×2) = −2 RS. These are manageable. The Accord gain via Thread-Weaving is essentially free except for Coherence.

**But wait — does the Accord derivation from Order even fire immediately, or only at Accounting?** The settlement spec says "Province Accord is now the floor of the average Order across all settlements." This reads as a continuous derivation, not a seasonal one. If it's continuous, Weaving Order mid-season immediately changes Province Accord mid-season — including during Parliamentary sessions, military negotiations, and Victory checks. If it's only computed at Accounting, the exploit is limited to once-per-season Accord manipulation.

**Required ruling:** Province Accord derivation from settlement Order average is computed **at Accounting only** (not continuously). Mid-season Order changes (from Weaving, Pacify, or events) take effect at next Accounting. This limits the exploit to one Accord-manipulation cycle per season and integrates with the existing Accounting rhythm. Without this ruling, real-time Accord manipulation via Thread is uncapped.

## 1.2 Single-Settlement Province — Accord = Order (No Averaging) [GAP]

T7 Rendstad: 1 settlement only (S-018, Order 2). Province Accord = floor(2/1) = 2. A single Relational Weave on Rendstad (Success → Order 3): Province Accord immediately → 3. There is no averaging buffer. Single-settlement provinces have 1:1 Thread → Accord leverage with zero dilution.

T11 Halvardshelm: 1 settlement (S-030, Order 2). Same vulnerability.

**Both are Varfell provinces.** A practitioner aligned with Varfell (or opposed to it) can swing these single-settlement provinces by one full Accord point with a single Relational Weave at Ob 5. Given that peninsular_strain Accord tables define political crisis thresholds, single-settlement province Accord manipulation is a direct political intervention tool. This is a structural asymmetry — provinces with more settlements are harder to Thread-manipulate because Accord dilution requires multiple Weavings.

**[GAP]** Multi-settlement vs single-settlement Thread-Accord vulnerability is uneven by design accident, not intent. Requires a note at minimum: "Single-settlement provinces are structurally more vulnerable to settlement-level Thread manipulation of Accord than multi-settlement provinces."

---

# 2. RS FRACTURED BAND → NPC STANCE TRIANGLE DESTABILIZATION

## 2.1 Inconsistent Memory Under Fractured RS [EMERGENT+ — design depth]

RS 39–20 (Fractured): "Non-practitioners experience rendering failures — inconsistent memories, déjà vu, objects in wrong places."

NPC social behavior is governed by the Stance Triangle: Conviction, Resonant Style, Certainty. The Evidence Resonant Style specifically depends on the NPC's ability to hold consistent factual knowledge ("specific, verifiable, named facts"). At Fractured RS: the NPC's memories are inconsistent. Evidence attacks — which require the NPC to confront facts they cannot dismiss — become structurally destabilized. The NPC's memory of the facts is itself unreliable.

**Mechanical implication:** Evidence Resonant Style attacks in a Fractured RS world lose some of their epistemic authority. An Evidence attack that presents "the Church's own records show X" to Himlensendt is partially undermined if Himlensendt cannot reliably distinguish between his memory of those records and rendering-failure artifacts. He's not sure whether he remembers the document or imagined it.

**This is not defined anywhere.** The NPC behavior system and the Rendering Stability threshold system operate in parallel without interaction. Required integration point: at Fractured RS (39–20), all NPCs make Recall checks (TN 7 Ob 1) before relying on Memory-genre claims in social contests. Failure: −1D on Memory-genre Argue pool for that exchange (their memory is rendering-failure compromised).

## 2.2 Fractured RS → Certainty Track Acceleration [EMERGENT+]

Rendering failures (objects in wrong places, inconsistent memories, déjà vu) are exactly the kind of Thread evidence that drives Certainty decline. The Certainty track advances toward Thread acceptance when characters witness Thread phenomena. Rendering failures are Thread phenomena — they are the substrate breaking through the rendered surface.

At Fractured RS: the entire non-practitioner population is witnessing persistent, unexplained rendering anomalies. This should systematically drive Certainty Track decline across the population — which feeds CI dynamics (CI advances with Certainty stability; rapid Certainty decline could destabilize the Church's institutional grip).

**[EMERGENT+]** At Fractured RS, Certainty Track acceleration should be a mechanical event: "At Accounting when RS is in Fractured band: all NPCs in affected territories make Certainty checks (TN 7 Ob 1). Failure: Certainty −1." This creates a cascade: RS degradation → population Certainty collapse → CI pressure changes → faction political dynamics shift. This is a rich emergent consequence that connects the worldtrack to the social layer.

---

# 3. DISSOLUTION OF A FORTIFICATION (FIELD/STRUCTURAL SCALE)

## 3.1 Can You Dissolve S-006 Lowenskyst Fortress? [EXPLOIT — SEVERE]

Settlement spec §5.1: "A Fortress settlement in the invader's path forces engagement — it cannot be bypassed unless the invader's Military exceeds the Fortress Defense by 3+. Lowenskyst Fortress (S-006, Defense 4) requires Military 7+ to bypass."

An attacker with a TS 70+ practitioner could attempt to Dissolve the fortress's physical configuration:
- Target: the physical fortification structure (stone, gates, walls — a "firmly actualized" territorial configuration).
- Three-axis Ob: Depth 5 (Field — a coherent local area: the fortress compound) + Breadth 2 (Formation — fortress infrastructure as a collective) + Distance 1 (Near — attacker outside walls, 10-100m) = **Ob 8, TN 8** (Restricted Operation).

At TS 70, Spirit 5, History +8D, TPS 7: pool = (5×2)+11+7 = 28D, TN 8. E[net] = 28×0.3 = 8.4. P(≥8) ≈ 50%.

On Success: the fortress dissolves. RS −5 (Dissolution Success). Gap forms, lasts one scene, closes. Defense 4 → 0? The fortification's intelligible face is torn away.

**On Failure:** RS −8 (Dissolution Failure). Full Gap tears open. Monstrous Incursion immediately. Practitioner Incapacitated. From RS 60 start at game beginning: Dissolution Failure at a fortress = −8 RS. If already at RS <8 + 8 = RS 0 → Rupture.

**This is the most devastating possible Thread operation on the military layer.** A single failed fortress Dissolution can end the campaign. A single successful fortress Dissolution eliminates one of the key chokepoints in the military design. Field-scale Dissolution of a fortification bypasses the entire siege mechanic.

**Required ruling:** Dissolution targeting physical fortification structures: the fortification's actualization is not its physical substance but its defensive function — the configured relationship between stone, garrison, and tactical position. This is Relational (the fortification's function within the military network), not Field (the physical compound). Reclassifying fortress Dissolution as Relational-scale: Ob = 3+2+1 = 6, TN 8. Still achievable at expert-tier but without the Field-scale Gap risk on Failure (Relational Dissolution Failure = RS −5 per... wait, Dissolution Failure always produces "Full Gap tears open. Rendering Stability −8. Monstrous Incursion immediately." Regardless of scale). The Failure risk is the designed check. The question is whether Field-scale Dissolution is the correct classification.

**[GAP — CRITICAL]** Settlement spec never addresses whether physical fortifications are Thread-targetable configurations. This must be ruled before the siege/military layer is finalized. If fortifications ARE Thread-targetable, Dissolution is the nuclear option for bypassing the military layer. If they are NOT (fortifications are physical objects rendered in substrate, not Thread configurations), this exploit is closed.

## 3.2 Mass Battle RS ×3 Multiplier on Fortress Assault [OK — surfaces severity]

If the fortress assault occurs as a mass battle (assault roll: Military vs Defense + garrison), and practitioners are performing Thread operations during it:

Dissolution Success RS cost (−5) ×3 (mass battle multiplier) = **−15 RS in one battle turn**. From RS 60: this is 25% of total campaign RS budget in a single fortification assault.

Dissolution Failure in mass battle: RS −8 ×3 = **−24 RS**. PP-204: "GM mandatory disclosure before any mass battle Dissolution declaration when RS<24. Dissolution Failure = −24 RS = Rupture if RS<24." At any RS below 24 + 24 = 48, a Dissolution Failure during a fortress assault = Rupture. A Dissolution attempt in a fortification assault at RS < 48 is a campaign-ending gamble.

**This should be a mandatory GM disclosure point:** Before any fortress assault involving practitioners with Dissolution capability, disclose the RS threshold. This is already partially covered by PP-204 but needs explicit application to settlement-layer fortress assaults.

---

# 4. COMPANION AS THREAD ANCHOR — INTENTIONALITY CONFLICT

## 4.1 Higher-TS Companion Becomes Anchor [GAP — STRUCTURAL]

Threadwork §2.5: "Anchor: Highest Thread Sensitivity practitioner. Sets the primary intentionality."

If a companion has TS 70 and the player has TS 50, the companion IS the Anchor in any collective operation. The Anchor "sets the primary intentionality" and "rolls their full operation pool."

Companion spec §4.2: "Companion fights using their own stats per combat_v30. They follow the player's tactical lead but may deviate if the combat conflicts with their Conviction."

**Contradiction:** In a collective Thread operation where the companion is the Anchor, the companion sets the primary intentionality — the companion leads the operation, not the player. The "player's tactical lead" rule is inverted for Thread operations where the companion outranks the player in TS.

**Specific problem scenarios:**
- Player wants to Weave a configuration. Companion (Anchor) has Conviction that opposes the Weaving (e.g., Equity conviction; Weaving = cohering power for an institution the companion considers unjust). As Anchor, the companion sets intentionality. Can the player override this? 
- Player wants to Dissolve an enemy practitioner. Companion Anchor has Faith conviction. Dissolution is theologically abhorrent. The Anchor refuses to set intentionality toward Dissolution.

**The companion spec gives the player authority over "tactical lead." The Thread mechanics give the Anchor authority over intentionality.** These are contradictory authority structures for high-TS companions.

**Required ruling:** "If the companion has higher TS than the player, the companion may serve as Anchor. However: the player declares the operation type and target. The companion has veto right if the declared operation conflicts with their Conviction — this functions identically to the combat Conviction deviation rule. If the companion vetoes: the collective operation does not form. The player may proceed as sole practitioner at standard pool."

## 4.2 Companion Anchor + Helper Contribution Cap [OK with surfacing]

If the companion is Anchor and the player is Helper: the player contributes floor(Cognition÷2) bonus dice. A player with Cognition 5 contributes +2D to the companion's pool.

The companion is now performing the operation with their own intentionality PLUS the player's cognitive contribution. For a high-TS companion NPC who doesn't always share the player's goals: the player is literally fueling the companion's Thread work. If the companion uses this collective operation for a purpose that the player disagrees with — can the player withdraw their Helper dice mid-roll?

**[GAP]** No rule exists for a Helper withdrawing consent mid-roll. The collective Leap procedure says "if a helper's contact drops... remove their contributed dice." Contact dropping is involuntary (Wound disruption, incapacitation). Voluntary withdrawal mid-Leap? PP-632 defines Opposing Beliefs: "If a helper's Belief directly opposes the operation's declared goal, the helper must pass a pre-Leap Belief check." The check is pre-Leap, not during. Once the Leap succeeds and the lattice forms, the helper cannot disagree mid-operation.

Ruling needed: Helper contribution is locked at Leap success. Withdrawal after Leap = lattice fracture (pool drops below half Anchor's solo pool → +1 Ob). This prevents mid-operation sabotage while keeping the rule clean.

---

# 5. COMPANION FIRST LEAP DURING TRAVEL

## 5.1 Near-Stirring Companion + Extended Journey [EMERGENT+]

A companion with TS 28 (near Stirring) traveling with the player across provinces. Fieldwork travel through Thread-active territories (RS Fragile or lower, Thread history in territories): Dissonance checks fire, Discovery Events trigger.

The First Leap Event is defined as a scene. A companion's First Leap fires as a Priority 0 Mandatory Scene Slate entry (companion spec §5.3: "arc branch trigger fires while traveling... IS a Priority 0 mandatory Scene Slate entry"). 

**The First Leap of a traveling companion occurs in the field — not at a settlement, not with institutional support, but mid-journey.** The companion's First Leap fires in whatever territory they're crossing. Co-movement fires at that location. The actual d6 effect produces a physical consequence in the field. A sensory anomaly (d6=4) in an open landscape is low-consequence. A nearby structural effect (d6=6) during a mountain pass crossing could be narratively dramatic.

More importantly: the companion's First Leap requires the Approach Training tag (the companion must have been training, consciously or not). If the companion has TS 28 but NO Approach Training tag, the auto-fail rule applies (PP-281): Leap auto-fails, Certainty −1, −1D Thread Pool Score for the scene. The companion's first attempt at the Leap, if untrained, is traumatic and fails.

**[EMERGENT+]** Companion First Leap during travel is a mandatory, location-variable, high-drama scene that the player witnesses directly. The companion's training status (Approach Training tag) determines whether this is a breakthrough or a crisis. The companion spec should note: "Companions who reach TS 30 during travel will fire their First Leap Event in the field. If the companion lacks Approach Training, the First Leap auto-fails with additional Certainty cost. The player may use a scene before the First Leap fires to help the companion prepare (treating it as an Approach Training scene — per fieldwork §5.2 Connect action, Ob 2)."

---

# 6. W-33 COMPANION RALLY + SATURATION COUNTER

## 6.1 W-33 in Same Battle Turn as Player Thread Op [OK — interaction surfaces]

W-33 note (threadwork_v30): "W-33 is effective only for units with CP ≥ 3. A rallied unit with CP ≤ 2 will have an effective combat pool of 0 despite Cohesion restoration."

W-33 is a mass battle Weaving operation performed on a broken unit's Cohesion (Relational scale — the bonds of military discipline within the unit). It counts as a Thread operation for Saturation Counter purposes.

Player performs W-33 (rally their own unit) in Phase 4. Companion performs a Pull (disrupting enemy Discipline) also in Phase 4. Two Thread operations in the same battle turn. Counter is now at 2. One more Thread op (from any practitioner, NPC ally, or NPC enemy) this turn: Saturation Counter fires → +1 Ob, +1 Coherence cost on all subsequent ops.

**Specific interaction:** The companion's Pull was declared at Phase 1 (per combat timing rules). The Saturation Counter fires after the 3rd op. The companion's Pull and the player's W-33 both happen at Phase 4. If an NPC enemy practitioner also fires a Thread op at Phase 4: the third op triggers Saturation mid-Phase 4 execution. The +1 Ob applies retroactively to operations after the trigger, not before. 

**[OK]** The Saturation Counter interaction with W-33 is clean. W-33 counts as a Thread op. The tactical implication: a companion using W-33 in the same turn the player is performing other Thread ops accelerates Saturation. The player must decide: is the unit rally worth triggering Saturation? Often yes for Power 3+ units (per W-33 note), but the Saturation penalty (+1 Ob to all subsequent ops this turn + +2 Ob cumulative across turns if Counter ≥ 3) degrades the entire Thread operation ecology for the battle. Worth surfacing explicitly.

---

# 7. PAST-ORIENTED PULL ON AN OBLIGATION + LOCK ON AN OBLIGATION

## 7.1 POP on an Obligation (Temporal Erasure of Social Contract) [EXPLOIT — MAJOR]

An obligation is a relational configuration actualized by historical commitment (a promise, a contract, a sworn fealty). POP targets past configurations. A practitioner can perform a POP targeting the historical moment when the obligation was established:

- "1–2 seasons" recency: Ob 4 (POP recency table), TN 8.
- "3–5 seasons": Ob 5, TN 8.
- Result (Success): the past event is pulled open — the obligation is displaced. Temporal Disjunction fires: memories of the obligation persist (both parties remember making it), but the configuration's actualization is opened. The obligation no longer has Thread force — it is an open configuration.

**What does "opened" obligation mean politically?** If an NPC pledged fealty to Crown 2 seasons ago, and a RM practitioner POPs that moment of fealty: the memories persist (the NPC remembers pledging) but the Thread configuration of the pledge is now loose-actualised. The NPC's Conviction framework may now allow them to break the pledge without the full Disposition penalty — because the relational substrate has been displaced.

**This is temporal contract erasure.** No social contest required. No political maneuvering. One Thread operation and an obligation's binding force is undermined. The memories remain (the NPC knows they pledged) but the Thread-substrate that makes pledges real is disrupted.

**Coherence cost:** POP = Coherence −1 additional on top of standard. Total: Relational POP = Coherence −1 (scale) + −1 (POP surcharge) = −2. RS cost: minimum −3 (POP Success). Not trivial, but achievable. The exploit: disrupting long-standing political arrangements via POP requires only TS 30+ (POP Ob allows TS 30+ for same-scene/session targets; 1-2 season targets presumably also TS 30+, though the minimum TS for POP isn't explicitly stated in params_threadwork — it only says TS 30+ for standard Pulling).

**[GAP — CRITICAL]** Minimum Thread Sensitivity for POP is not explicitly stated in params_threadwork. The standard Pull minimum is TS 30+. POP at "same scene/session" presumably requires TS 30+. But POP at "10+ seasons / generational" depth — surely this requires higher TS? The three-axis Ob system doesn't add Distance Ob for temporal depth. POP recency is handled by the Ob table (Ob 3–7), not TS minimum. A TS 30 practitioner with Spirit 3, TPS 3, History +4D = 16D, TN 8. At Ob 7 (10+ seasons): E[net] = 16×0.3 = 4.8. P(≥7) ≈ 16%. Possible but low. At Ob 4 (1–2 seasons): P(≥4) ≈ 75%. A TS 30 practitioner can reliably POP recent obligations.

**Required ruling:** POP minimum Thread Sensitivity should scale with recency: TS 30+ for same-scene through 2-season. TS 50+ for 3–10 seasons. TS 70+ for 10+/generational. This is currently unspecified and creates a gap where the cheapest TS threshold (30) can POP any obligation within 2 seasons.

## 7.2 Lock on an Obligation (Frozen Mid-Execution) [EMERGENT+]

An obligation has states: unfulfilled, in-progress, fulfilled, broken. A Lock targets what something "is" and prevents it from "becoming." Applying a Lock to an obligation in-progress:

- Target: the obligation's current state (partially executed fealty, ongoing debt repayment, current diplomatic agreement).
- Effect: the obligation cannot become anything else. It cannot be fulfilled (fulfillment = transition to fulfilled state). It cannot be broken (breaking = transition to broken state). It is frozen in its current partially-executed state indefinitely.
- Ob: Relational Lock (ongoing relational configuration, in active execution) = Depth 3 + Breadth 0-1 + Distance 0 = Ob 3-4, TN 8. Achievable at TS 50+.

**Political application:** Lock an ongoing peace treaty at its current terms. The treaty cannot be fulfilled (reaching the end terms would change the treaty's state) and cannot be broken (the parties cannot transition to hostility while the Lock holds). The peace persists indefinitely — the parties are locked into their current treaty state. This is the most elegant non-violent application of Lock in the political layer.

**Chronic consequences:** Relational Lock drift after season 2: RS −1/season. After season 4: RS −2/season. After permanent Lock: RS drift ceases but +1 Ob adjacent. A practitioner who Locks a permanent peace treaty is spending 1–2 RS/season to prevent war indefinitely. At some RS drain per season, this is a genuine strategic choice: pay RS to maintain peace, or allow the Lock to lapse and risk war.

**[EMERGENT+]** This is excellent design that surfaces naturally from the Lock mechanic. Should be explicitly noted as a political application in the threadwork or settlement layer documentation.

---

# 8. ALTONIAN THREAD PRACTITIONERS — RS AS SHARED VULNERABILITY

## 8.1 Foreign Practitioner RS Drain [CONFLICT — DESIGN ASSUMPTION VIOLATED]

The Rendering Stability track is described as a "shared track" — it represents the peninsula's substrate health, not any faction's health. RS is shared loss at 0 (The Rupture).

The IP recalibration assumes Altonian military pressure at IP ~80 in a 30-year game. If Altonians have Thread practitioners, their operations on the peninsula also drain peninsula RS. The RS track doesn't distinguish between Valorian practitioner Thread ops and Altonian practitioner Thread ops — both drain the same shared substrate.

**Implied design assumption:** The current RS tables calibrate Thread drain from Valorian practitioner activity. But if Altonians are conducting military operations with Thread-capable practitioners, they are simultaneously degrading the peninsula's substrate. An Altonian Dissolution of a Valorian fortification (see §3 above): −5 RS on Success, ×3 in mass battle = −15 RS per successful Dissolution. An Altonian campaign with 2 practitioners performing Dissolution once each per major battle: −30 RS over 5 battles. This is catastrophic — more than 50% of total RS budget.

**[CONFLICT]** The design documents describe Altonian military pressure purely in terms of IP (military metric), not in terms of Thread pressure (RS metric). If Altonians have practitioners, the RS budget for a 30-year game is dramatically under-estimated. 

**Required design decision:** Do Altonians have Thread practitioners? If yes: their RS contribution must be factored into the IP/RS calibration. If no: this needs a canon justification (Altonian theological prohibition? Geographic Thread isolation?). Current documents are silent on this.

## 8.2 Schoenland as Thread-Neutral Strategic Asset [EMERGENT+]

S-035/036 Schoenland: Island territory. T16. If Schoenland falls (Altonian use of Schoenland harbor), does the naval supply chain generate siege-equivalent RS drain?

Siege RS drain fires for "concentrated suffering" (the design note in threadwork_v30). A blockade or prolonged naval standoff isn't quite a siege, but if Schoenland is a permanent Altonian staging ground for invasion — sustained military presence causing suffering — the RS drain is plausible.

More importantly: Schoenland's geographic position (island) means all Thread operations there are at Distance Ob 3 (Far — 1km+) from peninsula practitioners, unless they travel to Schoenland itself. An Altonian practitioner based at Schoenland performing operations targeting peninsula configurations: +3 Distance Ob. The distance makes Thread-attack from Schoenland less effective. Peninsula practitioners retaliating against Schoenland Thread practitioners: same +3 Ob.

**Schoenland may function as a Thread-neutral zone by geographic distance.** Operations from Schoenland toward the peninsula are harder (Distance +3). This is a mechanical argument for Schoenland's strategic value beyond naval positioning.

---

# 9. N-WAY OPPOSING OPERATIONS IN PARLIAMENT

## 9.1 Parliamentary Thread Catastrophe [EXPLOIT — CATASTROPHIC]

Parliament is the setting for Grand Contests (5 exchanges). Named practitioners from multiple factions are present: potentially Warden representatives, RM-affiliated characters, Church-trained Inquisitors with TS, and player character.

If 3+ practitioners with genuinely opposing intentionalities all target the same configuration (the Parliament's political consensus, or a specific treaty proposal as a relational configuration) simultaneously:

Threadwork §2.6 N-Way Opposing Operations: "Three or more practitioners with at least two genuinely opposing intentionalities on the same configuration: automatic lattice collapse. All operations fail. Gap forms at target's scale. Rendering Stability −(2 × number of opposing practitioners). All: Coherence per §3.2; knot strain +2 Ob, 4 Composure."

- 3 opposing practitioners on Relational target: Gap forms at Relational scale. RS −6. All practitioners: Coherence −1 (Relational scale) + Knot strain.
- 4 opposing practitioners: RS −8. Gap at Relational scale.
- 5 opposing practitioners: RS −10. 

**Parliament with 5 factional practitioner representatives all Weaving/Pulling the treaty simultaneously = RS −10, Relational Gap forms in Parliament chamber, Monstrous Incursion risk at Fractured RS.**

The Parliament is the central political institution. A Gap forming in Parliament mid-session is a catastrophic political and metaphysical event. This can occur entirely by accident — each practitioner independently deciding to Thread-intervene in the treaty, unaware others are doing the same. N-way collision is automatic catastrophe.

**[EXPLOIT — but also intended?]** This may be intentional design — Thread warfare in political settings is inherently catastrophic, which deters practitioners from openly using Thread in Parliament. But it needs to be surfaced explicitly. Currently, no document warns practitioners that multi-party Thread intervention in shared configurations is the highest-risk possible action. 

**Required design note:** In Parliament and similar multi-practitioner political settings, independent Thread intervention by 3+ practitioners constitutes N-way Opposing Operations risk. Practitioners contemplating Thread intervention in political settings should first Diagnose whether other practitioners are also in contact.

---

# 10. SCALE HIERARCHY RULE + SETTLEMENT MENDING FUTILITY

## 10.1 Structural Disruption Blocking Settlement-Level Mending [EMERGENT+ — design depth]

Params_threadwork: "Scale hierarchy rule: Mending at scale X cannot hold while a disruption at scale X+1+ persists in the same area. Must work from deepest disruption upward."

Applied to the settlement layer: if there is a Structural-scale disruption in a province (a major institutional Dissolution — the Crown's sovereignty configuration dissolved, a provincial faction's structural Thread configuration broken open), all settlement-level Mending operations (Relational or Field scale) within that province cannot hold. They resolve mechanically but their effects fade because the deeper disruption overwhelms substrate self-repair capacity.

**Practical scenario:** RM performs Structural-scale Dissolution of the Church's institutional grip on T9 Himmelenger (TS 70+, RS −5, Structural Gap forms). Wardens then attempt to Mend settlement-level Gaps in S-023 Himmelenger Cathedral (Relational scale): Mending at Relational scale. The Structural Gap in the province means this Mending "cannot hold." The RS restoration still applies (the mechanical action fires), but the Mending's closure of the Relational Gap is temporary — it re-opens within 1d3 scenes (as per paradox window logic, or as GM discretion).

**[EMERGENT+]** This creates a strategic sequencing imperative: factions that engage in Structural Thread warfare force the entire province into Thread maintenance crisis. Settlement governance stabilization through Mending is futile until Structural disruptions are addressed. This elevates the stakes of Structural-scale Thread operations beyond their immediate RS cost — they invalidate all lower-scale Thread repair work in the affected area.

**This rule must be explicitly cross-referenced in the settlement layer.** Currently, the settlement spec has no mention of the scale hierarchy rule. A settlement governor trying to Mend local Thread damage in a war-torn province may be wasting operations without knowing why their Mending isn't holding.

---

# 11. RS CRITICAL + WORLDWIDE OB COMPOUNDING WITH COHERENCE-DEPLETED PRACTITIONERS

## 11.1 The Double Ob Trap [EMERGENT — DESIGN VALIDATION]

RS Critical (19–1): "+1 Ob worldwide to all Thread operations (the substrate resists manipulation)." Coherence 4–3 (Fragmented): "+1 Ob to all Thread operations including the Leap roll." Coherence 1 (Severed): "+2 Ob to all Thread operations including the Leap."

**Compound scenario:** RS 15 (Critical), practitioner Coherence 4 (Fragmented). All Thread operations: +1 Ob (RS Critical) + +1 Ob (Fragmented) = **+2 Ob worldwide.** A Relational Weave at Ob 5 (three-axis) is now effectively Ob 7. A Foundational Mending at Ob 12 is now Ob 14 (approaching the Ob 20 cap).

At RS Critical + Coherence Severed: +1 Ob (RS) + +2 Ob (Severed) = +3 Ob. Foundational Mending: Ob 15. 22D TN7 Ob 15: E[net] = 6.6. P(≥15) ≈ 1.5%. Effectively impossible.

**The endgame trap is tighter than the RS-alone analysis suggests.** When RS reaches Critical, practitioner Coherence has also been depleted by the campaign of Thread work that caused RS to degrade. The RS Critical endgame assumes practitioners can still perform high-Ob Mending operations — but those same practitioners have been operating for 30 game-years and are likely in Fragmented or Fractured Coherence. The compound Ob penalty makes Mending the Rupture nearly impossible.

**This is correct design.** The Einhir Catastrophe was not reversed because it could not be reversed. The endgame trap closes mechanically as well as narratively. But it should be stated explicitly in the endgame design note (threadwork_v30 §5.3): "At RS Critical, practitioner Coherence state compounds the worldwide Ob penalty. A campaign that has been Thread-active will likely have practitioners in Fragmented (4–3) or worse Coherence — adding +1 to +2 Ob on top of the RS Critical penalty. Mending at this stage requires either: (a) practitioners who have been held in reserve (non-practice for Coherence recovery) specifically for the endgame crisis, or (b) collective operations that pool multiple practitioners' depleted pools."

---

# 12. DISSOLUTION OF AN ADJUDICATOR — NUCLEAR OPTION IN SOCIAL CONTEST

## 12.1 Personal-Scale Dissolution of an Expert Judge [EXPLOIT — DARK]

Social contest §2: "Expert judge — A single authority evaluates arguments on merits." If the expert judge is a single NPC and a practitioner Dissolves them mid-contest:

- Personal-scale Dissolution: Ob (Depth 2 + Breadth 0 + Distance 0) = **Ob 2, TN 8** (Restricted Operation).
- R-55 correction: "For Dissolution targeting a living being at Personal scale: Ob = target's Endurance + target's Spirit + armour modifier." A typical NPC judge: End 3, Spirit 2, no armour = **Ob 5, TN 8**.

At TS 50+, pool 17D TN8: E[net] = 5.1. P(≥5) ≈ 50%. At TS 70+, pool 24D TN8: P(≥5) ≈ 90%.

On Success: the judge dissolves. RS −5. Gap forms. The contest... has no adjudicator.

**The social contest system has no rule for adjudicator dissolution mid-contest.** The contest ends by default? The Piety Track result is voided? The political/legal outcome is null? The murder of a judge mid-Parliament session is both a Thread catastrophe (RS −5, Gap) and a political catastrophe (CI +1 from Church observer investigation, faction Disposition collapse, legal crisis).

**[EXPLOIT — but self-punishing]** Dissolving an adjudicator eliminates the contest mechanism but at enormous cost: RS −5, political fallout, Coherence −1, Knot strain with any Close Knot who witnesses it. This is not a clean win — it's the practitioner destroying the political institution they're operating within. The contest system doesn't need a specific counter-rule; the systemic costs are the counter. But it needs an explicit ruling that dissolving the adjudicator voids the contest (treating it as "no adjudicator reached decision"), not a win for the dissolving party.

---

# 13. THREADCUT BEING AS SETTLEMENT GOVERNOR

## 13.1 Rendering Strain from Governing a Settlement [EMERGENT+ — worldbuilding]

A threadcut being serving as settlement governor is present in the settlement daily. Their beyond-ceiling rendering forces non-sensitive residents (TS 0) to render the threadcut being above their ceiling capacity.

Threadwork §6.2: "Each scene of beyond-ceiling rendering: +1 Rendering Strain (cumulative)." For a threadcut being in a town of ~500 TS 0 residents: every scene in the settlement adds Rendering Strain. If the threadcut being governs long-term (seasons), Rendering Strain accumulates.

A settlement "scene" occurs multiple times per season (governance actions, events, NPC encounters). Even at 1 scene-equivalent per week: 12 scenes per season (3 months/season). Each scene: +1 Rendering Strain. After one season: Rendering Strain +12. Health of a typical threadcut being: ~14–20. A threadcut being who governs a settled population for **one season** reaches De-Actualisation threshold.

**This makes permanent threadcut being settlement governance mechanically impossible.** A threadcut being can visit settlements (brief exposure = few scenes = manageable strain) but cannot reside as governor without De-actualising within one season.

**[EMERGENT+]** This is canon-consistent and philosophically appropriate — threadcut beings are mobile, transient, or remote for a reason. Their presence in densely-populated settlements is inherently self-destructive. A threadcut being can govern from the margins (the outpost, the wilderness, the border) but not from a Seat or City settlement. This should be noted as a constraint in both the settlement spec and the companion spec (if a threadcut being companion is asked to serve as governor).

---

# 14. FORGETTING EXPOSURE ON COMPANION CONVICTION ARCHITECTURE

## 14.1 Failed Forgetting Check — Conviction Without Emotional Core [GAP — CRITICAL]

Forgetting boundary (Southernmost): "Successful Forgetting Check: retains facts as intellectual knowledge, but emotional conviction is lost." Failed Forgetting Check: the specific content is more thoroughly stripped (worse than partial retention).

Companion spec §4.3: "Companion commentary reflects their Conviction and Resonant Style." Companion departure conditions include: "Companion's active Conviction is violated by the player's actions 3 times."

**A companion who undergoes a Failed Forgetting Check has their Conviction stripped of emotional foundation.** The companion still knows what their Conviction is (intellectual knowledge) but the emotional anchoring that makes it a genuine Conviction — the reason they care — is gone. A Faith companion who experiences Forgetting failure retains the doctrinal content of Faith but loses the emotional reality of belief. They can recite Faith's claims but they don't feel them.

**What does this do to Conviction violation tracking?** If the companion's Conviction is emotionally hollow after Forgetting: does the 3-strike departure mechanism still fire? They're still technically holding the Conviction (intellectually). But the Resonant Style vulnerability (Evidence attacks work because "the framework strains" against contradiction) becomes inoperative — a framework without emotional investment cannot strain.

**[GAP — CRITICAL]** No ruling exists for companion Conviction state after Forgetting exposure. Required: "A companion who fails a Forgetting Check retains their Conviction taxonomy but loses emotional investment in it. For departure tracking: Conviction violations still accumulate, but at halved rate (the companion registers violations intellectually without the emotional force that drives departure). Resonant Style attacks by the player on this companion's Conviction are ineffective until emotional recovery (one season of non-Southernmost engagement restoring the experiential dimension)."

## 14.2 Recall Anchor Mechanic Applied to Companions [OK — surfaces elegant interaction]

PP-253: "A practitioner who passes their Forgetting boundary Leap may act as a Recall Anchor for one other practitioner who failed or partially failed. Anchor elevates failing practitioner to fact-retention."

Companion spec §4.1: "If companion TS ≥ 30, they may participate in collective Thread operations." A companion with TS 30+ attempting the Forgetting boundary Leap who fails: the player can Anchor them. Player as Recall Anchor for their companion means: the companion retains facts (as if Success) — emotional conviction still lost.

**The player-companion Knot enhances this:** PP-632: Knot-sharing reduces social action Ob by 1. If the Anchoring counts as a connected action through the Knot, the Anchor mechanic may be more reliable with a Knotted companion. But PP-253 says "one Anchor per failed practitioner; Anchor cannot anchor more than one other." If the player has two practitioner companions both failing the Forgetting check, the player can only Anchor one. They must choose which companion to protect. This is genuinely agonizing and thematically appropriate.

---

# 15. GENERATIONAL SHIFT — ATTRIBUTE DECAY ON SOCIAL CONTEST POOLS

## 15.1 Faction Leader Argue Pool at Year 20–30 [EMERGENT — DESIGN VERIFICATION]

Generational Shift Threshold 4 (Year 20): original leaders −2 to highest attribute.
Threshold 6 (Year 30): −3 to highest attribute.

Social contest Argue pool = (Primary Attribute × 2) + History. Primary attribute is Cognition (Expert judge), Charisma (Crowd), or Attunement (No adjudicator).

**Himlensendt (Confessor, Church):** Cognition is presumably his highest or near-highest attribute (theological reasoning, doctrinal argument). If Cognition starts at 5: Cognition −2 at Year 20 = 3. Argue pool at Expert judge: (3×2) + History = 9D (pre-History). Thread Sensitivity 0 — no Thread option. By Year 30: Cognition 2, Argue pool = 7D. A Character who starts as Valoria's most formidable theologian is reduced to a mediocre debater by age.

**Baralta (Hafenmark):** If her primary contested attribute is Attunement (negotiator, Categorical Imperative ethics): Attunement −2 at Year 20 reduces her core negotiation capability. The faction leader the player has spent 20 years building relationships with is now mechanically weaker at the game's critical political moment.

**[EMERGENT+]** This creates a natural political urgency: the founding generation's window of peak competency closes around Year 10–15. Beyond that, they're declining while the player's Standing and Renown (if built consistently) reaches its peak. Year 20 is the crossing point: old-generation NPCs decline, player-era characters ascend. This is perfect. But it should be stated explicitly in the Generational Shift clock spec.

## 15.2 Coherence-Depleted NPC Leaders + Argue Pool Penalty [COMPOUNDING — EMERGENT]

A practitioner NPC faction leader at Year 20 with Coherence 4 (Fragmented): −1D all social rolls + Generational Shift −2 to highest attribute.

Compound effect: Argue pool = (Attribute×2 − 2 from Generational Shift) + History − 1D (Fragmented). A Cognition 5 leader becomes: (3×2) + History − 1D = 8D − 1D = 7D effective. Plus +1 Ob to all Thread ops (if they're a practitioner), making their Thread-political capabilities doubly degraded.

**By Year 20, practitioner NPC faction leaders who have been Thread-active are receiving penalties from both aging (attribute decay) and Thread use (Coherence degradation) simultaneously.** The double degradation makes mid-to-late game NPC practitioners far weaker than their starting sheet implies. This compounds the player's relative power growth — as the player's character advances Standing and Renown, the NPCs around them are declining from age and Thread cost. The dynamic of political succession becomes emergent from mechanics, not scripted.

---

# 16. KNOT FORMATION DURING THREAD CONTACT

## 16.1 Can a Contact Window Be Used for Connect (Knot Formation)? [GAP]

Thread contact: the practitioner's rendering is suspended. They are in the originary state — perceiving configurations without rendered mediation. Contact rounds are available for Thread operations (Weaving, Pulling, Mending, Locking, Dissolution).

Connect (fieldwork action for Knot formation): uses Bonds pool, not Spirit pool. It is not defined as a Thread operation. The practitioner during contact has access to Thread perception at depths unavailable in rendering. Can they use this perception to accelerate Knot formation — to perceive the Mitsein bond more directly and Connect from within the contact window?

**Arguments for yes:** (a) Thread contact reveals relational configurations directly — the practitioner perceives the Knot-bond at Thread-depth, which should make Connect more resonant. (b) The First Leap Event specifically fires "a wave of recognition" — the practitioner perceives the world's relational structure. Knot formation at that moment seems almost inevitable.

**Arguments for no:** (a) Connect is a fieldwork action with its own action economy. Using a contact round for Connect would consume an operation slot. (b) Contact window is for Thread operations, not social fieldwork actions. The suspension of rendering is for Thread perception, not social connection.

**[GAP]** No ruling exists. Proposed: a practitioner may use one contact round for a Connect action targeting a character present in the scene, treating the Connect as a Thread-assisted social action. Pool: Bonds (as normal), but the practitioner's Thread perception depth allows them to perceive the bond configuration directly — Connect Ob reduced by 1 (minimum 1). This uses the contact round (one less operation available) and costs the same Coherence as if a Relational operation had fired (Coherence −1, since the practitioner is using their contact depth for relational engagement). The Connect does not count as a Thread operation for Saturation Counter purposes.

---

# SUMMARY TABLE — BATCH 2

| Item | Finding | Severity | Action Required |
|------|---------|----------|----------------|
| SETT-01/02 | Province Accord manipulation via single-settlement Weave + Accounting timing | **[EXPLOIT — MAJOR]** | Rule: Accord derivation computed at Accounting only, not real-time |
| SETT-01/02 | Single-settlement provinces have 1:1 Thread→Accord leverage (no averaging buffer) | **[GAP]** | Design note: single-settlement provinces structurally more Thread-vulnerable |
| RS Fractured | NPC inconsistent memory under Fractured RS not connected to social contest pools | **[EMERGENT+]** | Add: Recall check Ob 1 before Memory-genre Argue in Fractured RS territories |
| RS Fractured | Fractured RS + Certainty Track acceleration undefined | **[EMERGENT+]** | Add Accounting event: NPCs in Fractured-RS territories make Certainty check Ob 1 |
| Fortress Dissolution | Field-scale Dissolution of fortification = military layer bypassed | **[EXPLOIT — SEVERE]** | Ruling needed: is fortification physical structure a Thread configuration? Reclassify as Relational if yes |
| Fortress Dissolution | Mass battle ×3 multiplier: Dissolution Failure at RS < 48 = Rupture | **[OK — surface]** | Extend PP-204 mandatory disclosure to settlement-layer fortress assaults |
| Companion | Higher-TS companion as Anchor contradicts "player tactical lead" | **[GAP — STRUCTURAL]** | Rule: player declares op; companion has Conviction veto; veto = no collective op |
| Companion | Helper withdrawal mid-Leap undefined | **[GAP]** | Rule: Helper commitment locked at Leap success; voluntary withdrawal = lattice fracture |
| Companion | Companion First Leap mid-travel fires as mandatory scene wherever they are | **[EMERGENT+]** | Add to companion spec: Approach Training check before First Leap; player can prep companion |
| W-33 | Companion W-33 rally counts toward Saturation Counter in same turn as player Thread op | **[OK — surface]** | Add tactical note: companion W-33 timing relative to player ops is real decision |
| Obligations | POP on obligation = temporal erasure of social contract | **[EXPLOIT — MAJOR]** | Ruling: POP minimum TS should scale with recency (TS 30+/2 seasons; TS 50+/10 seasons; TS 70+/generational) |
| Obligations | Lock on obligation = frozen mid-execution indefinitely | **[EMERGENT+]** | Surface as political application in design notes |
| Altonians | If Altonian practitioners exist, their ops drain the shared RS track | **[CONFLICT — DESIGN ASSUMPTION]** | Design decision: do Altonians have practitioners? If yes, recalibrate RS budget |
| Parliament | 3+ practitioners with opposing intentionalities = automatic catastrophic Gap | **[EXPLOIT — CATASTROPHIC]** | Surface as explicit design note; add: practitioners should Diagnose before Thread-intervening in political settings |
| Scale hierarchy | Structural disruptions block all lower-scale Mending in same area | **[EMERGENT+]** | Cross-reference scale hierarchy rule in settlement spec explicitly |
| RS Critical | Worldwide +1 Ob + Fragmented/Fractured practitioner Coherence compounds to +2/+3 Ob | **[EMERGENT — DESIGN VALIDATION]** | Add to RS Critical endgame note: reserve practitioners specifically for endgame Mending |
| Adjudicator | Dissolving an expert judge mid-contest: no ruling on outcome | **[EXPLOIT — self-punishing]** | Rule: adjudicator dissolution voids contest (no-decision outcome), not a win |
| Threadcut being | Governing a populated settlement = De-Actualisation within one season from Rendering Strain | **[EMERGENT+]** | Note constraint: threadcut beings cannot reside as settlement governors; outpost/wilderness only |
| Forgetting | Companion Conviction without emotional core after Forgetting failure — departure tracking undefined | **[GAP — CRITICAL]** | Rule: halved Conviction violation accumulation rate; Resonant Style attacks ineffective until emotional recovery |
| Forgetting | Player as Recall Anchor for Knotted companion; must choose if two companions both fail | **[OK — surfaces]** | Note: Anchor constraint (max 1 per practitioner) creates choice between companions |
| Generational Shift | Attribute decay reduces faction leader Argue pools 30–50% by Year 20–30 | **[EMERGENT+]** | State explicitly: player relative power peak crosses NPC decline ~Year 15–20 |
| Generational Shift | Coherence degradation + Generational Shift attribute decay compounds on NPC practitioners | **[EMERGENT+]** | Note: practitioner NPC leaders doubly penalized vs non-practitioners in late game |
| Knot formation | Connect action during Thread contact undefined | **[GAP]** | Rule proposed: contact round usable for Connect at −1 Ob; costs Coherence −1 as Relational engagement |

---

## NEW CRITICAL ITEMS FROM BATCH 2 (block integration)

1. **Province Accord real-time vs Accounting derivation** — must be ruled before settlement stats can be calibrated. Real-time derivation enables mid-season Thread-manipulation of Accord.

2. **Fortification as Thread configuration** — must be ruled before siege/military mechanics finalize. Dissolution of a fortification at Field scale bypasses siege entirely.

3. **POP minimum Thread Sensitivity scaling** — must be ruled before obligation mechanics or any historical configuration can be designed. TS 30 can POP 2-season-old obligations at 75% success rate; this seems too powerful at minimum TS.

4. **Altonian Thread practitioner status** — must be decided before IP/RS calibration for 30-year games is trustworthy. Unaddressed assumption underneath all RS budgeting.

5. **Companion Conviction post-Forgetting** — must be ruled before Southernmost-adjacent companion design is finalized.

---

*End of document. Session d8b924fb834a398c.*
