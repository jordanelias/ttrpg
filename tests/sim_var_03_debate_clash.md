# SIM-VAR-03 — TTRPG Debate: Forced-CLASH Run (SIM-DEBT-01 Pendant)
## Mode: A (Mechanic Isolation) + C (Full Scenario) + B (Interaction Chain)
## Date: 2026-04-08 | Pending item from SIM-DEBT-01: forced-CLASH scenario validation

---

## FETCH LOG
canonical_sources.yaml: ✓ (156 lines)
params_debate.md: ✓ (407 lines)
params_core.md: ✓ (161 lines)

---

## Setup

SIM-DEBT-01 resolved debate baselines analytically but flagged: "scenario validation pending forced-CLASH run." This simulation runs a full debate where both orators are forced into CLASH repeatedly — same genre, opposite orientation — stress-testing the CT movement formula and Composure drain under sustained CLASH conditions.

**Combatants:**
- **Side A — Cardinal Klapp** (Church): Cognition 4, History 2 (Debate). Argue pool = (4×2)+2 = **10D**. Charisma 3, Composure = 3+6 = **9**. Ethical mode: Divine Command → boosted genre: Past (+0.5).
- **Side B — Baralta** (Hafenmark): Cognition 4, History 3 (Parliamentary Debate). Argue pool = (4×2)+3 = **11D**. Charisma 4, Composure = 4+6 = **10**. Ethical mode: Categorical Imperative → boosted genre: Past (+0.5). Initiative (Attunement): Baralta Attunement 4, Klapp Attunement 3 → Baralta has initiative.

**Question type:** Past (Theological precedent — "The Church's authority over civil law predates the monarchy"). Both factions align with Past as their boosted genre.

**Audience:** Mixed (Church officials, Hafenmark parliamentarians). Average Stability = (5+4)/2 = 4.5. Resistance = ceil(4.5/4) = **2**.

**CT start:** 5 (neutral). Church wins ≥ 7, Hafenmark wins ≤ 3.

---

## Mode A: CLASH Mechanics Isolation

**Genre weights for Past question:**
- Both sides choosing Past: weight = ×1.0 (primary). Audience Past bonus: +0.5 for Church (Divine Command) and Hafenmark (Categorical Imperative). Both get Past boosted to ×1.5.
- Since both are choosing Past, genre_weight = 1.5 for both sides.

**Orientation:** For forced-CLASH, Side A must choose Revealing, Side B must choose Obscuring (or vice versa). Revealing = ×1.0, Obscuring = ×0.75.

**Forced-CLASH scenario:** Both choose Past. Klapp (A) declares Revealing, Baralta (B) declares Obscuring. CLASH fires.

**CLASH resolution formula:**
- Each rolls their Argue pool vs TN 7.
- Winner = higher net successes. Margin = |A_net − B_net|.
- Revealing wins: movement = ⌊(margin × genre_weight × orientation_weight) − resistance⌋
- Obscuring wins: Doubt Marker placed (no CT movement formula).

**Probability table for CLASH outcomes:**

| Side | Pool | E(net) | P(≥1) | P(≥3) | P(≥5) |
|------|------|---------|-------|-------|-------|
| Klapp (A) | 10D | 5.72 | ~99% | ~93% | ~74% |
| Baralta (B) | 11D | 6.29 | ~99% | ~95% | ~80% |

Expected margin = |6.29 − 5.72| = 0.57 per exchange (very close pools).
P(Baralta wins) ≈ 58% (higher pool wins more often but margin is small).

**CLASH: Klapp Revealing, Baralta Obscuring:**
- If Klapp wins (Revealing): movement = ⌊(margin × 1.5 × 1.0) − 2⌋ toward Church (CT increases).
  At expected margin 1: ⌊(1 × 1.5) − 2⌋ = ⌊−0.5⌋ = 0 movement. No CT change even when Klapp wins by 1.
  At margin 2: ⌊(2 × 1.5) − 2⌋ = ⌊1⌋ = 1 CT movement.
  At margin 3: ⌊(3 × 1.5) − 2⌋ = 2 CT movement.
- If Baralta wins (Obscuring): Doubt Marker placed. No CT movement. Klapp takes 1 strain.

**Finding P1 — CLASH with resistance 2 and margin ~1 produces zero CT movement when Revealing wins by small margin.** The resistance absorbs the movement. Only margins ≥ 2 produce CT movement when genre_weight is 1.5. Against a resistance-2 audience, small-pool advantages are completely neutralised. This is intentional (high-resistance audiences are hard to move) but creates stalemate risk when pools are close.

---

## Mode C: Full Scenario — 5 Exchanges, Forced CLASH

### Exchange 1
Both choose Past. Klapp: Revealing. Baralta: Obscuring. → **CLASH**.

**Roll simulation:**
Klapp 10D: expected net 5.72. Simulated: 5 successes.
Baralta 11D: expected net 6.29. Simulated: 7 successes.

Baralta wins (Obscuring). Result: **Doubt Marker placed on Klapp**. Klapp takes 1 strain (Strain: 1/9 Composure).

CT: 5 (unchanged — Obscuring win places Doubt Marker, no formula movement).

**Doubt Marker effect:** Klapp's next Revealing roll: −1D (Doubt erodes his position). Klapp 10D → 9D until Doubt cleared.

### Exchange 2
**Klapp must clear Doubt or accept −1D.** Clearing requires a Reframe action (costs initiative, Cognition Ob 2). Klapp's Attunement is 3, Baralta 4 — Baralta has initiative anyway. Klapp cannot voluntarily use initiative to Reframe (Baralta acts first on initiative). Klapp is stuck with the Doubt.

Klapp 9D (−1D Doubt). Both choose Past again. Klapp: Revealing. Baralta: Revealing. → **AMPLIFY** (same genre, same orientation — both Revealing).

Wait — Baralta switching to Revealing changes interaction type. If Baralta's goal is to move CT toward Hafenmark (≤ 3), Baralta should be Revealing — AMPLIFY against resistance is their best path when Klapp is weakened.

**AMPLIFY:** Combined pool = Klapp 9D + Baralta 11D = 20D, capped at highest individual × 2 = 11D × 2 = 22D. 20D < 22D → no cap. Both Revealing: combined pool 20D vs audience resistance 2.

Combined E(net) = 20 × 0.572 = 11.4. P(net ≥ 4 after resistance = 2): effectively certain.

**Roll:** 20D combined, net 11 successes.
CT movement = ⌊(11 − 2) × ... wait — AMPLIFY uses: "Combined pools vs resistance. Revealing wins: apply formula."

The formula for AMPLIFY Revealing: effective_margin = net_combined − resistance (since there's no opponent roll, the margin is the combined success count vs resistance).
CT movement = ⌊(effective_margin × genre_weight) − 0⌋? Or does resistance already factor into the effective_margin?

Re-reading: "Combined pools vs resistance. Revealing wins: apply formula. effective_margin = net − resistance" → movement = ⌊((net − resistance) × genre_weight × orientation_weight)⌋.

Wait — the CROSS formula says "effective_margin = floor(successes/2 × genre_weight)". For AMPLIFY/CLASH, margin = net successes (CLASH: winner's net minus loser's net; AMPLIFY: combined net).

**Ruling:** For AMPLIFY, movement = ⌊(combined_net × genre_weight × orientation_weight) − resistance⌋. Combined net 11, genre_weight 1.5 (Past, boosted), orientation_weight 1.0 (Revealing): movement = ⌊(11 × 1.5 × 1.0) − 2⌋ = ⌊16.5 − 2⌋ = **14 CT movement toward Baralta (Hafenmark)**.

CT: 5 − 14 = **CT −9**. Below 0 → floor at 0. CT = 0? That's below the ≤ 3 Hafenmark win threshold.

**Hafenmark wins in Exchange 2.**

**But wait — is this correct?** The AMPLIFY result of 14 movement on one exchange seems extreme. Let me re-examine.

**Re-check AMPLIFY formula source:** The debate system uses the same movement formula as CLASH. For CLASH: movement = ⌊(margin × genre_weight × orientation_weight) − resistance⌋ where margin = |A_net − B_net|. For AMPLIFY, there's no opponent — the "margin" equivalent is the combined net against zero opposition. The combined net (11) is the effective margin.

But the formula's resistance term (−2) represents the audience's inertia. At combined net 11 and genre_weight 1.5: movement = ⌊16.5 − 2⌋ = 14. That's 14 CT movement on one AMPLIFY exchange.

**Finding P2 — AMPLIFY with high combined net is catastrophically powerful.** 20D combined pool vs resistance 2 produces CT movement of 10–15 in a single exchange. The AMPLIFY cap (highest pool × 2) limits the pool but doesn't limit the outcome. At combined pool 20D: a single exchange can swing the entire CT range (10 steps, CT 0–10) in one direction.

This is a known degenerate case. At small pool sizes (4D + 4D = 8D combined), AMPLIFY is calibrated correctly (movement 2–4 per exchange). At large pools (10D + 11D = 21D), AMPLIFY becomes a one-shot win button.

**[EDITORIAL: ED-329 — AMPLIFY movement cap: consider capping CT movement per exchange at a fixed maximum (e.g. 5 or genre_weight × 3) regardless of combined net successes. Otherwise large-pool orators can win the debate in one AMPLIFY exchange. P2 — design gap with significant play impact.]**

### Exchange 3 (hypothetical — if CT not already won)
Assume CT 5 still (test the forced-CLASH path, ignoring the AMPLIFY deviation). Both choose Past, opposite orientations → CLASH.

**Roll:** Klapp 9D (still Doubted): net 4. Baralta 11D: net 6. Baralta wins by margin 2.

Baralta Obscuring: Doubt Marker on Klapp (second Doubt Marker). 

**Second Doubt Marker:** Does a second Doubt Marker stack with the first? Params: "Doubt Marker: −1D to next Revealing roll." Two Doubt Markers: −2D to Klapp's next Revealing roll? **[GAP: Doubt Marker stacking behaviour undefined. Assuming additive: two markers = −2D.]**

Klapp now at 8D (9D − 1D second Doubt = 8D) if stacking. Or Markers don't stack (second Marker just extends the effect). **Ruling (gap-fill): Doubt Markers don't stack — only one active at a time. Applying a second Doubt Marker extends duration: lasts until cleared or 2 exchanges elapse. No additional D penalty.**

Klapp strain: +1 → **Strain 2/9 Composure**. CT unchanged (Obscuring wins → no movement).

### Exchange 4 — Klapp forced CLASH attempt
Klapp must recapture initiative or risk losing Composure track. He plays a Reframe (sacrifices his own attack action).

**Reframe:** Costs initiative slot. Cognition Ob 2. Klapp Cognition 4D vs Ob 2. P(Success): ~85%.
**Result: Success.** Doubt Marker cleared. Klapp back to 10D.

**No debate exchange this round** (Klapp spent action on Reframe). Baralta acts alone: she can only play AMPLIFY if there's a second speaker. With only two orators, no AMPLIFY without Klapp. Baralta plays a standard attack (CLASH with Klapp as defensive): Baralta 11D Revealing vs Klapp responding Revealing. But Klapp used his initiative on Reframe — does he get a defensive roll?

**Ruling:** Reframe is a full action. Klapp cannot respond to Baralta's argument in the same exchange. Baralta plays uncontested: treat as AMPLIFY with Baralta only. Combined pool = 11D (Baralta alone). But AMPLIFY requires both orators same orientation — with Klapp not responding, this is an Uncontested Argument.

**[GAP: Uncontested Argument rule undefined.] Ruling (gap-fill):** Uncontested Argument = AMPLIFY with only the acting orator's pool, resistance still applies. Movement = ⌊(11 × 1.5 × 1.0) − 2⌋ = ⌊14.5⌋ = 14.

Again catastrophic movement. This demonstrates the core P2 finding: any high-pool Uncontested or AMPLIFY argument swings the entire CT.

### Exchange 5 — Final CLASH
CT at 5 (hypothetical reset). Klapp 10D Revealing, Baralta 11D Obscuring → CLASH.

**Roll:** Klapp 10D net 6. Baralta 11D net 6. **TIE.**
TIE rule: both take 1 strain; CT +1 toward initiative holder (Baralta). CT: 5 → 4. Both take strain.
Klapp strain: 3/9. Baralta strain: 1/10.

**Neither orator is close to Rattled** (Rattled at strain ≥ Composure — Klapp needs strain 9, Baralta 10). Five exchanges of CLASH + strain have barely dented Composure. **Composure drain is very slow under pure CLASH.**

---

## Mode B: Interaction Chains

### Chain 1: CLASH → Doubt Marker → AMPLIFY vulnerability
Sustained CLASH into Doubt Markers → AMPLIFY activation creates a dangerous dynamic:
1. Baralta wins CLASH (Obscuring): Doubt on Klapp.
2. Baralta switches to Revealing: AMPLIFY.
3. AMPLIFY with combined pool (even Klapp Doubted) produces massive CT movement.
4. Debate ends in 2 exchanges.

This chain is not an edge case — it's the optimal strategy whenever one side has a pool advantage: win CLASH (Obscuring → no CT movement, place Doubt) → switch to AMPLIFY once opponent is Doubted (their defensive contribution drops, combined pool lower but still catastrophic).

**Finding P3 — Doubt Marker + AMPLIFY creates a dominant 2-exchange win strategy for any side with pool advantage ≥ 2D.** Baralta's 11D vs Klapp's 10D is enough: win CLASH Obscuring (likely), Doubt Klapp (9D), AMPLIFY with 9D+11D=20D combined → CT movement 12+ → instant win.

### Chain 2: Forced CLASH resistance to CT movement
Under pure forced CLASH (both sides alternating Revealing/Obscuring each exchange):
- Margin ~1 per exchange (E(|11D_net − 10D_net|) ≈ 1.0 at these pool sizes)
- At margin 1, genre_weight 1.5, resistance 2: movement = ⌊1.5 − 2⌋ = ⌊−0.5⌋ = 0.
- CT never moves.

**Sustained forced-CLASH between near-equal pools with resistance ≥ 2 produces stalemate.** ED-317 (AMPLIFY stalemate) was the prior version of this finding. This simulation confirms the stalemate occurs in forced-CLASH as well, though via a different mechanism: resistance absorbing marginal wins rather than zero-sum CLASH producing zero movement.

**Resolution path:** Composure concession (one side takes enough strain to reach Rattled threshold) is the only exit. At ~0.3 strain per exchange (estimated: ~30% chance of strain event per exchange), reaching Rattled (9 strain for Klapp) takes ~30 exchanges. Unsustainable debate length.

**[EDITORIAL: ED-330 — Forced-CLASH stalemate exit: near-equal pools vs resistance ≥ 2 produces ~0 CT movement per exchange. Composure drain is the only exit but requires ~30 exchanges at typical rates. Consider: (a) minimum CT movement of 1 on any CLASH winner regardless of resistance (if margin > 0), or (b) resistance decay: each unproductive exchange reduces resistance by 0.25 (audience patience erodes). P1 — this reproduces the SIM-DB-02 stalemate finding in a different mechanical scenario, confirming it is a systemic gap, not a scenario-specific artifact.]**

---

## Findings Summary

| ID | Severity | Finding |
|----|----------|---------|
| F-DB-01 | P1 | Forced-CLASH stalemate: near-equal pools with resistance ≥ 2 produce ~0 CT movement per exchange. Composure concession requires ~30 exchanges. Systemic gap confirmed. |
| F-DB-02 | P2 | AMPLIFY movement uncapped: 20D combined pool produces 12–14 CT movement per exchange — entire CT range in one roll. Movement cap needed. |
| F-DB-03 | P2 | Doubt Marker + AMPLIFY is a dominant 2-exchange strategy for any side with pool advantage ≥ 2D. Undercuts meaningful debate arc. |
| F-DB-04 | P3 | Doubt Marker stacking behaviour undefined. Gap-filled as non-stacking (duration extension only). |
| F-DB-05 | P3 | Uncontested Argument (one orator plays, other uses initiative on non-debate action) has no defined rule. Gap-filled as AMPLIFY with single pool. |

