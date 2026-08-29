# Greenfield Systems Suite v2 — Index, Hierarchy and Compliance Contract

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Version: v2.0 · Lane: IN (cross-cutting: FA, SE, WR, MB, PC, SC, FI)
## Supersedes: `proposals/2026-08-28-greenfield-systems-suite/` (v1, archived in place)
## Reads: v1 + [`ARCHIVED.md`](../2026-08-28-greenfield-systems-suite/ARCHIVED.md) ·
## `engine/substrate/{descriptors,composition,keys}.py` · `engine/autoload/dice_engine.py` ·
## canon design docs cited inline (`systems/fieldwork/`, `systems/factions/`, `systems/world/`,
## `systems/settlements/`, `systems/characters/`, `systems/overview/`)

**Reading order:** 00 Index → [01 Substrate · stored primitives](01_substrate_primitives.md) →
[01 part 2 · extensions and seams](01_substrate_primitives_part2.md) →
[02 Character Generation](02_character_generation.md) → [03 World Population](03_world_population.md) →
[04 Personnel](04_personnel_management.md) → [05 Faction Actions](05_faction_actions.md) →
[05 part 2](05_faction_actions_part2.md) →
[06 Faction Management](06_faction_management.md) → [06 part 2](06_faction_management_part2.md) →
[07 Places](07_places_and_settlements.md) →
[08 Settlement Management](08_settlement_management.md) → [09 Ambitions and Arcs](09_ambitions_and_arcs.md) →
[09 part 2](09_ambitions_and_arcs_part2.md) →
[10 The Slate](10_the_slate_and_salience.md) → [10 part 2](10_the_slate_and_salience_part2.md) →
[11 World Events](11_world_events.md) →
[12 Adjacent Systems](12_adjacent_systems.md) → [13 Handoff](13_handoff_build_order.md)

---

## 0. What this is, and what changed

v1 designed eight systems over four stored primitives. A read-only adversarial pass on 2026-08-29
found **six structural failures, five absences, four partials, one pass** against sixteen design
requirements. Two of the six were *errors* rather than omissions: the one write rule had been
extended to identity, and identity carried `place.kind` and `person.capability` — so settlements
could not grow and characters could not progress; and faction personality had been over-corrected to
nothing, leaving no institution for anyone to be in tension with.

v2 is v1 with **seven changes (§4)**, a **form bucket** on the entity primitive, and two constraints
promoted to the front of the document because they decide everything downstream: the **elegance
criterion (§1)** and the **playing-surface budget (§2)**.

**What it is not.**

- **Not a migration plan.** No disposition is proposed for any shipping module under `systems/`.
  `references/throughlines_meta.md:233-238` requires an independent steelman pass before any
  subtractive verdict; none has been run. **This suite proposes no deletions.**
- **Not canon, and it does not ratify on merge.** Under ED-1094 a merge normally ratifies a PROPOSED
  document. **This suite is held back explicitly and in full.** Merging this directory files it; it
  flips no `## Status:` line and changes no behaviour.
- **Not derived from `systems/` code.** No module, formula, constant or interface under `systems/`
  is used as a *source for a mechanism*. Reading `systems/` **design documents for setting facts**
  — caste, Knots, presences, the Altonian overlay — is permitted and expected, and every such fact
  below is cited by file and line. Where this suite needs a rule canon already owns, it **cites
  canon** rather than restating it as its own design.

**Under `CLAUDE.md` §0.05 this suite is reference.** Delete it and the game behaves identically. It
becomes mechanism only when §7's contracts are code and §9's registries carry their rows.

### 0.1 The scope limit, stated once for the whole suite

The pessimistic NERS audit that passed v1 was scoped to **resolution**, and the things it examined
did pass. It never asked whether the design could *express the game*, because the methodology it
follows is a rolling-engine diagnostic and that question is out of its scope. **None of v1's six
root causes is a NERS failure.**

So: **a resolution-scoped audit cannot ask whether a design expresses the game.** Every property
audit in this suite is bounded by that. A clean N/R/S/E verdict on a resolver says the resolver is
sound; it says nothing about whether the world it resolves is worth living in. The instrument for
the second question is the elegance criterion below, and it is a judgment, not a check.

---

## 1. The elegance criterion — what the **E** in NERS demands

Jordan, 2026-08-29:

> **Elegant means distill as much as possible without losing emergent possibilities or robust
> choosing for the player.**

Two-sided, and **both sides fail loudly**:

| failure | looks like | example from v1 |
|---|---|---|
| **under-distilled** | two objects doing one job · a mechanic that is a magnitude variant of another · apparatus a player never perceives | treaties as a `Debt` tag pair while faction enmity was an edge — two representations of one relationship |
| **over-distilled** | a possibility the world can no longer express · a season where the options are obvious or few | faction character reduced to the head post's convictions, so no institution could betray its purpose |

**Every object v2 adds must survive both.** §4 adds a form bucket, a bloc, a project, a slate, an
open edge registry, presences and an event table. **Each document states, in one line, the emergent
possibility lost if its object were cut.** If an author cannot name that possibility, the object is
cut and the document says so. **A change specified for v2 is not a licence.**

**The corollary that binds hardest on `09`, `10` and `11`:** prefer **one object with a registry of
kinds** over several objects. A project, an event and a candidate are *rows in their own tables*;
none becomes a subsystem. §9 holds the whole suite to **two new registry files**, and that ceiling
is the enforcement.

---

## 2. The playing-surface budget — the constraint that decides what v2 looks like

Jordan, 2026-08-29:

> **A common problem with games that try to be deep is that they have too many choices and actions
> for the player. Minimise the actual playing surface and keep a lot of the hard work under the
> hood, away from the player.**

This **resolves the apparent tension in §1.** Distillation and emergent richness are only opposed if
depth must be *exposed*. It need not be: **the substrate is rich, the surface is narrow.**

### 2.1 The classification every object must declare

| class | means | objects in this suite |
|---|---|---|
| **substrate** | the engine runs it; the player never operates it directly and may never see its name | form transitions · presences · blocs · NPC projects · life-path stages · salience · world-event rows · divergence · edge strain · memory · the four primitives themselves |
| **surface** | the player is asked to decide something | the Slate item and its responses · appointments · a small strategic action set · the player's own project |

**Default is `substrate`; `surface` must be argued for.** Blocs, presences, projects and divergence
are all substrate. A player never opens a bloc manager; they experience a bloc as *"the Ehrenwall
wing is against you and you can feel it in every appointment"* — a situation arriving on the Slate,
not a screen.

### 2.2 The hard budget

| axis | v1 | v2 target |
|---|---|---|
| distinct player verbs across the whole game | ~20 verb-fork leaves + 7 action families, all menu-selectable | **a single digit** |
| responses to any one situation | varies | **3–5, genuinely different in kind** |
| decisions per season | unbounded — every place × every verb | **the scene budget, and nothing else** |

**Depth comes from which situation arrives and what it is entangled with, never from menu breadth.**
Ten verbs against a rich, remembering, entangled place is a deeper game than forty verbs against a
stat block, and it is a smaller game to learn, build and balance.

### 2.3 What this forces, concretely

1. **`08` must SHRINK, not grow.** If a fork is only ever correct in one situation, it is not a
   choice — it is the situation, and it belongs under the hood.
2. **`05`'s seven action families are a strategic *capability* list, not a menu.** Most are invoked
   by NPC post-holders headlessly. What reaches the player is a Slate item.
3. **New objects must not add verbs.** Blocs, projects, presences and events add *situations*, and a
   situation costs the player nothing to learn until it arrives.
4. **Every document states its player-facing surface in one short table** — what the player is
   actually asked, and how often. **If a document's surface table is longer than its substrate
   table, that document has the ratio backwards.**
5. **The per-object test:** *could this be removed from the player's hands entirely and still change
   the game?* If yes, it is substrate. Only what fails that test is surface.

---

## 3. The hierarchy

ED-IN-0200 (Jordan, 2026-08-27, ruled and unexecuted): *"key contracts and module contracts etc need
to be explicitly defined in a centralized hierarchical manner."* The measured state it records is
three flat namespaces referencing each other by string, with no surface from which a reader — or the
Godot port — can descend from the game to a subsystem to a module to its Keys.

```
GAME
├── SCALE      — how big an event is.  personal · settlement · territory · peninsula
│               (the runtime enum; four members; a fifth raises)
└── TIER       — what contains what.   place kinds and their parent edges
    │           (an ORTHOGONAL axis, declared in the form registry)
    │
    └── SUBSYSTEM   one lane · one folder · ONE wrapper that owns all Key I/O for it
        │
        └── MODULE  Key IN → resolver → OUT(+Keys) + owned state
            │       a registry ROW, never a branch
            │
            ├── STATE   exactly one of four buckets — entity · gauge · tag · post
            ├── FORM    which form values this module may transition, and by which rows
            ├── KEYS    type ids from the cooked registry; nothing invented (§8, P0-1)
            ├── REMIT   which posts may invoke this module
            └── VIEW    what is disclosed of its state, and at what granularity
```

### 3.1 `scale ⟂ tier` — carried from v1 unchanged, and still the load-bearing move

Five scale vocabularies are live in the tree and only *personal* appears in all of them. Two
questions have been forced into one field: *what size of thing is this event about* and *what
administrative tier owns this*. The runtime enum answers the first and hard-refuses a fifth member;
the ruled containment ladder answers the second and has no representation anywhere.

| axis | answers | members | owner | mutable? |
|---|---|---|---|---|
| `scale` | how far an event's consequence reaches | the runtime four | the Key substrate | no — the enum is ruled |
| `tier` | what contains what | open, declared per place kind | `references/form_registry.yaml` (§9) | yes — it is data |

A Place declares both. A Key carries only `scale`. Nothing here proposes a fifth scale member.

⚠ **This routes around the collision; it does not resolve it.** ED-IN-0103 fork 1 holds vocabulary
unification for Jordan. The split is compatible with either outcome — if the enum is later widened,
`tier` collapses into it; if not, `tier` stays separate.

**v2 delta:** `tier` is now a **form** value on a place, not an identity field. That is what lets a
village become a town (§4, change A). The axis split is unchanged; what moved is which bucket it
lives in.

---

## 4. The four primitives, the form bucket, and the seven changes

### 4.1 The roster

| # | Primitive | Stores | Written by | Class |
|---|---|---|---|---|
| **P-1** | **Entity** — kinds `person · place · faction · unit · edge · bloc` (**six**) | an id, a kind, **immutable identity**, and a **mutable `form`** | created at load or by generation; identity never written; form only through a declared transition | substrate |
| **P-2** | **Tag** | durable discrete memory: `(owner, kind, key, value, ttl, provenance)` | `tag_append`; provenance required and non-empty | substrate |
| **P-3** | **Post** | a grantable, revocable commission: kind, tier node, principal, holder, remit, term, budget | `post_grant` / `post_revoke` only | substrate (the *holder's* option set is surface) |
| **P-4** | **Gauge** | a bounded, continuously-read, geometrically-decaying value | `gauge_deposit(delta, provenance)` — **no setter** | substrate (its *band* is the one thing routinely surfaced) |

Two engine extensions store nothing: **E-1** `derive_ob` beside `roll_pool` in
`engine/autoload/dice_engine.py`; **E-2** a `disclosure:` block on every state row.

### 4.2 The one write rule (v2) — four leaves, not three

> Every write terminates at exactly one of: **1.** a Gauge deposit · **2.** a Tag append ·
> **3.** a Post grant/revoke · **4.** a **form transition**.

**Identity is still never written. No aggregate is ever written.** v1's rule was correct about
aggregates and wrong about identity, because it had put `place.kind` and `person.capability` there.
The fourth leaf is not a loosening: a form transition is a **declared registry row with a gate, a
cost, an emission and — when reversible — a required hysteresis band** (`01 §2`). It is a narrower
channel than the three it joins, not a wider one.

*Emergent possibility lost if the form bucket were cut:* places and people would be frozen at
creation — no growth, no decline, no career, no ruin.

### 4.3 The seven changes

| # | Change | Class | Fixes | Emergent possibility lost if cut | Doc |
|---|---|---|---|---|---|
| **A** | **Split identity from form.** `place.kind`, `place.tier`, `person.capability`, `person.life_stage` move into a mutable `form` bucket reachable only by declared transitions | substrate | 1a, 3a, 1e | growth, decline, careers and ruin — a world that cannot change shape | 01, 02, 07 |
| **B** | **Project / Ambition** — a *composition* (tag + gauge + registry row) that lets an entity want something over time | substrate | 4a, 2d, 3d | nothing in the world would pursue anything; every event an incident, never a development | 09 |
| **C** | **Faction ethos** in faction identity; `appeal` reads institution **and** holder; their **divergence** is derived and gates something | substrate | 2c, 2a, 1c | an institution could never betray its own purpose, and no believer could be at odds with their own church | 05, 06 |
| **D** | **The Slate** — an attention budget and a salience ordering above everything that emits | **surface** (the only wholly-surface change) | 4c, 3d | nothing — cutting it *adds* volume. What is lost is the player's ability to perceive any of it | 10 |
| **E** | **Open the edge registry.** `relation` becomes registry-declared; **Knot** is a first-class edge kind read from canon; treaties become edges, not tag pairs | substrate | 1d, 4b, 1f | the Thread layer could not touch the social layer at all, and every relationship would be the same kind of thing | 01, 12 |
| **F** | **Setting first-class** — caste and heritage as identity with a gating matrix; **presences** on places; Thread Sensitivity as a person gauge | substrate | 1b, 1c, 3c, 3e | the game's central social injustice would be flavour text, and a place would be numbers with nobody living in it | 02, 04, 07 |
| **G** | **Exogenous world events** — bounded, conditioned registry rows arriving as Slate candidates | substrate | 3d, 3a | the world could only ever react to the player, never act on them | 11 |

**D is the only change that is pure distillation**, and it is the one that pays for the other six:
A–C and E–G all *increase* what the world produces, and without D that increase reaches the player
as volume. **Ship D or do not ship the rest.**

---

## 5. Rulings this suite executes

| Ruling | What it says | Where executed |
|---|---|---|
| **Jordan, 2026-08-29** | elegance = distill without losing emergent possibility or robust choosing | **§1**, and the one-line loss statement required of every object |
| **Jordan, 2026-08-29** | minimise the playing surface; keep the hard work under the hood | **§2**, the `substrate`/`surface` declaration, and `10`'s scene budget |
| **ED-IN-0201** (2026-08-28) | no leader → no faction action; no governor → no settlement governance; no commander → no battle. The person shapes *which* action from the same option set with the same information | **05 §1** (the gate) · **01 §4.3** and **05 §3** (`remit` as a gate on the option set, never a modifier on a roll) |
| **ED-IN-0200** (2026-08-27) | Key and module contracts defined centrally and hierarchically | **§3** and the contract shape in **§7** |
| **Jordan, 2026-08-14** | an obstacle is the target's corresponding score/2 plus instance-specific modifiers | **E-1**, `01 §6`. Every roll derives its obstacle through one owner |
| **Jordan, 2026-08-25** (ED-IN-0196) | TN is 7. Always | inherited; no design here names a TN. `dice_engine._require_tn7` refuses any other |
| **Jordan, 2026-08-14** (margin ladder) | `margin ≥ 3` Overwhelming · `≥ 1` Success · `[0,1)` Partial · `< 0` Failure | inherited; **no design here has a consequence firing only on Partial** (§8, P0-3) |
| **Jordan, 2026-08-14** | the attribute roster **will be ten**; nine ship, the tenth is unnamed | `01 §1.2` — capability is keyed on `descriptors.ATTRIBUTES`; nothing names an attribute literally |
| **Jordan, 2026-08-24** (conviction roster) | thirteen canonical Convictions, owned by `descriptor_registry.yaml`, resolved through `descriptors.resolve_conviction`, unknown names **raise** | `01 §1.2`, `02 §3.1`. **Virtue is one of the thirteen** — v2 adds no parallel virtue axis |
| **Jordan, 2026-07-13** | factions hold **people**; the number of people and the weight of their positions carry a faction's value | **06** — derived weight aggregates over held posts, not territory |
| `propagation_spec_v1` AU-1 | no aggregate is ever written | **the one write rule**, §4.2 |
| **ED-SC-0032** | a ladder extension injects a declared `BandExtension` whose only power is to veto an Overwhelming | **05 §6**; `dice_engine.BandExtension` is the existing owner |
| **ED-912** (2026-06-28) | Knot tiers are Distant/Close on a bidirectional −5…+5 bond-strain gauge; rupture at +5 | **cited, not designed** — `01 §7.5` reads it from `systems/fieldwork/knots_v30.md` |

### 5.1 Waited on — named, not guessed

| # | Question | Blocks | Why genuinely open |
|---|---|---|---|
| **Q-1** | **What a leader is, structurally** | `04` appointment; the C1 gate's first satisfaction at world-gen | ED-IN-0201 §22 leaves it open. This suite designs the post and the candidate gate; turn-zero eligibility is a content decision |
| **Q-2** | **"No commander, no battle" — gate or penalty** | `12 §2` | ED-IN-0201 §20 flags it as the one genuine ambiguity. This suite designs the **gate** and marks it as the reading it took |
| **Q-3** | **The Partial band collapses across the pool range** | nothing — P0-3 forbids depending on it | Changing band widths edits a ruled surface |
| **Q-4** | **The name of the faction-scale acceptance aggregate** | `06 §2` uses `faction.acceptance` provisionally | *Mandate* is live under three incompatible readings |
| **Q-5** | **Whether down-targeted place deltas are disjoint from what the up-aggregate reads** | the convergence claim in `06 §4` | `propagation_spec_v1` §3 D.6 flags it HIGH PRIORITY and forbids resolving it locally |
| **Q-6** | **Is the `−1 Coherence on rupture` rule live?** | nothing in this suite; it is canon's own open item | `systems/fieldwork/knots_v30.md:203` carries it `[UNVERIFIED post-ED-912]` — PP-632 was struck and ED-912 did not restate it. `01 §7.5` cites it as unverified and depends on nothing |
| **J-N** | **Does the substrate get cross-season latency at all?** Today it has none: `drain_tick` has zero production callers and `next_tick` **raises** on a non-empty queue, so the guard *prevents* cascades rather than scheduling them late | `09` projects and `11` world events — both must advance by **reading state at the boundary**, never by an emission that lands later | Filed by `audit/2026-08-08-world-churn-audit` Part III. Building one-hop-per-season carry is a design act, not a property in hand. `01 part 2 §9.1` states the constraint |
| **J-O** | **Should the Key substrate be promoted from telemetry spine to churn engine at all** — or kept as an append-only telemetry/causality log with churn driven at the boundary directly? | potentially **wholesale**: every part of this suite that leans on Key *consumption* | That audit's Part VII names it as the one open question that can invalidate a whole programme rather than one item, and notes the alternative *"is never weighed anywhere"*. Every v2 document that depends on Key consumption says so, so the affected parts stay identifiable |
| **ED-SC-0002** | **The Debate→Domain-Echo keying fork** — band-keyed (`scale_transitions §5.4`) vs genre-keyed (`social_contest §6`) vs composed | every echo this suite's wrappers emit from a resolved contest | Pre-existing P0 docket item. `audit/2026-07-08-contest-settlement-faction-interface` finds one ruling here unblocks ED-SC-0007 and closes the AU-5 seam its whole report traces. **This suite names the fork and takes no side** |

### 5.2 A note on the two rulings above that are NOT Jordan's

`J-N` and `J-O` are filed by a **read-only audit whose own header excludes its Part III and Part VI
from what merging it ratifies**. They are held findings, not rulings. They are listed with the
rulings because they gate work the same way, and because a design that quietly assumed cross-season
latency would be wrong regardless of who ruled on it — `01 part 2 §9.1` verified the no-latency
finding against the tree independently.

### 5.3 Overrides — everything this suite decides against, in one place

**A silent override is the corpus disease this suite exists to stop.** It is how the tree acquired
three definitions of Combat Pool and two of Mandate. Each document carries its own `## Overrides`
block; this table collects every one so each can be vetoed individually.

| # | What is overridden | Tier | Where | Decision |
|---|---|---|---|---|
| **O-1** | v1's "identity is immutable and carries `place.kind` / `person.capability`" | this suite's own v1 | `01 §Overrides` | It made settlements ungrowable and characters unprogressable. Corrected by the **form** bucket, not loosened |
| **O-2** | v1's closed six-member `relation` enum, **and this suite's own draft eight-kind table** | this suite's own v1 and draft | `01 §Overrides`, `01 §7.2` | **Both cut, superseded by `systems/npcs/npc_relational_graph_v30.md` (PP-724)**, which already ships six NPC↔NPC edge types with per-type semantics and a decision log. Re-deriving a worse taxonomy to keep authorship is the failure §1 names |
| **O-3** | v1's `disposition` gauge on every edge | this suite's own v1 | `01 §7.3` | For NPC↔NPC pairs that stores an aggregate over edge strengths, which v1's own write rule forbids. PP-724 derives it instead |
| **O-4** | **PP-724 §13's "relational edges file (separate)" storage decision** | **ratified-adjacent** (Class A, PROVISIONAL) | `01 §7.3` | **The one real point of disagreement.** Edges become entities in the general store rather than an NPC-only file, so one provenance rule, one disclosure contract and one Key surface cover every binding kind — which is what Part VI's *"shared Key surface"* asks for. **Only storage moves; every per-kind semantic stays where PP-724 put it** |
| **O-5** | v1's "distributor" framing of the subsystem wrapper | this suite's own v1 | `01 part 2 §9.1` | Reframed to Part III's **herald** criterion: the wrapper populates `targets[]` and routes nothing |
| **O-6** | The arc-compile calibration set — the 138 register arcs | **evacuated** | `09` | Neither obeyable nor overridable: the corpus is gone. The template + binding-slot grammar and the anti-oatmeal defence stand on their own; the missing calibration set is a **named gap**, not a step |

**Preserved by construction, not merely respected** — the three anti-unification rulings Part VI
cites, located and read rather than taken on summary: **ED-POL-11** (patronage ≠ Knot — *"do not
conflate"*), **PP-724 §0** (PC↔NPC and NPC↔NPC *"do not collapse into one mechanic"*), **PP-724
§3.3** (Knot strain and edge strain *"do not aggregate into one counter"*). All three forbid unifying
**semantics**; none forbids sharing **storage**, which is the distinction O-4 turns on.

**Adopted whole rather than overridden, on merit** — recorded because deciding *not* to override is
also a decision. The **Light Function** (ED-IN-0011, ratified) is taken entire, and the salience
sketch this suite first drafted is discarded as the weaker duplicate (`10 §0`). The **herald
criterion** (`world-churn-audit` Part III, held) is adopted entire (`01 part 2 §9.1`).

## 6. Design principles this suite is held to

1. **Build bottom-up from primitives.** Four stored things, one write rule with four leaves, every
   mechanic a composition. A need for a fifth stored kind is a finding about the primitives.
2. **Never special-case an entity or an outcome.** No faction, place or person named in code.
   A design needing `if faction == X` is scripting drift and is rejected. Faction character now comes
   from **ethos + who holds the posts**, which is the C fix, not from a branch.
3. **A module is a registry row, not a branch.** Adding an action, a verb, a place kind, a relation
   kind, an event or a project kind is **data**.
4. **Gate where the answer is on the board; roll where it is genuinely uncertain.** The precedent
   survey's clearest structural finding is that the genre gates far more than this tree does. **Every
   form transition is a gate, never a roll** — the uncertainty was in getting the gauges there.
5. **Publish every input. Publish a band, never a number. Never publish the trigger.** There is no
   GM. Disclosure is owned once (E-2) and inherited. **One exception is ruled the other way:** the
   caste gate is an *input* and is published in full (`04`, `F`) — concealing it would make the
   system's central injustice invisible.
6. **Compress, and say what you cut.** Every document states its shipped set and its candidate set
   separately, and names what it refused.
7. **State the loop, name its bound, and say "unmeasured" where the gain is unmeasured.**
8. **The player is a person holding a post** (`01 §4.4`). No player entity, no player flag, no
   player-only module. An unattended post resolves through the **same module run headless**, never a
   second cheaper path.
9. **The surface is narrow and the substrate is rich** (§2). New machinery adds situations, not
   verbs.

---

## 7. The uniform module contract

`module_contracts.yaml` schema-2 plus the fields ED-IN-0200's hierarchy needs and schema-2 does not
carry. **`form:` and `transitions:` are the v2 additions.**

```yaml
module: <name>                     # unique across the game
parent: <subsystem>                # the hierarchy edge upward
class: substrate | surface         # NEW (v2) — §2.1; default substrate
scales: [<subset of the runtime four>]
tier: <place kind or null>         # the containment axis, orthogonal to scales
resolver: gate | d_sigma | accrual | derivation
remit: [<post kinds that may invoke this>]        # who may act
budget: {gauge: <gauge id>, cost: <int>} | null   # actions, never modifiers
consumes: [{type: <key type id>, from: [<module>]}]
emits:    [{type: <key type id>, terminal: <bool>}]
state:    [{name: <id>, bucket: entity|gauge|tag|post, writable: <bool>, owner: <module>}]
form:     [{entity_kind: <kind>, field: <form field this module may transition>}]   # NEW (v2)
transitions: [<transition id from references/form_registry.yaml>]                   # NEW (v2)
ob_sites: [{target: <gauge id>, modifier_max: <int>, pool_max: <int>}]             # NEW (v2)
disclosure: [{of: <state id>, inputs: published, presentation: band|exact, trigger: hidden}]
```

**A module may only transition a form field it declares in `form:`, using a transition row it names
in `transitions:`.** That is what keeps the fourth write leaf auditable: the set of modules that can
change a place's tier is a grep over one field, not over the whole tree.

**`ob_sites:` is what makes `01 §6.1`'s commensurability gate evaluable, and without it that gate is
a rule nothing can check.** Every site that calls `derive_ob` declares three things: the gauge it
targets, the **maximum total modifier** it may add, and the **maximum pool** its own pool expression
can produce. All three are required, and each closes a specific hole the single owner found when it
corrected the gate's first draft:

- **`target`** — the gate needs a declared ceiling to divide. A gauge whose ceiling is undeclared, or
  declared `None`, is **unevaluable**, not passing. (`engine/engine_params/descriptors.json` declares
  `prac.thread_sensitivity` with `ceiling: None` against canon's 0–100 hard cap, which is exactly
  this hole and is the FI/IN lane's row to correct.)
- **`modifier_max`** — `derive_ob`'s `modifiers` argument is **unbounded in its signature**, so
  checking a bare ceiling proves nothing if a site may add +10. The bound must be declared, not
  inferred.
- **`pool_max`** — there is **no `POOL_MAX` constant in `engine/`**; `roll_pool` enforces only a
  minimum of 1. A site's maximum pool is a property of the pool expression that site declares, which
  is why the gate is **per-site** rather than global, and why a check stated at one pool size is not
  a check.

**Two sites are blocked on this today and are named so they cannot be forgotten:**
`presence.<institution>` has no declared numeric range — `07` must declare its ceiling — and `05`'s
`act.contest_influence` targets an incumbent's presence through `derive_ob`'s modifiers, so `05` must
declare that site's `modifier_max`. Until both land, that site **cannot be shown to pass the gate**,
and the honest status is unverifiable rather than fine.

**Four resolver kinds, and picking the wrong one is the most common defect the precedent survey
found.**

| resolver | use when | never use when |
|---|---|---|
| `gate` | eligibility, availability, a threshold on state the player can read — **including every form transition** | the outcome is genuinely uncertain |
| `d_sigma` | a contested outcome with a real chance of failing | the answer is determined by state already on the board |
| `accrual` | something fills up over time at a declared rate | the rate depends on a roll |
| `derivation` | a read-only aggregate — **including `divergence` and `salience`** | anything writes it |

**`remit` is what makes ED-IN-0201 clause 2 structural.** A module is invocable only by a post whose
remit names it. Two holders of the same post kind get the same remit; two different *post kinds* get
different remits. The person changes the option set by being eligible for different modules —
a gate, not a bonus. **The choice differs; the odds do not.**

---

### 7.1 Two schema hazards the authors found, recorded because the next reader will hit them

**A derived value has no legal bucket.** Every `state:` row must name `entity | gauge | tag | post`,
and a derivation is stored in none of them — it is recomputed at read. v1 wrote
`bucket: gauge, writable: false` and this suite keeps that shape, because inventing a fifth bucket to
describe a thing that is *not stored* would be the exact error `01` exists to prevent. The hazard is
that `writable: false` is a convention rather than a mechanism, so the guard is a falsifier instead:
**no state name declared `writable: false` may appear as a gauge id in
`references/descriptor_registry.yaml`.** If one does, a derivation has silently acquired storage, and
AU-1 is broken. `01` should give this a proper home; until it does, the falsifier is the whole
enforcement.

**⚠ "Standing" now means three different things, and one of them is new.** `06`'s author nearly
shipped a third meaning before catching it:

| the word | what it means | whose |
|---|---|---|
| `standing` | a **person** gauge | `01 §5.2` |
| Standing | the ratified **0–7 rank ladder** | `systems/factions/faction_politics_v30.md:38` |
| ~~standing~~ → **`footing`** | a **faction's** multi-scale presence at a node | `06 §4`, **renamed** |

He renamed his to `footing` and neither existing meaning is touched. Recorded here rather than only
in `06` because **this is precisely the disease that gave the tree three definitions of Combat Pool
and two of Mandate** — and it was caught by an author checking his own vocabulary against the tree,
which is the only thing that catches it. Any later document introducing a fourth sense of a word
already in `references/names_index.yaml` or `descriptor_registry.yaml` must rename, not disambiguate
by context.

## 8. Preconditions the whole suite sits on

| # | Precondition | Why |
|---|---|---|
| **P0-1** | **`references/rendering_dispositions.yaml` must exist.** `key_type_registry_v30.md` §10 ratified it as a precondition on appending any new Key type, and it does not exist, so the gate is report-only | This suite needs new key types (§9.2). Appending them while the ratified precondition is unexecuted is the drift the precondition exists to stop. **Nothing here appends a key type until this file exists** |
| **P0-2** | **A dedicated RNG substream for person generation**, derived from the campaign seed, stashed on the world at creation, proven byte-identical against the existing seeded goldens before any person exists | Population re-phases every downstream draw on a shared stream. It is the only step in the suite provable byte-identical, and it makes every later step attributable |
| **P0-3** | **No mechanic may have a consequence firing only on Partial**, and every degree-consuming table is total over the four bands | The Partial window is a fixed one-success width over a spread growing as √Pool, so its probability falls monotonically. That is Q-3, a kernel question this suite does not get to change — so it declines to depend on it. **The guard is a checked-in test computing all four band probabilities across the practical pool range** |
| **P0-4** | **Every guard proposed satisfies `CLAUDE.md` §0.1 point 5's load-bearing predicate**, and each names the game mechanic it is load-bearing on | The tree is fighting guard proliferation. `13 §4` lists them; none guards apparatus |
| **P0-5** | ***(new, v2)*** **The Slate (`10`) lands before or with any of B, F, G.** | A–C and E–G increase what the world produces. Landing a producer before the attention economy is how v1's `sm.business` manufactured undifferentiated volume, and it is not recoverable by tuning afterwards |

---

## 9. What lands in the registries

The hierarchy is real only if it is machine-read. **v2 adds exactly two registry files for the whole
suite, and that ceiling is binding on every later author** — it is §1's corollary enforced rather
than asserted. A later document that wants a new kind of thing adds a **block or a row**, not a file.

| Registry | Gains | Read at runtime by |
|---|---|---|
| `references/module_contracts.yaml` | one `modules:` row per module, in §7's shape; one `composition_roles:` row per subsystem wrapper | `engine/substrate/composition.py` via cooked `composition.json` |
| `references/descriptor_registry.yaml` | one row per Gauge instance: key, name, scale, floor, ceiling, `lambda`, `rest`, bands | `engine/substrate/descriptors.py` via cooked `descriptors.json` |
| `systems/_architecture/key_type_registry_v30.md` | the minimum key-type set (§9.2), **after P0-1** | `engine/substrate/keys.py` via cooked `key_types.json` |
| **`references/form_registry.yaml`** *(new)* | **the mutable-shape axis, in one file**: every entity kind's form vocabulary (place kinds and their tier/parent-edge rule, edge relation kinds and the states each admits, life stages, faction postures, unit kinds, bloc states) **plus every form-transition row** (§7, `01 §2`) | a new leaf reader under `engine/substrate/`, cooked by `tools/export_form_registry.py` with a blocking `--check` |
| **`references/content_registry.yaml`** *(new)* | **the catalogue of kinds the world can contain**: institution/presence kinds (`07`), project kinds (`09`), world-event rows (`11`), the `(institution, post_kind, caste) → open \| gated \| closed` matrix (`04`) — **keyed per institution, not globally: `(post_kind, caste)` alone is too coarse to express canon's own asymmetry**, since it would collapse `head` under the Crown and `head` under Niflhel to one verdict per caste and erase the Warden ladder's deliberate favouring of Southern Einhir. One sub-matrix per institution | the same pattern; one exporter, one blocking `--check` |

### 9.1 Why two files and not one, and not six

Four questions, four homes, and they mean different things: *what state is* (descriptors), *how it
resolves* (module contracts), *how it is shaped and how that shape changes* (form), *what the world
contains* (content). v1 proposed a `tier_registry.yaml`; **that is folded into the form registry**,
because the containment ladder is a place's form and separating it would put one axis in two files.
Collapsing form and content together would put a vocabulary and a catalogue in one place — the
failure ED-IN-0200 names as *a hierarchy in shape and not in meaning*. Splitting them further would
be six files for one idea.

**Both new registries go through an exporter with a blocking round-trip**, on the pattern the tree
already has three times (`export_descriptors`, `export_key_types`, `export_composition`). That is
what lets the authored surface stay reviewable while code reads a cooked artifact. **No round-trip,
no landing.**

### 9.2 The minimum key-type set

Blocked on P0-1. Named so the blocked work is specific.

| type id | emitted by | carries |
|---|---|---|
| `person.generated` | 02 `cg.commit` | person id, the demand that caused it, capability provenance, stages walked |
| `form.transitioned` | any module with a `transitions:` row | entity, kind, field, from, to, the transition id, the gate's inputs |
| `post.granted` | 04 `pm.appoint` | post id, holder, principal, the candidate set passed over, the caste gate's verdict per candidate |
| `post.revoked` | 04 `pm.recall`, `pm.tenure` | post id, prior holder, the tag cited as cause |
| `post.vacant` | 04 `pm.vacancy` | post id, tier node, reason |
| `faction.action_declined` | 05 `fa.gate` | faction, tier, reason (`vacant_post` \| `budget_exhausted`) |
| `edge.formed` / `edge.transitioned` | 01 `substrate.edge` | endpoints, relation, from-state, to-state, cause |
| ~~`project.declared` / `project.fired` / `project.lapsed`~~ → **`state.project_formed` only** | 09 `am.declare` | owner, project kind, target, terms |
| `world.event_fired` | 11 `we.fire` | event row id, place/faction targets, the preconditions that held |
| `slate.item_surfaced` | 10 `sl.truncate` | candidate id, salience components, rank, whether mandatory |
| `place.directive_issued` / `place.directive_answered` | 08 `sm.directive`, `sm.respond` | place, directive kind, principal; response and degree where one was rolled |

Each has a producer and a consumer **in this suite**; none is declared speculatively.

⚠ **CORRECTED — this table proposed three key types that already exist, and `09`'s author caught it.**
Verified against `systems/_architecture/key_type_registry_v30.md`: **`mechanical.project_advanced`
(`:446`), `state.project_completed` (`:691`) and `state.project_failed` (`:710`) are already
registered**, under ED-935, with live contract edges and canon's Procedure C behind them. Three of
the four project moments were never missing. Only **formation** is, and `state.project_formed` was
already proposed independently as G-29
(`audit/2026-08-11-world-schema-gap-audit/01_gap_register_part2.md:281`).

**So the work blocked on P0-1 is one key type, not four.** That is a real reduction in this suite's
cost, and it was found only because an author checked the registry instead of trusting this index.
Treat the rest of this table the same way: **it is a proposal, and every row in it should be checked
against the ratified registry before anyone appends anything.** The suite's own head being wrong
about what already exists is precisely the failure mode `§0.05` warns about — a design document is
reference, and the registry is the mechanism.

---

## 10. Document map

| File | Covers | Introduces |
|---|---|---|
| [`01_substrate_primitives.md`](01_substrate_primitives.md) | **The four stored primitives.** Entity + **form**; form transitions and hysteresis; the four-leaf write rule; Tag incl. **Memory**; Post; Gauge | A, P-1…P-4 |
| [`01_substrate_primitives_part2.md`](01_substrate_primitives_part2.md) | **The extensions and seams.** `derive_ob`; **the open edge registry and Knot** (with its `## Overrides` block); the disclosure contract; **the wrapper as a herald, not a distributor**; the no-latency constraint; the player model; the substrate's own contracts | E, E-1, E-2 |
| [`02_character_generation.md`](02_character_generation.md) | **life paths as stages**; caste and heritage as identity; beliefs vs convictions; virtues and flaws | A, F |
| [`03_world_population.md`](03_world_population.md) | population as a function of posts and places; the bound; the idleness rule; life-stage and lineage | — |
| [`04_personnel_management.md`](04_personnel_management.md) | vacancy, candidate gate + **the caste gating matrix**, appointment, tenure, audit, recall, succession, custody | F |
| [`05_faction_actions.md`](05_faction_actions.md) | the C1 gate **per tier**; ethos in `appeal`; the per-post budget; **`act.contest_influence`** | C |
| [`05_faction_actions_part2.md`](05_faction_actions_part2.md) | the eight action rows; resolution; effects constraints; J-N/J-O; contracts | C |
| [`06_faction_management.md`](06_faction_management.md) | ethos and **divergence**; **blocs**; multi-scale derivation; collapse by gate | C |
| [`06_faction_management_part2.md`](06_faction_management_part2.md) | the six political compositions; posture; **collapse by gate**; loops; the player surface | C |
| [`07_places_and_settlements.md`](07_places_and_settlements.md) | the Place object; **growth/decay transitions with hysteresis**; **presences**; strata; terrain | A, F |
| [`08_settlement_management.md`](08_settlement_management.md) | the Directive down-stroke; a **shrunken** verb set; investigation ⇄ infrastructure; business now **emits candidates** | D |
| [`09_ambitions_and_arcs.md`](09_ambitions_and_arcs.md) | **new** — project as a composition; declare/advance/fire/lapse; arcs as tag chains | B |
| [`09_ambitions_and_arcs_part2.md`](09_ambitions_and_arcs_part2.md) | the project registry; obstruction; arcs through `causes[]`; contracts; property audit | B |
| [`10_the_slate_and_salience.md`](10_the_slate_and_salience.md) | **new** — candidates, salience, truncation to the scene budget, headless auto-resolution | D |
| [`10_the_slate_and_salience_part2.md`](10_the_slate_and_salience_part2.md) | inertia without storage; J-N/J-O; the player surface; contracts; property audit | D |
| [`11_world_events.md`](11_world_events.md) | **new** — conditioned exogenous rows, rate bounds, reachability in both directions | G |
| [`12_adjacent_systems.md`](12_adjacent_systems.md) | succession and collapse; units and the personnel↔battle seam; terrain into the force seam; **treaty-as-edge**; the deliberative body | E |
| [`13_handoff_build_order.md`](13_handoff_build_order.md) | build order, impact classes, controls, falsifiers, guards and their load-bearing predicate, what is blocked on what | — |
