<!-- DEPRECATED: 2026-04-09 — SUPERSEDED BY designs/board_game/valoria_bg_v05_simulation_and_patches.md. Do not use as a mechanical reference. Retained for audit trail only. -->

# VALORIA BOARD GAME — IMPROVEMENT ANALYSIS V3
## Date: 2026-03-31
## Builds on: bg_improvement_v1.md, bg_improvement_v2.md
## Games: The Quiet Year, Nemesis, Kingdoms Forlorn, Eldfall Chronicles, Heroes of Might and Magic, Under Our Sun, New Cold War, Crisis

---

## LANDMARK GAME ANALYSIS — THIRD WAVE

| Game | Core Mechanic | Valoria Application |
|------|--------------|---------------------|
| **The Quiet Year** | Community-building map game; Projects; Contempt tokens; Frost Shepherds countdown | Revolution faction complete redesign; multi-season Projects; Contempt as inter-faction pressure |
| **Nemesis** | Hidden personal objectives; Noise/Attention mechanic; infection spread; semi-cooperative betrayal | Secret secondary objectives per faction; Thread Contamination spread; Church Attention pool |
| **Heroes of Might and Magic** | Hero champions amplify armies; multi-resource economy; castle upgrade tree; spell books | Named leader units as mobile commanders; multi-resource economy; faction upgrade paths |
| **New Cold War** | Proxy warfare; influence without presence; brinkmanship escalation; ideological spread | Proxy Support system; Influence tokens in uncontrolled territories; IP as brinkmanship track |
| **Crisis** | State player with policy instruments affecting all; worker welfare; investment cycles | Crown as policy actor affecting all factions; unit morale/supply tied to territory welfare |
| **Kingdoms Forlorn** | Persistent campaign consequences; faction-specific unit types with thematic identity | Campaign legacy tokens; unit type identity per faction (not generic infantry) |
| **Eldfall Chronicles** | Card-driven action selection; civilization asymmetry through card distribution | Faction Political Hands driven by card acquisition, not fixed deck |
| **Under Our Sun** | [Low confidence — see note] | Flagged — cannot verify mechanics with confidence |

*Note on Under Our Sun: insufficient familiarity with this specific title to produce reliable analysis. If you can describe the relevant mechanic, I can apply it.*

---

## MECHANIC PROPOSALS — THIRD WAVE

### MP-21: COMMUNITY PROJECTS — The Quiet Year
**Addresses:** G-BG-04 (Thread passive), G-BG-05 (Revolution asymmetry), setting coherence
**Inspired by:** The Quiet Year (multi-week Projects as ongoing investments)

The Quiet Year's Project mechanic allows players to start something that will take multiple turns — a structure, a plan, a relationship — and place markers tracking its progress. Critically: Projects can be disrupted by other players or by world events before completion. The tension between starting Projects and defending them is the game's engine.

For Valoria, this maps directly to the Revolution AND to the three clocks — which are themselves collective Projects that multiple factions are building or opposing simultaneously.

**Community Projects (Revolution primary; any faction secondary):**

A faction may start a **Project** in any territory they have presence in. Projects are represented by a marker on the territory with a **Progress Track** (1–5, depending on scope).

Each season, a faction with presence in the Project territory may advance it by 1 (no order required for Revolution; costs 1 Domain order for other factions). Projects are disrupted if:
- Military action occurs in the territory (Battle in territory: Progress −2)
- The territory changes control (Progress −1)
- Heresy Investigation is opened there (Church presence: Progress −1/season)

**Project types:**

| Project | Scope | Effect on Completion |
|---------|-------|---------------------|
| Community Weave | 3 seasons | RS +2; Revolution Influence +2 in territory; creates a permanent Thread Resonance node (+1 TR/season to all factions with presence here) |
| Einhir Memory Recovery | 4 seasons | Reveals one historical fact about the Calamity (GM introduces as narrative hook); TK +1 to any faction that contributed; RS +1 |
| Restoration Network | 5 seasons | Revolution gains a permanent Presence in 2 adjacent territories even if disrupted (the network survives); IP −1 (Altonian agents note community stability) |
| Fortification (any faction) | 3 seasons | Territory Fort +1 at no Wealth cost (community labor replaces capital investment) |
| Diplomatic Mission (any faction) | 2 seasons | Target faction: Reputation +1 with all factions on completion; deal negotiations at −1 Ob next season |

**The Frost Shepherds equivalent:** The RS Rupture IS Valoria's Frost Shepherds — the slow inevitable doom that all Projects race against. Projects near Thread Wound territories (T12, T13) advance 1 faster each season (urgency of decay). Projects at RS < 40: all Progress checks gain +1 (the world is failing; people act faster).

**Canon compliance:** P-01 (Thread operations have consequences). Community Weave is a Thread operation with full co-movement. The Restoration Network and Einhir Memory Recovery are rendered-side activities, not Thread operations — they interact with the Thread world through information and community, not manipulation. PASS.

---

### MP-22: CONTEMPT TOKENS — Inter-Faction Pressure
**Addresses:** G-BG-02 (negotiation thin)
**Inspired by:** The Quiet Year (Contempt mechanic)

In The Quiet Year, when a player strongly disagrees with another player's action, they may give them a Contempt token. When a player accumulates enough Contempt, their contributions to discussions are ignored. It is a social-mechanical pressure system — disagreement has mechanical teeth.

In Valoria, **Contempt tokens** represent accumulated political grievances between factions.

**Gaining Contempt:**
- A faction receives a Contempt token from another faction when:
  - They break a Deal Pledge (MP-02)
  - They execute Brutal disposition against Valorian civilians
  - They seize territory from a faction they were previously allied with
  - The Church excommunicates a faction leader
  - Niflhel's operation is traced back to them

**Contempt effects:**
- Each Contempt token: −1 Reputation with the issuing faction (permanent until cleared)
- At 3+ Contempt tokens from one faction: that faction's Diplomacy orders targeting you automatically fail (no roll; they won't negotiate while this aggrieved)
- At 5+ total Contempt from all factions combined: faction cannot form alliances or receive Deal Tokens from any faction this season

**Clearing Contempt:**
- 1 Contempt cleared per season: spend 1 Wealth + 1 Influence order as public gesture of goodwill
- All Contempt from one faction cleared: deliver 2 Wealth directly to that faction as reparation + Diplomacy Overwhelming success

**Design effect:** Creates accumulated social history between factions. A Crown that breaks treaties and brutalizes territories accumulates Contempt that eventually makes them politically isolated — not just punished in a single round, but structurally cut off from alliance mechanics.

---

### MP-23: HIDDEN SECONDARY OBJECTIVES
**Addresses:** G-BG-10 (information asymmetry), replayability
**Inspired by:** Nemesis (hidden personal objectives — you might not be cooperating)

Each faction draws one **Secondary Objective card** at game start. These are kept secret. Secondary Objectives are checked only at game end — they score additional points or provide a secondary win path.

**Secondary Objective examples (2 per faction = 12 cards; shuffle all 12; each faction draws 1):**

*Crown cards:*
- *Legacy of Order:* At game end, if no Valorian faction has been eliminated (Stability 0), +4 VP.
- *Martial Supremacy:* At game end, if Crown has the most military units in play, +3 VP + Coup Counter reset to 0 permanently.

*Church cards:*
- *The Reckoning:* At game end, if the Church has excommunicated at least 2 faction leaders this game, +4 VP.
- *Sanctified Ground:* At game end, if Church controls Himmelenger continuously since turn 1, +4 VP.

*Hafenmark cards:*
- *Precedent Set:* At game end, if Hafenmark has at least 3 Parliamentary rulings in their favour, +4 VP.
- *Sovereign Proven:* At game end, if Baralta was never successfully excommunicated, +5 VP.

*Varfell cards:*
- *The Complete Picture:* At game end, if Varfell has revealed stats from all 5 other factions at least once, +4 VP.
- *Thread Scholar:* At game end, if TK = 5, +5 VP regardless of whether Varfell meets their primary victory condition.

*Guilds cards:*
- *Market Dominance:* At game end, if Guilds have active trade relationships in 4+ territories, +4 VP.
- *Necessary Evil:* At game end, if Guilds are the only faction that has never fought a battle, +5 VP.

*Niflhel cards:*
- *Perfect Record:* At game end, if no Niflhel arm was ever publicly compromised, +5 VP.
- *Everyone Has a Price:* At game end, if Niflhel has at least 1 Contempt token from every other faction, +4 VP (being universally distrusted is their success state).

**Secondary Objectives in shared survival:** If shared survival condition fails, Secondary Objectives score 0 — there is no individual "winning" when the world is gone.

**Canon compliance:** PASS. Secondary Objectives are private political ambitions, fully consistent with the faction ethical frameworks.

---

### MP-24: ATTENTION POOL — Nemesis Noise Mechanic
**Addresses:** G-BG-04 (Thread passive), setting coherence
**Inspired by:** Nemesis (intruder noise mechanic — your actions generate a measurable threat response)

In Nemesis, every action generates "noise" that is tracked on a track. When noise accumulates past thresholds, intruders activate. Players must balance doing things (which generates noise) with keeping quiet (which doesn't advance their objectives).

For Valoria: the **Church Attention Pool** tracks how much Thread and heretical activity the Church has detected this season.

**Church Attention Pool (0–10 per season):**

The pool accumulates from:
- Any Thread operation in a non-Church-controlled territory: +2 Attention
- Niflhel operations: +1 Attention per operation (covert activity disturbs Church networks even when unattributed)
- Einhir artefact surfaces (C-13 event): +2 Attention
- Revolution Community Weaving in Church-adjacent territory: +3 Attention
- Any faction with TR ≥ 3: +1 Attention per faction at that level
- RS dropping below a threshold: +1 Attention per threshold crossed

**At Attention thresholds:**
| Pool | Church Response |
|------|----------------|
| 3 | Church opens one Heresy Investigation anywhere (free, no order slot) |
| 5 | Church TC +1 (institutional response to perceived heretical surge) |
| 7 | Church activates Inquisitor protocol: all Thread-active factions take −1D to covert/Intel orders this season (Church surveillance heightened) |
| 10 | Church Crusade declared: Church may deploy Templar units anywhere in their territory without a Muster order this season |

**Pool resets** at Seasonal Accounting (surveillance is episodic, not cumulative).

**Church player / NPC interaction:** If Church is player-controlled, the Attention Pool is public information — they know how agitated their institution is. Player Church may choose to NOT respond to a threshold (Stability check Ob 1 to suppress institutional response — the Confessor holding back the zealots). NPC Church always responds to thresholds.

**Canon compliance:** The Church monitoring Thread activity is a rendered-world institutional behavior. The pool doesn't imply Thread agency or ground responsiveness. PASS.

---

### MP-25: HERO CHAMPIONS — Heroes of Might and Magic
**Addresses:** G-BG-05 (asymmetry), G-BG-09 (hybrid interface)
**Inspired by:** HoMM (hero units as mobile army commanders with growing capabilities)

Each faction has a **named Champion** (their faction leader as a mobile unit). The Champion is not just a stat block on the faction card — they are a deployable token that moves with the faction's military forces.

**Champion rules:**
- One Champion per faction (the named leader: Almud, Baralta, Inge Baralta, Vaynard, etc.)
- The Champion occupies a territory and provides bonuses to all friendly units there.
- Champions cannot be killed (they retreat when forces are routed) but can be captured.
- Champions move via March order at no additional cost (they travel with units or alone).

**Champion bonuses (base, all factions):**
- Units in Champion's territory: +1D to all rolls
- Stability checks in Champion's territory: −1 Ob
- Diplomacy orders executed by Champion: +1D

**Champion unique abilities (faction-specific, level up via play):**

Champions gain **Renown** (0–5) from victories, successful rolls while present, and narrative events. Renown unlocks abilities.

| Champion | Renown 1 | Renown 3 | Renown 5 |
|----------|----------|----------|----------|
| Almud (Crown) | Royal Presence: TC −1 while in Valorsplatz | Succession Weight: Torben Loyalty check −1 Ob | Virtue Embodied: all Church Excommunications against Almud require Mandate 6+ |
| Himlensendt (Church) | Pulpit Authority: Preach in Champion's territory auto-Success | Inquisitor's Gaze: +2D to Heresy Investigation | Doctrinal Command: TC +1 each season Champion is in Himmelenger |
| Baralta (Hafenmark) | Legal Precedent: Parliamentary Manoeuvre +1D | Sovereign Voice: once per game, Sovereign Authority costs no order slot | Constitutional Anchor: if Baralta present, TC cannot rise above 65 |
| Vaynard (Varfell) | Einhir Eye: +1 TK when Collection used in Varfell | Analytical Mind: Intel orders in Champion's territory: Overwhelming on 2+ successes | Archive Mastermind: all hidden stats revealed to Varfell permanently at Renown 5 |
| Guildmaster (Guilds) | Contract Security: contracts cannot be broken in Champion's territory | Market Sense: Trade Overwhelming on any Success in home territory | Economic Web: Guilds Wealth cannot be reduced below 3 while Champion is in play |
| Network (Niflhel) | [EDITORIAL: Niflhel has no single leader; Champion mechanic may not apply. Options: (a) each arm has a champion with limited stats; (b) Niflhel's "champion" is their accumulated Network Depth; (c) skip Champion for Niflhel as an expression of their headless structure.] | — | — |

**Champion capture:** If a faction's territory is taken by force while their Champion is present: Champion is captured. Held by the capturing faction. Captured Champion: the faction loses all Champion bonuses. Rescue: successful military action against capturing faction in their territory. Ransom: 3 Wealth + 1 Influence; Champion returns next season.

**Hybrid integration:** When a TTRPG Zoom-In occurs in a territory where the Champion is present, the Champion's stats (from compilation/stage13_npcs.md or faction card) are used directly in the personal-scale scene. The BG Champion token becomes a TTRPG PC/NPC instantiation.

**Canon compliance:** Named leader units as mobile commanders are fully rendered-world. PASS.

---

### MP-26: PROXY SUPPORT — New Cold War
**Addresses:** G-BG-02 (negotiation), G-BG-05 (asymmetry)
**Inspired by:** New Cold War (proxy warfare — influence without direct presence; brinkmanship)

In the Cold War, superpowers rarely fought each other directly. They funded, armed, and supported proxy factions while maintaining plausible deniability. The actual conflict happened in "neutral" territories where both sides had influence but neither had presence.

In Valoria, **Proxy Support** allows a faction to fund or arm another faction (or even a non-player force) in exchange for aligned action — without officially committing military force.

**Proxy Support procedure:**
1. During Diplomacy order resolution, a faction may secretly designate another faction as a Proxy. They pay 1–3 Wealth (sealed; revealed later).
2. The supported faction executes one order of their choice this season; the supporting faction's Wealth investment makes the roll at +1D per Wealth point spent.
3. If the Proxy's action achieves its intended result: the supporting faction gains 1 Influence in the target territory (covert influence from the proxy operation's success).
4. If the Proxy fails or refuses: supporting faction's Wealth is lost; no Influence gained.
5. **Attribution:** The Proxy's action is publicly visible; the Wealth source is not. Successful Intel vs Ob 3 reveals the support relationship. If revealed: supporting faction takes Contempt +1 from the targeted faction.

**Application to Revolution:** Revolution is the natural Proxy target. Any faction may quietly fund Community Weaving or Influence expansion in Revolution territory while maintaining political distance from the Restoration movement. This models how Varfell (and historically sympathetic nobles) support the Revolution without declaring alignment.

**IP as brinkmanship track:** The New Cold War's arms race mechanic maps directly to Valoria's IP track. As IP rises, the "cost" of Altonian involvement decreases — they are drawn in. The brinkmanship mechanic: at IP 60+, any faction may make a **Grand Gesture** (spend 3 Influence) to attempt IP −5 by demonstrating Valorian unity. If the gesture fails (the demonstration is visibly hollow): IP +3 instead. High-risk, high-reward diplomatic play.

**Canon compliance:** Proxy support is a rendered-world political mechanic. PASS.

---

### MP-27: CROWN AS POLICY ACTOR — Crisis
**Addresses:** G-BG-05 (asymmetry), Crown faction depth
**Inspired by:** Crisis (the State player manages policy instruments affecting all other factions)

In Crisis, the State player doesn't simply compete — they regulate the environment in which all other players operate. Their actions are policy decisions: set tax rates, manage debt, issue subsidies. Other players must adapt to the State's decisions.

Crown is structurally the closest Valorian equivalent: they hold Parliament, issue Decrees, and nominally govern the kingdom. Yet currently Crown uses the same order system as everyone else, just with better Mandate.

**Crown Policy Instruments (replace or augment existing Decree order):**

Each season, Crown may issue one **Policy** in addition to their normal orders. Policies affect the entire board, not just Crown's territories. Policies last 1 season unless renewed.

| Policy | Effect | Downside |
|--------|--------|----------|
| *Royal Taxation* | All Trade orders this season generate 1 additional Wealth for Crown | All non-Crown factions: Trade Ob +1 this season (taxation overhead) |
| *Conscription Mandate* | Any faction Mustering this season may do so at −1 Ob | All mustered units are "conscripted" — begin at Cohesion −1 until their first Govern order seasons later |
| *Free Trade Decree* | IP −1 (Altonian trade encouraged); all Schoenland Trade orders this season: +1D | Church TC +1 (Crown signals openness to Altonian influence) |
| *Curfew* | All Intel/Covert orders in Crown-controlled territories: +2 Ob | Niflhel gains Leverage +2 immediately (security crackdown drives underground activity deeper) |
| *Parliamentary Session* | All factions may execute one additional Diplomacy order this season (Parliament called) | Crown Mandate check Ob 1 — failure: Crown Mandate −1 (Parliament turned against them) |
| *Emergency Powers* | Crown executes one order without revealing it during planning (placed face-down; revealed at resolution) | Hafenmark gains Parliamentary Manoeuvre use for free this season in response; Church TC +1 |

**Policy constraints:**
- Crown may only issue a Policy while Mandate ≥ 4.
- Same Policy cannot be issued in consecutive seasons (Decree fatigue already modeled; extend to Policy).
- Any faction may oppose a Policy via Diplomacy Ob 3: Success = Policy effect halved. Overwhelming = Policy blocked entirely this season.

**Crown uniqueness:** No other faction can issue Policies. This is Crown's core structural asymmetry — they are the policy-setting entity in Valorian governance. A Crown that neglects Policies in favor of pure military play is mechanically under-resourced.

**Canon compliance:** Crown as policy actor is fully rendered-world governance. PASS.

---

### MP-28: UNIT IDENTITY — Kingdoms Forlorn / Eldfall Chronicles
**Addresses:** G-BG-05 (asymmetry), thematic coherence
**Inspired by:** Kingdoms Forlorn and Eldfall Chronicles (faction-specific unit types with thematic identity; not generic "Light Infantry")

Current unit types (Light Infantry, Heavy Infantry, Cavalry, etc.) are generic. Kingdoms Forlorn and Eldfall Chronicles give each faction's units thematic identity that expresses their faction's nature in the unit design itself.

**Proposed faction-specific unit names and unique properties:**

| Faction | Unit Tier 1 | Unique Property | Unit Tier 2 | Unique Property |
|---------|------------|-----------------|------------|-----------------|
| Crown | Royal Levy | Standard; if Champion present: +1D | Royal Guard | Elite; cannot be Routed while Almud is in same territory |
| Church | Parish Militia | Standard; Contempt to Church: +1 per Militia lost in battle | Knights Templar | Elite; immune to Co-Movement card Cohesion penalties; +2D vs practitioners |
| Hafenmark | Ducal Marines | +1D in coastal/port territories (Hafenvalor, Lowenskyst) | Baralta's Household | Elite; if defending: Defensive disposition always at base Ob (no penalty from table) |
| Varfell | Highland Scouts | +1D Intel order in any territory they occupy | Mountain Infantry | Cohesion 5; −1 Ob when defending in Varfell or adjacent highland territories |
| Guilds | Hired Blades | Wealth cost to deploy; +1 Martial if 2+ Wealth spent | Veteran Contractors | Cohesion recovers at year-end without Govern order (self-sustaining mercenaries) |
| Niflhel | Street Enforcers | Network Depth +1 in territory after winning a battle | Shadow Operators | Intel orders in their territory: Partial counts as Success |
| Revolution | [No standard units — see MP-18 Presence redesign] | — | Community Wardens | Emerge when RS < 40; Cohesion 3; cannot be permanently destroyed (return via Community Weaving) |
| Löwenritter | Iron Knights | Elite; immune to Rout this battle if Coup Counter < 4 | Grandmaster's Guard | Cannot be taken prisoner; Formation Break once only — second break = destroyed, not routing |

**Canon compliance:** Unit naming is setting-expression, not metaphysical claim. PASS.
**[EDITORIAL: Unit names and faction-specific properties — setting decisions. Particularly "Community Wardens" for Revolution (implies organized defense capacity; need to verify against Revolution's Rawlsian framework and P-04 non-moral entity design).]**

---

## CROSS-WAVE SYNTHESIS

After three analysis waves (V1–V3), the complete picture of Valoria BG's gap landscape:

**The core problem, restated:** The current BG is mechanically coherent but plays like a medium-weight Euro with a fantasy skin. The Thread system, the Philosophical Foundations, and the faction ethical frameworks are present as text but don't *drive* gameplay decisions the way the setting deserves. Players can win without ever thinking about RS.

**The five changes that would most transform play:**

1. **MP-18 + MP-21 (Hegemony + Quiet Year):** Radical faction asymmetry, especially Revolution. Revolution should feel like a completely different game being played on the same board. Community Projects make the Thread's materiality visceral — it's not just a number degrading, it's a thing communities are working to heal.

2. **MP-24 (Nemesis):** Church Attention Pool. Thread operations should feel *dangerous* — not just costly to the acting faction, but watched. The Church is the world's surveillance apparatus for Thread activity. Making that mechanical transforms the tension of every Thread operation.

3. **MP-25 (HoMM):** Champions. Named leaders on the board are the bridge between BG and TTRPG. Every Zoom-In condition has a physical token to point at. Almud in Valorsplatz is not an abstraction — he's a token that can be captured.

4. **MP-27 (Crisis):** Crown as Policy Actor. Crown should feel like governing — not just Governing one territory per season, but setting the conditions for everyone else's play. This is what makes Crown worth playing.

5. **MP-03 + MP-12 (Inis + Anachrony):** Deed Tokens (already integrated) + Thread Debt. Victory should feel close and threatened, not distant and accumulated. Thread Debt gives Thread operations weight — you can push the world, but it pushes back.

---

## EDITORIAL FLAGS ADDITIONS (V3)

| ID | Item | Blocking? |
|----|------|-----------|
| BG-E-24 | MP-21: Community Project types — setting/content decisions | Yes |
| BG-E-25 | MP-23: Secondary Objective card text per faction (12 cards) | Yes |
| BG-E-26 | MP-25: Niflhel Champion handling (arm model vs skip) | Yes |
| BG-E-27 | MP-25: Champion Renown ability text — all factions | Yes |
| BG-E-28 | MP-28: Unit names and faction-specific properties | Low — naming decisions |
| BG-E-29 | MP-28: Revolution "Community Wardens" — verify against P-04 and Rawlsian framework | Low |

---

## CONSOLIDATED NON-EDITORIAL READY-TO-IMPLEMENT LIST (all waves)

These proposals require no editorial decisions and can be integrated into stage_bg on confirmation:

| Proposal | What |
|----------|------|
| MP-12 | Thread Debt tokens for temporal operations |
| MP-14 | Leverage tokens from being targeted |
| MP-16 | Conviction invocation + Crisis in BG |
| MP-22 | Contempt tokens |
| MP-24 | Church Attention Pool |
| MP-26 | Proxy Support + Grand Gesture brinkmanship |
| MP-27 | Crown Policy Instruments (6 policies) |

These can all go into stage_bg in one integration pass.

---

*V3 complete. 8 additional mechanic proposals (MP-21 through MP-28). Total across all waves: 28 proposals.*
*Note: Under Our Sun not analyzed — insufficient mechanic familiarity. Provide mechanic description for targeted application.*
