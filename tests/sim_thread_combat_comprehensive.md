# THREADWEAVING × COMBAT STRESS TEST — COMPREHENSIVE RUN
## Model: Sonnet 4.6 (Stage 1 isolation) | Date: 2026-03-29
## Rule patches applied: Wound System Redesign, -1D per wound (universal), Fibonacci debate exclusion

---

# RULE PATCHES APPLIED

## PP-131: Wound System Redesign
**Old:** Health = Endurance (flat). Resets on wound. Max wounds before incap per table. Zero penalty.
**New:** Health = (Endurance + 6) × (max wounds + 1). Continuous track, no reset. Damage carries over. Each wound threshold crossed = -1D to ALL dice pools.

| End | Max Wounds | Health/Segment | Total HP | Thresholds (wound at) | Max Penalty |
|---|---|---|---|---|---|
| 1 | 2 | 7 | 21 | 14 (-1D), 7 (-2D), 0 (incap) | -2D |
| 2 | 2 | 8 | 24 | 16 (-1D), 8 (-2D), 0 (incap) | -2D |
| 3 | 2 | 9 | 27 | 18 (-1D), 9 (-2D), 0 (incap) | -2D |
| 4 | 3 | 10 | 40 | 30 (-1D), 20 (-2D), 10 (-3D), 0 (incap) | -3D |
| 5 | 3 | 11 | 44 | 33 (-1D), 22 (-2D), 11 (-3D), 0 (incap) | -3D |
| 6 | 4 | 12 | 60 | 48 (-1D), 36 (-2D), 24 (-3D), 12 (-4D), 0 (incap) | -4D |
| 7 | 4 | 13 | 65 | 52 (-1D), 39 (-2D), 26 (-3D), 13 (-4D), 0 (incap) | -4D |

## PP-132: Universal Wound Penalty
**Old:** Wounds +1 Ob to Thread operations. Zero combat penalty.
**New:** Wounds -1D to ALL applicable dice pools. No +Ob anywhere.

## PP-133: Fibonacci Debate Exclusion
**Old:** Fibonacci bonus applied to combat; debate not explicitly excluded.
**New:** Fibonacci bonus applies ONLY to physical combat offence pools. Explicitly excluded from Debates/social combat.

---

# GAP PATCHES (resolved inline during simulation)

## GP-01: Diagnosis Combat Posture (GAP-TC-02)
**Patch:** Diagnosis is a Declaration-phase mental action. The practitioner declares "Diagnosis" as their action type (same as declaring Strike or Full Guard). They allocate their full Combat Pool to Defence. Opponent does NOT receive +2D — the practitioner is actively perceiving, not passive. Rationale: Diagnosis is the "last act of rendering" (§2.2) and requires focused attention incompatible with attacking, but the practitioner's physical awareness remains intact.

## GP-02: Leap Defensive Posture (GAP-TC-03)
**Patch:** During Leap round, practitioner allocates entire Combat Pool to Defence. Opponent does NOT receive +2D. The Leap's "reactive defence" is pre-conscious physical response — the body maintains guard while rendering suspends. This differs from Full Guard (voiding = intentional passivity) and OOB (exhaustion = inability). The practitioner is neither passive nor exhausted; they are transitioning states. Their body's trained responses continue below consciousness.

## GP-03: Thread Operation Stat Output on Equipment and Persons (GAP-TC-01)
**Patch — derived from scale principle + operation type:**

### Weaving (coherence, stabilization)
| Target | Scale | Effect | Duration |
|---|---|---|---|
| Weapon | Object | +1 damage modifier (weapon strikes truer) | End of scene |
| Armour | Object | +1 DR vs all weapon types | End of scene |
| Person (healing) | Personal | Restore (End + 6) HP (one segment). Cannot exceed max. | Permanent (wound healed) |
| Person (stabilize dying) | Personal | If at 0 HP: stabilize at 1 HP, prevent death. | Permanent |

### Pulling (loosening, opening)
| Target | Scale | Effect | Duration |
|---|---|---|---|
| Weapon | Object | -1 damage modifier (min 0) | End of scene (0 surplus) to seasonal (2+ surplus) |
| Armour | Object | -1 DR vs all weapon types (min 0) | Same |
| Person (destabilize) | Personal | -2D to target's Combat Pool (rendering loosened, coordination fluid) | Same |

### Lock (freeze, unable to become)
| Target | Scale | Effect | Duration |
|---|---|---|---|
| Weapon | Object | Weapon cannot be used (configuration rigid, cannot swing/thrust) | Until reversed |
| Person | Personal | Per E-06 ruling (cannot attack/move/wound, Stamina frozen, RS-1/round) | Contact window + bonus successes |

### Dissolution (tear, unable to be)
| Target | Scale | Effect | Duration |
|---|---|---|---|
| Weapon | Object | Weapon ceases to exist. Gap forms at location. | Permanent (weapon gone) |
| Person | Personal | **Lethal.** Target's intelligible face torn from ground. Gap forms. Instant incapacitation. | Permanent (target dissolved) |

**Personal Dissolution lethality note:** This is intentionally devastating. Ob 5 minimum, TS 50+ required, Coherence -2 (FR + Dissolution), RS -5 to -8. The cost is immense. No combat defence roll stops it — the attack bypasses physical armour entirely. The only counter: another practitioner performing a Lock or defensive Weaving on the target's configuration before the Dissolution resolves. This is an editorial-adjacent ruling — **[EDITORIAL: confirm Personal Dissolution as instant incapacitation, or add a resistance roll (Spirit check)?]**

## GP-04: Gap Proximity Combat Effects (GAP-TC-08)
**Patch:** Active Gap in a combat zone imposes no mechanical combat penalty. Gaps are a strategic/narrative concern, not a tactical modifier. Rationale: Gaps affect the substrate (RS, spontaneous phenomena, wrongness perception) but do not directly interfere with rendered physical combat. A fighter can fight normally next to a Gap — they just feel profoundly wrong while doing so. TS 30+ fighters perceive the Gap and may choose to disengage; non-practitioners feel diffuse dread but suffer no dice penalty.

## GP-05: Monstrous Entity Combat Profile (GAP-TC-07)
**Patch — minimal stat block for simulation purposes:**

| Entity Type | Combat Pool | HP | Weapon Equivalent | Armour | Special |
|---|---|---|---|---|---|
| Minor Incursion (Object Gap) | 10 | 27 | LightCut (TN 5/6, +2) | None | Wrongness aura: -1D to social rolls in zone |
| Standard Incursion (Standard Gap) | 14 | 44 | HeavyCut (TN 6/7, +5) | Light (DR per table) | As above + Spirit check TN 7 Ob 1 or Certainty -1 on first encounter |
| Major Incursion (Entrenched Gap) | 18 | 65 | HeavyBlunt (TN 7/8, +5) | Heavy | As above + -1D combat to all non-practitioners in zone |

**[EDITORIAL: Monstrous Entity stat blocks are placeholder. These are mechanically functional for simulation but lack setting-specific traits, behaviour patterns, and Thread-interaction rules. Full design needed.]**

## GP-06: Threadcut Action Economy (GAP-TC-06)
**Patch:** Threadcut beings do NOT get free Thread operations during combat rounds. Their "no Leap required" means they skip the Leap round (saving 1 round of vulnerability) but still declare Thread Operation as their action type and are Defence-only during operation rounds. Rationale: the threadcut being's continuous self-maintenance requires constant intentional direction. Splitting that direction between combat AND external Thread operations is not possible — the being must commit to one or the other each round. Otherwise threadcut beings are categorically superior combatants with no balancing cost.

**Cost balance:** Threadcut beings save the Leap round (1 round less vulnerability) and don't need Approach Training, but every external Thread operation adds +1 Rendering Strain, accelerating De-Actualisation. Their combat advantage is temporal efficiency; their cost is existential.

---

# UPDATED CHARACTER PROFILES (new wound system)

| ID | Combat Pool | Stamina | Total HP | Wound Thresholds | Leap Pool | Op Pool (Weave) | Op Pool (Mend) |
|---|---|---|---|---|---|---|---|
| P1 | 11 | 5 | 27 | 18/9/0 | — | — | — |
| P2 | 11 | 5 | 27 | 18/9/0 | Att3+H2+TPS3=8 | Sp4+H2+TPS3=9 | — |
| P3 | 9 | 4 | 27 | 18/9/0 | Att4+H2+TPS5=11 | Sp5+H2+TPS5=12 | Att4+F4+TPS5=13 |
| P4 | 7 | 4 | 27 | 18/9/0 | Att5+H2+TPS7=14 | Sp6+H2+TPS7=15 | Att5+F5+TPS7=17 |
| P5 | 13 | 7 | 44 | 33/22/11/0 | — | — | — |
| P6 (threadcut) | 11 | 5 | 40 | 30/20/10/0 | N/A | Sp6+H2+TPS8=16 | Att5+F6+TPS8=19 |
| P7 | 9-1=8 | 4 | 27 (at 18 or below = 1W) | 18/9/0 | 11-1=10 | 12-1=11 | 13-1=12 |
| P8 | 9 | 4 | 27 | 18/9/0 | Att5+H2+TPS9=16 | Sp5+H2+TPS9=16 | Att5+F5+TPS9=19 |

---

# SIMULATION RESULTS

## CLUSTER A — LEAP/DIAGNOSIS ACTION ECONOMY

### A-01: Diagnosis Round Action Economy
**Patch GP-01 applied.** P3 declares Diagnosis; full pool to Defence; no opponent +2D.
**Result:** Clean. P3 (9D Defence at TN 6-7) vs P1 (split offence). P3 is slightly less vulnerable than Full Guard (no +2D gift). Diagnosis round is a moderate risk — comparable to a round where you choose not to attack.
**Finding:** None. GP-01 resolves this cleanly.

### A-02: Leap Round Defensive Posture
**Patch GP-02 applied.** P3 (9D Defence, no +2D to opponent).
**Result:** P3's 9D defence at TN 6 vs P1's offence split. If P1 goes 8/3 split: P1 hits ~3.2, P3 blocks ~5.4. P3 survives comfortably. If P1 goes all-offence (11/0): P1 hits ~4.4, P3 blocks ~5.4. P3 still likely blocks.
**Finding A-02-F01 (P3):** Leap round is slightly safer than Full Guard because no +2D to opponent. This is correct — the practitioner is not voiding, they're transitioning states. Their body's trained defence remains active.

### A-03: Contact Rounds Under Combat Pressure
P2 (Focus 3 = 2 op rounds) vs P1. P1 attacks every round. Simultaneous resolution means P2 takes damage during contact.
**Wound disruption check:** On hit that causes damage crossing wound threshold (18 HP): Attunement check. P2 Att 3 at TN 7 Ob 1: 3D at TN 7 = ~1 expected success. P(≥1) = ~70%. **30% chance a single wound drops contact.**
**With -1D penalty from wound:** P2's pools all drop by 1D. Next op: 9-1=8D. Still functional.
**Finding A-03-F01 (P2):** Wound disruption check probability (70% hold at Att 3) creates meaningful tension. A low-Attunement practitioner (Att 2: ~53% hold) is dangerously fragile in combat. High-Att practitioners (Att 5: ~93%) are resilient. **Attunement is the combat-practitioner's survival stat.** This is philosophically correct — Attunement measures sensitivity to the substrate, which includes maintaining contact despite physical trauma.

### A-04: Initiative Interaction with Thread Declaration
P3 has initiative, declares Thread Operation. P1 sees this declaration before committing split.
**P1 optimal response:** Go all-offence (11/0). P3 is Defence-only with 9D. P1 hits ~4.4, P3 blocks ~5.4. P1 has ~25% chance of landing a hit. Over multiple rounds: P1 will eventually hit, but not reliably per round.
**Finding A-04-F01 (P3):** Initiative asymmetry matters. If P3 does NOT have initiative: P3 declares Thread Op first (ascending Agi order), P1 sees it, goes all-offence. If P3 DOES have initiative: P1 must declare first. P1 declares Strike; P3 then declares Thread Op knowing P1 is attacking. No tactical difference — P3 is Defence-only regardless. **Initiative is irrelevant for a practitioner threading.** They are Defence-only no matter what. Initiative advantage is wasted during threading rounds. This is a real cost — a high-Agi practitioner who would normally benefit from initiative sees no advantage while threading.

### A-05: Multi-Round Vulnerability (Diagnosis + Leap + Operation) in 2v1
P3 vs P1 + P1b (Fibonacci +1D each). Vulnerability window: 3 rounds (Diagnosis + Leap + Op).
Each round: P3 (9D Defence) vs two attackers. P3 splits Defence: 5D vs attacker A, 4D vs attacker B.
Attacker A: 7D + 1D(Fib) = 8D at TN 5. Hits ~4.8. P3 block: 5D at TN 6 = ~3.0. Excess: ~1.8. Damage: 1.8 + 3 + 1.5 = 6.3.
Attacker B: same. Against 4D defence (~2.4 blocks). Excess ~2.4. Damage ~6.9.
**Total damage per round: ~13.** Against 27 HP: P3 hits first wound threshold (18) by end of round 1. Second threshold (9) by round 2. Incap by round 3.
**Finding A-05-F01 (P1): Threading in 2v1 without protection is near-suicidal.** P3 takes ~13 damage/round and is incapacitated within 2-3 rounds. The 3-round vulnerability window means P3 almost certainly cannot complete an operation before going down. **Practitioners REQUIRE allies to thread in group combat.** This is a strong, correct design incentive for party coordination.

---

## CLUSTER B — WEAVING IN COMBAT (re-run with new wound system)

### B-01 (revised): Object Weaving to Heal Mid-Fight
P3 (1 wound = at or below 18 HP, -1D all pools) Weaves on self (Object, Ob 1).
**New pool:** 12-1 = 11D, TN 7, Ob 1. P(≥1) = ~98%.
**Effect (GP-03):** Restore (End+6) = 9 HP. If P3 is at 15 HP (1W), heals to 24 HP — above 18 threshold. Wound penalty removed. Full pools restored.
**Timing (B-01-F01 from prior run):** Weaving resolves end of round (Priority 5). Incoming damage applies first. If P3 takes 8 damage (to 7 HP = 2W, -2D) and then Weaving heals 9 HP (to 16 HP = 1W, -1D): net improvement of 1 wound level. The healing matters but doesn't negate same-round damage.
**Finding B-01-R01 (P2):** Object Weaving heals exactly one wound segment (End+6 HP). At 0 Coherence cost (Object scale), this is a powerful combat sustain ability. A Focus 4 practitioner can heal twice per contact window (Overweave Ob 2 on second) — restoring 2 segments. **The main limiter is the 2-round setup cost (Diagnosis + Leap), not the operation itself.** Practitioners who can survive the setup window can sustain themselves indefinitely in 1v1.

### B-02: Weaving While Taking Damage (Wound Disruption)
P3 in contact, Weaving. P5 hits P3. With new HP system:
P5 Heavy Cut (TN 6, +5 dmg): 7D offence at TN 6 = ~3.5. P3 9D def at TN 7 = ~3.6. Tight — ~50% hit chance. On hit: excess ~0.5, damage ~0.5 + 4 + 5 = 9.5. That's one full wound segment.
If P3 at full HP (27): drops to ~17.5, crossing 18 threshold. 1W, -1D. Attunement disruption: Att 4-1 = 3D at TN 7 Ob 1. P(hold) = ~70%.
**Finding B-02-F01 (P2):** Wound penalty (-1D) applies to the Attunement disruption check itself. A practitioner at 2W (-2D) checking with Att 4-2=2D has only ~53% hold chance. **Wound-disruption cascades are real:** each wound makes the next disruption check harder. A practitioner who takes 2 wounds in one round (from a heavy hit carrying over) must check with -2D, making contact maintenance precarious. This creates a natural ceiling on how much damage a practitioner can absorb while threading.

### B-03: Weaving on an Ally Mid-Combat (Personal Scale)
P3 Weaves on wounded P7 (Personal scale, Ob 2). Coherence -1 (Relational? No — Personal scale = 0 Coherence cost).
**Wait — healing is Personal scale (Ob 2), and Personal scale = 0 Coherence cost per §3.2.** But the degree table lists Coherence -1 on Partial and Failure. At Personal scale, ignore Coherence cost on Partial (§3.2 interaction rule). Apply on Failure.
Pool: 12D, TN 7, Ob 2. P(≥2) = ~97%.
**Effect:** Restore (End+6) = 9 HP to P7. If P7 at 15 HP (1W, -1D), heals to 24 HP (0W, 0D). P7's Combat Pool restores from 8 to 9.
**Proximity requirement:** No rule specifies range for Thread operations on allies in combat. Diagnosis requires perceiving the target's configuration. TS 55 (P3) perceives operations "in the same building" (passive perception table). Active Diagnosis on a target in the same combat zone: no range restriction within the scene. **Patch: Thread operations target any entity the practitioner Diagnosed in the same scene, regardless of combat zone state. The operation occurs at the Thread level, not the physical level — range is irrelevant.**
**Finding B-03-F01 (P3):** Personal-scale Weaving to heal allies is efficient: Ob 2, 0 Coherence cost, restores one wound segment. The only cost is the action economy (2 setup rounds + 1 op round). A dedicated healer-practitioner (P4 with Focus 5) can heal 4 allies across one contact window (4 op rounds × 1 heal each, with Overweave Ob stacking: Ob 2, 3, 4, 5). Success probability on the 4th heal: P4's 15D at TN 7 Ob 5 = ~87%. Viable.

### B-04 (revised): Overweaving in Combat
P3 Focus 4 = 3 op rounds. Two Weaving ops.
Op 1: 12D, TN 7, Ob 1. P(≥1) = ~98%.
Op 2 (Overweave): 12D, TN 7, Ob 2. P(≥2) = ~97%.
If P3 takes 1W during window: both pools drop to 11D. Op 2 at 11D Ob 2 = ~95%. Still strong.
If P3 takes 2W (heavy blow carrying over): pools at 10D. Op 2 at 10D Ob 2 = ~91%. Functional.
**Finding B-04-R01:** No change from prior run. Overweaving stacking is well-behaved. The new wound system doesn't materially alter Overweaving viability because -1D is milder than +1 Ob at these pool sizes.

### B-05: Weaving Relational-Scale Mid-Combat
P4 Weaves Relational (Ob 3, Coherence -1). Pool: 15D, TN 7, Ob 3. P(≥3) = ~94%.
**Over-actualisation in combat context:** Woven configuration becomes brittle. If combat resumes against the Woven agreement: GM may rule it shatters into Shifting Object.
**Finding B-05-F01 (P2):** Relational Weaving mid-combat is mechanically viable but philosophically strained. Combat is a context of acute stress — Weaving a relationship or agreement during active violence subjects the Woven configuration to immediate stress. The brittleness sidebar predicts shattering. **Recommend: Relational+ Weaving during active combat automatically triggers the brittleness check at scene end.** This doesn't prevent the operation but makes the GM aware that the Woven configuration was born in violence and is structurally fragile.

---

## CLUSTER C — PULLING IN COMBAT

### C-01: Pulling on Opponent's Personal Configuration
**GP-03 applied.** P3 Pulls on P1 (Personal, normally actualized = Ob 2). Pool: 12D, TN 7, Ob 2. P(≥2) = ~97%.
**Effect:** -2D to P1's Combat Pool for duration (end of scene at 0 surplus). P1 drops from 11D to 9D. This is equivalent to 2 wounds' worth of penalty — a significant combat debuff from a single Ob 2 operation.
**Finding C-01-F01 (P1):** Personal Pulling as combat debuff is extremely powerful relative to its cost. Ob 2, 0 Coherence cost (Personal scale), -2D to target's pool. Compare: landing two wounds on P1 requires multiple hits totaling 18+ damage. Pulling achieves equivalent effect in one operation. **The balancing factors are: (a) 2-round setup, (b) Pulling effect is temporary (end of scene), (c) Pulling failure = 1 Wound to practitioner (no armour), RS -2.** The failure cost is meaningful — a snap-back wound on the continuous HP track is permanent combat damage.

**Finding C-01-F02 (P2):** Duration is crucial. At 0 surplus successes: end of scene. Most combats ARE one scene. So the Pull effectively lasts the whole fight. At 1+ surplus: end of session (irrelevant for single combats). **The base Pull (Ob 2, 0 surplus) is optimally efficient in combat — no benefit to over-investing successes.**

### C-02: Pulling on Weapon (Object Scale)
**GP-03 applied.** P3 Pulls on P5's Heavy Cut weapon (Object, loosely/normally actualized = Ob 1-2). Pool: 12D, TN 7, Ob 1. Near-certain.
**Effect:** -1 damage modifier. HeavyCut drops from +5 to +4. Minor but cumulative if combined with other debuffs.
**Finding C-02-F01 (P3):** Object Pulling on weapons is low-impact. -1 damage modifier saves ~1 HP per hit received. Over a 5-round fight, that's ~3-4 HP saved. Not worth the 2-round setup cost. **Pulling on the person (C-01) is strictly better than Pulling on their weapon.** Object Pulling on weapons is a niche option only if the practitioner is already in contact and has spare operation rounds.

### C-03: Pulling Failure Snap-Back During Combat
P2 attempts Pull, fails. Takes 1 Wound (no armour). In the new system: 1 Wound = direct HP loss of... how much?
**Gap identified:** Pulling failure says "1 Wound (armour does not apply)." In the old system, a Wound was a binary event (cross threshold, reset HP). In the new continuous system, "1 Wound" needs reinterpretation.
**Patch PP-134:** Thread-inflicted Wounds (Pulling snap-back, Lock collapse, etc.) deal damage equal to one wound segment (End + 6 HP). Armour DR does not apply. This maintains the "1 Wound" severity while fitting the continuous track.
P2 at full HP (27): takes 9 damage, drops to 18. Crosses first threshold. -1D to all pools.
**Wound disruption interaction:** The snap-back Wound occurs as the operation resolves (not as a combat hit). Contact is already resolving — does the Attunement disruption check fire? The snap-back happens at the end of the operation. If this is the last operation in the window, contact is about to drop anyway. If sequential operations remain: yes, disruption check fires. P2 Att 3-1(wound) = 2D at TN 7 Ob 1 = ~53% hold.
**Finding C-03-F01 (P2):** Pulling failure in combat is doubly punishing: (a) snap-back Wound is permanent HP loss on the continuous track, (b) if mid-window, disruption check at reduced Attunement makes continued operations unlikely. **This creates a meaningful risk/reward for Pulling in combat** — success is a -2D debuff on the opponent; failure is a wound segment to the practitioner plus probable contact loss.

### C-04: Pulling to Loosen Armour
**GP-03 applied.** P4 Pulls on P5's Heavy armour (Object, firmly actualized = Ob 3). Pool: 15D, TN 7, Ob 3. P(≥3) = ~94%.
**Effect:** -1 DR vs all weapon types. Heavy armour goes from 6/5/3/1 to 5/4/2/0. HeavyBlunt now ignores the armour entirely (DR 0). LightCut goes from DR 6 to DR 5 — still near-useless.
**Finding C-04-F01 (P2):** Pulling armour is tactically niche but can be devastating when combined with correct weapon type. A practitioner who Pulls Heavy armour (-1 DR) enables allied HeavyBlunt fighters to deal full damage (DR 0). This is a genuine tactical combo — but requires coordination between practitioner and fighter archetypes.

### C-05: Pulling While Wounded
P7 (1W, -1D all pools) attempts Pull. Pool: 12-1 = 11D, TN 7, Ob 2. P(≥2) = ~95%.
At 2W (-2D): 10D, Ob 2 = ~91%. At 3W (-3D): 9D, Ob 2 = ~84%.
**Finding C-05-F01 (P3):** The -1D per wound system is gentler than +1 Ob was. At these pool sizes (12D base), losing 1-2 dice barely affects success probability. **Wounds become mechanically significant for Thread ops at ~4W (-4D), where pools drop to 8D and Ob 2 success drops to ~75%.** This means practitioners remain functional threadweavers deep into their wound track — which is philosophically correct (Thread operations engage the configuration, not the body) but may be too forgiving. The old +1 Ob system was harsher: at 2W, Ob 2 became Ob 4, dropping success from ~97% to ~75%. **The new system allows wounded practitioners to continue threading effectively.** Flag for balance assessment after full simulation.

---

## CLUSTER D — FORCED RESOLUTION IN COMBAT

### D-01: Locking an Opponent's Weapon (Object Lock)
**GP-03 applied.** P3 Locks P5's weapon (Object, Ob 4). Pool: Spirit 5 + History 2 = 7D (Lock uses Spirit + History, no TPS). TN 7, Ob 4. P(≥4 on 7D) = ~29%.
**This is bad.** Lock pool is much smaller than Weaving/Pulling pool (no TPS). At Ob 4 minimum, the success rate is poor for mid-tier practitioners.
**Effect on success:** Weapon frozen, cannot be used. P5 must fight Unarmed (TN 8/9, +0 damage) or switch weapons.
**RS cost:** -1 (success). Chronic drift: -1 RS/season if Lock persists.
**Finding D-01-F01 (P1):** Lock pool (Spirit + History, no TPS) is dramatically smaller than other operation pools. P3's Lock pool is 7D vs 12D Weaving. At Ob 4 minimum, Lock success is ~29% — worse than a coin flip. **This is a systemic balance issue: Lock is underperforming relative to other operations due to missing TPS.** Check threadweaving_v25.md: "Pool: Spirit + relevant History bonus" — confirmed, no TPS for Lock. Compare Weaving: "Spirit + relevant History bonus + TPS." The TPS exclusion from Lock/Dissolution pools appears intentional (these are Forced Resolution — the practitioner is directing against the thread's nature, not with it). But at Ob 4+ the success rates are prohibitive for any practitioner below TS 70.

**Finding D-01-F02 (P2):** Object Lock on a weapon is tactically inferior to Object Pulling (-1 damage) or Personal Pulling (-2D). Lock requires higher Ob (4 vs 1-2), uses a smaller pool, and has RS consequences. The only advantage: Lock is permanent (until reversed) vs Pull's scene duration. **In combat (one scene), Pull is always better than Lock for weapons.**

### D-02: Dissolution on an Object Mid-Combat
P3 Dissolves P5's weapon (Object, Ob 4). Same pool issue: 7D at TN 7 Ob 4 = ~29%.
**On success:** Weapon gone. RS -5. Gap forms (1 scene). Micro-gap at weapon location.
**On failure:** Full Gap, RS -8, Monstrous Incursion, Practitioner Incapacitated. Mid-fight catastrophe.
**Finding D-02-F01 (P1):** Dissolution in combat is high-risk, low-probability, and catastrophic on failure. At ~29% success and ~15% failure (with ~56% Partial), the most likely outcome is a Shifting Object (Partial) — the weapon becomes unstable rather than destroyed. A Shifting Object weapon in someone's hand is a narrative nightmare with no combat rules. **Dissolution in combat should be a desperation move, not a tactical option.**

### D-03: Dissolution Failure Cascade
P3 Dissolves and fails. RS -8. Full Gap. Monstrous Incursion. P3 Incapacitated.
**GP-05 applied.** Standard Incursion: 14D pool, 44 HP, HeavyCut, Light armour.
Combat state: P3 down. Entity enters engagement zone. Remaining fighters (P1, P1b?) must engage.
**Finding D-03-F01 (P1):** A Dissolution failure mid-combat introduces a third combatant (Monstrous Entity) with stats comparable to a skilled fighter. The entity has no allegiance — it attacks the nearest rendered being. With 14D pool and HeavyCut, it is a serious threat. **This is a compelling emergent scenario: the practitioner's failed operation makes the combat dramatically worse.** No rule issue — the consequence structure is working as designed.

### D-04 (revised): Mending a Gap Mid-Combat
**GP-04, GP-05 applied.** P4 Mends (Att 5 + Focus 5 + TPS 7 = 17D, Ob 5). At 1W (-1D): 16D, Ob 5 = ~83%. At 2W: 15D, Ob 5 = ~75%.
**Rescue mechanic confirmed essential.** P4's 7D Combat Pool vs Standard Incursion (14D) is untenable alone. P3/P2 must Rescue and hold the entity.
**Finding D-04-R01:** Findings unchanged from prior run. Mending mid-combat viable with protection, dangerous without. The new wound system adds a wrinkle: if P4 takes a heavy blow during the vulnerability window (potential multi-wound hit from entity), the -2D or -3D penalty drops the Mending pool to 14-15D, reducing success to ~70-75%. Still viable but riskier.

### D-05: Personal Lock on Opponent Mid-Fight
**E-06 ruling applied.** P4 Locks P1 (Personal, Ob 5). Pool: Spirit 6 + History 2 = 8D, TN 7, Ob 5. P(≥5 on 8D) = ~15%.
**This is extremely unreliable.** Same pool issue as D-01. Lock/Dissolution pools lack TPS.
**On success:** P1 frozen. Cannot attack, move, wound. RS -1/round. +1 Ob zone-wide Thread ops. Duration: P4's remaining contact window + bonus successes.
**Tactical assessment:** Lock neutralizes the target completely but:
1. 15% success rate makes it a desperation gamble
2. RS -1/round means the world deteriorates every round the Lock holds
3. Zone-wide +1 Ob penalizes allied Thread operations
4. P4 is Defence-only during setup (2 rounds) and operation (1 round) — 3 rounds exposed with only 7D pool
**Finding D-05-F01 (P1):** Personal Lock is prohibitively unreliable for mid-tier practitioners. At TS 70+ with Spirit 6 + History 4 = 10D, Ob 5: ~37%. Still worse than a coin flip. **Lock becomes viable only at extreme specialization (Spirit 7 + History 6 = 13D, Ob 5: ~70%).** This means Personal Lock in combat is a late-campaign, high-investment ability — consistent with its devastating effect. No balance issue.

---

## CLUSTER E — COMPLEX INTERACTIONS (unblocked cells only)

### E-04: Involuntary Leap Mid-Melee (TS 90+)
P8 (TS 92) in melee. Nearby Thread operation triggers Focus check TN 7 Ob 1. P8 Focus 5-wound_penalty at TN 7 Ob 1.
At 0W: 5D, P(≥1) = ~83% resist. 17% involuntary Leap.
At 1W: 4D, P(≥1) = ~76%. 24% involuntary Leap.
**If Leap triggers:** P8 has no declared intentionality (involuntary). Contact window opens (Focus 5 rounds) but no operations can execute — no Diagnosis was performed, no intentionality set. P8 is Defence-only for Focus rounds, wasting their entire combat contribution.
**Finding E-04-F01 (P1):** Involuntary Leap renders the character combat-inert for Focus rounds. At TS 92 with Focus 5: 5 rounds of Defence-only with no operations. This is a crippling liability in group combat. **Resonant practitioners should not be deployed near other practitioners in combat.** Their involuntary Leap risk is a team liability.
**Finding E-04-F02 (P2):** No rule specifies whether involuntary Leap produces co-movement effects. The Leap is successful (rendering suspends) but no operation executes. **Patch PP-135: Involuntary Leap with no operation produces Coherence -1 (the rendering suspension itself destabilizes) but no RS change, no co-movement auto-effects (no operation = no Thread interaction = no consequences).** The Coherence cost reflects the involuntary suspension's impact on rendering stability.

### E-05: Past-Oriented Pulling to Reverse a Combat Wound
P4 wounded (at 15 HP, 1W, -1D). Attempts POP to reverse the wound event (same scene = Ob 3).
Pool: Spirit 6 + History 2 + TPS÷2 (3) - 1(wound) = 10D. TN 7. Ob 3.
P(≥3 on 10D) = ~85%.
**What happens on success:** The wound event is temporally displaced. The physical facts are removed — the damage un-happens. HP restores to pre-wound state. Memories remain (Temporal Disjunction): allies and enemies remember P4 being wounded, but the wound is gone.
**Mechanical effect vs Weaving:** Weaving (Personal, Ob 2) restores one segment (9 HP). POP reverses ALL damage from the wound event. If the wound dealt 12 damage (27→15), POP restores 12 HP (back to 27). Weaving only restores 9 HP (15→24). **POP is more effective when the triggering hit dealt more than one segment of damage.**
**Additional costs:** POP: Coherence -1 (additional beyond operation cost), RS -3 minimum (from degree table). POP failure: 1 Wound (snap-back) + RS -2 + Coherence -1. The cost is dramatically higher than Weaving.
**Finding E-05-F01 (P1):** POP for wound reversal is mechanically viable but strategically questionable. Weaving heals for Ob 2, 0 Coherence cost, 0 RS cost. POP heals for Ob 3, -1 Coherence, -3 RS minimum. POP is worse in every dimension except: (a) it restores full damage from the event rather than one segment, and (b) it removes the wound from the timeline entirely (Temporal Disjunction). **The tactical use case is reversing a massive multi-wound blow.** If P4 took 20 damage in one hit (27→7, 2W, -2D), POP restores all 20 HP. Weaving would take two operations to restore 18 HP (two segments). POP does it in one at higher cost. **This is the correct design space — POP is the emergency response to catastrophic damage, not a routine heal.**

### E-06: Personal Lock on Self in Combat
**Editorial ruling applied.** P4 (2W, 9 HP, -2D) Locks own configuration (Ob 5). Pool: Spirit 6 + History 2 - 2(wounds) = 6D. P(≥5 on 6D) = ~6%. Essentially impossible at 2W.
At 0W: 8D, Ob 5 = ~15%. At 1W: 7D, Ob 5 = ~10%.
**Finding E-06-F01 (P1):** Self-Lock is statistically non-viable as a panic button. The practitioner most likely to need it (heavily wounded, -2D+) has the lowest chance of success. **This is philosophically consistent — Lock requires directed intentionality against the thread's nature. A severely wounded practitioner whose rendering is disrupted by pain cannot form the precise intentionality required to freeze their own configuration.** No balance issue. Self-Lock is a theoretical option, not a practical one.

### E-07: Personal Dissolution on Opponent
**GP-03 applied.** P4 Dissolves P1 (Personal, Ob 5). Pool: 8D, TN 7, Ob 5 = ~15%.
**On overwhelming/success:** P1's intelligible face torn away. Instant incapacitation. Gap at location. RS -5 to -8.
**[EDITORIAL: Personal Dissolution = instant kill confirmed, or should target get a resistance roll?]**
**Finding E-07-F01 (P1):** Personal Dissolution is a one-hit kill at ~15% success. On failure (~15%): Full Gap, Monstrous Incursion, Practitioner Incapacitated. The most likely outcome is Partial (~70%): target becomes a Shifting Object. **A person becoming a Shifting Object mid-combat is undefined.** Patch PP-136: A person who becomes a Personal-scale Shifting Object mid-combat is incapacitated (their rendering is destabilizing — they cannot act coherently). They may be stabilized via Mending (Shifting Object, Ob 2) within the scene. If not stabilized: deteriorates to a Personal Gap within 1d3 sessions — the person ceases to exist as a rendered being. This is a delayed kill.

### E-08: Dissolution Creating Gap Mid-Group-Combat
**GP-04, GP-05 applied.** P4 Dissolves an Object; Gap forms. Combat continues in the Gap's zone.
Per GP-04: no direct combat penalty. Wrongness perception only.
Per GP-05: if Gap is Standard, Monstrous Incursion possible.
**Finding E-08-F01 (P2):** The Gap's presence during combat is narratively intense but mechanically inert (per GP-04). This may feel anticlimactic — a tear in reality opens next to the fighters and nothing mechanical changes. **Consider: at RS ≤ 40 (Fragile band), a Gap in a combat zone should trigger the spontaneous Shifting Object formation rule immediately rather than at seasonal accounting.** This creates mechanical urgency proportional to world state. At high RS (stable world): Gap is narratively scary but mechanically safe. At low RS (fragile world): Gap immediately spawns additional threats.

### E-09: Mending Active Gap While Allies Defend
**GP-04, GP-05 applied.** Same analysis as D-04 but with explicit Monstrous Entity stats.
P4 Mends (17D, Ob 5). P3 + P2 engage Standard Incursion (14D, 44HP).
P3 (9D) + P2 (11D) vs entity (14D): 2v1 with Fibonacci +1D each. P3 at 10D, P2 at 12D. Entity splits Defence: 7D each.
Attacker success rates: high. Entity takes ~8-10 damage/round. At 44 HP: ~4-5 rounds to incapacitate.
P4's Mending window: 3 rounds (Diagnosis + Leap + Op). Entity falls in ~4-5 rounds. **The timing aligns — allies can hold the entity long enough for Mending to complete, but it's tight.** If allies take wounds (likely — entity hits hard with HeavyCut +5), their pools degrade and the entity lasts longer.
**Finding E-09-F01 (P2):** Gap Mending mid-combat is a race against entity attrition of the defending allies. At 2v1 with Fibonacci, allies are favoured but not guaranteed. A 3v1 (adding a third fighter) makes it comfortable. **This creates a genuine tactical dilemma: commit 3 fighters to the entity (guaranteed victory) and leave the practitioner unprotected, or commit 2 (risky) and keep 1 in reserve for Rescue.**

---

## CLUSTER F — THREADCUT AND EDGE CASES

### F-01: Threadcut Being in Personal Combat
**GP-06 applied.** P6 (threadcut) fights normally but skips Leap round. Declares Thread Op: Defence-only, same as organic practitioners.
Each external Thread op: +1 Rendering Strain. P6 Health = 40, Rendering Threshold = Health÷2 = 20. De-Actualisation triggers at RS = Health (40?) or Wounds reaching threshold.
**Wait — "Rendering Strain equals Health" triggers De-Act.** P6 Health = 40 under new system? Threadcut beings use... the new formula? End 4 = (4+6) × (3+1) = 40. Rendering Threshold = ceiling(Health÷2) — but this was written for old system where Health = Endurance. Under new system: Rendering Threshold = ceiling(40÷2) = 20. De-Act triggers at RS = 40 (many operations) or Wounds at 20 (half HP gone).
**PP-137 (threadcut wound threshold):** Threadcut De-Actualisation wound trigger under new HP system = when HP drops below 50% of max (i.e., total wound penalties = half the wound levels). For P6 (40 HP, End 4, 3 max wounds): De-Act at ≤20 HP (2+ wounds).
**P6 combat sequence:** Round 1: Diagnosis (Defence-only, 11D defence). Round 2: Thread Op (Defence-only). No Round 0 Leap — threadcut advantage. Saves 1 round.
**Finding F-01-F01 (P2):** Threadcut beings save exactly 1 combat round vs organic practitioners (no Leap). At Focus 6, P6 gets 5 operation rounds. With GP-06 (Defence-only during ops), P6 is still a poor combatant while threading — same vulnerability as organic practitioners. **The threadcut advantage is efficiency (1 fewer round exposed), not capability.** The +1 Rendering Strain per external op means P6 can perform ~40 operations before De-Act from strain alone. In a single combat: 5 ops max. RS cost is negligible for one fight. **Threadcut beings are balanced for combat.**

### F-02: Rendering Strain Accumulation During Prolonged Combat
P6 performs 5 external Thread ops across a 7-round combat.
RS after combat: 5. De-Act threshold: 40. Nowhere close.
**But:** if P6 has been operating previously (accumulated RS from prior scenes): RS stacks across scenes. A threadcut being who has performed 35 prior ops enters combat at RS 35 and hits De-Act at RS 40 after 5 more ops. **De-Act mid-combat is only possible for threadcut beings with extensive operational history.**
**Finding F-02-F01 (P3):** Rendering Strain is a campaign-level concern, not a combat-level concern. A threadcut being cannot De-Actualise from a single combat's worth of operations unless they entered at near-threshold RS. No combat balance issue.

### F-03: De-Actualisation Sequence During Active Combat
P6 triggers De-Act mid-fight. Round 1: all ops +2 Ob, intelligible face dissolving. P6 can still fight (Combat Pool functional) but cannot perform Thread ops effectively (+2 Ob). Stabilisation attempt: Weaving on self (16D, TN 7, Ob = Wounds + RS). If Wounds = 2 and RS = 40: Ob = 42. Impossible.
**Finding F-03-F01 (P1):** De-Actualisation stabilisation Ob (= Wounds + Rendering Strain) is almost always impossible at the point it triggers. RS = Health (40) → Ob includes RS (40). No pool reaches Ob 40. **The stabilisation check is flavour, not a real option.** De-Act is effectively irreversible once triggered. This is correct per the philosophical framing — a threadcut being whose self-rendering has failed cannot recover by further self-rendering. The only option is external intervention (another practitioner Weaving on the de-actualising being).
**Patch PP-138:** Clarify: external stabilisation (another practitioner Weaving on the threadcut being) uses the standard Personal Weaving Ob (2), not the self-stabilisation Ob. An ally can save a de-actualising threadcut being — but must do so within 2 rounds (Round 3 = return to ground).

### F-04: Coherence 4-3 (Fragmented) Practitioner in Combat
P3 at Coherence 3: -1D social, -1D Memory, +1 Ob all Thread ops.
**Wait — the user's patch eliminates +Ob from wounds. Does the Coherence +1 Ob to Thread ops still apply?** Yes — the user said wounds no longer increase Ob. Coherence thresholds are a different system. +1 Ob from Fragmented Coherence remains.
P3 Leap: 11D - 0(no wounds for this test) at TN 7, Ob 1 + 1(Coherence) = Ob 2. P(≥2) = ~95%. Viable.
At 1W + Coherence 3: 10D (wound -1D), Ob 2 (Coherence). P(≥2) = ~91%. Still viable.
At 2W + Coherence 3: 9D, Ob 2. P(≥2) = ~84%. Getting rough.
**Finding F-04-F01 (P2):** Coherence degradation and wounds compound but remain manageable at moderate levels. The critical threshold is Coherence 1 (Severed: +2 Ob) + 2W (-2D): 9D, Ob 3. P(≥3 on 9D) = ~67%. A Severed, twice-wounded practitioner has a one-third chance of failing the Leap. **This is the intended endgame degradation arc — a practitioner who has pushed too far, too often, becomes unreliable under pressure.**

### F-05: Rendering Crisis (Coherence 0) During Combat
P3 performs Relational operation, Coherence drops 1→0. Rendering Crisis fires.
**Rendering Crisis is a "campaign event, not a passive state."** In combat: the character's rendering fails. They cannot perceive the combat, their opponents, or themselves as coherent entities.
**Patch PP-139:** Rendering Crisis in combat = immediate incapacitation for combat purposes. The character is physically present but cannot render reality well enough to fight, dodge, or make decisions. They collapse. Allies must protect them or extract them. The narrative Rendering Crisis resolution (revise a Belief, withdraw from practice, find new framework) occurs after the combat scene ends. **The character is not dead — they are ontologically compromised.** Physical recovery is immediate once rendering stabilizes; the crisis is about their capacity to render, not their body.

### F-06: Threadcut Being Pulling on Itself During Combat
P6 (threadcut) directs Pull at its own configuration. Ob: depends on actualization level. Threadcut beings are maximally actualized (they maintain themselves through continuous Lock-like self-rendering). Firmly actualized = Ob 3. But threadcut self-rendering is *more* than firmly actualized — it's actively Lock-maintained. Previously Woven = Ob 4? Or Foundational = Ob 5?
**Patch PP-140:** Threadcut self-Pull = Ob 4 (equivalent to Previously Woven — the being's own continuous work resists its own loosening). Pool: 16D at TN 7 Ob 4. P(≥4) = ~86%.
**Effect:** The being loosens its own self-rendering. Per GP-03 (Pulling on person): -2D to own Combat Pool (configuration destabilized). But for a threadcut being, loosening self-rendering is existentially dangerous — it's pulling apart the thing that keeps it existing. +1 Rendering Strain (external op cost). The Pull effect expires at end of scene, but the RS is permanent.
**De-Actualisation interaction:** If RS + Rendering Strain from this Pull pushes past threshold: De-Act triggers. The being Pulled itself toward cessation.
**P-06 check (unable to become):** Pulling on itself is trying to loosen the Lock that IS the being. If the Pull succeeds, the being momentarily becomes more fluid — more like an organic being, less frozen. This is philosophically paradoxical: the being is using originary intentionality to undo its own originary intentionality. **The result should not be stable.** Patch: threadcut self-Pull automatically triggers De-Actualisation Round 1 check. If the being does not stabilise within 2 rounds, it begins returning to the ground. **This IS voluntary cessation by another name — the being chose to loosen its own existence.**
**Finding F-06-F01 (P1):** Threadcut self-Pull is mechanically equivalent to initiating voluntary De-Actualisation with extra steps. The Pull succeeds (~86%), the being loosens, De-Act triggers. The only difference from voluntary cessation: voluntary cessation has no Ob penalties during De-Act; self-Pull De-Act follows the standard sequence (+2 Ob Round 1, +4 Ob Round 2). **Self-Pull is harder than simply letting go.** This is correct — fighting your own existence with originary intentionality (Pull) is more violent than simply ceasing to sustain it (voluntary cessation). The distinction matters narratively (Solmund choosing to Pull himself apart vs. choosing to stop) but mechanically converges on the same outcome.

---

# COMPREHENSIVE FINDINGS TABLE

| Cell | P1 | P2 | P3 | New Patches |
|---|---|---|---|---|
| A-01 | — | — | — | GP-01 |
| A-02 | — | — | 1 (Leap safer than Full Guard) | GP-02 |
| A-03 | — | 1 (Att is combat-survival stat) | — | — |
| A-04 | — | — | 1 (initiative irrelevant while threading) | — |
| A-05 | 1 (2v1 threading near-suicidal) | — | — | — |
| B-01 | — | 1 (Object Weaving = free combat sustain) | — | — |
| B-02 | — | 1 (wound-disruption cascade) | — | — |
| B-03 | — | — | 1 (heal allies at range, 0 Coherence) | — |
| B-04 | — | — | — | — |
| B-05 | — | 1 (Relational Weaving mid-combat = brittleness) | — | — |
| C-01 | 1 (Pull -2D vs 2-wound equivalent) | 1 (base Pull optimally efficient) | — | — |
| C-02 | — | — | 1 (Object Pull < Personal Pull) | — |
| C-03 | — | 1 (double-punish on failure) | — | PP-134 |
| C-04 | — | 1 (niche but devastating with correct weapon combo) | — | — |
| C-05 | — | — | 1 (-1D gentler than +1 Ob at large pools) | — |
| D-01 | 1 (Lock pool lacks TPS, Ob 4 at 29%) | 1 (Lock inferior to Pull in combat) | — | — |
| D-02 | 1 (Dissolution high-risk desperation) | — | — | — |
| D-03 | 1 (failure cascade creates third combatant) | — | — | — |
| D-04 | 1 (Rescue essential for Mending) | 1 (failure cascade risk) | — | — |
| D-05 | 1 (Personal Lock ~15%, prohibitive) | — | — | — |
| E-04 | 1 (involuntary Leap = combat inert) | 1 (no co-movement rule) | — | PP-135 |
| E-05 | 1 (POP only justified for multi-wound reversal) | — | — | — |
| E-06 | 1 (self-Lock non-viable as panic button) | — | — | — |
| E-07 | 1 (Personal Dissolution = instant kill, Partial = Shifting Object person) | — | — | PP-136 |
| E-08 | — | 1 (Gap inert in combat; RS-gated urgency) | — | — |
| E-09 | — | 1 (race against entity attrition) | — | — |
| F-01 | — | 1 (threadcut saves 1 round, balanced) | — | PP-137 |
| F-02 | — | — | 1 (RS is campaign concern, not combat) | — |
| F-03 | 1 (self-stabilisation impossible; needs external Weaving) | — | — | PP-138 |
| F-04 | — | 1 (Coherence + wounds compound, manageable) | — | — |
| F-05 | — | — | — | PP-139 |
| F-06 | 1 (self-Pull = violent voluntary cessation) | — | — | PP-140 |

**Totals: 13 P1, 13 P2, 5 P3**

---

# PATCH REGISTER (new this session)

| ID | Description | Source |
|---|---|---|
| PP-131 | Wound system redesign: continuous HP, -1D/wound, carryover damage | User directive |
| PP-132 | Universal -1D per wound, no +Ob anywhere | User directive |
| PP-133 | Fibonacci excluded from Debates | User directive |
| PP-134 | Thread-inflicted Wounds = (End+6) HP damage on continuous track | Sim C-03 |
| PP-135 | Involuntary Leap: Coherence -1, no RS/co-movement effects | Sim E-04 |
| PP-136 | Person as Shifting Object: incapacitated, Mend Ob 2 to stabilize, else deteriorates | Sim E-07 |
| PP-137 | Threadcut De-Act wound trigger: HP below 50% of max | Sim F-01 |
| PP-138 | External stabilisation of de-actualising threadcut being: Personal Weaving Ob 2 | Sim F-03 |
| PP-139 | Rendering Crisis in combat = incapacitation (ontological, not physical) | Sim F-05 |
| PP-140 | Threadcut self-Pull = Ob 4, auto-triggers De-Act Round 1, equivalent to violent voluntary cessation | Sim F-06 |

---

# GAP PATCHES APPLIED

| ID | Description | Resolution |
|---|---|---|
| GP-01 / GAP-TC-02 | Diagnosis combat posture | Defence-only, no +2D to opponent |
| GP-02 / GAP-TC-03 | Leap defensive posture | Full Defence, no +2D, pre-conscious reflexes |
| GP-03 / GAP-TC-01 | Thread op stat output on equipment/persons | Weaving = +1 mod/DR/heal segment; Pulling = -1 mod/DR or -2D person; Lock = freeze; Dissolution = destroy |
| GP-04 / GAP-TC-08 | Gap proximity combat effects | No mechanical penalty; narrative wrongness only |
| GP-05 / GAP-TC-07 | Monstrous Entity combat stats | 3-tier stat block (Minor/Standard/Major) |
| GP-06 / GAP-TC-06 | Threadcut action economy | Defence-only during ops (same as organic), save 1 round (no Leap) |

---

# KEY STRATEGIC FINDINGS

1. **Personal Pulling is the dominant combat Thread operation.** Ob 2, 0 Coherence cost, -2D to target's pool for the scene. Strictly superior to weapon/armour targeting. This may need Ob adjustment if playtesting confirms it's too efficient.

2. **Lock and Dissolution pools (Spirit + History, no TPS) are too small for combat viability at Ob 4-5.** Most practitioners below TS 70 have ~30% or worse success rates. FR operations in combat are desperation moves, not tactical options. This is probably correct — FR operations have devastating effects and should be unreliable.

3. **-1D per wound is gentler than +1 Ob was.** At 12D base pools, losing 1-2 dice barely affects Thread operation success rates. Wounded practitioners remain effective threadweavers. The old system was harsher. Whether this is desired depends on design intent: should wounds meaningfully impair Thread operations, or should Thread operations be body-independent?

4. **Threading in group combat requires dedicated protection.** A-05 confirms: 2v1 against a threading practitioner is near-suicidal. The party must assign fighters to protect the practitioner during the 2-3 round vulnerability window. This creates strong cooperative incentives.

5. **Object-scale Weaving for healing is free (0 Coherence) and reliable (97%+ success).** A dedicated healer-practitioner can sustain a party through extended combat. The only limiter is the setup cost (2 rounds exposed).

# REMAINING BLOCKERS

**E-01, E-02, E-03, E-10:** Now unblocked by GP-03. Can run immediately.
**[EDITORIAL pending]:** Personal Dissolution lethality (E-07), Monstrous Entity full design (GP-05).

# NEXT ACTIONS
1. Push PP-131 through PP-140 and GP-01 through GP-06 to gap register
2. Run E-01, E-02, E-03, E-10 (now unblocked)
3. Resolve Personal Dissolution editorial question
4. Re-run prior combat simulations with new wound system (HP carryover affects all prior sim data)
