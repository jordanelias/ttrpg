# PART ELEVEN: SCALE TRANSITIONS

Valoria operates across five scales simultaneously. A single session may move from personal combat to Thread operations to faction-level consequences within the same scene. The transition system provides vocabulary and eight formal handoff rules to manage these crossings without losing mechanical coherence.

---

## 11.1 Scale Table

| Scale | Example | Base Ob | Min TS | Coherence auto-cost |
|---|---|---|---|---|
| Object | One item; one wound; a mechanism | 1 | 30+ | 0 |
| Personal | One person; a character | 2 | 30+ | 0 |
| Relational | Small group; a social agreement; an officer and their unit | 3 | 50+ | −1 |
| Territorial | A duchy; a district; a settlement | 4 | 50+ | −1 |
| Structural | A kingdom; an institution; a lasting constitutional arrangement | 5+ | 70+ | −2 |

Base Ob applies when a Thread operation targets configurations at that scale. RS costs and degree-table consequences are per Stage3 operation tables. The legacy TT Multiplier column has been removed — it does not map to the current RS per-degree cost structure.

---

## 11.2 Vocabulary

These terms are used consistently throughout the rules. Each names a specific moment of scale-crossing:

**Zoom In** — the GM narrows focus from a larger scale to a smaller one:
*"Dav, you spot the Niflhel officer in the Templar formation. You have one exchange. Zoom in."*

**Zoom Out** — the GM widens focus back to the larger scale after smaller-scale resolution:
*"The duel ends. Zoom out — the battle has continued while you fought."*

**Register Shift** — a social scene changes its fundamental nature:
*"Serena's Unmask breaks the formal register. We're no longer in a Debate — the King is your audience now."*

**Domain Echo** — the moment when a personal success ripples up into a faction-level consequence. No separate roll or action required:
*"That testimony lands. Domain Echo — Church Mandate drops to five."*

---

## 11.3 Eight Handoff Rules

| Transition | Handoff Rule |
|---|---|
| Personal → Thread | The Leap action triggers the transition. Contact duration begins on the round the Leap succeeds. |
| Personal → Faction | The GM recognises faction-level scope and resolves a Domain Action from the same roll. Personal Ob resolves first; Domain Action Ob second. |
| Personal → Scene | A personal roll made before an audience may serve as the opening move of a social scene, or as the Appeal itself. |
| Scene → Faction | An Appeal or Debate that succeeds at sufficient scope produces a faction-attribute change via Domain Echo. |
| Thread → Faction | When a Thread operation targets a faction-level configuration, it resolves as a Domain Action using the Thread pool and appropriate Ob. No separate roll. |
| Thread → Mass | **Combat Thread operations** (Dissolution, offensive Pulling targeting enemy units) manifest at Phase 2 (before Engagement), simultaneous with Volley — declared Phase 1, fire before combat. **Support Thread operations** (Weave, Mend, Lock, non-offensive Pulling) manifest at Phase 5 (Cascade), after Engagement — declared Phase 1, Leap resolves Phase 5. |
| Mass → Personal | Any character may take a Personal Action at Phase 5 (equivalent to Priority 8). Limit: one exchange per battle turn. Non-incapacitated named targets become Contested Figures. The general's Phase 5 action is consumed by personal combat each turn until resolved — mass battle continues at reduced command efficiency (CR suspended). This is not a literal pause but a structural hold on CR effects. |
| Scene → Mass | Social scene outcomes in combat contexts affect the mass combat's opening state; applied before the next round's declaration phase. |

---

## 11.4 Scope Shift

A character may shift scope once per round, declared at the start of their turn. Verbal declaration only — no roll.

One action per round per scope. Taking an additional action in a different scope within the same round costs +1 Inspiration (spend before rolling).

---

## 11.5 Domain Actions

When a personal action has faction-level scope, the GM recognises it as a Domain Action. The personal roll resolves the personal outcome; the same roll simultaneously resolves the faction-level effect.

**Domain Ob** = target faction's relevant stat (1–7 scale, no division). A personal Debate against a faction representative uses the faction's Mandate as Ob for the faction-level consequence, even though the personal roll uses Disposition Ob for the interpersonal outcome.

**Domain Echo** fires automatically from any roll that crosses scales. Players do not declare it — the GM recognises scope and announces the echo.

**Seasonal cap**: Faction attributes may not change by more than ±2 per season regardless of how many Domain Actions or Domain Echoes target them. This cap is shared across TTRPG and board game modes in hybrid play.

---

## 11.6 Inert Knowledge

When a Thread-sensitive character explains Thread-level reality to a non-sensitive character, the non-sensitive character gains the information propositionally but cannot act on it with Thread-level precision.

Mark such information as **Inert Knowledge** on the non-sensitive character's sheet. They can recite it but it has no mechanical consequence until they develop sufficient sensitivity to render it as genuine knowledge.

This is not a punishment — it is a mechanical expression of the epistemological barrier the Foundations establish. The information is real; the capacity to use it is what's missing.

---

## 11.7 Mode-Specific Scale Behaviour

| Scale Context | TTRPG | Board Game | Hybrid |
|---|---|---|---|
| Mass combat resolution | Zone-based operational; Zoom In/Out for personal moments | Disposition table, single roll per battle | Board game resolution; Zoom In to TTRPG for key named-NPC moments |
| Siege resolution | Multi-season procedure with scenes (§8.4) | Siege order vs Fortification (single roll) | Board game roll; TTRPG scenes for infiltration or breakout |
| Domain Actions | Implicit — GM recognises scope from personal roll | Explicit — Order Set with placement and resolution | Strategic Phase uses board game orders; Personal Phase uses TTRPG Domain Echoes |
| Thread → Faction transitions | Standard handoff rule (Thread pool, faction-scale Ob) | Faction-card Thread orders (Weave/Investigate/Harvest) | Personal Phase: TTRPG. Strategic Phase: board game. Both count toward seasonal TT. |

**Key principle for hybrid**: Where a rule exists in both modes, the seasonal cap is shared. A faction attribute cannot change by more than ±2 per season regardless of how many sources target it in either phase.

---

## 11.8 STRESS TEST PATCHES — BATCH 11
## Source: tests/sim_combat_batch_11.md
## Applied: 2026-04-02

### PP-089 — Hybrid Season Phase Order
**Fixes P1-B11-04: §11.7 hybrid season phase order undefined**

> "**Hybrid season phase order:** Strategic Phase runs first. Personal Phase runs second. This order is fixed.
>
> Carryover rules:
> - Consequences established in the Strategic Phase (territory changes, unit deployments, faction stat changes) are visible to Personal Phase participants. PCs may respond to Strategic outcomes in their Personal Phase scenes.
> - Consequences established in the Personal Phase (NPC state changes, Knot resolutions, Domain Echoes from TTRPG scenes) take effect at the start of the NEXT season's Strategic Phase. They do not retroactively alter the current season's Strategic resolution.
> - Exception: If a Personal Phase scene involves a battle (PC enters an already-resolved BG battle territory), the outcome follows the Personal Phase → Next Season carryover rule unless the GM declares the scene simultaneous with the Strategic battle (must be declared before the Strategic Phase resolves).
>
> **The seasonal cap (±2 per attribute) is shared across both phases.** A faction attribute changed by Strategic actions and again by Personal Phase Domain Echoes cannot exceed ±2 total for that season."

### PP-090 — Mode-Switch Mid-Siege Conversion
**Fixes P1-B11-05: mode-switch mid-siege destroys garrison attrition state**

> "**Mid-siege mode switch:** When a TTRPG siege scene (personal-scale infiltration, breakout, or combat within a besieged location) transitions back to Board Game mode, carry the following state:
>
> - Each point of Endurance lost by a defending named character during the TTRPG scene = −0.5 Fortification (round down, minimum reduction 0). Example: defender loses 3 Endurance → Fortification −1.
> - Unit Strength lost during TTRPG-mode combat within the siege = −1 BG Strength per full TTRPG Strength point lost (conversion: 1 TTRPG Strength = 1 BG unit Strength point).
> - Morale changes from TTRPG personal combat carry forward as: each TTRPG Wound inflicted on the garrison commander = Morale −1 to their unit in subsequent BG turns.
>
> If no conversion is possible (TTRPG scene produced non-quantifiable narrative consequences), the GM records the outcome as a Domain Echo and applies its effect at the next Accounting Phase."

### CROSS-REFERENCE: P2-B11-16 — Personal Phase Interdiction vs Same-Season Battle
> "Personal Phase interdiction actions (blocking a commander, disrupting supply) take effect in the NEXT season (N+1) by default. GM may allow exception for scenes explicitly set immediately before a battle declared in the same season — but this must be declared before the Strategic Phase resolves. If not declared, N+1 timing applies."

### CROSS-REFERENCE: P2-B11-17 — Seasonal Cap Tracking
> "Explicit GM tracking sheet required for the ±2 seasonal cap on faction attributes. The cap is enforced at the moment of application — if a result would breach it, the excess is discarded. The tracker is updated after both Strategic Phase and Personal Phase each season."
