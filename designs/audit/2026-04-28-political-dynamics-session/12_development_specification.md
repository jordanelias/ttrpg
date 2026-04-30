<!-- [PROVISIONAL: 2026-04-29 v1.2 — development specification, simulation-validated] -->
<!-- STATUS: PROVISIONAL — CURRENT SOURCE OF TRUTH for political dynamics system -->
<!-- POSITION: designs/audit/2026-04-28-political-dynamics-session/12_development_specification.md -->
<!-- SUPERSEDES: stage docs 01-11 (preserved for design history); v1.0→v1.1 superseded 2026-04-29; v1.1→v1.2 superseded 2026-04-29 by simulation-validation revision -->
<!-- REVISIONS APPLIED: 17_specification_revisions.md (26 patches v1.0→v1.1); 21_v1_2_specification_revisions.md (39 patches v1.1→v1.2 resolving simulation-surfaced gaps) -->

# Political Dynamics System: Development Specification (v1.2)

**Status:** PROVISIONAL (development reference — eligible for canonical promotion review per §13)
**Version:** v1.2 (2026-04-29) — 39 patches applied per `21_v1_2_specification_revisions.md` resolving all simulation-surfaced gaps from 8-direction simulation chain (51 scenarios, validation report `19_v1_1_validation_report.md`). Three P1-CRITICAL resolutions: failed_da_proposals strict definition (SIM-B-G8), Settlement-Signal-Concern routing (SIM-C-G6), Knot rupture mechanic (SIM-H-G2). Plus ED-760 stall-escalator + 19 P2 + 16 P3 cleanups. P3 stubs documented in §0.1; §6 Jordan-decision items remain flagged.
**Supersedes:** v1.0 (2026-04-28) → v1.1 (2026-04-29, 26 patches) → v1.2 (2026-04-29, 39 additional patches from simulation validation).
**Audience:** Engine implementation, content authoring, simulation design.

---

## §0.1 v1.2 CHANGE LOG (this version)

39 patches applied 2026-04-29 from `21_v1_2_specification_revisions.md` resolving simulation-surfaced gaps. Patches grouped by priority.

**P1-CRITICAL (§1 of doc 21) — must-resolve-before-canonical:**
- PATCH v1.2-1 — `failed_da_proposals` strict definition (§8.1 Standing recalc; resolves SIM-B-G8).
- PATCH v1.2-2 — Settlement-Signal-Concern three-tier routing (§5.2; resolves SIM-C-G6).
- PATCH v1.2-3 — Knot rupture mechanic full specification (§2.5.2 new + §1.1 featured behavior; resolves SIM-H-G2).

**Recommendation patch (§2 of doc 21):**
- PATCH v1.2-4 — Stall-escalator term in `select_proposal()` (`+0.05 × seasons_stalled`); validated as anti-deadlock + anti-ossification mechanic at scale (per ED-760).

**Priority-2 (§3 of doc 21) — implementation determinism (19 patches):**
- PATCH v1.2-5 through v1.2-23. See doc 21 for full list. Highlights: drift coefficients (v1.2-5), iteration order (v1.2-6), 4th-level tie-break (v1.2-8), Standing-recalc counter state (v1.2-11), Mood-impact on aggregate weighting (v1.2-18), faction succession (v1.2-19), faction-internal coup (v1.2-20), war-state mechanic (v1.2-22), peace treaty (v1.2-23).

**Priority-3 (§4 of doc 21) — minor cleanups (16 patches):**
- PATCH v1.2-24 through v1.2-39. Doc/typo/authoring fixes including N-DIAG-A title rename (v1.2-35), banker's rounding clarification (v1.2-29), confidence boundary standardization (v1.2-26), authored-content scope additions.

Validation evidence base: `19_v1_1_validation_report.md` (consolidates 8-direction simulation chain).

---

## §0.1 v1.1 CHANGE LOG (predecessor)

26 patches applied 2026-04-29 from `17_specification_revisions.md`. Patches grouped by priority.

**Cross-cutting (§1 of doc 17) — single-writer Opinion model:**
- PATCH 1.4 — Procedure B Resolution rewritten: writes Memory only (Opinion change deferred to D).
- PATCH 1.5 — Procedure C Project Completion rewritten: writes Memories only.
- PATCH 1.6 — Procedure D banner: declares single-writer invariant.

**Priority-1 (§2 of doc 17) — implementation blockers:**
- PATCH 2.1 — `select_proposal()` algorithm + `DOMAIN_ARMATURE_ALIGNMENT` 42-entry table.
- PATCH 2.2 — `max_scars` definition (`inner_circle_active_npc_count × 2`).
- PATCH 2.3 — `conviction_alignment_multiplier` values + `OPPOSITIONAL_CONVICTION_PAIRS`.
- PATCH 2.5 — `compute_settlement_signal` null guards + governor fallback.
- PATCH 2.6 — `conviction_secondary=None` uniform-fallback + Armature Confidence (§3.6.X).
- PATCH 2.7 — Resonance lookup category fallback (§4.5).
- PATCH 2.8 — Armature modifier composition: additive + per-dimension normalization.

**Priority-2 (§3 of doc 17) — authoring blockers:**
- PATCH 3.1 — `concern_history` regeneration cooldown.
- PATCH 3.2 — Knowledge Decay sub-step B.0.
- PATCH 3.3 — Visibility gate in Concern generation.
- PATCH 3.4 — `get_or_init_opinion()` lazy initialization + `derive_initial_affect()`.
- PATCH 3.5 — Grieving handling in DA Proposal Phase.
- PATCH 3.6 — Knot integration via Priority 2 Outreach (opacity preserved).
- PATCH 3.7 — `scars_total` / `scars_conviction` split.
- PATCH 3.8 — Vindicated and Resolved Mood triggers.
- PATCH 3.9 — Population Disposition recalculation.
- PATCH 3.10 — Outreach Priority 3 default + salience-5/ttl-1 escalation.
- PATCH 3.11 — NPC Standing recalculation (§8.1).
- PATCH 3.12 — Settlement Signal scope (covered by PATCH 2.5).
- PATCH 3.13 — `generate_new_project()` two-tier derivation.
- PATCH 3.14 — `visible_actions` templates per domain.
- PATCH 3.15 — Passive NPC Memory replacement rules.

**Priority-3 (§4 of doc 17) — implementation-time stubs:** see doc 17 §4 for inventory; representative resolutions noted inline as `[P3-RESOLVED-PER-DOC17-§4]`.

**Featured-behavior (§5 of doc 17) — author commentary added at §1.1.**

**Pending Jordan decisions (§6 of doc 17 / ED-755):** marked inline as `[JORDAN-DECISION-PENDING-ED-755]`. Defaults from doc 17 §6 are recommended but not applied.

**Open questions for follow-up:** see doc 17 §8 (table calibration, OPPOSITIONAL pair canonicalization, visible_actions count target, Standing magnitudes, Path B threshold, Concern volume, Settlement Signal frequency).

---

## §0 PURPOSE AND SCOPE

This document specifies the engine-level architecture for treating named NPCs as autonomous political actors in Valoria. It replaces the implicit "AI priority tree responds to player actions" model with explicit inner-state architecture that produces NPC behavior independent of player involvement, generating emergent political dynamics through the interaction of:

- Per-NPC inner state (Conviction-derived interpretive armatures)
- Multi-scale meta-armatures (settlement and faction)
- Event Impact Matrix (shared event-context computation)
- Four engine procedures (Concerns, Projects, Opinions, Interactions) plus real-time Mood
- Domain Action proposal mechanism (inner-circle competition)

System scope: ~35 named Active NPCs + ~50 named Passive NPCs + statistical population NPCs. Integrates with existing Valoria systems (Conviction, Belief, Scar, Disposition, Knot, Standing, Domain Action, Scene Slate) without modifying them.

---

## §1 NPC TIER STRATIFICATION

| Tier | Population | Inner state |
|---|---|---|
| **Active** | ~35 named NPCs | Full architecture: all data structures, all procedures |
| **Passive** | ~50 named NPCs (parish priests, settlement mayors, junior officers) | Lite architecture: Conviction, Disposition, 1 Concern, 1 Opinion of player, 3 Memories |
| **Population** | All others | Statistical only: faction Disposition averages, Order/Prosperity contribution |

Passive NPCs participate in Settlement Signals (§5.4) and Knowledge propagation (§4.4) but do not run full procedures.

---

### 1.1 Featured Behaviors (designed-as-such, not bugs)

The following behaviors emerge from intersections of mechanics and are documented as intentional design rather than as defects to remediate. Author commentary added per `17_specification_revisions.md` §5.

- **Post-Contest Belief Recovery Arc (RS-50-A).** When a Belief is revised through a Total Victory Social Contest (Path A), the NPC carries the revision as a Scar without immediate dissonance. Over subsequent seasons, accumulated contradicting Memories re-engage the revised Belief through normal Concern processing, sometimes producing a "rebound" — partial return toward the prior position, expressed as ambivalence. This is the engine's representation of contested political reform: imposed change rarely sticks immediately, and the NPC's worldview re-asserts itself through ordinary cognitive processing. Designers should expect ~30% Belief-recovery rate over 8 seasons post-Contest in playtest; this is a feature.

- **Permanent Salience-5 Founding Memory (ST-16-A).** Each Active NPC carries one Memory of permanent salience 5 representing a personal founding event (origin, vow, defining trauma, formative mentor). This Memory is exempt from decay and the 10-Memory replacement rules — it is always referenced, always weighted maximally. Mechanically: a permanent Memory "anchor" that biases the NPC's interpretive frame across the full campaign. Authoring impact: 1 Founding Memory per Active NPC = ~35 entries.

- **Diagonal Chain Legibility (E-DIAG-A).** Concern-resolution → Memory creation → Procedure D Opinion drift produces a multi-Accounting causal chain (event T+0 → Memory T+0 → Concern T+1 → Memory T+1 → Opinion drift T+2). Players observing this chain see "the NPC took a while to come around" rather than instant reaction. The chain is legible because each step is observable through Read/Surveil/Outreach surfaces. Design intent: NPC inner state changes with *time* rather than *event*, preserving Renaissance-pace political feel.

- **Inner-Circle Threshold Milestone (N-DIAG-A, Standing 3↔4) (PATCH v1.2-35 rename).** When a Standing change crosses the inner-circle threshold (3 ↔ 4 transition), engine generates a milestone Scene Slate entry the next Accounting (Priority 3 — available). Player can attend the rising/falling NPC's adjustment scene, or skip it. Mechanically: makes Standing recalculation (PATCH 3.11 / §8.1) visible; thematically: confers narrative weight on institutional advancement/decline. *Note: prior v1.1 title "Standing 5 Milestone Visibility" was a labeling inconsistency (body specifies 3↔4 transition); renamed in v1.2 per SIM-D-G4.*

- **Knot Rupture (PATCH v1.2-3 / SIM-H-G2).** When sustained negative Disposition or major-betrayal events sever a Knot bond, the engine produces a public salience-5 event with cascading consequences: mutual Disposition crash to -4, Memory propagation to all observers, Concerns about relational reliability in inner-circle peers, future Knot-proposal difficulty increase, possible Belief revision. The rupture Memory is permanent (Founding-equivalent for involved parties). Recovery is multi-Year and partial; the original event is never fully erased. This is the engine's strongest *intimate-political* dramatic mechanic. Full mechanic specification: §2.5.2.

---

## §2 PER-NPC DATA STRUCTURES

### 2.1 Identity (static, set at NPC creation)

```
conviction_primary: one of {Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity}
conviction_secondary: one of the above (or None)
backstory_tags: 5-8 tags (e.g., "lost-sibling-eshlund", "trained-by-ehrenwall")
personality:
    risk_tolerance: -2 to +2
    social_warmth: -2 to +2  
    intellectual_rigor: -2 to +2
    institutional_deference: -2 to +2
```

Personality modifies how the NPC interprets identical events. Set at NPC creation; does not change.

### 2.2 State (dynamic)

```
mood: one of {Steady, Anxious, Confident, Grieving, Vindicated, Humiliated, Distracted, Resolved}
mood_set_by: event_id (provenance)
mood_duration: seasons remaining (typical 1-4)
beliefs: 2-3 structured beliefs (existing system)
scars_total: count of all revised Beliefs (existing system, renamed — PATCH 3.7 / N-33-A)
scars_conviction: count of revised Beliefs that engaged conviction_primary domains (subset of scars_total)
disposition_with_player: -3 to +5 (existing; can extend to -4 on Knot rupture)
certainty: 0-5 (existing, optional)
ts: existing Thread Sensitivity (optional)
concern_history: list of last 5 resolved Concern tags
```

**Mood is set in real-time** at event resolution, NOT batched at Accounting. See §6.1.

### 2.3 Concerns (1-3 active per NPC)

```
Concern:
    question: text
    source_event: event_id ref
    salience: 1-5 (decays -1 per season unless reinforced)
    ttl: seasons until forced resolution (default 4)
    seeking: weighted vector across [Agency, Intent, Mechanism] dimensions
    resolution: when satisfied, becomes Belief or modifies Opinion
```

Concerns drive autonomous NPC behavior. Generated by Procedure B (§6.2). Resolved when sufficient Memory matches the seeking tag set, OR force-resolved when salience reaches 0.

### 2.4 Projects (1-2 active per NPC)

```
Project:
    goal: text (e.g., "Train Torben to be a war-leader before Almud dies")
    progress: 0-10
    progress_status: {new (<3), established (≥3)}
    blockers: list of active conditions preventing advancement
    accelerators: list of conditions enabling rapid advancement  
    horizon: short/medium/long (1-3 / 4-8 / 9+ seasons)
    project_domain: tag (military, theological, scholarly, intelligence, economic, etc.)
    visible_actions: actions taken to advance (player-observable)
    completion_effect: stat changes / Opinion shifts when Project succeeds
    failure_effect: stat changes / Opinion shifts when Project fails
    domain_action_required: bool (does this Project need DA proposals?)
    seasons_stalled: int (failure trigger at 8+)
```

Projects are seeded at NPC creation (1 starting Project per Active NPC). Replaced as they complete or fail. New Projects may also be generated in response to Conviction Scars or Project failures.

### 2.5 Opinions (NPC-NPC only, ~5-10 per Active NPC)

Opinions cover NPC-to-NPC relationships. They DO NOT cover NPC-to-player (Disposition handles that).

**Boundary clarification:** Opinion of player is NOT a separate field. NPC-toward-player relationship is fully captured by Disposition for direct interactions and the player's Memory entries on the NPC's Memory list for non-player-present behavior. This eliminates redundancy.

```
Opinion of <other_npc_id>:
    affect_axis: -3 to +3 (computed from referenced Memories)
    confidence: 1-5 (how strongly held; affects hysteresis)
    evidence_memory_refs: list of Memory ids supporting the Opinion
    last_updated: season ref
    presentation_layer (rendered, not stored):
        affect_descriptor: text (e.g., "wary, slightly contemptuous")
        story: text (the narrative this NPC tells about the other)
```

**Hard bound:** affect_axis is clamped to [-3, +3] on every write. No operation can set affect_axis outside this range.

#### 2.5.1 Opinion Initialization (PATCH 3.4 / ST-15-A/B)

All Opinion mutations route through `get_or_init_opinion()`, which returns an existing Opinion or constructs one with derived initial values. Prevents crashes (ST-15-B) and uninitialized affect (ST-15-A) on first contact.

```
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
    
    # Standing differential — modest deference encoded elsewhere; no Opinion bias here
    if subject.faction == npc.faction and subject.standing > npc.standing + 1:
        base += 0
    
    return clamp(base, -3, +3)
```

NPCs of shared Conviction or shared faction start with mild positive Opinion (+1 each, capped at +3). Opposed Conviction or hostile factions start mild negative. Confidence starts at 1 (low — single piece of evidence will easily move the Opinion).

#### 2.5.2 Knot Rupture (PATCH v1.2-3 / SIM-H-G2)

A Knot is a sustained mutual relational commitment between Active NPCs (or NPC and Player). Knots are formed via existing Knot system mechanics (designs/threadwork/). Knot rupture is the formal severance event — among the engine's most dramatic mechanics, treated here as a featured behavior.

**Trigger conditions.** Knot rupture fires when EITHER:
1. `disposition_with_partner < -2` sustained for ≥ 2 consecutive seasons, OR
2. Major-betrayal event: a single contradicting Memory at salience ≥ 5 against a Belief held at confidence 4-5, where the Belief is Knot-related (e.g., "my partner is loyal," "my partner shares my Convictions," "my partner protects me").

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

    # Mutual Disposition shift (extends below normal -3 floor)
    npc_a.disposition_with(npc_b) = -4
    npc_b.disposition_with(npc_a) = -4

    # Knot bond severed
    sever_knot(npc_a, npc_b)
    # → no future P2 mandatory Knot Outreach scenes for this pair
    #   (PATCH 3.6 supersedence does NOT apply post-rupture)

    # Memory generated for all observers (inner-circle peers + Player if peripheral)
    for observer in observers_of(e):
        m = Memory(
            timestamp=current_season,
            event_type="knot_rupture_observed",
            participants=[npc_a, npc_b, observer],
            affect=-2 if (observer is npc_a or npc_b) else -1,
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
- **Future Knot proposals face increased skepticism.** When npc_a or npc_b is offered a new Knot (existing Knot system mechanics), the engine increases acceptance difficulty — receiving NPC's `disposition_with_proposer` requires ≥ +1 (vs ≥ 0 standard) before Knot can form. Reflects loss-of-trust.
- **Belief revision potential.** If npc_a (or Player) accumulates additional contradicting Memories about relational reliability after rupture, Path B Belief revision can fire. Player's Belief "I am trustworthy in personal commitments" can revise to "I am inconstant" — generating a permanent identity Scar.
- **Faction-level reputation:** inner-circle NPCs use the rupture event in their interpretive frame for years. A ruptured-Knot NPC who later argues for institutional trust faces pre-existing skepticism.

**Recovery path.** Knot rupture is reversible only through extended trust-rebuilding:
- npc_a's Disposition with former-partner must reach ≥ 0 again (sustained 4+ seasons of consistent positive Memories).
- A new Knot proposal can be made, subject to the increased-difficulty gate.
- The original `knot_rupture_observed` Memory persists — full erasure is not possible.

**Featured behavior commentary.** Knot rupture is a *politically-public personal-failure event* — both intimate and institutional. Players choosing playstyles that risk Knot rupture should be aware: this is a near-permanent character-mark, and the engine will weight it heavily in long-term relational interpretation. Designers authoring Knot-relevant content should treat Knot rupture as a *featured dramatic peak*, not a mere state-transition. See also §1.1 Featured Behaviors entry on Knot Rupture.

### 2.6 Memories (5-10 high-salience records)

```
Memory:
    timestamp: season ref
    event_type: tag (e.g., "promotion", "betrayal", "shared-crisis", "insult")
    participants: list of NPC ids and (optionally) player ref
    affect: text descriptor + numeric (-3 to +3)
    salience: 1-5 (decays -1 per 4 seasons unless referenced)
    salience_floor: int (set to reference_count × 0.5; floor on decayed salience)
    detail: short text
```

**Memory salience floor:** When a Memory is referenced (in Opinion drift, Concern resolution, or armature seeking-tag matching), its `reference_count` increments. Decayed salience cannot go below `reference_count × 0.5` (max 5). Founding-relationship Memories that are repeatedly used remain salient indefinitely.

**Memory replacement:** When new high-salience Memory would exceed cap (10), the lowest-salience existing Memory is dropped or merged ("another disappointment from the Crown" — collapses similar Memories).

**Passive NPC Memory replacement (PATCH 3.15 / R-42-A):** For Passive NPCs (3-Memory cap), the same replacement rules apply at the lower cap. When a new Memory would exceed cap:

1. If a similar-tag existing Memory exists with same affect-direction, **merge** (collapse "another disappointment from the Crown" — increment `reference_count`; new Memory's salience replaces if higher).
2. Otherwise, **drop the lowest-salience Memory**.
3. **Tie-break:** drop the older Memory (timestamp comparison).

Passive Memories also obey the salience-floor mechanic specified above. Merge path is critical because the 3-Memory cap fills quickly — without merging, every Accounting could swap Memories, producing flicker. Merging preserves cumulative pattern recognition.

---

### 2.7 Knowledge (info-rich NPCs only, variable count)

```
Knowledge:
    fact_tag: structured tag or text
    knowledge_type: {ongoing_state, historical_event, structural}
    source: how this NPC learned it
    salience: 1-5
    sensitivity: 1-5 (controls Disposition gate for sharing)
    valid: bool (set to false on event-driven invalidation)
```

**Knowledge type behavior:**
- `ongoing_state` (e.g., "spy is currently operating in Niedmark"): standard salience decay; marked `valid=false` when underlying state changes.
- `historical_event` (e.g., "spy was arrested in Year 4 Season 3"): salience does not decay; remains valid permanently.
- `structural` (e.g., "Hafenmark runs covert operations in this region"): slow decay (-0.1/season).

**Knowledge invalidation:** When a game-state event renders an `ongoing_state` Knowledge fact false, all NPCs holding it have it marked `valid=false`. The next Concern that would use this Knowledge resolves to "I thought X, but things may have changed" — generating a new Concern about the domain.

**Knowledge → Belief trigger:** When a high-salience (≥4) Knowledge fact is acquired by an NPC and contradicts an active Belief's domain, Procedure B generates a Concern: "Is [Belief] still accurate given what I now know?"

---

## §3 THE ARMATURE

### 3.1 Three-Dimension Armature

NPCs interpret events through a weighted armature derived from their characteristics. The armature has three dimensions:

```
Agency: who/what caused this?
    options: {individual-actor, institutional-force, structural-pressure, divine-will, chance}

Intent: what were they trying to achieve?
    options: {ideological, strategic, personal-ambition, moral-failure, external-compulsion}

Mechanism: how did this happen?
    options: {corruption, calculation, error, social-pressure, authority-exercise}
```

(The fourth dimension "Threat-sensitivity" was eliminated; threat domain priority is read from active Projects + active Concerns + Conviction.)

### 3.2 Weight Derivation

Armature weights are computed from existing NPC data — not authored separately:

```
base_weights_from_conviction(conviction_primary):
    # Authored weight tables: 7 Convictions × 3 dimensions × 5 options
    # Returns: dict[dimension][option] -> base_weight (0.0 to 1.0)

modify_by_personality(weights, personality):
    # Personality applies small dimension-modifiers
    # e.g., high intellectual_rigor: +0.1 to mechanism.calculation, mechanism.error
    # e.g., low risk_tolerance: +0.1 to all threat-related options

modify_by_scar_count(weights, scar_count, conviction_primary, conviction_secondary):  # PATCH 2.6 — uniform-fallback for None secondary
    # Scar 0: 100% conviction_primary weights
    # Scar 1: 75% primary + 25% secondary
    #   if conviction_secondary is None: 100% primary, but reduce armature confidence
    #   (see §3.6.X) — flag the NPC's interpretation as low-confidence
    # Scar 2: 50% primary + 50% secondary
    #   if conviction_secondary is None: 75% primary + 25% UNIFORM-FALLBACK
    # Scar 3+: secondary leads (75% secondary + 25% primary)
    #   if conviction_secondary is None: 50% primary + 50% UNIFORM-FALLBACK
    #   (NPC in protracted identity crisis — interpretations diffuse)
    #
    # UNIFORM-FALLBACK assigns equal weight (1/n) to every option in each dimension,
    # representing absence of an interpretive frame.
    # Soft transition; no abrupt personality flips
    # Note: scar_count uses scars_conviction (PATCH 3.7 / N-33-A), not scars_total

modify_by_active_projects(weights, active_projects):
    # +0.1 to options matching active Project domains
    # NPCs monitor what they're invested in

modify_by_active_concerns(weights, active_concerns):
    # +0.1 to options matching existing Concern seeking tags
    # Continuity bias — interpretive consistency
```

**`compute_armature()` — additive composition with per-dimension normalization (PATCH 2.8 / E-BOT-B):**

```
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
```

**Composition note.** Composition order (personality → scar → project → concern) is irrelevant under additive composition; the order is fixed for reproducibility. Modifiers compose independently; no modifier multiplicatively interacts with another. Per-dimension normalization preserves the probabilistic interpretation: `armature[dim]` sums to 1.0 over its options, suitable for `weighted_select()`. Floor-at-zero handles aggressive negative deltas without producing negative-probability weights.

**Modifier authoring scale.** Each modifier function returns a sparse delta dict. Modifier deltas are typically ±0.05 to ±0.2, with the largest deltas reserved for `scar_modifier` at high Scar counts (which can shift up to ±0.5 per option as armature rotates from primary to secondary).

Final armature: weighted vector across all three dimensions × all options.

### 3.3 Concern Generation Algorithm

```
function generate_concern(npc, event, event_impact_matrix):
    # Read NPC's row in the Matrix
    npc_effects = event_impact_matrix.get_effects_for(npc.id)
    
    # Compute armature for this NPC
    armature = compute_armature(npc)
    
    # For each active dimension in the event's profile:
    seeking = {}
    for dim in event.active_dimensions:
        options = event.options_for(dim)
        weights = armature[dim]
        # Weighted random selection (seeded for save-game reproducibility)
        seeking[dim] = weighted_select(options, weights, rng_seed=event.id+npc.id)
    
    # Build the Concern
    concern = Concern(
        question=render_question(seeking, event, npc),
        source_event=event.id,
        salience=base_salience_from_event(event) + npc_specific_modifiers(npc, event),
        ttl=4,
        seeking=seeking
    )
    
    return concern
```

### 3.4 Concern Resolution Algorithm

```
function resolve_concern(npc, concern):
    # Search NPC's Memories for matches to seeking tag set
    matches = []
    for memory in npc.memories:
        if memory.event_type matches any(concern.seeking) AND memory.salience >= 1:
            matches.append((memory, match_score(memory, concern.seeking)))
    
    matches.sort(by=match_score, descending=True)
    
    if matches:
        # Use highest-salience matching Memory
        top_memory = matches[0]
        resolution = construct_resolution(concern, top_memory, npc.armature)
        # Increment reference_count on used Memory
        top_memory.reference_count += 1
    else:
        # No match — fall back to NPC's prior Belief about the domain
        resolution = vague_resolution_from_priors(concern, npc.beliefs, npc.armature)
    
    return resolution
```

**Wrong resolution is intrinsic, not flagged:** Resolution is wrong when the NPC's armature doesn't match the event's actual cause. Faith-aligned NPC interpreting a strategic-calculation event through Faith seeking-tags produces a Faith-shaped explanation that doesn't match reality. This is the design.

### 3.5 Belief Revision Paths

Two paths to Belief revision, with explicit gating:

**Scar attribution (PATCH 3.7 / N-33-A):** When a Belief is revised (via Path A or Path B), check whether the Belief's domain engages `npc.conviction_primary`. If yes, increment both `scars_total` and `scars_conviction`. If no, increment only `scars_total`. `scars_conviction` drives `modify_by_scar_count()` (armature shift); `scars_total` drives `institutional_stability` (faction weight). See §2.2 for the field definitions.

**Path A — Social Contest (existing system):** Total Victory Contest with Resonant Style argument engaging the specific Belief → immediate Scar.

**Path B — Concern-driven self-correction (new):** When a Concern resolves with a Memory that contradicts an existing Belief:
- If contradiction is **strong** (resolution directly negates Belief's domain) AND there are 2+ contradicting Memories with salience ≥ 3: Belief revises, becomes Scar.
- If contradiction is **weak** (partial update): Belief modifies, no Scar.

**Calcified wrong Belief:** Belief unchallenged for 8+ seasons → calcified. Calcified Beliefs require 3+ contradicting Memories (vs standard 2) for self-correction. Path A Contests against calcified Beliefs are at +1 Ob.

**Belief-revision gating:** If a Belief is revised via Path A this season, all accumulated contradicting Memories for that Belief reset. The Contest result supersedes accumulated evidence.

---

### 3.6 Conviction Alignment for Opinion Drift (PATCH 2.3)

```
function conviction_alignment_multiplier(npc_a, npc_b):
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

NPCs sharing primary Conviction interpret each other's actions through a sympathetic frame, amplifying confidence in the Opinion-direction (1.5×). Sharing secondary as a bridge produces partial sympathy (1.2×). Oppositional Convictions (the four canonical antagonisms in the seven-Conviction system) dampen drift — the NPC's interpretive frame treats the other as untrustworthy regardless of evidence (0.7×). All other pairings are neutral (1.0×).

The multiplier compounds with the existing dampening factor `(1 - |affect|/3)`. Combined effect at extremes: a Faith NPC opining Reason-NPC at affect_axis +2 has dampening 0.33 × oppositional 0.7 = 0.23. Slow movement even with positive Memory evidence.

Note: `Continuity↔Reason` is intentionally included — Reason as restless innovation pressures Continuity's preserve-the-existing logic. Tunable per playtest. See `17_specification_revisions.md` §8.2 for canonicalization concern.

#### 3.6.X Armature Confidence (PATCH 2.6)

Armature confidence is a derived scalar [0,1] tracking the coherence of the NPC's interpretive frame.

- **Confidence = 1.0** when armature is dominated by one Conviction (single coherent frame).
- **Confidence = 0.5** when armature is mixed primary+secondary.
- **Confidence < 0.5** when uniform-fallback is active (frame absent — NPC in protracted identity crisis).

Low confidence increases per-event interpretation variance: in code, `weighted_select()` at `confidence < 0.7` re-rolls once and averages results, producing more inconsistent armature behavior. This is the mechanical surface of "the NPC's worldview has been shattered without a replacement frame" — produces interesting emergent narrative (NPC becomes hard to predict).

---

## §4 EVENT IMPACT MATRIX

### 4.1 Structure

When any event fires, the engine computes an Event Impact Matrix once. The Matrix is consumed by all armatures interpreting the event.

```
EventImpact:
    event_id: unique id
    event_type: tag
    source_actor: id
    
    material_effects[]:           # who gains/loses what tangibly
        actor_id
        type: {resource, position, capacity, territory}
        direction: {gain, loss, neutral}
        magnitude: 1-3
    
    symbolic_effects[]:           # SCOPED: inner-circle of affected factions only
        actor_id (or faction_id)
        conviction_resonance: {aligned, neutral, contradicted}
        institutional_resonance: {empowered, neutral, threatened}
    
    relational_effects[]:         # affected pairs only
        actor_pair: (actor_a, actor_b)
        direction: {convergent, divergent, asymmetric}
    
    scale_signature[]:            # what scales the consequences run at
        {personal, settlement, faction, peninsula}
    
    time_horizon: {immediate, near (1-3 seasons), far (4+ seasons)}
    
    visibility:
        public: bool
        semi_public_observers[]: actor_ids
        private_observers[]: actor_ids
    
    active_dimensions:            # for armature interpretation
        list of armature dimensions activated by this event
    
    options_for_dimension:        # for each active dimension, the legal options
        dict[dimension] -> list[option]
```

### 4.2 Scope Cap

`symbolic_effects` lists ONLY:
- For faction-scale events: inner-circle NPCs of affected factions (~10-15 per affected faction)
- For settlement-scale events: governor + named Passive NPCs in settlement
- For personal-scale events: 2-5 directly involved NPCs

Not all 35 Active NPCs. This bounds Matrix size.

### 4.3 Computation Cost

Per-event compute: ~50-100 simple lookups using existing data (event mechanical resolution, Disposition tables, Standing values) plus the 210-entry Conviction × event-type symbolic resonance authored table.

### 4.4 Cascade Attenuation

Signal magnitude decays at scale boundaries:

```
Scale boundary: personal ↔ settlement ↔ faction ↔ peninsula

Decay factor: 0.7 per boundary crossed

Example: Personal event with salience 5
    → Settlement Signal: salience 5 × 0.7 = 3.5
    → Faction Concern from Settlement Signal: 3.5 × 0.7 = 2.45
    → Peninsula consequence: 2.45 × 0.7 = 1.7

Threshold for influence:
    Salience < 2: Concern generates but does not affect Domain Action selection
    Salience 2+: standard influence
```

This prevents personal-scale events from disproportionately driving faction-level decisions while preserving meaningful cross-scale propagation.

---

### 4.5 Resonance Lookup Fallback (PATCH 2.7)

Unknown `event_type` lookups in the symbolic resonance table fall back through a category system. Each event_type is authored with a category tag; unknown event_types fall back to category defaults; a final `default` category catches truly unrecognized events (returns neutral on all Convictions).

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

Cross-reference from §4.1 where `symbolic_effects` are described.

**Coupling note.** This patch is independent of the E-38-A/B Jordan decision (`[JORDAN-DECISION-PENDING-ED-755]`). If E-38 cuts the symbolic_effects table, this fallback machinery becomes unused but harmless. If E-38 keeps the table, this fallback fills authoring gaps gracefully.

Categorical defaults derive from Renaissance institutional logic: violence threatens Faith and Equity definitionally; `institutional_change` threatens Order/Precedent/Continuity (which value stasis) and aligns with Autonomy (which values dynamism); discovery aligns with Reason and Autonomy. The `default` row is fully neutral so unrecognized events cause no spurious resonance.

---

## §5 META-ARMATURES

### 5.1 Settlement Meta-Armature

A settlement's interpretive frame is computed at Accounting from weighted inputs:

```
SettlementMetaArmature:
    governor_weight = 0.1 + 0.075 × min(governor_tenure_seasons, 4)
        # Scales 0.1 → 0.4 over first 4 seasons of tenure
        # New governor: 10% (no institutional weight yet)
        # Established (4+ seasons): 40%
    
    passive_npc_aggregate_weight = 0.6 - governor_weight
        # Scales inversely with governor tenure
        # New governor: 60% (institutional NPCs dominate)
        # Established: 30%
    
    institutional_character_weight = 0.2
        # Cathedral → Faith bias; Market → Reason/Autonomy; 
        # Fortress → Order/Continuity; Outpost → Autonomy
    
    population_disposition_weight = 0.1
        # Statistical mean Disposition with controlling faction
```

**Weight normalization:** If any tier is absent (e.g., remote Outpost has no Passive NPCs), normalize remaining weights to sum = 1.0:

```
total_present = sum(weights_for_present_tiers)
for each present_tier:
    effective_weight = raw_weight / total_present
```

**`population_disposition` recalculation (PATCH 3.9 / N-35-A — each Accounting):**

```
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

Order and Prosperity respond to faction governance quality; mapping them to population sentiment is a natural derivation. The event-delta term lets faction-caused disasters or windfalls move sentiment without per-population per-event tracking. Range clamped per existing Disposition spec.

---

### 5.2 Settlement Signal

The Settlement Meta-Armature interprets events affecting the settlement and produces a Settlement Signal:

```
function compute_settlement_signal(settlement, recent_memories):  # PATCH 2.5 — null guards + governor fallback (also PATCH 3.12: S-44-A scope)
    # Guard 1: settlement has no Passive NPCs (ST-20-A)
    if not settlement.passive_npcs:
        if settlement.governor:
            return SettlementSignal.from_governor(settlement.governor, settlement.recent_events)
        return None  # remote settlement w/ no governor and no Passive NPCs — no Signal
    
    # Aggregate Passive NPC Memories from last 2 seasons
    weighted_memories = []
    for npc in settlement.passive_npcs:
        for memory in npc.recent_memories(seasons=2):
            # Disposition-with-player only amplifies player-involving Memories (S-44-A / PATCH 3.12)
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

function SettlementSignal.from_governor(governor, recent_events):  # PATCH 2.5 — governor-only fallback
    # For settlements without Passive NPCs.
    if not recent_events:
        return None
    dominant = max(recent_events, key=lambda e: e.salience)
    return SettlementSignal(
        affect_axis=interpret_event_affect(dominant, governor.armature),
        primary_tag=dominant.event_type,
        salience=dominant.salience * 0.5,  # governor-only Signal at half weight
    )
```

Settlement Signal propagates to controlling faction's "relevant Active NPC" as a Concern (Procedure B input next Accounting). When `compute_settlement_signal` returns `None`, faction-level Concern generation skips this settlement's Signal that Accounting (sparse-settlement handling).

**Routing logic (PATCH v1.2-2 / SIM-C-G6):**

```
function route_signal_to_concern(signal, settlement, faction):
    # Tier 1 — settlement governor if Active NPC
    if settlement.governor and settlement.governor.is_active_npc():
        return settlement.governor

    # Tier 2 — faction leader if seat settlement
    if settlement == faction.seat_settlement:
        return faction.leader

    # Tier 3 — round-robin among inner-circle by signal.primary_tag domain affinity
    candidates = []
    for npc in faction.inner_circle:
        if npc.is_active():
            affinity = DOMAIN_ARMATURE_ALIGNMENT[derive_domain(signal.primary_tag)][npc.conviction_primary]
            candidates.append((npc, affinity))
    candidates.sort(key=lambda x: (-x[1], -x[0].standing, x[0].id))
    return candidates[0][0] if candidates else None
```

Where `derive_domain(tag)` maps Signal tag to its closest matching Project domain (e.g., "raid_threat" → military; "trade_deal" → economic; "ceremonial" → theological/diplomatic). Authored mapping in `params/signal_tag_to_domain.md`.

**Routing failures.** If Tier 3 also returns None (no Active NPCs in inner circle — extreme edge case), the Signal is dropped. This should occur only during severe Faction Crisis (institutional autopilot).

**Cross-border events (PATCH v1.2-37 / SIM-E-G1):** A single peninsula-scale event can produce one Signal per affected settlement (multi-settlement events). Each settlement's Signal propagates as its own Concern via the routing logic above. The event itself is unique; Signals are derived per-settlement; Concerns propagate per-Signal.

**Signal salience handling (PATCH v1.2-12 / SIM-C-G1, G2):** After cascade decay (`signal.salience *= 0.7`), if the resulting salience is below 1, the Signal is dropped (sub-threshold). Otherwise, salience is rounded to nearest integer for Concern propagation.

**Repeated-Signal handling on active Concern (PATCH v1.2-15 / SIM-C-G8):** When a Settlement Signal arrives matching an Active NPC's still-active Concern (same domain-tag), the existing Concern's salience is updated via max-update (`existing.salience = max(existing.salience, signal.salience)`); ttl is also max-updated. No new Concern generated. Prevents runaway Concern accumulation while reflecting ongoing severity.

### 5.3 Faction Meta-Armature

```
FactionMetaArmature:
    inner_circle_aggregate:
        weighted_average_of_inner_circle_armatures
        weights: Standing-based (S7: 1.0, S6: 0.7, S5: 0.5, S4: 0.3) × mood_modifier
        leader: (standing_weight × 1.5) × mood_modifier
        
        # PATCH v1.2-18 / SIM-G-G1 — Mood-impact dampening:
        mood_modifier = {
            Steady, Confident, Vindicated, Resolved: 1.0  # full institutional engagement
            Anxious, Humiliated:                     1.0  # still institutionally engaged
            Distracted:                              0.7  # cognitive dissonance reduces weight
            Grieving:                                0.5  # active withdrawal from institutional engagement
        }
        # Rationale: leaders/peers in difficult Mood states have reduced institutional weight,
        # reflecting their reduced engagement. Crown's Almud falling Distracted reduces his
        # armature contribution from 1.5 to ~1.05 (1.5 × 0.7); the inner circle's aggregate
        # shifts toward less-distracted peers. Realistic political dynamic.
    
    institutional_stability:
        single merged term (replaces prior institutional_inertia + ethical_framework_anchor)
        weight: 0.4 × max(0, 1 - (sum(npc.scars_total for npc in inner_circle) / (inner_circle_active_npc_count × 2)))  # PATCH 2.2 + PATCH 3.7 — max_scars=2×inner_circle; uses scars_total (institutional weight responds to all Belief revisions)
        value: faction's historical dominant Conviction at game-start
        # Crown: Order/Virtue-Ethics derived
        # Church: Faith/Divine-Command
        # Hafenmark: Precedent/Categorical-Imperative
        # Varfell: Reason/Consequentialist
        # etc.
    
    aggregate_weight = 1.0 - institutional_stability_weight
```

**Behavior under inner-circle compromise:**

The leader's individual armature carries 1.5× weight but does not dominate. A Reformer-arc Almud (Reason-shifted) does not single-handedly shift Crown's institutional interpretation — institutional_stability + Faith-aligned Confessor + Order-aligned Marshal pull the meta-armature toward Crown's traditional framework. This produces the historically realistic dynamic where reformer rulers find their courts resisting their personal transformations.

**Player joining inner circle:** At Standing 5+, the player's armature becomes part of the Faction Meta-Armature. The player's Conviction influences the faction's institutional interpretation.

#### Proposal Selection (PATCH 2.1)

The Faction Meta-Armature ranks competing inner-circle proposals via `select_proposal()`, defined in §6.2. The `DOMAIN_ARMATURE_ALIGNMENT` table is authored content (see §10).

**DOMAIN_ARMATURE_ALIGNMENT table (42 entries, 0.0–1.0):**

| domain | Faith | Order | Reason | Equity | Precedent | Autonomy | Continuity |
|---|---|---|---|---|---|---|---|
| military | 0.3 | 1.0 | 0.6 | 0.2 | 0.5 | 0.4 | 0.7 |
| theological | 1.0 | 0.4 | 0.3 | 0.3 | 0.7 | 0.2 | 0.6 |
| scholarly | 0.2 | 0.4 | 1.0 | 0.5 | 0.6 | 0.7 | 0.4 |
| intelligence | 0.3 | 0.7 | 0.8 | 0.2 | 0.5 | 0.6 | 0.5 |
| economic | 0.2 | 0.5 | 0.7 | 0.6 | 0.4 | 0.8 | 0.4 |
| diplomatic | 0.5 | 0.6 | 0.5 | 0.7 | 0.6 | 0.4 | 0.6 |

Six domains × seven Convictions. Add rows as new domains are introduced (`personal_legacy`, `personal_courtship`, etc.).

Standing bonus is small (0.1 × standing where standing ∈ [3,7] → max 0.7), so a low-aligned proposal cannot win on Standing alone.

Tie-breaks: Standing → seasons_stalled (higher → wins, prevents perpetual stall).

---

### 5.4 Faction Crisis Behaviors

**Faction crisis threshold:** If ≥ 40% of inner-circle NPCs are in {Distracted, Grieving} simultaneously:
- Faction Meta-Armature overrides to **institutional autopilot** mode
- Faction executes only existing Priority 1-2 Domain Actions from pre-existing patterns
- No new NPC Project proposals accepted
- No inner-circle competition this season
- Survival actions still fire normally

**Recovery paths (PATCH v1.2-21 / SIM-H-G4):**
1. Mood states improve below threshold — happens if external pressure subsides AND inner-circle peers process Concerns toward resolution. Standard recovery for transient crises (e.g., plague-induced).
2. Succession event resolves underlying conflict — leader-death + `designate_new_leader` (§5.4.1 below) OR successful Coup (§5.4.2 below). Leadership clarity restores institutional decision-making capacity even if some peers remain Distracted.
3. External alliance event — formal merging or vassalage to another faction (out of v1.2 scope; existing diplomatic mechanics).

A Faction Crisis without resolution path through (1)-(3) is structurally degenerate and indicates engine should generate diplomatic/external pressure events to force resolution. Long-running crises (>8 seasons) may trigger neighbor-faction interventions.

**Cross-faction event handling during simultaneous crises (PATCH v1.2-39 / SIM-H-G5):** When multiple factions are simultaneously in Faction Crisis (institutional autopilot), cross-faction events (treaty proposals, diplomatic overtures) are declined by autopilot factions. Bounce-back events (refused-overture) accumulate as Memories in the proposing faction and as latent diplomatic-tension Concerns to surface when crisis-state ends.

**Anomaly detection:** If ≥ 3 inner-circle NPCs simultaneously show {Disposition-with-leader < baseline} AND {at least 2 in negative Mood states (Distracted, Humiliated, Anxious)} AND no major external crisis event this season:
- Faction Meta-Armature generates Concern: "Internal destabilization detected?" salience 4
- Faction leader initiates Loyalty Interviews (Demand scenes) with flagged NPCs
- Does not directly expose adversarial player operations but creates scrutiny environment

**Minimum inner-circle friction:** If inner-circle active NPC count < 3:
- All faction Domain Actions take +1 Ob (institutional stress modifier)
- Stacks with any advisor opposition
- Distinguishes collapsed faction from functional faction even before territorial losses

**City-state Domain Actions** (collapsed factions, partial stat sheet):
- Available: Influence and Wealth Domain Actions only
- Unavailable: Military, Mandate, faction-large-scale actions
- Standard Ob formula applies

#### 5.4.1 Faction Succession (PATCH v1.2-19 / SIM-E-G2)

When the faction leader dies (or otherwise becomes permanently incapable — e.g., reduced to Standing < 4 below inner-circle threshold via long-term failure), the leader-flag must transfer.

**Trigger:** event_type = "leader_death" OR "leader_exit_inner_circle".

**Selection mechanic:**

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

#### 5.4.2 Leader Challenge / Coup Mechanic (PATCH v1.2-20 / SIM-H-G3)

A faction-internal peer challenger can attempt to displace the current leader through a Path A Total Victory Social Contest at faction-leader-Belief level.

**Trigger.** Challenger NPC initiates a Social Contest against the leader's Belief "I am the rightful leader of <faction>." Requires:
- `Challenger.standing >= leader.standing` (cannot challenge from clearly-lower position).
- `Challenger.opinion_of(leader).affect_axis < -1` (sustained negative Opinion).
- Challenger has accumulated ≥ 3 contradicting Memories about leader's competence at salience ≥ 3 in last 4 seasons.

**Contest dynamics.**
- Contest is Path A (Belief-level), public visibility.
- Faction Meta-Armature backs leader (institutional_stability anchor + leader's 1.5× weight with current mood_modifier per PATCH v1.2-18).
- Challenger's coalition: any inner-circle peer with `opinion_of(leader).affect_axis < 0` contributes to challenger's side; any peer with `opinion_of(leader).affect_axis > 0` contributes to leader's side.
- Player can support either side (if S5+ and aligned with one party).

**Outcomes.**
- **Total Victory for challenger:** leader-flag transfers; existing leader becomes peer at current Standing (no automatic exile). Trigger `leader_change` event.
- **Modified Victory for challenger:** leader retains flag but accepts institutional reorganization (similar to engaged-player coalition outcome — reorganization with minority protections).
- **Modified Defeat for challenger:** leader retains flag; challenger's Standing penalty (Δ_standing -1 to -2 immediate, not waiting for Year boundary).
- **Total Defeat for challenger:** leader retains flag + challenger's Belief revises to "leader is rightful" (Scar generated) + challenger may be exiled to peripheral status.

**Faction Crisis interaction.** If contest occurs during Faction Crisis (institutional autopilot), the contest is *the* resolution path — succession by combat, in effect. Crisis ends with Contest outcome.

---

## §6 PROCEDURES

### 6.1 Real-Time Mood (NOT a batched procedure)

Mood is set at event resolution, not at Accounting. When an event resolves:

```
function update_mood_real_time(npc, event, event_impact):
    if event_qualifies_as_mood_setter(npc, event):
        new_mood = mood_from_event_table(event_type, npc_armature, event_impact)
        npc.mood = new_mood
        npc.mood_set_by = event.id
        npc.mood_duration = standard_duration_for_mood(new_mood)
```

**Mood transition examples:**
- Successful Domain Action proposal → Confident (1-2 seasons)
- Treaty contradicting primary Conviction → Anxious or Humiliated based on advocacy
- Knot partner death → Grieving (2-4 seasons)
- Conviction Scar acquired → Distracted (1 season)
- Public political defeat → Humiliated (2-3 seasons)

**Mood mechanical effects:**

| Mood | Effect on actions taken by this NPC |
|---|---|
| Steady | No modifier |
| Anxious | +1 Ob to social/political actions; -1 Ob to defensive/security actions |
| Confident | -1 Ob to action this NPC initiates; +1 Ob if action requires caution |
| Grieving | Major actions auto-fail without Spirit check Ob 1; minor actions standard |
| Vindicated | -1 Ob to action aligned with the vindicating event's themes |
| Humiliated | +2 Ob to public actions; -1 Ob to private actions (retaliation, plotting) |
| Distracted | +1 Ob to all actions; new Projects (progress <3) halt; established Projects (≥3) continue at +1 Ob |
| Resolved | -1 Ob to action consistent with resolution; +1 Ob to inconsistent actions |

**Mood decay:** Each Accounting, Mood decays one step toward Steady unless reinforced this season. Personality modifies decay rate.

- **Vindicated** (PATCH 3.8 / E-37-A): NPC's previously-stated position is publicly confirmed by outcome.
    - Trigger conditions (any of):
      (a) NPC won a Total Victory Social Contest as defender within last 2 seasons.
      (b) A Project completion this season reflects NPC's earlier predicted outcome
          (e.g., NPC publicly opposed the project; project failed).
      (c) A Domain Action that NPC publicly advocated succeeded with positive consequence
          visible this season.
    - Duration: 2 seasons. -1 Ob to action aligned with vindication's themes.

- **Resolved** (PATCH 3.8 / E-37-A): NPC's Concern resolution produced a clear, satisfying answer that refines or confirms existing Belief (no Scar produced).
    - Trigger conditions: Concern resolves via `resolve_concern()` with a high-salience matching Memory (≥4) AND resolution does NOT produce a Scar (resolution.causes_belief_revision is False, OR contradiction_strength is "weak").
    - Duration: 1-2 seasons (1 if salience-4 Memory; 2 if salience-5).
    - Effect: -1 Ob to action consistent with resolution; +1 Ob to inconsistent.

(Procedure D and B-Resolution check these conditions and call `update_mood_real_time()` when applicable.)

---

### 6.2 Accounting Sequence

Procedures run in fixed order at Accounting: B → (Domain Action proposals) → C → D → E.

#### Procedure B — Concern Generation and Resolution

**B.0 — Knowledge Decay (PATCH 3.2 / N-BOT-D — runs before Generation):**
```
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

# referenced_recently() is set by any Procedure that uses the Knowledge fact
# (e.g., Procedure E knowledge sharing increments it).
```

**Visibility helper (PATCH 3.3 / N-BOT-E):**
```
function npc_observes_event(npc, event):
    if event.visibility.public:
        return True
    if npc.id in event.visibility.semi_public_observers:
        return True
    if npc.id in event.visibility.private_observers:
        return True
    return False
```

**Generation:** (with visibility gate and concern_history cooldown — PATCH 3.1, 3.3)
```
For each event in last_season.events:
    For each NPC in event.affected_npcs:
        # Visibility gate (PATCH 3.3 / N-BOT-E) — NPC must be an observer
        if not npc_observes_event(npc, event):
            continue
        if NPC is Active:
            # Concern regeneration cooldown (PATCH 3.1 / N-BOT-C)
            potential_tag = derive_concern_tag(event, npc.armature)
            if potential_tag in npc.concern_history and event.salience < 4:
                continue  # recent same-domain Concern resolved; suppress regen
            
            concern = generate_concern(npc, event, event_impact_matrix)
            npc.concerns.append(concern)
            if len(npc.concerns) > 3:
                drop_lowest_salience_concern(npc)

For each Active NPC:
    For each Knowledge in npc.knowledge with salience >= 4:
        if knowledge contradicts any active Belief domain:
            generate Concern("Is [Belief] accurate given Knowledge X?")
```

**Resolution:** (single-writer Opinion model — see PATCH 1.4 / §0.1 change log)
```
For each Active NPC:
    For each concern in npc.concerns:
        concern.salience -= 1  # standard decay
        if concern.salience <= 0 OR ttl exhausted:
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
            # Scar gating: strong contradiction + multiple high-salience contradicting Memories required
            # Calcified Belief check: if Belief unchallenged 8+ seasons, requires 3+ Memories
            # If Belief revised this season via social Contest (Path A): reset accumulated Memory weight
            
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
            
            # Concern history (cooldown — see PATCH 3.1 / §6.2 Generation)
            npc.concern_history.append(resolution.tag)
            if len(npc.concern_history) > 5:
                npc.concern_history.pop(0)
            
            remove(concern)
```

#### Domain Action Proposal Phase (between B and C)

```
flagged_proposers = []

For each Active NPC:
    if npc.active_project.domain_action_required:
        if npc.project_advancement_needs_da_this_season:
            # Personality and Mood gating
            # Grieving (PATCH 3.5 / ST-19-A): auto-fails proposal without Spirit Ob 1
            if npc.mood == Grieving:
                if not npc.spirit_check(ob=1):
                    continue  # Grieving NPC cannot propose this Accounting
                proposal_modifier = +1  # passes but +1 Ob
            elif npc.mood == Distracted and npc.personality.institutional_deference >= 1:
                continue  # high-deference Distracted NPCs suppress proposals
            elif npc.mood == Distracted and npc.personality.institutional_deference < 1:
                proposal_modifier = +1  # Distracted, low-deference: proposes at +1 Ob
            else:
                proposal_modifier = 0
            flagged_proposers.append((npc, npc.active_project, proposal_modifier))

# Personal priority insertion: Conviction-aligned Projects can displace Priority 5-6 institutional duties
For each (npc, project) in flagged_proposers:
    if project.domain_aligned_with_conviction_primary AND project.progress > 0:
        if npc.faction.priority_tree.has_priority_5_or_6_capacity:
            allow_displacement(npc, faction_priority_5_or_6_slot)
            # Displacement risk: institutional_deference check at Ob 1
            # Failure: faction leader may notice neglect

# Inner-circle competition: same-faction proposals
For each faction:
    proposals_in_faction = [p for p in flagged_proposers if p.npc.faction == faction]
    if len(proposals_in_faction) > 1 AND any pair shares domain:
        # Faction Meta-Armature evaluates
        winner = select_proposal(proposals_in_faction)  # PATCH 2.1 — defined below
        for loser in proposals_in_faction except winner:
            loser.project.seasons_stalled += 1

# select_proposal — Faction Meta-Armature inner-circle competition (PATCH 2.1 / E-36-A)
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
        # Stall-escalator (PATCH v1.2-4 / ED-760): long-stalled projects gradually escalate
        # +0.05 per season of stalling. Validated at scale (SIM-E Sc 2, SIM-G Sc 1-4) as both
        # anti-deadlock and anti-ossification mechanic. At seasons_stalled=4: +0.20 boost
        # (matches a 2-Standing differential). At seasons_stalled=8: +0.40 (matches 4-Standing).
        # Without it, unequal-Standing same-domain collisions can produce permanent winner-takes-all
        # deadlocks — see SIM-B Scenario 8.
        stall_escalator = 0.05 × p.project.seasons_stalled
        scores[p] = conviction_alignment + standing_bonus + stall_escalator
    
    # Four-level tie-break (PATCH v1.2-8 / SIM-B-G1):
    # score → Standing → seasons_stalled → NPC.id ascending (lower wins for stable determinism)
    winner = max(proposals, key=lambda p: (scores[p], p.npc.standing, p.project.seasons_stalled, -p.npc.id))
    return winner

# meta_armature.conviction_weights[c] is a normalized 7-vector summing to 1.0,
# derived from inner-circle aggregate (§5.3) plus institutional_stability anchor.

# Apply armature-induced Ob modifiers
For each proposal in selected_proposals:
    For each inner-circle NPC in proposal.faction:
        if NPC.armature interpretation aligns with proposal:
            proposal.ob_modifier -= 1  # supporter
        elif NPC.armature interpretation contradicts proposal:
            proposal.ob_modifier += 1  # opposer

execute_proposed_domain_actions(selected_proposals)
```

#### Procedure C — Project Advancement

```
For each Active NPC:
    project = npc.active_project
    
    # Check stall
    if project.progress unchanged this season:
        project.seasons_stalled += 1
        if project.seasons_stalled >= 8:
            execute_failure(project, npc)
            generate_replacement_project(npc)
            continue
    else:
        project.seasons_stalled = 0
    
    # Mood-based gating
    if npc.mood == Distracted:
        if project.progress < 3:
            continue  # new Projects halt
        # established Projects continue at +1 Ob (already applied)
    
    # Institutional deference gating during faction crisis
    if npc.faction.in_priority_1_filter and npc.personality.institutional_deference >= 1:
        continue  # high-deference: Project pauses during crisis
    
    # Advance project
    advance_project(project, mood_modifier)
    
    # Completion check
    if project.progress >= 10:
        execute_completion_effect(project, npc)
        # Project legacy → Memories only (D consolidates Opinion change — PATCH 1.5)
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
        generate_new_project(npc)
```

# generate_new_project — two-tier derivation (PATCH 3.13 / S-46-A)
function generate_new_project(npc):
    # Tier 1 — pre-authored project queue
    if npc.authored_project_queue and len(npc.authored_project_queue) > 0:
        return npc.authored_project_queue.pop(0)
    
    # Tier 2 — Conviction-aligned procedural generation
    domain = sample_domain_weighted_by_conviction(npc.conviction_primary)
    horizon = weighted_choice(["short", "medium", "long"], [0.4, 0.4, 0.2])
    
    # Look up template; sample one as Project's representative visible_action (PATCH 3.14 / NS-49-A)
    visible_actions_pool = VISIBLE_ACTIONS_TEMPLATES[domain]
    
    project = Project(
        goal=generate_goal_from_template(domain, npc),
        progress=0,
        progress_status="new",
        blockers=[],
        accelerators=[],
        horizon=horizon,
        project_domain=domain,
        visible_actions=[random.choice(visible_actions_pool)],
        visible_actions_pool=visible_actions_pool,  # for varying observation (PATCH 3.14)
        completion_effect=standard_effect_for(domain, npc),
        failure_effect=standard_effect_for_failure(domain, npc),
        domain_action_required=domain_action_required_for(domain),
        seasons_stalled=0,
    )
    return project

function sample_domain_weighted_by_conviction(conviction):
    # Reuse DOMAIN_ARMATURE_ALIGNMENT table from §6.2 / PATCH 2.1
    weights = {d: DOMAIN_ARMATURE_ALIGNMENT[d][conviction] for d in DOMAINS}
    return weighted_select(list(weights.keys()), list(weights.values()))
```

Tier 1 honors authored content (specific NPCs may have multi-Project arcs the designer wants preserved); Tier 2 ensures the spec is robust without that content (any NPC can always generate a fresh Project on completion). Conviction-aligned domain selection produces character-consistent follow-ups: a Faith NPC tends to start theological projects, a Reason NPC tends toward scholarly. Horizon weighting (40/40/20 short/medium/long) keeps the project pipeline diverse.

```
#### Procedure D — Opinion Drift

> **Single-writer invariant.** Procedure D is the only procedure that mutates
> Opinions. Procedures B-Resolution and C-Completion produce Memories; D consolidates
> all season-Memory effects into Opinion changes. See §0.1 change log / `17_specification_revisions.md` §1
> for rationale.

```
For each Active NPC:
    For each opinion in npc.opinions:
        # Find Memories created this season involving the opinion's subject
        new_memories = filter_memories(npc.memories, 
                                       subject=opinion.subject, 
                                       this_season=True)
        
        for memory in new_memories:
            # Lazy-init Opinion if first contact (PATCH 3.4 / ST-15-B)
            opinion = get_or_init_opinion(npc, memory.subject_npc_id)
            # Drift formula with dampening
            multiplier = conviction_alignment_multiplier(npc, opinion.subject_npc)  # PATCH 2.3
            drift = base_drift × (1 - abs(opinion.affect_axis) / 3) × multiplier
            
            if memory aligns with opinion:
                opinion.confidence += 0.0 to +1.0
                opinion.affect_axis += small_drift × sign(memory.affect)
            elif memory contradicts opinion:
                if opinion.confidence <= 2:
                    # Weak Opinion shifts
                    opinion.affect_axis += larger_drift × sign(memory.affect)
                    opinion.confidence = max(1, opinion.confidence - 1)
                elif opinion.confidence >= 3:
                    # Strong Opinion holds; cognitive dissonance
                    # Generate Concern: "Is [subject] who I thought they were?"
                    generate_concern_about_subject(npc, opinion.subject)
                    if opinion.confidence == 4 or 5 AND contradiction_acute:
                        npc.mood = Distracted
        
        # Hard clamp on every write
        opinion.affect_axis = clamp(opinion.affect_axis, -3, +3)
        
        # Increment reference_count on Memories used
        for memory in opinion.evidence_memory_refs:
            memory.reference_count += 1
            memory.salience_floor = max(memory.salience_floor, memory.reference_count × 0.5)
```

#### Procedure E — Off-Screen Interactions

**Budget:**
- Active NPCs in same inner circle: 60% ambient interaction probability per pair per season (reduced to 20% for Distracted NPCs)
- Cross-faction Distant Contact: 10% per qualifying pair (prior Memory + active mutual Opinion ≥|1|)

**Per-pair drift values (per interaction):**
- Shared primary Conviction: ±0.3 affect_axis drift
- Same faction, no shared Conviction: ±0.1 drift
- Different Conviction: ±0.05 drift
- Drift dampened by dampening factor: drift × (1 - |current_affect_axis| / 3)

```
For each inner-circle pair (npc_a, npc_b) in same faction:
    # Reduce probability if either is Distracted
    base_prob = 0.6
    if npc_a.mood == Distracted or npc_b.mood == Distracted:
        base_prob = 0.2
    
    # Faction crisis: halve ambient rate
    if faction.stability <= 2:
        base_prob = base_prob / 2
    
    if random() < base_prob:
        interaction = generate_interaction(npc_a, npc_b)
        apply_drift(npc_a.opinion_of(npc_b), interaction)
        apply_drift(npc_b.opinion_of(npc_a), interaction)
        
        # Knowledge sharing
        for npc, other in [(npc_a, npc_b), (npc_b, npc_a)]:
            for knowledge in npc.knowledge:
                if knowledge.salience >= 3 and knowledge.valid:
                    if any(other.concern.seeking matches knowledge.fact_tag for concern in other.concerns):
                        share_knowledge(npc, other, knowledge)
                        new_memory = Memory("Heard from [npc] that [knowledge.fact]")
                        new_memory.salience = knowledge.salience - 1
                        other.memories.append(new_memory)
        
        # Gossip propagation
        cumulative_drift = abs(interaction.drift_a) + abs(interaction.drift_b)
        if cumulative_drift > 0.5:
            generate_gossip_item(interaction)

# Cross-faction Distant Contact
For each cross-faction pair (npc_a, npc_b) with prior Memory and mutual Opinion |≥1|:
    if random() < 0.10:
        interaction = generate_distant_contact(npc_a, npc_b)
        apply_drift_with_decay(...)  # smaller drift values for Distant Contact
```

**Knot integration (PATCH 3.6 / S-LAT-A — opacity preserved):** Knot partners have guaranteed access to each other's Observable behavior (100% ambient probability when in same settlement). For each Knot partner with an active Concern of salience ≥ 2 about the player, a Priority 2 Outreach scene is generated for the player's next Scene Slate. The Concern is conveyed through partner-driven dialogue in that scene. The player learns of the Concern by attending the scene; NPCs share by choice through scenes (opacity principle preserved). Mechanically equivalent to direct surfacing — player still learns within one Accounting — but routed through Scene Slate so the player must actually attend rather than receive automatic disclosure.

---

## §7 PLAYER-FACING SURFACES

What the player can observe, and how:

### 7.1 Read Action (existing, expanded)

| Disposition | Read reveals |
|---|---|
| Any | NPC's current Mood |
| +2 (Friendly) | One observable behavior label (what NPC is currently doing) |
| +3+ (Trusting) | No additional structured information |

At Disposition +3+, NPCs voluntarily reveal partial Concern information through Outreach scene dialogue (candor), not through direct Read access. **Opacity is preserved at high Disposition** — NPCs choose to share, not give the player direct data access.

### 7.2 Observable Behavior Surfacing

NPC Project advancement actions surface to the player through:

1. **Ambient encounter:** 25% chance per player scene action in same settlement of encountering an NPC's visible_action in passing. Brief; no scene action cost.
2. **Read action at Disposition +2:** "active behavior" label.
3. **Investigation (Surveil):** Costs scene action. Reveals Project's visible_action plus Project-related Memories at current Depth.
4. **Gossip:** NPCs with high Disposition with player gossip about other NPCs' activities. Provides interpretive context: "She's grooming him for command, others say she's steering his political circle."
5. **Knot:** Guaranteed access to partner's Observable behavior (100% in shared settlement).

**Variable observation (PATCH 3.14 / NS-49-A):** Each Read or Surveil that surfaces a Project's `visible_action` samples a fresh string from `project.visible_actions_pool` (varying observation across encounters; the NPC is not always doing literally the same activity). The player surveilling the Marshal across multiple Accountings sees "drilling troops" then "inspecting fortifications" then "consulting with engineer" — all consistent with a military-domain Project but varied. Pool authored at ~10 entries per domain (~80 total; see §10).

### 7.3 Witness Mode (existing, capped)

When the player misses scenes due to scene action budget, Witness Mode fires to give passive observation. **Information cap: max 3 Read results per Accounting from Witness Mode.** Remaining witnessed scenes produce narrative summary only ("The Cardinal confronted Himlensendt publicly. You weren't there. Consequences pending.").

### 7.4 Crisis Priority Modifier

When Scene Slate is saturated (5+ competing scenes), priority ordering is adjusted:
- Standard priority ordering applies (faction leader removal > heresy investigation > stability crisis > etc.)
- BUT scenes involving NPCs with Disposition ≥ +3 with player receive +1 priority level
- Allows player relationship investment to shape which crises they personally attend

### 7.5 Factional Exposure with Loyalty Cover

Cross-faction interactions accumulate Factional Exposure. Detection probabilistic:
```
Each season: faction.intel_pool roll vs (player.cover + loyalty_cover_bonus)

loyalty_cover_bonus:
    Strong loyalty signal this season: +1 (max +2)
    Strong signals: council attendance with aligned vote, Standing advancement,
                    public faction defense in crisis
    Decays each season not renewed
```

### 7.6 NPC Outreach Generation (existing, augmented — PATCH 3.10 / R-39-A)

**Concern-driven Outreach:** NPCs with active Concerns about the player generate Scene Slate entries. Default **Priority 3 — AVAILABLE** (the player MAY choose to attend; if skipped, the scene does not consume a slot, and the underlying Concern continues its normal decay).

**Mandatory escalation:** When a Concern reaches `salience 5 AND ttl ≤ 1` (one season from forced resolution), the Outreach scene upgrades to **Priority 2 mandatory** for that Accounting only. After force-resolution, the scene drops from Slate.

**Tone:** Scene tone reflects current Mood (Anxious Concerns → worried tone; Vindicated → assertive tone; Grieving → subdued tone, etc.).

**Knot exception:** The mandatory upgrade rule applies only to Concerns about the player. NPC-NPC Concerns that surface via Knot (PATCH 3.6 / S-LAT-A) follow their own Priority 2 rules and are not subject to this gate.

This pattern preserves NPC autonomy (NPCs still generate Concerns and Outreach proactively) while restoring player agency (the player can decline non-urgent matters). Mandatory escalation ensures urgent Concerns reach the player; non-urgent matters become available content the player can engage with on their own initiative.

---

## §8 INTEGRATION WITH EXISTING SYSTEMS

| Existing system | Integration |
|---|---|
| Disposition track (-3 to +5) | Unchanged. Sole player-NPC relationship measure. |
| Conviction Scars | Unchanged. Triggers Mood: Distracted; generates Concerns; Path A revision supersedes Path B accumulated Memory. |
| Beliefs | Unchanged. Resolved Concerns may produce new Beliefs (potentially incorrect). Calcification mechanic for unchallenged Beliefs. |
| NPC Outreach (existing §8.11) | Augmented with Concern-driven Outreach. |
| Standing ladder | Unchanged. Promotion events generate Memories and Opinion shifts; player at Standing 5+ enters Faction Meta-Armature aggregate. |
| Domain Actions | Unchanged. Failed Domain Actions generate Concerns; successful advance proposing NPC's Project. Inner-circle competition for proposal selection. |
| Scene Slate | Augmented. Concern-generated Outreach at Priority 3. NPC-NPC interaction outcomes can spawn Priority 4 events. Crisis priority modifier applies. |
| Read/Appraise actions | Augmented per §7.1. Memory salience floor on referenced Memories. |
| Knot system | Augmented. 100% ambient probability for Knot partners; automatic Concern surfacing per season. |
| Factional Exposure | Augmented with Loyalty Cover bonus. Probabilistic detection (existing). |

---

### 8.1 NPC Standing Recalculation (Campaign Year boundary — PATCH 3.11 / R-40-A; refined PATCH v1.2-1, v1.2-11, v1.2-29)

At end of each Campaign Year (4 Accountings = 1 calendar year), each Active NPC's Standing is recalculated:

```
Δ_standing = (
    +0.5 × completed_projects_this_year
    -0.5 × failed_projects_this_year
    +0.25 × successful_da_proposals_this_year (max +1.0/year)
        # successful = won inner-circle competition AND DA roll succeeded
    -0.25 × failed_da_proposals_this_year (max -1.0/year)
        # failed = won inner-circle competition AND DA roll FAILED
        # (lost competitions do NOT count — they only increment seasons_stalled)
    -0.5 × public_conviction_scars_this_year
)
Δ_standing = clamp(Δ_standing, -2, +2)
npc.standing = round_half_to_even(clamp(npc.standing + Δ_standing, 3, 7))
```

**Counter scope (PATCH v1.2-1 / SIM-B-G8 strict definition):** Mood-suppressed proposals (Distracted high-deference `continue`; Grieving Spirit-check fail) do NOT increment any counter. Lost inner-circle competitions do NOT count as `failed_da_proposals` — they increment `seasons_stalled` only (see §6.2 Procedure C). Failed-deference checks during Conviction-aligned displacement do NOT count as `failed_da_proposals` — they produce a separate `displacement_neglect_observed` event (see §6.2 PATCH 3.5 / PATCH v1.2-9). Strict interpretation rewards execution rather than competition outcome; validated at scale by SIM-E Sc 2 and SIM-D Sc 6.

**Counter state (PATCH v1.2-11 / SIM-B-G7):** Each NPC maintains:

```
npc.year_counters = {
    completed_projects: 0,
    failed_projects: 0,
    successful_da_proposals: 0,
    failed_da_proposals: 0,
    public_conviction_scars: 0,
}
```

Counters increment during the Year on the appropriate events. They reset to zero at end of Standing recalc (after Δ_standing computed and applied). Counters are tracked per-NPC and are not visible to other NPCs (internal Standing-evaluation only).

**Rounding semantics (PATCH v1.2-29 / SIM-B-G6):** `round_half_to_even` (banker's rounding) used explicitly for determinism. E.g., 4.5 → 4; 5.5 → 6.

If `npc.standing` drops below 3 (rounded), NPC exits inner circle (becomes peripheral). If `npc.standing` rises above 7, capped at 7.

A Standing change triggers an event (`event_type: "standing_change"`) which propagates through the standard Event Impact Matrix; inner-circle NPCs receive Memories about the rising/falling colleague.

**Knock-on:** Faction Meta-Armature recomputation reflects shifted Standing weights. Inner-circle composition can change over campaign — a once-S5 NPC may drop to S2 (peripheral); a once-S4 may rise to S5 (inner circle). This is intended.

The Standing ladder row in this section is augmented: **Standing recalculates each Campaign Year based on prior-year activity per §8.1 above.**

Annual cadence (not per-Accounting) prevents Standing from being whippy; the changes accumulate and resolve at narrative milestones.

### 8.2 Inter-Faction War State (PATCH v1.2-22 / SIM-H-G6)

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
- Cross-faction Settlement Signals carry war-context tag (military events at borders amplify by 1.3×).
- Cross-faction Knots experience Disposition penalty (-0.2 per Accounting; sustained war risks Knot rupture per §2.5.2).
- DA Proposal Phase favors military proposals in both factions (`war_state` flag adds +0.1 to military-domain alignment scores).
- Population_disposition in border settlements drifts negative for whichever faction is perceived as aggressor.

**Peace mechanism:** see §8.2.1.

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
        duration=terms.duration,
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

**Treaty terms** (authored content per scenario): may include border adjustments, trade provisions, Knot exchanges (royal marriages), tribute, hostage arrangements. Terms structured as a list of Conviction-aligned-or-contradicted commitments — each faction's meta-armature evaluates whether terms are acceptable.

**Treaty violation:** if a faction takes action contradicting treaty terms, generates high-salience contradiction Memory in opposing faction's leadership; can re-trigger war_state via existing dynamics.

---

## §9 COMPUTATIONAL CHARACTERISTICS

**Per-Accounting estimated work:**

| Operation | Count | Cost per | Total |
|---|---|---|---|
| Event Impact Matrix | ~5 events | ~100 lookups | ~500 lookups |
| NPC armature interpretation | up to 35 Active NPCs × ~5 events | ~50 lookups | ~8,750 lookups |
| Settlement Meta-Armature | ~3-5 settlements per affected event | weighted average | ~15-25 computations |
| Faction Meta-Armature | ~7 factions per affected event | weighted average | ~35 computations |
| Procedure E ambient | ~63 inner-circle pairs × 60% | small | ~38 interactions |
| Procedure E Distant Contact | ~10 cross-faction pairs × 10% | small | ~1 interaction |
| Domain Action proposal | up to 1 per Active NPC | ~30 lookups | ~1,000 lookups |
| Inner-circle competition | per proposal pair | comparison | rare |

**Storage per NPC:**
- Active: ~3KB
- Passive: ~500 bytes  
- Total state: ~150KB for full campaign

**Honest position:** These are estimates without profiling. Actual costs require implementation-stage measurement. Recommended stage-gated implementation:

1. Stage 1: Per-NPC inner state + three-dimension armature + Event Impact Matrix
2. Stage 2: Add Procedure E (off-screen interactions, Gossip)
3. Stage 3: Add Settlement and Faction Meta-Armatures
4. Stage 4: Add Domain Action proposal mechanism
5. Stage 5: Add long-run mechanisms (Memory salience floors, calcification, Project legacy)

Profile at each stage. Each stage produces a working partial system that can be tested independently.

---

## §10 CONTENT AUTHORING REQUIREMENTS

| Item | Count | Notes |
|---|---|---|
| Conviction → armature weights | 105 | 7 Convictions × 3 dimensions × 5 options |
| Personality → armature modifiers | 12 | 4 personality dims × 3 armature dimensions |
| Event dimension profiles | ~270 | 30 event types × 3 dimensions × 3 options avg |
| Sentence frame templates | ~15 | Agency × Mechanism × Intent combinations |
| Domain × Conviction alignment table | 42+ | 6+ Project domains × 7 Convictions (PATCH 2.1) |
| visible_actions templates per domain | ~80 | ~10 actions × 8 domains (PATCH 3.14 / NS-49-A) |
| Authored project queue per Active NPC | 35-105 | 1-3 follow-ups per NPC, optional (PATCH 3.13 / S-46-A) |
| Goal text templates per domain | ~30 | ~5 templates × 6 domains (PATCH 3.13) |
| Conviction × event symbolic resonance table | 210 | 7 Convictions × 30 event types (single-cell ratings) |
| Settlement institutional character bias | 6 | Per settlement type |
| Faction institutional_stability values | 7 | One per faction |
| Domain Action sponsor mapping | ~30 | Per faction |
| Starting Projects per Active NPC | 35 | 1 per Active NPC at game start |
| Personality dimension calibration | ~140 | 4 dims × 35 Active NPCs |
| Starting Opinions, NPC-NPC | ~200 (recommended) | Inner-circle pairs only; let others form dynamically |
| Knowledge seeding | ~100 (recommended) | Most info-rich NPCs only (~10 NPCs at 5-10 facts) |
| Knot integration dialogue fragments | ~30 | Per Concern surfacing variant |
| Gossip text templates | ~30 (recommended) | High-frequency event types initially |

**Total: ~1,190 entries** (or ~700-800 with reductions on Knowledge, Opinions, Gossip).

---

## §11 OUTSTANDING DESIGN DECISIONS

Before implementation:

1. **Wrong-Belief Investigation interaction:**
   - Option A (forgiving): Investigations from wrong Beliefs pause pending player evidence submission
   - Option B (harsh): Wrong Beliefs fire consequences at normal speed
   - **Recommendation:** Option B per Ω-d (every action pays what it buys)

2. **Authoring scope:**
   - Full ~1,190 entries vs reduced ~700-800
   - Determines what's authored vs left to dynamic generation

3. **Carryover decisions** (from prior sessions):
   - Restoring Intelligence as 6th faction stat
   - LICENSE / GOV-08 decision

---

## §12 TESTING PROTOCOL

Recommended test sequence before promotion to canonical:

### 12.1 Unit Tests

- Per-NPC armature derivation from Identity (verify weights computed correctly)
- Concern generation and resolution paths (with and without matching Memories)
- Mood transition table coverage
- Event Impact Matrix construction
- Settlement Signal aggregation
- Cascade attenuation arithmetic

### 12.2 Integration Tests

- Single event propagating through all five layers (per T-1 in stress test document)
- Domain Action proposal competition with conflicting NPCs
- Faction Meta-Armature behavior under inner-circle Conviction divergence
- Knowledge propagation chain (originator → 2 hops, verify decay stops at threshold)

### 12.3 Stress Tests (re-run from 10_stress_tests_all_modalities.md)

- Cascade depth (verify ×0.7 decay terminates propagation appropriately)
- Simultaneous crisis (5+ events) handling
- Long-run temporal (Year 15 Memory state, calcified Beliefs)
- Adversarial player (systematic Insinuate farming) anomaly detection
- Mass Distraction (faction crisis threshold)
- Weight normalization (sparse settlements)
- Discrete event boundary enforcement (affect_axis clamp)
- Collapsed faction city-state Domain Actions
- Loyalty Cover under cross-faction operations

### 12.4 Simulation Tests

Before implementation:
- Simulate ~10 game-years across 3-5 player archetypes
- Verify computational budget assumptions
- Verify content authoring is sufficient (sparse content produces thin behavior; identify gaps)
- Verify emergent narrative quality (do interesting political situations arise?)

### 12.5 Playtest Tests

After Stage 3 implementation (basic political dynamics functional):
- Do players notice Gossip propagation, or does it feel like ambient noise?
- Does Witness Mode produce dramatic context or information overload?
- Do NPC Outreach scenes feel character-driven or scripted?
- Do Domain Action proposals from inner-circle NPCs feel meaningful?

---

## §13 PROMOTION CHECKLIST

To promote from PROVISIONAL to canonical:

- [ ] Re-vetting against current spec (the Class A vetting in 07 was pre-streamlining)
- [ ] All Outstanding Design Decisions in §11 resolved
- [ ] Editorial ledger entries (ED-XXX) for each major component
- [ ] Patch register entries (PP-XXX) with full vetting blocks
- [ ] Integration patches drafted against:
  - `designs/npcs/npc_behavior_v30.md`
  - `designs/architecture/player_agency_v30.md`
  - `designs/territory/settlement_layer_v30.md`
- [ ] Content authoring scope agreed
- [ ] Stage-1 simulation pass demonstrating viable basic behavior

---

## §15 PRIORITY-3 STUB RESOLUTIONS (per `17_specification_revisions.md` §4)

These are addressed at implementation time. The proposed answer for each is recorded below; full patch text is deferred to the implementation revision pass.

### 15.1 Tie-breaking and ordering (ST-13-A/B, ST-14-A/B, ST-17-A, ST-18-A, ST-30-A)
Where two or more entries tie in priority/salience, resolve in stable order: (1) NPC `id` ascending, (2) `created_timestamp` ascending, (3) string `tag` lexicographic. This applies to Concern ordering, Memory tie-breaks for replacement, DA Proposal Phase ties (after Standing and seasons_stalled), and event affected_npcs iteration. `[P3-RESOLVED-PER-DOC17-§4.1]`.

### 15.2 Threshold definitions (ST-22-A, ST-29-A/B, N-LAT-A, N-LAT-B, E-47-A/B, N-34-A)
Concrete numeric thresholds: Concern force-resolution at `salience ≥ 5 AND ttl ≤ 1`; Standing 5 inner-circle threshold uses `>= 4` (existing); high-salience event bypass at `≥ 4` (PATCH 3.1); calcified Belief at `unchallenged ≥ 8 seasons`; Path B Memory threshold at `2 contradicting Memories at salience ≥ 3` (existing). `[P3-RESOLVED-PER-DOC17-§4.2]`.

### 15.3 Search and gating (ST-27-A, ST-28-A, ST-31-A, N-HORIZ-A)
Memory.subject_npc_id null-safe access via `.get()` style; cross-faction Distant Contact gated by `prior Memory exists AND mutual Opinion |≥1|` (existing — verify); Procedure E gossip propagation gate at `cumulative_drift > 0.5`; Knowledge contradicts Belief check uses tag-based domain matching. `[P3-RESOLVED-PER-DOC17-§4.3]`.

### 15.4 Cascade and propagation (ST-21-A, ST-21-B, E-VERT-A, S-DIAG-A, S-VERT-A, S-43-A)
Settlement Signal cascade decay = ×0.7 per scale crossing (existing in PATCH 2.5); Faction Concern-from-Settlement uses Signal salience directly (no further amplification); event vertical propagation (settlement → faction → peninsula) decays ×0.7 per step; faction-to-peninsula propagation only fires for events tagged `peninsula_relevant`. `[P3-RESOLVED-PER-DOC17-§4.4]`.

### 15.5 Documentation gaps (ST-25-C, ST-26-B, S-45-A/B, N-DIAG-B, R-LAT-A, R-DIAG-A)
Documented in this v1.1 doc inline (gaps noted as `[P3-RESOLVED-PER-DOC17-§4.5]` markers in source where pertinent); broader documentation pass at v1.2.

### 15.6 Friction items (N-TOP-A, N-BOT-A, N-BOT-B, E-LAT-A, R-BOT-A, N-HORIZ-B)
Non-blocking friction observations from stress tests; addressed by playtest tuning rather than spec change. Recorded in editorial ledger ED-753. `[P3-RESOLVED-PER-DOC17-§4.6]`.

### 15.7 Cross-references
Several P3 items resolved in P1/P2 patches: ST-32-A (single-writer Opinion, PATCH 1.4-1.6), S-44-A (Settlement Signal scope, PATCH 2.5), and others. See `17_specification_revisions.md` §4.7 for full cross-reference inventory.

---

## §16 PENDING JORDAN-DECISION ITEMS (`[JORDAN-DECISION-PENDING-ED-755]`)

The following items from `17_specification_revisions.md` §6 require Jordan's design call before being applied to v1.2. Default recommendations from doc 17 are stated but **not** applied here. v1.1 operates with the existing v1.0 behavior on these axes; v1.2 will apply whichever resolution Jordan selects.

### 16.1 `[JORDAN-DECISION-PENDING-ED-755]` — E-38-A/B `symbolic_effects` & 210-entry resonance table
**Question:** Keep+define `symbolic_effects` consumption with the 210-entry Conviction × event resonance table, or cut the table entirely and rely on category fallback (PATCH 2.7) only? **Doc 17 default:** KEEP+define. **v1.1 behavior:** unchanged from v1.0 (table referenced but consumption not specified); PATCH 2.7 fallback active so unknown event_types don't crash.

### 16.2 `[JORDAN-DECISION-PENDING-ED-755]` — E-TOP-A opacity stance
**Question:** Faction-top behavior opaque-by-design or legible-by-design? **Doc 17 default:** opaque (factions have inscrutable internal logic; players see surfaces, not roots). **v1.1 behavior:** existing default is opaque (status quo).

### 16.3 `[JORDAN-DECISION-PENDING-ED-755]` — ST-31-B NPC self-monitoring
**Question:** Do NPCs introspect their own Standing/Conviction state for self-aware behavior? **Doc 17 default:** B = no (NPCs do not introspect; behavior is mechanism-driven). **v1.1 behavior:** existing default is no introspection.

### 16.4 `[JORDAN-DECISION-PENDING-ED-755]` — R-41-A crisis masking persistence
**Question:** Does crisis-masking behavior persist across Accountings under sustained crisis, or reset each Accounting? **Doc 17 default:** B = accept (mask persists). **v1.1 behavior:** existing per-Accounting reset.

### 16.5 `[JORDAN-DECISION-PENDING-ED-755]` — Carryover from prior sessions
- Intelligence as 6th faction stat (last touched ED-748 — marked struck per `canonical_definitive_r2`; confirm before reintroduction).
- LICENSE/GOV-08 status (status carryover; needs verification).
- §1.1 Knot Formation During Play (scope question; existing Knot system handles formation, but campaign-time formation specification incomplete).
- §1.2 Accord Propagation to Settlement Order (specification incomplete).

---

## §14 REFERENCE: Stage Documents in This Session

For design history and reasoning, see `designs/audit/2026-04-28-political-dynamics-session/`:

| # | Document | Purpose | Status |
|---|---|---|---|
| 00 | session_index.md | Session overview | Current (updated alongside this spec) |
| 01 | interpersonal_audit.md | 8-gap audit | Foundational; gaps still valid |
| 02 | initial_proposals_with_historical_precedents.md | Renaissance/Ottoman/Byzantine research | Historical research preserved |
| 03 | revision_directionality_emergence.md | RP-balance system attempt | Superseded; reasoning preserved |
| 04 | autonomous_actors_philosophical_reframe.md | Conceptual pivot to autonomous-actor framing | Foundational |
| 05 | groundup_mechanical_proposal.md | First mechanical specification | Superseded by iterative + streamlining |
| 06 | iterative_test_audit_patch_critique.md | 3 iterations of test/audit/patch | Reasoning preserved; specifics superseded |
| 07 | armature_system_vetting.md | Class A vetting | Vetting outcome valid; needs re-vetting against current spec |
| 08 | event_matrix_meta_armatures.md | Architectural addition | Concepts current; specifics updated in 09/10 |
| 09 | integration_test_streamlined.md | Streamlining pass | Specifications integrated into this document |
| 10 | stress_tests_all_modalities.md | 17 issues found, 16 patched | Patches integrated into this document |
| 11 | top_down_audit.md | Holistic audit | Findings drove this consolidation |

**This document (12_development_specification.md) is the current source of truth** for the political dynamics system. Stage documents 01-11 are preserved for design history; their specific mechanisms may have been superseded.

---

## §17 v1.2 PATCH ADDENDUM (consolidated P2/P3 clarifications)

Patches v1.2-1 through v1.2-4 (P1-CRITICAL + ED-760 stall-escalator) and v1.2-18, v1.2-19, v1.2-20, v1.2-21, v1.2-22, v1.2-23, v1.2-35 are applied surgically in their target sections (§2.5.2 Knot Rupture, §5.2 Settlement Signal routing, §5.3 Mood-impact aggregate weighting, §5.4.1 Faction Succession, §5.4.2 Coup Mechanic, §8.1 Standing Recalc strict definition + counter state, §8.2 War State, §8.2.1 Peace Treaty, §1.1 Featured Behaviors rename + Knot Rupture entry).

The remaining P2/P3 patches are consolidated here for reference. Each acts as a clarifying note; readers should interpret the indicated section accordingly. Authoritative for v1.2.

### 17.1 P2 Implementation-Determinism Clarifications

**PATCH v1.2-5 (SIM-A-G1) — Drift coefficients in §3.6.** Define drift coefficients explicitly:
- `base_drift = 0.3`
- `small_drift_coefficient = 0.3` (for confidence-aligned drift)
- `larger_drift_coefficient = 1.0` (for confidence-contradicting drift at low confidence)

**PATCH v1.2-6 (SIM-A-G2) — Drift loop iteration order in §6.2 Procedure D.** Iterate `new_memories` chronologically by timestamp; ties broken by salience descending.

**PATCH v1.2-7 (SIM-A-G3) — `weighted_select()` re-roll-and-average semantics in §3.6.X Armature Confidence.** At confidence < 0.7, sample twice per dimension. If samples agree, use that result. If they disagree, randomly choose one (over many calls, produces 50/50 split between sampled options). Produces interpretation variance — intended behavior of "frame absent."

**PATCH v1.2-9 (SIM-B-G2) — Failed-deference accounting in §6.2 DA Proposal Phase.** On displacement-deference-check failure: generates `displacement_neglect_observed` event (visibility=semi-public to faction leader); does NOT count as `failed_da_proposal` for Standing recalc. The proposal succeeded; only the deference check failed.

**PATCH v1.2-10 (SIM-B-G3) — `seasons_stalled` increment on non-proposal in §6.2 Procedure C.** If `project.progress` unchanged this season, `project.seasons_stalled += 1` regardless of cause: lost competition, Mood-suppression (Grieving Spirit-fail or Distracted high-deference suppression), no DA proposal made, etc. Stall reflects absence of progress, not specifically competitive failure.

**PATCH v1.2-13 (SIM-C-G3) — `interpret_event_affect()` algorithm in §5.2.** Maps event affect to armature-aligned interpretation: `return event.affect * (1 + 0.3 * armature_alignment_with_event_category(armature, event.event_type))`. Aligned events appear ~1.3× their nominal affect through this armature; contradicted events ~0.7×.

**PATCH v1.2-14 (SIM-C-G7) — `recent_event_delta` event-log infrastructure in §5.1.** Each settlement maintains `settlement.faction_event_history[faction] = [(season, delta, event_type), ...]`, capped at last 8 seasons (older entries dropped). Updated each Accounting by faction-governance-impact events. The `recent_event_delta` formula reads from this list with exponential decay (×0.7^seasons_ago).

**PATCH v1.2-16 (SIM-D-G2) — P2-evasion event handling in §7.6 NPC Outreach Generation.** When the player ignores a Priority 2 mandatory Outreach scene entirely (refuses attendance, sacrifices all other Slate slots), the engine spawns an `evasion_observed` event (visibility=semi-public to outreach_npc, salience=4). Consequences: outreach_npc generates a new Concern at salience+1 vs the original Concern (tag: `player_evading_<original_concern_domain>`); outreach_npc.mood may shift to Anxious or Distracted; Memory generated with affect -2. Mandatory P2 evasion produces accelerating relational damage rather than indefinite deferral.

**PATCH v1.2-17 (SIM-D-G5) — Memory-add edge case in §2.6 / PATCH 3.15.** Drop existing-lowest-salience Memory only if the new Memory's salience is at least as high as the existing minimum. If the new Memory's salience is strictly lower than `min(existing.salience)`, refuse to add the new Memory. Exception: if same-tag existing Memory exists, merge per Rule 1 regardless of salience comparison.

### 17.2 P3 Minor Cleanups

**PATCH v1.2-24 (SIM-A-G4) — `knowledge_contradicts_belief()` content-authoring helper in §2.7.** Define as tag-based domain matching using authored Belief-domain tags (specific implementation deferred to authoring stage; mechanism is straightforward tag-set intersection).

**PATCH v1.2-25 (SIM-A-G5) — `evidence_memory_refs` write timing in §6.2 Procedure D.** Update happens after drift application completes for the Memory. Order: apply drift → append memory_id to `evidence_memory_refs`.

**PATCH v1.2-26 (SIM-A-G6) — Confidence boundary standardization throughout §6.2 Procedure D.** Use `< 3` consistently (i.e., 1 or 2 = weak/low confidence; 3+ = strong). Replace any "<= 2" or ">= 3" inconsistencies in spec text.

**PATCH v1.2-27 (SIM-B-G4) — `generate_goal_from_template()` content scope in §10.** Add row to authoring requirements: "Goal text templates per domain | ~30 entries | params/project_goal_templates.md, 5 templates × 6 domains."

**PATCH v1.2-28 (SIM-B-G5) — Per-domain helpers in §10.** Add row to authoring requirements: `standard_effect_for()` and `domain_action_required_for()` per-domain authored constants in `params/project_domain_effects.md`.

**PATCH v1.2-30 (SIM-B-G9) — Mood-suppressed proposal accounting in §6.2.** Mood-suppressed proposals (Distracted high-deference `continue`, Grieving Spirit-fail) do NOT increment any Year-counter for Standing recalc. Non-events for accounting purposes. (Note: this is also reflected in §8.1 PATCH v1.2-1 Counter scope clause.)

**PATCH v1.2-31 (SIM-C-G4) — Salience-0 Memory lifecycle in §2.6.** Salience-0 Memories are eligible to be dropped on next replacement check; effectively pending-replacement until cap pressure forces them out.

**PATCH v1.2-32 (SIM-C-G5) — `categorize_event_type()` inverse-lookup in §4.5.** Build inverse dict at engine init: `CATEGORY_LOOKUP = {event_type: category for category, types in EVENT_CATEGORIES.items() for event_type in types}`. Used by `resonance_lookup()` fallback per PATCH 2.7.

**PATCH v1.2-33 (SIM-D-G1) — Concern dissipation `implied_affect` default in §6.2 Procedure B Resolution.** When Concern dissipates without engagement (decay-to-0 with no resolution event), generate Memory with `event_type='concern_dissipated_without_engagement'`, `affect=-0.5`, `salience=concern.salience` (at dissipation). Reflects mild negative reading from NPC's perspective ("their question went unanswered").

**PATCH v1.2-34 (SIM-D-G3) — PATCH 3.6 + PATCH 3.10 interaction for Knot Concerns in §7.6.** PATCH 3.6 (Knot Outreach P2 mandatory) supersedes PATCH 3.10 (P3 default) for Knot-partner Concerns about player. Knot Outreach is always P2 mandatory regardless of salience-5 escalation rule. (Note: post-rupture per §2.5.2, Knot Outreach no longer fires; rupture severs the bond.)

**PATCH v1.2-36 (SIM-D-G6) — Merge tie-break in §2.6 / PATCH 3.15.** When multiple existing Memories qualify for merge (same tag, same affect-direction), select most-recent (highest timestamp). Reasoning: newer event tends to be the "current" framing for the pattern.

**PATCH v1.2-38 (SIM-H-G1) — Subversive-intent dialogue interpretation in §10.** Scene templates expose explicit affect-direction tagging for each dialogue branch. Subversive-intent dialogue branches are tagged with negative-affect-direction; supportive branches with positive. Scene authoring distinguishes *what the player chooses to express* from the mechanical Memory affect produced. See `params/scene_templates.md`.

### 17.3 v1.2 Application Audit

**Applied surgically (in target sections):**
- PATCH v1.2-1 (§8.1): failed_da_proposals strict definition.
- PATCH v1.2-2 (§5.2): Settlement-Signal-Concern three-tier routing.
- PATCH v1.2-3 (§2.5.2 + §1.1): Knot rupture mechanic + featured behavior.
- PATCH v1.2-4 (§6.2): stall-escalator in select_proposal score.
- PATCH v1.2-8 (§6.2): 4th-level tie-break in select_proposal.
- PATCH v1.2-11 (§8.1): Standing recalc counter state.
- PATCH v1.2-12 (§5.2): Signal salience handling.
- PATCH v1.2-15 (§5.2): repeated-Signal max-update on active Concern.
- PATCH v1.2-18 (§5.3): Mood-impact on aggregate weighting.
- PATCH v1.2-19 (§5.4.1): faction succession.
- PATCH v1.2-20 (§5.4.2): leader challenge / coup mechanic.
- PATCH v1.2-21 (§5.4): Faction Crisis resolution paths.
- PATCH v1.2-22 (§8.2): war state mechanic.
- PATCH v1.2-23 (§8.2.1): peace treaty mechanic.
- PATCH v1.2-29 (§8.1): banker's rounding clarification.
- PATCH v1.2-35 (§1.1): N-DIAG-A title rename.
- PATCH v1.2-37 (§5.2): cross-border event Signal-attribution.
- PATCH v1.2-39 (§5.4): cross-faction event during simultaneous crises.

**Applied as addendum clarifications (this §15):**
- PATCH v1.2-5, -6, -7, -9, -10, -13, -14, -16, -17 (P2 implementation-determinism).
- PATCH v1.2-24, -25, -26, -27, -28, -30, -31, -32, -33, -34, -36, -38 (P3 minor cleanups).

All 39 v1.2 patches are present in this document. See `21_v1_2_specification_revisions.md` for full patch directives and rationale; see `19_v1_1_validation_report.md` for the simulation-evidence base supporting each patch.

---

*(See §14 above for stage-document references and §13 for Promotion Checklist.)*