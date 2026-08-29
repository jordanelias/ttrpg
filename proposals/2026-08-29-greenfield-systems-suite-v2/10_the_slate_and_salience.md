# The Slate — Candidates, Truncation, and Headless Resolution

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Version: v2.0 · Lane: IN (touches SC, SE, WR, FA) · Change **D**
## Reads: [`00_INDEX.md`](00_INDEX.md) · [`01_substrate_primitives.md`](01_substrate_primitives.md) ·
## [`01_substrate_primitives_part2.md`](01_substrate_primitives_part2.md) ·
## `audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md` §1–§4 (**RATIFIED**, ED-IN-0011) ·
## `systems/_architecture/player_agency_v30.md` §4 (**CANONICAL** 2026-04-17) ·
## `systems/_architecture/auto_manual_resolution_duality_v1.md` (**RULED** Jordan 2026-07-08, ED-SC-0013) ·
## `systems/_architecture/scale_transitions_v30.md` §4.3–§4.4 · `canon/02_canon_constraints.md` (P-08) ·
## `engine/autoload/scene_slate.py` · `registers/editorial_ledger_sc.jsonl` (ED-SC-0024, ED-SC-0026)

---

## 0. ⚠ THIS DOCUMENT DOES NOT DESIGN A SALIENCE FUNCTION

**The salience function is ratified canon and lives elsewhere.** `narrative_engine_design_v2_churn.md`
§4 — the **Light Function** — was ratified by Jordan on 2026-07-05 (ED-IN-0011) and is named as the
Narrative-engine head at `CURRENT.md:40`. It already owns: the selection score in integer basis points
(`:239`), the severance of casting from forecast (`:206`), light-inertia with an anti-strobe floor
(`:221`), the exempt cap and reserved promotion slice (`:223`), four coherence invariants, and the
weight set as exposed versioned data.

**This document binds to it and specifies the seam.** It contributes four things the Light Function
does not have and cannot supply for itself:

| this document owns | because the Light Function assumes it |
|---|---|
| **the candidate contract** — what an emitter must supply so the light can score it | it rations *"among candidates the churn produced"* and never says what one is |
| **the cast gate** — knowability before ranking (P-08, `01 §8`) | it requires a focalizer for the *render*; nothing yet forbids casting an unknowable candidate |
| **truncation to the scene budget**, proved bounded and monotone | it names a budget and a cap; the arithmetic of the cut is not written down |
| **headless resolution and its invariance** — the property that makes the filter honest rather than a cheat | it is subtract-only *by rule*; nothing yet makes that true *by construction* |

**If v2 needs a scoring term the ratified set lacks, that is a ruling request, not an edit.** This
document requests none. Every score term named below is one of the ratified six.

*Emergent possibility lost if the Slate were cut:* **none — cutting it adds volume.** What is lost is
the player's ability to perceive any of it. This is the one change in the suite that is pure
distillation, and it is why `00 §8` P0-5 lands it before B, F and G.

---

## Overrides

| # | What is overridden | Tier | Decision |
|---|---|---|---|
| **O-10.1** | `player_agency_v30.md:311-327` — the **cross-step lexicographic pruning algorithm** (sort non-mandatory entries by `(step_number, internal_index)`, take the first *k*) | **(2) ratified canon** | **Superseded by the Light Function's cast score.** Two ratified surfaces answer the same question and disagree: a step-order sort is *provenance-ranked* (a Duty-aligned entry always outranks an NPC-outreach entry, whatever is at stake in either), while ED-IN-0011 ranks on **meaningfulness × tie-proximity × identity-touch × inertia** and claims the relevance function as *"the engine's central object"*. The later ratification wins on both date (2026-07-05 vs 2026-04-17) and merit: step order cannot express *"this small thing is about your brother"*. **What survives untouched:** every Step-1..6 generator (they become emitters, §2.4), the budget (§1.2), mandatory bypass, Witness Mode, and the §4.5 not-pursued consequence table. Only the *comparator* changes |
| **O-10.2** | `player_agency_v30.md:262-272` — the Step-4 Conviction scan's **inline roster of NPC names, faction names, 17 territory names, ~25 keywords and 11 role→NPC mappings** | **(2) ratified canon**, mechanically minor | The scan is kept whole; its **tables move to `references/names_index.yaml`**, which `CLAUDE.md §4` already names as the single owner of definition naming. A generator that names Almud, Baralta and Ehrenwall inline is the `if faction == X` shape `00 §6` principle 2 rejects. Intent unchanged; storage corrected |
| **O-10.3** | `auto_manual_resolution_duality_v1.md:65` — *"consistency makes the fidelity choice free of strategic advantage"*, read as **E[auto] ≈ E[expert-played]** | **(1) a Jordan ruling — NOT overridden here; flagged** | **This document takes the AI-played-baseline reading** (§6.4) and says so, because a design must take one to be buildable. It does **not** claim authority to amend the ruling. **ED-SC-0024** (`registers/editorial_ledger_sc.jsonl`, `status: open`, `needs_jordan: true`) already files exactly this amendment, and **ED-SC-0026** supplies the argument that forces it: under the strict reading *"playing a contest is strictly wasted attention."* **If Jordan rules for strict parity instead, only the parity harness's baseline changes — no structure in this document moves** (§6.4, last paragraph) |
| **O-10.4** | *(not an override — recorded so the seam is not mistaken for one)* `engine/autoload/scene_slate.py` | shipped code | It is a 59-line priority **queue** (`queue_scene` / `next_scene`, sorted by an integer `priority`), with no budget, no salience, no truncation and no fidelity. `references/module_contracts.yaml:611` calls it a *"deterministic 7-priority slate generation"*; the file does not generate anything. It is **adopted as the dispatch buffer downstream of `sl.truncate`** (§5.5), not replaced |

**Adopted whole rather than overridden**, recorded because deciding *not* to override is also a
decision: the **Light Function** entire (§0); **fork A** of ED-SC-0013 (`:75`, *"auto = the contest
kernel run headless, played = the same kernel run interactively"*) entire (§6.1); **Witness Mode** and
the mandatory-overflow rule entire (`player_agency_v30.md:186-193`); and **`scale_transitions_v30 §4.4`
"Where Were You?"** entire — which is, independently arrived at and three months earlier, the ratified
Light Function's *"re-light renders the catch-up retroactively and always focalized"*. Two documents
converging on one mechanism without citing each other is the strongest evidence available that the
mechanism is right.

---

## 1. What the Slate is, and the numbers that make it the suite's whole answer

### 1.1 The claim

> **The Slate is how a deep world reaches a player through a small surface.** It is the only object in
> v2 that is *wholly* surface, and it is the reason every other object in v2 can be substrate.

`00 §2` sets a hard playing-surface budget: single-digit verbs, 3–5 responses per situation, and
*"decisions per season = the scene budget, and nothing else."* Changes A, B, C, E, F and G all
**increase what the world produces**. Without D, that increase reaches the player as volume — which is
Jordan's *oatmeal soup*: a hundred true, caused, well-provenanced things a season, none of which is
worth reading because all of them arrived.

### 1.2 The budget, which is canon and not a proposal of mine

| difficulty | opportunities on the Slate (`B`) | scene actions (`A`) | source |
|---|---|---|---|
| Narrative | 4–5 | 5 | `player_agency_v30.md:306` |
| Normal | 5–7 | 4 | `player_agency_v30.md:304` |
| Hard | 7–9 | 3 | `player_agency_v30.md:305` |

*"The surplus is the point"* (`:308`). *"Choosing what to attend is the gameplay"*
(`auto_manual_resolution_duality_v1.md:16`). **These numbers are ratified canon; I neither propose nor
retune them.** Every other constant in this document is a **shape proposal** and is marked as one.

### 1.3 The numbers — what the funnel actually is

**All per-emitter rates below are shape proposals with stated bases, not ledger constants.** They are
here because "minimise the playing surface" is an unfalsifiable instruction until someone writes down
the ratio it is asking for.

Per season, over a world of **37 settlements** (35 in-kingdom + 2 special-case march targets,
`systems/settlements/settlement_layer_v30.md:310`):

| emitter | rate basis | candidates / season |
|---|---|---|
| `08` place business | v1's `n = 1 + floor(pressure_band)` per place; five bands, mean band ≈ 1 | ≈ 70–75 |
| `09` projects | one advance/fire/lapse emission per active project; ~75 project-holding actors (≈30 named NPCs per churn `:76`, plus local actors at `settlement_layer_v30 §4.5`'s ruled per-type counts), ~⅓ emitting | ≈ 25 |
| `05`/`06` faction activity | 4–8 factions (count unreconciled, churn `:107`) × declared actions across tiers | ≈ 20 |
| `11` world events | rate-bounded by `11`'s own declared ceiling | ≤ 5 |
| `01 §2` form transitions | places and people crossing gated bands | ≈ 3 |
| `04` vacancies / appointments | posts falling vacant, terms expiring | ≈ 5 |
| **total** | | **≈ 125–130** |

| ratio | value |
|---|---|
| candidates : Slate entries (Normal, B = 6) | **≈ 21 : 1** |
| candidates : scene actions (Normal, A = 4) | **≈ 32 : 1** |
| over a 50-season campaign (`engine/tests/test_mc_v18_regression.py:16` runs 50-season campaigns) | ≈ **6,400 candidates resolve** · ≈ **300 surface** · ≈ **200 are played** |
| **fraction of what happens that the player ever sees** | **≈ 4.7%** |
| **fraction the player acts on** | **≈ 3.1%** |
| **fraction that resolves** | **100%** |

**That last row is the whole design.** The other 95% is not skipped, deferred, or approximated away —
it is resolved, at the same fidelity the AI would have given it had the player attended (§6), and it
deposits into the same gauges and writes the same tags. The player's window is 5%; the world is 100%.

### 1.4 What the Slate costs the player to learn

**Zero verbs.** The Slate adds no entry to the player's verb set. A Slate item offers **3–5 responses,
supplied by the candidate's own resolver row** (`00 §7`'s `remit` gate — the option set is a property
of the post the player holds, never of the Slate). The player learns *one* interaction: read the item,
pick a response or let it pass. Everything else they learn is **about the world**, not about the
interface — which is the distinction `00 §2.2` is making when it says depth comes from *which*
situation arrives.

---

## 2. The candidate — the contract every emitter satisfies

**This is the document's real deliverable.** The Light Function rations *"among candidates the churn
produced"* and never defines a candidate. Here is the definition.

### 2.1 The row

A candidate is **derived, never stored** (§7). It is a value an emitter returns at the accounting
boundary, in this shape:

```yaml
candidate:
  candidate_id:   <deterministic hash; §2.2>
  emitter:        <module id that produced it>          # e.g. sm.business, am.advance, we.fire
  kind:           <row id in references/content_registry.yaml>
  # ── anchoring: where and how big ────────────────────────────────────────────
  anchor:         <entity_id>            # the place, faction or person the situation IS AT
  scale:          personal | settlement | territory | peninsula   # 00 §3's runtime four
  subject_refs:   [<entity_id>, ...]     # sorted; everything the situation is ABOUT
  # ── the realized-state terms the Light Function scores (§4) ────────────────
  durability_bp:      <int>   # how long its consequence persists, in accountings
  identity_touch_bp:  <int>   # whether it bears on a subject's identity/convictions
  # tie_proximity_bp is NOT supplied by the emitter — it is derived (§4.1)
  # ── the forecast terms, which may govern DEPTH and never ENTRY (§4.2) ──────
  horizon:        {band: <int>, foreclosure_in: <int|null>}  # from Layer-A only, M1
  # ── resolution ─────────────────────────────────────────────────────────────
  resolver_ref:   <module id>            # the ONE module that resolves this, at either fidelity
  responses:      [<3..5 response ids from resolver_ref's declared option set>]
  mandatory:      <bool>                 # §5.4; enumerated rows only
  # ── epistemics and honesty ────────────────────────────────────────────────
  witness:        {channel: chronicle | witness_key | document_key | post_remit | co_located,
                   ref: <key_id | entity_id | post_id>}       # §3; REQUIRED, non-empty
  provenance:     <key_id>               # REQUIRED, non-empty — the Key that caused this
  disclosure_ref: <state id>             # the E-2 block governing what may be shown
```

**Six rules, all normative.**

| # | Rule | The failure it prevents |
|---|---|---|
| **C-1** | **`provenance` is required and non-empty**, exactly as `01 §3.3` requires of every Tag. A candidate with no causing Key cannot be constructed. | The channel by which a situation appears for no reason. In a game with no GM this is the property that makes the layer trustworthy — v1 `08 §5` got this right and it is carried verbatim in substance |
| **C-2** | **`witness` is required and non-empty** (§3). | A salient thing the player cannot know about leaking through the Slate — P-08's barrier being quietly institutional rather than metaphysical |
| **C-3** | **An emitter supplies realized-state terms only.** `durability_bp` and `identity_touch_bp` are functions of state on the board. An emitter may not supply, and the Slate may not read from it, any term computed from a *projected* future other than through `horizon`. | Part VI's world-visible-imminence prohibition and `01 §8`'s *"never publish the trigger"*, which are one rule seen from two sides |
| **C-4** | **`resolver_ref` names a module that already exists in `module_contracts.yaml` and resolves this candidate at *both* fidelities.** The Slate never names a "summary" or "auto" module. | A second cheaper resolution path — the Total War seam ED-SC-0024 records the community finding and exploiting |
| **C-5** | **`responses` is 3–5 ids drawn from `resolver_ref`'s declared option set, filtered by the player's `remit`.** The candidate does not invent responses. | Verb creep. `00 §2.2` caps responses at 3–5 *"genuinely different in kind"*; a candidate that could mint its own would route around the cap |
| **C-6** | **An emitter emits; it never presents, ranks, or checks the budget.** It does not know `B`, does not know what else was emitted, and cannot see the Slate. | The reason this is one function and not eight competing ones. v1's `sm.business` drew `1 + floor(pressure_band)` items *and presented them* — a per-place budget with no global view, which is how a 37-place world manufactures 75 undifferentiated demands |

### 2.2 `candidate_id`, and why the season is deliberately not in it

```
candidate_id = H( emitter ‖ kind ‖ anchor ‖ sorted(subject_refs) ‖ provenance )
```

A **fixed cross-platform hash** — the discipline the churn doc `:180` already demands of the ensemble
seed: never Python's per-process-salted `hash()`, never wall-clock, identical bytes on Python and
GDScript.

**The accounting index is not an input, and that is load-bearing.** A situation that persists across
seasons — an unserved claim, a running project, a place stuck at a bad band — must keep the *same* id,
or light-inertia (§4.1, §7) has nothing to carry and the anti-strobe floor cannot bind. A per-season id
would make every persisting situation look brand new every season, which is the exact opposite of
attention having momentum.

**Consequence, stated so it is not a surprise:** a genuinely recurring-but-distinct situation must
differ in one of the five hashed fields. Where it does not — the same claim coming due twice — it is
*the same candidate*, and that is correct: it was never answered.

### 2.3 What a candidate is not

| not | because |
|---|---|
| a stored object | §7 — derived at the boundary from state, stored nowhere. No fifth stored kind; no aggregate written (AU-1) |
| an entity | it has no identity that persists independently of its cause. Kill the cause and the candidate ceases to exist, which is right |
| a "card" or authored content | its content is the world's own state. Authored framing remains possible later as an enrichment on an existing row — never as a precondition, or the mechanic is inert until content exists |
| a *subsystem* | `00 §1`'s corollary: a candidate is a **row**, and the Slate is four derivation modules over rows (§10) |

### 2.4 The emitters, and what each owes

Every emitter in the suite stops presenting and starts emitting. `player_agency_v30 §4.2`'s seven
generation steps are kept **as emitters** (O-10.1) and are listed here beside v2's new ones so the set
is one set.

| emitter | owned by | supplies | notes |
|---|---|---|---|
| `sm.business` | `08` | place business from tags and gauge bands | **Its per-place `1 + floor(pressure_band)` draw is deleted, not scaled.** It emits *all* qualifying items; the global budget does the cutting. This is `08`'s single largest simplification |
| `am.advance` / `am.fire` / `am.lapse` | `09` | project beats | J-N: these fire because the world *is* a certain way at the boundary (§8) |
| `we.fire` | `11` | conditioned exogenous events | Routes **through** the Slate, never around it — Part VI's second surfacing path prohibition |
| `fa.*` | `05`/`06` | faction directives, bloc friction, divergence crossings | mostly NPC-invoked; what reaches the player is a candidate |
| `pm.vacancy` / `pm.tenure` | `04` | vacancies, terms expiring, contested appointments | |
| `substrate.form` | `01 §2` | form transitions, as **crossing facts** | Part VI: `threshold_crossed` carries crossing facts, never forecasts |
| **the eight mandatory triggers** | `scale_transitions_v30 §4.3.2` | Priority-0 rows | enumerated, `mandatory: true` (§5.4) |
| **the five world-state triggers** | `scale_transitions_v30 §4.3.3` | clock band transitions, treaties, control changes, Warden emergencies | |
| **Duty / Conviction / Outreach scans** | `player_agency_v30 §4.2` Steps 3–5 | the player-rooting terms, which is invariant (iii) of the Light Function | reads `references/names_index.yaml` per O-10.2 |

---

## 3. The cast gate — knowability is a **gate**, salience is a **ranking**

This is `01 §8`'s disclosure contract and canon constraint **P-08** applied to the Slate, and it is the
one place where the design must refuse to show the player something the light would happily rank first.

> **A candidate is cast only if it is knowable. Salience never buys knowability, and knowability never
> substitutes for salience.** The two are composed as `gate THEN rank`, never summed, never traded off.

P-08 (`canon/02_canon_constraints.md:17`): *"epistemological barrier = inaccessibility, not
suppression … the barrier is metaphysical, not institutional."* Its falsifier is stated in canon:
*"does any mechanic allow non-sensitives to gain Thread-level knowledge through study alone? If yes →
FAIL."* **A Slate that surfaced a Thread-constituted situation to a non-sensitive because it scored
highly would be exactly that failure**, delivered by the attention system rather than by a study rule.

### 3.1 The five witness channels

`witness.channel` must be one of five, and each is checkable:

| channel | holds when | what the item may show |
|---|---|---|
| `post_remit` | the player holds a post whose `remit` covers the subject | the institutional record — inputs published, band presentation, trigger hidden (`01 §8`) |
| `co_located` | the player's person is at the anchor place | direct perception |
| `witness_key` | a person with an edge to the player perceived it, and holds the **Memory** (`01 §3.1`) | **the witness's memory, which may be false** — §3.2 |
| `document_key` | a document, letter or record exists and has reached the player | the document's claim, with its own reliability |
| `chronicle` | the sanctioned past-tense register, for retrospective catch-up | `scale_transitions_v30 §4.4` — *about the player's relationship to the event*, never a replay |

These are the churn doc's `chronicle | witness_key | document_key` focalizers (`:270`) plus the two
that a *playable* protagonist has and a chronicle reader does not. **No sixth channel** — a candidate
that fits none of the five is shaded, whatever it scores.

### 3.2 The three consequences that make this a mechanic and not a filter

1. **Misperception reaches the Slate; the world's state does not.** A `witness_key` candidate is built
   from the witness's Memory tag, whose `value` is salience and whose content may be wrong. The
   disclosure contract still holds exactly, because what is published is **the witness's claim with its
   provenance**, not the world's state. This is what `01 §3.1` bought when it opened the tag enum to
   six, and the Slate is its principal consumer. **Memory sits inside `01 §3.4`'s relational cap** — it
   shifts weighting, never the board.
2. **A P-08-barred candidate is not suppressed; it arrives thinner.** A Thread-constituted situation
   reaching a non-sensitive is cast through its **surface effects** — the failing harvest, the sick
   cattle — with the Thread-level payload absent. The player sees that something is happening and
   cannot see what. Inaccessibility, not suppression, which is precisely what P-08 asks for.
3. **The gate is disclosed as an input.** Per `01 §8`, inputs are published: a player may inspect *why*
   an item is on their Slate (which channel carried it) and may reason about what channels they lack.
   The **trigger** — the score, the threshold, the budget arithmetic — stays hidden.

### 3.3 The one thing this forbids outright

**A candidate may not be cast on the strength of its salience alone**, and no term in the score may
raise a candidate over the gate. Mandatory rows (§5.4) bypass *ranking*; **they do not bypass the
cast gate** — every one of the eight mandatory triggers in `scale_transitions_v30 §4.3.2` is
knowability-satisfied by construction (each names the player's presence, targeting, or faction), which
is why the exemption costs nothing. If a future mandatory row is proposed that is not, it is rejected.

---

## 4. The ordering — two scores, because the ratified severance says two

The Light Function's selection score is (`narrative_engine_design_v2_churn.md:239`):

> meaningfulness (durability × tie-proximity × identity-touch) × **forecast mass** × **imminence** ×
> light-inertia carryover × scale-allocation weight

and it comes with the binding that makes it two scores rather than one (`:206`, `:243`):

> **casting is severed from forecast** — slate entry and summons key on the tie-graph and **realized**
> state only; forecast mass and imminence govern **render depth**, never which futures are impelled at
> the player.

### 4.1 `cast_score` — decides Slate entry. Realized terms only.

```
cast_score(c) = meaningfulness(c) × inertia(c) × scale_weight(c.scale)          [integer basis points]

meaningfulness(c) = durability_bp(c) × tie_proximity_bp(c, player) × identity_touch_bp(c)
```

**`tie_proximity_bp` is derived here, not supplied by the emitter** (C-3): it is the shortest path in
the edge graph (`01 §7`) from the player to any of `c.subject_refs`, converted to basis points by a
declared monotone-decreasing table. Deriving it centrally is what makes invariant (iii) —
**player-rooting** — hold for every emitter without every emitter having to know about the player.

`inertia(c)` is §7. `scale_weight` is the ratified scale-allocation term, keyed on `00 §3`'s runtime
four.

**Integer basis points throughout, `//` not `/`.** The churn doc's determinism discipline (`:180`) is
not decoration: float accumulation order differs between Python and GDScript and this ordering crosses
the port.

### 4.2 `depth_score` — decides render depth among the cast. Never entry.

```
depth_score(c) = cast_score(c) × forecast_mass(c) × imminence(c.horizon.band)
```

Computed **only for candidates already cast**, and it may change nothing about membership. It governs
how much the item is rendered, in how much detail, with how much anticipation texture.

**Why the severance matters concretely, in one sentence:** without it, forecasting that a settlement
will revolt makes the engine surface the settlement, which makes the player act on it, which changes
the forecast — the rubber-banding loop the churn doc `:274` severs structurally, and which fixture F8
(`:283`) exists to prove severed. **A design that merged the two scores would silently rebuild it.**

### 4.3 What is deliberately not in either score

| absent term | why |
|---|---|
| **novelty** | The ratified term is **light-inertia**, which is the *opposite shape*: attention has momentum. An earlier draft of the delta spec proposed novelty; it was struck. **Do not reintroduce it without a ruling** |
| **emitter identity / step number** | O-10.1. Ranking by *where a candidate came from* cannot express that a small thing is about the player's brother |
| **anything the player did last season** other than through inertia and tie-proximity | both already carry it, and a third channel would double-count |
| **any relational term above `01 §3.4`'s cap** | Memory and edge terms enter through `tie_proximity_bp` and are bounded by `RELATION_SHARE_MAX`. **Reachability bar:** at the maximum reachable relational total, the structurally-least-meaningful candidate must still be unable to outrank the structurally-most-meaningful one |

---

## 5. Truncation to the scene budget

### 5.1 The rule

Let `B` = slate target size and `A` = scene actions, both from §1.2. Constants marked ⟨shape⟩ are shape
proposals; the ratified surface (`narrative_engine_design_v2_churn.md:279`) is what makes them
**exposed versioned data**, tunable without re-ratification.

```
INPUT   C = { candidates emitted this boundary that pass the §3 cast gate }
CONST   X = exempt cap ⟨shape: 2⟩          R = reserved promotion slice ⟨shape: 1; ratified minimum 1⟩

1. M  := { c ∈ C : c.mandatory }                                     # §5.4, enumerated
   if |M| ≥ B:  Slate := M ;  goto 6                                 # mandatory-only; canon :314
2. E  := top-X of { c ∈ C∖M : engaged(c) } by cast_score             # demotion-exempt, but CAPPED
3. k  := max(0, B − |M| − |E| − R)                                   # free slots — score-independent
   F  := top-k of { c ∈ C∖(M∪E) } by cast_score
4. P  := top-R of { c ∈ C∖(M∪E∪F) : never_lit(c) } by cast_score     # the reserved slice
5. Slate := M ∪ E ∪ F ∪ P
6. Shade := C ∖ Slate                                                # → §6, headless, all of it
```

**Comparator:** `(cast_score DESC, candidate_id ASC)`. The tie-break on a deterministic hash makes the
order **total**, which is what §5.3 needs and what a score-only comparator does not give.

`engaged(c)` = the player spent a scene action on `c` in a prior season and it has not terminated —
the ratified demotion-exemption for player-pursued threads (`:222`). `never_lit(c)` = no
`slate.item_surfaced` Key exists for `candidate_id` (§7).

**Why `X` and `R` both exist, per `:223`:** exempt-only would let a player who engages `B`-many threads
starve every emergent and imminent candidate forever — the refuter's starvation case. The cap bounds
how much of the budget past attention can hold; the slice guarantees at least one seat the exempt set
**cannot** consume. Neither alone is sufficient and the ratified text says so.

### 5.2 Boundedness — proof

**Claim.** `|Slate| ≤ B` in every state, and `|Slate| ≥ min(|C|, R)` whenever `C ≠ ∅`.

**Upper bound.** Step 1 exits with `|Slate| = |M|` only when `|M| ≥ B`, so the bound needs `|M|` itself
bounded: **`M` is drawn from a closed enumeration** of mandatory rows (§5.4) and deduplicated per
`(trigger, anchor, accounting_index)` — the deduplication `scale_transitions_v30 §4.3.2` already
requires of settlement events (ED-750). Hence `|M| ≤ M_MAX`, a registry-counted constant. Otherwise
`|M| < B`, and `|Slate| = |M| + |E| + |F| + |P| ≤ |M| + X + k + R` where `k = max(0, B − |M| − |E| − R)`.
If `B − |M| − |E| − R ≥ 0` the sum is exactly `B`; if negative, `k = 0` and the sum is
`|M| + |E| + |P| < B` because that is the case the clamp fired in. Either way `≤ B`. ∎

**Lower bound.** `P` is taken last from the residue and is non-empty whenever an un-lit candidate
remains, so the Slate is never empty while the world produces anything — the *"never surface an emptier
Slate than the band floor"* clause `player_agency_v30.md:295` distilled into Step 6's backfill. **Here
the backfill is unnecessary**, because the emitters are no longer per-place-rationed (§2.4) and `C` is
two orders of magnitude larger than `B`. **That is a real simplification the truncation buys: a global
budget makes underfill structurally impossible, so the floor clause can be deleted rather than
implemented.**

⚠ **The one live hazard, stated rather than hidden.** `|M| ≥ B` degrades the game to mandatory-only
with Witness overflow, and it is reachable: eight mandatory triggers exist and a bad season can fire
several. Canon already accepts and handles this (`player_agency_v30.md:186`). **The bar this design
adds: `M_MAX` must be enumerable and the probability of `|M| ≥ B` must be measured, not assumed
small.** It is a falsifier in §11, not a claim.

### 5.3 Monotonicity — proof, and the trap it avoids

**Claim.** Raising one candidate's `cast_score`, all else equal, (a) never removes it from the Slate,
and (b) never adds to the Slate any candidate that was below it.

**Proof.** Steps 2–4 are each *"take the top-`n` of a set under a total order."* Such an operation is
monotone in each element's key **provided `n` does not depend on the keys**. Check each:

- `|M|` is fixed by a **gate** over enumerated rows — no score is read (§5.4). Score-independent. ✔
- `|E| = min(X, |{engaged}|)` — `X` is a constant and engagement is a fact about past seasons, not a
  score. Score-independent. ✔ *(This is the trap: had the exempt set been defined by a score
  **threshold** rather than a count **cap**, `|E|` would move with the scores, `k` would move with
  `|E|`, and raising one candidate's score could evict an unrelated one. **The ratified text says
  `cap`; the cap is what makes the proof go through.** Do not "improve" it into a threshold.)*
- `R` is a constant. ✔
- Therefore `k = max(0, B − |M| − |E| − R)` is score-independent, and each of Steps 2–4 is a monotone
  top-`n`. Composition of monotone selections over disjoint residues is monotone. ∎

**Why this property is worth proving.** Without it, the Slate is *unexplainable*: a player who acts to
make something matter more could watch it fall off the Slate, and there would be no honest account of
why. Monotonicity is what lets `01 §8`'s *"publish every input"* actually mean something — the inputs
are only worth publishing if moving them moves the outcome in the direction they point.

### 5.4 Mandatory bypass — rare, enumerated, and gated not scored

**Mandatory rows bypass ranking. They do not bypass the cast gate (§3.3), and they are not a general
mechanism.** The set is exactly the eight triggers at `systems/_architecture/scale_transitions_v30.md:125-141`
plus the one Thread-state row at MS ≤ 20 (`player_agency_v30.md:207`), and it is **closed**. Each is a
`gate` resolver (`00 §7`): a predicate over state, with no roll and no score. Adding a tenth requires
the same argument `01 §3.1` demanded for opening the tag enum — not *"this feels important."*

Each carries its own hysteresis where canon supplies one (Stability Crisis re-arms only after Stab ≥ 3
for two consecutive Accountings, ED-749) and its own dedupe (ED-750). **Those are not this document's
inventions and are not retuned here.**

Over-budget mandatories fall to **Witness Mode** (`player_agency_v30.md:186-193`) — present, one Read
or Appraise at Ob 1 requiring **a real roll, not an auto-success**, no Domain Echo, no Momentum or
Coherence spent. Adopted whole.

### 5.5 What the Slate hands downstream

`sl.truncate` emits one `slate.item_surfaced` Key per Slate member (`00 §9.2`), carrying
`candidate_id`, the score components, rank, and whether mandatory, and it writes a **fidelity label**
onto each candidate in the boundary's derived candidate set:

| label | who gets it | what it means |
|---|---|---|
| `played` | Slate members the player spends a scene action on | interactive; the player supplies the decisions |
| `witnessed` | mandatory overflow | present, one roll, no direction |
| `auto` | everything else — Slate members not attended, **and the whole Shade** | headless; NPC-AI supplies the decisions |

**The Slate does not resolve anything.** The label is a datum; the candidate's own `resolver_ref`
module, invoked by **its own subsystem's herald** (`01 part 2 §9.1`), does the resolving. See §6.2 —
this is the design's defence against Part VI's distributor prohibition and it is structural, not
rhetorical.

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
| **P-B** | **Baseline parity** | `E[outcome(c) | auto] = E[outcome(c) | AI-played]`. The auto path *is* the AI playing it — not a summary, not a table, not a cheaper approximation |
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
| **P-B binds the magnitude** | `E[outcome(c) | auto] = E[outcome(c) | AI-played]`. Nobody gains expected value by choosing a fidelity. Mode-shopping is dead |
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
| **2** | **Truncation is bounded:** `|Slate| ≤ B` in every reachable state (§5.2) | A property test over random `(|C|, |M|, |E|)` triples asserting `|Slate| ≤ B`. **Separately measurable and NOT assumed:** the frequency of `|M| ≥ B` over a seeded 50-season campaign. If it exceeds a stated rate, the mandatory enumeration is too wide and §5.4 is wrong |
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

### 11.5 The three weakest points, named rather than buried

1. **P-B is asserted and unverified**, and it depends on a fork Jordan has not closed (fork C, the
   tolerance) plus a reading of a ruled doctrine that is itself filed as needing him (ED-SC-0024,
   ED-SC-0026). **§6.5 is the least-supported paragraph in this document.**
2. **§1.3's funnel ratios are estimates.** They are the argument for the whole change, and they are not
   measured. Claim 11 is how they get measured, and it names the number at which the change should be
   cut instead of shipped.
3. **`|M| ≥ B` is reachable** and degrades the game to mandatory-only. Canon handles it; nobody has
   measured how often it happens.
