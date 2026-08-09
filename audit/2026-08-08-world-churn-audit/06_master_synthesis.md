# World Churn — the master synthesis: reconciliation, consolidation, orchestration

## Status: PROPOSED. Read-only audit. Nothing executed, no canonical head moved, no flag flipped, no design text changed.
## ⚠ HELD, LOUDLY (ED-1094): Part V is a list of decisions that are **Jordan's**. Merging this PR ratifies the *audit* — the measurements, the reconciliations, the sequencing rationale. It does **not** ratify a single Part V ruling, and no Part IV item may be built until the ruling it blocks on is made. If this document is merged and Part V is treated as settled, that is the failure ED-1094 exists to prevent.
## Date: 2026-08-09 · Lane: IN (cross-cutting) · ED-IN-0148 · Tree state: `690f4c3`, working tree clean
## Supersedes as the reading surface: `00_findings.md`, `01_plan.md`, `02_adversarial_review.md`, `03_causal_model.md`, `04_throughline_permutations.md`, `05_key_catalogue.md` — all six remain authoritative for their detail; this document is the reconciled index over them and, where they disagree, the adjudication.

---

## Part 0 · What this document is, and the rules it holds itself to

The session asked one question in escalating forms: **how does Key-substrate state change over a
campaign as subsystems interact, and do the primitives compose into emergent conditions that reach
NPCs, arcs and events?** Six documents, twenty-two read-only lenses and four adversarial passes
answered it in pieces. This document reconciles those pieces, consolidates them into one model, and
orders the work that follows.

Three self-imposed rules, because the answer is only worth what its weakest claim is worth:

1. **Every number carries its derivation or its instrument.** Topology figures come from
   `topology_probe.py`, committed alongside this document and re-runnable. Numbers I published
   earlier in the session that the probe does not reproduce are **retracted in Part I.1**, not
   quietly restated.
2. **Semantic verification, not lexical.** A term appearing (or not appearing) is not evidence.
   Where a claim rests on grep it is labelled as resting on grep, and the dynamic-access blind spot
   is checked by hand — Part I.2.B is the worked example.
3. **Disagreement is recorded, not smoothed.** Where the six documents contradict each other, or
   where an adversarial pass overturned an earlier claim, the overturn is printed. A synthesis that
   hides its disagreements is not evidence.

---

# PART I · RECONCILIATION

## I.1 · Retractions — numbers I published this session that do not reproduce

The topology figures I gave in conversation were miscounted. `references/key_graph.json` is
**unchanged** since `f09984e` (verified: clean working tree, no intervening commit), so this is my
arithmetic error, not graph drift. The probe is the falsifier.

| Published in session | Measured by `topology_probe.py` | Verdict |
|---|---|---|
| "16 of 27 modules consume nothing" | **15 of 27** pure sources | **Retracted → corrected.** Direction unaffected. |
| "108 of 125 consume-declarations on four modules" | **109 of 127 (86%)** | **Substantively confirmed**, figures corrected. |
| "32 broadcasts : 3 seams : 11 nexus" | **Unreproducible at any threshold.** Max fan-out in the graph is **4 consumers**; the histogram is 0→8, 1→4, 2→16, 3→21, 4→7. There is no cut yielding 11 of anything. | **Retracted in full.** |

**The retraction has a consequence downstream.** The synthesis lens built its closing argument on
"nine of eleven nexus keys are witnessing." At the declared ≥4 threshold there are **seven** highest-
fan-out key types, of which **four** are scene-scale witnessing events (`scene.battle_concluded`,
`scene.dialogue`, `scene.insult`, `scene.threat`); the other three are `da.antinomian_action`,
`da.covert_betrayal`, `env.peninsular_strain_shock`. The claim *"the substrate's native metaphor is
witnessing"* therefore survives **directionally but weakened**: 4 of 7, not 9 of 11. It is now an
observation, not a majority argument, and Part III does not lean on it.

That lens flagged, unprompted, that it had not re-verified the handed figures. It was right not to
trust them.

## I.2 · Contradictions inside the corpus, adjudicated

### A. Accord is three unit systems on one field — and one of them is a live bug

This is the session's single strongest concrete finding, and it was reached semantically: canon text
→ mapping table → bucket function → each comparison site read individually.

`Territory.accord` is written and read in **three incompatible units**:

| Unit | Where | Range |
|---|---|---|
| Canonical integer | canon docs (`victory_v30.md:81-86`) | 0–4 |
| Continuous | `Territory.accord`, via `ACCORD_MAP = {0:1.0, 1:2.5, 2:4.0, 3:5.5, 4:7.0}` (`game_state.py:58`) | 0.5–7.0 |
| Granular delta | `adjust_accord(d)` → `accord + d/MULTS['accord']`, `MULTS['accord']=10` (`game_state.py:42,156-157`) | ±N/10 |

`engine/substrate/canon_buckets.py:38` owns the continuous→canonical conversion
(`canonical_accord`, midpoints 1.75 / 3.25 / 4.75 / 6.25). **It is a single-owner primitive with
unrouted call sites.** Every live consumer of `.accord` was read:

- `systems/overview/sim/accounting.py:88` — **correct.** Buckets through `canonical_accord` before
  comparing, and its own docstring (`:58-60`) explains why mixing the two is forbidden.
- `engine/autoload/victory.py:71` — **WRONG, and live.** Compares the raw continuous value against
  `ACCORD_MIN = 2.0` (`:28`).
- `systems/factions/sim/insurgency_pipeline.py:231` — **WRONG, latent.** Compares a raw continuous
  average against `INSURGENCY_PROMOTE_MIN_ACCORD = 4` (`:46`).

**The live bug, stated exactly.** Canon requires canonical **Accord ≥ 2** in every held territory —
stated four times (`victory_v30.md:44`, `:63`, `:85` *"PV counts only at Accord ≥ 2"*, `:180`).
Canonical 2 is continuous **4.0**. The code compares against continuous **2.0**, which buckets to
canonical **1** — and 2.0 sits *below* even `ACCORD_MAP[1] = 2.5`, so the gate excludes only
canonical 0 (Revolt). Canon defines Accord 1 as *"Resistant: no Prosperity contribution, Govern Ob
+1, garrison required"* (`:83`) — the state canon most explicitly means to exclude.

**The design consequence is larger than the arithmetic.** Canon sets military conquest → Accord 1
(`:86`) and says the seizer *"must govern what it seized"* (`:311`). Under the live gate, a faction
that takes all fifteen territories by force sits at canonical Accord 1 everywhere **and wins
immediately**. The victory condition's entire governance burden — the design's answer to "conquest
should not be sufficient" — is bypassed by a unit mismatch. This is the second vacuous leg of the
same condition: `00_findings.md` D2 already showed the `PS ≤ 6` leg is vacuous because nothing
writes Turmoil. **Two of the three legs of the only victory condition in the game do not constrain.**

**The pattern, not the instance** (CLAUDE.md §0.1 point 5): the code was correct when written and
broke when the continuous representation arrived. One owner exists; the sites are not routed
through it; there is no guard. **The guard is nameable, which is the test that the pattern is
understood:** a test that fails on any comparison of `.accord` against a numeric literal outside
`canon_buckets`. Filed as the P0-6 item in Part IV. Until it exists, every future Accord threshold
inherits the hole.

*Held for Jordan (J-A):* the fix direction. `ACCORD_MIN = 2.0` → `canonical_accord(t.accord) >= 2`
matches canon text but **tightens a live gate by roughly one and a half buckets** and will change
every seeded campaign outcome. That is a balance decision, not a typo repair.

### B. The material world does not exist — verified against the dynamic-write blind spot

`00_findings.md` contains **no fiscal finding at all**, while `03_causal_model.md` ranks the fiscal
edge **#1** in the build order. That gap is this document's most consequential reconciliation; the
findings register was simply missing its highest-ranked subject. Recorded here as **D13**.

**Where money comes from: nowhere.** `run_accounting` has no Treasury-accrual step. The circuit
settlement production → extraction → treasury → expenditure → world is open at the first joint.

**Where it goes: four places, all costs.** Every mutation site of faction Wealth:

| Site | Constant | Sign |
|---|---|---|
| `faction_action.py:515` | `MUSTER_WEALTH_COST = 1`, applied negated | cost |
| `crown_initiative.py:90` | `ROYAL_PROGRESS_WEALTH_COST = -2` | cost |
| `crown_initiative.py:160` | `GREAT_WORK_WEALTH_COST_PER_SEASON = -1` | cost |
| `crown_initiative.py:245` | `CORONATION_WEALTH_COST = -2` | cost |

**Zero income sites — and this claim survives the blind spot.** A literal grep would miss the one
dynamic write path, `echo_transport.py:436` (`f.adjust(_stat, _delta * MULTS[_stat])`), where the
stat name is a variable. It was traced by hand to every producer of that variable:
`parliamentary_bridge.py:209` supplies `COMPOSED_GENRE_STAT = {"Memory":"L", "Projection":"I"}`
(`:74`); `scene_dispatch.py:267` supplies `"Mil"`; `:343` supplies `"L"`; `domain_echo.py:213`
supplies a fixed rule table over `Stability`/`Mandate` only (`:191-197`). **The reachable set is
{L, I, Mil, Stability, Mandate}. `W` is not in it.** Wealth has no income path, literal or dynamic.

**And the costs are no-ops anyway.** `MULTS['W'] = 100`, so a granular cost of −2 moves Wealth by
−0.02, against a floor clamp of 0.5. **In the live sim the material layer imposes no constraint:
war is a pure decision.** An army eats nothing, a treasury fills from nowhere, a siege costs the
besieger only time.

**The one number that would close the circuit is specified twice, 5× apart.** The gold a settlement's
Prosperity contributes to faction Treasury is **Prosperity × 10** (`derived_stats_v30.md:308`) and
**Prosperity × 50** (`settlement_layer_v30.md:47`). Neither is implemented; both are canon-marked.
*Held for Jordan (J-B).* Note the second is itself flagged "PENDING — Not canonicalized" upstream
(`settlement_layer_v30.md:44`), so this is not a simple typo either.

Consequent gaps, all verified: armies starve only by ledger (flat `Treasury −100/season`, no path,
depot or convoy); no winter or quartering rule; no credit instrument, so **"victorious but bankrupt"
is not a reachable state**; and no `econ.*` Key family exists to carry any of it.

### C, D, E · Three vocabulary splits and a start-value drift

- **Conviction: three vocabularies.** Substrate 4 axes (`keys.py:59`); character sim 9 names
  (`conviction.py:46`); NPE 8 names (`npe.py:80`). Overlap between the latter two is **three**.
  Any Key→person edge built before this is ruled is shape divergence by construction. *(J-C.)*
- **Scale: four vocabularies.** `keys.py:65` 4-enum vs `handoff_rules.py:35-40` 6 labels (zero
  overlap in spelling *or* membership) vs contracts' 7 vs mechanics_index's 9. Already held as
  OI-40a / ED-IN-0103. *(J-D.)*
- **CI start value: three.** Code 30.0 (`game_state.py:244`), `CI_STARTING = 28` (`ci_track.py:71`),
  registry 28 (`clock_registry_v30.md:17`). Acknowledged in-code, unresolved. Tuning, not blocking.

### F · Cross-document reconciliations

| Disagreement | Adjudication |
|---|---|
| `00_findings.md` §1 credited NPE stance drift as live churn | **Overturned** by adversarial review: `simulate_npc_actions` iterates `world.npcs`, which a strict xfail pins empty (`test_pipeline_reach.py:596-599`). The call happens; the drift never does. |
| "10 of 13 producerless subscriptions" | **Corrected to 11 of 13.** The disconnect is worse than first claimed. Any instrument must reproduce 11, or the error is baked into the baseline. |
| Throughline register "Count: 30" | **42 entries** by parse. The register's own self-count is stale; I briefly propagated it over my own instrument, which was the wrong way round. |
| "both `stat_deltas` sites faction-facing" | **One is settlement-facing** (`echo_transport.py:319-320`). Headline unchanged: no Key reaches a person. |
| "no code path sets `owner = None`" | **Softened.** `restore_world` (`game_state.py:357`) can re-materialize it from a serialized world. Not a live-campaign path, but "anywhere ever" was one site too absolute. |
| `00_findings.md` has no fiscal finding; `03` ranks fiscal #1 | **Reconciled here as D13** (Part I.2.B). |

---

# PART II · CONSOLIDATION — one model of the state of world churn

## II.1 · The finding, in one sentence

**The world does not churn because the churn machinery is DISCONNECTED — not because it is
scripted.** This is a good result about the architecture, and it was reached independently by three
lenses in their own words. The guardrail against scripting drift **held**: across twenty-two lenses,
exactly one entity-hardcoding instance was found (`pr119_event_deck_engine.py:74-75,115`), and it
sits in the zero-caller `sim_harness` prototype cluster. **The work ahead is wiring, not redesign.**

## II.2 · What actually churns (the honest inventory)

Season is the only world tick (`mc_v18.py:260-267`). Three closed loops:

1. **The political spine — LIVE, compounding, default-ON.** World `L`/`Sta` → per-season
   parliamentary vote → writes `L` immediately (`parliamentary_vote.py:213`) and `L`/`I` deferred at
   the accounting boundary → next season's vote re-reads the moved `L`. The one genuine,
   uncontested `world→scene→world` loop.
2. **Territory ↔ CI ↔ seizure — LIVE but broken-legged.** The seizure leg is unreachable:
   `resolve_mass_seizure` has zero callers, including tests.
3. **Conquest ↔ signals — LIVE, damped** at `[0.5, 7.0]`.

Plus genuine autonomous drift: CI +1/season, MS −1/year, and per-season stochastic faction actions.
**Factions do act on their own** — the single biggest affirmative in the audit.

## II.3 · What cannot churn — the disconnection register, consolidated

D1–D12 are stated in full in `00_findings.md §2`; D13 is added here. Condensed and re-ranked by
*leverage* — how much already-built machinery one missing edge would light up:

| # | Disconnection | Class |
|---|---|---|
| **D13** | The material layer imposes no constraint; no Treasury accrual, no Wealth income, costs clamped to no-ops, no `econ.*` family (Part I.2.B) | **Never built** |
| **D5** | Zero person-scale state changes in a seeded campaign. Conviction scars, beliefs, coherence, knots are real, correctly-wired mutable state that **nothing ever reaches**. The `world event → Key → person` path terminates at the Key: no code anywhere applies a Key's `impact_vector` or `stat_deltas` to any person store. | **Built, unreached** |
| **D1** | Insurgency pipeline: emergent, implemented, invoked every season, structurally unreachable (needs uncontrolled territory that nothing creates). Promotion is *doubly* dead. `insurgencies_formed` telemetry is always 0. | **Built, unreachable** |
| **D7** | The Key substrate is a telemetry spine, not the churn engine. 3 of 55 types emit live; exactly one closes a loop; zero Key→Key cascades are possible (`DEFAULT_CASCADE_DEPTH_MAX = 0`); 11 of 13 registered consumers subscribe to types with no producer, and at default flags 13 of 13 receive nothing. | **Declared, not running** |
| **D2 + I.2.A** | Two of three victory legs do not constrain: Turmoil has no writer; the Accord leg compares the wrong unit. | **Live defect** |
| **D4** | Battle casualties evaporate; `Faction.Mil` is a monotone ratchet with one writer that only raises it. Ten defeats cost nothing. | **Missing writeback** |
| **D10** | Treaties, mass seizure, settlement politics: whole mechanisms with no executor. `process_treaty_expirations` is called by nothing — there is **no time-driven expiration churn anywhere**. | **Built, uninvoked** |
| **D3** | The Stability-Crisis council cannot clear its own trigger — it repeats rather than compounds. | **Loop not closed** |
| **D9** | The one implemented world→scene difficulty channel idles; `scene_ob_modifier` is computed, stored, and consumed by nobody. | **Built, unread** |
| **D11** | Arcs are generated from documents, not churn — and the generator reads two evacuated trees. Following it as written would recreate `arcs/`. | **Stale + doc-only** |
| **D6** | The conviction gate silently no-ops on an unknown name **and** the one call site swallows exceptions — a double silencer. | **Latent, silent** |
| **D12** | Fidelity asymmetry, measured: dozens of tracked internal variables to one scalar at the boundary, per subsystem. | **Structural** |
| **D8** | Top-down Key delivery: one live `da.*` emitter exists but no genuinely top-down *delivery* ever fires; the test "proving" direction #4 does so by reusing a bottom-up Key. | **Vacuous proof** |

## II.4 · The topology, measured

Verbatim from `topology_probe.py` at `690f4c3` (thresholds declared in the output, not inferred):

```
modules declared: 27 · pure sources 15 · pure sinks 4 · bidirectional 8
consume-declarations 127 · produce-declarations 69
top 4 consumers hold 109/127 (86%): articulation_layer=44, npc_behavior=31,
                                    faction_state=25, piety_track=9
key types 56 — orphan(0 consumers) 8 · seam(1) 4 · channel(2-3) 37 · nexus(>=4) 7
key types with no declared producer: 2/56
```

**What this shape means.** Fifteen modules emit and hear nothing. Four hear and never speak. Of the
eight bidirectional modules, only `personal_combat` and `settlement_layer` are close to balanced;
`articulation_layer` is 44-in / 1-out. Read structurally, this is not a telephone exchange of
point-to-point wires, and it is not a router: it is **a public square with four standing audiences**
— people, factions, faith, narration. The concentration is not a defect to be flattened. What is
missing is (a) anything worth hearing at world scale, and (b) rule content in the ears — every one
of the 127 declarations is a subscription with no behaviour behind it.

## II.5 · Latent traps — inert today, wrong tomorrow

- **`temperaments.py` read/write asymmetry**, exactly the §0.1-point-1 class: the writer stores into
  `world.npc_drift_state`; the reader cannot accept a `world` argument at all. Any world-scoped
  drift write would be invisible to every read. Both sides currently zero-caller.
- **Two Accord unit dialects** at settlement/territory grain, monitored only by a report-only probe.
- The three vocabulary splits of Part I.2.C/D.

---

# PART III · THE ARCHITECTURE RULING — wrapper, or sockets?

The framing put to this audit was a fork: *"either there is a wrapper that sews everything together
and distributes, or the modules need to be robustly configured to connect with other modules where
they have many inputs not just many outputs."*

**Both pure forms have already been tried in this repo, and the tree refutes each.**

**The wrapper already exists.** `run_accounting` reads every track, recomputes CI, MS, insurgency
and NPE drift every season — and emits **zero Keys**. That is the wrapper's characteristic failure:
every band crossing is a private event of one function, and central code with no consumers has no
falsifiers. Its other costs are visible on disk too — a distributing wrapper must decide what events
*mean*, which drags every module's interpretation rules into one file; the corpus's one specimen of
centrally-resolved multi-way politics resolves by enumerating **named NPCs' reactions per outcome**,
which is scripting drift arrived at honestly, because a central author has no local state to
generalise over, only cases. And it ports to Godot as a monolithic autoload owning everyone's rules
— the exact inversion of the ruled one-subsystem-one-module-tree shape.

**The mesh already exists too — on paper.** 127 consuming declarations with no runtime behind any of
them. Declaration is cheap; **rule content is the entire cost**, and it scales by authored meaning,
not by subscription. Worse, the mesh is structurally deaf exactly where world churn lives: the
"derive, never write" rule forbids any module from writing Mandate, province Accord or band state —
so **no module is licensed to announce that they moved**. Adding inputs to modules cannot produce a
signal nothing is permitted to send.

**So the dichotomy is false, and the substrate has already voted for the resolution.** The criterion
that assigns each responsibility to exactly one side:

> **Detection is central where derivation is central; interpretation is always local.**
> A responsibility belongs to the boundary iff its truth is produced by *aggregation* — no single
> module could emit it without violating "derive, never write" or duplicating the derivation. A
> responsibility belongs to a module iff its effect depends on the *receiving entity's own state*.
> The Key is the only thing that crosses.

Which yields three assignments:

1. **The boundary becomes a herald, not a distributor.** `run_accounting` gains exactly one new job:
   **publish what it already computes.** It decides nothing and routes nothing.
2. **Every effect rule stays local.** Whether a fact scars a person depends on that person's
   convictions; whether a settlement complies depends on its own `L`. A subscription without rule
   content is decoration and should not be declared.
3. **Distribution is data, not code.** The router a wrapper would centralise **already exists as
   schema**: the five-role `targets[]` vocabulary, which no live emitter uses as more than a single
   element. One revocation Key whose `targets[]` lists every chartered settlement of a faction-type
   *is* the distribution mechanism.

One structural note in the mesh's favour, which changes how the whole thing should be read:
`DEFAULT_CASCADE_DEPTH_MAX = 0` plus boundary-deferred apply means a consumer that reacts by
emitting does so **next season at the earliest**. This is not a runaway reactive network — it is a
**clocked relay, one causal hop per season**. The termination guard, which reads as a limitation,
hands the design news-travels-at-horse-speed latency for free.

**The one-sentence answer to the fork: the world churns when its consequential changes become
witnessable public facts.** The boundary makes derived change witnessable; `targets[]` makes power's
reach witnessable; modules are witnesses with stakes.

---

# PART IV · ORCHESTRATION — the programme, dependency-ordered

Ordering rule: an item appears before another iff building it later would **corrupt a measurement,
silently no-op, or force a dialect**. Everything lands flag-gated OFF unless stated. Every item
names its falsifier, per §0.1 point 3.

## P0 · Repairs and instruments — before any measurement is trusted

| # | Item | Why first | Falsifier |
|---|---|---|---|
| P0-1 | **Conviction gate loud-fail.** `apply_conviction_scar` returns magnitude 0 on an unknown name while the caller reports success — **and** the call site swallows `ImportError/AttributeError` (`knots.py:353-354`). Both layers must go. | Every scar edge in P4 no-ops through this hole *while reporting success*. | A test passing an unknown conviction and asserting it raises — and that the raise is not swallowed at the `knots.py` call site. |
| P0-2 | **Connectivity instrument**, by *extending* `tools/build_execution_map.py` — not a second `key_graph.json` parser. | §8: never re-implement a rule. Baselines everything downstream. | Must reproduce **11 of 13** producerless subscriptions and the Part II.4 figures. |
| P0-3 | **De-vacuate the two victory legs** and retire the direction-#4 test to an honest xfail. | The programme otherwise mis-scores its own campaigns. | A test that fails when Turmoil has no writer, rather than passing vacuously. |
| P0-4 | **`rs_track` → delegate to `apply_ms_delta`** (RS == MS per ED-731 — *verify the threadwork Part 5 caveat first*). | Makes the only live person→world edge land. | If Part 5 defines a distinct RS, this becomes a design question, not a delegation. |
| P0-5 | **`temperaments.py` reader signature.** | Wired-tomorrow trap; free now, silent later. | A test writing world-scoped drift and reading it back. |
| P0-6 | **The Accord unit guard** (Part I.2.A). | Without it every future threshold inherits the hole. | A test failing on any `.accord` comparison against a numeric literal outside `canon_buckets`. **This is the item that proves the pattern was understood.** |
| P0-7 | **File what this programme is not fixing** — §0.1 point 5. | Scope discipline. | The filed list exists. |

## P1 · The boundary speaks — pure publication, no semantics

| # | Item | Unblocks |
|---|---|---|
| P1-1 | Emit `mechanical.season_change` + `mechanical.accounting`, log-only, on the proven `_emit_battle_concluded` pattern. | The event deck's autumn predicate, which currently predicates on a fact with no carrier. |
| P1-2 | **Rule, then implement, derivation-crossing emission** (`mechanical.threshold_crossed`) — edge-triggered, with hysteresis, boundary-owned, carrying `contributing_key_ids`. | The keystone. Slate Step 2; deck clock predicates; settlement-stat and Mandate shifts **as instances of one rule** rather than new dialects; and the only available reconciliation of "derive, never write" with causal legibility — because only the aggregator can see the derivation. Without hysteresis: emission storm on any oscillating gate. Without it at all: every later spine mints its own crossing key, which is shape divergence by construction. |

## P2 · The economy exists

| # | Item | Blocks on |
|---|---|---|
| P2-1 | **The fiscal edge** — `realized_income = Prosperity × stance × compliance(L)` plus the L/PS consume step. Adjudicated #1 on frequency, dependency and external warrant. | **J-B** (×10 vs ×50) and ED-SE-0045. |
| P2-2 | **Then** charge the attacker: casualty writeback and conquest cost. | **Hard prerequisite, not a preference** — before P2-1, attrition without an economy produces *first-mover extermination*. Also blocks on the FACTION-P2-02 confirm: a proportional coefficient without it is a fabricated constant. |

## P3 · Control lands at the hinge; the calendar churns

| # | Item | Note |
|---|---|---|
| P3-1 | Conquest fork at settlement grain **together with** the OI-37 Accord-write reconciliation. | Apart, three writers keep bypassing the hinge and one conquest counts at three grains. |
| P3-2 | Declare `scene_outcome` at one live producer. | Near-zero cost; pairs with P3-1 or nothing consumes it. |
| P3-3 | Revolt step, **formation half only** — `owner = None` via `canonical_accord` bucketing. | A naive `== 0` check is inert forever. Promotion half held on the insurgency-L ruling. |
| P3-4 | Wire `process_treaty_expirations` into the season loop **and emit `state.treaty_changed` from inside it**. | Highest-frequency bond event in the design; without the emission the churn stays silent and the personal scale stays structurally deaf to every broken treaty. |

## P4 · People exist, and hear

| # | Item | Note |
|---|---|---|
| P4-1 | **Populate**: seed Local Actors per the settlement quota. | The `mc_v18.py:175-186` deferral premise — *"no canon head names an initial world-gen population"* — is **false one subsystem over**: `settlement_layer_v30.md:857` gives the count rule (~45–50 across 36 settlements). Do not invent a number; use that one. **Cross-lane (SE/WR) — flag as such.** Until this lands, every person-scale edge is provably vacuous. |
| P4-2 | The **Key→person applier** at ACCOUNTING_BOUNDARY. | Blocks on **J-C** (conviction vocabulary) and on ORD-3. |
| P4-3 | World-fact scar rows, **landing together with vindication** (`state.scar_removed`). | Apart, a world that only wounds converges every long-lived NPC to permanent crisis. Route all spines through **one witness adapter**, never five person-edge dialects. |

## P5 · Authority and memory

| # | Item |
|---|---|
| P5-1 | The `gov.*` authority-act family **with multi-target emission** — the first live exploitation of `targets[]`. Before P4 it is keys with no audience. |
| P5-2 | Governance outcomes emit ledger records **plus one read-back consumer** (censure→grudge, pass→precedent→deck bias, obligation→debt). |
| P5-3 | `state.grievance_formed` — sides, stakes and blame in one payload. |

---

# PART V · RULINGS REQUIRED — Jordan's, not guessed

**Blocking — nothing sound can be built while these are open:**

| Id | Ruling | What waits |
|---|---|---|
| **J-A** | Accord unit fix direction (Part I.2.A). Matching canon tightens a live gate ~1.5 buckets and changes every seeded outcome. | P0-6, the victory condition's meaning |
| **J-B** | Prosperity→Treasury: **×10 or ×50** | P2 entirely |
| **J-C** | Conviction vocabulary — recommend: store on the canonical 13, derive the 4 axes, never the reverse | P4 entirely |
| **J-D** | ORD-3 / ORD-4 ordering | any generic `stat_deltas` applier — the highest-leverage single unblock in the line |
| **J-E** | The derivation-crossing emission rule itself | P1-2, the keystone |
| **J-F** | D.6 double-count owner — a canon-internal contradiction (direct Mandate write vs pure aggregate) | P2-2, P3-1 |
| **J-G** | Population/Weight: a stock is smuggled into a derived value, and naive conservation carries a **Mandate sign-flip that rewards misgovernance-driven emigration** | all migration edges |
| **J-H** | `scene.battle_concluded` consumer-roster reconciliation (registry vs `key_graph` disagree) | P1, P2-2 |
| **J-I** | Slate-ordering owner — nothing on disk says which spec owns it | P4-3, P5 |
| **J-J** | **L0 identity**: a ratified design whose corpus was evacuated vs an unratified proposal now occupying the same slot. Leaving both true is scripting-drift-by-neglect. | arc generation |
| **J-K** | ED-SE-0045 (M multiplier) | P2-1 |
| **J-L** | FACTION-P2-02 confirm (battle→Mil coefficient) | P2-2 |

**Tuning — needed, but nothing structural waits:** grievance-class and stake magnitudes; the CI
conditional-decay term; rumour-latency distance bands; payload extensions (three-degree encoding on
`battle_concluded`, `settlement_id` on `env.population_change`, `owner_after` on
`settlement_revolt`); which conviction a knot-break scars; CI start value 28 vs 30.

---

# PART VI · DO NOT BUILD

- **A distributor wrapper or "world director."** The strongest negative here. Distribution is
  `targets[]` data plus subscription; a router module is the god-loop with better PR.
- **A unified bond primitive.** Three anti-unification rulings already on disk. The real gap is
  **converters** (marriage-as-treaty, retainer-ripening) and a shared Key surface.
- **The captive-pool as new state** — ransom, refusal and the 3-season fork are already owned. Build
  the carrier, not the state.
- **A second surfacing path for world clocks**, bypassing the deck grammar.
- **A rumour subsystem** — the clocked relay already supplies coarse latency; make existing
  peninsula-wide effects legible as `causes[]` chains instead.
- **A world-visible imminence Key** — `threshold_crossed` carries crossing *facts*, never forecasts.
- **The arc compile as specified** — its validation corpus was evacuated. Force J-J instead.
- **Per-throughline key dialects**, and **false-friend reuse** (`scene.displacement` for migration,
  `scene.combat_felled` for executions) — the term-vs-concept error, pre-empted twice by the corpus.
- **An invented NPC population count** — the count rule exists; use it (P4-1).

---

# PART VII · Weakest claims, and what would falsify this document

Carried forward honestly, because this is what the document is worth at its edges:

1. **Every stability argument is reasoned, not simulated.** Conquest frequency, whether `Sta ≤ 2` or
   Accord 0 is ever reached in a seeded campaign, and the emission volume of `threshold_crossed`
   against the per-tick cap are **unmeasured**. P0-2 exists to convert them before P2 lands. Per
   §0.1 point 4, a number without a control is not a measurement — so no number is claimed here.
2. **Several structural claims rest on grep, with its known blind spot** for dynamic and duck-typed
   access: "39 types have zero traffic", "nothing mutates insurgency L", "no code computes Mandate".
   None has a guard test. The Wealth-income claim (Part I.2.B) is the one that was *hand-verified
   through* the blind spot, and is the template for the rest.
3. **One adversarial pass is missing.** `CRITIC_fidelity.md` returned a one-line stub. The
   live-vs-declared emitter labels rest on cross-verification between lenses, not on that critic —
   well-supported but **singly audited**.
4. **RS == MS rests on three rename records**, not a specification. P0-4 is a delegation only if
   that holds.
5. **Whether publication-first evades ORD-3** — the reading that log-only emission is safe under the
   open ordering forks, and that only *appliers* need J-D, is inference, not citation. Confirm
   against the armature before P1 lands.
6. **The topology figures are a measurement of the *declared* graph.** A declaration is not evidence
   of runtime traffic — that is D7's entire point. Part II.4 describes intent, not behaviour.

---

## Appendix A · Document map

| Document | Holds |
|---|---|
| `00_findings.md` | D1–D12 in full, with the corrections applied inline |
| `01_plan.md` (v2) | Tier 0–3 items with per-item verification |
| `02_adversarial_review.md` | Both critics' verdicts, including their own weakest claims |
| `03_causal_model.md` | The generative causal model and the adjudicated build order |
| `04_throughline_permutations.md` | 42 entries, the six-concept typology, branch-collapse analysis |
| `05_key_catalogue.md` | 67 edges × complete Key sets; per-key producers, consumers, payload |
| `06_master_synthesis.md` | **This document** — reconciliation, consolidation, orchestration |
| `topology_probe.py` | The falsifier for every figure in Part II.4 |

## Appendix B · Method

Twenty-two independent read-only lenses at `fable` tier; four adversarial passes under
`valoria-critic` (structurally read-only: Read/Grep/Glob, no write tooling); relay discipline
throughout — every critic received the producer's **output**, never its reasoning. Synthesis and
authorship at `opus`, per §10's ruling that the top tier belongs on audit and guardrail nodes rather
than on artifact authorship.

Adversarial passes overturned claims **in both directions** — they killed the NPE-drift churn claim
and the "both sites faction-facing" claim, and they made D7 *worse* (10→11) and D6 *worse* (a second
silencer). A critic that only ever softens findings is not independent.
