[PROVISIONAL: Southernmost faction engagement — faction behaviour/design proposal — pending Jordan editorial approval]

# DESIGN PROPOSAL: Southernmost Faction Engagement Pathways

## Status: PROPOSAL — requires Jordan approval before any canonical status
## Cross-references: params/bg/faction_actions.md, params/bg/clocks.md, params/bg/tracks.md, designs/threadwork/threadwork_v30.md §Mending, designs/world/southernmost_v30.md §6, designs/npcs/npc_character_analyses_v30.md §6 (Baralta), canon/00_philosophical_foundations.md §9 (Perceptual Prophylaxis), canon/03_canonical_timeline.md (Solmund)

---

## 1. THE PROBLEM

Three factions — Church, Crown, and Hafenmark — have no mechanical pathway to engage with the Southernmost. Their Southernmost Awareness (SA) starting values are 0, 0, and 1 respectively. No existing faction action targets T15 Askeheim (Uncontrolled). No existing trigger fires when Rendering Stability changes in southern territories. The expedition procedure (southernmost_v30 §6.3) requires TS 30+ practitioner officers, which none of these three factions possess at game start.

Result: the Southernmost is mechanically accessible only to Varfell (SA 2, environmental TS, southern geography) and the People's Revolution (SA 3, ideological investment). The peninsula's existential threat — RS degradation, Calamity radiation, Locked Zones — is invisible to the three factions with the most institutional power to address it.

This is historically accurate but strategically inert. The game needs a mechanism that brings the Southernmost into these factions' decision space without giving them unearned knowledge.

---

## 2. THE MECHANISM: Mending Visibility Propagation

### 2.1 What Already Exists

Threadwork_v30 §2.3 (Thread Operation Visibility): "Physical effects (a wound closing, an object moving) are visible to all."

Mending co-movement profile (epistemic auto-effect):
- Overwhelming: "Non-sensitives notice a distinct easing of tension."
- Success: "Non-sensitives may notice subtle easing."

Mending Ob table:
- Catastrophic Gap (3+ seasons): Ob 7, TS 70+, requires Einhir framework or collective operation
- Locked Zone border: Ob 8+, TS 70+, requires Einhir framework

Calamity radiation table (params/bg/clocks.md): RS effects graduate by Proximity Rating (node distance from T15). At RS 39-20, Proximity 2 territories experience "+1 Ob Thread; Shifting Objects (1d10: 1)." When RS improves (e.g., from band 39-20 to 59-40), these effects recede.

### 2.2 What Is Missing

No trigger connecting RS improvement to faction awareness. The RS track moves. Nobody notices.

### 2.3 The Proposed Trigger: Rendered-World Change Event (RWCE)

When a Mending operation at Ob 6+ succeeds (any degree), the physical and environmental consequences constitute a Rendered-World Change Event in the Mended territory and all territories at Proximity ≤ 2 from the Mending site.

**RWCE Scale by Mending Ob:**

| Mending Ob | RWCE Radius | Observable Effects |
|---|---|---|
| 6 (Entrenched Gap) | Mended territory only | Local: blight recedes, structures stabilise, water sources clear. Perceptible within the territory. Travellers report changes. |
| 7 (Catastrophic Gap) | Mended territory + Proximity 1 | Regional: adjacent territories perceive easing. Trade routes that were hazardous become passable. Seasonal anomalies (Shifting Objects, unexplained phenomena) cease in affected zone. |
| 8+ (Locked Zone border) | Mended territory + Proximity 2 | Peninsular: effects perceptible across the southern third of the peninsula. Territories that experienced Calamity radiation effects (even at Folklore level) notice the change. The southern landscape is materially, observably different. |

**RWCE does not grant thread knowledge.** It grants awareness that something changed in the south. The cause is unattributable to non-practitioners. The effects are physical: land, water, weather, structural stability, cessation of anomalous phenomena. This is exactly what Solmund's original acts looked like to non-practitioners — inexplicable, beneficial, large-scale environmental transformation.

### 2.4 RWCE → Faction Awareness Pathway

When RWCE fires, each faction with presence in any affected territory receives a SA increment:

| Faction | Presence Condition | SA Increment |
|---|---|---|
| Crown | Controls any territory in RWCE radius | +1 SA |
| Church | Has Parish, Cathedral, or PT ≥ 1 in any territory in RWCE radius | +1 SA |
| Hafenmark | Controls any territory in RWCE radius OR has Trade Route token in RWCE radius | +1 SA |
| Varfell | Automatic (southern geography) | +1 SA |

SA increment triggers awareness, not understanding. The faction knows something changed. What it means depends on the faction's interpretive framework.

---

## 3. BARALTA'S THEOLOGICAL POSITION

### 3.1 Canon Foundation

NPC character analysis §6 (Duchess Inge Baralta):
- Historical anchor: Isabella I of Castile / Henry VIII
- "She does not question the Church's theology. She questions its jurisdiction."
- "She believes the monarch rules by genuine divine right — not the Church's delegated authority"
- "Bounded Church authority under competent secular governance is what Solmund's grace demands"
- "Her faith is the engine of her ambition"
- "Sovereign Authority Doctrine is the legal instrument of this claim"
- "The Restoration introduces a third [source of authority] that delegitimises both"
- "She would suppress the Restoration more aggressively than the Church"

### 3.2 Jordan's Extension (This Session)

Baralta believes in a Protestant model of direct communion — anyone can commune with Solmund without Church mediation. This includes her. Her deeds (political accomplishments, institutional achievements, the Sovereign Authority Doctrine's success) are evidence of divine favour. She was divinely ordained as a superior person.

### 3.3 Reconciliation with Canon

Baralta does not question the Church's *content.* Solmund is real. His acts were divine. The weaving is the structure of reality. She accepts all of this. What she rejects is the Church's *monopoly on mediation.* The Confessor does not stand between Baralta and Solmund. Baralta communes directly. Her deeds are the evidence.

This is simultaneously:
- **Henry VIII** (sovereign authority supersedes Church jurisdiction)
- **Luther's priesthood of all believers** (direct communion without clerical mediation)
- **Prosperity gospel** (success = divine favour)
- **Deed-monarchy theology** (the founding logic of the Almqvist settlement, theologised — the throne goes to whoever's deeds prove worthiest, and worthiness is divinely conferred)

The synthesis is internally consistent. Baralta has built a complete theological framework that justifies her political ambition through genuine faith. She is not cynical. She believes every word.

### 3.4 Relationship to the Perceptual Prophylaxis

Canon §9.1: The Church's theology "directly forecloses the perceptual stance that thread sensitivity requires." Essentialism forecloses holding contingency. Divine determinism forecloses feeling the rendering as process.

Baralta's theology partially cracks the prophylaxis — not intentionally, not knowingly, but structurally:

| Prophylaxis Condition (§9.1) | Church Orthodoxy | Baralta's Theology |
|---|---|---|
| Contingency foreclosed by essentialism | Fixed natures, divine givens | Partially open: deeds determine standing, not birth. Contingency enters through merit. |
| Rendering-as-process foreclosed by determinism | World is exactly as God made it | Partially open: divine communion is ongoing, active, participatory. The world is responsive to those who act. |
| Demand for intelligibility reinforced | Reality is fully intelligible to the divine | Partially open: Baralta accepts that her communion exceeds institutional categories. She does not need the Church to explain what Solmund means to her. |

Baralta does not develop TS. Her theology does not go far enough — she still believes in a fixed divine order (just one where she's at the top). But populations under her influence experience a *weakened* prophylaxis. The theological shift from "only the Church mediates" to "anyone can commune through deeds" is a crack in the cognitive foreclosure. Over generations, territories with Baralta's theology dominant would produce higher base-rate TS than territories with orthodox Church theology.

**This is not speculative.** It follows directly from §9.1: TS development requires "the capacity to let go of the demand for intelligibility, to hold the world's contingency without flinching." Baralta's deed-theology introduces contingency (your standing depends on what you do, not what you are). The contingency is limited (divine right still constrains the framework), but it is more contingent than the Church's absolute essentialism.

### 3.5 Baralta's Relationship to the Restoration Movement

Canon: "She is the Restoration Movement's pure adversary." Einhir cultural revival introduces a source of authority predating Solmund, which delegitimises both sovereign divine right and Church theology.

With the direct communion extension, this opposition *deepens*. Baralta's framework has exactly two legitimate sources: the sovereign (divine right) and Solmund (theological content). The Restoration says there was something before Solmund — an older tradition with its own authority. If that's true, Baralta's divine right is provincial, not universal. She would not just suppress the Restoration — she would need to theologically annihilate it. Pre-Solmund tradition cannot be permitted to exist in her framework, because its existence implies Solmund is not the ultimate origin, which implies divine right from Solmund is not ultimate authority.

---

## 4. FACTION RESPONSE PATHWAYS

When RWCE fires and factions gain SA, each faction's AI processes the event through its existing decision framework.

### 4.1 Church Response

**Starting position:** SA 0, Certainty (institutional) very high, no TS, no practitioner officers.

**Interpretive framework:** The only available explanation for large-scale beneficial environmental transformation is Solmund. Canon: the Church's scriptural tradition was built on non-practitioner witness testimony of Solmund's original acts — inexplicable healing, restoration, stabilisation. An RWCE is structurally identical to what the original witnesses reported. The Church's institutional reflex is recognition: *this is what our scriptures describe.*

**Mechanical response sequence:**

1. **SA increment fires** → Church AI checks: is this consistent with Solmund theology? Answer: yes (beneficial transformation without visible cause = miracle).
2. **Church declares Miracle Investigation.** New action type (proposed):

**Church — Miracle Investigation (proposed)**
Type: Consul Outward (Church only). Prerequisite: SA ≥ 1 AND RWCE has fired in current or previous arc.
Roll: Mandate vs Ob 2.
Effect: Church sends an investigation mission to the territory where RWCE was strongest.

| Degree | Effect |
|---|---|
| Overwhelming | SA +2. Church gains PT +1 in investigated territory (miracle claim = missionary opportunity). Church Mandate +1 (institutional prestige from claiming the miracle). |
| Success | SA +1. Church gains PT +1 in investigated territory. |
| Partial | SA +1. No PT gain. Investigation inconclusive. |
| Failure | SA unchanged. Stability −1 (institutional embarrassment). |

3. **Investigation encounters practitioners.** If the Mending was performed by practitioners (which it was — Mending requires TS 50+), the investigation mission arrives in territory where threadwork is actively occurring. The Church investigators do not have TS. They perceive the EFFECTS (healed land, stabilised structures). They do not perceive the OPERATIONS. They encounter people who know what happened. Those people are either:
   - Restoration Movement practitioners (who will explain it as Einhir heritage)
   - Independent practitioners (who may or may not explain)
   - Varfell-aligned practitioners (who may conceal the mechanism for political reasons)

4. **The Church faces the aporia.** If practitioners explain the mechanism: the Church must decide whether threadwork-as-Mending is heresy or miracle. If the effects are Solmund's work (the Church's claim), and the effects were produced by threadwork (the practitioners' report), then threadwork produced Solmund's work. The Church cannot simultaneously condemn the practice and celebrate the product.

**Decision branch:**
- **Assert (suppress the practitioner account, maintain miracle framing):** CI +1 (institutional authority reinforced). RM relations −1. Risk: practitioners stop Mending, effects cease, miracle claim is undermined.
- **Accommodate (acknowledge practitioner involvement, reframe as divinely inspired):** CI −1 (monopoly weakened). SA +1 (genuine knowledge gained). Theological Dissatisfaction risk from orthodox constituencies.

This is a meaningful faction AI decision with genuine consequences in both directions. Neither choice is safe.

### 4.2 Crown/Baralta Response

**Starting position:** SA 0. Baralta is Hafenmark's faction leader (Duchess of Hafenmark), but her Crown ambitions and Sovereign Authority Doctrine operate across factional boundaries.

**Correction: Baralta is Hafenmark, not Crown.** Her response routes through Hafenmark's action framework but with Baralta's personal theological overlay.

**Interpretive framework:** Baralta interprets through divine right + direct communion. The RWCE is evidence that Solmund's grace is active in the world — and the appropriate secular response is sovereign action, not Church oversight.

**Mechanical response sequence:**

1. **SA increment fires** → Baralta's AI checks: does this support divine right? Answer: yes (divine intervention in the world validates the theological framework that justifies her authority claim).
2. **Baralta invokes Sovereign Authority Doctrine for Southernmost response.** This is a jurisdictional claim: the Crown (or in Baralta's ambition, the Hafenmark-led sovereign authority) has the right to direct the response to Southernmost events. The Church's Miracle Investigation is a competing jurisdictional claim. The two cannot coexist.

**Mechanical interaction with RDT/TD tracks:**

The RDT (Reformed Doctrine Track) already models Hafenmark's theological challenge to the Church. Baralta's Southernmost engagement accelerates RDT advancement:

- If Hafenmark controls a territory where RWCE has fired AND Church has Parish/Cathedral in that territory: RDT advancement condition is met (Hafenmark controls territory where Church has presence + Hafenmark M ≥ 3 + PI ≥ 4).
- RWCE provides the *political ammunition* for RDT advancement: Baralta can argue that the Church's passive theology (wait for Solmund) has been proven inadequate by events that require active sovereign response.

**TD (Theological Dissatisfaction) escalation:** Each RDT advancement at TD ≥ 2 fires when the Church plays Assert in response to the miracle claim. If the Church asserts its interpretive monopoly over the Southernmost events AND Hafenmark has Reformed Doctrine, TD increments. At TD 3, any season the Church loses PI gives Hafenmark PI +1 — meaning the Southernmost conflict directly transfers Church political capital to Hafenmark.

3. **Baralta's resource allocation.** Hafenmark has no Domain Action that reaches T15 Askeheim. But Baralta can:
   - Use Diplomat Card to establish diplomatic presence with practitioners operating in the south
   - Use Trade Network Investment to extend Hafenmark economic reach toward southern territories (T10 Spartfell → T11 Halvardshelm → T12 Sigurdshelm — approaching Varfell-controlled territory near the Southernmost)
   - Build the case for Parliamentary Session to formally authorise Southernmost engagement

4. **The constitutional crisis.** Baralta's divine-right claim for Southernmost authority triggers exactly the procedural emergency Hafenmark's constitutional culture was built to prevent. But Baralta IS Hafenmark's leader. The crisis is internal to the faction:
   - Peder Almstedt (#8) blocks: his conservative AI protects the founding settlement, which did not include sovereign divine right.
   - Gerik Strand (#9) may support: deed-logic says whoever acts most effectively deserves authority. If Baralta's Southernmost response produces results, Strand's meritocratic conviction is activated.
   - The Hafenmark Parliamentary Challenge action is designed to suppress CI. But if Baralta is using Hafenmark's institutional authority to make theological claims, Parliamentary Challenge could fire against Baralta's own programme — internal procedural resistance to her divine-right overreach.

### 4.3 Varfell Response

**Starting position:** SA 2. Southern geography. Environmental TS in population. Maret Uln's presence in the Southernmost. Closest faction to the Mending site.

**Interpretive framework:** Varfell understands threadwork. Vaynard investigates Thread knowledge as cultural heritage recovery. The RWCE is not a miracle. It is evidence that Mending works — that the Einhir approach to the Southernmost was correct, that the Catastrophe can be repaired, and that the Church and Crown have been obstructing the solution for 245 years.

**Mechanical response:** Varfell does not need a new pathway. Varfell is already in the south. RWCE validates Varfell's existing strategic investment. The question is how Varfell responds to Church and Hafenmark arriving in its operational territory.

- **Defensive:** Varfell secures the Mending site militarily. Prevents Church investigation from accessing practitioners. Controls the narrative by controlling physical access.
- **Strategic disclosure:** Varfell allows Church/Hafenmark access, knowing that what they discover will accelerate their internal contradictions. The Church arriving at the Southernmost and finding threadwork practitioners is worse for the Church than for Varfell.
- **Alliance with Restoration:** The People's Revolution (SA 3, highest awareness) has ideological alignment with the Mending programme. Joint Varfell-RM operations secure the south while the northern factions argue about jurisdiction.

### 4.4 Restoration Movement Response

**Starting position:** SA 3 (highest). Ideological investment. Practitioner networks. Elder Solvei Kaldring (#proposed leader) carries cultural authority but not military capability.

**Interpretive framework:** The Mending vindicates everything the Restoration has argued for centuries. Einhir knowledge works. The Catastrophe can be addressed. The Church's doctrine (wait for Solmund, the Wound heals in divine time) was wrong. The Restoration's programme (recover the knowledge, repair the damage, restore what was lost) was right.

**The political trap:** The Restoration cannot claim credit without exposing its practitioners to Church prosecution. The Mending was performed by people the Church would classify as heretics. If the Church declares the effects a miracle, the practitioners face a choice: accept the miracle framing (their work is co-opted, but they are safe) or claim the threadwork origin (their work is recognised, but they are prosecuted). This mirrors the original Solmund pattern — practitioner witness testimony suppressed in favour of miracle narrative.

---

## 5. THE TRIPLE INTERPRETATION AS MECHANICAL ENGINE

The RWCE creates a three-way interpretation conflict that generates factional tension without requiring any faction to be wrong:

| Faction | Interpretation | Implication | Blocks |
|---|---|---|---|
| Church | Miracle — Solmund's grace returning | Church oversight required; practitioners are instruments of divine will | Admitting the mechanism (threadwork) undermines the miracle claim |
| Hafenmark/Baralta | Divine communion — active grace rewards those who act | Sovereign authority directs the response; Church mediation unnecessary | Admitting the mechanism reveals that "direct communion" is actually threadwork, not prayer |
| Restoration/Varfell | Einhir heritage — ancestral knowledge applied | Practitioners are heirs of a pre-Solmund tradition; neither miracle nor communion | Claiming credit exposes practitioners to prosecution |

**Each interpretation is internally consistent.** None requires falsehood. Each requires ignoring one piece of evidence that the others supply.

**The evidence each interpretation must suppress:**

- Church must suppress: the practitioners' account of what they did (threadwork, not miracle)
- Hafenmark/Baralta must suppress: that the practitioners are Einhir-trained, not divinely inspired
- Restoration must suppress: that claiming credit for the work puts practitioners at institutional risk

**Mechanical expression:** The three interpretations compete through existing systems:
- Church uses CI (Church Influence) to enforce the miracle narrative
- Hafenmark uses RDT/TD to advance the reformed doctrine that supports Baralta's divine-right claim
- Varfell/Restoration uses SA (Southernmost Awareness) advancement to build the knowledge base that eventually makes the threadwork explanation undeniable

The competition is not symmetrical. CI and RDT/TD operate on institutional tracks with immediate political consequences. SA operates on a knowledge track with delayed but permanent consequences. In the short term, Church and Hafenmark can dominate the narrative. In the long term, SA advancement makes the truth progressively harder to suppress.

---

## 6. MECHANICAL PROPOSALS

### 6.1 New Trigger: Rendered-World Change Event (RWCE)

**Trigger condition:** Mending operation at Ob ≥ 6 achieves Success or Overwhelming in any territory at Proximity ≤ 2 from T15 Askeheim.

**Effect:** All factions with presence in affected territories (see §2.4) receive SA +1. RWCE is logged on the game timeline. RWCE is a one-time event per Mending — subsequent Mending in the same territory does not fire additional RWCEs unless RS band has shifted.

### 6.2 New Church Action: Miracle Investigation

As specified in §4.1. Consul Outward, Mandate vs Ob 2. SA advancement + PT gain in investigated territory.

### 6.3 New Scenario Trigger: Southernmost Contact Event

**Trigger condition:** Any faction with SA ≥ 2 has military or diplomatic presence in a territory at Proximity ≤ 1 from T15 AND a practitioner NPC is operating in that territory.

**Effect:** The faction's representatives encounter threadwork practitioners. This fires a Decision Event (similar to existing Named Character Event Cards):

**Church:** Assert (suppress practitioner account; CI +1, RM relations −1) or Accommodate (acknowledge practitioner role; CI −1, SA +1).
**Hafenmark:** Claim sovereign authority (RDT +1 if conditions met; constitutional crisis risk with internal NPCs) or Defer to procedural assessment (SA +1, no RDT advancement).
**Crown:** If Crown reaches the south (Crown SA ≥ 2 + military presence), Decision Event: Commission research (SA +2, Certainty −1 for Almud) or Suppress findings (SA unchanged, Stability +1).

### 6.4 Modification: SA-Gated Faction Actions

At SA thresholds, new faction actions unlock:

| SA | Unlock |
|---|---|
| 1 | Faction can discuss the Southernmost in Parliamentary Session (previously, SA 0 factions had no input) |
| 2 | Faction can deploy Consul Outward toward Proximity ≤ 2 territories for Southernmost-related investigation |
| 3 | Faction can fund Expedition (existing southernmost_v30 §6.3 procedure, but faction-backed: faction provides Resources Ob 3 and military escort) |
| 4 | Faction can sponsor Mending operations (provide resources, political cover, or military protection for practitioner teams) |
| 5 | Faction has operational knowledge of the Southernmost sufficient to formulate a Repair strategy (required for any faction-directed Extraordinary Repair Weaving per §6.6) |

### 6.5 Interaction: RDT Track and Southernmost Events

RWCE firing in a territory where both Hafenmark and Church have presence creates a contested-interpretation zone. If Hafenmark controls the territory and Church has PT ≥ 1:
- Baralta can use the RWCE as political ammunition for Reformed Settlement (RDT advancement condition)
- Church can use Miracle Investigation to claim the territory's events under Church theological authority (PT +1)
- The two actions compete: whichever faction acts first in the season gains the narrative advantage. The second faction responds to the first's framing.

---

## 7. CONNECTION TO EXISTING SYSTEMS

| Existing System | Connection Point |
|---|---|
| RS track (clocks.md) | RWCE fires when Mending improves RS locally. RS band transitions change the radiation table for affected territories — the effects that non-practitioners observe. |
| CI track (clocks.md) | Church's Assert/Accommodate response to Southernmost Contact Event modifies CI. The miracle narrative reinforces Church institutional power. |
| RDT/TD tracks (tracks.md) | Baralta's jurisdictional challenge to Church Southernmost authority routes through existing Reformed Doctrine advancement. TD escalation penalises Church assertion. |
| IP track (clocks.md) | Southernmost engagement diverts faction resources from northern border defence. Every season a faction commits forces to the south is a season those forces are unavailable against Altonian pressure. IP advances if border territories are under-garrisoned. The Southernmost engagement creates a strategic tradeoff: repair the Calamity or defend against Altonia. |
| Mending mechanics (threadwork_v30) | RWCE derives entirely from existing Mending rules. No Mending mechanics are changed. Only the faction-awareness CONSEQUENCE of Mending success is added. |
| NPC AI priority trees (Tier B — next queued task) | Baralta, Himlensendt, Vaynard, Almud, and Ehrenwall all need Decision Event branches for Southernmost Contact. These integrate into the NPC priority trees as arc-conditional branches: if SA ≥ threshold AND RWCE has fired, NPC enters Southernmost response mode. |
| POI system (fieldwork_v30 §8.1) | Seam Texts (from prose guide work) are Remnant-type POIs in Church territories. If Miracle Investigation succeeds, Church may transport scripture to the investigated territory — placing Seam Text POIs in new locations, extending the player's discovery space. |
| Conviction Track | Witnessing RWCE effects may trigger Conviction pressure for individual characters. A Crown officer at Certainty 4 who witnesses inexplicable beneficial transformation faces a Certainty decision: does this confirm or challenge their framework? |
| Tensions Deck | RWCE and the triple interpretation generate new Tension Cards: "Miracle or Method" (Church vs Restoration), "Sovereign Grace" (Hafenmark vs Church re: jurisdiction), "Southern Knowledge" (Varfell vs all northern factions re: SA monopoly). |

---

## 8. THE RECURSION — Why This Works Narratively

The mechanism reproduces the founding pattern of the Church of Solmund:

**245 years ago:** A threadcut being performed thread operations at TS 100+ across the peninsula. Non-practitioners witnessed the effects without perceiving the mechanism. They built a theology on the witness testimony. The theology suppressed the practice that produced the effects.

**Game present:** Human practitioners perform Mending at Ob 7-8 in the Southernmost. Non-practitioners witness the effects without perceiving the mechanism. The Church claims the effects as Solmund's return. Baralta claims them as divine communion. The Restoration claims them as ancestral heritage. Each claim suppresses the others.

The recursion is not a narrative trick. It is a structural consequence of the perceptual prophylaxis (§9.1). As long as the Church's theology forecloses TS development in the majority population, any large-scale threadwork event will be misinterpreted by the majority as miracle or divine intervention. The recursion stops only when the prophylaxis cracks — which is why Baralta's theology, despite being wrong about mechanism, is historically progressive: her direct-communion framework weakens the prophylaxis more than the Church's essentialist monopoly.

The game does not resolve this. The player navigates it. The three factions arrive at the Southernmost with incompatible readings of the same events. The player's choices — who to support, what to reveal, what to conceal — determine which interpretation dominates. None of the interpretations is fully wrong. None is fully right. The truth (threadwork by practitioners using recovered Einhir knowledge) is mechanically available but politically dangerous to every faction that encounters it.

---

*End of proposal. No mechanical changes to existing systems. Four new triggers/actions proposed (RWCE, Miracle Investigation, Southernmost Contact Event, SA-gated faction actions). All grounded in existing rules. All require Jordan editorial approval.*
