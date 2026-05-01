# Vector Audit — 2026-04-30 — Weakness Register

STATUS: AUDIT
RUN: 2026-04-30
PRIMARY DELIVERABLE
SCOPE: Terminology — drift, conceptual overlap, registry coverage, vocabulary debt.

---

## §0 Validation outcome (must be read first)

**2/3 properties pass** (P1 corrected, P3 pass; **P2 conviction-symmetry FAIL**). Methodology publishes as authoritative. P2 fail downgrades Mode F findings to **[CONFIDENCE: low]**; Modes A, B (caveated), C, D, E, G, H findings are **[CONFIDENCE: high]**. Full validation breakdown in `03_validation_report.md`.

**This run's primary use case** — terminology drift / registry coverage / vocabulary debt — relies almost exclusively on Modes G and H, both unaffected by P2 fail. Confidence on terminology findings is therefore high.

---

## §1 Mode G — Vocabulary debt sweep (today's corpus)

**[CONFIDENCE: high]** — direct grep, methodology-independent.

### §1.1 Today's actionable counts (excluding [STRUCK] markers)

| Term | Total para | Actionable | Δ vs v3 (2026-04-29) | Notes |
|---|---:|---:|---:|---|
| **GM (bare)** | 29 | 29 | new — not swept by v3 | Distinct from `Game Master` bigram. PP-678 swept the bigram (16 → 0); bare `GM` was not in scope. Session log: "Bare 'GM' corpus sweep TBD." |
| **Niflhel (as faction)** | 23 | 23 | not in v3 sweep list | ED-764 STRUCK Niflhel-as-faction; place references retained. Faction-context filter on `faction\|Mandate\|Influence\|grievance\|Operative\|Syndicate`. |
| **TC (as Church Influence)** | 21 | 21 | not in v3 sweep list | alias_registry collision_table claims "RESOLVED 2026-04-26" — **contradicted by corpus**. 16 of 21 concentrated in `designs/npcs/npc_behavior_v30.md`. |
| **VTM** | 18 | 18 | not in v3 sweep list | Strike 2026-04-19 per supersession_register. Highest concentration `designs/provincial/victory_v30.md` (5) + `params/bg/victory.md` (4). |
| **Cultural Reformation** | 13 | 13 | 15 → 13 (−2) | PP-678 partial sweep. 10 of 13 still concentrated in `designs/provincial/peninsular_strain_v30.md`. |
| **Coup Counter** | 6 | 6 | 11 → 6 (−5) | ED-781 STRUCK; replacement Graduated Autonomy. Spread across 4 docs; needs design-judgment substitution per site (not 1:1). |
| **Cohesion** | 5 | 5 | not in v3 sweep list | Renamed to Discipline (PP-232). Mass-combat doc cluster: `mass_battle_v30` (2) + `params/mass_combat` (2) + `peninsular_strain_v30` (1). |
| **Vaynard Thread Mastery** (full phrase, separately tracked) | 2 | 2 | not in v3 sweep list | Both in `params/bg/victory.md`. |
| **Rendering Stability** | 1 | 1 | not in v3 sweep list | `canon/02_foundations_amendment_leap_mechanism.md`. ED-731 note: "Historical RS references retained as annotations in canon/02 per intentional design" — **flag for verification this is the retained reference**, not residual. |
| **Combat Power** | 0 | 0 | clean | PP-678 + prior sweeps complete. |
| **Thread Depth** | 0 | 0 | clean | PP-166 + subsequent cleanup complete. |
| **Theocracy Counter** (full phrase) | 0 | 0 | clean | ED-782 successful for the bigram. The `TC` standalone abbreviation is the residual (separate row). |
| **Game Master** (full phrase) | 0 | 0 | 16 → 0 (−16) | **PP-678 fully effective.** Bare `GM` is the open follow-up. |

**Total actionable: 118 paragraphs across 9 distinct legacy terms.**

### §1.2 Concentration analysis (single-doc grep-replace candidates)

Methodology §3.7 / Mode G recommendation: "Single-doc concentration is the cleanup signal."

| Term | Top doc | Concentration | Action |
|---|---|---|---|
| TC (Church Influence) | `designs/npcs/npc_behavior_v30.md` | 16 / 21 (76%) | **Single-doc grep-replace TC → CI** in npc_behavior_v30. Resolves 76% in one commit. |
| Cultural Reformation | `designs/provincial/peninsular_strain_v30.md` | 10 / 13 (77%) | Single-doc deletion / strikethrough wrap (depending on CR-STRIKE replacement plan). |
| VTM | `designs/provincial/victory_v30.md` + `params/bg/victory.md` | 9 / 18 (50%) | Two-doc focused cleanup. Victory paths require design rewrite per supersession_register. |
| GM (bare) | `designs/npcs/npc_behavior_v30.md` | 5 / 29 (17%) | **Diffuse — no single-doc win.** Requires corpus-wide `\bGM\b` → `Game Master` substitution sweep. |
| Niflhel (as faction) | `designs/architecture/conflict_architecture_proposal.md` + `designs/provincial/faction_layer_v30.md` | 10 / 23 (43%) | Two-doc focused cleanup. Faction-context references need design-judgment substitution (Niflhel → Syndicate? → null?). |
| Coup Counter | dispersed across 4 docs (max 3) | 6 paragraphs total | Per-site Graduated Autonomy substitution; design judgment. |
| Cohesion | mass-combat doc cluster | 5 / 5 (100% in 3 docs) | Three-doc grep-replace `Cohesion` → `Discipline`. |
| Vaynard Thread Mastery | `params/bg/victory.md` | 2 / 2 (100%) | Single-doc cleanup paired with VTM abbreviation sweep. |
| Rendering Stability | `canon/02_foundations_amendment_leap_mechanism.md` | 1 / 1 | Verify per ED-731 retention note before action. |

### §1.3 Cleanup priority queue (action-ready)

1. **Single-doc grep-replace TC → CI** in `designs/npcs/npc_behavior_v30.md` (16 paragraphs, mechanical) — resolves the alias_registry vs corpus contradiction noted in the registries-only conflict report.
2. **Three-doc sweep `Cohesion` → `Discipline`** in `designs/provincial/mass_battle_v30.md`, `params/mass_combat.md`, `designs/provincial/peninsular_strain_v30.md` — straightforward rename per PP-232 legacy_renames.
3. **Two-doc VTM sweep** in `designs/provincial/victory_v30.md` + `params/bg/victory.md` — requires Varfell victory-path editorial rewrite per supersession_register VTM-STRIKE entry; cannot grep-replace without design substitution.
4. **Cultural Reformation cleanup** in `designs/provincial/peninsular_strain_v30.md` (10 paragraphs concentrated) — requires design substitution (CR struck per Vaynard military-conqueror identity; replacements TBD).
5. **Niflhel faction-context audit** of `designs/architecture/conflict_architecture_proposal.md` + `designs/provincial/faction_layer_v30.md` (10 paragraphs concentrated) — needs Jordan decision: are these residual ED-764 misses, or are they legitimate place-references that the context filter mis-flagged? Sample paragraphs needed.
6. **Coup Counter → Graduated Autonomy per-site substitution** — 6 paragraphs across 4 docs; design judgment per site.
7. **Bare `GM` corpus sweep** — 29 paragraphs across 14 docs; mechanical replacement (GM → engine resolution / Game Master full phrase / context-appropriate term). Diffuse; corpus-wide pass.
8. **Rendering Stability verification** in `canon/02_foundations_amendment_leap_mechanism.md` — 1 paragraph; confirm intentional-retention per ED-731.

---

## §2 Mode H — Multi-graph isolates (cross-referenced with registry coverage)

**[CONFIDENCE: high]** — degree calculations independent of P2.

Tokens with `max(degree) ≤ 1` across G_cite, G_throughline, G_mu, G_pp. Cross-referenced with glossary and alias_registry presence to inform action category.

| Token | cite | tl | mu | pp | Glossary? | Alias-reg? | Action category |
|---|---:|---:|---:|---:|:-:|:-:|---|
| **Wager** | 1 | 0 | 0 | 0 | NO | NO | **A — promote + register.** Canonical system per `canonical_sources.yaml`; no first-class doc; no glossary entry; no alias_registry entry. Session-log P1 deferral confirms Wager is "isolate promotion candidate ~PP-681-scope." Three-axis gap. |
| **Thread Revelation** | 1 | 0 | 0 | 0 | NO | NO | **A — promote + register.** Session log P1 deferral. Same three-axis gap as Wager. |
| **Armature System** | 0 | 0 | 0 | 0 | NO | NO | **B — clarify status.** Token marked PROVISIONAL in seed list (`vector_audit.py` SEED_TOKENS); no glossary, no alias-reg, no graph presence. Either canonical and needs full registration, or struck and needs supersession entry. |
| **Event Impact Matrix** | 0 | 0 | 0 | 0 | NO | NO | **B — clarify status.** Same as Armature System. |
| **Conviction Track** | 1 | 0 | 0 | 0 | YES | YES | **C — registered, structurally isolated.** Promoted to first-class doc PP-681 (`designs/personal/conviction_track_v1.md`). Glossary §3 + alias_registry `debate_system.conviction_track` both present. The `tl=0/mu=0/pp=0` is a **stale-graph artifact** — promotion happened recently and citation graph hasn't yet absorbed the new doc. Re-extract corpus on next audit run to refresh. |
| **Game Master** | 1 | 0 | 0 | 0 | YES | YES | **D — struck-target.** Glossary §9 + alias_registry `infrastructure.game_master` (standalone_ok: true) registered. PP-678 swept the bigram to 0; the cite=1 is a residual edge from the v3 corpus snapshot which has since cleaned. **Glossary should mark Game Master as videogame-engine-mapped per project instructions** (see §3 conceptual overlap). |
| **Faith** | 1 | 0 | 0 | 0 | NO | NO | **A — promote + register.** Conviction-class member. Per P2 finding, all 7 Convictions are degree-0 in G_throughline despite Conviction Track + NPC Behavior referencing them. Add to alias_registry under `convictions:` block; glossary needs new section "Convictions framework." |
| **Reason** | 1 | 0 | 0 | 0 | YES (line 213) | NO | **C-partial — glossary disambiguation entry, no canonical entry.** Glossary's mention is in COLLISION TABLE for "Reason" (English ambiguity). No canonical Conviction-as-Reason entry. Add. |
| **Equity** | 1 | 0 | 0 | 0 | NO | NO | **A — promote + register.** Same as Faith. |
| **Precedent** | 1 | 0 | 0 | 0 | YES (line 213) | NO | **C-partial.** Same as Reason. |
| **Continuity** | 1 | 0 | 0 | 0 | NO | NO | **A — promote + register.** Same as Faith. |
| **Authority** | 0 | 0 | 0 | 0 | YES (line 213) | NO | **C-partial.** Pressure-Point-class. Glossary disambiguation only; no canonical entry. |
| **Consequence** | 1 | 0 | 0 | 0 | NO | NO | **A — promote + register.** Pressure-Point-class. |
| **Loyalty** | 1 | 0 | 0 | 0 | NO | YES (alias only) | **A-partial.** Pressure-Point-class. alias_registry has it under disambiguation but no glossary entry. |

**Aggregate:**
- 7 of 14 isolates are NOT in glossary AND NOT in alias_registry → **fully unregistered canonical concepts** (action category A).
- 4 of 14 are partial-registered (glossary disambiguation only, or alias-reg only) → action category C/A-partial.
- 2 of 14 are fully registered but structurally isolated → stale-graph artefact or struck-target.
- 1 of 14 (Conviction Track) is a recent promotion with stale-graph artefact.

**Cross-reference to registries-only conflict report §4:** The 14 multi-graph isolates here OVERLAP with my §4 list of "15 canonical/provisional systems missing from glossary" but are not identical. Vector-audit isolates Wager, Thread Revelation, Armature System, Event Impact Matrix, and the Convictions/PP framework members. Registries-only §4 added Settlement Adjacency, Fractional Province Ownership, Faction Succession Split, Tensions Deck, Royal Assassination Fuse, Peninsular Strain, MS Trajectory, Approach Training, Wrong-Style Penalty, Heresy Investigation Lifecycle, Knot Lifecycle, Demotion Magnitude, Miraculous Event — most of which are NOT in the v3 token list (auto-extract threshold ≥3 docs AND ≥10 paragraphs failed for these recent additions). **Vector-audit and registries-only audit are complementary; neither subsumes the other.** Joint action queue:

| Source-of-finding | Tokens |
|---|---|
| Both audits | Wager, Thread Revelation, the 7 Convictions, the 4 Pressure Points |
| Vector-audit only | Armature System, Event Impact Matrix |
| Registries-only (below v3 token threshold) | Settlement Adjacency, Fractional Province Ownership, Faction Succession Split, Tensions Deck, Royal Assassination Fuse, Peninsular Strain (already in graph as hub — only registry-missing), MS Trajectory, Approach Training, Wrong-Style Penalty, Heresy Investigation Lifecycle, Knot Lifecycle, Demotion Magnitude, Miraculous Event, Graduated Autonomy |

---

## §3 Mode A — Multi-graph hubs

**[CONFIDENCE: high]** — top quintile in ≥3 of 4 graphs.

Inherited from v3 (no graph regeneration this run):

| Token | cite | tl | mu | pp | Note |
|---|---:|---:|---:|---:|---|
| Peninsular Strain | 31 | (top) | 2 | 5 | Highest cross-validated centrality. |
| IP | 17 | (top) | 2 | 3 | Pressure clock; load-bearing. |

**Single-graph cite hubs (supplementary, top 17):** NPC Behavior (56), CI (46), Settlement Layer (41), Peninsular Strain (31), Scale Transitions (27), Campaign Architecture (27), Faction Layer (26), Conflict Architecture (25), Victory (25), MS (21), CI Political (20), Threadwork (17), Mass Combat (17), IP (17), Church (16), Varfell (15), Stability (15).

**Terminology implication:**
- All multi-graph hubs and 15 of 17 cite hubs are **registered in glossary** (with the exception of Peninsular Strain, Conflict Architecture, Campaign Architecture, Victory, CI Political — all canonical systems per `canonical_sources.yaml` but not glossary entries). These are top-level systems; their absence from the glossary represents the gap "the registry treats systems as files, the glossary treats systems as terms" — they are systems with file-level canonical authority but no term-level canonical entry.
- **Action:** Add glossary entries for Peninsular Strain, Conflict Architecture, Campaign Architecture, Victory, CI Political. Each is a hub; their absence is a high-impact terminology gap.

---

## §4 Mode B — Implied-but-missing edges

**[CONFIDENCE: medium]** — partially affected by P2 (G_throughline contribution reduced).

Inherited from v3:

| Token A | Token B | Metadata graphs linking | Strength |
|---|---|---:|---:|
| Inge Baralta | TS | 2 (mu, pp) | 3 |
| Hafenmark | TS | 2 (mu, pp) | 3 |
| Hafenmark | Inge Baralta | 2 (mu, pp) | 3 |

**Terminology implication:** The three implied-missing pairs all involve **TS (Thread Sensitivity)** + a Hafenmark-related entity (Inge Baralta is the Hafenmark Cardinal NPC; Hafenmark is the faction). Pattern: TS is metadata-coupled to Hafenmark via mu (Μ-mode) and pp (patch register) but no explicit citation links them in the corpus. This suggests Hafenmark's TS-related provisions (institutional TS access, Cardinal scholarship → ceiling 10–20 per ED-727) are referenced in metadata but not anchored in faction-layer prose.

**Action:** Add explicit cross-references in `designs/provincial/faction_layer_v30.md` Hafenmark section linking to Thread Sensitivity stat + ED-727 (Lenneth pathway) + Inge Baralta's TS arc.

**No terminology drift here** — these are connection gaps, not term-naming conflicts. Noted for completeness; out of scope for the glossary update.

---

## §5 Mode C — Notional edges (top 15 by cite weight)

**[CONFIDENCE: high]** — cite weight + metadata absence are independent of P2.

Inherited from v3. Cite-weight ≥ 30 with no metadata coupling:

| Cite weight | Source → Target | Reading |
|---|---|---|
| 68 | Faction Layer → Stability | Heavy citation, no metadata coupling. |
| 58 | CI → Mandate | |
| 55 | NPC Behavior → TS | |
| 54 | Faction Layer → Mandate | |
| 51 | CI → Restoration Movement | |
| 48 | NPC Behavior → Stability | |
| 44 | CI Political → Mandate | |
| 44 | CI → Crown | |
| 44 | CI → Church | |
| 41 | Peninsular Strain → Victory | |
| 39 | CI → Hafenmark | |
| 38 | CI → MS | |
| 37 | NPC Behavior → Varfell | |
| 34 | CI → IP | |
| 33 | CI → Varfell | |

**Terminology implication:** **CI (Church Influence) appears as source in 9 of top 15 notional edges.** It is the single largest implicit hub with no metadata coupling — heavily cited but not formally linked into throughlines, Μ-modes, or patch register affects. Per Mode C action recommendation:

**Action:** Either (a) add CI to relevant throughlines (formalize the coupling — addresses P2-style framework gaps for clocks), or (b) downgrade citation visibility (which is impractical since CI is canonical hub).

**Glossary implication:** CI's glossary entry (line 62) currently lists thresholds 60 / 75 / 100 with descriptions. The alias_registry CI entry has a different threshold (`65 = Church Holy State (BG)`). The notional-edge density implies CI's narrative weight is not matched by structural metadata anchoring — including in the registries themselves. The glossary/alias-reg threshold disagreement is a symptom of this. **Resolve thresholds first** (registries-only conflict report §2) before propagating CI clock-state language.

---

## §6 Mode D — Cascade-without-return (top terminals)

**[CONFIDENCE: high]** — pure citation-graph DFS.

Inherited from v3 (12,166 chains total):

| Terminal | Chains ending here | Reading |
|---|---:|---|
| Threadwork | 487 | Foundation — receives, doesn't reference scenes (correct by design). |
| Church | 478 | Faction sink. |
| Coherence | 445 | Foundation. |
| Stability | 428 | Faction stat. Heavily downstream. |
| **Disposition** | 391 | **CONCERN — no own file.** Concept buried in NPC Behavior + factions. |
| Varfell | 377 | Faction. |
| Knot | 375 | Mechanic. |
| MS | 365 | World clock — foundation. |
| Hafenmark | 354 | Faction. |
| **Domain Action** | 346 | **CONCERN — no own file.** Concept buried in scale_transitions + faction_layer. |

**Terminology implication:** Two cascade sinks lack first-class docs:
- **Disposition** — referenced 391× as cascade terminal; alias_registry has it as `disposition: canonical: "Disposition", category: stat`. Glossary does **not** have Disposition as an entry. **Add to glossary.** Disposition is canonical mechanic, used heavily downstream, and currently exists only in alias_registry.
- **Domain Action** — referenced 346× as cascade terminal; glossary refers to it in passing (Zoom In definition: "Mechanically implemented as a transition phase during Domain Action resolution"). Neither glossary nor alias_registry has a canonical Domain Action entry. **Add to glossary; add to alias_registry under `mechanic` category.**

---

## §7 Mode E — Sparse-context tokens

**[CONFIDENCE: high]** — paragraph + cite degree only.

Inherited from v3 (bottom 10th percentile in BOTH paragraph count AND G_cite degree):

| Token | Paragraphs | Cite deg | Glossary? | Alias-reg? | Action |
|---|---:|---:|:-:|:-:|---|
| Wager | 4 | 1 | NO | NO | Promote (Mode H A-action) — corpus footprint thin because no first-class doc. |
| Thread Revelation | 6 | 1 | NO | NO | Promote (Mode H A-action). |
| Event Impact Matrix | 6 | 0 | NO | NO | Clarify status (Mode H B-action). |
| Consequence | 6 | 1 | NO | NO | Promote (Mode H A-action). |
| Authority | 6 | 0 | YES (disambig only) | NO | Promote — glossary canonical entry. |

All 5 sparse tokens are also Mode H isolates. Sparse-context confirms the registration gap from a different graph perspective: thin corpus footprint AND thin citation degree both indicate buried concepts.

---

## §8 Mode F — Throughline orphans

**[CONFIDENCE: low]** — directly degraded by P2 fail.

Inherited from v3 (≤2 substantiating paragraphs):

42 throughlines flagged. Top 15:

| Throughline | Substantiating paragraphs |
|---|---:|
| 01 Everything Is Thread | 0 |
| 02 Rendering Consciousness-Performed | 0 |
| 03 Inseparability | 0 |
| 04 RS Decay | 0 |
| 05 TC Accumulation | 0 |
| 06 IP Accumulation | 1 |
| 07 Peninsular Strain | 1 |
| 08 Church Rendering Reinforcement | 1 |
| 09 Varfell Thread Progressive | 1 |
| 11 Crown Pragmatic | 1 |
| 12 Practitioner Arc | 1 |
| 13 Certainty Journey | 0 |
| 14 Conviction Architecture | 1 |
| 15b Löwenritter Substrate-Agnostic Protector | 1 |
| 15c RM Substrate-Heritage Reclaimer | 1 |

**Caveat:** P2 fail means G_throughline has degenerate Conviction degrees (all zeros). Mode F's "substantiating paragraphs" measure depends on Load-bearing systems extraction from `references/throughlines_meta_infill.md`. With Conviction tokens degenerate, Conviction-bearing throughlines are systematically under-counted. **Numbers above are floor estimates.**

**Terminology implication:**
- Throughline 04 "RS Decay" still uses **Rendering Stability (RS)** — the legacy term renamed to Mending Stability per ED-731. This is a legacy-term residual in the throughlines table itself. **Action:** rename to "MS Decay" in `references/throughlines_meta_infill.md` T-04 row.
- Throughline 05 "TC Accumulation" still uses **TC** — the legacy term renamed to CI per ED-782. **Action:** rename to "CI Accumulation" in T-05 row.
- These are two terminology drift findings inside the throughlines framework table itself (not just the design corpus).

---

## §9 Mode H — Multi-graph isolates

See §2 above. Full table reproduced for register completeness; cross-referenced analysis is in §2.

---

## §10 Discourse / design ratio (Mode 7 overlay)

**[CONFIDENCE: medium]** — single-graph signal.

Inherited from v3, top 10 by ratio (discourse mentions / design mentions):

| Token | Discourse | Design | Ratio | Reading |
|---|---:|---:|---:|---|
| Conflict Architecture | 8 | 5 | 0.625 | Discourse-heavy — system designed in workplans, less anchored in canon. |
| Throughlines | 6 | 3 | 0.500 | Same. |
| Conviction Track | 16 | 7 | 0.438 | Recently promoted (PP-681); design-corpus presence catching up. |
| Guilds | 46 | 13 | 0.283 | Faction discussed in workplans more than designed in core docs. |
| **Coup Counter** | 11 | 3 | 0.273 | **Struck term still in discourse.** Workplan/audit references outpace design refs (which are now near-zero post-cleanup). Acceptable — discourse retains historical record. |
| Lisbeth Ehrenwall | 22 | 5 | 0.227 | NPC discussed in NPC analyses + audit work; less prose anchoring. |
| Domain Echo | 36 | 8 | 0.222 | |
| Löwenritter | 101 | 21 | 0.208 | Faction with high discourse but proportional design. |
| Social Contests | 20 | 4 | 0.200 | |
| Confessor Arne | 26 | 5 | 0.192 | |

**Terminology implication:** The Coup Counter discourse/design split is reassuring — struck term is appropriately fading from design corpus while audit trail retains it. Other high-discourse tokens (Conflict Architecture, Throughlines, Guilds) are not terminology drift — they are governance / design-process artefacts, not terminological problems. Out of scope for the glossary deliverable.

---

## §11 Synthesis — Terminology actions, ranked

### §11.1 P0 (do now — same session if directive permits)

1. **Resolve TC sweep status contradiction.** alias_registry says RESOLVED; corpus has 21 actionable TC=Church-Influence residuals. Single-doc grep-replace `\bTC\b` → `CI` in `designs/npcs/npc_behavior_v30.md` (16 paragraphs, 76% of total). Update alias_registry collision_table.tc.status from `resolved` to `partial — 16 in npc_behavior_v30 pending`.
2. **Add Disposition + Domain Action to glossary** (Mode D cascade sinks; both heavily downstream-referenced; Disposition is in alias_registry but not glossary; Domain Action is in neither).
3. **Add hub systems missing from glossary:** Peninsular Strain, Conflict Architecture, Campaign Architecture, Victory, CI Political (Mode A — all top-quintile cite hubs).
4. **Update glossary §12 (UNRESOLVED).** All entries (CERT, TLK, DD, FSTAT, CE, INT) are resolved in alias_registry. Either delete §12 or rewrite as historical annex.
5. **Resolve CI threshold disagreement.** glossary line 62 vs alias_registry line 149. Cross-check against `references/canonical_sources.yaml` `tc_political` entry (`designs/provincial/ci_political_v30.md` is canonical authority). Choose one threshold spec; propagate.

### §11.2 P1 (next directive)

6. **Promote Wager + Thread Revelation to first-class docs** (Mode H A-action; session log already flagged each as ~PP-681-scope).
7. **Convictions framework registration.** Add Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity to alias_registry under new `convictions:` block. Add a new glossary section "PART X — CONVICTIONS FRAMEWORK." Cross-link to Conviction Track.
8. **Pressure Points framework registration.** Add Evidence, Consequence, Authority, Loyalty to alias_registry under `pressure_points:` block. Add glossary section. Per session log, "Pressure Points Taxonomy" is also a P1 isolate-promotion candidate.
9. **Throughlines table legacy-term rename.** T-04 "RS Decay" → "MS Decay"; T-05 "TC Accumulation" → "CI Accumulation" in `references/throughlines_meta_infill.md`.
10. **Three-doc Cohesion → Discipline sweep** (Mode G #2).
11. **Bare GM corpus sweep** (29 paragraphs, 14 docs; mechanical replacement). Update alias_registry `infrastructure.game_master.standalone_ok` from `true` to `false` to bring policy in sync with practice; update glossary §9 to mark Game Master as "engine resolution authority in videogame implementation."

### §11.3 P2 (subsequent)

12. **VTM full sweep + Varfell victory-path editorial rewrite** (Mode G #3) — design judgment required, not mechanical.
13. **Cultural Reformation sweep + replacement** in `peninsular_strain_v30.md` (Mode G #4) — design judgment.
14. **Niflhel faction-context audit** (Mode G #5) — sample paragraphs needed.
15. **Coup Counter → Graduated Autonomy per-site substitution** (Mode G #6).
16. **Armature System + Event Impact Matrix status clarification** (Mode H B-action).
17. **Add to v3 token list for next vector-audit run:** Settlement Adjacency, Fractional Province Ownership, Faction Succession Split, Tensions Deck, Royal Assassination Fuse, MS Trajectory, Approach Training, Wrong-Style Penalty, Heresy Investigation Lifecycle, Knot Lifecycle, Demotion Magnitude, Miraculous Event, Graduated Autonomy. Re-extract auto-candidates with updated threshold tolerance to ensure these recent EDs are surfaced.
18. **Populate `references/censured_vocabulary.yaml`** with confirmed struck terms: VTM, Cultural Reformation, Coup Counter, Theocracy Counter, Combat Power, Cohesion, Thread Depth, Rendering Stability, Niflhel-as-faction. Currently empty stub.
19. **Update CI loss thresholds** in glossary + alias_registry to match canonical `designs/provincial/ci_political_v30.md` (with reference to supersession_register entry `250715f` probabilistic curve).

### §11.4 Methodology follow-ups (not terminology)

20. **P2 conviction-symmetry audit.** Investigate whether Conviction-bearing throughlines actually list Conviction tokens in their Load-bearing systems column. If yes — extraction script bug. If no — Convictions are not formalized as load-bearing despite participating in Conviction Track + NPC Behavior. Either case is a P2 → P1 finding.
21. **Re-run vector-audit after P0+P1 actions land** to refresh structural graphs and confirm Mode H reductions.

---

## §12 Closing notes

- **Validation:** Methodology PUBLISHES as authoritative (P1 corrected + P3 = 2/3). Terminology findings inherit HIGH confidence. P2 fail is a separate finding for the throughlines framework, not a terminology-audit caveat.
- **Inheritance:** Stages 0–5 + Modes A/B/C/D/E/F/H inherited from 2026-04-29. Mode G executed today against expanded struck-term list; superseded v3's narrower sweep. See `01_methodology.md` §1–§3 for full provenance.
- **Limit:** This run did NOT auto-extract new tokens. Recent EDs (ED-772..ED-779) and Stage 4 promotions (Solmund splits, miraculous_event, baralta) are not in the v3 token list. Action #17 above schedules them for the next run.
- **Cross-check vs registries-only conflict report:** This audit complements but does not subsume the registries-only conflict report. The registries-only pass surfaced glossary ↔ alias_registry drift (CI thresholds, §12 staleness, Standing miscategorization, RS legacy gap) that the vector-audit cannot see (no graph for registry internal consistency). The vector-audit surfaces corpus-wide vocabulary debt and isolate detection that the registries-only pass cannot quantify. **Both are needed.**

---

*Generated by valoria-vector-audit skill (v3 methodology) at user direction. Inheritance from designs/audit/2026-04-29-topographic-analysis/ disclosed in 01_methodology.md §1.*
