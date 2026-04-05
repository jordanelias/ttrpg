# PART ELEVEN: SCALE TRANSITIONS
## Version: v0.14-ST — PP-089/090 applied in-place; §11.8 appendix eliminated


Valoria operates across five scales simultaneously. A single session may move from personal combat to Thread operations to faction-level consequences within the same scene. The transition system provides vocabulary and eight formal handoff rules to manage these crossings without losing mechanical coherence.

---

## 11.1 Scale Table

| Scale | Example | Base Ob | Min Thread Sensitivity | Coherence auto-cost |
|---|---|---|---|---|
| Object | One item; one wound; a mechanism | 1 | 30+ | 0 |
| Personal | One person; a character | 2 | 30+ | 0 |
| Relational | Small group; a social agreement; an officer and their unit | 3 | 50+ | −1 |
| Territorial | A duchy; a district; a settlement | 4 | 50+ | −1 |
| Structural | A kingdom; an institution; a lasting constitutional arrangement | 5+ | 70+ | −2 |

**Coherence auto-cost ruling (PP-248):** §11.1 is authoritative. Object and Personal scale Thread operations cost 0 Coherence automatically. The −1/op auto-cost applies only at Relational scale and above. Mass battle Thread operations run at Territorial/Campaign scale and correctly incur −1/op. No contradiction.

Base Ob applies when a Thread operation targets configurations at that scale. Rendering Stability costs and degree-table consequences are per Stage3 operation tables. The legacy Thread Tension Multiplier column has been removed — it does not map to the current Rendering Stability per-degree cost structure.

---

## 11.2 Vocabulary

These terms are used consistently throughout the rules. Each names a specific moment of scale-crossing:

**Zoom In** — the Game Master narrows focus from a larger scale to a smaller one:
*"Dav, you spot the Niflhel officer in the Templar formation. You have one exchange. Zoom in."*

**Zoom Out** — the Game Master widens focus back to the larger scale after smaller-scale resolution:
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
| Personal → Faction | The Game Master recognises faction-level scope and resolves a Domain Action from the same roll. Personal Ob resolves first; Domain Action Ob second. |
| Personal → Scene | A personal roll made before an audience may serve as the opening move of a social scene, or as the Appeal itself. |
| Scene → Faction | An Appeal or Debate that succeeds at sufficient scope produces a faction-attribute change via Domain Echo. |
| Thread → Faction | When a Thread operation targets a faction-level configuration, it resolves as a Domain Action using the Thread pool and appropriate Ob. No separate roll. |
| Thread → Mass | **Combat Thread operations** (Dissolution, offensive Pulling targeting enemy units) manifest at Phase 2 (before Engagement), simultaneous with Volley — declared Phase 1, fire before combat. **Support Thread operations** (Weave, Mend, Lock, non-offensive Pulling) manifest at Phase 5 (Cascade), after Engagement — declared Phase 1, Leap resolves Phase 5. |
| Mass → Personal | Any character may take a Personal Action at Phase 5 (equivalent to Priority 8). Limit: one exchange per battle turn. Non-incapacitated named targets become Contested Figures. The general's Phase 5 action is consumed by personal combat each turn until resolved — mass battle continues at reduced command efficiency (Command (PP-232) suspended). This is not a literal pause but a structural hold on Command (PP-232) effects. |
| Scene → Mass | Social scene outcomes in combat contexts affect the mass combat's opening state; applied before the next round's declaration phase. |

---

## 11.4 Scope Shift

A character may shift scope once per round, declared at the start of their turn. Verbal declaration only — no roll.

One action per round per scope. Taking an additional action in a different scope within the same round costs +1 Inspiration (spend before rolling).

---

## 11.5 Domain Actions

When a personal action has faction-level scope, the Game Master recognises it as a Domain Action. The personal roll resolves the personal outcome; the same roll simultaneously resolves the faction-level effect.

**Domain Ob** = target faction's relevant stat (1–7 scale, no division). A personal Debate against a faction representative uses the faction's Mandate as Ob for the faction-level consequence, even though the personal roll uses Disposition Ob for the interpersonal outcome.

**Domain Echo** fires automatically from any roll that crosses scales. Players do not declare it — the Game Master recognises scope and announces the echo.

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
| Mass combat resolution | Zone-based operational; Zoom In/Out for personal moments | Disposition table, single roll per battle | Board game resolution; Zoom In to TTRPG for key named-Non-Player Character moments |
| Siege resolution | Multi-season procedure with scenes (§8.4) | Siege order vs Fortification (single roll) | Board game roll; TTRPG scenes for infiltration or breakout |
| Domain Actions | Implicit — Game Master recognises scope from personal roll | Explicit — Order Set with placement and resolution | Strategic Phase uses board game orders; Personal Phase uses TTRPG Domain Echoes |
| Thread → Faction transitions | Standard handoff rule (Thread pool, faction-scale Ob) | Faction-card Thread orders (Weave/Investigate/Harvest) — no battle-phase Thread in BG | Personal Phase: TTRPG. Strategic Phase: board game. Both count toward seasonal Thread Tension. |

> **Mid-siege conversion (PP-090):** Mid-siege mode switch: each Endurance lost by defender in TTRPG scene = −0.5 Fortification (round down). Unit Strength lost = −1 BG Strength per full TTRPG Strength point. Commander Wounds = Morale −1 to their unit in subsequent BG turns.

> **Phase order (PP-089):** Hybrid season phase order: Strategic Phase first, Personal Phase second (fixed). Domain Echo consequences from Personal Phase apply at start of next season Strategic Phase. Seasonal ±2 attribute cap shared across both phases.

> **Rendering Stability timing (PP-253):** PP-089 "next season" deferral applies to faction stat Domain Echoes only. RS changes from Thread operations apply immediately in both phases. RS is a live world track with no seasonal buffer; the ±2 faction stat cap does not govern it.

**Hybrid Strategic Phase Thread effects (PP-267):** Temporal auto-effects and paradox windows are not generated by Thread operations at strategic scale. Co-Movement cards produce narrative RS changes only. Paradox windows require personal-scale Leap contact; no faction Thread order generates them. This prevents paradox window tracking at BG scale.

**Thread in mass battle (TTRPG/Hybrid only):** Offensive Thread operations (Dissolution, Pulling, Locking) fire in Phase 4 — between Manoeuvre and Engagement. Support Thread operations (Weaving, Mending) fire in Phase 6 Cascade step 4–5. Damage from all phases (Volley, Thread, Engagement) applies simultaneously at Phase 6 Step 1. Board Game has no battle-phase Thread — faction Thread orders are abstracted to Co-Movement cards at strategic scale only.

**Key principle for hybrid**: Where a rule exists in both modes, the seasonal cap is shared. A faction attribute cannot change by more than ±2 per season regardless of how many sources target it in either phase.

**Zoom In cannot delay accounting consequences (PP-259):** Seasonal Accounting fires at its scheduled point regardless of any active Zoom In suspension. A Zoom In cannot be used to delay an imminent TC threshold check, victory condition check, or any other accounting-phase consequence. If Accounting is due while a Zoom In is active, Accounting resolves immediately; the Zoom In scene resumes or is aborted at GM discretion.

**Theocracy Counter cap — seizure classification (PP-254):** Territory seizure TC gains are a distinct category, not Domain Actions. All TC sources combined (Domain Actions, Mandate accrual, seizure, Thread operations, military outcomes) are subject to the existing ±5/season combined cap. The ±3 DA sub-cap does not apply to seizure.
---

## 11.8 GM Reference Card — Zoom In / Zoom Out (ED-055b)

*Laminate and keep at table. Content drawn from §11.2–11.3.*

| Term | Definition |
|------|-----------|
| Zoom In | GM narrows scale. Player gets one exchange at personal/scene scale. |
| Zoom Out | GM widens scale. Mass battle continues at reduced command efficiency. |
| Register Shift | Social scene changes nature. Unmask or external event triggers. |
| Domain Echo | Personal success produces faction consequence. No extra roll. |

**Eight Handoff Rules (summary):**
Personal→Thread: Leap action. Personal→Faction: GM recognises scope, Domain Action resolves. Personal→Scene: Roll serves as opening move or Appeal. Scene→Faction: Domain Echo on sufficient scope. Thread→Faction: Thread pool, faction-scale Ob. Thread→Mass: Offensive=Phase 2; Support=Phase 5. Mass→Personal: Phase 5, one exchange, named targets become Contested Figures. Scene→Mass: Social outcome affects mass combat opening state.

**Multiple simultaneous Zoom Ins (PP-252):** Two or more PCs triggering Zoom In at the same phase-lock point resolve their exchanges in Attunement order (higher first). Ties: higher Agility. Further ties: GM. Consequences of each exchange are visible to subsequent PCs before their exchange resolves.

**Contested Figure wound on Zoom Out (ED-167 provisional):** If a Contested Figure is wounded but not killed during a Zoom In exchange, the wound carries back to BG as +1 Ob to that commander's tactic rolls for the remainder of the current battle. Death = Stage 2 general consequences (existing rules). If the CF is killed during one PC's exchange and another PC's Zoom In has not yet resolved (ED-168 provisional): the second PC may redirect to any other named Non-Player Character in the zone, or Zoom Out immediately with no action consumed.

**Zoom In state to track:** PC location, current scale, actions remaining, mass battle turn state.
**Zoom Out trigger:** Exchange complete, or PC incapacitated.

**PC incapacitation during Zoom In — Stage 1 timing (PP-251):** Stage 1 general consequences (−1 Morale all units, Command halved, Morale floor suspended) fire immediately on Zoom Out, before mass battle resumes at its next phase. Incapacitation is a fact; consequences do not wait for Phase 6.
