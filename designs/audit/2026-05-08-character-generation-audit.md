# Valoria — Character Generation & NPC Texture Audit
## NERS + Prose-Feedstock Adequacy
### 2026-05-07 · max-effort full-coverage audit

**Scope.** The character generation process and the NPC roster, evaluated on two axes:
1. **NERS** — Necessary, Elegant, Robust, Smooth (canon_terms PI).
2. **Prose-feedstock adequacy** — does the texture data give the prose-writer skill enough anchored dimensions to render NPCs compelling and real?

**Files audited (full read).** Conviction stack (4); articulation layer (1); NPC bundle (10 docs covering roster, behavior, analyses, foils, two individual NPC docs); character histories lifepath (3 files); stance triangles (1); faction identity sample (1); prose-writer SKILL.md + calibration skeleton (consumer side). Total ~123k tokens of source material; verification loop applied to top findings.

---

## 1. Texture infrastructure as it actually exists

The character-texture stack is spread across five layers and at least seven files per significant NPC. There is no single canonical sheet.

| Layer | File(s) | What it carries | Status |
|---|---|---|---|
| Conviction substrate | `designs/personal/conviction_taxonomy_v30.md`, `conviction_axis_matrix_v30.md`, `conviction_migration_roster_v30.md`, `conviction_track_v1.md`, `params/factions/npc_stance_triangles.md` | Conviction vector, axis projection, cultural template, Self-Other orientation, drift dynamics, per-NPC migration mapping | **Three incompatible Conviction taxonomies coexist as canonical** (see §4 P1) |
| Articulation | `designs/articulation/articulation_layer_v30.md` | Tier 1/2/3 surfacing of state to player; trigger ruleset; Knot/Belief/Inspiration integration | Strong; PROVISIONAL pending ratification |
| NPC roster + behavior | `designs/npcs/npc_roster_v30.md`, `npc_behavior_v30.md`, `npc_character_analyses_v30.md`, `npc_foils_v30.md`, individual docs (`baralta_v30.md`, `edeyja_npc.md`, `companion_specification_v30.md`) | Stance triangles, ethical frameworks, behavioral AI, beliefs, arc maps, character analyses, foil dynamics, per-NPC deep dives | Rich for tier-1 NPCs; thin for inner-circle/tier-2; multiple empty-body sections |
| PC generator | `designs/world/character_histories_v30.md` (+ index, infill) | 4-stage Burning Wheel-style lifepath: Origin / Formation / Vocation / Catalyst. Generates skills, Knots, starting Belief | Strong as PC tool; **does not apply to NPCs** |
| Faction identity | `params/factions/riskbreakers_identity.md` and similar | Faction operational/ethical identity | Mixed; mostly editorial-resolution log rather than profile |

**The prose-writer is the consumer.** From `skills/prose-writer/SKILL.md` line 153:

> "Load-bearing NPCs need at least one anchored dimension (ethical framework, conviction, goal, inspiration, factional belonging)."

That is the explicit minimum the prose-writer demands. The audit's prose-feedstock pass evaluates against exactly this list plus the implicit voice anchors the skill consumes.

---

## 2. NERS scorecard

| Component | N | E | R | S | Notes |
|---|:-:|:-:|:-:|:-:|---|
| Conviction Taxonomy v30 (PP-684) | ✓ | ✓ | ✓ | ⚠ | Each conviction earns its place via Renaissance political ethics. 13D vector × 8 cultural templates × Self-Other axis × drift produces wide character space. Smoothness is dragged by downstream files that haven't migrated. |
| Conviction Axis Matrix | ✓ | ✓ | ✓ | ✓ | Per-row historical calibration is the model for how a substrate doc earns its claims. Acknowledges 4-axis collapses (Community ↔ Identity especially) — intellectually honest. |
| Conviction Migration Roster | ✓ | ✓ | ⚠ | ✗ | Maps 9 named legacy NPCs to 13-conv taxonomy. R-weakness: per-NPC notes are 2–4 lines (thin for prose-writer pull). S-fail: produces values that **conflict** with `npc_behavior_v30 §2` for the same characters (Maret Uln, Yrsa Vossen, Baralta — see §5). |
| Conviction Track v1 | ⚠ | ✓ | ✓ | ✗ | Marked CANONICAL but uses **stale 9-Conviction taxonomy** (Reason/Autonomy/Continuity — retired by PP-684). The Scar mechanic itself is sound; the taxonomy it indexes is dead. |
| Stance Triangles (params) | ⚠ | ✓ | ✓ | ✗ | Marked canonical but uses **stale 7-Conviction taxonomy.** Framework Drift table uses the SUPERSEDED ethical-framework labels (Virtue Ethics / Categorical Imperative / Divine Command / etc.). |
| Articulation Layer | ✓ | ✓ | ✓ | ✓ | Tier 1/2/3 architecture is load-bearing. 10-trigger ruleset is specific. `accumulated_narrative_weight` prevents narrative starvation — strong R. One internal contradiction: §2.4 says Beliefs are "player-authored" (protagonist-only) but §3.1 trigger #10 fires on `state.belief_revised` for any tracked NPC. |
| `npc_behavior_v30` (the 22.5k-token monolith) | ⚠ | ✗ | ✓ | ✗ | Necessary content (§2 stance triangles, §3 belief mechanics, §5 arc maps) but elegance-fail: §1.2 is now an empty redirect, §3.3 is an empty redirect, §3.4 is an empty redirect — each pointing to `conviction_track_v1` which itself is stale. The file is ~30% redirect stubs. **PP-681 promotion drained the file but didn't update what remained.** |
| `npc_roster_v30` | ✓ | ✓ | ✓ | ⚠ | 13 supporting NPCs with rich Behavioral AI + ethics + compromise per entry. Strong. S-weakness: doesn't cover the ruler diamond (Almud / Lenneth / Baralta / Vaynard) — those live in `npc_behavior_v30` and `npc_character_analyses_v30 PART TWO`. Coverage is split. |
| `npc_character_analyses_v30` | ✓ | ✓ | ✓ | ⚠ | Best per-NPC literary framing in the stack (titled essays: "The Last Maintenance Technician", "The Inquisitor's Uncertainty Principle", "The Ledger That Never Forgives"). Historical parallels function as inspirations. **E-fail in execution:** PART TWO has multiple empty-body entries (Cardinal Jarnstal #10, Vaynard #5, Cardinal Klapp #8, Cardinal Olafsson #9, Ehrenwall #11 are all 14–43 tokens — title only or one-line). Status DESIGN, not CANONICAL. |
| `npc_foils_v30` | ✓ | ✓ | ✓ | ✗ | Strong concept (4 axes × 6 pairings × 4 perspective views × 4 triangular foils). **S-fail in execution:** the skeleton file is mostly empty headers; body text is in the infill but distribution is uneven. ~40% of pairings have empty bodies. |
| Individual NPC docs (Edeyja, Baralta) | ✓ | ✓ | ✓ | ⚠ | Edeyja's doc is the gold standard — role, background, stats, Conviction, lineage, military reality, faction relationships, player access table, GM presence notes, canon compliance. Baralta's doc (PROVISIONAL) is a theological deep-dive. **N-gap:** these are the only two named NPCs with individual docs. The other ~30 named NPCs have no equivalent. |
| Character Histories (PC lifepath) | ✓ | ✓ | ✓ | ⚠ | 4-stage Burning Wheel-style lifepath. Each stage produces skills, Knots, and starting Belief. Stage 4 produces the player's starting Belief — clean integration with articulation_layer §2.4. **S-gap:** does not bridge to NPC generation. NPCs do not pass through this system; they are author-defined. |

**Summary read.** The substrate (Conviction Taxonomy + Axis Matrix + Articulation Layer) is N/E/R-strong and S-strong within its own boundary. The instantiation layer (per-NPC files) is N/R-strong for tier-1 NPCs and S-failing across files. The migration debt from PP-684/PP-681 is the largest single drag on Smoothness in the texture stack.

---

## 3. Prose-feedstock adequacy by dimension

The prose-writer skill's anchored-dimension list is the test. Five dimensions named (line 153) plus implicit voice/Spirit/TS/Coherence inputs.

| Dimension | Status | Where it lives | Verdict |
|---|---|---|---|
| **Ethical framework** | CONFLICTED / STALE | `npc_behavior_v30 §2` (every named NPC has explicit framework + Ob modifiers); stance_triangles Framework Drift table | The labels (Virtue Ethics, Divine Command, Categorical Imperative, Consequentialist Pragmatism, Rawlsian Social Contract, Moral Relativism, Martial Honour) are SUPERSEDED per `references/alias_registry.yaml` (PP-684 §6). A prose-writer pulling Almud's "ethical framework" gets canonically-retired data. The replacement (conviction-vector-based ethics via the Axis Matrix) hasn't reached `npc_behavior_v30`. |
| **Conviction** | CONFLICTED | 5+ files; same NPC has different convictions in different files | **Largest correctness risk for prose-writer.** Maret Uln: behavior says Equity/Reason; migration roster says Honor/Authority/Identity. Yrsa Vossen: behavior says Equity/Continuity; migration roster says Honor/Warden/Community. Baralta: behavior says Precedent/Faith (Hafenmark); migration roster says Faith/Virtue/Warden (ecclesiastical) — and the cultural template in roster is wrong (she's Hafenmark sovereign-claimant, not ecclesiastical). |
| **Goal** | IMPLICIT ONLY | Embedded in `npc_roster_v30` Behavioral AI fields, in `npc_behavior_v30 §5.2` arc maps, and in `npc_character_analyses_v30` arc trajectories | Adequate for tier-1 NPCs but requires synthesis across 2–3 sources. No explicit "goal" field on any NPC sheet. Prose-writer cannot pull a clean goal statement; must infer. For tier-2 NPCs, goal is absent or one-line. |
| **Inspiration** | LARGEST GAP | Historical parallels exist in `npc_character_analyses_v30` only — Sorge (Maret Uln), Luxemburg (Vossen), Henry VIII / Isabella I (Baralta), Cesare Borgia (Cesare). These are author-side analytical anchors, not in-character aspirations. | The prose-writer's "inspiration" dimension has no canonical NPC field. The articulation_layer treats Inspirations as **player-authored, protagonist-only** (§2.4). NPCs don't have aspirational arcs as queryable data. The historical parallels in character_analyses serve this implicitly for ~13 NPCs in prose form only. **The sharpest single gap in the prose-feedstock stack.** |
| **Factional belonging** | CLEAN | Every NPC has faction in roster + behavior + cultural label in migration roster | The cleanest dimension. Single point of truth (faction) is consistent across files. Cultural label (per migration roster) is the one place this dimension is sometimes wrong (Baralta misclassified ecclesiastical). |
| (implicit) **Voice anchor** | UNEVEN | First-person Beliefs in `npc_behavior_v30 §2` ("Order is not made — it is maintained.") | Where present, these are excellent — they ARE voice samples. Coverage is uneven: Almud has 2 (numbered 2 and 3, missing #1), Torben has zero (Belief block is empty), Vossen has only #3. Stance triangles file has none. |
| (implicit) **Speech register / lexical signature** | OFFLOADED | Prose-writer SKILL.md handles this via Lexical Register, Grammar Latitude, and per-coherence-tier author weighting. NPC files don't carry per-NPC speech-style. | Architectural choice (engine-state drives register) rather than gap, but worth flagging: the prose-writer cannot consult an NPC sheet to learn how that NPC sounds. The synthesis is generated from focalization + coherence + TS + Spirit, not from the NPC's own data. |
| (implicit) **Physical signature** | NEAR-ABSENT | Edeyja has visible Thread injury (legible at TS 15+). Almost no other NPC has a physical descriptor. | The prose-writer skill stresses physical presence (Self-Check items 11, 14: "Is the physical world present?"). NPC files supply almost none. Prose-writer must invent or omit. |
| (implicit) **Coherence / TS / Spirit** | TS PRESENT, COHERENCE/SPIRIT PARTIAL | TS values are explicit per NPC (Almud 28, Himlensendt 0, Edeyja 75–80, etc.). Coherence has rules in `npc_behavior_v30 §4.3` but per-NPC values are scattered (Edeyja 9, Almud not specified). Spirit is rarely specified. | TS is clean. Coherence baselines exist but aren't consistently authored per NPC. **Spirit is essentially absent from NPC sheets** — yet the prose-writer treats Spirit as the third independent axis at coherence ≤ 4 (Beckett vs Lispector textures). Per-NPC Spirit values should exist. |

### Tier asymmetry (orthogonal to per-dimension verdict)

| Tier | NPCs | Texture density | Prose-feedstock adequacy |
|---|---|---|---|
| Tier 1 (faction principals) | Almud, Lenneth, Himlensendt, Baralta, Vaynard, Ehrenwall, Vossen, Hann, Edeyja, Maret Uln, Lennart Haelgrund, Torben, Aldric Hann | Profiles in 4–5 files each; multiple beliefs; arc maps; foil networks; literary parallels | **Adequate for compelling-and-real prose.** |
| Tier 2 (operational supporting) | The 13 in `npc_roster_v30`: Sigrid Torsvald, Halvar Brandt, Annika Feldhaus, Peder Almstedt, Gerik Strand, Dalla Virke, Doux Alexios Laskaris, Rikard Solberg, Sæmund Haelgrund, Aldric Tormann, +3 | Roster entry (~200–400 tokens) + character analysis entry (~150–300 tokens). Behavioral AI + ethics + compromise + arc trajectory | **Adequate. Most files I would tap for tier-1 are absent for these — but `npc_roster` itself is dense enough.** |
| Tier 3 (Inner Circles / Council members) | Crown IC (Voss, Reichard, Thale, Linder, Kreutz); Hafenmark IC (Heljason, Geirson); Varfell Jarl Council (Holdar, Stenskald); Cardinal Officers (Klapp, Olafsson, Jarnstal, Tormann) | One-line table row in `npc_behavior §2.15-2.17`. Conviction tag + MS + Certainty + brief disposition note. **No beliefs. No resonant style. No arc.** | **INADEQUATE.** If any of these surface in a Tier 2 cut scene per articulation layer (and they will — Mathilde Heljason as Baralta's legal advisor is an obvious cut-scene presence), the prose-writer has no anchored dimension to draw from beyond a single conviction word. |
| Empty-body | character_analyses Cardinal Jarnstal (#10, 43 tokens), Cardinal Klapp #8 (14 tokens), Cardinal Olafsson #9 (16 tokens), Ehrenwall #11 (15 tokens), Vaynard #5 (14 tokens); npc_behavior Vaynard Arc A and B; ~40% of foil pairings | Title only or one sentence | **Critical gap.** The titles imply texture exists; the bodies say it doesn't. |

---

## 4. Top findings (ranked by leverage)

### P1 — Conviction taxonomy schism (3-version conflict, S-critical)

Three Conviction taxonomies are simultaneously canonical:

| Source | N | List |
|---|---|---|
| `npc_stance_triangles.md` | 7 | Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity |
| `conviction_track_v1.md` §1 + `npc_behavior_v30 §1.2` (redirect) | 9 | the 7 + Community + Warden |
| `conviction_taxonomy_v30.md` (PP-684) + `axis_matrix_v30.md` + `migration_roster_v30.md` | 13 | Faith, Authority, Order, Scholastic, Utility, Equity, Liberty, Precedent, Community, Identity, Warden, Virtue, Honor |

The migration roster (PP-685) was authored to bridge legacy → 13-conv, but downstream files (track, triangles, behavior §2 stance entries) **still use the legacy convictions**. The 9-conviction reference in `npc_behavior_v30 §1.2` redirects to `conviction_track_v1.md` which itself is the stale source. The redirect points at a dead document.

**Concrete consequence**: same NPC with different convictions in different files (verified §5).

**Fix scope**: regenerate stance triangles (7→13), regenerate `conviction_track_v1` to consume PP-684, regenerate `npc_behavior §2` stance triangle entries from `migration_roster §2`. The migration mapping data is already there; downstream files just need to consume it.

---

### P2 — Per-NPC sheet fragmentation (E + S double-fail)

A single named NPC has profiles distributed across at minimum:

```
For Almud Almqvist:
  designs/npcs/npc_behavior_v30.md §2.1            (stance triangle, beliefs, framework)
  designs/npcs/npc_character_analyses_v30.md §1   (literary analysis: "The Competent Custodian")
  designs/npcs/npc_foils_v30.md                    (paired with Lenneth, Baralta, Vaynard × 6 dyads)
  designs/personal/conviction_migration_roster_v30.md §2.1.Almud   (13-conv mapping)
  designs/npcs/npc_behavior_v30.md §5.2            (Arc Map A/B/C/D/E/F)
  references/character_histories canon (occasional cross-references)
```

There is no canonical NPC sheet from which these are projected. The migration roster + `npc_behavior §2` give incompatible conviction profiles for at least three NPCs (Maret Uln, Vossen, Baralta). The reader cannot construct "everything we know about Almud" from any single file.

**Fix scope**: define a per-NPC sheet schema (probably YAML); migrate existing data into it; make the existing files (roster, analyses, foils, behavior triangles) generated views or merge them. **This dissolves both P1 and P2 if done well**, because the per-NPC sheet is where 13-conv lives and the legacy files become regeneration outputs that never have the chance to drift.

---

### P3 — Tier-3 (Inner Circle) texture deficit, prose-feedstock-critical

Inner Circle NPCs (~14 NPCs across Crown / Hafenmark / Varfell + Cardinal Officers) carry only:
- Role
- Name
- Conviction (single tag)
- MS (single tag)
- Certainty (numeric)
- One-line disposition note

The articulation layer fires Tier 2 cut scenes on triggers including `state.scar_acquired for any tracked NPC` and `meta.knot_formed`. Inner Circle NPCs are eligible. When the prose-writer is invoked to render such a cut scene, it has one anchored dimension (conviction) to work with. Below the prose-writer's stated minimum.

**Fix scope**: extend texture floor to all named NPCs. Minimum additions per Inner Circle NPC: 1 belief (first-person voice anchor), 1 explicit goal, 1 inspiration. ~14 NPCs × 3 fields = ~42 author-decisions. Modest scope.

---

### P4 — No NPC `inspiration` field anywhere

The prose-writer skill explicitly lists "inspiration" as one of five anchored dimensions a load-bearing NPC needs. Yet:

- `articulation_layer §2.4` defines Inspirations as "**player-authored** aspirational arcs" — protagonist-only.
- `character_histories_v30` Stage 4 produces the **player's** starting Belief — Belief, not Inspiration; player, not NPC.
- `npc_character_analyses_v30` contains historical parallels (Sorge, Luxemburg, Henry VIII, Isabella I, Cesare Borgia) which **function as** author-side inspirations but are not labeled as such, are scattered prose only, and exist only for ~13 NPCs.

For 30+ named NPCs the prose-writer cannot pull "inspiration" because the field doesn't exist. For ~13 it can be inferred from prose. For zero NPCs is it queryable as data.

**Fix scope**: add `inspiration` (or `aspirational_arc`) as a structured field per NPC. Distinguish from PC's player-authored Inspirations (those are player-side — what the player wants their character to become). NPC inspiration is author-given — what the character wants to become / what the character treats as a model. Two facets per NPC: **historical_parallel** (e.g., "Cesare Borgia — instrumental Authority for self-aggrandizement") and **in-character aspiration** (e.g., "to be the ruler the deed-monarchy actually demands"). Both feed prose-writer.

---

### P5 — Empty-body sections across the texture stack

A non-trivial fraction of the texture infrastructure has headers without bodies:

- `character_analyses_v30` PART TWO: §5 Vaynard (14 tokens), §8 Cardinal Klapp (14), §9 Cardinal Olafsson (16), §10 Cardinal Jarnstal (43), §11 Ehrenwall (15) — title-only or one-line.
- `npc_behavior_v30 §5.2`: Vaynard Arc A and Arc B — empty bodies.
- `npc_foils_v30`: ~40% of pairings, ~60% of perspective views, all 4 triangular foils — empty body text.
- `npc_character_analyses Part One`: §10 Dalla Virke (12 tokens), §13 Prudence Cardinal (18 tokens) — empty-body or name-pending.
- `npc_behavior_v30 §1.2`, §3.3, §3.4 — redirect-only stubs to a stale document.

The headers imply texture exists; the bodies say it doesn't. Either condition is wrong: fill or strike.

---

### P6 — Ethical Framework labels are zombie data

Per `conviction_taxonomy_v30 §6` and `references/alias_registry.yaml`, these labels are SUPERSEDED:
- "Virtue Ethics" (used for Crown / Almud in npc_behavior §2.1)
- "Divine Command" (Church / Himlensendt §2.2)
- "Categorical Imperative" (Hafenmark / Baralta §2.3)
- "Consequentialist Pragmatism" (Varfell / Vaynard §2.4)
- "Rawlsian Social Contract" (Restoration / Vossen §2.6)
- "Moral Relativism" (Guilds — stance_triangles Framework Drift)
- "Martial Honour" (Löwenritter / Ehrenwall §2.5)
- "Epistemic Reason" / "Military Honor" — also retired

These remain embedded as the "Ethical Framework" field in every Tier 1 NPC stance triangle. They drive Ob modifiers (-1 / +1 / +2) which the engine consumes. **They are simultaneously canonically retired AND mechanically active.** The prose-writer cannot legitimately render "Almud's Virtue Ethics" because that is not a canonically-extant frame.

**Fix scope**: either redefine the labels as conviction-vector projections with new mechanical mapping, or strike from per-NPC sheets entirely and re-derive Ob modifiers from the conviction vector. The migration roster gives the conviction values needed for the second path.

---

### P7 — Internal articulation-layer contradiction on NPC Beliefs

`articulation_layer §2.4` defines Beliefs as "player-authored truth-statements" — protagonist-only.
`articulation_layer §3.1 trigger #10`: fires on `state.belief_revised` **for any tracked NPC** (Bonded ≥ 5 OR named-roster member).
`npc_behavior_v30 §2` has explicit Beliefs (first-person quoted) on most named NPCs.
`npc_behavior_v30 §3.2` defines NPC Belief Revision conditions.

Beliefs apparently both exist for NPCs (per behavior file) and are protagonist-only (per articulation §2.4). The trigger #10 spec implicitly resolves it (NPCs have beliefs that get revised — fire trigger), but the architectural description still contradicts. Worth a one-line clarification: NPCs have author-defined Beliefs that revise per `npc_behavior §3.2`; PCs have player-authored Beliefs per Stage 4 lifepath.

---

### P8 — Spirit is missing from NPC sheets

Prose-writer SKILL §Coherence-Indexed Weighting Principle treats Spirit as the third independent axis: "The Spirit axis becomes audible at Coherence 4 and below, where the Beckett texture (high Spirit) versus the Lispector texture (low Spirit) is the sharpest distinction the prose can make about what the PC still has."

The skill applies to NPCs too (per Self-Check item: "Do load-bearing NPCs have at least one anchored dimension?"). When focalizing through an NPC at degraded coherence, the prose-writer needs that NPC's Spirit value. NPC files supply TS reliably, Coherence inconsistently, **Spirit almost never**. Per-NPC Spirit values should exist as canonical data.

---

## 5. Verified cross-file inconsistencies (max-effort verification loop)

| # | Claim | Source A | Source B | Verified |
|---|---|---|---|:-:|
| V1 | Maret Uln has incompatible convictions across files | `npc_behavior_v30 §2.10`: Equity (primary), Reason (secondary) | `migration_roster_v30 §2.2`: Honor 0.30 + Authority 0.30 + Identity 0.20, lowenritter_military template | ✓ |
| V2 | Yrsa Vossen has incompatible convictions across files | `npc_behavior_v30 §2.6`: Equity (primary), Continuity (secondary) | `migration_roster_v30 §2.2`: Honor 0.35 + Warden 0.25 + Community 0.20, solmund_alpine template | ✓ |
| V3 | Baralta has incompatible convictions AND wrong cultural template | `npc_behavior_v30 §2.3`: Precedent (primary), Faith (secondary), **Hafenmark / Categorical Imperative** | `migration_roster_v30 §2.3 (under "Ecclesiastical Faction")`: Faith 0.50 + Virtue 0.20 + Warden 0.10, **ecclesiastical** template | ✓ — Duchess Inge Baralta (Hafenmark sovereign claimant) misfiled under Ecclesiastical with wrong cultural template |
| V4 | Three Conviction taxonomy versions canonical at once | `npc_stance_triangles.md` (7) | `conviction_track_v1.md` §1 (9) AND `conviction_taxonomy_v30.md §2` (13) | ✓ |
| V5 | Vaynard arc map has empty Arc A and Arc B | `npc_behavior_v30 §5.2 Magnus Vaynard — Arc Map`: "**Arc A: The Scholar**" then blank, "**Arc B: The Awakened**" then blank, "**Arc C: Consumed**" then content | — | ✓ |
| V6 | Inner Circle NPCs have no Beliefs or Resonant Style | `npc_behavior_v30 §2.15-2.17`: tables only — Role, Name, Conviction, MS, Certainty, brief note | — | ✓ |
| V7 | Ethical Framework labels are SUPERSEDED but still embedded | `conviction_taxonomy_v30 §6 + alias_registry.yaml`: Virtue Ethics, Categorical Imperative, Divine Command, Epistemic Reason, Rawlsian, Military Honor superseded | `npc_behavior_v30 §2.1` Almud: "Ethical Framework | Virtue Ethics (Crown)"; §2.5 Ehrenwall: "Martial Honour (Löwenritter)" | ✓ |
| V8 | Articulation layer self-contradicts on NPC Beliefs | §2.4: "Beliefs (player-authored truth-statements): ~3-5 per protagonist" | §3.1 trigger #10: "On any state.belief_revised Key for an NPC in the tracked roster" | ✓ |

---

## 6. Recommendations (ordered by leverage)

1. **Promote a single canonical per-NPC sheet schema.** YAML or markdown with: identity (name, role, faction, archetype/title), conviction vector (13-conv weights), self-other orientation, cultural label, beliefs (1–3 first-person voice anchors), goals (1–2 explicit), inspiration (historical parallel + in-character aspiration), arc map (A/B/C minimum), physical signature, speech register notes, key relationships. **Existing files (roster, analyses, foils, behavior triangles) become generated views or get merged.** Dissolves P1 and P2 simultaneously: the per-NPC sheet is the place 13-conv lives, and the legacy files become regeneration outputs that never have the opportunity to drift.

2. **Migrate stance triangles + conviction_track_v1 + npc_behavior §2 to 13-Conviction.** Migration roster (PP-685) already provides the per-NPC mapping data. Downstream files just need to consume it. Strike the 7- and 9-Conviction documents (or convert them to clean redirects). Resolves P1 directly.

3. **Extend texture floor to all named NPCs.** Inner Circles + Cardinal Officers + Varfell Jarl Council (~14 NPCs) get at minimum: 1 belief (first-person), 1 explicit goal, 1 inspiration. Resolves P3.

4. **Add `inspiration` as a structured per-NPC field.** Two facets: `historical_parallel` (Sorge, Luxemburg, Henry VIII, Cesare Borgia, etc. — author-side analytic anchor) + `in_character_aspiration` (what the NPC wants to become, in-fiction). Distinct from PC Inspirations (player-authored, protagonist-only). Resolves P4 and gives the prose-writer the missing anchored dimension.

5. **Fill or strike empty-body entries.** Inventory: ~5 character_analyses entries, ~10 foil pairings/perspectives/triangles, Vaynard Arc A and B, ~3 redirect-stub sections in npc_behavior. Either populate with ≥1 paragraph or remove the headers. Resolves P5.

6. **Decide on Ethical Framework labels.** Either redefine them as 13-Conviction projections with explicit conviction-pattern→label mapping (recommended: cleaner inheritance) or strike entirely and derive Ob modifiers from conviction vectors per Axis Matrix. Resolves P6.

7. **Reconcile articulation_layer §2.4 with §3.1 trigger #10.** One sentence: NPCs have author-defined Beliefs (per `npc_behavior §3.1`) that revise per `§3.2`; protagonist Beliefs are player-authored per character_histories Stage 4. Resolves P7.

8. **Add Spirit value to per-NPC sheets.** Default 4 (mid-range neutral) unless authored otherwise. The high-Spirit/low-Spirit distinction is what the prose-writer renders as Beckett vs Lispector at low coherence. Without it, the prose-writer cannot calibrate Spirit-axis output for NPC focalization. Resolves P8.

9. **Decide: NPC lifepath, or NPC author-defined?** PCs generate via 4-stage lifepath. NPCs are author-defined. The two systems do not bridge. Either build an NPC lifepath (using Origin/Formation/Vocation/Catalyst as a generation tool with named-NPC overrides) OR explicitly mark named NPCs as author-defined and dispense with the implicit assumption that they should fit the same generative system. Lower priority; affects N more than R.

---

## 7. What works, anchored

The substrate is genuinely strong. To narrow the change-surface (per `<anchor_in_what_works>`):

- **Conviction Taxonomy v30 + Axis Matrix is exemplary substrate design.** The per-row Renaissance-grounded calibration is the model for how a substrate doc earns its claims. The Self-Other axis as orthogonal scalar is load-bearing in a way 4-axis projection alone wouldn't be (Macbeth-arc emergence). Acknowledged 4-axis collapses are intellectually honest.
- **Articulation layer's Tier 1/2/3 architecture is load-bearing.** `accumulated_narrative_weight` prevents narrative starvation; trigger ruleset is specific; significance scoring is principled. Strong R.
- **`npc_roster_v30` Behavioral AI fields are excellent prose-feedstock.** Each NPC has a flaw-with-mechanical-consequence (Strand's flattery vulnerability; Laskaris's protective→catastrophic-reversal flip; Feldhaus's profit-maximisation that hollows political relevance). These produce strategic counters AND emergent surprises.
- **`npc_character_analyses` titles are the model for character framing.** "The Last Maintenance Technician" / "The Inquisitor's Uncertainty Principle" / "The Ledger That Never Forgives" / "The Right Answer to the Wrong Question" — each title is a thesis. Where the bodies are populated, the prose-feedstock is excellent.
- **Edeyja's individual NPC doc is the gold standard.** Role, background (with sensory detail — visible Thread injury), stats, Conviction, lineage, military reality, faction relationships, player access table, GM presence notes, canon compliance. Replicating this format for the other ~30 named NPCs would dissolve most of the prose-feedstock gaps in §3.
- **Beliefs as first-person quotes** (in `npc_behavior §2`) are excellent voice anchors where present. The format works; coverage just needs to be uniform.

**The fixes are integration debt, not design debt.** The architecture is sound; the data has not finished migrating into it.

---

## 8. Open items / `[GAP]`s

- `[GAP: NPC Spirit values — reason: per-NPC Spirit is rarely authored; prose-writer needs it for low-coherence focalization. Default 4 or audit to author per NPC?]`
- `[GAP: NPC physical signature beyond Edeyja — reason: prose-writer's "physical world is present" check requires anchoring detail; almost no NPC has one.]`
- `[GAP: PC↔NPC generative bridge — reason: lifepath generates PCs; NPCs are author-defined; no shared substrate. Acceptable design choice or unfinished work?]`
- `[GAP: Cultural template for Niflhel-related NPCs after PP-650 strike — reason: migration_roster §2.7 uses hafenmark_procedural as placeholder; specific replacement deferred to Stage 10.]`
- `[ASSUMPTION: prose-writer is the primary downstream consumer of NPC texture — basis: explicit list of anchored dimensions in `skills/prose-writer/SKILL.md` line 153. If other consumers (engine logic, BG layer) have different needs, audit findings would shift.]`
- `[ASSUMPTION: Tier-1 vs Tier-2 vs Tier-3 NPC tracking from `npc_behavior §11` reflects current intent — basis: PP-661 spec; verify against current player-facing roster decisions.]`
- `[CONFIDENCE: high — multi-file verification confirms each cross-file inconsistency in §5.]`
