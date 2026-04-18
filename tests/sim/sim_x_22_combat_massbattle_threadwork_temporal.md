# SIM-X-22 — Combat + Mass Battle + Threadworking + Temporal Axes
## Cross-System Stress Test

**Test ID:** SIM-X-22  
**Mechanics:** Combat (combat_design_v1), Mass Battle (mass_battle_v3), Thread (threadwork_redesign_v25), Temporal Axes (POP, Co-Movement §4, PP-181/182/192/193/203)  
**Mode:** TTRPG + Hybrid (delta)  
**Temporal:** PAST / PRES / CROSS  
**Tracks:** RS, Coherence, Str, Cohesion, Morale, Health, Stamina, Wounds, Mira Focus  
**Factions:** Lowenritter, Altonian (invasion)  
**NPCs:** Mira (TS70 practitioner-general), Kaspar (combatant), Generic Altonian Commander  
**Archetypes:** Practitioner-general, mass battle + personal combat overlap, temporal manipulation in battle  
**Date:** 2026-04-03  
**Status:** Complete  

---

## Simulator Modes Run

Modes A (Isolation), D (Edge Cases), G (Cross-System Full Scenario — 2 full battle turns + temporal test turn), J (Cognitive Load), K1 (Cross-Mode Delta), K2 (Transition Stress Test), L (Precedent Comparison).

---

## Findings Summary

| ID | Priority | System | Description | Resolution |
|----|----------|--------|-------------|------------|
| F-01 | P1 | Combat+Thread | Diagnosis+Leap 2-round setup vs active opponent (pool 13): E[Stamina lost before first op] = 3.74 of 5. Practitioner likely exhausted before contact window opens. | PP-228 PROVISIONAL — see below |
| F-02 | P1 | Mass Battle+Thread | FR operations (Lock/Dissolution) at Relational scale have 98.3% failure rate at TS70 in mass battle. They still cost RS on failure (×3 multiplier). At RS60, single Lock failure → RS51 (Strained). These ops are tactically inert but world-damaging. | ED-126 — see below |
| F-03 | P1 | Mass Battle+Thread | PP-190 (personal combat Diagnosis+Leap = 2 separate rounds) has no ruling for mass battle phases. Rounds ≠ phases. | PP-224 PROVISIONAL |
| F-04 | P1 | Mass Battle+Thread | Active Thread contact window state during Zoom In to personal combat is undefined. If Mira holds contact from Phase 4, does it persist into Phase 5 personal exchange? | PP-229 PROVISIONAL |
| F-05 | P1 | Mass Battle+Thread | Paradox window scene-tick during Zoom In personal combat is undefined. | PP-230 PROVISIONAL |
| F-06 | P1 | Mass Battle+Thread | Scope of 'scene' and 'session' for RS leakage at Coherence 0 (PP-197) is undefined in mass combat. | PP-223 PROVISIONAL |
| F-07 | P1 | Cognitive Load | Mass battle Thread ops (Load score 18–21) are 2–3× above redesign threshold (9). Novice time 7–11 min/resolution. Unplayable without reference card. | Structural — reference card required (not a patch) |
| F-08 | P2 | Mass Battle+Thread | POP in mass battle: E[RS] = −15.4 per attempt (including temporal auto-effect). At RS60, single POP → Fractured band (~RS38). | Informational finding — PP-201 disclosure extended |
| F-09 | P2 | Mass Battle | Cohesion degradation never fires at expected values in symmetric engagement (DR absorbs damage below Cohesion threshold). Only Thread-Str-loss or high-CP-asymmetry triggers it. | PP-231 PROVISIONAL |
| F-10 | P2 | Thread | Coherence 2 (Fractured band) has no explicit +Ob modifier. Interpolation ambiguous. | PP-221 PROVISIONAL |
| F-11 | P2 | Thread+Mass Battle | Offensive Lock on formation thread: no ruling on whether it blocks Cohesion degradation. This is mechanically powerful if so. | PP-222 PROVISIONAL — ED-122 for confirmation |
| F-12 | P2 | Thread | GAP-5: PP-192 ×3 applies to RS costs — unclear if RS gains (Weaving Overwhelming) also ×3. | PP-225 PROVISIONAL |
| F-13 | P2 | Thread | GAP-2: Temporal auto-effect RS (PP-181) — unclear if ×3 applies in mass battle. | PP-226 PROVISIONAL |
| F-14 | P2 | Mass Battle+Thread | P2 finding: declaration lock (Phase 1 commit) means a failed Offensive Lock leaves practitioner with zero Thread output for the entire turn (cannot pivot to Support Thread). | Informational — design choice confirmed |
| F-15 | P3 | Mass Battle+Thread | POP paradox window (P-22 delayed manifestation) interacts with Phase 5–6 engagement: no ruling on unit stats during window. | PP-227 PROVISIONAL |
| F-16 | P3 | Mass Battle | Coherence Rating cap (P-22 editorial: ED-123) — battle-turn vs scene vs session definitions needed for RS threshold effects. | PP-223 PROVISIONAL |
| F-17 | P3 | Cross-Mode | Hybrid Strategic Phase: temporal auto-effect and paradox windows undefined at strategic scale. | ED-125 |

---

## Provisionals Applied

### PP-221 [PROVISIONAL] — Coherence 2 Ob Penalty
Coherence 2 (Fractured band) = +1 Ob all Thread operations. Consistent with 4–3 band (which also carries +1 Ob). The table's separate listing of social/Memory penalties at Coherence 2 does not preclude the +1 Ob that applies through the Fragmented band. Clarify in Coherence table.

### PP-222 [PROVISIONAL] — Offensive Lock on Formation Thread
An Offensive Lock targeting a unit's formation thread (Cohesion/Morale anchor) blocks Cohesion degradation checks for that unit for the duration of the Lock (minimum 1 season unless Reversed). Rationale: Lock drives actuality to full actualization; "unable to become" (ED-100) means the configuration cannot degrade. Duration: as per standard Lock duration rules. This is mechanically powerful — surfaced as ED-122 for editorial confirmation.

### PP-223 [PROVISIONAL] — Battle-Turn = Scene for RS Threshold Effects
A mass battle turn (all 7 phases) = 1 scene for purposes of: RS leakage at Coherence 0 (PP-197), paradox window scene-tick (P-22), and all other "per scene" Thread mechanics. Phases are sub-units of a scene, not scenes themselves. Rationale: preserves scene scope as a meaningful unit; prevents ×7 amplification of per-scene effects within a single battle turn.

### PP-224 [PROVISIONAL] — Diagnosis+Leap in Mass Battle Phase 4
In mass battle Phase 4 (Offensive Thread), Diagnosis and Leap both occur within the single phase — no 2-round separation. PP-190's 2-round separation rule applies to personal combat rounds only. At mass battle scale, phases are strategic abstractions that subsume multiple personal-scale rounds. The practitioner performs Diagnosis → Leap → Op within Phase 4 as a single action block. (Support Thread: same, within Phase 6 Step 5.)

### PP-225 [PROVISIONAL] — RS ×3 Applies to Gains (Weaving Overwhelming)
PP-192's ×3 multiplier applies to all RS changes from Thread ops in mass battle, including RS gains. Weaving Overwhelming (Relational+) = RS +3 in mass battle (vs +1 personal). Rationale: PP-192 states "all RS costs" — interpreting "costs" as net change (not only losses) is mechanically consistent and avoids the counterintuitive result that the substrate responds asymmetrically to mass-scale interactions.

### PP-226 [PROVISIONAL] — Temporal Auto-Effect NOT Subject to ×3
Temporal auto-effect RS (PP-181 §4.3) is a separate auto-effect system, not an "RS cost from a Thread op" as specified in PP-192. The ×3 multiplier (PP-192) applies only to RS costs generated by operation degree tables. Temporal auto-effect fires independently and at ×1 regardless of combat scale. Rationale: PP-181 explicitly states the temporal auto-effect fires "independent of the operation's own RS cost" — it is structurally separate from the operation's degree outcome.

### PP-227 [PROVISIONAL] — Paradox Window During Mass Battle Engagement
When a POP in Phase 4 produces a delayed manifestation result (P-22 co-movement d6 = 6), the paradox window does not mechanically affect unit stats during Phase 5 engagement or Phase 6 Cohesion/Morale checks. Pre-displacement values are used for all mechanical checks during the paradox window. On window auto-resolution (end of scene = end of battle turn, per PP-223), apply displaced values to Cohesion/Morale. Rationale: P-22 definition: "physical facts have not yet updated" — unit stats are physical facts, not thread-level configurations.

### PP-228 [PROVISIONAL] — Practitioner Combat Vulnerability Signal
The Diagnosis+Leap setup cost (2 combat rounds of defensive-only play, E[Stamina lost] ≈ 3.74/5 vs a pool-13 opponent) is a design-intent vulnerability window, not a bug. The mechanic functions correctly — it means practitioners in personal combat require either: (a) a bodyguard absorbing attacker, (b) a less capable opponent, or (c) a non-combat context. No formula change. Add the following GM guidance note to combat_design_v1 §Practitioner Combat: *"A practitioner Leaping in melee against an active opponent (pool 8+) will typically exhaust their Stamina before their first op fires. Leap in personal combat is intended for practitioners operating with protection, against lower-quality opponents, or outside active melee."*

### PP-229 [PROVISIONAL] — Thread Contact Persistence During Zoom In
If a practitioner holds an active contact window (established via Leap in Phase 4) when the General Zoom In triggers in Phase 5, the contact window is suspended for the duration of the personal combat exchange (1 exchange, Phase 5). On return to mass battle scale, the contact window resumes with Focus count unchanged. The practitioner cannot execute Thread ops during the personal combat exchange (they are in rendering, not contact). Op rounds consumed: none.

### PP-230 [PROVISIONAL] — Paradox Window Tick During Zoom In
A paradox window active at Zoom In (mass battle → personal combat) does not tick down during the personal combat exchange. The personal combat exchange is a sub-scene of the mass battle scene (per PP-223: battle turn = scene). The window resumes counting at scene end.

### PP-231 [PROVISIONAL] — Cohesion Degradation Requires Thread-Assisted Str Loss
At expected values in symmetric mass battle engagement (comparable CP ratings, standard armour), Cohesion degradation does not trigger — DR absorbs enough damage that Str loss per turn is well below Cohesion rating. Cohesion degradation is mechanically active only when: (a) strong CP asymmetry (attacker eff CP ≥ 2× defender), (b) Thread Dissolution directly removes Str, or (c) artillery bombardment (HBl flat damage). This is a design confirmation, not a patch. Add GM note to mass_battle_v3: *"Cohesion degradation is an asymmetry mechanic, not an attrition mechanic. Expect it only in engagements with significant quality disparity or Thread-supported Str loss."*

---

## Editorial Items Added

| ID | Status | Description |
|----|--------|-------------|
| ED-120 | Open | GM mandatory disclosure (PP-204) at RS<24 for Dissolution: consider whether disclosure alone is sufficient given 90.3% Rupture probability. Note: §23.3 perverse incentive is design intent — no mechanical gate proposed. |
| ED-121 | Open | Define 'scene' for mass combat paradox window purposes. PP-223 provisional makes battle-turn = scene. Confirm. |
| ED-122 | Open | Confirm: Offensive Lock on formation thread blocks Cohesion degradation checks (PP-222 provisional). |
| ED-123 | Open | Confirm: battle-turn = scene definition for all RS threshold effects and PP-197 Coherence-0 leakage (PP-223 provisional). |
| ED-124 | Open | Confirm: Diagnosis+Leap collapse to single Phase 4 in mass battle (PP-224 provisional). |
| ED-125 | Open | Define temporal auto-effect and paradox window behaviour in Hybrid Strategic Phase. Currently undefined. |
| ED-126 | Open | FR operations (Lock/Dissolution) in mass battle: 98.3% failure at TS70 (Relational). Options: (a) accept as design (they are deterrents, not tools); (b) reduce mass battle FR Ob by 2; (c) restrict FR to TS90+ in mass battle contexts. Simulation confirms they are currently tactically inert for all practitioners below TS90. |

---

## Scenario Results (Turn-by-Turn)

### Turn 1
- RS: 60 → 51 (one failed Offensive Lock, E cost −9 at ×3)
- Altonian Heavy Infantry Str: 4 → 2.13 (engagement + volley)
- Mira Coherence: 10 → 9 (FR surcharge)
- No Cohesion/Morale triggers

### Turn 2
- RS: 51 → 53.1 (Mira switches to Support Weaving; E[RS] +2.13 from mass battle Weaving)
- Altonian Heavy Infantry Str: 2.13 → 0.37 (effectively destroyed by Turn 3)
- Mira Coherence: 9 → 8 (Relational scale auto-cost)
- Altonian Morale: 5 → 3 (Str < 50% and < 25% both triggered)

### Temporal Axis (Turn 3 projection)
- Single POP attempt: E[RS] −15.4 (base −14.4 + temporal auto −1)
- RS 53.1 → ~37.7: crosses into Fractured band at Accounting
- Coherence: 8 → 7 (POP additional cost)
- P(paradox window) ≈ 7.75% per POP attempt

### Cognitive Load Summary
- Mass Battle Lock: 18/10, novice 9m20s — P1 REDESIGN
- Mass Battle POP: 21/10, novice 10m45s — P1 REDESIGN  
- Personal combat Leap: 12/10, novice 5m45s — P1 REDESIGN
- **All three require reference card to be playable**

---

## Key Design Confirmation (Dominant Strategy)
Support Weaving is the only positive-EV Thread op in mass battle (E[RS] +2.13–+4.4). All other ops are RS-negative. Mending is net positive only with Collective support at TS70+. Lock and Dissolution are near-unusable at standard practitioner pools.

**Optimal practitioner role in mass battle:** Support Weaver in Phase 6, not Offensive FR practitioner.

---

## Patches Applied
PP-221 through PP-231 (all PROVISIONAL). See above.

## Editorial Items: 7 new (ED-120–ED-126). All open.
