<!-- [EDITORIAL: PP-671 — meta-throughline synthesis 2026-04-19, user-directed] -->

# VALORIA — META-THROUGHLINES

## Date: 2026-04-19
## Source: `references/throughlines_complete.md` (25 throughlines, 8 categories)
## Definition: A meta-throughline is a pattern that operates ACROSS multiple throughlines — a constitutive principle that the throughlines themselves instantiate.
## Purpose: Identify the deepest structural commitments of the game so design work can evaluate new mechanics against them.

---

## Summary

Five meta-throughlines emerge from reviewing the 25 throughlines. Each is grounded in specific throughlines where the pattern is mechanically visible. Together, they constitute the game's design DNA — the commitments that distinguish Valoria from generic faction strategy or generic Thread-fantasy RPG.

| # | Meta-Throughline | Instantiating Throughlines | Design consequence |
|-|-|-|-|
| M-1 | Decay-as-default | T-04, T-05, T-06, T-07, T-12, T-16, T-18, T-19 | World state degrades without player action; player intervention slows decay at best |
| M-2 | Substrate as universal medium | T-01, T-02, T-03, T-08, T-13, T-18, T-21, T-22 | Every system measures rendering/thread state; "everything is thread" is mechanical, not flavor |
| M-3 | Institutional identity = mechanical attractor | T-05, T-08, T-09, T-10, T-11 | No faction is mechanically interchangeable; each maps to a distinct substrate-relationship |
| M-4 | Scale-preserving chains | T-01, T-03, T-15, T-16, T-18, T-19, T-23, T-24, T-25 | Same throughlines operate at personal/settlement/province/peninsular scales |
| M-5 | Forced-choice architecture | T-12, T-13, T-14, T-17, T-20, T-22 | Every significant throughline produces irreducible tradeoffs; no universal solution exists |

---

## M-1: Decay-as-default

**Pattern:** The game's baseline state is entropic. Throughlines describing time-based pressure — clock decay (T-04 RS, T-05 TC, T-06 IP, T-07 Strain), individual-scale cycles (T-12 Coherence depletion), relational cascades (T-16 Knot Strain), geographic worsening (T-18 Radiation, T-19 Southernmost Spiral) — all advance regardless of player action. Player intervention slows decay at best; no player action can reverse the baseline direction.

**Grounding in canon:**
- T-04: "RS baseline decay (−1/year) + Gap persistence (−4/season) + Lock drift" — structural, not player-triggered
- T-05: "TC passive advance (+1/season conditional)" — Church expands by default
- T-07: "War destroys the capacity to govern ... positive feedback loop"
- T-18: "The Calamity is not a past event — it is a geographic condition that worsens as RS declines"

**Design consequence:** The videogame must NOT provide a "rest" state where the player can stabilize. Every turn must present active decay that the player is choosing which dimension of to address. The player's agency is in prioritization of which decay to intervene against, not in whether decay occurs.

**Exceptions (where something advances through player action):** T-15 (Player Progression) and T-14 (Conviction Architecture) both move via player action — but both also have decay vectors (Renown decay, Scar accumulation). Even progress-throughlines carry decay.

---

## M-2: Substrate as universal medium

**Pattern:** Every Valoria mechanic is mechanically, not metaphorically, a Thread interaction. Statistics across all scales (Health, Order, Prosperity, Mandate, Stability, Coherence, RS, TC, CV, Strain) measure configurations of the substrate at their respective scales. Perception (T-02), operations (T-03), politics (T-08), radiation (T-18), and collective action (T-22) all reduce to substrate state changes.

**Grounding in canon:**
- T-01: "Health, Composure, Order, Prosperity, Mandate, Stability — all measure thread-configuration state at different scales ... This is not metaphor; it is the game's ontological commitment"
- T-02: "The player does not see 'the world' — they see what their character's rendering can present"
- T-03: "Every intervention on the substrate produces unintended consequences"
- T-08: "The Church's institutional function is rendering-reinforcement"

**Design consequence:** When adding a new mechanic, ask: what thread-configuration state does this measure? A mechanic that cannot be expressed as substrate interaction is either (a) restateable in substrate terms, or (b) a violation of the game's core commitment. Physical UI in Godot should visualize thread-configuration wherever possible (TS gates on perception, rendering failures on low-RS maps, co-movement auras on Thread operations).

**Relationship to M-1:** Substrate state degrades over time (M-1 acts on M-2). The decay-as-default meta-throughline operates on the substrate-as-universal-medium meta-throughline. Decay is the substrate's temporal direction.

---

## M-3: Institutional identity = mechanical attractor

**Pattern:** Each major faction's political identity maps to a distinct, non-interchangeable mechanical relationship with the substrate. This is NOT faction-as-flavor with shared mechanics. Church (T-08), Varfell (T-09), Niflhel (T-10), Crown (T-11) each define their own causal chains with different systems, different victory pathways, and different relationships to Thread.

**Grounding in canon:**
- T-08 Church: "every mechanism it controls ... works to prevent the population from perceiving the substrate" → rendering-reinforcement
- T-09 Varfell: "the faction whose institutional interest aligns with substrate maintenance" → thread-progressive
- T-10 Niflhel: "the only faction whose strategic interest structurally diverges from RS preservation" → accelerationist
- T-11 Crown: "Thread-as-tool when advantageous, Thread-as-threat when dangerous" → pragmatist

**Design consequence:** A new faction would need its own substrate-relationship axis, not a reskinned existing one. The peninsula is full of factions because each one represents a distinct answer to "what is our institutional relationship to rendering?" Hafenmark (not in the listed four) would need explicit characterization along this axis — T-11 partially covers Crown via Thread Liaison, but Hafenmark's relationship to substrate remains categorically underspecified across the 25 throughlines (see §Meta-Observations below).

**Relationship to M-2:** The faction attractors carve up M-2's substrate-as-universal-medium into distinct political-mechanical territories. M-2 is the shared field; M-3 is how institutions stake territory on that field.

---

## M-4: Scale-preserving chains

**Pattern:** Throughlines fire identically at multiple scales. Personal Thread operations (T-03, T-12) produce the same co-movement pattern as mass Thread operations (T-03 at mass_battle scale). NPC arc emergence (T-23) mirrors faction emergence (T-15). Convergence (T-24) operates across all scales — a single-season crisis is just a scale-contracted version of the generational arc (T-25). The game's scale-transition architecture is mathematically the same system at different resolutions.

**Grounding in canon:**
- T-03: "Co-movement fires in all modes" — personal, relational, mass, structural scales
- T-15 Player Progression: "Standing 0 ... settlement governance ... provincial authority ... faction emergence" — 5-stage scale ladder uses same action types at each stage
- T-18 Radiation Gradient: "per-territory effects (Ob modifiers ... settlement Order effects)" — same matrix applied at territory and settlement
- T-23 NPC arc and T-25 Generational arc: same state-machine pattern at 1-NPC and 20-NPC-cohort scales

**Design consequence:** Implementation economy. Code written for personal-scale Thread operations (combat scene) should extend to mass-scale (strategic battle) with a scale-parameter change, not a rewrite. The scale-transition UX (zoom in/zoom out) is mechanically a parameter change, not a mode switch. This meta-throughline is the argument against per-scale code duplication.

**Non-preservation cases:** T-13 Certainty and T-14 Conviction are individual-only — they do not scale up to faction level. A faction does not have Certainty. (Though a faction's dominant NPC's Certainty influences faction behavior via priority trees.) This bounds M-4 — some throughlines are scale-bound to the personal layer.

---

## M-5: Forced-choice architecture

**Pattern:** Every significant throughline produces irreducible tradeoffs. The practitioner (T-12) trades Coherence for Thread power. The Certainty journey (T-13) opens capabilities and closes relationships. The Conviction Scar system (T-14) makes moral transformation costly. The companion Thread-departure (T-17) trades Thread freedom for relational bonds. The Two Contests (T-20) split resources between sovereignty and survival. The Belief Lattice (T-22) requires NPCs to break institutional commitments to cooperate.

**Grounding in canon:**
- T-12: "−1 TS permanent → recovery → ... The price of pulling back from the substrate"
- T-13: "The journey from C5 (orthodox) to C0 (Thread-accepted) cannot be reversed ... Each step opens capabilities and closes relationships"
- T-17: "The system forces the player to choose: Thread power or relational bonds"
- T-20: "The tension is unresolvable — the player must manage both contests simultaneously with insufficient resources for either"
- T-22: "The practitioners who must save the world can only cooperate after their institutional commitments have been broken by the crisis itself"

**Design consequence:** Valoria does not resolve its tensions. The game's shape is adversarial against optimization — there is no strategy that dominates all others because every strategy pays for what it buys. In Godot implementation, UX must surface the tradeoff at every choice point. Tooltips that show only the positive effect violate M-5. Every capability should display its cost.

**Relationship to M-1 and M-2:** Forced choices exist because resources are scarce (M-1 ensures scarcity via decay) in a substrate where all interventions produce side-effects (M-2 ensures interventions are lossy via Inseparability). M-5 is the player-facing expression of the combination of M-1 and M-2.

---

## Meta-Observations (not meta-throughlines, but structural findings)

### Hafenmark underspecification

The 25 throughlines include explicit characterizations for Church (T-08), Varfell (T-09), Niflhel (T-10), and Crown (T-11). **Hafenmark is not characterized** — it appears only as a throughline-affected party (e.g., T-05 "Hafenmark Parliamentary Challenge" as TC suppression tool) without its own institutional-attractor throughline. This is an M-3 gap: Hafenmark's institutional relationship to rendering is not defined.

**Implications:** Hafenmark's mechanical identity currently derives from Baralta's personal arc, Parliament mechanics, and Trade Network, but these are either NPC-scoped or cross-faction generic. No throughline defines Hafenmark's substrate-posture. Recommended: add T-26 (or renumbered) "Hafenmark as Institutional Compromise" — characterizing Hafenmark's rendering-relationship through its constitutional Parliament (substrate-agnostic political authority). This gap is flagged for future throughline-map revision.

### Löwenritter underspecification (same issue)

Löwenritter (T-nothing) appears as a mechanical actor in Coup Counter, Riskbreaker rank, military operations — but has no institutional throughline. Their relationship to Thread (Riskbreaker tolerance, military pragmatism) is a candidate for T-27.

### RM underspecification (same issue)

RM appears in multiple throughlines as affected party (T-05 suppression target, T-07 governance agent) but has no own institutional-attractor throughline. Given PP-666 formalized RM's settlement-emergence pathway and Jordan's clear design investment in RM as a co-primary faction, RM is a throughline gap. Recommended: T-28 "RM as Cultural Restoration" — rendering-relationship through pre-Calamity Einhir substrate recovery.

### Two contests distinguishes Valoria from peers

M-5 + T-20 together describe Valoria's deepest design commitment: the survival contest (RS/WC) and the sovereignty contest (territorial/faction) compete for the same resources. This is not a common strategy-game pattern. Most games present a single victory axis. Valoria presents two mandatorily-simultaneous axes where optimizing one endangers the other. M-5 enforces this at every scale from Coherence to national strategy.

### Throughline-to-throughline interaction is sparse

The Throughline Interaction Matrix (`throughlines_complete.md` §Interaction Matrix) defines 35 cross-throughline interactions among 7 throughlines (T-04, T-05, T-06, T-08, T-09, T-12, T-20). The other 18 throughlines have unmodeled interactions. If M-4 (scale preservation) and M-5 (forced choice) are real, then interaction density should be higher — a full matrix would reveal additional convergence markers beyond the 7+ collisions currently logged in `arc_register`.

---

## Meta-throughline satisfaction check for recent design work

| Patch | M-1 Decay | M-2 Substrate | M-3 Identity | M-4 Scale | M-5 Choice |
|-|-|-|-|-|-|
| PP-663 VTM strike | N/A | Negative (struck mechanic was substrate-interaction) | Neutral — doesn't re-characterize Varfell | N/A | N/A |
| PP-664 residual cleanup | N/A | N/A | N/A | N/A | N/A |
| PP-665 Yrsa rename | N/A | N/A | N/A | N/A | N/A |
| PP-666 settlement adjacency | N/A | Extends substrate-as-medium (edge types including Thread-Witnessed) | N/A | ✓ STRONG (same battle mechanic fires at settlement scale) | ✓ (bypass vs assault vs siege is forced choice) |
| PP-666 fractional ownership | ✓ STRONG (provinces decay in political unity, not just PV) | N/A | N/A | ✓ (settlement ↔ province ownership scales) | ✓ (consolidate-now vs accept-fragment forced choice) |
| PP-666 succession split | ✓ (succession is a decay/transition event) | N/A | ✓ STRONG (splits faction's institutional identity; M-3 specifies this was under-modeled) | ✓ (individual Standing → faction identity per T-15 scale) | ✓ STRONG (narrow winner → split is irreducible tradeoff) |
| PP-667 gap sweep | N/A | N/A | N/A | N/A | N/A |
| PP-668 propagation | N/A | N/A | N/A | N/A | N/A |

**Finding:** PP-666's three new systems each strongly satisfy multiple meta-throughlines. Specifically the faction succession split (ED-712) directly addresses the M-3 institutional-identity underspecification raised in this meta-analysis — it makes faction identity **forkable**, which is a deeper commitment to M-3 than having a single fixed attractor per faction.

---

## Usage

This document exists to provide evaluative criteria for future design work. When proposing a new mechanic, verify:

1. Does it satisfy or extend M-1 (does it contribute to decay, or does it provide unearned stability)?
2. Does it satisfy M-2 (is it expressible as thread-configuration state)?
3. Does it respect M-3 (does it reinforce a faction's attractor or blur identities)?
4. Does it honor M-4 (is it scale-transferable, or scale-bound with justification)?
5. Does it enforce M-5 (does it present an irreducible tradeoff, or provide dominant-strategy optimization)?

A mechanic that fails multiple meta-throughlines is likely off-vision, not just off-balance.
