# THREADWORK MECHANICS — v2.6
## Date: 2026-03-27 (revised 2026-04-02)
## Authority: Philosophical Foundations (immutable) → this document (design proposal, requires editorial approval)
## Version: v3.1 — Part Nine (S-01–S-06 / P-11–P-26) applied in-place. All appendix sections eliminated.
## Revision: Incorporates Leap-as-rendering-suspension. Supersedes v1.

---

---

## MODE APPLICABILITY INDEX
*Added 2026-04-02 — applied per user session instruction*

### ALL MODES (TTRPG, Board Game, Hybrid)
- Part 1: Philosophical Framing — foundational for all modes
- Part 4: Co-Movement (Version C) — core mechanic; BG uses card abstraction, TTRPG uses dice
- Part 5: Rendering Stability (World Track) — world-level track applies in all modes
  - §5.4: Rendering Stability in Board Game (BG only)
  - §5.5: Rendering Stability in Hybrid (Hybrid only)
- Part 8: Interdependency Map — implementation sequence for all modes
- Part 9: Stress Test Patches (S-01/P-11 through S-??/P-30) — all mode patches compiled here

> **Scale-based Rendering Stability (P-25):** Rendering Stability consequences on Partial and Failure results scale with operation scale. The below-the-waterline portion of a Structural thread is enormously larger than an Object thread's; when the interaction fails, the unintelligible portion's response is proportionally more severe. **Override degree table Rendering Stability values with the following:** | Scale | Partial Rendering Stability Cost | Failure Rendering Stability Cost | |---|---|---| | Object | 

> **BG Thread degree table (P-23):** Board game Thread orders use the standard four-degree system (Overwhelming / Success / Partial / Failure), consistent with the core engine. | Order | Overwhelming | Success | Partial | Failure | |---|---|---|---|---| | **Weave** | Rendering Stability +2 | Rendering Stability +1 | Rendering Stability unchanged; draw Co-Movement Card | Rendering Stability −1; draw Co-Movement Card | | **Mend** | Gap closed; Rendering Stability +2 | Gap closed; Rendering Stability +1 | Gap reduced one category; Rendering Stability un

> **Mass battle Rendering Stability cost note (ST-TW-03):** **Finding from sim_x_03_massbattle_thread.md**
**[DESIGN NOTE]**
The ×3 Rendering Stability multiplier for mass battle Thread operations means a practitioner performing 5+ Thread operations in a single large battle risks significant Coherence drain (−1/op = Coherence 5 after 5 ops → Dissonant threshold). This is pro

### TTRPG ONLY
- Part 2: Operations — Approach Training, Leap, all named operations (Weaving, Pulling, Locking, Dissolution, Mending, Collective)
- Part 3: Coherence (10→0) — personal practitioner track; no BG equivalent
- Part 6: Threadcut Beings — TTRPG encounter mechanics

> **Delayed manifestation (P-22):** When the actual co-movement d6 produces "delayed manifestation" (result 6) on a Past-Oriented Pull, the temporal displacement has occurred at the Thread level but the physical facts have not yet updated. For 1d3 scenes, the world contains a paradox window: - Practitioners with Thread Sensitivity 30+: perceive the target's thread as both present and absent — the displacement is visible at the Thread level even tho

> **Paradox window resolution (PP-193):** [PROVISIONAL] The P-22 paradox window resolves as follows. **Auto-resolution:** At window end (1d3 scenes), physical facts update; thread snaps to displaced state. Observers Thread Sensitivity 30+ perceive sudden realignment. **Early closure:** A practitioner may Mend the paradox window site (treat as Micro-Gap, Ob 3). Success: window closes immediately. Partial: duration halved. Failure: window persists full duration; RS −2. **Exploitation during window:** Another practitioner may target the paradoxed thread at +2 Ob (two simultaneous configurations resist). On Failure: window collapses immediately and operation's Failure consequences also apply. **After window:** Temporal Disjunction persists (memories intact; physical facts now match displaced state). No further mechanics unless new operation targets displaced thread.

> **Sequential POPs on paradoxed thread (PP-203):** [PROVISIONAL] If a practitioner attempts a Past-Oriented Pull targeting a thread that is currently in a paradox window (P-22 delayed manifestation active on that thread), the attempt **automatically fails**. The thread exists in two simultaneous states; intentionality cannot lock onto a thread with indeterminate configuration. The Leap still fires (Coherence cost applies, Focus window consumed), but the operation resolves as Failure without a roll (no RS cost from the operation itself — the substrate did not engage). The paradox window is unaffected. This ruling applies only to the paradoxed thread itself; other threads in the same scene are unaffected.



> **Threadcut/Mending (P-17):** A threadcut being present at a Gap site draws on the same substrate the practitioner is trying to Mend. Its continuous self-rendering competes with the Mending operation's intentionality. **Mechanical effect:** +Ob = being's Thread Sensitivity ÷ 20 (round up), maximum +4, to Mending operations targeting that Gap while the being is present. This Ob modifier stacks with other modifiers (territory effects, Fraying B

> **Opposing beliefs (P-12):** *Already patched into §2.5.* Directly opposing Beliefs require a pre-Leap Belief check. Tangential conflicts: non-chaining dice.

> **Pool floor correction (R-57):** Minimum 5 dice before rolling any Pull. Below 5D (from wounds, degradation, low stats):
practitioner cannot Pull. Lock is still available (does not require the same sustained openness).
Apply to §2.4 Pulling, eligibility section.

> **Ob correction (R-55):** For Dissolution targeting a living being at Personal scale:
> Ob = target's Endurance + target's Spirit + armour modifier (Light+1, Medium+2, Heavy+3)
> Standard success = Partial (Shifting Object, ~50% HP damage).
> Overwhelming required for immediate incapacitation.
Replaces: "same as Lock" for Pe

> **Scaled shifting objects (P-15):** Shifting Objects can form at any scale. The oscillation manifests differently by scale: | Scale | Manifestation | |---|---| | Object | Physical object oscillates between presence, absence, and distortion. The classic Shifting Object. | | Personal | A person's rendering flickers. Others perceive inconsistency — the person seems to be two things at once, or to phase between states. Not a Thread oper

### BOARD GAME ONLY
- §5.4: Rendering Stability in Board Game
- §7.1: Board Game — New Order: Mend, Co-Movement Card Deck (18 cards), Lock Chronic Drift, Rendering Stability Track

### HYBRID ONLY
- §5.5: Rendering Stability in Hybrid
- §7.2: Hybrid Mode
- §7.3: Updated Mode Branching

### CROSS-MODE (applies in both TTRPG and Hybrid)
- §2.3–2.4: All named operations — applicable whenever a practitioner Player Character is present (TTRPG and Hybrid personal scenes)
- §A.10 of mass_battle_v3.md: Thread operations in mass battle (Hybrid / TTRPG mass combat)

> **Cross-reference (ST-TW-05):** Coherence referenced in mass_battle_v3 §A.10 = this document's personal Coherence track (10→0). Not a unit stat. auto-cost −1/op depletes personal track by 1 per mass battle operation.

---

## PHILOSOPHICAL FOUNDATION
See `designs/ttrpg/threadwork_philosophical_reference.md` for the complete philosophical framing (What Threads Are, Ein Sof and Spooling, The Scale Principle, The Two States, Why Operations Produce Unpredicted Consequences). That document is the canonical reference for canon-guard P-01–P-15 compliance checks on threadwork mechanics.

# PART TWO: OPERATIONS

## 2.1 Approach Training

*No changes from current §5.1. Full season commitment, narrative confirmation, Approach Training tag granted.*

## 2.2 Diagnosis — STRUCK (ED-134/ED-124, 2026-04-03)

> Diagnosis as a standalone action is removed from the system. Practitioner either suspends their sense of self and Leaps, or does not. No preparatory gate action exists. In mass combat, Leap proceeds directly in Phase 4 without Diagnosis. In personal combat, Leap is a Priority 5 full-round action with no Diagnosis prerequisite. See params_threadwork.md §Diagnosis — STRUCK.


## 2.3 The Leap — Suspending Rendering

The Leap is the practitioner's transition from rendering to contact — the act of suspending their own always-already human rendering so that their configuration can interact with threads in originary intentionality.

This is not entering another state. It is leaving the only state consciousness knows. There is no bridge, no gradient, no partial Leap. You cannot get there from here by degrees. You must let go of the thing that constitutes your being as a conscious agent — your rendering — and trust that your configuration's intentionality, set during Diagnosis and declaration, will direct what happens in your absence from yourself.

### Eligibility (verify before rolling)

- Approach Training tag ✓
- Thread Sensitivity 30+ ✓
- Not currently engaged in melee with an opponent who has declared an attack this round ✓
- Not incapacitated (Health > 0) (PP-232 — prior ceiling(Health÷2) threshold removed; incapacitation is binary under current wound system)

The Leap is a **full-round action (Priority 5)**. No attack, no movement, no manoeuvres in the same round. Only reactive defence available: Parry or Dodge Backwards (character's choice when declaring). These are pre-conscious physical responses that do not require rendering.

### The Leap Roll

**Pool:** Spirit + Attunement + relevant History bonus (e.g., "Einhir Scholar": points + 3) + Thread Pool Score (Thread Pool Score = Thread Sensitivity ÷ 10, round down) (PP-232)
**TN:** 7
**Ob:** Thread Sensitivity 30–49 = 2 · Thread Sensitivity 50+ = 1 · +1 Ob per Wound

> **Einhir framework (P-26):** "Einhir framework" appears as a prerequisite for Locked Zone border Mending (Ob 8+). It requires all three of: 1. **Knowledge:** The practitioner has Diagnosed the Locked Zone's structure (requires a prior Southernmost expedition Diagnosis scene or equivalent scholarly research via Einhir Texts). 2. **Technique:** The practitioner possesses at least one Einhir Text technique applicable to Mending 

Pre-calculate the Leap pool on the character sheet as a named entry separate from History pools.

| Degree | Outcome |
|---|---|
| Overwhelming | Clean suspension. Next Operation's Ob reduced by 1 (minimum 1). Practitioner gains 1 Thread Sensitivity. |
| Success | Rendering suspended. Contact established. Proceed to operation. |
| Partial | Unstable suspension — rendering keeps reasserting. Operation Ob +1. Take 2 Composure strain. |
| Failure | Thread contact fails. −1D to Thread Pool Score for remainder of scene. (PP-232) |

**Partial result framing:** The rendering keeps bleeding through. The practitioner is partly present to themselves, which means they are partly interfering with the contact. Their consciousness is fighting the suspension. The operation is still possible but compromised — the practitioner's rendering is contaminating the interaction with their own categories.

**Failure framing:** The practitioner could not surrender rendering. Their consciousness held on. This is not weakness — it is the fundamental difficulty of doing something that your being resists constitutively. The aftereffect (−1D Thread Pool Score) represents the psychic friction of the failed attempt — the practitioner's engagement with Thread is degraded for the remainder of the scene, not from injury but from the failed surrender itself. (PP-232)

### The First Leap (Event Scene)

The first time a character attempts the Leap, it is run as a full event scene. The Game Master describes the approach and the perceptual boundary.

On success: the character experiences what it is to Be beyond their own being. They perceive — no, they do not perceive, that is the wrong word, but there is no right word because language IS rendering — they interact with the constitutive process that underlies everything they have ever known. When they return, they know their rendering is partial. Not intellectually. Ontologically. They have been outside it.

Thread Sensitivity score is revealed to the player. Practitioner designation granted. Certainty −1 (permanent: the old framework can never feel complete again).

On failure: **Dissociation** — the character's rendering reasserted violently. They are present in the world but shaken. Cannot attempt Thread operations for one season. Thread Sensitivity is frozen. They may attempt again next season.

### Contact Duration

Once the Leap succeeds, rendering is suspended for a number of rounds equal to the practitioner's **Focus score**. The Leap round itself counts as Round 1. At Round (Focus + 1), rendering reasserts naturally — the practitioner's consciousness reclaims its constitutive function.

> **Focus Halving (P-11):** When an environmental effect halves contact duration, round down. Focus 1 after halving = zero operations (experience only). Focus 3 halved = 1 = zero operations. Focus 5 halved = 2 = one operation. Environmental Focus reduction affects contact duration only, not pool calculation — the attribute itself is unchanged.

The window counts down whether or not the practitioner acts within it. Focus is how long you can hold your own rendering at bay. It is not concentration in the ordinary sense. It is the capacity to sustain the absence of the thing that makes you human.

**Revised standard sequence (Diagnosis precedes Leap):**
- **Pre-Leap round(s):** Diagnosis (Priority 4). Practitioner renders the target, reads configuration, sets intentionality. Declares operation type(s) and target(s).
- **Round 1 (Leap):** Rendering suspends. Contact established. No operation this round — the practitioner's configuration is orienting in originary intentionality. The suspension must settle before directed interaction can occur.
- **Round 2+:** Operations proceed as declared.
- **Round (Focus + 1):** Contact drops. Rendering reasserts. Practitioner returns to themselves.

**Operations per Focus:**

| Focus | Contact Rounds | Operation Rounds | Operations Available |
|---|---|---|---|
| 1 | 1 | 0 | None. Contact is too brief. Configuration orients and rendering reasserts. The practitioner experiences the suspension but cannot act within it. |
| 2 | 2 | 1 | One operation. |
| 3 | 3 | 2 | Two operations. |
| 4+ | 4+ | 3+ | Three or more. Rare — Focus 4+ requires significant investment. |

At Focus 1, the practitioner gains the experience of contact (relevant for Thread Sensitivity growth, First Leap) but cannot perform operations. This creates a meaningful progression gate: Focus 2 is the minimum for functional practice.

**Wound during the Leap round (before contact is established):** If the practitioner takes a Wound in the same round as the Leap roll, before the roll is resolved, apply +1 Ob to the Leap roll as normal (Wound penalty). The Attunement disruption check does not apply — it only triggers once contact is established. If the Leap succeeds despite the Wound penalty, contact proceeds normally.

**Incapacitation during contact:** If a Wound incapacitates the practitioner during contact (Wounds reach or exceed the incapacitation threshold: ceiling(Health ÷ 2)), contact terminates immediately regardless of the Attunement disruption check result. The operation in progress is treated as a Failure. The practitioner returns to rendering incapacitated.

**Wound disruption during contact:** When the practitioner takes a Wound while contact is established, make an Attunement check immediately: Attunement score in d10s, TN 7, Ob 1. Failure: rendering reasserts violently — the body's damage overrides the suspension. Contact drops.

### Thread Operation Visibility

Operations are invisible to characters with Thread Sensitivity 0–9. Detection by tier:

| Observer Thread Sensitivity | Perception |
|---|---|
| 0–9 | Nothing perceived |
| 10–29 | Vague unease; cannot locate source |
| 30–49 | Senses an operation in the scene; general direction identifiable |
| 50–69 | Identifies operation type and approximate target |
| 70+ | Perceives the full configuration being worked |

Physical effects (a wound closing, an object moving) are visible to all.

**Concealing from Thread Sensitivity 30+ observers:** Roll Cognition only (no History), TN 7, Ob = observer's Thread Sensitivity ÷ 30 (round up). This is a pre-Leap action — concealment is set before rendering suspends. The practitioner shapes how their configuration presents during contact, but cannot adjust concealment during contact itself.

**Wound penalties:** +1 Ob per Wound applies to all Thread operation rolls — Leap, Weaving, Pulling, Mending, FR. The body's damage impedes the suspension.

## 2.4 Operations During Contact

During contact, the practitioner is not consciously present. Their configuration interacts with threads directed by the intentionality set during Diagnosis and declaration. The player rolls dice — this is a game abstraction. In-fiction, the practitioner does not experience the operation as a sequence of decisions. They set intent, Leaped, and when they return to rendering, the outcome has occurred.

**Declaration before Leap:** The player declares the operation type (Weave, Pull, Mend, Lock, Dissolve) and the target (identified during Diagnosis) before the Leap roll. This declaration is the intentionality. Once the Leap succeeds, the operation proceeds as declared. The player cannot change operation type or target during contact — that would require rendering, which is suspended.

**Multiple operations in one contact window:** If Focus allows multiple rounds, the practitioner may perform sequential operations, but each was declared before the Leap as part of the overall intentionality. The sequence was set in advance. Adapting mid-contact is impossible.

**Sequential failure penalty:** If an operation fails, all subsequent operations in the same contact window are at +1 Ob (cumulative per failure). The practitioner's intentionality was set assuming each step would succeed. When one fails, the remaining intentions are directed at a state that no longer matches what the practitioner rendered during Diagnosis. The intentionality is misaligned. The interaction continues — the configuration still attempts the declared sequence — but the misalignment degrades the outcome.

### Weaving — Things Cohere

> **Design note (ST-TW-01):** W-24 (Coherent Strike) at Object scale: Rendering Stability unchanged, Coherence −0 on Success. If Leap round is protected (opponent at wrong range), operation is free in Thread terms. Design question: is this intended? See ED-046.

**What happens:** The practitioner's configuration interacts with a thread, and the thread is drawn toward greater coherence — toward stable actualization. The practitioner directed this through intentionality: they intended coherence, healing, stabilisation, and their configuration's interaction with the thread produced it.

**Why Weaving works with the ground:** Ein Sof spools continuously. Weaving aligns with that process — the practitioner's intentionality toward coherence assists what the ground is already providing. This is why Weaving effects are stable and permanent: the operation did not impose something foreign. It assisted the process that already sustains the thread. Scars are real. The world is consistent. No paradox.

**Pool:** Spirit + relevant History bonus + Thread Pool Score
**TN:** 7

**Ob by scale (Thread Sensitivity minimum required):**

| Scale | Example | Ob | Min Thread Sensitivity |
|---|---|---|---|
| Object | Close a wound; reinforce a cracking blade | 1 | 30+ |
| Personal | Stabilise a dying character; accelerate injury healing | 2 | 30+ |
| Relational | Bind a diplomatic agreement; reinforce trust | 3 | 50+ |
| Territorial | Raise a faction's Stability by 1; stabilise a region | 4 | 50+ |
| Structural | Permanent reinforcement of a fortification or institution | 5 | 70+ |

| Degree | Outcome |
|---|---|
| Overwhelming | Full effect. Rendering Stability +1 (Relational scale or above only). Practitioner gains 1 Thread Sensitivity. The effect exceeds the stated intention — the wound closes without scarring; the agreement develops genuine trust beyond its terms. |
| Success | Full effect. Rendering Stability unchanged. |
| Partial | Partial effect (Game Master sets scope). Rendering Stability −1. Coherence −1. |
| Failure | Interaction collapses. Rendering Stability −2. Coherence −1. At Rendering Stability ≤ 40: Shifting Object forms. At Rendering Stability ≤ 20: Gap opens. |

**Over-Actualisation Hazard (Relational+ scale):**

Successful Weaving at Relational scale or above drives a configuration toward more coherence than the substrate naturally supports. Ein Sof continues to spool through the thread, but the thread is now too rigid to integrate what the ground provides. The thread stiffens.

| Scale | Over-Actualisation Consequence on Success |
|---|---|
| Object / Personal | None. |
| Relational | Subsequent Thread operations targeting this same configuration: +1 Ob. Clears after one season or when the configuration is Pulled. |
| Territorial | As Relational, plus: Diagnosis on this configuration +1 Ob. |
| Structural | As Territorial, plus: +1 Rendering Stability degradation per season it persists (the rigid configuration obstructs substrate traffic). |

On Overwhelming at Relational+: over-actualisation effects halved in duration.

> **Over-actualisation modifier — Shifting Object carry-through (PP-208):** [PROVISIONAL] When a Woven thread shatters into a Shifting Object via the brittleness rule (§2.4 Weaving GM sidebar), the over-actualisation +1 Ob modifier **does not carry through** to the Shifting Object. The OA modifier was a property of the Woven configuration. When that configuration collapses into a Shifting Object, it ceases to exist as the target of the OA modifier — the Shifting Object is a new configuration formed from the collapse residue, not the Woven thread in a damaged state. Mending the Shifting Object therefore proceeds at base Ob without the OA penalty. Exception: if the Woven configuration did not shatter (e.g., OA persists on a still-Woven thread that a practitioner then Mends to prevent Gap formation), the OA modifier applies to the Mending attempt as normal (+1 Ob stacked on Mending base Ob).

> **Double over-actualisation — two independent Weavings (PP-209):** [PROVISIONAL] If two practitioners independently Weave the same configuration in separate contact windows within the same scene (e.g., both Leap separately after a lattice failure), and both succeed: the configuration acquires **two stacked OA modifiers** (+2 Ob total to subsequent ops targeting this configuration). Both stacks clear after 1 season or after a Pull. Brittleness is compounded: when a non-Thread stress event of sufficient severity strikes a doubly over-actualised thread, the shattering consequence is proportionally more severe — the GM may rule the Shifting Object is already at the next severity tier (e.g., Shifting Object forms as if already 1 season old, making its deterioration timeline shorter). The Overweaving +1 Ob cumulative rule (§2.4) applies only within a single contact window and does not govern separate contact windows — separate windows accumulate OA stacks, not Overweaving penalties.



**Game Master sidebar — Brittleness in volatile contexts:** Weaving at Relational+ scale stabilises a configuration but makes it rigid. A Woven diplomatic agreement, stabilised faction, or reinforced institution cannot adapt to stress the way an unworked configuration can. If a non-Thread event of sufficient severity strikes a Woven configuration — a siege, betrayal, institutional collapse — the Game Master may rule it shatters into a Shifting Object at its scale rather than simply failing. A broken Woven treaty may become a Relational Shifting Object (deteriorating to a Relational Gap within 1d3 seasons) rather than just a broken treaty.

Before Weaving in a politically volatile context, the Game Master should ask: is this configuration likely to face severe stress before it can be Pulled or allowed to expire naturally? If yes, Weaving may be counterproductive. The practitioner cannot know this during Diagnosis — brittleness is a consequence of over-actualisation that manifests only when external stress arrives.

**Overweaving:** Each operation after the first in the same contact window: +1 Ob (cumulative). A collapsed overweave: Rendering Stability −3 and local Shifting Object risk.

### Pulling — Things Open

> **Past-Pull reversion (P-21):** When Past-Oriented Pulling displaces an event, mechanical states triggered by that event may or may not revert. The Game Master determines which states revert based on their causal source: - **Physical-fact-triggered states revert.** Knot strain from "external events" (territory conquest, death of a Knot entity) was caused by a physical fact. If the fact is displaced, the strain reverts. The Knot entity is

> **Fortification Ob addition (R-67):** When Pulling a structural/territorial configuration that includes a fortified site (Fortification ≥ 1):
add the Fortification level to the Ob. Physical reinforcement increases actualization.
Apply to §2.4 Pulling, Foundational/Structural scale section.

**What happens:** The practitioner's configuration interacts with a thread, and the thread is drawn toward potential — toward looseness, openness, the constitutive ground. The practitioner intended loosening, and their configuration's interaction produced it.

**Why Pulling effects expire:** The thread returns to its natural configuration because Ein Sof continues to spool. The ground does not stop providing. The Pull temporarily interrupted the spooling; when the interruption ends, the process resumes. Duration represents how long the practitioner's originary intentionality holds against the ground's continuous provision.

**Pool:** Spirit + relevant History bonus + Thread Pool Score
**TN:** 7

**Ob by actualization level:**

| Actualization | Example | Ob | Min Thread Sensitivity |
|---|---|---|---|
| Loosely actualised | Thread already drifting | 1 | 30+ |
| Normally actualised | Standard state | 2 | 30+ |
| Firmly actualised | Strong configuration, deliberate or old | 3 | 50+ |
| Previously Woven | Another practitioner's work resists | 4 | 50+ |
| Foundational | Deep structural thread | 5 | 70+ |

**Duration by surplus successes:** 0 = end of scene. 1 = end of session. 2+ = until next seasonal accounting.

> **Correction (R-54):** Duration ladder shifted (Pull requires re-application at scene scale):
- 0 surplus successes = 3 rounds (was: end of scene)
- 1 surplus success = end of scene (was: end of session)
- 2+ surplus = end of session (was: until next seasonal accounting)
- 3+ surplus = until next seasonal accounting
Apply to §2.4 Pulling — Past-Oriented Pulling duration table.

| Degree | Outcome |
|---|---|
| Overwhelming | Full effect. Extended duration. Rendering Stability unchanged. |
| Success | Full effect. Standard duration. Rendering Stability unchanged. |
| Partial | Partial effect or reduced duration. Rendering Stability −1. Coherence −1. |
| Failure | Snap-back. 1 Wound (armour does not apply). Rendering Stability −2. Coherence −1. |

### Past-Oriented Pulling

**What happens:** The practitioner's intentionality is directed toward the thread's accumulated temporal depth — the history of spoolings that constitute what it has been. During contact, their configuration interacts with the thread at this deeper level, displacing temporal weight. The physical facts are removed. Memories — which are themselves spooled configurations in other beings — remain intact, producing Temporal Disjunction.

**Requirements:** Thread Sensitivity 70+ · Rendering Stability ≤ 60 (substrate must be stressed enough for temporal depth to be accessible — in a pristine world, the temporal weight is too firmly actualised to pull against)

**Foundational-scale Past-Oriented Pulling:** Displacing a Foundational event (the Einhir Catastrophe, a civilisation-ending collapse, a foundational institution's origin) requires all standard prerequisites plus: the Einhir framework (§9.15) — the intentionality required to reach Foundational temporal depth cannot be formed without it. Add +2 Ob surcharge to the recency Ob (Ob 7 recency + 2 = Ob 9 for a generational Foundational event). Rendering Stability consequence ×3 on all outcomes (Success: Rendering Stability −9 minimum; Failure: snap-back Wound + Rendering Stability −6 minimum). This is a near-mythic act — maximum conceivable practitioner achieves ~5% success — but it is mechanically possible. It is a legitimate campaign endpoint: the thing the Einhir could not do and the thing a generation of practitioners might spend a campaign attempting.
**Pool:** Spirit + relevant History bonus + Thread Pool Score÷2 (round down)
**TN:** 8 (PP-232 — corrected from 7; POP targets deeper temporal weight requiring greater precision)

**Ob by recency:**

| Recency | Ob |
|---|---|
| Same scene/session | 3 |
| 1–2 seasons | 4 |
| 3–5 seasons | 5 |
| 6–10 seasons | 6 |
| 10+ seasons / generational | 7 |

*All existing mechanics (Ob by recency, degree table, Thread Tension/Rendering Stability consequences, Fraying Bane) retained with Rendering Stability replacing Thread Tension throughout. Rendering Stability costs inverted: where Thread Tension was +3 minimum, Rendering Stability is −3 minimum.*

**Additional Ob modifier — active Knot Crisis:** If the target event has caused an active Knot Crisis in any character (the death is still being grieved, the loss is still raw), add +1 Ob. The ongoing relational weight of the grief makes the temporal thread more firmly actualised — living sorrow has woven itself into the thread's current configuration and resists displacement.

### Locking — Unable to Become

> **Rendering Stability drain cap (R-58):** Regardless of concurrent active Locks: Rendering Stability drain from Locks cannot exceed −1/round in combat
or −1/scene in non-combat. Multiple Locks do not stack Rendering Stability drain within a scene.
Seasonal drift is unaffected (each active Lock contributes independently at Accounting).
Apply to §3.2 Coherence Reduction / Loc

**What happens:** The practitioner's intentionality is directed toward total actualization — freezing the thread permanently in its current rendered state. During contact, their configuration drives the thread to full actualization. The thread can no longer move between actual and potential. Ein Sof continues to spool, but the thread cannot integrate what the ground provides. It is frozen. Unable to become.

**Requirements:** Thread Sensitivity 50+
**Pool:** Spirit + relevant History bonus
**TN:** 7
**Minimum Ob:** 4

**Ob by scale:**

| Scale | Ob |
|---|---|
| Object | 4 |
| Personal | 5 |
| Relational / Process | 6 |
| Territorial | 7 |
| Structural / Foundational | 8+ |

**Thread Sensitivity 70+ Tier Reduction:** −1 to all FR Rendering Stability costs (minimum 1).

| Degree | Outcome |
|---|---|
| Overwhelming | Target permanently locked. Rendering Stability −1. Practitioner gains 1 Thread Sensitivity. |
| Success | Target locked. Rendering Stability −1. |
| Partial | Partial lock (Game Master sets scope). Rendering Stability −2. Coherence −1 (cap). |
| Failure | Collapse onto practitioner. Take 2 Wounds (no armour). Rendering Stability −3. Coherence −1 (cap). Adjacent configurations become partially rigid: +1 Ob to all Thread operations targeting configurations adjacent to the failure site, remainder of season. |

**Chronic consequences:**

| Duration | Effect |
|---|---|
| 1 season | No additional effect. |
| 2–3 seasons | Rendering Stability −1/season (substrate strain from blocked configurational traffic). +1 Ob to operations targeting Lock or adjacent configurations. |
| 4+ seasons | Rendering Stability −2/season. Operations targeting any configuration in the same zone: +1 Ob (the frozen thread occludes Diagnosis, degrading intentionality for subsequent operations). |
| Permanent (never reversed) | Substrate adapts. Rendering Stability drift ceases. Permanent +1 Ob to adjacent operations. This is how Locked Zones form. |

> **Variable Rendering Stability drift (R-63):** Replaces uniform −1 Rendering Stability/season for locked institutions:
- Static domain (frozen process, unchanging institution): −0 Rendering Stability/season
- Slow-change domain (seasonal/yearly evolution): −1 Rendering Stability/season
- Dynamic domain (active contestation, living relationship): −2 Rendering Stability/season
Game Master determines domain type when Lock is applied.

**Reversing a Lock:** Pulling at Ob = (original practitioner's Thread Sensitivity ÷ 10, round up) − 2, minimum Ob 1. Successful release: Rendering Stability +1 per season the Lock persisted (max +5), as the substrate decompresses.

**Dissolution of a Lock:** Tears the locked configuration rather than unwinding it. No Rendering Stability release bonus (unlike Pulling — the configuration was torn, not cleanly unwound). Dissolution of a Permanent Lock (4+ seasons, substrate adapted) automatically fails — the configuration no longer exists as a discrete target; it has become part of the substrate's structure. Permanent Locks can only be addressed via the Einhir framework. A novice Lock (Thread Sensitivity 30) is trivially reversible (Ob 1); an expert Lock (Thread Sensitivity 100) requires a specialist (Ob 8). Long-standing Lock release: Rendering Stability +1 per season the Lock persisted (max +5). If 4+ seasons: Shifting Object risk from sudden configurational release.

### Dissolution — Unable to Be

**What happens:** The practitioner's intentionality is directed toward the unintelligible pole — driving the thread's intelligible face away entirely. During contact, their configuration interacts with the thread and tears its rendered surface from the constitutive ground. What remains is the ground showing through: a Gap. The thread is unable to be in the rendered world.

**Why Dissolution is acute:** Tearing is immediate and violent. The substrate ruptures. Ein Sof — infinite positive being — erupts through the tear as excess, not void. Monstrous configurations are forced through the rupture into the rendered world, partially intelligible and exceeding integration capacity.

**Requirements:** Thread Sensitivity 50+
**Pool:** Spirit + relevant History bonus
**TN:** 7
**Minimum Ob:** 4

**Ob table:** Same as Lock.

| Degree | Outcome |
|---|---|
| Overwhelming | Target dissolves cleanly. Rendering Stability −3. Micro-Gap forms and closes within the scene. |
| Success | Target dissolves. Rendering Stability −5. Gap forms, lasts one scene, closes. |
| Partial | Target becomes a Shifting Object. Rendering Stability −6. Gap does not close without Mending. Coherence −1 (cap). |
| Failure | Full Gap tears open. Rendering Stability −8. Monstrous Incursion immediately. Practitioner Incapacitated. Coherence −1 (cap). |

**Lock vs. Dissolution summary:**

| Dimension | Lock | Dissolution |
|---|---|---|
| What it does | Freezes the intelligible face | Tears the intelligible face away |
| Temporal character | Chronic (damage accumulates) | Acute (damage immediate) |
| Rendering Stability consequence | Lower immediate (−2 to −4), chronic drift (−1 to −2/season) | Higher immediate (−3 to −8), no drift |
| Gap risk | None on success; stiffening on failure | Always |
| Core violation | Unable to become | Unable to be |

> **Chronic perception (P-13):** *Already patched into §2.7 chronic table.* The frozen thread's perceptual occlusion manifests as +1 Ob to the operation (degraded intentionality from impaired Diagnosis), not to Diagnosis itself (which has no Ob).

### Mending — Repairing the Substrate

> **Mending co-movement (P-19):** The Mending epistemic co-movement profile now differentiates by outcome: | Degree | Epistemic Effect | |---|---| | Overwhelming | Strong settling. Observers with Thread Sensitivity 10+ perceive the area as markedly calmer. Non-sensitives notice a distinct easing of tension. | | Success | Settling. Observers with Thread Sensitivity 10+ perceive calming. Non-sensitives may notice subtle easing. | | Partial | Ambiguous. Observers p

> **Correction (R-56):** Healing operations (W-08 and variants) use accelerated Overweave: each healing operation in the same contact window adds +2 Ob (not +1). Sequence: 1st heal Ob 1, 2nd Ob 3, 3rd Ob 5, 4th Ob 7.

> **W-33 note (P-31):** W-33 is effective only for units with CP ≥ 3. A rallied unit with CP ≤ 2 will have an effective combat pool of 0 despite Cohesion restoration — the Cohesion penalty from Cohesion 2 eliminates the entire pool at low CP values. W-33's primary use case is Professional or Elite infantry (CP 3+) that has broken under morale pressure while retaining Strength.

**What happens:** Mending does not work on threads. The practitioner's intentionality is directed toward the substrate itself — the rendered world's capacity to integrate what Ein Sof provides. A Gap is where that capacity has failed. The practitioner Leaps, and during contact their configuration interacts not with a thread but with the absence of one — the place where the substrate should be supporting a thread and is not.

This requires a different intentionality than thread operations. The practitioner is not directing their configuration toward a thread's coherence or potential. They are directing it toward a structural absence, intending restoration of the conditions under which threads can exist. They are repairing the loom, not working a thread.

**Requirements:** Thread Sensitivity 50+ · Target must be a Gap, Shifting Object, or Locked Zone border
**Pool:** Attunement + Focus + Thread Pool Score
**TN:** 7

**Why Attunement + Focus:** Mending requires sensitivity to the substrate's condition (Attunement) and sustained suspension of rendering while engaging something that is not a thread (Focus). The standard Spirit + History pool targets threads via intentionality. Mending targets the space between threads — the substrate itself. The faculty engaged is different.

**Mending Ob ceiling:** Total Mending Ob cannot exceed 8, regardless of stacked modifiers (threadcut interference per §9.7, Rendering Stability threshold penalties, sequential failure penalties, Wound penalties). The ceiling reflects the substrate's own nature: Mending engages absence, not presence, and the difficulty of engaging absence cannot exceed the difficulty of the most damaged substrate configurations. Individual modifier sources still apply and stack — the ceiling caps the total, not each source.

**Ob by Gap severity:**

| Gap Type | Ob | Min Thread Sensitivity |
|---|---|---|
| Shifting Object (pre-Gap) | 2 | 50+ |
| Micro-Gap (same scene) | 3 | 50+ |
| Standard Gap (1 session – 1 season) | 5 | 50+ |
| Entrenched Gap (1+ seasons) | 6 | 70+ |
| Catastrophic Gap (3+ seasons) | 7 | 70+; requires Einhir framework or collective operation |
| Locked Zone border | 8+ | 70+; requires Einhir framework |

**Design note — Catastrophic Gaps and Locked Zones:** These are Calamity-tier damage. Solo Mending at Ob 7–8 is intentionally near-impossible (~40–58% even at maximum pool). These sites require collective operations, the Einhir framework, or multi-season Mending arcs. This is the Einhir Catastrophe's legacy made mechanical: the damage they caused cannot be reversed by a single practitioner acting alone.

| Degree | Outcome |
|---|---|
| Overwhelming | Substrate restored. Gap closes cleanly. Rendering Stability +2 (strain released). Coherence −1 (base cost; inclusive of §3.2). Mended area +1 Ob to future Gap formation in this zone for 1 season. |
| Success | Substrate restored. Gap closes. Rendering Stability +1. Coherence −1 (base cost; inclusive of §3.2). |
| Partial | Gap reduced one severity category. Rendering Stability unchanged. Coherence −1 (cap). Second Mending required. |
| Failure | Mending fails. Gap unchanged. Coherence −1 (cap). Rendering Stability −2. |

**Mending co-movement profile:**

*Temporal auto-effect:* Coherence −1. The practitioner engaged with damaged substrate, absorbing temporal dissonance.

*Epistemic auto-effect (by degree):*

| Degree | Epistemic Effect |
|---|---|
| Overwhelming | Strong settling. Thread Sensitivity 10+ observers perceive the area as markedly calmer. Non-sensitives notice a distinct easing of tension. |
| Success | Settling. Thread Sensitivity 10+ observers perceive calming. Non-sensitives may notice subtle easing. |
| Partial | Ambiguous. Observers perceive both settling and tension — something shifted but didn't fully resolve. |
| Failure | Increased tension. Observers perceive things worsening. Non-sensitives feel heightened unease. The substrate was disturbed without being repaired. |

No investigation Ob modifiers on Success or Overwhelming — Mending resolves epistemic instability rather than producing it. On Partial or Failure: +1 Ob to social rolls in the immediate area for the remainder of the scene.

*Actual (d6):*

| d6 | Effect |
|---|---|
| 1 | Dissolution residue at the Mending site |
| 2 | Nearby threads settle into slightly different configurations (minor Shifting Object risk in adjacent zone; self-corrects in 1d3 days) |
| 3 | Temperature/light/sound shift at site (Thread Sensitivity 10+ detectable) |
| 4 | Mended area retains a trace — Thread Sensitivity 30+ perceive a scar in the substrate for 1 season |
| 5 | Adjacent thread realigns, producing an unexpected minor benefit (Game Master describes) |
| 6 | Full closure delayed 1d3 scenes |

## 2.5 Collective Operations

When multiple practitioners operate on the same configuration, they Leap together. Each suspends their own rendering. Their configurations interact with each other and with the threads in a lattice of originary intentionality.

This is not coordination in any ordinary sense. The practitioners cannot communicate during contact — communication requires rendering. They share intentionality, set during collective Diagnosis before the Leap. They interact with each other's configurations below the level of consciousness.

**Collective Diagnosis:** Multiple practitioners may Diagnose in the same round as part of collective preparation. This is a shared Game Master exchange, not sequential individual rolls — all practitioners listen to the same description of the target configuration and set their intentionality together.

**Collective Leap procedure:** All practitioners roll their own Leap in the same round (Priority 5). If the Anchor fails: the collective lattice does not form. Helpers who succeeded are in individual contact (their own Focus windows) but pool their dice to no one — each may perform individual operations at their own Ob, without collective bonuses. If the Anchor succeeds but helpers fail: subtract their contributed dice; if remaining pool drops below half the Anchor's solo pool, apply +1 Ob (lattice fracture). If all fail: all take individual Leap failure consequences.

**Anchor:** Highest Thread Sensitivity practitioner. Sets the primary intentionality. Rolls their full operation pool.

**Helper contribution:** Each assisting practitioner contributes **floor(Cognition ÷ 2)** bonus dice to the Anchor's pool. Each helper must have their own active contact window.

**Constraints:**
- Helpers cannot Fork; Anchor cannot Fork when acting as Anchor.
- If a helper's contact drops (rendering reasserts) before the roll: remove their contributed dice. If total pool drops below half the Anchor's solo pool: +1 Ob (the lattice fractures — one configuration reasserted its rendering and disrupted the interaction).
- Conflicting Beliefs: if a helper's Belief is tangentially conflicting (relevant tension but not direct opposition), their dice cannot chain on 10 — their intentionality is misaligned, limiting coherence. If a helper's Belief **directly opposes** the operation's declared goal, the helper must pass a pre-Leap Belief check (Spirit TN 7 Ob 1) to suppress their opposing intentionality enough to align with the Anchor. Failure: the helper cannot align and drops out before the Leap. Success: participates with non-chaining dice.
- Stunt in collective operations: Anchor's auto-successes replace rolled dice; helpers' contributed dice do not apply to a Stunt.

**Co-movement scales with participant count.** Multiple configurations interacting simultaneously produces correspondingly significant consequences across all three dimensions.

---

# PART THREE: COHERENCE (10→0)

## 3.1 What Coherence Measures

Coherence tracks the stability of a practitioner's rendering — their capacity to render the world and themselves as a conscious being within it. Each Leap temporarily surrenders rendering. Each return restores it. But repeated practice of suspending the thing that constitutes your human being makes that thing less stable on return. Coherence measures how much of that stability remains.

Low Coherence is not corruption, seduction, or moral failure. It is what happens when you have repeatedly practiced the absence of your own consciousness from itself. Your rendering comes back each time, but it comes back a little less firmly. The categories it provides — self/other, past/present, human/monstrous, real/unreal — hold a little less tightly. Eventually, they do not hold at all.

This includes the effects previously attributed to dissolution residue use and the former Taint track. Contact with dissolution residue — compressed potential oriented toward the unintelligible ground — produces accelerated Coherence loss because the residue's volatile proximity to the ground intensifies the practitioner's exposure to what lies beyond rendering. The perceptual shift formerly called "epistemic seduction" is Coherence degradation: the categories that structure consciousness dissolving because the practitioner has spent too much time beyond them.

**Range:** 10 (fully coherent) → 0 (rendering crisis).
**Starting value:** 10 (all practitioners). Non-practitioners do not track Coherence.

## 3.2 Coherence Reduction

Coherence loss follows the scale principle. At Object and Personal scale, the practitioner's configuration interacts shallowly — the suspension is brief, the below-the-waterline engagement is minimal, and rendering reasserts with negligible destabilisation. At Relational scale and above, the practitioner's configuration engages deeply enough that the suspension leaves a mark on their rendering.

Co-movement still fires on every operation regardless of scale (P-11). The temporal auto-effect exists at all scales — but at Object/Personal, the temporal disturbance manifests in the world (d6 consequences, narrative effects) rather than as personal Coherence loss. The practitioner's own rendering absorbs negligible impact from shallow engagements.

| Source | Coherence Loss |
|---|---|
| Object or Personal scale operation | 0 (co-movement fires but practitioner's rendering absorbs negligibly) |
| Relational scale operation | −1 |
| Territorial scale operation | −1 |
| Structural scale operation | −2 |
| FR Lock or Dissolution (any scale) | −1 additional (Lock minimum total: −2; Dissolution minimum total: −2) |
| Past-Oriented Pulling | −1 additional on top of standard Pulling cost |
| Mending | −1 (substrate engagement is inherently deep regardless of Gap scale) |
| Dissolution residue use (per use) | −1 additional (on top of operation cost) |
| History Resonance risk die (shows 1) | −1 |
| Practitioner Flashback anchoring (Game Master discretion) | −1 |
| Extended proximity to Structural-scale Gap | −1 per season |

**Campaign pacing:** A practitioner who restricts themselves to Object and Personal scale work can operate indefinitely without Coherence loss. The moment they scale up — and the campaign will pressure them to scale up — degradation begins. Over a 30-session campaign with ~10–15 Relational+ operations, the practitioner loses ~10–15 Coherence. This produces a late-campaign crisis arc if they don't take recovery seasons. This is the Einhir trajectory in miniature: small-scale work is sustainable; ambition and necessity push toward larger scales; the costs accumulate.

**Coherence loss cap per operation:** Regardless of scale, degree table outcomes, combined auto-effects, or bonus costs (FR, residue, Past-Oriented Pulling), a single operation — from Leap through resolution — cannot reduce Coherence by more than 1.
> **FR surcharge cap exemption (PP-196):** [PROVISIONAL — canon: §1.1 Inseparability, P-01] The Forced Resolution (FR) surcharge (−1 Coherence additional for Lock or Dissolution) is **exempt from the §3.2 per-operation cap.** FR operations are deeper ontological violations than Pull or Weave: Lock drives actuality to total actualization (preventing becoming); Dissolution tears the intelligible face (preventing being). The inseparability principle requires that this greater ontological depth register differently at the personal track, not be flattened by a general cap. Consistent with: Dissolution residue use is already cap-exempt (§3.4). **Revised Coherence costs for FR:**
- FR Lock or Dissolution at Object/Personal scale: −1 total (FR surcharge only; scale cost = 0, but FR surcharge applies and is not capped).
- FR Lock or Dissolution at Relational scale: −2 total (−1 scale + −1 FR; cap does not suppress the FR surcharge).
- FR Lock or Dissolution at Territorial scale: −2 total (same as Relational).
- FR Lock or Dissolution at Structural scale: −3 total (−2 scale + −1 FR).
The §3.2 per-operation cap still governs non-FR operations.
 All Coherence costs from a single operation are treated as a single event and capped at −1 total. Multiple operations in a single contact window are each capped independently.

**Interaction with degree tables:** Some operation degree tables list additional Coherence costs (e.g., "Coherence −1" on Partial, "Coherence −2" on Failure). These are outcome costs, separate from the scale-based auto-effect above. They represent the additional destabilisation from an operation going wrong — the snap-back, the misaligned interaction, the violent reassertion of rendering. At Object/Personal scale: ignore degree-table Coherence costs on Partial results (the interaction was too shallow to destabilise rendering even when it went partially wrong). Apply degree-table Coherence costs on Failure (the violent snap-back shakes rendering regardless of scale). At Relational+ scale: apply all degree-table Coherence costs as written.

## 3.3 Coherence Thresholds

| Coherence | State | Effects |
|---|---|---|
| 10–8 | Stable | No penalty. Rendering solid. The world is legible. |
| 7–5 | Dissonant | Narrative flickers: wrongness, déjà vu, events slightly out of sequence. Close Knots sense wrongness (+1 strain per 3 sessions). |
| 4–3 | Fragmented | −1D to all social rolls. −1D to Recall-based rolls. (PP-234) Game Master may present the character's recollection differently from what others remember. All Knots at wrongness pace (+1 strain per 2 sessions). +1 Ob on all Thread operations including the Leap roll (rendering reasserts more aggressively, making suspension harder). Roll Fragmented Fallout on entering this band. |
| 2 | Fractured | −2D to all social rolls. −2D to Recall-based rolls. (PP-234) All Knots at accelerated wrongness (+1 strain per session). Once per scene with Thread operation: Spirit TN 7 Ob 1 or lose 1 round to a dissociative episode. Certainty maximum reduced by 1 per Coherence level below 3. **Belief Co-Authorship begins:** Game Master presents the practitioner's shifting perceptual framework as the character's internal voice. Player must rewrite each Belief to reflect the framework in which the categories that structure consciousness are loosening. Roll Fractured Fallout on entering this band. |
| 1 | Severed | −2D social, −2D Recall. (PP-234) Dissociative episodes once per scene regardless of operations (fire at scene start, not mid-operation). Involuntary perceptual events. All Knots +2 strain per session. +2 Ob on all Thread operations including the Leap (rendering barely holds; suspension is constitutively dangerous). The practitioner's rendering is barely functional. The distinction between self and world, between human and monstrous, between actual and potential, is dissolving. Not because something evil is happening to them. Because they have been outside rendering so many times that rendering no longer holds. |
| 0 | Rendering Crisis | Campaign event. Reality as commonly rendered is no longer accessible. The practitioner's spooling is destabilised — their organic drawing-from-ground is compromised. They must resolve the crisis narratively: sustained engagement with the world's rendered state, relational anchoring, or withdrawal from practice. If unresolved by season end: Non-Player Character. |

**Game Master protocol — Dissonant entry:** When a practitioner's Coherence drops to 7 (entering Dissonant), the Game Master names this to the player explicitly: "Your Coherence is now 7 — Dissonant. Each operation at Relational+ scale costs −1 Coherence. At this pace, Fragmented is [N] operations away." This is not a mechanical rule; it is a table protocol. The practitioner's rendering is still solid at Dissonant — but the player should make informed decisions about scale from this point forward.

## 3.4 Dissolution Residue

*Replaces §5.10 (Taint track) and §5.11 (Dissolution Residue). No separate Taint track.*

Dissolution residue is compressed potential oriented toward the unintelligible ground. A practitioner may draw on it during an operation: add bonus dice equal to Potency rating (1–5) to the operation pool. These dice explode on 9–10 (volatile).

**Cost:** −1 Coherence per use (additional, on top of the operation's normal Coherence cost). Maximum one use per contact window. Same source: +1 Ob per prior use (depletion).

**Coherence cap interaction:** Residue use is a distinct Coherence event from the operation itself and is not subject to the §3.2 cap. At Object or Personal scale (base operation cost = 0): residue use costs −1 Coherence — the only cost of the operation. At Relational+ scale (base operation cost = −1, already capped): the cap absorbs the residue cost — total remains −1. In practice: residue use has a real Coherence cost when the operation would otherwise be free (Object/Personal), and no additional cost when the operation already costs −1 (Relational+). This preserves the philosophical weight — engaging with residue at shallow scale still pushes the practitioner deeper into beyond-rendering states — without stacking costs at the scales where the cap already governs.

**Why residue accelerates Coherence loss:** The residue's proximity to the ground intensifies the practitioner's exposure during contact. They are not just suspending rendering — they are suspending it while in contact with something that pulls toward the unintelligible. Each use pushes them deeper into the beyond-rendering state, and each return leaves rendering less stable.

**There is no "Taint" track.** There is no separate transformation mechanic. There is Coherence, and it degrades. What the former Taint track described — the dissolution of perceptual categories, the softening of moral distinctions, the shift toward perceiving the human/monstrous distinction as a rendering artifact — IS Coherence degradation at low levels. A practitioner at Coherence 2 has not been "corrupted." They have been outside their own consciousness so many times, and so deeply, that the categories their consciousness provides are no longer firm.

**Community Intervention:** At Coherence 4–3, another practitioner may perform corrective Weaving (Ob 3) to stabilise the degraded practitioner's configuration: +1 Coherence per season. Below Coherence 3: requires the degraded practitioner's active cooperation, which their loosened categories make increasingly unlikely — not because they resist, but because they no longer perceive the need. From their perspective, the categories that others are trying to restore are arbitrary rendering artifacts. They are not wrong. They are also not functional.

## 3.5 Recovery

Coherence does not recover passively. Recovery requires the practitioner's spooling — their organic drawing-from-ground — to reassert itself. This means stepping back from the practice that destabilised rendering.

- **Full season of non-practice (no Thread operations):** +1 Coherence. Spooling reasserts when the practitioner stops suspending it.
- **A Close Knot voluntarily anchoring through a dedicated Anchoring Scene (Bonds check TN 7, Ob 2):** +1 Coherence. The shared thread of being — the relational spooling — helps stabilise rendering. Costs the Knot +1 strain.
- **Certain Einhir techniques (Game Master discretion, late-campaign):** +1 Coherence.
- **Cannot exceed 10. Cannot be purchased with CP.**

## 3.6 Fallout Tables

*Retained from current system.*

**Fragmented Fallout (d6):**
1. You vividly remember a conversation others recall differently
2. A specific skill-memory requires Memory check Ob 2 to access correctly
3. Your sense of timing this scene is wrong — you feel you arrived at a different moment
4. Someone you have not seen recently feels as though you just spoke to them
5. Something you said this session feels like it was said last session
6. A Knot's emotional valence briefly reverses

**Fractured Fallout (d6):**
1. A vivid memory of an event the world no longer contains — you do not know it is orphaned
2. Your most recent History advancement feels uncertain — borrowed, not learned
3. A named Knot briefly does not recognise you, or vice versa. Lasts one scene.
4. You perform an action you do not remember. Game Master describes the gap.
5. Your Inspiration refresh this scene feels already spent
6. A Belief reads, briefly, as belonging to someone else

---

## 3.7 Rendering Crisis Resolution (PP-194) [PROVISIONAL]

Rendering Crisis (Coherence 0) cannot be resolved by standard recovery (§3.5). Resolution requires a structured campaign arc.

**Minimum conditions:**
1. Full season withdrawal from Thread practice (no Leap, no Thread operations).
2. Three Anchoring Scenes with Close Knots (each: Bonds check TN 7, Ob 2; failed scene costs the scene without progress).
3. Physical stability — no active siege, no ongoing catastrophe in the practitioner's territory.

**Resolution attempt** (at Accounting after conditions met):
Pool: highest Close Knot's Bonds score + number of successful Anchoring Scenes, TN 7, Ob 3.

| Degree | Outcome |
|--------|----------|
| Overwhelming | Coherence → 4. Functional. Permanent −1 Thread Sensitivity. |
| Success | Coherence → 3 (Fragmented). Minimally functional. −1 Thread Sensitivity. |
| Partial | Coherence → 1 (Severed). Another full-season arc required for further recovery. |
| Failure | No recovery. Practitioner becomes Non-Player Character at season end. |

Rendering Crisis resolution is not guaranteed. A practitioner who reaches Coherence 0 may not return.

> **Rendering Crisis arc — stability disruption (PP-202):** [PROVISIONAL] If the physical stability prerequisite fails mid-arc (siege begins, territory invaded, active catastrophe), the arc **pauses**, it does not reset. Completed Anchoring Scenes and logged non-practice seasons are retained. The arc resumes when stability is restored. The non-practice requirement extends by disrupted seasons (siege seasons do not count as non-practice even with no Thread ops — environmental Thread load of mass conflict counts against the substrate). If the practitioner performs any Thread op during a disrupted season, the non-practice requirement resets entirely.


> **GM guidance — TS 30-31 Rendering Crisis risk (PP-206):** [PROVISIONAL] Before a practitioner with Thread Sensitivity 30 or 31 begins the Rendering Crisis arc (PP-194), the GM must inform the player: Success or Overwhelming results permanently reduce Thread Sensitivity by 1. At TS 30, this reduction yields TS 29 — below the Leap minimum. The practitioner survives the crisis but loses Thread ops permanently. This is intended. Surface this before the arc begins so the player makes an informed choice: attempt resolution (risk losing Thread access) or accept NPC status directly.

> **TS 90+ Coherence 0 — Reality Strain RS cost (PP-197):** [PROVISIONAL — canon: Amendment 01 §Resonant] A practitioner who reaches Coherence 0 with Thread Sensitivity 90+ is undergoing Structural-scale self-maintenance threadwork at every moment (per Amendment 01: they substitute layer 3 for failed layer 2). This continuous Structural-scale threadwork strains the substrate exactly as the Einhir site-network did, localized to their presence. **RS cost:** −1 RS per scene in which the practitioner is actively maintaining their existence (any scene in which they are conscious and present). This cost fires at scene end, not at Accounting — it is immediate and continuous. The practitioner need not perform any deliberate Thread operations for this cost to apply; their existence is the operation. This cost is separate from and stacks with all other RS degradation sources. For TS 30–69 practitioners at Coherence 0: no reality strain RS cost (insufficient Thread Sensitivity for layer 3 self-maintenance at the required depth — they are in ontological freefall, not self-maintenance). For TS 70–89: −1 RS per session (not per scene — Structural-scale self-maintenance is possible but less continuous than Resonant). Apply during Rendering Crisis arc and after, if the practitioner remains at Coherence 0.



---

# PART FOUR: CO-MOVEMENT (VERSION C)

## 4.1 Core Principle

Every Thread operation produces consequences across all three dimensions simultaneously. The three auto-effects are three descriptions of one event — the same disturbance perceived from three angles after the practitioner returns to rendering.

The practitioner was not consciously present during contact. When they return, the consequences are already in motion. They can perceive what changed (through Thread Sensitivity perception, which is rendering). They cannot trace all consequences to their own actions because they were not there as a conscious agent when those consequences occurred.

## 4.2 Why the Actual Effect Is Random

The temporal and epistemic auto-effects are consequences the practitioner can make sense of upon returning to rendering — they follow from the intelligible aspect of what happened. The actual d6 is random because it represents consequences of the originary interaction that do not resolve into intelligible patterns. The practitioner's configuration interacted with the threads, and something happened in the actual dimension that their returned rendering cannot trace to any intention or cause. This is structurally inevitable, not a design flaw.

## 4.3 Auto-Effect Tables

*Revised from current §5.8. All "ThS" references become "Coherence." All "Thread Tension" references become "Rendering Stability" (inverted). Temporal auto-effect Coherence costs revised per §3.2 scale principle: Object/Personal operations produce narrative temporal effects but 0 personal Coherence loss; Relational+ operations produce Coherence loss per the §3.2 table. Epistemic and actual tables unchanged except terminology.*

## 4.4 History Resonance and Flashback Anchoring

*Unchanged from current R37, R38. ThS → Coherence.*

---

# PART FIVE: RENDERING STABILITY (WORLD TRACK)

## 5.1 What Rendering Stability Measures

Rendering Stability (RS) is a world-scale tracker measuring the rendered world's remaining capacity to integrate what Ein Sof provides. As Thread operations strain the substrate, as Gaps persist, as calamities occur, the world's rendering becomes less stable. Weird things happen more frequently. The fabric frays.

**Range:** 100 (fully stable) → 0 (the Rupture).
**Starting value:** Campaign-dependent. Default: Rendering Stability 60 (the Valorian peninsula's substrate is already strained from the Einhir Catastrophe, the Locked Zones, and 245 years of unaddressed damage).

## 5.2 Rendering Stability Degradation Sources

| Source | Rendering Stability Change |
|---|---|
| Thread operation (Weaving, Pulling — partial or failure) | −1 to −2 per degree table |
| Thread operation (Weaving — overwhelming at Relational+) | +1 (restoration) |
| FR Lock | −1 to −3 (immediate) + chronic drift |
| FR Dissolution | −3 to −8 |
| Past-Oriented Pulling | −3 minimum |
| Micro-Gap persisting to Accounting (normally closes same scene) | −1 |
| Gap persisting (per season) | −4 |
| Siege (per season) | −1 (concentrated suffering) |
| Einhir site under stress during siege | −1 additional |
| Mending (success/overwhelming) | +1 to +2 (restoration); multiple successful Mendings in a season stack independently at Accounting |
| Community Weaving (Revolution success) | +1 to +2 |
| Southernmost expedition Mending | +2 permanent per successful season |
| Board game Weave order (success) | +1 |
| Board game Mend order (success) | +1 |
| Board game Weave order (failure) | −1 |
| Winter annual drift | −1 |

## 5.3 Rendering Stability Thresholds

> **Rendering Stability threshold cumulation (P-14):** Rendering Stability threshold effects are cumulative. Each lower band includes all effects from higher bands: - **Fractured (39–20)** includes all Fragile effects (spontaneous Shifting Objects, +1 Ob in affected territories) PLUS Fractured-specific effects (spontaneous Gaps, Monstrous Incursion risk, rendering failures for non-practitioners). - **Critical (19–1)** includes all Fragile + Fractured effects PLUS Crit

**Threshold timing:** Rendering Stability threshold effects activate and deactivate at Accounting (season end), not mid-scene. If Rendering Stability crosses a threshold boundary during play — due to a Thread operation, Mending, or other mid-scene change — the new effects do not apply until the following Accounting. Exception: the immediate consequences listed in operation degree tables (e.g., "Shifting Object forms," "Gap opens") resolve immediately as written. Only the persistent threshold-band effects (spontaneous Gaps per season, worldwide +1 Ob, faction Stability checks) are Accounting-gated.

> **Geographic graduation (ED-302):** The threshold effects below are not global. They radiate outward from Askeheim (T15) by node distance on the territory adjacency graph. As RS drops, effects reach further from the wound. The full RS-band × node-distance matrix is defined in `designs/setting/calamity_radiation.md`. The table below describes maximum-severity effects (i.e., effects at Askeheim itself and in territories where the radiation has reached). At RS ≤ 10, a one-time Southernmost Surge escalates effects one band worse within node distance 2 for one season.

| Rendering Stability | State | World Effects |
|---|---|---|
| 100–80 | Stable | No unusual phenomena. Substrate sound. |
| 79–60 | Strained | Occasional wrongness in territories with Thread history. Non-practitioners with Thread Sensitivity 10+ may sense unease near old operation sites. |
| 59–40 | Fragile | Shifting Objects form spontaneously in high-traffic Thread territories. One random Shifting Object per season at Accounting. Thread operations +1 Ob in affected territories. |
| 39–20 | Fractured | Gaps may open spontaneously (1d10 per season at Accounting; on 1–2: Gap in territory with lowest Prosperity). Monstrous Incursion risk in all territories with existing Gaps. Non-practitioners experience rendering failures — inconsistent memories, déjà vu, objects in wrong places. |
| 19–1 | Critical | As Fractured, plus: spontaneous Gaps on 1–4 (doubled risk). All Thread operations +1 Ob worldwide (the substrate resists manipulation). Seasonal Stability checks for all factions at Ob 1 (institutional rendering begins failing) — failure produces Mandate −1 for that faction (minimum 0). At Mandate 0, failure instead produces Faction Fracture: one sub-faction splinters off as a new minor faction (Game Master determines composition and goals). Mandate cannot go below 0. Discovery Events become common — Thread Sensitivity growth checks for any non-practitioner who witnesses a rendering failure. NPCs with coup or succession trigger conditions (flagged in design files) treat Rendering Stability ≤ 10 as +1 to their trigger check pool (institutional rendering failure accelerates political instability). |
| 0 | The Rupture | Rendered reality fails. Campaign ends in catastrophe. No faction wins. The Ein Sof's fullness overwhelms the rendered world's capacity. What emerges is not destruction but excess — too much being for consciousness to render. The world does not end. It becomes unintelligible. |

**Design note — Rendering Stability Critical as endgame:** Once Rendering Stability enters the Critical band (19–1), the campaign is in a 2–4 season endgame without dramatic intervention. At Rendering Stability 1, the endgame trap is complete: almost every Thread operation carries Rupture risk on Failure, but not operating also reaches Rupture within 1–3 seasons from Lock drift and winter. The only structural exit requires: remove all active Locks (eliminates drift), Mend all active Gaps (eliminates per-season Rendering Stability loss), then operate exclusively at Object/Personal scale until Rendering Stability recovers via successful Mending. Each Mending attempt at Rendering Stability 1 risks Rupture on Failure (~17–34% success at best). This is the Einhir Catastrophe replicated mechanically — they reached this point, and there was no escape. The game does not provide a clean rescue from Rendering Stability 1. It provides a narrow, difficult path that requires practitioner cooperation across faction lines and accepts that Rupture is a legitimate campaign ending. The convergence of Lock drift, Gap persistence, spontaneous Gap formation, and seasonal operation failures produces net Rendering Stability losses of 8–15 per season even with active Mending. The seasonal cap (±10) prevents single-Accounting Rupture but cannot arrest multi-season terminal decline. Rendering Stability Critical is the point of no return: the table must coordinate across faction lines to stabilise the world, or accept that the campaign ends in the Rupture. This is designed. The Einhir reached the same point.

## 5.4 Rendering Stability in Board Game

Rendering Stability replaces Thread Tension on the board game track. Invert all Thread Tension references: where Thread Tension went up, Rendering Stability goes down. Shared loss condition: Rendering Stability reaches 0.

**Rendering Stability is hidden from players by default.** The Investigate Thread order (Intelligence vs Ob 3) reveals the current Rendering Stability value. Overwhelming: also reveals which territories have Gaps. Players know the world is degrading (they see the threshold effects) but do not know the exact number without investigation.

## 5.5 Rendering Stability in Hybrid

Rendering Stability advances at Accounting (Cascade Phase). Both TTRPG-sourced changes (from Personal Phase Thread operations) and board-game-sourced changes (from Strategic Phase orders) are applied at the same Accounting. No double-counting; seasonal cap on Rendering Stability change is ±10 per season.

---

# PART SIX: THREADCUT BEINGS

## 6.1 Ontological Status

Organic beings persist through continuous Ein Sof spooling. A threadcut being does not spool. It maintains itself through continuous Thread work — actively sustaining its own actualization, temporality, and intelligibility at every moment. Where an organic being IS through the ground's continuous provision, a threadcut being IS through its own continuous effort. It radically is without becoming.

In terms of the Leap: organic beings render. A threadcut being's existence IS a permanent Leap — a permanent state of Being beyond ordinary rendering, sustained by continuous originary intentionality directed at self-maintenance. The threadcut being never returns to ordinary rendering because it has no ordinary rendering to return to. This is its paradox and its cost.

> **Gap-severity classification (ED-302):** Threadcut beings are classified by the Gap severity that produced them: **Micro-Gap emergent** (Thread Sensitivity 20–40, hours-to-days duration, non-combat), **Standard Gap emergent** (Thread Sensitivity 50–70, seasons duration, combat-capable), **Catastrophic Gap emergent** (Thread Sensitivity 80+, years-to-indefinite, campaign-level entity). Full classification table and emergence conditions in `designs/setting/calamity_radiation.md`.

## 6.2 Observer-Dependent Rendering

Each observer perceives a threadcut being at their own rendering ceiling.

| Observer Thread Sensitivity | Perception |
|---|---|
| 0–9 | Nothing, or vague unease. |
| 10–29 | A presence. Unstable image. Details shift. |
| 30–49 | Coherent figure, but features approximate. Real but wrong in inarticulable ways. |
| 50–69 | Stable perception. The being is fully rendered. Its continuous self-sustaining Thread work visible as a hum of operation. |
| 70+ | Full perception. The observer perceives the being's self-rendering effort — the continuous work that holds it in place. The being is something that holds itself up rather than something held up. |

### Rendering Beyond Observer Capacity

A threadcut being may render itself more intensely — making itself more present, more visible, more coherent than any observer's ceiling supports. Solmund did this: his works were ineffable and miraculous because he rendered himself at a level that exceeded what observers could hold.

**Cost:** Each scene of beyond-ceiling rendering: +1 **Rendering Strain** (cumulative). When Rendering Strain equals Health: De-actualisation begins.

The more intensely the being renders itself, the sooner it ceases to be.

## 6.3 Mechanical Distinctions

- **Past-Oriented Pulling:** Auto-produces a Gap. No temporal thread to pull — no accumulated past, no spooled depth.
- **Wounds:** Each costs 1 additional point of sustained Thread work rather than conventional Ob penalty.
- **Coherence track:** Does not apply. Threadcut beings do not render — they have no rendering to destabilise.
- **External Thread operations:** A threadcut being may direct their originary intentionality toward external threads rather than self-maintenance. No Leap is required — they are already in the originary state that organic practitioners must Leap to reach. Declare operation type and target; roll standard operation pool (Spirit + History + Thread Pool Score) against standard Ob. Cost: each external Thread operation adds +1 Rendering Strain (directing intentionality outward strains the continuous self-maintenance that constitutes the being's existence). A threadcut being performing external operations accelerates their own De-Actualisation. This is the Solmund dilemma: the being capable of Structural intervention faces the choice between acting (and beginning to cease) and withholding (and preserving existence at the cost of inaction).
- **Diagnosis:** Reveals the temporal paradox. No accumulated past. No natural trajectory. Something held rather than persisting.

## 6.4 De-Actualisation

When Rendering Strain equals Health, or Wounds reach **Rendering Threshold** (Health ÷ 2), the being can no longer sustain self-rendering.

**Triggers (independent):** Both triggers independently initiate De-Actualisation — whichever is reached first activates the sequence. If both cross simultaneously, the sequence begins once.

**Sequence:**
- **Round 1:** Intelligible face dissolving. Thread Sensitivity 30+ observers perceive loss of coherence. All operations +2 Ob. May attempt stabilisation: Weaving on itself (standard pool vs Ob = Wounds + Rendering Strain).
- **Round 2:** Perceivable only by Thread Sensitivity 50+. Operations +4 Ob. Second stabilisation attempt possible.
- **Round 3+:** Configuration returns to the unintelligible ground. Not death — cessation of self-rendering. Micro-Gap forms, closes within scene. Dissolution residue remains.

**Voluntary cessation:** The being may choose to stop sustaining itself at any time. This is Solmund's path. De-actualisation proceeds without Ob penalties — the being is not struggling but letting go.

---

# PART SEVEN: CROSS-MODE IMPLICATIONS

## 7.1 Board Game

### New Order: Mend

Available to any faction with an affiliated Thread Sensitivity 50+ character, or Revolution (via Community Mending).

**Revolution Community Mending prerequisite:** Revolution must have Mandate ≥ 1 to perform Community Mending. At Mandate 0, the community substrate has fractured and Community Mending is unavailable. Note: this creates a late-campaign feedback loop — Rendering Stability degradation reduces Stability, Stability failures reduce Mandate, Mandate 0 blocks Community Mending, Rendering Stability continues falling. The Revolution's Thread contribution fails precisely when the world needs it most. (Cross-reference: Community Weaving constraint defined in batch_d_designs.md §G-049.)

| Order | Roll | Effect |
|---|---|---|
| **Mend** | Intelligence (or faction-specific) vs Ob by Gap category (see below) | Success: Gap closed. Rendering Stability +1. Failure: Rendering Stability −1. Draw Co-Movement Card. |

**Board game Mend Ob** (lower than TTRPG — faction-level effort abstracts collective resources):

| Gap Category | Board Game Ob |
|---|---|
| Shifting Object | 1 |
| Standard Gap | 2 |
| Entrenched Gap | 3 |
| Catastrophic Gap | 4 |

### Revised Co-Movement Card Deck (18 cards)

Cards 1–15: retained (all Thread Tension references become Rendering Stability, inverted).
Cards 16–18 added:

16. **Substrate Settling** — Mended territory: all Thread operations −1 Ob next season.
17. **Scar Trace** — Mended territory retains visible Thread scar. Church Theocracy Counter +1. No Rendering Stability change.
18. **Residue Condensation** — dissolution residue forms at Mending site. Niflhel may harvest.

### Lock Chronic Drift

Territories with Locked configurations: Rendering Stability −1/season at Accounting. Shown on territory status card. Clearing requires Pull or Weave order targeting the Lock.

### Rendering Stability Track

Replaces Thread Tension track on board. Runs 100→0. Hidden by default (Investigate Thread reveals). Shared loss at 0.

## 7.2 Hybrid Mode
> **Coherence initialization — BG to Hybrid (PP-200):** [PROVISIONAL — canon: Amendment 01 §3] Coherence starts at 10 for all organic practitioners (Amendment 01: Coherence measures layer 2 integrity, which is fully intact before any Leap). In Board Game mode, Coherence is not tracked (practitioners are abstracted as faction assets; no Leaps occur). When a campaign transitions to Hybrid mode and a PC practitioner enters their first Personal Phase: **Coherence = 10** (no Leaps have occurred in BG mode; layer 2 is intact). After the first Personal Phase, Coherence is tracked explicitly and carries forward between all subsequent Personal Phases. If the campaign has had prior Personal Phases (e.g., after a previous Hybrid activation), use the practitioner's last recorded Coherence value. If no prior value exists: Coherence = 10. GMs should note each PC practitioner's Coherence on the Hybrid tracking sheet at the end of every Personal Phase.

> **Hybrid Coherence pacing guidance (PP-207):** [PROVISIONAL] Design intent for sustainable Hybrid campaign pacing: a practitioner who leads Thread orders should average **one Personal Phase Relational+ operation and one Strategic Phase leadership declaration per season** to reach Rendering Crisis at approximately session 10 (the intended late-campaign arc). Two Personal Phase Relational+ ops per session combined with two Strategic Phase declarations per session produces Rendering Crisis by session 3-5, which destroys the practitioner before the campaign develops. GMs should treat two Strategic Phase declarations per session as a high-stakes deviation requiring narrative justification, not routine play.



- **Mending:** Personal Phase = full TTRPG rules. Strategic Phase = Mend order. Both count toward Rendering Stability.
- **Coherence:** Tracked per Player Character practitioner during Personal Phase. Strategic Phase Thread orders: −1 Coherence only if a Player Character practitioner narratively leads the operation.
> **Hybrid Coherence declaration rule (PP-198):** [PROVISIONAL — canon: Amendment 01 §2, §3] Coherence cost in Hybrid Strategic Phase is paid by the Player Character who **declares leadership at Phase 1 of the Cascade Phase** (committing to have performed the Leap for that order). This declaration is binary and mechanical — it is not a narrative judgment. The declaring PC's layer 2 was suspended for that order; therefore their Coherence decrements. If no PC declares leadership at Phase 1: no Coherence cost applies to any PC for that order (the order was executed by Non-Player Character practitioners). Multiple PCs cannot co-declare leadership for a single order; only the declared PC pays. Replace all instances of "narratively leads" in Hybrid Coherence rules with "declared leadership at Phase 1 of Cascade Phase."
 Leadership is declared at the start of Cascade Phase — one Player Character per order. If no Player Character declares leadership, no Coherence cost is paid (the order was Non-Player Character-led). Multiple PCs cannot co-lead a single order; the leading Player Character pays the full Coherence cost alone.
- **Lock chronic effects:** TTRPG Lock registered on territory card at Cascade Phase. Drift begins next Accounting.
- **Rendering Stability changes:** Both Personal and Strategic Phase changes applied at Accounting. Seasonal cap: ±10 net (the cap applies to the net Rendering Stability change after all sources — positive and negative — are resolved at Accounting).
- **Cross-phase opposing operations:** If a TTRPG Thread operation (Personal Phase) and a board game Thread order (Strategic Phase) target the same configuration with opposing intentionalities, flag at Personal Phase declaration. Both are held and resolved simultaneously at Cascade Phase using the opposing operations procedure (§9.13). The TTRPG practitioner's roll from Personal Phase stands as their input; the board game order roll is made at Cascade Phase.

> **Hybrid co-declaration tie-break (PP-205):** [PROVISIONAL] If two or more Player Characters simultaneously declare leadership for the same Strategic Phase Thread order at Phase 1 of the Cascade Phase, the declaration resolves as follows: (1) The PC with the highest Thread Sensitivity declares. (2) If Thread Sensitivity is tied: the PC who declared first at the table (in real-world turn order, not game priority order) declares. (3) The non-declaring PC's declaration is void; they pay no Coherence cost for that order. This ruling applies only to simultaneous declarations. If PCs choose to negotiate among themselves before Phase 1 closes, that negotiation determines the declarer with no tie-break needed.


## 7.3 Updated Mode Branching

| Rule | TTRPG | Board Game | Hybrid |
|---|---|---|---|
| Thread operations | Weaving, Pulling, Mending, Lock, Dissolution — personal-scale | Weave, Mend, Investigate, Harvest — faction-scale | Personal Phase: TTRPG. Strategic Phase: board game. |
| Gap closure | Mending (Att + Focus + Thread Pool Score) | Mend order | TTRPG Mending or Mend order |
| Co-movement | Version C (temporal + epistemic auto, actual d6) | Co-Movement Cards (18) | Personal: Version C. Strategic: Cards. |
| Practitioner degradation | Coherence 10→0 | Not tracked | Coherence during Personal Phase |
| World stability | Rendering Stability 100→0 at seasonal accounting | Rendering Stability 100→0 at Accounting | Rendering Stability at Cascade Phase Accounting |
| Lock chronic | Game Master tracks; Rendering Stability drift at accounting | Territory card: Rendering Stability −1/season | TTRPG → territory card at Cascade |

---

# PART EIGHT: INTERDEPENDENCY MAP

## 8.1 Systems Replaced

| Old System | Replaced By | Scope |
|---|---|---|
| Intelligibility (§4.5, 10→0) | Coherence (10→0) | All character sheets, all Thread operation tables |
| ThS / CD (§5.9, 20→0) | Coherence (10→0) | Campaign tracking eliminated as separate system |
| Taint (§5.10, 0→10) | Coherence (low-end effects) | No separate track. Dissolution residue = accelerated Coherence loss. |
| Thread Tension (Thread Tension, 0→100) | Rendering Stability (Rendering Stability, 100→0) | Board game track, all threshold tables, all operation consequence tables |
| Gap closure via FR Dissolution | Mending (new operation) | §5.13, board game orders, Southernmost expedition |
| "Solmund" (all references) | "Solmund" | All files (logged for Haiku batch) |
| AG calendar | AS calendar | All files (logged for Haiku batch) |
| "Epistemic seduction" | Cut — Coherence degradation | All references |
| "Taint" | Cut — Coherence degradation | All references |

## 8.2 Systems Unchanged

- Core engine (dice, TN, Ob, degrees)
- Combat engine (pool split, Wounds, Health)
- Social system (Composure, Debates, Appeals)
- Faction system (Domain Actions, attributes, accounting)
- Political axes, mass combat, siege
- Histories, Beliefs, Inspirations
- Circles, Resources
- Clocks (Theocracy Counter, Institutional Pressure) — unchanged. Rendering Stability replaces Thread Tension as the third clock.
- Knot mechanics — strain sources consolidated but mechanical structure unchanged

## 8.3 Implementation Sequence

| Step | Task | Model |
|---|---|---|
| 1 | Simulate Coherence 10→0 degradation rates across archetype campaigns | Sonnet |
| 2 | Simulate FR Lock chronic Rendering Stability drift across 10-season campaigns | Sonnet |
| 3 | Simulate Mending pool (Att + Focus + Thread Pool Score) probability curves | Sonnet |
| 4 | Simulate over-actualisation impact on practitioner gameplay | Sonnet |
| 5 | Stress test Diagnosis-before-Leap sequence (timing in combat) | Sonnet |
| 6 | Stress test threadcut de-actualisation | Sonnet |
| 7 | Compile into Thread Operations chapter (new Stage 3) | Sonnet |
| 8 | Update board game Thread orders, Co-Movement deck, Rendering Stability track | Haiku |
| 9 | Update hybrid mode branching catalogue | Haiku |
| 10 | Solmund rename + AG→AS + Church rename (all files) | Haiku |
| 11 | Canon guard pass on complete redesign | Sonnet |

> **Opposing simultaneous ops (P-24):** When two practitioners in contact target the same configuration with opposing intentionalities (e.g., one Weaving, one Pulling; one Mending, one disrupting), both roll their respective pools against their respective Obs. | Outcome | Resolution | |---|---| | Both succeed | The thread receives contradictory direction. It oscillates. A **Shifting Object** forms at the thread's scale (per §9.5). Both 