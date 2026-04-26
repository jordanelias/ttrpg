# VALORIA — NPC · Faction · Arc Interdependency Matrices & Throughlines
**Date:** 2026-04-18 | **Source authority:** arc_register v8, npc_behavior_v30, arc_expansion_v1, faction_politics_expanded_v1, throughline_analysis_2026-04-17, throughline_resolutions_v1

> **Glossary note:** **CI** = Church Influence (Church institutional advancement clock, 0–100; renamed from Theocracy Counter per ED-782). Conviction Track (CT) is always written in full. (ED-756)

---

## HOW TO READ THIS DOCUMENT

**Interdependency matrices** show what each NPC/faction/arc depends on and what depends on it. Read rows as *providers*; read columns as *receivers*. An entry means: the row entity exerts force on the column entity through the specified mechanism. Blank = no direct mechanical dependency.

**Throughlines** synthesize the chains — what accumulates, what it converts into, what terminal states it produces. They are not arc summaries; they are the structural spines that connect disparate arcs into campaign-level trajectories.

**Symbols:** `→` converts into; `↔` mutual dependency; `⊗` mutual exclusion (cannot coexist at threshold); `∅` terminates the relationship; `↑` accelerates; `↓` decelerates; `⚠` single-point-of-failure; `★` player-decisional pivot

---

## PART I — NPC INTERDEPENDENCY MATRIX

### §1.1 Primary Named NPC × Primary Named NPC

Rows = source NPC. Columns = target NPC. Entry = dependency mechanism.

|  | **Almud** | **Himlensendt** | **Baralta** | **Vaynard** | **Ehrenwall** | **Edeyja** | **Vossen** | **Torben** |
|---|---|---|---|---|---|---|---|---|
| **Almud** | — | CI suppression sustained by Détente (ARC-S37); Crown inaction → CI unchecked | Détente: mutual benefit while Baralta Mandate ≥ 4; collapses at CI 42, ARC-S45, ARC-T19 | Diplomatic distance; no direct arc link | Coup Counter depends on 3 Crown behaviors; Almud's Discovery Event fires ARC-T19 governance pause → Counter may increment | Thread Liaison (ARC-S28) → Crown co-victory MS tracking | No direct arc; Crown's PI management indirectly sustains RM | **★** Torben Loyalty is Crown's primary external vulnerability; Almud's Arc B/C directly determine Torben's arc state |
| **Himlensendt** | CI accumulation pressure on Crown; ARC-T14 Consecration Crisis; ARC-T19 triggered by Almud's Discovery Event | — | ARC-S06 Baralta as CI brake; ARC-T03 Excommunication Himlensendt→Baralta. CI brake ends permanently on success | Church ontological suppression vs Vaynard's TK advancement; ARC-P04 Axis 9 | ARC-S03 Tribunal; no direct personal arc link | Thread suppression vs Warden work; ARC-T16 pastoral overwrite in same southern communities as Wardens | ARC-T16 Perceptual Prophylaxis runs in RM territories; ARC-S47 Cultural Reclamation in same communities | ARC-S07 Tutoring Demand fires at IP 30; Torben as religious education subject |
| **Baralta** | Détente; ARC-S45 Deed Claim activates on Almud weakness | ARC-S06 CI suppression (−1/season); ARC-T03 Excommunication target | — | No direct arc; Hafenmark Parliamentary vs Varfell Counter-Narrative (ARC-S30) | ARC-S06 Baralta's deed-logic and Ehrenwall's deed-logic: parallel, not linked | No direct arc | ARC-S43-ext Parliamentary Resentment | No direct arc |
| **Vaynard** | No direct arc; TK advancement feeds CI → Crown pressure | ARC-S01 Revelation Cascade: TK 3/4/5 = CI +1/+2/+3 | Parliamentary vs Counter-Narrative (ARC-S30); VTM Discretion (PP-438) allows CI suppression | — | No direct arc | **⚠** Warden-Vaynard: Edeyja's teaching is the only stable TS development path; without her, Vaynard → Arc C Consumed | RM/Varfell alignment possible if Maret Uln succession (NPC-ARC-ULN) | ARC-S31 Lock Distribution: Vaynard decides recipients including all named TS characters |
| **Ehrenwall** | **★** Coup Counter: 3 independent triggers, none decrements; Torben Loyalty ≤ 3 → Counter +1 | No direct arc | No direct arc | No direct arc | — | No direct arc | No direct arc | Cross-NPC: Torben Conviction = Order → Counter resets 0 (her Arc A triumph) |
| **Edeyja** | No direct arc | ARC-T16 cultural contest in same territories as Church missionaries | No direct arc | **⚠** Vaynard's death → Edeyja: Belief 2 update; WR requirement +1 for next player | No direct arc | — | ARC-S50-ext: RM communities in Proximity 1 are MS early-warning | No direct arc |
| **Vossen** | No direct arc; Crown PI management indirectly supports RM stability | ARC-T16: competing in same communities | ARC-S43-ext Parliamentary Resentment | Maret Uln succession: Varfell-RM alignment | No direct arc | ARC-S50-ext: community overlap in T6/T13 | — | No direct arc |
| **Torben** | **⚠** Loyalty track (8→0) at −1/season Covert Contact fail; Loyalty ≤ 3 → Counter +1; Loyalty ≤ 2 → Crown Mandate −2 | No direct arc | No direct arc | Vaynard's Consequence MS: one approach vector to Torben | Cross-NPC: Torben Conviction = Order → Counter reset | No direct arc | Cross-NPC: Torben Conviction = Equity → Vossen Arc B positive branch | — |

---

### §1.2 Secondary NPC × Primary NPC (One-Way Dependencies)

| **Secondary NPC** | **Primary dependency** | **Mechanism** |
|---|---|---|
| **Haelgrund (Church)** | Himlensendt | Arc A: neutral. Arc B: Whistleblower after player shows Evidence of Ministry corruption. Arc C: TS 20+, covert Thread-aware bureaucrat. Controls peninsula institutional memory. |
| **Klapp (Cardinal Temperance)** | Himlensendt | ARC-S08/S21: TS growth check per Thread exposure. At ARC-S21 crossing → CI pause + internal fracture. Cross-NPC: Himlensendt Arc B opens Klapp's dataset-sharing channel (COLLISION A potential). |
| **Olafsson (Cardinal Justice)** | Baralta | ARC-T03 Excommunication prosecutor. 2-season build. P(success) at Mandate 4 = 32%; Mandate 3 = 66%. |
| **Jarnstal (Cardinal Fortitude)** | Himlensendt | NPC-ARC-JAR: Independence Drift 0→3, never decrements. At Drift 3: military deploys on perceived threats without Himmensendt's direction. Himlensendt Arc C → Jarnstal Arc C (Schismatic General). |
| **Vorn (Cardinal Prudence)** | Himlensendt | ARC-S29 Cardinal Schism: fires at Church Stability 2 + hostile Senator same season. Embezzlement trail (Zoom In trigger). |
| **Torsvald (Riskbreaker)** | Ehrenwall | NPC-ARC-TOR: ~30% abort rate in Thread-active territories → Deniability Debt +1. Pattern → Ehrenwall/Brandt detection. Cross-NPC: Niflhel catastrophic extraction → mandatory Discovery Event for Torsvald. |
| **Brandt (Löwenritter)** | Ehrenwall | NPC-ARC-BRA: activates on Ehrenwall removal. Military redirects T3/T10 defense. Counter threshold drops 3→2. |
| **Orm (Warden)** | Edeyja | Cross-NPC: Orm's death → Edeyja Coherence −1 + WR requirement rebuild. |
| **Maret Uln (Varfell)** | Vaynard | NPC-ARC-ULN: activates on Vaynard elimination. VTM resets 0. Varfell aligns RM. |
| **Hann (RM secondary)** | Vossen | Operational complement; Consequence MS (operational failure). Takes leadership on Vossen elimination. |
| **Strand (Crown)** | Almud | NPC-ARC-STR: Intel Overwhelming → turn. Full Crown stat line + planned actions leak. Crown admin +1 Ob 2 seasons on removal. |
| **Laskaris (Altonian)** | Elske/Crown | NPC-ARC-LAK: PROTECTIVE delays Tutoring Demand 1 season; flips if Elske Loyalty ≤ 2 → IP +3 immediately. |
| **Solberg (Schoenland)** | Crown/Hafenmark | NPC-ARC-SOL: STABILITY-SEEKING bias downplays intelligence. Recall on discovery fires → replacement, no bias, Schoenland more dangerous. |
| **Virke (Niflhel)** | Niflhel structure | NPC-ARC-VIR: 3rd protection incident → replacement; all trade +1 Ob permanently. ARC-T25 ultimatum at incident 2. |
| **Elske (Crown)** | Almud/Torben | ARC-S23: Contact Ob 3. Three vectors. Laskaris flips at Elske Loyalty ≤ 2. Pre-coup diplomatic investment → Season 17 Regency (ST-52). |
| **Lenneth (Crown/Varfell-adjacent)** | Almud/Baralta | ARC-S26 Lenneth-Baralta Collision: mutually exclusive programmes. Both exist only while Almud is uncertain. ARC-S18 Western Archive (Varfell-side). |
| **The Witness (RM)** | Vossen/Church | ARC-T23: institutional continuity, not personal memory. Current TS 19–35. COLLISION E: simultaneous testimony source against Himlensendt. |
| **Almstedt (Hafenmark IC)** | Baralta | Deed-monarchy institutional memory. Only NPC who remembers original Almqvist founding terms. |
| **Thale (Crown IC)** | Almud | Spymaster; background obscured, Southern Einhir rumored. Niflhel contacts. Disposition −1 Haelgrund. |
| **Linder (Crown IC)** | Himlensendt/Almud | Church Canon seconded to Crown. Reports weekly to Himlensendt. Disposition −2 to Thread-practitioner players structurally. |
| **Kreutz (Crown IC/Löwenritter)** | Almud/Ehrenwall | Seconded to Royal Guard. Pre-designated allegiance to Almud personally — but coup targets Almud through Kreutz first. |

---

## PART II — FACTION INTERDEPENDENCY MATRIX

### §2.1 Faction × Faction: Structural Leverage Points

|  | **Crown** | **Church** | **Hafenmark** | **Varfell** | **Löwenritter** | **RM** | **Guilds** | **Niflhel** |
|---|---|---|---|---|---|---|---|---|
| **Crown** | — | CI Suppress (Royal Decree), ARC-T17 Diplomatic Outreach; Consortium threat: Thread Liaison (ARC-S28) theological signal | Treaty (PP-512–514); TE-01 loss → Baralta claim advances | ARC-S07 Torben; ARC-T17 Schoenland (vs Altonia) | Coup Counter triggers (3 independent); Kreutz dual-loyalty | Crown PI management sustains RM stability indirectly | ARC-P09 Royal Debt → Guilds leverage; ARC-T24 Tax Revolt | NPC-ARC-STR Strand turned → Crown stats exposed |
| **Church** | ARC-P01 CI passive +1/season + Conviction Yield; ARC-T14 Consecration Crisis; TE-08 Cathedral Falls | — | ARC-T03 Excommunication (Baralta); ARC-S19 Quaestio; ARC-S06 brake | ARC-S01 TK→CI +1/2/3 per TK level; ARC-S30 Counter-Narrative | TE-09 Mountain Garrison (adjacent +1D); ARC-S03 Tribunal | ARC-T16 Perceptual Prophylaxis vs ARC-S47 Cultural Reclamation (same communities) | TE-05 Mineral Leverage (Church controls T8); ARC-T24 Church Sanctuary offer | ARC-S11 Niflhel covert CI out of Crown reach (ARC-S09 Framework Trap) |
| **Hafenmark** | ARC-S37 Détente; ARC-T22 Trade Network (Guilds adjacent); TE-04 Highland Parliament | ARC-S06 CI brake (−1/season); ARC-S19 Quaestio | — | ARC-S30 Counter-Narrative (CI contest); TE-32 NW Corridor Control | ARC-S56 Lions' Table Fracture; TE-24 Flanking Route | ARC-S43-ext Parliamentary Resentment | ARC-T22 Hafenmark Trade Network: Guilds +1D defending Hafenmark |  — |
| **Varfell** | ARC-T21 Path Split; ARC-S27 Revelation Token | ARC-S30 Counter-Narrative; VTM Discretion (PP-438) | TE-29 Timber Contest; ARC-S44 Schoenland Gambit (counter) | — | No direct arc | NPC-ARC-ULN: Maret Uln succession → RM alignment | ARC-S52 Feldhaus Gambit (Varfell offer: trade intel for Collection use) | ARC-S11 Niflhel/Virke supply chain; ARC-S31 Lock Distribution through Quiet arm |
| **Löwenritter** | Coup Counter (ARC-P03); ARC-S57 Riskbreaker Exposure | ARC-T26 Martial Honour Violation | No direct arc | No direct arc | — | No direct arc | No direct arc | Torsvald × Niflhel proximity (Cross-NPC conditioner) |
| **RM** | ARC-S22 RM Emergence (WA/CV/MS triple condition); ARC-S49 Rawlsian Bind | ARC-S48 Vossen Saturation vs Church Heresy Investigation | ARC-S43-ext Parliamentary Resentment | NPC-ARC-ULN (Maret Uln alignment) | No direct arc | — | No direct arc | NPC-ARC-VOS: Maret Uln (if active) slows Church AP accumulation vs Vossen |
| **Guilds** | ARC-P09 Royal Debt; ARC-T24 Tax Revolt; ARC-S52 Feldhaus (Crown offer: Charter) | ARC-T24 Church Sanctuary offer | ARC-T22 Trade Network; ARC-S12 Favour Gate | ARC-S52 Feldhaus Gambit (Varfell offer) | No direct arc | No direct arc | — | NPC-ARC-FEL Supply Chain Exposure (Thread-touched goods via Niflhel/Virke) |
| **Niflhel** | NPC-ARC-STR Strand | ARC-S46-ext Inquisition Overwhelming; ARC-S55 Arms conflict | ARC-S11 Headless Network; ARC-S55 | ARC-S54 Quiet Overreach (TT accumulation) | ARC-S57 Riskbreaker Exposure Spiral | NPC-ARC-VOS (Maret Uln protection) | NPC-ARC-FEL Supply Chain | — |

---

### §2.2 Faction × Territory: Control Leverage

| Territory | **Owner gain** | **Wrong-owner cost** |
|---|---|---|
| T1 (Crown capital) | Baseline Crown function | TE-01: Crown Wealth −1/season, PI +2, Baralta claim ↑ |
| T8 (Hafenmark/Gransol) | Parliament operational | TE-04: Baralta personally retakes; ARC-S24 if she's dead |
| T9 (Church/Himmelenger) | CI Conviction Yield hub; +1D adjacent | TE-08: Church Mandate −3; Grand Debate |
| T12 (Varfell/Sigurdshelm) | Intel/Private Collection base | TE-10: Intel −2, VTM resets, Collection contested ⚠ |
| T14 (Löwenritter/Ehrenfeld) | 5-connection strategic hub | TE-26: controller +1D Military from T14 |
| T15 (Askeheim/Southernmost) | WC/WR progression | TE-13: Military → WC −1; TE-14: non-practitioner force collapses |
| T13 (Oastad/southern gate) | Varfell gate control | TE-12 + TE-16: WR pause; Church intel +1D |
| T6 (Stillhelm) | Crown southern route | TE-19: WC −1 if Crown was providing Warden access |
| T3 (Lowenskyst) | Border fortress | TE-22/23: Fort 0+IP 60 → Crown Military −1D; Fort 4+Military 5 → AER +1, IP −2 |
| T10 (Spartfell) | NW corridor anchor | TE-24/25: Hafenmark −1D without it; NW closed with T17+Military 3 |

---

## PART III — ARC INTERDEPENDENCY MATRIX

### §3.1 Clock Arcs → Faction Arc Cascade

Each clock arc is not self-contained — it feeds into or gates faction arcs. This matrix traces the cascade.

| **Clock Arc** | **Directly gates** | **Indirectly enables** | **Terminal if unaddressed** |
|---|---|---|---|
| ARC-P01 CI Accumulation | ARC-S19 Quaestio (CI 42); ARC-T03 Excommunication opportunity; TE-02 Territorial Seizure (CI 60); ARC-T10 Phase Transition (CI 75) | Church Priority Tree restructures; Rawlsian Bind fires (CI 50); Détente collapses (CI 42) | CI 75: territorial seizure mode, suppression irrelevant |
| ARC-P02 MS Decay | ARC-S15 Southernmost Spiral (MS 50); ARC-S05 Temporal Window (MS 60); ARC-S34 Edeyja Burnout | TE-15 Wound Speaks (MS 19); ARC-S33 Lattice of Enemies | MS 0: second Calamity |
| ARC-P03 Coup Counter | ARC-S56 Lions' Table Fracture (Counter 2); Coup fires (Counter 3) | Counter 2: ARC-T13 Torben transfer; NPC-ARC-BRA Brandt succession | Martial Law; Crown faction under Löwenritter control |
| ARC-P06 IP Accumulation | ARC-S07 Torben Loyalty Clock (IP 30); ARC-T02 Tutoring Demand (IP 30) | ARC-S23 Elske window closes on Torben loss; COLLISION C risk | IP 100 + AER ≤ 1: Altonian Conquest |
| ARC-P07 Public Instability | ARC-T24 Tax Revolt (PI 6+); ARC-S24 Baralta Succession gate | PI 10: institutional collapse; PI 8: Stability checks | PI 10: institutional collapse event |

---

### §3.2 Arc Chain Visualization (Primary Chains)

#### Chain A — CI/Church Domination Chain
```
ARC-P01 CI passive +1/season
    ↓ [no Crown action]
    → CI 40 → ARC-P03 Counter trigger #1 (Crown inaction)
    ↓ [Quaestio]
    → CI 42 → ARC-S19 Quaestio (Grand Debate fires)
              → Baralta forced public position
              → ARC-S37 Détente collapses
    ↓ [Baralta Mandate erodes]
    → ARC-T03 Excommunication → brake ends permanently → CI +4 one-time
    ↓
    → CI 60 → Territorial Seizure active
    ↓
    → CI 75 → ARC-T10 Phase Transition → Church priority restructures
              → COLLISION J: T9+T2+CI 60+MS 39 → Church siege of southern gates
```

#### Chain B — MS Collapse Chain
```
ARC-P02 MS Decay (−1 to −23/season depending on conditions)
    ↓ [no mending]
    → MS 60 → ARC-S05 Temporal Window closes (Past-Oriented Pulling unavailable)
    ↓
    → MS 50 → ARC-S15 Southernmost Spiral activates
              → ARC-S48 RM Vossen Saturation durability tested
              → BG-CV-05 Memory Lives fires
    ↓ [no stabilization]
    → MS 40 → Fractured → TE-17/18 Proximity 1 effects active
              → COLLISION J conditions approach
    ↓
    → MS 19 → ARC-S32 Mending Trap: individual throughput (6–10 MS/season) < decay (12–23/season)
             → ARC-S33 Lattice of Enemies: Belief compatibility blocks cooperation
             → ARC-S34 Edeyja Burnout: Ob compounds precisely when most needed
             → TE-15 Wound Speaks: Structural Dissolution required; success −3 to −8 MS
    ↓
    → MS 0 → Second Calamity
```

#### Chain C — Torben Conviction Race
```
Season 1–8: Investment window
    ↓ [faction Disposition ≥ +2 with Torben]
    → First faction at +2 before Season 8 sets primary Conviction [LOCKED]
    ↓ [if no faction reaches +2]
    → Default: Order (Crown institutional baseline)

IP 30 → ARC-S07 Tutoring Demand → Loyalty −1/season on Covert Contact fail
    ↓ [Loyalty ≤ 3]
    → ARC-P03 Counter +1
    → ARC-S20 Ehrenwall's Count accelerates

Almud Arc B (Fortress) → Cross-NPC: Torben Loyalty check → whichever faction has Disposition ≥ +2 LOCKS his Conviction this season
Almud Arc C (Overthrown) → Cross-NPC: Torben Loyalty → Ehrenwall; Conviction shifts to Ehrenwall's direction

[After Conviction locked:]
Torben Conviction = Order → Counter resets 0 [Ehrenwall Arc A triumph]
Torben Conviction = Reason → Vaynard/Maret Uln Arc B cross-trigger; Crown+Varfell co-victory path opens
Torben Conviction = Equity → Vossen Arc B positive branch; RM wins cultural argument
```

#### Chain D — Thread Axis Pressure Chain
```
ARC-P04 Axis 9 (background — irreversible accumulation)
    ↓
    → Vaynard TK 2+ → ARC-S40 Forgetting and the Scholar (political Axis 2 accessible)
    → Vaynard TK 4 → ARC-S31 Lock Distribution: 3–5 simultaneous Discovery Events possible
    → Vaynard TK 5 + MS ≤ 19 → NPC-ARC-VAY Unchecked → TE-13/14 (Warden threshold events)
    ↓
    → ARC-S01 Revelation Cascade: TK 3/4/5 = CI +1/+2/+3
    → ARC-S13 Duke Awakens: Discovery Event → TS 30; Certainty −1; TK +2
    ↓
    → ARC-T08 Vaynard's Confession: Hybrid moment; personal arc enters Parliamentary system
    → ARC-T21 Path Split: Path A (intelligence supremacy) ⊗ Path B (Warden Recognition)

    [If Edeyja × Vaynard unconnected:]
    → Vaynard enters Arc C Consumed: non-practitioner at high TS without Edeyja instruction
    → Edeyja receives Cross-NPC: WR +1 requirement for next player
```

#### Chain E — Crown Fracture Chain
```
ARC-P03 Counter accumulation
    ↓ [Counter 2]
    → ARC-S56 Lions' Table Fracture: Deed vs Failure Faction
    → Two Riskbreakers may implement partial Martial Law (2 territories)
    ↓ [Counter 3]
    → Coup fires → Almud Arc C (Overthrown)
    → Torben Loyalty → Ehrenwall
    → Baralta ARC-S45 Deed Claim activates (Coup Counter ≥ 2)
    → ARC-S35 Succession Vacuum: Torben + Elske + Lenneth simultaneously relevant
    → COLLISION F Succession Triangle fires

    [Parallel — ARC-S26 Lenneth-Baralta Collision:]
    → Almud's uncertainty enables both programmes simultaneously
    → Loss of uncertainty (Discovery Event, 218 AG truth) → COLLISION F fires
```

---

### §3.3 Collision Map (Full Cross-Arc Convergences)

| **Collision** | **Trigger pair** | **Combined effect** | **Player agency window** |
|---|---|---|---|
| **COLLISION A** — Church Double Fracture | Klapp conversion (ARC-S21) + Olafsson exposure (ARC-S06) simultaneously | Church Stability −3; CI generation pauses; removes education AND justice leadership simultaneously | Evidence MS engagement with Klapp before Olafsson fires; timing requires 2-track management |
| **COLLISION B** — Practitioner King | Almud TS 28→30 (ARC-S17) + Elske independent (ARC-S23) + Torben in Altonia (ARC-S07) | Crown distributed across 3 people in 3 states; CI +3 but MS improves | Requires sustained investment in Elske track AND Almud Thread exposure — different action budgets |
| **COLLISION C** — Tutoring + Southernmost | Torben Loyalty ≤ 3 (ARC-S07) + Southernmost Ritual failure (ARC-T04) | MS +8, IP +2, CI +2 same season; if MS near 50: cracking clock + MS +2/season | Prevent by maintaining Torben Loyalty above 3 AND sustaining Southernmost ritual capability — both are demanding |
| **COLLISION D** — Niflhel Weaponises | Church-Niflhel exposure + 218 AG assassination = Niflhel + Vaynard Collection in Niflhel hands | Niflhel has leverage over Crown, Church, Varfell simultaneously; sells to highest bidder | Prevent 218 AG discovery routing to Niflhel; or prevent Collection transfer; mutually exclusive preventions |
| **COLLISION E** — Einhir Elder and Baralta's Claim | Witness testimony (ARC-T23) + Baralta Solmund claim (ARC-S19) + Klapp archive access | Himlensendt's Evidence MS turned against Church by 3 simultaneous sources; Church Stability −3 if Grand Debate fails | Operational — ARC-T23 is resolved canonical; COLLISION E is live |
| **COLLISION F** — Succession Triangle | Almqvist deed-presumption weakens + Lenneth programme (ARC-S26) + Baralta Deed Claim (ARC-S35) both active | Three-way succession contest; mutually exclusive programmes; Ehrenwall must evaluate all three by deed-logic | Player faction positioning within triangle is permanent commitment — no temporary alliances |
| **COLLISION G** — Einhir Triangle | Lenneth revival + Baralta suppression + Vaynard revolutionary restoration all active | No stable coalition possible; Lenneth+Vaynard: diagnosis agree/treatment don't; Lenneth+Baralta: orientation agree/Einhir don't; Vaynard+Baralta: nothing | Player alignment within triangle is factional commitment |
| **COLLISION J** — Church Siege Southern Gates | Church T9+T2 (TE-28) + CI 60+ + MS ≤ 39 | Church winning political contest simultaneously destabilizes the substrate through which it wins; T15 access fires TE-13/14 | Prevent by keeping Church from T9+T2 control simultaneously; or prevent MS from reaching Fractured |

---

## PART IV — NPC × ARC ACTIVATION MATRIX

### §4.1 Which NPCs are the primary arcs' mechanical triggers

| **Arc** | **Primary NPC activator** | **Secondary NPC activator** | **Player-influenced** |
|---|---|---|---|
| ARC-P01 CI Accumulation | Himlensendt (institutional) | Baralta (suppressor) | Yes — CI Suppress action; ARC-T17 Diplomatic |
| ARC-P02 MS Decay | Edeyja (sole restorer at scale) | Vossen/RM (Community Weaving) | Yes — Expedition, Mending, Lock/Gap resolution |
| ARC-P03 Coup Counter | Ehrenwall (evaluates) | Torben (Loyalty ≤ 3 trigger) | Yes — maintain Torben Loyalty; Crown military response |
| ARC-P06 IP | Laskaris (delay) → Flip (spike) | Vaynard (TK → CI feeds IP indirectly) | Yes — AER, Diplomatic Outreach, Elske track |
| ARC-S06 Baralta Holds Line | Baralta | Olafsson (prosecution) | Yes — protect Baralta Mandate |
| ARC-S07 Torben Loyalty Clock | Torben | Laskaris | Yes — Covert Contact 3+ seasons floors at 6 |
| ARC-S08 Faith That Destroys | Klapp | Himlensendt (must respond) | Yes — Thread exposure pacing; 3-exposure cascade |
| ARC-S13 Duke Awakens | Vaynard | Practitioners providing exposure | Yes — Private Collection use rate |
| ARC-S15 Southernmost Spiral | Edeyja | Orm | Yes — Weaving stabilization Ob 3 |
| ARC-S19 Quaestio | Baralta/Himlensendt | All factions at CI 42 | Yes — keeping CI below 42 |
| ARC-S21 Klapp Threshold | Klapp | Himlensendt | Yes — sustained archive contact |
| ARC-S23 Elske Independence | Elske | Laskaris | Yes — three approach vectors; Loyalty-dependent |
| ARC-S25 Warden Cooperation | Edeyja | All expedition factions | Yes — expedition engagement is the only advancement path |
| ARC-S31 Lock Distribution | Vaynard | All TS 10+ characters | Yes — who receives Locks is the highest-impact single decision |
| ARC-S32 Mending Trap | Edeyja | All practitioners | Yes — multiple practitioners in rotation required |
| ARC-S33 Lattice of Enemies | All practitioners | — | Yes — Belief revision is the only resolution |
| ARC-S34 Edeyja Burnout | Edeyja | — | Yes — reduce operational burden on her through parallel Mending |
| ARC-S45 Deed Claim | Baralta | Ehrenwall (deed-logic follower) | Yes — Almqvist deed-presumption maintenance |
| ARC-S56 Lions' Table Fracture | Ehrenwall | Brandt | Yes — Coup Counter management |
| ARC-T03 Excommunication | Olafsson | Church Mandate level | Yes — keep CI below 55 for Parliamentary Stay window |
| ARC-T19 Governance Pause | Almud | — | Yes — controlling whether Discovery Event is attempted |
| NPC-ARC-TOR Torsvald Exposure | Torsvald | Ehrenwall/Brandt | Yes — pacing of Riskbreaker operations in Thread-active territories |
| NPC-ARC-ULN Maret Uln Succession | Maret Uln | Vaynard (must be eliminated) | Yes — Vaynard protection |

---

### §4.2 NPC Scar × Arc State Map

Scars are the micro-mechanism by which Contests permanently alter NPC arc trajectory. This maps Scar states to arc transitions.

| **NPC** | **Scar 0 (stable)** | **Scar 1 (conflict)** | **Scar 2 (transition)** | **Scar 3+ (crisis)** |
|---|---|---|---|---|
| Almud | Arc A/B by game state | Order + Reason active simultaneously; governance pauses possible | Primary may shift to Reason; Arc C vulnerability increases | Unpredictable; Coup Counter has less predictable trigger |
| Himlensendt | Default zealot | Cross-NPC Kald dataset-sharing opens (if Arc B) | Conviction crisis; Cardinals receive independence signals | COLLISION A precondition |
| Baralta | Constitutional proceduralism | Ad hoc action possible; Excommunication survival opens | Pragmatist (Arc B) available; Niflhel alliance possible | Leadership Deviation effectively eliminated |
| Vaynard | Knowledge-seeker | Consequence + Evidence both active | Primary may shift to Autonomy; Arc C Consumed risk | Thread operations without safety awareness |
| Ehrenwall | Institutional loyalist | Solidarity MS opens | Military self-determination | All decisions determined by crisis table |
| Edeyja | Holdout | Starts accepting evidence from outsiders | Arc B Collaboration | Arc C Final Stand |
| Vossen | Principled organiser | Consequence MS opens | Principles vs survival explicit choice | Rawlsian Bind fires regardless of CI level |

---

## PART V — THROUGHLINES

Throughlines are structural threads that run across multiple arcs, multiple NPCs, and multiple factions. They are not "stories" — they are mechanical spine structures that produce emergent narratives.

---

### THROUGHLINE 1: The CI/MS Pyrrhic Trade

**Structural form:** CI and MS move inversely under Church advancement. Every Church political victory degrades the substrate through which the victory is exercised.

**Mechanical nodes:**
- ARC-P01 CI +1/season passive → every Conviction Yield territory adds to this
- ARC-S01 TK 3/4/5 → CI +1/2/3 → Vaynard's research is Church's weapon against itself
- ARC-S09 Framework Trap → Crown's ethical frameworks prevent blocking covert CI
- COLLISION J → Church at T9+T2+CI 60+MS 39: institutional victory + substrate collapse simultaneous

**Player experience:** The player who lets Church grow powerful discovers the world is becoming ungovernable in parallel. The player who suppresses Church discovers CI management is itself an action economy drain. There is no cost-free solution — only different distributions of damage.

**Design verdict (confirmed ST-02, ST-05, ST-21):** Structural spine is working. CI 65 Church win = pyrrhic at mechanical level.

---

### THROUGHLINE 2: Torben as Latent Campaign Configuration

**Structural form:** Torben Almqvist is not a character — he is the campaign's most consequential uncommitted resource. Whatever 6–8 seasons of Disposition investment produces in him determines the character of Crown (Valoria's largest faction) for the campaign's final third.

**Mechanical nodes:**
- Season 1–8 investment window → first faction at Disposition ≥ +2 locks Conviction [IRREVERSIBLE]
- IP 30 → Tutoring Demand → Loyalty −1/season without Covert Contact → Coup Counter trigger
- Almud Arc B/C → Cross-NPC Torben Conviction formation acceleration
- Torben Conviction = Order → Counter reset (Ehrenwall wins without coup)
- Torben Conviction = Reason → Crown+Varfell co-victory path opens
- Torben Conviction = Equity → RM has produced a king who believes what they believe
- Torben Conviction = Autonomy (secondary, always present) → he follows strength when cornered

**Player experience:** Factions that ignore Torben lose control of the largest faction on the board. The optimal play is not obvious from Turn 1 — the investment value only becomes legible when Almud's arc begins shifting. By then, the window may be closing.

**Design verdict (confirmed ST-52, ST-58):** Investment competition correctly calibrated. Each Conviction produces genuinely distinct Crown Priority Tree behavior.

---

### THROUGHLINE 3: The Practitioner Bottleneck

**Structural form:** MS recovery requires practitioners. Practitioners are scarce, fatiguing, and mutually incompatible at Belief level. The world cannot be saved by individual heroism — but collective heroism requires exactly the political reconciliation the game's factions are trying to prevent.

**Mechanical nodes:**
- ARC-S32 Mending Trap: individual seasonal output 6–10 MS vs passive decay 12–23/season
- ARC-S33 Lattice of Enemies: opposing Beliefs → ~40% abort risk on collective operations
- ARC-S34 Edeyja Burnout: Ob compounds as MS falls; the most capable practitioner degrades precisely when most needed
- ARC-T18 Overweaving Cascade: uncoordinated Weaving → MS −6 to −12 in mass battle
- ARC-S04 Rendering Debt: mass battle × 3 MS cost → sustained operations hollow practitioners
- ARC-S31 Lock Distribution: who receives Locks → 3–5 simultaneous Discovery Events; new practitioners, but also new political complications
- Calamity reversal (4 practitioners TS 50+): gate inaccessible until Season 33+ even with optimal play

**Player experience:** Players who understand this throughline early invest in: (a) practitioner development across factions; (b) Belief compatibility management; (c) protecting Edeyja from operational overload. Players who don't understand it discover in mid-campaign that the world is degrading faster than they can restore it.

**Design verdict (confirmed ST-37, ST-57):** Correctly gated late-game achievement. The bottleneck is structural, not accidental.

---

### THROUGHLINE 4: The Information Asymmetry Economy

**Structural form:** Varfell's intelligence advantage is the campaign's most persistent resource imbalance — but it is also the campaign's most fragile single-point-of-failure (T12 loss = VTM reset, Collection contested). The tension between leveraging the advantage and protecting the infrastructure is Varfell's core strategic problem.

**Mechanical nodes:**
- ARC-S27 Revelation Token Cascade: 2 tokens on 2 factions = Path A "fully revealed" → all factions want to destroy Varfell while depending on it (only Varfell knows Altonian movements)
- ARC-S38/S40 Archive operations: Southernmost + pre-Forgetting records = permanent expedition bonuses
- ARC-S39 Fjord Blockade: Military T11+T12 → Guilds trade +1 Ob; NPC-ARC-SOL recall triggers earlier
- TE-10: ⚠ T12 loss = Intel −2, VTM reset, Collection contested — single point of failure confirmed BALANCE-002
- ARC-T21 Path Split: Path A (exposure) ⊗ Path B (Warden). Pursuing A makes Askeheim harder; pursuing B requires restraint that contradicts A
- NPC-ARC-ULN: Vaynard elimination → Maret Uln; VTM resets; RM alignment; information economy restructures

**Player experience:** Varfell players must choose between leveraging intelligence for political dominance (Path A) and using it for Thread work (Path B). They cannot fully pursue both. The faction that appears to be "winning" through information control may be producing exactly the conditions that bring everyone against it.

**Design verdict (confirmed ST-51):** Correctly specified as faction-agnostic intelligence market. Asset placement mechanic is the appropriate power level.

---

### THROUGHLINE 5: The Succession Compression

**Structural form:** Four succession crises are latent simultaneously — Crown, Church, Löwenritter, and Hafenmark. Each has different mechanics, different timelines, and different costs. They can converge. When they do, the campaign's political map can restructure in a single Accounting.

**Mechanical nodes:**
- Crown: Torben Loyalty track + 218 AG Investigation (ARC-P08) + Almud Longevity (12%/year) + COLLISION F Succession Triangle
- Church: Himlensendt Longevity (6%/year) + Cardinal fracture (4 arcs simultaneously on Arc C) + ARC-T14 Consecration Crisis
- Löwenritter: Ehrenwall Longevity (12%/year) + NPC-ARC-BRA Brandt succession; or post-coup Torben/Torsvald/Templar succession
- Hafenmark: Baralta Longevity (6%/year) + ARC-S24 Baralta Succession (PI gate)
- Generational Shift (§8, PP-660): Generational Shift now reaches within campaign timeline (corrected from 40 to ~10 seasons)

**Player experience:** The factions' institutional continuity is not guaranteed. NPCs die or are deposed. The player who has invested in successors and inner circles is positioned for post-transition play; the player who ignored them faces a board that has been reconfigured by events they did not influence.

**Design verdict (confirmed §8 correction, throughline_resolutions_v1):** Generational Shift fix makes succession crises mechanically reachable within campaign scope. ★ Critical correction.

---

### THROUGHLINE 6: Obligation as Distributed Consequence Engine

**Structural form:** The Obligation system is the game's most cross-cutting mechanic. Obligations produced in Grand Contests persist for 4 seasons, cascade across NPCs and arc conditioners, and distribute consequences across multiple Accountings.

**Mechanical nodes:**
- Grand Contest Obligation violated → all NPCs Disposition ≥ +1 with violating faction: −1 Disposition (network contracts)
- Church Obligation honored → Kald Evidence MS check: 1 fewer Scar to fire (docility rewarded in specific arc terms)
- Crown Obligation honored (T10 garrison) → Ehrenwall: Coup Counter −1
- Crown Obligation violated (T10 garrison) → Ehrenwall: Coup Counter +1
- Varfell Obligation honored (MS data to Wardens, 3 seasons) → Edeyja: WR +1

**Player experience:** Obligations are not optional narrative commitments — they are mechanical leverage. Honoring them advances NPC arcs in favorable directions; violating them cascades backward through relationship networks. The player who uses social contest system only tactically misses the arc-conditioning function of Obligation fulfillment.

**Design verdict (confirmed ST-28):** Most over-performing mechanic in the game. 3-Obligation cascade produced 7 correctly targeted consequences with no conflicts. Robust beyond its surface specification.

---

### THROUGHLINE 7: The Southern Einhir Cultural Contest

**Structural form:** The same communities — southern Einhir in T6, T13, T5 — are the contested ground for three simultaneous non-military operations: Church pastoral overwrite (ARC-T16), RM Cultural Reclamation (ARC-S47), and Calamity Radiation MS effects (proximity 1 conditions). These do not conflict mechanically — they compete for the same cultural substrate.

**Mechanical nodes:**
- ARC-T16 Perceptual Prophylaxis: Church missionaries educate AND overwrite — same act
- ARC-S47 Cultural Reclamation: RM Presence in 4+ territories → Community Memory Event; non-practitioners produce oral accounts (P-08 compliant)
- TE-21 Folklore Season: MS 79–60 + Proximity 1 in T6 → Church Influence +1 Ob; RM Presence −1 Ob
- ARC-S50-ext: RM communities in Proximity 1 are MS early-warning system
- COLLISION G Einhir Triangle: Lenneth (revival from above) + Baralta (suppression) + Vaynard (revolutionary restoration) — no stable coalition

**Player experience:** Southern territories are not military objectives — they are cultural ones. The player who sends military units there (TE-13/14 Warden threshold events) is playing the wrong game. The player who cultivates RM Presence, Warden access, and Lenneth's archive programme is building in the correct domain.

**Design verdict:** Three-way cultural contest produces genuine scene content without requiring player direction. The communities are already contested; player action modulates the contest, not initiates it.

---

### THROUGHLINE 8: NPC Conviction as Political Topology

**Structural form:** The 7 NPCs' Conviction taxonomy is not character flavor — it is the political map's underlying topology. Alliances that look politically natural may be Conviction-incompatible; alliances that look impossible may be Conviction-compatible. The Resonant Style vulnerabilities are the player's diplomatic terrain.

**Conviction map:**
| NPC | Primary | Secondary | Alignment with |
|---|---|---|---|
| Almud | Order | Reason | Evidence of systemic failure reaches him; Consequence of his Order breaks things |
| Himlensendt | Faith | Order | Evidence only — specific, documented, verifiable; Authority from Holy See theoretically |
| Baralta | Precedent | Faith | Evidence that procedure failed to prevent specific injustice |
| Vaynard | Reason | Autonomy | Consequence: his pursuit producing specific bad outcomes; Evidence: data beyond his TK |
| Ehrenwall | Order | Autonomy | Consequence: her actions producing instability she exists to prevent; Solidarity: comrade bonds |
| Vossen | Equity | Continuity | Solidarity: communities she has promised; Consequence: harm to those she serves |
| Edeyja | Continuity | Reason | Evidence: Thread state data, demonstrated competence only |

**Incompatibility traps:**
- Almud (Order/Reason) + Vaynard (Reason/Autonomy): shared Reason but Almud's Order contradicts Vaynard's Autonomy
- Baralta (Precedent) + Vaynard (Reason): Baralta's procedure vs Vaynard's consequentialism — no overlap
- Ehrenwall (Order) + Vossen (Equity): Ehrenwall's institutional Order vs Vossen's grassroots Equity — structurally incompatible
- Himlensendt (Faith) + Edeyja (Continuity): Faith vs empirical Thread work — Himlensendt cannot engage Evidence from Edeyja's domain

**Compatible through Resonant Style:**
- Almud + Edeyja: Almud's Consequence MS (show him Thread reality cost) + Edeyja's Evidence MS (show him Thread data) — Evidence can work on Almud because his Reason is secondary
- Baralta + Haelgrund: both Precedent/Continuity; proceduralism binds them even without faction alignment
- Vaynard + Haelgrund: both Reason-adjacent; archive contact creates Belief-compatibility for Thread collective operations

---

## PART VI — STRUCTURAL GAPS (FROM THROUGHLINE ANALYSIS)

These are gaps where the interdependency network has identified missing mechanics. All are canonical open items.

| Gap | Structural location | Impact |
|---|---|---|
| **ED-671 Thread-perception census** | Thread Axis 4 / ARC-P04 | Unknown penetration of Thread Sensitivity in general population; MS implications under-specified |
| **ED-666 Path B speed-run** | Varfell Path B calibration | WR 4 achievable too quickly in some configurations; Edeyja contact devalued |
| **ED-667 Coup Counter readiness gap** | ARC-P03 / Löwenritter | Counter 2 to 3 transition: Lions' Table Fracture mechanics need resolution order with ARC-T26 |
| **ED-632 Shadow Renown** | Riskbreaker sub-office | Deniability Debt mechanic exists; Shadow Renown tracking not fully mechanized |
| **ED-633 Deniability Debt** | Riskbreaker/ARC-S57 | Accumulation rate vs suppression rate not canonically specified |
| **ED-629 Heresy Proceedings auth loop** | Church Inquisitor; ARC-S46-ext | Phase 1 declaration mechanic for Partition needs co-specification with Heresy filing |
| **ED-663 Wealth cap** | Faction economy | Wealth ceiling not specified; Guilds BG-CV-04 victory (Wealth ≥ 6) may be unreachable at wrong cap |
| **Unnamed — ED-416** | ARC-S15 Southernmost | Southernmost Ritual required for cracking timeline; ritual not named or specified |
| **EDITORIAL: TE-08 Grand Debate** | CI 42 Quaestio + T9 loss | Whether both can fire same campaign arc and in what order — not specified |
| **EDITORIAL: TE-15 Structural Dissolution Ob** | MS Critical; Edeyja Burnout | Canonical Ob for Structural Dissolution targeting catastrophic Gap emergent not established |
| **EDITORIAL: ARC-S35 Deed-claim Ob** | Crown succession | Starting Ob for deed-claim invocation on weakened Almqvist deed-presumption not set |

---

## APPENDIX — QUICK-REFERENCE INTERDEPENDENCY LEGEND

**Single-point-of-failure NPCs:**
- ⚠ Baralta: sole institutional CI brake; elimination = permanent brake loss + CI +4
- ⚠ Edeyja: sole Structural Dissolution practitioner; only stable TS development path for Vaynard; MS recovery leader
- ⚠ Vaynard: VTM, TK, Private Collection all housed at T12; T12 loss = total Varfell intelligence collapse
- ⚠ Torben: campaign's most consequential uncommitted political resource; window Season 1–8 only

**Mutual exclusion pairs (⊗):**
- Varfell Path A (intelligence supremacy) ⊗ Path B (Warden Recognition) — pursuing one makes the other harder
- Lenneth revival programme ⊗ Baralta Crown claim (ARC-S26) — mutually exclusive programmes; Almud's uncertainty is the only coexistence condition
- ARC-S47 Cultural Reclamation ⊗ ARC-T16 Perceptual Prophylaxis — competing in the same communities simultaneously; not mechanically exclusive but culturally zero-sum

**Irreversible thresholds:**
- CI 42 → Quaestio fires; Détente forced to collapse
- CI 60 → Territorial Seizure active; suppression no longer sufficient
- CI 75 → Phase Transition; AER no longer modifies CI gains
- Coup Counter 3 → Coup fires; no decrement mechanic
- Torben Conviction lock → Season 8; permanently irreversible
- Baralta Excommunication success → brake ends permanently
- NPC Longevity death → succession fires; prior NPC investment does not transfer except where specified
- MS 0 → Second Calamity; no mechanic prevents it from this state

**Player-decisional pivots (★):**
- ★ Torben Disposition investment (Season 1–8): highest single-campaign impact
- ★ ARC-S31 Lock Distribution: who receives Locks; 3–5 simultaneous Discovery Events
- ★ ARC-T21 Path Split: Varfell Path A vs B (permanent strategic posture)
- ★ ARC-S49 Rawlsian Bind at CI 50: Principles maintained vs suspended (explicit player declaration)
- ★ Löwenritter Elske investment (Season 3–7): produces pre-coup Regency by Season 17 (ST-52)
- ★ Haelgrund Arc path: Arc A (neutral) / Arc B (Whistleblower) / Arc C (Archivist) — who controls peninsula institutional memory
