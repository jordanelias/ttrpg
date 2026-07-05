# S3 — Q4: How narratives are made present for the player (master section)

## Status: PROPOSED (spec-section draft, render lane, 2026-07-05)
## Lane: IN · Charter: `00_engine_charter.md` Q4 (L107–135) · Spine: Architecture B, layer **L5 Render** (`synthesis.md §1, §6`)

This section drafts the L5 (Render) master surface of the Arc-Vector Engine plus the parts of
L3 (Schedule/ration) that are player-facing presentation. It graduates the deterministic NLG
realizer (`03_articulation_nlg_architecture.md`, drafted as PP-688 §11) and completes the
articulation trigger table (ED-IN-0004), riding the existing Key substrate and the
`articulation_layer_v30` runtime socket. Every mechanism cites a canon head or is tagged
`[UNGROUNDED]`. Numbers tagged `[OPEN — Jordan tuning]` are calibration, not structure.

**Binding constraints (charter L24–41):** **C1** authored-templates-only, no runtime LLM
(`02_prose_render_stack.md (c)` quoting `videogame_mode_spec.md §0`). **C2** no narratological
surfacing — the doc-12 veto is standing (charter L28–30). **C3** the engine books venues, never
owns resolution. **C6** the four ED-681 Rendering-Crisis beats must render (`threadwork_v30 §3.7`).
**C7** never railroads; foreclosure only via arc events, surfaced afterward.

---

## Q4.1 — Surface map (four surfaces + texture)

Five presentation surfaces, four of them lifted directly from the CANONICAL articulation layer
(`articulation_layer_v30 §1`), the fifth (texture) new to close the immersion-audit gap
(`02_prose_render_stack.md (e).6`).

| Surface | Home | Mode | Interruption? | What it carries |
|---|---|---|---|---|
| **Tier-1 ambient lens** | `articulation_layer_v30 §2` | always-on UI, never modal | never | Concern queue, Memory salience, Bonds/Knot/Belief/Inspiration registers, chronicle search-bar (§2.1–2.5); **texture demotion destination** (Q4.7) |
| **Tier-2 cut scenes** | `articulation_layer_v30 §3` | 5–15s engine-rendered moment | **the ONLY interruption medium** (charter L109), rationed by the director (Q4.7) | a significant non-protagonist beat, focalized |
| **Tier-3 chronicle** | `articulation_layer_v30 §4` | annual, omniscient, searchable | never (retrospect) | year summary; Top-N beats by universal significance (§4.3) |
| **Texture-between-scenes** | Tier-1 sub-channel (NEW) | ambient, non-modal | never | rumor / overheard / documents / Thread-Reads — the demoted-arc destination and the trail medium (Q4.4) |
| **Scene slate** | `player_agency_v30 §4` (demoted to candidate-gen, `synthesis.md §5`) | the venue where narrative becomes **play** | player-elected | arc-tagged scene opportunities the player spends 3–5 scene actions on (§4.3) |

The first three are *watching* surfaces; texture and the slate are *participating* surfaces
(Q4.3). Cut scenes are the only medium that seizes control — everything else is either always-on
ambient (Tier-1/texture), retrospective (Tier-3), or player-elected (slate). This directly
honours the charter's "Tier-2 … ONLY interruption medium" and "Tier-1 … never modal" (L109).

### Information-class routing per surface per register

Which surface a beat reaches is the significance/rationing decision (Q4.7). *How* it reads once
it reaches a surface is the realizer's register selection (Q4.6), keyed to two orthogonal
modulation axes the corpus already defines:

- **Coherence** (`threadwork_v30 §3.3`, 10→0) selects the author-weighting band that shapes the
  protagonist-focalized prose — the six bands of `coherence-tiers.md` (Stable 10-8 … Rendering
  Crisis 0). This governs *protagonist-frame* surfaces (Tier-1, slate scenes focalized through the
  PC, cut scenes with the PC present).
- **Certainty** (`params/core.md §Certainty Track` PP-551; register table
  `solmund_voice_v30 §18`) selects the religious-register vocabulary and, for chronicle-mode,
  **which of the four canonical chroniclers** focalizes (Church Cert-5 / Hafenmark Cert-4 /
  Restoration Cert-2 / Warden Cert-0 TS-70+, `prose-writer/SKILL.md:151`). This governs Tier-3
  and any ecclesiastical content on any surface. Certainty is a canon overlay independent of PC
  Coherence; the PC's *rendering of* it degrades separately (`02_prose_render_stack.md (a).3`).

Both are inputs to the realizer's fragment-selection band (Q4.6.1), never surfaced as numbers
(the UI-ceiling rule: "my Faith is shaken," not "Certainty −1", charter L131–132).

---

## Q4.2 — Venue matrix and the no-popup rule

**Hard rule (charter L116):** every beat renders **AT a location, THROUGH a venue, or IN the
chronicle** — no modal dialog divorced from place. A cut scene is a *moment shown at a place*
(`articulation_layer_v30 §3.4`: "Local environmental state (scene location, time, present
actors)"), never a free-floating popup. A played beat is hosted by the subsystem engine that owns
its resolution (C3 — the engine books the venue, the ordinary engine resolves).

| Beat class | Hosting venue (subsystem engine that resolves it, C3) | Surface |
|---|---|---|
| Social/political contest | contest proceedings (8 × 4 games) | slate scene |
| Personal combat | duels / General Duel | slate scene |
| Thread operation | anchoring / **the four Rendering-Crisis beats** (`threadwork_v30 §3.7`) | slate scene / cut scene |
| Investigation | fieldwork trails / case board | slate scene (the trail consumer, Q4.4) |
| Mass battle | pre-/aftermath framing | cut scene + slate |
| Settlement governance | governance events | slate scene |
| Knot/Bond scene | fieldwork socializing venue | slate scene |
| Witness-mode observation (ED-761) | the mandatory scene the player did not personally attend | cut scene (watching) |
| Retrospect / convergence echo | chronicle | Tier-3 |
| Travel (thinnest — ED-694 residue, charter L116) | flagged as the weakest venue; renders as texture between provinces (`player_agency_v30:183`) | texture |

Venue-specific interaction shapes follow the contest-walkthrough model (charter L118, ED-IN-0005
policy). The realizer never invents a venue: `payload.direction` names the causal beat, the
casting resolver (L4) names the actors, and the venue is the resolving subsystem's own scene —
the realizer only supplies the prose skin (Q4.6). **Conformance rule `beat-has-venue`:** every
booked beat carries a non-null `venue` field resolving to a subsystem engine or `chronicle`; a
beat with `venue = null` is a compile-time error (capstone #7: every beat's venue labeled).

---

## Q4.3 — Watching vs participating, and the major-arc playable-beat guarantee

**The distinction (charter L119–121):** cut scenes, chronicle, and witness-mode (ED-761) are
*watching*; slate scenes and texture are *participating*. Spectator surfaces still carry casting
hooks (a cut scene can end on a slate candidate — "you could go there").

**The guarantee (charter L120–121):** every major arc keeps ≥1 open intervention point until it
converges, and routes through ≥1 playable scene. This is what makes a major arc a *game* and not
a cutscene reel.

**Offer-not-outcome (resolves the rubber-band hazard — adversarial M12).** The guarantee is
satisfied by a window having been **OFFERED**, never by the player taking it. This is forced by
Q1: "ignoring a summons is remembered, never a pause; arcs proceed autonomously" (charter L49–54).
The lifecycle FSM/clock advances **on schedule regardless of participation** (`synthesis.md §1
L1`); an all-ignored major arc still converges on time. Enforcing the guarantee by *holding* an
arc pre-converging until the player participates would be a pause = a rubber-band = the railroad
C7 forbids. The invariant therefore counts *offered* windows, never *taken* windows.

> **Conformance rule `watching-participating`** (charter Q4 headline test, `synthesis.md §10.6`):
> for every arc with `tier ∈ {major}` (taxonomy per charter Q3 L89), across its lifecycle
> `seeded → converging`, the count of beats whose `venue` is a *participating* surface AND whose
> `payload.participating_actors` includes the PC (or a tie-adjacent actor, L4 casting) must be
> **≥ 1** at the moment of the `converging` transition. The rule counts **offered** slate
> candidates / fired summonses, not attended scenes. A major arc that reaches `converging` having
> only ever produced cut scenes / chronicle lines (all-watched) is a **compile+runtime failure**.

**Engagement-window divergence (resolves the illusory-choice hazard — adversarial M9).** The
charter's anti-railroad proof requires that "a different choice at each engagement window
measurably changes trajectory" (L54). The watching/participating rule guarantees a window is
*offered*; it does **not** by itself guarantee the window *matters*. An FSM whose participated
win/lose branches collapse to the same successor state is a railroad that passes
`watching-participating`. A second rule closes it:

> **Conformance rule `engagement-window-divergence`** (NEW, closes adversarial M9): every
> `activity_mode ∈ {edge_triggered_retryable, convergence}` vector with the PC in
> `payload.participating_actors` must expose **≥2 participated-outcome classes** that map to **≥2
> distinct `lifecycle.state` successors OR ≥2 distinct `pressure_effects[]` sets**. A window whose
> outcomes collapse to one successor is flagged **illusory-choice at compile** and must either
> gain a divergent branch or drop the PC from `participating_actors` (demote to watched). This is
> the structural form of capstone #3 (participated outcome changes the arc's next stage).

---

## Q4.4 — Trails

**Every foregrounded beat leaves a followable diegetic trail** (charter L122–123): gossip,
witnesses, documents, Thread-Reads. Mechanically the trail IS the `causes[]` walk (PP-687 §5.4
causal graph; `articulation_layer_v30 §2.2` already exposes the "Why? — backward walk through
CAUSAL_GRAPH") rendered as in-world media rather than a debug view. A trail is not a new data
structure: it is the same `causes[]` chain the chronicle search-bar walks (§2.5), surfaced as
texture (Q4.1) — an overheard remark, a seized ledger page, a Thread-Read residue.

**Investigation is the natural trail consumer** (charter L123): the fieldwork case board
(`player_agency_v30 §4` / fieldwork venue) is the participating surface that *reads* trails —
following a `causes[]` chain toward a foregrounded beat IS a played investigation scene. This
gives texture a gameplay destination: a rumor (watching, Tier-1) becomes a lead the player can
*pursue* (participating, slate) — the immersion-audit "connective tissue" the cut-scene-only model
lacked (`02_prose_render_stack.md (e).6`).

Trail rendering obeys the same determinism ruling as all render (Q4.6.6): a trail fragment is
selected as a pure function of the `causes[]` Key metadata, never a random draw.

---

## Q4.5 — Showing vs telling

**Showing carries the present; telling is reserved for retrospect** (charter L124). Concretely:

- **Showing** = Tier-2 cut scenes (present-tense moment, `articulation_layer_v30 §3.4`) + slate
  scenes (played present) + texture (ambient present). Present-tense, focalized, at a venue.
- **Telling** = Tier-3 chronicle (`articulation_layer_v30 §4.2`, omniscient annual voice). Past,
  summarizing, searchable.

This maps onto the realizer's output-mode dial (`03_articulation_nlg_architecture.md §4`): default
**ready-to-hand** (show via Tier-1/UI/observable action, no prose generated) and escalate to
authored prose only at sifter-flagged **breakdown** beats. Showing is the default; telling is the
annual roll-up. A convergence is *experienced forwards* as pressure and choices (showing, via the
slate scenes its constituent vectors book) and *recognized backwards* as story (telling, via the
chronicle `causes[]` walk) — the charter's PLOT clause under the doc-12 veto (L100–104).

**Mandatory foreclosure render (resolves the silent-foreclosure hazard — adversarial M10).**
C7 requires foreclosure be "surfaced afterward in chronicle … never silent" (charter L41, L78).
Total-accounting alone does not satisfy this: a foreclosure `CONSUMED-INTO-STATE` is *accounted*
yet never *rendered*. Two rules close it:

> **Rule `foreclosure-via-arc-event`** (charter L41, L78): a `stakes_tags:[foreclosure]` lifecycle
> transition may fire **only** from `activity_mode ∈ {edge_triggered_once, edge_triggered_retryable,
> convergence}` — never from `clock_escalation` or `level_triggered`. A passive clock crossing a
> foreclosure threshold (e.g. ARC-S07 Loyalty ≤ 2 → Mandate −2, `01_arc_corpus.md (b)`) must first
> raise an edge-triggered arc event; the clock alone may not foreclose silently.

> **Rule `foreclosure-must-render`** (NEW, positive-surfacing check distinct from
> discard-with-reason logging): every foreclosure transition MUST emit a Tier-3 chronicle beat
> (charter L78 "surfaced afterward in chronicle"). This is asserted positively — the total-accounting
> linter (`synthesis.md §10.3`) confirms the Key is not dropped; `foreclosure-must-render` confirms
> it is *rendered*, not merely consumed. Almud's Arc A is the exemplar (charter L78).

---

## Q4.6 — The prose REALIZER (graduation of PP-688 §11)

Graduates `03_articulation_nlg_architecture.md` from architecture-only to a buildable PROPOSED
spec, filling the single deterministic socket `on_key_emitted_articulation(key) → emit_cut_scene(
key, sig)` (`articulation_layer_v30 §5`). The realizer is **select → substitute → splice** over a
frozen offline bake — zero runtime inference (C1). It closes the ED-IN-0004 render half and C6.

### Q4.6.1 — Template/slot schema (closes `02_prose_render_stack.md (e).1`)

The realizer composes four **orthogonal** factors (`03_articulation_nlg_architecture.md §2` —
"compose, don't multiply"; a product becomes a sum). A rendered beat = one slot-template ×
lexicon overlay × focalizer overlay × discourse connectives.

```
fragment:
  id
  key_type              # from key_type_registry_v30 §9 (the render-reaching subset)
  significance_band     # flash (5-10s) | scene (10-15s) | chronicle_paragraph
                        #   — the 2 authored render-STYLES of articulation §3.4, NOT the
                        #     3 numeric length tiers of §3.2 (dossier_content_economics)
  band:                 # the coherence/TS/spirit selection cell
    coherence_tier      # 10-8 | 7-5 | 4-3 | 2 | 1 | 0  (coherence-tiers.md)
    ts_band             # 0-29 | 30-49 | 50+           (coherence-tiers.md column heads)
    spirit              # high(5-7) | mid(3-4, free) | low(1-2)  — audible only at Coherence ≤4
  certainty_register    # 1-2 | 3 | 4 | 5 | 6+  (solmund_voice_v30 §18) | na  — see fork 6
  focalizer             # protagonist | church_chronicler | hafenmark_chronicler |
                        #   restoration_chronicler | warden_chronicler | companion | environmental
  slots: [{name, type}] # type ∈ entity_name | pronoun | place | axis_label |
                        #   causal_connective | time_phrase | chronicler_voice_tag |
                        #   stat_delta_phrase  — ALL resolve to qualitative/named output,
                        #   never a raw ID or number (C4 mechanical-vocab ban, charter L131)
  text                  # the authored fragment with slot markers
  degradation_rule_ref  # for low-Coherence bands (§5 authored degradation, not corruption)
  once_only / repeatable_guard   # callback re-fire control (§6 micro-reactivity)
  discourse_connectives_allowed  # cause→"because/so", reversal→"but/yet", sequence→"then" (§2.4)
  provenance            # source Key metadata this fragment reads
```

Slots are filled **only** from existing Key metadata — `causes[]`, `targets[].role`,
`symbolic_dimensions`, `significance`, `awareness` (`articulation_layer_v30 §3.4`;
`03_articulation_nlg_architecture.md §10`: "no new required Key fields anticipated"). This is
confirmed for the render lane: no new Key *fields*. (The two new Class B *types* the detector
emits — `meta.convergence_detected`, `meta.arc_state_changed`, `synthesis.md §8` — carry only
existing-shaped metadata.)

**Worked example (capstone #10) — ARC-S07 "Torben Loyalty Clock":** the arc's
`payload.direction` "Altonian pressure converts the heir into a lever against the dynasty"
(`01_arc_corpus.md (b)`) is the slot-template source. A `state.belief_revised` on Torben
(articulation trigger #10) at Coherence 8 / Certainty na / focalizer=protagonist selects the
`flash` band, fills `{entity_name: Torben, axis_label: Loyalty, causal_connective: because,
place: the Crown court}`, and splices one 5-10s caption. The SAME arc rendered at the annual
boundary through the Church chronicler (Cert-5) selects `chronicle_paragraph` + the Hopkins/Eliot
register (`solmund_voice_v30 §18` row 5) — same beat, different surface, different focalizer,
NO new fragment authored per arc. Full end-to-end trace is the Stage-5 capstone deliverable.

### Q4.6.2 — Runtime-executable coherence-tier table (closes `02_prose_render_stack.md (e).3`)

`coherence-tiers.md` ships author-weight tables (Author × TS-band, per tier) plus the Spirit
modifier (C4 and below: high Spirit +40% of the Lispector+Beckett pool to Beckett; low Spirit
+30% to Lispector — `coherence-tiers.md` Curve Summary). At runtime the weights are **NOT a
probability**: they are the **bake-time generation budget** that decided how many fragments were
authored per (tier, ts_band, author-voice) cell. Runtime does a **deterministic exact-match** on
the actor's live `(coherence_tier, ts_band, spirit)` against pre-tagged fragments, then a
deterministic tie-break (Q4.6.6). The table becomes a compile-time coverage manifest
(6 tiers × 3 TS-bands × 12 authors = 216 weight cells, `dossier_content_economics`), consumed by
the bake's coverage-closure CI gate, not evaluated live.

### Q4.6.3 — Runtime-executable Certainty-register table (closes `02_prose_render_stack.md (e).3`)

`solmund_voice_v30 §18` is a 5-row table: Certainty 1-2 (Böhme/Niflhel plain speech) · 3 (Thomas,
faith-as-habit) · 4 (Di Cicco inhabitation) · 5 (Hopkins/Ficino/Eliot, world-is-evidence) · 6+
with TS-30+ (John of the Cross, encounter). At runtime this is a **deterministic lexicon swap**:
the fragment's clean text is authored once; the Certainty band selects the vocabulary pool +
structural pattern (`solmund_voice_v30 §16` vocab lists, §17 structural patterns) substituted into
the ecclesiastical slots. Certainty and PC Coherence are **orthogonal filters on the same fragment
pool**, not alternatives (`02_prose_render_stack.md (a).3`): §18's register is a canon overlay;
the PC's rendering *of* it degrades via the Coherence band (Q4.6.2).

> **KNOWN schema gap (not a discovery; flagged for closure):** the §18 table has **no row for
> Certainty 0** and cites an out-of-range "6+" (`dossier_content_economics`;
> `02_prose_render_stack.md (a).3` / (d)). Certainty is a 0–5 track (`params/core.md` PP-551). The
> Warden chronicler is Cert-0 (`prose-writer/SKILL.md:151`) yet §18 has no Cert-0 register row.
> The realizer graduation must either (a) add a Cert-0 register row and clamp "6+" to the TS-gated
> mystical case, or (b) map Cert-0 to the Warden chronicler's fixed profile as the register source.
> `[OPEN — Jordan]` **Default: (b)** — the four chroniclers already carry fixed Cert/TS pairs, so
> Cert-0 render = Warden profile; the "6+ with TS-30+" row stays the rare paradox case
> (`solmund_voice_v30 §2.3` note). This is a schema-closure item, not a tuning number.

### Q4.6.4 — Per-NPC overlays (a DISTINCT bake line item — resolves adversarial M8)

Charter Q3 (L96–98) requires recognizable-yet-dynamic NPCs: slow variables (Convictions core,
Resonant Styles, voice register — arc-grade changes only) vs fast variables (opinions, concerns,
projects — every season); **per-NPC lexicon overlays**. Charter Q3 explicitly forbids the
name-swap floor: "two Bonded NPCs … must not read as the same template with a name swapped in."

The overlay is bounded in **cardinality** — `npc_behavior_v30 §11.2` (PP-661) caps Active-tier
NPCs at ~35, ~30 Passive get no overlay, Background is zero-overlay by design
(`dossier_content_economics`). But it is **NOT bounded in per-unit authoring cost**. The
combinatoric collapse (`dossier_content_economics`) folds per-NPC in at ~100–175 units (3–5
micro-units × 35 NPCs) — but that figure is the **name-swap FLOOR**, not the recognizable-yet-
dynamic bar. A genuinely distinct idiolect across the ~10 triggers that fire for a given NPC is
`35 × ~10 × (a few variants)` ≈ **~1,050 units** — exceeding the entire naïve-collapsed total.

> **Ruling (adversarial M8):** per-NPC voice is a **distinct bake line item**, budgeted at
> `35 × triggers-per-NPC × variants`, NOT `3-5 × 35`. Q3 recognizable-yet-dynamic is an
> **authoring-craft cost the combinatoric factoring does not certify** (`dossier_content_economics`
> §5). "Feasible" is conditional on budgeting this line item explicitly. The existing `gm_ref`
> corpus (8 files, ~300KB) is evidence the craft is achievable at scale, but current docs do not
> budget it as a line — this section makes it one.

### Q4.6.5 — Bake protocol and volume (resolves adversarial B1)

Bake pipeline (`dossier_nlg_graduation`; `03_articulation_nlg_architecture.md §8`): enumerate
reachable cells → draft (prose-writer skill, offline LLM) → audit (anti-pattern + `solmund §16` +
**C2 lint**, Q4.6.7) → freeze (versioned content-addressed assets in the **design repo** per
CLAUDE.md working-tree-is-truth, exported to Godot at Phase 5a) → validate (coverage-closure CI
gate + **Expressive Range Analysis**, Q4.9) → runtime consume (deterministic lookup) →
regress (5-seed narrative regression, Q4.9).

**Bake volume — stated honestly against BOTH resolutions of fork 6 (adversarial B1).** The naïve
full cross-product is infeasible by any method (`dossier_content_economics`: ~5.4M literal, ~31K
even at corrected granularity). Orthogonal composition collapses it — but the headline depends on
whether Certainty gates the frozen pool:

- **IF Certainty is a runtime lexicon-swap (fork-6 FALLBACK):** ~**350–450 authored units** —
  ~86 backbone slot-templates (key-type × 2 render-styles) + ~30–50 net-new shared lexicon +
  the per-NPC line item (Q4.6.4, budgeted at its true top end, not the ~100–175 floor) + ~110
  per-arc causal-sentence templates (`dossier_content_economics`). In this resolution Certainty is
  a vocabulary substitution over an already-selected fragment, adding no frozen-pool axis.
- **IF Certainty is a frozen-pool axis (fork-6 DEFAULT, charter Q4 authority):** the frozen pool
  is gated on Certainty band, multiplying the backbone by **up to ~5–6×** → the bake is in the
  **low-THOUSANDS**, not the low-hundreds (`dossier_content_economics` §3 item 3, §5 item 2).

**This section does NOT label ~350–450 "feasible" while defaulting to the 5–6× choice.** Under the
charter-default (Certainty in the pool), the honest headline is **low-thousands**. The ~350–450
figure holds **only** under the fork-6 fallback (Certainty as lexicon-swap). Either resolution is
buildable offline (it is a one-time authoring cost, not a runtime cost), but the volume claim must
travel with its fork. `dossier_content_economics` §5's own verdict is **CONDITIONAL-feasible**
("only if two open items close" — the Certainty fork and the per-NPC line item); this section
carries both conditions, not a stripped headline.

> **Fork 6 (restated from `synthesis.md §11.6`, adversarial B1):** bake key includes Certainty?
> `[OPEN — Jordan]`. **Default per charter authority = include it** → low-thousands bake. Fallback
> if the bake cost is prohibitive = Certainty as runtime lexicon-swap → ~350–450. The determinant
> is authoring budget, not structure; but the headline number is not honest without the fork.

### Q4.6.6 — Render determinism: fragment-selection ruling (resolves adversarial M4)

Charter replay-determinism (PP-687 §6 V4) and `propagation_spec_v1 O.8` require **"same Key log →
same rendered text."** `03_articulation_nlg_architecture.md §8` *asserts* "zero inference … same
Key log → identical output" but never *constructs* the selection function. It must be ruled,
because `RNG-MODEL-COLLISION` (`propagation_spec_v1 O.5`, decision-queue item 5) leaves three
unreconciled RNG models — so "which stream does the realizer draw from" has no canonical answer,
and a string-hash / dict-iteration-order / wall-clock / shared-`World.rng` draw would break prose
replay even when narrative state replays.

> **Ruling `render-is-pure` (NEW, closes adversarial M4):** realizer fragment selection is EITHER
> (a) **zero-randomness** — a pure deterministic function of `(key metadata, focalizer, register
> band)` with a **total-order tie-break** (Q4.6.6.1) — OR (b) drawn from a **dedicated render
> sub-stream seeded from `(campaign_seed, key.id)`**, so render draws never perturb simulation
> draws. **String-hash, dict/set-iteration order, and wall-clock selection are forbidden**
> (they violate ORD-2, `propagation_spec_v1 O.3`). **Default: (a) zero-randomness** — the chronicle
> renders at the annual boundary and MUST NOT perturb downstream simulation draws (RNG-3 per-Key
> isolation is unspecified, `propagation_spec_v1 O.5` / Open Flag O-3), which (a) guarantees by
> construction. Selecting (b) is acceptable only after RNG-3 lands.

> **Precondition (adversarial M4):** disposing of `RNG-MODEL-COLLISION` (`propagation_spec_v1 O.5`,
> RNG-MODEL-COLLISION open flag) is a **Stage-0 render-lane precondition** — the render lane cannot
> claim V4 "same rendered text" until the realizer's draw model is one of the two ruled forms and
> the three-model collision is disposed. Carried as an open flag (Q4.11).

#### Q4.6.6.1 — Total-order tie-break (shared with L3 rationing — resolves adversarial M2)

The coherence-tier weights (Q4.6.2) are integer generation budgets; among fragments matching the
same `(band, key_type, focalizer)` cell, and among arcs tied on integer salience at a rationing
boundary (Q4.7), ties are the COMMON case (integer `stakes_weight` 1-5, `significance` 0-13,
`articulation_layer_v30:131,137` over ~110 arcs). An unstable sort or set/dict-seeded selection
among ties → different rendered text / different injected scene set → V4 fails.

> **Rule `total-order-selection` (NEW, closes adversarial M2 + backs `render-is-pure`):** every
> fragment-selection and every rationing/Top-N selection sorts by a **total order** whose final key
> is a unique id — e.g. `(salience DESC, tier_rank, arc_vector.id ASC)` for rationing;
> `(band-match, significance DESC, fragment.id ASC)` for fragments. `arc_vector.id` and
> `fragment.id` are unique, so the order is total. **Unstable sort and set/dict-seeded selection are
> forbidden.** Applies to `articulation_layer_v30 §4.3` chronicle Top-N and §3.3 notable-individuals
> Top-N as well (both currently unspecified on tie-break).

### Q4.6.7 — C2 bake lint and convergence render treatment

**C2 literal-string lint (charter L28–30; `synthesis.md §10.4`):** because fragments are frozen
assets, a cheap regression gate at bake-audit time greps every fragment (and every
arc-lifecycle/salience state string) for narratological vocabulary — "Rising Action", "Act II",
"climax", "arc", "convergence", lifecycle state labels — and fails the bake if any surfaces. The
detector's `meta.convergence_detected` / `meta.arc_state_changed` labels are C2-internal
(`synthesis.md §8`): they drive selection but never appear in `text`. A convergence surfaces
**only** diegetically (a summons becomes a rumor; a chronicle line says what happened, never that
"an arc converged").

**Convergence render treatment (resolves adversarial M5).** The detector runs a general
cosine-similarity backbone alongside the 8 register-authored COLLISION conjunctions
(`synthesis.md §3`). A COLLISION Marker's combined pressure is an **authored** quantity "not
predictable from the constituent vectors" (`arc_register_events.md §VI`, e.g. COLLISION-C "RS +8,
IP +2, TC +2"). Wiring a cosine-detected convergence *outside* the authored set to produce a
combined pressure would **fabricate unauthored deltas** (CLAUDE.md §5/§7 anti-fabrication).

> **Rule `convergence-effect-provenance` (NEW, closes adversarial M5):** cosine-detected
> convergences **outside** the register-authored set are **RENDER/CHRONICLE-ONLY** — they carry
> **zero `pressure_effects[]`** (they may fire a Tier-2/3 beat noting the correlation, nothing
> more). Mechanical combined-pressure exists **only** for register-authored `convergence`
> arc_vectors. Every `pressure_effects[]` delta on a `convergence` vector must **trace to a
> register line** (`arc_register_events.md §VI`), checked by the conformance suite. This keeps the
> cosine backbone's generality (Q3 correlation-test) without either fabricating deltas or reducing
> mechanically-real convergence to a hardcoded whitelist of 8.

---

## Q4.7 — Beat budgets and the director contract (D11)

**The budget (charter L127–128):** per-tier season budgets sit inside `player_agency_v30 §4.3`'s
3–5 scene-action envelope (Normal: 5–7 opportunities, 4 actions; Hard: 7–9/3; Narrative: 4–5/5,
`player_agency_v30:300-302`). Articulation today fires cut scenes "whenever triggers match"
(`articulation_layer_v30 §7`, D11 explicitly **Deferred**) — no rationing. The director supplies
the missing ceiling.

**The director is a SUBTRACT-ONLY budget ceiling — NOT a tension-curve author (resolves
adversarial M7 + M13).** The charter (L128–129) and `synthesis.md §4` say the director "owns the
tension curve" and graduates `articulation §7 D11`. But `articulation_layer_v30:302-304` DEFERS
pacing precisely because "cut scenes fire whenever triggers match," and doc-10 §8.5's NOT-list
(which the charter Q3 L104–105 says **stands**) includes "no designed dramatic timing." A
scheduler that shapes *when* beats fire toward a rising-action target is the over-orchestration C7
forbids and the doc-12 §0 veto targeted (an engine imposing dramatic structure in real time). C2
non-surfacing answers *surfacing*, not *behavior*. Therefore:

> **Director contract (D11 graduation, subtract-only):** the director may only **RATION which
> already-emerged beats surface** — a **surfacing budget**, a CEILING not a floor (`synthesis.md
> §4`, charter C7). It **MUST NEVER manufacture, reorder, delay, insert, promote, or time-compress
> an underlying event to shape a curve.** Event timing stays fully emergent (the FSM/clock steps on
> schedule, Q4.3 offer-not-outcome), preserving doc-10 §8.5. The director's only operations are:
> **(1) cap** N cut scenes/season within the §4.3 envelope; **(2) demote** overflow to texture
> (Q4.1); **(3) select** which candidates fill the slate slots (via `total-order-selection`,
> Q4.6.6.1). It may only **SUBTRACT** (ration/demote), never **ADD** (insert/advance/re-time).
> The "tension curve" is at most a **read-only observation** the director may log, never a target
> it steers toward.

> **Conformance rule `director-subtract-only` (NEW, closes M7/M13):** no director operation may
> emit a beat Key, advance a lifecycle FSM, or alter a clock; the director's outputs are limited to
> `{surface_assignment, demote_to_texture, ration_drop-with-reason}`. Any director write to arc
> lifecycle or event timing is a compile-time violation.

**Salience economy and demotion (charter L96; `synthesis.md §4`).** A demoted arc's beats become
rumor/overheard/documents → Tier-1 texture, **never nothing** (total accounting). Background keeps
its dignity: re-promotable via the `articulation_layer_v30 §3.3` starvation accumulator generalized
to arcs (an arc accumulating un-surfaced weight eventually forces a surfacing). But demotion must
not railroad attention **away** from what the player is actively chasing:

> **Rule `player-pursued-demotion-exempt` (NEW, closes adversarial M14):** any arc with a **PC
> participated-outcome in `causes[]` within the last K seasons** (K = `[OPEN — Jordan tuning]`,
> default 3) is **demotion-exempt** (floored at foreground) until it resolves or converges.
> Demotion may only touch player-untouched arcs. This prevents the "CEILING not floor" ceiling from
> soft-railroading a player-chased arc down to a rumor.

**Impulsion cadence (charter Q2 L73).** Pressure arrives as choices with deadlines — diegetic
clocks, forced-choice M-6 turns (`scale_transitions §4.3.2`), refusal costs. This is the director's
*surfacing* of already-scheduled clock deadlines, not a manufactured tempo (consistent with
`director-subtract-only`).

---

## Q4.8 — Legibility acceptance criterion

**Each surface must answer ≥1 of the three dramatic-legibility questions from the screen, and all
three must be answerable at every scale** (charter L129–131). The three questions (the
dramatic-legibility triad, charter Q4) are: *what is at stake* / *who is acting and why* / *what
changed*. The acceptance criterion is a per-surface obligation:

| Surface | Answers |
|---|---|
| Tier-1 ambient | *who is acting and why* (Concern queue source Keys, `articulation_layer_v30 §2.1`); *what changed* (Memory salience, §2.2) |
| Tier-2 cut scene | *what is at stake* (axis emphasis / Conviction engaged, §3.4); *who is acting and why* (focalizer + casting edge, Q4.6.1) |
| Slate scene | *what is at stake* (the beat's stakes_tags surfaced diegetically); *who is acting and why* (why-you casting, L4) |
| Texture / trail | *what changed* (the `causes[]` remnant); leads toward *who is acting and why* (trail consumer, Q4.4) |
| Tier-3 chronicle | all three, in retrospect (§4.4 structure) |

**UI ceilings (charter L131–132):** 3–4 personal trackers (`articulation_layer_v30 §2.1` top 3-5
Concerns; §2.3 Bonds); **mechanical vocabulary never surfaces** — "my Faith is shaken," not
"Certainty −1". Enforced by the C4 slot-type constraint (Q4.6.1: `stat_delta_phrase` resolves to a
qualitative phrase, never a number) and the C2 lint (Q4.6.7).

> **Conformance rule `legibility-triad` (NEW):** every surface renderer declares which of the three
> triad questions it answers; the compile fails if any surface answers zero, or if any scale
> (personal / territory / faction / peninsula) has a triad question answerable at no surface
> (capstone: all three answerable at every scale, charter L130).

---

## Q4.9 — Anti-oatmeal: three defenses + the 5-seed narrative regression

Charter L132–135 mandates three defenses. This section states each honestly, correcting the
synthesis's over-claim (adversarial B2).

**Defense 1 — typed register vectors (STRUCTURAL only for slot-fillers, NOT for prose).** Arcs
instantiate from typed register vectors bound to specific factions/NPCs/territories
(`synthesis.md §2`; `arc_register_factions.md`). Because arc_vectors are DATA, two seeds
provably diverge in **named actors, stakes, and outcomes** — the slot-filler values differ.

> **Correction (resolves adversarial B2):** vector-as-data guarantees **slot-filler divergence**
> (proper nouns / stakes / outcome slots differ). It does **NOT** guarantee **prose
> distinctiveness**: the same `(band, key_type, focalizer)` cell + a name swap can still read as
> Compton oatmeal (`dossier_content_economics` §3 item 2: data-substitution is "good enough for a
> mechanical register, not obviously good enough for player-facing prose without additional
> arc-specific authored color"). Prose distinctiveness is **NOT structural** and must be certified
> by the ERA bake gate (Defense 2) over the 5 fixed seeds. **Arc-specific authored color beyond
> name-substitution is a distinct bake line item** (alongside per-NPC voice, Q4.6.4). The "by
> construction / capstone-satisfied" claim is withdrawn: capstone #11 is satisfied by the ERA gate
> passing, not by the vectors being data.

**Defense 2 — Expressive Range Analysis as a required bake gate (charter L133).** ERA computes
per-cell coverage/variance over the frozen fragment corpus and flags cells whose rendered outputs
cluster (`03_articulation_nlg_architecture.md §9`). **ERA is currently UNBUILT** (`dossier_nlg_
graduation` §4 step 5, §6 item 7; `02_prose_render_stack.md (e).5`). Building it is a **Stage-5
blocker** for the render lane — the anti-oatmeal capstone (#11) is NOT met until ERA runs green
over the 5 fixed seeds.

**Defense 3 — the arc_test_batch seed method as NARRATIVE regression (charter L134–135).** The
5 fixed seeds `[42, 77, 99, 137, 201]` (`01_arc_corpus.md (a)`) must yield chronicles that differ
in **named actors, stakes, and outcomes**. This is the executable form of capstone #11 (two-seed
chronicle comparison, generalized to five). It runs deterministically (given `render-is-pure`,
Q4.6.6) and its pass condition is: pairwise chronicle diffs are non-empty on the three required
dimensions AND ERA (Defense 2) reports no clustered cell.

> **Conformance rule `narrative-regression-5seed` (NEW):** bake the corpus, render the five
> seeds' annual chronicles, assert pairwise divergence on {named actors, stakes, outcomes} AND ERA
> non-clustering. This is a **Stage-5 gate**; it depends on ERA (Defense 2) existing and on
> `render-is-pure` (Q4.6.6). Until ERA is built, this gate is **red by default** and anti-oatmeal
> is **unverified**, not satisfied.

---

## Q4.10 — Deliverables (edits this section proposes)

1. **`articulation_layer_v30 §3.1` trigger-table completion** (ED-IN-0004 root,
   `articulation_layer_v30 L294-298` §6.4/ED-936 [ASSUMPTION]): add `scene.combat_resolved`,
   `scene.investigation_resolved`, the **four ED-681 Rendering-Crisis thread beats**
   (`threadwork_v30 §3.7` — C6), and the two new meta triggers. Socket `§5` untouched. Ships in
   Stage 0 (independent, `synthesis.md §7`).
2. **`03_articulation_nlg_architecture.md` → PP-688 §11 graduation**: the fragment schema
   (Q4.6.1), the two runtime tables (Q4.6.2–3), per-NPC line item (Q4.6.4), bake protocol +
   honest dual-figure volume (Q4.6.5), the `render-is-pure` + `total-order-selection` rulings
   (Q4.6.6), `convergence-effect-provenance` (Q4.6.7), the C2 lint, ARC-S07 worked example.
3. **`key_substrate_v30 §8.5` edit (resolves adversarial M15):** §8.5 L510 states verbatim
   "scene_slate: scene activation emits `mechanical.scene_entered`." If scene_entered is
   re-attributed to `game_director` (Q4.11 fork), this canonical line MUST be edited in the SAME
   PR (re-attribute emission, or split manifest-vs-lifecycle Key). Until §8.5 is edited, the
   re-attribution is a FORK, not a resolution.
4. **New conformance rules** (each once in `tools/`, `synthesis.md §10`): `beat-has-venue`,
   `watching-participating`, `engagement-window-divergence`, `foreclosure-via-arc-event`,
   `foreclosure-must-render`, `render-is-pure`, `total-order-selection`,
   `convergence-effect-provenance`, `director-subtract-only`, `player-pursued-demotion-exempt`,
   `legibility-triad`, `narrative-regression-5seed`.

---

## Q4.11 — Open flags and Jordan forks

**Render-lane forks (carry a default; never silently resolved):**

- **Fork 6 — bake key includes Certainty?** `[OPEN — Jordan]`. Default (charter authority) =
  include → **low-thousands** bake. Fallback = lexicon-swap → ~350–450. The volume headline is not
  honest without this fork (adversarial B1). (Q4.6.5)
- **Cert-0 register row** `[OPEN — Jordan]`. Default = map Cert-0 to the Warden chronicler profile;
  clamp "6+" to the TS-30+ paradox case. Schema-closure, not tuning. (Q4.6.3)
- **`render-is-pure` form** `[OPEN — Jordan]`. Default = (a) zero-randomness; (b) render sub-stream
  only after RNG-3 lands. (Q4.6.6)
- **`player-pursued-demotion-exempt` K-window** `[OPEN — Jordan tuning]`, default 3 seasons. (Q4.7)

**Charter [OPEN — Jordan] this lane does NOT silently resolve (adversarial M6 + M15):**

- **`mechanical.scene_entered` ownership** is `[OPEN — Jordan]` in the charter substrate contract
  (L148). `synthesis.md §5` relabels it "RESOLVED"; **this section restores it as an explicit
  fork.** Default (recommended resolution) = `game_director` single-source, citing `scene_timer`
  already consuming it `from:[game_director]` (`module_contracts.yaml:392-395`) — BUT this
  **contradicts** `key_substrate_v30 §8.5` L510 (which attributes emission to `scene_slate`), so
  the resolution is **incomplete without the §8.5 edit** (Deliverable 3). Carried as **held-back**
  per CLAUDE.md §2 ED-1094: it is a hard design call the merge review must ratify with the §8.5
  edit, not bundle silently. `[OPEN — Jordan]`

**Cross-lane preconditions the render lane depends on (not this lane's to rule):**

- **`RNG-MODEL-COLLISION`** (`propagation_spec_v1 O.5`) must be disposed as a **Stage-0 render-lane
  precondition** — V4 "same rendered text" is unclaimable until the realizer draw model is ruled
  and the three-model collision resolved (adversarial M4).
- **ORD-2 on convergence emission** (`propagation_spec_v1 O.3` / O.6): the detector's convergence
  dedup must be an order-preserving container (adversarial M1) — the render lane consumes
  `meta.convergence_detected` and inherits its emission order; if that order is set-seeded, prose
  replay breaks. Flagged to the detector lane.
- **Cosine ±0.40 + meaningfulness float determinism** (`articulation_layer_v30:99-101`): must be
  quantized to integer/fixed-point or a canonical summation order pinned identically in the GDScript
  port (adversarial M3, ED-1050-class port divergence, CLAUDE.md §6). The render lane's legibility
  acceptance depends on the detector's fired/not-fired decision being replay-stable. Flagged to the
  detector lane. The value 0.40 is `[OPEN — Jordan tuning]`; the arithmetic determinism is
  structure and must be ruled regardless.
- **Gate-0 / ED-1051 engine_clock** (`strategic_judgments J-2`): the tick/detect stages (Stage 2/3)
  that feed the render lane ride the temporal spine, which is `doc:null` pending ED-1051. **The
  render lane itself (Stage 0) has NO clock dependency** and may precede Gate-0; but the convergence
  beats it renders do not exist until Stage 2/3 land behind Gate-0 (adversarial M16). Flagged.
- **`pricing-preferred-over-gating`** (charter C7, L76): an unenforced authoring tag today
  (adversarial M11); a compile-time gating:pricing ratio report + a `gaps[]` justification on every
  `stakes_tags:[gating]` vector belongs to the **compile lane**, not render. Noted for that lane.

---

*End S3 — Q4 master section. PROPOSED, Jordan-vetoable.*
