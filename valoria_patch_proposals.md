# VALORIA PATCH PROPOSALS
## Consolidated from Batches 02–07
## Date: 2026-03-27 | Status: Proposals only — all require editorial approval before compilation

Format: Each entry = finding ID · severity · mechanic · issue · proposed fix · source batch
P1 = game-breaking | P2 = bad play experience | P3 = minor/design note
[EDITORIAL] tag = requires user decision, not mechanical resolution

---

## P1 PATCHES

---

### PP-001
**Finding:** F-B7-08 / F-B7-16 (consolidated)
**Severity:** P1
**Mechanic:** M-013 (Leap), M-016 (Pulling) — TD accumulation
**Issue:** TD is a permanent one-way ratchet. No recovery mechanic. At TD 15+, Pull success probability is ~2%. Practitioners become permanently non-functional.
**Proposed fix:** Add seasonal TD recovery option. Suggested: a season in which the practitioner performs zero Thread operations recovers TD −3 (represents gradual temporal re-anchoring). Extended withdrawal (full campaign arc, no ops): TD −10. This preserves TD as a meaningful cost while providing a recovery path for sustained campaign play.
**Source:** Batch 07 T-B7-03, T-B7-05

---

### PP-002
**Finding:** F-B7-17
**Severity:** P1
**Mechanic:** M-018 (FR-Dissolution), M-030 (Thread Tension)
**Issue:** A single practitioner's 3-op failure cascade can add TT +9, pushing TT past the global threshold (45) from a mid-game position (TT 36+).
**Proposed fix:** Cap TT gain from any single practitioner's operations in a single scene at TT +4. TT gains from multiple independent operations in the same scene beyond +4 carry to the next scene but do not fire thresholds mid-scene. This prevents one-scene TT collapse while preserving cumulative risk.
**Source:** Batch 07 T-B7-05

---

### PP-003
**Finding:** F-B7-06 / F80
**Severity:** P1
**Mechanic:** M-036 (Parliamentary Vote), M-037 (Grand Debate)
**Issue:** Grand Debate output (Composure shifts, CP awards) has no mechanical path to Parliamentary Vote resolution. Coalition mechanics absent.
**Proposed fix:** Add coalition formation step between Grand Debate and Vote:
1. Grand Debate outcome shifts faction Composure (existing).
2. Coalition formation: each faction with Composure ≥ 3 may join a coalition. Coalition leader makes Influence roll (Ob = number of opposing factions), adds 1D per allied faction.
3. Vote: coalition pool vs opposition pool. Net successes determine motion result.
Parliament Integrity (PI) modifies Ob: PI ≥ 7 = Ob +1 (stable institutions resist easy majorities).
**Source:** Batch 07 T-B7-02, T-B7-11

---

### PP-004
**Finding:** F-B7-12 / F-B7-22
**Severity:** P1
**Mechanic:** M-034 (Faction Stats)
**Issue:** No faction stat thresholds defined. Stats can reach 0 or negative with no consequence. Revolution Wealth −1 reachable in normal play.
**Proposed fix:**
- Stat floor: 0 (stats cannot go negative; excess loss is absorbed).
- Stat ceiling: 10 (stats cannot exceed 10; excess gain is absorbed).
- Threshold consequences (apply to all factions):
  - Any stat at 0: that stat's Domain Actions unavailable until stat recovers to 1+.
  - Stability 0: faction enters Crisis — cannot take Domain Actions of any type; loses 1 stat per season (starting with lowest) until Stability recovers or faction is eliminated.
  - Mandate 0: faction loses institutional legitimacy — IP +5, other factions may claim their territories without Domain Action cost.
  - Wealth 0: faction cannot fund Domain Actions costing Resources; basic ops continue at −1D.
  - Military 0: faction cannot conduct military Domain Actions; territory vulnerable to seizure.
  - Intel 0: faction has no covert capability; all their Domain Actions are publicly visible to all other factions.
**Source:** Batch 07 T-B7-04, T-B7-07

---

### PP-005
**Finding:** F-B7-23
**Severity:** P1
**Mechanic:** M-035 (Domain Actions)
**Issue:** Simultaneous conflicting Domain Actions have no sequencing or resolution rule.
**Proposed fix:** Domain Action resolution order within a season:
1. Defensive actions (fortify, stabilise, protect) resolve first.
2. Economic actions (trade, build, resource) resolve second.
3. Intelligence actions (spy, investigate, expose) resolve third.
4. Military actions (attack, seize, threaten) resolve fourth.
5. Political actions (debate, vote, negotiate) resolve last.
Direct conflicts within the same tier: resolve simultaneously; both effects apply unless one explicitly cancels the other (stated in action text). Where cancellation is mutual: the higher-pool roller's effect stands; the lower's is negated.
**Source:** Batch 07 T-B7-07

---

### PP-006
**Finding:** F-B7-29 / F100
**Severity:** P1
**Mechanic:** M-045 (Mass Combat)
**Issue:** Mass combat damage formula absent. All outcomes GM-determined.
**Proposed fix (design draft — [EDITORIAL] required):**
Pool: Military stat + commander Coord ÷ 2 (rounded down), TN7, Ob = enemy Military ÷ 2 (rounded up).
Damage: net successes above Ob = casualty rating (1–5 scale):
- Net 0 (Partial): 1 casualty step (unit loses 20% strength, morale −1)
- Net 1–2 (Success): 2 casualty steps (unit loses 40%, morale −2)
- Net 3+ (Overwhelming): 3 casualty steps (unit loses 60%, morale −3, rout check required)
Rout check: Morale roll (3D, TN7, Ob 2). Failure = unit routes, removes from field.
Battle ends when: one side has 0 units, or all units have routed, or commander concedes.
**Source:** Batch 07 T-B7-09; existing F100

---

### PP-007
**Finding:** F-B7-40
**Severity:** P1
**Mechanic:** M-007 (Conditions) — Composure
**Issue:** "Composure" used as both a degrading track (resource 0–10) and a dice pool source (attribute). Mechanically ambiguous in all Condition resolution rolls.
**Proposed fix:** Rename to resolve dual-use:
- **Composure track** (resource) → rename to **Poise** (0–10). Degrades under social/mental stress. At Poise 0: character is overwhelmed (social incapacitation equivalent).
- **Composure** (attribute/stat) → retained as the dice pool source for social and mental rolls.
This separates the resource from the attribute. All existing rules referencing "Composure" require audit: those referencing the degrading track → replace with Poise; those referencing roll source → retain as Composure.
[EDITORIAL: naming "Poise" requires approval]
**Source:** Batch 07 T-B7-13

---

### PP-008
**Finding:** F-B7-44 / F84
**Severity:** P1
**Mechanic:** M-056 (Niflhel Destabilisation) — Faction Stats
**Issue:** Niflhel Intel stat undefined. Faction cannot be run mechanically.
**Proposed fix:** Define Niflhel starting stats:
M(Mandate) 2, I(Influence) 3, W(Wealth) 5, Mi(Military) 1, In(Intelligence) 8, S(Stability) 6
Rationale: Niflhel is a covert faction — low public power (Mandate, Influence, Military), high covert capability (Intelligence), economically self-sufficient (Wealth), internally stable (Stability). Intel 8 distinguishes them from all other factions.
[EDITORIAL: starting stat values require approval]
**Source:** Batch 07 T-B7-15; existing F84

---

### PP-009
**Finding:** F-B6-RE-01 (Batch 6)
**Severity:** P1
**Mechanic:** Grand Debate — Reading Exchange
**Issue:** Reading Exchange has no stated Ob.
**Proposed fix:** Add to §9.4: "Reading Exchange uses Ob 1. Degrees: net ≥ 2 = Overwhelming (full style read + disposition reveal); net = 1 = Success (style identified); net = 0 = Partial (vague impression only); net ≤ −1 = Failure (opponent notices scrutiny)."
**Source:** Batch 06

---

### PP-010
**Finding:** F-27 (Batch 4)
**Severity:** P1
**Mechanic:** ThS Crisis + Certainty Rendering Crisis simultaneous
**Issue:** Two crises with contradictory resolution conditions (ThS = sustained engagement; Certainty = withdrawal). No rule for simultaneous fires.
**Proposed fix:** Combined Crisis procedure:
1. Address Certainty Rendering Crisis first (Belief revision — single scene declaration; does not require withdrawal from play).
2. ThS Crisis resolution then proceeds independently (multi-season sustained engagement requirement).
The Certainty resolution does not clear or modify the ThS requirement. Both must resolve on their own terms.
**Source:** Batch 04

---

### PP-011
**Finding:** F-25 (Batch 4)
**Severity:** P1
**Mechanic:** ThS Track
**Issue:** Active practitioners hit ThS Crisis by Season 3 at 2 ops/session. Recovery rate insufficient to sustain play.
**Proposed fix:** Add extended rest option: a full season with zero Thread operations recovers ThS +5 (instead of standard +2). This allows practitioners to cycle rest seasons and sustain practice across a full campaign arc. Standard per-session rest (+2) retained for short rests.
**Source:** Batch 04

---

### PP-012
**Finding:** F-26 (Batch 4)
**Severity:** P1
**Mechanic:** Intelligibility track / Coherence track (§4.5 vs §5.10)
**Issue:** Two tracks with same range (10→0) and conflicting rules — §5.10 grants Thread op bonuses at low Intelligibility; §4.5 does not. Dual-track naming problem.
**Proposed fix:** Resolve as two distinct tracks:
- **Intelligibility track** (§4.5): passive degradation from over-use. Social penalties at low values. No Thread bonuses. This is the "burning out" path.
- **Coherence transformation track** (§5.10): active monstrous development path, chosen or forced. Grants Thread op bonuses at low values. This is the "going native" path.
Triggers are distinct: Intelligibility degrades from ThS accumulation; Coherence transformation advances from direct Monstrous Entity contact or deliberate Thread immersion.
A practitioner can be on both tracks simultaneously — the paths are not mutually exclusive.
[EDITORIAL: confirm this interpretation against Philosophical Foundations P-03, P-04]
**Source:** Batch 04

---

### PP-013
**Finding:** F-23 (Batch 4)
**Severity:** P1
**Mechanic:** Collective Thread Operations — scaling
**Issue:** No scaling formula for participant count. "Correspondingly significant" is not a mechanic.
**Proposed fix:** Define scaling explicitly:
- d10 co-movement: roll once per collective operation (not per practitioner).
- Automatic effects (temporal/epistemic): fire once per participant beyond the Anchor. 4-practitioner lattice = 3 additional auto-effects, each rolling independently from the co-movement table.
- TT cost: standard TT cost applies once (not multiplied). Additional co-movement effects carry TT cost only if they independently generate TT (per normal rules for each effect type).
**Source:** Batch 04

---

### PP-014
**Finding:** F-24 (Batch 4)
**Severity:** P1
**Mechanic:** Collective Thread Operations — Anchor dropout
**Issue:** No rule for what happens when Anchor drops contact mid-lattice.
**Proposed fix:** Anchor dropout = immediate operation failure (Failure degree). No Helper promotion to Anchor mid-operation. Each Helper's contact window expires naturally per their own TD rules. TT penalty: standard failure costs apply (no additional penalty for the dropout itself beyond the failure).
**Source:** Batch 04

---

### PP-015
**Finding:** F-34 (Batch 4)
**Severity:** P1
**Mechanic:** TC 80 threshold — territorial seizure procedure
**Issue:** Procedure referenced in §7.2 and §8.3 but not written.
**Proposed fix (design draft — [EDITORIAL] required):**
- At TC 80+: Church may declare seizure on one territory per season.
- Roll: Church Mandate vs Ob = target faction's (Mandate + Stability) ÷ 4 (round up).
- Counter-play: controlling faction may resist via Domain Action (same-tier political action per PP-005 sequencing).
- Uncontested success: territory gains Church institutional authority (Church Influence +1, controlling faction Influence −1). Not military occupation.
- Cannot seize: territories with active military defence (Military stat ≥ 4), Hafenmark (Baralta's Ob +3 constitutional claim), Schoenland.
**Source:** Batch 04

---

### PP-016
**Finding:** F-38 (Batch 4)
**Severity:** P1
**Mechanic:** Character archetypes — Knight Templar, Restoration Seeker, Niflhel Operative
**Issue:** Three archetypes have no personal-scale mechanics defined.
**Proposed fix (design draft — [EDITORIAL] required for stat values):**
Knight Templar: Coord 4, End 4, Spirit 4. Unique tag: Devout Constraint active; +2D in combat when defending Church territory or personnel; CE accumulation rate ×1.5.
Restoration Seeker: Coord 2, End 3, Spirit 5. Unique tag: may perform Community Weaving without TS (at Ob +2); Histories always include one Restoration community bond.
Niflhel Operative: Coord 4, End 3, Spirit 3. Unique tag: starts with DD 0 and Deniability Debt mechanic active; +2D on Intelligence Domain Action contributions; identity is unknown to all factions at campaign start.
**Source:** Batch 04

---

### PP-017
**Finding:** F-40 (Batch 4)
**Severity:** P1
**Mechanic:** CE track — accumulation procedure
**Issue:** CE accumulation procedure incomplete past CE 3. No rule for CE 4–5.
**Proposed fix:** Complete CE track:
- CE 1: First session of Thread residue handling or witnessing Thread operation.
- CE 2: Repeated exposure (one increment per 2 sessions of regular contact with Thread-active environment).
- CE 3: Significant exposure (direct Thread work performed on this character, or 3+ sessions residue handling). TS growth check fires.
- CE 4: Intensive exposure (5+ sessions residue handling, or direct Thread work on character by practitioner TS 30+). Second TS growth check; Perception shift begins (character notices inexplicable things).
- CE 5: Transformation threshold. Spirit check TN7 Ob 2. Failure: permanent perceptual shift — character gains TS 5 involuntarily and cannot suppress Thread perception. Success: character resists transformation but CE resets to 3 (exposure has permanent partial effect).
**Source:** Batch 04

---

### PP-018
**Finding:** F-13 (Batch 3)
**Severity:** P1
**Mechanic:** TC pause + Baralta suppressor interaction
**Issue:** No rule governing TC when both TC pause (Stability ≤ 4) and Baralta suppressor (−1/season) are simultaneously active.
**Proposed fix:** Clarify: TC pause sets the season's TC change to 0 before modifiers. Negative modifiers (Baralta suppressor, Grand Debate victory, Niflhel destabilisation) still apply after the pause: TC can go negative in a pause season. This creates a beneficial player interaction where simultaneous Church Stability suppression + Baralta active = TC reduction even in pause seasons.
**Source:** Batch 03

---

### PP-019
**Finding:** F-14 (Batch 3)
**Severity:** P1
**Mechanic:** Niflhel network intelligence output
**Issue:** "One piece of information" undefined — no standard for what networks hold or what format reveals take.
**Proposed fix:** Standardise intelligence output as one of: (a) one currently secret faction stat value, (b) one NPC's active Belief, (c) one pending Domain Action intent (faction X intends to take action Y this season). GM selects most narratively relevant. In BG mode: GM draws from a pre-prepared intelligence card deck.
**Source:** Batch 03

---

### PP-020
**Finding:** F-07 (Batch 3)
**Severity:** P1 (escalated from P2 — structural trap)
**Mechanic:** Knot strain recovery vs Intelligibility decay
**Issue:** Recovery cannot outpace accumulation at Int ≤ 4. Knot is trapped in perpetual deterioration.
**Proposed fix:** When Int rises (rest season recovery: +1 Int), add cross-reference note: Int recovery above 4 reduces Knot strain accumulation rate from +1/2 sessions to +1/3 sessions. This linkage is already implicit in the track interactions but must be explicitly stated. Additionally: Int recovery of 5→6 should provide one free Knot strain reduction (−1 strain on practitioner's most stressed Knot).
**Source:** Batch 03

---

### PP-021
**Finding:** F-B5-M07-A (Batch 5)
**Severity:** P1
**Mechanic:** Group combat bonus — dual table conflict
**Issue:** §1.9 (Fibonacci Group Bonus) and §8.1 (Group Attacks) produce different outcomes at 3+ attackers. §1.9 gives 2× more bonus than §8.1.
**Proposed fix:** Remove §8.1 Group Attacks table. Replace with: "See §1.9 for group bonus calculation." §1.9 is canonical.
**Source:** Batch 05

---

### PP-022
**Finding:** F-B5-M06-D (Batch 5)
**Severity:** P1
**Mechanic:** Priority 3 sub-rule B × pool split
**Issue:** Priority attack for longer weapon vs closing shorter weapon: no rule for pool declaration timing when the priority attack was not anticipated at declaration phase.
**Proposed fix:** Add rule: "If a longer-weapon fighter's priority attack right was not anticipated at declaration (opponent closed unexpectedly), the longer-weapon fighter may re-declare their Offence pool allocation for that round only, before the priority attack resolves. This re-declaration applies only to the priority attack itself."
**Source:** Batch 05

---

## P2 PATCHES

---

### PP-023
**Finding:** F-B7-01
**Severity:** P2
**Mechanic:** M-002 (Wounds) — TN cliff
**Issue:** 1→2 Wounds drops attack success rate from ~70% to ~30% (6D pool). Steep cliff creates death spiral entry.
**Proposed fix:** Add a wound recovery option within combat: a character can spend their action to apply a field dressing (requires Materials resource or ally assistance) to reduce one Wound's TN penalty temporarily (TN reverts after scene ends). This does not remove the Wound — it provides a temporary stabilisation option that interrupts the spiral.
**Source:** Batch 07 T-B7-01

---

### PP-024
**Finding:** F-B7-04
**Severity:** P2
**Mechanic:** M-006 (Inspirations) — spend timing
**Issue:** Inspiration spend timing unspecified. Pre-roll vs retroactive is a ~15% probability difference.
**Proposed fix:** Add to Inspiration rules: "Inspiration must be declared before the dice are rolled. It may not be spent retroactively after seeing the result."
**Source:** Batch 07 T-B7-02

---

### PP-025
**Finding:** F-B7-05
**Severity:** P2
**Mechanic:** M-003 (Histories) — double-dipping
**Issue:** No cap on applicable Histories per roll. 4 applicable Histories = +8D, trivialising specialist rolls.
**Proposed fix:** Cap: maximum 2 Histories may contribute dice to any single roll, regardless of how many are narratively applicable. Player chooses which 2. Third and subsequent applicable Histories provide a narrative framing benefit only (describe why the History is relevant) without adding dice.
**Source:** Batch 07 T-B7-02

---

### PP-026
**Finding:** F-B7-09
**Severity:** P2
**Mechanic:** M-016 (Pulling) — Partial Pull side effects
**Issue:** GM has unlimited latitude on Partial Pull consequence. Inconsistent across tables.
**Proposed fix:** Add bounded Partial Pull side effect table (d6 or GM selection):
1. Unintended connection strengthened (a different Thread connection at the location is reinforced instead)
2. Temporal bleed (a nearby non-practitioner experiences a brief memory intrusion from the target period)
3. Knot formation (the Partial Pull creates a Knot rating 1 at the location)
4. Practitioner's own memory distorted (−1 to Certainty)
5. Operation partially reversed (half the intended effect applies)
6. Escalation (the Partial Pull draws attention from Thread-sensitive entities at the location)
**Source:** Batch 07 T-B7-03

---

### PP-027
**Finding:** F-B7-10
**Severity:** P2
**Mechanic:** M-010 (Knots) — escalation loop
**Issue:** Failed Thread ops → Knots → higher Ob → more failures → more Knots. Potential impassable obstacle.
**Proposed fix:** Add Knot rating cap: maximum Knot rating at any single location = 5. Ob modifier caps at +5 regardless of number of stacked Knots. This prevents absolute inaccessibility while preserving escalating difficulty.
**Source:** Batch 07 T-B7-03

---

### PP-028
**Finding:** F-B7-13
**Severity:** P2
**Mechanic:** M-035 (Domain Actions) — character contribution
**Issue:** Individual character skills (Histories, TS, Beliefs) have no pathway to Domain Action pools.
**Proposed fix:** Add character contribution rule: a PC may contribute to a faction's Domain Action if they are personally involved in the action (present in scene or specifically tasked). Contribution: the PC makes a relevant skill roll (Ob 2). Success: +1D to the faction's Domain Action pool. Overwhelming: +2D. Failure: no contribution. This creates a pathway without making character skill mandatory — faction stat still drives the pool.
**Source:** Batch 07 T-B7-04

---

### PP-029
**Finding:** F-B7-14
**Severity:** P2
**Mechanic:** M-011 (Circles) — obligation resolution
**Issue:** Partial Circles results create obligations with no discharge mechanic.
**Proposed fix:** Add obligation resolution procedure: Obligations created by Partial Circles results are logged with a debt rating (1–3). Each season, the creditor faction or NPC may call the obligation (GM trigger). If not called after 3 seasons, the obligation expires (the favour was forgotten or the situation changed). If called: PC must fulfill or suffer Circles −1 with that network.
**Source:** Batch 07 T-B7-04

---

### PP-030
**Finding:** F-B7-19
**Severity:** P2
**Mechanic:** M-017 (FR-Lock) — failure penalty
**Issue:** FR-Lock failure penalty (TT +3) exceeds non-attempt (TT +2). Perverse incentive to not attempt containment.
**Proposed fix:** Equalise: FR-Lock failure = TT +2 (same as non-attempt). FR-Lock success = TT −1 (containment actively reduces tension). This removes the perverse incentive while rewarding successful containment.
**Source:** Batch 07 T-B7-05

---

### PP-031
**Finding:** F-B7-24
**Severity:** P2
**Mechanic:** M-031 (Theocracy Clock) — Synod duration
**Issue:** Synod trigger defined but no exit condition.
**Proposed fix:** Synod duration: active until TC drops below 50 (through any combination of Grand Debate victories, Niflhel destabilisation, Church Stability suppression, or Baralta suppressor). While Synod is active: Church Mandate +2 (existing), all TC-reducing actions have Ob +1 (Church is actively defending its authority). Synod cannot last more than 5 seasons regardless of TC (institutional fatigue); after 5 seasons, Mandate bonus expires and TC continues from current value.
**Source:** Batch 07 T-B7-07

---

### PP-032
**Finding:** F-B7-25
**Severity:** P2
**Mechanic:** M-034 (Faction Stats) — Church structural poverty
**Issue:** Church Wealth hits 0 after 1 seasonal cycle at standard stat values.
**Proposed fix:** Add tithe income to Church seasonal accounting: Church receives Wealth +2 per season from tithe base (represents baseline institutional income independent of Domain Actions). This reflects Church's historical advantage as a landowning institution. Starting Wealth 5 + tithe 2 − upkeep 5 = Wealth 2 net (sustainable). [EDITORIAL: tithe mechanic requires approval as new faction-specific rule]
**Source:** Batch 07 T-B7-07

---

### PP-033
**Finding:** F-B7-26
**Severity:** P2
**Mechanic:** M-039 (Combat—Initiative) — tie resolution
**Issue:** No mechanic for tied initiative.
**Proposed fix:** Initiative ties resolve by: (1) highest End stat acts first; (2) if still tied, simultaneous resolution (both actions fire, damage applies to both before either checks incapacitation).
**Source:** Batch 07 T-B7-08

---

### PP-034
**Finding:** F-B7-30
**Severity:** P2
**Mechanic:** M-045 (Mass Combat) — unit attrition
**Issue:** All-or-nothing resolution; no morale failure cascade or retreat mechanic.
**Proposed fix:** Integrated with PP-006 (mass combat damage formula). Add morale track (0–10) per unit. Morale depletes per casualty step. At Morale 3: unit may attempt ordered withdrawal (commander roll, Ob 2; failure = rout). At Morale 0: automatic rout. Routing units may rally if commander succeeds Mandate roll (Ob 3) before end of battle.
**Source:** Batch 07 T-B7-09

---

### PP-035
**Finding:** F-B7-31
**Severity:** P2
**Mechanic:** M-040 (Priority Table) — mass combat adaptation
**Issue:** Individual Priority Table not adapted for unit-level combat.
**Proposed fix:** Add unit-type priority table for mass combat:
Priority 1: Cavalry charge (first engagement only)
Priority 2: Ranged units (archers, artillery)
Priority 3: Infantry formations
Priority 4: Irregular/skirmish units
Priority 5: Siege equipment
Commanders resolve actions in this order within each mass combat round.
**Source:** Batch 07 T-B7-09

---

### PP-036
**Finding:** F-B7-32
**Severity:** P2
**Mechanic:** M-046 (Thread Ops in Combat) — timing
**Issue:** Thread operation timing relative to physical combat actions undefined.
**Proposed fix:** Thread operations in combat use Priority 5 for initiation. Effects manifest at Priority 1 of the following round (existing rule confirmed — 2-round delay). Exception: Diagnosis manifests same round (observation, not operation). FR-Lock manifests immediately on success (emergency containment).
**Source:** Batch 07 T-B7-10

---

### PP-037
**Finding:** F-B7-33
**Severity:** P2
**Mechanic:** M-046 (Thread Ops in Combat), M-048 (Scale Transitions) — TTRPG→BG handoff
**Issue:** Individual combat state (Wounds, Conditions, active Thread ops) has no handoff procedure to mass combat.
**Proposed fix:** When TTRPG scene escalates to BG mass combat:
- Character Wounds carry over and apply to that character's contribution to the mass combat commander pool (each Wound = −1D from commander contribution).
- Active Conditions: Rattled = commander pool −1D; Unmask = faction loses 1 Intel temporarily.
- Active Thread operations: persist for their declared duration (Contact rounds remaining); they do not extend beyond their original window.
**Source:** Batch 07 T-B7-10

---

### PP-038
**Finding:** F-B7-34
**Severity:** P2
**Mechanic:** M-011 (Circles), M-037 (Grand Debate) — undocumented interaction
**Issue:** Circles-based narrative reframe can bypass formal debate mechanics. Undocumented but powerful.
**Proposed fix:** Document explicitly in both M-011 and M-037 rules: "A character with Circles ≥ 3 in a relevant network may attempt a Narrative Reframe as an alternative to a standard Debate argument. Roll: Circles rating + Coord, TN7, Ob 3. Success: the Debate frame shifts — opponent must argue from a less favorable position (Ob +1 on their next exchange). Failure: the reframe attempt is visible and clumsy — character loses 1 Debate exchange."
**Source:** Batch 07 T-B7-11

---

### PP-039
**Finding:** F-B7-37
**Severity:** P2
**Mechanic:** M-048 (Scale Transitions) — translation ratio
**Issue:** No formula for personal-scale Thread effects → faction stat change.
**Proposed fix:** Scale translation table:
- Personal Overwhelming Thread op: faction stat +1 (if narratively connected to faction domain).
- Territorial-scale Thread op (Dissolution or FR-Lock at Ob 8+): faction stat +2 or clock ±2.
- Personal-scale ops do not affect clocks directly; only territorial-scale ops move clocks.
One personal-scale Overwhelming = one Domain Action equivalent for the affected faction. Counts against their seasonal Domain Action limit.
**Source:** Batch 07 T-B7-12

---

### PP-040
**Finding:** F-B7-38
**Severity:** P2
**Mechanic:** M-048 (Scale Transitions), M-035 (Domain Actions) — economy
**Issue:** Thread-derived faction gains potentially additive to Domain Actions, doubling output.
**Proposed fix:** Thread-derived faction stat gains count as that faction's Domain Action for the season in the relevant domain. Example: Almud's Overwhelming Past Pull that strengthens Crown's legal claim = Crown's Political Domain Action for that season. Crown cannot also take a Political Domain Action that season. This caps the combined economy without eliminating the mechanic.
**Source:** Batch 07 T-B7-12

---

### PP-041
**Finding:** F-B7-41
**Severity:** P2
**Mechanic:** M-002 (Wounds) — permanent criteria
**Issue:** All Wounds heal on Full Rest; no rule for permanent Wounds. Combat has no lasting physical consequences.
**Proposed fix:** Permanent Wound criteria: a Wound becomes permanent when: (a) character reaches Wounds 4 (near-death threshold) without receiving immediate medical attention (within 1 scene); OR (b) the source of the Wound is specified as a permanent injury type (GM call: arrow through hand, lost eye). Permanent Wounds do not heal on Full Rest. Recovery requires: specialist medical treatment (Circles call, Ob 3) + full season of reduced activity.
**Source:** Batch 07 T-B7-13

---

### PP-042
**Finding:** F-B7-42
**Severity:** P2
**Mechanic:** M-054 (Einhir Sites) — detectability
**Issue:** Einhir sites at ThS 18 = Ob 1 passive detection for any TS ≥ 1 character. Near-automatic Inquisitor exposure.
**Proposed fix:** Add concealment option for Einhir sites: a practitioner with TS ≥ 20 may spend 1 hour performing a Dampening Weave (Ob 3) that reduces the site's effective ThS by 8 for the duration of operations (until the Weave disperses, ~3 hours). This allows preparation for Einhir site use without guaranteeing automatic exposure, while still requiring skilled preparation.
**Source:** Batch 07 T-B7-14

---

### PP-043
**Finding:** F-B7-45
**Severity:** P2
**Mechanic:** M-034 (Faction Stats) — Stability 0
**Issue:** Faction Stability 0 has no defined consequence.
**Proposed fix:** Integrated with PP-004: Stability 0 = faction Crisis (defined there). Additional: when Church Stability hits 0, TC gains are suspended (Church too internally divided to expand externally). This is the most severe form of TC suppression and should be explicitly noted as a player strategy.
**Source:** Batch 07 T-B7-15

---

### PP-044
**Finding:** F-B7-46
**Severity:** P2
**Mechanic:** M-050 (Riskbreakers), M-056 (Destabilisation) — passive faction detection
**Issue:** Factions have no mechanic for passively detecting ongoing covert operations.
**Proposed fix:** Add passive Intel threshold: each season, a faction with Intel ≥ 4 rolls 1D (TN7) passively. Success: faction becomes aware that a covert operation is occurring (not by whom). Intel ≥ 7: on success, faction learns the origin faction of the operation. This is not a full Domain Action — it is a background awareness check. Active Intel Domain Actions still provide more detailed information.
**Source:** Batch 07 T-B7-15

---

### PP-045
**Finding:** F-B5-M03-A (Batch 5)
**Severity:** P2
**Mechanic:** Stamina — "in a row" qualifier
**Issue:** "In a row" allows Stamina reset via single passive round, neutering the system.
**Proposed fix:** Remove "in a row." Stamina decreases by 1 for every round in which the character has Moved, Manoeuvred, or Attacked. Resets only on Catch Breath or Breather (explicit rest actions).
**Source:** Batch 05

---

### PP-046
**Finding:** F-B5-M04-C (Batch 5)
**Severity:** P2
**Mechanic:** Combat — projectile range closing
**Issue:** Closing against projectile weapon: "must dodge" with no stated Ob or procedure.
**Proposed fix:** Add closing procedure: "Closing vs. projectile: Agility check (standalone), Ob = ranged attacker's net successes that round (minimum Ob 1). Success: character closes to long range. Failure: no closure, character takes damage normally."
**Source:** Batch 05

---

### PP-047
**Finding:** F-B5-M07-C (Batch 5)
**Severity:** P2
**Mechanic:** Group combat bonus — "unsupported" all-or-nothing nullification
**Issue:** Single ally nullifies all group bonuses for any number of attackers.
**Proposed fix:** Change "unsupported" definition: "If the target has an ally engaging at least one attacker, reduce the group bonus by one step (e.g., 5 attackers = treat as 3 attackers for bonus calculation). Each additional ally engaging another attacker reduces by a further step."
**Source:** Batch 05

---

### PP-048
**Finding:** F-B5-D01 (Batch 5)
**Severity:** P2
**Mechanic:** Combat — fleeing/withdrawal
**Issue:** No defined procedure for escaping combat entirely.
**Proposed fix:** Add to §8.1: "Escaping combat: Agility roll, Ob = opponent's Cognition stat (their awareness of your intent). Success: character exits combat at full Stamina cost (Stamina → 0). Failure: opponent receives one free Priority 3 attack before character exits. Character cannot re-enter the same combat after escaping."
**Source:** Batch 05

---

### PP-049
**Finding:** F-B5-D03 (Batch 5)
**Severity:** P2
**Mechanic:** Combat — mutual Full Guard stalemate
**Issue:** Two combatants in mutual Full Guard can stall indefinitely.
**Proposed fix:** "A combatant who declares Full Guard for 2 or more consecutive rounds without any offensive action: Stamina −1 per full-guard round (tension fatigue). This prevents indefinite stalemate without penalising tactical use of 1–2 defensive rounds."
**Source:** Batch 05

---

### PP-050
**Finding:** F-10 (Batch 3)
**Severity:** P2
**Mechanic:** Vaynard Ambition Track — no decrease mechanic
**Issue:** Track is one-way ratchet. No diplomatic de-escalation path.
**Proposed fix:** Add one decrease trigger: "Successful Diplomacy Domain Action representing a major concession to Varfell by another faction (not merely defeating Vaynard militarily): Ambition −5. This creates a diplomatic cost-benefit calculation for PCs. Maximum one Diplomacy decrease per season."
**Source:** Batch 03

---

## P3 PATCHES (abbreviated — lower priority)

---

### PP-051 (P3) — Unmask/Circles interaction
Unmask condition should specify whether it reduces Circles rating with the exposed faction. Proposed: Unmask reduces Circles −1 with the faction whose member witnessed the exposure. (Batch 07 T-B7-01)

### PP-052 (P3) — Safe rest definition
"Safe location" for Full Rest: define as "a location where no combat check has been required in the previous hour and no active pursuit is ongoing." (Batch 07 T-B7-01)

### PP-053 (P3) — Certainty gate asymmetry
Add Certainty gate to Leap and Pull matching Diagnosis gate: at Certainty ≤ 2, all Thread operations have Ob +1 (not just Diagnosis). (Batch 07 T-B7-03)

### PP-054 (P3) — Late combat entrants
Add: "Combatants entering an ongoing combat roll initiative immediately on entry; they are inserted into the existing declaration order at their result." (Batch 05)

### PP-055 (P3) — Zone movement during Thread contact
Add note at §5.2: "Moving to an adjacent zone does not break Thread contact unless the target configuration is not present in the new zone." (Batch 05)

### PP-056 (P3) — TC cascade speed from Grand Debate
Document in GM reference: "Grand Debate + Thread event interrupt in the same scene can push TC from 48 to 51. Tables at TC 45+ should treat each Grand Debate as a potential Synod trigger." (Batch 07 T-B7-11)

### PP-057 (P3) — Knot/Residue catch-22
Add off-site Thread maintenance: a practitioner with TS ≥ 30 may perform a Remote Weave (Ob = Knot rating + 2) from an adjacent location, affecting the blocked location without requiring direct Thread-side access. (Batch 07 T-B7-06)

### PP-058 (P3) — Manoeuvres underuse
Document in GM guidance: "Manoeuvres (Disarm, Trip, etc.) are mechanically suboptimal vs direct attacks in most cases. They are intended for use when killing is not the goal. GMs should create scenarios where non-lethal objectives make Manoeuvres the only viable path." (Batch 07 T-B7-08)

### PP-059 (P3) — "Random territory" procedure (BG mode)
Add: "In BG mode, random territory selection: draw a territory number card or roll 1d(territory count)." (Batch 03)

### PP-060 (P3) — Niflhel destabilisation rate
Document in faction reference: "Niflhel's Destabilisation mechanic cannot outpace TC growth through normal Church Domain Actions. Niflhel's role is to slow TC accumulation, not reverse it. Meaningful TC reversal requires Grand Debate victories or Church Stability suppression by other factions." (Batch 07 T-B7-15)

---

## EDITORIAL DECISIONS REQUIRED
Items marked [EDITORIAL] above require user approval:
- PP-006: Mass combat damage formula stat values
- PP-007: "Poise" rename for Composure track
- PP-008: Niflhel starting stat values
- PP-012: Intelligibility vs Coherence as two distinct tracks (canon guard check against P-03, P-04 needed)
- PP-015: TC 80 territorial seizure procedure
- PP-016: Archetype stat values (Knight Templar, Restoration Seeker, Niflhel Operative)
- PP-032: Church tithe income as new faction-specific rule

---

## PATCH COUNT SUMMARY
| Severity | Count |
|----------|-------|
| P1 | 22 |
| P2 | 27 |
| P3 | 10 |
| **Total** | **59** |

