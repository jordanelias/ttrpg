# Epistemic Propositions with Provenance — the belief layer, and where it lives

## Status: DESIGN CALLS RULED 2026-08-18 (§10) — all five §8 questions answered, four confirming the design as drafted and P1 taking the population-scale branch; the DESIGN remains PROPOSED and unbuilt. Jordan-directed. No `.py` touched, no Key type registered, no registry amended. Every tree claim carries file:line.

**Date:** 2026-08-18 · **Lane:** FI (field investigation) · **IDs:** none allocated (design-only)
**Directive:** *"I want epistemic proposition about the world to be available alongside provenance references."* — Jordan, 2026-08-18
**Follows:** `proposals/2026-08-18-fieldwork-architecture-and-nonadversarial-play.md` §11.2 (merged PROPOSED, PR #318) — **this document supersedes that section's "adopt `state.belief_revised`" leg, which a read-only audit falsified.**

---

## §1 WHAT THE DIRECTIVE SETTLES

The prior proposal argued a **belief layer** was the one genuinely absent primitive, and proposed
adopting `state.belief_revised` for it. An adversarial read-only pass falsified that. The directive
resolves the question in the other direction and adds the requirement that makes it tractable:
**propositions carry provenance.**

Three things follow immediately, and the third is the one that pays:

1. A proposition must be **structured**, not prose — otherwise nothing can compare, contradict or corroborate it.
2. A proposition must be **held per agent, with confidence** — otherwise two characters cannot disagree.
3. A proposition with provenance is **the same object as a scripted hook's condition** (§4). Jordan's *"it's just composites of worldly facts"* and *"certain worldly facts she must navigate"* describe the engine's side of exactly this object; a belief is an agent's side of it.

## §2 WHY NOT `state.belief_revised` — verified, briefly

| Property | `state.belief_revised` (registry :1115-1135) | Needed |
|---|---|---|
| Structure | `prior_belief` / `new_belief` — **"short string"** | machine-comparable proposition |
| Confidence | **none** | per-agent, graded |
| Semantics | the **PC creed-Belief beat** — `fieldwork_socializing.md:104-110` is the Belief *Momentum* economy (aligned / challenging / betraying), `permanence: indelible`, "Triggers Tier 2 cut scene" | an epistemic claim that can be **wrong** and **revised** |
| Provenance | `triggering_keys` (optional) — the one compatible part | required, and load-bearing |

It is also **inert**: zero emitters, and its single code consumer (`engine/cross_scale/articulation.py:126`)
subscribes to the type and routes to `stubwire.stub_resolve` without reading the payload. Amending
its `required_payload_fields` would be a **Class A supersession event** (registry §10) *and* would
fold two distinct concepts into one type.

**Disposition: leave `state.belief_revised` as the creed-Belief beat it was registered for.** The
epistemic layer is a separate, new thing sitting alongside it.

## §3 THE DESIGN

### §3.1 `Proposition` — a structured claim, content-addressed

```
Proposition:
  id            # content-addressed hash of (subject, predicate, object, qualifier)
  subject       # entity ref: actor_id | settlement_id | faction_id | territory_id | key_id
  predicate     # verb from a CLOSED registry (see §6) — e.g. was_at, killed, owes,
                #   conspired_with, diverted, holds_office, caused
  object        # entity ref | scalar | null
  qualifier     # optional {season_index, location_id} — the when/where
```

**Content-addressing is the whole trick.** Two agents who hold the same claim hold the *same*
`Proposition.id`, computed rather than coordinated. That single property is what free strings cannot
give and what everything downstream needs: agreement is id-equality, contradiction is
id-equality-with-opposed-stance, corroboration is provenance-union over one id. It is also what lets
a parliamentary argument and an investigator's finding refer to the same fact.

### §3.2 `Holding` — the per-agent belief, with provenance

```
Holding:
  holder          # actor_id — the believer
  prop_id         # -> Proposition.id
  stance          # asserts | denies | suspects
  confidence      # int [1,5]   — the SAME ladder as state.opinion_revised, deliberately not a new one
  support_refs    # [key_id]    — PROVENANCE. the Keys this holder has that bear on the claim
  acquired_season # int
```

`stance` is what makes disagreement representable without duplicating the proposition: *A asserts P,
B denies P* is one `prop_id`, two holdings. `suspects` is the low-confidence hedge that keeps a lead
in the Case Board before it is assertable.

**`confidence` reuses `state.opinion_revised`'s `int [1,5]`** (registry :1162-1163) rather than
inventing a second ladder — the §11.8 fragmentation finding applied preventively.

### §3.3 Provenance and independence — what makes confidence honest

`support_refs` are Key ids, so a holding's support is auditable against the KeyLog. Confidence is
then not a vibe:

> **independent support = the number of `support_refs` whose `Key.causes` ancestries are disjoint.**

Two rumours traceable to one witnessing are **one** support, not two. That is the Heaven's Vault
corroboration ladder made mechanical, and it is the single owner the prior proposal called `W3`,
now with something real to read. It also gives the engine a check rather than a guess: a holding
whose `confidence` exceeds its independent-support count is a character who is **overconfident** —
which is a characterisation, not a bug, and should be *representable* rather than prevented.

⚠ **This is the standing blocker.** `Key.causes` is populated at three non-test sites and two of
them pass `causes=[]` (`echo_transport.py:317`, `parliamentary_transfer.py:166`,
`faction_action.py:389`). Independence is computable only once emitters populate ancestry.

### §3.4 Truth is separate — and this is where it unifies

A `Proposition` says nothing about whether it is **true**. Truth is whether the claim obtains in
world state, evaluated by the engine. That gives three distinct things over one grammar:

| | Who holds it | What it is |
|---|---|---|
| **Fact** | the world | the proposition obtains in world state |
| **Belief** | an agent | a `Holding` — may be false, is revisable, has provenance |
| **Condition** | a scripted hook | a proposition (or conjunction) the **engine** evaluates |

**A Crown Claim's `Hafenmark Mandate ≥ 4`, an investigator's finding, and a parliamentary argument's
premise are the same kind of object.** That is the ruled hook grammar and the belief layer meeting
in one place, and it is why *"argue and present what to do about the current state of things and
why"* becomes mechanical rather than aspirational: an argument is a set of `prop_id`s, each with a
provenance the opposition can attack.

## §4 THE HOME — `npc_memory`, which already specifies this and is empty

Not a new module. `references/module_contracts.yaml` declares `npc_memory` with:

- `doc: null`, `sim_module: none`, `state: []`, `emits: []` — declared and **entirely unbuilt** (its own note: *"find/grep for npc_memory* across the tree returns nothing"*);
- `resolver: state_reader` with the comment **"Memory store written from Keys; queried by Procedures"** — which *is* this design, written down in 2026-06-10;
- `consumes:` `scene.gossip`, `scene.interaction`, `state.concern_resolved`, `state.opinion_revised` — already the right inputs;
- `gap_notes: "home doc unlocated — Memory schema ... standalone spec [GAP]"`.

So the belief layer's home is one of the nine `doc: null` modules, and authoring it **closes that
gap rather than adding a tenth**. Proposed contract delta:

```yaml
- module: npc_memory
  doc: systems/npcs/<new — the standalone Memory spec the gap_note asks for>
  sim_module: systems/npcs/sim/memory.py
  resolver: state_reader          # unchanged; the [ASSUMPTION] tag can drop once the doc lands
  consumes:
    - {type: "scene.gossip", from: [npc_behavior]}          # unchanged
    - {type: "scene.interaction", from: [npc_behavior]}     # unchanged
    - {type: "state.concern_resolved", from: [npc_behavior]}# unchanged
    - {type: "state.opinion_revised", from: [npc_behavior]} # unchanged
    - {type: "scene.witness", from: [scene_slate, npc_behavior]}   # NEW — the observation edge
    - {type: "scene.evidence_gained", from: [fieldwork_action]}    # NEW (⊕ per the prior proposal)
  emits:
    - {type: "state.proposition_revised", terminal: false}  # ⊕ NEW — see §5
  state:
    - {name: "Proposition store", bucket: registry, writable: true}   # §3.1, world-scoped, content-addressed
    - {name: "Holdings", bucket: registry, writable: true}            # §3.2, per (holder, prop_id)
```

## §5 THE KEY TYPE — `state.proposition_revised`, modeled on `state.opinion_revised`

The store is **module state** because a Key is append-only and a belief must be revisable; Keys
**journal** revisions to it. Patterned deliberately on the one registered type that already carries
confidence *and* provenance:

```yaml
### state.proposition_revised
description: An agent's holding on a world-proposition changed — stance, confidence, or support.
             Epistemic (revisable, may be false); distinct from state.belief_revised, which is the
             creed-Belief character beat (fieldwork_socializing §5.5).
required_payload_fields:
  - holder                  # actor_id
  - prop_id                 # content-addressed proposition id
  - stance_before           # asserts | denies | suspects | none
  - stance_after            # asserts | denies | suspects | none
  - confidence_before       # int [0,5]   (0 = not held)
  - confidence_after        # int [0,5]
optional_payload_fields:
  - support_refs_added      # [key_id]    PROVENANCE — the directive's requirement
  - support_refs_dropped    # [key_id]    a retraction is as real as an acquisition
  - independent_support     # int         computed at emit; null while causes[] is unpopulated
default_scale_signature: [personal]
default_permanence: persistent          # NOT indelible — this is the revisable layer
default_time_horizon: near
default_visibility: private_observers=[holder]     # the epistemological barrier, by default
class: B
```

`default_visibility: private_observers=[holder]` is the important line: **P-08 is enforced by the
type's default**, mirroring `state.opinion_revised`'s `private_observers=[emitter, opinion_subject]`.

## §6 TWO REGISTRIES THIS NEEDS

1. **A closed predicate vocabulary** (§3.1's `predicate`). Free-form predicates re-create the
   free-string problem one level down. It belongs beside the other centralized vocabularies —
   `references/descriptor_registry.yaml` governs stats, `names_index.yaml` governs names; predicates
   want the same treatment. Start deliberately small; every predicate must be **engine-evaluable**
   against world state, or it cannot serve as a hook condition (§3.4).
2. **A `references/rendering_dispositions.yaml` row**, which registry §10 (RATIFIED 2026-07-07,
   ED-IN-0026) makes a **mandatory precondition** for any new type: *"how does the player ever see
   this?"* ⚠ **That file does not exist in the tree**, so the gate is warn-only today — but the
   question still has an answer here, and it is a good one: **RENDERED-RICH — the Case Board.** A
   proposition store with per-agent holdings, stances and provenance *is* the Case Board's data
   model, and its known-unknowns are propositions held at `suspects` whose support is thin.

## §7 WHAT THIS DOES NOT CHANGE

- `state.belief_revised` keeps its registered meaning and its `indelible` permanence. No Class A amendment.
- `state.opinion_revised` is untouched; this reuses its confidence ladder rather than competing.
- No degree-ladder change. `degree_from_net` still owns resolution; a proposition records a claim, not a roll.
- No new module. `npc_memory` was already declared for this.

## §8 THE CALLS THAT ARE JORDAN'S

| # | Question | Options and cost |
|---|---|---|
| **P1** | **Do NPCs hold propositions, or only the player?** | Player-only is far cheaper and makes the Case Board a UI. NPC-held is what makes gossip, lying and interrogation real — and `npc_memory` is an *NPC* module, which argues for both. Cost of NPC-held: a holdings store scaling with population. |
| **P2** | **Is `suspects` a third stance, or just low confidence?** | A stance is cleaner for the Case Board's known-unknowns; confidence-only is one less concept. |
| **P3** | **May a character hold a proposition whose support is zero** (rumour, prejudice, fabrication)? | Yes makes lying and manufactured evidence representable — probably essential for a game with Exposure and covert action. No makes provenance total and the system tidier. |
| **P4** | **Who owns the predicate registry** — FI, IN, or a shared vocabulary lane? It gates hook conditions as well as beliefs, so it is not really FI's. |
| **P5** | **Does the engine ever tell the player a holding is false?** | The prior proposal's Q5 in a new form, now concrete: with structured propositions, confirmation becomes mechanically possible, and P-08 argues against it. |

## §9 WHAT WOULD FALSIFY THIS

| Claim | Falsifier | Ran? |
|---|---|---|
| `state.belief_revised` is free strings, no confidence, creed semantics | read registry :1115-1135 + `fieldwork_socializing.md:104-110` | ✅ |
| It is inert — no emitters, consumer reads no payload | `articulation.py:126-147`; grep `prior_belief`/`new_belief` tree-wide | ✅ |
| `state.opinion_revised` carries `confidence int [1,5]` + `driver_memory_refs` | read registry :1156-1177 | ✅ |
| `npc_memory` is declared, unbuilt, and its resolver comment states this design | read `module_contracts.yaml` npc_memory entry in full | ✅ |
| `rendering_dispositions.yaml` does not exist, so §10's precondition is warn-only | `find . -name "rendering_dispositions*"` → no result | ✅ |
| `Key.causes` is unpopulated, so independence is not yet computable | grep `causes=` over `engine/` + `systems/` → 3 sites, 2 empty | ✅ |
| **Unverified:** that a content-addressed id is stable across the qualifier's optional fields | not designed in detail — hashing rule needs specifying before implementation, or two agents will hash the same claim differently and the whole scheme silently fails | ❌ **the first thing to nail down** |

**The claim most likely to be wrong:** that a closed predicate vocabulary can stay small enough to
be evaluable and large enough to be expressive. If it cannot, propositions degrade toward free text
and this design decays into the thing it replaced. The cheap test is to try to express, in
predicates alone, the ten facts a player would most want to assert in Jordan's drought→donation
chain and in a Crown Claim.

---

# §10 RULINGS LANDED — Jordan, 2026-08-18

All five §8 questions ruled. **Four confirm the design as drafted; one changes the home's scope.**

| # | Ruled | Effect on this design |
|---|---|---|
| **P1** | **NPCs hold propositions too** | The largest call, and it takes the expensive branch deliberately. Every NPC carries Holdings, so gossip propagation, lying, contradictory testimony and interrogation become mechanical rather than decorative. `npc_memory` being an *NPC* module is now load-bearing rather than incidental. **Obligation created:** NPE-generated NPCs need default holdings at spawn, and the store scales with population — see §10.2 |
| **P2** | **`suspects` is a third stance** | §3.2 stands as drafted. The Case Board gets a real category for a live lead, which is what makes known-unknowns renderable (the Outer Wilds property §6 claims as its rendering disposition) rather than derived from a number |
| **P3** | **Support may be empty** | §3.3 stands, and the permissive branch is ruled: a Holding may cite zero Keys. Rumour, prejudice and fabrication are representable, which a game with Exposure, Cover and `da.covert_betrayal` needs. **Consequence:** "do you believe it?" and "how do you know?" are now genuinely separate queries — the Case Board must not imply provenance where none exists |
| **P4** | **Split the predicate registry** | IN owns the **engine-evaluable** predicates (those a scripted hook's condition may test against world state); FI owns the wider **claim-only** set usable in beliefs and arguments. Two registries plus a promotion rule — heavier than §6 proposed, but it matches the two genuinely different obligations: a hook predicate must be computable, a claim predicate need only be *sayable* |
| **P5** | **Confirmation only through consequence** | No verdict surface. Act on a finding and the world's response reveals whether you were right. P-08 is preserved exactly as §3.4 wants it, and closure arrives without a truth oracle. **Obligation:** the Finding → `Leverage` / `Dossier` consequence paths must be legible enough to *read as* feedback, or the design silently becomes "never confirmed" |

## §10.1 A ruling from the fieldwork docket lands here too

**Q9 — per-NPC Disposition joins Holdings in `npc_memory`.** Relational state and epistemic state
share a home, so one module answers both *"what does she know?"* and *"what does she think of me?"*

⚠ **This stretches the contract's own framing.** `module_contracts.yaml`'s `npc_memory` resolver
comment reads *"Memory store written from Keys; queried by Procedures"* — accurate for propositions,
too narrow for a relational hub. **When the standalone Memory spec is authored (the module's own
`gap_notes` asks for it), that line must be re-worded**, or the next reader inherits a description
that no longer covers what the module holds. Filed as part of §4's contract delta.

## §10.2 What P1 obliges that this document did not cost

Population-scale Holdings is a real cost the draft assumed away, and it should be named before
anyone builds:

- **Default holdings at spawn.** `npe.generate_npc` must seed something. The cheap answer is nothing (an NPC believes only what they observe); the expensive one is demographic priors so a Church cleric starts believing Church things. Not ruled — flagged.
- **Growth is unbounded without a forgetting rule.** Holdings accumulate per NPC per proposition. `Key.permanence` and confidence decay are the two levers already in the substrate; which applies is undecided.
- **Only the belief layer is population-scale.** The `Proposition` store is shared and content-addressed, so it grows with distinct *claims*, not with `population × claims`. That is the design property that makes P1 affordable, and it is another argument for content-addressing beyond comparability.

## §10.3 Still the first thing to nail down

Unchanged by the rulings: **the content-address hashing rule is unspecified** (§9). If two agents
hash the same claim differently, every property this design rests on fails silently — no
comparison, no contradiction detection, no corroboration. With P1 ruled, this now matters across
the whole NPC population rather than for one player. Specify it before any implementation.
