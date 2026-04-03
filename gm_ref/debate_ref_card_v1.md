# VALORIA DEBATE — GM REFERENCE CARD
## Version: v1.5 | Source: debate_system_redesign_v1.md Part 6
## Print double-sided. Keep face-up during all debate scenes.

---

## SIDE A — SETUP & EXCHANGE FLOW

### 1. PRE-DEBATE SETUP (§6.1)

**Question type → Primary genre:**
| Question | Genre |
|----------|-------|
| "Did X happen?" | **Past** |
| "Is X true / Is this person fit?" | **Present** |
| "Should we do X?" | **Future** |

**Genre weights — set once, fixed:**
| Genre | Base weight | Audience boost (+0.5) |
|-------|------------|----------------------|
| Primary | ×1.0 | If audience ethical mode matches |
| Other two | ×0.5 | — |

| Audience | Boosted genre |
|----------|--------------|
| Crown (virtue ethics) | Present |
| Church (divine command) | Past |
| Hafenmark (categorical imperative) | Past |
| Varfell (consequentialism) | Future |
| Restoration (Rawlsian) | Future |
| Guilds (moral relativism) | GM chooses |

**Conviction Track:** 0–10. A wins ≥7. B wins ≤3. Compromise 4–6.
**Starting position:** GM-set (neutral = 5). Record in ledger.
**Resistance:** avg faction Stability of audience, round up, −1. Min 0. Typical: 0–2.

**Orientation:** Revealing ×1.0. Obscuring → Doubt Marker (no track movement).

---

### 2. EXCHANGE FLOW (§6.4)

```
STEP 1 — READ (both, Attunement only, TN7 Ob1)
  0 net  → Misleading signal (GM names a wrong genre as strong)
  1 net  → Primary genre only
  2 net  → Primary genre + orientation preference
  3+ net → Genre + orientation + one specific detail

STEP 2 — CHOOSE genre (Past/Present/Future) + orientation (Revealing/Obscuring)

STEP 2b — CORROBORATE (optional, before arguing)
  Corroborator rolls Bonds, TN7, Ob1 (Ob2 in asymmetric proceedings)
  Success → +1D to Lead's Argue roll this exchange (max 1 corroborator/side/exchange)
  Failure → corroborator takes 1 strain (asymmetric only)

STEP 3 — ARGUE (initiative holder declares + rolls first)
  Pool: (Presence × 2) + History bonus, TN7 (no fixed Ob — comparative)
  Memory bonus: +2D if citing specific named verifiable claim
  Momentum: spend 1 before rolling → +1 automatic success

STEP 4 — RESOLVE (identify interaction type, apply formula)
  → See SIDE B for full resolution tables

STEP 5 — FORFEIT ACTIONS (if applicable)
  Regroup: no argument, no strain, TC +1 toward opponent, Concentration +Focus
  Concede: 1 strain, TC +1 toward opponent, +1D next argue roll

STEP 6 — UPDATE STRAIN & CONCENTRATION
  Strain → Composure (at ≥ Composure: RATTLED −2D all debate, Focus def lost)
  Concentration −1 per exchange, −1 more if you lost (min 0; at 0: SPENT −2D, opp +1D)
  Rattled + Spent together: −4D total, pool min 1D

STEP 7 — GM RECORDS on hidden ledger
```

---

### 3. INITIATIVE

| Situation | Who holds |
|-----------|----------|
| Exchange 1 | Higher Presence |
| After CLASH/COMPETITION win | Winner |
| After DIVERGENCE | Unchanged — stays with holder |
| Tie in any exchange | Unchanged |
| Asymmetric proceedings | Institution always |

---

### 4. DERIVED VALUES (§6.2)

| Value | Formula |
|-------|---------|
| Argue pool | (Presence × 2) + History |
| Presence modifier | max(0, floor((Pres−3)/2)) → Pres 1–3: +0; 4–5: +1; 6–7: +2 |
| Focus defence | floor(Focus / 2) |
| Composure | Poise + Bonds + 3 |
| Concentration | Focus + Presence |
| Read pool | Attunement only (no History) |

---

## SIDE B — RESOLUTION, STATES & PROCEEDINGS

### 5. INTERACTION RESOLUTION (§6.4 Step 4)

**INTERACTION TYPE — identify first:**
| Condition | Type |
|-----------|------|
| Same genre, opposite orientation | CLASH |
| Same genre, same orientation | COMPETITION |
| Different genres | DIVERGENCE |
| Equal successes (any type) | TIE |
| Winner used Obscuring | OBSCURING WIN |

---

**CLASH** (same genre, opposite orientation):
```
  1. margin = |A successes − B successes|
  2. effective_margin = floor(margin × genre_weight × 1.0)
  3. if effective_margin > resistance → TC moves (effective_margin − resistance) toward winner
     else → 0 movement
  4. Strain to loser = margin + 1 + winner_Pres_mod − loser_Focus_def (min 1)
```

**COMPETITION** (same genre, same orientation):
```
  Same as CLASH except:
  Strain to loser = (margin − 1, min 1) + 1 + winner_Pres_mod − loser_Focus_def (min 1)
```

**DIVERGENCE** (different genres):
```
  Each side evaluated independently:
    effective_margin = floor((own successes / 2) × own genre_weight)
    (negative successes → treat as 0)
  if effective_margin > resistance → Δ = effective_margin − resistance toward own position
  Net TC = Δ_A − Δ_B (toward larger delta's side)
  No strain. Initiative stays with holder.
  If both score 0: TIE fires (1 strain each, TC +1 toward initiative holder)
  If Obscuring winner has larger delta: Doubt Marker instead of track movement
```

**TIE:**
```
  Both take 1 strain. TC +1 toward initiative holder. Initiative stays.
```

**OBSCURING WIN:**
```
  TC does NOT move toward winner.
  Place Doubt Marker on opponent.
  Doubt Marker: opponent's next winning exchange effective_margin −2 (before resistance).
  Only 1 active at a time. Second Obscuring win replaces existing marker. Consumed on use.
```

---

### 6. CONVICTION TRACK QUICK-MATH

```
  effective_margin = floor(margin × weight)   [weight = 0.5 / 1.0 / 1.5]
  movement = effective_margin − resistance     [if > 0; else 0]

  Genre weight × resistance → minimum margin to move TC:
  weight 0.5, res 1: margin ≥ 3 needed    weight 0.5, res 2: margin ≥ 5
  weight 1.0, res 1: margin ≥ 2 needed    weight 1.0, res 2: margin ≥ 3
  weight 1.5, res 1: margin ≥ 2 needed    weight 1.5, res 2: margin ≥ 2
```

---

### 7. POST-DEBATE (§6.5)

| TC position | Outcome |
|-------------|---------|
| ≥ 7 | Side A wins |
| ≤ 3 | Side B wins |
| ≥ 9 or ≤ 1 | Total Victory — extra consequences |
| 4–6 | Compromise |

**Domain Echo by winning genre:**
| Genre | Echo |
|-------|------|
| Past (Evidence) | Winning faction Mandate +1 |
| Present (Character) | Disposition change + Reputation shift |
| Future (Consequence) | +1D on first Domain Action pursuing argued future this season |

**Debate Fatigue:** Orator Rattled at any point → −1D next social roll (consumed on use). One per session.
**Total Victory extras:** Losing orator gets Debate Fatigue; winning orator +1 Momentum.
**Recovery:** All strain, Rattled, Spent clear at scene end.

---

### 8. PROCEEDING TYPES (§6.7)

| Type | Exchanges | Roles | Resistance | Notes |
|------|-----------|-------|------------|-------|
| Formal Debate | 3 | Alternating | Standard | Parliament default |
| Grand Debate | 5 | Alternating | Standard | Faction-defining |
| Royal Audience | 3 | Crown objects throughout | Halved for petitioner | — |
| Church Tribunal | 1–5 (Inquisitor sets) | Inquisitor proposes | Halved for accused | TC start biased toward institution. Set ≥3 exchanges for drama. |
| Casual Dispute | 1 | Initiator proposes | N/A (no TC) | No Thread consequences |
| Private Negotiation | 1–2 | Symmetric | 0 | No TC unless GM opts in |

**Asymmetric:** Advantaged orator 0 strain in DIVERGENCE (by design). Accused corroborates at Bonds Ob 2.
**Proposer role alternates independently of initiative transfer.**

---

### 9. SCALE VARIANTS (§§6.11–6.15)

**Pre-Debate Preparation** (§6.11, 1+ hr prep, Attunement+History TN7 Ob1):
Success → +1D Exchange 1 Argue. Overwhelming → also TN6 Read Exchange 1.

**Multi-Party Coalition** (§6.12): Lead rotates. Only Lead's Concentration depletes. Corroboration: Bonds Ob1, max 1/side/exchange. All Rattled → side must Regroup.

**BG Parliamentary Vote** (§6.13): Pool = sum of coalition Mandate. effective_vote = floor(net × genre_weight). Movement = effective_vote − resistance (base 0). Lobbying: prior Diplomacy domain action → TC start ±1 (max ±2). Both sides 0 → committee referral.

**Hybrid Debate** (§6.14): BG vote first → TC offset ±2 (capped). Then TTRPG debate from adjusted start. Exchange count: GM sets per context.

**Thread operations** (§6.15): R-65 during Argue step (visible). Between-exchange ops resolved after Step 7. Genre weights immutable. Observed weaving → Church Heresy Investigation (Domain Action Ob 2).

---

### 10. PROBABILITY QUICK REFERENCE (TN7)

| Pool | E[net] | P(≥1) | P(≥2) | P(≥3) |
|------|--------|--------|--------|--------|
| 4D | 1.3 | 80% | 50% | 25% |
| 6D | 2.0 | 92% | 70% | 45% |
| 8D | 2.6 | 97% | 82% | 60% |
| 10D | 3.3 | 99% | 90% | 73% |
| 12D | 4.0 | 99% | 95% | 83% |
| 15D | 5.0 | 99% | 98% | 92% |

**Typical argue pools (Presence × 2 + History):**
Pres 3 + Hist 2 = 8D. Pres 4 + Hist 3 = 11D. Pres 5 + Hist 3 = 13D. Pres 6 + Hist 3 = 15D.

**Thread + Debate (§6.15):**
R-65 during Argue: TS 30–59 +1D, TS 60–89 +2D, TS 90+ +3D. Visible — Church may Investigate.
Between-exchange ops: resolve after Step 7. Genre weights fixed — Thread cannot change them.
**Temporal axis conflict (PP-123):** Past-axis Thread op during Future-genre debate (or reverse) → both orators Read TN 8 next exchange.

---

*Valoria Debate Reference Card v1.5 | designs/debate/debate_system_redesign_v1.md*
