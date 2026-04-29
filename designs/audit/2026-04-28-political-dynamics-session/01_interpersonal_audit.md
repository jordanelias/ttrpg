<!-- [PROVISIONAL: 2026-04-28 session — d964fd13158349fa] -->
<!-- STATUS: PROVISIONAL — design exploration, not canonical mechanic -->
<!-- TITLE: Interpersonal → Political Dynamics Gap Audit -->
<!-- POSITION IN ARC: see designs/audit/2026-04-28-political-dynamics-session/00_session_index.md -->
<!-- VETTING: see 07_armature_system_vetting.md for canonical framework assessment -->

# Interpersonal → Political Dynamics Audit

## Scope

How interpersonal relationships operate mechanically in Valoria, and how those mechanics radiate into character advancement, arcs, settlement governance, faction dynamics, and cross-faction politics. Evaluated through the videogame implementation lens: what does the player experience, what does the engine compute invisibly, and where are the gaps?

---

## PART 1: THE INTERPERSONAL SUBSTRATE — WHAT EXISTS

### 1.1 The Disposition–Knot Pipeline

Valoria's interpersonal system runs on a two-stage pipeline:

**Stage 1 — Disposition (-3 to +5):** The PC's relationship state with any NPC. Movement via social actions (Converse, Connect, Read, Impress, Negotiate, Gift). Ceiling = Bonds attribute (structural gate: Bonds 3 = max Disposition +3). Each level unlocks information depth and Ob modifiers.

**Stage 2 — Knots (Close/Distant):** Deep Thread-mediated bonds at Disposition +5 + TS ≥ 30. Provide +1D social, shared Composure buffer, relational contagion (P-12), Knot strain lifecycle (Distant: 4 capacity, Close: 7). Rupture on counsel betrayal, partner death, FR Dissolution, or Conviction opposition.

**What this produces politically:** The pipeline creates a clear investment curve. Building a relationship to Disposition +3 (Trusting) takes 6–8 social actions across 3–4 seasons. Reaching Knot candidacy at +5 requires Bonds ≥ 5 at creation. This means the player's attribute allocation at character creation determines the ceiling of their political tool: high-Bonds characters can form Knots (and therefore access counsel extraction, Composure sharing, and the Solidarity contest style); low-Bonds characters are structurally locked out. This is a genuine strategic choice — Bonds competes with Agility, Spirit, and Cognition for creation points.

**Assessment:** Clean. The Disposition → Knot pipeline is mechanically complete, pacing-calibrated (PP-632), and has strain/rupture consequences. The Bonds ceiling (PP-684) is elegant — a single attribute gates maximum relational capacity without adding a separate trust mechanic.

### 1.2 NPC Beliefs, Scars, and Arc Emergence

Named NPCs hold 2–3 Beliefs. Belief revision requires: (1) decisive Contest outcome, (2) using the NPC's Resonant Style, (3) argument engaging the specific Belief. Revised Beliefs become Scars.

**Scar accumulation → political consequence:**
- 1 Scar: secondary Conviction activates, Decision Forks increase. NPC becomes less predictable.
- 2 Scars: primary Conviction may shift. NPC enters arc transition. Institutional Tendency diverges from personal behavior.
- 3+ Scars: Conviction crisis. d6 table per major decision. NPC is in full transformation — arc terminal phase.

**How this radiates:** An NPC faction leader accumulating Scars destabilizes the entire faction. Himlensendt at 2 Scars means the Church's AI priority tree produces less predictable behavior. Almud at 2 Scars means Crown Domain Actions may contradict the Virtue Ethics framework (triggering +1 Ob), or the Crown may pivot toward Thread acceptance (Arc A: Reformer). The player's interpersonal work — winning Contests against faction leaders — directly produces faction-level instability.

**Assessment:** Strong. The Scar → arc → faction consequence chain is the game's best interpersonal-to-political throughline (T-23). The videogame implementation is clear: the engine tracks Scar count per NPC, fires arc branch conditions, and updates faction AI priority trees accordingly.

### 1.3 Advisor-Principal Confidentiality (ED-664)

Named NPCs in formal advisor positions operate under confidentiality rules. Private counsel → no consequence. Public breach → Disposition/Renown/Standing loss. Strategic defection → role transfer.

**Political import:** The player can extract private counsel via Knot-mediated mechanism (Connect + Argue, Ob 3, single attempt per advisor per campaign). Success reveals one piece of actionable private counsel. But public citation of this counsel ruptures the Knot and resets Disposition to -4.

**What this creates:** A genuine trust-as-resource mechanic. The player who extracts counsel from Baralta's legal advisor learns what Baralta is privately considering — but using that information publicly destroys the relationship. This is the game's closest analog to the inspiration document's trust/surveillance tension (Sengoku parallel). The constraint is that it fires once per advisor per campaign, which limits it to a climactic moment rather than an ongoing political tool.

### 1.4 NPC Outreach Generation (§8.11)

Each named NPC evaluates whether to initiate a scene with the player each season. Outreach (Disposition ≥ +2): NPC approaches with Conviction-driven agenda. Demand (Disposition ≤ -2): NPC summons player under institutional authority.

**Political radiation:** This is how the game's interpersonal dynamics become bidirectional. The player doesn't just pursue NPCs — NPCs pursue the player based on accumulated Disposition and Conviction relevance. A player with Disposition +3 toward both Almud and Baralta receives competing Outreach scenes from faction leaders with incompatible agendas. Choosing which to attend is a political act (one faction's agenda advanced, another's deferred).

**Assessment:** Well-designed for the videogame: the Scene Slate presents 5–12 options per season (3–5 pursuable), and the player's choices among NPC-initiated scenes are the primary political input at personal scale.

---

## PART 2: HOW RELATIONSHIPS FEED ADVANCEMENT AND GOVERNANCE

### 2.1 Standing Ladder as Relationship Product

Standing 0–7 progression determines governance scope. The ladder is explicitly gated by interpersonal dynamics:

- Standing 3 (Counselor): Invited to faction council. Can negotiate or refuse Duties. Can argue for different faction priorities via social contest.
- Standing 5 (Senior): Council voting member. Speaks in faction's name.
- Standing 7 (Regent-Designate): Succession-eligible. Leadership challenge via social contest.

**The interpersonal input:** Standing advancement requires Renown (cross-faction reputation) and faction-specific actions. But the critical gates at Standing 3+ are institutional — the player needs the faction leader's Disposition high enough to be *trusted* with council access. The mechanics are implicit rather than explicit here. The faction leader grants council access, but there's no specified Disposition threshold for council invitation.

**GAP — Standing advancement Disposition gates:** The Standing ladder specifies what each rank unlocks but not the interpersonal prerequisite for promotion. In Valoria's historical-political framing, a faction leader doesn't promote someone they distrust. A Standing 2 → 3 advancement should require minimum Disposition +1 with the faction leader (or their designee). Standing 4 → 5 should require +2. Standing 6+ should require +3 or active Knot. This creates the historically correct dynamic: advancement requires not just deeds but relationships — and maintaining those relationships under political pressure.

### 2.2 Settlement Governance as Interpersonal Domain

When a player becomes Settlement Governor (Standing 3+), their seasonal Duty becomes governance. The governance actions (Develop, Fortify, Pacify, Administer) are personal-scale rolls using the PC's attributes against settlement stat thresholds.

**The interpersonal layer:** Administer reveals one local NPC's active Conviction. Pacify uses Charisma + local History. Prosperity 0 triggers population exodus (Order -1 automatic). Order 5 + Prosperity 4+ produces +1 Disposition with all local NPCs.

**How this connects to politics:** A player-governor's interpersonal work in a settlement directly shapes that settlement's contribution to factional politics. A well-governed settlement (high Order, high Prosperity) contributes treasury, stability, and NPC loyalty to the controlling faction. A poorly governed settlement becomes a vulnerability that rival factions can exploit.

**What's missing:** The settlement-to-faction feedback loop is specified for stats (Prosperity → treasury, Order → stability check), but the *interpersonal* settlement-to-faction loop is thin. Local NPCs have Dispositions and Convictions, but their relationship with the player-governor doesn't formally feed into faction-level dynamics. A player-governor who builds +3 Disposition with 5 local NPCs has a loyal settlement, but that loyalty doesn't mechanically translate into faction Mandate or Stability in ways the player can observe and strategize around.

**GAP — Settlement loyalty as faction resource:** Settlements with Order 4+ and governor Disposition +3 with ≥ 3 local NPCs should resist hostile faction takeover (+1 Ob to conquest or subversion). This is the holdout mechanic from §6.3 Faction Collapse (governors with Disposition ≥ +3 can resist new controllers), but it activates only on faction collapse. It should be a continuous effect: well-governed settlements with strong interpersonal networks are harder to pry loose, period. This creates a political incentive for factions to assign capable governors and for players to invest in local relationships — the interpersonal work produces structural political advantage.

### 2.3 Companion System as Political Asset

Companions (per companion_specification) are recruited NPCs who travel with the player. They have their own Convictions, Beliefs, and Disposition tracks.

**Political radiation:** A companion serving as settlement governor gets 1 free action per season (social OR governance, not both). This means the player's companion network extends their governance reach — a player governing 3 settlements (Standing 4+) needs companions to manage the ones they can't personally attend. The companion's Conviction and Disposition with local NPCs shapes that settlement's political character.

**Assessment:** Mechanically sound but the political consequences of companion governance are underspecified. A companion-governor whose Conviction contradicts the controlling faction's Ethical Framework should produce Framework Drift friction at the settlement level. A companion-governor with low Bonds cannot build deep local relationships, limiting that settlement's interpersonal resilience. These are logical consequences of existing mechanics that need explicit specification.

---

## PART 3: INTERPERSONAL DYNAMICS → FACTION POLITICS

### 3.1 The Vertical-Only Problem

The design's interpersonal relationships are overwhelmingly vertical: Player ↔ NPC. The NPC Outreach system, Disposition track, Knot formation, advisor counsel — all run between the player and individual NPCs. The inspiration document's core critique applies: **NPC ↔ NPC horizontal relationships are structurally unmodeled**.

What's present:
- **Knot strain propagation (§5.0b):** NPC arc transitions produce Knot strain on connected contacts, including other NPCs. This is the one horizontal NPC ↔ NPC interaction path.
- **Inner-circle dynamics (§2.15):** Crown IC has named members (Spymaster, Steward, Confessor, Marshal, Chancellor). They have individual Convictions and can disagree in private counsel (ED-664). But their *relationships with each other* are not tracked.
- **Framework Drift (§7):** Factions drift passively. But drift is institutional, not interpersonal — it doesn't emerge from NPC relationships within the faction.

What's missing:
- **NPC-to-NPC Disposition**: Ehrenwall and Almud have a defined political relationship (Löwenritter loyal to Crown but with graduated autonomy trigger). Baralta and Himlensendt have structural opposition (Sovereign Authority Doctrine vs. Church Seizure). But these are hard-coded faction relationships, not interpersonal Dispositions that evolve through play.
- **NPC rivalry**: Two NPCs competing for the same position, the same player's attention, or the same faction resource. The inner-circle positions are static — there's no mechanic for an NPC to lobby for a position held by another NPC.
- **NPC coalition formation**: NPCs with shared Convictions aligning against NPCs with opposing Convictions, independent of faction boundaries.

**Why this matters for politics:** The game's political dynamics are currently a set of bilateral channels (Player ↔ Almud, Player ↔ Baralta, Player ↔ Himlensendt) rather than a political environment where NPCs act on each other and the player navigates the resulting landscape. In Valoria's videogame implementation, this means the player is the only political agent who connects factions — NPCs don't form relationships with each other that the player must react to, work around, or exploit.

**Recommendation:** NPC-to-NPC Disposition doesn't need the full -3 to +5 track. A simplified three-state system would suffice for the engine:

| State | Meaning | Mechanical effect |
|---|---|---|
| Aligned | NPCs share Conviction or institutional interest | Joint actions possible; NPC vouches for the other to the player; Domain Action coordination enabled |
| Neutral | No strong relationship | Default state; independent behavior |
| Opposed | Competing Conviction, prior betrayal, or institutional rivalry | Obstruction (+1 Ob to actions benefiting the opposed NPC); won't share intelligence; may actively undermine |

This is computed at Accounting from: (a) Conviction overlap (same primary = Aligned bias), (b) shared faction membership (+1 toward Aligned), (c) recent Domain Action conflicts (-1 toward Opposed), (d) player-mediated introduction (Connect action used to introduce two NPCs = +1 toward Aligned). The engine evaluates NPC-NPC relationships as a matrix and uses it to modify AI priority trees. The player sees the consequences — an NPC who refuses to cooperate because they're Opposed to the NPC the player just brought into the inner circle — but the computation is invisible.

### 3.2 Cross-Faction Relationships as Political Terrain

The design handles cross-faction Disposition via starting values (same faction: +1; rival: -1 to -2; hostile: -2 to -3). But it doesn't specify what happens when a player builds deep relationships across faction lines.

**What currently exists:**
- A player embedded in the Crown (Standing 4) can simultaneously build Disposition +3 with Vossen (RM). There's no mechanical consequence for maintaining cross-faction relationships.
- The Sincerity Gate (Spirit check, 37% failure) applies to instrumental social approaches regardless of faction.
- NPC Outreach fires based on Disposition + Conviction relevance, so cross-faction NPCs with high Disposition will initiate scenes that create competing demands on the player's time.

**What this means for politics:** The player can be a genuine cross-faction broker — someone with high Disposition in multiple factions — without mechanical penalty. This is appropriate for some political roles (diplomat, mediator) but historically, maintaining deep relationships across hostile faction lines carried real costs. The player who dines with both the Crown and the RM should face: (a) exposure risk if the Crown discovers their RM contacts, and (b) loyalty pressure from their primary faction.

**Assessment:** The Exposure system (§6) handles (a) partially — covert RM contacts accumulate Exposure, and Exposure reaching Cover threshold triggers detection. But there's no systematic loyalty test from the player's own faction when cross-faction relationships are discovered. The faction leader should react to learning that their Standing 4 Lieutenant has a Knot with the RM leader. This creates the political player's genuine dilemma: deep cross-faction relationships are strategically valuable but institutionally dangerous.

**GAP — Cross-faction relationship discovery consequences:** When an NPC faction leader discovers (via Exposure, intelligence, or public observation) that their officer has Disposition ≥ +3 with a rival faction NPC, the faction leader's Disposition with the player shifts by -1 (or -2 for hostile faction contacts). This feeds Standing demotion risk and creates the historically correct dynamic of court politics: the player must manage their patron's perception while cultivating their cross-faction network.

### 3.3 Interpersonal Work → Domain Echo

Domain Echo (scale_transitions §7) is the mechanism by which personal-scale actions produce faction-level consequences. A successful social contest against Himlensendt doesn't just change his Belief — it reverberates through the faction layer.

**How it currently works:** An action produces Domain Echo when it meets the "Sufficient Scope" threshold (the action's consequences affect faction stats, NPC arc transitions, or territorial conditions). The Echo is adjudicated per scale_transitions and modifies faction stats at Accounting.

**The interpersonal input:** The player who spends 3 seasons building Disposition +5 with Almud and then wins a decisive Contest that pushes Almud's Certainty from 3 to 1 produces the following Echo: Crown enters Reformer Arc → Crown-RM co-victory path opens → Church TC acceleration (responds to Crown heresy) → Löwenritter Coup Counter may advance. One interpersonal chain → four faction-level consequences.

**Assessment:** The Echo mechanism is the game's most important interpersonal → political channel. It works because the NPC arc system is mechanically complete — Scar accumulation has defined thresholds that fire defined faction consequences. The gap is that Echo is retrospective (evaluated at Accounting), not immediate. The player doesn't see the faction consequence in the moment of the Contest victory — they see it at season's end. For the videogame, an immediate visual feedback (faction stat delta preview at Contest resolution) would reinforce the connection between interpersonal action and political outcome.

### 3.4 Faction-to-Faction Diplomacy and Internal Consequences

The inspiration document identifies a critical gap: diplomatic actions should produce internal political consequences. The current design specifies diplomatic actions (treaties, NAPs, tribute) but doesn't specify how these affect NPC Dispositions or internal faction dynamics.

**What exists:**
- The Nine Political Axes are qualitative and not tracked numerically. They describe the political landscape but don't generate mechanical effects from diplomatic decisions.
- The Tensions Deck amplifies one friction point per campaign but is drawn at game start, not during play.
- Faction AI priority trees dictate NPC actions based on faction stat thresholds, not on diplomatic relationships.

**GAP — Diplomatic decisions as interpersonal events:** When the player (at Standing 5+, acting in the faction's name) signs a treaty with another faction, each named NPC in the player's faction should evaluate the treaty against their Conviction:

| NPC Conviction alignment with treaty | Disposition with player |
|---|---|
| Treaty serves NPC's primary Conviction | +1 (gratitude/validation) |
| Treaty neutral to NPC's Convictions | +0 |
| Treaty contradicts NPC's primary Conviction | -1 (perceived betrayal of shared values) |
| Treaty benefits a faction the NPC is Opposed to | -2 |

This creates the trilateral court politics dynamic the inspiration document identifies: the player isn't just deciding whether the treaty serves the faction — they're deciding which internal NPCs the treaty empowers and which it alienates. A military alliance with Varfell satisfies Consequentialist-aligned NPCs but frustrates Faith-aligned NPCs in the Crown court.

---

## PART 4: SUCCESSION AS RELATIONAL STRUCTURE

### 4.1 What Exists

Succession is specified in settlement_layer §7.2 (Extended Timeline), faction_politics_expanded (Torben's Readiness Track, Baralta succession), and throughline T-25 (Generational Shift). Named NPCs age (-1/-2/-3 to highest attribute per Generational Shift clock). Succession fires when a leader dies or is incapacitated. At Standing 7, the player can succeed directly.

### 4.2 What's Missing: Anticipatory Succession

The inspiration document's Ottoman succession analysis applies directly. Valoria has the right components — Standing ladder, NPC Convictions, faction institutional structures — but succession is treated as an event that fires on leader death/removal, not as a political force that reshapes behavior throughout the campaign.

**GAP — Succession anxiety as ambient relationship modifier:**

When a faction leader's highest attribute drops below 4 (Generational Shift effect) or the leader enters an arc that signals potential removal (Almud Arc C conditions approaching, Himlensendt Arc B activating):

1. NPCs within the faction begin evaluating potential successors. For Crown: Torben, Ehrenwall (if Coup), or PC (if Standing 7). Each NPC's Disposition with each potential successor becomes politically relevant.

2. NPCs whose Conviction aligns with the current leader's successor (e.g., Faith-aligned Church NPCs who support Himlensendt's designated successor vs. Reason-aligned Cardinals who want change) should shift their behavior: they become less responsive to the current leader's priority tree and more responsive to their preferred successor's anticipated priorities.

3. The player should be able to observe this through Appraise/Read actions: "The Cardinal of Temperance is distracted during our council session. He seems to be thinking about what happens after Himlensendt."

**What this creates:** A persistent governance variable, not a single event. The player managing succession politics throughout the campaign — cultivating relationships with potential successors, building Standing toward succession eligibility, reading which NPCs are positioning for which successor — produces richer political gameplay than the current model where succession fires abruptly on leader removal.

---

## PART 5: INTELLIGENCE AS INTERPERSONAL WEAPON

### 5.1 Current State

Intelligence operations in Valoria work through:
- Varfell Private Collection (Intel vs Ob 2: reveal hidden faction attribute, +2D Thread-related Domain Action, or -1 Ob Einhir Research)
- Settlement-layer intelligence brokers (post-Niflhel dissolution): local Intel ≤ 4, single NPCs
- Exposure system (Cover = Cog + History; Exposure accumulates through covert actions)
- Investigation (Evidence Track with Simple/Complex/Structural thresholds)

**What's specified for interpersonal intelligence:** The Appraise action in social contests reveals NPC Conviction and Resonant Style. Read action in socializing reveals Disposition, Beliefs, emotional state. These are personal-scale intelligence tools.

**What's missing:** Active influence operations — the ability to use interpersonal relationships to degrade an enemy NPC's loyalty or Disposition with their faction leader. The inspiration document's tiered intelligence model (Information → Influence → Recruitment) maps well onto Valoria's existing architecture:

**GAP — Influence operations as social actions:**

Tier 1 (Information, existing): Appraise + Read reveal NPC state. Investigation reveals evidence.

Tier 2 (Influence, new): A player with Disposition +2 or higher with a target NPC in a rival faction can attempt to shift that NPC's Disposition with their own faction leader. Mechanism: Converse action, Ob = target NPC's Stability-equivalent (Certainty for personal stability) + 1. Success: target NPC's Disposition with their faction leader decreases by 1. This represents manufactured grievance — the player plants doubts about the leader's competence, fairness, or priorities without explicitly recruiting the NPC.

Tier 3 (Recruitment, partially existing): NPC Recruitment (complete_systems_reference §1.12) requires Cha×2+H+3 pool, Ob = floor(NPC highest Disp/2)+1. This targets NPCs whose loyalty is already low. Tier 2 operations lower that loyalty to make Tier 3 viable.

**What this creates:** Intelligence becomes an interpersonal campaign, not a single roll. The player spends seasons building Disposition with a rival NPC, then uses that relationship to erode the rival NPC's institutional loyalty, then recruits them when their loyalty is critically low. Each stage is a choice with consequences — the Exposure system means that spending time with rival NPCs is detectable, and a botched Influence operation (Failure on Converse targeting NPC-leader Disposition) could alert the rival faction to the player's intentions.

---

## PART 6: STRUCTURAL GAPS SUMMARY

| # | Gap | Severity | Systems affected | Resolution complexity |
|---|---|---|---|---|
| G-1 | **NPC-NPC horizontal relationships unmodeled** | High | Faction AI, inner-circle dynamics, coalition formation, Settlement politics | Medium — simplified 3-state system (Aligned/Neutral/Opposed) computed at Accounting from Conviction overlap + recent actions |
| G-2 | **Standing advancement lacks Disposition gates** | Medium | Player progression, faction politics, governance access | Low — add minimum Disposition thresholds to Standing 3/5/7 promotion requirements |
| G-3 | **Settlement interpersonal loyalty → faction stat feedback absent** | Medium | Settlement governance, faction Stability/Mandate, holdout mechanics | Low — extend existing holdout mechanic (§6.3) to continuous effect: well-governed settlements with high NPC Disposition resist subversion |
| G-4 | **Diplomatic decisions don't produce NPC Disposition shifts** | High | Diplomacy, internal faction dynamics, court politics | Medium — treaty/alliance decisions evaluated per NPC Conviction at Accounting; +1/-1/-2 Disposition shifts |
| G-5 | **Succession is event, not structure** | Medium | NPC behavior, faction AI, player strategic planning | Medium — succession anxiety modifier when leader attributes decline or arc removal conditions approach |
| G-6 | **Cross-faction relationship discovery has no internal consequence** | Medium | Exposure, faction loyalty, Standing, court politics | Low — faction leader Disposition shift (-1/-2) on discovering officer's deep cross-faction contacts |
| G-7 | **Intelligence lacks active influence tier** | Medium | Intelligence operations, NPC loyalty, cross-faction subversion | Medium — new social action to degrade rival NPC's Disposition with their own leader via manufactured grievance |
| G-8 | **Companion-governor Conviction → settlement Framework Drift unspecified** | Low | Companion system, settlement governance, Framework Drift | Low — companion-governor's dominant Conviction shifts settlement's implicit framework alignment over time |

### Priority Assessment

**G-1 (NPC-NPC horizontal relationships)** and **G-4 (diplomatic → NPC Disposition)** are the highest-impact gaps. Together they represent the absence of court politics as a system: NPCs don't form opinions about each other, and faction-level decisions don't cascade into interpersonal consequences. Resolving these two produces the trilateral court dynamic identified in the inspiration document — every political decision empowers some courtiers and alienates others, and courtiers form coalitions independent of the ruler's intent.

**G-5 (succession as structure)** is the highest-narrative-value gap. Valoria's 30-year game span (T-25) means succession is not a late-game event but a persistent political force. The game already has the components (Standing ladder, Generational Shift clock, NPC arc emergence) — what's missing is the connective tissue that makes anticipatory succession reshape NPC behavior before the succession event fires.

**G-2, G-3, G-6** are low-complexity additions that extend existing mechanics. They don't require new systems — they add Disposition thresholds and consequence tables to mechanics that already exist.

**G-7 (intelligence as influence)** extends the social action system into cross-faction subversion. It's moderate complexity but high engagement value — it gives the player a political tool beyond direct confrontation and opens the intelligence game to non-combat characters.

---

## PART 7: WHAT THE DESIGN GETS RIGHT

The audit should not only surface gaps. Several interpersonal → political chains are well-designed:

1. **Scar → Arc → Faction chain (T-23):** The best interpersonal-to-political throughline in the design. Personal-scale Contest victories accumulate Scars on NPCs, Scars trigger arc transitions, and arc transitions reshape faction behavior. This is mechanically complete and produces emergent political narrative.

2. **Bonds as structural gate:** The Bonds attribute simultaneously caps Disposition ceiling, max Knot count, and Knot formation eligibility. One attribute controls the player's entire relational capacity. This is elegant — it forces a meaningful creation choice without requiring a separate trust/loyalty/capacity subsystem.

3. **Sincerity Gate (37% failure rate):** Prevents instrumental relationship farming. The player who approaches NPCs purely for political advantage risks detection (Spirit check failure → Disposition decrease or stagnation). This mechanically produces the tension between genuine and strategic relationship-building.

4. **Advisor-Principal Confidentiality (ED-664):** Models the historical distinction between private counsel and public loyalty. The Knot-mediated counsel extraction (single attempt per campaign) creates a genuine climactic political moment — the player must choose the right moment to cash in their deepest relationship for actionable intelligence.

5. **Scene Slate as political triage:** The player's 3–5 scene actions per season force choices among competing NPC Outreach and Demand scenes. These choices are implicitly political — attending Almud's Outreach while ignoring Baralta's creates Disposition consequences that accumulate over seasons.

6. **Stature Ladder mapping to governance scope:** The progression from nobody (Standing 0) to national actor (Standing 7) through accumulated deeds and relationships is the game's answer to player agency at political scale. The ladder is concrete enough for videogame implementation while preserving the feeling of earned political power.

---

## PART 8: VIDEOGAME IMPLEMENTATION NOTES

For each gap, what does the player see vs. what does the engine compute?

### G-1 (NPC-NPC Relationships)
**Player sees:** NPC dialogue referencing other NPCs ("Ehrenwall has been avoiding the Spymaster lately"). Inner-circle scenes where NPCs argue with each other. Coalition indicators in the faction UI (icons showing which NPCs are aligned/opposed).
**Engine computes:** 3-state matrix updated at Accounting. AI priority tree modified by NPC-NPC state (an NPC who is Opposed to the player's ally may refuse to execute Domain Actions that benefit the ally's settlement).

### G-4 (Diplomatic → NPC Disposition)
**Player sees:** After signing a treaty, a notification: "Cardinal of Fortitude disapproves of the Varfell alliance. (-1 Disposition)." Inner-circle scenes where NPCs argue about the treaty's merits.
**Engine computes:** Treaty evaluated against each inner-circle NPC's primary Conviction. Disposition shifts applied at treaty signing, not Accounting (immediate feedback reinforces the connection between diplomatic decisions and interpersonal consequences).

### G-5 (Succession Anxiety)
**Player sees:** NPCs mentioning succession in Outreach scenes. Read action revealing "anxious about the future" emotional state. Inner-circle members visibly positioning — attending the heir's events, seeking the heir's favor.
**Engine computes:** Ambient loyalty modifier applied when leader's highest attribute < 4 or leader's arc approaches removal branch condition. NPCs with Disposition ≥ +2 toward a specific successor shift priority tree weighting toward that successor's anticipated preferences.

### Domain Echo Visualization
**Player sees:** At Contest resolution (the moment of victory), a brief faction-stat delta preview: "Crown Stability -1 at Accounting. Church TC acceleration +1/season." This connects the interpersonal moment to its political consequence immediately rather than waiting for Accounting.
**Engine computes:** Already computed (Domain Echo evaluation). The addition is UI: surfacing the Echo at the moment of the triggering action rather than burying it in the Accounting phase.
