<!-- DEPRECATED: 2026-04-09 — SUPERSEDED BY designs/board_game/valoria_bg_v05_simulation_and_patches.md. Do not use as a mechanical reference. Retained for audit trail only. -->

# BG CONSOLIDATED SYNTHESIS — AMENDMENT 1

**Date:** 2026-03-31
**Trigger:** User design clarifications on three-mode mandatory architecture, political/metaphysical parity, and scale interweaving
**Amends:** bg_consolidated_synthesis.md

---

## CORRECTION 1: BG IS A MANDATORY STANDALONE MODE

### The Error

The Sonnet synthesis stated: *"The BG is the Strategic Phase, not a standalone game... designed to feel incomplete without the personal layer. Proposals that make the BG feel like a complete, satisfying standalone experience risk undermining this design intent."*

The consolidated synthesis carried this framing forward.

### The Correction

Stage12 §12.2 defines BG as a full standalone mode with its own session structure (2–4 hours), season pacing (3–5 seasons per session), endgame triggers, and victory conditions. It is one of three **mandatory** game modes: TTRPG, hybrid, and board game. All three are full games. None is subordinate to any other.

The Sonnet synthesis's Fact 1 mischaracterizes the design. The BG must be a complete, satisfying game on its own terms AND function as the strategic layer in hybrid mode. These are not competing requirements — they are simultaneous mandates.

### Cascading Impact

| Prior Assessment | Correction |
|-----------------|------------|
| MP-23 (Secondary Objectives) labeled "BG-only accommodation" | MP-23 is a **core BG mechanic** for replayability and information asymmetry in standalone mode. Not an accommodation — a design requirement. |
| MP-36 (Hollow Victory) labeled "BG-only Tier 2" | MP-36 is a **core BG mechanic** that gives standalone BG its own moral-weight system. Elevate to Tier 1. |
| MP-06 (Solo) labeled "accessibility accommodation" | Solo is a full mode variant within the mandatory BG mode. Treat as Tier 2, not Tier 3. |
| General framing that "completeness" risks undermining hybrid | Removed. The BG should feel complete. The hybrid mode adds depth to a game that already works, not completion to a game that doesn't. |

---

## CORRECTION 2: POLITICAL AND METAPHYSICAL LAYERS ARE CO-EQUAL

### The Error

Both reviews tilted toward Thread/metaphysical compliance as the primary evaluation lens. The Opus review spent 70% of its findings on Thread-related P-code violations. The Sonnet synthesis centered its "deeply right" assessment on how well reference games express the Thread substrate. Political mechanics (Deal Tokens, Contempt, Crown Policy, Proxy Support, Institutional Belief) were evaluated primarily for whether they *didn't interfere* with Thread compliance, not for whether they carried their own weight.

### The Correction

The political landscape — its factions, boiling points, institutional tensions, clock pressures — gives the game purpose. Thread grounds that purpose philosophically. Both layers are load-bearing. A BG that perfectly expresses Thread inseparability but produces flat political play fails just as badly as one with rich politics but broken Thread mechanics.

The three clocks express this parity:
- **RS** = metaphysical substrate integrity (Thread layer)
- **TC** = institutional power struggle between secular and theocratic governance (political layer)
- **IP** = geopolitical pressure from an external power watching for weakness (political layer)

RS has metaphysical priority *in the fiction* (if the substrate fails, politics is meaningless). But TC and IP have **design parity** — they must generate equally compelling decisions, equally urgent crises, and equally interesting faction dynamics.

### Cascading Impact

**1. The "RS as substrate modifier" precondition is refined.** My prior recommendation — that RS level should modify baseline Ob for all territorial actions — remains directionally correct but must not make TC and IP feel secondary. RS degradation affecting all actions is a background pressure, not a dominating mechanic. TC and IP should have their own environmental effects:

- **TC affects social/institutional actions.** High TC = Church orders in all territories at −1 Ob, non-Church Diplomacy at +1 Ob. Low TC = Church orders at +1 Ob, secular governance easier.
- **IP affects external-facing actions.** High IP = Trade with Schoenland disrupted (+1 Ob), but Altonian intelligence leaks give all factions +1D to Intel orders (Altonia is watching everyone, information flows both ways). Low IP = trade flourishes, but factional complacency.

All three clocks modify the environment. RS is not the only substrate — TC and IP are the political substrate.

**2. Proposal evaluations gain a second axis.** Every proposal should be tested on two criteria, not one:

| Criterion | Question |
|-----------|----------|
| **Canon compliance** | Does this violate P-01–P-14? |
| **Political weight** | Does this produce faction dilemmas with real stakes, visible consequences, and emergent narrative? |

Prior reviews only applied the first. Proposals like MP-27 (Crown Policy), MP-22 (Contempt), MP-34 (Institutional Belief), MP-26 (Proxy Support), and MP-02 (Deal Tokens) were treated as "keeps" without interrogating whether their political mechanics actually generate the factional pressure the setting demands.

**3. MP-34 (Institutional Belief) is confirmed as the highest-priority new mechanic** — not just because it bridges the TTRPG Belief system, but because it makes faction identity *mechanically consequential* in political play. The Uphold/Compromise structure forces players to weigh institutional coherence against strategic advantage every time an event challenges their mandate. This is the political layer's equivalent of co-movement: every political action has identity consequences.

---

## CORRECTION 3: SCALE INTERWEAVING IS A CORE DESIGN CRITERION

### The Error

Neither review evaluated proposals against the scale transition architecture (stage11). The 33 proposals were assessed for canon compliance and throughline coherence but not for how they support movement between individual scenes, mass battles, and faction-level play — or how mechanical systems hand off across these transitions.

### The Correction

Stage11 defines five scales (Object → Personal → Relational → Territorial → Structural), eight formal handoff rules, and mode-specific branching tables. The ability to move between scales fluidly, with consequences propagating across transitions, is not a feature — it is the architecture.

Every BG proposal must be evaluated against a third criterion:

| Criterion | Question |
|-----------|----------|
| **Canon compliance** | Does this violate P-01–P-14? |
| **Political weight** | Does this produce faction dilemmas with real stakes? |
| **Scale interweaving** | Does this mechanic support clean transitions between personal, mass, and faction-level play? Does it generate emergent conditions at multiple scales simultaneously? |

### Proposal-Level Scale Assessment

**Strong scale interweaving:**

| Proposal | Why |
|----------|-----|
| MP-25 (Champions) | A Champion token on the BG map IS a named NPC in the TTRPG. Zoom In to a territory with a Champion and you have a personal scene with a defined character. Champion wound states (MP-32) persist across scales — a Champion wounded in a mass battle enters the TTRPG scene Wounded. |
| MP-09 (Zoom-In Triggers) | Directly defines scale transition conditions. But needs expansion — currently 8 triggers, all from BG→TTRPG. Stage11 handoff rules support TTRPG→BG transitions (Domain Echoes) that MP-09 doesn't address. |
| MP-35 (Cascade Phase Effects) | Explicitly bridges personal outcomes to faction card economy. The Concordia card-hand becomes the medium through which scale transitions express themselves mechanically. |
| MP-34 (Institutional Belief) | When a BG event challenges the faction's Mandate, the Uphold/Compromise decision is a faction-scale moment. In hybrid, if the PC faction leader is present, this becomes a personal-scale scene — the leader must decide in character whether to uphold or compromise. The same mechanic fires at two scales simultaneously. |
| MP-21 (Community Projects) | A Project marker on the BG board is a location in the TTRPG. A Community Weave project in progress IS a TTRPG scene waiting to happen — practitioners working, Church surveillance approaching, military forces threatening. Projects generate emergent personal scenes by existing on the map. |

**Weak scale interweaving (proposals that work only at faction scale):**

| Proposal | Issue |
|----------|-------|
| MP-30 (Research Tracks) | Pure faction-level bookkeeping. Advancing a Research Track has no personal-scale expression. A Crown player advancing Military Tradition L3→L4 doesn't generate a scene or a mass battle moment. Fix: tie Research Track advances to specific events — L3 Military Tradition requires winning a battle with the Champion present, not just accumulating March/Muster orders. |
| MP-14 (Leverage Tokens) | Faction-scale currency with no personal-scale equivalent. A faction that gains Leverage from being targeted doesn't produce a personal moment. Fix: in hybrid, Leverage gain from a specific attack triggers a zoom-in opportunity — the targeted faction leader may respond in a TTRPG scene. |
| MP-11 (Lead/Follow) | Resolution modifier with no scale bridge. Following another faction's lead doesn't generate a scene. Acceptable — not every mechanic needs to bridge scales, but don't count this as supporting interweaving. |

**Emergent narrative generation — the strongest combinations:**

The proposals that generate emergent narrative conditions are those where multiple mechanics intersect to produce situations nobody prescribed:

1. **MP-24 (Attention Pool) + MP-21 (Community Project) + MP-25 (Champion):** Revolution starts a Community Weave in territory 7. Church Attention Pool rises. Church Champion Himlensendt is in adjacent territory 6. At Attention threshold 3, Church opens a Heresy Investigation in territory 7. In hybrid mode, this generates a TTRPG scene: Himlensendt's agents arrive to investigate a community weaving practice. If a PC is involved in the project, they must decide whether to hide, confront, or flee. None of this was scripted — it emerged from three mechanics intersecting on the map.

2. **MP-34 (Institutional Belief) + MP-22 (Contempt) + MP-27 (Crown Policy):** Crown issues Royal Taxation (MP-27). Guilds' Institutional Mandate ("Commerce is neutral; we serve whoever can pay") is challenged — taxation is non-neutral government interference in commerce. Guilds must Uphold (refuse to collect, losing Wealth) or Compromise (collect, gaining self-Contempt). If they Compromise and the Church later challenges Crown, Guilds' accumulated self-Contempt makes them politically unreliable allies. The political landscape shifts from a single policy decision cascading through the Belief and Contempt systems.

3. **MP-12 (Thread Debt) + MP-04 (Thread Resonance) + Scale Transition:** A Revolution practitioner incurs Thread Debt to Mend a damaged territory. Thread Resonance rises for all factions in the area. Varfell's TR hits 3 — they gain intelligence bonuses on Thread-active sites. Varfell Intel order targets the Revolution project. In hybrid, this is a TTRPG scene: Varfell agent investigating Thread activity, encountering the practitioner mid-operation. The Thread Debt is ticking — if the practitioner is interrupted, the debt remains unpaid and RS degrades. The personal scene's outcome (does the Varfell agent report the practitioner to Church?) feeds back into the BG state at Cascade Phase.

These are the conditions the system should produce: multi-scale, multi-mechanic narrative situations that emerge from play rather than from a scenario script. The BG mechanics are the scenario engine — not because they're subordinate to the TTRPG, but because they generate the conditions from which all three modes' narrative emerges.

---

## CORRECTION TO P-14 CO-MOVEMENT FINDING

### Refinement

My Opus review identified a "systemic P-14 failure" — no BG co-movement protocol exists. This was imprecise.

Stage12 §12.5 shows the BG already has a co-movement system: the Co-Movement Card deck (18 cards). TTRPG uses Version C (deterministic auto-effects + d6). BG uses the card deck. These are different implementations of the same principle.

The accurate finding is: **the co-movement card deck may be insufficient** to express three-dimensional consequences for *all* Thread operations proposed in V1–V4. The existing deck covers the existing BG Thread orders (Weave/Mend/Investigate/Harvest). New Thread mechanics (Thread Debt, Community Weaving, Crisis Response RS variant) need co-movement coverage added to the deck or resolved through a parallel protocol.

This is a design extension task, not a systemic gap. The architecture exists. The new proposals need to be connected to it.

---

## REVISED PRECONDITIONS

Given all three corrections, the preconditions for Tier 1 integration are:

1. **BG-E-30: Adopt MP-31 (Concordia Card-Hand)** — structural foundation for all modes
2. **Co-Movement deck expansion** for new Thread mechanics (Thread Debt, Community Weaving, Crisis Response RS) — design task, not architecture gap
3. **Clock environmental effects** for all three clocks (RS, TC, IP each modify the action environment) — political parity
4. **[EDITORIAL] MP-34 Institutional Mandate text and trigger conditions per faction** — content decision
5. **Scale transition audit** for all Tier 1 proposals against stage11 handoff rules — verify each mechanic supports or at minimum doesn't obstruct scale interweaving

---

*Amendment 1 complete. Core corrections: BG is standalone-mandatory; political weight is co-equal with metaphysical compliance; scale interweaving is a design criterion. Three prior assessments corrected (MP-23, MP-36, MP-06 elevated; MP-30, MP-14 flagged for scale weakness; P-14 finding refined from "systemic gap" to "deck expansion needed"). Three emergent narrative examples demonstrate scale interweaving as a testable criterion.*
