# Valoria Emergent Arcs — Batch 02
## Generated: 2026-04-08 | Source reads: params_factions.md, params_core.md, params_threadwork.md, params_debate.md, params_mass_combat.md, glossary.md, canonical_sources.yaml
## Framework typology: RS decay spiral · Debate outcome cascading into Mandate collapse · Mass battle aftermath · Thread Tension as slow extinction clock
## Prior arcs checked: gm_ref/arcs_01_04_nongreedy.md — 4 arcs. No duplication.

---

## Arc 5: The Quiet Fracture

**Primary mechanics:** Rendering Stability (RS) baseline decay (−1/year, PP-255), Thread operations (cumulative RS cost), Theocracy Counter (TC) passive advance (+1/season, PP-402), Weaving scale escalation
**Primary factions:** Church, Varfell
**Arc shape:** 3 seasons + Year-End. Open spiral — no natural close without player action.

---

### Narrative

The world is not breaking. That is the problem. If it were breaking in a way anyone could point to, someone would respond. Instead the players keep hearing two things said in the same week by people who have never spoken to each other: that the winters feel longer than they used to, and that the Church's healing work has never been more effective.

Both statements are true. Both emerge from the same mechanic. Every Structural Weaving the Church performs — and there have been three this year, Ob 8 each, in territories where the Restoration Movement's presence has made Thread-adjacent activity symbolically important — costs two points of Rendering Stability (RS) on Failure, one on Partial. The Church's practitioners are not failing catastrophically. They are partially succeeding, consistently, at scale, which is worse. The cumulative drain is invisible in any single operation and obvious in retrospect, across four seasons of accounts.

Varfell knows. Or rather, Varfell's Truthseekers know, and Varfell's political structures have not yet decided whether this knowledge is a lever or a liability. Their consequentialist ethical framework weights future outcomes — boosted Future genre in debate, per the faction parameters — which means they see the ten-season trajectory and are running the calculation on whether revealing it helps them more than it hurts the Church. That calculation has been running for two seasons. It has not yet produced an output.

Meanwhile the year-end comes, Rendering Stability ticks down by its baseline point, and everyone in the room feels slightly more tired than they expected to feel.

---

### Mechanical Causal Chain

```mermaid
flowchart TD
    A["SEED\nRS = 55 (TTRPG start 60, −5 from prior ops)\nChurch commences Structural Weaving campaign\nOb 8, Pool ~9–11D (Spirit + Thread Pool Score)"]
    B["SEASON 1\n3× Structural Weaving attempts\nExpected: 2× Partial (RS −1 each), 1× Success\nNet RS drain: −2. RS: 55→53\nTC passive +1 (1→2 TTRPG)"]
    C["Year-End\nRS baseline decay −1 (PP-255)\nRS: 53→52"]
    D["SEASON 2\nVarfell Truthseeker completes analysis\nEDITORIAL decision point: reveal or hold?"]
    E{"Varfell reveals to players?"}
    F["YES: Players have RS trajectory data\nDebate opportunity opens — Church vs Varfell\n(Future genre, Varfell boosted × 1.5)\nConviction Track starts neutral (5)"]
    G["NO: Varfell holds data as leverage\nApproach Church leadership privately\nMandatory Domain action: Mandate 4 vs Church Mandate 6\nOb = 6. Expected: Failure likely"]
    H["Debate resolves\nVarfell wins → Church agrees to Weaving moratorium\nRS drain halted. TC passive continues."]
    I["Debate fails (Church wins)\nChurch Weaving continues\nRS: −2–4 per season\nAt RS ≤ 40: Weaving Failures trigger Gaps"]
    J["Domain action Failure\nVarfell Stability −1 (PP-403)\nChurch now aware of Varfell analysis\nEDITORIAL: Church response options"]
    K["RS reaches 40\nWeaving Failure now triggers Shifting (Object scale)\nRS ≤ 20: Gaps on Failure\nPlayers begin witnessing physical instability"]
    L["RESOLUTION A\nMoratorium + negotiated Weaving protocol\nRS stabilises above 40\nTC continues rising — different crisis"]
    M["RESOLUTION B\nNo intervention. RS crosses 20.\nGaps manifest in territories.\nRupture clock visible to all factions."]
    N["RESOLUTION C\nVarfell-Church private deal\nThread knowledge suppressed\nPlayers learn of it through Rupture symptoms"]

    A --> B --> C --> D --> E
    E --> F --> H --> L
    H --> I --> K --> M
    E --> G --> J --> N
    K --> M
```

**Emergent logic:** No player designed this. The Church's ritual success rate, combined with Ob 8's expected partial-success frequency at realistic pool sizes, produces a structural RS drain that looks like competence. The gap between what the Church intends (healing) and what the world records (destabilisation) is the arc.

---

## Arc 6: The Debate That Won the Wrong Thing

**Primary mechanics:** Debate system (Conviction Track, Genre weights, Composure), Mandate stat, Stability cost on Domain action Failure (PP-403), TC Suppress (PP-402)
**Primary factions:** Crown, Church, Hafenmark
**Arc shape:** 2-season setup, 1-season resolution event, 1-season aftermath. Linear with branching aftermath.

---

### Narrative

Hafenmark called for the debate. They were right to. The question on the floor — whether the Church's arbitration courts in southern territories constitute a parallel legal jurisdiction, and whether that jurisdiction is subject to parliamentary oversight — was exactly the question that needed public resolution. Hafenmark's orators are strong. Their Categorical Imperative ethical framework gives them a boosted Past genre weight of 1.5, and the historical record of Church encroachment is long and well-documented. They won.

The Conviction Track moved to eight. The chamber ruled for parliamentary oversight. The Church accepted. Three witnesses in the gallery noted that the Confessor representing the Church had agreed very quickly, and in agreeing had framed the oversight mechanism in terms that, reading the formal record later, did not actually constrain anything currently operational. He had conceded the principle and retained the practice. The orators who had won did not immediately recognise what they had lost.

What follows is not a Church counterattack. It is a Crown crisis. The Crown's Virtue Ethics framework (Present genre boosted × 1.5) had positioned it to arbitrate the outcome — the Royal Decree that would have implemented the ruling. That implementation required a Domain action: Mandate 5 vs Church Mandate 6, Ob 6, TN 7. Probability of Success at this pool is roughly 35%. The roll failed. Stability −1 (PP-403). The Crown's implementation attempt failed publicly, visibly, and the implementation mechanism was now poisoned — a second attempt would raise Ob by the consecutive-use rule.

Hafenmark won the debate and created a Crown weakness they now have to decide whether to exploit or repair.

---

### Mechanical Causal Chain

```mermaid
flowchart TD
    A["SEED\nHafenmark calls Debate: Church arbitration courts jurisdiction\nConviction Track starts at 5 (neutral)\nAudience: Crown (Present ×1.5) + Hafenmark (Past ×1.5)\nChurch not orating — audience only (Stability 5)"]
    B["EXCHANGE RESOLUTION\nHafenmark orators 10D (Cognition 5 ×2) vs Church representative 8D\nPast genre boosted ×1.5 for Hafenmark\nExpected: Hafenmark wins in 4–6 exchanges\nConviction Track → 8. Hafenmark victory."]
    C["CHURCH RESPONSE\nAccepts ruling. Confessor frames concession narrowly.\nNo Composure 0 — Church concedes voluntarily at CT=8.\nKey: concession language creates implementation ambiguity\n[EDITORIAL: ED-322 — exact language is a design decision]"]
    D["Crown Domain Action: Implement ruling\nPool: Mandate 5 (Crown) + History bonus\nOb = Church Mandate 6 = Ob 6 at TN 7\nP(Success) ≈ 35% at ~9D"]
    E{"Implementation roll result"}
    F["SUCCESS\nRuling implemented. Church courts formally subordinated.\nTC Suppress available to Crown at −1 Ob next season.\nChurch begins quiet reorganisation."]
    G["FAILURE\nCrown Stability −1 (PP-403)\nConsecutive Royal Decree: +1 Ob next attempt\nChurch arbitration continues unchanged\nHafenmark: debate win without enforcement"]
    H["Hafenmark choice: support Crown retry?"]
    I["YES: Joint Domain action\nHafenmark Mandate 4 + Crown Mandate 5 pooled\nOb raised by 1 (consecutive) = Ob 7\nP(Success joint) ≈ 55%"]
    J["NO: Hafenmark uses Crown weakness\nApproaches Guilds (Influence 4) for economic coalition\nMandatory EDITORIAL: what Hafenmark wants"]
    K["Joint Success\nRuling enforced. Church reorganises around it.\nTC passive unchanged (+1/season).\nHafenmark-Crown relationship strengthened."]
    L["Joint Failure\nBoth factions Stability −1\nChurch arbitration system now functionally permanent\nTC accelerates: +2/season (Assert not needed — courts provide)"]
    M["Hafenmark-Guilds coalition\nEconomic pressure route opens\nSeparate arc branch — political realignment"]

    A --> B --> C --> D --> E
    E --> F
    E --> G --> H
    H --> I --> K
    I --> L
    H --> J --> M
```

**Emergent logic:** The Debate system produces winners and outcomes, not implementations. The gap between a won Conviction Track and a successful Domain Action is the arc. The Church did not engineer this — they simply knew the gap existed and positioned their concession inside it.

---

## Arc 7: The Army That Stayed

**Primary mechanics:** Mass combat (Discipline, Morale, Phase 6 Cascade), Institutional Pressure (IP), Faction Stability, Domain actions post-battle
**Primary factions:** Crown, Löwenritter, Altonian Empire (non-player character faction)
**Arc shape:** 1-season mass battle event, 3-season political aftermath. Branching based on Discipline check outcomes.

---

### Narrative

The battle was a victory. That is the formal position, and formally it is not wrong. The Altonian probing force — two units, Size 4 and Size 3, sent to test the northern pass — was driven back. Crown units held the line. Institutional Pressure (IP) dropped from 32 to 27, a genuine strategic gain. The Löwenritter Templars, whose presence was decisive in Phase 4 (Offensive Thread collapsed one Altonian unit's Discipline to zero), are heroes.

The players start to feel something is wrong in the second season. The Löwenritter have not left. Their Battle Leader cites ongoing threat assessment, continued Altonian mobilisation on the far side of the pass, the practical wisdom of not dissolving a force that took three seasons to assemble. All of this is accurate. None of it explains why their camp has expanded south rather than north. Why they are buying grain locally rather than drawing from Church supply lines. Why the Crown garrison commander cannot get a meeting.

What happened mechanically: in Phase 6 Step 2, two Löwenritter units failed their Discipline checks (Discipline 4, Command 3, pool = min(4,3)+3 = 6D, Morale Ob 3, TN 7 — P(Success) ≈ 70%, so both failing has P ≈ 9% — rare, but this is a campaign). Failed Discipline checks in Phase 6 apply a Morale condition. That condition carries into Reform and was not fully resolved at battle end. The Löwenritter units are mechanically in a sustained high-alert state. Their Battle Leader is not fabricating the threat; his units cannot stand down without a formal Morale restoration process (Rally action, Command check, Ob 2) that he has not initiated because standing down removes his justification for presence.

He is trapped by his own units' state. The players are watching a political crisis caused by a 9% probability event in Phase 6 Step 2.

---

### Mechanical Causal Chain

```mermaid
flowchart TD
    A["SEED\nMass battle: Crown + Löwenritter vs Altonian probe\nLöwenritter: 2 units. Discipline 4, Command 3, Power derived from Size.\nPhase 4: Offensive Thread collapses Altonian unit 1 Discipline → 0"]
    B["Phase 6 Step 2: Discipline checks\nPool = min(Discipline,Command) + Command = min(4,3)+3 = 6D\nMorale Ob 3, TN 7. P(both fail) ≈ 9%\n[Outcome: both units fail]"]
    C["Phase 6 Step 4: Rally opportunity\nBattle Leader does not attempt Rally\n(victory declared; Reform Phase 7 covers non-engaged units only)\nMorale condition persists into post-battle"]
    D["Season 1 Aftermath\nLöwenritter remain deployed\nBattle Leader: 'Altonian threat not resolved'\nIP = 27. Crown Domain action to investigate: Ob = Löwenritter Mandate 3"]
    E{"Crown investigates?"}
    F["YES: Domain action\nOb 3, TN 7\nPartial or better: players learn of Morale condition"]
    G["NO: Löwenritter presence normalises\nSeason 2: begins grain purchasing (Wealth drain)\nCrown Stability check trigger if Löwenritter cross into Crown territory"]
    H["Players learn Morale condition\nOption: assist Rally (personal scene, Command Ob 2)\nOption: Request formal withdrawal through Church mediation"]
    I["Rally succeeds\nLöwenritter Morale restored\nWithdrawal possible. Diplomatic resolution.\nIP drift resumes normal rate."]
    J["Rally fails or not attempted\nSeason 3: Löwenritter establish supply depot\nPublic Instability (PI) −1 (BG: presence without Crown sanction)\nLöwenritter become a faction problem, not a military one"]
    K["Church mediation\nConviction Track: Crown vs Löwenritter withdrawal terms\nLöwenritter Stability 4 → resistance = ceil(4/4) = 1\nChurch gains Influence regardless of outcome"]
    L["RESOLUTION A\nRally + withdrawal\nLöwenritter relationship maintained\nCrown-Löwenritter trust +1 (qualitative)"]
    M["RESOLUTION B\nLöwenritter entrench\nCrown must treat as Domain action threat\nFaction conflict opens"]
    N["RESOLUTION C\nChurch mediates withdrawal terms\nChurch Influence 6→7 in affected territory\nTC +1 bonus from mediation role"]

    A --> B --> C --> D --> E
    E --> F --> H
    H --> I --> L
    H --> J --> M
    E --> G --> J
    H --> K --> N
```

**Emergent logic:** A 9% probability event in Phase 6 Step 2 generates a three-season political crisis. No player intended this. The Battle Leader is not a villain — he is a commander whose units are in a mechanical state he cannot resolve without admitting the problem exists. The arc is caused by the interaction of Discipline check probabilities with the absence of a mandatory post-battle Rally protocol.

---

## Arc 8: What the Guilds Know

**Primary mechanics:** Faction stats (Wealth 6, Influence 4), Domain actions (Intel), nine political axes (Information: Transparency vs Secrecy), TC Suppress eligibility, Stability costs
**Primary factions:** Guilds, Crown, Church
**Arc shape:** 4 seasons. Slow accumulation → forced decision → aftermath. No mass violence.

---

### Narrative

The Guilds do not have an Intel stat in the current parameters. The table shows a dash. This is not an oversight in the design — it reflects the Guilds' actual institutional structure: they do not maintain a centralised intelligence apparatus. They maintain trade networks. Trade networks produce information as a byproduct, at scale, without anyone intending it.

What the players observe is that Guild factors seem to know things. Not secrets — nothing dramatic. They know which Crown officials have been travelling to which territories. They know which Church properties have been receiving unusually large timber orders. They know that two of the three Löwenritter's senior commanders have family in Hafenmark. They know these things the way that people who talk to everyone know things: obliquely, incidentally, with no single source that could be interrogated or suppressed.

The Church has noticed. The Theocracy Counter (TC) passive advance (+1/season, PP-402) is a mechanism the Church understands — they can see the counter, roughly, from the inside. What they cannot see is what the Guilds are doing with the rate-of-advance data. Someone is tracking how seasons with active Crown Suppress actions correlate with seasons in which Church territorial reach expands at half the expected rate. That someone has a ledger. The Church wants the ledger.

The arc is not about whether the Church can get the ledger. It is about what the Guilds will trade it for.

---

### Mechanical Causal Chain

```mermaid
flowchart TD
    A["SEED\nGuilds Wealth 6, Influence 4, Intel: —\nTrade network produces TC rate-of-advance data organically\nChurch becomes aware (Mandate 6, Influence 6 — detection via pastoral networks)"]
    B["Season 1: Church opens contact\nDomain action: Influence 6 vs Guild Stability 5 (as proxy Ob)\nOb = ceil(5/4) = 2\nP(Success): high. Church establishes dialogue."]
    C["Season 2: Church offer\nInformation suppression in exchange for:\nGuild tax exemption in 2 Church-administered territories\nChurch arbitration exclusion for Guild contracts\nGuild choice: accept or escalate"]
    D{"Guild response"}
    E["ACCEPT\nLedger exchanged under terms\nChurch gains TC data — can model Crown Suppress timing\nGuild Influence grows via Church access\nCrown unaware"]
    F["DECLINE — approach Crown\nGuild offers data to Crown\nCrown Domain action: Mandate 5 vs Ob 2\nSuccess: Crown gains TC insight. Suppress actions optimised."]
    G["DECLINE — leverage publicly\nGuild factor reads ledger in Parliament session\nPublic Instability (PI) −1 (BG) from institutional exposure\nChurch forced to respond in public"]
    H["Crown gains TC insight\nSuppress actions: Ob 5 instead of 6 (intel bonus)\nP(Suppress success) rises from ~30% to ~55%\nTC advance slows structurally"]
    I["Church responds to public reveal\nExcommunication threat: Crown Mandate −1 if Crown uses data\nDebate opens: Transparency vs Church authority\nConviction Track starts at 5"]
    J["TC data absorbed quietly\nChurch adjusts: Assert only in seasons Crown cannot Suppress\nNet TC gain slightly accelerates"]
    K["RESOLUTION A\nChurch-Guild deal: quiet suppression\nCrown uninformed\nGuild positioned as Church ally — dangerous at TC 60"]
    L["RESOLUTION B\nCrown-Guild alliance\nTC advance slows\nGuild exposed to Excommunication risk"]
    M["RESOLUTION C\nPublic debate + Conviction Track resolution\nGuild Influence +1 from visibility regardless of outcome"]

    A --> B --> C --> D
    D --> E --> J --> K
    D --> F --> H --> L
    D --> G --> I --> M
```

**Emergent logic:** The Guilds have no Intel stat because they do not need one. The arc emerges from the structural interaction of Wealth 6 (network reach), the TC passive advance mechanic, and the Church's Mandate 6 detection capacity. No one designed the information asymmetry — it is a product of which stats are present and which are absent.

---

## Arc 9: The Practitioner Who Stopped

**Primary mechanics:** Thread Sensitivity (TS) accumulation, Coherence track (10→0), Rendering Stability (RS) shared cost, PP-261 (Coherence 0 → Non-Player Character transition), Faction Stability (Varfell)
**Primary factions:** Varfell
**Arc shape:** Slow burn. 4–6 seasons. Personal arc that becomes a faction crisis.

---

### Narrative

The Truthseeker stopped operating six months ago. No announcement. No explanation that anyone outside Varfell's inner circle received. She had been Varfell's primary Thread practitioner — Thread Sensitivity 72, which put her Thread Pool Score at 7, a genuine strategic asset — and then she was in the archive, doing research, not doing operations.

The players begin to notice the absence. Situations where a practitioner would have been useful resolve differently. A Rendering Stability event that would have been caught with a Weaving goes uncaught. Varfell's Mandate score holds — she was never the source of their political authority — but their capacity to respond to Thread-adjacent crises quietly degrades.

What happened is this: her Coherence is at 3. She knows it. She can feel the threshold approaching in the way that Valoria's Thread mechanics make legible — the practitioner's experience of operating in a substrate that is recording her. At Coherence 0, the rule is clear (PP-261): she becomes a Non-Player Character. Fully functional, completely herself in every way that anyone outside her head can verify, but the part of her that chooses is gone. She has not told Varfell's leadership because there is no political frame in which that information helps her. She has not stopped permanently — she is rationing operations, holding Coherence at 3 as a floor, trying to complete something before the transition takes it from her.

What she is trying to complete is the question of what she found.

---

### Mechanical Causal Chain

```mermaid
flowchart TD
    A["SEED\nVarfell Truthseeker: Thread Sensitivity 72, Coherence 3\nOperating at Coherence 3: each failed op risks −1 Coherence\nDecision: stop operating publicly, continue privately\nRS: 52 (post prior arcs)"]
    B["Season 1: Absence noted\nVarfell does not deploy practitioner for routine Weaving\nRS drain from Church ops continues unchecked\nVarfell Stability: 4 (unaffected directly)"]
    C["Private operation: what is she researching?\n[EDITORIAL: design space — options:\nevidence of RS manipulation / Thread Tension source /\nhistorical Rupture precedent / identity of another practitioner]"]
    D{"Players investigate Truthseeker absence?"}
    E["YES: Attunement roll, Ob 2, TN 7\nSuccess: players learn she is present but withdrawn\nOverwhelming: players detect Thread activity in archive"]
    F["NO: Absence normalises\nSeason 3: Varfell requests Church practitioner assistance\nChurch Influence in Varfell territory +1 if agreed\nVarfell cedes Thread knowledge access"]
    G["Players find her\nCoherence 3. She explains the threshold.\nPlayer choice: assist research or surface to Varfell leadership"]
    H["Assist research\nThread operation (players assist pool)\nRisk: additional Coherence loss on Failure\nSuccess: research complete. Information surfaces."]
    I["Surface to Varfell\nVarfell leadership decision: force retirement (preserve Coherence)\nor permit supervised operations\n[EDITORIAL: ED-323 — Varfell ethical response to practitioner welfare]"]
    J["Coherence 0 transition (PP-261)\nBecomes Non-Player Character — fully functional, no agency\nVarfell loses strategic asset and gains a question:\nwhat does she do now?"]
    K["Research complete\nInformation released\nNature of finding drives subsequent arcs\n[EDITORIAL: content of finding]"]
    L["Varfell forces retirement\nPractitioner stable at Coherence 3–4\nVarfell permanently degraded in Thread capacity\nThey approach players as potential practitioners"]
    M["Supervised operations\nCoherence held at 3 with careful rationing\nSlow research completion over 2 more seasons\nRisk of Coherence loss each op"]

    A --> B --> C --> D
    D --> E --> G
    G --> H --> K
    G --> I --> L
    G --> I --> M --> J
    D --> F
    H --> J
```

**Emergent logic:** PP-261 (Coherence 0 Non-Player Character transition) creates a mechanical cliff that produces genuine strategic calculation. The Truthseeker's behaviour — rationing, silence, archive work — is not a scripted character choice. It is the only rational response to a mechanic with no recovery path once the threshold is crossed. The arc exists because the rule has no exit.

---

## Cross-Arc Interaction Table

| Arc | Interacts With | Mechanism | Effect |
|-----|---------------|-----------|--------|
| Arc 5 (RS Spiral) | Arc 7 (Army Stays) | RS ≤ 40 triggers Weaving failure cascades at same time Löwenritter presence strains Crown capacity | Crown cannot address both simultaneously — forced triage |
| Arc 5 (RS Spiral) | Arc 9 (Practitioner Stops) | Truthseeker's research may be about the RS drain — Varfell data + Church Weaving correlation | If Arc 9 resolves with information released, Arc 5 becomes politically legible |
| Arc 6 (Debate Win) | Arc 8 (Guilds Know) | Failed Crown implementation creates Stability −1; Guild ledger shows third consecutive season of Crown Stability pressure | Guild data now includes Crown weakness — changes what they can trade |
| Arc 7 (Army Stays) | Arc 6 (Debate Win) | If Church mediates Löwenritter withdrawal (Resolution C), Church Influence +1 in territory; TC +1 bonus stacks with passive | Church gains from military crisis without taking any action |
| Arc 8 (Guilds Know) | Arc 5 (RS Spiral) | If Crown-Guild alliance (Resolution B) optimises Suppress timing, Church forced to Assert in sub-optimal seasons — but Weaving continues regardless | TC suppression buys time; RS drain is independent of TC |
| Arc 9 (Practitioner Stops) | Arc 5 (RS Spiral) | If Truthseeker completes research revealing RS manipulation, Varfell has evidence but no practitioner to act on it | Knowledge without capacity — requires player bridge |
