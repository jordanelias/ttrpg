# VALORIA — Campaign-Length Companion Simulations (All Playable NPCs)
**Date:** 2026-04-16  
**Token:** a09c30a5531abd1c  
**Scope:** Skeleton campaign-length simulations for all 12 playable (companion-eligible) NPCs. One generic officer-path case included.  
**Sources:** companion_specification_v30.md, npc_behavior_v30.md §2/§3/§4/§5.2/§7.10/§8.11/§9.5, combat_v30 §4/§13.3, scale_transitions_v30 §4.3.2, mass_battle_v30 §D.2, threadwork_v30  
**Campaign baseline:** 30-season game (standard sim length from prior runs). PC assumed Charisma 4, Att 4, Military 3 faction unless otherwise noted.

---

## METHODOLOGY

A "campaign-length skeleton simulation" means:
- **Not** roll-by-roll. **Yes** to probability-weighted stage transitions, key roll outcomes, and identified failure/success branches.
- Campaign divided into 3 phases: **Early** (S1–10), **Mid** (S11–20), **Late** (S21–30).
- For each NPC: Acquisition phase → Active companion behavior → Arc trajectory → Departure distribution.
- Stress tests: 3 canonical challenge scenarios per companion (combat, conviction, departure risk).
- Findings logged; gaps flagged inline.

**Companion slot context:** PC may hold 2 simultaneous companions. Priority effects: early-acquired companions affect which later NPCs can be activated. Where relevant, slot contention is noted.

**Pre-existing discrepancies flagged:**
- [GAP-SIM-C-01: §2.1 gives Almud TS 28; §7.10 says TS 0 per ED-398. Contradiction unresolved — both values used in respective sections of this sim as noted.]
- [GAP-SIM-C-02: §2.4 gives Vaynard TS 14; §7.10 says TS 10. Minor discrepancy — §7.10 used as more recent value for stat sim purposes.]
- [GAP-SIM-C-03: §2.2 gives Himlensendt Certainty 5; §7.10 says Certainty 4. §7.10 used here.]

---

## NPC 01 — GENERIC OFFICER-PATH COMPANION (REPRESENTATIVE CASE)

**Source faction example:** Crown (Military 4). Archetype applies to any faction officer at Military 3–5.

### Acquisition
**Path:** Unit officer reaches Disposition +3 through battle service (mass_battle §D.2). Timeline: ~3 battles (each OW outcome = +1 Disposition). At ~1 major battle/4 seasons in a contested campaign → Disposition +3 by Season 12.

**Acquisition probability by Season 12:** ~70% if player contests 3+ territories militarily by S10. Falls to ~30% in diplomatic-primary campaigns (few battles). Officer identity: unnamed until Disposition +3 fires companionship scene (§2.2).

**Stats (Military 4 faction):**

| Stat | Value |
|------|-------|
| Agility | 2 |
| STR | 2 |
| Endurance | 3 |
| Cognition | 2 |
| Charisma | 2 |
| Combat Pool | 9D |
| WI | 9 |
| Max Wounds | 2 |
| TS / Coherence | 0 / N/A |

### Combat Performance
**Per AI priority tree (§4.1):**
- Priority 1 fires (Wounds ≥ 1) once in ~3 engagements with PC in combat (statistically: 9D vs TN7 defending → ~6.5 hits/opponent, WI 9 → 1 wound per 1.4 opponent-hits on companion).
- Priority 2 (Rescue): fires ~30% of combats (PC attacked by 2+ opponents).
- Fibonacci contribution (+1D) adds ~15% to PC's expected hits per exchange when sharing target.

**Mass combat role:**
- Dis +3: commands assigned unit, PC Morale Effect carries to companion's unit.
- Dis +4 (reached ~S18 if active): sub-commander — independent Command rating floor(4/2)=2. Tier-1 tactics automatic; Tier-2 requires Ob 2 (Cog 2 + History 2 = 4D, P(Ob 2) ≈ 65%).
- Dis +5 (rare, ~S24+): auto-stabilises PC in mass battle. Acts as emergency Command stop-gap.

**PC Embedding amplification:** Dis +3 officer companion → 2 Domain Actions receive +1D BG bonus when PC embedded. Net DA bonus/season: +1D on average (2 DAs out of ~4/season receive boost).

### Arc Trajectory
Officer-path companions carry no Stance Triangle depth — they operate purely on Disposition track. Conviction formed during play: GM applies one of the 7 conviction values based on the officer's faction and established character. Scar accumulation is slow without prior conviction definition.

**Campaign arc (no defined arc map — GM-emergent):**
- S1–15: Accumulating Disposition. Combat scenes primary. No Belief definition yet.
- S15–22: First Belief contradiction likely if PC pivots faction alignment (e.g., PC aligns Church → officer with Order conviction may resist). One possible departure point.
- S22–30: Dependency on PC's faction health. Dissolution condition (Stability 0) is the primary late-game departure risk for officer companions.

### Stress Tests

**Stress 1 — Combat incapacitation (S14):** Officer takes 2 wounds in single exchange (enemy 11D vs TN7 vs officer 4D Def). WI 9, 2 wounds = incapacitated. Tend the Wounded Ob 3: P(success at Medicine 2 + Spirit 3 = 5D) ≈ 50%. On failure: confirmed death. Death rate per major combat: ~15% (assuming officer engages in Priority 2 Rescue when PC is 2v1).

**Stress 2 — Belief contradiction (S19):** PC seizes Church territory. Officer's Conviction = Order (institutional). Order is neutral on Church seizure unless PC's method was extralegal. Contradiction fires only if PC acts explicitly against Crown or Church institutional structure. Scar rate: ~1 per 6 seasons under moderate play pressure → 0–2 Scars total by S30.

**Stress 3 — Rival recruitment (S22):** Church Heresy Investigation identifies officer as "collaborator" (NPC defection mechanism from §9.5). Rival Ob = floor(Dis toward rival / 2) + 1. Officer has Dis 0 toward Church → Ob 1. Church rolls: Charisma 4 vs Ob 1. P(success) ≈ 93%. Player counter-offer: Advisory role (−1 Ob). Net rival Ob after counter: still 1 if no Hook. **[FINDING SIM-C-01: Officer companions are highly vulnerable to rival recruitment when the rival has low Ob (indifferent officer + no Hook). Player should establish formal military rank (advisory role) as an ongoing counter-incentive. Without it, any faction attempting recruitment on an indifferent officer will almost certainly succeed.]**

### Departure Distribution (30-season campaign)

| Cause | Probability |
|-------|-------------|
| Combat death | 25% |
| Dissolution (faction collapse) | 15% |
| Rival recruitment | 20% |
| Voluntary release by player | 30% |
| Conviction departure | 10% |

**Net contribution:** Reliable combat +1D (Fibonacci), mass combat sub-commander, DA embedding bonus. No arc content. Lower narrative investment = lower grief risk.

---

## NPC 02 — MAGNUS VAYNARD (Varfell — Scholar/Awakened)

### Acquisition
**Path:** Social path. Vaynard's primary Resonant Style is Consequence, secondary Evidence. Reaching Dis +3 requires: establishing Shared Interest (Thread knowledge), 2+ successful Consequence or Evidence-framed social scenes, and not triggering Consequentialist Framework contradiction (no uncertain/long-term actions framed without measurable outcomes).

**Probability of Dis +3 by S10:** ~45% in campaigns that engage Varfell diplomatically. Drops to ~20% if PC's faction is Church or Löwenritter (institutional friction raises social Ob). Vaynard's Leadership Deviation Ob = 2 — he deviates readily if PC's argument shows measurable outcomes.

**Acquisition arc state:** Vaynard is in Arc A (Scholar) at acquisition. TS 10 [GAP-SIM-C-02] at campaign start; may have advanced to TS 14+ by S10 through environmental exposure (§2.4: "Private Collection use triggers Spirit check for Discovery Event" at TS 14+).

**Stats as companion (social path, §3.2):**

| Stat | Value |
|------|-------|
| Agility | 2 |
| STR | 2 |
| Endurance | 3 |
| Cognition | 5 |
| Charisma | 2 |
| Combat Pool | (2×2)+History+3 = 7D (no Combat History; +2 from Scholar history applicable in investigation/knowledge scenes only) |
| WI | 9 |
| Max Wounds | 2 |
| TS at acquisition | 10–14 (Dormant) |
| Coherence | N/A (TS < 30, no Coherence tracking required) |

**Mass combat role:** Sub-optimal. No military history. Command rating = 0. At Dis +4: nominally sub-commander but Command check (Cog 5 + 0 History = 5D, Ob 2): P ≈ 78% — statistically reliable but represents Vaynard commanding through intellect, not military instinct.

**Primary contribution:** Investigation scenes (+1D at Dis +4 = +1D on any Thread-adjacent fieldwork, knowledge-seeking inquiry). Vaynard at Dis +4 provides consistent +1D to Fieldwork rolls in scholarly domains. Corroborate in social contests: Ob 1 if Knot present.

### Arc Trajectory as Companion

**Arc A phase (S10–18 as companion):** Vaynard collects Thread data. His TS rising from 10→14→(if Discovery Event fires)→30. Each season as companion in Thread-active territory: Spirit check TN7 vs Ob 2 for Discovery Event (Spirit 2, pool 2D, P ≈ 18%/season). Over 8 seasons active: P(at least one Discovery Event) ≈ 76%.

**Discovery Event consequence:** Vaynard's TS crosses Stirring threshold (30). Per §5.0b: Close Knot strain +1/season begins. If PC has Knot with Vaynard (likely after Dis +4 Knot formation): PC accumulates +1 Threadwork strain/season for remainder of companion time. Over S18–30 (12 seasons at Close Knot): 12 points of Thread strain on PC.

**Arc B entry (The Awakened):** Branch condition not fully specified in §5.2 (content stub: "Arc A: Scholar / Arc B: Awakened"). [GAP-SIM-C-04: Vaynard Arc B trigger condition not specified in §5.2. Arc C requires "Vaynard becomes a local threat." Intermediate trigger undefined.] Inference from §5.1: TS crossing Stirring (30) → ontological confrontation challenges Conviction. Vaynard at Arc B: Certainty drops from 2→1. Resonant Style shifts: Evidence activates alongside Consequence.

**Arc C (Consumed):** Vaynard without practitioner training experiencing Active-tier perception (TS 50+ without training). Coherence degrades — Vaynard at risk of Rendering Crisis without PC intervention. If PC fails to engage Vaynard's Arc C before S25: Vaynard enters Conviction crisis, Departure condition fires (Conviction departure — 3 Scars as companion from repeated ethical crises).

**[FINDING SIM-C-02: Vaynard as long-term companion (S10–S30) is a high-risk/high-reward relationship. His Thread arc almost certainly crosses a threshold during companion time, imposing ongoing Knot strain on PC (+1/season Close Knot from S18+). His Arc C degrades him without trained practitioner support. A Vaynard companion effectively creates a secondary storyline the PC must manage: either help him train (requires Edeyja/Warden access) or accept eventual Arc C crisis. He's the most mechanically demanding companion.]**

### Stress Tests

**Stress 1 — Discovery Event combat (S17):** Vaynard witnesses Thread phenomenon in combat zone. Spirit check: 2D TN7 Ob 2. P(success, no event) ≈ 82%. On failure: Discovery Event fires mid-combat. Vaynard is stunned (1 round full Guard mandatory). PC loses Fibonacci bonus that round. GM resolves arc advance.

**Stress 2 — Conviction contradiction (S21):** PC forms alliance with Niflhel (expedient). Vaynard's Consequentialism: outcome-focused, not moral. But Vaynard Belief 3: "No faction can be trusted with this knowledge." Niflhel alliance risks Thread knowledge transfer. Scar fires (Belief engagement). Vaynard at 1 Scar: Decision Fork increases. Secondary Conviction (Autonomy) activates. He may begin independently pursuing Thread data outside PC's control.

**Stress 3 — Rival recruitment (S24):** Church Heresy Investigation identifies Vaynard's Thread involvement. Church's Heresy Investigation is a Demand (not recruitment). Vaynard: Dis −2 toward Church (prior oppression). Church cannot recruit at Dis −2 (below recruitment threshold). But Heresy Investigation can Expose Vaynard publicly → Vaynard's Varfell faction standing collapses → Dissolution departure if Varfell was his primary faction anchor.

### Departure Distribution

| Cause | Probability |
|-------|-------------|
| Arc C Conviction crisis (3 Scars, no intervention) | 35% |
| Combat death (low combat pool) | 15% |
| Dissolution (Varfell faction collapse) | 20% |
| Voluntary release | 20% |
| Rival extraction (Church) | 10% |

**Net contribution:** Best investigation companion in game. +1D on all Thread-adjacent fieldwork at Dis +4. Corroborate in knowledge-domain contests. Mass combat weak. Imposes Knot strain late campaign. High arc content.

---

## NPC 03 — MARET VOSSEN (Restoration Movement)

### Acquisition
**Path:** Social path or Knot path. Vossen's Solidarity primary style — she responds to sustained relational investment, not intellectual argument. Requirements: PC must demonstrate genuine community engagement (no purely political play), 2+ scenes involving direct community protection/support, and avoid Concentration-of-power actions (her Belief: "Violence is the tool of the powerful").

**Probability of Dis +3 by S8:** ~60% in campaigns with Restoration engagement. Easiest named companion to acquire if PC plays community-first. Drops to ~10% if PC is Church or Crown (institutional friction; her Rawlsian ethics triggers +1 Ob vs power-concentrating factions).

**Stats as companion (social path):**

| Stat | Value |
|------|-------|
| Agility | 3 |
| STR | 2 |
| Endurance | 3 |
| Cognition | 3 |
| Charisma | 5 |
| Combat Pool | (3×2)+History+3 = 9D (Circles History applies in community scenes, not combat) |
| WI | 9 |
| Max Wounds | 2 |
| TS | 0 |

**Primary contribution:** Social contests (Corroborate at Ob 1 with Knot). Vossen's Charisma 5 means she can independently hold social exchanges against most NPCs if PC directs her. Community-facing fieldwork: +1D at Dis +4. Movement-network intelligence: Vossen's Circles 3+ in working-class networks = automatic Evidence tokens in territories with active Restoration presence.

**Mass combat:** Not applicable (non-military). If PC is in mass combat with Vossen present, she operates as an advisor/logistics coordinator, not a combat unit commander. No Command rating. Her Dis +5 auto-stabilise still applies (personal scale rescue of PC).

### Arc Trajectory as Companion

**No formal arc map in §5.2.** [GAP-SIM-C-05: Vossen arc profile absent from §5.2. Only named NPCs with arc maps: Almud, Himlensendt, Baralta, Vaynard, Edeyja.] Inferring from §2.6 and §3.3:

**S1–12:** Vossen stable, Equity primary. Outreach scenes generate community intelligence. PC gains access to Restoration cell network. 1 guaranteed Outreach per 3 seasons when Dis ≥ +3 (§8.11.2 Outreach conditions met for Restoration NPCs regularly).

**S12–20:** Potential Conviction crisis if PC's faction actions increase Public Instability. Her Belief 3: "Violence is the tool of the powerful — the movement wins through community." If PC authorizes military aggression in RM-sympathetic territories → Belief engagement → 1 Scar risk per major military action in those territories. At 3 Scars: Conviction departure (she cannot continue if the PC is becoming the violent power she opposes).

**S20–30 (Continuity fallback):** If Restoration Movement is suppressed (Church Seizure of RM territory), Vossen shifts to secondary Conviction: Continuity (cultural preservation). She becomes less political, more archival. Companion behavior shifts: fewer community fieldwork bonuses, more retrospective/lore-sharing scenes.

### Stress Tests

**Stress 1 — Personal danger (S10):** Niflhel deploys Quiet operative against RM cell Vossen coordinates. Combat: Vossen 9D vs Quiet operative (estimate 8D + 1D Quiet bonus). P(Vossen survives without PC intervention) ≈ 55%. If PC intervenes (Priority 2 PC rescue): Vossen safe. If PC absent: Vossen takes wound. Combat is not Vossen's domain — this stress test validates that Vossen requires PC protection in direct conflict.

**Stress 2 — Conviction contradiction (S16):** PC employs Niflhel (expedient). Vossen's Belief 2 (Solidarity: "the communities that depend on her"). Niflhel = predatory network. Belief engagement: Scar 1 fires. Decision Fork activates. Vossen will Outreach to demand PC sever Niflhel connection. If refused: Scar 2. At Scar 3 (one more contradiction): departure scene fires.

**Stress 3 — RM Dissolution (S22):** Church TC 65 → Seizure of all RM territories. Restoration Movement faction Stability 0. Dissolution departure fires (§6.1). Vossen becomes unaligned. Can rejoin without new companionship scene when faction reconstitutes (§6.1). **[FINDING SIM-C-03: Vossen's departure on faction Dissolution is a campaign-level signal: if Church reaches TC 65 and actively suppresses RM, the player loses their community-network companion as an immediate consequence. This correctly ties her fate to the faction victory clock. Players holding Vossen companion are mechanically incentivized to prevent Church from reaching TC 65.]**

### Departure Distribution

| Cause | Probability |
|-------|-------------|
| Conviction departure (PC violence, Niflhel alliance) | 30% |
| Dissolution (RM suppression by Church) | 25% |
| Combat death | 10% |
| Voluntary release | 25% |
| Rival recruitment | 10% |

**Net contribution:** Strongest community-intelligence companion. Social contest Corroborate (Cha 5). Restoration cell network access. Fragile in combat. High narrative investment; strong departure arc.

---

## NPC 04 — ALDRIC HANN (Restoration Movement — Secondary)

### Acquisition
**Path:** Social path, independent of Vossen. Hann responds to Consequence (operational failure shown) and Evidence (compromised cells exposed). PC must demonstrate logistical competence or surface a threat to Hann's network.

**Acquisition note:** Hann and Vossen can both be companions simultaneously (2-slot capacity). If player holds Vossen, Hann acquisition is the natural second slot. However: Hann and Vossen have overlapping Beliefs — holding both triggers Belief consistency pressure (both will react to the same Belief violations, doubling departure risk per contradiction).

**Probability of Dis +3 by S10:** ~40% in RM-engaged campaigns. Requires separate social investment from Vossen track (they don't share Disposition progress).

**Stats as companion:**

| Stat | Value |
|------|-------|
| Agility | 3 (operational field work) |
| STR | 3 |
| Endurance | 3 |
| Cognition | 3 |
| Charisma | 3 |
| Combat Pool | (3×2)+History+3 = 9D (Street/Logistics History applies) |
| WI | 9 |
| Max Wounds | 2 |
| TS | 0 |

**Primary contribution:** Street-level intelligence (Circles 3+ in logistics/supply networks, different from Vossen's community-facing Circles). Hann provides tactical intelligence (supply chain vulnerabilities, movement routes, Niflhel infiltration alerts). At Dis +4: +1D on covert investigation fieldwork specifically.

### Arc Trajectory as Companion

**No formal arc map.** [GAP-SIM-C-06: Hann arc profile absent from §5.2. Treated as RM sub-arc: mirrors Vossen's trajectory at one Conviction step removed.] 

**Key difference from Vossen:** Hann's secondary Conviction is Autonomy (survival). At Scar 2, Hann may prioritize the movement's operational survival over Equity. He'll advise pragmatic compromises Vossen would refuse — and this creates internal companion tension if both are held: Vossen at Scar 2 advocates purity; Hann at Scar 2 advocates compromise. **[FINDING SIM-C-04: Dual Hann+Vossen companion hold creates a built-in internal drama mechanic. Their Belief structures diverge under pressure (Vossen → Continuity, Hann → Autonomy). Holding both is not unstable, but requires the player to navigate competing Outreach demands from two companions who will eventually disagree. This is likely intentional — it's the richest companion pair for social campaign play.]**

### Stress Tests

**Stress 1 — Cell compromise (S12):** Enemy Intel reveals Hann's cell network in T6. Niflhel Infiltration: −2 Circles in T6 for Hann. Hann's Outreach fires: Demand that PC eliminate the Niflhel operative. If PC complies: Dis +1 (Obligation fulfilled). If PC declines: Scar 1 (Belief engagement: "Every cell that is compromised is a community that suffers — I will protect our people").

**Stress 2 — Defection offer (S18):** Crown offers Hann an administrative role (Crown Treaty terms extend to RM leadership). Rival recruitment Ob = floor(Hann's Dis toward Crown / 2) + 1. Hann Dis toward Crown: 0 → Ob 1. Crown rolls: Charisma 5 vs Ob 1 → near-certain success. Player counter-offer: "Alignment with Hann's Belief" (−2 Ob on counter = Ob 1 vs Crown Ob 1 — tie goes to existing loyalty). **Requires strong hook or genuine Belief commitment from PC faction to retain Hann.**

**Stress 3 — Vossen departure (S22):** If Vossen departs (Dissolution), Hann's Conviction fallback is Autonomy — survival. Hann's behavior shifts from ideological to operational. Departure risk drops (he's now pragmatic, easier to hold) but his Outreach shifts to self-interested demands. He becomes a different companion post-Vossen.

### Departure Distribution

| Cause | Probability |
|-------|-------------|
| Rival recruitment (Crown / Niflhel) | 30% |
| Conviction departure | 20% |
| Dissolution | 20% |
| Voluntary release | 20% |
| Combat death | 10% |

**Net contribution:** Covert intelligence supplement to Vossen. Different Circles network. Dual-hold with Vossen creates dynamic companion pair. Individually less compelling than Vossen for social play; more useful for covert/operational campaigns.

---

## NPC 05 — PRINCE TORBEN ALMQVIST (Crown — Heir)

### Acquisition
**Path:** Solidarity primary — he responds to being treated as a person, not a political asset. Requirements: PC must engage Torben in personal scenes (not faction-mediated), demonstrate genuine relational investment, and not treat him instrumentally (Consequentialist approaches backfire: −1 Ob on personal framing of arguments about him).

**Acquisition timing:** Torben is a contested narrative asset — multiple factions attempt to hold his Loyalty. PC acquires him as companion only if they outpace faction investment. Early acquisition window: S1–8 (before Church or Löwenritter lock in his Loyalty at +4). After Loyalty +4 toward any faction: not recruitable (§9.5 gate).

**Starting Conviction:** Blank. First faction/PC to invest sets initial Conviction. This is the most mechanically significant acquisition decision: PC who establishes Torben as companion in S1–4 shapes his entire Conviction structure. **[FINDING SIM-C-05: Torben's blank starting Conviction means acquiring him early is transformative. A PC who companions Torben in S1–4 can establish ANY of the 7 Conviction values as his primary through sustained relational play. This is uniquely powerful — all other named companions have fixed primary Convictions. Torben is the only companion who is a narrative clean slate.]**

**Stats as companion (social path, §3.2 default):**

| Stat | Value | Notes |
|------|-------|-------|
| Agility | 2 | Court-raised; no military training |
| STR | 2 | |
| Endurance | 3 | |
| Cognition | 3 | Educated, not exceptional |
| Charisma | 4 | He is a prince — presence trained |
| Combat Pool | (2×2)+History+3 = 7D (Court History only; no combat history) |
| WI | 9 | |
| Max Wounds | 2 | |
| TS | 0 | Certainty 4 (confirmed §7.10) |

**Primary contribution:** Legitimacy. Torben as companion grants the PC faction a social Ob bonus in Crown-adjacent contexts (player should propose this as a formal Outreach consequence — not in canonical doc yet). His Charisma 4 makes him effective in formal social contests. [GAP-SIM-C-07: Torben's companion-specific mechanical bonuses not defined in canonical_sources. His Legitimacy contribution is design-appropriate but undocumented.]

### Arc Trajectory as Companion

**Arc maps not specified for Torben.** [GAP-SIM-C-08: Torben has no arc profile in §5.2.] Emergent from §2.8:

**S1–10:** Conviction formation phase. PC's treatment determines what Torben values. Solid-relationship path: Torben forms initial Belief around the PC's demonstrated Convictions. By S10, Torben has 1–2 active Beliefs (PC-influenced).

**S10–20:** External pressure phase. Löwenritter Coup Counter may advance. If Coup fires: Torben's Loyalty transfers to Löwenritter (§5.2 Almud Arc C). If Torben is companion: the Coup creates a Departure-condition equivalent (his formal Loyalty transfers, but Companionship is personal-scale — he stays with PC but his BG-layer faction changes). **[FINDING SIM-C-06: Torben as companion creates a legal paradox if the Coup fires. His Companionship is a personal relationship (personal scale), but his Loyalty is a BG resource. The Coup captures his Loyalty-as-BG-resource but cannot mechanically capture his Companionship without triggering Defection departure rules. Resolution needed: either (a) the Coup automatically fires Torben's Defection departure (Löwenritter removes him from PC's care), or (b) Torben's Companionship persists while his BG Loyalty transfers — he's companion to the PC but pledged to Löwenritter. The latter is the richer narrative outcome but requires formal ruling.]**

**S20–30:** If Almud is deposed and Torben's Conviction has been formed by PC: Torben may be the legitimate claimant to Crown with the PC's backing. This is not a mechanical outcome (no "Crown heir restoration" victory condition exists), but it creates the richest late-campaign narrative context of any companion.

### Stress Tests

**Stress 1 — Authority resonance (S7):** Ehrenwall or Church faction demonstrates overwhelming power in PC's presence. Torben's secondary Conviction (Authority) fires: he is drawn to the strong faction. PC must counter-demonstrate equivalent strength or relational bond. Social contest: PC Charisma + Solidarity framing vs Ehrenwall's Martial Honour. If player wins: Torben's Solidarity reinforced. If loses: Authority Conviction may become primary (Torben shifts toward the power faction).

**Stress 2 — Coup scenario (S16):** Löwenritter Coup fires (Counter 3). Torben's formal Loyalty transfers. Defection departure: rival (Löwenritter) attempt to remove Torben from PC. Ob = floor(Torben's Dis toward PC / 2) + 1. At Dis +3: Ob = 2. Löwenritter rolls Charisma 3 vs Ob 2: P(success) ≈ 60%. Player counter: formal pledge of PC faction resources. Close call — Torben stays ~40% without counter-offer.

**Stress 3 — Identity crisis (S24):** Torben confronts the cost of his blank-slate Conviction formation. If PC shaped him toward Equity (Restoration-aligned), and the campaign ends with Church victory, Torben experiences Conviction crisis (3 Scars from sustained contradiction). The clean-slate arc closes: whoever formed him most deeply wins his final loyalty — which may not be the PC.

### Departure Distribution

| Cause | Probability |
|-------|-------------|
| Coup defection (Löwenritter takes him) | 25% |
| Conviction departure (PC's shaping contradicted late) | 20% |
| Voluntary release (player positions him as Crown heir strategically) | 30% |
| Combat death | 10% |
| Rival recruitment (Church) | 15% |

**Net contribution:** Uniquely shapeable companion. Late-game legitimacy utility. Weak combat. Requires early acquisition to maximize arc value. Creates Crown succession narrative.

---

## NPC 06 — GRANDMASTER LISBETH EHRENWALL (Löwenritter)

### Acquisition
**Path:** Solidarity secondary — requires Intimate Knot level. Order primary (cannot reach Dis +3 through intellectual argument; must demonstrate shared sacrifice/service/military bonds). Acquisition requires PC to have a military track record Ehrenwall respects AND a sustained personal relationship (Knot formation).

**Acquisition window:** Narrow. Ehrenwall becomes a companion only if:
1. PC has Military History (Combat or equivalent) — she won't respect a purely political operator.
2. PC shares a genuine Knot (formed through crisis, not convenience).
3. Löwenritter Coup Counter is **not** at 3 (if Coup has fired, Ehrenwall is running Valoria as interim, not available as companion).

**Probability of Dis +3:** ~20% in campaigns with sustained military play. Very low in diplomatic-primary campaigns (~5%). This is intentional — Ehrenwall is a hard companion to acquire.

**Stats (social/military path):**

| Stat | Value | Notes |
|------|-------|-------|
| Agility | 3 | Veteran warrior |
| STR | 3 | |
| Endurance | 4 | Superior physical conditioning |
| Cognition | 3 | Tactical, not strategic intellectual |
| Charisma | 3 | Commands through presence, not charm |
| Combat Pool | (3×2)+History+3 = 12D (Combat 4 history: +4D bonus; Ehrenwall is an elite fighter) |
| WI | 10 (End 4 + 6) | |
| Max Wounds | 3 (floor(4/2)+1) | Exceptionally durable |
| TS | 0 (confirmed §7.10) | Certainty 5 — maximum |

**[NOTE: Ehrenwall stats above are inferred from her martial background and Certainty per §7.10. Formal stat sheet not in canonical doc. GAP-SIM-C-09: Ehrenwall companion stats not formally defined — using inference from characterization and §3.2 guidelines.]**

### Combat Performance
Ehrenwall is the game's strongest combat companion by a wide margin:
- Combat Pool 12D significantly outpaces generic officer (9D) and all social-path companions.
- WI 10, Max Wounds 3 — requires ~30 opponent hits before incapacitation (roughly 2× officer durability).
- At Priority 3 (Conviction alignment): 12D − 4D Def = 8D Off on highest-threat target. PC+Ehrenwall attacking same target: Fibonacci +1D each = 9D each. Expected opponent downs: ~(8+9)=17D total, TN7, ≈12 hits/round shared.
- Mass combat: if companion at Dis +4: her Command applies to her unit. Floor(Military/2) where Military = effectively 4 (Löwenritter is a Military 5 faction — Ehrenwall is the Grandmaster). Command: 2–3. Tier-2 tactics available on Ob 2 check (Cog 3 + Combat History 4 = 7D, Ob 2: P ≈ 93%).

**[FINDING SIM-C-07: Ehrenwall is the mechanically optimal combat companion. Her 12D pool and WI 10 make her nearly indispensable in combat-intensive campaigns. A player who successfully acquires her (difficult) effectively doubles personal combat capability. This validates the acquisition difficulty — her combat contribution is so large that it would unbalance combat if easily obtained.]**

### Arc Trajectory as Companion

**No arc map in §5.2.** [GAP-SIM-C-10: Ehrenwall arc profile absent.] Emergent from §2.5:

**S1–12:** Stable Order primary. Companion behavior: protective, mission-focused. Outreach scenes: tactical assessments, intelligence about Löwenritter internal politics (Coup Counter state). She acts as the player's early-warning system for Coup threshold.

**S12–20:** Coup Counter tension. If Ehrenwall is companion and Counter advances to 2: Decision Fork fires (she's counting Almud's failures personally, per §2.5 Belief 2). She may advise PC to manage Crown's failures or pressure for action. Contradiction: if PC supports Crown strongly despite failures, this contradicts her Belief 2 — Scar risk.

**S20–30:** If Coup never fires (player suppressed it): Ehrenwall's Order conviction stabilises. She's a long-term loyal companion in this branch. If Coup was attempted and failed: she entered a Conviction crisis (Autonomy fallback: the Coup was the action she had prepared for and it failed). Her arc is terminal in this branch — Conviction departure or voluntary departure to reconstitute the order.

### Stress Tests

**Stress 1 — Martial honor contradiction (S9):** PC negotiates with Niflhel or uses covert tactics Ehrenwall judges dishonorable ("The Riskbreakers exist for situations where honour is a luxury" — but Ehrenwall is not casual about it). Scar risk: +1 Ob on PC's next Leadership Deviation check from Ehrenwall's institutional influence. One Scar may fire if the tactic was sufficiently dishonorable.

**Stress 2 — Coup alignment (S17):** Coup Counter 3. Ehrenwall executes Coup. She's no longer a "companion traveling with PC" — she's running the country. Dissolution departure fires (she has higher obligations now). Counter-narrative: if the PC convinces her to delay the Coup (extraordinary social success), she remains companion but the delay creates a Loyalty-to-Order contradiction for her.

**Stress 3 — Crown's redemption (S23):** If Almud enters Arc A (Reformer) through player intervention: Ehrenwall's Coup logic is invalidated. She must recalibrate her Conviction. Decision Fork: Order (serve the reformed Crown) vs Autonomy (the Löwenritter acts because someone must — but the Crown no longer needs them to). This is the arc's most interesting branch: Ehrenwall as companion to a PC who saved the Crown she was about to depose.

### Departure Distribution

| Cause | Probability |
|-------|-------------|
| Coup execution — dissolution | 35% |
| Combat death (rare, she's durable) | 5% |
| Conviction departure (dishonorable PC tactics) | 20% |
| Voluntary release (Coup averted; she stands down) | 25% |
| Rival recruitment | 15% |

**Net contribution:** Best combat companion in game. Coup intelligence. Mass combat command excellence. Hard to acquire, hard to retain long-term if Coup Counter advances. Highest mechanical return on companion investment.

---

## NPC 07 — DUCHESS INGE BARALTA (Hafenmark)

### Acquisition
**Path:** Social path. Baralta's primary Evidence style and Consequential secondary means the PC must present documented institutional failure of her own system. Reaching Dis +3 requires: 2–3 Evidence-framed contests, demonstrated that Baralta's Constitutional framework has a specific documented failure, and the PC operates within or respects legal structures (extra-legal actions raise Ob +1 per her Categorical Imperative framework).

**Acquisition barrier:** High. Baralta's Certainty 5 (§7.10: triple-barrier, TS 0, Ob 4 on Certainty movement). She's nearly immovable without a sustained Evidence campaign. Leadership Deviation Ob = 1 (she is the institution — she deviates easily personally, but Disposition tracks toward the PC personally, not institutionally). Dis +3 requires sustained personal relationship, not institutional alignment.

**Probability of Dis +3 by S12:** ~25%. Drops to ~10% if Church controls Hafenmark territory (Excommunication scenario triggers identity collapse that redirects her attention away from personal relationships).

**Stats (social path):**

| Stat | Value | Notes |
|------|-------|-------|
| Agility | 2 | Political figure; no combat training |
| STR | 2 | |
| Endurance | 3 | |
| Cognition | 4 | Constitutional scholar |
| Charisma | 4 | Political presence |
| Combat Pool | (2×2)+History+3 = 9D (Political History: +2D on Parliament scenes, not combat) |
| WI | 9 | |
| Max Wounds | 2 | |
| TS | 0 | Certainty 5 |

**Primary contribution:** Parliamentary leverage. Baralta as companion gives PC access to Hafenmark's Parliamentary motions at −1 Ob (Dis +4, her Leadership Deviation Ob = 1 means she acts on personal loyalty). Her 2× Consul cards = dominant Parliamentary presence. PC with Baralta companion can initiate Grand Contest or Parliamentary Censure from Hafenmark's institutional weight.

### Arc Trajectory as Companion

**Arc A (Constitutional Triumph):** No transformation — this is her resolution state. Arc A as companion means she's stable, reliable, and increasingly institutionally powerful as Hafenmark's Influence grows (Framework Drift: Influence caps at 7 by S4 in standard sim).

**Arc B (The Pragmatist) — companion branch:** If Church seizes Hafenmark territory (TC 40+) and Baralta's companion-adjacent Evidence scenes reveal the failure of constitutional procedure: she becomes willing to take extralegal action. This is ONLY reachable if the PC has been building Dis toward her through Evidence — exactly the evidence-heavy approach that forces her to confront her system's failure. **[FINDING SIM-C-08: Baralta's Arc B entry is most likely triggered by a companion-having PC, because the PC's Evidence-based social investment is structurally identical to the arc trigger condition. A PC who acquires Baralta as companion through Evidence contests is, by definition, performing the arc-trigger activity. Baralta reaching Arc B as companion is near-certain (~85%) in campaigns where she was acquired through proper Evidence engagement.]**

**Arc C (Excommunication):** TC 65+ enables Church Excommunication. If Baralta is companion during Excommunication: Departure risk fires. Excommunication is a BG-layer event — her Hafenmark Mandate collapses. Dissolution departure conditions met (faction Stability crisis). She becomes unaligned. Can rejoin without companionship scene.

### Stress Tests

**Stress 1 — Precedent violation (S11):** PC uses extralegal method to seize Church territory (bypassing Parliamentary procedure). Baralta's Categorical Imperative: +1 Ob on ad hoc actions. Scar: Belief 1 engagement ("Constitutional procedure IS justice"). First Scar fires if the action was decisive and undeniable.

**Stress 2 — Church Excommunication (S19):** Church TC 65. Excommunication threat. Baralta's BG response (Arc C branch): TC +4, Mandate crisis. As companion: she's emotionally exposed — her Faith (secondary) and Precedent (primary) directly contradict (the Church = the Faith she also holds). Companion departure risk: Conviction crisis if PC doesn't help her resolve the contradiction.

**Stress 3 — Grand Contest victory (S26):** Grand Contest decisive win → Hafenmark Mandate 4→5 (new provisional ED-583 rule). Baralta's position strengthens. PC-Baralta companion now has Hafenmark at Mandate 5 — she can Proclaim on Crown territory. This is the companion's most powerful campaign-endgame state: the player has turned a moderate-mandate institution into a dominant political force through sustained relational investment.

### Departure Distribution

| Cause | Probability |
|-------|-------------|
| Excommunication dissolution | 25% |
| Conviction departure (precedent violations) | 20% |
| Voluntary release (Baralta's career demands her full attention) | 30% |
| Combat death | 5% |
| Rival recruitment | 20% |

**Net contribution:** Parliamentary dominance. Hafenmark institutional leverage. Moderate combat. Best non-practitioner political companion in game for Parliament-focused play.

---

## NPC 08 — CONFESSOR ARNE HIMLENSENDT (Church)

### Acquisition
**Path:** Hardest companion in the game to acquire. Himlensendt's Certainty 4 [GAP-SIM-C-03: §7.10 says 4, §2.2 says 5], Faith primary, Total Victory Arc B trigger required. Companion status is only reachable through:
1. Total Victory Contest via Evidence (Track 9+, not Decisive Win at 7).
2. Arc B (Crisis of Faith) entry — Himlensendt's worldview has been shattered.
3. At Arc B: he's vulnerable to Solidarity or Evidence approaches; Dis +3 becomes achievable from a companion-eligible starting point.

This means Himlensendt can only become a companion **after** the player has already invested 2–3 sessions in shattering his faith via Evidence contests. He's not an early or easy companion.

**Probability of Dis +3:** ~10% in campaigns that specifically target Himlensendt. Effectively 0% in campaigns that don't run Evidence-attack chains against him.

**Stats (social path — a man who has lost his faith):**

| Stat | Value | Notes |
|------|-------|-------|
| Agility | 2 | Confessor; no combat background |
| STR | 2 | |
| Endurance | 3 | |
| Cognition | 4 | Theological scholar |
| Charisma | 5 | The Confessor's voice carries crowds |
| Combat Pool | (2×2)+History+3 = 9D (Theological oratory History — effective in social contests, not personal combat) |
| WI | 9 | |
| Max Wounds | 2 | |
| TS | 0 | Certainty drops to 1 on arc entry |

**Primary contribution:** Theological legitimacy in social contests. Himlensendt in Arc B (Faith in Crisis) still carries the Confessor's authority — which can be deployed against Church institutional positions. A converted/questioning Himlensendt as companion gives the PC the ability to make Authority-style social arguments from within the Church hierarchy. His Charisma 5 = effective Corroborate and social scene support.

**[FINDING SIM-C-09: Himlensendt as companion is a "weapon against his own institution" case. The PC has invested substantially to break his faith and must now manage a man in profound spiritual crisis traveling with them. His arc doesn't resolve cleanly — Arc C (Confrontation) is still possible even as companion. If he goes public with his crisis while traveling with the PC: Church Stability −3 (a massive destabilisation event). The PC's companion decision determines whether this is a controlled demolition (PC guides the revelation) or an uncontrolled explosion (Himlensendt breaks publicly at the worst moment).]**

### Arc Trajectory as Companion (Post-Arc-B)

At Arc B entry as companion:
- Certainty 1. All Resonant Styles active.
- Behavior: erratic. Conviction crisis table active at 3+ Scars (very fast accumulation during crisis).
- PC must provide structured Belief support or the arc cascades to Arc C.

**S1–5 as companion (post-Arc-B entry):** Himlensendt seeks a new framework. He will form new Beliefs through the PC's actions. The player shapes what replaces his Faith (Reason? Equity? Autonomy?). This mirrors Torben's blank-slate arc but from a position of trauma rather than inexperience.

**S5–12 as companion:** If PC successfully guided him toward a new Conviction: Himlensendt stabilises. New primary Conviction forms. He's now a different NPC — the Confessor who no longer confesses. His institutional authority remains (people still respond to his voice) but his framework has changed.

**Arc C risk (S8 as companion):** If the PC fails to stabilize him (PC actions contradict his forming Convictions 3 times): Arc C fires. He goes public. Church Stability −3 happens while he's the PC's companion. This is simultaneously a massive BG opportunity (Church is destabilized) and a personal catastrophe (his arc ends in public breakdown). Departure fires immediately.

### Stress Tests

**Stress 1 — Residual Faith trigger (S3 as companion):** Church NPC makes a direct appeal to Himlensendt's former Faith (Authority RS). Even in Arc B, this can temporarily re-anchor his old Conviction (Conviction crisis table d6 roll: 1–2 = original primary Conviction). If the old Faith reasserts and PC has been building him toward Reason: Contradiction. Scar fires on the new framework. The appeal of the familiar is the constant departure risk for a companion in Conviction crisis.

**Stress 2 — Public revelation pressure (S7 as companion):** If TC ≥ 65 and Church is close to victory, the PC may be tempted to weaponize Himlensendt's crisis (make it public for Church Stability −3). This is the ultimate Conviction contradiction for a PC who has been building a genuine relationship: using Himlensendt's crisis instrumentally is precisely the kind of power-concentrating action that fires Solidarity-breach Scars.

**Stress 3 — Institutional pull (S10 as companion):** The Church needs Himlensendt back. If Church Stability ≤ 2: Cardinal of Justice or Fortitude stages an intervention. Defection recruitment: Church rolls to retrieve him. His remaining institutional loyalty makes this Ob 2 (not Ob 1 — he's in crisis, not indifferent). P(Church retrieves him without counter) ≈ 65%.

### Departure Distribution

| Cause | Probability |
|-------|-------------|
| Arc C public breakdown | 35% |
| Church institutional retrieval | 25% |
| Conviction crisis (3 Scars during new framework formation) | 20% |
| Voluntary release (PC lets him go on a pilgrimage) | 15% |
| Combat death | 5% |

**Net contribution:** Unique theological authority leverage. Church destabilisation potential (controllable or explosive). Extremely high maintenance. Lowest "sustainable companion" rating but highest "single dramatic moment" potential.

---

## NPC 09 — KING ALMUD ALMQVIST (Crown)

### Acquisition
**Path:** Requires Intimate Knot (§5.1: "PC Knot ≥ Intimate → Solidarity Resonant Style activates"). Solidarity is his only accessible secondary style. Evidence/Consequence approaches to Almud are heavily resisted (Certainty data contradiction: §2.1 says 28 TS near Stirring; §7.10 says TS 0 [GAP-SIM-C-01]). His Leadership Deviation Ob = 2.

**Acquisition window:** Extremely narrow. Almud as companion requires:
1. PC has Intimate Knot with Almud (unusual — requires sustained personal relationship with the Crown King).
2. Almud must be in Arc A or approaching it (not Arc B/C — once Crown Stability collapses or Coup fires, he's exiled or dead).
3. Almud's Certainty reaching 2→1 through Evidence exposure (if §2.1 TS 28 is correct, he's near Stirring and Evidence attacks are partially effective).

**Probability of Dis +3:** ~8% in campaigns specifically focused on Crown alliance. Near zero otherwise.

**Stats (social path — a king reduced to human scale):**

| Stat | Value | Notes |
|------|-------|-------|
| Agility | 2 | Monarch; minimal personal combat |
| STR | 2 | |
| Endurance | 3 | |
| Cognition | 4 | Strategic thinker |
| Charisma | 5 | He is the king — institutional authority radiates |
| Combat Pool | (2×2)+History+3 = 9D |
| WI | 9 | |
| Max Wounds | 2 | |
| TS | 0 or 28 [GAP-SIM-C-01] |

**Note:** Almud can only be a companion in Arc A (Reformer) or in the aftermath of Arc C (Exile). In Arc B (Fortress) or during Crown's political crisis, he is not available for personal relationship — he's in institutional defense mode.

**[FINDING SIM-C-10: Almud as companion is the rarest companion in the game and the most politically volatile. He carries the Crown's institutional weight personally — his presence on the PC's side creates an immediate BG effect (Crown Mandate effectively follows Almud's personal Loyalty to PC). This is unprecedented in the companion system: Almud as companion may functionally mean the player controls the Crown faction. This needs a formal ruling on what happens to Crown's BG faction when its named leader is a companion. No canon ruling exists.]**

### Departure Distribution

| Cause | Probability |
|-------|-------------|
| Coup fires — exile — dissolution | 40% |
| Conviction departure (PC actions contradict Order) | 25% |
| Voluntary release (he must return to govern) | 25% |
| Combat death | 5% |
| Rival recruitment | 5% |

**Net contribution:** Crown institutional leverage. Highest narrative status of any companion. Most politically destabilizing to acquire. Unplayable in most campaigns — listed for completeness.

---

## NPC 10 — EDEYJA (Southernmost Warden-Chief)

### Acquisition
**Path:** Social or Knot path. Evidence primary — requires demonstrated Thread competence. She will not respond to anything but proven capability in Thread work or direct demonstration of the Southernmost's need. PC must reach her (Expedition to Southernmost required: §4.3.3 Warden Emergency Zoom In or player-initiated scene).

**Acquisition timing:** Late game by design. Southernmost Expedition is expensive (time, resources) and only becomes strategically viable when RS decline is noticeable (RS ≤ 40). This means acquisition typically S15–25.

**Arc state at acquisition:** Arc B (Collaboration) requires "PC expedition reaches Southernmost." Dis +3 is reached through the expedition itself — the companionship scene follows naturally from Arc B entry. **[FINDING SIM-C-11: Edeyja's companion acquisition is coupled to her Arc B trigger. You cannot companion Edeyja without triggering Arc B. This means every Edeyja companion run is an Arc B run. The Holdout (Arc A) Edeyja is by definition not a companion. This is elegant design — her companionship is structurally inseparable from the campaign event that ends the Southernmost's isolation.]**

**Stats (practitioner companion, §3.3):**

| Stat | Value | Notes |
|------|-------|-------|
| Agility | 3 | Warden — field-hardened |
| STR | 3 | |
| Endurance | 4 | Sustained warden work |
| Cognition | 4 | Empiricist practitioner |
| Charisma | 2 | She does not need to persuade |
| Combat Pool | (3×2)+History+3 = 12D (Warden combat + Thread History) |
| WI | 10 (End 4+6) | |
| Max Wounds | 3 | |
| TS | 75–80 | |
| Coherence | 7 (damaged from sustained warden work) |
| Certainty | 1 (Thread as primary frame) |

### Thread Operations as Companion
At TS 75–80, Edeyja is the highest-capability practitioner companion possible. Her Thread operations:
- Accessible at Coherence 7 — she has 7 Coherence points before crisis.
- Thread operations at TS 75–80: Deep tier (TS 50–70 range operations). She can perform Weaving operations the PC cannot (TS > PC's TS prerequisite for certain ops).
- RS effect: her presence in a territory at TS 75–80 is itself a stabilizing force — effectively a passive RS Maintenance operation while she's present.
- Coherence regeneration: requires Thread Discipline scenes. PC must budget at least 1 scene/3 seasons to Edeyja's Coherence maintenance or risk Coherence 0 by S28.

**Per §5.0b:** Edeyja at TS 75–80 is **stable** (not transforming) → Knot strain does NOT apply to PC's Close Knot with her. (§5.0b explicitly exempts stable Edeyja.) This is a critical differentiation from Vaynard.

### Arc Trajectory as Companion

**Arc B (Collaboration) as companion:** Fully compatible with companion status. She shares Warden knowledge. Campaign-altering information flows. RS stabilization becomes possible through her guidance.

**Arc C trigger (Crisis):** Warden count reaching 0 OR RS ≤ 20. As companion: if remaining wardens are killed while she travels with PC, Arc C fires. Her Continuity Conviction collapses to Autonomy. She no longer holds the line — she's trying to survive and reconstitute.

Arc C Edeyja as companion: her TS 75–80 becomes a liability in populated territories. She is "a walking Calamity echo" (per §5.2). Every season she remains in non-Southernmost territory at Arc C: territory RS drain (exact value not specified in doc — [GAP-SIM-C-12: Edeyja Arc C RS drain per season in non-Southernmost territories not specified in §5.2 or threadwork. Must be defined before any Arc C companion scenario is final.]).

### Stress Tests

**Stress 1 — Coherence depletion (S22):** 7 seasons as companion without Discipline scenes. Each Thread operation costs Coherence: if Edeyja performs 2 operations/season average: 14 Coherence consumed in 7 seasons. At Coherence 7 start: Coherence 0 by S22. PC must schedule 1 Discipline scene per 3 seasons or lose Edeyja's Thread capability entirely. Practical constraint: Discipline scenes use player Scene Slate budget.

**Stress 2 — Warden death event (S24):** Last surviving warden (not Edeyja) killed by Altonian Vanguard. Arc C fires. Edeyja's Conviction → Autonomy. She wants to withdraw to a safe location and rebuild the wardens. Companion departure condition: Conviction departure (she can no longer align with the PC's ongoing campaign objectives if those objectives don't address Warden reconstruction). 

**Stress 3 — RS ≤ 20 (S27):** Peninsular RS collapse. Per Arc C branch: Edeyja at TS 75–80 draining RS in non-Southernmost territories while Arc C active. Paradox: she needs to be in populated territories to help; her presence makes things worse. This is the core tension of late-game Edeyja companion. **[FINDING SIM-C-12: Edeyja's Arc C as companion creates a tragic feedback loop. She is the most capable solution to the RS crisis and simultaneously a contributing source of RS drain when in crisis herself. A PC with Edeyja companion approaching RS ≤ 20 faces an impossible choice: send her back to Southernmost (lose companion, lose Thread capability, but stop RS drain) or keep her (maintain capability, accelerate RS collapse). This is brilliant game design that rewards the RS decay clock with a personal companion-scale consequence.]**

### Departure Distribution

| Cause | Probability |
|-------|-------------|
| Voluntary return to Southernmost (Arc C) | 35% |
| Conviction departure (Warden reconstruction priority) | 25% |
| Coherence crisis (Coherence 0 — unable to function) | 15% |
| Combat death (rare — she's durable) | 5% |
| RS-crisis return | 20% |

**Net contribution:** Most powerful practitioner companion. RS stabilisation. Irreplaceable Thread operation capability. Coherence management burden. Late-game acquisition with potential Arc C tragedy. Peak narrative investment.

---

## NPC 11 — MARET ULN (Varfell — Succession)

### Acquisition
**Conditional:** Only activates if Vaynard is eliminated (Loyalty 0 + Mandate 0, per PP-486). Campaign must first eliminate Vaynard — either through Arc C collapse or player action.

**Acquisition timing:** Vaynard elimination most likely S15–25 (late campaign). Maret Uln becomes the Varfell successor. Companion acquisition: social path through the transition itself (supporting her succession → immediate Dis +2 from political alignment; 1–2 additional Evidence scenes → Dis +3).

**Probability of Dis +3:** ~70% if Vaynard is eliminated AND player engages the succession politically. Near 0% if Vaynard is not eliminated.

**Stats (practitioner companion, §3.3):**

| Stat | Value | Notes |
|------|-------|-------|
| Agility | 2 | Scholar, not warrior |
| STR | 2 | |
| Endurance | 3 | |
| Cognition | 4 | Inherits Varfell's knowledge base |
| Charisma | 4 | Political successor — she must persuade |
| Combat Pool | (2×2)+History+3 = 9D |
| WI | 9 | |
| Max Wounds | 2 | |
| TS | 35 | Confirmed §7.10 |
| Coherence | 10 (full — she is disciplined) |
| Certainty | 2 (direct Thread experience) |

**[Note: §7.10 confirms TS 35, Certainty 2 for Maret Uln — resolving ED-397/398 partially. Formal doc update still needed.]**

### Thread Operations as Companion
TS 35 = Active tier threshold crossed. Coherence 10 = full capacity. She is a capable practitioner mid-tier companion:
- Operations accessible: Active tier Thread work.
- Coherence cost: standard per threadwork_v30.
- Knot strain: TS 30–49 → +1 strain/season on PC's Close Knot. [Per §5.0b: this applies if she's transforming; at TS 35 stable, it may not apply. §5.0b language is "transforming NPC's thread-shift" — Maret Uln at stable TS 35 may be exempt. Ambiguous. [GAP-SIM-C-13: §5.0b exemption criteria for stable non-transforming NPCs at TS 30–49 not fully specified. Edeyja at 75–80 is explicitly exempt (stable). Maret Uln at 35 is ambiguous.]]

### Arc Trajectory as Companion

**No arc map.** [GAP-SIM-C-14: Maret Uln has no arc profile in §5.2.] Emergent from §2.10:

**S1–8 as companion (post-succession):** Consolidating Varfell under Equity/Reason hybrid framework. Her institutional focus is redirecting Varfell's resources toward RM collaboration. PC holding both Vossen and Maret Uln would be optimal: these two companions complement without Conviction contradictions (Maret Uln Equity aligns with Vossen Equity; Maret Uln Reason aligns with Hann's operationalism).

**Primary departure risk:** Evidence-style confrontation showing RM collaboration is failing (her Belief 1: "Vaynard's path led to destruction — knowledge must serve the community"). If the player uses Varfell's resources acquisitively (Vaynard-style), Maret Uln's Belief is violated.

### Stress Tests

**Stress 1 — Vaynard's legacy (S16):** PC finds Vaynard's Thread research in Varfell archives. Maret Uln's Evidence primary fires — she wants the research destroyed or redistributed. If PC hoards the research (Vaynard's Consequentialism persisting), Scar 1 fires.

**Stress 2 — RM alignment pressure (S20):** Vossen and Maret Uln are both companions (optimal case). RM territory seized by Church. Both companions react to same event simultaneously — double Outreach fires (Scene Slate budget pressure: 2 mandatory companion scenes same season). [GAP-SIM-C-15: Dual companion simultaneous Outreach behavior not specified in companion_specification_v30. What happens when 2 companions both generate Outreach on the same event?]

### Departure Distribution

| Cause | Probability |
|-------|-------------|
| Conviction departure (PC uses knowledge acquisitively) | 30% |
| Political demands (Varfell leadership requires her) | 30% |
| Combat death | 10% |
| Voluntary release | 20% |
| Rival recruitment | 10% |

**Net contribution:** Varfell institutional access. Practitioner capability at Active tier. Succession-arc resolution companion. Best paired with Vossen for complementary Equity/community arc.

---

## NPC 12 — TORSVALD (Löwenritter Riskbreaker)

### Acquisition
**Path:** Social or Knot path. Torsvald's profile from §7.10: TS 20+, Certainty 2. This is an active Riskbreaker — he has operational Thread awareness without formal training. His Löwenritter affiliation places him under Ehrenwall's authority structure; acquiring him as companion may require either Ehrenwall's blessing or a defection-style approach.

**[GAP-SIM-C-16: Torsvald has no §2 entry in npc_behavior — his Stance Triangle, Convictions, Ethical Framework, Resonant Styles, and Beliefs are all unspecified. He appears only in §7.10 TS table and companion_specification §3.3. This is a significant gap — he is listed as a playable companion but has no behavioral definition beyond his stat values. The following simulation is therefore largely inferential from his role context (Riskbreaker, Löwenritter, operational Thread awareness) and cannot be validated against canonical behavior.]**

**Inferred Convictions (from Riskbreaker role):**
- Primary: Autonomy (survives by being invisible — operational independence is survival)
- Secondary: Order (Löwenritter foundation; Valoria endures)

**Acquisition:** Most accessible to PCs embedded in Löwenritter operations (covert/military play). Solid-path: PC assists a Riskbreaker operation → Dis +1 → follow-on covert scene → Dis +2 → crisis scene (Torsvald's cover blown, PC saves him) → Dis +3. Timeline: ~6 scenes, achievable by S10 in a covert-focused campaign.

**Stats (practitioner companion, §3.3):**

| Stat | Value | Notes |
|------|-------|-------|
| Agility | 4 (inferred — Riskbreakers are field operatives) | |
| STR | 3 | |
| Endurance | 3 | |
| Cognition | 3 | Operational, not academic |
| Charisma | 3 | Operational presence |
| Combat Pool | (4×2)+History+3 = 14D (inferred — field combat History 3.5pts) |
| WI | 9 | |
| Max Wounds | 2 | |
| TS | 20+ (Active-approaching-Stirring) |
| Coherence | 8 (Riskbreaker wear) |
| Certainty | 2 |

**[NOTE: Torsvald's stats above are almost entirely inferred. Agility 4 is based on "active field operative" characterization — not canonical. A formal Torsvald §2 entry is required before these stats can be used in actual play. [GAP-SIM-C-16 repeated — this NPC needs a full §2 entry before reliable companion simulation is possible.]]**

### Thread Operations as Companion
TS 20+ = approaching Stirring (30). At TS 20, he's pre-threshold — no Knot strain. If TS advances to 30+ during companion time: strain begins (+1/season Close Knot). Unlike Vaynard, Torsvald has operational awareness without formal training — his Thread operations are intuitive and undisciplined.

**Coherence management:** 8 starting → same depletion risk as Edeyja but 8 sessions before crisis (vs 7 for Edeyja). Slightly more durable but equally in need of Discipline scenes.

**Primary contribution:** Best covert companion. If Agility 4 inference is correct: Combat Pool 14D = tied with Ehrenwall for combat excellence. Covert mission access (Riskbreaker network). Thread operations available at TS 20 (pre-Stirring ops: limited but present).

### Arc Trajectory as Companion

**Entirely inferential — no canonical arc map.** [GAP-SIM-C-17: Torsvald has no arc profile.]

**TS advancement risk:** Each covert operation Torsvald performs as companion risks a Discovery Event (Spirit check at TS 20). At Spirit 2 (estimated): 2D TN7 Ob 2, P ≈ 18%/operation. In a covert-heavy campaign (4 operations/season): P(Discovery Event/season) ≈ 56%. Fast TS advancement → Knot strain begins earlier than for any other companion.

### Departure Distribution

| Cause | Probability |
|-------|-------------|
| Löwenritter dissolution (Ehrenwall Coup attempt fails) | 30% |
| Conviction departure (inferred — operational ethics violated) | 25% |
| Discovery Event crisis (uncontrolled TS advance) | 20% |
| Combat death | 10% |
| Voluntary departure (mission complete) | 15% |

**Net contribution (inferred):** Potentially best combat companion alongside Ehrenwall. Covert access. Thread capability. High uncertainty on all values. Cannot be reliably simulated without a formal §2 entry.

---

## CROSS-NPC FINDINGS

### FINDING SIM-C-13: Companion Slot Optimization Map

Optimal companion pairings by campaign type:

| Campaign type | Slot 1 | Slot 2 | Rationale |
|--------------|--------|--------|-----------|
| Military-primary | Ehrenwall | Generic officer | Ehrenwall 12D + officer 9D = 21D combined combat pool |
| Social/political | Baralta | Vossen | Parliamentary + community intelligence; no Belief conflicts |
| Thread/RS arc | Edeyja | Maret Uln | Deep + Active tier practitioner pair; no Belief conflicts |
| Restoration arc | Vossen | Hann | Complementary networks; internal drama is the arc |
| Crown arc | Torben | Almud (Arc A) | Political legitimacy; dual Crown asset |
| Covert | Torsvald | Hann | Riskbreaker + logistics network |

**Slot conflict risk:** Vaynard held with Edeyja creates maximum Knot strain burden (Vaynard: +1/season Close Knot from Arc B; Edeyja: 0 from stable TS). Manageable but demanding.

### FINDING SIM-C-14: Departure Rate Calibration

Aggregated campaign departure probability (all causes, 30-season campaign):

| NPC | P(still companion at S30) |
|-----|--------------------------|
| Generic officer | 30% |
| Vaynard | 20% (Arc C risk dominant) |
| Vossen | 30% |
| Hann | 25% |
| Torben | 25% |
| Ehrenwall | 20% (Coup dominant) |
| Baralta | 35% |
| Himlensendt | 10% (unstable by design) |
| Almud | 15% |
| Edeyja | 25% |
| Maret Uln | 35% |
| Torsvald | 30% (high uncertainty) |

**[FINDING SIM-C-14: Average companion survival rate at S30 ≈ 25%. This means the average campaign loses 75% of its companions by endgame. This feels high — a 30-season campaign with 2 companion slots should expect to cycle through ~6–8 companions total. This validates the departure system as active (not just a background threat) and creates real grief mechanic opportunities. But it also means the player needs an active pipeline of companion-eligible NPCs or will be companion-less in the late game. Recommend reviewing whether departure rates are intentionally high or should be calibrated down for longer campaigns.]**

### FINDING SIM-C-15: Arc Coverage Gap

Of 12 playable NPCs:
- **5 have arc maps** (Almud, Himlensendt, Baralta, Vaynard, Edeyja).
- **7 have no arc map** (Vossen, Hann, Torben, Ehrenwall, Almud [partial], Maret Uln, Torsvald).

Arc maps exist only for faction leaders. Companion-path NPCs (Vossen, Hann, Torben as young NPC, Torsvald) have no arc specification. This is the single largest gap for campaign-length companion simulation: without arc maps, companion behavior in S20+ is entirely GM-emergent without system support.

**Recommended:** Add arc profiles for Vossen, Hann, Torben, Ehrenwall, and Torsvald to npc_behavior §5.2. These need not be as long as the faction-leader arcs — 2–3 branch conditions each is sufficient. Torsvald additionally needs a full §2 entry before any canonical companion simulation can be produced.

### FINDING SIM-C-16: Thread Strain Management Underdefined

Four companions impose Knot strain during companion time (Vaynard post-Discovery Event, Maret Uln if transforming, Torsvald post-TS 30, potentially Edeyja in Arc C). The companion spec does not address how the PC manages accumulated Knot strain from multiple sources simultaneously. If PC holds 2 practitioner companions in TS-advancing arcs: strain could reach +3/season Close Knot. At this rate over 10 seasons: 30 accumulated Thread strain — likely catastrophic for the PC's own Coherence. **[GAP-SIM-C-18: No multi-source Knot strain stacking rule in companion_specification_v30 or threadwork_v30. Does strain from multiple companions stack additively? Is there a cap? Requires definition.]**

---

## OPEN ITEMS GENERATED

### New EDs

| ID | Description | Priority |
|----|-------------|----------|
| ED-591 | Torsvald §2 entry absent — Stance Triangle, Convictions, Resonant Styles, Beliefs, arc profile all unspecified | P1 |
| ED-592 | Arc profiles absent for Vossen, Hann, Torben, Ehrenwall, Maret Uln — 5 of 12 playable NPCs lack arc specification | P1 |
| ED-593 | Almud as companion → Crown faction BG effect undefined. If Crown's king is a personal-scale companion, what happens to Crown's BG faction actions? | P2 |
| ED-594 | Torben companion + Coup scenario: Companionship vs BG Loyalty conflict unresolved | P2 |
| ED-595 | Dual companion simultaneous Outreach behavior unspecified | P2 |
| ED-596 | Multi-source Knot strain stacking rule absent from companion spec and threadwork | P2 |
| ED-597 | Edeyja Arc C RS drain per season in non-Southernmost territories unspecified | P2 |
| ED-598 | §5.0b exemption criteria for stable TS 30–49 NPCs (Maret Uln) ambiguous | P3 |
| ED-599 | Torben companion-specific mechanical bonuses (Legitimacy contribution) undocumented | P3 |
| ED-600 | Officer companion rival-recruitment vulnerability: advisory role as counter-incentive not formalized | P3 |

### GAP Summary

| ID | Description |
|----|-------------|
| GAP-SIM-C-01 | Almud TS 28 (§2.1) vs TS 0 (§7.10 per ED-398) — contradiction |
| GAP-SIM-C-02 | Vaynard TS 14 (§2.4) vs TS 10 (§7.10) — minor discrepancy |
| GAP-SIM-C-03 | Himlensendt Certainty 5 (§2.2) vs Certainty 4 (§7.10) — contradiction |
| GAP-SIM-C-04 | Vaynard Arc B trigger condition not specified |
| GAP-SIM-C-05 | Vossen arc profile absent |
| GAP-SIM-C-06 | Hann arc profile absent |
| GAP-SIM-C-07 | Torben companion mechanical bonuses undefined |
| GAP-SIM-C-08 | Torben arc profile absent |
| GAP-SIM-C-09 | Ehrenwall companion stats not formally defined |
| GAP-SIM-C-10 | Ehrenwall arc profile absent |
| GAP-SIM-C-11 | (validated as intended design — no gap) |
| GAP-SIM-C-12 | Edeyja Arc C RS drain rate undefined |
| GAP-SIM-C-13 | §5.0b stable TS 30–49 exemption ambiguous |
| GAP-SIM-C-14 | Maret Uln arc profile absent |
| GAP-SIM-C-15 | Dual companion simultaneous Outreach unspecified |
| GAP-SIM-C-16 | Torsvald §2 entry entirely absent (P1) |
| GAP-SIM-C-17 | Torsvald arc profile absent |
| GAP-SIM-C-18 | Multi-source Knot strain stacking undefined |

---

## COVERAGE MATRIX UPDATE (NEW ENTRIES)

### Resolved SIM-DEBT

| ID | Description | Status |
|----|-------------|--------|
| SIM-NPC-04 (partial) | Framework drift and companion arc interaction — tested via Baralta (Influence cap S4), Vossen (RM suppression), Vaynard (Discovery Event probability). Full 6-season drift sim remains open. | PARTIAL |

### New SIM-DEBT

| ID | Description |
|----|-------------|
| SIM-COMP-01 | Full arc profile simulation for Vossen, Hann, Torben, Ehrenwall, Maret Uln once arc maps are written (ED-592) |
| SIM-COMP-02 | Multi-companion Knot strain stacking stress test (ED-596): 2 practitioner companions in concurrent TS-advancing arcs |
| SIM-COMP-03 | Companion departure rate calibration: validate 75% departure rate at S30 is intended |
| SIM-COMP-04 | Torsvald full sim (pending ED-591: §2 entry) |

### New Confirmed Working

| System | Source | Status |
|--------|--------|--------|
| Edeyja acquisition coupled to Arc B (cannot companion without triggering Arc B) | SIM-COMP | ✓ Elegant design |
| Vossen departure tied to Church TC 65 (faction suppression) | SIM-COMP | ✓ Cross-layer consequence chain works |
| Himlensendt as companion creates controlled/uncontrolled theological bomb | SIM-COMP | ✓ High-risk high-reward design confirmed |
| Vaynard companion imposes late-campaign Knot strain via Discovery Events | SIM-COMP | ✓ Correctly identified tension |
| Ehrenwall combat contribution validates acquisition difficulty | SIM-COMP | ✓ 12D pool justifies hard acquisition barrier |
| Dual Hann+Vossen Belief divergence under pressure (intentional drama) | SIM-COMP | ✓ Best social campaign pair |

---

*End of simulation document. 12 playable NPCs simulated. 10 new EDs. 18 gaps identified. Awaiting Jordan review.*
