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
## Continues in: [`10_the_slate_and_salience_part2.md`](10_the_slate_and_salience_part2.md) — §§7–11

---

## 0. THIS DOCUMENT DOES NOT DESIGN A SALIENCE FUNCTION — a decision, not a prohibition

⚠ **Authority note (2026-08-29, Jordan-directed, mid-flight).** The instruction under which this
document began said the Light Function is ratified and may not be replaced. **That instruction was
withdrawn while this was being written:** *"existing work is not necessarily required to keep all the
way through to things like obstacles being stat/2 or whatever is ratified and canon"* … *"I just want
the best possible proposal."* Nothing in the tree is out of bounds, including this.

**So the sentence below is a judgement made on the merits, with the ratified text read line by line
first, and it is defended in §0.1 rather than asserted.**

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

### 0.1 Read on the merits, and kept — including the two terms I tried hardest to break

Under the amended authority the correct output is not compliance but a verdict. Here is the verdict,
term by term, having read `narrative_engine_design_v2_churn.md` §4 (`:190-285`) line by line.

| ratified term | attacked how | kept? |
|---|---|---|
| **light-inertia** (attention has momentum) | This is the term an earlier draft of the delta spec tried to replace with **novelty** — the *opposite shape*. I re-ran that argument from scratch, because "surface what is new" is the intuitive design and it is worth knowing why it is wrong. **It is wrong because the world produces ~125 candidates a season (§1.3) and almost all of them are new.** A novelty term in a world with that emission rate ranks by *arrival*, which is a random variable, and the result strobes: the player is handed six unrelated first-time situations every season and no thread ever develops. Inertia is what makes a season the continuation of a season. **Kept, and the earlier draft's instinct is now understood rather than merely overruled** | **kept** |
| **casting severed from forecast** | The tempting simplification is one score. I traced what one score does: forecast → surface → player acts → forecast strengthens. That is the rubber-banding loop at `:274`, and it is *invisible in play* — the game would feel prescient rather than broken. **A term I would not have thought to sever, and could not have discovered by reasoning about my own design.** Kept, and it is what turns one score into two (§4) | **kept** |
| **exempt-cap + reserved promotion slice** | The obvious design is "player-engaged threads are exempt from demotion", full stop, and it is what I would have written. The ratified text caps it *and* reserves a slice, because uncapped exemption lets a player engaging `B`-many threads starve imminence permanently. **It is also what makes §5.3's monotonicity proof go through** — a cap is score-independent where a threshold is not. Two independent reasons, neither of which I had | **kept** |
| **anti-strobe floor** | This is P-iii hysteresis under another name, and `01 §2.3` requires the same shape of every reversible form transition. Consistent with the suite by construction | **kept** |
| **integer basis points** | The ordering crosses the Python↔GDScript port. Float accumulation order differs. Non-negotiable | **kept** |
| **meaningfulness = durability × tie-proximity × identity-touch** | The only term I would still like evidence for is the **product** form: a candidate with zero identity-touch scores zero however durable and close it is. That is probably right (a thing that touches nobody's identity is not a story) but it is asserted, not shown. **Recorded as a live question, not proposed as an override** — the weight set is exposed data (`:279`), so if the product form is wrong it is tunable to near-additive without re-ratification | **kept, with one question** |

**One reconciliation, which is not an override but should not pass silently.** The ratified text
describes inertia as a *"persistent priority term whose carryover decays"* — a carried value. `01 part
2 §9.3` establishes, verified against the tree, that **the substrate has no mechanism to carry
anything across a season.** Two true statements that cannot both be implemented as written. §7 resolves
them by computing the identical arithmetic as a **derivation over the append-only Key log**: same decay
law, same floor, same integer discipline, nothing stored and nothing carried. **The ratified property is
preserved exactly; only its implementation is relocated from a carried field to a derived read.**

**What I did not do, and would flag if I had:** propose a replacement term, add a second scoring
function beside the ratified one, or reweight the ratified constants. Two mechanisms doing one job is
the elegance failure `00 §1` names, whoever wrote either.

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
| **O-10.5** | **The Light Function itself** (`narrative_engine_design_v2_churn.md` §4, ED-IN-0011) | **(2) ratified canon — CONSIDERED FOR OVERRIDE AND DECLINED** | Recorded here rather than left silent, because under the 2026-08-29 authority amendment *not* overriding is now also a decision that needs an argument. **§0.1 is that argument, term by term.** Verdict: adopted entire, unreweighted, with no term added and no second scoring function beside it. The one term carrying an open question — the *product* form of meaningfulness — is named there and is tunable data, not a structural override |
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
