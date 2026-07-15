# Judge — PLAYER EXPERIENCE lens

## Status: SUPERSEDED (working record of the emergent-narrative-engine design effort; head RATIFIED as ../narrative_engine_design_v2_churn.md + narrative_engine_design_v1.md-as-amended + spec/churn_amendments.md, ED-IN-0011, 2026-07-05). Not independently ratifiable; retained as record. [status reconciled 2026-07-15, proposal-reconciliation pass, ED-IN-0069]
## Date: 2026-07-05 · Lane: IN · Judge lens: PLAYER EXPERIENCE (Q2/Q4 acceptance tests + C2/C7)

Scored against `00_engine_charter.md` §§Q2, Q4, C2, C7 and the capstone list (§153-164).
Not scored on build-cost/ratifiability except where it changes what the *player* gets.

---

## 1. The acceptance-test grid (charter, verbatim anchors)

**Q2 tests** (charter §57-79):
- **Casting quality** — ONE tie-graph rule drives every summons channel; casting explains *why-you* diegetically; same rule casts NPCs.
- **Position determines native story** — leaders get subordinate-originated beats (concern/project engine pointed upward, anti-spreadsheet); members get duties-with-refusal-costs.
- **Factionless on-ramp** — EXPLICIT acceptance test: "a factionless PC gets playable seasons" (§68).
- **Social-scale ladder** — individual→family→settlement→territory→faction→world, each rung names its carrier; family is the thinnest rung.
- **Impulsion** — pressure arrives as choices with deadlines (diegetic clocks, forced-choice M-6 turns).
- **History conditions option space** — gating / pricing (preferred) / foreclosure / pattern-response; every gate cites its ledger cause.

**Q4 tests** (charter §107-135):
- **Surface map** — Tier-1 ambient / Tier-2 cut scenes (rationed) / Tier-3 chronicle / **texture-between-scenes** (immersion-audit gap) / the slate.
- **Watching vs participating** — "every major arc keeps ≥1 open intervention point until converging and routes through ≥1 playable scene" (§120-121).
- **Legibility acceptance criterion** — each surface answers ≥1 of the three dramatic-legibility questions.
- **Anti-oatmeal** — typed register vectors; ERA bake gate; arc_test_batch as narrative regression (5 seeds differ in named actors, stakes, outcomes).
- **Trails** — causes[] walk as in-world media.
- **Beat budget & pacing** — per-tier season budgets inside the 3-5 scene envelope; director owns the tension curve.

**C2** (absolute): no narratological surfacing — the doc-12 veto (charter §29-31, `03_prior_art §a` doc-12).
**C7** (absolute): never railroads — engagement windows real/seed-testable; pricing preferred over gating; foreclosure via arc events only (§40-41).

---

## 2. Per-architecture verdict on the lens

### Architecture A — Minimal Detector

- **Casting (Q2):** WEAK. Rides the existing tie-graph, but only for the 8 markers, which are overwhelmingly faction/territory tier. No new casting surface. `why-you` works only where a marker's `participating_actors[]` happens to intersect a Bond/Duty.
- **Position (Q2):** ABSENT. The architecture's own Q2 concedes leader-beat routing "has no owner" because it deliberately does NOT claim `game_director` or resolve the `scene_entered` conflict (`module_contracts.yaml:349,375`). Position-determines-native-story is "not addressed at all."
- **Factionless on-ramp (Q2):** FAILS the explicit acceptance test. Its own text: the family rung and the factionless on-ramp "get NOTHING new from a minimal detector." No playable-seasons guarantee for a factionless PC.
- **Impulsion (Q2):** THIN. Deadline pressure surfaces via the marker cut scene only.
- **History/option-space (Q2):** partial — rides constituent-arc gates but builds no new pricing/foreclosure surface.
- **Surface map / texture (Q4):** render gap closed (trigger-table completion + NLG graduation), but texture-between-scenes explicitly NOT addressed; trails get no dedicated surface; pacing deferred.
- **Watching vs participating (Q4):** FAILS the headline Q4 test — "cannot be guaranteed; there is no converging lifecycle state to hold a window open until… fires AT the convergence instant, not across an escalation the player can enter earlier." This is the single most visible Q4 shortfall.
- **Anti-oatmeal (Q4):** weak — capstone #11 two-seed divergence rides only stat-flips; #8 meaningfulness test unbuilt.
- **C2:** STRONGEST of the three by construction — one new state (a fired-set), no lifecycle labels, no salience ledger; plus an explicit C2 literal-string bake-audit lint. Least surface to leak.
- **C7:** MODERATE — anti-railroad holds through downstream stat change, but no engagement-window guarantee and no new pricing machinery.

Player-experience read: A closes the EDs and gets prose on screen, but it is the weakest possible answer to the two questions this lens weights. Q2 is "the question minimalism serves worst" (its own words), and it fails the Q4 intervention-window test outright. Its only lens win is C2 safety.

### Architecture B — Arc-Vector Engine

- **Casting (Q2):** STRONGEST. ONE casting resolver reads each vector's `participating_actors[]` against the tie-graph (Duty/Conviction, Bonds/Knots, lifepath/location, Standing, position); `why-you` = the matched tie edge surfaced diegetically. Same rule casts NPCs into `participating_actors[]` (co-protagonists, one ledger). Rides `player_agency_v30 §4`'s 7-priority slate for channel placement.
- **Position (Q2):** BUILT. Leaders — a vector with `scope.faction=leader's` subscribes to `npc_behavior_v30 §5` concern/project Keys (filter target=leader), injects reports-as-scenes / requests-for-ruling as named actors with wants (anti-spreadsheet honoured). Members — `stakes_tags:[pricing]` duties with refusal costs under T-30 asymmetry.
- **Factionless on-ramp (Q2):** THE ONLY architecture that structurally satisfies the explicit acceptance test. Builds the vector ladder: Conviction/Duty vectors → TE-tier settlement arcs → Standing/Obligation proto-currency → recruitment-as-arc → GD-3 build-your-own. A factionless PC has live vectors, therefore playable seasons.
- **Social ladder (Q2):** traverses rungs on the same aggregate-up/distribute-down transport as state (Domain Echo up, faction-pressure down, NPC-ARC↔NPC-ARC lateral, TE-recruits-NPC diagonal).
- **Impulsion (Q2):** present via `activity_mode:clock_escalation` + `temporal_window`; forced-choice turns = escalating-state exit conditions. (Thinner than C — see graft 5.)
- **History/option-space (Q2):** four `stakes_tags` (gating / pricing-preferred / foreclosure→`lifecycle:abandoned` / pattern_response), each carrying `ledger_cause` as a schema field — "every gate cites its ledger cause" becomes CI-checkable. Best of the three.
- **Surface map / texture (Q4):** slate injection + salience routing (§3.3 accumulator generalized). Trails = the causes[] walk as in-world media, enabled by causes[] population. BUT pacing/texture-between-scenes DEFERRED to the NLG lane; inherits articulation's "fire whenever triggers match" no-rationing gap.
- **Watching vs participating (Q4):** SATISFIES the headline test structurally — the lifecycle invariant "every escalating major vector carries ≥1 pending injection candidate until converging and routes through ≥1 playable scene." Because lifecycle state is first-class, the window is a real object held open until the `converging` transition. Capstone #4 counter-case (followed-only vector) is representable.
- **Anti-oatmeal (Q4):** STRONGEST. The arc-vector payload IS the prose slot set; two-seed chronicles differ in named actors/stakes/outcomes by construction and it is *verifiable because vectors are data* (capstone #11). ERA + arc_test_batch are bake gates fed by arc-vector variety.
- **C2:** MODERATE. Builds lifecycle/convergence-window state, but it is internal and surfacing is delegated to the NLG realizer (payload internal, C2/C4). Lower leak risk than C because the engine is data+state, not a tension-curve director; but it must still adopt a C2 lint on the lifecycle state (see graft 4).
- **C7:** STRONGEST. FSM branches on outcome (ARC-S07 floor-6 vs Loyalty-0→ARC-T13), seed-testable via arc_test_batch; pricing preferred; foreclosure only via arc events; engagement window guaranteed by lifecycle invariant. Full C7 answer.

Player-experience read: B is the fullest Q2 answer (casting, position, factionless on-ramp, four-mode history) and satisfies the two most concrete Q4 acceptance tests (intervention-window guarantee, anti-oatmeal two-seed) — while being SAFER on both absolute constraints (C2, C7) than C. Its Q4 gap is precisely the pacing/texture/rationing zone, which is C's home turf and gained by graft.

### Architecture C — Director Layer

- **Casting (Q2):** STRONG-but-derivative. The tie-graph rule itself lives in `player_agency §4` Steps 3-5; C adds casting-channel *arbitration* — holds the ≤3/season Outreach budget and the Mandatory-Crisis override ordering. Real Q2 value (which summons fire, in what order) but does not itself own the casting rule.
- **Position (Q2):** BUILT via the concern/project engine, and C uniquely *rate-limits* which concerns surface as scenes vs demote to texture (salience economy on Q2 inputs). Strong.
- **Factionless on-ramp (Q2):** MENTIONED (Conviction/Duty ladder) but not built as a first-class carrier the way B builds it; C schedules existing channels rather than constructing the on-ramp vectors. Weaker than B on the explicit acceptance test.
- **Impulsion (Q2):** STRONGEST — the director owns the diegetic-clock cadence, scheduling forced-choice M-6 turns (`scale_transitions §4.3.2`). This is the graft-worthy Q2 element.
- **History/option-space (Q2):** four modes at slate-generation time, gates cite ledger cause; foreclosure budgeted to majors. Comparable to B.
- **Surface map / texture (Q4):** STRONGEST — and uniquely closes the texture-between-scenes immersion gap: texture IS the demotion destination (a demoted arc's beats become texture, not nothing — total accounting), routed to Tier-1 ambient. Neither A nor B addresses this.
- **Watching vs participating (Q4):** STRONGEST enforcement — per-arc participated (slate/texture) vs watched (Witness/cut/chronicle) counters; "a major arc cannot be all-watched before converging (CI-checkable)." This turns the Q4 acceptance test into an enforced invariant, stronger than B's structural-but-unenforced version.
- **Legibility criterion (Q4):** owns surface routing/salience → best positioned to guarantee each surface answers ≥1 dramatic-legibility question.
- **Beat budget & pacing (Q4):** its raison d'être. Closes the rationing gap articulation §3 explicitly lacks ("fire whenever triggers match"); allocates the 3-5 scene envelope across Tier-2/slate/texture. The charter NAMES D11 the tension-curve owner (§128).
- **Anti-oatmeal (Q4):** feeds ERA via arc-vector variety but does not OWN the arc data (B does) — so the two-seed divergence guarantee is weaker/derived.
- **C2:** HIGHEST RISK — its own #1-severity risk: "the director's ENTIRE state IS the narratological state the doc-12 veto forbids surfacing (tension curve, salience ledger, arc/lifecycle labels)." Mitigated by a hard internal/external boundary + C2-lint, but the risk is structural and load-bearing. For a lens that treats C2 as absolute, this is the decisive mark against C.
- **C7:** HIGHEST RISK — over-orchestration→railroad is its #1 risk; "booking guarantee as a floor not a ceiling funnels every season into the current major," plus the doc-10 §8.5 "designed dramatic timing" NOT-list. Mitigated by curve-as-ceiling + Witness-Mode valve, but the tension-curve-owning director is structurally the most railroad-prone.

Player-experience read: C is the fullest Q4 answer and the only one to close the texture/pacing/rationing gap and to *enforce* the watching-vs-participating ratio. But it buys that supremacy at the highest C2 leak risk (its whole state is the forbidden state) AND the highest C7 railroad risk — the two constraints this lens must never trade away — and its Q2 casting/factionless answers are derivative of B's underlying data.

---

## 3. Scoring (0-100, player-experience lens)

| Test | A | B | C |
|---|---|---|---|
| Casting quality (Q2) | weak | **strong** | strong (derivative) |
| Position → native story (Q2) | absent | **built** | built + rate-limited |
| Factionless on-ramp (Q2, explicit) | **fails** | **satisfies** | mentioned only |
| Impulsion (Q2) | thin | present | **strongest** |
| History/option-space (Q2) | partial | **strongest (CI-checkable)** | strong |
| Surface map / texture (Q4) | render only | slate+trails, no texture | **texture closed** |
| Watching vs participating (Q4) | **fails** | satisfies (structural) | **enforced (CI)** |
| Legibility criterion (Q4) | minimal | salience-routed | **owns routing** |
| Anti-oatmeal two-seed (Q4) | weak | **structural/verifiable** | derived |
| Beat budget & pacing (Q4) | deferred | deferred | **owns it** |
| C2 (absolute) | **safest** | moderate | **highest risk** |
| C7 (absolute) | moderate | **strongest** | highest risk |

**Totals:** A = **58** · B = **82** · C = **76**.

Rationale for B > C on this lens: the tests split — B wins casting, factionless on-ramp (the explicit test), four-mode history, anti-oatmeal, and C7; C wins impulsion, texture, watching-ratio-enforcement, legibility-routing, and pacing. But (1) B wins the one EXPLICIT acceptance test (factionless playable seasons) that C only gestures at, (2) B is SAFER on both absolute constraints C2/C7 while C is riskiest on both, and (3) C's wins are concentrated in the pacing/surface/rationing zone that grafts cleanly onto B, whereas B's Q2 depth (typed vectors, participating_actors) is the *substrate C's scheduling reads* and cannot be grafted the other way without rebuilding C into B. A is a distant third: it fails the factionless test and the intervention-window test — the two sharpest player-experience acceptance tests — its only lens virtue being C2 minimalism.

**Winner: Architecture B — the Arc-Vector Engine.**

---

## 4. Grafts — what the synthesis MUST keep from the non-winners

From **C (Director Layer)** — the entire pacing/surface layer B defers:
1. **Beat-budget rationing** (graduate articulation §7 D11): allocate the 3-5 scene-action envelope (`player_agency §4.3`) across Tier-2/slate/texture. B inherits articulation's "fire whenever triggers match" no-rationing gap; without this the Q4 beat-budget test is unmet.
2. **Texture-between-scenes as the demotion destination**: a demoted arc's beats become texture (rumor/overheard/documents → Tier-1 ambient), not nothing — total accounting. Closes the immersion-audit gap neither A nor B touches (Q4 surface map).
3. **Watching-vs-participating ratio as a CI-checkable invariant**: per-arc participated vs watched counters; a major arc cannot be all-watched before converging. Stronger than B's structural-only lifecycle invariant for the Q4 headline test.
4. **The C2 hard internal/external boundary + C2 literal-string lint applied to ALL arc-lifecycle/salience state**: B builds the same leak-prone lifecycle state, so it must adopt C's mitigation, not just A's bake-fragment lint. Demotion manifests only diegetically (summons→rumor).
5. **Director-owned diegetic-clock / impulsion cadence** (`scale_transitions §4.3.2` forced-choice M-6 scheduling): B's impulsion is thinner; graft C's cadence ownership for the Q2 impulsion test.

From **A (Minimal Detector)** — the architecture-neutral render-path fixes that must ship regardless of engine:
6. **The §3.1 trigger-table completion**: add `combat_resolved`, `investigation_resolved` (the ED-IN-0004 root, `§6.4 [ASSUMPTION]` discharge) **plus the four ED-681 Rendering-Crisis thread beats** (`threadwork_v30 §3.7`) — C6 is a hard constraint and is closed only by this edit, whichever engine sits above it.
7. **NLG realizer graduation with the ARC-S07 worked example** + coherence/Certainty tables→runtime lookups + C2 literal-string bake-audit lint: this is the Q4 render path and capstone #10, architecture-neutral. Keep A's concrete graduation plan and its explicit total-accounting DISCARD-with-reason logging for non-firing predicates.

From **C**, one more (Q3-adjacent but load-bearing for legibility):
8. **The trigger-9 cosine-similarity sim-validated primitive** (articulation §3.1 trigger 9, 4-season window, ±0.40, corr +0.937 at the Crown/Hafenmark pair) generalized to arc-vector pairs — this supplies the **temporal window** B's COLLISION conjunctions lack register-wide (dossier finding: no COLLISION specifies a temporal window; charter Q3 names it required). Use it as B's convergence correlation test rather than un-windowed predicate conjunctions.

---

## 5. Open items the synthesis inherits (not this lane's to resolve)

- `mechanical.scene_entered` ownership (scene_slate vs game_director, `module_contracts.yaml:349,375` [OPEN — Jordan]) — B and C both resolve it in game_director's favour; A leaves it open. The synthesis should adopt B/C's resolution (game_director single-sources; scene_slate = candidate/manifest generator) because leader-beat routing (Q2 position test) has no owner otherwise.
- Per-arc lifecycle-state field ownership (Class B extension of `npc_behavior` arc-state bucket `L150` vs new game_director/scenario_authoring store) — recommend engine-owned store per dossier.
- `temporal_window` rule for convergence (same-season / same-Accounting / N-season) [OPEN — Jordan] — graft 8 supplies a concrete default (4-season cosine window).
- Coup-Counter→Löwenritter-Autonomy migration + ARC-T04 dangling ID — corpus defects blocking full compile; player-experience-neutral but block the capstone trace.
