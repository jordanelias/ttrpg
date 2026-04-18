# THREADWEAVING × COMBAT STRESS TEST MATRIX v2
## 35 cells across 6 clusters — all novel intersections
## Reconstructed from: threadweaving_redesign_v25.md + stage8_combat.md (post-push)
## Pure combat and pure thread isolation already tested. This matrix covers ONLY the intersection.

---

## Terminology (current — absorb before simulation)

| Old Term | Current Term | Notes |
|---|---|---|
| Intelligibility | **Coherence** | 10→0 countdown, practitioner rendering stability |
| TT (Thread Tension) | **RS (Rendering Stability)** | 100→0, world track, inverted direction |
| Health = Endurance + 6 | **Health = Endurance** | Flat, no +6 |
| Wound Ob penalty | **None** | Wounds are dramatic thresholds with zero combat penalty |
| Wound Ob to Thread ops | **+1 Ob per Wound** | Still applies to Leap, Weaving, Pulling, Mending, FR |

---

## Character Profiles (shared across clusters)

| ID | Profile | Combat Pool | Stamina | Health | Weapon | Armour | TS | Focus | Spirit | Attunement | TPS |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | Baseline fighter (non-practitioner) | 11 (Agi 3×2 + Hist 2 + 3) | 5 (End 3 + Hist 1 + 1) | 3 | LightCut Short | Light | 0 | — | 3 | — | — |
| P2 | Combat practitioner (Stirring) | 11 | 5 | 3 | LightCut Short | Light | 35 | 3 | 4 | 3 | 3 |
| P3 | Attuned practitioner (combat-capable) | 9 (Agi 2×2 + Hist 2 + 3) | 4 | 3 | LightCut Short | None | 55 | 4 | 5 | 4 | 5 |
| P4 | Sensitive practitioner (high TS, weak combat) | 7 (Agi 1×2 + Hist 2 + 3) | 4 | 3 | Unarmed | None | 75 | 5 | 6 | 5 | 7 |
| P5 | Heavy fighter (non-practitioner) | 13 (Agi 3×2 + Hist 4 + 3) | 7 (End 5 + Hist 1 + 1) | 5 | HeavyCut Long | Heavy | 0 | — | 2 | — | — |
| P6 | Threadcut being (Mode 3) | 11 | 5 | 4 | N/A (Thread ops) | None | 80 | 6 | 6 | 5 | 8 |
| P7 | Wounded Attuned practitioner | 9 | 4 | 3 (1W taken) | LightCut Short | Light | 55 | 4 | 5 | 4 | 5 |
| P8 | Resonant practitioner (involuntary Leap risk) | 9 | 4 | 3 | LightCut Short | None | 92 | 5 | 5 | 5 | 9 |

---

## CLUSTER A — LEAP/DIAGNOSIS ACTION ECONOMY IN COMBAT (5 cells)

Tests how the Leap's Priority 5 full-round action and Diagnosis Priority 4 interact with the pool-split simultaneous combat system.

| Cell | Test | Profiles | Question | Rules Engaged |
|---|---|---|---|---|
| A-01 | Diagnosis round action economy | P3 vs P1 | P3 declares Diagnosis (Priority 4) during combat. What happens to their pool split? Diagnosis is a standard action — does the practitioner still split Offence/Defence, or is the round consumed? If they split, do they attack while Diagnosing? | §2.2 Priority 4 vs §8.2 Declaration/Split |
| A-02 | Leap round defensive posture | P3 vs P1 | P3 declares Leap (Priority 5, full-round). Only reactive defence available. How does "reactive defence" interact with the pool-split system? Is the entire Combat Pool allocated to Defence? Does opponent get +2D (as per Full Guard logic)? | §2.3 Leap + §8.4 Full Guard/OOB |
| A-03 | Contact rounds under combat pressure | P2 vs P1 | P2 Leaps (Focus 3 = 3 contact rounds, 2 operation rounds). Opponent attacks each round. Does simultaneous resolution mean P2 takes damage during contact? Does Wound disruption (Attunement check Ob 1) trigger per round hit? | §2.3 Contact Duration + §8.2 Simultaneous Resolution |
| A-04 | Initiative interaction with Thread declaration | P3 vs P1 (P3 has initiative) | P3 holds initiative, declares Thread Operation. P1 sees this declaration before committing split. Does P1 gain tactical advantage from knowing P3 is threading (all-Offence against a Defence-only target)? How does initiative asymmetry affect practitioner vulnerability? | §8.3 Initiative + §2.3 Leap declaration |
| A-05 | Multi-round Diagnosis + Leap sequence | P3 vs P1 + P1b (2v1) | P3 faces 2v1. Must spend Round N on Diagnosis, Round N+1 on Leap, Round N+2+ on operations. During Diagnosis and Leap rounds, P3 is Defence-only or reduced. How many rounds of vulnerability before first operation? What is survival probability across this window against 2 attackers with Fibonacci +1D? | §2.2 + §2.3 + §8.7 Group + §8.8 Fibonacci |

---

## CLUSTER B — WEAVING IN COMBAT (5 cells)

Tests Weaving operations (healing, stabilization) performed during active combat.

| Cell | Test | Profiles | Question | Rules Engaged |
|---|---|---|---|---|
| B-01 | Object-scale Weaving to close a wound mid-fight | P3 (1W) vs P1 | P3 has taken 1 Wound. Leaps, Weaves Object-scale (Ob 1, TN 7) to close wound. Does wound removal reset Health? Does healing complete before the opponent's simultaneous attack resolves? Timing of wound removal vs incoming damage in same round. | §2.4 Weaving Object + §8.7 Wounds + §8.2 Simultaneous |
| B-02 | Weaving while taking damage (wound disruption) | P3 vs P5 | P3 is in contact, attempting Weaving. P5 hits P3 this round, dealing enough damage to Wound. Attunement disruption check fires. If check fails, contact drops — does the Weaving attempt auto-fail? If check succeeds, does the new Wound add +1 Ob to the Weaving roll retroactively or only next operation? | §2.3 Wound Disruption + §2.4 Weaving + §8.2 Simultaneous |
| B-03 | Weaving on an ally mid-combat (Personal scale) | P3 + P7 vs P1 + P1b | P3 Weaves on wounded ally P7 (Personal-scale, Ob 2). P3 is Defence-only during Leap. P7 continues fighting. Does P3 need line-of-sight/proximity to target? Can P3 target P7 while P7 is in a different engagement pair (different zone state)? | §2.4 Weaving Personal + §8.8 Group Combat zones |
| B-04 | Overweaving in combat (multiple operations in one contact window) | P3 vs P1 | P3 has Focus 4 (3 operation rounds). Attempts two sequential Weaving operations. Second Overweave: +1 Ob. If first Weaving succeeds and second fails: what is the combat state? Does sequential failure penalty (+1 Ob to remaining ops) stack with Overweave penalty? | §2.4 Overweaving + Sequential failure penalty |
| B-05 | Weaving Relational-scale mid-combat (over-actualisation in combat context) | P4 vs P1 + P1b | P4 attempts Relational Weaving mid-fight (e.g., binding an agreement to cease hostilities). Ob 3, Coherence −1. On success: the Woven configuration is brittle per GM sidebar. If combat resumes (the agreement is stressed), does it shatter into a Shifting Object mid-scene? | §2.4 Weaving Relational + Over-Actualisation + Brittleness sidebar |

---

## CLUSTER C — PULLING IN COMBAT (5 cells)

Tests Pulling operations (loosening, disruption, temporal manipulation) during active combat.

| Cell | Test | Profiles | Question | Rules Engaged |
|---|---|---|---|---|
| C-01 | Pulling on an opponent's personal configuration mid-fight | P3 vs P1 | P3 Pulls on P1's configuration (Personal scale, normally actualized = Ob 2). On success: what is the rendered combat effect? The opponent's configuration is loosened — does this translate to a mechanical combat penalty? Duration = end of scene (0 surplus). | §2.4 Pulling Personal + combat effect gap |
| C-02 | Pulling on weapon configuration (Object scale) | P3 vs P5 | P3 Pulls on P5's weapon (Object scale, Ob 1). On success: the weapon's configuration is loosened. Does this degrade weapon stats (Hit TN, damage modifier)? Duration = end of scene. On failure: snap-back 1 Wound to P3 (no armour). | §2.4 Pulling Object + §8.5 Weapon System |
| C-03 | Pulling failure snap-back during combat | P2 vs P5 | P2 attempts Pull and fails. Takes 1 Wound (no armour), RS −2, Coherence −1. Does this Wound trigger the Attunement disruption check for contact (or has contact already resolved for this round)? Is the snap-back Wound simultaneous with combat damage? | §2.4 Pulling Failure + §2.3 Wound Disruption + §8.2 Simultaneous |
| C-04 | Pulling to loosen armour configuration | P4 vs P5 | P4 Pulls on P5's Heavy armour (Object scale, firmly actualized = Ob 3). On success: armour DR is reduced? Armour ceases functioning? Duration = end of scene. What is the mechanical translation of "loosened armour configuration"? | §2.4 Pulling Object + §8.6 Armour |
| C-05 | Pulling while Wounded (+1 Ob stack) | P7 vs P1 | P7 (1 Wound) attempts Pull. +1 Ob from Wound. Total Ob = normally actualized (2) + Wound (1) = 3. Pool: Spirit 5 + History 2 + TPS 5 = 12D. P(≥3 at TN 7) probability? Is this still viable or does Wound Ob push Pulling out of reach for wounded practitioners? | §2.4 Pulling + Wound Ob + probability |

---

## CLUSTER D — FORCED RESOLUTION IN COMBAT (5 cells)

Tests Lock, Dissolution, and Mending performed during active combat scenes.

| Cell | Test | Profiles | Question | Rules Engaged |
|---|---|---|---|---|
| D-01 | Locking an opponent's weapon (Object Lock) | P3 vs P5 | P3 Locks P5's weapon (Object, Ob 4). On success: weapon is frozen — unable to become. Does this mean the weapon cannot be used (its configuration is rigid)? Does the Lock have chronic RS drift? What if P5 retrieves a different weapon? | §2.4 Lock Object + §8.5 Weapon + Lock chronic |
| D-02 | Dissolution on an Object mid-combat | P3 vs P5 | P3 Dissolves P5's weapon (Object, Ob 4). On success: weapon ceases to exist. RS −5, Gap forms (1 scene). Mid-combat Gap: does the micro-Gap at the weapon's location affect adjacent fighters? Monstrous Incursion risk in a melee? | §2.4 Dissolution Object + Gap consequences |
| D-03 | Dissolution Failure cascade in combat | P3 vs P1 + P1b | P3 attempts Dissolution and gets Failure. RS −8, Monstrous Incursion, Practitioner Incapacitated. Full Gap tears open mid-fight. How does this interact with the ongoing combat? Does the Monstrous Incursion become a third combatant? Does the Gap affect zone states? | §2.4 Dissolution Failure + §8.8 Group + Monstrous Incursion |
| D-04 | Mending a Gap that opened during combat | P3 + P4 | A Gap opened mid-combat (from a prior Dissolution or external event). P4 attempts to Mend while P3 defends. Mending pool = Attunement + Focus + TPS. Mending requires Diagnosis (Priority 4) + Leap (Priority 5) + operation round. How many rounds of vulnerability while Mending? Is the Mending Ob affected by combat-scene temporal pressure? | §2.4 Mending + §2.2 Diagnosis + combat action economy |
| D-05 | Lock on a practitioner's configuration mid-fight (Personal Lock) | P4 vs P3 | P4 Locks P3's personal configuration (Ob 5). On success: P3 is unable to become — frozen. What does this mean in combat? Is P3 incapacitated? Can P3 still fight (their body is Locked in current state)? Does Lock prevent healing? Does Lock prevent death (configuration cannot change)? | §2.4 Lock Personal + combat state interaction |

---

## CLUSTER E — COMPLEX CROSS-SYSTEM INTERACTIONS (10 cells)

High-complexity intersections requiring sustained reasoning across multiple foundation principles and mechanical subsystems.

| Cell | Test | Profiles | Question | Rules Engaged | Blockers |
|---|---|---|---|---|---|
| E-01 | Weaving stat output on a weapon (Object enhancement) | P3 + weapon | P3 Weaves on ally's weapon (Object, Ob 1). On success: what changes? Does Weaving add to damage, improve Hit TN, add DR? No rule specifies Thread operation stat output on equipment. | §2.4 Weaving Object + §8.5 Weapon | **GAP-TC-01** |
| E-02 | Pulling stat output on armour (Object degradation) | P3 vs P5 armour | P3 Pulls on P5's armour. On success: what degrades? DR reduction? Stamina mod removal? No rule specifies Thread operation stat output on equipment. | §2.4 Pulling Object + §8.6 Armour | **GAP-TC-01** |
| E-03 | Weaving stat output on a person (Personal enhancement) | P3 → P7 | P3 Weaves on P7 (Personal, Ob 2). Does this heal wounds? Add temporary Health? Boost Combat Pool? No rule specifies Thread operation stat output on persons in combat. | §2.4 Weaving Personal + §8.1 Combat Pool | **GAP-TC-01** |
| E-04 | Involuntary Leap mid-melee (TS 90+) | P8 vs P1 + P1b | P8 (TS 92) is in melee. Nearby Thread operation triggers involuntary Leap risk (Focus check TN 7 Ob 1). P8 fails check. What happens to their pool split? Are they immediately Defence-only? Does the involuntary Leap produce a contact window with no declared intentionality? | §2.3 Involuntary Leap + §8.2 Round Structure |
| E-05 | Past-Oriented Pulling to reverse a combat Wound | P4 (wounded) | P4 has taken a Wound during this fight. Attempts Past-Oriented Pulling (same scene = Ob 3, + TPS÷2 pool) to reverse the Wound event. Does temporal displacement of the Wound restore Health? Does the Wound's damage "un-happen"? Memories remain (Temporal Disjunction) — allies remember P4 being wounded but the wound is gone. Does this interact with §8.7 wound thresholds? | §2.4 Past-Oriented Pulling + §8.7 Wounds + Temporal Disjunction | Requires §9.10 reversion logic |
| E-06 | Personal Lock on self in combat (self-preservation Lock) | P4 in extremis | P4 is near incapacitation (2W of 3 max). Locks own personal configuration (Ob 5). On success: P4 cannot change — cannot take further Wounds (configuration frozen). But also cannot heal, cannot be Pulled, cannot act (acting = becoming = impossible while Locked). Is this a valid survival tactic? Does it produce a combat stalemate? **Editorial ruling received: [record ruling here].** | §2.4 Lock Personal + §8.7 Wounds + Lock ontology (P-06) | E-06 editorial |
| E-07 | Dissolution of an opponent mid-melee (Personal Dissolution) | P4 vs P1 | P4 Dissolves P1's personal configuration (Ob 5). On overwhelming/success: P1 ceases to exist as a rendered being. This is lethal. RS −5 to −8. Gap at P1's location. Is Personal Dissolution a one-hit kill mechanic? What defences exist? Can P1 resist? How does this interact with P-01, P-02 (inseparability, Ein Sof fullness)? | §2.4 Dissolution Personal + P-01, P-02, P-06, P-08 |
| E-08 | Dissolution creating Gap mid-group-combat | P4 vs P1 in 3v3 | P4 Dissolves an Object mid-fight; Gap forms. Gap persists for the scene. All fighters are in proximity to an active Gap. Effects: TS 30+ perceive it; non-practitioners experience wrongness; Certainty checks? Does the Gap affect combat mechanically (zone disruption, morale)? How does it interact with Fibonacci/zone states? | §2.4 Dissolution + Gap effects + §8.8 Group Combat |
| E-09 | Mending an active Gap mid-fight while allies defend | P4 + P3 + P2 vs Monstrous Entity | A Gap opened (from prior Dissolution or Monstrous Incursion). P4 attempts Mending while P3 and P2 fight the entity. Mending pool: Att 5 + Focus 5 + TPS 7 = 17D. Standard Gap Ob 5. But P4 is in a combat scene — is there a time pressure modifier? Monstrous entity targets P4 (the practitioner): can P3/P2 intercept? Rescue mechanic applicability? | §2.4 Mending + §8.8 Rescue + Monstrous Incursion rules |
| E-10 | Weaving a weapon during active use (Object Weaving on held weapon) | P2 with damaged weapon | P2's weapon is degraded (from a Pull or environmental damage). P2 Weaves on their own weapon (Object, Ob 1) while in combat. Can a practitioner Weave on an object they're holding? Does the weapon need to be put down (rendering vulnerability)? Does the Weaving affect the weapon's stats? | §2.4 Weaving Object + §8.5 Weapon | **GAP-TC-01** |

---

## CLUSTER F — THREADCUT BEINGS AND EDGE CASES (5 cells)

| Cell | Test | Profiles | Question | Rules Engaged |
|---|---|---|---|---|
| F-01 | Threadcut being in personal combat (no Leap required) | P6 vs P1 + P1b | P6 (threadcut) can perform Thread operations without Leaping. In combat, P6 can attack AND operate in the same round? No Leap = no Priority 5 full-round action = no Defence-only constraint? Does this make threadcut beings overwhelmingly powerful in combat? | §6.3 External operations + §8.2 Round Structure |
| F-02 | Rendering Strain accumulation during prolonged combat | P6 vs P1 × 4 | P6 performs external Thread operations during a 6-round combat. Each operation: +1 Rendering Strain. At Health 4: De-Actualisation at RS = 4. How many operations before De-Actualisation triggers? Can P6 balance combat and self-preservation? | §6.3 + §6.4 De-Actualisation triggers |
| F-03 | De-Actualisation sequence during active combat | P6 (RS threshold crossed) vs P1 | P6 triggers De-Actualisation mid-fight. Round 1: all ops +2 Ob, intelligible face dissolving. Round 2: +4 Ob, perceivable only by TS 50+. Round 3+: returns to ground, micro-Gap. How does the 3-round sequence interact with ongoing combat? Can P6 still fight while de-actualising? Can P6 attempt self-stabilisation Weaving while under attack? | §6.4 De-Actualisation sequence + §8.2 combat rounds |
| F-04 | Coherence 4–3 (Fragmented) practitioner in combat | P3 at Coherence 3 | P3 enters combat at Coherence 3: −1D social rolls, −1D Memory, +1 Ob to all Thread ops including Leap. Roll Fragmented Fallout. How does +1 Ob to Leap compound with Wound Ob? At 1W + Coherence 3: Leap Ob = base (1) + Wound (1) + Fragmented (1) = 3. Pool: Att 4 + Hist 2 + TPS 5 = 11D. Viable? How does Memory penalty interact with Thread declaration (declared operations are set during Diagnosis — is Diagnosis a Memory-dependent act)? | §3.3 Coherence thresholds + §2.2 Diagnosis + §2.3 Leap |
| F-05 | Rendering Crisis (Coherence 0) triggering during combat | P3 at Coherence 1 | P3 performs a Relational operation in combat, taking Coherence from 1 to 0. Rendering Crisis fires. "Campaign event, not passive state." But the character is mid-fight. Does combat pause for the narrative event? Does P3 become an NPC immediately? Can allies defend P3 while the crisis resolves? | §3.3 Rendering Crisis + combat continuity |
| F-06 | Threadcut being Pulling on itself during combat | P6 in combat | P6 attempts to Pull on its own configuration to loosen self-maintenance rigidity (reduce over-actualisation from continuous Lock-like self-rendering). This is Pulling directed at a threadcut configuration — the being is Pulling on the thing that sustains its existence. +1 Rendering Strain (external op cost). Does the Pull accelerate De-Actualisation? Is this mechanically equivalent to voluntary cessation? Requires De-Actualisation round tracking against P-06 (unable to become). | §6.3 + §6.4 + §2.4 Pulling + P-06 |

---

## GAPS (pre-simulation)

| Gap ID | Description | Cells Blocked |
|---|---|---|
| GAP-TC-01 | Weaving/Pulling stat output on weapons, armour, persons — no rule specifies what Thread operations DO to combat stats | E-01, E-02, E-03, E-10 |
| GAP-TC-02 | Diagnosis action economy in combat — Priority 4 but no explicit pool-split ruling | A-01 (testable with assumptions) |
| GAP-TC-03 | Leap defensive posture — "reactive defence" not mapped to pool-split vocabulary | A-02 (testable with assumptions) |
| GAP-TC-04 | Pulling combat effect on persons — what does "loosened configuration" mean for combat stats? | C-01 |
| GAP-TC-05 | Personal Lock combat implications — frozen configuration vs ongoing combat | D-05, E-06 |
| GAP-TC-06 | Threadcut action economy — no Leap means no full-round constraint? | F-01 |
| GAP-TC-07 | Monstrous Incursion as combatant — no stat block or combat integration rules | D-03, E-08, E-09 |

---

## EDITORIAL RULINGS RECEIVED

| ID | Ruling | Date | Cells Unblocked |
|---|---|---|---|
| E-06 | Personal Lock in combat — **[ruling content: to be confirmed from handoff]** | This session | E-06, downstream to E-07, E-08, E-09 |

---

## EXECUTION ORDER

```
Stage 1 — Mode A: Isolation simulations (cells with no editorial blockers)
  Priority: B-01, B-04, D-04 (no blockers, clean test questions)
  Then: A-01 through A-05, B-02, B-03, B-05, C-01 through C-05, D-01 through D-03, D-05
  Flag: cells requiring assumptions about unmapped rules

Stage 2 — Gap surfacing
  After Stage 1: present GAP-TC-01 through GAP-TC-07 with simulation evidence
  User resolves or provides editorial guidance

Stage 3 — Mode B: Interaction chains (cross-cluster)
  After gaps resolved: E-04 through E-09, F-01 through F-06
  Opus required for: E-05, E-06 downstream, F-06

Stage 4 — Mode C: Constructed scenarios
  3 worst-case compound scenarios combining findings from Stages 1-3
```

---
*Document version: v2 RECONSTRUCTED — 2026-03-29*
*Source: threadweaving_redesign_v25.md + stage8_combat.md (post-push)*
*All pure combat isolation and pure thread isolation excluded — already tested.*
