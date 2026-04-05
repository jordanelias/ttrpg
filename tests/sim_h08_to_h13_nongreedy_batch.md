# VALORIA — UNIQUE TEST BATCH 2
## SIM-H-08 through SIM-H-13
## Date: 2026-04-04 | Non-greedy PC decision-making throughout
## Canonical sources: params_core, params_combat, params_threadwork, params_debate, params_factions, params_mass_combat, stage6, stage12

---

## NON-GREEDY DESIGN NOTE
All PCs in this batch operate under the non-greedy constraint:
- PCs do not always take the highest-EV action. They pursue Belief-driven choices even when mechanically suboptimal.
- PCs conserve resources (Momentum, Inspiration) when narrative stakes are low.
- PCs accept partial successes rather than stacking all available bonuses.
- PCs make choices that create complications, not just victories.
This tests whether the system produces meaningful outcomes when PCs do not min-max.

---

## OPENING STATE (Season 7)
RS: 54 | TC: 45 | IP: 34 | Public Instability: 5
Mira: TS 59, Momentum 2, Coherence 10, CP 16
Arend: Momentum 1, CP 13
Dagmara: Momentum 0, Inspiration (Halvard) depleted, CP 11
Theron: Momentum 1, CP 9

---

## SIM-H-08: Dagmara's Parliament Speech — Without Her Best Tool
**Mode:** TTRPG | **Scene type:** Debate (solo orator, no anchor)
**Mechanic tested:** Debate with constrained preparation; non-greedy resource use; Conviction Track from below-neutral start

**Non-greedy constraint:** Dagmara will NOT spend Inspiration (Harbour District congregation, value 3) on this debate. She is saving it for the moment Halvard openly moves against her community. She also will not Fork her Clandestine Courier History into the Debate — it would expose her Revolution contact to Parliament observation.

**Setup:** Dagmara speaks against the Church motion in Parliament. Conviction Track starts at 4 (Church has already moved the narrative — TC 45 gives them institutional authority bonus). Audience: Hafenmark delegates (Categorical Imperative, Past-boosted), one Guilds representative (Moral Relativism, GM picks genre), three Crown seats (Virtue Ethics, Present-boosted).

Audience ethical mode: mixed. Dominant: Hafenmark majority → Past genre boosted for audience.

**Step 1 — Appraise:** Dagmara Att(5), TN 7, Ob 1 → 5D.
E[net]: 5×0.30 = 1.5. P(≥1): ~95% → Success: reads Church speaker's primary genre as Past, orientation Obscuring (suppressing the TC timeline from Parliament).

**Dagmara chooses: Past/Revealing.** She will use Church history AGAINST the Church — citing the original Reformed Settlement terms that TC crossing 40 was supposed to trigger consultation, not unilateral motion.

Church counter-speaker (NPC): Att 4 → reads Dagmara's genre as Past. NPC chooses Past/Obscuring (institutional doctrine, suppress).

**CLASH:** Same genre (Past), opposite orientation.

Dagmara Argue pool: Cog(4)×2 + Ordained Deacon History(7) = **15D** | Memory bonus: she is citing the Reformed Settlement text specifically → **+2D = 17D** | TN 7
NO Inspiration spend. No Fork.

Church NPC pool: Cog(5)×2 + Church Doctrine History(8) = **18D** | TN 7

Dagmara E[net]: 17×0.30 = **5.1**
Church E[net]: 18×0.30 = **5.4**

**CLASH resolution:**
Genre weight (Past, Hafenmark-majority audience): **1.5**
Orientation (Revealing): **1.0** | (Obscuring): **0.5**
Resistance: avg Stability (Hafenmark 4, Crown 3, Guilds 4) = **3.7 → 4**

Expected margin (Church wins by ~0.3): essentially a coin flip. In ~52% of cases the Church speaker wins by a narrow margin.

**Simulation most likely outcome: Church wins by margin 1.**
Movement: ⌊(1 × 1.5 × 0.5) − 4⌋ = ⌊0.75 − 4⌋ = ⌊−3.25⌋ = 0. No movement. Track stays at 4.

**Non-greedy finding:** Without Inspiration spend (+4D) or Fork (+1D), Dagmara cannot reliably move the track. The speech is delivered, the argument is made, but the margin is insufficient to overcome audience resistance.

**But:** Dagmara chose Past/Revealing against Church Past/Obscuring with a Past-boosted audience. This was the right genre call. The failure is in resources withheld, not strategy.

**Narrative outcome:** The speech lands — Parliament hears it, journalists note it. But the Church motion stands. Dagmara earns +1 CP (Belief 1 pursued). The Guilds delegate approaches her afterward: Theron's deal is now active. Next season she gets the Guilds speaker bonus (+2D collaborative pool toward their agreed action).

**State delta:** Conviction Track: 4 → 4 (no change). Dagmara CP: 11 → 12. Halvard notes her public speech — his suspicion advances one step. Church motion unchallenged this season.

---

### SIM-H-08 FLOWCHART

```
SIM-H-08: DAGMARA PARLIAMENT SPEECH
─────────────────────────────────────────────────────────────────────
ENTRY: Conviction Track 4 | Dagmara Inspiration conserved
NON-GREEDY: No Inspiration spend | No Fork | No Momentum spend

STEP 1 — APPRAISE
  Pool: 5D (Att) | TN 7 | Ob 1 → SUCCESS
  Information: Church speaker = Past/Obscuring

STEP 2 — CHOOSE
  Dagmara: Past/Revealing (cites Reformed Settlement text → Memory +2D)

STEP 3 — ARGUE (CLASH)
  Dagmara: 17D | TN 7 | E[net]: 5.1
  Church NPC: 18D | TN 7 | E[net]: 5.4
  ┌─ Church wins margin 1 (~35%) ───────────────────────────────────┐
  │  Movement: ⌊(1×1.5×0.5)−4⌋ = 0 → Track stays at 4            │
  └─────────────────────────────────────────────────────────────────┘
  ┌─ Dagmara wins margin 1–2 (~30%) ───────────────────────────────┐
  │  Movement: ⌊(1×1.5×1.0)−4⌋=0; ⌊(2×1.5)−4⌋=⌊−1⌋=0           │
  │  Still no movement — Dagmara needs margin ≥3 to move track     │
  └─────────────────────────────────────────────────────────────────┘
  ┌─ Dagmara wins margin ≥3 (~15%) ────────────────────────────────┐
  │  Movement: ⌊(3×1.5)−4⌋=⌊0.5⌋=0; needs margin 3+ for 1pt     │
  │  margin 4: ⌊(4×1.5)−4⌋=2 → Track moves to 6 (Dagmara win)   │
  └─────────────────────────────────────────────────────────────────┘

RESOLUTION: Most likely stalemate. Track: 4 → 4.

KEY FINDING: Without Inspiration (saving for congregation), Dagmara needs
  margin 3+ against a stronger NPC pool. P(margin ≥3) ≈ 15%. Non-greedy
  constraint correctly produces failure without rendering the attempt meaningless.

EXIT: CP +1 | Halvard suspicion +1 step | Guilds deal activates next season
DOMAIN ECHO: None (no stat change — stalemate does not trigger Echo)
─────────────────────────────────────────────────────────────────────
```

---

## SIM-H-09: Arend's Dilemma — Withholding Evidence
**Mode:** TTRPG | **Scene type:** Investigation + social roll
**Mechanic tested:** Circles; partial success consequences; Belief conflict driving suboptimal action

**Non-greedy constraint:** Arend believes the Revolution Southernmost access evidence should go to Crown Marshal Aldric — not Torben. His Belief 1 says so. But getting to Aldric requires going through Torben's secretariat, who will alert Torben. Arend could shortcut this by bribing a secretariat clerk (costs 1 Momentum, higher success rate) — but he won't spend Momentum on a covert act. "I do this clean or not at all." This is his Belief 3 operating.

**Action — Circles roll to reach Aldric directly (bypassing secretariat):**
Pool: Agi(5) + Border Patrol History(7) = 12D (using Agi as primary for fieldwork networks) | TN 7 | Ob 3 (Aldric is politically isolated by Torben, access restricted).

No Momentum spend. No Inspiration.

E[net]: 12×0.30 = 3.6 | P(≥3): ~65%

**Most likely: Success.** But let's use the full distribution:

| Degree | Net | P |
|--------|-----|---|
| Overwhelming | ≥6 AND ≥3 | ~45% |
| Success | 3–5 | ~20% |
| Partial | 1–2 | ~25% |
| Failure | ≤0 | ~10% |

**Simulation result: Success** (contact established, no alert to Torben).

Arend reaches Aldric through an ex-patrol contact. Presents the Revolution marker. Aldric's response: he already knows Revolution has Southernmost access. Torben told him. Arend's evidence is not new — it's corroboration. Aldric is using Torben. Torben is using Aldric. Arend is in the middle.

**Belief 1 challenged:** The distinction between "serving the Crown" and "serving Torben" has dissolved. Aldric and Torben are coordinated, not opposed.

**State delta:** Arend CP +1 (Belief 1 pursued) +1 (Belief 1 challenged = genuine engagement) = +2. Total CP: 13 → 15. No Momentum spent. Arend does not know what to do next — Belief 1 must be rewritten. This is correct: the system is producing narrative advancement through mechanical success + story complication.

**Non-greedy finding:** Arend reached his goal mechanically (Success) but the goal was the wrong goal. The non-greedy constraint (no bribery, no shortcut) meant he did it the slow way — and discovered the truth he didn't want. This is exactly what the Belief system is designed to produce.

---

### SIM-H-09 FLOWCHART

```
SIM-H-09: AREND REACHES ALDRIC
─────────────────────────────────────────────────────────────────────
ENTRY: Belief 1 (bring evidence to Aldric, not Torben) active
NON-GREEDY: No Momentum spend | "Clean or not at all"

CIRCLES ROLL — Reach Aldric directly
  Pool: 12D (Agi5 + History7) | TN 7 | Ob 3
  P(≥3): ~65%
  ┌─ OVERWHELMING (~45%) ───────────────────────────────────────────┐
  │  → Contact + additional info (Aldric shares one hidden detail) │
  └─────────────────────────────────────────────────────────────────┘
  ┌─ SUCCESS (~20%) ────────────────────────────────────────────────┐
  │  → Contact established, no complications                       │
  └─────────────────────────────────────────────────────────────────┘
  ┌─ PARTIAL (~25%) ────────────────────────────────────────────────┐
  │  → Contact via intermediary; 1-day delay; Torben notified      │
  └─────────────────────────────────────────────────────────────────┘
  ┌─ FAILURE (~10%) ────────────────────────────────────────────────┐
  │  → No contact; secretariat flags inquiry; Torben aware         │
  └─────────────────────────────────────────────────────────────────┘

RESOLUTION: SUCCESS → Aldric already knows. Torben and Aldric coordinated.

BELIEF SYSTEM TRIGGERS:
  → Belief 1 pursued: +1 CP
  → Belief 1 challenged (goal achieved, but goal was wrong): +1 CP
  → Belief 1 must be rewritten next session: signals campaign advancement

STATE DELTA: Arend CP 13→15 | Momentum unchanged | Belief 1 in flux
─────────────────────────────────────────────────────────────────────
FINDING SIM-H-09-F1: Success + story complication is the system's ideal
  output. Non-greedy constraint (no Momentum bribe) produced a clean roll
  that revealed the truth — not a shortcut that would have hidden it.
FINDING SIM-H-09-F2: Belief rewrite is the CP-richest event in the system
  (+2 on revision). The system correctly incentivises engagement with failure.
─────────────────────────────────────────────────────────────────────
```

---

## SIM-H-10: Mira's Past-Oriented Pull — The 14-Day Actor
**Mode:** TTRPG | **Scene type:** Thread operation sequence
**Mechanic tested:** Past-Oriented Pulling (POP); Coherence cost; Temporal Disjunction; non-greedy use of Overwhelming Leap result

**Non-greedy constraint:** Mira has confirmed the 14-day RS degradation cycle. She knows a Pull event occurred 3 days ago — she can attempt a POP to observe it. But she does NOT attempt Dissolution or Locking after the POP (which would maximise tactical advantage). Her Belief 2 says "find proof" — not "stop it." She takes what the system gives her and withdraws.

**State:** RS 54. Mira TS 59, Coherence 10, Momentum 2. Location: a Thread-active territory (high-traffic, not Southernmost).

### Action A — Leap Roll

Pool: Spi(4) + Att(3) + TPS(5) + History(7) = **19D** | TN 7 | Ob 1 (TS 50+)

E[net]: 19×0.30 = 5.7 | P(Overwhelming): ~87%

**Outcome: Overwhelming.** Clean suspension. Next op Ob −1. TS: 59→60. TPS: 60÷10=**6**.

**Non-greedy decision:** She does NOT use the Ob−1 on anything aggressive. She uses it on the POP — reducing the already-high Ob by 1. This is consistent with her Belief.

### Action B — Past-Oriented Pull (observe, not displace)

Mira attempts to observe the POP event from 3 days ago (recency: 3 days → Ob 1 by recency; Personal scale — observing a practitioner's action → Ob 2 for relational scale observation). Total Ob with RS penalty (+1, RS 54 < 60): **Ob 3**. Overwhelming Leap reduces: **Ob 2**.

**POP pool:** Spi(4) + History(7) + TPS(6)÷2 round down = TPS contribution: 3 | Total: 4+7+3 = **14D** | TN 8 (POP is always TN 8)

E[net at TN 8]: 14×0.20 = **2.8** | P(≥2): ~56% | P(≥4, Overwhelming): ~17%

**Simulation — most likely: Success.** Net 2–3.

**Success outcome:** Mira observes the past Pull event. She sees: a practitioner with TS above 60 (the Thread signature is too precise for sub-60 TS), operating at relational scale, displacing a Thread configuration tied to the RS substrate. The degradation is deliberate. The practitioner's Leap signature is distinctive — high Focus (5+), unusually clean. She cannot identify them from this distance. But she has the signature.

**RS cost (POP Success):** RS unchanged on Success (per params_threadwork POP degree table).
**Coherence cost:** POP Success: −0 (Success on POP doesn't cost Coherence, only Partial and Failure do).

**Temporal Disjunction:** POP observation at relational scale — Mira now holds a memory that the physical world does not contain. She knows the practitioner existed in this space 3 days ago. No one else does. No Disjunction condition triggered (observation, not displacement).

**Non-greedy finding:** Mira could have attempted to Lock the Thread configuration the POP actor used — but she withdrew. The information she gained (TS 60+, Focus 5+, relational-scale precision) is tactically rich. She sacrificed mechanical advantage to honour her Belief.

### Action C — Forgetting Check (no Southernmost context)

**Not required.** This operation was in a normal territory, not the Southernmost. Forgetting Check only applies to Southernmost exposure. Confirmed by stage4_southernmost text: "The Southernmost's danger cannot be rendered by those without Thread sensitivity" — the Forgetting is zone-specific.

**State delta:** Mira TS 59→60, TPS 5→6. RS: 54 (unchanged). Coherence: 10. Intelligence gained: actor profile (TS 60+, Focus 5+, relational-scale precision). Belief 2 advanced — proof acquired. CP: +1 (Belief pursued) +1 (Belief challenged by what she found) = +2. Total CP: 16→18.

**Candidate list implications:** TS 60+ in Valoria is rare. Confirmed TS 60+ practitioners known: Mira (59, now 60 — cannot be self-observation of future), Lenneth (Mira's mentor, TS unknown but trained her). [EDITORIAL: ED-161 — Lenneth's Thread Sensitivity not established in any canonical doc. Flag for NPC roster development.]

---

### SIM-H-10 FLOWCHART

```
SIM-H-10: MIRA PAST-ORIENTED PULL
─────────────────────────────────────────────────────────────────────
ENTRY: RS 54 | TS 59 | Coherence 10 | Momentum 2
NON-GREEDY: No aggressive follow-up after POP | No Lock | No Dissolution

ACTION A — LEAP
  Pool: 19D | TN 7 | Ob 1
  P(Overwhelming): ~87%
  OUTCOME: OVERWHELMING → Clean suspension; Ob−1 banked; TS 59→60; TPS→6

ACTION B — PAST-ORIENTED PULL (observe 3-day-prior event)
  Base Ob: 2 (relational-scale observation) + RS penalty 1 − Leap bonus 1 = Ob 2
  Pool: 14D (Spi4+Hist7+TPS3) | TN 8
  ┌─ OVERWHELMING (~17%) ─────────────────────────────────────────┐
  │  → Clear observation + practitioner TS range identifiable    │
  │  → TS: +1 → 61 | Next op Ob −1                              │
  └───────────────────────────────────────────────────────────────┘
  ┌─ SUCCESS (~39%) ──────────────────────────────────────────────┐
  │  → Observation: actor profile (TS 60+, Focus 5+) | RS±0     │
  └───────────────────────────────────────────────────────────────┘
  ┌─ PARTIAL (~28%) ──────────────────────────────────────────────┐
  │  → Partial observation: TS range only (no Focus read)        │
  │  → RS −1 | Coherence −1                                     │
  └───────────────────────────────────────────────────────────────┘
  ┌─ FAILURE (~16%) ──────────────────────────────────────────────┐
  │  → Snap-back: 1 Wound | RS −2 | Coherence −1               │
  └───────────────────────────────────────────────────────────────┘

RESOLUTION: SUCCESS (most likely)
  → Actor profile secured | RS unchanged | Coherence intact

NON-GREEDY DECISION POINT:
  After Success, Mira could: Lock the configuration (+RS cost), attempt
  Dissolution (RS −3 to −8), or attempt to pull the actor's identity.
  CHOICE: Withdraw. Belief 2 is "find proof" — achieved. Over-extension
  risks Coherence and reveals her presence to the actor.

EXIT STATE:
  TS: 60 | TPS: 6 | RS: 54 | Coherence: 10
  Intelligence: actor is TS 60+, Focus 5+, relational-scale practitioner
  CP: 16→18 | Belief 2: advanced (proof obtained)
  New editorial: ED-161 (Lenneth TS undefined)
─────────────────────────────────────────────────────────────────────
FINDING SIM-H-10-F1: POP at TN 8, 14D produces 56% success rate.
  At TN 8 the system correctly makes even expert practitioners uncertain.
FINDING SIM-H-10-F2: Non-greedy withdrawal after Success preserves RS
  and Coherence. PCs who do not over-extend keep the RS clock stable.
  This is the correct incentive structure.
FINDING SIM-H-10-F3: TS cliff at 60 confirmed from player side — TS 60
  unlocks TPS 6, which adds +3D vs TPS 5. Significant jump at this threshold.
─────────────────────────────────────────────────────────────────────
```

---

## SIM-H-11: Theron's Debt — The Hafenmark Creditor
**Mode:** TTRPG | **Scene type:** Social (Appeal + Circles) + Domain Echo
**Mechanic tested:** Belief-driven constraint; Appeal at asymmetric power; Domain Echo (PP-252)

**Non-greedy constraint:** Theron owes a Hafenmark creditor (his Belief 3 focus, unnamed). He will NOT use the Guilds faction bonus dice on this roll — the Guilds cannot know about this personal debt. He also will NOT spend Momentum — he's saving it for the Parliament manoeuvre next season.

**Setup:** The creditor (Vennrich Solt — distinct from Vrenna Solt the delegate; Theron's earlier Circles contact introduced a confusion he hasn't corrected) calls in the debt. Payment: Theron must provide the Guilds' trade route mapping for the eastern territories. This is faction intelligence. Theron must either pay or refuse.

**Non-greedy decision:** Theron tries to negotiate — not to win, but to buy time. He Appeals, but his goal is merely a partial success: delay the debt by one season.

**Appeal roll — buy one season of delay:**
Pool: Cha(5) + Merchant-factor History(7) = **12D** | TN 7 | Ob 2 (creditor is motivated; Ob 3 would be "won't budge"; Ob 2 = willing to negotiate but not for free)
No Momentum. No faction bonus.

E[net]: 12×0.30 = 3.6 | P(≥2): ~92%

**Most likely: Success or Overwhelming.** Theron buys one season.

**But the non-greedy element:** He reveals more than he intended during the negotiation — the creditor now knows Theron has Vrenna Solt access (Parliamentary delegate). The creditor is Hafenmark-aligned. This is information he should not have.

**Mechanical form of this:** Overwhelming vs Success matters here.
- **Overwhelming** (P ≈ 60%): Delay secured; nothing revealed.
- **Success** (P ≈ 32%): Delay secured; creditor notes Theron's Parliament access (revealed as a Partial complication of the social scene — GM ruling, not a Partial roll).
- **Partial** (P ≈ 6%): One-week delay only; creditor demands proof of Guilds backing.

**Simulation result: Overwhelming** (most likely). Theron secures the delay cleanly. Nothing revealed.

**Non-greedy consequence:** Even on Overwhelming, Theron has not resolved his Belief 3 — he's delayed it. He earned no CP for Belief 3 this season (no genuine pursuit). He chose the minimum viable action. The system correctly produces: mechanical success, narrative stasis.

**CP this scene:** +0 (Belief 3 not genuinely pursued — avoidance doesn't trigger Belief CP).

**Domain Echo (PP-252):** Does this scene have faction-level scope? Theron's delay prevents trade route disclosure — Guilds Intel (+1, protected) would be the Echo, but only on Success or Overwhelming that actively preserves a faction asset. Overwhelming: Guilds Intel +1 (Domain Echo: Guilds maintains intelligence advantage this season). Magnitude: Overwhelming → stat +1 per PP-252.

---

### SIM-H-11 FLOWCHART

```
SIM-H-11: THERON — HAFENMARK DEBT NEGOTIATION
─────────────────────────────────────────────────────────────────────
ENTRY: Belief 3 (debt comes due) active | Momentum 1 conserved
NON-GREEDY: No Guilds bonus dice | No Momentum spend | Minimum viable action

APPEAL — Buy 1 season delay
  Pool: 12D (Cha5+History7) | TN 7 | Ob 2
  ┌─ OVERWHELMING (~60%) ─────────────────────────────────────────┐
  │  → Delay secured | Nothing revealed                          │
  │  → Domain Echo (PP-252): Guilds Intelligence +1 (protected) │
  └───────────────────────────────────────────────────────────────┘
  ┌─ SUCCESS (~32%) ──────────────────────────────────────────────┐
  │  → Delay secured | Creditor notes Parliament access           │
  │  → Domain Echo: Guilds Intelligence +1 (but creditor gains   │
  │    +1D to any future Hafenmark roll targeting Guilds)        │
  └───────────────────────────────────────────────────────────────┘
  ┌─ PARTIAL (~6%) ───────────────────────────────────────────────┐
  │  → 1 week delay only | Must prove Guilds backing next scene  │
  └───────────────────────────────────────────────────────────────┘

RESOLUTION: OVERWHELMING (most likely) → Clean delay; Domain Echo fires

CP CHECK:
  Belief 3 (debt comes due) — avoidance. No genuine pursuit.
  → CP award: 0 (system correctly does not reward avoidance)

NON-GREEDY FINDING: Mechanical success without narrative resolution.
  The system correctly produces: "you won the exchange, not the war."
─────────────────────────────────────────────────────────────────────
FINDING SIM-H-11-F1: Domain Echo (PP-252) fires correctly — Overwhelming
  personal scene converts to Guilds faction stat +1. Magnitude calibrated.
FINDING SIM-H-11-F2: Non-greedy avoidance produces 0 CP even on Overwhelming.
  The Belief system correctly does not reward deferral.
FINDING SIM-H-11-F3: Distinction between Vennrich Solt and Vrenna Solt is a
  GM-created information hazard. The system does not mechanically track NPC
  name confusion — this is a narrative gap that could derail faction politics.
  [GAP-H-06: No rule for PC-held incorrect NPC information. Recommend GM
  guidance note in stage10 or NPC roster.]
─────────────────────────────────────────────────────────────────────
```

---

## SIM-H-12: Mass Combat — Varfell Skirmish Under PP-248
**Mode:** TTRPG (mass combat) | **Scene type:** 2-turn engagement
**Mechanic tested:** PP-248 Discipline degradation (asymmetry precondition); Battle Plan Templates (PP-235); Domain Echo post-battle

**Non-greedy constraint:** The Crown force commander (Arend, acting in advisory capacity) chooses the "Hold" battle plan rather than "Advance." Tactically, Advance would produce more aggressive engagement and potentially faster resolution. Hold is chosen because the Crown does not want a decisive engagement — they want to demonstrate presence without escalating. This is politically motivated, not optimal.

**Setup:** A Varfell border patrol (3 units) is asserting contested territory against a Crown Legionary detachment (2 units). Arend is advising — not commanding — a Crown officer (Non-Player Character General, Command 4).

**Varfell force:** Unit A: Size 4, Command 3, Discipline 4, Power 2, DR 1. Unit B: Size 3, Command 2, Discipline 3, Power 1, DR 0. Unit C: Size 2, Command 2, Discipline 2, Power 1, DR 0.
**Crown force:** Unit X: Size 5, Command 4, Discipline 4, Power 3, DR 2. Unit Y: Size 4, Command 3, Discipline 3, Power 2, DR 1.

**Battle Plan: Crown = Hold (Defensive formation). Varfell = Advance (Aggressive).**

### Turn 1, Phase 5 — Engagement

Crown Unit X (Hold/Defensive) vs Varfell Unit A (Advance/Aggressive):
Pool = min(Size,Command) + Command = min(5,4)+4 = **8D** (Crown X) | TN 7 | Ob = attacker's Command = 3 (Varfell A Command)

Varfell Unit A pool = min(4,3)+3 = **6D** | TN 7 | Ob = Crown X Command = 4

Crown X E[net]: 8×0.30 = 2.4. Varfell A E[net]: 6×0.30 = 1.8.

**Simultaneous resolution (Phase 6 Step 1):**

Crown X damage on Varfell A: E[hits] at E[net] 2.4. Damage per success = 1+Power(3) = 4. E[damage] = 2.4 × 4 = 9.6 HP. Varfell A total HP = Size(4) × H. H = min(Discipline,Command)+DR = min(4,3)+1 = 4. Total HP = 16. After damage: 16−9.6 = 6.4 → Size = ⌊6.4÷4⌋ = **1** (from 4 to 1 — lost 3 Size).

Varfell A damage on Crown X: E[net] 1.8. Damage per success = 1+Power(2) = 3. E[damage] = 1.8×3 = 5.4. Crown X HP = 5×(min(4,4)+2) = 5×6 = 30. After: 30−5.4 = 24.6 → Size = ⌊24.6÷6⌋ = **4** (from 5 to 4 — lost 1 Size).

**Phase 6 Step 2 — Discipline Degradation Check (PP-248):**

Varfell A: Size lost this turn = 3. Discipline = 4. 3 > 4? No. Discipline check does NOT fire. **Correct — PP-248 requires Size lost > Discipline.**

Crown X: Size lost = 1. Discipline = 4. 1 > 4? No. No check.

**BUT: Power asymmetry check.** Crown X Power(3) > Varfell A Power(2). Asymmetry exists. **However**, the trigger requires BOTH: Size lost > Discipline AND Power asymmetry. Crown X inflicted 3 Size loss on Varfell A. Is Crown X Power(3) > Varfell A Power(2)? Yes. Is Size lost(3) > Varfell A Discipline(4)? No (3 < 4). **PP-248 correctly does not fire.**

*This is a key finding: PP-248 requires Size lost > Discipline. The higher-Discipline unit absorbs more punishment before degrading. This is correct design — veteran units are harder to break.*

**Phase 6 Step 3 — Morale Check:**

Varfell A lost 75% of its Size. Morale check: pool = Discipline(4)D, TN 7, Ob 2 (heavy casualties).
E[net]: 4×0.30 = 1.2. P(≥2): ~50%. **Most likely: Partial or Failure.** Partial: unit holds but disordered. Failure: unit routs.

Assuming Partial: Varfell A holds, disordered. No rout.

### Turn 2 — Varfell Tactical Withdrawal

Non-Player Character Varfell commander reads the engagement. Unit A is effectively destroyed (Size 1). Withdraws. Crown holds ground. No pursuit (Hold plan — withdrawal is not contested under Hold).

**Battle outcome: Crown Success. No decisive engagement. Both sides withdraw.**

**Domain Echo (PP-252):** Crown Personal Phase scene precedes this. Arend's advisory role + battle Success → Domain Echo: Crown Military +1 (demonstrated credible presence). Magnitude: Success → stat +1.

**PP-248 validation:** Discipline degradation did not fire in 2 turns despite significant Size loss. This is correct: Varfell's Discipline 4 cushioned the impact. A unit with Discipline 2 (like Varfell Unit C) would have degraded after losing 3 Size. The mechanic correctly differentiates veteran from levy units.

---

### SIM-H-12 FLOWCHART

```
SIM-H-12: VARFELL SKIRMISH — PP-248 VALIDATION
─────────────────────────────────────────────────────────────────────
ENTRY: Crown Hold plan | Varfell Advance | Arend advisory (non-greedy: Hold)

TURN 1 ENGAGEMENT (simultaneous):
  Crown X (8D) vs Varfell A (6D):
  Crown X → Varfell A: E[damage] 9.6 → Size 4→1 (lost 3)
  Varfell A → Crown X: E[damage] 5.4 → Size 5→4 (lost 1)

PP-248 DISCIPLINE DEGRADATION CHECK:
  Varfell A: Size lost(3) > Discipline(4)? NO → no fire ✓
  Crown X: Size lost(1) > Discipline(4)? NO → no fire ✓
  Power asymmetry present (Crown Power 3 > Varfell Power 2) but
  both conditions required — size threshold not met → correctly blocked

MORALE CHECK — Varfell A (75% casualties):
  4D | TN 7 | Ob 2 | P(≥2): ~50%
  ┌─ SUCCESS/OVERWHELMING (~50%) → unit holds, disordered ─────────┐
  └─────────────────────────────────────────────────────────────────┘
  ┌─ PARTIAL/FAILURE (~50%) → unit routs ──────────────────────────┐
  └─────────────────────────────────────────────────────────────────┘
  MOST LIKELY: Partial — holds but tactically spent

TURN 2: Varfell withdraws. Crown holds. No pursuit.

DOMAIN ECHO (PP-252): Crown Success → Crown Military +1
SEASONAL CAP CHECK: +1 within ±2 season cap ✓

─────────────────────────────────────────────────────────────────────
FINDING SIM-H-12-F1: PP-248 correctly blocks Discipline degradation when
  Size lost < Discipline. Veteran units (Discipline 4+) can absorb 3
  Size loss per turn without organisational collapse. Design confirmed.
FINDING SIM-H-12-F2: Morale check at 75% casualties is a genuine 50/50.
  This is appropriate — units near collapse should face real risk.
FINDING SIM-H-12-F3: Hold plan produces clean tactical result without
  decisive engagement. Non-greedy (political over optimal) choice correctly
  produces "won the field, gained little" outcome.
─────────────────────────────────────────────────────────────────────
```

---

## SIM-H-13: Collective Weaving — PP-253 Recall Anchor in Practice
**Mode:** TTRPG | **Scene type:** Thread operation + Southernmost exposure
**Mechanic tested:** Collective Forgetting (PP-253 Recall Anchor); Weaving at territorial scale; Coherence cost cascade

**Non-greedy constraint:** Mira (Anchor) could attempt a second Thread operation after the Collective Weave — she has remaining Focus rounds. She does not. She withdraws to protect her Coherence. Dagmara (secondary practitioner, TS 31) defers entirely to Mira's assessment rather than attempting her own operation.

**Setup:** Mira and Dagmara are in the Southernmost Locked Zone at Einhir-7. Dagmara is there to witness — not to operate. Mira attempts a territorial-scale Mending (closing a Micro-Gap at the Einhir core approach). This is beyond her typical Object-scale work.

**Mira — Leap:**
Pool: Spi(4)+Att(3)+TPS(6)+History(7) = **20D** | TN 7 | Ob 1 (TS 60+, no RS penalty — RS 54 < 60, but Ob 1 floor applies; RS penalty would make Ob 2, but Ob minimum is 1. Wait: RS penalty is +1 Ob to operations at RS < 60, not a floor override. Ob 1 + RS penalty = Ob 2.)

Revised: Ob **2**.

E[net]: 20×0.30 = 6.0 | P(Overwhelming): ~95%

**Outcome: Overwhelming.** TS 60→61. Next op Ob −1.

**Mira — Mending (Territorial scale, Micro-Gap):**
Micro-Gap is the smallest Gap category. Mending Ob by Gap size: Micro-Gap = Ob 2. Territorial scale surcharge: +2 Ob (scale-based Ob increases from threadwork v25). RS penalty: +1 Ob. Total Ob: 2+2+1 = **5**. Leap Overwhelming: Ob −1 → **Ob 4**.

Pool: Spi(4)+Att(3)+TPS(6)+Mending-relevant History (Einhir Expedition, 7) = **20D** | TN 7 | Ob 4

E[net]: 20×0.30 = 6.0 | P(≥4): ~90% | P(Overwhelming, ≥8 AND ≥3): ~55%

**Outcome: Success** (using the middle estimate; Overwhelming possible but not certain).

**RS change:** Mending Success at Territorial scale. RS cost per scale multiplier: standard Mending Success: RS +1. Territorial scale surcharge: ×scale modifier. [GAP: Territorial-scale Mending RS gain not defined — params_threadwork states Mending Success = RS +1 at Object scale; scale multiplier for gains is undefined. Object confirmed; Territorial extrapolated.]

**Provisional ruling:** RS +1 per scale tier above Object (Object=+1; Personal=+1; Relational=+2; Structural=+3; Territorial=+4; Foundational=+5). This is consistent with the failure cost scaling (Dissolution at Structural = RS −5 on Success; scaling implies proportional gains).

RS: 54 + 4 = **58**. [FLAGGED FOR REVIEW: ED-162 — Mending RS gain by scale. Confirm scale progression or define explicitly.]

**Coherence cost (Territorial scale operation):**
Threadwork v25 Coherence table: Territorial scale operation → Coherence −2 (from the scale Coherence cost table, threadwork §3.4 — Relational: −1; Structural: −2; Territorial: −2 to −3; using −2 as lower bound).
Mira Coherence: 10 → **8**.

**Dagmara — Forgetting Check (Interior-equivalent depth — they've been at the Locked Zone for 2 hours):**
Pool: Cog(4)+Rec(3)+TS-bonus(31÷20=1) = **8D** | TN 8 | Ob 2.
E[net]: 8×0.20 = 1.6 | P(≥2): ~45% | P(Partial, net=1): ~30% | P(Failure): ~25%

**Dagmara outcome: most likely Partial.** She retains emotional impression but loses content.

**PP-253 Recall Anchor activation:** Mira passed her own Forgetting Check earlier (she's TS 60 now — Interior Ob 2, pool 11D TN 8, P(≥2)=~56%). Assume Mira passed. She acts as Recall Anchor for Dagmara.

**Anchor effect:** Dagmara's Partial → elevated to Success-equivalent retention. She retains facts (what she witnessed, Mira's Mending, the Micro-Gap location) but not emotional conviction. She cannot testify credibly — but she can write it down immediately and use those notes.

**Non-greedy outcome:** Mira withdrew after Mending. Did not attempt Lock or Diagnosis. RS gained +4. Coherence cost −2. Dagmara's information is preserved through Anchor. The system produced: net RS gain, Coherence cost, partial information preservation. No overreach.

---

### SIM-H-13 FLOWCHART

```
SIM-H-13: COLLECTIVE MENDING — PP-253 ANCHOR
─────────────────────────────────────────────────────────────────────
ENTRY: RS 54 | Mira TS 60, Coherence 10 | Dagmara TS 31, Coherence 10
NON-GREEDY: Withdraw after Mending | Dagmara defers entirely

ACTION A — MIRA LEAP
  Pool: 20D | TN 7 | Ob 2 (RS penalty applied)
  P(Overwhelming): ~95%
  OUTCOME: OVERWHELMING → TS 60→61 | Next op Ob −1

ACTION B — MIRA MENDING (Territorial, Micro-Gap)
  Base Ob: 2 (Micro-Gap) + 2 (Territorial scale) + 1 (RS) − 1 (Leap) = Ob 4
  Pool: 20D | TN 7
  P(≥4): ~90%
  ┌─ OVERWHELMING (~55%) ─────────────────────────────────────────┐
  │  → Gap closed | RS +4 (provisional scale gain) | Coherence −2│
  │  → TS 61→62                                                  │
  └───────────────────────────────────────────────────────────────┘
  ┌─ SUCCESS (~35%) ──────────────────────────────────────────────┐
  │  → Gap closed | RS +4 (provisional) | Coherence −2           │
  └───────────────────────────────────────────────────────────────┘
  ┌─ PARTIAL (~8%) ───────────────────────────────────────────────┐
  │  → Gap reduced one category | RS unchanged | Coherence −2    │
  └───────────────────────────────────────────────────────────────┘
  ┌─ FAILURE (~2%) ───────────────────────────────────────────────┐
  │  → Gap unchanged | RS −2 | Coherence −1                      │
  └───────────────────────────────────────────────────────────────┘

RESOLUTION: SUCCESS (most likely) → Gap closed, RS 54→58

FORGETTING CHECKS:
  Mira: 11D TN 8 Ob 2 → P(pass): ~56% → PASS (assumed)
  Dagmara: 8D TN 8 Ob 2 → P(pass): ~45%
  ┌─ Dagmara PASSES (~45%) ───────────────────────────────────────┐
  │  → Both retain; no Anchor needed                             │
  └───────────────────────────────────────────────────────────────┘
  ┌─ Dagmara PARTIAL/FAILS (~55%) ────────────────────────────────┐
  │  → PP-253 Recall Anchor fires: Mira anchors Dagmara          │
  │  → Dagmara: Partial elevated to Success-equivalent retention │
  └───────────────────────────────────────────────────────────────┘
  MOST LIKELY: Anchor fires. Dagmara retains facts only.

EXIT STATE:
  RS: 58 | Mira TS 61, Coherence 8 | Dagmara: notes retained
  [FLAGGED FOR REVIEW: ED-162 — Mending RS gain by scale]
─────────────────────────────────────────────────────────────────────
FINDING SIM-H-13-F1: PP-253 Recall Anchor fires in ~55% of Dagmara cases.
  It correctly elevates a failed/partial to fact-retention without emotional
  conviction. This is a meaningful mechanical distinction.
FINDING SIM-H-13-F2: Territorial-scale Mending RS gain (provisional +4)
  is significant — single operation can move RS by 4 points. This may be
  too impactful; confirm against RS clock design intent.
  [FLAGGED FOR REVIEW: ED-162]
FINDING SIM-H-13-F3: Coherence −2 per Territorial operation is the
  correct pressure point. Over 5 Territorial operations, Mira would reach
  Coherence 0. This is a realistic campaign arc constraint.
FINDING SIM-H-13-F4: Non-greedy withdrawal after one operation preserves
  Coherence for future sessions. The system correctly incentivises restraint.
─────────────────────────────────────────────────────────────────────
```

---

## BATCH SUMMARY TABLE

| Test | Mechanic | Mode | Novel | Non-Greedy Element | Key Finding |
|------|----------|------|-------|--------------------|-------------|
| SIM-H-08 | Debate CLASH, conserved resources | TTRPG | Solo orator without Inspiration | No spend → stalemate | System produces meaningful failure without trivialising attempt |
| SIM-H-09 | Circles, Belief revision | TTRPG | Clean evidence chain | No bribe/Momentum | Success + story complication = system ideal output |
| SIM-H-10 | POP, TS cliff at 60, non-aggressive withdrawal | TTRPG | POP with deliberate non-escalation | No follow-up ops | Non-greedy preserves RS; proof obtained without overreach |
| SIM-H-11 | Appeal, Domain Echo PP-252, Belief avoidance | TTRPG | Debt negotiation, minimum viable action | No faction bonus | 0 CP on Overwhelming avoidance — correct Belief system behaviour |
| SIM-H-12 | PP-248 validation, Battle Plans PP-235 | TTRPG mass combat | Asymmetry precondition test | Hold plan vs optimal Advance | PP-248 correctly blocks degradation; morale 50/50 at 75% casualties |
| SIM-H-13 | PP-253 Collective Forgetting, Territorial Mending | TTRPG | Recall Anchor first test; scale RS gain | Withdraw after single op | Anchor fires 55% of the time; Territorial RS gain needs calibration review |

## NEW FINDINGS THIS BATCH

| ID | Finding | Severity |
|----|---------|---------|
| SIM-H-08-F1 | Non-greedy CLASH stalemate produces meaningful failure with no trivialisation | Design confirmed |
| SIM-H-09-F1 | Success + complication is ideal output; Belief rewrite incentivised | Design confirmed |
| SIM-H-09-F2 | Belief avoidance correctly earns 0 CP | Design confirmed |
| SIM-H-10-F1 | POP at TN 8, 14D: 56% success — expert practitioners face real uncertainty | Design confirmed |
| SIM-H-10-F2 | Non-greedy withdrawal keeps RS stable — correct incentive structure | Design confirmed |
| SIM-H-10-F3 | TS cliff at 60: +3D jump in TPS — significant advancement milestone | Design note |
| SIM-H-11-F1 | Domain Echo PP-252 fires correctly on Overwhelming (Guilds Intel +1) | PP-252 validated |
| SIM-H-11-F2 | 0 CP on Belief avoidance even on Overwhelming — correct | Design confirmed |
| SIM-H-11-F3 | NPC name confusion (Vennrich vs Vrenna Solt) — no mechanical tracking rule | GAP-H-06 |
| SIM-H-12-F1 | PP-248 correctly blocks degradation when Size lost < Discipline (even with Power asymmetry) | PP-248 validated |
| SIM-H-12-F2 | Morale check at 75% casualties: 50/50 — appropriate tension | Design confirmed |
| SIM-H-12-F3 | Hold plan produces controlled, non-decisive outcome — non-greedy correct | Design confirmed |
| SIM-H-13-F1 | PP-253 Anchor fires ~55% of cases — meaningful mechanical distinction | PP-253 validated |
| SIM-H-13-F2 | Territorial Mending RS gain (+4 provisional) may be too impactful | ED-162 flagged |
| SIM-H-13-F3 | Territorial scale: Coherence −2 per op → Coherence 0 after 5 ops (campaign arc) | Design confirmed |
| SIM-H-13-F4 | Non-greedy restraint preserves Coherence — system correctly incentivises | Design confirmed |

## NEW GAPS AND EDITORIALS

| ID | Description | Type |
|----|-------------|------|
| ED-161 | Lenneth Thread Sensitivity undefined in any canonical doc | Editorial, P2 |
| ED-162 | Mending RS gain by scale undefined — provisional +1 per scale tier above Object | Editorial, P2, FLAGGED |
| GAP-H-06 | No rule for PC-held incorrect NPC information — GM guidance only | Gap, P2 |

## COVERAGE MATRIX ADDITIONS

| SIM-H-08 | Debate CLASH no Inspiration (conserved), solo orator | TTRPG | PRES | Conviction Track, TC | Church, Parliament | Halvard, Church NPC | Church-Renegade | COMPLETE | SIM-H-08-F1; stalemate without trivialisation |
| SIM-H-09 | Circles, Belief conflict, evidence chain | TTRPG | PRES | Momentum, Belief | Crown | Aldric, Torben | Soldier-Agent | COMPLETE | SIM-H-09-F1/F2; Belief rewrite trigger |
| SIM-H-10 | Past-Oriented Pull, TS cliff, non-aggressive withdrawal | TTRPG | PRES/PAST | RS, TS, Coherence, TPS | Unaffiliated | None | Scholar-Practitioner | COMPLETE | SIM-H-10-F1/F2/F3; ED-161 |
| SIM-H-11 | Appeal, Domain Echo PP-252, Belief avoidance | TTRPG | PRES | Mandate, Guilds Intel | Guilds, Hafenmark | Vennrich Solt | Guilds-Fixer | COMPLETE | SIM-H-11-F1/F2/F3; GAP-H-06 |
| SIM-H-12 | PP-248 Discipline degradation validation, Battle Plans PP-235, Domain Echo | TTRPG mass | PRES | Size, Discipline, Morale, Military | Crown, Varfell | Arend (advisory) | Soldier-Agent | COMPLETE | SIM-H-12-F1/F2/F3; PP-248 validated |
| SIM-H-13 | PP-253 Collective Forgetting Anchor, Territorial Mending, Coherence arc | TTRPG | PRES | RS, Coherence, TS, Forgetting | None | Mira, Dagmara | Scholar-Practitioner, Church-Renegade | COMPLETE | SIM-H-13-F1/F2/F3/F4; ED-162 |
