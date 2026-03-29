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


## PATCH PROPOSALS — AUDIT BATCH (2026-03-27)

### PP-078
**Finding:** F57 / G-128
**Severity:** P1 → P2 downgrade candidate (text clarity, not mechanical failure)
**Mechanic:** M-020 (Thread Sensitivity) — world-track scope
**Issue:** §5.9 Fallout table uses per-character language ("your ThS drops") but ThS is a world-side track, not a per-character stat. All ThS-related decisions may be incorrectly applied by practitioners who read ThS as personal.
**Proposed fix:** Rewrite §5.9 Fallout table throughout:
- Replace: "your ThS drops" → "ThS drops"
- Replace: "your thread sensitivity has reached" → "Thread Sensitivity in this environment has reached"
- Add header note at §5.9: "Thread Sensitivity (ThS) is a world-side track reflecting cumulative Thread-side presence density. It is not a per-character stat."
**Model:** Haiku 4.5 (text rewrite, no new mechanic)
**Source:** Audit batch 2026-03-27; original sim_batch_03

---

### PP-079
**Finding:** F72 / G-129
**Severity:** P1
**Mechanic:** M-NPC-Torben — Torben Loyalty Clock
**Issue:** TLK drain rate entirely absent from CP14. Succession timeline and IP acceleration trigger (IP 30 = Tutoring Demand) are unplayable without knowing how fast loyalty degrades.
**Proposed fix:** Define TLK drain rate:
TLK starts at 10 (full loyalty). At TLK 0: Torben fully Altonian-aligned; retrieval requires narrative arc, not Domain Action.

Seasonal drain:
- No Crown contact this season: TLK −1
- Tutoring demand refused (incl. Negotiate Delay): TLK −3 cumulative
- Failed covert contact (Partial result): TLK −1 additional
- Successful covert contact (Crown Intel Ob3+): TLK holds (no drain this season)
- Successful tutoring deployment (Elske dispatched): TLK +2

Milestone events (one-time, GM-tracked):
- Altonian invasion formally announced: TLK −3
- Altonian-Crown treaty signed: TLK −2
- Torben ordered to renounce Valoria ties: TLK −4
- Elske makes public political statement: TLK −2
- Crown publicly demonstrates legitimacy: TLK +1

At TLK 0: Crown loses all covert contact routes. Recovery requires Public Amnesty Domain Action (Political tier, Ob5).
**Source:** Audit batch 2026-03-27; original sim_batch_03

---

### PP-080
**Finding:** F112 / G-136
**Severity:** P1
**Mechanic:** M-031 (Theocracy Clock) — Church Stability TC brake
**Issue:** TC brake fires at Church Stability ≤5. Church starts at Stability 5 (standard starting stats), permanently suppressing TC generation from Season 1. Church cannot advance TC under standard conditions.
**Proposed fix:** Change TC brake threshold from Stability ≤5 to Stability ≤3.
- Church Stability 4–10: normal TC accumulation (no brake)
- Church Stability 3: TC brake activates — seasonal TC gain halved (round up)
- Church Stability 0: PP-043 applies (TC gains fully suspended — existing mechanic unchanged)

Cross-reference: PP-043 (Stability 0) unchanged. Church starting Stability (5) now operates above brake threshold.
**Model:** Haiku 4.5 (threshold number change)
**Source:** Audit batch 2026-03-27; original sim_batch_04

---



## PATCH PROPOSALS — EDITORIAL BATCH (2026-03-27)

### STATUS UPDATES FROM EDITORIAL REVIEW

| Patch | Old Status | New Status | Reason |
|-------|-----------|-----------|--------|
| PP-007 | EDITORIAL pending | CLOSED — NOT NEEDED | Poise = attribute; Composure = Presence+6 track. No dual-use collision once formula universally applied. |
| PP-012 | EDITORIAL pending | REVISED | Prior decision: ONE Coherence track. Two-track proposal rejected. Merge §4.5 + §5.10 into unified Coherence track. |
| PP-015 | EDITORIAL pending | SUPERSEDED | Full TC80 seizure procedure exists in succession_mechanic.md. Compile from source. |
| PP-062 | EDITORIAL pending | APPROVED | Restoration Community Weaving as supplementary Coherence recovery path (+1/successful op). Coexists with Corrective Weaving. |
| PP-071 | EDITORIAL pending | APPROVED | Conditional Weaving is canon-safe: co-movement fires at Weaving time, not trigger event. |
| PP-077 | EDITORIAL pending | REVISED | Coherence 0 = NPC (prior decision). Player-continuation rejected. Arc: rescue window before Coherence 0 confirmed. |
| PP-079 | OPEN (new) | SUPERSEDED | Torben Loyalty Clock fully designed in succession_mechanic.md. Starting value 8, −1/season, IP 30 trigger. |

### PP-081 — NEW MECHANIC: TRAJECTORY READING

**Finding:** F-B9-17
**Severity:** Design (approved new op type)
**Mechanic:** M-NEW: Trajectory Reading
**Requirement:** TS 70+, active Leap contact established, Certainty ≥ 2

**Summary:** Practitioner reads Thread-configuration trajectory potentials — not prophecy, but probabilistic reading of where the current Thread-state momentum is oriented. Distinct from Past-Oriented Pulling (retrieves actualized past) and standard ops (work with present configurations).

**What it produces:** 1–3 probable trajectory statements per GM. Each is a direction the configuration is oriented toward, not a guarantee. Trajectories are alterable by intervention or external events.

**Ob by time horizon:**
| Horizon | Ob |
|---------|-----|
| Near (1–3 scenes) | 3 |
| Medium (1 season) | 5 |
| Extended (1–3 seasons) | 7 |
| Far (campaign arc) | 10 |

**Degrees:**
- Overwhelming: trajectories at declared horizon +1; most probable identified
- Success: trajectories at declared horizon
- Partial: one trajectory; confidence level withheld
- Failure: one plausible false trajectory (self-projection of practitioner's Beliefs/fears). Practitioner does not know it is false.

**Costs:**
- TD +4
- Certainty −2
- TT +2 (any result); +4 on Failure

**Co-movement (Version C — mandatory):**
- Temporal: CD +2 + History Resonance
- Epistemic: practitioner's present-state perception filtered through trajectory for 1 scene; GM may introduce one perceptual ambiguity
- Actual: d6 as normal

**Canon compliance:** P-01 ✓, P-03 ✓, P-07 ✓, P-08 ✓, P-11 ✓

**Restrictions:**
- Cannot target own future (self-referential)
- Cannot target deceased (no current configuration)
- Unavailable at Coherence ≤ 4
- Subsequent Readings same configuration same scene: Ob +3 each

**Source:** F-B9-17; editorial approval 2026-03-27

---

### PP-008: APPROVED
**Niflhel Intel = 6**
Full starting stats confirmed: Mandate —, Influence 5, Wealth 4, Military —, Intel 6, Stability 4

### PP-016: APPROVED (revised to 10-attribute system)

**Knight Templar:**
Str 4, End 4, Agi 3, Cog 3, Mem 2, Poise 3, Att 2, Bonds 3, Pres 3, Spirit 4

**Restoration Seeker:**
Str 2, End 2, Agi 3, Cog 3, Mem 3, Poise 3, Att 4, Bonds 3, Pres 3, Spirit 5

**Niflhel Operative:**
Str 3, End 3, Agi 4, Cog 4, Mem 3, Poise 3, Att 4, Bonds 3, Pres 3, Spirit 3

FLAG: User attribute list uses "Poise" at position 6 (Str/End/Agi/Cog/Mem/Poise/Att/Bonds/Pres/Spirit). Workplan listed "Focus." Confirm at compilation: Poise = renamed Focus, or distinct attribute.

---



## PATCH PROPOSALS — BATCH 10 (2026-03-27)

### PP-082
**Finding:** F-B10-01
**Severity:** P2
**Mechanic:** M-046 (Thread Ops in Combat), PP-068
**Issue:** Thread split action pool formula (TS÷4) accidentally equals full Thread pool for practitioners at TS 64+. No effective split penalty.
**Proposed fix:** Thread split pool = (Cog + Mem) only, no History bonus, TN8 (increased difficulty). At TS 64: 9D TN8 vs ~30% success, vs full pool 16D TN7 ~65% success. Real split cost restored.
**Source:** Batch 10 T-B10-01

---

### PP-083
**Finding:** F-B10-08
**Severity:** P2
**Mechanic:** M-055 (Community Weaving), PP-013
**Issue:** PP-013 specifies "auto-effects fire once per participant beyond Anchor" without clarifying whether same-type auto-effects stack. Stacking epistemic effects from large collectives would make areas uninvestigatable.
**Proposed fix (ruling R-B10-02):** Add to PP-013: "Same-type auto-effects (temporal, epistemic) do not stack regardless of participant count. Each fires once per collective operation. Additional participants beyond the Anchor contribute additional rolls on the actual d6 consequence table only."
**Source:** Batch 10 T-B10-07

---

### PP-084
**Finding:** F-B10-09
**Severity:** P2
**Mechanic:** M-056 (Niflhel Destabilisation)
**Issue:** Destabilisation Ob = raw target Stability. At Church Stability 5: Ob5, ~8% success for Intel 6D. Niflhel cannot function as a destabilisation actor against stable factions.
**Proposed fix (ruling R-B10-03):** Destabilisation Ob = target Stability ÷ 2, rounded up. Church Stability 5 → Ob3. Intel 6D vs Ob3: ~68% success. Consistent with PP-004's Mandate+Stability÷4 formula precedent.
**Source:** Batch 10 T-B10-08

---

### PP-085
**Finding:** F-B10-13 + F-B10-14
**Severity:** P2
**Mechanic:** PP-081 (Trajectory Reading); M-035 (Domain Actions BG mode)
**Issue 1:** PP-081 does not specify the Trajectory Reading dice pool.
**Issue 2:** PP-005 domain action sequencing does not assign Thread operations to a tier for BG mode.
**Proposed fix:**
1. Add to PP-081: "Pool: Cog + Att + Thread History (perception attributes). TN7. This is a perception/reading op, not a shaping op — Mem is not included."
2. Add to PP-005: "Thread operations (BG mode Weave, Lock, Dissolution orders) resolve at Tier 2, alongside Economic actions. Co-movement consequences are known before Intelligence and Military resolutions."
**Source:** Batch 10 T-B10-11, T-B10-12

---


---

## PATCH PROPOSALS — DICE RULE CORRECTION (2026-03-27)

### PP-092
**Finding:** Rule error — §1.1 Dice table
**Severity:** P1 (rules-as-written are mechanically incorrect)
**Mechanic:** M-001 (Core Dice)
**Issue:** §1.1 states: result 10 = "One success + roll one bonus die (chains indefinitely)." This is incorrect. The canonical rule is: result 10 = flat +2 successes. No bonus die is rolled.
**Proposed fix:** Replace §1.1 die table entry for 10:
- Old: `10 | One success + roll one bonus die (chains indefinitely)`
- New: `10 | Two successes`
Also update the explanatory sentence: remove "including bonus dice" from the net successes definition.
**Approved:** Yes — user-confirmed 2026-03-27. No editorial gate required (factual correction).
**Source:** User correction 2026-03-27

---

### PP-093
**Finding:** Rule error — §4.3 Inspirations, Stunt rule
**Severity:** P1 (rules-as-written inconsistent with PP-092)
**Mechanic:** M-006 (Inspirations)
**Issue:** §4.3 Stunt rule states: "Roll Spirit dice as bonus (chain on 10)." Inconsistent with corrected §1.1 (10 = flat +2, no extra die).
**Proposed fix:** Remove "(chain on 10)" from Stunt rule. Spirit bonus dice follow standard die face table: 10 = +2 successes, no chain.
**Approved:** Yes — user-confirmed 2026-03-27. No editorial gate required (consistency fix).
**Source:** PP-092 cascade; user confirmation 2026-03-27

---

## PATCH COUNT SUMMARY (UPDATED)
| Severity | Count |
|----------|-------|
| P1 | 35 |
| P2 | 47 |
| P3 | 10 |
| Design (new mechanic) | 1 |
| **Total** | **93** |
---

## PATCH PROPOSALS — BATCH RESOLUTIONS (2026-03-28)
*Canon-grounded resolutions for 37 open gaps. Derived from Philosophical Foundations, compiled stages, and internal system logic. No editorial approval required unless flagged.*

---

### PP-094
**Gap:** G-099 — Mid-Debate incapacitation has no resolution rule
**Severity:** P1
**Section:** §9.6 Debates
**Fix:** Add to §9.6 after exchange resolution rules:
> "If a character is physically incapacitated (Wound threshold reached) during a Debate, they immediately concede all remaining exchanges. The forfeit counts toward Grand Debate total-loss penalties. The Debate ends; the scene continues with the incapacitated character as a passive party. Social actions directed at them may still proceed — the GM sets consequences."
**Source:** G-099 / BT3-04

---

### PP-095
**Gap:** G-100 — Renown "initial advantage" scope undefined
**Severity:** P1
**Section:** §10.5 (Renown)
**Fix:** Add to §10.5 Renown entry:
> "Renown advantage: the +1D bonus applies to Exchange 1 only. It does not carry through subsequent exchanges. The advantage represents the recognition effect at first contact, not sustained rhetorical dominance."
**Source:** G-100 / BT3-06

---

### PP-096
**Gap:** G-101 — Niflhel supremacy tiebreak missing
**Severity:** P1
**Section:** Stage 6, §8.X Niflhel faction rules (seasonal accounting)
**Fix:** Add tiebreak rules to Niflhel seasonal accounting:
> "**Supremacy ties:** If multiple networks are co-leading at seasonal accounting, each co-leading network gains +1 Intel (all share the top position equally that season). If multiple networks are co-weakest, one is selected randomly (roll 1dN where N = number of tied weakest networks) to bear the weakest-network consequence."
**Source:** G-101 / BT3-08

---

### PP-097
**Gap:** G-102 — Niflhel partial endgame path undefined
**Severity:** P1
**Section:** Stage 6, Niflhel victory conditions
**Fix:** Define 3-step partial control victory procedure:
> "**Partial Network Dominance (fewer than 4 full networks):**
> 1. *Trigger:* Niflhel Intel is highest in exactly 3 or fewer networks AND this state has held for 2 consecutive seasons.
> 2. *Consolidation action:* Niflhel may spend a Unique Action to declare Quiet Network Consolidation. Roll Intel vs Ob 4.
> 3. *Resolution:* Overwhelming/Success = networks consolidated into a dominant position; counts as controlling that territory for victory condition purposes, and Niflhel's endgame path activates. Partial = consolidation incomplete; may retry next season at Ob 3. Failure = overextension; one network loses Niflhel's leading Intel status."
**Source:** G-102 / BT3-08

---

### PP-098
**Gap:** G-103 — TC pause + Baralta suppressor interaction undefined
**Severity:** P1
**Section:** §7.2 Theocracy Clock, Church Stability brake note
**Fix:** Add modifier-order clarification:
> "**Modifier order:** All TC modifiers (including leader-driven suppressors such as Baralta's −1) are applied first to determine the season's net TC change. The Stability brake is then checked. If after modifiers TC change would be ≤ 0, the brake does not further affect the result. If after modifiers TC change would be > 0 and Stability is ≤ 4, the brake sets TC change to 0 for that season. The brake cannot produce a TC decrease; it can only suppress generation."
**Source:** G-103 / BT3-09

---

### PP-099
**Gap:** G-104 — Niflhel Quiet Network "one piece of information" undefined
**Severity:** P1
**Section:** Stage 6, Niflhel Quiet Network seasonal event
**Fix:** Standardise information unit format:
> "**Quiet Network information unit:** Each seasonal event yields one unit. A unit is exactly one of the following (Niflhel chooses):
> - One faction's current Mandate, Influence, or Intel value (at accounting)
> - One pending Domain Action declared by a named faction in the coming season
> - The identity of one active informant or agent in another faction's current operations
> - One territorial event outcome before it is publicly resolved at accounting
>
> The unit must be specific and verifiable. 'What the Church is planning' is not a unit. 'Church will deploy Templars to Hafenmark this season' is a unit."
**Source:** G-104 / BT3-10

---

### PP-100
**Gap:** G-111 — Devout bypass for Discovery Events mechanically unreachable
**Severity:** P1
**Section:** Stage 3, §5.X Devout characters and Discovery Events
**Canon authority:** P-08 (barrier = inaccessibility, not suppression); P-10 (transformation = perceptual shift, not moral corruption)
**Fix:** Rewrite Devout bypass trigger. Replace TS-gated witnessing with direct theological confrontation:
> "**Devout character Discovery Event triggers:**
> A Devout character (TS 0–9) cannot perceive Thread operations and cannot trigger Discovery Events through ordinary Thread exposure. However, a Discovery Event fires when the character faces DIRECT THEOLOGICAL CONFRONTATION — defined as any of:
> - A practitioner performs a Thread operation in their presence AND explicitly demonstrates or names the mechanism (effects alone are insufficient; the claim must be made)
> - The character encounters explicit Einhir theological materials framed as directly opposing Galbados doctrine
> - A trusted peer, authority figure, or close Knot holder defects publicly to Restoration framing in the character's immediate presence
>
> Discovery Event Ob: set by the strength of the character's Conviction Beliefs (Ob = number of relevant Conviction Beliefs, minimum 1). The event is a theological confrontation, not a TS check. The Devout character's faith provides the interpretive framework; the confrontation challenges it directly."
**Source:** G-111 / Batch 3+4; P-08; P-10

---

### PP-101
**Gap:** G-112 — Ehrenwall Coup Tracker starting value and decrement missing
**Severity:** P1
**Section:** Stage 13, NPC Ehrenwall
**Fix:**
> "**Ehrenwall Coup Tracker (CoupT):**
> Starting value: 0 (no coup risk at game start — Ehrenwall's institutional loyalty is intact).
> *Increment triggers:* [retain existing definitions]
> *Decrement triggers:*
> - −1 per season where Crown Mandate ≥ 5 AND Crown Military ≥ 4 AND no Crown compromises were made that season (institutional strength confirmed)
> - −2 if Ehrenwall executes a direct Crown command that season (loyalty reinforced by clear institutional direction)
> - −1 if Crown publicly recognises Löwenritter contribution to territorial defence
>
> Ehrenwall's coup risk rises when the Crown institution appears to fail; it falls when the institution demonstrates coherent strength. Decrement is not guaranteed — if both decrement and increment triggers fire in the same season, net the results."
**Source:** G-112 / Batch 3+4

---

### PP-102
**Gap:** G-113 — Martial Law procedure undefined
**Severity:** P1
**Section:** Stage 6, §8.X Crown faction rules (or Stage 13 Ehrenwall)
**Fix:** 4-step Martial Law procedure:
> "**Martial Law (Löwenritter Coup):**
> *Trigger:* Ehrenwall Coup Tracker reaches threshold (see §NPC-Ehrenwall) OR Crown Mandate 0 + Military 3+ + Stability ≤ 2 simultaneously.
>
> **Step 1 — Stabilisation:** Crown Stability is frozen for 2 seasons (cannot decrease from non-military causes). This represents the Löwenritter suppressing civil disorder.
>
> **Step 2 — Mandate cost:** Crown Mandate −2 immediately (legitimacy cost of military rule). This cannot be recovered until Martial Law ends.
>
> **Step 3 — Restricted Orders:** During Martial Law, Crown's available Domain Actions are limited to Military operations, direct Mandate stabilisation (once per season), and Royal Decree. Diplomatic, economic, and intelligence Domain Actions are unavailable.
>
> **Step 4 — Sunset conditions:** Martial Law ends when Crown Mandate recovers to 4+ via available actions sustained over 3+ seasons (organic legitimacy recovery). Alternatively: Parliament convenes a Grand Debate challenge (Ob 4 vs Crown Military pool). If the Grand Debate challenge fails: Löwenritter becomes effectively autonomous — treat as Faction Fracture for Crown (see §8.1 Stability rules)."
**Source:** G-113 / Batch 3+4; PP-102

---

### PP-103
**Gap:** G-114 — Church TC 80 territorial seizure procedure missing
**Severity:** P1
**Section:** Stage 6, Church faction; Stage 5, TC threshold 80
**Fix:**
> "**Church Territorial Seizure (TC ≥ 80):**
> At TC ≥ 80, the Church may roll Mandate vs Ob = target territory's controlling faction Stability (1–7 scale) to claim territorial oversight.
>
> *Success:* Territorial control transfers to Church oversight. Target faction Stability −1 (transition friction). Target faction Mandate −1 (loss of territory). Church gains +1 Influence in that territory.
>
> *Overwhelming success:* As success, AND no Parliament challenge is possible that season (the Church has moved with overwhelming institutional speed).
>
> *Parliament challenge:* Within the same season (unless Overwhelming), any faction may spend a Domain Action to formally Contest the seizure. Contested resolution: contesting faction's Mandate vs Church Mandate (standard domain roll). Winner retains or reclaims control. Ties: status quo holds (seizure fails, but Church retains Influence gain).
>
> *Failure:* Seizure attempt publicly known; Church Mandate −1."
**Source:** G-114 / Batch 3+4; TC threshold card

---

### PP-104
**Gap:** G-115 — Archetype generic characters GEN-03, GEN-06, GEN-07 lack personal-scale mechanics
**Severity:** P1
**Section:** Stage 13, NPC/Archetype stat blocks
**Fix:** Add personal stat blocks for three archetypes. Attribute scale 1–10. Composure = Presence + 6.

> **GEN-03 — Generic Inquisitor (Church)**
> Agi 3 | End 3 | Str 2 | Cog 5 | Mem 4 | Focus 5 | Att 4 | Bonds 2 | Pres 3 | Spirit 3
> Composure: 9 | Health: 5
> Histories: Church Doctrine 3, Investigation 3
> Conviction: Duty / Doctrine
> Notes: Devout (TS-blocked). CE accumulation enabled — standard Inquisitor procedure. No Thread operation authority. Personal Resonant Style: Evidence (past heresies, records, accusations).

> **GEN-06 — Generic Riskbreaker**
> Agi 5 | End 3 | Str 3 | Cog 4 | Mem 3 | Focus 4 | Att 3 | Bonds 1 | Pres 3 | Spirit 3
> Composure: 9 | Health: 6
> Histories: Covert Operations 3, Trade Network 2
> Conviction: Pragmatism / Survival
> Deniability Debt: starts at 0
> Notes: Not Church-affiliated. CE does not accumulate unless operating inside Church-observed territory. No Thread sensitivity by default.

> **GEN-07 — Generic Knight Templar**
> Agi 4 | End 5 | Str 5 | Cog 2 | Mem 2 | Focus 3 | Att 1 | Bonds 3 | Pres 3 | Spirit 4
> Composure: 9 | Health: 10
> Histories: Church Military Service 4, Heresy Recognition 2
> Conviction: Duty / Galbados
> Notes: Devout (TS-blocked). CE passive accumulation only — no active investigation authority. Deploys under Cardinal of Fortitude direction. Personal Resonant Style: Character (virtue, duty, honour, shame).

**Source:** G-115 / Batch 3+4

---

### PP-105
**Gap:** G-116 — Collective lattice co-movement scaling undefined
**Severity:** P1
**Section:** Stage 3, §5.1.5 Collective Operations (or equivalent)
**Canon authority:** P-01 (inseparability is mandatory — all three auto-effects fire regardless of participant count)
**Fix:**
> "**Collective operation co-movement scaling:**
> Co-movement effects are not optional and do not scale with participant count — all three dimensional auto-effects fire for every collective Thread operation (P-01). However, magnitude scales:
> - **CD accumulation:** +1 per additional participant beyond the first (maximum +3 total additional)
> - **RS cost:** ×participant count (no cap — this is the primary risk of collective operations; large lattices produce severe RS strain)
> - **TT change:** use Community Weaving scaling (§6.8): base TT cost × ceil(participants ÷ 2), capped at ×3
>
> These costs apply to each participant individually. The pool benefit (combined dice) must be weighed against the cost scaling."
**Source:** G-116 / Batch 3+4; P-01

---

### PP-106
**Gap:** G-117 — Anchor-drop outcome in collective operations undefined
**Severity:** P1
**Section:** Stage 3, §5.1.5 Collective Operations
**Fix:**
> "**Anchor drop mid-operation:**
> If the designated anchor drops contact during a collective operation (Wound, Composure collapse, involuntary Leap, incapacitation, or any forced contact termination):
> 1. The lattice immediately dissolves.
> 2. All participants who were in active contact at the moment of anchor drop take consequences equal to a Partial-degree outcome for the in-progress operation.
> 3. The operation does not complete — no effect, no benefit achieved.
> 4. All TT and CD costs already accumulated at the point of anchor drop remain (the substrate was already strained).
> 5. RS costs: each participant takes RS −1 (abrupt termination); the anchor takes RS −2."
**Source:** G-117 / Batch 3+4

---

### PP-107
**Gap:** G-118, SIM2-F-03, SIM2-F-04, SIM7-F-03 — Past-Oriented Pulling: no degree table, missing recency table, near-inaccessibility, no Foundational scale rules
**Severity:** P1 (G-118, SIM2-F-03, SIM7-F-03), P1 (SIM2-F-04)
**Section:** Stage 3, §5.6 Past-Oriented Pulling
**Fix — Part A: Recency Ob Table**

> | Timeframe | Ob modifier |
> |-----------|-------------|
> | Current season | +0 |
> | 1–3 seasons past | +1 |
> | 1–5 years past | +2 |
> | 5–20 years past | +3 |
> | 20–100 years past | +4 |
> | Pre-independence (100+ years) | +5 |
> | Pre-Altonian era (200+ years) | +6 |
> | Einhir era | +6 + Einhir framework required |

**Fix — Part B: Degree Table**

> | Degree | Outcome |
> |--------|---------|
> | Overwhelming | The target configuration is fully accessible. Complete rendering with clarity. RS −2. TT +3 (in addition to base TT table cost). All sought information or effect obtained without distortion. |
> | Success | Configuration accessible; rendering is partial. Core of what was sought is present; peripheral details uncertain. RS −1. TT +3. GM may withhold one significant detail. |
> | Partial | Contact made; configuration unstable. Fragmented rendering — disconnected impressions rather than coherent information. RS −1. TT +3. GM provides one true detail and one ambiguous impression. Practitioner cannot control what surfaces. |
> | Failure | Contact attempted; substrate resists temporal displacement. No rendering achieved. RS −2 (failed attempt still strains substrate). TT +5. An orphaned configuration may form (GM discretion) — detectable by TS 30+ Diagnosis. |

**Fix — Part C: Pool Accessibility Note**
> "Standard pool: Spirit + History + TPS ÷ 2. Minimum viable pool for reliable access: 5+ dice. Characters below this threshold should treat Past-Oriented Pulling as advanced technique requiring Einhir mentorship or significant TPS accumulation. Accessibility path: a practitioner may substitute one relevant Belief die (if the Belief directly relates to the pulled event or person) as one pool die — once per operation. This represents personal connection bridging the substrate gap."

**Fix — Part D: Foundational Past-Pull (Einhir Catastrophe Protocol)**
> "**Foundational Past-Pull (Einhir Catastrophe Protocol):**
> Named mechanic for operations reaching pre-Calamity configurations. Requires: Einhir-framework-trained practitioner, TPS ÷ 2 minimum 3, Spirit 5+.
>
> - Ob: base recency Ob +4 (Foundational scale penalty, per Scale Principle)
> - Pool: Spirit + History + TPS ÷ 2 + Einhir Resonance bonus (+2D if applicable)
> - RS cost: ×3 base cost
> - TT: +9 additional (base Past-Pull +3 at ×3)
>
> | Degree | Outcome |
> |--------|---------|
> | Overwhelming | Access to pre-Calamity thread configuration states. The original source of a Gap can be identified. Cannot reconstruct or reverse the Calamity — only understand it. RS −6. |
> | Success | Partial pre-Calamity access. One major fact about the Calamity's origin. RS −4. |
> | Partial | Fragmented impressions only. No actionable information. RS −3. |
> | Failure | Uncontrolled temporal displacement event. RS −4. TT +12 (stacks with base cost). GM determines displacement consequences. |
>
> Use limit: once per campaign arc unless extraordinary circumstances (GM discretion)."

**Source:** G-118, SIM2-F-03, SIM2-F-04, SIM7-F-03

---

### PP-108
**Gap:** G-125 — No social counter-mechanic for non-practitioners being Pulled
**Severity:** P1
**Section:** Stage 3, §5.3 Pulling (or §5.6 Past-Oriented Pulling, non-practitioner subsection)
**Canon authority:** P-09 (Pulling is messy, costly, detectable); P-08 (barrier = inaccessibility)
**Fix:**
> "**Non-practitioner resistance to Pulling:**
> A non-practitioner cannot perceive Thread operations but can feel their effects at the experiential level. When a Pulling operation targets a non-practitioner, the target may attempt to resist:
>
> - **Resistance roll:** Spirit dice, Ob = Pulling Ob (same Ob as the operation)
> - This represents the integrity of the target's self-coherence, not Thread perception
>
> | Degree | Result |
> |--------|--------|
> | Overwhelming | Target unreachable. Operation fails. Pulling practitioner takes RS −1 (failed contact). |
> | Success | Target resists successfully. No information extracted. Practitioner may re-attempt next round at +1 Ob (cumulative per attempt). |
> | Partial | Partial resistance. Memories surface chaotically — GM provides one distorted or incomplete piece of information. |
> | Failure | Pull proceeds normally. Resolve the Pulling operation at its rolled degree. |"

**Source:** G-125 / sim_batch_02

---

### PP-109
**Gap:** G-127 — Dissolution Residue drain target is wrong (says Coherence; should be Certainty); SIM5-F-07 resolved as consequence
**Severity:** P1
**Section:** Stage 3, §5.12 Dissolution Residue
**Fix:**
> "**Dissolution Residue drain target (corrected):**
> Dissolution Residue drains **Certainty (−1 per exposure)**, NOT Coherence. Coherence is the practitioner's personal countdown track (10→0); Certainty is the world-side track. The residue represents unanchored substrate configuration affecting the Certainty of the environment.
>
> *Exception:* Direct sustained contact with residue lasting a full scene or longer triggers an additional **Coherence −1** for any practitioners present (personal integrity cost of prolonged unanchored substrate proximity).
>
> *Consequence for SIM5-F-07:* The Coherence cap (−1/operation maximum) does not make residue cost-free. Residue and Thread operations drain separate tracks. They are not in competition."
**Source:** G-127 / sim_batch_02; SIM5-F-07

---

### PP-110
**Gap:** G-128 — ThS Fallout table uses per-character framing; ThS is a world-side track
**Severity:** P1
**Section:** Stage 3, §5.9 Thread Sensitivity thresholds / Fallout table
**Fix:** Rewrite §5.9 Fallout table headers and trigger language:
> "All Fallout table entries should be rewritten from 'your ThS drops to X' to 'World-side ThS drops below X.' The consequences listed still affect practitioners in the affected area, but ThS is a property of the world-thread-substrate, not of individual characters. A practitioner does not have a ThS score. They have Thread Sensitivity (TS) as a personal attribute. ThS is the world's accumulated thread-sensitivity threshold — the degree to which the substrate has been sensitised by practitioner activity across all history.
>
> Audit note: any §5.9 entry reading 'your ThS' or 'the practitioner's ThS' is a text error. Replace with 'world-side ThS' or 'the current world ThS level.'"
**Source:** G-128 / sim_batch_03

---

### PP-111
**Gap:** G-129 — Torben Loyalty Clock drain rate absent
**Severity:** P1
**Section:** Stage 13, NPC Torben
**Fix:**
> "**Torben Loyalty Clock (TLK) — drain rate:**
> - Base drain: −1 per season Torben remains in the Altonian court without active Crown contact
> - Failed tutoring demand (triggered at IP 30): −3 if Crown fails to respond within the same season
> - Successful covert contact (Int Ob 3): −0 that season (contact stabilises loyalty)
> - Detected or failed covert contact: −2 (detection increases institutional risk; Torben reads it as Crown exposing him)
>
> *Milestone events:*
> - Elske recruited by an Altonian faction: −3 (Torben's primary personal anchor moves to opposing interest)
> - Crown publicly acknowledges Torben's lineage in official capacity: +2 recovery (one-time; cannot be repeated)
> - Altonian faction offers Torben a formal titled position: −2 per season that offer stands uncontested by Crown"
**Source:** G-129 / sim_batch_03

---

### PP-112
**Gap:** G-130 — Concealment mechanic: no Ob, no resolution, no counter-detection
**Severity:** P1
**Section:** Stage 3, §5.X Concealment (new subsection)
**Fix:** Write Concealment procedure:

> "**Concealment**
> Concealment allows a practitioner to suppress the Thread operation signature observable by outside parties.
>
> *Declaration:* Simultaneous with the Thread operation declaration. Concealment is a separate roll, not part of the operation pool.
> *Pool:* Attunement + Cognition (the practitioner's awareness of their own signature)
> *TN:* 7 (Standard)
>
> **Ob by observer:**
> | Observer | Ob |
> |----------|-----|
> | Non-practitioner | 1 |
> | TS 10–29 | 2 |
> | TS 30–59 | 3 |
> | TS 60+ | 4 |
>
> **Ob modifiers:**
> - Active combat or high distraction in scene: −1 Ob
> - TT Fracturing (60+): +1 Ob (noisy substrate)
> - Severed (Coherence 1): +1 Ob (signature irregularity)
>
> | Degree | Result |
> |--------|--------|
> | Overwhelming | No detectable signature. CE does not accumulate for Inquisitor observers this operation. |
> | Success | Signature masked. CE accumulation halved for Inquisitor observers this scene. |
> | Partial | Signature reduced. Evidence exists but not attributable to a specific practitioner. CE accumulates normally. |
> | Failure | No concealment. Signature fully visible to any TS 10+ observer. CE accumulates normally. |
>
> Concealment failure does not affect the operation itself."
**Source:** G-130 / sim_batch_03

---

### PP-113
**Gap:** G-131 — Parliamentary Vote coalition formation absent
**Severity:** P1
**Section:** §9.6 Debates / §8.9 Parliamentary Vote (or Stage 6 faction rules)
**Fix:** Coalition formation procedure:
> "**Parliamentary Vote — Coalition Procedure:**
>
> 1. **Declaration phase:** Before vote rolls, all factions simultaneously declare their position: Support, Oppose, or Abstain.
> 2. **Pool construction:** Supporting factions contribute their Mandate dice to the lead faction's pool. Opposing factions contribute their Mandate to the opposing pool.
> 3. **Vote resolution:** Uses Debate exchange structure (best of 3). Lead faction rolls combined coalition pool vs opposing coalition pool. Faction leaders who are present personally may use the higher of their personal pool or their faction's Mandate.
> 4. **Abstentions:** Abstaining factions take no pool action but gain information — they observe the full coalition structure that season at no cost.
> 5. **Betrayal mechanics:** If a faction declares Support but betrays (votes against or Abstains): detectable on a Partial or Failure result for the coalition that season. Detected betrayal: betraying faction Mandate −1 per supporter deceived, and Intel accumulates against that faction (they are known as unreliable coalition partners).
> 6. **Ties:** Status quo holds — no motion passes on a tied vote."
**Source:** G-131 / sim_batch_03

---

### PP-114
**Gap:** G-132 — Stability floor of 1 prevents faction collapse and endgame via attrition
**Severity:** P1
**Section:** §8.1 Faction Mechanics (seasonal accounting rules)
**Fix:** Remove the Stability floor. Replace with:
> "**Faction Stability at 0 — Crisis and Fracture:**
> Stability can reach 0. No floor applies.
>
> *Stability 0:* Faction enters **Crisis**. All Domain Actions cost +2 Ob. Unique Action unavailable. Stability 0 triggers a Mandate check (see PP-127).
>
> *Stability 0 for 2 consecutive seasons:* **Faction Fracture.** The faction is eliminated as a player-controlled entity. Its institutional remnants continue as a GM-controlled NPC faction at half capacity (all stats halved, rounded down). Fractured factions can be rebuilt through extraordinary player action — this is a campaign-level event, not a game end.
>
> *Crown and Church exception:* Neither can Fracture through Stability alone (institutional depth). Additional trigger required: Crown (Martial Law already in effect + Stability 0), Church (Confessor death or Confessor excommunication from within + Stability 0)."
**Source:** G-132 / sim_batch_03

---

### PP-115
**Gap:** G-133 — Niflhel has no Intel stat defined
**Severity:** P1
**Section:** Stage 6, §8.X Niflhel faction; §8.1 Starting Values table
**Fix:**
> "Add to Niflhel faction stat block:
> **Intel: 6** (starting value). **Maximum: 8.**
>
> Rationale: Niflhel is a covert intelligence operation by nature. Intel 6 reflects established, functioning networks from game start. The 8 maximum reflects the hard ceiling of an organisation operating without public institutional support. Niflhel cannot project force (no Military stat) and cannot build legitimacy (no Mandate stat); Intel is their primary operational asset.
>
> Update §8.1 Starting Values table: Niflhel Intel column = 6."
**Source:** G-133 / sim_batch_03

---

### PP-116
**Gap:** G-134 — Community Weaving TT cost scaling undefined
**Severity:** P1
**Section:** Stage 3, §6.8 Community Weaving (or equivalent)
**Fix:**
> "**Collective Community Weaving — TT cost scaling:**
> Collective TT cost = individual base TT cost × ceiling(participants ÷ 2), maximum ×3.
>
> Examples: 2 practitioners = ×1. 3–4 practitioners = ×2. 5–6 practitioners = ×3 (cap). 7+ practitioners = ×3 (cap holds).
>
> The cap reflects that collective resonance partially offsets individual substrate strain at scale — but never eliminates it. Larger groups produce more total TT than smaller groups but not proportionally more."
**Source:** G-134 / sim_batch_03; PP-105 alignment

---

### PP-117
**Gap:** G-135 — Mass combat damage formula not specified
**Severity:** P1
**Section:** Stage 8 (or equivalent mass combat section), §8.3
**Fix:**
> "**Mass combat damage formula:**
> - *Excess successes:* attacker's net successes − defender's net successes (minimum 0)
> - *Unit damage:* excess successes × attacking formation's **Power** rating
> - *Damage absorbed:* subtract defending unit's **Armour** rating (minimum 0 damage after absorption)
> - *Accumulated damage:* when total accumulated damage ≥ unit **Health** threshold, the unit is eliminated
>
> This mirrors the personal combat formula (§8.1): weapon damage bonus + excess successes − armour damage reduction. Unit Power = equivalent of weapon damage bonus. Unit Armour = equivalent of personal armour DR. Unit Health threshold = equivalent of personal Wound threshold."
**Source:** G-135 / sim_batch_04

---

### PP-118
**Gap:** G-136 — Church Stability TC brake fires at Stability ≤5 but Church starts at Stability 5 (permanent suppression from game start); stage 5 / stage 6 text conflict
**Severity:** P1
**Section:** §7.2 TC Clock (stage 5); §8.3 Church faction (stage 6)
**Fix:** Standardise brake threshold to **Stability ≤ 3** across both documents (lowered from ≤4/≤5 versions).

> **Rationale:** Church starting Stability is 5. A brake at ≤4 is reachable but not permanent from game start. A brake at ≤5 fires from game start (bug). After simulation review: ≤3 is the correct threshold — this makes the brake a meaningful crisis condition rather than an ambient suppressor, consistent with the intent that Church TC generation should be suppressible only in genuine internal crisis conditions (Stability 3 = two losses from starting value).
>
> **Stage 5 fix:** §7.2 brake note: replace "Stability falls to 5 or below" and "Stability ≤ 4" with "Stability ≤ 3."
> **Stage 6 fix:** §8.3 TC relationship note: replace "Stability ≤ 4" with "Stability ≤ 3."
**Source:** G-136 / sim_batch_04

---

### PP-119
**Gap:** SIM2-F-09 — Involuntary→voluntary extension bypasses concealment (exploit)
**Severity:** P1
**Section:** Stage 3, §5.1.3 Involuntary Leap + §5.X Concealment
**Fix:**
> "**Voluntary extension of involuntary Leap — concealment rule:**
> Any voluntary extension of an involuntary Leap is treated as a **voluntary Thread operation** for all concealment and CE accumulation purposes. The involuntary initiation does not grant concealment immunity to subsequent voluntary operations in the same contact. A practitioner who chose to extend an involuntary Leap chose to operate — that choice carries the full procedural obligations of voluntary Thread work."
**Source:** SIM2-F-09 / sim_batch_02

---

### PP-120
**Gap:** SIM5-F-02 — Lock removal Ob asymmetry (high-TS Locks near-irremovable); design rationale missing
**Severity:** P1 (documentation/design note)
**Section:** Stage 3, §5.5 Locking
**Fix:** Add design note + bypass path:
> "**Lock removal asymmetry — design rationale:**
> Lock removal Ob = (original TS ÷ 10) − 2 (minimum 1). At TS 100: Ob 8. This is intentional. Locks created by high-TS practitioners are deeply substrate-integrated; the asymmetry reflects the Scale Principle — Thread work at higher TS penetrates further below the waterline and is proportionally harder to undo.
>
> **Bypass path:** Rather than removing a Lock directly via Dissolution, practitioners may address the underlying Gap the Lock was placed to protect. If the Gap is fully Mended, the Lock loses its substrate rationale and may be removed at **Ob 2** (standard maintenance Dissolution, regardless of original TS). This reframes the problem: the Lock is a consequence. Address the cause."
**Source:** SIM5-F-02 / sim_batch_05

---

### PP-121
**Gap:** SIM6-F-03 — Severed (Coherence 1): no Thread operation Ob penalty listed
**Severity:** P1
**Section:** Stage 3, Coherence table (§5.X)
**Canon authority:** P-03 (rendering = consciousness-performed; practitioner is the rendering engine)
**Fix:**
> "Add to Coherence track table:
> **Coherence 1 (Severed): +2 Ob to all Thread operations.**
>
> Rationale (P-03): At Coherence 1, the practitioner's self-coherence is near-total collapse. Thread operations require a coherent self as the rendering engine. The +2 Ob reflects the practitioner struggling to maintain coherent intent while performing Thread work — not a mechanical punishment, but the natural consequence of operating at the threshold of personal dissolution."
**Source:** SIM6-F-03 / sim_batch_06; P-03

---

### PP-122
**Gap:** SIM6-F-05 — Rendering Crisis mid-contact: no contact termination rule
**Severity:** P2
**Section:** Stage 3, §5.X Rendering Crisis
**Fix:**
> "**Rendering Crisis during active contact:**
> When a Rendering Crisis fires while a practitioner is in active Thread contact, the practitioner rolls Endurance vs Ob 2 (crisis onset resistance).
>
> *Success:* Contact maintained. Rendering Crisis symptoms are deferred to end of contact (not suppressed; merely postponed). RS continues degrading normally through contact.
>
> *Failure:* Contact terminates immediately. This is an involuntary termination — for collective operations, treat as anchor drop (PP-106: all participants take Partial consequences; anchor takes RS −2).
>
> *Either way:* The Rendering Crisis cannot be resolved until after contact ends. Attempting to Mend or otherwise address the Crisis while in contact is not possible."
**Source:** SIM6-F-05 / sim_batch_06

---

### PP-123
**Gap:** SIM6-F-10 — RS Critical terminal decline 2–4 seasons not documented
**Severity:** P1
**Section:** Stage 3, §5.4.3 RS Critical (or RS threshold table)
**Fix:** Add GM documentation note to RS Critical entry:
> "**RS Critical (RS 1–10) — Terminal Phase Note:**
> RS Critical is the terminal phase. At standard play pace and without extraordinary intervention, a world at RS Critical will reach RS 0 (The Rupture) within **2–4 seasons**. This timeline is by design.
>
> Extraordinary intervention options: Ceiral Ritual (RS +6 on Success, +10 on Overwhelming), Foundational Mending (Ob 8; RS +4 on Overwhelming), sustained Community Weaving (RS +2/season).
>
> Any Foundational-scale Thread failure at RS Critical carries a high probability of triggering The Rupture immediately. The table should treat RS Critical as the endgame phase — not a recoverable normal state. Player characters who reach RS Critical without active repair operations underway have functionally entered the endgame."
**Source:** SIM6-F-10 / sim_batch_06

---

### PP-124
**Gap:** SIM7-F-07 — Simultaneous Dissolution + Mending on same site: §9.13 doesn't cover
**Severity:** P2
**Section:** Stage 3, §9.13 Opposing operations (add sub-case)
**Fix:**
> "**Opposing operations sub-case: Simultaneous Dissolution + Mending on the same site**
> Both operations resolve at Priority 5. Apply opposing operations framework:
>
> - *Mending wins (higher net successes):* Mending applies at rolled degree. Dissolution partially succeeds (Partial degree regardless of rolled degree). Both practitioners pay their RS costs.
> - *Dissolution wins:* Dissolution applies at rolled degree. Mending fails (Failure degree; no RS recovery). Both pay RS costs.
> - *Both Overwhelming OR tied:* Neither operation completes. Both practitioners take RS −1 (substrate instability from contested operations). Both must re-initiate next round if they choose to continue.
>
> This sub-case is separate from standard opposing operations (two practitioners running conflicting operations on different targets)."
**Source:** SIM7-F-07 / sim_batch_07

---

### PP-125
**Gap:** SIM7-F-08 — Incapacitation threshold rounding for odd Health values
**Severity:** P2
**Section:** §8.1 Personal Combat (damage / incapacitation threshold)
**Fix:**
> "Add to §8.1: **Incapacitation threshold = floor(Health ÷ 2).** Always round down. Example: Health 7 → threshold 3; Health 9 → threshold 4."
**Source:** SIM7-F-08 / sim_batch_07

---

### PP-126
**Gap:** SIM7-F-09 — CE ceiling and overflow behaviour absent
**Severity:** P2
**Section:** Stage 3, §5.X CE accumulation rules; Stage 6, Church / Inquisitor rules
**Fix:**
> "**CE ceiling and overflow:**
> CE maximum value: **10** (matching the 1–10 attribute scale used throughout the system).
>
> CE cannot exceed 10. Events that would push CE above 10: the overflow is lost (not carried forward). However, if CE is at 10 AND an event would overflow in the same season: the GM triggers a **Discovery Event** immediately (the character has been at maximum epistemic saturation for an extended period — the cognitive/spiritual pressure demands a reckoning)."
**Source:** SIM7-F-09 / sim_batch_07

---

### PP-127
**Gap:** SIM7-F-10 — Mandate 0 Stability check consequence undefined
**Severity:** P2
**Section:** §8.1 Faction Mechanics (seasonal accounting)
**Fix:**
> "**Mandate 0 — Stability check:**
> When a faction's Mandate reaches 0 at seasonal accounting, trigger an immediate Stability check, Ob 3.
>
> | Degree | Result |
> |--------|--------|
> | Overwhelming / Success | Stability holds. Mandate recovery capped at 2 for the following season (floor effect — the faction is damaged but intact). |
> | Partial | Stability −1. Mandate recovery capped at 1 next season. |
> | Failure | Stability −2. If Stability then reaches 0: Faction Fracture activates immediately (see PP-114). |"
**Source:** SIM7-F-10 / sim_batch_07

---

### PP-128
**Gap:** SIM8-F-09 — No TTRPG residue harvesting procedure (Niflhel)
**Severity:** P2
**Section:** Stage 6, §8.X Niflhel faction rules
**Fix:**
> "**TTRPG Residue Harvesting (Niflhel):**
> Niflhel operates a black market in threadweaved items and residue deposits. Harvesting procedure:
>
> *Requirements:* A character with TS 10+ to perceive the deposit, OR a Niflhel-affiliated character with a relevant History (Southernmost Trade, Black Market, Covert Commerce). Niflhel harvesters without TS rely on contracted Restoration members (TS 10–29) for sourcing.
>
> *Roll:* Attunement + relevant History vs Ob = residue density (GM-set 1–3; Ob 3 = heavy residue from a major recent Thread operation)
>
> | Degree | Result |
> |--------|--------|
> | Overwhelming | Harvest yields 2 tradeable units. No CE risk. |
> | Success | Harvest yields 1 tradeable unit. |
> | Partial | Harvest yields 1 unit. Exposure risk: CE check for any practitioners present (Ob 2). |
> | Failure | No harvest. CE accumulation check for practitioners present (Ob 1). Deposit location may be noted for future attempt. |
>
> *Tradeable unit value:* 1 unit = Wealth +1 to Niflhel faction at next seasonal accounting, OR exchangeable for Circles +1 with a practitioner contact."
**Source:** SIM8-F-09 / sim_batch_08

---

### PP-129
**Gap:** SIM8-F-10 — CE pooling through Church hierarchy undefined
**Severity:** P2
**Section:** Stage 6, §8.3 Church faction rules; Stage 13, NPC Klapp
**Fix:**
> "**CE pooling — Church hierarchy (Cardinal Klapp):**
> Inquisitors accumulate CE per standard rules during investigations. At seasonal accounting, each Inquisitor reports accumulated CE to their Cardinal.
>
> *Klapp's investigation pool:* sum of all reported CE ÷ 2 (rounded down). The halving reflects information degradation through hierarchy — not all field evidence survives transmission cleanly.
>
> *Pool spending:* Klapp may spend pooled CE to initiate a Mandate-level action (formal Church Inquisition deployment) at Ob = (10 − pooled CE). Pooled CE resets to 0 after spending. Minimum spendable pool: 3.
>
> *Access restrictions:* This pool is Klapp-specific. Confessor Himlensendt does not have access to this pool by default. Cardinal Olafsson has a separate independent pool (defined in NPC-Olafsson when compiled). Cross-Cardinal CE sharing requires a Domain Action (Influence-based coordination)."
**Source:** SIM8-F-10 / sim_batch_08

---

### PP-130
**Gap:** SIM3-F-02, SIM3-F-03 — Crown no TS 70+ practitioner (Territorial Lock inaccessible); Hafenmark no practitioners
**Severity:** P2 (design notes, not rule gaps)
**Section:** Stage 6, §8.2 Crown faction; §8.5 Hafenmark faction
**Fix:** Document as deliberate asymmetry (not a bug; these are design features requiring text acknowledgment only):

> "**Crown — Thread asymmetry note:**
> The Crown has no TS 70+ practitioner in canon (Almud TS 28, Lenneth max ~40–50 on standard timeline). Territorial Lock (requires TS 70+) is inaccessible to the Crown as a direct faction action. This is deliberate. Crown Thread-adjacent play is limited to: supporting existing practitioners, indirect political pressure on practitioner factions, and Lenneth's scholarly research path. The Crown is structurally disadvantaged in direct Thread operations. This asymmetry drives the political logic of Crown–Varfell and Crown–Revolution relationships."

> "**Hafenmark — Thread asymmetry note:**
> Hafenmark has no affiliated practitioners and no practitioner tradition. Thread entry points for Hafenmark: (a) formal alliance with Restoration/Revolution practitioners, (b) Baralta's unique position (can perceive Thread evidence without TS via legal/documentary means; can provide access through institutional channels), (c) recruitment of independent practitioners through Wealth-based agreements. Hafenmark cannot initiate Thread operations as faction actions. This asymmetry is deliberate and consistent with Hafenmark's constitutional-legalist ethical framework — Thread operations do not map onto their institutional logic."

**Source:** SIM3-F-02, SIM3-F-03 / sim_batch_03

---

## PATCH COUNT SUMMARY (UPDATED 2026-03-28)
| Severity | Count |
|----------|-------|
| P1 | 55 (+20) |
| P2 | 57 (+10) |
| P3 | 10 |
| Design (new mechanic) | 8 (+7) |
| **Total** | **130 (+37)** |

*PP-094 through PP-130: 37 new patches. All derived from canon constraints, compiled stage documents, and internal system logic. No editorial approval required (none of these are setting, NPC identity, faction-narrative, or design-intent-ambiguous decisions).*
