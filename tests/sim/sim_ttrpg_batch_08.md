# VALORIA STRESS TESTS — BATCH 08
## Remaining Cell Coverage + BG Mode Combat + P1 Mechanic Isolation
**Executed:** 2026-03-27 | **Model:** Opus 4.6 | **Skill:** valoria-simulator
**Purpose:** Close remaining isolation/scenario cells; cover M-026/M-041/M-052 interaction bar; BG combat mode; P1 mechanic missing cells.

---

## T-B8-01 — PULLING: INTERACTION + SCENARIO (M-016)
**Coverage:** M-016, M-011, M-037, M-048
**Mode:** TTRPG | **Temporal:** PRES/CROSS | **Tracks:** TT,TD,TS,FSTAT,IP | **Factions:** Crown,Church | **NPCs:** Almud,Himlensendt | **Archetypes:** Practitioner,Faction Leader
**Cells filled:** M-016 Interaction, M-016 Scenario

### Mode B — Interaction (F25 deep test)

**Setup:** Almud (TS 8) attempts a Pull on Himlensendt's belief network — altering his Thread-connected relationship to the Church's founding covenant. This is the canonical F25 scenario: Pull against a social relationship with no counter-roll.

**Chain:** Almud diagnoses Himlensendt's Thread connections (M-014) → Pulls on the covenant connection (M-016) → Faction stat consequence (M-034) → Scale transition check (M-048)

**Practitioner state:**
```
Almud — TS 8, TD 3, Certainty 7, Coord 3
TT 30 | TC 48
```

**Pull mechanics — F25 confirmed pathways:**

Pool: TS/2 = 4D, TN7, Ob 3 (social relationship Pull, elevated from personal Ob 2)
TD 3: below threshold 5, no modifier.
Expected net: 4 × 0.33 = 1.32 | P(≥3 net) ≈ 25%

This is a low-probability operation. Almud is a mid-tier practitioner attempting a high-Ob Pull.

**No counter-roll from Himlensendt (F25 confirmed):** Himlensendt has no mechanic to resist or detect the Pull unless he has TS. Himlensendt TS = 0 (Devout). The Pull occurs entirely without his awareness or participation.

**Interaction with M-011 (Circles):**
The Pull targets a Thread connection underlying a *social* relationship (Himlensendt's covenant bond). If successful, the altered Thread connection should weaken Himlensendt's institutional authority claim (his Circles with Church hierarchy would logically degrade). No mechanic specifies that a successful Pull on a social relationship reduces target's Circles rating.
**GAP: Pull success has no mechanical expression on social mechanics.** The Thread is altered but the social consequence is GM-narrative only. A successful Pull on Himlensendt's covenant bond *should* mechanically reduce his Church Circles or Mandate contribution, but doesn't.

**Proposed fix extension to PP-026:** Add: "A successful Pull on a Thread connection underlying a social relationship reduces the target's relevant Circles rating by 1. An Overwhelming Pull reduces it by 2."

**Interaction with M-048 (Scale Transitions):**
If Almud's Pull achieves Overwhelming (P ≈ 5% at current pools): Scale transition triggers.
Personal Pull → Faction-level consequence: Church Mandate −1 (covenant bond weakened at institutional scale).
Per PP-039: this counts as Crown's Political Domain Action for the season.

**Scenario — The Synod Session:**
TC 48. Himlensendt is presenting at Synod (if active) or preparing the TC-50 threshold motion.
Almud acts during the preparation period (between sessions of formal debate).

Most likely Pull outcome (75% probability = Failure or Partial):
- Failure (75%): Almud's Pull fails. TT +1 (failed operation still causes ambient Thread activity). Himlensendt's conviction is unaltered. TC motion proceeds.
- Partial (if net >0 but <3): Pull partially lands. Thread connection wobbles — Himlensendt experiences a moment of doubt (Composure −1 this scene). Not mechanical enough to alter his faction behavior.

Low probability Pull success (25%): Himlensendt's conviction is altered. He debates less effectively this season (Mandate −1 for Debate purposes only, not general). TC gain from his Domain Action this season: −1D.

**M-016 as a low-probability precision tool:** This test confirms that M-016 (Pulling) at standard practitioner levels is a low-probability, high-impact mechanic. It's not a reliable combat tool — it's a surgical intervention that occasionally lands and shifts the campaign when it does. This is consistent with Foundations P-09.

### Proposed fix PP-026 extension (above) + new finding:

**F-B8-01** (P2) — Pull success has no mechanical expression on social mechanics. The Thread connection is altered but Circles/Mandate remain unchanged. Successful Pulls are narratively validated but mechanically invisible beyond the GM's fiction.

**Proposed fix:** Add to Pull rules: "A successful Pull on a Thread connection underlying a social relationship (Circles network, institutional authority, interpersonal bond) reduces the target's relevant Circles or faction stat by 1. Overwhelming: by 2. The character whose Thread is altered is not aware of the cause unless they have TS ≥ 5."

---

## T-B8-02 — COHERENCE TRACK: INTERACTION + SCENARIO (M-021)
**Coverage:** M-021, M-009, M-020, M-016, M-013
**Mode:** TTRPG | **Temporal:** CROSS | **Tracks:** CERT,ThS,TD,TT | **Factions:** Niflhel | **NPCs:** — | **Archetypes:** Practitioner
**Cells filled:** M-021 Interaction, M-021 Scenario

### Mode B — Interaction Chain

**Chain:** Coherence degradation (M-021) → Certainty floor reduction (M-009) → ThS accumulation (M-020) → attempted Leap (M-013) → Pull failure (M-016) → Coherence −1

**Practitioner state — high-use scenario:**
```
TS 20, TD 9, Certainty 4, Coherence 5/10
TT 36 | ThS 16
```

**Coherence 5 mechanical effects:**
Per §4.5/§5.10 conflict (PP-012): if Intelligibility track governs (passive degradation path):
- Coherence 5: no penalty yet (threshold at 3)
- At Coherence 3: Intelligibility degradation begins — social communication impaired

If Coherence transformation track governs (active path):
- Coherence 5: +2D to Thread ops (§5.10)

Using passive degradation interpretation (pending PP-012 resolution).

**Certainty floor at Coherence 5:**
Certainty maximum = Spirit stat + Coherence tier bonus. At Coherence 5: no maximum reduction yet.
At Coherence ≤ 3: Certainty maximum = Spirit (no Coherence bonus). For Spirit 3 practitioner: Certainty max = 3.
**Coherence degradation compresses the Certainty ceiling — this is the interaction.**

**Leap attempt (M-013):**
Pool: TS/2 = 10D, TN7, Ob 2 → TD 9 (below threshold 10, Ob +1 at 10) → Ob 2
P(≥2 net, 10D) ≈ 90%. Leap succeeds.
TD: 9 → 10 (threshold crossed). Next operations: Ob +2 total.

**Coherence −1 from Leap at high TD:**
Rule (reconstructed from batch data): each Thread op at TD ≥ 10 risks Coherence degradation. Check: d10, result ≤ TD: Coherence −1.
At TD 10: d10 ≤ 10 = 100%. **Every Thread op at TD 10+ degrades Coherence automatically.**
This is the terminal cascade: TD 10 = guaranteed Coherence loss per operation.

**Coherence 5 → 4 → 3 (Intelligibility threshold in 2 operations):**
At Coherence 3: social communication impaired (−2D on explanation/coordination rolls).
At Coherence 2: character cannot clearly communicate Thread perceptions.
At Coherence 1: character is isolated — others cannot understand them on Thread topics.
At Coherence 0: character is unreachable (Monstrous Entity transition threshold).

**ThS interaction (M-020):**
ThS 16 at Coherence 3: practitioner is both cognitively degrading AND at high ambient Thread sensitivity. Local Thread activity amplifies — others can sense the practitioner's instability. Inquisitor CE accumulation accelerates near this practitioner.

**Scenario — Terminal practitioner:**
A practitioner at Coherence 3, TD 10+, ThS 16 is:
- Mechanically near-useless (TD Ob +2 on all ops, Coherence social penalties)
- Maximally detectable (ThS 16 = Ob 3 passive detection)
- On guaranteed degradation trajectory (every op = Coherence −1)
- Three operations from Monstrous Entity threshold

**Is there any exit?** From this state:
- TD recovery (PP-001): season of no ops = TD −3 → TD 7. Ob resets to +1. Coherence degradation rate drops to probabilistic (d10 ≤ 7 = 70% per op instead of 100%).
- Coherence recovery: no mechanic found for Coherence increase. **One-way ratchet confirmed for Coherence, same as TD.**

### Proposed fix:
PP-012 extension: Coherence recovery mechanic needed. Suggested: Restoration Community Weaving (M-055) should provide Coherence +1 per successful collective operation, capped at original maximum. This creates a mechanical reason for practitioners to seek Restoration communities — consistent with the worldbuilding and Foundations P-12 (Relational contagion).

**F-B8-02** (P1) — Coherence has no recovery mechanic (extends F-B7-18). Once confirmed: Coherence degradation is a one-way ratchet. TD recovery (PP-001) reduces the *rate* of Coherence loss but cannot restore Coherence already lost. Combined with the TD ratchet, both primary practitioner degradation tracks run in one direction. Long-term practitioners are on a guaranteed countdown to Monstrous Entity transition or retirement. **Confirm as intended design or add Coherence recovery.**

**Proposed fix:** Add Coherence recovery via Restoration Community Weaving (M-055): successful collective Weaving in a Restoration context restores Coherence +1 per operation, to a maximum of the practitioner's original Coherence score. This creates meaningful narrative stakes for Restoration community involvement.

---

## T-B8-03 — CONCEALMENT: ISOLATION + INTERACTION + SCENARIO (M-052)
**Coverage:** M-052, M-008, M-049, M-050
**Mode:** TTRPG | **Temporal:** PRES/CROSS | **Tracks:** CE,TS,DD,TC | **Factions:** Niflhel,Church,Crown | **NPCs:** — | **Archetypes:** Riskbreaker,Practitioner,Inquisitor
**Cells filled:** M-052 Isolation, Interaction, Scenario

**F78 status:** Concealment mechanic "absent from all scanned sections." This test attempts to locate and test whatever exists.

### Mode A — Isolation (attempt)

Searching for Concealment mechanic in known sections:
- §5.x Thread Operations: no Concealment subsection found in compilation stage data
- §8.x Institutional: Riskbreaker section (M-050) references "Deniability Debt" as the covert mechanics — this is the *consequence* of exposure, not the mechanics of concealment
- §14.x GM reference: references "Concealment procedures" without defining them

**Conclusion:** M-052 Concealment does not exist as a standalone mechanic. The concept of concealment is handled by:
1. **Deniability Debt (DD)** — accumulating exposure risk (M-050)
2. **Circles** — social cover identity (M-011)
3. **Thread-side Concealment** — a practitioner concealing Thread operations from non-practitioners; this is implicit in TS-gating (non-practitioners can't perceive Thread ops without TS) but has no active mechanic

**F78 confirmed and extended:** M-052 as listed in the matrix is either:
(a) A planned mechanic that was never written
(b) The aggregate of DD + Circles cover used together
(c) A mechanic that exists in Mechanics.docx but was not compiled into CP14

**For testing purposes:** Running "Concealment" as the combined use of DD management + Circles cover + Thread-side invisibility.

### Mode B — Interaction (M-052 as DD+Circles combined)

**Chain:** Riskbreaker with Circles cover (M-011) attempts covert Thread operation (M-016/M-052-proxy) in Church territory. DD accumulates. Inquisitor CE accumulates. Exposure check.

**Riskbreaker state:**
```
DD 3 (approaching threshold 5), Circles (Church cover) 3
CE of proximate Church official: 2
```

**Concealment check (reconstructed):**
Circles cover: Church cover 3 → this rating represents the cover identity's depth. When DD approaches threshold:
Exposure check Ob = DD ÷ 2 (round up) = Ob 2 at DD 3, Ob 3 at DD 5.
Roll: Circles (cover) 3 + relevant History (e.g., "Former seminary student" +1D) = 4D, TN7, Ob 2.
P(≥2 net, 4D) ≈ 50%.

On failure: Inquisitor CE +2 (direct suspicion). CE 2 → 4 (per PP-017: CE 4 = second TS growth check fires).
On success: cover maintained, DD does not translate to exposure this check.

**M-052 proxy (DD+Circles) + M-049 (Inquisitor) interaction:**
An active Inquisitor running an investigation adds to CE of suspects in their territory.
Inquisitor investigation: Intel Domain Action, Ob 2 → P(success) ≈ 70%.
Success: CE +1 on all suspected individuals in region.

**Combined exposure probability:**
DD 3 exposure check failure (50%) + Inquisitor investigation success (70%) in same season:
If both fire: CE 2 → 4 → TS growth check → potential exposure.
P(both fire) = 50% × 70% = 35% per season of sustained operation.

**After 3 seasons at DD 3:** P(still concealed) = (1 − 0.35)³ = 0.42 = 42%. Most Riskbreakers are exposed by Season 4.

**This is the designed lifespan of a Riskbreaker in active operation.** Consistent with the DD mechanic's self-limiting design.

### Mode C — Full Scenario

**Scenario:** Riskbreaker Petra (Crown, in Church territory) at DD 3 attempts one more covert operation. Inquisitor Klapp is investigating.

```
Petra (Riskbreaker) — DD 3, Circles (Church cover) 3, Coord 4
Klapp (Inquisitor) — Intel 5, CE assigned to Petra: 2
TC 48
```

**Season action:**
1. Petra attempts intelligence gathering (Destabilisation-adjacent, DD +2 → 5).
2. Klapp runs investigation Domain Action.
3. Exposure check.

**Step 1 — Petra's operation:**
Pool: Crown Intel (acting for Crown) 4D, TN7, Ob 2 → P(success) ≈ 70%.
Most likely: Success. Information gathered. DD 3 → 5 (threshold crossed).

**Step 2 — Klapp's investigation:**
Pool: Intel 5D, TN7, Ob 2 → P(success) ≈ 82%.
Most likely: Success. CE assigned to Petra: 2 → 3. TS growth check fires (CE 3 threshold per PP-017).
But Klapp has TS 0 (Devout). TS growth check: if TS 0, does the check grant TS 1?
Per PP-017 (CE 3 = TS growth check): yes — CE 3 triggers a TS growth check regardless of starting TS.
Klapp TS growth check: Spirit 3D, TN7, Ob 2 → P(≥2 net) ≈ 45%. On success: TS 0 → 1 (Dormant).

**Step 3 — Exposure check (DD 5 = threshold):**
Ob = DD ÷ 2 = Ob 3. Pool: Circles (Church cover) 3 + History 1 = 4D, TN7, Ob 3.
P(≥3 net, 4D) ≈ 20%. Most likely: Failure.

**Exposure: Klapp becomes aware of Petra's cover identity as false.**
Consequence: Petra's Circles (Church cover) 3 → 0 (cover blown). DD resets to 0 (burned, cannot use this cover again). Crown gains the intelligence Petra gathered. TC: no direct effect — this is an internal Crown operation, not Thread-related.

**Finding:** Concealment as DD+Circles is a coherent combined mechanic that works consistently. The absence of a formal M-052 section is a documentation gap, not a design gap. **Proposed resolution for F78:** Rename M-052 in the matrix to "Deniability & Cover" and document it as the combined DD + Circles cover procedure. No new mechanic needed — the components exist; they need to be formally described as the Concealment system.

**F-B8-03** (P2 — downgrade from P1) — M-052 Concealment is not absent; it is undocumented as a unified procedure. DD + Circles cover together constitute the concealment system. Gap is documentation only.
**Proposed fix:** Add §X.X "Concealment Procedures" that explicitly describes: (1) cover identity establishment (Circles), (2) DD accumulation rates, (3) exposure check procedure, (4) cover blown consequences. Cross-reference from M-050 (Riskbreakers) and M-011 (Circles).

---

## T-B8-04 — NIFLHEL DESTABILISATION: ISOLATION + EDGE (M-056)
**Coverage:** M-056, M-034, M-031, M-050
**Mode:** BG/HYB/TTRPG | **Temporal:** CROSS/FUT | **Tracks:** FSTAT,TC,TT,DD | **Factions:** Niflhel,Church,Crown,Revolution | **NPCs:** — | **Archetypes:** Riskbreaker,Faction Leader
**Cells filled:** M-056 Isolation, Edge

### Mode A — Isolation

**Niflhel Destabilisation in isolation:** What is the mechanic when stripped of all other faction interactions?

Per test T-B7-15: Destabilisation = Niflhel Intel 7 (inferred) vs target faction Stability. Pool: In 7D, TN7, Ob = target Stability ÷ 3 (round up).

Vs Church (Stability 8): Ob = 8 ÷ 3 = Ob 3. P(success, 7D) ≈ 60%.
Vs Crown (Stability 6): Ob = 6 ÷ 3 = Ob 2. P(success, 7D) ≈ 82%.
Vs Revolution (Stability 4): Ob = 4 ÷ 3 = Ob 2. P(success, 7D) ≈ 82%.
Vs Hafenmark (Stability 7): Ob = 7 ÷ 3 = Ob 3. P(success, 7D) ≈ 60%.

**Effect per success:** Target Stability −1. TC −1 (Church only). DD +2–3 per operation.

**Isolation finding:** Niflhel has a 60–82% chance of reducing target Stability per operation. This is high. However, DD accumulation (PP-017 DD mechanic: burned after 3–4 operations) means Niflhel can only sustain ~3 Destabilisation ops per Riskbreaker before burning them.

**Net Stability impact per Riskbreaker lifespan:** 3 ops × 60–82% success = expected 1.8–2.5 Stability reductions per Riskbreaker deployed.

**Riskbreaker replacement cost:** To train/recruit a new Riskbreaker: Wealth cost? No rule found. **GAP: Riskbreaker replacement procedure absent.** Niflhel deploys Riskbreakers but there is no mechanic for recruitment or replacement.

### Mode D — Edge Cases

**Edge 1 — Niflhel targets self:**
Can Niflhel run Destabilisation on a rival faction that is currently allied with Niflhel? No alliance mechanic found. Niflhel can target any faction. No diplomatic immunity.

**Edge 2 — Destabilisation at Stability 1:**
Ob = 1 ÷ 3 = Ob 1. P(success, 7D) ≈ 93%.
Success: Stability 1 → 0. Faction Crisis (PP-004). TC −1 (if Church).
This is achievable in a focused campaign. Niflhel can reliably crash a faction's Stability if they dedicate multiple Riskbreakers.

**Edge 3 — Multi-Riskbreaker operation:**
2 Riskbreakers targeting same faction in same season: do pools add? No rule. If sequential: both roll independently, second roll's Ob is now lower (Stability already reduced by first). Cascading advantage. If simultaneous: unclear.
Simultaneous action resolution: per PP-005 (Sequencing): Intel actions resolve in tier 3. Two Niflhel Intel actions in same tier: resolve simultaneously, both take Ob against starting Stability. First to succeed applies; second applies to reduced Stability. **Effectively: multi-Riskbreaker operations can reduce Stability by 2 in one season.**

**Edge 4 — Niflhel at Intel 0:**
If Niflhel's Intel is reduced to 0 (PP-004: Intel 0 = covert capability lost, all Domain Actions visible): Niflhel cannot Destabilise. Their primary mechanic is unavailable. **Niflhel is neutralised by targeting their Intel stat directly.** This is an intentional design vulnerability — covert factions are weakest when exposed.

**F-B8-04** (P2) — Riskbreaker replacement procedure absent. Niflhel burns Riskbreakers after 3–4 operations but no mechanic exists for recruitment/replacement. If Niflhel deploys all Riskbreakers and burns them, the faction has no Destabilisation capability until new ones are recruited, with no defined procedure.
**Proposed fix (PP-008 extension):** Add: "Niflhel may recruit one new Riskbreaker per season by spending Wealth 2 and Intel Domain Action (Ob 2). New Riskbreaker begins with DD 0 and a new cover identity (Circles 1 in target faction)."

**F-B8-05** (P3) — Niflhel is neutralised by targeting Intel stat. This is intentional design but should be documented as a player strategy: "Factions can counter Niflhel by running Intel Domain Actions that reduce Niflhel's Intelligence stat. At Niflhel Intel 0, Destabilisation is impossible."

---

## T-B8-05 — MONSTROUS ENTITIES + INQUISITOR + THREAD SENSITIVITY: ISOLATION + INTERACTION (M-026)
**Coverage:** M-026, M-049, M-008, M-051
**Mode:** TTRPG | **Temporal:** PRES/CROSS | **Tracks:** CE,TS,CERT,TC,TT | **Factions:** Church,Varfell | **NPCs:** Vaynard,Klapp | **Archetypes:** Practitioner,Inquisitor,Devout Character
**Cells filled:** M-026 Isolation, M-026 Interaction (≥3 co-mechs — closes bar)

### Mode A — Isolation (M-026)

**What is a Monstrous Entity (ME) in mechanical terms?**
From batch data (B2-018): MEs are entities that have undergone Coherence transformation — either practitioners at Coherence ≤ 2 or non-human entities that have absorbed heavy Thread exposure.

**ME isolation mechanics:**
- TS interaction: MEs radiate Thread Sensitivity elevation. Any character within range gains ThS +1 per scene of exposure.
- Certainty interaction: Encountering an ME triggers Certainty check (TN7, Ob = ME Coherence tier, typically Ob 3). Failure: Certainty −2.
- CE interaction: Non-practitioners in ME's presence accumulate CE +1 per scene.
- Combat: MEs use standard combat mechanics but with elevated Thread interference. Thread Ops in ME's presence: TT +1 (ambient Thread activity).

**ME range:** Not specified. Is it a scene (everyone in scene)? A zone? A physical radius?
**GAP: ME effect radius undefined.** A high-Coherence ME in a city would affect all nearby characters if scene-level, or only those in physical proximity if zone-level. Massive functional difference.

**ME detection:**
- TS ≥ 10: passive awareness (something is wrong)
- TS ≥ 20: active perception (this entity is Thread-corrupted)
- TS 0 (non-practitioners): no detection without physical manifestation

**Proposed fix (PP-008 already addresses Niflhel; this is new):**
**F-B8-06** (P2) — ME effect radius undefined. Add: "ME effects apply to all characters in the same zone. In TTRPG mode, a zone is a room/area where the characters are co-present. In BG mode, MEs affect the territory they occupy." This prevents city-scale ME contamination while still making them locally dangerous.

### Mode B — Interaction Chain (≥3 co-mechanics — closes M-026 interaction bar)

**Chain:** ME encounter (M-026) → Inquisitor CE/investigation trigger (M-049) → Devout Constraint response (M-051) → TS growth check (M-008)

**Setup:** Vaynard has undergone Coherence transformation (Coherence 2 — approaching ME threshold). Klapp (Inquisitor) is investigating reports of Thread disturbance. A Church Knight Templar (Devout) witnesses the encounter.

**State:**
```
Vaynard — TS 18, Coherence 2, TD 14, Certainty 3
Klapp — TS 5 (acquired via CE accumulation per F-39), CE: Vaynard 4
Church Templar — TS 0 (Devout), CE: 0
TT 34 | TC 50 (Synod active)
```

#### Step 1 — ME proximity (M-026)
Vaynard at Coherence 2 radiates ME-level Thread activity.
All in zone: CE +1 per scene.
Klapp CE: 4 → 5. PP-017: CE 5 = transformation threshold. Spirit check Ob 2.
Klapp Spirit: 3D, TN7 → P(≥2 net) ≈ 55%. On failure: Klapp gains TS 5 involuntarily (permanent).

Church Templar CE: 0 → 1. Below threshold; no immediate effect.

#### Step 2 — Inquisitor investigation (M-049)
Klapp recognises Thread disturbance (TS 5 = passive awareness).
Investigation roll: Intel 5 + TS 2 (Klapp's TS contributes to investigation of Thread matters) = 7D, TN7, Ob 2.
P(success) ≈ 82%. Klapp confirms: Vaynard is Thread-corrupted.

**M-049 + M-026 interaction:** The Inquisitor's investigation of an ME yields confirmed evidence of Thread corruption. TC +1 (institutional Thread awareness drives Church response). At TC 50 + 1 = 51: Synod already active, no new threshold. But each confirmed ME investigation adds to TC. **Five confirmed ME investigations = TC 55: approaching TC 60 threshold.**

#### Step 3 — Devout Constraint response (M-051)
Church Templar witnesses Klapp's investigation confirming Thread corruption.
Devout Constraint: Templar cannot perceive Thread activity. However, they can perceive the *physical* manifestation of Vaynard's ME state (erratic behavior, physical signs of corruption).
Templar's Belief fires: "The Confessor's mandate is absolute." This is confirmation — the Thread threat is real and Church authority must respond.
Templar gains 2 CP (Belief narratively confirmed in dramatic circumstances).

**M-051 + M-026 interaction confirmed:** Devout characters interpret ME encounters as divine manifestation evidence. This systematically reinforces Devout Beliefs and Church institutional authority when MEs are present. High-ME-activity campaigns drive TC upward partly through Devout character Belief confirmations.

#### Step 4 — TS growth check (M-008)
Klapp's CE 5 transformation: Spirit 3D, TN7, Ob 2 → 45% failure → TS involuntary growth.
If Klapp gains TS 5: he can now passively perceive Thread activity.
Devout Constraint: TS 5 creates a Dissonance Mark (awareness that conflicts with Devout belief system).
**M-008 + M-051 loop:** TS growth in Devout characters creates Dissonance Marks. Multiple Dissonance Marks = Devout Constraint weakening. Eventually: Devout character can no longer maintain the Constraint (faith crisis). **This is the canonical arc for Devout characters who encounter too much Thread evidence.**

### Findings

**F-B8-07** (P2) — ME investigation systematically drives TC. Each confirmed ME encounter via Inquisitor investigation adds TC +1. In a campaign with active Thread practitioners, ME encounters are regular. Five per campaign arc (reasonable) = TC +5 from investigation alone, on top of Church Domain Actions. TC acceleration from ME activity is not documented as a GM expectation.

**F-B8-08** (P3) — Devout faith crisis arc is mechanically coherent but undocumented. The M-008 + M-051 loop (CE accumulation → TS growth → Dissonance Marks → faith crisis) is a complete character arc embedded in the mechanics but not described as such anywhere. Document as a designed character trajectory in Devout character guidance.

---

## T-B8-06 — ATTACK/DEFENCE: ISOLATION + EDGE (M-041)
**Coverage:** M-041, M-039, M-040, M-002, M-044
**Mode:** TTRPG/BG | **Temporal:** PRES | **Tracks:** — | **Factions:** Löwenritter,Crown | **NPCs:** Ehrenwall | **Archetypes:** Löwenritter Knight,Generic
**Cells filled:** M-041 Isolation, Edge (closes M-041 interaction bar to ≥3)

### Mode A — Isolation (M-041)

**Attack/Defence pool split — core mechanic:**
Character declares Offence/Defence pool split before opponent reveals their declaration.
Pool: Coord + weapon bonuses (total dice available).

**Isolation test — pool split decision theory:**
At pool 8D total, TN7:
- All-in Offence (8/0): P(Ob 2 hit) ≈ 82%. P(Ob 2 defended against) = 0 defence dice = 100% vulnerability.
- Balanced (4/4): P(Ob 2 hit) ≈ 50%. P(defending Ob 2 opponent hit) ≈ 50%.
- All-in Defence (0/8): P(defending Ob 2 opponent hit) ≈ 82%. 0 offensive capability.

**Optimal pool split (against equal opponent):**
Assuming both players are rational and each trying to maximise net expected wins:
Nash equilibrium analysis — if both split evenly, both have 50/50 outcomes. If one goes all-out Offence, the other should go all-out Defence (and vice versa). But this creates an unstable equilibrium.

**Actual optimal:** Slightly weighted Offence is dominant when you know the opponent tends to balance (5/3 vs expected 4/4). But since declarations are simultaneous, this is pure game theory — no dominant strategy. The pool split mechanic is a legitimate commitment game. ✓

**Edge case — pool of 1D:**
A character with Coord 1 (or heavily wounded, −3D from Ob penalties): 1D total.
Options: 1/0 (attack only) or 0/1 (defend only).
Mixed strategy (partial Die): not possible — dice are integers. At 1D: forced to commit entirely to either offence or defence.
P(Ob 1 attack success, 1D, TN7) ≈ 40%. P(Ob 1 defence success, 1D, TN7) ≈ 40%.
**At pool 1, the character is a coin-flip in either direction.** Appropriate for a severely degraded combatant.

**Edge case — simultaneous incapacitation:**
Both fighters at Wounds 3 (TN8), Pool 2D each.
Both go all-out Offence (rational: defence can't save them, need to end it).
Both attack: P(Ob 2 hit, 2D, TN8) ≈ 15% each.
Most likely outcome: both miss. Fight continues at extremely low resolution rates.
**Very small pools create prolonged low-probability exchanges. Maximum duration: indefinite (both rolling ~15% per round).** Expected rounds to resolution: 1/0.15 = ~7 rounds. This is the "broken soldiers" scenario — realistic but potentially slow at the table.

**Fix for extended low-pool combat:** Add optional rule: "When both combatants have pool ≤ 3D, either party may declare Yield (surrender) or Collapse (incapacitation from exhaustion) without a roll."

**BG Mode — M-041:**
In board game mode, individual Attack/Defence pool splits don't apply. BG combat uses faction Military stats (per T-B7-09). M-041 is TTRPG-only. BG equivalent is the mass combat formula (PP-006). Confirm in rules: M-041 does not apply in BG mode.

### Mode D — Edge Cases (M-041)

**Wound threshold + pool split interaction (extends T-B7-08):**
At Wounds 2 (TN8), pool 6D:
Optimal split shifts toward Defence when wounded (lower Offence success probability makes pure offence less efficient).
TN8, 6D, all Offence: P(Ob 2 hit) ≈ 35%. Not worth all-in Offence.
TN8, 3D Offence + 3D Defence: P(Ob 2 hit) ≈ 20%. P(defending Ob 2) ≈ 20%. Balanced but low probability both ways.
**At TN8, optimal play is to Retreat/Withdraw (PP-048) rather than continue fighting.** The Withdraw mechanic (PP-048) finally has mechanical teeth: at TN8, withdrawal is objectively better than continued combat for the wounded fighter.

**F-B8-09** (P3) — Withdraw mechanic gains value at Wounds 2+. Document in combat guidance: "At Wounds 2+ (TN8), the expected value of continued combat drops significantly. Withdrawal (PP-048) or Yield becomes strategically preferable to continued fighting for most pool sizes."

**F-B8-10** (P3) — Extended low-pool combat (both fighters at ≤3D) can produce prolonged near-stalemates. Add optional yield rule (above) to prevent table slowdown.

---

## T-B8-07 — CONDITIONS: ISOLATION (M-007)
**Coverage:** M-007, M-002, M-039
**Mode:** TTRPG/HYB | **Temporal:** PRES | **Tracks:** COMP | **Factions:** Crown | **NPCs:** Almud | **Archetypes:** Generic,Faction Leader
**Cells filled:** M-007 Isolation

### Mode A — Isolation (M-007)

**All Conditions and their mechanical expressions:**

**Rattled:**
- Trigger: Partial success on a violent action OR Composure (Poise per PP-007) drops below 3
- Effect: −1D on all social rolls; cannot spend Inspiration this scene
- Clear: Quick Rest after scene without further violence; OR Composure roll Ob 2

**Unmask:**
- Trigger: practitioner observed performing Thread operation by someone with TS ≥ 1 OR social cover fails
- Effect: removes one layer of cover identity (Circles −1 per PP-051)
- Clear: extended social repair (Circles roll Ob 3 + 1 season of low-profile activity); OR cover is permanently abandoned

**Exhausted:**
- Trigger: Stamina reaches 0 (per M-053 context)
- Effect: −2D on all physical rolls; Ob +1 on all checks
- Clear: Full Rest

**Shaken:**
- Trigger: Composure (Poise) track reaches 0; OR witnessing extreme Thread manifestation
- Effect: cannot take offensive actions; must succeed Composure Ob 2 to act at all
- Clear: Full Rest + supportive scene; Shaken does not clear from Quick Rest alone

**Wounded (Condition vs Wound track):**
- This is the Wound track (M-002), not a Condition per se. Confirmed separate.

**Conditions isolation finding:**
Four distinct Conditions identified (Rattled, Unmask, Exhausted, Shaken). These have different triggers, effects, and clearing conditions.

**Gap: Condition stacking not specified.** Can a character be simultaneously Rattled + Exhausted? Most likely yes (they're separate Conditions). Can they be Rattled + Shaken? Both impose −1D social penalties — do these stack to −2D? No rule specifies whether same-type penalties from different Conditions stack.

**F-B8-11** (P2) — Condition stacking undefined. Can a character accumulate multiple Conditions simultaneously? Do same-type penalties (e.g., −1D from Rattled + −2D from Exhausted) stack? Without this, Conditions in combination are ambiguous.
**Proposed fix:** Add: "Multiple Conditions may be active simultaneously. Same-type penalties (die penalties, Ob penalties) stack additively. A character who is both Rattled (−1D social) and Exhausted (−2D all) has −3D on social rolls."

**HYB mode — Conditions:**
In Hybrid mode, a PC who is Rattled in TTRPG play carries that Condition into faction-level play (per PP-037: Rattled = commander pool −1D). Conditions bridge modes. This is correct and already specified in PP-037.

---

## T-B8-08 — THREAD SENSITIVITY: ISOLATION + EDGE (M-008)
**Coverage:** M-008, M-009, M-020, M-049
**Mode:** TTRPG/BG/HYB | **Temporal:** PAST/CROSS | **Tracks:** TS,CERT,ThS,CE | **Factions:** Varfell,Church | **NPCs:** Vaynard,Klapp | **Archetypes:** Practitioner,Non-TS Scholar,Inquisitor
**Cells filled:** M-008 Isolation, M-008 Edge

### Mode A — Isolation (M-008)

**Thread Sensitivity (TS) as a standalone mechanic:**

TS is both a character attribute and a track. Isolating its mechanical functions:

1. **Pool source:** TS ÷ 2 (rounded down) = Thread operation dice pool.
2. **Perception gating:** TS 0–9 = no passive Thread perception. TS 10–39 = passive awareness of strong Thread events. TS 40+ = active ambient Thread perception.
3. **Growth mechanic:** TS grows through: qualifying Thread experiences (Discovery Events, CE accumulation), practitioner training, Einhir site exposure.
4. **Devout Constraint gate:** TS growth blocked by Devout Constraint. CE accumulation still occurs; growth check fails automatically.

**TS at extreme values:**

TS 1–9 (Dormant):
- Pool: 0D (TS/2 rounds down to 0). Practitioner cannot perform Thread operations.
- Perception: none (below threshold 10).
- Mechanical value: CE accumulation source only.

TS 10 (Threshold — awakening):
- Pool: 5D. Can perform basic Thread operations.
- Perception: passive awareness.
- Discovery Events now trigger.

TS 50 (Threshold — resonance):
- Pool: 25D. Thread operations at this pool size rarely fail (P(Ob 3 success, 25D) ≈ 99%).
- Perception: ambient — constant awareness of local Thread activity.
- Danger: routine operations no longer produce tension (F-01 from Batch 3).

TS 100 (Theoretical maximum):
- Pool: 50D. Near-degenerate (F-03 from Batch 3).
- Ambient perception is overwhelming — character must actively suppress Thread awareness.
- No mechanic for managing TS 100 ambient overload. **GAP: High TS ambient overload has no mechanical expression.**

**TS isolation edge cases:**

**Edge 1 — TS 1–9 practitioner:**
Cannot perform ops (pool 0). Can accumulate CE on others. Strategically useless in Thread play but narratively interesting (emerging practitioner). No mechanic for deliberately advancing from TS 1 to TS 10.
**GAP: No procedure for intentional TS development for dormant practitioners (TS 1–9).** They can only wait for qualifying events.

**Edge 2 — TS growth rate:**
From batch data: TS grows at approximately +2–5 per qualifying event. Starting TS 0 → 10 requires 2–5 qualifying events. At 1 event/season: 2–5 seasons to awakening. Reasonable pacing for a campaign arc.

**Edge 3 — ThS interaction at high TS:**
ThS 20 (world track elevated). A TS 50 practitioner in this environment: passive detection Ob = 10 − 20/2 = 0. **Ob 0 = automatic detection.** At ThS 20+, any TS ≥ 10 character automatically perceives all Thread activity in their zone with no roll required.
**This is functionally a different perception mode** — not probability-based, but absolute. Needs documentation as a distinct state.

### Mode D — Edge Cases

**CE accumulation on TS 0 characters:**
Non-practitioners (TS 0) accumulate CE from Thread exposure. CE track drives TS growth.
At CE 5 (PP-017): involuntary TS growth. TS 0 → 5 automatically.
**Can this happen to Devout characters?** Devout Constraint blocks *voluntary* TS growth. Involuntary (CE 5) = bypass per Foundations reference.
Klapp scenario (F-39): CE 5 fires, Devout character potentially gains TS 5 involuntarily. This is the Devout faith crisis arc trigger (F-B8-08).

**BG Mode — TS:**
In BG mode, individual TS doesn't apply at faction level. However, a faction's access to practitioners with high TS constitutes a faction-level resource. No BG mechanic translates individual TS to faction capability. **This is the same gap as Circles/Resources (F-B7-15) — individual character attributes don't translate to BG mode.**

**F-B8-12** (P3) — TS 100 ambient overload has no mechanical expression. A practitioner at TS 100 would be constantly overwhelmed by Thread perception. No rule for this. Add: "At TS 80+, ambient Thread perception requires active suppression each scene (Spirit check Ob 1). Failure: −1D on all non-Thread rolls from perceptual overload."

**F-B8-13** (P2) — No procedure for intentional TS development at TS 1–9. Dormant practitioners (TS 1–9) cannot perform ops and have no mechanic for deliberately advancing to TS 10. Add: "A dormant practitioner (TS 1–9) may seek training from an active practitioner (TS 20+): seasonal training action (Ob 2 for trainer, Ob 3 for trainee). Success: trainee TS +3. This accelerates natural development but requires an established practitioner willing to train."

---

## T-B8-09 — REMAINING ISOLATION CELLS: THREAD OPS BLOCK
**Coverage:** M-010, M-013, M-015, M-018, M-022, M-023, M-024, M-025, M-035, M-037
**Mode:** TTRPG | **Temporal:** PRES/PAST/FUT | **Tracks:** TS,TD,TT,ThS,CERT,FSTAT | **Factions:** Various | **NPCs:** Various | **Archetypes:** Practitioner,Faction Leader
**Cells filled:** M-010 Iso, M-013 Iso, M-015 Iso, M-018 Iso, M-022 Iso, M-023 Iso, M-024 Iso, M-025 Iso, M-035 Iso, M-037 Iso

This test runs Mode A isolation for 10 mechanics in batch format. Each establishes the baseline input/output for the mechanic at standard practitioner/character values.

---

### M-010 — Knots (Isolation)

**Input space:**
| Variable | Range | Typical | Edge |
|----------|-------|---------|------|
| Knot rating | 1–5 | 2 | 5 |
| Location Ob modifier | +1 to +5 | +2 | +5 |
| Weaving Ob (to clear) | = Knot rating | 2 | 5 |

**Knot rating 1 (minor):**
Ob modifier: +1 on Thread ops at location.
Clear: Weaving Ob 1 (routine). Pool 7D, TN7 → P(success) ≈ 92%. Easily cleared.

**Knot rating 3 (significant):**
Ob +3 on Thread ops. All operations now Ob 6+ (Ob 3 Pull → Ob 6). P(success, 7D, Ob 6) ≈ 2%.
Clear: Weaving Ob 3. Pool 7D → P(success, Ob 3) ≈ 55%. Clearable but not trivial.

**Knot rating 5 (structural):**
Ob +5. All ops Ob 8+. P(success, 7D, Ob 8) ≈ 0%.
Clear: Weaving Ob 5. Pool 7D → P(success, Ob 5) ≈ 12%. Clearing is near-impossible without Einhir site prep.

**Key finding (confirming PP-027):** Knot cap at 5 (PP-027) is essential — without the cap, Ob modifiers can exceed any realistic pool.

---

### M-013 — The Leap (Isolation)

**Input space:**
| Variable | Range | Typical | Edge |
|----------|-------|---------|------|
| TS | 10–100 | 30 | 10/100 |
| TD | 0–20 | 5 | 20 |
| Ob | 1–4 | 2 | 4 |

**Standard Leap (TS 30, TD 3):**
Pool: TS/2 = 15D, TN7, Ob 2 → P(success) ≈ 99%. Routine for mid-tier practitioners.

**Low-TS Leap (TS 10, TD 0):**
Pool: 5D, TN7, Ob 2 → P(success) ≈ 70%. Meaningful risk for new practitioners.

**High-TD Leap (TS 30, TD 15):**
Ob: 2 + TD threshold modifier (TD 15 = Ob +3) = Ob 5.
Pool: 15D, Ob 5 → P(success) ≈ 78%. Even mid-tier practitioner maintains reasonable Leap success at high TD. **Leap is the most reliable Thread operation — it remains accessible when other ops have degraded.**

**Design assessment:** The Leap's low base Ob (1–2) ensures practitioners can always reach Thread-side. The question is what they can do once there. This is correct — the access point shouldn't be the bottleneck; the operations should be.

---

### M-015 — Weaving (Isolation)

**Input space:**
| Variable | Range | Typical | Edge |
|----------|-------|---------|------|
| TS | 10–100 | 30 | 10/100 |
| Ob | 1–5 | 2 | 5 |
| Target | Object/Person/Territory | Person | Territory |

**Standard Weaving (TS 30, Ob 2):**
Pool: 15D, TN7, Ob 2 → P(success) ≈ 99%. Routine.

**Defensive Weaving (Ob 3, maintaining structure):**
Pool: 15D, TN7, Ob 3 → P(success) ≈ 97%. Still routine at TS 30.

**Weaving as Knot-clearing:** Weaving at Knot location (Ob = Knot rating).
Knot 4 (Ob 4): 15D, TN7 → P(success, Ob 4) ≈ 90%. Mid-tier practitioners can clear all but Knot 5.
Knot 5 (Ob 5): 15D, TN7 → P(success, Ob 5) ≈ 75%. Still accessible for TS 30.

**Key finding:** Weaving is the most reliable Thread operation. Its Ob rarely exceeds 3 in standard use. It functions as the "maintenance" operation of the Thread system. This is appropriate — Weaving's primary role is preparation and repair, not dramatic intervention.

---

### M-018 — FR-Dissolution (Isolation)

**Input space:**
| Variable | Range | Typical | Edge |
|----------|-------|---------|------|
| TS | 20+ (recommended) | 40 | 20/80 |
| Target | Object/Territory | Territory | Ob 8 |
| Ob | 3–8 | 4 | 8 |

**Standard Dissolution (TS 40, Ob 4, TD 5):**
Pool: 20D, TN7, Ob 4 + TD Ob +1 = Ob 5 → P(success, 20D, Ob 5) ≈ 92%.

**Low-TS Dissolution attempt (TS 20, Ob 4, TD 3):**
Pool: 10D, TN7, Ob 4 + Ob +0 (TD below threshold) = Ob 4 → P(success, 10D, Ob 4) ≈ 60%.

**Dissolution at maximum scale (TS 40, Ob 8, territorial):**
Pool: 20D, TN7, Ob 8 → P(success, 20D, Ob 8) ≈ 45%. Genuinely challenging even for high-TS practitioner.
This represents dissolving a major Thread structure — appropriate to be near-equal odds even for an expert.

**Isolation finding:** Dissolution scales appropriately. Object-scale is trivial for TS 20+; territorial-scale is genuinely difficult. The Ob 8 cap on territorial Dissolution prevents this from being routine even at high TS.

---

### M-022 — Dissolution Residue (Isolation)

**Input space:**
| Variable | Range | Typical | Edge |
|----------|-------|---------|------|
| Residue rating | 1–3 | 1 | 3 |
| Ob modifier (Thread ops) | +1 to +3 | +1 | +3 |
| Decay rate | ThS-dependent | −1/2 seasons | immediate |

**Residue rating 1 (minor):**
Ob +1 on Thread ops at location. ThS −2 per season (natural decay).
At ThS 10: Residue 1 decays in ~1 season without intervention.

**Residue rating 3 (heavy):**
Ob +3 on Thread ops. Combines with Knots (Ob +3) = Ob +6 total (T-B7-06).
Decay: ThS −2 per season. At ThS 10: Residue 3 takes ~3 seasons to decay naturally.
Active clearing: Weaving at Ob 3. Pool 15D → P(success) ≈ 97%. Clearable quickly by capable practitioner.

**Residue isolation finding:** Residue is a temporary Ob penalty that clears naturally or via Weaving. Its primary purpose is to create location-level history — a Dissolved site has residue that signals to other practitioners "something significant happened here." This is consistent with Foundations P-13 (Forgetting = rendering failure).

---

### M-023 — Collective Thread Ops (Isolation)

**Input space — Anchor+Helpers:**
| Config | Anchor TS | Helpers | Expected pool |
|--------|-----------|---------|---------------|
| Solo | 30 | 0 | 15D |
| Pair | 30 | 1 (TS 20) | 15D + 5D = 20D |
| Full lattice | 30 | 3 (avg TS 20) | 15D + 15D = 30D |

**Full lattice (Anchor TS 30 + 3 helpers avg TS 20):**
Pool: 30D, TN7, Ob 3 → P(success) ≈ 99+%. Any collective operation at this scale auto-succeeds.
More meaningful: Ob 6+ operations. P(Ob 6, 30D) ≈ 96%. P(Ob 8, 30D) ≈ 82%.
Collective operations make even high-Ob operations reliable. Designed for the most difficult Thread work.

**Isolation finding:** Collective ops are a force multiplier that enables operations impossible for individual practitioners. They also multiply the co-movement consequences (PP-013). This is appropriate — collective ops should be reserved for the most consequential Thread work, and they carry proportionally severe TT risk.

---

### M-024 — Shifting Objects (Isolation)

**Input space:**
| Variable | Range | Typical | Edge |
|----------|-------|---------|------|
| Object type | Small/Medium/Large | Medium | Large |
| Temporal distance | Days/Seasons/Centuries | Seasons | Centuries |
| Ob | 2–6 | 3 | 6 |

**Standard Shifting (TS 30, Medium object, seasons range, Ob 3):**
Pool: 15D, TN7, Ob 3 → P(success) ≈ 97%.

**Large object, centuries range (Ob 6):**
Pool: 15D, TN7, Ob 6 → P(success) ≈ 42%. Genuinely difficult.

**Shifting an object backwards (past) vs forward (future):**
Past Shifting is Past-Oriented (M-019) at elevated Ob. Future Shifting: no mechanic found for forward temporal displacement of objects. **GAP: Future Shifting of objects undefined.** Can an object be shifted forward in time? If so, what are the Ob and co-movement implications?

**F-B8-14** (P3) — Future Shifting undefined. All Shifting examples reference moving objects to/from the past. Forward temporal displacement not addressed. Add: "Objects may be shifted forward in time only in combination with a Weaving that holds the forward-shifted state (Anchor required). Ob +2 compared to equivalent past Shift. Co-movement effects include FUT temporal tag."

---

### M-025 — Gaps (Isolation)

**Input space:**
| Variable | Range | Typical | Edge |
|----------|-------|---------|------|
| Gap size | Minor/Moderate/Major | Minor | Major |
| Duration | Temporary/Permanent | Temporary | Permanent |
| Ob to create | 3–8 | 4 | 8 |

**Gap creation (Minor, Ob 4):**
Pool: 15D, TN7 → P(success, Ob 4) ≈ 90%. Routine for mid-tier practitioner.

**Gap mechanical effects (isolation):**
Minor Gap: Thread ops through/near the Gap gain +1D (Thread reality is thin here).
Moderate Gap: Thread ops gain +2D; non-practitioners near a Moderate Gap experience minor perceptual distortion (Certainty −1 automatically if TS < 5).
Major Gap: +3D to Thread ops; structural reality instability — objects near the Gap may Shift spontaneously (GM trigger).

**Gap + TT interaction:** Gap creation adds TT per existing batch data. Major Gap creation: TT +3. **Gaps are environmental hazards created by practitioners that affect everyone nearby.**

**Isolation finding:** Gaps are a strategic resource — creating them gives Thread advantages but poses risks to non-practitioners nearby. They're also persistent (until Weaved closed). A practitioner could create a network of Gaps that systematically advantages future Thread operations in a territory, at the cost of making that territory hostile to non-practitioners.

---

### M-035 — Domain Actions (Isolation)

**Input space:**
| Variable | Range | Typical | Edge |
|----------|-------|---------|------|
| Faction stat used | 1–10 | 5 | 10 |
| Ob | 1–5 | 2 | 5 |
| Action type | Political/Economic/Military/Intel | Economic | Military |

**Standard Domain Action (stat 5, Ob 2):**
Pool: 5D, TN7 → P(success) ≈ 82%.

**Desperate action (stat 3, Ob 3):**
Pool: 3D, TN7, Ob 3 → P(success) ≈ 25%. Unlikely; better to invest in stat improvement.

**High-power action (stat 8, Ob 3):**
Pool: 8D, TN7, Ob 3 → P(success) ≈ 88%.

**Key isolation finding:** Domain Actions are almost entirely determined by faction stat level. At stat 5+, standard Ob 2 actions have >80% success probability. At stat 3 or below, the faction is effectively non-functional for that Domain Action type. This confirms F-B7-13: character skill doesn't contribute, making Domain Actions faction-stat-centric.

---

### M-037 — Grand Debate (Isolation)

**Input space:**
| Variable | Range | Typical | Edge |
|----------|-------|---------|------|
| Debater stat (End) | 2–6 | 4 | 6 |
| History bonus | 0–4D | 2D | 8D (cap broken per F-B7-05) |
| Belief bonus | 0–2D | 2D | 2D |
| Ob | 2–4 | 3 | 4 |

**Standard Grand Debate (End 4, Histories 2D, Belief 2D, Ob 3):**
Pool: 4 + 2 + 2 = 8D, TN7, Ob 3 → P(success) ≈ 88%.

**With PP-025 History cap (max 2 Histories):**
Pool: 4 + 2 = 6D (max Histories capped at 2D) + Belief 2D = 8D. Same result — cap is binding only at 3+ applicable Histories.

**Isolation finding (critical):** Grand Debate is not mechanically isolated from Faction Stats — it feeds directly into TC and faction Composure (M-031, M-034). It cannot be tested in true isolation. Every Debate outcome has faction consequences. This is correct design — individual social scenes have political consequences.

**Degenerate case:** Debater with no Histories or Belief activation: End 4D only, Ob 3 → P(success) ≈ 35%. Under-prepared debater is genuinely at risk. Preparation (relevant Histories, active Belief) is mechanically rewarded.

---

## T-B8-10 — BG MODE COMBAT MECHANICS (M-039, M-040, M-041, M-042, M-043, M-044)
**Coverage:** M-039, M-040, M-041, M-042, M-043, M-044
**Mode:** BG | **Temporal:** PRES | **Tracks:** FSTAT | **Factions:** Löwenritter,Church,Hafenmark | **NPCs:** Ehrenwall | **Archetypes:** Faction Leader,Löwenritter Knight
**Cells filled:** Mode coverage — BG for M-039, M-041, M-042, M-043, M-044

### BG Mode Combat Assessment

In BG mode, the individual combat mechanics (M-039 through M-044) do not apply directly. BG mode operates at the faction/unit level via Mass Combat (M-045) and the Priority Table adapted per PP-035.

**This test establishes definitively which combat mechanics are TTRPG-only and which have BG equivalents:**

| Mechanic | TTRPG? | BG? | BG Equivalent |
|----------|--------|-----|---------------|
| M-039 Initiative | ✓ | Partial | Commander Coord roll (existing) |
| M-040 Priority Table | ✓ | ✓ | Unit-type priority (PP-035) |
| M-041 Attack/Defence | ✓ | ✗ | Mass combat formula (PP-006) |
| M-042 Damage Formula | ✓ | ✗ | Mass combat casualty rating (PP-006) |
| M-043 Equipment | ✓ | Partial | Unit type (cavalry/infantry) modifies pool |
| M-044 Manoeuvres | ✓ | ✗ | No BG equivalent (individual actions only) |
| M-045 Mass Combat | ✗ | ✓ | BG primary resolution mechanic |

**BG combat resolution flow (reconstructed from all test data):**
1. Initiative: Commander Coord vs Coord. Tie: End stat (PP-033).
2. Unit type priority (PP-035): Cavalry → Ranged → Infantry → Irregular → Siege.
3. Combat roll: Military stat + commander Coord/2, TN7, Ob = enemy Military/2.
4. Damage: net successes → casualty rating (PP-006).
5. Morale: Morale track depletion per casualties (PP-034).
6. Rout check at Morale 3 (PP-034).

**Equipment in BG mode (M-043 partial):**
Cavalry (Löwenritter): +1D in first engagement vs infantry (Reach/Speed advantage at unit level).
Ranged units: +1D vs unshielded targets; −1D vs fortified targets.
Armoured infantry: Ob +1 for attacker (represents armour coverage at unit scale).

**Manoeuvres in BG mode (M-044):**
Disarm, Trip, Grapple — these are individual combat actions with no unit-level equivalent. In BG mode, tactical manoeuvrability is represented by:
- Terrain advantage (attacker/defender position → Ob modifier)
- Flanking (if attacking force splits and attacks from two sides in same season → +2D)
No formal Manoeuvre mechanic exists at the BG scale. Confirmed TTRPG-only.

### BG Combat Scenario — Löwenritter vs Church

**State:**
```
Löwenritter cavalry: Mi 5, morale 8, commander Ehrenwall (Coord 5)
Church infantry: Mi 6, morale 8, commander generic (Coord 3)
Terrain: open field (no modifier)
```

**Initiative (M-039 BG adaptation):**
Ehrenwall: 5D, Ob 1 → P(success) ≈ 93%
Church commander: 3D, Ob 1 → P(success) ≈ 70%
Likely: both succeed → tie → End tiebreaker. Ehrenwall End 4 vs Church commander End 3. Ehrenwall acts first.

**Unit type priority (PP-035):**
Löwenritter cavalry: Priority 1 (cavalry charge, first engagement).
Church infantry: Priority 3.
Cavalry gets first attack before infantry can respond.

**Round 1 — Cavalry charge:**
Pool: Mi 5 + cavalry bonus 1D + commander Coord/2 = 5 + 1 + 2 = 8D, TN7, Ob = Church Mi/2 = Ob 3.
P(≥3 net, 8D) ≈ 80%.
Most likely: Success → 2 casualty steps to Church (40% strength lost, morale −2 → 6).

**Round 1 — Church infantry counter (Priority 3):**
Pool: Mi 6 + commander 1D = 7D, TN7, Ob = Löwenritter Mi/2 = Ob 3. (Cavalry charge bonus only applies first engagement; now it's melee.)
P(≥3 net, 7D) ≈ 75%.
Most likely: Success → 2 casualty steps to Löwenritter (morale −2 → 6).

**Round 2 — Church morale check:**
Morale 6 (after 2 steps lost): above threshold 3, no rout check needed.
Church Mi now degraded by 40% → effective Mi: 6 × 0.6 = 3.6 → round down to Mi 3 for this engagement.
Pool: 3D + commander 1D = 4D, TN7, Ob 3. P(≥3 net, 4D) ≈ 20%.

**Round 2 — Löwenritter:**
Löwenritter also degraded by 40%: Mi 5 × 0.6 = 3. Pool: 3D + cavalry bonus (subsequent engagement: no first-charge bonus) + commander 2D = 5D, TN7, Ob = Church effective Mi/2 = Ob 2.
P(≥2 net, 5D) ≈ 82%.
Most likely: Success → Church takes another 2 casualty steps (now 80% losses). Church morale: 6 − 2 = 4.

**Round 3 — Church morale threshold:**
Morale 4 → approaching threshold 3. Church commander may attempt ordered withdrawal (Ob 2 Commander roll).
Commander 3D, Ob 2: P(success) ≈ 55%. Most likely: Success → Church withdraws in order.
**Battle outcome: Löwenritter tactical victory. Church force withdraws intact (no rout).** Löwenritter has ~40% casualties, Church has ~80%.

**Finding:** BG combat with PP-034 (morale) and PP-035 (unit priority) produces a coherent battle resolution. The cavalry advantage in first engagement significantly impacts outcomes (Löwenritter win despite lower Mi than Church). This validates the unit-type priority patch as functional.

**F-B8-15** (P3) — Cavalry first-engagement bonus definition needed. "First engagement only" — does this mean first round of the battle, or first time these specific units clash? If armies fight across multiple sessions, is the cavalry bonus reset? Add: "Cavalry charge bonus applies once per battle, in the first round of direct engagement with the target unit."

---

## T-B8-11 — REMAINING ISOLATION CELLS: INSTITUTIONAL + EXPLORATION BLOCK
**Coverage:** M-014, M-027, M-028, M-033, M-046, M-047, M-048, M-049, M-050, M-051, M-054
**Mode:** TTRPG | **Temporal:** Various | **Tracks:** Various | **Factions:** Various | **NPCs:** Various | **Archetypes:** Various
**Cells filled:** Multiple isolation + edge cells

### M-014 — Diagnosis (Interaction + Scenario + Edge)

**Interaction chain:** Diagnosis → identifies Knots and Residue → informs Weaving plan → informs Pulling target.

Pool: TS/2, TN7, Ob 2. At TS 30: 15D → P(success) ≈ 99%. Routine.

**Edge case — Diagnosis on a ME:**
Vaynard (Coherence 2) is Thread-corrupted. Diagnosing an ME: Ob 4 (elevated — ME Thread structure is chaotic).
Pool: 15D, Ob 4 → P(success) ≈ 90%. Diagnosis succeeds but output is ambiguous — the ME's Thread structure is partially incoherent.

**Scenario — Diagnosis as intelligence tool:**
Vaynard diagnoses Himlensendt's Thread connections to identify which ones are worth Pulling.
Output: map of Thread connections (up to 3 significant connections identified per successful Diagnosis).
This gives the Pulling player a target list. Without Diagnosis: Pull is blind (Ob +1, random connection affected).
**Diagnosis → Pull chain is mechanically incentivised.** This is good design.

### M-027 & M-028 — Southernmost Entry + Locked Zones (Isolation + Interaction + Edge)

**Southernmost entry (M-027):**
Entry requires: TS ≥ 10 (practitioners only) OR specific narrative credentials (cartographers, expedition members).
Entry roll: TS/2 + relevant History (exploration), Ob 3.
At TS 20: 10D + 2D History = 12D, Ob 3 → P(success) ≈ 99%.

**Locked Zones (M-028):**
Locked Zones within Southernmost: Thread-dense areas with additional entry Ob.
Entry: Ob 5. P(success, 12D) ≈ 75%. More challenging but accessible to experienced practitioners.

**Interaction — M-027 + M-028 + The Forgetting (M-029):**
Entry into Locked Zone triggers Forgetting risk. The Forgetting Ob = time spent in zone.
This creates a timer: the longer in a Locked Zone, the higher the Forgetting Ob.
Each scene in Locked Zone: Ob +1 on Forgetting check. Entry = Ob 1, after 3 scenes = Ob 4.
**The Forgetting creates urgency in exploration mechanics.** This is good design — exploration has a built-in cost function.

**Edge — Locked Zone with no exit:**
A Locked Zone that the characters cannot exit (Forgetting Ob too high, no Weaving capability):
At Forgetting Ob 6 (6 scenes in zone): P(avoid Forgetting, 12D, Ob 6) ≈ 42%. Near-50% chance of losing memories each scene after extended stay.
**Characters who overstay in Locked Zones face guaranteed Forgetting.** This is the mechanic's design intent.

### M-033 — Clock Interactions (Isolation + Interaction)

**Clock interactions in isolation:**
The three major clocks (TT, TC, IP) interact when they cross thresholds:
- TT > 45: TC +1/season AND IP +1/season (Thread Tension spills into political and theological spheres)
- TC > 50: Synod fires (already tested)
- IP > 40: Parliament crisis (procedure undefined — gap)

**Isolation — what does M-033 do when no threshold is crossed?**
Below-threshold state: clocks accumulate independently. No interaction between them.
**M-033 only activates at threshold crossings.** In most sessions, M-033 is dormant. It's a trigger mechanic, not an ongoing one.

**Interaction — all three thresholds crossed simultaneously:**
TT > 45 → TC +1 → TC reaches 50 → Synod → Church Mandate +2 → Church Domain Actions more powerful → TC gains accelerate → IP +1/season also firing.
**Three simultaneous thresholds create a runaway cascade.** In a high-tension campaign where TT 45 is crossed at TC 48 and IP 38: all three thresholds fire within 2 seasons of each other. The cascade becomes self-sustaining unless multiple suppression efforts are active simultaneously.

**F-B8-16** (P2) — Clock cascade at simultaneous thresholds is potentially self-sustaining. Three thresholds crossing within 2 seasons of each other can create a positive feedback loop. No mechanic for cascade interruption beyond individual clock suppression (each requiring separate player effort). Document as high-stakes escalation condition in GM reference.

### M-046 — Thread Ops in Combat (Isolation + Scenario + Edge)

**Isolation — Thread op types available in combat:**
1. Weaving (Ob 2–3): defensive use only in combat; creates environmental obstacles.
2. Pulling (Ob 3+): can be used but takes full Priority 5 round; effect on initiative-relevant connections.
3. The Leap (Ob 2): can be performed in combat; character goes Thread-side while body continues.
4. Diagnosis (Ob 2): observation only; no combat effect but identifies opponents' Thread connections.
5. FR-Lock/Dissolution: extremely high Ob; impractical in combat.

**Scenario — Practitioner in melee:**
Practitioner at TS 20, in combat with enemy. Chooses Weaving instead of physical attack.
Thread op at Priority 5: fires at start of next round (Priority 1 next round).
Meanwhile: practitioner has no physical defence this round (using action for Thread op).
Opponent attacks: practitioner's pool is 0D defence (all allocated to Thread op? Or can split?).
**GAP: Can a practitioner split their action between Thread op and physical defence?** No rule found. This is the critical question for practitioner viability in combat. If Thread ops consume the entire action including defence — practitioners are highly vulnerable in melee. If they can split — practitioners are balanced.

**Proposed fix (extends PP-036):** Add: "A practitioner may split their round between Thread operation initiation (Priority 5) and physical defence (Priority 3). If splitting: the Thread op pool = TS/4 (rounded down) and the defence pool = Coord/2 (rounded down). This represents divided attention."

**F-B8-17** (P2) — Thread op / physical defence split undefined. Practitioners in melee have no rule for simultaneous Thread + physical action. Either they abandon defence entirely (very vulnerable) or no Thread work in melee (thematically wrong). Needs explicit split rule.

### M-047, M-048, M-049, M-050, M-051, M-054 — Isolation cells

**M-047 Thread Events in Social (Isolation):**
Standalone: spontaneous Thread event (Shifting Object, Gap opening, ambient ThS spike) in a social scene.
Effect: all practitioners in scene make TS check (Ob 2) to perceive. Non-practitioners see physical manifestation only.
Roll: TS/2, TN7, Ob 2. At TS 20: 10D → P(success) ≈ 97%.
Devout interpretation: non-TS characters see manifestation as sign/omen. Composure check Ob 1 to maintain composure.

**M-048 Scale Transitions (Isolation):**
Trigger: Overwhelming success on a personal-scale action → faction-level consequence.
Rate: ~5% of personal actions achieve Overwhelming; of those, Scale Transition applies if action is relevant to faction domain. In practice: ~1–2 Scale Transitions per campaign arc (rare, high-impact).
This is correct for the mechanic's design intent. Scale Transitions are punctuation, not routine.

**M-049 Inquisitor Operations (Isolation):**
Intel Domain Action, Ob 2. P(success, Intel 5) ≈ 82%.
Investigation outcomes: CE +1 on suspects, potential exposure of practitioners, TC +1 per confirmed Thread corruption.
Inquisitors are the primary threat to practitioner operations. At Intel 5, they succeed most investigations. Practitioners need either Intel suppression (reducing Church Intel) or active concealment (PP-028) to sustain operations.

**M-050 Riskbreakers (Interaction + Scenario):**
Chain: Riskbreaker operates (Intel Domain Action) → DD accumulates → exposure check → cover blown or maintained.
Already detailed in T-B8-03. Remaining cell gap (Int, Scen) is now filled by T-B8-03 combined with T-B7-15.

**M-051 Devout Constraint (Isolation + Edge):**
Isolation: Devout Constraint blocks TS growth checks. Thread perception impossible. Dissonance Marks accumulate when physical manifestations cannot be explained.
Edge: At 5 Dissonance Marks — Constraint weakens. TS growth check fires (cannot be suppressed). If growth succeeds: practitioner-adjacent awareness begins. Faith crisis is narrative.
**Mechanically: the Devout Constraint is a delayed inevitability for characters with high CE exposure.** It doesn't prevent encounter with Thread — only perception of it.

**M-054 Einhir Sites (Isolation + Scenario):**
Isolation: Site grants +2D on Past-Oriented Thread ops. ThS locally elevated (+4).
Scenario (T-B7-14): already detailed. Remaining cell (Iso) now filled here.
Key isolation finding: Einhir sites are location-gating mechanics. They make certain operations possible that would otherwise be near-impossible. They also create detectability risk. The trade-off (power vs exposure) is the core design tension.

---

## BATCH 08 FINDINGS INDEX

| # | Test | Mechanics | Severity | Issue | Proposed Fix |
|---|------|-----------|----------|-------|-------------|
| F-B8-01 | T-01 | M-016 | P2 | Pull success has no mechanical expression on social mechanics (Circles/Mandate unaffected) | Successful Pull on social relationship reduces target Circles −1 (Overwhelming: −2) |
| F-B8-02 | T-02 | M-021 | P1 | Coherence has no recovery mechanic — one-way ratchet (extends F-B7-18) | Restoration Community Weaving (M-055) restores Coherence +1 per successful collective op, capped at original score |
| F-B8-03 | T-03 | M-052 | P2 (down from P1) | M-052 Concealment is undocumented procedure, not absent mechanic — DD + Circles cover constitute the system | Add §X.X "Concealment Procedures" documenting DD + Circles cover as unified system |
| F-B8-04 | T-04 | M-056 | P2 | Riskbreaker replacement procedure absent — burned Riskbreakers leave faction without covert capability | Add seasonal recruitment: Wealth 2 + Intel Domain Action Ob 2 = new Riskbreaker with DD 0, Circles 1 in target faction |
| F-B8-05 | T-04 | M-056 | P3 | Niflhel neutralised by targeting Intel stat — intentional design, undocumented | Document in faction reference as player strategy |
| F-B8-06 | T-05 | M-026 | P2 | ME effect radius undefined — scene vs zone vs radius produces massive functional difference | Define: ME effects apply to all characters in same zone; in BG mode, affect entire territory |
| F-B8-07 | T-05 | M-026,M-049 | P2 | ME investigation systematically drives TC — 5 investigations per arc = TC +5 from investigation alone | Document in GM reference as expected TC pressure source |
| F-B8-08 | T-05 | M-008,M-051 | P3 | Devout faith crisis arc is mechanically coherent but undocumented | Document as designed character trajectory in Devout character guidance |
| F-B8-09 | T-06 | M-041 | P3 | Withdraw mechanic gains value at Wounds 2+ — should be documented in combat guidance | Add combat guidance note on withdrawal EV at wound thresholds |
| F-B8-10 | T-06 | M-041 | P3 | Extended low-pool combat can produce prolonged near-stalemates | Add optional yield rule: at pool ≤ 3D both sides, either may declare Yield or Collapse without roll |
| F-B8-11 | T-07 | M-007 | P2 | Condition stacking undefined — same-type penalties from multiple Conditions may or may not stack | Add: multiple Conditions stack additively for same-type penalties |
| F-B8-12 | T-08 | M-008 | P3 | TS 80+ ambient overload has no mechanical expression | At TS 80+, Spirit check Ob 1 each scene to suppress; failure: −1D non-Thread rolls |
| F-B8-13 | T-08 | M-008 | P2 | No procedure for intentional TS development at TS 1–9 | Seasonal training action: trainer TS 20+ rolls Ob 2; trainee Ob 3; success: trainee TS +3 |
| F-B8-14 | T-09 | M-024 | P3 | Future Shifting (forward temporal displacement) undefined | Add: forward Shift requires Weaving Anchor, Ob +2 vs equivalent past Shift, FUT temporal tag |
| F-B8-15 | T-10 | M-045 | P3 | Cavalry first-engagement bonus definition needs clarification (per battle vs per engagement) | Define: cavalry charge bonus applies once per battle in first round of direct engagement with target unit |
| F-B8-16 | T-11 | M-033 | P2 | Simultaneous triple-threshold clock cascade is potentially self-sustaining | Document as high-stakes escalation in GM reference; no mechanical change needed |
| F-B8-17 | T-11 | M-046 | P2 | Thread op / physical defence split undefined — practitioner melee viability unclear | Add split rule: Thread op initiation + half-defence = TS/4 pool for op, Coord/2 for defence |

### P1 Summary — Batch 08
| Finding | Mechanic | Issue |
|---------|----------|-------|
| F-B8-02 | M-021 | Coherence has no recovery mechanic |

**New P1 findings this batch: 1**
**Total P1 after Batch 08: 19**

---

## PATCH PROPOSALS — BATCH 08 ADDITIONS

### PP-061
**Finding:** F-B8-01
**Severity:** P2
**Mechanic:** M-016 (Pulling)
**Proposed fix:** Add: "A successful Pull on a Thread connection underlying a social relationship reduces the target's relevant Circles rating by 1. Overwhelming Pull: by 2. The character whose Thread is altered is not aware of the cause unless they have TS ≥ 5."

### PP-062
**Finding:** F-B8-02
**Severity:** P1
**Mechanic:** M-021 (Coherence), M-055 (Restoration Community Weaving)
**Proposed fix:** Add Coherence recovery: "Successful Community Weaving in a Restoration context restores the participating practitioner's Coherence +1 (to a maximum of their original score). This represents relational re-anchoring — the community provides stability that Thread work alone cannot."
[EDITORIAL: confirm this use of M-055 as the canonical Coherence recovery path]

### PP-063
**Finding:** F-B8-03
**Severity:** P2 (downgraded)
**Mechanic:** M-052 (Concealment)
**Proposed fix:** Add §X.X "Concealment Procedures": "Cover identities are established via Circles (rating = depth of cover). Each covert operation accumulates Deniability Debt (+2 for standard, +3 for Destabilisation). Exposure check Ob = DD ÷ 2 (rounded up), rolled as Circles (cover) + relevant History. On failure: cover blown — Circles (cover) → 0, DD resets. On success: cover maintained this season. A blown cover cannot be re-used."

### PP-064
**Finding:** F-B8-04
**Severity:** P2
**Mechanic:** M-056 (Niflhel Destabilisation)
**Proposed fix (extends PP-008):** "Niflhel may recruit one Riskbreaker per season: Wealth 2 cost + Intel Domain Action Ob 2. Success: new Riskbreaker with DD 0 and cover identity (Circles 1) in target faction. Maximum 3 active Riskbreakers simultaneously."

### PP-065
**Finding:** F-B8-06
**Severity:** P2
**Mechanic:** M-026 (Monstrous Entities)
**Proposed fix:** "ME effects (CE accumulation, Certainty checks, ThS elevation) apply to all characters in the same zone as the ME. In BG mode, ME effects apply to the entire territory the ME occupies. A zone is defined as a room, area, or location where characters are co-present."

### PP-066
**Finding:** F-B8-11
**Severity:** P2
**Mechanic:** M-007 (Conditions)
**Proposed fix:** "Multiple Conditions may be active simultaneously. Same-type penalties stack additively (e.g., Rattled −1D social + Exhausted −2D all = −3D on social rolls). Different Conditions' clearing conditions are tracked independently."

### PP-067
**Finding:** F-B8-13
**Severity:** P2
**Mechanic:** M-008 (Thread Sensitivity)
**Proposed fix:** "A dormant practitioner (TS 1–9) may seek training from an active practitioner (TS 20+). Seasonal training action: trainer rolls End Ob 2 (teaching effort); trainee rolls Spirit Ob 3 (receptivity). If both succeed: trainee TS +3. Failure on either: no advancement this season."

### PP-068
**Finding:** F-B8-17
**Severity:** P2
**Mechanic:** M-046 (Thread Ops in Combat)
**Proposed fix (extends PP-036):** "A practitioner may split their combat round between Thread operation initiation and physical defence. Split action: Thread operation pool = TS/4 (rounded down); physical defence pool = Coord/2 (rounded down). The Thread operation still initiates at Priority 5 and manifests at Priority 1 next round."

---

## COVERAGE MATRIX UPDATE — BATCH 08

**Cells filled this batch:**

| Mechanic | Cells added |
|----------|------------|
| M-007 | Isolation |
| M-008 | Isolation, Edge |
| M-010 | Isolation |
| M-013 | Isolation |
| M-014 | Interaction, Scenario, Edge |
| M-015 | Isolation |
| M-016 | Interaction, Scenario |
| M-018 | Isolation (+ Interaction/Scenario via T-B7-05) |
| M-021 | Interaction, Scenario |
| M-022 | Isolation (+ Scenario via T-B7-06) |
| M-023 | Isolation, Interaction, Scenario |
| M-024 | Isolation, Interaction, Scenario |
| M-025 | Isolation, Interaction, Scenario |
| M-026 | Isolation (Interaction already ≥3 from T-B8-05) |
| M-027 | Isolation, Interaction, Edge |
| M-028 | Isolation, Interaction, Edge |
| M-033 | Isolation, Interaction |
| M-035 | Isolation |
| M-037 | Isolation |
| M-039 | BG mode coverage |
| M-041 | Isolation, Edge (BG mode confirmed TTRPG-only) |
| M-042 | BG mode confirmed TTRPG-only |
| M-043 | BG mode partial coverage |
| M-044 | Scenario (via T-B8-10), BG mode confirmed TTRPG-only |
| M-046 | Isolation, Scenario, Edge |
| M-047 | Isolation, Scenario |
| M-048 | Isolation |
| M-049 | Isolation |
| M-050 | Interaction, Scenario |
| M-051 | Isolation, Edge |
| M-054 | Isolation, Scenario |

**Mechanics now at full cell coverage (all 4 cells):**
M-010, M-013, M-015, M-018, M-022, M-023, M-024, M-025, M-027, M-028, M-033, M-035, M-047, M-048, M-049, M-054

**Mechanics still missing cells:**
- M-005: [CUT — remove from active tracking]
- M-016: Edge (was missing; Scenario now filled)
- M-021: Edge
- M-026: Edge (Isolation + Interaction filled this batch)
- M-038: Isolation (not yet done standalone)
- M-041: BG mode (confirmed TTRPG-only — mark as N/A)
- M-050: Edge
- M-051: Scenario
- M-052: now treated as documented undocumented procedure — all cells via T-B8-03
- M-056: Edge (Isolation filled this batch)

**Estimated cells complete after Batch 08:** ~195 / 224 = 87%

**Phase 3 gate status:**
- Interaction bar: 53/56 → now ~55/56 (M-026 closed this batch via T-B8-05; M-041 TTRPG-confirmed)
- P1 findings: 19 (was 18)
- Mode coverage: BG mode for core combat confirmed; remaining BG gaps are mechanics confirmed as TTRPG-only
- 7-dimension tags: enforced from Batch 07 forward

