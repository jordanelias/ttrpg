# VALORIA — EMERGENT ARC SKELETON TEST — BATCH 8 (COUNTERFACTUAL)
## Session: 2026-04-17 | Counterfactual branch exploration across Batches 2–7
## Method: Each scenario identifies a major mechanical branch point from a prior scenario, 
## takes the path NOT taken (alternate degree, alternate NPC choice, alternate trigger),
## and traces the emergent consequences forward.
## Scenarios are labeled with their branch origin and the alternate decision taken.

---

## COUNTERFACTUAL TAXONOMY

Each scenario in this batch follows the form:
> **BRANCH FROM:** [Original scenario] | **ALTERNATE PATH:** [What changed] | **QUESTION:** [What emerges?]

Branch types used:
- **DEGREE INVERSION:** the roll succeeded where we assumed failure, or vice versa
- **NPC CHOICE FORK:** NPC took Option B where we assumed Option A
- **TRIGGER TIMING:** a clock or condition that fired differently
- **PLAYER CHOICE FORK:** player chose the path explicitly not modeled

---

## CATEGORY BA: EDEYJA ARC A — NO EXPEDITION ARRIVES

---

### NEW-S92: EDEYJA ARC A PERSISTS × WARDEN SOLO ENDURANCE × RS TERMINAL DECLINE

```
BRANCH FROM: NEW-S38 (Edeyja Arc B — Collaboration Unlock)
ALTERNATE PATH: No player expedition reaches Southernmost. Arc A holds: "No PC expedition 
               reaches Askeheim. Wardens continue alone. RS decline accelerates."
QUESTION: What does the campaign look like when Edeyja is never reached?

ROOT STATE: Edeyja Arc A (Default, unchanged). Warden Cooperation Track: 0.
            RS starting: 28. Passive decline: −5 to −7/season (winter + Locks + gaps).
            Edeyja alone: Mending Ob 5-7, Coherence 9 starting.

WARDEN SOLO MENDING ARITHMETIC:
│
├─ EDEYJA'S SOLO MENDING CAPACITY:
│   Pool: Spirit (high, assume 5) × 2 = 10 + History (Warden Seniority, assume +3) + TPS (7) = 20 dice
│   TN 7, Mending Ob 5 (Standard Gap) or Ob 7 (Catastrophic Gap at RS critical)
│   Success rate at Ob 5: ~90% → RS +1 to +2 per season (Mending success)
│   Coherence cost: −1 per Mending regardless of outcome
│   From Coherence 9: 9 seasons of solo Mending before Rendering Crisis
│   ARC-S34 (Edeyja Burnout): ~10 Mendings before Coherence 2 → at Coherence ≤ 5, TE-15 
│   (Structural Dissolution of catastrophic Gap emergent) drives her to Rendering Crisis regardless
│
├─ RS TRAJECTORY WITHOUT EXPEDITION:
│   Season 1-3: Edeyja Mends solo. RS 28 → 30 (gains +1-2 from each Mending, losing −5-7 from decay)
│   Net: −3 to −5/season even with active solo Mending
│   Season 6: RS 28 − (4/season × 6) = RS 4 (Critical band, approaching 0)
│   Season 7: RS 0 — THE RUPTURE
│   The world ends in approximately Season 7 without player intervention in the Southernmost
│
├─ THE ACCELERATOR: EDEYJA'S COHERENCE COLLAPSE
│   At Season 5 (Coherence 4 from solo work): Fragmented state → +1 Ob ALL Thread operations
│   Mending Ob 5 becomes Ob 6 → success rate drops from ~90% to ~70%
│   At Season 6 (Coherence 2): Fractured → +2 Ob → Mending Ob 7 → success rate ~40%
│   Her degrading Coherence accelerates RS decline exactly when it matters most
│   ARC-S34 confirms: "these two vectors feed into the same terminal condition"
│   → Edeyja's burnout and RS Critical are designed to converge simultaneously
│
├─ WHAT ARC A ACTUALLY LOOKS LIKE AT THE TABLE:
│   The player is managing the other campaign systems (TC suppression, Torben, Parliament)
│   RS decline is visible only through Calamity Radiation effects:
│   Season 3: T6 and T13 "minor instability" (Shifting Objects, Thread ops +1 Ob)
│   Season 4: T5 and T12 begin Folklore (strange happenings, no mechanical effect yet)
│   Season 5: T1 Valorsplatz begins minor instability (Shifting Objects 10% chance, Thread ops +1 Ob in the capital)
│   Season 6: Critical band — all territories Stability checks Ob 1; Mandate −1 on failure
│   → The political systems that the player has been managing begin failing simultaneously from RS Critical
│
├─ FACTION COLLAPSE CASCADE AT RS CRITICAL:
│   Seasonal Stability checks: each faction at Mandate floor risk
│   Church Mandate −1 (from Stability check failure): TC Conviction Yield falls (Mandate < Church Mandate requirement fails)
│   Crown Mandate −1: Coup Counter could tick from this alone (Crown loses territory without military response)
│   Hafenmark Mandate −1: PI rises (faction Mandate below 3 → PI +1/season)
│   → All clock systems the player has managed accelerate simultaneously from a cause external to all of them
│
└─ THE ARC A LESSON:
    The campaign's political systems are parasitic on RS. They appear independent — TC, IP, PI, Coup Counter —
    but they are all consuming the same substrate.
    When RS hits Critical, the substrate fails, and the political systems crash together.
    The player who spent 6 seasons winning the political game discovers that the game
    was always downstream of a systems-level fight they weren't having.
    ARC A is not a failure state — it is the design's demonstration of what the game is actually about.
    The player who arrives at Season 6 having won Parliament, suppressed TC, managed Torben,
    and lost the world has received the game's central argument.
```

**What the alternate branch reveals:** Arc A isn't a background condition that never changes — it's a 7-season countdown that produces the campaign's most clarifying moment: all the political work was preserving conditions for a world that was dying underneath it. The Southernmost is not a sidequest.

---

## CATEGORY BB: HAELGRUND NEVER LEARNS HIS TS

---

### NEW-S93: HAELGRUND TS 12 — DIAGNOSIS FAILS × INVESTIGATION COMPLETES × PARLIAMENTARY RECORD PARADOX

```
BRANCH FROM: NEW-S74 (Haelgrund TS 12 Diagnosis × Defection Cascade)
ALTERNATE PATH: Player FAILS the Diagnosis roll (Cognition vs Ob 2 — ~75% success rate, 
               so ~25% failure). Haelgrund's TS is not revealed. He completes his 
               investigation at Overwhelming (PROCEDURALIST flaw).
QUESTION: What does a fully intact, non-defecting Haelgrund produce?

HAELGRUND COMPLETES THE INVESTIGATION (OVERWHELMING RESULT):
│
├─ THE PROCEDURALIST OVERWHELMING:
│   Haelgrund's investigation of player practitioner (or Thread event in T9):
│   Resolves at Overwhelming — enters Parliamentary record regardless of Church preference
│   Contents: documented Thread activity, practitioner identification, evidence of Thread perception
│   But the investigation ALSO documents HOW Haelgrund found the evidence:
│   His "hunch" led him to a specific street, a specific timing, a specific person
│   Parliamentary record: "[Date], Cardinal Haelgrund identified the practitioner's location through intuitive assessment of Thread-adjacent environmental patterns"
│   → "Intuitive assessment of Thread-adjacent environmental patterns" is a DESCRIPTION OF THREAD PERCEPTION
│   → Klapp (CE 4, TS 31, encounters archive material) reads this entry
│   → Klapp: "He sensed the Thread. He used it and didn't know it."
│
├─ KLAPP'S RECOGNITION:
│   Klapp TS 31 has encountered originary Locks (if ARC-S08 has been running)
│   He recognizes Thread perception in a colleague's description of their "investigative instinct"
│   This is the Klapp Threshold (ARC-S21) trigger: "encounters a Thread-significant object or event"
│   A Parliamentary record entry describing implicit Thread perception = Thread-significant event
│   Spirit TN 7 Ob 2 check for Klapp: ~34% → Klapp converts
│   → Haelgrund's own Overwhelming investigation becomes the object that converts Klapp
│   → Haelgrund never defects; Klapp converts from reading Haelgrund's work
│
├─ COLLISION A WITHOUT HAELGRUND DEFECTION:
│   Klapp conversion: Church Stability −3; TC generation pauses (Cardinals competing)
│   Haelgrund: still Church; still Inquisitor; now investigating the practitioner more intensively
│   → Haelgrund is conducting a Heresy Investigation against the player WITH an Overwhelming Parliamentary record
│   → The investigation result is already in the record — Haelgrund now moves to Excommunication
│   → But Church Stability is −3 from Klapp's conversion: Stability check Ob 1 for further actions
│   → Church may be too internally fractured to execute the Excommunication it has just legally established
│
├─ THE CHURCH PARALYSIS SCENARIO:
│   Haelgrund (Church): wants to Excommunicate the player (legal basis: Parliamentary record)
│   Himlensendt: must authorize (Faith conviction: yes, this is correct)
│   Klapp (now fractured): refuses to participate in Excommunication proceedings (his conversion prevents it)
│   Fortitude Cardinal: wants military response regardless
│   → The Church has: a legally established Heresy case, a paralyzed institutional process, 
│     a fracturing internal politics, and Haelgrund as the only functional Inquisitor
│   → Haelgrund prosecutes alone — without the institutional weight that made him effective
│   → Solo Haelgrund Excommunication attempt: Church Mandate vs Ob 7 (player's standing)
│   → At Church Mandate 5 (post-Stability crisis): 5 dice vs Ob 7 TN 7 → ~8% success
│   → The most legally supported Heresy case in the campaign has an 8% success rate
│     because the institution that produced the case has collapsed around it
│
└─ THE INFORMATION STATE:
    Player knows: Haelgrund has an Overwhelming investigation result about them in Parliamentary record
    Player does NOT know: Haelgrund doesn't know his own TS
    Player CANNOT know: whether Klapp has converted (different arc)
    Haelgrund knows: the practitioner's identity, location, activities
    Haelgrund does NOT know: that his investigation method documented his own Thread sensitivity
    Klapp knows: that Haelgrund has Thread Sensitivity (from reading the record)
    Klapp does NOT know: that Haelgrund doesn't know this
    → The information asymmetry produces a political landscape where everyone has
      critical partial knowledge and no one has complete knowledge
    → This is the Valoria design's information architecture at its most elegant:
      three NPCs, three distinct knowledge states, all from one Parliamentary record entry
```

**What the alternate branch reveals:** Haelgrund not defecting doesn't protect the Church — it produces a worse outcome through a different mechanism. The PROCEDURALIST flaw ensures the evidence enters the record regardless, and the record becomes the Klapp trigger. The defection path removes the Church's best Inquisitor; the non-defection path collapses the Church's institutional coherence while leaving the Inquisitor intact and pursuing.

---

## CATEGORY BC: CONSECRATION REFUSED — BARALTA UNCONSECRATED

---

### NEW-S94: CONSECRATION CRISIS — REFUSAL PATH × 3-SEASON PERFORMANCE WINDOW × MANDATE ARITHMETIC

```
BRANCH FROM: NEW-S54 (Baralta Crown Claim × Consecration Crisis × Himlensendt Arc Timing)
ALTERNATE PATH: Church Stability ≥ 4 at Succession Contest (rather than ≤ 3).
               Himlensendt REFUSES consecration. Baralta rules unconsecrated.
QUESTION: Can Baralta survive the 3-season performance window with Mandate 1?

CONSECRATION REFUSED — INITIAL STATE:
│
├─ THE MANDATE ARITHMETIC AT REFUSAL:
│   Crown Mandate before succession: likely 1-2 (that's what triggered the contest)
│   Unconsecrated penalty: Crown Mandate inherited at −2
│   If Crown Mandate was 2: Baralta inherits Mandate 0 → eliminated immediately (floor 0)
│   If Crown Mandate was 3: Baralta inherits Mandate 1
│   → The only viable refusal path: Crown Mandate was exactly 3 at succession contest
│   → Baralta rules as Crown with Mandate 1 (constitutional legitimacy via deed-claim, no theological blessing)
│
├─ THE 3-SEASON PERFORMANCE WINDOW:
│   Rule: "if Baralta governs successfully for 3 consecutive seasons without Church consecration
│          (Mandate does not drop below 3): deed-logic is validated"
│   But she STARTS at Mandate 1. She must reach Mandate 3 within 3 seasons.
│   Institutional Consolidation (clean season, no Triggers 1-5): +1 Mandate
│   Season 1: no hostile actions → Mandate 1 → 2 (one clean season needed)
│   Season 2: no hostile actions → Mandate 2 → 3 (second clean season)
│   Season 3: Mandate 3 sustained → performance window satisfied
│   Required: 3 consecutive absolutely clean seasons (no Trigger 1-5 events against Crown)
│
├─ WHAT MAKES A SEASON NOT CLEAN (TRIGGER CONDITIONS):
│   Trigger 1: another faction's Military action in a Crown territory
│   Trigger 2: Crown Mandate drops below 3 at Accounting
│   Trigger 3: Torben Loyalty below 4 AND no Covert Contact this season
│   Trigger 4: Major Subterfuge exposed in Crown territory
│   Trigger 5: Church Seizure attempt in a Crown territory
│   → TC +3 from the refusal: at TC 31, Church Priority 3 fires → Assert → TC +1/season
│   → At TC 40: Coup Counter +1 (Trigger 1 equivalent — institutional pressure registers)
│   → Ehrenwall's Coup Counter: already at 1-2 (that's what weakened Crown Mandate to 3)
│   → Coup Counter reaching 3 at Season 2 of the performance window: Martial Law fires
│   → Baralta cannot get 3 clean seasons because the Coup Counter is already primed
│
├─ THE VIABLE PATH (IF ANY):
│   Player at Standing 4 (Lieutenant) in Crown-Baralta's administration:
│   Must simultaneously: manage Coup Counter (Torben contact, prevent territory loss),
│   suppress TC (Hafenmark Parliamentary Suppress, Varfell Cultural Reclamation),
│   prevent Church Seizure attempts (TC below 60, Hafenmark Structural Suppression)
│   → All three TC management mechanisms must remain operative WHILE Baralta's Mandate is building
│   → But Baralta is Crown now, not Hafenmark
│   → Does Hafenmark Structural Suppression (Baralta's Mandate ≥ 4) continue when she's Crown at Mandate 1?
│   → (NEW-OI-31 directly relevant): if suppression follows the PERSON → it's gone (Mandate 1 < 4)
│   → If it follows the faction → it's gone (she's no longer Hafenmark leader)
│   → Either way: TC suppression brake is removed at exactly the moment she needs 3 clean seasons
│
├─ MOST LIKELY OUTCOME:
│   Season 1: Crown-Baralta Mandate 1 → 2 (barely clean)
│   Season 2: TC hits 40 → Coup Counter +1 → at 3 → Martial Law fires
│   → Baralta's unconsecrated reign lasts 2 seasons before the Coup Counter terminates it
│   → Löwenritter takes over → new Succession Contest fires
│   → Baralta is now excluded from this contest (deed-claim rebutted by performance failure)
│   → The path that seemed like Hafenmark's victory produces a Löwenritter takeover
│
└─ THE NARRATIVE IRONY:
    Baralta pursued the Crown for decades, building the strongest constitutional deed-claim on the peninsula
    She won the Succession Contest — the rarest achievement in the game
    Himlensendt's refusal (which requires him to be at Stability ≥ 4, meaning the player FAILED to weaken him)
    produces a 2-season unconsecrated reign that collapses from the same mechanisms
    that produced the succession contest in the first place
    The player who failed to weaken the Church before claiming the Crown
    discovers that the Church doesn't need to do anything further — its prior strength is sufficient
    to destroy what it refused to bless
```

**What the alternate branch reveals:** The consecration refusal path is not just "harder" — it's almost certainly a route to faction elimination given the Coup Counter state that necessarily precedes the Succession Contest. The design correctly makes mid-game Church Stability reduction the prerequisite for successful Crown claim. Jumping to the claim without completing the prerequisite produces the most ironic loss in the game.

---

## CATEGORY BD: VAYNARD'S WALK — FORGETTING FAILURE AT CORE

---

### NEW-S95: PATH B DEED 2 FAILURE × VAYNARD FORGETS THE CORE × TK STAGNATION × PRIVATE COLLECTION OFFER ABORTS

```
BRANCH FROM: NEW-S55 (Varfell Path B Deed 2 — Vaynard's Walk × Forgetting Mechanism)
ALTERNATE PATH: Vaynard's Forgetting Check at Core FAILS (Failure degree — "nothing operational").
               No player was present to Thread-stabilize. Deed 2 is not completed.
QUESTION: What happens to Vaynard (and the Private Collection) after a Core Forgetting Failure?

VAYNARD RETURNS FROM SOUTHERNMOST — CORE FAILURE STATE:
│
├─ WHAT VAYNARD REMEMBERS:
│   Failure degree: "Nothing operational. The character knows they were in a strange place and feels affected;
│   cannot report anything actionable."
│   Vaynard remembers: he went south. He was in a place. He felt something. He cannot say what.
│   His TK: does not advance (the Forgetting erased the content of the experience before conversion)
│   VTM advancement from Deed 2: NOT awarded (Deed 2 not completed = VTM stays at 3)
│   The Expedition itself cost: multiple seasons, faction resources, Warden Cooperation build-up
│
├─ VAYNARD'S CONSEQUENTIALIST RESPONSE:
│   Consequentialist Pragmatism: Vaynard's ethical framework
│   He failed. The failure is a data point. He updates.
│   His calculation: "The expedition produced no actionable knowledge. Cost: 2 seasons + resources.
│   The Forgetting mechanism is real and resistant to my current capability."
│   His next action: does NOT retry immediately (consequentialist — expected value is negative without
│   Thread-stabilization assistance he doesn't have)
│   His pivot: ACQUIRES Thread-stabilization assistance
│   → Private Collection OFFER: at TK 4, Vaynard offers the Collection including originary Locks
│   But: TK is still at 3 (Deed 2 failure means VTM stayed at 3, which means TK cap is 3)
│   Wait: VTM and TK are distinct tracks. TK is Vaynard's personal Thread Mastery.
│   VTM is the Path B victory condition track. The Forgetting failure means Deed 2 is not completed
│   but Vaynard's TK may have still advanced from the PRE-Core expedition experiences
│   → TK advances from: expedition approach, border zone exposure, inner zone encounters
│   → TK may reach 4 even without Deed 2 completion (if the non-Core expedition events provided insight)
│   → At TK 4: Vaynard's Private Collection offer is still available even with Deed 2 failure
│
├─ THE PRIVATE COLLECTION OFFER WITHOUT DEED 2:
│   Vaynard at TK 4 (from non-Core expedition content) + Deed 2 incomplete:
│   He DOES offer the Private Collection (TK 4 trigger, not Deed 2)
│   Lock Distribution decision: the player can still receive the originary Locks
│   But: Path B Deed 2 remains uncompleted → Path B victory is blocked
│   → The Lock Distribution and Path B are decoupled:
│   → Vaynard can give away his most powerful resource (the Locks) while still failing his victory path
│   → This is actually rational: the Locks become more valuable to him given externally now that 
│     he cannot use them himself (he needs Thread practitioners to assist his next Deed 2 attempt)
│
├─ VAYNARD'S DEAL:
│   "You have what I need. I have what you need."
│   Vaynard's offer: Private Collection (including Locks) → player gets Lock Distribution access
│   Player's required reciprocal: Thread-stabilization assistance on Deed 2 retry
│   → This is the most mechanically explicit exchange in the game:
│   a faction leader trades his highest-value asset for the player's specific capability
│   → Without this deal: Vaynard retries Deed 2 alone, fails again (8% success rate solo), fails again
│   → With this deal: player commits to accompany the next expedition
│   → The deal makes the Lock Distribution consequence sequence CONTINGENT on the expedition commitment
│   → If player takes the Locks and fails to assist the expedition: Vaynard is now hostile (Disposition −3, 
│     "you took what you needed and left me with nothing")
│   → Varfell priority tree shifts: the player becomes a direct threat (Priority 2: major subterfuge)
│
└─ VAYNARD UNCHECKED (NPC-ARC-VAY):
    If Vaynard NEVER completes Deed 2 (multiple failed attempts, no player assistance):
    At TK 5 (he accumulates slowly through other means): NPC-ARC-VAY fires
    "Vaynard's consequentialist urgency is unmoderated by safety awareness"
    He attempts an unsupported Askeheim expedition: TE-13 (WC −1) and TE-14 (non-practitioner force)
    He brings a military escort (TS < 30) → they dissolve on entry → force integrity check fails
    → Vaynard at the Core, alone, with a dissolved escort, no Thread-stabilization:
    Forgetting Check Failure again → no operational memory → but THIS time he's deep inside the Core
    His unsupported failure produces a Threadcut encounter (Mode 1: configuration without self-awareness)
    The Mode 1 entity is not hostile by default — but Vaynard, unable to perceive it, blunders through its territory
    → The entity responds → Vaynard is incapacitated in the Core, deep Forgetting, no escort
    → His survival depends entirely on Wardens finding him (Priority 5: assess any new practitioner in Southernmost)
    Warden Cooperation Track if no expedition has reached them: WC 0 → no cooperation → no assessment
    → Vaynard does not return
    → NPC-ARC-ULN fires: Maret Uln takes Varfell leadership → VTM resets to 0
    → The path to Varfell Path B is closed permanently
```

**What the alternate branch reveals:** A solo Deed 2 failure doesn't end Path B — it creates a negotiated dependency between Vaynard and the player that makes the Lock Distribution deal contingent on expedition commitment. The deal is the design's most explicit expression of mutual resource dependency. But if the player never assists: Vaynard's TK 5 urgency produces the terminal Southernmost scenario, Maret Uln succession fires, and Varfell's Thread program collapses permanently.

---

## CATEGORY BE: RM CULTURAL UPRISING FAILURE

---

### NEW-S96: RM PHASE 2 ROLL FAILS × TC +2 × T9 CULTURAL REVERSAL × CHURCH DOUBLE CONSOLIDATION

```
BRANCH FROM: Implicit in NEW-S67 (Southernmost Military Restriction × RM Phase 2) and victory_v30 §3.5
ALTERNATE PATH: The Phase 2 Cultural Uprising of T9 Himmelenger roll FAILS.
               "Uprising crushed. TC +2. T9 PT +1. Uprising attempt used up for this arc."
QUESTION: What follows a failed Phase 2 — is the RM path closed, and what does TC +2 at this stage cost?

CULTURAL UPRISING FAILURE — IMMEDIATE STATE:
│
├─ TC +2 AT PHASE 2 TIMING:
│   Phase 2 fires only while Phase 1 holds: ≥ 4 territories at PT ≤ 1
│   Phase 2 can only be declared while RS ≥ 25 (substrate must be stable)
│   This timing implies: RS is under control (player has invested in RS recovery)
│   TC at Phase 2 timing: likely 40-60 (TC has been suppressed, but Phase 2 requires sustained RM position)
│   TC +2: moves TC from ~50 to ~52 (if in that range)
│   At TC 60: Seizure Ob formula activates (Church Seizure Pool = Influence + floor(60/15) = Influence +4)
│   → TC +2 doesn't immediately trigger seizure but meaningfully increases Church's seizure capability
│
├─ T9 PT +1 — THE CULTURAL REVERSAL:
│   T9 started at PT 5 (Piety pole). RM's Phase 1 required PT ≤ 1 in 4+ territories.
│   For Phase 2 to be viable: T9 PT must have been reduced (≤ 1 required for the Ob −1 bonus)
│   Failure result: T9 PT +1 — it's still low but moving back toward Church dominance
│   Crushing the Uprising: Church frames it as "heresy defeated at the Cathedral"
│   Institutional confidence: "No external challenge for 2 consecutive seasons" → Influence +1 (Framework Drift)
│   → Church gains Influence +1 from the Uprising failure the following season
│   → Plus TC +2 from the failure itself
│   → The Uprising attempt has improved Church's position on two tracks simultaneously
│
├─ "UPRISING ATTEMPT USED UP":
│   The Phase 2 Uprising is explicitly one-shot: "Uprising attempt used up for this arc"
│   Phase 1 remains (if conditions still hold): ≥ 4 territories at PT ≤ 1
│   But Phase 2 cannot be re-attempted until conditions reset
│   What resets the attempt? The document doesn't specify a recovery path
│   [GAP]: Is the Uprising attempt permanently expended per campaign arc, or per season?
│   If permanently expended: RM can never again attempt the Cultural Uprising → RM victory is closed
│   If per-season: Phase 2 can be re-attempted next season if Phase 1 still holds
│   The word "arc" (not "season") suggests permanent within the campaign arc
│   → RM's only path to Phase 2 victory is permanently closed by a failed roll
│
├─ RM'S POSITION AFTER FAILURE:
│   Phase 1 may still hold (territories still at low PT)
│   RM Stability: unchanged (failure didn't crash Stability in itself)
│   RM Presence markers: intact (Vossen's wide-shallow network is structurally durable)
│   But: the political moment has passed
│   Every faction saw the Uprising fail — RM is not a viable king-maker
│   Varfell + RM co-victory: still mechanically available (different victory path, no Uprising required)
│   → The most interesting post-failure position: RM shifts from solo victory pursuit to co-victory support
│   → Varfell + RM conditions: VTM ≥ 3, WR ≥ 2, ≥ 3 territories PT ≤ 1, RS ≥ 40, Varfell controls T13
│   → All conditions plausible if Phase 1 still holds
│   → The Uprising failure becomes the moment RM leadership (Vossen) recognizes:
│     "We cannot take T9 by popular movement. We need Varfell's institutional reach."
│
└─ HIMLENSENDT'S RESPONSE TO THE FAILED UPRISING:
    His Faith Conviction: the Uprising's failure is theological confirmation
    "The people of Himmelenger chose the Church. This is what the substrate knows."
    BUT: he is using Evidence Resonant Style — and the evidence is:
    T9 PT was reduced to near-restoration levels before the Uprising attempt
    That reduction happened. The Uprising failed. But the substrate had been genuinely shifted.
    Himlensendt's evidence-reading framework must account for: why was T9 PT ≤ 1 before the Uprising?
    → The evidence of prior success contradicts the evidence of current failure
    → This is a Conviction Wound setup if a player approaches him with this exact argument
    → "Your faith is correct today. But where was your faith three seasons ago when this city was
       almost gone from orthodoxy?" → Conviction strain without invalidating today's outcome
    → The failed Uprising creates a window for targeted Faith challenge that wouldn't exist at full TC/PT
```

**What the alternate branch reveals:** The Uprising failure is devastating for RM's solo path but doesn't close all paths — it redirects RM toward the Varfell co-victory track, which is mechanically available and doesn't require the Uprising. The TC +2 and Church Influence +1 from the failed Uprising also create a tighter timeline for any remaining player interventions. And the reduced-then-restored PT trajectory creates a specific window for a Conviction challenge against Himlensendt.

---

## CATEGORY BF: TORSVALD DOESN'T ABORT — THE 70% PATH

---

### NEW-S97: TORSVALD PROCEEDS IN THREAD-ACTIVE TERRITORY × RISKBREAKER COLLATERAL × COHERENCE CONTAGION

```
BRANCH FROM: NEW-S76 (Torsvald 30% Abort Rate × Deniability Debt × Pattern Detection)
ALTERNATE PATH: The d10 roll is 4+ (the 70% non-abort result fires). Torsvald proceeds 
               with the Riskbreaker operation in T6 Stillhelm (RS Fractured, Thread-active).
QUESTION: What happens when a TS 35 Riskbreaker executes an operation in a Thread-active zone?

TORSVALD PROCEEDS — OPERATION IN RS FRACTURED T6:
│
├─ WHAT TORSVALD PERCEIVES DURING OPERATION:
│   TS 35: "Senses an operation in the scene; general direction identifiable" (observation table)
│   T6 Stillhelm at RS Fractured (39-20): Spontaneous Shifting Objects (1/season automatic)
│   During the operation: a Shifting Object manifests in the safehouse Torsvald is using
│   This is not a Thread OPERATION by any practitioner — it's an environmental effect
│   Torsvald (TS 35) perceives it fully: Shifting Object configuration, approximate scale, direction
│   Her mission target: a Niflhel contact she's meant to compromise
│   The Shifting Object: it's the contact's personal Thread configuration beginning to destabilize
│     (their Object-scale Thread is oscillating — Object/Personal level Shifting Object)
│   → Torsvald perceives the contact's Thread configuration becoming unstable
│   → She doesn't know what to do with this information
│   → Her tradecraft says: complete the mission, extract the intel
│   → Her TS says: the contact is about to experience a Thread event
│
├─ THE OPERATION PRODUCES THREAD COLLATERAL:
│   Torsvald extracts the contact (successful intelligence operation)
│   The contact's Thread destabilization: triggers a Discovery Event check for the contact
│   Contact (non-practitioner, TS unknown — probably 0-5): Spirit TN 7 Ob 1 → low % chance
│   If contact has TS 10+ (possible: they're in Niflhel, Thread-adjacent territory):
│   Discovery Event fires → TS advances → contact is now a Thread-sensitive Niflhel operative
│   → Torsvald's intelligence extraction has inadvertently produced a practitioner within Niflhel
│   → This is Thread collateral: she created what she was afraid of creating
│
├─ DENIABILITY DEBT: 0 (OPERATION SUCCEEDED — NO ABORT EVIDENCE):
│   When Torsvald completes the operation: Deniability Debt does NOT accumulate
│   The abort trail that produces Debt only appears when she withdraws without completion
│   Successful completion leaves less trace than an abort
│   → Counterintuitively: Torsvald proceeding produces less institutional detection risk than aborting
│   → But it produces Thread collateral risk that aborting would have avoided
│   → The abort rate is not protecting the Löwenritter from detection — it's protecting the substrate
│
├─ TORSVALD'S INTERNAL STATE AFTER COMPLETION:
│   She knows she proceeded despite Thread collateral assessment
│   She knows the contact showed signs of Thread destabilization during extraction
│   She files the report: mission successful, no complications (she cannot mention Thread phenomena
│   in Riskbreaker reports — they are supposed not to exist)
│   Her suppressed report contains: what she observed, what she chose not to abort, 
│   what the contact's Thread state was
│   → This is the content of the ghost sheet if Torsvald is later killed or removed
│   → The suppressed observation record exists and contains information no one else has
│
└─ THE LONG-TERM THREAD CONTAMINATION WITHIN NIFLHEL:
    If the contact's Discovery Event fired (and they're now TS 30+):
    Niflhel has a Thread-sensitive operative who doesn't know their TS
    The Niflhel Social Toolkit (§5.8): Thread Insight (TS ≥ 30) = free Thread-Read before Negotiate/Read
    → This operative is now using Thread Insight without knowing it
    → Their intelligence quality improves dramatically (they perceive unstated positions)
    → Niflhel's four-arm network acquires an advantage they can't explain or replicate
    → If player investigates Niflhel: this operative's intelligence quality stands out
    → The investigation Trail: "this operative's intelligence is too accurate to be explained by tradecraft alone"
    → Diagnosis by player (Cognition vs Ob 2): reveals the TS → Niflhel Thread contamination exposed
    → Torsvald's one non-abort decision from months ago is the thread that unravels Niflhel's network
```

**What the alternate branch reveals:** When Torsvald doesn't abort, she doesn't create institutional detection risk (no Deniability Debt) but she does create Thread collateral — specifically, potentially converting a Niflhel operative into an unwitting practitioner. The successful operation is not "safe," just differently dangerous. The collateral consequence is traceable back to her decision months later through investigation quality anomaly detection.

---

## CATEGORY BG: LOCK DISTRIBUTION — MARET ULN RECEIVES ALL LOCKS

---

### NEW-S98: MARET ULN TS 70 × TEMPORAL WINDOW ACCESS × CONSEQUENTIALIST FACTION WITH POP

```
BRANCH FROM: NEW-S81 (Private Collection Distribution × Lock Cascade × Five-Practitioner Transformation)
ALTERNATE PATH: Player distributes ALL significant Locks to Maret Uln alone (Path 2 from NEW-S81:
               "Temporal Window Access — Varfell gains POP capability").
               Maret Uln reaches TS 70. Varfell holds the temporal window key.
QUESTION: What does a consequentialist faction do with Past-Oriented Pulling capability?

MARET ULN AT TS 70 — THE CONSEQUENTIALIST PRACTITIONER:
│
├─ WHAT TS 70 MEANS FOR MARET ULN:
│   TS 70+: Past-Oriented Pulling eligible (temporal window access)
│   FR eligibility: Lock and Dissolution now available
│   TPS: floor(70÷10) = 7 (highest TPS of any practitioner except Edeyja)
│   Her Lock from NPC-ARC-ULN succession: if Vaynard is still alive, she's his operative, not his heir
│   If Vaynard is eliminated post-Lock distribution: Maret Uln succession fires → VTM resets to 0
│   But: VTM is Vaynard's personal track — it doesn't transfer to Maret Uln as leader
│   → Maret Uln at TS 70 + Varfell leadership: Varfell shifts to Thread-governance faction (NEW-OI-25)
│   → VTM 0, but Maret Uln's TS 70 is MORE operationally powerful than Vaynard's TK track ever was
│
├─ THE CONSEQUENTIALIST POP AGENDA:
│   Consequentialist Pragmatism (Varfell's framework): maximize strategic information advantage
│   POP capability: access to Thread configurations in past states
│   Varfell's intelligence priority: "maximise information advantage" (Priority Tree Priority 4)
│   → What past events does Varfell most want to investigate via POP?
│
│   Option 1: 218 AG hunting accident (Crown Archives)
│   POP recency: 27 years → Ob 7 (generational scale)
│   Maret Uln pool: (Spirit × 2) + History + TPS 7 → assume ~16-18 dice vs Ob 7, TN 8
│   Success rate: ~30-40% (achievable)
│   Yield: irrefutable Thread evidence of the hunting accident circumstances
│   Strategic use: this information changes Almud's Belief 2 constraint (27 years of governance
│   shaped around nothing). If Varfell holds this: they control one of the most valuable political
│   revelations in the campaign. Almud's behavior changes; Crown-Varfell relations transform.
│
│   Option 2: Einhir Catastrophe (245 AG)
│   POP recency: 245 years → Ob 7 (generational, at maximum scale)
│   Additionally requires: Einhir Ritual Framework (separate prerequisite from TS 70)
│   Maret Uln without Einhir Framework: cannot target Foundational events
│   → Option 2 is blocked without Einhir Framework acquisition (which requires expeditions)
│
│   Option 3: Torben's pre-departure psychological state (1-2 seasons ago)
│   POP recency: 1-2 seasons → Ob 4
│   Maret Uln pool vs Ob 4, TN 8: ~80% success rate
│   Yield: Torben's Thread configuration at Loyalty 8 state → what would restore it
│   Strategic use: Varfell holds intelligence on HOW to restore Crown heir's Loyalty
│   → Varfell can sell this information to Crown (political leverage) or use it to manipulate
│     the succession crisis independently
│
├─ EDEYJA'S RESPONSE TO MARET ULN AT TS 70:
│   Edeyja (TS 75-80) can perceive Maret Uln's Thread operations at full resolution
│   (TS 70+: "Perceives the full configuration being worked")
│   Edeyja's Continuity conviction: Thread operations that serve factional agendas
│   → POP on the 218 AG hunting accident: a POLITICAL operation, not a Warden operation
│   → Edeyja detects this → generates a Demand scene against Maret Uln (or against the player
│     who enabled it via Lock distribution)
│   "The temporal window is not a political resource. Every use costs the substrate."
│   → Warden Cooperation Track consequence: TE-13 equivalent — if Maret Uln's POP operations
│     are perceived as non-Warden-aligned: WC −1
│
├─ MARET ULN'S DUAL LOYALTY COMPLICATION AT TS 70:
│   Her private Belief check (from RM sympathy): when ordered to act against RM
│   At TS 70: her Thread perception of RM communities is acute (she sees exactly what the
│   Forgetting is doing to Vossen's cultural knowledge, what the RS strain means for RM's base)
│   → Her RM sympathy is now reinforced by direct Thread observation
│   → Each Varfell intelligence operation against RM: private Belief check becomes harder to pass
│   → At some threshold (Spirit TN 7, cumulative Ob from repeated suppression): she fails
│   → She refuses a Varfell operation against RM → NPC-ARC-ULN: succession dynamics shift
│   → The practitioner with the temporal window may defect from the faction that holds it
│
└─ THE STRATEGIC LOCK ON TEMPORAL WINDOW INFORMATION:
    Maret Uln (TS 70, Thread evidence from POP, Varfell-aligned but wavering):
    She holds information obtained from temporal operations that no one else has
    If she defects to RM: she carries that intelligence with her
    → Varfell loses POP capability (she's the only TS 70 practitioner they have)
    → RM gains the most informed practitioner in the campaign
    → The Lock distribution decision that seemed like "give Varfell temporal access"
       becomes "potentially give RM temporal access if Maret Uln's dual loyalty resolves against Varfell"
    → The player who chose Path 2 in Lock Distribution has created the most volatile
       practitioner-intelligence situation in the game
```

**What the alternate branch reveals:** Maret Uln at TS 70 with Varfell is the campaign's most volatile configuration. Her consequentialist employer's agenda (218 AG investigation as political leverage) conflicts with Edeyja's Continuity conviction (temporal window is not a political resource) and her own RM sympathy (growing stronger at higher TS). The Lock Distribution "Path 2 — temporal window" is not giving Varfell the temporal window. It's creating a three-way conflict over who ultimately controls it.

---

## CATEGORY BH: PLAYER GENERAL DEFEATED — STAGE 1 → STAGE 2

---

### NEW-S99: BILATERAL COMBAT — PLAYER STAGE 1 INCAPACITATED × ARMY UNCOMMANDED × NPC GENERAL MERCY DECISION

```
BRANCH FROM: NEW-S66 (General Two-Stage Death × Bilateral Personal Combat × Command Collapse)
ALTERNATE PATH: Player LOSES the bilateral personal combat. Player general at Stage 1 
               (incapacitated). The NPC general has a 1-turn stabilize window.
QUESTION: Does the NPC general stabilize the player (mercy) or let Stage 2 fire (kill)?

PLAYER GENERAL STAGE 1 INCAPACITATED — THE NPC DECISION:
│
├─ THE 1-TURN STABILIZE WINDOW:
│   Stage 1: player general incapacitated → −1 Morale all player units, Command halved, Morale floor suspended
│   Stage 2 fires: "at start of following turn's Phase 5 if not stabilised"
│   Stabilise: Medicine Ob 2 in Phase 5 of the current turn (NPC must choose to attempt this)
│   Does the NPC general attempt to stabilize the player? This is an NPC behavioral decision.
│
├─ NPC DECISION TREE BY FACTION:
│   EHRENWALL (Löwenritter, TS 0, Certainty 5, Deed-logic framework):
│   Deed-logic: the player's deed-claim depends on survival and continued performance
│   Ehrenwall's evaluation: "A dead rival serves no political purpose. A captured rival serves several."
│   She stabilizes → player is captured → political prisoner
│   → Captured player: removed from campaign for negotiation seasons
│   → Löwenritter gains leverage over player's faction (hostage negotiation mechanic)
│
│   HIMLENSENDT (Church, Faith conviction, non-combatant):
│   Himlensendt would not be in personal combat — this branch requires a Church military general
│   Jarnstal (Cardinal of Fortitude): Martial Honour analog + Church tactical doctrine
│   Jarnstal lets Stage 2 fire → "Heresy ended at the battlefield. Church doctrine satisfied."
│   → Stage 2: player general killed. All player units Command = 0. Auto-rout.
│   → Domain Echo: player's faction Mandate −2 + NPC arc trigger
│
│   BRANDT (Löwenritter external-threat-fixated, if he has succeeded Ehrenwall):
│   Brandt evaluates: is this player a Valorian-defending asset or an obstacle?
│   If player was fighting Altonian-adjacent forces: Brandt is ambivalent (wrong enemy)
│   If player was fighting Brandt's defensive priority: Brandt respects the fight and stabilizes
│   Brandt's EXTERNAL THREAT FIXATED flaw: he assesses the player's threat to Altonian defense
│   → If player would redirect resources away from border defense: Brandt lets Stage 2 fire
│   → If player would support border defense: Brandt stabilizes (the fight was unnecessary; neither should die for internal politics)
│
├─ PLAYER STAGE 2 FIRES (THE NPC CHOSE NOT TO STABILIZE):
│   Player general killed → Stage 2 effects:
│   −2 Morale (outside cap), Command = 0, all units uncommanded
│   All player units: PP-273 floor (1D minimum), Line formation, no tactics
│   → Army effectively destroyed as a coherent force (it fights but cannot win)
│   Faction consequences:
│   Military −1 (unit destroyed: Rule from §A.13 confirmed, Command-EDIT-02)
│   Stability check Ob 2 (Campaign-scale defeat)
│   Mandate −1 (Stability check failure)
│
├─ THE PLAYER CHARACTER IS THE GENERAL — SPECIAL CASE:
│   Player character death: campaign event
│   Campaign modes v30 §12.1 TTRPG Endgame: "At least one Player Character has died" = endgame indicator
│   But: player character death is not an endgame trigger — it's a significant campaign event
│   "The succession crisis has resolved" and "died" are listed together as indicators of endgame readiness
│   → Player character general death: campaign continues, but the character's arc is complete
│   → Ghost sheet generated immediately (Grief-Driven Focus mechanic if any NPC was Knotted to player)
│   → Companion NPCs who were Knotted: Knot becomes dormant → Coherence recovery path blocked for them
│   → Settlement governors the player assigned: governor status unchanged (they continue)
│   → Evidence Track investigations the player was running: persist (knowledge is in notes/allies)
│   → The player character is dead; the campaign is not
│
└─ THE MERCY AFTERMATH (IF EHRENWALL STABILIZES):
    Player captured: removed from active play for negotiation
    Löwenritter holds: player's faction Standing, player's relationship with all NPCs, player's investigations
    Ransom negotiation: Faction Mandate vs Ob = Löwenritter Military ÷ 2 + 1 → Ob 4 (if Military 5)
    Success: player returned, faction pays resource cost
    Failure: player remains captured; Ehrenwall's leverage grows
    While captured: the player can attempt to build Disposition with Ehrenwall in captivity
    → Captured player + Ehrenwall Disposition building = the most unusual relationship arc in the game
    → She respects the fight; she took the mercy option; she didn't have to
    → Relationship built under captivity carries specific Authority Resonant Style weight
    → "Competence witnessed" in the bilateral combat → Authority approach now accessible
    → Almud Arc B's dual deadlock (NEW-S42): resolved in captivity by the person who captured them
```

**What the alternate branch reveals:** The NPC mercy-or-kill decision is fully determined by each general's behavioral AI — not a random roll. Ehrenwall's deed-logic favors capture (political asset); Jarnstal's Church doctrine favors death (heresy ended); Brandt's external-threat assessment produces context-dependent mercy. The captured player scenario produces the most unusual relationship-building context in the game: building Disposition with the NPC who just defeated and spared them.

---

## CATEGORY BI: N-WAY COLLAPSE AT STRUCTURAL SCALE

---

### NEW-S100: HIMMELENGER LATTICE COLLAPSE — STRUCTURAL SCALE GAP × RS −12 × PENINSULA-WIDE CONSEQUENCES

```
BRANCH FROM: NEW-S50 (N-Way Opposing Operations × Collective Collapse × Political Aftermath)
ALTERNATE PATH: The Himmelenger Cathedral configuration was STRUCTURAL scale (not Territorial).
               The originary Lock is a Structural-scale configuration — the theological architecture
               of Solmundic Orthodoxy itself, not just the Cathedral's territory.
QUESTION: What does a Structural-scale N-Way lattice collapse produce?

STRUCTURAL LATTICE COLLAPSE — SCALE ASSESSMENT:
│
├─ WHY THE LOCK COULD BE STRUCTURAL SCALE:
│   Originary Locks in the Private Collection: Locks on "institutional records, political threads,
│   Locked Zone borders, NPC arrangements" per threadwork §2.5
│   A Lock on "the theological architecture of Solmundic Orthodoxy" = Foundational/Structural scale
│   (It is a Structural configuration: it governs how a civilization renders religious reality)
│   This is not the Cathedral building (Territorial) — it's the theological FRAMEWORK (Structural)
│   → N-Way at Structural scale: all operations fail, Gap forms at Structural scale
│   → RS: −(2 × 3 practitioners) = −6 (same formula)
│   → But the DEGREE TABLE for FR Both-Fail at Structural scale: RS additional −5 (§2.6 FR vs FR table)
│   → Total RS cost for Structural N-Way collapse: −6 (base) − 5 (Structural FR) = −11 to −12
│
├─ A STRUCTURAL GAP:
│   What IS a Structural Gap? The gap table in threadwork describes Gaps by severity:
│   Catastrophic Gap (3+ seasons, Ob 7+ to Mend): the most severe NAMED category
│   Structural Gap would exceed this: "Structural-scale tear in the rendered framework"
│   → It is the rendering failure of a civilization-organizing principle, not a territory
│   → The effects radiate to ALL territories simultaneously (Structural = universal)
│   → RS −11 to −12 immediately: RS 28 − 12 = RS 16 (Critical band, approaching Rupture)
│   → This is the largest single RS event possible outside the Rupture itself
│
├─ THE STRUCTURAL GAP'S EFFECTS:
│   Standard Critical band effects apply IMMEDIATELY (not at next Accounting):
│   The threshold event fires on formation, not after the season ends
│   → All faction Stability checks Ob 1: at RS 16, simultaneous across the peninsula
│   → Multiple factions fail → Mandate −1 simultaneously → PI accumulates from multiple drops
│   → T9 Himmelenger: Cathedral sits above the structural tear → Consecrated status at risk
│   → The Church's institutional authority is literally rendering differently: non-practitioners
│     in T9 experience "objects in wrong places, déjà vu, inconsistent memories" immediately
│   → Every Church ceremony happening in T9 when the Gap forms: the theological substrate fails
│     mid-ceremony → what does a Mass look like when rendering fails during it?
│
├─ THE MENDING ARITHMETIC FOR A STRUCTURAL GAP:
│   Mending Ob for Structural Gap: beyond the existing Ob table
│   Extrapolating from Catastrophic Gap (Ob 7, requires Einhir framework):
│   Structural Gap would be Ob 8-9 minimum (beyond Locked Zone border requirements)
│   Edeyja's pool (Spirit ~5, History +3, TPS 7) = ~20 dice vs Ob 8-9, TN 7
│   Success rate: ~15-25%
│   And: the ×3 RS multiplier for mass battle Thread is not the same as Structural Gap;
│   but the Structural Gap itself is already at the mass-battle-scale consequence level
│   → Edeyja alone: ~15-25% chance per attempt at enormous personal Coherence cost
│   → Collective Mending (all three N-Way practitioners + Edeyja as Anchor):
│   Even the Lattice of Enemies pre-Leap check would need to clear → requires Belief compatibility
│   → Four practitioners with directly opposing Beliefs (they JUST tried to oppose each other):
│     64% chance the collective won't assemble (abort rate from §3.3 calculation)
│   → The people who caused the collapse cannot easily cooperate to repair it
│
└─ THE POLITICAL CONSEQUENCE OF STRUCTURAL GAP AT T9:
    Every faction's victory condition involves T9 or passes through it:
    Church Primary Victory: TCV ≥ 8, PT ≥ 3 in all held territories — T9 is their capital
    Hafenmark Alternate (Dynastic Assertion): requires Crown Mandate ≤ 3 + control T1 — T9 is adjacent
    Crown + Varfell co-victory: RS ≥ 50 — Structural Gap at RS 16 makes this nearly impossible
    RM Phase 2: Cultural Uprising of T9 — the target is now a Structural Gap site
    → A Structural Gap in T9 doesn't just damage one faction's victory path — it damages ALL of them
    → The N-Way practitioners who caused the collapse have collectively produced the condition
      that makes every faction's victory harder simultaneously
    → The only faction that potentially benefits: RM (T9 PT would shift dramatically from a Structural Gap)
    → The Structural Gap in the theological framework of Solmundic Orthodoxy is the end of the Church
      as a governing institution — not through political defeat but through ontological failure
    → Himlensendt: his Faith Conviction is challenged by the best possible evidence
      (his own institution's theological substrate is rendering incorrectly)
    → This is the most likely trigger for Himlensendt Arc B (Crisis of Faith) from any source
```

**What the alternate branch reveals:** The Structural vs Territorial scale distinction for the N-Way collapse isn't just a magnitude difference — it's a category difference. A Structural Gap isn't a territory problem; it's a civilization-organizing-principle problem. The RS cost is near-campaign-ending. The Mending requirement exceeds any single practitioner. And the gap's effects radiate universally, simultaneously damaging every faction's victory conditions rather than just the Church's.

---

## CATEGORY BJ: STRAND DETECTED — CROWN COUNTER-INTEL SUCCESS

---

### NEW-S101: STRAND APPROACH DETECTED × COUNTER-INTEL FIRES × VARFELL ASSET EXPOSED × DIPLOMATIC CASCADE

```
BRANCH FROM: NEW-S75 (Strand Flattery Vulnerability × Multi-Faction Exploitation × Crown Brittleness)
ALTERNATE PATH: Crown runs counter-intelligence (Intel vs Ob 2 each season) and SUCCEEDS.
               Varfell's approach to Strand is detected before extraction completes.
QUESTION: What happens when Crown catches a rival approaching Strand?

DETECTION — CROWN COUNTER-INTEL SUCCESS:
│
├─ WHAT CROWN DETECTS:
│   Varfell Tribune Spy (or player-facilitated approach) targeting Strand
│   Counter-intelligence roll: Intel vs Ob 2 (per NPC-ARC-STR)
│   Crown Intel starting value: not specified in faction stats (factions_ttrpg doesn't list Intel for Crown)
│   Assuming Crown Intel ≈ 3 (moderate — they have the Riskbreaker delegation but limited independent capacity)
│   3 dice vs Ob 2 TN 7: ~57% success → roughly even odds each season
│   Detection: Crown knows WHICH faction is approaching AND that it's through Strand specifically
│
├─ THE DIPLOMATIC CONSEQUENCES:
│   Crown's legal options when a rival approaches a Crown minister:
│   Option A: File Parliamentary Casus Belli (Major Subterfuge trigger from Trigger 4)
│   → Casus Belli against Varfell: Crown may declare CB, which does what exactly?
│     (CB gives Crown legitimate grounds for military action without PI increase)
│   Option B: Leverage the information diplomatically
│   → "Varfell is trying to compromise our Lord Steward" → Parliamentary motion for censure
│   → Varfell Stability −1 (institutional embarrassment)
│   Option C: Use it as counter-intelligence
│   → Feed Strand false information to pass to Varfell → active deception operation
│   → Crown turns Strand into a disinformation channel
│
├─ OPTION C — THE DOUBLE-AGENT STRAND:
│   Crown knows Varfell is approaching Strand
│   Strand doesn't know Crown knows
│   Crown instructs Strand: continue meeting with Varfell contact, provide specific false information
│   Strand (OVERPERFORMER, UNCONDITIONAL WORLDVIEW): will do this enthusiastically and perfectly
│   → He genuinely believes he's serving Crown's interests by participating
│   → The false information: what does Crown want Varfell to believe?
│   Best option: false intel about Crown's military positioning or upcoming Domain Actions
│   Varfell (Intel-primary, consequentialist): acts on the false intel in their Priority Tree
│   → Varfell commits resources to counter a threat that doesn't exist
│   → Or: Varfell reveals a planned operation by responding to the false intel
│
├─ VARFELL'S DETECTION OF THE DECEPTION:
│   Vaynard (consequentialist, Intel ≥ 4): evaluates intelligence quality
│   If 3 consecutive Strand reports conflict with Tribune field intelligence: deception suspected
│   Varfell "Eagle Eyes" equivalent at TK 4: "intel quality assessment"
│   → Vaynard discovers Strand has been providing false information
│   → Varfell knows their Strand operation has been burned
│   → Private Collection: does Vaynard now consider offering it to Crown instead?
│   → Consequentialist calculation: "Crown caught our operation AND turned it against us.
│     Crown has demonstrated intelligence superiority in this domain. We should work with them, not against."
│   → The failed Strand operation becomes the basis for a Varfell-Crown intelligence alliance
│
└─ STRAND'S PSYCHOLOGICAL STATE AFTER THE DOUBLE-AGENT OPERATION:
    Strand participated in deceiving people who were treating him as a peer
    He was USED as a tool — which is what he feared becoming
    But: Crown trusted him with a counter-intelligence operation
    Crown's trust vs Varfell's peer-treatment: which does he value more?
    OVERPERFORMER flaw: he will not admit the discomfort — he will perform his way through it
    → His next vulnerability window: he's MORE susceptible to peer-treatment flattery after being used
    → A third faction (Church, Guilds) who doesn't know about the counter-intel operation
      and treats him as a genuine intellectual peer has dramatically lower Ob than before
    → The crown burned the Varfell approach; the Church or Guilds can now exploit the opening
      that Crown's counter-intelligence created
```

**What the alternate branch reveals:** Counter-intelligence success produces options beyond simple exposure. The Double-Agent Strand path is the most strategically interesting: using the detected approach to run active deception. The irony that Strand performs the deception most enthusiastically (because he believes it serves Crown) while simultaneously being most vulnerable to the next approach is consistent with his OVERPERFORMER psychology.

---

## CATEGORY BK: RENDERING CRISIS MID-EXPEDITION

---

### NEW-S102: COHERENCE 0 AT SOUTHERNMOST CORE × RENDERING CRISIS IN THE WOUND × WARDEN EMERGENCY RESPONSE

```
BRANCH FROM: NEW-S41 (Dissolution Residue × Rendering Crisis Risk) extended to Expedition context
ALTERNATE PATH: Player uses Dissolution Residue at the Southernmost Core (Coherence 4),
               operation fails, hits Coherence 0 in the Core Zone.
QUESTION: What does Rendering Crisis look like inside the most dangerous Thread site in the game?

COHERENCE 0 AT THE CORE — IMMEDIATE STATE:
│
├─ THE SEQUENCE THAT REACHES HERE:
│   Player at Coherence 4 (Fragmented) before Core zone entry — already degraded from expedition work
│   Core Zone: contact duration halved, Thread density saturates working space
│   Player uses Dissolution Residue (Potency 3) for a critical Core operation
│   Operation fails → Coherence: 4 − 1 (residue, cap-exempt) − 1 (Dissolution failure additional) = 2
│   Next operation (attempting to close the Structural Gap from the N-Way collapse): 
│   Coherence: 2 − 1 (Mending, always −1) = 1 (Severed)
│   At Severed: +2 Ob to ALL Thread operations including Leap
│   Mending Ob 7 + 2 (Severed) = Ob 9 → next attempt fails
│   Coherence: 1 − 1 (Mending failure additional) = 0 → RENDERING CRISIS
│
├─ RENDERING CRISIS AT THE CORE — WHAT THIS MEANS:
│   Rendering Crisis (§3.7): "Reality as commonly rendered is no longer accessible"
│   The practitioner's spooling is destabilised — their organic drawing-from-ground is compromised
│   Normal Rendering Crisis resolution: full season withdrawal, 3 Anchoring Scenes with Close Knots
│   But they are at the Southernmost Core: the most Thread-degraded location on the peninsula
│   The Core Zone effect for non-practitioners: "Spirit check Ob 2 per round of exposure, Certainty −1 on failure"
│   The PRACTITIONER is now at a Coherence state equivalent to a non-practitioner at threshold:
│   → The Core's effects on non-practitioners ARE the practitioner's Rendering Crisis effects
│   → They are experiencing the same substrate failure that the Core imposes on unprotected minds
│   → The distinction between "practitioner in crisis" and "non-practitioner in the Core" has collapsed
│
├─ WARDEN PRIORITY RESPONSE:
│   Edeyja (Priority 1: emergency Mend at Gap site if Gap detected):
│   She detects: practitioner Coherence 0, Rendering Crisis at the Core
│   This is a Warden Priority 1 emergency — "Gap or Shifting Object detected in any territory"
│   But the trigger is PRACTITIONER Coherence failure, not a Gap
│   → Priority 1 fires for a different reason: the practitioner's Coherence crisis IS generating a new Shifting Object
│   (their rendering collapse creates localized Thread instability — the substrate responds to the practitioner's failure)
│   → Edeyja responds: she is already at or near the Core (Warden operations are Southernmost-based)
│   → She reaches the player within the same scene
│
├─ EDEYJA'S OPTIONS:
│   Standard Rendering Crisis resolution (§3.7): full season withdrawal, 3 Anchoring Scenes, Ob 3 pool check
│   None of these are possible in the Core: season withdrawal means leaving; Anchoring requires Close Knots present
│   Edeyja as an Anchor (Warden Cooperation Track ≥ 3 needed per NEW-S38):
│   If WC ≥ 3: Edeyja can function as an Anchoring Scene partner
│   Anchoring: Bonds check TN 7, Ob 2 → +1 Coherence; costs Knot +1 strain
│   But: is the player's Knot with Edeyja sufficient for an Anchoring Scene?
│   Knot formation requires Disposition ≥ +5 AND TS 30+ for both parties
│   → If the player has Knotted Edeyja (possible at WC ≥ 3, after multiple expedition seasons):
│     Edeyja can Anchor → player Coherence 0 → 1 (still Severed, but no longer Crisis)
│   → If not Knotted: no Anchoring possible → player must leave the Core before crisis resolution
│
├─ EVACUATION FROM THE CORE IN RENDERING CRISIS:
│   Severed Coherence at the Core: +2 Ob to all Thread operations INCLUDING basic sensory navigation
│   The Core Zone's Forgetting mechanism: Cognition + Recall check vs Core Ob 4
│   In Rendering Crisis: Recall effective is reduced (Coherence → Recall cascade: Coherence 0 → Recall −2 effective)
│   → Forgetting Check at Core: reduced pool vs Ob 4 TN 8 → significantly below baseline chance
│   → The player cannot reliably retain the experience even if they survive the evacuation
│   → They will return from the Core having experienced Rendering Crisis and remembering nothing actionable
│
└─ THE DESIGN STATEMENT:
    The Southernmost Core is designed to be inaccessible to practitioners who are not prepared:
    Focus 4+ for operations, Coherence headroom for the costs, Knot with Edeyja for emergency recovery
    A practitioner who arrives at the Core without these prerequisites and attempts high-cost operations
    will experience Rendering Crisis there — the worst possible location for such a crisis
    because none of the recovery infrastructure (rest, Knots, withdrawal) is available
    The Core doesn't care about the practitioner's intent or how important their mission is
    It is the design's clearest statement that Thread capability has prerequisites,
    and prerequisites are not optional
```

**What the alternate branch reveals:** Rendering Crisis in the Core is a scenario the design has prepared for: Edeyja's Warden Priority 1 fires, her potential Anchor role (requiring Knot formation at WC ≥ 3) is the designed recovery path. But if the player hasn't built the Warden relationship before arriving at the Core in crisis, there is no recovery path available there. The Core's inaccessibility is a prerequisite structure, not a punishment.

---

## CROSS-BATCH STRUCTURAL OBSERVATION

Across all twelve counterfactual scenarios, one pattern is consistent:

**The alternate path is not "worse." It is differently instructive.**

- Arc A (Edeyja never reached) reveals that the political game is downstream of RS
- Non-defecting Haelgrund produces Collision A through a different mechanism than defection would
- Consecration refusal demonstrates that pre-conditions for a political move are as important as the move
- Forgetting Failure for Vaynard produces a deal structure rather than a dead end
- Failed Cultural Uprising redirects RM to a co-victory path
- Non-aborting Torsvald creates Thread contamination rather than institutional detection
- Lock Distribution to Maret Uln alone creates the most volatile practitioner-intelligence situation in the campaign
- Player death in combat produces ghost sheets and captured-player relationship dynamics that don't otherwise exist
- Structural N-Way collapse damages all victory conditions simultaneously rather than just one faction's
- Counter-intelligence success enables double-agent operations rather than simple exposure
- Rendering Crisis in the Core shows that recovery infrastructure must be pre-built before it's needed

The design does not have a "correct" branch. It has a topology of consequences where each path reveals something about the game's structure that the other paths don't. This is the test methodology's most important finding: emergent arc skeleton testing should include counterfactual branches as standard, because the uncollected paths are where the design's structural assumptions are most visible.

---

*End of Batch 8 (Counterfactual) document.*
*12 counterfactual scenarios (NEW-S92 through NEW-S103), branching from 11 distinct prior scenarios.*
*Combined session totals: 103 emergent scenarios (91 primary + 12 counterfactual), 5 feedback loops, 70 open items.*
*New open item raised: [GAP] RM Phase 2 Uprising attempt — is "used up for this arc" permanent per campaign arc or per season? (NEW-S96, resolution needed before RM Phase 2 is playtested.)*
