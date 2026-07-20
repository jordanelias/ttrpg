# Dossier — Articulation Layer (PP-688)

Lane: articulation dossier. Read: `designs/articulation/articulation_layer_v30.md` (364 lines, full read).
Grounding read: 00 charter, 01 lineage, 02 interdependency map, 03 threadwork surface.

## 1. What the file is

Three tiers: Tier 1 protagonist UI lens (Concern queue, Memory salience, Bonds/Knot/Belief/
Inspiration register, chronicle search-bar §2.5); Tier 2 trigger ruleset — 10 Key-type conditions
(§3.1 table) each firing a 5–15s cut scene scored by a `significance()` function (§3.2) with an
"unarticulated weight" anti-starvation accumulator (§3.3); Tier 3 annual Chronicle (§4) — top-N
Keys by universal significance, 5 paragraph types (§4.4). §5 wires it as a universal Key-stream
subscriber (`consumes: {type: "*"}` per `module_contracts.yaml` L768); `emits: []` (L769) — a pure
sink. Stage 10 sim (`designs/audit/2026-05-01-stage-10-validation/02_articulation_evaluation.md`)
ran the (then 8-trigger) battery A1–A6, all PASS, incl. determinism (A5, hash match) and A6
cross-faction clustering decision support (corr +0.937). No `tests/coverage_matrix.md` entry exists
for articulation (grep, zero hits) — the sim above is a one-off audit artifact, not CI.

## 2. Coverage of "canonical collision moments"

§3.1 explicitly covers: coup (#2), succession (#3), covert-betrayal-exposed (#5), peninsular-strain
shock (#8), cascade-cluster formation (#9), belief revision (#10), Knot formed/ruptured (#6/#7),
scar acquired (#1), mission shift (#4). It does **not** cover `scene.battle_concluded` (siege/mass-
battle conclusion) or `scene.investigation_resolved` (trial/verdict) as explicit §3.1 triggers —
yet both are registered consumers of articulation per `key_type_registry_v30.md` §7 (L699, L721)
and §6.4 of this very file claims "`scene.battle_concluded` (existing) already triggers Tier 2 cut
scene." No such rule exists in §3.1's 10-item table. This is an internal contradiction, not merely
an absence — the doc asserts an already-implemented trigger the doc's own canonical ruleset does
not contain. Siege-fall, named explicitly in my brief, is exactly this gap.

Zero mentions of Thread, Coherence, Calamity, Gap, Dissolution, or Rendering Crisis anywhere in the
file (grep confirms) — matches grounding 03 §3's flagged silent juncture verbatim ("no Key/trigger
for Gap manifestation, Rendering Crisis, or Dissolution witnessing... narratively load-bearing per
ED-681"). I found no dedicated ED ticket for this specific gap (searched `editorial_ledger.jsonl`
for "articulation"; only ED-785/841/842/936/1030 hit, none address the threadwork silence) — so
tag **KNOWN-UNTRACKED**, not KNOWN-TRACKED, contra a naive read of ED-911 (that ticket is about
`combat_engine_v1`'s own resolver, not articulation's rendering of thread events).

Victory-condition era transitions (Post-Calamity MS=0, Phased Occupation IP=100, Anarchy
all-dissolved — `victory_v30.md` §5, GD-1-adjacent) are **UNKEYED**: `module_contracts.yaml` L679
states directly "articulation is blind to era changes via the Key stream." This is tracked —
**ED-1006** (open) lists "victory era transitions" among 4 unkeyed CANONICAL/DESIGN systems as
registry SS10 candidates. New scope I'm adding: ED-1006 frames this generically as an unkeyed-Key-
type problem; the sharper articulation-specific framing is that the one layer whose entire mandate
is "make collisions visible as story" cannot render the game's own endgame-adjacent state
transitions at all.

## 3. Anti-starvation mechanism does not do what §3.3 claims

§3.3 prose: "if a Bonded NPC accumulates many low-stakes Keys with no cut scene fired, eventually a
routine Key triggers a higher-significance cut scene." But the only emission gate is
`matches_trigger_ruleset(key)` (§5 pseudocode, L256); `unarticulated_weight` is consumed purely as
an additive term inside `significance()` (§3.2, `accumulated_narrative_weight`) — it can only raise
the *significance score of an already-firing* trigger, never cause a non-matching Key to fire one.
A background Bonded NPC whose Keys never intersect one of the 10 §3.1 types can accumulate
unboundedly and will *never* receive a cut scene under the stated mechanism. This reads as a
genuine spec/implementation gap inside the canonical doc, not an intentional simplification (no
`[ASSUMPTION]` or Jordan-vetoable flag on it, unlike §6.4's combat_resolved note at L298).

## 4. Zero mechanical emission — sink is real, "deliberate vs missed" is undetermined

Confirmed: `emits: []` (module_contracts L769), and interdependency map (02) lists "Articulation =
universal sink... emits nothing back into mechanics" as edge #11 — this is the grounding doc's own
prior finding, so **KNOWN-TRACKED** (cite grounding 02 edge 11), not novel. Extension I add: the
repo has an NPC Renown/Standing track (`npcs/npc_behavior_v30.md` — Renown/Standing table L~428)
that a "chronicle becomes legend NPCs remember" loop could plausibly feed (would satisfy P-14's
inseparability-in-every-mode spirit and Ω's autonomous-world clause), and §4.6 frames Tier 3 only as
"diagnostic and replay value" with no explicit statement rejecting a mechanical feedback loop. I
found no doc arguing FOR the sink as deliberate design (vs. simply unbuilt) — flag intent gate
UNDETERMINED, Jordan call.

## 5. Status self-contradiction (backwards/currency)

Same file carries four status markers that don't agree: header comment L1 "[CANONICAL:... promoted
from PROVISIONAL]"; L2 "STATUS: PROVISIONAL"; L6 "## Status: CANONICAL"; L9 "**Status:**
PROVISIONAL"; L363 footer "End spec. PROVISIONAL pending ratification." `CURRENT.md` L33 lists the
file with zero status annotation (unlike sibling rows that carry inline CANONICAL/PROPOSED notes),
so the index does not resolve the ambiguity. Per CLAUDE.md §1, `CURRENT.md` + a doc's own `##
Status:` line are the only currency authority — here they disagree with each other and with the
same doc's own competing markers.

## 6. Decision points actually held by the player in THIS layer

- Belief/Inspiration authorship (chargen + revision, §2.4): player writes 3–5 Belief statements +
  Inspiration arcs; engagement drives +2/+1 significance bumps (§3.5). Real authorial choice with
  downstream mechanical weight on what gets rendered. **Moderate.**
- Chronicle search-bar query (§2.5): pure retrieval, no state change. **Thin.**
- Concern queue / Memory salience / Bonds-Knot register (§2.1–2.3): informational only, not
  decisions — they inform choices made in OTHER subsystems (fieldwork, DA). **Degenerate** as a
  decision surface in this layer specifically (appropriate for a UI/rendering layer, but worth
  naming so the North-Star choice-density read isn't miscounted against this subsystem).

## 7. North Star / Q / legibility

Choice density: **thin** — by design this is a renderer, not a decision generator; it should be
judged on legibility service to OTHER subsystems' collisions, not on generating its own choices.
On that test it is uneven: strong for faction/succession/combat-adjacent collisions (dense, sim-
verified trigger coverage), silent for Thread collisions, and internally contradictory for siege/
battle conclusions and blind to victory-adjacent era transitions — exactly the moments a "renderer
of emergence" exists to catch. Q-elegant: significance formula restates cleanly after one read
(pass). Q-smooth: composes as declared (universal subscriber, O(1) callbacks) but the trigger-table
vs. §6.4 claim divergence is a smoothness violation between two sections of the same doc. Q-robust
dramatic-legibility test: **partial** — from this subsystem's state alone (Tier 1 Concern queue +
Tier 2 fired cut scenes + Tier 3 chronicle) a designer can answer "whose position is at risk" and
"what does each actor want" reasonably well for factions/NPCs with fired triggers, but cannot for
actors whose Keys never intersect the 10-trigger set (§3.3 gap) or for Thread/Calamity-adjacent
threats (zero surfacing) — so legibility is real but has blind spots correlated with exactly the
collision types named in my brief.
