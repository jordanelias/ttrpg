# Valoria — Emergent Narrative Arcs: Structural Misreader Archetypes
## SIM-ARC-04 | Generated: 2026-04-04 | Model: Sonnet 4.6
## Mechanics targeted: Certainty track, Binding Operations, Composure/Rattled redesign,
##   Community Weaving as RS restoration, Diverge state, Discipline asymmetry (PP-297)
## Source: params_core PP-289/290/291, params_threadwork PP-287/293/296, params_contest PP-280-286/292-295, params_mass_combat PP-297

---

## Structural Misreader Archetypes (NG-M through NG-R)

Distinct from all prior batches. These players understand individual systems correctly but misread *inter-system relationships* — how mechanic A constrains or enables mechanic B. The errors are not compulsive (IP-A–F), not restrained (NG-A–F), not social-structural (NG-G–L). They are *architectural*: the player has a coherent mental model of the game that is wrong in a specific cross-system linkage.

| Code | Archetype | Behaviour |
|------|-----------|-----------|
| NG-M | **The System Isolator** | Treats each mechanic as independent. Optimises Thread operations without considering RS/Certainty effects. Optimises Contest without tracking Domain Echo. Never reads cross-system consequences. Correct within each system; blind to interactions. |
| NG-N | **The Scale Conflator** | Applies personal-scale rules at faction scale and vice versa. Uses personal social mechanics (Composure, Rattled) as proxies for faction Stability without understanding the conversion. Attempts personal Thread ops to solve strategic problems. |
| NG-O | **The Resource Pool Mixer** | Treats all pools as fungible. Spends Momentum on Thread rolls (which it cannot affect). Tries to use Wealth to repair Coherence. Applies Combat Pool dice to non-combat situations. Each pool is correctly understood in isolation; their distinctness is the blind spot. |
| NG-P | **The Causal Inverter** | Reads causation backwards in multi-stage chains. Addresses the symptom rather than the cause: reduces TC (symptom) rather than Church Mandate (cause). Patches RS (symptom) rather than reducing Thread operation frequency (cause). Always one stage behind. |
| NG-Q | **The Threshold Chaser** | Optimises toward threshold crossings (RS 60, TC 60, Mandate 5) but does not model what happens immediately after crossing. Achieves the threshold, then is unprepared for the cascade it triggers. Correct target selection; zero preparation for consequences. |
| NG-R | **The False Synergy Reader** | Identifies two mechanics that superficially appear to interact and builds strategy around the interaction — which doesn't exist. Classic case: assumes high Certainty suppresses RS loss (it doesn't — they're independent). Builds strategies around phantom linkages. |

Notation: optimal path = solid line; structural misreader branch = dashed line with `[NG-X]` tag.

---

## ARC 16: The Certainty Cascade

### Mechanical Seed
Practitioner PC undergoes three high-TS Thread events in rapid succession → Certainty drains from 10 toward 0 → at Certainty 3, character's social interactions produce Diverge states (both parties asserting incompatible realities) → at Certainty 0, GM takes partial narrative control → Composure (Rattled redesign) interacts with Certainty loss via social scenes → players attempt to restore Certainty via rest, but rest requires leaving Southernmost proximity.

### Narrative

Certainty degradation is invisible until it isn't. The practitioner player character keeps functioning — they roll, they succeed, they move through scenes. What changes is subtle: they describe what they see in Thread-adjacent terms that other characters don't follow, they reference configurations that aren't visible to non-practitioners, they occasionally correct the GM's description of what's physically present. Other players accommodate this. The GM notes the Certainty track. Nobody talks about it.

At Certainty 5, the character starts generating Diverge states in social exchanges without intending to. They assert something true (Thread-perceptible) that no other NPC in the scene can verify. The NPC isn't wrong from their perspective; the player character isn't wrong from theirs. Both assert, both succeed, neither track moves. The Diverge state triggers after three consecutive mismatched assertions — the NPC simply stops engaging, not from hostility but from a failure to find common ground. This is the mechanic of being between two realities at once.

At Certainty 3, other players will notice something is wrong. At Certainty 0, the GM is running part of the character.

### Flowchart

```mermaid
flowchart TD
    A["Practitioner PC: 3 high-TS Thread events in 2 seasons\nCertainty track: 10 → 7 → 5 → 3\n[PP-289: −1 per Coherence 0 event; −1 per sustained Southernmost exposure ≥3 scenes]"]
    A --> B["Certainty 5: social Diverge states begin\n[PP-271: Diverge fires when both parties Success+\nopposing positions, margin ≤ 1]\nThread-factual assertions = systematically non-shared basis\nP(Diverge) ≈ 40% per social exchange with non-practitioner"]
    B --> C["3 consecutive Diverge states:\nNPC exits engagement without hostility\nPlayers lose social action without expending Composure\nFaction relationship unchanged but no progress made"]

    C --> D{Players respond to Certainty drain}

    D -->|"Optimal: rest protocol\nLeave Southernmost proximity (≥ 3 scenes from Thread-active zone)\nLong rest: Certainty +1/night\nNeed 4 nights: Certainty 3 → 7\n4 sessions of normal play window"| E["Certainty recovers 3 → 7 in 4 nights\nDiverge state frequency drops\nP(Diverge) ≈ 10% per exchange at Certainty 7\nPractitioner rejoins social play effectively"]

    D -.->|"[NG-M] System Isolator:\n'Certainty is a Thread track —\nkeep running Thread ops while resting.\nResting means not doing mass combat,\nnot stopping Thread work.'"| F["Thread operations during 'rest' period:\nPP-289: long rest requires no Thread operations\nEach Thread op during rest = Certainty −1 (no recovery)\nCertainty 3 → 2 → 1 over 2 sessions\n'Rest' achieved on all other systems;\nCertainty drained instead of recovered"]
    F --> G["Certainty 1: social Diverge P(70%)\nPractitioner effectively non-functional in social scenes\nGM warns: one more Coherence 0 event → Certainty 0"]

    D -.->|"[NG-R] False Synergy Reader:\n'High Spirit suppresses Certainty loss —\nSpirit is the anchor stat for Thread.\nRun Spirit-boosting actions to\nstabilise Certainty.'"| H["Spirit-boosting actions: no effect on Certainty\n[PP-289: Spirit unrelated to Certainty — explicitly stated]\nPlayer spends 2 seasons on Spirit investment\n(History Point allocation, Spirit-primary scenes)\nCertainty continues draining from environmental exposure\nSpirit 5 → 6: no Certainty effect"]
    H --> I["Certainty 2 when Spirit investment completes\nPlayer discovers the linkage doesn't exist\n2 seasons of wrong investment\nCertainty recovery now requires 6 nights of rest\n(Certainty 2 → 8 = 6 nights)\nbut the window for the current arc has passed"]

    D -.->|"[NG-P] Causal Inverter:\n'Certainty loss is from Diverge states —\neliminate Diverge states to stop\nCertainty draining'"| J["Causal chain: Certainty loss → Diverge states\n(not Diverge states → Certainty loss)\nPlayer attempts to prevent Diverge by\navoiding social exchanges with non-practitioners\nPractitioner withdraws from social play\nfor 1 season to 'stop the drain'"]
    J --> K["Social withdrawal: Certainty continues draining\nfrom environmental Thread exposure\n(Southernmost proximity, not social scenes)\nCertainty 3 → 2 with no social scenes\nPlayer eliminated a symptom; cause unaddressed\nDiverge states return immediately when\npractitioner re-enters social play"]

    D -.->|"[NG-Q] Threshold Chaser:\n'We need to get Certainty back to 5\nbefore the next social scene.\nJust need to hit the threshold.'"| L["Player focuses on reaching Certainty 5\n(2 nights of rest: Certainty 3 → 5)\nthen immediately re-engages social play\nand Thread operations simultaneously"]
    L --> M["Certainty 5: P(Diverge) still 40%\n— threshold of 5 is not the 'safe' threshold\nSafe threshold is 7+ (P(Diverge) ≈ 10%)\nThread ops during social-engagement period:\nCertainty 5 → 4 → 3 within 1 season\n'Reset to 5' becomes a treadmill:\nreach 5, drain back to 3, rest to 5, drain"]

    E --> N["Certainty 7: functional recovery\nPractitioner can engage socially and operate Thread\nbut must monitor Certainty actively\n— 3 more high-TS events will drain back to 5\nLong-term: Southernmost proximity management\nis the actual solution"]
    G --> O["Certainty 0: GM takes partial narrative control\n'You perceive the Thread state of the room\nmore vividly than the social dynamics.\nWhat do you do?' — GM describes what the character\nbelieves they're doing; player specifies intent only\nMechanically: practitioner removed from\nfaction and social play until Certainty recovers\n— requires full campaign-rest (10+ nights)"]
    I --> P["2-season wrong investment\nCertainty 2 when discovered\nRecovery window missed for current arc\nSpirit 6 is a permanent gain — not wasted —\nbut the campaign context has moved on"]
```

### Footer

Emerges from the Certainty track (PP-289) interacting with Thread operation frequency, Southernmost proximity, and the Diverge state (PP-271). No player designed this — it is the output of sustained high-TS Thread work colliding with a new cross-system track. Arc shape: 2–4 seasons of degradation, 1–2 seasons of recovery. The arc exists to test whether players track cross-system effects or treat Certainty as a background resource.

**Structural misreader findings:**
- NG-M (System Isolator): The most common architectural error. Thread ops and Certainty recovery are explicitly cross-linked (rest requires no Thread ops). The System Isolator reads "rest" as a combat/social category, not a Thread category. The error is a definitional scope failure: "rest" means all high-intensity activity including Thread work.
- NG-R (False Synergy Reader): Spirit-Certainty linkage doesn't exist. It *looks* plausible (Spirit is the Thread attribute; Certainty is Thread-adjacent). PP-289 explicitly states "Spirit is unrelated to Certainty." The phantom synergy is the most seductive wrong model in the system.
- NG-P (Causal Inverter): Certainty loss is the cause, Diverge states are the symptom. Avoiding social scenes prevents Diverge events but doesn't address environmental Thread exposure, which is the actual drain mechanism. The character retreats from the symptom while the cause continues.
- NG-Q (Threshold Chaser): Certainty 5 is not the functional threshold — 7 is. The chaser achieves 5, re-engages, and drains back to 3 within one season. The "threshold" they're chasing is the wrong one, and they don't model the drain rate of normal play.

---

## ARC 17: The Composure Trap

### Mechanical Seed
High-Composure NPC (Himlensendt, Composure 12 or Baralta, Composure 11) faces players in a formal Contest → Rattled redesign (PP-266): Rattled fires when full Composure track expended from one hit, not a simple threshold → players must deliver sufficient net successes to expend the full track in a single exchange → optimal play requires concentrating force rather than spreading damage → Contest ends before Rattled can fire if players distribute small wins across multiple exchanges.

### Narrative

The players have beaten Himlensendt in debate before. Or they think they have — they won exchanges, moved the Conviction Track, achieved their position. What they may not understand is that winning exchanges in the Contest System does not damage Composure. Composure is expended when a single overwhelming exchange delivers enough social damage to drain the full track. Three successful exchanges delivering 3 track movement each is not the same as one exchange delivering enough to trigger Rattled.

Against Himlensendt (Composure 12), triggering Rattled requires an exchange that delivers 12 net social damage in one hit. That means net successes dramatically exceeding Ob in a single exchange — not spread across many. The players who "won" past debates won the position (Conviction Track) but never touched Composure. They can do this again. Himlensendt will not be Rattled. He will concede the stated stakes, comply with the ruling, and continue exactly as before with no persistent impairment. His Composure is intact.

This arc tests whether players understand that Track position victory and Composure damage are different win conditions.

### Flowchart

```mermaid
flowchart TD
    A["Formal Contest vs Himlensendt\nComposure: 12 [Charisma 6 + 6, PP-266]\nRattled condition: full 12-point track expended in one hit\n[PP-266: Rattled is a full-track event, not a threshold]"]
    A --> B["Players' Contest objective:\n(a) Win position (Conviction Track) — standard play\n(b) Rattle Himlensendt (persistent impairment) — requires 12 net social damage/exchange"]
    B --> C["Himlensendt's Contest pool:\nCharisma 6 × 2 + Theology History 3+3 = 18D TN7\nE[net] = 18 × 0.3 = 5.4 per exchange\nPlayer pool required to exceed this AND hit Composure threshold"]

    C --> D{Player strategy}

    D -->|"Optimal: concentrate force\nAmplify + Momentum + faction boost\nTarget single exchange for maximum net margin\nPool: Charisma 5×2 + History 5+3 + Amplify 2 + Momentum 2 = 24D TN7\nE[net] = 7.2 vs Himlensendt 5.4\nNet margin ≈ 1.8 — insufficient for Composure 12 in one exchange\n[Social damage per exchange = net margin × Charisma modifier]\nAt Charisma 5: modifier +2 → ~3.6 damage/exchange"| E["Expected outcome: Rattled in ~3 exchanges\n(3 × 3.6 = 10.8 — close but not 12)\nRattled fires on 4th exchange typically\nVia accumulated full-track model:\nbut wait — PP-266 specifies one-hit expend\nRattled requires 12 in a SINGLE exchange\nExpected single-exchange damage: 3.6\nRattled probability in single exchange: ~2%"]
    E --> F["Rattled is near-impossible vs Himlensendt\nin a standard Contest at standard pools\nRequires extreme pool stacking:\nAmplify + all Momentum + Guilds/faction boost\nPool ~30D+ for realistic chance\nConclusion: players win position routinely;\nRattled requires campaign-level resource expenditure"]

    D -.->|"[NG-M] System Isolator:\n'We won 4 exchanges — we won.\nHimlensendt is beaten.'"| G["Players win Conviction Track position\nHimlensendt concedes stated stakes\nPlayers treat this as full victory\nHimlensendt: no Composure damage\nno Rattled state\nIn 2 seasons: same issue recurs\nHimlensendt restarts from full Composure 12\nPlayers 'win' the same Contest again\n— indefinitely, without permanent change"]

    D -.->|"[NG-N] Scale Conflator:\n'Himlensendt's Composure is Church Stability.\nIf we damage his Composure,\nChurch Stability drops.'"| H["Composure and Stability are distinct tracks\n[Composure: personal social endurance]\n[Stability: faction institutional cohesion]\nThey do not directly interact\nRattling Himlensendt personally:\n→ he is impaired in social scenes for the rest of this scene\n→ Church Stability: unchanged\nPlayers spend resources pursuing\n'Church Stability damage' via Composure attack\n— wrong mechanic for the goal"]

    D -.->|"[NG-O] Resource Pool Mixer:\n'We'll use Momentum auto-successes\nto stack our Contest pool PLUS\nuse our Combat Pool dice —\nthis is a confrontation, it should all count'"| I["Combat Pool dice cannot be added to Contest rolls\n[Separate pool mechanics: Combat Pool = Agility-based;\nContest pool = Charisma-based]\nPlayer attempts to add Combat Pool 7D\n(treating it as 'confrontation' dice)\nActual pool: Charisma 5×2 + History 8 + Momentum 2 = 20D\nIllegal pool: +7D Combat = 27D\nEffect of error: overestimates damage capacity\nActual damage: ~4.0/exchange (20D)\nExpected (from 27D): 5.4/exchange\nRattled threshold remains 12 — still near-impossible\nbut player has incorrect expectation of when it fires"]

    D -.->|"[NG-P] Causal Inverter:\n'Himlensendt keeps winning Contests\nbecause Church Stability is high.\nDrop Church Stability first,\nthen his Contest pool will weaken.'"| J["Himlensendt's Contest pool:\nPersonal attributes (Charisma 6, Theology 3+3)\nNOT derived from Church Stability\nChurch Stability affects faction Domain Actions,\nnot Himlensendt's personal Contest pool\nPlayers spend 2 seasons on Church Stability Domain Actions\nbefore attempting Contest\n— correct understanding of Stability's function;\n  wrong belief that it feeds into personal Contest pool\nContest attempt after: Himlensendt pool unchanged\nPlayers have spent 2 seasons on a non-cause"]

    F --> K["Correct model established:\nPosition victory (Conviction Track) = achievable\nRattled = near-impossible without extreme resources\nBoth are valid win conditions; they cost different amounts\nPlayers can choose which to pursue with eyes open"]
    G --> L["Indefinite position victories\nHimlensendt never impaired\nChurch policy continues regardless of Contest wins\nPlayers wonder why 'winning debates' doesn't change anything —\nbecause winning the Track doesn't change the actor,\nonly the stated stakes of that specific debate"]
    H --> M["Wrong mechanic pursued\nComposure attacks that don't hit Church Stability\nPlayers spend Momentum/Amplify on Rattled pursuit\nwhen Stability Domain Action was the correct tool\n2 seasons, no Stability change, Himlensendt unimpaired"]
    J --> N["2 seasons spent reducing Stability (which works)\nbut for the wrong reason (Stability didn't affect Contest pool)\nParadox: the action was mechanically correct\n(reducing Stability is valid) but for the wrong reason\nPlayers get the right outcome by accident\n— at double the cost (2 seasons instead of 1)"]
```

### Footer

Emerges from the Rattled redesign (PP-266) colliding with high-Composure NPCs. The redesign makes Rattled require a single overwhelming exchange rather than accumulated damage — specifically to model institutional figures who do not crack gradually. The arc has no villain; Himlensendt's immunity to Rattled is structural, not unfair. Arc shape: 1 Contest scene, consequence extends 2–3 seasons. Most impactful in TTRPG mode where NPC persistence matters.

**Structural misreader findings:**
- NG-M (System Isolator): Track position victory feels like a complete win. Within the Contest system it is. Across systems, it isn't: Himlensendt restarts at full Composure next scene. The System Isolator has a complete, correct understanding of the Contest system and a total blind spot for NPC persistence mechanics.
- NG-N (Scale Conflator): Composure and Stability look like parallel tracks for individuals and factions respectively. They are not linked. Rattling Himlensendt doesn't touch Church Stability. The confusion is architecturally reasonable; the linkage doesn't exist.
- NG-O (Resource Pool Mixer): Combat Pool dice cannot contribute to Contest rolls. The "confrontation" framing makes this feel intuitive — all the character's capability should count. It doesn't. The error produces an overestimate of damage potential without affecting the mechanic.
- NG-P (Causal Inverter): Church Stability and Himlensendt's personal Contest pool are independent. Reducing Stability before the Contest is correct strategy — but for different reasons (Stability affects faction Domain Actions, not personal Contest pools). The Causal Inverter does the right thing for the wrong reason and is surprised it works.

---

## ARC 18: The Community Weaving Bottleneck

### Mechanical Seed
RS at 55 and declining → players identify Community Weaving (PP-296) as restoration tool → Community Weaving pool: Attunement + History + TPS, Ob 3, RS +1/+2 → requires Thread Sensitivity 50+ practitioner → practitioner already committed to 2 other Thread operations per scene → Community Weaving vs operational Thread use is a direct resource competition → players must choose between RS restoration (long-term) and Thread effectiveness (short-term) every scene.

### Narrative

Community Weaving is the only player-accessible RS restoration mechanism that doesn't require extreme Thread Sensitivity or foundational-scale operations. It is not passive — it requires a sustained Thread operation (Attunement + History + TPS, Ob 3) that consumes the practitioner's contact window for other operations that scene. The question is never whether to do it; it is always whether to do it *now*, given what else the practitioner needs this scene.

The arc begins when RS crosses 55 and players first look for a restoration path. They find Community Weaving in params_threadwork. They understand the mechanic. The problem is that their practitioner is also running an active investigation (Thread Diagnosis equivalent operations), defending against an Inquisitor approach (Binding Ops), and occasionally Weaving for tactical advantage. Every scene has competing Thread priorities. Community Weaving always loses to the urgent.

The RS decay continues at the rate of Thread operations minus Community Weaving output. If the practitioner runs 2 ops/scene without Weaving: RS −4 to −6/scene. If they substitute 1 Community Weave/scene: RS net approximately −2 to +1 depending on outcome. The choice is visible. The urgency of non-Weaving ops is what makes it hard.

### Flowchart

```mermaid
flowchart TD
    A["RS at 55, declining\nPractitioner Thread ops: 2/scene average\n[RS drain: ~3-4/scene without restoration]\nCommunity Weaving identified as restoration tool\n[PP-296: Attunement+History+TPS, Ob3, RS+1 Success / RS+2 Overwhelming]"]
    A --> B["Typical practitioner pool:\nAttunement 4 + History 3+3 + TPS 4 = 14D TN7\nE[net] = 4.2 vs Ob 3\nP(Success) ≈ 85%, P(Overwhelming) ≈ 65%\nExpected RS gain per Weave: 0.85×1 + 0.65×1 = +1.5 (avg)\n[Success gives +1; Overwhelming gives +2; these don't stack — Overwhelming includes Success]"]
    B --> C["Net RS budget per scene:\nWithout Weaving: −3 to −4 (2 ops)\nWith 1 Weave replacing 1 op: −1.5 to +0.5 (net)\nWith full Weaving (all contact rounds): RS +1.5 net/scene\n— but practitioner runs zero ops"]

    C --> D{Player strategy}

    D -->|"Optimal: scheduled Weaving\nDesignate 1 scene per 2 scenes as Weaving-primary\nOdd scenes: 2 ops (tactical use)\nEven scenes: 1 Weave + 0 ops (restoration)\nNet RS per 2-scene cycle: (−3) + (+1.5) = −1.5\n— still declining but at 1/3 prior rate\nRS 55 → stable ≈ 40 over 10 seasons\nWith Overwhelming more frequent: net zero achievable"| E["Sustainable RS management\nRS does not collapse within campaign arc\nPractitioner effectiveness: 75% of unmanaged rate\n(1 op/2 scenes not run)\nFaction consequences: slightly reduced Thread contribution\nbut RS collapse avoided"]

    D -.->|"[NG-M] System Isolator:\n'Community Weaving is a Thread operation,\nnot a recovery action.\nWe'll do recovery between scenes —\nin the narrative downtime.'"| F["Community Weaving requires active contact window\n— cannot be performed 'between scenes' (no contact established)\nPlayer treats it as a passive recovery action\nsimilar to HP rest in other systems\nActual recovery: 0\nRS continues declining at full rate\nRS 55 → 40 within 5 scenes"]

    D -.->|"[NG-R] False Synergy Reader:\n'RS recovers when we achieve Beliefs.\nBeliefs are spiritual coherence; RS is world coherence.\nThey should interact — we'll focus\non Belief achievement to restore RS.'"| G["Belief achievement has no RS effect\n[RS restoration: only via Mending, Community Weaving,\nNiflhel document study (PP-258), or controlled Ritual]\nBeliefs affect Momentum gain and CP awards\nPlayer spends 2 scenes pursuing Belief achievement\n(correct play for Momentum; wrong play for RS)\nRS declines during both Belief-achievement scenes\n— no restoration occurs"]

    D -.->|"[NG-P] Causal Inverter:\n'RS is declining because we're in\nSouternmost-adjacent territory.\nMove away from Southernmost to stop RS drain.'"| H["RS drain cause: Thread operations (primarily)\nnot physical location (secondarily)\nSouthernmost exposure: RS −1/session passive\nThread ops: RS −2 to −4/operation\nMoving away from Southernmost: saves ~1 RS/session\nThread ops in non-Southernmost territory: still drain RS\nPlayer moves party to 'safe' territory\nPractitioner continues 2 ops/scene\nRS still declines at −3 to −4/scene vs −4 to −5 before\nMinor improvement; major drain unaddressed"]

    D -.->|"[NG-Q] Threshold Chaser:\n'RS needs to be above 60 before\nwe worry about it. It's at 55 —\nlet's push it back to 60 then\nstop worrying.'"| I["Player runs 3 Community Weaves in 1 scene\n(contact window at Focus 4 = 3 op rounds)\nRS 55 → 58 (approximate)\nThen returns to 2-ops-per-scene with no Weaving\nRS 58 → 52 in 2 scenes\n'Pushed to 60' — actually only reached 58\nand returned to declining trajectory\nNo structural change to op/Weave ratio\nRS threshold chase is a treadmill"]

    D -.->|"[NG-N] Scale Conflator:\n'Community Weaving is a faction action,\nnot a personal Thread op.\nWe should run it as a Domain Action\nto get faction-stat benefit.'"| J["Community Weaving is a Thread operation\n[PP-296: NOT a Domain Action; no faction stat involvement]\nPlayer attempts to frame Community Weaving\nas a Domain Action for Mandate or Stability benefit\nGM clarifies: Community Weaving = Thread op, RS target only\nPlayer loses the scene planning around\na non-existent mechanical linkage\nCommunity Weave performed correctly:\n+1 RS; no faction benefit\nPlayer disappointed — expected Stability +1 as well"]

    E --> K["RS managed long-term\nDecline rate 1/3 of unmanaged\nPractitioner slightly less effective tactically\nbut world remains playable\nRS 55 → 42 over 10 seasons (vs 15 without management)"]
    F --> L["RS 40 within 5 scenes\nRS threshold effects reactivate\nChurch Intel fires on anomalies\nSame cascade as ARC 2 (RS Drain) but faster"]
    I --> M["RS treadmill: 55→58→52→56→49→53...\nEach spike of Weaving followed by\nunmanaged decline\nNet: RS still declining at ~60% of unmanaged rate\nCompared to scheduled Weaving: twice the RS spend\nfor 2/3 of the benefit"]
```

### Footer

Emerges from Community Weaving (PP-296) being the primary RS restoration tool but competing directly with offensive/tactical Thread operations for the same contact window. No player designed the tension — it is the structural output of Thread operation economics. Arc shape: ongoing across all seasons where RS is below 65; becomes critical below 50. The arc has no dramatic peak — it is pure resource management. Its simulation value is in finding the player archetypes that fail to sustain it.

**Structural misreader findings:**
- NG-M (System Isolator): Treats Community Weaving as a passive/narrative action. The cross-system link — Weaving requires an active Thread contact window — means it competes with other ops. The Isolator models Weaving as "downtime recovery" rather than "active operation competing for the same resource pool."
- NG-R (False Synergy Reader): Belief achievement → RS restoration is the most plausible phantom synergy in the game. Both Beliefs and RS represent coherence (personal and world respectively). The linkage looks canonical. It isn't. Beliefs affect Momentum; RS has its own restoration toolkit. The False Synergy Reader built a strategy on a philosophically compelling but mechanically absent connection.
- NG-P (Causal Inverter): Southernmost proximity is a real RS drain — but it's secondary. Thread operations are the primary drain. Moving away from Southernmost treats the minor cause as the major one. RS continues declining at 90% of prior rate in "safe" territory.
- NG-Q (Threshold Chaser): Three Weaves in one scene pushes RS up — then the player returns to 2-ops-per-scene. The spike decays within 2 scenes. The threshold chaser optimises for the peak without modelling the sustainable rate. "Push to 60" fails because 60 is not achievable in one scene (RS 55 + ~3 from 3 Weaves = 58 at most) and decays before the next threshold event.

---

## ARC 19: The Discipline Fault Line

### Mechanical Seed
Large formation (Size 8, Discipline 4) engages a smaller formation (Size 4, Discipline 6) in symmetric engagement → PP-297: symmetric engagements (equal losses) do NOT trigger Discipline check → players pursuing attrition strategy assume Discipline check fires on every loss → fail to distinguish symmetric from asymmetric exchanges → miss the mechanic that protects large formations in even fights while making asymmetric losses catastrophic.

### Narrative

The battle looks simple from the players' side. Löwenritter heavy infantry (Size 8, Discipline 4) versus Crown cavalry (Size 4, Discipline 6). The players, advising the Crown cavalry, want to use mobility to inflict asymmetric losses — hit hard, pull back, deny the larger formation the close engagement it needs. The mechanic supports this: asymmetric losses trigger the Discipline check that might break the Löwenritter formation.

What the players may not understand is the converse: if the exchange is symmetric (both sides lose 1 Size in the same Engagement Phase), neither side's Discipline fires. The Löwenritter's Discipline 4 only becomes a liability when they lose more than the cavalry in the same exchange. In a grinding mutual attritional fight — which is where the Size-8 formation wants to be — Discipline checks do not fire. The large formation is designed to win the symmetric fight.

The asymmetric-loss strategy is correct. The question is whether players execute it correctly or slip into mutual attrition when the scene gets chaotic.

### Flowchart

```mermaid
flowchart TD
    A["Mass Battle: Löwenritter Heavy Infantry\nSize 8, Discipline 4, CP 4, Cohesion 4\nvs Crown Cavalry\nSize 4, Discipline 6, CP 5, Cohesion 5\n[PP-297: Discipline check fires only when unit loss > opposing loss by ≥1 in same Engagement Phase]"]
    A --> B["Cavalry tactical advantage:\nMobility — can choose Offensive disposition\nSpeed — can Withdraw to avoid engagement\nCP 5 vs CP 4 — slight combat pool edge\n\nLöwenritter tactical advantage:\nSize 8 — more Volley targets\nSize 8 — Phase 6 cascade harder to trigger\nDiscipline 4 — checks rarely in symmetric fight"]

    B --> C{Cavalry commander strategy}

    C -->|"Optimal: asymmetric harassment\nOffensive Cavalry vs Balanced Infantry\nCavalry Offence: 5D TN7 per engagement\nInfantry Defence: 4D TN7\nExpected Cavalry net advantage: ~0.5\nP(Cavalry inflicts more than Infantry this phase) ≈ 55%\nWith Overwhelming: Cavalry nets 2+ more → Discipline check fires\nOb for Infantry Discipline check: 4D vs Ob 4 — P(hold) ≈ 55%\nP(Formation Break per engagement) ≈ 0.45 × 0.45 ≈ 20% per Overwhelming exchange"| D["Over 5 Overwhelming exchanges:\nP(at least 1 Formation Break) ≈ 67%\nCavalry achieves formation disruption without\nentering mutual attrition\nSize 4 preserved while Size 8 fragments"]

    C -.->|"[NG-M] System Isolator:\n'Discipline 4 is low — every loss\nthey take triggers a Discipline check.\nPush them to take any losses at all.'"| E["Misread: Discipline check requires asymmetric loss\n[PP-297: symmetric losses do NOT trigger]\nPlayer pursues any-loss strategy:\nCavalry enters close engagement, accepts mutual losses\nBoth sides lose 1 Size in Engagement Phase\nNeither Discipline check fires\nSize 4 → 3, Size 8 → 7\nCavalry now at 3 vs 7: size disadvantage compounds\nCavalry Discipline 6 check fires (their loss was equal but cavalry is smaller —\nthe Phase still doesn't trigger per PP-297 if losses are equal)\nCavalry must withdraw having gained nothing"]

    C -.->|"[NG-P] Causal Inverter:\n'Their Discipline 4 is the weakness.\nAttack Discipline directly —\nuse Phase 3 Tactic cards to reduce it.'"| F["Discipline is a derived stability stat,\nnot a pool — it cannot be targeted directly\nTactic cards target: Cohesion, Morale, Size, CP\nNo Tactic card reduces Discipline directly\nPlayer spends Tactic card activation seeking\na 'reduce Discipline' option that doesn't exist\nTurn passes without Tactic benefit\nCorrect approach: trigger the Discipline CHECK\nnot reduce the Discipline value\nThe stat is the check target; the check is what\nneeds to fire (via asymmetric loss)"]

    C -.->|"[NG-Q] Threshold Chaser:\n'Get Infantry Size down to 5\n(half of 8 rounded up) — that's the\nmorale cascade threshold.\nJust need to hit that number.'"| G["Size 5 (Löwenritter) → Morale check Ob 2\n[mass_combat cascade: Size ≤ half → Morale check]\nPlayer pursues Size-reduction as primary goal\nwithout considering Discipline\nTo get Size 8 → 5 via symmetric attrition:\nCavalry also loses ~3 Size (Size 4 → 1)\n— numerically impossible; cavalry eliminated first\nThreshold is correct; path to threshold incorrect\nSymmetric attrition eliminates cavalry before reaching threshold"]

    C -.->|"[NG-N] Scale Conflator:\n'Löwenritter Military 5 means\ntheir individual units are Military 5.\nOur cavalry has CP 5 —\nthat matches their Military 5 stat.'"| H["Military faction stat ≠ unit CP\n[stage6: Military = max CP ceiling and starting Cohesion ceiling]\nLöwenritter Military 5: maximum CP a unit can have\nActual unit CP: determined by unit type and training\n— Heavy Infantry: CP 4 (standard)\nCavalry CP 5: already exceeds Infantry CP 4\nPlayer believes they're matched when they have CP advantage\nUnderestimates their actual tactical edge\nProceeds with excessive caution\n(Balanced disposition rather than Offensive)\nDamage output 20% lower than it could be"]

    D --> I["Optimal result: Formation Break in 5+ exchanges\nCavalry preserves ~3 Size\nLöwenritter disrupted — subsequent accounting:\nMilitary −1 (unit disrupted)\nStability check Ob 2 for Leadership Deviation\n(Löwenritter commander broke formation)"]
    E --> J["Mutual attrition: Cavalry eliminated\nLöwenritter reduced but functional\nDiscipline never checked — symmetric fight\nCavalry spent tactical advantage on a fight\nthey were structurally unlikely to win"]
    G --> K["Cavalry eliminated before reaching Size threshold\nThreshold correct; approach fatal\nThe threshold chaser identified the right endpoint\nand chose a path that destroyed the tool\nbefore reaching it"]
```

### Footer

Emerges from the Discipline asymmetry precondition (PP-297) interacting with standard attrition strategy intuitions. Most wargame experience tells players "inflict any losses to trigger morale effects." PP-297 specifically requires asymmetric losses. The arc tests whether players read the precondition or assume symmetric loss works. Arc shape: 1 battle scene; consequence extends if cavalry is eliminated (Löwenritter retain military advantage). Most impactful in Hybrid mode where mass battle feeds back to BG faction stats.

**Structural misreader findings:**
- NG-M (System Isolator): The Discipline check trigger is correctly identified as "Size loss > Discipline threshold." The asymmetry precondition (PP-297) is the second half of the rule that the Isolator misses. Within the mass combat system, the Isolator has read the condition correctly but not the full condition.
- NG-P (Causal Inverter): Discipline is a target value for checks, not a pool to drain. The Causal Inverter tries to reduce the stat rather than trigger the check. The distinction between "reduce a stat" and "trigger a check that tests the stat" is the architectural blind spot.
- NG-Q (Threshold Chaser): The Size-half threshold is real. The path to it via symmetric attrition is fatal because cavalry is smaller. The chaser identified the correct goal and the impossible route simultaneously.
- NG-N (Scale Conflator): Military faction stat ≠ unit CP. The faction's Military ceiling sets maximum unit quality; it doesn't describe the actual unit's CP. The Conflator is underestimating their CP advantage because they think the enemy "Military 5" means enemy unit CP 5.

---

## ARC 20: The Diverge Cascade

### Mechanical Seed
Two factions simultaneously contest the same political question via separate Contest scenes in the same season → each generates a Diverge state (PP-271) in their respective scenes → Diverge states accumulate in the same NPC's Conviction Track across scenes → three consecutive Diverge states across scenes → forced Unmask fires (PP-282 maximum 10 exchanges / PP-271 max 3 consecutive Diverge) → NPC exits the political question entirely → the faction that was winning the position (closer to success on Conviction Track) loses access to the decision-making context.

### Narrative

The players are not the only people in the Contest. Two factions are simultaneously arguing the same political question — Hafenmark and Crown are both trying to convince Parliament of the same policy direction, each through separate scenes. Neither knows the other is running a parallel Contest this season. The NPC at the centre (a Parliamentary moderator, a swing vote on the council) is receiving competing arguments from two different directions.

Each Contest generates Diverge states independently. The moderator is not confused by any individual argument — each is coherent on its own terms. The problem is that across two scenes, the moderator has now experienced six exchanges arguing competing positions with equal success rates. The Conviction Track hasn't moved significantly in either direction. Three consecutive Diverge states have accumulated across the combined scene count. Forced Unmask fires: the moderator withdraws from the question entirely. Neither faction wins. The policy question goes unresolved.

The players, who were winning position in the first scene, lose access to the decision because a second Contest they didn't know about saturated the NPC's tolerance for the question.

### Flowchart

```mermaid
flowchart TD
    A["Same political question: two factions contesting simultaneously\nScene 1: Players (Crown) vs Parliamentary Moderator NPC\nScene 2: Hafenmark vs same Parliamentary Moderator NPC\n[Neither faction knows the other is running a Contest this season]"]
    A --> B["Scene 1 (Crown Contest):\n3 exchanges. Conviction Track moves 2 positions toward Crown.\n1 Diverge state fires (exchange 2: both Success+, margin ≤ 1)\nScene ends — Crown in winning position"]
    B --> C["Scene 2 (Hafenmark Contest, same season):\n3 exchanges. Conviction Track moves 1 position back (contested terrain).\n2 more Diverge states fire (exchanges 1 and 3 match condition)\nTotal across both scenes: 3 consecutive Diverge states accumulated"]
    C --> D["PP-282 + PP-271: 3 consecutive Diverge → forced Unmask fires\nNPC (Parliamentary Moderator) exits the political question\nConviction Track position: Crown was winning (2 ahead)\nBut NPC exits before decision resolves\nPolicy question unresolved — passed to full Parliament vote\nCrown loses personalised advocacy access they were winning"]

    D --> E{Players respond}

    E -->|"Optimal: identify second Contest immediately\nCircles Ob 2 to determine who else lobbied this season\nDomain Action: Intel to flag Hafenmark activity"| F["Players learn Hafenmark ran parallel Contest\nCoordination possible: signal Hafenmark to delay\ntheir Scene 2 by one season\nBoth Contests can proceed without saturation\nNPC available next season at Conviction Track: Crown +2 carry forward"]

    E -.->|"[NG-M] System Isolator:\n'We won our Contest exchanges.\nThe Conviction Track shows Crown +2.\nThe decision should resolve in our favour.'"| G["Diverge cascade across scenes not tracked by players\nPlayers assume their Contest win is sufficient\nNPC exits before decision resolves\nPlayers: 'What happened? We won all our exchanges.\nThe track was in our favour.'\nCross-scene Diverge accumulation is the mechanic\nthey didn't model — it's a session-spanning count,\nnot resetting between scenes"]

    E -.->|"[NG-N] Scale Conflator:\n'Parliament's vote resolves this —\nuse the Parliamentary Vote mechanic\n(Domain Action: Influence pool)\ninstead of Contest.'"| H["Parliamentary Vote mechanic (ED-053) is\na BG-mode tool for faction-level vote resolution\nIn TTRPG mode: Parliamentary outcome is\ndriven by personal advocacy (Contest) first,\nthen full Parliament vote if advocacy fails\nPlayers abandon Contest midway to use BG mechanic\nin TTRPG context\nGM: 'The Parliamentary Vote fires at accounting,\nnot in scene. Your personal advocacy scene is\nwhat you're in right now.'\nScene ends inconclusively — advocacy abandoned"]

    E -.->|"[NG-P] Causal Inverter:\n'The NPC exited because we\ndidn't win enough exchanges.\nRun more exchanges to win them back.'"| I["Forced Unmask is final for this scene\n— NPC has exited the question, not the Contest\nPlayers attempt to re-engage the NPC\nin the same scene to 'win them back'\nGM: 'She's not engaging on this topic anymore this season.'\nForced Unmask means NPC unavailable for\nthis specific political question until next season\nPlayer runs 'more exchanges' against a closed door\nSpend Composure/Momentum on null interactions"]

    E -.->|"[NG-Q] Threshold Chaser:\n'We need Conviction Track +5 to win.\nWe have +2. Run more exchanges\nuntil we hit +5 — that resolves it.'"| J["Scene is complete (3 exchanges run, NPC exits)\nThreshold Chaser attempts to reopen the scene\nfor additional exchanges toward target\nGM: 'The scene has ended. The NPC exited.'\nThreshold chaser doesn't model that\nscene exit terminates access to the mechanic —\nthe Contest wasn't 10 exchanges (PP-282 limit);\nit was 3 exchanges + forced Unmask via Diverge count\nThreshold was correct; access is what was lost"]

    F --> K["Coordinated lobbying: both Contests succeed\nNPC available next season at Crown +2 carry forward\nHafenmark delays by 1 season\nPolicy resolved next season\nMinor cost: 1 season delay\nMajor benefit: access preserved"]
    G --> L["NPC exits; policy question to full Parliament\nCrown loses personalised advocacy advantage\nParliament vote: Influence 5D vs Ob 3 (Crown default)\nP(Crown wins Parliament vote) ≈ 72%\nvs P(Crown wins Contest) ≈ 88% (won position)\nCross-scene Diverge cost: ~16pp win probability"]
    I --> M["Momentum and Composure spent on null interactions\nScene already closed — no mechanical effect\nPlayer expended resources on an inaccessible mechanic\nForced Unmask is not 'reluctance' — it is scene termination"]
```

### Footer

Emerges from the Diverge state's cross-scene accumulation rule (PP-271: max 3 consecutive) interacting with two parallel Contests targeting the same NPC in the same season. No player designed the Hafenmark Contest — it fires from Hafenmark's Institutional Tendency (constitutional procedure). Arc shape: 1-season window; 1-season consequence. Demonstrates the cross-system interaction between Contest mechanics and faction Institutional Tendency.

**Structural misreader findings:**
- NG-M (System Isolator): Contest wins are scene-local. Conviction Track position carries forward; NPC access does not if Forced Unmask fires. The Isolator models the Contest correctly within its scene but doesn't track cross-scene Diverge accumulation as a session-spanning counter.
- NG-N (Scale Conflator): TTRPG personal advocacy scenes and BG Parliamentary Vote are sequential, not interchangeable. The Scale Conflator treats the BG mechanic as usable in TTRPG context mid-scene. The correct sequence is: personal advocacy (Contest) → if advocacy fails, full Parliament vote at Accounting.
- NG-P (Causal Inverter): Forced Unmask is not a measure of exchange count — it is a measure of Diverge count. Running more exchanges doesn't undo a Forced Unmask. The Causal Inverter treats "exited the question" as "lost the lead," which is a recoverable position. It isn't.
- NG-Q (Threshold Chaser): Conviction Track +5 is the right target. Access to the NPC is what was lost. The Threshold Chaser correctly identifies the target and doesn't model that the tool (Contest with this NPC) is no longer available this season.

---

## Cross-Arc Interaction Table (SIM-ARC-04)

| | ARC 16: Certainty | ARC 17: Composure | ARC 18: Weaving | ARC 19: Discipline | ARC 20: Diverge |
|---|---|---|---|---|---|
| **ARC 16: Certainty** | — | Certainty 5+ generates Diverge states in social (ARC 20 risk rises); Certainty 0 removes practitioner from ARC 17 Contest | Community Weaving is a Certainty-safe operation (no Coherence cost at Personal scale) — scheduling it can protect Certainty | Practitioner at Certainty 3 cannot reliably direct ARC 19 Thread ops in mass battle | Certainty-driven Diverge states can trigger ARC 20 Forced Unmask even without parallel Contests |
| **ARC 17: Composure** | Himlensendt Contest loss (position) doesn't impair him — he restarts at Composure 12 next scene, contributing to ARC 16 TC growth | — | Himlensendt unimpaired means Church Thread suppression continues — Community Weaving faces ongoing Inquisitor pressure (ARC 18 harder) | Himlensendt Contest win means Church can pursue Domain Actions freely — ARC 19 Löwenritter military engagement more likely | Himlensendt generates Diverge states in Contest due to Thread-factual vs doctrine mismatch — ARC 20 interaction possible |
| **ARC 18: Weaving** | Community Weaving protects RS — but if Certainty drops, Weaving efficiency unchanged (Certainty ≠ Thread effectiveness) | RS above 55 enables Himlensendt's institutional authority (Church stronger at RS > 50) — maintaining RS keeps the problem | — | Mass battle Thread ops (ARC 19) compete with Community Weaving for contact window — battlefield and restoration in direct competition | RS above threshold reduces Church anxiety about Thread — fewer Inquisitor actions, fewer ARC 20 Contest opponents |
| **ARC 19: Discipline** | Practitioner at Certainty 3 is less reliable for ARC 19 precision targeting (Thread Diagnosis before Pulling general) | ARC 19 loss (cavalry eliminated) means Crown Military −1 — Crown Mandate drops — ARC 17 Contest position harder to maintain | Community Weaving interrupted by ARC 19 battle demands — RS declines during battle seasons | — | ARC 19 Löwenritter victory means Löwenritter Military dominant — Parliament moderator (ARC 20) faces stronger Löwenritter faction pressure |
| **ARC 20: Diverge** | Diverge cascade (ARC 20 NPC exits) sends policy to Parliament — Crown loses Contest advantage — Certainty practitioner's social contribution matters less (ARC 16) | Himlensendt is likely to participate in Parliamentary fallback (ARC 20) — his Composure 12 makes him the strongest voice | RS above 55 reduces Church urgency — Himlensendt less aggressive in ARC 20 Parliament — fewer parallel Contests from Church | Löwenritter Parliament presence (after ARC 19 victory) adds competing voice — more Diverge risk | — |

**Convergence risk (SIM-ARC-04):** NG-M applied across all four arcs simultaneously produces: Certainty draining unchecked (no Thread rest, ARC 16), Contest positions won but NPC unimpaired (ARC 17), RS declining at full rate (ARC 18 Community Weaving not scheduled), Discipline check misunderstood (ARC 19 cavalry eliminated), Diverge cascade untracked (ARC 20 NPC exits). All five failures are independent System Isolator errors that compound: RS collapse activates Church Intel, eliminating the practitioner from social play (ARC 17), degrading the one mechanic that could restore RS (ARC 18), while the military loss (ARC 19) strengthens Löwenritter faction pressure in the Parliament vote (ARC 20) that the players defaulted to by failing the Contest (ARC 20).

**Systemic finding (SIM-ARC-04):** Structural misreaders cluster around **definitional scope failures** — the player's model of a mechanic is correct within a narrower scope than the mechanic actually operates. The System Isolator (NG-M) has the most pervasive failure mode because isolation is the default cognitive approach to complex rule systems. Every arc in this batch has at least one NG-M failure path, and all are caused by the same error applied to different mechanics: "this mechanic operates in this system and only this system."

---

## Simulation Findings Summary (SIM-ARC-04)

| Finding | Arc | Mechanic | Severity |
|---------|-----|----------|----------|
| F-ARC4-01 | ARC 16 | NG-M: Thread ops during "rest" prevent Certainty recovery; player scopes rest as combat/social, not Thread | Critical — Certainty drains to 0 |
| F-ARC4-02 | ARC 16 | NG-R: Spirit-Certainty phantom synergy; PP-289 explicitly states Spirit unrelated; 2 seasons wrong investment | High — explicitly contradicted by params |
| F-ARC4-03 | ARC 16 | NG-P: Avoiding social scenes treats Diverge symptom; Southernmost exposure (cause) continues | Medium — partial mitigation only |
| F-ARC4-04 | ARC 16 | NG-Q: Certainty 5 treadmill; safe threshold is 7, not 5; drain rate identical below 7 | High — wrong threshold identification |
| F-ARC4-05 | ARC 17 | NG-M: Track position victory ≠ NPC impairment; Himlensendt restarts at Composure 12 every scene | High — most common player assumption |
| F-ARC4-06 | ARC 17 | NG-N: Composure ≠ faction Stability; Rattling Himlensendt doesn't touch Church institutional stats | High — parallel track confusion |
| F-ARC4-07 | ARC 17 | NG-O: Combat Pool cannot contribute to Contest rolls; overestimates damage capacity | Medium — illegal pool addition |
| F-ARC4-08 | ARC 17 | NG-P: Church Stability doesn't feed Himlensendt's Contest pool; 2 seasons correct action for wrong reason | Medium — right action, wrong model |
| F-ARC4-09 | ARC 18 | NG-M: Community Weaving requires active contact window; cannot be performed as "downtime recovery" | Critical — zero RS restoration |
| F-ARC4-10 | ARC 18 | NG-R: Belief achievement → RS is most plausible phantom synergy; philosophically coherent, mechanically absent | High — seductive wrong model |
| F-ARC4-11 | ARC 18 | NG-P: Moving from Southernmost treats secondary drain; Thread ops are primary; RS still declines at 90% | Medium — minor improvement, major cause unaddressed |
| F-ARC4-12 | ARC 18 | NG-Q: RS spike via 3 Weaves decays in 2 scenes; treadmill vs sustainable rate | Medium — threshold achieved; rate unchanged |
| F-ARC4-13 | ARC 19 | NG-M: Discipline check requires asymmetric loss; symmetric attrition (any loss) does not trigger | Critical — cavalry eliminated on wrong strategy |
| F-ARC4-14 | ARC 19 | NG-P: "Reduce Discipline stat" vs "trigger Discipline check"; no Tactic card targets the stat directly | Medium — turn wasted seeking non-existent option |
| F-ARC4-15 | ARC 19 | NG-Q: Size threshold (half) correct; symmetric attrition path eliminates cavalry before reaching it | High — correct target, self-defeating path |
| F-ARC4-16 | ARC 19 | NG-N: Military faction stat ≠ unit CP; Scale Conflator underestimates own CP advantage; excess caution | Low — underperforms but doesn't lose |
| F-ARC4-17 | ARC 20 | NG-M: Cross-scene Diverge count not modelled; assumed Contest win is sufficient; NPC exits | High — session-spanning counter missed |
| F-ARC4-18 | ARC 20 | NG-N: TTRPG Contest and BG Parliamentary Vote are sequential, not interchangeable | Medium — abandons winning position |
| F-ARC4-19 | ARC 20 | NG-P: Forced Unmask ≠ exchange count loss; running more exchanges against closed NPC access | Medium — resource burn on null interactions |
| F-ARC4-20 | ARC 20 | NG-Q: Conviction Track target correct; access to NPC is what was lost; threshold reachable next season | Low — correct model, wrong timing |

**Test ID:** SIM-ARC-04
**Mechanics:** Certainty track (PP-289), Composure/Rattled redesign (PP-266), Community Weaving (PP-296), Discipline asymmetry precondition (PP-297), Binding Ops (PP-293), Diverge state (PP-271), Contest forced resolution (PP-282), Hybrid TC clamp (PP-283), Reach terminology (PP-290 — contextual)
**Mode:** TTRPG primary; mass combat (ARC 19) Hybrid-applicable
**Temporal:** Multi-season; ARC 16 ongoing; ARC 17 per-scene; ARC 18 ongoing; ARC 19 single battle; ARC 20 single season
**Tracks:** Certainty, Composure, RS, Discipline, Conviction Track, Diverge counter
**Factions:** Crown, Church, Hafenmark, Löwenritter
**NPCs:** Himlensendt, Parliamentary Moderator (generic), Löwenritter commander (generic)
**Archetypes:** NG-M through NG-R (all six structural misreader archetypes)
