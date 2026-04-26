# Canon Rectification PP-675 / ED-783 (consolidated)

## Consolidation front matter

- **topic_id:** `09_canon_rectification_pp675_ed783`
- **atom_count:** 18
- **scope:** valoria_session_2026_04_25_master_consolidation.md + cross-source PP-675 atoms. Censured-vocabulary / term-governance work.
- **source distribution:**
  - `valoria_session_2026_04_25_master_consolidation.md`: 15 atoms
  - `valoria_session_master_2026-04-25.md`: 2 atoms
  - `VALORIA_SESSION_2026-04-25_MASTER.md`: 1 atoms
- **drift surface:** cross-source
- **post-audit canon target:** `canon/patch_register_active.yaml (verify), canon/editorial_ledger.yaml (verify), references/propagation_map.md`
- **status:** assembled (pending audit Stage 3)
- **assembled_from_commit:** atoms committed at `83c37da7001defdf3bb3425b17dda3f934d262d3`

## Audit checklist (Stage 3 input)

- [ ] PP-675 final spec matches whatever landed in canon/patch_register_active.yaml.
- [ ] ED-783 statement matches canon/editorial_ledger.yaml.
- [ ] Outstanding Work (§10) cross-checked against current next_action queue.
- [ ] Censured Vocabulary list (§2) is the authoritative one.

## Known drift dimensions

- PP-675 description across 3 sources may use different framings.
- ED-783 framing (term governance vs vocabulary censuring vs canon rectification) — pick one.

## Cross-source drift table

Rows = canonical IDs. Columns = source documents. Cells list atom IDs in this topic that reference the row's canonical ID. Empty cell = source does not reference that ID. Multiple atom IDs in a cell = potential per-source drift to verify during audit.

| id | VALORIA_SESSION_2026-04- | v_session_2026_04_25_m_c | v_session_m_2026-04-25 |
|---|---|---|---|
| **ED-667** | — | — | context-window-3-e, status |
| **ED-710** | section-9-open-ite | — | — |
| **ED-711** | section-9-open-ite | — | — |
| **ED-717** | — | — | context-window-3-e, status |
| **ED-768** | section-9-open-ite | — | — |
| **ED-779** | section-9-open-ite | — | — |
| **ED-783** | section-9-open-ite | preamble, 1-scope, 9-verification-sta, 10-outstanding-wor, 14-references | — |
| **PP-675** | section-9-open-ite | preamble, 9-verification-sta, 14-references | context-window-3-e, status |

## Content

Atoms grouped by source. Within each source, ordered by section_index. Read across sources to identify drift.

### From `VALORIA_SESSION_2026-04-25_MASTER.md` (1 atoms)

<!-- atom: valoria_session_2026-04-25_master__09__section-9-open-items-at-session-close | section_index: 9 | source_section: "Section 9 — Open Items at Session Close" -->


## Section 9 — Open Items at Session Close

### Final open EDs (4)

| ED | Description | Status |
|---|---|---|
| ED-710 | Settlement adjacency graph | Workplan-scale, deferred |
| ED-711 | Fractional province ownership | Workplan-scale, deferred |
| ED-768 | 13 orphaned PROVISIONAL markers | Jordan-blocked review |
| TC→CI bulk propagation | ~675 residual TC references in active spec | Queued cleanup |

### Tests not run

21, 23, 25, 32, 37, 61, 62, 64, 65.

### Belief mechanic propagation

Canonical Belief content still resides in `deprecated/valoria_ttrpg_complete §10.2`. ED-779 (Inspiration) §5.3.4 includes a TODO note flagging this for separate future propagation.

### True blockers

- D-4 Altonian invasion timeline revision (separate workplan per session log).
- D-5 Einhir site-network three-layer model (separate workplan).
- SIM-NPC-01 + sim-validation queue: requires `engine_v4`.
- TC residuals (~675 outside top-5 files).
- CP/TD ~149 disambig per-context.

### Out-of-session commits observed

Two commits appearing on the same date but not produced by this conversation:
- `b14f067` — `[editorial] §16 rewrite (Drift From Human-Mode Being) + censure rectification across foundations, rules, canon/01 cross-refs, canon/02 P-02/P-06/P-10/P-12 — PP-675 / ED-783`
- `aae1e72` — `[editorial] §16.1 close — operational origin of Coherence loss (alignment vs opposition to substrate tendency) — PP-675 / ED-783`

These are flagged for awareness; they were not part of this session's audit/stress-test workstream.

---

### From `valoria_session_2026_04_25_master_consolidation.md` (15 atoms)

<!-- atom: valoria_session_2026_04_25_master_consolidation__00__preamble | section_index: 0 | source_section: "(preamble)" -->


# Valoria Canon Rectification — Master Consolidation

**Session date:** 2026-04-25
**Patch proposal:** PP-675
**Editorial ledger:** ED-783
**Commits:**
- `b14f0671ae9c7e7bb578865f92745dbcaab64bf0` — primary 4-file rectification
- `aae1e72413f9417f46a6d2fd8cb25646bd9ee6aa` — follow-up §16.1 close (operational origin of Coherence loss)

---

<!-- atom: valoria_session_2026_04_25_master_consolidation__01__1-scope | section_index: 1 | source_section: "1. Scope" -->


## 1. Scope

This work consolidates a single coherent batch:

1. Surface and surface-classify all instances of censured terminology in `canon/`.
2. Rewrite `canon/00_philosophical_foundations.md` to remove censured terminology and execute Jordan's directives on P-02 (Lacanian Real grounding for monstrosity), P-10 (Coherence-as-commensurability), P-12 (drift propagation), philosophical foundations as a closed prose document (no external mechanics references; no non-rhetorical questions).
3. Audit the rewrite for logical consistency against existing canon (canon/01 self-rendering amendment, canon/02 leap mechanism amendment) and against Jordan's articulated philosophical content on Coherence (apperception, intersubjective judgment, etymology, equilibrium-tendency, substrate-and-possibility duality, tridimensional simultaneity).
4. Fully revise §16 to absorb the canon/01 / leap-mechanism amendments' philosophical content into foundations, so foundations grounds the amendments rather than being thinner than them.
5. Propagate the §16 rewrite through dependent docs: rules A11/C4, canon/01 cross-references, canon/02 P-02/P-06/P-10/P-12.
6. Verify all canon clean of censured terms post-commit.

**What this work does not cover** (deferred — see §10):
- Term-governance enforcement infrastructure (project-instructions block, registry, read-time injection, safe_commit gate, CI workflow).
- Design-tier sweep of `designs/` for censured terminology.
- Conviction Track rename.
- Certainty → Religious Conviction rename.
- Cross-system terminology boundary enforcement (mass battle / combat / social contest / faction actions / fieldwork must not share terminology with metaphysics / ontology / threadwork / beliefs / personalities / inspirations / duties).
- Editorial ledger regeneration to record ED-783.

---

<!-- atom: valoria_session_2026_04_25_master_consolidation__02__2-censured-vocabulary | section_index: 2 | source_section: "2. Censured Vocabulary" -->


## 2. Censured Vocabulary

Three terms identified for permanent censure:

| Term | Status | Replacement framework |
|---|---|---|
| `taint` (and variants: tainted, tainting, taints) | Banned outright. The "Taint track" mechanic is retired; its function is subsumed by Coherence. | None needed. The phenomenon previously called "taint" is the drift indexed by Coherence. |
| `corruption` (and variants: corrupt, corrupts, corrupted, corrupting, corruptive, corruptly) | Banned outright in the moral/character-condemnation register. | The phenomenon previously framed as "corruption" is reframed as **Drift** (Coherence-indexed structural decoupling from human-mode equilibrium, not moral fall). |
| `epistemic seduction` | Banned outright as a term. | The concept is retained but reframed: what was called "epistemic seduction" was a partial gesture at what is now articulated as Drift — but Drift is a more complete account: tridimensional, dual-facing, Coherence-indexed. |

**Note on "Drift":** working term. May be renamed in future term-governance work but the concept is settled.

---

<!-- atom: valoria_session_2026_04_25_master_consolidation__03__3-pre-work-contamination-surface-canon-tier | section_index: 3 | source_section: "3. Pre-Work Contamination Surface (canon/ tier)" -->


## 3. Pre-Work Contamination Surface (canon/ tier)

Word-boundary scan (avoiding "Certainty"-style substring false positives) found 16 contaminated lines across 4 canon docs:

### `canon/02_canon_constraints.md` — 4 lines, highest severity

| Line | Severity | Term(s) | Function |
|---|---|---|---|
| L11 | S3 (negation) | `corruption` | P-02 enforcement clause: "must not imply evil, corruption, or negativity..." |
| L15 | S1 (structural) | `Taint` | P-06: "Taint track does not apply" — names the mechanic |
| L19 | S1+S3 | `Taint`, `corrupts`, `Epistemic seduction` | **P-10 itself** — the principle was *named* "Epistemic seduction." Self-referential censorship: forbade "language of corruption" while naming the mechanic "Taint." |
| L21 | S1 | `Taint` (×2) | P-12: "Knot strain mechanics... Patch O: +1 strain/season on Close Knots at Taint 4–6" |

### `canon/00_philosophical_foundations_rules.md` — 4 lines

A11 (axiom heading), C4 (constraint heading), B-table glossary row, D enforcement-line — all named "Epistemic Seduction" structurally.

### `canon/00_philosophical_foundations.md` — 7 lines

§16.1 section title, §19.4 section title, plus 5 body-prose definitional uses across §16.1, §16.3, §19.4, §22.1, and Appendix A row 6.3.

### `canon/01_foundations_amendment_self_rendering.md` — 1 line

L50 cross-reference: "The epistemic seduction described in §16.1..."

### Severity classification

- **S1 (Structural)** — the term *names* a canonical principle, axiom, or mechanic. Replacement requires a new concept name and propagates through all citations.
- **S2 (Doctrinal body text)** — body prose using censured term to define or explain canon. Editorial rewrite needed.
- **S3 (Negation prose)** — "must not be X / not a X mechanic" — using term to forbid it. Easy rephrase, no concept replacement needed.

### Cross-file dependency map (resolved)

```
canon/00_philosophical_foundations.md
  §16.1 "Epistemic Seduction"  → renamed §16.1 "Coherence as the Integrity of Layer-Two Self-Rendering"
  §19.4 "Epistemic Seduction Curve"  → DELETED (Part Nine entirely removed)
       ↑ cited by ↓
canon/00_philosophical_foundations_rules.md
  A11 "Epistemic Seduction"  → renamed A11 "Drift From Human-Mode Being"
  C4  "Epistemic Seduction"  → renamed C4 "Drift Mechanics"
       ↑ cited by ↓
canon/02_canon_constraints.md
  P-06 referenced "Taint track"  → references "Coherence" (layer-2 absence for threadcut)
  P-10 named "Epistemic seduction" + "Taint track must not... corruption"  → rewritten as Coherence-commensurability
  P-12 referenced "Taint 4–6"  → rewritten as tridimensional drift propagation
       ↑ cited by ↓
canon/01_foundations_amendment_self_rendering.md (§16.1 cross-ref)  → updated
[+ ~30 design files cite Taint track / A11 / P-10]  → DEFERRED to design-tier sweep
```

---

<!-- atom: valoria_session_2026_04_25_master_consolidation__04__4-proposed-architecture-for-term-governance-deferr | section_index: 4 | source_section: "4. Proposed Architecture for Term Governance (deferred — see §10)" -->


## 4. Proposed Architecture for Term Governance (deferred — see §10)

Eight-layer enforcement model, ordered by leverage and feedback speed:

| Tier | Layer | Action | Purpose |
|---|---|---|---|
| 1 | **A — Pre-bootstrap** | Project-instructions censure block | Precedes all reads; one-time edit; highest leverage |
| 2 | **B — Bootstrap** | `references/censured_vocabulary.yaml` + bootstrap loader + status block reinforcement | Re-asserts ban every session |
| 3 | **D — Read-time** | Wrap `github_ops.read_files_graphql` to inject `[CENSURED VOCABULARY DETECTED]` warning header on contaminated reads | Breaks the regen cycle: Claude reads file, sees warning, knows not to mirror terms |
| 4 | **Source** | Canon-tier rewrite | **DONE** (this work) |
| 5 | **E — Commit** | New `censure_gate()` in `safe_commit` | Hard reject of additions containing censured terms outside permitted contexts |
| 6 | **F — Post-push CI** | GitHub Actions check on push | Catches manual web-UI edits and any path bypassing hooks |
| 7 | **C — Skill-load** | Editorial scrub of contaminated skill files | Closes secondary propagation channel |
| 8 | **Meta** | `valoria_collator.py` extension: new drift type `CENSURED_VOCABULARY` + recurring sweep | Long-term audit |

**Two-channel surfacing** for what to censure:
1. **Automated discovery** — term-frequency scan across all design docs cross-referenced against `alias_registry.yaml` + `proper_noun_registry.yaml`. Anything appearing 5+ times but unregistered is a candidate for review.
2. **Manual seed** — Jordan provides terms; Claude greps to find footprint and classifies (banned vocab vs. struck concept vs. needs-replacement-decision).

---

<!-- atom: valoria_session_2026_04_25_master_consolidation__05__5-pipeline-data-stream-analysis | section_index: 5 | source_section: "5. Pipeline / Data-Stream Analysis" -->


## 5. Pipeline / Data-Stream Analysis

Channels through which censured terminology can re-enter Claude's outputs, in order of leverage:

```
Layer A — Pre-bootstrap (every conversation)
  ├─ project_instructions
  └─ project_files

Layer B — Bootstrap (mandatory, first turn)
  ├─ session_log_current.md
  ├─ canon/editorial_ledger_summary.yaml
  ├─ references/file_index_summary.md
  └─ references/canonical_sources.yaml

Layer C — Skill loads (when Claude reads /mnt/skills or fetches skills/* from repo)
  ├─ skills/valoria-orchestrator/scripts/* (already loaded in bootstrap)
  ├─ skills/valoria-canon-guard/SKILL.md (CONTAMINATED — pre-rectification)
  ├─ skills/valoria-mechanic-audit/SKILL.md (CONTAMINATED)
  └─ skills/valoria-simulator/SKILL.md (CONTAMINATED)

Layer D — Per-task fetches via github_ops.read_files_graphql
  ├─ canon/* (4 of 10 files contaminated pre-rectification, now CLEAN)
  ├─ designs/* (heavy contamination — pending sweep)
  ├─ params/* (false positives mostly; few real hits)
  └─ references/* (throughlines_complete, throughlines_meta_infill CONTAMINATED — pending)

Layer E — Commit (safe_commit gate)
Layer F — Post-push (CI)
Layer G — Session close (safe_session_close)
```

**Regeneration cycle (root cause):** Claude reads canon files containing censured terms → mirrors the terms in output → output gets committed → next session reads the contaminated file → cycle persists. The canon-tier rewrite breaks this at the source. Layers A/B/D add containment for terms that re-emerge from training-data priors or from contaminated non-canon files.

---

<!-- atom: valoria_session_2026_04_25_master_consolidation__06__6-audit-of-philosophical-foundations-rewrite | section_index: 6 | source_section: "6. Audit of Philosophical Foundations Rewrite" -->


## 6. Audit of Philosophical Foundations Rewrite

The first-pass rewrite proposal was audited against:
- canon/01_foundations_amendment_self_rendering.md
- canon/02_foundations_amendment_leap_mechanism.md
- canon/02_canon_constraints.md (other unchanged P-rules)
- Jordan's articulated philosophical content on Coherence

### Pattern discovered

**Foundations was thinner than its own amendments.** canon/01 Amendment 2 L38 already contained the tridimensional articulation of Coherence ("the being's actuality is altered, their intelligibility is altered — both to themselves and to others per Husserl's apperception, and their temporality is altered as retention and protention decohere"). The first-pass §16 rewrite under-articulated this. The Leap-mechanism amendment Amendment 1 already distinguished reflexive and outward facings of layer 2; the first-pass §16 specified only reflexive. canon/01 Amendment 3 explicitly stated apperception by others as a Coherence diagnostic; the first-pass §16 missed this entirely.

The amendment is supposed to *extend* the foundation. When it adds philosophical content, that content should be *upstreamed* into foundations. This was not happening — the amendment did the philosophical work, and the foundation fell behind.

### Audit categories (22 findings)

| Category | Count | Severity distribution |
|---|---|---|
| A — Major structural inconsistencies in proposed §16 | 8 | 4 SEVERE, 4 MODERATE |
| B — Internal contradictions within rewrite | 2 | 2 LOW |
| C — Inconsistencies between rewrite and unchanged docs | 5 | 2 SEVERE, 3 MODERATE |
| D — Issues with proposed dependent-doc rewrites | 5 | 4 SEVERE, 1 LOW |
| E — Vocabulary table inconsistencies | 3 | 2 MODERATE, 1 LOW |
| F — Existing canon docs not yet audited | 3 | 3 INFO |
| G — Rhetorical-question scrub residual | 2 | 1 LOW, 1 PASS |
| H — Editorial markers retained | 1 | 1 LOW (decision flagged) |

### All SEVERE and MODERATE findings closed

Final state:
- §16 rewritten to absorb canon/01 amendment philosophical content (A-1 through A-8).
- B-1, B-2 closed via §16.2 explicit Real-approach articulation.
- C-1 (canon/01 L50 cross-ref): patched to "drift described in §16.1".
- C-2 (canon/01 L60 "Relational contagion"): patched to "Relational propagation".
- C-3 (orthogonality of Coherence/TS): stated in §16.1.
- C-4 (operation-type alignment principle): closed by follow-up commit `aae1e724` adding paragraph at end of §16.1: "Drift accumulates not from threadwork as such, but from threadwork that opposes the rendering's stabilising tendency."
- C-5 (cross-ref §5.3 → canon/01 four-mode taxonomy): intentionally not added; the foundations stays at its level, the amendment refines.
- D-1 (rules A11/C4 expanded): rewritten to mirror revised §16.
- D-2 (P-10 expanded): tridimensional + dual-facing + Coherence-0 ≠ threadcut.
- D-3 (P-02 positive grounding): Lacanian Real positively grounded + moral-language exclusion.
- D-4 (P-12 tridimensional): rewritten as tridimensional propagation.
- D-5 (P-06 layer-2 framing): rewritten with layer-2 absence for threadcut.
- E-1 (Coherence vocab entry): expanded with full content.
- E-3 (Real entry includes drifting practitioner): added.
- G-1, G-2 (rhetorical-question scrub): all questions in §16/§17/§18 are declarative or rhetorical-defining.
- H-1 (editorial markers retained): retained with rationale (meta-philosophical, not external mechanics).

---

<!-- atom: valoria_session_2026_04_25_master_consolidation__07__7-philosophical-content-established | section_index: 7 | source_section: "7. Philosophical Content Established" -->


## 7. Philosophical Content Established

The substantive philosophical content that crystallized through this work. This is the durable intellectual deliverable beyond the file changes.

### 7.1 Coherence — the integrity of layer-two self-rendering

**Definition.** Coherence is the structural integrity of the practitioner's layer-two self-rendering: the always-already, unconscious threadwork by which the being is held in the configuration of human-mode being. Etymologically, *cohaerere* — "to stick together, to adhere together" — names exactly this: the adhering-together by which the practitioner's threads are sustained in the shape of a human being-in-the-world.

**What Coherence is not.** Spiritual strength. Moral standing. Willpower. Religious or theological conviction. Sanity in any colloquial sense. Capability or capacity. Character.

### 7.2 The two facings of layer-two self-rendering

Layer-two self-rendering has two facings, and Coherence is the integrity of both simultaneously.

- **Reflexive facing.** The apperceptive self-presentation by which the practitioner is given to themselves — the Husserlian I-think that accompanies all their representations, the moment-to-moment unity that holds *I am this person, in this time, in this world, of this kind*.
- **Outward facing.** The configuration as it is rendered to others' apperception — the practitioner appearing as a unified human subject to those whose rendering is processing them.

Both must be intact for Coherence. Degradation of either is Coherence loss.

### 7.3 Coherence is structurally intersubjective

A practitioner cannot fully judge their own Coherence. The apperceptive self-presentation that is failing is the same apperceptive self-presentation that would be required to perceive the failure. Others — whose renderings must work harder to integrate the drifting practitioner as a coherent human subject — register the failure first, through the somatic and perceptual labour of attempting to apperceive what their rendering's specification cannot easily hold.

This is why Coherence diagnostics depend on intersubjective observation in canon/01's "Fragmented" and "Fractured" bands, where the practitioner is apperceived differently by different observers.

### 7.4 Coherence loss is tridimensional per Inseparability

Threads are simultaneously substrate and condition of possibility. The Inseparability Principle (§1.1) entails that any change to the practitioner's thread-configuration manifests across all three dimensions at once. Coherence loss is therefore tridimensional in its very structure:

- **Actuality.** The practitioner's material configuration shifts. (Posture wrong, light interacts oddly, presence occupies more space than the body.)
- **Intelligibility.** The practitioner becomes harder to apperceive — both to themselves and to others. (Speaking through glass; addressed differently by different people; self-presentation falters.)
- **Temporality.** Retention and protention decohere; experience of time becomes structurally less stable. (Micro-slippages between action and response; conversations that loop or skip.)

**Any account of Coherence that treats it as moving along one dimension only — as moral state, as perceptual quality, as somatic signature — is incomplete by definition.** The drift is irreducibly tridimensional because the configuration that drifts is irreducibly tridimensional.

### 7.5 Coherence is orthogonal to Thread Sensitivity

TS measures perceptual reach into the substrate. Coherence measures the integrity of layer-two self-maintenance. They do not co-vary as a structural matter. Any combination is possible:
- High TS + high Coherence: perceptive and stable
- High TS + low Coherence: perceptive and destabilising
- Low TS + low Coherence: blind and destabilising
- Low TS + high Coherence: ordinary baseline

**Implication for character design.** Edeyja with potentially the highest Spirit in the game (6, possibly 7) is also at 0 Religious Conviction (formerly Certainty — see §10 for rename). High Spirit + low Religious Conviction + high Coherence + arbitrary TS is structurally permitted. The previous "Certainty implies spiritual strength" implicit conflation is broken by the rename.

### 7.6 Coherence-0 ≠ threadcut

A practitioner at Coherence 0 has lost layer-two self-rendering. **They are not threadcut.** Layer 1 (Ein Sof spooling) continues unchanged: the ground continues to provide their thread-substrate. What has ceased is the always-already self-threadwork that shaped that spooling into the human configuration.

Categorical distinction:
- **Threadcut beings:** no layer 1 (no Ein Sof spooling); maintained entirely by layer 3.
- **Coherence-0 practitioners:** no layer 2; layer 1 still active.
- **Organic humans:** layers 1 + 2.
- **High-TS Coherence-0 practitioners:** layers 1 + 3.

### 7.7 What follows Coherence 0 is TS-gated

The endpoint of Coherence loss is not a single state. It is a TS-gated set of structurally distinct trajectories (canon/01 Amendment 4):

- **TS 30–49 (Stirring): Ontological Freefall.** Cannot self-render at depth; reshaped by environmental thread-forces.
- **TS 50–69 (Attuned): Relational Persistence.** Can maintain knot-bonds; identity becomes relational.
- **TS 70–89 (Sensitive): Structural Reconstitution.** Can self-rework into stable non-human configuration.
- **TS 90–100 (Resonant): Full Reconstitution + Reality-Strain.** Maintains arbitrary configuration through continuous deliberate threadwork; produces substrate strain in vicinity (the localised Einhir parallel).

### 7.8 The operational origin of Coherence loss

Not every thread operation produces drift. The principle (the §16.1 closing paragraph from the follow-up commit):

> Operations aligned with the rendering's stabilising tendency — those that accelerate what the substrate's own spooling would resume given sufficient time, restoring configurations the substrate was already moving toward — leave the practitioner's configuration aligned with the direction the substrate is going in its own tendency. Such operations produce no Coherence cost. Operations that impose configurations the substrate would not resume of its own tendency — that hold actualised states the spooling did not provide — must be sustained against the absence of the substrate's support. The cost of holding such a configuration is a configurational alteration to the practitioner: the substrate's non-support is borne, structurally, by the practitioner's own threads. This is the operational origin of Coherence loss. Drift accumulates not from threadwork as such, but from threadwork that opposes the rendering's stabilising tendency.

The mechanical taxonomy that sorts operations along this axis (restorative / manipulative / destructive) is in canon/02_foundations_amendment_leap_mechanism.md Amendment 3. The structural principle is in foundations.

### 7.9 Drift propagation is tridimensional

A drifting practitioner's configurational alteration propagates through every knot they hold, manifesting on connected entities across all three dimensions:
- **Actuality** — configurational pull on the connected entity.
- **Intelligibility** — apperceptive degradation in the connected entity's relation to the practitioner.
- **Temporality** — retention/protention disturbance regarding shared experiences.

Cumulative exposure to a drifting practitioner is itself a form of low-grade confrontation. This means: a single drifting practitioner is, over time, a vector by which others' Coherence may begin to fail. Drift is propagable through community.

This is why early detection and communal accountability are structurally necessary. The practitioner is not the only one at risk; everyone knotted to them is bearing tridimensional force their own configuration may not be able to absorb.

### 7.10 The Reality-Strain Principle

A practitioner whose Coherence has failed and who has the perceptual reach to maintain themselves through deliberate layer-three threadwork is, by structural necessity, drawing on the substrate the way the Einhir site-network drew on it. The scale is different (one being vs. civilizational lattice). The duration is different (a lifetime vs. centuries). **The physics is the same.**

The Calamity is therefore not only a historical event in the deep past. It is the structural consequence of exactly the configuration a Coherence-0 practitioner of high perceptual reach is sustaining — localised, reduced in scale, but identical in mechanism.

### 7.11 Monstrosity grounded in the Lacanian Real

Monstrosity is what Lacan named the Real in embodied form: that which escapes symbolisation, what cannot be captured by the rendering's signifying capacity, what remains as the unassimilable remainder when the rendering has done all it can do. The Real is not the opposite of the symbolic; it is what the symbolic cannot reach. Monstrosity is the Real arriving as something the rendering must contend with — a being-encounter where the rendering's signifying operations meet what they cannot constitute.

**Monstrosity is structurally outside the moral register.** Monstrous beings are not evil. They are surfeit-of-being from the Ein Sof, arriving through structural openings, and the rendering's failure to integrate them produces the phenomenology (uncanny, terrifying, wrong) that human renderings register.

**Connection to drift.** A drifting practitioner approaches the Real as their configuration decouples from human-mode equilibrium. Advanced drift produces effects that approximate the rendering-strain produced by proximity to monstrous beings, scaled to the partial decoupling.

### 7.12 No external-mechanics references in foundations

The philosophical foundations document is now a closed prose document. It contains no:
- References to specific tracks or scales beyond defining what Coherence (orthogonal track) is conceptually
- References to dice, rolls, GM judgment, or system mechanics
- Cross-references to design-doc mechanics

It contains:
- Internal cross-references (§1.1, §4.1, etc.)
- One cross-reference to canon/01 (the parallel-tier amendment) and canon/02 leap-mechanism (the parallel-tier amendment) in service of articulating Coherence as a layer concept; these are foundations-tier, not mechanics-tier.
- No questions that aren't rhetorical definitions. All Q-form sentences in the original were converted to declarative form or were rhetorical-defining.

---

<!-- atom: valoria_session_2026_04_25_master_consolidation__08__8-canon-changes-committed | section_index: 8 | source_section: "8. Canon Changes Committed" -->


## 8. Canon Changes Committed

### 8.1 `canon/00_philosophical_foundations.md` (full rewrite)

| Change | Type | Locus |
|---|---|---|
| §4.1 reframed: monstrosity = Lacanian Real | Doctrinal rewrite | Body |
| §4.3 cross-ref blockquote to leap-mechanism amendment removed | Mechanics excision | Body L419 of original |
| §16 fully rewritten as "The Drift From Human-Mode Being" with §16.1–§16.4 | Doctrinal rewrite | Body |
| §18 vocabulary table updated: removed Epistemic Seduction; added/expanded Coherence, Apperception, The Real, Drift, Reality-Strain | Vocabulary | Body |
| Parts Nine through Twelve (mechanics translations: ttrpg, board game, video game, hybrid) deleted | Section deletion | Body §19–§23 |
| Appendix A row 6.3 updated to reference §16.1–§16.4 with new content | Cross-reference | Appendices |
| Editorial marker added | Provenance | §16 |
| Document size: 1464 lines → 446 lines | Size reduction | Whole document |

### 8.2 `canon/00_philosophical_foundations_rules.md`

| Change | Locus |
|---|---|
| A7 (Monstrosity) updated: "grounded in the Lacanian Real" + structural-outside-moral-register | A7 |
| A9 (Threadcut Beings) updated: categorical distinction from Coherence-0 practitioners explicit | A9 |
| A11 renamed: "Epistemic Seduction" → "Drift From Human-Mode Being"; full content per revised §16 | A11 |
| A12 (Knotting) updated: drift propagates tridimensionally per A11 | A12 |
| B-table glossary updated: removed Epistemic Seduction; added/expanded Coherence, Apperception, The Real, Drift, Reality-Strain | B section |
| C4 renamed: "Epistemic Seduction" → "Drift Mechanics"; tridimensional + dual-facing + propagation + reality-strain content | C4 |
| D enforcement-line: "A11 (epistemic seduction)" → "A11 (drift from human-mode being)" | D section |

### 8.3 `canon/01_foundations_amendment_self_rendering.md`

Two surgical line-edits:
- L50: "The epistemic seduction described in §16.1" → "The drift described in §16.1"
- L60: "Relational contagion (§16.3)" → "Relational propagation (§16.3)"

### 8.4 `canon/02_canon_constraints.md`

| Constraint | Change |
|---|---|
| **P-02** | Reframed as Lacanian Real grounding for monstrosity. Mechanical implication includes positive grounding (monstrous origin in surfeit-of-being from Ein Sof) AND prohibition (no evil/sin/moral-negativity language as ontological source). Violation test catches both failures. |
| **P-06** | Updated framing: threadcut beings have no layer 2; their self-maintenance is layer-3 deliberate threadwork without ground-spooled accumulation. Coherence does not apply (absent by structure, not degraded). Categorical distinction from Coherence-0 practitioners explicit. |
| **P-10** | Completely rewritten. New principle: "Coherence indexes commensurability with human-mode being." Mechanical implication requires tridimensional manifestation per Inseparability and dual-facing structural effects. Violation test catches single-dimension reductions, moral-standing framing, and Coherence-0/threadcut conflation. |
| **P-12** | Completely rewritten. New principle: "Drift propagation is tridimensional." Mechanical implication requires effects in actuality (configurational pull), intelligibility (apperceptive degradation), and temporality (retention/protention disturbance) on connected entities. Violation test catches single-dimension propagation and generic-strain-value reductions. |

### 8.5 Files unchanged (verified clean)

- canon/02_foundations_amendment_leap_mechanism.md (already clean)
- canon/03_canonical_timeline.md
- canon/README.md
- canon/editorial_ledger_index.md
- canon/patch_register_index.md
- canon/session_checkpoint.md

---

<!-- atom: valoria_session_2026_04_25_master_consolidation__09__9-verification-status | section_index: 9 | source_section: "9. Verification Status" -->


## 9. Verification Status

### 9.1 Censure compliance

Post-commit fetch from GitHub, full canon scan:

```
canon/00_philosophical_foundations.md          : CLEAN
canon/00_philosophical_foundations_rules.md    : CLEAN
canon/01_foundations_amendment_self_rendering.md: CLEAN
canon/02_canon_constraints.md                  : CLEAN
canon/02_foundations_amendment_leap_mechanism.md: CLEAN
canon/03_canonical_timeline.md                 : CLEAN
canon/README.md                                : CLEAN
canon/editorial_ledger_index.md                : CLEAN
canon/patch_register_index.md                  : CLEAN
canon/session_checkpoint.md                    : CLEAN

CANON TOTAL: 0 censured-term hits across 10 files
```

### 9.2 Structural compliance

Live-file checks against the post-commit version of `canon/00_philosophical_foundations.md`:

- §16 retitled "The Drift From Human-Mode Being" ✓
- §16.1 new title "Coherence as the Integrity of Layer-Two Self-Rendering" ✓
- §16.4 reality-strain principle present ✓
- Operational-origin paragraph present (follow-up commit) ✓
- Apperception in §18 vocabulary table ✓
- Lacanian Real in §4.1 ✓
- Editorial marker [PP-675 ED-783] present ✓
- §19–§23 (mechanics) absent ✓

### 9.3 Hook compliance

All commits passed:
- `commit_message_gate` (correct `[scope] description — PP-NNN / ED-NNN` format)
- `pre_commit_gate` (additions/deletions accounted for)
- `safe_commit` (atomic write)
- `task_gate('editorial')` (editorial scope confirmed)

---

<!-- atom: valoria_session_2026_04_25_master_consolidation__10__10-outstanding-work | section_index: 10 | source_section: "10. Outstanding Work" -->


## 10. Outstanding Work

### 10.1 Term-governance enforcement infrastructure (NEXT)

Implementation of Layers A/B/D/E from §4 architecture. Now that canon is clean, the gates can prevent reintroduction:

1. **Layer A — Project-instructions censure block.** Edit project instructions to include a censured-vocabulary section.
2. **Layer B — `references/censured_vocabulary.yaml`.** Create registry file. Extend bootstrap to fetch it. Add status-block line: "Censured terms: [N loaded]."
3. **Layer D — Read-time injection.** Wrap `github_ops.read_files_graphql` to scan fetched content for censured terms and prepend warning header to contaminated files.
4. **Layer E — `safe_commit` censure gate.** New gate function `censure_gate()` runs after `commit_message_gate`. Blocks any addition containing a censured term outside permitted contexts (revision-note markers, deprecated/ path).

### 10.2 Sub-system terminology boundary directive

Per Jordan: terms relating specifically to mass battle / personal combat / social contest / faction actions / fieldwork must be sharply defined and have **no possibility of confusion** with other systems — most critically, **no terminology overlap with metaphysics / ontology / threadwork / beliefs / personalities / inspirations / duties**.

This is a governance principle requiring:
- Audit of current sub-system vocabulary for any cross-domain collisions.
- Encoding the boundary in `censured_vocabulary.yaml` as a separate `cross_domain_collisions` block or in `alias_registry.yaml` per-term.
- A separate drift type in the collator: `CROSS_DOMAIN_COLLISION`.

### 10.3 Design-tier sweep

Per pre-rectification scan:
- "taint" raw hits: 288 (many false positives from "Certainty" substring; need word-boundary scan)
- "corruption" raw hits: 64
- "epistemic seduction" raw hits: 40

Many in `deprecated/` (legitimate). Real contamination in active design docs:
- `designs/threadwork/threadwork_v30.md` and infill
- `designs/npcs/npc_behavior_v30.md` and infill
- `designs/ui/valoria_ui_ux_v4_1.md` and v4_2_workplan and max_audit
- `designs/arcs/arc_expansion_v30.md`
- `designs/provincial/faction_politics_v30_index.md`
- `designs/architecture/player_agency_v30.md`
- `designs/audit/throughlines_transitions_hierarchy.md`
- `designs/audit/valoria_systems_workplan.md` and valoria_workplan_final.md
- `designs/scene/fieldwork_godot.md`
- `designs/world/worldbuilding_canon_audit_v30_infill.md`
- `references/throughlines_complete.md`
- `references/throughlines_meta_infill.md`
- `references/propagation_log.md`
- `params/board_game.md`
- `params/bg/ministry.md`

Plus skill files:
- `skills/valoria-canon-guard/SKILL.md`
- `skills/valoria-mechanic-audit/SKILL.md`
- `skills/valoria-simulator/SKILL.md`

This is multi-session editorial work. The censure gate (Layer E) will prevent further drift from this point; the sweep is cleanup of pre-existing state.

### 10.4 Conviction Track rename

Jordan flagged: "Conviction Track" implies "how influenced someone is by your arguments" but that's misleading. Replacement name needed.

**Status:** GAP — requires either (a) Claude reads `designs/scene/conviction_track_v30.md` and proposes 2–3 candidate names, or (b) Jordan specifies what CT actually tracks semantically and Claude proposes against that.

### 10.5 Certainty → Religious Conviction rename

Jordan directed: rename Certainty to Religious Conviction. The current "Certainty" doc's range is "Solmund orthodoxy (5) → Thread acceptance (0)" — i.e., it tracks belief-in-Solmund-theology, not spiritual strength. Renaming to "Religious Conviction" disambiguates from Spirit (which is the spiritual-strength stat).

**Status:** Decision pending on:
- Abbreviation: "RC"? Conflicts with anything?
- Order of operations: rename Conviction Track first (to avoid collision), then rename Certainty?

Scope of rename:
- `references/alias_registry.yaml` (canonical entry)
- `params/core.md` (Certainty Track section, ~30 lines)
- All design docs that mention Certainty (significant footprint — collator will surface as `LEGACY_TERM_USED` post-rename)
- All session logs / editorial-ledger entries
- `canon/02_canon_constraints.md` P-01 ("Certainty modifiers")

The collator's existing `legacy:` field per alias entry is exactly the case the registry was designed for. Once renamed, the collator flags every legacy use for cleanup.

### 10.6 Editorial ledger regeneration

ED-783 is now active (cited in editorial marker in `canon/00_philosophical_foundations.md`). The editorial ledger summary (`canon/editorial_ledger_summary.yaml`) is auto-generated and currently shows `next_id: 739` (stale — actual max in ledger is 782, now 783 with this work). A regeneration is needed to:
- Update `next_id` to 784
- Add ED-783 to `recent_resolutions`
- Reflect the canon/00 + canon/01 + canon/02 + rules updates

---

<!-- atom: valoria_session_2026_04_25_master_consolidation__11__11-key-decisions | section_index: 11 | source_section: "11. Key Decisions" -->


## 11. Key Decisions

Decisions made during this work that future sessions need to know:

| # | Decision | Rationale |
|---|---|---|
| K-1 | "Drift" is the working term for the Coherence-indexed phenomenon | Etymology of "Coherence" (cohaerere = to adhere together) + drift = decoupling. May be renamed in future term-governance work; concept is settled. |
| K-2 | "Taint track" is retired (not renamed) | Coherence already exists as a track and now carries this phenomenology natively. Two tracks for one phenomenon would be redundant. |
| K-3 | Foundations contains no external mechanics references | Per Jordan's directive. Cross-references to canon/01 and canon/02 amendments are at the foundations tier (parallel philosophical work), not mechanics tier. |
| K-4 | Foundations contains no non-rhetorical questions | Per Jordan's directive. All Q-form sentences in original were converted to declarative or rhetorical-defining form. |
| K-5 | Parts Nine through Twelve (mechanics translations) deleted from foundations | Per directive. ~470 lines of TTRPG / board-game / video-game / hybrid mechanics content removed. Belongs in design docs. |
| K-6 | The §16 phenomenon (drift) is irreducibly tridimensional | Per Inseparability Principle (§1.1). Any single-dimension account of Coherence is incomplete by definition. Mechanics violating this fail P-10. |
| K-7 | Coherence has two facings (reflexive + outward) and is intersubjective | Apperceptive self-presentation + apperception by others. Both must be intact. Coherence is judged externally; the practitioner cannot fully self-assess. |
| K-8 | Coherence-0 ≠ threadcut, categorically | Layer-1 (Ein Sof spooling) continues at Coherence 0. Threadcut beings lack layer 1. Mechanics conflating these fail P-06. |
| K-9 | Drift propagates tridimensionally through knots | Single-dimension propagation or generic-strain-value reductions fail P-12. |
| K-10 | Reality-strain is foundational, not mechanical | The Einhir parallel principle (one-being-scale Calamity-mechanism) is in §16.4 of foundations. The mechanical taxonomy (restorative/manipulative/destructive) is in canon/02 leap-mechanism amendment. |
| K-11 | Operational origin of Coherence loss is alignment vs. opposition to substrate tendency | Restorative ops (aligned with substrate stabilising tendency) cost zero Coherence; manipulative/destructive ops (opposing) cost Coherence proportional to deviation. |
| K-12 | Editorial markers retained in foundations | Meta-philosophical (resolution-status of philosophical critique items), not external mechanics. |
| K-13 | Censure rectification is canon-tier complete; design-tier deferred | Containment first (canon clean → enforcement infrastructure → design sweep). |

---

<!-- atom: valoria_session_2026_04_25_master_consolidation__12__12-pending-decisions-gaps | section_index: 12 | source_section: "12. Pending Decisions / GAPs" -->


## 12. Pending Decisions / GAPs

| GAP | Topic | Required input |
|---|---|---|
| GAP-A | "Drift" working term — confirm or rename | Concept-name preference. May leave as-is; flagged as working term. |
| GAP-D | Conviction Track rename | Either let Claude read the design doc and propose candidates, or specify what CT actually tracks semantically. |
| GAP-E | Certainty → Religious Conviction abbreviation | "RC" abbreviation? Order of operations vs. Conviction Track rename? |
| GAP-F | Editorial ledger regeneration | Manual regen, or wait for auto-process? |
| GAP-G | Layer A/B/D/E term-governance infrastructure scope | Confirm priority and any constraints on implementation order. |
| GAP-H | Sub-system terminology boundary audit scope | Which sub-systems first? Is the directive to audit existing terms only, or also to constrain future naming? |

---

<!-- atom: valoria_session_2026_04_25_master_consolidation__13__13-process-meta-observations | section_index: 13 | source_section: "13. Process / Meta Observations" -->


## 13. Process / Meta Observations

For future sessions and for general project hygiene:

1. **The amendment-exceeds-foundations pattern is a documentation anti-pattern.** When canon/01 and canon/02 amendments accumulated philosophical content, that content should have been upstreamed into foundations rather than living only in amendments. The audit phase caught this; the rewrite phase fixed it. Future amendments should explicitly upstream their philosophical work to the foundation document at the time of the amendment.

2. **Word-boundary regex is mandatory for term scanning.** Substring matching produces too many false positives (e.g., "Certainty" contains "tain" and shows up in any "taint" search). All term-governance scans must use `\b` boundaries.

3. **TOC vs. body splice hazards.** The first-pass file build for `canon/00_philosophical_foundations.md` used a regex that matched TOC entries when targeting body sections. Positional indexing (counting occurrences of a section header pattern, taking the second one for body) is more robust than regex matching when both TOC and body use the same anchor strings.

4. **The censure registry must distinguish three classes:**
   - **Banned outright** (vocabulary, no replacement needed — e.g., "taint")
   - **Banned, concept obsolete** (mechanic killed, references should be deleted)
   - **Banned, concept needs new name** (rewrite required — e.g., "epistemic seduction" became "drift")

5. **Editorial markers referencing censured terms must use abstract phrasing.** The first attempt at the §16 editorial marker named the censured terms ("Censured terminology removed (Epistemic Seduction, Taint, corruption-as-mechanic)") and re-contaminated the file. Markers should reference "censured terminology" generically with citation to the rectification batch.

6. **Bootstrap session tokens are per-process-invocation.** Each `bash_tool` call is a fresh subprocess and requires re-running `read_files_graphql` to establish a session token. Long multi-step work needs to re-fetch bootstrap context at the start of each script.

7. **Commit message format is enforced.** `[scope] description — PP-NNN / ED-NNN if applicable` with valid scopes: `bugfix, cleanup, compilation, editorial, fix, godot, infrastructure, patch, phase, simulation, skill`.

---

<!-- atom: valoria_session_2026_04_25_master_consolidation__14__14-references | section_index: 14 | source_section: "14. References" -->


## 14. References

**Repository:** `jordanelias/ttrpg`
**Patch Proposal:** PP-675
**Editorial Ledger:** ED-783
**Commits:**
- `b14f0671ae9c7e7bb578865f92745dbcaab64bf0` — primary 4-file rectification
- `aae1e72413f9417f46a6d2fd8cb25646bd9ee6aa` — operational-origin paragraph follow-up

**Files modified:**
- `canon/00_philosophical_foundations.md`
- `canon/00_philosophical_foundations_rules.md`
- `canon/01_foundations_amendment_self_rendering.md`
- `canon/02_canon_constraints.md`

**Related canon (unchanged but contextually relevant):**
- `canon/02_foundations_amendment_leap_mechanism.md` — operation-type taxonomy
- `canon/03_canonical_timeline.md` — Calamity, Solmund emergence
- `references/canonical_sources.yaml` — `struck:` block for outmoded mechanics
- `references/alias_registry.yaml` — `legacy:` field per term entry

*End of Master Consolidation*

### From `valoria_session_master_2026-04-25.md` (2 atoms)

<!-- atom: valoria_session_master_2026-04-25__03__context-window-3-ed-717-cleanup | section_index: 3 | source_section: "Context Window 3 — ED-717 + Cleanup" -->


## Context Window 3 — ED-717 + Cleanup

### ED-717: Faction Substrate-Postures (М-4 Throughlines)

Every faction now has a defined relationship to Thread/substrate. М-4 count: 4 → 7.

#### T-15a: Hafenmark — Unmediated Sovereigntist

Baralta is the Protestant faction. Shares Church theology entirely (Solmund is divine, threadwork is heresy, Solmundian ethics are correct) but rejects two things: that the Holy Confessor has exclusive access to Solmund, and that the Church should govern. Divine-right claim: anyone truly faithful can hear Solmund, therefore governance belongs to the faithful ruler.

**Chain:** Shared Solmundian theology → rejection of ecclesial monopoly → divine-right governance → Parliamentary Suppress CI → Dynastic Proclamation → Thread revelation forces confrontation (TS 0 means Baralta can't access what she claims governance by right of faith).

**Crisis at revelation:** If Thread access is experiential, Baralta's TS 0 means she cannot personally access what she claims to govern by right of faith. The faction whose identity is "faith is not mediated" may discover that Thread access IS mediated — by sensitivity she doesn't have.

#### T-15b: Löwenritter — Substrate-Agnostic Protector

Praetorian faction. Governance authority from institutional duty and military capability. Substrate irrelevant to national defense. Ehrenwall: Certainty 4, TS 0, Martial Honour ethics.

**Chain:** Martial Honour oath → substrate irrelevant to defense → graduated autonomy driven by Crown competence, not Thread → Thread revelation: the crisis destroying Valoria has a substrate cause → military tools cannot address substrate decay → forced choice: adapt mission (cooperate with Varfell/Wardens, compromise identity) or maintain military-only mission (fight symptoms).

**Crisis at revelation:** The existential threat is physics, not politics. The military order dedicated to Valoria's survival is fighting the wrong war.

#### T-15c: RM — Substrate-Heritage Reclaimer

Only faction with an **unconscious** substrate-posture. Einhir cultural practices were substrate-connected, but RM rebuilds them as political tradition without knowing why they work. Hidden Thread-site bonus: RM governance produces better outcomes at Thread-proximate settlements for reasons no one understands.

**Chain:** Einhir suppression → consensus cells → hidden Thread-site bonus → Thread revelation: heritage was substrate-connected all along → forced choice: Embrace (validates identity but risks becoming another faith-governance claim) / Denial (remain political, abandon deepest identity source) / Schism (movement splits).

**Crisis at revelation:** Vindication AND identity crisis simultaneously. Every other faction's substrate-posture is conscious. RM is doing substrate-aligned governance without knowing it.

| Commit | SHA | Files Modified | What |
|--------|-----|----------------|------|
| 11 | `5537bc9` | references/throughlines_complete.md, throughline_registry.md, throughlines_meta.md, throughlines_meta_infill.md, canonical_sources.yaml | T-15a Hafenmark |
| 12 | `cb50098` | Same 5 files | T-15b Löwenritter + T-15c RM |

### Complete М-4 Map

| T | Faction | Substrate-Posture | Conscious? | TS | Revelation Crisis |
|---|---------|-------------------|------------|-----|-------------------|
| T-08 | Church | Rendering reinforcement | Yes | Varies | Substrate reality threatens essentialist theology |
| T-09 | Varfell | Thread progressive | Yes | High | Vindicated but politically exposed |
| T-11 | Crown | Pragmatic instrumentalist | Yes | 0 | Tool becomes uncontrollable force |
| T-15a | Hafenmark | Unmediated sovereigntist | Yes | 0 | Divine right without divine access |
| T-15b | Löwenritter | Substrate-agnostic protector | Yes | 0 | Wrong war — enemy is physics |
| T-15c | RM | Substrate-heritage reclaimer | **No** | 0 | Vindication + identity crisis |
| T-21 | (cross-faction) | Thread political warfare | — | — | Mutual deterrence via shared RS |

### Editorial + Cleanup

| Commit | SHA | What |
|--------|-----|------|
| 13 | `fb16bd3` | ED-717 resolved, ED-667 resolved in editorial ledger. P1 count 2→1 |
| 14 | `7b96edd` | Residual Niflhel/Coup refs in arcs_31_35, emergent_campaign_arcs, factions_personal_v30_infill |
| 15 | `ef19887` | PP-675 backstory strike — assigned PP number to all STRUCK markers (Patch 7 from Session A) |

---

<!-- atom: valoria_session_master_2026-04-25__04__status | section_index: 4 | source_section: "Status" -->


## Status

### Resolved This Session

- **ED-717** — All factions have М-4 substrate-posture throughlines
- **ED-667** — Graduated autonomy resolves Coup Counter readiness gap
- **PP-675** — Backstory strike (father assassination → Royal Crisis Tension Card)
- **Session B** — Niflhel dissolution + Löwenritter graduated autonomy fully propagated
- **Session C** — Tensions Deck + Royal assassination specs canonized
- **conflict_architecture_proposal.md** — PROPOSAL → CANON

### Remaining

- **P1 blocker (1):** CI cap vs Piety Yield at T9 — Jordan design decision pending
- **Index regeneration** for ~15 modified files
- **Retroactive canon audit** — deferred until engine_v4 smoke-test data
- **Incidental Niflhel refs** (~30 across arc/NPC files) — non-mechanical, not blocking
- **Throughline interaction matrix** — 7 of 28 throughlines have mapped cross-interactions

## Provenance

Atom-by-atom inventory in source/section order:

| atom_id | source | section_index | source_section | lines |
|---|---|---|---|---|
| `valoria_session_2026-04-25_master__09__section-9-open-items-at-session-close` | `VALORIA_SESSION_2026-04-25_MASTER.md` | 9 | Section 9 — Open Items at Session Close | 37 |
| `valoria_session_2026_04_25_master_consolidation__00__preamble` | `valoria_session_2026_04_25_master_consolidation.md` | 0 | (preamble) | 11 |
| `valoria_session_2026_04_25_master_consolidation__01__1-scope` | `valoria_session_2026_04_25_master_consolidation.md` | 1 | 1. Scope | 21 |
| `valoria_session_2026_04_25_master_consolidation__02__2-censured-vocabulary` | `valoria_session_2026_04_25_master_consolidation.md` | 2 | 2. Censured Vocabulary | 14 |
| `valoria_session_2026_04_25_master_consolidation__03__3-pre-work-contamination-surface-canon-tier` | `valoria_session_2026_04_25_master_consolidation.md` | 3 | 3. Pre-Work Contamination Surface (canon/ tier) | 53 |
| `valoria_session_2026_04_25_master_consolidation__04__4-proposed-architecture-for-term-governance-deferr` | `valoria_session_2026_04_25_master_consolidation.md` | 4 | 4. Proposed Architecture for Term Governance (defe | 21 |
| `valoria_session_2026_04_25_master_consolidation__05__5-pipeline-data-stream-analysis` | `valoria_session_2026_04_25_master_consolidation.md` | 5 | 5. Pipeline / Data-Stream Analysis | 36 |
| `valoria_session_2026_04_25_master_consolidation__06__6-audit-of-philosophical-foundations-rewrite` | `valoria_session_2026_04_25_master_consolidation.md` | 6 | 6. Audit of Philosophical Foundations Rewrite | 49 |
| `valoria_session_2026_04_25_master_consolidation__07__7-philosophical-content-established` | `valoria_session_2026_04_25_master_consolidation.md` | 7 | 7. Philosophical Content Established | 111 |
| `valoria_session_2026_04_25_master_consolidation__08__8-canon-changes-committed` | `valoria_session_2026_04_25_master_consolidation.md` | 8 | 8. Canon Changes Committed | 53 |
| `valoria_session_2026_04_25_master_consolidation__09__9-verification-status` | `valoria_session_2026_04_25_master_consolidation.md` | 9 | 9. Verification Status | 44 |
| `valoria_session_2026_04_25_master_consolidation__10__10-outstanding-work` | `valoria_session_2026_04_25_master_consolidation.md` | 10 | 10. Outstanding Work | 83 |
| `valoria_session_2026_04_25_master_consolidation__11__11-key-decisions` | `valoria_session_2026_04_25_master_consolidation.md` | 11 | 11. Key Decisions | 22 |
| `valoria_session_2026_04_25_master_consolidation__12__12-pending-decisions-gaps` | `valoria_session_2026_04_25_master_consolidation.md` | 12 | 12. Pending Decisions / GAPs | 13 |
| `valoria_session_2026_04_25_master_consolidation__13__13-process-meta-observations` | `valoria_session_2026_04_25_master_consolidation.md` | 13 | 13. Process / Meta Observations | 23 |
| `valoria_session_2026_04_25_master_consolidation__14__14-references` | `valoria_session_2026_04_25_master_consolidation.md` | 14 | 14. References | 23 |
| `valoria_session_master_2026-04-25__03__context-window-3-ed-717-cleanup` | `valoria_session_master_2026-04-25.md` | 3 | Context Window 3 — ED-717 + Cleanup | 57 |
| `valoria_session_master_2026-04-25__04__status` | `valoria_session_master_2026-04-25.md` | 4 | Status | 19 |
