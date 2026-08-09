# World Churn — the master synthesis: reconciliation, consolidation, orchestration

## Status: PROPOSED. Read-only audit. Nothing executed, no canonical head moved, no flag flipped, no design text changed.
## ⚠ HELD, LOUDLY (ED-1094): **Parts III, V and VI are all held — not merely Part V.** Merging this PR ratifies the *audit*: the measurements, the reconciliations, and the record of what the adversarial passes overturned. It does **not** ratify (a) any Part V ruling, (b) **Part III's architecture ruling**, or (c) **Part VI's do-not-build prohibitions**. Adversarial review caught the original header holding only Part V — which would have let the document's *largest* design decisions (the herald architecture; six standing prohibitions) ratify silently by merge while a ×10-vs-×50 constant was held explicitly. That is the ED-1094 failure mode applied one level up, and the header is corrected accordingly. No Part IV item may be built until the ruling it blocks on is made.
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

## I.1 · A retraction, and the retraction of that retraction

This section changed twice, and the sequence matters more than the numbers, because it is a worked
example of the defect class this whole audit is about.

**First pass.** I re-derived the topology figures I had given in conversation and got different
answers. `references/key_graph.json` is unchanged since `f09984e` (clean working tree, no
intervening commit), so this could not be graph drift — it had to be my arithmetic. I retracted
three figures.

**Second pass.** Preparing the adversarial brief, I asked a critic to check whether *"a defensible
alternative reading reproduces the retracted numbers — if so the retraction is itself wrong."*
Checking that question myself first, it turned out to be exactly so.

`key_graph.json` carries **56 entries, one of which is the literal key `"*"`** — a wildcard
*subscription pattern* declared in `module_contracts` by `articulation_layer` and `fieldwork_knots`,
with `well_formed: false` and no producers. **It is not a key type.** My probe had counted it as
one. Excluding it:

| Published in session | Probe **counting** the wildcard | Probe **excluding** it | Verdict |
|---|---|---|---|
| "16 of 27 modules consume nothing" | 15 | **16** | **Correct as published — retraction withdrawn.** |
| "108 of 125 consume-declarations on four modules" | 109 / 127 | **108 / 125** | **Correct as published, exactly — retraction withdrawn.** |
| "32 broadcasts : 3 seams : 11 nexus" | unreproducible | **still unreproducible** | **Retracted, and it stays retracted.** |

The wildcard alone accounts for every discrepancy: it inflates the key count 55→56 and the
declaration total 125→127, adds one to `articulation_layer`'s in-degree, and — the qualitative
change — flips `fieldwork_knots` from a **pure source** into a bidirectional module, which is
precisely the 16-vs-15 difference. It also silently reconciles a discrepancy sitting unexplained
between two parts of this document: `00_findings.md` D7 counts **55 registry types** while my first
probe printed **56**. Same wildcard.

**The third figure is genuinely gone.** The real consumer histogram is 0→8, 1→4, 2→15, 3→21, 4→7.
Maximum fan-out in the entire graph is **four consumers**. No threshold, and no alternative
definition I tried (producer-gated, module-span, family-span), yields 11 of anything. That number
was invented by me and is withdrawn without replacement.

**Consequence for the argument.** The synthesis lens built its closing flourish on *"nine of eleven
nexus keys are witnessing."* On the corrected basis there are **seven** highest-fan-out key types,
of which **four** are scene-scale witnessing events (`scene.battle_concluded`, `scene.dialogue`,
`scene.insult`, `scene.threat`); the rest are `da.antinomian_action`, `da.covert_betrayal`,
`env.peninsular_strain_shock`. The claim *"the substrate's native metaphor is witnessing"* survives
**directionally but weakened** — 4 of 7 is an observation, not a majority argument. Part III does not
rest on it, and that has been checked rather than asserted.

**Why this belongs in the document rather than in a quiet fix.** The wildcard is a *pseudo-entry
that reads as data*, and it produced a wrong number in a probe written specifically to be the
falsifier for other numbers. An instrument is not automatically more trustworthy than the memory it
corrects — it encodes its author's model of the data, and mine was wrong about what a "key" is.
`topology_probe.py` now excludes the wildcard by default, prints the inflated basis alongside, and
carries the reasoning in its docstring, so neither figure can be quoted again without its basis.

That synthesis lens flagged, unprompted, that it had not re-verified the handed figures. It was
right to flag it — and, as it happens, the figures it declined to trust were the correct ones.

## I.2 · Contradictions inside the corpus, adjudicated

### A. Accord is three unit systems on one field — and one of them is a live bug

This is the session's single strongest concrete finding, and it was reached semantically: canon text
→ mapping table → bucket function → each comparison site read individually.

`Territory.accord` is written and read in **three incompatible units**:

| Unit | Where | Range |
|---|---|---|
| Canonical integer | canon docs (`victory_v30.md:80-86`) | **0–3** |
| Continuous | `Territory.accord`, via `ACCORD_MAP = {0:1.0, 1:2.5, 2:4.0, 3:5.5, 4:7.0}` (`game_state.py:58`) | 0.5–7.0 |
| Granular delta | `adjust_accord(d)` → `accord + d/MULTS['accord']`, `MULTS['accord']=10` (`game_state.py:42,156-157`) | ±N/10 |

**A fourth divergence, found by adversarial review:** canon defines Accord as a *"Per-territory
attribute (0–3)"* (`victory_v30.md:80`) and enumerates exactly four states (3 Aligned … 0 Revolt,
`:81-84`) — while `ACCORD_MAP` and `canonical_accord` both range **0–4**. The code carries a fifth
bucket canon does not define.

`engine/substrate/canon_buckets.py:38` owns the continuous→canonical conversion
(`canonical_accord`, midpoints 1.75 / 3.25 / 4.75 / 6.25). **It is a single-owner primitive with
unrouted call sites.** The draft claimed *"every live consumer of `.accord` was read"* and listed
three. **That enumeration was incomplete — adversarial review found at least five more**, and the
correction strengthens the finding rather than weakening it:

- `systems/overview/sim/accounting.py:88` — **correct.** Buckets through `canonical_accord` before
  comparing, and its own docstring (`:58-60`) explains why mixing the two is forbidden.
- `engine/autoload/victory.py:71` — **WRONG, and live.** Compares the raw continuous value against
  `ACCORD_MIN = 2.0` (`:28`).
- `systems/world/sim/insurgency_pipeline.py:231` — **WRONG, latent.** Compares a raw continuous
  average against `INSURGENCY_PROMOTE_MIN_ACCORD = 4` (`:46`). *(Path corrected: this module is in
  the WR lane, not FA as the draft cited.)*
- `systems/settlements/sim/settlement.py:120` — **WRONG, live, and a FOURTH dialect.** Derives
  settlement Order as `math.floor(t.accord)` — bypassing `canonical_accord` entirely, and
  disagreeing with it: `floor(2.5) = 2` where `canonical_accord(2.5) = 1`. This is the precise drift
  `canon_buckets.py:43` warns about, committed in live code.
- `systems/factions/sim/faction_action.py:156` (`t.accord < LOW_ACCORD_SEED = 4.0`) and
  `systems/factions/sim/crown_initiative.py:56, :101` (`t.accord <= 2.5`), `:109` — raw continuous
  comparisons against literals. These appear **deliberate and commented**, which is exactly why the
  P0-6 guard needs an **allowlist story** the draft did not mention: a guard that fires on every
  literal comparison would fire on intentional ones too. Filed into P0-6.
- `systems/world/sim/npe.py:184-189` — **correct.** Buckets through `canonical_accord`.

**The live bug, stated exactly.** Canon requires canonical **Accord ≥ 2** in every held territory —
stated three times in live text (`victory_v30.md:44`, `:85` *"PV counts only at Accord ≥ 2"*, `:180`,
reinforced at `:311`). *(The draft cited `:63` as a fourth; adversarial review found `:63` sits inside
§0.1, struck `[SUPERSEDED-BY: GD-1]` at `:52`. One of four supporting citations was superseded text —
removed. The claim does not depend on it.)*
Canonical 2 is continuous **4.0**. The code compares against continuous **2.0**, which buckets to
canonical **1** — and 2.0 sits *below* even `ACCORD_MAP[1] = 2.5`, so the gate excludes only
canonical 0 (Revolt). Canon defines Accord 1 as *"Resistant: no Prosperity contribution, Govern Ob
+1, garrison required"* (`:83`) — the state canon most explicitly means to exclude.

**The design consequence — corrected, and smaller than the draft claimed.** The draft wrote that a
faction taking all fifteen territories by force *"wins immediately"*, its governance burden bypassed.
Adversarial review broke that vignette on two counts, both verified:

1. **`SUSTAIN_SEASONS = 2`** (`victory.py:30`, streak logic `:76-84`) — qualification must hold two
   consecutive seasons. Nothing is immediate.
2. **Conquest is a delta, not a set-to-Accord-1.** `ACCORD_STORM = -25` granular → **−2.5**
   continuous, `ACCORD_TERMS = -10` → −1.0 (`faction_action.py:76-77,482,493`). Storming a
   canonical-2 territory (4.0) leaves 1.5; storming a canonical-1 territory (2.5) leaves the 0.5
   floor. **Both fail even the buggy 2.0 gate.** A conqueror must still Govern territories back up.

**What survives, and it is still the strongest finding here:** the bar is set at continuous **2.0**
where canon requires **4.0** — a gate at *half* its intended height, admitting canonical-1
("Resistant": no Prosperity contribution, garrison required) where canon admits only Compliant and
above. The governance burden is **halved, not bypassed**. Combined with D2 — the `PS ≤ 6` leg is
vacuous because nothing writes Turmoil — **two of the three legs of the only victory condition in
the game fail to constrain as designed.**

**The pattern, not the instance** (CLAUDE.md §0.1 point 5). *One qualification from adversarial
review, accepted:* the draft asserted this "was correct when written and broke when the continuous
representation arrived." That is **UNSUPPORTED** — `victory.py:6` and the continuous `ACCORD_MAP`
(`game_state.py:5,36`) are both headed Phase 1, 2026-05-17, so the on-disk evidence says
**born-mismatched**, not correct-then-broken. The pattern conclusion is unaffected and if anything
stronger: one owner exists, at least three live sites are not routed through it, a fourth bucketing
dialect exists in `settlement.py`, and there is no guard. **The guard is nameable, which is the test that the pattern is
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
(`:74`); `scene_dispatch.py:267` supplies `"Mil"`; `:343` supplies `"L"`. **The reachable set is
{L, I, Mil}. `W` is not in it.** Wealth has no income path, literal or dynamic. An independent
adversarial census of every `.adjust(` site, every `setattr`, and the deserialization path reached
the same conclusion and judged this *"the strongest inference in the corpus."*

> *Two trace corrections, both in the safe direction.* The draft's reachable set also listed
> `Stability`/`Mandate` via `domain_echo.py:213`'s rule table (`:192-199`, not `:191-197` as cited).
> Neither can actually be reached: `compute_thread_echo` has **zero callers**, and neither name is a
> `MULTS` key, so `echo_transport.py:435`'s `_stat in MULTS` guard would drop them regardless. The
> set is narrower than claimed; `W` is still not in it.

**But "the costs are no-ops anyway" was FALSE, and the correction makes the finding sharper.** The
draft reasoned that `MULTS['W'] = 100` turns a −2 cost into −0.02. Adversarial review caught that
`crown_initiative.py` **pre-multiplies**: `_MULTS_W = 100` (`:32`), so `crown.adjust('W',
ROYAL_PROGRESS_WEALTH_COST * _MULTS_W)` (`:90`) lands a full **−2.0**, as the code's own log line
says (`:91`); likewise `:160` (−3.0) and `:245` (−2.0). These fire from `faction_take_action`
(`faction_action.py:278-286`), which runs every season. Only Muster (`:515`, no pre-multiply) is the
−0.01 no-op the draft described — **one of four sites, not four of four.**

**And Wealth is consequential in the live sim:** it gates Great Work (`crown.W >= 3.0`,
`crown_initiative.py:313`) and sizes the muster pool (`pool = Mil + floor(W/2)`,
`faction_action.py:518`).

**So the corrected headline is worse, not milder.** Not *"the material layer imposes no
constraint"* — that flourish is withdrawn — but: **real, full-sized costs draining a non-renewing
stock that has no income and gates military and prestige capacity.** The material layer is a
**one-way ratchet**. Factions can only get poorer; wealth-gated options progressively disappear; and
because nothing refills the stock, the long-run equilibrium is universal impoverishment rather than
an economy. D13's "costs clamped to no-ops" is struck. **J-B's framing and P2's premise are
rewritten around *real costs, zero income*.**

**The one number that would close the circuit is specified twice, 5× apart.** The gold a settlement's
Prosperity contributes to faction Treasury is **Prosperity × 10** (`derived_stats_v30.md:308`) and
**Prosperity × 50** (`settlement_layer_v30.md:47`). Neither is implemented; both are canon-marked.
*Held for Jordan (J-B).* Note the second is itself flagged "PENDING — Not canonicalized" upstream
(`settlement_layer_v30.md:43`), so this is not a simple typo either.

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
| "no code path sets `owner = None`" | **Overturned outright, in two steps.** First softening: `restore_world` (`game_state.py:357`) can re-materialize it from a serialized world. Then adversarial review found the stronger case: **`create_world` materializes `owner=None` at world-gen** in every campaign (`STARTING_OWNER['T15'] = None`, `game_state.py:48,223-224`). This is a live-campaign path, not an edge case. The claim was wrong, not merely absolute. |
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
| **D13** | The material layer is a **one-way ratchet**: no Treasury accrual and no Wealth income of any kind, while three of four cost sites levy full-sized drains on a non-renewing stock that gates Great Work and muster pool. No `econ.*` family exists to carry any of it (Part I.2.B). *(Corrected by adversarial review — the draft said costs were clamped to no-ops; that was true of one site out of four.)* | **Half-built, one-directional** |
| **D5** | Zero person-scale state changes in a seeded campaign. Conviction scars, beliefs, coherence, knots are real, correctly-wired mutable state that **nothing ever reaches**. The `world event → Key → person` path terminates at the Key: no code anywhere applies a Key's `impact_vector` or `stat_deltas` to any person store. | **Built, unreached** |
| **D1** | Insurgency pipeline: emergent, implemented, invoked every season, structurally unreachable. *(Precision correction from adversarial review: T15 **does** start uncontrolled — `create_world` materializes `owner=None` from `STARTING_OWNER['T15']` in every campaign, so the draft's "uncontrolled territory that nothing creates" was wrong. What nothing creates is a **second contiguous** uncontrolled territory, which is what formation requires.)* Promotion is *doubly* dead. `insurgencies_formed` telemetry is always 0. | **Built, unreachable** |
| **D7** | The Key substrate is a telemetry spine, not the churn engine. 3 of 55 types emit live; exactly one closes a loop; zero Key→Key cascades are possible (`DEFAULT_CASCADE_DEPTH_MAX = 0`, and `drain_tick` — the only path that would carry one — has zero production callers); 11 of 13 registered consumers subscribe to types with no producer, and at default flags 13 of 13 receive nothing. | **Declared, not running** |
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

Condensed from `topology_probe.py`'s output at `690f4c3` — thresholds declared in the output, not
inferred. *(The draft said "verbatim"; the probe prints multi-line labelled sections and this block
reformats them. Figures are unchanged; the word was wrong.)*

```
modules declared: 27 · pure sources 16 · pure sinks 4 · bidirectional 7
consume-declarations 125 · produce-declarations 69
top 4 consumers hold 108/125 (86%): articulation_layer=43, npc_behavior=31,
                                    faction_state=25, piety_track=9
key types 55 — orphan(0 consumers) 8 · seam(1) 4 · channel(2-3) 36 · nexus(>=4) 7
key types with no declared producer: 1/55
(the literal "*" wildcard subscription is excluded — see Part I.1)
```

**What this shape means.** Sixteen modules emit and hear nothing. Four hear and never speak. Of the
seven bidirectional modules, only `personal_combat` and `settlement_layer` are close to balanced;
`articulation_layer` is 44-in / 1-out. Read structurally, this is not a telephone exchange of
point-to-point wires, and it is not a router: it *can* be read as **a public square with a few
standing audiences** — people, factions, faith, narration. What is missing is (a) anything worth
hearing at world scale, and (b) rule content in the ears — every one of the 125 declarations is a
subscription with no behaviour behind it.

> **Adversarial review upheld a rationalisation charge here, and it stands.** The draft asserted the
> concentration "is not a defect to be flattened" and that "the substrate has already voted." But a
> declaration with zero runtime cost and zero rule content measures **authoring enthusiasm, not
> architecture** — and this document supplies its own defeater two sentences later ("no behaviour
> behind it") and again in Part VII.6 ("intent, not behaviour"). The rival hypothesis — that the
> concentration is an artifact of *who wrote module contracts, in what bulk waves* — was never
> raised, and **no instrument here can distinguish the two.** Commit-dating the declarations, or
> correlating them against authored rule content, would; neither was done. Note also that
> `articulation_layer` alone is 43 of 125 (34%), and a narration layer subscribing to nearly
> everything is close to tautological — it inflates the "audiences" story without evidencing the
> other three. **The public-square reading is a hypothesis this audit did not test.** It is retained
> as a reading, not as a finding, and Part III's ruling is re-grounded below so that it does not
> depend on it.

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

> **Weakened by adversarial review, correctly.** A wrapper that emits nothing is an *incomplete*
> wrapper — evidence of neglect, not a refutation of the category — and "a central author has no
> local state to generalise over" is false as a mechanism, since in-process central code can read
> everything (`run_accounting` does). What actually defeats the wrapper here is **doctrine, not the
> tree**: the ruled one-subsystem-one-module-tree shape (CLAUDE.md §3 §2a). The tree-based
> refutation of the *mesh*, below, is the genuine one — and it is the half doing less of the
> rhetorical work in the original draft.

**The mesh already exists too — on paper.** 125 consuming declarations with no runtime behind any of
them. Declaration is cheap; **rule content is the entire cost**, and it scales by authored meaning,
not by subscription. Worse, the mesh is structurally deaf exactly where world churn lives: the
"derive, never write" rule forbids any module from writing Mandate, province Accord or band state —
so **no module is licensed to announce that they moved**. Adding inputs to modules cannot produce a
signal nothing is permitted to send.

**So the dichotomy is false, and the substrate has already voted for the resolution.** The criterion
that assigns each responsibility to exactly one side:

> **Aggregate-crossing detection belongs to the aggregator; effect magnitude belongs to the
> effect's owner.**

> **This is the NARROWED form, and the narrowing was forced.** The draft stated it as a biconditional
> — *"Detection is central where derivation is central; interpretation is always local… a
> responsibility belongs to the boundary **iff** its truth is produced by aggregation… to a module
> **iff** its effect depends on the receiving entity's own state."* Adversarial review tested that
> `iff` against five concrete responsibilities and broke it on three: **P2-1's income** satisfies
> *both* clauses at once (an aggregation whose terms depend on each settlement's own `L` through
> `compliance(L)`); **Accord-0 revolt detection** reads on Accord, which is *directly written* rather
> than derived, so the letter of the criterion assigns detection locally to each of three writers —
> triplicated detection, the exact outcome it exists to prevent; and **the P4-3 witness adapter** is
> centralised *interpretation*, which the criterion forbids and the programme builds anyway. Two of
> five assign cleanly. A rule that straddles on three of five is a slogan, not a criterion. The
> narrowed form above is what survives the test; the biconditional is withdrawn.

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

> **WITHDRAWN by adversarial review — this paragraph was mechanically false, and its withdrawal is
> the single largest correction the review produced.** It read: *"`DEFAULT_CASCADE_DEPTH_MAX = 0`
> plus boundary-deferred apply means a consumer that reacts by emitting does so next season at the
> earliest… a clocked relay, one causal hop per season… the termination guard hands the design
> news-travels-at-horse-speed latency for free."* Verified against the tree, every clause fails:
> `schedule_emission` takes `depth = self._current_depth + 1` **only when `_in_drain`**, and
> `drain_tick` has **zero production callers** — only `tests/valoria/test_key_substrate.py:336,361,376,388`;
> the live loop calls `accounting_boundary()` then `next_tick()` directly (`mc_v18.py:158-161`).
> There is **no cross-season carry**: `next_tick` *raises* `TerminationBreach` if the queue is
> non-empty (`keys.py:598-599`). And the cap is self-labelled `[caps PROVISIONAL — OF-CAP]`
> (`keys.py:559`), sized in comment to the current sole emitter (`echo_transport.py:87-90`).
>
> **Corrected reading:** the guard *prevents cascades outright*; it does not schedule them late.
> One-hop-per-season semantics is not a property the design has — it is a mechanism someone would
> have to **build** (per-consumer carried state, or a scheduler rolling depth-1 emissions into the
> next tick's depth 0). That is a design act requiring a ruling, filed as **J-N**. This was a
> provisional safety bound being read as intentional latency architecture — I turned a constraint
> into a virtue, which is precisely the rationalisation Part I.1 warns about, committed thirty lines
> after warning about it.

**The one-sentence answer to the fork: the world churns when its consequential changes become
witnessable public facts.** The boundary makes derived change witnessable; `targets[]` makes power's
reach witnessable; modules are witnesses with stakes.

---

# PART IV · ORCHESTRATION — the programme, dependency-ordered

**Two orders, not one — a distinction adversarial review forced.** Everything lands flag-gated OFF,
and `01_plan.md:31-32` makes flipping a flag "a separate, measured act." So there is a **landing
order** (what must be built first) and a **flip order** (what must be switched on first), and the
draft conflated them — arguing several landing constraints on grounds that only govern flips. Each
row below now says which order it constrains.

Landing-order rule: an item appears before another iff building it later would **corrupt a measurement,
silently no-op, or force a dialect**. Everything lands flag-gated OFF unless stated. Every item
names its falsifier, per §0.1 point 3.

## P0 · Repairs and instruments — before any measurement is trusted

| # | Item | Why first | Falsifier |
|---|---|---|---|
| P0-1 | **Conviction gate loud-fail.** `apply_conviction_scar` returns magnitude 0 on an unknown name while the caller reports success — **and** the call site swallows `ImportError/AttributeError` (`knots.py:353-354`). Both layers must go. | Every scar edge in P4 no-ops through this hole *while reporting success*. | A test passing an unknown conviction and asserting it raises — and that the raise is not swallowed at the `knots.py` call site. |
| P0-2 | **Connectivity instrument**, by *extending* `tools/build_execution_map.py` — not a second `key_graph.json` parser. | §8: never re-implement a rule. Baselines everything downstream. | Must reproduce **11 of 13** producerless subscriptions and the Part II.4 figures. |
| P0-3 | **De-vacuate the two victory legs** — and **pin Turmoil's unit, not just its writer** — and retire the direction-#4 test to an honest xfail. **Gated on J-A** (corrected: this, not P0-6, is the Jordan-gated item). | The programme otherwise mis-scores its own campaigns. And per Part VII.6 the first strain-shock pass will write Turmoil in registry units (0–10) against `PS_MAX = 6.0` — the Accord defect recurring in a field we can already see. | A test that fails when Turmoil has no writer *and* a test that fails if a Turmoil write arrives in the wrong unit. |
| ~~P0-4~~ | **MOVED OUT OF P0 by adversarial review → now P1-3.** `rs_track` → delegate to `apply_ms_delta`. It is a **behaviour-changing wiring item**, not a repair: it "makes the only live person→world edge land," which alters the very system P0-2 is about to baseline. A baseline taken after it measures a different world. It also rests on the RS==MS identity that Part VII.4 grades as three rename records rather than a specification. | Sequenced after the baseline. |
| P0-5 | **`temperaments.py` reader signature.** | Wired-tomorrow trap; free now, silent later. | A test writing world-scoped drift and reading it back. |
| P0-6 | **The Accord unit guard** (Part I.2.A). **Needs no ruling — write it now.** | Without it every future threshold inherits the hole. Also covers `settlement.py:120`'s `math.floor` fourth dialect. | A test failing on any `.accord` comparison against a numeric literal outside `canon_buckets` — **with an explicit allowlist**, added after adversarial review found several *deliberate, commented* literal comparisons (`faction_action.py:156`, `crown_initiative.py:56/:101/:109`). A guard with no allowlist would fire on intentional sites, get muted, and become the thing it was meant to prevent. **This is the item that proves the pattern was understood.** |
| P0-7 | **File what this programme is not fixing** — §0.1 point 5. | Scope discipline. | The filed list exists. |

## P1 · The boundary speaks — pure publication, no semantics

| # | Item | Unblocks |
|---|---|---|
| P1-1 | Emit `mechanical.season_change` + `mechanical.accounting`, log-only, on the proven `_emit_battle_concluded` pattern. | The event deck's autumn predicate, which currently predicates on a fact with no carrier. |
| P1-2 | **Rule, then implement, derivation-crossing emission** (`mechanical.threshold_crossed`) — edge-triggered, with hysteresis, boundary-owned, carrying `contributing_key_ids`. | **NOT "the keystone" — downgraded by adversarial review.** The draft called it that, but walking Part IV, *not one* downstream item lists it as a blocker: P2 blocks on J-B/J-K/J-L, P3 on OI-37 and the insurgency ruling, P4 on J-C/J-D, P5 on nothing. Even P3-3 detects an Accord crossing without routing through it. It is **coherence-critical on a parallel track**: it is the only available reconciliation of "derive, never write" with causal legibility, and without it every later spine mints its own crossing key (shape divergence). That is a strong reason to do it early — it is not a serial dependency, and calling it one converted a preference into a false constraint. Without hysteresis: emission storm on any oscillating gate. |
| P1-3 | **`rs_track` → delegate to `apply_ms_delta`** (was P0-4). | Makes the only live person→world edge land. Lands *after* the P0-2 baseline so it does not move the system being measured. Blocks on the threadwork Part 5 RS caveat. |

## P2 · The economy exists

| # | Item | Blocks on |
|---|---|---|
| P2-1 | **The fiscal edge** — `realized_income = Prosperity × stance × compliance(L)` plus the L/PS consume step, **emitting `econ.income_realized`**. Adjudicated #1 on frequency, dependency and external warrant. | **J-B** (×10 vs ×50) and **J-K**.<br><br>**The emission is a correction, not an embellishment.** Adversarial review caught the programme's highest-priority item violating its own architecture ruling: the draft's P2-1 was a cross-subsystem read/write (settlement Prosperity/`L` → faction Wealth) with **no Key anywhere**, while Part III's criterion says *"the Key is the only thing that crosses"* — and Part I.2.B notes no `econ.*` family exists. Either the criterion is wrong or the item was. The item was: an income realisation is exactly an **aggregate crossing**, so under the narrowed criterion the boundary must publish it. This is also what makes a fiscal shock witnessable rather than a private fact of `run_accounting` — the whole point of Part III. |
| P2-2 | Charge the attacker: casualty writeback and conquest cost. | **Corrected — this constrains the FLIP order, not the landing order.** The draft called it a "hard prerequisite, not a preference." Adversarial review showed the argument does not meet the document's own landing-order test: writeback code landing OFF before income code corrupts no measurement, no-ops nothing, forces no dialect. **Land in either order; flip income before writeback,** because attrition without an economy produces *first-mover extermination* — and note even that claim is unsimulated (Part VII.1) and has a countervailing force the draft never weighed: with costs real, conquest also taxes the attacker toward stalemate. Blocks on **J-L**: a proportional coefficient without it is a fabricated constant. |

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
| P4-1 | **Populate**: seed Local Actors per the settlement quota. **J-M RULED in session — unblocked.** | **Corrected — the draft committed the error it cites elsewhere.** It said the `mc_v18.py:175-194` deferral premise is *"false one subsystem over"* because `settlement_layer_v30.md:858` gives a count (~45–50 across 36 settlements). But the deferral is about `generate_npc` / `world.npcs`, whose canon (investigation_systems_v30 SYSTEM 1 Two-Tier Generation) is explicitly **scene-specification-driven**; `§4.5` names **Local Actors**, a settlements-lane T7 entity — *"lightweight non-faction NPCs,"* 1–2 per settlement, one Conviction, a Disposition track. **These are different tiers, and the draft assumed they were one** — the term-vs-concept conflation `03_causal_model.md:157-170` names as the corpus's defining error, committed while citing it. What is true: Local Actors have a ratified world-gen count and are a genuine population. What was **not** established by the draft: that they share a store with NPE NPCs.<br><br>**RULED by Jordan in session, 2026-08-09: "local actors should be NPCs."** The identity holds — Local Actors *are* NPCs, not a separate lightweight tier. So P4-1 seeds them **through the NPC path into `world.npcs`**, with `§4.5` supplying the world-gen count and the per-type table (Seat 2, City 2, Town 1, Fortress 1, Port 2, Cathedral 1, Mine 1, Outpost 0) and the Role/Conviction/Disposition profile. **Note precisely what changed:** the draft's *conclusion* is now correct, but its *reasoning* was not — it assumed the identity rather than establishing it, the critic was right that it was unestablished, and Jordan has now supplied the missing premise. A conclusion rescued by a ruling is not a vindicated inference. **Unblocked.** Cross-lane (SE/WR) — the ruling is cross-lane and should be echoed into both lanes' handoffs. |
| P4-2 | The **Key→person applier** at ACCOUNTING_BOUNDARY. **Not gated on P4-1** — corrected by adversarial review. | Blocks on **J-C** (conviction vocabulary) and **J-D** (ORD-3) — population is *not* among its blockers. The applier can land flag-OFF and be exercised against fixture worlds; the strict xfail pins only the *live* store empty, and a vacuously-zero live measurement is a **true** measurement of the live state, not a corrupted one — so the landing-order rule's own test fails here. J-C gains urgency from Jordan's Local-Actor ruling: `§4.5` gives each Local Actor **one Conviction**, and there are three incompatible conviction vocabularies to draw it from (Part I.2.C). |
| P4-3 | World-fact scar rows; **recommended** to land together with vindication (`state.scar_removed`). | **Softened — the draft created a dependency and then cited it.** Vindication is a mechanic *proposed inside this audit* (`03_causal_model.md:193-197`, "the proposed mirror") on an unsimulated convergence argument, then treated as a hard landing constraint. The reasoning is good — a world that only wounds converges every long-lived NPC to permanent crisis — but it is a **design proposal to be ruled, not an established constraint**. Route all spines through **one witness adapter**, never five person-edge dialects. |

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
| **J-A** | Accord unit fix direction (Part I.2.A). Matching canon tightens a live gate ~1.5 buckets and changes every seeded outcome. | **P0-3 (the fix), NOT P0-6.** Corrected by adversarial review, which caught the gating crossed: P0-6 is the *guard* and needs no ruling to write, while the *fix* lives in P0-3 where no blocker had been recorded. As drafted, Part V blocked the free item and left the Jordan-gated one formally unblocked. |
| **J-B** | Prosperity→Treasury: **×10 or ×50** | P2 entirely |
| **J-C** | Conviction vocabulary — recommend: store on the canonical 13, derive the 4 axes, never the reverse | P4 entirely |
| **J-D** | ORD-3 / ORD-4 ordering | any generic `stat_deltas` applier — the highest-leverage single unblock in the line |
| **J-E** | The derivation-crossing emission rule itself | P1-2 (coherence-critical, *not* a serial keystone — see the P1-2 row) |
| **J-F** | D.6 double-count owner — a canon-internal contradiction (direct Mandate write vs pure aggregate) | P2-2, P3-1 |
| **J-G** | Population/Weight: a stock is smuggled into a derived value, and naive conservation carries a **Mandate sign-flip that rewards misgovernance-driven emigration** | all migration edges |
| **J-H** | `scene.battle_concluded` consumer-roster reconciliation (registry vs `key_graph` disagree) | **P2-2 only.** Corrected: P1-1 emits *new* types on the `_emit_battle_concluded` pattern, and reusing a pattern does not require the roster dispute settled. J-H gates *wiring consumers*, not publication. |
| **J-I** | Slate-ordering owner — nothing on disk says which spec owns it | P4-3, P5 |
| **J-J** | **L0 identity**: a ratified design whose corpus was evacuated vs an unratified proposal now occupying the same slot. Leaving both true is scripting-drift-by-neglect. | arc generation |
| **J-K** | ED-SE-0045 (M multiplier) | P2-1 |
| **J-L** | FACTION-P2-02 confirm (battle→Mil coefficient) | P2-2 |
| **J-N** | **Cascade carry — NEW, from adversarial review.** There is no mechanism by which a consumer's reaction reaches a later season: `drain_tick` has zero production callers and `next_tick` raises on a non-empty queue. If reactive chains are wanted at all, someone must design the carry (per-consumer state, or rolling depth-1 emissions into the next tick's depth 0). If they are *not* wanted, say so and the cap stops being labelled PROVISIONAL. | every reactive edge; Part VI's rumour prohibition |
| **J-O** | **Does the Key mesh deserve promotion at all? — NEW, the assumption the whole programme rests on.** See Part VII.0. The alternative never weighed: keep Keys as an append-only telemetry/causality log, drive churn through the boundary directly, and *retire* the consumer mesh. | **P1 through P5 wholesale** |

**Ruled in session (2026-08-09), recorded here rather than held:**

| Id | Ruling | Effect |
|---|---|---|
| **J-M** | **Jordan: "local actors should be NPCs."** The `§4.5` Local Actor and the NPE NPC are the same entity class, not two tiers. | **Unblocks P4-1.** Seed through the NPC path into `world.npcs`; `§4.5` supplies the count, per-type table and profile. Raises the urgency of **J-C**, since each Local Actor carries one Conviction and three vocabularies compete to supply it. |

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
- **A rumour subsystem** — but **on corrected grounds.** The draft justified this with *"the clocked
  relay already supplies coarse latency."* That justification is **withdrawn**: there is no relay
  (Part III), and the substrate supplies **no latency at all** — reactions cannot reach a later
  season because nothing carries them there (**J-N**). What survives is the narrower, still-good
  reason: make existing peninsula-wide effects legible as `causes[]` chains before inventing a
  transport for them. If J-N rules that reactive chains *are* wanted, revisit this prohibition —
  it was resting on a property the tree does not have.
- **A world-visible imminence Key** — `threshold_crossed` carries crossing *facts*, never forecasts.
- **The arc compile as specified** — its validation corpus was evacuated. Force J-J instead.
- **Per-throughline key dialects**, and **false-friend reuse** (`scene.displacement` for migration,
  `scene.combat_felled` for executions) — the term-vs-concept error, pre-empted twice by the corpus.
- **An invented NPC population count** — the count rule exists; use it (P4-1).

---

# PART VII · Weakest claims, and what would falsify this document

Carried forward honestly, because this is what the document is worth at its edges.

**VII.0 · The load-bearing assumption this section originally omitted.**
Adversarial review's sharpest finding was not about any claim in the document — it was about the
shape of this list. Every weakness the draft named (grep blind spots, a missing critic, unsimulated
stability arguments) was **safe**: conceding any of them changes not one Part IV item. The
assumption that actually carries the programme was never listed.

**It is this: that the Key substrate deserves promotion from telemetry spine to churn engine at
all — that "wiring, not redesign" means wiring *the mesh*.** P1's herald, P1-2's crossing rule,
P3-4's emission, P4-2's applier and P5's families all presuppose the declared Key architecture is
the right vehicle and merely unfed. **This document's own evidence supports the opposite reading
with equal force:** the one loop that genuinely churns — the political spine — runs on direct writes
and deferred applies, **not through a single Key consumer**; real inter-subsystem traffic runs over
16 direct Python imports, and the tree itself says *"a substrate with one call site is a prototype,
not an architecture"*; all 13 consumers are stubs; and `drain_tick` has never been called in
production.

The alternative — **keep Keys as an append-only telemetry and causality log, drive churn through the
boundary directly, and retire the consumer mesh** — is never weighed anywhere in this document,
including in Part VI where competing architectures are ruled out. If it is the right answer, P1
through P5 are wrong wholesale. Filed as **J-O**, and it is the first thing to settle, because it is
the only open question that can invalidate the entire programme rather than one item of it.

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
6. **The Turmoil vacuity is the claim most likely to be true today and wrong next month** — named
   by adversarial review as this document's weakest verified-as-true claim, and the judgement is
   right. "Nothing writes Turmoil" is a pure *absence* claim, held by exhaustive grep with no guard
   test, over a field that already exists in the clock dict, is registered with range 0–10
   (`clock_registry_v30.md:19`), and sits beside `peninsular_strain` machinery explicitly marked
   "unbuilt, dormant groundwork" (`game_state.py:238-243`). The first strain-shock wiring pass will
   write it — **in registry units (0–10), against `PS_MAX = 6.0`** — at which point the leg becomes
   load-bearing with neither its vacuity nor its unit ever pinned by a test. That is the Accord
   defect about to happen a second time, in a field we can see coming. P0-3 should pin the unit, not
   just the writer.
7. **The topology figures are a measurement of the *declared* graph.** A declaration is not evidence
   of runtime traffic — that is D7's entire point. Part II.4 describes intent, not behaviour.

---

# PART VIII · What the adversarial pass changed — the record

Recorded because a synthesis that hides what its critics did to it is not evidence. Two structurally
independent read-only critics (no write tooling) received this document's **output only**, never the
reasoning behind it. Their findings, and the disposition of each:

| # | Finding | Disposition |
|---|---|---|
| 1 | **The "clocked relay" was mechanically false.** `drain_tick` has zero production callers; `next_tick` raises on a non-empty queue, so no cross-season carry exists; the cap is self-labelled PROVISIONAL. | **UPHELD, verified by hand, paragraph WITHDRAWN.** Largest single correction. New ruling **J-N**. Part VI's rumour prohibition re-grounded. |
| 2 | **Part VII named only safe weaknesses**; the assumption carrying the whole programme — that the Key mesh deserves promotion at all — was unlisted. | **UPHELD.** New **VII.0** and ruling **J-O**, which can invalidate P1–P5 wholesale. |
| 3 | **P4-1 conflated two entity tiers** — Local Actors (`§4.5`) vs NPE `world.npcs` — committing the term-vs-concept error while citing it. | **UPHELD as a reasoning defect.** Then **RULED by Jordan in session**: local actors *are* NPCs. Conclusion rescued, inference still faulty; both recorded. |
| 4 | **The audience-structure reading is a rationalisation** the audit cannot distinguish from an artifact of who wrote contracts. | **UPHELD.** Demoted from finding to untested hypothesis; Part III re-grounded so it does not depend on it. |
| 5 | **The Part III criterion is not decidable** — it straddles on 3 of 5 test cases. | **UPHELD.** Biconditional withdrawn; narrowed to *aggregate-crossing detection belongs to the aggregator; effect magnitude belongs to the effect's owner.* |
| 6 | **P2-1 violates Part III's own criterion** — the #1 item crosses subsystems with no Key. | **UPHELD.** P2-1 now emits `econ.income_realized`. |
| 7 | **Landing order vs flip order conflated** — P2-2's "hard prerequisite" governs flips, not builds. | **UPHELD.** Both orders now stated separately per row. |
| 8 | **P1-2 is not a keystone** — no downstream item lists it as a blocker. | **UPHELD.** Downgraded to coherence-critical on a parallel track. |
| 9 | **P4-2 is not gated on P4-1** — the applier can land against fixtures. | **UPHELD.** Ungated. |
| 10 | **P0-4 is a behaviour change, not a repair** — it moves the system P0-2 is about to baseline. | **UPHELD.** Moved to P1-3, after the baseline. |
| 11 | **J-A gated the free item and left the gated one unblocked**; **J-H did not block P1.** | **UPHELD.** Both re-gated. |
| 12 | **P4-3 created a dependency then cited it** — vindication is a proposal from this audit treated as a constraint. | **UPHELD.** Softened to a recommendation requiring a ruling. |
| 13 | **The wrapper refutation generalised from an incomplete instance.** | **UPHELD.** Now rests on doctrine (the ruled Godot module shape), not on the tree. |
| 14 | **The ED-1094 hold covered only Part V**, letting the architecture ruling and six prohibitions ratify silently. | **UPHELD.** Header now holds Parts III, V and VI. |
| 15 | **The Part I.1 assurance was technically true, substantively thin** — the metaphor outlived the evidence cut from 9/11 to 4/7. | **UPHELD as stated.** Recorded here rather than re-argued. |

**Critic 2 — factual accuracy.** It verified every `file:line` citation, every constant, and re-ran
both headline traces independently:

| # | Finding | Disposition |
|---|---|---|
| 16 | **"The costs are no-ops anyway" is FALSE.** `crown_initiative.py:32` pre-multiplies by `_MULTS_W = 100`, so three of four Wealth sites levy full −2.0/−3.0 drains, live every season; only Muster is the no-op described. Wealth also gates Great Work and sizes the muster pool. | **UPHELD, verified.** Headline rewritten: not "no constraint" but a **one-way ratchet** — real costs, zero income, non-renewing stock. **Sharper than the original claim.** |
| 17 | **"Wins immediately" is overstated.** `SUSTAIN_SEASONS = 2`; and conquest is a *delta* (−2.5 storm), not a set-to-Accord-1, so most stormed territories fall below even the buggy gate. | **UPHELD, verified.** Vignette withdrawn. What survives: the gate sits at half its canonical height — the governance burden is **halved, not bypassed**. |
| 18 | **The `.accord` consumer enumeration was incomplete** — at least five more live sites, including `settlement.py:120`'s `math.floor`, a **fourth** bucketing dialect that disagrees with `canonical_accord`. Several literal comparisons are deliberate, so P0-6 needs an allowlist story. | **UPHELD.** Strengthens the pattern finding; P0-6 amended. |
| 19 | **Canon defines Accord 0–3**, not 0–4 (`victory_v30.md:80`) — the code carries a fifth bucket canon does not define. And `:63`, one of four cited canon statements, is **superseded text**. | **UPHELD.** New divergence recorded; citation dropped to three live statements. |
| 20 | **"Correct when written, broke later" is UNSUPPORTED** — `victory.py` and `ACCORD_MAP` are both dated 2026-05-17: born-mismatched. | **UPHELD.** Reclassified. Pattern conclusion unaffected. |
| 21 | **D1's premise was wrong**: T15 *does* start uncontrolled (`create_world` materializes `owner=None`). What is missing is a **second contiguous** uncontrolled territory. | **UPHELD.** Both D1 and the earlier "softened" row corrected — the original claim was wrong, not merely absolute. |
| 22 | **The Part I.1 retraction was itself wrong** — excluding the `"*"` wildcard reproduces 16 / 108 / 125 exactly. | **CONVERGENT.** I found this independently while writing the critic's brief and had already withdrawn the retraction. **Two independent routes to the same correction** is the strongest confirmation in this document. |
| 23 | **"Verbatim" was false as to form**; the reachable-set trace listed two unreachable stats; three citation off-by-ones (`domain_echo` table span, `settlement_layer:43/:858`); `insurgency_pipeline` is in the **WR** lane, not FA. | **UPHELD.** All corrected. |
| 24 | **The Turmoil vacuity is the weakest verified-as-true claim** — an unpinned absence over a field that will be written in *registry units (0–10)* against `PS_MAX = 6.0`. | **UPHELD.** Added as Part VII.6: the Accord defect about to recur in a field we can see coming. |

**What the critics could not break** (they tried): Part I.2.A's victory-gate chain — the escape routes
were checked and none exists; Part I.2.B's Wealth trace, judged *"the strongest inference in the
corpus and the correct template for the other grep-based absences"*; the **mesh** half of Part III's
refutation, which is a real incompatibility of a pure mesh with the ratified derivation rule rather
than a badly-executed-instance complaint; and P3-1+OI-37 and P3-3's bucketing point, both
independently corroborated.

**The critics' own weakest claims, carried forward rather than suppressed:** the `drain_tick`
zero-caller finding rests on grep plus a boundary read, with no guard pinning it — dynamic dispatch
would evade it (I re-verified the callers by hand, but the guard is still unwritten); and the
tier-conflation attack rested on two document surfaces, which is why Jordan's ruling — not the
critic's reading — is what settles it.

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
