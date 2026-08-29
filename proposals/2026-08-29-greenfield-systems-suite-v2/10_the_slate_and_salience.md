# The Slate — Candidates, Truncation, and Headless Resolution

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Version: v3 · Lane: IN (touches SC, SE, WR, FA) · Change **D**
## v3: §1.3 funnel RE-DERIVED after `08` O-6 deleted the draw · §2.1a `informational` · §2.1 transport
## rule · §4.2 an `imminence` producer · §5.1 `engaged(c)`'s `fidelity` field · §6 moved to part 2
## Reads: [`00_INDEX.md`](00_INDEX.md) · [`01_substrate_primitives.md`](01_substrate_primitives.md) ·
## [`01_substrate_primitives_part2.md`](01_substrate_primitives_part2.md) ·
## `audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md` §1–§4 (**RATIFIED**, ED-IN-0011) ·
## `systems/_architecture/player_agency_v30.md` §4 (**CANONICAL** 2026-04-17) ·
## `systems/_architecture/auto_manual_resolution_duality_v1.md` (**RULED** Jordan 2026-07-08, ED-SC-0013) ·
## `systems/_architecture/scale_transitions_v30.md` §4.3–§4.4 · `canon/02_canon_constraints.md` (P-08) ·
## `engine/autoload/scene_slate.py` · `registers/editorial_ledger_sc.jsonl` (ED-SC-0024, ED-SC-0026)
## Continues in: [`10_the_slate_and_salience_part2.md`](10_the_slate_and_salience_part2.md) — §§6–11

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

**Every score term named below is one of the ratified six**, and this document proposes no seventh.
Under the amended authority it *could* — but §0.1 is where that option was exercised and declined, and
a term proposed there would have gone in the `## Overrides` block like anything else.

### 0.1 Read on the merits, and kept — including the two terms I tried hardest to break

Under the amended authority the correct output is not compliance but a verdict. Here is the verdict,
term by term, having read `narrative_engine_design_v2_churn.md` §4 (`:190-285`) line by line.

| ratified term | attacked how | kept? |
|---|---|---|
| **light-inertia** (attention has momentum) | This is the term an earlier draft of the delta spec tried to replace with **novelty** — the *opposite shape*. I re-ran that argument from scratch, because "surface what is new" is the intuitive design and it is worth knowing why it is wrong. **It is wrong because the world produces ~195 candidates a season (§1.3) and almost all of them are new.** A novelty term in a world with that emission rate ranks by *arrival*, which is a random variable, and the result strobes: the player is handed six unrelated first-time situations every season and no thread ever develops. Inertia is what makes a season the continuation of a season. **Kept, and the earlier draft's instinct is now understood rather than merely overruled** | **kept** |
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

⚠ **RE-DERIVED (v3). The v2.0 figures on this line were computed from a formula this document
deletes.** `10 §2.4` rules `08`'s per-place draw *"deleted, not scaled"*, and `08 §5` O-6 has now
executed that. But v2.0's `08` row here read *"v1's `n = 1 + floor(pressure_band)` per place; five
bands, mean band ≈ 1 → ≈ 70–75"* — **the numerator of the headline ratio was the output of the very
quota the change removes.** A headline number resting on a deleted formula is worse than no number,
so it is recomputed below on the emission basis that actually ships, with every basis stated.

Per season, over a world of **37 settlements** (35 in-kingdom + 2 special-case march targets,
`systems/settlements/settlement_layer_v30.md:310`):

**`08`, re-derived per place from `08 §5`'s six qualifying rows** — there is no longer a draw, so the
rate is the expected count of *qualifying items*, not a quota:

| `08 §5` row | basis | items / place / season |
|---|---|---|
| 1 · open `Grudge` on the place or its governor | a stock, not a flow: deduped on `(owner, kind, key)`, appended by Defy (`08 §4.2`), by failed `05` rows and by world events, swept at `ttl` | ≈ **1.5** |
| 2 · unserved `Debt` with a running term | `Debt` is issued only by Commute, which is *gated* and is one of ≤4 responses to one directive per season; term ≈ 3 seasons | ≈ **0.4** |
| 3 · a gauge at or near an extreme band | **13 gauges per place** (`acceptance` ×2, `condition` ×3, `pressure`, `accrual.entitlement`, `presence.<institution>` ×6 — `07 §4.1`'s six institution kinds). **Not uniform over five bands:** `01 §5.1`'s geometric decay concentrates the stationary distribution near `rest`, so p ≈ 0.10 per gauge, and `pressure` qualifies at a lower band (p ≈ 0.20) | ≈ **1.4** |
| 4 · a `Precedent` tested by a new event | needs a *new* event touching an *existing* Precedent: 1 directive/place/season + ≈0.14 world events/place, × ≈0.15 hit rate | ≈ **0.2** |
| 5 · an adjacent settlement at an extreme band | **0 — collapsed into row 3 by `08 §5`'s dedupe rule.** Without that rule this row alone would have multiplied every crisis by the adjacency degree | **0** |
| 6 · an open `investigation_surface` row with a matching unresolved tag | needs an enabling facility/presence **and** an unresolved tag; facilities are tier-gated and sparse | ≈ **0.3** |
| **per place** | | **≈ 3.8** |

| emitter | rate basis | candidates / season |
|---|---|---|
| `08` place business | **the table above × 37 places** (v2.0: ≈70–75, from the deleted quota) | ≈ **135–145** |
| `09` projects | one advance/fire/lapse emission per active project; ~75 project-holding actors (≈30 named NPCs per churn `:76`, plus local actors at `settlement_layer_v30 §4.5`'s ruled per-type counts), ~⅓ emitting | ≈ 25 |
| `05`/`06` faction activity | 4–8 factions (count unreconciled, churn `:107`) × declared actions across tiers. **Unchanged in kind by `08` O-5:** the eight up-stroke rows move here as `tiers: [settlement]` rows, but they were already counted as `08` substrate output and are not double-counted | ≈ 20 |
| `11` world events | rate-bounded by `11`'s own declared ceiling | ≤ 5 |
| `01 §2` form transitions | places and people crossing gated bands | ≈ 3 |
| `04` vacancies / appointments | posts falling vacant, terms expiring | ≈ 5 |
| **total** | | **≈ 190–200** |

| ratio | v3 value | v2.0 value |
|---|---|---|
| candidates : Slate entries (Normal, B = 6) | **≈ 33 : 1** | ≈ 21 : 1 |
| candidates : scene actions (Normal, A = 4) | **≈ 49 : 1** | ≈ 32 : 1 |
| over a 50-season campaign (`engine/tests/test_mc_v18_regression.py:16` runs 50-season campaigns) | ≈ **9,750 candidates resolve** · ≈ **300 surface** · ≈ **200 are played** | ≈ 6,400 · 300 · 200 |
| **fraction of what happens that the player ever sees** | **≈ 3.1%** | ≈ 4.7% |
| **fraction the player acts on** | **≈ 2.1%** | ≈ 3.1% |
| **fraction that resolves** | **100%** | 100% |

### 1.3a What the re-derivation actually showed, including the part that is against this document

**The number went UP and its evidential quality went DOWN. Both halves matter.**

1. **The ratio improved, and that is the self-serving direction, so it needs a control.** D deletes
   `08`'s quota; deleting the quota roughly doubles `08`'s emission; `08`'s emission is the largest
   term in the numerator of the ratio D cites as its own justification. **A change that inflates its
   own headline metric has to be judged on the metric it would have had without the change.** That
   control is v2.0's own column: at the *pre-deletion* rate the ratio is **≈ 21 : 1**, still seven
   times claim 11's cut threshold. **D's case does not depend on the deletion**, which is the only
   reason the deletion is allowed to improve the number.
2. **The basis got weaker even as the number got larger.** The v2.0 figure rested on **one** stated
   basis — a formula and a band mean, both auditable in one line. The v3 figure rests on **six
   independent shape assumptions**, and rows 1 and 3 alone carry **≈ 76%** of the per-place mass.
   **Neither is bounded by any document in this suite**: no document caps open `Grudge`s per place,
   and the p ≈ 0.10 stationary-band estimate is asserted from the shape of `01 §5.1`'s decay law
   rather than computed from declared `λ` and `rest` values, which `07` has not published. **This is
   a genuinely less trustworthy number than the one it replaces, and it is published as such.**
3. **A second falsifier direction opened that claim 11 did not have.** Under the quota the only risk
   was the rate being too *low* (D not earning its keep). Without the quota there is a risk in the
   other direction: if row 1 or row 3 is materially unbounded, the **Shade** grows without limit —
   and every shaded candidate still resolves at full fidelity (`§6`), which is what the *"fraction
   that resolves: 100%"* row commits to. That cost lands on the **simulation's per-season work**, not
   on the Slate, and nothing in this document would show it. Claim 11 is amended to measure both
   directions.

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

> **The transport is the boundary return, and it is the only one.** A candidate is **never** a Key.
> `sl.candidates` declares `consumes: []` *"because emitters return at the boundary, not by
> subscription"* (part 2 §10, §8), and `00 §9.2` registers **no** candidate-carrying key type. v2.0's
> `08` contract emitted `place.business_item_offered`, a type `00 §9.2` does not register and this
> document does not consume — **two answers to one seam, and this sentence is the single one.** `08`
> §8 has been corrected to `emits: []`. **No key type is minted for a candidate, so nothing about the
> candidate contract is blocked on P0-1.**

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
  informational:  <bool>                 # §2.1a; default false. True ⇒ news, not a situation:
                                         # exempt from C-4 and C-5, rendered and never resolved
  resolver_ref:   <module id | null>     # the ONE module that resolves this, at either fidelity.
                                         # null IFF informational
  responses:      [<3..5 response ids from resolver_ref's declared option set>]   # [] IFF informational
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
| **C-4** | **`resolver_ref` names a module that already exists in `module_contracts.yaml` and resolves this candidate at *both* fidelities.** The Slate never names a "summary" or "auto" module. **Exempt iff `informational` (§2.1a).** | A second cheaper resolution path — the Total War seam ED-SC-0024 records the community finding and exploiting |
| **C-5** | **`responses` is 3–5 ids drawn from `resolver_ref`'s declared option set, filtered by the player's `remit`.** The candidate does not invent responses. **Exempt iff `informational` (§2.1a).** | Verb creep. `00 §2.2` caps responses at 3–5 *"genuinely different in kind"*; a candidate that could mint its own would route around the cap |
| **C-6** | **An emitter emits; it never presents, ranks, or checks the budget.** It does not know `B`, does not know what else was emitted, and cannot see the Slate. | The reason this is one function and not eight competing ones. v1's `sm.business` drew `1 + floor(pressure_band)` items *and presented them* — a per-place budget with no global view, which is how a 37-place world manufactures 75 undifferentiated demands |

### 2.1a `informational` — the world's own news, which the contract otherwise excluded

**The contract as written could not carry a crossing fact, and `§2.4` lists an emitter of exactly
those.** C-4 requires `resolver_ref` to name a module that resolves the candidate at both fidelities;
C-5 requires 3–5 responses from that module's option set. **`substrate.form` emits *"form transitions,
as crossing facts"* — a village grew, a bloc formed, a presence crossed a band — and a crossing fact
has no resolver and no response set**, because it has already happened and there is nothing to decide
about it. So either that emitter could construct no legal candidate and the player is never told the
village grew, or the contract is violated on every one of its ≈3 emissions a season. Neither is
acceptable, and the second is worse because it would be silent.

**The fix is one boolean.** `informational: true` marks a candidate as *news*:

| | informational candidate |
|---|---|
| **C-1 provenance** · **C-2 witness** | **bind exactly as before.** News still has a cause and still must be knowable. These are the two rules that make the Slate trustworthy and neither is relaxed |
| **C-3 realized-terms-only** | binds. A crossing fact is the *most* realized thing the Slate carries |
| **C-4 `resolver_ref`** | **exempt.** `resolver_ref: null`. There is no resolution and no fidelity, so no second cheap path can hide here |
| **C-5 `responses`** | **exempt.** `responses: []` |
| **C-6 emitter never ranks** | binds |
| costs a **Slate seat** (`B`)? | **yes** — it is one of the things the season is about, and it competes for the seat on `cast_score` like everything else |
| costs a **scene action** (`A`)? | **no.** There is nothing to attend. It is read, and reading is free (§9) |
| can ever be `engaged`? | **no** — no scene action can be spent on it, so it can never enter the exempt set `E`. Stated because §5.3's proof reads that set |
| can be `mandatory`? | **yes**, and three of the five world-state triggers in `scale_transitions_v30 §4.3.3` are exactly this shape |

**The crowding risk is real and is bounded by a constant, not by hope.** Nothing above stops a season
of quiet news from filling the Slate with items the player cannot act on. `INFO_CAP ⟨shape: 2⟩` caps
informational members of the Slate. It is a **count cap on a disjoint subset, never a score
threshold** — the same discipline §5.3 shows is load-bearing — so it is score-independent and the
monotonicity proof still goes through (§5.3 checks it explicitly).

*Emergent possibility lost if the boolean were not added:* the player would learn nothing about the
world except through things they can act on, which is precisely a world with no outside — the failure
`08 §3` refuses one document earlier.

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
| `sm.business` | `08` | place business from tags and gauge bands | **Its per-place `1 + floor(pressure_band)` draw is deleted, not scaled.** It emits *all* qualifying items; the global budget does the cutting. This is `08`'s single largest simplification. **Executed in `08 §5` O-6, and §1.3's numerator re-derived on the new basis** — v2.0's ≈70–75 was computed from this very formula |
| `am.advance` / `am.fire` / `am.lapse` | `09` | project beats | J-N: these fire because the world *is* a certain way at the boundary (§8) |
| `we.fire` | `11` | conditioned exogenous events | Routes **through** the Slate, never around it — Part VI's second surfacing path prohibition |
| `fa.*` | `05`/`06` | faction directives, bloc friction, divergence crossings | mostly NPC-invoked; what reaches the player is a candidate |
| `pm.vacancy` / `pm.tenure` | `04` | vacancies, terms expiring, contested appointments | |
| `substrate.form` | `01 §2` | form transitions, as **crossing facts** | Part VI: `threshold_crossed` carries crossing facts, never forecasts. **These are `informational: true` by construction (§2.1a)** — a crossing fact has no resolver and no response set, and before v3 the contract could not carry one |
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

⚠ **`imminence` had no producer, and without one the term is vacuous over this suite's candidates.**
`09 §3` point 3 forbids a project publishing how close it is to firing (*"a project may never publish
how close it is to firing"*, Part VI, adopted without reservation); `11 §3` sets `world.event_fired`'s
`horizon` to `{band: 0, foreclosure_in: null}` because a fired event is realized; and nothing anywhere
computes a Layer-A horizon. So **every candidate this suite emits arrives with a null or zero
horizon**, `imminence(c.horizon.band)` is constant, and `depth_score` collapses to `cast_score ×
forecast_mass`. The ratified design's own motivating case — *"a quiet arc about to foreclose should
foreground **before** it fires"* — cannot happen.

**The smallest fix, and it is deliberately not a re-weighting: `sl.rank` DERIVES a coarse horizon
band.** The emitter still publishes nothing about proximity, which is what `09` and Part VI actually
forbid. `sl.rank` reads what `01 §8` already publishes as an **input** — the candidate's advance terms
and its subject gauges' **bands** — and derives `horizon.band` as a monotone function of *band
distance* to the nearest gate the candidate's own kind declares. **Three properties make this legal
where a published forecast would not be:**

1. **The threshold stays hidden.** Band distance is computed from published bands; the *trigger* — the
   numeric threshold — is never read and never shown (`01 §8`, `09 §3` point 2).
2. **It cannot reach `cast_score`.** `horizon` enters only `depth_score`, and §4.2's severance means
   `depth_score` **cannot change membership**. So the rubber-banding loop the churn doc `:274` severs
   stays severed *by the same construction*, not by a new promise.
3. **No emitter changed.** This is a derivation the Slate performs on candidates it already holds —
   C-3 is untouched, because the emitter still supplies no projected term.

**What this does not do:** it does not re-weight the Light Function, add a seventh term, or give
`forecast_mass` a producer. `forecast_mass` remains **unproduced** and is named in part 2 §11.5 as
such. This fix makes *one* of the two forecast terms non-vacuous; the honest state is one of two, and
saying "the forecast terms now work" would be false.

⚠ **And it is partial even for `imminence`, which is this fix's weakest point.** Band-distance is only
defined for a candidate whose **kind declares a gate to be distant from** — a project with a
`threshold`, a form transition with a band edge, a gauge approaching a declared band. A candidate
emitted from an open `Grudge` or an unserved `Debt` (`08 §5` rows 1–2, together ≈50% of the largest
emitter's output, §1.3) declares no gate, so its `horizon.band` stays 0 and its render depth is
unchanged. **So `imminence` goes from vacuous over *all* candidates to meaningful over *some*, and the
fraction is not measured.** That is a real improvement over a term with no producer at all, and it is
not the same thing as the term working. Claim 15's first assertion is deliberately *"non-constant"*
rather than *"populated"* for exactly this reason.

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
        I = informational cap ⟨shape: 2⟩   # §2.1a; a COUNT cap on a disjoint subset, never a threshold

1. M  := { c ∈ C : c.mandatory }                                     # §5.4, enumerated
   if |M| ≥ B:  Slate := M ;  goto 6                                 # mandatory-only; canon :314
2. E  := top-X of { c ∈ C∖M : engaged(c) } by cast_score             # demotion-exempt, but CAPPED
3. k  := max(0, B − |M| − |E| − R)                                   # free slots — score-independent
   F  := top-k of { c ∈ C∖(M∪E) } by cast_score,
              admitting at most I members with informational = true      # §2.1a
4. P  := top-R of { c ∈ C∖(M∪E∪F) : never_lit(c) } by cast_score     # the reserved slice
5. Slate := M ∪ E ∪ F ∪ P
6. Shade := C ∖ Slate                                                # → §6, headless, all of it
```

**Comparator:** `(cast_score DESC, candidate_id ASC)`. The tie-break on a deterministic hash makes the
order **total**, which is what §5.3 needs and what a score-only comparator does not give.

`engaged(c)` = the player spent a scene action on `c` in a prior season and it has not terminated —
the ratified demotion-exemption for player-pursued threads (`:222`). `never_lit(c)` = no
`slate.item_surfaced` Key exists for `candidate_id` (§7).

⚠ **`engaged(c)` read state nothing wrote, and §5.3's monotonicity proof leans on it. Fixed here.**
Candidates are derived and never stored (§2.3); `slate.item_surfaced`'s registered payload is
*"candidate id, salience components, rank, whether mandatory"* (`00 §9.2`) and carries **no attendance
or fidelity**; and no key type in `00 §9.2` records a scene-action spend. So next season's Step 2 had
**no data source**, `|E|` was undefined rather than merely uncomputed, and a proof whose second bullet
is *"engagement is a fact about past seasons"* rested on a fact nothing recorded.

**Fix: one field.** `slate.item_surfaced` gains `fidelity: played | witnessed | auto` — the label §5.5
already computes and already names. Then `engaged(c)` ⟺ a `slate.item_surfaced` exists for this
`candidate_id` with `fidelity = played` and `c` has not terminated; `never_lit(c)` is unchanged.

**One sequencing consequence, or the field records nothing.** The label is final only once attendance
is settled, so `slate.item_surfaced` is emitted at the **close** of the boundary, not at truncation.
That costs nothing: §6.2 establishes the Slate does not dispatch — the Key is a **log entry** and
nothing downstream waits on it — and §7 reads the same log for inertia either way.

⚠ **This is a Key-type change and `00 §8` P0-1 blocks it.** `slate.item_surfaced` was *already* on the
blocked list (part 2 §10), so this adds a field to work already blocked rather than a new blocker.
**Until P0-1 clears, `engaged(c)` is unimplementable and Step 2 is `E := ∅`** — a degraded Slate, not
a broken one: `X` is a cap, so `|E| = 0` returns those seats to `F`, and every proof in §5.2–§5.3
holds at `|E| = 0`. Stated so the blocked state is a known configuration rather than a hole.

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
**well over an order of magnitude** larger than `B` (§1.3: ≈33 : 1 — *not* the "two orders" v2.0
claimed here, which was loose even on its own smaller numerator). **That is a real simplification the truncation buys: a global
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
- `I` is a constant capping a **disjoint subset** of `F` chosen by a boolean field, not a score.
  Score-independent ✔ — same trap as `X`, same answer. A rule of the form *"admit informational items
  only above score `t`"* would move `|F|`'s composition with the scores and break the proof.
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
`candidate_id`, the score components, rank, whether mandatory, and — **added in v3, §5.1** — the
**`fidelity`** label, emitted at the close of the boundary once attendance is settled. That label is
written onto each candidate in the boundary's derived candidate set:

| label | who gets it | what it means |
|---|---|---|
| `played` | Slate members the player spends a scene action on | interactive; the player supplies the decisions. **The only writer of `engaged(c)`** (§5.1) |
| `witnessed` | mandatory overflow | present, one roll, no direction |
| `auto` | everything else — Slate members not attended, **and the whole Shade** | headless; NPC-AI supplies the decisions |
| *(none)* | an `informational` Slate member (§2.1a) | nothing resolves it; it is rendered and it ends. Logged as `auto` for uniformity; no resolver is invoked |

**The Slate does not resolve anything.** The label is a datum; the candidate's own `resolver_ref`
module, invoked by **its own subsystem's herald** (`01 part 2 §9.1`), does the resolving. See §6.2 —
this is the design's defence against Part VI's distributor prohibition and it is structural, not
rhetorical.

---

**Continues in [`10_the_slate_and_salience_part2.md`](10_the_slate_and_salience_part2.md)** — §6 headless
resolution and its three invariance properties · §7 light-inertia without storage and **J-N** · §8 **J-O** ·
§9 the player surface · §10 module contracts · §11 the property audit.

> **§6 moved to part 2 in v3, keeping its number.** Part 1 grew past the ~14k-token split threshold
> (`CLAUDE.md §4`, `references/atomization_rules.yaml`) when §1.3 was re-derived and §2.1a added.
> **Every `10 §6.x` citation in the suite still resolves** — the section number, its subsection
> numbers and its text are unchanged; only which of the two part-files holds it moved.
