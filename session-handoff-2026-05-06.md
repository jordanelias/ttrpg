# Session Handoff — 2026-05-06 Prose Skill Audit & Lit Review

## Session summary

Five commits to `jordanelias/ttrpg`: `05a3579`, `3f5563a`, `6ce2926`, `7d70fac`, `2a9a1fd`. First three are clean (Spirit axis, test battery part 4, Tartt/Beckett distillation). Last two (`7d70fac` lit review, `2a9a1fd` reconciliation) contain unverified scholarly citations and should be treated as provisional.

## Critical findings requiring action

### 1. Citation verification failures (highest priority)

Spot-checked 5 citations from the lit review committed in `7d70fac`. Results:

- **Tara K. Menon, "The 'Beauty Is Terror' Equation in Donna Tartt's *The Secret History*" (in *The Henry James Review*)** — FABRICATED. Menon is a real Harvard scholar but works on 19th-century British novel. No Tartt essay exists. Described in the lit review as "the most-cited academic essay on Tartt." Must be removed entirely; Tartt section must be rewritten honestly.
- **Sandra Beedham, *The Novels of Kazuo Ishiguro* (Palgrave Macmillan, 2009)** — WRONG NAME AND YEAR. Author is **Matthew Beedham**, published **2010**. Book exists and is a Reader's Guide to Essential Criticism. Substantive claims attributed to Beedham may be accurate but are unconfirmed.
- **Walkowitz, *Cosmopolitan Style* (2006)** — BOOK EXISTS but specific argument misattributed. Walkowitz's actual Ishiguro concept is "treason" (cosmopolitan critique of national identification). The Gricean quantity-violation framework I attributed to her appears to be my analytical synthesis, not her specific argument. Needs reframing: either verify she does use Gricean framework, or reattribute the quantity-violation reading as synthesis-internal.
- **Turner, *Translating Tolkien* (Peter Lang, 2005)** — BOOK EXISTS. Primarily a translation-studies work. Whether parataxis-as-marked-register is Turner's central argument or a tangential observation is unconfirmed. Prominence may be overstated.
- **Klingenberg, *Fantasies of the Feminine* (Bucknell, 1999)** — VERIFIED CLEAN. Correct author (Patricia Nisbet Klingenberg), publisher, year, subject.

Extrapolating from 5 checks: ~20-40% of the 60+ bibliography entries may have errors of varying severity. The entire lit review's citation apparatus is epistemically suspect.

### 2. Downstream contamination

Commit `2a9a1fd` (reconciliation) replaced known-bad citations (Perez, Encyclopedia.com, Heschel/JWA) with names from the unverified lit review (Klingenberg-Mancini, Nunes). Klingenberg checked out; Nunes has not been verified. The reconciliation may have traded visible-bad citations for invisible-bad citations.

Files affected: SKILL.md, anti-patterns-skeleton.md, anti-patterns-infill.md, techniques-skeleton.md, techniques-infill.md, calibration-skeleton.md, calibration-infill.md, test-battery-part1.md.

### 3. Anti-patterns structural problem

Jordan flagged: "I am suspicious that anti-patterns is an incoherent assemblage of granular rules rather than structured sets of complementary roles." Confirmed by audit. 62 numbered rules accumulated by session-addition with no organizing structure, substantial redundancy, and categorically different rule types mixed under sequential numbering.

Proposed restructuring into 6 categories:

**I. Prose Quality (always-on)** ~8 rules from current ~25. Consolidates forbidden-language lists, sentence architecture, specificity, over-explanation cluster, content leakage, meta-commentary, repetition discipline, Master Rule.

**II. X-Axis Deployment (coherence-tier checks)** ~4 rules from current ~8. Tier-author alignment, content-rendering distinction, capacity ceiling, recalibration frame.

**III. Y-Axis Deployment (substrate/TS checks)** ~2 rules. Within-observation gradient, subject/object lamination.

**IV. Z-Axis Deployment (Spirit checks)** ~2 rules. Spirit distinction, over-explained absence.

**V. Author Deployment** 12 sub-rules (one per roster author). Mannerism risk + misuse risk for each. Currently missing: Beckett, Lem, McCarthy, Le Carré.

**VI. Focalization** ~3 rules. Unanchored editorial, mode conflation, NPC dimensionality.

**Moved to infill:** #62 (critical-tradition flattening — interpretive caution, not pattern-matchable). #28 (absorbed into V.6 Borges mannerism). #47 (absorbed into infill as deployment-context reference).

### 4. Architectural clarification established in this session

The X/Y/Z architecture was clarified through conversation:

- **X (Coherence)** = interiority's position on the human-legibility continuum
- **Y (Thread Sensitivity)** = exteriority's position on the same continuum
- **Z (Spirit)** = whether the character finds equilibrium outside human rationality (high) or collapses (low)

Same metric (legibility) at two loci (interiority, exteriority). Spirit orthogonal.

Four quadrants:
- Q1 (high X, low Y): realist territory. Tolkien/Mistry/Tartt/Ishiguro/Márquez/Le Carré dominant.
- Q2 (high X, high Y): scholar-confronting-substrate. Lem/Borges/Márquez/Tolkien dominant.
- Q3 (low X, low Y): interior recalibration in legible world. Lispector/Beckett/Ocampo/Ishiguro dominant.
- Q4 (low X, high Y): full irreal. Lispector/Ocampo/Beckett dominant.

Z modifies Q3/Q4: high Spirit → Beckett up, Lispector active-engagement; low Spirit → Lispector dissolution, Beckett near-zero.

The skill files still encode pre-clarification single-column weights. Need rebuilding as 2D grid (X bands × Y bands) with coarse bands, not percentages.

### 5. Roster changes established

- **Beckett and Lem** confirmed as roster authors (10 total from 8). Need: calibration anchors, weighting in 2D grid, mannerism rules, lit-review sections (web-verified).
- **McCarthy** approved as 11th author for combat/violence prose. Need: full integration (calibration anchor, lit-review section web-verified, mannerism rule, weighting).
- **Le Carré** approved as 12th author for institutional-political/tradecraft prose. Need: same.
- **Borges** narrowed to Q1-Q2 only. Was carrying Q3-Q4 weight he shouldn't have (prose-recursion at low X is Lispector paradox-recursion / Beckett dialectical succession, not Borges content-level recursion).
- **Wodehouse and Sedaris** rejected. No comedy needed in the game experience.

### 6. Throughlines identified

Six throughlines running through the skill:
1. Enactment over statement (the deepest principle)
2. Focalization anchors everything
3. The legibility continuum at two loci (X/Y architecture)
4. Specificity as the reality-effect operation
5. Recalibration not dysfunction
6. Author deployment is coordinate-dependent

Six meta-throughlines about the skill's structural problems:
A. Detail without architecture (granularity increased, structure didn't)
B. Scholarly apparatus epistemically suspect throughout
C. Self-auditing has diminishing returns (need external verification)
D. False precision masks uncertainty (percentages, scores, numbered rules)
E. Architecture evolved through correction, not design (files reflect accumulated layers)
F. Technique-extraction conflated with critical-anchoring (these should be separated)

## Next session task order

Architecture first, content second.

### Phase 1: Architecture (do first)

1. **Rebuild anti-patterns** from the 6-category structure. Consolidate 62 → ~25. Map each rule to the X/Y/Z coordinate(s) where it applies. Add missing author-deployment rules (Beckett, Lem, McCarthy, Le Carré).

2. **Separate technique-extraction from critical-anchoring** in all skill files. Technique-extractions (what each author's prose does — based on primary works) stand as synthesis-internal readings. Critical-anchoring (what scholars argue) gets [UNVERIFIED] tags and moves to infill. Skeleton files should not be load-bearing on any specific scholarly citation.

3. **Rebuild weighting tables** as 2D grid (X bands × Y bands) with coarse bands (primary / strong / moderate / minimal / absent). Four-corner quadrant structure. Z modifier notes. No percentages until calibration data exists from generated test passages.

### Phase 2: Citation cleanup (do second)

4. **Fix Menon fabrication** in lit review. Remove the fabricated essay. Rewrite Tartt section honestly: Tartt has the thinnest academic apparatus of the roster authors; the technique-extractions are synthesis-internal readings of the primary texts; the critical anchoring comes from reviews (Mendelsohn, Hargreaves, Wood) not monographs.

5. **Fix Beedham** (Matthew, 2010) in lit review and techniques-infill.

6. **Fix Walkowitz** framing. Either web-verify she uses Gricean terminology specifically, or reframe as: "The synthesis reads Ishiguro's unreliability as built through quantity-violation (long sentences containing little information). Walkowitz's *Cosmopolitan Style* (2006) treats Ishiguro's unreliability within a cosmopolitan-critique frame; the synthesis draws on her broader reading while the specific quantity-violation mechanism is synthesis-internal."

7. **Web-verify remaining high-stakes citations.** Priority order: Sarlo 12-word quote, Moser "veers toward abstraction" quote, Borges scholars (Sarlo, Molloy, Aizenberg, Alazraki, Balderston), Márquez scholars (Vargas Llosa, Williamson, Fiddian, Faris), Mistry scholars (Bharucha, Morey, Malak).

### Phase 3: Content integration (do third)

8. **Integrate McCarthy and Le Carré** as roster authors. Calibration anchors (McCarthy: passage from *Blood Meridian*; Le Carré: passage from *Tinker Tailor*). Lit-review sections web-verified during composition. Mannerism rules (V.10, V.11). 2D grid weighting entries.

9. **Integrate Beckett and Lem** fully. Calibration anchors (Beckett: passage from *Worstward Ho* or *The Unnamable*; Lem: passage from *Solaris*). Lit-review sections web-verified. Restore appropriate scholarly citations after web verification. 2D grid weighting entries.

10. **Propagate Borges narrowing.** Update coherence-tiers.md, techniques-skeleton.md, calibration-skeleton.md to reflect Q1-Q2-only deployment. Reattribute Q3-Q4 prose-recursion to Lispector paradox-recursion and Beckett dialectical succession.

### Phase 4: Verification (do throughout)

11. **Every new citation must be web-searched before committing.** No exceptions. Training-data citations are not reliable. A `prose_skill_lint` hook checking for [UNVERIFIED] tags on citations would enforce this going forward.

## Decision points for Jordan

- **12 authors confirmed?** Tolkien, Mistry, Tartt, Ishiguro, Márquez, Borges, Ocampo, Lispector, Lem, Beckett, McCarthy, Le Carré. Yes/no before integration work begins.
- **Anti-patterns 6-category structure approved?** The consolidation from 62 → ~25 is a substantial restructure. Confirm the six categories (Prose Quality, X-Axis, Y-Axis, Z-Axis, Author Deployment, Focalization) before implementation.
- **2D grid format approved?** Quadrant-based weighting with coarse bands replaces single-column percentage tables. Confirm before rebuilding.
- **Epistemic downgrade of lit review:** should the document be (a) reframed at the top as "synthesis-internal commentary with unverified scholarly references," (b) corrected citation-by-citation via web search, or (c) both?

## Files in current state

### Clean (commits 1-3):
- skills/prose-writer/references/test-battery-part4.md
- skills/prose-writer/references/coherence-tiers.md (also touched by Jordan's a1a65694 commit)

### Provisional (commits 4-5, contain unverified citations):
- skills/prose-writer/references/literary-review-deep.md — contains fabricated Menon essay, wrong Beedham name/year, likely misattributed Walkowitz argument, 55+ unchecked bibliography entries
- skills/prose-writer/SKILL.md — reconciliation edits clean (Grice→Walkowitz reframing, Short→Short-on-Márquez); underlying Walkowitz attribution unverified
- skills/prose-writer/references/anti-patterns-skeleton.md — #62 sub-items reference unverified scholars; structural problem (incoherent assemblage) identified
- skills/prose-writer/references/anti-patterns-infill.md — parataxis fix clean; other content pre-existing
- skills/prose-writer/references/techniques-skeleton.md — reconciliation edits; Beedham wrong name
- skills/prose-writer/references/techniques-infill.md — Nunes, Klingenberg-Mancini substitutions; Nunes unverified
- skills/prose-writer/references/calibration-skeleton.md — pairing markers added (anchored/synthesis distinction); content sound
- skills/prose-writer/references/calibration-infill.md — six→eight fix clean; Turner citation fixed; Sarlo quote unverified
- skills/prose-writer/references/test-battery-part1.md — Gricean→Walkowitz fix; underlying Walkowitz attribution unverified

### Untouched this session:
- skills/prose-writer/references/calibration-infill.md (pre-existing content)
- skills/prose-writer/references/techniques-infill.md (pre-existing content beyond this session's edits)
- skills/prose-writer/references/composition-test-definitive.md
- skills/prose-writer/references/rendstad-arc.md, rendstad-audit.md, rendstad-scenes-6-7.md
- skills/prose-writer/references/coherence-ts-canonical-audit.md
- skills/prose-writer/references/test-battery-part1.md, part2.md, part3.md (pre-existing content)
