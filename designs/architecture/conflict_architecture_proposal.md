# Valoria — Conflict Architecture Proposal

**Date:** 2026-04-19  
**Status:** PROPOSAL — synthesizes 4 sim batches + ignition analysis + Jordan feedback  
**Supersedes:** `early_game_ignition_analysis.md` (timing model revised, Niflhel dissolved, Tensions Deck rescoped)

---

## Core Insight

The game's conflict engine is the three-scale governance hierarchy: **Peninsula → Province → Settlement.** Control flows upward (win settlements → hold provinces → control the peninsula). Pressure flows downward (peninsula events → province consequences → settlement disruption). This bidirectional flow makes the game self-sustaining — structural misalignment at any scale propagates to the others.

The early-game ignition problem was never a missing system. It was a failure to recognize that the starting settlement map already contains five governance disputes. The game starts on fire. The design just didn't know it.

---

## The Three Scales

**Peninsula** (strategic map). Faction victory measured by PV accumulation. Parliamentary weight, RS/CI/IP/PI clocks, Altonian pressure, and victory conditions live here. This is what the player sees when they zoom out. Changes at this scale take 5+ seasons to materialize. The peninsula is the *consequence layer* — it registers what happened below.

**Province** (territory cards). Governance legitimacy measured by Accord. Province PV derives from the prosperity of aligned settlements. Fragmentation checks fire here when settlements don't align with the province controller. Military movement, mass battles, and territorial transfer operate here. The province is the *contest layer* — where factions formally compete for control.

**Settlement** (nodes within provinces). Infrastructure presence determines functional allegiance. Church buildings, Guild markets, Crown ministerial offices, RM consensus cells, garrisons, and governors all compete for institutional space within each settlement. The settlement is the *engine layer* — where power is actually built, and where friction generates conflict that propagates upward.

**Resolution order each season:** Settlement → Province → Peninsula. Infrastructure resolves first; fragmentation and military resolve second; clocks and victory resolve third. This means ground-level governance changes are always the leading indicator of strategic-level shifts. A player watching the peninsula map sees provinces changing color — but the real game happened two resolution phases earlier, when infrastructure actions at settlement scale changed who actually governs the population.

---

## Starting Friction Points (Already in Canon)

Five provinces begin the game with non-aligned settlements. No new system is required to generate early-game conflict — only the recognition that these misalignments produce fragmentation checks from S1.

**T1 Valorsplatz: Crown vs Church.** S003 Valorsplatz Cathedral is Church-held within the royal capital. This IS the Investiture Controversy at settlement scale. Who governs the Cathedral district — the king's appointed magistrate or the bishop who runs the cathedral? Every Accounting, Crown runs a fragmentation check (Influence 5 vs Ob 3). On failure, the Cathedral district moves toward formal Church governance. Crown must either consolidate (political cost — Church cries persecution) or accept (Church footprint in the capital grows). Hafenmark watches for parliamentary leverage.

**T8 Gransol: Hafenmark vs Guilds.** S017 Market Quarter (Prosperity 5, highest non-capital) is Guild-held within Baralta's capital province. Hafenmark's parliamentary sovereignty platform is undermined by a merchant district that doesn't answer to Parliament. Forcibly consolidating alienates the merchant class. Tolerating creates a permanent PV leak. This is the historical tension between feudal authority and merchant republics — Florence vs the Medici, the Hanseatic cities vs their nominal lords.

**T14 Ehrenfeld: Crown vs Löwenritter.** S014 Barracks is Löwenritter-held within Crown's most strategic province (Fort 3, five-way hub). Crown claims the province; Ehrenwall commands the garrison. With graduated autonomy (below), this friction produces the entire Löwenritter arc without needing a separate Coup Counter — the settlement-level misalignment IS the institutional tension.

**T4 Grauwald: Varfell vs RM.** S029 Lodge is RM's covert foothold in Vaynard's territory. Varfell and RM want compatible things (Einhir restoration) through incompatible methods (military conquest vs community organizing). If Vaynard suppresses the Lodge, he loses Einhir cultural infrastructure his population values — Accord drops. If he tolerates it, RM grows.

**T13 Oastad: Varfell vs RM.** S032 Shrine is RM's overt presence. Same dynamic as T4 but more visible — the Shrine is a public Einhir ceremonial site, not a covert meeting lodge.

Each of these fires a fragmentation check every Accounting from S1. The game doesn't need an event card to start a conflict. The conflict is structural. What it needs is for the simulation (and the player) to notice.

---

## Church Expansion: Bishop Appointment

Church gains a second territorial expansion path that bypasses CI entirely and operates at settlement scale.

**Ecclesiastical Appointment.** Domain Action (Consul Outward). Available when: settlement has Church building ≥ tier 2 (Church or Cathedral) AND settlement has no governor OR settlement governor Disposition toward Church ≥ +2. Church rolls Influence vs Ob 1. Success: Church installs a bishop-governor. The settlement is now Church-governed. Its Prosperity flows to Church. Its Order is maintained by Church institutional infrastructure.

Why Ob 1: the appointment is administrative, not contested. The bishop is already there running the church. The "appointment" is formalizing what's already happening. The contest isn't whether the bishop becomes governor — it's whether other factions react.

**Consequences flow through existing systems:**
- Province fractionalizes (non-aligned settlement → fragmentation checks fire)
- Accord in the settlement adjusts by PT alignment (high PT territory: population accepts; low PT: population resists)
- The province controller must choose: consolidate (take the settlement back — costs a card slot and creates a political incident) or accept (Church footprint grows, PV leaks)
- Casus Belli NOT generated (appointment is non-military — this is the key distinction from Seizure)

**Interaction with CI/Mass Seizure:** Church still accumulates CI through Piety Yield. Mass Seizure at CI 60+ still exists as the nuclear option. But bishop appointment means Church has territorial control *before* Seizure fires. Mass Seizure becomes the moment Church stops being a partner in governance and declares itself the government — the formalization of a reality that's been building at settlement scale for 15 seasons.

**The Geneva trap:** A secular faction that accepts Church infrastructure for the Stability bonus (+0.5 from Parish Social Services) is accepting a future bishop appointment claim. The benefit is real and immediate. The cost is deferred and incremental. This is how historical theocracies actually formed — not through conquest but through institutional helpfulness that became institutional control.

---

## Graduated Löwenritter Autonomy

Replace the binary coup (Counter ≥ 4 → instant faction separation) with a four-stage progression driven by the T14 settlement friction.

| Stage | Trigger | T14 Status | Crown Effect |
|-------|---------|-----------|--------------|
| **Loyal** | Start | S014 Barracks answers to Crown via Ehrenwall. Garrison deployable. | Normal. Crown controls T14 fully. |
| **Restless** | Crown Stability ≤ 3, or no military action for 4+ seasons, or Crown loses a province | S014 follows Löwenritter orders for defensive actions. Crown can deploy garrison offensively at +1 Ob. | Crown feels garrison slipping. Fragmentation checks at T14 get harder (Ob +1). |
| **Autonomous** | Crown Stability ≤ 2, or Ehrenwall's Disposition toward Almud drops below 0, or 4+ seasons at Restless without resolution | S014 does not respond to Crown commands. T14 garrison follows Ehrenwall exclusively. Crown retains sovereignty claim — map still shows Crown color. | Crown Military reduced by T14 garrison units. Crown cannot access Fort 3. PI −1. De facto split, de jure fiction of loyalty. |
| **Split** | Crown attacks Löwenritter, or Crown is eliminated, or 4+ seasons at Autonomous without diplomatic resolution | T14 becomes Löwenritter territory. Löwenritter = separate faction (M3/I2/W3/Mil6/Stab5). PI −3. | Crown loses T14, PV drops by 3. Löwenritter negotiates independently. T14 Fort 3 + Mil 6 = nearly impregnable. |

The **Autonomous** stage is the richest game state. It's the Teutonic Order in Prussia — nominally loyal, functionally independent, and every neighboring faction must decide how to treat the ambiguity. It can persist for many seasons without resolving. It creates the Praetorian dynamic without needing an artificial Coup Counter: the settlement-level misalignment at T14 IS the institutional pressure.

The progression is reversible at stages 1–3. Crown can return Löwenritter to Loyal by: raising Stability above 3, conducting a military action that validates Löwenritter's martial identity, or improving Ehrenwall's Disposition through diplomatic engagement. Only stage 4 (Split) is irreversible without reconquest.

---

## Royal Assassination as Fuse

One assassination event per campaign, firing at S8+ minimum. Target determined at game start (Tensions Deck draw or randomized). The assassination succeeds when it fires — no attempt/failure variance.

**Fuse model:** S0: the player receives signals that a plot exists (NPC dialogue, atmospheric events, intelligence reports). S1–S7: escalation visible. Player can investigate (costs card slots). If the player identifies and stops the plot: assassination averted, but the investigation itself reveals faction-level tensions and NPC allegiances. If the player doesn't intervene: the event fires at S8+ (exact season randomized within S8–S12 window).

**Target consequences:**

**Lenneth dies → Almud revenge arc.** Crown's king diverts resources to finding the killer. Crown governance suffers as Almud's attention narrows. Investigation arc opens — every faction is a suspect. Crown's defensive posture breaks from inside (the king himself is pulling resources away from governance into pursuit). Meanwhile, without Lenneth's moderating influence, Crown's Einhir policy hardens. RM PW advances. Southern Accord erodes.

**Torben dies → Elske retrieval.** Crown must get Elske back from Altonia — she's the only remaining heir. Retrieval requires military deployment to T4 (Varfell territory) to establish an extraction route. This is a direct provocation against Varfell AND an Altonian diplomatic crisis (IP spike). The succession question and the Altonian question merge into one compound event that touches three factions simultaneously.

**Almud dies → Lenneth takes the throne.** Crown's factional identity inverts. Lenneth is pro-Einhir, pro-Thread-research, anti-caste-suppression. Crown becomes an ally of Varfell and RM on the Einhir question while becoming a heresy target for Church. Löwenritter must decide whether to protect a "heretic queen" or advance toward Autonomous/Split. This is the most transformative outcome — it changes what Crown IS, not just what Crown has.

Each target produces a different mid-game. The player sees the fuse burning from S1 and must decide: spend resources investigating (competing with faction-building) or let it burn and deal with the consequences.

---

## Niflhel Dissolution

Strike Niflhel as a faction. Distribute its functions into settlement-level phenomena.

**Black Markets.** Any settlement with Order ≤ 1 or no governor develops a black market. Effect: settlement Wealth +0.5 (illicit trade is still trade), Accord −0.5 (population distrusts lawless governance). Disappears when Order ≥ 3. This is a systemic consequence of governance failure, not a faction's strategy. A faction that over-extends generates black markets that provide income but erode legitimacy.

**Intelligence Brokers.** Individual NPCs in specific settlements who sell information. Not coordinated — each broker operates independently for personal profit. Discoverable through Tribune or Riskbreaker actions. Can fabricate intel for profit when peace reduces demand for genuine intelligence (the Ems Dispatch pattern, but driven by individual greed rather than organizational strategy). Can be killed, bought out, or turned. Replaces Niflhel's entire intelligence arm with a more textured, settlement-anchored system.

**Thread Exploitation Sites.** Specific settlements at Proximity ≤ 2 where Thread residue accumulates naturally. Anyone who finds these sites can harvest. Harvesting degrades RS further. The economic incentive to harvest creates moral hazard — the tragedy of the commons, not a conspiracy. Replaces Niflhel's Quiet arm Thread Harvest mechanic with a location-based phenomenon.

**What's eliminated:** Niflhel faction stat block, priority tree, four-arm structure, intelligence product system, all references to Niflhel as a coordinated organization. NPC characters previously described as Niflhel operatives (the Quartermaster, the Quiet One) become independent actors tied to specific settlements.

**What's preserved:** Every function Niflhel performed — intelligence sale, economic exploitation of weak governance, Thread resource extraction, fabricated intelligence as conflict catalyst — still exists. It's just systemic rather than factional. More historically grounded. No shadow conspiracy required.

---

## Tensions Deck (Rescoped)

The Tensions Deck is a variability modifier, not an ignition necessity. Settlement governance friction generates early-game conflict regardless of which cards are drawn. The deck amplifies specific friction points for per-game variety.

**Reduced scope:** 6 cards, draw 1 at game start. Each card is a fuse (condition established S0, event fires S8+). The single drawn card determines which starting friction point burns hottest and which mid-game disruption event fires.

| # | Card | Amplifies | S8+ Event |
|---|------|-----------|-----------|
| 1 | **Royal Crisis** | T1 Crown-Church friction + succession | One Royal family member assassinated (sub-roll for target) |
| 2 | **Feldmark Famine** | T5 Crown breadbasket | Prosperity collapse in Crown's food supply → economic crisis |
| 3 | **Cardinal Independence** | T1 + T9 Church internal | Rogue Cardinal unilaterally appoints bishop-governor in Crown settlement |
| 4 | **Guild Fracture** | T8 Hafenmark-Guild friction | S017 Guild schism → Market Quarter becomes contested |
| 5 | **Einhir Incident** | T4 + T13 Varfell-RM friction | Public Einhir cultural confrontation forces all factions to declare position |
| 6 | **Ministry Crisis** | T14 Crown-Löwenritter + Crown governance | Ministry bureaucracy collapses → Crown governance vacuum → Church fills |

Every card creates a visible fuse from S1 (NPC dialogue, atmospheric events, player-visible signals). The player can investigate and attempt intervention during S1–S7. The event fires if not averted.

**Why 1 card instead of 2:** Jordan's conversation direction emphasized that settlement friction is the real ignition. With 5 starting friction points already generating conflict, adding 2 amplifiers over-determines the early game. One card gives variety without overwhelming the player's attention. Different campaigns have different fires — but only one is externally stoked. The rest ignite from the structural misalignments already present.

---

## What's Cut

| From the original ignition analysis | Why cut |
|-----|---------|
| Niflhel Provocation (Priority 2b) | Niflhel dissolved. Replaced by intelligence broker fabrication at settlement level. |
| Löwenritter Martial Honor Pressure (Priority 3b) | Subsumed by graduated autonomy. The T14 settlement friction + autonomy progression IS the pressure. A separate mechanic is redundant. |
| Tensions Deck at 8–10 cards, draw 2 | Overschoped. Settlement friction is the ignition. Deck is variability, not necessity. 6 cards, draw 1. |
| Altonian Ultimatum card | Too early for Altonian pressure. IP starts at 0; Altonian events belong in mid-game, triggered by IP thresholds. The Torben assassination (Royal Crisis card) creates Altonian pressure naturally if Elske retrieval fires. |
| Löwenritter Exercises card | Redundant with graduated autonomy. |
| Calendar deadline (treaty expiration) mechanic | No canon basis for starting treaties. Added complexity without proportional value. The fuse model on the Tensions Deck cards already creates the deadline dynamic. |
| New faction (any) | Confirmed unnecessary. Settlement phenomena + existing factions cover all ignition roles. |

---

## Assessment: Robust, Smooth, Elegant

**Robust.** The three-scale model allows strategic thinking at every level (where to build infrastructure, which settlements to contest, which provinces to prioritize, which peninsula-level clocks to manage). Customization comes from faction-specific tools at settlement scale (Church builds, Crown administers, Hafenmark trades, Varfell organizes, RM communes). Variety comes from which starting friction points the player prioritizes. Emergent narrative comes from fragmentation checks, bishop appointments, and black market emergence — all system-driven, no scripting.

**Smooth.** Settlement → Province → Peninsula resolution order is clean. Infrastructure actions at settlement feed fragmentation at province feed PV/clocks at peninsula. Each scale has its own resolution logic but they feed each other through defined interfaces (settlement Order → province Accord; settlement controller alignment → province PV share; province military action → peninsula RS/IP/Strain). The bishop appointment mechanic integrates with the existing governor system (settlement_layer §3.2). Graduated autonomy integrates with the existing Coup Counter and T14 starting conditions.

**Elegant.** The insight that "the game already starts on fire" eliminates the need for complex ignition mechanics. One fragmentation check rule produces all early-game conflict. One bishop appointment action produces the entire Church governance-expansion dynamic. One four-stage autonomy table replaces the binary coup. One card draw gives per-game variability. Each mechanism is one rule with cascading consequences through existing systems. No new resource tracks, no new stat sheets, no new resolution procedures.

---

## Implementation Priority

**1. Settlement-governance-as-ignition (immediate — engine_v4 Phase 1).** Verify that the settlement substrate correctly models starting controller misalignments. Run fragmentation checks from S1 on the 5 already-fractional provinces. This is the single most important finding from the session: the ignition system already exists in the data.

**2. Bishop appointment (engine_v4 Phase 2).** One new Church Domain Action. Requires: settlement Church building ≥ tier 2, no governor or governor Disposition ≥ +2. Ob 1. Effects flow through existing fragmentation/Accord systems.

**3. Graduated Löwenritter autonomy (engine_v4 Phase 2).** Replace binary coup. Four stages driven by Crown Stability, military action frequency, and Ehrenwall Disposition. Reversible at stages 1–3.

**4. Royal assassination fuse (engine_v4 Phase 4).** One Tensions Deck card with sub-roll. Fuse from S1, fires S8+. Three targets, three different games.

**5. Niflhel dissolution (engine_v4 Phase 2–4).** Replace faction with black markets (Phase 2 — settlement Order rule), intelligence brokers (Phase 4 — NPC placement), Thread exploitation sites (Phase 2 — location data).

**6. Tensions Deck remainder (engine_v4 Phase 5).** Remaining 5 cards written and integrated during smoke testing. Low priority — the game works without them.
