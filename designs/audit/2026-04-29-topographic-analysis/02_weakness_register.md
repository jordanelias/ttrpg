<!-- [PROVISIONAL: 2026-04-29 — topographic analysis weakness register] -->
<!-- STATUS: PROVISIONAL — first-pass corpus-derived findings; methodology limits called out in §0 -->
<!-- AUTHORITY: PP-676, ED-760 (workplan); this register is the Stage 4 output -->

# Topographic Analysis — Weakness Register

**Date:** 2026-04-29
**Method:** TF-IDF cosine + doc-level Jaccard over 53 canonical/provisional design docs (~344k tokens of full text). 126 curated tokens, 4,225 paragraphs (3,068 canonical / 934 provisional / 223 retired).
**Companion:** v1 connections artifact at `/mnt/user-data/outputs/valoria_connections.jsx` (31 nodes, 53 hand-curated edges).

---

## §0 Methodology — what this measurement can and cannot see

Two complementary corpus measurements were used:

**TF-IDF cosine similarity** over paragraph-level vectors. Detects **semantic co-mention** — tokens that appear together in the same paragraphs. Strong at finding semantic clusters (NPC archetype clusters, faction families, conviction co-occurrence). Weak at detecting causal/functional links that span doc boundaries (Threadwork affects MS, but the cause and the effect are described in different docs in different paragraphs).

**Doc-level Jaccard** over per-token document sets. Detects **shared territory** — which pairs of tokens recur across the same set of docs. Broader lens; catches cross-doc relationships that paragraph-cosine misses.

**Hand-curated edges (v1 artifact)** encode designer-asserted causal/functional logic. The corpus may or may not substantiate them through co-mention.

The diagnostic value is in the **disagreement between the three lenses**, not in any single one.

A v1 edge that scores **cosine < 0.05 AND jaccard < 0.10** is a *genuinely-thin* edge: hand-curation asserts a connection the corpus does not weave through. This is a real propagation/coverage finding.

A v1 edge that scores **cosine low BUT jaccard ≥ 0.20** is *methodology-limited*: the connection is real and the corpus shares territory, but the cause and effect are described in separate paragraphs that don't textually co-occur. Not a finding; a measurement limit.

---

## §1 Genuinely-thin hand-curated edges (HIGH-VALUE FINDINGS)

These v1 edges are asserted in the hand-curated graph but the corpus barely substantiates them. Each represents a **propagation gap**: the connection lives in one place (canonical_sources, complete_systems_reference) but isn't woven through the dependent specs.

| v1 edge | cosine | jaccard | Reading |
|---|---|---|---|
| Self-Rendering ↔ NPC Behavior | 0.000 | 0.059 | propagation thin |
| Conflict Architecture ↔ Faction Layer | 0.000 | 0.000 | propagation thin |
| Throughlines ↔ Campaign Architecture | 0.000 | 0.000 | propagation thin |
| Throughlines ↔ Conflict Architecture | 0.000 | 0.000 | propagation thin |
| Throughlines ↔ Armature System | 0.000 | 0.000 | propagation thin |
| Threadwork ↔ MS Trajectory | 0.000 | 0.080 | propagation thin |
| Fractional Province ↔ Faction Layer | 0.000 | 0.000 | propagation thin |
| Peninsular Strain ↔ MS Trajectory | 0.000 | 0.000 | propagation thin |
| Royal Assassination ↔ NPC Behavior | 0.000 | 0.091 | propagation thin |
| Armature System ↔ Faction Layer | 0.000 | 0.000 | propagation thin |

**Interpretation per edge:**

- **Threadwork ↔ MS Trajectory** (jac 0.080) — Threadwork operations *cause* MS shifts per canon, but `threadwork_v30.md` and `ms_trajectory_v1.md` barely cross-reference. The connection is asserted in `canonical_sources.yaml` not woven through either spec. **Open propagation issue.**
- **Royal Assassination ↔ NPC Behavior** (jac 0.091) — the assassination fuse is supposed to fork NPC arcs; `royal_assassination.md` and `npc_behavior_v30.md` don't co-locate the fork-trigger machinery. Recent canonical (PP-666 era), under-propagated.
- **Fractional Province ↔ Faction Layer** (jac 0.000) — a provisional system claiming to affect canonical Faction Layer, but the canonical doc doesn't yet reference it. Matches its **provisional + ED-711 open** status; the propagation work is exactly what ED-711 is waiting on.
- **Self-Rendering ↔ NPC Behavior** (jac 0.059) — Coherence's effect on NPCs is asserted philosophically but rarely operationalized in NPC behavior specs.
- **Throughlines → {Campaign Arch, Conflict Arch, Armature System}** (jac 0.000 each) — the *vetting authority* relationship is metadata not content. Throughlines doesn't substantively appear in those design docs because vetting happens at register-entry time, not in the design itself. **Probably correct as-is** — different category of link.
- **Peninsular Strain ↔ MS Trajectory** (jac 0.000) — this is surprising; both are peninsula-clock docs. Inspecting: `peninsular_strain_v30` and `ms_trajectory_v1` likely use different terminology for overlapping content. **Possible terminology drift candidate.**

---

## §2 Implied-but-missing edges (high-jaccard pairs not in hand-curation)

Pairs with strong doc-level co-occurrence (jaccard ≥ 0.30) that v1 did not connect. Each is a candidate edge for v2 audit.

| jaccard | Pair | Likely interpretation |
|---|---|---|
| 0.407 | **Knot ↔ Social Contest** | Knot Bonds affect Contest pool sizes; cross-system reference missing |
| 0.406 | **Knot ↔ Leap** | Knot Anchoring affects Coherence recovery — direct causal link |
| 0.400 | **Knot ↔ Threadwork** | Knots vs Thread ops, contrast pair (PP-632) — explicit edge implied |
| 0.394 | **Combat ↔ Knot** | Bonds affect combat behavior via Disposition; thinly explicit |
| 0.414 | **CI Clock ↔ Social Contest** | Heresy Investigation uses Contest mechanics → CI shifts |
| 0.405 | **CI Clock ↔ Mass Combat** | Mass Battle affects CI through Stability Trigger 5; weave thin |
| 0.400 | **CI Clock ↔ Combat** | Spillover from CI ↔ Mass Combat |
| 0.400 | **CI Clock ↔ Domain Echo** | Contest Domain Echo can shift CI |
| 0.400 | **CI Clock ↔ Victory** | Universal Victory requires Political Stability bound; CI is in that lattice |
| 0.400 | **Faction Succession ↔ Royal Assassination** | Both succession-territory mechanics; should cross-reference |
| 0.500 | **Combat ↔ Fieldwork** | Both personal-scale; contained in same docs |
| 0.423 | **Combat ↔ Domain Echo** | Personal combat → faction shift via Domain Echo |
| 0.353 | **Domain Echo ↔ NPC Behavior** | NPC priority stacks reference Domain Echo |
| 0.345 | **Domain Echo ↔ Knot** | Bonds affect Domain Echo magnitude |
| 0.389 | **Mass Combat ↔ Threadwork** | Thread phase in mass battle (7-phase structure) |
| 0.333 | **Mass Combat ↔ Victory** | Battle outcomes feed victory clocks |

**Strongest individual finding:** the **Knot system** is connected to many things (Social Contest, Leap, Threadwork, Combat, Domain Echo) at high jaccard but only loosely in v1. Knots are everywhere in the corpus and central to Bonds-driven mechanics, but the v1 graph drew Knots as a peripheral personal-scale node. **The Knot system should be elevated to a hub in v2.**

The **CI Clock** has dense co-occurrence with multiple other systems (Social Contest, Mass Combat, Combat, Domain Echo, Victory) — also under-edged in v1. CI is more central than v1 portrayed.

---

## §3 Sparse / under-developed concepts (low corpus coverage)

Tokens appearing in fewer than 10 paragraphs across the entire corpus. These are either intentionally narrow concepts or under-developed canon.

| Token | Paragraphs | Primary doc | Reading |
|---|---|---|---|
| MS Trajectory | 2 | ms_trajectory_v1.md | Lives only in own doc — **isolated**, no propagation |
| Royal Assassination | 6 | npc_behavior_v30.md | Recent canonical — under-propagated |
| Faction Succession | 6 | various | Provisional, ED-open |
| Pressure Point | 7 | complete_systems_reference.md | Foundational concept appears mostly in summary doc, thinly in NPC specs |
| Settlement Adjacency | 9 | settlement_adjacency_v30.md | Provisional, ED-710 open — matches expected |
| Fractional Province | 8 | own doc | Provisional, ED-711 open — matches |
| Tensions Deck | 8 | conflict_architecture_proposal.md | Lives almost entirely inside conflict arch doc — under-propagated |
| N Necessity | 6 | throughlines_meta.md | Framework concept, lives only in throughlines docs |
| Sufficient Scope | 9 | scale_transitions_v30.md | Critical scale-bridge concept lives in one doc |
| Socializing | 6 | faction_layer_v30.md | PP-632 introduced major socializing changes — primary doc placement is wrong |
| Stealth | 2 | complete_systems_reference.md | Surprisingly absent from canonical specs |
| Zoom-Out | 8 | scale_transitions_v30.md | One-sided of the Zoom-In/Zoom-Out pair |

**Findings of concern:**
- **Stealth at 2 paragraphs** is a real surprise. If Stealth is intended to be a Personal-scale system equal to Combat/Threadwork/Fieldwork, the canonical specs barely cover it. Either it's mostly subsumed under Fieldwork (and shouldn't be a separate token) or it's genuinely under-specified.
- **Socializing's primary doc is `faction_layer_v30.md`** — this is wrong. PP-632 introduced Sincerity Gate and Disposition mechanics in the personal-scale Socializing system; it should have a primary doc in `designs/scene/` or `designs/npcs/`. Doc placement issue.
- **Tensions Deck lives inside `conflict_architecture_proposal.md`** with no separate top-level spec doc — but `params/bg/tensions_deck.md` exists. The corpus distribution suggests the params file is barely referenced from the design corpus. Propagation gap.
- **MS Trajectory is conceptually isolated** despite being central — this isolation is itself a finding.

---

## §4 Hub structure — what's actually load-bearing

Top hubs by edge degree (sim ≥ 0.15) are dominated by **Convictions and factions**, not by the systems v1 portrayed as hubs:

| Token | Edge degree | Doc count | Category |
|---|---|---|---|
| Autonomy | 10 | 56 | Autonomy |
| Order | 9 | 134 | Order |
| Faith | 7 | 52 | Faith |
| Reason | 7 | 44 | Reason |
| Equity | 7 | 26 | Equity |
| Precedent | 7 | 39 | Precedent |
| Continuity | 7 | 40 | Continuity |
| Crown | 7 | 262 | Crown |
| Varfell | 7 | 188 | Varfell |
| Torben | 6 | 39 | Torben |

**Reading:** the seven Convictions form a ring of high-degree hubs because they appear in every NPC profile, every Decision Procedure reference, every Pressure Point discussion. Crown/Church/Hafenmark/Varfell/Löwenritter/RM appear because every faction-relevant spec references multiple factions.

The notable absence: **most v1 hub-systems (faction_layer, scale_transitions, conflict_architecture, threadwork) do not appear as hubs in this measurement.** This is partly the methodology limit (their cross-doc relationships don't surface as paragraph-cosine), but partly real: those specs are *contained* — they describe themselves coherently and don't constantly cross-reference other systems.

The **Convictions cluster** is meaningful: Reason ↔ Equity (0.664), Equity ↔ Continuity (0.658), Reason ↔ Continuity (0.632). Either these Convictions are textually intertwined for good reason (they share NPC archetype space — RM, Lenneth, etc.) OR they're under-differentiated. **Worth investigating** whether the design distinguishes them sufficiently when they collide in NPC profiles.

---

## §5 Cross-cutting tokens with diffuse distribution

The political-dynamics armature system tokens appear broadly but never densely with any specific partner:

| Token | Paragraphs | Edge degree (sim≥0.15) |
|---|---|---|
| Domain Action | 162 | 0 |
| Concern | 118 | 0 |
| Standing | 90 | 0 |
| Knowledge | 85 | 0 |
| Project (NPC) | 74 | 0 |
| Armature System | 70 | 0 |
| Inner Circle | 58 | 0 |
| Cascade Attenuation | 56 | 0 |
| Institutional Stability | 14 | 0 |
| Event Impact Matrix | 11 | 0 |

**Reading:** these tokens are **diffusely defined** — referenced in many places but never in tight conjunction with any specific other system. This is consistent with the political dynamics work's PROVISIONAL status (12_development_specification.md is the source-of-truth, but its concepts haven't been woven into specific spec docs). 

After 12_development_specification.md edits land (PP-PROP-ARMATURE-* series), this analysis should be re-run to see whether these tokens become more densely connected.

---

## §6 The Niflhel anomaly

**Conflict Architecture ↔ Niflhel: cosine 0.608.**

This is the highest non-noise pairing and reflects something specific: every paragraph that mentions Niflhel is in `conflict_architecture_proposal.md` (the doc that *dissolved* Niflhel). Niflhel is now defined entirely by its dissolution, not by its prior presence as a faction. The corpus correctly captures the new state but the high cosine reflects how concentrated the historical content has become.

**Not a problem.** The dissolution propagation appears to have worked — Niflhel doesn't surface in faction-layer or victory or peninsular_strain anymore. The 0.608 is a fingerprint of clean removal, not of a propagation gap.

---

## §7 Cross-cutting design observations

Three structural observations the corpus surfaces:

**1. The political dynamics layer is not yet woven in.** Armature System, Domain Action, Concern, Memory, Project, Knowledge, Inner Circle — all high-frequency, all degree-0. The 12_development_specification.md is comprehensive in itself but disconnected from the rest of the canonical corpus. This is a known state (PROVISIONAL, 68 stress test issues open, ED-750..755 batch fixes pending) and matches the documented status. The topographic analysis confirms it numerically.

**2. The Knot system is more central than v1 suggested.** Knots co-occur strongly with Combat, Social Contest, Threadwork, Leap, Domain Echo. The hand-curated graph drew Knots as a peripheral Personal-scale node; the corpus treats them as a connective hub spanning Personal/Scene scales and reaching into Foundation (Leap) and Architecture (Domain Echo) territory. **v2 should re-elevate Knots.**

**3. Sufficient Scope is structurally undersized.** This concept is the load-bearing trigger for Domain Echo, scale transitions, and zoom-in events — but it appears in only 9 paragraphs, all in `scale_transitions_v30.md`. Critical mechanic, single-doc presence, no cross-spec propagation. Worth its own ED entry.

---

## §8 Methodology recommendations for next iteration

- **Cross-doc reference graph** (Jaccard) was more revealing than paragraph-cosine for this corpus. Future iterations should run both as standard.
- **Tier the corpus by status** — the current weighting (canonical 1.0, provisional 0.7, retired 0.2) is reasonable but may be smoothing legitimate signals. A side-by-side analysis of canonical-only vs canonical+provisional would expose whether provisional content is creating phantom edges.
- **Section-level rather than paragraph-level granularity** would catch causal links that paragraph segmentation breaks apart.
- **Surface-form coverage** is the largest source of noise. Patterns for "Stealth" missed something. Patterns for the contest styles need redesign (the 4 styles aren't ever called by their names in prose). A second pass with broader regex + sample validation per token would tighten findings.

---

## §9 Concrete weakness register entries

Findings worth tracking as ED entries pending Jordan signoff:

| ID | Finding | Source diagnostic |
|---|---|---|
| TOPO-01 | Stealth canonical spec coverage gap (2 paragraphs in entire corpus) | §3 sparse |
| TOPO-02 | Socializing primary doc placement wrong (lives in faction_layer, should be in scene/npcs) | §3 sparse + structural |
| TOPO-03 | MS Trajectory conceptually isolated — no cross-spec propagation | §3 sparse + §1 thin edge |
| TOPO-04 | Sufficient Scope load-bearing but single-doc — propagation gap | §3 sparse + §7 |
| TOPO-05 | Tensions Deck content lives in conflict_arch, not in own params doc — propagation gap | §3 + §1 |
| TOPO-06 | Royal Assassination → NPC Behavior fork machinery thinly woven | §1 |
| TOPO-07 | Threadwork ↔ MS Trajectory functional link not textually present | §1 |
| TOPO-08 | Knot system under-edged in v1 connections artifact (high jaccard with Social Contest, Leap, Combat, Domain Echo) | §2 |
| TOPO-09 | CI Clock under-edged — corpus shows broader connectivity than v1 captured | §2 |
| TOPO-10 | Faction Succession ↔ Royal Assassination overlap — both succession-territory, should cross-reference | §2 |
| TOPO-11 | Convictions Reason/Equity/Continuity high cosine (≥0.63) — investigate whether under-differentiated in NPC archetype space | §4 |
| TOPO-12 | Political-dynamics layer (Armature, Domain Action, Concern, etc.) entirely degree-0 — confirms PROVISIONAL status, not woven into canonical corpus | §5 |

---

## §10 What the analysis cannot tell you

Per workplan §5, restated: this analysis does not surface UX failures (Scene Slate pressure type), computational cost, pacing/tedium, mechanical correctness, authoring debt, or intentional asymmetries. The findings here are **structural** and **textual**. Each warrants designer judgment before becoming an action.

The gap-between-views method is most useful as a **search-light** for v2 connections audit — it points where to look, not what to conclude.
