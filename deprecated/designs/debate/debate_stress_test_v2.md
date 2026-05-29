<!-- DEPRECATED: 2026-04-09 — SUPERSEDED BY designs/contest/social_contest_system_v2.md — test of superseded debate system. Do not use as a mechanical reference. Retained for audit trail only. -->

# DEBATE SYSTEM STRESS TEST v2

## Model: Opus 4.6
## Input: All D-01 through D-10 patches + R-01 through R-07 revisions applied
## Method: Compile patched system → Isolation retest → Full scenario retest → New findings → Final patches

---

# PHASE 0: COMPILED PATCHED SYSTEM

All mechanics as they stand after v1 patches and revisions.

## 0.1 Game Master Setup

1. **Question** determines primary genre (Past / Present / Future).
2. **Audience** identified by faction(s) present.
3. **Genre weights** derived mechanically:
   - Primary genre: ×1.0
   - Other two genres: ×0.5 base
   - Audience ethical mode adjusts ONE genre by +0.5:
     - Virtue ethics (Crown): Present +0.5
     - Divine command (Church): Past +0.5
     - Categorical imperative (Hafenmark): Past +0.5
     - Consequentialism (Varfell): Future +0.5
     - Moral relativism (Guilds): Game Master picks based on context
     - Rawlsian social contract (Restoration): Future +0.5
   - Weight range: 0.5 / 1.0 / 1.5. Never 0, never above 1.5.
4. **Orientation weights** fixed: Revealing ×1.0, Obscuring ×0.75. (Invertible for specific scenarios.)
5. **Conviction Track** starts at Game Master-set position (0–10). Typical: 4–6 for neutral.
   - Side A wins at ≥7 (R-07 revision). Side B wins at ≤3.
   - Compromise zone: 4–6.
   - **Audience resistance** = average Stability of represented factions, round up. Typical: 1–3.
   - **Movement formula (R-05 revision):** If margin × genre_weight × orientation_weight ≤ resistance → 0 movement. If greater → (margin × genre_weight × orientation_weight) − resistance, rounded down.
6. **Weights are fixed at setup.** No dynamic shifting. Recorded in ledger.
7. **Stakes** defined: consequences for each side winning, compromise, total loss.

## 0.2 Initiative

- Exchange 1: higher Presence speaks first.
- Subsequent: transfers to exchange winner.
- Tie: stays with holder.
- After Divergence (R-01): stays with holder.

## 0.3 Exchange Structure

**Step 1 — Read:** Both orators roll Attunement alone (no History). TN 7, Ob 1.

| Net | Output |
|---|---|
| Failure (0) | Misleading signal — one genre identified as strong that is actually weak. |
| Partial (1) | Primary genre identified. No orientation signal. |
| Success (2) | Primary genre + orientation preference identified. |
| Overwhelming (3+) | Genre + orientation + one specific detail (swing faction, emotional state, impatience). |

**Step 2 — Choose:** Each orator selects genre (Past / Present / Future) and orientation (Revealing / Obscuring).

**Step 3 — Argue:** Initiative holder declares argument and rolls first. Respondent hears, then declares and rolls.
- **Pool:** Cognition + History bonus, TN 7.
- **Memory bonus:** +2D when citing a specific, named, verifiable claim. Binary — qualifies or doesn't. Any genre.

**Step 4 — Resolve:** Depends on interaction type.

**CLASH (same genre, opposite orientation):**
- Compare successes. Higher wins. Margin = difference.
- Tracker: if margin > resistance → Δ = margin − resistance toward winner's position. If ≤ resistance → 0.
- Apply genre weight and orientation weight to margin BEFORE resistance comparison: effective_margin = floor(margin × genre_weight × orientation_weight).
- Strain to loser: margin + 1 + winner's Presence modifier (R-06 revision: base is margin + 1, Presence adds on top).
- Loser's Focus defence: reduce strain by floor(Focus / 2). Passive, no roll.

**COMPETITION (same genre, same orientation):**
- Compare successes. Higher wins. Margin = difference.
- Tracker: same formula as Clash. No loser bonus (R-04 revision).
- Strain to loser: (margin − 1, minimum 1) + 1 + winner's Presence modifier. Reduced strain because arguments partially reinforced each other.

**DIVERGENCE (different genre):**
- No direct comparison. Each evaluated independently.
- Initiative holder: effective_margin_A = floor(successes_A × genre_weight_A × orientation_weight_A). If > resistance → Δ = effective_margin_A − resistance toward A's position.
- Respondent: effective_margin_B = floor(successes_B × genre_weight_B × orientation_weight_B). If > resistance → Δ = effective_margin_B − resistance toward B's position.
- Net tracker movement = difference between the two deltas. Direction: toward whichever side produced the larger delta.
- No strain dealt. Neither argument attacked the other.
- Initiative stays with holder (R-01).

**TIE (same successes, any interaction type):**
- Both orators take 1 strain (D-06).
- Tracker moves 1 toward initiative holder's position (D-06).
- Initiative stays with holder.

**FORFEIT (Regroup or Concede):**
- Tracker moves +1 toward non-forfeiting side (R-02). No genre weight applied.
- Strain per Regroup: 0 (you chose recovery over argument).
- Strain per Concede: 1 (self-inflicted). +1D on next exchange.

**Step 5 — Strain and Concentration:**
- Strain accumulates toward Composure (Poise + Bonds + 3).
- At strain ≥ Composure → **Rattled:** −2D to all debate rolls. Focus defence lost. Persists until Unmask or scene end.
- Concentration (Focus + Presence) depletes by 1 per exchange + 1 additional on a loss (D-04C).
- At Concentration 0 → **Spent:** Concentration resets to max. Next exchange: −2D, opponent gets +1D.

**Step 6 — Game Master records exchange on hidden ledger.**

## 0.4 Post-Debate

- Game Master reveals ledger.
- Conviction Track position determines outcome: ≥7 Side A wins, ≤3 Side B wins, 4–6 compromise.
- Winner's final genre + orientation determines thread co-movement type.
- Stakes resolve.

## 0.5 Derived Values Reference

**Presence modifier:** floor((Presence − 3) / 2). Range: +0 to +2.

**Focus defence:** floor(Focus / 2). Range: 0 to 3.

**Composure:** Poise + Bonds + 3. Range: 5–17. Typical: 9–11.

**Concentration:** Focus + Presence. Range: 2–14. Typical: 6–10.

**Attunement read pool:** Attunement score only (1–7D). No History.

---

# PHASE 1: ISOLATION RETESTS

## Retest 1.1: Revised Tracker Movement Formula

**Test: margin 1, genre weight ×1.0, orientation ×1.0, resistance 2.**
effective_margin = floor(1 × 1.0 × 1.0) = 1. 1 ≤ 2 (resistance). Movement: 0. ✓ Small wins absorbed.

**Test: margin 2, genre ×1.0, orientation ×1.0, resistance 2.**
effective_margin = 2. 2 ≤ 2. Movement: 0. Still absorbed.

**Finding v2-01 (P1):** At resistance 2, even margin-2 wins produce zero movement. Only margin 3+ moves the tracker at ×1 weight. In a typical pool-11 vs pool-11 matchup, margin 3+ occurs roughly 20% of exchanges. A 5-exchange Grand Debate produces about 1 decisive exchange. Net movement: ~1 point. Starting at 5, ending at 6 or 4. Always compromise.

**The resistance-as-floor model (R-05) overcorrected.** Resistance 2 is too high for standard debates.

**Test: margin 3, genre ×1.5, orientation ×1.0, resistance 2.**
effective_margin = floor(3 × 1.5 × 1.0) = 4. 4 > 2. Movement: 4 − 2 = 2. This works — a decisive win in a strongly-weighted genre produces real movement.

**Test: margin 2, genre ×1.5, orientation ×1.0, resistance 2.**
effective_margin = floor(2 × 1.5) = 3. 3 > 2. Movement: 1. Borderline functional.

**Assessment:** The system works when genre weight is ×1.5 (audience's preferred genre) but not at ×1.0. This means orators MUST argue in the audience's preferred genre to move the room. Arguing in ×1.0 genres at typical margins produces nothing.

**This might be correct design.** It means reading the room is essential — argue in the wrong genre and your wins are meaningless. But it also means that if the primary genre IS ×1.0 (no ethical mode boost), the debate is almost impossible to win outright.

**Patch v2-P01:** Reduce default resistance by 1. Audience resistance = average Stability of represented factions, round up, MINUS 1 (minimum 0). Typical resistance: 0–2 instead of 1–3. This preserves the resistance mechanic while making ×1.0 genres functional.

Recheck: margin 2, genre ×1.0, orientation ×1.0, resistance 1.
effective_margin = 2. 2 > 1. Movement: 1. ✓ Functional.

margin 1, genre ×1.0, orientation ×1.0, resistance 1.
effective_margin = 1. 1 ≤ 1. Movement: 0. Margin-1 wins still absorbed at resistance 1. Only margin-1 at resistance 0 moves the tracker.

This is acceptable. Margin-1 wins being absorbed at resistance 1 correctly models "you barely won the exchange — the room doesn't care." Margin-2+ at resistance 1 moves.

## Retest 1.2: Revised Strain Formula

**Formula (R-06):** Strain = margin + 1 + Presence modifier.

**Scenario: margin 2, winner Presence 3 (modifier +0).**
Strain = 2 + 1 + 0 = 3. Focus 3 defence: −1. Net: 2. ✓ Meaningful.

**Scenario: margin 2, winner Presence 5 (modifier +1).**
Strain = 2 + 1 + 1 = 4. Focus 3 defence: −1. Net: 3. ✓ Presence matters but doesn't dominate.

**Scenario: margin 1, winner Presence 1 (modifier +0).**
Strain = 1 + 1 + 0 = 2. Focus 3 defence: −1. Net: 1. ✓ Even weak wins produce minimum strain.

**Scenario: margin 4 (blowout), winner Presence 7 (modifier +2).**
Strain = 4 + 1 + 2 = 7. Focus 5 defence: −2. Net: 5. Against Composure 9: over half in one exchange. Devastating. ✓ Blowouts should be devastating.

**Grand Debate accumulation (losing every exchange at margin ~2, opponent Presence 5):**
Per exchange net strain: ~3. After 5 exchanges: 15. Against Composure 9: Rattled at exchange 3. **Rattled fires.** ✓

**Grand Debate accumulation (losing every other exchange at margin ~2, opponent Presence 3):**
Per loss net strain: ~2. Losing 3 of 5: ~6 total. Against Composure 9: not Rattled. Close but survives. ✓ Mixed results don't produce Rattled — correct. You have to be losing badly to get Rattled.

**Assessment:** Strain formula is correctly calibrated after R-06. Rattled fires in genuine domination scenarios (3+ exchange losses in Grand Debate) but not in close contests. Low-Presence winners still deal minimum strain (margin + 1) rather than zero.

## Retest 1.3: Revised Conviction Track Thresholds

**Thresholds (R-07):** ≥7 wins, ≤3 wins. Compromise: 4–6.

**Starting at 5 (neutral), resistance 1 (v2-P01). How many net tracker points to win outright?**
Need to reach 7: +2 net movement. Or reach 3: −2 net movement.

**Can a dominant debater achieve +2 net in 3 exchanges (Formal)?**
Winning all 3 at margin 2, genre ×1.0, orientation ×1.0, resistance 1: 3 exchanges × (2 − 1) = 3 points movement. Tracker: 5 → 8. Wins. ✓

Winning all 3 at margin 2, genre ×1.0, orientation ×0.75 (Obscuring), resistance 1: effective_margin = floor(2 × 0.75) = 1. 1 ≤ 1 → 0 movement per exchange. Tracker stays at 5. Obscuring debater cannot win outright even with total exchange domination. ✗

**Finding v2-02 (P2):** Obscuring orientation at ×0.75 combined with resistance ≥1 means Obscuring arguments almost never move the tracker. An orator who consistently argues Obscuring (defence, doubt-casting, blocking action) will win exchanges but lose the room. This might be intentional — institutions prefer clarity — but it makes Obscuring a mechanically dead choice for tracker movement. Obscuring's value would need to come from somewhere else.

**Proposed function for Obscuring:** Instead of moving the tracker toward your side, Obscuring BLOCKS the opponent's tracker movement. When you win an exchange with Obscuring orientation, the opponent's NEXT winning exchange has its tracker movement reduced by 1 (minimum 0). You're not persuading the room — you're preventing the room from being persuaded.

**Patch v2-P02:** Obscuring does not move the Conviction Track toward your position. Instead, a winning Obscuring exchange places a **Doubt Marker** on the opponent. Their next winning exchange has its effective_margin reduced by 2 before resistance is applied. Doubt Marker is consumed on use. Only one Doubt Marker can be active at a time.

**Recheck:** Orator A wins exchange 1 with Past + Obscuring. No tracker movement. Doubt Marker placed on Orator B. Orator B wins exchange 2 with Future + Revealing, margin 3, genre ×1.0, resistance 1. Normally: effective_margin 3 − resistance 1 = 2 movement. With Doubt Marker: effective_margin 3 − 2 (doubt) = 1. 1 ≤ 1 (resistance) → 0 movement. The Obscuring argument completely neutralized the opponent's next win.

This makes Obscuring a denial tool, not a persuasion tool. Thematically correct: casting doubt doesn't convince people of your position, it prevents them from being convinced of the opponent's. Mechanically distinct from Revealing.

## Retest 1.4: Attunement Read (Calibrated)

**Pool: Attunement alone, 1–7D, TN 7.**

| Attunement | E[successes] | P(failure) | P(success 2+) | P(overwhelming 3+) |
|---|---|---|---|---|
| 1 | 0.4 | 60% | 4% | <1% |
| 2 | 0.8 | 36% | 12% | 2% |
| 3 | 1.2 | 22% | 23% | 7% |
| 4 | 1.6 | 13% | 35% | 15% |
| 5 | 2.0 | 8% | 47% | 25% |
| 7 | 2.8 | 2% | 68% | 47% |

**Assessment:** Attunement 1–2: more likely to fail than succeed. Misleading reads are common. These characters are debating blind.

Attunement 3–4: coin flip between useful information and nothing/misleading. Functional but unreliable.

Attunement 5+: reliably reads the room. Overwhelming (the full picture) at 25%+ chance.

**This is correct calibration.** Attunement investment matters. A character who dumps Attunement will frequently get bad reads and choose the wrong genre. The difference between Attunement 2 (36% failure, 12% full read) and Attunement 5 (8% failure, 47% full read) is massive.

**Finding v2-03 (P3 — confirmed working):** Attunement reads are well-calibrated. No patch needed.

## Retest 1.5: Concentration with Revised Depletion

**Focus + Presence, depletes 1/exchange + 1 on loss.**

| Focus | Presence | Conc. | Exchanges losing all | Exchanges to Spent |
|---|---|---|---|---|
| 1 | 1 | 2 | 2 per exchange (1 + 1 loss) | 1 exchange |
| 3 | 3 | 6 | 2 per exchange | 3 exchanges |
| 5 | 3 | 8 | 2 per exchange | 4 exchanges |
| 3 | 5 | 8 | 2 per exchange | 4 exchanges |
| 5 | 5 | 10 | 2 per exchange | 5 exchanges |

**Winning:** Depletion 1 per exchange only.

| Focus | Presence | Conc. | Exchanges winning all | Exchanges to Spent |
|---|---|---|---|---|
| 3 | 3 | 6 | 1 per exchange | 6 exchanges |
| 5 | 5 | 10 | 1 per exchange | 10 exchanges |

**Mixed (alternating win/loss):** Average depletion 1.5 per exchange.

| Focus | Presence | Conc. | Average exchanges to Spent |
|---|---|---|---|
| 3 | 3 | 6 | 4 exchanges |
| 5 | 5 | 10 | ~7 exchanges |

**Assessment:** Concentration now bites in Grand Debates for characters with Focus + Presence ≤ 6. A losing debater with Concentration 6 is Spent after 3 exchanges — they must Regroup or suffer −2D. A winning debater with Concentration 6 lasts 6 exchanges — they're comfortable in Grand Debates if they keep winning.

**Finding v2-04 (P3 — confirmed working):** Concentration depletion with loss penalty creates the right pressure curve. Losing is doubly punishing (strain + concentration drain), which creates a death spiral for the outmatched debater — correct behaviour. Regroup provides an escape valve.

---

# PHASE 2: FULL SCENARIO RETEST

## Scenario: Church Tribunal (Asymmetric)

**Context:** Confessor Arne brings heresy charges against a Player Character practitioner (Maret) who was witnessed performing a Thread operation in Himmelstift. This is a Church Tribunal — asymmetric proceeding.

**Question:** "Is Maret guilty of heresy?" → Past primary (what did she do?).

**Audience:** Church tribunal judges. Church faction only.

**Weights (D-01):** Past ×1.0 (primary) + Church ethical mode (divine command, Past +0.5) = Past ×1.5. Present ×0.5. Future ×0.5. Orientation: Revealing ×1.0, Obscuring ×0.75.

**Audience resistance (v2-P01):** Church Stability 5. Resistance = 5 − 1 = 4. **Very high.** This tribunal is almost unmovable by argument alone.

**Conviction Track:** Starting at 3 (biased toward guilty — the Church brought charges for a reason). Threshold: ≥7 = acquittal, ≤3 = guilty. Maret starts at the conviction threshold.

**Institutional constraints:** Asymmetric. Arne (Inquisitor) proposes — sets the charges. Maret (accused) responds. Roles do NOT alternate. 3 exchanges. Maret cannot Call for Division. Arne controls exchange count (can end early if he's satisfied).

**Characters:**

| | Arne | Maret |
|---|---|---|
| Cognition | 5 | 4 |
| Memory | 5 | 3 |
| Focus | 4 | 5 |
| Attunement | 2 | 5 |
| Presence | 5 | 3 |
| Poise | 4 | 4 |
| Bonds | 3 | 5 |
| Composure | 10 | 12 |
| Concentration | 9 | 8 |
| History | "Church Doctrine" (5pts, +8D) | "Thread Lore" (4pts, +7D) |
| Pool | 13D | 11D |

Arne is the stronger debater in this context — higher Cognition, higher Memory (critical for citing doctrine), higher Presence. Maret's advantages are Attunement (she reads the room better), Focus (she's harder to rattle), and Bonds (allies could corroborate — but a tribunal may not permit corroboration).

**[EDITORIAL: Can the accused have corroborators in a Church Tribunal? The Church controls the proceeding. Historically, inquisitorial proceedings forbade defense counsel. If corroboration is blocked, Maret's Bonds advantage is nullified.]**

For this test: no corroboration permitted. Maret stands alone.

### Exchange 1

**Read:**
Arne: Attunement 2, 2D → rolls 3, 8 → 1 success. Partial. Game Master: "The judges care about the past — what she did." (True — Past is ×1.5.)
Maret: Attunement 5, 5D → rolls 7, 9, 4, 2, 8 → 3 successes. Overwhelming. Game Master: "Past is dominant — this is a tribunal about facts. Revealing is strongly preferred. The judges are devout — divine command ethics. Arguments from doctrine will land hardest. One specific detail: the youngest judge hesitated when reading the charge — he may be sympathetic but won't act unless given doctrinal cover."

Maret has excellent intelligence. She knows the ethical mode, the genre weight, and has identified a potential sympathizer.

**Initiative:** Arne (Inquisitor proposes in Tribunal — institutional rule, not Presence).

**Arne chooses:** Past + Revealing. Present the eyewitness testimony and charge.

**Maret must respond.** She knows Past + Revealing is the strong play. Her options:
- Past + Obscuring (challenge the evidence): Obscuring places a Doubt Marker but doesn't move the tracker. At tracker 3 (guilty threshold), she needs to move it UP, not just block Arne.
- Past + Revealing (counter-testimony): Clash. She's outpooled 13D to 11D. Risky.
- Present + Revealing (establish her character — she's a healer, a community member): ×0.5 weight. Won't move the tracker much even if she wins.

Maret chooses: **Past + Obscuring.** She'll challenge the evidence. Even though Obscuring doesn't move the tracker, the Doubt Marker (v2-P02) will blunt Arne's next win. She's playing defence — buying time.

**Interaction:** Clash (same genre, opposite orientation).

**Arne rolls:** 13D + Memory +2D (cites the specific eyewitness deposition and the relevant Church law) = 15D. Rolls: 8,3,7,5,9,2,7,1,8,4,6,7,3,9,5 → 7 successes.

**Maret rolls:** 11D. No Memory bonus (she's casting doubt, not citing). Rolls: 7,3,5,8,2,9,4,7,1,6,8 → 5 successes.

**Arne wins, margin 2.**

**Tracker:** effective_margin = floor(2 × 1.5 × 1.0) = 3. Resistance 4. 3 ≤ 4 → 0 movement. Even a margin-2 win in ×1.5 genre doesn't clear Church resistance.

**Finding v2-05 (P1):** Church Tribunal resistance of 4 makes the tracker effectively immovable. Even dominant wins in the strongest genre don't clear it. This means the tribunal ALWAYS convicts — argument quality is irrelevant. The institution's resistance is higher than any achievable effective_margin in a 3-exchange proceeding.

**This might be intentionally oppressive** — the Church tribunal IS designed to convict. The accused cannot win through argument. Their only paths are: Unmask (reveal something so true and raw that it bypasses the system), outside intervention (allies disrupt the proceeding), or accepting conviction and dealing with consequences.

**But:** if the tracker literally cannot move, why have a debate at all? The system needs to offer at least the possibility of acquittal, even if remote.

**Patch v2-P03:** Tribunal asymmetry rule: in asymmetric proceedings, the advantaged institution's resistance is halved (round up) for the disadvantaged party's DEFENCE only. The institution is hard to sway toward the accused's position, but not impossibly so. Church resistance for Maret's tracker movement: ceil(4/2) = 2 instead of 4.

**Recheck with v2-P03:** effective_margin 3, resistance 2. 3 > 2. Movement: 1 toward acquittal. Tracker: 3 → 4. Maret has moved off the guilty threshold.

**BUT:** Maret chose Obscuring, which doesn't move the tracker (v2-P02). She gets a Doubt Marker instead. The tracker stays at 3.

This is correct behaviour. She chose a defensive stance. She blocked Arne's next win instead of trying to persuade the judges. Her strategy is valid but doesn't move the tracker.

**Strain to Maret:** 2 (margin) + 1 (base) + 1 (Arne's Presence modifier) = 4. Focus defence: floor(5/2) = 2. Net: 2. Maret at 2/12.

**Concentration:** Arne 9→8. Maret 8→6 (−1 base, −1 loss).

### Exchange 2

**Read:**
Arne: 2D → 1, 4 → 0 successes. Failure. Game Master gives misleading signal: "The judges are tiring of the factual arguments — perhaps character testimony would be more effective." (False — Past is still ×1.5.)
Maret: 5D → 8, 3, 7, 5, 9 → 3 successes. Overwhelming. Game Master: "Past is still dominant. Revealing still preferred. The youngest judge's sympathy is still accessible — he's been reading his copy of the doctrinal code repeatedly. He wants a doctrinal basis to doubt the charge."

Maret now has critical intelligence: there's a doctrinal argument that could sway the sympathetic judge. She needs to find it.

**Arne (initiative, retained from institutional rule) chooses:** Present + Revealing (misled by his failed read — he thinks character testimony will work). He'll attack Maret's moral standing.

**Maret responds.** Arne pivoted to Present. Maret knows Past is still the strong genre. She could:
- Diverge to Past + Revealing (argue the doctrinal point, her strongest play): evaluated independently, high effective_margin.
- Clash on Present + Obscuring (defend her character): risk winning the exchange but not the room.

Maret chooses: **Past + Revealing.** She'll cite a doctrinal precedent she recalls from Thread Lore — a historical case where a Thread-sensitive individual was acquitted because the Thread operation was performed to heal, not to harm. She's aiming at the youngest judge's doctrinal doubt.

**Interaction:** Divergence (different genres).

**Arne:** 13D (no Memory — character attack, not citation) → rolls: 7,5,8,3,2,9,7,4,6,8,1,7,3 → 6 successes. Present ×0.5, Revealing ×1.0. effective_margin = floor(6 × 0.5 × 1.0) = 3. Resistance 2 (v2-P03 applies symmetrically? No — Arne is the advantaged party. Full resistance 4 for Arne's tracker movement? This is the prosecution, not the defence.)

**Ruling needed:** In asymmetric proceedings, does the halved resistance (v2-P03) apply to the institution's arguments too? No — the institution has FULL access to its own judges. v2-P03 halves resistance for the disadvantaged party only.

Arne's effective_margin: 3. Resistance for prosecution moving toward guilty: we need a rule for this. The tracker starts at 3 (biased toward guilty). The prosecution wants to keep it there or push it lower. The defence wants to push it higher.

**Finding v2-06 (P2):** Resistance should apply in BOTH directions — it represents the institution's inertia, not its bias. Even the prosecution must overcome institutional inertia to move the tracker. The starting position (3, biased toward guilty) already represents the bias. Resistance is the cost of moving the room at all.

Arne's effective_margin: 3. Full resistance 4 (prosecution faces full institutional inertia). 3 ≤ 4 → 0 movement. Arne's Present attack doesn't move the room.

**Maret:** 11D + Memory +2D (citing the specific historical case — "In the year 12 after Solmund, the Synod of Elkenford acquitted Sister Varda of Thread-heresy on grounds that her operation was consistent with healing ministry") = 13D. Rolls: 9,7,3,8,5,7,2,8,4,6,7,1,9 → 7 successes. Past ×1.5, Revealing ×1.0. effective_margin = floor(7 × 1.5 × 1.0) = 10. Resistance 2 (halved for defence). 10 > 2. Movement: 10 − 2 = 8 toward acquittal. Tracker: 3 → 11. **CAPPED AT 10.** Tracker: 3 → 10. Acquittal.

**Wait.** That's absurd. A single roll shouldn't move the tracker 8 points.

**Finding v2-07 (P0 — SYSTEM-BREAKING):** Divergence with high genre weight (×1.5) and high roll (7 successes) against halved resistance (2) produces catastrophic tracker movement. The effective_margin formula (successes × weight) uses RAW successes, not margin-over-opponent. In Clash/Competition, margin is the difference between two rolls — typically 0–3. In Divergence, each roll is evaluated independently against resistance, using total successes — typically 3–7. This means Divergence produces 2–4× the tracker movement of Clash.

**This is broken.** Divergence was supposed to be the "no strain, no direct engagement" trade-off. Instead it's the dominant strategy — argue in a different genre from your opponent and your full roll counts toward the tracker.

**Root cause:** Divergence uses successes, not margin. Clash/Competition uses margin (difference between rolls). These are different scales.

**Patch v2-P04:** Divergence tracker formula uses HALF successes, not full. effective_margin = floor((successes / 2) × genre_weight × orientation_weight). This brings Divergence movement into the same range as Clash margin.

**Recheck:** Maret 7 successes. floor((7/2) × 1.5 × 1.0) = floor(3.5 × 1.5) = floor(5.25) = 5. Resistance 2. Movement: 5 − 2 = 3. Tracker: 3 → 6. Compromise zone. Not acquittal, not conviction.

Better. A brilliant argument in the perfect genre against halved resistance produces significant but not game-ending movement.

**Arne:** 6 successes. floor((6/2) × 0.5 × 1.0) = floor(1.5) = 1. Resistance 4. 1 ≤ 4 → 0. Arne's off-genre argument produces nothing, even with 6 successes.

**Net Divergence movement:** 3 toward acquittal. Tracker: 3 → 6. Entering compromise zone.

**No strain dealt (Divergence rule).**

**Maret also has a Doubt Marker active on Arne from exchange 1.** In a Divergence, no one "wins" an exchange that would trigger the Doubt Marker. Doubt Marker persists.

**Concentration:** Arne 8→7 (no loss). Maret 6→5 (no loss — Divergence has no loser).

### Exchange 3 (Final)

**Read:**
Arne: 2D → 7, 3 → 1 success. Partial. Game Master: "They care about the past." (True.)
Maret: 5D → 8, 7, 2, 9, 4 → 3 successes. Overwhelming. Game Master: "Past still dominant. Revealing preferred. The youngest judge is visibly engaged — the Synod of Elkenford citation shook him. He's now looking at Arne for a response to the doctrinal precedent. The other two judges are unmoved."

**Arne chooses:** Past + Revealing. He MUST address the Synod precedent or lose the young judge entirely. He'll argue the precedent was exceptional and does not apply.

**Maret responds:** Past + Revealing. She'll press the doctrinal argument. Same genre, same orientation → COMPETITION.

**Arne:** 13D + Memory +2D (citing the Synod records and their limited scope) = 15D → 8 successes.
**Maret:** 11D + Memory +2D (citing the specific healing context parallel) = 13D → 5 successes.

**Arne wins, margin 3.** Doubt Marker is active on Arne — his effective_margin is reduced by 2 before resistance. effective_margin = floor((3 − 2) × 1.5 × 1.0) = floor(1.5) = 1. Resistance 4 (prosecution, full). 1 ≤ 4. Movement: 0.

**The Doubt Marker neutralized Arne's decisive win.** Maret's exchange 1 Obscuring play paid off — she sacrificed tracker movement then to blunt his tracker movement now.

**Strain to Maret (Competition):** (3 − 1, min 1 → 2) + 1 (base) + 1 (Presence mod) = 4. Focus defence: −2. Net: 2. Maret at 4/12. Comfortable.

**Concentration:** Arne 7→6. Maret 5→3 (−1 base, −1 loss).

### Resolution

**Exchange count:** Arne won 2 exchanges (1 Clash, 1 Competition). Maret won 0. Divergence had no winner.

**Conviction Track:** 6. Compromise zone (4–6).

**Game Master Ledger:**

| Exch | Type | Winner | Margin | A Genre×Wt | M Genre×Wt | Doubt | Tracker Δ | Tracker |
|---|---|---|---|---|---|---|---|---|
| 1 | Clash | Arne | 2 | Past ×1.5 | Past(Obsc) ×1.5 | Placed | 0 (3 ≤ res 4) | 3 |
| 2 | Divergence | — | — | Present ×0.5 | Past ×1.5 | Active | +3 Maret (5−2) | 6 |
| 3 | Competition | Arne | 3 | Past ×1.5 | Past ×1.5 | Consumed | 0 (1 ≤ res 4 after doubt) | 6 |

**Outcome:** Tracker at 6. Compromise. The tribunal cannot convict outright — the doctrinal precedent introduced reasonable doubt. But the tribunal cannot acquit — the evidence of the Thread operation is clear. The Game Master rules: **Conditional verdict.** Maret is placed under Church supervision for one season. If no further Thread activity is observed, the charge is dismissed. If further activity occurs, the charge is reinstated without retrial.

This is a realistic institutional outcome — the Church saves face, the accused avoids conviction, but the Church retains leverage. The doctrinal argument created enough doubt to prevent conviction but not enough to force acquittal against the Church's institutional weight.

**Mechanical consequences:**
- No Mandate changes (conditional verdict — neither side won or lost outright)
- Maret is mechanically "under surveillance" — Church Intelligence rolls against her at −1 Ob for one season
- The Synod of Elkenford precedent is now public — future heresy trials may cite it (long-term consequence)
- Rendering Stability: +1 (the tribunal discussed Thread operations publicly in a Church setting — the topic itself disturbs the rendering)

---

# PHASE 3: FINDINGS AND FINAL PATCHES

## New Findings from v2 Testing

| ID | Severity | Finding |
|---|---|---|
| v2-01 | P1 (RESOLVED by v2-P01) | Resistance too high at standard formula |
| v2-02 | P2 (RESOLVED by v2-P02) | Obscuring has no tracker function |
| v2-03 | P3 | Attunement reads well-calibrated — no patch |
| v2-04 | P3 | Concentration depletion well-calibrated — no patch |
| v2-05 | P1 (RESOLVED by v2-P03) | Tribunal resistance makes conviction automatic |
| v2-06 | P2 | Resistance applies in both directions (clarification, not patch) |
| v2-07 | P0 (RESOLVED by v2-P04) | Divergence uses successes not margin — catastrophic tracker movement |

## Cumulative Patch List (Final State)

### From v1 (confirmed or revised)

| ID | Description | Status |
|---|---|---|
| D-01 | Genre weights derived from Question + Ethical Mode | ✓ Confirmed |
| D-02 | Attunement read calibration, Attunement only, misleading on failure | ✓ Confirmed |
| D-03 | Conviction Track 0–10, ≥7/≤3 thresholds | ✓ Revised by R-07 (thresholds) and v2-P01 (resistance) |
| D-04A | Strain = margin + 1 + Presence modifier | ✓ Revised by R-06 |
| D-04B | Rattled = −2D + lose Focus defence | ✓ Confirmed |
| D-04C | Concentration −1 extra on loss | ✓ Confirmed |
| D-05 | Clash / Competition / Divergence | ✓ Revised by R-04, v2-P02, v2-P04 |
| D-06 | Ties: mutual 1 strain + tracker +1 toward initiative holder | ✓ Confirmed |
| D-07 | Focus passive: floor(Focus/2) | ✓ Confirmed |
| D-08 | Presence modifier: floor((Presence−3)/2) | ✓ Confirmed |
| D-09 | Memory: +2D for specific citation, any genre, binary | ✓ Confirmed |
| D-10 | Composure = Poise + Bonds + 3 | ✓ Confirmed |

### From v1 retest (confirmed or revised)

| ID | Description | Status |
|---|---|---|
| R-01 | Initiative stays with holder after Divergence | ✓ Confirmed |
| R-02 | Forfeit: +1 tracker toward non-forfeiting side, no genre weight | ✓ Confirmed |
| R-04 | Competition: no loser tracker bonus | ✓ Confirmed |
| R-05 | Resistance as floor | ✓ Confirmed, revised by v2-P01 |
| R-06 | Base strain = margin + 1 | ✓ Confirmed |
| R-07 | Thresholds ≥7 / ≤3 | ✓ Confirmed |

### From v2 (new)

| ID | Description | Status |
|---|---|---|
| v2-P01 | Resistance = avg Stability − 1 (min 0) | ✓ Tested, functional |
| v2-P02 | Obscuring places Doubt Marker (−2 to opponent's next effective_margin). Does not move tracker. | ✓ Tested, functional |
| v2-P03 | Asymmetric proceedings: halved resistance for disadvantaged party | ✓ Tested, functional |
| v2-P04 | Divergence uses half successes: floor((successes/2) × weight) | ✓ Tested, functional |

---

# PHASE 4: REMAINING OPEN ITEMS

## Confirmed Working (No Further Testing Needed)

- Attunement reads (calibration, failure consequences, Attunement-only pool)
- Concentration depletion (loss penalty, Regroup recovery, Spent threshold)
- Strain formula (margin + 1 + Presence, Focus passive defence)
- Genre weight derivation (Question + Ethical Mode, fixed at setup)
- Conviction Track scale and thresholds (0–10, ≥7/≤3)
- Clash resolution
- Competition resolution (reduced strain, no loser bonus)
- Divergence resolution (half successes, no strain)
- Doubt Marker from Obscuring
- Tie consequences (mutual strain + tracker lean)
- Forfeit consequences (fixed +1 tracker)
- Asymmetric resistance halving

## Untested (Require Separate Testing)

| Item | Why Untested | Priority |
|---|---|---|
| Multi-party debates (3+ orators) | No procedure exists | P1 |
| Thread operations during debate | No interaction procedure | P1 |
| Corroboration in practice | Not used in either scenario | P2 |
| Parliamentary proceeding type | No scenario tested Parliament specifically with the new formulas | P2 |
| Royal Audience proceeding type | No scenario tested | P2 |
| Casual Dispute (1 exchange) | Not tested — may have edge cases with tracker at 1 exchange | P3 |
| Regroup exploit in Grand Debate | Identified in v1, not fully retested with new depletion rates | P2 |
| Genre pivot mid-debate (orator tries to shift the Question's genre) | No procedure | P2 |
| Rattled → Unmask decision point | Rattled never triggered in retests | P2 |
| Multiple Doubt Markers (Obscuring wins 2+ exchanges) | Rule says only 1 active — but what happens to the second? | P3 |
| Ethical mode interaction when multiple factions in audience | Guilds moral relativism (Game Master picks) is the only flex point — how does mixed audience work? | P2 |

## Editorial Decisions Required

| Item | Decision |
|---|---|
| Can the accused have corroborators in a Church Tribunal? | Historically no. Mechanically this nullifies Bonds for accused. |
| Does resistance apply symmetrically (both prosecution and defence face it)? | v2-06 says yes. Confirm. |
| Is Obscuring as pure denial (Doubt Marker, no tracker movement) the intended function? | v2-P02 makes Obscuring a blocking tool. Confirm this matches design intent. |
| How does genre pivot work? | Orator argues a different genre from the Question. Is this permitted? Penalised? Requires a specific action? |
| Niflhel social mode | Confirmed: no formal debate. What CAN Niflhel characters do socially? Appeal only? Private manipulation? |
| Grand Debate exchange count for role alternation | 5 exchanges — who proposes 3 times vs 2? Institutional setting determines? |

---

# PHASE 5: FINAL SYSTEM SUMMARY

## The Debate System (Post v2 Patches)

**Game Master Setup:** Question → primary genre. Audience → ethical mode adjustment. Weights fixed, recorded. Resistance = avg Stability − 1. Track starts at Game Master-set position. Stakes defined.

**Each Exchange:**
1. Read (Attunement alone, calibrated output table)
2. Choose (genre + orientation)
3. Argue (initiative holder first, Cognition + History, +2D Memory for citations)
4. Resolve by interaction type:
   - **Clash** (same genre, opposite orientation): margin moves tracker, strain to loser
   - **Competition** (same genre, same orientation): margin moves tracker, reduced strain
   - **Divergence** (different genre): half-successes independently evaluated, no strain
   - **Tie**: mutual 1 strain, +1 tracker toward holder
5. Obscuring wins → Doubt Marker (blocks opponent's next tracker movement)
6. Strain reduced by Focus (passive). Accumulates toward Composure → Rattled.
7. Concentration depletes. Extra on loss. → Spent.

**Resolution:** Ledger revealed. Track ≥7 = Side A. ≤3 = Side B. 4–6 = compromise. Thread co-movement from winner's genre + orientation.
