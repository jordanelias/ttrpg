# Judge lane — BUILDABILITY

## Status: SUPERSEDED (working record of the emergent-narrative-engine design effort; head RATIFIED as ../narrative_engine_design_v2_churn.md + narrative_engine_design_v1.md-as-amended + spec/churn_amendments.md, ED-IN-0011, 2026-07-05). Not independently ratifiable; retained as record. [status reconciled 2026-07-15, proposal-reconciliation pass, ED-IN-0069]
## Date: 2026-07-05 · Lane: IN · Judge lens: BUILDABILITY (cost realism, staging, ships-first, Godot typed-export, C1 bake, doc:null burden, N=necessity)

---

## 0. Lens definition & what I hold constant

Buildability asks: **can you build what each architecture specifies, at a realistic cost, and does
every component earn its existence (N)?** Sub-axes: (a) cost realism vs the content-economics
dossier, (b) staging quality / independently-mergeable increments, (c) what ships first, (d) Godot
typed-export path (charter §5 recommendation — a typed engine-params asset Godot ingests directly),
(e) C1 bake feasibility (authored-templates, offline, deterministic), (f) doc:null authoring burden,
(g) N — necessity of each component.

**Architecture-independent cost (held constant across A/B/C):** the NLG realizer bake. The
content-economics dossier is decisive — under strict orthogonal composition (NLG §2 "compose don't
multiply") the bake collapses from a naive ~31K–5.4M fragments to **~350–450 authored units**
(~86 Key-type×render-style backbone + ~30–50 net-new shared lexicon + ~100–175 per-NPC bounded
overlays [≤35 Active cap, npc_behavior §11.2] + ~110 per-arc causal-sentence templates). All three
architectures inherit this whole; it is NOT a differentiator. The **Certainty-in-bake-key
discrepancy** (NLG §8 omits Certainty; charter Q4 includes it → ~5–6× swing) is a must-resolve for
ALL three before the real bake is scoped (content-economics open-Q 1). [grounded: dossier
content-economics; 02_prose_render_stack (c)/(e)]

**Shared corpus-defect blockers (all three inherit, none can dodge):** Coup Counter is STRUCK
(ED-781, params/factions_personal.md:68) → 5+ arcs + COLLISION-A/F/G need Löwenritter-Autonomy
migration; ARC-T04 dangling+mis-cited (both ED-416 entries unrelated) → COLLISION-C un-buildable
until authored-or-struck; **temporal_window unspecified register-wide** → convergence has no
correlation window though charter Q3 names it required. These are [OPEN — Jordan] build
preconditions independent of which architecture wins. [grounded: dossier register-formalizability]

**Note:** the transport-fitness dossier is a stub ("test"/"a"/"b") — no usable transport-cost
signal; I lean on the substrate sections of each architecture instead.

---

## 1. Architecture A — Minimal Detector

**Cost realism: excellent (lowest of the three).** Three edits to existing homes (accounting.py:37-79
step-6, articulation §3.1 table, NLG graduation) + one new data file (convergence_registry.md, 8
markers) + one genuinely-new owned state (convergence_fired_set). Zero new modules claimed. It
DECLINES the ~55% of the register that is not free to compile (register dossier: ~40% needs a new
buildable field + ~15% GM-judgment-irreducible) — a real cost saving, because it only transcribes
the 8 COLLISION conjunctions, not the ~110-arc corpus.

**Staging: excellent.** 4 stages, each independently mergeable, each riding an existing home,
dependency-minimal by design. Stage 2 (articulation §3.1 completion: combat_resolved,
investigation_resolved, 4 ED-681 thread beats) closes ED-IN-0004 + C6 **cheaply and early** without
waiting on any compiler — the single best ship-first move in the whole field.

**Godot export: good, small.** 8 typed predicates + a data file — a clean, small typed-export
surface.

**doc:null burden: minimal — but this is also its buildability GAP.** It explicitly does NOT claim
game_director/scene_slate and leaves the mechanical.scene_entered ownership conflict OPEN. But the
charter substrate contract REQUIRES resolving that conflict and giving game_director/scenario_authoring
homes (charter §"substrate contract", Edges). A declines a mandatory deliverable — honest, but
incomplete against spec.

**N: leanest — but under-scopes charter-MANDATORY components.** Every component A builds earns its
existence. The problem is what it OMITS: charter Q3 names "lifecycle states (seeded→…→resolved),
persistent and queryable" as **required content**, and the substrate contract owns "arc-vector
states." A builds no arc lifecycle at all (excluded by premise). Consequence: capstones #1 (seed→
resolution across 3 rungs), #3 (participated outcome changes next stage), #8 (meaningfulness
pass/fail) are not fully demonstrable; Q2 social-ladder (family rung, factionless on-ramp) gets
nothing; Q4's "keep ≥1 intervention point open UNTIL converging" is impossible (A fires AT the
convergence instant — no converging state to hold a window open). The 8 markers are a **whitelist,
not a discriminator** → Q3 general correlation-test unmet.

**Verdict:** maximally buildable/ratifiable *for what it scopes*, but it under-scopes against
mandatory charter content. Ideal as a FIRST INCREMENT, not as THE architecture.

**Score: 76.**

---

## 2. Architecture B — Arc-Vector Engine  ★ WINNER

**Cost realism: high, and HONEST — but it is the SPEC's cost, not inflation.** B compiles
references/arcs/ (~110 IDs) into typed arc_vectors with lifecycle FSMs. Register dossier: ~45%
compile now (post trivial TC→CI/RS→MS rename), ~40% need one buildable field, ~15% GM-judgment-
irreducible. "Authoring becomes engineering, permanently" is B's central, correctly-surfaced cost.
**But charter C5 literally mandates "arcs compile from register DATA"** — B is building exactly the
substrate the charter specifies. The cost is real; it is the charter's own cost, honestly owned.

**Godot export: BEST of the three — decisive on this lens.** The register→typed-vector compiler
produces a **frozen compiled arc_vector corpus** — the direct analogue of references/engine_params/
*.json, i.e. exactly the typed engine-params asset charter §5 (and CLAUDE.md §5) says does not yet
exist and must be built for Godot to ingest numbers without hand-transcription. The arc_vector
schema IS the authoring-time↔runtime seam. This is the single strongest Godot-buildability property
in the field.

**Total accounting: cleanest.** Zero new Key types (C3) and zero new currency (C5) → the registry
"every emitted Key has ≥1 consumer" invariant holds with zero additions → capstone #9 (zero
unaccounted Keys) by design. This is a genuine buildability win: no new registry surface to audit.

**Staging: sound, higher up-front.** 6 stages; Stage 0 is a GATE (compile register + resolve the 3
corpus defects) that ships the ~45% compiling now and unblocks everything. Risk: nothing ships
before compilation works — so the cheap ED-IN-0004 render win (A's Stage 2) must NOT be trapped
behind Stage 0 (see grafts).

**doc:null burden: claims 3 homes (game_director, scenario_authoring, scene_slate) and resolves
scene_entered** — it DOES the authoring A declines, discharging charter-required substrate-contract
deliverables. More work, but it is required work.

**N: strong.** The arc-vector store + lifecycle FSM IS the concrete form of ED-IN-0003 (the
generalized per-arc lifecycle-state field, register dossier §4.1) — the charter-mandatory substrate
A omits. Every component earns existence AND is charter-required. The one N hazard: the ~15%
judgment-irreducible arcs need authored decision functions that risk C5 scripting-drift or silently
fail to fire — a real wart, but bounded and flagged.

**Verdict:** builds precisely the charter's specified substrate, with the cleanest Godot typed-
export seam and the cleanest total accounting, at a cost that is the spec's own cost honestly
surfaced. **Winner on the buildability lens.**

**Score: 85.**

---

## 3. Architecture C — Director Layer

**Cost realism: highest — and partly self-imposed.** C is a **superset of B's core**: it needs the
same generalized per-arc lifecycle field for all ~110 arcs (Stage 1) AND a convergence detector
(Stage 2) — i.e. it inherits B's full compile cost — PLUS a director superstructure (tension curve,
beat budgets, salience economy, texture scheduler, watching/participating counters, World-scope
scene-queue). Strictly more code than B for the same ED closure.

**Two new Class B Key types** (meta.arc_state_changed, meta.convergence_detected) vs B's zero —
more registry surface and more total-accounting burden (C handles it, but it is more to audit).

**Godot export: hardest.** The director's tension-curve/salience-economy is **runtime-computed
narratological state** that must port to GDScript deterministically AND is the C2-risk surface —
much harder than B's frozen-data-asset seam.

**Staging: reasonable, but highest-value Q4 items gated deepest** (director core Stage 3, texture
Stage 5). EDs close at Stages 1-2 (== B's core); C's differentiated value ships only Stages 3-6 —
slowest to unique value.

**doc:null burden: same 3-module blast radius as B + a NEW pacing_director_v1.md.**

**N: WEAKEST of the three.** ED-IN-0003/0004 close at Stages 1-2 (the B-equivalent core); the
director (Stages 3-6) is a Q4-QUALITY superstructure, not ED-closure-by-construction. It is not
gratuitous — it is the ONLY architecture delivering cut-scene rationing, texture-between-scenes, and
the watching/participating invariant, all of which are charter Q4 **required content** B under-serves
— but on a necessity axis, C spends the most to add a layer whose necessity is "Q4 presence quality,"
and it carries the **highest constraint-violation risk**: C2 leak is highest-severity (the
director's ENTIRE state IS the narratological state doc-12 forbids surfacing), plus C7 railroad
(booking-guarantee-as-floor), doc-10 §8.5 designed-dramatic-timing, and determinism fragility on the
OPEN ORD-3/ORD-4 preconditions.

**Verdict:** most ambitious, best Q4 delivery, but most expensive (B+director), riskiest (C2),
weakest necessity (superstructure over the same core B builds), hardest deterministic port.

**Score: 72.**

---

## 4. Ranking & winner

**B (85) > A (76) > C (72). Winner: Architecture B — Arc-Vector Engine.**

On buildability B wins on the two properties that matter most for THIS game (Godot, deterministic,
typed-export): the compiled arc_vector corpus IS the typed engine-params asset §5 demands, and zero
new Keys/currency gives the cleanest total accounting. Its high cost is the charter's own C5-mandated
cost, honestly owned — not architecture inflation. A is cheaper but structurally omits charter-
mandatory components (arc lifecycle per Q3; scene_entered resolution). C is a strict superset of B's
core plus a risky, less-necessary superstructure with the hardest deterministic port.

---

## 5. GRAFTS — non-winner elements the synthesis MUST keep

From **A (Minimal Detector):**
- **G1 — Early-mergeable ED-IN-0004 lane.** Ship articulation §3.1 trigger-table completion
  (combat_resolved, investigation_resolved, 4 ED-681 thread beats + the marker Key) as an
  INDEPENDENT early stage, NOT trapped behind B's Stage-0 compile gate — closes C6 + renders
  already-declared-but-dropped Keys at near-zero cost. Best ship-first move in the field.
- **G2 — C2 literal-string bake-audit lint** as the cheap frozen-asset regression gate (A names it
  most concretely; all three need it).
- **G3 — The 8 COLLISION markers as edge-triggered-once typed predicates over settled state at
  ACCOUNTING_BOUNDARY (fired-set dedup).** Keep this concrete minimal detection primitive INSIDE B's
  fuller detector — the 8 hand-authored conjunctions are ground truth; don't over-engineer them away.
- **G4 — A's honesty ledger:** declare unused transport directions (UP/DOWN/DIAGONAL) as gaps rather
  than faking them; keep the discipline of marking gaps as gaps.

From **C (Director Layer):**
- **G5 — Cut-scene RATIONING / beat budget** (charter Q4 required; B feeds a realizer but does NOT
  ration — articulation §3.1 currently fires "whenever triggers match"). Keep it as a SUBORDINATE
  budget filter over B's detector output — bounded, not the spine — to avoid C's C2/over-orchestration
  risk.
- **G6 — Texture-between-scenes scheduling**, with texture as the DEMOTION DESTINATION (total-
  accounting-clean). This is the immersion-audit gap (02 (e)6), charter Q4 required content that both
  A and B leave unaddressed. C is the only source.
- **G7 — Watching-vs-participating ratio as a CI-checkable booking invariant** — operationalizes the
  charter's "every major arc keeps ≥1 open intervention point until converging." A cannot guarantee
  it; B asserts it; C makes it a checkable counter. Keep C's operationalization.
- **G8 — The sim-VALIDATED trigger-9 cosine-similarity primitive** (articulation §3.1 trigger 9,
  cascade_fidelity_history cosine, ±0.40, corr +0.937 at the Crown/Hafenmark pair) as the GENERAL
  correlation-detector layer ABOVE the 8-marker whitelist — the buildable path to charter-Q3
  detection generality, grounded in an existing sim-validated mechanism.

Shared (B & C agree, A omits) — **resolve mechanical.scene_entered ownership** (game_director single-
sources it; scene_slate demoted to candidate/manifest generator, consistent with scene_timer already
consuming it from game_director, module_contracts.yaml:392-395). Required substrate-contract
deliverable — carry the resolution.

---

## 6. Build preconditions the synthesis inherits regardless of winner
- Resolve the Certainty-in-bake-key discrepancy (5-6× bake-cost swing) BEFORE scoping the real bake.
- Coup Counter → Löwenritter Autonomy migration [OPEN — Jordan]; ARC-T04 author-or-strike [OPEN];
  temporal_window rule for convergence (same-season / same-Accounting / N-season) [OPEN].
- Budget the ~350–450-unit NLG bake as its own line item (architecture-independent, but the
  dominant content-authoring cost — and the anti-oatmeal per-NPC/per-arc EFFORT is not certified by
  the cardinality math).
