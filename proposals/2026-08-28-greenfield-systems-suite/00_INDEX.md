# Greenfield Systems Suite — Index, Hierarchy and Compliance Contract

## Status: PROPOSED (2026-08-28) — surfaced by location (`proposals/`); ratifies nothing
## Version: v1.0 · Lane: IN (cross-cutting: FA, SE, WR, MB, PC, SC)
## Reads: `research/valoria_systems_integration_master_v1{,_part2,_part3,_part4}.md` ·
## `research/valoria_game_precedent_companion_v1{,_part2..part8}.md` ·
## `research/cross_scale_action_catalogue_v1.md` · `research/personnel_muster_integration_master_v1.md`

**Reading order:** 00 Index → [01 Substrate](01_substrate_primitives.md) →
[02 Character Generation](02_character_generation.md) → [03 World Population](03_world_population.md) →
[04 Personnel](04_personnel_management.md) → [05 Faction Actions](05_faction_actions.md) →
[06 Faction Management](06_faction_management.md) → [07 Places](07_places_and_settlements.md) →
[08 Settlement Management](08_settlement_management.md) → [09 Adjacent Systems](09_adjacent_systems.md) →
[10 Handoff](10_handoff_build_order.md)

---

## 0. What this is, and what it is not

**What it is.** A clean-slate design for the eight systems named in the brief — character generation,
world population, personnel management, faction actions, faction management, settlements, settlement
management, and the systems adjacent to them — expressed as a **hierarchy of module contracts over
four stored primitives**, composed on `engine/` and the centralized registries under `references/`.

**What it is not.**

- **Not a migration plan.** These are designs for what the systems *should be*. What happens to any
  currently-shipping module is a disposition question, and `references/throughlines_meta.md:233-238`
  requires an independent pass to steelman each existing action for KEEP before any subtractive
  verdict is final. No such pass has been run. **This suite proposes no deletions.**
- **Not canon, and it does not ratify on merge.** Under ED-1094 a merge normally ratifies a PROPOSED
  document's contents. **This suite is held back explicitly and in full**: it asserts mechanisms that
  would replace ratified surfaces, and every one of them needs its own decision. Merging this
  directory files it; it flips no `## Status:` line anywhere and changes no behaviour.
- **Not derived from `systems/`.** By instruction, no module, formula, constant or interface under
  `systems/` was used as a source for any design below. The suite composes on `engine/`,
  `references/` and the rulings named in §3. Where a design necessarily lands in the same conceptual
  place as something that exists, that is convergence, not citation, and §5 says what to do about it.

**Under `CLAUDE.md` §0.05 this suite is reference.** Delete it and the game behaves identically. It
becomes mechanism only when the contracts in §4 are written as code and the registries in §6 carry
their rows.

---

## 1. The hierarchy

ED-IN-0200 (Jordan, 2026-08-27, ruled and unexecuted): *"key contracts and module contracts etc need
to be explicitly defined in a centralized hierarchical manner."* The measured state it records is
three flat namespaces referencing each other by string, with no surface from which a reader — or the
Godot port — can descend from the game to a subsystem to a module to its Keys to the fields those
Keys carry.

This is that descent. **Five levels, and one axis split at level 1 that is the reason the hierarchy
can exist at all.**

```
GAME
├── SCALE      — how big an event is.  personal · settlement · territory · peninsula
│               (the runtime enum; four members; a fifth raises)
└── TIER       — what contains what.   place kinds and their parent edges
    │           (an ORTHOGONAL axis, declared in its own registry)
    │
    └── SUBSYSTEM   one lane · one folder · ONE wrapper that owns all Key I/O for it
        │
        └── MODULE  Key IN → resolver → OUT(+Keys) + owned state
            │       a registry ROW, never a branch
            │
            ├── STATE    exactly one of four buckets — entity · gauge · tag · post
            ├── KEYS     type ids from the cooked registry; nothing invented (§5, P0-1)
            ├── REMIT    which posts may invoke this module
            └── VIEW     what is disclosed of its state, and at what granularity
```

### 1.1 The axis split, and why it is the load-bearing move

Five scale vocabularies are live in the tree and only one member — *personal* — appears in all of
them. The honest reading is that **two different questions have been forced into one field**: *what
size of thing is this event about* and *what administrative tier owns this*. The runtime enum answers
the first and hard-refuses a fifth member; the ruled containment ladder answers the second and has no
representation anywhere.

Forcing them apart costs nothing and unblocks both:

| axis | answers | members | owner | mutable? |
|---|---|---|---|---|
| `scale` | how far an event's consequence reaches | the runtime four | the Key substrate | no — the enum is ruled |
| `tier` | what contains what | open, declared per place kind | a new tier registry (§6) | yes — it is data |

A Place declares both. A Key carries only `scale`. Nothing in this suite proposes a fifth scale
member, and nothing in it requires the containment ladder to be squeezed into four.

⚠ **This does not resolve the collision; it routes around it.** ED-IN-0103 fork 1 holds vocabulary
unification for Jordan. The split above is compatible with either outcome — if the enum is later
widened, `tier` collapses into it; if it is not, `tier` stays separate. It is named here as a
**design decision this suite takes**, not as a ruling it makes.

---

## 2. The four stored primitives

Everything in this suite is composed from four things that store state, plus two engine extensions
that store nothing. `01_substrate_primitives.md` specifies them; this is the roster.

| # | Primitive | Stores | Written by | Read as |
|---|---|---|---|---|
| **P-1** | **Entity** — kinds `person · place · faction · unit · edge` | an id, a kind, and immutable identity fields declared per kind | created at load or by generation; **never written afterward** | the actors, the containers and the relations of the game |
| **P-2** | **Tag** | durable discrete memory: `(owner, kind, key, value, ttl, provenance)` | `tag_append`, provenance required and non-empty | a ledger on any entity — person, faction, place, post, edge |
| **P-3** | **Post** | a grantable, revocable commission: kind, tier node, principal, holder, remit, term | `post_grant` / `post_revoke` only | who may act, and what option set they have |
| **P-4** | **Gauge** | a bounded, continuously-read, geometrically-decaying value | `gauge_deposit(delta, provenance)` — **no setter** | every continuous quantity in the game |

**One entity primitive with five kinds, not five primitives.** A person, a place, a faction, a unit
and a relation all have the same shape — an identity that does not change, plus gauges, tags and
posts that do. Giving each its own primitive would put identically-structured containers into
different taxonomies, which is exactly the shape-divergence failure a top-imposed contract exists to
prevent.

**The one write rule.** Every write in this suite terminates at one of exactly three leaves: a Gauge
deposit, a Tag append, or a Post grant/revoke. **Entities are never written after creation, there is
no fourth channel, and no aggregate is ever written.** That is `propagation_spec_v1.md` §2's AU-1
made structural rather than a discipline: an aggregate has no setter because the primitives it is
derived from are the only things with one.

**The two engine extensions**, which store nothing and live beside the code that already owns their
neighbours:

| # | Extension | Where it belongs | What it ends |
|---|---|---|---|
| **E-1** | `derive_ob(target_score, modifiers)` — the obstacle, fractional, floor `OB_MIN` | beside `roll_pool` in `engine/autoload/dice_engine.py` | the obstacle having a ruling and no owner |
| **E-2** | a `disclosure:` block on every state row | the registries in §6 | disclosure being a per-system choice |

---

## 3. The rulings this suite executes, and the ones it waits on

### 3.1 Executed by the designs below

| Ruling | What it says | Where this suite executes it |
|---|---|---|
| **ED-IN-0201** (2026-08-28) | No leader → no faction action; no governor → no settlement governance; no commander → no battle. And the person shapes *which* action is chosen from the same option set with the same information | **05 §1** (the gate) and **05 §3** (the decider, as a GATE on the option set — never a modifier on a roll, per that ruling's own NERS constraint) |
| **ED-IN-0200** (2026-08-27) | Key and module contracts explicitly defined in a centralized hierarchical manner | **§1** above, and the uniform contract shape in **§4** |
| Jordan, 2026-08-14 | An obstacle rolled against a character or faction is *their corresponding score/2 plus whatever specific modifiers exist for them in that instance* | **E-1**. Every roll in this suite derives its obstacle through one owner and nowhere else |
| Jordan, 2026-08-25 (ED-IN-0196) | TN is 7. Always | inherited; no design below names a TN |
| Jordan, 2026-08-14 (margin ladder) | `margin ≥ 3` Overwhelming · `≥ 1` Success · `[0,1)` Partial · `< 0` Failure, single owner | inherited; **no design below has a consequence that fires only on Partial** — see §5, P0-3 |
| Jordan, 2026-07-13 | Factions hold **people**, and it is the number of people and the weight of their positions that carry the value of a faction | **06** — a faction's derived weight is an aggregate over held posts, not over territory alone |
| `propagation_spec_v1` AU-1 | No aggregate is ever written | **the one write rule**, §2 |
| ED-SC-0032 | A subsystem extending the ladder injects a declared `BandExtension` whose only power is to veto an Overwhelming | **05 §6** — information gates option sets and may declare a BandExtension; it never adds dice |

### 3.2 Waited on — named, not guessed

These are the questions this suite deliberately does not answer. Each blocks a specific piece and
each is stated where it blocks.

| # | Question | Blocks | Why it is genuinely open |
|---|---|---|---|
| **Q-1** | **What a leader is, structurally** — an authored character, a generated person, or whoever holds the head post by some other rule | `04` appointment, and therefore the C1 gate's first satisfaction at world-gen | ED-IN-0201 §22 leaves it open in terms. This suite designs the *post* and the *candidate gate*; who is eligible for the head post on turn zero is a content decision |
| **Q-2** | **"No commander, no battle" — a gate or a penalty** | `09 §2` | ED-IN-0201 §20 flags it as the one genuine ambiguity. A gate composes with C1's other two clauses; a penalty re-opens the personal→mass leverage problem nobody has solved. This suite designs the **gate** and marks it as the reading it took |
| **Q-3** | **The Partial band collapses across the pool range** (a fixed one-success window over a spread growing as √Pool) | nothing in this suite — see §5, P0-3 for the constraint that makes it not block | Changing the band widths edits a ruled surface. This suite refuses to design around it and instead forbids itself from depending on it |
| **Q-4** | **The name of the faction-scale acceptance aggregate** | `06 §2` uses `faction.acceptance` provisionally | *Mandate* is live under three incompatible readings. Picking one is a canon act |
| **Q-5** | **Whether the down-targeted place deltas are disjoint from what the up-aggregate reads** | the convergence claim in `06 §4` | `propagation_spec_v1` §3 D.6 flags this as HIGH PRIORITY and explicitly forbids resolving it locally. This suite states its loops as **requiring** the arithmetic check, and claims no convergence it has not shown |

---

## 4. The uniform module contract

Every module in this suite is one row in this shape. It is `module_contracts.yaml` schema-2 plus the
four fields ED-IN-0200's hierarchy needs and schema-2 does not carry.

```yaml
module: <name>                     # unique across the game
parent: <subsystem>                # NEW — the hierarchy edge upward
scales: [<subset of the runtime four>]
tier: <place kind or null>         # NEW — the containment axis, orthogonal to scales
resolver: gate | d_sigma | accrual | derivation
remit: [<post kinds that may invoke this>]   # NEW — who may act
budget: {gauge: <gauge id>, cost: <int>} | null   # NEW — actions, never modifiers
consumes: [{type: <key type id>, from: [<module>]}]
emits:    [{type: <key type id>, terminal: <bool>}]
state:    [{name: <id>, bucket: entity|gauge|tag|post, writable: <bool>, owner: <module>}]
disclosure: [{of: <state id>, inputs: published, presentation: band|exact, trigger: hidden}]
```

**Four resolver kinds, and picking the wrong one is the most common defect the precedent survey
found.** The genre gates far more than this tree does; reaching for the kernel where a threshold is
the right tool is how a budget decision becomes a dice throw.

| resolver | use when | never use when |
|---|---|---|
| `gate` | eligibility, availability, a threshold on state the player can read | the outcome is genuinely uncertain |
| `d_sigma` | a contested outcome with a real chance of failing | the answer is determined by state already on the board |
| `accrual` | something fills up over time at a declared rate | the rate depends on a roll |
| `derivation` | a read-only aggregate | anything writes it |

**`remit` is what makes ED-IN-0201's clause 2 structural.** A module is invocable only by a post
whose remit names it. Two different holders of the same post kind get the same remit; two different
*post kinds* get different remits. The person changes the option set by *being eligible for
different modules*, which is the ruling's "different choices with the same information and options"
expressed as a gate rather than as a bonus.

---

## 5. Preconditions the whole suite sits on

Four things must be true before any module below can land. Each is a P0.

| # | Precondition | Why it is a precondition |
|---|---|---|
| **P0-1** | **`references/rendering_dispositions.yaml` must exist.** `key_type_registry_v30.md` §10 ratified it as a precondition on appending any new Key type, and the file does not exist, so the gate is report-only and every proposed key type is governed but unrecorded | This suite needs new key types (`post.granted`, `person.generated`, `faction.no_action`, and the rest of §6.3's minimum set). Appending them while the ratified precondition is unexecuted would be exactly the class of drift the precondition exists to stop. **Nothing here appends a key type until this file exists** |
| **P0-2** | **A dedicated RNG substream for person generation**, derived from the campaign seed and stashed on the world at creation, proven byte-identical against the existing seeded goldens before any person exists | Population re-phases every downstream draw on a shared stream. This is the only step in the entire suite that can be proved byte-identical, and it is the one that makes every later step attributable. It lands first or nothing after it can be measured |
| **P0-3** | **No mechanic in this suite may have a consequence that fires only on Partial**, and every degree-consuming table must be total over the four bands | The Partial band's probability falls monotonically across the practical pool range because its window is a fixed one-success width over a spread growing as √Pool. That is a kernel question (Q-3) and this suite does not get to change the kernel — so it declines to depend on the band whose width is under question. **A checked-in test computing all four band probabilities across the practical pool range is the guard**, and it is load-bearing on the game, not on this repository's process |
| **P0-4** | **Every guard this suite proposes must satisfy `CLAUDE.md` §0.1 point 5's load-bearing predicate.** The six it proposes are listed in `10_handoff_build_order.md` §4 with the game mechanic each is load-bearing on | The tree is fighting guard proliferation. Six new guards is a real cost and each has to earn it. None of them guards apparatus |

---

## 6. What lands in the registries

The hierarchy is only real if it is machine-read. Three registries carry it, and one is new.

| Registry | Gains | Read at runtime by |
|---|---|---|
| `references/module_contracts.yaml` | one `modules:` row per module below, in the §4 shape; one `composition_roles:` row per subsystem wrapper | `engine/substrate/composition.py` via the cooked `composition.json` |
| `references/descriptor_registry.yaml` | one row per Gauge instance: key, name, scale, floor, ceiling, decay coefficient, bands | `engine/substrate/descriptors.py` via the cooked `descriptors.json` |
| `systems/_architecture/key_type_registry_v30.md` | the minimum key-type set (§6.3), **after P0-1** | `engine/substrate/keys.py` via the cooked `key_types.json` |
| **`references/tier_registry.yaml`** *(new)* | place kinds, their parent edges, adjacency, and the accrual rate each kind supports | a new leaf reader under `engine/substrate/`, cooked by an exporter with a blocking `--check`, on the pattern the three existing cooked artifacts already set |

### 6.1 Why a new registry rather than a field on an old one

The containment ladder is not a descriptor (it is not a quantified-qualitative value), it is not a
module contract (it has no resolver), and it is not a key type. It is the map's shape. Adding it to
any of the three would put a fourth kind of thing in a registry that means something else — which is
the failure ED-IN-0200 names as *a hierarchy in shape and not in meaning*.

### 6.2 Every registry addition goes through an exporter with a blocking round-trip

The tree already has this pattern three times (`export_descriptors`, `export_key_types`,
`export_composition`), and it is the reason the authored surface can stay reviewable while code reads
a cooked artifact. The tier registry gets the same treatment or it does not land.

### 6.3 The minimum key-type set

Blocked on P0-1. Named here so the blocked work is specific rather than gestured at.

| type id | emitted by | carries |
|---|---|---|
| `person.generated` | 02 `cg.commit` | person id, the demand that caused it, capability provenance |
| `post.granted` | 04 `pm.appoint` | post id, holder, principal, the candidate set passed over |
| `post.revoked` | 04 `pm.recall`, `pm.tenure` | post id, prior holder, the tag cited as cause |
| `post.vacant` | 04 `pm.vacancy` | post id, tier node, reason |
| `faction.action_declined` | 05 `fa.gate` | faction, reason (`vacant_head` \| `budget_exhausted`) |
| `place.directive_issued` | 08 `sm.directive` | place, directive kind, principal |
| `place.directive_answered` | 08 `sm.respond` | place, response, degree where one was rolled |

Seven. Each has a producer in this suite and a consumer in this suite; none is declared speculatively.

---

## 7. The design principles this suite is held to

These are the constraints every document below was written against, and the ones a reviewer should
attack it on.

1. **Build bottom-up from primitives.** Four stored things, one write rule, and every mechanic is a
   composition. If a design needs a fifth kind of stored thing, that is a finding about the
   primitives, not a licence to add a field.
2. **Never special-case an entity or an outcome.** No faction, place or person may be named in code.
   Faction character comes from who holds the head post; place character comes from its tier kind and
   its gauges. A design that needs `if faction == X` is scripting drift and is rejected.
3. **A module is a registry row, not a branch.** Adding an action, a verb or a place kind is data.
   This is what makes the suite extensible without growing the engine.
4. **Gate where the answer is on the board; roll where it is genuinely uncertain.** The precedent
   survey's clearest structural finding is that the genre gates far more than this tree does.
5. **Publish every input. Publish a band, never a number. Never publish the trigger.** There is no
   GM: nobody narrates why a governor was passed over or why a faction declined to act. Disclosure is
   a contract owned once (E-2) and inherited, not a per-system choice — the alternative is one game
   with a loved half and a resented half, separated by nothing but visibility.
6. **Compress.** Every design below states its shipped set and its candidate set separately, and the
   shipped set is deliberately small. A five-layer apparatus that reproduces the feel of a one-line
   rule is a defect, not thoroughness.
7. **State the loop, name its cap, and do not claim a damper you have not measured.** Every design
   below that closes a feedback loop says so, names the bound, and where the gain is unmeasured says
   *unmeasured* rather than *damped*.
8. **The player is a person holding a post** (`01 §3.4`). There is no player entity, no player flag
   and no player-only module. Every module is invocable by the player exactly when a post they hold
   names it in its remit, and an unattended post resolves through the same module with its holder's
   own preferences supplying the choice — one engine, several entry points, not a second cheaper path.

---

## 8. Document map

| File | Covers | Primitives it introduces or instantiates |
|---|---|---|
| [`01_substrate_primitives.md`](01_substrate_primitives.md) | Entity, Tag, Post, Gauge; `derive_ob`; the disclosure block; **the player model**; the wrapper architecture | P-1 … P-4, E-1, E-2 |
| [`02_character_generation.md`](02_character_generation.md) | four-stage conditioned generation; authored-first resolution; determinism contract | P-1 |
| [`03_world_population.md`](03_world_population.md) | population as a function of posts and places; the bound; the idleness rule | P-1, P-3 |
| [`04_personnel_management.md`](04_personnel_management.md) | vacancy, candidate gate, appointment, tenure, audit, recall, succession, custody | P-3, P-2 |
| [`05_faction_actions.md`](05_faction_actions.md) | the C1 gate, the C2 decider, the action budget, the seven action families | P-3, P-4 |
| [`06_faction_management.md`](06_faction_management.md) | the faction as a composition; derived weight; fiscal stance; collapse by gate | P-4, derivation |
| [`07_places_and_settlements.md`](07_places_and_settlements.md) | the Place object, the tier registry, the gauge set, referential integrity | P-4, the tier registry |
| [`08_settlement_management.md`](08_settlement_management.md) | the Directive down-stroke, the verb up-stroke, pressure, the ledger-as-deck | P-4, P-2 |
| [`09_adjacent_systems.md`](09_adjacent_systems.md) | succession and collapse; units and the personnel↔battle seam; the deliberative body; the wrapper layer | all four |
| [`10_handoff_build_order.md`](10_handoff_build_order.md) | build order, impact classes, controls, falsifiers, what is blocked on what | — |
