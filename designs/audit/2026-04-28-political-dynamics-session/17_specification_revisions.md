<!-- [PROVISIONAL: 2026-04-29 session — specification revisions v1] -->
<!-- STATUS: PROVISIONAL — proposed resolutions for 68 issues from docs 13/14/15/16 -->
<!-- POSITION: designs/audit/2026-04-28-political-dynamics-session/17_specification_revisions.md -->
<!-- COMPANION: 12_development_specification.md is the target of the patches in this document. -->

# Political Dynamics Specification Revisions v1

**Status:** PROVISIONAL — proposed resolutions; pending Jordan review and application to doc 12.
**Predecessors:** 13_stress_tests_extended.md · 14_ners_stress_tests.md · 15_stress_tests_batch3.md · 16_session_close_observations.md.
**Scope:** Resolutions for the 68 issues identified in docs 13/14/15, organized as in 16. Each resolution carries (a) issue context, (b) proposed resolution, (c) exact patch text for application to doc 12, (d) rationale.

---

## §0 READING GUIDE

This document is the response to the 68-issue stress test. Its purpose is to specify the spec-edits that resolve the implementation-blocking and authoring-blocking issues, with exact patch text. Application to `12_development_specification.md` is a follow-up session.

Structure:
- §1 — One cross-cutting architectural change: **single-writer Opinion model**. This resolves three issues simultaneously (E-HORIZ-A / S-HORIZ-A / ST-32-A) and dictates how Procedures B and C are rewritten. Read this first; subsequent resolutions reference it.
- §2 — Priority-1 resolutions (8 items): blockers for any implementation work.
- §3 — Priority-2 resolutions (15 items): blockers for content authoring.
- §4 — Priority-3 resolutions (16 items): implementation-time issues with stub resolutions sufficient for current planning depth.
- §5 — Featured-behavior items (4 items): document-as-designed; no spec change.
- §6 — Items requiring Jordan decision (5 items): cannot be resolved without design call.
- §7 — Application checklist for v1.1 doc 12 revision.

Convention for patch blocks:
```
PATCH N — <doc 12 section>
LOCATE: <unambiguous text marker in current doc 12>
REPLACE WITH: <new text>
```
Where the patch is an insertion, LOCATE points to the line after which insertion happens. Where the patch removes text, REPLACE WITH is empty or stated.

---

## §1 CROSS-CUTTING — SINGLE-WRITER OPINION MODEL

### 1.1 Problem

Three procedures currently write to NPC Opinions in the same Accounting:
- Procedure B-Resolution: when a Concern resolves, may directly modify Opinion of subject NPC.
- Procedure C-Completion: `apply_project_legacy()` writes to Opinions of supporters and obstructors.
- Procedure D-Drift: processes new Memories and modifies Opinions accordingly.

Because B-Resolution also creates a Memory record of the resolution, and Procedure D then processes that Memory in the same Accounting, the same evidence drives two separate Opinion changes. This is the double-write problem (ST-32-A). It produces a single-responsibility violation (E-HORIZ-A) and a sequencing problem (S-HORIZ-A: changes from C land before D, so C's writes pre-decay D's drift surface).

### 1.2 Resolution

Procedure D becomes the **sole writer** to Opinions. Procedures B and C produce only Memories. The Opinion-state changes those Memories imply are computed in Procedure D's existing drift loop.

This means:
- B-Resolution writes a Memory of the resolution (event_type = `concern_resolved`); never touches Opinion directly.
- C-Completion writes Memories tagged `project_legacy_support` / `project_legacy_obstruction`; never touches Opinion directly.
- D processes ALL new Memories from the season, including those produced earlier this Accounting by B and C, in one consolidated drift pass.

Because the Accounting order is fixed at B → DA → C → D → E, all Memories produced this Accounting (by B and C) are visible to D when it runs. There is no inter-Accounting lag; the consolidation happens in-band.

### 1.3 Knock-on effect: drift parameters

Because D now sees more Memories per Accounting (including resolution-Memories and project-legacy-Memories that previously bypassed D), the per-Memory drift values in Procedure D should remain unchanged. The total Opinion change is now correctly attributed to one mechanism rather than spread across three with double-counting.

The resolution-Memory's `affect` carries the directional signal that B-Resolution used to write directly. The project-legacy-Memory's salience (4) is high enough that drift × dampening still produces a substantial Opinion shift over 1-2 Accountings, comparable to the prior direct write but properly subject to Conviction-alignment multiplication.

### 1.4 Patch — Procedure B Resolution

```
PATCH 1.4 — §6.2 Procedure B Resolution

LOCATE: "if concern.salience <= 0 OR ttl exhausted:"

REPLACE the apply_resolution() block with:

            resolution = resolve_concern(npc, concern)
            
            # Belief revision (direct — produces Scar, not Opinion change)
            if resolution.causes_belief_revision:
                if resolution.contradiction_strength == "strong":
                    revise_belief_to_scar(npc, resolution.target_belief)
                    npc.scars_total += 1
                    if resolution.target_belief.engages_conviction_primary:
                        npc.scars_conviction += 1
                else:
                    modify_belief(npc, resolution.target_belief, resolution.delta)
            
            # Resolution Memory (D consumes — drives Opinion change next)
            if resolution.subject_npc_id:
                m = Memory(
                    timestamp=current_season,
                    event_type="concern_resolved",
                    participants=[npc.id, resolution.subject_npc_id],
                    affect=resolution.implied_affect,           # +/- per resolution polarity
                    salience=resolution.salience,                # carries Concern salience at resolution
                    detail=resolution.text,
                )
                add_memory(npc, m)                               # respects 10-Memory cap with merge/drop
            
            # Concern history (cooldown: see §3 N-BOT-C)
            npc.concern_history.append(resolution.tag)
            if len(npc.concern_history) > 5:
                npc.concern_history.pop(0)
            
            remove(concern)
```

### 1.5 Patch — Procedure C Project Completion

```
PATCH 1.5 — §6.2 Procedure C Project Completion

LOCATE: "# Project legacy (added in stress test patches):"

REPLACE the apply_project_legacy block with:

            # Project legacy → Memories only (D consolidates Opinion change)
            for supporter_id in project.supporters:
                m = Memory(
                    timestamp=current_season,
                    event_type="project_legacy_support",
                    participants=[npc.id, supporter_id],
                    affect=+0.5,                                  # was direct Opinion delta
                    salience=4,                                   # legacy weight
                    detail=f"Stood with me on {project.goal_short}",
                )
                add_memory(npc, m)
            for obstructor_id in project.obstructors:
                m = Memory(
                    timestamp=current_season,
                    event_type="project_legacy_obstruction",
                    participants=[npc.id, obstructor_id],
                    affect=-0.5,
                    salience=4,
                    detail=f"Worked against me on {project.goal_short}",
                )
                add_memory(npc, m)
```

### 1.6 Patch — Procedure D unchanged interface

Procedure D's logic in doc 12 already iterates Memories and applies drift. No change needed to D's drift loop — only that D is now the only writer. Confirm this by adding a banner to §6.2 D:

```
PATCH 1.6 — §6.2 Procedure D banner

LOCATE: "#### Procedure D — Opinion Drift"

INSERT immediately under heading:

> **Single-writer invariant.** Procedure D is the only procedure that mutates 
> Opinions. Procedures B-Resolution and C-Completion produce Memories; D consolidates 
> all season-Memory effects into Opinion changes. See §1 of revisions doc 17 for 
> rationale.
```

### 1.7 Verification claim

After application of patches 1.4–1.6, the following invariants hold:
- For any season, the sum of Opinion deltas equals exactly Σ (per-Memory drift) over Memories created this season, with no double-attribution.
- Opinion changes are reproducible from the Memory sequence alone (no hidden writes from B or C).
- The Concern-resolution → Opinion-shift pathway is preserved end-to-end, just routed through D.
- Project legacy effects are preserved at comparable magnitude (Memory salience 4 yields drift comparable to the prior direct ±0.5 write under D's standard formula).

---

## §2 PRIORITY-1 RESOLUTIONS (8 items)

These are blockers for any implementation work.

### 2.1 — E-36-A · `select_proposal()` and domain_armature_alignment table

**Issue.** Doc 12 §6.2 Domain Action Proposal Phase calls `faction_meta_armature.select_proposal(proposals_in_faction)` for inner-circle competition but does not define the algorithm or the domain_armature_alignment table it would require.

**Resolution.** Score each proposal as the Faction Meta-Armature's Conviction-weighted alignment with the Project's domain, plus a small Standing modifier. Highest score wins. Ties broken by Standing, then by `seasons_stalled` (higher → wins, prevents perpetual stall).

```
function select_proposal(proposals):
    scores = {}
    for p in proposals:
        meta_armature = p.faction.meta_armature
        domain = p.project.project_domain
        # Conviction-weighted domain alignment
        conviction_alignment = sum(
            meta_armature.conviction_weights[c] × DOMAIN_ARMATURE_ALIGNMENT[domain][c]
            for c in CONVICTIONS
        )
        # Standing bonus (modest, breaks near-ties)
        standing_bonus = p.npc.standing × 0.1
        scores[p] = conviction_alignment + standing_bonus
    
    winner = max(proposals, key=lambda p: (scores[p], p.npc.standing, p.project.seasons_stalled))
    return winner
```

`meta_armature.conviction_weights[c]` is a normalized 7-vector summing to 1.0, derived from the inner-circle aggregate (existing — §5.3) plus institutional_stability anchor toward the faction's historical dominant Conviction.

**DOMAIN_ARMATURE_ALIGNMENT table (42 entries, 0.0–1.0):**

| domain | Faith | Order | Reason | Equity | Precedent | Autonomy | Continuity |
|---|---|---|---|---|---|---|---|
| military | 0.3 | 1.0 | 0.6 | 0.2 | 0.5 | 0.4 | 0.7 |
| theological | 1.0 | 0.4 | 0.3 | 0.3 | 0.7 | 0.2 | 0.6 |
| scholarly | 0.2 | 0.4 | 1.0 | 0.5 | 0.6 | 0.7 | 0.4 |
| intelligence | 0.3 | 0.7 | 0.8 | 0.2 | 0.5 | 0.6 | 0.5 |
| economic | 0.2 | 0.5 | 0.7 | 0.6 | 0.4 | 0.8 | 0.4 |
| diplomatic | 0.5 | 0.6 | 0.5 | 0.7 | 0.6 | 0.4 | 0.6 |

Six domains × seven Convictions. Add rows as new domains are introduced (personal_legacy, courtship, etc., per content authoring).

**Patch.**

```
PATCH 2.1 — §6.2 DA Proposal Phase

LOCATE: "winner = faction_meta_armature.select_proposal(proposals_in_faction)"

REPLACE with the function definition above. Add a new subsection at end of §5.3 
(Faction Meta-Armature) titled "Proposal Selection" containing:

   The Faction Meta-Armature ranks competing inner-circle proposals via 
   select_proposal(), defined in §6.2. The DOMAIN_ARMATURE_ALIGNMENT table is 
   authored content (see §10).

Add to §10 Content Authoring Requirements:

   | Domain × Conviction alignment table | 42+ | 6+ Project domains × 7 Convictions |

LOCATE existing row "Conviction × event symbolic resonance table" — insert above it.
```

**Rationale.** Faction Meta-Armature already aggregates inner-circle armatures (§5.3); using its Conviction weights to score domain alignment is a natural extension. The table values follow Renaissance institutional logic: military aligns with Order (discipline) and Continuity (inherited authority); theological aligns with Faith definitionally and Precedent (canon); scholarly aligns with Reason and Autonomy (intellectual freedom); etc. Standing bonus is small (0.1 × standing where standing ∈ [3,7] → max 0.7) so a low-aligned proposal cannot win on Standing alone.

**Authoring impact.** ~42 entries (new). Subsequent domain additions: +7 per domain.

---

### 2.2 — E-48-A · `max_scars` definition

**Issue.** §5.3 Faction Meta-Armature `institutional_stability` formula uses `max_scars` denominator; undefined.

**Resolution.** `max_scars = inner_circle_active_npc_count × 2`.

**Patch.**

```
PATCH 2.2 — §5.3 Faction Meta-Armature

LOCATE: "weight: 0.4 × (1 - (total_inner_circle_scars / max_scars))"

REPLACE with:
    weight: 0.4 × max(0, 1 - (total_inner_circle_scars / (inner_circle_active_npc_count × 2)))
```

**Rationale.** A typical Active NPC accumulates ~2 conviction-engaging Scars over a long campaign. An inner circle of 5–7 NPCs yields max_scars 10–14. As collective Scarring approaches that ceiling, institutional_stability decays toward 0, modeling the realistic dynamic where a faction whose inner circle has lost its Conviction anchors loses institutional weight. The `max(0, ...)` floor handles overshoot (inner circle exceeds typical Scar count).

**Note.** Total scars uses `scars_total` (not `scars_conviction`) — institutional weight responds to all Belief revisions, not only those engaging primary Conviction. See P2-N-33-A for the split.

---

### 2.3 — E-BOT-A · `conviction_alignment_multiplier` values

**Issue.** §6.2 Procedure D drift formula `drift = base_drift × (1 - abs(opinion.affect_axis) / 3) × conviction_alignment_multiplier` — multiplier values undefined.

**Resolution.** Define multiplier table and an OPPOSITIONAL pair set.

```
conviction_alignment_multiplier(npc_a, npc_b):
    if npc_a.conviction_primary == npc_b.conviction_primary:
        return 1.5
    if npc_a.conviction_secondary and npc_b.conviction_secondary and (
        npc_a.conviction_primary == npc_b.conviction_secondary or
        npc_a.conviction_secondary == npc_b.conviction_primary
    ):
        return 1.2
    if (npc_a.conviction_primary, npc_b.conviction_primary) in OPPOSITIONAL_CONVICTION_PAIRS:
        return 0.7
    return 1.0

OPPOSITIONAL_CONVICTION_PAIRS = {
    (Faith, Reason), (Reason, Faith),
    (Order, Autonomy), (Autonomy, Order),
    (Precedent, Equity), (Equity, Precedent),
    (Continuity, Reason), (Reason, Continuity),
}
```

**Patch.**

```
PATCH 2.3 — §6.2 Procedure D

LOCATE: "drift = base_drift × (1 - abs(opinion.affect_axis) / 3) × conviction_alignment_multiplier"

INSERT above the line:
    multiplier = conviction_alignment_multiplier(npc, opinion.subject_npc)

REPLACE the line with:
    drift = base_drift × (1 - abs(opinion.affect_axis) / 3) × multiplier

INSERT new subsection in §3 (THE ARMATURE), at the end, titled "3.6 Conviction 
Alignment for Opinion Drift", containing the multiplier function and OPPOSITIONAL 
pair set above.
```

**Rationale.** NPCs sharing primary Conviction interpret each other's actions through a sympathetic frame, amplifying confidence in the Opinion-direction (1.5×). Sharing secondary as a bridge produces partial sympathy (1.2×). Oppositional Convictions (the four canonical antagonisms in the seven-Conviction system: Faith↔Reason, Order↔Autonomy, Precedent↔Equity, Continuity↔Reason) dampen drift — the NPC's interpretive frame treats the other as untrustworthy regardless of evidence (0.7×). All other pairings are neutral (1.0×).

The multiplier compounds with the existing dampening factor `(1 - |affect|/3)`. Combined effect at extremes: a Faith NPC opining Reason-NPC at affect_axis +2 has dampening 0.33 × oppositional 0.7 = 0.23. So a Faith NPC's positive Opinion of a Reason NPC moves slowly even with positive Memory evidence — the design intent is "you don't change your mind easily about someone whose worldview opposes yours."

Note: Continuity↔Reason appears intentionally — Reason as restless innovation pressures Continuity's preserve-the-existing logic. This may be tuned if playtesting reveals unintended antagonism.

---

### 2.4 — E-HORIZ-A / S-HORIZ-A / ST-32-A · Single-writer Opinion

**Issue.** Three procedures write to Opinions; double-counting and ordering issues. See §1 above.

**Resolution.** Specified in §1 of this doc. Patches 1.4, 1.5, 1.6 apply.

---

### 2.5 — ST-20-A · Empty Passive NPC null guard in Settlement Signal

**Issue.** §5.2 `compute_settlement_signal` calls `max(grouped, key=...)` which crashes when `grouped` is empty (no Passive NPCs in settlement, or none with recent Memories).

**Resolution.** Three guards: empty Passive NPC set, empty weighted_memories, empty grouped. Each returns early; if a governor exists, fall back to governor armature; otherwise return None (Settlement does not produce Signal this Accounting).

**Patch.**

```
PATCH 2.5 — §5.2 Settlement Signal

LOCATE: "function compute_settlement_signal(settlement, recent_memories):"

REPLACE the entire function body with:

    # Guard 1: settlement has no Passive NPCs
    if not settlement.passive_npcs:
        if settlement.governor:
            return SettlementSignal.from_governor(settlement.governor, settlement.recent_events)
        return None  # remote settlement w/ no governor and no Passive NPCs — no Signal
    
    # Aggregate Passive NPC Memories from last 2 seasons
    weighted_memories = []
    for npc in settlement.passive_npcs:
        for memory in npc.recent_memories(seasons=2):
            # Disposition-with-player only amplifies player-involving Memories (S-44-A)
            if memory.involves_player:
                weight = memory.salience * npc.local_disposition_with_player
            else:
                weight = memory.salience
            weighted_memories.append((memory, weight))
    
    # Guard 2: Passive NPCs exist but no recent Memories
    if not weighted_memories:
        return None
    
    # Group by event_type tag
    grouped = group_by_event_type(weighted_memories)
    
    # Guard 3: all weights zero (rare but possible)
    if not grouped or all(sum_of_weights(g) == 0 for g in grouped):
        return None
    
    dominant_tag = max(grouped, key=sum_of_weights)
    
    total_weight = sum(w for _, w in weighted_memories)
    net_affect = sum(memory.affect * w for memory, w in weighted_memories) / total_weight
    
    signal = SettlementSignal(
        affect_axis=net_affect,
        primary_tag=dominant_tag,
        salience=min(5, max(1, abs(net_affect) * 2)),
    )
    signal.salience *= 0.7  # cascade decay
    return signal

ADD nearby:

function SettlementSignal.from_governor(governor, recent_events):
    # Governor-only fallback for settlements without Passive NPCs.
    # Build Signal from governor's interpretation of recent events.
    if not recent_events:
        return None
    dominant = max(recent_events, key=lambda e: e.salience)
    return SettlementSignal(
        affect_axis=interpret_event_affect(dominant, governor.armature),
        primary_tag=dominant.event_type,
        salience=dominant.salience * 0.5,  # governor-only Signal at half weight
    )
```

**Rationale.** Three specific failure modes (empty list at three call sites) → three guards. The governor fallback preserves Signal generation for sparse settlements; halved salience reflects reduced institutional weight (one voice, not aggregated). Returning None propagates cleanly: faction-level Concern generation skips this settlement's Signal that Accounting.

---

### 2.6 — ST-23-A · `conviction_secondary=None` at Scar 3+

**Issue.** §3.2 `modify_by_scar_count` says "Scar 3+: secondary leads" — undefined when conviction_secondary is None.

**Resolution.** Specify uniform-distribution fallback for the secondary share when conviction_secondary is None, representing protracted identity dissolution (NPC has lost the primary frame but has no replacement).

**Patch.**

```
PATCH 2.6 — §3.2 modify_by_scar_count

REPLACE the entire docstring/spec with:

    Scar 0: 100% conviction_primary weights
    Scar 1: 75% primary + 25% secondary
        if conviction_secondary is None: 100% primary, but reduce armature 
        confidence (see §3.6.X) — flag the NPC's interpretation as low-confidence
    Scar 2: 50% primary + 50% secondary
        if conviction_secondary is None: 75% primary + 25% UNIFORM-FALLBACK
    Scar 3+: secondary leads (75% secondary + 25% primary)
        if conviction_secondary is None: 50% primary + 50% UNIFORM-FALLBACK
            (NPC in protracted identity crisis — interpretations diffuse)

Where UNIFORM-FALLBACK assigns equal weight (1/n) to every option in each dimension, 
representing absence of an interpretive frame.

INSERT new subsection §3.6.X "Armature Confidence" near §3.2:

    Armature confidence is a derived scalar [0,1] tracking the coherence of the NPC's 
    interpretive frame. Confidence = 1.0 when armature is dominated by one Conviction 
    (single coherent frame). Confidence = 0.5 when armature is mixed primary+secondary. 
    Confidence < 0.5 when uniform-fallback is active (frame absent). Low confidence 
    increases per-event interpretation variance; in code, weighted_select() at 
    confidence < 0.7 should re-roll once and average results, producing more 
    inconsistent armature behavior.
```

**Rationale.** Many NPCs are conviction_primary only. The previous spec implied a graceful primary→secondary transition that does not work when secondary is undefined. Uniform fallback represents identity dissolution mechanically: the NPC's interpretations become unpredictable (high variance), which is the realistic outcome of an NPC whose worldview has been shattered without a replacement frame. Designer alternatives considered:
- Lock secondary to faction's institutional Conviction at high Scar count: violates per-NPC autonomy (the NPC becomes a faction-puppet at trauma).
- Keep primary Conviction at 100% always: contradicts the existing spec's intent that high Scarring shifts the armature.

The uniform-fallback path preserves both autonomy and the high-Scar shift, at the cost of accepting that some NPCs become genuinely chaotic at high trauma. This is realistic and produces interesting emergent narrative (an NPC's behavior becomes hard to predict — a player concern in itself).

---

### 2.7 — ST-24-A · Unknown event_type fallback

**Issue.** §4 Event Impact Matrix consults the 210-entry symbolic resonance table; unknown event_types crash the lookup.

**Resolution.** Category-based fallback. Each event_type is authored with a category tag; unknown event_types fall back to category defaults. A final `default` category catches truly unrecognized events (returns neutral on all Convictions).

```
EVENT_CATEGORIES = {
    violent: ["assault", "battle", "execution", "raid", "siege", "duel", ...],
    institutional_change: ["promotion", "demotion", "appointment", "dismissal", "succession", ...],
    discovery: ["revelation", "investigation_break", "confession", "evidence_surface", ...],
    ceremonial: ["coronation", "wedding", "funeral", "mass", "audience", ...],
    economic: ["trade_deal", "tariff", "windfall", "bankruptcy", "embargo", ...],
    diplomatic: ["treaty", "envoy_received", "alliance", "rupture", "summit", ...],
    personal: ["birth", "death_natural", "courtship", "knot_formation", "knot_rupture", ...],
    default: [],  # fallback for unrecognized
}

CATEGORY_DEFAULT_RESONANCE = {
    violent:               {Faith: contradicted, Order: neutral, Reason: neutral, Equity: contradicted, Precedent: neutral, Autonomy: neutral, Continuity: neutral},
    institutional_change:  {Faith: neutral, Order: contradicted, Reason: neutral, Equity: neutral, Precedent: contradicted, Autonomy: aligned, Continuity: contradicted},
    discovery:             {Faith: neutral, Order: neutral, Reason: aligned, Equity: neutral, Precedent: neutral, Autonomy: aligned, Continuity: neutral},
    ceremonial:            {Faith: aligned, Order: aligned, Reason: neutral, Equity: neutral, Precedent: aligned, Autonomy: neutral, Continuity: aligned},
    economic:              {Faith: neutral, Order: neutral, Reason: aligned, Equity: contradicted, Precedent: neutral, Autonomy: aligned, Continuity: neutral},
    diplomatic:            {Faith: neutral, Order: aligned, Reason: aligned, Equity: aligned, Precedent: neutral, Autonomy: neutral, Continuity: neutral},
    personal:              {Faith: neutral, Order: neutral, Reason: neutral, Equity: neutral, Precedent: neutral, Autonomy: neutral, Continuity: neutral},
    default:               {Faith: neutral, Order: neutral, Reason: neutral, Equity: neutral, Precedent: neutral, Autonomy: neutral, Continuity: neutral},
}

function resonance_lookup(conviction, event_type):
    if (conviction, event_type) in RESONANCE_TABLE:
        return RESONANCE_TABLE[(conviction, event_type)]
    category = categorize_event_type(event_type)  # returns "default" if unknown
    return CATEGORY_DEFAULT_RESONANCE[category][conviction]
```

**Patch.**

```
PATCH 2.7 — §4 EVENT IMPACT MATRIX

ADD new subsection §4.5 "Resonance Lookup Fallback" containing the function and 
tables above. Cross-reference from §4.1 where symbolic_effects are described.
```

**Rationale.** Category fallback keeps Matrix construction crash-free under content extension. Authors adding new event_types without updating the 210-entry table get a sensible default automatically. Categorical defaults are derived from Renaissance institutional logic: violence threatens Faith and Equity definitionally; institutional_change threatens Order/Precedent/Continuity (which value stasis) and aligns with Autonomy (which values dynamism); discovery aligns with Reason and Autonomy; etc. The `default` row is fully neutral so unrecognized events cause no spurious resonance.

**Coupling note.** This patch is independent of the E-38-A/B Jordan decision. If E-38 cuts the symbolic_effects table, this fallback machinery becomes unused but harmless. If E-38 keeps the table and defines consumption, this fallback fills authoring gaps gracefully.

---

### 2.8 — E-BOT-B · Armature modifier composition (additive, normalized)

**Issue.** §3.2 stacks `modify_by_personality`, `modify_by_scar_count`, `modify_by_active_projects`, `modify_by_active_concerns` — composition operation undefined; no normalization rule.

**Resolution.** Specify additive composition with floor-at-zero and per-dimension normalization to a probability distribution.

**Patch.**

```
PATCH 2.8 — §3.2 Weight Derivation

REPLACE the procedural pseudocode for compute_armature with:

function compute_armature(npc):
    # Base — dict[dim][option] -> [0, 1]
    weights = base_weights_from_conviction(npc.conviction_primary)
    
    # Modifiers compose ADDITIVELY. Each returns a delta dict[dim][option] -> delta 
    # (sparse: only non-zero entries). add_modifier mutates in-place.
    add_modifier(weights, personality_modifier(npc.personality))
    add_modifier(weights, scar_modifier(npc.scars_conviction, npc.conviction_primary, npc.conviction_secondary))
    add_modifier(weights, project_modifier(npc.active_projects))
    add_modifier(weights, concern_modifier(npc.active_concerns))
    
    # Floor at 0 — modifier deltas can be negative; never go below zero
    for dim in ARMATURE_DIMENSIONS:
        for option in weights[dim]:
            weights[dim][option] = max(0.0, weights[dim][option])
    
    # Normalize per dimension — each dimension becomes a probability distribution
    for dim in ARMATURE_DIMENSIONS:
        total = sum(weights[dim].values())
        if total > 0:
            for option in weights[dim]:
                weights[dim][option] /= total
        else:
            # all options zeroed (rare) — uniform fallback
            n = len(weights[dim])
            for option in weights[dim]:
                weights[dim][option] = 1.0 / n
    
    return weights

function add_modifier(weights, delta):
    for dim, opt_dict in delta.items():
        for option, delta_value in opt_dict.items():
            weights[dim][option] = weights[dim].get(option, 0) + delta_value

INSERT note at end of §3.2:

    Composition order (personality → scar → project → concern) is irrelevant under 
    additive composition; the order is fixed for reproducibility. Modifiers compose 
    independently; no modifier multiplicatively interacts with another. Per-dimension 
    normalization preserves the probabilistic interpretation: armature[dim] sums to 
    1.0 over its options, suitable for weighted_select().
```

**Rationale.** Additive composition is order-independent (a + b = b + a), supports negative deltas (low risk_tolerance: −0.1 to mechanism.calculation), and is intuitive to author ("personality contributes +0.1 to mechanism.calculation"). Multiplicative composition would require carefully designed neutral multipliers (1.0) and would compose order-dependently. Per-dimension normalization preserves armature as a probability distribution per dimension, which is what `weighted_select()` consumes. Floor-at-zero handles aggressive negative deltas without producing negative-probability weights.

**Implication for modifier authoring.** Each modifier function (personality, scar, project, concern) returns a sparse delta dict. Modifier deltas are typically ±0.05 to ±0.2, with the largest deltas reserved for scar_modifier at high Scar counts (which can shift up to ±0.5 per option as armature rotates from primary to secondary).

---


## §3 PRIORITY-2 RESOLUTIONS (15 items)

These resolve before content authoring begins.

### 3.1 — N-BOT-C · `concern_history` consumption

**Issue.** §2.2 declares `concern_history: list of last 5 resolved Concern tags`, written by Procedure B-Resolution, never read.

**Resolution.** Use `concern_history` as a regeneration cooldown: an NPC who has just resolved a Concern in domain X is suppressed from regenerating a fresh Concern in domain X unless triggered by a high-salience event (≥4). High-salience events bypass the cooldown — major events are exempt.

**Patch.**

```
PATCH 3.1 — §6.2 Procedure B Generation

LOCATE: "For each event in last_season.events:"

REPLACE the inner loop body with:

    For each event in last_season.events:
        For each NPC in event.affected_npcs:
            # Visibility gate (see PATCH 3.3 / N-BOT-E)
            if not npc_observes_event(npc, event):
                continue
            if NPC is Active:
                # Concern regeneration cooldown (concern_history)
                potential_tag = derive_concern_tag(event, npc.armature)
                if potential_tag in npc.concern_history and event.salience < 4:
                    continue  # recent same-domain Concern resolved; suppress regen
                
                concern = generate_concern(npc, event, event_impact_matrix)
                npc.concerns.append(concern)
                if len(npc.concerns) > 3:
                    drop_lowest_salience_concern(npc)

ADD note at §2.2 (concern_history field):

    `concern_history` operates as a Concern-regeneration cooldown. NPCs do not 
    regenerate a Concern in a domain whose tag matches a recent (last 5) resolution, 
    unless event salience ≥ 4.
```

**Rationale.** Without the cooldown, a single ongoing crisis can perpetually regenerate the same Concern in an NPC every Accounting, monopolizing Concern slots. The cooldown gives space for other Concerns to surface. The salience-4 bypass ensures genuine escalations (major events) do break through — otherwise NPCs would seem unrealistically apathetic to recurring problems.

---

### 3.2 — N-BOT-D · `knowledge_type` decay implementation

**Issue.** §2.7 declares decay behavior per knowledge_type but no procedure implements it.

**Resolution.** Add a Knowledge-decay step at the start of Procedure B (before Generation), iterating all Active NPCs' Knowledge.

**Patch.**

```
PATCH 3.2 — §6.2 Procedure B (new sub-step at start)

INSERT immediately after "#### Procedure B — Concern Generation and Resolution":

##### B.0 — Knowledge Decay (new sub-step, runs before Generation)

For each Active NPC:
    For each knowledge in npc.knowledge:
        if not knowledge.valid:
            continue  # invalidated Knowledge is not decayed; awaiting Concern processing
        if knowledge.knowledge_type == "ongoing_state":
            knowledge.salience -= 0.5
        elif knowledge.knowledge_type == "structural":
            knowledge.salience -= 0.1
        elif knowledge.knowledge_type == "historical_event":
            pass  # no decay; permanent
        knowledge.salience = max(0, knowledge.salience)
    
    # Cull dead Knowledge
    npc.knowledge = [k for k in npc.knowledge 
                     if k.salience >= 1 or k.referenced_recently(seasons=4)]

Where referenced_recently is set by any Procedure that uses the Knowledge fact 
(e.g., Procedure E knowledge sharing increments it).
```

**Rationale.** Implements §2.7's stated decay rules. Cull threshold of salience<1 prevents indefinite Knowledge-list growth. The 4-season recency window keeps recently-shared Knowledge alive past one decay step; otherwise structural Knowledge (-0.1/season) would never be culled and ongoing_state Knowledge (-0.5/season) would be culled in 4 seasons regardless of usage.

---

### 3.3 — N-BOT-E · `visibility` enforcement in Concern generation

**Issue.** §4.1 EventImpact.visibility is authored (public/semi_public_observers/private_observers) but Procedure B treats all `event.affected_npcs` as observers.

**Resolution.** Gate Concern generation on visibility. An NPC is an observer iff event is public, OR the NPC is in semi_public_observers, OR the NPC is in private_observers.

**Patch.**

```
PATCH 3.3 — §6.2 Procedure B

ADD helper near the top:

function npc_observes_event(npc, event):
    if event.visibility.public:
        return True
    if npc.id in event.visibility.semi_public_observers:
        return True
    if npc.id in event.visibility.private_observers:
        return True
    return False

INSERT in Generation loop (per PATCH 3.1):

    if not npc_observes_event(npc, event):
        continue  # NPC has no Knowledge of event; no Concern generated
```

Note: PATCH 3.1 already includes this call. Patches 3.1 and 3.3 are co-applied.

**Rationale.** The visibility field is part of the data structure for a reason: not every NPC sees every event. Without this gate, private events (e.g., a covert meeting between two NPCs witnessed by no one else) would generate Concerns in NPCs across the peninsula, breaking the opacity model. The patch correctly scopes Concern generation to actual observers.

**Knock-on.** Future patches can extend the gate to allow indirect observation (NPC X tells NPC Y about a private event → Y's Knowledge update → Knowledge → Belief trigger fires a Concern via the §2.7 path). The visibility gate is for direct first-hand observation; gossip-mediated observation routes through Knowledge.

---

### 3.4 — ST-15-A/B · Opinion initialization on first contact

**Issue.** Procedures D and E mutate `npc.opinions[subject]`; if no Opinion exists for that subject (first contact this season), the dictionary access crashes (ST-15-B) or produces uninitialized affect (ST-15-A).

**Resolution.** Lazy initialization with derived initial affect. All Opinion mutations route through `get_or_init_opinion(npc, subject_id)` which returns an existing Opinion or constructs one with derived initial values.

**Patch.**

```
PATCH 3.4 — §2.5 Opinions (insert new helper)

INSERT at end of §2.5:

#### 2.5.1 Opinion Initialization

function get_or_init_opinion(npc, subject_id):
    if subject_id in npc.opinions:
        return npc.opinions[subject_id]
    npc.opinions[subject_id] = Opinion(
        affect_axis=derive_initial_affect(npc, subject_id),
        confidence=1,                     # newly formed
        evidence_memory_refs=[],
        last_updated=current_season,
    )
    return npc.opinions[subject_id]

function derive_initial_affect(npc, subject_id):
    subject = lookup_npc(subject_id)
    base = 0
    
    # Conviction alignment baseline
    if subject.conviction_primary == npc.conviction_primary:
        base += 1
    elif (npc.conviction_primary, subject.conviction_primary) in OPPOSITIONAL_CONVICTION_PAIRS:
        base -= 1
    
    # Faction alignment
    if subject.faction == npc.faction:
        base += 1
    elif npc.faction.is_hostile_to(subject.faction):
        base -= 1
    
    # Standing differential — modest deference toward higher Standing within shared faction
    if subject.faction == npc.faction and subject.standing > npc.standing + 1:
        base += 0  # institutional deference encoded elsewhere; no Opinion bias here
    
    return clamp(base, -3, +3)

INSERT in §6.2 Procedure D, before drift loop:

    # Ensure Opinion exists for subject (lazy init)
    opinion = get_or_init_opinion(npc, memory.subject_npc_id)

INSERT in §6.2 Procedure E, before apply_drift calls:

    op_a_to_b = get_or_init_opinion(npc_a, npc_b.id)
    op_b_to_a = get_or_init_opinion(npc_b, npc_a.id)
    apply_drift(op_a_to_b, interaction)
    apply_drift(op_b_to_a, interaction)
```

**Rationale.** Lazy init handles first-contact gracefully. Derived initial affect captures the realistic prior: NPCs of shared Conviction or shared faction start with mild positive Opinion; NPCs of opposed Conviction or hostile factions start with mild negative. Range clamped to [-3,+3] per the existing hard bound. Confidence starts at 1 (low — single piece of evidence will easily move the Opinion).

---

### 3.5 — ST-19-A · Grieving handling in DA Proposal Phase

**Issue.** §6.1 Mood table specifies "Grieving: Major actions auto-fail without Spirit check Ob 1; minor actions standard." But §6.2 DA Proposal Phase pseudocode does not branch on Grieving.

**Resolution.** Add Grieving-mood gating to DA Proposal Phase: Grieving NPCs auto-fail proposal unless they pass Spirit Ob 1, and pass at +1 Ob.

**Patch.**

```
PATCH 3.5 — §6.2 Domain Action Proposal Phase

LOCATE: "if npc.mood == Distracted and npc.personality.institutional_deference >= 1:"

INSERT before this line:

    # Grieving: auto-fails major Domain Action proposal without Spirit Ob 1
    if npc.mood == Grieving:
        if not npc.spirit_check(ob=1):
            continue  # Grieving NPC cannot propose this Accounting
        proposal_modifier += 1  # passes but +1 Ob
```

**Rationale.** Aligns DA Proposal Phase with the §6.1 Mood table specification. Without this gate, Grieving NPCs would still propose at standard Ob, contradicting the Mood spec. Spirit Ob 1 is permissive (Spirit pool typically 3-6, Ob 1 succeeds easily) so Grieving NPCs can sometimes still propose — they just have a higher floor.

---

### 3.6 — S-LAT-A · Knot auto-surfacing rephrase

**Issue.** §6.2 Procedure E "Knot integration" specifies "One Concern about each Knot partner is automatically surfaced per season (no Read action required)" — contradicts the opacity principle (NPCs share by choice through scenes).

**Resolution.** Replace direct surfacing with mandatory Priority 2 Outreach scene generation. Mechanically equivalent (player learns the Concern); philosophically consistent (NPC chooses to share via scene dialogue).

**Patch.**

```
PATCH 3.6 — §6.2 Procedure E (Knot integration paragraph)

REPLACE the entire Knot integration paragraph with:

    Knot integration: Knot partners have guaranteed access to each other's 
    Observable behavior (100% ambient probability when in same settlement). 
    For each Knot partner with an active Concern of salience ≥ 2 about the 
    player, a Priority 2 Outreach scene is generated for the player's next 
    Scene Slate. The Concern is conveyed through partner-driven dialogue in 
    that scene. The player learns of the Concern by attending the scene; 
    NPCs share by choice through scenes (opacity principle preserved).
```

**Rationale.** Mechanically identical — player still learns about the Concern within one Accounting. The salience ≥ 2 threshold prevents trivial Concerns from clogging the Scene Slate. Priority 2 (mandatory, scheduled) ensures the player sees the scene without being able to skip it indefinitely. Routing through Scene Slate consolidates information delivery into one channel and preserves the engine's narrative-through-scene model.

---

### 3.7 — N-33-A · `scars_total` / `scars_conviction` split

**Issue.** §2.2 has a single `scars` field. §3.2 uses it to gate primary→secondary armature shift. §5.3 uses it (implicitly via `total_inner_circle_scars`) for institutional_stability. But peripheral Scars (Belief revisions on non-primary-Conviction-engaging Beliefs) should not shift core armature, only fracture institutional_stability.

**Resolution.** Split into two fields. `scars_total` counts all Belief revisions; `scars_conviction` counts only those engaging conviction_primary domain.

**Patch.**

```
PATCH 3.7 — §2.2 State

REPLACE: 
    scars: count of revised Beliefs (existing)

WITH:
    scars_total: count of all revised Beliefs (existing system, renamed)
    scars_conviction: count of revised Beliefs that engaged conviction_primary 
                      domains (subset of scars_total)

UPDATE §3.2 modify_by_scar_count to use scars_conviction (not scars_total) — 
only Conviction-engaging Scars shift the armature toward secondary.

UPDATE §5.3 institutional_stability formula to use scars_total — institutional 
weight responds to all fracturing, not only Conviction-engaging.

ADD note at §3.5 Belief Revision Paths:

    When a Belief is revised (via Path A or Path B), check whether the Belief's 
    domain engages npc.conviction_primary. If yes, increment both scars_total and 
    scars_conviction. If no, increment only scars_total.
```

**Rationale.** Resolves the design issue in N-33-A: a player imposing a peripheral Belief revision via Total Victory Contest should not flip the NPC's worldview (which would require Conviction-engaging revision) but should still register as institutional fracture (the NPC's coherence is reduced). The split correctly attributes weight: armature is sensitive only to Conviction-engaging Scars; faction stability is sensitive to all Scars.

**Authoring impact.** Each existing Belief in the world needs a tag indicating which Convictions it engages. ~30-50 Beliefs × Conviction-engagement tags = ~30-50 small annotations. Defaults to "engages_primary_only" if author omits.

---

### 3.8 — E-37-A · Vindicated and Resolved Mood triggers

**Issue.** §6.1 Mood table includes Vindicated and Resolved but examples list only the "set" Moods (Confident, Anxious, etc.), not the conditions that trigger Vindicated or Resolved.

**Resolution.** Define triggers explicitly.

**Patch.**

```
PATCH 3.8 — §6.1 Mood transition examples

EXTEND the examples list with:

- Vindicated: NPC's previously-stated position is publicly confirmed by outcome.
    Trigger conditions (any of):
      (a) NPC won a Total Victory Social Contest as defender within last 2 seasons.
      (b) A Project completion this season reflects NPC's earlier predicted outcome 
          (e.g., NPC publicly opposed the project; project failed).
      (c) A Domain Action that NPC publicly advocated succeeded with positive 
          consequence visible this season.
    Duration: 2 seasons. -1 Ob to action aligned with vindication's themes.

- Resolved: NPC's Concern resolution produced a clear, satisfying answer that 
  refines or confirms existing Belief (no Scar produced).
    Trigger conditions: 
      Concern resolves via resolve_concern() with a high-salience matching Memory 
      (≥4) AND resolution does NOT produce a Scar (resolution.causes_belief_revision 
      is False, OR contradiction_strength is "weak").
    Duration: 1-2 seasons (1 if salience 4 Memory; 2 if salience 5).
    Effect: -1 Ob to action consistent with resolution; +1 Ob to inconsistent.

(Procedure D and B-Resolution check these conditions and call update_mood_real_time() 
when applicable.)
```

**Rationale.** Vindicated rewards NPCs for advocating positions that play out correctly; Resolved rewards Concern processing that confirms existing convictions. Both produce mood durations and Ob effects already specified in §6.1 — only the trigger conditions were missing.

---

### 3.9 — N-35-A · Population Disposition update trigger

**Issue.** §5.1 Settlement Meta-Armature uses `population_disposition_weight: 0.1` and references `Statistical mean Disposition with controlling faction`. No procedure updates this value, so it is static across the campaign.

**Resolution.** Recompute population_disposition each Accounting from settlement Order/Prosperity statistics plus an event-decay term.

**Patch.**

```
PATCH 3.9 — §5.1 Settlement Meta-Armature

INSERT new sub-paragraph after population_disposition_weight definition:

    population_disposition recalculation (each Accounting):
    
    population_disposition[settlement, faction] = clamp(
        0.4 * normalized_order(settlement) +
        0.4 * normalized_prosperity(settlement) +
        0.2 * recent_event_delta(settlement, faction, seasons=4),
        -3, +5
    )
    
    where:
      normalized_order maps settlement.order [0, 10] to [-2, +2]
      normalized_prosperity maps settlement.prosperity [0, 10] to [-2, +2]
      recent_event_delta = sum of Δ-Disposition events this faction caused this 
        settlement in last 4 seasons, exponentially decayed (×0.7^seasons_ago).
```

**Rationale.** Order and Prosperity are existing settlement stats that respond to faction governance quality. Mapping them to population sentiment is a natural derivation. The event-delta term lets faction-caused disasters or windfalls move sentiment without requiring per-population per-event tracking. Range clamped per existing Disposition spec.

---

### 3.10 — R-39-A · Outreach as available, not mandatory

**Issue.** Mid-campaign, all five player Scene Slate slots may fill with NPC-driven mandatory Priority 1-3 content (Concern-driven Outreach), leaving zero discretionary scene actions. This breaks the "player decisions feedback loop" intent.

**Resolution.** Concern-driven Outreach defaults to Priority 3 **available** (player MAY take, decays if skipped). Only escalates to Priority 2 mandatory when Concern reaches salience 5 AND ttl ≤ 1 (about to force-resolve).

**Patch.**

```
PATCH 3.10 — §7.6 NPC Outreach Generation

REPLACE the existing description with:

Concern-driven Outreach: NPCs with active Concerns about the player generate 
Scene Slate entries. Default Priority 3 — AVAILABLE (the player may choose to 
attend; if skipped, the scene does not consume a slot, and the underlying Concern 
continues its normal decay).

Mandatory escalation: When a Concern reaches salience 5 AND ttl ≤ 1 (one season 
from forced resolution), the Outreach scene upgrades to Priority 2 mandatory for 
that Accounting only. After force-resolution, the scene drops from Slate.

Tone: Scene tone reflects current Mood (Anxious Concerns yield Outreach with 
worried tone; Vindicated Concerns yield assertive tone).

Note: The mandatory upgrade applies only to Concerns about the player. NPC-NPC 
Concerns that surface via Knot (PATCH 3.6) follow their own Priority 2 rules and 
are not subject to this gate.
```

**Rationale.** Preserves NPC autonomy (NPCs still generate Concerns and Outreach proactively) while restoring player agency (the player can decline). Mandatory escalation ensures urgent/important matters do reach the player; non-urgent matters become available content the player can engage with on their own initiative. Aligns with the "intent of game" line in project README.

---

### 3.11 — R-40-A · NPC Standing recalculation

**Issue.** Standing weights NPC influence in Faction Meta-Armature (§5.3). Standing values never change during a campaign — a Marshal who fails every Project remains S6.

**Resolution.** Recalculate Standing at each Campaign Year boundary based on Project completion/failure, DA proposal record, and Conviction Scars.

**Patch.**

```
PATCH 3.11 — §8 Integration with Existing Systems

UPDATE the "Standing ladder" row:

    Augmented. Promotion events generate Memories and Opinion shifts. Player 
    at Standing 5+ enters Faction Meta-Armature aggregate. **Standing recalculates 
    each Campaign Year based on prior-year activity (see §8.1).**

INSERT new subsection §8.1:

#### 8.1 NPC Standing Recalculation (Campaign Year boundary)

At end of each Campaign Year (4 Accountings = 1 calendar year), each Active NPC's 
Standing is recalculated:

    Δ_standing = (
        +0.5 × completed_projects_this_year
        -0.5 × failed_projects_this_year
        +0.25 × successful_da_proposals_this_year (max +1.0/year)
        -0.25 × failed_da_proposals_this_year (max -1.0/year)
        -0.5 × public_conviction_scars_this_year
    )
    Δ_standing = clamp(Δ_standing, -2, +2)
    npc.standing = round(clamp(npc.standing + Δ_standing, 3, 7))

If npc.standing drops below 3 (rounded), NPC exits inner circle (becomes peripheral). 
If npc.standing rises above 7, capped at 7.

A Standing change triggers an event (event_type: "standing_change") which propagates 
through the standard Event Impact Matrix; inner-circle NPCs receive Memories about 
the rising/falling colleague.
```

**Rationale.** Realizes the design intent that "makes players feel like they are impacting the game world": player actions that cause NPC failure (or success) are reflected in NPC Standing. A failing Marshal loses institutional weight, reducing his armature's contribution to Crown's Faction Meta-Armature; a rising Bishop gains it. This dynamism is critical for emergent political shifts. Annual cadence (not per-Accounting) prevents Standing from being whippy; the changes accumulate and resolve at narrative milestones.

**Knock-on.** Faction Meta-Armature recomputation now reflects shifted Standing weights. Inner-circle composition can change over campaign — a once-S5 NPC may drop to S2 (peripheral); a once-S4 may rise to S5 (inner circle). This is intended.

---

### 3.12 — S-44-A · Settlement Signal scope

**Issue.** §5.2 amplifies all Memories by `npc.local_disposition_with_player`, even Memories that don't involve the player.

**Resolution.** Restrict the player-Disposition amplification to Memories that involve the player as participant. Already addressed in PATCH 2.5 (within compute_settlement_signal). No additional patch.

```
PATCH 3.12 — already applied via PATCH 2.5

(See PATCH 2.5 for the per-Memory weight calculation that gates 
local_disposition_with_player on memory.involves_player.)
```

**Rationale.** Prevents settlement Signals from being secretly biased by the player's relationship with one Passive NPC. Memories about other actors (NPC-NPC events, faction events) get standard salience-based weight; Memories where the player participated get the Disposition-boosted weight, modeling the realistic "this Passive NPC heard about the player from someone whose opinion matters to them."

---

### 3.13 — S-46-A · Replacement Project derivation

**Issue.** §6.2 Procedure C completion calls `generate_new_project(npc)`; never specified.

**Resolution.** Two-tier derivation: (1) authored project queue if available, (2) Conviction-aligned procedurally generated Project. The second tier reuses the DOMAIN_ARMATURE_ALIGNMENT table from PATCH 2.1.

**Patch.**

```
PATCH 3.13 — §6.2 Procedure C

INSERT after the apply_project_legacy block (now Memory-based per PATCH 1.5):

function generate_new_project(npc):
    # Tier 1 — pre-authored project queue
    if npc.authored_project_queue and len(npc.authored_project_queue) > 0:
        return npc.authored_project_queue.pop(0)
    
    # Tier 2 — Conviction-aligned procedural generation
    domain = sample_domain_weighted_by_conviction(npc.conviction_primary)
    horizon = weighted_choice(["short", "medium", "long"], [0.4, 0.4, 0.2])
    
    project = Project(
        goal=generate_goal_from_template(domain, npc),
        progress=0,
        progress_status="new",
        blockers=[],
        accelerators=[],
        horizon=horizon,
        project_domain=domain,
        visible_actions=lookup_visible_actions_template(domain),
        completion_effect=standard_effect_for(domain, npc),
        failure_effect=standard_effect_for_failure(domain, npc),
        domain_action_required=domain_action_required_for(domain),
        seasons_stalled=0,
    )
    return project

function sample_domain_weighted_by_conviction(conviction):
    # Reuse DOMAIN_ARMATURE_ALIGNMENT table from §6.2 / PATCH 2.1.
    # Sample domain weighted by alignment score for the NPC's primary Conviction.
    weights = {d: DOMAIN_ARMATURE_ALIGNMENT[d][conviction] for d in DOMAINS}
    return weighted_select(list(weights.keys()), list(weights.values()))

UPDATE §10 Content Authoring Requirements:

    | Authored project queue per Active NPC | 35-105 | 1-3 follow-ups per NPC, optional |
    | Goal text templates per domain | ~30 | ~5 templates × 6 domains |
    | visible_actions templates per domain | ~80 | 10 actions × 8 domains (PATCH 3.14) |
```

**Rationale.** Tier 1 honors authored content where it exists (specific NPCs may have multi-Project arcs the designer wants preserved); Tier 2 ensures the spec is robust without that content (any NPC can always generate a fresh Project on completion). Conviction-aligned domain selection produces character-consistent follow-up Projects: a Faith NPC tends to start theological projects, a Reason NPC tends toward scholarly. Horizon weighting (40/40/20 short/medium/long) keeps the project pipeline diverse — not all auto-generated Projects are short-term.

---

### 3.14 — NS-49-A/B · `visible_actions` templates for procedurally-generated Projects

**Issue.** Procedurally-generated Projects (PATCH 3.13) have no `visible_actions` data, producing null Observable Behavior surface.

**Resolution.** Author 8-12 visible_actions templates per Project domain. `lookup_visible_actions_template(domain)` returns the templates list.

**Patch.**

```
PATCH 3.14 — §10 + new content authoring requirement

ADD to §10 Content Authoring Requirements:

    | visible_actions templates per domain | ~80 | 10 actions × 8 domains |

CONTENT specification (to be authored separately, in params/visible_actions.md):

    For each Project domain (military, theological, scholarly, intelligence, 
    economic, diplomatic, personal_courtship, personal_legacy):
      
      Author 8-12 visible_actions strings, each describing a domain-appropriate 
      action observable to outside parties.
    
    Example (military domain):
      "drilling troops on the parade ground"
      "inspecting fortifications"
      "convening officer council"
      "reviewing scouting reports"
      "training with weapons master"
      "writing letters to allied commanders"
      "examining recruit rolls"
      "demonstrating swordwork to junior officers"
      "consulting with engineer over siegeworks"
      "interviewing veteran for command appointment"
    
    (Similar 8-12 entry lists for each remaining domain.)

INSERT in §6.2 Procedure C / generate_new_project:

    # Look up template; sample one as Project's representative visible_action
    visible_actions_pool = VISIBLE_ACTIONS_TEMPLATES[domain]
    project.visible_actions = [random.choice(visible_actions_pool)]
    project.visible_actions_pool = visible_actions_pool  # for varying observation

INSERT in §7.2 Observable Behavior Surfacing:

    Each Read or Surveil that surfaces a Project's visible_action samples a fresh 
    string from project.visible_actions_pool (varying observation across encounters; 
    the NPC is not always doing literally the same activity).
```

**Rationale.** Gives every procedurally-generated Project a content surface. Rotating display through the pool produces realistic variation: the player surveilling the Marshal across multiple Accountings sees "drilling troops" then "inspecting fortifications" then "consulting with engineer" — all consistent with a military-domain Project but varied. Authoring scope ~80 entries; modest.

---

### 3.15 — R-42-A · Passive NPC Memory replacement rules

**Issue.** §1 specifies Passive NPCs hold 3 Memories; §2.6 Memory replacement rules are written for the 10-Memory Active cap and may not transfer cleanly.

**Resolution.** Specify Passive Memory replacement explicitly: same rules (lowest-salience drop or merge into similar) but applied to the 3-Memory cap.

**Patch.**

```
PATCH 3.15 — §1 NPC Tier Stratification (or §2.6 Memories)

ADD note at end of §2.6:

    For Passive NPCs (3-Memory cap), the same replacement rules apply at the lower 
    cap. When a new Memory would exceed cap:
      1. If a similar-tag existing Memory exists with same affect-direction, merge 
         (collapse "another disappointment from the Crown" — increment 
         reference_count; new Memory's salience replaces if higher).
      2. Otherwise, drop the lowest-salience Memory.
      3. Tie-break: drop the older Memory (timestamp comparison).
    
    Passive Memories also obey the salience-floor mechanic from §2.6.
```

**Rationale.** Same logic, smaller cap. Tie-break by age handles equal-salience ties (newer events feel more relevant; older Memory drops). The merge path is critical for Passive NPCs because the 3-Memory cap fills quickly — without merging, every Accounting could swap Memories, producing flicker. Merging preserves cumulative pattern recognition.

---


## §4 PRIORITY-3 RESOLUTIONS (implementation-time, brief)

These are addressable when implementation begins. Each is a stub with the proposed answer; full patch text is deferred to the implementation revision pass.

### 4.1 — Tie-breaking and ordering (ST-13-A/B, ST-14-A/B, ST-17-A, ST-18-A, ST-30-A)

- **ST-13-A** Memory replacement tie at equal salience: drop the older Memory (lower timestamp). If timestamps equal: drop the one with lower reference_count.
- **ST-13-B** Memory merge trigger: merge two Memories when (a) same event_type, (b) same affect_direction, (c) timestamps within 4 seasons, (d) overlapping participants set. Merge increments reference_count and adopts the higher salience.
- **ST-14-A** Concern cap tie at equal salience: drop the Concern with lower ttl (closer to forced resolution stays — the player has invested more in it). If ttl equal: drop the older Concern.
- **ST-14-B** Concern cap transient overflow under simultaneous events: if multiple Concerns generated this Accounting push above cap, queue all generated, then apply replacement rule once (not per-Concern). This avoids cascading drops.
- **ST-17-A** Path A reset via `contested_this_season` flag: add `contested_this_season: bool` to each Belief. Set on Path A revision; reset at start of next Accounting. Procedure B-Resolution checks this flag before applying Path B Memory accumulation; if true, accumulated Memory contradiction count resets.
- **ST-18-A** Procedure B ordering of Mood-set events: Mood is set in real-time (§6.1) at event resolution, before Accounting. So when Procedure B runs, Mood is already current. No procedural reordering needed; document as comment in spec.
- **ST-30-A** Witness Mode NPC uniqueness: Witness Mode picks at most one scene per NPC per Accounting. Tracking set: `seen_npcs_this_accounting`; deduplicate before applying the 3-result cap.

### 4.2 — Threshold definitions (ST-22-A, ST-29-A/B, N-LAT-A, N-LAT-B, E-47-A/B, N-34-A)

- **ST-22-A** Major external crisis threshold: an event_type with `peninsula` in its scale_signature AND magnitude ≥ 3 AND time_horizon ∈ {immediate, near}. This blocks Anomaly Detection (per §5.4) for one Accounting.
- **ST-29-A** Loyalty Cover decay rate: `loyalty_cover_bonus` decays −1 per Accounting unless renewed by qualifying signal that season. Floor at 0.
- **ST-29-B** Loyalty Cover base value: `player.cover` is unchanged baseline cover stat (existing system). loyalty_cover_bonus is a stacking modifier above that base.
- **N-LAT-A** DA failure Concern salience: `concern.salience = 3 + (project.horizon == long ? 1 : 0)` — failure on a long-horizon project produces salience 4 (heavier weight; long-investment loss).
- **N-LAT-B** Priority 4 Scene Slate trigger: NPC-NPC interaction outcome generates Priority 4 scene if `cumulative_drift > 0.8` AND at least one participant has Disposition with player ≥ +2. This bounds Priority 4 generation to scenes with player-relevant context.
- **E-47-A** Settlement Signal window magic: replace fixed 2-season window with `window = 2 + (settlement.event_density < 1.0 ? 1 : 0)` — quiet settlements get a 3-season window to accumulate enough Memories.
- **E-47-B** Density-aware window: settlement.event_density = events_in_last_4_seasons / 4. Threshold tuned per playtest.
- **N-34-A** Horizon-proportional stall threshold: replace fixed 8-season stall with `stall_threshold = 4 + 2*horizon_index` where horizon_index ∈ {0,1,2} for short/medium/long. Short Projects fail in 4 stalled seasons; long Projects in 8.

### 4.3 — Search and gating (ST-27-A, ST-28-A, ST-31-A, N-HORIZ-A)

- **ST-27-A** Project failure obstructor tracking: maintain `project.opposers: list of NPC ids` populated when other NPCs publicly oppose the Project (DA proposal +1 Ob contribution per E-36-A select_proposal scoring; Outreach scenes where opposition is voiced). On failure, all opposers are tagged in `project.obstructors` for Memory generation per PATCH 1.5.
- **ST-28-A** Knowledge in Concern resolution: extend `resolve_concern.matches` search to include Knowledge entries: a Knowledge fact whose `fact_tag` matches a `concern.seeking` tag is a candidate match with weight = knowledge.salience × 0.7 (slight downweight relative to direct Memory match).
- **ST-31-A** Knowledge sharing sensitivity gate: Procedure E knowledge sharing requires `Disposition_a_b ≥ knowledge.sensitivity`. Sensitivity 1 → freely shared; 5 → only at Trusting+Knot relationships. Default sensitivity 2 unless authored.
- **N-HORIZ-A** Seek-tag vocabulary: enumerated tag set authored once in `params/political_dynamics_tags.md` covering ~30 tag types (event categories, conviction domains, faction identifiers). Concerns and Memories share the vocabulary; matching is exact-tag or category-membership.

### 4.4 — Cascade and propagation (ST-21-A, ST-21-B, E-VERT-A, S-DIAG-A, S-VERT-A, S-43-A)

- **ST-21-A** Downward propagation from peninsula scale: peninsula-scale events propagate to factions at full salience (no decay) but to settlements at salience × 0.7 and to NPCs at salience × 0.5 (two boundaries crossed). Faction-scale events propagate downward symmetrically.
- **ST-21-B** scale_signature split-by-scale: an event's scale_signature is a list of scales it has consequences at; each scale processes independently. Per-scale signal magnitude is event.magnitude (not derived from highest-scale).
- **E-VERT-A / S-DIAG-A** Salience cliff at 4-vs-5 binary: introduce `propagation_weight` per event-type (default 1.0; 1.5 for personally-significant low-salience events like Knot interactions, deaths, betrayals). Multiplied into salience before cascade decay. This softens the 4/5 cliff: a salience-4 personal-significance event with weight 1.5 now propagates at 6 → 4.2 (above 2.0 threshold), reaching faction influence.
- **S-VERT-A** Settlement Signal 2-season lag: structural to the design (Settlement Signal aggregates Memories, which take 1 Accounting to form). Document as expected; do not patch. Player-facing: surfaced as "the city is starting to talk about X" with appropriate temporal hedging in narration.
- **S-43-A** Priority Knowledge fast-path (salience 5): when a Knowledge fact at salience 5 is acquired, generate the Concern this Accounting (not next), bypassing the standard 1-season lag. Implementation: Knowledge acquisition at salience 5 triggers immediate Procedure-B subroutine call in same season.

### 4.5 — Documentation gaps (ST-25-C, ST-26-B, S-45-A/B, N-DIAG-B, R-LAT-A, R-DIAG-A)

- **ST-25-C** "Disposition-with-leader" referent: clarify in §5.4 — refers to NPC's Disposition with their faction's leader (e.g., Marshal's Disposition with the Crown). Add explicit definition.
- **ST-26-B** institutional_stability regeneration: as `total_inner_circle_scars` decreases (NPCs leaving inner circle, replaced by un-scarred NPCs), institutional_stability automatically rises. Document as inherent in the formula.
- **S-45-A** +3 Disposition no benefit over +2 in Read Action: redesign Disposition +3+ to grant "behavior-context label" (one-sentence interpretation of why the visible_action is being taken). Adds a meaningful tier between +2 (label only) and +3 (label + context).
- **S-45-B** Read/Outreach two-system documentation: add explicit subsection to §7 noting that Read is player-initiated structured-information access; Outreach is NPC-initiated narrative-information delivery. Both are valid information channels with different surface area.
- **N-DIAG-B** Exposure + Anomaly coordination: add coordination check — if Exposure detection fires AND Anomaly detection fires same season for the same player target, only Exposure produces the Loyalty Interview cycle (Anomaly is suppressed; Exposure is the more specific signal).
- **R-LAT-A** Cross-system chain gated by uncontrollable conditions: document as design tradeoff in §11 (some long-form strategies are intentionally luck-dependent; this is the cost of multi-system depth). No mechanical patch.
- **R-DIAG-A** 6-season investment threshold for max faction-shift: under the §3.11 (NPC Standing recalc) + Faction Meta-Armature aggregation, sustained 6-season investment (24 Accountings) yields a measured shift of ~1-2 Standing points across 2-3 inner-circle NPCs. Document the expected magnitude in §10 simulation tests.

### 4.6 — Friction items (N-TOP-A, N-BOT-A, N-BOT-B, E-LAT-A, R-BOT-A, N-HORIZ-B)

- **N-TOP-A** Settlement layer dependency on Passive NPC count: PATCH 2.5 adds the empty-Passive-NPC fallback (governor-only Signal at half weight). Mark in §5.1 that settlements with fewer than 3 Passive NPCs produce reduced-salience Signals.
- **N-BOT-A** `backstory_tags` consumption: tags are referenced by Concern generation seeking-tag matching (an NPC with `lost-sibling-eshlund` backstory tag generates higher-salience Concerns about events involving Eshlund). Add explicit consumption: `salience += 1 if any backstory_tag matches event.tags`. Without this consumption, the field can be cut at content-authoring stage to save ~210 entries.
- **N-BOT-B** `certainty` / `ts` cross-system orphans: `certainty` is consumed by Belief revision (high certainty = harder to revise — extends calcification timer). `ts` (Thread Sensitivity) is consumed by other-system mechanics (existing). Document scope in §2.2 to remove ambiguity.
- **E-LAT-A** Scene Slate scattered hooks: refactor four scattered hook points (NPC Outreach, Knot integration, Crisis priority, Witness Mode) into one `PoliticalSlate` interface that returns a list of (priority, scene, source) tuples each Accounting. Mechanically equivalent; cleaner abstraction.
- **R-BOT-A** Personality → armature modifier table: author 12 entries (4 personality dimensions × 3 armature dimensions), each specifying how a +2 personality value modifies armature option weights. Example: `intellectual_rigor=+2` adds +0.1 to mechanism.calculation, +0.05 to mechanism.error, -0.05 to mechanism.social_pressure. Authoring task added to §10.
- **N-HORIZ-B** Gossip mechanical input: gossip currently is purely player-informing. Proposal: gossip propagating between NPCs adds a low-salience Memory to recipient NPC ("I heard from X that Y did Z"). Memory salience = original salience × 0.5, capped at 2. This integrates gossip as a Knowledge-mediated Memory channel.

### 4.7 — Items resolved by other patches (cross-references)

- **R-VERT-A** Personal → faction insignificance: addressed by PATCH 4.4 (E-VERT-A propagation_weight) + PATCH 3.11 (NPC Standing recalc surfaces personal investment).
- **S-HORIZ-B** Procedure E lag: marked acceptable in doc 16; document as expected behavior.
- **ST-19-B** Project stall on Grieving: PATCH 3.5 covers DA Proposal; Procedure C already pauses new Projects on Grieving. Document the cumulative effect.

---

## §5 FEATURED-BEHAVIOR ITEMS (document as designed; no spec change)

These are correct emergent behaviors that the test process flagged for clarity. Each gets a dedicated §3.5.X-style explanatory subsection in doc 12 to mark them as features rather than gaps.

### 5.1 — RS-50-A · Post-Contest Belief Recovery Arc

When a Belief is imposed on an NPC via Path A (Total Victory Social Contest), the NPC's armature continues to interpret subsequent events. If those interpretations contradict the imposed Belief, Path B accumulation gradually erodes it. Without continuous reinforcement (the player attending Outreach scenes that re-engage the Belief; further Contests; aligned Project completions), an imposed Belief recovers toward the NPC's Conviction-authentic position over 4-8 seasons.

This is the system working as designed. **Player implication:** imposed Beliefs are unstable; politically-shaped NPCs require ongoing investment. Document in §3.5 (Belief Revision Paths) as a featured dynamic.

### 5.2 — ST-16-A · Permanent Salience-5 Founding Memory

A Memory at salience 5 with reference_count ≥ 10 has salience_floor of 5 (cannot decay below maximum). This produces "founding" Memories — unforgettable shared events that anchor an Opinion permanently. Examples: a Knot partnership formed over a shared crisis; a betrayal that cannot be forgiven.

This is the system working as designed. Document in §2.6 as the reference-count → salience-floor mechanism's intended outcome.

### 5.3 — E-DIAG-A · Diagonal Chain Legibility

Long event chains (e.g., personal event → Settlement Signal → faction Concern → Domain Action shift → settlement governance change) are legible only to heavily-invested players who track multiple systems. The full causal chain is not surfaced in any one place; the player must connect the dots from disparate observations.

This is intentional. Players with shallow engagement see surface effects; players with deep engagement see causal architecture. Document as a known tradeoff in §11.

### 5.4 — N-DIAG-A · Standing 5 Milestone Visibility

When the player crosses Standing 5 in a faction, they enter the Faction Meta-Armature aggregate (§5.3). This event is currently invisible to the player. **Resolution:** generate a Priority 2 Outreach scene on that Accounting from the faction leader: "You've earned a place at this council." Scene narration explicitly describes the player's now-counted vote in faction interpretation.

This is a documentation/scene-trigger addition, not a mechanical change. Add to scene authoring requirements.

---

## §6 ITEMS REQUIRING JORDAN DECISION

These cannot be resolved without a design call. Each presents the question, options, and provides a default recommendation if expedient.

### 6.1 — E-38-A/B · `symbolic_effects` and the 210-entry resonance table

**Question.** The Conviction × event-type symbolic resonance table (210 entries) is consumed by no procedure. Either define consumption or cut the table.

**Option A (KEEP + DEFINE):** Use symbolic_effects as Concern salience modifier in Procedure B. `aligned` resonance: -1 salience on Concern generation (event affirms NPC's frame; less alarming). `contradicted`: +1 salience (event challenges frame; more alarming). `neutral`: no modifier.

  - Authoring cost: 210 entries (already partially specified; some still to author).
  - Mechanical impact: integrates the table with Concern salience, justifying the authoring investment. Without this, the table is mechanically inert.

**Option B (CUT):** Remove `symbolic_effects` from EventImpact. Save ~210 authoring entries. The Conviction × event signal is captured indirectly through armature interpretation: a Faith-weighted NPC will already interpret Faith-contradicting events as higher-salience Concerns through the `armature × event.active_dimensions` matching path.

  - Authoring savings: ~210 entries.
  - Mechanical impact: minimal (the indirect path covers most of the signal). Slight loss of fine-grained control over Concern salience.

**Default recommendation if no decision:** Option A. The table partially exists already; integrating it is a small marginal cost compared to redesigning around its absence. The salience modifier provides explicit author control over Concern intensity per Conviction-event pairing.

**Stakes.** Highest single design decision in this batch. Affects ~210 authoring entries.

### 6.2 — E-TOP-A · Opaque-by-design vs Legible-by-design

**Question.** The system currently produces rich internal NPC state (armatures, Concerns, Beliefs) but exposes only narrow surfaces (Read, Outreach, Witness, Surveil). Should the design lean toward more opacity (NPC inner state remains hidden, narrative emerges through surfaces) or more legibility (UI exposes NPC interpretive frames more directly)?

**Option A (OPAQUE):** Keep current design. Player infers NPC state through surfaces. Discovery is part of gameplay. May frustrate strategic players who want full state visibility.

**Option B (LEGIBLE):** Add a "Read Deep" action (cost: 1 scene action + Disposition ≥ +3) that surfaces full armature interpretation of recent events. Reduces inference burden; risks making NPCs feel mechanical rather than mysterious.

**Stakes.** Affects player UX significantly. No mechanical patch is correct without this decision.

### 6.3 — ST-31-B · NPC self-monitoring on sensitive disclosure

**Question.** When an NPC shares sensitive Knowledge in Procedure E (passes the sensitivity gate per ST-31-A), does the NPC generate a follow-up Concern about whether they should have shared?

**Option A:** Yes — generate Concern("Did I share too much with X?"); produces Disposition-with-X drift downward over subsequent Accountings as the NPC's anxiety processes.

**Option B:** No — sharing decisions are atomic; once shared, the NPC moves on. Simpler; lighter computational load.

**Default:** Option B. NPC self-monitoring adds Concern volume without clear narrative payoff for most cases.

### 6.4 — R-41-A · Crisis masking persistence counter

**Question.** Players can suppress Anomaly Detection by manufacturing major external crises (which override the detection per ST-22-A threshold). Should the engine maintain a persistence counter that detects pattern of crisis-masking?

**Option A:** Add `consecutive_crisis_masked_seasons` counter; if ≥ 3, faction Anomaly Detection fires anyway with note "Despite the crises, something else is wrong."

**Option B:** Accept crisis-masking as legitimate adversarial play. Player who can engineer 3 consecutive crises has earned the suppression.

**Default:** Option B. Adversarial player creativity is part of the design's emergent space.

### 6.5 — Carryover items from prior sessions

These were flagged in earlier sessions and remain unresolved:

- **Intelligence stat as 6th faction stat** — unblocks Spy Ob, Varfell Path A scoring.
- **LICENSE / GOV-08 decision** — repository governance.
- **§1.1 Knot Formation During Play** — ongoing knot lifecycle clarification.
- **§1.2 Accord Propagation to Settlement Order** — settlement-stat update on faction-level accord ratification.

These are not in scope for this revisions doc but must be tracked.

---

## §7 APPLICATION CHECKLIST (for v1.1 doc 12 revision session)

When applying these revisions to `12_development_specification.md` to produce v1.1:

1. Apply PATCH 1.4 (Procedure B Resolution → Memory only).
2. Apply PATCH 1.5 (Procedure C Project Completion → Memories only).
3. Apply PATCH 1.6 (Procedure D banner — single-writer invariant).
4. Apply PATCH 2.1 (select_proposal + DOMAIN_ARMATURE_ALIGNMENT table).
5. Apply PATCH 2.2 (max_scars).
6. Apply PATCH 2.3 (conviction_alignment_multiplier + OPPOSITIONAL pairs).
7. Apply PATCH 2.5 (compute_settlement_signal null guards + per-Memory weight gate from PATCH 3.12).
8. Apply PATCH 2.6 (modify_by_scar_count secondary=None fallback + Armature Confidence).
9. Apply PATCH 2.7 (resonance_lookup category fallback).
10. Apply PATCH 2.8 (compute_armature additive composition + per-dim normalization).
11. Apply PATCH 3.1 (concern_history cooldown + Generation loop with visibility gate).
12. Apply PATCH 3.2 (B.0 Knowledge Decay sub-step).
13. Apply PATCH 3.3 (npc_observes_event helper — co-applied with 3.1).
14. Apply PATCH 3.4 (Opinion lazy initialization + derive_initial_affect).
15. Apply PATCH 3.5 (Grieving in DA Proposal).
16. Apply PATCH 3.6 (Knot integration via Priority 2 Outreach).
17. Apply PATCH 3.7 (scars_total / scars_conviction split).
18. Apply PATCH 3.8 (Vindicated / Resolved Mood triggers).
19. Apply PATCH 3.9 (population_disposition recalculation).
20. Apply PATCH 3.10 (Outreach Priority 3 default + 5-and-ttl-1 escalation).
21. Apply PATCH 3.11 (NPC Standing recalculation §8.1).
22. PATCH 3.12 already applied via PATCH 2.5.
23. Apply PATCH 3.13 (generate_new_project Tier 1+2).
24. Apply PATCH 3.14 (visible_actions templates + Procedure C/§7.2 wiring).
25. Apply PATCH 3.15 (Passive NPC Memory replacement explicit).
26. Apply §4 P3 stubs as documentation-grade additions to relevant sections (lower priority — can land in v1.2).
27. Apply §5 featured-behavior subsections as new explanatory paragraphs in doc 12.
28. Surface §6 Jordan-decision items in §11 OUTSTANDING DESIGN DECISIONS of doc 12 (lift the four new items into that list alongside the existing carryover items).

**Total patches:** 23 primary (P1+P2) + 16 P3 stubs + 4 featured + 5 Jordan flags = 48 distinct doc 12 modifications.

**Editorial ledger entries needed:**
- ED-XXX-revisions-batch-1: PATCH 1.4-1.6 (single-writer Opinion).
- ED-XXX-revisions-batch-2: PATCH 2.1-2.8 (P1 items).
- ED-XXX-revisions-batch-3: PATCH 3.1-3.15 (P2 items).
- ED-XXX-revisions-batch-4: §4 stubs (P3 documentation).
- ED-XXX-revisions-batch-5: §5 featured-behavior documentation.

Patch register entries (PP-XXX) required only for canonical promotion; provisional revisions at this stage are tracked in editorial ledger.

---

## §8 OPEN QUESTIONS FOR FOLLOW-UP

These emerged during resolution authoring and warrant subsequent attention:

1. **DOMAIN_ARMATURE_ALIGNMENT table calibration.** Values in PATCH 2.1 are derived defaults. Playtest may indicate adjustments (e.g., is military really 0.4 for Autonomy, or should it be lower since military is institutional-not-individual?).

2. **OPPOSITIONAL_CONVICTION_PAIRS canonicalization.** PATCH 2.3 lists four pairs. Continuity↔Reason is the least confident; it may be that Continuity↔Equity is more canonical (equity-driven reform vs preserve-the-existing). Worth checking against existing Conviction system canon.

3. **Authoring scope for visible_actions templates** (PATCH 3.14). 80 entries is the proposal; could be 60 (8 per domain) or 96 (12 per domain). Calibrate per playtest of repetition tolerance.

4. **NPC Standing recalc magnitudes** (PATCH 3.11). Values (+0.5 per project completion, etc.) are tentative. Should produce ~1-2 Standing point shifts per campaign year for active NPCs; calibrate after simulation.

5. **Path B Memory threshold** (existing spec: 2 contradicting Memories at salience ≥3). Now that single-writer Opinion model routes more Memories through D (PATCH 1.4-1.6), the effective rate of Memory accumulation may shift. Verify in simulation that 2-Memory threshold still produces appropriate revision frequency.

6. **Concern volume per NPC per Accounting.** With visibility gate (PATCH 3.3), regen cooldown (PATCH 3.1), and Knowledge → Concern path (existing), measure mean Concerns per NPC per Accounting. Target: 0.5-1.5. Above 2 risks Concern thrashing.

7. **Settlement Signal frequency.** With null guards (PATCH 2.5), some settlements will produce no Signal some Accountings. Verify this is acceptable (faction Concern volume from settlements remains adequate to drive faction-scale dynamics).

---

**END OF DOC 17 v1.**

This document specifies 48 distinct revisions to `12_development_specification.md`. Application produces doc 12 v1.1, after which a re-vetting pass (per §13 Promotion Checklist of doc 12) and a follow-up simulation pass should validate the revised spec before further work.
