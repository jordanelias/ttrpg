# Valoria — Emergent Campaign Arcs 46–55
*Batches 07–08 — Consolidated and Corrected*
*Critique applied: 2026-04-13 | Supersedes: arcs_46_50_batch07.md, arcs_51_55_batch08.md*

---

## Critique Summary (applied inline)
Findings applied per critique session 2026-04-13:
- F-02, F-08, F-09, F-11, F-14, F-20: Errors corrected
- F-01, F-18: Clarifications added
- F-06: [PROVISIONAL] flag propagated
- F-03/04/05/07/10/12/13/15/16/17/19/21: [UNVERIFIED] flags added inline

---

## Arc 46: The Quiet Seizure

**Mechanical seed:** Church Influence (CI) passive +1/season × Crown Suppress failure cost → Church Mandate grows faster than Suppress Ob reduces

**Systems in play:** CI passive advance (PP-402) · Failed Domain Action Stability cost (PP-403) · Territorial Seizure unique action (CI ≥ 60) · Crown Royal Decree unique action (separate mechanic — consecutive Ob escalation does not apply to Suppress)

---

### Narrative

For three seasons, the Crown has been trying to keep the Church in check through the procedural instrument of Suppress: a declaration each season that the Church's institutional momentum will not advance this year. The Crown keeps losing these rolls. The Church's Mandate is 5; Suppress Ob is calculated from that Mandate, then halved and rounded up (floor(5/2)+1 = 3; ÷2 round up = 2; min 1 — Ob 2). The Crown's pools are barely clearing Ob 2 in favourable seasons and failing in bad ones.

Every failed Suppress costs the Crown −1 Stability. Over three seasons this has reduced Crown Stability from 4 to 1. The Crown is now in a position where it cannot afford another Suppress failure — and yet the CI passive advance of +1/season has been running unchecked in the failed seasons, and the CI is now at 47. Three more seasons of unchecked advance brings it to 50. Another thirteen puts it in Seizure range.

The players are not watching a political crisis unfold. They are watching an institution slowly win by continuing to exist. The Church has done almost nothing — it did not Assert in the seasons it didn't need to. It is winning on momentum mechanics alone. When the Seizure threshold is crossed, the Church does not announce it.

**Causal flowchart:**

```
CI passive +1/season (PP-402, automatic at Accounting)
    │
    ▼
Crown declares Suppress (Ob 2 from Church Mandate 5 — note: Royal Decree has consecutive Ob
escalation; Suppress does not. These are separate mechanics with different Ob rules.)
    │
    ├─ Success → CI +0 that season (passive negated)
    │       └─ Repeat next season — Suppress Ob unchanged (no escalation rule)
    │
    └─ Failure (net ≤ 0) → CI +1 (passive applies) + Crown Stability −1 (PP-403)
            │
            ▼
        Crown Stability falls (4 → 3 → 2 → 1)
            │
            ├─ Stability 1: Crown risks Stability Check on next failure → Stability 0 → faction eliminated
            │
            └─ Crown stops Suppressing (cannot absorb another failure)
                    │
                    ▼
                CI advances unchecked: +1/season baseline
                    │
                    ├─ [Player intervention] Varfell or Hafenmark begin Suppressing
                    │       └─ Domain Action contested against Church Mandate — same Ob applies
                    │
                    └─ [No intervention] CI reaches 60
                            │
                            ▼
                        Church Territorial Seizure available (Mandate vs floor(owner Mandate/2)+1 per territory)
                            │
                            ├─ Seizure success → administrative control; Church Mandate unchanged
                            └─ Seizure failure → Church Mandate −1 per failed roll
```

**Emergent logic:** No player action caused the CI to approach 60. It advanced because Suppress failed repeatedly due to stat-line tension. The Church did not Assert aggressively — it won passively.

**Arc shape:** 4–6 seasons. Detectable at CI 40–47. Seizure threshold forces resolution window.

---

## Arc 47: Loyalty Split

**Mechanical seed:** Torben Loyalty track and Elske Loyalty track running independently → divergence creates Crown internal contradiction feeding Coup Counter

**Systems in play:** Torben Loyalty (0–7, start 3, PP-498) · Elske Loyalty (0–7, start 4) · Coup Counter (0–4, Löwenritter private) · Parliament Integrity (0–20, track — not a dice pool)

---

### Narrative

The players have been managing Crown relationships pragmatically. At some point they helped Torben — gave him information, backed his position in a proceeding, supported a resource claim. His loyalty to the Crown increased. Later, in a different context, they made an enemy of Elske — not deliberately, but because the situation required a choice and she was on the losing side of it. Her loyalty decreased.

The system does not announce consequences immediately. Torben's loyalty upward is producing one effect: stronger Crown Military representation when he acts. Elske's loyalty downward is feeding Coup Counter through the Löwenritter private track. The Coup Counter is invisible — the players cannot see it without Intel resources or specific in-game knowledge.

The split between Torben (high loyalty) and Elske (low loyalty) produces an internal contradiction. The Crown appears to have strong military support when Torben acts. But underneath, the Coup Counter is ticking. Löwenritter is patient. The arc is not a dramatic betrayal — it is a slow structural divergence between what the Crown appears to control and what it actually controls.

**Causal flowchart:**

```
[Player interaction → Torben Loyalty ↑ and Elske Loyalty ↓ from independent decisions]
    │
    ├─ Torben Loyalty ≥ 5 → Crown effective Military +1 when Torben leads action
    │       └─ Crown Domain Actions appear stronger
    │
    └─ Elske Loyalty ≤ 3 → Coup Counter advances (rate: [UNVERIFIED — confirm trigger
            condition and advancement rate against params_board_game.md §Coup Counter])
            │
            ▼
        Coup Counter advances toward threshold (≥ 4 = Löwenritter active coup condition)
            │
            ├─ [Players discover Coup Counter] — requires Intel resources or NPC disclosure
            │       └─ Decision: repair Elske loyalty vs accelerate
            │
            └─ [Coup Counter reaches 4]
                    │
                    ├─ Löwenritter executes coup condition
                    │   (Resolution procedure: Coup Counter ≥ 4 triggers coup;
                    │   Parliament Integrity is a track, not a dice pool — no PI roll occurs.
                    │   Resolution is track-threshold-based per params_board_game.md.)
                    │
                    └─ Torben's high loyalty becomes a liability — he is protecting an institution
                            the Löwenritter are actively undermining
```

**[UNVERIFIED: Elske Loyalty → Coup Counter advancement rate not confirmed in fetched params. Confirm against params_board_game.md §Coup Counter before treating as canonical.]**

**Emergent logic:** Two loyalty tracks made in separate sessions running in opposite directions and their separate downstream effects feeding into different clocks.

**Arc shape:** 3–8 seasons. Coup Counter is invisible until players invest in Intel.

---

## Arc 48: The Practitioner Economy

**Mechanical seed:** Thread Sensitivity advancement raises operation frequency → RS decay accelerates

**Systems in play:** RS baseline decay −1/year (PP-255) · Thread operations RS cost (params_threadwork.md) · Thread Sensitivity advancement (Overwhelming Leap → +1 Thread Sensitivity) · Coherence degradation · Intelligibility effects

---

### Narrative

The party has a Thread practitioner. Over five seasons they have advanced carefully — learned operations, tested Coherence limits, avoided the Locking and Dissolution operations that carry TN 8. The practitioner is now Thread Sensitivity 40, Thread Pool Score 4. Every Thread operation carries an RS cost — not catastrophic, but cumulative. The RS started at 60. It has been declining quietly across sessions.

No one has been calling attention to this. The practitioner is doing exactly what the system trains them to do. The arc is about what happens when optimising individual play degrades shared infrastructure.

**Causal flowchart:**

```
Thread Sensitivity ↑ (practitioner advancement)
    │
    ▼
Thread operations per session increase (higher Thread Sensitivity = more eligible operation types)
    │
    ├─ Operations succeed: RS cost absorbed within normal range
    └─ Operations fail (especially TN 8: Locking, Dissolution, Past-Oriented Pulling)
            │
            ▼
        RS degrades per failure cost (params_threadwork.md)
            │
            ▼
        RS baseline decay −1/year (PP-255) applies at Year-End Accounting
            │
            ▼
        RS declining: 60 → 55 → 50 → 45...
            │
            ├─ [UNVERIFIED: RS 50 and RS 40 intermediate threshold effects not confirmed
            │   in fetched params_threadwork.md. May be in threadwork_redesign_v25.md full doc.
            │   Flag effects at these thresholds as unconfirmed until verified.]
            │
            └─ RS 0: The Rupture — campaign loss (confirmed)
                    │
                    ├─ [Players discover RS trajectory] → restrict Thread operations; seek RS restoration sources
                    └─ [No intervention] → RS continues degrading
                            └─ Thread Sensitivity has become a shared liability
```

**[UNVERIFIED: Specific Coherence threshold for non-practitioner Intelligibility effects not confirmed in fetched params. Consistent with P-15 but threshold value requires design doc confirmation.]**

**Canon — P-07:** RS decay from Thread operations models substrate tension from practitioner activity. The ground does not respond or fight back. Compliant.

**Emergent logic:** TS advancement incentivising more operations + each operation carrying RS cost + baseline decay = three independent rules producing shared infrastructure degradation.

**Arc shape:** 6–10 sessions. Players may not notice until RS drops significantly. Recovery requires RS restoration sources or operational moratorium.

---

## Arc 49: The Mediator's Debt

**Mechanical seed:** Warden Cooperation (WC) track advancement + ethical framework alignment → Hafenmark becomes most viable CI suppressor through unintended leverage

**Systems in play:** CI passive advance (PP-402) · Suppress Domain Action · Warden Cooperation (WC 0–3) · Ethical framework Ob modifier (−1 Ob when aligned) · Hafenmark Stability gate (PP-571 [PROVISIONAL])

---

### Narrative

Hafenmark built Warden Cooperation (WC) for reasons that had nothing to do with Church politics — intelligence benefits and institutional Ob reduction. Over three seasons of patient play, they advanced WC to 2. The unintended consequence is that Hafenmark's ethical framework alignment with institutional mediation makes their Suppress action more reliable than Crown or Varfell attempting the same.

Both Crown and Church now need Hafenmark to keep acting. Hafenmark did not seek this leverage — they sought trade routes and quiet stability. Now every major faction is considering how to keep Hafenmark engaged in CI suppression without triggering the Hafenmark Stability gate.

**Causal flowchart:**

```
Hafenmark builds WC to Level 2 (for unrelated benefits)
    │
    ▼
Ethical framework alignment → Hafenmark Suppress Ob −1 vs other factions
[UNVERIFIED: WC Level 2 providing additional Ob reduction on Suppress not confirmed —
victory_architecture_v1.md returned empty. Ethical framework −1 Ob is confirmed.
WC-specific Ob reduction requires verification.]
    │
    ▼
Hafenmark becomes most reliable CI-suppressing faction
    │
    ├─ Crown defers Suppress to Hafenmark (saves Crown Stability)
    └─ Church calibrates Assert timing around Hafenmark Suppress schedule
            │
            ▼
        Both factions structurally dependent on Hafenmark remaining engaged
            │
            ▼
        Hafenmark Stability gate [PROVISIONAL — PP-571, flagged for Jordan review]:
        Parliamentary Sovereignty requires Stability ≥ 3
            │
            ├─ Any action reducing Hafenmark Stability → Crown and Church scramble to prevent it
            │
            └─ Hafenmark overextends → Stability drops to 2 → Parliamentary Sovereignty closes
                    │
                    └─ CI advance unchecked; both Crown and Church face crisis simultaneously
```

**Emergent logic:** Hafenmark built WC for internal reasons. The leverage was not designed — it emerged from WC Ob reduction interacting with ethical framework modifier (pending WC verification). The Stability gate exists for independent design reasons.

**Arc shape:** 4–7 seasons. Players may not recognise Hafenmark's leverage until another faction makes an unusually generous offer.

---

## Arc 50: The Counter That Runs Backward

**Mechanical seed:** Vaynard Thread Mastery (VTM) advances → VTM Level 3+ contributes CI +0.5/season (PP-563) → Varfell's independence-building mechanically accelerates Church dominance

**Systems in play:** VTM track (0–5, Varfell faction-specific) · CI passive advance (PP-402) · VTM-CI contribution rule (PP-563: +0.5/1/1.5 per season at VTM 3/4/5) · Varfell ethical framework · CI Seizure threshold (60)

---

### Narrative

Varfell has been investing in the Vaynard Thread Mastery (VTM) track because their long play is institutional independence — Thread resource access without Church oversight. VTM Level 3 is the first tier where Varfell gets access to Thread operations that don't require Church-licensed practitioners.

What accounting has been recording is that VTM Level 3 contributes +0.5 to CI advance per season. VTM Level 4 contributes +1. VTM Level 5 contributes +1.5. A Varfell at VTM 4 means CI is advancing +2/season instead of +1/season — twice as fast — while Varfell simultaneously opposes the Church politically.

Varfell is caught between their long-term strategic investment (VTM) and the medium-term threat that investment is accelerating (CI advance toward Seizure). Every Varfell VTM advancement roll is a Church Assert wearing different clothes.

**Causal flowchart:**

```
Varfell invests in VTM track (goal: institutional independence from Church)
    │
    ▼
VTM Level 3 reached
    │
    ├─ Varfell gains: Thread operation access without Church licensing
    └─ CI contribution begins: +0.5/season (PP-563) added at Accounting CI phase
            │
            ▼
        CI advancing faster than baseline: +1 (passive) + 0.5 (VTM 3) = +1.5/season
            │
            ├─ [Players unaware] → VTM advances to 4: CI now +2/season
            │       └─ Seizure threshold approaches in approximately 16 seasons (from CI 28) vs 32
            │
            └─ [Players aware] → decision: halt VTM at 3, accept strategic plateau
                    │
                    ├─ VTM halted: institutional independence goal frozen; CI stabilises at +1.5/season
                    │
                    ├─ VTM continued: CI accelerates; Varfell faces Seizure it helped create
                    │
                    └─ Suppress strategy: Varfell uses Domain Actions to counter CI they are generating
                            │
                            └─ Suppress Ob at Church Mandate 6:
                               floor(6/2)+1 = 4; ÷2 round up = 2; min 1 → Ob 2
                               (Not Ob 4 — the formula halving step applies)
```

**Cross-arc stack (corrected):** If Church Asserts + VTM 4 contributing simultaneously:
- Assert replaces passive: +2 total (not additive to +1 baseline)
- VTM 4: +1
- Total: +3/season
- Correct decomposition: Assert (+2, replacing passive) + VTM (+1) = +3. Not: passive +1 + VTM +1 + Assert +1 = +3. The total is the same; the mechanism is different — Assert does not stack on the passive, it replaces it.

**Emergent logic:** Varfell advancing VTM is the correct Varfell play. The arc emerges from PP-563 being written as a worldbuilding consequence of Thread activity concentrating institutional pressure — not as a check on Varfell. The two rules were written for completely different reasons.

**Arc shape:** 5–12 seasons. Critical inflection at VTM 3→4. Discovery of the CI contribution link requires Audit Domain Action or NPC disclosure.

---

## Arc 51: The Open Contact

**Mechanical seed:** Focus 1 practitioner advances Thread Sensitivity without ever gaining operations; Coherence decay from Experience alone; P-15 TS-gated resolution at Coherence 0

**Systems in play:** Leap eligibility (Thread Sensitivity 30+) · Contact Duration (Focus 1 = 0 op rounds, Experience only) · Thread Sensitivity +1 on Overwhelming Leap · Coherence decay · P-15 three-layer being-persistence · Intelligibility

---

### Narrative

There is a character in the party who can perceive Threads but has Focus 1. Contact Duration at Focus 1 is zero operation rounds — they Leap, they Experience, they return. Every session. They can see more than any practitioner in the group. They cannot do anything with it.

As Thread Sensitivity climbs, the gap between what they perceive and what they can act on widens. Coherence degrades — not from operations (they make none) but from the accumulated weight of Experience contacts. At high Thread Sensitivity with low Coherence, the character becomes legible to non-practitioners as wrong.

At Coherence 0, P-15 applies TS-gated branching: at low Thread Sensitivity, dissolution of self-configuration. At high Thread Sensitivity — which this character will have accumulated — forced self-maintenance via layer 3 (sustained deliberate threadwork). The character cannot simply dissolve. They are forced into sustained Thread work to maintain their own existence. But they have Focus 1. The layer 3 self-maintenance that saves them requires operations they cannot execute in a single contact window.

This is not NPC conversion. This is a character who has perceived too much and must now act in ways their build does not support — or fail at the level of their own persistence.

**Causal flowchart:**

```
Practitioner: Thread Sensitivity 30+ → Leap eligible
    │
    ▼
Focus 1 → Contact Duration 0 op rounds → Experience only
    │
    ├─ Overwhelming Leap → +1 Thread Sensitivity
    └─ Thread Sensitivity climbs: 38 → 45 → 52 → 60 → 70...
            │
            ├─ Thread Sensitivity 50: Leap Ob 2 → 1; more frequent Leap
            │
            └─ Coherence decay from Experience contacts [UNVERIFIED: whether Experience
                    carries Coherence cost is not confirmed in fetched params_threadwork.md.
                    If absent, this causal chain requires revision. Verify against
                    threadwork_redesign_v25.md before running.]
                    │
                    ▼
                Coherence declining: 10 → 8 → 6 → 4...
                    │
                    ├─ Coherence ≤ threshold [UNVERIFIED: specific threshold value]:
                    │   Intelligibility active — non-practitioners sense wrongness
                    │   [Whether Experience triggers P-01 co-movement requirements
                    │   also unverified — if yes, dimensional auto-effects compound costs]
                    │
                    └─ Coherence 0: P-15 TS-gated branching applies
                            │
                            ├─ Low Thread Sensitivity: dissolution of self-configuration
                            │
                            └─ High Thread Sensitivity (this character at Thread Sensitivity 70+):
                                    forced self-maintenance via layer 3 (sustained deliberate threadwork)
                                    — NOT flat NPC conversion
                                    │
                                    └─ Crisis: layer 3 self-maintenance requires operations;
                                            character has Focus 1 (0 op rounds).
                                            Either Focus advances (costs resources, competes with
                                            other priorities) or character faces layer 2 failure
                                            without the tools to address it via layer 3.
```

**Canon — P-15:** Arc models TS-gated Coherence 0 branching as required. High-TS characters do not dissolve — they face forced self-maintenance. This is the correct resolution branch for this arc's character profile.

**Emergent logic:** The character built toward Thread Sensitivity because Overwhelming results rewarded it. Focus was never prioritised because operations never seemed within reach. The arc emerges from the gap between two advancement tracks running at different rates — and resolves at a layer of being-persistence most players will not have considered.

**Arc shape:** 8–15 sessions. Thread Sensitivity advances on Overwhelming outcomes only — pace varies. Coherence decay is slow. The P-15 crisis builds quietly.

---

## Arc 52: Parliament as Weather

**Mechanical seed:** Parliament Integrity (PI) accumulates from aggregate of legitimate faction Domain Actions → no faction is attacking Parliament; all are doing normal things

**Systems in play:** Parliament Integrity (PI 0–20, start 7, auto-resolves at ≥ 20) · Coup Counter (Löwenritter private, 0–4) · Per-action PI contribution amounts [UNVERIFIED]

---

### Narrative

In Board Game mode, Parliament Integrity is not a clock any faction controls. It advances from events: contested Domain Actions in Parliamentary seats, failed Suppresses spilling into public administration, faction overextension into territory where Parliamentary oversight applies. Each faction that touches Parliament moves the needle — usually by 1, occasionally by 2. No faction is trying to collapse Parliament.

What the factions do not see is that the aggregate of their legitimate operations has been pushing PI since Season 2. By Season 6 it is at 14. Three more triggering events bring it to 17. At 20 it auto-resolves.

The Löwenritter Coup Counter has been at 2 since Season 4. It advances as a secondary trigger when PI ≥ 15 each season. It is at 3. The players are not watching Parliament collapse — they are watching factions do what factions do, while an invisible threshold approaches.

**Causal flowchart:**

```
PI starts at 7 (BG start — Parliament Integrity track, distinct from Public Instability)
    │
    ▼
Each season: faction Domain Actions touching Parliamentary institutions → PI +N per trigger
[UNVERIFIED: specific PI contribution values per action type not confirmed in fetched params.
The PI track and auto-resolution threshold at 20 are confirmed. Per-action amounts require
verification against full params_board_game.md or stage6_factions.md.]
    │
    ▼
        PI climbs toward 20
            │
            ├─ PI ≥ 15: Löwenritter Coup Counter advances +1/season (secondary trigger)
            │
            └─ PI ≥ 20: Auto-resolution — Parliament dissolved
                    │
                    ├─ Löwenritter coup condition active (if Coup Counter ≥ 4)
                    └─ Hafenmark loses Parliamentary Sovereignty action permanently
                            │
                            └─ [Players track PI] → deliberate coordination: all factions pause
                                    Parliamentary-touching actions (coordination problem — every faction
                                    must simultaneously stop doing planned actions)
```

**Note:** Factions do not lose Influence from skipping Domain Actions. No inactivity decay rule exists in params. Consequence of Guild inactivity is simply the absence of their Domain Action's effects that season — not a stat decrease.

**Emergent logic:** No faction caused this. PI advanced from the aggregate of normal play. The coordination problem to stop it is harder than any single political crisis.

**Arc shape:** 6–10 seasons in BG mode.

---

## Arc 53: The Wound Economy

**Mechanical seed:** Wound penalty −1D per wound propagates from TTRPG personal combat to faction Domain Action pool via faction leader's pool

**Systems in play:** Wound penalty −1D per wound, cumulative (PP-232) · Domain Action pool formula (NPC factions: relevant stat as d10 pool, TN 7) · Failed Domain Action Stability cost (PP-403)

---

### Narrative

Vaynard leads Varfell. He participates in TTRPG scenes and in Season 4 took two wounds in a physical confrontation. Recovery was not prioritised. At seasonal accounting, Vaynard's Domain Action pool for Varfell runs on his stat line — two wounds means −2D. The roll fails. Varfell takes −1 Stability.

The players understand wounds as a personal consequence. They do not always register that the same wound penalty propagates into the faction layer. The arc is about a TTRPG-layer event — a scene combat no one thought much about — creating a faction-layer consequence players trace back, if they trace it at all, to a moment three sessions ago when no one thought to find a healer.

**Causal flowchart:**

```
Vaynard takes 2 wounds in TTRPG scene combat (Season 4)
    │
    ├─ No recovery action taken — wounds persist into Accounting phase
    │
    └─ Seasonal Accounting: Varfell Domain Action (Vaynard leading)
            │
            ▼
        [UNVERIFIED: whether wound penalty propagates to faction Domain Action pool depends
        on whether leadership pool = personal pool or faction stat pool. If faction Domain
        Actions use the faction's Military stat directly (not the leader's personal pool),
        wound penalty does not propagate. Verify leadership pool rule against stage6_factions.md
        §faction leadership before treating this arc as mechanical canon.]
            │
        Assuming propagation confirmed:
            │
            ▼
        Pool = Military stat − 2D (wound penalty, PP-232)
            │
            └─ Increased failure probability → Domain Action fails → Stability −1 (PP-403)
                    │
                    ▼
                Season 5: wounds still present
                    │
                    └─ Crown or Hafenmark observe Varfell Domain Action outcomes degrading
                            → contest Varfell positions while pool is depressed
                                    │
                                    ├─ [Players recognise] → prioritise Vaynard wound recovery scene
                                    └─ [Wounds unaddressed] → Varfell Stability → Stability Check
```

**Emergent logic:** The wound penalty applies wherever the pool applies. TTRPG-to-faction propagation is mechanical, not narrated.

**Arc shape:** 2–4 seasons. Fast-developing. Crisis is recognising the connection before Stability collapses.

---

## Arc 54: What The Unaffiliated Know

**Mechanical seed:** Intelligibility from Coherence decay makes practitioners observable to non-sensitives; Varfell Intel network documents them before players are aware they're being profiled

**Systems in play:** Intelligibility (Coherence-threshold effects, P-15 compliant) · Varfell Intel Advancement Counter (0–3 → Intel +1) · P-08 epistemological barrier (metaphysical, not institutional)

---

### Narrative

The party's Thread practitioner has Coherence 5 after a difficult run of operations. Intelligibility is active — not dramatically, but present as an uncanny quality that observant people register. Varfell's Intel network is exactly the kind of distributed, observant apparatus that registers this. Their agents in three territories have independently reported the same travelling figure.

Varfell does not know what Thread Sensitivity is in a theoretical sense. They know this figure is different in a way their Intel apparatus can document. Niflhel already knew — Niflhel operates adjacent to Thread-adjacent phenomena. But Varfell knowing is new, and Varfell's knowledge is institutional. The practitioner is now in Varfell's files.

**Causal flowchart:**

```
Party Thread practitioner: Coherence 5 from accumulated operations
    │
    ▼
Intelligibility active at Coherence ≤ threshold [UNVERIFIED: specific threshold value;
consistent with P-15 three-layer being-persistence but not confirmed in fetched params]
    │
    ▼
Varfell Intel 3 → domain-wide observation network
    │
    └─ Varfell agents in multiple territories independently flag the same figure
            │
            ▼
        Varfell cross-references via Intel Domain Action [UNVERIFIED: Intel-based
        observation Domain Action not confirmed in fetched params. If this action
        does not exist in stage6, resolution procedure is unspecified.]
            │
            ├─ Success → Varfell partial profile: "anomalous figure, operative capacity unknown"
            │   (NOT a Thread Sensitivity estimate — P-08: epistemological barrier is metaphysical.
            │   Non-sensitives can observe effects and document anomalousness; they cannot render
            │   Thread Sensitivity as a precise quantity. Profile stays categorical, not numerical.)
            │
            └─ Overwhelming → Varfell confident in anomalous classification; begins asset/threat
                    assessment using observable behaviour, not Thread metrics
                    │
                    ▼
                Varfell decision: approach as asset? neutralise? observe?
                    │
                    ├─ Niflhel Influence 5 → Niflhel aware of Varfell's awareness
                    └─ [Party unaware] → Varfell can shape encounters using profile
                            while players negotiate on other topics
```

**Canon — P-08:** Profile is categorical ("anomalous") not quantitative. Varfell cannot render Thread Sensitivity as a number — the epistemological barrier is metaphysical. This reframing strengthens the arc: Varfell's knowledge is real but imprecise, making it more interesting as an information asymmetry.

**Canon — P-03:** Information asymmetry between sensitives and non-sensitives is the core mechanic. This arc plays precisely in that space.

**Emergent logic:** Intelligibility designed as a personal consequence of Coherence decay. Intel Advancement Counter designed to pace Varfell's information capacity. Arc emerges from their interaction — a cross-layer visibility neither rule was written to produce.

**Arc shape:** 5–7 seasons. Varfell has the file before players know.

---

## Arc 55: The Guild Favour Trap

**Mechanical seed:** Crown and Church Domain Actions in commercial territories depress Guild Favour; Guilds withdraw; Crown loses political buffer it did not know it had

**Systems in play:** Guild Favour (0–7, oscillating per territory) [UNVERIFIED: movement triggers] · Guilds Wealth stat 6 · Ethical framework Ob modifier · CI passive advance

---

### Narrative

The Guilds are a high-Wealth NPC bloc the players interact with as a buffer — they broker, smooth, and occasionally call in favours. Guild Favour in key trading territories has been sitting at 5 — comfortable, stable. The Crown's Royal Decree sequence in Season 5 landed in Feldmark. The Church's Assert in Season 4 had already affected Kronmark. Guild Favour is now at 3 in two key territories.

At Guild Favour 3 or below, the Guilds reduce their Domain Action pace — not out of punishment but out of withdrawal from economically uncertain territories, consistent with their framework. The Crown, which had been relying on Guild engagement as a political buffer, finds that buffer absent precisely when it needs it most.

**Causal flowchart:**

```
Crown Royal Decree in Feldmark (Season 5) + Church Assert effects on Kronmark (Season 4)
    │
    └─ Guild Favour in both territories −1 each
    [UNVERIFIED: specific Guild Favour movement triggers and amounts not confirmed in fetched
    params. The track exists; per-event contribution values require verification against
    stage6_factions.md §Guilds.]
            │
            ▼
Guild Favour: 5 → 3 in two territories
    │
    ├─ Guild Favour ≤ 3: Guilds reduce Domain Action pace [UNVERIFIED: specific threshold effect]
    │
    └─ Guilds skip Domain Action Season 6
            │
            ├─ Consequence: absence of Guild Domain Action effects that season
            │   (No Influence stat decay from inactivity — no such rule exists in params)
            │
            └─ Crown loses Guild engagement as political buffer
                    │
                    └─ CI advance less buffered by procedural Guild activity
                            │
                            └─ [Players restore Guild Favour] → Domain Action in each territory
                                    → Ob check: Crown framework vs mercantile efficiency framing
                                    [UNVERIFIED: "mercantile efficiency" as Guilds framework name]
                                    → if framework conflicts: +1 Ob
                                    → Hafenmark framework aligns: Ob unchanged
                                    → Hafenmark again becomes most efficient actor (cf. Arc 49)
```

**Emergent logic:** Crown and Church were aiming at each other. Neither was thinking about Guild Favour. Guild withdrawal is a mechanical consequence of their economic interference, not a political response.

**Arc shape:** 3–5 seasons. Fast-developing once Guild Favour drops below threshold.

---

## Cross-Arc Interaction Table (Consolidated)

| Arc pair | Interaction | Severity |
|----------|-------------|----------|
| 46 + 49 | Crown Suppress failures make Hafenmark the only viable suppressor — Crown weakness directly creates Hafenmark leverage | High |
| 46 + 50 | VTM contribution adds +0.5–1.5/season to CI advance Crown is already failing to suppress — two independent acceleration sources | Critical |
| 47 + 49 | Elske Loyalty degradation weakens Crown; Crown needs Hafenmark more; Hafenmark leverage amplified | Medium |
| 48 + 50 | RS decay from Thread operations + VTM advancing RS through operational co-movement — both degrade shared infrastructure via different channels | High |
| 49 + 50 | Varfell suppressing their own CI contribution competes with Hafenmark's Suppress slot — only one Suppress per season (params confirmed) | Medium |
| 46 + 47 + 49 | Crown Suppress failures + Elske loyalty degrading Crown internally + Hafenmark carrying suppression load = three simultaneous Crown weakening vectors | Critical |
| 51 + 54 | Thread Sensitivity advancement increases Intelligibility signal strength — more advancement without Focus resolution = more legible to Varfell Intel network | High |
| 52 + 53 | Vaynard wound-degraded Domain Actions may trigger Parliamentary-touching rolls that push PI — weak Varfell pool failing in a Parliamentary seat contributes PI | Medium |
| 52 + 55 | Guild Favour collapse reduces Guild Domain Action pace, removing procedural PI buffering; PI accelerates when Guilds are inactive | Medium |
| 53 + 55 | Varfell wound-weakened + Crown disrupting Guild Favour = two factions operating below normal capacity in the same accounting season | High |
| 51 + 48 | Focus 1 practitioner leaping frequently generates RS decay at same rate as operations-capable practitioner — without operational benefit | High |
| 54 + 49 | Varfell builds Intel to profile the practitioner while Hafenmark gains CI suppression leverage — both arcs produce knowledge asymmetries in same season window | Medium |

**Critical stack — Arcs 46 + 50 (corrected):**
If Assert fires + VTM 4 active: CI advances +3/season [Assert (+2, replacing passive) + VTM (+1)].
Under normal play (no Assert, no VTM): +1/season.
Acceleration factor: ×3. CI 28 → 60 in ~11 seasons instead of ~32.

**Three-arc stack — Arcs 52 + 53 + 55 (corrected):**
If Vaynard has wounds (Arc 53), Guild Favour at 3 (Arc 55), and PI at 14 (Arc 52):
One failed Varfell Domain Action in a Parliamentary territory contributes PI +N [UNVERIFIED: amount].
Guild inactivity removes procedural buffering that season.
PI advances faster from reduced faction engagement with Parliamentary process.
Löwenritter secondary trigger fires at PI ≥ 15. Coup Counter advances.

---

## [UNVERIFIED] Items Requiring Design Doc Confirmation

| ID | Item | Arc | Verify Against |
|----|------|-----|----------------|
| U-01 | Elske Loyalty → Coup Counter advancement rate | 47 | params_board_game.md §Coup Counter |
| U-02 | RS threshold effects at 50 and 40 | 48 | threadwork_redesign_v25.md |
| U-03 | Coherence threshold for non-practitioner Intelligibility | 48, 54 | threadwork_redesign_v25.md |
| U-04 | WC Level 2 Ob reduction on Suppress | 49 | victory_architecture_v1.md §6 (returned empty — source file may need re-fetch) |
| U-05 | Coherence decay from Experience (no operation) | 51 | threadwork_redesign_v25.md |
| U-06 | Whether Experience triggers P-01 co-movement | 51 | canon/00_philosophical_foundations.md + threadwork_redesign_v25.md |
| U-07 | Per-action PI contribution values | 52 | params_board_game.md §PI (full fetch) |
| U-08 | Wound penalty → faction Domain Action pool propagation via leader pool | 53 | stage6_factions.md §faction leadership |
| U-09 | Intel-based observation Domain Action existence | 54 | stage6_factions.md §Varfell §Intel |
| U-10 | Guild Favour movement triggers and per-event amounts | 55 | stage6_factions.md §Guilds |
| U-11 | "Mercantile efficiency" as Guilds ethical framework name | 55 | stage6_factions.md §Guilds ethical framework |

**[PROVISIONAL] Items (PP-571):**
Arc 49 cites PP-571 (Hafenmark Stability ≥ 3 gate on Parliamentary Sovereignty). This patch is marked [PROVISIONAL] in session_log_current.md and flagged for Jordan review. Arc 49's resolution depends on this mechanic. If PP-571 is revised, Arc 49's flowchart requires update.

---

*Supersedes: gm_ref/arcs_46_50_batch07.md, gm_ref/arcs_51_55_batch08.md*
*These files should be retained for history but this document is canonical for arcs 46–55.*

[EDITORIAL: ED-782 — Theocracy Counter (TC) → Church Influence (CI) rename per vocabulary audit]
