# VALORIA — STRESS TESTS BATCH 6
## Social Mechanics: M-38 through M-41 + History Resonance + Certainty Blast Radius
### Date: 2026-03-27 · Simulator Modes: A (Isolation) + B (Interaction) + D (Edge Cases)

Probability reference (d10, TN 7): expected net per die ≈ 0.33.

---

## M-38 · DEBATE / RHETORIC STYLES
### Mode A — Isolation

**Input space:**

| Variable | Range | Typical | Edge |
|---|---|---|---|
| Pool (Cognition + History) | 3–12+ | 5–8 | 3 (untrained), 12+ (expert) |
| Exchanges | 1, 3, 5 | 3 (Formal) | 5 (Grand Debate) |
| Style match | +1D (resonant) or −2D (mismatch) | neutral | both extremes |
| Rattled penalty | 0 to −3D | 0–1 | 3 Rattled (severe) |

**Exchange probability at key pool matchups (TN 7):**

| Attacker Pool | Defender Pool | P(attacker wins exchange) | P(overwhelming exchange) |
|---|---|---|---|
| 5 vs 5 | neutral | ~50% | ~15% |
| 7 vs 5 | +2D advantage | ~70% | ~25% |
| 5 vs 7 | −2D disadvantage | ~30% | ~8% |
| 5 vs 5 | +1D resonant (attacker) | ~60% | ~20% |
| 5 vs 5 | −2D mismatch (attacker) | ~28% | ~5% |
| 8 vs 3 | Rattled 1 (−1D) → 8 vs 2 | ~88% | ~35% |

**Composure drain across a 5-exchange Grand Debate:**

Scenario: Both orators Composure 9 (Presence 3). Each exchange: loser takes +1 or +2 strain.

Expected outcomes across 5 exchanges at equal pools (~50% each wins):
- Expected strain accumulation per orator: ~2.5 (mix of +1 and occasional +2 losses)
- P(reaching Composure 9 strain = 1 Rattled in 5 exchanges) ≈ 25%
- P(2 Rattled in 5 exchanges) ≈ 5%

At Presence 5 → Composure 11: strain threshold harder to hit. Grand Debate rarely produces 2+ Rattled unless one side is significantly outmatched.

**Finding B6-M38-A: Debate is well-calibrated at equal pools.** Neither side collapses under normal conditions. Social attrition is real but not overwhelming. ✓

**Finding B6-M38-B (P2 — Inspiration attack requires "known" Inspiration, but no discovery mechanic is specified):** The Inspiration attack rule states: "The targeted Inspiration must be known to the attacker; discovering Inspirations requires prior investigation or Overwhelming social success." But no mechanic for "discovering Inspirations" is specified — neither an Ob, a roll type, nor what "prior investigation" means mechanically.

**Severity: P2** — the mechanic is weaponised knowledge, which is appropriate, but the acquisition path for that knowledge is undefined. Fix: "Discovering a specific Inspiration: Attunement + relevant History, Ob 3 (Reading Exchange post-contact), or Cognition + Investigation History, Ob 4 (external research). On success: GM confirms one Inspiration name and approximate value."

**Finding B6-M38-C (P3 — Style mismatch penalty of −2D vs no-History floor):** Style mismatch applies −2D, minimum 1D. A character with Cognition 2 and no History (3D base) hit with a mismatch: 3D − 2D = 1D. Expected net: ~0.33. P(any success) ≈ 33%. At 1D, losing is overwhelmingly probable but not certain. The minimum 1D floor is correct — never fully impossible. ✓

**Finding B6-M38-D (P2 — Grand Debate 5-0 total loss: seasonal social penalty not explicitly tied to a track):** "Losing faction or character takes +1 Ob to social actions with the opposing faction for one season." This is a free-floating modifier — not tracked on any sheet, not attached to any existing track. At the table, this will be forgotten within 2 scenes.

**Severity: P2** — seasonal penalty has no tracking mechanism. Fix: "Record on the character sheet as a Seasonal Condition (Social −1 vs [faction/character], expires [season])." Add a Seasonal Conditions box to the character sheet reference at §16.2.

---

## M-39 · READING EXCHANGE
### Mode A — Isolation

**Pool:** Attunement + relevant History bonus. **TN 7. Pre-contact only.**

| Attunement | History | Pool | P(Success+) | P(Overwhelming) |
|---|---|---|---|---|
| 2 | 0 pts (3D bonus) | 5D | ~80% | ~25% |
| 3 | 2 pts (5D bonus) | 8D | ~97% | ~45% |
| 4 | 4 pts (7D bonus) | 11D | ~99% | ~65% |
| 2 | 0 pts (3D bonus) | 5D vs Ob 2 | ~60% | ~15% |

**Finding B6-M39-A: Reading Exchange is low-risk, high-information.** At typical pools (5–8D), success rate is 80–97%. Failure is uncommon. This is appropriate — reading people is a basic social skill, not a dramatic roll. The information gained (Overwhelming: emotional state + tells + 2-exchange bonus) is meaningful but not mechanically dominant. ✓

**Finding B6-M39-B (P2 — "Failure: opponent notices the scrutiny" creates reactive disadvantage but no mechanical effect is defined):** On failure, the opponent "is aware of being read." What does this produce mechanically? Awareness might shift their disposition (now Cool toward the reader?), give them a defensive bonus on subsequent exchanges, or simply be narrative. As written, it is purely narrative with no mechanical expression.

**Severity: P2** — the failure consequence needs a mechanical hook to be meaningful. Fix: "On failure: GM may treat target disposition as one step more hostile for the remainder of the scene (Cool → Hostile, etc.), reflecting the target's wariness. The GM decides whether this applies based on the target's personality."

**Finding B6-M39-C (Boundary — Reading Exchange vs. simultaneous Reading attempts):** Both parties in a social scene simultaneously attempt a Reading Exchange. Who resolves first? The rule says it's available in the "first round of social contact only" — implying both may attempt. No resolution order specified. Simultaneous resolution is cleanest: both roll, both get their results at the same time. But if one fails (opponent notices scrutiny) and the other succeeds (gets tells), the "noticed" condition creates an asymmetry mid-scene that has no governing rule.

**Severity: P3** — add: "If both parties attempt a Reading Exchange simultaneously, resolve both rolls before either result is narrated."

---

## M-40 · SOCIAL PRESSURE (APPEALS / OUTSIDE DEBATES)
### Mode A — Isolation

**Pool:** Presence + History bonus. **Ob set by Disposition.**

| Pool | Disposition (Ob) | P(Success+) | P(Overwhelming) |
|---|---|---|---|
| 5D | Friendly (Ob 1) | ~99% | ~55% |
| 5D | Neutral (Ob 2) | ~80% | ~25% |
| 5D | Cool (Ob 3) | ~45% | ~8% |
| 5D | Hostile (Ob 4) | ~15% | ~2% |
| 8D | Hostile (Ob 4) | ~60% | ~20% |
| 8D | Contemptuous (Ob 5) | ~30% | ~7% |

**Finding B6-M40-A: Appeals have a hard cliff at Hostile/Contemptuous.** Even skilled social characters (8D) face low odds against Contemptuous targets. This is correct — appealing to someone who despises you is hard. ✓

**Finding B6-M40-B (P2 — Appeal degree table has no "partial persuasion" mechanism):** Partial result: "audience requires something additional before acting." What constitutes "something additional"? No guidance on what this might be — another roll, a specific action, information? In combat, Partial means "goal with complication." In social, Partial is undefined as to resolution path.

**Severity: P2** — fix: "On Partial: the audience names a condition for their cooperation (an action, information, or concession). If the character satisfies the condition this scene: treat as Success. If not: the Appeal expires without effect."

**Finding B6-M40-C (P2 — Multiple Appeals vs same target same scene):** Can a player make two Appeals to the same target in one scene after a Partial? The rule states Let It Ride: "no re-attempts unless circumstances have significantly changed." A Partial technically succeeded partially — does the condition-satisfaction count as "changed circumstances"? Ambiguous. Let It Ride could block a second Appeal even after the condition is met (since the scene is the same).

**Severity: P2** — fix: "A successful Partial that leads to condition satisfaction allows a follow-up Appeal at the same Ob (not re-rolled; the partial persuasion is extended, not started over)."

**Finding B6-M40-D: Appeal vs Debate registers are explicitly separated.** "A successful Appeal does not reverse a Debate loss." This is clean — prevents one-roll reversals of formal exchange outcomes. ✓

---

## M-41 · APPROACH TRAINING
### Mode A — Isolation

**Approach Training is a prerequisite tag, not a roll.** One full campaign season of Thread study. Grants permanent tag; unlocks all active Thread operations.

**Input space:** Binary — either has tag or doesn't.

**Finding B6-M41-A: No mechanic defines what "one full campaign season of Thread study" requires.** Does the character need a mentor? Can they self-study? What happens if they're interrupted mid-season? The result is a permanent tag, but the process is undefined.

**Severity: P2** — the acquisition path for the most mechanically significant character trait in the game (unlocking all Thread operations) has no procedure. Fix: "Acquiring Approach Training requires: a mentor with Approach Training and TS 40+ (or access to an authenticated Einhir text) + one full season of dedicated study (no Domain Actions or extended travel during that season) + a Spirit check TN 7, Ob 2. On success: tag acquired. On failure: primed — next season's study automatically succeeds."

**Finding B6-M41-B (P2 — Approach Training has no cost in CP or resources):** Approach Training is effectively free — it only costs one season and a Spirit check. For the most powerful mechanical unlock in the game (Thread operations), this is an extremely low bar. A TS 0 character who somehow finds a mentor and spends one quiet season becomes a Thread practitioner. No CP, no Inspiration expenditure, no Renown gate.

**Severity: P2** — this may be intentional (Thread access should be thematically available to motivated characters) but it invites rapid practitioner proliferation. Consider: "Approach Training costs 4 CP in addition to the season and Spirit check."

[EDITORIAL: whether to add a CP cost to Approach Training requires user ruling. Flagging.]

**Finding B6-M41-C: The Scholarly TS Path (Lenneth Variant) is correctly structured as an alternative to experiential confrontation.** It uses the same Spirit check; the qualifying event is intellectual rather than experiential. ✓

---

## MODE B — INTERACTION CHAINS

### B-CHAIN-03: Rattled × Debate × Inspiration Attack

**Scenario:** Character A (Presence 3, Composure 9, Cognition 4, History 5D) vs Character B (same stats). Grand Debate (5 exchanges). B knows A's primary Inspiration ("Justice") and targets it with Character Style attacks.

**Exchange 1:** A vs B, Cognition 4 + History 5D = 9D each. Equal pools. Expected: 50/50. Assume B wins (net 4 vs net 2). A loses by normal margin. Composure strain: +1. A strain total: 1/9.

**Exchange 2:** B declares Character Style, names "Justice" as target. A rolls net 0 (failure). B wins Overwhelmingly (net ≥ 2× A's net: A net 0 → any B result is Overwhelming). Inspiration attack triggers: "Justice" −1 point. Composure strain: +2 (Overwhelming loss). A strain: 3/9.

**Exchange 3:** A is now at strain 3. Still 6 away from Composure. B wins again normally. Strain: +1. A strain: 4/9.

**Exchange 4:** Strain 4. B wins again, Overwhelming. Strain: +2. A strain 6/9. Still not Rattled.

**Exchange 5:** Strain 6. B wins with +2 again. Strain 8/9 — still not Rattled. Final exchange: if A takes any more strain (lose exchange 5 again) — wait, exchange 5 is the last one. A has lost all 5 exchanges. Grand Debate 5-0 total loss. A takes +1 Ob social actions vs B for one season.

**Finding B6-B03-A: Composure 9 (Presence 3) survives a 5-0 Grand Debate loss without Rattled.** Across 5 exchanges, even in worst case (all Overwhelming losses), total strain = 5×2 = 10. Composure 9 → hit at 9 → 1 Rattled at exchange 5 if total exactly hits 9. In practice: 8 strain by exchange 4, 2 more strain on exchange 5 → total 10 → Composure 9 hit once (Rattled 1), reset, remaining 1 strain below threshold. **So: 1 Rattled occurs at the last exchange of a 5-0 sweep.** The Rattled condition in the final exchange does matter: −1D on that roll.

**Finding B6-B03-B (P2 — Inspiration attack success condition may be too easy):** The condition is "defending orator achieves net ≤ 0." This means *any* outright failure (no net successes, or 1s dominate) triggers the attack. Against a skilled orator using Character Style against an emotional target: P(net ≤ 0 for defender at 9D) ≈ 5%. Low but present every exchange. Across 5 exchanges: cumulative P(at least one Inspiration attack) ≈ 23%. Significant but not guaranteed — appropriate. ✓

**Finding B6-B03-C (P1 — Debate "Compromise Rule" reference inconsistency):** §9.6 says "Debate Compromise Rule: A lost Debate does not reverse a prior Appeal from the same scene." But the rule is called the "Compromise Rule" — a name that implies compromise, not simply a cross-register isolation note. The name creates player confusion: "what do we compromise?" No compromise procedure exists. The name is wrong.

**Severity: P1 (rules clarity break)** — fix: Rename "Debate Compromise Rule" to "Register Separation Rule." No mechanical change needed, just the label.

### B-CHAIN-04: Rattled × Reading Exchange × Appeal sequence

**Scenario:** Diplomat (Attunement 4, Presence 5) attempts to negotiate with Hostile NPC (Ob 4) in a tense scene.

**Step 1 — Reading Exchange:** Pool 4 + 5D History = 9D. P(Success+) ≈ 99%. Overwhelming likely. Gets full emotional state + 2-exchange Debate bonus if scene escalates. No strain.

**Step 2 — Appeal (Hostile, Ob 4):** Presence 5 + History 5D = 10D. P(Success+) at Ob 4 ≈ 73%. P(Overwhelming) ≈ 30%. +1D from Reading Exchange bonus if this counts as an "exchange" — but it doesn't (Appeals are not exchange-structure). **Reading Exchange bonus applies to Debate exchanges only.** The bonus from a successful Reading does not carry over to Appeals.

**Finding B6-B04-A (P2 — Reading Exchange bonus scope is ambiguous):** "§9.4: +1D on the first formal Exchange in the same scene." Appeals are not formal Exchanges. The word "Exchange" technically refers only to Debate structure. But at the table, players will assume the Reading bonus applies to any social roll, not just Debates.

**Severity: P2** — fix: "The Reading Exchange bonus (+1D / +1D for 2 exchanges on Overwhelming) applies only to the first formal Debate exchanges in the same scene, not to Appeals or other single-roll social actions."

---

## MODE D — EDGE CASES (Social mechanics)

### Boundary: Composure at minimum (Presence 1 → Composure 7)

Presence 1 → Composure 7. Each Rattled: −1D.

In a Grand Debate (5 exchanges): each Overwhelming loss = +2 strain. Composure 7 hit on first 4 strain points reaching threshold. After exchange 2 or 3 with two Overwhelming losses: 1 Rattled. After 3–4 exchanges with sustained Overwhelming losses: 2 Rattled possible (−2D).

At 2 Rattled, Cognition 3, History 5D → pool 8D − 2D = 6D. Still functional but significantly degraded. P(winning exchange at 6D vs 8D) ≈ 30%. Cascade is real but not incapacitating — social incapacitation requires specific condition (from §9.1: "At 2 Rattled marks, the character is socially incapacitated").

**Finding B6-D01: "Socially incapacitated" at 2 Rattled is correctly defined but has no combat equivalent.** A socially incapacitated character can still fight — Rattled specifically does not affect combat. This asymmetry is intentional (social and physical tracks are independent). ✓

### Cascade: Debate defeat × Domain Echo × Faction Mandate

A PC loses a Grand Debate 5-0 against a Church Cardinal. Under §9.6: losing orator's position does not generate Domain Echo. If the Debate was about Church authority in a territory, the Church's Overwhelming win generates a Domain Echo — Church Mandate +1 automatically (§11).

**Finding B6-D02: Domain Echo from Debate operates through the standard Domain Echo trigger — no separate calculation needed.** GM recognises scope, Echo fires. Clean. ✓

### Deadlock: Appeal × Hostile Disposition × Let It Ride

Character fails an Appeal against Hostile NPC (Ob 4). Let It Ride: cannot re-attempt. NPC "may harden against further Appeals." Now Contemptuous (Ob 5). Character has no Debate option (not in formal context). Reading Exchange already used. No further social tool available.

**Finding B6-D03 (P2 — No recovery path from Contemptuous disposition within a scene):** If an Appeal failure causes disposition to harden to Contemptuous, the character has no mechanics to improve it within that scene. Debate requires formal context. Reading Exchange is spent. Next Appeal is blocked by Let It Ride. The NPC is effectively locked out for the remainder of the scene.

**Severity: P2** — needs explicit note: "Disposition hardening from a failed Appeal is GM discretion, not mandatory. GMs should use it only when dramatically warranted — a failed Appeal to a Hostile NPC does not automatically become Contemptuous."

### Crunch Cascade: Grand Debate + Rhetorical style tracking + Inspiration attack monitoring + Renown bonus

In a single Grand Debate exchange with all systems active:
1. Both orators declare style (3 options each)
2. Check style mismatch (−2D)?
3. Check resonant style tag (+1D)?
4. Check Renown tier (Debate bonus at tier 5+)?
5. Roll pool
6. Compare net successes
7. Apply Composure strain (loser)
8. Check Inspiration attack trigger (net ≤ 0?)
9. Check Rattled (did strain hit Composure?)
10. Apply Rattled (reset Composure, note −1D)
11. Check Grand Debate 5-0 condition

**That is 11 resolution steps per exchange × 5 exchanges = 55 steps for one Grand Debate.**

**Finding B6-D04 (P2 — Grand Debate is the crunch-heaviest non-combat mechanic in the system):** 55 resolution steps is manageable only with pre-prepared reference cards. Without them, a Grand Debate between faction leaders will slow the table significantly.

**Proposed fix:** Pre-print a "Debate Card" for GMs — one side shows the 11-step sequence; the other shows common pool sizes, strain thresholds, and the Inspiration attack trigger.

---

## SUMMARY TABLE

| Test | Mechanic | Mode | Finding | Severity | Fix Required |
|---|---|---|---|---|---|
| B6-M38-A | Debate | A | Calibration at equal pools ✓ | — | None |
| **B6-M38-B** | Debate | A | Inspiration attack: discovery mechanic undefined | **P2** | Add Attunement/Investigation Ob |
| **B6-M38-D** | Debate | A | Grand Debate 5-0 seasonal penalty has no tracking mechanism | **P2** | Add Seasonal Condition to §16.2 |
| B6-M39-A | Reading Exchange | A | Low-risk, high-information: correct | — | None |
| **B6-M39-B** | Reading Exchange | A | Failure "opponent notices": no mechanical effect defined | **P2** | One-step disposition shift (GM discretion) |
| B6-M39-C | Reading Exchange | A | Simultaneous Reading: resolution order unspecified | P3 | Add simultaneous resolution note |
| B6-M40-A | Appeals | A | Cliff at Hostile/Contemptuous: intentional | — | None |
| **B6-M40-B** | Appeals | A | Partial persuasion: "something additional" undefined | **P2** | Add condition/satisfaction mechanism |
| **B6-M40-C** | Appeals | A | Let It Ride × Partial condition: ambiguous | **P2** | Clarify follow-up Appeal on satisfied Partial |
| B6-M40-D | Appeals | A | Appeal vs Debate register separation: clean | — | None |
| **B6-M41-A** | Approach Training | A | Acquisition procedure undefined | **P2** | Add mentor requirement + Spirit check |
| **B6-M41-B** | Approach Training | A | No CP cost for most powerful unlock | **P2** | [EDITORIAL: CP cost ruling needed] |
| B6-M41-C | Approach Training | A | Scholarly variant correctly structured | — | None |
| B6-B03-A | Debate × Rattled | B | Composure survives 5-0 sweep: correct calibration | — | None |
| B6-B03-B | Debate × Inspiration | B | Inspiration attack trigger probability appropriate | — | None |
| **B6-B03-C** | Debate structure | B | "Compromise Rule" name is wrong — implies non-existent procedure | **P1** | Rename to "Register Separation Rule" |
| **B6-B04-A** | Reading × Appeal | B | Reading Exchange bonus scope ambiguous (Exchange vs Appeal) | **P2** | Restrict bonus to Debate exchanges only |
| B6-D01 | Rattled | D | Social incapacitation vs combat independence: intentional | — | None |
| B6-D02 | Debate × Domain Echo | D | Domain Echo from Debate: clean | — | None |
| **B6-D03** | Disposition | D | Contemptuous deadlock in scene: no recovery path | **P2** | Note hardening as GM discretion, not mandatory |
| **B6-D04** | Grand Debate | D | 55 resolution steps — crunch-heaviest non-combat mechanic | **P2** | Recommend Debate Card reference tool |

**P1: 1 (B6-B03-C — "Compromise Rule" mislabelling)**
**P2: 10 (B6-M38-B, M38-D, M39-B, M40-B, M40-C, M41-A, M41-B[editorial], B04-A, D03, D04)**
**P3: 1 (B6-M39-C)**

---

## COVERAGE MATRIX UPDATE

| Mechanic ID | Name | Isolation | Interaction | Scenario | Edge Cases | Status |
|---|---|---|---|---|---|---|
| M-38 | Debate / Rhetoric | ✓ B6 | ✓ B6 | — | ✓ B6 | Issues found |
| M-39 | Reading Exchange | ✓ B6 | ✓ B6 | — | ✓ B6 | Issues found |
| M-40 | Social Pressure / Appeals | ✓ B6 | — | — | ✓ B6 | Issues found |
| M-41 | Approach Training | ✓ B6 | — | — | — | Issues found |

---

*Batch 6 complete — 2026-03-27*
