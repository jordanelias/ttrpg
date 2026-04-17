# VALORIA — NPC-as-Player Campaign Simulations
**Date:** 2026-04-16  
**Token:** 340ad4e30f5b1e35  
**Scope:** Campaign-length (30-season) skeleton simulations for all 11 major named NPCs played as the player character. Tests patch register mechanics (FAC-01/02, SUC-01-03, LIN-01-04, COUP-01-02, POW-01-03, NPC-01-04, OFC-01-04, REN-01-03, MIN-01-06) against existing canonical system.  
**Source documents:** faction_politics_patch_register_2026-04-16.md (PROPOSAL — awaiting approval), npc_behavior_v30.md, companion_specification_v30.md, player_agency_v30 (inferred), scale_transitions_v30.md, combat_v30.md, threadwork_v30.md  
**Design premise corrected this session:** High-status NPCs (Kings, Confessors) are institutional leaders, not companion candidates. Their Availability State (NPC-01), Authority Gradient (NPC-02), and Deference Hierarchy (NPC-04) make them inaccessible to low-Standing players. Playing AS them is the natural mode for players who want faction-leader perspective.

---

## METHODOLOGY

**Player-as-NPC means:**
- The player starts with the NPC's full Conviction, stats, Inner Circle, and faction standing baked in. No origin arc, no acquisition scene. You ARE this person from Session 1.
- The NPC's BG priority tree becomes the player's *agenda* — but the player may deviate (at Leadership Deviation cost). This is the primary tension: your institutional role vs. your Conviction.
- World events hit the player directly. Church TC advancing to 40 is not "a thing happening to the map" — if you are Baralta, it is an immediate existential threat to your constitutional position.
- The player's Availability State (NPC-01) runs in reverse: you are "In Session" by default. Other players/NPCs must approach you through the correct channels.
- Delegation (NPC-03) is the primary scene-generation mechanic: you send agents, review reports, and make decisions based on delegated intelligence. Fieldwork is for your agents, not for you.

**Simulation structure per NPC:**
- Starting state (stats, rank, obligations, inner circle)
- Season structure (what a typical season looks like from the inside)
- Three-phase arc (S1–10, S11–20, S21–30)
- Three stress tests (granular probability resolution)
- Findings and gaps

**Patch register status:** All FAC/SUC/LIN/COUP/POW/REN/NPC/OFC/MIN patches are proposals. This simulation tests them against the canonical engine. Findings logged as POL-* EDs.

---

## NPC 01 — KING ALMUD ALMQVIST (Crown)

### Starting State
**Standing:** 5 (Reichsseneschall — faction leader). The rank ladder's top tier is your starting position, not your destination.  
**Stats:** Cognition 4, Charisma 5, Agility 2, STR 2, Endurance 3. Combat Pool: 9D.  
**Faction state:** Crown Mandate 5, Influence 5, Wealth 4, Military 4, Stability 5. TCV 12. TC: 28 at campaign start.  
**Conviction:** Order (primary), Reason (secondary, private). Certainty 3. TS 0 (per §7.10).  
**Ethical Framework:** Virtue Ethics — Aligned: public, visible, virtuous action (−1 Ob). Contradictory: covert/expedient action (+1 Ob).  
**Inner Circle (SUC-01):** Royal Marshal (Order, military deference), Lord Treasurer (Precedent, fiscal conservatism), Archbishop's Representative (Faith, TC monitor), Torben (Continuity, heir-as-co-legitimator), Captain of Royal Guard (Autonomy, Löwenritter liaison).

### Season Structure
**Priority tree as player agenda:**
1. IF Stability ≤ 2 → Govern (Inward)
2. IF Coup Counter ≥ 3 → Royal Guard counter
3. IF PI ≥ 10 → Parliamentary Manoeuvre
4. IF Torben Loyalty ≤ 2 → Dynasty management
5. IF TC ≥ 50 → Suppress Church
6. IF hostile Mandate ≥ Crown → Royal Decree
7. DEFAULT → Senator (Outward, Diplomacy)

**Departure from tree** = Leadership Deviation cost (Virtue Ethics Framework: if Almud acts covertly → +1 Ob AND Stability check at next Accounting). Player deviating from Priority 1–3 triggers this.

**Scene slate for faction leader (In Session default):**
- Mandatory: One Royal Audience per Ceremonial Scene cycle (REN-02). All Crown inner circle NPCs present as observers. Player navigates deference hierarchy on their own home turf.
- Mandatory: Duty cycle — 2 inner circle Duty scenes per year-arc (per Standing 5 obligation).
- Delegated: Marshal fieldwork reports (NPC-03). Player reviews, approves, redirects. Does NOT accompany.
- Optional: Parliamentary Manoeuvre (player initiates motion; scene at Parliament). Ceremo scale.
- Optional: Coup Counter management (private meeting with Ehrenwall — she is inner circle-adjacent; requires her Availability State to be In Session or Private Retreat, and Almud's relationship to get there).

### Phase 1 (S1–10): Order Maintained, Certainty Eroding

Almud begins with Certainty 3 — already questioning. His private secondary Conviction (Reason) is suppressed institutionally. The player's first meaningful tension: Almud sees things in the BG layer that contradict his public Order stance.

**S1–4:** Priority 8 Default fires. Almud (player) runs Diplomacy with Guilds (nearest ally). Crown maintains Mandate 5. TC 28→31 under Church pressure (Church Assert pattern confirmed from prior sim). Almud's Virtue Ethics Framework: every Diplomacy scene is "public, visible, virtuous" — −1 Ob on all social scenes he participates in. He rolls 5 Charisma + 1 Virtue bonus = effectively 6D in public social contests.

**S5:** PI from Church-Crown tension reaches 8 (Parliament becoming restive). Priority 3 fires: Parliamentary Manoeuvre. Player must conduct a Ceremonial Scene (Parliament Convening). All inner circle present. At a Parliament Convening: player's contest outcomes have Renown ±2 (REN-02). If player wins the Parliamentary motion: Crown Renown +2. If player loses publicly: Renown −2 AND Disposition −1 with every attending NPC.

**Key dynamic — Torben Loyalty track (S6–8):** Torben starts at Loyalty 3. Church begins Dynasty pressure (Priority 4 Church AI: Himlensendt sends Archbishop's Representative to build Church-Crown alignment through Torben). Player (Almud) must respond: invest scene actions in Dynasty management (Priority 4 fires at Loyalty ≤ 2) or delegate to the Captain of the Royal Guard (NPC-03). Delegating is safer but produces filtered intelligence — the Captain's Autonomy Conviction means he will selectively report things that reinforce his own agenda.

**[FINDING POL-SIM-01: The faction-leader player's core information problem is delegation filtering. Almud's agents are Inner Circle NPCs with their own Convictions. Every delegated report is filtered through the delegate's stance. The Archbishop's Representative (Faith Conviction) will present TC data in theologically favorable terms. The Treasurer (Precedent Conviction) will frame fiscal data conservatively. Playing as Almud means learning to read the filtered reports and inferring what was left out. No canonical mechanic exists for delegation bias. ED needed.]**

**S9–10:** Certainty erodes. Church presents Evidence through the Archbishop's Representative. Player (Almud at Certainty 3) faces first Conviction challenge: RS ≤ 50 somewhere — the Rendering Stability is declining and Almud can feel something is wrong (TS 0, so intellectually, not perceptually). His Reason secondary Conviction activates: he privately acknowledges what he cannot publicly say. Decision Fork fires.

Decision Fork resolution per §4.1: at 0 Scars, Almud chooses Conviction (personal Reason) over Framework (institutional Order). This costs a Leadership Deviation Stability check. P(success at Stability 5, Ob 1): ~90%. Clean. But it reveals something: Almud's institutional behavior diverges from his private understanding. For the player, this is a recurring tension.

### Phase 2 (S11–20): Coup Pressure, Arc Branch

**S11:** Löwenritter Coup Counter. At S11 equivalent (Crown Stability 4, Almud has deviated once from pure Order): Counter at 1. Ehrenwall is watching. Priority 2 fires at Counter ≥ 3 — player must prevent the Counter from advancing by demonstrating Crown strength.

**Counter management as gameplay:** Player must maintain Crown Stability ≥ 3 AND demonstrate military competence (at least 1 Military Domain Action per year-arc — Royal Guard scenes or March actions). Failure to do so advances the Counter by 1 each year-arc of weakness. Counter management is a persistent background obligation that competes with every other priority.

**S14:** TC 40. Priority 5 fires: Suppress. Player runs Suppress as a Domain Action (Crown Mandate 5, Ob 2). 5D: P(success) ≈ 85%. On Suppress OW: TC −1 net (Church's Assert gain offset). But the Archbishop's Representative (inner circle) is watching and will report this to Himlensendt. Inner Circle Disposition event: Archbishop's Representative Disposition toward player drops −1 (Almud acted against Church interests).

**[FINDING POL-SIM-02: Playing as Almud, Suppress actions against the Church damage the Archbishop's Representative's Disposition toward the player. The Archbishop is an Inner Circle member — at SUC-01 succession, he is one of 5 votes. If the player aggressively suppresses Church TC, they erode a key succession vote. This creates a structural tension: effective anti-Church play weakens Almud's own succession security. The inner circle mechanic converts every BG action into a personal political cost. This is excellent design — confirm intended.]**

**S16 (Arc branch):** Arc A or Arc B determination. If Certainty has reached 1 through Evidence exposure (player finding RS decline data): Almud enters Arc A (Reformer) — potentially. But Arc A requires Löwenritter Coup Counter ≤ 1. If the player has managed the Counter, Arc A is available. If the Counter is at 2, Arc B (Fortress) is forced: Order doubles down, no reform possible.

**Playing Arc A from inside:** The player (as Almud Arc A) runs a reform agenda that publicly contradicts his own institutional framework. Virtue Ethics Framework: reform is NOT "public, visible, virtuous action" by the Crown's prior standards — it is radical change. Framework contradiction: +1 Ob on all reform-domain scenes. The player is fighting their own institutional framework to reform. Stability cost: −1 per arc transition.

**Playing Arc B from inside:** Player is locked into pure Order. All scenes in personal contexts: only Authority RS available (§5.2 Almud Arc B). Secondary Conviction (Reason) fully suppressed. The player experiences Almud Arc B as having fewer options — a mechanical narrowing of approach. Over 5–8 seasons, this is oppressive by design.

### Phase 3 (S21–30): Coup or Legacy

**S21 (Arc C risk):** Coup Counter 3 fires if Stability has been ≤ 3 for 2 consecutive year-arcs. Ehrenwall moves. This is not something happening to an NPC — the player IS the target.

**Coup defense as player experience:** Player must run SUC-03 Contested Succession Cascade FROM THE OTHER SIDE. Ehrenwall (as inner circle-adjacent actor) presents herself as the crisis solution. Player has 2 seasons to: lobby opposing inner circle members (social contests at their settlements, appropriate Availability State), undermine Ehrenwall's military legitimacy (fieldwork finding: Riskbreaker operation exposing overreach), or present a viable alternative (formal Recognition Event for a new succession candidate).

**[FINDING POL-SIM-03: The Coup scenario played as Almud is the most intense single dramatic sequence in any NPC-as-player run. The player is simultaneously trying to maintain their faction's BG stats (Stability, Military response), manage 5 inner circle relationships (each requiring a scene), and personally engage Ehrenwall in some form (diplomatic or confrontational). A 2-season window is very tight for these simultaneous demands — the scene slate cannot accommodate all of them without Standing 5 delegation (NPC-03). But delegation to the very inner circle members you're lobbying creates a circular conflict. Stress test this formally.]**

### Stress Test 1 — Archbishop's Ultimatum (S12)

Church TC reaches 40. Archbishop's Representative (inner circle) delivers private ultimatum to Almud (player): "The Crown must formally acknowledge the Church's authority in T3 or the Archbishop withdraws Crown-Church cooperation." This is a Demand (per NPC-01 Demand Conditions), not a public scene.

**Stakes:** Accepting = TC consolidates in T3 (Church Accord 3 permanent), Crown loses TC counter ability there. Refusing = Archbishop's Representative Disposition −2 (from +1 to −1). At Disposition −1: Archbishop OPPOSES succession. That's 1 of 5 Inner Circle against the player at succession time.

**Resolution options:**
- Accept (Virtue Ethics aligned — "public, virtuous" cooperation): TC concession but succession secure. P(Archbishop maintains support): 95%.
- Refuse (Reason secondary Conviction: "I know this is wrong"): Archbishop opposition, succession contested. Stability check required.
- Counter-offer (negotiate scope): Social contest. Player Charisma 5, 5D vs Archbishop's Authority RS (Ob 2). P(success): ~78%. Partial: TC concession limited to T3 Accord 2 (not 3). Archbishop Disposition 0 (Abstains at succession).

**Outcome tree:** Counter-offer is the optimal play. P(clean succession retained): 78%. P(contested succession): 22%.

### Stress Test 2 — Reason vs. Order (S18)

RS ≤ 40. Thread phenomena are visible in Crown territories. Almud (Certainty 2 by S18 if not confronted) faces a decision: publicly acknowledge Thread reality (Reason conviction, risks Faith of population) or suppress it (Order conviction, risks losing the wardens' eventual cooperation).

**Decision Fork at 1 Scar:** Almud chooses secondary Conviction (Reason) per §4.1. Leadership Deviation Stability check: Ob 1, Stability 4 → P(success): ~90%. On success: Almud privately authorizes a warden contact (Edeyja's Collaboration arc begins). On failure: Stability 3, Coup Counter advances.

**[FINDING POL-SIM-04: Almud's Reason→Order Conviction tension is mechanically productive when played from the inside. Every Reason-motivated action triggers Leadership Deviation. Over 20 seasons, this accumulates. A player who consistently follows Reason will have run 8–10 Deviation checks, each at P(failure) ≈ 10%. P(at least one failure over 10 checks) ≈ 65%. Almud's Stability is expected to be 1–2 points lower than the neutral case by S20 from accumulated Deviation costs. This is the personal cost of intellectual honesty for a ruler whose institutions demand Order.]**

### Stress Test 3 — Torben Coming of Age (S24)

Generational Shift: Torben reaches political maturity. If player (Almud) has built Disposition ≥ +2 with Torben: Torben formally endorses Almud's legacy succession choice (LIN-02 Condition B available). If Disposition < +2: Torben seeks to establish his own power base. Rival Standing 1 for Torben. He's not an enemy — he's an heir who was neglected, and he's asserting himself.

**Player options:** Recognize Torben's claim (voluntary limitation of personal power: the player's faction becomes a dual-authority structure — POW-03 Parallel Authority, with Torben as the figurehead's emerging successor). Fight for continued control (Rival Standing escalation, civil war risk S26+). Or negotiate a transition timeline (formal Regency agreement: player governs for 3 more seasons, then formal handover).

**The Regency path** is the Tokugawa option (LIN-03 historical precedent: establish the institutional form, then step aside to your designated successor): Almud sets the terms, Torben formally accepts, Crown transitions cleanly. Stability −1 (transition). Legacy secured. This IS the most likely "good ending" for an Almud player who has built Disposition with Torben.

### Departure from Play (Almud)
Unlike companion departure, an Almud player doesn't "depart" — they end the campaign in one of:
- Crown governance stable, Arc A reforms enacted, Torben in good standing (Reformer Legacy)
- Coup removed, exile or death (Arc C)
- Fortress governance until Torben asserts (Standstill Ending)
- Partial reform, Torben as co-ruler (Parallel Authority resolution)

**[FINDING POL-SIM-05: Almud as a player character has one of the richest end-state possibility spaces of any NPC. Four distinct campaign endings, each with clearly different mechanical paths. The Conviction tension (Order vs. Reason) drives the branch conditions organically. This validates that Almud is an excellent player character choice — his internal conflict is structurally embedded in his faction obligations.]**

---

## NPC 02 — CONFESSOR ARNE HIMLENSENDT (Church)

### Starting State
**Standing:** 5 (Prelate — Confessor). Church's absolute institutional authority.  
**Stats:** Cognition 4, Charisma 5, Agility 2, STR 2, Endurance 3. Social pool dominant; combat pool 9D but combat is never appropriate.  
**Conviction:** Faith (primary, absolute), Order (secondary). Certainty 4 [per §7.10]. TS 0.  
**Framework:** Divine Command. Aligned: doctrine-consistent action (−1 Ob). Thread truth: +2 Ob.  
**Inner Circle (College of Prelates):** Cardinal Fortitude (Faith+Order, Templar deployment), Cardinal Justice (Faith hardline, Heresy acceleration), Cardinal Prudence (Order+Autonomy, fiscal protection), Cardinal Temperance (Reason+Faith, AER maintenance). Church needs 3 of 5 College votes for succession; Himlensendt IS the 5th (himself).

### Season Structure
**Priority tree as player agenda:**
1. IF Stability ≤ 2 → Consul (Inward)
2. IF TC ≥ 75 → Graduated Seizure
3. IF Mandate ≥ 3 → Assert (Pontifex — post ED-572, every 2 seasons)
4. IF AER ≤ 1 → Cardinal Temperance Focus
5. IF AP ≥ 3 → Deploy Inquisitor
6. IF Mandate < 3 → Consul (Outward, rebuild)
7. DEFAULT → Assert

**Distinct authority as player:** The player has command over the Inquisitor network (OFC-03) as a managed institutional resource. Deploying an Inquisitor is a scene action at zero Ob (it's the player's authority — no roll required, just scene generation). The Inquisitor REPORTS BACK (NPC-03 delegation in reverse: the player receives investigation findings and decides what to do with them).

**Inquisitor as intelligence asset:** An Inquisitor can generate Evidence Tokens (AP management) from any territory with Church Attention Pool ≥ 3. The player reads these findings and decides: prosecute? suppress? use as leverage? This is the central moral choice of Inquisitor deployment — the Confessor has access to everything the investigation found, including things the Inquisitor wasn't supposed to find.

### Phase 1 (S1–10): The Certainty of Purpose

Himlensendt at Certainty 4 operates without genuine doubt. His scene slate is dominated by Assert (Priority 3/8 DEFAULT), AER maintenance (Temperance Cardinal delegation), and Heresy Investigation deployment (Priority 5 fires at AP ≥ 3).

**The player's experience:** Everything about Himlensendt's institutional role confirms his worldview. Evidence that might challenge Faith never reaches him without being filtered through the College (Deference Hierarchy, NPC-04: Cardinals below him won't contradict him publicly). The player is epistemically isolated from challenge — not by choice, but by institutional structure. This is the authentic experience of Himlensendt's position: he doesn't know what he doesn't know.

**Certainty 4 mechanical effects:** First Coherence loss per session nullified. +1D in Church contexts. Combined with Divine Command Framework (−1 Ob on doctrine-aligned action): Himlensendt's social actions in Church contexts are rolled at effectively −2 Ob. A Diplomacy action that would be Ob 2 for others is Ob 0 for Himlensendt in a Church Convocation. He auto-succeeds most institutional actions.

**[FINDING POL-SIM-06: Himlensendt at Certainty 4 makes most institutional actions trivially easy. This correctly models how an institution captures its own leader: the system is designed to make the leader successful within the system, reinforcing both the system and the leader's self-belief. The tension cannot come from inside the Church's normal operations — it must come from external evidence that penetrates the deference hierarchy. This validates NPC-02 (Authority Gradient): Himlensendt is only challenged by things that bypass the normal hierarchy.]**

**S7:** AER dips to 2. Cardinal Temperance is concerned; his Reason conviction pushes him toward investigation. Player (Himlensendt) must decide: authorize Temperance to investigate (which risks him finding Thread-adjacent evidence that challenges doctrine) or redirect Temperance's focus (Procedural Objection in College: a social scene where Himlensendt overrides Temperance's concern with doctrinal authority). P(Himlensendt wins such a contest): ~95% given his Certainty 4 + Church context bonus. He can suppress the investigation easily. He will, by default, because his priority tree (Priority 4: AER ≤ 1 triggers response, not at 2) doesn't flag this yet as urgent.

**[FINDING POL-SIM-07: The most significant gap in playing as Himlensendt is that his priority tree and institutional reflexes almost always produce the worst possible long-term outcome. The "correct" play (authorize Temperance's AER investigation) conflicts with his Conviction's institutional logic. A player playing faithfully to Himlensendt's Conviction will suppress investigations that would help them. A player "gaming" the system will deviate from Conviction — taking Leadership Deviation costs. This is the central experience of Himlensendt-as-player: being inside a Conviction structure that consistently produces bad epistemic outcomes.]**

### Phase 2 (S11–20): Evidence Reaches the Throne

**S13:** Player-initiated player contest arrives. Another PC (in multi-player context) or GM-controlled action: Evidence attack on Himlensendt. His Faith framework: Evidence at +0 Ob (not his primary RS vulnerability, but not blocked either). His Certainty 4 means: first Coherence loss negated (this acts as a first-Evidence-exchange immunity — the contest must produce successive decisive wins to accumulate Scars).

Playing as Himlensendt experiencing Evidence attack:
- **Within-scene experience:** Himlensendt rolls his full pool (Cognition 4 + Charisma 5 + Church context bonus + Certainty 4 +1D = effectively 11D in Church Convocation). His opponents roll less. He wins most exchanges.
- **After decisive loss (Track ≥ 7):** Scar 1. Player (Himlensendt) now experiences what Scar 1 does FROM INSIDE: secondary Conviction activates. Order now sits alongside Faith in every decision. Decision Forks increase. The player notices they're "playing two characters at once" — Faith-response and Order-response sometimes diverge.

**S16:** Scar 2 escalates. Primary Conviction may shift to secondary (§3.3). Player (Himlensendt) now has a Certainty of 2–3. The auto-success institutional advantage degrades. Church context bonus still applies but Certainty nullification is gone. Player feels the mechanical tightening: rolls that were trivial now require attention.

**College internal tension:** Cardinal Justice (Faith hardline) sees Himlensendt's uncertainty as weakness. At Scar 2: Justice begins quietly building College support for himself. Rival Standing 1 for Justice (SUC-02). Player must either demonstrate continued Faith commitment (suppress all doubt publicly) or begin building alternative coalition (Cardinal Prudence and Temperance may support a more flexible Confessor).

### Phase 3 (S21–30): Crisis or Transformation

**Arc B (Crisis of Faith):** Player now inhabits the existential disorientation they previously imposed on others through Heresy Investigations. The player's Faith-primary Conviction at Scar 3 generates random behavior (Conviction crisis table, d6 per major decision). From inside, this is the player rolling d6 to determine their own NPC's decision — institutional authority plus personal chaos. The player is fighting their own dice table.

**Arc C (Confrontation — public):** If the player allows Arc B to become public (or it's forced by game events), Church Stability −3. Player is simultaneously the cause and the victim. The College convenes an emergency session. Cardinal Justice proposes a Heresy charge against Himlensendt himself (the Inquisitor investigating the Confessor — a formally possible action per OFC-03, if explicitly authorized by Prelate majority). Player (Himlensendt) must defend against a Heresy charge using the Church's own tools — their evidence against themselves.

**[FINDING POL-SIM-08: Himlensendt's Arc C from inside is the game's most dramatically inverted scenario. The player who deployed Inquisitors to investigate heresy is now the subject of an Inquisitorial inquiry. The player must use the same social contest mechanics they previously wielded institutionally, now in personal defense. This is structurally excellent — the mechanics close the loop perfectly. The only gap: the formal Heresy Proceeding mechanic (OFC-03) requires the Confessor's explicit authorization for investigating Church leadership. If Himlensendt IS the Confessor being investigated, who authorizes? The Prelate College (3 of 5 votes). This needs a formal ruling.]**

### Stress Tests

**Stress 1 — The Temperance Defection (S15):** Cardinal Temperance brings Himlensendt documented evidence: Thread phenomena in T9 (Church capital territory) are producing AER decay. Himlensendt's Faith framework: +2 Ob to accept Thread-adjacent truth. Social contest: Temperance presents Evidence. Player rolls Faith defense: 11D (at Certainty 3 by S15). Temperance: 8D Evidence. P(Temperance decisive win): ~15%. P(partial, Scar): ~30%. Most likely: Himlensendt suppresses the evidence. AER continues to decay. Correct outcome.

**Stress 2 — Assert frequency vs. College unrest (S11):** Pontifex Assert cooldown requires player to wait 2 seasons between Asserts. In off-seasons, other Cardinals handle Domain Actions. Cardinal Justice uses his off-season autonomy to accelerate Heresy Investigations beyond what Himlensendt authorized. Player must either endorse (Faith-aligned but the investigations are targeting innocents) or rein in Justice (Order-aligned proceduralism — but publicly contradicting Cardinal Justice in the College costs player Disposition with Justice −1). No neutral option.

**Stress 3 — Excommunication decision (S22):** Player (Himlensendt) must decide whether to Excommunicate Baralta. This is a Doctrine-aligned action (−1 Ob) that his Faith framework strongly supports. But the player, after 22 seasons inside Himlensendt's arc, may have developed sufficient understanding of the consequences to hesitate. The Virtue of the action is clear. The Consequence (Church Stability −3 from Hafenmark's response, TC backlash, Coup Counter risk for Crown) is also clear. Playing Himlensendt requires acting on Faith over Consequence — or taking a Scar for failing to act.

---

## NPC 03 — DUCHESS INGE BARALTA (Hafenmark)

### Starting State
**Standing:** 5 (Kanzler — Parliamentary Chancellor). She IS the institution.  
**Stats:** Cognition 4, Charisma 4, Agility 2, STR 2, Endurance 3. Combat Pool: 9D.  
**Conviction:** Precedent (primary), Faith (secondary). Certainty 5 (§7.10). TS 0 (triple-barrier: Ob 4 on growth).  
**Framework:** Categorical Imperative — Aligned: legal/constitutional action (−1 Ob). Contradictory: ad hoc/precedent-breaking (+ 1 Ob).  
**Inner Circle:** Senior Parliamentary Chair (constitutional process), Guild Comptroller (trade stability), Legal Advisor (procedural legitimacy), Military Commander (border security). Parliamentary succession: requires Parliamentary majority OR super-majority if contested.  
**Rank obligations:** Vote every Parliament session; maintain constitutional doctrine publicly; maintain coalition majority; govern at least one province-level settlement.

### Season Structure
Parliament Convening (Ceremonial Scene, REN-02) is Baralta's home terrain. Every Parliament session: Baralta's Renown benefits from +2 on decisive contest wins, −2 on decisive losses. This is her primary performance arena. Between sessions: Govern province settlements, manage Guild Comptroller's fiscal agenda, monitor TC advancement.

**What Baralta does NOT do:** Fieldwork. Investigation. Personal combat. These are delegated. The Guild Comptroller handles economic data. The Legal Advisor maintains precedent records. The Military Commander manages border deployments. Baralta receives filtered reports (POL-SIM-01 applies: her delegates filter through their own Convictions — the Legal Advisor will frame everything in procedural terms; the Guild Comptroller will frame everything economically).

### Phase 1 (S1–10): Constitutional Supremacy

**S1–6:** Framework Drift in action. Every Baralta action in these seasons is Framework-aligned (Govern, Parliament, treaty procedures). Per npc_behavior §7.1: Influence +1 per Framework-aligned season. By S4: Influence 7 (cap). Baralta's Suppress actions at TC 40+ will roll 7D — OW probability 88%.

**Parliament as resource:** Player conducts 2 Parliament Convening scenes per year-arc (mandatory obligation). These are Ceremonial Scenes. Each successful social contest win in Parliament: Renown +1 (public victory). Over 10 seasons of 2 Convening scenes each: player accumulates Renown track from parliamentary wins. Coalition majority maintained through Disposition building with each Parliamentary NPC (3 of 4 inner circle members must be maintained at Abstain or Support).

**Guild Comptroller management:** MIN-01 equivalent for Hafenmark — the Guild Comptroller is the Haushalt analog. At Competence 2: Hafenmark Wealth +1/season. Player must invest 1 audit scene action per 3 seasons to maintain Competence ≥ 2 (MIN-02 decay: Ob 2 attribute roll per Accounting, P(failure) ≈ 18%/season). Without audits: Competence decays to 1 in ~5 seasons.

**[FINDING POL-SIM-09: Baralta as player demonstrates the Ministry/administration audit problem clearly. The Guild Comptroller's Competence decay (P ≈ 18%/season without audits) means a player who does not invest scenes in administration will face declining Wealth yield. But scene investment in administration competes directly with Parliamentary dominance (the player's primary political arena). Trade-off: administrative efficiency vs. political presence. No current rule specifies the scene cost of Ministry-equivalent audits for non-Crown factions. ED needed.]**

**S8:** TC 38 — approaching 40. Baralta's Priority 5 fires at 40: Suppress. Player is watching the TC clock, preparing resources. Two seasons of advance preparation: player positions Legal Advisor to draft the Sovereign Authority Doctrine (documented constitutional precedent against Church TC). This is an Investigation fieldwork scene — Legal Advisor conducts it (delegated NPC-03). Finding: documented legal precedent. Evidence Token (Verified): +1D on the eventual Suppress contest.

### Phase 2 (S11–20): Suppress as Permanent Obligation

**S11:** TC 40. Priority 5 fires. Baralta Suppress: Influence 7 (capped), Ob 2, OW rate 88%. In non-OW case (12%): TC holds but Suppress is not decisive. Church Piety Yield still fires next season.

**The Suppress obligation structurally:** From inside Baralta's perspective, the Suppress action at TC ≥ 40 is MANDATORY (her Priority 5 always fires once the threshold is crossed). This means the player has no choice but to allocate one of Hafenmark's Domain Action slots to Suppress every season. The remaining actions (2 Consul cards) must handle all other Hafenmark needs (Govern province, Parliamentary Motions, Diplomacy, trade). Senate-level governance of a faction with 3 Domain Actions total, one permanently committed to Church counter-pressure.

**[FINDING POL-SIM-10: Playing as Baralta makes the TC counter-pressure obligation visceral. From the NPC AI perspective, Suppress is a Priority 5 instruction that fires automatically. From the player's perspective, the Suppress action is a mandatory season-to-season obligation that cannot be skipped without violating her Conviction (Precedent: constitutional protection of Hafenmark IS her identity). This creates a form of lock-in the player experiences directly: Baralta cannot NOT Suppress once TC ≥ 40 without betraying who she is. This is the correct design experience for this NPC.]**

**S15 — Grand Contest opportunity (ED-583 new rule):** If player wins Grand Contest decisive victory over another faction in Parliament: Hafenmark Mandate 4→5. This is the one Mandate growth path for Hafenmark. Player must engineer a Grand Contest (requires contested territorial dispute, Parliamentary showdown). The scene: a Parliamentary Convening (Ceremonial Scene) where Baralta is the primary advocate, opposition is another faction's representative. Stakes: Mandate advancement. Renown ±2. All inner circle observing.

**Grand Contest mechanics:** Social contest, Ob 3, parliamentary framework. Baralta: Cognition 4 + Charisma 4 + Constitutional doctrine bonus (−1 Ob = Ob 2 effective) + Legal Advisor Evidence Token (+1D) = 9D vs Ob 2. P(decisive win, Track ≥ 7): ~45%. P(success, Track 5-6): ~30%. P(failure): 25%.

**On decisive win:** Mandate 4→5. Hafenmark can now pursue Dynastic Proclamation on any faction at Mandate ≤ 4 (previously only Varfell at 3 was reachable). Crown at Mandate 5 is now level with Hafenmark — still no Proclamation target. Grand Contest on Crown requires TWO decisive wins (Mandate 5→6) to get Proclamation leverage over Crown (at 5). Possible but requires sustained parliamentary dominance.

### Phase 3 (S21–30): Constitutional Legacy or Excommunication

**S21 — Excommunication threat:** Church TC ≥ 65. Himlensendt triggers Excommunication against Baralta (Arc C trigger). Player faces the scenario from inside: Church Convocation formally announces Excommunication. TC +4 immediate. Hafenmark Mandate −2 (public authority crisis — her Faith secondary Conviction is now directly contradicted by her legal standing being stripped by the Church she privately believes in).

**Internal experience:** Precedent Conviction: "Constitutional procedure IS justice." But the Church is using a constitutional procedure (Excommunication) against her. Her own framework is being weaponized. Decision Fork at 1 Scar: secondary Conviction activates (Faith). Player now has Faith pulling toward compliance (accept the Church's authority) and Precedent pulling toward resistance (the Church's claim is procedurally invalid under Hafenmark's constitution).

**Resolution path:** Hafenmark Parliament invokes the Sovereign Authority Doctrine (Legal Advisor's prepared Evidence Token). Parliamentary vote: 3-1 in Baralta's favor (coalition maintained). Church Excommunication is declared constitutionally non-binding in Hafenmark territory. TC +4 still stands (Church gains TC regardless of Baralta's legal counter). But Hafenmark's institutional integrity survives.

**[FINDING POL-SIM-11: The Excommunication-from-inside experience validates the design. Baralta's Categorical Imperative Framework means she CANNOT simply ignore the Excommunication — it is a real action by a real authority, and her proceduralism demands she engage with it procedurally. The player cannot just say "ignore it" — they must play the Constitutional counter, which consumes scene actions, inner circle coordination, and Parliamentary coalition management. The Excommunication is not just a BG stat change; it generates a 2–3 season arc of institutional defense.]**

### Stress Tests

**Stress 1 — Coalition collapse (S14):** Guild Comptroller, dissatisfied with Baralta's anti-Church stance (Guild trade with Church territories impacted by Suppress actions), withdraws from Parliamentary coalition. Player loses 1 of 4 inner circle members. Majority maintained (3 of 4 remaining = sufficient, but barely). Demotion trigger from Standing 5: "Coalition collapse for 2 consecutive sessions" — player must restore Comptroller's Disposition within 2 Parliaments. Scene: private negotiation (Baralta In Session, Comptroller visits). Player rolls Charisma 4 + Categorical Imperative (constitutionally-framed offer) = 5D Ob 1. P(restore): 85%.

**Stress 2 — Precedent violation forced (S17):** Varfell invades Hafenmark T10 (Spartfell). Standard response: deploy Military Commander. But Military Commander's competence is 1 (player hasn't audited in 3 seasons, per POL-SIM-09 finding). Military response is weak. To effectively counter, Baralta must personally authorize an extralegal military response (borrowing Crown troops without prior Parliamentary sanction). This violates her Categorical Imperative Framework: +1 Ob AND Scar risk (her Belief 1: "Constitutional procedure IS justice"). Player chooses: take the Scar to save the territory or watch T10 fall while Parliament deliberates. This is the Baralta "Pragmatist" arc trigger from inside.

**Stress 3 — Succession design (S26):** Baralta has no designated successor. Parliamentary succession requires majority vote. Who does the player position? Option A: Designate a Legal Advisor heir (procedurally clean, weak military). Option B: Position the Military Commander (strong, but violates constitutional precedent as it's a military appointment to a civilian role). Option C: Constitutional Revision (LIN-02 Condition C: Parliamentary super-majority 2/3 redefines succession criteria). Condition C requires 2 seasons of Parliamentary challenge. Playing as Baralta means managing your own succession — the most uncomfortable leadership challenge.

---

## NPC 04 — DUKE MAGNUS VAYNARD (Varfell)

### Starting State
**Standing:** 5 (Hochjarl — Jarl-Regent, effectively). Varfell faction leader.  
**Stats:** Cognition 5, Charisma 2, Agility 2, STR 2, Endurance 3. Knowledge-focused. Combat Pool: 7D.  
**Conviction:** Reason (primary), Autonomy (secondary). Certainty 2 (§7.10). TS 10 (hidden, starting).  
**Framework:** Consequentialist Pragmatism — Aligned: measurable outcomes (−1 Ob). Contradictory: uncertain/long-term payoff (+1 Ob).  
**Jarl Assembly obligations:** Attend annual Assembly; hold majority Jarl support (3 of 5 senior Jarls); maintain Military ≥ 4 in provinces; conduct independent military operations only with prior notice.

### Unique Context: Thread Pursuit as Player Goal
Vaynard's Reason conviction + TS 10 (environmental exposure) makes Thread knowledge pursuit his primary Conviction-driven goal. From inside: every Domain Action the player takes is evaluated through "what does this produce in measurable outcomes, and does any of it advance Thread understanding?" The player is simultaneously a faction leader AND a private researcher — and these two roles compete for scene slots.

**VTM advancement as player investment:** VTM is Vaynard's faction-specific clock. Player allocates Tribune actions to Expedition (VTM advancement). Each Tribune Expedition: Influence 4 + Path bonus, Ob 2. P(success per Expedition season) ≈ 65%. VTM reaches target (Path A: 5, Path B: 4, Path C: 3) in 6–10 seasons depending on path and allocation.

**Discovery Events as player-facing risk:** At TS 14+ (reached ~S6 through environmental exposure), every Private Collection deployment triggers a Spirit check (Spirit 2, Ob 2, TN7): P(Discovery Event/session) ≈ 18%. Player (Vaynard) cannot prevent Discovery Events — they are a consequence of his position. Each Event: TS advances. At TS 30: Ontological Confrontation challenges Conviction. Certainty 2→1. Player's Consequentialist Framework starts destabilizing.

### Phase 1 (S1–10): The Scholar in Power

**S1–4:** Player manages Jarl Assembly obligations (annual scene: Vaynard must attend). Assembly is a Ceremonial Scene (REN-02) for Varfell. At the Assembly, Vaynard's Cognition 5 + Reason Conviction + Evidence RS primary = he is the strongest information-presentation actor in any Assembly scene. P(winning Assembly social contests): ~80%.

**Jarl management:** Three of five Jarls must support Vaynard. Eastern March Jarl requires military excellence (regular Military Domain Action; player must allocate at least 1 Military action/year-arc or risk Jarl Eastern March shifting to Opposition). Western Highlands Jarl requires settlement development (player must govern T11 or T12 within first year-arc). Skald-Chief requires adherence to Varfell tradition (the player's Reason conviction occasionally conflicts with traditional precedent — Decision Fork potential).

**Discovery Event S6:** P(first Discovery Event by S6, 6 seasons at 18%/season) ≈ 68%. Event fires. Player rolls Spirit 2 (2D, Ob 2, TN7): P(success) ≈ 18%. Most likely: FAIL. Discovery Event fires. TS 10→18 (mid-Dormant advance). Player has now experienced what Vaynard experienced — the moment the Thread substrate became personally real. Certainty 2: not a crisis yet, but Vaynard's certainty is already low enough that this is confirmatory rather than shattering.

### Phase 2 (S11–20): Knowledge and Governance in Tension

**S11:** VTM 2 reached (assuming Path A, ~10 Tribune Expeditions). Cultural Reformation available. Player now has the power to directly reduce TC in low-PT territories: Colonist action, 6D Ob 3 (at VTM 2). P(OW, TC −1): ~45%. This is a major BG tool — but it costs Tribune cards and competes with VTM advancement Expeditions. Player must choose: consolidate current VTM utility or advance toward VTM 3+ for deeper Thread knowledge.

**Jarl Eastern March tension:** If player has under-invested in Military (Thread research competing with Military Domain Action obligation): Eastern March Jarl Disposition drops. At Disposition −1: Rival Standing 1 for Eastern March Jarl. Player receives early warning from Skald-Chief (if competent — Skald-Chief's Conviction is tradition-adherence, and the Eastern March Jarl's dissatisfaction is traditional grounds for challenge). Player must: dedicate next season to Military display at Eastern March (Ceremonial Scene: Military Muster and Review), OR negotiate with Eastern March Jarl directly (social contest, Ob 2, Vaynard Cognition 5: P(success) ≈ 78%).

**Discovery Event S16:** P(second Discovery Event by S16, 10 seasons at 18%) ≈ 86%. Second event fires. TS 18→28 (near Stirring). If player has not sought Warden training: Certainty 2→1 (ontological confrontation, §5.1). Consequentialist Framework begins to destabilize. Vaynard (player) starts experiencing what Arc B looks like from inside: measurable outcomes no longer satisfy a mind that is perceiving Thread substrate directly without the tools to interpret it.

**[FINDING POL-SIM-12: Vaynard's Discovery Events are the most punishing player-facing mechanic of any NPC-as-player run because they are probabilistically unavoidable and compound. By S16, the probability of having experienced 2+ Discovery Events is ~86%. Each event degrades Certainty. Without Warden access (requires Edeyja's collaboration, which is late-game), Vaynard the player is watching their character progressively destabilize without any recourse. The design is intentional (Arc B/C is his arc), but the player should know: playing Vaynard is playing toward a crisis you cannot prevent, only manage. The game should be explicit about this as a campaign mode choice.]**

### Phase 3 (S21–30): Consumed or Awakened

**Arc B active (S20+):** Player's Certainty 1. All RS accessible (secondary Evidence activates). The player now has access to the widest social toolkit of any point in the campaign — but their institutional reliability is degrading. Jarl Assembly: Vaynard's behavior is unpredictable enough that the Skald-Chief raises concern at S22 Assembly. Rival Standing 2 for Eastern March Jarl (sustained military under-investment AND now erratic Ducal behavior).

**Arc C (Consumed) path:** TS reaches 30+ without trained support (Edeyja or Maret Uln not available). Coherence-equivalent degradation. Player (Vaynard) is experiencing Thread perception without the framework to manage it. Mechanically: Conviction crisis table fires (d6 per major decision). The player rolls d6 to determine their own NPC's behavior. This is designed as campaign-ending degradation — Vaynard in Arc C is not a viable long-term player character. He needs intervention.

**Warden Path (avoid Arc C):** If player reached Edeyja's collaboration (Arc B → Arc B with Warden contact): Edeyja (or Maret Uln) provides practitioner training. TS 30 with proper training = Stirring threshold crossed with Coherence management in place. Vaynard stabilizes at Certainty 0 (Thread acceptance — his own Reason Conviction reaches its logical endpoint: Thread is the most important truth). He becomes a different kind of faction leader: one who sees the world as it is.

### Stress Tests

**Stress 1 — Maret Uln preparation (S8):** Vaynard must decide whether to formally groom Maret Uln as a succession option. This requires acknowledging he might not survive his own Thread arc. Consequentialist Framework: the Ob-minimizing action is succession preparation. But his Belief 3 ("Varfell alone can handle this responsibly") resists sharing institutional power. Scar risk: 0, but Decision Fork. If player prepares Maret Uln: Varfell succession secured. If not: Arc C Vaynard elimination produces a vacuum.

**Stress 2 — Jarl Assembly challenge (S19):** Eastern March Jarl presents formal challenge at Assembly. SUC-03 fires. Resolution window: 2 seasons. Player must lobby 3 Jarls (Assembly has 5 total). P(maintaining majority without Maret Uln preparation): ~55% if Disposition-building has been maintained. P(with Maret Uln as prepared ally, her Alliance provides 1 additional Jarl vote): ~75%.

**Stress 3 — Knowledge extraction attempt (S23):** Niflhel attempts to acquire Vaynard's Thread research. Schattendienst-equivalent (Varfell has no formal Schattendienst, but has Tribune intel network). If Vaynard's delegation intelligence has been maintained (regular Tribune audits), Niflhel attempt is flagged 1 season in advance. If not: Niflhel successful extraction. Thread knowledge transferred. This triggers Vaynard's Belief 3 → Scar (the faction he distrusted most has proven untrustworthy with the knowledge). Conviction crisis table risk.

---

## NPC 05 — MARET VOSSEN (Restoration Movement)

### Starting State
**Standing:** Functionally 5, but NO formal rank ladder exists for RM (no FAC-01 equivalent). Vossen is a grassroots organiser leading a movement without institutional infrastructure.  
**Stats:** Charisma 5, Cognition 3, Agility 3, STR 2, Endurance 3. Circles 3+ in working-class networks.  
**Conviction:** Equity (primary), Continuity (secondary). Certainty 3. TS 0.  
**Framework:** Rawlsian Social Contract — Aligned: actions benefiting common population (−1 Ob). Contradictory: power-concentrating actions (+1 Ob).  
**No formal Inner Circle** — RM is not a faction with Inner Circle succession mechanics. Vossen's "inner circle" is her cell network leaders and Aldric Hann (structural sub-leader).

### The Fundamental Structural Difference
Vossen as player character operates outside every hierarchical system the patch register is designed for. She has no:
- Rank ladder (FAC-01 doesn't apply — no formal rank)
- Formal Parliament seat (Parliamentary Manoeuvre unavailable without Standing 2 in Hafenmark)
- Ministry structure (MIN-01 doesn't apply)
- Succession mechanics (SUC-01 doesn't apply — RM has no formal succession)
- Domain Action slots (RM is "Post-Founding Only" per §8.9, starting state is Pre-Founding)

**[FINDING POL-SIM-13: Maret Vossen as player character is the game's most structurally divergent run. All mechanics from the patch register are absent or inapplicable. She has no rank ladder, no inner circle succession, no ministry system, no ceremonial scene home terrain, no formal Domain Action economy. Playing as Vossen is playing entirely in TTRPG mode (personal scale) with BG consequences emerging from her Uprising and Founding mechanics. The patch register does not address insurgent faction play at all — only established institutional factions. This is a significant design gap for RM players.]**

### Season Structure (Pre-Founding)
Vossen's season is structured entirely around:
1. **Outreach generation:** Her own Outreach to other NPCs (Circles 3+ in community networks → 1 free Interview-equivalent/season).
2. **Uprising building:** RM victory condition requires "Uprising OW in T9 AND holding PT ≤ 3 in T9" (per ED-588/589 — contested). Player must build community support across settlements, creating conditions for Uprising rolls.
3. **Safety management:** Church Attention Pool in RM territories. At AP ≥ 3: Church Priority 5 fires (Inquisitor deployed). Vossen as player is managing the AP clock as a personal safety metric — not a faction stat to observe, but a threat to her physical operation.
4. **Cell network maintenance:** Hann's operational sub-network. Player delegates operational intel to Hann (NPC-03 in reverse: Hann is the delegated agent). Hann reports filtered through his Consequence RS (operational success framing).

**Scene loop (no Availability State constraint — Vossen is always available to her own people):** Vossen operates In Session (community organizing), Traveling (between settlements), and occasionally In Private Retreat (planning). But she has NO Unavailable state — her community expects her to be present. This creates burnout risk if the player tries to maintain presence across too many territories simultaneously.

### Phase 1 (S1–10): Movement Building

**S1–4:** Community investment. Player builds Circles in 3 settlements. Each settlement: 2–3 Outreach scenes to establish trust (Charisma 5 + Equity Framework: −1 Ob on community-benefit actions = Ob 0 for basic community trust-building). Auto-success on most early scenes. Player feels powerful in their natural domain.

**S5 — First Heresy Investigation:** AP reaches 3 in T6 (Church Priority 5 fires). Inquisitor deployed. Player (Vossen) is now the investigation target. Scene: Inquisitor in T6. Player must either: go underground (lose T6 community access for 2 seasons), confront the Inquisitor publicly (social contest, Ob 2, Vossen Charisma 5: P(success) ≈ 78%, but public success = AP +1 in T6 from Church attention), or redirect the Inquisitor toward a false target (requires subterfuge: Hann's network handles this, but it costs a cell exposure if Hann fails). Player learns: staying visible is a ticking clock.

**S7 — Founding threshold:** RM requires specific conditions for formal Founding (not fully specified in canonical docs — [GAP-SIM-POL-01: RM Founding conditions not defined in canonical docs. §8.9 says RM Priority Tree is "Post-Founding Only." What triggers Founding? What are the mechanical conditions? Without this, Vossen-as-player has no BG domain action economy for the first N seasons of the campaign. This is the critical undefined mechanic for RM play.]).

### Phase 2 (S11–20): Post-Founding

Assuming Founding achieved at S10 (player successfully meets conditions): RM now has Priority Tree access (§8.9). Domain Action economy begins. But RM cards: Vossen has Charisma-heavy toolkit, not the institutional cards of established factions. RM's Domain Actions are community-oriented: Uprising (Charisma + Circles pool), Outreach (relationship building), Supply Network (logistics).

**Church suppression management:** Church Priority 5 (Inquisitor) fires whenever AP ≥ 3 in any RM territory. RM territories: Vossen's community network. She is simultaneously building the community AND is the primary target of its investigation. Player (Vossen) is always managing the AP clock in multiple settlements simultaneously — a tracking burden.

**[FINDING POL-SIM-14: Vossen-as-player has the highest information-tracking burden of any NPC. She must monitor AP in every community-active settlement, Hann's cell network health, Founding conditions/progress, Uprising readiness (ED-588 PT ≤ 3 holding condition), Church Attention pressure, and her own Movement's community trust levels. No existing mechanic aggregates these into a manageable dashboard. RM play at the leader level needs a movement-health tracker analogous to the faction mat. Without it, Vossen-as-player is tracking 5+ independent variables that existing canonical tools don't accommodate.]**

**Vossen's Victory Condition as player goal:** The RM victory condition is not "control the most territories" — it's Uprising + PT management. Playing as Vossen means the player's entire campaign is oriented toward a fundamentally different victory shape: popular legitimacy, not territorial dominance. Every action is evaluated against "does this build the conditions for an Uprising that the population sustains?" This is a radically different campaign experience than any institutional faction player.

### Stress Tests

**Stress 1 — Solidarity Contradiction (S9):** Hann suggests using a Niflhel-connected contact to funnel supplies. Vossen's Belief 3: "Violence is the tool of the powerful." But Niflhel isn't violent — they're covert. The contradiction: using the tools of an amoral network to serve a moral movement. Scar risk: Belief engagement (Belief 3 addresses means, not just ends). Player must decide: Conviction adherence (refuse, lose supply efficiency) or pragmatic acceptance (Scar 1, Hann's Autonomy secondary activates, driving toward the Hann/Vossen divergence identified in the companion sim).

**Stress 2 — Uprising failure (S15):** First Uprising attempt: Charisma 5 + Circles 3 = 8D, Ob 3 (ED-588 proposed fix: PT ≤ 3 holding condition). P(success) ≈ 50%. On failure: Church Priority 2 fires (TC ≥ 75 + PT conditions for Graduated Seizure). Church seizes T9 territory that Vossen was preparing for Uprising. RM Stability crisis. Vossen (player) faces dissolution of 2 seasons' work. Continuity secondary Conviction activates: shift from political liberation to cultural preservation mode. The player's strategic horizon narrows.

**Stress 3 — Equity vs. safety (S20):** A RM cell leader in T3 is captured by Church Inquisition. Vossen can expose herself to rescue him (Solidarity primary) or protect the movement by cutting him loose (Autonomy/consequentialist — Hann would advise this). Vossen's Belief: "the communities that depend on her" = the cell leader IS the community. She cannot abandon him without Scar 1. P(rescue mission success without triggering full Inquisitorial investigation): ~35% (covert fieldwork, AP management). Decision: certain Scar from abandonment vs. 65% chance of operational catastrophe from rescue. This is Vossen's most characteristic dilemma.

---

## NPC 06 — PRINCE TORBEN ALMQVIST (Crown)

### Starting State
**Standing:** 1–2 (Hofmann / Kronagent — not yet senior). Torben starts as the heir-apparent, not the ruler. He is a political asset operated within Crown's hierarchy.  
**Stats:** Cognition 3, Charisma 4, Agility 2. Combat Pool: 7D. Certainty 4 (§7.10).  
**Conviction:** BLANK. Torben has no primary Conviction at start. First faction/PC to invest sets his initial Conviction.  
**Campaign mode:** Torben-as-player starts at the BOTTOM of the rank ladder and works UP. This is the only NPC-as-player run that uses the full Standing 1→5 progression. He begins as a Kronagent (Standing 2) — his royal birth gives him immediate access to Standing 2 without FAC-02 Recognition Event requirements (birthright).

### Season Structure (Early — Standing 1–2)
Torben-as-player operates under Crown's hierarchy. His superiors: Almud (Standing 5), Royal Marshal (Standing 4 equivalent), Archbishop's Representative (standing 4 equivalent). Deference Hierarchy (NPC-04): Torben will not contradict these figures publicly. In scenes with Almud: Torben defers. He may have private opinions but cannot act on them without Leadership Deviation cost.

**The Blank Conviction experience:** No Conviction means no Framework alignment bonuses and no Conviction contradictions. Torben-as-player starts with neutral Ob on all actions (no −1 Ob bonuses, no +1 Ob penalties). The player is making Conviction choices throughout S1–6 that will define Torben's framework. Each decisive scene outcome can be declared "Belief formation" by the GM: the experience crystallizes into a lasting Conviction.

**[FINDING POL-SIM-15: Torben-as-player is the most malleable NPC run and the most emotionally resonant. The player is literally building a character identity through play, not working with a pre-existing character identity. Every scene is simultaneously a tactical choice AND a character definition moment. By S10, Torben will have 2–3 Beliefs formed from his experiences. The player shaped every one of them. This is the most "protagonist creation" experience the NPC-as-player system offers — and it's uniquely available to Torben because of his blank slate.]**

### Phase 1 (S1–10): Formation

**S1–3:** Torben operates as Crown Kronagent. His Standing 2 obligations: maintain Disposition ≥ 0 with at least one Crown NPC, maintain Wealth ≥ 1. Scene access: Crown courier network (free information relay per season). His authority ceiling: can conduct fieldwork in Crown's name (+1D on Interview in Crown territories). He cannot direct officers, cannot initiate Domain Actions independently.

**Conviction formation scenes (S2, S5, S8):** Three key scenes where the player makes Conviction-defining choices:
- S2: Witness Crown military suppression of a Restoration-sympathetic settlement. Choice: report faithfully (Order reinforced) or frame it sympathetically to Almud (Equity seed planted).
- S5: Archbishop's Representative pressures Torben to attend a Church ceremony publicly endorsing the Inquisition. Choice: attend (Faith reinforced) or find a scheduling conflict (Autonomy seed planted).
- S8: Ehrenwall invites Torben to observe Löwenritter training. Player observes military excellence and camaraderie. Choice: be moved by it (Order/Solidarity seeds) or remain analytically detached (Reason seed).

By S10: Torben has 1–2 Beliefs formed, primary Conviction emerging. The player has defined who Torben will be for the next 20 seasons.

### Phase 2 (S11–20): Standing Advancement

FAC-02 Recognition Events fire at Standing 3 (Bannerherr) and Standing 4 (Kronleutnant). Each is a Ceremonial Scene (Royal Audience — Almud presides). Player must navigate: what does Torben say in his Recognition audience? This is a scene that builds the public record of Torben's character.

**Standing 3 (S11–12):** Torben may now direct one NPC officer and govern a settlement. His obligations: govern at least one settlement, maintain its Order. He is, for the first time, a genuine governor. If his Conviction formed toward Equity (S2 scene choice): he will govern differently than if it formed toward Order. This is the first governance expression of his formed character.

**Rival dynamics:** SUC-02 Succession Rivals. If Almud is declining (Arc B), a Cadet Claimant may emerge (LIN-01: Cadet Claim). Torben's Bloodline Claim supersedes any Cadet Claim, BUT: if Torben's Disposition with key inner circle members is low (< +1), the Cadet Claimant can exploit succession ambiguity. Player (Torben) must actively maintain Crown Inner Circle Dispositions to secure his birthright claim.

### Phase 3 (S21–30): Succession or Conflict

**S21 — Almud's Arc:** Crown is either in Arc A (Reformer, supported by player if Torben-player invested) or Arc C (Coup: Ehrenwall acts). 

**If Coup fires:** Torben is the key legitimacy figure. Ehrenwall's Coup Counter 3 fires. Löwenritter declares: "We act to protect Crown stability." But Torben IS the Crown's legitimate heir. Löwenritter must either co-opt Torben (building Disposition ≥ +2, which they have not necessarily done) or override him (which is explicitly LIN-04 Coup territory: forcible seizure). Torben-as-player now has the most powerful individual card in the game: his Bloodline Claim. He can either:
- Back Ehrenwall (she manages, he legitimizes — POW-01 Figurehead Status from Torben's perspective): he becomes a Figurehead. Power to Löwenritter; legitimacy stays with Torben.
- Resist Ehrenwall (he asserts his own claim): SUC-03 Contested Succession Cascade fires. Torben vs. Löwenritter for actual governance authority.
- Seek outside support (Hafenmark, RM) to balance Löwenritter's military weight.

**The Restoration trajectory (S26):** If Torben allowed Figurehead Status (POW-01): POW-02 Restoration Event fires at S24–26 when Torben reaches political maturity and Löwenritter Mandate ≤ 2 (degraded from governance difficulty). This is the Meiji Restoration from Torben's perspective: he demands restoration of actual governance authority. The player makes this demand and resolves the confrontation with Ehrenwall through whatever path they built.

### Stress Tests

**Stress 1 — Conviction challenge (S13):** Torben's formed primary Conviction (assume Order) is challenged when Crown suppresses a community Vossen helped build. Player witnesses the consequences. Belief contradiction (if S2 scene planted an Equity seed alongside Order): Decision Fork fires. The player must decide: act on Order (Crown policy) or act on the emerging Equity understanding. The first Scar risk of Torben's formation — and it will define whether his arc ends in "Order Torben" (classic Crown heir) or "Reform Torben" (the heir who changed).

**Stress 2 — Almud's decline (S17):** Almud enters Arc B (Fortress). He summons Torben and explicitly tells him: "You must represent Order absolutely. No deviation." This is a Standing 5 Duty assignment (deference hierarchy: Almud is Torben's superior, NPC-04 applies). Torben-as-player must either comply (Duty fulfilled: Standing +1 toward Recognition Event) or refuse (Leadership Deviation: Stability check, but Torben gains his own Belief about independence: "I will not be my father's instrument"). The refusal is the Autonomy Conviction crystallization.

**Stress 3 — Legitimacy auction (S22):** Three factions simultaneously approach Torben to support their version of Crown succession. Church offers Consecration (LIN-02 Condition D) for their preferred outcome. Ehrenwall offers military backing (Löwenritter will enforce Torben's claim if he supports the Coup). RM (Vossen or Hann) offers popular legitimacy (community support network). Each offer comes with an Obligation (social_contest §6.1). Player can accept one: which Conviction drives the choice?

---

## NPC 07 — GRANDMASTER LISBETH EHRENWALL (Löwenritter)

### Starting State
**Standing:** 5 (Grandmaster). Löwenritter faction leader.  
**Stats:** Agility 3, STR 3, Endurance 4, Cognition 3, Charisma 3. Combat Pool: 12D (Combat History 4: +4D). WI 10. Max Wounds 3.  
**Conviction:** Order (primary), Autonomy (secondary). Certainty 5 (§7.10). TS 0.  
**Framework:** Martial Honour — Aligned: orders protecting Valorian sovereignty (−1 Ob). Contradictory: advancing personal/factional gain at Valoria's expense (+2 Ob).  
**Inner Circle:** Riskbreaker Commander (Autonomy, covert ops), Senior Templar Captain (Faith+Order, military command), Löwenritter Seneschal (Precedent, institutional records), Deputy Grandmaster (Order, succession candidate).

### Coup Counter as Player Experience
The Coup Counter is Löwenritter's primary faction clock. Ehrenwall-as-player is managing this clock FROM THE INSIDE — she is not just responding to Crown failures, she is the one who decides when failures have accumulated enough to act. Counter advancement is a player decision (she advances it intentionally when she judges Crown governance failing).

**This is the most morally complex NPC-as-player run:** The player is simultaneously Valoria's most disciplined guardian AND its most credible overthrower. Every season, the player evaluates Crown's governance and decides whether to advance the Counter. This is an ethical decision with mechanical consequences, not an automatic response.

**[FINDING POL-SIM-16: Playing as Ehrenwall inverts the Coup Counter from a threat to a tool. The player controls when it reaches 3. This means the player has extraordinary structural leverage — they can time the Coup to maximize their success conditions (Crown weakest, Torben's disposition best, Church suppressed). But the Martial Honour Framework punishes advancing the Coup Counter for personal advantage (+2 Ob on any action advancing personal/factional gain at Valoria's expense). Ehrenwall's Conviction is the primary brake on using the Coup Counter opportunistically. Players who advance the Counter too early (before Crown genuinely fails Valoria) will face Leadership Deviation costs and inner circle confidence erosion. The ethics of the decision ARE the gameplay.]**

### Phase 1 (S1–10): The Watching

Ehrenwall begins as an NPC-mode faction (Löwenritter Priority Tree §7.5 only activates on Crown elimination or Coup). Pre-Coup, she has no formal Domain Action economy — she operates through Riskbreaker Operations (OFC-02), military readiness, and Crown inner circle observation.

**Pre-Coup scene loop:**
- Annual: Military Muster and Review (Ceremonial Scene — demonstrates Löwenritter's military strength publicly, maintains Renown).
- Seasonal: Evaluate Crown's governance (player assesses Almud's Stability, Military engagement, TC advancement). Decide: does this season advance the Coup Counter?
- Delegation: Riskbreaker Commander provides covert intelligence on Crown inner circle dispositions (OFC-02: Löwenritter intelligence archives). Player receives filtered reports (Commander's Autonomy Conviction: he will emphasize intelligence that supports action).
- Political: Build Torben's Disposition (SUC-01: for Coup to succeed cleanly, Torben at Disposition ≥ +2 reduces succession costs). This requires personal investment in the one relationship that will determine whether the Coup creates a clean transition or a civil war.

**Counter advancement logic (S4–8):** Crown Stability 5, TC 30, Torben Loyalty 3. Ehrenwall's judgment (player's decision): No action yet. Counter stays at 0. But by S8: TC 35, Crown has not suppressed. Almud's Certainty 3 is visible as inconsistency. Counter advances to 1. Player has made the first deliberate escalation decision.

### Phase 2 (S11–20): The Edge

**Counter at 2 (S14):** Two Crown failures accumulated. Ehrenwall is now actively preparing the Coup — though she hasn't executed it. This is POW-03 territory: she is effectively running a Parallel Authority scenario internally, managing the Order's operations as if she were already governing, without the formal claim.

**Torben relationship (SUC-02):** Torben is a succession rival in the most literal sense: his Bloodline Claim supersedes any Löwenritter action without his consent. If player has invested in Torben's Disposition (Intimacy Knot possible if player has been treating him genuinely per §2.8: Solidarity primary style), Torben will cooperate with the Coup. If not: Torben resists.

**Deputy Grandmaster watch:** Inner circle member with Order conviction — the Order's succession candidate if Ehrenwall falls. Player must maintain Deputy Grandmaster's Disposition ≥ +1 (SUC-01: if succession is ever contested, Deputy needs to be a reliable ally, not a rival). A Deputy who feels overshadowed will begin building his own Rival Standing.

### Phase 3 (S21–30): The Coup and Its Consequences

**Counter at 3 (S20–22):** Ehrenwall executes. COUP-01 Type 1 (Palace Coup — internal): Crown Stability −1 to −2 depending on inner circle reaction. Torben's Bloodline Claim: if Torben at Disposition ≥ +2 with Ehrenwall: clean co-governance (Legitimacy Token, POW-01). Crown becomes Löwenritter-governed with Torben as figurehead.

**Post-Coup governance (S22–30):** Löwenritter Priority Tree now active (§7.5 fires). Player runs this as their faction AI. Priority 1: Stability ≤ 1 → Military action. Priority 3: Torben Loyalty ≤ 2 → Dynasty management. Player must maintain Torben's cooperation to keep the Legitimacy Token valid. If Torben's Disposition drops below 0 at any point: Legitimacy Token revoked (POW-01). Every other faction gains Casus Belli. Ehrenwall loses the Mandate +1 bonus. The Coup becomes an unprovoked seizure.

**Restoration threat (S26):** POW-02: Torben's maturity triggers Restoration Event if Löwenritter Mandate ≤ 2 AND Torben has inner circle majority. Player (Ehrenwall) must choose: Accept (peaceful transition to Torben, Ehrenwall retains treaty relationships and territory, loses Legitimacy Token) or Resist (civil war — Torben has inner circle, Ehrenwall has military, it's a genuine contest).

### Stress Tests

**Stress 1 — Justified Coup timing (S11):** Crown Stability drops to 3 (Almud's Arc B beginning). Counter at 1. This is a genuine Crown failure — Ehrenwall's Martial Honour Framework would not penalize action here. But Torben is only Standing 1 and Disposition +1 with Ehrenwall (insufficient for clean co-governance). Player choice: execute Coup now (tactical advantage) vs. wait until Torben Disposition ≥ +2 (2 more seasons of relationship building). Advancing the Counter to 2 here: no Framework contradiction. But executing at Counter 2 (next season): leaves succession messy. The patient play is better.

**Stress 2 — Riskbreaker exposure (S16):** Riskbreaker operation (OFC-02 player delegation) goes wrong. A Riskbreaker operative is captured by Church Inquisition. The Löwenritter must disavow (OFC-02 constraint: "If captured or exposed, the Löwenritter disavows them"). Player (Ehrenwall) must publicly deny the operative's Löwenritter affiliation. Lie Ob +2 (Martial Honour Framework contradiction: advancing factional interest through deception). Leadership Deviation Stability check. P(success): ~80%. P(Scar from Honour contradiction): depends on contest outcome.

**Stress 3 — Church challenge (S24, post-Coup):** Himlensendt (or his successor) recognizes the Coup's illegitimacy. Church invokes Excommunication against Ehrenwall for deposing the legitimate Crown. TC +4. Hafenmark may opportunistically support Church's position (constitutional grounds: Baralta opposes Palace Coups). Player must navigate multi-front institutional pressure while governing a faction in the first years of post-Coup stability recovery.

---

## NPC 08 — EDEYJA (Southernmost Warden-Chief)

### Starting State
**Standing:** N/A (no faction hierarchy). She leads the wardens without institutional rank structure.  
**Stats:** Agility 3, STR 3, Endurance 4, Cognition 4, Charisma 2. Combat Pool: 12D (Warden + Thread History).  
**Conviction:** Continuity (primary), Reason (secondary). Certainty 1 (Thread as primary frame). TS 75–80. Coherence 9 (sustained discipline).  
**No formal Inner Circle** — wardens are a functional group, not an institutional hierarchy. Senior wardens (3–5 NPCs) advise but do not vote on succession.  
**No priority tree pre-emergence** — §8.10 fires only Post-Emergence (Arc B). Pre-Emergence (Arc A): no BG Domain Action economy.

### The Most Distinctive Play Experience

Edeyja-as-player is entirely Thread-domain play until Arc B. The player does not manage a faction, does not attend Parliamentary sessions, does not advance Standing. The player is managing:
1. **RS monitoring:** RS across all territories. Edeyja perceives Thread substrate directly at TS 75–80. The player "knows" RS values that other faction leaders are guessing at. This is unique information asymmetry.
2. **Coherence management:** Every Thread operation costs Coherence. Player manages Edeyja's Coherence like a resource pool (starting at 9). Without Discipline scenes, Coherence depletes at 1–2/season from sustained warden operations.
3. **Warden count:** How many wardens remain. Edeyja's arc is partially determined by this number — reaching 0 triggers Arc C regardless of player agency.
4. **Isolation:** Edeyja's charisma 2 and "no outsider has earned the right to warden knowledge" Belief 2 means she CANNOT easily build relationships with faction leaders. This is a deliberate design constraint. She is mechanically isolated from most of the political game.

**[FINDING POL-SIM-17: Edeyja-as-player is the game's most mechanically distinct campaign mode. She has no faction mat, no rank ladder, no Ministry system, no succession concern. Her campaign is a survival horror-adjacent experience: managing declining resources (Coherence, Warden count), tracking an external threat (RS decline), and making the decision about when to break isolation (Arc A → Arc B transition). The game should be explicit that Edeyja-as-player is a specialist mode, not a standard faction leader experience.]**

### Scene Loop
**Warden operations:** Each season, Edeyja and remaining wardens conduct RS maintenance operations. Edeyja's Thread operations: TS 75–80, accessible at deep tier. RS Maintenance: Coherence cost 2 per operation (estimated — [GAP-SIM-POL-02: Exact Coherence cost of RS Maintenance operations not specified in threadwork_v30 for TS 75–80 wardens.]). At 2 Coherence/season: Edeyja's 9 Coherence lasts ~4.5 seasons without Discipline recovery.

**Discipline scenes:** Edeyja must spend 1 scene/3 seasons on Thread Discipline to prevent Coherence depletion. From inside her play: this means every 3 seasons, she "loses" a scene to personal maintenance. Not dramatic — necessary.

**The isolation break (S10–15):** The player decides when Edeyja reaches out. Her Evidence RS and Consequence RS tell her exactly what the data says: the wardens cannot hold the Southernmost alone. The Continuity Conviction demands she hold. The Reason secondary Conviction tells her this is an irrational position if it ends in total failure. Breaking isolation = Arc B entry.

**Arc B trigger from inside:** Player declares Arc B by choosing to accept an outside expedition to the Southernmost. This is an active player choice, not a mechanical trigger. The player is making the decision to acknowledge Edeyja's limits. This is the campaign's most emotionally weighted moment — the player playing Edeyja has been living inside her isolation, and the choice to break it is the character's defining moment.

### Stress Tests

**Stress 1 — Warden death (S8):** A warden is killed by Altonian Vanguard Assault (ED-551 Priority 2b fires). Warden count: 5→4. Player (Edeyja) must decide: intensify operations (risk more wardens), maintain current pace (accelerate RS decline), or seek replacements (requires training new wardens — 3 season minimum, consumes scene slots). Training option: Continuity Conviction-aligned (the work must continue), but delays RS maintenance for those seasons.

**Stress 2 — RS ≤ 40 (S15):** Rendering Stability critical. Player (Edeyja) receives the RS data that makes the strategic picture clear. At TS 75–80, she perceives this directly — not as a stat, but as physical sensation (Thread substrate is thinning). This is the moment her Reason secondary forces a confrontation with Continuity primary: she cannot hold by herself. Arc B becomes necessary. The player has been waiting for this moment — or avoiding it. Either way, it's now unavoidable.

**Stress 3 — Thread anchor failure (S22, Arc B active):** Two seasons after collaboration begins, a major Thread Anchor fails (Lock dissolves). RS −4 in one accounting. Edeyja (Coherence 7) must perform emergency intervention: 2 additional Thread operations this season (Coherence cost: 4). Coherence 7→3. One more intensive season would leave her at Coherence 0 (Rendering Crisis). Player must choose: take the RS loss (−4) and protect Coherence, or intervene fully and risk Coherence Crisis. The companion simulation identified this as a tragic feedback loop. From inside, it's not a design observation — it's a real decision with catastrophic stakes on both branches.

---

## NPC 09 — MARET ULN (Varfell — Succession)

### Starting State
**Conditional activation.** Maret Uln as player only available after Vaynard's elimination. This creates a unique campaign mode: the player plays THROUGH the first Vaynard arc (watching Vaynard as NPC deteriorate), then inherits the faction at the succession moment.

**Standing:** 3→5 (progressive — she begins as a mid-rank Varfell member, then becomes Hochjarl on succession).  
**Stats:** Cognition 4, Charisma 4, Agility 2, STR 2, Endurance 3. Combat Pool: 9D. TS 35 (Active tier). Coherence 10.  
**Conviction:** Equity (primary), Reason (secondary). Certainty 2. Framework: Rawlsian/Consequentialist hybrid.  
**Key difference from Vaynard:** Maret Uln's Equity Conviction means she CANNOT allocate Varfell resources acquisitively. Where Vaynard's Consequentialism justified private Thread research, Maret Uln's Equity requires resources to benefit the community. Her research is collaborative, not proprietary.

### Pre-Succession Play (S1–Vaynard's fall)
If the campaign begins with both Vaynard and Maret Uln as playable, the player as Maret Uln is operating at Lendmann (Standing 3) within Vaynard's court. She has real authority: governs an assigned settlement, may conscript local garrison. But she cannot act against Vaynard's agenda directly (NPC-04: Vaynard is her superior, she defers publicly).

**The internal conflict:** Maret Uln's Equity Conviction conflicts with Vaynard's acquisitive Thread research. She can see what he's doing and disagrees with it — but can't publicly contradict him until she reaches succession. This is the most politically constrained pre-succession experience: the player knows what needs to change but cannot change it from their current position.

### Post-Succession Play
**Jarl Assembly succession (SUC-03):** Vaynard eliminated. Maret Uln presents herself (Standing 3 → needs Assembly vote for promotion to 5). SUC-02: Vaynard's protégé (NPC) is a standing candidate. Assembly votes: player must lobby 3 of 5 Jarls before the vote. Skald-Chief: Maret Uln's RM alignment gives her a tradition question (she's not the traditional Varfell succession candidate). Eastern March: Thread knowledge matters to him. Western Highlands: resource security. Player must navigate 3 separate Disposition-building scenes in the Resolution Window (2 seasons per SUC-03).

**[FINDING POL-SIM-18: Maret Uln's succession is one of the richest single dramatic sequences in the system. She must simultaneously: win the Jarl Assembly vote (3 of 5 Jarls), navigate the deference hierarchy transitioning out of (Vaynard's protégé still commands old guard loyalty), and establish her Equity-based governance agenda against a faction culture of Consequentialist pragmatism. The 2-season resolution window for contested succession (SUC-03) is likely too short for a transition of this complexity. ED needed.]**

### Stress Tests

**Stress 1 — RM alignment scandal (S3 post-succession):** Maret Uln's known RM alignment triggers Varfell's LendmannS Council concern: "She's going to redirect our resources to the movement." Player must manage: reassurance scene (Varfell Covenant commitment) OR actually redirect resources (Equity Conviction alignment, but costs Varfell's Consequentialist NPC support). The founding governance tension of Maret Uln's rule.

**Stress 2 — Vaynard's Thread research legacy (S5 post-succession):** Vaynard's private Thread research exists in Varfell archives. This is a resource that could benefit either Varfell privately (Consequentialist option) or the peninsula broadly (Equity option). Maret Uln's Belief 1: "Vaynard's path led to destruction — knowledge must serve the community." She must redistribute the research — but to whom? Edeyja (Southernmost), RM (Vossen/Hann), Hafenmark (Baralta academic network)? Each choice creates a different alliance and a different obligation.

**Stress 3 — Protégé challenge (S8 post-succession):** Vaynard's protégé reaches Rival Standing 3 (having built his own Jarl support during Maret Uln's transition period). SUC-03 fires again. Another contested succession within Maret Uln's first year-arc. Player must win a second Jarl Assembly contest while already governing. This reveals the structural fragility of succession succession (a faction that has lost its previous leader and undergone contested succession is immediately vulnerable to another challenge while the new leader is still establishing authority).

---

## NPC 10 — TORSVALD (Löwenritter — Riskbreaker)

### Starting State
**Standing:** 2→4 (Riskbreaker's public Standing is always 1 externally — OFC-02: "appears to be at Standing 1 to anyone outside the Order"). Internal Standing: 2–4 within Löwenritter covert command chain.  
**Stats:** Agility 4 (inferred), STR 3, Endurance 3, Cognition 3, Charisma 3. Combat Pool: 14D (inferred). TS 20+. Coherence 8. Certainty 2.  
**Conviction:** Inferred Autonomy (primary), Order (secondary). [GAP-SIM-POL-03: Torsvald §2 entry still absent — confirmed by ED-591 from prior session. Simulation remains inferential.]  
**Office:** OFC-02 Riskbreaker — distinct authority and constraints govern every action.

### The Riskbreaker Play Mode
This is the game's most operationally specialized NPC-as-player run. Torsvald-as-player uses:
- **Covert fieldwork as primary tool:** Enter hostile territories without Exposure escalation on entry. Active fieldwork still accumulates AP.
- **Evidence suppression (1/scene):** Remove a finding from Evidence Track when operating covertly.
- **Löwenritter intel archives:** +1D on Interview actions with historical precedent.
- **Niflhel contacts:** +1D on subterfuge when working through Niflhel-adjacent channels.

**The core constraint:** Torsvald cannot be acknowledged by the Löwenritter if exposed. No backup. If captured: the Grandmaster (Ehrenwall, NPC or player) must disavow. This creates an unusual player relationship with the faction: you are simultaneously a member with real Standing AND an asset the institution will burn if convenient.

### Season Structure
**Mission loop (per OFC-02):**
1. Receive mission from Riskbreaker Commander (delegation in reverse: the Commander is Torsvald's superior, not Ehrenwall directly). Mission: Intelligence gather, neutralize target, plant evidence, suppress investigation.
2. Infiltrate target location. Player conducts covert fieldwork (Shadow Renown accumulates, not public Renown).
3. Execute mission. Key mechanic: P(successful extraction without attribution) — Agility 4 (inferred) + Autonomy Conviction alignment (covert = not power-concentrating, but also not community-benefiting — Conviction neutral). Roll: 8D (estimated), Ob varies by mission type.
4. Extract. If successful: mission complete, Shadow Renown +1. If exposed: disavowal scene (Ehrenwall or Commander explicitly denies Torsvald's existence in a scene — this is a Scene Slate entry that the GM must run separately).

**TS advancement risk:** Each covert operation triggers Discovery Event check (Spirit 2, Ob 2, P = 18%/operation). 4 operations/season: P(Discovery Event/season) ≈ 56%. Fast TS advancement (per companion sim finding SIM-C-02 extended: Torsvald's path accelerates TS faster than any other NPC). By S8: TS likely 30+ (Stirring crossed).

**[FINDING POL-SIM-19: Torsvald-as-player is the game's most mechanically fragile run precisely because of TS advancement. His operational intensity (4+ missions/season in a covert campaign) almost certainly crosses the Stirring threshold within 8–10 seasons. Without practitioner training (Edeyja unavailable to him unless the Warden Collaboration arc fires — which requires a non-Torsvald player to achieve), he faces unmanaged TS advancement toward Active tier. The discovery events pile up faster than his Coherence can sustain. Torsvald-as-player has an expected campaign lifespan of ~12–15 seasons before the Thread arc becomes unmanageable without outside intervention.]**

### Stress Tests

**Stress 1 — Mission target is innocent (S5):** Player receives mission: suppress the Inquisition's investigation in T6 (remove Evidence from Church AP track). Arrives to find: the "target" is a genuine Thread practitioner who the Church is correctly pursuing — but who is also RM-affiliated and Vossen's community contact. Suppressing the evidence protects the community. Torsvald's Autonomy Conviction: his job is the mission, not the ethics. But his Certainty 2 means he genuinely perceives Thread reality — he KNOWS the practitioner is real and the Church is genuinely dangerous to Thread practice. Decision Fork: complete the mission (OFC-02 operational framework) or deviate (Riskbreaker Commander becomes aware, Rival Standing risk).

**Stress 2 — Exposure (S10):** A mission goes wrong. Torsvald is identified by Church Inquisition. OFC-02: Löwenritter disavows. Ehrenwall publicly denies. Torsvald is now persona non grata — no faction backing, no identity. He must survive independently for 2 seasons until the situation can be cleared. This is a pure personal-scale survival arc: Torsvald with 14D combat pool, TS 30+ (first Discovery Event likely past), and Coherence 8 (depleting). Shadow Renown helps: Niflhel contacts may provide safe house access.

**Stress 3 — TS crisis (S14):** TS 35+ (Active tier). Discovery Events at operational intensity: Coherence 8→6→4 over S12–14. Player (Torsvald) is running missions at reduced Coherence, aware that Thread substrate is increasingly present to his perception. At Coherence 4: each Thread operation costs 2 Coherence (Rendering Crisis approaches). Player must either reduce mission tempo (disobeying Commander's operational demands → Rival Standing within Löwenritter covert chain) or push through (Coherence 0 within 2 seasons). There is no clean resolution without practitioner support.

---

## NPC 11 — ALDRIC HANN (Restoration Movement)

### Starting State
**Standing:** Informal 3–4 within RM (Hann is the operational sub-leader, not the symbolic leader). No formal rank system.  
**Stats:** Agility 3, STR 3, Endurance 3, Cognition 3, Charisma 3. Combat Pool: 9D. Circles 3+ in logistics/street networks.  
**Conviction:** Equity (primary, less committed than Vossen), Autonomy (secondary). Certainty 3.  
**Relationship to Vossen:** Hann operates UNDER Vossen in RM hierarchy. If both are player characters in multi-player context: Hann is Vossen's delegate (NPC-03 in RM structure). If Hann is the solo player character: Vossen is the NPC leader above him, and Hann experiences delegation from the other side — receiving assignments from Vossen, not giving them.

### The Operational Experience
Hann-as-player is the game's most operationally focused character who is NOT a specialist (unlike Torsvald/Riskbreaker). He works in logistics, street networks, and covert supply chains — but with full visibility to the player, not the institutional anonymity of the Riskbreaker. Hann is the man in the warehouse, not the man in the shadows.

**Primary tools:** Circles 3+ logistics network. Each season: free Interview-equivalent from logistics contact (supply chain information). Covert network management: monitor Church infiltration of RM cells (AP tracking for RM territories from the street level, not the leader level). Operational efficiency: −1 Ob on supply chain fieldwork actions.

**The Vossen dynamic (if Vossen is NPC):** Hann receives Duties from Vossen (NPC-03 delegation). He has less freedom than Vossen but more operational flexibility (Vossen's Equity framework constrains means; Hann's Autonomy secondary allows more pragmatic methods). The tension: Hann can achieve operationally what Vossen won't authorize, and he knows it. Decision Forks arise when Hann's assessment of operational necessity diverges from Vossen's Conviction-based restrictions.

**[FINDING POL-SIM-20: Hann-as-player under Vossen-NPC is the game's most interesting subordinate play experience. The player regularly assesses: "I could do this more effectively using methods Vossen won't approve." The player chooses compliance (Vossen's Duty structure maintained, Trust +1) or independent action (operational success, but Vossen's Disposition −1 if discovered). This is the dual-agenda mechanic (player_agency_v30 §1.2) at its purest: institutional loyalty vs. personal judgment. Hann-as-player generates this tension every season.]**

### Stress Tests

**Stress 1 — Niflhel integration (S6):** Hann discovers that Niflhel already has a contact inside a key RM supply chain. He can: expose the infiltration (Vossen approves, cell disrupted, supply chain weakened), co-opt the contact (Hann uses Niflhel contact for RM ends — Vossen never knows, operational efficiency maintained), or report to Vossen and let her decide (Vossen's Equity framework will shut it down, Hann loses operational leverage). The co-option option: Autonomy Conviction alignment (survival of the operation matters). But if Vossen ever discovers: massive Disposition loss and Scar risk from betrayal of movement values.

**Stress 2 — Vossen captured (S14):** Church Inquisition arrests Maret Vossen. Hann is now effectively the RM leader. Player inherits all of Vossen's obligations without any of her Standing or Charisma. Hann (Charisma 3 vs. Vossen's 5): all community-building actions at Ob +1 (he is less effective in Vossen's domain). Player must run the movement through the crisis while simultaneously planning Vossen's rescue (operational planning = Hann's domain, P(successful extraction): ~35% covert, ~55% with Niflhel contact help).

**Stress 3 — Successor dilemma (S22):** If Vossen has been lost or stepped back, Hann is the RM leader. He doesn't have Vossen's grassroots legitimacy. A more charismatic community organizer (NPC) is emerging who could better serve the movement. Hann's Autonomy secondary: "I should do what's best for survival, even if that means stepping aside." His Equity primary: "The community deserves the best leader, not me if I'm not the best leader." The decision to voluntarily cede leadership is the most Equity-consistent action Hann can take — and the most counterintuitive for a player who has been building the character for 20 seasons.

---

## CROSS-NPC FINDINGS

### FINDING POL-SIM-21: The Delegation-Filtering Problem is Universal

Every faction-leader NPC-as-player (Almud, Himlensendt, Baralta, Vaynard, Ehrenwall) faces the same information asymmetry: their delegates filter reports through their own Convictions. No canonical mechanic exists for this. Players who play faction leaders must understand that "the Marshal says the military situation is stable" means "the Marshal, whose Order Conviction prioritizes stability, has assessed the situation through that lens and selected information that supports a stable reading." This is accurate to historical governance — but it needs a mechanic.

**Proposed mechanic:** Each delegate has a Filtering Ob (1–3, based on Conviction divergence from delegated task): a player who wants unfiltered intelligence must either conduct personal Investigation (breaking their Availability State, which costs social Renown per REN-03) or invest in a Schattendienst-equivalent auditing mechanism. Without this investment, all delegated intelligence is filtered.

### FINDING POL-SIM-22: Scene Slate Overload at Faction Leader Level

Every faction leader NPC-as-player (Almud, Baralta, Vaynard) has more mandatory scene obligations than can be accommodated in a standard season:
- Parliament/Assembly Ceremonial Scenes: 2/year-arc
- Inner Circle Duty scenes: 2/year-arc (Standing 5 obligation)
- Recognition Event scenes (delegated): 1–2/year-arc for NPCs advancing through ranks
- Outreach/Demand from NPCs: 1–3/season
- Crisis response scenes (Priority 1–3 fires): ad hoc

**A Baralta player in a typical year-arc:** 2 Parliament scenes + 2 Inner Circle Duty scenes + 1 Guild Comptroller audit + 2 incoming Outreach scenes = 7 mandatory scenes/year-arc, before the player initiates any personal scenes. Current scale_transitions scene slot economy does not address faction-leader scene overload. The scale_transitions §4.3.2 trigger list was designed for a personal-scale player with faction standing, not for the faction leader themselves.

**[GAP-SIM-POL-04: No rule specifies how faction-leader players manage scene overload. Does delegation count as a scene? Can the player "pass" mandatory ceremonial scenes by delegating attendance? What is the scene cost of running a Royal Audience as the presiding authority vs. attending one as a petitioner? These are fundamental questions for NPC-as-player mode that the existing system doesn't answer.]**

### FINDING POL-SIM-23: The Conviction-Obligation Loop

For every faction-leader NPC-as-player, their institutional obligations are Conviction-aligned. Breaking obligations means breaking Conviction. This creates a self-reinforcing loop:
- Baralta's obligation (maintain coalition majority) IS her Precedent Conviction (the parliamentary process must be maintained).
- Almud's obligation (attend court audiences) IS his Order Conviction (visible, public, virtuous governance).
- Ehrenwall's obligation (maintain military readiness) IS her Order Conviction (Valoria endures through martial excellence).

This means faction-leader players have almost no Conviction contradiction in their routine obligations — the institution was designed to house their Conviction. The contradiction only comes from world events that challenge the institution itself. This is historically accurate (institutional structures are self-reinforcing for their leaders) and produces the correct play experience: easy in calm times, intensely contradictory in crisis.

### FINDING POL-SIM-24: Rank Ladder Progression Times (FAC-01/02 Testing)

Running the FAC-01/02 rank ladder for Torben-as-player (the one NPC who actually uses the full ladder):

| Standing | Rank | Recognition Event | Time to achieve |
|----------|------|-------------------|----------------|
| 1→2 | Hofmann→Kronagent | Automatic (birthright) | S1 |
| 2→3 | Bannerherr | Royal Audience (Almud presides) | S10–12 (requires 3 Duty completions at Crown estimate) |
| 3→4 | Kronleutnant | Royal Audience + inner circle majority | S16–18 |
| 4→5 | Reichsseneschall | Royal Audience + succession eligibility declared | S22–24 (if Almud survives) |

Progression timeline: ~22–24 seasons to Standing 5 from a royal birthright start. This is appropriate for a 30-season campaign — Torben reaches succession eligibility in the final phase. But it reveals: if Almud is eliminated before S22 (Coup Counter 3 fires at S16–20 in typical campaign), Torben will not have reached Standing 5 yet. The Coup fires before the legitimate heir is ready. This may be intentional.

**[FINDING POL-SIM-24 CONT: The Coup Counter's typical firing range (S16–22 in aggressive Crown failure scenarios) and Torben's progression timeline (S22–24 to succession eligibility) create a consistent 0–6 season gap where the Coup fires before the heir is ready. This gap is the Löwenritter's operating window — the period where they must govern without Torben's full institutional backing. The Figurehead Status mechanic (POW-01) is specifically designed to bridge this gap. The timeline analysis confirms: POW-01 is not a contingency mechanic, it's the expected outcome for most Ehrenwall-Torben scenarios.]**

### FINDING POL-SIM-25: Structural Gaps for Non-Institutional Players

Three NPC-as-player modes have no patch register support: Vossen, Edeyja, Torsvald. Each operates outside the institutional framework the patch register assumes.

| NPC | Missing support |
|-----|----------------|
| Vossen | No RM rank ladder; no Founding trigger definition; no movement-health tracker; no Uprising holding condition resolution (ED-588 pending) |
| Edeyja | No warden count tracking mechanic; no RS drain rate for Arc C; no BG Domain Action economy pre-emergence |
| Torsvald | No §2 entry (ED-591 confirmed); no discovery-event rate calibration for operational tempo; no practitioner support pathway |

All three need supplementary design before their NPC-as-player mode is playable.

---

## NEW EDITORIAL ITEMS GENERATED

### New EDs (next_id: 601)

| ID | Description | Priority |
|----|-------------|----------|
| ED-601 | Delegation-filtering mechanic absent. Delegate reports should carry Filtering Ob (1–3) based on Conviction divergence. Players cannot access unfiltered intelligence from high-status delegates without direct Investigation (breaking Availability State). | P2 |
| ED-602 | Faction-leader scene slate overload. No rule for scene capacity at Standing 5. Faction leaders face 7+ mandatory scenes/year-arc before personal agenda. Need scene delegation cost rules and ceremony attendance proxy mechanics. | P2 |
| ED-603 | RM Founding trigger conditions undefined. §8.9 states RM Priority Tree is "Post-Founding Only" but no mechanic defines what constitutes Founding or when it triggers. P1 for Vossen-as-player mode. | P1 |
| ED-604 | Pre-Emergence Edeyja has no BG Domain Action economy. §8.10 fires post-emergence only. Edeyja-as-player has no BG-layer agency before Arc B trigger. Design needed for warden season structure. | P1 |
| ED-605 | Torsvald TS advancement from operational tempo: Discovery Event rate at 4 missions/season (~56%/season) reaches Stirring within 8 seasons. No practitioner pathway available to Riskbreaker. Without Edeyja collaboration, Torsvald-as-player has an expected playable lifespan of 12–15 seasons. Confirm intended or add practitioner access path. | P2 |
| ED-606 | Contested succession 2-season Resolution Window (SUC-03) insufficient for faction-leader transitions at the complexity level of Maret Uln's succession. Recommend 3-season window for succession following Arc C elimination of predecessor. | P2 |
| ED-607 | Parallel Authority (POW-03) + Torben companion paradox (ED-594) requires unified ruling: when Torben is simultaneously a companion (personal scale) and a Figurehead (BG scale), do personal Disposition and BG Loyalty advance independently or synchronize? | P2 |
| ED-608 | Ministry system (MIN-01-06) proposed for Crown only. No equivalent administration mechanic for Hafenmark (Guild Comptroller analog), Varfell (Jarl sub-network), or Church (College of Prelates management). Cross-faction parity gap. Confirm whether administration mechanic is Crown-specific or needs all-faction equivalents. | P2 |
| ED-609 | Warden count tracking: Edeyja's arc depends on Warden count but no mechanic tracks this number or triggers arc conditions when count reaches 0 or other thresholds. | P1 |
| ED-610 | Coup Counter advancement should require Leadership Deviation check when advanced opportunistically (player advancing Counter without genuine Crown failure). Martial Honour Framework penalty (+2 Ob on personal/factional gain at Valoria's expense) applies but is not explicitly tied to Counter management. Confirm or deny. | P2 |

### Open ED-POL Items from Patch Register
The following ED-POL items from the patch register were not resolved by these simulations and remain as proposed editorials requiring design attention:

| ID | Priority | Status |
|----|----------|--------|
| ED-POL-01 | P1 | Inner circle NPCs unnamed — blocks succession simulation fidelity |
| ED-POL-03 | P1 | Torben generational clock undefined — Restoration Event timing depends on this |
| ED-POL-05 | P1 | Ministry NPCs need Stance Triangles (Schattendienst and Markamt ministers especially) |
| ED-POL-06 | P1 | Ministry competence decay sim needed (BALANCE-POL-02 concurrent) |
| ED-POL-12 | P1 | Availability State tracking implementation unspecified |
| BALANCE-POL-01 | P1 | Cross-faction rank parity review pending |

---

## NEW SIM-DEBT

| ID | Description | Status |
|----|-------------|--------|
| SIM-POL-01 | Ministry competence decay and player-intervention rate calibration (ED-POL-06) | OPEN |
| SIM-POL-02 | Torben generational clock: test milestone timing against typical Coup Counter activation | OPEN |
| SIM-POL-03 | Hann-as-player under Vossen-NPC: full 30-season dual-agenda simulation | OPEN |
| SIM-POL-04 | Edeyja pre-emergence warden season structure: validate operational tempo and Coherence consumption | OPEN |

---

## COVERAGE MATRIX ADDITIONS

### Confirmed Working (NPC-as-player)
| System | Source | Status |
|--------|--------|--------|
| Conviction-obligation loop self-reinforces in calm; breaks in crisis — correct design | All faction leaders | ✓ Validated |
| Baralta Suppress obligation viscerally mandatory from inside — correct | POL-SIM-10 | ✓ Elegant lock-in |
| Ehrenwall Coup Counter as player-controlled tool — ethics ARE the gameplay | POL-SIM-16 | ✓ Correct |
| Torben blank Conviction formation via scene choice — best protagonist creation system | POL-SIM-15 | ✓ Distinctive |
| Almud's Reason→Order deviation costs produce expected Stability erosion by S20 | POL-SIM-04 | ✓ Calibrated |
| Himlensendt Arc C from inside inverts Inquisition tools against himself — loop closes perfectly | POL-SIM-08 | ✓ Brilliant |
| Vaynard Discovery Events probabilistically unavoidable — correctly produces inevitable arc | POL-SIM-12 | ✓ Intentional design |
| FAC-02 Recognition Event timeline puts Torben at succession eligibility S22–24, Coup at S16–22 — creates expected Figurehead gap | POL-SIM-24 | ✓ POW-01 is not contingency, it's expected |

*End of simulation document. 11 NPCs as player characters. 10 new EDs (601–610). 4 SIM-POL items. Multiple gap confirmations and design validations.*
