# VALORIA STRESS TESTS — BATCH 6
## Remaining Untested Mechanics
### Date: 2026-03-27 | Model: Sonnet 4.6

Mechanics covered: History Resonance, Certainty Blast Radius (Push), Diagnosis (standalone), Co-Movement Cards (BG), Impression Track, Reading Exchange, Defection (gap status check), Fortification, BG Turn Structure, Victory Conditions, Hollow Victory.

---

## B6-01 — History Resonance (M-003 extension, stage3 §5.8)

**Mechanic:** When temporal co-movement fires during a Thread op, a relevant History resonates. Next use of that History: +1 bonus die. If bonus die shows 1: ThS −1.

**Mode:** TTRPG | Temporal: CROSS | Tracks: TD/ThS | Archetypes: Practitioner

### Mode A — Isolation

**Trigger rate:** "Fires approximately 1–2 times per session at typical play rates." This is GM-called, not auto. The constraint "only one Resonance active per History at a time" prevents stockpiling.

**Probability analysis — bonus die risk:**

The bonus die shows 1 → ThS −1 with P = 10%.

Expected ThS cost per Resonance: 0.1 per discharge.
Over 30 sessions at 1.5 Resonances/session: 45 total Resonances × 0.1 = 4.5 expected ThS loss. Confirmed by ruleset note ("~4–5 additional CD over 30 sessions").

**Is the bonus worth the risk?**

+1 bonus die to any roll = approx. +0.333 expected net successes at TN7. On a roll where the character is already rolling 8D (E(net)=2.67), the bonus is ~12% improvement. On a tight Ob 3 roll: marginal but occasionally decisive.

Risk = 10% chance of −1 ThS per discharge. ThS starts at 20. If depleted to 0: Crisis state. Expected sessions to Crisis from Resonance alone (at 4.5 ThS loss per 30 sessions) = 30/4.5 × 20 ≈ 133 sessions. **Resonance alone is not a significant ThS drain.** The risk is real but mild — as documented.

**Interaction with Forks and History investment:** Characters with high-investment Histories (8–10 points) will trigger Resonance more often (more Thread ops using those Histories). Heavily-invested practitioners face slightly more Resonance risk. Not imbalanced — the tradeoff is built into the history investment.

**Edge case: Resonance pending during a critical moment.** A practitioner with Resonance pending (bonus die available) approaches a high-stakes roll. They spend the Resonance. Result: if 1 appears on bonus die, ThS −1 at worst possible moment (already stressed situation). P = 10%. Not a problem — the mechanic is intentionally risky.

**Findings:**

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| B6-HR-01 | P3 | "Fires approximately 1–2 times per session" is GM judgment with no mechanical trigger. Inconsistent tables will see wildly different Resonance rates. | Add concrete trigger: "Resonance fires when temporal co-movement produces degree = CROSS (past or future temporal effect). GM may waive for non-Thread-touching temporal effects." |

---

## B6-02 — Certainty "Push" / Blast Radius

**Mechanic (from CP14 glossary):** Push = re-roll all failed dice once after any non-Thread roll. Costs −1 Certainty. Once per roll.

**Mode:** TTRPG | Temporal: PRES | Tracks: CERT | Archetypes: all

### Mode A — Isolation

**Push probability value:**

Push = re-roll all dice that did not show 7+ or 1 (the "failed" dice = 2–6 results). On N dice pool, expected failed dice = N × 0.5 (the 2–6 range). Re-rolling those at TN7: each adds expected 0.333 net successes.

*Example: 8D pool. Expected failed dice = 4. Re-roll 4D: E(additional net) = 4 × 0.333 = 1.33.*

So Push adds ~1.33 expected net successes to an 8D pool. At Ob 3, this can shift a likely Partial into a likely Success. The benefit is substantial — nearly equivalent to adding 4 dice to the original pool.

**Cost:** −1 Certainty. Certainty range: Spirit (1–7). At Spirit 3 (typical): 3 Certainty total. Three Pushes = Certainty 0 = Rendering Crisis. **Push is a high-value, limited resource.**

**Restriction: Thread operations excluded.** Prevents Push from amplifying the already-powerful Thread op economy.

**"Blast radius" framing:** The term "blast radius" in the handoff note appears to refer to how Certainty depletion (from Pushing aggressively) cascades into TS growth pressure and Rendering Crisis. At Certainty 0, the practitioner hits Rendering Crisis. The "blast" is the downstream consequence chain of using Push heavily.

**Chain analysis: Push → Certainty 0 → Rendering Crisis → forced narrative resolution → ThS implications.**

A practitioner using Push aggressively (3× in one session, Spirit 3) hits Rendering Crisis immediately. Crisis resolution requires: revise a Belief, withdraw, or find new framework. This forces a narrative pivot mid-session. If the practitioner ignores the crisis and continues Thread ops: +1D ThS per operation (newly added rule). 3 Thread ops during crisis = ThS −3. This is the blast radius: aggressive Pushing → crisis → compounding ThS cost if crisis is ignored.

**P(Rendering Crisis from Push alone, Spirit 3, 1 session):**

If the player uses Push 3× in one high-stakes session: Certainty 0. P = 100% (deterministic). The question is whether 3 Pushes is "likely" play. In a crisis scene, yes — players will spend Certainty to succeed.

**Findings:**

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| B6-PU-01 | P3 | "Blast radius" of Push → Rendering Crisis is the intended pressure valve. The cascade (Push → Crisis → ThS cost if ignored) is functional and well-designed. No fix needed — note for GM that Push is a session-arc resource, not per-scene. | Document in §4.6 or GM reference: "Push is a Certainty trade. Three Pushes at Spirit 3 triggers Rendering Crisis. GMs should signal when players approach this threshold." |
| B6-PU-02 | P2 | Push is not restricted to non-practitioners. A non-practitioner spending Certainty (start = Spirit) has no TS growth pathway — Certainty loss has no upside for them. For non-practitioners, Push is purely negative (risk without transformation benefit). | Note in §1 or §4.6: "Non-practitioners who reach Certainty 0 from Push do not enter Rendering Crisis — they enter a state of existential doubt. Narrative consequence only; no mechanical ThS effect. GMs should treat this as a character-defining moment rather than a game mechanic." |

---

## B6-03 — Diagnosis (Standalone)

**Mechanic:** No roll. Contact round at Priority 4. GM exchange revealing: Ob, residue, Gap risk, Taint trace, temporal weight. Mandatory before FR and Past-Oriented Pulling (penalties for skipping).

**Mode:** TTRPG | Temporal: PAST/PRES | Tracks: none directly | Archetypes: Practitioner

### Mode A — Isolation

**Diagnosis is a no-roll information mechanic.** All probability concerns are downstream (how Diagnosis affects subsequent rolls).

**Ob-setting:** Diagnosis tells the practitioner the Operation Ob. This allows tactical decisions: proceed (low Ob), abort (high Ob), Call a Knot for dice bonus, or use Inspiration. The mechanic functions as an information-gathering phase, not a gating roll.

**"Mandatory" penalty analysis:**

Skip FR without Diagnosis: +2 Ob + automatic Gap on Failure.
At Ob 3 (typical FR): becomes Ob 5. P(Success) at 8D TN7 Ob5: ~17.8%. P(Failure) at Ob5: ~14%. Failure = automatic Gap. P(Gap from skipped Diagnosis) = P(Failure) = ~14% on an 8D pool. Gap creation → TT escalation → potentially serious.

Skip Past-Oriented Pulling without Diagnosis: +3 Ob + temporal Gap on Failure. Ob 2 POP becomes Ob 5. P(Failure) = 14% → temporal Gap. A temporal Gap is worse than a standard Gap (higher TT consequence presumably). **Skipping Diagnosis on POP is genuinely dangerous.**

**Contact window cost:** Diagnosis costs one contact round. Contact Duration = Focus score (1–7). At Focus 3: 3 contact rounds. Diagnosis consumes Round 1 (priority 4). Remaining: 2 contact rounds for operations. This is a real cost for low-Focus practitioners.

*Low-Focus practitioner (Focus 2): only 2 contact rounds. Diagnosis uses Round 2 (earliest available). Remaining: Round 3+ (contact ends at Focus+1 = 3). One operational round available after Diagnosis. If the operation requires 2 rounds: must re-Leap.*

**P1 gap check:** Does Diagnosis extend the contact window in any circumstance? No. Does it fire if the practitioner can't afford the round? Yes — it "does not shorten the contact window" (the round still counts). This is fine.

**Findings:**

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| B6-DX-01 | P3 | Low-Focus practitioners (Focus 2) face a real tradeoff: Diagnosis on Round 2 leaves only 1 operational round. They may skip Diagnosis to get 2 operational rounds, accepting +2 Ob risk. This is intended pressure (Focus governs Thread contact) but should be explicit. | Add note in §5.3: "Low-Focus practitioners may choose to skip Diagnosis, accepting the Ob penalty. This is a legitimate tactical choice, not a rules violation." |
| B6-DX-02 | P3 | Diagnosis result ("set Ob") is based on GM judgment. No calibration guidance for GMs. Consistent Ob-setting is critical for session-to-session fairness. | §13/GM Tools: add Diagnosis Ob reference table (e.g., Ob 1 = simple configuration, no prior working; Ob 3 = complex or previously worked; Ob 5 = contested, Taint 5+, active Gap nearby). |

---

## B6-04 — Co-Movement Cards (BG)

**Mechanic:** 20-card deck (10 designed, 10 editorial pending). Each card: Temporal + Epistemic + Actual effect. Draw one per Thread operation regardless of result. Apply all three.

**Mode:** BG | Temporal: CROSS | Tracks: TT/TC/IP + territory stats | Factions: all

### Mode A — Isolation

**Draw rate:** 1 card per Thread operation in BG. Thread operations are Priority 1 per round. A faction performing 1 Thread op/season = 1 card/season. Over 16-round game: 16 cards drawn (if one faction consistently operates). **Less than 1 full deck cycle per standard game.** This is good — cards don't repeat frequently.

**Card effect analysis (CM-01 through CM-10):**

| Range | Temporal effects | Epistemic effects | Actual effects |
|---|---|---|---|
| TT change | −3 to +2 (range of 5) | Information reveal/hide/shuffle | Territory Prosperity ±1, Fortification −1, faction stat changes |
| TC change | −1 to +1 | — | — |
| IP change | −1 to +1 | — | — |
| Nothing | CM-05 Actual=nothing, CM-07 Temporal=nothing | CM-03/05/06/08/09/10 | CM-03/06/07/09/10 |

**Clock pressure from cards:** 10 cards; net TT from all 10 = (−1−1+1−1−1+0+0+0+2−3) = −4. Net TC = (0+1+0+0+0+0+0+0+0+0) = +1. **The designed 10 cards are net TT-negative (stabilising) and TC-neutral.** This matters for game balance — Thread ops in BG mode slightly reduce TT rather than increase it (design intent: operations by competent practitioners help manage Thread pressure).

**P-01 compliance:** Every card has at least one effect that bridges all three dimensions (Temporal, Epistemic, Actual). CM-07 has no Temporal effect — only Epistemic and Actual. **CM-07 potentially violates P-01 (inseparability requires co-movement in all three dimensions).** P-01: "co-movement mandatory." If CM-07's Temporal=nothing means no temporal co-movement fired, this is a P-01 violation.

**Mitigation check:** The co-movement is in the *structure* (all three effect slots exist), not necessarily requiring all to fire. A "nothing" result may mean the temporal dimension was unaffected, not that co-movement didn't happen. The canon guard may accept this if "nothing" is interpreted as "temporal dimension unaffected = temporal co-movement produced no net change" rather than "no temporal movement occurred." This is ambiguous.

**10 missing cards (CM-11–CM-20) gap:** These are editorial pending. The simulation cannot validate balance until all 20 cards exist. The net effect of the deck (TT/TC/IP balance, epistemic information distribution) is currently unknown for the complete deck.

**Findings:**

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| B6-CM-01 | P2 | CM-07 has Temporal=nothing. May violate P-01 if "nothing" means no temporal co-movement occurred. | Canon-guard check: clarify that "nothing" in Temporal slot = "temporal substrate unaffected this operation" (a valid outcome of co-movement). Add note to B7: "A 'nothing' entry means co-movement produced no observable effect in that dimension, not that co-movement was absent." |
| B6-CM-02 | P2 | 10 cards missing (CM-11–CM-20). Full deck balance unvalidatable. Currently net TT=−4 from 10 cards. | Flagged as BG-E-01 (already in editorial register). Deck must be completed before Phase 3 gate. |
| B6-CM-03 | P3 | No reshuffle rule specified. What happens when the 20-card deck is exhausted? In a 16-round game with one faction operating each round = 16 draws. With multiple factions: deck could exhaust mid-game. | Add to B7: "When the Co-Movement deck is exhausted, shuffle discards and redraw." |

---

## B6-05 — Impression Track

**Mechanic:** 0–5 NPC relationship scale. Advances through meaningful scenes (no roll). At 5: triggers significant NPC action on character's behalf. NPC at 5 can become Inspiration focus.

**Mode:** TTRPG | Temporal: CROSS (past investment → future trigger) | Tracks: none | Archetypes: all

### Mode A — Isolation

**Advancement rate:** No roll specified — purely narrative (GM confirms scenes are "meaningful"). No rate cap found beyond implicit session pacing. A character with good roleplay could theoretically advance an Impression Track 5 in 5 sessions.

**Trigger at 5:** "Significant NPC action on character's behalf." This is deliberately vague — GM designs the action appropriate to the NPC. Mechanically light. The value is narrative (an ally NPC takes independent action), not mechanical (no stat bonus, no dice).

**Interaction with Inspiration:** NPC at Impression 5 can become an Inspiration focus. Connecting Impression Track to Inspiration economy creates a mechanical reward for investing in relationships. This is elegant.

**Gaps:**

1. No rule for what happens if the NPC dies before reaching 5, or is permanently alienated. Does the track reset? Does it transfer?
2. No rule for NPC Impression Track decay — does a relationship maintain at 5 without maintenance, or does it degrade?
3. No mechanic for what "significant NPC action" means mechanically — entirely narrative.
4. The Knot system handles ongoing relationship mechanics (strain, crisis). Impression Track handles relationship *development* toward a threshold. **These are parallel systems for NPC relationships.** A PC's significant NPC relationship could be both an Impression Track (advancement toward trigger) and a Knot (strain/calling). Interaction between systems is unspecified.

**Impression Track + Knot collision:** Could an NPC at Impression 5 AND with a Knot in Crisis simultaneously? Yes — both systems track independently. A Knot in Crisis means "the connected entity takes action — confrontation, departure, or betrayal." An Impression Track at 5 triggers "significant action on character's behalf." If both fire simultaneously: the NPC both acts for the character AND acts against them? This is a contradiction that needs resolution priority.

**Findings:**

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| B6-IT-01 | P2 | Impression Track + Knot Crisis can fire simultaneously with contradictory NPC actions. No resolution priority. | Add: "If an NPC reaches Impression Track 5 while their Knot is in Crisis, the Crisis takes precedence. The Impression Track trigger is deferred until the Crisis is resolved." |
| B6-IT-02 | P2 | No rule for Impression Track if NPC dies or is permanently removed. | Add: "If the NPC dies before Impression 5 is triggered, the PC may convert the partial track to CP at 1 CP per 2 full track points accumulated (minimum 1 CP)." |
| B6-IT-03 | P3 | No decay rule. Impression Tracks presumably hold their value indefinitely. | Confirm: Impression Tracks do not decay unless a scene contradicts the relationship. GM discretion to set back by 1 for major relationship rupture (not requiring session maintenance like Knots). |

---

## B6-06 — Reading Exchange

**Mechanic:** Social perception action, first round of contact only. Pool: Attunement + History bonus. TN7. Not a Debate exchange. Degrees: OW = detailed state + 2D on first 2 Exchanges; Success = emotional state + 1 tell + 1D on first Exchange; Partial = surface affect; Failure = no info + target notices scrutiny.

**Mode:** TTRPG | Temporal: PRES | Tracks: none | Archetypes: all

### Mode A — Isolation

**Pool range:** Attunement 1–7 + History. Typical: Attunement 3, History 6 pts = 3 + 9 = 12D. At 12D TN7: E(net) = 4.0. P(OW at Ob1) = 84%. **Reading Exchanges are almost always Overwhelming for invested social characters.**

*Wait — Reading Exchange has no Ob specified.* It uses degrees (OW/Success/Partial/Failure) but doesn't state an Ob. The degrees table shows outcomes based on degree, not on net successes vs Ob. This means: the result is determined by net successes alone, with implicit Ob structure:
- OW = net ≥ some threshold?
- Or does the system use a different interpretation?

Re-reading: the degrees table doesn't use "Ob" language. It uses "degree" language — which in Valoria maps to net success count. Looking at the standard degree table: Partial = net > 0 but < Ob; Success = net ≥ Ob; OW = net ≥ 2×Ob. Without a stated Ob, the mechanic is incomplete.

**P1 gap — B6-RE-01: Reading Exchange has no stated Ob. Without Ob, the degree table cannot resolve.**

Possible intent: Reading Exchange always uses Ob 1 (routine perception check, success is finding *something*). At Ob 1: OW = net ≥ 2, Success = net ≥ 1, Partial = implied as net = 0? But "Partial" in the table shows "surface affect only" — which requires some success. This suggests Partial = partial success (net ≥ 0 but not full).

Alternatively: Reading Exchange uses a custom degree structure — not the standard Ob-based system. The degree descriptions suggest this: "Partial = surface affect (no Exchange bonus)" is a usable outcome, not a "success with complication." This may be an intentional non-Ob roll.

**Recommended fix:** State explicitly "Reading Exchange uses Ob 1. Partial is net > 0 but < Ob (i.e., net = 0 would be Failure, net = 1 = Partial if Ob 2 or Success if Ob 1)." Or alternatively: "Reading Exchange rolls at Ob 1; degrees map as: net ≥ 2 = Overwhelming; net = 1 = Success; net = 0 = Partial; net < 0 = Failure."

**Bonus interaction with Inspiration (post B5 fix):** Reading Exchange is not a Thread operation. Inspiration may be spent. A social character with Inspiration "Almud's court" spending on a Reading Exchange vs Almud: pool = 12D + Spirit bonus (e.g., 4D) = 16D. OW at Ob 1 = near-certain. This is appropriate — expert social characters should read opponents reliably.

**Failure consequence — target notices scrutiny:** "The opponent is aware of being read." This is a meaningful social consequence: the opponent knows the character attempted perception. They may become guarded (Ob increase on subsequent social rolls), or they may use the information strategically. No mechanical specification of how "noticed scrutiny" is expressed. P3 gap — narrative-only consequence is fine, but GM guidance helps.

**Findings:**

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| B6-RE-01 | **P1** | Reading Exchange has no stated Ob. Cannot determine degree boundaries (OW vs Success vs Partial vs Failure) without it. | Add to §9.4: "Reading Exchange uses Ob 1. Degrees: net ≥ 2 = Overwhelming; net = 1 = Success; net = 0 = Partial; net ≤ −1 = Failure." |
| B6-RE-02 | P3 | "Target notices scrutiny" on Failure has no mechanical expression. | Add: "On Failure, the GM may have the opponent react with increased guardedness — treat as Disposition one step more hostile for the remainder of the scene." |

---

## B6-07 — Defection / Cross-Faction Recruitment

**Status check:** G-036 ("Defection / cross-faction recruitment") is a P2 design gap in the consolidated gap register — marked "Design needed." Not present in any compilation stage.

**Finding:** Defection mechanics do not yet exist. Coverage matrix entry: NOT STARTED — DESIGN PENDING.

No simulation possible until design is completed. Confirm gap remains open.

---

## B6-08 — Fortification

**Mechanic:** Territory stat (implied 0–5 from siege rules). Sieges require Fortification 2+. Assaulted directly at Fortification 0–1. Built via Domain Actions (unspecified construction time). Reduced via Sappers (Intel vs Ob=Fort+1) and Dissolution Weaving.

**Mode:** TTRPG/BG | Temporal: PRES/FUT | Tracks: TT (from siege Einhir) | Factions: all | Archetypes: Faction Leader

### Mode A — Isolation

**Fortification scale:** Referenced as 0–5 (Fortification 2+ triggers siege rules; 0–1 = direct assault). Stage7 territories presumably define starting values. Stage8 gives combat interactions.

**Ob calculations with Fortification:**

| Fortification | Assault Ob | Starve Ob | Sapper Ob | Thread Bombardment Ob |
|---|---|---|---|---|
| 1 | 3 | 1 | 2 | 1 |
| 2 | 4 | 2 | 3 | 2 |
| 3 | 5 | 3 | 4 | 3 |
| 4 | 6 | 4 | 5 | 4 |
| 5 | 7 | 5 | 6 | 5 |

At Military 4 (pool Martial + Commander Coordination, ~8D): Assault vs Fort 4 (Ob 6): P(Success+OW at 8D Ob6) ≈ 1.2% + 14.2% = ~15%. **High-fortification territories are extremely difficult to assault.** Starve (Ob 4) at 8D: P(Success+OW) ≈ 34%. Sappers (Intel pool, Ob 5) at Intel 5 (6D): P(Success+OW) ≈ 7.5%. **Starvation is the most viable siege strategy against high-fortification targets.**

**Thread Bombardment:** Weaving at Relational+ scale, Ob = Fort level, TT +2 regardless. At Fort 3 (Ob 3): practitioner pool 8D+TPS. Spirit 4+TPS 3 = 7D. P(Success) at 7D Ob 3 = 41+5 = 46%. On success: garrison Cohesion −2. On Failure: practitioner ThS −3. **Thread Bombardment is a high-risk option.** ThS −3 is a massive cost (~15% of total ThS budget). The failure cost heavily discourages use unless the practitioner has strong pool and manageable ThS.

**Building Fortification:** Stage8 §8.4 siege rules don't specify construction time or cost. The "1 season construction" cost mentioned only for Artillery. Fortification building presumably requires a Domain Action with Wealth cost. **Gap: Fortification construction rules not found in compilation stages.**

**BG mode Fortification:** Stage_bg §B6 Siege references "Fortification 2+" for siege triggers. Fortification stat presumably on territory sheets. No Fortification construction order in B5 Orders — not a placeable order. **Gap in BG: how does Fortification increase in board game play?**

**Findings:**

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| B6-FO-01 | P2 | Fortification construction mechanism not found in TTRPG compilation stages. Siege rules reference it but it can only be reduced, not built up, in current text. | Add to §8.4 or §faction Domain Actions: "Construct Fortification Domain Action: Wealth Ob = target Fortification level + 1. One season construction. Max Fortification = 5." |
| B6-FO-02 | P2 | BG mode has no Fortification construction order. Territory Fortification can only decrease (via sappers/siege), creating one-directional attrition. | Add to B5 Orders: "FORTIFY order (available to controlling faction): Wealth Ob = target Fortification level + 1. Success: Fortification +1 (max 5). Cannot Fortify while under siege." |

---

## B6-09 — BG Turn Structure

**Mechanic:** 6-phase round (Season Card → Planning → Intel Reveal → Order Resolution → Seasonal Accounting → Cleanup). Order Resolution Priority 1–6. 12–16 standard rounds.

**Mode:** BG | Temporal: FUT | Tracks: all global | Factions: all

### Mode A — Isolation

**Simultaneous declaration mechanics:**

All orders placed face-down, revealed simultaneously. Lowest Stability places first, highest Stability places last. This creates information asymmetry: high-Stability factions see where others have placed before committing (within the placement order). **The rule says orders are placed face-down — but placement order reveals territory choices before reveal.** A high-Stability faction places last: they see which territories have tokens (but not what orders). This is meaningful information.

**Contested resolution:** "Both roll simultaneously. Apply results simultaneously." With 5+ player factions and contested territories, a single Order Resolution phase could have multiple simultaneous battles in different territories all resolving at once. This is complex but tractable — each territory resolves independently.

**Phase 3 — Intel Reveal:** Niflhel reveals "information-gathering result from last season." This means Intel orders produce results that are publicly delayed by one season. A faction that ran Intel order in Season 4 reveals results in Season 5 Phase 3. This creates a 1-season intelligence lag — appropriate for the setting.

**Priority 6 conflict with Decree/Parliamentary Manoeuvre:** "Take effect at next accounting if timing is ambiguous." This deferred resolution creates a 1-season lag for Crown Decrees. A player using a Decree to block an opponent's action this season may find the Decree takes effect next season — too late. GMs/players need clarity on when "timing is ambiguous."

**Clock accounting timing:** Clocks update at Phase 5 (Seasonal Accounting). Thread ops fire at Priority 1 in Phase 4. The TT change from Thread ops applies *within* Phase 4, before accounting. **A Thread op that pushes TT to 100 mid-Phase 4 triggers THE RUPTURE immediately** (game-end triggers apply "immediately" per B10). This requires Phase 4 to pause mid-resolution for a game-end check. **No explicit mid-phase game-end check rule exists.**

**Findings:**

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| B6-TS-01 | P2 | Mid-phase game-end check not specified. TT reaching 100 from a Thread op in Phase 4 should trigger THE RUPTURE immediately, but Phase 4 hasn't completed. | Add to B4: "If a game-end trigger (TT/TC/IP = 100) fires during Phase 4 Order Resolution, complete the current priority tier, then apply the endgame event before continuing to Phase 5." |
| B6-TS-02 | P3 | Decree/Parliamentary Manoeuvre at Priority 6 with "next accounting if timing ambiguous" — ambiguity condition not defined. | Clarify: "Timing is ambiguous when the Decree targets an effect that was already determined in Priorities 1–5. If the Decree targets a Phase 5 accounting change, it takes effect this season." |

---

## B6-10 — Victory Conditions

**Mechanic:** Per-faction victories + shared survival condition (TT/TC/IP all < 80). Multiple win paths. Collective loss if shared survival fails.

**Mode:** BG | Temporal: FUT | Tracks: TT/TC/IP + FSTAT | Factions: all

### Mode A — Isolation

**Shared survival condition analysis:**

TT < 80 AND TC < 80 AND IP < 80 simultaneously when game-end fires.

**Probability a random game state meets shared survival at Round 16:**

Starting TT = 28. If TT rises 2/season average (typical with 2–3 Thread ops/season): TT at Round 16 ≈ 28 + 32 = 60. Under 80. Probable survival.

TC: Church AI drives TC. TC rising ~3/season (active Church): TC at Round 16 ≈ 48. Under 80 if no escalation events.

IP: Hidden, rising from Schoenland trade disruption and Altonian ambitions. Harder to estimate without full event deck simulation. Likely mid-range (~40–60) in standard play.

**Finding: Shared survival is likely achievable in standard play.** The game doesn't feel like it's designed for collective loss to be common — rather, collective loss is a dramatic failure condition when players ignore clock management. This is correct design.

**Faction victory condition tensions:**

Church victory (TC ≥ 80 + territorial control) directly conflicts with shared survival (TC < 80). **The Church cannot achieve its victory condition while shared survival is met.** Church wins only if shared survival has already failed — which means collective loss is triggered simultaneously. This is a design contradiction: Church can never "win" in the normal sense.

Reading more carefully: "If shared survival is not met: no per-faction victory counts... unless one of the transcendent endgame paths is achieved." The Church's TC ≥ 80 victory is only accessible if shared survival fails — but then per-faction victories don't count. **The Church's stated victory condition is therefore inaccessible in normal play unless THE HOLY STATE endgame fires and the Church controls the required territories AND the Constitutional Resistance path isn't triggered.**

This is likely intentional — the Church is designed as a destabilising actor, not a "winnable" faction in standard play. The Church's play style drives TC upward (threatening shared survival) as leverage rather than a genuine path to victory.

**Varfell victory (Information Supremacy):** Involves 3 artefacts + Southernmost integration condition. The Southernmost integration condition for victory needs final wording (editorial pending per register). **Cannot fully simulate.**

**2-player adjustment validity:** NPC factions execute 2 orders instead of 3 at 2 players. Clock threshold delays: +1 season persistence. **Effect on balance:** 5 NPC factions × 1 fewer order = 5 fewer orders/season. This substantially reduces clock pressure. At −5 orders/season over 16 seasons = 80 fewer order activations, many of which would have driven TT/TC/IP. The 2-player game runs significantly slower-clock than stated. This may undermine the tension of the base mechanics.

**Findings:**

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| B6-VC-01 | P2 | Church victory condition (TC ≥ 80) is inaccessible in normal play — requires shared survival failure which prevents per-faction victories. Church is de facto an unwinnable faction OR only wins via THE HOLY STATE endgame trigger. | [EDITORIAL] Confirm Church is intentionally unwinnable in standard play (acts as threat-actor). If unintentional, redesign: "Church wins if TC ≥ 60 and controls Himmelenger + Valorsplatz at game-end, even under shared survival." |
| B6-VC-02 | P2 | Varfell victory condition incompletely specified (Southernmost integration condition pending editorial). | Flagged BG-E-01 equivalent — editorial required. |
| B6-VC-03 | P3 | 2-player NPC order reduction (2 instead of 3) dramatically reduces clock pressure. The core game tension may be absent in 2-player. | Recommend: 2-player NPC AI runs full 3 orders but with Clock threshold delay of +1 season. Remove order reduction; keep only threshold delay. |

---

## B6-11 — Hollow Victory

**Search result:** "Hollow victory" not found in any compilation stage or CP14. Checking BG B10 for related concept.

The closest match in B10: "If shared survival condition is not met: no per-faction victory counts. The game ends in collective loss unless one of the transcendent endgame paths is achieved." The "collective loss despite individual faction success" scenario is what would constitute a hollow victory — a player achieves their faction condition but the world is destroyed.

The ruleset calls this a "collective loss" rather than "hollow victory." The concept exists but the term is not used. The handoff note may have been using informal terminology.

**Simulation analysis of collective loss + individual faction success:**

Scenario: Guilds player achieves Economic Dominance (required Wealth stats) in Round 14. Simultaneously, TT = 85 at accounting (shared survival fails, TT ≥ 80). Game-end trigger fires at Round 16 by standard completion. At accounting: shared survival = FAIL. Result: Guilds' individual victory does not count. Collective loss.

The player achieved their goal mechanically but the world-state prevents it counting. This is the "hollow victory" experience — and the ruleset explicitly doesn't reward it. **This is correct per P-01 compliance: inseparability means individual gain doesn't survive collective Thread failure.**

**Findings:**

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| B6-HV-01 | P3 | "Hollow victory" term not in ruleset; concept exists as "collective loss despite individual faction achievement." Experienced players may be confused when their faction "wins" but the game calls it a loss. | Add to B10: "Hollow Outcome: If a faction meets its victory condition but shared survival fails, this is recorded as a Hollow Outcome — a faction that thrived while the world deteriorated. Not a win. The Hollow Outcome is a narrative end-state, not a mechanical victory." |

---

## COVERAGE MATRIX UPDATES

| Test ID | Mechanics | Mode | Temporal | Tracks | Status | Findings |
|---------|-----------|------|----------|--------|--------|---------|
| B6-01 | History Resonance | TTRPG | CROSS | ThS | Complete | B6-HR-01 (P3) |
| B6-02 | Certainty / Push blast radius | TTRPG | PRES | CERT | Complete | B6-PU-01 (P3), B6-PU-02 (P2) |
| B6-03 | Diagnosis (standalone) | TTRPG | PRES/PAST | none | Complete | B6-DX-01/02 (P3) |
| B6-04 | Co-Movement Cards (BG) | BG | CROSS | TT/TC/IP | Complete | B6-CM-01 (P2), B6-CM-02 (P2), B6-CM-03 (P3) |
| B6-05 | Impression Track | TTRPG | CROSS | none | Complete | B6-IT-01/02 (P2), B6-IT-03 (P3) |
| B6-06 | Reading Exchange | TTRPG | PRES | none | Complete | B6-RE-01 **(P1)**, B6-RE-02 (P3) |
| B6-07 | Defection | — | — | — | NOT STARTED — design pending (G-036) | — |
| B6-08 | Fortification | TTRPG/BG | PRES/FUT | TT | Complete | B6-FO-01/02 (P2) |
| B6-09 | BG Turn Structure | BG | FUT | all global | Complete | B6-TS-01 (P2), B6-TS-02 (P3) |
| B6-10 | Victory Conditions | BG | FUT | TT/TC/IP/FSTAT | Complete | B6-VC-01 (P2 + EDITORIAL), B6-VC-02/03 (P2/P3) |
| B6-11 | Hollow Victory | BG | FUT | — | Complete (concept found as "collective loss") | B6-HV-01 (P3) |

---

## SUMMARY

| Priority | Count | Items |
|---|---|---|
| **P1** | 1 | B6-RE-01 (Reading Exchange missing Ob) |
| P2 | 9 | B6-PU-02, CM-01/02, IT-01/02, FO-01/02, TS-01, VC-01/02/03 |
| P3 | 8 | B6-HR-01, PU-01, DX-01/02, CM-03, IT-03, RE-02, TS-02, HV-01 |
| Editorial | 1 | B6-VC-01 (Church victory condition intent) |
| Design pending | 1 | B6-07 Defection (G-036) |

