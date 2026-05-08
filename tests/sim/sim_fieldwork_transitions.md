# SIMULATION: Fieldwork System Transitions
## Mode C: Full Scenario (6 transitions) + Mode D: Edge Cases
## Date: 2026-04-13 | Reviewer: Opus 4.6
## Sources fetched: fieldwork_design_v1.md (720 lines), combat_design_v1.md (434),
##   social_contest_system_v2.md (405), mass_battle_v3.md (716), stage11_scale_transitions.md (138),
##   params_core.md (188), params_combat.md (286), params_threadwork.md (636), params_mass_combat.md (532)

---

## SCENARIO CONTEXT

**Season:** Summer, Year 2. RS: 65. CI: 34. IP: 28.

**Territory:** Ehrenfeld (T14) — Crown's military hinge. 5 connections. Fort 3.
Proximity Rating: 3. Piety Track: 2. Church Attention Pool: 0.
Crown-controlled. Löwenritter Coup Counter: 2.

**Dramatic situation:** Varfell intelligence suggests Löwenritter loyalists are smuggling
pre-Calamity weapons through Ehrenfeld to arm a coup attempt. The PCs are investigating
on Varfell's behalf while Crown forces prepare for a possible Altonian probe at the border.

### Characters

**Torsten** — Varfell Tribune agent. Non-sensitive investigator.
Agi 4, End 3, Str 3, Cog 5, Rec 4, Foc 3, Att 4, Bon 3, Cha 3, Spi 3.
History: "Varfell Intelligence Service" (4 pts). Cover = Cog 5 + Hist 4 = 9.
TS: 0. Certainty: 3. Coherence: 10. Momentum: 0. Wounds: 0.
Combat Pool: (4×2) + (4+3) = 15D (if using intelligence History for improvised combat).
Fieldwork Pool (Examine): (5×2) + (4+3) = 17D. Fieldwork Pool (Interview): (4×2) + (4+3) = 15D.
Health: End 3 + 6 = 9. Composure: Cha 3 + 6 = 9. Stamina: End 3 + 4 + 1 = 8 (no armour).
Armour: Light leather (DR 1 vs blade, 0 vs blunt). Weapon: Short Heavy Blade (arming sword, TN 6).

**Signy** — Restoration practitioner embedded as Torsten's "scholarly assistant."
Agi 3, End 3, Str 2, Cog 4, Rec 3, Foc 4, Att 5, Bon 4, Cha 2, Spi 5.
History: "Einhir Folk Practice" (3 pts). Cover = Cog 4 + Hist 3 = 7.
TS: 42. Certainty: 1 (Transitional). Coherence: 7. Momentum: 1. Wounds: 0.
Combat Pool: (3×2) + (3+3) = 12D (using folk practice as improvised).
Fieldwork Pool (Thread-Read): (5×2) + (3+3) = 16D + TPS(42÷10=4) = 20D.
Health: 9. Composure: Cha 2 + 6 = 8. Stamina: 7 (no armour).
Armour: None. Weapon: Staff (Long Light Blunt, TN 7).

---

## TRANSITION 1: INVESTIGATION → SCENE COMBAT

### Scene Setup

Torsten is conducting a Surveil action (Cognition-primary) on the Ehrenfeld armoury
at night, tracking a suspected Löwenritter courier. This is an active investigation:
"Who is smuggling weapons to the Löwenritter?" (Complex, Threshold 5). Evidence Track: 2/5.

**Fieldwork state at transition point:**
Torsten: Exposure 3 (Noticed — from prior actions this season). TN: 7. Ob: 2 (Hidden depth).

### Transition Trigger

Torsten succeeds on the Surveil (Cog 5×2 + Hist 4+3 = 17D, TN 7, Ob 2).
Most likely outcome: Success. Evidence Track: 2 + 2 = 4/5. Exposure: +2 (Surveil).
Total Exposure: 3 + 2 = 5 → equals Noticed threshold (Cover 9 → Noticed at 7).
Still below Noticed. Torsten remains undetected... for now.

**But the Surveil reveals:** The courier is loading crates NOW. Torsten moves closer.
A Löwenritter guard spots him.

**GM calls transition: Fieldwork → Combat.**

### Handoff Procedure

Per stage11 §11.2: this is not a Register Shift (that requires a social scene
changing nature). This is a direct transition: the situation has changed from
investigation to physical danger. No handoff rule explicitly covers
"Investigation → Personal Combat" in stage11.

**[FINDING F-TRANS-01]: Missing handoff rule.** stage11 §11.3 defines eight
handoff rules. None covers "Fieldwork → Personal Combat." The closest is
"Personal → Scene" (personal roll serves as opening move of a social scene),
but there is no "Fieldwork → Combat" equivalent.

**Proposed handoff rule:** When fieldwork is interrupted by hostile contact,
the transition follows these steps:
1. Current fieldwork action resolves (degree applied, Evidence/Exposure updated).
2. Combat begins. Initiative determined per combat_design_v1.md §3 (higher Attunement acts last in Exchange 1).
3. Fieldwork Exposure carries into the combat context — the character's compromised position may affect the combat (GM may grant the ambusher a positional advantage: +1D first exchange Offence, equivalent to Stunt bonus).
4. Evidence gathered this scene is retained regardless of combat outcome.

### Combat Resolution

**Exchange 1 — Initiative:**
Torsten Att 4 vs Guard Att 2. Torsten acts last (information advantage). Correct.
Guard declares pool split first.

**Guard stats (estimated Löwenritter soldier):**
Agi 3, End 3, Str 4. Combat Pool: (3×2) + (2+3) = 11D. Weapon: Short Heavy Blade (TN 6).
Light armour (DR 1 blade). Health: 9. The guard has surprise advantage: +1D Offence (Stunt: ambush positioning).

Guard declares: 7D Offence / 4D Defence (aggressive — discovered an intruder).
With Stunt: 8D Offence.
Torsten sees this, declares: 6D Offence / 9D Defence (defensive — caught off guard).

**Guard attacks:** 8D, TN 6 (Short Heavy Blade). E[net] ≈ 8 × 0.4 = 3.2.
vs Torsten Defence: 9D, TN 7. E[net] ≈ 9 × 0.33 = 3.0.
Net hits: ~0.2. With DR 1 (Torsten's leather): Damage = max(0, 0 + 4(Str) + 6(HBlade vs Light) - 1(DR)) = unlikely to land a meaningful hit this exchange.

P(guard net hits ≥ 1): approximately 55%. If hit: Damage = net hits + Str 4 + weapon mod (Heavy Blade vs Light = +2) − DR 1 = net + 5. At net 1: 6 damage. Torsten Health 9. Survives.

**Torsten attacks:** 6D, TN 6. E[net] ≈ 6 × 0.4 = 2.4.
vs Guard Defence: 4D, TN 7. E[net] ≈ 4 × 0.33 = 1.3.
Net hits: ~1.1. Damage = 1 + 3(Str) + 2(HBlade vs Light) − 1(DR) = 5.
Guard Health: 9 − 5 = 4. Not yet wounded.

**Exchange 2:** Initiative transfers to winner. Torsten likely won Exchange 1
(higher net damage). Torsten declares second.

Torsten's goal is ESCAPE, not kill. He declares **Establish Distance** (Priority 4).
If successful (Agility contest: Torsten 4 vs Guard 3): Torsten disengages and flees.

P(Torsten wins Agility contest): ~60%. Torsten escapes with evidence intact.

### State After Transition 1

```
Torsten: Health 9 (or 3 if hit), Wounds 0, Exposure 5 (T14).
  Evidence Track: 4/5. Last evidence: Observational (Surveil — identified courier).
  FINDING: Transition worked but EXPOSED A GAP — no formal handoff rule.
```

### Edge Cases

**F-TRANS-01 (P2):** No "Fieldwork → Combat" handoff in stage11. Must add.
**F-TRANS-02 (P3):** Should Exposure affect combat? Currently no rule. The ambusher's
Stunt bonus is a reasonable GM ruling but not codified. Proposal: "When combat
interrupts fieldwork at Exposure ≥ Noticed, the interrupting party gains +1D
on their first exchange Offence (positional awareness advantage)."

---

## TRANSITION 2: INVESTIGATION → DEBATE (CONTEST)

### Scene Setup

Torsten has gathered evidence (Evidence Track 4/5) identifying the courier.
He brings this to a Crown official (Lord Ehren, commander of the Ehrenfeld garrison)
in a formal audience. Torsten's goal: convince Lord Ehren to intercept the shipment.

Lord Ehren does not want foreign intelligence agents operating in his territory.
Torsten must persuade him.

**Fieldwork state at transition:**
Torsten: Evidence Track 4/5. Disposition with Lord Ehren: −1 (Wary — Varfell agent in Crown territory).

### Transition Trigger

Torsten attempts a **Negotiate** action (Attunement-primary, Ob = floor(Ehren's highest stat / 2) + 1).
Lord Ehren's highest stat: Military (estimated) 5. Ob = floor(5/2) + 1 = 3.

Torsten Negotiate pool: (Att 4×2) + (Hist 4+3) = 15D. TN 7. Ob 3 + 1 (Wary Disposition) = Ob 4.
P(≥4 net): ~37%.

**Most likely outcome: PARTIAL** (net 1-3). Ehren is unconvinced but not dismissive.

Per §5.7: Negotiate applies only when parties share a goal but disagree on method,
OR outcome is not consequential enough for full Contest. Here, the parties have
opposed positions (Torsten wants Crown military action; Ehren wants Varfell out
of his territory). This meets Contest initiation conditions (social_contest_system_v2.md §1):
"two or more parties with opposed positions AND outcome is uncertain and consequential."

**GM calls escalation: Fieldwork (Negotiate) → Contest (Royal Audience format).**

### Handoff Procedure

Per fieldwork_design_v1.md §5.7 (Contest Escalation):
1. Current Disposition (−1 Wary) maps to Piety Track offset: ±1 per 2 Disposition
   points, cap ±2. Disposition −1 → offset −0.5 → rounds to 0. Starting Conviction: 5.
2. Format: Royal Audience (social_contest_system_v2.md §2 Step 5). 3 exchanges.
   Lord Ehren objects throughout (asymmetric). Halved resistance for petitioner (Torsten).
3. Adjudicator type: Expert Judge (Lord Ehren evaluates arguments on merits).
   Primary attribute for Argue: **Cognition**.

**[FINDING F-TRANS-03]:** The transition from Negotiate (Attunement-primary) to
Contest (Cognition-primary for Expert Judge) changes the relevant attribute mid-interaction.
This is correct — Negotiate is about reading the other party and calibrating;
Contest is about constructing arguments. The skill set genuinely shifts. Not a problem.

### Evidence as Contest Argument

Torsten's evidence (Observational from Surveil + Documentary from prior Research)
can be cited in the Contest:

Per social_contest_system_v2.md §4 Step 3: "+2D when citing a specific, named,
verifiable claim (document, date, prior statement, named precedent)."

Torsten cites the Surveil evidence (names the courier, the time, the armoury).
This is a Recall bonus: +2D on the Argue roll. Evidence tag: Observational (admissible).

### Contest Resolution (abbreviated)

**Torsten Argue pool:** (Cog 5×2) + (Hist 4+3) = 17D + 2D (evidence citation) = 19D.
TN 7. Genre: Memory (citing what he observed). Primary genre match: +1D.
Total: 20D.

**Lord Ehren Argue pool (estimated):** (Cog 4×2) + (Hist 3+3) = 14D.
Genre: Projection (arguing what will happen if Varfell is allowed to operate).
Not primary genre: +0D. Total: 14D.

Exchange 1 — CROSS (different genres):
Torsten effective margin: floor(20D × 0.33 / 2) = floor(3.3) = 3.
Ehren effective margin: floor(14D × 0.33 / 2) = floor(2.3) = 2.
Net movement: 1 toward Torsten. Piety Track: 5 → 4. Halved resistance for
petitioner (Royal Audience): resistance effectively 0 for Torsten.

After 3 exchanges (Torsten's evidence advantage gives him ~60% per exchange):
Expected final Conviction: ~3. Side B wins (≤ 3). Torsten's petition succeeds.

**Domain Echo:** Ehren agrees to intercept the shipment. Crown Military action
in Ehrenfeld next season. Varfell Mandate +0 (no faction change — this is a
private agreement, not a public political act).

### State After Transition 2

```
Torsten: Evidence Track 4/5 (investigation not yet complete — Contest used evidence
  but did not resolve the investigation itself). Piety Track: 3 (Torsten wins).
  Composure: some strain accumulated (1-3 from exchanges). Exposure: unchanged
  (Contest was a formal audience, not fieldwork).
  FINDING: Investigation continues after Contest. Evidence is consumed as argument
  but the investigation's question ("Who is smuggling?") is not answered by winning
  the debate. The Evidence Track remains at 4/5.
```

### Edge Cases

**F-TRANS-04 (P2):** Does using evidence in a Contest "consume" it from the
Evidence Track? **NO.** Evidence is information — citing it in a debate does
not erase it. The investigator still has the evidence. The investigation
continues. But this should be stated explicitly.

**F-TRANS-05 (P3):** Disposition with Lord Ehren after Contest. The Contest
Piety Track result implies Ehren was persuaded. Should Disposition update?
**Proposed rule:** After a Contest won by the petitioner, the adjudicator's
Disposition shifts +1 toward the winner (grudging respect or acceptance).
After a Contest lost: Disposition −1 (resentment or dismissal).

---

## TRANSITION 3: INVESTIGATION → MASS BATTLE

### Scene Setup

Torsten's investigation has progressed (Evidence Track 4/5). Meanwhile, an
Altonian probing force crosses Lowenskyst (T3) and pushes into Ehrenfeld (T14).
Crown forces muster. Torsten is embedded with Crown forces as a Varfell observer.

Signy is present as Torsten's "assistant" — actually a Restoration practitioner
who will operate Thread support if needed.

### Transition Trigger

GM declares mass battle. The investigation is **suspended**, not abandoned.
Evidence Track freezes at 4/5. The investigation question remains open.

**[FINDING F-TRANS-06]:** No explicit rule for suspending fieldwork during
mass battle. Investigation persistence (§4.1) says "persistent across scenes
and sessions," which covers this — the mass battle is a new scene. But
should be explicit: "Mass battle suspends all active fieldwork. Evidence Tracks
freeze. Exposure continues to accumulate only from battle-relevant actions
(e.g., Thread operations during battle)."

### Mass Battle Setup

**Crown forces:**
Unit 1: Ehrenfeld garrison. Size 5, Power 4, Discipline 5.
General: Lord Ehren. Command: floor((Cha 4 + Cog 4) / 2) = 4.
Effective Pool: min(5, 4) + 4 = 8D.

**Altonian probe:**
Unit 1: Vanguard. Size 4, Power 3, Discipline 4.
General: Altonian captain. Command: 3.
Effective Pool: min(4, 3) + 3 = 6D.

**Signy's position:** Reserve (rear). Can safely Leap in Phase 4 for
offensive Thread operations, or Phase 6 for support Threadweave.

### Battle Turn 1

Phase 1 — Strategy Declaration: Both sides declare Offence/Defence split.
Crown: 5D Off / 3D Def (confident — larger force).
Altonia: 3D Off / 3D Def (probing — testing Crown response).

Phase 2 — Volley: Crown has no ranged. Altonia has crossbow sub-unit.
Altonia Volley: 2D (crossbow sub-unit), TN 7. E[net] = 0.66.
Damage recorded, deferred to Phase 6.

Phase 3 — Manoeuvre: No special manoeuvres declared.

Phase 4 — Offensive Thread Operations:
Signy is in Reserve → safe Leap window. She declares a Thread-Read
(perceptive Leap) on the Altonian formation, not an offensive operation.

**[FINDING F-TRANS-07]: Thread-Read during mass battle.** The fieldwork system
defines Thread-Read as a perceptive Leap (§4.5). Mass battle defines Phase 4
as "Offensive Thread Operations." A Thread-Read is not offensive — it is
perceptive. Can Signy Thread-Read during Phase 4?

**Proposed ruling:** Thread-Read during mass battle resolves in Phase 4
(same window as Thread operations) but is classified as an intelligence
action, not an offensive action. It does not produce offensive damage.
Co-movement still fires (it is a Leap). Evidence Track advances if applicable.

Signy Thread-Reads the Altonian formation for Thread-adjacent intelligence.
Pool: 20D. TN 7. Ob: 3 (Buried — military intelligence at Thread level).
Her investigation question: "Does the Altonian force carry Thread-enhanced
equipment?" This is a NEW investigation (Simple, Threshold 3). Evidence: 0/3.

P(≥3 net): ~78%. Most likely: Success. Evidence Track: 0 + 2 = 2/3.
Co-movement fires: temporal (minor History Resonance), epistemic (Signy
perceives the Altonian soldiers' Thread configurations — they carry no
Thread-enhanced equipment, but their commander has a Thread-Locked pendant),
actualized (d6 → 2 = no environmental effect).
Coherence: Object/Personal scale → 0 auto-cost. Coherence stays at 7.
Exposure: +1 (Thread-Read) + 1 (sensitive at Depth 3+) = +2. Total Exposure: 2 (T14).

Phase 5 — Engagement: Crown 5D Off vs Altonia 3D Def. Crown 3D Def vs Altonia 3D Off.
Crown likely wins Phase 5 (8D pool vs 6D pool, Crown attacking with larger force).
Expected Altonian Size loss: 1-2. Expected Crown Size loss: 0-1.

Phase 6 — Cascade: Apply all damage. Altonia Size: 4 → ~2-3. Crown Size: 5 → ~4-5.

### State After Turn 1

```
Crown: Size ~4-5, Discipline 5, Morale stable.
Altonia: Size ~2-3, Discipline check (lost more than Crown → if Size loss > Discipline: −1).
Signy: Coherence 7, Exposure 2, Evidence Track (Altonian investigation): 2/3.
Torsten: Exposure 5, suspended investigation (smuggling): 4/5. Observing battle.
```

### Edge Cases

**F-TRANS-07 (P2):** Thread-Read in mass battle Phase 4 — intelligence vs offensive.
Must classify and add to fieldwork handoff rules.
**F-TRANS-08 (P3):** Signy's Exposure during mass battle. Exposure is per-territory.
Battle Exposure stacks with fieldwork Exposure in the same territory. Signy at
Exposure 2 + future battle Thread ops could hit Watched (threshold 7 for Cover 7)
within a few turns. This is correct — sustained Thread activity in battle draws
Church attention after the battle ends (at Accounting).

---

## TRANSITION 4: SCENE COMBAT → INVESTIGATION

### Scene Setup

After escaping the armoury guard (Transition 1), Torsten retreats to a safe house.
He examines the wound from the fight (if he took one) and begins examining a
document he grabbed during the escape — a shipping manifest from the courier's crate.

### Transition Trigger

Combat ends (Torsten escaped via Establish Distance). The scene transitions
naturally from combat to investigation. No formal handoff needed — the combat
scene concludes and a new fieldwork scene begins.

### Handoff Procedure

Per stage11 §11.2: this is a Zoom Out (combat was a moment of violence within
a larger investigation arc). The Zoom Out fires automatically when combat ends.

**State carries forward:**
- Wounds from combat persist: if Torsten took a wound, −1D to physical fieldwork
  (Endurance-based, Surveil) per §2.2.
- Momentum gained from Overwhelming combat result (if any) carries to fieldwork.
- Exposure from the combat scene: the fight itself was conspicuous. GM rules:
  +2 Exposure (combat in a restricted area draws attention).

Torsten Exposure: 5 (prior) + 2 (combat conspicuousness) = 7.
Cover 9: Noticed at 7. **Torsten is now Noticed** in Ehrenfeld.
+1 Ob to all fieldwork rolls remainder of season.

### Investigation Continues

Torsten examines the shipping manifest.
Action: Examine (Cognition-primary). The manifest is physical evidence at Hidden depth (Depth 2).
Pool: 17D. TN 7. Ob: 2 (Hidden) + 1 (foreign) + 1 (Noticed) = Ob 4.
P(≥4 net): ~61%. Expected net: 5.6.

Most likely outcome: Success. Evidence Track: 4 + 2 = 6/5. **THRESHOLD REACHED.**

Investigation resolves: "The courier is Hauptmann Greis, a Löwenritter officer using
Crown military supply chains to move pre-Calamity weapons from Einhir cache sites
in Kronmark (T2) through Ehrenfeld (T14) to a Löwenritter staging area."

**Finding tag:** Verified (physical document) + Observational (Surveil).
Strongest tag: Verified. Admissible in Contest, Court, or Domain Action justification.

### State After Transition 4

```
Torsten: Evidence Track: RESOLVED. Exposure 7 (Noticed). Wounds: 0 or 1.
  Finding: "Löwenritter smuggling via Crown supply chains." Tag: Verified.
  FINDING: Transition smooth. Combat → Investigation requires no special handoff.
  Wounds and Exposure carry naturally. The +1 Ob from Noticed made the final
  Examine harder — correct consequence for a messy escape.
```

### Edge Cases

**F-TRANS-09 (P3):** Combat Exposure. The system has no rule for Exposure gained
from combat during a fieldwork arc. The GM ruling (+2) is reasonable. Codify:
"Combat that occurs during a fieldwork arc generates Exposure in the current
territory: +1 for a quiet fight (subdued opponent, no witnesses), +2 for a
conspicuous fight (noise, property damage, witnesses), +3 for a public battle
(multiple combatants, civilian observers)."

---

## TRANSITION 5: DEBATE (CONTEST) → INVESTIGATION

### Scene Setup

Torsten has won the Royal Audience with Lord Ehren (Transition 2). Ehren agrees
to intercept the shipment. During the Contest, Ehren's arguments revealed something
Torsten did not expect: Ehren mentioned a "sealed inventory" that Crown intelligence
keeps on all Löwenritter-associated officers.

This is an Appraise result from the Contest (social_contest_system_v2.md §4 Step 1):
at Overwhelming Appraise, the appraiser learns "one specific detail: a key individual's
Belief, the audience's resistance threshold, or the opponent's emotional state."

Torsten's Appraise revealed: Ehren's emotional state is *fear*, not anger. Ehren
knows more about the Löwenritter plot than he has admitted.

### Transition Trigger

Contest concludes. Torsten opens a NEW investigation: "What does Lord Ehren know
about the Löwenritter plot that he hasn't shared?" (Simple question, Threshold 3).
Evidence Track: 0/3.

**No handoff rule needed.** The Contest ends, the scene continues as fieldwork.
The Contest's Appraise result feeds directly into the investigation as a clue:

**Evidence from Contest:** The Appraise result is information gained through
social perception (Attunement). It has reliability tag: **Testimonial** (the
information came from reading a person's emotional state, not from a document).
Evidence Track: 0 + 1 = 1/3 (Appraise result counts as Partial-quality evidence —
a direction, not a full detail).

### Investigation Continues

Torsten's Disposition with Ehren is now +0 (post-Contest: winner's Disposition
shift +1 from −1 Wary = 0 Neutral). Torsten attempts a Read (Attunement-primary)
on Ehren to probe his fear.

Pool: (Att 4×2) + (Hist 4+3) = 15D. TN 7. Ob: 2 (Hidden depth — Ehren's
hidden motivation). Disposition 0 → +0 Ob modifier.
P(≥2 net): ~86%.

Most likely: Success. Evidence Track: 1 + 2 = 3/3. **THRESHOLD REACHED.**

Investigation resolves: "Ehren knows the Löwenritter are smuggling weapons
because his own quartermaster is complicit. Ehren has been covering for the
quartermaster to avoid a scandal that would cost him his command. Ehren's
agreement to intercept is an attempt to clean up the mess before Crown
central command discovers his negligence."

**Finding tag:** Testimonial (from Read). Admissible in Contest but −1
reliability if Ehren is hostile to the presenter.

### State After Transition 5

```
Torsten: Evidence Track (Ehren investigation): RESOLVED. Disposition with Ehren: 0.
  Two resolved investigations:
  1. "Löwenritter smuggling" (Verified) — Threshold 5, completed.
  2. "Ehren's complicity" (Testimonial) — Threshold 3, completed.
  Exposure: unchanged from Contest (formal audiences don't generate Exposure).
  FINDING: Contest → Investigation is the smoothest transition. Appraise results
  from Contest feed naturally as investigation evidence. Disposition post-Contest
  sets the starting conditions for continued social fieldwork.
```

### Edge Cases

**F-TRANS-10 (P2):** Appraise result as Evidence Track contribution. The system
currently does not define how Contest Appraise results translate to investigation
evidence. **Proposed rule:** "Information gained through a Contest Appraise action
(social_contest_system_v2.md §4 Step 1) may be applied to an active Evidence
Track as +1 progress (Partial-quality). Reliability tag: Testimonial. This
application is automatic — no additional fieldwork action required."

**F-TRANS-11 (P3):** Multiple resolved investigations creating a composite
intelligence picture. Torsten now has two Findings. Can they combine?
**Proposed rule:** "Multiple resolved Findings on related topics can be
presented as a combined argument in Contest. The combined argument uses
the strongest constituent reliability tag. Each additional Finding beyond
the first adds +1D to the Argue roll (max +2D from combined Findings).
This represents the rhetorical weight of convergent evidence."

---

## TRANSITION 6: MASS BATTLE → INVESTIGATION

### Scene Setup

The Altonian probe has been repulsed (Turn 1 of Transition 3). Crown forces
hold Ehrenfeld. Post-battle, the field is strewn with dead Altonian soldiers.
Signy's Thread-Read during the battle revealed the Altonian commander's
Thread-Locked pendant.

### Transition Trigger

Mass battle concludes. GM declares Zoom Out from battle to post-battle scene.
Per stage11 §11.2: Zoom Out widens focus from mass combat to personal/scene scale.

**State carries forward from battle:**
- Signy's Evidence Track (Altonian investigation): 2/3. Partially complete.
- Signy's Coherence: 7 (unchanged — no Coherence cost at Personal scale).
- Signy's Exposure: 2 (from battle Thread-Read).
- Crown unit status: Size ~4-5, Discipline 5. Battle won.

**Fieldwork resumes.** Signy's suspended investigation reactivates. She needs
1 more progress to resolve.

### Investigation Continues

Signy examines the Altonian commander's body (the commander was killed or
captured during the rout). She performs an Examine (Cognition-primary) on
the Thread-Locked pendant.

Pool: (Cog 4×2) + (Hist 3+3) = 14D. TN 7. Ob: 3 (Buried — Thread-locked
artifact, Einhir-era). Signy has TS 42 (≥ 10 gate met).
P(≥3 net): ~59%.

Most likely: Success. Evidence Track: 2 + 2 = 4/3. **THRESHOLD EXCEEDED.**

Investigation resolves at Depth 3: "The pendant is a Thread-Locked Einhir
communication device. The Altonian commander was receiving Thread-transmitted
intelligence from inside Valoria. Someone with TS ≥ 30 and access to Einhir
infrastructure is feeding Altonian invasion planning. The source is somewhere
in the southern peninsula — the pendant's Thread signature traces toward
the Southernmost."

**Finding tag:** Verified (physical artifact) + Thread-verified (Thread-Read
during battle). Strongest non-Thread tag: Verified. Admissible to non-sensitive
audiences. Thread-verified component adds detail accessible only to TS ≥ 30
characters.

**Rendering strain:** Signy handled the Thread-Locked pendant directly.
Depth 3 → Minor strain. TS 42 ≥ 10 gate: no mechanical effect. Certainty
pressure: Signy is already at Certainty 1 (Transitional), below the Depth 3
automatic-movement threshold (≥ 3). No shift.

### Domain Echo

This Finding has faction-level scope. Per stage11 §11.5: "When a personal
action has faction-level scope, the GM recognises it as a Domain Action."

The discovery that Altonia has a Thread-connected intelligence source inside
Valoria is faction-level intelligence. **Domain Echo fires:**
- Varfell Influence: +0 (Torsten is Varfell's agent, but the discovery benefits
  all factions equally — shared threat).
- IP effect: The GM may rule +1 IP at next Accounting (Altonia's intelligence
  network is more sophisticated than assumed).
- Narrative hook: New investigation opens — "Who is the Thread-sensitive mole
  feeding Altonian intelligence?"

### State After Transition 6

```
Signy: Evidence Track (Altonian investigation): RESOLVED.
  Coherence 7. Exposure 2 (T14). TS 42.
  Finding: "Altonian Thread-intelligence network." Tag: Verified + Thread-verified.
Torsten: Evidence Track (smuggling): RESOLVED. Evidence Track (Ehren): RESOLVED.
  Exposure 7 (Noticed).
  Domain Echo: IP +1 at Accounting (GM ruling).
```

### Edge Cases

**F-TRANS-12 (P2):** Post-battle investigation timing. Should the post-battle
Examine consume a fieldwork time unit (scene action)? Or is it part of the
battle aftermath (no time cost)? **Proposed rule:** "Post-battle investigation
of the battlefield (examining bodies, equipment, terrain) constitutes one
fieldwork scene. It consumes one time unit and may generate Exposure normally.
The battle itself does not consume fieldwork time units — it is a separate
activity that interrupts the season's fieldwork budget."

**F-TRANS-13 (P3):** Thread-Locked artifact examination. Signy used Examine
(Cognition-primary), not Thread-Read (Attunement-primary), because the pendant
is a physical object at Depth 3. But the Thread-Locked nature means Thread
perception would add depth. Should examining a Thread-Locked artifact require
Thread-Read? **Ruling:** No. Examine at Depth 3 with TS ≥ 10 suffices to
identify the artifact's function. Thread-Read would reveal additional detail
(the specific Thread signature, the source direction — Depth 4 content).
The two methods access different depths of the same object. This is the
dual-path design working correctly.

---

## TRANSITION SUMMARY

| # | Transition | Handoff Quality | Gap Found? |
|---|-----------|----------------|------------|
| 1 | Investigation → Combat | Functional but MISSING RULE | **F-TRANS-01 (P2):** No explicit handoff |
| 2 | Investigation → Debate | Clean — Disposition → Conviction offset | F-TRANS-04 (P2): Evidence consumption clarity |
| 3 | Investigation → Mass Battle | Functional — suspension rule needed | **F-TRANS-06 (P2):** No explicit suspension rule |
| 4 | Combat → Investigation | Smooth — wounds/Exposure carry naturally | F-TRANS-09 (P3): Combat Exposure codification |
| 5 | Debate → Investigation | Smoothest — Appraise feeds evidence | **F-TRANS-10 (P2):** Appraise → Evidence Track rule |
| 6 | Mass Battle → Investigation | Clean — resume from frozen state | F-TRANS-12 (P2): Post-battle time accounting |

## FINDINGS REGISTER

### P2 Findings (must resolve before fieldwork is fully playable)

| ID | Description | Proposed Fix |
|----|-------------|--------------|
| F-TRANS-01 | No "Fieldwork → Combat" handoff in stage11 | Add 9th handoff rule: current action resolves → combat begins → Exposure carries (ambusher may gain +1D from positional awareness at Noticed+) |
| F-TRANS-04 | Using evidence in Contest: does it "consume" from Evidence Track? | No. Add explicit statement: "Evidence cited in Contest is not consumed. The Evidence Track and its contents persist." |
| F-TRANS-06 | No fieldwork suspension rule for mass battle | Add: "Mass battle suspends active fieldwork. Evidence Tracks freeze. Resume after battle at frozen state. Battle actions do not consume fieldwork time units." |
| F-TRANS-07 | Thread-Read in mass battle Phase 4 classification | Thread-Read is intelligence, not offensive. Resolves in Phase 4 window. Co-movement fires. Evidence Track advances. No offensive damage. |
| F-TRANS-10 | Contest Appraise → Evidence Track | Appraise result = +1 Evidence Track progress (Partial quality, Testimonial tag). Automatic, no additional action. |
| F-TRANS-12 | Post-battle investigation time accounting | One fieldwork scene. Consumes one time unit. Battle itself does not consume fieldwork budget. |

### P3 Findings (polish)

| ID | Description | Proposed Fix |
|----|-------------|--------------|
| F-TRANS-02 | Exposure → combat advantage | At Noticed+, interrupting party gains +1D first exchange Offence |
| F-TRANS-05 | Post-Contest Disposition update | Winner: Disposition +1 with adjudicator. Loser: −1. |
| F-TRANS-09 | Combat Exposure values | Quiet fight: +1. Conspicuous: +2. Public battle: +3. |
| F-TRANS-11 | Combined Findings in Contest | Each additional Finding beyond first: +1D Argue (max +2D). |
| F-TRANS-13 | Thread-Locked artifact Examine vs Thread-Read | Examine at Depth 3 identifies function. Thread-Read at Depth 4 reveals configuration. Dual-path works correctly. |

## EMERGENT PROPERTIES

1. **Evidence pipeline across systems.** Evidence gathered in fieldwork feeds directly
into Contest arguments (+2D Recall bonus). Contest Appraise results feed back into
investigation. The systems are porous in the right direction — information flows
freely but changes form (evidence tag) as it crosses system boundaries.

2. **Exposure as cross-system pressure.** Combat during a fieldwork arc adds Exposure.
Battle Thread operations add Exposure. Exposure from any source feeds the same
per-territory track, creating genuine trade-offs: aggressive investigation makes
combat riskier (Noticed → ambusher advantage), and conspicuous combat makes
subsequent investigation harder (+1 Ob at Noticed).

3. **Sensitive/non-sensitive party dynamics persist across transitions.** Signy's
Thread-Read during mass battle generated Exposure that persists after the battle.
Torsten's documentary evidence has broader institutional admissibility. The
epistemological barrier shapes every transition: non-sensitives gather admissible
evidence and provide institutional cover; sensitives access deep information
but attract attention. This holds in combat (Signy is more conspicuous),
investigation (Thread-Read generates Exposure), Contest (Thread-verified evidence
is inadmissible in Church tribunals), and mass battle (Thread operations in
Phase 4 are detectable).

4. **Domain Echo from investigation.** The discovery of the Altonian Thread-intelligence
network produces a faction-level consequence (IP +1) without any deliberate
Domain Action. This is stage11 §11.5 working as intended: "the GM recognises
faction-level scope from personal roll." Investigation → Domain Echo is not
currently in the eight handoff rules but functions naturally through existing
stage11 principles.

5. **Desperate Trail never triggered.** Across all six transitions, no character
hit 3 consecutive failures. At these pool sizes (14-20D) against Ob 2-4,
Desperate Trail is genuinely rare (~0.1-1% probability). It functions as a
safety valve for low-pool characters or extreme-Ob situations, not as a routine
mechanic. This is correct — investigation should normally progress, and
Desperate Trail is the exception that proves the fail-forward rule.
