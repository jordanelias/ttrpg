# The Slate — Inertia, Contracts and Property Audit (part 2)

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Version: v3 — §6 received from part 1 · §7 Memory fallback CUT + §7.1 inertia bootstrap fix ·
## §11.2 stale `pressure` loop restated · §11.4 dominance hand-off · claims 12–16 · §11.5
## Reads: [`10_the_slate_and_salience.md`](10_the_slate_and_salience.md) — **part 1 first; this continues it**
## Part 1: §§0–5 (the override list, the funnel numbers, the candidate contract, the cast gate,
## the two orderings, truncation with its proofs)
## Part 2: §§6–11 (headless resolution and the skill premium, light-inertia without storage and
## **J-N**, **J-O**, the player surface, the module contracts, the property audit)
## ⚠ **§6 moved here from part 1 in v3 and kept its number** — every `10 §6.x` citation still resolves.

---

## 6. Headless auto-resolution — the same module, run headless

### 6.1 Fork A, restated because it is already ruled

`auto_manual_resolution_duality_v1.md:75` (RULED, Jordan, 2026-07-08, ED-SC-0013):

> **auto = the contest kernel run headless, played = the same kernel run interactively.** Not two
> mechanics — one engine at two fidelities. … same engine ⇒ consistent by construction.

The delta spec's *"auto-resolution is the same module run headless, never a second cheaper path"* is
this ruling. **This document adds nothing to it and takes nothing from it.** What it adds is the three
properties that make *"consistent by construction"* true of the *Slate*, which fork A asserts of the
*kernel* and which does not follow automatically once a filter sits above it.

### 6.2 The Slate has no resolver, and that is the anti-distributor argument

Part VI's strongest negative (`audit/2026-08-08-world-churn-audit/06_master_synthesis.md:551`, **held,
not ratified**): *"a distributor wrapper or 'world director'. Distribution is `targets[]` data plus
subscription; a router module is the god-loop with better PR."*

**An attention system is the single most likely thing in this suite to become that.** So:

1. **The Slate holds no resolver and no effect rule.** Its four modules (§10) are three `derivation`s
   and one `gate`. `state: []` in all four. It cannot deposit into a gauge, append a tag, grant a post,
   or transition a form.
2. **It does not dispatch.** It labels. Each candidate names its own `resolver_ref`, written by the
   **emitter**, and that module is invoked by that subsystem's **own herald** at the boundary. There is
   no central invocation and no map from candidate to module held anywhere but on the candidate itself.
3. **It is subtract-only by construction, not by rule.** Its outputs are a subset, an ordering, and a
   label. It has no channel by which it could inject a candidate, alter a resolution, accelerate a
   clock, or emit a pressure-bearing Key — the ratified discipline at `:198`, made structural.

> **Falsifier.** If a future version of this document gives an `sl.*` module a `state:` row, a `form:`
> row, a `transitions:` row, or a resolver other than `gate`/`derivation`, that version has built the
> prohibited thing, and this paragraph is the test.

### 6.3 The three invariance properties

| # | Property | Statement |
|---|---|---|
| **P-A** | **Fidelity neutrality of the world** | For every pair of candidates `c ≠ c′`: the outcome of `c′` is **bit-identical** whether `c` was played, witnessed, shaded, or absent from the Slate |
| **P-B** | **Baseline parity** | `E[outcome(c) \| auto] = E[outcome(c) \| AI-played]`. The auto path *is* the AI playing it — not a summary, not a table, not a cheaper approximation |
| **P-C** | **Order neutrality** | The season's outcome is invariant under any permutation of the order in which candidates are resolved, and under the order in which the player attends their scenes |

**P-A is the load-bearing one.** If surfacing changed outcomes, the filter would be a cheat: the player
would be farming the attention system rather than playing the world, and every claim in §1 about the
other 95% would be false.

### 6.4 What makes them true

**Three mechanisms, and all three are necessary.**

**(1) One snapshot.** Every candidate resolves against the **settled state at the accounting boundary**
— the same snapshot the candidate set was derived from. No resolver reads a state another resolver
wrote this season. This is not an extra rule; it is what `01 part 2 §9.3` already forces, because the
substrate has no latency: a form gate reads current state, a gauge decays on elapsed time, and nothing
carries an emission forward. **The absence of latency, which is a limitation everywhere else in this
suite, is exactly what buys simultaneity here.**

**(2) Commutative effects, with the two non-commutative cases decided.** All effects are collected and
applied at the boundary:

| write leaf | commutes? | rule |
|---|---|---|
| gauge deposit | **yes** — addition | none needed |
| tag append | **yes**, given a rule | `01 §3.3` dedupes on `(owner, kind, key)`; on collision **the higher `value` wins, ties broken by `provenance` key id ascending**. Deterministic and order-free |
| post grant / revoke | **no** | **At most one post operation per post per boundary.** A second is a gate failure and emits `faction.action_declined`. Contention is a *situation*, not a race |
| form transition | **yes**, by sequencing | transitions fire **after** all deposits, reading the settled result. `01 §2.2` already gates them on state rather than on a received Key |

**(3) A per-candidate RNG substream.** This is the mechanism most likely to be omitted and it is the
one that actually carries P-A.

```
seed(c) = H( campaign_seed ‖ accounting_index ‖ candidate_id )        # 64-bit, fixed hash
```

**Not** a shared sequential stream. On a shared stream, surfacing candidate `c` changes how many draws
are consumed before `c′` is resolved, so **whether the player attended one thing silently re-rolls
everything after it.** That is a real, subtle, and completely invisible leak — a game could ship with
it and nobody would find it by playing. The construction mirrors the churn doc's ensemble seed
(`:180`) and composes with `00 §8` P0-2's dedicated generation substream: same discipline, one more
axis.

### 6.5 The skill premium — answering ED-SC-0026 head-on

**ED-SC-0026** (`registers/editorial_ledger_sc.jsonl`, open, `needs_jordan: true`) states the sharpest
objection to everything above:

> *under our OWN ratified doctrine, playing a contest is currently strictly wasted attention* … *if
> E[auto] ≈ E[played] AND every output is a scalar, the promised "richness" does not exist and
> auto-resolving is strictly correct play. The played fidelity can only justify itself if playing
> shapes **WHICH** consequences occur, not their expected size.*

**That last sentence is the design.** Stated precisely, and this is the reading O-10.3 takes:

| | |
|---|---|
| **P-B binds the magnitude** | `E[outcome(c) \| auto] = E[outcome(c) \| AI-played]`. Nobody gains expected value by choosing a fidelity. Mode-shopping is dead |
| **Playing selects the branch** | The player substitutes their decisions for the AI policy's **at the same decision points, from the same option set** (`remit`-as-gate, `00 §7`). Same distribution of *magnitudes*; different *which* — which tag is written, whose Grudge, which Precedent, which edge strains |
| **The premium is real and is paid for** | Play above the AI baseline is a legitimate gain — ED-SC-0024's Football Manager argument, where *"a watched match diverges from an unwatched one exactly by the manager's live interventions."* It is not mode-shopping because it **cannot be had without spending a scene action**, and the budget is 3–5 |

**So the scene budget is the price of the skill premium, and that is what makes triage a real decision
rather than an interface.** A player who attends nothing gets an honest AI campaign. A player who
attends well gets a better one, in the 3–5 places a season where they chose to be. `player_agency_v30`
already said this in prose (`:308`, *"the revolt you didn't attend to resolves based on garrison
strength alone"*); this section is the arithmetic under it.

**⚠ This is a reading of a ruled doctrine, not a ruling.** ED-SC-0024 is filed, open, and
`needs_jordan: true` precisely because it amends `auto_manual_resolution_duality_v1.md:65`. **If Jordan
rules for strict expert-parity instead, nothing in §§2–5 or §6.1–6.4 changes** — only the parity
harness's baseline moves, and §6.5's premium becomes zero. The design is robust to the ruling; the
*reason to play* is not, which is why ED-SC-0026 says CIP-9b must not be ruled separately from CIP-1.

---

---

## 7. Light-inertia without storing anything, and **J-N**

The ratified inertia term (`:220`) is a **carryover across seasons**: `inertia_bp = inertia_bp · NUM // DEN`,
integer, a pure function of the accounting index, with an anti-strobe floor. Carryover across seasons is
exactly what `01 part 2 §9.3` says the substrate cannot do.

**Resolution: inertia is *derived from the Key log*, not carried and not stored.**

```
last_lit(c)   = the accounting_index of the most recent slate.item_surfaced Key with this candidate_id
d             = t − last_lit(c)
inertia_bp(c) = INERTIA_NEUTRAL                                    if none      # v3 — was 0; see §7.1
              = INERTIA_NEUTRAL + INERTIA_BASE · NUM^d // DEN^d    otherwise
anti-strobe:    if 0 < d ≤ STROBE_MIN ⟨shape: 2⟩ :
                    inertia_bp(c) := max(inertia_bp(c), STROBE_FLOOR)  ⟨shape⟩
```

⚠ **The `if none` line read `0` in v2.0 and that was a bootstrap deadlock** — inertia multiplies into
`cast_score` (§4.1), so a never-lit candidate scored zero and could never be lit. **§7.1 is the
argument; this block is the corrected arithmetic, and there is only one of it.** Falsifier: claim 16.

`INERTIA_NEUTRAL`, `INERTIA_BASE`, `NUM`/`DEN`, `STROBE_MIN` and `STROBE_FLOOR` are **shape proposals**;
they belong to the ratified F-F weight surface (`:279`) as exposed versioned data.

**Three things this buys.**

1. **No fifth stored kind, no new write leaf, no aggregate written (AU-1).** A derivation over an
   append-only log the engine already keeps.
2. **J-N compliance, exactly.** `01 part 2 §9.3` forbids *"a module reacting to a Key by publishing a
   Key that lands next season"* and prescribes *"it reads state at the boundary."* Reading the log is
   reading state. **Nothing is posted to next season's Slate; next season's Slate re-derives
   everything, including how much attention this thing already had.** ⚠ **What J-N forbids here,
   concretely: there is no "carry this candidate forward" flag, no deferred-item queue, and no
   next-season promise.** A situation reappears next season because it is *still true*, or it does not
   reappear at all. **J-N is the ruling that would change this.**
3. **J-O robustness.** This reads the Key log as **telemetry**, which `01 part 2 §9.4` records as
   surviving a "telemetry only" ruling. Inertia does not depend on the consumer mesh.

**The fallback is CUT in v3, and the reason is worth more than the fallback was.** v2.0 named one:
*"if the log is not queryable by `candidate_id` at acceptable cost,"* store a `Tag` with `kind: Memory`
on the anchor, `key = candidate_id`, `value = INERTIA_BASE`, bounded by `MEMORY_CAP`. `01` O-6 has
since cut the `Memory` kind — its `key`+`value` cannot say *what* is misremembered, and `Holding`
replaces it — which forced this line open again. **Re-opened, it fails on three counts that have
nothing to do with the kind's name, so it is deleted rather than renamed.**

1. **The cost it insures against cannot arise, by this document's own boundedness proof.** The log is
   written by `sl.truncate` **once per Slate member**, and §5.2 proves `|Slate| ≤ B` with `B ≤ 9`
   (`player_agency_v30.md:305`). So it grows at **≤ 9 rows per season and ≤ 450 over the 50-season
   campaign** `engine/tests/test_mc_v18_regression.py:16` runs, and `inertia_bp` needs one `max` over
   the rows carrying a given `candidate_id`. **The number that could have made this expensive is the
   candidate rate — ≈195/season, ≈9,750/campaign (§1.3) — and the log does not record candidates, only
   LIT ones.** The fallback confused the two, and re-deriving §1.3 is what made the gap between them
   visible.
2. **It gave `sl.*` a tag write, which §6.2 forbids in its own falsifier** — *"it cannot deposit into a
   gauge, **append a tag**, grant a post, or transition a form"* — and §10 declares `state: []` in all
   four modules. **This was equally true under `Memory`;** the kind's removal exposed the breach rather
   than caused it. Cutting the fallback is what finally makes **claim 8 honest**, since claim 8 asserts
   precisely the property this paragraph was contradicting.
3. **The proposed landing, `Precedent(owner=anchor, key=candidate_id)`, is worse than what it replaces,
   and specifically so.** `08 §5` row 4 draws candidates from *"a `Precedent` tag being tested by a new
   event"* on the place. A Precedent-kind attention marker sitting on the anchor would therefore feed
   the Slate's own output back into `sm.business`'s input — **a channel by which the Slate injects its
   next season's candidates**, which is the exact property §6.2 point 3 claims to hold *by
   construction*. Separately, `01 §3.2` states the salience derivation applies to *"any tag kind that
   declares a salience reading; only `Holding` does today"* — so the decay this fallback depends on is
   not even available on `Precedent` without extending `01` as well.

**There is therefore no store and no bound to declare, which is the strongest available form of that
answer.** The log is the only mechanism; it is bounded at `B` per season by a proved theorem rather
than by a cap; §11.2's inertia loop is unchanged. **A bounded fallback was considered and rejected:**
adding a store that breaches this document's own structural prohibition, to insure against a cost the
document proves cannot occur, is the trade §0 exists to refuse.

### 7.1 What happens when there is no log at all — and the defect that question exposed

`slate.item_surfaced` is blocked on `00 §8` P0-1 (§10), so there is a real window in which `last_lit(c)`
is undefined for **every** candidate. Working out what the Slate does in that window surfaced a defect
that is **not** confined to it:

> **As written above, `inertia_bp(c) = 0` when a candidate has never been lit — and §4.1's `cast_score`
> MULTIPLIES by it. So a never-lit candidate scores zero, and a candidate scoring zero cannot be lit.**
> Every candidate begins never-lit, so on a cold start every `cast_score` is `0`, the comparator falls
> through to its `candidate_id ASC` tie-break, and **the Slate ranks the world by hash.** The reserved
> slice does not rescue it: Step 4 also orders by `cast_score`, so it picks by hash too — and Step 3's
> free pool `F`, which is most of the Slate, is in the same state. This is a bootstrap deadlock, and it
> is reachable on season 1 of every campaign.

**Fix, and it is the smaller of the two available.** `inertia` is a **momentum** term: the ratified
reading is that attention *has* momentum, not that inattention *annihilates* meaningfulness. Its
neutral value is therefore `1` — `INERTIA_NEUTRAL = 10000 bp` ⟨shape; 1.0 in basis points⟩ — and the
boost is **added to** that baseline rather than replacing it. **The corrected arithmetic is in §7's
block above; it is not restated here, so there is exactly one formula to implement.**

**What this preserves, and the one thing it changes.** The ratified property — *a recently-lit
candidate outranks an otherwise-identical un-lit one by a margin that decays geometrically to nothing*
— is preserved exactly; the decay law, the anti-strobe floor and the integer discipline are untouched.
What changes is only **the baseline the boost is measured from**, and the `0` baseline was never a
design choice anyone made. §5.3's monotonicity proof is unaffected: it quantifies over *raising* a
score and reads `|M|`, `|E|`, `X`, `R` and `I`, none of which is a function of inertia's baseline.

**And it makes the P0-1 window benign rather than catastrophic.** With no log, every candidate sits at
`INERTIA_NEUTRAL` and `cast_score` reduces to `meaningfulness × scale_weight` — a Slate with no
momentum, correctly ordered. That is the exact parallel of §5.1's `E := ∅`, and **both blocked-state
behaviours are now named configurations rather than holes.**

⚠ **Scope, stated plainly: this is beyond what v3 set out to change here.** It was found by asking what
the deleted fallback was insuring against. It is fixed in place rather than filed because it needs no
ruling — an absent multiplicative case written as `0` is an oversight, not a design call — which is
`CLAUDE.md §0`'s *fix it in this commit or drop it*. Its falsifier is **claim 16**.

---

## 8. ⚠ This document leans on Key consumption — **J-O**

Per `00 §5.1` and `01 part 2 §9.4`, stated so the affected parts stay identifiable if J-O rules that
the Key mesh stays a telemetry spine:

| what it depends on | survives a "telemetry only" ruling? |
|---|---|
| **inertia derived from `slate.item_surfaced`** (§7) | **yes** — append-only log read; that is telemetry |
| **`provenance` on every candidate** (C-1) and `causes[]` as the chain a player follows | **yes** — telemetry and causality are what the alternative keeps |
| **emitters returning candidates at the boundary** (§2.4) | **yes** — they are boundary derivations over state, not Key reactions. This was chosen deliberately; an emitter subscribing to Keys would have been the natural design and would have been J-O-fragile |
| **`slate.item_surfaced` as an emission** | **yes** as a log entry |
| **the fidelity label reaching a subsystem herald as a Key** (§5.5) | **no** — this becomes a boundary read of the derived candidate set. **The only J-O-fragile line in this document**, and it is one line |

**This document takes no position on J-O.**

---

## 9. What the player actually touches

**Per `00 §2.3` item 4, and the ratio is the point.**

**Surface — 1 verb, 2 reads:**

| what the player is asked | how often | budget |
|---|---|---|
| **attend a Slate item** — spend a scene action, then pick one of 3–5 responses the item supplies | 3–5 times per season | `A`, from §1.2 |
| *read:* the Slate — item, anchor, witness channel, the tag saying what generated it (`player_agency_v30.md:299`) | once per season | — |
| *read:* an item's published inputs — never its score, threshold, or rank arithmetic (`01 §8`) | on demand | — |

**Substrate — 4 modules, 6 derived terms, 2 orderings, 3 fidelities, 5 witness channels, 1 hash, 0
stored objects.**

The player never sees the word *salience*, never sees `cast_score`, never sees a candidate that was
shaded, never sets a filter, never configures a priority, and never learns that ~195 things happened and
6 arrived. **They see a season with six things in it, and each one is about something.**

---

## 10. Module contracts

Per `00 §7`. Four modules; **`state: []` in all four**; no `form:`, no `transitions:`; `remit: []`
because none is invoked by a post-holder — they run at the boundary for every player. Per W-6, every
`consumes:` row names what the consumer does.

```yaml
- module: sl.candidates
  parent: slate
  class: surface                  # the only surface subsystem in v2 (00 §4.3)
  scales: [personal, settlement, territory, peninsula]
  tier: null
  resolver: derivation            # gathers emitter returns; invents nothing
  remit: []
  budget: null
  consumes: []                    # emitters return at the boundary, not by subscription (§8)
  emits: []
  state: []
  form: []
  transitions: []
  disclosure: [{of: candidate_set, inputs: published, presentation: exact, trigger: hidden}]

- module: sl.cast
  parent: slate
  class: surface
  scales: [personal, settlement, territory, peninsula]
  tier: null
  resolver: gate                  # knowability + realized; no roll, no score (§3)
  remit: []
  budget: null
  consumes: []
  emits: []
  state: []
  form: []
  transitions: []
  disclosure: [{of: witness_channel, inputs: published, presentation: exact, trigger: hidden}]
  # the channel is an INPUT and is published — a player may reason about what they cannot know

- module: sl.rank
  parent: slate
  class: surface
  scales: [personal, settlement, territory, peninsula]
  tier: null
  resolver: derivation            # cast_score and depth_score; read-only, writes nothing
  remit: []
  budget: null
  consumes: []
  emits: []
  state: []
  form: []
  transitions: []
  disclosure: [{of: cast_score, inputs: published, presentation: band, trigger: hidden}]
  # components published; the composed score is a band; the budget arithmetic is the trigger

- module: sl.truncate
  parent: slate
  class: surface
  scales: [personal, settlement, territory, peninsula]
  tier: null
  resolver: derivation            # top-n under a total order; §5
  remit: []
  budget: null
  consumes: []
  emits: [{type: slate.item_surfaced, terminal: false}]
  state: []
  form: []
  transitions: []
  disclosure: [{of: slate, inputs: published, presentation: exact, trigger: hidden}]
```

**`slate.item_surfaced` is blocked on `00 §8` P0-1** (`references/rendering_dispositions.yaml` must
exist before any key type is appended). Named so the blocked work is specific.

---

## 11. Property audit

**Scope gate, honoured (`00 §0.1`, delta spec §10): none of the four modules rolls.** Three are
`derivation` and one is `gate`. **A NERS verdict is not manufactured for them.** They are diagnosed on
their loops and gates instead, below, and on P-iii (no oscillation) and P-v (no dominant option) which
do apply to a selection function.

### 11.1 Claims and falsifiers

| # | Claim | Falsifier |
|---|---|---|
| **1** | **This document designs no salience function** (§0) | Grep every score expression here against `narrative_engine_design_v2_churn.md:239-246`. A term appearing here that is not one of the ratified six — or the struck **novelty** term reappearing — falsifies it. **⚠ v3's derived horizon (§4.2) is NOT a seventh term:** `imminence` is one of the ratified six and was already in `depth_score`; what v3 adds is a *producer for its input*, which is why claim 15's second assertion (membership invariant under `horizon`) is the one that matters |
| **2** | **Truncation is bounded:** `\|Slate\| ≤ B` in every reachable state (§5.2) | A property test over random `(\|C\|, \|M\|, \|E\|)` triples asserting `\|Slate\| ≤ B`. **Separately measurable and NOT assumed:** the frequency of `\|M\| ≥ B` over a seeded 50-season campaign. If it exceeds a stated rate, the mandatory enumeration is too wide and §5.4 is wrong |
| **3** | **Truncation is monotone** (§5.3) | A property test: sample a candidate set and a comparator, raise one candidate's `cast_score`, assert it did not leave the Slate and that no candidate ranked below it entered. **Mutation check that the proof is load-bearing:** redefine the exempt set by a score *threshold* instead of a count *cap* and confirm the test then fails |
| **4** | **P-A — a candidate's outcome does not depend on whether any other was surfaced** (§6.3) | Run a seeded season twice with identical state, differing only in which Slate items were attended, with all attended items forced to the AI policy. Assert the resulting world state is **bit-identical**. **This is the single most important test in the document.** Mutation check: replace the per-candidate substream with a shared sequential stream and confirm it fails |
| **5** | **P-C — order neutrality** (§6.3) | Resolve one season's candidate set under `n` random permutations; assert one state. Mutation check: allow two post operations on one post per boundary and confirm it fails |
| **6** | **P-B — baseline parity** | The **parity harness** of `auto_manual_resolution_duality_v1.md:67`, comparing auto against **AI-played** on matched inputs. ⚠ **The tolerance is fork C, genuinely open**, and this document does not set it. Until the harness lands, P-B is **asserted and unverified** |
| **7** | **No unknowable candidate reaches the Slate** (§3) | A test asserting every Slate member has a non-empty `witness` on one of the five channels, and that no Thread-constituted candidate is cast to a person below the canonical Thread Sensitivity gate. This is P-08's own falsifier applied to the attention system |
| **8** | **The Slate writes nothing** (§6.2) | A contract test asserting all four `sl.*` modules have `state: []`, no `form:`, no `transitions:`, and a resolver in `{gate, derivation}`. **⚠ This claim was FALSE in v2.0 and nobody noticed**, because §7's inertia fallback appended a tag from `sl.*`. v3 cut the fallback (§7 point 2); the claim is now honest and this test would actually have caught it |
| **9** | **Candidate identity is stable across seasons** (§2.2) | A seeded campaign asserting a persisting situation keeps one `candidate_id` across ≥ 3 seasons. Mutation check: add `accounting_index` to the hash and confirm inertia stops carrying |
| **10** | **Zero new player verbs** (§1.4) | Count verbs across the suite before and after `10`. This document must add 0 and does add 0 — it adds one *interaction* (attend) which is the budget's own unit, not a verb over the world |
| **11** | **The funnel ratios of §1.3, re-derived in v3** | They are **estimates with stated bases, not measurements**, and §1.3a records that the v3 basis is *weaker* than the v2.0 one it replaces even though the number is larger. Falsified by instrumenting one seeded 50-season campaign and counting emitted candidates per season, **broken out per `08 §5` row**, because rows 1 and 3 carry ≈76% of the mass and neither is bounded by any document. **⚠ v3 amends this to test BOTH directions.** *Too low:* if the true rate is under **~3× the budget** (≈18/season), the Slate is not earning its keep and **D should be cut**. *Too high:* if `08`'s per-place rate exceeds **~8** (≈300/season peninsula-wide), the Shade — all of which still resolves at full fidelity (§6) — is a per-season simulation cost nothing in this document would surface, and the answer is a bound in `08 §5`, **never a second rationer here** |
| **12** *(v3)* | **`engaged(c)` has a data source** (§5.1) | A test asserting `slate.item_surfaced` carries `fidelity`, and that Step 2's exempt set is computed from it. **Mutation check:** remove the field and confirm Step 2 becomes uncomputable rather than silently empty. **Until P0-1 clears this is expected RED**, and §5.1 states the degraded configuration (`E := ∅`) that holds meanwhile |
| **13** *(v3)* | **An `informational` candidate is rendered and never resolved** (§2.1a) | A test asserting every `informational: true` candidate has `resolver_ref: null` and `responses: []`, that no resolver is invoked for one, that it never enters the exempt set `E`, and that `\|{informational} ∩ Slate\| ≤ I`. **Mutation check:** relax C-1 or C-2 for informational rows and confirm the §3 cast-gate test (claim 7) then fails — the exemption is C-4/C-5 only |
| **14** *(v3)* | **A candidate never crosses a seam as a Key** (§2.1) | A test asserting no module contract in the suite declares an `emits:` row whose type carries a candidate, and that `00 §9.2` registers none. **This is what makes the `08`↔`10` seam single-valued**; v2.0 had `08` emitting `place.business_item_offered` while this document consumed nothing |
| **15** *(v3)* | **`imminence` has a producer and it cannot reach `cast_score`** (§4.2) | Two assertions in one test: that `sl.rank` derives a non-constant `horizon.band` over a seeded season's candidate set, **and** that permuting every candidate's `horizon` leaves the Slate's *membership* bit-identical. The second is the load-bearing half — it is what keeps the derivation on the render side of the ratified severance. **Mutation check:** let `horizon` into `cast_score` and confirm the second assertion fails |
| **16** *(v3)* | **A never-lit candidate can be lit — no bootstrap deadlock** (§7.1) | Rank a seeded season's candidate set with an **empty** `slate.item_surfaced` history and assert the resulting Slate is ordered by `meaningfulness × scale_weight` and is **not** equal to the first `B` candidates under `candidate_id ASC`. Then assert the same at a non-empty history, so the test covers both the cold start and the P0-1 window. **Mutation check:** set `INERTIA_NEUTRAL = 0`, restoring v2.0's arithmetic, and confirm the Slate becomes hash-ordered. **This is the cheapest test on the list and the defect it catches makes season 1 of every campaign meaningless** |

**On guards (`00 §8` P0-4, `CLAUDE.md §0.1` point 5).** Every test above is load-bearing on **the
game**: 2, 3, 5, 9 and 12 on whether the player's season is coherent; 4 and 6 on whether the attention
system is honest; 7 on a canon constraint; 13 on whether the player is ever told what the world did;
14 on whether one seam has one answer; 15 on whether a ratified severance survives a fix that touches
it; **16 on whether the first season of a campaign is ordered by meaning or by hash.** **None guards
apparatus.** Note 11 is a *measurement*, not a guard, and §1.3a is explicit that it
now cuts in two directions.

### 11.2 Loops, each with its bound

| loop | bound | measured? |
|---|---|---|
| **light → slate → played → changed state → next season's light** — the ratified North-Star loop (`:272`), and the reason this document exists | Bounded by `B` per season and by the truncation's monotone top-`n`. **The dangerous form is across accountings, not within one**, and it is severed structurally: casting reads realized state only (§4.2), forecast objects are actor-invisible, and allocation is **one-pass per accounting** — no fixed-point iteration | **unmeasured.** Fixture F8 (`:283`) is the ratified test that would measure it and it does not exist |
| **inertia → lit → inertia** (attention self-reinforcing) | Bounded above by geometric decay (`NUM/DEN < 1`) and below by `STROBE_FLOOR` for `STROBE_MIN` seasons; the **exempt cap `X`** bounds how much of `B` past attention can occupy, and the **reserved slice `R ≥ 1`** guarantees a seat it cannot reach | **unmeasured.** The ratified fixture is F6 (`:553`) |
| **unserved candidate → `pressure` deposit → higher band → the place QUALIFIES under `08 §5` row 3** | Owned by `08`/`07`, not here. ⚠ **Re-stated in v3: this loop used to read *"→ more candidates"*, which was true only while `08` scaled its draw by `pressure`'s band. `08` O-6 deleted that quota, so a higher band no longer produces MORE candidates — it makes the place *qualify*, once, for the one row 3 candidate it would otherwise not emit.** The loop is therefore weaker than v2.0 described, not stronger. Bounded by geometric decay to a finite fixed point `rest + a/λ` (`01 §5.1`), and now additionally by the fact that its output is a boolean rather than a count. **The Slate does not participate**: it neither creates nor suppresses the deposit, because a shaded candidate resolves (§6) exactly as a surfaced one does | bounded by construction; rate unmeasured |
| **qualifying item never surfaced → still qualifying next season → emitted again** *(v3, and it is what deleting the quota adds)* | **`candidate_id` stability (§2.2).** The re-emission is the *same* candidate, so it accrues **inertia**, not volume — an unanswered thing gets more likely to surface, which is the correct behaviour and the reason the accounting index is deliberately not in the hash. Bounded above by `B` per season regardless | **unmeasured**, and it is the loop `§1.3a` point 3 says nobody would see fail |
| **player attends → thread persists → engaged → exempt → attends again** | `X` — a count cap, and §5.3 shows why it must be a cap | **unmeasured** |

### 11.3 Gates, each with what it reads

| gate | reads | rolls? |
|---|---|---|
| `sl.cast` knowability | the five witness channels; Thread Sensitivity for P-08-barred subjects | no |
| mandatory enumeration | the nine closed trigger predicates, with canon's own hysteresis and dedupe | no |
| exempt eligibility | whether a scene action was spent on this `candidate_id` in a prior season | no |
| reserved slice eligibility | whether any `slate.item_surfaced` exists for this `candidate_id` | no |
| one-post-op-per-boundary (§6.4) | the boundary's collected post operations | no |

### 11.4 P-iii and P-v, which do apply

**P-iii — no oscillation.** The failure a naive attention system has is *strobing*: a candidate on the
score boundary enters and leaves the Slate every season. The **anti-strobe floor** (§7) is the
hysteresis band, and it is the ratified mechanism, not an invention here. It is the same shape `01 §2.3`
requires of every reversible form transition, and it is required for the same reason.

**P-v — no dominant option.** The response set is 3–5 *"genuinely different in kind"* (`00 §2.2`) and
is supplied by the resolver, not by the Slate. **A dominant response is a defect in the resolver's
option set, not in the Slate** — and the Slate cannot mask one, because it can neither add nor remove
a response (C-5).

⚠ **That is a disclaimer, not an owner, and v2.0 shipped it as if it were both.** *"It belongs to the
resolvers"* was true and left **no document actually testing it**: no resolver document in the suite
picks up dominance testing, so the property is asserted at every site and checked at none. The worked
case is `08 §4.2`'s Comply/Defy fork, where **Comply looks structurally dominant** — Defy's gain
(`acceptance.support`) decays geometrically under `01 §5.1` while its costs (`standing` down,
`exposure` up, a `Precedent` tag) are durable and compound into the next season's Bargain obstacle.
Nobody has tested it and it is the one player decision `08` still ships.

**Where it goes, named rather than punted again: `13 §5`, as one shared falsifier binding every
document that declares a response set** — *each declared response is the argmax under some reachable
state*. It belongs in the build order and not here for a reason this document can state precisely:
**the Slate cannot run that test.** It never sees a resolver's effect rows, only response *ids*
(C-5), so it has no access to the quantity the test compares. **The Slate does not own dominance
testing, cannot own it, and this paragraph is the hand-off — not a second disclaimer.**

### 11.5 The six weakest points, named rather than buried

1. **P-B is asserted and unverified**, and it depends on a fork Jordan has not closed (fork C, the
   tolerance) plus a reading of a ruled doctrine that is itself filed as needing him (ED-SC-0024,
   ED-SC-0026). **§6.5 is the least-supported paragraph in this document.**
2. **§1.3's funnel ratios are estimates, and v3 made them *less* well-founded while making them
   larger.** They are the argument for the whole change. The v2.0 numerator rested on one auditable
   basis; the v3 numerator rests on six shape assumptions of which two carry ≈76% of the mass and
   neither is bounded anywhere in the suite (§1.3a point 2). **The change also inflates its own
   headline metric** — deleting `08`'s quota is what doubles the numerator — so the ratio that should
   be believed is the *pre-deletion control*, ≈21 : 1, which is still 7× the cut threshold (§1.3a
   point 1). Claim 11 is how both directions get measured.
3. **`|M| ≥ B` is reachable** and degrades the game to mandatory-only. Canon handles it; nobody has
   measured how often it happens.
4. **Two structural claims in this document were false in v2.0 and were found only when an unrelated
   edit forced their section open** — §6.2's *"the Slate writes nothing"* (contradicted by §7's own
   fallback) and §7's inertia baseline (a bootstrap deadlock on every cold start). Both are fixed in
   v3 and both now have falsifiers (claims 8, 16). **The weak point is not the two defects; it is that
   neither was found by the four rounds of review this suite has had, and both were sitting inside
   sections the review passed.** The honest inference is that prose-level review does not catch a
   contradiction between a normative table and a paragraph six sections away, and that claims 8 and 16
   should be among the first tests written rather than among the last.
5. **`forecast_mass` still has no producer, and §4.2 only fixed `imminence`.** The v3 derivation
   gives `imminence` a real input (a coarse band derived from published band-distance, render-side
   only). It does **nothing** for the other forecast term. So `depth_score` is now
   `cast_score × forecast_mass × imminence` with **one of the two multiplicands still constant**, and
   the honest description of the forecast layer is *half-produced*, not *working*. Naming a producer
   for `forecast_mass` needs a Layer-A forecast object that no document in this suite ships, and
   inventing one here would be the second scoring function §0 refuses.
6. **The product form of meaningfulness is asserted, not shown** (part 1 §0.1). A candidate with zero
   `identity_touch_bp` scores zero however durable and close it is. That is probably right and is
   certainly the ratified shape — but this document adopted it on the strength of the ratification and
   an intuition, not on evidence. **The falsifier is cheap and worth running early:** score one seeded
   season's candidate set under the product form and under a weighted-sum form, and inspect the two
   Slates side by side. If the product form drops items a reader judges obviously belong, the weight
   set is exposed data (`narrative_engine_design_v2_churn.md:279`) and is tunable toward additive
   **without re-ratification** — which is exactly why keeping the ratified shape costs nothing now.
