# Valoria — The Emergent Narrative Engine · Design v2: THE CHURN ENGINE

## Status: RATIFIED (Jordan, 2026-07-05 — "Ratify commit merge all", PR #78; record ED-IN-0011. Supersedes-IN-PART design v1 — v1 stays as record, ratified as amended. The previously held-back F-F/fork-8 Light-Function decision is RATIFIED at its stated default — subtract-only discipline + the weight set as exposed, versioned authorial parameters; the weight VALUES remain tunable data, revisable anytime without re-ratification)
## Date: 2026-07-05 · Lane: IN · Branch: `claude/ners-audit-fable5-9cpfdz` · Companion: `spec/churn_amendments.md` (per-chapter deltas to v1's s1–s5)

**Why v2 exists.** v1 (the Arc-Vector Engine) answered *how detected story-moments reach the
player*. Jordan's critique showed that was the smaller question: the game is a **generative
churn** — character ambitions × world states × event cards × scene resolutions branching into
a combinatorially vast Key space (census: ~10³ live Key instances/season over 44 declared Key
types — 48 by physical grep; rendered-prose space 10⁶–10⁷), probabilities propagating forward
at every calculation —
and the engine's job is to harness that churn **as** an emergent story: a coherent narrative
derivable from ANY realized trajectory, at any scale, with no runtime LLM. Grounding:
`01_workings/dossier_forecast_tractability.md` + `dossier_combinatorial_census.md` (both
committed; every load-bearing number below cites one of them).

---

## §0 · The critique of v1 (kept honestly; self-authored, bias flagged)

1. **Enumerative bias** — L0 compiled arc *instances*. The register's 138 arcs (census — the
   earlier "~110" was a 25% undercount) are narrative text applied to sample trajectories
   through state graphs, collapsing to **~13 structural shapes** (sampled range 12–15, from a
   24-of-138 classification — census §3.2); v1 treated the samples as the content.
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
  seeds → instantiated vectors (the module's authoring-vs-runtime classification is
  `[OPEN — Jordan]` in module_contracts — surfaced as fork 11, §10, default compile =
  authoring-time). The 138 register arcs + 8 COLLISIONs are the
  **validation/calibration set**: the compiled generator must reproduce them from their
  trigger states (fixture §9-F4) — never the content ceiling.
- **Specificity from binding at instantiation.** A template bound to THIS settlement's
  circumstances (its own stat vector, temperament, thread sites, Local Actors) and THIS NPC's
  ambition is particular by construction — how thousands of permutations stay individually
  meaningful rather than generic (anti-oatmeal defense 1, §6).
- Grammar-closed Key space **with two honest residues**: predicates quantify over the 44
  declared type families (48 by physical grep) — no enumerated whitelist anywhere
  (dissolving §0.4) — EXCEPT (a) the ~15% GM-judgment-irreducible arcs (fork 7, declared
  non-firing) and (b) the **bespoke-EFFECT NPC-ARCs**, whose *triggers* bind as templates but
  whose effect logic is an authored decision procedure, not a slot (NPC-ARC-JAR's threat
  taxonomy, ARC-S52's per-NPC utility tie-break, ARC-S56's two-faction read of one counter,
  ARC-S29's max-friction selection, ARC-P05's qualitative roll): these join fork 7's honesty
  ledger — declared non-firing by default, or hand-authored as effect tables in DATA (§7),
  never silently implied to fire.
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
  Domain Echo maps degree→delta by a zero-RNG table (`domain_echo.py`). Clock horizons split
  honestly: **pure-drift residuals** (MS baseline −1/yr, CI passive +1/season) have exact
  linear hitting times — (threshold − x₀)/rate, deterministic, no distribution involved;
  **state-coupled clocks** (CI *generation* under PP-412, IP, RS, Turmoil, Accord — and MS
  itself once thread ops or Restoration move it) get Layer-A horizons only as an
  APPROXIMATION under a frozen-drift assumption, flagged as such, per the dossier's gate:
  analytic if the per-season delta distribution is known, else sample (promote to Layer B
  where the coupling is material). Layer-A marginals are per-stake and **not jointly
  valid** — clocks share drivers, so joint/convergence questions always go to Layer B.
- **Layer B — seeded ensemble (cheap, shared-code).** The discrete structural branches EV
  cannot collapse — **which action, which target, which card** (correction from the dossier:
  faction priority trees are NOT fully deterministic; GD-2 mandates only that the
  deterministic mandatory pass PRECEDES stochastic selection — `faction_action.py` draws
  action and target) — sample through the LIVE code paths via `mc_v18.run_campaign(seed,
  max_seasons)` with `season.run_season(action_callback)` as the lever-injection seam and
  `game_state.serialize_world` as the snapshot/branch point. N≈64 futures × k≈4 seasons at
  accounting cadence ≈ 10⁶–10⁷ ops, **<100 ms per Accounting on desktop** — provided scenes
  are NEVER rolled in forecast (rolling personal kernels would 10²–10³× the cost). The
  scene-skip is itself shared code, not a forecast fork: a `strategic_cadence_only` flag on
  the scene seam that BOTH callers honor (live never sets it; forecast always) EV-summarizes
  each scene by its degree distribution — single-sourced, an R-F1 sub-clause (§7), and one
  of the paths still to be built. **Per-lever cost splits by branch class**: continuous
  stakes take the lever as a Layer-A μ/odds shift (free — no extra ensemble; §9.1's
  spymaster lever is exactly this); per-lever horizons on DISCRETE structural branches would
  re-run Layer B once per lever (N × k × L ≈ 5–15× the <100 ms budget at L≈5–15 candidate
  actions) and are **deferred post-M1** — M1's lever previews are continuous-class only.
- **The port↔oracle discipline holds by construction**: forecast and live play share resolver
  code (conformance rule R-F1, §7); fork F-A is EV-vs-sampled *within* the shared functions,
  never a parallel model.
- **Outputs** (typed, engine-owned state): `stake_horizon{stake, P-band per k, under
  no-intervention and per player lever}` — the third legibility question, computed;
  `convergence_candidate{targets, co-spike vector, window}` — discovery over the ensemble,
  with the 8 authored COLLISIONs as priors it must reproduce (fixture §9-F4);
  `foreclosure_countdown`; `option_distribution`. Detection (L2) becomes actual + potential.
  **Forecast objects are actor-invisible**: no actor resolver (`faction_action`, `npc_ai`)
  ever takes a `stake_horizon`/`convergence_candidate` as input — NPCs anticipate via
  diegetic heuristics over observable state (§6); the forecast informs the render and the
  light's depth allocation, never the world's behavior (conformance R-AI, §7; fixture F8
  proves the severance).
- **Honesty bounds** (also C7 protections): the forecast models venues at unconditional odds
  — per-lever conditioning is an odds/stat shift, so horizons are *"field pressure under
  average play," never a promise*; and forecast quality is bounded by the sim's own known
  gaps — **preconditions before any Layer-B horizon is trusted**: the ~19 sim stubs on
  Layer-B paths (`npc_ai`, `ip_track`, `rs_track`, ~8 provincial actions), the unbuilt event
  deck, the scene-EV flag path, the `canonical_key_log` serialization spec + ORD-3/ORD-4
  landing (below), and a deterministic seeded smoke oracle for ensemble outputs (extending
  `sim/tests/` — the known degenerate ~87% win-share currently has nothing flagging it,
  CLAUDE.md §7). These gate Stage 2.5's Layer B (§8). **M1 ships Layer A alone — a hard
  gate, not a preference**: `stake_horizon` (continuous), `foreclosure_countdown`,
  stakes-previews, and the light's imminence term are all Layer-A-satisfiable; Layer B's
  unique outputs (convergence discovery, `option_distribution`) switch on only after fixture
  F7 passes and the stubs land — until then the 8 authored COLLISION priors are the entire
  convergence surface.
- **Determinism guards** (from the dossier + v1's s4 — stated as work to BUILD, not
  properties in hand): stable-key sorted iteration everywhere (the `ALL_PLAYABLE_15`
  frozenset hazard; forbid raw `set()` in marginals); **integer basis-point marginals**,
  which fix float ACCUMULATION order — the residual float boundary is the Φ quantization
  step, so Φ ships as a **precomputed integer lookup table** (quantized once, offline;
  identical bytes on Python and GDScript; no live `erf` on either side), pinned as its own
  parity fixture (F7 extension); until that table exists, Layer-A horizons are **not
  port-parity-clean** and any Godot forecast is gated on it. Ensemble seed =
  `sha256(canonical_key_log ‖ accounting_index ‖ future_index)` truncated to 64 bits — a
  FIXED cross-platform hash, never Python's per-process-salted builtin `hash()`, never
  wall-clock (kill `mc_v18`'s `time.time()` fallback). Two prerequisites the seed itself
  depends on, named as Stage-2.5 preconditions: a **`canonical_key_log` serialization spec**
  (explicit field set excluding runtime-only fields, stable field/record order, an explicit
  rule for authored-vs-reentrancy `causes[]` edges — no such spec exists yet), and
  propagation_spec's **ORD-3/ORD-4 landing** (without them the log the seed reads is not
  itself deterministic).

## §4 · THE AUTHOR — the Light Function (pruning as authorship)

Roots (world clocks) → trunk (factions) → branches (settlements, each with unique
circumstances) → leaves (characters) → capillaries (every resolution draw). **You cannot
narrate the tree; you narrate the light's path through it** — and how light falls shapes the
game's whole narrative development. v2 therefore owns the relevance function as the engine's
central object and the game's authorial voice.

- **Strictly selective (the fork-8 reconciliation, stated once, binding):** the Light
  Function **rations among candidates the churn produced. It can never inject content, shape
  the RESOLUTION of any scene, accelerate a clock, or emit a pressure-bearing Key.** (The
  honest scope, refuter-forced: light allocation is outcome-RELEVANT — what gets played
  changes the trajectory, the reflexivity bullet below — so the discipline is stated where
  it can actually hold: resolution-neutral, clock-neutral, Key-log-neutral. Catch-up
  re-light beats are render-only, zero `pressure_effects` — conformance R-RL, §7.)
  Allocation-among-given IS the subtract-only discipline; the director graduates as this
  function's scheduler, nothing more. **And casting is severed from forecast**: slate entry
  and summons key on the tie-graph + REALIZED state only (the charter's one casting rule);
  forecast mass governs render depth and anticipation texture among lit material, never
  which futures are impelled onto the player — and it may never demote a thread the player
  is actively pursuing out of the playable set.
- **The coherence guarantee — a legible chronicle out of ANY branch.** Four invariants hold
  on every trajectory: **(i) proximate causal connectivity** — every lit beat traces via
  causes[] to lit ancestors or roots, AND successive lit beats within one projection share a
  proximate common ancestor or a common actor/stake within bounded causal hops
  (root-connectivity alone is vacuous — everything eventually reaches a world clock; the
  invariant binds at the proximate level or it binds nothing). **(ii) light-inertia** —
  attention has momentum: lit threads carry a persistent priority term whose carryover
  decays by integer/fixed-point arithmetic (`inertia_bp = inertia_bp · NUM // DEN`,
  constants in the F-F weight-set DATA; decay a pure function of the accounting index — no
  float, no RNG; the same discipline propagation_spec's OF-3 demands of the Key-ledger's
  `decay()`, disposed together with it); an anti-strobe floor (integer threshold) forbids
  flicker; engaged threads (player-participated) are demotion-exempt (v1 rule) — **but the
  exempt set counts against the budget under a cap, and a reserved promotion slice the
  exempt set cannot consume keeps ≥1 slot live for emergent/imminent candidates** (otherwise
  a player engaging budget-many local threads starves the very imminence term v2 added —
  the refuter's starvation case; cap and slice constants live in the F-F surface, and the
  explicit accounting restores the O(budget) render bound §6 leans on). Continuity is a
  property of the LIGHT, not the events. **(iii) player-rooting** — tie-graph proximity is a
  permanent weight term; the seedling grows where the protagonist stands. **(iv) liveness**
  — a lit, protagonist-proximate stake may not reach terminal (foreclosing) resolution in
  the shade without first surfacing its terminal intervention point: autonomy may DEFER a
  lit proximate climax, never silently foreclose it — enforced at L4 (which owns
  scheduling), as the mechanism behind the charter's open-intervention-point guarantee
  rather than a race against it; if the player declines the surfaced point, foreclosure
  proceeds (C7 — surfaced, never forced). A chronicle of the lit subtree is therefore
  *connected, continuous, rooted, and live* — whichever branch every calculation took. What
  that buys, stated honestly: a LEGIBLE chronicle, not a guaranteed satisfying plot (§9.4;
  regression fixture §9-F1).
- **The selection score** (per candidate beat/thread, integer basis-points): meaningfulness
  (durability × tie-proximity × identity-touch, v1 s2) × **forecast mass** (the §3 horizons —
  the new term) × **imminence** (horizon band) × light-inertia carryover × scale-allocation
  weight. Quiet-meaningful-imminent outranks loud-hollow. Two bindings on the score
  (refuter-forced): **(a) reach** — the score governs RENDER DEPTH and attention (which lit
  material gets prose, at what granularity); casting/slate injection reads only the
  realized-state terms (meaningfulness, tie-proximity, inertia), never forecast mass or
  imminence (the severance above). **(b) forecast dependency, tagged per term** — for M1 the
  forecast-mass and imminence terms compute from Layer-A horizons + the 8 authored COLLISION
  priors ALONE; Layer-B convergence discovery joins as an additive input only after F7
  passes (§3) — the author organ never leans on the unbuilt, currently-degenerate ensemble.
- **Scale allocation**: the attention budget distributes across canopy layers, so a
  settlement's circumstance catches light bottom-up (character consequence) or top-down
  (faction stakes); the same event is shade at one player position and centerpiece at
  another (holonomy, §1).
- **Shade semantics**: unlit ≠ deleted — total accounting already forbids silent drops;
  shaded branches keep churning (autonomy is earned in the shade, bounded by invariant iv),
  accrue to the §3.3-generalized accumulators, and **re-light renders the catch-up
  retroactively as a designed beat — always focalized**: through the chronicle's sanctioned
  past-tense omniscient register, or through a diegetic carrier with a trail (a returning
  agent, gossip, a document, a witness who was there) — "the letters from Hafenmark, a year
  unread, told the change in a stranger's hand" — never placeless present-tense narration of
  the unwitnessed (P-08: the shade stays epistemically real; every catch-up beat cites its
  focalizer — `chronicle | witness_key | document_key` — conformance R-RL, §7). Fixture
  §9-F2.
- **Reflexivity, owned and bounded**: light causes story (lit → slate → played → changed
  trajectory) — the North-Star loop made explicit. The dangerous loop is not within an
  Accounting but ACROSS them: forecast → lights/impels → actors move toward the forecast →
  next forecast strengthens → rubber-banding toward the predicted attractor. A forecast can
  be epistemically honest and still manufacture its own referent — so v2 severs the loop
  structurally, not with a one-pass rule alone: (a) casting/impulsion never reads forecast
  terms (the severance above); (b) forecast objects are actor-invisible — NPC/faction
  anticipation is a diegetic heuristic over OBSERVABLE state and memory, never a read of
  `stake_horizon`/`convergence_candidate` (R-AI, §7); (c) one-pass allocation per Accounting
  (no fixed-point iteration); (d) fixture F8 proves the severance empirically: seed a
  forecast of convergence C, suppress player participation, verify realized P(C) does not
  exceed the forecast-blind control — if forecasting C raises P(C), the loop is live and the
  build fails.
- **The authorial surface — RATIFIED at this default (F-F/fork-8, Jordan 2026-07-05, ED-IN-0011):** the weight set
  (identity-touch · durability · forecast mass · imminence · tie-proximity · scale
  allocation · inertia/decay constants · the anti-strobe floor · the attention-budget sizes
  and the exempt-cap/reserved-promotion-slice constants) IS Jordan's narrative voice —
  every tunable that shapes the light, enumerated here, none left in prose or inherited
  config — exposed, versioned data (§7). The subtract-only discipline + this enumerated
  surface were ratified together; the weight VALUES stay data — Jordan revises them at any
  time without re-ratification.

## §5 · THE SUBSTANCE — the claim-grammar interface (real arguments, not number-manipulation)

A parliamentary debate about a particular matter needs actual arguments — histories, events,
named people — or the contest system is just moving a persuasion track. **Arguments are typed
claims over ledger objects; the world's recorded state IS the argument content.**

- **The matter is a ledger object** (a fired Key, an Obligation breach, a grain crisis) with
  receipts: causes[] chain, witnesses (targets[]/visibility), prior outcomes, named actors.
- **A claim = rhetorical move × evidence binding.** The move half is the SC lane's live
  ground, cited here in ITS vocabulary (the ED-1083 §2 shape-divergence guardrail — no
  narrative-engine-local rhetoric dialect): the stasis grounds **FACT / DEFINITION / QUALITY
  / JURISDICTION (+ CONSEQUENCE / FEASIBILITY)**, the appeals ethos/pathos/logos, the
  Style×Conviction armature, Doubt/CR5 — plus **Recall**, which is a setup advantage, not a
  stasis. (The **commitment store is NOT live**: it is a read-and-cited concept from the SC
  source-research trilogy, in no kernel and on no schedule — listed below as a proposed
  deliverable, not an existing part.) The evidence half is v2's requirements input, and
  **per-ground evidence binding is NEW behavior for the SC lane to accept or reshape**: a
  FACT claim cites a witnessed Key; a DEFINITION claim contests its classification; a
  QUALITY claim warrants via the causal chain; Recall's citation names a real prior
  adjudication instead of a self-asserted one — which changes Recall's qualification basis
  (today: binary, self-asserted, params/contest.md's +2D) and is therefore an SC-resolution
  edit, flagged as such. **Evidence weight is gradable from the object**: witness
  count/visibility, chain strength (causes[] depth), recency, asserter's Standing — so the
  track moves *because* the cited history is strong.
- **Interface objects (read/write surface; the engine's side of the contract):**
  `evidence{key_ref, witnesses, chain_strength, recency, asserter_standing}` — fully
  substrate-backed today (Key · targets[]/visibility · causes[] depth · season stamp · the
  live Standing tracker) · `precedent{verdict_key, matter_class, adjudicator, season}` and
  `commitment{speaker, claim, contest_ref}` — **these two require new SC-lane-owned stores
  that exist nowhere yet** (schema, owner, lifecycle for the SC lane to declare;
  `matter_class` becomes a new payload field on the verdict Key; the engine's render READS
  both stores, so they join s4's READS column once declared). An unbound claim is a weaker
  move class (**bluster** — priced per a versioned DATA table, §7; its attackability is one
  of the four SC additions below — the armature as it stands is a judge-aimed δσ shift with
  no unbound-claim attack move), never a rendering fallback.
- **The record grows by play**: verdicts become citable precedents; the commitment store
  (once the SC lane builds it) makes an NPC's hypocrisy a discoverable, exploitable fact;
  **investigation is the evidence supply chain** (trails → evidence → argument → precedent →
  new stakes — the FI lane, ED-FI-0001, is the contest system's armory). NPCs argue in
  character AND substance: Resonant Style picks the appeal; Convictions gate which warrants
  they will use; their own recorded deeds are their material.
- **Lane boundary (binding, honestly scoped):** v2 ships this as a REQUIREMENTS INPUT that
  **adds four contest sub-systems, none of which exist today**: (1) an evidence-weight δσ
  input family (witnesses/chain-depth/recency terms — the live δσ set has none of them; the
  natural insertion point is the Gate-C leverage channel, where corroboration already sits);
  (2) the bluster move class + its pricing; (3) the precedent store + the Recall rewire;
  (4) the commitment store + the hypocrisy-exploit read. The existing resolution math
  (CLASH/REINFORCE/CROSS/TIE, the σ substrate, CR4 +1D, CR5 backfire) does not change — but
  the SHAPE of all four additions, not just their numbers, is the SC lane's to accept,
  reshape, or reject at its next stage, which receives this section as input — sequenced by
  workplan v6. Worked example (illustrative of the contract once the stores exist): §9.3.

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
  regional/temperament overlays · venue-class scene shapes (grounded count 10, estimate ~12)
  · aggregation templates.
- **Census-grounded totals**: authored bake ≈ **~1,200–2,700 units** under fork 6's stated
  default (Certainty gates the frozen fragment pool — the census's single biggest swing
  factor, carried as the honest headline per s5's O-6 rule); the low figure, **230–450**,
  holds only under the fallback (Certainty as runtime lexicon-swap). Fork 6 needs Jordan's
  ruling before build scoping. Rendered combinatoric space: **10⁶–10⁷**. Actually rendered
  per season: **~10–30 distinct prose beats** (the 3–5 slate scenes + rationed cut scenes +
  chronicle + texture).
- The proven no-LLM lineage (CK3 event text, Dwarf Fortress histories, RimWorld tales), with
  one upgrade: **the offline prose-writer bake means an LLM authored the parts.** The
  coherence-tier author-weight tables (Tolkien 26%→5%, Lispector 0%→18%, the
  Beckett-continuation/Lispector-dissolution Spirit split, TS-gated Borges/Lem) are **bake
  DIRECTIVES** — for each (beat-class × band) the prose-writer writes the frozen variants
  UNDER that blend, so the fragments carry the voice and runtime band-selection replays it.
  `solmund_voice §18`'s Certainty registers become lexicon overlays + chronicler selection;
  the three-axis-test worked examples become bake QA fixtures. Existing assets offset the
  skeleton/causal-template lines (gm_ref ~300KB; the >1MB tests/ arc corpus, census §5's
  corrected count — verified: mechanics skeletons, not prose lines), never the lexicon rows.
- **Most narrative isn't sentences.** The bulk renders are behavioral: NPCs and factions
  acting on their own diegetic expectations — heuristics over OBSERVABLE state and memory
  (armies muster because the border reports say muster; prices move on what merchants can
  see), never on engine forecast objects (R-AI, §7 — prudent NPCs, not the forecast's
  delivery mechanism) — zero prose cost and the most diegetic render of a world under
  pressure; structured chronicle lines; short high-reuse texture. **The Light Function is
  also the render-cost governor: prose cost is O(attention budget), never O(world).**

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
sparing chronicle counterfactual ghosts — under two hard render rules on every anticipation
surface: **never a promise** (C7 — anticipation renders pressure and direction, not
verdicts), and **never a meter** (band→line coupling must be many-to-one: multiple bands can
yield the same line, a line stays compatible with a range of horizons, NPC variance noises
the mapping — so repeated play cannot invert the counsel back to the number; no quantized
horizon ever surfaces — no counts-remaining, no dates-certain — and `foreclosure_countdown`
schedules internal urgency only, never rendering as a countdown). Expectation-vs-outcome is
itself a beat.

**The anti-slop theorem** — slop is unbound, consequence-free, unlimited content; five
properties, each with a named check, forbid it structurally (four checkable now, one pending
its instrument): **(1) BINDING** — every rendered event names actors-with-wants and
stakes-with-history (causes[]); **(2) CONSEQUENCE** — one-ledger: no cosmetic events can
exist; **(3) SCARCITY** — the light budget manufactures significance by selection;
**(4) MEMORY** — precedents, callbacks, anti-repetition; **(5) RANGE** — the any-seed
regression (§9-F1) + Expressive Range Analysis as a bake gate (proposed — the ERA instrument
is UNBUILT, a Stage-5 blocker per s5; do not read RANGE as operative today). Miss any one
and you get slop.

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
  fragment banks, lexicons, voice/idiom tables · **the intent-class roster** (the dialogue
  grammar's terminal set — never an enum in the emitter) · **venue-class scene shapes** (the
  grounded 10) · **the chronicler/focalizer roster** · **aggregation templates**
  (first-class, §1) · **Light-Function weight sets** (the authorial surface as data,
  including budget sizes, exempt-cap/promotion-slice, anti-strobe floor, decay constants) ·
  claim-type/evidence-weight tables + **the bluster-price table** · bespoke-effect tables
  for the fork-7 residue arcs (§2) · **the bake DIRECTIVES themselves** (prose-writer
  prompts versioned so re-bakes are reproducible) · histories (the chronicle/Key log is
  replayable runtime data and an editable scenario seed). Each asset class: schema +
  validator + CI round-trip (the `references/engine_params/` pattern generalized).
  **Update/change/add/delete any event, prompt, history, or starting condition = a data-file
  edit that validates — never an engine change.**
- **WRAPPER (thin, stable API):** loads packs, exposes the module contract, mediates Key
  I/O — the only surface other modules see; pack churn never ripples (holonic containment).
- **Conformance rules added by v2** (each one rule, one `tools/` home; joins v1's s4 R1–R10):
  **R-F1** forecast/live shared resolver code — no parallel model; sub-clause: the scene-EV
  summary is a flag-gated mode INSIDE the shared scene seam (`strategic_cadence_only`),
  honored by both callers, never a forecast-only fork · **R-F2** ensemble determinism
  (sha256 seed derivation over the canonical Key-log serialization + sorted iteration +
  basis-point marginals + integer light-inertia decay) · **R-HB** the hard-bake AST hunt
  (content literal in kernel = failure) · **R-CL** grammar-closure check (no Key family
  without a render path) · **R-AI** forecast actor-invisibility (no actor resolver takes a
  `stake_horizon`/`convergence_candidate` as input — checked at the import/signature level)
  · **R-RL** re-light discipline (catch-up beats are render-only — zero `pressure_effects` —
  and cite a focalizer: `chronicle | witness_key | document_key`).

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
→ **Stage 2.5 forecast** (**M1 = Layer A alone, a hard gate**: analytic horizons are
near-free and immediately power stakes-previews and the light's imminence term; Layer B
switches on only after ITS preconditions land — the named sim stubs, the event deck's first
code, the scene-EV flag path, the `canonical_key_log` serialization spec + ORD-3/ORD-4, and
fixtures F7+F8 passing) → Stage 3 detect (discovery + priors; fork 3
window) → Stage 4 light + cast (+ ORD-4 scene-queue fix + scene_entered resolution) →
Stage 5 substance interface + scale-complete banks + conformance suite + the build-time
fixtures (§9-F).

## §9 · Verification

**Authored now (worked examples in this doc):**

**§9.1 Ensemble-stats mini-trace (one Accounting, the Torben stake).** Settled state: IP 30
crossed (Tutoring Demand fired); Torben Loyalty 5 (register 8→0 scale; range conflict fork 9
noted). The stake advances by Covert Contact, a faction-scale action through the domain
resolver — one resolver, one model, every number below derived from its single grid: Crown
Intel 5 vs Difficulty 4 → M = +1 → P(success) = clamp(0.50 + 0.10·M) = **0.60**, P(fail) =
0.40 per season. *Layer A horizons (exact binomial over that P)*: P(≥2 failed contacts
within 2 seasons | no intervention) = 0.40² = **0.16** → band GUARDED; within 4 seasons =
1 − 0.60⁴ − 4·0.40·0.60³ ≈ **0.52** → band ELEVATED; under the lever "assign the spymaster"
(Intel +2 → M = +3 → P(fail) = 0.20): the 4-season band drops to ≈ **0.18** → LOW — a real,
computed lever preview (continuous-class, hence Layer-A-only, per §3). *Layer B*
`[TRACE-ILLUSTRATIVE — Layer B cannot run today; its §3 preconditions are unmet]`: an
ensemble pass would test whether `Loyalty≤3` co-spikes with `Church.Stability≤4` on the
shared target Crown within the window — a `convergence_candidate` DISCOVERED rather than
authored (COLLISION-C's cousin; the authored priors reproduce separately in fixture F4).
*Render at three Certainty registers (under §6's never-a-meter/never-a-promise rules — no
quantized horizon, no verdict, band→line many-to-one)*: Orthodox counselor (Cert-5):
"Providence has not turned its face from the boy — but silence, left to lengthen, becomes an
answer of its own." · Skeptic clerk (Cert-2): "Every silence from the boy is ground given.
The odds harden against the Crown the longer this drags." · Warden chronicler (Cert-0/TS70):
"The weave around the boy pulls toward the Church's tear; not taut yet." One stake, one
computation, three voices — none invertible to the band, none a promise — C1/C2/C7 clean.

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

**§9.3 Claim-grammar mini-trace (a parliamentary matter, evidence-bound — illustrative of
the §5 contract once the SC lane builds its two new stores).** Matter:
`da.covert_betrayal{exposed:true}` — the grain-levy diversion (ledger object; causes[] to
the famine clock; 2 witnesses; season stamp). Moves: (1) Prosecution, Fact-rung + logos:
cites `evidence{key_ref: K-levy, witnesses:2, chain:3, recency:1}` — full weight. (2)
Defense, Definition-rung + ethos: "requisition under famine powers, not theft" — contests
classification, warrant = causes[] link to the famine clock (chain strength 2). (3)
Prosecution, Quality-rung: cites `precedent{verdict_key: K-morret-case, matter_class:
diversion}` — a PRIOR adjudication (Recall's +2D naming a real object — the §5 Recall
rewire, an SC-resolution edit). (4) Defense BLUSTER (no binding available on the
counter-claim) — weaker move class, priced per the bluster table; its attackability is SC
addition (2), §5. Outcome: Definition verdict for prosecution → **new `precedent{...}`
object emitted** into the proposed precedent store — future debates cite it; the defense
NPC's claims enter the proposed commitment store (his earlier public praise of the levy is
now a citable contradiction). The track moved because the evidence was strong; the record
grew by play.

**§9.4 The any-seed theorem (argument — conclusion stated honestly).** For any
seed/trajectory: every beat the Light Function lights satisfies invariant (i) (proximate
connectivity — candidates enter only via Keys whose causes[] the engine populates per s4's
rules, and selection preserves proximate-ancestor-or-shared-actor/stake linkage, not mere
root-reachability), (ii) (inertia — the carryover term + anti-strobe floor bound attention
churn, with the reserved promotion slice keeping emergence live), (iii) (rooting — the
tie-proximity term is never zero for the protagonist's holon), (iv) (liveness — no lit
proximate stake forecloses in the shade unsurfaced). **What the theorem proves**: a
chronicle projected from a connected, continuous, rooted, live subtree is a **legible**
chronicle — the audit's dramatic-legibility triad (*what is at stake · who is acting and
why · what changed*) is answerable at every lit beat. **What it does NOT prove** (extending
v1 §6 / doc-10 §8.5's NOT-list): no guaranteed three-act shape; no guaranteed heroic arc;
no guarantee the answers are COMPELLING — a quiet neighborhood yields a legible but
low-stakes chronicle (rooting buys proximity, not stakes-density); and liveness guarantees
a playable terminal intervention point is SURFACED, not taken — a declined climax resolves
as witnessed, not played (C7: surfaced, never forced). Different seeds light different
subtrees (the census's ~10³ Key space per season × branch divergence), hence different
stories — the distinctness half is empirical, fixture F1.

**Build-time fixtures (named now, built at Stage 5):** F1 any-seed story regression (5+
seeds ⇒ chronicles differing in named actors, stakes, outcomes; each connected/continuous/
rooted) · F2 shade/re-light trace (incl. R-RL focalizer + render-only checks) · F3
grammar-closure check (R-CL) · F4 COLLISION-prior calibration (discovery reproduces the 8
authored rows on their trigger states) · F5 scale budget table (live-measured against the
census estimates) · F6 light-inertia/anti-strobe check (incl. exempt-cap + reserved-slice
accounting) · F7 forecast smoke oracle (the §3 precondition — seeded ensemble output bands
stable across runs; flags the known degenerate win-share class; pins the offline Φ lookup
table as a port-parity fixture) · **F8 anti-self-fulfillment control** (seed a forecast of
convergence C with player participation suppressed; realized P(C) must not exceed the
forecast-blind control — §4's severance, proven empirically).

## §10 · Open forks (consolidated; v1's forks 1–7 and 9 stand unchanged)

**T0-class (block M1 path):** **F-F/fork-8 — the Light-Function decision (RATIFIED at default, Jordan 2026-07-05, ED-IN-0011):**
subtract-only discipline + the weight set as Jordan's authorial parameters (the full §4
enumeration, including budget sizes, exempt-cap/promotion-slice, anti-strobe floor,
durability, decay constants) — one surface, signed off. · fork 1 Coup-Counter remap
(RATIFIED at default: 1:1 remap onto Löwenritter Autonomy 4-stage — EXECUTION remains a
Stage-1 work item) · fork 2 ARC-T04 (RATIFIED at default: strike; COLLISION-C → 7-of-8 —
execution remains).
**T1-class (block a named stage):** F-A forecast fidelity EV-vs-sampled per branch class
(default: Layer A analytic for continuous, Layer B sampled for discrete — the dossier's
shape; discrete PER-LEVER horizons deferred post-M1 outright, §3) · fork 3 convergence
temporal window (same-Accounting for authored priors; 4-season cosine for discovery —
default) · fork 6 **Certainty-in-bake** (the census's single biggest swing: authored units
~1,200–2,700 under the include-default headline vs 230–450 under the lexicon-swap fallback;
rule before build scoping) · **NEW fork 10 — faction-count reconciliation** (census: 4–8
across four docs; blocks any faction-scope bank/binding table; ED-FA-0001 filed — the COUNT ruling itself stays open, no default exists) ·
**NEW fork 11 — `scenario_authoring` authoring-vs-runtime classification** (module_contracts
`[OPEN — Jordan]`; RATIFIED at default 2026-07-05: compile is authoring-time, its output
packs seed runtime — ED-IN-0011).
**T2-class (tuning/taste):** F-B horizon k + ensemble N · F-C forecast-RENDER access rules
(which counsel/omen surfaces a position sees; position-scoped default; T-30 — NPC reads are
barred outright by R-AI, not a fork) · F-D counterfactual-ghost budget (sparing) · F-E
anticipation reflexivity (one-pass default) · F-G evidence-weight formula (form canonical,
numbers Jordan's — the ED-874 split; the SHAPE of all four SC additions stays the SC lane's,
§5) · fork 7 GM-judgment-irreducible ~15% + the bespoke-EFFECT NPC-ARCs (§2 — declare
non-firing default, or hand-authored effect tables in DATA).

## §11 · Crosswalk

This design executes ED-IN-0003 (detection, now two-tier discovery) and ED-IN-0004 (Stage 0)
as v1 did; additionally: mechanizes T-24 without the whitelist; computes the third
legibility question; gives P-11/threadwork the forecast-perception juncture; makes the
census's corpus findings (faction count, PI/Axis-9, 138-not-110) tracked items for v6; and
supplies the SC lane's next stage with §5 as a requirements input — honestly labeled as four
new contest sub-systems whose shape stays the SC lane's to decide. The five-lens adversarial
pass (determinism/cost · C2/C7 · fabrication · Light Function · interface reality) is
recorded in `01_workings/refute_v2_*.md`; every REQUIRED_FIX is applied in this text, and
the survivors became forks 10–11 + F8 + the M1 Layer-A hard gate. Per-chapter deltas to
v1's normative spec: `spec/churn_amendments.md`.
