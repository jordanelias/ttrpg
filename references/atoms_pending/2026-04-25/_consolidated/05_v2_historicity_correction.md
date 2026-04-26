# v2 Historicity Correction (Three Kingdoms / Sengoku) (consolidated)

## Consolidation front matter

- **topic_id:** `05_v2_historicity_correction`
- **atom_count:** 9
- **scope:** valoria_master_analysis.md atoms not already in throughline cluster. v2 cross-lens audit Parts B (Three Kingdoms) and C (Sengoku); 5-tier factual audit; 54-proposal N-check.
- **source distribution:**
  - `valoria_master_analysis.md`: 9 atoms
- **drift surface:** single-source
- **post-audit canon target:** `designs/audit/`
- **status:** assembled (pending audit Stage 3)
- **assembled_from_commit:** atoms committed at `83c37da7001defdf3bb3425b17dda3f934d262d3`

## Audit checklist (Stage 3 input)

- [ ] All 5 audit tiers are described once.
- [ ] All 54 proposal N-check entries are present and individually auditable.
- [ ] Cross-references to designs/audit/ files are valid.
- [ ] Historicity claims (e.g., Three Kingdoms / Sengoku) are documented with sources.

## Known drift dimensions

- Internal only — single source.

## Content

Atoms in section_index order from source.

<!-- atom: valoria_master_analysis__00__preamble | section_index: 0 | source_section: "(preamble)" -->


# Valoria v2 Historicity Correction — Master Analytical Document

**Session.** `4870a501cdf4853e`, continuation 2026-04-22/23.
**Scope.** Historicity correction of cross-lens audit Parts B (Three Kingdoms) and C (Sengoku); full analytical chain from v2 production through throughline/meta-throughline identification.

---

<!-- atom: valoria_master_analysis__01__section-1-task-and-corrections-made | section_index: 1 | source_section: "Section 1 — Task and corrections made" -->


## Section 1 — Task and corrections made

**Original problem.** v1 cross-lens audit (prior-session output) used *Romance of the Three Kingdoms* (Sanguo Yanyi, 14th c. novel) and Edo-period romanticized Sengoku framings rather than historical Han-collapse (184-280 CE) and Sengoku-era (1467-1600) sources.

**Struck from v1:** Peach Garden Oath, Empty City Ploy, Borrowed Arrows, 36-Stratagems catalog, moral-archetype character framings (Guan-Yu-Righteousness / Cao-Cao-Pragmatic-Ambition / Zhuge-Liang-Complete-Wisdom), novelistic weapon names (Green Dragon Crescent Blade, Serpent Spear, Sky Piercer), Zhuge-Liang-hut-visits as central narrative device; *fudai/tozama* as strict Sengoku categories (Tokugawa formalization), *sankin-kōtai* as Sengoku (Tokugawa 1635), Masamune/Muramasa cursed-sword moral polarity (Edo folklore), shinobi-as-covert-ops popular framing, Nagashino-volley-fire-revolution-as-settled-fact, Rikyū-as-unaffiliated-master (Hideyoshi retainer), symmetric-losses "ritualized mutual exchange" overstatement.

**Replaced with:** Chen Shou's *Sanguozhi* (三國志, composed 280s-90s CE under Jin) for TK; attested Sengoku-era institutions and events for Sengoku.

**Scope preservation.** Parts A (non-Renaissance → Renaissance) and D (missing Renaissance elements, full R/E/S treatment) kept verbatim from v1. v1's Part A and D are architecturally sound.

---

<!-- atom: valoria_master_analysis__02__section-2-deliverables-produced | section_index: 2 | source_section: "Section 2 — Deliverables produced" -->


## Section 2 — Deliverables produced

| File | Lines | Purpose |
|---|---|---|
| `valoria_cross_lens_audit_and_renaissance_expansion.md` | 761 | v2 cross-lens audit — Parts A, D preserved; Parts B, C historically rewritten; summary updated |
| `valoria_overview_renaissance_audit.md` | 458 | Overview — 7 targeted str_replace corrections to novelistic passages + full rewrite of summary bullet block |
| `v2_audit_findings.md` | ~120 | Self-audit of v2 — 5-tier findings |
| `v2_n_checks.md` | ~130 | Per-proposal N-check (54 proposals) |
| `v2_branch_holistic_checks.md` | ~180 | 10 branches + system-level analysis |
| `v2_throughline_meta_checks.md` | ~230 | 15 throughlines + 5 meta-throughlines, full N + R/E/S |
| `valoria_master_analysis.md` | (this) | Compiled synthesis |

---

<!-- atom: valoria_master_analysis__03__section-3-v2-factual-audit-findings-5-tiers | section_index: 3 | source_section: "Section 3 — v2 factual audit findings (5 tiers)" -->


## Section 3 — v2 factual audit findings (5 tiers)

### Tier 1 — Factual errors requiring fix

**1. Zhang Lu Hanzhong dating wrong.** B.5: "Zhang Lu's Celestial Masters regime governed Hanzhong 184-215 CE." Zhang Lu established Hanzhong governance c. 191 CE (not 184 — that's Yellow Turban year, mental-merge error). **Correct: c. 191-215 CE.**

**2. Taiping Dao / Celestial Masters conflation (B.4).** B.4 attributes Zhang-Lu-specific governance apparatus (confession houses, communal grain stores, parish hierarchy) to Zhang Jue's Taiping Dao. Zhang Jue's Taiping Dao was revolutionary/millenarian movement that collapsed after 184 uprisings; the stable territorial-governance apparatus was Zhang Lu's Celestial Masters (correctly credited in B.5). **Fix: relabel B.4 "Taiping Dao RM-polity pathway" to "Zhang-Lu / Celestial-Masters RM-polity pathway."** Summary (Section 7 of v2) correctly distinguishes both movements as separate models.

**3. Tianming overclaim.** B.4 and B.11: "*Tianming* (Mandate of Heaven) was material-ritual, not mystical-moral." Overstates. Han-era *tianming* retained moral-cosmological dimensions (Dong Zhongshu's *Chunqiu fanlu*; emperor's moral conduct linked to natural order/omens). **Correct framing: "in legitimacy contests, *tianming* was operationalized through material-ritual infrastructure."**

**4. Ieyasu hostage dates wrong.** C.10 Ieyasu entry: "Hostage-youth at Imagawa 1547-60." Actually: **Oda 1547-49 (initial capture), Imagawa 1549-60.**

**5. Kenshin death framing.** C.10: "died 1578 (stroke or assassination)." Period sources overwhelmingly attribute to illness (likely stroke/cerebral hemorrhage). **Correct: "died 1578 (illness; speculative assassination theories exist but not in period sources)."**

**6. Sun Ce death imprecision.** C.10 (Sun Quan context) / B.10: "assassinated brother Sun Ce." Sun Ce was mortally wounded by assassins 200 CE; died from wound complications over subsequent weeks — not killed outright. **Correct: "died from wounds inflicted by assassins in 200 CE."**

### Tier 2 — Precision / sourcing issues

7. Zhuge-crossbow "attested" overclaims — should be "referenced" or "traditionally attributed."
8. Ishiyama Honganji "10-year siege" simplifies intermittent campaign over decade.
9. Sima Yi "resisted Shu northern expeditions 230s" — Cao Zhen commanded first three expeditions (228-230); Sima Yi commanded fourth and fifth (231, 234).
10. *Chushibiao* singular/plural — two memorials (227, 228); first accepted as Zhuge Liang's, second's authenticity debated.
11. Hōjō Sōun "minor retainer" — Ise Shinkurō background, established low-rank samurai lineage, not peasant-adjacent.
12. Saitō Dōsan single-generation rise — recent scholarship (Kuwata Tadachika) argues two-generation compression.
13. Hideyoshi "peasant-origin" — ashigaru-class origin also scholarly-argued; dispute unflagged.
14. Sun Quan "Two Palaces 241-250" — should be 242-250.

### Tier 3 — Framing / structural issues

15. NPC archetype templates (B.10, C.10) anchored to specific figures ("Cao Cao type," "Nobunaga type") — historically-sourced but figure-labeled rather than pattern-abstracted.
16. Confirmation-bias in TK/Sengoku convergence claim — I was looking for convergence.
17. N-check not formalized for Parts B and C (Part D has explicit N-checks; asymmetric).
18. Overview Maret+Vaynard = Xun-Yu analog imperfect — Xun-Yu's principled-opposition arc differs from Maret's dual-loyalty structure.
19. Preserved v1 error in Part A.5 — Venetian *Consiglio dei Dieci* described as "collective advisory/intelligence" — Dieci was specifically security/intelligence organ, not general advisory body. Out of v2 scope (Part A preserved).
20. Asymmetric material-trigger tagging — B.10 closes with tagging declaration, C.10 doesn't.

### Tier 4 — Minor residual issues

21. "Novelistic moral-flaw reading obscures structural driver" (B.4 re Lü Bu) — written as critique of absent-readers rather than positive claim.
22. Chibi fire-attack specifics — *Sanguozhi* account more compressed than phrasing implies.
23. Yellow Turban 184 labeling — shorthand OK but movement-planning began earlier.
24. "Warlord era 184-220" convention-dependent; also framed as 189-220 in some scholarship.
25. Okehazama framing — revisionist scholarship disputes terrain-narrowness; traditional framing unflagged.

### Tier 5 — Confirmed-correct items (sample)

26-37 (partial): Material-ritual legitimacy framing (despite tianming overclaim), gekokujō structural pattern, Fudai/tozama as Tokugawa formalization, Ōnin War 1467-77 → shugo → shugodai → sengoku daimyō devolution, Nagashino volley-fire revisionism, Ishiyama Honganji 1580 imperial-mediation surrender, Rikyū as embedded Hideyoshi household retainer, Matsunaga-Hiragumo Shigisan 1577, Akechi-Satomura Atago renga 1582, Xun-Yu-under-Cao-Cao as historical scholar-administrator pattern, Zhuge Liang's historical administrative record (Dujiangyan, Southern Man 225, Northern Expeditions 228-234), Tuntian / Nine-Rank Arbiter / Kenchi / Katanagari / class-fixing edict dating and attribution.

**Audit summary.** v2 is substantially historically-grounded at pattern level. Tier 1 items (#1-6) are factual errors requiring fix. Tier 2-3 are precision/framing issues. Tier 4 minor. Tier 5 confirms ~12+ major items correct.

---

<!-- atom: valoria_master_analysis__04__section-4-individual-mechanic-n-check-54-proposals | section_index: 4 | source_section: "Section 4 — Individual mechanic N-check (54 proposals)" -->


## Section 4 — Individual mechanic N-check (54 proposals)

Per-proposal attestation-as-load-bearing test applied to each v2 mechanical proposal across Parts B (TK: 28 proposals) and C (Sengoku: 26 proposals, with duplicates).

**Verdict distribution:**
- **Pass (decisive):** 20 — multi-instance attested, structurally central
- **Pass:** 20 — attested with adequate period-record support
- **Pass (qualified):** 13 — attested but single-instance or pattern-inferential
- **Fail:** 1 — **B.4 Taiping RM-polity pathway** (mislabel, matches Tier 1 finding #2)

**Pass-decisive concentration:** *Tuntian*, Multi-Season Siege, Memorial DA, Governor Devolution (*zhou mu*), Nine-Rank Arbiter, Cishi/Zhou-mu distinction, Great-House shizu unit, Household vs Ministry court tension, Xiaolian recommendation, Ashigaru Militia, Ie continuity + adoption, Gekokujō structural pattern, Shugo-devolution pathway, Four religious-institution types, Kenchi survey DA, Hollowed Crown state, Bifurcated legitimacy, Lifepath origin modifiers (Sengoku cluster).

**Qualified-pass cluster:** Single-event prototypes (Yantielun 81 BCE, Nagashino 1575 defensive-palisade, Akechi-Satomura renga 1582, Kobayakawa Sekigahara 1600 defection, Hideyoshi 1591 class-fixing edict, post-Sekigahara retrospective-legitimation), sustained-but-single-instance polities (Zhang Lu Hanzhong, Kaga Ikkō-ikki), archetype-template abstractions from named figures.

**Cross-lens convergence at pass-decisive tier:** siege-as-dominant-form (B.2 + C.2), administrative-innovation-as-asymmetric-advantage (*tuntian* + *kenchi* + class-fixing), central-to-hereditary-local devolution (*zhou mu* + shugo → daimyō), material-circumstance-over-moral-archetype NPC behavior. This cross-lens convergence at decisive tier provides the strongest warrant for implementation-priority.

---

<!-- atom: valoria_master_analysis__05__section-5-branch-level-analysis | section_index: 5 | source_section: "Section 5 — Branch-level analysis" -->


## Section 5 — Branch-level analysis

Ten functional branches emerge from aggregating related proposals across Parts A + B + C + D:

| Branch | Members | N | R | E | S | Status |
|---|---|---|---|---|---|---|
| B1. Written Political Communication | 10+ mechanics | Pass | Pass | **Qualified fail** | Qualified | Memorial/Publish functional overlap; Yantielun redundant |
| B2. Authority Devolution & Succession | 11+ mechanics | Pass (decisive) | Pass | **Fail** | **Fail** | Four parallel "faction-becomes-sovereign" pathways; Hollowed/Retrospective/Material-Legitimacy each duplicated |
| B3. Siege & Extended Military Campaign | 15+ mechanics | Pass (decisive) | Pass | Qualified fail | Pass | Multi-Season Siege duplicated TK+Sengoku; 3 parallel named-infrastructure types |
| B4. Economic & Financial | 14+ mechanics | Pass | Pass | Qualified fail | Qualified | Wealth overloaded; compound cascades (Bank+Mercenary+Plague) unordered |
| B5. Religious Institutions & RM-Polity | 13+ mechanics | Pass | Pass | Qualified fail | Pass | Two RM-polity models (Zhang Lu + Kaga) cover overlapping ground |
| B6. NPC Framework | 16+ mechanics | Pass | Pass | **Fail** | Qualified | 14 archetype templates + 11 new NPC categories — excessive |
| B7. Lifepath | 9+ modifiers | Pass | Pass | Qualified pass | Pass | Reorganization-not-reduction; load manageable as optional origin-tags |
| B8. Legitimacy & Ritual Infrastructure | 12+ mechanics | Pass | Pass | **Fail** | Pass | Heavy duplication with B2; merge recommended |
| B9. Investigation & Intelligence | 9+ extensions | Pass | Pass | Pass | Pass | Lowest-friction branch |
| B10. Plague Crisis | 8+ components | Pass | Pass (decisive) | Pass | Pass | Self-contained subsystem |

**Branch findings:**
- 4 branches pass cleanly (B7, B9, B10, and part of B4)
- 6 branches fail or qualified-fail on elegance from internal duplication or cluster-heaviness
- Most elegant-failing branches (B2, B6, B8) are candidates for unification, not rejection

**Consolidation targets identified per branch:**
1. Unified Authority Devolution Track (B2) — collapse 4 pathways to 1 with variants
2. Unified Textual Intervention (B1) — single DA with scale-parameter (petition/broadcast)
3. Unified Multi-Season Siege (B3 = B3 duplicate) — single mass-battle variant
4. Unified RM-Polity Pathway (B5) — single mechanic with historical-model parameter
5. 5-6 NPC archetype templates (B6) — collapse from 14 to cross-lens abstractions
6. Unified Financial Cascade (B4) — single Bank Failure + Bankruptcy cascade
7. Named Strategic Infrastructure category (B3) — Chokepoint + Tenshu + Port as typed
8. Sub-Faction Actor framework (B6) — Great House + Arbiter + Karō + Named Captain + Privateer + Chancery Secretary unified with role-parameter
9. Drop Yantielun venue, Renga distinct venue, Defensive-Palisade-Missile as named plan

**Aggregate inventory:** ~85-130 discrete mechanical additions proposed across Parts A+B+C+D, depending on bundling granularity. Consolidation targets reduce to ~60-70.

---

<!-- atom: valoria_master_analysis__06__section-6-holistic-system-level | section_index: 6 | source_section: "Section 6 — Holistic system-level" -->


## Section 6 — Holistic system-level

**Aggregate scope:** ~11 new tracks, ~4 new territory attributes, ~6 new unit types, ~11 new NPC categories, ~6 new POI/artifact types, ~18 new DAs, ~4 new venues, ~4 new states, ~14 new NPC archetype templates, ~9 new lifepath modifiers. Total: ~85-130 discrete additions.

**Valoria baseline:** Already substantial (Mandate, CI, Contest genres, TS/RS, Stability/Prosperity/Accord/Order, lifepath, combat matrices, Investigation, NPE, etc.).

**System-level R/E/S/N verdicts:**

| Dimension | Verdict | Reason |
|---|---|---|
| **N (system)** | Fail at current scope; Pass at consolidated (~60-70) scope | Branch analysis shows ~40-50% redundancy; individual N-passes do not aggregate |
| **R (system)** | Pass, with shallow-choice risk flagged | 18+ new DAs on top of existing action economy; variety achieved, meaningful-choice threatened |
| **E (system)** | **Fail** | ~120 additions against Valoria baseline violates "logically simple / no unnecessary overhead"; internal duplications (authority-devolution ×4, siege-campaign ×2, RM-polity ×2, etc.) directly fail elegance |
| **S (system)** | Qualified fail; pass at consolidated scope | Compound cascades (Bank + Mercenary + Plague + Peninsular Strain) unordered; Memorial/Publish/Named-Infrastructure-types disambiguation friction |

**Critical holistic finding:** Granular-pass auditing approved too much. The ~120 individually-passing mechanics contain ~40-50% redundancy at branch level. Elegance fails from sheer scope regardless of individual validity.

**Cascade ordering gap:** Compound cascade interaction (Bank Failure → Mercenary Defection → Plague → Financial → Peninsular Strain → Territorial Amalgamation) lacks explicit ordering and trigger-priority specification. Required before any implementation.

---

<!-- atom: valoria_master_analysis__09__section-9-required-fixes-to-v2-cross-lens-audit | section_index: 9 | source_section: "Section 9 — Required fixes to v2 cross-lens audit" -->


## Section 9 — Required fixes to v2 cross-lens audit

Actionable errors from Tier 1 audit findings, confirmed by N-check and consistent across analysis layers:

| # | Location | Fix required |
|---|---|---|
| 1 | B.4 "Taiping RM-polity pathway" | **Relabel to "Zhang-Lu / Celestial-Masters RM-polity pathway."** Move governance-apparatus claim from Taiping Dao to Celestial Masters where it historically belongs. Only N-fail. |
| 2 | B.5 "Hanzhong 184-215 CE" | **Correct to c. 191-215 CE.** |
| 3 | B.4 and B.11 "material-ritual, not mystical-moral" | **Reframe as "in legitimacy contests, operationalized through material-ritual infrastructure"** — retains core claim while allowing cosmological-moral dimension historically present. |
| 4 | C.10 Ieyasu entry "1547-60 at Imagawa" | **Split: Oda 1547-49, Imagawa 1549-60.** |
| 5 | C.10 Kenshin "stroke or assassination" | **Correct to "illness (likely stroke); speculative assassination theories exist but not in period sources."** |
| 6 | C.10 Sun Quan context "assassinated brother Sun Ce" | **Correct to "died from wounds inflicted by assassins 200 CE."** |

Tier 2-3 precision issues (Tier 2 findings #7-14, Tier 3 #15-20) are recommended-not-required corrections. See Section 3 for details.

---

<!-- atom: valoria_master_analysis__10__section-10-implementation-priority-throughline-der | section_index: 10 | source_section: "Section 10 — Implementation priority (throughline-derived)" -->


## Section 10 — Implementation priority (throughline-derived)

Throughline-coverage analysis shows 5 Tier-1 mechanics cover 8-11 of 15 throughlines; Tier 1+2 together cover all 15.

### Tier 1 — Multi-throughline high-leverage mechanics (5)

| Mechanic | Throughlines served |
|---|---|
| 1. **Authority Devolution Track unified** | T-α primary; T-η partial (religious-order devolution); T-ε partial (local fortification accumulation) |
| 2. **Material-Legitimacy three-component** (capital + archive + ritual-site) | T-γ primary; T-o partial (retrospective legitimation of infrastructure control) |
| 3. **NPC material-interest tagging + 5-6 unified archetypes** | T-ι primary; T-μ (principled-administrator as material-circumstance outcome); T-κ partial (ransom as material practice) |
| 4. **Multi-Season Siege Campaign** | T-ε primary; T-α partial (fortified-seat as devolution anchor); T-η partial (religious-polity siege-resistance) |
| 5. **Ie continuity + adoption mechanic** | T-θ primary; T-α partial (succession as devolution trigger); T-ι partial (succession-position as material-circumstance) |

### Tier 2 — Single-throughline load-bearing (5)

| Mechanic | Throughlines served |
|---|---|
| 6. Plague crisis system (D.5) | T-λ primary; T-η partial (crisis-triggered religious-polity emergence); T-δ partial (fiscal collapse from plague tax-base reduction) |
| 7. Banking + Credit + Usury (D.1) | T-δ primary |
| 8. Printing + Index + Burning (D.2) | T-ζ + T-ξ |
| 9. Textual Intervention DA (Memorial + Publication + Canonical Citation unified) | T-μ + T-β + T-ξ |
| 10. Religious-institution types (4 types, C.5) | T-η expansion |

**Tier 1+2 coverage: all 15 throughlines served.**

### Tier 3 — Extension mechanics

11. Condotta + Ransom unified (T-κ primary) — D.4 + A.8
12. Tea Ceremony + Meibutsu paired (T-ν primary) — C.3
13. Lifepath origin additions (T-ι + T-θ support) — B.9 + C.9
14. Named Strategic Infrastructure unified (T-ε extension) — Chokepoint + Tenshu + Port typed

### Tier 4 — Defer or drop

15. Retrospective Legitimation Victory epilogue (T-o only, end-game frequency)
16. Renga distinct venue (collapse into Tea Ceremony or Attunement Contest)
17. Yantielun Contest venue (redundant with Ministry Parliamentary disputes)
18. Defensive-Palisade-plus-Missile as named battle plan (sub-option, not named)
19. School-lineage lifepath flavor (no core-throughline service)

**Net scope after prioritization:** ~10 primary mechanics (Tier 1+2) + ~4 extension (Tier 3) = ~14 mechanics covering all 15 throughlines. From ~85-130 proposals → ~14 consolidated mechanical expressions.

---

## Provenance

Atom-by-atom inventory in source/section order:

| atom_id | source | section_index | source_section | lines |
|---|---|---|---|---|
| `valoria_master_analysis__00__preamble` | `valoria_master_analysis.md` | 0 | (preamble) | 7 |
| `valoria_master_analysis__01__section-1-task-and-corrections-made` | `valoria_master_analysis.md` | 1 | Section 1 — Task and corrections made | 12 |
| `valoria_master_analysis__02__section-2-deliverables-produced` | `valoria_master_analysis.md` | 2 | Section 2 — Deliverables produced | 14 |
| `valoria_master_analysis__03__section-3-v2-factual-audit-findings-5-tiers` | `valoria_master_analysis.md` | 3 | Section 3 — v2 factual audit findings (5 tiers) | 52 |
| `valoria_master_analysis__04__section-4-individual-mechanic-n-check-54-proposals` | `valoria_master_analysis.md` | 4 | Section 4 — Individual mechanic N-check (54 propos | 18 |
| `valoria_master_analysis__05__section-5-branch-level-analysis` | `valoria_master_analysis.md` | 5 | Section 5 — Branch-level analysis | 37 |
| `valoria_master_analysis__06__section-6-holistic-system-level` | `valoria_master_analysis.md` | 6 | Section 6 — Holistic system-level | 21 |
| `valoria_master_analysis__09__section-9-required-fixes-to-v2-cross-lens-audit` | `valoria_master_analysis.md` | 9 | Section 9 — Required fixes to v2 cross-lens audit | 17 |
| `valoria_master_analysis__10__section-10-implementation-priority-throughline-der` | `valoria_master_analysis.md` | 10 | Section 10 — Implementation priority (throughline- | 45 |
