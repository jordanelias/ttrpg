# The Slate — Inertia, Contracts and Property Audit (part 2)

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`10_the_slate_and_salience.md`](10_the_slate_and_salience.md) — **part 1 first; this continues it**
## Part 1: §§0–6 (the override list, the funnel numbers, the candidate contract, the cast gate,
## the two orderings, truncation with its proofs, headless resolution and the skill premium)
## Part 2: §§7–11 (light-inertia without storage and **J-N**, **J-O**, the player surface,
## the module contracts, the property audit)

---

## 7. Light-inertia without storing anything, and **J-N**

The ratified inertia term (`:220`) is a **carryover across seasons**: `inertia_bp = inertia_bp · NUM // DEN`,
integer, a pure function of the accounting index, with an anti-strobe floor. Carryover across seasons is
exactly what `01 part 2 §9.3` says the substrate cannot do.

**Resolution: inertia is *derived from the Key log*, not carried and not stored.**

```
last_lit(c)   = the accounting_index of the most recent slate.item_surfaced Key with this candidate_id
inertia_bp(c) = 0                                   if none
              = INERTIA_BASE · NUM^(t − last_lit(c)) // DEN^(t − last_lit(c))     otherwise
anti-strobe:    if 0 < t − last_lit(c) ≤ STROBE_MIN ⟨shape: 2⟩ :
                    inertia_bp(c) := max(inertia_bp(c), STROBE_FLOOR)  ⟨shape⟩
```

`INERTIA_BASE`, `NUM`/`DEN`, `STROBE_MIN` and `STROBE_FLOOR` are **shape proposals**; they belong to
the ratified F-F weight surface (`:279`) as exposed versioned data.

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

**Fallback if the log is not queryable by `candidate_id` at acceptable cost:** a `Tag` with
`kind: Memory` on the candidate's anchor, `key = candidate_id`, `value = INERTIA_BASE`, decaying by
`01 §3.2`'s derived-salience law — the same arithmetic, one stored row per lit candidate, bounded by
`MEMORY_CAP`. **Named so the fallback is a decision and not an improvisation.** Prefer the log.

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
shaded, never sets a filter, never configures a priority, and never learns that 125 things happened and
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
| **1** | **This document designs no salience function** (§0) | Grep every score expression here against `narrative_engine_design_v2_churn.md:239-246`. A term appearing here that is not one of the ratified six — or the struck **novelty** term reappearing — falsifies it |
| **2** | **Truncation is bounded:** `\|Slate\| ≤ B` in every reachable state (§5.2) | A property test over random `(\|C\|, \|M\|, \|E\|)` triples asserting `\|Slate\| ≤ B`. **Separately measurable and NOT assumed:** the frequency of `\|M\| ≥ B` over a seeded 50-season campaign. If it exceeds a stated rate, the mandatory enumeration is too wide and §5.4 is wrong |
| **3** | **Truncation is monotone** (§5.3) | A property test: sample a candidate set and a comparator, raise one candidate's `cast_score`, assert it did not leave the Slate and that no candidate ranked below it entered. **Mutation check that the proof is load-bearing:** redefine the exempt set by a score *threshold* instead of a count *cap* and confirm the test then fails |
| **4** | **P-A — a candidate's outcome does not depend on whether any other was surfaced** (§6.3) | Run a seeded season twice with identical state, differing only in which Slate items were attended, with all attended items forced to the AI policy. Assert the resulting world state is **bit-identical**. **This is the single most important test in the document.** Mutation check: replace the per-candidate substream with a shared sequential stream and confirm it fails |
| **5** | **P-C — order neutrality** (§6.3) | Resolve one season's candidate set under `n` random permutations; assert one state. Mutation check: allow two post operations on one post per boundary and confirm it fails |
| **6** | **P-B — baseline parity** | The **parity harness** of `auto_manual_resolution_duality_v1.md:67`, comparing auto against **AI-played** on matched inputs. ⚠ **The tolerance is fork C, genuinely open**, and this document does not set it. Until the harness lands, P-B is **asserted and unverified** |
| **7** | **No unknowable candidate reaches the Slate** (§3) | A test asserting every Slate member has a non-empty `witness` on one of the five channels, and that no Thread-constituted candidate is cast to a person below the canonical Thread Sensitivity gate. This is P-08's own falsifier applied to the attention system |
| **8** | **The Slate writes nothing** (§6.2) | A contract test asserting all four `sl.*` modules have `state: []`, no `form:`, no `transitions:`, and a resolver in `{gate, derivation}` |
| **9** | **Candidate identity is stable across seasons** (§2.2) | A seeded campaign asserting a persisting situation keeps one `candidate_id` across ≥ 3 seasons. Mutation check: add `accounting_index` to the hash and confirm inertia stops carrying |
| **10** | **Zero new player verbs** (§1.4) | Count verbs across the suite before and after `10`. This document must add 0 and does add 0 — it adds one *interaction* (attend) which is the budget's own unit, not a verb over the world |
| **11** | **The funnel ratios of §1.3** | They are **estimates with stated bases, not measurements**. Falsified by instrumenting one seeded 50-season campaign and counting emitted candidates per season. **If the true rate is under ~3× the budget, the Slate is not earning its keep and D should be cut** |

**On guards (`00 §8` P0-4, `CLAUDE.md §0.1` point 5).** Every test above is load-bearing on **the
game**: 2, 3, 5 and 9 on whether the player's season is coherent; 4 and 6 on whether the attention
system is honest; 7 on a canon constraint. **None guards apparatus.**

### 11.2 Loops, each with its bound

| loop | bound | measured? |
|---|---|---|
| **light → slate → played → changed state → next season's light** — the ratified North-Star loop (`:272`), and the reason this document exists | Bounded by `B` per season and by the truncation's monotone top-`n`. **The dangerous form is across accountings, not within one**, and it is severed structurally: casting reads realized state only (§4.2), forecast objects are actor-invisible, and allocation is **one-pass per accounting** — no fixed-point iteration | **unmeasured.** Fixture F8 (`:283`) is the ratified test that would measure it and it does not exist |
| **inertia → lit → inertia** (attention self-reinforcing) | Bounded above by geometric decay (`NUM/DEN < 1`) and below by `STROBE_FLOOR` for `STROBE_MIN` seasons; the **exempt cap `X`** bounds how much of `B` past attention can occupy, and the **reserved slice `R ≥ 1`** guarantees a seat it cannot reach | **unmeasured.** The ratified fixture is F6 (`:553`) |
| **unserved candidate → pressure deposit → higher band → more candidates** | Owned by `08`/`07`, not here. Bounded by geometric decay to a finite fixed point `rest + a/λ` (`01 §5.1`). **The Slate does not participate**: it neither creates nor suppresses the deposit, because a shaded candidate resolves (§6) exactly as a surfaced one does | bounded by construction; rate unmeasured |
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

### 11.5 The four weakest points, named rather than buried

1. **P-B is asserted and unverified**, and it depends on a fork Jordan has not closed (fork C, the
   tolerance) plus a reading of a ruled doctrine that is itself filed as needing him (ED-SC-0024,
   ED-SC-0026). **§6.5 is the least-supported paragraph in this document.**
2. **§1.3's funnel ratios are estimates.** They are the argument for the whole change, and they are not
   measured. Claim 11 is how they get measured, and it names the number at which the change should be
   cut instead of shipped.
3. **`|M| ≥ B` is reachable** and degrades the game to mandatory-only. Canon handles it; nobody has
   measured how often it happens.
4. **The product form of meaningfulness is asserted, not shown** (part 1 §0.1). A candidate with zero
   `identity_touch_bp` scores zero however durable and close it is. That is probably right and is
   certainly the ratified shape — but this document adopted it on the strength of the ratification and
   an intuition, not on evidence. **The falsifier is cheap and worth running early:** score one seeded
   season's candidate set under the product form and under a weighted-sum form, and inspect the two
   Slates side by side. If the product form drops items a reader judges obviously belong, the weight
   set is exposed data (`narrative_engine_design_v2_churn.md:279`) and is tunable toward additive
   **without re-ratification** — which is exactly why keeping the ratified shape costs nothing now.
