# The Delta — what is designed, what is built, and why the world is empty

## Status: FINDINGS. Content/design only — another session owns the restructure; no tooling, no moves, no registry edits. Compliance bookkeeping light per Jordan 2026-08-19; reconciliation pending.

**Date:** 2026-08-19 · **Revised 2026-08-22 after the full antagonist pass.**
**Method:** agonist→antagonist. Eight producers (code as basis, design as comparator), one **Fable 5 authoritative full-read pass barred from grep/regex/pattern-matching** per Jordan's direction, then **five independent read-only antagonists**, also barred from pattern-matching.

**The antagonist pass changed this document materially.** It overturned the headline tractability claim, corrected five numbers, and found that several findings were already filed elsewhere in the corpus. Everything overturned is recorded in **§8**, not quietly deleted. Every correction below was re-verified by hand against the working tree before it was written here.

---

## §1 THE ONE-LINE FINDING

> **In every seeded campaign, the population of Valoria is zero.**

`generate_npc` is correct, tested, and has **no world-gen or season-tick call site**. `world.npcs` is empty every run; the seasonal stance-drift loop iterates an empty dict.

**⚠ Framing correction (antagonist, upheld).** This is **not an oversight** — it is a ruled, permanent honest deferral, and the corpus has *already retracted* the framing I first gave it. `engine/tests/test_pipeline_reach.py:137-145` records the reclassification verbatim: the item *"was 'generate_npc has zero call sites', framed as an oversight"* and is now *"a PERMANENT deferral until canon specifies a trigger, not a to-do for a later wave"* (OI-05), carried as a `@pytest.mark.xfail(strict=True)` manifest row at `:596-599`. The canon basis is real: `investigation_systems_v30.md:102` specifies *scene-specification-driven* generation ("Scene specification declares density and composition") and no live scene spec generates anyone.

So the finding is not *"someone forgot to call it."* It is: **the trigger canon specifies does not exist in the live loop, and nothing else fills the gap.** That is a content gap, which is what this session is for.

And the shape of the loss, in one comparison:

> **The settlement record has a slot for people (`Settlement.npc_ids`, `registry.py:87`). The person record has a slot for nothing and no one.**

---

## §2 THREE FAILURE MODES, NOT ONE — and they need different fixes

### §2.1 ORPHANED MECHANISM — built, correct, no caller

| Mechanism | Status |
|---|---|
| **threadwork, entire** | 7 operation types, a 6-branch opposing-outcome table matching its design cell-for-cell, a 15-card Co-Movement deck, a working Coherence track. `mc_v18` never imports it; no `scene_type` branch exists |
| **settlement ledger** | Precedent / Grudge / Debt / Reputation / Leverage — complete write API, dedupe, TTL, succession-survival. **Only production caller is `ledger_sweep`** |
| **`combat_engine_v1`** | 6,155 lines, 53 weapons, a real acquisition layer. **No path by which a game turn calls it** — `scene_dispatch.py:37-38` states no `queue_scene("combat", ...)` call site exists |
| **`references/npc_registry.yaml`** | **46 fully-authored characters** — see §6. Zero loaders (ED-IN-0121) |
| `generate_npc` · `succeed_governor` · `mass_seizure` · `treaty` expiry · `add_belief` · `revise_belief` · `Settlement.ap` | all built, all uncalled |

**Fix: add a caller.**

### §2.2 HOLLOW SEAM — ⚠ CORRECTED. The caller does *not* fire, and the body is four gaps, not one

**This section was wrong in my first draft, in both directions. The antagonist overturned it and I verified every structural fact by reading.**

`engine/mc_v18.py:257-258` does call `articulation.subscribe_all(world.echo_scheduler)`, registering 13 trigger types. What I got wrong:

**(a) It is flag-gated, not unconditional.** The call sits *inside* `if _echo_transport_on(effective_params):` (`mc_v18.py:241`). Default-ON, but a flag.

**(b) Zero callbacks fire in a default campaign.** I checked `_TRIGGER_TYPE_IDS` (`articulation.py:116-130`) against what the live loop actually emits:

- `scene.contest_resolved` — the *only* type a default campaign emits — **is not in the trigger list.**
- `scene.combat_resolved` / `scene.combat_felled` need `DISPATCH_COMBAT_BRIDGE`, **default OFF** (`mc_v18.py:81`), *and* a queued combat scene that nothing queues.
- `scene.accord_echo` is *"organically DORMANT … fires zero times in any seeded campaign"* (`echo_transport.py:246-247`).

The repo's own oracle says so: the reach test is `xfail` *"while DISPATCH_COMBAT_BRIDGE is OFF (today's default)"* and hand-builds the `SceneSlot` to test at all (`test_pipeline_reach.py:703-706, 725-726`).

**(c) The stub could not render even if it fired — four independent blockers, all verified:**

1. **No world reach.** The callback is `def _on_key(key, scheduler)` (`articulation.py:140`), and `subscribe_all(scheduler)` (`:152`) receives `world.echo_scheduler`, never `world`. Its own docstring makes it a contract: *"The closure captures only `type_id` (a str) — no Key/world state is retained."*
2. **No sink.** `engine/substrate/keys.py:576-577` is `for callback in …: callback(key, self)` — **the return value is discarded.** A perfect chronicle entry would be thrown away.
3. **No return types.** `LensState`, `Trigger`, `ChronicleEntry` exist only in the docstring (`:13-15`) and `io_contract` strings. `articulation.py` defines no class.
4. **No destination.** `World` has no chronicle field; `CampaignResult` has no slot.

**Corrected fix: articulation is a subscriber shell with no emitters, no world reach, no result sink, and no result types.** That is a seam to *design*, not a body to fill.

Also corrected: the "do not build it here" phrase appears **twice** (`articulation.py:32`, `:68`), not six times, and `:51` carries a different reason (OI-08) — my "repeated six times" overstated the deliberateness.

`fieldwork.py` and `investigation.py` remain as reported: 112 lines of pure no-op, with `run_fieldwork_scene` and `resolve_npe_response` **literally interchangeable** because neither has activity-specific logic.

### §2.3 STARVED SEAM — caller and body both real, fed degenerate input

**This section survived the antagonist pass unchanged.** Social contest is not orphaned. It runs live. And:

- **every live contest is `logos_spammer` vs `logos_spammer`** — the same trivial policy on both sides
- the caller never passes `world=`, so audience resistance is derived and then always `None`
- no `Dossier` is ever populated — evidence never enters
- no armature is passed, so **Style, the CLASH/REINFORCE algebra, and the CR5 backfire — all working code — are unreachable**
- `base_ob = 2.0`, fixed, never overridden by any of the 8 proceedings
- the consequence spine is **a ±1/±2 Mandate delta on one faction**

**Fix: enrich the call site — no new mechanism required.** With §2.2 downgraded, **this is now unambiguously the cheapest large win in the tree.**

---

## §3 WHAT AN ENTITY CAN BE, IN CODE

| | Settlement | Faction | NPC |
|---|---|---|---|
| Fields | 25 | 16 | 12 |
| Named? | **yes, authored** | yes | **no** |
| Instantiated every campaign? | **yes** — `populate_from_geography` at `create_world` | yes | **never** |
| Populated at boot | **8 of 25** (corrected) | stats + 7 booleans (4 spent-action flags) | n/a |
| Read after boot? | **yes, every season** (corrected) | yes | loop runs over an empty dict |
| Memory | ledger (5 kinds) — **never written** | none | `persistent_state` — **never written** |
| Relations | province, adjacency, `npc_ids` | territory ownership only | **none** |

**Two corrections to this table, both verified by loading the file rather than reading a docstring:**

- **`owner_faction` is populated for 37 of 37 settlements, not one.** I read the geography YAML with a parser: every entry carries `controller` — Crown 15, Hafenmark 10, Varfell 10, Church 1, Schoenland 1. My producer had misread `registry.py:233-236`, whose "one entry, S-037/Schoenland" scopes the *non-parliamentary controller value*, not the presence of the key. Boot-populated fields are `sid, name, stype, province_id, owner_faction, prosperity, defense, order` = **8 of 25**.
- **The registry is not boot-only.** `systems/overview/sim/accounting.py:143` calls `_probe_province_accord_drift` unconditionally every season, which calls `province_members` / `province_accord` per province (`:86-88`). This *sharpens* the contract finding rather than softening it: `references/module_contracts.yaml:693` points `sim_module:` at `settlement.py`, which has **no importer**, while `registry.py` — the file with a live per-season reader — has no `sim_module:` row at all (a disclosed split, `module_contracts.yaml:696-699`, not an absence).

**Factions:** personality is a string comparison. `if faction.name == 'Crown'` … `elif == 'Church'`. **Hafenmark and Varfell have no branch at all** — swap their names in the starting-stats table and the simulation is unchanged. `parliamentary_action.py:68-69`: *"No grudge / hostility / inter-faction-relationship stat exists in game_state.Faction."*

**No PC record exists.** `form_knot` duck-types `.bonds`, `.spirit`, `.history_relationships`, `.ts` — **no class in the tree defines them.** A PC is a bare `actor_id` string used as a key across five registries, of which `world.npcs` is territory-keyed rather than actor-keyed (`game_state.py:188`), so even the shared-key framing is only true of four.

⚠ **Scope correction:** "no actor class" is true of **PCs**. It is false of actors generally — `NPC` (`npe.py:115`) and `Combatant` (`combatant.py:92`) are real actor classes with per-instance state and `to_dict`/`from_dict` round-trips, and `generate_npc` differentiates each instance across nine fields. The defensible claim is the narrower one.

---

## §4 DEFECTS FOUND BY READING

### §4.1 Confirmed, unchanged

1. **The hidden-allegiance deviation is a dead write.** `npe.py:296-299` assigns a *local*; the constructor at `:308-319` never passes it. **Sharpened by the antagonist:** this is not one dead field — it silently voids **1 of 5 branches** of the Tier-2 deviation mechanic (`npe.py:283`, `rng.randint(0, 4)`), so ~20% of deviation rolls produce no state change, against canon's *"one axis is rolled against the opposite extreme"* (`investigation_systems_v30.md:104`). The field is canon-required: `investigation_systems_v30.md:86`.
2. **`npe.py:261` comments "weighted by faction"; the code is an unweighted `rng.choice`.**
3. **`apply_knot_loss` drops two of four consequences** — `composure_damage` and `disposition_set_to` are written into a local dict no caller applies.
4. **`persistent_state` is never written.** Default at `npe.py:134`, serialized at `:147`/`:163`, no assignment site. Canon wanted it for *"Remember interactions with the player (Disposition changes carry forward)"* (`investigation_systems_v30.md:109`).

### §4.2 The Conviction cluster — REFRAMED. My version was arithmetically wrong and diagnostically backwards.

I claimed `conviction.py`'s 9-tuple was "a garbled set" with 4 members in no taxonomy. **I read the two files side by side. That is false — the correct number is zero.** `conviction.py:44-49` is the `conviction_track_v1.md:20-28` §1 table **verbatim, in table order**: Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity, Community, Warden.

The real defect is worse and different: **it is a documented-supersession violation.** `conviction_track_v1.md:2` says *"New readers: do not use §1 of this file for Conviction definitions."* `conviction.py:46` uses exactly that — while its own comment at `:40-43` declares the set superseded. The comment is wrong twice: it also cites *"the canonical names used in §3 Thread Operation matrix"*, and that matrix has **seven** columns, omitting Community and Warden.

**The `'Loyalty'` no-op is real but is a cross-roster collision, not a typo.** `knots.py:349-353` scars `'Loyalty'`; `conviction.py:191-193` returns magnitude-0 for any unknown name. `'Loyalty'` **is** a first-class member of a third roster — `npe.py:80` — and that roster is quoted **verbatim from its own canon head**: `investigation_systems_v30.md:84` asserts that *"Faith, Order, Reason, Justice, Survival, Loyalty, Truth, Power"* **is** "the existing conviction taxonomy." **The defect lives in canon, not in `npe.py`.** A code-only fix would leave the false canon standing.

Scope, corrected upward: against the canonical 13, **six** of `npe.py`'s eight are absent — Reason, Justice, Survival, Loyalty, Truth, Power — not three. Two are live term collisions: **Loyalty** is also a 0–3 affiliation scalar in the same file (`npe.py:125`), and **Truth** is also the renamed 0–5 personal axis (`conviction.py:61-63`, ED-IN-0075).

### §4.3 New defects, found only by the antagonists

5. **A green test masks the `'Loyalty'` bug.** `engine/tests/test_knots_ed912.py:103-116` asserts `c["conviction_scar"] == 1` — but `knots.py:346` sets that flag **unconditionally, before and independently of** the `apply_conviction_scar` call at `:349-353`. The test asserts the *intent flag*, never the *effect*; it never calls `conviction.get_state`. **This is CLAUDE.md §0.1 point 2 exactly** — an assertion that cannot observe the failure it excludes — sitting in the blocking `sim-regression` job. The bug is not untested; it is *masked by the test written to pin it*. Also: `apply_knot_loss` returns a dict that lies (`conviction_scar: 1` when none was applied), the `try/except` at `:354-355` cannot catch it because the no-op is a `return`, and the inline comment at `:350` documents a `conviction` parameter the signature does not have.
6. **A read/write asymmetry of the exact class CLAUDE.md §0.1 point 1 names.** `temperaments.py:153-158` writes drift through `_drift_store(world)` → `world.npc_drift_state` (a real, serialized `World` field). `temperaments.py:117` reads `_drift_store()` **with no `world`**, always hitting the module-level global. Any world-scoped drift ever written is invisible to its only consumer. Latent today (neither has a caller); silent the moment either is wired.
7. **`CI_GAIN_TEMPLAR` is a dead canonical constant with a docstring asserting the opposite.** `infrastructure.py:53` declares it (+1 CI/season); `ci_track.py:37` declares the dependency in prose — and imports nothing from `infrastructure`, applying no Templar term in its 5-step PP-412 computation.
8. **Latent `KeyError` in `generate_npc`.** `_ecology_weights` returns `{}` for an unknown territory (`npe.py:180-181`); `:254` and `:272` then subscript it unguarded while `:240` uses `.get`. Safe only by accident of the caller.
9. **`npe.py`'s own header contradicts its body.** `:10-15` says `game_state.World` has no NPC registry and awaits schema migration; that migration happened — `game_state.py:188-189, 302-305, 378-382` — and `npe.py:93-94` says so 80 lines later.
10. **`companion.py:4` cites a doc CLAUDE.md §6 flags as STALE** (`godot/scene_tree_architecture.md`) while `systems/npcs/companion_specification_v30.md:4` is **CANONICAL** and specifies the mechanic in full. The one line of code points at the wrong document.
11. **`Settlement.ap` is dead, and my producer's version of the claim was wrong.** It does not "always evaluate to 2" — `registry.py:92-97` adds +1 at Seat/Cathedral-City, so S-001, S-031 and S-036 give 3. The real finding is that **`ap` has zero readers anywhere in `engine/` or `systems/`.**

### §4.4 Contradictions inside single documents

`npc_relational_graph_v30.md` marks §7 and §8 **"BUILT 2026-06-09, ED-1000"** at `:501`/`:521` while `:655-657` lists B1.2 and B1.3 as *"full mechanics deferred (§7 hook only)"*. §6's `[Implemented PP-725 / B1.4]` at `:388` collides with `:657`'s "not stress-tested (§6 hook)" the same way. There is **no code behind any of them** — no `canon/relational_edges_v30.yaml`, no cascade module, repo-wide.

---

## §5 THE NARRATIVE LAYER — ⚠ I MISSED A WORKING PIPELINE

I reported that the only prose renderer is `contest/narrative.py` with no production caller. **That was a coverage failure.** A complete, runnable game-state → prose → UI pipeline already ships:

- **`systems/combat/combat_engine_v1/workbench/narrate.py`** — 116 lines, `render(events, seed)` turning the engine event stream into readable beats, *"also runnable standalone."*
- **`workbench/commentary.py`** — a **second**, independent renderer: sports-commentator transcript with per-beat mechanical annotation.
- **`workbench/server.py`** — a live stdlib HTTP server, no external deps, no build step: `POST /api/trace -> {result, narration, events}`, served into `workbench/static/index.html`, importing both renderers.
- **`contest/agon_harness.py:218-229`** — an interactive human-playable harness printing framing and verdict text, *not* using `narrative.py` — a third independent player-facing surface.
- **`contest/dictionaries.py:32-37`** — every Style and Proceeding row carries `flavor`: *"real, final, player-facing UI-card copy"*, live in code.

**The corrected finding is sharper than the one I had.** It is not that Valoria cannot render prose. It is that **the two places that can are the two places with no campaign reach** — the combat workbench (whose engine has no `queue_scene` caller, §2.1) and the contest chronicle (whose only callers are its own tests). *Rendering exists and is orphaned; the campaign loop that runs has no renderer.*

`contest/narrative.py` also **would not generalise**: `Chronicle.render()` (`:53-80`) binds to `.contract`'s A/B and a bout beat-log shaped `advA/advB/appeal/ground/gain/side/i` (`:144-148`). Contest-specific by construction.

**Authored prose is discarded at load — corrected and narrowed.** `valoria_geography_v30.yaml` carries `name`, `coords` and a hand-written `description` for each of 37 settlements. `populate_from_geography` carries **`name`** through (`registry.py:261`) and drops **`description` and `coords`**, because `Settlement` has no prose or position field. So authored strings are not wholly discarded — the *prose* is, and the *map geometry* with it.

**58 authored event cards** (`grounded_event_card_deck_v1.md`, PROPOSED) with trigger predicates and stat deltas — zero implementing code. Of the four unconstructable registered key types, one correction: `systems/world/sim/miraculous_event.py` **does exist** (a `stubwire` no-op, not absent), and `meta.legacy_event`'s declared emitter is `substrate (auto)`, which is live. The conclusion — unconstructable in a campaign — survives; two of my four stated reasons were false.

**A contest still has no subject.** No topic, claim, or argument content exists anywhere; `ground` is one of six abstract stasis tags. The authored flavor prose describes *kinds* of move and *kinds* of room, never what a debate is about. **This is the finding in this section I could not break.**

**What a campaign outputs today:** `CampaignResult` — with the correction that it does carry `winner: str` (`mc_v18.py:86`), `key_log_hash` (`:103`), and `final_state=serialize_world(world)` (`:307`), which means **37 authored settlement names do reach the terminal result.** "No string field" was false as written.

---

## §6 THE ONE BUILD THAT CHANGES THE MOST — strengthened, not weakened

> **Build the authored-person loader** — a named-NPC registry populated from canonical content at `create_world`, on the exact pattern of `populate_from_geography`.

**The antagonist pass made this recommendation stronger, because the authored content is larger and more machine-ready than I knew.** I loaded it with a YAML parser rather than reading about it:

**`references/npc_registry.yaml` holds 46 fully-structured characters.** Every entry carries `id`, `first_name`, `faction`, `role`, `birthplace`, **`territory`**, `ts`, `coherence`, a `stats` block (cognition / focus / endurance / social), a `convictions` block with **weighted primaries**, `cultural_label`, `self_other_initial` and migration notes, plus `goals` (a list of authored sentences), `arc_trajectory`, `resonant_style` and `notes`. NPC-001 is Edeyja, Warden-Chief of T15, primary Warden 0.4 / Precedent 0.2, three authored goals. Its line 5 states: *"ENFORCEMENT: No character name may appear in design docs without an entry here."*

**It has zero Python loaders — and that is a filed, named defect.** `tests/valoria/test_references_yaml_parse.py:1-9` records that the file *"was unparseable for the whole of its visible git history and NOTHING NOTICED … It survived because the file has zero Python loaders"* (ED-IN-0121).

`conviction_migration_roster_v30.md:41-245` adds 13 authored, machine-parseable conviction profiles on the same model, and `conviction_axis_matrix_v30.md:26-38` supplies a complete numeric 13×4 matrix with the composition rule written out at `:209-211`.

**So the corrected diagnosis is not "we have no people."** It is:

> **The people are authored, structured, canonical and machine-readable. Every store that would hold them is declared, routed and serialized. The single missing artifact is a loader.**

Why it still outranks the alternatives:

1. **The pattern is proven in-tree and it produced the only real entity in the game.** Settlements are realized for exactly one structural reason: authored YAML plus a loader called at world-gen.
2. **Every dormant person-mechanic is a store waiting for occupants.** `world.convictions`, `world.beliefs`, `world.knots`, `world.npcs` are declared, routed and fully serialized; `simulate_npc_actions` already runs every season over an empty dict; `Settlement.npc_ids` waits. **One loader turns four or five already-ticking systems live at once.**
3. **It converts the generator from the ceiling into the floor.** `generate_npc` cannot be the path to real people — its output is anonymous by construction, and its trigger is a ruled permanent deferral (§1). Named, placed NPCs give generated ones something to be background *to*.
4. **The counterfactuals are weaker.** The ledger first gives settlements memories of governors who are strings. Edges without instantiated NPCs is a graph with no nodes.

**It forces two fixes in passing:** a loaded NPC must seed convictions in *some* canonical taxonomy — which retires the vocabulary split and the `'Loyalty'` no-op together — and the registry's `territory` field is exactly the key `Settlement.npc_ids` and `get_npcs_in_territory` are waiting on.

---

## §7 MASS BATTLE AND WORLD — the delta that arrived after the first commit

Not previously folded in. Reported here as producer-grade; **not yet antagonist-checked** — treat accordingly.

- **`_faction_to_unit` hardcodes both sides identically** (`command=4, discipline=5, 'Line', infantry`), so only `power` varies between armies and `terrain` is always `None`. Every battle in the strategic layer is symmetric by construction.
- **The degree ladder is read on one path and dead on the other.** The strategic `degree` drives the Terms/Storm fork; the per-engagement `degree` is dead in TREE A and load-bearing in TREE B.
- **`insurgency_pipeline.py` promotion is structurally dead** — `rec.L` is set once to 1.0, the gate requires ≥3, and nothing else writes it.
- **Every `systems/world/` lore doc has zero code citations.** The world's authored material has no mechanical surface at all.

---

## §8 WHAT THE ANTAGONISTS OVERTURNED — the falsifier record

Per CLAUDE.md §0.1 point 3, the corrections belong in the same document as the claims, named.

| My claim | Verdict | Correction |
|---|---|---|
| "The gap is **ONE function body**" | **OVERTURNED** | Four structural blockers; no world reach, no sink, no types, no destination (§2.2) |
| "13 triggers fire **every season**" | **OVERTURNED** | **Zero** fire in a default campaign; the only emitted type is not in the trigger list |
| "`articulation.subscribe_all` is unconditional" | **CORRECTED** | Flag-gated inside `_echo_transport_on` |
| "~6-7 of 25 settlement fields populated" | **CORRECTED** | **8 of 25**, and `owner_faction` for **37 of 37**, not 1 |
| "4 of `conviction.py`'s 9 are in no taxonomy" | **OVERTURNED** | **Zero.** It is the legacy 9 verbatim; the defect is supersession violation (§4.2) |
| "Justice/Survival/Power in no taxonomy" | **CORRECTED UPWARD** | **Six** of eight absent from the 13; and all eight are quoted verbatim from canon at `investigation_systems_v30.md:84` |
| "`contest/narrative.py` is the only prose renderer" | **OVERTURNED** | Three more exist, one with a live HTTP UI (§5) |
| "Authored strings are discarded at load" | **NARROWED** | `name` is carried; `description` and `coords` are dropped |
| "`CampaignResult` has no string field" | **FALSE** | `winner`, `key_log_hash`, and `final_state` carrying 37 settlement names |
| "`Settlement.ap` always evaluates to 2" | **FALSE** | 3 at Seat/Cathedral-City; the real finding is zero readers |
| "No actor class exists" | **SCOPED** | True of **PCs**; false of actors — `NPC` and `Combatant` are real |
| "`generate_npc` uncalled" (framed as oversight) | **REFRAMED** | A ruled permanent deferral (OI-05) whose oversight framing the corpus already retracted |
| "`miraculous_event` has no `.py`" | **FALSE** | It exists as a `stubwire` no-op |
| "'do not build it here' ×6" | **CORRECTED** | Twice |

**Prior art I failed to cite** — findings I presented as discoveries that were already filed:

- **`proposals/2026-08-15-character-and-faction-stats-and-progression.md:342-343`** already records the superseded-9 roster *and* the `'Loyalty'` no-op, seven days before this session. I never opened `proposals/`.
- **`audit/2026-08-10-subsystem-atlas-verification/code_strategic.md:82-120`** already records the 8-field boot population, inert `legitimacy`/`popular_support`, the `religious_building` collision, and `ap`/`add_tag`/`succeed_governor` callerless. One producer even inherited that audit's off-by-one line number (`registry.py:81`, actually `:82`) — evidence it read the audit rather than the file.
- **`settlement_layer_v30.md:740-778`** specifies the Dearth/granary chain in full as **ED-SE-0008 (PROPOSED)**, including the exact `granary: int (0-3)` registry field. Reporting "zero food/harvest code tree-wide" without naming it reads as *canon is silent* when canon is explicit and awaiting ratification.
- **ED-IN-0121** already records `npc_registry.yaml`'s zero-loader status.

**Presenting tracked defects as discoveries inflates apparent yield.** The method fix is one line: *read `proposals/` and `audit/` before claiming a defect is new.*

---

## §9 WHAT REMAINS UNVERIFIED

| Claim | Basis | Confidence |
|---|---|---|
| Population is zero; `generate_npc` uncalled | Fable full-read + antagonist + xfail manifest | **high** |
| Articulation cannot render from what it receives | antagonist, **re-verified by me** at `articulation.py:140/152`, `keys.py:576-577`, `mc_v18.py:241/257` | **high** |
| `owner_faction` 37/37; 8 of 25 fields | **re-verified by me**, YAML parsed | **high** |
| `conviction.py` = legacy 9 verbatim | **re-verified by me**, both files read side by side | **high** |
| 46 authored characters in `npc_registry.yaml` | **re-verified by me**, YAML parsed | **high** |
| The `'Loyalty'` scar no-op | Fable + antagonist + a filed proposal | **high**, but **latent, not live** — knot formation is itself deferred (`mc_v18.py:204-209`) |
| Ledger's only production caller is `ledger_sweep` | Fable + antagonist full season-path read | **high** |
| Social contest is `logos_spammer` vs `logos_spammer` live | producer + the lane's own prior audit | medium-high |
| Threadwork entirely unreachable | producer | medium — **no antagonist ran on this** |
| §7 mass battle / world findings | producer only | **medium — no antagonist ran on this** |

**Coverage gaps the antagonists declared, carried forward honestly:** `systems/npcs/{npc_behavior,npc_roster,npc_foils,npc_character_analyses}_v30.md` and `npcs_flow_skeleton_v1.md` unread; `character_histories_v30_infill.md` and `conviction_track_v30*` unread; 14 of 17 `systems/factions/sim/` modules unread; `systems/overview/sim/season.py` unread, so "every season" for the NPE call rests on a comment rather than a read.

**The single most useful next check** is no longer §2.2's tractability — that one is settled and negative. It is whether the authored-person loader can be written against `npc_registry.yaml` **without** first resolving the conviction taxonomy split, since every one of the 46 entries carries weighted convictions in the canonical 13 while the live validator runs the legacy 9.
