# Throughlines under composition — branch structure across permutations of systems

## Status: PROPOSED (read-only; nothing executed). Adversarial pass PENDING at time of writing.
## Date: 2026-08-08 · Lane: IN · ED-IN-0148 · Four Fable-5 read-only hub traces, lexical evidence barred

---

## §0 · One live bug, found in reachable code

**The victory Accord gate is mis-scaled by a full canonical band.**

`ACCORD_MAP = {0: 1.0, 1: 2.5, 2: 4.0, 3: 5.5, 4: 7.0}` (`game_state.py:58`) — canonical **2** is continuous
**4.0**. `canon_buckets.canonical_accord` buckets continuous `< 3.25` as canonical **1**. But
`victory.py:28` sets `ACCORD_MIN = 2.0` and compares it against the **continuous** field (`:71`).

**A territory at continuous 2.0–3.24 — canonical 1, "Resistant" — passes the gate that is supposed to
mean "Accord ≥ 2".** `insurgency_pipeline.py:46` encodes the same canonical-2 concept correctly as `4`.
Two gates in the same hub, both meaning "Accord ≥ 2", using 2.0 and 4.0. Victory is easier than designed.

**HELD, not fixed.** Which side is wrong is a design call with balance consequences (raise `ACCORD_MIN`
to 4.0, or was "≥ 2" always meant as continuous?). It is checked every season (`mc_v18.py:267-273`), so
any campaign measurement taken before it is ruled is measuring the wrong game.

**Adjacent landmine, dormant:** `mass_seizure.py:295` writes *canonical ints into the continuous field*,
so a Success (canonical 2) and an Overwhelming (canonical 3) seizure both read back as canonical 1 —
**inverting the design's core seizure-beats-conquest distinction**. No caller today; it detonates the day
one is added.

---

## §1 · The register is 42 entries, not 30 — and its own counts disagree

`references/throughlines_complete.md` carries **43 `### T-` headers, 42 live** (T-10 struck). It states
**"Count: 30"** at `:298` and **"Count: 41"** at `:375` — two contradictory totals in one file, both wrong.
Sibling files add two more inconsistent counts: **four mutually inconsistent counts across three documents
that cite each other.**

Consequence: the naive pair space is **C(42,2) = 861**, not 435. The hand-authored interaction matrix
covers **20 pairs — 2.3%.**

*Orchestrator's own correction, recorded because it is the session's recurring failure mode:* the first
computation printed 43 entries and 861 pairs; the orchestrator overrode its own instrument with the
document's stale self-count of 30. **Trusting prose over a measurement already taken** is precisely the
defect this audit keeps finding in the tree.

---

## §2 · "Throughline" is six concepts sharing one register

Each type composes by a different rule, so a single pairwise matrix is a category error:

| Type | n | Composition rule |
|---|---|---|
| **Axioms** (T-01 "Everything Is Thread"; Systems field literally `ALL`) | 7 | **Conjunction.** No state to change; constrains everything at once. Axiom × X is a compliance check, never a cell. |
| **Clocks** (T-04/05/06/07/25) | 5 | **Shared-variable coupling** — the only type matching the register's own definition. Already written as arithmetic, therefore computable. |
| **Postures** (institutional policies over shared state) | 8 | **Mediated only.** Posture × Posture has *no direct cell*; they interact through the variables they read and write. |
| **Personal state machines** | 13 | Shared character-sheet fields; relational edges; cross-scale aggregation. |
| **Geographic projections** (T-18/19) | 2 | **Operators, not occupants** — they parameterize every clock (*where* pressure lands). |
| **Second-order structures** (T-20/24/26/27/30…) | 7 | **No cell semantics.** They describe how first-order machinery is perceived or combined. |

**T-24 "Convergence as Emergent Crisis" is ruled a type error.** It quantifies over other throughlines and
owns no state, so by the register's own definition (`:4`) it fails entry-hood. **It is the composition
operator, mis-filed as an entry in the list it operates on.** Its convergence markers are instances — i.e.
authored cells — not a row.

**Type-admissible pairs: 297 of 861.** Realized (shared declared state): estimated **~90, about 10%** —
**explicitly not banked**; it is exactly the number §5's fix would replace with a measurement.

**The tooling already ruled on this, in July.** `vector_audit.py:1067-1069` records that the interaction
matrix **was measured and REJECTED**: *"20/21 throughline pairs 'interact', a near-complete graph that
would just inflate the Clocks/MS hubs with no discrimination."* The right object is the **bipartite
throughlines × state-variables graph**; the pair matrix is its lossy one-mode projection.

**Collapses found** (each shrinks the real space): T-19 = T-04 ∘ T-06 ∘ T-20 localized to a place;
T-26/T-32 fold into T-08+T-27; T-40 ⊂ T-33; T-17 ⊂ T-14 × T-16; the Solmund appendix duplicates T-27,
T-29 (*by name*) and T-26. T-23 shares T-14's spine **but appends a return edge** (`→ Domain Echo →
political landscape shift → new arc triggers`) — that is T-14-plus-loop-closure, and the loop closure is
the valuable part. Net ≈ **34 independent entries.**

---

## §3 · How the branches actually collapse — three hubs, three different reasons

### MS / rendering — collapse by construction
**The substrate branch space is one-dimensional.** Any combination of drains and restores reduces within a
season to one net delta, clamped ±10. Real multiplication lives only in *side-state*: hysteresis flags, the
one-shot Surge, permanent expedition streams — all unbuilt.

**The radiation matrix is ~85% false richness.** Nominally 6 bands × 6 distances × 4 settlement types ≈
144 cells; actually a **shifted diagonal** (severity ≈ band − distance) yielding **~11 distinct mechanical
states**, of which perhaps **4 are distinguishable in play**. Settlement type adds no states — and two live
surfaces contradict each other on whether that axis exists at all (`calamity_radiation_v30.md:22-31` vs
`settlement_layer_v30.md:1156`).

**MS 0 — the most important branch point in the game — has three incompatible rulings**: *"Campaign ends
in catastrophe. No faction wins"* (`threadwork_v30.md:825`) / *"all factions lose"*
(`wc_survival_spine.md:16`) / *"**No shared loss. No fade to black**"* with recovery to 20 in ten seasons
(`peninsular_strain_v30.md:463`).

**The restore arm is unreachable:** `mending_stability_delta` is set in three places and **applied
nowhere**. The world can lose renderability and never regain it above the year-end floor — the
practitioner loop runs half its cycle.

Also falsified: the interaction matrix's own cell *"Practitioner Coherence spent on Mending"* is wrong
post-ED-871 — Mending costs **0 Coherence**.

### Faith / CI — collapse by a missing writer, measured over 40 campaigns
`parliamentary_transfer.py:133-134` records a 2026-08-03 instrumented re-measurement: **"CI ≥ 60 is met in
20/20 seeds and CI = 100, the FORCED declaration point where P(declare)=1, is reached in 8/20"** — while
`mass_seizure` is **UNREACHABLE**, with *"zero production callers … no owner write in 40 seeded
campaigns."*

**In 40% of campaigns the game reaches a state where a Theocracy declaration is mechanically forced, and
nothing happens.**

**`Territory.adjust_pt` has exactly one occurrence in the tree — its own definition.** Zero callers:
**Piety is frozen at authored start values forever**, so the Church's yield source can never move. The
designed decoupling triple (world decays → piety collapses → Church ends powerful but unbelieved) is
negated by that single missing writer. And the **only reachable CI consumer is Excommunication, which adds
CI +3** — the sole live feedback through the hub is positive.

### Accord / control — collapse by scoping, plus a canon-level gap
**Anarchy is invisible to the instruments that exist to detect it.** Both the Strain and IP counts scope to
territories *"controlled by playable factions"*, so once territory goes Uncontrolled it **leaves both
counts** — total governance collapse reads as calm, and Strain even qualifies for its −1/season decay.
**The worst world-state produces the least pressure.**

**T-04's return limb does not exist in canon text at all.** `calamity_radiation_v30.md` contains **zero
occurrences of "Order" or "Accord"** — so T-18's cited *"settlement Order effects → Accord erosion"* has no
receiving surface. T-04 passes **out of** this hub, never through it, and the "institutional crisis" in its
own title is unearned.

**The register misidentifies its own gate.** T-07 claims Strain 9+ caps Accord at 2 *"making victory
possible only by ending the war"* — but cap-at-2 is **compatible** with the Accord ≥ 2 victory condition.
What actually blocks victory at Strain 9 is the **Turmoil ≤ 6** clause — which, per the churn audit, has no
writer and is vacuously true.

**Four dialects of "Accord"**: doc range 0–3; the doc's own derived table emits **4** — outside its own
declared range, with no threshold row for it; engine canonical 0–4; engine continuous 0.5–7.0.

---

## §4 · Order sensitivity — latent nondeterminism, three hubs

Each hub surfaced sequence questions that are unspecified and would change outcomes:
- **Accord**: the province-Accord recompute has **no step in §7's list** while Steps 4c/4d read and write
  the derived value directly — so whether a Strain-Crisis Order write triggers a Revolt in the same
  Accounting or the next is undefined. Two §2.4 rules write derived Accord directly and are in neither
  targeting category — the next recompute silently reverts them.
- **MS**: whether *immediate* writes (battle, PP-197 at scene end) count against the ±10 Accounting cap is
  unspecified; a battle-heavy season can exceed the cap or not depending on an unwritten rule.
- **Faith**: the ±1 PT cap does not say whether opposed same-season moves net to zero or clamp
  order-dependently; and **no ±5/season CI clamp is implemented** despite being canon.

---

## §5 · The minimum fix — derive the interaction space instead of authoring it

Do **not** rewrite the 2026-04-18 prose. Add a sidecar **`references/throughlines_index.yaml`**: one row per
live entry — `{id, type, reads, writes, status}` — whose `reads`/`writes` tokens must resolve against the
**already-existing** canonical quantity vocabulary in `descriptor_registry.yaml:186-189`. Then:

1. **Derive** `interact(i,j) ⟺ writes(i) ∩ reads(j) ≠ ∅`, filtered by the §2 type-admissibility rules.
2. **Derive triple candidates** mechanically: variables with ≥3 writers (bus contention — MS surfaces
   immediately), and threshold-conjunction across clocks. Hand-author only those.
3. **One CI assertion**: every `### T-NN` block has an index row, and every token resolves.

This fixes the pre-rename staleness (**RS 22× vs MS 3×; TC 14× vs CI 0×**) at the index layer for free,
without touching a historical document — and **the parser already exists** (`vector_audit.py:1073-1098`,
already letter-suffix aware and already skipping struck T-10).

**Not recommended:** hand-extending the matrix toward 861; renaming inside the prose; integrating the
Solmund appendix before the §2 collapses are ruled.

---

## §6 · The register's three metadata columns each rotted differently

The *chains* are the most valuable structural asset in the repo — the churn audit kept independently
rediscovering things this register stated in April. It is the metadata that failed:

| Column | State |
|---|---|
| `Systems:` | Free text — **186 distinct tokens, 4 (2%) canonical**; some are parse debris from mid-sentence commas. Cannot be machine-joined to anything. |
| `Implementation status` | Claims **"Fully implemented"** for T-04, T-05, T-07 — chains with no writer, no evaluator, and no callers. It measures *design* completeness while labelled as implementation. |
| `Arc Register Coverage` | Of 20 ARC vectors cited: **9 dangling**, **6 resolving only into evacuated audit workings** banner-marked "not independently ratifiable", **5 reaching a live surface**. |

---

## §7 · Weakest claims, carried forward

The **~90 realized pairs** figure is an estimate with no instrument and is deliberately not banked (§0.1
point 4 cuts both ways). The five irreducible triples are **simulation hypotheses, not findings**. Type
assignments for ~5 borderline entries are judgment calls — which is itself an argument for the sidecar's
explicit `type` field. Player-distinguishability counts in the MS band analysis have no playtest
instrument. Absence claims rest on greps plus full reads of owning modules, with the known dynamic-access
blind spot and **no guard test pinning any of them**.
