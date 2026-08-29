# 02 (part 2) — Character generation: determinism, the surface, the contracts and the audit

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`02_character_generation.md`](02_character_generation.md) — **part 1 first; this continues it**
## Part 1: §§1–7 (the problem, caste and heritage, the stage ladder, grants, edges and Knots,
## beliefs, flaws) — and the `## Overrides` block, which governs both parts
## Part 2: §§8–11 (determinism and totality, the player surface, the module contracts, the audit)

Section numbers run continuously across both parts. The `## Overrides` block and the anti-fabrication
statement are in **part 1** and bind here without being restated.

---

## 8. Determinism, totality, and the two properties v1 got right

Carried from v1 `02 §4-5`, unchanged in substance, restated because they now cover a **loop** — the
stage ladder of [part 1 §3](02_character_generation.md):

```
substream = Random( H(campaign_seed, "cg", tier_node, faction, ordinal, stage_index) )
```

`stage_index` is the only addition and it is required: without it a person walking four stages
consumes four draws from one position and re-phases every later person. **The generator draws from its
own substream, never the shared campaign stream** (P0-2), so population size cannot re-phase any other
consumer of randomness.

**Generation is total.** For any well-formed demand the ladder returns a person; there is no failure
branch and no "no suitable candidate", and ill-formed demands are **load-time validation errors**.
That is what lets ED-IN-0201's gate be a precondition rather than a trap: a head post can always be
filled by *someone*; whether that someone is any good is the game.

**Totality gains a second obligation, because stages can fail their gates.** A stage whose gate does
not hold is **skipped, not retried**, and skipping is legitimate: a person who never had a Formation
never had a mentor, and the world should be able to make one. **Origin may never be skipped** — it is
where identity is fixed. Falsifier in §11.1.

⚠ **A guard that counts generator calls does not observe any of this.** Carried from v1: a population
guard must read the **person store**, because a call counter is invisible to a loader, a restore, or
any other path constructing people without the generator.

---

## 9. The player-facing surface — counted against `00 §2`'s budget

**`02` spends zero of the whole-game single-digit verb budget.** Character generation is where a deep
game most often explodes its surface; canon already ruled the other way — *"the player never sees
Conviction weights, Self-Other values, or cultural template assignments"* (`questionnaire:32`).

| what the player is asked | how many | how often |
|---|---|---|
| scenario questions across the four creation stages, **12–16 total**, canon's number (`questionnaire:43`) | 12–16 | **once per character**, ~10–15 minutes (`:47`) |
| a response to a **challenge** situation a flaw or a belief put on the Slate | `10`'s 3–5, inherited | when the Slate ranks it in — never pushed by this document |
| **in-play verbs added by this document** | **0** | — |

| what the player never touches |
|---|
| a stage row, a conditioning distribution, a `Δ_MAX`, a `p_floor`, an entropy floor |
| a capability number, a conviction weight, a credence value, a TS or Truth number (**bands only** — `clock_registry_v30.md:71`) |
| a flaw's `binds_when` predicate, a belief's revision band, an age gate's threshold — **triggers are hidden** (`01 §8`) |
| the caste **matrix** — but its **verdict on a named candidate is published in full** (`04`; `00 §6` principle 5) |
| whether a knot candidate passed canon's gate — they experience the relationship, not the roll |

**Substrate objects: 4 creation stages + N career stages · 1 grant vocabulary of 8 members · 6
adopted edge kinds · flaw rows · belief propositions · 2 identity fields. Surface: 12–16 one-time
questions, 0 verbs.** The substrate table is longer than the surface table, which is the ratio
`00 §2.3` point 4 requires.

**The 12–16 questions are not a verb, and the distinction is load-bearing.** A verb is selected from
a menu **every season**; the budget is about recurring load. A one-time interface the player never
revisits costs the *learning* budget once and the *per-season* budget never. If that is rejected, the
fix is to shorten canon's question set — never to move the derivation onto the player.

---

## 10. Module contracts

`00 §7`'s shape, with the v2 `form:` and `transitions:` fields. **Five modules; four are v1's, and
`cg.stage` is the only addition** — it is where change A lands for people.

```yaml
# cg.demand and cg.condition are UNCHANGED from v1 02 §6 and share one shape, given once:
#   parent: character_generation · class: substrate · tier: null · remit: [] (not player-invocable)
#   budget: null · emits: [] · form: [] · transitions: [] · ob_sites: []
- module: cg.demand
  scales: [personal]     resolver: gate         state: []      disclosure: []
  consumes: [{type: post.vacant, from: [pm.vacancy]}]     # → one demand per vacant post
- module: cg.condition
  scales: [personal, settlement]   resolver: derivation   consumes: []
  state: []                       # pure; consumes no RNG and stores nothing
  disclosure: [{of: distribution, inputs: published, presentation: band, trigger: hidden}]

- module: cg.stage                # NEW (v2). Walks ONE stage row. Two callers: generation, boundary.
  parent: character_generation
  class: substrate
  scales: [personal]
  tier: null
  resolver: gate                  # age/service gate; the CONTENT is cg.draw's derivation
  remit: []
  budget: null
  consumes: []                    # reads state at the boundary — never a posted emission (J-N)
  emits:
    - {type: form.transitioned, terminal: false}
  state:
    - {name: person.life_stage,  bucket: entity, writable: true, owner: cg.stage}
    - {name: person.capability,  bucket: entity, writable: true, owner: cg.stage}
    - {name: person.traits,      bucket: entity, writable: true, owner: cg.stage}
    - {name: person.beliefs,     bucket: entity, writable: true, owner: cg.stage}
    - {name: credence,           bucket: gauge,  writable: true, owner: cg.stage}
    - {name: tag,                bucket: tag,    writable: true, owner: substrate.ledger}
  form:
    - {entity_kind: person, field: life_stage}
    - {entity_kind: person, field: capability}
    - {entity_kind: person, field: traits}
    - {entity_kind: person, field: beliefs}
  transitions: [stage.*, belief.retire, flaw.challenge]     # from references/form_registry.yaml
  ob_sites: []                    # cg.stage is a GATE. It derives no obstacle. §10.1
  disclosure:
    - {of: person.life_stage, inputs: published, presentation: exact, trigger: hidden}
    - {of: person.traits,     inputs: published, presentation: exact, trigger: hidden}
    - {of: credence,          inputs: published, presentation: band,  trigger: hidden}

- module: cg.draw
  parent: character_generation
  class: substrate
  scales: [personal]
  tier: null
  resolver: derivation            # a draw from a declared distribution, not a contest
  remit: []
  budget: null
  consumes: []
  emits: []
  state:
    - {name: entity, bucket: entity, writable: false, owner: substrate.entity}
  form: []
  transitions: []
  ob_sites: []                    # a conditioned categorical draw, not a contest. §10.1
  disclosure:
    - {of: person.capability_provenance, inputs: published, presentation: exact, trigger: hidden}

- module: cg.attach
  parent: character_generation
  class: substrate
  scales: [personal]
  tier: null
  resolver: derivation
  remit: []
  budget: null
  consumes: []
  emits:
    - {type: person.generated, terminal: false}
    - {type: edge.formed,      terminal: false}
  state:
    - {name: edge,               bucket: entity, writable: true,  owner: substrate.entity}
    - {name: thread_sensitivity, bucket: gauge,  writable: true,  owner: cg.attach}
    - {name: truth,              bucket: gauge,  writable: true,  owner: cg.attach}
    - {name: tag,                bucket: tag,    writable: true,  owner: substrate.ledger}
  form: []
  transitions: []                 # a knot CANDIDATE is submitted to canon's gate; no transition here
  ob_sites: []                    # canon's Knot formation Ob is canon's site, not this module's. §10.1
  disclosure:
    - {of: thread_sensitivity, inputs: published, presentation: band, trigger: hidden}
    - {of: truth,              inputs: published, presentation: band, trigger: hidden}
```

**Two contract facts, stated rather than left to be inferred.** No module here declares a `budget:` —
generation is not an action economy, and a budget that bought characters would be the modifier-shaped
currency `01 §5.3` refuses. And `cg.stage` is the **only** module in this suite declaring
`form: person.capability`, so what can move a person's competence is a grep over one field — the whole
point of the fourth write leaf being declared rather than free (`01 §2.4`).

**Key types used: `form.transitioned`, `person.generated`, `edge.formed`, all three already in
`00 §9.2`. This document appends none** — which matters because P0-1
(`references/rendering_dispositions.yaml`) is unexecuted, and appending a type meanwhile is the drift
that precondition exists to stop.

### 10.1 `ob_sites:` and the commensurability gate — `02` declares none, and says where the two real sites are

`00 §7` now requires every module to declare `ob_sites: [{target, modifier_max, pool_max}]`, because
without it `01 §6.1`'s commensurability gate is a rule nothing can check. **Every module in `02`
declares `ob_sites: []`, and that is a fact about the design rather than an omission:** nothing here
rolls. Four of the five modules are `derivation` and the fifth is a `gate`; a conditioned categorical
draw has no obstacle, and **every form transition is gated, never rolled** (`01 §2.2`).

Two obstacles are nonetheless reachable from this document, and both belong to someone else:

| the site | whose | what it must declare |
|---|---|---|
| **canon's Knot formation roll** — `Spirit × 2 + History, TN 7, Ob 2` (`01 §7.5`, `knots_v30.md:76`) | **canon's**, FI lane. `cg.attach` submits a *candidate* to it and does not own it (§5.2) | canon fixes `Ob 2` outright, so no `derive_ob` target is involved and the gate does not bite |
| **the alternative duty row** C-5 proposes in place of canon's `+1 Ob` caste penalty (§2.4) | **`04`/`08`'s** — `02` owns the argument, not the implementation | a real `ob_sites:` row with all three fields, whose `target` is the **duty's own** target, not the actor. That is the whole point of the override: the obstacle comes from the thing being attempted, never from who is attempting it |

⚠ **Thread Sensitivity is a gate target and must never become an obstacle target.** `01 §6.2` records
it as failing the commensurability gate **catastrophically** — ob 50 against μ 7.2 — and notes the
failure is not in the gauge but in ever passing it to `derive_ob`. **`02` uses TS only as canon uses
it: as a gate** — `TS ≥ 30` for Knot formation (§5.2) and the Warden ladder's TS rungs (§2.3). The
same holds for the other seeds: `truth` is seeded and read, never targeted. This paragraph exists so a
later author extending the life-path design does not reach for TS as an obstacle, which is now a
known-dead mechanic rather than an untested one.

**`credence` is the one new gauge this document introduces, so declaring its bound is `02`'s job, not
a later lane's.** `01 §6.2` lists `standing`, `exposure`, `pressure` and others as *"unverifiable
today — scale undeclared in this suite"*, and a new gauge that silently joined that list would be
three declaration-time guards inert on it (`01 §2.3`'s `H_MIN`, `01 §5.1`'s fixed-point falsifier, and
the commensurability gate). So: **`credence` is declared on a bounded `0–5` scale in
`references/descriptor_registry.yaml`**, matching canon's own belief-adjacent meter — the Truth track
is 0–5 (`clock_registry_v30.md:71`) and `01 §6.2` scores that family **pass**. `credence` therefore
inherits a passing verdict *by construction* rather than being left unverifiable, and `02` still
targets it with nothing. A later document that wants to may, and must then declare the site.

> **Falsifier.** A declaration-time test asserting every gauge this document introduces has a declared
> non-`None` ceiling, and that no `cg.*` module declares a non-empty `ob_sites:`. Load-bearing on the
> game: a gauge with no ceiling is one `01`'s three arithmetic guards silently skip.

---

## 11. Property audit

### 11.1 Engine class — and the scope gate, honoured

**Nothing in this document rolls.** A conditioned categorical draw is not the continuous engine and
every transition here is a **gate** (`00 §6` principle 4). Per the suite's rule — *do not manufacture
a NERS verdict for a module that does not roll* — the properties below are diagnosed against the
generator directly, and where one is about resolution it says so rather than being scored. The single
roll in this document's blast radius is **canon's Knot formation roll** (`01 §7.5`,
`knots_v30.md:76-83`): cited, not designed, not audited here.

| property | verdict | reasoning and falsifier |
|---|---|---|
| **P-i** legible odds | **pass, scoped** | The player does not choose against this draw, so its odds are not a decision they make. What P-i requires here is a legible *result*: `capability_provenance`, the conditioning inputs and every caste verdict are published (`01 §8`; `04`). **Falsifier:** a test asserting every `cg.*` state row carries a disclosure block and none sets `trigger: published` |
| **P-ii** uniform leverage | **pass** | §3.5 — additive log-odds with a bounded shift; a unit of conditioning moves the distribution by the same amount wherever it lands. The multiplicative form fails this and is the version not built. **Falsifier:** apply a fixed signal to a tail category and a head category and assert the log-odds delta is identical |
| **P-iii** bounded, monotonic | **pass, with the layering caveat** | Capability moves one axis by at most one band per stage, clamped; conviction reweights sum into the declared band; `Δ_MAX` bounds conditioning, `p_floor` bounds degeneracy. **The caveat is real:** these bounds were proved for ONE application in v1 and now apply `S` times. **Falsifier:** §3.5's terminal-distribution test, plus a test that no generated capability exceeds `ATTRIBUTE_CEILING` after the longest reachable ladder |
| **P-iv** graded, recoverable | **pass** | §8 — generation is total, and the load-bearing event (can a required post be filled) cannot fail. Stage skipping is graded, not all-or-nothing. **Falsifier:** a test asserting every well-formed demand returns a person, and that `Origin` is present on **every** person in a seeded world |
| **P-v** right engine | **pass** | Not a contest, so neither canonical resolver applies; a draw from a declared distribution is the right tool, and a contested roll here would resolve something that is a construction. Every *transition* is a gate: the uncertainty was upstream |

### 11.2 Loops, each with its bound

| loop | bound | gain |
|---|---|---|
| demand → generation → post filled → (later vacancy) → demand | demands come only from vacancies and scenes, both bounded by the map; satisfying one **removes** it | **not a gain loop** (carried from v1) |
| stage `k` → conditions stage `k+1` → … | finite and age-gated; `reversible: false` on every stage transition, so no cycle exists | **bounded by construction** |
| career stage → capability up → better outcomes → post retained → career stage | `N`-season period; one axis by one band per stage; `ATTRIBUTE_CEILING` clamps | **positive feedback, bounded above. Gain UNMEASURED** — no campaign has run long enough to see whether an incumbent becomes unbeatable before the ceiling binds. §3.3's upper reachability bar is the guard and it is unverified |
| belief evidence → credence → revision → Scar → conviction shift (`character_canon §6.3`) → new belief | active set ≤ 3 by canon; canon's Scar ladder terminates at "3+ — crisis" | **gain UNMEASURED**; the escalation is canon's, not this document's |
| flaw binds → candidate → scene → challenge → transition | the Slate's scene budget (`10`) bounds how many reach the player; `challenge` is `reversible: false` | **bounded by the Slate** — why P0-5 orders `10` before F |

### 11.3 What this document depends on that could move

| dependency | tier | if it moves |
|---|---|---|
| `character_canon_v30.md` (belief object, `≤3` cap, revision conditions) | **PROVISIONAL** | §6's cap becomes a parameter — the gauge-per-belief decision is then re-argued against `01 §3.2`, not tuned |
| `npc_relational_graph_v30.md` (PP-724) | Class A, **PROVISIONAL** | §5.1's kinds change; the *container* does not (`01 §7.3`) |
| `faction_politics_v30.md §3.2` | **CANONICAL** | `04`'s gate changes; `02` supplies the input, not the rule |
| Key **consumption** (`cg.demand`'s one `consumes:` row) | **J-O** open | it becomes a boundary read over vacant posts; nothing else here consumes a Key |
| cross-season latency | **J-N** open | §3.4's career gate is a boundary state read precisely so it survives either ruling |

### 11.4 N / R / S / E

**Necessary** — a game gated on people existing cannot omit what makes people, and the belief object
already in the tree has **no producer** (`characters_flow_skeleton_v1.md:30-31`, `:92`). **Robust** —
both failure directions are bounded by a declared parameter with an arithmetic check; layering is the
one place robustness is *weaker* than v1's, which §11.1 P-iii says rather than hides. **Smooth** —
one pipeline for authored and generated characters, one substream, one stage walker serving both
creation and career, zero attributes and zero convictions named literally. **Elegant** — four stages
adopted from canon rather than invented, one grant vocabulary of eight members, one new module, **no
new registry file, no new stored primitive, no new Tag kind, no new Key type, no in-play verb**.

### 11.5 The weakest claim in this document, named

**That a belief belongs in a Gauge.** It rests on canon's `≤3` cap, and that cap is **PROVISIONAL**.
If the cap moves — or if a later layer wants propositions held by *every* person about *many* facts —
the gauge-per-belief count grows exactly the way `01 §3.2` refused for memories, and the correct
response is to re-derive credence at read from tag data rather than to raise a limit. The falsifier
is cheap and should be run before any belief content is authored: **count `credence` gauge instances
in a seeded world and assert the per-person count is `≤ 3` and the world total is `≤ 3 × persons`.**
