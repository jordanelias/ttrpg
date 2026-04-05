# Valoria — Emergent Narrative Arcs: Irrational Player Behaviour Stress Test
## Generated: 2026-04-04 | Model: Sonnet 4.6
## Source authority: stage6_factions.md, stage12_campaign_modes.md, stage13_npcs.md, params_core.md

---

## Irrational Player Archetypes

Before arcs: the six human-play patterns injected as non-optimal choice nodes. These are not rules violations — they are recognisable table behaviours that produce mechanically incoherent results.

| Code | Archetype | Behaviour |
|------|-----------|-----------|
| IP-A | **The Fixated** | Pursues one Belief obsessively regardless of changed circumstances. Spends all Momentum on that Belief even when doing so collapses other tracks. |
| IP-B | **The Diplomatic Idealist** | Attempts to negotiate with every faction including active enemies. Rolls social when combat is required. Triggers Ethical Framework penalties by refusing actions that violate personal values even when mechanically optimal. |
| IP-C | **The Thread Maximiser** | Every scene, attempts a Thread operation regardless of Rendering Stability (RS) level or personal Coherence. Treats Thread as the answer to non-Thread problems. |
| IP-D | **The Hoarder** | Never spends Momentum. Saves Wealth faction contributions. Refuses to commit resources until a "perfect moment" that never arrives. |
| IP-E | **The Splitter** | When the party faces a two-front problem, splits the group — each Player Character handles one front alone, halving all pools. |
| IP-F | **The Confronter** | Escalates every social scene to a direct challenge before Reading the Room. Misidentifies Resonant Styles. Always opens with the wrong mode (Character when the Non-Player Character responds to Consequence, etc.). |

Notation in flowcharts: optimal path = solid line; irrational branch = dashed line; irrational code in `[brackets]`.

---

## ARC 1: The Succession Weapon

### Mechanical Seed
Theocracy Counter (TC) crosses threshold 30 → Church institutional pressure fires → Himlensendt invokes doctrine (Domain Action: Influence attack on Crown Mandate) → King Almud's Sovereign Constraint activates → Torben loyalty clock becomes contested asset.

### Narrative

The players will first notice something is wrong with the Church through small things: a sermon referenced in passing, a minor official refusing to confirm a merchant's contract without a tithe review, a locked archive that was open last season. No one announces that Confessor Arne Himlensendt has decided to move.

By the time the Theocracy Counter crosses 30, the Church has already run two Domain Actions — one to increase its Influence in the southern parishes, one to reduce the Crown's Mandate among the commons by seeding a scandal about treasury mismanagement. Players watching only the explicit scene layer will have seen neither. Players watching faction stats will notice Crown Mandate has dropped one. If they investigate, the trail leads to a retired clerk named Vaynard who, under pressure, reveals he passed documents to a Church representative.

The lever the Church pulls is Torben. When Institutional Pressure reaches 30, Altonia's education demand arrives — and Himlensendt uses his Influence network to ensure it arrives with Church endorsement. Torben leaves Valoria. The Torben Loyalty Clock starts counting.

Now the players face a structural problem, not a villain to fight: the king cannot act without collapsing his coalition, the Church is acting within its formal authority, and Altonia is a foreign power with trade leverage. Every route to stopping Torben's drift requires sacrificing something. The arc ends in one of three states — Torben retrieved, Torben Altonian, or Torben dead — and every ending rewrites the succession entirely.

### Flowchart

```mermaid
flowchart TD
    A["TC crosses 30\n[Theocracy Counter threshold — stage12 §12.3]"]
    A --> B["Church Domain Action: Influence attack\nvs Crown Mandate\n[Domain Ob = Crown Mandate 5; Church Influence 6D TN7]"]
    B --> C{Outcome}
    C -->|"Partial/Fail\n(Church net < 5)"| D["Crown Mandate holds\nChurch plots longer-term\n[next attempt Season +2]"]
    C -->|"Success/Overwhelming\n(Church net ≥ 5)"| E["Crown Mandate −1 (now 4)\nSovereign Constraint pressure increases"]
    E --> F["Institutional Pressure reaches 30\nAltonian Education Demand triggers\n[stage13 §13.1 Torben]"]
    F --> G{Player response}

    G -->|"Optimal: Investigate Church-Altonia link\n(Circles Ob 3 + Intel scene)"| H["Evidence gathered\nElske recruitable\n[stage13 §13.1 — Resonant Style: Evidence]"]
    H --> I["Debate Himlensendt with Evidence\nvs Composure 12, Ob 3\n[Debate system — asymmetric]"]
    I -->|"Success"| J["Church withdraws Altonian endorsement\nTorben departure delayed 1 season"]
    I -->|"Fail"| K["Torben departs\nLoyalty Clock starts at 8"]

    G -.->|"[IP-F] Open with direct accusation\nno evidence gathered"| L["Himlensendt Composure 12\nWrong Resonant Style: Character used vs Consequence NPC\n+1 Ob penalty — Ob 4 effective"]
    L --> M["Near-certain Debate loss\nChurch Stability +1 (martyrdom effect)\nKing Almud public rebuke of players"]
    M --> K

    G -.->|"[IP-B] Attempt to negotiate with Altonia\ndirectly — foreign territory"| N["Circles Ob 3 to reach Altonian contact\nNo faction backing = −2D\n[pool likely 3D vs Ob 3 = ~45% success]"]
    N -->|"Fail"| O["Altonian Intel +1 (players identified)\nTorben departure accelerated to this season"]
    N -->|"Success"| P["Temporary delay 1 season\nbut no structural fix — demand repeats"]

    K --> Q["Torben Loyalty Clock 8 → tracks down\n[stage13 §13.1 loyalty table]"]
    Q --> R{Loyalty at season end}
    R -->|"≥6"| S["Retrieval straightforward\nArc ends — minor Crown cost"]
    R -->|"4-5"| T["Crown Mandate −1\nRetrieval requires Altonian consent\nor covert extraction — Military/Intel action"]
    R -->|"≤3"| U["Löwenritter coup trigger #2 approaches\nElske becomes only viable heir\n→ Arc feeds into ARC 3"]

    G -.->|"[IP-D] Hoard Momentum — refuse\nto spend on Circles rolls"| V["Circles attempt at base pool\n(no Momentum expenditure)\n~30% success rate vs Ob 3"]
    V -->|"Fail (likely)"| O

    D --> W["Church bides — other arcs accelerate\n[feeds ARC 2: RS erosion]"]
```

### Footer

No player designed this arc. It emerges from TC threshold mechanics, the Torben Loyalty Clock, and Himlensendt's Beliefs running in parallel without player input. Arc shape: 3–4 seasons, compressed in BG mode to 1 session. Endgame indicator: succession resolved or definitively broken.

**Irrational behaviour findings:**
- IP-F (Confronter): Misidentifying Himlensendt's Resonant Style (Consequence, not Character) costs +1 Ob on the critical Debate, making loss near-certain. Church Stability bonus from martyrdom effect compounds — the players made Himlensendt stronger.
- IP-B (Diplomatic Idealist): Negotiating with Altonia directly exposes the players as foreign operatives in Altonian territory, accelerating Torben's departure rather than delaying it. Good intention, structural failure.
- IP-D (Hoarder): Withholding Momentum on the Circles roll against Ob 3 with a likely 4D pool drops success probability from ~80% to ~45%. The single point of Momentum expenditure was the correct play; saving it produces a bad outcome and doesn't use the Momentum for anything better.

---

## ARC 2: The Rendering Stability Drain

### Mechanical Seed
One Thread practitioner Player Character runs operations every scene for 3 seasons without Thread management → Rendering Stability (RS) decays to threshold 50 → world-legibility effects begin → non-practitioner factions notice anomalies → Varfell mobilises its intelligence network → Church interprets manifestations as heresy → Institutional Pressure spike.

### Narrative

The players won't notice the drain from their side. The Thread practitioner is doing what Thread practitioners do — Leaping when there's an advantage, running Diagnosis on Unstable threads, occasionally overreaching. Each operation costs RS fractions and no single scene looks alarming.

What they will notice is the world getting strange at the edges. A trade document from Hafenmark arrives with an ink error that shouldn't exist — a word in a dead form, no longer used. An old man in the market describes a road that isn't there and has never been. A miller's dog won't stop barking at a wall. These are not random events — they are RS manifestations: the substrate producing legibility failures as it degrades. Players who don't understand what Rendering Stability is will try to investigate these incidents as normal mysteries. They are not mysteries. They are symptoms.

By the time RS crosses 50, Varfell's intelligence network has logged enough anomalies to flag a "thread-active zone" to their leadership. They don't announce this. They move an agent to the town. Meanwhile, the Church's perception is different: Himlensendt's theological framework converts the anomalies into evidence of heresy. He doesn't know he's wrong. His institutional perceptual prophylaxis prevents him from making the causal inference a practitioner would make. He knows something is happening. He concludes it is spiritual corruption. He begins an inquiry.

The players are now being watched by two factions for completely different reasons, and the correct mechanical response — reduce Thread operations, restore RS — is the one response that feels like giving up power.

### Flowchart

```mermaid
flowchart TD
    A["Player Character Thread practitioner\noperates every scene\n[RS decays at rate ~2–4/operation depending on Ob]"]
    A --> B["RS crosses 72 → no effect\nRS crosses 60 → minor legibility noise\n[params_threadwork: RS threshold table]"]
    B --> C{Player response at RS 60}

    C -->|"Optimal: reduce operations\nthread management scene\n[RS restoration: Spirit+Attunement vs Ob 2]"| D["RS stabilises 58–62\nFaction surveillance does not trigger\nArc deflates — minor"]

    C -.->|"[IP-C] Thread Maximiser: continues\noperating regardless"| E["RS continues decay\ncrosses threshold 50"]

    E --> F["RS 50 effects:\nLegibility failures visible to civilians\nVariances in physical/social terrain\n[stage12 §12.2 endgame indicator band]"]
    F --> G["Varfell Intel action fires automatically\n[Institutional Tendency: map anomalies]\nVariances logged over 2 scenes"]
    F --> H["Church interprets anomalies as heresy\nHimlensendt — Institutional Pressure +2\n[stage6 §8 Church ethical framework]"]
    G --> I["Varfell moves agent into area\nIntel +1 vs players' faction\n[Domain Action: Intel surveillance]"]
    H --> J["Church begins formal inquiry\nTheocracy Counter +3 if inquiry formalized\n[Domain Action: Institutional Pressure attack]"]

    I --> K{Players detect Varfell agent?}
    K -->|"Attunement+Intel Ob 3 (opposed by agent Intel 4)"| L["Agent identified\nVarfell contact scene available\n[Axis 7: Information vs Secrecy]"]
    K -->|"Fail"| M["Varfell gains full intelligence on Thread operations\nfaction stat advantage next contested action"]
    L --> N["Players can share RS data with Varfell\n→ Varfell joins restoration effort\n[Domain Action: Wealth→RS restoration]"]

    J --> O{Players respond to Church inquiry}
    O -->|"Optimal: Provide cover story\nvs Cognition+History Ob 3"| P["Inquiry stalled 1 season\nThread operations must stop"]
    O -.->|"[IP-C] Continue Thread ops during inquiry\n— operational need justification"| Q["RS drops below 40\nThread operation now sets Ob at TN 8\n[params_threadwork: TN 8 for Desperate operations]"]
    Q --> R["Operation pool collapse:\ne.g. Spirit 4+Attunement 3+TPS 3 = 10D\n@ TN8: E[net] = 2.0 vs Ob 2 standard\nstill functional — but Ob rising with RS"]

    O -.->|"[IP-F] Confront Himlensendt directly\nabout Thread truth\n[Axis 9: Ontological]"| S["Church ethical framework: +2 Ob\nfor revealing Thread truth\nHimlensendt Composure 12, effective Ob 5\nPlayers need net 5+ against pool ~8D TN7"]
    S -->|"Fail (likely — ~35% at 8D)"| T["Theocracy Counter +5\nChurch formally declares heresy\nPlayers marked — Institutional Pressure spike"]
    S -->|"Success (rare)"| U["Himlensendt shaken — 1 season\nbut institutional momentum continues without him\n[Leader vs Institution rule]"]

    N --> V["RS restoration: Varfell Domain Action\nWealth 5D vs Ob 3\n~88% success\nRS +8 (restoration effect)"]
    P --> V
    V --> W["RS stabilises 48–56\nArc moves to monitoring phase\nfaction relationships permanently shifted"]

    T --> X["ARC feeds ARC 1 (TC spike)\nand ARC 4 (Church military action)\n→ multi-arc convergence"]
```

### Footer

Emerges from the RS decay mechanic running in the background while players pursue unrelated Beliefs. No faction player designed the Varfell surveillance or the Church inquiry — both fire automatically from their Institutional Tendency when RS crosses threshold. Arc shape: 2–3 seasons building, 1 season crisis. Critical in all three modes but most visible in TTRPG.

**Irrational behaviour findings:**
- IP-C (Thread Maximiser): The key failure is not immediate — the pool numbers remain functional down to RS 50 (TN shift). The failure is *political*: the Thread operations are legible to factions before they become mechanically limiting. By the time the Maximiser notices mechanical degradation, the Church inquiry is already filed and Varfell has the intelligence. The mechanic punishes the archetype through surveillance, not through pool collapse.
- IP-F on Himlensendt: The +2 Ob for Thread truth revelation is the Church's hardest modifier. Even a well-built Debate pool (~8D) has only ~35% success against effective Ob 5. The confrontation route is nearly a guaranteed Theocracy Counter spike. Most tables will not see this coming.

---

## ARC 3: The Löwenritter Legitimacy Problem

### Mechanical Seed
Löwenritter Military 5 + Lowenritter no Mandate stat → they can win battles but cannot govern → if coup triggers, Löwenritter hold capital without legitimacy infrastructure → Stability degrades automatically → Revolution Influence grows in vacuum → forced Coalition or collapse.

### Narrative

The Löwenritter are not a faction the players are meant to fight. They are a faction whose logic is legible and internally consistent, and that is what makes them dangerous. Their coup isn't villainy — it is the rational consequence of watching the Crown fail on multiple axes simultaneously. The players will know the coup is possible before it happens; they can read the trigger conditions in faction behaviour. Whether they act on that knowledge depends entirely on what their Beliefs say.

After the coup, if it happens, the city feels different. The Löwenritter have Military presence everywhere. Supplies move. People follow orders out of fear or relief depending on where they sit. But no one is holding the civic fabric together — the guilds are frozen, the parish priests are receiving no guidance, the merchant dispute system has no authority to refer to. Within one season, the Löwenritter are doing something they were not designed to do: governing. They are failing at it methodically, and their Stability is declining one point per accounting cycle.

The Revolution, watching from outside, sees an opportunity. A faction with no Mandate has created a power vacuum that Influence and Stability can fill. The players are caught between a military government that's losing control and a popular movement that has never held power and has no Wealth. If they help neither, the arc resolves without them, messily. If they help one, they own the consequences.

### Flowchart

```mermaid
flowchart TD
    A["Coup triggers — any 2 of 3 conditions met:\n1. Crown Mandate ≤ 2\n2. Torben loyalty ≤ 3 OR heir compromised\n3. RS ≤ 40 + Church declares heresy"]
    A --> B["Löwenritter Military Domain Action:\n5D vs Crown Military 4 (Ob 4)\nE[net] = 1.5, P(success) ≈ 68%"]
    B -->|"Success"| C["Coup successful\nCrown Mandate → 0 (temporary — no Mandate stat available to Löwenritter)"]
    B -->|"Fail"| D["Coup suppressed\nLöwenritter Stability −2, Intel −1\nCrown Mandate +1 (popular legitimacy)"]

    C --> E["Governing phase begins\nLöwenritter Stability 5 → automatic −1/season\n(no Mandate infrastructure to stabilise)"]
    E --> F["Season 1 post-coup:\nRevolution Influence 3D vs vacuum Ob 1\n~98% success\nRevolution Influence +1"]
    F --> G{Player response Season 1}

    G -->|"Optimal: Support Löwenritter\nwith legitimacy infrastructure\n[Guilds Domain Action: Wealth→structure]"| H["Guilds Wealth 6D vs Ob 2 = ~97%\nLöwenritter Stability holds at 5\nRevolution Influence growth stalled"]
    G -->|"Optimal: Support Revolution\n[Circles Ob 2 to contact Edith Varn]"| I["Revolution gains organised structure\nInfluence +2 over 2 seasons\nLöwenritter Military response probable"]

    G -.->|"[IP-A] Fixated on old Belief:\n'Restore the Crown'\n— Crown effectively gone"| J["Players spend all Momentum on\nCircles rolls to find Crown loyalists\n(Ob 4 — scattered, unfunded)\n~50% success per attempt"]
    J -->|"Fail repeatedly"| K["Löwenritter Stability declines unchecked\nRevolution fills vacuum without player help\n— arc resolves without Player Characters"]
    J -->|"Success after 3 seasons"| L["Crown loyalist faction formed\nThree-way contest: Löwenritter/Revolution/Crown\n— longer arc, more volatile"]

    G -.->|"[IP-E] Split party:\nOne Player Character to Löwenritter\nOne Player Character to Revolution"| M["Each Player Character acting alone\npool halved — Circles at −2D each\nBoth negotiations at ~50% vs optimal ~80%"]
    M -->|"One or both fail"| N["Neither faction stabilised\nLöwenritter Stability −2 that season\nRevolution Influence +2 that season\nConflict timeline accelerated by 1 season"]
    M -->|"Both succeed"| O["Both factions stable but opposed\nPlayers have agents in both camps\n— information advantage, conflict locked in"]

    G -.->|"[IP-D] Hoard Wealth\n— 'we need it for later'"| P["No economic stabilisation action\nGuilds do not act without Player Character direction\nLöwenritter Stability −1, Wealth vacuum continues\n→ same as uncontested Revolution path"]

    H --> Q["Coalition government:\nLöwenritter Military + Guild administration\nStability recovers to 4\nTC decreases (Church loses leverage)"]
    I --> R["Revolution takes power Season 3–4\nWealth 0 — immediate economic crisis\nMilitary confrontation if Löwenritter resist"]
    L --> S["Succession resolved violently or through\nlong Parliament negotiation\n→ feeds endgame indicators"]
    N --> T["Civil conflict erupts Season 3\nRS takes collateral damage −5\n→ feeds ARC 2"]
```

### Footer

Emerges from Löwenritter's partial stat sheet (no Mandate) colliding with coup trigger conditions. The faction was never designed to govern — the absence of a Mandate stat is a structural design choice, not an oversight. Arc shape: 4–6 seasons if players engage; 2–3 if they don't. Most impactful in TTRPG mode; abstracted to single Military vs Stability contest in BG mode.

**Irrational behaviour findings:**
- IP-A (Fixated): "Restore the Crown" is not a wrong Belief — it is a mechanically expensive one. The Crown loyalists exist, but finding them costs Ob 4 Circles rolls repeatedly at low success rates. Meanwhile, the Löwenritter Stability clock does not pause. The arc resolves around the players, not through them. The Fixated archetype produces the most interesting emergent outcome: a three-way contest no one planned.
- IP-E (Splitter): Halved pools produce a ~30% success-rate penalty on Circles. The loss probability compounds: if each independent negotiation has ~50% success, both succeeding is 25%. The likely outcome (one or both fail) accelerates the timeline by a full season, pushing the arc into crisis before players have leverage.
- IP-D (Hoarder): The economic stabilisation action requires no Momentum — it uses Guilds Wealth 6D. The Hoarder refuses anyway, holding faction Wealth "for emergencies." The emergency is this. The unwillingness to commit resources is mechanically identical to taking no action.

---

## ARC 4: The Thread Truth Cascade

### Mechanical Seed
Axis 9 (Ontological) resolved publicly → Thread truth becomes common knowledge → Church Theocracy Counter collapses (−20 minimum) → Church Stability crisis → Himlensendt's institutional power breaks → vacuum in moral authority → all factions reposition on Axis 1 (Sovereignty) simultaneously → political cascade.

### Narrative

The players will probably not mean to resolve Axis 9. It will happen because one scene went further than expected — a Thread demonstration in public, an Inquisitor who saw something and lived, a document recovered from Niflhel that was too specific to deny. Resolving Axis 9 means the world now knows that the substrate of reality is mutable, that practitioners can move it, and that the Church has been systematically suppressing that knowledge for at least a century.

The immediate effect is not what players expect. There is no riot, no sudden collapse. There is a silence. People do not process ontological revelations quickly. What they process quickly is that the institution they were told to trust lied to them about the most fundamental question there is. That anger takes two to three scenes to become organised. When it does, it moves faster than any Domain Action.

Himlensendt does not lose faith. That is the thing. His theological framework simply — converts. He finds a new interpretation that maintains Church authority while accepting the physical reality of Thread. He is now more dangerous, not less: a sophisticated institution adapting rather than collapsing. The Church's Theocracy Counter drops, then stabilises. What the players thought they had destroyed has become something different.

Meanwhile, every other faction repositions. The Crown can now openly acknowledge what Almud has always privately suspected. The Guilds see commercial opportunity in legitimate Thread services. Varfell — the faction that was already there — finds itself suddenly central rather than marginal. The Revolution, which used Thread truth as a political weapon, must decide what it stands for now that the weapon has fired.

### Flowchart

```mermaid
flowchart TD
    A["Axis 9 resolution event:\nPublic Thread demonstration OR\nDocument release OR\nInquisitor testimony\n[stage6 §8.1 Nine Political Axes]"]
    A --> B["Church ethical framework fires:\n+2 Ob on any action to suppress\n(institutional perceptual prophylaxis now fails)\n[stage6 §8.3 Church framework]"]
    B --> C["TC −20 (minimum) — automatic\n[Threshold: TC below 20 = Church authority broken indicator\nstage12 §12.1 endgame indicators]"]
    C --> D{"TC position before revelation"}
    D -->|"TC was 50–70 → now 30–50"| E["Church weakened but functional\nHimlensendt adaptation begins\n2 seasons to new doctrine"]
    D -->|"TC was 30–50 → now 10–30"| F["Church in crisis\nStability −2 this season\nTemplar independence fractures"]
    D -->|"TC was 15–30 → now 0–10"| G["Church collapses institutionally\nEndgame indicator: Church broken\nMoral authority vacuum — all factions scramble"]

    E --> H{Player response to adapting Church}
    H -->|"Optimal: engage Himlensendt\nwith Evidence on doctrine\n[Resonant Style: Consequence — Ob 3]"| I["Debate succeeds on Evidence\nNew doctrine shaped by Player Character input\nChurch emerges as Thread-acknowledging institution"]
    H -.->|"[IP-F] Confront directly\n— 'you were lying'"| J["Accusation mode vs Consequence NPC\n+1 Ob (wrong style) + weakened Church context\nHimlensendt: Composure 12 still holds\n~55% success at best 10D pool"]
    J -->|"Fail"| K["Church adapts without player input\ndoctrine hostile to practitioners\nVarfell excluded — Axis 2 re-opens"]
    J -->|"Success"| L["Partial doctrine influence\nbut relationship with Himlensendt permanently adversarial"]

    F --> M["All factions begin Axis 1 repositioning\nCrown: Mandate +1 (fills vacuum)\nGuilds: Influence +1 (commercial opportunity)\nRevolution: Stability +1 (validation)\nVarfell: Influence +2 (central now)\n[Domain Actions fire simultaneously — 1 season lag]"]
    M --> N{Players direct any faction repositioning?}

    N -->|"Direct Crown: support Almud\n[Virtue Ethics: visible public support = −1 Ob]"| O["Crown Mandate Domain Action\nPool: 5D + player pool (if leadership)\nvs Ob 3 (multiple competitors)\nP(success) ≈ 82%\nCrown becomes dominant faction"]
    N -->|"Direct Varfell: operationalise Thread services"| P["Varfell Influence 4D vs Ob 2\nP(success) ≈ 93%\nThread economy begins — RS restoration viable\nas commercial service"]
    N -.->|"[IP-C] Player Character Thread operations\nat all revealed locations\n— 'demonstrate capability'"| Q["RS −8 over 2 scenes\n(multiple operations, Rendering Stability burn)\nRS may cross 40 if already degraded\nARC 2 re-activates"]

    N -.->|"[IP-B] Negotiate with all factions\nsimultaneously\n— 'everyone should benefit'"| R["Circles Ob 3 × 4 factions\neach contested by competing factions\nPlayers at ~50% per roll without faction backing\n3 of 4 likely fail"]
    R --> S["Players perceived as committed to nobody\nFaction relationship penalty: −1 with all contacted factions\n(wasted their time)"]

    G --> T["Moral authority vacuum:\nNo faction has Mandate above 3 simultaneously\nendgame indicator fires\nGM signals: 2–3 sessions to final resolution"]
    T --> U{Players have dominant faction alliance?}
    U -->|"Yes"| V["Allied faction drives ending\nplayers shape final doctrine/governance"]
    U -->|"No — IP-B or IP-D pattern"| W["Ending driven by Non-Player Character Beliefs\nBaralta or Himlensendt adaptation determines outcome\nPlayer Characters present but not central"]

    I --> X["Integrated ending:\nThread economy + reformed Church + stable Crown\nRS restoration trajectory begins"]
    O --> X
    P --> X
    K --> Y["Fractured ending:\nThread suppression continues covertly\nAxis 2 remains live\n→ campaign extension or sequel seed"]
    S --> W
    Q --> Z["RS-crisis ending:\nPhysical substrate damaged\nRupture risk within 2 seasons\n→ feeds ARC 2 endgame"]
```

### Footer

Axis 9 resolution is an endgame indicator, not a mid-arc event — this arc only fires in a late campaign. No player can deliberately trigger it cleanly; it emerges from accumulated scenes where Thread truth leaked incrementally. Arc shape: 1–2 seasons of cascade, then resolution. In BG mode, compressed to single TC threshold event with faction repositioning table.

**Irrational behaviour findings:**
- IP-C (Thread Maximiser): The revelation scene creates a window where Thread operations are *expected* — the world knows they exist. The Maximiser reads this as permission. The RS burn from multiple demonstration operations during the cascade can push RS below 40, re-triggering ARC 2 at exactly the moment the political situation is most volatile. Two simultaneous crises (RS collapse + political cascade) is the most punishing combined outcome.
- IP-B (Diplomatic Idealist): Negotiating with all four repositioning factions simultaneously is the "fair" play — everyone benefits. Mechanically, it fails because faction-backed rolls are required to clear Ob 3, and the players have not committed to any faction. All four rolls are at base pool without bonus dice. Expected outcome: 1 of 4 succeeds. The players spent 4 actions to achieve what 1 focused action would have.
- IP-F: Himlensendt post-revelation is in a weaker political position but still has Composure 12. The confrontation impulse ("you were lying") is understandable but still targets the wrong Resonant Style. The Consequence-focused NPC responds to structural reasoning, not moral accusation. Even a weakened Church produces a doctrine hostile to practitioners if the social scene fails.

---

## ARC 5: The Niflhel Provenance

### Mechanical Seed
Niflhel (no Mandate, no Military, partial sheet) holds historical documents → players discover Niflhel has pre-Galbados Thread records → Church learns players are accessing Niflhel → Intel war begins → Niflhel's Stability becomes the central contested asset → documents change the RS mechanics themselves if published.

### Narrative

Niflhel barely registers in the early campaign. They have Influence and Stability and nothing else. Players treating factions as power-players will ignore them — no Military, no Mandate, what threat do they pose? The answer is that Niflhel is the only faction holding memory. They have records of what the world looked like before Galbados rewrote the ontological consensus. Those records are not magical — they are historical, specific, boring to read. Thread Sensitivity 50+ practitioners who encounter them will have a different experience.

The arc begins when a player character who has never seen a pre-Galbados account reads one and the text does something no text should do: it describes a physical sensation of Thread contact that the reader feels. The document is not performing a Thread operation — it is a sufficiently accurate first-person account that the substrate responds to being read. Niflhel's leadership, who have kept the documents without understanding them, watches this happen and reassesses everything.

Now Niflhel wants something. They have leverage they didn't know they had. The Church knows the documents exist — their Intel network flagged the access. Himlensendt's institutional perceptual prophylaxis means he doesn't understand what the documents are, but he understands they are dangerous. The Church begins an Intel action to locate and destroy the archive. Niflhel's Stability is the only thing standing between the documents and the fire.

The players must decide whether to use the documents (RS consequences), protect them (Intel and social mechanics), or release them (triggers ARC 4). All three are legitimate choices with mechanical teeth.

### Flowchart

```mermaid
flowchart TD
    A["Players access Niflhel archive\n[Circles Ob 2 to establish Niflhel contact\nNiflhel Influence 5 available as introduction path]"]
    A --> B["Thread Sensitivity 50+ Player Character:\npassive contact with pre-Galbados document\n[RS +3 — substrate responds to accurate account]"]
    B --> C["Niflhel leadership reassessment\nNiflhel Stability holds — they want negotiation\n[Institutional Tendency: preserve and leverage]"]
    C --> D["Church Intel fires:\nIntel network detects Niflhel archive access\n[Church has no Intel stat — proxied via Influence 6]\nIntel action: Influence 6D vs Niflhel Stability 4\nOb 4; P(Church success) ≈ 70%"]
    D -->|"Church success"| E["Church knows document location\nPlanning destruction action — 2 season delay\n(logistical + ethical framework: overt action = +1 Ob)"]
    D -->|"Church fail"| F["Church suspects but cannot locate\nNiflhel has 2 extra seasons of safety"]

    E --> G{Players respond to Church surveillance}
    G -->|"Optimal: Niflhel Intel defence\n[proxy: Influence 5D vs Church Ob 3]"| H["P(success) ≈ 88%\nChurch loses document location\nBack to fail path — 2 seasons additional safety"]
    G -.->|"[IP-D] Hoard documents\n'don't use them yet — too risky'"| I["Documents safe but unused\nChurch search continues each season\nOdds compound: by Season 3, P(Church find) ≈ 91%\ndespite early fail"]
    I --> J["Church finds and destroys archive\nPlayers had the documents and produced nothing\nNiflhel Stability −2, Influence −1\n[maximum bad outcome from caution]"]

    G -.->|"[IP-A] Fixated on publishing immediately\n— 'people must know'"| K["Release triggers ARC 4 (Axis 9 resolution)\nbut RS at current level — may not survive cascade\nif RS already degraded (< 55)"]
    K -->|"RS ≥ 55"| L["ARC 4 fires — survivable cascade\nPlayers gave up leverage for principle\nNiflhel relationship ends (documents gone)"]
    K -->|"RS < 55"| M["ARC 4 + ARC 2 simultaneous\nRS crisis + political cascade\nMost volatile possible outcome"]

    G -.->|"[IP-E] Split party:\nOne guards documents\nOne negotiates with Church"| N["Guard: alone vs potential Church extraction team\nCombat pool halved if confrontation\n[Military 4D Church vs single Player Character]"]
    N -->|"Guard overwhelmed"| O["Documents destroyed\nPlayer Character captured or wounded\nChurch Intel +2 (they know what they found)"]
    N -->|"Guard holds — unlikely at halved pool"| P["2-season delay but Church now knows\nlocation exactly — next attempt harder"]

    H --> Q{Players negotiate with Niflhel}
    Q -->|"Niflhel asks: RS restoration\nif documents used safely"| R["Players control document access\nThread practitioners can use documents\nas RS restoration catalyst\n[RS +5 per controlled study session\nvs RS −2 per normal operation]"]
    Q -->|"Niflhel asks: protect them\nfrom all factions"| S["Niflhg Stability becomes player-sponsored\nDomain Action: Influence support\nvs Church Ob 3 each season\nP(success) ≈ 72% — sustainable but costly"]

    R --> T["Document study programme:\nRS net +3/season (restore − operation cost)\nNiflhel Stability +1 (legitimacy from purpose)\nChurch Theocracy Counter −5 (over 3 seasons)\nas Thread truth leaks incrementally"]
    S --> U["Documents preserved — no RS benefit\nChurch search continues but blocked\nArc extends until players choose release or use"]

    T --> V["Controlled Axis 9 resolution path:\nThread truth emerges gradually\nChurch has time to adapt (Himlensendt)\nTC drops 15 over 4 seasons vs 20 in one event\n→ softer landing than sudden ARC 4 trigger"]
    U --> W["Stalemate: documents safe, crisis deferred\nNiflhel Stability 5, protected\nArc becomes background tension\nuntil another arc forces the question"]
    J --> X["Hard loss: documents destroyed\nRS loses restoration pathway\nNiflhel diminished — faction effectively inactive\nPlayers must find alternate RS restoration method"]
    M --> Y["Combined crisis — hardest endgame\nRequires all remaining resources to stabilise\ncan still resolve if faction alliances solid"]
```

### Footer

Emerges from Niflhel's partial stat sheet — they can survive (Stability 4, Influence 5) but cannot project power. The documents are the only leverage they have, and they don't know it at arc start. No player invented this situation; it emerges from Niflhel's institutional structure intersecting with the Church's Intel proxy and the RS restoration mechanic gap. Arc shape: 3–5 seasons; can be compressed or extended depending on player engagement. The document study programme is the only arc that generates net-positive RS over multiple seasons.

**Irrational behaviour findings:**
- IP-D (Hoarder): The most self-defeating play in any arc. Saving the documents produces zero benefit — they degrade in value as the Church search narrows. The Hoarder's caution compounds geometrically against them: each season of inaction increases Church find-probability while granting no RS benefit. Maximum bad outcome (documents destroyed, no use extracted) is the Hoarder's most likely result.
- IP-A (Fixated on publication): Not wrong as a goal — but timing-dependent. Publishing when RS < 55 creates the hardest combined outcome in the game: ARC 2 and ARC 4 simultaneously. The Fixated archetype is least harmful here when RS is healthy; catastrophic when RS is already degraded.
- IP-E (Splitter): The party split against a Church extraction team is the clearest mechanical failure in the batch. A halved combat pool (Military proxy) against a Church Templar unit near-guarantees document loss. The "cover all bases" instinct produces the worst single outcome of any split scenario in these arcs.

---

## Cross-Arc Interaction Table

| | ARC 1: Succession | ARC 2: RS Drain | ARC 3: Löwenritter | ARC 4: Axis 9 | ARC 5: Niflhel |
|---|---|---|---|---|---|
| **ARC 1: Succession** | — | TC spike from Church inquiry accelerates RS decay | Torben loyalty ≤3 is coup trigger #2 | Public destabilisation widens Axis 9 crack | Niflhel documents contain Torben-relevant lineage data [EDITORIAL: ED-NNN — is this canon?] |
| **ARC 2: RS Drain** | Thread anomalies accelerate TC (Church inquiry) | — | RS collapse is coup trigger #3 (crisis condition) | RS must be ≥55 for controlled Axis 9 resolution | Documents provide only net-positive RS pathway |
| **ARC 3: Löwenritter** | Coup removes Crown as stabilising factor | Löwenritter military action adds RS stress (mass battle) | — | Coup accelerates TC collapse (Church loses Crown buffer) | Löwenritter indifferent to documents — but Revolution is not |
| **ARC 4: Axis 9** | Thread truth destabilises succession (Almud's private suspicion now public) | RS cascade if Axis 9 fires at RS < 55 | Political vacuum accelerates if Church collapses simultaneously | — | ARC 5 controlled path is the only soft Axis 9 trigger |
| **ARC 5: Niflhel** | Documents irrelevant to succession unless lineage angle exists | Document study is only net-positive RS path | Revolution would weaponise documents if they gain power | ARC 5 soft path prevents ARC 4 cascade | — |

**Convergence risk:** ARC 1 + ARC 2 + ARC 3 firing simultaneously (Torben gone, RS at 50, coup occurring) produces the hardest possible game state. All three are driven by irrational player behaviour: IP-B accelerates ARC 1, IP-C drives ARC 2, IP-A prevents ARC 3 mitigation. An irrational-archetype party can create all three conditions within 4 seasons without ever intending to.

**Stabilisation path:** ARC 5 document study programme + ARC 3 coalition government + ARC 1 Elske recruitment is the only combination that produces a net-positive trajectory across all arcs without requiring Axis 9 to fire.

---

## Simulation Findings Summary

| Finding | Arc | Mechanic | Severity |
|---------|-----|----------|----------|
| F-ARC-01 | ARC 1 | Himlensendt Resonant Style misidentification costs +1 Ob → near-certain Debate loss → Church Stability bonus from martyrdom (unintended buff) | Medium — recoverable |
| F-ARC-02 | ARC 1 | IP-B Altonian negotiation exposes players as foreign operatives; accelerates Torben departure rather than delaying it | Medium |
| F-ARC-03 | ARC 2 | IP-C Thread Maximiser failure is political (surveillance triggers) before it is mechanical (pool collapse at TN8) — players may not connect cause and effect | High — likely missed |
| F-ARC-04 | ARC 2 | Church +2 Ob for Thread truth revelation makes IP-F confrontation ~35% success — players will not expect the modifier | High — likely attempted |
| F-ARC-05 | ARC 3 | IP-A Fixated "restore Crown" play resolves arc without players — three-way contest emerges autonomously | Low severity, high interest — good emergent play |
| F-ARC-06 | ARC 3 | IP-E Splitter halved pools produce ~25% joint-success probability → arc timeline accelerates by 1 season | High — accelerates crisis |
| F-ARC-07 | ARC 4 | IP-C Thread operations during cascade push RS below 40 → ARC 2 re-activates simultaneously | Critical — combined crisis |
| F-ARC-08 | ARC 4 | IP-B multi-faction diplomacy produces 1/4 success rate (no faction backing); players perceived as committed to nobody; −1 faction relationship across board | High — wastes action economy |
| F-ARC-09 | ARC 5 | IP-D Hoarder compound probability: Church find-chance rises from 30% to 91% by Season 3 with zero benefit extracted | Critical — maximum bad outcome |
| F-ARC-10 | ARC 5 | IP-A publication at RS < 55 creates hardest combined state (ARC 2 + ARC 4 simultaneous) | Critical — requires all resources to survive |
| F-ARC-11 | ARC 5 | IP-E split party vs Church extraction team → near-certain document loss at halved combat pool | Critical — worst single-scene outcome |

**Findings requiring design review:**
- [GAP: Martyrdom effect from failed Church Debate — not defined in params. Assumed Church Stability +1 from public confrontation failure; needs explicit ruling]
- [GAP: RS response to accurate Thread document reading — stated in arc as RS +3; no canonical params entry for this. Flag for design doc]
- [EDITORIAL: ED-NNN — does Niflhel archive contain lineage data relevant to Torben? Requires user ruling before ARC 1/ARC 5 cross-arc interaction is canonical]

**Test ID:** SIM-ARC-01
**Mechanics:** Domain Actions, Debate system, RS decay/restoration, TC thresholds, Torben Loyalty Clock, Niflhel document mechanic (provisional), Coup trigger conditions
**Mode:** TTRPG primary; BG notes included per arc
**Temporal:** Multi-season, cross-arc
**Tracks:** RS, TC, Institutional Pressure, Torben Loyalty, Mandate, Stability, Influence, Military, Coherence
**Factions:** All eight
**NPCs:** Almud, Himlensendt, Torben, Elske, Edith Varn (referenced), Baralta (referenced)
**Archetypes:** IP-A through IP-F (all six irrational archetypes)
