# Valoria — Emergent Campaign Arcs 46–55
*Batches 07–08 — Consolidated, Critiqued, and Fully Resolved*
*Critique applied: 2026-04-13 | Resolution applied: 2026-04-13*
*Supersedes: arcs_46_50_batch07.md, arcs_51_55_batch08.md, arcs_46_55_consolidated.md (prior)*

> **Glossary note:** **CI** = Church Influence (Church institutional advancement clock, 0–100; renamed from Church Influence per ED-782). Piety Track (CT) is always written in full. (ED-756)

---

## Resolution Log

All [UNVERIFIED] items resolved against fetched sources. Findings:

| ID | Resolution | Arc Impact |
|----|-----------|-----------|
| U-01 | Elske Loyalty has no Coup Counter link in stage6. Triggers are: CI ≥ 40 unopposed, Torben loyalty ≤ 2–3, Crown loses 2+ territories without military response. Coup Counter ceiling = 3 (stage6), fires at 3. | Arc 47 rebuilt around correct triggers. |
| U-02 | MS thresholds confirmed: 79–60 Strained, 59–40 Fragile, 39–20 Fractured, 19–1 Critical. No thresholds at 50 or 40. Starting MS 60 = already in Strained. First effect fires at MS 59. | Arc 48 threshold references corrected. |
| U-03 | Coherence 7–5 (Dissonant): Close Knots sense wrongness only. Broader non-practitioner perception is via Thread Sensitivity perception table (TS 10–29 = vague unease), not Coherence thresholds. | Arcs 48/54 reframed: Intelligibility is Thread Sensitivity-gated observation, not Coherence-threshold broadcast. |
| U-04 | WC effects: +1D Thread ops (WC ≥ 1), MS decay halved (WC ≥ 2), MS +2/season (WC 3). No Ob reduction on any Domain Action. | Arc 49 mechanical seed corrected: only ethical framework −1 Ob is real. WC contribution to Suppress removed. |
| U-05 | Experience at Focus 1 carries zero Coherence cost per §3.2. No operation = no Coherence reduction trigger. | Arc 51 causal chain rebuilt: Focus 1 characters do not Coherence-decay from Experience. New mechanism: Thread Sensitivity growth without Focus creates perceptual burden unaddressed by any recovery mechanic. |
| U-06 | P-01 co-movement requires an operation. Experience produces no operation. P-01 does not apply to Focus 1 Experience-only contact. | Arc 51 confirmed: no co-movement fires on Experience alone. |
| U-07 | PI per-action contribution values not specified in any fetched source. Stage6 PI is 0–10 (TTRPG). Params BG PI is 0–20 start 7. Arc 52 is BG mode — uses params_board_game.md ceiling/auto-resolve. Per-action amounts remain design-layer gap. | Arc 52 flags this gap inline. Causal logic retained; specific amounts noted as requiring design decision. |
| U-08 | Stage6 confirmed: Domain Action pool = character's personal roll; faction leadership adds faction stat as bonus dice. Wound penalty reduces personal pool → confirmed propagation to Domain Action. | Arc 53 confirmed mechanically sound. |
| U-09 | No named "Read Intel" Domain Action. Varfell's Private Collection (Intel vs Ob 2, reveals hidden faction attribute) is closest. Standard Domain Action rules allow Intel-based observation as a general action. | Arc 54 reframed: uses Private Collection or standard Intel Domain Action, not a hypothesised named action. |
| U-10 | Guild Favour moves only on Guild Economic Leverage Failure (−1 in that territory). Crown/Church Domain Actions do not trigger Guild Favour changes. | Arc 55 rebuilt: causal chain replaced with confirmed mechanic. |
| U-11 | No named Guild ethical framework in fetched sources. "Mercantile efficiency" was invented. | Arc 55: framework reference removed. Ob modifier rules apply per standard table (aligned/contradicting). |

---

## Arc 46: The Quiet Seizure *(confirmed)*

**Mechanical seed:** CI passive +1/season × Crown Suppress failure Stability cost → Church wins by institutional momentum alone

**Systems:** CI passive advance (PP-402) · Failed Domain Action Stability cost (PP-403) · Territorial Seizure (CI ≥ 60) · Suppress (no consecutive Ob escalation — distinct from Royal Decree)

---

### Narrative

For three seasons, the Crown has been Suppressing — a procedural declaration each season that the Church's institutional momentum will not advance this year. The Church's Mandate is 5. Suppress Ob = floor(Church Mandate / 2) + 1, then ÷ 2 round up, min 1 = Ob 2. The Crown keeps failing. Every failed Suppress costs −1 Stability (PP-403). Crown Stability: 4 → 3 → 2 → 1. The Crown cannot afford another failure.

Meanwhile CI has advanced unchecked in the failed seasons. It is at 47. The Church has not Asserted. It has done nothing except exist. It is winning on passive momentum alone.

**Flowchart:**

```
CI passive +1/season (PP-402, automatic)
    │
    ▼
Crown Suppress: Ob 2 (Church Mandate 5). Note: Royal Decree has consecutive Ob escalation;
Suppress does not. Separate mechanics.
    │
    ├─ Success → CI +0 (passive negated). No escalation next season.
    └─ Failure → CI +1 + Crown Stability −1 (PP-403)
            │
            ▼
        Crown Stability: 4 → 3 → 2 → 1
            │
            ├─ Stability 1: next failure → Stability 0 → Stability Check → possible elimination
            └─ Crown stops Suppressing
                    │
                    ▼
                CI unchecked: +1/season
                    │
                    ├─ [Intervention] Varfell or Hafenmark Suppress
                    └─ [None] CI → 60 → Church Territorial Seizure
                            (Mandate vs floor(owner Mandate/2)+1 per territory)
```

**Emergent logic:** CI advanced because Suppress failed due to stat-line tension. Church did nothing aggressive. Passive rule + Stability cost produced a crisis no one designed.

**Arc shape:** 4–6 seasons. Detectable at CI 40–47.

---

## Arc 47: The Counter She Keeps *(rebuilt — U-01)*

**Mechanical seed:** Three independent Coup Counter triggers running simultaneously → Grandmaster Ehrenwall marks failures she does not revise; the counter never decrements

**Systems:** Coup Counter (0–3, private, fires at 3 — stage6 §8.9) · CI passive advance (PP-402) · Torben Loyalty (0–7, start 7 per PP-599) · Crown territory loss rule (2+ territories in one season without military response)

---

### Narrative

The Löwenritter Coup Counter is private. Grandmaster Ehrenwall keeps it. It has three triggers: CI reaching 40 while the Crown took no action to reduce it; Torben's loyalty dropping to 2 or lower; the Crown losing two or more territories in one season without a military Domain Action response. Each fires once and adds 1 to the counter. The counter never decrements.

The players will rarely see all three threats simultaneously. They are more likely to see one, manage it, and not realise the other two are also running. The arc generates when a campaign reaches a point where two triggers have already fired — perhaps CI crossed 40 in Season 3 before the players were tracking it, and Torben's loyalty has been slowly degrading through Altonian diplomatic pressure — and only the third trigger remains. The players do not know the counter is at 2. When the Crown loses a territory without mounting a military response, the counter hits 3 and the coup fires at the next accounting.

The Löwenritter's loyalty is to the Crown as institution. This is not betrayal. This is institutional quality control.

**Flowchart:**

```
Coup Counter starts at 0. Ceiling: 3. Fires at 3. Counter never decrements.
Three independent triggers, any order:

Trigger A: CI reaches 40 while Crown took no Suppress/Assert-counteraction that season
    │ → Coup Counter +1

Trigger B: Torben Loyalty ≤ 2 (Altonian alignment — loyalty track starts 7 per PP-599)
    │ → Coup Counter +1
    │ Note: Torben Loyalty ≥ 5 previously gave Crown effective Military bonus (confirmed).
    │ Elske Loyalty is a separate track with no confirmed Coup Counter link.

Trigger C: Crown loses 2+ territories in one season without a military response Domain Action
    │ → Coup Counter +1
    │
    ▼
Coup Counter = 3 → coup fires at next seasonal accounting
    │
    ├─ Löwenritter impose Martial Law on all Crown-held territories
    │   (All non-Military Domain Actions require secondary Military check Ob 2 to proceed)
    │
    └─ [Players aware] → must address open triggers before all three close
            → CI reduction: Suppress or military pressure on Church
            → Torben Loyalty repair: Influence Domain Actions
            → Territory: Military Domain Action response to any loss
```

**Emergent logic:** Three triggers written for independent reasons — CI clock, NPC loyalty track, military accountability — converge silently. No player decision caused two triggers to fire before the players knew to watch the counter.

**Arc shape:** 4–10 seasons. Counter invisible without NPC disclosure. If players learn the counter is at 2, the remaining trigger becomes the most important roll in the campaign.

---

## Arc 48: The Practitioner Economy *(MS thresholds corrected — U-02, U-03)*

**Mechanical seed:** Thread Sensitivity advancement raises operation frequency → MS decay crosses Fragile threshold (59) → world-level Ob penalties increase operation failure rate → more failures → more MS cost (compounding)

**Systems:** MS baseline decay −1/year (PP-255) · Thread operations MS cost (§5.2) · MS thresholds: Strained (79–60), Fragile (59–40), Fractured (39–20), Critical (19–1) · Co-movement (P-01)

---

### Narrative

The campaign starts at MS 60 — already in the Strained band. This is not unusual; the Valorian peninsula's substrate has been strained since the Einhir Catastrophe. The practitioner is careful. They operate at Object and Personal scale most of the time. But necessity and ambition push them toward Relational+ scale operations, and those carry MS costs on Partial and Failure. MS: 60 → 57 → 54 → 51 → 48.

At MS 59, the world crosses into Fragile. Shifting Objects form spontaneously in high-traffic Thread territories. Thread operations take +1 Ob in affected territories. That +1 Ob increases the failure rate of every Thread operation. More failures → more MS costs on the degree table. The degradation accelerates. The practitioner is not doing anything wrong — they are responding to exactly the incentives the system provides — and the world is getting worse at a rate that is now faster than anyone planned for.

Non-practitioners notice wrongness — but not from Coherence thresholds. They notice because Thread operations at TS 10–29 produce "vague unease; cannot locate source." As operations increase and Shifting Objects appear, the ambient wrongness in the world is perceivable to anyone sensitive enough. The practitioner is not radiating personal wrongness. The world is.

**Flowchart:**

```
MS starts at 60 (Strained band — effects: "occasional wrongness near old operation sites")
    │
    ▼
Thread operations accumulate MS costs:
    − Weaving/Pulling partial or failure: −1 to −2 per degree table
    − Past-Oriented Pulling: −3 minimum
    − MS baseline decay: −1/year (PP-255, Year-End Accounting)
    │
    ▼
MS crosses 59 → Fragile band
    │
    ├─ Shifting Objects form spontaneously (1 random per season at Accounting)
    ├─ Thread operations +1 Ob in affected territories
    │       └─ Higher Ob → higher failure rate → more MS costs → compounding
    └─ Non-practitioners with TS 10–29 sense "vague unease" near old operation sites
            (Thread Sensitivity perception table — not Coherence-broadcast)
            │
            ▼
        MS crosses 39 → Fractured band
            │
            ├─ Gaps may open spontaneously (1d10/season; 1–2 = Gap in lowest-Prosperity territory)
            ├─ Monstrous Incursion risk in Gap territories
            └─ Non-practitioners experience rendering failures (inconsistent memories, déjà vu)
                    │
                    └─ [Intervention needed] Mending, restrict operations, MS restoration sources
                       (Each successful Mending: +1 to +2 MS)
```

**Emergent logic:** TS advancement incentivises more operations. More operations produce MS costs. MS degradation increases Ob, which increases failure rate, which produces more MS costs. Three independent rules produce compounding feedback — no single decision caused this.

**Arc shape:** 6–10 sessions. MS 60 → 59 crossing may happen within 2–3 seasons. Fragile → Fractured requires sustained failure. Players may not notice threshold effects until Shifting Objects appear.

---

## Arc 49: The Mediator's Debt *(WC Ob reduction removed — U-04)*

**Mechanical seed:** Hafenmark ethical framework alignment gives −1 Ob on Suppress → makes Hafenmark the most reliable CI suppressor → both Crown and Church structurally need Hafenmark stable → leverage Hafenmark did not seek

**Systems:** CI passive advance (PP-402) · Suppress Domain Action · Ethical framework modifier (−1 Ob aligned, confirmed) · Hafenmark Stability gate (PP-571 [PROVISIONAL]) · WC effects (confirmed: +1D Thread ops, MS decay halved — no Domain Action Ob reduction)

---

### Narrative

The Crown has been failing Suppress rolls. Hafenmark begins Suppressing — not for the Crown's benefit, but because CI advance threatens the Parliamentary legitimacy that Hafenmark's entire position depends on. Their institutional framework is aligned with procedural suppression of theocratic overreach. Suppress costs them −1 Ob per the ethical framework modifier. Their rolls succeed more reliably than the Crown's.

Note: Warden Cooperation adds +1D to Thread operations and halves MS decay at WC ≥ 2. It does not reduce Domain Action Ob. Hafenmark's advantage on Suppress comes purely from ethical framework alignment. This is a narrower advantage than previously modelled — but it is real and confirmed.

Both Crown and Church recognise that Hafenmark is now doing the work. Crown cannot afford to Suppress (Stability 1). Church has no incentive to stop CI advance. Only Hafenmark is Suppressing, and only Hafenmark has the framework alignment to do it consistently.

**Flowchart:**

```
Crown fails Suppress → Stability 1 → stops Suppressing
    │
    ▼
Hafenmark begins Suppressing (independently motivated: CI threatens Parliamentary legitimacy)
    │
    ▼
Ethical framework alignment: Hafenmark Suppress Ob −1 (framework modifier, confirmed)
    Ob = 2 (Church Mandate 5) − 1 (framework) = Ob 1 (min 1 applies — stays Ob 1)
    vs Crown: Ob 2 with no framework discount
    │
    ▼
Hafenmark Suppress succeeds more reliably than Crown's did
    │
    ├─ Crown defers Suppress to Hafenmark (saves own Stability)
    └─ Church adjusts Assert timing around Hafenmark Suppress schedule
            │
            ▼
        Both factions depend on Hafenmark remaining engaged
            │
            ▼
        Hafenmark Stability gate [PROVISIONAL — PP-571, for Jordan review]:
        Parliamentary Sovereignty requires Stability ≥ 3
            │
            ├─ Any action reducing Hafenmark Stability → Crown and Church both oppose it
            └─ Hafenmark Stability drops to 2 → Parliamentary Sovereignty closes
                    → CI unchecked; both Crown and Church face crisis simultaneously
```

**Note on Suppress slot:** Suppress may be declared once per season by one faction. Varfell suppressing their own CI contribution (Arc 50) competes for this slot.

**Emergent logic:** Hafenmark Suppressed for its own reasons. The ethical framework modifier made their rolls better. The leverage was not designed.

**Arc shape:** 4–7 seasons. Detectable when Crown makes an uncharacteristically generous offer to keep Hafenmark stable.

---

## Arc 50: The Counter That Runs Backward *(Ob formula and Assert decomposition corrected)*

**Mechanical seed:** VTM Level 3+ contributes CI +0.5/season (PP-563) → Varfell's independence-building mechanically accelerates Church dominance

**Systems:** VTM (0–5, Varfell) · CI passive advance (PP-402) · PP-563 (VTM CI contribution: +0.5/1/1.5 at VTM 3/4/5) · Suppress Ob formula · Assert replaces passive (not additive)

---

### Narrative

Varfell advancing VTM is the correct Varfell play. At VTM 3, they gain access to Thread operations without Church licensing. This is their path to institutional independence. What accounting has been quietly noting is that VTM 3 contributes +0.5 to CI advance per season. VTM 4: +1. VTM 5: +1.5.

A Varfell at VTM 4 means CI advances at +2/season instead of +1/season. Every Varfell VTM advancement roll is mechanically equivalent to a partial Church Assert.

**Flowchart:**

```
Varfell invests in VTM (goal: Thread independence from Church)
    │
    ▼
VTM 3: Thread access without Church licensing + CI contribution +0.5/season (PP-563)
    │
    ▼
CI: +1 (passive) + 0.5 (VTM 3) = +1.5/season
    │
    ├─ [Unaware] VTM → 4: CI +1 (passive) + 1 (VTM 4) = +2/season
    │       → CI 28 → 60 in ~16 seasons vs ~32 at baseline
    │
    └─ [Aware] Decision: halt VTM at 3, accept independence plateau
            │
            ├─ VTM halted: Varfell independence goal frozen
            ├─ VTM continued: CI accelerates; Varfell faces Seizure it helped create
            └─ Suppress: Varfell uses Domain Actions to counter own CI contribution
                    Ob at Church Mandate 6: floor(6/2)+1=4; ÷2 round up=2; min 1 → Ob 2
                    (Ob 2, not Ob 4)

Stack correction — if Assert fires + VTM 4 active:
    Assert replaces passive: +2 total (NOT additive)
    VTM 4: +1
    Total: +3/season
    Breakdown: Assert (+2, replacing +1 passive) + VTM (+1) = +3
    Not: passive +1 + VTM +1 + Assert +1 = +3 (wrong decomposition, same result)
    CI 28 → 60 under this triple condition: ~11 seasons
```

**Emergent logic:** PP-563 was written as a worldbuilding consequence of Thread activity concentrating institutional pressure — not as a check on Varfell. The interaction with CI passive advance was not designed.

**Arc shape:** 5–12 seasons. Discovery requires Audit Domain Action or NPC disclosure.

---

## Arc 51: The Weight of Sight *(rebuilt — U-05, U-06)*

**Mechanical seed:** Focus 1 practitioner advances Thread Sensitivity without Coherence cost from Experience → Thread Sensitivity grows uncapped by recovery mechanics → at high Thread Sensitivity, the perceptual gap between what they see and what they can do is not a Coherence problem — it is a practitioner problem the system provides no clean resolution for

**Systems:** Leap eligibility (Thread Sensitivity 30+) · Contact Duration (Focus 1 = 0 op rounds, Experience only, confirmed) · Thread Sensitivity +1 on Overwhelming Leap · Coherence §3.2 (Experience at Focus 1: zero Coherence cost, confirmed) · P-15 (Coherence 0 TS-gated branching) · Thread Sensitivity perception table

---

### Narrative

Experience at Focus 1 carries no Coherence cost. This is confirmed. The practitioner leaps, experiences contact, returns. Every session. Thread Sensitivity advances on Overwhelming Leap outcomes. Over twelve sessions they are at Thread Sensitivity 58. Thread Sensitivity Ob dropped from 2 to 1 at Thread Sensitivity 50. They leap nearly automatically now.

Their Coherence is 10. They have not degraded at all. They are not fracturing. They are perceiving the world at a resolution that no other practitioner at this campaign stage can access — Thread Sensitivity 58 means they identify operation types and approximate targets; Thread Sensitivity 70 will let them perceive the full configuration being worked. And they cannot do anything with it.

The arc is not about degradation. It is about the increasing gap between perception and agency, and what happens when a practitioner at Thread Sensitivity 58 needs to act. The system's pressure to scale up — to perform Relational+ operations — lands on a practitioner with Focus 1 and zero operation rounds. They must either advance Focus (costs specific Histories, resource-intensive, competes with other advancement priorities) or remain permanently in the role of observer at a resolution that demands action.

The P-15 crisis eventually arrives not from Coherence decay but from a specific forced event: a situation requiring the practitioner to act at Relational+ scale where no other practitioner can. Focus 1 means they cannot. The arc is about what happens at that moment.

**Flowchart:**

```
Thread Sensitivity 30+ → Leap eligible
    │
    ▼
Focus 1 → 0 op rounds → Experience only (confirmed: no Coherence cost per §3.2)
    │
    ├─ Overwhelming Leap → +1 Thread Sensitivity (standard rule)
    └─ Thread Sensitivity climbs: 38 → 45 → 52 → 58 → 65+
            │
            ├─ Thread Sensitivity 50: Leap Ob 2→1; leaping nearly automatic
            ├─ Thread Sensitivity 50–69: "identifies operation type and approximate target"
            └─ Thread Sensitivity 70+: "perceives full configuration being worked"
                    │
                    ▼
                Perceptual gap widens: sees more, can still do nothing
                    │
                    ├─ [No forcing event] → practitioner accumulates perception; no crisis
                    │       (Experience costs nothing; Thread Sensitivity growth is low-risk)
                    │
                    └─ [Forcing event: Relational+ operation required, only practitioner eligible]
                            │
                            ├─ Focus 1 → cannot perform the operation
                            ├─ If Coherence 0 reached via other route (not Experience):
                            │   P-15 TS-gated branching applies
                            │   High-TS branch: forced layer 3 self-maintenance, not dissolution
                            └─ Real crisis: campaign pressure requires action from someone
                                    who can see everything and do nothing
                                    → Focus advancement is the resolution gate
                                    → Focus 2 minimum for functional practice (confirmed)
```

**Emergent logic:** The system rewards Thread Sensitivity advancement with Overwhelming Leaps and Ob reductions. Experience at Focus 1 costs nothing. A practitioner who never scales up — who only Leaps and Experiences — advances Thread Sensitivity indefinitely with no Coherence cost. The arc emerges from the gap between the two advancement tracks having no internal pressure to close. The system does not force Focus advancement. Only campaign events can.

**Arc shape:** 10–20 sessions. No internal pressure creates the crisis — it must be created by external forcing events.

---

## Arc 52: Parliament as Weather *(PI contribution amounts flagged as design gap — U-07)*

**Mechanical seed:** PI (BG track, 0–20, start 7) accumulates from aggregate of legitimate faction actions → auto-resolves at ≥ 20 → no faction is attacking Parliament; all are pursuing normal goals

**Systems:** Parliament Integrity (BG mode: 0–20, start 7, auto-resolves ≥ 20 = Crown elimination, params_board_game.md) · Coup Counter (Löwenritter, fires at 3 per stage6)

---

### Narrative

Parliament Integrity in Board Game mode is not a clock any faction controls. It advances from the aggregate of faction activity in Parliamentary-adjacent contexts. No faction targets Parliament. The Crown wants it functional. Hafenmark's position depends on Parliamentary legitimacy. Varfell uses Parliamentary procedure as cover.

What the board has been recording is that each faction's normal operations have been nudging PI upward since Season 2. By Season 6 it is at 14. The auto-resolve threshold is 20. The Löwenritter secondary trigger (confirmed in stage6: CI ≥ 40 unopposed fires Coup Counter +1, not a PI trigger directly) is separate — but if PI auto-resolves at 20, Crown elimination fires, which changes the entire faction landscape.

**Design gap acknowledged:** Per-action PI contribution values are not specified in any fetched source. The mechanic's existence and auto-resolve threshold are confirmed (params_board_game.md). The specific amounts per action type (Royal Decree in Parliamentary seat, Hafenmark Parliamentary Sovereignty, Church Excommunication of Parliamentary figure, etc.) are a design-layer gap requiring a future table. The arc's logic holds; the per-action amounts are `[DESIGN GAP: PI per-action contribution table — needs specification in params_board_game.md or stage6]`.

**Flowchart:**

```
PI starts 7 (BG). Auto-resolves at ≥ 20 (Crown elimination).

Each season: faction Domain Actions touching Parliamentary institutions → PI +N
[DESIGN GAP: per-action amounts not specified — design decision required]
    │
    ▼
PI climbs: 7 → ~14 by Season 6 (at plausible rate of +1–2/season)
    │
    ├─ PI ≥ 20: auto-resolution → Crown elimination + Löwenritter coup condition if Coup Counter = 3
    │
    └─ [Players track PI] → coordinate all factions to pause Parliamentary-touching actions
            (Coordination problem: each faction must forgo planned actions simultaneously)
            Note: skipping Domain Actions has no stat decay consequence — no inactivity decay rule exists.
            Consequence is simply absence of that action's effects for the season.
```

**Emergent logic:** No faction intended to collapse Parliament. PI advanced from aggregate of legitimate normal play. The coordination problem to stop it is harder than any single political crisis.

**Arc shape:** 6–10 BG seasons. Threshold visible on shared board; easy to lose track of under session pressure.

---

## Arc 53: The Wound Economy *(confirmed — U-08)*

**Mechanical seed:** Wound penalty (+0.15 Ob per wound, cumulative) applies to personal roll → faction leader's personal roll drives Domain Action → wound propagates from TTRPG personal combat to faction accounting layer [SUPERSEDED FRAMING, ED-PC-0005/ED-PC-0006, 2026-07-08: the original −1D-per-wound pool cut (PP-716, now struck) is replaced by a fractional Ob added to the roll, never a pool cut — value reuses ED-1041's combat "attacking" magnitude, the active-roller case]

**Systems:** Wound penalty +0.15 Ob per wound, cumulative (ED-PC-0005/ED-PC-0006; supersedes PP-232/PP-716's −1D) · Domain Action pool (stage6 confirmed: personal roll + faction stat bonus dice if holding leadership) · Failed Domain Action Stability cost (PP-403)

---

### Narrative

Vaynard leads Varfell. His personal roll — the base pool for his Domain Actions — carries his wound penalty. Stage6 confirms: the rolling character's personal action drives the Domain Action; holding leadership adds faction stat as bonus dice. Two wounds adds +0.30 Ob to his personal roll. The bonus dice from faction stat are unaffected, but the base roll faces a harder target.

The players understand wounds as a personal combat consequence. They do not always register that the same penalty propagates into the faction layer at accounting. A TTRPG-layer event — a combat no one thought much about — becomes a faction-layer consequence players trace back, if they trace it at all, to a session where no one thought to find a healer.

**Flowchart:**

```
Vaynard takes 2 wounds in TTRPG scene combat (Season 4)
    │
    ├─ No recovery action taken
    └─ Seasonal Accounting: Varfell Domain Action (Vaynard leading)
            │
            ▼
        Pool = personal roll, Ob +0.30 (wound penalty, ED-PC-0005/ED-PC-0006; supersedes PP-232's −2D framing) + Varfell Military (bonus dice)
        The harder target raises failure probability.
            │
            └─ Domain Action fails → Stability −1 (PP-403)
                    │
                    ▼
                Season 5: wounds persist
                    │
                    ├─ Crown/Hafenmark observe Varfell failure rate → contest positions
                    └─ Stability: 4 → 3 → 2 → Stability Check risk
                            │
                            ├─ [Players recognise] → Vaynard wound recovery scene
                            └─ [Unaddressed] → Varfell existential risk from a two-wound combat
```

**Emergent logic:** The wound penalty applies wherever the pool applies. TTRPG-to-faction propagation is mechanical, not narrated. Mechanically confirmed.

**Arc shape:** 2–4 seasons. Fast-developing. Recognition is the crisis, not resolution.

---

## Arc 54: What The Unaffiliated Know *(reframed — U-03, U-09)*

**Mechanical seed:** Thread Sensitivity perception table (TS 10–29: vague unease) × Varfell Intel network × Private Collection action (reveal hidden faction attribute) → Varfell profiles the practitioner before players know they're being profiled

**Systems:** Thread Sensitivity perception table (§2.3) · Varfell Private Collection unique action (Intel vs Ob 2 — confirmed) · P-08 (epistemological barrier: metaphysical, not institutional) · P-03 (information asymmetry as core mechanic)

---

### Narrative

The party's Thread practitioner has been operating. Operations are visible to Thread Sensitivity observers — at TS 10–29, observers sense vague unease and cannot locate the source. Varfell's network is distributed and observant. Their agents across several territories independently report the same travelling figure produces an uncanny ambient quality. Individually these reports mean nothing. Cross-referenced, they produce a pattern.

Vaynard's Private Collection action (Intel vs Ob 2) has one option: "reveal one hidden faction attribute." Vaynard can deploy this — not to measure the practitioner's Thread Sensitivity numerically, but to confirm that the practitioner is operating at a level that makes the Private Collection's Thread-signature detection relevant. On Success or Overwhelming, Varfell's profile of the practitioner advances: not Thread Sensitivity numbers (P-08 — epistemological barrier is metaphysical; non-sensitives cannot render Thread Sensitivity as a quantity) but categorical: "this figure operates at a scale that our artefacts can detect."

The profile is real. It is precise enough to act on. It is not what the practitioner would recognise as knowledge about themselves.

**Flowchart:**

```
Practitioner operates in multiple territories across multiple sessions
    │
    ▼
Thread operations visible per perception table:
    TS 0–9: nothing
    TS 10–29: "vague unease; cannot locate source"
    TS 30–49: "senses operation in scene; general direction identifiable"
    │
    ▼
Varfell agents (Intel network, distributed) independently report ambient wrongness
    │
    ▼
Vaynard deploys Private Collection: Intel vs Ob 2
    ├─ Success: "reveal one hidden faction attribute"
    │   → Varfell confirms: practitioner operating at Thread-signature-detectable scale
    │   → Profile: categorical ("anomalous; detectable by Thread artefacts")
    │   → NOT a Thread Sensitivity number (P-08: epistemological barrier is metaphysical)
    └─ Failure: artefact's Thread signature detected → Church Intel +1D vs Varfell for 1 season
            │
            ▼
        Varfell has a profile. Players do not know they have it.
            │
            ├─ Niflhel (Influence 5) aware of Varfell's awareness → may intercept
            └─ [Party unaware] → Varfell shapes subsequent interactions using profile
                    (Asymmetric information: Varfell's offers and refusals are informed
                    by knowledge the party has not offered)
```

**Canon — P-08:** Profile is categorical, not quantitative. The epistemological barrier is metaphysical — Varfell can observe effects; they cannot render Thread Sensitivity as a number. This strengthens the arc: their knowledge is real but imprecise.

**Canon — P-03:** Information asymmetry between sensitives and non-sensitives is the core mechanic. This arc plays in that space at faction scale.

**Emergent logic:** Thread Sensitivity perception table + Varfell's Intel network + Private Collection action were written for independent purposes. Their interaction produces faction-level profiling of TTRPG-layer practitioners — a cross-layer visibility none of the rules were written to create.

**Arc shape:** 5–7 seasons. Profile exists before players are aware. Resolution depends on whether the party engages with Varfell before Varfell acts on it.

---

## Arc 55: The Withdrawal *(rebuilt — U-10, U-11)*

**Mechanical seed:** Guild Economic Leverage Failure → Guild Favour −1 in that territory → Guild Favour < 5 closes Guild Leverage eligibility in that territory → Guild action economy contracts → NPC bloc that factions rely on as economic buffer becomes unavailable

**Systems:** Guild Economic Leverage unique action (Wealth vs target Wealth, constraint: Guild Favour ≥ 5 in territory — stage6 confirmed) · Guild Favour (0–7, territory-level, oscillating) · Guilds Wealth 6 (starting) · Guilds NPC — no ethical framework named in fetched sources

---

### Narrative

The Guilds are not a player faction. They are a high-Wealth NPC bloc with a specific constraint: their Economic Leverage action can only target factions in territories where Guild Favour ≥ 5. Guild Favour moves in one confirmed direction from one confirmed trigger: Guild Economic Leverage Failure produces Guild Favour −1 in that territory. The Guilds do not like failing publicly — it reads as extortion that backfired.

Over several seasons, the Guilds have been active in the key trading territories. They have failed some rolls — not catastrophically, but consistently enough that Guild Favour in two territories has dropped from 5 to 4. They can no longer deploy Economic Leverage in those territories. Their action economy contracts. The territories where they cannot act are precisely the ones where the Crown had been using Guild pressure to manage Church economic influence.

The Crown loses an NPC tool it was relying on. The Guilds did not withdraw deliberately. Their failed rolls cost them the access threshold, and the threshold is binary: Guild Favour 5 = eligible, Guild Favour 4 = ineligible. One point of drift closes the action.

**Flowchart:**

```
Guilds active in key trading territories (Guild Favour 5 in target territories)
    │
    ▼
Guild Economic Leverage action: Wealth vs target faction Wealth
    │
    ├─ Overwhelming: target −1 Wealth + −1 Prosperity in one territory
    ├─ Success: target faction −1 Wealth for 1 season
    └─ Failure: Guild Favour −1 in that territory (confirmed, stage6 §8.6)
            │
            ▼
        Guild Favour: 5 → 4 in one or more territories
            │
            ▼
        Guild Favour < 5: Economic Leverage ineligible in that territory
            │
            ├─ Guilds cannot act in the territories where they dropped below threshold
            └─ Crown loses Guild pressure in those territories
                    │
                    ├─ Church economic expansion in formerly Guild-buffered territories
                    └─ [Players try to restore Guild Favour] →
                            No confirmed mechanic for restoring Guild Favour from outside.
                            Guild Favour only moves on Guild action failure (confirmed source).
                            Restoration requires Guilds to succeed in those territories again —
                            which requires getting their Favour back above 5 first.
                            [DESIGN GAP: Guild Favour restoration mechanic not specified.
                            Is there a player-accessible Domain Action to restore Guild Favour?
                            Requires design decision.]
```

**Note on inactivity:** No stat decay from skipping actions. If Guilds cannot act in certain territories, their consequence is simply the absence of their action — not a Stability or Wealth reduction from inactivity.

**Emergent logic:** The Guilds failed their own rolls. The failure cost is documented: −1 Guild Favour in that territory. The threshold is documented: Guild Favour ≥ 5 required to act. One point of drift closes an action permanently until restored. The Crown relied on this action being available and had no input into the Guilds' failure rate.

**Arc shape:** 3–6 seasons. Can develop quietly. Players notice when they try to invoke Guild pressure and find the Guilds cannot act in the territories that matter.

---

## Cross-Arc Interaction Table *(consolidated and corrected)*

| Arc pair | Interaction | Severity |
|----------|-------------|----------|
| 46 + 49 | Crown Suppress failures (Arc 46) make Hafenmark the only suppressor (Arc 49) — Crown weakness creates Hafenmark leverage | High |
| 46 + 50 | VTM contribution (Arc 50) adds +0.5–1.5/season to CI already not being suppressed (Arc 46) | Critical |
| 47 + 46 | CI ≥ 40 (Arc 46, if unaddressed) fires Coup Counter Trigger A (Arc 47) | Critical |
| 47 + 50 | VTM accelerating CI (Arc 50) can push CI past 40, triggering Coup Counter Trigger A (Arc 47) without any Crown failure | High |
| 48 + 50 | MS decay from Thread operations (Arc 48) + VTM advancing independently — both degrade shared infrastructure | High |
| 49 + 50 | Varfell suppressing own CI contribution competes for the one Suppress slot/season (Arc 49 + 50 cannot both Suppress simultaneously) | Medium |
| 51 + 54 | Higher Thread Sensitivity (Arc 51) produces higher-tier perception entries — at Thread Sensitivity 50–69, Varfell agents get cleaner pattern matching (Arc 54) | High |
| 52 + 53 | Vaynard wound-weakened Domain Actions may fail in Parliamentary contexts, contributing PI (Arc 52) | Medium |
| 53 + 47 | Crown territory loss from Varfell exploitation of wound-weakened period → fires Coup Counter Trigger C (Arc 47) | High |
| 55 + 46 | Guild Favour collapse (Arc 55) removes economic buffer from the territories Crown most needs to hold, accelerating territory loss risk → feeds Coup Counter Trigger C | Medium |
| 47 + 53 + 55 | Vaynard wounds reduce Varfell Domain Actions (Arc 53) → Varfell expansion stalls → Crown territory loss is more likely in adjacent zones → Coup Counter Trigger C closer; simultaneously Guild withdrawal (Arc 55) weakens Crown economic position → political vulnerability compounds | High |

**Critical stack — Arcs 46 + 47 + 50:**
- CI passive: +1/season
- VTM 4: +1/season
- No Suppress (Crown Stability 1): +0 mitigation
- Total CI advance: +2/season
- CI 28 → 40 (Coup Counter Trigger A): 6 seasons
- CI 28 → 60 (Seizure threshold): 16 seasons
- If Church Asserts even once: CI +2 replacing passive, net for that season = +3 including VTM

**Three-trigger convergence — Arc 47:**
Trigger A: CI crosses 40 unmitigated (Arc 46 + 50 compound)
Trigger B: Torben Loyalty degraded via Altonian diplomatic pressure
Trigger C: Crown territory loss during wound-weakened period (Arc 53) without military response
All three can fire within the same 6-season window without any player awareness of the Coup Counter.

---

## Design Gaps Identified (for Jordan)

| Gap | Arc | Description |
|-----|-----|-------------|
| PI per-action contribution table | 52 | PI advancement amounts per Domain Action type not specified in any fetched source. Params_board_game.md confirms track exists and auto-resolves at 20. Specific trigger amounts need design decision. |
| Guild Favour restoration mechanic | 55 | No confirmed player-accessible mechanic to restore Guild Favour. Guild Favour only moves (downward) on Guild Economic Leverage Failure. Upward movement source not documented. |

---

*Supersedes all prior versions. Canonical for arcs 46–55 as of 2026-04-13.*
*Sources used: stage6_factions.md, threadwork_redesign_v25.md, params_board_game.md, params_factions.md, params_core.md, clock_registry.md, canon/02_canon_constraints.md, canon/00_philosophical_foundations_rules.md §1–3.*


[PROVISIONAL: reference path updated to philosophical_foundations_rules.md — no content change]
