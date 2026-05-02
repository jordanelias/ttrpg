<!-- [CANONICAL: 2026-05-01 — PP-688 v1 articulation layer; promoted from PROVISIONAL after Stage 10 sim PASS (12/14 battery; commits bb5e293 lateral + 3cb5207 articulation); carry-forward P2: belief_revised not in 8-trigger ruleset (articulation sim §4.1); A6 supports clustering 9th trigger ADD] -->
<!-- STATUS: PROVISIONAL — Class A canonical document; consumes PP-687 substrate, reads PP-684 + PP-686. -->
<!-- AUTHORITY: PP-688 -->

# Articulation Layer (PP-688)

**Class:** A — narrative-articulation system bridging happenings (Key log) and the player's experience of story.
**Status:** PROVISIONAL.
**Sequencing:** consumes PP-687 substrate; reads PP-684 Conviction taxonomy and PP-686 faction state; extends Key registry with 3 Class B types.
**Companion docs:** `designs/architecture/key_substrate_v30.md`, `designs/architecture/key_type_registry_v30.md`, `designs/personal/conviction_taxonomy_v30.md`, `designs/provincial/faction_behavior_v30.md`, `designs/scene/fieldwork_socializing.md` (Knot/Belief/Inspiration), `params/core.md` (Belief/Inspiration markers).

---

## §1 Statement

The Key log records what *happened*. The articulation layer determines what the player *experiences as story*. It accomplishes three things:

1. **Tier 1 — Protagonist UI lens:** continuous engine state shaped through the protagonist's frame (Concern queue, Memory salience, Bonds register).
2. **Tier 2 — Trigger ruleset:** thresholds at which the engine decides "this Key warrants a cut scene"; produces 5–15 second moments highlighting significant non-protagonist events.
3. **Tier 3 — Chronicle generator:** annual summary in omniscient voice; offers periodic narrative authority over the broader peninsula's events.

The architecture is grounded in the artifact 11 distinction: a story is the artifact our minds make from sequenced consequential happenings; the engine emits happenings; articulation makes them legible.

---

## §2 Tier 1 — Protagonist UI Lens

The protagonist is one actor among many in the engine. Tier 1 is the always-on UI that frames continuous engine state for the player.

### §2.1 Concern queue

The Concern queue (per `doc 12 Procedure A` and `npc_behavior_v30.md`) is rendered as the protagonist's "current focus" UI. Concerns generate from Key memory salience filtered by axis-relevance to the protagonist's `armature_position_personal`.

UI surfaces:
- Top 3-5 Concerns by salience, with axis-aligned framing
- Concern source: which Key(s) drove its generation
- Concern resolution path: which DA categories or scene types could resolve it

### §2.2 Memory salience indicator

Per-Key salience visible to the protagonist on Memory recall (engine reads Memory Query API, PP-687 §4.4). UI:
- Recent significant Keys: top-10 list ordered by recency × salience
- Each Key: short caption, source, axis-alignment indicator
- Optional "Why?" diagnostic: backward walk through CAUSAL_GRAPH (PP-687 §5.4)

### §2.3 Bonds register (existing)

Reads `Bonds_5_or_higher` set per `fieldwork_socializing.md`. UI: list of named NPCs with Bond level, Knot status, Belief markers active for this NPC.

### §2.4 Knot / Belief / Inspiration integration

Three signal types from `fieldwork_socializing.md` §5.5–5.6 + `params/core.md` L128 + ED-773:

- **Knots** (Loose / Medium / Close): pair-relational binding requiring socializing investment; rupture causes Composure damage (5 default per ED-773).
- **Beliefs** (player-authored truth-statements): ~3-5 per protagonist; engaged by scene events; revision is a high-significance state transition.
- **Inspirations** (player-authored aspirational arcs): each with associated NPCs; engaged by Bonds + scene events.

Tier 1 surfaces these continuously:
- Knot tier indicator per Bonded NPC
- Belief register with engagement count per Belief
- Inspiration tracker with engagement count per Inspiration

### §2.5 Chronicle search-bar (Tier 1 access to Tier 3)

Player query "what happened in [territory] last year" → engine returns:
- Tier 3 chronicle entry for that period (if generated)
- Direct Key-log filter for player-observable Keys in scope
- Causal walk anchored on player's most-salient Key for the period

---

## §3 Tier 2 — Trigger Ruleset (Cut Scenes)

A cut scene is a short (5–15 second) engine-rendered moment showing a non-protagonist event in evocative detail. Triggered by thresholds on Key emissions; not authored.

### §3.1 Trigger ruleset (10 triggers — 8 initial per D10, +#9 cascade clustering added 2026-05-01, +#10 belief_revised added 2026-05-02 per Stage 10 §4.1 finding)

A Key fires a Tier 2 cut scene if it matches **any** of:

| # | Trigger condition | Rationale |
|---|---|---|
| 1 | `state.scar_acquired` for any tracked NPC (Bonded, named in roster) | Conviction Scars are inflection points |
| 2 | `state.coup_attempted` for any faction | Internal challenge regardless of outcome |
| 3 | `state.succession` with `succession_mode in [contested, emergency, imposed]` | Non-routine leadership change |
| 4 | `mechanical.mission_shift` | Faction direction change |
| 5 | `da.covert_betrayal` with `exposed == true` | High symbolic weight regardless of outcome |
| 6 | `meta.knot_formed` (Class B per §6) | New Bond tier |
| 7 | `meta.knot_ruptured` (Class B per §6) | Composure-load-bearing rupture event |
| 8 | `env.peninsular_strain_shock` with `severity in [severe, crisis]` | Peninsula-scale narrative beat |
| 9 | `meta.cascade_cluster_event` (cluster forms or dissolves; sustained ≥ 4 seasons) | Cross-faction ideological alignment / opposition |
| 10 | `state.belief_revised` for any tracked NPC (Bonded, named in roster) | Singular protagonist-internal belief inflection (Stage 10 articulation sim §4.1: sig=7 mid-tier, otherwise routed only via K/B/I bumps) |

**Trigger 9 specification (added 2026-05-01 per Stage 8b sim verification):**

```
Condition:
    For each pair (faction_a, faction_b):
        sim = cosine_similarity(faction_a.cascade_fidelity_history[-4:],
                                faction_b.cascade_fidelity_history[-4:])
        if abs(sim) > 0.40 (Stage 10 A6 calibration; replaces 2026-05-01 starting 0.7 — see footnote):
            if sustained ≥ 4 seasons (regime entry):
                emit meta.cascade_cluster_event Key with payload:
                    cluster_pair: [faction_a, faction_b]
                    similarity: sim
                    cluster_type: aligned (sim > 0) | anti_aligned (sim < 0)
                    sustained_seasons: streak
                scale: peninsular (if abs(sim) > 0.95) | territorial
                fire once per regime; refire on regime transition
```

The cluster threshold ±0.40 reflects Stage 10 articulation sim A6 evidence (corr +0.937 at the canonical Crown/Hafenmark cascade pair, 30-season window; signal classified DETECTABLE per |corr| ≥ 0.30 floor). The original 2026-05-01 starting threshold was ±0.7; Stage 10 §3.6 recommended tightening to ±0.40 to capture cross-faction clustering above the MARGINAL band (0.15–0.30) without false positives from coincidental short-window synchronization. Stage 8b sim (`designs/audit/2026-05-01-stage-8-sim/01_findings_8b_trigger9.md`) verified the architecture; Stage 8c calibration sweep (Phase 5a) refines threshold further and dedup logic. Per integration plan §3.4 D10, trigger 9 was deferred from initial release pending sim-validation of clustering detection — Stage 8b + Stage 10 A6 jointly provide that validation.

**Trigger 10 specification (added 2026-05-02 per Stage 10 articulation sim §4.1 finding):**

```
Condition:
    On any state.belief_revised Key for an NPC in the tracked roster
    (Bonded ≥ 5 OR named-roster member per fieldwork_socializing.md):
        emit Tier 2 cut scene (sig accumulator + cut scene rendering per §3.4)
```

State.belief_revised was previously routed only through §3.5 K/B/I integration as a payload **bump** to scene_event significance. Stage 10 §4.1 finding observed: a belief-revision Key on its own — without a co-firing trigger — has sig=7 (mid-tier) but does not produce a cut scene. Adding trigger #10 closes this gap. Cross-reference: integration plan §3.4 D10 originally placeholdered the 9th-trigger slot; with cross-faction clustering already promoted to #9 (2026-05-01) and Stage 10 A6/§4.1 dual-finding, both belief revision and cluster events now have canonical trigger entries.

### §3.2 Significance function

Each fired Key receives a per-trigger `significance` score:

```
significance(key) =
    stakes_weight(key)                    # 1-5 from Key.scale_signature + targets
  + protagonist_alignment(key)            # 0-3 if protagonist or Bonded NPC mentioned
  + cascade_event_weight(key)             # 0-2 from cascade_fidelity delta if state-of-faction Key
  + accumulated_narrative_weight(key)     # 0-3 from cumulative tracker (§3.3)
```

Range: 0–13. Cut scene length scales with significance: 5s for 0–4, 10s for 5–9, 15s for 10–13.

### §3.3 Accumulated narrative weight

A per-NPC and per-faction tracker that accumulates as their Keys go un-articulated. Resets when a cut scene featuring them fires. Prevents narrative starvation:

```
on_key_emitted(key):
    for actor in key.targets:
        actor.unarticulated_weight += stakes_weight(key)

# at trigger fire:
weight = actor.unarticulated_weight
actor.unarticulated_weight = 0
```

Effect: if a Bonded NPC accumulates many low-stakes Keys with no cut scene fired, eventually a routine Key triggers a higher-significance cut scene. Calibrate at Stage 10.

### §3.4 Cut scene rendering

Cut scenes are rendered through engine systems, not authored. Each draws on:
- Key payload contents
- Targets' `armature_position_personal` for interpretive framing
- Key.symbolic_dimensions for axis emphasis
- Local environmental state (scene location, time, present actors)

Two render styles:

**5–10 second style ("flash"):**
- Single image of the moment
- Caption (1-2 sentences in protagonist's interpretive voice if present, otherwise omniscient)
- Axis emphasis: which Conviction is being engaged

**10–15 second style ("scene"):**
- Setting establishing
- Action representation (what occurred)
- Aftermath beat (1 sentence on consequence)

Phase 5a Godot scope adds 1–2 sessions for cut scene rendering per integration plan §3.5.

### §3.5 Belief / Inspiration / Knot engagement

Scene-event Keys gain three optional payload fields (additive; existing Keys unaffected):

```yaml
scene_event_key.payload (extension):
  belief_engagement_for: {<actor_id>: <aligned | challenging | betraying>}
  inspirations_engaged_for: {<actor_id>: [<inspiration_name>, ...]}
  knot_partners_present: [<actor_id_a>, <actor_id_b>, ...]
```

**Effect on significance:**
- `belief_engagement_for[protagonist]` non-empty → +2 significance
- `inspirations_engaged_for[protagonist]` non-empty → +1 significance per inspiration
- `knot_partners_present` includes protagonist's Bonded NPC pair → +1 significance

These additions raise significance for scenes that engage the player's authored Beliefs / Inspirations / Knot pairs, ensuring those scenes more often qualify for cut-scene articulation.

---

## §4 Tier 3 — Chronicle Generator (Annual)

### §4.1 Trigger

Tier 3 chronicle generates on `mechanical.accounting` Key with `annual == true` (year boundary). One chronicle per year, peninsula-scope.

### §4.2 Voice

**Omniscient narrative voice.** The chronicle speaks of all factions, territories, and named NPCs from outside any single perspective. Per artifact 13 §2: this is the engine's narrative authority, distinct from the protagonist's interpretive frame at Tier 1.

The voice is steady, periodically lyrical, factual about what happened, sparing in editorial. Reference: artifact 15 §2 (Almud Year 3 sample).

### §4.3 Significance function for Tier 3

Same significance form as Tier 2 (§3.2) but with **universal track**: stakes_weight + cascade_event_weight + accumulated_narrative_weight (no protagonist_alignment term). Top-N Keys per year by significance get chronicle paragraphs.

```
significance_universal(key) =
    stakes_weight(key)
  + cascade_event_weight(key)
  + accumulated_narrative_weight(key)
```

Plus a **protagonist track** retained alongside, surfacing the protagonist's significant events as a final chronicle paragraph.

### §4.4 Chronicle structure

Per year, the chronicle emits ~5–12 paragraphs:

1. **Peninsula-scale opening** — major peninsula-scale Keys (env.crisis, env.peninsular_strain_shock with severity=crisis, treaties between factions)
2. **Per-faction movements** — for each faction with significant year, a paragraph: Mission progress, Cascade fidelity trajectory, Legitimacy/Popular Support shift, succession events
3. **Notable individuals** — top-N named NPCs by accumulated weight; their pivotal Keys
4. **Knot/Belief inflections** — Knot formations and ruptures, Belief revisions
5. **Protagonist paragraph** — the player character's year through the omniscient lens

### §4.5 Source data per paragraph

Each paragraph is generated by selecting Keys per significance, then templating prose with reference to:
- Key payload content
- Targets' Conviction interpretations
- Causal-graph chains (what led to what)
- Peninsula state at year boundary

Tier 3 is engine-rendered, not authored. Style guide and templates per Phase 5a Godot implementation.

### §4.6 Diagnostic + replay value

Beyond narrative articulation, Tier 3 chronicles support:
- Multi-decade campaign legibility (years 5, 10, 15, etc., readable as continuous history)
- Diagnostic of engine emergent behavior across long campaigns
- Save-state portability: a save's chronicle history is the campaign's narrative record

---

## §5 Integration with Substrate (PP-687 §8.7)

Articulation layer subscribes to all Key emissions per PP-687 §4.1 step 5. Subscription callbacks:

```
on_key_emitted_articulation(key):
    # Tier 2 trigger evaluation
    if matches_trigger_ruleset(key):
        sig = compute_significance(key)
        emit_cut_scene(key, sig)
        reset_unarticulated_weight(key.targets)
    else:
        accumulate_unarticulated_weight(key)
    
    # Tier 1 awareness update
    update_protagonist_concern_queue(key)
    update_protagonist_memory_index(key)
    
    # Tier 3 deferred (fired only on annual accounting)
```

All callbacks O(1) or queue-based; no synchronous emission stalls.

### §5.1 Awareness update

Per PP-687 §4.1 step 7: when a Key has `causes[]`, each cause Key's `awareness` field increments (`+0.1` clamped 0–1). High awareness on a cause Key indicates "this earlier Key has been recently woven into a chain"; significance computation reads awareness as part of stakes_weight.

---

## §6 Class B Extensions to Key Type Registry

Three new Key types required by articulation layer; declared as Class B extensions per PP-687 §10:

### §6.1 meta.knot_formed (already in registry per PP-687 §8)

Confirmed in registry; no new declaration needed. Articulation layer is the consumer.

### §6.2 meta.knot_ruptured (NEW Class B addition)

Per PP-687 key_type_registry_v30.md §8. Articulation layer consumes; ED-773 Composure damage handled by `npc_behavior` (existing).

### §6.3 state.belief_revised (NEW Class B addition)

Per PP-687 key_type_registry_v30.md §8. Articulation layer consumes; emits Tier 2 cut scene by default (high-significance per §3.5).

---

## §7 Pacing (Deferred per D11)

Pacing — engine determining when scenes flow at "minute-by-minute" tempo vs "season-by-season" — is **deferred to a future PP**. The articulation layer as specified does not enforce pacing; cut scenes fire whenever triggers match, and chronicle fires annually. Stage 10 sim observation may surface pacing concerns; specific pacing PP authored if needed.

---

## §8 Verification (Stage 10 sim plan)

Stage 10 articulation simulation per integration plan §3.5:

| # | Test | Expected |
|---|---|---|
| A1 | Significance scoring against authored ground truth | Top-10 significance Keys overlap ≥80% with author-marked beats |
| A2 | 8-trigger ruleset firing rate | 1.5–4 cut scenes per season at default thresholds |
| A3 | Chronicle prose generation | Coherent omniscient prose per year; no narrative gaps |
| A4 | K/B/I integration | Belief revision + Knot rupture both fire cut scenes; Inspirations engage with appropriate frequency |
| A5 | Determinism | Same Key log → same cut scene + chronicle output |
| A6 | Cross-faction clustering candidate | Sim observation of cascade fidelity correlation; supports decision on Phase B 9th trigger |

Phase 5a Godot scope: +1-2 sessions for cut-scene rendering, +1 session for chronicle paragraph generator.

---

## §9 Vetting Block (per PP-674 framework)

```yaml
vetting:
  class: A
  necessity: pass
  omega: pass
  mu: [Μ-α, Μ-γ, Μ-δ]
  m_ratings:
    M-1: "+"
    M-2: "○"
    M-3: "+"
    M-4: "✓"
    M-5: "+"
    M-6: "+"
    M-7: "✓"
    M-8: "+"
    M-9: "+"
    M-10: "✓"
    M-11: "+"
  q: pass
```

---

## §10 Open Items Resolved per Integration Plan §3.4

| Decision | Resolution |
|---|---|
| **D10** Trigger ruleset (8 initial) | Per §3.1 |
| **D11** Pacing | Deferred per §7 |
| Story-vs-happenings probability | PP-688 raises full-engine story-fraction estimate to ~75-85% (per artifact 11 §3.5; substrate alone produces ~15%) |
| K/B/I integration | Per §2.4 + §3.5 |
| Class B Key types | meta.knot_formed (existing) + meta.knot_ruptured (new) + state.belief_revised (new) per §6 |
| Significance function form | §3.2 (Tier 2) + §4.3 (Tier 3) |

---

**End spec. PROVISIONAL pending ratification.**
