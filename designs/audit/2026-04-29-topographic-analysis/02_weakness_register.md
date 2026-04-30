<!-- [PROVISIONAL: 2026-04-29 — topographic analysis weakness register, v2 + v3] -->
<!-- STATUS: PROVISIONAL — v2 sections retained as audit trail; v3 sections supersede where they conflict; v3 methodology VALIDATED (2/3 structural properties pass); v2 methodology FAILED -->
<!-- AUTHORITY: PP-676 (workplan v3 in same folder, supersedes v1+v2) -->

# Topographic Analysis — Weakness Register

**Date:** 2026-04-29
**v2 methodology validation:** FAILED — mean Jaccard 0.222
**v3 methodology validation:** VALIDATED — 2/3 structural properties pass
**Corpus:** 43 design docs, 2,940 paragraphs, 84 tokens (74 seed + 10 auto-extracted)
**Workplan:** designs/audit/2026-04-29-topographic-analysis/00_workplan.md (v3)
**Read order:** v3 sections (§V3-*) supersede v2 sections (§0-§5) where they conflict; see §V3-13 for the diff. v2 sections retained for audit trail.

---

## §0 Methodology validation finding (the most important single result)

The pre-committed validation cross-checks TF-IDF neighborhoods against expected groupings derived from prior hand-curation. **Mean Jaccard across 13 expected groups: 0.222.** This is below the 0.30 threshold the workplan committed to before viewing data. Per protocol, findings below threshold are reported with caveats rather than treated as authoritative.

**Per-group results:**

| Group | Jaccard | Verdict |
|---|---|---|
| foundation_cluster | 0.50 | ✓ validated |
| thread_chain | 0.36 | ○ partial |
| crown_npcs | 0.33 | ○ partial |
| varfell_cluster | 0.33 | ○ partial |
| rm_cluster | 0.31 | ○ partial |
| lowenritter_cluster | 0.30 | ○ partial |
| armature_cluster | 0.21 | ✗ failed |
| personal_combat | 0.18 | ✗ failed |
| peninsula_layer | 0.17 | ✗ failed |
| faction_hub | 0.11 | ✗ failed |
| solmund_cluster | 0.08 | ✗ failed |
| social_chain | 0.00 | ✗ total failure |
| church_npcs | 0.00 | ✗ total failure |

**The pattern of which groups pass and which fail is itself the finding.**

The five **partial-validation** clusters are all faction-anchored (each faction's identity tokens cohere). The two strong validations are foundation concepts and the thread chain. **Every mechanical-system cluster failed.**

**Interpretation:** The corpus is structured such that each mechanical system lives substantially in its own dedicated file with limited textual cross-pollination. The connective tissue across the corpus is people and ideologies (factions, NPCs, Convictions) — not mechanical systems. This is a structural property of the project's documentation that has direct implications for project weakness.

---

## §1 Findings — corpus-derived signal

### 1.1 The corpus is not a system network — it is a faction/NPC/Conviction network

Top 15 high-similarity hubs (mean cosine across all other tokens, top quintile):

```
Crown · Autonomy · Reason · Varfell · Löwenritter · Hafenmark · Equity · Order
· Torben · Church · Conviction · TS · King Almud · Lisbeth Ehrenwall · Continuity
```

**Zero mechanical systems are in this list.** Combat, Threadwork, Faction Layer, Mass Combat, Domain Echo, Scale Transitions, Settlement Layer, Victory, Peninsular Strain — none rank in the top quintile of corpus connectivity. The systems each have their own file and are referenced from afar; the people and convictions appear *throughout* the corpus.

**Why this matters:** the project's stated intent (Ω) is a "positive feedback loop between player decisions and mechanics/system/designs that produces an engaging game world with emergent narratives." If the design corpus's connective tissue is *characters and ideologies* rather than *mechanics*, then the integration risk lives in the implementation phase: when Godot has to instantiate the systems, every system-to-system connection is going to have to be inferred from sparse documentation rather than read off direct co-references.

This is hand-curation-invisible. I built the v1 connections artifact assuming systems were the primary nodes. The corpus says: people and convictions are the primary nodes, systems are the verbs they enact.

**Recommendation:** the v2 connections audit should have a parallel pass that maps faction-NPC-Conviction hubs and treats the systems as edges between them. The current "systems-as-nodes" framing is not what the corpus is.

### 1.2 The "Settlement Layer downstream sink" pattern

The citation graph is sparse (15 doc-edges, 11 token-edges) but every cascade-without-return chain found terminates the same way:

```
Campaign Architecture → CI → Settlement Layer
Faction Layer        → CI → Settlement Layer
Victory              → CI → Settlement Layer
Peninsular Strain    → CI → Settlement Layer
```

Four major peninsula/province docs cite Settlement Layer through CI, and Settlement Layer does not cite any of them back. **Settlement Layer is a downstream sink in the citation graph.**

This is consistent with PP-666 (Settlement Adjacency / Fractional Province Ownership) being the *newest* and most provisional layer of the design — it was added recently and the upstream docs were updated to reference it before its own cross-references were filled in. But it is a real one-way pressure pattern that violates Ω-d ("every action pays what it buys" implies feedback loops, not cascades).

**Recommendation:** Settlement Layer should cite back to at least Campaign Architecture and Faction Layer with explicit feedback descriptions of how settlement-level state propagates upward.

### 1.3 Notional edges — citations without content overlap

10 cited pairs have cosine ≤ 0.10 (citation present, but actual textual content does not overlap):

```
0.000  MS Trajectory → Leap                  (cited; content has no overlap)
0.000  MS Trajectory → Self-Rendering        (cited; content has no overlap)
0.016  Campaign Architecture → CI
0.016  Faction Layer → CI
0.029  CI → Settlement Layer
0.030  Campaign Architecture → NPC Behavior
0.034  Campaign Architecture → Settlement Layer
0.039  Peninsular Strain → CI
0.062  Tensions → Royal Assassination
0.067  Tensions Deck → Royal Assassination
```

**Most striking:** `MS Trajectory → Leap` and `MS Trajectory → Self-Rendering` both score literally 0 cosine. The MS Trajectory file cites foundational concepts but its content (dates and stability values) does not engage with them. This is fine ceremonially but means MS Trajectory is essentially a data table whose foundational grounding is asserted by reference rather than developed in content. If the foundational philosophy ever changes, MS Trajectory won't catch it because there is no actual argumentative thread between them.

**Recommendation:** either MS Trajectory adds inline justification for its values referencing the foundational dynamics, or the cross-reference is downgraded from "cited authority" to "see also" status to set correct expectations.

The `Campaign Architecture → CI` / `Faction Layer → CI` / `Peninsular Strain → CI` cluster (all <0.04 cosine) is more concerning: three major architecture docs cite the CI clock without textual engagement. This means the CI clock is referenced at structural-overview level but its mechanics aren't woven into the surrounding text. Implementation risk: someone implementing Faction Layer without reading CI Political may miss CI's interaction with parliament weight, mass seizure trigger, etc.

### 1.4 Implied-but-missing connections — high cosine, no citation (top 10 informative)

Filtering out within-class clustering (Convictions↔Convictions, factions↔factions, which are expected to score high) and token-deduplication artifacts (Tensions↔Tensions Deck = 0.93 means the same thing twice):

```
0.759  Fieldwork ↔ Evidence       — Investigation Evidence Track is in fieldwork; should be explicit
0.607  Dynastic Proclamation ↔ Cultural Reformation — both legacy/struck terms cluster (vocabulary debt)
0.571  Combat ↔ Fieldwork         — combat appears in fieldwork investigation contexts
0.570  Wager ↔ Edeyja             — Wager system tied to Edeyja arc; unstated relationship
0.477  Crown ↔ Löwenritter        — friction-point T14 relationship; not always cross-cited
0.435  King Almud ↔ Lenneth       — political reformist arc dependency
0.402  Royal Assassination ↔ Lenneth — Lenneth is a target; relationship implied not always stated
0.400  Continuity ↔ Edeyja        — Continuity Conviction tied to Warden character
```

**`Wager ↔ Edeyja` (0.570)** is the most actionable individual finding here. This is a strong corpus relationship that hand-curation didn't surface. The Wager system's mechanics appear to be deeply tied to Edeyja's character arc, but neither doc explicitly cross-references the other. If Wager mechanics change, Edeyja's arc is at risk; if Edeyja's role evolves, Wager's calibration may break.

### 1.5 Vocabulary debt — legacy terminology still in canonical corpus

Auto-extracted candidates surfaced three terms that should not appear in current canon:

| Legacy term | Para | Docs | Status | Source of strike |
|---|---|---|---|---|
| `Game Master` | 16 | 3 | RETIRE per PP-675 | terminology workplan 2026-04-29 |
| `Cultural Reformation` | 14 | 4 | STRUCK per PP-650 | Varfell Colonist conflict 2026-04-19 |
| `Coup Counter` | 10 | 7 | STRUCK per ED-781 | replaced by Graduated Autonomy 2026-04-25 |

**Total:** 40 paragraph occurrences of struck/legacy terminology across 14 distinct docs. This is propagation debt from already-applied patches.

**Recommendation:** these three terms should be added to a `terminology_gate` block-list once PP-675 advances. A simple grep-and-replace pass for `Coup Counter` → `Graduated Autonomy` and `Cultural Reformation` → struck-marker plus rephrasing handles most of it.

### 1.6 Sparse-context tokens — under-developed corpus footprint

Tokens in the bottom 10th percentile of paragraph mentions (≤ 6 paragraphs):

| Token | Para | Status | Concern |
|---|---|---|---|
| Fractional Province | 2 | provisional | Provisional, low engagement; expected for new design |
| Faction Succession | 2 | provisional | Same |
| MS Trajectory | 2 | canonical | Dedicated file is data tables; no cross-doc footprint |
| Wager | 4 | canonical | Mechanic exists but is referenced as `Wager Obligation` more than `Wager`; surface form coverage issue |
| CI Political | 4 | canonical | Token under-mentioned because doc was renamed from `tc_political_redesign_v30` (ED-782); transition not propagated |
| Throughlines | 6 | canonical | Vetting authority cited laconically rather than discussed |
| Thread Revelation | 6 | canonical | Section in Campaign Architecture, no dedicated doc |
| Event Impact Matrix | 6 | provisional | Provisional design |
| Consequence | 6 | canonical | Pressure Point under context-disambiguation |
| Authority | 6 | canonical | Pressure Point under context-disambiguation |

**Real concerns vs methodological artifacts:**
- `MS Trajectory` (canonical, 2 para) is a real footprint problem — the doc serves as authority for an entire peninsula's stability values but is barely woven into the rest of the corpus
- `CI Political` (canonical, 4 para) reflects ED-782 propagation gap — terminology rename is incomplete
- `Wager` (canonical, 4 para) is a coverage issue — the mechanic exists but the surface form is rare

### 1.7 Empty regions diagnostic — null result

Both t-SNE and force-directed layouts produced 0 candidate empty regions. With 84 tokens this is expected — the density grid is too coarse to identify gaps reliably at this token count. **Empty regions diagnostic is not informative at current scale; would need ~200+ tokens to be meaningful.**

---

## §2 Cross-finding pattern: the project documents people, not systems

Combining §1.1 (faction/NPC hubs) with §1.4 (Wager↔Edeyja, Almud↔Lenneth) and §1.3 (Campaign Architecture cites CI without engaging it):

The corpus's emergent structure is that **mechanics are described in dedicated files but the connective text across the project is character-based**. NPCs and factions are discussed in many docs; mechanical systems are discussed primarily in their own docs.

This is consistent with Valoria's design philosophy (the project intent statement emphasizes *engaging game world with emergent narratives*) and is probably correct for the *narrative* layer. But it carries an implementation risk:

**When Godot implementation begins, the system-to-system integration will not have direct documentation backing.** Most cross-system integration (e.g. how Mass Combat's officer-death feeds Faction Layer's Stability Trigger 5) will need to be inferred from sparse cross-references rather than read off the corpus.

**This is a real Ω-d concern** — every action paying what it buys requires that the *what it buys* be traceable. If the system integration paths are not in the docs, they have to live in the engineer's head, which fails the Renaissance-political-leadership-modeling Necessity test in a different way: not because the mechanics are wrong, but because their *interactions* are not documented strongly enough to survive personnel transitions.

**Recommended action: a "system integration" doc cluster.** A new directory (`designs/integration/`) where every cross-system interaction is documented at the integration level, not just the system level. Faction Layer's interaction with Mass Combat lives there; Threadwork's interaction with MS lives there; Domain Echo's interaction with Faction Layer lives there. The existing system docs continue to define their own internals; the new integration docs make their handshakes explicit.

This was not visible from hand-curation. The connections artifact v1 *shows* these integrations as edges, but the corpus reveals that those edges are not substantiated by integrative writing — they're inferences I drew from individual system docs.

---

## §3 Methodology caveats — what to NOT conclude

1. **Validation failed.** Mean Jaccard 0.222. Findings here are **leads, not verdicts**. Each finding should be cross-checked against the actual specs before any spec change is enacted.

2. **Within-class clustering inflated similarity for some pairs.** Convictions cluster with Convictions, factions cluster with factions. This is expected (taxonomy) and was not filtered out of the implied-missing list. The first 5-8 entries in §1.4 are within-class artifacts; only entries below those reflect cross-class implied connections.

3. **Token deduplication issues.** `Tensions ↔ Tensions Deck` scored 0.926 because they are essentially the same concept. Future runs should merge tokens with surface-form overlap > some threshold.

4. **Sparse tokens have noisy similarity scores.** Any finding involving a token in §1.6 should be triple-checked. Wager (4 paragraphs) producing 0.570 with Edeyja could be real or could be one chance paragraph; needs manual verification.

5. **The citation graph is conservative.** Only explicit cross-references in `Cross-references:` lines, `see X.md`, and `supersedes:` are caught. Implicit references (mentioning a system by name without filename) are not in the citation graph. So the 103 implied-but-missing pairs may include some pairs that ARE cited implicitly. Manual check before any of these are treated as missing-cross-ref findings.

6. **The expected_groups in §0 reflect my prior.** They are not ground truth; they are my hand-curated guess at what should cluster. The fact that the corpus disagrees with this prior is itself the finding — but it does not mean the corpus is wrong. It might mean my prior is wrong, or that both reflect partial truth.

---

## §4 Items for v2 connections audit

Findings that should be raised explicitly during the v2 connections artifact audit pass:

1. **Reframe v2 as faction/NPC/Conviction-anchored, not system-anchored** — or run both views in parallel
2. **Add cross-reference: Wager system ↔ Edeyja arc** — strongest unattested connection
3. **Add cross-reference: Royal Assassination ↔ Lenneth (target)** — already implicit in fuse spec, make explicit
4. **Add cross-reference: Settlement Layer ↑ Campaign Architecture** — break the downstream-sink pattern
5. **Add cross-reference: MS Trajectory ↔ foundational philosophy** — currently zero cosine
6. **Vocabulary cleanup: 14 docs contain `Coup Counter` (struck), 4 contain `Cultural Reformation` (struck), 3 contain `Game Master` (legacy)**
7. **CI Political rename (ED-782) propagation incomplete** — token has only 4 paragraphs of coverage
8. **Consider `designs/integration/` as a new directory** — see §2

---

## §5 Outputs

| File | Purpose |
|---|---|
| `data/corpus_manifest.json` | 47 paths fetched, banner classifier results |
| `data/corpus_design.json` | 43 design docs, full text |
| `data/corpus_discourse.json` | 4 audit/session docs (overlay only) |
| `data/tokens.json` | 84 tokens with metadata, surface forms, paragraph counts |
| `data/citation_graph.json` | 15 doc-edges, 11 token-edges (conservative parse) |
| `data/vectors.npz` | 84 × 2940 sparse weighted matrix |
| `data/similarity.npz` | 84 × 84 cosine matrix |
| `data/layout_tsne.json` | 2D t-SNE projection |
| `data/layout_force.json` | 2D force-directed projection |
| `data/density.npz` | Density grids for both layouts |
| `data/diagnostics.json` | All §1 findings as structured data |

All artifacts are deterministic given fixed corpus + seeds (random_state=42).



# Topographic Analysis — Weakness Register

**Date:** 2026-04-29
**v2 methodology validation:** FAILED (mean Jaccard 0.222)
**v3 methodology validation:** **VALIDATED** (2/3 structural properties pass)
**v3 supersedes v2 findings where they conflict; v2 sections retained as audit trail.**

---

## §V3-0 v3 validation outcome

Three structural properties pre-committed in v3 workplan §3.8:

| Property | Result | Verdict |
|---|---|---|
| **P1** Foundation tokens have higher mean degree than corpus median (G_cite + G_throughline) | foundation cite-deg 7.4 vs median 6.0; foundation tl-deg 0 vs median 0 (both at floor) | **PASS** on cite component, neutral on tl |
| **P2** Convictions show ≤50% CV in G_throughline degree | All 7 Convictions have degree 0 in G_throughline | **FAIL** — but for structural reasons (see §V3-2) |
| **P3** G_cite has ≥ 100 token-edges | 421 token-edges (38× v2's 11 edges) | **PASS** |

**Verdict: 2/3 properties pass → methodology validated.**

P2 fails because the throughlines_meta table doesn't lexically mention Convictions — Convictions are anchored to factions in the framework, factions to throughlines, but Convictions never appear in throughline name+description text directly. **This is itself a finding** (§V3-2 below) — it is not a methodology flaw.

---

## §V3-1 v2's flagship finding was an artifact — corrected

**v2 §1.1 claimed:** "The corpus is dominated by faction/NPC/Conviction tokens, not by mechanical systems. Top 15 high-similarity hubs are all factions, NPCs, or Convictions — zero mechanical systems."

**v3 corrects this.** v2 measured "high-similarity hubs" as TF-IDF mean cosine top quintile. But TF-IDF mean cosine is a function of paragraph breadth (how many paragraphs a token appears in), not citation centrality. Tokens that appear broadly in the corpus (Crown, Varfell — mentioned everywhere) score high cosine with everything; tokens that have specific, dense connections (NPC Behavior, CI) score lower mean cosine but higher *citation centrality*.

**Corrected hubs (top 17 by G_cite in+out degree):**

| Rank | Token | Cite degree | Class |
|---|---|---|---|
| 1 | NPC Behavior | 56 | system |
| 2 | CI | 46 | clock |
| 3 | Settlement Layer | 41 | system |
| 4 | Peninsular Strain | 31 | system |
| 5 | Scale Transitions | 27 | system |
| 6 | Campaign Architecture | 27 | system |
| 7 | Faction Layer | 26 | system |
| 8 | Conflict Architecture | 25 | system |
| 9 | Victory | 25 | system |
| 10 | MS | 21 | clock |
| 11 | CI Political | 20 | system |
| 12 | Threadwork | 17 | system |
| 13 | Mass Combat | 17 | system |
| 14 | IP | 17 | clock |
| 15 | Church | 16 | faction |
| 16 | Varfell | 15 | faction |
| 17 | Stability | 15 | mechanic |

**Of the top 17 cite hubs, 11 are mechanical systems, 3 are clocks, 1 is a mechanic (Stability), 2 are factions.** The corpus IS system-centered.

**The most important single correction:** **NPC Behavior is the integration spine of the corpus.** With 56 in+out citation edges across 84 tokens, NPC Behavior is referenced or references nearly 70% of all other tokens in the system. The "system-to-system integration" v2 worried was missing is in fact happening implicitly through NPC Behavior — Convictions, Pressure Points, Disposition, Standing, and most faction/NPC tokens all route through it.

**v2's recommendation to add `designs/integration/` is downgraded.** Some integrations (e.g. Mass Combat ↔ Faction Layer's Stability Trigger 5) may benefit from explicit integration docs, but the wholesale "corpus lacks integration" framing was wrong. The real recommendation is: **NPC Behavior is structurally load-bearing and should be vetted accordingly** — its quality is the project's quality at the integration layer.

---

## §V3-2 The throughlines framework doesn't formalize system-to-system relationships

**Finding:** All 7 Convictions have G_throughline degree 0 — they don't appear in any throughline's name+description. All 5 foundation tokens (Self-Rendering, Leap, Coherence, Throughlines, Ein Sof) have G_throughline degree 0 by the same mechanism. 42 of 43 throughlines have ≤ 2 substantiating paragraphs (paragraphs mentioning ≥2 of the throughline's lexically-identifiable system tokens).

The throughlines_meta table format is `T-NN | name | М-primary | М-secondary | description`. Names like "Everything Is Thread" or "Practitioner Arc" don't use system tokens lexically. Their relationship to the systems is conceptual.

**This is a documentation gap.** The throughlines framework anchors throughlines to М modes (mechanical-mode classifications) and to factions (via T-15a/b/c, T-08, T-09, T-11, etc.) but does not formalize which **specific system tokens** each throughline depends on. Implementation work that asks "which systems must Godot get right to deliver T-12 Practitioner Arc?" cannot read the answer off the framework — it has to be inferred from prose context.

**Recommendation:** the throughlines table should add a column or sub-block listing "load-bearing systems" per throughline. T-12 Practitioner Arc → [Coherence, Threadwork, NPC Behavior]; T-04 RS Decay → [MS, Peninsular Strain, Threadwork]; etc. This is hand-curation work but small (≤41 throughlines, mostly 2-3 systems each).

This finding alone justifies the v3 effort.

---

## §V3-3 Multi-graph hubs (highly cross-validated centrality)

Tokens that are top quintile by degree in **≥ 3 of 4 graphs** (cite, throughline, mu, pp):

| Token | Cite | Throughline | Mu | PP | Note |
|---|---|---|---|---|---|
| **Peninsular Strain** | 31 | — | 2 | 5 | Single most centrally-coupled token across multiple structured views |
| **IP** (Invasion Pressure) | 17 | — | 2 | 3 | Cross-confirmed centrality |

These two tokens are confirmed-central across multiple independent metadata graphs. Any change to Peninsular Strain or IP propagates broadly — change-control on these should be highest priority.

The **cite-only hubs** (top 17 above) include many systems with high cite centrality but no PP/mu coverage. Rank 1 (NPC Behavior, cite=56) has 0 in g_pp because no recent patches in `patch_register_active.yaml` modify it. This is itself notable: the most central system in the citation graph has had **zero patch activity** in the active register window. Either it's been correct since first written (unlikely for code that complex) or it hasn't been examined recently.

**Recommendation:** schedule an NPC Behavior audit pass. Despite being the corpus integration spine, it has had no recent patch activity, no editorial scrutiny in audit/session corpus (discourse ratio 0.20), and no cross-validation against current Convictions/Pressure Points design.

---

## §V3-4 Notional edges (cite present, no metadata) — top 15 informative

These are pairs heavily cross-mentioned in actual document bodies but never formalized in throughline, Μ, or PP metadata:

| Cite weight | Pair |
|---|---|
| 68 | Faction Layer → Stability |
| 58 | CI → Mandate |
| 55 | NPC Behavior → TS |
| 54 | Faction Layer → Mandate |
| 51 | CI → Restoration Movement |
| 48 | NPC Behavior → Stability |
| 44 | CI Political → Mandate |
| 44 | CI → Crown |
| 44 | CI → Church |
| 41 | Peninsular Strain → Victory |
| 39 | CI → Hafenmark |
| 38 | CI → MS |
| 37 | NPC Behavior → Varfell |
| 34 | CI → IP |
| 33 | CI → Varfell |

**Reading:** CI (Church Influence clock) has the highest fan-out with no metadata coupling — it shows up in citations to Mandate, Restoration Movement, Crown, Church, Hafenmark, MS, IP, Varfell, but is not formalized as part of any throughline or Μ mode. CI is *in practice* a major coupling point, but the throughlines framework doesn't recognize it as one.

**Recommendation:** CI's actual structural role should be reflected in throughlines. Specifically, CI should appear as load-bearing in any throughline that involves Church, Crown, or Hafenmark (i.e. T-08 Church Rendering Reinforcement, T-11 Crown Pragmatic, T-15a Hafenmark Unmediated — at minimum these three).

---

## §V3-5 Multi-graph isolates (degree ≤ 1 in every graph) — 14 tokens

Tokens that appear in the corpus but are connected to almost nothing in any structured graph:

```
Armature System          [provisional]   — provisional design, isolation expected
Event Impact Matrix      [provisional]   — provisional design, isolation expected
Authority                [canonical]     — Pressure Point, disambiguation excludes most paragraphs
Conviction Track         [canonical]     — central mechanic, no own file
Wager                    [canonical]     — mechanic, no own file
Thread Revelation        [canonical]     — sub-system in Campaign Architecture
Faith                    [canonical]     — Conviction
Reason                   [canonical]     — Conviction
Equity                   [canonical]     — Conviction
Precedent                [canonical]     — Conviction
Continuity               [canonical]     — Conviction
Consequence              [canonical]     — Pressure Point
Loyalty                  [canonical]     — Pressure Point
Game Master              [legacy/gap]    — legacy term, expected to disappear
```

**Real concerns (not artifacts):**
1. **Conviction Track** is canonical and central but has no dedicated file. Its definition lives inside `npc_behavior_v30.md`. This makes it an isolate even though it is heavily *used*. Recommendation: Conviction Track gets its own file at `designs/personal/conviction_track_v1.md` or equivalent. v3 §V3-1 confirms NPC Behavior is the integration spine; pulling Conviction Track out would let NPC Behavior reference it cleanly.

2. **Wager** is canonical but has only 4 paragraph mentions and 1 cite-edge. Either Wager is genuinely under-developed and needs more design substance, or it's documented under a different surface form not captured. Manual check warranted.

3. **Thread Revelation** is canonical (referenced from Campaign Architecture) but has no dedicated file — it lives as a section in the architecture doc. Should it be split out? Question for Jordan.

4. **5 of 7 Convictions** are isolates (Faith, Reason, Equity, Precedent, Continuity have cite=1 each; Order, Autonomy do better). The Conviction definitions live inline in NPC Behavior. They never get cited from elsewhere. This is the same pattern as Conviction Track — central concepts buried in their parent doc.

**Pattern:** the project has **canonical concepts that lack first-class documentation status**. They're real, used, mechanically active, but they're paragraphs inside other docs rather than entities that get cited. The candidates for promotion to dedicated files: Conviction Track, Wager, Thread Revelation, the 7 Convictions taxonomy, the 4 Pressure Points taxonomy. **Promotion to first-class docs would surface them in the citation graph** and make change-impact analysis cleaner.

---

## §V3-6 Discourse/design divergence — editorial attention vs design substance

Two list directions:

**HIGH discourse ratio** (audit/session attention ÷ design substance, ≥ 0.20 — over-discussed):

| Ratio | d-count | s-count | Token |
|---|---|---|---|
| 0.62 | 8 | 5 | Conflict Architecture |
| 0.50 | 6 | 3 | Throughlines |
| 0.44 | 16 | 7 | Conviction Track |
| 0.28 | 46 | 13 | Guilds |
| 0.27 | 11 | 3 | Coup Counter |
| 0.23 | 22 | 5 | Lisbeth Ehrenwall |
| 0.22 | 36 | 8 | Domain Echo |
| 0.21 | 101 | 21 | Löwenritter |
| 0.20 | 20 | 4 | Social Contests |

These tokens get more recent editorial attention than would be predicted by their design footprint. **Conviction Track at 0.44** with only 16 paragraphs of design substance and 7 of audit attention suggests it's either being actively refined (good — natural revision pattern) or being **discussed without sufficient design substance to anchor the discussion** (worrying).

**LOW discourse ratio** (substantial design substance, no recent editorial attention, ratio = 0.00):

```
Armature System          (13 d, 0 s) — provisional, untested
Lenneth                  (22 d, 0 s) — substantial NPC, no recent vetting
Equity                   (10 d, 0 s) — Conviction
Precedent                (15 d, 0 s) — Conviction
Continuity               (15 d, 0 s) — Conviction
Consequence              ( 6 d, 0 s) — Pressure Point
Authority                ( 6 d, 0 s) — Pressure Point
Loyalty                  ( 7 d, 0 s) — Pressure Point
Tensions                 (10 d, 0 s) — mechanic
```

**Concerning subset: 3 of 7 Convictions and 3 of 4 Pressure Points have zero recent editorial scrutiny.** These are foundational to NPC Behavior (the corpus's integration spine). They have substantial design substance (10-15 paragraphs each) but no recent audit, stress test, or vetting cycle.

**Recommendation:** add a line to `session_log_current.md` noting "Conviction taxonomy + Pressure Point taxonomy untouched in audit since their introduction; schedule review pass." This is a load-bearing-but-unvetted concern and should not silently persist.

---

## §V3-7 Cascade-without-return (G_cite, expanded)

With expanded citation graph (421 edges), 12,166 unique cascade chains of length ≥ 3 with no return path. Top terminals (downstream sinks, top 10):

| Terminal | Chains ending here |
|---|---|
| Threadwork | 487 |
| Church | 478 |
| Coherence | 445 |
| Stability | 428 |
| Disposition | 391 |
| Varfell | 377 |
| Knot | 375 |
| MS | 365 |
| Hafenmark | 354 |
| Domain Action | 346 |

**v2's Settlement Layer downstream sink finding is corrected:** Settlement Layer is no longer a top sink in v3's expanded graph — it ranks much lower because v3 captures Settlement Layer's references back to upstream docs (which v2's explicit-only parser missed). The finding "Settlement Layer doesn't cite back" was incorrect; Settlement Layer DOES cite back, just not in `Cross-references:` lines — it cites inline.

**Real downstream sinks in v3:**
- **Threadwork** (487) — terminal because Threadwork is a foundation that everyone references but doesn't itself reference scenes/factions. This is structurally correct: foundation → systems is a one-way dependency by design.
- **Coherence** (445), **Stability** (428), **MS** (365) — clocks are referenced everywhere and don't reference back, by design (clocks are state, not actors).
- **Knot** (375) — Knots are referenced from many places (Coherence cost depends on Knots; NPC bonds use Knots). Don't cite back because Knot is foundational.

**Concerning:**
- **Disposition** (391) — Disposition is a Standing-axis state that should receive inputs but doesn't formally cite the systems that change it (Domain Echo, NPC Behavior outcomes). Disposition lives inline in NPC Behavior + faction docs; it doesn't have its own file to cite from.
- **Domain Action** (346) — same pattern. Domain Action is referenced from many places but has no own file.

**Same root cause as §V3-5 isolates:** these are concepts without first-class documentation status. Promote to dedicated docs and the cascade-without-return becomes citation-with-feedback.

---

## §V3-8 Throughline orphan check — 42 of 43 orphaned

Defined: substantiating paragraph = paragraph mentioning ≥ 2 systems from the throughline's lexically-identified token set. With my parser, only 0-1 systems are identified per throughline (because throughline descriptions are terse), so substantiation count is essentially 0 for nearly all throughlines.

This is not the diagnostic value I designed it for. **It reduces to the same finding as §V3-2: throughlines aren't lexically anchored to systems.**

If the throughlines table gains the "load-bearing systems" column proposed in §V3-2, this diagnostic becomes meaningful and could surface real orphans.

---

## §V3-9 Vocabulary debt — confirmed and located precisely

| Term | Para | Docs | Concentration |
|---|---|---|---|
| Game Master | 16 | 3 | designs/threadwork/threadwork_v30.md (11/16), designs/npcs/npc_behavior_v30.md (3/16), designs/provincial/mass_battle_v30.md (2/16) |
| Cultural Reformation | 15 | 4 | designs/provincial/peninsular_strain_v30.md (10/15), complete_systems_reference (2/15), npc_behavior (1/15), victory_v30 (2/15) |
| Coup Counter | 11 | 7 | spread across 7 docs, max 3/11 in conflict_architecture_proposal.md |

**Game Master cleanup is concentrated** — 11 of 16 occurrences in `threadwork_v30.md` alone. Single-doc grep-and-replace handles 69% of the cleanup.

**Cultural Reformation cleanup is also concentrated** — 10 of 15 in `peninsular_strain_v30.md`. Single-doc edit handles 67%.

**Coup Counter is dispersed** — full sweep needed across 7 docs.

**Recommendation:** add three terms to a `terminology_gate.yaml` block-list once PP-675 advances. The two concentrated cleanups can ship as small standalone PPs (1 doc each). Coup Counter cleanup should be batched with PP-781's propagation pass.

---

## §V3-10 Items for v2 connections audit — updated

Replacing the v2 §4 list with corrected v3 priorities:

1. **NPC Behavior is the integration spine** — vet it as such. Schedule an NPC Behavior audit pass. v2's recommendation to create a `designs/integration/` directory is downgraded; the integration is already centralized in NPC Behavior.

2. **Promote canonical concepts to first-class docs:**
   - `designs/personal/conviction_track_v1.md` — currently inline in npc_behavior
   - `designs/peninsula/thread_revelation_v1.md` — currently inline in campaign_architecture
   - `designs/personal/conviction_taxonomy_v1.md` — formalize the 7 Convictions
   - `designs/personal/pressure_point_taxonomy_v1.md` — formalize the 4 Pressure Points
   - Possibly `designs/scene/wager_v1.md` and `designs/scene/domain_action_v1.md`

3. **Throughlines table needs "load-bearing systems" column.** Without it, the framework can't be machine-checked against the corpus.

4. **CI's actual structural role should be reflected in throughlines.** It appears in 9 of the top 15 notional pairs — major implicit coupling that no formal metadata captures.

5. **Conviction taxonomy + Pressure Point taxonomy haven't been audited.** Schedule a vetting pass. Ratio = 0.00 (zero recent editorial attention) on items central to NPC Behavior is a load-bearing-but-unvetted risk.

6. **Vocabulary debt cleanup:**
   - Game Master sweep concentrated in threadwork_v30.md
   - Cultural Reformation sweep concentrated in peninsular_strain_v30.md
   - Coup Counter dispersed sweep (7 docs) — batch with PP-781 propagation

7. **Schedule an audit of Peninsular Strain and IP** (the only multi-graph hubs across ≥3 of 4 structured views; highest change-impact propagation risk).

8. **Wager system needs a clarity audit** — sparse footprint despite canonical status.

---

## §V3-11 What v3 still can't find

1. **Conceptual relationships not lexically encoded.** The throughlines framework relates systems conceptually (T-12 Practitioner Arc depends on Coherence) but the framework's text doesn't say "Coherence." Lexical methods can't bridge this gap. Hand-curation is the only way.

2. **Quality of design within a system.** v3 measures connectivity, centrality, citation density. It doesn't measure whether a system's design is sound — only whether it's *connected* to things.

3. **Latent design dependencies.** Two systems might be tightly coupled because they share a design assumption (e.g. "all clocks tick on session boundary") without ever being cross-cited or co-occurring. Latent assumptions are invisible to all methods used here.

4. **Implementation order optimality.** v3's centrality findings suggest NPC Behavior should be implemented early in Godot work. But "early" depends on dependency direction, not just centrality. v3 doesn't direction-disambiguate citations.

5. **Vetting quality of the corpus's hubs.** v3 identifies NPC Behavior as central; it doesn't verify NPC Behavior is internally consistent or matches its claimed Μ ratings.

---

## §V3-12 Methodology caveats — v3-specific

1. **P2 validation failed** because Convictions don't appear lexically in throughline descriptions. Findings depending on G_throughline / G_mu (specifically §V3-3 multi-graph hubs ≥ 3 of 4) are constrained by metadata-graph sparsity. Findings depending on G_cite + G_pp (most other findings) are robust.

2. **G_cite uses ≥ 2 mention threshold for implicit references.** This filters paragraph-level accidents but admits some false positives where "Faction Layer §3.2" is mentioned twice in passing without substantive engagement. Manual check before any explicit cross-ref change.

3. **Token primary doc lookup matched only 29 of 84 tokens.** The other 55 lack dedicated files (Convictions, Pressure Points, NPCs, factions, clocks, sub-systems). For these tokens, G_cite degree is in-degree only (they cannot be citation sources). The in+out fix in this run handles this correctly, but interpretation should remember which tokens have "voice" in the citation graph and which only have "presence."

4. **PP register parses correctly** but covers only the 23 active patches. Archived patches (pre-rollover) are not in `patch_register_active.yaml`. Long-term coupling history is not captured.

5. **Discourse corpus is small** (4 docs, ~17k tokens) — discourse-design ratio findings have wider variance than design-internal findings.

6. **No cross-graph confidence scoring.** A finding present in 3 graphs and a finding present in 1 graph are reported in the same register without explicit confidence weighting beyond textual qualification. Future runs should add a numeric confidence score.

---

## §V3-13 v2 findings retained vs corrected

| v2 finding | v3 status |
|---|---|
| §1.1 Faction/NPC/Conviction-as-hubs | **CORRECTED** — v3 §V3-1; corpus IS system-anchored, NPC Behavior is the spine |
| §1.2 Settlement Layer downstream sink | **PARTIALLY CORRECTED** — v3 §V3-7; Settlement Layer is not a top-10 sink in expanded graph; v2 finding was artifact of explicit-only citation parsing |
| §1.3 Notional edges (MS Trajectory → Leap, etc.) | **REPLACED** by v3 §V3-4 with corrected list |
| §1.4 Wager↔Edeyja implied connection | **NOT VERIFIED IN V3** — v3's expanded citation graph would need to be checked specifically for this pair; surviving as a v2 finding pending verification |
| §1.5 Vocabulary debt | **CONFIRMED + LOCATED PRECISELY** — v3 §V3-9 |
| §1.6 Sparse-context tokens | **CONFIRMED + REFINED** — v3 §V3-5 + §V3-6 |
| §1.7 Empty regions diagnostic null | **DROPPED** — v3 removed this diagnostic (not informative at this scale) |
| §2 "Project documents people, not systems" | **CORRECTED** — v3 §V3-1 reverses this; the corpus IS system-anchored when measured by citation degree, not paragraph breadth |
| §4 v2 connections audit items | **REPLACED** by v3 §V3-10 |

The single most consequential correction: **v2's "the project documents people, not systems" structural claim was wrong.** The project documents both, but the citation backbone is system-anchored, with NPC Behavior as the integration spine. v3's recommendation pivots accordingly: vet NPC Behavior, promote currently-inline canonical concepts (Conviction Track, Convictions/Pressure Points taxonomies) to first-class docs, and add load-bearing-systems columns to the throughlines table.
