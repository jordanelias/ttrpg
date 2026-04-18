# Valoria — Emergent Narrative Arcs: New Non-Greedy Actor Archetypes
## SIM-ARC-03 | Generated: 2026-04-04 | Model: Sonnet 4.6
## Source: stage6_factions.md, stage13_npcs.md, params_core.md, params_threadwork.md, editorial_resolution_pass.md

---

## New Non-Greedy Actor Archetypes (NG-G through NG-L)

Distinct from both SIM-ARC-01 (irrational/compulsive) and SIM-ARC-02 (restraint/hesitation). This batch models **social-structural** non-optimality: players who read the room correctly but respond to the social dynamics of the *table* rather than the game world, and players who apply real-world institutional logic that doesn't map onto Valoria's mechanics.

| Code | Archetype | Behaviour |
|------|-----------|-----------|
| NG-G | **The Consensus Builder** | Before any major action, seeks full party agreement. Will not act without unanimous buy-in. Delays Domain Actions by 1 season while negotiating internally. Correct social instinct; wrong scale for the mechanic. |
| NG-H | **The Precedent Follower** | When facing a new mechanical situation, defaults to "what did we do last time?" rather than reading the current state. Applies prior-session rulings to different contexts. Ignores faction stat changes since the last time they engaged. |
| NG-I | **The NPC Sympathiser** | Once a player has an emotional connection to an NPC, will not take any action that harms that NPC's interests — even indirectly, even when the NPC's stated Beliefs would accept the cost. Projects player-table reluctance onto the NPC. |
| NG-J | **The Clean Hands Player** | Refuses any action that could be construed as manipulative, deceptive, or instrumentalising — including using knowledge the players gained via Intel actions. Will not deploy advantage gained through surveillance. |
| NG-K | **The Completionist** | Before acting on a problem, needs to understand all dimensions of it. Investigates each arc to exhaustion before responding. Never commits while information is still outstanding, even when the outstanding information is marginal. |
| NG-L | **The Momentum Spender** | Spends Momentum on the first roll of each scene regardless of stakes. Uses auto-successes on Circles, investigation, or social warm-up rolls rather than preserving them for the scene's critical Debate or Domain Action. |

Notation: optimal path = solid line; new non-greedy branch = dashed line with `[NG-X]` tag.

---

## ARC 11: The Parliament Clock

### Mechanical Seed
Institutional Pressure (IP) track reaches 30 → Altonian education demand fires automatically → Crown must respond → Parliament is the constitutional mechanism for Crown response → players can sponsor a Parliamentary Vote to delay, redirect, or block the demand → Parliamentary Vote mechanic (Domain Action: Influence, pool vs Ob) requires faction leadership commitment → the window for Parliamentary intervention is exactly 1 season.

### Narrative

The players will know the Altonian demand is coming before it arrives. Institutional Pressure at 25 is legible — a player watching faction stats sees the trajectory. What they may not know is that the Parliamentary response window is exactly one season: the demand arrives at IP 30 accounting, and Parliament meets at the end of that same season. If the players don't act before accounting closes, the demand is answered by default.

The Parliamentary Vote is not dramatic. It is procedural. A motion is filed, factions declare positions, the vote resolves. What makes it dramatic is the positioning before the vote — the season of lobbying, the favours spent, the faction alliances disclosed. Hafenmark will vote against the demand (Baralta's Beliefs; Crown authority). The Church will vote for it if TC is above 40 (Altonian ecclesiastical leverage). The Guilds will abstain unless someone pays them to care. Varfell will vote against it if their Thread investigation gives them reason to want Torben present in Valoria.

The players are not the vote. They are the people who shape what the vote means before it happens.

### Flowchart

```mermaid
flowchart TD
    A["Institutional Pressure reaches 25\n[Trajectory visible to watching players]"]
    A --> B["IP crosses 30 at Accounting\nAltonian education demand triggers\n[stage13 §13.1 Torben — automatic mechanical fire]\nParliamentary Vote window: 1 season"]
    B --> C["Players must lobby before Accounting closes\nEach faction: 1 Domain Action to align position\nHafenmark: votes No (default — Baralta Beliefs)\nChurch: votes Yes if TC≥40 / No if TC<40\nGuilds: Abstain unless lobbied\nVarfell: votes No if TK≥3 (Torben leverage)"]

    C --> D{Players lobby which faction?}

    D -->|"Optimal: Guilds (swing vote)\nCircles Ob 2 + Wealth offer (1 Wealth)"| E["Guilds lobbied: Influence 4D+1 bonus vs Ob 2\nP(success) ≈ 93%\nGuilds vote No → demand fails 3-1 (Church only Yes)\nTorben stays — Loyalty Clock doesn't start"]
    E --> F["Demand defeated this season\nIP resets to 25 (demand registered but blocked)\nChurch TC +1 (frustration — institutional response)\nGuilds Influence +1 (demonstrated relevance)"]

    D -.->|"[NG-G] Consensus Builder:\n1 season of internal party debate\n'Should we use Wealth for this?'\n'What if the Church retaliates?'"| G["Season passes in deliberation\nAccountig closes — no lobby action taken\nGuilds default to Abstain\nVote result: Church Yes, Hafenmark No, Guilds Abstain, Varfell No\nIf TC<40: demand fails 1-3 (Hafenmark + Varfell block)\nIf TC≥40: demand passes 1-1 (tie → Crown decides)"]
    G -->|"TC≥40 (likely by IP 30)"| H["Tie vote → Almud decides\nAlmud Belief: 'trade relationship holds regardless'\nAlmud yields → Torben departs\nLoyalty Clock starts — players spent nothing, gained nothing"]
    G -->|"TC<40"| I["Demand fails without player action\nPlayers spent 1 season debating unnecessarily\n— they were safe the whole time but didn't know"]

    D -.->|"[NG-K] Completionist:\n'We need to understand Varfell's\nposition before we act — what's TK?'"| J["Players spend season investigating Varfell TK\nCircles Ob 2 + Cognition read\n— this information is not marginal, TK is relevant\n— but 1 scene of investigation is sufficient\nCompletionist spends entire season on it"]
    J --> K["Investigation complete: TK confirmed at 3\nVarfell votes No (players now know this)\nBut: season spent on investigation\nnot on lobbying Guilds\nGuilds remain at Abstain\nSame result as NG-G TC<40 path"]

    D -.->|"[NG-I] NPC Sympathiser:\n'Torben is a child — we can't\nuse him as a political lever'"| L["Players refuse to engage\nParliamentary mechanics at all\n'We'll deal with Torben directly\nnot through institutional procedure'"]
    L --> M["No lobby action\nVote resolves on faction defaults\nTorben departs if TC≥40\nPlayers then face Circles Ob 3\n(Altonian territory) to reach Torben directly\nvs Ob 2 parliamentary route they refused"]
    M --> N["Direct retrieval: harder, slower, more exposed\nPlayers protected Torben from being\n'used politically' by doing nothing\nwhile he was sent to Altonia"]

    D -.->|"[NG-L] Momentum Spender:\nSpends 2 Momentum on\nCircles warm-up roll to Guilds contact\n(Ob 1 — trivially succeeds without Momentum)"| O["Circles Ob 1 succeeds without Momentum\n(Momentum overkill on a near-certain roll)\nMomentum depleted entering Guilds lobby scene\nLobby scene: Influence Domain Action Ob 3\n(contested — Church is also lobbying Guilds)\nWithout Momentum: pool 5D vs Ob 3 — P(success) ≈ 55%\nWith Momentum: 5D+1 auto-success — P(success) ≈ 80%"]
    O -->|"Fail lobby without Momentum (45%)"| P["Guilds Abstain\nVote: Church-Yes, Hafenmark-No, Guilds-Abstain\nSame tie result as NG-G if TC≥40\nMomentum burned on wrong roll"]
    O -->|"Success (55% — still likely)"| Q["Guilds vote No\nDemand defeated — correct outcome\nbut at reduced probability from the spend pattern"]

    F --> R["Best outcome: demand defeated\nTorben stays, Loyalty Clock never starts\nGuilds relationship asset\nIP resets to 25 — but Altonia tries again in 2 seasons"]
    H --> S["Torben departs\nLoyalty Clock starts at 8\n→ feeds ARC 1 (Succession Weapon)\nPlayers spent 1 season debating\ninstead of a single Circles roll"]
    N --> T["Torben in Altonia\nRetrieval route: Circles Ob 3 (harder)\nPlayers chose harder path\nto avoid institutional manipulation\nof a child who is now in Altonia"]
```

### Footer

Emerges from IP threshold mechanics, Torben Loyalty Clock, and Parliamentary Vote procedure running in parallel. No player designed the 1-season window — it is the mechanical output of IP 30 threshold + same-season Parliament timing. Arc shape: 1 season crisis, 2 season consequence. The window closes whether or not players act.

**New archetype findings:**
- NG-G (Consensus Builder): Internal party consensus-building is the correct social behaviour in many contexts. Here it consumes the action window. The players had the information, the plan, and the resources — they spent the season deciding, not acting. The outcome depends on TC, which they couldn't control.
- NG-K (Completionist): Investigating Varfell's TK is not wrong — TK is relevant. The error is spending a full season on it when 1 scene suffices, and not simultaneously lobbying Guilds with the rest of the party. The investigation was worth doing; doing only the investigation was not.
- NG-I (NPC Sympathiser): Protecting Torben from being "used politically" by refusing to engage Parliament produces Torben going to Altonia through the harder-to-reverse path. The sympathiser's protective instinct made things worse for Torben.
- NG-L (Momentum Spender): Momentum on Ob 1 Circles is waste. The critical roll was the Ob 3 contested lobby. 2 Momentum on the lobby roll would have pushed success to ~90%. Spending it on the approach roll burned it before the scene where it mattered.

---

## ARC 12: The Maret Severance

### Mechanical Seed
Maret Uln's Loyalty to Varfell reaches 3 (defection threshold) → Vaynard must decide: retain Maret (costly, requires Stability check), release Maret (Varfell loses the most valuable Thread practitioner on the peninsula), or report Maret to Church (eliminates the risk, destroys Maret) → players learn of the crisis first → intervention window is 1 scene.

### Narrative

Maret has never been a Varfell asset. He has always been pursuing his own Belief — reconstructing the Ceiral Ritual before the Inquisitors find the text. Vaynard has been calculating since he recruited him: Maret is the most valuable person on the peninsula for the Southernmost problem, and also a liability to Varfell's Church relationships. As long as Maret's loyalty stayed above 4, the calculation held.

Loyalty 3 changes it. At Loyalty 3, Maret is not working for Varfell. He is working for himself, in Varfell's infrastructure, with access to Varfell's archives. Vaynard's Stability check at next accounting — Ob 2 — is a formalisation of what the institution already knows: this arrangement is unstable.

The players learn through a scene, not a report. Maret says something to the right person. A thread-sense impression. A document request that doesn't fit any current Varfell project. The players know before Vaynard acts. They have one scene to intervene — one conversation with Vaynard, one approach to Maret, one institutional manoeuvre. After accounting closes, Vaynard decides.

### Flowchart

```mermaid
flowchart TD
    A["Maret Loyalty to Varfell: 3\n[stage13 §13.4 — defection threshold]\nStability check at Accounting: Ob 2\nP(Vaynard Stability holds) = ~70%\nP(Vaynard acts to resolve) = 30%"]
    A --> B["Players learn 1 scene before Accounting\nOptions: approach Maret, approach Vaynard,\nor institutional manoeuvre"]

    B --> C{Player approach}

    C -->|"Optimal: approach Maret directly\nPresence+Attunement vs Maret Composure 8, Ob 2\n[Maret Resonant Style: Consequence — forward stakes]\nPool ~8D TN7 — P(success) ≈ 82%"| D["Success: Maret's Belief clarified\nHe will continue Ceiral work regardless\nbut agrees to formal non-Varfell status\nLoyalty → 5 (neutral contractor)\nVarfell Stability check cancelled\nMaret retains archive access; Varfell retains research output\n[both parties benefit — clean resolution]"]
    D --> E["Maret as non-aligned Thread resource\nVarfell Influence +1 (Maret's goodwill)\nChurch cannot claim Maret as 'Varfell heretic'\nPlayers have independent Maret relationship"]

    C -.->|"[NG-I] NPC Sympathiser:\n'Maret's Belief is valid —\nwe won't pressure him to compromise'"| F["Players decline to approach Maret\nVaynard's Stability check fires at Accounting\nP(Vaynard holds) = ~70%"]
    F -->|"Vaynard holds (70%)"| G["Maret stays in Varfell — Loyalty 3\nVarfell Stability −1 (internal tension)\nMaret continues Ceiral work unsupported\nChurch Intel flags Maret's work Season+1\n→ Heresy Investigation opens without player knowledge"]
    F -->|"Vaynard acts (30%)"| H["Vaynard chooses Release\n(least confrontational — his Consequence mode)\nMaret ejected from Varfell infrastructure\nMaret loses archive access — Ceiral research delayed 2 seasons\nMaret approaches Revolution for support\n→ Revolution Stability +1, Intel +1"]

    C -.->|"[NG-H] Precedent Follower:\n'Last time we dealt with Vaynard,\nthe Consequence approach worked —\ngo tell him about the downstream risks'"| I["Approach Vaynard with Consequence-mode argument\n(correct — Vaynard IS Consequence Resonant Style)\n+1D bonus applies\nbut the argument is based on last session's\nVarfell stat values — Influence was 4 then\nInfluence is now 3 (Domain Action loss in interim)"]
    I --> J["Argument references Varfell Influence 4 leverage\nthat no longer exists (now 3)\nVaynard's response: 'Our position has changed'\nPlayers lose the +1D bonus and credibility\nEffective Ob rises to 3 (from 2)\nP(social success) drops from ~82% to ~72%"]
    J -->|"Success (72%)"| K["Vaynard convinced — Maret arrangement formalised\nCorrect outcome, lower probability\n— precedent application was partially wrong"]
    J -->|"Fail (28%)"| L["Vaynard decides independently\nP(Release) = 50%, P(Report to Church) = 30%, P(Retain) = 20%\nWorst outcome: Report to Church\nMaret arrested — Ceiral Ritual lost\nVarfell TC +2, Church Stability +1"]

    C -.->|"[NG-J] Clean Hands Player:\n'We got this information through\nThread Sensitivity impression (surveillance) —\nwe can't act on knowledge Maret\ndidn't share voluntarily'"| M["Players decline to use the information\nthey hold about Maret's loyalty\nApproach Vaynard without referencing Maret\n'General conversation about Varfell's practitioners'"]
    M --> N["Vaynard: 'What specifically concerns you?'\nPlayers cannot answer without using\nthe knowledge they obtained\nConversation produces nothing actionable\nVaynard's Stability check fires regardless\nP(Release) = 50% if Vaynard acts (30% probability)"]

    C -.->|"[NG-G] Consensus Builder:\n'We need to agree on whether\nto prioritise Maret or Vaynard\nbefore approaching either'"| O["Internal party consensus-building\n— scene ends before consensus reached\nAccounting closes\nMaret Loyalty still 3\nVaynard acts independently\nP(Release) = 50%"]

    D --> P["Clean resolution: Maret independent\nVarfell Stability holds\nChurch has no Varfell target\nCeiral work continues — RS implications next season"]
    G --> Q["Deferred crisis: Heresy Investigation opens on Maret\n2 seasons of delay then forced resolution\nPlayers lost the window to shape it\n→ ARC 13 accelerated"]
    H --> R["Maret with Revolution:\nRevolution Intel +1\nCeiral Ritual access moves to Revolution control\nIf Revolution gains power (ARC 3)\nCeiral is their leverage — not players'"]
    L --> S["Worst outcome: Church arrests Maret\nCeiral Ritual lost\nVarfell TC +2, Church Stability +1\nRS restoration via Ceiral now impossible\n→ ARC 5 (Niflhel) becomes only RS path"]
```

### Footer

Emerges from Maret's Loyalty track running independently and Vaynard's Institutional Tendency (conservative, calculative) producing a decision at threshold without player input. No player designed the 30% probability that Vaynard acts unilaterally. Arc shape: 1-scene window, then consequence. Maret's fate shapes Ceiral Ritual availability for the rest of the campaign.

**New archetype findings:**
- NG-I (NPC Sympathiser): Not pressuring Maret out of respect for his Belief produces a 30% chance Vaynard acts unilaterally and a 70% chance of deferred crisis via Heresy Investigation. Respecting Maret's autonomy was the correct intuition; the error was that Vaynard was going to act regardless — the players' intervention was the thing that could have produced a mutually acceptable outcome.
- NG-H (Precedent Follower): Using last session's Varfell Influence 4 in an argument when current Influence is 3 is the most precise representation of the archetype — applying a correct approach (Consequence mode, right) with stale data (wrong). The +1D bonus is correctly gained from style matching; the credibility loss from stale data removes it. Net: −1D effective on the key roll.
- NG-J (Clean Hands Player): Refusing to act on intelligence gained via Thread impression is consistent and principled. The mechanical consequence is that Vaynard acts without player influence. The players' scruples about surveillance-derived knowledge prevented them from using the knowledge to help the person that knowledge was about.

---

## ARC 13: The Ceiral Ritual Window

### Mechanical Seed
Ceiral Ritual requires: Thread Sensitivity 70+ practitioner, Niflhel archive access, RS ≤ 60 (stressed substrate needed for temporal depth) → all three conditions have independent timelines → window where all three conditions align simultaneously is approximately 2 seasons → players must commit to the Ritual while committing to other concurrent arcs → Ritual produces RS −6 on Success (net RS cost), RS +8 on Failure (catastrophic).

### Narrative

The Ceiral Ritual is not a secret. Maret talks about it obsessively. The players will know about it within two sessions. What they may not understand is the timing problem: the Ritual requires a substrate stressed enough to allow temporal depth (RS ≤ 60), a practitioner with Thread Sensitivity 70+, and the Niflhel archive. These three conditions align only when RS has degraded to a particular band and a practitioner has advanced to a particular level. The window isn't indefinite.

The Ritual itself is not dangerous in the way players expect. It is not a combat scene. It is a sustained Thread operation — a Past-Oriented Pulling at foundational scale, Ob 7+2 surcharge (Ob 9), RS consequences ×3. The dangerous part is the Failure outcome: RS +8. In a game where RS is already degraded to make the Ritual viable, RS +8 means the world becomes significantly more legible — an apparent improvement that is actually a system shock. The substrate doesn't respond to being forced toward coherence gracefully.

The players will want to do the Ritual when it becomes available. The question is whether they've done the preparation — practitioner at TS 70+, Niflhel archive secured, RS in the right band — or whether they're trying to rush it because they can see the window closing.

### Flowchart

```mermaid
flowchart TD
    A["Three conditions for Ceiral Ritual:\n1. TS 70+ practitioner (Thread Sensitivity track)\n2. Niflhel archive access (secured or vulnerable)\n3. RS ≤ 60 (substrate stressed)\n[params_threadwork: POP requirements]"]
    A --> B["Condition alignment window: ~2 seasons\nIf window missed: TS advances past 70\nbut RS may recover above 60 (window closes)\nor Niflhel archive becomes unavailable (ARC 5)"]

    B --> C{Players assess readiness}

    C -->|"Optimal: systematic prep\n— confirm TS via Thread Diagnosis (TN7 Ob1)\n— confirm archive access (Niflhel scene)\n— confirm RS range (passive observation)\n— then execute"| D["All conditions verified\nRitual: Spirit+History+TPS÷2 = ~8D TN8 vs Ob9\n[POP at foundational scale: TN8, Ob 7+2=9]\nE[net] at TN8 = 8×0.2 = 1.6 vs Ob 9\nP(success) ≈ 4% — very low"]
    D --> E["Expected result: Failure\nRS +8 (catastrophic restoration)\nRS rebounds above 60 — window closes\nPractitioner Snap-Back Wound + RS −6 minimum"]
    D -->|"Overwhelming (rare, ~0.5%)"| F["RS −10 (sustained substrate opening)\nThread truth more accessible — Axis 9 crack\nCeiral practitioner gains TS +5\nWindow extends 1 additional season\n→ feeds ARC 4 (Thread Truth Cascade) softly"]

    C -.->|"[NG-K] Completionist:\n'We need to understand\nall Ceiral variations before committing\n— what are the alternative ritual forms?'"| G["1 season of archive research\nlearning Ceiral variations\n(marginal information — one ritual, one form)\nRS drift during research: +3 (Thread management,\nno RS-consuming ops while researching)\nRS crosses 65 → Ritual window closes\nAll conditions aligned EXCEPT RS"]
    G --> H["Window closed by over-research\nPlayers learned everything about a\nRitual they can no longer attempt this arc\nRS must degrade again — 2+ seasons"]

    C -.->|"[NG-G] Consensus Builder:\n'We all need to agree\nwhether the Ritual is worth RS −6 risk'"| I["Consensus required from all party members\nSome are uncertain (RS −6 is significant)\n1 season of internal deliberation\nRS recovers slightly: +2 from no ops\n— same window-closing effect as NG-K\nbut faster"]
    I --> J["RS crosses 63 by Season+1\nWindow closes\nConsensus reached — about a closed window"]

    C -.->|"[NG-H] Precedent Follower:\n'Last time we did a Thread op at RS 55,\nit cost RS −4. This should be similar.'"| K["Players apply POP RS cost from a prior\nWeaving operation (RS−4 was Weaving)\nCeiral is POP Foundational: RS consequences ×3\nPlayers expect RS −4; actual on Failure = RS +8\n(restoration shock, not cost)\nThey proceed without Mending preparation\nor RS buffer"]
    K -->|"Failure (likely)"| L["RS +8 applied\nPlayers expected RS −4 buffer\nactual result: RS rebounds to 70\nPractitioner Snap-Back Wound\nChurch Intel flags anomalous RS event\n— investigation opens\nRS above 60: RS-consuming ops no longer viable\nARC 2 threshold effects reactivate"]

    C -.->|"[NG-L] Momentum Spender:\nSpends 3 Momentum on\nThread Diagnosis pre-check (Ob 1)\ninstead of reserving for Ritual roll"| M["Diagnosis: Ob 1, trivially succeeds\nMomentum spent: 3 auto-successes on Ob1\nRitual: 8D TN8 vs Ob9\nWithout 3 Momentum: E[net] = 1.6 — ~4% success\nWith 3 Momentum: effective net = 4.6 — ~15% success\nMomentum spend pattern reversed the probabilities\nby a factor of ~4"]
    M -->|"Ritual without Momentum (~4%)"| N["Failure: RS +8\nSame catastrophic outcome\nbut players had the Momentum to\nmake it a real attempt"]
    M -->|"3 Momentum preserved for Ritual (~15%)"| O["Better-than-expected outcome distribution\nP(Success or better) ≈ 15% (vs 4%)\nP(Overwhelming) ≈ 0.5% (unchanged)\nStill likely fails — but 3× more likely to succeed"]

    C -.->|"[NG-J] Clean Hands Player:\n'Maret's research notes are his private work\n— we won't read them without permission\n(they contain the ritual preparation steps)'"| P["Players don't access Maret's notes\nPrepare ritual without preparation steps\n+2 Ob penalty (no Ritual preparation)\nEffective Ob 11\nP(success) ≈ 0.5%\nP(overwhelming) ≈ 0%"]

    E --> Q["Expected outcome: RS rebounds\nWindow closes\nPartially successful: RS −6 on the attempt\n(base cost regardless of outcome)\n+ RS +8 on Failure = net RS +2\nCeiral Ritual is net-positive RS only\non Overwhelming (RS −10 net)\nFor all other outcomes it is RS-neutral to RS-harmful"]
    F --> R["Rare best outcome:\nSoft Axis 9 crack\nThread truth more accessible\nRS net −10 — world more stable\n→ controlled approach to ARC 4"]
    L --> S["RS +8 → 70+\nWindow closed catastrophically\nChurch Investigation fires\nARC 2 reactivated\nMulti-arc convergence — hardest state"]
    N --> T["Same outcome as optimal Failure path\nbut with Momentum pool empty\nnext scene has no auto-success option"]
```

### Footer

Emerges from the POP foundational scale Ob 9 (Ob 7 + 2 surcharge) colliding with a TS 70 practitioner's expected pool (~8D TN 8, E[net] 1.6). The Ritual is mechanically near-impossible for a TS 70 practitioner — it requires TS 90+ for viable success probability. This is the design: the Ceiral Ritual is the game's hardest achievable action, not a reliable tool. The arc tests whether players attempt it understanding the odds, or rush it because the window is closing. Arc shape: 2-season window; 1-scene execution; consequences extend for 3+ seasons regardless of outcome.

**New archetype findings:**
- NG-K (Completionist): Over-research closes the window. The information gained (alternative ritual forms) is genuinely marginal. The window was time-limited; the information was not worth the time. The completionist prioritised knowing everything over knowing the most important thing (the window).
- NG-H (Precedent Follower): Applying prior RS cost data from a Weaving operation to a Foundational POP is a category error. The ×3 RS consequence modifier is not intuitive; players who don't re-read POP rules will assume linear scaling from prior experience. The failure outcome is catastrophically worse than expected.
- NG-L (Momentum Spender): Momentum spent on Thread Diagnosis (Ob 1) is the clearest spend-pattern error in the batch. 3 Momentum on Ob 1 is 3 auto-successes above the minimum needed. The same Momentum on the Ob 9 Ritual roll raises P(success) from 4% to 15%. The spend pattern was wrong by a factor of ~4.
- NG-J (Clean Hands Player): Not reading Maret's notes without permission is respectful. The +2 Ob penalty from missing preparation steps drops an already-near-impossible roll to effectively impossible. The players' ethical constraint is correctly reasoned; the consequence is that they attempt the hardest action in the game without the one preparation that marginally improves it.

---

## ARC 14: The Guilds' Quiet War

### Mechanical Seed
Guilds Wealth 6 (highest in the game) + no Military + no Mandate → Guilds can never win a direct confrontation but can make every other faction's Domain Actions more expensive → players can channel Guilds Wealth into faction-support actions that produce +1D bonuses across multiple factions simultaneously → players must choose between spreading Guilds support (all factions +1D, none dominant) or concentrating it (one faction +2D, others unaffected) → Church's Ethical Framework penalises economic actions that involve the Guilds (Guilds = secular autonomy = Axis 5).

### Narrative

The Guilds don't want power. This is the thing players will misread for the first few sessions. The Guilds want to operate. They want trade routes open, debts honoured, contracts enforced. They are the only faction that benefits from every other faction being functional — a Church collapse means no parish contracts, a Crown collapse means no royal charter, a Hafenmark collapse means no maritime trade. The Guilds' institutional interest is in the stability of the system, not in its direction.

What this means mechanically is that Guilds Wealth 6 is available to any faction that offers the right terms. The players, if they're allied with or embedded in a faction, can broker Guilds financing. They can make the Guilds' support concrete — +1D to Domain Actions backed by Guilds commercial infrastructure. The question is whether they spread it (maintaining Guilds neutrality, supporting all factions equally) or concentrate it (giving one faction a decisive advantage, which the Guilds' Institutional Tendency does not want but their leadership might accept).

The Church is watching. Any action that routes Guilds support into secular factional advantage activates the Church's Ethical Framework at +1 Ob (Guilds autonomy contradicts divine economic authority). If players route Guilds support to Varfell — the faction investigating Thread truth — the Church adds an additional +1 Ob (Axis 2 tension). The Guilds don't know this is happening until the Heresy Investigation names a specific transaction.

### Flowchart

```mermaid
flowchart TD
    A["Guilds Wealth 6 available\nNo Military, no Mandate, no Intel\nInstitutional Tendency: maintain stability of all factions\n[stage6 §8.6 Guilds profile]"]
    A --> B["Players identify Guilds as financing source\nOptions: distribute support, concentrate support,\nor ignore Guilds entirely"]

    B --> C{Player strategy}

    C -->|"Optimal: targeted concentration\nBroker Guilds financing to one aligned faction\nCircles Ob 2 (Guilds contact established)\nNegotiation: Wealth 1 per season + target faction benefit"| D["Guilds provides +2D to one faction's\nDomain Action per season\nTarget faction Influence or Mandate Domain Action\neffectively boosted: e.g. Hafenmark 4D → 6D\nP(success on Ob 4) rises from ~55% to ~82%\nGuilds Stability +1 (used their wealth productively)"]
    D --> E["Church detects economic routing\nChurch Ethical Framework: +1 Ob on Church Domain Actions\ntargeting Guilds this season\n(Guilds autonomy = Axis 5 tension)"]
    E --> F["Net: target faction boosted significantly\nChurch slightly penalised in counter-actions\nGuilds activated as a political actor\n(changes Guilds from passive to engaged)"]

    C -.->|"[NG-G] Consensus Builder:\n'Every faction should benefit equally\n— we can't play favorites\namong our potential allies'"| G["Players insist on distributing Guilds support\nto all non-Church factions equally\n(+1D each to Crown, Hafenmark, Varfell)\nTotal cost: 3 Wealth / season\nGuilds Wealth 6 → 3 in 2 seasons\nGuilds Wealth threshold at 4 fires: Stability check Ob 2"]
    G --> H["Guilds Stability −1 if check fails (30%)\nAll factions get +1D — no faction decisive advantage\nChurch receives Church Ethical Framework\n+1 Ob on all Guilds-adjacent Domain Actions\n— same penalty as targeted, but\nthe boost is distributed rather than concentrated\nResult: everyone slightly better off;\nnobody decisively better off"]
    H --> I["Guilds Wealth depleted in 2 seasons\nThe fair distribution made\nnone of the intended effects decisive\nChurch's +1 Ob penalty still active\nGuilds spent as a political resource\nwith marginal strategic return"]

    C -.->|"[NG-J] Clean Hands Player:\n'We can't use Guilds financing\nwithout full Guilds disclosure\nto all affected factions'"| J["Players tell Crown, Church, Hafenmark, Varfell\nthat they're arranging Guilds financing\nbefore doing so\n— 'transparency in faction relationships'"]
    J --> K["Church immediately responds:\nInstitutional Pressure on Guilds +1\nChurch Domain Action: Influence 6D vs Guilds Stability 5 (Ob 5)\nP(Church success) ≈ 55%\nIf success: Guilds threatened → financing arrangement collapses"]
    K -->|"Church success (55%)"| L["Guilds refuse financing arrangement\nunder Church pressure\nGuilds Stability −1 (pressure)\nPlayers' transparency enabled the counter-action\nthat destroyed the arrangement"]
    K -->|"Church fails (45%)"| M["Guilds proceed despite Church pressure\nFinancing goes through\nbut at reduced terms: +1D not +2D\n(Guilds risk-adjusted the deal)\nSame outcome as optimal but −1D"]

    C -.->|"[NG-H] Precedent Follower:\n'Last time we engaged the Guilds,\nWealth exchange was enough —\nno Circles needed'"| N["Players skip Circles approach\ngo directly to Guilds Wealth exchange\nWithout Circles (no established contact):\n+1 Ob on the negotiation\nGuilds Stability check required (Ob 3 instead of Ob 2)\nP(Guilds agree) drops from ~88% to ~72%"]
    N -->|"Guilds refuse (28%)"| O["No financing arrangement\nPlayers attempted approach without establishing\nthe social relationship first\n'We don't know you' — Guilds default to caution"]
    N -->|"Guilds agree (72%)"| P["Financing at Wealth −1 surcharge\n(higher risk premium, no relationship trust)\nEffective cost: Wealth 2/season not 1\nGuilds deplete faster — arrangement lasts\n1 season not 2"]

    C -.->|"[NG-K] Completionist:\n'We need to map all\nGuilds' commercial interests\nbefore proposing terms'"| Q["2-season Guilds commercial survey\n(marginal — Guilds interests are stable and known)\nDuring 2 seasons:\nChurch runs Domain Action on Guilds unprovoked\nP(Church success on Guilds Stability Ob 5) ≈ 55%\nIf success: Guilds Stability −1\nFinancing arrangement now at +1 Ob (weakened partner)"]
    Q -->|"Church acts first (likely)"| R["Guilds weakened before players engage\nArrangement terms worse\nPlayers surveyed an asset while it depreciated"]

    F --> S["Best outcome: one faction decisively boosted\nGuilds activated as political ally\nChurch slightly penalised\nArrangement sustainable 2-3 seasons\n— requires Wealth replenishment from target faction"]
    I --> T["Fair distribution: all factions marginally better\nGuilds depleted in 2 seasons\nNo decisive outcome achieved\nPolitical capital spent for distributed +1D"]
    L --> U["Transparency enabled counter-action\nFinancing collapsed before use\nGuilds relationship damaged (pressure)\nPlayers gained nothing from disclosure"]
```

### Footer

Emerges from Guilds' structural position — highest Wealth, no Military, no Mandate — making them a pure financing faction. The arc has no NPC villain; the Church's counter-action is its Institutional Tendency, not a deliberate attack on players. Arc shape: 2-season arrangement window; immediate once-per-season benefit. The Guilds are the most underused faction in standard play; this arc makes them central.

**New archetype findings:**
- NG-G (Consensus Builder): Distributing Guilds support "fairly" produces no decisive outcome. The fair instinct is wrong because the Guilds' Institutional Tendency is already toward stability; what the players can add is direction. Distributing equally maintains the status quo while depleting Guilds Wealth. The fair distribution made nobody decisively better off and depleted the resource.
- NG-J (Clean Hands Player): Transparency with all factions before acting enables the Church to counter-action before the arrangement completes. The 55% Church success probability means fair disclosure has an even-chance of destroying the arrangement it's disclosing. The clean hands instinct assumed all factions would respond to disclosed information neutrally; the Church responds institutionally.
- NG-H (Precedent Follower): Skipping Circles because "Wealth was enough last time" misses the Guilds' contact establishment requirement. The +1 Ob penalty from no established relationship is the mechanic that Circles removes. Prior successful Wealth exchange doesn't substitute for relationship infrastructure.
- NG-K (Completionist): Surveying Guilds commercial interests over 2 seasons while the Church can run Domain Actions on the Guilds in that period means the asset the completionist was studying degraded while being studied. The survey produced marginal information; the delay produced a weakened partner.

---

## ARC 15: The Lenneth Channel

### Mechanical Seed
Queen Lenneth secretly funds Revolution academic work and holds pre-Altonian coastal survey with Thread-perception content → players discover this via a separate investigation → Lenneth becomes a potential intelligence channel between Crown and Revolution → using this channel requires players to either disclose it to Almud (who doesn't know) or keep it secret from him → each choice has distinct mechanical costs.

### Narrative

Lenneth Almqvist is not a mystery. She is a person with a hidden position on Axis 4 (Cultural Identity) and Axis 7 (Information), funding work she believes in through a structure her husband doesn't know about. The players will find this through investigation — a paper trail that doesn't reach the Crown, a reference in an academic document to a foundation that doesn't exist in public records. A Thread Sensitivity 50+ character who reads the coastal survey she holds will understand what it is before they understand who holds it.

When they find her, Lenneth doesn't deny it. She is not frightened. She is calculating: the players now know something, and she wants to know whether they're going to be useful or dangerous. Her Resonant Style (Consequence) means she'll engage with anyone who shows her the structural implications of what they know and what they want.

The channel she represents is real: Lenneth has access to Revolution academic networks that no other Crown actor does. Through her, the players can move information, resources, or people between the Crown and Revolution without either faction formally acknowledging the other. This is the most valuable information-brokerage asset in the campaign. Whether to use it — and whether to tell Almud — is the arc's decision.

### Flowchart

```mermaid
flowchart TD
    A["Players discover Lenneth's hidden network:\n— Foundation funding Revolution academics\n— Pre-Altonian coastal survey (Thread-perception account)\n[stage13 §13.1 Lenneth — hidden networks]"]
    A --> B["Lenneth's Resonant Style: Consequence\nComposure: 10\nDominant Conviction: Liberty\nPlayers must approach her before she\nlearns they know — 1-scene window"]

    B --> C{Players approach Lenneth}

    C -->|"Optimal: present structural implications\nvs Lenneth Composure 10, Ob 2\nConsequence mode (+1D)\nPool ~8D TN7 — P(success) ≈ 92%"| D["Success: Lenneth agrees to\nchannel arrangement\n'You understand why I do this'\nCrown-Revolution information channel active\nPlayers can pass Intel between factions\nwithout formal alliance\nLenneth RS survey available to TS50+ practitioner"]
    D --> E{Do players tell Almud?}
    E -->|"Tell Almud"| F["Almud knows his wife funds Revolution\n— Almud Composure check (Spirit TN7 Ob2)\nP(success) ≈ 70%"]
    F -->|"Success"| G["Almud processes this\nSovereign Constraint partially reduced\n(Lenneth's network provides alternative path\nfor Einhir action without Crown institution)\nCrown Mandate −1 (domestic tension)\nChannel still active — Almud becomes aware ally"]
    F -->|"Fail — Almud acts"| H["Almud issues Royal Decree requiring\nLenneth's foundation to cease operations\nChannel collapses\nRevolution loses academic funding\nLenneth relationship with players damaged\n(they disclosed when she trusted them)"]
    E -->|"Don't tell Almud — keep secret"| I["Channel active, Almud unaware\nPure intelligence asset\nLenneth Stability +1 (protected)\nbut players are now holding a secret\nfrom their Crown ally\nIf Almud discovers independently:\nCrown relationship −1D on future social rolls"]

    C -.->|"[NG-I] NPC Sympathiser:\n'Lenneth is doing the right thing —\nwe shouldn't leverage this,\njust keep her secret'"| J["Players approach Lenneth not to use the channel\nbut to reassure her they won't disclose\nLenneth: 'What do you want in return?'\nPlayers: 'Nothing'\nLenneth's Consequence mode finds this\nmechanically unconvincing — Ob rises to 3\n(no structural exchange offered)"]
    J -->|"Success Ob3 (~72%)"| K["Lenneth doesn't trust pure altruism\nbut accepts the reassurance\nNo channel established\nLenneth network protected\nbut players have no access to it\n'You protected something you can't use'"]
    J -->|"Fail (~28%)"| L["Lenneth suspects players have\nundisclosed interests\nWithdraws the conversation\nNetwork goes deeper underground\nPlayers lose access permanently"]

    C -.->|"[NG-H] Precedent Follower:\n'Consequence NPCs respond to\nlong-term structural thinking —\nwe'll present Lenneth's network\nas a threat to her long-term position'"| M["Players present the 'danger' of her position\n(threat framing)\nLenneth's Consequence mode reads\nthis as: 'They're trying to frighten me'\nNot a danger presentation — a threat\nOb rises to 4 (wrong register)"]
    M --> N["Consequence NPCs respond to\nfuture-oriented argument, not fear\nPrior use of Consequence mode was probably\nwith a different NPC in a different context\nLenneth: 'I've lived with this danger\nfor twelve years. Tell me something new.'\nP(success Ob4) ≈ 55% — significant drop from 92%"]

    C -.->|"[NG-J] Clean Hands Player:\n'We found this through\ninvestigation — we should tell her\nwe know before using it'"| O["Players disclose they know about\nher hidden network before approaching\n'We know about the foundation'\nThis is what Lenneth feared\nher first instinct: denial\nOb rises to 3 (she's defensive now)"]
    O -->|"Success Ob3 (~72%)"| P["Lenneth accepts that they know\nand agrees to work with them\nChannel established at higher\ntrust threshold — more durable\nLenneth relationship asset stronger\nbut starting Ob was higher"]
    O -->|"Fail (~28%)"| Q["Lenneth treats them as threats\nNetwork goes dark\nPaper trail destroyed within the scene\nSurvey hidden elsewhere\nChannel permanently lost"]

    C -.->|"[NG-G] Consensus Builder:\n'We need to discuss as a party\nwhether to involve the Queen\nbefore approaching her'"| R["Internal consensus required\nScene where Lenneth is accessible passes\nShe moves to a different location\nNextCircles Ob 3 to reach her\n(she's now more cautious — heard rumours\nthat someone was asking about\nthe Foundation from her staff)"]
    R --> S["Ob 3 approach instead of Ob 2\nLenneth now at higher alert level\nP(success) drops from 92% to 72%\n— the delay made her harder to reach\nbefore the players even spoke to her"]

    G --> T["Best outcome: Almud informed,\nchannel active, Sovereign Constraint reduced\nCrown Mandate −1 is the only cost\n→ enables ARC 10 (Einhir) most cleanly"]
    I --> U["Channel active, Almud unaware\nPlayers hold Crown secret\nUsable for 2-3 seasons before\nAlmud likely discovers independently\n(Crown Intel processes)\nTimer on the secret"]
    K --> V["Network protected, players locked out\nLenneth grateful but the asset is inert\nThe sympathiser preserved the thing\nthey wanted to use but couldn't use it"]
    Q --> W["Network destroyed\nLenneth's 12-year project gone\nRevolution academic funding collapsed\nPlayers who disclosed their knowledge\ncaused more harm than anyone who\nwould have suppressed it"]
```

### Footer

Emerges from Lenneth's hidden networks intersecting with the Crown-Revolution relationship gap and the coastal survey's Thread content. No player designed the network — it has been running for years before the campaign starts. Arc shape: 1-scene approach window, then 3–4 season channel duration. The survey's RS resonance (PP-258) makes Lenneth's asset materially relevant to RS restoration — a fact players may not connect until they've read it.

**New archetype findings:**
- NG-I (NPC Sympathiser): Approaching Lenneth to protect her rather than to use the channel presents a pure altruism signal that Consequence-mode NPCs distrust. Lenneth's entire life is calculating structural exchange. "We want nothing" is not reassuring — it is suspect. The sympathiser's correct instinct (protect her) produced the wrong opening position (nothing to trade), raising Ob and potentially triggering her withdrawal.
- NG-H (Precedent Follower): Prior Consequence-mode success with another NPC included threat-framing as part of the structural argument. Lenneth's Consequence mode is oriented toward positive futures, not away from dangers. The threat framing worked elsewhere because the NPC's Consequence orientation included threat assessment. Lenneth has lived with danger for 12 years; it doesn't move her. The precedent was partially applicable — Consequence mode correct, register wrong.
- NG-J (Clean Hands Player): Disclosing knowledge before using it is the most principled approach and raises Ob to 3. Lenneth's defensive response is not irrational — she assumed the worst from discovery. The clean hands player made a true statement ("we know") that produced a defensive reaction rather than a collaborative one. The same information delivered as structural implication (optimal path) rather than disclosure would have produced Ob 2.

---

## Cross-Arc Interaction Table (SIM-ARC-03)

| | ARC 11: Parliament | ARC 12: Maret | ARC 13: Ceiral | ARC 14: Guilds | ARC 15: Lenneth |
|---|---|---|---|---|---|
| **ARC 11: Parliament** | — | Maret's independence from Varfell (ARC 12) weakens Varfell's Parliamentary No vote reliability | Ceiral Ritual RS consequences affect Parliamentary timing (RS rebound → Church stronger) | Guilds financing (ARC 14) can back Parliamentary lobby — Guilds Wealth funds the 1 Wealth lobby cost | Lenneth channel (ARC 15) gives players Crown-Revolution coordination on Parliamentary votes |
| **ARC 12: Maret** | If Torben departs (ARC 11 fail), Maret loses his primary source (Vaynard's leverage over Crown) | — | Maret holds Ceiral knowledge — his fate determines Ritual accessibility | Guilds could finance Maret's independent research (ARC 14) — Maret leaves Varfell to Guilds | Lenneth's network connects to Revolution academics adjacent to Maret's work |
| **ARC 13: Ceiral** | Ritual RS consequence (RS +8 on Failure) spikes RS → Church has less justification for Thread suppression (ARC 11 Church vote changes) | Maret's fate blocks or enables Ritual (holds the preparation knowledge) | — | Guilds has no Thread interest but Wealth could fund Niflhel archive security (Ritual requires archive access) | Lenneth's survey is a secondary Thread-perception account — not the Ritual, but RS +2 (PP-258) |
| **ARC 14: Guilds** | Guilds swing vote is critical in Parliament (ARC 11); financing the lobby is direct integration | Guilds financing Maret (NG-I path) gives Revolution Thread capability | Guilds Wealth can fund Niflhel archive protection (Ritual enabler) | — | Lenneth's Revolution network overlaps with Guild academic contracts — information can flow both ways |
| **ARC 15: Lenneth** | Lenneth channel enables Crown-Revolution Parliamentary coordination (ARC 11) | Lenneth's academic network has contact with Maret's adjacent research community | Lenneth's survey provides RS +2 (PP-258) — minor but real Ritual preparation benefit | Lenneth's foundation funds some Guild-adjacent research — information overlap | — |

**Convergence risk (SIM-ARC-03):** NG-G (Consensus Builder) applied simultaneously to ARC 11 (Parliament window), ARC 12 (Maret 1-scene window), and ARC 15 (Lenneth approach window) closes all three windows in the same season. Three 1-scene windows consumed by internal deliberation produces: Torben departs, Maret crisis deferred to Heresy Investigation, Lenneth network inaccessible at standard Ob. Single-archetype pattern creates maximum simultaneous exposure.

**Synergy path (all new archetypes avoided):** ARC 15 (Lenneth channel established) → ARC 11 (Crown-Revolution coordination blocks demand) → ARC 14 (Guilds financing secured, Guilds activated) → ARC 12 (Maret independent contractor, Ceiral accessible) → ARC 13 (Ritual attempted with preparation, Maret's notes, RS in range). Full chain requires 4–6 seasons of active play. Each arc's optimal outcome enables the next.

---

## Simulation Findings Summary (SIM-ARC-03)

| Finding | Arc | Mechanic | Severity |
|---------|-----|----------|----------|
| F-ARC3-01 | ARC 11 | NG-G: 1 season of internal consensus-building consumes the entire Parliamentary window; TC-dependent result varies but players spent nothing to achieve it | High — window-sensitive |
| F-ARC3-02 | ARC 11 | NG-K: Full-season Varfell TK investigation when 1 scene suffices; Guilds unlobbied; same outcome as NG-G | Medium — information vs action trade |
| F-ARC3-03 | ARC 11 | NG-I: Refusing Parliamentary mechanics to protect Torben produces Torben in Altonia via harder retrieval route | High — protection instinct backfires |
| F-ARC3-04 | ARC 11 | NG-L: 2 Momentum on Ob 1 Circles warm-up depletes Momentum before contested Ob 3 lobby; success probability 80% → 55% | Medium — misallocated resource |
| F-ARC3-05 | ARC 12 | NG-I: Not pressuring Maret produces 30% chance Vaynard acts unilaterally; 70% chance deferred Heresy Investigation | High — deferred crisis |
| F-ARC3-06 | ARC 12 | NG-H: Stale Varfell Influence data (4→3) removes credibility from argument; effective Ob rises 2→3; P(success) 82%→72%; fail branch = worst outcome (Church report) | High — stale data error |
| F-ARC3-07 | ARC 12 | NG-J: Refusing to use Thread impression knowledge protects Maret's autonomy; Vaynard acts without player input regardless | Medium — principled constraint produces same outcome as inaction |
| F-ARC3-08 | ARC 13 | NG-K: 1 season over-research closes the RS window; Ritual becomes impossible this arc | Critical — window closed by information-seeking |
| F-ARC3-09 | ARC 13 | NG-H: Applying Weaving RS cost (−4) to POP Foundational (×3 multiplier) → players expect RS −4 buffer; actual Failure = RS +8; catastrophic surprise | Critical — category error in precedent application |
| F-ARC3-10 | ARC 13 | NG-L: 3 Momentum on Ob 1 Diagnosis; Ritual at Ob 9 without Momentum; P(success) 15% → 4% (factor of 4 reduction) | Critical — highest-stakes misallocation in batch |
| F-ARC3-11 | ARC 13 | NG-J: Not reading Maret's notes +2 Ob on Ob 9 Ritual → P(success) 4% → 0.5%; effectively impossible | High — ethical constraint makes impossible more impossible |
| F-ARC3-12 | ARC 14 | NG-G: Equal distribution of Guilds support depletes Wealth in 2 seasons; no decisive advantage; Church penalty same as targeted route | High — fair distribution is strategically equivalent to inaction |
| F-ARC3-13 | ARC 14 | NG-J: Transparency with all factions enables Church 55% counter-action; arrangement destroyed before use in majority of cases | Critical — disclosure enabled the opponent |
| F-ARC3-14 | ARC 14 | NG-H: Skipping Circles establishment; +1 Ob on Guilds negotiation; P(agreement) 88% → 72%; faster depletion | Medium — relationship infrastructure has mechanical value |
| F-ARC3-15 | ARC 15 | NG-I: Pure altruism approach (no structural exchange) raises Ob 2→3 for Consequence NPC; possible network withdrawal | Medium — Consequence mode requires reciprocal structural logic |
| F-ARC3-16 | ARC 15 | NG-H: Threat-framing as Consequence-mode argument works with some NPCs, not Lenneth; Ob 2→4 | High — same register, different NPC response profile |
| F-ARC3-17 | ARC 15 | NG-J: Disclosure before approach triggers Lenneth defensive response; Ob 2→3; 28% chance network destroyed permanently | High — principled disclosure is adversarial in this context |
| F-ARC3-18 | ARC 15 | NG-G: Internal consensus delays approach; Lenneth becomes more cautious from staff rumours; Ob 2→3 | Medium — delay makes target harder |

**Systemic findings (SIM-ARC-03):**

1. **Window failures dominate NG-G and NG-K:** Every arc in this batch has a 1-scene or 1-season window. NG-G (Consensus Builder) and NG-K (Completionist) close windows through process rather than error. The players' internal logic is correct; the window doesn't wait for it.

2. **Disclosure paradox (NG-J):** Disclosure raises Ob uniformly (Lenneth, Guilds, Maret-via-Vaynard). The clean hands instinct assumes disclosure is neutral or trust-building. In Valoria's mechanics, disclosure to a Consequence-mode NPC means showing your hand before the exchange is established. The optimal path — structural implication rather than disclosure — is more honest in the sense that it presents what the players actually want (a productive arrangement) rather than what they know (surveillance-derived information).

3. **Precedent failures narrow by context (NG-H):** Each NG-H failure in this batch is distinct: stale faction data (ARC 12), wrong RS cost category (ARC 13), skipped relationship step (ARC 14), wrong register within correct mode (ARC 15). The Precedent Follower applies the right method (Consequence mode, Wealth exchange, Circles relationship) but with context-specific errors that prior experience didn't expose.

**Test ID:** SIM-ARC-03
**Mechanics:** Parliamentary Vote, Torben Loyalty Clock, Maret Loyalty Track, Ceiral Ritual (POP Foundational), Guilds financing, Crown-Revolution channel, Lenneth hidden networks, RS ×3 consequence, IP threshold
**Mode:** TTRPG primary
**Temporal:** Multi-season, cross-arc, 1-scene window mechanics prominent
**Tracks:** IP, TC, RS, Torben Loyalty, Maret Loyalty, Mandate, Stability, Influence, Wealth, Thread Sensitivity
**Factions:** All eight; Guilds central in ARC 14
**NPCs:** Almud, Lenneth, Torben, Vaynard, Maret, Baralta (referenced), Himlensendt (referenced)
**Archetypes:** NG-G through NG-L (all six new non-greedy archetypes)
