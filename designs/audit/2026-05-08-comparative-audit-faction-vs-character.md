# Comparative Audit — Faction Canon vs Character Canon Frameworks
## Date: 2026-05-08 · Status: PROVISIONAL analytical document.

---

## §1 — Side-by-side section comparison

| Faction canon §N | Content | Character canon §N | Content | Parallel? |
|---|---|---|---|---|
| §1 | Status / scope / supersession | §1 | Status / scope / supersession | **Yes** — same structure |
| §2 | Per-faction sheet schema | §2 | Per-NPC sheet schema | **Yes** — same structure, different fields |
| §3 | PP-686 4-component model (Mission/Cascade/PE/L+PS) | §3 | Conviction substrate recap (PP-684 13-Conviction + cultural templates + 4-axis) | **Partial** — both are substrate but faction has its own 4-component architecture |
| §4 | Role templates + expected_convictions | §4 | Self-Other orientation | **No** |
| §5 | Stat lineup (7-stat, L+PS scope DESIGN-ISSUE) | §5 | Resonant Style taxonomy (4 styles) | **No** |
| §6 | Public Temperament (5 types) | §6 | Belief / Scar / Conviction-crisis | **No** |
| §7 | Nine Political Axes | §7 | Three orthogonal personal-scale axes (TS/Coherence/Spirit/Certainty) | **No** — but structurally analogous (both are multi-axis positioning systems) |
| §8 | Stability mechanics (5 triggers + recovery + collapse) | §8 | Arc state machine (generic triggers) | **Partial** — both are change-over-time mechanics |
| §9 | Tactic / Unique Action overview | §9 | Tier system | **No** |
| §10 | Sub-organization layers | §10 | Voice anchors + prose-feedstock | **No** |
| §11 | Partial sheet handling | §11 | Decision log (D1–D8) | **No** |
| §12 | Decision log (D1–D7) | — | — | Faction has extra section |

**Finding:** the files share bookends (§1 Status, final § Decision log) and substrate reference (§3 in both). The middle sections diverge. They are NOT currently commensurate.

---

## §2 — Shared substrate (what both reference, neither duplicates)

Both files reference the same canonical documents:

| Substrate document | What it provides | Faction use | Character use |
|---|---|---|---|
| `conviction_taxonomy_v30` (PP-684) | 13-Conviction taxonomy + structured concentration + cultural templates | Role templates (§3.3.1 expected_convictions); aggregate derivation | Personal_convictions (§3.2); cultural background (§3.3) |
| `conviction_axis_matrix_v30` | 13→4-axis projection matrix | Armature_position for faction-role context | Armature_position for personal context |
| `conviction_migration_roster_v30` (PP-685) | Per-NPC 13-Conviction mapping | Leader Conviction values for cascade input | Per-NPC Conviction values |
| `faction_behavior_v30` (PP-686 v2) | 4-component faction model + cascade math | Primary architecture document | §3.5 effective_convictions; §3.8 dual-armature |
| `key_substrate_v30` (PP-687) | Key type system + subscription | Mission alignment Keys; faction state-change Keys | Scene Keys; Belief-engagement Keys |
| `articulation_layer_v30` (PP-688) | Cut scene triggers + Belief engagement | Faction-event triggers (#6 Domain Echo) | NPC-event triggers (#1–#10); per-Belief engagement counts |

**The conviction taxonomy (PP-684) is the true shared substrate.** Both files consume it; neither modifies it. The cascade math (PP-686 §3.2) is the formal bridge — it transforms personal-scale Convictions into faction-scale aggregates. This is the system's strongest architectural claim: one vocabulary, two scales, clean derivation.

---

## §3 — Asymmetries (what exists at one scale only)

### §3.1 Character-scale only (no faction equivalent)

| Mechanic | Why no faction equivalent |
|---|---|
| **Resonant Style** (4 types) | Factions don't have argument-shape vulnerability. A faction is influenced through Domain Actions, Parliament, Treaties — not through Evidence/Consequence/Authority/Solidarity targeting. |
| **Beliefs** (first-person truth-statements) | Factions have Mission (a stated telos), not first-person quoted Beliefs. Mission is public and declared; Beliefs are private and often unrevealed. Different objects. |
| **Conviction Track / Scars** | Factions don't accumulate moral wounds. Stability is the faction-scale equivalent of institutional damage, but Stability is a stat, not a narrative track. A faction at Stability 2 hasn't been "scarred" — it's been weakened. |
| **TS / Spirit (metaphysical) / Certainty** | Personal-scale metaphysical axes. Factions don't have Thread Sensitivity, will-to-grip, or cosmological-framework alignment. The faction's substrate-posture (T-15) is the closest analog but is qualitative, not quantified. |
| **Knots / Bonds** | Relational mechanic between individuals. Factions relate via treaties, political axes, and Domain Actions — not via emotional bonds. |
| **Caste** | Individual social position. Factions have institutional roles, not castes. |
| **Disposition** | Per-NPC toward-PC tracker. Factions have institutional stances, not personal feelings. |
| **Behavioral AI flaw** | Per-NPC mechanical individuation. Factions have institutional tendency, not personal flaws. |
| **Sparking** | Skill acquisition during play. Factions don't learn skills — they change stats. |

### §3.2 Faction-scale only (no character equivalent)

| Mechanic | Why no character equivalent |
|---|---|
| **Mission** (formal telos with victory track) | Characters have Goals (implicit, situational) not a formally declared telos with aligned/contradicted DA categories. |
| **Cascade** (hierarchy-blended Convictions) | Characters have raw personal_convictions — no blending from a hierarchy. (effective_convictions is cascade-derived but is a faction-produced overlay on the character, not a character mechanic.) |
| **Public Expectation** (role template × Mission consistency) | No character-level "what the populace expects of you." Closest: Standing + Caste floor determine social expectations, but this is not a Conviction-shaped expectation template. |
| **Legitimacy + Popular Support** (two-scalar populace relation) | Characters don't have populace acceptance. They have Standing (per-faction) and Renown (public). Different structure. |
| **Stability triggers** (5 canonical) | Characters have Coherence (0–10) as self-rendering integrity, but Coherence triggers are different (Thread operations, not military defeats or treaty terms). |
| **Parliament / Treaties / Occupation** | Strategic-layer institutional mechanics. No personal-scale equivalent. |
| **Tactic / Unique Actions** | Faction-signature moves. Characters have skills and Lifepath-derived competencies, but not "one signature faction-level move." |
| **Public Temperament** (per-territory populace disposition) | No character-level equivalent. |
| **Nine Political Axes** (qualitative positioning) | Characters position on the axes via their Convictions, but the axes are defined as faction-level concerns. |

### §3.3 Structural analogs (exist at both scales but work differently)

| Character | Faction | Relationship |
|---|---|---|
| **Coherence** (0–10, self-rendering integrity) | **Stability** (0–7, institutional cohesion) | Analogous: both measure how well the entity holds together under stress. NOT equivalent: Coherence is metaphysical (rendering-layer), Stability is political (institutional-layer). Different triggers, different recovery, different scales. |
| **Beliefs** (first-person truth-statements) | **Mission** (declared institutional telos) | Analogous: both express what the entity asserts as guiding. NOT equivalent: Beliefs are private, multiple, revisable via Contest; Mission is public, singular, shifts under enumerated triggers. |
| **Conviction Track / Scars** (accumulated moral wounds) | **Stability crisis / faction collapse** (accumulated institutional shocks) | Analogous: both produce existential-identity-change under accumulated pressure. NOT equivalent: Scars produce character transformation; collapse produces faction dissolution. |
| **Arc state machine** (generic NPC triggers → arc transition) | **Faction arc trajectory** (e.g., Löwenritter Loyal→Split; Crown Reform/Fortress/Overthrown) | Analogous: both trace entity transformation over campaign. Related: faction arcs are often *driven by* leader's personal arc. |
| **Goals** (per-NPC, currently implicit) | **Mission primary_objective** (per-faction, authored) | Analogous: both express what the entity is trying to accomplish. NOT equivalent: Goals are personal and situational; Mission is institutional and tied to victory conditions. |
| **Cultural template** (per-NPC, 8 types) | **Faction identity** (implicit in role + leader + doctrine) | Analogous: both express cultural grounding. Related: templates map to factions (valorian_court → Crown; ecclesiastical → Church). |

---

## §4 — Should they be commensurate?

### §4.1 Arguments for commensurability

- **Same vocabulary** (Convictions) at both scales → same §-structure would reinforce that unity.
- **Cascade math** formally bridges scales → parallel structure would make the bridge visible.
- **A reader who learns one framework can navigate the other** if structure is parallel.
- **Cross-referencing** is cleaner with matched §-numbers.
- **Reveals structural parallels** (Stability ↔ Coherence; Mission ↔ Belief; Cascade Fidelity ↔ Conviction Track) that are architecturally important.

### §4.2 Arguments against commensurability

- **Forced symmetry distorts.** Factions have Stability; characters have Coherence. They are analogous but NOT equivalent. Forcing them into the same § implies equivalence that doesn't exist. A reader who thinks "character Coherence = faction Stability" will make wrong predictions.
- **Different readers for different purposes.** A faction designer doesn't need to know about TS/Coherence/Spirit. A character designer doesn't need to know about Parliament mechanics. Parallel structure invites irrelevant reading.
- **Each file should be navigable standalone.** If understanding the character framework REQUIRES understanding the faction framework's parallel §-structure, the files aren't standalone — they're half-documents.
- **The middle sections genuinely diverge.** 8 of 12 sections don't parallel. Commensurability would require either (a) adding stub sections in each file for the other's unique content ("§X — Parliament: see faction_canon") or (b) restructuring both files around a shared template that doesn't match either domain well.

### §4.3 Recommendation: partial commensurability

**Commensurate sections** (same §-number, same structural role):
- §1 Status / scope / supersession
- §2 Per-entity sheet schema
- §3 Substrate reference (both reference PP-684; faction adds PP-686 4-component recap)
- §(last) Decision log

**Independent sections** (numbered per-domain, no forced parallelism):
- Everything else. Faction covers faction mechanics in whatever order serves a faction designer. Character covers character mechanics in whatever order serves a character designer.

**Cross-scale bridge appendix** (new, added to both files):
- A shared appendix (same content in both files) mapping which mechanics bridge scales and how. This is where the structural analogs table lives. It's the "how this connects to the other scale" reference — available but not embedded in the framework flow.

This preserves: standalone navigability, honest treatment of asymmetries, and cross-scale visibility via the appendix.

---

## §5 — Organization and categorization

### §5.1 Current structure assessment

Both files use a flat §-numbered sequence. This works for 11–12 sections. If sections grow (e.g., adding the cross-scale appendix, expanding the schema), the flat sequence becomes harder to navigate.

### §5.2 Categorical grouping option

Instead of flat numbering, group sections by functional role:

**Faction canon:**
```
IDENTITY      — §1 Status · §2 Schema · §3 Substrate
BEHAVIOR      — §4 Role templates · §5 Stats · §6 Temperament · §7 Axes
DYNAMICS      — §8 Stability · §9 Tactics · §10 Sub-orgs · §11 Partial sheets
GOVERNANCE    — Decision log · Cross-scale bridge appendix
```

**Character canon:**
```
IDENTITY      — §1 Status · §2 Schema · §3 Substrate
PERSONALITY   — §4 Self-Other · §5 Resonant Style · §6 Belief/Scar
METAPHYSICAL  — §7 TS/Coherence/Spirit/Certainty
BEHAVIORAL    — §8 Arcs · §9 Tiers · §10 Voice anchors
GOVERNANCE    — Decision log · Cross-scale bridge appendix
```

This produces: IDENTITY (shared structure) → DOMAIN-SPECIFIC (middle, ungrouped across files) → GOVERNANCE (shared structure). The "sandwich" pattern — commensurate outer layers, independent inner layers.

### §5.3 Recommendation

The categorical grouping adds organizational clarity at the cost of an extra indirection layer. For files at 11–12 sections this is marginal. **Recommendation: keep flat numbering; add the cross-scale bridge appendix as a final section before the Decision log in both files.** Revisit categorical grouping if either file exceeds ~20 sections.

---

## §6 — Mechanics mapping (which uses what, which bridges scales)

### §6.1 The conviction substrate — consumed by everything

```
conviction_taxonomy_v30 (PP-684)
  ├── character_canon: personal_convictions per NPC (§3.2)
  ├── character_canon: cultural templates per NPC (§3.3)
  ├── faction_canon: expected_convictions per role template (§4)
  ├── faction_canon: aggregate via cascade (§3.2)
  ├── Contest system: Conviction Track targeting
  ├── Articulation Layer: Belief engagement + cut scene triggers
  ├── prose-writer: voice anchoring from Conviction weights
  └── questionnaire: derivation target (§2 of questionnaire design)
```

### §6.2 Mechanics that bridge scales (directional)

| Bridge | Character → Faction | How |
|---|---|---|
| **Cascade aggregation** | NPC personal_convictions aggregate via α-weighted hierarchy into faction aggregate_effective_convictions | PP-686 §3.2: `effective = α × personal + (1-α) × supervisor's effective`. Faction aggregate = Standing-weighted sum. |
| **Self-Other → PS attribution** | Leader's Self-Other modulates how Mission outcomes are attributed to faction's Popular Support | PP-686 §3.4: `attributed_outcome = raw × (1 − 0.5 × max(0, leader.self_other))`. Self-aggrandizing leaders see reduced PS attribution. |
| **Leader Scar ≥ 3** | Leader Conviction in crisis | PP-686 §3.2.5: cascade damping suspended — new leader Convictions propagate immediately. Produces visible institutional instability. |
| **Belief revision of leader** | Leader's personal_convictions shift | Cascade re-resolution triggered. `mechanical.cascade_resolution` Key emitted with old + new values. |
| **Succession** | New leader's personal_convictions | PP-686 §3.1 trigger 2: immediate cascade re-resolution. New aggregate computed from new leader + existing hierarchy. |
| **Domain Echo** | Personal-scene outcome | scale_transitions §3.4: personal-scene outcome modifies Domain Action roll (+1D, etc.). |
| **Standing** | Per-NPC Standing in faction (rank ladder) | Standing determines NPC's weight in faction aggregate (§3.2.6); Standing determines NPC's social access and rank-gate content. |

| Bridge | Faction → Character | How |
|---|---|---|
| **Stability ≤ 1** | NPC Conviction collapses to Liberty | Arc state machine §8.1: faction Stability ≤ 1 → all NPCs in faction enter "any action that improves Stability" mode; Convictions collapse to Liberty. |
| **Mandate < 3** | NPC enters Constrained sub-arc (ED-586) | Priority 2/3 actions replaced by Priority 6 (institutional rebuilding). Conviction and Resonant Style unchanged; behavioral priority shifts. |
| **Faction collapse (Stability = 0)** | All NPCs enter Independent status | faction_layer §1.5 Step 3: named officer NPCs retain Conviction/Beliefs/Disposition but lose faction affiliation. Recruitable by other factions. |
| **effective_convictions overlay** | NPC in faction-role context uses cascade-derived effective_convictions instead of personal_convictions | PP-686 §3.8: `role_acting = true` → effective_convictions; `role_acting = false` → personal_convictions. Dual-armature. |
| **Mission alignment → Ob** | NPC's Domain Action Ob modified by Mission alignment | PP-686 §3.7: `Ob_modifier = mission + cascade + expectation`, clamped ±2. |

| Bridge | Bidirectional | How |
|---|---|---|
| **Standing ↔ rank ladders** | NPC Standing determines rank in faction hierarchy; rank determines NPC's weight in faction aggregate AND social access | faction_politics §1.0–1.4 rank ladders + PP-686 §3.2.6 Standing-weighted aggregate. |

### §6.3 Mechanics consumed by the prose-writer

The prose-writer skill (`skills/prose-writer/SKILL.md`) consumes from both layers:

| Source | What prose-writer reads | From which file |
|---|---|---|
| Conviction vector | Primary 1–3 Conviction weights; cultural template | Character |
| Beliefs | First-person quoted voice anchors | Character |
| TS / Coherence / Spirit | Coherence-tier → author-weighting; Spirit → Beckett/Lispector texture; TS → perception-access | Character |
| Conviction voices (proposed) | Per-Conviction characteristic claims; engine surfaces 1–2 per scene | Character (proposed addition) |
| Speech register (proposed) | Per-NPC diction/register descriptor | Character (proposed addition) |
| Textural hooks (proposed) | Per-NPC queryable memories from questionnaire | Character (proposed addition) |
| Faction identity | Leader + Mission + doctrine notes | Faction |
| Nine Political Axes | Faction positioning for Domain Echo framing | Faction |
| Substrate-Posture (T-15) | Faction-level metaphysical stance for leader voice | Faction |

### §6.4 Mechanics consumed by the questionnaire

The unified questionnaire (proposed) produces output that maps to both frameworks:

| Questionnaire output | Character canon field | Faction canon field |
|---|---|---|
| Conviction vector (derived) | personal_convictions (§3.2) | Cascade input (§3.2) if NPC is faction member |
| Self-Other (derived) | Self-Other orientation (§4) | PS attribution modifier if NPC is leader |
| Cultural template (derived) | Cultural background (§3.3) | — |
| Beliefs (derived) | Beliefs (1–3 quoted) | — |
| Goals (derived) | Goals (currently implicit) | — |
| Histories (derived) | Lifepath histories + skills | — |
| TS / Certainty (derived) | Personal-scale axes (§7) | — |
| Textural hooks (new) | Per-NPC queryable memories | — |
| Starting Knots (derived) | Knots/Bonds (§relational) | — |

The questionnaire output is overwhelmingly character-side. The faction-side connection is indirect: NPC character state feeds into faction behavior via cascade math. The questionnaire does not produce faction-level state directly — it produces NPC state that the faction machinery then consumes.

### §6.5 Which mechanics are cross-scale singletons

Some mechanics exist only at the junction between scales, not cleanly at either:

| Mechanic | Why it's cross-scale |
|---|---|
| **effective_convictions** | Computed FROM personal (character) BY cascade (faction). Not a character mechanic (character doesn't author it); not a faction mechanic (faction doesn't store it on individual NPCs). It's a derived quantity that exists at the junction. |
| **Substrate-Posture** | Authored at faction level; expressed through leader's personal worldview. Not clearly character or faction. |
| **Domain Echo** | Personal-scene outcome → faction-layer Domain Action modifier. The mechanic IS the bridge — it doesn't live at either scale. |
| **Standing** | Per-NPC quantity that determines rank in faction hierarchy AND individual social access. Bidirectional bridge. |

These should be documented explicitly in the cross-scale bridge appendix, not forced into either file.

---

## §7 — Recommendations

### §7.1 File structure

**Keep two files.** Partial commensurability: §1, §2, §3, and Decision log (last §) parallel; middle sections independent. Add cross-scale bridge appendix as penultimate section in both (same content duplicated — the bridge table from §6.2 above).

### §7.2 Naming

Align field names where concepts parallel:

| Faction field | Character field | Aligned name |
|---|---|---|
| Mission (text) | Goal (proposed first-class field) | Keep distinct — they ARE different. Mission is institutional telos; Goal is personal. |
| L + PS | — | No character-scale equivalent; don't force one. |
| Stability | Coherence | Keep distinct names — analogy acknowledged in bridge appendix. |
| expected_convictions | personal_convictions | Keep distinct — one is role-template-derived, one is identity-authored. |
| cascade_fidelity | — (no character equivalent) | Keep faction-only. |
| Institutional Beliefs (proposed, per-faction voice anchors) | Beliefs (per-NPC voice anchors) | Could align: both are "first-person voice anchors for the prose-writer." The faction version is institutional voice; the character version is personal voice. Same field name, qualified: `beliefs.institutional` vs `beliefs.personal`. |

### §7.3 Schema alignment

Both schemas should include:

**Shared fields** (same name, same purpose, different scale):
- Identity
- Convictions (personal vs expected/aggregate)
- Beliefs (personal vs institutional)
- Strategic Goals (personal vs Mission)
- Inspiration (personal vs institutional historical anchoring)
- Provenance

**Scale-specific fields** (unique to one schema, clearly marked):
- Character-only: Resonant Style, TS/Coherence/Spirit/Certainty, Knots, Disposition, Caste, Behavioral AI, Arc Map, Speech Register, Sensory Anchor
- Faction-only: Mission (full spec), L+PS, Stats (7-stat), Stability triggers/recovery, Tactic/Unique Action, Sub-orgs, Partial sheets, Public Temperament, Nine Political Axes, Doctrine Notes

### §7.4 Questionnaire integration

The questionnaire produces character-state objects. These feed into faction-state objects via cascade math. The questionnaire itself does not need to reference the faction framework — it references the character schema only. The faction framework consumes the character framework's output.

This means: the questionnaire design document references `character_canon_v30 §2` (schema) and `conviction_taxonomy_v30` (substrate). It does not reference `faction_canon_v30` directly.

### §7.5 What should change in existing files

**character_canon_v30 §2 (schema):** add Goal as explicit first-class field (currently implicit). Add cross-scale bridge appendix as §12 (before Decision log). Align Beliefs field name with faction-side Institutional Beliefs concept (document the parallel, don't rename).

**faction_canon_v30 §2 (schema):** add cross-scale bridge appendix as §13 (before Decision log). Document that per-faction Institutional Beliefs parallel per-NPC Beliefs for prose-writer consumption.

**Both files:** add the §6.2 bridge table (directional mechanics mapping) as the cross-scale appendix content.

---

## §8 — Summary finding

The two frameworks are **rightly asymmetric.** Factions and characters ARE different things; they need different sections covering different mechanics. Forced commensurability would distort both.

What they share is **substrate** (PP-684 Conviction taxonomy) and **bridge mechanics** (cascade math, Standing, Domain Echo, effective_convictions). These shared elements should be documented explicitly in a cross-scale appendix in both files, not hidden in the middle of domain-specific sections.

The strongest structural claim: **one vocabulary (Convictions), two scales (personal/institutional), clean derivation (cascade math), documented bridges (appendix).** The files don't need to look the same. They need to be navigable standalone while making the bridges visible.
