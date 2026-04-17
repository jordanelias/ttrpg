# VALORIA — Thread Horizontal Integration Specification
## ED-673 through ED-681 | Status: CANONICAL
## Date: 2026-04-17
## Scope: All remaining cross-system Thread fire paths, editorial resolutions, and patches
## Depends: rs_budget.md (ED-668), wc_survival_spine.md (ED-669), npc_behavior_v30 §3.4/§4.3 (ED-670–672)
## Resolves: All open questions from thread_constitutive_integration_analysis_v2.md

---

## EDITORIAL RESOLUTIONS (all 7 open questions)

| # | Question | Resolution | Rationale |
|---|---|---|---|
| 1 | Scar severity × Certainty scaling | **Yes.** C5: +1 Scar. C0: −1 Scar. C2–3: standard. | Already applied in npc_behavior_v30 §3.4. Follows Certainty Track's own mechanical bonus model. |
| 2 | Player Conviction × Thread events | **Yes.** Spirit TN 7 Ob 1. Failure: active Conviction shaken for 1 season. | Already applied in npc_behavior_v30 §3.4 (ED-671). Player parity with NPC Scar system. |
| 3 | Battle-driven TS development | **No separate mechanic.** Radiation model sufficient. Discovery Events at RS Critical/Proximity 3 (calamity_radiation_v30) covers environmental TS growth. Battle-specific TS growth would produce too many practitioners in sustained war campaigns, undermining Thread scarcity. | Per calamity_radiation_v30: TS growth is environmental (substrate instability) not experiential (battlefield trauma). |
| 4 | NPC AI formalization | **Direct priority tree amendments.** Arc register vectors translated into NPC faction priority tree gates. | Already started with npc_behavior_v30 §4.3 Coherence AI. Remaining: Thread warfare doctrine as priority tree amendments (§THREAD WARFARE AI below). |
| 5 | Niflhel Harvest | **Confirmed.** Harvest = Dissolution Residue collection. Niflhel is the accelerationist faction. | Resolved in wc_survival_spine.md. Quiet One arc (arc_expansion_v1) is the behavioral specification. |
| 6 | Settlement Thread granularity | **Per-territory (radiation matrix).** Not per-settlement. | Calamity radiation is graduated by proximity (per-territory). Adding per-settlement would multiply granularity without proportional strategic depth. Settlement Order effects fire when territory-level radiation triggers. |
| 7 | Integration approach | **Hybrid.** Cross-system fires in this document. In-place patches to target documents for mechanical specifications. | Follows existing pattern: Certainty Track in params_core, TC trigger in params_threadwork, Domain Echo in scale_transitions. New fire paths specified here; inserted into target documents by propagation. |

---

## ED-673: Thread Domain Echo Pathway

**Target:** designs/hybrid/scale_transitions_v30.md — insert after §5.5 Accord Domain Echo

**Specification:**

### §5.6 Thread Domain Echo (ED-673)

Thread events produce Domain Echo to faction stats when they meet Thread Significance (distinct from general Sufficient Scope):

**Thread Domain Echo fires when:**
- (a) Thread operation produces RS change ≥ 1, OR
- (b) Thread operation is witnessed by NPC with Conviction engaged and Scar fires (per npc_behavior_v30 §3.4), OR
- (c) Thread operation creates or destroys a Gap, Lock, or Knot at Territorial+ scale

**Effect:** ±1 to most relevant faction stat, determined by political context.

| Thread Event | Affected Stat | Direction |
|---|---|---|
| Dissolution Success (any scale) | Controlling faction Stability | −1 (violence against substrate) |
| Mending Success (territorial+) | Controlling faction Mandate | +1 (governance of substrate) |
| Gap creation | Controlling faction Stability | −1 |
| Lock creation (unauthorized) | Controlling faction Mandate | −1 (governance challenge) |
| Public Thread operation, Church territory | Church Mandate | −1 (authority challenged) |
| Public Thread operation, Varfell territory, VTM ≥ 3 | Varfell Mandate | +1 (institutional validation) |

**Timing:** Queued to next Accounting (same as Accord Domain Echo). Does not fire mid-scene.

**Cap:** Maximum 1 Thread Domain Echo per scene per faction (mirrors existing PP-329 rule).

**Model:** Extends Epistemic Auto-Effect TC Trigger (PP-182) from Church-specific to all factions. The TC trigger remains independent — Thread Domain Echo and TC trigger may both fire from the same event.

---

## ED-674: Scene Slate Thread-State Factor

**Target:** designs/systems/player_agency_v30.md §4.2 Generation Algorithm — insert as Step 2b

**Specification:**

### Step 2b — Thread-State Scenes (ED-674)

After Step 2 (Priority scenes from active arcs), check local thread state:

| Condition | Scene Added | Priority |
|---|---|---|
| RS ≤ 20 (Critical) in current territory | Thread Crisis scene: substrate instability manifests. Content from calamity_radiation_v30 per territory proximity. | Priority 1 (mandatory) |
| Active Gap in current territory | Investigation/Mending opportunity: scene at Gap site. | Priority 2 |
| Active Lock in current territory | Governance rigidity scene: a policy or relationship frozen by the Lock manifests as bureaucratic/social obstruction. | Priority 3 |
| RS dropped below threshold since last Slate | Threshold-crossing scene: the world visibly changes. Content per calamity_radiation_v30 band. | Priority 2 |
| WC advanced since last Slate | Warden cooperation scene: new Thread resources available, new relationships with Warden NPCs. | Priority 3 |

**Maximum 1 Thread-State scene per Slate.** If multiple conditions qualify, highest priority fires.

**Model:** Extends existing Scene Slate Priority system. Thread-State scenes use the same Priority 1/2/3 structure as arc-driven and world-state scenes.

---

## ED-675: Settlement Thread Environment

**Target:** designs/systems/settlement_layer_v30.md — insert after §4.3 Settlement Events

**Specification:**

### §4.4 Settlement Thread Environment (ED-675)

Settlement effects fire when territory-level Thread events occur (per calamity_radiation_v30 matrix):

| Territory Thread Event | Settlement Effect |
|---|---|
| Spontaneous Gap fires in territory (radiation matrix) | Lowest-Order settlement in territory: Order −1 |
| Spontaneous Shifting Object fires | No settlement stat change. Narrative: strange events reported. |
| Territory enters new RS band (downward) | All settlements in territory: 1 season of unrest (all governance actions +1 Ob next season) |
| Thread operation (Dissolution/Lock) occurs at a specific settlement | That settlement: Order −1. If settlement has Warden management: Order change waived (Wardens stabilize). |
| Mending restores Gap in territory | Highest-Order settlement in territory: Order +1 (relief) |

**Granularity:** Per-territory, not per-settlement. Calamity radiation matrix provides the trigger; settlement stats receive the effect.

**Warden Outpost exception (existing):** Warden-managed settlements detect RS effects 1 band earlier. This advantage now also grants the settlement immunity to Thread-event Order loss (Wardens stabilize the local environment).

---

## ED-676: CV Movement from Visible Thread Operations

**Target:** designs/conviction_track/conviction_track_v30.md — insert after §1.3 Calamity Drift

**Specification:**

### §1.4 Thread Operation CV Drift (ED-676)

Visible Thread operations in a territory shift CV:

| Thread Event | CV Change | Condition |
|---|---|---|
| Public Dissolution | CV −1 | Witnesses present. Thread reality becomes undeniable. |
| Public Mending | No change | Ambiguous: Church claims miracle; practitioners claim mastery. Neither framing shifts CV definitively. |
| Public Weaving (non-harmful) | CV −0.5 (round at Accounting) | Mild Thread exposure. Accumulates slowly. |
| Visible Rendering Crisis | CV +1 | Thread danger reinforces Church framework. Fear response. |
| Monstrous Incursion (spontaneous, radiation) | CV −1 | Substrate instability is visible proof of Thread reality beyond Church explanation. |

**Scope:** "Public" = witnessed by non-practitioner NPCs. Operations concealed per threadwork_v30 §2.3 concealment roll do not trigger CV drift.

**Interaction with Calamity Drift (§1.3):** CV Thread Drift stacks with Calamity Drift. Both fire at Accounting. At RS Critical, territories near Askeheim experience both drains — Calamity Drift from RS degradation AND Thread Drift from spontaneous manifestations.

**Cap:** Maximum CV ±2 per territory per season from Thread sources (Calamity Drift + Thread Operation Drift combined).

---

## ED-677: Thread Perception Extension

**Target:** designs/ttrpg/threadwork_v30.md §2.3 — extend existing visibility table

**Specification:**

### Rendered-Level Thread Event Visibility (ED-677)

Extension of §2.3 to cover rendered-level events (not practitioner operations):

| Observer TS | Combat Wound | Death | Mass Casualty | Composure 0 (Contest) | Gap Manifestation | Rendering Crisis |
|---|---|---|---|---|---|---|
| 0–9 | Nothing | Nothing | Nothing | Nothing | Nothing | Vague wrongness |
| 10–29 | Vague unease at violence | Sense of loss beyond normal grief | Deep wrongness; nightmares for days | Nothing | Unease near site | Overwhelming wrongness; Certainty check |
| 30–49 | Perceives thread disruption at wound site | Perceives configuration ceasing to cohere | Senses mass thread disruption; direction identifiable | Perceives epistemic structure straining | Perceives absence; Gap topology partially readable | Perceives full crisis — practitioner's substrate state visible |
| 50–69 | Identifies wound depth (surface vs structural) | Perceives dissolution of thread-configuration | Identifies scope and approximate casualties through substrate reading | Identifies which epistemic dimension is under pressure | Full Gap reading: original configuration reconstructible (forensic) | Perceives crisis cause; can identify which operation produced it |
| 70+ | Full structural perception of wound's thread-state | Perceives the dying configuration's complete thread-state | Perceives every individual disruption in the mass event | Full epistemic structure of both parties visible | Full forensic reading + temporal trace | Can intervene: Anchoring Scene assistance possible |

**No mechanical changes.** This table provides narrative and investigative information only. Does not modify combat, contest, or Thread operation mechanics.

**Integration with fieldwork:** Thread-Read of rendered-level events uses this table to determine what evidence is available at each TS level. Supplements §4.5 Thread-Read evidence quality.

---

## ED-678: Lifepath → Starting TS/Certainty Derivation

**Target:** designs/characters/character_histories_v30.md — insert after Stage 3 Vocation

**Specification:**

### Starting Certainty and Thread Sensitivity from Lifepath (ED-678)

| Lifepath Element | Certainty Modifier | TS Modifier |
|---|---|---|
| **Origin:** Church Territory (1E) | +1 (toward 5) | 0 |
| **Origin:** Southern Einhir (1D) | −1 (toward 0) | +5 baseline |
| **Origin:** Border Settlement (1G) | 0 | +2 (proximity to substrate instability) |
| **Origin:** Displaced (1H) | 0 | +1 |
| **Formation:** Church Schooling (2A) | +1 (toward 5) | 0 |
| **Formation:** Practitioner Mentorship (2F) | −2 (toward 0) | +10 (post-First Leap) |
| **Formation:** Monastic Seclusion (2G) | +1 (toward 5) | 0 |
| **Vocation:** Any Church Vocation | +1 (toward 5) | 0 |
| **Vocation:** Any Varfell Vocation (Thread-adjacent) | −1 (toward 0) | +5 |
| **Vocation:** Any Guild/Crown/Hafenmark Vocation | 0 | 0 |

**Base:** Certainty 4 (average Valorian). TS 0 (non-practitioner).

**Calculation:** Apply all modifiers. Certainty clamped to 0–5. TS clamped to 0 (minimum); no maximum from lifepath (TS 30+ requires First Leap during play, not lifepath — except Formation 2F which represents pre-game First Leap).

**Consistency with params_core:** Starting Certainty values in params_core §Certainty Track are now derived from this table rather than assigned ad hoc. Formation 2F (Practitioner Mentorship) produces Certainty 2 (4 − 2 = 2), matching params_core "Post-First Leap practitioner: 2."

---

## ED-679: Thread Warfare NPC AI Doctrine

**Target:** designs/systems/npc_behavior_v30.md §8 BG Priority Trees — amend relevant faction trees

**Specification:**

### Thread Warfare Doctrine — Priority Tree Amendments (ED-679)

**All Thread-aware factions (Varfell, Niflhel, Wardens):**
- Priority gate: If RS ≤ 25, reduce all offensive Thread operations to defensive only (Mending, defensive Weaving). RS preservation overrides tactical advantage.
- Exception: Niflhel at RS ≤ 25 with Harvest active → RS-monitoring subroutine gates Harvest intensity to 1 Dissolution/season maximum.

**Varfell §8.5 Amendment:**
- Priority 2 addition: If Coherence ≤ 5 on primary practitioner → defer Thread operations 1 season (per §4.3 Coherence AI).
- Priority 5 addition: If RS ≤ 30 AND enemy faction has practitioner-general → Thread brinksmanship eligible: present high-value target to bait enemy into risky operations. Brinksmanship requires Intel ≥ 4 to identify enemy practitioner.

**Niflhel §8.8 Amendment:**
- Priority 3 addition: Harvest intensity gate: if RS ≤ 30, Harvest = 1 Dissolution/season max. If RS ≤ 20, Harvest suspended. Quiet One Arc B/C (arc_expansion_v1) provides thresholds.
- Priority 5 addition: Lock-and-cede doctrine: if Niflhel-aligned territory is about to be conquered, place Locks on critical configurations before ceding. Requires available practitioner with Coherence ≥ 5.

**Edeyja/Wardens §8.10 Amendment:**
- Priority 1: RS preservation. If RS ≤ 30, Warden actions = Mending only (existing). NEW: If Edeyja Coherence ≤ 5, Wardens request practitioner assistance from allied factions (triggers outreach to Varfell or player).
- Priority 2 addition: Coherence gate per §4.3 applied to all Warden practitioners.

**Church §8.2 — No amendment.** Church does not use Thread operations. Church priority tree remains Thread-resistant by design (Faith Conviction, Devout general restriction).

---

## ED-680: Case Board Dual-Depth Overlay

**Target:** designs/systems/investigation_systems_proposal_2026-04-15.md §The Case Board

**Specification:**

### Case Board Thread Layer (ED-680)

When a PC with TS ≥ 30 opens the Case Board, a toggle enables the Thread Layer:

**Thread Layer ON:** Each evidence node shows dual-depth information:
- **Rendered level** (always visible): physical evidence, testimony, documents
- **Substrate level** (TS-gated): thread-configuration data from Thread-Read operations

Evidence from Thread-Read and evidence from mundane investigation that describe the same event are linked. The link is the constitutive insight: "the bloodstain on the floor (rendered) and the thread disruption I perceived (substrate) are the same event at different depths."

**Mechanical effect:** When a player connects rendered evidence to substrate evidence describing the same event, the Evidence Track advances +1 (insight bonus). Maximum 1 insight bonus per investigation.

**TS gate:** Thread Layer only available at TS ≥ 30. Below TS 30, substrate evidence appears as "something is wrong here but I cannot perceive what" — no linkage possible.

---

## ED-681: Rendering Crisis Narrative Structure

**Target:** designs/ttrpg/threadwork_v30.md §3.7 — expand existing specification

**Specification:**

### Rendering Crisis — Designed Narrative Beats (ED-681)

The existing specification (1 season withdrawal + 3 Anchoring Scenes + resolution roll) is a mechanical checklist. For videogame implementation, each beat needs scene structure:

**Beat 1 — Withdrawal Scene:** Practitioner unable to sustain normal rendering. Scene structure: the world appears wrong. Colors desaturate. Sounds echo. NPCs' words arrive with delay. The practitioner knows they are perceiving the thread-substrate without the rendering filter. Mechanical: no rolls. Pure narrative. Companion Commentary fires if companion present (bridge_part1_revisions B.3.3).

**Beat 2 — Anchoring Scene 1 (Knot):** A Knot-bonded NPC arrives. The practitioner perceives them simultaneously as rendered person and thread-configuration. Scene structure: conversation where the NPC's words are both meaningful (rendered) and structurally patterned (substrate). Mechanical: Spirit check TN 7 Ob 1. Success: Coherence +1. Failure: no change; NPC receives Knot Strain +1.

**Beat 3 — Anchoring Scene 2 (Place):** The practitioner visits a location with personal significance (determined by lifepath — hometown, formation site, or vocation location from character_histories_v30). Scene structure: the place's familiar configuration provides rendering reference. Mechanical: Spirit check TN 7 Ob 2. Success: Coherence +1. Failure: the practitioner perceives the place's thread-history (involuntary Thread-Read, co-movement fires).

**Beat 4 — Anchoring Scene 3 (Choice):** The practitioner confronts the epistemic seduction question: do I want to return to rendering? Scene structure: the practitioner has a moment of full substrate perception — the world as it actually is, not as rendering presents it. The choice is: step back (accept rendering's limitations, accept being a rendered being) or step forward (accept deeper substrate engagement, accept further Coherence risk). Mechanical: This is the resolution roll. Spirit + Focus, TN 7, Ob 2. Overwhelming: +2 Coherence, −1 TS (the cost of pulling back). Success: +1 Coherence. Partial: no change. Failure: no Coherence recovery; Coherence floor at current value for 1 additional season.

**Career rhythm:** The crisis is not punishment. It is the practitioner's existential season — spring/summer of operations, autumn of burnout, winter of crisis, spring of recovery. The UI should present this as a natural arc, not a failure state.

---

## PROPAGATION MAP

| ED | Target Document | Section | Action |
|---|---|---|---|
| ED-668 | references/rs_budget.md | New file | Create |
| ED-669 | references/wc_survival_spine.md | New file | Create |
| ED-673 | designs/hybrid/scale_transitions_v30.md | After §5.5 | Insert §5.6 |
| ED-674 | designs/systems/player_agency_v30.md | §4.2 | Insert Step 2b |
| ED-675 | designs/systems/settlement_layer_v30.md | After §4.3 | Insert §4.4 |
| ED-676 | designs/conviction_track/conviction_track_v30.md | After §1.3 | Insert §1.4 |
| ED-677 | designs/ttrpg/threadwork_v30.md | §2.3 | Extend visibility table |
| ED-678 | designs/characters/character_histories_v30.md | After Stage 3 | Insert derivation table |
| ED-679 | designs/systems/npc_behavior_v30.md | §8 | Amend priority trees |
| ED-680 | designs/systems/investigation_systems_proposal_2026-04-15.md | §Case Board | Insert Thread Layer |
| ED-681 | designs/ttrpg/threadwork_v30.md | §3.7 | Expand beats |
| — | canon/editorial_ledger.yaml | Append | ED-673 through ED-681 |
| — | references/canonical_sources.yaml | Add entries | rs_budget, wc_survival_spine |
| — | references/file_index_summary.md | Update | New files, propagation status |
| — | designs/ui/valoria_ui_ux_v4_1.md | §Thread state display | Cross-reference WC UI requirement |

---

## CLOSE STATUS FOR PRIOR EDs

| ED | Status | Action |
|---|---|---|
| ED-666 | Applied | Close → resolved |
| ED-667 | Applied (§9.4b in social_contest_v30) | Close → resolved |
| ED-668 | This commit | Close → resolved |
| ED-669 | This commit | Close → resolved |
| ED-670 | Applied (§3.4 in npc_behavior_v30) | Close → resolved |
| ED-671 | Applied (§3.4 in npc_behavior_v30) | Close → resolved |
| ED-672 | Applied (§4.3 in npc_behavior_v30) | Close → resolved |

---

*Thread horizontal integration specification complete. All open questions resolved. All fire paths specified. Propagation to individual documents is a mechanical application of the specifications in this document.*
