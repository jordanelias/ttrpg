# 10 — Handoff: build order, controls, guards, and what not to do

> ⚠ **ARCHIVED / SUPERSEDED (2026-08-29).** This is the **pre-critique** version. It is retained
> unedited so the adversarial findings against it stay checkable — **do not build from it.** Six of
> its claims are known false; see [`ARCHIVED.md`](ARCHIVED.md). The live suite is
> `proposals/2026-08-29-greenfield-systems-suite-v2/`.


## Status: PROPOSED (2026-08-28) — held back from ratification-on-merge
## Reads: all of `00`–`09`
## Audience: the session that writes this — Sonnet for the mechanical stages, Opus for the judgment ones (§7)

---

## 1. The one thing to read first

Under **ED-IN-0201** a campaign with no people performs zero faction actions. Every design in this
suite therefore sits behind a population, the population sits behind an RNG substream, and the
substream is **the only step in the entire suite that can be proved byte-identical**.

Land it first, prove it, and every later step's golden movement is attributable to that step. Skip it
and the first campaign that obeys the ruling is also the first campaign nobody can attribute.

---

## 2. Impact classes

Reused from the existing taxonomy rather than re-coined.

| class | meaning | what it costs to land |
|---|---|---|
| **DOC** | documentation, a registry row, or a test. No behaviour. | an edit and a commit |
| **INERT** | code lands and is unreachable, default-off, or provably not campaign-reachable. Seeded goldens byte-identical **by construction** | review only |
| **MOVES** | changes RNG draws or campaign-reachable state. Goldens shift | a re-pin **plus a controlled run** showing the shift is not a balance regression |
| **RULING** | cannot be built until a decision is made | a decision, not a commit |

**One re-pin cycle per landed MOVES item, never one for a batch.** A batched re-pin cannot attribute a
shift to its cause, which makes the measurement worthless in both directions.

---

## 3. Build order

Each row names its impact class and **the control that makes its result a measurement rather than a
number**. Rows within a phase may land in any order unless an arrow says otherwise; phases are strict.

### Phase 0 — preconditions (nothing below can land without these)

| # | item | class | control |
|---|---|---|---|
| 0.1 | **`references/rendering_dispositions.yaml`** — the ratified precondition on appending any Key type. It does not exist, so the gate governing new key types is report-only and every proposed type is ungoverned | **DOC** | none needed; it is a registry file. **Blocks §6.3 of `00` entirely** |
| 0.2 | **A dedicated RNG substream for person generation**, derived from the campaign seed | **INERT** | goldens must be **byte-identical**. That is not a side effect — it is the whole deliverable |
| 0.3 | **Population guards read the person store**, not a generator call counter | **INERT** | the guards still pass; and a synthetic two-person store must now be *visible* to them, which it currently would not be |
| 0.4 | **Band-probability test** — compute all four band probabilities across the practical pool range. **Assert** a floor on Failure, Success and Overwhelming; **report** Partial (§4, G3) | **DOC** (a test) | it is the control |

### Phase 1 — the substrate

Nothing here is reachable from a campaign. All INERT by construction.

| # | item | class | control |
|---|---|---|---|
| 1.1 | **Gauge** primitive: `deposit` / `value` / `band`, geometric decay, no setter | INERT | no caller exists yet; goldens byte-identical |
| 1.2 | Gauge rows in `references/descriptor_registry.yaml` + exporter + blocking `--check` | DOC | the round-trip is the control |
| 1.3 | **Tag** primitive, entity-scoped, `provenance` required and non-empty | INERT | as 1.1 |
| 1.4 | **Post** primitive, vacancy as a first-class state | INERT | as 1.1 |
| 1.5 | **Entity** primitive with its five kinds (`person`, `place`, `faction`, `unit`, `edge`); a person cannot be constructed without at least two edges | INERT | as 1.1 |
| 1.6 | **`derive_ob`** beside `roll_pool` in `engine/autoload/dice_engine.py` | INERT | **no existing call site is repointed.** Adding an unused function changes nothing; repointing an existing site is a different change in a different lane and is not this suite's to make |
| 1.7 | The extended contract shape (`00 §4`) + a shape check enforcing `disclosure:` on every state row and `writable: false` on every derivation | DOC | the check reports against the suite's own rows |

⚠ **1.6 is the one place this suite touches a shared engine module.** It *adds*; it repoints nothing.
The three existing obstacle sites whose reconciliation is suspended are untouched and stay untouched.

### Phase 2 — the map

| # | item | class | control |
|---|---|---|---|
| 2.1 | **`references/tier_registry.yaml`** + its exporter with a blocking `--check` | DOC | the round-trip |
| 2.2 | A leaf reader under `engine/substrate/` — stdlib only, reads the cooked artifact, no `engine.*` or `systems.*` imports | INERT | import-graph probe unchanged |
| 2.3 | Load validations **V-1 … V-4** (`07 §2.1`) | INERT | **expect raises on first run against real map data.** A raise here is a finding about the data, not a defect in the check — resolve the data, do not soften the check |

### Phase 3 — people exist ← *the first MOVES, and the largest*

| # | item | class | control |
|---|---|---|---|
| 3.1 | `cg.condition` (pure, no draws) → `cg.draw` → `cg.attach` | INERT | nothing calls them yet |
| 3.2 | **`wp.worldgen`** — instantiate required posts, issue one demand per post, satisfy authored-first | **MOVES** | goldens re-pin **once**, with a controlled run at ≥120 campaigns per arm. This is the single largest golden movement in the suite and it must land alone |
| 3.3 | `wp.census` ceiling test | DOC | computes the ceiling from registries and asserts the store never exceeds it |
| 3.4 | `wp.displacement` — the one-time standing deposit on post loss | MOVES (small) | measure the standing distribution at season 50 against the arm without it |

### Phase 4 — the gate and the decider

| # | item | class | control |
|---|---|---|---|
| 4.1 | **`fa.gate`** — C1 | **MOVES** | with Phase 3 landed, no faction should ever be gated out at world-gen. **A campaign in which any faction is gated out on season 1 is a Phase 3 defect, not a Phase 4 result** |
| 4.2 | **`fa.select`** — C2, the published `appeal` ranking, consuming no randomness | **MOVES** | action-mix distribution across a controlled run, against the arm without it. Expect the mix to *differ per faction*; a mix that is identical across factions means `appeal` is not reading the holder |
| 4.3 | `fa.resolve` + the seven action rows | **MOVES** | one re-pin, one control, **per action family** — seven cycles, not one |

### Phase 5 — personnel

| # | item | class | control |
|---|---|---|---|
| 5.1 | `pm.vacancy` → `pm.candidates` → `pm.appoint`, with the passed-over grudge | MOVES | appointment-churn rate and grudge-magnitude distribution at season 50 |
| 5.2 | `pm.tenure` → `pm.audit` | MOVES | audit outcome distribution across the four bands; assert none is empty |
| 5.3 | `pm.recall`, with the citable-cause requirement and the per-season cap | MOVES | recall rate; assert the cap binds at least sometimes — a cap that never binds is indistinguishable from no cap |
| 5.4 | `pm.custody` | MOVES | frequency of live `Leverage` tags on posts at season 50 |

### Phase 6 — places and governance

| # | item | class | control |
|---|---|---|---|
| 6.1 | `pl.gauges`, `pl.yield` | MOVES | treasury trajectory; **assert it is not monotone in either direction** |
| 6.2 | `sm.gate`, `sm.business`, `sm.directive`, `sm.respond` | MOVES | directive response mix; assert all four responses are reached |
| 6.3 | `sm.verb` — four verbs, eight forks | MOVES | one cycle per verb. **Assert every fork is chosen sometimes** — a fork nobody takes is a fork that failed the §4.1 rule in `08` |
| 6.4 | The **facility writer** | MOVES | ⚠ **this is the item that closes the post loop.** Measure the loop's gain here, with a control, before it lands. `03 §7`, `06 §7` and `07 §9` all name this loop from their own ends and all three say the gain is unmeasured |

### Phase 7 — adjacent

| # | item | class | control |
|---|---|---|---|
| 7.1 | `ad.succession` | MOVES | outcome distribution over decisive/contested/split; assert none is empty |
| 7.2 | **The personal→mass leverage guard, part 1** — the form check (`09 §2.4`, G6a) | **DOC** (a test) | **lands BEFORE 7.3.** Its whole value is being in place before anything can produce the effect it bounds. Part 2 (G6b) is scheduled against `resolve_force`, not against this phase |
| 7.3 | `ad.unit`, garrison as assignment, two-tier defeat severity | MOVES | force-composition distribution; garrison/field split |
| 7.4 | `ad.motion`, recorded defeat, the sanction dial | MOVES | motion subject variety — **assert the same subject does not recur every season**, which is the defect the subject requirement exists to fix |

---

## 4. The six guards, and why each earns its existence

`CLAUDE.md` §0.1 point 5 admits a guard only where the defective artifact would be load-bearing on
**the game**, on the exported params, on the port, or on a Jordan decision. A pattern defect in an
artifact that is load-bearing only on this repository's process is evidence the artifact can be wrong
without cost.

| # | guard | what it fails on | load-bearing on |
|---|---|---|---|
| **G1** | no reachable Tag has empty `provenance` | a durable relationship outcome with no cause behind it | **the game** — the mechanic is *why did this actor turn on me*, and a forged relationship corrodes the system for players who never forge one |
| **G2** | every declared Gauge satisfies `rest + max_accrual/λ ≤ ceiling` | a gauge whose declared sources can pin it at its ceiling | **the game** — the difference between a place that can recover and one that cannot, reached from ordinary play |
| **G3** | **asserts** a floor on the Failure, Success and Overwhelming band probabilities across the practical pool range; **reports** the Partial band without failing on it | a degree band the suite depends on that stops discriminating at one end of the pool range | **the game** — the ladder is the output every mechanic in the suite reads |
| **G4** | no module contract declares a `budget:` whose cost is consumed inside a pool or obstacle expression | a budget that has become a modifier | **the game** — one currency spendable across two engines with different leverage curves is an exploit, not an economy |
| **G5** | the person store never exceeds the ceiling computed from the registries | unbounded population growth | **the game** — the failure it catches is the one that makes a late campaign unplayable |
| **G6a** | no declared personal→mass input is expressed as an absolute — every one is a coefficient on a unit-scoped gauge | a flat personal effect on a mass outcome | **the game** — the difference between a commander mattering and a commander deciding |
| **G6b** | *(lands with `resolve_force`, not with this suite)* the same personal-scale input moves the outcome probability by an in-band amount across three orders of magnitude of unit size | the same, measured rather than declared | as G6a |

**G1–G5 and G6a are arithmetic and none needs a campaign run.** That is deliberate: a guard that
requires a campaign to evaluate is a guard nobody runs. G6b is the one that needs an implementation
under it, and it is scheduled against that seam (`05 §5.1`) rather than left to be discovered.

**A seventh guard was considered and rejected:** a check that every module contract's `remit` names a
post kind that exists. It is real, it is cheap, and its subject is the *contract registry* rather than
a game mechanic — a defect in it costs a confusing error message, not a wrong game. Under the
load-bearing predicate that is evidence the artifact can be wrong without cost, so it is not minted.
The exporter's blocking round-trip already fails on an unresolvable target, which is the part that
matters.

---

## 5. The ruling docket

Five open questions, each stated where it blocks. None is a question a session should answer by
picking the most familiar option.

| # | question | blocks | why it survives the five tests |
|---|---|---|---|
| **Q-1** | **What a leader is, structurally** — an authored character, a generated person, or a role held by whoever meets some other bar | Phase 3.2's first satisfaction of the head post | ED-IN-0201 §22 leaves it open in terms. The *post* and the *candidate gate* are designed; who is eligible for the head post on turn zero is a content decision with materially different games behind each answer |
| **Q-2** | **"No commander, no battle" — a gate or a penalty** | `09 §2.3`. **This suite takes the gate and marks it as the reading it took** | ED-IN-0201 §20 flags it as the ruling's one genuine ambiguity. A gate composes with C1's other two clauses; a penalty is a modifier on a mass outcome and re-opens the leverage problem nobody has solved |
| **Q-3** | **The Partial band's width** | nothing here — P0-3 makes the suite independent of it | Changing the band widths edits a ruled surface. G3 measures it; this suite refuses to depend on it |
| **Q-4** | **The name of the faction-scale acceptance aggregate** | `06 §2.1` uses a provisional name | The obvious word is live under three incompatible readings; choosing one is a canon act |
| **Q-5** | **Are down-distributed place deltas disjoint from what the up-aggregate reads** | the convergence claim in `06 §7` | `propagation_spec_v1` §3 D.6 flags it high-priority and explicitly forbids resolving it locally. The suite stays internally disjoint by convention (`09 §4.4`); the general question is untouched |

**Two further forks are flagged rather than escalated**, because both have a defensible default and
neither would overwrite ratified canon: whether garrisoned units may move offensively without
reassignment (`09 §2.2`), and whether `fm.policy` changes should cost an action or be free (`06 §5`
charges one).

---

## 6. What not to do

The failure modes most likely to be reached by a session working in good faith from these documents.

| do not | because |
|---|---|
| **Batch the MOVES items** | eight simultaneous golden movements and no way to attribute any of them. That is not a fast path, it is an unmeasurable one |
| **Repoint an existing obstacle site to `derive_ob`** | three built sites disagree and their reconciliation is deliberately suspended. Phase 1.6 *adds* a function; it repoints nothing |
| **Add a fifth `scale` member** | the runtime enum is ruled and raises. The containment ladder lives on the `tier` axis precisely so it does not need one |
| **Add a sixth tag family** | a recurring term-limited claim is `Debt(recurs=True, ttl=…)`. The enum is closed so a mechanic cannot be smuggled in as a family |
| **Give a Gauge a setter** | it is the one thing that makes *no aggregate is ever written* structural rather than a discipline every future author has to remember |
| **Convert budget into dice or an obstacle shift** | `01 §4.3`. G4 catches it; do not need it to |
| **Build a spawner** | population is a function of posts and places. The documented failure of the alternative is five-figure late-campaign rosters and two community fixes pulling in opposite directions |
| **Write an event deck before `sm.business` runs on the ledger** | the ledger is the deck (`08 §5`). Cards are an enrichment; building them first makes the layer content-blocked for no gain |
| **Branch on a faction, place or person name** | scripting drift. A faction's character is who holds its head post; a place's is its kind and its gauges |
| **Give the player their own entity kind, flag or module** | `01 §3.4`. The player is a person holding a post; a player-only path is scripting drift by construction, and it is also how a fast path becomes a *different* algorithm from the played one |
| **Let a relational term outrank the structural ones** in any selection function | `01 §2.4`. Uncapped, custody becomes strictly better than office and opinion dissolves positional conflict — the documented failure of relationship modifiers that grow large enough to paper over structure |
| **Restore a saturating additive decay** | a restoring term with a ceiling below its input pins the gauge permanently, from ordinary play. G2 catches it |
| **Treat any of these documents as canon because they merged** | the whole suite is held back from ratification-on-merge, explicitly and in the PR body |
| **Delete anything under `systems/`** | this suite proposes no deletions. No subtractive verdict is final until an independent pass has steelmanned the existing action for KEEP, and none has been run |

---

## 7. Model tiering for the build

Per `CLAUDE.md` §10 — set it per task rather than inheriting one tier across the fan-out.

| stage | tier | why |
|---|---|---|
| Registry rows: gauge declarations, tier registry, action rows, verb rows, contract rows | **sonnet** | bounded transcription against a stated schema, with a blocking round-trip as the check |
| The four substrate primitives and their tests | **sonnet** | the contracts are specified; the work is faithful implementation |
| Exporters and their blocking `--check` round-trips | **sonnet** | pattern-matching against three existing instances |
| The six guards | **sonnet** | each is an arithmetic assertion with its property stated |
| `cg.condition`'s conditioning form, `fa.select`'s `appeal`, the loop-gain measurements | **opus** | judgment nodes where being wrong is silent — a mis-shaped conditioning function produces a plausible population that is subtly degenerate, and an uncontrolled loop measurement is worse than none |
| Q-1 … Q-5 | **nobody** — these go to Jordan | a live design choice where two defensible options lead to materially different games |

---

## 8. Verification, per commit

```
python -m pytest tests/valoria -q          # the shipping gate; not a belief gate
python tools/ci_naming_check.py
python tools/validate_ed_citations.py
python tools/compliance_check.py --check-only --repo-state .
python tools/currency_consistency_check.py
```

And for every **MOVES** item, additionally:

```
python tools/export_descriptors.py --check     # if a gauge row moved
python tools/export_composition.py --check     # if a composition role moved
python tools/balance_oracle.py                 # the control arm — not a CI gate
```

⚠ **`pytest tests/valoria` passing is a shipping gate, not evidence a change is correct.** It catches a
confounded change only when the change incidentally breaks something unrelated; a clean implementation
of a wrong design is green. The controls in §3 are what make each step a measurement, and the guards
in §4 are what make a recurrence loud.

---

## 9. Definition of done

Per `CLAUDE.md` §0.2: **a juncture is done when the behaviour executes, and something ran it.** Not
when a document exists with a status line.

| stage | the execution artifact that closes it |
|---|---|
| Phase 0 | a byte-identical golden across the substream change, and the band-probability report |
| Phase 1–2 | the exporters' round-trips green, and the load validations raising on malformed data |
| Phase 3 | a seeded campaign in which `|persons| > 0` and every faction's head post is filled at season 1 |
| Phase 4 | a seeded campaign in which two factions with different heads take **different actions from the same world state** |
| Phase 5 | a seeded campaign containing at least one appointment, one audit and one grudge written by being passed over |
| Phase 6 | a seeded campaign in which a place's gauges move, its ledger has entries, and its business is drawn from them |
| Phase 7 | a seeded campaign containing a succession whose outcome was not decisive |

Each row is a claim about a run, and each is falsifiable by making the run and looking. None of them
can be satisfied by writing.
