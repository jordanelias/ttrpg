<!-- [PROVISIONAL: 2026-04-28 session — d964fd13158349fa] -->
<!-- STATUS: PROVISIONAL — design exploration, not canonical mechanic -->
<!-- TITLE: Structural Revision: Directionality and Emergence -->
<!-- POSITION IN ARC: see designs/audit/2026-04-28-political-dynamics-session/00_session_index.md -->
<!-- VETTING: see 07_armature_system_vetting.md for canonical framework assessment -->

# Interpersonal → Political Proposals: Structural Revision

## Diagnosis

The v1 proposals have three structural flaws:

**1. Vertical-only chains.** Most proposals run Player ↔ NPC or NPC ↔ Faction Leader. The player is the only agent who connects systems. NPCs react to the player but don't generate political dynamics independently.

**2. Threshold-triggered pattern matching.** "Disposition ≥ X → effect Y." "Clock reaches 3 → consequence fires." These produce deterministic outcomes from fixed inputs. The same game state always produces the same result. No context sensitivity, no multiple paths to the same outcome, no surprising combinations.

**3. One-shot cascades, not feedback loops.** Treaty → NPC evaluation → Disposition shift → done. The shift doesn't feed back into the conditions that generated it. The system settles into a new equilibrium immediately rather than producing ongoing instability that forces continuous political management.

This revision restructures each proposal around three principles:

- **Multi-directionality:** Every proposal must produce effects that move laterally (NPC ↔ NPC), diagonally (personal → settlement → faction, or faction → settlement → personal), and feed back into their own inputs.
- **Context-dependent evaluation:** The same structural conditions should produce different outcomes depending on what else is happening. An NPC rivalry during peacetime is a nuisance; the same rivalry during a succession crisis is an existential threat.
- **Emergent combination:** No individual proposal should fully specify its consequences. The interesting dynamics should emerge when 2–3 proposals interact in ways that aren't pre-scripted.

---

## P-1 REVISED: NPC Regard as Behavioral Output, Not Computed State

### What was wrong

Regard was computed from structural inputs at Accounting: same Conviction = Collegial, competing position = Rivalrous. Deterministic. And the 3-state system is too coarse — it makes every NPC-NPC relationship a fixed category rather than a dynamic trajectory.

### Revision

**Regard is not a state — it's a running balance.** Each NPC-NPC pair accumulates Regard Points (RP) on a scale of −6 to +6 over time. RP shifts are driven by *events*, not structural snapshots.

**What generates RP shifts (not exhaustive — these are categories, not a closed list):**

| Event | RP shift | Direction |
|---|---|---|
| NPC-A's Domain Action proposal was adopted while NPC-B's was rejected this season | NPC-B: −1 toward NPC-A | Lateral (intra-faction) |
| Both NPCs participated in a successful joint Domain Action | +1 mutual | Lateral |
| Player promoted over NPC-A (P-2 interaction) | NPC-A: −1 toward player AND −1 toward any NPC who visibly supported the promotion | Lateral + diagonal (promotion at faction level generates NPC-NPC friction) |
| Treaty signed that serves NPC-A's Conviction (P-3 interaction) | NPCs whose Conviction was contradicted: −1 toward NPC-A if NPC-A advocated for it | Lateral (diplomatic decision creates internal rifts) |
| NPC-A's governed settlement suffered Order loss while NPC-B's thrived | NPC-A: −1 toward NPC-B (perceived comparison) | Diagonal (settlement-level outcome creates personal-level resentment) |
| Shared crisis: faction Stability ≤ 2 | +1 mutual among all inner-circle NPCs (external threat suppresses internal rivalry) | Lateral, context-dependent |
| NPC-A's Conviction Scar (arc transition) | All NPCs with Collegial regard toward NPC-A's *old* Conviction: −2 toward NPC-A (betrayal of shared values). NPCs aligned with NPC-A's *new* Conviction: +1 toward NPC-A (new ally). | Lateral + diagonal (personal-scale arc change restructures all horizontal relationships) |

**Why this matters:** Regard is now a *history*, not a snapshot. Two NPCs at RP −4 got there through accumulated grievances, not a single structural condition. The player who wants to reconcile them needs to understand *why* the RP is negative — was it position competition? Conviction clash? Accumulated slights from opposed Domain Action proposals? Different causes require different interventions.

**The feedback loop:** RP influences NPC behavior, and NPC behavior generates new RP events. An NPC at RP −3 toward a colleague begins obstructing their proposals (+1 Ob to Domain Actions the colleague benefits from). The obstruction may cause the colleague's Domain Action to fail. Failure costs the colleague's faction Stability −1 (per PP-403). The Stability loss triggers crisis behavior in other NPCs. The crisis behavior reshuffles priorities. The reshuffled priorities generate new Domain Action conflicts. New conflicts generate new RP shifts. **The system doesn't settle — it oscillates.**

**Downward ripple:** An NPC at RP −4 toward the player's ally who governs a settlement may withhold garrison support from that settlement, reducing its Defense stat. The Defense reduction makes the settlement vulnerable to hostile action. Hostile action triggers a Scene Slate event. The scene produces personal-scale content (the player must defend the settlement) that originated from a lateral NPC-NPC relationship.

**Upward ripple:** Two NPCs at RP +5 (strong Collegial) begin coordinating their Domain Action proposals. Their coordination produces faction-level strategic coherence that rivals notice. A rival faction detects the coordination through intelligence and targets the weaker of the two NPCs with Tier 2 Influence operations (P-6 interaction), attempting to break the coalition by degrading one NPC's loyalty.

### NPC-Initiated Relationship Events

Critical change: NPCs don't just passively accumulate RP — they *act* on their Regard independently of the player.

**At Accounting, each NPC with RP ≤ −3 toward any colleague evaluates one action from this list (AI priority order):**

1. **Obstruct:** Declare opposition to one of the colleague's active projects next season. The project (Domain Action, settlement governance directive, military deployment) takes +1 Ob.
2. **Inform:** Approach another NPC (or the player) with damaging information about the colleague. This is a free Read result — the informing NPC volunteers one piece of intelligence about the colleague's activities, Beliefs, or vulnerabilities. The recipient's RP with the colleague shifts −1 (information poisons the relationship).
3. **Coalition:** Approach another NPC who also has RP ≤ −2 toward the same colleague. If both NPCs share this antipathy, they form a **Bloc** — a temporary coalition that coordinates opposition. A Bloc of 2 NPCs produces +2 Ob on any Domain Action that benefits their shared target. A Bloc of 3+ produces +3 Ob and triggers a mandatory Faction Council Scene (the player must attend and take a side).

**At Accounting, each NPC with RP ≥ +4 toward any colleague evaluates one action:**

1. **Vouch:** If the colleague has low Disposition with the player or the faction leader, the vouching NPC spends social capital to improve it: colleague's Disposition +1 with the vouched-to party, voucher's Disposition −1 with the vouched-to party if the vouched colleague later betrays or underperforms. The voucher takes on *risk* for their ally.
2. **Coordinate:** Propose a joint Domain Action next season. Joint Domain Actions pool both NPCs' relevant stats, producing a larger dice pool but requiring both NPCs to commit their seasonal action. If successful, +1 RP mutual.
3. **Mentor:** If one NPC is higher Standing, they mentor the lower, providing +1D to the mentee's next contested roll. Mentoring creates a dependency bond — if the mentor later defects or is removed, the mentee's Stability check is at +1 Ob (loss of institutional support).

**What this produces that v1 didn't:** NPCs form coalitions, obstruct rivals, vouch for allies, and mentor juniors — all without player involvement. The player enters a political environment that is already in motion. They can intervene (Reconcile action, strategic social investment, choosing which factions to support in council scenes) but they cannot control the horizontal dynamics. This is the curia regis pattern — the court is a living political system, not a set of bilateral relationships with the ruler.

---

## P-2 REVISED: Promotion as Political Event

### What was wrong

Static threshold check. No lateral consequences. Promotion is a private transaction between player and faction leader.

### Revision

**Promotion triggers a Regard cascade.** When the player advances in Standing, every NPC in the faction who is at the *same or adjacent Standing* evaluates:

| NPC condition | Response |
|---|---|
| NPC is at the same Standing the player just reached AND NPC's RP with the player is ≤ 0 | RP −2 toward player (they were passed over or now share a crowded rank). NPC may Obstruct (per P-1 revised) in the following season. |
| NPC sponsored the player's promotion (Disposition +3 with player, same faction) | RP +1 toward player. But: NPC expects reciprocal support. If the player does not support the sponsor's next Domain Action proposal, the sponsor's Disposition with the player drops −2 (betrayal of patronage obligation). |
| NPC is from a *different faction* and observes the promotion | Rival faction leaders update their threat assessment. If the promoted player is now Standing 5+ in a rival faction, the rival faction's AI priority tree adds "monitor [player]" as a secondary priority. This can trigger Tier 1 intelligence operations (P-6 interaction). |

**Downward ripple:** A promotion to Standing 4+ (Lieutenant, eligible for settlement governance) changes what the player can *do* in settlements. New settlements become available for governance assignment. The faction leader's choice of *which* settlement to assign is itself a political act — a prestigious settlement assignment signals favor and provokes jealousy from NPCs who wanted that assignment. The settlement's existing governor (if replaced) has an opinion. The replaced governor's RP with the player shifts −3 (displacement). If the replaced governor had high local NPC Disposition, those local NPCs' Disposition with the new player-governor starts at −1 (loyalty to the old governor).

**Lateral ripple:** NPCs who were also eligible for the settlement assignment but weren't selected form a potential Bloc (per P-1 revised) against the player. The Bloc may target the player's settlement governance — obstructing supply shipments, withholding military support, or generating bureaucratic friction that increases the Ob of governance actions by +1.

**The feedback loop:** The player's promotion creates NPC resentment → resentment produces obstruction → obstruction makes the player's governance harder → governance difficulty may reduce Settlement Resilience (P-7 interaction) → reduced resilience makes the settlement vulnerable → the player needs to spend scene actions resolving the vulnerability instead of advancing their agenda → the delay in advancing their agenda may cause the faction leader's expectations to go unmet → unmet expectations risk Disposition loss with the faction leader → Disposition loss risks demotion. **The promotion itself creates the conditions that threaten the promotion.**

This is the historical pattern: advancement in a political hierarchy is never free. Every step up creates enemies, obligations, and vulnerabilities that must be managed continuously.

---

## P-3 REVISED: Diplomatic Decisions as Political Shockwaves

### What was wrong

One-directional cascade. NPCs receive a Disposition number change and that's it. They don't *act* on their alienation.

### Revision

**Diplomatic decisions generate NPC Actions, not just Disposition shifts.**

When a treaty is signed:

**Phase 1 — Evaluation (immediate):** Each inner-circle NPC evaluates the treaty against their Conviction (unchanged from v1). But the evaluation produces an **Alignment Score** for this specific treaty, not just a Disposition shift:

- Alignment Score +2: Treaty perfectly serves this NPC's Conviction and institutional interests.
- Alignment Score +1: Treaty is compatible.
- Alignment Score 0: Neutral.
- Alignment Score −1: Treaty contradicts this NPC's Conviction.
- Alignment Score −2: Treaty actively empowers a rival or damages an interest the NPC has staked their position on.

**Phase 2 — Reaction (next Accounting, context-dependent):** Each NPC with Alignment Score ≤ −1 selects a response based on their current political position (not just the treaty in isolation):

| NPC's context | Response to alienating treaty |
|---|---|
| NPC has RP +3 with the decision-maker AND Alignment −1 | Private counsel dissent (ED-664 mechanism). NPC expresses disagreement in private. No public consequence. Disposition with decision-maker unchanged. But: the NPC's Belief about the decision-maker may be challenged — "I thought they shared my values." If this is the 2nd+ alienating decision, the NPC's Belief about the decision-maker acquires narrative pressure toward revision. |
| NPC has RP ≤ +1 with the decision-maker AND Alignment −1 | Public grumbling. Disposition with decision-maker −1. NPC approaches other NPCs with similar Alignment Scores to discuss opposition (feeds P-1 coalition formation). |
| NPC at any RP AND Alignment −2 | Active opposition. NPC generates an Outreach scene with the player (or Demand if Disposition ≤ −2) confronting the treaty directly. NPC begins evaluating whether their faction still serves their Conviction (feeds P-4 succession evaluation and potentially P-6 intelligence vulnerability). |
| NPC governs a settlement AND Alignment ≤ −1 | **Settlement-level resistance (diagonal ripple).** The governor *deprioritizes* treaty implementation in their settlement. If the treaty required resource transfer, the settlement's contribution is reduced. If the treaty involved military cooperation, the governor delays garrison redeployment. This is not sabotage — it's bureaucratic foot-dragging that produces the same effect. The controlling faction's treaty obligations go partially unmet, which damages diplomatic reliability with the counterparty. |

**Phase 3 — Counter-reaction (following season):** NPCs with Alignment Score ≥ +1 notice the opposition and respond. They may:

- Vouch for the treaty to the decision-maker, reinforcing the decision-maker's commitment (RP +1 with decision-maker).
- Obstruct the opposing NPCs (feeds P-1 rivalry).
- Approach the player for support in maintaining the treaty.

**The feedback loop:** Treaty → alienation → coalition formation → obstruction → partial treaty failure → diplomatic reliability damage → counterparty faction re-evaluates relationship → new diplomatic crisis → player must decide whether to enforce the treaty (alienating the opposition further) or reverse it (alienating the supporters). **The treaty doesn't settle the political question — it opens it.**

**Cross-faction diagonal:** The alienated NPC's public opposition is *intelligence* that rival factions can detect. A rival faction that learns (through Tier 1 operations) that the Crown's inner circle is divided over a treaty can exploit the division — approaching the alienated NPC with a counter-offer, or timing a diplomatic provocation to coincide with the internal friction.

---

## P-4 REVISED: Succession as Environmental Pressure, Not Clock

### What was wrong

Threshold-based clock. Deterministic escalation. Ticks up in fixed increments, fires effects at fixed values.

### Revision

**Succession is not a clock — it's an environmental condition that modifies all other systems.**

Instead of a separate Succession Pressure counter, succession anxiety is expressed through the *existing* systems operating under modified parameters.

**When a faction leader's vulnerability indicators activate** (highest attribute reduced by Generational Shift, arc approaching removal, Stability ≤ 2 sustained), the following systemic modifications engage:

**1. NPC AI priority tree modification:** All NPCs in the faction gain a new evaluation criterion in their decision procedure (npc_behavior §4.1 Decision Procedure). Before the institutional filter, a **Succession Filter** evaluates: "Does this action position me well for the next leader?" If the NPC has Disposition ≥ +2 with a specific potential successor, actions that benefit that successor gain −1 Ob (the NPC is motivated). Actions that contradict the successor's expected priorities gain +1 Ob (the NPC is reluctant). This doesn't override the existing priority tree — it *biases* tiebreakers.

**2. RP dynamics intensify:** NPC-NPC Regard shifts (P-1) are doubled during succession conditions. A rivalry that would normally produce −1 RP produces −2. A shared crisis bonus that would produce +1 produces +2. The political environment becomes more volatile because the stakes are higher — every relationship now has succession implications.

**3. Cross-faction exploitation (diagonal):** Rival factions whose intelligence reveals succession vulnerability gain a new AI behavior: **Succession Exploitation.** The rival faction targets the vulnerable faction's most alienated inner-circle NPCs with Tier 2 Influence operations (P-6 interaction). The pitch is not "defect now" but "the next leader will be hostile to you — prepare alternatives." This is slower and subtler than direct recruitment but creates a *pre-positioned* defection that fires only if the succession produces an unfavorable outcome.

**4. Settlement-level consequences (downward ripple):** NPCs who govern settlements and are positioning for succession shift their governance priorities. A governor who supports Successor-A may redirect settlement resources toward Successor-A's preferred policies (e.g., military buildup if Successor-A is militaristic), degrading other settlement stats. This is visible to the player: a settlement whose Order is declining despite having a competent governor is a signal that the governor is neglecting governance for political positioning. The player can investigate (Read action) and discover the succession dynamic.

**5. Player involvement (upward ripple from personal scale):** The player's relationships with potential successors become politically significant. Other NPCs observe who the player spends time with, which Outreach scenes they attend, and which potential successor they seem to favor. The player's social choices *generate information* that feeds into the P-1 Regard system: NPCs aligned with the player's apparent preferred successor shift +1 RP toward the player; NPCs aligned with other successors shift −1. **The player's mere social behavior during a succession period is a political act that restructures the court around them.**

**Why this is not pattern matching:** The succession condition doesn't fire a pre-scripted cascade. It modifies *how every other system operates*. The specific dynamics depend on: which NPCs have which relationships with which potential successors, what the settlement governance situation is, which rival factions are actively conducting intelligence, and what the player is doing socially. The same succession vulnerability in two different game states produces entirely different political dynamics because the modifier applies to a complex system, not to a fixed trigger.

---

## P-5 REVISED: Cross-Faction Exposure as Probabilistic, Bidirectional Risk

### What was wrong

Linear counter. Deterministic threshold. One-directional (only the player's faction discovers).

### Revision

**Exposure is probabilistic, not threshold-based.** Each season, the player's faction rolls its Intel pool against the player's Cover value. Success = discovery. This means discovery timing is *unpredictable* — the player doesn't know when they'll be caught, only that the probability increases as they spend more time with cross-faction contacts.

**Exposure probability modifiers (context-dependent):**

| Condition | Modifier to faction's Intel roll |
|---|---|
| Faction is at Stability ≤ 2 (crisis — paranoid surveillance) | +2D |
| Faction is at Stability ≥ 4 (confident — inattentive) | −1D |
| Faction currently engaged in external military conflict | −2D (attention elsewhere) |
| A Rivalrous NPC (P-1) is actively seeking to undermine the player | +1D (deliberate informing) |
| The cross-faction contact is with a *hostile* faction (not just rival) | +1D (more scrutiny on hostile contacts) |
| Player meets the contact in a settlement governed by a Collegial NPC | −1D (friendly governor provides cover) |
| Player meets the contact in a settlement governed by a Rivalrous NPC | +2D (hostile governor reports the contact) |

**Bidirectional risk:** The cross-faction NPC's faction runs the same exposure check. If *both* factions discover the relationship simultaneously, the political consequences are amplified: each faction assumes the contact is intelligence-related, and both factions' inner circles react. The player's cross-faction NPC contact faces their own Demand scene from their own faction leader. The contact's response to that Demand scene (capitulate, deflect, or defect) is an NPC decision that the player can influence through their existing Disposition but cannot control.

**Diagonal consequence:** If the cross-faction contact is an NPC who governs a settlement, discovery of the relationship may destabilize the contact's governance position. Their faction leader may reassign them, removing a governor the player had invested in. The settlement's local NPCs, who had built Disposition with the old governor, face a disruption — a new governor with different Conviction and no local relationships arrives. Settlement Order drops. The Order drop creates a Scene Slate event. **The player's personal relationship with a cross-faction NPC produced a governance crisis in a settlement they don't even control.**

---

## P-6 REVISED: Intelligence as Ecosystem, Not Tier List

### What was wrong

Three separate tiers stacked vertically. Each tier is a standalone action with fixed prerequisites. No interaction between tiers; no counter-play that creates dynamics.

### Revision

**Intelligence operations create observable behavioral changes that other actors can detect and respond to.** The tiers are not sequential gates — they're overlapping activities that generate signals.

**Tier 1 → Tier 2 feedback:** A player who has Appraised a target NPC (Tier 1) and learned their Conviction and current emotional state gets *targeting data*. This doesn't just grant +1D to Insinuate — it allows the player to choose *which relationship* to target and *which grievance* to exploit. An Insinuate against a target NPC's relationship with their leader using a grievance the player has specifically identified through Appraisal is at −1 Ob compared to a generic Insinuate. **Tier 1 makes Tier 2 more effective, not through a bonus die, but through better target selection.**

**Tier 2 → Counter-intelligence signal:** An NPC whose loyalty is being degraded by Insinuate operations doesn't just lose Disposition silently. They *behave differently*. The behavioral change is detectable by attentive actors:

- The degraded NPC's AI priority tree shifts subtly — they're less responsive to the faction leader's priorities, more likely to pursue independent actions, more likely to attend Outreach scenes from the player's faction.
- Other NPCs in the target faction can detect this through their own RP relationships. An NPC who is Collegial (RP +3) with the degraded NPC may notice the behavioral change and report it to the faction leader (this is an NPC-initiated counter-intelligence action, not a player action).
- The faction leader, if they have Intel ≥ 3, may initiate a **Loyalty Interview** — a Demand scene with the degraded NPC. The degraded NPC's response depends on their current Disposition with the leader and their Disposition with the player: high Disposition with the player + low with the leader = potential defection. High with both = conflicted (generates a Belief revision opportunity). Low with both = isolated (NPC may flee or become a free agent).

**Tier 2 → NPC lateral action:** The degraded NPC doesn't just passively lose loyalty. If their Disposition with their leader drops below +1 AND they have RP ≥ +3 with another NPC in the same faction, the degraded NPC may *recruit their friend* into shared dissatisfaction. This is NPC-initiated Tier 2 — the player's influence operation spreads laterally through the target faction's NPC network without additional player action. The spread follows RP relationships: NPCs Collegial with the degraded NPC are susceptible; NPCs Rivalrous with the degraded NPC are immune (they're glad the rival is weakening).

**Tier 3 → Upward ripple:** A recruited NPC doesn't just bring intelligence and join the player's faction. Their departure creates a *hole* in the source faction's structure:

- If the recruited NPC governed a settlement, the settlement needs a new governor immediately. The faction's AI assigns one, but the assignment is from a diminished pool. The new governor may be less competent, shifting settlement stats downward.
- If the recruited NPC was in the inner circle, the faction's decision-making capacity is reduced. The faction's AI evaluates whether to replace the inner-circle member (from their Standing 5+ pool) or leave the seat empty. An empty seat reduces the faction's effective Influence by −1.
- If the recruited NPC was Collegial with other NPCs, those NPCs face a forced RP evaluation: do they follow the defector (RP ≥ +4 with the defector AND RP ≤ −2 with the faction leader = follow) or feel abandoned (RP drops with the defector's new faction)? This is the patronage cascade the inspiration document identified — but it emerges from the RP system rather than being specified as a separate mechanic.

---

## P-7 REVISED: Settlement Resilience as Dynamic Response, Not Static Score

### What was wrong

Static score. Computed once, applied as passive modifier. No context sensitivity.

### Revision

**Resilience is tested by specific stressors, and the response depends on the stressor type.** Different threats interact differently with a settlement's interpersonal network.

**Military threat (hostile force targets the settlement):**
- Resilience test: Governor's Charisma pool vs Ob = attacker's Military ÷ 2. Success = local NPCs contribute to defense (settlement Defense +1 for the battle). Failure = local NPCs flee or capitulate (settlement Defense −1).
- **Diagonal interaction:** If the governor has RP ≤ −3 with the faction's military commander (P-1), the military commander delays garrison reinforcement. The delay gives the attacker a free round. This is not an abstract modifier — it's a specific consequence of a specific NPC-NPC relationship producing a specific military outcome.

**Subversion threat (enemy intelligence targets the settlement via P-6):**
- Resilience test: Governor's Cognition pool vs Ob = attacker's Intel. Success = the intelligence operation is detected (counter-intelligence). Failure = the operation proceeds undetected.
- **Feedback loop:** A successful counter-intelligence detection reveals the *source* of the operation. The governor can report to the faction leader, providing Tier 1 intelligence about the attacker's intelligence priorities. This intelligence feeds back into the faction's own Tier 2 operations.

**Political threat (rival faction attempts to flip the settlement's allegiance via diplomatic pressure):**
- Resilience test: Governor's average local NPC Disposition vs Ob = rival faction's Influence ÷ 2. Success = local NPCs reject the overture. Failure = local NPCs consider the offer.
- **Downward ripple on failure:** If the local NPCs consider the rival faction's offer, a new Scene Slate event fires: a local NPC approaches the player (or governor) and says "The [rival faction] is offering better terms. Why should we stay with [current faction]?" This is a personal-scale scene generated by a faction-level action targeting a settlement-level actor. The player must resolve it through social engagement — Negotiate, Connect, or Contest — not through a stat modifier.

**Upward ripple from all tests:** Every resilience test result feeds back to the faction level. A settlement that successfully resists a threat generates a report to the faction leader that increases the faction's effective Stability by +0.5 at Accounting (institutional confidence). A settlement that fails generates a report that decreases it by −0.5.

---

## P-8 REVISED: Governor Drift as Political Ecosystem Effect

### What was wrong

Linear accumulation. Deterministic threshold. The governor's Conviction acts on the settlement in isolation.

### Revision

**Governor drift operates through the settlement's NPC network, not as a direct stat modifier.**

The companion-governor doesn't impose their Conviction on the settlement — they *influence local NPCs* whose behavior then shifts the settlement's character.

**Each season, the companion-governor's Conviction interacts with each local NPC's Conviction:**

| Overlap | Effect |
|---|---|
| Same primary Conviction | Local NPC's Disposition with governor +1 (per-season, caps per Bonds). This NPC becomes an ally of the governor's approach. |
| Adjacent Conviction (shares one of the 7 types) | No shift. The NPC tolerates the governance approach. |
| Opposed Conviction | Local NPC's Disposition with governor −1 (per-season, floor at −3). This NPC becomes a friction source. |

**What this produces laterally:** Over 3–4 seasons, the settlement's local NPC network splits into pro-governor and anti-governor groups. The pro-governor NPCs provide governance support (+1D to governance actions). The anti-governor NPCs obstruct governance (+1 Ob). The settlement's effective governance becomes a function of the governor's local political success, not just their attribute scores.

**Upward ripple:** The anti-governor NPCs may generate information that reaches the controlling faction's leader. If 3+ local NPCs are at Disposition ≤ −2 with the governor, the faction leader receives a notification at Accounting: "Governance friction in [settlement]." The faction leader evaluates: reassign the governor (disrupting the player's companion deployment) or tolerate the friction (accepting governance inefficiency). This is a faction-level decision driven by settlement-level interpersonal dynamics.

**Diagonal interaction with P-5:** If the companion-governor's Conviction is aligned with a rival faction's Framework, the anti-governor local NPCs may approach the rival faction independently. An opposed-Conviction local NPC at Disposition −3 with the governor generates a 20% chance per season of reaching out to the rival faction whose Framework matches their Conviction. This is an NPC-initiated cross-faction contact — the settlement is generating its own political dynamics without player involvement.

---

## EMERGENCE: How Proposals Interact

The revised proposals don't operate in isolation. They share inputs and outputs that create emergent political dynamics.

### Scenario: The Treaty That Broke the Court

**Season 1:** Player (Crown, Standing 4) signs a military alliance with Varfell. Treaty Conviction Cascade (P-3) fires. Crown inner-circle NPCs evaluate:
- Marshal (Order): Alignment +1 (military strength serves order). RP +1 toward player.
- Confessor (Faith): Alignment −2 (Varfell's Consequentialist framework is antithetical to Divine Command). RP −2 toward player.
- Spymaster (Autonomy): Alignment +1 (intelligence sharing opens new operations). RP +1 toward player.

**Season 2:** Confessor (Alignment −2) uses P-1 Inform action: approaches the Chancellor (Precedent) with concerns about the alliance. Chancellor evaluates: treaty contradicts precedent (Crown has no prior alliance with Varfell). Chancellor's RP with player shifts −1. Confessor and Chancellor form a Bloc (P-1). Bloc applies +2 Ob to the player's next Domain Action that implements the treaty.

**Season 3:** Player's treaty implementation Domain Action fails (the +2 Ob was decisive). Failed Domain Action costs Crown Stability −1 (PP-403). Stability drop approaches succession anxiety conditions (P-4). Almud's Succession Filter activates — NPCs begin evaluating successors. Torben's Conviction alignment becomes relevant. NPCs shift RP based on Torben's likely policies.

**Season 4:** Varfell detects (via Tier 1 intelligence) that the Crown court is divided over the alliance. Varfell's AI priority tree adds "exploit Crown division" as secondary priority. Vaynard initiates Tier 2 Influence targeting the Confessor — not to recruit them, but to deepen their alienation from Almud, hoping the Confessor will obstruct Crown military cooperation so severely that Varfell can renegotiate better terms.

**Season 5:** The Confessor, now at RP −4 with the player and Disposition −1 with Almud, generates an Outreach scene demanding the player explain why they prioritized a Varfell alliance over Church interests. Meanwhile, the player's companion-governor in a Crown settlement near the Varfell border (P-8) has been drifting toward Reason Conviction. Local Faith-aligned NPCs are reaching out to the Church.

None of this was pre-scripted. It emerged from the interaction of P-1 (NPC Regard), P-3 (Treaty Cascade), P-4 (Succession), P-6 (Intelligence), and P-8 (Governor Drift), each feeding outputs into the others' inputs.

### Scenario: The Settlement That Defected

**Season 1:** Player assigns a Reason-aligned companion as governor of a Church-controlled settlement (P-8). Governor begins building Disposition with local NPCs.

**Season 3:** Governor has Disposition +3 with 3 Reason-aligned local NPCs, Disposition −2 with 2 Faith-aligned local NPCs. Settlement is politically split along Conviction lines.

**Season 4:** Faith-aligned local NPCs (Disposition −2 with governor) reach out to the Church (P-8 diagonal interaction). Church learns that a Crown-controlled settlement has a governor whose Conviction contradicts Church interests. Church initiates Tier 2 Influence targeting the Faith-aligned local NPCs — not to recruit them, but to encourage them to resist the governor's policies.

**Season 5:** Church-influenced local NPCs begin obstructing governance (+1 Ob to governance actions). Settlement Order declines. The Order decline triggers a Settlement Event (fieldwork §4.3): local revolt risk at Order 0. The player must intervene personally (Scene Slate Priority 1 if Order reaches 0) or reassign the companion-governor.

**Season 6:** Player intervenes personally, discovers (via Read action) that the local NPCs' resistance is being amplified by Church influence operations. Player now faces a multi-layered decision: confront the Church (diplomatic incident that feeds P-3 Treaty Cascade), replace the governor (losing settlement investment), or attempt to Reconcile the local NPC factions (social engagement that might fail, consuming scene actions they need elsewhere).

**What this demonstrates:** A companion assignment decision (personal scale) created a settlement-level political split (settlement scale), which attracted cross-faction intelligence attention (faction scale), which produced governance failure (settlement scale), which generated personal-scale scene content (personal scale). The dynamic moved personal → settlement → faction → settlement → personal. Genuinely diagonal. No single proposal produced the outcome — it emerged from P-1 + P-6 + P-7 + P-8 interacting.
