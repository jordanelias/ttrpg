<!-- [PROVISIONAL: 2026-05-07 — Character canon consolidation; supersedes piecemeal lookup across npc_roster_v30 / npc_behavior_v30 / npc_character_analyses_v30 / npc_foils_v30 / character_histories_v30 / individual NPC docs / migration_roster_v30 / stance_triangles for per-NPC texture. Substrate (PP-684 13-Conviction taxonomy + axis_matrix) remains in source files; this consolidation references, does not duplicate.] -->
<!-- STATUS: PROVISIONAL — pending Jordan ratification. PART A (Framework) complete; PART B (NPC sheets) pending Q1 scope decision. -->
<!-- AUTHORITY: consolidates PP-684 (13-Conviction) + PP-685 (migration roster) + PP-681 (Piety Track promotion) + PP-688 (Articulation Layer) + npc_behavior_v30 §§1-12 + npc_roster_v30 + npc_character_analyses_v30 + character_histories_v30 + individual NPC docs (edeyja_npc, baralta_v30, companion_specification). -->

# Valoria — Character Canon (Consolidated)
## Status: PROVISIONAL — pending ratification.
## Date: 2026-05-07
## Companion: `designs/provincial/faction_canon_v30.md` (per-faction sheets) — Stage 1 complete.
## Substrate: `designs/personal/conviction_taxonomy_v30.md` (PP-684 13-Conviction) + `designs/personal/conviction_axis_matrix_v30.md` — both files remain canonical and are referenced, not duplicated, here.

---

# PART A — FRAMEWORK

## §1 Status, Scope, and Supersession

This document consolidates per-NPC texture canon scattered across:

- `designs/npcs/npc_roster_v30.md` (+ index, infill) — supporting-NPC roster (Tier 2)
- `designs/npcs/npc_behavior_v30.md` (+ index, infill) — Tier 1 stance triangles (§2), Belief mechanics (§3), Decision derivation (§4), Arc state machine (§5), Resonant Style integration (§6), Framework Drift (§7), Priority Trees (§8), Recruitment (§9.5), Roster Tiers (§11)
- `designs/npcs/npc_character_analyses_v30.md` (+ index, infill) — literary analyses with historical parallels (the de facto inspirations field)
- `designs/npcs/npc_foils_v30.md` (+ infill) — Ruler Diamond foil networks
- `designs/npcs/edeyja_npc.md` — individual deep dive (gold standard)
- `designs/npcs/baralta_v30.md` — individual theological extension (PROVISIONAL)
- `designs/npcs/companion_specification_v30.md` — companion-app behavior
- `designs/world/character_histories_v30.md` (+ index, infill) — PC lifepath system (Origin / Formation / Vocation / Catalyst)
- `designs/personal/conviction_taxonomy_v30.md` (PP-684) — 13-Conviction taxonomy substrate
- `designs/personal/conviction_axis_matrix_v30.md` — Conviction → 4-axis projection
- `designs/personal/conviction_migration_roster_v30.md` (PP-685) — per-NPC mapping from legacy 7-/9-Conviction labels to 13-Conviction
- `designs/personal/conviction_track_v1.md` — Scar accumulation + Conviction crisis mechanic (uses stale 9-Conviction taxonomy — see §11 D-decisions)
- `params/factions/npc_stance_triangles.md` — Framework Drift table (uses stale 7-Conviction labels)

**What this consolidation does:**
- Defines a single per-NPC sheet schema (Part B follows it).
- Pulls texture for each named NPC into one place per character.
- Surfaces every conflict between sources rather than silently resolving (per Decision Log §11).
- Lifts the scattered historical-parallel prose from `npc_character_analyses_v30` into structured `inspiration` fields per NPC.
- Marks every Tier-3 NPC with explicit `[GAP — Phase B authoring]` for missing dimensions; does not invent.

**What this consolidation does NOT do:**
- Does not retcon canonical Conviction values, Belief quotes, or arc trajectories.
- Does not silently regenerate `npc_behavior_v30 §2` stance triangles from migration roster (though they conflict — see §11 D1).
- Does not invent texture for empty-body sections (Vaynard Arc A/B, Cardinal Klapp/Olafsson/Jarnstal/Ehrenwall character_analyses entries, ~40% of foil pairings). Surfaces what exists; flags `[GAP]` for the rest.
- Does not commit. Lands as artifact for Jordan review.

**Supersession (informational):**
- Legacy 7-Conviction taxonomy (`npc_stance_triangles.md`): SUPERSEDED by PP-684 13-Conviction. Retained in source for historical reference; per-NPC sheets in Part B use 13-Conviction primary with legacy mapping shown for traceability.
- Legacy 9-Conviction taxonomy (`conviction_track_v1.md` §1): SUPERSEDED by PP-684. **The Scar mechanic itself remains canonical** — the taxonomy it indexes is stale. Part B references the Scar mechanic; conviction values use 13-Conviction.
- Legacy ethical-tradition labels (Categorical Imperative, Virtue, Faith, Scholastic, Equity, Honor): SUPERSEDED by PP-684 §6. Aliases recorded in `references/alias_registry.yaml`. Per-NPC sheets retain legacy labels as **descriptive disposition tags** with `[SUPERSEDED]` markers.
- `params/bg/core.md §Ethical Framework Modifiers` and `factions_personal §Ethical Framework Modifiers`: SUPERSEDED 2026-05-01/02 per SUPERSESSION-PP686-001/002. Mechanical Ob modifiers come from PP-686 §3.7 triadic calculation, not from these labels.

---

## §2 How to Read an NPC Sheet

Each named NPC in Part B follows this schema. The schema parallels the per-faction sheet schema in `faction_canon_v30.md` — convictions are the shared substrate; what differs is the dimensions specific to personal-scale rendering (TS / Coherence / Spirit) and prose-feedstock (Beliefs, Speech register, Physical signature).

```
## <Name> — <Title / Role> (<Faction>)
[Tier · Status · TS · Coherence · Spirit · Certainty · Self-Other]

Identity            — full name, pronouns, title, faction, archetype, role within faction
Convictions         — primary 1–3 (13-Conviction weights, sum 0.6–0.8) + cultural template
                      + legacy mapping ("← was [old label]" for traceability)
Self-Other          — initial value [-1.0..+1.0] + drift direction + archetype implication
Beliefs             — 1–3 first-person voice quotes (anchors for prose-writer)
Goals               — 1–2 explicit; standing vs situational; what they want vs what they
                      think they want
Inspiration         — historical_parallel + in_character_aspiration (lifted from
                      character_analyses literary framing)
Ethical Disposition — legacy label [SUPERSEDED tag] + Ob modifier intent (mechanical Ob now
                      from PP-686 §3.7)
Resonant Style      — primary + secondary (per npc_behavior §1.3 — what argument shape can
                      reach them)
Behavioral AI       — flaw + mechanical consequence (per npc_roster §X.X for Tier 2)
Arc Map             — A / B / C minimum; D/E/F where royal-fuse arcs apply
Physical Signature  — sensory anchors where they exist (Edeyja's Thread injury is the
                      gold standard)
Speech Register     — diction, register, characteristic patterns; defaults to focalization-
                      driven via prose-writer
Personal-scale axes — Thread Sensitivity (0–100) · Coherence (0–10) · Spirit (1–7) ·
                      Certainty (0–5) — with [PROVISIONAL] flags where authored values
                      diverge from defaults
Knot/Bond capacity  — relational thresholds + named close Knots
Key Relationships   — foil pairings, advisor-principal links, faction Cascade position
Provenance          — source files this entry consolidates from
```

---

## §3 The Conviction Substrate (Reference)

The 13-Conviction taxonomy lives in `designs/personal/conviction_taxonomy_v30.md` (PP-684). **That file is canonical and is not reproduced here.** What follows is a working summary.

### §3.1 The 13 Convictions (recap, PP-684 §2)

Faith · Authority · Order · Scholastic · Utility · Equity · Liberty · Precedent · Community · Identity · Warden · Virtue · Honor.

Each Conviction earns its place via a load-bearing Renaissance political-ethics dimension. For per-Conviction definitions, period equivalents, and rationale see PP-684 §2 in source.

### §3.2 Vector representation (recap, PP-684 §4)

Each NPC's `personal_convictions` is a 13-element vector with **structured concentration**:

```yaml
NPC.personal_convictions:
  primary:
    - {conviction: <name>, weight: 0.6..0.8 sum across primaries}
    # 1–3 entries
  cultural_background:
    - {conviction: <name>, weight: 0.05..0.20}
    # multiple entries from cultural template; sum 0.2..0.4
```

### §3.3 Cultural Background Templates (recap, PP-684 §5)

Eight authored templates supply the cultural-background distribution:

`varfell_alpine` · `crown_lowland` · `valorian_court` · `ecclesiastical` · `hafenmark_procedural` · `lowenritter_military` · `restoration_reformist` · `einhir_traditional`.

Per-NPC sheets in Part B reference template by name. Distributions live in PP-684 §5.1.

### §3.4 4-axis projection (recap, axis_matrix_v30)

The 13-Conviction vector projects onto a 4-axis substrate (`hierarchical / sacred / instrumental / traditional`) via a 13×4 matrix. Used by the engine for armature_position computation, Cascade Fidelity (faction-side), and Key symbolic-dimension projection. Per-Conviction calibration lives in axis_matrix §3 with Renaissance grounding for each row.

### §3.5 Effective Convictions (faction-coupled)

Per PP-686 §3.2, NPCs in faction-role context use `effective_convictions` (cascade-blended from supervisor) rather than raw `personal_convictions`. Per-NPC sheets in Part B show `personal_convictions` (the authored value); `effective_convictions` is computed at runtime from the faction's organizational hierarchy. See `faction_canon_v30 §3.2` for the cascade math.

---

## §4 Self-Other Orientation

Per PP-684 §3. A scalar `[-1.0, +1.0]` orthogonal to the Conviction vector. Tracks whom the actor primarily benefits — themselves vs the broader populace.

| Range | Interpretation |
|---|---|
| -1.0..-0.5 | Self-sacrificing — outcomes attributed primarily to collective benefit |
| -0.5..-0.1 | Mildly altruistic — collective-leaning |
| -0.1..+0.1 | Neutral / balanced |
| +0.1..+0.5 | Mildly self-interested |
| +0.5..+1.0 | Self-aggrandizing — outcomes primarily personal benefit |

**Why this is orthogonal to Convictions.** Cesare Borgia and a public-spirited republican magistrate may share a high Utility Conviction; what distinguishes them is *for whom* they instrumentalize. The Conviction tells you what the actor values; Self-Other tells you who benefits when they act on it.

**Drift mechanic** (PP-684 §3.2). Self-Other drifts under accumulated outcomes:

```
Δ orient per season = κ × Σ(outcome_with_self_benefit) − κ × Σ(outcome_with_collective_sacrifice)
```

with `κ = 0.03` default (calibrate at Stage 10), bounded `[-1, +1]`. This produces emergent character development: a leader whose Mission victories repeatedly enrich themselves drifts toward +; one whose decisions repeatedly favor the collective drifts toward −. **The Macbeth arc / fall-from-grace arc / moral-development arc emerges from accumulated outcomes rather than authored beats.**

Per-NPC initial values authored per archetype. Most NPCs start in `[-0.2, +0.2]`. Outliers (named historical-equivalent figures) start further. Player characters default 0.0.

---

## §5 Resonant Style Taxonomy

Per `npc_behavior_v30 §1.3`. Four canonical Resonant Styles. Each NPC has a primary and secondary; together they specify what argument shape can reach the NPC and force genuine reconsideration.

| Resonant Style | The NPC is vulnerable to | Because their Conviction... | Contest mapping |
|---|---|---|---|
| **Evidence** | Specific, verifiable, named facts contradicting their operative belief | ...claims to be reality-responsive. Confronted with reality it cannot dismiss, the framework strains. | Memory + Revealing (Precedent style) |
| **Consequence** | Demonstrated or projected outcomes their framework fails to explain or prevent | ...claims to produce good results. Confronted with its failures, it cannot deflect. | Projection + Revealing (Vision style) |
| **Authority** | Appeals from a source their framework recognises as binding | ...defers to certain authorities. When that authority contradicts their position, structural bind. | Memory + Obscuring (Suppression) — accumulated weight forecloses dismissal |
| **Solidarity** | Appeals grounded in relational obligation (debts, shared history, personal bonds) | ...values relationships. When a relationship demands what the position forbids, the bind is genuine. | Any genre + Revealing; **requires active Knot with the NPC** |

**TS Gate** (per `npc_stance_triangles`): Thread-level evidence is invalid as Evidence targeting vs TS 0 NPCs (P-08 compliance). Ontical evidence only.

**Wrong-Style Penalty** (per `npc_behavior §6.4` Church Martyrdom Extension): targeting an NPC with their non-resonant Style produces +1 Ob in Contests; the NPC reads the attempt as off-target and may treat it as confirmation of their position.

**Stacking Limits** (per `npc_behavior §6.5`): a single Contest can target one Style at a time. Sequenced multi-style argument is canonical and produces compound vulnerability if both fire.

---

## §6 Belief / Scar / Conviction-Crisis Mechanic

Consolidated from `conviction_track_v1.md` (the mechanic itself; **the 9-Conviction taxonomy used in the source is stale** — convictions referenced here use PP-684 13-Conviction names) + `npc_behavior_v30 §3`.

### §6.1 Belief Structure

NPCs hold authored Beliefs — first-person truth-statements that shape interpretation. Beliefs are revealed to players through:

- Contest Appraise step (Overwhelming: one Belief revealed per `social_contest_system_v2 §4`)
- Observation (engine grants Belief revelation when the NPC acts on a Belief in a way the PC witnesses)
- Settlement-broker intelligence (per `settlement_layer_v30 §4.7-4.9` — replaces struck Niflhel intelligence-broker mode)

Per-NPC sheets in Part B carry 1–3 Beliefs as first-person quoted strings. These are the **voice anchors** the prose-writer skill consumes.

### §6.2 Belief Revision

An NPC revises a Belief when ALL hold:

1. A Contest produces decisive outcome (Piety Track ≥ 7 or ≤ 3) against the NPC.
2. The winning argument used the NPC's primary or secondary Resonant Style.
3. The argument specifically engaged the Belief.

Old Belief → permanent Scar. New Belief forms.

### §6.3 Scar Accumulation and Conviction Effects

| Scars | Effect on Conviction | Effect on Resonant Style | Effect on Behavior |
|---|---|---|---|
| 0 | Default | Default | Stable institutional behavior |
| 1 | Secondary Conviction activates alongside primary; Decision Forks increase | No change | NPC exhibits internal conflict; both Convictions influence decisions |
| 2 | Primary may shift to secondary (engine judgment); arc transition state | Secondary Resonant Style activates permanently; vulnerable on two fronts | Institutional Tendency may diverge from personal behavior |
| 3+ | **Conviction crisis.** Engine rolls on crisis table per major decision | All Resonant Styles active; socially exposed | Full transformation; arc enters terminal phase — stabilise into new configuration or be destroyed |

**Conviction crisis table** (3+ Scars, engine d6 per major decision):

| Roll | NPC acts on... |
|---|---|
| 1–2 | Original primary Conviction (habitual regression) |
| 3–4 | Secondary Conviction (conscious pivot) |
| 5 | Liberty (survival instinct overrides — was "Autonomy" in the legacy 9-Conv source; remapped to Liberty per PP-684 §6) |
| 6 | Whichever Conviction most aligns with the last PC interaction (relational pull) |

### §6.4 Thread Operation → Conviction Scar Triggers (ED-663, ED-664)

Per `conviction_track_v1 §3`. Thread operations witnessed by NPCs produce Scars. Parallels Certainty Track (cosmological framework shift; `params_core` PP-551) but targets a different track: Certainty = framework shift; Scar = moral wound.

Witness requirement: direct witness OR credible testimony (Evidence Track + Disposition ≥ +1). Certainty scaling: C5 +1 Scar severity; C0 −1; C2–3 standard. Season cap: max 1 Scar/season from Thread witnessing per NPC. Mending exception: never produces Scars. **Faith specificity:** Faith-primary NPCs Scar from ANY Thread operation except Mending.

Player Conviction Checks (ED-664): player witnesses Thread event → Spirit pool, TN 7, Ob 1. Failure: active Conviction shaken (mechanical = NPC Scar 1 effect) for 1 season.

---

## §7 Three Orthogonal Personal-Scale Axes

The prose-writer skill (`skills/prose-writer/SKILL.md`) treats three axes as independent. Per-NPC sheets in Part B show authored values for all three (or `[ASSUMPTION: default]` where unauthored).

### §7.1 Thread Sensitivity (TS, 0–100)

What the actor perceives beyond ordinary human capacity. Axis substrate of the setting.

| TS Band | Label | Interpretive Frame |
|---|---|---|
| 0 | Foreclosed | Theologically suppressed (Church framework) — cannot develop without confrontation that shatters prophylaxis |
| 1–9 | Latent | Trace; below conscious access |
| 10–19 | Hidden | Unrecognised; "hunches" attributed to skill or instinct |
| 20–29 | Dormant | Conscious access begins; below Forgetting-resistance gate (29) |
| 30–49 | Stirring → Active | Practitioner threshold; Thread-Read available |
| 50–69 | Deep | Substantive Thread perception during operations |
| 70+ | Apex | Edeyja band; near theoretical ceiling of human capability |

TS is canonical per NPC across the texture stack — most reliable single dimension.

### §7.2 Coherence (0–10)

The structural integrity of the practitioner's always-already self-rendering. Whether the actor's self-rendering holds them as a human configuration. Bands per `threadwork_v30 §3.3`:

| Coherence | Label | Decision Rule (NPC practitioner per ED-665) |
|---|---|---|
| 10–6 | Stable | Operate freely |
| 5 | Dissonant | Self-limit to defensive Thread ops only |
| 4–3 | Fragmented | Cease Thread operations; non-Thread combatant |
| 2 | Fractured | Seek withdrawal; arc transition consideration |
| 1 | Severed | Crisis mode; arc transition fires; +2 Ob all Thread ops; dissociative episodes (EDGE-02) |
| 0 | Conversion | NPC transition per `params_core` PP-261 |

**MS Override (Warden):** MS ≤ 20 → Warden NPCs override Degraded/Fractured for Mending only (Continuity Conviction overrides personal safety). Mechanism for Edeyja Burnout arc.

Per-NPC Coherence baselines exist for some named NPCs (Edeyja: 9). For most others, **authored Coherence is absent** — sheets in Part B carry `[ASSUMPTION: default 8 Stable]` where unauthored.

### §7.3 Spirit (1–7, the metaphysical attribute)

Whether the will continues to grip when rendering fails. From the prose-writer skill:

> "The Spirit axis becomes audible at Coherence 4 and below, where the Beckett texture (high Spirit) versus the Lispector texture (low Spirit) is the sharpest distinction the prose can make about what the PC still has."

| Spirit | Texture at low Coherence |
|---|---|
| 6–7 | Beckett continuation — the will grips, the decision recurs, agency persists despite rendering collapse |
| 4–5 | Mid-range neutral — neither agency-grip nor agency-dissolution dominant |
| 1–3 | Lispector dissolution — the name recedes, the feet replace the self, agency yields |

**Spirit is essentially absent from canonical NPC sheets.** Per Decision Log §11 D5: per-NPC sheets in Part B carry default Spirit 4 (mid-range neutral) with `[ASSUMPTION]` flag. Where the design pressure clearly diverges (Edeyja high; Vaynard at Arc C low), the sheet notes the design pressure but does not author a specific value.

### §7.4 Certainty (0–5)

Cosmological framework alignment with Solmundan orthodoxy. Distinct from Conviction (the moral-belief axis) — Certainty tracks whether the actor's interpretive framework matches Church doctrine.

| Certainty | Label |
|---|---|
| 5 | Orthodox |
| 4 | Faithful |
| 3 | Questioning |
| 2 | Skeptic |
| 1 | Transitional |
| 0 | Accepted (full Thread acceptance — Solmund as rendering, not source) |

Movement triggers: Thread events witnessed; Practitioner relationship; arc transitions; Resonant Style targeting.

### §7.5 Why these are orthogonal

The prose-writer's coherence-tier weighting requires these axes be tracked independently:

- A low-Coherence PC **without** TS experiences rendering failure as inexplicable breakdown.
- A low-Coherence PC **with** TS experiences rendering failure AND substrate perception — but one does not cause the other.
- A low-Coherence **high-Spirit** PC grips the decision (Beckett texture) while rendering fails.
- A low-Coherence **low-Spirit** PC dissolves into the dissolution (Lispector texture) — agency yields.

Conflating them produces incorrect prose. Per-NPC sheets in Part B always show all four values (TS / Coherence / Spirit / Certainty) so the prose-writer can calibrate without inference.

---

## §8 Arc State Machine

Per `npc_behavior_v30 §5`. Generic transition triggers + per-NPC arc profiles.

### §8.1 Generic Transition Triggers (`§5.1`)

| Trigger | Conviction effect | Resonant Style effect | Behavior effect |
|---|---|---|---|
| Total Victory Contest defeat via Resonant Style | Secondary Conviction activates | No change | Decision Fork frequency increases |
| Belief Scar (per §6 above) | Per Scar accumulation | Per Scar accumulation | Per Scar accumulation |
| Faction Stability ≤ 1 | Collapses to Liberty | All Resonant Styles suppressed | Any action that improves Stability, regardless of Framework |
| PC Knot ≥ Intimate | Solidarity Resonant Style activates (if absent) | — | NPC weighs PC relationship in Decision Fork |
| TS crosses threshold (Stirring 30 / Active 50) | Ontological confrontation challenges Conviction | Evidence style intensifies | Certainty movement; less predictable behavior |
| Certainty reaches 0 | Conviction permanently altered | Primary becomes Authority (old framework's authority void) | NPC in crisis; new arc phase |
| Faction eliminated | Conviction collapses to Liberty | All styles suppressed for 1 season (shock) | NPC becomes unaffiliated actor; new Belief set forms |

**Constrained sub-arc state** (ED-586): when faction Mandate < 3, NPC's primary arc behaviors requiring Mandate expenditure suspend. NPC enters Constrained state — Priority 2/3 actions replaced by Priority 6 (institutional rebuilding). Conviction and Resonant Style unchanged; only behavioral priority sequence shifts. Mandate ≥ 3 → exits Constrained, resumes prior arc.

### §8.2 Transformation Knot Strain Propagation (AUD-NPC-02 fix, P-12 compliance)

Per canon `02_foundations_amendment Amendment 2`: a transforming NPC's thread-shift exerts force on everyone knotted to them.

| NPC TS state | Close Knot strain | Distant Knot strain |
|---|---|---|
| TS 30–49 (Active) | +1 strain/season | None |
| TS 50–69 (Deep) | +2 strain/season | +1 strain/season |
| TS 70+ or in epistemic seduction | +3 strain/season | +2 strain/season |

Applies to: Vaynard Arc C (TS crosses threshold → epistemic seduction); Himlensendt Arc C (TS awakens from 0 → rapid advancement). Does NOT apply to Almud (TS 28, no threshold crossing) or Edeyja (TS 75–80 stable, not transforming).

### §8.3 Per-NPC arc profiles

Tier 1 NPCs have arc maps (A / B / C minimum; D/E/F where royal-fuse arcs apply). Per-NPC sheets in Part B reference `npc_behavior_v30 §5.2 <Name> — Arc Map` and reproduce the arc skeleton.

**Empty-body arcs are flagged `[GAP]`.** Vaynard Arc A and Arc B in `npc_behavior §5.2` have empty bodies (header only). Sheets surface the empty headers; do not invent content.

---

## §9 Tier System

Per `npc_behavior_v30 §11` (PP-661). Roster Tracking Capacity defines tracking depth per NPC; consolidation surfaces texture-floor expectations per tier.

### §9.1 Tiers

| Tier | Tracking | Texture floor |
|---|---|---|
| **Tier 1** (Tracked Named) | Full per-season state evolution; Belief revision; Scar accumulation; arc transitions | All schema fields populated; ≥1 Belief; ≥1 Goal; Inspiration; Arc Map A/B/C minimum; Resonant Style primary+secondary |
| **Tier 2** (Operational Supporting) | State updates per-season; Belief tracked; arc trajectory tracked | Identity + Convictions + Behavioral AI flaw + Goal + Inspiration (where authored) + Arc trajectory; Beliefs **may be implicit in Behavioral AI prose** |
| **Tier 3** (Inner Circle / Council) | Conviction tracked; Disposition updated; arc not tracked individually | Identity + Conviction tag + MS + Certainty + 1-line disposition note. **Below prose-writer minimum** — see D3. |
| **Background** | Cohort-tracked; no individual evolution | N/A — not in this consolidation |

### §9.2 Tier-3 prose-feedstock deficit

The audit (2026-05-07) verified: Tier-3 NPCs (Crown IC, Hafenmark IC, Varfell Jarl Council, Cardinal Officers — ~14 NPCs) carry only Conviction tag + MS + Certainty + brief disposition note. **Below the prose-writer's stated minimum of one anchored dimension.**

When `articulation_layer §3.1` Tier 2 cut scenes fire on Inner Circle NPCs (e.g., Torvi Heljason as Baralta's legal advisor at a Knot rupture trigger), the prose-writer has only one anchored dimension to draw from. Per Decision Log §11 D3: Part B sheets for Tier-3 NPCs carry `[GAP — Phase B authoring]` per missing field. **Texture floor extension is recommended at minimum** ≥1 Belief + ≥1 Goal + ≥1 Inspiration per Tier-3 NPC. ~14 NPCs × 3 fields = ~42 author-decisions.

### §9.3 Tier promotion / demotion

Per `npc_behavior §11.3`. Demotion triggers (priority order):
1. NPC dies / faction collapses / formal removal.
2. Disposition with all PCs ≤ 0 for 4+ consecutive seasons (forgotten).
3. Roster cap exceeded (highest-Disposition NPC retained; lowest demoted).

Promotion: Tier 2 → Tier 1 on first Knot ≥ Close OR sustained narrative weight ≥ 3 cut scenes featuring NPC; Tier 3 → Tier 2 on first PC-driven scene where NPC is consequential.

---

## §10 Voice Anchors and Prose-Feedstock Dimensions

The prose-writer skill (`skills/prose-writer/SKILL.md` line 153) names the minimum anchored dimensions per load-bearing NPC: **ethical framework, conviction, goal, inspiration, factional belonging.** This consolidation's per-NPC schema covers these directly plus implicit voice/Spirit/TS/Coherence inputs.

### §10.1 Per-dimension status (per audit 2026-05-07)

| Dimension | Status pre-consolidation | This consolidation |
|---|---|---|
| Ethical framework | CONFLICTED — labels SUPERSEDED but mechanically active | Retained as descriptive disposition tag with [SUPERSEDED] marker. Mechanical Ob via PP-686 §3.7. |
| Conviction | CONFLICTED — 3 incompatible taxonomies (7 / 9 / 13) coexist canonical | 13-Conviction primary (PP-684); legacy mapping shown for traceability. See D1. |
| Goal | IMPLICIT in Behavioral AI / arc map | Pulled into explicit Goals field per NPC. |
| Inspiration | LARGEST GAP — historical parallels exist as prose only in character_analyses | Lifted into structured `inspiration` field with `historical_parallel` + `in_character_aspiration` facets. |
| Factional belonging | CLEAN | Single-source-of-truth retained. |
| (implicit) Voice anchor | UNEVEN | First-person Beliefs in `npc_behavior §2` pulled into `Beliefs` field. Coverage gaps flagged. |
| (implicit) Speech register | OFFLOADED to prose-writer | Per-NPC notes added where character_analyses gives diction guidance. Prose-writer remains primary calibrator. |
| (implicit) Physical signature | NEAR-ABSENT | Pulled where authored (Edeyja Thread injury). [GAP] for the rest. |
| (implicit) TS / Coherence / Spirit | TS reliable; Coherence partial; Spirit absent | All four axes (incl Certainty) shown per NPC; defaults flagged with [ASSUMPTION]. |

### §10.2 What the prose-writer cannot consult an NPC sheet for

- **Per-NPC speech-style data** is intentionally absent. The prose-writer generates voice from focalization + Coherence tier + TS + Spirit + author-weighting calibration. NPC sheets supply the inputs (Convictions, Beliefs, Cultural Background, archetype) — not the output. This is architectural: the synthesis is the voice, not a per-NPC overlay.

### §10.3 Inspiration as structured field — pattern

Two facets per NPC. The audit's recommendation (lift `npc_character_analyses_v30` historical parallels into a structured field):

```
Inspiration:
  historical_parallel: <author-side analytic anchor>
    e.g. Almud → "Wars of the Roses Lancastrian deed-claim under structural assault"
         Maret Uln → "Richard Sorge — sympathy with the country he is sent to manage"
         Yrsa Vossen → "Rosa Luxemburg — visibility as vulnerability"
         Baralta → "Isabella I of Castile / Henry VIII — sovereign authority supersedes Church jurisdiction"
         Cesare → "Cesare Borgia — instrumental Authority for self-aggrandizement"
         Vaynard → "Reinhardt von Lohengramm — cunning in service of pride"
         Edeyja → "the last maintenance technician of a building whose occupants don't know it exists"
  in_character_aspiration: <what the NPC wants to become / what they treat as a model>
```

Distinct from PC Inspirations (`articulation_layer §2.4` — player-authored aspirational arcs). NPC Inspirations are **author-given**, not player-side.

---

## §11 Decision Log

Decisions made in producing this consolidation. Surfaced rather than silently resolved.

| # | Decision | Resolution |
|---|---|---|
| **D1** | Conviction values when sources conflict (e.g., Maret Uln: behavior says Equity/Reason; migration roster says Honor/Authority/Identity. Yrsa Vossen: behavior says Equity/Continuity; migration roster says Honor/Warden/Community.) | Use `conviction_migration_roster_v30` (PP-685) values as **primary** in per-NPC sheets — most-recent canonical. Show legacy values inline as "← was [old]" for traceability. Flag any case where I'm uncertain with `[CONFLICT-RESOLVE: <which I picked> — basis: <why>]`. **Do not attempt to silently regenerate `npc_behavior §2` from migration roster** — that's a separate propagation cycle. |
| **D2** | Ethical Framework labels SUPERSEDED per PP-684 §6 + alias_registry, but still embedded in `npc_behavior §2` and mechanically active via Ob modifiers | Retain as **descriptive disposition tag** ("Crown / Virtue legacy") with `[SUPERSEDED → mechanical role replaced by PP-686 §3.7 triadic Ob calc]` note. Mechanical Ob modifiers stay attached to the label since they're live in engine. **Do not silently re-derive Ob modifiers from conviction vector** — that's a separate cycle. |
| **D3** | Tier-3 NPCs (Inner Circles / Cardinal Officers / Jarl Council) carry only Conviction + MS + Certainty + 1-line note. Below prose-writer minimum. | Mark `[GAP — Phase B authoring]` per missing field per NPC. **Do not invent.** Recommend texture-floor extension: ≥1 Belief + ≥1 Goal + ≥1 Inspiration per Tier-3 NPC. |
| **D4** | Empty-body sections (Vaynard Arc A and Arc B in `npc_behavior §5.2`; ~5 character_analyses entries title-only; ~40% of foil pairings; redirect-stub sections in `npc_behavior §1.2 / §3.3 / §3.4` pointing to stale `conviction_track_v1`) | Surface what exists; flag `[GAP]` for empty bodies. **Do not fabricate.** |
| **D5** | Spirit values absent from canonical NPC sheets; prose-writer treats Spirit as third independent axis at Coherence ≤ 4 | Default Spirit 4 (mid-range neutral) per prose-writer guidance. Flag with `[ASSUMPTION]` per NPC where applied. Where design pressure clearly diverges (Edeyja high; Vaynard at Arc C low), note the pressure but do not author specific value. |
| **D6** | Baralta (Hafenmark sovereign claimant) misfiled in `migration_roster §2.3` under "Ecclesiastical Faction" with cultural template `ecclesiastical` | **Surface, do not fix.** Per-NPC sheet shows `[CONFLICT: migration_roster §2.3 places under Ecclesiastical with template "ecclesiastical"; npc_behavior §2.3 places her in Hafenmark with Categorical Imperative framework. Recommend correction to hafenmark_procedural template — defer to Jordan.]` |
| **D7** | Cesare and Lorenzo (Crown succession alternates per migration_roster §2.1) are not in `npc_behavior §2` named-NPC roster but have full conviction profiles in migration roster | Include as Tier 1 / 2 succession-alternate entries. Mark status `succession_alternate (per sim §1.2)` rather than authored-active. Profiles drawn entirely from migration roster + sim continuity. |
| **D8** | Piety Track (`conviction_track_v1.md`) Scar mechanic remains canonical; the 9-Conviction taxonomy it indexes is stale | Reference Scar mechanic at §6 above. Crisis-table d6 entry "5: Autonomy" remapped to "Liberty" per PP-684 §6 alias_registry. Source file's stale taxonomy preserved as historical reference until source-file propagation cycle runs. |

---

**End of PART A — FRAMEWORK.**

PART B — NPC SHEETS pending Q1 scope decision (37 NPCs full vs Tiers 1+2 only). Schema and decision log above lock the structure regardless of final scope.
