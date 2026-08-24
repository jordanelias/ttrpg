# Suite 04 — What to Wire, Where, and What Is Missing

**Status:** WIRING ANALYSIS. This is the engineering counterpart to Suite 02's census: 02 measures
what the content layer holds, 04 says what would have to connect for the engine to reach it, and
which of those connections are *coded but uncalled*, *stubbed*, *designed only*, or *unspecified*.

**Status vocabulary**, used throughout:

| term | meaning |
|---|---|
| **CODED** | Implemented and reached by a live path |
| **CODED-BUT-UNREACHED** | Implemented, correct, and called by nothing |
| **STUBBED** | A typed no-op that returns a well-formed empty result |
| **DESIGNED-ONLY** | Specified in a design document; no code |
| **UNSPECIFIED** | Neither coded nor specified — someone must decide first |

The distinction that matters most is **CODED-BUT-UNREACHED vs UNSPECIFIED**. The first is a call site;
the second is a design session. Conflating them is how "we're one function away" gets said about work
that has not been designed.

---

## §1 The person layer is the root

Five separate chains terminate at the same missing piece, and it is worth stating plainly before any
table: **`references/npc_registry.yaml` has no loader.** 46 authored characters, `world.npcs == {}`,
and the only Python that opens the file is a parse test and a documentation generator.

What that single absence blocks:

1. **Conviction scarring** — `record_scar` needs an actor with state; there are no actors.
2. **Knot formation** — `mc_v18.py:204-209` stubwires it; the participants do not exist.
3. **Settlement habitation** — `Settlement.npc_ids` is empty on all 37 (Suite 02 §3); the only writer
   in the tree is a test fixture (`goldenfurt_fixture.py:89`), and `get_npcs_in_territory` has zero
   callers.
4. **Social contest at personal scale** — the live path derives contest parties from *aggregate
   faction stats* (`scene_dispatch.py:120-138`: `(max(1, round(f.L)), max(1, round(7.0 - f.Sta)))`),
   i.e. two bare integers, because no concrete actors are available.
5. **Any narrative render** — a chronicle of events between nobody.

**But the loader is not the gap.** This session initially published *"the single missing artifact is a
loader"* and it is wrong, for a reason worth recording: the registry's fields and the engine's `NPC`
dataclass do not correspond.

```
NPC (systems/world/sim/npe.py:114-134)  — 12 fields, 5 conviction axes.
   has: stance, worldview, volatility, compromise, deviation
   lacks: name, goals, stats, ts, coherence

npc_registry.yaml entry                 — has all of the latter, none of the former.
Overlap that maps cleanly: faction, territory.
```

`world.npcs` is keyed by territory (`game_state.py:188`), and only 7 of 46 characters name a territory
— three of those to a hole (Suite 02 §2.5). `ConvictionState` (`conviction.py:108-123`) has no weight
field, while the registry stores weighted primaries.

**So the gap is UNSPECIFIED, not CODED-BUT-UNREACHED.** Somebody has to decide what a character *is*
at runtime — whether the authored record and the simulation record are one object or two, and if two,
what maps between them. A loader written before that decision would be writing the decision.

---

## §2 The sixteen design gaps

Ordered by what they block. "Blocked on" names the decision, not the code.

| # | Gap | Status | Blocked on |
|---|---|---|---|
| 1 | Registry record ↔ runtime `NPC` correspondence | **UNSPECIFIED** | §1 — the root |
| 2 | Conviction weights have no home in `ConvictionState` | **UNSPECIFIED** | Gap 1 |
| 3 | Strategic `faction.Mil` → mass-battle cells | **UNSPECIFIED** | Suite 01 §1.2; blocks Ruling A |
| 4 | Contest `resistance` — declared, unplumbed | **DESIGNED-ONLY** | What resistance modifies |
| 5 | Armature unreachable through the contest wrapper | **CODED-BUT-UNREACHED** | Call-site shape |
| 6 | Chronicle / narrative render | **UNSPECIFIED** | §4 — no consumer, no home |
| 7 | Belief layer | **DESIGNED-ONLY** | The 2026-08-18 epistemic proposal, unratified |
| 8 | `state.succession` — nothing emits it | **UNSPECIFIED** | `Faction` has no leader field |
| 9 | Settlement ↔ NPC linkage | **CODED-BUT-UNREACHED** | Gap 1 |
| 10 | Settlement economy | **UNSPECIFIED** | `doc: null` in module contracts |
| 11 | `engine_clock` — the temporal spine | **UNSPECIFIED** | `doc: null`; no home design doc |
| 12 | Domain actions home | **UNSPECIFIED** | ED-FA-0002, open on the workplan |
| 13 | Relational graph edges | **DESIGNED-ONLY** | No edge data exists in any format |
| 14 | Voice canon has no consumer | **DESIGNED-ONLY** | Suite 03 §6 |
| 15 | Godot skeleton spine (`BaseEngine`, `Key`, `KeyBus`, …) | **UNSPECIFIED** | CLAUDE.md §6 — defined nowhere |
| 16 | Scene actor derivation from aggregate state | **DESIGNED-ONLY** | `scene_dispatch.py:18-30` names it a deliberate boundary |

**Nine of sixteen are UNSPECIFIED.** That is the shape of the project right now: the blocker is
overwhelmingly design, not implementation. Only gaps 5 and 9 are call-site work.

---

## §3 Orphaned mechanisms — coded, correct, unreachable

These are the highest-value entries in the whole session, because each is finished work sitting one
call away from being live. Every one verified by AST sweep or by reading.

### §3.1 The Treaty system is wholly inert — and cannot work if wired

`systems/factions/sim/treaty.py` implements treaty registration, active-treaty query and expiration.
An AST sweep for calls to `process_treaty_expirations`, `register_treaty` and `get_active_treaties`
across every live `.py` in the tree returns:

```
NO CALLERS ANYWHERE — including tests.
```

**And there is a defect waiting inside it.** `treaty.py:137-138`:

```python
roll = rng.random() if rng else 0.95   # default to high-lapse if no rng
lapsed = roll < lapse_rate
```

Canonical lapse rates are 0.90–0.95. With no rng the roll is fixed at 0.95, so `0.95 < 0.90..0.95` is
**always False** and **no treaty can ever lapse**. The comment says "default to high-lapse"; the line
does the exact opposite. A comment that inverts its own code, in a module nothing calls, so nothing
has ever noticed.

A third issue on wiring: `register_treaty:150` keys the store by `tuple(sorted(parties))`, while
`game_state.py:190` documents the World's treaty store as **frozenset**-keyed. Two key types for one
store.

*Also worth recording:* `crown_initiative.py` contains no treaty formation. Its single mention
(`:195`) is a precondition in a docstring. Diplomacy has no producer.

### §3.2 The Mandate penalty is permanent, and says it is temporary

`systems/social_contest/sim/parliamentary_vote.py:207-219`. On §10 Total Victory or Total Defeat, the
losing coalition's dominant faction takes Mandate −1 via `adjust("L", ...)` — a direct stat mutation —
and appends the note:

> *"[one-season penalty; temporary-modifier restoration deferred to season_manager]"*

`engine/autoload/season_manager.py` defines exactly two functions: `advance_season` and
`check_arc_boundary`. `Faction.reset_seasonal` (`game_state.py:134-136`) clears two booleans. **There
is no temporary-modifier machinery anywhere in the engine.**

So the penalty is permanent and **compounds across the campaign** — a balance defect on a live path,
not a dormant one, and it is one of the few things in this document that changes campaign outcomes
today.

### §3.3 The settlement memory layer has zero callers

Covered in Suite 02 §3.2 and repeated here because it belongs to this list.
`systems/settlements/sim/ledger.py` — Precedent / Grudge / Debt / Reputation / Leverage, deduped, TTL'd,
surviving governor succession by design. AST sweep: `Settlement.add_tag` / `has_tag` / `tags` have
**zero callers anywhere, including tests**; the only writers of any kind are under
`tools/sim_harness/adapters/pr119_governance/`, and one of those writes an unratified `"Compact"`
kind — which `ledger_add` accepts, because it never validates `kind` against `TAG_KINDS`.

This is the single most consequential dead module for narrative texture: it is the mechanism by which
a place would remember what was done to it.

### §3.4 `state.succession` — three layers deep

Nothing emits it. `articulation.py:119` lists it in the consumer roster; there is one test and one tool
docstring. Below that: `Faction` has **no leader field** at all, so there is nothing to succeed. The
gap is not a missing emitter — it is a missing entity.

### §3.5 Smaller orphans, verified

| Site | Defect |
|---|---|
| `systems/factions/sim/mass_seizure.py:291-293` | Writes a canonical 0–3 integer into `t.accord`, a continuous `ACCORD_MAP` field. Wrong scale. The sibling site (`parliamentary_transfer.py:278`) is correct. The code comment at `:291-292` self-admits it. |
| `systems/settlements/sim/temperaments.py:117 vs :153-158` | Read/write asymmetry — reads via `_drift_store()` (no world), writes via `_drift_store(world)`. CLAUDE.md §0.1 point 1, exactly. |
| `systems/world/sim/npe.py:283, 296-299` | `hidden_allegiance` assigned to a local the constructor omits — voids one of five deviation branches (~20% of the behaviour). |
| `systems/world/sim/npe.py:261-262` | Comment says "weighted by faction"; the code is an unweighted `rng.choice`. |
| `systems/settlements/sim/infrastructure.py:53` | `CI_GAIN_TEMPLAR` dead. `ci_track.py:37` declares the dependency in prose and imports nothing. |
| `engine/cross_scale/scene_dispatch.py:313` | Cites `dictionaries._APPEAL_TO_GENRE`, which exists nowhere. Nearest real symbol is `rhetoric._GROUND_TO_GENRE` (`rhetoric.py:91`). |
| `systems/npcs/faction_canon_v30.md:6-7` | Carries `Status: CANONICAL` and `Status: PROVISIONAL` on consecutive lines. |
| `engine/autoload/echo_transport.py:246-247` | Accord-echo fires zero times — the two live echo context dicts (`scene_dispatch.py:342-343`, `parliamentary_bridge.py:207-211`) carry neither `scene_outcome` nor `target_settlement`. |

---

## §4 The chronicle chain

The narrative render is Gap 6, and it is the one place where "almost wired" is close to true — so it
is worth stating precisely how close, and where it stops.

Structurally, the chain exists at every link: `wrapper.py:229-230` builds a Bout and binds it to an
unused `_bout`; the Bout carries a log (`:198`); `resolver.py:245` writes to it; `narrative.py`
summarises and renders it. The wrapper simply does not pass `record=`, and `scene_dispatch.py:299`
discards the bout.

**But three things below that link are missing, and they are not kwargs:**

1. **No home.** `World` has no chronicle field (`game_state.py:167-212`); `CampaignResult` has no slot
   (`mc_v18.py:84-105`) — it carries winner, `key_log_hash` and final state. A rendered chronicle has
   nowhere to be stored or returned.
2. **No output channel from the consumer.** `articulation.py:140` subscribes as `_on_key(key,
   scheduler)` — it never receives `world`. Return values are discarded at notify
   (`keys.py:576-577`); the sanctioned in-callback channel is `schedule_emission` (`:525-536`).
3. **The renderer misclassifies.** `narrative.py:88` maps a banded verdict to DEADLOCK, and `:92`
   treats any non-A, non-draw winner string as side B. Fixing the chain without fixing `classify`
   produces a chronicle that is wrong about who won.

So: the *plumbing* is one kwarg; the *feature* is a design decision about where a chronicle lives and
how a callback returns anything. Also note that this session claimed to have executed the one-kwarg
check and quoted its output — **no run artifact for that exists in the tree**, so treat the structural
reading as verified and the execution claim as unverified.

---

## §5 Emission — what the world actually says about itself

Two Key types are emitted on live paths and **both are absent from articulation's
`_TRIGGER_TYPE_IDS`** (`articulation.py:116-130`), while the registries declare articulation a
consumer of each:

| Type | Emitted at | Condition | Declared consumers |
|---|---|---|---|
| `scene.contest_resolved` | `parliamentary_bridge.py:212` | Only if `winner is not None and degree in ("Overwhelming","Success")` (`:206`) | npc_behavior, faction_layer, articulation (`key_type_registry_v30.md:854`) |
| `scene.battle_concluded` | `faction_action.py:342` | **Unconditional** per resolved war action | four, incl. articulation (`key_graph.json:1307-1313`) |

The world emits events; the module declared to hear them does not list them. This is the narrowest
real wiring gap in the document — a roster entry, not a design question — and it is worth doing early
because everything narrative downstream reads that roster.

One doctrine note, recorded because it is deliberate and looks like a bug: `faction_action.py:386-388`
sets `causes=[]` with a stated reason. `Key.causes` is the causal-bookkeeping field
(`keys.py:147`, invariant enforced at `:384`), so an empty `causes` on the most frequent unconditional
emitter means the causal graph is not being populated from the busiest source.

---

## §6 What needs Jordan

Ordered by how much is blocked behind each.

| # | Question | Blocks |
|---|---|---|
| **Q1** | **What is a character at runtime?** One object or two — authored record and simulation record — and what maps between them? | Gaps 1, 2, 9; five chains (§1) |
| **Q2** | **What is a strategic army, in cells?** | Gap 3; **Ruling A cannot land without it** |
| **Q3** | **Where does a chronicle live, and how does a Key consumer emit output?** | Gap 6; all narrative render |
| **Q4** | **Should Binding operations be harder than Weaving, and on what axis?** | Suite 01 §2.4 — implied by Ruling B, unanswered |
| **Q5** | **One pool document: document the eight formulas, or normalise them?** | Suite 01 §3.4 — three of the differences are design positions, not drift |
| **Q6** | Ratify or reject the belief layer (2026-08-18 epistemic proposal) | Gap 7 |
| **Q7** | Author `engine_clock` — the temporal spine has no design doc | Gap 11; the Godot port beyond combat |

**Q1 and Q2 are the two that matter.** Everything else is downstream of one of them or is small.

---

## §7 Corrections this document makes to earlier session output

1. **"The single missing artifact is a loader."** Wrong. The registry schema and the `NPC` dataclass
   do not correspond; the gap is UNSPECIFIED (§1).
2. **"`scene.contest_resolved` is emitted every season."** Conditional on winner and degree (§5).
3. **"D5 (mass_seizure) needs only the call."** It also needs the ACCORD_MAP conversion (§3.5) — the
   call alone writes a wrong-scale value.
4. **"`owner_faction` is populated for one settlement."** 37 of 37 (Suite 02 §3).
5. **Chronicle band bug cited at `narrative.py:114/:126`.** The defect is at `:88/:92`; the cited lines
   are a different, non-defective function (§4).

---

_Verified 2026-08-23 against `claude/fable5-investigations-architecture-1phbx9` at `512400f`. AST
sweeps used for reachability (treaty API, ledger API, pool constructors, TN loads); every quoted line
read at source. Not verified in this pass: the 40-seed mass_seizure unreachability measurement
(carried as quoted); the chronicle one-kwarg execution claim (structure verified, run not reproduced);
`Settlement.ap`'s zero-reader status._
