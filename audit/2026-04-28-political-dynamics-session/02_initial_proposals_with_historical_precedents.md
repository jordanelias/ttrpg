<!-- [PROVISIONAL: 2026-04-28 session — d964fd13158349fa] -->
<!-- STATUS: PROVISIONAL — design exploration, not canonical mechanic -->
<!-- TITLE: Initial Gap-Fill Proposals (Historical Precedents) -->
<!-- POSITION IN ARC: see designs/audit/2026-04-28-political-dynamics-session/00_session_index.md -->
<!-- VETTING: see 07_armature_system_vetting.md for canonical framework assessment -->

# Interpersonal → Political Dynamics: Gap-Fill Proposals

## Historical Research Base

Seven historical systems inform these proposals, each chosen because it models a specific dynamic Valoria needs.

---

## PROPOSAL 1: NPC-NPC Horizontal Relationships (G-1)

### Historical Precedent: The Curia Regis and Inner-Circle Rivalry

The medieval King's Council (curia regis) was never a unified body — it was a permanent arena of rivalry. By 1237, the English curia had formally split because the barons complained they were inadequately represented relative to the king's personal favorites. The composition of the council itself became the central political question under Henry III, leading to the Provisions of Oxford (1258) which forced the king to accept an elected council of fifteen. The lesson: **who advises the ruler is itself a political contest**, not a settled arrangement.

The Ottoman court produced the same dynamic through the devshirme system. Sultans deliberately recruited slave-administrators to counterbalance the Turkish aristocratic nobility. This created a permanent two-faction court: devshirme officials (loyal to the sultan personally, owing their position entirely to him) versus hereditary Turkish nobles (with independent power bases, ancestral claims, and regional ties). Grand viziers from devshirme backgrounds were easier for the sultan to control but lacked the institutional legitimacy of the aristocratic faction. Every appointment, every command, every diplomatic mission was shaped by this rivalry between factions whose power derived from fundamentally different sources.

### Mechanical Proposal: NPC Regard Matrix

Each named NPC maintains a **Regard** value toward every other named NPC in their faction's inner circle. Regard is not a full Disposition track — it's a 3-state system computed at Accounting from structural inputs.

**Regard States:**

| State | Meaning | How computed |
|---|---|---|
| **Collegial** | NPCs cooperate effectively | Shared primary Conviction, OR shared successful Domain Action this season, OR player-mediated introduction (Connect action bridging two NPCs) |
| **Indifferent** | No strong opinion | Default. Different Convictions but no active conflict. |
| **Rivalrous** | Active friction | Competing for same position/resource, OR opposed Convictions that clashed in a recent faction decision, OR one NPC was promoted while the other was passed over |

**What generates rivalry (computed at Accounting):**

1. **Position competition:** Two NPCs eligible for the same appointment (e.g., two Crown inner-circle members both qualified for a governorship that only one received). The passed-over NPC shifts toward Rivalrous with the appointed NPC.

2. **Conviction clash:** When a faction decision this season aligned with NPC-A's primary Conviction but contradicted NPC-B's, NPC-B shifts toward Rivalrous with NPC-A if NPC-A visibly advocated for the decision. This is the trilateral dynamic — faction decisions create winners and losers within the court.

3. **Standing proximity:** Two NPCs at the same Standing within 1 rank of the faction leader become Rivalrous by default unless they share a primary Conviction. This is the Ottoman lesson — proximity to power generates competition for the sultan's ear.

4. **Player mediation:** A player with Disposition +2 or higher with both NPCs can attempt a **Reconcile** social action (Attunement pool, Ob = 2 + number of active rivalry triggers between the pair). Success shifts Rivalrous → Indifferent. This gives the player a political tool: the mediator role.

**Mechanical effects of Regard state:**

| State | Effect |
|---|---|
| Collegial | Joint Domain Actions between these NPCs gain +1D. NPC-A vouches for NPC-B to the player (free +1 starting Disposition with NPC-B if NPC-A is already at +2). |
| Indifferent | No modifier. |
| Rivalrous | NPC-A obstructs actions benefiting NPC-B (+1 Ob). NPC-A may leak information about NPC-B to the player unprompted (free Read result at NPC-initiated Outreach). NPC-A refuses to share intelligence about their domain if NPC-B would also benefit. |

**Videogame implementation:** The Regard matrix is engine-computed at Accounting. The player sees consequences: inner-circle meetings where NPCs argue, Outreach scenes where an NPC complains about a rival, or a Domain Action that fails because a rivalrous NPC obstructed it. The matrix itself is invisible unless the player uses Read/Appraise to detect NPC-NPC dynamics.

**Historical validation:** This is the curia regis pattern. The king's council isn't a team — it's a political environment where courtiers compete for influence, form temporary alliances, and undermine rivals. The king (or player) must manage these relationships as a political resource. The Ottoman devshirme parallel applies to Valoria's Crown court: Almud's inner circle contains both aristocratic-origin officers and institutional appointees whose legitimacy derives from different sources, creating structural rivalry.

---

## PROPOSAL 2: Standing Advancement Disposition Gates (G-2)

### Historical Precedent: Medieval Court Precedence and Patronage

In medieval and Renaissance courts, advancement required not just competence but the patron's active favor. The patron-client relationship was the engine of political mobility. An English baron seeking appointment to the Privy Council needed the monarch's personal confidence, not just a record of service. The Privy Council's composition was itself a political statement — who the king chose to sit closest to him signaled who had favor and who was being marginalized.

Renaissance Italian courts formalized this through elaborate precedence rules. At the Medici court, seating position, speaking order in council, and proximity to the duke during public events all communicated political standing. A courtier who lost precedence — seated farther from the duke, spoken to less frequently — understood that their standing was declining before any formal demotion.

### Mechanical Proposal: Patronage Threshold for Promotion

Standing advancement requires minimum Disposition with the faction leader (or the relevant inner-circle member who controls promotions for that Standing level):

| Advancement | Minimum Disposition with... | Rationale |
|---|---|---|
| 0 → 1 (Operative) | Faction leader: 0 (Neutral) | Entry-level: the leader permits you, no personal relationship needed |
| 1 → 2 (Agent) | Faction leader: 0 | Competence demonstrated through Duties, not personal favor |
| 2 → 3 (Counselor) | Faction leader: +1 (Interested) | Council access requires the leader wanting you there |
| 3 → 4 (Lieutenant) | Faction leader: +2 (Friendly) | Sub-command authority requires active trust |
| 4 → 5 (Senior) | Faction leader: +2, AND at least one inner-circle member: +2 | Consensus — the court must accept you, not just the leader |
| 5 → 6 (Prince/Chancellor) | Faction leader: +3 (Trusting) | Inner-circle entry: deep personal relationship |
| 6 → 7 (Regent-Designate) | Faction leader: +3, AND majority of inner-circle: +2 | Succession eligibility: institutional consensus, not just personal favor |

**Demotion trigger:** If the faction leader's Disposition drops below the threshold for the player's current Standing, a **Review Scene** fires on the next Scene Slate (Priority 2). The player may defend their position via social contest against the faction leader (Cognition-based, institution as adjudicator). Failure: Standing −1. Success: maintained, but the Disposition threshold becomes a persistent pressure — another drop triggers another Review.

**Historical anchor:** This is the Privy Council pattern. The council's membership was the monarch's prerogative, granted and revoked based on personal confidence. The Provisions of Oxford's forced composition was a *crisis* response to a king who lost his barons' trust — not normal governance. Normal governance meant the king chose his advisors based on personal relationship, and those advisors maintained their position by maintaining the relationship.

---

## PROPOSAL 3: Diplomatic Decisions → NPC Disposition Cascades (G-4)

### Historical Precedent: The Western Schism and Alliance Polarization

The Western Schism (1378–1417) is the clearest historical case of a single institutional decision forcing every political actor to declare allegiance. When the French cardinals elected an antipope, every secular ruler in Europe had to choose which pope to recognize. This was not an abstract theological question — it was a concrete political act that restructured every alliance, every trade relationship, and every court appointment across the continent. France, Aragon, Scotland recognized Avignon. England, the Holy Roman Empire, Poland recognized Rome. Each choice empowered domestic factions aligned with the chosen pope and alienated factions aligned with the other.

The Austria-Hungary Compromise of 1867 (Ausgleich) demonstrates the same dynamic in a dual-authority context directly parallel to Valoria's faction structure. When Franz Joseph granted Hungary autonomous internal governance while maintaining shared foreign policy and military, every institutional actor in the empire had to recalculate. Magyar nationalists were satisfied but Slavic minorities felt betrayed — their aspirations were explicitly subordinated to the Magyar-German settlement. The Compromise didn't resolve tensions; it restructured them, creating new winners and losers whose rivalries would persist until 1918.

### Mechanical Proposal: Treaty Conviction Cascade

When a faction-level diplomatic action is taken (treaty signed, alliance formed, NAP declared, tribute paid, intelligence cooperation initiated), the engine evaluates each named NPC in the acting faction's inner circle against the treaty:

**Step 1 — Conviction Evaluation:**

| NPC's primary Conviction vs. treaty alignment | Disposition shift with the decision-maker |
|---|---|
| Treaty directly serves NPC's primary Conviction | +1 |
| Treaty is neutral to NPC's Convictions | +0 |
| Treaty contradicts NPC's primary Conviction | −1 |
| Treaty benefits a faction the NPC is Rivalrous toward (per G-1 Regard matrix) | −1 additional |
| Treaty involves concession the NPC's Ethical Framework classifies as contradictory (+1 Ob category) | −1 additional |

**Step 2 — Cascading to other factions:**

NPCs in *other* factions also evaluate the treaty, but their shifts affect their Disposition toward the *treaty's counterparty faction leader*, not the player directly. This models the historical pattern: when England recognized the Roman pope, French-aligned courtiers in neutral courts shifted their loyalties.

**Step 3 — Public Knowledge:**

Treaty Conviction Cascades fire only for publicly known diplomatic actions. Covert intelligence cooperation (if undetected) produces no cascade. This incentivizes covert diplomacy — the player who wants Guild economic cooperation without alienating the Church can pursue it secretly, but at Exposure risk.

**Historical anchor:** The Schism cascade. Every major institutional decision forces a reckoning across the entire political landscape. The player who signs a Crown-Varfell military alliance must accept that Faith-aligned Crown inner-circle members will be alienated (Varfell's Consequentialist framework contradicts Divine Command), while Reason-aligned members will be satisfied. The decision is never bilateral — it is always multilateral in its internal consequences.

---

## PROPOSAL 4: Succession as Persistent Political Structure (G-5)

### Historical Precedent: Ottoman Succession and the Kafes

The Ottoman succession system evolved through three phases, each of which demonstrates a different dynamic Valoria can model:

**Phase 1 — Open Competition:** Early Ottoman princes received provincial governorships (sanjaks) where they built administrative experience and personal armies. When the sultan died, the first prince to reach Constantinople and secure the janissaries' support took the throne. The others were executed. This produced capable sultans but catastrophic succession crises (the Ottoman Interregnum, 1402–1413, lasted over a decade).

**Phase 2 — Institutional Fratricide:** Mehmed II legalized fratricide. New sultans executed all brothers immediately. This prevented civil war but reduced dynasty to a single line — one disease could end the dynasty entirely. The largest instance: Mehmed III had 19 brothers killed.

**Phase 3 — The Kafes:** From ~1603, surplus princes were confined in palace quarters rather than killed. This preserved the dynasty's resilience but produced sultans with no administrative experience, no personal networks, and no political education. Crucially, **the anticipation of succession reshaped court behavior continuously**: every courtier evaluated which confined prince was most likely to emerge, and positioned themselves accordingly. The vizier's rivalry with the Valide Sultan (mother of the sultan) was often a succession-proxy conflict — who controlled access to the confined princes controlled the next transition.

### Mechanical Proposal: Succession Anxiety Clock

A new ambient clock, **Succession Pressure**, tracked per faction. It rises based on leader vulnerability indicators and produces mechanical effects on NPC behavior before succession actually fires.

**Succession Pressure triggers (each contributes +1 to the clock):**

| Trigger | Condition |
|---|---|
| Leader aging | Leader's highest attribute reduced by Generational Shift (below starting value) |
| Arc approaching removal | Leader's arc has ≥ 2 of 3 branch conditions for removal arc met |
| No designated successor | Faction has no NPC at Standing 7 or designated heir |
| Stability crisis | Faction Stability ≤ 2 for 2+ consecutive seasons |
| Leader Scar accumulation | Leader has 2+ Conviction Scars |

**Succession Pressure effects (cumulative):**

| Clock value | Effect |
|---|---|
| 1 | NPCs in the faction evaluate potential successors. Each NPC's AI priority tree adds "succession positioning" as a secondary consideration (won't override primary priorities but influences tiebreakers). |
| 2 | NPCs with Disposition +2 toward a specific potential successor shift +1 Disposition toward that successor and −1 toward rival successors. Factionalization begins. Player can detect this via Read action ("She seems to be thinking about what comes next"). |
| 3 | Outreach scenes reference succession explicitly. NPCs may request the player's support for a specific successor. Faction Domain Action efficiency −1D (institutional paralysis from positioning). |
| 4 | Succession is imminent. If Standing 7 player exists, they receive a mandatory Scene Slate entry: "Declare candidacy or support another." If no player candidate, NPC succession contest fires per existing rules. |

**Succession Pressure decay:** Clock resets to 0 when: (a) a successor is formally designated AND the designee has Disposition +2 with ≥ 50% of inner circle, OR (b) the leader reverses the vulnerability indicators (e.g., Stability returns above 2, arc branch conditions recede). Designation alone doesn't resolve anxiety — the designee must be *accepted* by the court.

**Historical anchor:** This is the Ottoman kafes dynamic transposed to Valoria's faction structure. The kafes prevented princes from building power bases, but courtiers still positioned for succession by cultivating relationships with the confined princes' mothers and allies. In Valoria, the "confinement" is structural — the designated successor may be Torben (Crown), Maret Uln (Varfell), or a Cardinal (Church) — but the court's anticipatory positioning is the same. The player navigating succession politics isn't waiting for an event; they're managing a persistent political force.

---

## PROPOSAL 5: Cross-Faction Relationship Discovery (G-6)

### Historical Precedent: Byzantine Faction Allegiance and the Nika Dynamic

The Byzantine Blues and Greens began as chariot-racing factions but became proxies for deeper political, religious, and class allegiances. Emperors courted factions for legitimacy, and faction leaders influenced appointments through public pressure. The critical dynamic: **faction allegiance was visible**. A courtier's alignment with the Blues or Greens was public knowledge, and emperors used this information to evaluate loyalty. A Blue-aligned official appointed to a Green-dominated province was understood to be either a loyalty test or a deliberate provocation.

The Nika Riot (532) demonstrated the catastrophic potential when factions temporarily united against the emperor — but also showed that the default state was mutual surveillance. The factions monitored each other's members and reported disloyalty to the emperor, making cross-faction relationships genuinely dangerous.

### Mechanical Proposal: Factional Exposure Track

When a player builds Disposition ≥ +3 with an NPC from a rival faction, a **Factional Exposure** counter begins accumulating:

| Action with rival-faction NPC | Factional Exposure gained |
|---|---|
| Social action at Disposition +3 | +1 per action |
| Social action at Disposition +4–5 | +2 per action |
| Knot formation with rival NPC | +3 (one-time) |
| Meeting in the rival NPC's territory | +1 additional per scene (more visible) |
| Meeting in neutral territory | +0 additional |
| Meeting in the player's own faction's territory | +1 additional (the rival NPC's presence is noticed) |

**Factional Exposure threshold = player's Cover value** (Cognition + History, per fieldwork §6.1). When Factional Exposure exceeds Cover:

1. The player's faction leader learns of the cross-faction relationship.
2. Faction leader's Disposition shifts: −1 for allied-faction contacts, −2 for rival-faction contacts, −3 for hostile-faction contacts.
3. A Demand Scene fires from the faction leader: explain the relationship. Player can justify (Negotiate action, Ob = 3 — the leader is not easy to convince), deflect (Ob = 4), or accept the reprimand (Disposition stabilizes at −1 but no further action).
4. If the player justifies successfully ("I'm cultivating an intelligence asset" / "I'm pursuing diplomatic opening"), the Factional Exposure counter resets AND the faction leader's Disposition is restored. The relationship is sanctioned — but the player must actually deliver results from it, or the next discovery will be harder to justify (+1 Ob).

**Historical anchor:** The Byzantine faction-surveillance dynamic. Allegiance was visible, cross-faction contact was monitored, and the emperor evaluated loyalty based on observed associations. The player can maintain cross-faction relationships, but must manage the visibility of those relationships against their own faction's surveillance capacity.

---

## PROPOSAL 6: Intelligence as Influence Operations (G-7)

### Historical Precedent: Venice's Council of Ten — Three-Channel Intelligence

Venice's Renaissance intelligence apparatus, administered by the Council of Ten, operated through three channels that map directly to a tiered intelligence system:

1. **Professional channel:** Formally appointed diplomats and state servants who gathered intelligence as part of their official duties. This is overt information-gathering — the ambassador's dispatch is intelligence, but it's also a legitimate governmental function.

2. **Mercantile channel:** Venetian merchants stationed in commercial hubs of strategic significance. Their commercial activity provided cover for intelligence-gathering. This is semi-covert — the merchant's presence is legitimate, but their reporting to the Ten is secret.

3. **Mercenary channel:** Run-of-the-mill spies willing to risk their lives for cash, privilege, or political favor. This is fully covert active espionage — infiltration, theft, and increasingly, **influence operations** designed to shape the target's behavior rather than merely observe it.

The Council of Ten's organizational maturity was specifically in their ability to *compare and contrast* information from all three channels, evaluating reliability and identifying contradictions. They didn't just collect — they assessed.

### Mechanical Proposal: Three-Tier Intelligence Operations

Builds on existing Varfell Private Collection (Intel vs Ob 2) and settlement-layer intelligence brokers:

**Tier 1 — Observation (existing, formalized):**
- **Mechanism:** Read/Appraise social actions, Investigation Evidence Track.
- **Output:** NPC Disposition, Beliefs, Conviction, emotional state. Faction stats visible at Standing 2+.
- **Cost:** Scene actions. Exposure accumulation.
- **Historical parallel:** Venice's professional channel. Diplomats observing and reporting.

**Tier 2 — Influence (new):**
- **Prerequisite:** Disposition +2 with target NPC. Intel stat ≥ 3 (player's faction or personal).
- **Mechanism:** New social action — **Insinuate**.
  - Pool: Attunement × 2 + relevant History + 3
  - Ob: floor(target NPC's Cognition / 2) + 2 (smart NPCs are harder to manipulate)
  - Target: a specific relationship the target NPC holds (e.g., target NPC's Disposition with their faction leader)
- **Effect on Success:** Target NPC's Disposition with the specified relationship shifts by −1 this season. The shift is *manufactured grievance* — the player plants doubts, exaggerates slights, reminds the NPC of past injuries.
- **Effect on Failure:** Target NPC's Disposition with the player shifts by −1 (the NPC detects the manipulation). Exposure +2.
- **Effect on Overwhelming:** Target NPC's Disposition with the specified relationship shifts by −2, AND the NPC volunteers one piece of previously-hidden information about the relationship (they're venting).
- **Limits:** One Insinuate per target NPC per season. Cannot stack with other Insinuate attempts against the same relationship in the same season (even from different agents). Cannot target the player's own Disposition with the NPC (that's just Converse).
- **Historical parallel:** Venice's mercantile channel. The merchant who trades with a rival state's official and subtly undermines their confidence in their own government's policies. The relationship is real; the intelligence purpose is hidden.

**Tier 3 — Subversion (new, high-investment):**
- **Prerequisite:** Tier 2 Influence has reduced target NPC's Disposition with their faction leader to ≤ 0. Player has Disposition +3 with target NPC. Standing 4+ in player's faction (authority to make offers).
- **Mechanism:** Recruit action per existing §1.12: Cha×2+H+3, Ob = floor(NPC highest Disp/2)+1. But now the Ob is lower because Tier 2 operations have degraded the NPC's institutional loyalty.
- **Additional effect:** A recruited NPC brings intelligence proportional to their former Standing. Standing 3+ NPC: reveals inner-circle deliberation content. Standing 5+ NPC: reveals faction stat values and active Domain Action plans. This is the defection intelligence bonus — the higher the defector's position, the more they know.
- **Counter-intelligence:** The target faction can detect Tier 2 operations through their own Intel stat. Each season, the faction's Intel pool rolls against Ob = player's Cover value. Success: the faction identifies that an Influence operation is underway (though not necessarily who's running it). The faction leader can then initiate a counter-Demand scene against the target NPC to reinforce loyalty.
- **Historical parallel:** Venice's mercenary channel. The spy who infiltrates, builds trust, and turns an asset. The Council of Ten's genius was organizational — they assessed information across channels. Valoria's engine does the same: the AI evaluates Tier 1 observations, Tier 2 influence effects, and Tier 3 recruitment attempts as a coherent intelligence picture.

---

## PROPOSAL 7: Settlement Loyalty → Faction Resilience (G-3)

### Historical Precedent: The Ausgleich — Institutional Loyalty as Structural Resilience

The Austria-Hungary Compromise demonstrates how institutional loyalty at the sub-state level creates structural resilience for the larger entity. Hungary's autonomous governance under the Compromise meant that the Habsburg monarchy was more resilient than a unitary state would have been — Hungarian institutions continued to function even when Austrian institutions were in crisis, and vice versa. But this resilience was conditional on the local institutions being *loyal* to the framework. When Hungarian nationalism exceeded the Compromise's ability to contain it, the resilience became fragility.

The parallel to Valoria's settlement layer: settlements with strong local governance (high Order, high Prosperity) and a governor with deep local NPC relationships should be structurally resilient against faction-level disruption. A well-governed settlement doesn't collapse when its controlling faction loses a battle or suffers a Stability crisis — it has local institutional capacity that persists independent of the national faction's health.

### Mechanical Proposal: Settlement Resilience Score

**Settlement Resilience** = Order + floor(Governor's average Disposition with local named NPCs / 2). Range: 0–7 (Order 0–5 + Disposition contribution 0–2).

**Effects:**

| Resilience | Effect |
|---|---|
| 5+ | Settlement resists hostile takeover: +1 Ob to conquest or subversion targeting this settlement. Settlement generates +1 Stability for the controlling faction at Accounting. |
| 3–4 | Settlement functions normally. Standard rules. |
| 2 or below | Settlement is vulnerable: −1 Ob for hostile actions targeting this settlement. No Stability contribution. |

**How this connects interpersonal work to politics:** A player-governor who spends 4 seasons building Disposition +3 with 3 local NPCs (average Disposition +3 → +1 Resilience contribution) and maintaining Order 4 (Pacify/Administer actions) produces Settlement Resilience 5. This settlement is now a political asset — it contributes Stability to the faction AND resists enemy subversion. The interpersonal investment has a measurable political return.

**Faction collapse interaction:** When a faction loses its last province (§6.3 Faction Collapse), settlements with Resilience 5+ automatically become holdout settlements. The existing holdout mechanic (governor Disposition ≥ +3) is now computed from a broader base that includes the governor's interpersonal network, not just their personal loyalty.

---

## PROPOSAL 8: Companion-Governor Framework Alignment (G-8)

### Historical Precedent: Cardinal Governors and the Papal-Secular Tension

The tension between papal and secular governance in medieval Europe provides the historical model. A bishop appointed as governor of a secular territory brought the Church's institutional priorities into secular governance. Over time, the governed territory's character shifted toward the bishop's institutional alignment — more resources directed to ecclesiastical purposes, more Church-favorable rulings in disputes, gradual entrenchment of Church authority in local governance.

This is already partially modeled in Valoria's Bishop-Governor mechanic (settlement_layer §3.2 PP-TBD). The extension is to apply the same principle to all companion-governors: any companion governing a settlement gradually shifts that settlement's implicit framework alignment toward their own Conviction.

### Mechanical Proposal: Governor Conviction Drift

Each season a companion-governor holds a settlement:

1. If the companion's primary Conviction aligns with the controlling faction's Ethical Framework: no drift. Governance is harmonious.
2. If the companion's primary Conviction *differs* from the controlling faction's Ethical Framework: the settlement accumulates +1 **Framework Tension** per season.
3. At Framework Tension 4: the settlement generates a Scene Slate event (Priority 4) — local NPCs express confusion or resistance to the governor's priorities. The controlling faction leader receives a notification that governance of this settlement is diverging from institutional expectations.
4. At Framework Tension 8: the settlement's Domain Action support shifts — Domain Actions aligned with the companion's Conviction gain −1 Ob in this settlement, while Domain Actions aligned with the controlling faction's Framework gain +1 Ob. The settlement has been shaped by its governor's personal values.

**Reset:** Framework Tension resets to 0 if the companion-governor is replaced or if the companion's Conviction shifts to align with the faction's Framework.

**What this creates:** A soft pressure against mindless companion deployment. The player must consider whether their Reason-aligned companion governing a Church-controlled settlement will eventually create institutional friction. This is the cardinal-governor problem: the Church's man governing a secular territory serves the Church's interests, not the territory's secular lord's interests.

---

## SUMMARY: Priority and Complexity

| Proposal | Gap | Historical precedent | Complexity | Systems touched |
|---|---|---|---|---|
| P-1 NPC Regard Matrix | G-1 | Curia regis, Ottoman devshirme | Medium | NPC AI, inner-circle, faction politics |
| P-2 Standing Disposition Gates | G-2 | Privy Council patronage, court precedence | Low | Player progression, faction politics |
| P-3 Treaty Conviction Cascade | G-4 | Western Schism, Ausgleich | Medium | Diplomacy, NPC behavior, faction AI |
| P-4 Succession Anxiety Clock | G-5 | Ottoman kafes, succession anticipation | Medium | Clocks, NPC behavior, faction AI |
| P-5 Factional Exposure Track | G-6 | Byzantine faction surveillance | Low | Exposure system, Disposition |
| P-6 Three-Tier Intelligence | G-7 | Venice Council of Ten | Medium-High | Social actions, Intel stat, NPC loyalty |
| P-7 Settlement Resilience | G-3 | Ausgleich institutional loyalty | Low | Settlement stats, Stability |
| P-8 Governor Conviction Drift | G-8 | Cardinal governors, papal-secular tension | Low | Companion system, settlement governance |

**Recommended implementation order:** P-2 → P-7 → P-5 → P-8 (low complexity, extend existing mechanics) → P-1 → P-3 (medium complexity, new systems) → P-4 → P-6 (medium-high complexity, new systems with extensive AI integration).
