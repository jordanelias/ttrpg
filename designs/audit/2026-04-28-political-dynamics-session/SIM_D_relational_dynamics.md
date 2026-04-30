<!-- [PROVISIONAL: 2026-04-29 — simulation Direction D] -->
<!-- STATUS: PROVISIONAL — granular trace of relational dynamics under doc 12 v1.1 -->
<!-- POSITION: designs/audit/2026-04-28-political-dynamics-session/SIM_D_relational_dynamics.md -->
<!-- COMPANION: SIM_A, SIM_B, SIM_C; 12_development_specification.md v1.1 -->

# Simulation D — Relational Dynamics (Standing recalc, Outreach, Knot, Memory replacement)

**Source spec:** `12_development_specification.md` v1.1 (commit `9dede391`).
**Primary patches under test:** PATCH 3.10 (Outreach P3 default + escalation); PATCH 3.6 (Knot via P2 Outreach); PATCH 3.11 (Standing recalc §8.1); PATCH 3.15 (Passive Memory replacement at 3-cap); §1.1 featured behaviors (E-DIAG-A diagonal chain, N-DIAG-A Standing milestone).
**Method:** Eight scenarios traced with explicit state transitions. Relational invariants verified.

---

## §0 Conventions

NPCs: Almud (Crown leader, S7, Order), Marshal (S7, Order), Confessor (S5, Faith), Ambassador (S4, Continuity), Reformer (S3, Autonomy), Spouse (Knot partner of Player, S5 Crown, Faith). Passive: Baker_Solmund (3-Memory cap).

### 0.1 Relational invariants under test

- **`[REL-INV-1]` Outreach priority correctness.** P3 default; escalates to P2 only when `salience ≥ 5 AND ttl ≤ 1`. P3-skipped does not consume slot.
- **`[REL-INV-2]` Knot opacity preserved.** Knot information goes through P2 Outreach scene; player must attend; no auto-disclosure.
- **`[REL-INV-3]` Standing change generates event.** PATCH 3.11 emits `standing_change` propagated to inner-circle peers.
- **`[REL-INV-4]` Memory replacement deterministic.** merge → drop-lowest-salience → drop-older. Same input → same outcome.
- **`[REL-INV-5]` Standing milestone scene fires on 3↔4 crossing.** Per N-DIAG-A featured behavior.
- **`[REL-INV-6]` Outreach tone reflects mood.** Per PATCH 3.10.

---

## §1 Scenario 1 — P3 Outreach skipped, no consequence (PATCH 3.10 default path)

**Setup.** Confessor.concerns = [Concern(c-001, "doctrinal_question", subject=Player, salience=2, ttl=4)]. Confessor.mood=Steady.

**Trace.** End of T+0 Procedure E generates Outreach for c-001. Salience 2 (<5), ttl 4 (>1) → **Priority 3 default**. Tone: Steady → contemplative. Player T+1: skips slot 3. Per PATCH 3.10, "scene does not consume a slot, Concern continues normal decay."

**T+1 Procedure B Resolution:** c-001.salience: 2→1, ttl: 4→3.

**Verification.** `[REL-INV-1]` ✓ default P3. `[REL-INV-6]` ✓ Steady → contemplative. **Knock-on:** Repeated P3 skip across Accountings → c-001 decays naturally to 0 → auto-resolves at salience-0 OR ttl-0 → Memory generated with `resolution.implied_affect ~ -0.5` (mild negative). **Strategic property:** P3-skip has *delayed mild negative consequence* over 4 seasons, not zero. Player can manage relational budget by choosing which P3s to attend.

**`[GAP: SIM-D-G1]` Dissipation `implied_affect` default unspecified.** Recommend -0.5 default for `concern_dissipated_without_engagement` event_type. v1.2 spec target.

---

## §2 Scenario 2 — P3 → P2 escalation at salience-5 + ttl-1

**Setup.** Marshal.concerns = [Concern(c-100, "treaty_violation_by_player", subject=Player, salience=4, ttl=2, mood=Anxious)]. Player has skipped Marshal's outreach for 2 prior Accountings.

**T+3 → T+4 escalation trigger.** New evidence (Memory at salience 5) bumps c-100.salience: 4→5. ttl: 2→1.

**End of T+3 Procedure E:** `c-100.salience >= 5 AND ttl <= 1` → **escalate to Priority 2 mandatory**. Outreach{npc=Marshal, type=treaty_inquiry_demand, priority=2, tone=Anxious_pressed}.

**T+4:** Mandatory slot. Player must attend (or sacrifice all other Slate slots).

If attended: scene plays; resolution Memory generated; standard Direction-A processing. If refused: `evasion_observed` event spawns Concern in Marshal's queue ("Player is hiding something"); Mood shift; potential Loyalty Interview escalation next Accounting.

**Verification.** `[REL-INV-1]` ✓ escalation correct. **One-Accounting-only:** "for that Accounting only" — Marshal's Outreach drops back from Slate after this turn; doesn't persist as P2. ✓

**`[GAP: SIM-D-G2]` P2-evasion event handling unspecified.** Recommend `evasion_observed` event spawning Concern with salience+1 and Mood shift. v1.2 spec target.

---

## §3 Scenario 3 — Knot integration via P2 Outreach (PATCH 3.6)

**Setup.** Spouse.concerns = [Concern(c-200, "marital_distance_growing", subject=Player, salience=3, ttl=4, mood=Anxious)]. Spouse and Player share a Knot.

**End of T+0 Procedure E (Knot integration step per PATCH 3.6):**
- Spouse has active Concern about Player at salience ≥ 2 → qualifies.
- Generate Outreach Slot for T+1: **Priority 2 mandatory** (per PATCH 3.6).
- Outreach{npc=Spouse, type=marital_dialogue, priority=2, tone=Anxious_intimate, revealed_concern=c-200.tag}.

**Crucial:** Player learns c-200 only through scene attendance. No automatic disclosure (pre-PATCH-3.6 behavior eliminated).

**T+1 attendance:** Player attends (mandatory). Dialogue choices determine resolution affect:
- Show up emotionally → Spouse Mood shifts toward Steady; c-200 resolves with positive affect (~+1.5).
- Deflect → c-200.salience may bump to 4 (deepening); Spouse Mood → Distracted.
- Invoke pressing affairs → Spouse Mood → Distracted; c-200 persists.

**Verification.** `[REL-INV-2]` Knot opacity preserved ✓. `[REL-INV-1]` Knot Outreach is P2 (not P3) — exception to default rule. ✓ Per PATCH 3.6 spec, Knot Outreach is P2 regardless of salience-5 threshold (because Knot is special).

**Cross-direction:** Resolution Memory feeds Procedure D (SIM-A path); Spouse's Opinion of Player drifts based on dialogue outcome. Direction A and Direction D interlock through scene-mediated Memory generation. ✓

**`[GAP: SIM-D-G3]` PATCH 3.6 + 3.10 interaction for Knot-partner-about-player Concerns: PATCH 3.6 (P2 mandatory) supersedes PATCH 3.10 (P3 default). v1.2 minor doc clarification.**

---

## §4 Scenario 4 — Standing change cascade: Confessor S5 → S7 (large jump)

**Setup.** End of Campaign Year 2. Confessor counters: completed_projects=2, failed_projects=0, successful_da_proposals=4 (capped at +1.0), failed_da_proposals=1, public_conviction_scars=0.

**PATCH 3.11 calculation:**
```
Δ_standing = +0.5×2 - 0.5×0 + 0.25×4 (cap +1.0) - 0.25×1 - 0.5×0
           = +1.0 + 1.0 - 0.25 = +1.75
Δ_standing = clamp(+1.75, -2, +2) = +1.75
Confessor.standing = round(clamp(5 + 1.75, 3, 7)) = round(6.75) = 7
```

**S5 → S7 jump in one year.** No 3↔4 crossing → **N-DIAG-A milestone scene does NOT fire**. But standard `standing_change` event fires per PATCH 3.11.

**Event propagation:**
```
e-201: standing_change(Confessor, +2, year=2). visibility=public.
  affected_npcs: [Almud, Marshal, Ambassador]. salience=4.
```

T+1 Procedure B Generation: each peer observes (visibility public), derives Concern about Confessor's elevation, salience=4. Concerns resolve next Accountings → Memories → Procedure D Opinion drift toward Confessor (positive or negative depending on prior relation).

**Faction Meta-Armature update:** Confessor's contribution rises 0.5/total → 1.0/total. Faith weight in Crown aggregate: ~0.13 → ~0.20. Future `select_proposal()` calls (Direction B) favor theological proposals more. **Cumulative drift: Crown's strategic flavor tilts toward Faith.** Realistic political consequence of internal promotion.

**Verification.** `[REL-INV-3]` Standing-change event ✓. `[REL-INV-5]` milestone — did NOT fire because no 3↔4 crossing. **N-DIAG-A label is misleading: title says "Standing 5" but body specifies 3↔4 transition.**

**`[GAP: SIM-D-G4]` N-DIAG-A title vs body inconsistency.** Title "Standing 5 Milestone" but body describes 3↔4 transition. Recommend rename to "Inner-Circle Threshold Milestone (Standing 3↔4)." v1.1 typo / v1.2 clarification target.

**`[OBSERVATION: SIM-D-O1]` Per-year clamp ±2 allows two-step Standing jumps (S5→S7 in single year). May be too generous. Renaissance promotions typically multi-year. v1.2 design call — consider tightening clamp to ±1 per year for slower trajectory.**

---

## §5 Scenario 5 — Standing 3↔4 transition (true N-DIAG-A milestone)

**Setup.** End of Campaign Year 1. Reformer (S3, Autonomy primary, peripheral). Counters: completed_projects=1, failed_projects=0, successful_da_proposals=3, failed_da_proposals=2 (lost competitions per SIM-B Scenario 8 deadlock), public_conviction_scars=0.

**PATCH 3.11 calculation:**
```
Δ_standing = +0.5 + 0 + 0.75 - 0.5 + 0 = +0.75
Reformer.standing = round(3 + 0.75) = round(3.75) = 4
```

**3 → 4 crossing.** N-DIAG-A milestone scene fires.

**Cascade:**
```
e-301: standing_change(Reformer, +1, year=1). visibility=public. salience=3.
  affected_npcs: [Almud, Marshal, Confessor, Ambassador].

# N-DIAG-A milestone scene next Accounting:
  Scene{type=standing_milestone_adjustment, npc=Reformer, priority=3, 
        tone=Reformer.mood (Vindicated from Y1 success) → triumphant,
        framing="Reformer arriving at Crown's inner circle table for first time"}
```

Player attendance options: sympathetic (builds player↔Reformer Disposition +1), skeptical (neutral or generates Concern from Reformer about Player), skip (drops, no relational event).

Inner-circle peers generate Concerns from e-301. Direction A processing follows: each peer's Opinion of Reformer drifts based on prior relation + dialogue/event resolution.

**Faction Meta-Armature update:** Reformer (Autonomy primary) entering inner circle adds Autonomy weight to Crown's aggregate (formerly negligible at 0.005 → now at S4 weight 0.3/total ≈ 0.06 contribution to Autonomy). Crown becomes very-slightly more Autonomy-receptive in `select_proposal()`. **First Autonomy NPC in Crown inner circle creates new strategic possibilities** for economic/scholarly/intelligence domain proposals.

**Verification.** `[REL-INV-3]` Standing-change event ✓. `[REL-INV-5]` Milestone scene fires correctly on 3↔4 crossing ✓. Cross-direction: Direction A (Memory drift) + Direction B (meta-armature shift) + Direction D (milestone scene) all triggered by single event.

---

## §6 Scenario 6 — Standing demotion: failed-DA-proposal cascade (interaction with SIM-B-G8)

**Setup.** End of Campaign Year 3. Confessor (assume back at S5 after some recovery, or original S5). Year 3 counters: completed_projects=0, failed_projects=0, successful_da_proposals=0, **failed_da_proposals=4** (lost all theological competitions to Almud per SIM-B Scenario 8 deadlock), public_conviction_scars=1 (one public Belief revision).

**Scenario 6a — Liberal interpretation of `failed_da_proposals` (SIM-B-G8 unresolved):**
```
Δ_standing = +0 - 0 + 0 - 0.25×4 (cap -1.0) - 0.5×1 = -1.0 - 0.5 = -1.5
Confessor.standing = round(5 + (-1.5)) = round(3.5) = 4
```

**Confessor demoted to S4.** Still inner circle but at the threshold. Next year another -1 could push him to S3, then potentially S2 → out of inner circle.

**Scenario 6b — Strict interpretation (SIM-B-G8 resolved per recommendation):**
```
Δ_standing = +0 - 0 + 0 - 0.25×0 (no DA-roll-failures, only competition-losses don't count) - 0.5 = -0.5
Confessor.standing = round(5 - 0.5) = round(4.5) = 4 or 5 (depends on rounding rule)
```

**With round-half-to-even:** 4.5 → 4. Confessor still demoted but less harshly.
**With round-half-up:** 4.5 → 5. Confessor stays put.

The two interpretations differ materially. **SIM-B-G8 critical-priority gap is reaffirmed by SIM-D Scenario 6.** The downstream implication is Confessor's potential exit from inner circle vs continued participation. **Resolves as P1-CRITICAL for v1.2.**

**Cascade if demoted (6a):**
```
e-401: standing_change(Confessor, -1, year=3). visibility=public. salience=3.
  N-DIAG-A milestone scene fires (5→4 crossing inner-circle threshold from above).
  Scene tone: somber_or_diminished.

# Faction Meta-Armature: Confessor weight 0.5/total → 0.3/total. Faith weight drops in Crown aggregate.
# Strategic implication: Crown becomes more Order-dominant (less Faith-balanced).
```

If next year Confessor drops to S3: exits inner circle. Almud's faction loses its primary Faith-aligned voice. Crown's strategic flavor shifts notably toward unmixed Order. **Long-term political consequence of cumulative deadlock-loss.**

**Verification.** `[REL-INV-3]` ✓. `[REL-INV-5]` 5→4 also crosses 4↔3-threshold → milestone fires per N-DIAG-A. ✓

**Cross-reference SIM-B-G8 confirmed P1-critical:** the interpretation of `failed_da_proposals` materially shifts cumulative inner-circle composition. Self-reinforcing-inequality dynamic if liberal interpretation; stable-equilibrium if strict.

---

## §7 Scenario 7 — Passive NPC Memory replacement at 3-cap (PATCH 3.15)

**Goal.** Verify Memory replacement rules at the 3-Memory cap; trace merge/drop priority.

### 7.1 Setup A — merge path

```
Baker_Solmund (Passive NPC, 3-Memory cap):
  memories: [
    M-A: event_type="trade_deal_succeeded", affect=+1, salience=3, season=T-2, reference_count=1
    M-B: event_type="trade_deal_succeeded", affect=+1.5, salience=2, season=T-1, reference_count=1
    M-C: event_type="raid_threat", affect=-1, salience=4, season=T-2, reference_count=1
  ]

New event T+0: another trade_deal_succeeded → new Memory M-D(affect=+0.5, salience=3, season=T+0).
add_memory(Baker, M-D) — would exceed cap.
```

**Trace per PATCH 3.15:**

```
1. Check for similar-tag same-affect-direction existing Memory:
   M-A: tag=trade_deal_succeeded, affect=+1 (positive). M-D affect=+0.5 (positive). Same tag, same direction.
   M-B: tag=trade_deal_succeeded, affect=+1.5 (positive). Same tag, same direction.
   Both A and B match. Use most recent (B) or higher-salience (A)? **Spec doesn't fully specify.**

   Assume: most recent same-tag Memory selected (M-B).
   Merge into M-B:
     reference_count: 1 → 2
     salience: max(M-B.salience=2, M-D.salience=3) = 3 (new takes if higher).
     M-B.salience: 2 → 3
   M-D itself is NOT added (merged into M-B).
```

End state: `[M-A, M-B (updated to salience 3, ref_count 2), M-C]`. Cap unchanged.

### 7.2 Setup B — drop-lowest path

```
Baker_Solmund (current state):
  M-A (positive, salience 3, T-2)
  M-B (positive, salience 3, T-1)
  M-C (negative, salience 4, T-2)

New event T+0: M-D(event_type="harvest_failed", affect=-0.5, salience=2). Different tag from all existing.
```

**Trace per PATCH 3.15:**

```
1. Similar-tag check: none of A/B/C tag matches "harvest_failed". Merge path skipped.
2. Drop lowest salience: M-A and M-B both at salience 3, tied with M-D at salience 2. M-D is lowest → would M-D be dropped? Or do we drop existing-lowest to make room?
   Rule per PATCH 3.15: "Drop the lowest-salience Memory." Among existing list, lowest is A or B at 3.
   But M-D at salience 2 is lower than the existing minimum. **Edge case: if new Memory's salience is below existing minimum, do we drop the existing lowest or just refuse the new Memory?** Spec doesn't say.
   
   Reasonable interpretation: drop existing lowest only if new Memory's salience is at-least-as-high. Otherwise, drop new Memory (refuse to add).
```

**`[GAP: SIM-D-G5]` Memory-add edge case when new Memory salience < all existing.** PATCH 3.15 says "drop lowest-salience Memory" but doesn't specify whether the new Memory is itself eligible to be the dropped one. Surface: `[GAP: PATCH 3.15 — when new Memory.salience < min(existing.salience), behavior unspecified — surfaced by SIM-D scenario 7B; v1.2 spec target — recommend "if new.salience < min(existing.salience), refuse to add (or merge if same-tag); else drop existing-lowest"]`.

### 7.3 Setup C — tie-break by age (drop-older)

```
Baker_Solmund:
  M-A (positive, salience 3, T-3)  ← older
  M-B (positive, salience 3, T-1)  ← newer  
  M-C (negative, salience 4, T-2)

New M-D(different tag, salience 4, T+0). New min would be among A, B, C.
M-A and M-B are tied at salience 3; tie-break = drop older.
M-A dropped. M-D added.
```

End state: `[M-B, M-C, M-D]`. Verified.

### 7.4 Verification (Scenario 7)

- **`[REL-INV-4]` Memory replacement deterministic:** ✓ Same input → same outcome (modulo SIM-D-G5 edge case).
- **Merge mechanics preserve cumulative pattern:** Multiple "trade_deal_succeeded" events fold into one Memory with rising reference_count. Baker observes "another disappointment from Crown" or "another favor from Crown" pattern across many specific events. Realistic.
- **3-Memory cap forces hard prioritization.** Passive NPCs maintain only most-recent + most-salient impressions. Cumulative effects work via merge.
- **Knock-on into Direction C:** Baker's Memories feed `compute_settlement_signal()` per SIM-C Scenario 1. Memory replacement at 3-cap shapes which events propagate as Settlement Signals. **Inactive NPCs (3-cap) effectively act as "decay+merge" filters on settlement-political signal.**
- **`[GAP: SIM-D-G6]` Merge path tie-break (most-recent vs highest-salience for selecting which existing Memory to merge into).** Spec says "merge" but doesn't specify which existing Memory if multiple match. Recommend: most-recent same-tag Memory (newer event tends to be the "current" framing). Surface for v1.2.

---

## §8 Scenario 8 — Multi-NPC multi-Accounting relational dynamics

**Goal.** 4 inner-circle NPCs, 4 Accountings, with mixed Outreach pressures, Standing changes, and Knot dynamics. Surface emergent relational patterns.

### 8.1 Setup

```
Crown inner circle (start of Year 4 quarter 1):
  Almud (S7, Order), Marshal (S6, Order — slightly demoted from Year 2-3 mediocre performance),
  Confessor (S4, Faith — recovered with strict-failed_da interpretation),
  Reformer (S4, Autonomy — promoted from S3 in Year 1).

Player has Knots with: Almud (political ally), Spouse (S5 Crown peripheral, not inner circle).

Pending state: Reformer and Confessor both new-inner-circle entrants; Marshal demoted; Almud constant.
```

### 8.2 Year 4 (4 Accountings) — relational pressure traces

**Acct 13:** Marshal generates Concern about Reformer's Autonomy-driven proposals (per SIM-B Scenario 3 displacement dynamic). c-Marshal-1: salience 3 about Reformer. Per PATCH 3.10, Outreach for Player at P3 "Marshal asks for player's read on Reformer."

Player attends or skips. If skips: c decays. If attends: shapes Marshal's Opinion of Reformer through dialogue + Memory.

**Acct 14:** Reformer's project completes (Year 1 displacement-success follow-up). Procedure C generates Memories per PATCH 1.5 (single-writer). Almud, Marshal, Confessor each receive Memory of project legacy (positive for Reformer-supporters; negative for Reformer-obstructors). Direction A processes drift.

**Acct 15:** Almud's Knot with Player surfaces a Concern (Almud is concerned about Player's relationship with Reformer — politically charged). Per PATCH 3.6: P2 mandatory Outreach for Player. Player attends. Dialogue choices: ally with Almud, defend Reformer, deflect.

**Acct 16:** End of Year 4. Standing recalc:
- Almud: Δ ≈ 0 (steady leader). S7 → S7.
- Marshal: completed_projects=1, failed_projects=0, sda=2, fda=1 (strict interpretation), pcs=0. Δ = +0.5 + 0.5 - 0.25 = +0.75. S6 → S7. **Promotion back to S7.**
- Confessor: completed=1, failed=0, sda=2, fda=2 (lost competitions don't count under strict), pcs=0. Δ = +0.5 + 0.5 - 0.0 = +1.0. S4 → S5. **Promotion.**
- Reformer: completed=1, failed=0, sda=3, fda=1, pcs=1 (Belief revision from displacement consequences). Δ = +0.5 + 0.75 - 0.25 - 0.5 = +0.5. S4 → round(4.5) = 4 or 5 depending on rounding. With banker's rounding → 4 (no change).

**Cascade events:** Marshal +1 (no 3↔4 crossing). Confessor +1 (no 3↔4 crossing). No N-DIAG-A milestone scenes this year. Standard `standing_change` events fire.

**Faction Meta-Armature trajectory:** End of Year 4 vs End of Year 1:
- Y1: Almud (Order, S7×1.5), Marshal (Order, S6→0.7), Confessor (Faith, S5→0.5), Ambassador (Continuity, S4→0.3). Order-dominant.
- Y4: Almud (Order, S7×1.5), Marshal (Order, S7→1.0), Confessor (Faith, S5→0.5), Reformer (Autonomy, S4→0.3). 

  Order weight: 1.5+1.0 = 2.5/total. Total = 2.5+0.5+0.3 = 3.3. Order share = 0.76. Faith share = 0.15. Autonomy share = 0.09.
  Ambassador (S4 Continuity) is no longer in this composition — assume departed inner circle or replaced by Reformer (rough).
  
- **Compared to Y1: Order share rose; Continuity dropped (Ambassador out); Autonomy entered.**

Crown over 4 Years has shifted from a balanced Order/Continuity/Faith composition to a more strongly Order-dominant + minority Autonomy + Faith composition. **Cumulative institutional drift verified across multi-Year span.**

### 8.3 Verification (Scenario 8)

- **All invariants hold under multi-Accounting load.** ✓
- **SIM-B-G8 strict interpretation produces stable equilibrium**: Confessor recovers from his deadlocked Year 3 because lost-competitions don't count against Standing. Confessor's S4→S5 promotion validates the interpretation (vs liberal interpretation which would have left him at S4 or lower).
- **Knot Outreach (Almud's, Acct 15) interlocks with Direction B (institutional politics) — Player's response to Almud's concern about Reformer affects Player's strategic alignment within Crown.**
- **Cumulative drift over 4 Years observed:** Crown becomes more Order-dominant, gains Autonomy minority, loses Continuity. **Direction E composition target — would amplify across multi-faction multi-decade Campaign.**
- **Emergent relational property:** Player's choice to attend/skip Outreach scenes shapes which inner-circle NPCs feel "consulted" by Player. NPCs whose Outreach is consistently skipped develop slow negative drift toward Player; consulted NPCs develop positive drift. **Long-term, Player's relational choices reshape Player↔inner-circle Disposition matrix**, which affects Faction Meta-Armature when Player crosses S5 (joins inner circle).

---

## §9 Direction-D summary

### 9.1 Invariants — verified across 8 scenarios

| Invariant | Status | Notes |
|---|---|---|
| `[REL-INV-1]` Outreach priority correctness | ✓ | Verified scenarios 1, 2, 3 |
| `[REL-INV-2]` Knot opacity preserved | ✓ | Verified scenario 3 |
| `[REL-INV-3]` Standing change generates event | ✓ | Verified scenarios 4, 5, 6 |
| `[REL-INV-4]` Memory replacement deterministic | ✓ | Verified scenario 7 (with G5/G6 edge cases) |
| `[REL-INV-5]` Standing milestone scene on 3↔4 | ✓ | Verified scenario 5 (S5→S7 of Sc 4 did not trigger correctly per spec — N-DIAG-A label issue G4) |
| `[REL-INV-6]` Outreach tone reflects mood | ✓ | All Outreach traces show mood-tone alignment |

**All 6 relational invariants verified.**

### 9.2 Surfaced specification gaps (6 total)

| ID | Surface | Issue | Severity |
|---|---|---|---|
| SIM-D-G1 | Scenario 1 | Dissipation `implied_affect` default unspecified | P3 |
| SIM-D-G2 | Scenario 2 | P2-evasion event handling unspecified | P2 |
| SIM-D-G3 | Scenario 3 | PATCH 3.6 + 3.10 interaction for Knot Concerns about Player (clarification) | P3 |
| SIM-D-G4 | Scenario 4 | N-DIAG-A title vs body inconsistency ("Standing 5" but body specifies 3↔4) | P3 (typo) |
| SIM-D-G5 | Scenario 7B | PATCH 3.15 — new Memory salience < min(existing) edge case | P2 |
| SIM-D-G6 | Scenario 7A | PATCH 3.15 merge tie-break (most-recent vs highest-salience among same-tag) | P3 |

### 9.3 Emergent properties observed (5)

1. **Player's relational budget allocation shapes long-term Disposition matrix.** Skipping/attending Outreach scenes accumulates into multi-Year drift in Player↔inner-circle relations. Critical for Player at S5+ joining Faction Meta-Armature.
2. **Knot mandatory P2 enforces commitment.** Player cannot manage marriages/partnerships passively. Active engagement required — mechanically encodes intimate relationships as cognitive load.
3. **Standing recalc creates inner-circle composition flux.** S3→S4 entries and S5→S4 exits change faction strategic flavor over multi-Year. Renaissance institutional dynamism.
4. **3-cap Passive Memory acts as decay+merge filter on settlement-political signal.** Settlement Signals (SIM-C) are shaped by what survives at the Passive cap; merge produces "pattern recognition" of recurring affect-aligned events.
5. **Cumulative institutional drift over 4 Years observed.** Crown shifted from Order/Continuity/Faith balance to Order-dominant/Autonomy-minority. Direction E target — would amplify across multi-faction multi-decade Campaigns.

### 9.4 Cross-direction observations

- **SIM-A integration:** Outreach attendance generates Memories (resolution of Concern). Direction A consumes via Procedure D. Closed loop.
- **SIM-B integration:** Standing changes from PATCH 3.11 propagate to Faction Meta-Armature; Direction B `select_proposal()` weights shift. Multi-Year cumulative drift in faction alignment is the joint output of D (Standing) + B (proposal selection).
- **SIM-C integration:** 3-Memory-cap Passive replacement (PATCH 3.15) shapes what feeds `compute_settlement_signal()`. Direction D mechanics determine Direction C inputs.
- **SIM-B-G8 confirmation:** Scenario 6 reaffirmed `failed_da_proposals` definition is P1-critical. Liberal interpretation produces self-reinforcing inequality; strict produces stable equilibrium. Recommendation persists for v1.2.

### 9.5 Direction D — VERDICT

**PASS with 6 P2/P3 spec gaps.** Relational mechanics — Outreach priorities, Knot opacity, Standing recalc cascades, Memory replacement at cap — are sound under the patches. Six minor specification clarifications recommended for v1.2. Five emergent relational properties documented; cross-direction integration verified across all four directions traced.

---

**END OF SIM-D.**
