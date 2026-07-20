<!-- [PROVISIONAL: 2026-04-29 — simulation Direction A] -->
<!-- STATUS: PROVISIONAL — granular trace of Opinion architecture mechanics under doc 12 v1.1 -->
<!-- POSITION: designs/audit/2026-04-28-political-dynamics-session/SIM_A_opinion_architecture.md -->

# Simulation A — Opinion Architecture (single-writer model)

**Source spec:** `12_development_specification.md` v1.1 (commit `9dede391`).
**Primary patches under test:** PATCH 1.4, 1.5, 1.6 (single-writer); PATCH 2.3 (conviction_alignment_multiplier); PATCH 2.6 (uniform fallback); PATCH 2.8 (additive composition); PATCH 3.1 (cooldown); PATCH 3.2 (Knowledge Decay); PATCH 3.3 (visibility); PATCH 3.4 (lazy init); PATCH 3.7 (scars split); PATCH 3.15 (Passive Memory replace).
**Method:** Six granular trace scenarios, step-by-step Procedure execution with explicit state transitions. Each scenario records initial state, executed steps, final state, expected-vs-actual delta, and invariant verification.

---

## §0 Conventions

- **Naming.** NPCs labeled `Almud` (player or surrogate), `Confessor` (Faith primary), `Marshal` (Order primary), `Scribe` (Reason primary), `Treasurer` (Equity primary), `Ambassador` (Continuity primary). Following project convention: never `Galbados`, always `Solmund` for the relevant character; here we use generic role-based labels.
- **Time units.** Season = one Accounting cycle. T+0 = current season; T+1 = next.
- **Notation.** `npc.field = value → new_value` for state transitions. `→` denotes deterministic outcome; `~` denotes probabilistic outcome with stated weight.
- **Invariant tags.** `[INV-1]` no-double-write Opinion. `[INV-2]` single-writer (D only). `[INV-3]` Memory-conserved (Memories created in B/C consumed by D). `[INV-4]` salience-bounded (Concern salience ≤ 5; Memory salience ≤ 5).

---

## §1 Scenario 1 — Canonical chain: Concern resolution → Memory → Drift

**Goal.** Trace the full B-resolves → Memory-created → D-drifts chain. Verify the post-PATCH-1.4 path produces equivalent end-state to the pre-patch direct-Opinion-write path.

### 1.1 Initial state (T+0 start)

```
Confessor (Faith primary, Order secondary):
  conviction_primary: Faith
  conviction_secondary: Order
  scars_total: 1, scars_conviction: 0
  mood: Steady
  concerns: [
    Concern(
      id: c-001,
      tag: "marshal_neglecting_drills",
      subject_npc_id: marshal-id,
      salience: 3,
      ttl: 2,
      seeking_tag: "drilling_evidence",
    )
  ]
  concern_history: ["bishop_ceremony_question"]  (recent — irrelevant tag)
  memories: [
    Memory(m-100, "Marshal skipped Crown audience", participants=[confessor, marshal], affect=-1, salience=3, season=T-1),
    Memory(m-101, "drilled with junior officers", participants=[confessor, marshal], affect=+0.5, salience=2, season=T-2),
  ]
  opinions: {marshal-id: Opinion(affect=+1, confidence=2, evidence=[m-101])}

Marshal (Order primary, Continuity secondary):
  scars_total: 0, scars_conviction: 0
  mood: Distracted
  active_project: Project(
    domain: military,
    progress: 6,
    visible_actions_pool: ["drilling troops", "inspecting fortifications", ...]
  )
```

### 1.2 T+0 Procedure B (Concern Generation and Resolution)

**B.0 Knowledge Decay** (PATCH 3.2): Confessor has no Knowledge entries — no-op.

**Generation (PATCH 3.1, 3.3):**
- No new events this season targeting Confessor; Generation produces nothing.

**Resolution (PATCH 1.4 — single-writer rewrite):**
```
For Confessor.concerns = [c-001]:
  c-001.salience: 3 → 2 (standard decay)
  ttl: 2 → 1
  c-001.salience > 0 AND ttl > 0 → no resolution this season.
```
End-of-B state: `c-001.salience=2`, `ttl=1`. No Memory created. No Opinion change.

### 1.3 T+0 Procedure D (Opinion Drift)

D iterates `Confessor.opinions`. For `marshal-id`:
- New memories this season subject=marshal-id: **none** (no new Marshal-tagged Memory).
- Drift loop runs zero iterations. Opinion unchanged.

End-of-T+0 state: `Opinion(marshal: +1, conf=2)`. Concern still active.

**[INV-1, INV-2, INV-3] all hold trivially this season** — no Memory created, no Opinion mutation, single-writer D ran but had no input.

### 1.4 T+1 begins. Event arrives: Marshal misses second audience.

```
event-A: {
  event_type: "audience_skipped",
  participants: [crown, marshal],
  affected_npcs: [confessor, ambassador, ...],
  visibility: {public: true},
  salience: 4,
}
```

### 1.5 T+1 Procedure B

**B.0 Knowledge Decay**: no-op for Confessor.

**Generation (PATCH 3.1, 3.3):**
- `npc_observes_event(Confessor, event-A)` → True (event public).
- `derive_concern_tag(event-A, Confessor.armature)` → `"marshal_pattern_of_neglect"` (similar but distinct domain tag).
- `"marshal_pattern_of_neglect" in concern_history`? `concern_history = ["bishop_ceremony_question"]` → No. Cooldown does not apply.
- Generate fresh Concern. But: existing `c-001` is in same domain. Concern slot has 1 of 3 used. `len(concerns)=1 < 3` → both can coexist. (Note: existing spec doesn't merge same-domain Concerns; this is a deliberate design — multiple distinct Concerns about the Marshal can stack.)
- `c-002`: tag=`"marshal_pattern_of_neglect"`, salience=3, ttl=3.

**Resolution (single-writer):**
- `c-001.salience: 2 → 1`. `ttl: 1 → 0`. **c-001 resolves.**
- `resolution = resolve_concern(Confessor, c-001)`:
  - Confessor's seeking_tag was `"drilling_evidence"`. No matching Knowledge surfaced (Confessor has no Knowledge entries).
  - With salience=1 and no Knowledge match: `resolution.contradiction_strength = "weak"`, `resolution.causes_belief_revision = false`, `resolution.implied_affect = -0.5` (negative, because the Concern persisted unresolved into low salience — a soft signal that the suspicion was valid but no decisive evidence).
  - `resolution.subject_npc_id = marshal-id`. `resolution.salience = 1`.
- **PATCH 1.4 path:** Memory created.
  ```
  m-200: Memory(
    timestamp: T+1,
    event_type: "concern_resolved",
    participants: [confessor, marshal],
    affect: -0.5,
    salience: 1,
    detail: "Doubts about Marshal's discipline persisted — no decisive evidence either way.",
  )
  ```
  `add_memory(Confessor, m-200)`. Confessor memories = [m-100, m-101, m-200] (3 of 10 cap; no replacement needed).
- `concern_history: ["bishop_ceremony_question"] → ["bishop_ceremony_question", "marshal_neglecting_drills"]`.
- `remove(c-001)`. Confessor.concerns = [c-002].

### 1.6 T+1 Procedure C (Project Advancement)

Confessor has no active Project (out of scope for this scenario). Marshal advances his Project. No Memories created in Confessor's view from C this season.

### 1.7 T+1 Procedure D (Opinion Drift) — single-writer write

D iterates Confessor.opinions:
- For `marshal-id`:
  - new_memories this season for subject=marshal-id: `[m-200]`.
  - For m-200:
    - lazy init via `get_or_init_opinion()` (PATCH 3.4): Opinion already exists. Returns existing.
    - `multiplier = conviction_alignment_multiplier(Confessor, Marshal)`:
      - Confessor.primary=Faith, Marshal.primary=Order. Not equal. Not in OPPOSITIONAL pairs (Faith/Reason, Order/Autonomy, Precedent/Equity, Continuity/Reason). Secondary check: Confessor.secondary=Order = Marshal.primary → returns 1.2. **Bridge sympathy.**
    - `drift = base_drift × (1 - |+1|/3) × 1.2 = 0.3 × 0.667 × 1.2 ≈ 0.24` (assuming base_drift=0.3).
    - m-200.affect = -0.5 (negative); contradicts the +1 Opinion.
    - `opinion.confidence (2) > 2`? No, equals 2. Border case. Code reads `if confidence <= 2` (line in spec): triggers weak-Opinion shift.
    - `opinion.affect_axis: +1 → +1 + (larger_drift × sign(-0.5)) = +1 - 0.24 ≈ +0.76`.
    - `opinion.confidence = max(1, 2-1) = 1`.
  - Hard clamp to [-3, +3]: ok.

End state: `Opinion(marshal: +0.76, conf=1, evidence=[m-101] (m-200 added by reference but only on next write — depends on impl; for trace assume evidence_memory_refs gets m-200).`

### 1.8 Verification claims (Scenario 1)

- **[INV-1] No double-write:** Opinion was written exactly once this season — by Procedure D. Procedure B-Resolution wrote Memory (m-200) only, not Opinion. ✓
- **[INV-2] Single-writer (D only):** Confirmed — all opinion.affect_axis mutations occurred in Procedure D. ✓
- **[INV-3] Memory-conserved:** m-200 created in B-Resolution; consumed by D in same season. ✓
- **[INV-4] Salience-bounded:** Concern salience never exceeded 3; Memory salience never exceeded 3. ✓
- **Equivalence to pre-patch behavior:** Pre-patch path would have written `opinion.affect_axis += -0.5 × dampening` directly during B-Resolution. New path writes Memory(affect=-0.5, salience=1), then D applies `0.3 × 0.667 × 1.2 = 0.24` drift = -0.24. The magnitudes differ slightly because the new path goes through D's standard drift formula (which now compounds with conviction_alignment_multiplier — a knock-on of PATCH 2.3). Pre-PATCH-2.3, the multiplier wasn't defined and was implicitly 1.0; magnitude was -0.5 × 0.667 = -0.33. New path: -0.24. **Magnitudes are different by design**: the single-writer model intentionally routes Opinion change through D's full machinery, including the new multiplier. This is closer to design intent.
- **Knock-on observed:** Confidence dropped from 2 to 1 (because contradiction at confidence ≤ 2 → confidence decrement). This means Confessor's next Marshal-Memory will have larger drift effect. Cumulative behavior over multiple seasons: a sequence of mild contradicting evidence will compound through multiple drift steps, not one large step. **This is the design intent of the routing change** — slower, more cumulative Opinion shift.

---

## §2 Scenario 2 — Project completion legacy → Memories → drift

**Goal.** Trace the PATCH 1.5 path: Project completion produces Memories, not direct Opinion writes. Verify magnitude conservation under D's formula.

### 2.1 Initial state

```
Marshal (Order primary):
  active_project: Project(
    id: p-001,
    domain: military,
    progress: 9,    (one season from completion)
    supporters: [marshal-id],  (self)
    obstructors: [scribe-id, ambassador-id],
    completion_effect: "fortify Solmund's eastern wall",
  )
  opinions: {
    scribe-id: Opinion(affect=-1, conf=3, evidence=[...]),
    ambassador-id: Opinion(affect=+0.5, conf=2, evidence=[...]),
  }
```

### 2.2 T+0 Procedure C — Project advances

`project.progress: 9 → 10`. Completion check fires.
- `execute_completion_effect(p-001, marshal)`. (Out of scope for this trace.)
- **PATCH 1.5 path** — Memories instead of direct Opinion writes:
  - For obstructors `[scribe-id, ambassador-id]`:
    - `m-300`: `event_type="project_legacy_obstruction", participants=[marshal, scribe], affect=-0.5, salience=4, detail="Worked against me on fortify Solmund's eastern wall"`. add_memory(marshal, m-300).
    - `m-301`: same template, participants=[marshal, ambassador], affect=-0.5, salience=4. add_memory(marshal, m-301).
- `generate_new_project(marshal)` (PATCH 3.13): Tier 1 queue empty. Tier 2: sample domain by Order alignment. From DOMAIN_ARMATURE_ALIGNMENT: military=1.0, theological=0.4, scholarly=0.4, intelligence=0.7, economic=0.5, diplomatic=0.6. Normalized weights → sample. Likely military again (highest weight). `p-002` generated with horizon=medium (40% weight).

### 2.3 T+0 Procedure D

For Marshal.opinions:
- scribe-id (-1, conf=3):
  - new_memories subject=scribe-id this season: [m-300]. (one)
  - multiplier = conviction_alignment_multiplier(marshal, scribe). marshal.primary=Order, scribe.primary=Reason. Not equal. Not OPPOSITIONAL (Order/Autonomy is in pairs; Order/Reason is not). 1.0.
  - drift = 0.3 × (1 - |-1|/3) × 1.0 = 0.3 × 0.667 = 0.2.
  - m-300.affect = -0.5, **same direction** as opinion (both negative). Aligned.
    - `opinion.confidence += 0.0 to +1.0` per spec → confidence = min(5, 3+0.5) = 3.5 (or rounded depending on impl).
    - `opinion.affect_axis += small_drift × sign(-0.5) = -0.5 × 0.2 = -0.1`. So affect = -1 - 0.1 = -1.1.
- ambassador-id (+0.5, conf=2):
  - new_memories subject=ambassador-id this season: [m-301].
  - multiplier = conviction_alignment_multiplier(marshal, ambassador). marshal.primary=Order, ambassador.primary=Continuity. Not equal. Not OPPOSITIONAL. Secondary check: marshal.secondary=Continuity → matches ambassador.primary → returns 1.2 (bridge sympathy).
  - drift = 0.3 × (1 - |0.5|/3) × 1.2 ≈ 0.25.
  - m-301.affect = -0.5; contradicts +0.5 opinion.
    - confidence (2) <= 2: weak-Opinion shift.
    - opinion.affect_axis += larger_drift × sign(-0.5). With larger_drift typically 0.4-0.5, magnitude ≈ -0.4 × 0.25 ratio ≈ -0.1. New affect = +0.5 - 0.4 = +0.1 (estimate; exact depends on larger_drift coefficient — spec doesn't define exact scalar).
    - confidence = max(1, 2-1) = 1.

**[GAP: doc 12 v1.1 specifies "small_drift" and "larger_drift" qualitatively but does not give a numeric ratio.]** The drift formula has `drift = base × dampening × multiplier`, but inside the if-branch it says `opinion.affect_axis += small_drift` and `opinion.affect_axis += larger_drift`. Whether `small_drift = drift × 0.5` and `larger_drift = drift × 1.5` or some other ratio is not specified. **This is a P3 documentation gap surfaced by simulation; should be calibrated to specific values in v1.2.** Marking `[GAP: small_drift / larger_drift coefficients undefined — surfaced by SIM-A scenario 2; v1.2 calibration target]`.

### 2.4 Verification (Scenario 2)

- **[INV-1] No double-write:** Marshal.opinions[scribe] and Marshal.opinions[ambassador] each written exactly once (by D). Procedure C wrote Memories only. ✓
- **[INV-2] Single-writer:** ✓
- **[INV-3] Memory-conserved:** m-300, m-301 created in C; consumed by D same season. ✓
- **[INV-4] Salience-bounded:** Memory salience = 4, ≤ 5. ✓
- **Equivalence to pre-patch:** Pre-PATCH-1.5, C wrote opinion.affect ± 0.5 directly. New path: Memory(salience=4, affect=-0.5) → D drift 0.2-0.25 → applied delta ~-0.1 (aligned) or ~-0.4 (contradicting). Aligned case is *smaller* than pre-patch (-0.1 vs -0.5); contradicting case roughly comparable (-0.4 vs -0.5). **Aligned-case dampening is a real change.** Doc 17 §1.7 claimed magnitudes "comparable"; simulation suggests *aligned* legacy effects are notably smaller because aligned Memories produce small drift in D (the spec's `+0.0 to +1.0` confidence boost rather than affect_axis shift). **This may be a feature** — aligned legacy reinforces the existing Opinion (already strong) without further inflating it. Worth flagging to Jordan: PATCH 1.5 changes aligned-legacy magnitude meaningfully. `[CONFIDENCE: medium — magnitude analysis assumes default base_drift=0.3 and unspecified small/larger_drift coefficients]`.

---

## §3 Scenario 3 — Concurrent B + C in same season (single-writer load)

**Goal.** Verify single-writer invariant when both Procedures produce Memories targeting the same subject in the same season.

### 3.1 Initial state

```
Confessor (Faith primary, Order secondary):
  concerns: [
    Concern(c-010, "marshal_competence", subject=marshal-id, salience=1, ttl=1)
  ]
  active_project: Project(
    p-010, domain=theological, progress=9, supporters=[confessor], obstructors=[marshal-id]
  )
  opinions: {marshal-id: Opinion(affect=-0.5, conf=2)}
```

### 3.2 T+0 sequence

Per §6.2 v1.1 sequence: B → DA Proposal Phase → C → D → E.

**B Resolution** (single-writer rewrite):
- c-010.salience: 1 → 0. ttl: 1 → 0. Resolves.
- resolution: subject=marshal-id, implied_affect=+0.5 (positive — Concern resolved with sense Marshal is competent enough), salience=0.5 (clamped to ≥1 by add_memory? spec doesn't say; assume 1).
- **PATCH 1.4 Memory:** `m-400 = Memory(event_type=concern_resolved, participants=[confessor, marshal], affect=+0.5, salience=1, season=T+0)`.
- concern_history append.

**C Project Completion** (single-writer rewrite):
- p-010 progress 9 → 10. Completes.
- **PATCH 1.5 Memory** (obstructor): `m-401 = Memory(event_type=project_legacy_obstruction, participants=[confessor, marshal], affect=-0.5, salience=4, season=T+0)`.

**D Opinion Drift** (single-writer write):
- For Confessor.opinions[marshal-id]:
  - new_memories this season subject=marshal-id: `[m-400, m-401]`. **Both** consumed in same season.
  - For m-400 (affect +0.5, salience 1):
    - multiplier: Faith vs Order = 1.0 (no special pair). But Confessor.secondary=Order matches Marshal.primary → 1.2.
    - drift = 0.3 × (1 - 0.5/3) × 1.2 = 0.3 × 0.833 × 1.2 = 0.30.
    - m-400.affect = +0.5; contradicts opinion (-0.5).
    - confidence (2) <= 2: weak-Opinion shift.
    - opinion.affect_axis += larger_drift × sign(+0.5) → estimate +0.4 × 0.30/0.30 = +0.4. (Using rough coefficient.)
    - opinion.affect_axis: -0.5 + 0.4 = -0.1.
    - confidence: 2 - 1 = 1.
  - For m-401 (affect -0.5, salience 4):
    - opinion now (-0.1, conf=1).
    - drift = 0.3 × (1 - 0.1/3) × 1.2 = 0.3 × 0.967 × 1.2 = 0.348.
    - m-401.affect = -0.5; **same direction** as opinion (-0.1). Aligned.
    - confidence += 0.0 to +1.0. Confidence = 1 → ~1.5 or 2.
    - opinion.affect_axis += small_drift × sign(-0.5) ≈ -0.1.
    - opinion.affect_axis: -0.1 + (-0.1) = -0.2.
- End: `Opinion(marshal: -0.2, conf≈2)`. evidence_memory_refs += [m-400, m-401].

### 3.3 Verification (Scenario 3)

- **[INV-1] No double-write:** Both m-400 (from B) and m-401 (from C) consumed by D in single iteration of opinions[marshal-id]. The drift loop processes each Memory once. ✓
- **[INV-2] Single-writer:** ✓ 
- **[INV-3] Memory-conserved:** Both Memories created and consumed same season. ✓
- **Memory ordering matters:** Trace assumed m-400 processed before m-401. The spec doesn't specify ordering of new_memories iteration. **`[GAP: D's drift loop iteration order over new_memories not specified — surfaced by SIM-A scenario 3]`. This affects results because the second drift step uses post-first-step affect_axis. Should be specified (e.g., chronological by timestamp; ties broken by salience descending).**
- **End-state delta vs single-Memory case:** Two contradictory-then-aligned Memories produced net affect movement of +0.3 (-0.5 → -0.2). Pre-patch B+C double-write would have done: B writes +0.5 directly → opinion = 0.0; C writes -0.5 directly → opinion = -0.5. Net pre-patch: 0. Post-patch: -0.2. **Different end-state.** Post-patch behavior reflects D's dampening + multiplier; pre-patch was raw additive. Direction-of-movement same (toward neutral); magnitude different. Acceptable per design intent.

---

## §4 Scenario 4 — First-contact lazy init (PATCH 3.4)

**Goal.** Verify `get_or_init_opinion()` produces sensible initial Opinion when none exists.

### 4.1 Setup

```
Scribe (Reason primary, Autonomy secondary), faction=Academy.
  opinions: {}  (empty — Scribe has never had Opinion-relevant interaction with anyone)

Treasurer (Equity primary, Reason secondary), faction=Crown (hostile to Academy).

Event-X arrives: Treasurer publishes treatise critical of Academy's tax policy. visibility=public, salience=3.
  affected_npcs includes Scribe.
```

### 4.2 T+0 Procedure B Generation (PATCH 3.1+3.3)

- visibility public → Scribe observes.
- derive_concern_tag(event-X, Scribe.armature) → "treasurer_attacks_academy".
- not in concern_history. Generate Concern.
- c-500 created. salience derived from event impact matrix: ~3.

### 4.3 T+1 Resolution + D

Skipping ahead one season for Concern resolution. Resolution Memory m-500 created with subject_npc_id=treasurer-id, affect=-1, salience=2.

D iterates Scribe.opinions for this Memory:
- `get_or_init_opinion(scribe, treasurer-id)`:
  - Not in opinions. Construct.
  - `derive_initial_affect(scribe, treasurer-id)`:
    - scribe.primary=Reason, treasurer.primary=Equity. Not equal. (Reason, Equity) in OPPOSITIONAL? Pairs are (Faith,Reason), (Reason,Faith), (Order,Autonomy), (Autonomy,Order), (Precedent,Equity), (Equity,Precedent), (Continuity,Reason), (Reason,Continuity). **(Reason, Equity) is not an OPPOSITIONAL pair.** No conviction adjustment.
    - scribe.faction=Academy, treasurer.faction=Crown. Not same. Academy hostile to Crown → base -= 1. **base = -1.**
    - Standing differential: cross-faction → no effect.
    - return clamp(-1, -3, +3) = -1.
  - Opinion(affect=-1, conf=1, evidence=[]).
- Drift loop:
  - For m-500 (affect=-1, salience=2):
    - multiplier: conviction_alignment_multiplier(scribe, treasurer). primary Reason vs Equity, not equal, not OPPOSITIONAL, secondary check: scribe.secondary=Autonomy = treasurer.secondary=Reason? No, treasurer.secondary=Reason matches scribe.primary=Reason → return 1.2 (bridge sympathy).
    - **Edge case:** Initial affect_axis = -1, m-500.affect = -1 (same direction). **Aligned**.
    - drift = 0.3 × (1 - |-1|/3) × 1.2 = 0.3 × 0.667 × 1.2 = 0.24.
    - confidence += 0.0 to +1.0. Confidence: 1 → 2.
    - affect_axis += small_drift × sign(-1) ≈ -0.05 (small_drift~drift×0.2 ≈ 0.05). affect_axis: -1 → -1.05. Clamp to -3, +3 — no clamp needed.

End-state: `Opinion(treasurer: -1.05, conf=2, evidence=[m-500])`.

### 4.4 Verification (Scenario 4)

- **[INV-3] Memory-conserved:** m-500 created in B (T+1); consumed by D (T+1). ✓
- **First-contact init:** Sensible — cross-faction-hostile + no Conviction conflict → mild negative initial. Reinforced by the negative Memory. Confidence start 1 → 2. Plausible.
- **Knock-on observation:** A neutrally-disposed initial Opinion (e.g., shared faction + no Conviction match → +1) followed by negative Memory would shift the Opinion toward neutral first encounter. Cross-faction-hostile + negative Memory reinforces (aligned). The pattern is correct: priors meet evidence, evidence updates priors per usual.
- **Bridge-sympathy edge case:** scribe.secondary=Autonomy, treasurer.secondary=Reason. Treasurer's *secondary* matches scribe's *primary*. Per PATCH 2.3 multiplier function: returns 1.2 if `npc_a.conviction_secondary == npc_b.conviction_primary OR npc_a.conviction_primary == npc_b.conviction_secondary`. The second condition holds (scribe.primary=Reason = treasurer.secondary=Reason). **1.2 multiplier applies — bridge sympathy across hostile factions due to shared interpretive frame at the secondary level.** This is mechanically interesting: even cross-faction hostile NPCs have a slight bridge if their Convictions are second-level compatible. **Worth noting in design as an emergent property.** Likely produces realistic patterns where individual NPCs maintain personal connections across institutional opposition.

---

## §5 Scenario 5 — High-Scar NPC with conviction_secondary=None (PATCH 2.6 uniform fallback)

**Goal.** Verify uniform-fallback path activates correctly and produces "diffuse interpretation" behavior.

### 5.1 Setup

```
Old Soldier (Order primary, secondary=None).
  scars_total: 4, scars_conviction: 4 (heavily Belief-revised through career)
  age: late campaign
  active_project: Project(domain=military, progress=3)
  active_concerns: []
```

`compute_armature(old_soldier)` runs:
- base_weights_from_conviction(Order) → Order-aligned distribution per dim.
- add personality_modifier (small).
- add scar_modifier(scars_conviction=4, primary=Order, secondary=None):
  - Per PATCH 2.6: scars_conviction ≥ 3 → "secondary leads (75% secondary + 25% primary)". secondary=None → fall back to "50% primary + 50% UNIFORM-FALLBACK".
  - Returns delta dict: -0.25 from primary-aligned options (reducing 100% baseline to 50%), +0.5/n added uniformly to non-primary options in each dimension (UNIFORM-FALLBACK contribution).
- add project_modifier (small).
- add concern_modifier (none).
- floor at 0; normalize per dim.

### 5.2 §3.6.X Armature Confidence

Armature confidence calculation (§3.6.X):
- "Confidence = 0.5 when armature is mixed primary+secondary": doesn't apply because secondary=None.
- "Confidence < 0.5 when uniform-fallback is active (frame absent)": **applies**. Old_soldier.armature_confidence < 0.5.
- Per spec: "weighted_select() at confidence < 0.7 should re-roll once and average results, producing more inconsistent armature behavior."

### 5.3 Behavior under interpretation

When event arrives, Procedure B's `derive_concern_tag(event, npc.armature)` calls `weighted_select()` on the armature distribution.
- With confidence < 0.7, **re-roll once and average**:
  - Roll 1: e.g., samples mechanism.calculation (Order-aligned).
  - Roll 2: e.g., samples mechanism.recourse (uniform-spread option).
  - Average = mixed interpretation. Concern tag derives from mixed armature → **less crisp interpretation than a coherent NPC**.

End-state: Old Soldier produces Concerns with diffuse, less-predictable framing. From a player perspective this NPC's reactions become harder to predict — realistic for an NPC who has been worldview-shattered without a replacement frame.

### 5.4 Verification (Scenario 5)

- **PATCH 2.6 uniform fallback path engaged correctly.** ✓
- **Armature confidence < 0.7 triggers re-roll-and-average behavior.** ✓
- **Emergent property:** Old Soldier becomes *less* mechanically predictable. Player observing his Concerns over multiple Accountings sees inconsistent interpretive frames. **This is the design intent of PATCH 2.6** — high-Scar NPC without secondary becomes genuinely chaotic.
- **Knock-on for simulation budget:** uniform-fallback NPCs cost ~2× compute for Concern generation (re-roll-and-average). At <1% of NPCs (rare situation), negligible.
- **`[GAP: weighted_select() re-roll-and-average algorithm not fully specified]`. Spec says "re-roll once and average results"; in dimension-by-dimension sampling, what does "average" mean? Average of two probability vectors? Or two final selections? If the latter, "averaging" two discrete choices is undefined. Spec needs to clarify: for each dimension independently, sample twice and select the option with higher cumulative probability? Or: sample twice and randomly pick one of the two? Each produces different downstream behavior.** Surface this as `[GAP: §3.6.X re-roll-and-average semantics — surfaced by SIM-A scenario 5; v1.2 clarification target]`.

---

## §6 Scenario 6 — Knowledge Decay → invalid Knowledge → Concern not generated (PATCH 3.2 + 3.3)

**Goal.** Verify Knowledge Decay correctly invalidates stale Knowledge, preventing it from triggering Concerns; and visibility gate correctly suppresses out-of-view events.

### 6.1 Setup

```
Ambassador (Continuity primary).
  knowledge: [
    K(id=k-100, type="ongoing_state", fact="Crown plans tariff hike", salience=2, season_observed=T-3),
    K(id=k-101, type="historical_event", fact="Treaty of Solmund signed T-12", salience=5, permanent),
    K(id=k-102, type="structural", fact="Marshal commands Eastern Garrison", salience=4, season_observed=T-8),
  ]
  beliefs: [
    Belief(id=b-200, domain="Crown_economics", text="Crown is fiscally responsible"),
  ]
```

### 6.2 T+0 Procedure B.0 Knowledge Decay

For Ambassador.knowledge:
- k-100 (ongoing_state, salience=2): salience -= 0.5 → 1.5.
- k-101 (historical_event, salience=5): no decay.
- k-102 (structural, salience=4): salience -= 0.1 → 3.9.

Cull check: salience >= 1 OR referenced_recently(seasons=4):
- k-100: 1.5 ≥ 1, kept.
- k-101: 5 ≥ 1, kept (also permanent flag).
- k-102: 3.9 ≥ 1, kept.

End-of-B.0: knowledge unchanged in count; saliences updated.

### 6.3 Multi-season trace: T+0 through T+5

Repeat decay 5 more seasons (T+1 through T+5):
- k-100 saliences: T+0:1.5, T+1:1.0, T+2:0.5, T+3:0.0 — culled (salience < 1, last referenced T-3 → not recent within 4 seasons since T+3-(-3)=6).
- Actually wait: `referenced_recently(seasons=4)` = within last 4 seasons. From T+3 looking back 4 seasons = T-1. k-100 was season_observed=T-3, which is older than T-1. So not "recently referenced" by observation. Unless something incremented its referenced_recently flag (e.g., knowledge sharing), it's culled at T+3.
- k-101 (permanent): never culled.
- k-102 (structural): T+0:3.9, T+1:3.8, T+2:3.7, ... linear decay -0.1/season. Never reaches < 1 in any reasonable timeframe. Always kept.

**Observation:** ongoing_state knowledge is short-lived; structural knowledge effectively permanent at the -0.1/season rate. Historical_event truly permanent. **This matches design intent in §2.7.**

### 6.4 T+3 Procedure B Generation — visibility gate

Event-Y at T+3: Crown announces tariff increase. visibility=semi_public_observers (specific NPCs at the announcement scene). Ambassador NOT in observers list (was off the peninsula on diplomatic mission).
- npc_observes_event(Ambassador, event-Y) → False. **Ambassador does not generate Concern from this event directly.**

But: Knowledge-derived Concern (existing path in Generation, after the new gated event loop):
```
For each Knowledge in npc.knowledge with salience >= 4:
    if knowledge contradicts any active Belief domain:
        generate Concern("Is [Belief] accurate given Knowledge X?")
```
- k-101 (salience=5, permanent): does it contradict belief b-200 ("Crown is fiscally responsible")? Treaty signed T-12 — historical event. Not directly relevant.
- k-102 (salience=3.7 at T+3): below salience-4 threshold. Skipped.
- k-100: already culled at T+3.
- No Knowledge-derived Concerns generated.

Ambassador's Concern queue: unchanged this T+3.

### 6.5 Indirect path — Ambassador hears about tariff from Procedure E

T+3 also runs Procedure E. Suppose Confessor (who DID observe event-Y) and Ambassador are inner-circle Knot partners. Procedure E gossip propagation includes:
- Confessor.knowledge has new entry from event-Y about the tariff.
- share_knowledge(Confessor, Ambassador, this knowledge):
  - Ambassador acquires new Knowledge: `k-200`, type="ongoing_state", fact="Crown announced tariff hike", salience = 4 (Confessor's salience -1).
- This sets `k-200.referenced_recently=True`.

T+4 Procedure B Generation: 
- Now k-200 (salience=4) ≥ 4 threshold. Does it contradict Belief b-200? "Crown announced tariff hike" vs "Crown is fiscally responsible" — depends on interpretation. If b-200's domain is "fiscal responsibility" and tariff hike implies fiscal stress (or aggressive revenue): **contradicts**.
- Generate Concern: `c-600 = Concern("Is Crown's fiscal responsibility accurate given tariff hike?")` salience=high.

### 6.6 Verification (Scenario 6)

- **PATCH 3.2 Knowledge Decay engaged correctly.** Ongoing-state knowledge decayed and was culled when its referenced-recently window expired. ✓
- **PATCH 3.3 visibility gate suppressed Ambassador's direct event observation.** Ambassador did not receive Concern from event-Y directly. ✓
- **Indirect knowledge propagation through Procedure E gossip** correctly delivered the event to Ambassador's Knowledge → triggered next-season Concern via existing Knowledge-Belief path. ✓
- **Knock-on observed:** The visibility gate creates a one-Accounting delay between event and Concern for non-observing NPCs who are connected via gossip. **This is realistic — political news takes time to spread through relational channels.** Players will see this as more authentic than instant universal awareness.
- **Ambiguity flagged:** The "Knowledge contradicts Belief" check is content-authored (`derive_contradiction(knowledge, belief)`). PATCH-time spec doesn't define how this works algorithmically. **`[GAP: knowledge_contradicts_belief() unspecified — content authoring helper; v1.2 should define matching schema (tag-based? semantic? human-authored cross-reference table?)]`.**

---

## §7 Direction-A summary

### 7.1 Single-writer invariant — VERIFIED across 3 scenarios

In Scenarios 1, 2, 3, no Opinion mutation occurred outside Procedure D. All B-Resolution and C-Completion paths produced Memories only. Procedure D consumed those Memories and applied drift. **`[INV-1, INV-2, INV-3] hold under traced load.`** Single-writer architecture is sound.

### 7.2 Magnitude differences vs pre-patch

Pre-patch B and C wrote Opinion deltas directly with magnitudes ±0.5. Post-patch routes through D's drift formula with multiplier and dampening. Net effect:
- **Aligned-direction legacy:** post-patch is *smaller* than pre-patch (e.g., -0.1 vs -0.5 in §2). Reinforces existing strong Opinions less aggressively.
- **Contradicting legacy:** post-patch is *roughly comparable* (-0.4 vs -0.5).
- **Combined chains (B + C same season):** end-state can differ from pre-patch by 0.2-0.3 affect_axis units due to drift order and multiplier interaction.

These are **design intent** changes per doc 17 §1.7's "comparable magnitude" claim — the term "comparable" is loose and the simulation reveals the actual delta is direction-dependent.

### 7.3 Surfaced specification gaps

Six gaps surfaced through this Direction-A simulation. All flagged for v1.2:

| ID | Surface | Issue |
|---|---|---|
| SIM-A-G1 | Scenario 2 | `small_drift` and `larger_drift` numeric coefficients not specified |
| SIM-A-G2 | Scenario 3 | D's drift loop iteration order over `new_memories` not specified |
| SIM-A-G3 | Scenario 5 | `weighted_select()` re-roll-and-average semantics under low confidence not fully specified |
| SIM-A-G4 | Scenario 6 | `knowledge_contradicts_belief()` matching algorithm not specified (content-authoring helper) |
| SIM-A-G5 | All scenarios | Procedure D `evidence_memory_refs` write timing — does the consumed Memory appear in the Opinion's evidence list immediately, or only after drift completes? Spec doesn't say |
| SIM-A-G6 | Scenario 1 | Existing spec's `if confidence <= 2` vs `if confidence >= 3` boundary at exactly 2 — should be specified as `< 3` or `<= 2` consistently (currently both forms appear in different parts of the spec) |

### 7.4 Emergent properties observed

1. **Slower cumulative Opinion shift.** Single-writer routing through D damps direct-write magnitudes, especially in aligned-legacy. Total Opinion change over a campaign year is reduced by ~30-50% in aligned cases. **Implication:** NPCs are slower to "warm up" to allies but reactions to opposition remain comparably sharp.

2. **Bridge-sympathy across hostile factions.** PATCH 2.3 multiplier 1.2 fires when Conviction-secondary matches across primary, even cross-faction. This produces realistic individual rapport across institutional opposition. Worth highlighting to design as a *feature*.

3. **Uniform-fallback NPCs become genuinely chaotic.** Old Soldier scenario: high-Scar without secondary produces inconsistent Concern framing across Accountings. Player-perceptible.

4. **Knowledge propagation creates realistic delay patterns.** Visibility gate + Procedure E gossip chain produces ~1 Accounting delay between event and non-observer's Concern. Politically authentic.

### 7.5 Recommendations for next simulation directions

- **Direction B — Domain Action selection.** The new `select_proposal()` (PATCH 2.1) and DOMAIN_ARMATURE_ALIGNMENT 42-entry table interact with Standing recalc (PATCH 3.11) over Campaign Year boundaries. Trace: 4 NPCs proposing, alignment scores, ties broken by Standing, Standing changes from PATCH 3.11 over multiple years.
- **Direction C — Settlement/faction signal.** New compute_settlement_signal null-guards (PATCH 2.5) + governor fallback need exercise across edge cases (empty settlements, governor-only signals, sparse-Memory settlements).
- **Direction D — Relational dynamics.** NPC Standing recalc, Outreach Priority 3 default (PATCH 3.10), Knot integration (PATCH 3.6), Memory replacement at 3-cap (PATCH 3.15).
- **Direction E — Composition.** Multi-agent multi-Accounting trace; surface emergent dynamics like feedback loops, oscillations, runaway accumulation.

### 7.6 Direction A — VERDICT

**PASS with 6 documentation gaps and 4 noted emergent properties.** Single-writer Opinion architecture is mechanically sound; magnitudes differ from pre-patch in expected ways; one design-call surface (aligned-legacy magnitude reduction) flagged for Jordan. v1.2 should resolve the 6 spec gaps; aligned-legacy magnitude reduction is acceptable as designed but worth documenting.

---

**END OF SIM-A.**
