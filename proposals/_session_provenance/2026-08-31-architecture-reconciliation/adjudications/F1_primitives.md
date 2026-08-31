# F1 — ADJUDICATION: the primitive set and the ownership model

Adjudicator: Fable 5, read-only pass over `/home/user/ttrpg` at 2026-08-31. Nothing in the four
proposals executes; every "the design says" below is a claim about reference prose (CLAUDE.md §0.05),
never about behaviour. Where I say a thing RUNS, I cite the code and the golden that observes it.

---

## 0. METHOD, and what I verified with my own eyes vs took from a log

**Read in full:** trace logs PR339, PR340 (all sections), PR342, PR343 (§3, §11, §13), PR344 (all),
R1, R2, R4. **Verified directly against the working tree (my own greps/reads, not the logs'):**

1. `grep -rn "compute_observers|memory_query|MemoryIndex|compute_salience|memory.record" --include=*.py
   engine/ systems/ tools/ tests/` → **exactly one hit**, `engine/substrate/__init__.py:18`, inside a
   docstring that says *"implementing compute_observers() before [ORD-3] lands would bake in
   hash-order nondeterminism"* — i.e. the one code mention is an explicit statement of
   NON-implementation. The same identifiers appear as pseudocode in
   `systems/_architecture/key_substrate_v30.md:195-314` and four other design docs.
2. `grep -rn "class Person|class Tenure|class Rung|class Office\b|class Site\b|class StateChange|def
   choose(|def witness(" --include=*.py engine/ systems/` → zero carrier/edge/StateChange/choose/witness
   definitions. (`def resolve` hits are bespoke per-subsystem resolvers: `combat_bridge.py:131`,
   `combat_engine_v1/core.py:98`, `social_contest/sim/contest/resolver.py` — seven distinct signatures.)
3. `engine/substrate/keys.py` read directly: `class Key` at :138, `id: str` at :143, `lookup()` at
   :364, invariant 1 (id uniqueness) :379-381, invariant 3 (referential integrity of `causes[]`)
   :384-388, invariant 4 (cycle-freedom by construction) :390-392, `class KeyLog` :336,
   `class TickScheduler` present. Header docstring (:1-46) states §4.1 steps 3-4 (observer/witness)
   are **deliberately NOT implemented**, blocked on unratified ORD-3.
4. `engine/mc_v18.py:66-75`: `ECHO_TRANSPORT` **default ON** (Jordan ratification; env default `'1'`);
   `engine/cross_scale/parliamentary_bridge.py:5` — *"Activates the Key & Echo transport in the LIVE
   campaign loop"*; `engine/tests/test_parliamentary_bridge.py:35,70,85,105,120,148` pins
   `_ON_KEYLOG_HASH` values and `keys_emitted 13 → 75 → 187 → 169` across golden re-pins. **Keys are
   emitted, validated, and content-hashed in every default seeded campaign.** (One nuance verified at
   `engine/cross_scale/echo_transport.py:14-42`: the §5.2 domain-echo leg is WIRED but DORMANT — no
   live scene ctx carries an `echo` block — while the parliamentary leg is live.)
5. `references/module_contracts.yaml` parsed with `yaml.safe_load`: 27 modules; `doc: null` on exactly
   9 (audit, domain_actions, engine_clock, game_director, npc_memory, scenario_authoring, scene_slate,
   scene_timer, settlement_economy); `resolver:` is a six-value strategy enum
   (`clock_advance, d_sigma, deterministic_accounting, dice_pool, manifest, state_reader` + one None)
   — a label, not a typed signature. `npc_memory` is `doc: null`, `resolver: state_reader`, no code.
6. `engine/autoload/game_state.py`: `class Faction` :110 (stored aggregate stats, `adjust()` :153),
   `class Territory` :234, `class World` :256-301 (14 Any-typed schema-migration registries + settlements;
   comment: element classes live in `systems/`, engine never defines them). No leader field on Faction.
7. `proposals/2026-08-31-ideal-v2/01_ARCHITECTURE.md` §2 read in full (:139-538, :640-719): carriers,
   id rule, Tenure table with per-kind cardinality, the Partition (Jordan verbatim), Query rename,
   §2.7 Faction deletion + amended four-owner table, §3.1a GDScript purity downgrade.
8. `proposals/2026-08-31-ideal/10_SUPERSEDING.md` §4.2 (:330-345): the FIVE-row table with the Faction
   row, verbatim; §6 seven-phase/three-write-class structure (:647-677).
9. `systems/settlements/scale_hierarchy_v1.md` :9-39 (Province existence-conditional), :81-95
   (§5.1 "factions hold people, not territory") — both verbatim as R2 quoted.
   `systems/_architecture/holonic_container_doctrine_v1.md` :15-45 — "one uniform canonical shape at
   every scale" is about CODE MODULE shape, confirmed by its own cross-map table.
10. `key_substrate_v30.md:1-2` carries **two conflicting status lines**: line 1
    `[CANONICAL: 2026-05-01 — PP-687 …]`, line 2 `STATUS: PROVISIONAL — Class A canonical document;
    ratification by Jordan or designated authority required for promotion.` Noted in §8.
11. `03_COMPENDIUM.md` section map and §3.4/§12 spot-reads; `04_GODOT_IMPLEMENTABILITY.md`
    RefCounted/cycle passages (:69-80, :100-124, :223-254).

**Taken from logs without independent re-derivation** (each marked where used): PR339/PR340's 21-of-22
verified repo-claims tables; R4's ledger line-counts and `hold`-stance citation
(`systems/mass_battle/sim/config.py:269` — spot-trusted, R4 quotes the literal dict); PR343's diff
accounting. The Godot cycle-collector fact I verified from engineering knowledge: Godot 4's
`RefCounted` is pure reference counting with no cycle collector; reference cycles leak (Godot's own
docs recommend `WeakRef`). The claim in `01_ARCHITECTURE.md:228-243` is engineering-true.

---

## 1. ⭐ THE R1/R2 CONFLICT, RULED

**R1's claim, precisely:** zero of ~22 proposed design objects exist as named first-class types in
`engine/`; no edge type exists at all; no uniform `choose`/`resolve`/`witness` signatures exist
(27 bespoke resolver signatures); therefore "greenfield territory, not a refactor."

**R2's claim, precisely:** the proposal's Event/StateChange/witness/Claim/Query cluster "is already
CANONICAL **and executable** as the Key substrate" — `compute_observers()` + `memory.record()` =
witness, `memory_query()` = Query, `causes[]` = provenance — and `resolve : (Act[], World) -> Event[]`
"is already wired via `module_contracts.yaml`'s fixed Key IN→resolver→OUT shape."

**RULING: both are half right, and the halves are cleanly separable at one line of code.**

**Is the Key substrate already the design's Event/Claim/Query mechanism?**
- **Event: YES, in substance.** `Key` (`keys.py:138`) is an executable, canonical (ED-IN-0018/0026,
  ratified 2026-07-07), append-only, id-unique, referentially-checked, cycle-free-by-construction,
  content-hashed event record with `causes[]` provenance — and it RUNS: default-ON in every seeded
  campaign (`mc_v18.py:75`), goldens pin its hash and emission count
  (`test_parliamentary_bridge.py:70-148`). Calling this "greenfield territory" is false.
- **Claim/witness/Query: NO, as mechanism.** `compute_observers`, `memory.record`, `memory_query`,
  `MemoryIndex` exist **only as pseudocode** in `key_substrate_v30.md:195-314`. The executable
  substrate's own docstring (`engine/substrate/__init__.py:16-20`, `keys.py:9-11`) says observer
  resolution is deliberately unimplemented, blocked on ORD-3. Under CLAUDE.md §0.05, a design doc may
  not be cited as the reason a behaviour exists. **R2's word "executable" is overturned for exactly
  this half.** R2 conflated document status (CANONICAL — itself muddied, see §8.5) with execution.
- **`resolve` "already wired": NO.** `module_contracts.yaml`'s `resolver:` field is a six-value
  strategy *label* (verified by parse, §0.5); `composition.json`'s 27 roles have seven-plus mutually
  incompatible callable signatures (verified, §0.2). A declared consumes/emits edge list is a shape
  precedent, not a signature. R1 is correct here, exactly as stated.

**Is the authoritative architecture a greenfield build or a refactor onto `engine/substrate/`?**

**Neither word survives. It is a GREENFIELD CARRIER-AND-EDGE LAYER COMPOSED ON TOP OF A KEPT,
EXECUTING SUBSTRATE.** Precisely:
- **KEPT and composed upon** (never re-implemented — CLAUDE.md §0's bottom-up rule): the event
  record + log + invariants + id/lookup machinery (`keys.py`), the determinism discipline
  (seeded RNG, `content_hash`, derived substreams), the role-resolution seam (`composition.py`),
  the registry-bounds pattern (`descriptors.py`), the degree ladder (`dice_engine.degree_from_net`,
  single owner, TN7 ruled), the flag-gated-parallel-build cutover pattern (ECHO_TRANSPORT /
  DISPATCH_COMBAT_BRIDGE precedent). `01_ARCHITECTURE.md` §2.2 and `03_COMPENDIUM.md` §12 already
  rule this way ("the precedent to copy rather than re-derive") — I confirm it.
- **GREENFIELD** (zero code exists; verified §0.2): Person/Rung/Office/Site carriers, the Tenure
  edge, StateChange with the Partition, the per-person claim ledger + witness fan-out, Sensation/View,
  the six-step loop (current `engine_clock.run_tick` is three-phase), and the uniform three
  signatures. The current strategic layer (`Faction`/`Territory` stored aggregates, ~31 `.adjust()`
  writer sites) is not a base to refactor — it is the thing the design's refusal rows 5/6 forbid, so
  the path is the repo's established one: build beside it flag-gated, golden-controlled, cut over.

**Ground:** §0 items 1-5 above — every load-bearing fact re-verified against the tree this session.
**Falsifier:** my ruling is wrong if (a) any `.py` file in the tree defines
`compute_observers`/`memory_query`/a per-person claim ledger that executes — the grep in §0.1 would
have found it and found only the not-implemented docstring; or (b) the Key substrate were dormant in
default campaigns — refuted by `mc_v18.py:75` (default ON) and the pinned `keys_emitted`/hash goldens.

**What this ruling costs:** R1's headline sentence ("greenfield, not a refactor") can no longer be
quoted whole, and R2's headline ("already canonical and executable") can no longer be quoted at all.
Both logs' *bodies* were more careful than their summaries — R1 §9.2 itself says the design's Event
primitives "would likely want to sit ON TOP of this substrate."

---

## 2. THE FOUR PRIMITIVE SETS, COMPARED

| object | #339 (archived) | #340 (v2 suite) | #342/#343 (SUP) | #344 (head) | engine/ actually has | verdict |
|---|---|---|---|---|---|---|
| identity carrier | Entity (5 kinds) | Entity (6 kinds, +form bucket) | Person only | Person (weight≥1) + Rung + Office + Site | `Faction`/`Territory`/`World` stat-bags (`game_state.py:110,234,256`); **no individual actor** | Entity: **superseded**. Person: **survives** (weight absorbs cohort) |
| relationship/edge | `edge` Entity kind (6 relations) + Tag families | edge container, PP-724 kinds + 3 extensions | containment tree + alignment map (2 relations, not reified) | **Tenure** (one edge, 7 kinds, per-kind cardinality) | **nothing** — `Faction.territories` list :124, `world.treaties`, `Settlement.governor_id`, `world.knots` — five unkinded shapes | Tenure: **survives as the unifier**; #340's per-kind-semantics rule survives inside it |
| durable memory | Tag (5 kinds) | Tag (7 kinds incl. Holding, Ambition) | per-person Claim ledger | Claim ledger (closed 4 sources, 14 predicate forms) | **nothing** (`world.beliefs` dict slot; `Belief` class in `systems/characters/sim/beliefs.py:50`) | Tag: **superseded by Claim+stance+Tenure**; Holding's epistemic content survives as Claim vocabulary |
| office/post | Post (6 kinds, budget Gauge) | Post (same) | Office (9 fields incl. `seat_items`) | Office (`seat_items` deleted, `revocation` kept) + `hold` Tenure | **nothing** (`Faction.parliamentary: bool` :112 is the nearest gesture) | Post: **renamed/reshaped → Office**; vacancy-as-first-class **survives** from #339 |
| continuous value | Gauge (geometric decay, no setter) | Gauge (same) | refused (no stored aggregate; scheduled recovery refused) | refused (refusal rows 5/6/12); primary state only on Site.condition/stores as **fixed-point integers**; decay only on matter/bodies/claim-confidence | `Faction.L/Sta/W/…` ARE stored gauges with writers | Gauge: **superseded by refusal**; its decay law survives narrowly in claim-confidence/recency |
| state change | one-write rule, 3 leaves | 4 leaves (+form transition) | 3 write classes, 7 phases | **StateChange := (subject, mode∈mint\|alter\|efface, driver∈Act\|Event)**, 4 write classes, 6 steps/4 barriers | direct field mutation (`.adjust()`), plus OF-7 deferred-apply through Keys for echo writes | StateChange: **survives**; #339/#340's "write leaf" idea is its ancestor; OF-7 is its executable precedent |
| event record | 7 proposed key types (blocked on P0-1) | same discipline | Event (resolve output, unreified) | Event := (id, kind, subject, changes[], emitted_at) | **`Key` — executable, 55 types, running** (`keys.py:138`) | **never was greenfield**: compose Event onto Key (§1) |
| query | derivations (`writable:false`) | fm.derive etc. | "Nobody" owner row + R-1 | **Query** (renamed from Derived; 23-row catalogue; resolver-side takes World first) | `canon_buckets.canonical_accord`, `descriptors.faction_bounds` — Query-shaped, unnamed | Query: **survives**; rename verified necessary (three live sources use `Derived` for the opposite; R4 §3 confirmed) |
| loop | phase placement onto existing 3-phase tick | 13-phase build order | seven phases P0-P7, 3 write classes | **six steps, four barriers, four write classes** | `engine_clock.run_tick` 3 phases (`SEASON_TICK→ACTION→ACCOUNTING_BOUNDARY`) | #344's loop **survives**; #343's P-labels retired by its own namespace rule |
| faction | Entity kind | Entity kind + bloc + ethos | 5th owner row (proposition + commitment map) | **deleted as carrier** — Proposition + commit Tenures, fully derived | `Faction` dataclass with stored stats | deletion **survives** (see §4) |
| attention/salience | — (root cause D of archive) | **the Slate** (binds ratified Light Function, ED-IN-0011) | — | **absent** (view assembly only) | `scene_slate.py` deque (59 LOC, different animal) | **never superseded — the head's largest uncited hole**; see §9 |
| actorless world channel | — (root cause E) | `11_world_events.md` (registry-row events, `hazard_pool`) | — | MATTER-barrier events under the Partition (mechanism only, no content schema) | nothing | #340's **content schema survives as the composition target** for #344's mechanism |

Never-existed anywhere in code, any set: Rung, Tenure, StateChange, Sensation, View, choose, witness,
CALENDAR/MATTER/DELIBERATE/RESOLVE/WITNESS/CENSUS as phases.

---

## 3. ⭐ THE AUTHORITATIVE PRIMITIVE SET

**RULING: the authoritative set is #344's (`01_ARCHITECTURE.md` §2), with the four amendments below.
#339 is archived by its own adversarial pass; #343's SUP remains source-of-truth only where #344's §10
does not depart; #340 is neither authoritative nor dead — it is the content-layer quarry (§9). The set
is chosen on grounds, not recency: it is the only one of the four that (a) carries Jordan's verbatim
rulings as structure (the Partition, the containment axiom, Kingdom/Duchy-as-factions, D-2,
community+family as required rungs), (b) composes on the executing substrate by citation rather than
beside it, and (c) survived structurally-independent adversarial review (five runners, an antagonist
that broke four of its parent review's claims, and two Jordan ontology corrections).**

The set — each primitive, its record, identity, owner, cardinality, and what composes ON TOP of it:

1. **Person** `:= (id, weight, marks, capability, stance, ledger, ties)` — weight≥1, default 1; a
   cohort IS a Person at weight>1 (one type; prevents elite-only politics by construction). Identity:
   `id = H(world_seed, tick, subject_id, purpose)`, minted at CENSUS (individuation) — never by a
   clock. Owner: itself (everything interior; every Tenure whose subject it is; its uttered
   Propositions). **Composes on top:** cohorts (weight), the player (a person holding posts, no player
   entity), NPC ambition behaviour (#340 Part-3 dossier content as stance/ledger contents, not fields).
   *Justified by:* ED-IN-0201 (ruled 2026-08-28, open, unexecuted — "all faction actions … are
   predicated upon people existing"; measured: `Faction` has no leader field, `world.npcs` empty in
   every seeded campaign). This carrier IS that ruling's execution vehicle and must cite it.
2. **Rung** `:= (id, kind, stake[], judging_set_rule, dates[], matter, envelope)` — the containment
   node. Owner: itself — matter and dates ONLY, never a social aggregate. **Composes on top:**
   Hearth/Community/Settlement/Territory/Province/Realm as *kinds*, not classes; Province's
   existence-conditionality (`scale_hierarchy_v1.md` §2, RATIFIED) becomes a Query over `hold`
   Tenures rather than a fixed tier — the ratified precedent generalized, not contradicted.
3. **Office** `:= (id, post, rung?, remit, conferral, revocation, establishment, dates[], upkeep)`.
   Owner: itself. **Composes on top:** every rank ladder in `faction_politics_v30.md` (offices +
   `hold` Tenures + advancement/demotion gates), parliament (a Date + Venue + remit `determine`).
4. **Site** `:= (id, rung, kind, condition, drawers[])` — `condition` is primary state, fixed-point
   integer, written at RESOLVE (acts) and MATTER (`wear` only). **Composes on top:** economy
   (`yield`), the verb band-gate, restoration play (F6's in-flux world). Its readmission argument
   (accumulator-reads-own-value ⇒ primary state; node-keying destroys identity) is verified sound.
5. **Tenure** `:= (id, subject, object, kind∈{hold,commit,contain,succeed,tie,knot,oblige}, since,
   until?, conferrer?, degree?, payload?)` — THE one edge; owned by its subject; object side a derived
   index; per-kind cardinality declared on the schema (see §5). **Composes on top:** factions
   (`commit`), the containment tree (`contain`), annexation/enfeoffment (`hold`), succession
   (`succeed`), the social graph (`tie`/`knot` — PP-724 semantics preserved per kind), kin obligation
   (`oblige`), entrenchment (`until?`).
6. **StateChange** `:= (subject, mode∈{mint,alter,efface}, driver∈{Act,Event}, field?, delta?, spec?)`
   under Jordan's Partition, carried in `Act := (id, actor, verb, changes[], reads[], contests[],
   payload)` and `Event := (id, kind, subject, changes[], emitted_at)`. **Composes on top of the KEPT
   substrate:** Event is the design-level face of `Key` — same id discipline, same append-only log,
   same `causes[]` provenance, same content-hash replay surface (`keys.py`, executing today). Build
   Event AS a Key type family or as Key's successor sharing `KeyLog`'s invariants; never as a second
   log. (§0.1 pt 5's load-bearing predicate: the log is load-bearing on the game — it stays.)
7. **Claim** `:= (id, subject, predicate(14 closed forms), value, when, source(4 closed constructors),
   confidence, visibility)`, per-person ledger; minted only by `witness`. **Composes on top:**
   investigation (6 acts), argument (Grounds cite claims), epistemic play, the purge-at-the-venue.
8. **Query** — never stored, always recomputed; resolver-side takes `World` first, person-side reads
   only the asker's ledger. **Composes on top:** faction, leaders, presence/density/footprint, norm,
   condition-at-a-rung, address, entrenchment, filter_share — 23 catalogued rows, replacing every
   stored aggregate. Executable precedent: `canon_buckets.canonical_accord`,
   `descriptors.faction_bounds` (verified Query-shaped, no storage).
9. **The three signatures** `choose:(Person,View,Sensation)->Act · resolve:(Act[],World)->Event[] ·
   witness:(Person,Event)->Claim[]` — with §3.1a's port-honest downgrade (unreachable-by-name, 23
   enforcement sites, not type-unwritable) already ruled into the head. **Composes on top:** the
   three deferred subsystems re-enter at RESOLVE as nested instances (the seam, §8 of the head).

**Exclusions, each justified by what already covers it:** Entity-kinds (covered by four typed
carriers — a closed kind enum on one struct was #339's own archival lesson: it froze what must grow);
Tag (covered by Claim + stance + Tenure + `until?`-as-history); Gauge (covered by Query for every
aggregate, primary state for Site/stores, and the refusal of scheduled social recovery — refusal row
12); Post-budget (covered by D-2's one-act rule + `capacity(date)`); a Faction carrier (covered by
Proposition + commit Tenures — §4); a second resolver (refusal row 8); `annex`/`secede` verbs
(covered by `confer` on `hold`; `secede` additionally collides with `05:594`'s shipped defection
sense); a fifth Claim source (covered by `research → told_by(record,…)`, the head's own withdrawal
of `documented()` — verified in `03_COMPENDIUM.md` §2.4).

**The four amendments I rule in (grounds: §0's test 5 — architecture calls with one clearly right
answer; none overwrites ratified canon):**

- **A1 — Proposition's status is stated, not fudged.** It carries an id, persists, is a Tenure
  subject/object and a stance referent, yet is "not a carrier." Rule: a **carrier** is an
  identity-bearing record with *mutable* state; a Proposition is the one identity-bearing
  **immutable** record (fixed at utterance, never effaced). Five identity-bearing kinds, four
  carriers. This is a definition the head implies and never states; without it "four carriers" is
  quotable into a false claim.
- **A2 — the Partition's membership test is a schema column, not an instance judgment.** See §6.
- **A3 — the ownership table's Person row rule ("every Tenure whose subject they are") is generalized
  to "every Tenure is owned by its subject, whichever carrier that is."** `succeed` (subject: Rung)
  and `hold` (subject: Proposition allowed) already break the Person-row phrasing; the Rung/Office
  rows never mention Tenures. One sentence closes a real seam (found by this pass; see §8.7).
- **A4 — the `hold` collision with live mass-battle code is recorded and disarmed.** See §5.

---

## 4. THE OWNERSHIP TABLE — authoritative

| state | sole owner | writers | readers | stored or recomputed | where it lives in code today |
|---|---|---|---|---|---|
| Person interior (marks, capability, stance, ledger, ties) | the Person | RESOLVE (stance, via acts); WITNESS (ledger, own only); CENSUS (mint) | `choose` (own only); resolver-side Queries | stored | **nowhere** — greenfield (nearest: `systems/world/sim/npe.py` NPC, `systems/characters/sim/beliefs.py:50`) |
| every Tenure | **its subject** (A3) | RESOLVE (`confer`/`revoke`/`commit`/mint/efface); MATTER (`until` on death only) | Queries (object side = derived inverse index, stored nowhere) | stored, append-`until`, never deleted | **nowhere** (five unkinded shapes: `game_state.py:124`, `world.treaties`, `Settlement.governor_id`, `faction_politics` ranks, `world.knots`) |
| Rung matter (`stores`, Sites, Records, transmission pointer, envelope) + dates | the Rung | MATTER (metabolism, wear); RESOLVE (transfer/levy, act deltas); CALENDAR (dates/dockets); CENSUS (envelope reconcile) | everyone via Queries | stored (fixed-point ints for stores/condition) | **nowhere** (Settlement dataclass `systems/settlements/sim/registry.py:55` is the nearest shape) |
| Office fields + its dates | the Office | RESOLVE (mint/efface/amend-remit acts); CALENDAR (dates) | Queries; `opening_set` via believed remits | stored | **nowhere** |
| Site `condition` | the Site | MATTER (`wear` only) + RESOLVE (act deltas, summed, clamped once) | `verbs(site,c)` resolver-side only | stored, primary | **nowhere** |
| Event log | the log (append-only) | RESOLVE + MATTER emit; nothing mutates | WITNESS fan-out; **no decision function may read it** | stored, append-only, hashed | **`engine/substrate/keys.py` — EXECUTING** (KeyLog, 8 invariants, `content_hash`) |
| a returned Act | its actor, for one tick | DELIBERATE only | RESOLVE | transient | nowhere |
| **Nobody** | — | *no writer may exist* | everyone, via the 23 Queries | **recomputed, never stored**: aggregates, norms, densities, needs, openings, scale, reputation, **leadership**, faction | precedent: `canon_buckets.py:35-46`, `descriptors.py:98-108`; **violated by the current engine on purpose-of-record**: `Faction.L/Sta/W/I/Mil` are stored aggregates with ~31 writer sites — the legacy layer the new one replaces behind a flag |

**The deleted Faction row — RULED CORRECT.** Grounds, in §0's test order: (3) answered by design
document — Jordan verbatim: *"Factions are only as strong as the people under their purview"*, and
the §1.2 spec requires dynamically generated/collapsing royal factions, which a lifecycle-object
faction must implement and a derived faction gets free; (4) answered by precedent —
`scale_hierarchy_v1.md` §5.1 (RATIFIED, verified verbatim): *"Factions do not necessarily need to
hold territory — they need to hold PEOPLE"* — commitment-held-on-persons is already the ratified
model, the row deletion is its logical completion. **Costs, stated:** (a) "the Dicastery decided" is
permanently inexpressible (B-11's accepted cost); (b) every faction read is a derived index over
commit Tenures — a real performance obligation on the port (the object-side index must be maintained
incrementally or recomputed; `03_COMPENDIUM.md` §5's own gap row); (c) `10_SUPERSEDING.md:339`'s
five-row table is now historical — any doc citing "the five owners" must be read as superseded by
`01_ARCHITECTURE.md` §2.7.

**"Nobody owns aggregates" — RULED CORRECT, with its edge named.** It is the design's strongest
single idea (power is a query ⇒ power is not static) and has executable precedent in this tree. The
edge: it makes the CURRENT strategic layer (stored Faction stats, pinned by goldens) structurally
non-compliant. That is not a contradiction to resolve by softening the rule — it is the migration
the repo's flag-gated pattern exists for (ECHO_TRANSPORT precedent: land parallel, byte-exact
default, ratify the flip).

---

## 5. THE EDGE — ruling on `Tenure`

**One edge with seven kinds is RIGHT, and it is the proposals' single largest genuine contribution.**
Checked kind-by-kind against what the repo already has:

| kind | existing repo mechanism it unifies | verified at | verdict |
|---|---|---|---|
| `hold` (Person→Office) | rank/office holding, prose ladders | `faction_politics_v30.md` (Standing 0-7, per-faction) | unifies five prose ladders into one record; **right** |
| `hold` (P\|Prop→Site\|Rung) | `Faction.territories: list[str]` (`game_state.py:124`); `Settlement.governor_id` FK | direct read | replaces unkinded list-membership with a disputable, dated, conferral-bearing record; **right** — this is what makes annexation witnessable |
| `commit` | **nothing stored today** (faction membership has no representation) | greps §0.2 | net-new; **right** |
| `contain` | fixed geographic parents in `scale_hierarchy_v1.md` §1 | :9-23 | reifies the ratified tree as data; cardinality 1-per-subject generalizes single-parent to Rungs (fixes the prior brief's Person-only scoping — `03_COMPENDIUM.md` §3.4); **right** |
| `succeed` | succession prose (hearth pointer) | #342 04§1.3 | **right**; needs A3 (owner = the Rung) |
| `tie` / `knot` | `world.knots` registry + `systems/fieldwork/sim/knots.py:111` (`Knot(actor_a, actor_b, strain, …)`) | R2 §5, spot-trusted | **right with a caveat**: these are affective channels, not disputable political facts — they ride Tenure for the id/claim-subject/storage machinery, and their semantics stay per-kind in `payload` (depth, strain). PP-724's anti-unification rulings (patronage≠Knot; strains never sum) forbid unifying *semantics*, not *storage* — the head complies. The weakest membership in the seven; keep, and never let a Query sum across kinds. |
| `oblige` | Ledger `Debt`/`Compact` tags (#340), `TreatyRecord` terms | `systems/factions/sim/treaty.py:62` (R2) | **right**; treaties themselves stay Dispensations with TreatyClause terms — do not force them into `oblige` |

**Per-kind cardinality as a schema-level constraint: RULED IN, emphatically.** The argument is
verified sound: without it, two `succeed` edges on one hearth are each individually legal and the
invariant breaks only after both resolve; with it, the conflict rule's third clause (two `mint`s
jointly breaking a declared cardinality) fires at RESOLVE. This also supplies the validation point
single-parent containment never had. Executable precedent for schema-carried per-field metadata:
`references/descriptor_registry.yaml`'s dotted quantity keys (`03_COMPENDIUM.md` §12, verified the
registry exists and is the sole-runtime-read pattern via `descriptors.py`).

**Not over-unified — because of two disciplines that must ship with it:** (1) `payload` is the
kind's own record (semantics per kind); (2) **A4**: the collision register must add the fifth live
sense of `hold` — `STANCE_SPEED_MOD["hold"]` in `systems/mass_battle/sim/config.py:269`, a
currently-executing tactical stance in the one adjacent subsystem most likely to interoperate with
`Tenure(kind=hold)` (R4's finding; the design's own register missed it). Disambiguation rule: the
edge kind is always written `Tenure(kind=hold)` in prose and `tenure.hold` in any exported
namespace; the bare token `hold` is never a cross-subsystem identifier.

---

## 6. THE STATE CHANGE — ruling on `mint|alter|efface` × `Act|Event` and Jordan's Partition

**The 3×2 grid: RULED CORRECT.** Mode closed at three is what keeps the verb and event-kind
vocabularies safely open (the resolver branches on `(subject, mode, field, delta)`, never on `verb`
or `kind` — refusal row 13 honored by construction). The mint-spec with pre-computable id, the
`reads[]`/`contests[]` re-siting (they are declarations, not modes — verified real work, not a
relabel: `reads[]` feeds the conflict rule, `contests[]` routes to `contest`), events-resolve-first
at their own barrier, and the sum-then-clamp-once batching over fixed-point integers (citing this
repo's own paid-for 1-ulp defect, CLAUDE.md §0.1 pt 2) are all internally consistent and
port-honest. The bottom-left cell (event-driven `mint`) is a genuine new capability none of the
three prior sets had.

**Jordan's Partition — is the partition-by-subject predicate well-formed?** As stated
("IT decides which driver is legal"), **it lacks a decision procedure for exactly one carrier, and
that carrier is the important one: Person.** A Person's body is non-social matter (ages, festers,
dies — event-driven at MATTER, and the head writes it there) while a Person's standing, commitment
and grievance are social (act-driven at RESOLVE, and the head writes them there). So the head
already *practices* a finer partition than it *states*: the partition is by **(subject-type,
field)**, not by subject-instance.

**The membership test, given precisely (amendment A2):** every record kind and every field of every
carrier carries a static schema tag `social: bool`. A StateChange is legal iff
`driver == (Act if social(subject_type, field ?? existence) else Event)`, where `existence` is the
tag for `mint`/`efface` of the whole record. Assignments: all Tenure kinds, Office.*, Proposition,
stance, ledger-reachable social predicates, and the *existence* of Rung/Office/Site-as-institution →
`social: true`; Person.body-fields, Site.condition-via-`wear`, stores-via-yield, envelope weights,
travel, weather, off-peninsular pressure, tears, and the existence of non-social matter →
`social: false`. Person.existence splits exactly as the head rules: body-death is an event (MATTER);
Person-as-record mint is individuation (CENSUS, matter class); the *social consequences* propagate
only at telling speed. The plague/settlement worked case then falls out of the table mechanically —
which is the test of well-formedness the prose version cannot pass alone. Edge subjects (famine,
heresy) decompose into their touched fields, each of which has a tag; no instance-level judgment
remains. This is §0's test 5 (an architecture call with one right answer), not an escalation.

---

## 7. IDENTITY AND IDS — ruling on `id(x) = H(world_seed, tick, subject_id, purpose)` and ids-not-pointers

**RULED CORRECT, on three verified grounds:**
1. **The executable precedent is real and exact.** `Key.id: str` (`keys.py:143`), uniqueness raised
   as invariant 1 (:379-381), referential integrity as invariant 3 (:384-388), cycle-freedom by
   construction (:390-392), first-class `lookup()` (:364). The head's instruction to copy rather
   than re-derive is the correct application of CLAUDE.md §0's bottom-up rule. (Its citations are
   off by ≤2 lines against the current tree — `:145` vs actual `:143` — substance exact; see §8.6.)
2. **No-allocator hashing closes determinism and parallelism with one mechanism.** Verified
   reasoning: a shared id counter is precisely the mutable global that would serialize the
   DELIBERATE map and re-phase every roll on any insertion (the order-independence property
   `SUP:611-613` names as invisible-when-absent). The scheme leans on one hidden coupling worth
   recording: **uniqueness within (tick, subject) rests on D-2's one-act rule plus `purpose` slot
   discipline** — if D-2 is ever relaxed, `purpose` must grow an attempt discriminator (SUP's
   original substream had one). Also unstated: the hash's width/truncation is unspecified; the port
   must pin one (full-width, cross-platform-stable — the #340 suite's own `candidate_id` discipline,
   "identical bytes on Python and GDScript," is the rule to reuse).
3. **The cycle-collector argument is engineering-true and load-bearing.** Godot 4's `RefCounted` is
   pure reference counting — no cycle collector exists; a reference cycle is a permanent leak
   (Godot's own guidance is `WeakRef`). And the design's reference graph is cyclic **by
   construction**: `succeed ∘ contain` (Rung→Person→Rung) is the *normal* case — the heir lives in
   the hearth; ties/knots are symmetric; claims cite claims; conferral paths may cycle
   (`03_COMPENDIUM.md` §3.4, verified present). Ids break every cycle at the storage layer. The
   standing note ("the first Godot-fluent reviewer will suggest precisely the edit that breaks
   this") is correct and should survive every future edit. One follow-on the compendium itself
   catches and I endorse: **every graph traversal needs a visited set** — cycle-freedom holds for
   the *event log* by append-only construction (`keys.py:390-392`), not for the Tenure graph, which
   has no such construction; and a cyclic `Office.conferral` chain silently self-excludes from its
   cluster rather than erroring — a detector belongs in load-time validation, not a runtime guard.

---

## 8. WHAT I OVERTURN

1. **R2's headline verdict** — "the proposal's Event/StateChange/witness/Claim/Query cluster is
   already CANONICAL **and executable**." The witness/Claim/Query half exists only as pseudocode
   (`key_substrate_v30.md:195-314`); the sole code reference is a NOT-implemented notice
   (`engine/substrate/__init__.py:16-20`). Overturned as to "executable"; §0.05 forbids the
   remaining "canonical prose" from being cited as mechanism.
2. **R2's "resolve is already wired via module_contracts.yaml"** — the `resolver:` field is a
   six-value strategy label (verified by parse); no uniform signature exists anywhere (verified,
   seven-plus bespoke `def resolve` shapes). Overturned as stated.
3. **R1's headline verdict** — "This is greenfield territory, not a refactor." Overturned as a
   whole-architecture claim: the Event/id/determinism substrate exists, is canonical, and EXECUTES
   in every default campaign (`mc_v18.py:75` default-ON; `test_parliamentary_bridge.py` pins
   `keys_emitted` 13→75→187→169 and four `_ON_KEYLOG_HASH` values). R1's own §9.2 contradicts its
   own summary sentence.
4. **R1's keys.py line citations** — `Key` "at keys.py:126-158" (actual class at :138, fields to
   ~:160), `KeyLog` ":319" (actual :336), invariants ":355-406" (actual :378-425). Off by 12-17
   lines throughout — the substance is right, the line numbers are not to be trusted or copied.
5. **Any unqualified "key_substrate_v30.md is CANONICAL"** (R2 and both PR-log summaries repeat it).
   The file's own header carries two conflicting status lines: `:1` `[CANONICAL: 2026-05-01 —
   PP-687 …]` and `:2` `STATUS: PROVISIONAL — Class A canonical document; ratification … required
   for promotion.` CURRENT.md lists it as head, which settles *currency*, but a doc whose own header
   disagrees with itself cannot be quoted as unambiguously ratified. Someone should reconcile the
   two lines (a one-line fix; the CANONICAL banner postdates and supersedes on its face, but §1's
   own discipline says the stale line must go, not be outvoted).
6. **`01_ARCHITECTURE.md:223`'s citation `Key.id: str at engine/substrate/keys.py:145`** — actual
   `:143`; and `:225`'s `keys.py:389-392` for cycle-freedom — actual comment at `:390-392`. Both
   ≤2 lines off: substance verified true, cite drift noted so nobody "fixes" the design against
   stale numbers.
7. **The head's ownership-table Person-row phrasing** ("every Tenure whose subject they are") stated
   as if it covered Tenure ownership generally — it doesn't: `succeed`'s subject is a Rung and one
   `hold` row admits a Proposition subject, and neither the Rung row nor any other row mentions
   Tenures. The rule the head *means* is stated once at §2.3 ("A TENURE IS OWNED BY ITS SUBJECT");
   the table must say so or the table is wrong. (Amendment A3.)
8. **#344's collision register on `hold`** — incomplete: misses the live, executing mass-battle
   stance sense (`systems/mass_battle/sim/config.py:269`, per R4 with quoted literal) and the
   process-vocabulary `HELD`/"held for Jordan" sense. (Amendment A4.)
9. **The claim, implicit in reading #344 as a clean supersession chain, that #340 is dead.** The
   head's own §12 limit 8 concedes four of its "new or missing" mechanisms were already designed in
   #340's uncited documents (world_events' actorless channel + `we.altonian_pressure`;
   ambitions_and_arcs' derived `progress`; the_act_economy's D-2 split; the_slate_and_salience).
   #340 is unarchived, PROPOSED, and partially reinvented — an unstable disposition no document
   owns. See §9.
10. **Not overturned, recorded as verified against the accused text:** the `Derived`→`Query` rename
    (three live sources confirmed by R4 at file:line, one re-verified here); the Site readmission;
    the Faction-row deletion; the cardinality-on-schema rule; the events-resolve-first barrier; the
    fixed-point-integer ruling.

---

## 9. WHAT ESCALATES TO JORDAN

Applying §0's five tests in order to every candidate this pass surfaced:

- *R1/R2 conflict* — answered here (§1). Not escalated.
- *Which primitive set governs* — answered by Jordan's own rulings + ratified precedent (tests 3/4);
  ruled in §3. Not escalated.
- *Faction-row deletion* — answered (test 3 + 4; §4). Not escalated.
- *Partition well-formedness* — answered by architecture (test 5; §6, amendment A2). Not escalated.
- *ED-IN-0200 (centralized hierarchical contracts) and ED-IN-0201 (personnel precondition), both
  open* — answered by design documents now on disk (test 3): the head's Compendium is the descent
  surface 0200 demands in embryo, and the Person carrier is 0201's execution vehicle. What remains
  is session work — cross-cite them and close the rows — not a Jordan question. Not escalated.
- *Engine migration path (stored-aggregate strategic layer vs Nobody-owns-aggregates)* — answered by
  precedent (test 4): the ECHO_TRANSPORT flag-gated parallel-build-and-ratified-flip pattern,
  byte-exact default until Jordan flips it. Not escalated.
- *`wear` : restoration ratio (F6's balance question)* — a number to measure, not a ruling to make
  (§0.2: an execution artifact, when something runs). Not escalated.
- *#340-v2 formal archival* — dispositive only after the one genuine escalation below is answered;
  the archival banner is then session work under the #339 `ARCHIVED.md` precedent. Held, not
  escalated on its own.

**ESCALATION 1 (the only one that survives all five tests): does the ratified Light Function / Slate
bind the new architecture's player surface, or is it superseded?**
- **Why it survives:** not superseded (the head names the Slate doc and expressly did not read it —
  `01_ARCHITECTURE.md:1805`: *"the general question — how does anything get put in front of a
  decider — is designed at length in `…-v2/10_the_slate_and_salience.md` … which this suite did not
  read"* — verified this session); not irrelevant (the Light Function is RATIFIED — ED-IN-0011, per
  #340's `10_the_slate_and_salience.md` which binds to it term-by-term); not answered by a design
  document (the head's View/salience machinery governs what a *character* retrieves, not what a
  *player* is shown, and it leaves the Slate's disposition explicitly open); not answered by
  precedent (the two precedents point opposite ways: #339's archival root-cause D ruled an action
  economy without an attention economy a structural failure, while #344 ships exactly that shape);
  not an obvious architecture call (both options compose cleanly).
- **The two defensible options:** (a) the Slate binds — every emission is a candidate, the ratified
  Light Function ranks what reaches the player, `#340`'s `10_*` docs are adopted as the surface
  layer over #344's substrate; (b) the head's Witness-only model is the surface — the player sees
  what their person's view assembles, full stop, and the Light Function is superseded as
  strategic-layer machinery.
- **Why materially different games:** (a) is a curated season — the engine editorializes attention,
  volume is shaped, "Ship D or do not ship the rest" (#340 §0's own warning); (b) is raw
  witnessing — undifferentiated volume reaches the player, which #339's adversarial pass called a
  structural failure (root cause D), but which maximally honors the head's no-apparatus,
  no-second-scoring-function refusals. A ruling either way silently rewrites the other's ratified
  or reviewed surface — that is exactly the §0 definition of a genuine escalation.

---

## 10. CONFIDENCE

| ruling | confidence | what would raise it |
|---|---|---|
| §1 R1/R2 ruling (Event executable; witness/Query prose-only) | **HIGH** — every leg re-verified against the tree this session | nothing needed; it is grep-falsifiable and the falsifiers are stated |
| §1 greenfield-atop-kept-substrate verdict | **HIGH** | a spike that actually emits one Event-family Key through `KeyLog` would convert it from ruling to demonstration (§0.2) |
| §3 authoritative set = #344 + A1-A4 | **MEDIUM-HIGH** — grounds are Jordan's verbatim rulings and verified precedent, but nothing has executed and §0.2 forbids calling any of it done | the four structural tests (no-world-in-choose · divergent witnessing · postless action · order independence) actually running |
| §4 Faction deletion + Nobody row | **HIGH** on grounds; **MEDIUM** on cost (derived-index performance on the port is asserted, unmeasured) | a measured index-maintenance cost at the compute budget #342 09§10 projected |
| §5 Tenure, 7 kinds, schema cardinality | **HIGH** for hold/commit/contain/succeed/oblige; **MEDIUM** for tie/knot membership (semantic fit is the weakest; PP-724 is itself Class A PROVISIONAL) | Jordan glancing at the tie/knot rows; a load-time validator draft proving cardinality is checkable from schema alone |
| §6 Partition + A2 field-level test | **MEDIUM-HIGH** — A2 is my amendment; the head practices it but never states it | the `social:` column actually written into the type catalogue and walked against the head's own worked cases |
| §7 ids + cycle argument | **HIGH** (engineering fact + verified code precedent) | pinning the hash function/width for the port |
| §8 overturns | **HIGH** for 1-6 (each is a direct observation); **MEDIUM** for 8's process-sense claim (R4's grep, spot-trusted) | re-running R4's `hold` grep myself (declined on budget; the quoted literal is specific enough to trust) |
| §9 single escalation | **HIGH** — no longer a silence inference: the head names the Slate doc as owning the reach-a-decider question and states it did not read it (`01_ARCHITECTURE.md:1805`, grep-verified across all four v2 docs) | nothing; the question is cleanly posed for Jordan as-is |

Marked `[unclear]` nowhere above; every uncertain leg carries its confidence and its lift instead.
