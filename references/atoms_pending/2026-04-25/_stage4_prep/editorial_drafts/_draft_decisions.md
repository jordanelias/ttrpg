# Stage 4 — Draft Editorial Decisions

**Status:** DRAFT for Jordan review. NO commits made. Approve / reject / modify each block, then I execute.

**Method:** Maximum editorial judgment within constraints. Setting/character/narrative substance preserved as `[PROPOSED:]` for explicit Jordan approval — these are pure editorial calls. Process/structural/derivable decisions made directly with reasoning shown.

---

## Decision 1 — Solmund (Topic 02) per-PART recommendations

Solmund decomposes into 8 PARTs + 2 appendices. Each has a different ingestion path based on its nature.

| PART | header | nature | metrics | draft decision |
|---|---|---|---|---|
| 1 | VOICE AND REGISTER | setting-anchored (multiple canon entities — verify against canon/03 + designs/world/) | chars=9896, paths=0, mech=6, P-refs=0 | **INGEST-WITH-CANON-CROSSCHECK** |
| 2 | KABBALISTIC LITERARY TRADITIONS | canon-anchored (P-constraint references present — verify against canon/02) | chars=4354, paths=0, mech=2, P-refs=1 | **INGEST-WITH-CONSTRAINT-VERIFICATION** |
| 3 | PHILOSOPHICAL FRAMEWORKS | canon-anchored (P-constraint references present — verify against canon/02) | chars=4281, paths=0, mech=0, P-refs=1 | **INGEST-WITH-CONSTRAINT-VERIFICATION** |
| 4 | SOLMUND'S NATURE AND THE TWO WITNESS TRADITIONS | canon-anchored (P-constraint references present — verify against canon/02) | chars=8088, paths=1, mech=7, P-refs=1 | **INGEST-WITH-CONSTRAINT-VERIFICATION** |
| 5 | ARTIFACT TAXONOMY | setting-anchored (multiple canon entities — verify against canon/03 + designs/world/) | chars=3068, paths=0, mech=2, P-refs=0 | **INGEST-WITH-CANON-CROSSCHECK** |
| 6 | VOCABULARY AND WRITING PATTERNS | setting-anchored (multiple canon entities — verify against canon/03 + designs/world/) | chars=3313, paths=0, mech=1, P-refs=0 | **INGEST-WITH-CANON-CROSSCHECK** |
| 7 | SOUTHERNMOST ENGAGEMENT DESIGN | system-touching (mechanical specs present) | chars=12109, paths=0, mech=54, P-refs=0 | **SPLIT-FROM-SOLMUND-INTO-DESIGN** |
| 8 | THROUGHLINES AND IMPLEMENTATION | system-touching (mechanical specs present) | chars=10644, paths=0, mech=19, P-refs=2 | **SPLIT-FROM-SOLMUND-INTO-DESIGN** |

### Per-PART reasoning

**PART 1 — VOICE AND REGISTER** → `INGEST-WITH-CANON-CROSSCHECK`
- References canon entities; verify per-claim against canon/03_canonical_timeline.md and designs/world/. P-constraint refs found: (none).

**PART 2 — KABBALISTIC LITERARY TRADITIONS** → `INGEST-WITH-CONSTRAINT-VERIFICATION`
- References P-['P-07'] — verify each constraint reference against canon/02_canon_constraints.md.

**PART 3 — PHILOSOPHICAL FRAMEWORKS** → `INGEST-WITH-CONSTRAINT-VERIFICATION`
- References P-['P-08'] — verify each constraint reference against canon/02_canon_constraints.md.

**PART 4 — SOLMUND'S NATURE AND THE TWO WITNESS TRADITIONS** → `INGEST-WITH-CONSTRAINT-VERIFICATION`
- References P-['P-08'] — verify each constraint reference against canon/02_canon_constraints.md.

**PART 5 — ARTIFACT TAXONOMY** → `INGEST-WITH-CANON-CROSSCHECK`
- References canon entities; verify per-claim against canon/03_canonical_timeline.md and designs/world/. P-constraint refs found: (none).

**PART 6 — VOCABULARY AND WRITING PATTERNS** → `INGEST-WITH-CANON-CROSSCHECK`
- References canon entities; verify per-claim against canon/03_canonical_timeline.md and designs/world/. P-constraint refs found: (none).

**PART 7 — SOUTHERNMOST ENGAGEMENT DESIGN** → `SPLIT-FROM-SOLMUND-INTO-DESIGN`
- Mechanical specs (RWCE, SA Increment, etc.) — these belong in designs/scene/ or designs/provincial/, not designs/world/. Recommend extracting to a separate design-track ingestion that goes through Stage 4 mechanical-promotion path, NOT through Solmund editorial path.

**PART 8 — THROUGHLINES AND IMPLEMENTATION** → `SPLIT-FROM-SOLMUND-INTO-DESIGN`
- Mechanical specs (RWCE, SA Increment, etc.) — these belong in designs/scene/ or designs/provincial/, not designs/world/. Recommend extracting to a separate design-track ingestion that goes through Stage 4 mechanical-promotion path, NOT through Solmund editorial path.

### Solmund overall recommendation

Solmund is **not a single editorial deliverable** — it is a multi-track consolidation that should be split before ingestion:

- **Voice/Style track** (PARTs 1, 2, 6) → ingest provisional into `designs/world/solmund_voice_v30.md` (new file). Pure editorial; no canon conflict to verify.
- **Philosophical/Theological track** (PARTs 3) → ingest into `designs/world/solmund_philosophy_v30.md` (new file). Editorial substance, but cross-check Augustine/Wittgenstein/Kierkegaard treatment doesn't contradict canon/00_philosophical_foundations.md.
- **Solmund Nature + Witness Traditions track** (PART 4) → ingest into `designs/world/solmund_v30.md` (new file). High canon-anchoring; verify against canon/03_canonical_timeline.md and existing designs/world/southernmost_v30.md.
- **Artifact Taxonomy track** (PART 5) → ingest into `designs/world/solmund_artifacts_v30.md` (new file). Setting work; verify entity names against canon.
- **Southernmost Engagement / RWCE track** (PART 7) → **DO NOT route through Solmund editorial.** This is mechanical (RWCE mechanism, SA increment, faction action gating). Extract to `designs/scene/rwce_mechanism_v30.md` and route through standard mechanical-promotion path. Subject to PP / ED registration.
- **Throughlines track** (PART 8) → integrate into `references/throughlines_meta_infill.md` table with M-parent assignments. Already throughline territory.
- **Appendices** → resolved findings inform existing canon entries; open items become new ED entries.

Splitting Solmund prevents a single 32-atom editorial review from spanning voice/setting/mechanical concerns. Each track has its own canonical destination and its own gate.

---

## Decision 2 — Topic 06 sub-decomposition (refined)

Original sub-decomposition produced 21 sub-topics (some with 1-3 atoms). Refined to 13 sub-topics by merging adjacent under-5-atom numeric subs and grouping Roman appendix sections.

| sub-topic | atoms | covers |
|---|---|---|
| `06_audit_meta` | 7 | II.2 Open Decisions Requiring Jordan (16 / II.5 Rating Corrections Applied / II.6 Mechanics Flagged for Removal |
| `06_claims_meta` | 4 | V.3 Derived Stats (GAP-07) / V.4 Caste / Social Structure / V.5 Royal Assassination Fuse |
| `06_num_1+3` | 14 | (preamble) / 1.1 Die Face Rule (d10) / 1.3 Obstacle Scale |
| `06_num_10+11+12` | 5 | 10.3 Zoom In / Zoom Out / 11.2 Hybrid Phase Structure / 12.2 CI (Church Influence) |
| `06_num_13+14` | 10 | 13.1 Universal Victory — Peninsular Sove / 13.2 Faction Toolkits (NOT Alternate End / 13.3 Co-Victory (6 Pairings) |
| `06_num_15` | 5 | 15.1 Unit Representation / 15.2 Muster / 15.3 TC Competitive Formula |
| `06_num_16` | 8 | 16.2 Named NPC Profiles (12 core) / 16.3 Decision Procedure / 16.3 Mending Community |
| `06_num_20` | 2 | 20.1 Formula Consistency / 20.2 The Complete Pipeline |
| `06_num_4` | 5 | 4.1 Adjudicator → Pool Rotation / 4.2 Styles (2×2) / 4.3 Interaction Types |
| `06_num_5` | 7 | 5.2 Three-Axis Ob / 5.3 Operations / 5.4 Opposing Operations (PP-653) |
| `06_num_6` | 5 | 6.2 Fieldwork Pool and Attribute Rotatio / 6.3 Evidence Track / 6.4 Socializing / Disposition |
| `06_num_7+8` | 5 | 7.1 Core Formula (PP-233) / 7.3 Key Mechanics / 7.4 PROVISIONAL Count |
| `06_num_9` | 6 | 9.1 Card-Hand Economy / 9.2 Action Ob Formulas / 9.4 Faction Starting Stats |

**Refinement rules applied:**
- Numeric sub-topics with <5 atoms merged with the next-numbered adjacent sub-topic (e.g., `06_num_10+11+12` if 10/11/12 each have <5).
- Roman-numeral PARTs II/III/IV (audit meta-content) grouped as `06_audit_meta`.
- PART V (claims meta) standalone as `06_claims_meta`.
- Misc atoms (preamble, etc.) folded into the largest numeric bucket.

---

## Decision 3 — ED-543 disposition

**Decision: REGISTER**

```yaml
id: ED-543
date: '2026-04-25'
description: '[PROPOSED: Clock registry update — full refresh from peninsular_strain_v30 and tc_political_redesign_v30. Sourced from valoria_master_consolidation
  atom (2026-04-21/22 audit synthesis); no other canon mention found.]'
status: open
severity: P1
source: 'atom: valoria_master_consolidation__20__from-holistic-audit-valoria-holistic-audit-md'
rationale_for_register: Atom context unambiguously describes a P1 editorial decision (clock registry refresh from two named designs). No mention
  in canon registers, but content is substantive enough to register rather than strike. Single-atom evidence is weak — verify intent before [editorial]
  commit. If the work was already done in a different ED, mark as superseded.
verify_before_commit:
- Did the clock registry refresh actually happen in another ED entry (ED-538..ED-545 range, or designs/audit/)?
- If not, is this still pending work or already integrated?
```

---

## Decision 4 — Missing paths resolution

### `designs/architecture/derived_stats_v30.md` → **RENAME-IN-ATOMS**

- **reasoning:** Filename match at score 10 with `designs/scene/derived_stats_v30.md` (existing). Path drift, not orphan. Update atom-level references via [infrastructure] commit. Affects topics 03, 06, 08, 09.
- **replacement:** `designs/scene/derived_stats_v30.md`

### `designs/architecture/core_experiential_moments.md` → **STRIKE-REFERENCES**

- **reasoning:** No rename candidate found in repo. Likely a proposal-stage doc that was never written, or referenced speculatively. Striking atom references is safer than creating an empty placeholder. If the doc is needed later, it can be written then.

### `references/censured_vocabulary.yaml` → **CREATE-PLACEHOLDER**

- **reasoning:** PP-675 / ED-783 (canon rectification) directly references censured_vocabulary as the authoritative term-governance store. The rectification work landed but the vocabulary file did not. This is a real gap. Create as a minimal placeholder yaml with a stub structure, then expand as Stage 4 promotes specific terms.
- **replacement:** `create new file with stub structure`

---

## Decision 5 — Promotion drafts refined

All 62 drafts auto-refined where derivable:
- **Severity:** derived from highest-priority bucket among evidence atoms (P1 atom → P1 severity).
- **Affects (PP):** derived from `canon_mentions` filtered to `designs/`.
- **Parent_meta (T/M):** derived from existing throughlines_meta_infill table row when found.
- **Description:** stripped leading markdown markers, trimmed to coherent sentence ending.

**Items still flagged for Jordan attention** in each refined draft:
- `finding_id` for PP entries — requires Jordan tie to specific simulation/audit finding
- `parent_meta` for T/M without existing canon row
- Final description wording (auto-extraction is approximate)
- Severity-override if my priority-bucket inference is wrong

Per-topic refined drafts at `editorial_drafts/refined_promotion_drafts/<topic_id>_promotion_drafts.yaml`.

| topic | drafts | P1 | P2 | P3 |
|---|---|---|---|---|
| `01_throughlines_meta` | 2 | 1 | 1 | 0 |
| `03_threadwork_design` | 19 | 0 | 16 | 3 |
| `04_faction_balance_three_modes` | 3 | 2 | 1 | 0 |
| `06_mechanical_review_audit` | 27 | 0 | 14 | 12 |
| `08_session_consolidation` | 7 | 0 | 6 | 1 |
| `09_canon_rectification_pp675_ed783` | 2 | 1 | 1 | 0 |
| `10_session_log_index` | 2 | 2 | 0 | 0 |

---

## Decision 6 — Topic 07 disposition

**Decision: FOLD-INTO-08**

- **reasoning:** Only 2 residual atoms remain after throughlines (01) and threadwork (03) absorbed most of master_consolidation.md. Both topics share the consolidation/synthesis role with topic 08. Folding keeps related residuals together; preserving 07 standalone yields a 2-atom audit unit with no leverage.
- **atoms to migrate:** 2 (from `07_audit_s1_s7_synthesis` to `08_session_consolidation`)

---

## Decision 7 — Stage 5 archive strategy

**Decision: OPTION-C: front-matter status updates + retain folder**

- **reasoning:** Provenance trail is genuinely useful. Stages 2-4 created real value by reasoning about these atoms; that reasoning must be reproducible. Option A (move to atom_archive/) loses the analytical artifacts (priority queue, audit reports, reviews, prep package). Option B (delete) loses everything. Option C preserves the full chain and signals consolidation completion via per-atom status field.
- **implementation:** Per-atom front-matter update: add status: consolidated | skipped | rejected with target commit OID. Single [infrastructure] commit applying status updates to all 316 atoms.

---

## Summary of decisions

| # | decision | type |
|---|---|---|
| 1 | Solmund split into 7 ingestion tracks (voice/style, philosophy, nature, artifacts, RWCE-mech, throughlines, appendices) | structural + per-track per-PART |
| 2 | Topic 06 sub-decomposition refined from 21 → 13 sub-topics | structural |
| 3 | ED-543: REGISTER (P1, status=open, single-atom evidence) | editorial |
| 4 | Paths: 1 RENAME / 1 STRIKE / 1 CREATE-PLACEHOLDER | structural |
| 5 | 62 promotion drafts refined; severity/affects/parent_meta derived where possible | structural |
| 6 | Topic 07: FOLD into 08 | structural |
| 7 | Stage 5: OPTION C (front-matter status updates) | structural |

## What still requires explicit Jordan input

After approving this draft, three categories of editorial calls remain that I cannot make on your behalf:

1. **Solmund substantive content** — within each track, do the specific claims (5 voice registers, 6 Kabbalistic sources, etc.) survive as canonical, or do you want changes? I have no basis to call this.
2. **Promotion draft `finding_id` fields (PP)** — each PP needs its underlying simulation/audit finding identifier. Atom contexts don't reliably contain these.
3. **ED-543 verification** — confirm my register decision (vs. strike) by checking whether the clock registry refresh actually happened in another ED I missed.

Everything else in this draft I will execute on approval.
