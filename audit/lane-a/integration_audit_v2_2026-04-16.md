# VALORIA — Integration Audit v2: Player-World Connection
## Critique and Revision of the First Audit, the Integration Proposal, and All Referenced Documents
## Date: 2026-04-16

---

# CRITIQUE OF THE FIRST AUDIT

Before presenting the revised proposal, an honest account of what the first audit got wrong is warranted. The revised document is substantially restructured as a result.

**What the first audit failed to do:**

The first audit presented itself as a critique of the integration proposal but was actually an extension of it — Part 1 ("What the Integration Proposal Gets Right") listed only things to protect. A real audit must identify structural failures in the proposal it is examining, not just affirm them. This audit does that in Part 0.

The first audit produced a companion specification with mechanical gaps: combat command timing conflicts with combat_v30's priority table (Priority 1 = Strike, not "Issue Commands"); companion departure was tied to "Disposition below 0" which is vague against a −4 floor; Community Weaving for non-practitioners used Charisma to drive Spirit-gated Thread operations, which violates the existing gate system; the Knot-strain model for companion departure was unresolved against PP-632.

The Founded Organization pathway was built on the IC-1 proposal (NPE Coalition embryo) from the comprehensive audit — a non-canonical proposal cited as if canonical. A three-stage progression was presented as linear when Stages 2 and 3 could fire simultaneously. The relationship between the Founded Organization and the existing Standing track in faction service was acknowledged but not resolved.

The scene trigger taxonomy mixed three distinct trigger types — World Zoom In triggers (world-state events generating scenes), Character Arc triggers (character-state events), and End-State triggers (game-conclusion events) — into one undifferentiated numbered list. Triggers 12, 15, and 25 are categorically different from the others and were incorrectly grouped.

The Domain Echo extended table proposed new Echo outputs without addressing the seasonal cap interaction or confirming whether new sources stack against the existing ±2/season/stat ceiling. Several rows in the table described effects using non-canonical stats ("Faction Intelligence" as a separate resource) not currently in the World State Model.

The non-standard actor protocols were inconsistent in depth: the Ministry received three engagement routes and full scene graph architecture; the Restoration Movement received one paragraph. This inconsistency is not just aesthetic — it means the RM protocol is insufficient for implementation while the Ministry protocol is overspecified.

The Three Presence Rules — the document's most important design insight — appeared in Part 7.2, the penultimate section, when they should be the document's load-bearing premises, stated first.

The Appendix on faction formation made an assertive design judgment ("kingmaker is better than king") that should be a design decision for Jordan, not a directive from the audit.

**What the first audit got right:**

The Universal Actor Engagement Architecture framing is correct. The companion as immersion engine is correct. The non-standard actor gap identification is correct. The Scene Slate expansion need is correct and the taxonomy, though miscategorized, is mostly sound. The engagement protocols for Ministry, Guilds, Niflhel, and Wardens are directionally correct and only need mechanical resolution. These are retained, corrected, and deepened in this revision.

---

# PART 0: CRITIQUE OF THE INTEGRATION PROPOSAL

The integration proposal is the project's finest document, but it has three structural problems that this audit must address directly.

**Problem 1: The Scene Slate/Scene Graph unification (B-2) is underspecified.**

The proposal correctly states that "the Scene Slate is the generation system; the Scene Graph is the delivery format; they are two phases of the same mechanism." But it doesn't specify the transition rule: when the player selects a Scene Slate entry and it instantiates a Scene Graph, what governs which graph template is used? The World State Model at the moment of selection contains enough information to determine context (territory, NPCs present, active investigations, Exposure level) but the template-selection algorithm is unspecified. Without it, Scene Slate entry selection produces either a random graph or requires hardcoded one-to-one mappings between entry types and graph templates — neither of which is correct. The entry type (from the five priority levels) must map to a graph template family, with the specific instantiation determined by current world state. This mapping needs to be formally specified.

**Problem 2: The Dialogue Lattice → Social Contest handoff (B-3) addresses transition but not coexistence.**

The proposal specifies what state carries across from a completed Lattice session into a Contest (Conviction Wound count, Disposition offset, Evidence preload, Momentum). What it doesn't address: what happens when a Contest becomes necessary mid-Lattice — when the escalation trigger fires during an exploratory conversation that hasn't reached its natural close? The Concentration and Composure of both parties at the moment of escalation must be tracked and carried. The NPC's Composure entering the Contest is not full if the Lattice session has already been running for three nodes. This is the most common case — most escalations happen after extended conversation, not at the opening — and the handoff is only specified for the cold-start case.

**Problem 3: The Stature-Scaled Domain Echo (DE-I from the comprehensive audit) interacts with the ±2 seasonal cap in an unspecified way.**

At Standing 4, "Success outcomes generate ±2 instead of ±1." At Standing 5, "Overwhelming outcomes generate ±3." But the integration proposal also specifies a ±2 per-season per-stat cap on Domain Echo. A Standing 5 player generating a ±3 OW Echo in a season has already exceeded the cap from a single action. Either the Stature-Scaling overrides the cap (the intent, but unstated), or the cap applies and the Stature-Scaling is never realizable at OW level, or the cap is per-action rather than per-season (which would be a revision to the integration proposal). This interaction must be resolved.

**Resolution to Problem 3:** The cap is per-season, per-stat, cumulative across all Echo sources from one character. Stature-Scaling does not override the cap. Instead, Stature-Scaling increases the probability of reaching the cap from fewer actions: at Standing 4, a single OW action can alone exhaust the seasonal capacity; at Standing 5, it overflows by 1 (which is simply lost). This preserves the cap's purpose (personal actions shouldn't dominate the faction layer) while giving high-Standing characters genuinely larger individual-action impact.

---

# PART 1: FOUNDATIONS — THE THREE PRESENCE RULES

All systems proposed in this document are derived from three premises. They are stated first, not last.

**Rule 1 — Every institution has a face.**

No Domain Action resolves, no clock advances, no political event fires without a person attached to it in the player's experience. The Ministry's obstruction is an officer. The Guild's leverage is a guild leader with a named conviction. Niflhel's intelligence package is an intermediary who exists physically in the world. This is not simulation overhead — it is the game's central metaphysical claim (P-03: rendering is consciousness-performed) made into a design principle. The player doesn't fight abstractions. They argue with people.

**Rule 2 — Every consequence has a scene.**

Domain Echo fires as a stat change. That stat change is anchored to a witnessed or reported event. The integration proposal's "Witnessed Layer / Reported Layer" distinction is correct: the player either was in the scene that produced the change, or they receive a human-terms report of what happened in their absence. "Baralta used the evidence you delivered. Himlensendt's motion failed." The world didn't just update — something happened, and the player knows who made it happen and why.

**Rule 3 — Every actor has a tempo.**

Worldly actors are present throughout the season, not only at Accounting moments. A Schoenland trader visits port territories quarterly. A Ministry officer processes applications on a cycle the player can discover through Research. A Warden patrols between Gap sites on a schedule discoverable through Surveil in Southernmost-adjacent territories. The discovery of an actor's tempo is investigative information. Using that tempo — being in the right place when the window opens — is the game's primary skill expression at the personal level.

These three rules govern every specification that follows. Any proposed mechanic that satisfies all three rules is implementable and immersive. Any mechanic that violates one should be revised until it doesn't.

---

# PART 2: THE UNIFIED RELATIONAL ARCHITECTURE

The first audit proposed the Companion Specification and the Player Network Formation pathway as separate systems. They are not separate. They are the atom and the molecule of the same system: the player's relational life. A companion is the deepest individual relationship. A network is what multiple such relationships produce when they share direction. A founded organization is what a network becomes when it reaches critical mass. This part specifies all three as one architecture.

## 2.1 The Companion — Formal Specification

**Definition.** A companion is a Knot-bonded NPC who has accepted a co-travel invitation. The Knot (PP-632) is the prerequisite: it requires the player's Disposition with the NPC to reach floor(Bonds/2)+1 — a genuine, sustained relational investment. The co-travel invitation is a distinct social action using the existing Negotiate mechanic (Attunement pool, Ob governed by the NPC's active Beliefs and Conviction alignment with the player's arc). A refused invitation is not failure — it is the NPC's character expressing itself, and it updates the NPC's arc vector.

**Capacity.** The player can maintain at most floor(Bonds/2) active co-traveling companions simultaneously (not floor(Bonds/3)+1 as previously proposed — this revision aligns the formula with PP-632's existing floor(Bonds/2)+1 Disposition ceiling, using the same base with a −1 offset to reflect the greater load of co-travel vs. friendship). At Bonds 2: 1 companion. At Bonds 4: 2 companions. At Bonds 6: 3 companions.

**The action economy resolution.** The first audit was correct that companions don't consume the player's scene action budget. The reconciliation with fieldwork_v30 §3.2 (multi-character exploration rules) is: a companion is an assistant in the §3.2 sense when they are performing investigation actions. The same rules apply — companion rolls at Ob+1 to assist the player's lead; companion success adds +1 to the player's net successes; companion failure adds +1 Exposure for both. The Companion Scene Contribution (CSC) table from the first audit is not a separate mechanic — it is a categorization of which §3.2-compatible assistant actions the companion performs based on their Conviction. Naming the CSC type doesn't change the underlying resolution. This eliminates the redundancy identified in the critique.

The table below maps Conviction to likely CSC choice and the underlying mechanic it invokes:

| Conviction | Default CSC Choice | Underlying Mechanic |
|---|---|---|
| Faith | Contest Corroboration (affirms moral position) | social_contest_v30 §4 Step 2b |
| Order | Watchkeeping (maintains security posture) | fieldwork_v30 §6 (Exposure reduction) |
| Reason | Assist Investigation via Knowledge Contribution | fieldwork_v30 §3.2 assistant role |
| Equity | Social Access (leverages their community relationships) | fieldwork_v30 §5.1 Disposition offset |
| Autonomy | Combat Support (keeps options open physically) | combat_v30 named NPC rules |
| Continuity | Thread Assist (maintains the work of the substrate) | threadwork_v30 collective ops |
| Precedent | Assist Investigation via Research | fieldwork_v30 §3.2 assistant role |

**Combat command timing — resolved.** The first audit proposed "Issue Commands at Priority 1." Combat_v30 §4 specifies that Priority 1 = Strike in the action priority table. These are incompatible. The resolution: companion combat commands are declared during **Phase 1 (Strategy Declaration)** — the simultaneous secret declaration phase that precedes all action resolution. This is not an action priority; it is the planning phase. The player writes their command alongside their Offense/Defense split declaration. On the companion's turn within the round, the companion attempts to execute the command. Ob 1, Charisma-primary. Success = companion executes. Failure = companion follows their Conviction's combat instinct. No action slot consumed; only the declaration phase used.

**Companion departure — resolved.** The first audit's "Disposition below 0" trigger was vague. The correct mechanic: companion departure triggers when Disposition drops by 3 or more through **Belief-contradiction events specifically** (not general social friction, not successful social actions, not normal Disposition decay). Belief contradiction is defined as: the player takes an action that directly and visibly serves a goal opposed to the companion's active Belief. Each such action is a Belief-contradiction event. Three cumulative events = the companion initiates a leave scene. The scene is a Social Contest (private negotiation type, Attunement adjudicator, 1 exchange) where the player can attempt to explain their reasoning. Contest win: companion stays, Disposition resets to +1, their Belief revises to acknowledge the conflict. Contest loss: companion leaves.

**The leave scene and the Knot — resolved.** PP-632 establishes Knots as constitutive. A companion leaving does not sever the Knot — it strains it. Each Belief-contradiction event adds +1 Knot strain (per the existing strain model in fieldwork_v30 §2.6). At Knot strain 5, the companion's co-travel becomes unavailable (the relational load exceeds capacity) but the Knot persists — the relationship remains real, just non-co-traveling. Strain reduces by 1 per season of non-exploitation. If the player Mends the relationship through deliberate Disposition investment over 2 consecutive seasons, strain resets to 0 and co-travel can be re-offered. Companion death adds +2 Knot strain permanently (the constitutive bond now connects to an absence) and imposes Coherence −1 as the player's rendering processes the loss.

## 2.2 The Network — From Atom to Molecule

A Network is not designed — it emerges. The player does not decide to build a network; the game recognizes when the player's relational pattern has produced one. The recognition threshold and its consequences are specified here.

**Network recognition condition.** The player has: (a) at least two active companions, AND (b) at least two additional named NPCs (not companions) with Disposition ≥ +2, AND (c) all four or more NPCs share at least one Conviction alignment with the player's dominant Belief theme (derived from the existing Belief tag structure). When all three conditions hold simultaneously, the player's relational cluster constitutes a recognized Network.

**What recognition produces.** Recognition changes two things. First, the Scene Slate Priority 3 (Belief-aligned) slot now generates at least one Network scene per season — a scene that reflects the network's collective activity rather than any single NPC's arc. These scenes feel different from individual social scenes: they have multiple NPE-generated minor NPCs in addition to the player's network members, producing the texture of a community rather than a dyad. Second, the player's Domain Echo from personal actions touching the Network's shared Conviction carries the Standing modifier one tier higher than the player's actual Standing — as if the player were Standing 1 above their current level, for Echoes in the Network's domain only. This represents the multiplier effect of collective relational capital.

Network recognition is not permanent. If any of the three conditions lapses (a companion leaves, a key NPC's Disposition drops below +2, the Belief theme diverges), Network status dissolves until the conditions are re-met.

## 2.3 The Founded Organization — From Molecule to Institution

A Founded Organization is what a Network becomes when it produces the world's recognition. It requires three conditions to be met simultaneously — all three, not just one or two:

**Condition A (Evidence):** The player has completed a Structural-threshold investigation (Evidence Track 8) whose subject directly concerns the Organization's founding purpose (the shared Conviction theme of the Network).

**Condition B (Territory):** At least one territory has ≥ 3 Network-member NPCs with Disposition ≥ +2. This territory becomes the Organization's home territory.

**Condition C (Duration):** The Network has been continuously recognized (per §2.2) for three consecutive seasons.

**Why these three and not others:** Evidence demonstrates that the player has actually understood the domain they're organizing around — not just assembled friends. Territory demonstrates physical presence in the world — organizations don't exist only in minds. Duration demonstrates commitment — not a temporary cluster of relationships but a sustained pattern.

When all three conditions are met, the Founded Organization formal status activates.

**What the Founded Organization receives:**

One Domain Action per season from a restricted list based on founding Conviction. This is a new Domain Action capability — not derived from any existing faction card, but using the same resolution mechanics (pool = relevant Network attribute, Ob = standard table):

| Founding Conviction | Available Domain Actions |
|---|---|
| Reason | Survey (fieldwork_v30 §8.1), Tribune Investigate (existing) |
| Equity | Organize (Community Weaving at territory scale — see §3.6), Rumour at territory scale |
| Order | Fortify (limited: Fort +1 in home territory only), Govern (home territory only) |
| Faith | Piety Assertion (Assert-equivalent, targeting home territory only, not TC) |
| Autonomy | Tribune Spy (existing, against one faction per season) |
| Precedent | Senator (limited: Rebuttal action only, no Parliament initiation) |
| Continuity | Mending at territory scale (Thread operation; requires at least one practitioner in the Organization) |

**Mandate track (0–3):** Derived from collective Disposition weight. Each Network member at Disposition ≥ +2 contributes 0.5 to Mandate (round down, minimum 0, maximum 3). The Mandate track uses the same mechanics as faction Mandate for Parliament purposes only when the motion directly concerns the Organization's domain. An Equity-based Organization can vote on motions affecting common population welfare. A Reason-based Organization can vote on intelligence-related motions. Mandate does not grant the Organization standing to propose motions (Mandate ≥ 2 required for Parliamentary Motion; an Organization at Mandate 3 can propose if the motion is domain-aligned).

**The Standing-to-Organization relationship — resolved.** A player can simultaneously hold Standing in an existing faction AND operate a Founded Organization. They are not mutually exclusive. However, the Domain Action from the Organization and the Domain Actions from faction Standing are separate: the Organization's action is personal-scale (requires player involvement); the faction's Domain Actions proceed through the faction's card hand independently. In Parliament, the player contributes votes both from their faction's Mandate (if Standing 3+, per Agency System §5) and from their Organization's Mandate (if the motion is domain-aligned). These are additive only if the player is present in the territory and the Organization vote is officially registered by a Senator action the previous season.

**The ceiling — stated as a design decision, not an assertion.** Whether a Founded Organization can achieve Universal Victory is a choice Jordan must make. The case for *yes*: it is consistent with the philosophical premise that legitimate governance emerges from genuine relationships, not institutional succession. A player who builds enough relationships, enough investigations, enough genuine territorial presence should be able to govern. The case for *no*: a founded organization at Mandate 0–3 cannot realistically contest Crown (Mandate starting ~4–6), Church, or Hafenmark; the victory would require 15+ seasons of intense play and would crowd out every other narrative. The mechanics currently make it possible but structurally difficult. The design recommendation is to leave it possible and not advertise it — an easter egg for the most dedicated relational play styles, not a designed primary path.

---

# PART 3: NON-STANDARD ACTOR PROTOCOLS

Each actor in this section follows a consistent format: **Actor Definition → World State Model (reads/writes) → Access Tiers → Scene Slate Generation → Companion Candidacy → Domain Echo Outputs → Interdependency Declarations.**

This consistency was absent in the first audit and is the primary structural improvement in this revision.

## 3.1 The Ministry

**Actor definition.** The Ministry is the peninsula's civil service — institutional friction between political will and execution. It has no factional loyalty beyond procedural integrity. It serves whoever exercises legitimate authority, which means it serves everyone and therefore truly serves no one. Its one distinctive ability is the Procedural Objection, which can delay any faction's Domain Action for one season at Mandate cost.

**World State Model.** Reads: Controlling faction Mandate per territory (T1 primary). Writes: Domain Action delay (existing mechanic). No new tracks.

**Access tiers:**

*Tier 0 — Public Service (no condition):* Any character can request Surface/Settled depth (Depth 0–1) records from a Ministry office in any Crown-controlled territory. Research action per existing fieldwork rules, Ob per Depth table. No faction alignment required. No Standing required. The Ministry is a public institution.

*Tier 1 — Restricted Access (Disposition +1 with any Ministry officer NPC):* Hidden depth (Depth 2) records accessible. Interview action to establish officer relationship. Starting Ministry officer Disposition: faction Standing /2 rounded down (Crown Standing 4 = officer starts Disposition +2; independent Standing 0 = officer starts Disposition 0). Disposition +1 is achievable in one season through sustained Converse actions.

*Tier 2 — Classified Access (Disposition +2 with a PAL 2+ officer):* Buried depth (Depth 3) records accessible. PAL (Procedural Access Level) is an officer attribute from 1 to 3, invisible at first encounter. PAL is discovered through: (a) Surveil of the officer's office patterns (PAL visible as scene node label after Surveil Success), (b) Research in the archive revealing the officer's title and authority level (Ob 1), or (c) companion's Knowledge Contribution if companion has any administrative History. This resolves the catch-22 identified in the first audit's critique.

*Tier 3 — Ministry Alliance (Completed Complex investigation revealing Ministry corruption/inefficiency + presented to PAL 3 officer):* Generates the "Ministry Internal Reform Pressure" arc vector. The player gains permanent Procedural Access equivalent to Tier 2 without per-scene Disposition requirements. The Tier 3 officer becomes a named NPC with Conviction Wound 1 (Order conviction strained by the evidence of institutional failure). One Procedural Objection per season can be directed by the player's request.

**Scene Slate generation.** Ministry Procedural Obstruction → Priority 2 (Duty-aligned: the blocked Domain Action was presumably the player's faction's interest). Ministry records relevant to active Belief → Priority 3 (Belief-aligned, generated when active Belief tags reference institutional, legal, or historical subjects). Clean-season consolidation → Priority 5 (ambient: a Ministry courier delivers routine documentation the player can ignore or examine).

**Companion candidacy.** PAL 3 Ministry officer: Disposition ceiling floor(Bonds/2)+1 (standard). Conviction typically Order (primary) and Precedent (secondary). Companion value: Knowledge Contribution on legal, administrative, and historical topics; Watchkeeping in institutional spaces.

**Domain Echo outputs.** Buried-depth evidence delivered to faction: +1 Faction Influence (existing Echo row, confirmed appropriate). Ministry Alliance (Tier 3): cancels one Procedural Objection against the player's faction per season — equivalent to −1 Ob to one Domain Action, which is a standing +1D effect on that action.

**Interdependencies.** Ministry records are the primary source of Documentary evidence at Depth 2–3. Documentary evidence carries the "can be presented in Church Tribunal" reliability tag (fieldwork_v30 §4.3) — unlike Thread-verified evidence, which cannot. Ministry access is therefore strategically valuable specifically for Church-related investigations, as it provides admissible evidence the Church cannot dismiss on methodological grounds.

## 3.2 The Guilds — Individual Leaders

**Actor definition.** The Guildmaster Council is a collective with emergent Moral Relativism behavior (npc_behavior_v30 §2.11). Individual guild leaders are distinct sub-NPCs with their own Conviction triangles. Approaching "the Guilds" abstractly produces Consequentialist/economic responses. Approaching a specific guild leader produces individuated Conviction engagement.

**World State Model.** Reads: Territory Prosperity, faction Wealth, active Trade routes (geography_v30). Writes: Guild Favour (a personal-scale relationship token, not a formal clock — specification below). No faction stat changes from personal engagement alone; faction stat changes only through Domain Echo at sufficient scale.

**Guild Favour clarification.** Guild Favour is not a formal tracked value in the clock registry. It is a relationship token — a named, specific institutional debt. Each token names: the guild domain, the service rendered, and a two-season expiry. At expiry, the token dissolves. There is no decay track — the token exists or doesn't. The player's journal tracks active tokens. This resolves the "floating non-clock track" problem identified in the critique.

**The five guild leader templates:**

| Domain | Territory Presence | Primary Conviction | Compromise Profile | Unique Offer |
|---|---|---|---|---|
| Maritime | Port territories (T8, T3, T1) | Autonomy | Economic (primary), Informational (secondary) | Navigation routes, cargo schedules, harbor access |
| Textile & Agricultural | Rural territories (T6, T11, T13) | Equity | Economic (primary), Personal (secondary) | Supply chain data, harvest information, rural NPC introductions |
| Arms & Metals | Military-adjacent territories (T14, T12, T9) | Order | Economic (primary), Informational (secondary at Disposition +2) | Equipment outside normal acquisition, contract intelligence |
| Scholarly & Archive | Capital and church territories (T1, T9) | Reason | Informational (primary), Economic (secondary) | Archive access at Depth 2 Ob −1 (complements Ministry Tier 1) |
| Shadow | City territories (any major settlement) | Autonomy | Informational (primary), Economic (secondary) — never Personal | Gray-market intelligence; see Niflhel crossover below |

**Access.** Guild leaders are Drift NPCs on seasonal schedules (discoverable via Surveil in their primary territory). Once located: standard fieldwork Socializing (Connect/Negotiate). Guild leaders' starting Disposition: 0 for any player character by default, +1 if the player's faction has Wealth ≥ 3 (commercial familiarity), −1 if the player is known to have recently opposed commercial interests.

**Guild Favour activation.** A Negotiate action (Attunement pool, Ob = floor(guild leader's highest stat / 2) + 1) where the player declares an offer that matches the guild leader's Compromise Profile. On Success: Guild Favour token issued. On Overwhelming: Favour token + the guild leader enters the named NPC pool for this territory (becomes an Anchor NPC for future sessions). On Failure: Favour token not issued; Disposition −1 (the offer was wrong and revealed the player's misunderstanding of what the guild leader values). The guild leader's Compromise Profile condition must be met: offering money to the Shadow guild leader (who values information, not money) fails regardless of offer magnitude.

**Guild Favour uses.** A held Favour token can be spent in one of three ways: (a) +1D to a Trade Domain Action in the token's guild domain territory; (b) Parliamentary Endorsement — the token shifts one vote's worth of Mandate toward the player's faction's position in any motion touching commercial interests; (c) Evidence of consortium — a Guild Favour token is admissible as Testimonial evidence in any Social Contest where commercial interests are relevant (+1D to the Argue roll for one exchange when presented).

**Scene Slate generation.** Commercial disruption in a guild domain territory (Prosperity ≤ 1, ongoing Blockade, or recent military battle) → Priority 2 (Duty-aligned if player's faction has trade interests) or Priority 3 (Belief-aligned if player has a Belief touching economic justice or commercial access). Guild leader passing through current territory → Priority 4 (Territorial: an opportunity to engage without seeking them out). Guild Favour token nearing expiry (one season before expiry) → Priority 5 (ambient: "the guild's patience is limited").

**Companion candidacy.** Any guild leader: reachable at Disposition +3 maximum (Compromise Profile never reaches Personal except Textile/Agricultural secondary; Knot formation requires Disposition floor(Bonds/2)+1 which may exceed what commercial relationship can reach). Most likely companion candidate: Scholarly & Archive (Reason conviction, investigative utility) or Shadow (Autonomy, covert operation utility).

**Domain Echo outputs.** Guild Favour token spent on Parliamentary Endorsement: shifts vote weight, which is territory-scale (not faction-stat), not subject to ±2 Echo cap. Favour token spent on +1D Domain Action: not an Echo — it's a pool modifier. No Domain Echo from Guild engagement alone; Echo fires only if guild engagement produces evidence (investigation) or Conviction Wound (social contest) that has Sufficient Scope.

**Interdependencies.** Shadow guild leader overlaps with Niflhel Tier 1 access: the same tavern contact point may serve as entry to either network. The shadow guild leader's information brokerage operates in the same gray market. The key distinction: Shadow guild leader trades public-ish commercial intelligence; Niflhel trades operational covert intelligence. A player who has built Shadow guild trust and attempts a Niflhel Tier 1 approach in the same territory gets −1 Ob on the Rumour action (familiar with the social infrastructure). Conversely, a player who has burned their Niflhel relationship in a territory gets +1 Ob on Shadow guild leader engagement there (Niflhel has flagged them as problematic and the shadow market has noted it).

## 3.3 Niflhel as Service Network

**Actor definition.** Niflhel is simultaneously a playable faction, an NPC faction, and a service network that operates regardless of who is "in charge." The four-arm structure (from the npc_behavior_v30 §2.12) means no single actor controls the whole. A player engaging Niflhel as a service is engaging one arm's commercial operation, not the institutional whole.

**World State Model.** Reads: Territory Exposure levels, faction Intel stats, player character Exposure. Writes: faction Exposure (when services leak), Intel (for the purchasing faction), Niflhel Arm records (player-character entry added on Tier 2+). No formal stat changes from personal engagement alone.

**Niflhel service tiers:**

*Tier 0 — Awareness:* The player knows Niflhel exists and operates in the city. This requires either (a) Tribune Spy action Success or Overwhelming revealing Niflhel presence, (b) a companion with any relevant History (streetwise, criminal, intelligence), or (c) a completed Simple investigation (Evidence Track 3) on any subject touching city information networks. No contact yet — only knowledge.

*Tier 1 — Contact Point:* Rumour action (Charisma pool, Ob 2 in any city territory) produces a contact location — an Evidence node in the city's scene graph. Approaching the contact location is a scene, costing 1 scene action. The contact is an intermediary (not an Arm Leader) with Genome: Autonomy-convicted, Compromise Profile: Economic and Informational, Disposition 0 toward all known parties. No service is purchased at Tier 1 — only the contact is established. The player learns the correct approach protocol (what to ask for, what currency is accepted). This prevents naive approaches that would cause the contact to disappear.

*Tier 2 — Brokerage:* Requires two prior visits to the Tier 1 contact without triggering the contact's Priority 6 (Exposure containment) response. On the third visit, a service menu becomes available:

| Service | Payment (choose one) | Mechanical Output | Exposure Generated |
|---|---|---|---|
| Intelligence Purchase | 1 Wealth (player's faction) | One Tribune Spy result equivalent: one faction's stat value revealed. Target faction must be in the same territory or adjacent. | +2 to player character in contact territory |
| Covert Access | 1 Wealth OR completion of a Minor favor (GM specifies: deliver a package, confirm a location, report on a third party) | −2 Ob on one Investigation or Stealth action in a specified territory for one season | +1 (the access has been arranged but footprint increases) |
| Disinformation | 2 Wealth OR genuine intelligence about a rival faction (value assessed by Niflhel; Documentary or Verified evidence required) | Target faction receives false Tribune Spy results next season (their Intel action returns incorrect stat values). Duration: 1 season. | +1 to player; +3 to the faction that will discover the disinformation eventually |
| Counter-Surveillance | 1 Wealth | −3 Exposure in current territory immediately. Clears one Noticed threshold's worth of Exposure. | 0 (the point is to reduce Exposure) |

**Domain Echo sacrifice payment — resolved.** The first audit proposed "Domain Echo sacrifice" as payment. This is mechanically fragile: Echo fires at Accounting, service is delivered immediately. The revision: the player signs a "debt obligation" at the service point, committing that at the next Accounting, one of their Domain Echo results (player's choice of which, declared at Accounting) will not produce its faction stat change — instead the value is absorbed by Niflhel as institutional resource (they receive the equivalent Mandate or Influence benefit that the player's faction would have). The temporal gap between service and payment is intentional: Niflhel extends credit but collects with certainty. If the player's Accounting produces no Echoes (a bad season), Niflhel applies the debt against the player's faction's Intelligence score (−1 Faction Influence for the faction the player serves, or −1 to the player's own Organization Mandate if independent). This makes the payment system have teeth.

*Tier 3 — Arm Contact:* Requires (a) five Tier 2 transactions in the same city without Exposure triggering Priority 6 against the player, AND (b) Niflhel record of the player as a reliable buyer (five transactions without counteroperations). An Arm Leader makes contact directly — not through the intermediary. The Arm Leader has a full named NPC Genome: Autonomy primary, Continuity secondary, Evidence and Consequence as Resonant Styles, Compromise Profile: Informational (primary, no limit), Economic (secondary). At Tier 3, assassination and covert extraction services become available (valued at 3–5 Wealth equivalent depending on target).

**Niflhel counter-operations against the player — specified.** When the player's investigation Evidence Track against Niflhel activities reaches Simple threshold (3) while they have an active Tier 2+ relationship, Niflhel's Priority Tree evaluates: Priority 6 fires (exposure containment). This generates a Priority 1 Scene Slate entry: the player's contact has gone cold — the tavern table is empty when they arrive. Pursuing the scene reveals the contact has been relocated. The player must either (a) abandon the Niflhel investigation (the contact reappears, the relationship continues), (b) continue investigating (the contact remains unavailable, Tier 2 access suspended for 2 seasons), or (c) attempt to reach the contact through a secondary route (Research or Surveil in the same territory at +2 Ob). This creates exactly the tension a covert information economy should produce: you can investigate Niflhel, but they will know you're doing it, and they will respond.

**Faction Niflhel vs. Service Niflhel distinction.** When Niflhel is a player-controlled faction (BG mode), the service network mechanics above are player-deployed. When Niflhel is an NPC faction, the service network mechanics above are the mechanism through which non-Niflhel players interact with the network. The service tiers survive under either condition — they describe the network's external face regardless of who controls the institutional core.

**Scene Slate generation.** Niflhel operation detected in player's territory → Priority 1 (crisis: who is Niflhel watching?). Tier 2+ contact opportunity → Priority 3 (Belief-aligned if Belief involves intelligence or covert operations). Niflhel debt collection approaching (next Accounting) → Priority 4 (territorial: ambient tension). Counter-surveillance sweep (Priority 6 fired) → Priority 1 (the world is reacting to the player).

**Companion candidacy.** Arm Leader: reachable at Tier 3. Most unlikely companion in the game — Disposition ceiling requires sustained reliable dealing over multiple seasons. Autonomy conviction creates constant tension in any scene where institutional loyalty vs. personal relationship is tested. Survival-first conviction means the companion will depart at the first sign that co-travel creates serious personal risk (three Belief-contradiction events come quickly for an Autonomy NPC traveling with an activist). This arc is deliberately designed as a high-difficulty, high-reward relationship, not a standard companion option.

**Interdependencies.** Niflhel service vs. Church Attention Pool: purchasing Covert Access to reduce Ob in a Church territory doesn't reduce the Exposure that feeds the Church Attention Pool — it reduces the Ob on the action itself, not the Exposure that action generates. Clarified: Counter-Surveillance service reduces Exposure directly (−3) and therefore does affect the AP if the reduction brings the player below the Watched threshold that would have fed the AP at next Accounting. Intelligence Purchase: the resulting intelligence is the player's faction's Intel property, not a formal faction stat entry. It is an investigation Finding (Reliability: Verified, tagged as Tribune-equivalent) that can be used as Corroboration in contests or as Casus Belli evidence.

## 3.4 The Wardens — Thread Competence as Currency

**Actor definition.** The Wardens are the Southernmost's Thread containment infrastructure. They have no political agenda, no institutional loyalty, and no interest in anything that doesn't affect the substrate's stability. Their only measure of a person is Thread competence and the discipline not to make things worse.

**World State Model.** Reads: MS, Thread Tension in Southernmost-adjacent territories, active Gaps (threadwork_v30 Gap registry). Writes: WR and WC tracks (defined below). These are new personal-scale tracks, parallel to Disposition but domain-specific.

**Warden Recognition (WR, 0–5) — formal definition:**

WR measures the Wardens' awareness of the player as a Thread practitioner of note. It is not Disposition — it is professional acknowledgment.

| WR | Advancement Condition | Effect |
|---|---|---|
| 0 | Default | Player is unknown; Warden NPEs in Southernmost-adjacent territories treat player as potential threat (Disposition 0, no information shared) |
| 1 | Player character survives 1 scene in a territory with Calamity Radiation (Proximity Rating ≤ 2) while having TS ≥ 15 | Wardens aware the player can sense Thread phenomena; Warden NPEs shift Disposition to +1 in Southernmost-adjacent territories |
| 2 | Player completes a Mending operation at Success or better at Depth 3+ **OR** completes a Structural investigation (Evidence Track 8) on Thread phenomena | Wardens recognize restorative practice OR analytical competence; WC track unlocks; WR 2 is accessible through non-Thread-op route for players below TS 30 |
| 3 | Player survives a Breach (Depth 5) encounter without Coherence loss **OR** sustains 3+ consecutive seasons of Thread operations without creating a Gap | Warden Cooperation becomes available; Edeyja's arc enters Assessment monitoring phase |
| 4 | Physical presence in Southernmost (T15) for at least 2 scenes; requires TS ≥ 30 | Edeyja's Assessment phase activates; a Warden will seek the player out as a Priority 4 arc event |
| 5 | Edeyja's personal Assessment: a dedicated Social Contest (Cognition adjudicator, Memory-primary genre, Thread-verified evidence required as Corroboration) — Success or better | Full recognition; WC 3 unlocks; teaching access granted |

**WR 2 non-Thread route — resolves the TS gap.** A player with TS < 30 cannot Mend. But they can complete a Structural investigation on Thread phenomena using Examine, Research, and Reconstruct — no Thread ops required. This route reaches WR 2 through analytical rather than operational competence, which is philosophically consistent: the Wardens recognize both types of practitioner engagement.

**Warden Cooperation (WC, 0–3) — formal definition:**

WC measures the operational relationship. Requires WR 2 to unlock.

| WC | Advancement Condition | Effect |
|---|---|---|
| 0 | Default (WR 2 unlocked) | Wardens share Gap location intelligence in regions the player is in (Priority 4 Scene Slate entries) |
| 1 | One successful joint Thread operation (player + Warden, either leading) | Wardens share proactive intelligence: Thread Tension accumulations and Niflhel activity in Southernmost territories |
| 2 | Three joint Thread operations across different territories | Full Cooperative Operations: a Warden joins as collective Thread operation assistant (threadwork_v30 collective rules); Warden's TS bonus contributes to collective pool |
| 3 | WR 5 + Edeyja's Assessment cleared | Partnership: Edeyja available as companion candidate; teaching access (TS +10 per scene, max 2 advances from Edeyja's instruction) |

**WC decay.** WC −1 if the player creates a Gap through Dissolution in any territory the Wardens maintain. The Wardens observe this through Thread-perception and it costs the relationship. WC does not advance above WR level — you cannot be a Warden partner before you are recognized as a competent practitioner.

**The Warden Deathwatch Arc.** If Warden count reaches 0 (all other Wardens killed or incapacitated, per Edeyja Arc C trigger in npc_behavior_v30) and the player has WC 3, the game generates a Priority 1 Scene Slate entry: Edeyja is the last Warden standing. The player can (a) become a Warden (accept responsibility for the Southernmost containment work — a permanent Belief must be written committing to this; the player's Domain Action becomes one Mending per season in T15 territory; this is the only way to pass the Warden organization to a new generation), (b) decline and witness Edeyja face the final stage alone (Edeyja Arc C completes as designed), or (c) recruit other practitioners from the Network or companions to form a new Warden cohort (requires three practitioner-capable NPCs at WR 2+, triggering a new Warden Emergence arc). This arc is not scripted — it is an emergent outcome of the player's Thread engagement history.

**Scene Slate generation.** Gap formation in any territory + WR ≥ 2 → Priority 1 (Warden emergency response scene). MS drops below a band boundary + WR ≥ 3 → Priority 1 (Edeyja mobilizes, player has access). WC 1+ maintenance → Priority 4 (Warden patrol intersects player territory — intelligence sharing opportunity). Edeyja Assessment activation (WR 4) → Priority 2 (the master-practitioner wants to evaluate you).

**Companion candidacy.** Edeyja: WC 3 required. The most competent practitioner alive (TS 75–80, Coherence 9). Companion value is extraordinary: Thread Assist at collective scale; her presence in Thread-sensitive territories provides ambient co-movement awareness (+1D to all Thread ops when Edeyja is present). Her companion arc is Continuity/Reason — the tension between her need to maintain the work and her gradual recognition that she cannot do it alone forever. She will depart if the player's actions consistently degrade MS (three Dissolution-based Gap formations while she is co-traveling). She will deepen her relationship if the player demonstrates sustained restorative practice over multiple seasons.

**Interdependencies.** WC track references in npc_behavior_v30 §8.5 (Varfell Priority Tree: "WC < 2") are now formally defined: Varfell's Warden-contact strategy targets WC 0–1 (before full cooperative operations). Varfell seeks Warden knowledge at a diplomatic level; the player's WC track represents individual-level Thread competence recognition, which is different from and complementary to Varfell's institutional Warden Recognition pursuit. A player who achieves WC 3 while also having Standing 3+ in Varfell creates an extraordinary intelligence advantage: they have access to both Warden Thread knowledge and Varfell's analytical apparatus — the combination that could produce a Structural investigation into the Southernmost's true nature.

## 3.5 The Restoration Movement Before Formal Emergence

**Actor definition.** Before the NPE Coalition emergence trigger fires (see §2.3 Condition B territory requirements), the Restoration Movement is not a faction — it is a social tendency in the population, a community memory, a shared grief. It has no Domain Actions, no Mandate, no formal organizational existence. Engaging it means engaging people, not institutions.

**The pre-emergence RM engagement pathway:**

Any player character can engage with RM-sympathetic communities through standard fieldwork Socializing actions. The character doesn't need a label, an affiliation, or a declaration. RM-sympathetic NPCs (generated by the NPE in territories with Piety ≤ 2, Equity/Continuity conviction weight ≥ 3) are available through standard contact. Their Compromise Profile typically includes Personal (they want genuine connection, not political transaction). The Sincerity Gate matters especially here: an instrumental approach to RM community members generates 37% failures at a higher consequential cost than usual — word spreads in close communities that someone is mining them for resources, and Disposition with all RM-sympathetic NPEs in the territory drops −1 if a Sincerity Gate failure occurs in public.

**Community Weaving for non-practitioners — resolved.** The first audit proposed Charisma-instead-of-Spirit for non-practitioners performing Community Weaving. This violates the Thread operation gate system: Thread operations require TS and Spirit. The resolution: non-practitioners performing Community Weaving are not performing a Thread operation. They are performing a **Cultural Practice action** — a new social fieldwork action distinct from Thread operations but producing an overlapping effect.

**Community Weaving (Cultural Practice variant):**

*Pool:* (Charisma × 2) + most relevant History + 3. This is the standard social fieldwork pool — it is correct because cultural practice is a social act.

*TN:* 7 (standard).

*Ob:* 3 + 1 per MS band below 60 (the substrate's instability makes collective resonance harder, paralleling how Calamity radiation adds Ob to other actions in high-distress territories).

*Effect on Success:* Territory Piety −1 (in the direction toward Thread-acceptance; this is distinct from the MS restoration that practitioner-led Mending produces). Accord +1 in the territory (the community feels heard, acted upon, collectively engaged).

*Effect on Overwhelming:* As Success + one NPE-generated community NPC permanently shifts Conviction toward Continuity or Equity (their worldview is genuinely moved by the collective experience).

*Church Attention Pool interaction:* Community Weaving generates +1 Exposure in Church-influenced territories (it is detectable) and +1 Church Attention Pool entry at Watched threshold (it is political). This is not suppressed or reduced — Community Weaving is a visible act of cultural resistance. The player accepts the detection cost.

*Practitioner-led Community Weaving:* When a practitioner (TS ≥ 30) leads Community Weaving, the same cultural practice rules apply AND the Thread operation rules fire simultaneously. The practitioner uses Spirit for their Thread operation resolution; the community's participation (non-practitioner) uses the cultural practice rules to add +1D to the practitioner's roll (the collective resonance supports the individual Thread operation). This means practitioner-led Community Weaving can both restore MS (Thread operation effect) and shift Piety (cultural practice effect) simultaneously — the most powerful single action available for RM-aligned play.

**Scene Slate generation.** Territory with Piety ≤ 1 + at least 3 Equity/Continuity NPEs present → Priority 3 (Belief-aligned for RM-sympathetic players). Community Weaving successfully completed → Priority 4 the following season (community asks the player to return; the relationship is building). NPE Coalition approaching emergence threshold → Priority 3 (the community's organizing is becoming visible to the player).

## 3.6 Schoenland and the Altonian Vanguard

These actors are conditional — their engagement becomes relevant at specific IP thresholds. They are correctly lower priority than the permanent actors above. The key corrections from the first audit:

**Schoenland at IP < 40.** Traders are standard commercial contacts with Compromise Profile: Economic. Standard Guild engagement rules apply (they are effectively a maritime guild operating through Schoenland's trade routes). No political dimension. The unique element: Schoenland traders have **Altonian Insider** tag in their Genome — they know things about Altonian commercial and military preparation that are unavailable through any other route. This tag is discoverable through Overwhelm Appraise (Read action). Once discovered, it upgrades the Schoenland contact to Priority 3 (Belief-aligned for any player with a Belief touching Altonian threat or peninsula defense).

**Schoenland at IP ≥ 40.** The trader Conviction shifts from Autonomy (trade freedom) to Precedent (maintaining the Accord they operate under). A diplomatic conversation unlocks — not a full Social Contest, but a Dialogue Lattice session where the player can receive Altonian intelligence from a source that is frightened of what's coming. The intelligence quality: Testimonial evidence (the trader has heard things, not seen them) but the most current available about Altonian intentions.

**Altonian Vanguard commander engagement.** At IP ≥ 75 + Vanguard deployment, the scene is a full Social Contest. Clarification from the first audit: the adjudicator is "No adjudicator" type (private negotiation — neither party can appeal to a third power), which makes Attunement the primary pool. Genre: Projection-primary (both parties are arguing about what will happen next, not what happened). The contest is 3 exchanges maximum. On Success: formal Truce (1 season, IP −3). On Overwhelming: Truce + the commander becomes a named NPC with Conviction Wound 1 (his Order conviction is strained by the political waste of a pointless invasion). On Failure: the commander's assessment of Valorian resistance falls — IP +1 (he has tested the waters diplomatically and found no resistance).

---

# PART 4: THE SCENE TRIGGER TAXONOMY — PROPERLY CATEGORIZED

The first audit produced 25 triggers in one undifferentiated list. They are in fact three distinct categories with different mechanical nature.

## 4.1 Category A — World Zoom In Triggers

World-state events that generate personal scene opportunities. These compete in the Scene Slate Priority queue. Selecting one costs a scene action. Not selecting one allows the event to resolve through NPC AI.

**W-01: Occupation Territory Crisis** (Trigger 1 from faction_layer_v30 in player-adjacent territory)
Scene: Resistance Scene in the occupied territory. Anchor NPC from displaced population. Opportunity to initiate or support the Resistance Check as a personal scene action.

**W-02: Parliamentary Vote on Player's Faction** (Trigger 3 from faction_layer_v30 reaching vote threshold)
Scene: Lobbying opportunity. Social Contest (Charisma-primary, Crowd adjudicator, 1 exchange) against a representative of an undecided faction. On Success: +1 vote weight for the player's faction's position. Priority 2 if Standing 3+; Priority 3 if Standing 1–2.

**W-03: Ministry Procedural Obstruction** (Priority tree §7.6 Procedural Objection fires against player's faction)
Scene: The specific Ministry officer who filed the objection is discoverable via Research (existing). Social or investigative engagement per §3.1 access tiers. Priority 2.

**W-04: Guild Commercial Disruption** (Guild domain territory Prosperity drops, or Blockade/Embargo enacted)
Scene: Relevant guild leader (now elevated urgency) in the affected territory. Commerce Crisis scene per §3.2. Priority 2 if player has active Guild Favour token; Priority 4 otherwise.

**W-05: Niflhel Counter-Operation** (Niflhel Priority 6 fires when player investigation of Niflhel reaches Simple threshold while active Tier relationship exists)
Scene: Contact has gone cold. Player must investigate why or stand down. Priority 1.

**W-06: Niflhel Operation Detected** (Tribune Spy Success reveals Niflhel activity in player's territory)
Scene: Intercept opportunity. Investigation scene with 4-node graph (evidence, witness, contact point, exit route). Priority 3.

**W-07: Warden Emergency** (Gap formation OR MS drops below a band boundary AND WR ≥ 2)
Scene: Warden contact seeks the player. Cooperation opportunity. Priority 1 if WR ≥ 3; Priority 3 if WR 1–2.

**W-08: Guild Leader in Territory** (Drift NPC schedule places guild leader in player's current territory)
Scene: Opportunity to engage without seeking them out. Priority 4.

**W-09: Schoenland Intelligence Contact** (IP ≥ 40 AND player has Schoenland Disposition ≥ +1)
Scene: Diplomatic conversation with frightened trader. Priority 3. (Priority 2 if player has Belief touching Altonian threat.)

**W-10: Altonian Vanguard Deployment** (IP ≥ 75)
Scene: Border scene. Vanguard commander as Anchor NPC. Social Contest opportunity per §3.6. Priority 1.

**W-11: Occupation Resistance Check Window** (Faction_layer §2.5 — free Accounting action available)
Scene: The personal version of the Resistance Check. Player leads or participates in territory resistance. Priority 2 for displaced-faction players.

**W-12: Church Cardinal Schism** (Church Stability ≤ 2)
Scene: One of the four Cardinals seeks contact. Dialogue Lattice session, conviction-specific. Priority 1 if player has Evidence relating to Church internal affairs; Priority 3 otherwise.

**W-13: Vaynard Thread Awakening** (Vaynard TS crosses 30 without direct player engagement; Arc B activation)
Scene: Varfell territory shows signs of unguided practitioner activity. Investigation leads to Vaynard. Priority 2.

**W-14: Himlensendt Crisis Evidence** (Church Attention Pool ≥ 5 in any territory AND Complex-threshold investigation underway touching Church activities)
Scene: Cardinal of Temperance presents AER-relevant scholarly findings. Archive POI access scene. Priority 2.

**W-15: Ministry Alliance Opportunity** (Complex investigation revealing Ministry corruption + PAL 3 officer encounter in same territory)
Scene: Presentation opportunity. If delivered, Tier 3 Ministry Alliance activates. Priority 2.

**W-16: Elske Hostage Arc Moment** (Crown Stability ≤ 2 AND Löwenritter Military ≥ 5)
Scene: Elske in a Löwenritter-adjacent territory. Dialogue Lattice session that defines her character through play. Priority 2.

**W-17: Riskbreaker Contact** (Coup Counter ≥ 1)
Scene: Torsvald as Drift NPC in player's territory. Ambiguity Node Layer active (anomalous behavior discoverable through Surveil before direct approach). Priority 3.

**W-18: NPE Coalition Embryo Forming** (Stance convergence in a territory where player has Disposition ≥ +1 with ≥ 2 of the converging NPCs — per comprehensive audit IC-1)
Scene: Social coalescence moment. Player can lead or observe. Founding implications if Network conditions are met. Priority 3.

**W-19: RM Community Weaving Opportunity** (Territory Piety ≤ 1 + ≥ 3 Equity/Continuity NPEs present)
Scene: Community gathering. Cultural Practice action available. Priority 3 for RM-aligned players; Priority 4 for others.

**W-20: Founded Organization First Action** (Organization completes its first Domain Action)
Scene: Organizational consequence visible in the home territory — the action's effects manifest as witnessed world events. Priority 2.

## 4.2 Category B — Character Arc Triggers

Character-state events that generate personal scenes. These are **not competitive with the Scene Slate Priority queue** — they are mandatory scene generation that supersedes the Slate when they fire. They do not cost a scene action; they replace one (the scene action that would have gone to Priority 1 this season is consumed by the Character Arc trigger). The player cannot choose not to engage with these.

**C-01: Companion Belief Crisis** (Companion accumulates 2 Belief-contradiction events while co-traveling)
Mandatory scene: Mid-scene companion confrontation. Dialogue Lattice with companion as primary NPC. Outcome determines whether companion stays, departs, or deepens the relationship.

**C-02: Belief Near-Fulfillment** (Belief Progress Track reaches Near Fulfillment)
Mandatory scene: Belief Resolution scene. The scene graph is generated around the Belief's subject matter. Outcome determines Fulfillment (Momentum + Echo) or Contradiction (revised Belief with narrative acknowledgment).

**C-03: Certainty Crisis** (Certainty shifts by 2+ in one season from any source)
Mandatory scene: Rendering Moment. Three-choice response (Anchor, Resist, Accept) as previously specified. This fire interrupts the normal season flow and is processed before Phase 1 of the following season.

**C-04: Coherence Critical** (Player practitioner's Coherence drops to 3 or below)
Mandatory scene: Thread crisis. The existing Dissonant mechanics (Spirit check, −1D social/memory) are augmented by a scene where the player's rendering instability is visible to any companions and NPCs they are currently with. Companions at this scene can either provide Knot Anchoring (restoring Coherence +1, per existing Knot Anchoring rules) or withdraw (if their conviction makes them unwilling to engage with Thread-reality distress). This converts a stat-track event into a personal scene.

**C-05: Network Recognition** (Player achieves Network status per §2.2 for the first time)
Mandatory scene: The first Network scene — a gathering of the player's relationships that acknowledges the pattern. This is not a political event; it is a personal one. The scene has no mechanical objective; it is the game acknowledging that the player has built something real.

## 4.3 Category C — End-State Scenes

These fire when victory or shared-loss conditions are triggered. They are not Zoom In triggers — they are the final scenes of the game's arc. They belong in a separate section of the game's end-state specification and are noted here only for completeness.

**E-01 through E-07 cover:** Crown Treaty Ratification, Church Theocracy Declaration, Varfell Thread Mastery culmination, Hafenmark Parliamentary Sovereignty, RM Cultural Revolution completion, Rupture onset (MS 0), Altonian Conquest, and Anarchy. Each should be specified as a personal scene the player's character inhabits at the moment of resolution — not a statistics screen.

---

# PART 5: INTEGRATING WITH BELIEFS, DUTIES, AND STANDING

The first audit engaged with Beliefs primarily in the companion arc section and barely engaged with Duties and Standing at all. This was the largest structural omission. The full integration is specified here.

## 5.1 Beliefs and Non-Standard Actors

The Belief tag system (per comprehensive audit CS-1 resolution: structured tag fields) must accommodate non-standard actors. The following tags should be added to the available Belief tag vocabulary:

| Tag Category | New Tags |
|---|---|
| [NPC: name] | Ministry Officer (PAL-tier), Guild Leader (domain), Niflhel Contact (tier), Warden Name, Arm Leader name |
| [Faction: name] | RM, Ministry (as an institution), Schoenland |
| [System: keyword] | Thread (existing), Warden-Work, Information-Economy, Cultural-Practice |
| [Territory: name] | All existing territory tags remain |

When a Belief is tagged with a non-standard actor or system, Scene Slate Priority 3 generation preferentially surfaces scenes involving that actor in the player's current or adjacent territory. A Belief tagged [NPC: Edeyja] and [System: Warden-Work] generates one Priority 3 entry per season as long as the player is within two territories of the Southernmost.

## 5.2 Duties and Non-Standard Actors

The Agency System §3.3 Duty types table lists eight types. The following extensions cover non-standard actor assignments, available when the player has relevant Standing with a faction whose interests intersect with non-standard actors:

| Duty Type | Assignment Condition | Success Condition | Failure Consequence |
|---|---|---|---|
| Ministry Access | Faction needs Buried-depth records it can't formally request | Achieve Tier 2 Ministry access and retrieve specified record | Records remain sealed; faction acts on incomplete legal intelligence |
| Guild Negotiation | Faction needs Guild Favour in a specific domain | Obtain Guild Favour token in specified domain | Commercial disadvantage persists; rival faction gets first access |
| Intelligence Acquisition | Faction Tribune Spy slot is spent; intelligence priority exists | Obtain equivalent intelligence through Niflhel Tier 2 | Faction makes a Domain Action with incomplete intelligence (hidden +1 Ob applied next season) |
| Warden Liaison | Faction needs Thread intelligence from Southernmost region | Achieve WC 1 and receive territory-level Thread Tension report | Faction's Thread-related Domain Actions operate without substrate intelligence |
| Community Stabilization | Territory has RM-sympathetic population at risk of Revolt | Prevent Revolt through Community Weaving or social engagement | Accord drops to 0; Revolt resolves through faction AI |

These Duty types are available to players with Standing 2+ (they require access to faction intelligence to even know these needs exist). They represent the faction layer reaching into the non-standard-actor space through the player's personal capabilities.

## 5.3 Standing and Non-Standard Actor Access

The Standing track (0–5) within an existing faction gains the following non-standard actor unlocks, layered on top of the existing stature description in the Agency System §5.1:

| Standing | Non-Standard Actor Unlock |
|---|---|
| 2 (Agent) | Faction shares which non-standard actors are active in current assignment territory (Niflhel presence known, Ministry officer identity known, guild leaders in the region identified) |
| 3 (Counselor) | Faction invites player to broker relationships with non-standard actors on the faction's behalf (Duty types above become available; Guild Favour tokens acquired can be assigned to faction use) |
| 4 (Lieutenant) | Player can direct NPC officers to approach non-standard actors (a junior officer maintains a Tier 1 Niflhel relationship; player's Ministry access is leveraged for faction intelligence; Warden Liaison is delegated when player is not personally available) |
| 5 (Successor) | Player's non-standard actor relationships are institutionalized — the faction formally maintains them at the player's achieved tier even across seasons when the player is absent |

The Standing 5 institutionalization is the culmination of the non-standard actor architecture: the player's personal relationship-building has been absorbed into the faction's institutional capabilities. What the player built through individual Sincerity Gates, individual investigations, and individual Thread demonstrations is now a persistent capability of the organization they lead or will lead.

---

# PART 6: DOMAIN ECHO EXTENDED REFERENCE — WITH CAP CLARIFICATION

**Seasonal cap confirmation.** The ±2 per-season per-stat cap applies cumulatively across ALL Domain Echo sources from a single player character, including extensions from this audit. Stature-Scaling (DE-I from the comprehensive audit) does not override the cap; it changes the per-action magnitude, increasing the probability of hitting the cap from fewer actions.

**Cap interaction with non-standard actor Echoes.** Non-standard actor Echoes (Guild Favour Parliamentary Endorsement, Ministry Alliance obstruction cancellation, Warden cooperative Mending) are all territory-scale effects rather than faction-stat effects. They therefore do not count against the ±2 faction-stat cap. This is deliberate — these actors primarily affect territory-level values (Accord, Piety, Prosperity, Fort Level, POI access) and are intended to give the player influence at the territory scale without competing with the faction-stat cap that governs strategic-layer influence.

Extended Domain Echo table (additions only — does not replace the integration proposal's Part 8 table):

| Action Type | Sufficient Scope Condition | Echo Target | OW | Success | Partial | Failure |
|---|---|---|---|---|---|---|
| Ministry Tier 2 record retrieval | Record contains Structural-quality evidence on political subject | Faction Influence (delivering faction); Casus Belli if applicable | +2 Influence; CB generated if warranted | +1 Influence; record is Verified evidence | Record adds to Case Board (player knows); faction not yet informed | Access burned for this season; Ministry officer Disposition −1 |
| Ministry Tier 3 Alliance activation | Structural investigation on Ministry + PAL 3 presentation | Territory: Procedural Access permanent (Ministry treats player's faction's Domain Actions with reduced friction) | One Procedural Objection against player's faction cancelled per season | −1 Ob on one Domain Action per season (Ministry smooths the process) | Case-by-case support (no permanent effect) | Alliance attempt failed; PAL 3 officer retaliates with a Procedural Objection against the player's faction next season |
| Guild Favour token spent — Parliamentary Endorsement | Token exists AND motion affects guild's domain | Vote weight: +1 toward player's faction in that motion only | Token spent; vote shifts +1; guild leader Disposition +1 (they appreciate the ask) | Token spent; vote shifts +1 | Token spent; no vote shift (guild leader's endorsement wasn't decisive) | Token burned; guild leader publicly disassociates; Disposition −2 with that guild leader |
| Niflhel Intelligence Purchase | Intelligence target is faction-level (reveals hidden stat or covert Domain Action) | Player's faction: one Investigation Finding (Verified, Tribune-equivalent) | Faction gains the Finding immediately + information on what the target faction's next Domain Action will be (covert preview) | Finding gained | Finding quality: Testimonial (less reliable) | False intelligence purchased; player faction acts on incorrect data for 1 season |
| Niflhel Debt Collection at Accounting | Player purchased services; debt obligation activated | Player's faction loses one Echo result (declared by player at Accounting) | N/A (debt always collected) | N/A | N/A | If no Echo available: −1 Faction Influence (or Organization Mandate if independent) |
| Warden Cooperative Mending | WC 2+ joint operation at Success+ | MS | +2 MS (collective amplification of existing Mending magnitude) | +1 MS | MS stable; no loss | Mending fails; −1 WC (relationship cost for failed joint work) |
| RM Community Weaving (Cultural Practice) | Piety ≤ 1 territory, non-practitioner lead | Piety drift; Accord | Piety −1 immediate; Accord +1; one NPE permanently shifts conviction | Piety drift accelerated by 1 season; Accord +1 | Accord +1 only | Exposure +3; Church Attention Pool +1 in this territory; no cultural effect |
| RM Community Weaving (practitioner-led) | TS ≥ 30, with community participants | MS; Piety; Accord | +2 MS; Piety −1; Accord +1; one NPE conviction shift | +1 MS; Piety drift accelerated | +1 MS; no Piety shift | Coherence −1; Exposure +3; MS unaffected |
| Companion Belief fulfillment (player enables companion's Belief) | Player scene action directly advances companion's active Belief | NPC arc trigger; Companion Conviction Wound resistance | Companion arc advances one stage; +2 Momentum to player; one NPC related to companion's Belief shifts Disposition +1 toward player | Companion arc updates; +1 Momentum | Companion Belief Progress Track advances; no external effect | Companion Belief stalls; companion Disposition −1 (they sense the attempt was unsuccessful) |
| Founded Organization Domain Action | Organization completes a Domain Action at Success+ | Territory per action type (see §2.3 Domain Action list) | OW equivalent to Standing 4 (per Stature-Scaled Echo table) | Success equivalent to Standing 3 | Narrative shift in territory; no stat change | Organization Mandate −1; local credibility reduced |
| Schoenland Vanguard Truce | Social Contest against Vanguard commander at Success+ | IP | IP −3; Truce 1 season; commander gets Conviction Wound 1 | IP −1; Vanguard advance delayed 1 season | No mechanical effect | IP +1 (Vanguard commander assesses Valoria as diplomatically weak) |

---

# PART 7: THE INTEGRATION MAP — RESOLVED INTERDEPENDENCIES

The following interdependencies were either unresolved or unaddressed in the first audit and the integration proposal. Each is resolved here.

**ID-01: Companion Investigation vs. fieldwork_v30 §3.2 assistant rules.**
Resolution: The companion CSC "Assist Investigation" IS the assistant role from §3.2. Same rules apply — Ob+1, success adds +1 to leader's net, failure adds +1 Exposure. The CSC table is a conviction-to-action-preference mapping, not a separate mechanic. No conflict.

**ID-02: Companion Corroboration in Social Contests vs. social_contest_v30 §4 Step 2b.**
Resolution: A co-traveling companion is automatically eligible as a Corroborator under §4 Step 2b. They roll at Ob 1 (Knot-bonded companion = Ob 1 per existing Knot rules; Knot formation is the prerequisite for co-travel, so all companions are always Ob 1 Corroborators). The companion's Contribution for a Contest scene IS the Corroboration action. This is not additional — it is the existing mechanic named.

**ID-03: Companion dual-membership (faction recruit AND companion).**
Resolution: Not mutually exclusive. An NPC recruited into the player's faction AND Knot-bonded as a companion operates under both statuses. Their faction role provides Domain Action intelligence (they know what the faction needs); their companion status provides personal scene contributions. The tension between these roles IS the drama: a faction-recruited companion may receive Duties from the faction that conflict with the player's personal Beliefs — exactly the Duty vs. Belief tension the Agency System identifies as the game's engine.

**ID-04: Founded Organization vs. existing Standing track — Parliamentary voting resolution.**
Resolution (per §2.3 in this audit): The player contributes votes from two sources if both apply: (a) their faction's Mandate (if Standing 3+, per Agency System §5); (b) their Organization's Mandate (if the motion is domain-aligned). These are additive only if the Organization vote is formally registered via a Senator action the previous season. If the player hasn't spent a scene action to register the Organization's parliamentary intent, only the faction vote applies. This prevents the Organization from being a "free" parliamentary actor that doubles the player's influence without cost.

**ID-05: Domain Echo seasonal cap with multiple non-standard actor engagements.**
Resolution (per Part 6 above): Non-standard actor Echoes targeting territory-scale values (Piety, Accord, Prosperity) do not count against the ±2 faction-stat cap. Only Echoes targeting Peninsula-scale values (faction Mandate, Influence, Wealth, Military, Stability) count against the cap. A busy season engaging Ministry, Guild, Niflhel, and Wardens produces multiple territory-scale Echoes without cap conflict, plus potentially one faction-stat Echo (if evidence from Ministry access is delivered to the faction). The territory-scale Echoes are the architecture of the non-standard actors' design space; the cap governs the strategic layer.

**ID-06: Niflhel counter-operations and Scene Slate generation.**
Resolution: When Niflhel Priority 6 fires against the player, it generates Priority 1 Scene Slate entry W-05 (specified in Part 4). The player's choice of how to respond to W-05 determines whether the Tier relationship continues, pauses, or escalates to full counter-operations (which would be Priority 1 in subsequent seasons until resolved). This is the only mechanic in the game where an NPC priority tree directly generates a Scene Slate entry targeting the player personally — making it the sharpest expression of the "world is alive independently of you" design principle.

**ID-07: Community Weaving for non-practitioners and the TC formula.**
Resolution: Non-practitioner Community Weaving generates +1 Exposure (standard for conspicuous social action) and, at Watched threshold, +1 Church Attention Pool per territory per season (per fieldwork_v30 §6.5 cap: +1 per character per season). Practitioner-led Community Weaving generates the same Church Attention Pool effect (it is equally or more visible) plus the Thread operation Exposure (+1 per Thread-Read/Leap action from fieldwork_v30 §6.3). In a Church-controlled territory with Piety ≥ 3, both versions of Community Weaving are high-risk: they rapidly advance the AP toward Heresy Investigation eligibility. This is intentional. RM cultural practice in Church territory is politically confrontational — it should feel that way.

**ID-08: WR/WC track vs. Varfell Path B mechanics.**
Resolution: The WR/WC tracks now formally defined in this audit are what Varfell's npc_behavior_v30 §8.5 Priority 4b references ("Warden Cooperation track WC < 2"). A Varfell player pursuing Path B needs WC ≥ 2 to complete Warden Recognition. The Varfell AI pursuit of Warden contact (via Expedition Domain Action) represents institutional-level Warden Recognition — separate from the personal WR/WC track that the player character builds. A Varfell player with personal WC 3 AND their faction pursuing Warden Recognition diplomatically creates a synergy: the faction's institutional approach and the player's personal thread-competence recognition compound.

**ID-09: Niflhel service and Church Attention Pool.**
Resolution: Counter-Surveillance service (−3 Exposure) affects the Exposure value that feeds the AP. If Counter-Surveillance reduces the player below Watched threshold, the AP does not receive the entry it would have at Accounting. This is the correct behavior — the service exists to reduce the player's operational risk, and the AP entry fires from Exposure thresholds, not from actions directly.

**ID-10: Dialogue Lattice mid-session Escalation — Composure/Concentration carry.**
Resolution (per the integration proposal critique in Part 0): When Escalation fires mid-Lattice, the Social Contest begins with both parties' Composure at their full values MINUS the strain accumulated during the Lattice session. Each filter failure that produced a hostile response generated strain even in the Lattice phase — the emotional cost of a difficult conversation applies regardless of whether it's in a Lattice or a Contest. The handoff carries: Concentration = full (fresh tactical engagement), Composure = full − strain already taken in Lattice, Conviction Wound count as specified, Disposition offset as specified. The starting Piety Track position is also modified: if the Lattice session ended because the NPC reached Wound 1 (the typical escalation trigger), the starting CT position is shifted −1 toward the player's position (the NPC is already under pressure before the Contest begins).

---

# PART 8: PRIORITY RECOMMENDATIONS — CONSOLIDATED

All recommendations from the integration proposal, the first audit, and this revision are consolidated here in a single ordered list. The integration proposal's B-1 through B-5 remain correct and are retained without renumbering.

## Blocking (required before videogame integration)

**B-1:** Domain Echo Reference Table formal commit (integration proposal).

**B-2:** Scene Slate/Scene Graph unification with template-selection algorithm specifying how entry type + world state → graph template family (this revision adds the algorithm requirement to the integration proposal's B-2).

**B-3:** Dialogue Lattice → Social Contest handoff, extended to include: mid-Lattice escalation Composure carry, starting CT modification for Wound 1 escalation cases (this revision extends the integration proposal's B-3).

**B-4:** Stability trigger → Scene Slate coupling (integration proposal).

**B-5:** J-7 territory scale resolution and propagation (integration proposal).

**B-6:** Companion specification formal commit using the unified version in Part 2 of this document. Specifically: combat command timing (Phase 1 declaration, not action priority), Bonds/2 capacity formula, Knot-strain departure model, Belief-contradiction threshold (3 events + leave scene).

**B-7:** Warden WR/WC track formal definition, committed to clock registry or params_fieldwork as personal-scale tracks. The advancement conditions and unlocks in §3.4 of this document are the proposed canonical form.

**B-8:** Niflhel service protocol formal specification, resolving ED-041. The tier system in §3.3 of this document is the proposed canonical form, including the debt-obligation payment model.

**B-9:** Community Weaving Cultural Practice variant formally specified (non-practitioner Charisma pool, Piety-drift effect, distinct from Thread op version). This resolves the mechanical conflict between the existing Thread op gate system and RM non-practitioner engagement.

**B-10:** Scene trigger taxonomy formally categorized into World Zoom In (Part 4.1), Character Arc (Part 4.2), and End-State (Part 4.3). Minimum 20 World Zoom In triggers committed before videogame integration (W-01 through W-20 in Part 4.1 are the proposed canonical set).

## High Value (implement in next design sprint)

**H-1 through H-6:** Per integration proposal (all retained).

**H-7:** Ministry named officers — three NPCs (PAL 1, 2, 3), with Genome entries per the npc_behavior_v30 template. Specifically: primary Conviction (Order), secondary (Precedent or Reason depending on tier), active Beliefs, Compromise Profile (Political primary, Informational secondary).

**H-8:** Five guild leader Genome entries — full conviction triangles, Beliefs, and Compromise Profiles per the §3.2 templates in this document.

**H-9:** Companion-faction alignment tension matrix — for each named NPC companion candidate, specify which player faction alignments create Belief-contradiction tension and which create Belief-alignment coherence.

**H-10:** Non-standard actor Duty types committed to the Agency System §3.3 table (Part 5.2 of this document).

**H-11:** Standing track non-standard actor unlocks committed to the Agency System §5.1 table (Part 5.3 of this document).

## Creative Enrichment

**E-1 through E-5:** Per integration proposal (all retained).

**E-6:** Warden Deathwatch arc authored — the scene where the player either accepts Warden succession, declines it, or creates a new cohort (§3.4 of this document).

**E-7:** Founded Organization first-action Scene Type authored — what territory-level visible changes look like when an Organization acts for the first time (§2.3 W-20 trigger).

**E-8:** Niflhel Arm Leader companion arc — the formal design of the Autonomy vs. Knot tension that defines this relationship (the most difficult companion arc in the game).

**E-9:** End-State scenes (Category C triggers, Part 4.3) authored for all six victory conditions and three shared-loss conditions. Every campaign end is a personal scene.

---

# APPENDIX: THE FACTION FORMATION DESIGN DECISION

The question of whether the player can form their own faction — one that competes symmetrically for Universal Victory — is a genuine design decision, not a resolved specification. The following positions the choice clearly without asserting which is correct.

**Option A — Full Faction Creation is Available**

The Founded Organization can, over a long campaign (15+ seasons of maximum investment), reach Mandate 5 and compete for Universal Victory through the parliamentary and territorial mechanisms that all factions use. The path is intentionally difficult: it requires building 15+ NPC relationships, multiple Structural investigations, sustained territorial governance, and eventual Parliament representation.

*For:* Consistent with the philosophical premise that legitimate governance emerges from genuine relationships. Rewards the most committed relational playstyle. Creates an entirely novel late-game experience no other faction provides.

*Against:* Extremely long path crowds out other arcs. The player spending 15 seasons on faction-building cannot also pursue Thread mastery, Warden collaboration, and deep personal relationships simultaneously. Risk of the Founded Organization being a weaker version of existing factions rather than a distinct experience.

**Option B — Founded Organization as Political Multiplier (Proposed)**

The Founded Organization maxes at Mandate 3. It cannot achieve Universal Victory alone. It can, however, be decisive in other factions' victories (intelligence that enables Crown Treaty, cultural work that enables RM Cultural Revolution, Warden partnership that enables Thread Mastery). The player's legacy is their contribution to the world's resolution, not their name on the victory banner.

*For:* Creates a genuinely different experience from all existing faction paths. Better supports the philosophical premise that the peninsula's problems require cooperation, not personal triumph. The player's founded organization is the mechanism through which unlikely alliances become possible — Crown and Wardens working together, RM and Hafenmark finding shared parliamentary ground.

*Against:* Some players will find it unsatisfying that personal effort and relationship-building doesn't produce "their" victory. May create a sense that independent play is second-class compared to faction service.

**Option C — Conditional Full Victory**

The Founded Organization can achieve a unique victory condition unavailable to formal factions: **Civic Renewal** — Accord ≥ 3 in 10+ territories, Founded Organization Mandate ≥ 2, MS ≥ 50, Political Stability ≤ 4, for 2 consecutive seasons. This victory represents a peninsula that has stabilized through distributed governance rather than centralized authority. It requires different conditions than Universal Sovereignty (no need for military control, but higher Accord thresholds and MS requirement) and reflects a different theory of political success.

*For:* Gives the Founded Organization a genuine victory condition while making it distinct from existing faction victories. The Accord and MS requirements mean the player must engage with both the social and Thread layers — the most philosophically complete Valorian playthrough.

*Against:* Adds a ninth victory condition, complicating the victory architecture. The Accord/MS requirements may interact with the Church's Piety dynamics in complex ways that need simulation.

**Recommendation:** Option C is the most creatively and philosophically aligned choice, but it is Jordan's decision. All three options are mechanically supportable within the existing system. The Founded Organization mechanics in Part 2 are specified to be compatible with any of the three options — the choice of victory condition ceiling does not require redesigning the organization's mechanics.

---

*All specifications in this document are in PROPOSAL status and require explicit approval before integration into canonical documents. The Companion Specification (Part 2), Non-Standard Actor Protocols (Part 3), Scene Trigger Taxonomy (Part 4), and Domain Echo Extended Reference (Part 6) are the primary actionable deliverables. The integration map (Part 7) and priority consolidation (Part 8) are intended as an immediate working reference.*

*End of document.*
