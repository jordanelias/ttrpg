# Valoria — The Emergent Narrative Engine · Design v2: THE CHURN ENGINE

## Status: PROPOSED (Jordan-vetoable throughout; supersedes-IN-PART design v1 — v1 stays as record; the F-F/fork-8 Light-Function decision is HELD BACK from merge-ratification)
## Date: 2026-07-05 · Lane: IN · Branch: `claude/ners-audit-fable5-9cpfdz` · Companion: `spec/churn_amendments.md` (per-chapter deltas to v1's s1–s5)

**Why v2 exists.** v1 (the Arc-Vector Engine) answered *how detected story-moments reach the
player*. Jordan's critique showed that was the smaller question: the game is a **generative
churn** — character ambitions × world states × event cards × scene resolutions branching into
a combinatorially vast Key space (census: ~10³ live Key instances/season over 48 registered
types; rendered-prose space 10⁶–10⁷), probabilities propagating forward at every calculation —
and the engine's job is to harness that churn **as** an emergent story: a coherent narrative
derivable from ANY realized trajectory, at any scale, with no runtime LLM. Grounding:
`01_workings/dossier_forecast_tractability.md` + `dossier_combinatorial_census.md` (both
committed; every load-bearing number below cites one of them).

---

## §0 · The critique of v1 (kept honestly; self-authored, bias flagged)

1. **Enumerative bias** — L0 compiled arc *instances*. The register's 138 arcs (census — the
   earlier "~110" was a 25% undercount) are narrative text applied to sample trajectories
   through state graphs, collapsing to **~13 structural shapes**; v1 treated the samples as
   the content.
2. **Backward-only detection** — L2 saw settled state only; story tension is mostly potential.
3. **"What happens if no one acts" was authored, not computed** — fabrication risk at scale;
   unavailable for generated content; it is literally a forward-simulation query.
4. **The convergence whitelist** (refuter-flagged in v1's own pass) — 8 authored conjunctions
   as the entire convergence surface.
5. **No mass/imminence term in salience** — promotion keyed on accumulated past weight; a
   quiet arc about to foreclose should foreground *before* it fires.
6. **Scale untested; surfaces event-shaped** — one arc traced; nothing rendered what looms.
7. **Deepest: the pruning question unanswered.** *How does a coherent narrative come out of
   nigh-infinite combinations?* Relevance selection feeds back (lit → slate → played →
   trajectory changed) and shapes the whole narrative development — **pruning IS authorship**
   — and v1 buried the game's author inside a "salience economy" subsection.

**What survives v1 intact:** C1–C7, Key-native transport and total accounting, the tie-graph
casting rule, the venue matrix and no-popup rule, the realizer/bake concept, the one-ledger
rule, the subtract-only director discipline, the module homes (game_director /
scenario_authoring / scene_slate), and the s1–s5 chapters as amended
(`spec/churn_amendments.md`).

---

## §1 · THE INVARIANT — narrative holonomy (one stream, scale as a view)

Everything meaningful and rooted, at every level of play from smallest to largest, is a
candidate for prose and emergent arcs — and it all coheres into **a single unified narrative
stream, simply viewed at differing scale/scope**.

- **One stream, many projections.** There is exactly ONE beat stream: the lit subtree of
  Keys/beats (§4). A character's story, a household's season, a settlement's year, a faction's
  campaign, and the world chronicle are PROJECTIONS of that stream — filter by holon,
  re-render at that scope's granularity and focalizer. The per-rung prose banks (§6) are
  render granularities of one stream, never separate content systems.
- **Zoom coherence.** One Key set → the chronicle's line, the faction's paragraph, the played
  scene — identical facts, different focalization (worked example §9.2). The
  `scale_transitions_v30 §4` zoom protocol generalizes from play to story.
- **Narrative aggregate-up / distribute-down.** Story rides `propagation_spec_v1`'s
  transforms: many settlement beats aggregate to one faction-scope sentence ("the northern
  towns turned restive"); a world event distributes down as its local consequence ("the war
  reached Hafenmark as grain prices"). Aggregation templates are a first-class bank class.
- **Candidacy universal, selection scoped.** Grammar closure (§6, fixture §9-F3) means every
  meaningful, rooted event at ANY rung can enter the stream; the meaningfulness test
  (durability × tie-proximity × identity-touch, v1 s2) evaluates per-holon; the Light
  Function (§4) allocates depth per scope. *Meaningful+rooted ⇒ candidate; lit ⇒ rendered;
  scope ⇒ granularity.*

This is `holonic_container_doctrine_v1` applied to narrative itself.

## §2 · THE SUBSTRATE — the generator, not a corpus

The durable substrate is the **state graphs themselves**: clocks (registry + the census-
confirmed gaps PI and Axis-9 — real mechanics, missing rows), faction stats, settlement stats
(37 settlements × ~6), NPC tracks (~25–35 named), ambitions/projects, priority trees, event
decks (`governance_play_redesign_v1`: 7 card families, 60–100 target — **no deck code exists
yet**; the goldenfurt slice is the worked example). On that substrate:

- **Arc-vector TEMPLATES with binding slots** — the ~13 structural shapes the 138 register
  arcs collapse to (census §3), each a typed template: trigger predicates over state-graph
  FAMILIES (`clock.* ≥ θ`, `track.falling ∧ stat.≤`, convergence-conjunction, …) × binding
  slots (faction × territory × settlement × NPC × stake). The full typed schema is v1's
  (id/tier/scope/activity_mode/trigger/pressure_effects/payload/lifecycle/cross_refs/gaps —
  s2 §Q3.9), now read as the TEMPLATE grammar, instantiated at runtime.
- **The seeded pipeline mechanized** — the valoria-arc-generator method (seed → causal
  skeleton → typed vector) becomes `scenario_authoring`'s compile: templates × bindings ×
  seeds → instantiated vectors. The 138 register arcs + 8 COLLISIONs are the
  **validation/calibration set**: the compiled generator must reproduce them from their
  trigger states (fixture §9-F4) — never the content ceiling.
- **Specificity from binding at instantiation.** A template bound to THIS settlement's
  circumstances (its own stat vector, temperament, thread sites, Local Actors) and THIS NPC's
  ambition is particular by construction — how thousands of permutations stay individually
  meaningful rather than generic (anti-oatmeal defense 1, §6).
- Grammar-closed Key space: predicates quantify over the 48 registered type families —
  no enumerated whitelist anywhere (dissolving §0.4).
- Corpus defects the compile surfaced, carried loudly (v6 schedules them): Coup Counter
  STRUCK (ED-781) yet live in 6 register entries (fork 1); ARC-T04 dangling (fork 2); Torben
  Loyalty range register-vs-clock_registry conflict (fork 9); **faction count unreconciled
  4–8 across four docs** (census §1.2 — new corpus finding, needs its own ED); PI/Axis-9
  registry rows.

## §3 · THE FIELD — forward probability propagation (L1.5, the churn core)

Each Accounting, over settled state, the engine computes the forward probability field —
**a two-layer forecast** (tractability dossier verdict):

- **Layer A — analytic (near-free).** Every continuous strategic variable advances by a
  closed-form step: the dice engine gives `P = Φ((μN − (Ob−0.5))/(σ√N))` (implemented:
  `sigma_leverage.p_success`); the domain resolver's clamp bands ARE the probabilities;
  Domain Echo maps degree→delta by a zero-RNG table (`domain_echo.py`). Drift clocks (MS
  −1/yr, CI +1/season) get **exact Normal first-passage horizons** — P(threshold within k
  seasons) with no sampling.
- **Layer B — seeded ensemble (cheap, shared-code).** The discrete structural branches EV
  cannot collapse — **which action, which target, which card** (correction from the dossier:
  faction priority trees are NOT fully deterministic; GD-2 mandates only that the
  deterministic mandatory pass PRECEDES stochastic selection — `faction_action.py` draws
  action and target) — sample through the LIVE code paths via `mc_v18.run_campaign(seed,
  max_seasons)` with `season.run_season(action_callback)` as the lever-injection seam and
  `game_state.serialize_world` as the snapshot/branch point. N≈64 futures × k≈4 seasons at
  accounting cadence ≈ 10⁶–10⁷ ops, **<100 ms per Accounting on desktop** — provided scenes
  are NEVER rolled in forecast (rolling personal kernels would 10²–10³× the cost).
- **The port↔oracle discipline holds by construction**: forecast and live play share resolver
  code (conformance rule R-F1, §7); fork F-A is EV-vs-sampled *within* the shared functions,
  never a parallel model.
- **Outputs** (typed, engine-owned state): `stake_horizon{stake, P-band per k, under
  no-intervention and per player lever}` — the third legibility question, computed;
  `convergence_candidate{targets, co-spike vector, window}` — discovery over the ensemble,
  with the 8 authored COLLISIONs as priors it must reproduce (fixture §9-F4);
  `foreclosure_countdown`; `option_distribution`. Detection (L2) becomes actual + potential.
- **Honesty bounds** (also C7 protections): the forecast models venues at unconditional odds
  — per-lever conditioning is an odds/stat shift, so horizons are *"field pressure under
  average play," never a promise*; and forecast quality is bounded by the sim's own known
  gaps — **preconditions before any horizon is trusted**: the ~19 sim stubs on Layer-B paths
  (`npc_ai`, `ip_track`, `rs_track`, ~8 provincial actions), the unbuilt event deck, and a
  deterministic seeded smoke oracle for ensemble outputs (extending `sim/tests/` — the known
  degenerate ~87% win-share currently has nothing flagging it, CLAUDE.md §7). These gate
  Stage 2.5 (§8).
- **Determinism guards** (from the dossier + v1's s4): stable-key sorted iteration everywhere
  (the `ALL_PLAYABLE_15` frozenset hazard; forbid raw `set()` in marginals); **integer
  basis-point marginals** (no float-boundary nondeterminism); shared erf/Φ lookup for the
  Godot port (no `math.erf` divergence) pinned by the ED-1050-class parity harness; ensemble
  seed = `hash(canonical_key_log, accounting_index, future_index)` — never wall-clock (kill
  `mc_v18`'s `time.time()` fallback).

## §4 · THE AUTHOR — the Light Function (pruning as authorship)

Roots (world clocks) → trunk (factions) → branches (settlements, each with unique
circumstances) → leaves (characters) → capillaries (every resolution draw). **You cannot
narrate the tree; you narrate the light's path through it** — and how light falls shapes the
game's whole narrative development. v2 therefore owns the relevance function as the engine's
central object and the game's authorial voice.

- **Strictly selective (the fork-8 reconciliation, stated once, binding):** the Light
  Function **rations among candidates the churn produced. It can never inject content, shape
  an outcome, accelerate a clock, or touch resolution.** Allocation-among-given IS the
  subtract-only discipline; the director graduates as this function's scheduler, nothing
  more.
- **The coherence guarantee — a story out of ANY branch.** Three invariants hold on every
  trajectory: **(i) causal connectivity** — every lit beat traces via causes[] to lit
  ancestors or roots; the lit subtree is connected by construction. **(ii) light-inertia** —
  attention has momentum: lit threads carry a persistent priority term; an anti-strobe floor
  forbids flicker; engaged threads (player-participated) are demotion-exempt (v1 rule).
  Continuity is a property of the LIGHT, not the events. **(iii) player-rooting** —
  tie-graph proximity is a permanent weight term; the seedling grows where the protagonist
  stands. A chronicle of the lit subtree is therefore *connected, continuous, and rooted* —
  a story — whichever branch every calculation took. (Argued as the any-seed theorem, §9.4;
  regression fixture §9-F1.)
- **The selection score** (per candidate beat/thread, integer basis-points): meaningfulness
  (durability × tie-proximity × identity-touch, v1 s2) × **forecast mass** (the §3 horizons —
  the new term) × **imminence** (horizon band) × light-inertia carryover × scale-allocation
  weight. Quiet-meaningful-imminent outranks loud-hollow.
- **Scale allocation**: the attention budget distributes across canopy layers, so a
  settlement's circumstance catches light bottom-up (character consequence) or top-down
  (faction stakes); the same event is shade at one player position and centerpiece at
  another (holonomy, §1).
- **Shade semantics**: unlit ≠ deleted — total accounting already forbids silent drops;
  shaded branches keep churning (autonomy is earned in the shade), accrue to the
  §3.3-generalized accumulators, and **re-light renders the catch-up retroactively as a
  designed beat** ("while you were at war, Hafenmark changed"). Fixture §9-F2.
- **Reflexivity, owned and bounded**: light causes story (lit → slate → played → changed
  trajectory) — the North-Star loop made explicit. Bounds: attention-only (above); one-pass
  allocation per Accounting (no fixed-point iteration); NPC anticipatory behavior (§6) reads
  position-scoped forecasts, not the light ledger (F-C/F-E).
- **The authorial surface — HELD BACK as one decision (F-F/fork-8):** the weight set
  (identity-touch · forecast mass · imminence · tie-proximity · scale allocation · inertia
  constants) IS Jordan's narrative voice — exposed, versioned data (§7), presented for
  explicit sign-off together with the subtract-only discipline. Merging this PR ratifies
  neither.

## §5 · THE SUBSTANCE — the claim-grammar interface (real arguments, not number-manipulation)

A parliamentary debate about a particular matter needs actual arguments — histories, events,
named people — or the contest system is just moving a persuasion track. **Arguments are typed
claims over ledger objects; the world's recorded state IS the argument content.**

- **The matter is a ledger object** (a fired Key, an Obligation breach, a grain crisis) with
  receipts: causes[] chain, witnesses (targets[]/visibility), prior outcomes, named actors.
- **A claim = rhetorical move × evidence binding.** The move half already exists in the
  contest system (appeals ethos/pathos/logos, the Ciceronian stasis ladder CR4, the
  Style×Conviction armature, Doubt/CR5, and the commitment-store concept from its
  source-research trilogy). The evidence half is v2's interface: Fact-rung cites a witnessed
  Key; Definition-rung contests its classification; Quality-rung warrants via the causal
  chain; Recall's precedent citation names a real prior adjudication. **Evidence weight is
  gradable from the object**: witness count/visibility, chain strength (causes[] depth),
  recency, asserter's Standing — so the track moves *because* the cited history is strong.
- **Interface objects (read/write surface; the engine's side of the contract):**
  `evidence{key_ref, witnesses, chain_strength, recency, asserter_standing}` ·
  `precedent{verdict_key, matter_class, adjudicator, season}` ·
  `commitment{speaker, claim, contest_ref}`. An unbound claim is a weaker move class
  (**bluster** — priced, attackable), never a rendering fallback.
- **The record grows by play**: verdicts become citable precedents; commitment stores make an
  NPC's hypocrisy a discoverable, exploitable fact; **investigation is the evidence supply
  chain** (trails → evidence → argument → precedent → new stakes — the FI lane, ED-FI-0001,
  is the contest system's armory). NPCs argue in character AND substance: Resonant Style
  picks the appeal; Convictions gate which warrants they will use; their own recorded deeds
  are their material.
- **Lane boundary (binding):** v2 ships this as the INTERFACE CONTRACT only; contest-internal
  mechanics (how moves resolve, how evidence weight enters the roll) belong to the SC lane's
  next stage, which receives this section as a requirements input — sequenced by workplan v6.
  No contest redesign here. Worked example: §9.3.

## §6 · THE RENDER — the load answer and the content pipeline (no runtime LLM)

**The load factorizes — additive authoring, combinatorial output.** Thousands of state
variables are the easy half (census: ~400–550 live strategic variables; accounting-cadence
ticks are trivial; the ensemble is the only heavy organ and it is bounded, §3). The prose
fear — "millions of sentences?" — dissolves because authoring is **grammar × lexicon, and
state binds the slots**:

- Beat-class template skeletons (hundreds, per rung below) · slot fillers bound from live
  data (names, places, stakes — free) · register overlays as **word-class substitution
  tables**, not sentences (Coherence 6 × Certainty 6 × Spirit 2 × focalizer 5 — each a
  ~200–500-row lexicon) · per-NPC voice tics (10–30 rows × ~30 NPCs) · per-faction idiom ·
  regional/temperament overlays · ~12 venue-class scene shapes · aggregation templates.
- **Census-grounded totals**: authored bake ≈ **230–450 units** (low-to-mid hundreds),
  swinging to **~1,200–2,700** if Certainty must gate the frozen fragment pool (fork 6 —
  needs Jordan's ruling before build scoping; fallback = Certainty as runtime lexicon-swap).
  Rendered combinatoric space: **10⁶–10⁷**. Actually rendered per season: **~10–30 distinct
  prose beats** (the 3–5 slate scenes + rationed cut scenes + chronicle + texture).
- The proven no-LLM lineage (CK3 event text, Dwarf Fortress histories, RimWorld tales), with
  one upgrade: **the offline prose-writer bake means an LLM authored the parts.** The
  coherence-tier author-weight tables (Tolkien 26%→5%, Lispector 0%→18%, the
  Beckett-continuation/Lispector-dissolution Spirit split, TS-gated Borges/Lem) are **bake
  DIRECTIVES** — for each (beat-class × band) the prose-writer writes the frozen variants
  UNDER that blend, so the fragments carry the voice and runtime band-selection replays it.
  `solmund_voice §18`'s Certainty registers become lexicon overlays + chronicler selection;
  the three-axis-test worked examples become bake QA fixtures. Existing assets offset the
  skeleton/causal-template lines (gm_ref ~300KB; the ~850KB tests/ arc corpus — verified:
  mechanics skeletons, not prose lines), never the lexicon rows.
- **Most narrative isn't sentences.** The bulk renders are behavioral: NPCs and factions
  acting on position-scoped forecasts (armies muster, prices move, faces change in the lens)
  — zero prose cost and the most diegetic render of the probability field; structured
  chronicle lines; short high-reuse texture. **The Light Function is also the render-cost
  governor: prose cost is O(attention budget), never O(world).**

**The content pipeline, scale-complete** (one stream, projections per §1 — every rung gets
banks, binding sources, voice): **character** — intent-grammar dialogue (the NPC engine's
concerns/projects emit intents: request, demand, warn, confide, accuse, deflect…; templates
per intent-class bound to topic = the live stake, relationship = Bond/Standing/npc_memory,
and voice = the slow variables selecting per-NPC overlays; players choose intents/styles,
never sentences; deterministic anti-repetition memory per NPC) · **family/household** —
kinship and oath idiom over Bond/Knot clusters + lifepath ties (full prose coverage
regardless of where the family-rung mechanical fork lands) · **faction** — decrees,
manifestos, parliamentary records, internal memos, per-faction idiom tables · **settlement**
— *the unique-circumstances renderer*: place description, street/market texture, local
rumor, event-deck beats, bound to each settlement's own state vector × regional idiom ×
temperament — every unique settlement READS as its unique circumstances · **territory** —
travel prose, calamity-radiation distance bands as lexicon bands, seasonal turns · **world**
— the chronicle's omniscient registers, era transitions, the MS-clock's voice. **Scenes are
assembled, not written**: venue-class shapes (setup → loop → resolution, the
contest-walkthrough model) instantiated by the slate entry's binding. **Plots project
forward**: each lit thread carries a computed, revisable projected-next-beat + horizon band,
rendered as anticipation — counsel/omens in Certainty-keyed voices, NPC hedging, **Thread
perception as the native forecast query** (P-01/P-11-grounded), stakes-preview lines,
sparing chronicle counterfactual ghosts — never promised (C7); expectation-vs-outcome is
itself a beat.

**The anti-slop theorem** — slop is unbound, consequence-free, unlimited content; five
checkable properties forbid it structurally: **(1) BINDING** — every rendered event names
actors-with-wants and stakes-with-history (causes[]); **(2) CONSEQUENCE** — one-ledger: no
cosmetic events can exist; **(3) SCARCITY** — the light budget manufactures significance by
selection; **(4) MEMORY** — precedents, callbacks, anti-repetition; **(5) RANGE** —
Expressive Range Analysis as a bake gate + the any-seed regression (§9-F1). Miss any one and
you get slop.

## §7 · THE MODULARITY CONTRACT — kernel / data / wrapper (nothing hard-baked)

Per the repo's proven combat split (wrapper = state machine · systems = pure functions ·
config = data, enforced by the existing architecture-invariant guards):

- **KERNEL (content-blind code):** FSM stepper · two-layer forecast runner · light allocator
  · claim evaluator · splice realizer — pure machinery over typed data. **Zero content
  literals**: the no-name-table AST guard extends to this engine (no event, NPC, place,
  template string, or weight constant in kernel code — ever).
- **DATA (everything swappable, versioned, schema-validated):** arc-vector templates (the
  ~13 shapes + growth) · event decks/cards · COLLISION priors · campaign skeletons &
  **starting conditions** (`scenario_authoring`'s compile output is a loadable pack) ·
  fragment banks, lexicons, voice/idiom tables · **Light-Function weight sets** (the
  authorial surface as data) · claim-type/evidence-weight tables · **the bake DIRECTIVES
  themselves** (prose-writer prompts versioned so re-bakes are reproducible) · histories
  (the chronicle/Key log is replayable runtime data and an editable scenario seed). Each
  asset class: schema + validator + CI round-trip (the `references/engine_params/` pattern
  generalized). **Update/change/add/delete any event, prompt, history, or starting condition
  = a data-file edit that validates — never an engine change.**
- **WRAPPER (thin, stable API):** loads packs, exposes the module contract, mediates Key
  I/O — the only surface other modules see; pack churn never ripples (holonic containment).
- **Conformance rules added by v2** (each one rule, one `tools/` home; joins v1's s4 R1–R10):
  **R-F1** forecast/live shared resolver code (no parallel model) · **R-F2** ensemble
  determinism (seed derivation + sorted iteration + basis-point marginals) · **R-HB** the
  hard-bake AST hunt (content literal in kernel = failure) · **R-CL** grammar-closure check
  (no Key family without a render path).

## §8 · Stack and staging

**Stack:** L0 GENERATOR (offline compile: templates × bindings × seeds; validation = the 138
+ 8) → L1 STORE+TICK (lifecycle FSMs) → **L1.5 FORECAST** (Layer A analytic + Layer B
ensemble) → L2 DETECT (actual + potential; discovery with authored priors) → L3 **LIGHT**
(replaces v1's salience economy; subtract-only) → L4 CAST/IMPEL (tie-graph casting; computed
deadlines) → L5 RENDER (claim-grammar interface, scale-complete banks, forecast surfaces,
splice realizer). Scenes always resolve in the ordinary engines (C3): the engine books
venues, never owns resolution.

**Staging (each independently mergeable; Gate-0 honesty carried from v1):**
Stage 0 render-gap close (ED-IN-0004; unchanged; ships first) → Stage 1 **generator compile
gate** (template grammar + the validation compile; blocked on forks 1–2) → Stage 2 store+tick
→ **Stage 2.5 forecast** (Layer A first — analytic horizons are near-free and immediately
power stakes-previews; Layer B gated on its preconditions: the named sim stubs, the event
deck's first code, and the seeded smoke oracle) → Stage 3 detect (discovery + priors; fork 3
window) → Stage 4 light + cast (+ ORD-4 scene-queue fix + scene_entered resolution) →
Stage 5 substance interface + scale-complete banks + conformance suite + the build-time
fixtures (§9-F).

## §9 · Verification

**Authored now (worked examples in this doc):**

**§9.1 Ensemble-stats mini-trace (one Accounting, the Torben stake).** Settled state: IP 30
crossed (Tutoring Demand fired); Torben Loyalty 5 (register 8→0 scale; range conflict fork 9
noted); Covert Contact = Crown Intel pool vs Ob 3, P(success) ≈ Φ-band ~0.62 (Layer A, from
the live odds surface). *Layer A horizons*: P(Loyalty≤3 within 2 seasons | no intervention) =
P(≥2 failed contacts) ≈ 0.14 → band LOW; within 4 seasons ≈ 0.35 → band GUARDED; under the
lever "assign the spymaster" (Intel +2 → P(fail)≈0.19/season): 4-season band drops to LOW.
*Layer B (N=64, k=4, seeds from Key-log hash)*: 9/64 futures co-spike `Loyalty≤3` with
`Church.Stability≤4` on shared target Crown within the same window → `convergence_candidate
{targets:[Crown,Torben,Church], window:4}` at band GUARDED — **discovered, not authored**
(COLLISION-C's cousin; the authored priors reproduce separately in fixture F4). *Render at
three Certainty registers (numbers never surface)*: Orthodox counselor (Cert-5): "Providence
has not yet turned its face from the boy — but two winters of silence would be an answer of
its own." · Skeptic clerk (Cert-2): "Miss two more contacts and the heir is theirs by
spring — the odds are not kind past that." · Warden chronicler (Cert-0/TS70): "The weave
around the boy pulls toward the Church's tear; not taut yet." One stake, one computation,
three voices — C1/C2 clean.

**§9.2 Zoom-coherence mini-trace (one Key set, three scopes).** Key: `state.belief_revised
{Almud, Belief-3 exposed, tribunal T1}` + its causes[] (the levy evidence, the witness).
*Played scene (character scope)*: the tribunal beat itself — Almud's line rendered at his
Certainty band, the player's Appraise reveal, the verdict move. *Faction paragraph (trunk
scope, aggregation template)*: "The Crown's own tribunal heard the granary ledgers read
aloud; by session's end the Chancellor's doubt was public record, and Crown standing in the
north bent under it." *Chronicle line (world scope, Tier-3)*: "In that year the Almud
tribunal broke the levy scandal open, and the north remembered it." Same facts, three
granularities, three focalizers — no contradiction possible because all three render from
the same Key set (R-CL checks the projection paths exist).

**§9.3 Claim-grammar mini-trace (a parliamentary matter, evidence-bound).** Matter:
`da.covert_betrayal{exposed:true}` — the grain-levy diversion (ledger object; causes[] to
the famine clock; 2 witnesses; season stamp). Moves: (1) Prosecution, Fact-rung + logos:
cites `evidence{key_ref: K-levy, witnesses:2, chain:3, recency:1}` — full weight. (2)
Defense, Definition-rung + ethos: "requisition under famine powers, not theft" — contests
classification, warrant = causes[] link to the famine clock (chain strength 2). (3)
Prosecution, Quality-rung: cites `precedent{verdict_key: K-morret-case, matter_class:
diversion}` — a PRIOR adjudication (Recall's +2D, now naming a real object). (4) Defense
BLUSTER (no binding available on the counter-claim) — weaker move class, priced; the
armature makes it attackable. Outcome: Definition verdict for prosecution → **new
`precedent{...}` object emitted** — future debates cite it; the defense NPC's claims enter
his commitment store (his earlier public praise of the levy is now a citable
contradiction). The track moved because the evidence was strong; the record grew by play.

**§9.4 The any-seed theorem (argument).** For any seed/trajectory: every beat the Light
Function lights satisfies invariant (i) (connectivity — candidates enter only via Keys whose
causes[] the engine populates per s4's rules, and selection preserves ancestor-lit-or-root),
(ii) (inertia — the carryover term + anti-strobe floor bound attention churn), (iii)
(rooting — the tie-proximity term is never zero for the protagonist's holon). A chronicle
projected from a connected, continuous, rooted subtree is a narrative by the definition the
audit's dramatic-legibility criterion uses (whose position, what they want, what happens
next — all answerable along the lit path). Different seeds light different subtrees (the
census's 10³ Key space per season × branch divergence), hence different stories — the
distinctness half is empirical, fixture F1.

**Build-time fixtures (named now, built at Stage 5):** F1 any-seed story regression (5+
seeds ⇒ chronicles differing in named actors, stakes, outcomes; each connected/continuous/
rooted) · F2 shade/re-light trace · F3 grammar-closure check (R-CL) · F4 COLLISION-prior
calibration (discovery reproduces the 8 authored rows on their trigger states) · F5 scale
budget table (live-measured against the census estimates) · F6 light-inertia/anti-strobe
check · F7 forecast smoke oracle (the §3 precondition — seeded ensemble output bands stable
across runs; flags the known degenerate win-share class).

## §10 · Open forks (consolidated; v1's forks 1–7 and 9 stand unchanged)

**T0-class (block M1 path):** **F-F/fork-8 — the Light-Function decision (HELD BACK):**
subtract-only discipline + the weight set as Jordan's authorial parameters — one surface,
explicit sign-off requested. · fork 1 Coup-Counter remap (blocks Stage 1) · fork 2 ARC-T04
(blocks COLLISION-C in the validation set).
**T1-class (block a named stage):** F-A forecast fidelity EV-vs-sampled per branch class
(default: Layer A analytic for continuous, Layer B sampled for discrete — the dossier's
shape) · fork 3 convergence temporal window (same-Accounting for authored priors; 4-season
cosine for discovery — default) · fork 6 **Certainty-in-bake** (swings authored units
230–450 → 1,200–2,700; default include, fallback runtime lexicon-swap; rule before build
scoping) · **NEW fork 10 — faction-count reconciliation** (census: 4–8 across four docs;
blocks any faction-scope bank/binding table; needs its own ED + ruling).
**T2-class (tuning/taste):** F-B horizon k + ensemble N · F-C forecast access rules
(position-scoped default; T-30) · F-D counterfactual-ghost budget (sparing) · F-E
anticipation reflexivity (one-pass default) · F-G evidence-weight formula (form canonical,
numbers Jordan's — the ED-874 split) · fork 7 GM-judgment-irreducible ~15% (declare
non-firing default).

## §11 · Crosswalk

This design executes ED-IN-0003 (detection, now two-tier discovery) and ED-IN-0004 (Stage 0)
as v1 did; additionally: mechanizes T-24 without the whitelist; computes the third
legibility question; gives P-11/threadwork the forecast-perception juncture; makes the
census's corpus findings (faction count, PI/Axis-9, 138-not-110) tracked items for v6; and
supplies the SC lane's next stage with §5 as a requirements input. Per-chapter deltas to
v1's normative spec: `spec/churn_amendments.md`.
