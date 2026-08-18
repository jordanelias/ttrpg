# Fieldwork, Investigation and Non-Adversarial Play — an architecture, not a redesign

## Status: PROPOSED — DESIGN-ONLY, HELD FOR JORDAN. No `.py` touched, no constant changed, no default flipped, no golden re-recorded, no key type allocated. Every repo claim below was read off the working tree at HEAD and carries a file:line; every precedent claim carries a confidence tag.

**Date:** 2026-08-18 · **Lane:** FI (field investigation) · **IDs:** none allocated (design-only)
**Bears on:** ED-916 (the FI design gate) · ED-FI-0001 (investigation_systems_v30 audited by no lane) · ED-FI-0002 (EP-6 counter-espionage) · `godot_conversion_strategy_v1.md` Gate-0 · CLAUDE.md §6 "porting is blocked on authoring canon first"

> **What this document is.** Two agents ran concurrently. Fable 5 read the field-investigation
> design corpus, the Key schema and the module contracts read-only; Opus 5 researched how acclaimed
> games manage exploration, investigation, fieldwork and other non-adversarial play, and wrote this.
> The instruction that shaped it: **draw most directly from the design documents we already have,
> so long as they work well alongside our other systems.** So the default answer to "how should
> fieldwork do X" is *a mechanic this repo already authored*, and the plan's job is to **wire** it.
> §8 enumerates every genuinely new piece, and the list is deliberately short.

---

## §1 THE FINDING THAT REORDERS EVERYTHING

Fieldwork is **prose-complete and code-empty**, and the two gaps blocking it are not in fieldwork.

| Measured at HEAD | Value |
|---|---|
| Fieldwork design prose | **3,132 lines** across 19 `.md` files in `systems/fieldwork/` |
| Real sim modules | **1** — `systems/fieldwork/sim/knots.py` (Knot, KnotState, form/sustain/rupture/loss) |
| Stub-wired entry points | **6** — all of `sim/fieldwork.py` and `sim/investigation.py` route to `engine/substrate/stubwire.py:stub_resolve` |
| Entries in `references/module_contracts.yaml` | **1** — `fieldwork_knots`. There is **no** `fieldwork`, `fieldwork_exploration`, `fieldwork_investigation` or `fieldwork_socializing` module contract |
| Design gate | **ED-916** — "Zero continuous-engine validation at fieldwork parameters", P2, open since 2026-06-11 |

`systems/fieldwork/sim/fieldwork.py` says this itself, and it is worth quoting because it already
found the hole this plan fills:

> "`module_contracts.yaml` has no entry for this module by that exact name (only the sibling
> `fieldwork_knots` is contract-declared — verified 2026-07-29, G12: the register's 'io_contract
> from their module contracts' lead does not resolve for `fieldwork`/`investigation` themselves)"

So the task in front of us is **not** "improve the fieldwork system". It is: *the fieldwork system
has never been built, and most of the design that would build it is already written.* That makes
this a wiring problem with a contract-authoring prerequisite — which is exactly what CLAUDE.md §6
says the Godot port is blocked on, for this subsystem specifically.

---

# §2 PRECEDENT RESEARCH — how acclaimed games run non-adversarial play

Method: six structural problems every non-adversarial mode must solve; for each, the games that
solved it, the mechanism named precisely, and the Valoria surface that already holds the
counterpart. Confidence tags follow the house convention already used in
`proposals/social_contest_consolidation_integration_v1.md` (`[HIGH]` = mechanism is
well-documented and I can state it exactly; `[MED]` = mechanism is right, detail may be off).

## §2.1 P1 — THE ACCESS PROBLEM (investigation stalls on a missable clue)

| Precedent | Mechanism | Confidence |
|---|---|---|
| **GUMSHOE** (Laws, 2007) | The *core clue* is never gated behind a roll. Investigative ability spends buy **quality and leverage**, never access. The roll is on the margin, not the gate. | `[HIGH]` |
| **Blades in the Dark** | No failed action blocks; position/effect converts failure into consequence. Flashbacks retroactively supply preparation, so "I didn't think of that" is never terminal. | `[HIGH]` |
| **Brindlewood Bay** / Carved-from-Brindlewood | A clue is **raw material with no fixed referent**. The `Theorize` move assembles gathered clues into a solution that the Keeper also did not know; beat the roll and the theory *becomes* true. | `[HIGH]` |

**Valoria already holds this.** `fieldwork_v30.md` §4.4 Desperate Trail (Fail Forward) is the
GUMSHOE floor by another name. The borrow is not a mechanic, it is a **discipline**: state the
access/quality split explicitly in the contract so no future resolver can put access behind a roll.

**Rejected:** Brindlewood's player-authored truth. Valoria has a strategic layer that must
propagate consequences from a fact; a truth that does not exist until the players name it cannot
be an input to faction, settlement or world resolution. (A bounded variant survives as a Jordan
question for *cold* cases — see §9 Q6.)

## §2.2 P2 — THE DEDUCTION LOCUS (player's head, or character's sheet?)

| Locus | Precedent | Mechanism | Confidence |
|---|---|---|---|
| Player | **Return of the Obra Dinn** | Verification oracle: fates lock only when three are simultaneously correct. Deduction is entirely player-side; the character is a camera. | `[HIGH]` |
| Player | **The Case of the Golden Idol** | Fill-in-the-blank sentence: the assertion is a *typed structure*, not free text — which is what makes it machine-gradable. | `[HIGH]` |
| Player | **Her Story / Immortality** | The traversal verb *is* the search term. What you know determines what you can reach. | `[HIGH]` |
| Player | **Outer Wilds** | Knowledge is the only persistent state across loops. Nothing else banks. | `[HIGH]` |
| Character | **Sherlock Holmes: Crimes & Punishments** | Deduction board: bind two evidence nodes → a deduction node → choose between **competing conclusions**. You may convict the wrong person and the game continues to a complete ending. | `[HIGH]` |
| Character | **L.A. Noire** | An accusation must **cite a held evidence item**. The evidence-binding, not the accusation, is the mechanical act. | `[HIGH]` |
| Character | **Disco Elysium** | Skills are interlocutors that *interpret for you* — and can be wrong. Interpretation is characterised, not neutral. | `[HIGH]` |

**Valoria is forced into a hybrid, and the constraints say which one.** There is no GM, so the
engine must hold a resolvable truth. P-08 (epistemological barrier) and P-03 (rendering =
consciousness-performed) say the character holds only a rendered subset. Therefore:

> **the engine holds ground truth · the character holds a visibility-restricted view of it ·
> the player commits a typed, evidence-bound assertion · the resolver grades the assertion
> without ever revealing ground truth.**

That is Golden Idol's typed assertion + L.A. Noire's evidence-binding + Sherlock's
competing-conclusions-with-consequences, and it is **one resolver**, not three systems.

**Rejected:** Obra Dinn's confirm-in-threes (a brute-force guard for a closed 60-person puzzle; a
global verification oracle would dissolve P-08 outright) and L.A. Noire's facial tells (a
ground-truth channel that bypasses the barrier).

## §2.3 P3 — THE GROUND-TRUTH PROBLEM (no GM: where does the answer come from?)

| Precedent | Mechanism | Confidence |
|---|---|---|
| **Blade Runner** (Westwood, 1997) | The culprit is **randomised per playthrough**. The consequence is architectural: the evidence system *cannot* be a script, it must be generative. | `[HIGH]` |
| **Shadows of Doubt** | A procedurally generated city where cases are solvable because the **generator guarantees a chain** (prints → address → employment → alibi), not because a designer placed clues. | `[MED]` on chain specifics, `[HIGH]` on the principle |
| **Dwarf Fortress** | Knowledge propagates as **rumours with provenance**: who knows a thing, and from whom they heard it, are modelled world state. | `[HIGH]` |
| **Ultima VII / Kingdom Come: Deliverance** | NPC schedules make *when* you look a real variable, without any authored gating. | `[HIGH]` |

**Valoria already holds the generator.** `investigation_systems_v30.md` System 1 (NPC Population
Engine) has two-tier generation, persistence and genome records. What is missing is the thing that
makes a generated case *playable*:

> **a solvability invariant on the generator** — for a case to be admissible, there must exist a
> reachable chain of Keys from the investigator's starting visibility to the true assertion.

*[CORRECTED 2026-08-18 — §11.1: this is NOT a "new requirement". Jordan ruled that scripting narrative hooks and sequences is allowed, and `baralta_crown_claim_v30`'s condition table is exactly this object: a scripted conjunction of world facts gating an emergent outcome. Read it as **generation-time precondition + emergent erosion**, never as a constraint maintained against the sim — that half would be scripting an arc.]*

## §2.4 P4 — THE TIME / ATTRITION PROBLEM (what makes *where to look* matter?)

| Precedent | Mechanism | Confidence |
|---|---|---|
| **Pathologic 2** | 12 days, more needs than hours. Triage *is* the game: every hour spent is an hour not spent. Already cited at `systems/_architecture/player_agency_v30.md:51`. | `[HIGH]` |
| **Pentiment** | Finite days; you cannot interview everyone; you accuse without certainty. Already cited at `player_agency_v30.md:57`. | `[HIGH]` |
| **Citizen Sleeper** | A **pool allocated per day across sites**, not a roll per action. The scarcity is placement, not success. | `[HIGH]` |
| **Outer Wilds** | Hard time pressure with **no progress loss** — knowledge persists, so the clock creates urgency without punishing exploration. | `[HIGH]` |

**Valoria already holds all of it**: §2 Fieldwork Pool, §3.3 Movement and Time, §6 Exposure,
the clock registry and `engine/autoload/season_manager.py`. The borrows are two disciplines:
1. **Citizen Sleeper**: the Fieldwork Pool is allocated **per scene across sites**, not rolled per
   action — which is what `run_fieldwork_scene(scene)` already implies by its signature.
2. **Pathologic**: what makes triage bite is that presence itself costs. Exposure should accrue on
   *being somewhere*, not only on failing there (`fieldwork_v30.md` §6.3 Exposure Sources is the
   home; whether it already does this is a doc question, not a new mechanic).

## §2.5 P5 — CONFIDENTLY WRONG (letting a player be sure and mistaken)

| Precedent | Mechanism | Confidence |
|---|---|---|
| **Heaven's Vault** (inkle) | Translation is **provisional**: you guess, the game rarely says "wrong", confidence accrues only by **matching a word across multiple independent artefacts**, and a wrong guess *narrows* the candidate set rather than blocking. | `[HIGH]` — verified 2026-08-18 |
| **Pentiment** | You never learn whether you were right. The accusation has consequences regardless. | `[HIGH]` |
| **Paradise Killer** | The trial runs on whatever evidence you bring. Partial conviction is a legal outcome, not a failure state. | `[HIGH]` |

**Heaven's Vault is the precise mechanism Valoria's Evidence Quality wants.** `fieldwork_v30.md`
§4.3 (Evidence Quality and the Epistemological Barrier) and `knots_v30.md` §4.5 (Knot-sharing
corroboration) are both asking the same question — *how sure are we* — and the answer should be
computed once:

> **confidence in a proposition = the number of INDEPENDENT support chains for it**, where
> independence means disjoint `causes` ancestry on the Key substrate.

One owner, three consumers (Evidence Quality, Knot corroboration, Thread-Read §4.5).

## §2.6 P6 — THE RECORD (how accumulated knowledge is held)

| Precedent | Mechanism | Confidence |
|---|---|---|
| **Outer Wilds** ship log | Auto-populated, graph-shaped, and critically it renders **known unknowns** — "there's more to explore here". That is what turns a log into direction without a quest marker. | `[HIGH]` |
| **Return of the Obra Dinn** book · **CK3** hooks panel · **Frostpunk** book of laws | Diegetic, auto-populated, cross-linked, and it **visibly banks**. Already adopted in-house at `proposals/social_contest_consolidation_integration_v1.md:490` `[HIGH]`. | `[HIGH]` |
| **Crusader Kings III** secrets | Information as an **ownable, discoverable, leakable object** with consequences on exposure — which is exactly what Cover/Exposure is. | `[HIGH]` |

**Valoria's counterpart** is the Case Board (`investigation_systems_v30.md` System 2), its Thread
Layer (ED-680) and the Investigation Journal (`fieldwork_v30.md` §10.3). The borrow is one rule:

> **the Case Board is a DERIVED VIEW over the KeyLog and owns no state**, and it must render
> known-unknowns (a Key whose `causes` chain has an unresolved antecedent) or it is a diary
> rather than a board.

## §2.7 WHAT THE CONVERGENCE SAYS

Across nineteen precedents the same three-way split recurs, under different names every time:

| | GUMSHOE | Obra Dinn | Heaven's Vault | Sherlock C&P | Valoria's existing name |
|---|---|---|---|---|---|
| **Access** — can I reach it | core clue, free | free to observe | artefact found | scene node | Intelligibility Gradient / §1 Depth Axis |
| **Interpretation** — do I read it right | spend for quality | player's head | provisional translation | deduction node | §4.3 Evidence Quality / P-08 |
| **Commitment** — do I act on it | — | confirm-in-threes | dictionary entry | condemn / absolve | §4.6 Contested Investigation / the assertion |

Valoria already names all three axes. **The architecture below adds no fourth axis** — it gives
each of the three exactly one owner.

---

## §3 THE PRIMITIVE MAP — what fieldwork must compose on, never re-implement

Every row verified by reading the file at HEAD. This is the §0 "build bottom-up from primitives"
list for this lane: if a fieldwork module ever computes one of these itself, that is the bug.

| Capability | Single owner (verified) | What fieldwork must NOT build |
|---|---|---|
| Universal state/event object | `engine/substrate/keys.py:138` `Key` — `id, type, emitted_at, source_actor, causes[], targets[], scale_signature[], symbolic_dimensions{}, visibility, time_horizon, permanence, payload{}` | any `Clue`, `Lead`, `Evidence` or `Rumour` class |
| Event log + validation + tick propagation | `keys.py:336` `KeyLog`, `keys.py:184` `TypeRegistry`, `keys.py:463` `TickScheduler` | any fieldwork-local event store or timer |
| Key type vocabulary — **55 types** | `systems/_architecture/key_type_registry_v30.md`, cooked to `engine/engine_params/key_types.json` by `tools/export_key_types.py`, round-trip-gated | any private event-name vocabulary |
| Degree ladder (ruled owner) | `engine/autoload/dice_engine.py:104` `degree_from_net(net, ob)` — margin bands 0/1/3, Jordan 2026-08-14, guarded by `tests/valoria/test_degree_ladder_single_owner.py` | any bespoke success/failure banding |
| Contest degree (**HELD**, pool-aware) | `engine/autoload/sigma_leverage.py:292` `degree(net, ob, pool)` — deliberately divergent, in the HELD registry | treating it as interchangeable with the above — see §5.5 |
| Scene queue and dispatch | `engine/autoload/scene_slate.py:25` `SceneSlot(scene_type, context, priority)` — **`"fieldwork"` is already in its documented `scene_type` vocabulary** (`scene_slate.py:26`) | any parallel scene manager |
| World state | `engine/autoload/game_state.py` | any fieldwork-local world store |
| Season / clock | `engine/autoload/season_manager.py` + `TickScheduler` + the clock registry | any bespoke fieldwork timer |
| Relational bonds | `systems/fieldwork/sim/knots.py` (real, contract-declared as `fieldwork_knots`) | anything relational — Knots are done |
| Unimplemented-surface discipline | `engine/substrate/stubwire.py:stub_resolve` | `raise NotImplementedError` |

**The scene-type finding is load-bearing and pleasant:** `scene_slate` already names `"fieldwork"`
as a scene kind. Fieldwork is therefore not a new scale, a new loop or a new envelope. It is a
**dispatcher registered against a queue that already expects it.**

---

## §4 THE TWO REAL GAPS — and both are in the substrate, not in fieldwork

These are the findings that change the build order. Both were measured, both are falsifiable, and
both are the same defect class §0.1 point 1 warns about: **a field with an asymmetry between its
writers and its readers.**

### GAP-A — `Key.visibility` is written and never read. *This is the epistemological barrier, unimplemented.*

`Key` carries a `Visibility` block (`keys.py:109`) with `public / semi_public_observers /
private_observers`, and `KeyLog._validate` enforces the §2.3-#8 "exactly one of three shapes"
invariant at construction (`keys.py:420-426`). **Nothing else in `engine/`, `systems/` or `tools/`
reads it.** There is no function anywhere that answers *"which Keys may actor X see?"*.

That is fine for combat and mass battle, where the interesting state is public. It is
disqualifying for investigation, where **"what does this character know, and how did they come to
know it" is the entire subject matter.** P-08 (epistemological barrier) and P-03 (rendering =
consciousness-performed) are today enforced by prose and by nothing else.

*Falsifier, run:* `grep -rn "private_observers\|semi_public_observers" --include=*.py engine/ systems/ tools/` returns only the dataclass, its serializer, and the constructor-side validator. If a reader exists under another name, this finding is wrong and §5.2 is already built.

### GAP-B — `Key.causes` is essentially unpopulated. *This is provenance, unfed.*

`Key.causes` is a list of antecedent key ids — the schema's provenance chain. Across the whole live
tree there are **three** non-test sites that set it, and **two of those pass `causes=[]`**:

- `engine/cross_scale/echo_transport.py:317` — `causes=[caused_by_key_id] if caused_by_key_id else []` (the only real one)
- `systems/factions/sim/parliamentary_transfer.py:166` — `causes=[]`
- `systems/factions/sim/faction_action.py:389` — `causes=[]`

So the ancestry graph exists in the schema and not in the data. Corroboration (§5.3), the Case
Board's known-unknowns (§2.6) and Evidence Quality (§4.3 of `fieldwork_v30`) all read that graph.
**Fieldwork cannot be built on an empty `causes` field**, and populating it is a cross-lane ask,
not an FI-lane change.

*Falsifier, run:* the grep above. If emitters populate `causes` through a helper I did not match, this is wrong and §5.3 is unblocked today.

### What is NOT a gap — the knowledge graph is already typed

Worth stating, because it is the reason this plan needs so little new design:

- `scene.witness` (registry L63) carries `observed_key_id` + `witness_actor` — **a Key that points at another Key.** That is the "who knows what, learned from where" edge Dwarf Fortress models as rumour propagation, and it is already canonical, already emitted by `scene_slate`/`npc_behavior`, already consumed by `conviction_track`/`npc_behavior`/`articulation`.
- `scene.investigation_resolved` (registry L880) already carries `finding: exonerated | guilty | inconclusive`. **The three-valued verdict — including "inconclusive" — is already canon.** Pentiment and Paradise Killer's "act without certainty" is not something we need to add; it is something we need to stop dropping.

> **The investigation knowledge graph = the KeyLog, plus `scene.witness` edges, plus `causes`
> ancestry, filtered by `visibility`.** Three of those four exist. The plan is mostly the fourth.

---

## §4b THREE MORE THINGS THE READ-ONLY PASS FOUND — and one of them is a one-line gap

Fable 5's independent read added three findings that change the plan's shape, and one that makes it
much smaller than expected. All four re-verified here at HEAD.

### §4b.1 The scene pipeline is built end-to-end. **`evaluable` is a one-element set.**

`engine/cross_scale/scene_dispatch.py:344-360` already carries a live `elif st in ("fieldwork",
"investigation")` branch that routes to the stubs and says so in its own comment:

> "ctx/world are threaded through so a future real resolver drop-in needs no call-site change here."

`scene_slate.py:26` already names `"fieldwork"` a scene type. `queue_triggered_scenes`
(`scene_dispatch.py:102`) already queues whatever `evaluate_triggers` fires. And
`zoom_in_out.check_mandatory_triggers(world)` already evaluates a full trigger registry.

Then this, at `scene_dispatch.py:96`:

```python
evaluable = {"Stability Crisis"}
deferred = [t.trigger_name for t in zoom_in_out.check_mandatory_triggers(world)
            if t.trigger_name not in evaluable]
```

**Every non-contest trigger the registry fires is computed and then dropped into a `deferred` list
that nothing consumes.** The only `scene_type` literal produced anywhere in `engine/` or `systems/`
is `"contest"` (`scene_dispatch.py:86`).

So the fieldwork pipeline is not missing a dispatcher, a queue, a scene type or a call site. It is
missing **an entry in a set, and a resolver behind the seam that is already cut for it.** *[CORRECTED 2026-08-18 — §11.4 C7: this framing is overweighted. Adding `"fieldwork"` to `evaluable` is necessary and nowhere near sufficient — it also needs trigger definitions, a resolver and state homes. It is a **seam**, not a gap, and a reader could otherwise conclude the system is nearly done.]*

### §4b.2 Fieldwork's prose degree tables encode the RULED-OUT ladder

`fieldwork_v30.md` §2.2 (L69) states "Overwhelming requires net ≥ 2×Ob AND net ≥ 3
(PP-232/PP-249)". Jordan's 2026-08-14 ruling deleted the Ob-scaled bar; the owner is
`degree_from_net` with margin bands 0/1/3. The same stale bands recur in §5.6a (L477-482) and
`knots_v30` §3.2 (L78-84) — **while `knots.py:226-228` already routes through
`dice_engine.degree_label`.** Code current, prose stale.

**Consequence for the plan: transcribe the *yield* column of every fieldwork degree table, never
the *band* column.** A build that ports the tables verbatim re-creates the exact defect
`sigma_leverage.degree` is quarantined for (§5.5).

### §4b.3 The receiving objects for a "Finding" already exist — twice

- **Citation path:** `systems/social_contest/sim/contest/primitives.py` has `Dossier` / `EvidenceItem`, with corroboration diminishing returns already implemented in its resolver.
- **Durability path:** `systems/settlements/sim/ledger.py:7-14` has `Precedent / Grudge / Debt / Reputation / Leverage`, durable across succession, named single-owner by ED-SC-0019.

So a Finding should be **constructible into an `EvidenceItem`** and **recordable as a ledger
entry**. No third record type. (This is the CK3-secrets shape from §2.6 arriving via a path the
repo already built for a different lane.)

### §4b.4 The vocabulary is already reserved — and `Cover` is the one hole

`references/descriptor_registry.yaml:190-196` `not_descriptors` already classifies:
`Evidence` → **clock** · `Disposition` → **track** · `Fieldwork`, `Knot` → **pools**.
**`Cover` appears in neither `derived_values` nor anywhere else** — `fieldwork_v30` §6.1 calls it a
Derived Value and the registry has no row for it. One registration, flagged.

### §4b.5 A correction to CLAUDE.md §6 itself — and to the method that produced it

CLAUDE.md §6 states that in `references/module_contracts.yaml` "10/27 modules have `doc: null`" and
"11/27 resolvers are `[ASSUMPTION]`-grade". A `grep -c` reproduces those numbers. **Parsing the
YAML does not.**

| | grep -c | parsed | why they differ |
|---|---|---|---|
| `doc: null` | 10 | **9** | the 10th hit (`:884`) is inside a `gap_notes` **string**, not a field |
| `[ASSUMPTION]` | 13 | **10** resolvers | `:14` is the file's header comment; `:878` annotates a `state` entry, not a resolver |

The nine are `npc_memory, scene_slate, game_director, scene_timer, audit, domain_actions,
settlement_economy, engine_clock, scenario_authoring`. `engine_clock` — the temporal spine §6 singles
out — is genuinely among them, so §6's *argument* survives intact; only its arithmetic is off by one
in each term.

Worth recording for the method, not the digit: this document's read-only pass reported these counts
as "VERIFIED exact" **by the same `grep -c`**, and the write-up pass then re-ran them by parsing and
got different answers. That is §0.1 point 4 in miniature — *a number without a control is not a
measurement* — and it is the reason every count in §1 and §4 above was taken structurally rather
than by line-matching. Filing the CLAUDE.md correction is an IN-lane edit, not this lane's to make.

---

---

## §5 THE ARCHITECTURE — a composition layer, five modules, four wrappers, no new resolver family

**Thesis.** Fieldwork gets **no resolver of its own**. It gets modules whose wrappers *adapt and
route* — the contract `systems/social_contest/sim/contest/wrapper.py` states verbatim for its own
kernel — plus four thin owners of one question each, every one pointing at a centralized
definition rather than carrying a copy.

```
   zoom_in_out.check_mandatory_triggers   →   evaluate_triggers   →   queue_triggered_scenes
        (registry exists)                     ⚠ evaluable={"Stability Crisis"}      (exists)
                                                       │
                                                       ▼
                                        scene_slate.SceneSlot(scene_type="fieldwork")   (exists)
                                                       │
                                        scene_dispatch._resolve_slot :344               (exists, seam cut)
                                                       │
        ┌──────────────────────────────────────────────┴──────────────────────────────────┐
        │  fieldwork_action · fieldwork_social · investigation_dialogue · fieldwork_sites  │
        │  fieldwork_knots (BUILT)                                                         │
        └──────────────────────────────────────────────┬──────────────────────────────────┘
                                                       │
              W1 pool/scene   W2 EvidenceView   W3 Corroboration   W4 Assertion
              (allocation)    (closes GAP-A)    (needs GAP-B)      (grades vs truth)
                    │               │                 │                  │
                    └──────► dice_engine.degree_from_net ◄───────────────┘
```

### §5.1 The four wrappers

| # | Wrapper | Owns exactly one question | Points at |
|---|---|---|---|
| **W1** | `FieldworkScene` pool allocation | *how much attention does this scene buy, and where is it spent* — allocated **across sites for the scene** (Citizen Sleeper, §2.4), not rolled per action. The existing signature `run_fieldwork_scene(scene)` already has this shape. | `dice_engine.roll_pool` / `continuous_engine_sample`; pool formula from the doc, attribute names via `descriptor_registry` |
| **W2** | `EvidenceView(keylog, observer_id) -> Iterable[Key]` | *what may this character see* | `Key.visibility` + `scene.witness` edges. **Closes GAP-A.** |
| **W3** | `Corroboration.confidence(keylog, proposition) -> int` | *how sure are we* — count of **independent** support chains, independence = disjoint `causes` ancestry | `Key.causes`. **Blocked on GAP-B.** |
| **W4** | `Assertion.assert_finding(view, claim) -> Degree` | *is the player right, and what happens either way* | `degree_from_net`; emits `scene.investigation_resolved` |

**W2 is simultaneously** the epistemological barrier (P-08 / P-03), the Case Board
(`investigation_systems_v30` System 2), its Thread Layer (ED-680), the Investigation Journal
(`fieldwork_v30` §10.3) and the Intelligibility Gradient's data source. One implementation, five
surfaces. It **owns no state**, and per the Outer Wilds rule (§2.6) it must render
**known-unknowns** — a Key whose `causes` chain has an antecedent the observer cannot see — or it
is a diary rather than a board. The Case Board's "connections drawn at Reconstruct" is literally
the `causes[]` DAG rendered.

**W3 collapses three same-question implementations**: `fieldwork_v30` §4.3 Evidence Quality,
`knots_v30` §4.5 Knot-sharing corroboration, `fieldwork_v30` §4.5 Thread-Read. It is Heaven's
Vault's mechanism exactly (§2.5): confidence accrues by matching across **independent** artefacts.

**W4** is Golden Idol's typed claim + L.A. Noire's evidence-binding + Sherlock's
competing-conclusions. Ground truth is never revealed (P-08); `finding: inconclusive` is a
first-class outcome **because the registry already says so** (`scene.investigation_resolved`:
`finding: exonerated | guilty | inconclusive`).

### §5.2 The five modules (contract shape — full YAML in §6)

| Module | Doc | Sim home | Status |
|---|---|---|---|
| `fieldwork_action` | `fieldwork_v30.md` §1–§4, §6 | `systems/fieldwork/sim/fieldwork.py` — **replaces the stub bodies in place**; `scene_dispatch.py:349` needs no call-site change | new contract |
| `fieldwork_social` | `fieldwork_v30.md` §5.1–§5.4, §5.9 | `systems/fieldwork/sim/social.py` (new); Disposition **stored on `npe.NPC`**, not here | new contract |
| `investigation_dialogue` | `investigation_systems_v30.md` Systems 3–4 | `systems/fieldwork/sim/investigation.py` — replaces stubs | new contract; **REFINE gate is build-blocking** |
| `fieldwork_sites` | `fieldwork_v30.md` §3.1–§3.3a | settlement-anchored (T3, §3.1:183) — SE-lane coordination | new contract |
| `fieldwork_knots` | `knots_v30.md` | `systems/fieldwork/sim/knots.py` | **EXISTS — extend, never recreate** |
| `fieldwork_content` | — | authored data pack, code-free | all Jordan/authorial |

### §5.3 The ladder seam — the one place fieldwork touches two degree owners

Two declared ladders exist and the divergence is deliberate and registered
(`sigma_leverage.py:292`, in `test_degree_ladder_single_owner.py`'s HELD registry). So:

- **non-contest fieldwork** — Discovery, Survey, Evidence actions, Disposition advance — uses `dice_engine.degree_from_net`;
- **escalation** at `fieldwork_v30` §5.7 hands off to `contest/wrapper.py:build_contest/resolve_contest` **and nothing else**, and *that handoff is where the ladder changes*.

This must be an explicit, tested seam. The social_contest lane's own audit found "three resolution
models under one name" (`HANDOFF_SC.md`); a fieldwork Lattice that grows its own escalation
semantics becomes model #4.

### §5.4 What fieldwork does NOT get

- No `Clue` / `Lead` / `Evidence` / `Rumour` class — a clue is a Key (§3, §4). *[AMENDED 2026-08-18 — §11.2: still no clue class, but a **belief layer is required and is not a Key**. A Key is an immutable event; much evidence is a mutable, per-agent proposition, and `state.belief_revised` already exists as its own type.]* A parallel clue store forks save/replay ("save = serialize the log") **and** the causal graph. The Evidence *Track* is a bounded counter (a **clock**, per the registry); each *piece* of evidence is a Key; the Journal is a read.
- No second Interview object — ED-FI-0004 already ruled the Dialogue Lattice the single home.
- No second NPC-response engine — the Response Matrix's five filters must each **read the owning module's state** (`conviction.py`, NPE genome, Disposition, contest rhetoric axes), not hold copies.
- No settlement writes — fieldwork emitting `scene.poi_discovered` and `settlement_layer` applying the bonus is correct; `settlement.prosperity += 1` inside a fieldwork resolver is the holonic-doctrine §2.1 violation outright.
- No Church-Attention arithmetic — fieldwork emits, `territorial_piety` consumes and applies §6.5's caps at *its* end.
- No bespoke timer, no new scale, no entity special-casing.

---

## §6 THE MODULE CONTRACTS — in `references/module_contracts.yaml` shape

Types marked **⊕** are **not** in the 55-type roster and require a `key_type_registry_v30.md`
registration *first* — `KeyLog.append` → `registry.validate_payload` raises on an unregistered type
(invariant 2, `keys.py:305`), so **a new fieldwork Key is a registry edit before it is code.**

```yaml
- module: fieldwork_action          # kernel wrapper — ADAPTS + ROUTES, resolves nothing
  doc: systems/fieldwork/fieldwork_v30.md              # §1–§4, §6
  sim_module: systems/fieldwork/sim/fieldwork.py       # replaces the stub bodies IN PLACE
  scales: [personal, scene]
  resolver: dice_pool     # pool = (registry-resolved Primary×2)+History+3 via dice_engine;
                          # degree via degree_from_net — NEVER private bands (§4b.2)
  consumes:
    - {type: "mechanical.scene_entered", from: [game_director]}
    - {type: "mechanical.accounting",    from: [engine_clock]}   # exposure reset, desperate-trail clear
  emits:
    - {type: "scene.evidence_gained", terminal: false}     # ⊕ investigation_id, delta, reliability_tag, depth, source_action
    - {type: "scene.poi_discovered",  terminal: false}     # ⊕ settlement_id, poi_category, degree
    - {type: "state.exposure_change", terminal: false}     # ⊕ territory_id, delta, threshold_crossed
    - {type: "scene.investigation_resolved", terminal: false}   # EXISTING — Reconstruct completion
  state:
    - {name: "Evidence Track", bucket: clock, writable: true}
    - {name: "Exposure",       bucket: track, writable: true}
    - {name: "Cover",          bucket: derived_value, writable: false}   # ⚠ no registry row yet (§4b.4)
  transitions: [{via: "scale_transitions §3.9 Fieldwork ↔ All Systems"}]
  accounting_phase: [settlement_accounting]

- module: fieldwork_social          # Disposition, non-contest social actions, Sincerity Gate
  doc: systems/fieldwork/fieldwork_v30.md              # §5.1–§5.4, §5.9
  sim_module: systems/fieldwork/sim/social.py          # NEW; storage on npe.NPC, not here
  scales: [personal]
  resolver: dice_pool
  consumes:
    - {type: "scene.contest_resolved", from: [social_contest]}   # post-contest ±1 shift (§2.3)
    - {type: "scene.gift",             from: [scene_slate]}
  emits:
    - {type: "state.disposition_change", terminal: false}   # ⊕ consumed by npc_behavior + dialogue gating
  state:
    - {name: "Disposition Track", bucket: track, writable: true}   # −5..+5 flat (ED-912), per (NPC, PC), asymmetric

- module: investigation_dialogue    # the ED-FI-0004 single Interview home
  doc: systems/fieldwork/investigation_systems_v30.md  # Systems 3–4
  sim_module: systems/fieldwork/sim/investigation.py   # replaces stubs
  scales: [scene]
  resolver: manifest      # gates evaluate deterministically; rolls delegate to fieldwork_action
  consumes:
    - {type: "state.disposition_change", from: [fieldwork_social]}
    - {type: "state.scar_acquired",      from: [piety_track]}     # Filter 2 conviction-wound routing
  emits:
    - {type: "scene.evidence_gained", terminal: false}   # via fieldwork_action's economy (ED-921 fix)
    - {type: "scene.dialogue",        terminal: false}   # EXISTING
    # escalation is NOT an emit — direct handoff to social_contest.build_contest
  gates:
    - {id: g_refine, when: "Response Matrix resolves",
       then: "compact 'why this NPC responded' readout emitted",
       source: "investigation_systems_v30 ED-FI-0004 REFINE — BUILD-BLOCKING"}

- module: fieldwork_sites           # POI registry + TS-gated visibility
  doc: systems/fieldwork/fieldwork_v30.md              # §3.1–§3.3a
  sim_module: settlement-anchored (T3, §3.1:183) — SE-lane coordination required
  scales: [settlement, territory]
  resolver: state_reader
  consumes:
    - {type: "scene.poi_discovered",        from: [fieldwork_action]}
    - {type: "env.peninsular_strain_shock", from: [peninsular_strain]}   # MS-conditional gates
  emits: []   # settlement bonuses applied by settlement_layer — NEVER written here

- module: fieldwork_knots           # EXISTS (module_contracts.yaml:373) — extend, never recreate
  # deltas only: emit its already-declared meta.knot_formed / meta.knot_ruptured as REAL Keys
  # (the sim emits none today); route apply_knot_loss's unapplied consequence fields to their
  # owners (Composure → contest kernel, Disposition → fieldwork_social); give form_knot its
  # Scene-Slate Priority-2 caller (§5.6a:473); call strain decay from run_accounting.

- module: fieldwork_content         # authored data pack, code-free (clock_registry precedent)
  # POI catalogs (ED-507), scene-graph templates, Lattice utterances, stance triangles,
  # starting Dispositions (ED-508). ALL Jordan/authorial — the engine consumes, never fabricates.
```

**Where these plug into contracts that already exist** (verified in `module_contracts.yaml`):
`scene.investigation_resolved` is already consumed by `faction_state` (:91) and `npc_behavior`
(:160) — the *emitter* side finally exists. `fieldwork_knots` emits already feed `npc_behavior`
(:151-152) and `piety_track` (:267). Domain Echo rides `scale_transitions §3.4` exactly as combat's
`scene.combat_resolved` does, and `domain_echo.compute_domain_echo(degree, …)` consumes a degree
label directly — so `fieldwork_v30` §2.5's Domain-Echo-from-investigation is usable **as-is**.

⚠ **One attribution note, surfaced not resolved:** `scene.investigation_resolved` already carries a
standing `[OPEN — Jordan]` dual attribution (`faction_politics` + `scene_slate`). Adding
`fieldwork_action` makes three claimants. **Do not silently resolve this** — it is Q3 below.

### Centralized definitions every module points at

| Identifier kind | Owner (single) |
|---|---|
| Key types | `systems/_architecture/key_type_registry_v30.md` → cooked `engine/engine_params/key_types.json` by `tools/export_key_types.py` (blocking round-trip) |
| Attributes / stats | `references/descriptor_registry.yaml` (+ `KeyLog(stat_vocabulary=…)` hook, `keys.py:345`) |
| Tracks / clocks / pools | `not_descriptors` in the same registry (`:190-196`) — Evidence=clock, Disposition=track, Fieldwork/Knot=pools |
| Degree ladder | `engine/autoload/dice_engine.py:104` |
| Module IO | `references/module_contracts.yaml` |
| Mechanics rows | `registers/mechanics_index.yaml` — rows `fieldwork`, `investigation_npe`, `disposition_track`, `evidence_track`, `knots` **already exist (:280-368) — update, don't add** |
| Names | `references/names_index.yaml` |
| Numbers | code, exported via a `tools/export_*.py` with a blocking `--check` (principle 7 / ED-1050) |

---

## §7 BUILD SEQUENCE — seven stages, each with a gate and a guard

Ordered by **dependency, not by appetite**. Note stages 0–2 are substrate and registry work: the
fieldwork lane cannot start with fieldwork.

| # | Stage | Gate (how we know it's done) | Guard (what fails on recurrence) |
|---|---|---|---|
| **S0** | **Author the five module contracts** into `module_contracts.yaml`. Contract before code — CLAUDE.md §6's own rule. | contract checks green; no `doc: null`; `_identifier_census.yaml` regenerates clean | existing contract CI |
| **S1** | **Register the ⊕ Key types** (`scene.evidence_gained`, `scene.poi_discovered`, `state.exposure_change`, `state.disposition_change`) + a `Cover` registry row. | `export_key_types.py --check` round-trip green; roster 55 → 59 | the existing blocking round-trip |
| **S2** | **Close GAP-A: build `EvidenceView`.** The one reader of `Key.visibility`. | a test asserting a non-observer cannot obtain a private Key through the view | **G1**: no module outside the view may read `visibility` — a write/read sweep in the `tests/valoria/test_morale_write_sweep.py` `_CELL_OWNED` style |
| **S3** | **Close GAP-B: populate `causes` at fieldwork emit sites** (and file the cross-lane ask for the two `causes=[]` faction sites). | every Key a fieldwork module emits cites its antecedent | **G2**: a test failing on a fieldwork Key emitted with empty `causes` and a non-root cause |
| **S4** | **Replace the `fieldwork.py` / `investigation.py` stub bodies.** No call-site change needed (`scene_dispatch.py:349`). Transcribe **yield columns only** (§4b.2). | ED-916's own condition — continuous-engine validation at fieldwork parameters, seeded and deterministic | **G3**: extend `test_degree_ladder_single_owner.py` to fail on any fieldwork module computing a band itself |
| **S5** | **Add `"fieldwork"` to `evaluable`** and wire the triggers. This is §4b.1's one-line gap plus its trigger definitions. | a seeded campaign in which a fieldwork scene is organically queued, resolved, and its Key consumed downstream | **G4**: a test asserting the `deferred` list does not silently swallow a fieldwork trigger |
| **S6** | **`Corroboration` + `Assertion`**, then the **solvability invariant** on the generator. | generative test: for N seeded worlds, a reachable Key-chain exists from starting visibility to the true assertion (§2.3) | **G5**: the generative test itself — this is the falsifier that makes the whole design honest |
| **S7** | **Typed fieldwork params export**, mirroring `tools/export_engine_params.py`. | blocking `--check` round-trip in CI | existing pattern |

**Three stages are explicitly gated on Jordan and cannot be started**: S4 needs Q1 (the obstacle
model) because it decides every number; `investigation_dialogue` needs Q4 (the REFINE gate); and
the attribute question Q2 blocks any pool that names Recall or Cognition.

---

## §8 WHAT IS GENUINELY NEW — the whole list

Per the steering instruction, everything else is wiring. The new set is four items:

1. **ED-FI-0002 counter-espionage response surface** — the subsystem's one acknowledged new design, and even here the trail is Keys the rival DA already emits (`da.covert_betrayal` is a registered type); detection is an investigation whose evidence source is that Key stream.
2. **State homes + their ⊕ Key types** — Evidence Track, Exposure, Disposition, POIs. Mechanical, but genuinely absent: no World or NPC field exists for any of them today.
3. **The Response-Matrix legibility readout** — required by the build-blocking REFINE gate; its shape is unruled.
4. **Authored content packs** — POI catalogs, scene-graph templates, utterances, stance triangles, starting Dispositions. All flagged `[EDITORIAL — requires user approval]` **in the CANONICAL doc itself**; an implementation that fabricates them violates the no-fabrication gate.

Plus three **architectural** additions that are new as *code* but not as *design intent*:
`EvidenceView` (P-08 made executable), `Corroboration` (three same-question sites collapsed to one),
and the solvability precondition (§2.3). *[CORRECTED 2026-08-18 — §11.1: this was claimed as "the only genuinely new idea". **Withdrawn.** It is this repo's existing hook grammar applied to evidence, and the pattern has been in the tree since 2026-04-11. The genuinely absent primitive is instead the **belief layer** of §11.2.]*

---

## §9 THE CALLS THAT ARE JORDAN'S

| # | Question | Options and what each costs |
|---|---|---|
| **Q1** | **Does the score/2 obstacle ruling extend to environmental obstacles?** Fieldwork's Depth table (Ob 1/2/3/5/8) is environment-derived; the ruling derives Ob from an opponent. | (a) Depth table stands as the environmental branch — cost: two obstacle models, needs an explicit which-applies-when rule. (b) Depth becomes a site "score", values re-derive — cost: recalibrates every SIM-DEBT-FW result. (c) score/2 for contested only — cheapest, but overwrites §4.6's roll-based Concealment Ob. **This decides every number in the subsystem; S4 cannot start without it.** |
| **Q2** | **What rolls Research / Reconstruct / Interview?** Recall is absent from the ruled roster; Cognition is only an `[ASSUMPTION]` alias of Acuity; the tenth attribute is unnamed. | (a) re-key to Acuity — cheap, flattens Investigation's attribute spread. (b) **the unnamed tenth attribute is Recall-shaped** — resolves this and the tenth-slot workshop at once. (c) adopt the 2026-08-15 proposal's acquisition-layer answer and drop attribute-primaries — most aligned, largest redesign. |
| **Q3** | **`scene.investigation_resolved` attribution.** It has a standing `[OPEN — Jordan]` dual attribution; `fieldwork_action` would be a third claimant. | Make fieldwork the primary emitter (the semantically right answer) vs. keep all three vs. split the type. Surfaced deliberately rather than resolved. |
| **Q4** | **Is the Dialogue Lattice in scope for the first build, or does the bare-roll baseline ship first?** The REFINE gate blocks the Matrix build on a legibility answer. | (a) baseline-first — fast, builds a thing scheduled to retire. (b) Lattice-first with the §E0 wrapper fixes — honors the MERGE, needs REFINE ruled. (c) both, flag-gated — recreates the exact EP-8 state the MERGE closed. |
| **Q5** | **Is ground truth ever confirmed to the player?** Heaven's Vault ("never quite sure") vs Obra Dinn (verified). | Never-confirmed preserves P-08 intact and matches Pentiment; confirmation is more satisfying but needs an in-fiction channel that does not dissolve the barrier. Note `finding: inconclusive` is already canon either way. |
| **Q6** | **How hard is the solvability invariant?** Every generated case solvable, vs P% of seeds. | A hard guarantee constrains the generator heavily. A soft one is defensible — Pentiment and Paradise Killer both ship unsolvable-but-actionable as a *design*, and `inconclusive` is already a legal finding. |
| **Q7** | **ED-FI-0008 (P-06)** — confirm threadcut-Coherence → self-maintenance-strain, so the sim never implements the FAIL-marked model. Already `needs_jordan`; the plan needs only yes/no before knot-lifecycle wiring. | — |
| **Q8** | **ED-FI-0006 / 0007** — wound-language sign-off (+0.15 Ob/wound everywhere; strike the −1D and flat +1 Ob remnants). Mechanically already decided by ED-PC-0005/0006. | — |
| **Q9** | **Where does per-NPC Disposition live** — on `npe.NPC` uniformly (recommended), or a separate relationship registry? | Decides the NPC-side schema migration. |

---

## §10 WHAT WOULD FALSIFY THIS

Per §0.1 point 3, each claim carries the check that would show it wrong, and whether it was run.

| Claim | Falsifier | Ran? |
|---|---|---|
| Fieldwork has no module contract; the sims are stub-wired | read both sim files; `grep` `module_contracts.yaml` | ✅ both, first-hand |
| CLAUDE.md §6's "10/27 `doc: null`, 11/27 `[ASSUMPTION]`" | parse the YAML, don't `grep -c` | ✅ — **and BOTH numbers are wrong: the true figures are 9/27 and 10/27** (§4b.5) |
| **GAP-A** — `Key.visibility` has no reader | `grep -rn "private_observers\|semi_public_observers" --include=*.py engine/ systems/ tools/` — returns only the dataclass, its serializer, and the constructor-side validator | ✅ **If a reader exists under another name, §5.1-W2 is already built and S2 is unnecessary.** |
| **GAP-B** — `Key.causes` is unpopulated | `grep -rn "causes=" --include=*.py engine/ systems/` — 3 non-test sites, 2 of them `causes=[]` | ✅ **If emitters populate `causes` through a helper this grep missed, S3 is unnecessary and W3 is unblocked today.** |
| **§4b.1** — only "Stability Crisis" is evaluable; only `"contest"` is ever queued | read `scene_dispatch.py:96`; `grep -rn '"scene_type":'` over `engine/`+`systems/` | ✅ first-hand, both legs |
| The fieldwork dispatch seam is pre-cut | read `scene_dispatch.py:344-360` | ✅ (it says so in its own comment) |
| Two degree ladders, deliberate | read `dice_engine.py:104` + `sigma_leverage.py:292` and its HELD note | ✅ |
| `scene.investigation_resolved` already carries `inconclusive` | read the registry entry (L880) | ✅ |
| `scene.witness` carries `observed_key_id` — the provenance edge already exists | read the registry entry (L63) | ✅ |
| **Precedent claims (§2)** | Each is a published, widely-documented mechanic; Brindlewood's Theorize move and Heaven's Vault's corroboration ladder were re-verified against external sources on 2026-08-18. The rest are stated from knowledge at the confidence tagged. **No quotation is attributed to any designer.** | partial by design |
| **Inference, not fact** | §5's decomposition, §6's contracts and §7's sequence are **design proposals**. Every "exists / is absent" claim above is tree-verified; nothing in §5–§7 is. | — |

**The one claim most likely to be wrong, and the one to attack first:** that a clue can be a Key
with no loss. If evidence turns out to need per-observer *mutable* state — a reliability tag that
differs by who holds it, or a partial reading that upgrades — then a Key (immutable once appended)
is the wrong carrier and §5.4's "no Clue class" collapses. The falsifier is cheap: try to express
`fieldwork_v30` §4.3's reliability tags and the P-08 half-value rule purely as Key payload +
`EvidenceView` filtering. **That test has not been run**, and it should be S2's first act.

---

# §11 RECONCILIATION — the adversarial pass, folded in

Added 2026-08-18, same day. §1–§10 were critiqued adversarially; **one objection was overturned by
a Jordan ruling, two were sustained and change the design, and the rest are accepted as
corrections.** Per §0's rule that producing and checking are different jobs, this section is the
checking half — kept as a visible reconciliation rather than a silent rewrite, so the next reader
sees what changed and why.

## §11.1 JORDAN'S RULING — scripting hooks and sequences is ALLOWED; scripting arcs is not

> **"We can script narrative hooks and sequences so long as we don't script entire arcs.
> We've done it with the coup counter, for example."** — Jordan, 2026-08-18

**This overturns the critique's objection to §2.3, and it is load-bearing on the whole design.** The
tree carries two worked precedents, and they draw the line precisely:

| Precedent | What IS scripted | What is NOT scripted |
|---|---|---|
| **Löwenritter coup / graduated autonomy** (`systems/factions/factions_personal_v30_infill.md:74-77`; track per ED-781/ED-767) | A private counter that **never decrements** (:76); a **guaranteed** fire at threshold — "when it reaches 3, the Split fires at the next seasonal accounting" (:74); a fixed consequence sequence — Martial Law on all Crown-held territories simultaneously (:77) | *When* it trips, *who* pushed it there, what the player does about it, and everything downstream. The trigger is emergent state (Crown Stability, Ehrenwall's Disposition, accumulated failure marks) |
| **Royal Assassination as Fuse** (`systems/_architecture/conflict_architecture_proposal.md:85-89`, **CANONICAL**) | One per campaign; fires at S8+; **"succeeds when it fires — no attempt/failure variance"**; target fixed at game start | The season within S8–S12; the target (deck draw / randomized); whether the player detects and averts it; the entire consequence arc per target (:91+) |
| **Baralta's Crown Claim** (`systems/factions/baralta_crown_claim_v30.md:17, :26-40`; Status: DESIGN, ED-408) | A scripted **conjunction of world facts** that must obtain: Crown eliminated (Mandate 0 + Loyalty 0) **or** Royal Deposition (PI ≥ 5 + Church Mandate ≥ 5 + Crown Mandate ≤ 1 + 2 Standing tokens); then per-claimant conditions — *Baralta alive + Hafenmark Mandate ≥ 4*, *Löwenritter Autonomy ≥ 3*, *CI ≥ 40* | **Whether any of those facts ever obtain**, by what route, who else qualifies, and who wins the resulting Succession Contest |

And the same document draws the boundary explicitly at the *arc* level: emergent narrative comes
from fragmentation checks, bishop appointments and black-market emergence — **"all system-driven,
no scripting"** (:156). So `conflict_architecture_proposal.md` is itself the worked example of the
ruling: a scripted fuse sitting inside an unscripted narrative economy.

### The Crown Claim generalizes it — and dissolves the invariant into existing grammar

Jordan's third precedent is the decisive one: *"there are going to be certain worldly facts that
she must navigate in order for her Crown Claim to occur."* Read the condition column above — the
hook **is** a scripted conjunction of world facts, and everything about whether those facts obtain
is emergent. Nothing scripts the arc; the script is the *predicate*.

That is the same object as a case's solvability precondition, and it means:

> **A case is a scripted conjunction of world facts that must obtain for a finding to be reachable
> — expressed exactly the way `baralta_crown_claim_v30` expresses a claim's conditions.**

So the "solvability invariant" is not a new mechanism, not a constraint on the sim, and not an
import from Blade Runner '97. **It is this repo's existing hook grammar, applied to evidence.**
§8's "genuinely new" list loses another entry: the invariant is a *condition table*, and the tree
has had the pattern since 2026-04-11.

**Note the assassination fuse is already an investigation hook** — *"Player can investigate (costs
card slots). If the player identifies and stops the plot: assassination averted, but the
investigation itself reveals faction-level tensions and NPC allegiances"* (:89). Fieldwork does not
need to invent its hook grammar. **It has a CANONICAL one, and it is unbuilt.**

### What this does to the solvability invariant (§2.3, §8)

The critique argued the invariant was forbidden scripting, because the world sim can destroy an
evidence chain — a witness dies in a mass battle, a settlement is sacked — so it could only be held
by constraining the sim, which is scripting drift at world scale.

**Half of that was right and the conclusion was wrong.** Under the ruling:

- **Guaranteeing a case is solvable AT GENERATION is a scripted hook** — the same class of object as "the assassination succeeds when it fires". **Legitimate.**
- **Maintaining solvability against the sim would be a scripted arc** — constraining who may die so the chain survives. **Forbidden**, and the critique was right about that half.

So the invariant survives in a better form than either draft had:

> **Generate solvable, let the world erode it, and make the erosion legible.** Solvability is a
> generation-time precondition, never an ongoing constraint. A witness who dies before you reach
> them is not a bug in the invariant — it is the Pathologic texture the game already wants, and it
> is exactly what makes `finding: inconclusive` a real outcome rather than a consolation.

Erosion is then *content*, and it is measurable: the fraction of generated cases still solvable at
season N is telemetry on how hard the world bites, not a gate. **§8's "the only genuinely new idea"
claim is withdrawn** — the invariant is not new, it is the assassination fuse applied to evidence.

## §11.2 SUSTAINED — a Key is an event; evidence is often a proposition

The critique's strongest hit, and it stands. `Key` is an **event**: `emitted_at`, `causes`,
immutable once appended. Much evidence is a **proposition** — *"the steward was in Varfell that
night"* — which is atemporal, can be **false**, and is **held at different confidence by different
agents**. Collapsing the two means false belief has no clean home, two characters cannot hold
contradictory readings of one artefact without minting divergent Keys that pollute the log with
non-events, and confidence cannot change without a new event.

**The tree already answered this and §5.4 walked over it: `state.belief_revised` exists as its own
type.** So the corrected architecture is two layers, not one:

| Layer | Carrier | Mutable? | Owner |
|---|---|---|---|
| **Observation** — *what happened, who saw it* | `Key` + `scene.witness` edges + `causes` ancestry | no (append-only) | `engine/substrate/keys.py` |
| **Belief** — *what an agent holds true, at what confidence* | per-agent propositions, revised via `state.belief_revised` | **yes** | new, and it is the real absent primitive |

`EvidenceView` (§5.2) is therefore **not** the whole answer — it is the *observation* filter, and a
belief layer sits on top of it. §5.4's flat "no Clue class" is **amended**: no clue class, but a
**proposition** record is required and is not a Key.

**Consequence for §7: S2 is re-ordered.** Its own falsifier — can `fieldwork_v30` §4.3's
reliability tags and the P-08 half-value rule be expressed as Key payload + view filtering? — must
run **before** S2 builds, not as S2's first act. The answer is now expected to be *no*, which is
why the belief layer is named here rather than discovered mid-build.

## §11.3 SUSTAINED — the information economy already half-exists, and §5 builds pipes past it

`module_contracts.yaml:192-195` declares `npc_behavior` as emitter of **`state.opinion_revised`**
(per drift threshold), **`scene.interaction`** (per ambient pair) and **`scene.gossip`**
(cumulative_drift > 0.5). The NPE that drives them is **built and season-wired**
(`systems/world/sim/npe.py`, called from `systems/overview/sim/accounting.py`).

That reframes the subsystem's thesis. Investigation in Valoria is not *"find the authored clue"* —
it is **"tap a rumour network that runs whether or not you look, while your own tapping leaks back
out through Exposure."** Information propagates on its own; the investigator intercepts, and is
intercepted.

⚠ **Stated at its true strength, not higher:** those three types are **contract-declared and not
implemented** — no `.py` in the tree emits a gossip or opinion Key today. This is a
designed-and-half-built opportunity, not a running one. Overstating it would be the same defect
this document was written to avoid.

**Consequence for §5:** the decomposition is sound but mis-centred. The organising loops are:

```
   NPE drift ──► scene.gossip / state.opinion_revised ──► EvidenceView ──► belief layer
        ▲                                                                      │
        │                                                                      ▼
   Exposure ◄──── what you spend to learn ◄──── investigation actions ──► Finding
                                                                              │
                        ┌─────────────────────────────────────────────────────┤
                        ▼                                                     ▼
        contest Dossier/EvidenceItem                          settlements ledger.py Leverage
        (dice for the argument)                               ("a hook the player holds",
                                                               durable across succession)
```

**The central player decision is "what do you expose in order to learn?"** — because Cover/Exposure
already couples investigation to Church attention and faction notice. §5.1's "allocate pool across
sites" is the thin version of this and should be subordinate to it.

## §11.4 ACCEPTED CORRECTIONS

| # | Correction | Where it lands |
|---|---|---|
| C4 | Architecturally rich, gameplay-thin — no decision texture specified | §11.3's Exposure loop is the answer; §5.1 demoted |
| C5 | Cross-system coupling asserted, not designed. `ledger.py`'s **Leverage** is literally *"a hook the player holds (e.g. konrad-corrupt)"* — investigation is the **acquisition path for a resource factions already spend**. Contest's `Dossier`/`EvidenceItem` makes investigate→dossier→contest a **complete loop already half-built**. **Combat coupling is entirely absent** — whether you know the garrison strength decides whether combat happens on your terms | §11.3 diagram; combat coupling filed as open |
| C6 | Personal/scene-scoped plan wearing a multi-scale label. `Intelligence Holdings` is a registered faction-side derived value (`descriptor_registry.yaml:192`); BG Survey is an existing faction action. **A spy network and a personal investigation should be the same mechanic at two scales** — the actual multi-scale claim | Filed as the strongest unexplored direction |
| C7 | "The gap is one line" overweighted. Adding `"fieldwork"` to `evaluable` is **necessary and nowhere near sufficient** — it needs trigger definitions, a resolver, and state homes. It is a **seam**, not a gap | §4b.1's framing corrected here |
| C9 | Precedent selection biased toward **authored, finite, single-case** mysteries; the genuinely applicable generative precedents (Shadows of Doubt, Blade Runner '97, Dwarf Fortress) got the least detail and the only `[MED]` tag | §2 acknowledged as centre-of-gravity-wrong for a campaign game |
| C10 | Seven stages and three rulings before one playable scene, in a subsystem stubbed since 2026-05-17. **A deliberately ugly vertical slice** — one trigger, one site, one roll, one Key, one consequence — de-risks more than S0's contract authoring, and the assassination fuse (§11.1) is the ready-made trigger | Recommended as the revised S0 |

## §11.5 REVISED SEQUENCE — what actually changes in §7

1. **New S0: the vertical slice.** Take the CANONICAL assassination fuse as the hook. One trigger, one site, one roll through `degree_from_net`, one Key, one consequence into `ledger.py` as Leverage. Ugly, end-to-end, playable. It answers more design questions than contract authoring does, and it exercises the seam that `scene_dispatch.py:344` already cut.
2. **S2 is gated by its own falsifier** (§11.2), and the belief layer is expected to be needed.
3. **Solvability is a generation-time precondition with erosion telemetry** (§11.1), not a maintained constraint.
4. Everything else in §7 stands.

## §11.6 WHAT WOULD FALSIFY THE RECONCILIATION

- **§11.1** — if the coup counter and assassination fuse turn out to be `PROPOSED` rather than canonical, the ruling's in-tree support weakens. **Checked:** `conflict_architecture_proposal.md:2` reads `## Status: CANONICAL`, `:4` "CANON — approved by Jordan"; the Löwenritter track is live in `factions_personal_v30*`. ⚠ **`baralta_crown_claim_v30.md:6` is `## Status: DESIGN (editorial decision, flagged for review)` under ED-408, NOT canonical** — so it demonstrates the *grammar* and does not by itself ratify it. Two canonical precedents plus one design-tier one; the ruling holds on the first two.
- **§11.2** — falsified if `state.belief_revised`'s registry entry turns out to be an *event* record with no per-agent confidence semantics, in which case the belief layer needs authoring rather than adopting. **Not checked** — read the entry before building S2.
- **§11.3** — falsified if a gossip/opinion emitter exists under a name my grep missed, which would upgrade the opportunity from half-built to running. **Grep run**, `.py` only; a GDScript or data-driven emitter would not have been caught.

## §11.7 THE UNIFICATION — worldly facts, and the two ways they perdure

Jordan, 2026-08-18, extending the ruling three times in one sitting:

> *"a drought within a territory causing crops to fail for a settlement, which causes food supply
> and taxation issues offset by the Church buying favour in the area through its donations which in
> turn allows it to build more infrastructure. All of these involve keys and conditions to be met
> for worldly facts that propagate … players, characters and factions [can] see impacts in the
> settlement and at the level of governance and parliament, argue and present what to do about the
> current state of things and why. **It's just composites of worldly facts.**"*
>
> *"Church Influence hitting a certain point to enable attempted territory seizures and a pivot to
> a theocratic military campaign is another major scripted moment."*
>
> *"Maybe the Church donates, maybe it doesn't. Maybe a duchy steps in. Maybe there's just famine.
> Who's to say? But **the facts emerge and perdure in the world whether temporally and materially
> or in memory later.**"*

### The second example is already built, and it settles the pattern's status

`mechanical.theocracy_unification_declared` is a **registered Key type** whose description reads:
*"CI reaches 100 — Church publicly declares Papal Sovereignty and triggers the one-shot Mass
Seizure on every territory with Church buildings (ci_political_v30 §2.2)."* A threshold over
emergent world state, a guaranteed consequence, no roll. The registry note even records that it was
registered **once** to close two silent emitters "rather than duplicating a type per module" —
single-owner discipline applied to a scripted hook.

And it is not exceptional. The same shape recurs across the roster:

| Registered type | Predicate over world state | Guaranteed consequence |
|---|---|---|
| `mechanical.theocracy_unification_declared` | CI reaches 100 | Papal Sovereignty + one-shot Mass Seizure on every Church-building territory |
| `state.settlement_revolt` | Settlement Order reaches 0 | Local revolt; governor expelled unless a garrison is present |
| `mechanical.settlement_captured` | Defense 0, no garrison, hostile military entry | **Auto-captured — no roll** |

**So "scripted hook" is not a concession the architecture has to make room for. It is already the
tree's dominant idiom, registered in the Key type roster, and the fieldwork plan should have been
written in it from the start.**

### The unification

Putting the three statements together with the substrate as read:

> **A worldly fact is a Key.** A **scripted hook is a predicate over composites of worldly facts** —
> `baralta_crown_claim`'s condition column, `CI ≥ 100`, `Order = 0`, `Autonomy = 3`.
> **Nothing scripts the response.** Whether the Church donates, a duchy steps in, or there is simply
> famine is faction logic weighing its own position — emergent, per Jordan's *"who's to say?"*

And the last clause is the one that closes the design, because **the schema already distinguishes
the two modes of perdurance Jordan names**:

| Perdures… | Carrier in the tree | Property |
|---|---|---|
| **temporally and materially** | the `KeyLog` itself + the state Keys wrote — `Key.permanence` ∈ `transient / persistent / indelible`, `Key.time_horizon` ∈ `immediate / near / far` | complete, append-only, indifferent to who saw it |
| **in memory later** | per-agent belief — `state.belief_revised`, the `npc_memory` module, `Key.visibility`, `scene.witness` edges | **partial, revisable, and can be wrong** |

**The gap between those two columns is the investigation surface.** That is the thesis this document
lacked and now has:

> **Fieldwork is the mechanic by which memory is reconciled against the material record — and P-08's
> epistemological barrier is precisely the guarantee that the two never fully converge.**

### What this does to the plan

1. **Fieldwork stops being a subsystem and becomes the epistemic layer of the whole game.** The same predicate language serves four consumers that today each roll their own: hooks fire on it, investigations discover whether it holds *and to whom*, **parliament arguments cite it**, and faction actions gate on it. Jordan's *"argue and present what to do about the current state of things and why"* is a social contest whose claims are world-fact predicates — which is exactly why contest already has `Dossier`/`EvidenceItem`.
2. **§11.2's belief layer is promoted from a correction to the centrepiece.** It is the "memory" column, and it is the one genuinely absent primitive in the whole design.
3. **The Church-donation branch is the worked test of "no scripted arc":** the *predicate* (drought → failed harvest → shortfall) is scripted; the *response* (Church donates / duchy intervenes / famine) is three factions weighing an emergent state. If a build ever hardcodes which one happens, that is the scripting-drift line being crossed, and it is now testable.

### ⚠ A verified hole in Jordan's own example chain

The drought chain is **typed at both ends and hollow in the middle.** `env.disaster` covers blight
and is consumed by `settlement_layer`; `env.population_change` is emitted by it. But:

- **`settlement_economy` has `doc: null`, an empty `emits:` list, and an empty `state:` list** — it consumes `da.economic_intervention` and `env.population_change` and produces nothing.
- **There is no food, harvest, granary or taxation code anywhere** in `systems/` or `engine/` (grep, `.py`).

So *drought → crop failure* is expressible today and *crop failure → food supply → taxation* is
not. That is a `settlement_economy` authoring gap (SE lane), not a fieldwork one — filed here
because it is load-bearing on the example Jordan chose, and because §6's "no `doc: null`" gate
would catch it the moment anyone tried to wire the chain.

## §11.8 ONE RESOLUTION GRAMMAR — verified, with the gap that stops it being one today

> *"Field investigations give us a framework to explore narrative moments and set arcs in motion,
> and their logic is scalable because of how our key schema works: a solution to a mystery is the
> same as the conclusion to a negotiation is the same as a debate in parliament is the same as
> developing a scar against an actor is the same as challenging a belief or meeting a goal: it's
> all about keys and how they log worldly facts, interactions and outcomes."* — Jordan, 2026-08-18

**Checked against the registry. The claim is right about the envelope and the tree does not yet
honour it in the payload** — which is the most actionable finding in this document.

### What is already one thing (the envelope)

Every terminal outcome Jordan names is a `Key`, and they share the whole envelope: `targets[]` with
a `role` from the canonical five and an `impact_vector` over the canonical four axes, plus
`visibility`, `permanence`, `time_horizon`, `causes` and `scale_signature`. **That is the scalable
grammar, and it is real** — a mystery's solution and a parliamentary vote genuinely propagate
through identical machinery.

### What is five things (the payload)

| Outcome Jordan names | Registered type | Its "how did it come out" field |
|---|---|---|
| solution to a mystery | `scene.investigation_resolved` | `finding: exonerated \| guilty \| inconclusive` |
| conclusion to a negotiation / debate in parliament | `scene.contest_resolved` | `outcome: initiator_win \| target_win \| compromise \| stalemate` |
| developing a scar against an actor | `state.scar_acquired` | `scar_count_before` / `scar_count_after` |
| challenging a belief | `state.belief_revised` | `prior_belief` / `new_belief` — **free strings** |
| meeting a goal | `state.project_completed` / `state.project_failed` | `completion_effect` |

**Five bespoke vocabularies for one concept, and not one of them is the degree ladder.** The tree
single-owned *resolution* in `degree_from_net` (Jordan, 2026-08-14) and never single-owned the
*record of a resolution*. So the outcomes propagate through one envelope and cannot be compared,
aggregated or reasoned over as a class — which is exactly what "argue and present what to do about
the current state of things" (§11.7) requires.

Two consequences fall straight out:

1. **The unifying move is a shared outcome shape on the payload** — a `resolution` field carrying
   the `Degree` the ladder already produces, plus a valence, with each type's existing field kept
   as its domain-specific detail. `scene.investigation_resolved`'s three-valued
   `exonerated / guilty / inconclusive` is the closest existing thing to the general shape, and
   `inconclusive` is the member the other four mostly lack.
2. **`state.belief_revised`'s free-string payload is a direct blocker for §11.2's belief layer.**
   A belief layer needs machine-comparable propositions — you cannot corroborate, contradict or
   cite `prior_belief: "short string"`. Note also its description reads *"Player Belief revision per
   fieldwork_socializing §5.5"*, which is in-tree evidence that the standing
   `[OPEN — Jordan]` attribution on this type resolves **toward fieldwork** (§9 Q3's neighbour).

This also sharpens the earlier social-contest finding — that lane's audit found *"three resolution
models under one name"* (`HANDOFF_SC.md`). Corpus-wide the number is larger, and the fieldwork lane
is where it becomes load-bearing, because investigation is the subsystem whose whole job is to
produce comparable claims about the world.

**Filed, not fixed:** unifying the outcome payload is a cross-cutting IN/SC/FI change touching five
registered types and their consumers. It is out of scope for an FI-lane proposal to execute, and it
is the single highest-leverage thing this session found.

---

# §12 CORRECTIONS — three claims in this document are false

Added 2026-08-18 after merge, from a read-only audit pass. Recorded inline rather than silently
edited, per the convention §11 used. **All three were verified independently before filing.**

## §12.1 §11.8's headline claim is false at roster scale

§11.8 states five outcome vocabularies exist and *"not one of them is the degree ladder."* **True of
the five types sampled; false of the 55-type roster.**

- **`mechanical.scene_exited.outcome_class` (registry :403) is `overwhelming | success | partial | failure | unknown`** — verbatim the `dice_engine.Degree` enum values (`dice_engine.py:24-28`) plus `unknown`. A terminal outcome carrying the ladder **already exists**, is emitted by `game_director`, and is the closest in-roster precedent for the `resolution` field §11.8 proposes — closer than `investigation_resolved.finding`.
- `scene.combat_hit.degree` (:943) carries the combat kernel's variant (`graze | partial | success | overwhelming`); `meta.thread_woven.degree_of_success` (:1065) is a third degree-shaped field with no declared vocabulary.

**The census is also larger than five:** 9 enumerated verdict vocabularies, 7 before/after
transition pairs, plus type-as-outcome splits (`state.project_completed` / `state.project_failed`).
Two findings outrank the original: the **`da_outcome` family is headed "Domain Action results" and
4 of its 5 members carry no outcome field at all**; and the **indeterminate outcome already exists
roster-wide under five spellings** — `inconclusive` (investigation, coup), `unknown` (scene_exited),
`stalemate` (dialogue, contest), `draw` (combat_resolved), null-`victor` (battle_concluded). That
*strengthens* the unification case: the class is universal, only the naming is fragmented.

**And the fragmentation already costs something in shipped code:** `echo_transport.py:103-108`
(`_OUTCOME_BY_DEGREE`) down-converts the ladder into the bespoke vocabularies **lossily** at emit
time — Overwhelming and Success collapse to one token — while `_derive_degree` (:187-197)
reconstructs a degree going the other way. The seam pays conversion costs in both directions today.

## §12.2 §5.2's "no call-site change needed" is false

§5.2 states `fieldwork_action` "replaces the stub bodies in place; `scene_dispatch.py:349` needs no
call-site change", citing that line's own comment: *"ctx/world are threaded through so a future real
resolver drop-in needs no call-site change here."*

**The comment is wrong about its own code.** `scene_dispatch.py:354` passes only
`_fieldwork_mod.run_fieldwork_scene(ctx.get("scene"))` — **`world` is not passed**. Only the
investigation branch (:356) receives it. A fieldwork resolver that must write a Leverage tag or
reach the scheduler cannot, without a call-site change. This document took a code comment at face
value instead of reading the line beneath it.

## §12.3 §11.2's "adopt `state.belief_revised`" is falsified

§11.2 proposed adopting `state.belief_revised` as the belief layer. It cannot serve:

- `prior_belief`/`new_belief` are **free strings** (:1121-1122); **no confidence field** exists.
- Its registered semantics are the **PC creed-Belief beat** — `fieldwork_socializing.md:104-110` is the Belief *Momentum* economy (aligned / challenging / betraying), `permanence: indelible`, Tier-2 cut scene — not an epistemic claim about the world.
- `state.opinion_revised` (:1156-1177) is the shape template instead: `confidence_before/after int [1,5]`, `driver_memory_refs` provenance, `private_observers` visibility.
- It is **inert**: zero emitters; its one code consumer (`articulation.py:126`) subscribes and routes to `stubwire.stub_resolve` without reading the payload.

**Also, §11.8's reading that the "per fieldwork_socializing §5.5" citation resolves the standing
attribution toward fieldwork is overdrawn.** The citation fixes the type's original referent as the
PC creed beat; it does not settle who emits for NPC belief revision, and `module_contracts.yaml`
carries a **three-way** tension (`npc_behavior` :187, `fieldwork_knots` :392, plus npc_behavior
consuming it from `fieldwork_knots` :163). Still genuinely `[OPEN — Jordan]`.

**Disposition:** superseded by `proposals/2026-08-18-epistemic-propositions-and-provenance.md`,
written to Jordan's directive that epistemic propositions be available alongside provenance
references. `state.belief_revised` keeps its registered meaning; the epistemic layer is a separate
thing, homed in the already-declared-and-empty `npc_memory` module.

## §12.4 What survived the audit unchanged

§11.3 (no gossip/opinion emitter exists) was re-checked at full-tree scope — GDScript, YAML/JSON,
and dynamic type construction, beyond the original `.py`-only grep — and **stands**. The live tree
has exactly four `Key(` construction sites and none can produce those types; `npe.py` contains no
`emit`, `Key(` or scheduler use at all. §11.1's ruling precedents and §11.7's unification are
unaffected.
