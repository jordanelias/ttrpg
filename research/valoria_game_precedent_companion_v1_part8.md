# Game Precedent Companion — Part 8: The Personnel Precondition (ED-IN-0201)

## Status: PROPOSED (2026-08-28) · reference under §0.05, not canon
## Version: v1.0 · Lane: IN (cross-cutting — FA, SE, MB, PC)
## Records: **ED-IN-0201**, ruled by Jordan 2026-08-28, not executed
## Reads: Part 7 (stance), Part 6 (shape), master `_part4` §6 (U-3 / P4)

**Reading order:** [1](valoria_game_precedent_companion_v1.md) → [2](valoria_game_precedent_companion_v1_part2.md) → [3](valoria_game_precedent_companion_v1_part3.md) → [4](valoria_game_precedent_companion_v1_part4.md) → [5](valoria_game_precedent_companion_v1_part5.md) → [6](valoria_game_precedent_companion_v1_part6.md) → [7](valoria_game_precedent_companion_v1_part7.md) → [8 · The Personnel Precondition](valoria_game_precedent_companion_v1_part8.md)

---

## §15 THE RULING

> *"All faction actions, settlement governance, mass battles, etc are predicated upon people
> existing. We do not allow the game to perform faction actions if there is no leader of that
> faction, and that leader themselves is going to influence what choices are made for available
> faction actions in the same way that the person(s) who are governing a settlement or conducting a
> battle may make different choices with the same information and options."*
>
> — Jordan, 2026-08-28. Filed **ED-IN-0201**, `status: open`, **not** `needs_jordan`: he has ruled;
> what is missing is execution.

### 15.1 Two clauses, and they are separable

| | clause | what it is |
|---|---|---|
| **C1** | **The gate.** No leader → no faction action. No governor → no settlement governance. No commander → no battle | A **precondition**. Nothing resolves; the scale simply does not act |
| **C2** | **The decider.** The person shapes **which** action is chosen, from the same option set, with the same information | **Presence as identity**, in Part 7 §14.4's terms — the person changes *the choice*, not a modifier on a roll |

C2 is the harder half and the more important one. Part 7's census found Valoria has **no**
identity-presence anywhere: mass battle is `power = round(Mil)`, and everything else is a stat. C2
says every scale must move to the third column.

### 15.2 What the ruling settles that was open

- **U-3 and Proposal 4 are no longer proposals.** The master's `_part4` offered "the season is a
  person's season" as one of four rival organisations; C1 makes it **the** organisation. What was a
  fork is now a requirement.
- **Part 7 §14.1's stance question is answered for the on-behalf half.** A delegation object is
  mandatory at three scales. The *within* half — the position object, the Standing ladder — is not
  addressed by this ruling and stays open.
- **The presence question is answered.** C2 rules out presence-as-a-stat.

---

## §16 MEASURED STATE — what the gate would find at HEAD

Every row verified by reading the file, not by citation.

| Scale | The delegation object the gate needs | State at HEAD |
|---|---|---|
| **Faction** | a leader field | **Does not exist.** `Faction` (`game_state.py:109-140`) has six stats, a territory list, `standing`, four turn-flags — and no leader, ruler or head |
| **Faction** | the gate itself | `mc_v18.py:132-136` gates the faction pass on exactly two conditions — `faction.parliamentary` and `faction.territories` — then calls the action unconditionally |
| **Faction** | the decider | `faction_take_action` selects with **one `rng.random()`** against a prior re-weighted by three **faction-level** signals. **No person is consulted anywhere in the path** |
| **Settlement** | `governor_id` | Exists, is `None` on all 37 after world-gen; its only writer `succeed_governor` has **zero callers** |
| **Battle** | a commander | `_faction_to_unit` sets **neither** charisma nor cognition, so `derive_command` falls back to the hardcoded `command = 4` — despite `COMMAND_SIGMA_ENABLED` now defaulting **ON** |
| **All** | people at all | `world.npcs` is empty in every seeded campaign; `generate_npc` is complete and has no call site |

---

## §17 THE BOOTSTRAP CONSEQUENCE — the load-bearing one

**Under C1, with `world.npcs` empty, a campaign performs zero faction actions.**

That is not a bug in the ruling; it is the ruling working correctly against a world with no people in
it. But it changes the status of the loader completely:

> **The person loader stops being an enhancement and becomes a precondition of the engine running at
> all.**

Three things follow, and the third is a sequencing trap.

1. **Leaders must exist at world-gen, before season 1.** A generator that produces people *during*
   play cannot satisfy C1 on the first tick. This settles the CK3-versus-CK2 population question
   found in Part 5 §12.5 in favour of the corpus's own recommendation — *generate on demand, not on a
   clock* — because an ambient spawner cannot guarantee a leader exists when the season loop asks.
2. **The 46 authored characters are not decoration.** `references/npc_registry.yaml` carries `role`
   and `faction` on **46/46**, which is exactly the field pair a leader assignment needs. The registry
   was already the right shape; it has zero runtime loaders.
3. **The sequencing trap.** The integration master's F10 established that a two-NPC load moves the
   seed-42 winner, because `simulate_npc_actions` draws the shared campaign RNG once per qualifying
   pair. Under C1 the loader is mandatory, so **that golden movement is now unavoidable** — which
   makes the NPE RNG substream a hard prerequisite rather than a nicety. Land the substream first,
   prove it byte-identical, then load; otherwise the first campaign that obeys the ruling is also the
   first campaign nobody can attribute.

---

## §18 WHAT ELSE THE GATE TURNS ON

### 18.1 It makes succession load-bearing

`systems/social_contest/sim/contest/faction.py::succession` is a within-faction two-claimant contest
on the Persuasion Track, returning `unified` / `decisive` / `split` with §7.2.1 ratios and a
Verdun-843 grounding. It is **unreachable by construction** today, because `Faction` has no leader
field and leader elimination is therefore not an event the season loop can produce.

Under C1 it becomes the mechanism that decides **whether a faction resumes acting at all**. And that
gives faction collapse something it currently lacks entirely: a faction with no viable successor
**stops acting**, which is a far better failure state than the designed Collapse Exit Procedure that
nothing detects.

### 18.2 It makes the AI a person-AI

`engine/autoload/npc_ai.py` is the module named for NPC decision-making. Both entry points are typed
no-ops with zero production callers, and **its docstring names `faction_action` as a dependency —
which is backwards under this ruling.** C2 puts the deciding logic on the person, so `npc_ai` becomes
the caller and `faction_action` the executor.

### 18.3 It re-scopes what the three RNG-free signals are for

`faction_take_action`'s three signals — target-exists, military advantage, undergoverned share — are
real state reads and Part 3 credits them as *"the skeleton an interior would hang on."* Under C2 they
do not disappear; they become **the information the leader is deciding with**, which is exactly the
ruling's phrasing: *the same information and options.* The signals stay; what changes is that a
person, not a prior, weighs them.

---

## §19 THE NERS CONSTRAINT ON C2

**C2 must not be implemented as a flat trait bonus on the selection roll.**

A flat shift of size `X` is worth `Δz = X / (0.8·√Pool)` — **more to a small pool than a large one**.
A leader trait applied as a bonus would therefore be worth systematically more to a weak faction than
a strong one, which is the flat-shift trap the integration master's `_part4` already found twice.

**The in-band implementation, and the precedent supports it.** Part 6 §13.8's census found that
**the genre gates where Valoria rolls** — and Total War: Three Kingdoms gates *which unit types exist*
on the commander's **class** rather than scaling a bonus. So C2's shape should be:

- the leader **changes the option set** — which actions are available at all;
- the leader **changes the pool source** — whose score is rolled;
- the leader does **not** add a modifier to a roll that would happen anyway.

That is presence-as-identity expressed as a `GATE`, and it satisfies C2's wording exactly: *different
choices with the same information and options* means the **choice** differs, not the odds.

⚠ **And Part 6's other warning binds here:** gate on a **role**, not a **biography**. TK's class
gating means losing a person is a promotion opportunity; Valoria's designed §1.5 gates on *"the
officer with Cavalry History"*, so losing one person costs you cavalry permanently. C2 should key on
what a leader **is** in the structure, not on their individual history.

---

## §20 THE ONE GENUINE AMBIGUITY, FLAGGED RATHER THAN DECIDED

**"No commander, no battle" has two readings, and they lead to different games.**

| reading | shape | what it means | precedent |
|---|---|---|---|
| **(a) A gate** | `GATE` | A faction with no available commander **cannot declare a conquest.** Consistent with C1's other two clauses | The ruling's own wording. Nothing in the survey does exactly this |
| **(b) A penalty** | modifier | It can, and an **unled army fights at a penalty** | **Dominions** — the army is anchored to its commander and routs when he dies. This is the *scale-blind* failure pole from Part 5 §12.7 |

**Why it matters.** (a) is a precondition and composes cleanly with the rest of the ruling. (b) is a
modifier, and it re-opens the leverage question the corpus says nobody has solved — a flat penalty on
an unled army is the Dominions shape, whose documented failure is that a single commander's fate
dominates an arbitrarily large force.

**Recorded open in ED-IN-0201.** My reading is that (a) is what the ruling says and the one that
composes; but the ruling's text addresses faction actions explicitly and battles by extension, so I
have not decided it.

---

## §21 WHAT EXECUTION WOULD LOOK LIKE, IN ORDER

Not a proposal — the ruling is made. This is the dependency order the measured state implies.

| # | step | why here | impact |
|---:|---|---|---|
| 1 | **NPE RNG substream, derived from the campaign seed** | §17's trap: the loader is now mandatory, so its golden movement must be attributable *before* it lands | **INERT** — must be byte-identical, and that is the proof |
| 2 | **Re-point the three population guards at `world.npcs`** | They observe `world.npc_counter`, which only `generate_npc` increments and a loader never touches — so they cannot see the change they exist to catch | INERT |
| 3 | **A leader field on `Faction`, and a `roles` notion on the person** | The delegation object C1 gates on. Part 7: on-behalf needs a delegation object; this is it | **RULING-adjacent** (schema), then MOVES |
| 4 | **Load the 46 authored characters at world-gen, assigning leaders** | C1 cannot be satisfied on season 1 otherwise. `role` + `faction` are on 46/46 already | **MOVES** — every golden |
| 5 | **The gate itself**, at `mc_v18`'s faction pass | One condition added beside `parliamentary` and `territories` | MOVES |
| 6 | **C2 at faction scale** — the leader changes the option set and the pool source, per §19 | The decider half. Route it through `npc_ai`, not `faction_action` | MOVES |
| 7 | **`tick_settlements` + `succeed_governor` caller** | C1 at settlement scale needs a governor, and appointment needs a flow | MOVES |
| 8 | **Charisma and cognition through `_faction_to_unit`** | C1/C2 at battle scale. Strict superset — with no commander attached the value stays `None` and the path is byte-identical | MOVES on attach, INERT before |
| 9 | **Succession made reachable** | §18.1 — what happens when the gate closes, and the mechanism faction collapse currently lacks | MOVES |

**Steps 1–2 are the only ones that can be proved byte-identical**, and they are the only ones that
should land before the schema question in step 3 is settled.

---

## §22 WHAT THIS DOES NOT SETTLE

- **The within-faction stance.** The ruling is about people being *required* and *deciding*; it does
  not address the position object — Standing, the ladder, promotion, or the divergent-interest agent
  of Part 7 §14.5. A leader who decides is not yet a leader who can be *challenged*.
- **What a leader is, structurally.** Whether the leader is one of the 46 authored characters, a
  generated officer, or a role held by whoever has highest Standing, is a schema question the ruling
  leaves open — and step 3 above cannot proceed without it.
- **Whether the gate applies to the four non-parliamentary or territory-less factions**, which
  `mc_v18` already skips on other grounds.
- **The commander ambiguity** of §20.
