# Dossier — NLG-Proposal Graduation Needs

## Status: WORKING NOTES (lane: NLG-proposal graduation, 2026-07-05 EMERGENT NARRATIVE ENGINE effort)
_Sonnet lane. Working-tree only. Cites file+section; [UNGROUNDED] where noted; [OPEN — Jordan tuning] preserved verbatim from source._

## 0. Scope & method

Charter question (`00_grounding/00_engine_charter.md` Q4, "**Prose realizer**: graduate the NLG
proposal…"): what exactly must be decided/authored to take
`designs/audit/2026-06-28-narrative-state-articulation/03_articulation_nlg_architecture.md`
(explicitly `<!-- STATUS: PROPOSAL (architecture-only)… No data schemas, no worked example… -->`,
§0/header) from architecture-only to a buildable spec (a real future PP-688 §11)?

Read in full per assignment: `00_grounding/02_prose_render_stack.md`; the entire
`designs/audit/2026-06-28-narrative-state-articulation/` bundle (`00_key_io_review.md`,
`01_narrative_legibility.md`, `02_prior_art_and_methodology.md`, `03_articulation_nlg_architecture.md`);
`skills/prose-writer/references/coherence-tiers.md` (structure); `designs/world/solmund_voice_v30.md`
§18 (+ §16/§17 for the vocabulary/structure tables that feed it); `skills/prose-writer/SKILL.md`
(for the chronicler↔Certainty binding referenced but not defined in the render-stack doc).

## 1. What the proposal itself says is missing (its own §9/§10, plus doc-02 gap list)

`03_articulation_nlg_architecture.md` is explicit that it is architecture-only. Its own closing
section (§10 "Where it slots in & what stays open") lists open decisions verbatim:
> "aggregation tuning; significance/sifting recalibration; director pacing curves; realization
> home (design-repo frozen assets vs. `valoria-game` GDScript); bake granularity/count budget;
> whether sifting patterns are authored as Datalog or via an example-driven synthesizer." (§10)

§9 (oatmeal risk register) names, unresolved: Expressive Range Analysis is proposed as a
mitigation but not built; the tension between "vary on perceivable axes" and preserving
uncanny/deliberate seams (Sych) is flagged, not resolved.

§8 (offline-bake protocol) is "conceptual" only — no schema, no storage format, no worked example.

`00_grounding/02_prose_render_stack.md` (e) "Named gaps" independently confirms the same six
items, numbered 1-6, and adds: no data schema/fragment format/worked example exists **anywhere,
incl. Godot skeleton** (gap 1); "runtime-executable form of the two authoring tables… unspecified"
(gap 3, this lane's direct assignment); pacing director unbuilt (gap 4, out of scope here — see
§6 below); oatmeal/ERA unresolved (gap 5); texture-between-cut-scenes unspecified (gap 6, Q4's
job, not this lane's).

**Conclusion: graduation requires (A) a data schema + worked example, (B) the two authoring
tables made runtime-executable, (C) a concrete bake pipeline with a storage-location decision,
(D) an ERA method, (E) explicit dispositions on every §10 open item — pacing explicitly
deferred/out-of-scope, not silently dropped.** Each is addressed below.

## 2. Candidate template/slot data schema

### 2.1 Grounding for the fields

Fragment conditions must be expressible over exactly the Key metadata the substrate already
carries — `03_…` §10 states "no new required Key fields anticipated." Per
`00_key_io_review.md` §1: universal Key fields are `id, type, source_actor, emitted_at
{season_index, sub_step_index}, causes[], targets[] {actor_id, role, impact_vector,
stat_deltas}, scale_signature[], symbolic_dimensions, visibility, time_horizon, permanence,
payload`. Per `01_narrative_legibility.md` §2, the "narrative key" is exactly this metadata:
`causes[]`→connectives, `emitted_at`→ordering, `targets[].role`→grammatical roles,
`symbolic_dimensions`/`impact_vector`→axis emphasis, `significance`→length/surfacing,
`awareness`→callback foregrounding.

The four orthogonal composition factors are `03_…` §2 verbatim: slot-templates (per Key-type ×
significance-length band) ⟂ register/lexicon overlay (X/Y/Z = Coherence/TS/Spirit,
`02_prose_render_stack.md` (a)) ⟂ focalizer overlay (4 chroniclers + protagonist, P-03) ⟂
discourse/connective grammar (from `causes[]` relation).

### 2.2 Fragment record (proposed)

```yaml
fragment:
  id: string                     # stable across bakes; content-addressed recommended
  key_type: <key_type_registry_v30 type | family wildcard>   # what this fragment answers
  significance_band: [flash_5s | scene_10s | scene_15s | chronicle_paragraph]
                                  # maps to articulation_layer_v30 §3.2 (0-4/5-9/10-13) + §4 tier-3
  band:                          # the X/Y/Z quadrant this fragment was authored for
    coherence_tier: [10-8 | 7-5 | 4-3 | 2 | 1 | 0]     # coherence-tiers.md tier headings
    ts_band: [0-29 | 30-49 | 50-69 | 70+]              # coherence-tiers.md TS columns
    spirit: [high | mid | low | na]                    # "na" above Coherence 4 (coherence-tiers.md
                                                        # "Spirit axis referenced only at C4 and below")
  certainty_register: [1-2 | 3 | 4 | 5 | 6+ | na]       # solmund_voice_v30 §18; "na" if Key has no
                                                        # religious symbolic_dimensions axis
  focalizer: [protagonist | church_chronicler | hafenmark_chronicler |
              restoration_chronicler | warden_chronicler | companion | environmental]
                                  # prose-writer/SKILL.md L151: chroniclers are FIXED
                                  # Cert/TS pairs (5/0, 4/0, 2/0, 0/70+) — not independently selected
  slots: [ {name, type} ]         # see §2.3 slot types
  text: "templated string with {slot} placeholders"
  degradation_rule_ref: <id | null>   # only set if coherence_tier <= "4-3"; points into §3 table
  once_only: bool
  repeatable_guard: <flag_name | null>   # per 03_… §6 boolean micro-reactivity guard
  discourse_connectives_allowed: [because, so, but, yet, then, ...]  # subset gated by causes[] relation
  extra_conditions: [ <boolean expr over flags/armature state> ]  # beyond band/type match, e.g.
                                                                    # awareness flags, once-only state
  provenance: {baked_by: prose-writer, baked_at: <date>, source_note: <what design intent it encodes>}
```

### 2.3 Slot types

- `entity_name` — resolved from `targets[].actor_id` via the name registry (never a raw ID).
- `pronoun` — referring-expression state (name-then-pronoun, `03_…` §2.4/NLG aggregation).
- `place` — resolved location string.
- `axis_label` — resolved from `symbolic_dimensions` dominant axis → the Conviction/axis *name*,
  never a raw score (C4's "mechanical vocabulary never surfaces" ceiling, charter Q4).
- `causal_connective` — chosen from `causes[]` relation type (cause→because/so,
  reversal→but/yet, sequence→then; `01_…` §2, `03_…` §2.4).
- `time_phrase` — derived from `emitted_at`, never the raw `season_index`/`sub_step_index`.
- `chronicler_voice_tag` — which of the 4 chroniclers is speaking (only for chronicle-mode).
- `stat_delta_phrase` — a *qualitative* phrase keyed off `stat_deltas` magnitude/sign bucket
  (small/large, gain/loss), never the numeric delta itself — same C4 mechanical-vocabulary ban.

### 2.4 Condition keys (what gates fragment selection at runtime)

`key.type`, `key.targets[].role`, dominant axis of `key.symbolic_dimensions`, the live
`significance` band computed by articulation §3.2/§4.3, the *actor's* live `coherence_tier` /
`ts_band` / `spirit` (not the fragment's authored band — matching is actor-state-driven), the
world/actor Certainty value bucketed per §18, `awareness`/micro-reactivity boolean flags, and
`once_only`/`repeatable_guard` state. This is a strict subset of already-existing state — no new
Key fields, consistent with `03_…` §10's own claim.

### 2.5 Degradation-rule form (coherence ≤ "4-3")

Not a per-sentence dice roll. At **bake time**, `coherence-tiers.md` gives, per tier × TS band, an
author-weight table (e.g. Tier 10-8: Tolkien 26/22/17 across TS 0-29/30-49/50+; full tables
§"Tier 10-8" through "Coherence 0" and the Curve Summary). These weights are consumed as a
**generation budget**: the prose-writer skill authors roughly `round(weight_pct/100 × per-cell
fragment budget)` fragments in each author's voice for that (tier, ts_band) cell, plus the
Spirit-axis modifier at Coherence ≤4 (coherence-tiers.md "Spirit modifier (C4 and below)": High
Spirit +40% of combined Lispector+Beckett pool to Beckett; Low Spirit +30% to Lispector). At
**runtime**, the degradation rule is: look up the actor's live (coherence_tier, ts_band, spirit)
→ filter to fragments authored for that exact cell → select (deterministically, see §4 below).
The weight table is a **bake-time authoring-budget input, not a runtime probability
distribution** — this is itself an open decision item (§6, item recommended-default below) since
the proposal never states which.

## 3. Runtime-executable form of the two authoring tables

### 3.1 Coherence-tier weights → lexicon selection rules

Source: `skills/prose-writer/references/coherence-tiers.md`, twelve per-tier tables (Author ×
TS-band 0-29/30-49/50+) plus the Curve Summary and the Spirit modifier note. Proposed frozen
form: `lexicon_weights[tier][ts_band][author] = weight_pct` (a flat lookup table, one row per
tier×ts_band×author, 6×3×12 = 216 cells, minus the TS-gated-only rows that are legitimately 0 at
low TS). Consumption:
- **Bake time**: drives how many author-voiced fragment variants get generated per
  (key-type-family × significance-band × tier × ts_band) cell — proportional allocation, not
  verbatim per-passage quota (coherence-tiers.md: "The weighting describes aggregate tendency,
  not per-passage quota").
- **Runtime**: NOT re-consulted as a live probability (see §2.5) — fragments are pre-tagged with
  their authored tier/ts_band/spirit at bake time; runtime does exact-match lookup on the actor's
  live state. The weight table's only runtime role (if any) is as a **tie-break** when 2+
  fragments qualify for the same slot in the same cell — proposed default: deterministic
  seeded pick (seed = `key.id` + `season_index`, satisfying PP-687 §6 V4 replay determinism), not
  weighted-random, to avoid a hidden second RNG source. **[OPEN decision, not resolvable by this
  lane alone — flagged in §6.]**

### 3.2 Section-18 Certainty registers → register table

Source: `designs/world/solmund_voice_v30.md` §18 (5-row table: Certainty 1-2/3/4/5/6+ → dominant
register/voice), cross-referenced against §16 (Vocabulary Constraints: Orthodox / Suppressed-
Heterodox / Forbidden term lists) and §17 (Structural Writing Patterns: Cusan Triad, Ficinian
Cascade, Di Cicco Inhabitation, Thomas Absence, John of the Cross Paradox, Böhmean Eruption,
Pican Address). Proposed frozen form:

```yaml
certainty_register_table:
  "1-2": {voice: [Böhme, Niflhel-plain-speech], vocab_pool: suppressed_heterodox_ok, structure: [Böhmean Eruption]}
  "3":   {voice: [Thomas, early-Levertov], vocab_pool: orthodox_minimal, structure: [Thomas Absence]}
  "4":   {voice: [Di-Cicco, folk-vernacular], vocab_pool: orthodox, structure: [Di Cicco Inhabitation]}
  "5":   {voice: [Hopkins, Ficino, Eliot], vocab_pool: orthodox_full, structure: [Ficinian Cascade]}
  "6+":  {voice: [John-of-the-Cross, Teresa], vocab_pool: orthodox+heterodox_paradox, structure: [John of the Cross Paradox]}
        # requires TS 30+ per §18 row 5 caveat; else clamp to "5"
```

This is independent of the **chronicler↔Certainty binding**, which is fixed, not selected:
`skills/prose-writer/SKILL.md` line 151 — Church Chronicler (Cert 5, TS 0), Hafenmark Chronicler
(Cert 4, TS 0), Restoration Chronicler (Cert 2, TS 0), Warden Chronicler (Cert 0, TS 70+). This
matches `02_prose_render_stack.md` (a)3 verbatim ("Church Cert-5 / Hafenmark Cert-4 / Restoration
Cert-2 / Warden Cert-0-TS70+"). Runtime consumption: when a chronicle-mode (Tier-3) fragment is
needed and the content touches the religious axis, the **focalizer choice is not free** — it is
constrained to whichever of the 4 chroniclers' fixed Cert/TS pair the narrative content and
canon-overlay Certainty level calls for; the §18 register table then supplies vocabulary/
structure constraints *within* that chronicler's fixed voice. Note §18's caveat: "Canon overlay
independent of PC coherence; the PC's *rendering of* it degrades" (`02_prose_render_stack.md`
(a)3) — i.e. the Certainty register governs the *content's* register, and the PC's own Coherence
tier (§2 above) separately governs how reliably that content is rendered through the PC's frame.
These are orthogonal filters that both apply to the same fragment pool, not alternatives.

## 4. Bake pipeline steps

1. **Enumerate reachable cells** — not the full combinatorial cross-product (44 Key types × 4
   significance bands × 6 tiers × 4 TS bands × 3 Spirit states × 6 Cert bands × 7 focalizers would
   be tens of thousands of cells; `03_…` §2's whole thesis is "a product becomes a sum"). Drive
   enumeration from **which Key types actually reach Tier-2/3** per the significance function
   (`articulation_layer_v30.md` §3.2/§4.3) and **which bands are reachable together**
   (Certainty bands only apply to religious-axis Keys; Spirit only matters at Coherence ≤4; TS
   bands only matter for TS-gated content per coherence-tiers.md's "TS perception is never
   referenced in prose unless the PC has the TS to perceive it").
2. **Draft** — for each needed cell, invoke `prose-writer` (skill) offline to draft N fragment
   variants (N = a count budget — open, §6) covering: the primary case, first-class failure
   fragments (anti-passives, `02_prior_art_and_methodology.md` §A "~211 anti-passives fire on
   *failure*"), and once-only vs. repeatable variants (`03_…` §6).
3. **Audit** — each fragment checked against: (a) coherence-tiers.md's per-tier "Anti-patterns at
   this tier" list; (b) §16 vocabulary constraints (no Forbidden terms; Suppressed/Heterodox terms
   only where the register table permits); (c) **C2 literal-string lint** — no narratological
   vocabulary ("Rising Action," "arc," "convergence") ever appears in fragment text, since C2 is
   absolute and a bake-time regression is cheaper than a runtime one; (d) the prose-writer's own
   audit step (`skills/prose-writer/SKILL.md` workflow: "write beats... write... audit").
4. **Freeze** — fragments serialized to versioned, content-addressed frozen assets. **Storage
   location is an open decision** (`03_…` §10: "design-repo frozen assets vs. `valoria-game`
   GDScript") — see recommended default in §6.
5. **Validate (CI gate)** — an emit-closure analogue to the substrate's A2/A3
   (`00_key_io_review.md` §3): every (key-type × significance-band) combination the significance
   function can actually produce must have ≥1 matching fragment for every reachable
   (tier × ts_band × spirit × cert_band × focalizer) cell it can land in; flag orphan/uncovered
   cells before ship. This is also where **Expressive Range Analysis** (Compton, cited
   `02_prior_art_and_methodology.md` §C, proposed mitigation in `03_…` §9 but unbuilt) plugs in:
   compute coverage/variance stats over the frozen corpus per cell (flat 1-fragment cells flagged
   as oatmeal risk) as a required, not optional, bake gate (charter Q4 anti-oatmeal item 2).
6. **Runtime consumption** — `on_key_emitted_articulation(key)` (`articulation_layer_v30.md` §5
   callback) → significance/tier assignment (§3.2/§4.3, unchanged) → sifter/story-sifting layer
   (`03_…` §3, new) → deterministic fragment lookup (exact-match on key_type + live actor
   coherence/ts/spirit + cert register + focalizer) → slot-fill from Key payload/`targets[]`/
   `causes[]` → discourse connective from `causes[]` relation → NLG aggregation pass (collapse
   same-subject atoms, `01_…` §2) → splice → render. **Zero inference at runtime** (C1); replay
   determinism per PP-687 §6 V4 (`03_…` §8).
7. **Regression** — re-run the charter's own arc_test_batch 5-seed method (capstone req 11; charter
   anti-oatmeal item 3) against the frozen asset set whenever the corpus changes, confirming
   chronicles differ in named actors/stakes/outcomes. This doubles as the bake's acceptance test.

## 5. What "graduate to buildable spec" concretely requires (synthesis)

Beyond the schema/tables/pipeline above (which this dossier proposes as *candidates* for Jordan
to ratify or amend), graduation needs:

- **A worked example.** The charter's own capstone requirement 10 ("ARC-S07 Torben Loyalty Clock
  compiled end-to-end: typed vector + template slots + trace") IS this worked example — it is
  not a separate ask, it's the proof the schema in §2 actually closes on a real arc. No schema
  proposal is buildable until at least one arc is hand-compiled through it.
- **A concrete aggregation/discourse rule set**, not the hand-wave "aggregation tuning" §10 open
  item — needs an actual small rule table (same-subject-same-window → conjunction; cross-subject →
  new sentence; etc.), even a provisional one, or the realizer has no discourse-planning stage at
  all.
- **A storage-location ratification** (design-repo vs. Godot-native) — blocks knowing what format
  the frozen assets take and what the CI gate in §4 step 5 actually validates.
- **An ERA method definition** — currently just a named risk (`03_…` §9), not a procedure; §4
  step 5 above is this dossier's candidate procedure, needs ratification.
- **An explicit, loud disposition on the pacing director (D11)** — CLAUDE.md §"Merging a PR
  ratifies..." principle applies by extension: if this graduation pass does NOT resolve pacing,
  that must be stated as a held-back exception, not silently absent from the graduated spec
  (`03_…` §7 already defers it; graduation must carry that deferral forward explicitly, not drop
  it).
- **Resolution (or explicit non-blocking flag) of the `mechanical.scene_entered` ownership
  conflict** (charter substrate contract: "scene_slate vs `game_director`, [OPEN — Jordan]") —
  this determines who calls the realizer's entry point and is a dependency, not something this
  lane can resolve, but graduation should name it as a blocking prerequisite for Phase 5a wiring.
- **A CI conformance rule per invariant** (charter substrate contract: "a CI-checkable rule per
  invariant, each living once in `tools/`") for at least: fragment-coverage closure (§4 step 5),
  the C2 literal-string lint (§4 step 3c), and replay-determinism (same Key log → same narrative
  state).

## 6. Open decisions the proposal lists (§8/§9/§10) — enumerated with recommended defaults

From `03_articulation_nlg_architecture.md` §10 ("Open decisions (deferred)") verbatim list, plus
§8/§9 items folded in:

1. **Aggregation tuning** — [structural, not just calibration] Recommended default: same-subject
   atoms co-occurring in one significance window collapse via simple conjunction/subordination
   ("and"/"then"/relative clause) per Reiter & Dale (`02_…` §C); escalate only cross-subject
   aggregation to a case-by-case authored rule. Needs Jordan ratification of the rule table, not
   just the principle.
2. **Significance/sifting recalibration** — Recommended default: do **not** touch the existing
   Stage-10-validated `articulation_layer_v30.md` §3.2 formula; the new story-sifting layer
   (`03_…` §3) is additive (Datalog correlation patterns over `causes[]`/`targets[]` overlap,
   temporal windows) sitting *above* the unchanged significance score, not a replacement.
3. **Director pacing curves (D11)** — Recommended default: **explicitly out of scope for this
   graduation pass.** Not required by any of the charter's 12 capstone requirements (none name
   pacing-curve tuning). Track as a distinct future PP-688 §12 addendum; state this deferral
   loudly in the graduated spec per §5 above, not silently.
4. **Realization home** (design-repo frozen assets vs. `valoria-game` GDScript) — Recommended
   default: **author/freeze in this design repo** as the single source of truth (mirrors
   CLAUDE.md §2's working-tree-is-truth rule and the `params/*.md`→Godot pipeline pattern
   in CLAUDE.md §5), export/transpile to a Godot resource format at Phase 5a build time. Avoids a
   second hand-transcription drift surface on top of the one CLAUDE.md §5 already flags for
   numbers.
5. **Bake granularity/count budget** — Recommended default: start at ~3-5 fragment variants per
   reachable cell (not per full cross-product — see §4 step 1), expand only where the ERA gate
   (§4 step 5) or playtesting surfaces perceived repetition. This is explicitly [OPEN — Jordan
   tuning] on the exact number; the *structural* decision (variants-per-reachable-cell, not
   variants-per-full-product) is what needs ratification, the count itself is calibration.
6. **Sifting patterns: Datalog vs. example-driven synthesizer** — Recommended default: **Datalog-
   style authored rules** (matches the Felt/Winnow precedent `02_…` §C already cites as this
   design's own methodology, and is inspectable/CI-checkable — consistent with CLAUDE.md §8's
   "every rule lives once, in `tools/`" invariant). An example-driven synthesizer would
   reintroduce an opaque, non-authored decision surface in tension with C1's determinism intent
   even though it wouldn't itself be a runtime LLM.
7. **(§9) Expressive Range Analysis** — currently unbuilt; recommended default is §4 step 5's
   coverage/variance procedure, promoted to a required (not optional) bake gate per charter
   anti-oatmeal item 2.
8. **(§9) Specificity vs. sanded seams** — no structural resolution possible; recommended
   default is an authoring guideline (preserve deliberate "seams-laid-bare" beats per Sych,
   `01_…` §5) enforced as prose-writer QA judgment at audit time (§4 step 3), not a mechanical
   rule.

## 7. Things this dossier deliberately does NOT decide

Per charter method rules: numbers/counts above are calibration ([OPEN — Jordan tuning]), not
structure — the schema shapes, table conversions, and pipeline steps are the structural proposal;
the fragment counts, tie-break RNG mechanism choice, and exact aggregation rule wording are
flagged as needing Jordan's explicit call, consistent with §6's per-item flags. This dossier does
not attempt Q4's texture-between-cut-scenes gap (`02_prose_render_stack.md` (e) item 6) or the
pacing director (item 4) — both are named out of scope for the NLG-schema lane by the charter's
own gap list, and pacing is explicitly recommended deferred (§6 item 3 above).
