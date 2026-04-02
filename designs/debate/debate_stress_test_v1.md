# DEBATE SYSTEM STRESS TEST v1

## Model: Opus 4.6
## Method: Isolation → Interaction → Edge Case → Findings → Patches → Retest
## Input: Debate system as described in conversation (not yet compiled into a document)

---

# PHASE 0: SYSTEM AS STATED

Before testing, capture every mechanical claim made during design. If a component has no specified procedure, flag it immediately.

## 0.1 Stated Mechanics

| Component | Specified? | Procedure |
|---|---|---|
| Initiative (exchange 1) | Yes | Higher Presence speaks first |
| Initiative (subsequent) | Yes | Winner of previous exchange. Draw retains. |
| Read (step 1) | Partial | Roll Attunement + History, TN 7. Success → Game Master gives signal about audience state. |
| Genre choice | Yes | Past / Present / Future |
| Orientation choice | Yes | Revealing / Obscuring |
| Argument roll | Yes | Cognition + History bonus, TN 7 |
| Memory bonus | Partial | Game Master awards 1–3D "when citing specific precedent, contradiction, or documented fact" |
| Focus defence | Partial | Roll Focus vs incoming strain. Successes reduce strain. |
| Presence modifier | Partial | Modifies strain dealt. Formula: "every 2 points above 3" → +1 strain |
| Composure | Yes | Threshold. Strain ≥ Composure → Rattled (−1D all debate rolls) |
| Concentration | Yes | Focus + Presence. Depletes by 1 per exchange. At 0 → Spent (−2D, opponent +1D). |
| Conviction Track | Partial | Audience on a track between two positions. Moves by margin. |
| Genre weight | **NO** | Game Master decides ×1, ×0.5, ×0 per genre. No procedure for how. |
| Orientation weight | **NO** | Game Master decides. No procedure. |
| Dynamic weight shift | **NO** | Game Master shifts weights between exchanges. No procedure for how or when. |
| Attunement read output | **NO** | Game Master decides what to tell the player. No calibration for success degrees. |
| Conviction Track scale | **NO** | "10 points" mentioned in example. No defined scale. |
| Conviction Track threshold | **NO** | "+5 for outright victory" in example. No procedure for setting. |
| Tracker movement formula | **NO** | "Margin minus audience Spirit modifier" mentioned once, never specified. |
| Tie resolution | Partial | Initiative stays. No tracker movement. No other consequence. |
| Ethical mode interaction | **NO** | Factions have ethical modes. How they mechanically affect anything is unstated. |
| Respondent advantage | Stated but unspecified | "They heard the argument before choosing." No mechanical advantage defined. |
| Same genre / opposite orientation resolution | **NO** | "Direct clash" stated. No procedure. |
| Same genre / same orientation resolution | **NO** | "Competition" stated. No procedure. |
| Different genre resolution | **NO** | "Talking past each other" stated. Institutional preference mentioned. No procedure. |
| Corroboration | Partial | Bonds + History, Ob 1, +1D on success. Knot required. |
| Regroup | Partial | Forfeit exchange. Restore Concentration by Focus score. |
| Concede a Point | Partial | Forfeit exchange. 1 strain. +1D next exchange. |
| Call for Division | Partial | Force vote after exchange 2+. Count exchanges won. |
| Unmask | Yes | Clear strain. Reveal truth. Debate ends. |
| Thread co-movement | Stated | Winner's genre + orientation determines type. No magnitude specified. |
| Game Master ledger | Yes | Shown after resolution. |
| Asymmetric proceedings | Stated | Tribunal, Royal Audience described conceptually. No mechanical procedure. |

## 0.2 Unspecified Components (Pre-Test Findings)

**F-00-01 (CRITICAL): Genre weight has no procedure.** The entire Conviction Track system depends on the Game Master assigning weights. There is no rule for how to set them, how to shift them, or what constrains the Game Master. This is the system's load-bearing component and it is entirely fiat.

**F-00-02 (CRITICAL): Attunement read output has no calibration.** The read roll exists but what the Game Master says on success vs partial vs failure is undefined. In the example, the Game Master gave detailed tactical intelligence on every read. There is no rule for what information corresponds to what roll result.

**F-00-03 (CRITICAL): Interaction types have no resolution procedure.** Three interaction types were identified (same genre/opposite orientation, same genre/same orientation, different genre) but none has a mechanical resolution distinct from "compare successes."

**F-00-04 (HIGH): Conviction Track has no defined scale, threshold, or movement formula.** The example used a 10-point track with a +5 threshold. These numbers were invented during narration.

**F-00-05 (HIGH): Ethical mode has no mechanical expression.** Factions have ethical frameworks. The design claims they affect susceptibility. No procedure connects ethical mode to any roll, modifier, or tracker adjustment.

**F-00-06 (HIGH): Spirit as audience resistance is mentioned once and never specified.** "Each successful exchange moves the marker by margin minus audience Spirit modifier" — what is this modifier? Where does it come from? How is audience Spirit determined?

**F-00-07 (MEDIUM): Memory bonus is Game Master-discretionary.** The Game Master awards 1–3D when the player cites specifics. No rule determines 1D vs 2D vs 3D. No rule defines what counts as "specific enough."

**F-00-08 (MEDIUM): Focus defence is mechanically thin.** Roll Focus, successes reduce strain. But: what TN? What Ob? Is it a flat reduction (each success = −1 strain) or compared to something? The example implied flat reduction but didn't state it.

**F-00-09 (MEDIUM): Presence strain modifier formula is unclear.** "Every 2 points above 3" was stated once. The example then used "Presence − 3" as the formula. These produce different results. Presence 5: the first gives +1, the second gives +2.

**F-00-10 (LOW): Concentration formula may produce degenerate values.** Focus + Presence. A character with Focus 1, Presence 1 has Concentration 2 — Spent after 2 exchanges, making Formal Debates (3 exchanges) mechanically impossible without Regroup.

---

# PHASE 1: ISOLATION TESTS

## Test 1.1: Argument Roll (Cognition + History)

**Input space:**

| Variable | Range | Typical | Edge Low | Edge High |
|---|---|---|---|---|
| Cognition | 1–7 | 4 | 1 | 7 |
| History bonus | 3–10 | 7 | 3 (1 pt History + 3) | 10 (7 pt History + 3) |
| Total pool | 4–17 | 11 | 4 | 17 |

**Expected successes at TN 7 (P(success per die) = 0.4):**

| Pool | E[successes] | P(0 successes) | P(≥5 successes) |
|---|---|---|---|
| 4 | 1.6 | 13.0% | 8.7% |
| 7 | 2.8 | 2.8% | 26.6% |
| 11 | 4.4 | 0.1% | 63.3% |
| 14 | 5.6 | <0.1% | 82.1% |
| 17 | 6.8 | <0.1% | 93.1% |

**Finding S1-01 (P2):** The argument pool range is 4–17. At pool 4, the orator averages 1.6 successes. At pool 17, they average 6.8. The expected margin between a pool-4 and pool-17 orator is ~5.2 — a blowout every exchange. This means Cognition + History quality dominates everything else. A character with Cognition 7 and a relevant 7-point History will beat a character with Cognition 2 and a 1-point History in every exchange regardless of genre choice, read quality, or audience state.

**Comparison to combat:** Combat pool is (Agility × 2) + History + 3, minimum 5. Range: 5–20. But combat pool is SPLIT between offence and defence. A pool-20 fighter who goes all offence has 20 attack dice but 0 defence dice. The split creates tactical variance. Debate has no split — the full pool is always applied. This means debate has LESS tactical variance per exchange than combat, despite being designed for more.

**Finding S1-02 (P1):** No pool split in debate means no allocation decision. Combat's core tactical choice is absent. The orator rolls their full pool every time. This is the single largest mechanical gap between the two systems.

## Test 1.2: Focus Defence

**As stated:** Roll Focus, TN 7 (assumed — not specified). Each success reduces incoming strain by 1.

| Focus | E[successes] | E[strain reduction] |
|---|---|---|
| 1 | 0.4 | 0–1 (usually 0) |
| 3 | 1.2 | 1 |
| 5 | 2.0 | 2 |
| 7 | 2.8 | 2–3 |

**Incoming strain (margin + Presence modifier):** Typical range 1–6. Edge case: blowout margin 5 + Presence modifier 4 = 9 strain in one exchange.

**Finding S1-03 (P2):** Focus at 3 (typical) reduces strain by 1 on average. This is marginal. A blowout (strain 6+) is barely affected by Focus. Focus defence as currently designed is a minor reduction, not a meaningful tactical layer. In combat, defence dice fully oppose attack dice — the defence pool can completely negate the attack. In debate, Focus reduces strain after the fact, like armour DR. It's a passive soak, not an active opposition.

**Finding S1-04 (P2):** Focus defence has no specified TN. If TN 7 (standard), Focus is weak. If TN 6 (easier), Focus becomes significantly stronger (P = 0.5 per die). This is an unresolved parameter.

## Test 1.3: Presence Strain Modifier

**Formula conflict:** Two formulas stated:
- "Every 2 points of Presence above 3, +1 strain" → Presence 5 = +1, Presence 7 = +2
- "Presence − 3" → Presence 5 = +2, Presence 7 = +4

**Finding S1-05 (P1):** Formula is contradictory. Must be resolved. The "Presence − 3" formula is dangerously strong: Presence 7 adds +4 strain per winning exchange. Combined with a margin of 3, that's 7 strain per exchange — enough to Rattle a Composure-9 character in a single exchange. The "every 2 above 3" formula is more moderate: Presence 7 adds +2.

**Recommendation:** Use floor((Presence − 3) / 2) to cap the modifier. Presence 3 = +0, Presence 4 = +0, Presence 5 = +1, Presence 6 = +1, Presence 7 = +2. This keeps Presence valuable without making it dominant.

## Test 1.4: Composure and Rattled

**Composure formula not stated in this session.** Prior §9 used Composure = Poise + Heart, then Composure = Presence + 6. The example used Composure 11 (Baralta) and 9 (Vaynard) without stating the derivation.

**Finding S1-06 (P1):** Composure formula is undefined in the redesign. Must be specified. Prior values ranged from 7 to 14 depending on formula.

**Rattled effect:** −1D to all debate rolls. This is a permanent debuff once triggered (until Unmask or scene end).

**Finding S1-07 (P2):** Rattled at −1D is mild. In a pool of 11, losing 1D is a 9% reduction in expected successes. A Rattled orator is barely worse than a non-Rattled one. Combat's wound equivalent (incapacitation threshold) is dramatic — you're out of the fight. Rattled should be more severe to create real pressure toward Unmask.

**Options:**
- −2D (moderate — 18% reduction at pool 11)
- Halve pool (severe — as stated in original §9 for Poise)
- Cannot use Focus defence while Rattled (thematic — you've lost composure, you can't stay on topic)
- All of the above in escalating stages (Rattled 1, Rattled 2, etc.)

## Test 1.5: Concentration and Spent

**Concentration = Focus + Presence.** Depletes by 1 per exchange.

| Focus | Presence | Concentration | Exchanges before Spent |
|---|---|---|---|
| 1 | 1 | 2 | 2 (cannot complete Formal without Regroup) |
| 3 | 3 | 6 | 6 (comfortable for Grand) |
| 5 | 5 | 10 | 10 (never threatened) |
| 7 | 3 | 10 | 10 (never threatened) |
| 3 | 5 | 8 | 8 (never threatened) |

**Finding S1-08 (P2):** Concentration is only relevant for characters with Focus + Presence ≤ 5. Anyone with Focus 3 + Presence 3 = 6 can survive a Grand Debate (5 exchanges) without regrouping. The mechanic only bites for extreme low-stat characters. For typical characters, Concentration is a non-factor.

**Comparison to combat:** Stamina = Endurance + History + 1, depletes by 1 per ROUND. Combat rounds are faster than debate exchanges and there are more of them per scene. A combat with 8 rounds is normal. A Grand Debate has 5 exchanges. Stamina bites because there are more rounds. Concentration doesn't bite because there are fewer exchanges.

**Recommendation:** Either increase depletion (−2 per exchange, or −1 per exchange + −1 when you lose an exchange) or reduce the base pool (Concentration = Focus alone, not Focus + Presence).

## Test 1.6: Attunement Read

**No calibrated output table exists.** The Game Master decides what to say. Testing what SHOULD happen:

| Net Successes | What Should Be Communicated |
|---|---|
| 0 (Failure) | Misleading or no information. Orator misjudges the room. |
| 1 (Success) | One accurate signal: which genre the audience currently favours, OR whether Revealing or Obscuring is stronger. Not both. |
| 2 (Overwhelming) | Both signals: favoured genre AND favoured orientation. |
| 3+ (Exceptional) | Both signals + one specific detail: "The Crown delegates are the swing votes" or "Baralta's last argument annoyed the Speaker." |

**Finding S1-09 (P1):** This table doesn't exist in the system. It must. Without it, the Game Master has no procedure and will give inconsistent information. The read step is the most important tactical decision in the system — it's how players learn what works. If the output is uncalibrated, the entire tactical layer collapses into Game Master narrative preference.

## Test 1.7: Conviction Track Movement

**As stated:** Margin of victory moves the tracker, modified by genre weight and orientation weight.

**Formula (reconstructed from example):** Tracker Δ = margin × genre_weight × orientation_weight.

But: what ARE the weights? The Game Master sets them. There is no rule.

**Finding S1-10 (P0 — SYSTEM-BREAKING):** The Conviction Track is the win condition. Its movement depends entirely on Game Master-set weights with no constraining procedure. This means:

- The Game Master decides who wins before the debate starts (by setting weights that favour one side's likely genre)
- The Game Master can change the outcome mid-debate (by shifting weights)
- The players cannot verify whether the weights were fair until the ledger is revealed, at which point the debate is over

The ledger provides transparency but not fairness. Showing that Past was weighted ×1 after the fact doesn't help if the Game Master set it knowing Baralta would argue Past.

**This is the system's critical failure point.** The weight-setting procedure must be mechanical, not discretionary.

---

# PHASE 2: INTERACTION TESTS

## Test 2.1: Read + Genre Choice Interaction

**Scenario:** Orator A rolls Attunement and gets Overwhelming (3+ net). Game Master correctly signals that Future is the strong genre. Orator A chooses Future + Revealing. Orator B rolls Attunement and fails — gets no signal or a misleading one. Orator B chooses Past + Revealing (their default).

**Expected outcome:** Orator A's argument is fully weighted. Orator B's argument is at ×0.5 or ×0. Even if Orator B wins the exchange on raw successes, the tracker moves toward A because A's winning argument was on-genre.

**Problem:** Orator B won the exchange but the tracker moved against them. From B's perspective, they won the argument and lost the room. This is intended behaviour — but it requires the player to understand and accept that exchange victory ≠ debate victory. If the system isn't clearly communicated, this will feel like the Game Master cheating.

**Finding S2-01 (P2):** The gap between exchange winner and tracker winner must be explicitly communicated to players before the debate begins. "Winning the argument and winning the room are different things" should be a stated system principle, not a surprise.

## Test 2.2: Initiative + Respondent Information Advantage

**Scenario:** Baralta (initiative) declares Future + Revealing. Vaynard (respondent) hears this and knows what she argued. He can now choose to match (Future + Revealing — competition), oppose (Future + Obscuring — direct clash), or pivot (Past + Revealing — different genre).

**Problem:** The respondent's advantage is informational, but how does it translate mechanically? Currently: it doesn't. Both roll Cognition + History regardless. The respondent has no mechanical bonus for reacting. Their advantage is purely in genre/orientation selection — they can choose to match, oppose, or pivot with full knowledge.

**Finding S2-02 (P2):** The respondent advantage is real but subtle. It works through genre/orientation choice, not through dice modifiers. This is correct and doesn't need a patch — but it needs to be stated explicitly so players understand WHY initiative is valuable (you set the frame) and WHY responding is valuable (you choose whether to engage on those terms).

## Test 2.3: Corroboration + Primary Argument Interaction

**Scenario:** Orator A has an ally with Bonds 4 and a Knot. Ally rolls Bonds 4 + History 6 = 10D, TN 7, Ob 1. Expected: 4 successes, net 3 (Overwhelming). Orator A gets +2D (per Overwhelming corroboration).

**Orator A's new pool:** Cognition 4 + History 7 + Corroboration 2 = 13D. Expected successes: 5.2.
**Without corroboration:** 11D. Expected successes: 4.4.

**Difference:** +0.8 expected successes. Meaningful but not overwhelming.

**Finding S2-03 (P3):** Corroboration is well-calibrated. +1D or +2D is a genuine but not dominant advantage. The Knot requirement prevents corroboration spam. The one-per-phase (now one-per-exchange) limit prevents stacking. This mechanic works as designed.

## Test 2.4: Strain Accumulation over Grand Debate (5 Exchanges)

**Scenario:** Orator A (Cognition 5, Presence 5, pool 12) vs Orator B (Cognition 3, Presence 3, pool 9). A wins every exchange.

**Exchange margins (expected):** A averages 4.8 successes, B averages 3.6. Expected margin: 1.2 per exchange.

**Strain per exchange to B:** Margin 1.2 + Presence modifier (floor((5-3)/2) = +1) = 2.2 average.

**Focus defence by B:** If Focus 3, E[reduction] = 1.2. Net strain per exchange: ~1.

**Cumulative strain after 5 exchanges:** ~5.

**B's Composure (assume ~9):** 5 strain < 9 Composure. B is NOT Rattled even after losing all 5 exchanges.

**Finding S2-04 (P1):** In a pure domination scenario (one side wins every exchange), the loser does not reach Rattled in a Grand Debate with the current numbers. Strain accumulation is too slow relative to Composure thresholds. This means Composure/Rattled/Unmask — the dramatic crisis mechanic — almost never fires. The debate ends on exchange count long before the emotional threshold is reached.

**This is the equivalent of a combat system where nobody ever takes a wound.** The dramatic stakes mechanic is non-functional at typical values.

**Root cause:** Strain per exchange is too low (typically 1–3 after Focus defence) and Composure is too high (typically 8–12). The ratio doesn't produce Rattled within 3–5 exchanges.

## Test 2.5: Memory Bonus Interaction with Genre

**Scenario:** Orator argues Past + Revealing (prosecution). Cites specific documents, dates, testimony. Game Master awards Memory bonus.

**Question:** Does Memory bonus apply to Present or Future genre arguments? If the orator argues Future + Revealing ("I recall the economic projections from last season's Guild report showing that this policy will fail"), is that a Memory-eligible citation?

**Finding S2-05 (P2):** Memory bonus has no genre restriction. An orator can cite precedent or documentation in any genre. This is correct (you can cite a past projection to support a future argument), but it means Memory is universally applicable, not Past-specific as implied by the design. This is fine — but it should be stated.

## Test 2.6: Interaction Type Resolution (Same Genre / Different Orientation)

**Scenario:** A argues Past + Revealing (prosecution). B argues Past + Obscuring (defence). This is the "direct clash" case.

**Current resolution:** Both roll Cognition + History. Compare successes. Higher wins.

**Problem:** This is identical to two orators arguing the same genre and same orientation. There is no mechanical difference between clashing and competing. The interaction types were identified as structurally distinct but resolve identically.

**Finding S2-06 (P1):** Interaction types are flavour, not mechanics. Same genre / opposite orientation, same genre / same orientation, and different genre all resolve the same way: compare Cognition + History rolls. The structural analysis promised three distinct resolution modes. The system delivers one.

---

# PHASE 3: EDGE CASES

## Test 3.1: Attunement 1 vs Attunement 7

**Orator A (Attunement 1, History +7):** Read pool 8D. E[successes] = 3.2. Net 2.2 (Success to Overwhelming).
**Orator B (Attunement 7, History +7):** Read pool 14D. E[successes] = 5.6. Net 4.6 (Exceptional).

**Problem:** Even low-Attunement characters with good Histories read the room effectively. The History bonus dominates Attunement. A character with Attunement 1 and a 7-point History reads better (pool 8) than a character with Attunement 5 and no History (pool 5).

**Finding S3-01 (P2):** History bonus applies to Attunement reads but the read is about perceiving the room's emotional state — not about the subject matter. A History in "Constitutional Law" shouldn't help you read whether the Crown delegates are sympathetic. Consider: Attunement reads use Attunement alone (no History bonus). This makes Attunement investment meaningful and prevents History from dominating every roll in the system.

## Test 3.2: Presence 7, Cognition 1

**Character concept:** Commanding presence, terrible arguer. High strain output on the rare occasions they win, but almost never wins.

**Pool:** Cognition 1 + History 7 = 8D. E[successes] = 3.2.
**Against typical pool 11:** E[successes] = 4.4. Expected to lose by 1.2 every exchange.
**On the rare win:** Strain dealt = margin + floor((7-3)/2) = margin + 2. If margin 1: 3 strain. Significant.

**This character concept works.** They lose most exchanges but when they land a hit, it's devastating. Low Cognition, high Presence is a glass cannon in reverse — an iron cannon that rarely fires.

**Finding S3-02 (P3):** Character archetype differentiation works. The attribute spread creates distinct debate identities: the sharp arguer (Cognition), the enduring wall (Focus), the devastating speaker (Presence), the room-reader (Attunement), the team player (Bonds). This is correct and doesn't need patching.

## Test 3.3: All Exchanges Tie

**Scenario:** Grand Debate, 5 exchanges, all tie.

**Current rules:** Initiative never transfers. Conviction Track never moves. No strain dealt. After 5 exchanges of nothing, the debate ends with the starting Conviction Track position unchanged.

**Outcome:** Whoever the audience was initially biased toward wins by default. Neither orator accomplished anything.

**Finding S3-03 (P1):** Complete stalemate is anticlimactic and produces a victory for the initially favoured side without either orator earning it. Ties need consequences: either mutual strain (the audience is frustrated, both orators feel pressure), partial tracker movement (the initiative holder's argument slightly dominates in a tie — they set the frame), or a mechanical tiebreaker (Presence contest).

## Test 3.4: Regroup Exploit

**Scenario:** Orator A has Focus 5, Concentration 10. Grand Debate (5 exchanges). A regroups in exchanges 2 and 4 (forfeiting both, giving opponent margin-1 wins). A argues exchanges 1, 3, and 5 at full Concentration.

**Result:** Opponent wins exchanges 2 and 4 (margin 1 each). A needs to win exchanges 1, 3, and 5 to win 3-2. A argues at full capacity in their exchanges because they never run low on Concentration.

**Problem:** Regroup is an exchange forfeit that restores Concentration by Focus score. Focus 5 restores 5 Concentration — more than enough for the remaining exchanges. The cost (margin-1 loss) is minimal because the Conviction Track penalty for a margin-1 loss is small.

**Finding S3-04 (P2):** Regroup in alternating exchanges is a viable exploit for high-Focus characters in Grand Debates. They sacrifice two exchanges at minimum cost and fight three exchanges at full capacity. The opponent wins 3-2 on exchanges but may not win the room if the Regrouping orator's three arguments were in the right genre. This isn't necessarily degenerate — it's a legitimate strategy for endurance debaters — but the Concentration mechanic needs to be relevant enough that this is a real tradeoff, not free recovery.

## Test 3.5: Practitioner Uses Thread Operations Mid-Debate

**Scenario:** A practitioner orator initiates a Thread operation during a Grand Debate. They target the audience's emotional state (W-42: Crowd Coherence from stage15 catalogue).

**Current rules:** No interaction specified between Thread operations and the debate system. The Thread operation resolves through Thread mechanics (Leap, Contact, Weaving). Its effect on the debate is undefined.

**Finding S3-05 (P1):** Thread operations during debates have no resolution procedure. A practitioner who Weaves the audience's emotional state mid-debate is performing a mechanical action (Thread operation) that should interact with a mechanical system (debate) but doesn't. Both systems function independently. The practitioner could Weave the audience to be sympathetic and then argue, but the sympathetic audience has no mechanical expression in the debate system because genre weights are Game Master fiat anyway.

## Test 3.6: 3+ Party Debate

**Scenario:** Three faction representatives debate in Parliament. Crown, Hafenmark, and Church each argue different positions.

**Current system:** Initiative is between two orators. Exchange resolution is pairwise. There is no multi-party procedure.

**Finding S3-06 (P2):** Multi-party debates have no mechanical structure. Parliament with three or more speakers is a core gameplay scenario for this game. The system only handles 1v1.

## Test 3.7: Audience with Split Factions

**Scenario:** Parliament audience is 40% Hafenmark (Kantian — cares about universalizable principle), 30% Crown (virtue ethics — cares about character), 30% Guilds (moral relativism — context-dependent).

**Current system:** The Game Master sets one genre weight for the whole audience. But this audience has three different ethical modes pulling in different directions. A Past + Revealing argument moves Hafenmark (who respects precedent as universal principle), partially moves Crown (who respects it as evidence of character), and barely moves Guilds (who say "that was then, this is now").

**Finding S3-07 (P1):** Split audiences have no procedure. The Game Master must somehow average across faction ethical modes to produce one weight set. This is the kind of judgment call that makes Game Master prep burdensome and outcomes inconsistent. The system needs either: (a) one tracker per faction group in the audience, or (b) a mechanical formula for blending ethical modes into composite weights.

---

# PHASE 4: FINDINGS SUMMARY

## Priority 0 (System-Breaking)

| ID | Finding | Impact |
|---|---|---|
| S1-10 | Genre weight has no constraining procedure. Game Master decides who wins. | Win condition is fiat |

## Priority 1 (Must Fix Before Play)

| ID | Finding | Impact |
|---|---|---|
| F-00-01 | Genre weight has no procedure | Core mechanic undefined |
| F-00-02 | Attunement read output uncalibrated | Tactical layer undefined |
| F-00-03 | Interaction types have identical resolution | Promised complexity doesn't exist |
| F-00-04 | Conviction Track has no scale/threshold/formula | Win condition undefined |
| F-00-05 | Ethical mode has no mechanical expression | Faction identity in debate is flavour only |
| F-00-06 | Spirit as audience resistance is unspecified | Audience difficulty is undefined |
| S1-02 | No pool split — less tactical variance than combat | Core decision absent |
| S1-05 | Presence strain formula contradictory | Damage calculation broken |
| S1-06 | Composure formula undefined | Health threshold broken |
| S1-09 | Attunement read output table missing | Cannot run read step |
| S2-04 | Strain too slow / Composure too high — Rattled never fires | Drama mechanic non-functional |
| S2-06 | Interaction types are flavour not mechanics | Three modes promised, one delivered |
| S3-03 | All-tie stalemate defaults to initial bias | Anticlimactic, rewards nothing |
| S3-05 | Thread operations have no debate interaction | Cross-system gap |
| S3-07 | Split audiences have no procedure | Core scenario unsupported |

## Priority 2 (Should Fix)

| ID | Finding | Impact |
|---|---|---|
| F-00-07 | Memory bonus is discretionary | Inconsistent application |
| F-00-08 | Focus defence underspecified (TN?) | Minor ambiguity |
| F-00-09 | Presence formula conflicted (less severe than S1-05 — same finding) | — |
| F-00-10 | Low Concentration characters can't complete Formal | Edge case hardship |
| S1-01 | Cognition + History dominates — blowouts at high disparity | Low counterplay |
| S1-03 | Focus defence too weak | Defence layer marginal |
| S1-07 | Rattled at −1D is too mild | Threshold not threatening |
| S1-08 | Concentration rarely bites | Resource mechanic non-functional |
| S2-01 | Exchange win ≠ tracker win not communicated | Player confusion |
| S2-05 | Memory has no genre restriction (may be intended) | Clarification needed |
| S3-01 | History dominates Attunement reads | Attribute investment pointless |
| S3-04 | Regroup exploit in Grand Debates | Free recovery |
| S3-06 | Multi-party debates unstructured | Missing scenario |

## Priority 3 (Minor)

| ID | Finding | Impact |
|---|---|---|
| S2-03 | Corroboration well-calibrated | No patch needed |
| S3-02 | Character archetypes differentiate correctly | No patch needed |

---

# PHASE 5: PATCHES

## PATCH D-01: Genre Weight Procedure (fixes S1-10, F-00-01, F-00-05)

**Problem:** Genre weight is pure Game Master fiat. The win condition depends on it.

**Patch:** Replace Game Master-discretionary weights with a mechanical derivation from the Question and the Audience.

**Step 1 — The Question sets the Primary Genre:**
- "Did X happen?" → Past primary
- "Is X true / is this person fit?" → Present primary
- "Should we do X?" → Future primary

**Step 2 — Primary genre is weighted ×1. The other two genres are weighted ×0.5 by default.**

**Step 3 — Audience ethical mode adjusts ONE genre by +0.5 or −0.5:**

| Ethical Mode | Genre Adjustment |
|---|---|
| Virtue ethics (Crown) | Present +0.5 (character matters) |
| Divine command (Church) | Past +0.5 (scripture and doctrine are historical) |
| Categorical imperative (Hafenmark) | Past +0.5 (precedent as universal principle) |
| Consequentialism (Varfell) | Future +0.5 (outcomes matter) |
| Moral relativism (Guilds) | No fixed adjustment — Game Master chooses based on context (this IS moral relativism) |
| Rawlsian social contract (Restoration) | Future +0.5 (what system should we build?) |

**Resulting weight range:** 0.5, 1.0, or 1.5. Never 0 — no genre is completely irrelevant. Never above 1.5 — no genre is doubly weighted.

**Step 4 — Orientation weight is fixed:** Revealing = ×1. Obscuring = ×0.75. (Institutions prefer clarity. This can be inverted for specific scenarios — a Niflhel-dominated backroom might weight Obscuring higher — but the default favours Revealing.)

**Step 5 — Weights do NOT shift dynamically.** They are set during Game Master setup and do not change. The Game Master's only discretion is the Guild adjustment and any scenario-specific inversions, both of which are recorded in the ledger before the debate begins.

**Effect:** Weights are derivable, predictable (if you know the audience), and verifiable. Players who read the room correctly can deduce the weights from the read signal. The Game Master's ledger records the derivation, not just the result.

## PATCH D-02: Attunement Read Calibration (fixes F-00-02, S1-09)

**Problem:** No defined output per success level.

**Patch:** Attunement reads use Attunement alone, no History bonus (fixes S3-01). Output table:

| Net Successes | Output |
|---|---|
| Failure (0) | Game Master gives a misleading signal. One genre identified as strong that is actually weak. Player acts on bad intelligence. |
| Partial (1) | Game Master identifies the Primary genre only. ("They care about what happened.") No orientation signal. |
| Success (2) | Game Master identifies the Primary genre AND whether Revealing or Obscuring is favoured. ("They want to know what happened, and they want certainty.") |
| Overwhelming (3+) | Primary genre, orientation, AND one specific detail about the audience's current emotional state or factional composition. ("The Crown delegates are the swing votes and they're getting impatient with technicalities.") |

**Failure is actively misleading, not merely blank.** This creates real risk in the read step. An orator who rolls poorly and trusts their read will choose the wrong genre and pay for it on the Conviction Track.

## PATCH D-03: Conviction Track Specification (fixes F-00-04, F-00-06)

**Problem:** No defined scale, threshold, or movement formula.

**Patch:**

**Scale:** 0 to 10. Starting position set by Game Master at setup (0 = fully biased toward Side B, 5 = neutral, 10 = fully biased toward Side A). Typical start: 4–6.

**Threshold:** Side A wins if tracker ≥ 8. Side B wins if tracker ≤ 2. Between 3 and 7: compromised outcome (Game Master narrates partial victory proportional to position).

**Movement formula:** Tracker Δ = floor(margin × genre_weight × orientation_weight) − audience_resistance.

**Audience resistance:** Fixed value derived from audience Spirit. If the audience is a faction, use the faction's Stability score as resistance (stable institutions are hard to move). If mixed, average the represented factions' Stability scores (round up). Typical resistance: 1–3.

**Example:** Margin 3, genre weight ×1, orientation ×1, audience resistance 2. Tracker Δ = floor(3 × 1 × 1) − 2 = 1.

**Effect:** High-resistance audiences (Church at Stability 5, resistance 3) are very hard to move — you need large margins in the right genre just to shift the tracker by 1. Low-resistance audiences (a demoralized faction at Stability 2, resistance 1) move easily.

## PATCH D-04: Strain Acceleration (fixes S2-04, S1-07, S1-08)

**Problem:** Strain accumulates too slowly. Rattled never fires. Concentration never bites.

**Patch (three changes):**

**A) Base strain increase:** Loser takes strain = margin + Presence modifier + 1 (the +1 ensures even a margin-1 loss produces real strain).

**B) Rattled severity increase:** Rattled effect becomes: −2D to all debate rolls AND Focus cannot be used for defence while Rattled. This creates a genuine crisis — the Rattled orator is both weaker and more vulnerable.

**C) Concentration depletion increase:** Concentration depletes by 1 per exchange PLUS 1 additional when you lose an exchange. An orator who loses 3 straight exchanges depletes 6 Concentration (3 base + 3 loss penalties). This makes losing streaks mechanically punishing and Regroup more necessary.

**Retest with Patch D-04:**

Scenario: Orator A (pool 12, Presence 5) vs Orator B (pool 9, Focus 3, Composure 9). A wins every exchange with expected margin 1.2.

**Strain per exchange (patched):** 1.2 (margin) + 1 (Presence modifier) + 1 (base) = 3.2. Focus defence reduces by 1.2. Net: ~2 per exchange.

**After 3 exchanges (Formal Debate):** ~6 strain vs Composure 9. Not Rattled but close.
**After 5 exchanges (Grand Debate):** ~10 strain vs Composure 9. **Rattled at exchange 5.** The drama mechanic fires.

**Concentration (patched):** B starts at 6. Loses 1 per exchange + 1 per loss = 2 per exchange. After 3 exchanges: 0. **Spent.** B must Regroup or fight exchange 4 at −2D.

**Assessment:** Patch produces Rattled and Spent at appropriate moments. Grand Debates are now genuinely dangerous for the losing orator. Formal Debates are tense but survivable.

## PATCH D-05: Interaction Type Resolution (fixes F-00-03, S2-06)

**Problem:** Three interaction types resolve identically.

**Patch:**

**Same genre, opposite orientation (CLASH):** Direct opposition. Both rolls fully count. Winner's margin moves the Conviction Track. Loser takes strain. This is the standard resolution.

**Same genre, same orientation (COMPETITION):** Both arguments move the same direction. Winner's margin moves the tracker, but the LOSER'S argument also moves the tracker by 1 in the same direction (the audience heard both and was partially persuaded by both). Strain is reduced: loser takes margin − 1 (minimum 1). The arguments reinforced each other even though one was stronger.

**Different genre (DIVERGENCE):** The arguments don't engage. Each is evaluated independently against genre weight. The initiative holder's argument moves the tracker by floor(successes × holder_genre_weight × orientation_weight) − audience_resistance. The respondent's argument moves it by floor(successes × respondent_genre_weight × orientation_weight) − audience_resistance, in the OPPOSITE direction. Net movement is the difference. No strain dealt to either side — neither argument attacked the other.

**Effect:** Divergence means no strain but also no strain dealt. It's a cold exchange. Players who want to damage their opponent must engage on the same genre. Players who want to move the tracker without personal risk can diverge — but they give up the chance to strain the opponent.

## PATCH D-06: Ties Produce Consequences (fixes S3-03)

**Problem:** Ties are dead exchanges.

**Patch:** On a tie, both orators take 1 strain (the effort of arguing to a standstill is draining) and the tracker moves 1 point toward the initiative holder (they set the frame, the audience slightly favours the person who spoke with authority even if neither dominated).

## PATCH D-07: Focus Defence Specification (fixes F-00-08, S1-03, S1-04)

**Problem:** Focus defence is underspecified and weak.

**Patch:** Focus is passive, not rolled. Incoming strain is reduced by floor(Focus / 2). Focus 1–2 = −1 strain. Focus 3–4 = −1 strain. Focus 5–6 = −2 strain. Focus 7 = −3 strain.

**Rationale:** Passive reduction is simpler (no extra roll per exchange), always relevant, and scales predictably. It parallels armour DR in combat (passive damage reduction, not active defence roll).

**Interaction with Patch D-04B:** When Rattled, Focus defence is lost. The orator no longer reduces incoming strain. This makes Rattled a genuine crisis — you're taking full strain every exchange until you Unmask.

## PATCH D-08: Presence Strain Formula (fixes S1-05, F-00-09)

**Problem:** Two contradictory formulas.

**Patch:** Presence strain modifier = floor((Presence − 3) / 2). 

| Presence | Modifier |
|---|---|
| 1–3 | +0 |
| 4–5 | +1 |
| 6–7 | +2 |

Clean, bounded, consistent with combat scaling.

## PATCH D-09: Memory Scope (fixes F-00-07, S2-05)

**Problem:** Memory bonus is discretionary and genre-unrestricted.

**Patch:** Memory bonus applies whenever the orator cites a specific, verifiable claim — a date, a document, a prior statement, a named precedent. Available in any genre. The bonus is fixed at +2D (not variable 1–3D). Either the citation is specific enough to qualify or it isn't. Binary, not graduated. Game Master determines qualification, but the rule is clear: "Did the player cite a specific, named, verifiable thing? If yes, +2D."

## PATCH D-10: Composure Formula (fixes S1-06)

**Problem:** Composure formula undefined in redesign.

**Patch:** Composure = Poise + Bonds + 3.

**Rationale:** Poise is composure under pressure (the primary component). Bonds is relational grounding — characters with strong relationships are harder to destabilize because they have something to hold onto. The +3 baseline prevents extreme fragility at low attributes.

**Range:** Composure 5 (Poise 1, Bonds 1) to 17 (Poise 7, Bonds 7). Typical: 9–11.

---

# PHASE 6: RETEST (Post-Patch)

## Retest 6.1: Full Grand Debate with All Patches Applied

**Setup:**

**Baralta:** Cognition 4, Memory 3, Focus 5, Attunement 3, Presence 5, Poise 5, Bonds 4. Composure 12. Concentration 10. History bonus +7. Pool: 11D.

**Vaynard:** Cognition 5, Memory 4, Focus 3, Attunement 4, Presence 3, Poise 3, Bonds 2. Composure 8. Concentration 6. History bonus +6. Pool: 11D.

**Question:** "Should Parliament authorize the Crown's trade agreement with Altonia?" → Future primary.

**Audience:** Parliament (mixed). Crown (virtue ethics, Present +0.5), Hafenmark majority (Kantian, Past +0.5). Average Stability: 4. Audience resistance: 2.

**Weights (D-01):** Future ×1 (primary). Past ×1 (Hafenmark adjustment +0.5 on base 0.5). Present ×1 (Crown adjustment +0.5 on base 0.5). All genres equally weighted in this specific setup — a consequence of the mixed audience. Orientation: Revealing ×1, Obscuring ×0.75.

**Starting Conviction Track:** 5 (neutral). Threshold: ≥8 for Side A (approve), ≤2 for Side B (reject).

**Exchange 1:**

Read: Baralta rolls Attunement 3 alone (D-02): 3D → 1 success. Partial. Game Master: "They care about the future — this is a policy question." No orientation signal.

Vaynard rolls Attunement 4: 4D → 2 successes. Success. Game Master: "Future is primary, and they want clarity — Revealing is strong. Obscuring will land weakly."

Initiative: Baralta (Presence 5 > 3).

Baralta chooses: Future + Revealing (she knows the genre from her read).
Vaynard chooses: Future + Obscuring (risk-amplification — "we don't know what Altonia really wants"). He knows from his read that Obscuring is weak, but he wants to block the deal and this is his genuine position.

**Interaction type (D-05):** Same genre, opposite orientation → CLASH.

Baralta rolls: 11D → 5 successes. Vaynard rolls: 11D → 4 successes. Baralta wins, margin 1.

**Strain to Vaynard (D-04, D-08):** 1 (margin) + 1 (Presence mod, Baralta Presence 5 → +1) + 1 (base) = 3. Focus defence (D-07): floor(3/2) = 1 reduction. Net strain: 2. Vaynard at 2/8.

**Tracker (D-03):** Δ = floor(1 × 1.0 × 1.0) − 2 (resistance) = −1. Minimum movement: 0. **Tracker doesn't move.** The audience resistance absorbed the margin.

**Concentration:** Baralta 10→9. Vaynard 6→4 (−1 base, −1 loss penalty per D-04C).

**Analysis:** The high audience resistance (2) means a margin-1 win produces zero tracker movement. This correctly models a stubborn Parliament — small victories don't move the room. Only decisive wins (margin 3+) will shift the tracker. This creates real pressure to win BIG, not just win.

**Exchange 2:**

Read: Baralta 3D → 0 successes. Failure. Game Master gives misleading signal: "The room seems to be responding to character arguments — who you are matters more than what you propose." (This is false — Future is still primary.)

Vaynard 4D → 2 successes. Success. Game Master: "Future is still primary. Revealing still favoured."

Baralta, misled, chooses: Present + Revealing (she'll try to establish her credibility on trade matters).
Vaynard, correctly informed, chooses: Future + Revealing (he pivots — instead of blocking, he'll propose alternative trade terms). He's competing with Baralta on different genre.

**Interaction type (D-05):** Different genre → DIVERGENCE. Each evaluated independently.

Baralta rolls: 11D → 4 successes. Present weight ×1.0, Revealing ×1.0. Movement: floor(4 × 1.0 × 1.0) − 2 = 2 toward Baralta (approve).
Vaynard rolls: 11D → 5 successes. Future weight ×1.0, Revealing ×1.0. Movement: floor(5 × 1.0 × 1.0) − 2 = 3 toward Vaynard (reject, or his alternative).

**Net tracker movement:** 3 − 2 = 1 toward Vaynard. Tracker: 5 → 4.

**Strain (D-05 Divergence):** No strain dealt. Neither argument attacked the other.

**Concentration:** Baralta 9→8. Vaynard 4→3.

**Analysis:** Baralta's failed read cost her. She argued Present when the room cared about Future. Vaynard's correctly-read Future argument moved the tracker more. The Divergence mechanic worked — no strain, but the tracker moved based on argument quality × genre match. Baralta's bad read produced a real mechanical consequence.

**Exchange 3:**

Read: Baralta 3D → 2 successes. Success. Game Master: "Future is primary. Revealing is preferred." She now has correct information.

Vaynard 4D → 1 success. Partial. Game Master: "They care about what should happen." Genre only, no orientation.

Initiative: Vaynard won exchange 2 (via tracker advantage in Divergence — needs a ruling). Actually in Divergence there's no "winner" in the exchange sense. **Gap: who gets initiative after Divergence?**

[FINDING R-01: Initiative after Divergence is undefined. Patch needed: initiative stays with holder after Divergence, since neither orator defeated the other.]

Initiative stays with Baralta (original holder, no transfer).

Both choose: Future + Revealing. Baralta is corrected. Vaynard stays on course.

**Interaction type:** Same genre, same orientation → COMPETITION (D-05).

Baralta: 11D + Memory bonus (she cites specific trade projections from last season's Guild audit) = 13D → 6 successes.
Vaynard: 11D + Memory bonus (he cites Altonia's prior trade violations) = 13D → 5 successes.

Baralta wins, margin 1.

**Tracker (Competition per D-05):** Winner moves tracker by floor(1 × 1.0 × 1.0) − 2 = −1. Minimum 0. No movement from winner's margin. BUT: Competition rule — loser's argument also moves tracker by 1 in same direction. So: +1 toward approve (Baralta's direction). Tracker: 4 → 5.

**Strain (Competition per D-05):** Margin − 1 = 0 (minimum 1). 1 + Presence mod 1 + base 1 = 3. Focus: −1. Net: 2 to Vaynard. Vaynard at 4/8.

**Concentration:** Baralta 8→7. Vaynard 3→1 (−1 base, −1 loss).

**Exchange 4:**

Vaynard at Concentration 1. If he doesn't Regroup, he fights exchange 5 at Concentration 0 → Spent (−2D). He chooses to **Regroup**: forfeits exchange 4, Baralta wins automatically (margin 1), Vaynard restores Concentration by Focus (3). Concentration: 1 + 3 = 4.

Strain from forfeit: 1 (margin) + 1 (Presence) + 1 (base) = 3 − 1 (Focus) = 2. Vaynard at 6/8.

Tracker: Baralta wins margin 1. floor(1 × genre_weight × orientation_weight) − resistance. But what genre? Regroup doesn't involve an argument. **Gap: how does a forfeited exchange interact with genre weight and the tracker?**

[FINDING R-02: Forfeited exchanges have no genre. Tracker movement from a forfeit should be fixed at +1 toward the non-forfeiting side, regardless of weight. The audience saw one orator speak and the other stay silent — that moves the room by a fixed amount, not by argumentative quality.]

Tracker: 5 → 6 (fixed +1 toward Baralta).

**Exchange 5 (final):**

Read: Baralta 3D → 1 success. Partial. Vaynard 4D → 3 successes. Overwhelming. Vaynard has the better read.

Both choose Future + Revealing (COMPETITION).

Baralta: 11D → 4 successes. Vaynard: 11D → 5 successes. Vaynard wins, margin 1.

**Tracker (Competition):** Winner (Vaynard) movement: floor(1 × 1.0 × 1.0) − 2 = −1 → 0. No movement from Vaynard's win. Loser's argument: +1 toward Vaynard's direction (reject). Tracker: 6 → 5.

Wait — Competition moves tracker in the SAME direction for both. If Vaynard won, both arguments move toward reject. That's wrong. Both were arguing Future + Revealing but for OPPOSITE positions. Competition should move the tracker in the WINNER'S direction, with the loser's +1 also in the winner's direction (the winning argument dragged the losing argument's audience along).

[FINDING R-03: Competition tracker movement direction needs clarification. Both orators argue the same genre/orientation but for different positions (approve vs reject). The winner moves the tracker in their direction. The "+1 for loser's argument" should also go in the winner's direction — the audience was persuaded in that direction by both arguments, just more by one.]

Tracker: 6 → 5 (Vaynard's direction). Then +1 loser's contribution also toward Vaynard: 5 → 4. Wait — Vaynard is arguing against the deal (toward ≤2). So: 6 → 5 → 4? That's a net −2, which is too much for a margin-1 Competition win.

[FINDING R-04: Competition's "+1 for loser" is too generous when combined with the winner's movement. The loser's contribution should only fire if the winner's margin exceeds audience resistance. If the winner's argument doesn't clear resistance, the loser's certainly doesn't. Remove the loser's +1 contribution. Competition resolves identically to Clash but with reduced strain (margin − 1).]

**Revised tracker:** Vaynard margin 1. floor(1 × 1.0 × 1.0) − 2 = −1 → 0. No movement.

Tracker stays at 6.

**Strain to Baralta:** Competition: margin − 1 = 0 → minimum 1. 1 + Presence mod (Vaynard Presence 3 → +0) + base 1 = 2. Focus defence floor(5/2) = 2. Net: 0 strain. Baralta takes nothing.

Vaynard's low Presence means even when he wins, he barely hurts.

**Final State:**

| | Baralta | Vaynard |
|---|---|---|
| Strain | 0 / 12 | 6 / 8 |
| Concentration | 6 | 3 |
| Exchanges won | 2 (1 + forfeit) | 1 |
| Ties | 0 | 0 |
| Divergence | 1 (lost) | 1 (won) |

**Conviction Track:** 6 / 10. Between thresholds (3–7 = compromise zone).

**Outcome:** Neither side achieved outright victory. Tracker at 6 (slightly toward approve). Parliament approves the trade agreement with amendments reflecting Vaynard's concerns. Baralta gets the deal but not on her terms. Vaynard doesn't block it but secures modifications.

## Retest Assessment

**What worked post-patch:**
- Audience resistance (D-03) prevented small margins from moving the tracker. Only margin 3+ wins at ×1 weight clear resistance 2. This makes large victories matter and small ones irrelevant to the room — correct.
- Baralta's failed read in exchange 2 produced a real consequence (wrong genre choice, tracker moved against her). The misleading signal (D-02) worked.
- Vaynard's Concentration crisis (D-04C) forced a Regroup in exchange 4. The mechanic bit at the right time.
- Strain accumulation (D-04A) brought Vaynard to 6/8 — close to Rattled but not there in 5 exchanges. A 7-exchange debate would have Rattled him.
- Divergence (D-05) created a real tactical moment — no strain but the tracker moved.

**What didn't work:**
- The Conviction Track barely moved. After 5 exchanges: 5 → 6. Audience resistance of 2 absorbed almost all movement. A neutral starting position (5) with threshold 8 requires net +3 movement — that means three decisive (margin 3+) wins in the right genre. This might be TOO resistant. The audience is almost immovable.
- Competition's "+1 for loser" was incoherent (R-04). Removed during retest.
- Initiative after Divergence is undefined (R-01).
- Forfeit interaction with genre weight is undefined (R-02).
- Vaynard's low Presence means he can never deal significant strain even when winning. Presence as strain modifier creates a "can't punch hard enough" problem for low-Presence characters. His Cognition advantage (he wins exchanges) is undermined by his inability to hurt when he wins.

**New findings from retest:**

[FINDING R-05: Audience resistance at 2 makes the tracker nearly immovable for margin-1 wins. Consider: resistance applies to the FIRST point of movement only (threshold), not subtracted from all movement. Margin 1: blocked. Margin 2: 1 point movement. Margin 3: 2 points. This makes the resistance a floor rather than a tax.]

[FINDING R-06: Low-Presence characters who win on Cognition deal negligible strain. The system punishes characters who argue well but speak softly. Consider: base strain on loss should be margin + 1, with Presence as bonus on top. This ensures every loss hurts regardless of the winner's Presence.]

[FINDING R-07: The Conviction Track compromise zone (3–7) is very wide. In a 5-exchange debate starting at 5, the most likely outcome is compromise regardless of debater quality. Consider: narrowing the compromise zone (4–6) or reducing the threshold distance (≥7 instead of ≥8 for outright win).]

---

# PHASE 7: CUMULATIVE PATCH LIST (Post-Retest)

| ID | Description | Status |
|---|---|---|
| D-01 | Genre weight derived from Question + Ethical Mode, fixed at setup | APPROVED — tested in retest |
| D-02 | Attunement read calibration table, Attunement only (no History), misleading on failure | APPROVED — tested, failure consequence worked |
| D-03 | Conviction Track: 0–10, thresholds, movement = floor(margin × weights) − resistance | NEEDS REVISION per R-05 (resistance as floor not tax) |
| D-04A | Base strain +1 per exchange loss | APPROVED — strain rate correct |
| D-04B | Rattled = −2D + no Focus defence | APPROVED — not triggered in retest but math checks out |
| D-04C | Concentration −1 extra on loss | APPROVED — forced Regroup at right moment |
| D-05 | Three interaction types: Clash / Competition / Divergence | NEEDS REVISION per R-04 (remove Competition loser bonus) |
| D-06 | Ties produce mutual strain and +1 toward initiative holder | NOT TESTED — no ties in retest |
| D-07 | Focus as passive reduction: floor(Focus/2) | APPROVED — simplified, scaled correctly |
| D-08 | Presence modifier: floor((Presence−3)/2) | APPROVED |
| D-09 | Memory bonus: fixed +2D for specific citation, any genre | APPROVED — used in retest, clean |
| D-10 | Composure = Poise + Bonds + 3 | APPROVED — range 5–17, typical 9–11 |
| R-01 | Initiative stays with holder after Divergence | NEW — needs confirmation |
| R-02 | Forfeited exchanges: fixed +1 tracker toward non-forfeiting side | NEW — needs confirmation |
| R-04 | Competition: remove loser's +1 tracker bonus. Same as Clash but reduced strain. | NEW — revision of D-05 |
| R-05 | Resistance as floor: margin ≤ resistance → 0 movement. Margin > resistance → margin − resistance. | NEW — revision of D-03 |
| R-06 | Base strain = margin + 1 (not margin + Presence + 1). Presence adds ON TOP. | NEW — revision of D-04A |
| R-07 | Narrow thresholds: outright win at ≥7 (not ≥8) and ≤3 (not ≤2). | NEW — revision of D-03 |

---

*End of stress test v1. 17 findings identified pre-test. 7 additional findings from retest. 10 patches proposed. 4 patches need revision. System is functional but requires a second stress test pass after revisions are applied.*
