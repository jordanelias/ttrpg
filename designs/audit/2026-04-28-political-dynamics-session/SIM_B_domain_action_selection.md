<!-- [PROVISIONAL: 2026-04-29 — simulation Direction B] -->
<!-- STATUS: PROVISIONAL — granular trace of Domain Action selection mechanics under doc 12 v1.1 -->
<!-- POSITION: designs/audit/2026-04-28-political-dynamics-session/SIM_B_domain_action_selection.md -->
<!-- COMPANION: SIM_A_opinion_architecture.md (Direction A); 12_development_specification.md v1.1 -->

# Simulation B — Domain Action Selection (`select_proposal()` and Standing recalc interaction)

**Source spec:** `12_development_specification.md` v1.1 (commit `9dede391`).
**Primary patches under test:** PATCH 2.1 (`select_proposal()` + `DOMAIN_ARMATURE_ALIGNMENT`); PATCH 3.5 (Grieving Mood gate); PATCH 2.6 (uniform fallback for armature confidence in select); PATCH 3.11 (Standing recalc over Campaign Year); PATCH 3.13 (`generate_new_project()` two-tier).
**Method:** Eight granular scenarios, step-by-step state transitions through the DA Proposal Phase. Each scenario records initial state, executed steps, scoring math, final state, invariant checks, and gap-surfacing.
**Companion:** Builds on SIM-A invariants `[INV-1..4]` (Opinion architecture). Adds DA-specific invariants below.

---

## §0 Conventions and DA-Specific Invariants

### 0.1 Naming and notation

NPCs labeled by role: `Almud` (Crown leader), `Confessor` (Faith primary), `Marshal` (Order primary), `Scribe` (Reason primary), `Treasurer` (Equity primary), `Ambassador` (Continuity primary), `Reformer` (Autonomy primary), `Magistrate` (Precedent primary). All inside `Crown` faction unless noted; cross-faction scenarios specify factions explicitly.

State transitions use `npc.field: old → new` notation. Scoring uses `score = X.XX` with explicit arithmetic shown.

### 0.2 DA-specific invariants under test

- **`[DA-INV-1]` Single-winner per faction-domain-collision.** When ≥2 inner-circle proposers share a domain in same faction-Accounting, exactly one wins and others have `seasons_stalled += 1`.
- **`[DA-INV-2]` Score determinism.** `select_proposal()` is deterministic given fixed inputs. Same proposers + same meta-armature + same standings produce same winner.
- **`[DA-INV-3]` Standing-Δ bounds.** Per Campaign Year, `Δ_standing ∈ [-2, +2]`; `npc.standing` clamped to `[3, 7]`.
- **`[DA-INV-4]` Tie-break stability.** Three-level tie-break (alignment-score → Standing → seasons_stalled) produces stable orderings under repeated calls.
- **`[DA-INV-5]` Crisis exclusion.** When ≥40% of inner-circle is `{Distracted, Grieving}`, faction enters institutional autopilot (per §5.4) and DA Proposal Phase is bypassed for that faction. No proposers selected.
- **`[DA-INV-6]` Conviction-aligned displacement.** A `domain_aligned_with_conviction_primary` Project with `progress > 0` can claim a Priority 5-6 slot from the institutional priority tree, gated by `institutional_deference` check at Ob 1.
- **`[DA-INV-7]` Generated-project domain coherence.** `generate_new_project()` Tier-2 procedural domain selection probabilistically follows the NPC's `conviction_primary` weight in `DOMAIN_ARMATURE_ALIGNMENT`.

### 0.3 Reference: meta-armature scoring formula (PATCH 2.1)

```
score(p) = sum over c in CONVICTIONS of [
              meta_armature.conviction_weights[c] × DOMAIN_ARMATURE_ALIGNMENT[domain][c]
          ] + 0.1 × p.npc.standing
```

`conviction_weights[c]` is a 7-vector summing to 1.0. `DOMAIN_ARMATURE_ALIGNMENT[domain][c]` is a 7-vector of values in [0.0, 1.0]. Standing bonus ranges `[0.3, 0.7]` (Standing 3 → 7). Total score range: `[0.0 + 0.3, ~7.0 + 0.7]`; in practice scores cluster in `[0.7, 1.5]` because conviction_weights sums to 1 (so the alignment dot-product is essentially a weighted average of alignment values).

---

## §1 Scenario 1 — Single-faction inner-circle competition: 3 same-domain proposers

**Goal.** Trace `select_proposal()` with three Crown inner-circle NPCs proposing same-domain (military) projects in same Accounting. Verify deterministic single-winner selection.

### 1.1 Initial state (T+0 start, end of Procedure B)

```
Crown faction inner circle:
  Almud (Standing 7, leader): conviction_primary=Order, secondary=Continuity. mood=Steady.
    armature_confidence: 1.0
  Marshal (Standing 6): conviction_primary=Order, secondary=Continuity. mood=Steady. 
    scars_conviction=0.
  Confessor (Standing 5): conviction_primary=Faith, secondary=Order. mood=Steady. scars_conviction=1.
  Ambassador (Standing 4): conviction_primary=Continuity, secondary=Order. mood=Steady. scars_conviction=0.

Crown.faction.meta_armature.conviction_weights (computed each Accounting from inner_circle_aggregate + institutional_stability):
  Inner circle aggregate (Standing-weighted: S7×1.5(leader)=1.5, S6×0.7=0.7, S5×0.5=0.5, S4×0.3=0.3; total 3.0):
    Almud's primary Order contribution: 1.5/3.0 = 0.50 → 0.50 toward Order in his armature → ~0.40 weight on Order (Almud's armature has 80% Order weight by base)
    Marshal's: 0.7/3.0 = 0.233 → ~0.19 toward Order
    Confessor's: 0.5/3.0 = 0.167 → ~0.13 toward Faith (primary)
    Ambassador's: 0.3/3.0 = 0.10 → ~0.08 toward Continuity
  Inner circle aggregate ≈ {Order: 0.59, Faith: 0.13, Continuity: 0.08, others: residual ~0.20}
  
  institutional_stability: weight 0.4 × max(0, 1 - (sum scars_total / (4 × 2))) = 0.4 × (1 - 1/8) = 0.4 × 0.875 = 0.35
    value: Crown's historical dominant Conviction = Order (Order/Virtue-Ethics derived per §5.3)
  
  aggregate_weight = 1.0 - 0.35 = 0.65
  
  Final conviction_weights ≈ {
    Order: 0.65 × 0.59 + 0.35 × 1.0 = 0.384 + 0.35 = 0.734
    Faith: 0.65 × 0.13 = 0.085
    Continuity: 0.65 × 0.08 = 0.052
    others: 0.65 × 0.20 = 0.13 (distributed)
  }
  Normalized: {Order: 0.734, Faith: 0.085, Continuity: 0.052, Reason: 0.04, Equity: 0.04, Precedent: 0.04, Autonomy: 0.005}

Three flagged proposers (post-Mood-gating, all pass):
  P1: Marshal — Project "Reinforce Eastern Garrison" (military domain, progress=4, seasons_stalled=0)
  P2: Confessor — Project "Crusade against heretics in Hafenmark" (military domain — note: surprising for a Faith-primary, but he sees it as religious-military; project_domain="military", progress=2, seasons_stalled=1)
  P3: Ambassador — Project "Standing army for border defense" (military domain, progress=0 (new), seasons_stalled=0)

All three share domain "military". Faction Meta-Armature evaluates select_proposal.
```

### 1.2 Score computation

For each proposer, score = Σ(conviction_weight × DOMAIN_ARMATURE_ALIGNMENT[military]) + 0.1 × Standing.

`DOMAIN_ARMATURE_ALIGNMENT[military] = {Faith: 0.3, Order: 1.0, Reason: 0.6, Equity: 0.2, Precedent: 0.5, Autonomy: 0.4, Continuity: 0.7}`

Conviction-weighted alignment (same for all three because they share a domain — alignment depends on faction's meta-armature, not on proposer):
```
alignment_part = 
    0.085 × 0.3   (Faith)         = 0.0255
  + 0.734 × 1.0   (Order)         = 0.734
  + 0.04  × 0.6   (Reason)        = 0.024
  + 0.04  × 0.2   (Equity)        = 0.008
  + 0.04  × 0.5   (Precedent)     = 0.020
  + 0.005 × 0.4   (Autonomy)      = 0.002
  + 0.052 × 0.7   (Continuity)    = 0.0364
                                  ──────
                                  ≈ 0.850
```

All three proposers have alignment_part ≈ 0.850 (military is the dominant alignment for an Order-led Crown faction). Differentiation comes from Standing bonus + tie-breaks.

```
score(Marshal)    = 0.850 + 0.1 × 6 = 0.850 + 0.6 = 1.450
score(Confessor)  = 0.850 + 0.1 × 5 = 0.850 + 0.5 = 1.350
score(Ambassador) = 0.850 + 0.1 × 4 = 0.850 + 0.4 = 1.250
```

### 1.3 Selection

`max(proposals, key=lambda p: (scores[p], p.npc.standing, p.project.seasons_stalled))`:
- Marshal: (1.450, 6, 0)
- Confessor: (1.350, 5, 1)
- Ambassador: (1.250, 4, 0)

Marshal wins by score. No tie at first level → tie-breaks not consulted.

### 1.4 State updates

```
Marshal.project: seasons_stalled = 0 → 0 (proposed; advances next via Procedure C if domain_action succeeds)
Confessor.project: seasons_stalled = 1 → 2
Ambassador.project: seasons_stalled = 0 → 1

# Apply armature-induced Ob modifiers (existing spec):
For each inner-circle NPC in Crown:
  If NPC.armature interpretation aligns with Marshal's military proposal:
    proposal.ob_modifier -= 1
  elif NPC.armature interpretation contradicts:
    proposal.ob_modifier += 1

# Almud (Order primary): aligns. -1.
# Marshal (Order primary): self-aligns; doesn't count (or aligns trivially).  
# Confessor (Faith primary, Order secondary): mixed — secondary aligns slightly. Net: 0.
# Ambassador (Continuity primary, Order secondary): mixed — Continuity also aligns 0.7 with military. Net: -1.

# Final ob_modifier on Marshal's proposal: -2.
```

### 1.5 Verification (Scenario 1)

- **`[DA-INV-1]` single-winner:** Confirmed — Marshal selected; Confessor and Ambassador had `seasons_stalled` incremented. ✓
- **`[DA-INV-2]` determinism:** Calling `select_proposal([Marshal, Confessor, Ambassador])` again with same state returns Marshal. ✓
- **`[DA-INV-4]` tie-break stability:** Not exercised (no tie at first level). Trivially satisfied. ✓
- **Faction-Meta-Armature integration:** Score reflects Crown's Order-dominance. A military proposal is well-aligned (alignment = 0.85). Note: a theological proposal in same faction would score `alignment ≈ 0.085×1.0 + 0.734×0.4 + 0.052×0.6 + … = 0.085 + 0.294 + 0.031 + 0.012 + 0.029 + 0.001 + 0.020 ≈ 0.473`. So military beats theological by ~0.38 score even before Standing — institutional bias is real and significant.
- **Knock-on observed:** Confessor's "Crusade against heretics" project, despite being Faith-aligned in his individual armature, scores in Crown's *meta-armature* not in his individual armature. Crown weights military highly and Faith less highly — so Confessor's military-flavored Crusade is institutionally favored over a pure-theological project. **Emergent property:** Faith NPCs in Crown often pursue theological-coded military projects because that's what the faction will sponsor. Realistic Renaissance pattern (Crusades, religious wars).

---

## §2 Scenario 2 — Tie-break cascade

**Goal.** Construct exact alignment-score tie; verify Standing-then-seasons_stalled cascade.

### 2.1 Setup

Two proposers, same faction (Hafenmark, Precedent-led):

```
Hafenmark.faction.meta_armature.conviction_weights ≈
  {Precedent: 0.65, Order: 0.10, Continuity: 0.08, others: 0.17}
  (Hafenmark institutional_stability anchored to Precedent; Categorical-Imperative derived)

Magistrate (Standing 6): primary=Precedent. Project "Codify trade-tariff statute" (economic, progress=3, seasons_stalled=0)
Treasurer (Standing 6): primary=Equity. Project "Audit guild treasuries" (economic, progress=3, seasons_stalled=2)
```

### 2.2 Score computation

`DOMAIN_ARMATURE_ALIGNMENT[economic] = {Faith: 0.2, Order: 0.5, Reason: 0.7, Equity: 0.6, Precedent: 0.4, Autonomy: 0.8, Continuity: 0.4}`

Both proposers have same domain (economic) and same Hafenmark meta-armature. Same alignment_part for both:
```
alignment = 
    0.65 × 0.4 (Precedent)  = 0.260
  + 0.10 × 0.5 (Order)      = 0.050
  + 0.08 × 0.4 (Continuity) = 0.032
  + 0.17 × ~0.55 (others avg)= 0.094
                              ──────
                            ≈ 0.436
```

Both score: `0.436 + 0.1 × 6 = 1.036`.

### 2.3 Tie-break activation

`max(proposals, key=lambda p: (scores[p], p.npc.standing, p.project.seasons_stalled))`:
- Magistrate: `(1.036, 6, 0)`
- Treasurer: `(1.036, 6, 2)`

First level (alignment score): tie. Both 1.036.
Second level (Standing): tie. Both 6.
Third level (seasons_stalled): Treasurer=2, Magistrate=0. **Treasurer wins** (higher seasons_stalled).

### 2.4 Verification (Scenario 2)

- **`[DA-INV-4]` tie-break stability:** Confirmed. Same call returns Treasurer deterministically. ✓
- **Anti-stall design intent verified:** Treasurer's Project has been stalled 2 seasons; tie-break favors it to prevent perpetual stall. Without this tie-break (alignment-only or alignment-Standing), an Equity-leaning Project in a Precedent-dominant faction with equal Standing peer would never advance. **Solves a real problem the stress tests anticipated.**
- **Knock-on for Equity-leaning NPCs in Precedent factions:** Treasurer's Equity primary is intrinsically less-aligned with Hafenmark's institutional weight (0.6 × 0.17 ≈ 0.10 vs Magistrate's Precedent 0.4 × 0.65 = 0.26 in their respective alignment contributions). But because they share a *domain* (economic), and the alignment is computed per-domain not per-Conviction, they score equally. **The conviction_primary of the proposer doesn't enter `select_proposal()` directly** — only the faction's meta-armature does.

This is a subtle but important structural property: **`select_proposal()` rewards the *faction's* alignment with the *project's domain*, NOT the *proposer's Conviction*.** A Reformer (Autonomy primary) in Crown can win economic-domain proposals against a Marshal because economic aligns with Autonomy at 0.8 — but only if Crown's meta-armature has any Autonomy weight (it usually has very little). In practice, the proposer's individual Conviction shapes which Projects they *propose* (via `generate_new_project()`'s `sample_domain_weighted_by_conviction`), but the faction's meta-armature decides which proposal wins competition. **Emergent property: NPCs propose what they want; factions select what aligns institutionally.**

- **`[GAP: SIM-B-G1]` Tie at all three levels.** What if alignment-score, Standing, and seasons_stalled are all tied? Spec gives no fourth-level tie-break. Possibilities: NPC.id ascending (per SIM-A's stable-order rec), random, project.id, or alphabetic on goal text. Surface for v1.2: `[GAP: select_proposal() fourth-level tie-break unspecified — surfaced by SIM-B scenario 2; v1.2 spec target — recommend NPC.id ascending per SIM-A §4.1 / §15.1]`.

---

## §3 Scenario 3 — Personal priority insertion (Conviction-aligned displacement)

**Goal.** Trace the `domain_aligned_with_conviction_primary` displacement of a Priority 5-6 institutional duty, gated by `institutional_deference` check.

### 3.1 Setup

```
Crown faction:
  Almud (S7, Order primary, deference=2): leading institutional Priority 1-4.
  Reformer (S5, Autonomy primary, secondary=Reason, institutional_deference=0):
    active_project: "Establish guild-charter precedent" (economic, progress=3, seasons_stalled=0)
    Project domain "economic" — does it align with conviction_primary "Autonomy"?
    DOMAIN_ARMATURE_ALIGNMENT[economic][Autonomy] = 0.8 — high alignment.
    Per spec convention: alignment ≥ 0.7 → "domain_aligned_with_conviction_primary" = True.
  Crown.faction.priority_tree: Priority 5 = "Maintain trade routes"; Priority 6 = "Patron the academy."
    Both have_priority_5_or_6_capacity = True (slots available).

Reformer is flagged (Mood gating: Steady → proposal_modifier=0).
```

### 3.2 DA Proposal Phase — displacement check

```
For Reformer's proposal:
  project.domain_aligned_with_conviction_primary = True (economic + Autonomy: 0.8 ≥ 0.7).
  project.progress > 0 (3 > 0). ✓
  npc.faction.priority_tree.has_priority_5_or_6_capacity = True.
  → allow_displacement(Reformer, faction_priority_5_or_6_slot)
  
  # Displacement risk: institutional_deference check at Ob 1 (existing spec)
  Reformer.institutional_deference = 0; Ob 1 check:
    With deference=0, this is a poor stat. Spec doesn't fully define the dice system here, but
    institutional_deference 0 → fail Ob 1 dice check ~70% probability (assumed).
  
  Outcome: ~30% pass (proposal succeeds without faction-leader notice), ~70% fail (faction leader 
    may notice neglect of institutional Priority 5/6 → generates Concern/event for Almud).
```

Trace specific dice roll: assume fail (-> faction-leader-notices branch).

### 3.3 Failed deference check — Almud notices

```
Event generated: 
  event-display: {
    event_type: "displacement_neglect_observed",
    participants: [reformer, almud],
    visibility: {public: false, semi_public_observers: [almud, ...]},
    salience: 2,
  }

Almud's next-Accounting Procedure B Generation:
  npc_observes_event(Almud, event-display) → True (Almud in semi_public).
  derive_concern_tag → "reformer_neglecting_institutional_duties".
  Cooldown check: not in concern_history. Generate.
  Almud.concerns.append(Concern(salience=3, ttl=4, subject=reformer))

# Knock-on into next Accounting:
T+1 Procedure E: if Almud and Reformer interact:
  apply_drift on Almud.opinions[reformer]:
    new_memory generated by displacement event will arrive at D.
  Almud's opinion of Reformer drifts negative.
```

### 3.4 Verification (Scenario 3)

- **`[DA-INV-6]` Conviction-aligned displacement:** Confirmed engaged. ✓
- **Multi-Accounting feedback verified:** Reformer's displacement → Almud's Concern → Almud's Opinion-of-Reformer drift over next 1-2 Accountings. The political consequence of bypassing institutional priority is *delayed and indirect* — exactly the design intent of Renaissance-pace political simulation.
- **Knock-on into Standing recalc:** Failed displacement checks are *failed_da_proposals* (per PATCH 3.11)? **Ambiguous.** Spec doesn't clarify whether a successful displacement-with-failed-deference-check counts as `successful_da_proposal` (proposal won) or `failed_da_proposal` (deference check failed). The proposal succeeded mechanically; the *check* failed. **`[GAP: SIM-B-G2]` Failed-deference-check accounting in PATCH 3.11 Standing-recalc formula unclear. Surface for v1.2: should failed deference (Reformer's case) count as a failed proposal? Recommend NO — proposal succeeded, deference failure produces a separate observation event; `failed_da_proposals` should mean "proposal lost competition" or "Domain Action roll failed." Not "got institutional side-eye."**
- **Strategic property:** A high-Autonomy NPC with low institutional_deference will pursue Conviction-aligned displacement frequently. Each such displacement risks a deference failure → Almud-Concern → Opinion drift. Cumulative effect over Campaign Year: Reformer earns Almud's displeasure. If Standing is recalculated based on conviction Scars (PATCH 3.11: `-0.5 × public_conviction_scars_this_year`), and this dynamic causes Reformer to develop Conviction-engaging Scars (e.g., Almud's Loyalty Interview pressure → Belief revision under Path A), Reformer's Standing could drop. **Emergent narrative arc:** Autonomy-driven inner-circle members destabilize over multi-year Campaigns. Realistic.

---

## §4 Scenario 4 — Grieving Mood gate (PATCH 3.5)

**Goal.** Trace Spirit Ob 1 check for Grieving NPC; both pass and fail paths.

### 4.1 Setup A — pass path

```
Confessor (S5, Faith primary): Spirit pool = 5 (high). Mood = Grieving (set by death of patron 1 season ago, duration 4 seasons remaining).
  active_project: "Memorial cathedral consecration" (theological, progress=6).
```

### 4.2 DA Proposal Phase trace

```
For Confessor:
  npc.mood == Grieving → check Spirit Ob 1.
  spirit_check(ob=1) with Spirit pool 5: succeed ~95% (very easy for high-Spirit NPC).
  Assume pass.
  proposal_modifier = +1  # passes but +1 Ob.
  flagged_proposers.append((Confessor, "Memorial cathedral consecration", +1))

# Confessor proceeds to inner-circle competition (if applicable) with +1 ob_modifier.
# select_proposal() proceeds normally; Confessor's score is unaffected by mood (score formula doesn't include mood).
# But the +1 ob_modifier propagates to the Domain Action roll itself (next phase).
```

### 4.3 Setup B — fail path

```
Magistrate (S6, Precedent primary): Spirit pool = 2 (low). Mood = Grieving (long-standing — perhaps multi-season grief from family loss).
  active_project: "Reform inheritance code" (legal/precedent — domain mapping unclear, treat as economic/diplomatic; let's say diplomatic).
```

### 4.4 DA Proposal Phase trace

```
For Magistrate:
  npc.mood == Grieving → check Spirit Ob 1.
  spirit_check(ob=1) with Spirit pool 2: succeed ~50% (basic dice; Spirit pool = dice; Ob 1 needs ≥1 success).
  Assume fail.
  continue  # Magistrate cannot propose this Accounting.

# Magistrate.project.seasons_stalled remains unchanged (no proposal made — but spec is silent on whether
# a non-proposal counts as stall for the seasons_stalled counter).
```

### 4.5 Verification (Scenario 4)

- **`[DA-INV-2]` determinism:** Spirit check is probabilistic; not deterministic. **This is a real exception to the score-determinism invariant.** Spec correctly treats Mood-gated checks as randomized. Score-determinism applies only to selected proposals, not to which NPCs make it to the selection round.
- **Pass path operational:** +1 Ob carries to actual Domain Action roll, making the action itself harder for Grieving NPC. Mechanically appropriate.
- **`[GAP: SIM-B-G3]` Stall counter on non-proposal.** When a Grieving NPC fails the Spirit check and `continue`s, does `project.seasons_stalled` increment? Spec doesn't say. Two interpretations: (a) seasons_stalled tracks only progress-not-made (so non-proposal due to grief = stall), or (b) seasons_stalled tracks competitive losses (so non-proposal due to grief = no event, no stall). **Recommend (a) — increment** because the Project genuinely didn't progress; the NPC was simply unavailable. Project staleness is real regardless of cause. Surface: `[GAP: seasons_stalled increment on Grieving-suppressed non-proposal — surfaced by SIM-B scenario 4; v1.2 spec target — recommend always-increment on non-progression]`.
- **Long-grief multi-Accounting effect:** Magistrate fails Spirit check repeatedly across multi-season grief. Project rotates through stall accumulation → eventually `seasons_stalled >= 8` → `execute_failure(project, npc)` → `generate_replacement_project(npc)` per Procedure C. **Effect:** prolonged Grieving Mood causes Project failure cascade → potentially Standing impact via PATCH 3.11 (`-0.5 × failed_projects_this_year`). NPCs in long grief become quietly less effective; their faction Standing erodes. **Emergent narrative arc:** Grief cascading into political decline. Politically authentic.

---

## §5 Scenario 5 — Distracted Mood interactions (existing spec, post-PATCH-3.5)

**Goal.** Verify that PATCH 3.5's Grieving check doesn't break the existing Distracted handling. Trace high-deference and low-deference Distracted paths.

### 5.1 Setup

```
Three Distracted Crown NPCs in same Accounting:
  Marshal (Distracted, institutional_deference=2 high): high-deference
  Reformer (Distracted, institutional_deference=0): low-deference
  Treasurer (Distracted, institutional_deference=1): medium-deference

(All have active projects requiring DA.)
```

### 5.2 DA Proposal Phase trace per NPC

After PATCH 3.5 the gate sequence is:
```
if npc.mood == Grieving:
    [Spirit check]
elif npc.mood == Distracted and npc.personality.institutional_deference >= 1:
    continue  # high-deference Distracted suppress proposals
elif npc.mood == Distracted and npc.personality.institutional_deference < 1:
    proposal_modifier = +1
else:
    proposal_modifier = 0
```

```
Marshal (Distracted, deference 2 ≥ 1): continue. NOT flagged. seasons_stalled implications same as scenario 4 [GAP].
Reformer (Distracted, deference 0 < 1): proposal_modifier = +1. Flagged with +1 Ob.
Treasurer (Distracted, deference 1 ≥ 1): continue. NOT flagged.
```

### 5.3 Knock-on: faction crisis threshold

If Crown inner circle has 4 active NPCs (Almud, Marshal, Reformer, Treasurer) and 3 of 4 are Distracted (Marshal, Reformer, Treasurer), that's 75% Distracted. **Triggers faction crisis (`§5.4`):**
- 75% > 40% → Faction enters institutional autopilot.
- DA Proposal Phase is bypassed entirely for Crown.
- No new Project proposals accepted.
- Existing Priority 1-2 actions execute on autopilot from pre-existing patterns.

This means even Reformer (low-deference Distracted, who would otherwise propose at +1) does not propose. **`[DA-INV-5]` activated.**

### 5.4 Verification (Scenario 5)

- **PATCH 3.5 doesn't conflict with existing Distracted handling.** ✓ The `elif` chain correctly orders Grieving > Distracted-high-def > Distracted-low-def.
- **`[DA-INV-5]` crisis exclusion verified.** When 75% inner-circle is Distracted, no proposals are processed regardless of deference. Reformer's low-deference advantage is overridden by faction-level autopilot mode.
- **Strategic property:** Mass-Distracted faction state is a *political crisis indicator* visible to the player. From a player perspective, Crown stops issuing new initiatives — visible behavior change. The player can use Read or Surveil to observe inner-circle Mood states and infer the faction has entered autopilot. **Player feedback loop:** if the player has been pressuring multiple inner-circle NPCs (causing Distractedness through sustained Concerns), they can deliberately destabilize a faction's strategic capability. Lever for emergent gameplay.

---

## §6 Scenario 6 — `generate_new_project()` two-tier derivation (PATCH 3.13)

**Goal.** Trace both Tier 1 (authored queue) and Tier 2 (procedural) paths. Verify Conviction-weighted domain sampling produces character-coherent follow-ups.

### 6.1 Setup A — Tier 1 (authored queue)

```
Marshal (Order primary): just completed Project p-001 ("Reinforce Eastern Garrison" — military, progress 10).
  authored_project_queue: [
    Project(goal="Establish standing army", domain=military, ...),
    Project(goal="Train successor cohort", domain=military, ...),
  ]
```

### 6.2 Trace: Tier 1 hit

```
generate_new_project(Marshal):
  # Tier 1 — pre-authored project queue
  Marshal.authored_project_queue is non-empty (length=2).
  return Marshal.authored_project_queue.pop(0)
  → returns Project("Establish standing army")
  → Marshal.authored_project_queue now [Project("Train successor cohort")]
```

Marshal continues with deterministic authored Project p-002. Designer-intended multi-Project arc preserved.

### 6.3 Setup B — Tier 2 (procedural)

```
Scribe (Reason primary, secondary=Autonomy): just completed Project p-100 ("Translate Hafenmark codex").
  authored_project_queue: []  (empty — Scribe has no specifically-authored follow-up arc).
```

### 6.4 Trace: Tier 2 procedural

```
generate_new_project(Scribe):
  # Tier 1: queue empty. Skip.
  # Tier 2: 
  domain = sample_domain_weighted_by_conviction(Reason)
    weights = {d: DOMAIN_ARMATURE_ALIGNMENT[d][Reason] for d in DOMAINS}
    From the table:
      military:     0.6
      theological:  0.3
      scholarly:    1.0  ← highest
      intelligence: 0.8
      economic:     0.7
      diplomatic:   0.5
    weighted_select samples proportional to weights.
    Total weight = 0.6 + 0.3 + 1.0 + 0.8 + 0.7 + 0.5 = 3.9
    Probabilities:
      scholarly:    1.0/3.9 = 25.6%  ← most likely
      intelligence: 0.8/3.9 = 20.5%
      economic:     0.7/3.9 = 17.9%
      military:     0.6/3.9 = 15.4%
      diplomatic:   0.5/3.9 = 12.8%
      theological:  0.3/3.9 = 7.7%
  
  horizon = weighted_choice(["short", "medium", "long"], [0.4, 0.4, 0.2])
    short:  40%
    medium: 40%
    long:   20%
  
  visible_actions_pool = VISIBLE_ACTIONS_TEMPLATES["scholarly"]
    (from PATCH 3.14 / §10 authoring scope: ~10 entries per domain)
  
  project = Project(
    goal = generate_goal_from_template("scholarly", Scribe),
    progress = 0,
    horizon = "medium",  (sampled)
    project_domain = "scholarly",
    visible_actions = [random.choice(visible_actions_pool)],
    visible_actions_pool = visible_actions_pool,
    completion_effect = standard_effect_for("scholarly", Scribe),
    failure_effect = standard_effect_for_failure("scholarly", Scribe),
    domain_action_required = domain_action_required_for("scholarly"),
    seasons_stalled = 0,
  )
  return project
```

Scribe's new Project: scholarly-domain (highest probability for Reason primary), medium-horizon, with a visible_action sampled from scholarly templates ("transcribing manuscript" or similar).

### 6.5 Multi-NPC procedural distribution

If 7 NPCs with each Conviction primary all generate procedural Projects in same Accounting, what's the distribution?

| primary | most-likely domain (P) | second-most (P) | third (P) |
|---|---|---|---|
| Faith | theological (1.0) | precedent-aligned domain set (n/a — domains not Convictions) | — |
| Order | military (1.0) | intelligence (0.7) | diplomatic (0.6) |
| Reason | scholarly (1.0) | intelligence (0.8) | economic (0.7) |
| Equity | diplomatic (0.7) | economic (0.6) | scholarly (0.5) |
| Precedent | theological (0.7) | diplomatic (0.6) | scholarly (0.6) |
| Autonomy | economic (0.8) | scholarly (0.7) | intelligence (0.6) |
| Continuity | military (0.7) | diplomatic (0.6) | theological (0.6) |

Wait — let me check Faith. `DOMAIN_ARMATURE_ALIGNMENT[theological] = {Faith: 1.0, ...}` so for sampling by Conviction Faith, we look up each domain's Faith column:
- military[Faith]: 0.3
- theological[Faith]: 1.0
- scholarly[Faith]: 0.2
- intelligence[Faith]: 0.3
- economic[Faith]: 0.2
- diplomatic[Faith]: 0.5

Faith primary → most-likely theological (1.0/2.5 = 40%), then diplomatic (0.5/2.5 = 20%), then military and intelligence tied (12% each), etc.

**Aggregate property:** Procedurally-generated Projects in a 7-NPC setup follow Conviction-coherent distribution. A Faith-Order-Reason-leaning faction (Crown + Church alliance) would generate primarily theological + military + scholarly Projects — institutionally coherent. **Emergent property:** procedural generation amplifies Conviction-faction patterns, producing Renaissance-faction-coherent strategic flavors over multi-Accounting campaigns.

### 6.6 Verification (Scenario 6)

- **`[DA-INV-7]` Conviction-coherent procedural domain selection:** Verified. Reason primary samples scholarly most often (25.6%), reflecting alignment table. ✓
- **Tier 1 deterministic:** Authored queue produces same-result on re-call. ✓
- **`[GAP: SIM-B-G4]` `generate_goal_from_template()` not specified in v1.1.** Patch 3.13 references it but doesn't define template format. Likely needs a content-authoring spec like `params/project_goal_templates.md`. Surface: `[GAP: project goal-template format and content-authoring spec — surfaced by SIM-B scenario 6; v1.2 / params authoring target — recommend "${verb} ${object} ${qualifier}" with per-domain pools]`.
- **`[GAP: SIM-B-G5]` `standard_effect_for()` and `domain_action_required_for()` not specified.** Both are referenced as helpers but no definition. Likely per-domain authored constants. Surface: `[GAP: domain effect/action helper specs — surfaced by SIM-B scenario 6; v1.2 / content authoring target]`.
- **Knock-on for visible_actions consistency:** Each procedural Project gets visible_actions_pool = template list (per PATCH 3.14). Player observing Scribe's Project across multiple Accountings sees varying scholarly-themed actions ("transcribing manuscript" → "consulting library" → "writing commentary"). **Pool variation produces realistic surface diversity without bloating authored content.** This is exactly the design intent of PATCH 3.14.

---

## §7 Scenario 7 — Standing recalc over Campaign Year boundary (PATCH 3.11)

**Goal.** Trace 4 Accountings (= 1 Campaign Year) for a single NPC, then recalculate Standing. Then trace another year, verifying cumulative trajectory.

### 7.1 Setup — Year 1 begin

```
Marshal (S6, Order primary): start of Campaign Year 1.
  Year-1 events tracker (initialized): {
    completed_projects_this_year: 0,
    failed_projects_this_year: 0,
    successful_da_proposals_this_year: 0,
    failed_da_proposals_this_year: 0,
    public_conviction_scars_this_year: 0,
  }
```

### 7.2 Year 1 traces (Accountings 1-4)

```
Accounting 1: Marshal proposes "Reinforce Garrison" (military). Wins inner-circle competition. 
              Domain Action succeeds. progress 4→5. → successful_da_proposals++. counter=1.

Accounting 2: Marshal's "Reinforce Garrison" advances. progress 5→7. No DA needed this season.
              No proposal made.

Accounting 3: Marshal proposes again to reach progress 7→8. Wins (no competitor). DA fails (bad roll).
              progress unchanged. seasons_stalled=1. → failed_da_proposals++. counter=1.

Accounting 4: Marshal proposes to reach progress 8→9. Wins. DA succeeds. progress 8→10. PROJECT COMPLETES.
              → completed_projects_this_year++. counter=1.
              → successful_da_proposals++. counter=2.
              # Generate replacement project (PATCH 3.13 Tier 1 if queue exists, else Tier 2)
              # Marshal had authored_queue → "Establish standing army" begins as new active_project.
```

### 7.3 End of Year 1 — Standing recalc

```
Δ_standing = (
    +0.5 × completed_projects_this_year (1)        = +0.5
    -0.5 × failed_projects_this_year (0)            = +0.0
    +0.25 × successful_da_proposals_this_year (2; max +1.0) = +0.5
    -0.25 × failed_da_proposals_this_year (1; max -1.0) = -0.25
    -0.5 × public_conviction_scars_this_year (0)   = +0.0
)
Δ_standing = +0.75

Δ_standing = clamp(+0.75, -2, +2) = +0.75
Marshal.standing = round(clamp(6 + 0.75, 3, 7)) = round(6.75) = 7

Standing change event generated:
  event_type: "standing_change", participants: [marshal], delta: +1
  visibility: public (Standing changes are observable by all inner-circle).
  affected_npcs: all Crown inner circle.
  
# Inner-circle NPCs receive Memories about Marshal's elevation (next-Accounting Procedure E knowledge sharing
# or directly via event).
```

Marshal at S7. Now ties Almud at top of inner circle.

### 7.4 Year 2 — additional dynamics

```
Almud (still S7), Marshal (now S7): both at top.

Faction Meta-Armature recalc (next Accounting):
  Standing weights: leader (Almud) × 1.5 = 1.5, Marshal at S7 × 1.0 = 1.0.
  But: leader is defined as singular (the faction's official head). Almud is leader; 
       Marshal is just S7 inner-circle peer.
  
  Confessor (S5) × 0.5 = 0.5
  Ambassador (S4) × 0.3 = 0.3
  
  Total weight: 1.5 + 1.0 + 0.5 + 0.3 = 3.3
  
  Compare to pre-elevation: 1.5 + 0.7 + 0.5 + 0.3 = 3.0
  Marshal's contribution: was 0.7/3.0 = 0.233; now 1.0/3.3 = 0.303. **Marshal's institutional weight grew ~30%.**
```

`select_proposal()` called in Year 2 with Crown's updated meta-armature reflects Marshal's increased influence. Crown's Order-weight rises slightly (since Marshal is also Order primary), reinforcing military-domain bias.

### 7.5 Year 2 — Marshal under-performs

```
Accounting 5-8 (Year 2):
  Acct 5: Marshal proposes for new project ("Standing army"). Wins. DA succeeds. SDA++. counter=1.
  Acct 6: progress unchanged. seasons_stalled=1. No proposal made (no DA needed).
  Acct 7: Marshal proposes; wins; DA fails. seasons_stalled=2. FDA++. counter=1.
  Acct 8: Marshal proposes; wins; DA fails. seasons_stalled=3. FDA++. counter=2.
  # Project not yet failed (threshold seasons_stalled >= 8); but trending poorly.
```

End of Year 2 Standing recalc:
```
Δ_standing = (
    +0.5 × 0 (no completion)                = +0.0
    -0.5 × 0 (no failure yet)                = +0.0
    +0.25 × 1 (1 success)                    = +0.25
    -0.25 × 2 (2 failures)                   = -0.50
    -0.5 × 0 (no public Conviction scars)    = +0.0
)
Δ_standing = -0.25

Marshal.standing = round(clamp(7 + (-0.25), 3, 7)) = round(6.75) = 7
```

Marshal stays at S7 due to rounding (6.75 → 7). Year 3 if same trajectory: 6.75 - 0.25 = 6.5 → 7 (rounds up at .5 — ambiguous; round-half-to-even gives 6, round-half-up gives 7). 

### 7.6 Verification (Scenario 7)

- **`[DA-INV-3]` Standing-Δ bounds:** ✓ +0.75 within [-2, +2]; result 7 within [3, 7].
- **Annual cadence reduces whippiness:** Marshal's Year-2 mediocre performance produces only -0.25 delta; rounded result is unchanged at 7. Without rounding, it would slowly trend down. **Design intent verified: changes accumulate over multiple years rather than triggering instant Standing volatility.**
- **`[GAP: SIM-B-G6]` Round-half handling.** Spec says `round(...)`. Python `round()` uses banker's rounding (half-to-even). Some other languages use half-up. For Marshal's 6.75 case, result is unambiguously 7. For 6.5 → could be 6 or 7. **Surface: `[GAP: round() semantics in Standing recalc — surfaced by SIM-B scenario 7; v1.2 spec target — recommend explicit rounding rule, e.g., "round half-to-even" or "floor at decimal .5"]`.**
- **Inner-circle composition shift verified:** Marshal's S6→S7 shifts Crown's meta-armature toward Order-dominance. **Knock-on:** Year-2 `select_proposal()` calls now favor military-domain Projects more than Year-1. A Reformer-Autonomy proposal in Year-2 has *less* chance of winning than in Year-1 because the meta-armature has drifted further toward Order. **Cumulative institutional drift is real and emerges from Standing recalc → meta-armature recomputation → proposal selection feedback.**
- **Unintended consequence:** Successful project completions reinforce institutional bias. A faction whose inner circle accumulates Order-aligned successes becomes *more* Order-biased, making it harder for non-Order NPCs to get proposals selected. Long-running campaigns may see institutional ossification — a faction becomes increasingly homogeneous in its strategic flavor. **Emergent narrative property:** Renaissance institutional inertia. May be a feature; may be a P3 design call. Worth flagging.
- **`[GAP: SIM-B-G7]` Counter-tracking infrastructure.** PATCH 3.11 implies per-NPC per-Year counters for completed/failed projects, successful/failed DA proposals, public conviction scars. Spec doesn't define where these counters live or when they reset. Recommend: `npc.year_counters = {...}`, reset at end of recalc. Surface: `[GAP: PATCH 3.11 counter-state location and reset cadence — surfaced by SIM-B scenario 7; v1.2 spec target]`.

---

## §8 Scenario 8 — Multi-NPC, Multi-Accounting trace (composition stress test)

**Goal.** 4 NPCs, 3 Accountings, all DA-related dynamics interacting. Surface emergent patterns.

### 8.1 Setup

```
Crown faction inner circle (4 NPCs at start of Year 3):
  Almud (S7, Order primary, secondary=Continuity, leader): mood=Steady. 
    active_project: "Coronation reaffirmation" (theological/diplomatic, progress=2).
  Marshal (S7, Order primary, after Year 1+2 trajectory): mood=Distracted (low priority). 
    active_project: "Standing army" (military, progress=5, seasons_stalled=3).
  Confessor (S5, Faith primary, secondary=Order): mood=Vindicated (recent Concern resolved well). 
    active_project: "Visit Hafenmark seminary" (theological/diplomatic, progress=4, seasons_stalled=0).
  Ambassador (S4, Continuity primary, secondary=Order): mood=Steady. 
    active_project: "Renew Solmund-Hafenmark trade treaty" (diplomatic, progress=6, seasons_stalled=0).

Crown.faction.meta_armature: ~ {Order: 0.70, Faith: 0.10, Continuity: 0.07, others: 0.13}
  (Marshal's promotion shifted Order weight up; institutional_stability still 0.35.)
```

### 8.2 Accounting 9 (Year 3, season 1)

**Procedure B:** several events; Concerns generated; resolutions apply per Direction-A simulation. Not detailed here.

**DA Proposal Phase:**
- Almud: mood Steady → flagged. Project domain=theological. proposal_modifier=0.
- Marshal: mood Distracted, deference (assumed 1) >= 1 → suppressed (continue).
- Confessor: mood Vindicated → not Grieving, not Distracted → proposal_modifier=0. Flagged.
- Ambassador: mood Steady → flagged. Project=diplomatic. proposal_modifier=0.

Three proposers: Almud (theological), Confessor (theological/diplomatic — let's settle on theological for clarity), Ambassador (diplomatic). Two domains: theological (2 proposers) and diplomatic (1).

**Inner-circle competition:**
- theological collision: Almud vs Confessor.
- diplomatic: Ambassador alone, no competition.

Compute scores for theological collision:

`DOMAIN_ARMATURE_ALIGNMENT[theological] = {Faith: 1.0, Order: 0.4, Reason: 0.3, Equity: 0.3, Precedent: 0.7, Autonomy: 0.2, Continuity: 0.6}`

```
alignment_part_theological = 
    0.10 × 1.0   (Faith)        = 0.10
  + 0.70 × 0.4   (Order)        = 0.28
  + 0.04 × 0.3   (Reason est)   = 0.012
  + 0.03 × 0.3   (Equity est)   = 0.009
  + 0.03 × 0.7   (Precedent est)= 0.021
  + 0.005 × 0.2  (Autonomy est) = 0.001
  + 0.07 × 0.6   (Continuity)   = 0.042
                                  ──────
                                ≈ 0.465
```

```
score(Almud) = 0.465 + 0.1 × 7 = 1.165
score(Confessor) = 0.465 + 0.1 × 5 = 0.965
```

Almud wins (1.165 > 0.965). Confessor.project.seasons_stalled: 0 → 1.

Diplomatic: Ambassador alone — no competition; auto-selected. 

Selected proposers this Accounting: [Almud, Ambassador]. (Marshal suppressed; Confessor lost competition.)

**Apply armature-induced Ob modifiers:**
For Almud's theological proposal:
- Almud (Order primary, secondary Continuity): Order aligns with theological at 0.4 (mid). Not strong. Treat as no modifier.
- Marshal (Order primary): aligns 0.4. Mid. No modifier.
- Confessor (Faith primary): aligns 1.0. Strong align. -1.
- Ambassador (Continuity primary): aligns 0.6. Mild align. No modifier.
- Final ob_modifier on Almud: -1 (from Confessor's strong alignment as supporter).

For Ambassador's diplomatic proposal:
- Almud: diplomatic[Order]=0.6. Mild. No mod.
- Marshal: same. No mod.
- Confessor: diplomatic[Faith]=0.5. Mid. No mod.
- Ambassador: self.
- Final ob_modifier: 0.

**Procedure C executes (advances projects of those whose DA proposals succeeded). Skipping detail.**

### 8.3 Accounting 10 (Year 3, season 2)

State changes since Accounting 9:
- Marshal's project still stalled (seasons_stalled=4).
- Confessor's "Visit Hafenmark seminary" stalled once (seasons_stalled=1).
- Almud's Coronation advanced (progress 2 → 3).
- Ambassador's treaty advanced (progress 6 → 7).

Mood changes from event-resolution between Accountings (assume):
- Confessor: Vindicated→Steady (duration expired).
- Ambassador: Steady (unchanged).
- Marshal: Distracted persists (no triggering event to resolve).

DA Proposal Phase:
- Almud: flagged. theological.
- Marshal: still Distracted high-deference: continue.
- Confessor: Steady, flagged. theological. (still proposing same project.)
- Ambassador: flagged. diplomatic.

Theological collision again: Almud vs Confessor.
Same scores (state didn't change relevant inputs). Almud wins again.
Confessor seasons_stalled: 1 → 2.

Pattern emerges: **Confessor's Project chronically loses to Almud's theological proposals.** Confessor's project will continue stalling until either (a) Almud's project completes and frees the slot for unopposed Confessor wins, or (b) Confessor's seasons_stalled accumulates enough that the tie-break (which orders by alignment-score → Standing → seasons_stalled) lifts Confessor above Almud at some threshold. But Almud's score (1.165) is fixed > Confessor's (0.965); no tie-break triggers. **Confessor's project will never win** unless one of:
- Almud's project completes (frees the theological slot).
- Almud's Standing drops (-2 to S5; Almud's score becomes 0.465 + 0.5 = 0.965 = Confessor's tie; then seasons_stalled tie-break favors Confessor — by then 4+ seasons stalled).
- Confessor's score increases (Standing rise from 5 to 7+ — would need Standing recalc benefit over a year).
- Faction crisis pulls everyone into autopilot.

### 8.4 Accounting 11 (Year 3, season 3)

Almud's Coronation advances (progress 3 → 4 if DA succeeds; assume succeeds). Marshal's project hits seasons_stalled=5. Approaching the seasons_stalled>=8 failure threshold.

Confessor's project stalled 3 seasons. Frustration would accumulate (in real political logic). Spec doesn't have a "Project frustration" mechanic, but...

**Knock-on observation:** PATCH 3.13 generates new projects when Project completes via execute_completion_effect. But what about chronic stall? Procedure C executes failure:
```
if project.seasons_stalled >= 8:
    execute_failure(project, npc)
    generate_replacement_project(npc)
```

Confessor's project hits stall 8 around Accounting 16-17 (5 more seasons). That's 1.25 Years away. Then Confessor gets a procedurally-generated new Project (Tier 2 — Faith primary). Most likely domain: theological (1.0 weight). **Confessor will likely propose another theological project, again colliding with Almud.** Loop.

This is potentially a **structural deadlock**. The only escape: Almud's project completes first (frees slot) OR Confessor's Standing changes via PATCH 3.11.

Confessor's PATCH 3.11 counters at end of Year 3:
- completed_projects: 0 (project deadlocked, didn't fail or complete).
- failed_projects: 0 (or 1 if it hits stall-8 within year — probably won't yet).
- successful_da_proposals: 0 (Confessor never won proposal).
- failed_da_proposals: count of times Confessor proposed and lost — depends on whether "lost competition" counts as `failed_da_proposal`. **GAP again.**
- public_conviction_scars: depends on event resolution.

```
Δ_standing = +0 + 0 + 0 - 0.25 × failed_proposals - 0 = depends.
If Confessor proposed 4 times (every Accounting) and lost each: -0.25 × 4 = -1.0 (capped at -1.0 per year).
Confessor.standing = round(5 + (-1.0)) = round(4.0) = 4.
```

**Standing 4!** Confessor still in inner circle (≥3) but lower. This *worsens* the deadlock — Confessor's score drops to 0.465 + 0.4 = 0.865, now further below Almud's 1.165.

### 8.5 Verification (Scenario 8) — emergent properties

- **Structural deadlock identified.** Two same-domain proposers in same faction, where one is permanently lower-Standing-and-meta-aligned, can be locked out indefinitely. Standing recalc *worsens* the deadlock if "failed proposals" includes "lost competitions."
- **`[GAP: SIM-B-G8]` `failed_da_proposals` definition.** This is a critical-priority spec gap because it materially affects Standing trajectory. Two interpretations:
  - **Liberal:** "Lost inner-circle competition" counts as a failed proposal. Worsens deadlocks.
  - **Strict:** Only "Domain Action roll failed" counts. Lost competitions don't count.
  
  **Recommend Strict** for v1.2: PATCH 3.11 should distinguish "proposed but lost competition" (no Standing impact) from "proposed, won, DA roll failed" (negative Standing impact). Otherwise the system creates self-reinforcing inequality where lower-Standing NPCs lose competitions, which lowers their Standing, which causes them to lose more competitions. **Surface: `[GAP-CRITICAL: failed_da_proposals definition — surfaced by SIM-B scenario 8; v1.2 spec target — recommend "Domain Action roll failed" only, NOT "lost competition"]`.**
- **`[GAP: SIM-B-G9]` Mood-suppressed proposals (continue case from PATCH 3.5 / Distracted high-def) — these don't fire `proposal` at all. Should they be tracked for Standing recalc? Recommend NO — no proposal made = no event to count. Surface: `[GAP: Standing-recalc accounting for Mood-suppressed proposals — surfaced by SIM-B scenarios 4-5-8; recommend non-proposal does not increment failed counter]`.**
- **Tie-break-via-stall as escape valve:** The `seasons_stalled` tie-break (PATCH 2.1 spec, Tie-breaks line) is the *intended escape* from same-domain-collision deadlocks. But it only triggers when alignment-scores are equal. In this scenario, Almud's S7 produces a +0.2 score advantage that prevents tie-engagement. **The tie-break works for equal-Standing collisions but fails for unequal-Standing collisions.** This is a structural limit of the patch.
- **Recommended P2 follow-up patch (suggested for v1.2):** Add a "stall escalator" to score formula. E.g., `score(p) = alignment + 0.1 × standing + 0.05 × p.project.seasons_stalled`. This would slowly tilt long-stalled projects toward winning. With seasons_stalled=4, Confessor's score becomes 0.465 + 0.5 + 0.20 = 1.165 — exactly tied with Almud. Tie-break by Standing favors Almud, but by seasons_stalled would favor Confessor (4 vs 0). At seasons_stalled=8 (right before failure), Confessor would clearly win (score 0.465 + 0.5 + 0.40 = 1.365 vs Almud's 1.165). **Stall escalator would prevent infinite-deadlock without disrupting normal competition.** Surface: `[RECOMMENDATION: stall-escalator term in select_proposal score formula — surfaced by SIM-B scenario 8; v1.2 design call]`.
- **Faction-leader behavior under structural deadlock:** Almud (the leader) is winning all theological collisions against Confessor. Realistic outcome: Confessor's Faith-primary inner-circle weight is *under-deployed* because his proposals never pass institutional review. Long-term, Confessor may either: (a) abandon theological projects in favor of unique-domain projects (e.g., a personal_legacy project that doesn't compete), (b) develop Concern about Almud's gatekeeping (potential negative Opinion drift toward Almud), (c) eventually exit inner circle if Standing drops to 2 (per PATCH 3.11). All three are politically authentic outcomes; design-coherent.

---

## §9 Direction-B summary

### 9.1 Invariants — verified across 8 scenarios

| Invariant | Status | Notes |
|---|---|---|
| `[DA-INV-1]` single-winner per collision | ✓ | Verified scenarios 1, 2, 8 |
| `[DA-INV-2]` score determinism | ✓ | Probabilistic Spirit checks (Grieving) are an explicit exception |
| `[DA-INV-3]` Standing-Δ bounds | ✓ | Verified scenario 7 |
| `[DA-INV-4]` tie-break stability | ✓ | Verified scenario 2 |
| `[DA-INV-5]` crisis exclusion | ✓ | Verified scenario 5 |
| `[DA-INV-6]` Conviction-aligned displacement | ✓ | Verified scenario 3 |
| `[DA-INV-7]` Conviction-coherent procedural domain | ✓ | Verified scenario 6 |

**All 7 DA-specific invariants hold under traced load.**

### 9.2 Surfaced specification gaps (9 total)

| ID | Surface | Issue | Severity |
|---|---|---|---|
| SIM-B-G1 | Scenario 2 | Fourth-level tie-break in `select_proposal()` unspecified | P2 |
| SIM-B-G2 | Scenario 3 | Failed-deference accounting in PATCH 3.11 unclear | P2 |
| SIM-B-G3 | Scenario 4 | `seasons_stalled` increment on non-proposal unspecified | P2 |
| SIM-B-G4 | Scenario 6 | `generate_goal_from_template()` unspecified | P3 (authoring) |
| SIM-B-G5 | Scenario 6 | `standard_effect_for()` and `domain_action_required_for()` unspecified | P3 (authoring) |
| SIM-B-G6 | Scenario 7 | `round()` semantics in Standing recalc unspecified | P3 |
| SIM-B-G7 | Scenario 7 | PATCH 3.11 counter state location and reset cadence unspecified | P2 |
| **SIM-B-G8** | Scenario 8 | **`failed_da_proposals` definition unclear — affects Standing trajectory materially** | **P1** |
| SIM-B-G9 | Scenarios 4, 5, 8 | Standing-recalc accounting for Mood-suppressed proposals | P2 |

**SIM-B-G8 is critical.** The interpretation of "failed_da_proposals" determines whether the system has a self-reinforcing-inequality dynamic (deadlocked low-Standing NPCs become more deadlocked) or a stable equilibrium. Recommend "DA roll failed" only for v1.2.

### 9.3 Emergent properties observed (5)

1. **Faction selects proposals by domain alignment, not proposer Conviction.** NPCs propose what their Conviction wants; factions filter for institutional fit. Realistic Renaissance dynamic.
2. **Conviction-aligned displacement creates delayed political consequences** through Almud's Concern → Opinion drift → multi-Accounting feedback. Renaissance-pace political authenticity.
3. **Long-grief Mood produces Project failure cascade** → Standing erosion → quiet political decline. Authentic.
4. **Faction crisis state (≥40% inner-circle Distracted/Grieving) is a player-observable strategic vulnerability.** Lever for emergent gameplay.
5. **Cumulative institutional drift:** Successful project completions strengthen inner-circle weight of successful NPCs, biasing meta-armature further toward their alignment. Long campaigns may see institutional ossification. Possible feature; possibly P3 design call.

### 9.4 Recommended additional patch for v1.2

**Stall-escalator in `select_proposal()`:** Add `+0.05 × p.project.seasons_stalled` to score formula. Prevents infinite-deadlock for unequal-Standing same-domain collisions. Allows long-stalled projects to escalate toward winning over multi-Accounting timelines without disrupting normal competition. Surfaced by Scenario 8's structural deadlock analysis.

### 9.5 Cross-direction observations

- **Compounds with SIM-A findings:** Almud's failed-displacement event (Scenario 3) generates Memory in Almud's view → consumed by Procedure D (per SIM-A scenarios 1-3) → drift in Almud's Opinion of Reformer. Direction A and Direction B mechanics interlock via the Memory-bus.
- **Knock-on into Direction D (relational dynamics):** Standing changes (PATCH 3.11) generate `standing_change` events; inner-circle NPCs receive Memories about rising/falling colleagues; Procedure D drifts opinions. Standing mobility produces relational reorganization. Direction D should trace this in detail.
- **Knock-on into Direction E (composition):** Multi-faction dynamics across multiple Campaign Years would surface long-term institutional ossification (Scenario 7 + Scenario 8 emergent properties amplified). Worth ≥1 Direction-E scenario.

### 9.6 Direction B — VERDICT

**PASS with 1 critical gap (SIM-B-G8) and 8 P2/P3 gaps.** Domain Action selection mechanics are sound; `select_proposal()` produces deterministic, coherent winners; Standing recalc operates within bounds; procedural project generation produces Conviction-coherent follow-ups. **One critical clarification required for v1.2:** `failed_da_proposals` definition. One recommended additional v1.2 patch: stall-escalator in score formula. Five emergent properties documented.

---

**END OF SIM-B.**
