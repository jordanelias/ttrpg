<!-- [PROVISIONAL: 2026-04-29 — v1.2 specification revisions] -->
<!-- STATUS: PROVISIONAL — patch directives for producing doc 12 v1.2 from v1.1 -->
<!-- POSITION: designs/audit/2026-04-28-political-dynamics-session/21_v1_2_specification_revisions.md -->
<!-- COMPANION: 12_development_specification.md v1.1; 19_v1_1_validation_report.md -->

# v1.2 Specification Revisions

**Status:** PROVISIONAL — patch list for producing v1.2 from v1.1.
**Source:** Resolves 39 specification gaps surfaced by SIM-A through SIM-H + narrative pass; adds ED-760 stall-escalator.
**Predecessor:** `12_development_specification.md` v1.1 (commit `9dede391`).
**Companion validation:** `19_v1_1_validation_report.md`.
**Application target:** `12_development_specification.md` v1.2 (replaces v1.1 in same path).

---

## §0 READING GUIDE

This document specifies the spec-edits that resolve all 39 surfaced gaps. Patches grouped:
- **§1** — Three P1-CRITICAL resolutions (GAP-1, GAP-2, GAP-3). Must be applied for canonical promotion.
- **§2** — ED-760 stall-escalator (recommended additional patch).
- **§3** — 19 P2 resolutions (implementation determinism).
- **§4** — 16 P3 cleanups (doc / typo / authoring).
- **§5** — Application checklist for v1.2 production.

Patch convention as in doc 17:
```
PATCH N — <doc 12 section>
LOCATE: <unambiguous text marker in current doc 12 v1.1>
REPLACE/INSERT/ADD/UPDATE: <directive>
```

---

## §1 P1-CRITICAL RESOLUTIONS

### 1.1 GAP-1 (SIM-B-G8) · `failed_da_proposals` definition

**Issue.** §8.1 PATCH 3.11 Standing recalc formula uses `failed_da_proposals_this_year` but doesn't define what counts. "Lost competition" interpretation produces self-reinforcing inequality.

**Resolution.** Strict definition: only "Domain Action roll failed" counts. Lost competitions increment `seasons_stalled` (existing) but not `failed_da_proposals`.

**Patch.**

```
PATCH v1.2-1 — §8.1 NPC Standing Recalculation

LOCATE: "+0.25 × successful_da_proposals_this_year (max +1.0/year)
    -0.25 × failed_da_proposals_this_year (max -1.0/year)"

REPLACE with:
    +0.25 × successful_da_proposals_this_year (max +1.0/year)
        # successful = won inner-circle competition AND DA roll succeeded
    -0.25 × failed_da_proposals_this_year (max -1.0/year)
        # failed = won inner-circle competition AND DA roll FAILED
        # (lost competitions do NOT count — they only increment seasons_stalled)

ADD note immediately after formula:
    **Counter scope (clarification per v1.2):** Mood-suppressed proposals (Distracted high-deference 
    continue; Grieving Spirit-check fail) do NOT increment any counter. Lost inner-circle 
    competitions do NOT count as failed_da_proposals — they increment seasons_stalled only. 
    Failed-deference checks during Conviction-aligned displacement do NOT count as failed_da_proposals 
    — they produce a separate `displacement_neglect_observed` event (see §6.2 PATCH 3.5).
```

**Rationale.** Strict interpretation aligns with design intent — Standing-recalc rewards execution, not competition outcomes. Validated at scale by SIM-E Sc 2 (~8 percentage points of Crown's Order share over 3 Years differs between interpretations) and SIM-D Sc 6 (Confessor recovery vs exile under deadlock). Strict interpretation also ensures the stall-escalator (PATCH ED-760) works as anti-ossification mechanic without compounding via unintended Standing penalties.

---

### 1.2 GAP-2 (SIM-C-G6) · Settlement-Signal-derived Concern routing

**Issue.** §5.2 says "Settlement Signal propagates to controlling faction's relevant Active NPC as a Concern" but doesn't define "relevant."

**Resolution.** Three-tier routing logic.

**Patch.**

```
PATCH v1.2-2 — §5.2 Settlement Signal propagation

LOCATE: "Settlement Signal propagates to controlling faction's relevant Active NPC as a Concern (Procedure B input next Accounting). When `compute_settlement_signal` returns `None`, faction-level Concern generation skips this settlement's Signal that Accounting (sparse-settlement handling)."

REPLACE with:
    Settlement Signal propagates to controlling faction's "relevant Active NPC" as a Concern 
    (Procedure B input next Accounting). When `compute_settlement_signal` returns `None`, 
    faction-level Concern generation skips this settlement's Signal that Accounting.
    
    **Routing logic (PATCH v1.2-2 / SIM-C-G6):**
    
    function route_signal_to_concern(signal, settlement, faction):
        # Tier 1 — settlement governor if Active NPC
        if settlement.governor and settlement.governor.is_active_npc():
            return settlement.governor
        
        # Tier 2 — faction leader if seat settlement
        if settlement == faction.seat_settlement:
            return faction.leader
        
        # Tier 3 — round-robin among inner-circle by signal.primary_tag domain affinity
        # Compute domain alignment for signal's primary_tag with each inner-circle NPC's primary Conviction
        # Highest-affinity NPC receives the Concern; ties broken by Standing (higher), then NPC.id (ascending)
        candidates = []
        for npc in faction.inner_circle:
            if npc.is_active():
                affinity = DOMAIN_ARMATURE_ALIGNMENT[derive_domain(signal.primary_tag)][npc.conviction_primary]
                candidates.append((npc, affinity))
        candidates.sort(key=lambda x: (-x[1], -x[0].standing, x[0].id))
        return candidates[0][0] if candidates else None
    
    Where `derive_domain(tag)` maps Signal tag to its closest matching Project domain (e.g., 
    "raid_threat" → military; "trade_deal" → economic; "ceremonial" → theological/diplomatic).
    Authored mapping in `params/signal_tag_to_domain.md`.
    
    **Routing failures.** If Tier 3 also returns None (no Active NPCs in inner circle — extreme 
    edge case), the Signal is dropped. This should occur only during severe Faction Crisis 
    (institutional autopilot).
```

**Rationale.** Tier (a) handles cases where governance-NPC institutionally tracks the settlement (most common). Tier (b) handles seat-settlement default for the faction leader. Tier (c) distributes peripheral-settlement Concerns by relevance, preventing leader overload. Validated under cross-border (SIM-E Sc 1) and three-faction (SIM-E Sc 5) load conditions.

---

### 1.3 GAP-3 (SIM-H-G2) · Knot rupture mechanic

**Issue.** Knot rupture is referenced in §2.2 (`disposition_with_player ... can extend to -4 on Knot rupture`) but never defined: no triggers, no mechanic, no consequence cascade.

**Resolution.** Full specification of Knot rupture as a featured behavior. New §2.5.2 subsection.

**Patch.**

```
PATCH v1.2-3 — §2.5 Opinions, new §2.5.2 Knot Rupture

INSERT after §2.5.1 Opinion Initialization (PATCH 3.4):

#### 2.5.2 Knot Rupture (PATCH v1.2-3 / SIM-H-G2)

A Knot is a sustained mutual relational commitment between Active NPCs (or NPC and Player). 
Knots are formed via existing Knot system mechanics (designs/threadwork/). Knot rupture is 
the formal severance event.

**Trigger conditions.** Knot rupture fires when EITHER:
  (a) `disposition_with_partner < -2` sustained for ≥ 2 consecutive seasons, OR
  (b) Major-betrayal event: a single contradicting Memory at salience ≥ 5 against a 
      Belief held at confidence 4-5, where the Belief is Knot-related (e.g., "my partner 
      is loyal," "my partner shares my Convictions," "my partner protects me").

**Rupture event mechanic.**

```
function trigger_knot_rupture(npc_a, npc_b, cause):
    # Public event of high salience
    e = Event(
        event_type="knot_rupture",
        participants=[npc_a, npc_b],
        visibility=public,  # Knots are public commitments
        salience=5,
        cause=cause,
    )
    publish_event(e)
    
    # Mutual Disposition shift
    npc_a.disposition_with(npc_b) = -4  # extends beyond normal -3 floor
    npc_b.disposition_with(npc_a) = -4
    
    # Knot bond severed
    sever_knot(npc_a, npc_b)
    # → no future P2 mandatory Knot Outreach scenes for this pair (PATCH 3.6 supersedence
    #   does not apply post-rupture)
    
    # Memory generated for all observers (inner-circle peers + Player if peripheral)
    for observer in observers_of(e):
        m = Memory(
            timestamp=current_season,
            event_type="knot_rupture_observed",
            participants=[npc_a, npc_b, observer],
            affect=-2 if observer is npc_a or npc_b else -1,
            salience=5,
            detail=cause.description,
        )
        add_memory(observer, m)
    
    # Concerns about both parties' relational reliability propagate
    for observer in observers_of(e):
        if observer.is_active() and observer != npc_a and observer != npc_b:
            generate_concern(observer, e, event_impact_matrix)
            # Concern tag: "relational_reliability_questioned"
    
    # Mood impact for involved parties
    npc_a.mood = Grieving  # duration: 4 seasons
    npc_b.mood = Grieving
```

**Long-term consequences.**
- **Damaged-character Memory persists.** The `knot_rupture_observed` Memory is permanent salience 5 (Founding-equivalent for involved parties; high-salience long-decay for observers). Future relational events involving npc_a or npc_b are interpreted against this Memory.
- **Future Knot proposals face increased skepticism.** When npc_a or npc_b is offered a new Knot (existing Knot system mechanics), the engine increases the difficulty of acceptance — receiving NPC's `disposition_with_proposer` requires ≥ +1 (vs ≥ 0 standard) before Knot can form. Reflects loss-of-trust.
- **Belief revision potential.** If npc_a (or Player) accumulates additional contradicting Memories about relational reliability after rupture, Path B Belief revision can fire. Player's Belief "I am trustworthy in personal commitments" can revise to "I am inconstant" — generating a permanent identity Scar.
- **Faction-level reputation:** inner-circle NPCs use the rupture event in their interpretive frame for years. A ruptured-Knot NPC who later argues for institutional trust faces pre-existing skepticism.

**Recovery path.** Knot rupture is reversible only through extended trust-rebuilding:
- npc_a's Disposition with former-partner must reach ≥ 0 again (sustained 4+ seasons of consistent positive Memories).
- A new Knot proposal can be made, subject to the increased-difficulty gate.
- The original `knot_rupture_observed` Memory persists — full erasure is not possible.

**Featured behavior commentary (mirror to §1.1 Featured Behaviors).** Knot rupture is among the engine's most dramatic mechanics. It is a *politically-public personal-failure event* — both intimate and institutional. Players choosing playstyles that risk Knot rupture should be aware: this is a near-permanent character-mark, and the engine will weight it heavily in long-term relational interpretation. Designers authoring Knot-relevant content should consider Knot rupture as a *featured dramatic peak*, not a mere state-transition.

UPDATE §1.1 Featured Behaviors — append new entry:

- **Knot Rupture (PATCH v1.2-3 / SIM-H-G2).** When sustained negative Disposition or major-betrayal events sever a Knot bond, the engine produces a public salience-5 event with cascading consequences: mutual Disposition crash to -4, Memory propagation to all observers, Concerns about relational reliability in inner-circle peers, future Knot-proposal difficulty increase, possible Belief revision. The rupture Memory is permanent (Founding-equivalent for involved parties). Recovery is multi-Year and partial; the original event is never fully erased. This is the engine's strongest *intimate-political* dramatic mechanic.
```

**Rationale.** SIM-H Scenario 1 reached the Knot rupture state but trace had to invent the mechanic. The recommended specification per SIM-H Scenario 6 produces coherent cascade with public recognition, cross-relationship Opinion drift, long-term character marker, and recovery path. Treating Knot rupture as featured behavior (per SIM-H-O2) gives it appropriate spec weight — it's not a fix, it's a mechanic.

---

## §2 RECOMMENDATION PATCH — ED-760 STALL-ESCALATOR

**Issue.** SIM-B Scenario 8 surfaced structural deadlock dynamic — unequal-Standing same-domain proposers can be infinitely deadlocked. SIM-E and SIM-G validated stall-escalator as both anti-deadlock and anti-ossification mechanic.

**Resolution.** Add `+0.05 × seasons_stalled` term to `select_proposal()` score.

**Patch.**

```
PATCH v1.2-4 — §6.2 select_proposal() (PATCH 2.1)

LOCATE: "    scores[p] = conviction_alignment + standing_bonus"

REPLACE with:
    # Base: alignment + Standing bonus
    base_score = conviction_alignment + standing_bonus
    # Stall-escalator (PATCH v1.2-4 / ED-760): long-stalled projects gradually escalate
    stall_escalator = 0.05 × p.project.seasons_stalled
    scores[p] = base_score + stall_escalator

ADD note immediately after function definition:
    **Stall-escalator behavior (PATCH v1.2-4 / ED-760).** A long-stalled project escalates 
    its score by 0.05 per season of stalling. This means:
      - At seasons_stalled=0: no escalator, normal competition.
      - At seasons_stalled=4 (~1 Campaign Year of stalling): +0.20 score boost.
      - At seasons_stalled=8 (Project failure threshold): +0.40 score boost.
    
    Interaction with Standing-bonus differential: a 1-Standing differential is 0.10. So a 
    project stalled 2+ seasons can compete on equal alignment with a project from a 1-Standing-
    higher peer. Stalled 5+ seasons can outcompete a 2-Standing-higher peer.
    
    Validated at scale (SIM-E Sc 2, SIM-G Sc 1-4) as both anti-deadlock and anti-ossification 
    mechanic. Without stall-escalator, unequal-Standing same-domain collisions can produce 
    permanent winner-takes-all deadlocks — see SIM-B Scenario 8 / ED-760 in editorial ledger.
```

**Rationale.** Stall-escalator is a graceful escalation mechanism — minor effect early, growing influence over time, natural break-out for genuinely-stalled projects. Doesn't disrupt normal competition (small effect at low stall counts) but prevents Scenario-8-style permanent deadlock. Anti-ossification effect verified at long-horizon scale (SIM-G).

---

## §3 P2 RESOLUTIONS (15 patches, condensed)

### 3.1 SIM-A-G1 · Drift coefficients

```
PATCH v1.2-5 — §3.6 Conviction Alignment for Opinion Drift / Procedure D

LOCATE: drift formula in Procedure D pseudocode

REPLACE/ADD: After multiplier definition, define drift coefficients:
    base_drift = 0.3
    small_drift_coefficient = 0.3   # for confidence-aligned drift
    larger_drift_coefficient = 1.0  # for confidence-contradicting drift at low confidence

Update drift formula:
    drift = base_drift × (1 - abs(opinion.affect_axis) / 3) × multiplier
    if memory aligns with opinion:
        opinion.affect_axis += small_drift_coefficient × drift × sign(memory.affect)
        opinion.confidence += 0.0 to +1.0 (rounded)
    elif memory contradicts opinion AND opinion.confidence < 3:
        opinion.affect_axis += larger_drift_coefficient × drift × sign(memory.affect)
        opinion.confidence = max(1, opinion.confidence - 1)
    elif memory contradicts opinion AND opinion.confidence >= 3:
        # Strong Opinion holds; cognitive dissonance
        generate_concern_about_subject(npc, opinion.subject)
        if opinion.confidence in [4, 5] AND contradiction_acute:
            npc.mood = Distracted
```

### 3.2 SIM-A-G2 · Drift loop iteration order

```
PATCH v1.2-6 — §6.2 Procedure D drift loop

LOCATE: "for memory in new_memories:"

REPLACE with: 
    # Iteration order: chronological by timestamp; ties broken by salience descending
    sorted_memories = sorted(new_memories, key=lambda m: (m.timestamp, -m.salience))
    for memory in sorted_memories:
```

### 3.3 SIM-A-G3 · weighted_select() re-roll-and-average

```
PATCH v1.2-7 — §3.6.X Armature Confidence

LOCATE: "in code, weighted_select() at confidence < 0.7 should re-roll once and average results, producing more inconsistent armature behavior."

REPLACE with:
    in code, weighted_select() at confidence < 0.7 implements re-roll-and-average per dimension:
        for each dimension dim:
            sample_1 = weighted_select(weights[dim])
            sample_2 = weighted_select(weights[dim])
            if sample_1 == sample_2:
                result[dim] = sample_1
            else:
                # Average: probabilistically pick either; over many calls, produces
                # a 50/50 split between the two sampled options
                result[dim] = random.choice([sample_1, sample_2])
        return result
    
    This produces interpretation variance across calls; an NPC at confidence 0.5 
    making the same decision twice may produce different armature interpretations, 
    which is the intended behavior of "frame absent."
```

### 3.4 SIM-B-G1 · 4th-level tie-break in select_proposal

```
PATCH v1.2-8 — §6.2 select_proposal()

LOCATE: "winner = max(proposals, key=lambda p: (scores[p], p.npc.standing, p.project.seasons_stalled))"

REPLACE with:
    # Three-level tie-break: score → Standing → seasons_stalled → NPC.id (4th-level)
    winner = max(proposals, key=lambda p: (
        scores[p], p.npc.standing, p.project.seasons_stalled, -p.npc.id
    ))
    # NPC.id ascending (lower wins) provides stable deterministic 4th-level tie-break
```

### 3.5 SIM-B-G2 · Failed-deference accounting

```
PATCH v1.2-9 — §6.2 DA Proposal Phase

LOCATE: "# Displacement risk: institutional_deference check at Ob 1
            # Failure: faction leader may notice neglect"

REPLACE with:
    # Displacement risk: institutional_deference check at Ob 1
    # On failure: generates `displacement_neglect_observed` event (visibility=semi-public to 
    # faction leader); does NOT count as failed_da_proposal for Standing recalc (PATCH 3.11).
    # The proposal succeeded; only the deference check failed.
```

### 3.6 SIM-B-G3 · seasons_stalled increment on non-proposal

```
PATCH v1.2-10 — §6.2 Procedure C Project Advancement

LOCATE: "if project.progress unchanged this season:
        project.seasons_stalled += 1"

REPLACE with:
    if project.progress unchanged this season:
        project.seasons_stalled += 1
        # Increment regardless of cause: lost competition, Mood-suppression (Grieving Spirit-fail
        # or Distracted high-deference suppression), no DA proposal made, etc. Stall reflects 
        # absence of progress, not specifically competitive failure.
```

### 3.7 SIM-B-G7 · Counter state for Standing recalc

```
PATCH v1.2-11 — §8.1 NPC Standing Recalculation

LOCATE: end of §8.1 formula block

ADD note:
    **Counter state (PATCH v1.2-11 / SIM-B-G7).** Each NPC maintains:
    
        npc.year_counters = {
            completed_projects: 0,
            failed_projects: 0,
            successful_da_proposals: 0,
            failed_da_proposals: 0,
            public_conviction_scars: 0,
        }
    
    Counters increment during the Year on the appropriate events. They reset to zero at 
    end of Standing recalc (after Δ_standing computed and applied). Counters are tracked 
    per-NPC and are not visible to other NPCs (internal Standing-evaluation only).
```

### 3.8 SIM-C-G1, G2 · Signal-salience handling

```
PATCH v1.2-12 — §5.2 Settlement Signal propagation

LOCATE: "signal.salience *= 0.7  # cascade decay
    return signal"

REPLACE with:
    signal.salience *= 0.7  # cascade decay (PATCH 2.5)
    # Post-decay floor: if salience < 1, drop the Signal (sub-threshold)
    if signal.salience < 1:
        return None  # PATCH v1.2-12 / SIM-C-G2
    signal.salience = round(signal.salience)  # PATCH v1.2-12 / SIM-C-G1: integer salience
    return signal
```

### 3.9 SIM-C-G3 · interpret_event_affect

```
PATCH v1.2-13 — §5.2 SettlementSignal.from_governor

LOCATE: "affect_axis=interpret_event_affect(dominant, governor.armature),"

ADD nearby (in same function-block area):
    # interpret_event_affect: maps event affect to armature-aligned interpretation
    function interpret_event_affect(event, armature):
        # Base: event's intrinsic affect
        base = event.affect  # signed scalar from event impact matrix
        # Modulate by armature-event-type alignment
        alignment = armature_alignment_with_event_category(armature, event.event_type)
        # alignment is from CATEGORY_DEFAULT_RESONANCE (PATCH 2.7), encoded as
        # {-1=contradicted, 0=neutral, +1=aligned} -> scalar in [-1, +1]
        return base * (1 + 0.3 * alignment)
        # Aligned events appear ~1.3× their nominal affect through this armature;
        # contradicted events appear ~0.7× (preserves sign, attenuates magnitude).
```

### 3.10 SIM-C-G7 · recent_event_delta event-log

```
PATCH v1.2-14 — §5.1 Settlement Meta-Armature

LOCATE: "recent_event_delta = sum of Δ-Disposition events this faction caused this 
        settlement in last 4 seasons, exponentially decayed (×0.7^seasons_ago)."

ADD note:
    **Event-log infrastructure (PATCH v1.2-14 / SIM-C-G7).** Each settlement maintains:
    
        settlement.faction_event_history[faction] = [
            (season, delta, event_type),
            ...
        ]
    
    Capped at last 8 seasons (older entries dropped). Updated each Accounting by faction-
    governance-impact events (good/bad governance, response to crises, etc.). The 
    `recent_event_delta` formula reads from this list.
```

### 3.11 SIM-C-G8 · Repeated-Signal handling on active Concern

```
PATCH v1.2-15 — §6.2 Procedure B Generation

LOCATE: end of Generation block (after concern_history cooldown handling)

ADD note:
    **Repeated-Signal handling on active Concern (PATCH v1.2-15 / SIM-C-G8).** When a 
    Settlement Signal arrives matching an Active NPC's still-active Concern (same domain-tag), 
    the existing Concern's salience is updated via max-update:
    
        if matching_concern_active(npc, signal.primary_tag):
            existing_concern = find_active_concern(npc, signal.primary_tag)
            existing_concern.salience = max(existing_concern.salience, signal.salience)
            existing_concern.ttl = max(existing_concern.ttl, default_ttl_for_signal_tag)
            # Skip generating new Concern (deduplication)
        else:
            # Standard generation per existing flow
            generate_concern(npc, signal_event, event_impact_matrix)
    
    Prevents runaway Concern accumulation while reflecting ongoing severity.
```

### 3.12 SIM-D-G2 · P2-evasion event handling

```
PATCH v1.2-16 — §7.6 NPC Outreach Generation (PATCH 3.10)

LOCATE: end of §7.6 (after Knot exception note)

ADD subsection:
    **Player evasion of mandatory P2 (PATCH v1.2-16 / SIM-D-G2).** When the player ignores 
    a Priority 2 mandatory Outreach scene entirely (refuses attendance, sacrifices all 
    other Slate slots), the engine spawns an evasion event:
    
        e = Event(
            event_type="evasion_observed",
            participants=[outreach_npc, player],
            visibility=semi-public to outreach_npc,
            salience=4,
        )
    
    Consequences:
      - outreach_npc generates a new Concern at salience+1 vs the original Concern.
        Tag: "player_evading_<original_concern_domain>"
      - outreach_npc.mood may shift to Anxious or Distracted.
      - Memory generated in outreach_npc with affect -2 (significant negative read).
    
    Mandatory P2 evasion thus produces accelerating relational damage rather than 
    indefinite deferral. Player has agency to refuse but bears mounting cost.
```

### 3.13 SIM-D-G5 · Memory-add edge case

```
PATCH v1.2-17 — §2.6 Memories / PATCH 3.15 Passive Memory replacement

LOCATE: "2. Otherwise, drop the lowest-salience Memory."

REPLACE with:
    2. Otherwise, drop the lowest-salience existing Memory — but only if the new 
       Memory's salience is at least as high as the existing minimum. If the new 
       Memory's salience is strictly lower than min(existing.salience), refuse to 
       add the new Memory (it's not important enough to displace anything). 
       Exception: if same-tag existing Memory exists, merge per Rule 1 regardless 
       of salience comparison.
```

### 3.14 SIM-G-G1 · Mood-impact on aggregate weighting

```
PATCH v1.2-18 — §5.3 Faction Meta-Armature inner_circle_aggregate

LOCATE: "weights: Standing-based (S7: 1.0, S6: 0.7, S5: 0.5, S4: 0.3)
        leader: standing_weight × 1.5"

REPLACE with:
    weights: Standing-based (S7: 1.0, S6: 0.7, S5: 0.5, S4: 0.3), each multiplied by 
            mood_modifier (PATCH v1.2-18 / SIM-G-G1):
            mood_modifier = 1.0 if mood in {Steady, Confident, Vindicated, Resolved}
                          = 1.0 if mood in {Anxious, Humiliated} (still institutionally engaged)
                          = 0.7 if mood == Distracted (cognitive dissonance reduces institutional weight)
                          = 0.5 if mood == Grieving (active withdrawal from institutional engagement)
    leader: (standing_weight × 1.5) × mood_modifier
    
    Rationale: leaders/peers in difficult Mood states have reduced institutional weight, 
    reflecting their reduced engagement. Crown's Almud falling Distracted reduces his 
    armature contribution from 1.5 to ~1.05 (1.5 × 0.7); the inner circle's aggregate 
    shifts toward less-distracted peers. Realistic political dynamic.
```

### 3.15 SIM-E-G2 · Faction succession

```
PATCH v1.2-19 — §5.4 Faction Crisis Behaviors / new subsection

ADD subsection §5.4.1:

#### 5.4.1 Faction Succession (PATCH v1.2-19 / SIM-E-G2)

When the faction leader dies (or otherwise becomes permanently incapable — e.g., reduced 
to Standing < 4 below inner-circle threshold via long-term failure), the leader-flag must 
transfer.

**Trigger:** event_type = "leader_death" OR "leader_exit_inner_circle".

**Selection mechanic.**

```
function designate_new_leader(faction):
    # Tier 1: highest-Standing same-faction Active NPC
    candidates = [npc for npc in faction.inner_circle if npc.is_active()]
    candidates.sort(key=lambda n: -n.standing)
    
    if len(candidates) == 0:
        # Faction has no inner circle — institutional collapse
        return None  # Faction dissolves or merges per external mechanic
    
    if len(candidates) == 1:
        return candidates[0]
    
    # Tier 2 (tie-break): Conviction-alignment with faction's institutional anchor
    top_standing = candidates[0].standing
    tied_candidates = [c for c in candidates if c.standing == top_standing]
    if len(tied_candidates) == 1:
        return tied_candidates[0]
    
    tied_candidates.sort(key=lambda n: -conviction_alignment_score(n, faction.dominant_conviction))
    
    # Tier 3 (final tie-break): NPC.id ascending
    return tied_candidates[0]
```

**Cascade events on succession:**
- New leader emits `standing_change` event (now flagged as leader; meta-armature recomputation reflects 1.5× weight).
- Inner-circle peers receive Memories about succession (affect varies per their Conviction-alignment with new leader).
- Faction Meta-Armature recomputes immediately (next Accounting reflects new leader's armature).
- Optionally: succession milestone scene (Priority 3 available — player can witness if interested).

**Faction Crisis state interaction.** If the previous leader died during a Faction Crisis (multiple inner-circle Distracted/Grieving), succession may help resolve crisis (institutional clarity restored); or may extend it (new leader inherits crisis without legitimacy). Engine handles via standard Mood recovery dynamics.
```

### 3.16 SIM-H-G3 · Faction-internal coup mechanic

```
PATCH v1.2-20 — §5.4 Faction Crisis Behaviors / new subsection

ADD subsection §5.4.2:

#### 5.4.2 Leader Challenge / Coup Mechanic (PATCH v1.2-20 / SIM-H-G3)

A faction-internal peer challenger can attempt to displace the current leader through 
a Path A Total Victory Social Contest at faction-leader-Belief level.

**Trigger:** Challenger NPC initiates a Social Contest against the leader's Belief 
"I am the rightful leader of <faction>." Requires:
- Challenger.standing >= leader.standing (cannot challenge from clearly-lower position).
- Challenger.opinion_of(leader).affect_axis < -1 (sustained negative Opinion).
- Challenger has accumulated ≥ 3 contradicting Memories about leader's competence at 
  salience ≥ 3 in last 4 seasons.

**Contest dynamics.**
- Contest is Path A (Belief-level), public visibility.
- Faction Meta-Armature backs leader (institutional_stability anchor + leader's 1.5× weight 
  with current mood_modifier).
- Challenger's coalition: any inner-circle peer with `opinion_of(leader).affect_axis < 0` 
  contributes to challenger's side; any peer with `opinion_of(leader).affect_axis > 0` 
  contributes to leader's side.
- Player can support either side (if S5+ and aligned with one party).

**Outcomes.**
- **Total Victory for challenger:** leader-flag transfers; existing leader becomes peer 
  at current Standing (no automatic exile). Trigger `leader_change` event.
- **Modified Victory for challenger:** leader retains flag but accepts institutional 
  reorganization (similar to SIM-F Y4 dynamic — reorganization with minority protections).
- **Modified Defeat for challenger:** leader retains flag; challenger's Standing penalty 
  (Δ_standing -1 to -2 immediate, not waiting for Year boundary).
- **Total Defeat for challenger:** leader retains flag + challenger's Belief revises to 
  "leader is rightful" (Scar generated) + challenger may be exiled to peripheral status.

**Faction Crisis interaction.** If contest occurs during Faction Crisis (institutional 
autopilot), the contest is *the* resolution path — succession by combat, in effect. 
Crisis ends with Contest outcome.
```

### 3.17 SIM-H-G4 · Faction Crisis state resolution path

```
PATCH v1.2-21 — §5.4 Faction Crisis Behaviors / clarification

LOCATE: "Recovery: when inner-circle Mood states improve below threshold"

REPLACE with:
    Recovery paths (PATCH v1.2-21 / SIM-H-G4):
      (a) Mood states improve below threshold — happens if external pressure subsides 
          AND inner-circle peers process Concerns toward resolution. Standard recovery 
          for transient crises (e.g., plague-induced).
      (b) Succession event resolves underlying conflict — leader-death + designate_new_leader 
          (PATCH v1.2-19) OR successful Coup (PATCH v1.2-20). Leadership clarity restores 
          institutional decision-making capacity even if some peers remain Distracted.
      (c) External alliance event — formal merging or vassalage to another faction (out 
          of v1.2 scope; existing diplomatic mechanics).
    
    A Faction Crisis without resolution path through (a)-(c) is structurally degenerate 
    and indicates engine should generate diplomatic/external pressure events to force 
    resolution. Long-running crises (>8 seasons) may trigger neighbor-faction interventions.
```

### 3.18 SIM-H-G6 · Sustained war-state mechanic

```
PATCH v1.2-22 — §8 Integration / new subsection 8.2

ADD subsection §8.2 War State:

#### 8.2 Inter-Faction War State (PATCH v1.2-22 / SIM-H-G6)

Sustained military conflict between factions is tracked at faction-pair level:

```
faction_pair_state[faction_a, faction_b] = {
    war_state: bool,
    war_started_at: season,
    accumulated_military_events: list[(season, event_type, casualties)],
    diplomatic_breakdown_count: int,
}
```

**War-state trigger:**
- 3+ military Domain Actions executed against faction-pair within 4 seasons, AND
- No active treaty between factions, AND
- Diplomatic Domain Action attempted by either faction has failed within 2 seasons.

**During war state:**
- Cross-faction Settlement Signals carry war-context tag (military events at borders 
  amplify by 1.3×).
- Cross-faction Knots experience Disposition penalty (-0.2 per Accounting; sustained 
  war risks Knot rupture per PATCH v1.2-3).
- DA Proposal Phase favors military proposals in both factions (war_state flag adds 
  +0.1 to military-domain alignment scores).
- Population_disposition in border settlements drifts negative for whichever faction 
  is perceived as aggressor.

**Peace mechanism:** see PATCH v1.2-23 (treaty mechanic).
```

### 3.19 SIM-H-G7 · Inter-faction treaty / peace mechanic

```
PATCH v1.2-23 — §8.2 War State (continuation)

ADD subsection §8.2.1 Peace Treaty:

#### 8.2.1 Peace Treaty Mechanic (PATCH v1.2-23 / SIM-H-G7)

Peace treaty is a diplomatic Domain Action at faction-pair level:

```
function propose_peace_treaty(faction_a, faction_b, terms):
    # Both factions must approve
    a_approves = faction_a.meta_armature_evaluates_treaty(terms)
    b_approves = faction_b.meta_armature_evaluates_treaty(terms)
    
    if not (a_approves and b_approves):
        # Treaty rejected; war_state continues; diplomatic_breakdown_count += 1
        return TreatyOutcome.REJECTED
    
    # Both approve — treaty enters force
    treaty = Treaty(
        signatories=[faction_a, faction_b],
        terms=terms,
        signed_at=current_season,
        duration=terms.duration,  # specified in treaty
    )
    
    # End war state
    faction_pair_state[faction_a, faction_b].war_state = False
    faction_pair_state[faction_a, faction_b].war_ended_at = current_season
    
    # Generate ceremonial event
    event = Event(
        event_type="treaty_signed",
        participants=[faction_a.leader, faction_b.leader],
        visibility=public,
        salience=4,
    )
    publish_event(event)
    
    return TreatyOutcome.SIGNED
```

**Treaty terms** (authored content per scenario): may include border adjustments, 
trade provisions, Knot exchanges (royal marriages), tribute, hostage arrangements. 
Terms structured as a list of Conviction-aligned-or-contradicted commitments — each 
faction's meta-armature evaluates whether terms are acceptable.

**Treaty violation:** if a faction takes action contradicting treaty terms, generates 
high-salience contradiction Memory in opposing faction's leadership; can re-trigger 
war_state via existing dynamics.
```

---

## §4 P3 CLEANUPS (16 patches, brief)

These are minor doc/typo/authoring fixes. Listed compactly.

```
PATCH v1.2-24 (SIM-A-G4): Define knowledge_contradicts_belief() in §2.7 — tag-based 
domain matching using authored Belief-domain tags.

PATCH v1.2-25 (SIM-A-G5): §6.2 Procedure D — append note: "evidence_memory_refs 
update happens after drift application completes for the Memory."

PATCH v1.2-26 (SIM-A-G6): Standardize confidence boundary to "< 3" throughout §6.2 
Procedure D drift formula. Replace any "<= 2" or ">= 3" inconsistencies.

PATCH v1.2-27 (SIM-B-G4): §10 Content Authoring — add row "Goal text templates per 
domain | ~30 entries | params/project_goal_templates.md, 5 templates × 6 domains".

PATCH v1.2-28 (SIM-B-G5): §10 Content Authoring — add row for standard_effect_for() 
and domain_action_required_for() per-domain constants in params/.

PATCH v1.2-29 (SIM-B-G6): §8.1 Standing Recalc — add explicit note: "Use banker's 
rounding (round half-to-even) for `round()` operations to ensure determinism."

PATCH v1.2-30 (SIM-B-G9): §6.2 DA Proposal Phase — append note: "Mood-suppressed 
proposals (Distracted high-deference continue, Grieving Spirit-fail) do NOT increment 
any Year-counter for Standing recalc. They are non-events for accounting purposes."

PATCH v1.2-31 (SIM-C-G4): §2.6 Memories — append: "Salience-0 Memories are eligible 
to be dropped on next replacement check; effectively pending-replacement until cap 
pressure forces them out."

PATCH v1.2-32 (SIM-C-G5): §4.5 Resonance Lookup Fallback — add: "categorize_event_type() 
constructs an inverse dict from EVENT_CATEGORIES at engine init: 
  CATEGORY_LOOKUP = {event_type: category for category, types in EVENT_CATEGORIES.items() 
                    for event_type in types}"

PATCH v1.2-33 (SIM-D-G1): §6.2 Procedure B Resolution — append: "When Concern dissipates 
without engagement (decay-to-0 with no resolution event), generate Memory with 
event_type='concern_dissipated_without_engagement', affect=-0.5, salience=concern.salience 
(at dissipation)."

PATCH v1.2-34 (SIM-D-G3): §7.6 NPC Outreach Generation — append: "PATCH 3.6 (Knot 
Outreach P2 mandatory) supersedes PATCH 3.10 (P3 default) for Knot-partner Concerns 
about player. Knot Outreach is always P2 mandatory regardless of salience-5 escalation 
rule."

PATCH v1.2-35 (SIM-D-G4): §1.1 Featured Behaviors — rename "Standing 5 Milestone 
Visibility (N-DIAG-A)" to "Inner-Circle Threshold Milestone (N-DIAG-A, Standing 3↔4)". 
Body unchanged.

PATCH v1.2-36 (SIM-D-G6): §2.6 Memories / PATCH 3.15 — append: "Merge tie-break: 
when multiple existing Memories qualify for merge (same tag, same affect-direction), 
select most-recent (highest timestamp). Reasoning: newer event tends to be the 
'current' framing for the pattern."

PATCH v1.2-37 (SIM-E-G1): §5.2 Settlement Signal — append: "A single peninsula-scale 
event can produce one Signal per affected settlement (multi-settlement events). 
Each settlement's Signal propagates as its own Concern via routing logic (PATCH v1.2-2). 
The event itself is unique; Signals are derived per-settlement; Concerns are propagated 
per-Signal."

PATCH v1.2-38 (SIM-H-G1): §10 Content Authoring — append: "Scene templates expose 
explicit affect-direction tagging for each dialogue branch. Subversive-intent dialogue 
branches are tagged with negative-affect-direction; supportive branches with positive. 
Scene authoring should distinguish *what the player chooses to express* from the 
mechanical Memory affect produced. See params/scene_templates.md."

PATCH v1.2-39 (SIM-H-G5): §5.4 Faction Crisis Behaviors — append: "When multiple 
factions are simultaneously in Faction Crisis (institutional autopilot), cross-faction 
events (treaty proposals, diplomatic overtures) are declined by autopilot factions. 
Bounce-back events (refused-overture) accumulate as Memories in the proposing faction 
and as latent diplomatic-tension Concerns to surface when crisis-state ends. See 
post-crisis political reorganization in §5.4."
```

---

## §5 APPLICATION CHECKLIST FOR v1.2

Patches grouped for sequenced application:

**Sequence 1 — P1-Critical (apply first):**
- [ ] PATCH v1.2-1 (GAP-1, failed_da_proposals strict definition).
- [ ] PATCH v1.2-2 (GAP-2, Settlement-Signal-Concern routing).
- [ ] PATCH v1.2-3 (GAP-3, Knot rupture mechanic — also touches §1.1 featured behaviors).

**Sequence 2 — Recommendation:**
- [ ] PATCH v1.2-4 (ED-760 stall-escalator).

**Sequence 3 — P2 (15 patches):**
- [ ] PATCH v1.2-5 (drift coefficients).
- [ ] PATCH v1.2-6 (drift loop iteration order).
- [ ] PATCH v1.2-7 (weighted_select re-roll-and-average).
- [ ] PATCH v1.2-8 (4th-level tie-break).
- [ ] PATCH v1.2-9 (failed-deference accounting).
- [ ] PATCH v1.2-10 (seasons_stalled increment on non-proposal).
- [ ] PATCH v1.2-11 (Standing recalc counter state).
- [ ] PATCH v1.2-12 (Signal-salience handling).
- [ ] PATCH v1.2-13 (interpret_event_affect).
- [ ] PATCH v1.2-14 (recent_event_delta event-log).
- [ ] PATCH v1.2-15 (repeated-Signal handling).
- [ ] PATCH v1.2-16 (P2-evasion event handling).
- [ ] PATCH v1.2-17 (Memory-add edge case).
- [ ] PATCH v1.2-18 (Mood-impact on aggregate weighting).
- [ ] PATCH v1.2-19 (faction succession).
- [ ] PATCH v1.2-20 (faction-internal coup).
- [ ] PATCH v1.2-21 (Faction Crisis resolution paths).
- [ ] PATCH v1.2-22 (war state mechanic).
- [ ] PATCH v1.2-23 (peace treaty mechanic).

**Sequence 4 — P3 cleanups (PATCH v1.2-24 through v1.2-39):** 16 brief patches.

**Sequence 5 — Header update:** doc 12 v1.1 → v1.2; update §0.1 change log to reflect v1.2 patches.

**Verification gates:**
- After each P1 patch: re-read affected section; confirm semantic intent matches PATCH RATIONALE.
- After Sequence 2: spot-check `select_proposal()` behavior under SIM-B Sc 8 condition (deadlock should now break around seasons_stalled 4-5).
- After all patches: full re-read of v1.2; verify no regressions; run §13 Promotion Checklist.

**Expected output:** `12_development_specification.md` v1.2 (~1700-1900 lines, up from 1565). Three new top-level subsections: §2.5.2 Knot Rupture, §5.4.1 Faction Succession, §5.4.2 Coup Mechanic, §8.2 War State. Updated §0.1 change log. Total ~30 new patches applied.

---

## §6 OUTPUT EXPECTATIONS

After v1.2 application + re-vet pass, doc 12 should:
- Have all 39 specification gaps resolved.
- Include 3 new featured-behavior commentaries (Knot Rupture, Faction Succession, Coup).
- Have all formulas explicit (drift coefficients, mood-impact weighting, stall-escalator, etc.).
- Be ready for §13 Promotion Checklist evaluation toward canonical.

After canonical promotion, the engine reaches:
- Implementation-ready specification.
- Comprehensive simulation-validated invariants.
- Documented emergent properties.
- Recorded forward-looking design observations for future iterations.

---

**END OF v1.2 SPECIFICATION REVISIONS.**
