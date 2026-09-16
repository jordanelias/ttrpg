<!-- STATUS: PROPOSED — held back in full. Analysis, not a decision. -->
<!-- AUTHORITY: none claimed. Rules nothing, supersedes nothing. -->

# Formal analysis — what the findings jointly establish about computing behaviour

## Status: PROPOSED — HELD BACK

**§0.05 class: REFERENCE.** Companion to `behaviour_census.md` (diagnosis) and
`behaviour_algorithms.md` (proposals B and C; proposal A scrapped by Jordan, *"Lexicographic is
stupid"*).

---

## §1 Method and evidential status

Three classes of evidence, kept separate because they fail differently.

| class | how obtained | who can reproduce it |
|---|---|---|
| **E — executed** | ran the season loop or the closed form | this session only; **neither critic has an execution tool** |
| **R — read** | opened the file at the line | both critics; independently re-verified where noted |
| **D — derived** | follows from E and R by argument | anyone, from the premises |

⚠ **Every executed number in this session's documents rests on one instrument and one operator.**
One of them — §8.3's tie-break claim — has already been found to measure the wrong stage
(`sorted()` rather than `choose()`), **by both critics independently**, and was then confirmed
wrong by execution. Treat class E as the weakest class here, not the strongest.

---

## §2 The established facts, stratified

The findings are not a list. They stratify into four layers, and the layer decides what the finding
can possibly block.

### 2.1 Carrier layer — what can be represented at all

| | fact | class |
|---|---|---|
| **C1** | `Claim` fields are `id · holder · subject · predicate · value · when · source · confidence · visibility · round`. **No teller.** `source` is a channel kind, not an identity; `witness.py:358` has `_teller` in scope and discards it. | R |
| **C2** | `utter` is untyped, so every person-formed `Proposition` is `mood="OUGHT"`, `predicate=""`, `value=None` (`loop/effects.py:430`). Nothing in the decision path reads `predicate` or `value`. | R |
| **C3** | `Person` has no `scar`, no `needs`, no `orient`, no fear field. `matrix_rows_without_a_field()['absent']` lists `(Person, scar)`, `(Person, axis_count)`, `(Person, coherence)`. | E+R |
| **C4** | `Person.marks` is read by **no Python** in the tree; `Person.capability` is read once, as a dice source, where the fixture states *"Rank supplies dice and gates nothing."* | R |
| **C5** | `Person.stance` exists and holds **0 rows across 12 persons** in a built realm. | E |
| **C6** | `View` exposes `holder`, `claim_ids`, `question`; every other attribute raises `Forbidden`. | R |

### 2.2 Gate layer — what can be formed

| | fact | class |
|---|---|---|
| **G1** | `person_side_eligible` declines on `remit:`, `presence:` and `hold:<placeholder>`. **10 of 38 verbs are unformable person-side** — the eight remit acts, `levy`, `destroy_record`. | R+E |
| **G2** | `eligibility_kinds` is closed at four; its note: *"`capability` IS NOT AND MUST NEVER BE A MEMBER… Adding a fifth kind is a DESIGN CHANGE… not a table edit."* | R |
| **G3** | `opening_set` scopes candidates to `q.referents`; the aperture is ~25 candidates per referent and **28 distinct verbs under every aggregation rule**. | E |

### 2.3 Flow layer — what can move

| | fact | class |
|---|---|---|
| **F1** | `aggregate_questions` under `one_per_source`/`all` **re-mints** a Question carrying only `qs[0].source`, `qs[0].about` and a flattened referent union. | R |
| **F2** | Six loop steps. MATTER, CALENDAR, CENSUS and WITNESS each carry a refusal law against a Person social write; DELIBERATE *"returns an act array and writes nothing else."* **Only RESOLVE remains, i.e. only an act — and H-62: no verb writes any Person interior field.** | R |
| **F3** | `choose.py:318` runs `_sample_order` **after** the score sort. At the shipped `choice_temperature = 0.1` it re-ranks by `−(score/τ + g)`, `g ~ Gumbel(0,1)`. | R+E |
| **F4** | `_load_projection` and `_load_alignment` raise at **module scope** on a roster mismatch or an all-zero table. | R |

### 2.4 Measured behaviour

| | fact | class |
|---|---|---|
| **M1** | Q4 `need` — the ambition source — leads for **12/12 persons at genesis and 0/12 in every season after**; reactive traffic reaches 136–180 questions while `need` stays at 12. | E |
| **M2** | Ambition's referent reaches deliberation **0/12** under `first`, **12/12** under `one_per_source`. | E |
| **M3** | 580 claims after two seasons, **100% `firsthand`**. `tell` **resolved 9 times and deposited 0** claims. | E |
| **M4** | `standing_of` returns **1000 — the maximum-gap default — for all 12 persons**, permanently, because its `told_by` input is empty. | E |
| **M5** | Score plateau of 2.2 candidates, first-to-second gap **exactly 0.0000** for 12/12. The sampler then changes the top choice for **9/12**. | E |

---

## §3 Results

### R1 — The representability bound

*A ranking function cannot discriminate on an input that is not represented.*

Of Jordan's twelve, by §2.1: **2 (needs), 3 (fears) and 8 (self vs public) have no carrier at all**;
**9, 11 and 12 have a field with no data and no reader** (C4, C5); **1 and 10 have a carrier whose
content is empty or unformable** (C2, G1); **4 and 5 share one field**, as do **6 and 7**.

> **R1.** At most **two** of the twelve can produce a difference between two candidates today:
> convictions (items 6+7, collapsed, via `fit`), and memory/epistemic (items 4+5, collapsed, via
> `opening_set`'s belief filter). Both are pairs of Jordan's items sharing one field.

**Corollary R1.1 — the choice between B and C is underdetermined by the twelve-item requirement.**
Neither can be preferred on the grounds of serving the inputs better, because the inputs that would
distinguish them are not representable. *The design question this session has been answering is not
a question the evidence can decide.*

### R2 — Extensional collapse

*Two programs are extensionally equal if they produce the same output on every input.*

**B** ranks by `pressure(item(c)) × g(fit(c))`. By C2 no candidate can be attributed to an ambition
(the Proposition has no content to match against); by G1 no candidate can be a remit act; by C3
there is no store for `pressure`. The attribution map is therefore constant, and
`score = k · g(fit)` for constant `k`. **B ≡ the incumbent's first term.**

**C** contests the top two of {duty, ambition, fear, conviction, regard}. `duty` is null by G1;
`ambition` is null by C2; `fear` has no carrier; `regard` is identically 0 by C5. **One non-null
nominator remains, so the fork predicate (`kind(k1) ≠ kind(k2)`) can never fire. C ≡ argmax over
conviction ≡ the incumbent's first term.**

> **R2.** Executed against the tree as it stands, **B and C are both extensionally equal to the
> current engine, and to each other.** Neither is wrong; both are unreachable.

**R2's C half was executed rather than left derived**, because a derived impossibility is the
cheapest claim to make and the hardest to see wrong (§0.1 pt 3). Counting C's five nominators over
twelve deliberating persons at tick 2:

| non-null nominators | persons |
|---:|---:|
| 1 | **12** |
| ≥2 (a fork is possible) | **0** |

C's fork predicate requires two non-null nominators **of different operator kinds**. It cannot fire
once, for anybody, in this world. The surviving nominator is `conviction` in every case.

### R3 — The noise floor, exactly

Two candidates with scores `s₁ > s₂` invert under `_sample_order` iff `g₂ − g₁ > Δ/τ`, where
`Δ = s₁ − s₂`. The difference of two independent standard Gumbels is standard Logistic, so:

> **R3.**  **P(inversion) = 1 / (1 + e^{Δ/τ})**

Verified against 200,000 simulated draws per row, agreeing to four decimal places:

| Δ | Δ/τ at τ=0.1 | P(inversion), closed | simulated |
|---:|---:|---:|---:|
| 0.000 | 0.0 | 0.5000 | 0.5000 |
| 0.050 | 0.5 | 0.3775 | 0.3782 |
| 0.128 | 1.28 | 0.2176 | 0.2175 |
| 0.200 | 2.0 | 0.1192 | 0.1190 |
| 0.294 | 2.94 | 0.0502 | 0.0506 |
| 0.500 | 5.0 | 0.0067 | 0.0069 |

**Design rule, derived:** a term is decisive at fidelity `p` iff `Δ ≥ τ·ln(p/(1−p))`. At the shipped
`τ = 0.1`: **Δ ≥ 0.294 for 95%, Δ ≥ 0.460 for 99%.**

**Corollary R3.1.** The measured live plateau gap is **0.0000**, i.e. exactly the `P = 0.5` row.
Within the plateau the engine is a coin. **Corollary R3.2.** Neither B nor C states the range of
any of its terms, so neither can be shown to clear 0.294. **Corollary R3.3.** B's ratchet is
self-defeating in both directions: low pressure sits below the floor and is noise; unbounded
pressure drives `Δ/τ → ∞` and **destroys** the sampled non-rationality the requirements record as
built.

### R4 — Write-step exclusion collapses five problems into one

By F2, any mechanism persisting per-person state across seasons must write a Person field at
RESOLVE, via an act; and no act does.

> **R4.** B's `pressure`, C's `scar`, the needs counter, the fear item and the production of
> `stance` rows are **not five problems. They are one** — the absence of a Person-interior write
> path — and one ruling unblocks all five.

### R5 — Aggregation collapse

By F1, the aggregator discards every field but `source`, `about` and the referent union.

> **R5.** The cost of §8's carrier expansion is not one rewrite; it is **one fold rule per field**
> (how do two `kind`s merge? two horizons? two witness sets?), each a design decision. Per-referent
> roles are the worst case: a role tuple cannot survive a sorted-set union.

### R6 — Migration atomicity

By F4 the refusals are at module scope.

> **R6.** There is no state in which the engine runs with a partially-populated new axis set.
> Adopting a seven-axis basis is **atomic**: a 13×7 projection and a 7×38 alignment table must both
> exist before first import. There is no graceful-degradation path and no incremental migration.

### R7 — Projection non-separability (why axis 1 cannot be an axis)

Axis values are reachable only through
`conviction[a] = Σ_c w_c · P[c][a]` — a **linear map** `L : ℝ¹³ → ℝᵏ` from the conviction vector.

Any axis value is therefore a linear functional of `w`. Two persons with identical `w` have
identical images under any linear map, hence identical values on **every** axis, necessarily.

`conviction_taxonomy_v30.md` §2.3 requires precisely the opposite for self/other: Cesare Borgia and
a public-spirited magistrate *"may share a high Utility Conviction; what distinguishes them is for
whom they instrumentalize"* — *"different gameplay even with identical Conviction vectors."*

> **R7.** **Selfish ↔ Selfless is not representable as an axis in this architecture.** Not
> redundant with `orient.self_other` — *unsatisfiable*, by linearity. It requires an input to the
> decision that is not a function of the conviction vector.

---

## §4 Verdict

**On B and C:** neither is refuted and neither is reachable. R2 makes them presently
indistinguishable from the incumbent and from each other; R1 makes the requirement that would
choose between them unrepresentable; R3 makes both unfalsifiable as stated, since neither declares
a term range and the sampler inverts anything below Δ = 0.294.

**On the session's method:** every finding above sits in the **carrier, gate, flow or step** layers.
**Not one is about ranking.** The proposals answer a question — *what function ranks the
candidates?* — that no evidence in this session bears on. That is the analysis's principal result
and it is a result about the work, not about the tree.

**On the axes:** R6 and R7 together say the axis question is not a data edit and is not fully
satisfiable as posed. R7 disqualifies the first of the seven on structural grounds; R6 prices the
rest at two full authored tables before anything runs.

---

## §5 The order that follows

A topological sort of the dependency graph above. Each item unblocks those below it; none can be
usefully attempted before its predecessors.

| | do | unblocks | cost |
|---|---|---|---|
| **1** | `q_rule = one_per_source` | M2: ambition reaches deliberation at all | one word |
| **2** | **H-71** — a person can read their own remit (arm 2: the grant rides on the `hold` Tenure) | G1: 10 verbs, hence duty, office, and every mediated fear | already specified, three arms |
| **3** | A **Person-interior write path** — one ruling | R4: pressure, scar, needs, fear, stance — five mechanisms | a ruling, then a verb |
| **4** | An **operand on `utter`** so a Proposition can say what is wanted | C2: ambitions acquire content; B's attribution and C's nominator become possible | carrier + verb row |
| **5** | **`Claim.teller`**, or grade at deposit | C1: Jordan's relationship-weighted testimony | one field, or none with a cost (below) |
| **6** | **Fold rules** for each new Question field | R5: §8's expansion survives Φ1 | one decision per field |
| **7** | Declare **term ranges** against R3's floor | R3: makes any proposal falsifiable | measurement, not design |
| **8** | *Then* B vs C becomes decidable | — | — |

**On item 5, the fork Jordan has already half-ruled.** He ruled *hearer's belief about the
relation* over objective relation. Grading at deposit needs no new field but **freezes the relation
at the moment of telling** — learn later that your "lord" was a fraud and his claims keep their
inflated confidence. Storing the teller permits re-grading. A belief that cannot be revised is not
a belief, so the ruling implies the field; that implication is stated here and not taken.

---

## §6 What this analysis does not establish

- **R2 is a claim about today's tree, not about the proposals' merit.** B and C may both be good
  designs for a tree that can carry them. Nothing above says which.
- **Class E is single-operator.** Neither critic could reproduce any executed number. M1–M5 and R3's
  simulation rest on this session alone, and one earlier E-class claim was already wrong.
- **R7 assumes the projection stays linear.** A non-linear or multi-input projection would evade it.
  That is a design option, not a refutation.
- **The fear model is unverified in either direction.** `fear|fears` matches one file in all of
  `engine/` — a case fixture. There is nothing to test against.
- **No NERS pass has been run** on any of this, and `engine/season/requirements.yaml` — the declared
  instrument for whether this tree is a game — has not been consulted about any proposal.
