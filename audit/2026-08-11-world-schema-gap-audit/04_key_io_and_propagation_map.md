# Key I/O and propagation map — the bus, as declared and as built

## Status: REFERENCE — a traced map over existing artifacts. **Ratifies nothing.**

**Date:** 2026-08-11 · **Lane:** IN · **EDs:** ED-IN-0153 (audit), ED-IN-0155 (stale emit-coverage measurement) · **Base:** `63d4d0c`

Companion to [`03_discussion.md`](03_discussion.md). Where that document asks *what is missing*, this
one asks **how information moves** — every key type that exists, is stubbed, is missing, or is
proposed, arranged so the propagation paths are visible as paths rather than as a list.

**Every count below was recomputed from `references/key_graph.json` and the tree this session.** Where
a number contradicts a figure carried elsewhere in the corpus, the contradiction is stated rather
than quietly resolved (§3.1).

---

## 1. The transport — there is exactly one

Before any topology: the mechanism. A Key does not travel by being consumed. It travels by
`TickScheduler`, and the substrate offers **two distinct channels**, which the rest of this document
depends on keeping apart:

| Channel | Call | Effect | Live sites |
|---|---|---|---|
| **Deferred-apply (OF-7)** | `sched.emit(key, apply=fn)` | key is logged immediately; `fn` runs at `accounting_boundary()` and **writes state** | **2** |
| **Log-only** | `sched.emit(key)` | key is logged; **nothing is written, ever** | **2** |
| **Subscription** | `sched.subscribe(type_id, cb)` | `cb` fires on matching emissions | 13 type_ids, **all stub callbacks** |

`engine/substrate/keys.py:506` defines `subscribe`. **`articulation.py:169` is the only production
`.subscribe(` call site in the entire tree** — every other hit is a test — wired from
`engine/mc_v18.py:258` → `subscribe_all(world.echo_scheduler)`. `articulation.py:164`'s own docstring
records that calling it twice registers duplicate callbacks.

**A third emission path exists and is unexercised.** `keys.py:525` defines `schedule_emission()` — the
B1 cascade path (OF-B1, `propagation_spec` §4.2), also `apply=` capable. It has **zero production
callers**; the only references outside `keys.py` itself are in `tests/valoria/test_key_substrate.py`.
It is omitted from the table above because the table counts live sites, but the omission matters for
§7: `echo_transport.py:91` sets `DEFAULT_CASCADE_DEPTH_MAX = 0`, so a `schedule_emission` during drain
would raise `TerminationBreach` (`keys.py:531-535`) under default parameters. **The cascade half of the
substrate is not merely unused — it is switched off by default and has never run in production.**

**The consequence that shapes everything below:** consumption and state-change are different
mechanisms. `apply=` writes; `subscribe` observes. A key can have a declared consumer, a live
subscriber, and still change nothing — and today, 13 of the 13 subscribed types do exactly that.

---

## 2. The bus as **declared**

55 key types across 7 families; 27 modules. Recomputed from `key_graph.json` (which itself joins the
registry's prose `emitting_systems`/`consuming_systems` against the contracts' typed `emits`/`consumes`).

**Families:** `mechanical_event` 12 · `system_meta` 11 · `scene_outcome` 8 · `scene_event` 8 ·
`state_transition` 7 · `da_outcome` 5 · `environmental` 4.

### 2.1 Topology — who is on the bus, and in which direction

| module | emits | consumes | role |
|---|---|---|---|
| `articulation_layer` | 1 | **43** | absorber |
| `npc_behavior` | 11 | **31** | absorber |
| `faction_state` | 3 | **25** | absorber |
| `piety_track` | 1 | 9 | absorber |
| `scene_slate` | 8 | 0 | producer-only |
| `domain_actions` | 6 | 0 | producer-only |
| `faction_politics` | 4 | 0 | producer-only |
| `fieldwork_knots` | 4 | 0 | producer-only |
| `peninsular_strain` | 4 | 0 | producer-only |
| `social_contest` | 4 | 1 | both |
| `personal_combat` | 3 | 2 | both |
| `settlement_layer` | 3 | 2 | both |
| `game_director` | 3 | 0 | producer-only |
| `engine_clock` · `scenario_authoring` · `threadwork` · `victory` | 2 each | 0 | producer-only |
| `ci_political` · `mass_battle` · `miraculous_event` · `territorial_piety` | 1 each | 0 | producer-only |
| `campaign_architecture` · `clock_registry` | 0 | 0 | **on the bus roster, no edges at all** |
| ~~`echo_transport`~~ · ~~`player_input`~~ | 1 each | 0 | **NOT contract modules** — see below |
| `npc_memory` | 0 | 4 | consumer-only |
| `audit` · `scene_timer` | 0 | 3 each | consumer-only |
| `settlement_economy` | 0 | 2 | consumer-only |

⚠ **Roster correction (found by adversarial review of this document).** `echo_transport` and
`player_input` emit on the bus but are **not contract modules** — `key_graph.json` files both under
`unresolved_references`, alongside `all`, `all subscribing systems`, `legacy-aware consumers only` and
`substrate (auto)`, and `KEY_INDEX.md:57-58` marks them *"not a contract module — unresolved
reference"*. Conversely `campaign_architecture` and `clock_registry` **are** among the 27 modules and
carry **zero key edges in either direction**. An earlier version of this table listed the first two as
modules and omitted the second two; the total of 27 survived only because the errors cancelled. The
corrected reading is sharper: **two of the 27 modules are on the bus roster and touch the bus not at
all**, and two emitters are prose names with no contract behind them (one of ED-IN-0151's four held
decisions).

### 2.2 Three readings of that table

**(a) The bus is a funnel, not a mesh.** Four absorbers take **108 of the 125 declared consume
edges — 86.4%** (recomputed from `key_graph.json`: 125 consume edges, 69 produce edges). Sixteen of 27 modules consume *nothing at all*. This is not inherently wrong — a substrate
observer legitimately reads everything — but it means the declared graph is mostly *scene/faction
producers → three sinks*, not systems talking to each other.

**(b) `articulation_layer`'s 43 is a wildcard, not 43 decisions.** It declares `{type: "*"}` — a
deliberate universal read of the Key stream — and the join does not expand wildcards, so every
explicit type the registry names it against appears as an under-declaration. `KEY_INDEX.md` reports
**44 of 52 undeclared edges belong to this one module**. Whether the wildcard should be expanded into
explicit declarations is one of ED-IN-0151's four held decisions. **It is one decision, not 44.**

**There are two such declarers, not one.** `module_contracts.yaml:387` gives `fieldwork_knots` the
identical construct — `{type: "*", from: engine}`, commented *"Memory Query API — Bonds ≥ 5
prerequisite"* — and `KEY_INDEX.md:45` names both. `fieldwork_knots` appears as consumes-0 in §2.1
for the same reason `articulation_layer` appears as consumes-43: the join treats one wildcard as
unresolvable and the other as expandable. **Two modules read the whole stream by declaration, and the
generated view renders them incomparably.**

⚠ **A fourth divergent count for the same quantity exists**, one file from where this map looked:
`module_contracts.yaml:973` comments that *"registry also lists 31 explicit per-type subscriptions"*
for `articulation_layer`, against the join's 43, the 44-including-wildcard figure, and the 13
actually subscribed in code. Four numbers for adjacent quantities — the same rot class as §3.1.

**(c) Consumer-only modules are the honest signal.** `npc_memory` (4 consumes, 0 emits) is declared
as a pure sink — and its `state:` block is empty, with no memory store in code. A module that only
reads and holds nothing cannot be doing what its contract says. This is G-39.

### 2.3 Terminals

- **1 key nobody produces:** `meta.legacy_event`. A payload schema no system fills.
- **8 keys nobody consumes:** `env.crisis`, `mechanical.era_transition`, `mechanical.season_change`,
  `mechanical.second_calamity`, `mechanical.settlement_captured`,
  `mechanical.theocracy_unification_declared`, `meta.legacy_event`, `state.settlement_revolt`.

**How to read that 8 — corrected by adversarial review, because the first reading was backwards.**

**5 of the 8** are deliberate **DECLARE-ONLY** registrations: `mechanical.settlement_captured`,
`mechanical.era_transition`, `mechanical.second_calamity`,
`mechanical.theocracy_unification_declared` (`key_type_registry_v30.md:1251`) and
`state.settlement_revolt` (`:1252`). The registrations are **ED-IN-0014** (OI-25, 2026-07-29 W3);
**ED-IN-0096** is the *later correction* that emptied their `consuming_systems`. An earlier version of
this section credited the registrations to ED-IN-0096 and said *"the emit exists"*. **Both were
wrong.** The registry's own words are *"all DECLARE-ONLY, **zero live emit calls**"*, and `:750` spells
out the intent: *"registration now, emit call when the evaluator is built."*

The correction reverses the conclusion. These five have **no producer in code and no consumer**, which
makes them *more* debt-shaped than a key with a live emitter and no reader — and the claim contradicted
§3.2 of this very document, where none of the five appears among the live-emitted types. **Do not read
the 8 as closed.** `02_verdict_and_residuals.md` §3 item 4 holds **all eight** at ED-IN-0151 item c.

Two of the remaining three are a *different* defect: `env.crisis` and `mechanical.season_change`
declare their consumers as unresolvable wildcards — `[all]` and `[all subscribing systems]` — while
their siblings name real modules. **That is a join defect, not an absent declaration** (G-42),
invisible from the generated view, which renders both as a blank cell.

The eighth is `meta.legacy_event`, and it is the strangest entry on the bus: the **only key nobody
produces**, with a *third* wildcard consumer form (`[legacy-aware consumers only]`), a
`default_scale_signature: [system_meta]` that is **not a member of `SCALES`** (§6.4 — it would raise at
runtime exactly as `territorial` does), and an `emitting_systems: [substrate (auto)]` that is not a
module name. Untouched by this audit and flagged here so it is not mistaken for covered.

---

## 3. The bus as **built**

### 3.1 A correction: the "1 of 55" figure is stale, and nothing guards it

`tests/valoria/test_key_graph.py:4` states, in its module docstring:

> *"MEASURED 2026-08-02: **55 key types declared, 1 emitted anywhere in the codebase**
> (`scene.accord_echo`), while the real inter-subsystem traffic is 16 direct Python imports. The
> contracts reference 47 dotted key names; implemented coverage is ~2%."*

**That figure is prose in a docstring. No assertion in that file tests it.** All twelve test
functions were read: they assert graph non-vacuity, producer/consumer presence, the shrink-only
`KNOWN_NO_PRODUCER`/`KNOWN_NO_CONSUMER` ratchet, participant-module reality, conflict-freedom, name
well-formedness, rebuild currency and module authority. **Not one references an emit count.**

And measured this session, the figure is wrong: **four real `sched.emit()` call sites carry five
distinct type_ids** (§3.2), not one.

⚠ **Why it is wrong is an open question, and the first version of this section answered it without
evidence.** That version said the emit sites were "dated after the measurement" — i.e. ordinary rot.
**No date on disk supports that, and two contradict it:** `key_type_registry_v30.md:1254` dates
`scene.accord_echo`'s live emit to *"ED-IN-0091 plan §3 Wave 3 Handoff item 1 (**2026-07-29**) —
LIVE (queued via sched.emit, not declare-only)"*, and `echo_transport.py:368` dates the same write to
*"as of W3 Handoff item 1, **2026-07-29**"*. Both **precede** the docstring's *"MEASURED 2026-08-02"*.

If those dates hold, this is not a measurement that rotted — it is **a measurement that was false when
written**, which is the worse class: a number published with no instrument, in the unfavourable
direction (§0.1 point 4 cuts both ways). Neither reading is asserted here; the commit dates were not
checked, and **that is the open item**. Either way the fix is the same guard.

Filed as **ED-IN-0155**. I repeated the stale figure earlier in this session before measuring it,
which is how it earns a ledger entry rather than a silent correction.

### 3.2 The live emit ledger — 4 call sites, 5 type_ids

| # | type_id | site | channel | what it actually does |
|---|---|---|---|---|
| 1 | `scene.accord_echo` | `engine/cross_scale/echo_transport.py:343` | **`apply=`** | writes `Settlement.order` at the accounting boundary |
| 2 | `scene.contest_resolved` | `echo_transport.py:438` (via `KEY_TYPE_BY_SCENE`) | **`apply=`** | writes a faction stat delta at the accounting boundary |
| 3 | `scene.combat_resolved` | `echo_transport.py:438` (same site, same map) | **`apply=`** | as above |
| 4 | `da.public_governance` | `systems/factions/sim/parliamentary_transfer.py:176` | log-only | **nothing** — `# NO apply= -- log-only, byte-exact goldens cannot move` |
| 5 | `scene.battle_concluded` | `systems/factions/sim/faction_action.py:394` | log-only | **nothing** — `# NO apply= — log-only, deferred nothing, writes nothing` |

`KEY_TYPE_BY_SCENE` (`echo_transport.py:97-100`) maps exactly two scene types, with a guardrail
comment: *"Only the two live personal-scale resolvers are mapped; adding a scale here without its
resolver is shape-divergence."*

**Both log-only emits sit inside swallowing `try/except` blocks** (`faction_action.py:395-397`,
`parliamentary_transfer.py:177-179`) that re-raise only under `VALORIA_STRICT_KEYS`. So "log-only"
understates them: under a payload defect they log **nothing**, silently, and the default configuration
is the silent one.

**Reachability confirmed, not assumed.** `emit_scene_echo` has two production callers:
`engine/cross_scale/parliamentary_bridge.py:212` (the contest leg) and
`engine/cross_scale/scene_dispatch.py:392` (dispatched scenes).

**So the live bus is: 5 of 55 type_ids emitted (9%), of which 3 write state and 2 write nothing.**

### 3.3 The subscriber wall

`articulation.py:116-130` subscribes **13 type_ids**: `state.scar_acquired`, `state.coup_attempted`,
`state.succession`, `mechanical.mission_shift`, `da.covert_betrayal`, `meta.knot_formed`,
`meta.knot_ruptured`, `env.peninsular_strain_shock`, `meta.cascade_cluster_event`,
`state.belief_revised`, `scene.combat_resolved`, `scene.combat_felled`, `scene.accord_echo`.

Every callback is a `stubwire.stub_resolve` no-op. The module's own comment is candid about why:
*"the minimal bus subscriber observes the zero-subscriber state without inventing the render layer."*

**Note the near-disjointness.** Of the 5 live-emitted types, only **2** (`scene.combat_resolved`,
`scene.accord_echo`) are subscribed — and `scene.contest_resolved`, one of the three types that
actually writes state, is subscribed by nobody. Of the 13 subscribed types, **11 are never emitted by
any live producer**. The two halves of the bus were wired against the *declared* graph, independently,
and they barely touch.

---

## 4. Throughlines

### T1 · The one fully closed loop
```
scene resolves  →  emit_scene_echo / _apply_accord_echo
   →  Key(scene.accord_echo, scale=[settlement], targets=[{actor_id: sid, stat_deltas:{order: Δ}}])
   →  sched.emit(key, apply=_apply)          [logged now]
   →  accounting_boundary()                  [deferred]
   →  Settlement.order  ← written
```
The only path where a Key emission changes settlement-scale state. It carries `causes=[upstream_key_id]`
when a genuine upstream Key exists and `[]` when it does not — the honesty rule is enforced by
`engine/tests/test_accord_echo.py`. **This is the template every proposed key below should be read
against.**

### T2 · Domain Echo — personal → faction
```
contest / combat resolves  →  emit_scene_echo(scene_type, result, ctx, world)
   →  KEY_TYPE_BY_SCENE  →  scene.contest_resolved | scene.combat_resolved
   →  targets=[{actor_id: affected_faction, stat_deltas:{affected_stat: Δ}}]
   →  sched.emit(key, apply=_apply)  →  accounting_boundary()  →  faction stat written
```
Two scales bridged: personal/scene → faction. **Settlement, territory and province are not
participants in any cross-scale path** — `module_contracts.yaml` names the transition
*"scale_transitions §3.2 Personal → Faction"*, skipping the middle rungs by name.

### T3 · Log-only emissions — the bus as an audit trail
`da.public_governance` and `scene.battle_concluded` are emitted with no `apply=`, **deliberately**:
both comments cite byte-exact goldens that cannot move. They make the log truthful about what
happened without letting the log drive anything. Legitimate, and worth naming because from the
declared graph they are indistinguishable from T1.

### T4 · The subscriber wall — where consumption stops
```
13 subscribed type_ids  →  _make_trigger_callback(type_id)  →  stubwire.stub_resolve(...)  →  ∅
```
Subscription is real and wired; consumption is not. **This is the single largest structural fact
about the bus:** the transport works, one subscriber exists, and no subscriber does anything yet.

### T5 · Broken throughlines — where a chain is *specified* and a link is absent

Each row is a path canon requires, with the missing link named. Register IDs in brackets.

| # | Intended throughline | Missing link |
|---|---|---|
| B1 | settlement captured / revolts → province ownership recomputed → faction Mandate | **neither producer nor consumer** — both are DECLARE-ONLY (ED-IN-0014), so nothing emits them either; all 8 held at ED-IN-0151 item c. *(An earlier version cited G-42 here; G-42 is the `env.crisis`/`season_change` wildcard pair, a different defect.)* |
| B2 | population shock → settlement Population → Prosperity | `env.population_change` is **declared** as emitted into a field that does not exist — `settlement_layer` has no Population state row. Not among the 5 live-emitted types, so nothing emits it today either. G-30's own softener: Settlement Weight `W_s` partly operationalises Population already [G-30] |
| B3 | territory Accord hits 0 → territory Uncontrolled → Turmoil +1 | **no key type can carry it.** Only the settlement-scale analogue was ever declared [G-26] |
| B4 | territories stop sharing a holder → province dissolves | **no key at all** for province formation/dissolution, though B12 makes existence conditional [G-27] |
| B5 | faction declared / collapses / splits → world learns a new actor exists | **no lifecycle key at any tier**; four lanes across three passes [G-01] |
| B6 | NPC's Standing moves on one of 4+ ladders → faction learns which | `state.standing_change` carries **no `faction_id`, no `ladder_id`** [G-08] |
| B7 | conviction resolves → Truth shift, arc trigger, Domain Echo eligibility, Portrait | **no key type** for the game's central progression mechanic [G-28] |
| B8 | NPC project completes/fails → a new project forms | `state.project_completed` / `_failed` exist; **`state.project_formed` does not**, so the loop cannot close [G-29] |
| B9 | scene → NPC memory → later behaviour | `npc_memory` consumes 4 types and **owns no store** [G-39] |
| B10 | treaty signed → binding state → expiry → Casus Belli | **no module owns `World.treaties`**, and no key represents an *ongoing* treaty. Sharper than first written: `register_treaty`/`process_treaty_expirations` have **zero production callers** (G-07 correction b), so `da.diplomatic_alliance` fires not once but **never** [G-07, G-06] |
| B11 | faction affiliation changes | **no key**; `NPC.affiliation_faction` is set once at generation [G-40] |
| B12 | settlement governance action names its target settlement | `da.public_governance` is territory-grained [G-31 — *see §6.3, partly refuted*] |

**The shape across B1–B12:** eleven of twelve break at the *consumer or state* end, not the producer
end. The engine can say what happened. It cannot record it, and it cannot hear it.

---

## 5. Proposed keys, placed on the bus

Eight `propose_key` rows. Every one composes on an existing family and cites a sibling — none
introduces a family, and none special-cases an entity.

| Row | Proposed type_id | Family | Composes on | Closes |
|---|---|---|---|---|
| G-01 | `state.faction_lifecycle_event` | `state_transition` | `state.succession` | B5 |
| G-04 | `state.governor_changed` | `state_transition` | `state.succession`, `state.coup_attempted` | settlement governance |
| G-08 | `state.standing_change_v2` *(sibling, not a payload edit)* | `state_transition` | `state.standing_change` | B6 |
| G-26 | `state.territory_revolt` | `state_transition` | `state.settlement_revolt` | B3 |
| G-27 | `mechanical.province_coherence_changed` | `mechanical_event` | `mechanical.era_transition` | B4 |
| G-28 | `state.conviction_resolved` | `state_transition` | `state.belief_revised` | B7 |
| G-29 | `state.project_formed` | `state_transition` | `state.project_completed`/`_failed` | B8 |
| G-40 | `state.affiliation_changed` | `state_transition` | `state.standing_change` | B11 |

**Seven of eight land in `state_transition`** — the table above shows seven, and an earlier version
of this sentence said six. Only G-27 lands elsewhere (`mechanical_event`). The family sizes are `mechanical_event` 12 ·
`system_meta` 11 · `scene_outcome` 8 · `scene_event` 8 · `state_transition` 7 · `da_outcome` 5 ·
`environmental` 4 — so `state_transition` is mid-sized, **not** the smallest, and any claim that it is
should be rejected. The load-bearing ratio is the one between the two families that model *change*:
**7 entity-state-transition types against 12 world-event types.** The bus is richer in things that
happen to the world than in things that happen to its entities, which is the opposite weighting an
emergent-narrative engine built on persistent entities needs — and it is why six of eight proposals
land on the lighter side.

⚠ **Two counts exist for `state_transition` and this section uses the smaller.** `key_graph.json`'s
`family` field gives **7** (physical filing); the registry's own §9 logical table
(`key_type_registry_v30.md:1252`) gives **9**, because two `state.*` types are physically filed under
§8 `system_meta`. `KEY_INDEX.md:144` documents the split. The 7-vs-12 contrast is therefore the
*flattering* framing; on the logical count it is 9-vs-12 and the asymmetry is milder. Stated so the
argument can be checked rather than taken.

**G-08 is the row worth reading closely**, because the critics inverted its cost. Two lanes proposed
*adding `faction_id` to `state.standing_change`'s payload*. `key_type_registry_v30.md:1273-1278` makes
modifying `required_payload_fields` a **Class A supersession event** — supersession register entry,
migration path for existing Keys, Class A patch entry — while adding a new type is Class B. **The
"smaller" fix is the expensive one.** The register therefore proposes a sibling type.

### 5.1 All eight are blocked by the same door

§10 of the registry (RATIFIED, ED-IN-0026) forbids appending **any** new key type without a row in
`references/rendering_dispositions.yaml` — a per-type verdict on *how the player ever sees this*
(RENDERED-RICH / GENERIC / UNRENDERED / DELIBERATE-SILENT). **That file does not exist** (verified by
directory listing). The gate is currently report-only and flips to blocking once the file exists and
the 55-type backlog is at zero.

⚠ **Precision this map got wrong first time, and G-17 exists to correct.** §10's A15 enforcement is
**report-only today** (`key_type_registry_v30.md:1287-1291`), flipping to blocking once the file exists
and the backlog is at zero. So appends are **governed and unrecorded, not mechanically refused** — an
earlier version said *"nothing in the key half can proceed until this is answered or waived,"* which
overstates a live gate into a locked door. The practical position is worse in a subtler way: eight
keys *could* be appended today and each would enter with **no recorded answer to "how does the player
ever see this?"**, which is the exact debt §10 was written to stop accumulating.

**G-17 is still the first move**, and it is a Jordan call: author the file and disposition the existing
55, or waive the precondition deliberately.

---

## 6. What the bus can and cannot express

Four semantics that determine whether a proposed key is even necessary. **Two of the four refuted
producer claims in this audit** came from reasoning about a key type without reading the substrate.

### 6.1 `causes[]` — provenance is already solved
Keys carry `causes=[key_uuid]`, and the substrate invariant is that referenced keys are already in the
log. All four live emit sites, across three modules, populate it honestly and cite `[]` rather than
fabricate (`echo_transport.py:403` populates; `faction_action.py:365-368` and
`parliamentary_transfer.py:166` explain their `[]`). **Any "we cannot
trace why this happened" claim is false**: the channel exists and is used.

### 6.2 `targets[]` — arity is already solved, and two lanes missed it
`key_substrate_v30.md:45-53` defines `targets[]` with per-target `role` (subject/object/witness/
beneficiary/bystander), `impact_vector` and `stat_deltas`. Two producer lanes reasoned from a type's
`optional_payload_fields` table to *"this key cannot express a multi-target fan-out"* — and the live
`scene.accord_echo` emitter populates exactly that array.

> **Rule for anyone extending this map: a claim that a key cannot express an arity must cite
> `key_substrate_v30.md`, not the type entry. The type entry does not describe the envelope.**

### 6.3 Grain — and the one place §6.2 does *not* rescue
G-31 claimed `da.public_governance` cannot name a target settlement. The critic softened it: the
"territory-only across the whole family" half is **false** as written, and whether a settlement id is
a legal `actor_id` in `targets[]` is an open substrate question (held, §3 item 12 of `02`). If it is
legal, no payload field is needed. **This is a genuine open question, not a gap** — and it is the
question two lanes answered wrongly in opposite directions.

### 6.4 `scale_signature` — the vocabulary is split four ways
`engine/substrate/keys.py:65` is the enforced runtime roster:

```python
SCALES = ("personal", "settlement", "territory", "peninsula")
```

Four values. **No `provincial`, no `national`, no `duchy`, no `country` — and no `scene` or `thread`
either**, both of which `module_contracts.yaml` uses. Measured this session: `provincial` appears
**0 times** in the key type registry, while it is the declared scale for every faction module in the
contracts.

`faction_action.py:369-371`'s own comment shows a live emitter navigating this by hand: *"'territory',
not 'provincial': the substrate's canonical roster is
`("personal","settlement","territory","peninsula")`."*

**Unification is HELD at ED-IN-0103 §6 fork 1**, whose text bars any change "here or anywhere else."
This map contributes measurements and proposes nothing. But the practical consequence should be
explicit: **a key emitted at a scale the substrate does not know is rejected at runtime** —
`keys.py:415-418` raises `KeyValidationError`, it does not warn, so the vocabulary split is not cosmetic — it is a hard constraint on which of §5's
proposed keys can carry the scale their design needs. `state.faction_lifecycle_event` at *national*
scale has nowhere legal to sit today.

### 6.5 One executable parser defect, found and unfixed
G-18, and this map owes it a citation the first version omitted. The defect is
**`engine/substrate/keys.py:294`**:

```python
elif value.startswith("[") and value.endswith("]"):
```

falling through to `:297-298`'s `else: entry[field] = value` — a bare string.
`key_type_registry_v30.md:1084` declares
`default_scale_signature: [territorial]   # peninsular when abs(similarity) > 0.95 …`, which does not
end in `]` and therefore **silently parses as a scalar**.

**It is a pattern defect, and the parser's own docstring proves it.** `keys.py:275-276` advertises
support for block lists *"(`- item`, inline `# comments` preserved)"* **and** flow lists — so
comment-tolerance was implemented for one shape and not the other. That is the §0.1 point-5 signature:
any entry with a trailing comment on a flow line is affected.

**Blast radius, which the first version did not scope:** `tools/build_key_graph.py:155-170` parses with
real `yaml`, so the *generated* graph is unaffected. The damage is confined to the substrate's own
registry loader. Note also that `territorial` is not in `SCALES` regardless, so this entry would fail
invariant 7 at `keys.py:415` if it ever reached validation — a second, independent defect on one line.
A correction, not a ruling; it should not wait on the held forks.

---

## 7. Five holistic observations

1. **The transport is largely sound; the endpoints are not.** OF-7 deferred-apply, `causes[]`
   provenance and `targets[]` arity are a coherent bus design, and every *schema* finding is at an
   endpoint — a producer that does not emit, a consumer that does not exist, or state with nowhere to
   live. **Two qualifications, both from adversarial review of this document**, and the first version
   asserted the unqualified claim: the substrate's registry loader carries a live parser defect
   (§6.5, `keys.py:294`), and its **cascade path has never run** — `schedule_emission` (`keys.py:525`)
   has zero production callers and `DEFAULT_CASCADE_DEPTH_MAX = 0` would raise `TerminationBreach` if
   it did. "No defect in the substrate" was too strong.
2. **Emission and consumption were wired against the declared graph independently, and barely meet.**
   11 of 13 subscribed types are never emitted; 3 of 5 emitted types are never subscribed. Neither
   side is wrong on its own terms; nobody checked them against each other. A join test — *"every live
   emitted type has a live subscriber, or a recorded reason it does not"* — would have caught this and
   does not exist.
3. **The bus is a funnel into three sinks, two of which cannot hold anything.** `articulation_layer`
   (43 consumes) is all stubs; `npc_memory` (4 consumes) owns no store. Of the four absorbers only
   `faction_state` has real state to write into.
4. **`state_transition` carries seven of eight proposals** (not six, and it is *not* the smallest
   family — `environmental` 4 and `da_outcome` 5 are smaller). The registry grew around *world events*
   (12 `mechanical_event`) rather than *entity state changes* (7 physical / 9 logical). For an engine
   whose narrative comes from persistent entities changing, that weighting is inverted.
5. **The most consequential absence is not a key — it is a shape.** G-24: the bucket taxonomy is
   `{derived_value, track, clock, pool}`, four shapes all for single-owner scalars. Treaties,
   relational edges, subnational footholds and sanctions are all per-counterparty relations with no
   legal shape, so each is stored as an untyped dict outside the schema. **Adding all eight proposed
   keys would not fix one of them.**

---

## 8. What this map does not cover

- **It is a map of the *declared* and *live* bus, not of all inter-module traffic.** The corpus's own
  figure is that real traffic is dominated by **direct Python imports**, not Key emissions. Those
  imports are not mapped here; `references/ENGINE_ATLAS.md` and the flow skeletons cover them.
- **No path was verified by execution.** Reachability claims rest on grep plus caller tracing. No
  campaign was run, no key log inspected at runtime.
- **The 16-direct-imports figure is from the same stale docstring as the 1-of-55 figure** (§3.1) and is
  **not** re-measured here. Do not cite it without measuring.
- **Subsystems that produced no findings produced no throughlines**: combat, social contest,
  fieldwork, threadwork, UI, victory. Their key I/O is present in §2's declared topology and was not
  traced against code.
- **`meta.legacy_event`** — the one key nobody produces — is listed in §2.3 and not investigated.
