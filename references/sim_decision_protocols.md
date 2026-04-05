# Valoria Simulation: Player Decision-Making Protocol Library
## Version: 1.0 | Created: 2026-04-04
## Purpose: Define actor decision frameworks for use in all simulation modes
## Applies to: All Mode C / G / M simulations; all NPC and PC actor slots
## Maintained by: valoria-simulator skill

---

## Overview

Every simulated actor — Player Character (PC), Non-Player Character (NPC), or faction — must be assigned a decision protocol before simulation begins. Protocols are **not** personality descriptions; they are **mechanical decision rules** that determine how an actor selects actions, allocates resources, and responds to outcomes.

Using a single protocol (e.g. greedy optimiser) across all actors produces degenerate simulations. This library provides a full spectrum. Assign protocols that stress the mechanic under test, not protocols that validate it.

**Assignment notation:**  
`[PROTOCOL: <code> — <actor name>]`  
e.g. `[PROTOCOL: BELIEF-FIXED — Almud]`

**Multi-protocol actors:** A single actor may hold two protocols — a primary and a fallback triggered by a threshold condition. Notation:  
`[PROTOCOL: BELIEF-FIXED → SURVIVAL-FLOOR when Health ≤ 3]`

---

## Protocol Index

| Code | Name | Category |
|------|------|----------|
| GREEDY | Greedy Optimiser | Benchmark |
| BELIEF-FIXED | Belief-Fixed Actor | Goal / Belief |
| BELIEF-UPDATING | Belief-Updating Actor | Goal / Belief |
| FACTION-LOYAL | Faction-Loyal Actor | Goal / Faction |
| FACTION-OPPORTUNIST | Faction Opportunist | Goal / Faction |
| SATISFY | Satisficer | Non-Optimal |
| RISK-AVERSE | Risk-Averse Actor | Non-Optimal |
| MOMENTUM-HOARDER | Momentum Hoarder | Non-Optimal |
| MARTYR | Martyr | Irrational / Value |
| CONTRARIAN | Contrarian | Irrational |
| SPITE | Spite Actor | Irrational |
| PANIC | Panic Actor | Irrational / Stress |
| RITUAL | Ritual Actor | Irrational / Fixed |
| SURVIVAL-FLOOR | Survival-Floor Actor | Conditional |
| DEFERRED | Deferred Actor | Passive |
| RANDOM | Random Actor | Baseline Noise |

---

## Protocol Definitions

---

### GREEDY — Greedy Optimiser
**Category:** Benchmark  
**Use:** Establish upper-bound performance baseline only. Never the sole protocol in a simulation.

**Decision rule:**  
At every decision point, select the action with the highest expected net successes against current Obstacle (Ob). When two actions have equal expected net, prefer the one that raises a relevant stat. Never spend a resource when a free action achieves comparable expected net.

**Resource rule:** Spend Momentum, Stamina, or faction stats only if the spend improves expected net by ≥ 2.

**Applies across modes:**
- TTRPG: maximise dice pool size each round
- Hybrid: maximise Domain Action efficiency (output ÷ resource cost)
- Board Game (BG): take highest-yield action card each turn; never pass

**Flag trigger:** If GREEDY produces optimal play that a normal player could not identify without calculation, flag `[DOMINANT STRATEGY CANDIDATE]`.

---

### BELIEF-FIXED — Belief-Fixed Actor
**Category:** Goal / Belief  
**Use:** Characters with strong convictions that do not update in response to evidence. Tests whether the system creates mechanical pressure against principled play.

**Decision rule:**  
The actor has 1–3 fixed beliefs defined at simulation start (drawn from canon NPC profiles or assigned for the test). At every decision point:
1. Identify all available actions
2. Eliminate any action that contradicts a fixed belief (even if mechanically superior)
3. Among remaining actions, select the highest expected net

**Belief overrides:** A belief is never abandoned mid-simulation. If all available actions contradict beliefs, the actor takes the least-violating option and accepts the penalty.

**Example beliefs (assign at sim start):**
- "I will not betray the Church even under threat"
- "I will not spend Wealth to gain Military advantage — only lawful means"
- "I will not harm a named ally regardless of tactical value"

**Resource rule:** Beliefs constrain resource use. An actor with "no bribery" belief will not spend Wealth on Intel-gaining actions that require covert payment.

**Applies across modes:** All three. In BG, belief constraints eliminate specific card plays. In Hybrid, they block certain Domain Actions.

**Diagnostic value:** Reveals whether constrained play still has viable paths, or whether the system punishes principled actors into irrelevance.

---

### BELIEF-UPDATING — Belief-Updating Actor
**Category:** Goal / Belief  
**Use:** Characters who start with beliefs but revise them when mechanical pressure accumulates. Tests belief-revision thresholds and whether the system rewards or punishes adaptation.

**Decision rule:**  
Same as BELIEF-FIXED until a **revision trigger** fires. Revision trigger = any of:
- A belief-consistent action fails at Ob 3+ twice in the same scene
- Health or Composure drops below 50% of maximum
- An ally takes a Wound as a direct consequence of the actor holding the belief

On trigger: the actor may revise one belief to its nearest pragmatic equivalent (e.g. "I will not betray the Church" → "I will not betray the Church publicly"). Log the revision.

**Resource rule:** Post-revision, no constraint. Pre-revision, same as BELIEF-FIXED.

**Diagnostic value:** Tests whether the system has natural belief-revision inflection points, and whether revised actors become indistinguishable from GREEDY (a design problem).

---

### FACTION-LOYAL — Faction-Loyal Actor
**Category:** Goal / Faction  
**Use:** NPC actors whose decisions are entirely subordinate to their faction's current strategic goal. Tests faction AI coherence and whether individual actions correctly aggregate to faction-level outcomes.

**Decision rule:**  
At simulation start, assign the faction one seasonal goal from the following list (or as defined in faction design docs):
- Expand Mandate
- Expand Wealth
- Suppress rival faction stat
- Trigger a clock threshold
- Defend current stats (reactive)

At every decision point, select the action that most directly advances the assigned seasonal goal. Ignore personal benefit. Ignore inter-faction alliances unless the alliance directly serves the goal.

**Resource rule:** Spend faction resources freely in service of the goal. Do not hoard.

**Applies across modes:**  
- TTRPG: Domain Actions and individual NPC actions aligned to seasonal goal
- Hybrid: Faction assets deployed toward goal; personal character actions secondary
- BG: Action cards selected by goal alignment, not expected net

**Diagnostic value:** Reveals whether faction-level strategic play is mechanically coherent, and whether factions can actually execute their goals within seasonal resource limits.

---

### FACTION-OPPORTUNIST — Faction Opportunist
**Category:** Goal / Faction  
**Use:** Actors who have faction loyalty but exploit windows opened by other actors' moves. Tests whether the system rewards reactive play and whether it creates first-mover / second-mover asymmetries.

**Decision rule:**  
Maintain a passive baseline (take lowest-cost action that does not lose ground). Watch for **opportunity triggers:**
- A rival faction spends a resource and leaves a stat exposed
- A clock threshold is reached by another actor's action
- A PC creates a narrative gap (absent for a scene, makes a public commitment)

On trigger: pivot immediately to the highest-yield action that exploits the opening. Do not commit resources to the opening if the cost exceeds the expected gain by more than 1 net success.

**Resource rule:** Hoard resources until an opportunity trigger fires; then spend aggressively.

**Diagnostic value:** Tests whether the system has meaningful reactive windows, and whether opportunism is mechanically incentivised over proactive play.

---

### SATISFY — Satisficer
**Category:** Non-Optimal  
**Use:** Actors who pursue "good enough" outcomes rather than optimal ones. Models realistic player behaviour for most table situations. Primary alternative to GREEDY for routine simulations.

**Decision rule:**  
At every decision point, identify the **satisficing threshold**: the minimum outcome that advances the actor's current goal (typically: meet Ob, gain +1 stat, avoid a condition).

Select the **first available action** that meets the threshold, not the best one. If multiple actions meet the threshold simultaneously, select the one with lowest resource cost — but do not search for a lower-cost option if the first viable one is found.

**Resource rule:** Spend only when the free-action pool fails to meet the threshold. Do not spend to exceed the threshold.

**Applies across modes:** All three. In BG, select the first card that achieves the goal stat change; do not search hand for optimal card.

**Diagnostic value:** Reveals whether the system rewards optimisation disproportionately over competent play. If SATISFY and GREEDY produce near-identical outcomes, the decision space is too narrow.

---

### RISK-AVERSE — Risk-Averse Actor
**Category:** Non-Optimal  
**Use:** Actors who systematically avoid outcomes with high variance, even when expected net is positive. Tests whether low-risk paths remain viable, and whether the system punishes conservative play.

**Decision rule:**  
At every decision point, calculate expected net and variance for each available action (use the probability table in the simulator skill).  
Select the action with the **lowest probability of failure**, not the highest expected net.  
If two actions have equal failure probability, select the lower-cost one.  
Never take an action where P(failure) > 30%, even if expected net is high.

**Resource rule:** Spend resources to convert failure-possible rolls into near-certain outcomes. Accept reduced upside for reduced variance.

**Threshold for forced action:** If all available actions have P(failure) > 50%, take the one with lowest Ob and accept the probable failure.

**Applies across modes:**  
- TTRPG: prefer defensive actions, Composure preservation, actions at TN6 (Controlled) when available
- Hybrid: prefer Domain Actions with fixed outcomes over variable rolls
- BG: avoid action cards with conditional effects; prefer guaranteed stat changes

**Diagnostic value:** Reveals whether the system has viable low-variance paths, and whether cautious play leads to mechanical stagnation.

---

### MOMENTUM-HOARDER — Momentum Hoarder
**Category:** Non-Optimal  
**Use:** Actors who accumulate Momentum without spending it — either from risk aversion, uncertainty about when to spend, or misunderstanding of the resource. Tests Momentum system for hoarding pathologies.

**Decision rule:**  
Spend Momentum only when:
- Spending prevents a Wound or condition (defensive spend only)
- Momentum would be lost at end of scene (forced spend)

Never spend Momentum offensively or to exceed Ob by more than 1.

**Hoarding cap:** If Momentum reaches maximum carry limit, spend the minimum required to drop below cap.

**Applies to:** TTRPG and Hybrid only (BG does not use Momentum in the same way — substitute equivalent BG resource if applicable).

**Diagnostic value:** Tests whether Momentum hoarding is self-defeating (correct design) or competitive with active spending (design problem). Also surfaces carry-limit interactions and scene-boundary rules. Directly addresses prior sim finding SIM-X-26 where Solmund wasted 2 Momentum by not spending.

---

### MARTYR — Martyr
**Category:** Irrational / Value  
**Use:** Actors who accept personal mechanical harm — Wounds, stat loss, Composure damage — to protect another actor or advance an abstract principle. Tests whether the system has meaningful sacrifice mechanics, and whether sacrificial choices produce different mechanical outcomes than optimal play.

**Decision rule:**  
At simulation start, assign one **protection target** (named actor) or one **principle** (e.g. "preserve Rendering Stability").

At every decision point:
1. If an available action reduces harm to the protection target or advances the principle: take it, regardless of personal cost
2. If no such action is available: take the action with the lowest personal resource cost (do not optimise)

**Self-preservation threshold:** None. Martyr actors do not consider their own Health or Composure in action selection. They continue until incapacitated.

**Resource rule:** Spend all resources in service of the protection target or principle. No hoarding.

**Applies across modes:** All three. In BG, Martyr faction sacrifices Wealth/Military to protect an allied faction's stat.

**Diagnostic value:** Reveals whether the system mechanically supports sacrifice, or whether sacrificial play is simply sub-optimal with no compensating narrative/mechanical output.

---

### CONTRARIAN — Contrarian
**Category:** Irrational  
**Use:** Actors who consistently act against the mechanically dominant option, regardless of consequence. Tests whether the system remains coherent when actors refuse coordination.

**Decision rule:**  
At every decision point, identify the GREEDY-optimal action. Do not take it. Among remaining actions, select randomly (use uniform distribution across available options).

**Resource rule:** Spend resources on non-optimal actions. Refuse to coordinate with other actors even when coordination produces mutual benefit.

**Override:** If only one action is available, take it.

**Applies across modes:** All three.

**Diagnostic value:** Tests system resilience to uncooperative actors. A system that breaks under CONTRARIAN play (produces deadlock or impossible states) has a structural fragility.

---

### SPITE — Spite Actor
**Category:** Irrational  
**Use:** Actors who prioritise harming a specific other actor over their own advancement. Models feuding NPCs, vengeance-driven characters, or faction sabotage plays. Tests whether the system allows spite as a viable strategy.

**Decision rule:**  
Assign one **spite target** at simulation start.

At every decision point, prefer any action that reduces the spite target's stats, advances a clock that harms the target, or forces the target into a worse position — even if the action has no benefit to the Spite Actor.

If no action directly harms the spite target: take the lowest-cost available action (preserve resources for future spite opportunities).

**Resource rule:** Spend aggressively to harm the target. No cost is too high if it damages the target's position.

**Termination:** Spite ends only if the target is eliminated or the Spite Actor is incapacitated.

**Diagnostic value:** Tests whether targeted harassment is mechanically viable, whether it breaks faction balance, and whether the system has corrective mechanisms (social pressure, clock acceleration, etc.) that disincentivise spite.

---

### PANIC — Panic Actor
**Category:** Irrational / Stress  
**Use:** Actors under extreme mechanical pressure (Health ≤ 2, Composure ≤ 2, or facing an existential clock threshold). Tests whether the system degrades gracefully under stress or produces incoherent outcomes.

**Decision rule:**  
This protocol is typically a **fallback** triggered by a threshold condition on another protocol.

When active:
1. Take the action with the highest immediate safety value (i.e. most likely to prevent further Health/Composure loss this round), ignoring long-term consequences
2. Spend all available resources without calculation
3. Do not coordinate with other actors
4. Do not take actions with expected net < 0 unless no other action is available

**Duration:** Panic persists until the triggering threat is resolved or the actor is incapacitated.

**Notation:** `[PROTOCOL: SATISFY → PANIC when Health ≤ 2]`

**Diagnostic value:** Tests whether the system has runaway failure states, and whether emergency spending creates meaningful recovery options or only delays incapacitation.

---

### RITUAL — Ritual Actor
**Category:** Irrational / Fixed  
**Use:** Actors who follow a fixed action sequence regardless of circumstances. Models heavily scripted NPCs, institutionally constrained actors (e.g. Church procedural actors), or rule-bound faction behaviour.

**Decision rule:**  
Define a fixed action sequence at simulation start (e.g. "Phase 1: expand Mandate → Phase 2: suppress rival Intel → Phase 3: trigger Theocracy Counter"). Execute the sequence in order, one action per available action slot, regardless of current mechanical state.

**Override condition:** Sequence may pause (not deviate) if the current step is mechanically impossible (e.g. stat already at max). Skip to next step; return to paused step when viable.

**Resource rule:** Allocate resources according to sequence phase. No reactive spending.

**Diagnostic value:** Tests whether scripted-AI faction behaviour produces interesting or deadlocked outcomes. Useful for establishing baseline NPC behaviour in Mode G4 (Seasonal Faction Play) before introducing adaptive protocols.

---

### SURVIVAL-FLOOR — Survival-Floor Actor
**Category:** Conditional  
**Use:** Actors who optimise normally until a survival threshold is crossed, then shift entirely to self-preservation. Tests the system's wound/condition escalation and whether survival play has viable paths.

**Decision rule (above threshold):** Same as SATISFY.

**Survival threshold trigger:** Health ≤ 2 OR Composure ≤ 1 OR facing Wound that would reduce Health to 0.

**Decision rule (below threshold):**
1. All actions selected solely on P(success) for defensive outcomes (reduce incoming damage, restore Health/Composure, escape)
2. No offensive or resource-generating actions
3. Spend all Momentum and Stamina immediately for defensive effect
4. Retreat or disengage if the option exists

**Return to SATISFY:** If Health recovers above threshold via healing/rest, resume SATISFY protocol.

**Diagnostic value:** Tests whether the wound/condition system has a viable recovery path from near-incapacitation, and whether survival play can be sustained for more than 1–2 rounds.

---

### DEFERRED — Deferred Actor
**Category:** Passive  
**Use:** Actors who take no meaningful action — they follow, wait, or defer to others. Tests whether the system accommodates passive actors without breaking, and whether passive actors create mechanical burdens on other actors.

**Decision rule:**  
Take the lowest-cost available action each round. Never spend resources. Never take an action with a contested roll unless forced. If another actor has taken the "lead" in the scene, mirror their action type at minimum competence.

**Applies across modes:** All three. In BG, Deferred faction passes action where permitted; takes minimum mandatory action where not.

**Diagnostic value:** Tests action economy minimum requirements, and whether the system forces all actors to be active or permits passive participation without catastrophic mechanical consequence.

---

### RANDOM — Random Actor
**Category:** Baseline Noise  
**Use:** Pure randomisation. Establishes noise floor for comparison. Rarely the primary protocol; most useful as one actor in a multi-actor simulation.

**Decision rule:**  
At every decision point, select uniformly at random from all available actions (including self-defeating ones). Resource spending: random (50% chance to spend any available resource on any given round).

**Diagnostic value:** Tests whether the system produces wildly different outcomes under random input than under purposeful input. If outcomes are similar, decision architecture has insufficient mechanical leverage (P2).

---

## Assignment Guidelines

### For Mode C (Full Scenario)
Assign each actor a protocol before the scenario begins. Document in the 7-dimension tag under `Archetypes:`. Use at least 3 different protocols across the actor roster.

### For Mode D (Edge Case Discovery)
Use GREEDY + one IRRATIONAL protocol. Greedy finds the mechanical optimum; irrational finds the failure modes.

### For Mode F (NPC Stress Test)
Default protocol assignments for named NPCs (override as needed for specific tests):

| Non-Player Character | Default Protocol | Rationale |
|-----|-----------------|-----------|
| Almud | BELIEF-FIXED | Political paralysis from fixed dynastic beliefs |
| Lenneth | BELIEF-UPDATING | Scholar; revises beliefs under evidence pressure |
| Torben | FACTION-LOYAL | Crown instrument; acts on seasonal Crown goal |
| Elske | SATISFY | Independence-seeker; good enough over optimal |
| Himlensendt | RITUAL | Church procedural; follows institutional sequence |
| Olafsson | FACTION-OPPORTUNIST | Cardinal politics; exploits openings |
| Klapp | FACTION-OPPORTUNIST | Intelligence ops; reactive and resource-hoarding |
| Baralta | BELIEF-FIXED | Devout legalist; belief never yields to pragmatism |
| Vaynard | RISK-AVERSE | Secret research; avoids exposure above all |
| Maret Uln | SATISFY | Pragmatic Southernmost practitioner |
| Ehrenwall | FACTION-LOYAL → PANIC when Stability ≤ 2 | Coup-trigger actor; loyal until existential threat |

### For Mode G4 (Seasonal Faction Play)
Assign one protocol per faction. Do not use GREEDY for more than one faction. Suggested baseline roster:

| Faction | Protocol |
|---------|---------|
| Crown | FACTION-LOYAL (Mandate expansion) |
| Church | RITUAL (theological sequence) |
| Hafenmark | FACTION-OPPORTUNIST |
| Varfell | RISK-AVERSE |
| Guilds | SATISFY |
| Niflhel | BELIEF-FIXED |
| Restoration Movement | MARTYR |
| Löwenritter | GREEDY (benchmark only) |

### For Mode G2 (Debate)
Minimum two protocols in any debate. Suggested pairings:

| Pairing | What it tests |
|---------|--------------|
| GREEDY vs RISK-AVERSE | Whether conservative rhetorical play is viable |
| BELIEF-FIXED vs BELIEF-UPDATING | Whether conviction or adaptability wins |
| SATISFY vs SPITE | Whether targeted disruption breaks satisficing actors |
| MARTYR vs CONTRARIAN | Extreme case — system coherence under irrationality |

---

## Simulation Output Requirements

When a decision protocol is active, the simulation output must record:

```
Actor: [name]
Protocol: [code]
Round N action: [action taken] — [why this action per protocol rules]
Protocol override fired? [YES/NO — if YES, state trigger]
```

If an actor's protocol produces a decision the protocol rules do not clearly resolve, flag:  
`[PROTOCOL GAP: <actor> — <decision point> — protocol insufficient]`

Add to the editorial ledger only if the gap reveals a mechanic ambiguity (not just an under-specified test case).

---

## Commit Target

This file: `references/sim_decision_protocols.md`  
Link from: `skills/valoria-simulator-SKILL.md` (Read Protocol section) and `references/file_index.md`  
Canonical status: Design-layer reference document. Not a params file.

---

*v1.0 — 2026-04-04*
