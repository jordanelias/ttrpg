# The Wiring Map — every required connection, where it lands, and whether it is coded or merely designed

## Status: FINDINGS — a connection map, not a work plan and not a design. Nothing here rules anything. No `.py` touched. Content/design only; another session owns the restructure. Reconciliation against that work pending.

**Date:** 2026-08-22 · **Input:** `proposals/2026-08-19-subsystem-delta-and-narrative-robustness.md` (and its §8 falsifier record) · **Method:** a Fable 5 read-only pass barred from pattern-matching, then independent re-verification by parser and by reading for every load-bearing claim (§9 records which).

**What this document is for.** The delta said *what is broken*. This says *what would have to be connected to what, where the connection would physically go, and whether the thing on each end exists*. It deliberately does not estimate effort, rank by importance beyond what dependencies force, or propose new design. Where design is missing it says **DESIGN GAP** and names the unmade decision.

**The five status terms are the whole product.** Confusing them is how this corpus has repeatedly mis-scoped work:

| Term | Meaning |
|---|---|
| **CODED** | exists in `.py` and runs in a live path |
| **CODED-BUT-UNREACHED** | exists and is correct; no production caller |
| **STUBBED** | a `stubwire.stub_resolve` (or equivalent typed no-op) holds the seam open |
| **DESIGNED-ONLY** | specified in `.md`/`.yaml`; no `.py` at all |
| **UNSPECIFIED** | nobody has designed it and nobody has built it |

---

## §0 THE TWO HEADLINE CORRECTIONS — this map breaks the delta's own recommendations

Read this before anything else. The delta's two most quotable claims do not survive the map, and both were mine.

### §0.1 "The single missing artifact is a loader" — FALSE. It is a loader plus five unmade decisions.

The delta's §6 said the 46 authored characters were *"authored, structured, canonical and machine-readable"* and that only a loader was missing. I re-parsed the file rather than trusting that. **The registry does not fit any coded destination:**

- **Only 7 of 46 entries carry a territory at all.** The other 39 have none. `world.npcs` is *territory-keyed* (`game_state.py:188`), so **39 of 46 authored people cannot be placed without a decision that does not exist.**
- **The 7 that do carry one are formatted wrong for the key.** They read `"T15 (Southernmost)"`, `"T1 (Valorsplatz)"`, `"T9 (Himmelenger)"`, `"T14 (Ehrenfeld)"`, `"T16 (Schoenland)"` — the live map is keyed bare `'T1'..'T15','T17'` (`game_state.py:47-52`). And **`T16` is not in that map at all**: the territory roster runs T1–T15 and T17. One authored character lives in a territory the engine does not have.
- **20 distinct faction strings** for four parliamentary factions — `Crown (Inner Circle)`, `Crown (Royal Family)`, `Crown (Ministry)`, `Guilds`, `Löwenritter`, `Altonia`, `Restoration Movement`, `Independent (Southernmost Wardens)`, `Church (dual-loyalty: Crown Inner Circle agent for Himlensendt)`, and more. No mapping to `STARTING_STATS`' four exists anywhere.
- **`ConvictionState` has no weight field.** The registry carries weighted identity convictions (`{conviction: Warden, weight: 0.4}`, 81 weighted primaries across the file). `conviction.py:108-123` stores `scars`, `resonant_active`, `in_crisis`, `pending_belief_revisions`, `last_scar_season`, `log` — **and no baseline weight anywhere in the coded conviction model.** Even with the taxonomy ruled, a weighted profile has nowhere to land.
- **The registry's field set does not fit the `NPC` dataclass** (`npe.py:114-134`), field by field. `first_name`, `role`, `goals`, `arc_trajectory`, `resonant_style`, `birthplace`, `ts`, `coherence`, `stats{cognition,focus,endurance,social}`, `cultural_label`, `self_other_initial`, `title`, `notes` have **no NPC field**. `NPC`'s `stance`, `worldview`, `compromise_category`, `volatility`, `deviation_roll` have **no registry source**. Exactly two fields map directly — `faction` and `territory` — and both are the two that collide.
- **Value types are inconsistent:** `ts` is a string range (`"75–80"`) in 2 entries, an int in 8, null in 36; `stats.social` can be `"3–4"`; 3 entries have no primary convictions.

**The honest restatement:** the content is authored and canonical. It is **not** machine-ready, and the loader is blocked behind five decisions nobody has made. The delta's §6 conclusion — that this is the highest-fan-out build — survives. Its characterization of the work as *"one loader"* does not.

**And a new defect, found while verifying.** `references/npc_registry.yaml:835` and `:850` read:

```yaml
    faction: Hafenmark (Inner Council #4)
    faction: Varfell (Jarl Council #5)
```

YAML treats ` #4)` as an **inline comment**. NPC-081 and NPC-082 therefore parse as `'Hafenmark (Inner Council'` and `'Varfell (Jarl Council'` — truncated, with unbalanced parens. This is the exact class of defect ED-IN-0121 records (`tests/valoria/test_references_yaml_parse.py:1-9`: the file *"was unparseable for the whole of its visible git history and NOTHING NOTICED … It survived because the file has zero Python loaders"*). The file now parses; **it still carries silent parse damage**, and for the same reason: nothing loads it, so nothing checks it.

### §0.2 "Enrich the call site — no new mechanism required" — HALF FALSE.

The delta called the social-contest seam the cheapest large win *because the kernel side was already live*. That is true of three of the five starved inputs and **false of the two I named first**.

`Contest.resistance` is **metadata-only**. `wrapper.py:74-77` says so in its own words — *"NOT plumbed into resolution — the resolver reads no resistance and `Venue.base_ob` is not set from it. Wiring it is the reserved ED stub (contest_rebuild, ED-1055..1079)"* — and I confirmed independently that `resolver.py` contains **zero** `resistance` references. So:

- **passing `world=` today changes nothing about resolution**, and
- **`base_ob` has no producer** — its designed producer *is* the resistance value, reserved to the same ED.

There is also a shape mismatch nobody had noticed: `_derive_resistance` expects a plain dict `{"stabilities": [...]}` (`wrapper.py:46`, an `isinstance(world, dict)` branch), not the `game_state.World` object the call site holds.

**What survives, and it is still substantial:** policy selection, the dossier/evidence path, and the chronicle kwarg are all genuinely live kernel-side. See §2. The corrected claim is *"three of five starved inputs are one argument away; two are blocked on a reserved ED."*

---

## §1 A — THE AUTHORED-PERSON LOADER

### A1 · Registry → world loader

| | |
|---|---|
| **FROM** | `references/npc_registry.yaml` — 46 entries under `characters` |
| **TO** | `world.npcs` (`game_state.py:188`), `world.convictions` (`:197`), `world.beliefs` (`:198`), `world.practitioners` (`:185`), `Settlement.npc_ids` (`registry.py:87`) |
| **INSERTION POINT** | `engine/autoload/game_state.py::create_world`, immediately after the `populate_from_geography` call at `:260-261` |
| **STATUS** | **UNSPECIFIED** |
| **BLOCKED BY** | A2, plus the five design gaps in §0.1 |

**What exists — and it is a great deal.** The model loader is in-tree and documented: `registry.py::populate_from_geography` (`:216-267`), whose docstring (`:216-245`) records the discipline to copy — deterministic, no RNG draw, every field mapping cited to the canon row that authorizes it, illegal values raised rather than silently registered.

**Every receiving store is declared, serialized and restored.** This is the delta's strongest surviving point and it holds up:

| Store | Declared | Serialized | Restored |
|---|---|---|---|
| `world.npcs` | `game_state.py:188` | `:302-305` | `:378-382` (via `NPC.from_dict`) |
| `world.convictions` | `:197` | `:311-312` | `:389-392` |
| `world.beliefs` | `:198` | `:313-315` | `:393-396` |
| `Settlement.npc_ids` | `registry.py:87` | `:128` | `:153` |

And the season consumer is already ticking: `accounting.py:139` calls `simulate_npc_actions(world)` unconditionally every season; the loop body (`npe.py:338-372`) iterates `world.npcs` — an empty dict, every run.

**What is missing:** the loader function, and the five decisions in §0.1.

### A2 · The conviction-taxonomy split

| | |
|---|---|
| **FROM** | the registry's conviction vocabulary — **exactly the canonical 13**, parser-verified: Authority 14, Order 10, Utility 9, Precedent 7, Equity 7, Faith 6, Liberty 6, Warden 5, Honor 5, Community 5, Scholastic 3, Identity 2, Virtue 2 (81 weighted primaries) |
| **TO** | `conviction.py:46-49` — the legacy 9-tuple, and the membership gate at `:191-193` |
| **STATUS** | **DESIGNED-ONLY** (canonical 13 fully specified: `conviction_axis_matrix_v30.md:24-38`, plus 13 authored profiles in `conviction_migration_roster_v30.md`) vs **CODED** legacy 9 in the validator |
| **BLOCKED BY** | nothing — this is a ruling followed by a tuple edit |

**The exact overlap, computed rather than estimated.** Of the registry's 13 conviction names, **6 pass** the coded gate (Faith, Order, Equity, Precedent, Community, Warden) and **7 silently no-op** (Authority, Utility, Liberty, Honor, Scholastic, Identity, Virtue) — covering **41 of the 81** weighted primaries in the file. Conversely, **3 of the coded 9** (Reason, Autonomy, Continuity) appear in **no** registry entry.

So: load the registry today against the live validator and **half the authored conviction data silently evaporates.** `apply_conviction_scar` returns a magnitude-0 record for any unrecognized name (`conviction.py:191-193`) — no exception, no warning.

**The rejection surface is narrower than it looks.** There is exactly **one** production write path — `knots.py:349-353` — and it is itself latent, because knot formation is a stubwired deferral (`mc_v18.py:204-209`). `check_conviction_threshold` and `get_state` have no production callers. `world.convictions` is read by nothing in production except `serialize_world`/`restore_world`.

**Three coded rosters would still disagree after the tuple swap:** `npe.py:80`'s 8 (quoted verbatim from its own canon head, `investigation_systems_v30.md:84`), the deviation-opposites table keyed on those 8 (`npe.py:290-293`), and `knots.py`'s `'Loyalty'` — a member of the 8, and also the NPC affiliation scalar, and in neither the 9 nor the 13.

> **DESIGN GAP 1.** Which taxonomy governs — `npe.py`'s 8, `conviction.py`'s 9, or the canonical 13. **This is a canon ruling, not a code fix**: the delta correctly located the defect in `investigation_systems_v30.md:84`, which asserts its 8 *are* "the existing conviction taxonomy."
>
> **DESIGN GAP 2.** What conviction *weights* live on. No coded class holds a baseline weight.

### A3 · `Settlement.npc_ids` writer / `get_npcs_in_territory` caller

| | |
|---|---|
| **FROM** | a loaded NPC's territory (A1) |
| **TO** | `Settlement.npc_ids` (`registry.py:87`); `npe.py::get_npcs_in_territory` (`:375-377`) |
| **INSERTION POINT** | inside the A1 loader — the only place that will ever hold both keys — using `registry.province_members(territory_id, world)` (`:181-182`) |
| **STATUS** | **CODED-BUT-UNREACHED** on both ends |
| **BLOCKED BY** | A1 |

`Settlement.npc_ids` has **no writer** anywhere in `engine/` or `systems/` (only `from_dict` at `:153`; the sole assigning writer in the tree is a non-production harness fixture). `get_npcs_in_territory` has **zero callers of any kind**.

> **DESIGN GAP 3.** Which settlement within a multi-settlement territory an NPC belongs to. `npc_ids` is per-settlement; the registry's field is per-territory.

---

## §2 B — THE SOCIAL-CONTEST SEAM

**A structural correction the delta missed: there are two live paths, not one.**

1. **`scene_dispatch.py:277-343`** — the Stability-Crisis emergency council, which calls the contest kernel directly.
2. **`parliamentary_bridge.py:180-222`** — the per-season §10 vote, which calls `run_parliamentary_vote` and **never builds a Bout at all.**

Every enrichment below lands only on path (1). Path (2) — the one that runs every single season — does not go through the kernel and cannot be enriched by passing it better arguments.

### B1 · Policies — **live, one argument away**

| | |
|---|---|
| **FROM** | `contest/policy.py` — 11 coded policies (`:56-60`), including `advocate` (`:37-42`), the only one that plays `Move("evidence")` |
| **TO** | `wrapper.py::resolve_contest` (`:229` — defaults `policy_a=policy_b=logos_spammer`) |
| **INSERTION POINT** | `scene_dispatch.py:299`. The call `contest.resolve_contest(built)` takes the defaults — **this line *is* where policies are selected, by omission** |
| **STATUS** | kernel **CODED**; call-site selection **UNSPECIFIED** |
| **BLOCKED BY** | nothing |

> **DESIGN GAP 4.** Which policy each side of a council argues with. Nothing in canon or code derives a policy from faction state.

### B2 · `world=` → audience resistance — **blocked, contra the delta**

| | |
|---|---|
| **FROM** | the `world` in scope at `scene_dispatch.py:298` |
| **TO** | `wrapper.py::build_contest(world=…)` → `_derive_resistance` (`:42-55`) → `Contest.resistance` (`:73-77`) |
| **STATUS** | derivation **CODED**; consumption **DESIGNED-ONLY** |
| **BLOCKED BY** | ED-1055..1079 kernel-side wiring — which precedes any call-site value |

See §0.2. Also note the dict-vs-`World` shape mismatch at `wrapper.py:46`.

### B3 · Dossier / evidence — **kernel live, producer absent**

| | |
|---|---|
| **FROM** | nothing — no world state maps to `EvidenceItem(ground, weight, appeal)` |
| **TO** | `wrapper.py::_as_contestant` (`:90-96`) → `resolver.py`, where the evidence move is genuinely live: `_Side.dossier` built at `:210`, `Move("evidence")` presents the best unpresented relevant item as readiness-free hard proof, capped (`:340-346`) |
| **INSERTION POINT** | `scene_dispatch.py:280-298` — replace the bare ints from `_emergency_council_parties` (`:120-138`) with dict side-specs carrying evidence |
| **STATUS** | kernel **CODED**; producer **UNSPECIFIED** |
| **BLOCKED BY** | B1 — `logos_spammer` never plays `Move("evidence")`, so a dossier without a policy change is dead weight |

> **DESIGN GAP 5.** What evidence *is* at aggregate scale. The only in-tree producer of `EvidenceItem`s is demo content in `agon_harness.py:196-201`, explicitly *"not a canonical constant."* **This is the delta's "a contest has no subject" in mechanical form** — the one narrative finding I could not break.

### B4 · Armature (Style / CLASH-REINFORCE / CR5) — **live in the resolver, unreachable through the wrapper**

| | |
|---|---|
| **TO** | `resolver.py::Bout(…, armature=…)` (`:237`) — genuinely live: CR4 pool bonus + δσ leverage at `:383-387`, CR5 self-backfire at `:404-409`, liveness proven by the wrapper's own invocation self-test (`:387-397`) |
| **STATUS** | kernel **CODED**; wrapper carriage **UNSPECIFIED**; derivation from world state **UNSPECIFIED** |

**Two layers, and the delta only saw one.** The blocker is not primarily the call site — it is that **`build_contest` accepts no armature and `_resolve_agon` builds the Bout without one** (`wrapper.py:197`: `Bout(ca, cb, venue, adj, record=record)`). The `Contest` object has no armature slot. The MECHANICS registry documents the toggle as `Bout(armature=…)` — i.e. *below* the wrapper. `scene_dispatch` goes through the wrapper, so it **cannot reach the toggle at all today.** The in-tree workaround is `agon_harness.py:204-214`, which builds the Contest and then hand-assembles the Bout, labelled "WORKAROUND 3".

> **DESIGN GAP 6.** (a) Whether the wrapper API carries armature (SC lane owns it). (b) Where a judge's `ArmaturePosition` comes from — the natural source is the registry's weighted convictions × the 13×4 axis matrix (`conviction_axis_matrix_v30.md:24-38`, composition rule at `:209-211`), **which makes this partially downstream of A1/A2.**

### B5 · `base_ob` override

Consumer **CODED** (`resolver.py:155`, default 2.0, live at `:288-289`). Producer **DESIGNED-ONLY** — and its designed producer is B2's resistance value. **Not a separate gap; the same reserved ED.** No insertion point exists: `build_contest` has no `base_ob` parameter, so a caller must pass a prebuilt Venue or `dataclasses.replace` the built one (`wrapper.py:172-181` is the in-tree precedent). None of the 8 canonical proceedings sets it.

### B6 · The consequence spine and its terminus

**Where it ends today, read end to end:** `emit_scene_echo` (`echo_transport.py:360-455`) → `compute_domain_echo` → a `scene.contest_resolved` Key plus a deferred `_apply` closure calling `Faction.adjust` (`:430-436`), landing at the accounting boundary (`mc_v18.py:158-161`). **That `Faction.adjust` on L/I is the entire consequence spine of every live contest.**

**Four coded, currently-unfed sinks it could also write to:**

1. **`Settlement.order` via the §5.5 Accord-Echo leg — fully coded and dormant.** `echo_transport.py:134-170` classifies only an explicit caller-declared `echo['scene_outcome']` from a closed vocabulary; `:291-343` builds a real `scene.accord_echo` Key with an OF-7 deferred settlement-Order write. **The missing inputs are exactly two `ctx` fields no live producer sets:** `echo['scene_outcome']` and `echo['target_settlement']`. Insertion point: the same two echo-block constructions at `scene_dispatch.py:342-343` and `parliamentary_bridge.py:207-211`.
   > **DESIGN GAP 7.** Which §5.5 outcome class an emergency council or a vote *is*, and which settlement it occurred in.
2. **The settlement ledger** (D3) — write API coded, zero producers.
3. **`beliefs.social_success` §9.5** (D6) — coded; only caller is the retired legacy stub.
4. **The Chronicle** (E2) — one kwarg away, at the same call site.

---

## §3 C — ARTICULATION / THE RENDER SEAM

### C1 · World reach for the subscriber

| | |
|---|---|
| **FROM** | `mc_v18.py:257-258`, where `world` **is** in scope |
| **TO** | `articulation.py::_on_key(key, scheduler)` (`:140`) |
| **STATUS** | **STUBBED** |
| **BLOCKED BY** | nothing structurally; gated on the ED-IN-0073 Q1–Q4 fork |

**Is there an existing convention for subscribers that need world state?** No — and this is the useful finding. **Articulation is the first and only caller of `TickScheduler.subscribe` in the entire tree.** `echo_transport` is an *emitter*, not a subscriber. `subscribe` has exactly one form: `subscribe(type_id, callback)`, `callback(key, self)` (`keys.py:506-507`, `:576-577`). No richer variant exists.

**The in-tree convention for world reach on the bus is closure capture at the *emit* side** — every `_apply` closure captures `world` and re-resolves entities by id at apply time (`echo_transport.py:325`, `:430-436`). That is the precedent a subscriber-side fix would either follow or deliberately break.

> **DESIGN GAP 8.** None of {closure-captured world, scheduler-held world ref, world in the callback signature} is chosen anywhere — and OI-08's own scope note *forbids* building it there (`articulation.py:30-32`), assigning it to ED-IN-0073.

### C2 · The discarded return

The discard at `keys.py:576-577` is **CODED by contract** (§4.1 step 5, synchronous notify). **The fix is not in `keys.py`.** The substrate already provides the sanctioned in-callback output channel: **`TickScheduler.schedule_emission(key, apply)`** (`:525-536`) — *"a consumer reacting to an observed Key enqueues its new Key"*, drained by `drain_tick`. A chronicle-writing callback would **emit a chronicle Key** rather than return one.

> **DESIGN GAP 9.** Chronicle-entry-as-Key needs a registered key type, and **no chronicle/Tier-3 type exists** in the registry. Minting one is a canon addition.

### C3 · The missing return types

`LensState`, `Trigger`, `ChronicleEntry` are named in the module docstring (`:13-15`) and defined nowhere. **DESIGNED-ONLY**: the shapes exist in prose (`articulation_layer_v30.md` Tier 1 §2, Tier 3 §2.5) with **no field-level schema.**

### C4 · The destination

`World` has 20 registries and **no chronicle field** (`game_state.py:167-212`). `CampaignResult` has 12 fields and **no chronicle slot** (`mc_v18.py:84-105`). The full checklist to add one is set by the OI-07 settlements precedent: declare, serialize, restore, tolerate-missing.

> **DESIGN GAP 10.** Whether the chronicle is a World registry (save/restore-surviving) or CampaignResult-only telemetry — **and whether the KeyLog, already in `final_state` via `key_log_hash`/`keys_emitted`, is the chronicle's source of truth, making a separate store redundant.**

### C5 · `scene.contest_resolved` missing from the trigger roster — **OMISSION, not a canon decision**

This is the map's cleanest actionable finding, and it is settled on the corpus's own evidence:

> ⚠ **CORRECTED 2026-08-22, same day, by the reconciliation pass — and the correction strengthens the finding.** This section first read *"`scene.contest_resolved` is the only Key type a default campaign emits."* **False.** `faction_action.py::_emit_battle_concluded` (`:342`) builds a real `scene.battle_concluded` Key and is called **unconditionally** at `:480` after every resolved war action. Its own docstring names it *"THE FIRST KEY EMISSION OUTSIDE `echo_transport` (ED-IN-0122)"*, landed precisely because *"a substrate with one call site is a prototype, not an architecture."* I inherited the single-emitter claim from a measurement that predates that commit.
>
> **Why this makes C5 bigger, not smaller:** `scene.battle_concluded` is **also absent** from `_TRIGGER_TYPE_IDS` (verified — the tuple has 13 entries and does not contain it), while `references/key_graph.json` declares **four** consumers for it, `articulation_layer` among them (`faction_action.py:474-476`). So the registry-vs-trigger-roster inconsistency is **two omitted rows, not one**, and the second one's emitter fires on every battle. The delta's §2.2 conclusion — that **zero** articulation callbacks fire in a default campaign — is unaffected and still holds.

- `scene.contest_resolved` is emitted every season — `echo_transport.py:97-100` maps `"contest"` → it, and `parliamentary_bridge.py:212` emits one **every season**.
- It is absent from `_TRIGGER_TYPE_IDS` (`articulation.py:116-130`) **and** from the canon trigger table (`articulation_layer_v30.md` §3.1, rows 1–13).
- **But the key-type registry already declares articulation a `consuming_systems` member of it** (`key_type_registry_v30.md:854`).
- And the trigger table's own history note describes *exactly this class of gap* — *"declares articulation a consuming_systems member … but this ruleset never listed either type"* — as **the defect that rows #11/#12 (ED-IN-0004) and row #13 (OI-03) were added to close.**

`scene.contest_resolved` is the remaining instance of that same class, with the strongest emitter of all. Insertion point: a §3.1 row #14 plus one tuple entry at `articulation.py:130`, following the two-surface-in-one-change discipline rows 11–13 used.

**Payoff is bounded:** the callback it would reach is still the C1–C4 stub. This closes a *registry inconsistency*, not the render gap.

**A second correction to §0.1, from the same pass.** I wrote that the registry holds *"46 fully-structured characters"* and enumerated the fields *"every entry carries."* **That is false as a population claim** — those are the schema's **optional** fields, and I never counted them. Measured across all 46:

| Field | Populated | | Field | Populated |
|---|---|---|---|---|
| `id` / `first_name` / `faction` / `role` / `status` / `source` / `convictions` | **46** | | `notes` | 15 |
| `last_name` | 44 | | `ts` | 10 |
| `cultural_label` | 43 | | `territory` | **7** |
| `arc_trajectory` | 36 | | `title` | 7 |
| `self_other_initial` | 28 | | `birthplace` | 5 |
| `resonant_style` | 18 | | `stats` | **1** |
| `goals` | 17 (39 sentences) | | `coherence` | **1** |
| `certainty` | 8 | | `age` | **0** |

**One entry has a stats block. One has a coherence value.** The honest characterization is **46 *identified* characters, all carrying a conviction profile, of which roughly a third are deeply authored** — not 46 fully-structured ones.

**And a schema defect a loader will hit immediately:** `cultural_label`, `self_other_initial` and `migration_notes` appear at **two different nesting levels** across entries — top-level for some, nested under `convictions` for others (`cultural_label`: 17 top-level, 26 nested; `self_other_initial`: 2 top-level, 26 nested). A loader reading either level alone silently misses most of the data. This is not in the sixteen gaps; it is a data-hygiene fix.

---

## §4 D — ORPHANED MECHANISMS NEEDING A CALLER

### D1 · Threadwork — **CODED-BUT-UNREACHED; caller UNSPECIFIED**

A queued `"threadwork"` scene today falls into the OI-02 total-mapping fallback and stub-resolves (`scene_dispatch.py:360-371`; the full elif chain is combat `:224` / contest `:277` / fieldwork+investigation `:344` / else stub `:360`).

**Three insertion points, not one:** an `elif st == "threadwork":` branch between `:343` and `:344`; a trigger in `evaluate_triggers` (`:75-99`, where **only Stability Crisis is evaluable**, `:96`); and the handoff-pair map (`:157-160`) if its outcome hands up.

**What the entry point requires:** `operations.py:26-33` exposes 7 `attempt_*(actor, target, world)` with full TN/Ob tables (`:45-117`), duck-typing an actor with `.spirit`, `.focus`, `.ts` and optionally `.history` — its docstring is explicit that *"World has no practitioner stat schema yet … caller supplies a Practitioner-like object"* (`:15-19`). `world.practitioners` holds only `CoherenceState` per actor, not stats. **The registry carries `ts`, `coherence` and `stats.focus` — but no `spirit`.**

> **DESIGN GAP 11.** A threadwork trigger evaluable on the aggregate World, and a practitioner-actor derivation. `spirit` has no source anywhere.

### D2 · `combat_engine_v1` — **two blockers, one of them a scheduled decision**

The bridge is read end to end and is real: `derive_parties(ctx, world)` requires `ctx['factions'] = (fid_a, fid_b)` (`combat_bridge.py:114-128`); each side becomes a `Combatant` whose **only** derived field is `history = max(1, round(Faction.Mil))` (`:103-111`) — the one Lifepath output that is coded; resolution calls `wrapper.fight` as-is with a world-stream rng (`:131-141`). **The echo half is already coded** at `scene_dispatch.py:240-267`.

**What would have to be true for a combat scene to be queued:**
1. **A trigger** producing `scene_type="combat"` with `ctx['factions']`. The other 7 §4.3.2 triggers are deferred precisely because their conditions are not evaluable on the aggregate World (`scene_dispatch.py:58-60`, `:96-99`), so a new evaluable condition must be ruled.
2. **The flag flipped ON.** `DISPATCH_COMBAT_BRIDGE` defaults OFF (`mc_v18.py:70-81`), and the flip's named precondition is the cross-faction attribution model — `scene_dispatch.py:246-259`: *"who is credited/debited on a win … are all open design questions."*

> **DESIGN GAP 12.** The combat trigger condition, and the echo attribution model.

### D3 · The settlement ledger — **write API coded, zero production writers, no event→tag semantics**

**Verified zero production writers:** every `add_tag` caller in the tree is under the non-production `tools/sim_harness/adapters/pr119_governance/` prototype cluster; `ledger_sweep`'s only production caller is `succeed_governor` (`registry.py:207`), itself uncalled.

**Four season-loop events exist in code that could hang a tag on:** parliamentary territory transfer (live every season via the OI-04 bridge, `parliamentary_bridge.py:165-177`, whose ownership write already emits a `da.public_governance` Key at `parliamentary_transfer.py:116-169`); conquest ownership changes via `faction_action`; the emergency-council verdict; and the dormant §5.5 accord-echo settlement write.

**One hazard worth flagging:** `ledger_add` does **not** validate `kind` against `TAG_KINDS` (`:30` defines the five; `:47-58` never checks). The pr119 harness already writes an unratified `"Compact"` kind through it unchecked.

> **DESIGN GAP 13.** No canon or code maps any strategic event to a tag (kind, key, ttl). The only in-tree specification of event→tag semantics is the non-production harness and the PROPOSED card deck — which itself invokes three **unratified** tag families (Outlawed / Capital-Posture / Compact, not in `TAG_KINDS`).

### D4 · `succeed_governor` — **CODED-BUT-UNREACHED, and circularly blocked**

No succession or appointment event exists in the season loop; nothing writes `Settlement.governor_id` outside `succeed_governor` itself and `from_dict`.

> **DESIGN GAP 14.** Who appoints or loses a governor, when, and what a governor id denotes. **No NPC exists to hold the office** — circularly dependent on A1. The harness uses bare strings like `"podesta-appointee"`.

### D5 · `mass_seizure` — ⚠ **CORRECTED 2026-08-22: it is NOT purely a call site**

> **This section first read "the only D-item with no design gap" and "the missing artifact is purely the call." A full read of the module broke that, and I verified it.** `mass_seizure.py:293` writes `t.accord = float(starting_accord)` — a **canonical index** (0–4) written raw into `Territory.accord`, which is a **continuous** field on the `ACCORD_MAP` scale `{0:1.0, 1:2.5, 2:4.0, 3:5.5, 4:7.0}` (`game_state.py:61`). The sibling transfer site does it correctly: `parliamentary_transfer.py:278` is `terr.accord = ACCORD_MAP[accord_level]`.
>
> A seizure intended at Accord 2 therefore stores **2.0** where canon means **4.0**, and reads back through `canonical_accord` as a lower bucket. `game_state.py:65-70` warns about exactly this class in its own words — modules looking up canon-keyed tables *"MUST bucket through these helpers"* — and the site's own comment half-admits it: *"Convert int accord to ACCORD_MAP-style continuous if needed; for now, set directly."*
>
> **So wiring D5 as-is ships a wrong-scale write into the live world.** The fix is the call **plus** the `ACCORD_MAP` conversion. It is still the shortest path in the map; it is no longer a free one. `mass_seizure` also has **zero test coverage of any kind**, unlike the six stubs in the same package, which are pinned by `test_pipeline_reach.py:750-755`.

### D5 (continued) — the canon-specified trigger

Recorded as measured at `parliamentary_transfer.py:127-135`: *"UNREACHABLE. Zero production callers … no owner write in 40 seeded campaigns. Its gate is not the obstacle — CI ≥ 60 is met in 20/20 seeds and CI = 100 … reached in 8/20."*

**Unlike D1/D2, the trigger IS specified by canon** — a per-season probabilistic declaration check once CI ≥ 60, forced at CI = 100. The missing artifact is **purely the call**: a Church-scoped check in the season path. One recorded `[ASSUMPTION]` to honor at wiring time: the Influence-stat mapping (`mass_seizure.py:26-33`).

**This is the shortest complete path in the entire map.**

### D6 · `add_belief` / `revise_belief` / `beliefs.social_success`

All three **CODED**, world-routed and serialized. All three unreached, and **(i)'s previous wire was severed by the kernel promotion**: `social_success`'s only caller is the retired legacy stub (`contest_legacy_stub.py:240-242`), which `scene_dispatch` explicitly stopped calling (`:285-287`).

**The blocking problem is that a live contest has no actor.** `social_success` needs an `actor_id` and a `belief_id`; the live contest's "sides" are faculty integers for **one faction's two facets**. There is nobody to hold a belief.

> **DESIGN GAP 15.** The registry carries `goals` (authored sentences), not Beliefs. No mapping from goals to `Belief(statement, position, underlying_convictions)` exists anywhere.

---

## §5 E — PROSE RENDERERS WITH NO CAMPAIGN REACH

### E1 · The combat workbench pipeline

**What it eats:** a traced-fight event stream — `fight_start`, `turn_start`, `engagement_start`, `approach`, `stophit`, `commit`, `read`, `mode`, `roll`, `outcome`, `engagement_end`, `fight_result` (`narrate.py:38-99`), produced by the engine's own trace seam: `wrapper._TRACE`, set by `workbench/trace.py::run_traced_fight` (`:14-26`, which wraps `wrapper.fight` and restores `_TRACE` after).

**Is that stream produced in the campaign loop?** No. The campaign's only combat path calls `wrapper.fight` directly with `_TRACE` unset (`combat_bridge.py:139-141`) — and that path never runs anyway (D2).

**The adapter already exists.** `run_traced_fight` *is* the adapter: `(Combatant, Combatant, seed) → (result, events)`. `combat_bridge.resolve` already holds both Combatants and a derived seed (`:140`). **The gap is one call-shape substitution inside `combat_bridge.resolve`, plus somewhere to put `events`** — and its return dict is shape-pinned by `engine/tests/test_combat_bridge_seam.py` as additive-field-only.

**BLOCKED BY:** D2 (no combat scene to trace) and C4 (no destination for narration).

### E2 · The contest Chronicle — **one kwarg from producing, blocked only on a destination**

**What it eats:** `narrative.summarize(log, winner, why)` → `Chronicle.render()`. `log` is the Bout's opt-in beat trace — `resolver.py:245` (`self.log = [] if record else None`), rows `dict(i, side, kind, appeal, ground, gain, advA, advB)` at `:426-434`.

**Confirmed contest-specific by construction**, as the antagonist said: it binds `contract.A/B` and the bout beat shape, and **cannot render the parliamentary vote path**, which never builds a Bout.

**The live kernel call is one kwarg away.** `resolve_contest` exposes `record=` (`wrapper.py:229`) and returns the bout (`:198`) — **unpacked and discarded as `_bout` at `scene_dispatch.py:299`.** The chain `record=True` → `summarize(_bout.log, verdict, verdict_reason)` → `Chronicle` is **entirely coded**.

**What has no coded answer is the destination** (C2/C4): a rendered string with nowhere to go.

**This is the single cheapest step toward player-visible narrative in the tree** — and it terminates in the one gap ED-IN-0073 owns.

### E3 · `agon_harness`

Not an integration target. Its value to this map is as **the existence proof and reference implementation** for B3/B4/E2's call shapes: `setup_contest` (`:190-215`) is the canonical fully-enriched kernel call — `build_contest` with a dossier'd Contestant, then a hand-built `Bout(record=True, armature=ArmatureConfig(..., cr5=True))` — exercising **every seam the campaign starves**, via the documented workarounds for the wrapper gaps. It also consumes the authored flavor copy (`PROCEEDINGS_TABLE[proceeding].flavor`).

---

## §6 F — DESIGNED-ONLY CONTENT

### F1 · The 58 event cards

**What would consume a card** is answered by the deck's own §C.1/C.4: a Π-weighted event-table draw engine, self-tagged *"[NEW ENGINE — surface for canon ratification]"*, unbuilt. Card *resolution* then routes to three already-ratified resolvers (d+σ domain actions, deterministic settlement accounting, social-contest dice pool). A non-production prototype of the whole loop exists at `tools/sim_harness/adapters/pr119_governance/pr119_event_deck_engine.py`.

**Do the trigger predicates reference world state that exists?** **Mostly no.** Sampled triggers reference: a wealthy patron NPC with high Weight/Treasury (**no NPCs exist; no Treasury field exists**), NPC `ambition.progress` / `expected_tenure` / `power_base` (**no ambition schema anywhere**), `marriage_contract_banked` / `patronage_installation` Keys (**unregistered**), Capital-Posture ledger tags (**unratified family**), `settlement.PS contestable` (`popular_support` exists but is declared **INERT**, `registry.py:69-75`). What *does* exist: `Settlement.prosperity`, Π ≈ `Settlement.pressure`, and adjacency conditions partially.

The deck's own §C.3 honestly surfaces most of these as findings-to-ratify.

### F2 · ED-SE-0008's Dearth/granary chain — **the best-specified unbuilt chain in the map**

Beyond the `granary: int (0-3)` field it names as an explicit follow-on code task, it needs: a Dearth trigger evaluator (trigger (i) Prosperity 0 is evaluable today; (ii) "grain route cut" needs a route mechanism with no code; (iii) fiscal stance needs the FA-1 verb system with no code); **a governor response-verb selection point — no governance-action phase exists in the loop, and no governor exists to select** (D4); PS ±1/±2 writes landing on the **INERT** `popular_support`; the riot and black-market checks; and ratification.

**Jordan's own worked example** — drought → crop failure → food/taxation → Church donations buying favour → infrastructure — maps onto this chain almost exactly. It is the closest thing in the tree to that scenario, and it is blocked on a governance phase that does not exist.

### F3 · The relational-edge graph

Confirmed **DESIGNED-ONLY with a self-contradictory status marking**: §7/§8 carry *"BUILT 2026-06-09, ED-1000"* headers (`:498`, `:519`) while §12 (`:653-657`) lists the same items as *"full mechanics deferred (§7/§8 hook only)"*. **No `canon/relational_edges_v30.yaml` and no relational-edge `.py` exists anywhere.** Do not trust the BUILT marker.

**BLOCKED BY:** A1 (a graph with no nodes) plus the unauthored edges YAML, which the doc itself defers as a Class-D content task.

### F4 · `systems/world/` lore — **my claim was too broad**

The delta said *"every `systems/world/` lore doc has zero code citations."* **True of the lore subset, false of the directory.** The lore proper (`solmund_*`, `worldbuilding_*`, `narrative_voice_canon_v30.md`, `southernmost_v30*`, `calamity_radiation_v30*`, geography prose) has no implementing `.py` — the only code hits are the names-registry apparatus, which the vector-audit skill itself classifies "not a mechanic." But `insurgency_pipeline_v30.md` has a real partial sim, and `miraculous_event_v30.md` has a stubwire no-op.

> **DESIGN GAP 16.** No mechanism anywhere consumes the lore corpus. The nearest declared hooks are `miraculous_event`'s stub, the cards' flavor grounding, and articulation's unbuilt chronicle voice — `narrative_voice_canon` would presumably govern C3's render, but **nothing says so in code or contract.**

---

## §7 THE DEPENDENCY GRAPH

Derived only from what was read.

```
A2 (taxonomy ruling) ──────────────┐
                                   ├──► A1 (loader) ──► A3 (npc_ids / get_npcs_in_territory)
ConvictionState weight-field gap ──┘         │
                                             ├──► D1 (threadwork actors — ts/focus exist, spirit does not)
                                             ├──► D4 (a governor who is a person) ──► F2 (Dearth response verbs)
                                             ├──► D6 (actors to hold beliefs; goals→Belief gap)
                                             ├──► B4-derivation (judge positions from weights × 13×4 matrix)
                                             └──► F3 (nodes for the edge graph) ──► F1 (NPC-referencing triggers)

ED-1055..1079 (resistance plumbing) ──► B2 ──► B5
B1 (policy selection) ──► B3 (dossier: only `advocate` plays evidence)
B4-wrapper-gap (armature carriage) — independent; precedes any armature use from scene_dispatch

C1 (world reach) ──► C2 (sink) ──► C4 (destination) ◄── C3 (types)      [all gated on ED-IN-0073]
C5 (trigger row #14) — independent; payoff bounded by C1-C4
E2 (chronicle: record=True + summarize) ──► needs C4 for a destination
D2 (combat trigger + flag flip, gated on the attribution ruling) ──► E1
D3 (ledger writes) — three events unblocked; the accord-echo event blocked by B6-sink-1
D5 (mass_seizure caller) — blocked by nothing
F2 — blocked by the governance-verb phase (shares D4's gap) + LPS-1 + ratification
```

**Two roots with no in-map blocker at all: A2's taxonomy ruling, and D5's call site.** The deepest chain is A2 → A1 → F3 → F1.

**What the graph says that the delta did not.** The person layer is not one build among several — **it is the root of five separate chains** (threadwork actors, governors, belief-holders, judge armature positions, and graph nodes). Nothing else in the map has that position. That is a stronger argument for the delta's §6 recommendation than the "one loader" claim it actually made, and it survives the correction that killed that claim.

---

## §8 THE SIXTEEN DESIGN GAPS

Each stated as the unmade decision, because that is the form in which Jordan can rule on it.

| # | The unmade decision | Owner |
|---|---|---|
| 1 | **Which conviction taxonomy governs** — `npe.py`'s 8 (canon-quoted), `conviction.py`'s 9 (self-superseded), or the canonical 13 | canon ruling |
| 2 | **What conviction weights live on** — no coded class holds a baseline weight | PC/FI |
| 3 | **What an authored person deserializes into** — `npe.NPC` (poor fit), a new dataclass, or NPC + `persistent_state` payload | WR/FI |
| 4 | **Territory/faction key normalization** — `"T15 (Southernmost)"` → `'T15'`; where 39 territory-less people go; what `T16` is; how 20 faction strings map to 4 | WR |
| 5 | **Settlement membership of an NPC** — `npc_ids` is per-settlement, the registry field is per-territory | SE |
| 6 | **Policy selection rule** for contest sides | SC |
| 7 | **What evidence IS at aggregate scale** | SC/FI |
| 8 | **Wrapper carriage of the armature**, and derivation of judge positions from world state | SC |
| 9 | **§5.5 classification of live scenes** — which `scene_outcome`, which `target_settlement` | IN |
| 10 | **How a bus subscriber reaches world**; and **what the chronicle sink is** — Key-emission (needs a new registered type), World field, or CampaignResult telemetry | ED-IN-0073 |
| 11 | **Field-level schema** of `LensState` / `Trigger` / `ChronicleEntry` | ED-IN-0073 |
| 12 | **A combat trigger condition** evaluable on the aggregate World, and **the echo attribution model** | PC/IN |
| 13 | **The event→tag mapping** for the ledger, plus ratification of three PROPOSED tag families | SE |
| 14 | **Governor succession/appointment** — who, when, what the id denotes | SE/FA |
| 15 | **goals → Belief mapping** for authored persons | FI |
| 16 | **Any mechanical consumer of the lore corpus** | WR |

**Two non-gaps, for contrast — and they are the two places to start:**

- **D5 (`mass_seizure`) has no design gap.** Canon specifies its trigger; only the call is missing.
- **C5 is an omission, not a decision.** The registry already declares articulation a consumer of `scene.contest_resolved`.

---

## §9 WHAT I RE-VERIFIED MYSELF, AND WHAT I DID NOT

Per CLAUDE.md §0.1 point 3 — a result claim carries the check that would have shown it wrong.

**Re-verified by parsing or reading, personally, after the map was delivered:**

| Claim | How |
|---|---|
| 46 characters; 7 with territory; the `"T<N> (<name>)"` format; `T16` absent from `STARTING_OWNER` | parsed the YAML; read `game_state.py:44-54` |
| 20 distinct faction strings, with the distribution | parsed |
| Conviction vocabulary is exactly the canonical 13; 81 weighted primaries; 3 entries with none | parsed |
| **The `#4)` / `#5)` inline-comment truncation on NPC-081/082** | parsed for unbalanced parens, then read `references/npc_registry.yaml:835,850` |
| `ConvictionState` has no weight field | read `conviction.py:105-128` |
| `resolver.py` has zero `resistance` references; `wrapper.py:74-77` says metadata-only | read both |

**Not independently re-verified — carried at the map's confidence:** the B-path resolver internals (`:340-346`, `:383-409`), the D3 ledger writer census, D5's 40-seed measurement (it is quoted from an in-tree comment, not re-run), F1's trigger sampling, and E1's `test_combat_bridge_seam` shape pin.

**Declared unread by the map, and still unread:** `systems/factions/sim/faction_action.py`; `systems/overview/sim/season.py`; `systems/social_contest/sim/parliamentary_vote.py` (so the §10 Mandate penalty rests on a docstring, not a read); `contest/primitives.py`, `dictionaries.py`, `rhetoric.py`, `armature.py`; `systems/fieldwork/sim/knots.py` in full; `systems/settlements/sim/temperaments.py`; `engine/cross_scale/domain_echo.py`, `zoom_in_out.py`, `handoff_rules.py`; `engine/autoload/scene_slate.py`, `victory.py`; the combat engine core. **Whether anything emits `state.succession` was not verified** — relevant to D4.

**The claim in this document most likely to be wrong** is E2's — that the chronicle is "one kwarg away." Every link in that chain was read, but the chain has four links and I re-verified none of them personally. If it is wrong, it is wrong in the same direction the delta's §2.2 was wrong: a seam that looks one step from live because the pieces exist, while nothing has ever passed a value end to end. **The check that would settle it is a single run with `record=True` and a print — which is code execution, deferred by this session's design-only scope.**
