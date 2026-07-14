# Per-Subsystem Discussion — Where the Gaps Are, and What Solutions Exist (v1)

## Status: FILED — 2026-07-14 · ED-IN-0064 · companion to `subsystem_synthesis_v1.md` + `gap_register_v1.md`

> A readable discussion of each gameplay subsystem: what it is, **where its gaps are** (explained, not just
> listed), and **what solutions exist** — with the specific canon or code that already backs each fix. Fixes are
> typed **[CTC]** (complete-the-chain — the surrounding built logic determines the answer; no imported mechanism)
> or **[GENUINE]** (a real design/mechanism call). **All HELD-BACK (ED-1094); leads, not verdicts** (the L0
> validation gate FAILED 1/3). Directional status per `directional_coverage_v1.md`.
>
> **Two corrections from the adversarial gate are already folded in here:** the `MS`-owner gap and `engine_clock`
> are **[CTC]**, not genuine — their fixes are determined by code/canon that already exists (see `victory` and the
> infra note).

The recurring shape across all sixteen: **the "missing" architecture is overwhelmingly unbuilt wiring on sound
logic.** Two integration hubs (`faction_state`, `npc_behavior`) absorb almost everything while both run an
unverified `[ASSUMPTION]` resolver; a cluster of CANONICAL docs (`ci_political`, `territorial_piety`, `victory`)
touch no Key at all; and the genuinely-novel surface is tiny — the strategic-turn home doc, one env event's
consumer, the first diagonal exemplar, and a deferred decay term. Everything else is registration, annotation, and
grounding work.

---

## Personal combat
**What it is.** The one *compound* module — a `CombatEngine` hosting 11 EngineModules (strike + wound ported to
Godot, armour-defeat folded in, 8 still pending), resolved on the continuous d+σ model. It has real `sim/` code and
is the only module skeletoned toward Godot.
**Where the gaps are.** Two of its three emitted Keys — `scene.combat_felled` and `scene.combat_resolved` — go
**nowhere**; they're declared but no module consumes them, so "a character was felled" is a fact the rest of the
world never hears. Its core stats (`Wounds`, `Poise`, `Initiative`, `cumulative_damage`) are **pointer-debt** — used
in the contract but not resolved to a canonical registry key, so a Godot importer can't bind them. And the Godot
spine it `extends` (`BaseEngine`, `KeyBus`, `Key`) is defined nowhere, so the skeleton can't compile.
**What solutions exist.** The dead emits are **[CTC]** — the module's own `gap_notes` already names the intended
consumers (`npc_behavior`, `faction_layer`, `articulation`); the fix is to wire them "when npc_behavior/faction_state
are next touched," exactly as the note says. Pointer-debt is **[CTC]** — register the four combat scalars against
their canonical keys (most already exist). The Godot spine is the port's Gate-0 work (`godot_conversion_strategy`),
out of scope here. *Directionally:* combat receives top-down fine (it consumes `scene.combat_strike`); its
bottom-up leg is the dead-emit debt.

## Social contest
**What it is.** The debate/persuade/threaten engine (dice-pool), mid-rebuild — the `contest_rebuild` kernel is at
`sim/personal/contest/`, Stage 4 pending.
**Where the gaps are.** Its `sim/` code is the corpus's largest import cycle — a **9-module strongly-connected
component** (`contest ↔ appraise ↔ armature ↔ dictionaries ↔ faction ↔ modes ↔ resolver ↔ rhetoric ↔ wrapper`). Its
CANONICAL head reads as **unregistered** to the currency tooling (a `canonical_sources.yaml` key-name the regex
misses). And its live feedback loop with `npc_behavior` has a damper annotated on only one side of the cycle.
**What solutions exist.** The import cycle is **[CTC-but-intentional]** — it's an artifact of an in-flight rebuild;
revisit at Stage-4 close rather than force-decoupling now. The registration miss is **[CTC]** — verify the body
`**Status:**` line, then fix the key name (same regex blind spot hits `march_layer`, `settlement_adjacency`,
`fractional_province_ownership`). The one-sided damper is **[CTC]** — mirror the Procedure-D cadence + threshold
annotation onto the `npc_behavior` side so the loop's stability is documented at both ends.

## Mass battle
**What it is.** The army-command layer (dice-pool), with real `sim/` code.
**Where the gaps are.** One emitted Key, `scene_outcome.battle_concluded`, is **fabricated** — `scene_outcome` is a
family name, not a type prefix; canon writes `scene.battle_concluded` (which the module also correctly emits). So the
contract carries a phantom edge to nowhere. Separately, `sim.provincial.massbattle` and `units` form a mutual import
cycle.
**What solutions exist.** The fabricated type is a **known no-action** — it is *already filed as ED-MB-0010*
(2026-07-13). The fix is to delete that one contract line; do **not** re-file it and do **not** render it as a real
edge (the interactive graph draws it dashed-to-orphan for exactly this reason). The `massbattle↔units` cycle is a
**[CTC]** refactor lead — break the mutual import if it isn't load-bearing.

## Threadwork
**What it is.** The magic/weaving layer (Leap + operation rolls), real `sim/thread/` package.
**Where the gaps are.** In the L0 prose graph, Threadwork is simultaneously a **hub** (heavily cited) and a
**cascade sink** — 190 citation chains terminate at it with no return path, a one-way pressure pattern. It's also
the top concentration of the struck term "Game Master" (vocabulary debt).
**What solutions exist.** The cascade-sink pattern is a **lead** to check against the Ω-d feedback principle (is the
one-way flow intended?). Vocab-debt is a **[CTC]** single-doc grep-replace (the PP-678 workflow). *Directionally,
threadwork is the most important subsystem in this whole audit:* it owns the **diagonal exemplar**. The §5.6 Thread
Echo resolver (`compute_thread_echo`) is written but has **zero callers**, and `causes[]` — the skip-scale channel —
is populated *nowhere in the codebase*. Wiring Thread Echo and populating its `causes[]` would author the **first
executable diagonal instance** in the game (**[GENUINE-small]**), after which every other diagonal becomes CTC.

## Fieldwork / investigation / knots
**What it is.** Investigate, socialize, form Knots (bonds); dice-pool; reads the whole Key stream via a `{type:"*"}`
Memory-Query wildcard.
**Where the gaps are.** Its three `sim/` modules (`fieldwork`, `investigation`, `knots`) are **import-orphans** —
nothing imports them, so they read as dead code. `knot strain` is pointer-debt.
**What solutions exist.** The import-orphans are a **[CTC]** dead-code triage — but *verify before removal*: several
may be wired by string (adapters) rather than by import. The wildcard read is **by design** (the Memory-Query API),
not a defect. Register `knot strain` **[CTC]**. Directionally healthy — up (Domain Echo `scene.gift`), lateral, and
vertical are all covered.

## Domain actions
**What it is.** The strategic-turn verb surface — the 5 `da.*` action types plus `scene.draft_da`, on the d+σ
resolver.
**Where the gaps are.** It is **doc:null** — no home design doc — and its resolver is `[ASSUMPTION]`-grade. It also
carries three `!A6` cross-scale seams (down into npc_behavior, piety_track, settlement_economy).
**What solutions exist.** This is the audit's most defensible **[GENUINE]** — but it *leans* CTC, and honestly so:
`ED-FA-0002` records that the playable verbs **already exist**, merely *fragmented* across `params/bg/core.md`,
`params/bg/faction_actions.md`, and the faction-layer resolver math. So authoring the home doc is mostly
*consolidation of existing canon*; the genuinely-new part is the strategic-turn *structure* (the domain-echo /
governance-verb spine that hangs off it). The three seams are **[CTC] annotation-debt** — populate sub-scale
`targets[]` per §12.3 (they're 3 of the 8 catalogued §12.4 seams).

## Faction state
**What it is.** The primary integration hub — Mandate/Treasury/faction-stats accounting, with d+σ for contested
resolution (ED-874).
**Where the gaps are.** It absorbs **in-13** (nearly every subsystem routes here) and is an L2 cut-vertex — yet its
resolver is `[ASSUMPTION]`-grade. That combination — highest in-degree, unverified resolver — is the single
highest-leverage grounding target in the graph. Its `Mandate↔L/PS` feedback loop with `settlement_layer` is
**invisible** to the formula auditor, because the two legs spell the quantity differently (`faction Mandate` bare vs
`faction Mandate (cross-module → faction_state)` annotated), so the cycle never closes into a detectable SCC. And
`faction stats 1-7` is pointer-debt.
**What solutions exist.** Grounding the resolver is **[CTC]** — the contested-resolution path already has d+σ
(ED-874); the accounting spine is defined; the fix is to promote it from `[ASSUMPTION]` to verified against the sim.
The invisible loop is a **tooling [CTC]** — give formula-audit a registry-key node identity so bare-vs-annotated
legs unify (the loop's damper is already real canon, settlement §1.8). Register the stats **[CTC]**.

## Faction politics
**What it is.** The Standing-ladder / coup / succession engine; its head was flipped out of doc:null on 2026-07-05
(ED-IN-0016, PP-660, a 1115-line doc).
**Where the gaps are.** Despite that large canonical head, its **contract carries no `state` block** — so the
Standing ladder, coup state, and succession machinery aren't represented as owned quantities. Its resolver is
`[ASSUMPTION]`, and it has one `!A6` seam into npc_behavior.
**What solutions exist.** Extracting the state is a **[CTC]** contract-completeness pass — the state exists in the
1115-line head; it just hasn't been lifted into `module_contracts.yaml`. Ground the resolver **[CTC]**; annotate the
seam **[CTC]**.

## CI political (Church influence)
**What it is.** The Church political-card game — stat economy + card system, a CANONICAL doc.
**Where the gaps are.** It has **zero Key integration** — `consumes:[] emits:[]`. A whole designed subsystem that
touches no Key, so nothing cross-scale can read or write the Church's influence, card hands, or pool. Its
`card hands`, `cooldown`, and `faction political pool` are pointer-debt.
**What solutions exist.** **[CTC]** — key the emitters and consumers so `CI` and the political pool radiate into the
graph (the design logic exists; only the wiring is absent). This is the same shape as the governance docket's
"lift the Church keys into the registry as an ideological-consent axis." Some of the pointer-debt (`card hands`) is
structured state — a **[design ruling]** on whether it's a registry quantity, not an automatic registration.

## Territorial piety
**What it is.** Per-territory Piety (CV) and Church Influence (CI) accounting, with a Theocracy-Unification gate at
CI=100.
**Where the gaps are.** Like ci_political, **zero Key integration** in a CANONICAL doc — it's inert. Its resolver is
`[ASSUMPTION]`. And it shares the name "Piety Track" with the *personal* `piety_track` — a three-way collision
(`territorial_piety`/`conviction_track_v30` vs `piety_track`/`conviction_track_v1`) flagged `[OPEN — Jordan]` in both
contracts. CV is pointer-debt.
**What solutions exist.** Key it **[CTC]** (parallels ci_political). The name collision is **[UNRECONCILED —
Jordan]**: do **not** merge the two nodes — they are genuinely different mechanics at different scales; disambiguate
the display name. Ground the resolver and register CV **[CTC]**.

## Settlement layer
**What it is.** The richest quantity surface in the game — Prosperity/Defense/Order, Legitimacy/Popular-Support,
their derived values (Local Economy, Garrison, Public Order, province Accord), and the saturating Mandate loop.
**Where the gaps are.** Pointer-debt on the cross-module outputs (`province Accord`, `faction Mandate`,
`Treasury income`). The much-discussed "Prosperity ×50 vs ×10" is **not** a contract collision — ×50 produces Local
Economy, ×10 produces Treasury income; they're *different outputs*, so the formula auditor correctly reports zero
multi-definition. The real ×50/×10 conflict lives only in `params/*.md` prose and is already ED-SE-0045.
**What solutions exist.** Register the cross-module pointers **[CTC]** (`W_s` is correctly excluded as a
formula-local intermediate). The prose conflict is **no-action here** — it's ED-SE-0045's, in a layer this
contract-level auditor deliberately doesn't parse. The Mandate loop's damper is real canon (settlement §1.8,
saturating + mean-reverting); the only debt is the *contract loop-annotation*, a **[CTC]** upgrade.

## Settlement economy
**What it is.** Nominally a settlement-scale economic module.
**Where the gaps are.** It is a **phantom** — doc:null, no state, no emitted Keys, `[ASSUMPTION]` resolver,
in-3/out-0 (it consumes and produces nothing downstream). It exists as a node and does no work.
**What solutions exist.** **[RETIRE]** — it's already flagged for retirement (ED-SE-0005); fold its (empty) role into
`settlement_layer`. This resolves its doc:null and `[ASSUMPTION]` flags by deletion. (It is the "16 vs 17" ambiguity
in the task's subsystem count — treated as a degenerate 17th, not a first-class subsystem.)

## Peninsular strain
**What it is.** The Hafenmark-invasion pressure spine — Turmoil and Institutional Pressure, with the Occupation
phase gates.
**Where the gaps are.** It emits `env.crisis` — which **no concrete module consumes** (only wildcard readers see
it). It carries three `!A6` seams. It's the top concentration of the struck term "Cultural Reformation." Resolver is
`[ASSUMPTION]`; Turmoil is pointer-debt.
**What solutions exist.** `env.crisis` is the sharpest orphan-emit, hedged as **[GENUINE-candidate]** but it **leans
CTC**: `peninsular_strain_v30 §2.6` defines Crisis/Collapse as settlement Order/Accord penalties, which *points at
`settlement_layer` as the determined consumer* — so the fix is likely "wire `env.crisis → settlement_layer`," not an
imported mechanism. The three seams are **[CTC]** `targets[]` annotation-debt (§12.4). Vocab-debt is a **[CTC]**
single-doc cleanup. Ground the resolver, register Turmoil **[CTC]**.

## NPC behavior
**What it is.** The integration spine — the simulated social world (beliefs, opinions, concerns, projects, arcs)
that every other subsystem feeds. In-12, out-4, an L2 cut-vertex.
**Where the gaps are.** Like faction_state, it pairs highest-tier centrality with an `[ASSUMPTION]` resolver — the
#2 grounding-leverage node. Its state (`beliefs/opinions/concerns/projects/arc state`) is **non-scalar structured
state** and un-pointered. And `scene.dialogue` has a **dual-emit attribution conflict** — the registry credits
`scene_slate`+`social_contest`, but npc_behavior's contract also claims it.
**What solutions exist.** Ground the resolver **[CTC]** (Procedures B–E are specified). The non-scalar state is a
**[design ruling — Jordan]**, left open on purpose: whether `beliefs`/`opinions`/`arc state` are registry quantities
at all is a design question, *not* an automatic registration (forcing it would silently mis-model structured state as
scalars). The dual-emit is **[UNRECONCILED — Jordan]**: assign a single canonical emitter per type.

## Piety track
**What it is.** The personal scar/crisis track — the 7 Convictions and their Resonant-Style / crisis gates.
**Where the gaps are.** Its real home doc, `conviction_track_v1.md`, is **unregistered** in `canonical_sources.yaml`
(only the *territorial* `conviction_track_v30.md` is registered — the name collision again). It shares the "Piety
Track" name (the three-way collision). Resolver is `[ASSUMPTION]`. And it is the origin of the **P2 validation
failure**: the 7 Convictions live *inline* in NPC Behavior and are cited from nowhere, so they sit at
throughline-degree 0 — structurally isolated.
**What solutions exist.** Register the home **[CTC]** (ED-IN-0048; coordinate ED-SC-0003). Disambiguate the name
**[Jordan]**. Ground the resolver **[CTC]**. The Convictions' isolation is a real finding: give them first-class doc
status or throughline substantiation so they're structurally connected, not just inline prose (this is what would
flip P2 on a rerun).

## Miraculous event
**What it is.** A rare, gated narrative-mechanical event (state_reader), resolved out of doc:null.
**Where the gaps are.** Modest — its resolver is `[ASSUMPTION]`-grade; otherwise it's cleanly wired (emits
`meta.miraculous_event` up to faction_state and laterally to npc_behavior).
**What solutions exist.** Ground the resolver **[CTC]**. No structural gap; it's a good example of a small,
well-behaved subsystem.

## Victory
**What it is.** The win-state reader and world-state era machine — Baseline / Post-Calamity / Second-Calamity /
Occupation P1–P3 / Anarchy, gated on the clocks it reads (MS, IP, CI, Turmoil, Accord, Mandate, PV, PT). GD-1: exactly
one victory path.
**Where the gaps are.** Its headline input, **`MS` (Mending Stability), has no owning module** in the 27 contracts —
the terminal Calamity/recovery machine turns on a clock no contract declares. Its era reads are pointer-debt.
**What solutions exist — corrected to [CTC] by the adversarial gate.** This is *not* the genuine gap it first looked
like. `MS` **is already ticked in the running sim**: `params/core.md` §MS Baseline Decay (PP-255) is the canonical
mechanic; `sim/peninsular/ms_track.py:59` implements `apply_ms_baseline_decay`; and `sim/peninsular/accounting.py:61`
**wires it into the Year-End cascade** (grep-verified). So the gap is purely at the *contract* layer — no
`module_contracts.yaml` module *declares* MS ownership even though the peninsular spine writes it. The fix is
**[CTC]**: add a contract owner (a `substrate_state`/peninsular module emitting `env.ms_delta`) that declares the MS
clock and points at the existing decay — a prior audit already drafted exactly this. Register the era reads **[CTC]**.

---

## Infrastructure note (context, not first-class subsystems)
The eleven infra modules are plumbing, but two carry corrected classifications worth stating:
- **`engine_clock`** — doc:null, but **[CTC]**, not genuine: its home doc **exists and is CANONICAL** —
  `propagation_spec_v1.md` (ratified 2026-07-02), whose §O.2 is literally titled "engine_clock module contract
  (retires doc:null/[ASSUMPTION])." Only the `module_contracts.yaml` pointer-flip pends ED-1051 (administrative). A
  sliver (the tick-scoped scheduler / `cascade_depth`) is genuinely new apparatus, but the temporal-spine core is
  ruled canon, already coded (`season.py`/`accounting.py`).
- The other doc:null infra (`scene_slate`, `game_director`, `scene_timer`, `audit`, `npc_memory`,
  `scenario_authoring`) are telemetry/orchestration/authoring-time — author brief homes or mark them authoring-time;
  none blocks gameplay. `campaign_architecture` is a **[RETIRE]** stub.

## The through-line
Sixteen subsystems, one story: **register the pointers, key the inert modules, ground the two `[ASSUMPTION]` hubs,
annotate the seams, and wire the handful of built-but-uncalled resolvers** — and the architecture is largely
complete. The genuinely-new design surface is small and specific: the strategic-turn home doc (leaning
consolidation), one env event's consumer (leaning determined), the **first diagonal exemplar** (threadwork's Thread
Echo), and the deferred temporal `decay()` term. Everything a rerun of this observatory would want to see flip is
CTC work the surrounding logic already determines.
