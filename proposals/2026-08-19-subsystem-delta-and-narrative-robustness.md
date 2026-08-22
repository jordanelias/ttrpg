# The Delta — what is designed, what is built, and why the world is empty

## Status: FINDINGS. Content/design only — another session owns the restructure; no tooling, no moves, no registry edits. Compliance bookkeeping light per Jordan 2026-08-19; reconciliation pending.

**Date:** 2026-08-19 · **Method:** agonist→antagonist. Eight producers (code as basis, design as comparator), one **Fable 5 authoritative full-read pass barred from grep/regex/pattern-matching** per Jordan's direction, and independent read-only antagonists per delta. Where Fable and a producer disagree, Fable wins — it read the files.

---

## §1 THE ONE-LINE FINDING

> **In every seeded campaign, the population of Valoria is zero.**
> — Fable 5, from reading `engine/mc_v18.py:186-194`, `scene_dispatch.py`, and `npe.py` end to end

`generate_npc` is correct, tested, and has **no world-gen or season-tick call site** — deliberately, per `mc_v18.py:186-194`, because canon specifies scene-driven generation and no live scene spec generates any. `world.npcs` is empty every run. The seasonal stance-drift loop iterates an empty dict.

And the shape of the loss, in one comparison:

> **The settlement record has a slot for people (`Settlement.npc_ids`, `registry.py:87`). The person record has a slot for nothing and no one.**

---

## §2 THREE FAILURE MODES, NOT ONE — and they need different fixes

The investigation began looking for missing design. It found almost none. What it found instead sorts cleanly into three kinds of break, each with its own remedy.

### §2.1 ORPHANED MECHANISM — built, correct, no caller

| Mechanism | Status |
|---|---|
| **threadwork, entire** | 7 operation types, a 6-branch opposing-outcome table matching its design cell-for-cell, a 15-card Co-Movement deck, a working Coherence track. `mc_v18` never imports it; no `scene_type` branch exists |
| **settlement ledger** | Precedent / Grudge / Debt / Reputation / Leverage — complete write API, dedupe, TTL, succession-survival. **Only production caller is `ledger_sweep`** |
| **`combat_engine_v1`** | 6,155 lines, 53 weapons, a real acquisition layer. **No path by which a game turn calls it** — no `queue_scene("combat")` exists |
| `generate_npc` · `succeed_governor` · `mass_seizure` · `treaty` expiry · `add_belief` · `revise_belief` | all built, all uncalled |

**Fix: add a caller.**

### §2.2 HOLLOW SEAM — the caller fires; the body is a stub

**`engine/mc_v18.py:255-256` calls `articulation.subscribe_all(world.echo_scheduler)`.** Thirteen trigger types — `state.scar_acquired`, `state.coup_attempted`, `state.succession`, `state.belief_revised`, `scene.combat_resolved` and nine more — **fire callbacks on every campaign season.** Every callback resolves to `stubwire.stub_resolve`.

The stubbing is deliberate, not neglect: *"the render layer stays ED-IN-0073's docket (Q1-Q4 qualitative-rendering fork, unbuilt) — do not build it here"*, repeated six times in `articulation.py`.

`fieldwork.py` and `investigation.py` are the same shape: 112 lines of pure no-op, with the producer's damning observation that `run_fieldwork_scene` and `resolve_npe_response` are **literally interchangeable** because neither has activity-specific logic.

**Fix: write the body.** ⚠ Whether this is small or large is the one open question — see §6.

### §2.3 STARVED SEAM — caller and body both real, fed degenerate input

**Social contest is not orphaned. It runs live.** And:

- **every live contest is `logos_spammer` vs `logos_spammer`** — the same trivial policy on both sides, emitting the same move every exchange
- the caller never passes `world=`, so audience resistance is derived and then always `None`
- no `Dossier` is ever populated — evidence never enters
- no armature is passed, so **Style, the CLASH/REINFORCE algebra, and the CR5 backfire — all working code — are unreachable**
- `base_ob = 2.0`, fixed, never overridden by any of the 8 proceedings
- the entire consequence spine is **a ±1/±2 Mandate delta on one faction**

The kernel supports texture. The call site hands it two integers.

**Fix: enrich the call site — no new mechanism required.** This is the cheapest large win in the tree.

---

## §3 WHAT AN ENTITY CAN BE, IN CODE

| | Settlement | Faction | NPC |
|---|---|---|---|
| Fields | ~25 | 16 | 12 |
| Named? | **yes, authored** | yes | **no** |
| Instantiated every campaign? | **yes** — `populate_from_geography` at `create_world` | yes | **never** |
| Populated in production | ~6-7 of 25 | stats + 7 booleans (4 spent-action flags) | n/a |
| Memory | ledger (5 kinds) — **never written** | none | `persistent_state` — **never written** |
| Relations | province, adjacency, `npc_ids` | territory ownership only | **none** |

**Factions:** personality is a string comparison. `if faction.name == 'Crown'` … `elif == 'Church'`. **Hafenmark and Varfell have no branch at all** — swap their names in the starting-stats table and the simulation is unchanged. Every module meant to carry their identity is a `stubwire` stub. `parliamentary_action.py:68-69` says it outright: *"No grudge / hostility / inter-faction-relationship stat exists in game_state.Faction."*

**No PC record exists.** `form_knot` duck-types `.bonds`, `.spirit`, `.history_relationships`, `.ts` — **no class in the tree defines them.** A PC is a bare `actor_id` string used as a key across five mutually unaware registries.

---

## §4 SIX DEFECTS FOUND BY READING

Fable 5's pass, barred from pattern-matching, confirmed three producer claims and found three more. All are small, all are silent.

1. **The hidden-allegiance deviation is a dead write.** `npe.py:298` assigns a *local*; the constructor at `:308-319` never passes it. One of five canonical deviation outcomes silently does nothing.
2. **The Knot-break → Conviction Scar consequence is a silent no-op.** `knots.py:349-353` scars `'Loyalty'`; `conviction.py:46-49` has no `Loyalty`; `:191-193` returns a magnitude-0 record. The one implemented cross-system emotional consequence fires and lands nowhere.
3. **`npe.py:261` comments "weighted by faction"; the code two lines down is `rng.choice(CONVICTIONS)`** with no weighting. The comment promises what the code does not do.
4. **`conviction.py:42` calls its own 9-tuple "the canonical 13-Conviction set"** — the comment miscounts the thing it annotates.
5. **THREE conviction taxonomies disagree.** `npe.py`'s 8 (**Justice, Survival and Power appear in no design taxonomy at all**), `conviction.py`'s 9, canon's 13. The relational-graph doc adds Honor, in none of them.
6. **`apply_knot_loss` drops two of four consequences** — `composure_damage` and `disposition_set_to` are written into a local dict no caller applies.

---

## §5 THE NARRATIVE LAYER

**A working prose renderer already exists** — `systems/social_contest/sim/contest/narrative.py`, `Chronicle.render()`, producing real sentences. Its only callers are its own tests.

**Authored prose is discarded at load.** `valoria_geography_v30.yaml` carries a hand-written `description:` for each of 37 settlements. `populate_from_geography` reads that file at world-gen, maps four fields, and drops `description` because `Settlement` has no prose field. **The sentence sits three lines above a `yaml.safe_load()` the engine genuinely executes.**

**58 authored event cards** (`grounded_event_card_deck_v1.md`, PROPOSED) with trigger predicates and stat deltas — zero implementing code, cannot fire. `env.crisis`, `env.disaster`, `meta.miraculous_event`, `meta.legacy_event` are registered types whose declared emitting systems have no `.py` at all.

**A contest has no subject.** No topic, claim, or argument content exists anywhere — `ground` is one of six abstract stasis tags. The authored flavor prose describes *kinds* of move and *kinds* of room, never what a debate is about.

**What a campaign outputs today:** `CampaignResult` — a winner id, a season count, a battle count, three telemetry integers.

---

## §6 THE ONE BUILD THAT CHANGES THE MOST

Fable's recommendation, argued from the code and adopted here:

> **Build the authored-person loader** — a named-NPC registry populated from canonical content at `create_world`, on the exact pattern of `populate_from_geography`, including residence and relational edges.

Why it outranks the alternatives:

1. **The pattern is proven in-tree, once, and it produced the only real entity in the game.** Settlements are realized for exactly one structural reason: authored YAML plus a loader called at world-gen. Nothing about that is settlement-specific.
2. **Every dormant person-mechanic is a store waiting for occupants, not a system waiting to be built.** `world.convictions`, `world.beliefs`, `world.knots`, `world.npcs` are already declared, routed and fully serialized. `simulate_npc_actions` already runs every season — over an empty dict. `Settlement.npc_ids` waits. **One loader turns four or five already-ticking systems from vacuously-true to live simultaneously.** No other single build has that fan-out.
3. **It converts the generator from the ceiling into the floor.** `generate_npc` cannot be the path to real people — its output is anonymous by construction. Named, placed, edge-bearing NPCs give generated ones something to be background *to*.
4. **The counterfactuals are weaker.** Writing the ledger first gives settlements memories of governors who are themselves strings. Building edges without instantiated NPCs is a graph with no nodes.

**It also forces a fix in passing:** a loaded NPC must seed convictions in *some* canonical taxonomy, which retires the vocabulary split and the `'Loyalty'` no-op together.

---

## §7 WHAT IS NOT YET VERIFIED

Honest status: the antagonist pass is **incomplete at time of writing**. Five critics were dispatched with the no-pattern-matching constraint; their corrections are not yet folded in.

| Claim | Basis | Confidence |
|---|---|---|
| Population is zero; `generate_npc` uncalled | **Fable, read in full** | high |
| The `'Loyalty'` scar no-op; the dead `hidden_allegiance` write | **Fable, read in full** | high |
| Ledger's only production caller is `ledger_sweep` | **Fable, read in full** | high |
| No PC/actor class exists | Fable + a producer, agreeing independently | high |
| Articulation's 13 triggers fire into stubs every season | producer (grep-assisted) | **medium — antagonist running** |
| "The gap is ONE function body" | producer inference | **low — this is the claim I most want killed.** It may understate what `generate_chronicle_entry` would need to reach |
| Threadwork entirely unreachable | producer (grep-assisted) | medium |
| Social contest is `logos_spammer` vs `logos_spammer` live | producer, corroborated by the lane's own prior audit | medium-high |

**The claim most likely to be wrong** is §2.2's tractability — that the render layer is a small fix because the bus is already wired. A stub firing is not the same as a stub that *could* produce text from what it receives, and nobody has yet checked whether the callback's arguments carry enough state to render from.
