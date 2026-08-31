# F2 — ADJUDICATION: keys, naming, vocabulary

Adjudicator: Fable 5, read-only pass, 2026-08-31. Governing rules applied: `CLAUDE.md` §0.05 (code is
mechanism, prose is reference), §0.1 (a claim ships with its falsifier), §0 five-test escalation
ordering, §4 (idempotent in meaning · idiomatic in choosing · define it in BOTH places).

---

## 0. METHOD, and what I verified myself

Primary sources read in full, in the working tree: `engine/substrate/keys.py` (601 lines),
`proposals/2026-08-31-ideal-v2/03_COMPENDIUM.md` (950 lines, all sections),
`proposals/_session_provenance/2026-08-31-fable5-review/v2/KEYS_AUDIT.md` (982 lines),
`proposals/canonical_nomenclature_v1.md` (342 lines), `systems/_architecture/key_substrate_v30.md`
(header + §1–§4 structure), the ED-IN-0200 and ED-IN-0201 ledger rows extracted programmatically from
`registers/editorial_ledger_in.jsonl:56-57`, and `proposals/2026-08-29-greenfield-systems-suite-v2/00_INDEX.md:185-300`
(the rival ED-IN-0200 execution). `references/module_contracts.yaml` parsed with `yaml.safe_load`
(27 modules, 27 composition_roles); `engine/engine_params/key_types.json` parsed with `json.load`
(55 types, `type_count` self-consistent). Trace logs R4/R1/R2 and PR340/341/344 read as secondary
sources; **every collision claim below that came from a log was re-verified by grep or read against
the working tree**, and the greps for the NEW collisions (§4: `stance`, `witness`, `strike`,
`envelope`, `payload`) are mine, run this session against `engine/`, `systems/`, `references/`,
`tools/`, `tests/`. Line numbers cited are from today's tree; where the design's citations have
drifted from it, §8 says so.

What I did not do: read all 2,186 lines of `01_ARCHITECTURE.md` or the 18-file greenfield suite in
full (I read their register/hierarchy sections and the PR logs); grep `godot/` exhaustively beyond
the cited classes; run any code. Marked `[unclear]` where that matters.

---

## 1. ⭐ THE KEY SUBSTRATE AS IT EXISTS

**This is the one executable identity-and-event mechanism in the repository.** Under §0.05 it is
MECHANISM; `key_substrate_v30.md` and `key_type_registry_v30.md` are its reference prose (the prose
is CANONICAL-class, PP-687, but if the two disagree the code is the formula). Status: RATIFIED
(ED-IN-0018 2026-07-07; §5 fork docket ruled ED-IN-0026 same day) — `keys.py:1-48` docstring.

### 1.1 The enums (closed, enforced at validation)

| enum | members | where |
|---|---|---|
| `AXES` | hierarchical · sacred · instrumental · traditional | `keys.py:59` |
| `ROLES` | **subject · object · witness** · beneficiary · bystander | `keys.py:62` |
| `SCALES` | personal · settlement · territory · peninsula | `keys.py:65` |
| `PERMANENCE_VALUES` | transient · persistent · indelible | `keys.py:67` |
| `TIME_HORIZON_VALUES` | immediate · near · far | `keys.py:68` |
| phases | `ACTION` · `ACCOUNTING_BOUNDARY` | `keys.py:70-71` |

Note for §4: three of the five `ROLES` members — `subject`, `object`, `witness` — are words the
design also binds to other meanings. These are live enum members that raise on violation
(`keys.py:406-410`).

### 1.2 The records

- **`Key`** (`keys.py:138-174`): `id: str` (:143) · `type: str` (:144) · `emitted_at: EmittedAt`
  (:145) · `source_actor: str|None` (:146) · `causes: list[key_id]` (:147) · `targets: list[Target]`
  (:148) · `scale_signature: list[str]` (:149) · `symbolic_dimensions: dict` (:150) ·
  `visibility: Visibility` (:151) · `time_horizon` (:152) · `permanence` (:153) · `payload: dict`
  (:154). `cascade_depth` is deliberately NOT a field (SSI-4, :139-141) — scheduler-internal, never
  logged.
- **`Target`** (`keys.py:87-105`): `actor_id` · `role` (one of ROLES) · `impact_vector:
  axis→signed magnitude` (:96) · `stat_deltas: stat_name→delta` (:97). Wide fan-out is ONE Key with
  N targets; targets[] width never increments cascade depth (:89-92).
- **`Visibility`** (`keys.py:108-121`): `public: bool` + two observer lists; exactly one of three
  shapes (invariant 8).
- **`EmittedAt`** (`keys.py:124-134`): `season_index` caller-supplied; `sub_step_index` assigned by
  the log at append (SSI-1 append order).

### 1.3 The id rule and the type registry

Type ids match `[a-z_]+\.[a-z_]+` — `family.type` — enforced structurally by the markdown heading
regex (`keys.py:177`) and re-enforced on the JSON path (`keys.py:250-254`) so the two loaders cannot
disagree. **The roster is ONE roster with two representations**: authored in
`key_type_registry_v30.md`, cooked to `engine/engine_params/key_types.json` by
`tools/export_key_types.py` (ED-IN-0136), pinned identical by a blocking round-trip gate plus
`test_key_substrate.py::test_json_and_markdown_registries_are_identical` (`keys.py:12-18,199-202`).
55 types, `type_count` self-checked at load (`keys.py:261-264`). Per-type required payload fields
are validated at append (`keys.py:308-320`); per-type defaults applied at emit (`keys.py:322-334`).
Key **instance** ids are plain strings with no shape constraint — the shape rule governs type ids
only.

### 1.4 The invariants, exactly as enforced (`KeyLog._validate`, `keys.py:378-434`)

1. **id unique across the log** — duplicate raises (:380-382).
2. **type registered + payload contract satisfied** — unknown type or missing required field raises
   (:305-306, :383).
3. **referential integrity on `causes[]`** — a cause naming an id not already in the log raises
   (:385-389).
4. **cycle-freedom BY CONSTRUCTION** — append-only log whose `causes[]` may cite only already-logged
   Keys; no logged Key can gain an edge to a later one (:390-393). The §4.6 BFS check is subsumed.
5. **season ordering** — non-decreasing `season_index` (:395-398).
6. **canonical axes** on `symbolic_dimensions` and every `impact_vector` (:399-405); **canonical
   roles** on every target (:406-410).
7. **`scale_signature` non-empty and canonical** (:411-418).
8. **exactly one visibility shape** (:419-430). Plus closed `time_horizon`/`permanence` (:431-434).
9. *(candidate, WARN-tier, deliberately not raised)* — `stat_deltas` key names resolve against an
   optional `stat_vocabulary` (OPT-AV-16, `keys.py:436-451`); unresolved names collect into
   `stat_vocabulary_warnings`.

### 1.5 The log and the hash

`KeyLog` is append-only; `lookup(key_id)` is first-class (:364-365); `serialize()` is canonical
sorted-key JSON, one line per Key in log order (:453-457); `content_hash()` is SHA-256 of that
(:459-460) — two identical runs produce byte-identical logs, and this hash is what
`tools/m1_acceptance.py` row 2 compares (CLAUDE.md §0.2).

### 1.6 The scheduler

`TickScheduler` (`keys.py:463-601`): both termination caps are REQUIRED constructor arguments with
no default (OF-CAP is an open fork — no fabricated constant, :30-33, :471-473); `emit` at depth 0;
`schedule_emission` at parent+1 (B1 — synchronous re-entry raises under the default-ON `no_sync_reentry`
flag, :518-523); `drain_tick` FIFO; OF-7 `defer_apply` default ON queues settlement-locus effects to
`accounting_boundary()` while the Key logs live; `next_tick()` raises on an undrained queue (:598-599).
Phases: `ACTION` → `ACCOUNTING_BOUNDARY`, and **`engine/autoload/engine_clock.py` owns the composition
SEASON_TICK → ACTION → ACCOUNTING_BOUNDARY** (engine_clock.py:7-8, CANONICAL per propagation_spec
§O.1, module landed ED-IN-0199, 2026-08-27).

### 1.7 What it already guarantees — stated plainly

Deterministic, hash-comparable, append-only event history with per-record identity, uniqueness,
referential integrity, structural cycle-freedom, typed payload contracts behind an exporter-gated
55-type roster, a 5-role target vocabulary, a 4-scale signature, a 3-shape visibility model, and a
guarded emission scheduler with re-entrancy and volume caps. **Every identity gap the KEYS_AUDIT
found in the design (no ids, no uniqueness, no integrity, cycles, no lookup) has a working answer
here, and the compendium's §12 correctly says so.** What it does NOT provide: persistent carriers
(no Person/Settlement record lives here), typed relationships between carriers, or any hierarchy
over the three registries — which is exactly ED-IN-0200's finding.

---

## 2. ⭐ THE KEY NAMESPACE, AUTHORITATIVE

### 2.1 The bound names

**The roster is `engine/engine_params/key_types.json`: 55 types, 6 families** — `da` 5 ·
`env` 4 · `mechanical` 12 · `meta` 6 · `scene` 18 · `state` 10. **47 of the 55 appear in
`module_contracts.yaml` flows; 8 are registry-only** (registered, no declared consumer/emitter row):
`mechanical.era_transition`, `mechanical.second_calamity`, `mechanical.settlement_captured`,
`mechanical.theocracy_unification_declared`, `meta.cascade_cluster_event`, `meta.legacy_event`,
`scene.accord_echo`, `state.settlement_revolt`. One wildcard consumer row `*` exists
(`fieldwork_knots`, `articulation_layer` — the Memory Query API edge, `module_contracts.yaml:561`).
Do not cite "48" as the roster (that is 47 flow types + `*`); the roster is 55.

The 47 flow-bound types, emitter → consumer (parsed, this session):

| type | emitted by | consumed by |
|---|---|---|
| da.antinomian_action | domain_actions | faction_state, npc_behavior, piety_track |
| da.covert_betrayal | domain_actions | faction_state, npc_behavior, piety_track |
| da.diplomatic_alliance | domain_actions | faction_state |
| da.economic_intervention | domain_actions | faction_state, settlement_economy |
| da.public_governance | domain_actions | faction_state, npc_behavior |
| env.crisis | peninsular_strain, scenario_authoring | — |
| env.disaster | peninsular_strain, scenario_authoring | faction_state, settlement_layer |
| env.peninsular_strain_shock | peninsular_strain | faction_state, npc_behavior, settlement_layer |
| env.population_change | peninsular_strain, settlement_layer | faction_state, settlement_economy |
| mechanical.accounting | engine_clock | faction_state |
| mechanical.cascade_resolution | faction_state | faction_state, npc_behavior |
| mechanical.mission_shift | faction_state | faction_state, npc_behavior |
| mechanical.project_advanced | npc_behavior | npc_behavior |
| mechanical.scene_entered | scene_slate, game_director | scene_timer, audit |
| mechanical.scene_exited | game_director | scene_timer, audit |
| mechanical.scene_skipped | game_director | scene_timer, audit |
| mechanical.season_change | engine_clock | — |
| meta.knot_formed | fieldwork_knots | npc_behavior |
| meta.knot_ruptured | fieldwork_knots | npc_behavior, piety_track |
| meta.miraculous_event | miraculous_event | faction_state, npc_behavior |
| meta.thread_woven | threadwork | npc_behavior, piety_track |
| scene.battle_concluded | mass_battle | faction_state, npc_behavior, piety_track |
| scene.combat_felled | personal_combat | faction_state, npc_behavior |
| scene.combat_hit | personal_combat | personal_combat |
| scene.combat_resolved | personal_combat | faction_state, npc_behavior |
| scene.combat_strike | scene_slate | personal_combat |
| scene.contest_resolved | social_contest | faction_state, npc_behavior |
| scene.dialogue | npc_behavior, scene_slate, social_contest | faction_state, npc_behavior, piety_track |
| scene.displacement | npc_behavior | npc_behavior |
| scene.draft_da | domain_actions | npc_behavior |
| scene.gift | fieldwork_knots, scene_slate | faction_state, npc_behavior |
| scene.gossip | npc_behavior | npc_memory |
| scene.insult | scene_slate, social_contest | faction_state, npc_behavior, piety_track |
| scene.interaction | npc_behavior | npc_memory |
| scene.investigation_resolved | scene_slate, faction_politics | faction_state, npc_behavior |
| scene.thread_operation | threadwork | npc_behavior |
| scene.threat | scene_slate, social_contest | faction_state, npc_behavior, piety_track |
| scene.witness | npc_behavior, scene_slate | npc_behavior, piety_track |
| state.belief_revised | npc_behavior, fieldwork_knots | npc_behavior |
| state.concern_resolved | npc_behavior | npc_memory |
| state.coup_attempted | faction_politics | faction_state, npc_behavior |
| state.opinion_revised | npc_behavior | npc_memory, social_contest |
| state.project_completed | npc_behavior | npc_behavior |
| state.project_failed | npc_behavior | npc_behavior |
| state.scar_acquired | piety_track | faction_state, npc_behavior |
| state.standing_change | faction_state, faction_politics | faction_state, npc_behavior |
| state.succession | faction_politics | faction_state, npc_behavior |

Adjacent bound namespaces that share the surface: the 27 module names (bare snake_case:
`faction_state, npc_behavior, npc_memory, piety_track, territorial_piety, threadwork,
fieldwork_knots, scene_slate, game_director, scene_timer, audit, social_contest, mass_battle,
domain_actions, peninsular_strain, settlement_layer, settlement_economy, ci_political, victory,
engine_clock, faction_politics, miraculous_event, scenario_authoring, articulation_layer,
clock_registry, personal_combat, campaign_architecture`), their 6-value `resolver:` enum
(`deterministic_accounting · dice_pool · state_reader · manifest · d_sigma · clock_advance`), 27
`composition_roles`, and the dotted descriptor keys (`attr.body.strength` …, `fac.*`, `set.*`,
per `references/descriptor_registry.yaml:45-172`).

### 2.2 THE NAMING SCHEME — ruled

The rule set, made mechanical (a reader can test any new name against it):

1. **Key/event types: `family.type`, lowercase snake, regex `[a-z_]+\.[a-z_]+`.** UNCHANGED — this
   is the one namespace in the tree measured as working (median 24 bare hits vs 131 for bare
   contract names, `canonical_nomenclature_v1.md:85-93`), and it is already regex-enforced in
   mechanism (`keys.py:177,250-254`). New families are an edit to the authored registry + re-cook,
   never an inline invention. Test: does `TypeRegistry.load_json` accept it? Then it is a legal id.
2. **Quantities and owned state: dotted owner-first ids per `canonical_nomenclature_v1.md` §3.1's
   grammar** (`<namespace>.<leaf>`, namespaces and leaves spelled out, no bare ambiguous-English
   leaf, one concept one id) — ADOPTED, see §6. Every quantity a Key's `stat_deltas` names must
   resolve in this namespace (that is what the substrate's candidate invariant 9 already checks,
   `keys.py:436-451`).
3. **Record/carrier types: Capitalized singular nouns** (`Person`, `Rung`, `Office`, `Site`,
   `Tenure`, `Claim`, `Record`, `Event`…), each with a row in `references/names_index.yaml`
   (schema at `names_index.yaml:19-32`) carrying `context:` terms when the word collides with
   ordinary English — the field exists precisely for that (`names_index.yaml:30-32`).
4. **Enum members and kinds: lowercase, and NEVER bare in an export.** In prose, always
   record-qualified (`Tenure.kind = hold`); in any YAML/JSON an exporter emits, the path must carry
   the record (`tenure.kind`, never a bare `kind:` at a level where two record types coexist —
   `descriptor_registry.yaml:16-19`'s `KIND:` enum and `module_contracts.yaml:171-178`'s
   `kind: value` field are the two live collisions this rule exists to not-widen).
5. **Loop steps, write classes, substrate phases: UPPERCASE words, never letter-number tokens.**
   The compendium's §0.2 ruling ("the loop steps have no letter-number names, permanently") is
   UPHELD — it closed the worst self-inflicted collision in the corpus (B1/M1).
6. **The casing IS the namespace test**: dotted-lowercase = a registry id · Capitalized = a record
   type · lowercase = a field/kind/verb (must be qualified) · UPPERCASE = a step/class/phase.
   A name that cannot be classified by its casing is not a legal new name.

**Hierarchy**: the namespace is two-axis, not one tree — `family.type` for events (what happened),
owner-dotted for state (what is), per canonical_nomenclature §2's ruling-shaped recommendation.
`scale` stays a Key field over the closed 4-member enum; `tier`/containment is data, not a scale
member (adopting greenfield `00_INDEX.md:213-227`'s `scale ⟂ tier` split, which routes around
ED-IN-0103 without foreclosing it).

---

## 3. ⭐ ED-IN-0200, EXECUTED AS A RULING

### 3.1 The ruling, quoted

`registers/editorial_ledger_in.jsonl:56` — ED-IN-0200, 2026-08-27, `status: open`,
`needs_jordan: false`, confidence high:

> "'KEY CONTRACTS AND MODULE CONTRACTS ETC NEED TO BE EXPLICITLY DEFINED IN A CENTRALIZED
> HIERARCHICAL MANNER' (Jordan, this session) — RULED, NOT EXECUTED, AND LOGGED LATE. […] Three
> registries exist and none of them is hierarchically related to the others:
> references/module_contracts.yaml (27 modules + 27 composition_roles, with each module's Key IN ->
> resolver -> OUT and owned state), engine/engine_params/key_types.json (55 key types, cooked from
> key_type_registry_v30.md behind a blocking exporter), and references/descriptor_registry.yaml
> (attributes, aggregates, faction/settlement stats and their bounds). They are three FLAT
> namespaces that reference each other by string. There is no single surface from which a reader —
> or the Godot port — can descend from 'the game' to a subsystem to a module to its Keys to the
> fields those Keys carry. WHY IT IS NOT DONE HERE […]: it is a genuine architecture job, not a
> re-siting. It needs a decision about what the hierarchy's LEVELS are (scale? subsystem? module?
> Key?), whether the existing three registries become views of one artifact or stay separate with a
> declared parent, and what the exporter/round-trip story is for the composite. Faking it by
> nesting the current three files under a new top-level key would produce a hierarchy in shape and
> not in meaning, which is worse than the honest flat state because it would look done. […]
> RELATED AND DELIBERATELY SEPARATE: the wrapper/orchestrator architecture Jordan described in the
> same conversation (each subsystem has a wrapper handling all Key I/O; inputs trickle down with
> increasing granularity, outputs aggregate up) is the RUNTIME half of the same idea."

(Citations in the row: ED-1051, ED-SC-0032. Full text verified against the ledger this session.)

### 3.2 The reconciliation the situation demands, stated first

**There are not one but TWO merged, unexecuted answers to this ruling, and they do not cite each
other.** (a) The greenfield suite v2 (PR #340, 2026-08-29) cites ED-IN-0200 explicitly and executes
its SHAPE: `GAME → SCALE ⟂ TIER → SUBSYSTEM (one wrapper owning all Key I/O) → MODULE → {STATE,
FORM, KEYS, REMIT, VIEW}` (`proposals/2026-08-29-greenfield-systems-suite-v2/00_INDEX.md:185-208`),
with a contract shape extending module_contracts schema-2 (`:376-381`) — and it also names the
wrapper clause of the ruling. (b) The ideal-v2 suite (PR #342-#344, 2026-08-31) never cites
ED-IN-0200 anywhere (grep of `proposals/2026-08-31-ideal*` returns zero hits — verified), yet its
compendium §1–§5 IS a hierarchical contracts register over a different ontology
(Person/Rung/Office/Site/Tenure). PR #341 adversarially found the greenfield suite's throughlines
zero-SUPPORTED/two-BLOCKED/seven-PARTIAL. Neither suite ratified on merge; neither runs. The
ontology choice between them escalates (§9.1); **the hierarchy specification below is deliberately
ontology-neutral so ED-IN-0200's structural half is discharged either way.**

### 3.3 The centralized hierarchical definition — the specification

**Levels** (answering the ruling's own first question):

```
GAME
└── SUBSYSTEM            = the lane (the 9-code roster CLAUDE.md §4 already owns: MB PC FI SC FA WR IN GO SE
    │                      is the *process* lane set; the *game* subsystem set is module_contracts'
    │                      grouping) — one wrapper per subsystem owns all Key I/O (the ruling's runtime half;
    │                      ED-SC-0032's BandExtension seam is the one built instance)
    └── MODULE           = one row of module_contracts.yaml: Key IN → resolver → OUT + owned state
        ├── KEYS         = type ids FROM key_types.json, by reference — never restated
        │   └── FIELDS   = each type's required/optional payload fields, owned by key_type_registry_v30.md
        │                  and readable in the cooked JSON (already true today)
        └── STATE        = dotted descriptor keys FROM descriptor_registry.yaml / the quantity
                           namespace of §2.2 rule 2, by reference — never restated
SCALE  = a Key field over the closed 4-member enum (keys.py:65), NOT a hierarchy level
TIER   = containment, data-declared (greenfield's ⟂ split), NOT a hierarchy level
```

**The composite artifact**: `module_contracts.yaml` schema 3 — each module row gains `subsystem:`
(the parent edge) and its `consumes`/`emits`/`state` entries become **validated references** into
the other two registries. The three files STAY SEPARATE WITH A DECLARED PARENT (the ruling's second
question, answered): key_types.json and descriptor_registry.yaml are already single-owned and
exporter- or CI-gated; merging them into one file would re-home two working surfaces to fix a
linkage problem. What is missing is not a super-file but a **resolver + gate**.

**The exporter/round-trip story** (the ruling's third question): one new tool,
`tools/export_contract_tree.py --build|--check`, that (i) loads all three registries, (ii) fails on
any string in a `consumes`/`emits` row absent from key_types.json (today that check would PASS —
verified: flow-types ⊆ registry, §2.1), (iii) fails on any `state:` name absent from the quantity
namespace, (iv) emits `engine/engine_params/contract_tree.json` for the Godot port to ingest, and
(v) runs `--check` as a blocking gate, the same pattern as `export_key_types.py`. **Readers**: the
Godot port (the surface ED-IN-0200 names), `engine/substrate/composition.py` (role resolution —
already reads `module_contracts.yaml` by role), and the substrate's `stat_vocabulary` hook
(`keys.py:436-451`), which becomes the runtime enforcement of level STATE the moment a caller
passes the exported quantity roster to `KeyLog`.

**What this does NOT fake**: the ruling's own warning stands — 9 of 27 modules carry `doc: null`
and 11 of 27 resolvers are `[ASSUMPTION]`-grade (verified counts, R4 §5 / my parse), so the tree
centralizes holes as much as content until those contracts are authored. The gate must therefore
report `doc: null` and `[ASSUMPTION]` per row rather than hiding them. **Under §0.2 this ruling is
DONE only when `--check` runs green in CI and the port (or `composition.py`) reads the export** —
this specification is the design of that mechanism, not its execution, and ED-IN-0200 stays `open`
until the tool exists.

---

## 4. ⭐ THE COMPLETED COLLISION REGISTER

A meaning in running code outranks a meaning in prose. **Mechanical** = the disambiguation is
enforced or enforceable by a regex/enum/schema; **convention** = someone must remember it.

| word | every meaning (path:line) | ruled form | mechanical? |
|---|---|---|---|
| **`hold`** — SIX | ① Tenure kind (compendium §2.2) ② Proposition mood `HOLDS` (§2.4) ③ predicate form `HOLDS(person, office\|holding\|mark)` (§2.7, `03:68`) ④ coercion quantity ("force and hold never in a precondition", ABS:287) ⑤ **LIVE CODE, missed by the design: mass-battle tactical stance** — `systems/mass_battle/sim/config.py:269` `STANCE_SPEED_MOD = {"…","hold": -99,…}`, `:280` `STANCE_COMMITMENT`, `:359` `PC_SHOCK_HOLD_BRACE`, consumed `units.py:1416,1701`, `resolution.py:196`, `engine.py:387` ⑥ process sense HELD/"held for Jordan" (`tests/valoria/test_degree_ladder_single_owner.py:19,155`, `HANDOFF_IN.md`) | ①`Tenure(kind=hold)` / "a hold-edge" ② `mood = HOLDS` ③ `HOLDS(p, x)` with arguments ④ unused in the suite, and the §9.13 refusal is about the QUANTITY (ruled in ARCH §9.11 — upheld) ⑤ **the stance member is mass-battle-local; any export placing Tenure kinds and stance members in one namespace must emit `tenure.hold` vs `stance.hold`** ⑥ HELD is process vocabulary, uppercase, never a game term | ①-④ convention; ⑤ mechanical once §2.2 rule 4 binds exporters; ⑥ convention |
| **`stance`** — FIVE, **entirely missing from the design's register** | ① design `Person.stance = map[referent → (valence, weight, provenance)]` (compendium §2.1, ABS:73) ② **LIVE: mass-battle unit stance** `{aggressive, balanced, hold, retreat}` — `config.py:269`, field slot `units.py:298`, branch `units.py:1416` ③ **LIVE: NPE per-issue opinion scalar 1–5** — `systems/world/sim/npe.py:150,165,339,377-393` (drifts every accounting pass; "NPE stance drift" runs in every seeded campaign) ④ the closed "stance referent kinds" set (§2.7) ⑤ `stanceweight` in salience (§4.4) | ① is the record; **at execution time it must ABSORB or be reconciled with ③ — the NPE stance is the live prototype of the same concept (an opinion held per subject) and two co-existing stores would be the §0.1 pt 1 read/write-asymmetry hazard by construction**. Prose: "unit stance" (②), "NPE stance" (③), `Person.stance` (①). ② keeps its word — it is live and local | convention now; mechanical only when ①/③ merge under one owner |
| **`witness`** — FIVE, **missing from the design's register** | ① **LIVE: Key Target role** — `keys.py:62` `ROLES = ("subject","object","witness",…)`, enforced `:406-410` ② **registered Key type `scene.witness`** — `module_contracts.yaml:306,329,429,630` ③ the design's function `witness : (Person, Event) -> Claim[]` (§4.1) ④ the WITNESS loop step (§4.2) ⑤ prose "witnessed by someone holding it higher" (advancement gate, §4.4) | ④ UPPERCASE. ③ always with its signature or parentheses `witness()`. ① "the witness role". ② its dotted id. **Declare the congruence once: the design's `witness()` is the per-person consumption of a Key whose `targets[]` row carries `role: witness` — same concept, two layers, and the design must say so rather than appear to coin it** | casing + dotted ids make ①②④ mechanical; ③⑤ convention |
| **`strike`** — THREE, **missing from the register** | ① fault severity `strike` — "kills the ground at every venue for everyone" (§2.7, SUP:1536-1542) ② **LIVE: `scene.combat_strike` Key type + `combat.strike` PORTED module** — `module_contracts.yaml:624,1318,1343`; `godot/skeleton` strike module ③ ordinary verb | ① never exported bare: `fault.strike` if it ever enters a registry; prose "struck at the venue". ② already dotted — safe | ② mechanical already; ① mechanical under §2.2 rule 4 |
| **`envelope`** — THREE, missing | ① design demographic `Envelope` (§2.6) ② **LIVE comment/model vocabulary: weapon reach envelope** — `units.py:2175,2218`, `geometry.py:582`; plus "envelopment" as an MB manoeuvre (ED-MB-0039) ③ process "ED-911 envelope" (`systems/combat/__init__.py:5`) | ① Capitalized + names_index row; ②③ descriptive prose, unqualified is acceptable — no identifier collision found | convention; low risk |
| **`subject`** — FIVE | `Tenure.subject` · `Claim.subject` · `Proposition.subject` · `subject_id` (substream) · **LIVE Key Target role `keys.py:62`** (the design cites `:65` — line drift, see §8) | always record-qualified; bare `subject` never used (design ruling UPHELD, extended: an exporter may never emit a field literally named `subject` adjacent to a Target role value) | prose convention; export rule mechanical |
| **`object`** — FOUR | `Tenure.object` · `touch.target` (renamed, breaking the collision — upheld) · generic English · **LIVE Key Target role `keys.py:62`** (dropped from the compendium row; KEYS_AUDIT D.2 had it) | design ruling upheld + the role sense restored to the register | as above |
| **`kind`** — NINE | `Rung.kind` · `Tenure.kind` · mark kind · need kind · stance-referent kind · `Record.kind` · `MatterKind` · **LIVE: `descriptor_registry.yaml:16-19` `KIND:` taxonomy enum (14 values)** · **LIVE: `module_contracts.yaml:171-178` `kind: value` field** | prose: always record-qualified (upheld). **Exports: never a bare `kind:` YAML key where two record types coexist — `tenure_kind:` / nested paths** (R4's finding, adopted as a rule) | mechanical under §2.2 rule 4 |
| **`condition`** — THREE | `condition(site)∈[0,1]` · `ConveningCondition` · stasis "named condition" | design ruling upheld (argument-carrying scalar; full type name; "a named condition"). No additional live-code binding found (R4 §6, spot-checked) | convention |
| **`View`/`view`** — THREE | ① the type passed to `choose` ② the function → **renamed `assemble`** (upheld) ③ **the engine-atlas documentation lens** — `systems/_architecture/engine_atlas_v1.md:33` (verified) | ② rename upheld; ③ always "atlas View"; ① "the View record". Third sense added to the register | convention |
| **`presence`** — FOUR | ① Query `presence(prop, c)` — a weighted sum ② "deposits by presence" ③ `enforcer_presence` ④ **legacy Core Attribute `Presence`, now an alias of Charisma** — `references/descriptor_registry.yaml:58`, `references/glossary.md:61` (verified); dozens of legacy formula citations | ① always with arguments; ② "by presence"; ④ **the alias row must never be deleted while formulas cite it; prose citing the attribute writes "Presence (legacy alias of Charisma)"**. Fourth sense added | ④ mechanically protected by the alias machinery + `ci_names_consistency` |
| **`act`/`Act`** — FOUR | the record `Act` · `remit.acts` closed five · currency ("his season's act") · **LIVE: the substrate `ACTION` phase** (`keys.py:70`, `engine_clock.py:7-8`) and the design's ACTS write class naming the same slot | design's three rulings upheld; **ACTS-vs-ACTION: the design's write class and the live phase must be declared as one thing or explicitly mapped before execution — see §7/§9** | convention + the §3 mapping |
| **`matter`** | `Rung.matter` field · MATTER step/class · "matter events" · English verb | upheld: step UPPERCASE, field record-qualified | convention |
| **`root`** | graph root Rung · root token (provenance) · conferral_path root · repo-process "root" (R4) | upheld: "the root Rung" / "root token"; process sense unqualified is fine | convention |
| **`degree`** — FOUR | commitment degree 0–5 · degree-of-success band · knot depth · **LIVE: `dice_engine.degree_from_net` + `sigma_leverage.degree`** (`dice_engine.py:227-252`) | upheld ("commitment degree" / "degree band") **with one sharpening: "degree band" MEANS the ruled four-band margin ladder owned by `degree_from_net`, and nothing else — see §8.6** | the ladder is mechanically single-owned (ED-SC-0031/0032) |
| **`stake`** / **`address`** / **`magnitude`** / **`standard`** | as the design's register (§7) — verified, no further live senses (`impact_vector` magnitude at `keys.py:96` confirmed) | upheld | convention |
| **`commit`** — THREE | Tenure kind · `commit(+Δ)` operation · git commit | upheld: declared-acceptable | convention |
| **`Derived`** | design's retired category vs **LIVE stored values** — `glossary.md:65-82`, `params_tables.yaml`, `descriptor_registry.yaml:284` (all three verified) | rename to `Query` upheld; necessary, not cosmetic | closed by rename |
| **`Query`** | the adopted category · "Memory Query API" (`module_contracts.yaml:561`, substrate §4.4) | congruent senses (both = read-only ask); ADOPTED, no conflict | — |
| **`Container`/`Node`** | Godot built-ins; stale classes `godot_architecture_specification.md:381,402` | `Rung` upheld | closed by rename |
| **`HOLDS`** | folded into `hold` row ① — the four-way ruling upheld | — | — |
| **`payload`** — NEW row | **LIVE: `Key.payload`** (`keys.py:154`) · `Tenure.payload?` · `Act.payload` (⛔ untyped, G-11) | congruent (typed extension record in all three) — declare the congruence; no rename | — |
| **`ledger`** — NEW row | game: `Person.ledger` (claims) · process: the editorial ledgers (`registers/editorial_ledger*.jsonl`) | process always "editorial ledger"; game "a person's ledger" — cross-session idempotency guard | convention |
| **`census`** — NEW row | CENSUS loop step · English "census" in live comments (`dice_engine.py:46`, tests) | UPPERCASE step; English use unqualified acceptable | casing |
| **`Claim`** | the design record · false friend "Baralta Crown Claim" (`module_contracts.yaml:1182`) | one disambiguating note where the design's Claim first ships into the corpus | convention |
| **`B1`/`M1`…** | loop barriers (retired) vs review finding ids vs `M1` the milestone | **words-only loop steps, permanently — UPHELD**, the register's best ruling | mechanical (no token shape overlap remains) |
| **`Event`** | design record `Event := (id, kind, subject, changes[], emitted_at)` · the live Key event substrate (`mechanical.*`, `scene.*` … types) | **RULED: the design's `Event` IS the Key.** Both carry `id`, `emitted_at`, `payload`; `Event.kind ↦ Key.type` (family.type), `Event.subject ↦ targets[]`, `changes[] ↦ payload`/`stat_deltas`. Building a second event record beside a ratified, running one would violate §8's every-rule-lives-once invariant. G-12 ("Event's record is defined nowhere") is thereby CLOSED: it is defined at `keys.py:138-174` | mechanical — the record exists and validates |

**Verdict on the design's register**: right method, wrong closure claim. Its §7 footer — *"After
this section, no term in §1–§5 is used in more than one sense"* — is false: `stance`, `witness`,
`strike`, `envelope`, `payload` are used in §1–§5 and have unregistered second meanings, three of
them in running code. The register is now finished as above.

---

## 5. THE NAMING RULES, AUTHORITATIVE

CLAUDE.md §4's two tests applied; "defined in CODE" = the site §4 itself prescribes
(`names_index.yaml` row with `context:`; registry enum; exporter output; docstring at the call
site).

| term | coined or ordinary? | idempotent? | idiomatic? | RULED name | must be defined in code at |
|---|---|---|---|---|---|
| **`Rung`** | ordinary word, novel binding | pass | pass (`SUP:337`'s own gloss "Container (a rung)") | **ADOPTED.** One correction: "collides with nothing anywhere" is overstated — English ladder metaphors occur in process prose (`ci_checks_registry.yaml:44,69,484`; R-2's "rung module" in SUP). No BOUND sense collides | `names_index.yaml` row, `category: substrate`, `context: [containment, carrier]` |
| **`Query`** | ordinary | pass | pass | **ADOPTED** (replacing `Derived` — repo-verified opposite sense). Congruent with the live "Memory Query API" | names_index row; the R-1 definition cited as its `context` |
| **`Tenure`** | ordinary word, stretched binding | fail (right for `hold`, wrong for the other six) | fail (calling a friendship a Tenure is not supplied by usage) | **KEPT, against both tests, with the compendium's mandatory qualifier** ("`Tenure` is the record; lowercase `tenure` in prose means the duration of a hold"). Reasoning: §4's worked failure is TWO words for ONE thing; a third rename (Holding→Tenure→Edge) would manufacture exactly that across ~12k merged lines, and `Edge` itself is graph-vocabulary-loaded in this tree. The qualifier must live in a names_index `context:` row, or this ruling flips to `Edge` — a §4-failing word without its code-side definition is not kept | names_index row with `context: [edge, relation, hold]`; the record's future dataclass docstring |
| **`Sensation`** | ordinary | pass | pass | **KEPT AND BOUND** (upheld): "`Sensation` is the record; `needs` are what it reports; only two of four reach it." Zero repo collisions (verified) | names_index row; the binding sentence in the future record's docstring |
| **`mint` / `alter` / `efface`** | `mint` ordinary-but-double-bound; `alter` ordinary; `efface` coined-feeling | `mint` FAILS (root-token sense at SUP:245 + live token sense at `systems/factions/sim/parliamentary_transfer.py:207`); `efface` passes barely | `mint` passes; `efface` FAILS (English: rub out, near-reflexive — not "destroy") | **OVERTURNED: the StateChange modes are `create · alter · destroy`.** §4 is a Jordan ruling and it is explicit: *"Coin nothing that a plain word already covers."* The design's own gloss supplies the plain words ("building, founding, establishment, birth" — KEYS_AUDIT D.1.1), nothing executes yet so the rename window is free, and it retires two §4 failures at once. `mint` is thereby reserved EXCLUSIVELY for root tokens (`witness` mints a token) — its one live sense. `efface`'s target restriction carries over verbatim: **`destroy` may never target a Claim in another person's ledger** | the mode enum in the future `StateChange` code + names_index rows; until then, an amendment row in the compendium §2.7 |
| **`Site`** | ordinary | pass | pass | **ADOPTED.** No live identifier collision (no `Site`/`site_id` in `engine/`+`systems/` python — verified). Must be registered before it meets `descriptor_registry`'s `settlement`/`territory` domains, which are its nearest neighbours | names_index row; a `domain:` decision in descriptor_registry when Site state ships |
| **`Office`** | ordinary | pass | pass | **ADOPTED** — no Godot builtin, no repo binding | names_index row |
| **`Claim`** | ordinary | pass | pass | **ADOPTED** with the Baralta false-friend note (§4) | names_index row with `context: [ledger, belief, source]` |
| **`View`** | ordinary | pass (with the case rule) | pass | **KEPT for the type; the function is `assemble`** (upheld); "atlas View" qualifier for the third sense | names_index row |
| **`Act`** | ordinary | pass with qualifiers | pass | **KEPT**, capitalised record; the ACTS write class must reconcile with the live `ACTION` phase (§7, §9) | names_index; the write-class enum when the loop is coded |
| **`Event`** | ordinary | — | — | **RULED: not a new type — it is the Key** (§4, last row). The design word survives as prose for "a Key consumed as a happening" | already defined: `keys.py:138` |
| **six loop-step words** (CALENDAR · MATTER · DELIBERATE · RESOLVE · WITNESS · CENSUS) | ordinary | pass as UPPERCASE tokens | pass | **ADOPTED as names**, with two riders: (i) RESOLVE vs the live `resolver:` registry field, WITNESS vs the live role/type (§4) — the uppercase-only rule carries the weight; (ii) **the composition itself is NOT adopted by naming it**: `engine_clock.py` owns SEASON_TICK → ACTION → ACCOUNTING_BOUNDARY (CANONICAL, ED-IN-0199), so the six steps must be declared as a refinement of that composition (CALENDAR/MATTER before ACTION; DELIBERATE+RESOLVE inside ACTION; WITNESS/CENSUS at ACCOUNTING_BOUNDARY) or as a ruled replacement — in `engine_clock.py`, not in prose | `engine_clock.py` docstring + phase constants when built |
| **`HOLDS(p, x)` predicate form** | ordinary word, formal binding | pass with the arguments rule | pass | **ADOPTED**: the mood is `mood = HOLDS`; the form always carries arguments; the Tenure kind is `Tenure(kind=hold)` (§4 row 1) | the predicate-form enum when the claim system is coded; until then compendium §2.7 |
| **`oblige`** / **`leaders`** / **`Place`** | ordinary | pass | pass | ADOPTED (leaders over principals: four live senses of "principals" incl. `_identifier_census.yaml:3371` — verified reasoning upheld) | names_index rows |

---

## 6. `canonical_nomenclature_v1.md` JUDGED

**Its scheme, reproduced** (`proposals/canonical_nomenclature_v1.md`): the dotted namespace already
exists (113 keys in `names_index.yaml`) but was never adopted — measured 2026-08-11: 16/51
non-proper-noun keys appear nowhere outside the registries, 32 only in tooling, **3 in real code or
live design docs** (`:33-53`), with the falsifier for the measurement stated (`:55-59`). Grep noise
is measured (Order 1,630 hits; Authority 1,366; contract names median 131 bare occurrences, zero
qualified) and the **Key types are the control group: dotted by construction, median 24, never a
complaint** (`:85-93`). Three live axes contradict (kind/category vs event-domain vs owner/scale,
`:96-113`); recommendation: **two-axis grammar — axis C (owner/scale) for entities and owned state,
axis B (event-domain) retained unchanged for Key types, axis A retired** (`:115-127`). Grammar
rules ×5 (`:135-164`): spell out namespaces and leaves; no bare ambiguous-English leaf; the dotted
id is the access path; one concept one id. Phasing: rulings → registry+instruments (report-only) →
migrate registries → adopt per-lane → flip blocking (`:264-314`). Known blocker: the rename
executor `tools/valoria_rename.py` silently covers a fraction of the tree (`:229-260`). Status:
PROPOSED, deliberately no ED allocated (`:10-15`).

**RULED: it PARTLY SOLVES the collision problem, and it is ADOPTED rather than duplicated.**

- What it solves — and the design needs: identifier-level ambiguity. Every "exporter must qualify"
  ruling in §4 (bare `kind:`, `tenure.hold` vs `stance.hold`, `subject` vs the Target role) is an
  instance of its grammar; its Phase-1 `namespace_registry.yaml` + report-only checker is the
  correct code-side home for §5's names_index obligations. Its control-group argument (the Key-type
  namespace works because it is dotted) is the strongest empirical naming result in the tree.
- What it does not solve: prose-sense collisions (nothing about `hold`'s six senses is an
  identifier problem), record-type naming (Person/Rung/Tenure casing), loop-step vocabulary, and
  the reconciliation of competing stores (`stance`). Those are §4/§5's territory.
- It is NOT superseded: nothing later replaces it; the ideal-v2 compendium §6 explicitly mirrors
  `names_index.yaml`'s row shape "so a later migration is transcription" (`03_COMPENDIUM.md:638`),
  which is compatibility with this plan in all but citation. The two must cite each other.
- Residual: its Phase 0 rulings are still Jordan's where they are design calls (§9.3); its §2 axis
  recommendation is hereby treated as the working answer (test 5 — the architecture-obvious call),
  subject to Jordan's veto at Phase 0.

---

## 7. THE CLOSED SETS — enumerated and adjudicated

"Genuinely closed" = the set is complete by argument or mechanism; "fenced-open" = someone wrote a
fence around an open set and it will grow.

| set | members | count | verdict |
|---|---|---|---|
| StateChange modes | create · alter · destroy (renamed §5) | 3 | **GENUINELY CLOSED** — a complete create/update/delete partition of "change" |
| change drivers | Act · Event(=Key) | 2 | **CLOSED by Jordan's partition ruling** (subject decides which is legal) |
| **Tenure kinds** | hold · commit · contain · succeed · tie · knot · oblige | 7 | **FENCED-OPEN.** The design itself grew it 6→7 in one revision (oblige). Rule: closed-at-version, extension by registry row + names_index entry, never by prose |
| write classes | CALENDAR · MATTER · ACTS · INTERIOR | 4 | closed, **conditional on the ACTS↔ACTION reconciliation** (§5) |
| loop steps | CALENDAR · MATTER · DELIBERATE · RESOLVE · WITNESS · CENSUS | 6 | closed as names; the composition is owned by `engine_clock.py` (§5) |
| stance referent kinds | Person · Proposition · Place(=Rung\|Site) | 3 | closed but **fragile** — Office was excluded by argument, not mechanism; the moment someone needs an attitude toward an institution-as-such the fence moves. Watch item, not a defect |
| owner table | Person · Rung · Office · Nobody | 4 | closed; the strongest structural ruling in the suite |
| `remit.acts` | issue · determine · confer/revoke · dispatch · convene | 5 | genuinely closed (it is a gate list, not the act vocabulary — the design's own correction, upheld) |
| act verb vocabulary | open | — | **CORRECTLY DECLARED OPEN** ("the resolver never branches on it") — the one open set the design fences honestly |
| `binds` | members-by-admission · persons-by-presence | 2 | closed |
| containment ladder | Person→Hearth→Community→Settlement→Territory→Province→Realm | 7, "extensible" | **fenced-open by its own label** — fine, it is data (TIER, §3.3) |
| **degree bands** | compendium: Disaster(≤−2)·Failure(−1)·Costed Success(0)·Clean(+1,+2)·Overwhelming(≥+3) | 5 | **OVERRULED AS STATED.** The live single owner is `dice_engine.degree_from_net` (`dice_engine.py:227-252`): margin ≥3 Overwhelming · ≥1 Success · [0,1) Partial · <0 Failure — FOUR bands, Jordan-ruled 2026-08-14, migrated to single ownership ED-SC-0031/0032. See §8.6 |
| dispensation terms | Price·Prohibition·Levy·Exemption·EntryStandard·Excommunication·Blockade·TreatyClause·Ordenanza | 9 | fenced-open (a taxonomy of legal instruments will grow); closed-at-version |
| stasis ladder | Denial·Definition·Quality·Jurisdiction | 4 | genuinely closed (ordered, strongest-first, complete by construction of the argument model) |
| the twelve faults + severities | 12 faults; strike·descend·close | 12 / 3 | closed-at-version; severities genuinely closed; `strike` naming per §4 |
| proposition moods | HOLDS · OUGHT | 2 | genuinely closed (is/ought) |
| need kinds | subsistence·standing (world) · commitment·exposure (view) | 4 | genuinely closed with the two-two split — the Sensation binding (§5) is what keeps it closed |
| larder bands | Provisioned→Sufficient→Thin→Hungry→Failing | 5 | closed-at-version (band tables are tuning surfaces) |
| commitment ladder | 0–5 with weights | 6 | closed; its licence column is a G-26 open ruling — the SET is closed, its semantics are not |
| avowal | avowed · private · covert | 3 | genuinely closed (the design's own repair of a boolean-narrowed enum — upheld) |
| mark kinds / legibility | 6 / open·attested·latent | 6 / 3 | closed-at-version / genuinely closed |
| resolution strata | 5, ordered | 5 | closed |
| fidelities | played · witnessed · auto | 3 | genuinely closed ("differ only in who is asked to choose") |
| carrier choices upward | forward·amend·bundle·drop | 4 | genuinely closed (exhaustive over a docket item) |
| channels for the office-less | 5 | 5 | fenced-open (a design inventory, not a partition) |
| decider-free exceptions | 4 | 4 | closed by the partition ruling; each maps to the Event driver |
| individuation / person-generation triggers | 4 / 5, "exhaustive", RULED | 4 / 5 | closed by ruling |
| de-individuation predicate | 4 conjunctive clauses | 4 | genuinely closed (it is a refcount) |
| knot rupture triggers | 6 | 6 | fenced-open (trigger inventories grow) |
| force forms | seize·restrain·strike·burn·expel·disperse·kill | 7 | fenced-open; `strike` naming per §4 |
| **predicate forms** | 14, enumerated `03:66-79` | 14 | closed-at-version **with a stated membership test for a 15th** — the best-governed fence in the suite; upheld |
| **Claim source constructors** | firsthand · told_by(person\|record) · inferred · firsthand_via_knot | 4 | **GENUINELY CLOSED**, and proven so: the attempted fifth (`documented`) was shown to be a reinvention of `told_by(record,…)` and withdrawn. The record-as-speaker reading is the closure argument |
| investigative acts | examine·interview·research·surveil·reconstruct·Thread-Read | 6 | closed-at-version |
| deception deltas | sincere·lie·overclaim·false witness·invention | 5 | genuinely closed (a delta taxonomy over one act) |
| visibility | open · discreet · concealed | 3 | genuinely closed |
| channel dispositions | approve · suppress · surface | 3 | genuinely closed |
| empty-view ladder | 4, ordered | 4 | closed |
| the thirteen Convictions | 13 incl. Virtue | 13 | **CLOSED AND MECHANIZED** — the only set here already enforced in running code (`descriptor_registry.yaml:235-251`; unknown names raise via `descriptors.resolve_conviction`). This is what "closed" should mean everywhere |
| substrate enums (AXES/ROLES/SCALES/…) | §1.1 | 4/5/4/3/3 | **CLOSED AND MECHANIZED** (`keys.py:399-434` raises) |
| MatterKind | authored, never effaced | open | **correctly OPEN** — world-authoring data |

The pattern to enforce: a set is closed when code raises on a non-member (Convictions, substrate
enums, TN7) — every "closed" set above that matters at runtime should graduate to that standard via
the §3.3 export; until then its closure is prose.

---

## 8. WHAT I OVERTURN

1. **Compendium §7's closure claim** — *"After this section, no term in §1–§5 is used in more than
   one sense"* (`03_COMPENDIUM.md:678-679`) — **FALSE.** `stance`, `witness`, `strike`,
   `envelope`, `payload` are used in §1–§5 with unregistered second meanings; `stance` and
   `witness` and `strike` collide with running code (§4).
2. **Compendium §7 `hold` row's sufficiency** — it records four senses and rules them; the fifth
   (mass-battle stance, live at `config.py:269`) and sixth (HELD) are absent. The row's rulings
   survive; the row was not finished.
3. **"`Rung` collides with nothing anywhere"** (`03_COMPENDIUM.md:645`) — overstated. No bound
   sense collides; the English ladder metaphor is live in process prose (`ci_checks_registry.yaml:44`
   et al.) and in SUP's own "rung module" (R-2). Downgrade to "no bound sense collides".
4. **Compendium §6.1's KEEP verdicts on `mint` and `efface`** — overturned to `create`/`destroy`
   (§5). CLAUDE.md §4 outranks the design's continuity preference, and the design's own evidence
   (four plain-word glosses; the live token sense of `mint`) argues against itself. Cost: a prose
   sweep over the unexecuted suite; benefit: two §4 failures retired before any code binds them.
5. **`presence` and `View` rows as shipped** — each missing a live third sense (attribute alias at
   `descriptor_registry.yaml:58`; atlas lens at `engine_atlas_v1.md:33`). Completed in §4.
6. **The compendium's five-band degree ladder presented as "SHIPPED"** (`03_COMPENDIUM.md:326`,
   §4.4 "degrees" row). The ruled, code-owned ladder is FOUR bands
   (`dice_engine.degree_from_net`, Jordan 2026-08-14, single-owner ED-SC-0031). A design line may
   PROPOSE a five-band ladder, but under §0.05 it may not restate one as shipped without naming the
   live ruling it would overwrite — and its demotion gate keys on "Disaster", a band the ruled
   ladder does not have. The compendium's §12 warns about `params_tables.yaml`'s stale ladder while
   omitting that its own §2.7 table conflicts with the live one. Flagged, not silently harmonized:
   changing bands is Jordan's, but citing the design's bands as current would be wrong today.
7. **The suite's implied novelty against the ledger** — the ideal-v2 line cites neither ED-IN-0200
   nor ED-IN-0201 (grep-verified zero hits) while the rival merged suite cites and "executes" both
   (`greenfield-v2/00_INDEX.md:187,288-292`). The compendium's §12 precedent table reaches for
   `keys.py` but not for the two rulings that are its own charter. Not a naming defect — a
   provenance defect in the governing register of a naming-obsessed suite.
8. **Line-drift in the compendium's substrate citations** — `keys.py:65` for the Target roles
   (actual: `:62`; `:65` is SCALES), `keys.py:145` for `Key.id` (actual: `:143`), §12's
   `:379-381/:384-388/:389-392/:363-365` each off by ~1 (actual `:380-382/:385-389/:390-393/
   :364-365`). Substance correct; cite today's lines.
9. **KEYS_AUDIT D.1's recommendation to rename `Tenure` → `Edge`** — overturned in favour of the
   compendium's keep-with-qualifier, WITH the added teeth that the qualifier must land in
   `names_index.yaml` or the ruling flips (§5). One of the two documents had to lose; the cheaper
   loss is the audit's.
10. **Any citation of "48 key types"** from module-contract flow counts — the roster is 55; 47 are
    flow-bound; 8 registry-only (§2.1). Two counts of one roster must not circulate as two rosters.

---

## 9. WHAT ESCALATES TO JORDAN

Applying §0's five tests in order; everything below survived superseded/irrelevant/design-doc/
precedent/architecture.

1. **Which merged design line is the execution vehicle for ED-IN-0200/0201's ontology** —
   greenfield-v2's Entity/Tag/Post/Gauge + GAME→SUBSYSTEM→MODULE hierarchy (cites both rulings;
   adversarially rated zero-SUPPORTED by PR #341) vs ideal-v2's Person/Rung/Office/Site/Tenure
   (never cites either; later; carries its own uncleared verdicts). Two defensible architectures,
   materially different games, both merged PROPOSED three days apart. §3.3's hierarchy spec is
   ontology-neutral precisely so this is the only part that must wait. *(Not answerable by tests
   1–5: no later ruling, both live, docs conflict, no precedent, and architecture arguments cut
   both ways.)*
2. **The degree-band conflict as a design question** (§8.6): does Jordan want a Disaster band and a
   Costed-Success band added to the ruled four-band ladder? The current answer in mechanism is no;
   the design proposes yes; only Jordan can move a 2026-08-14 ruling.
3. **`piety_track`'s owner** (settlement vs territory vs character) — three docs disagree
   independently of any naming scheme (`canonical_nomenclature_v1.md:211-215`); blocks that
   proposal's Phase 0. A live design choice, not an engineering default.
4. **F6 / G-30 — is the world dying or misunderstood** — carried by the design as the one fork
   where "the code is identical either way"; the in-flux/`wear` ruling answered the mechanism, not
   the fork. Still genuinely Jordan's.
5. **"No commander, no battle": gate reading (a) vs penalty reading (b)** — ED-IN-0201's own
   recorded ambiguity; two different games; carried open in the ledger, re-surfaced here because
   the Person-carrier design will force it at execution.

**Deliberately NOT escalated** (answered under test 5, recorded): `leaders`' comparator — adopt
`commitment degree × backing raisable` (REV:772-778) as the provisional engineering answer, tag it
revisable (G-04 closes to "provisionally ruled"); the mint/efface rename (answered by §4, test 3);
the Tenure name (test 5); the ACTS↔ACTION mapping (test 4 — precedent: `engine_clock` owns
composition, ED-IN-0199); the tenth attribute's name (already queued to Jordan elsewhere — not
re-flagged).

---

## 10. CONFIDENCE

| ruling | confidence | what would raise it |
|---|---|---|
| §1 substrate reproduction | **HIGH** — read the code in full, line-cited | running `pytest tests/valoria/test_key_substrate.py` (read-only session; not run) |
| §2 key-namespace table (55/47/8, emitter/consumer map) | **HIGH** — parsed programmatically this session | a CI gate pinning flow⊆registry (the §3.3 exporter's check iii) |
| §2.2 naming scheme | **HIGH** on rules 1, 4–6 (they codify live mechanism); **MEDIUM** on rule 2 (adopts a PROPOSED plan whose Phase 0 is unruled) | Jordan's Phase 0 sitting |
| §3 ED-IN-0200 discharge | **HIGH** on the quotation and the measured state; **MEDIUM** on the specification (a design, unexecuted by definition — §0.2) | `export_contract_tree.py --check` green in CI |
| §4 collision register | **HIGH** on every live-code sense (grepped, path:line); **MEDIUM** on "no further senses exist" claims — greps covered `engine/ systems/ references/ tools/ tests/`, not `canon/`+`research/` prose exhaustively | a whole-tree token census per word (the `canonical_nomenclature` Phase-1 instrument) |
| §5 mint/efface → create/destroy overturn | **MEDIUM** — the §4 argument is strong, but it edits a Jordan-merged head's vocabulary; if Jordan prefers continuity, the fallback is the compendium's keep-with-qualifiers, which is defensible | one line from Jordan |
| §5 Tenure kept | **MEDIUM** — judgment call against a §4 double-fail, on churn-cost grounds | the names_index row landing (the condition of the ruling) |
| §6 canonical_nomenclature adoption | **HIGH** that it partly solves and should be adopted, not duplicated | its Phase 0 rulings |
| §7 closed-set verdicts | **HIGH** for mechanized sets; **MEDIUM** for closed-at-version calls (predictions about growth) | graduating each set to raise-on-non-member |
| §8 overturns | **HIGH** for 1–3, 5, 6, 8, 10 (each verified against the tree); **MEDIUM** for 4, 9 (judgment) | — |
| §9 escalation list | **HIGH** that these five survive the five tests | — |
