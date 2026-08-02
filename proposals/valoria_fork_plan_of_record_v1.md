# Valoria Fork — Plan of Record v1

## Status: ⚠️ **SUPERSEDED-PENDING-REWRITE — DO NOT EXECUTE.** PROPOSED charter, 2026-08-02, failed
## an independent read-only critic pass the same day (16 CONFIRMED-WRONG findings against 19
## survivals). It is kept in the tree as the record of what was measured and what was got wrong;
## a rewrite (r3) must replace it before any wave starts. **The ED cited below is a collision** —
## `ED-IN-0122` was already allocated and resolved for unrelated work; `id_reservations.yaml` reads
## `next_free: 123`, so the rewrite allocates **ED-IN-0123**. §0.1 of this file's own §9 rule
## applies to itself: a Class-A charter opening on an ID collision is the failure the lane scheme
## exists to prevent.
##
## WHAT SURVIVED (verified against disk by an independent reader): every recomputed graph number —
## 56 key types, 164 implied edges, 11 multi-P×multi-C types, 14/5/8 authority, 16 sibling imports,
## 253 helpers, 21 duplicated names, 12 `.tres`, 8 `.gd`, 7 canon files; §4.2's sequencing diagnosis;
## §8.3's `parliamentary_bridge` target; the `vector_audit` markdown-only and `godot/skeleton`
## non-compilable characterizations; §7.4's failure count; §2's authoring-vs-runtime reasoning.
##
## WHAT BROKE — the four that make it non-executable:
##   1. **`references/wiring_manifest.yaml` is never cited and already holds half of this plan** —
##      the per-subsystem manifest §3 proposes building, the §1 "finding that reorders everything"
##      (banked 2026-07-29), a **character-layer foundation gap**, and `save_replay_premise:
##      status: violated` — *the live strategic loop mutates World directly with no Key trace, so
##      the Key log cannot reconstruct strategic state.* That is a harder falsification of W0's
##      `key_log_hash` gate than this document's own 38%-coverage caveat, and §8 omits it.
##   2. **W0's falsifier cannot observe the failures it excludes.** It is import-scoped; the real
##      escapes are PATH LITERALS — `engine/tests/` reaches into `skills/` (DIES), `audit/`
##      (STAYS), `registers/`, and a retired `designs/` path whose load sits inside a bare
##      `except`, so a parity class **silently skips today**. §9 of this file records that exact
##      lesson; §6 then wrote the import-scoped gate anyway.
##   3. **`tests/sim/mass_battle` — 28 modules, 11,269 LOC, last advanced 2026-07-31 — is
##      unclassified** by §5. Mislabelled a frozen archive; `wiring_manifest.yaml` says "reconcile
##      before porting"; held for Jordan under ED-MB-0043.
##   4. **"14 homeless modules" is inflated to 8.** Six of the fourteen name a `doc:` in the
##      adjacent field — `mass_battle`'s row states outright that `sim_module` is empty by
##      LANE-OWNERSHIP discipline, not absence. Genuinely homeless: 8, exactly the `authority:
##      none` set. The wrapper-granularity decision in §3 rests on the inflated figure.
##
## Further confirmed and not yet folded: `orchestrator.resolve()` converts a statically visible edge
## into one W2's own AST falsifier cannot see (F6); the orchestrator as specified inverts CLAUDE.md's
## stated `acyclic — autoload is a leaf` invariant (F10); §4.3(a) grows a second interface dialect
## against the CANONICAL holonic doctrine with no supersession (F11); §4.1 proposes hand-authoring
## into a file whose header says NEVER hand-edit — the arrays are already a generated view, and the
## two-representation defect is upstream in the registry/contracts pair (F12); W2's surface is ~38
## statements, not 16 (F5); `review_core` is a dispatcher over tooling §5 deletes (F16).
##
## STRATEGIC FINDING THAT SURVIVES AND REORDERS THE WORK (§2.5, from an end-to-end pipeline trace):
## two extraction pipelines already produce **554 typed values** (`combat_engine_v1.json` 230 +
## `sim_params.json` 324), and **zero pipelines deliver a value to anything that runs** — every
## terminus is a test, a dashboard, or self-verification. `engine/params/*.md` has **zero readers**
## in `engine/` or `systems/`. So W3 is aimed wrong: the work is not converting prose, it is
## INVERTING the two existing extractions and building the missing consumer half (the cook step).
## **The repo is producer-heavy and consumer-empty; the fork's critical path is delivery.**
##
## Class: A — substrate/architecture. **The merge-ratifies-W0–W2 clause below is WITHDRAWN** while
## this document is superseded: F8/F9/F11 show it would ratify past held gates.
## Provenance: authored by an Opus-5 session from a Fable-5 read-only audit, over a day of execution-verified
## measurement. Every number carries the command that produced it. Corrections to earlier drafts are stated
## in place, not silently applied.

---

## 0. The decision this plan serves

Jordan's ruling, 2026-08-02, restated:

1. The repository is a **Python/prose project that sets up a game made in Godot**.
2. All code is structured so it is **readily portable to Godot**.
3. Game primitives / derivatives / scores are **centralized**.
4. Architecture: **core engines/resolvers · an orchestrator whose Keys manage I/O · centralized data ·
   modular subsystems · data among subsystems and between them and the orchestrator managed by Keys**.
5. **Python-first**: the engine/systems become 100% runnable in Python, *then* the port to Godot happens,
   where UI and graphics get solved.
6. Python Monte Carlo is a **modelling tool**, not the oracle.
7. **Code/tables are always authoritative over prose. Prose is canon only where no code pair exists.**
8. Data lives in tables/graphs. JSON for canon; SQLite permitted for **derived** query layers only.

This plan does not re-litigate any of the above.

---

## 1. Where the repository actually is (measured, not asserted)

| | measured | command |
|---|---|---|
| Enforcement code | 55,737 LOC (tools 23,770 · tests 24,922 · skills 7,045) | `wc -l` over each tree |
| Simulation | 29,267 LOC | `wc -l` |
| **Godot** | **539 LOC · 8 files · NO `project.godot` · no GDScript loads any data file** | `find . -name "*.gd"`, `find . -name project.godot` |
| Markdown | 423,257 lines / 1,769 files | `find`+`wc` |
| — canon that never converts | **1,055 lines / 7 files** | classified by tree |
| — research/design (the conversion backlog) | **72,105 / 280** | " |
| — process/audit (not game material) | **339,462 / 1,435 — 80%** | " |
| Campaign | `run_campaign(seed=42)` runs: Crown, 50 seasons, 29 `battle_count` | executed |
| Stubs | `stub_hits: 100` = **two** functions × 50 seasons, both honestly deferred | stubwire spy |
| Key types declared | 56 | `key_graph.json` |
| Key types **emitted** | **2** (`scene.contest_resolved` 13 · `scene.battle_concluded` 62) | `TickScheduler.emit` spy |
| Module authority | 14 code · 5 prose · **8 none** | `key_graph.json` |
| Modules with no subsystem home | **14 of 27** — incl. `engine_clock`, the temporal spine | " |

**The finding that reorders everything.** A seed-42 campaign under `coverage --source=systems,engine`
executes **38% of statements**, leaves **37 files at 0%**, and produces **zero rows for
`combat_engine_v1`** — the most complete subsystem in the repo is not exercised by the campaign at all.

> `python3 -m coverage run --source=systems,engine covrun.py && python3 -m coverage report`
> → `TOTAL 7883 stmts, 4851 missed, 38%`

The `key_log_hash` golden — the thing a fork would naturally use to prove a clean move — certifies
roughly one third of the portable surface and none of personal combat. **Any plan whose first gate is
that hash is verifying a third of what it claims.**

---

## 2. What external practice settles

**Authoring format ≠ runtime format, with a cook step between them.** The canonical content-pipeline
shape is *author → export → validate → import → cook → package → deploy*; design-time components
transform the authored form, runtime loads a compact serialized one, and **validation lives in the cook
step**. ([MonoGame](https://docs.monogame.net/articles/getting_to_know/whatis/content_pipeline/CP_Architecture.html))

This resolves the format argument. JSON authored → `.tres` cooked is not a compromise, it is the standard
shape — and the round-trip gate is not overhead, it *is* the cook step's validation stage. **The generator
and the gate are one artifact, not two.**

**SQLite belongs in the build cache, not in canon.** O3DE ships `assetdb.sqlite` inside the Asset Cache,
maintained by the Asset Processor, queried with parameter binding; studios query the database *about*
assets rather than inspecting files. ([O3DE](https://docs.o3de.org/docs/user-guide/assets/asset-processor/asset-database/))
It is a derived build artifact — not source, not shipped. That is exactly the boundary principle 8 draws,
and it is a mainstream engine's practice rather than a novel position.

**Adopt the relational discipline, not the database, as the conditioner.** Entities get primary keys;
relationships are explicit rows, not embedded arrays; a composite key means a join table. Applied to this
repo it immediately finds a real defect — see §4.1.

---

## 3. Architecture, resolved

```
             ┌────────────────────────────────────────┐
             │  ORCHESTRATOR   engine/orchestrator/   │
             │  owns: KeyBus · module registry ·      │
             │        resolver registry · state store │
             │        engine_clock (temporal spine)   │
             │  exposes: step() / run_season()        │
             └───────┬───────────────────────┬────────┘
                     │ Keys (deferred)       │ resolve() (synchronous)
        ┌────────────┴──────┐         ┌──────┴──────────┐
        │  SUBSYSTEM  ×14   │  Keys   │  SUBSYSTEM      │
        │  manifest + wrapper◄────────►  manifest+wrapper│
        │  internals private│         │                 │
        └────────┬──────────┘         └─────────────────┘
                 │ reads
        ┌────────┴──────────────────────────────────────┐
        │  CENTRALIZED DATA   data/**.json (authored)   │
        │  → cooked → .tres / typed accessors           │
        └───────────────────────────────────────────────┘

  modelling/   mc_v18 + workbench — CONSUMERS of the engine, never its oracle
```

**The orchestrator vs `mc_v18`.** The orchestrator owns the KeyBus, the registries, the state store and
the clock, and exposes `step()`/`run_season()`. It has **no concept of seeds, batches, winners or
metrics**. `mc_v18` (337 LOC) is exactly that residue and moves to `modelling/` — which is principle 6
made structural rather than declared.

**Wrapper granularity: per-subsystem (14), not per-module (27).** Each subsystem ships a manifest naming
the contract-modules it owns, the keys it emits/consumes, and its registered resolvers. Building 27
wrappers would enshrine a roster where **8 have no authority at all and 14 have no home**. CLAUDE.md §2a
already rules 1:1 subsystem↔folder↔Godot-module; per-subsystem wrappers are its executable form.

---

## 4. The four modelling decisions

### 4.1 The `edges` relation **replaces** the arrays

`key_graph.json` currently stores `producers[]` and `consumers[]` on a *type* row. That flattening
silently asserts a full cross-product: **164 implied edges from 56 types**, with 11 types having both >1
producer and >1 consumer — `scene.dialogue` alone asserts 3×4 = **12 edges nobody authored**.

```json
{"type": "scene.dialogue", "producer": "social_contest", "consumer": "npcs",
 "provenance": "code|prose|both", "cite": "ED-XX-NNNN", "status": "live|declared|assumed"}
```

Composite primary key `(type, producer, consumer)`. The per-type arrays become **generated views** —
derivable in one groupby, never hand-edited. Two representations of one truth is the single-owner
violation this repo is organised against; the migration forces someone to author or drop each of the 164,
which is the point.

### 4.2 The KeyLog owns the sequence counter

`Key.id` is composite (`type.s{season}.n{seq}`) and uniqueness *is* enforced —
`KeyLog._validate` raises on collision. But the counters are per-emitter attributes on `world`
(`_echo_key_seq`, `_battle_key_seq`): collision-freedom holds by naming accident, not by construction.

Move `seq` assignment into `KeyLog.append`, one counter per `(type, season)`. Emitters stop passing it.
This **changes the seed-42 hash**, so per §0.1 it ships with a paired-arm test proving old and new streams
are identical *except* seq assignment, and re-records the golden in the same commit.

### 4.3 The 16 cross-subsystem imports — three patterns, none survives as a bare import

- **(a) Synchronous resolver invocation** (`faction_action`→`massbattle`, cross_scale→contest/fieldwork).
  Stays a **call** — the caller needs the answer now, and Keys are deferred to the accounting boundary.
  Forcing it through the bus would be scripting the bus. It routes through
  `orchestrator.resolve("mass_battle", …)`, which removes the import edge and *is* Godot's singleton shape.
- **(b) Type imports for snapshot/restore** (`game_state`'s lazy `CoherenceState`, `NPC`, `Knot`…).
  Inverted: each subsystem **registers its serializable types** at startup.
- **(c) Central-state reads** (`accounting`→settlement/world tracks). That state is centralized data
  (principle 3); it moves under the orchestrator's store and is read from there, not from a sibling.

Keys stay reserved for the deferred notifications they already model correctly.

### 4.4 Homeless modules

`engine_clock` is **substrate, not a subsystem** — it belongs to the orchestrator, since it is the spine
`step()` runs on. `domain_actions` → `factions` (open as ED-FA-0002; **needs Jordan**). The remaining 12
are assigned to manifests in W4.

---

## 5. Migrates · stays · dies

**MIGRATES** (~33k LOC + ~73k lines of conversion-input prose)
`engine/substrate` · `engine/autoload` (refactored) · `engine/cross_scale` → orchestrator ·
`engine/tests` (the parity suite — part of W0's gate) · all `systems/*/sim` · `combat_engine_v1`
(**7,849 LOC total**, of which workbench 2,031 stays Python forever as a modelling tool) ·
`combat_engine_v1.json` + `export_engine_params.py` — **the template for all W3 data** ·
`key_graph.json` → the edges relation · `module_contracts.yaml` → subsystem manifests ·
the 7 canon files (1,055 lines) · the 280-file design backlog **as conversion inputs** ·
the behavioural subset of the 1,585 collected tests, ported to **direct imports**.

Minimal tooling: `structure_audit`'s AST import-graph core (it is W2's falsifier) · `review_core` ·
`ci_naming_check` · the fabrication gate **rebuilt full-tree** — its changeset-scoping was this
session's proven blind spot.

**STAYS** (source repo, frozen provenance archive)
`registers/` · `audit/` · `arcs/` · `workplans/` · `dashboard/` · the observability apparatus.
The fork cites back by `repo@SHA + PP/ED`.

**DIES**
339k lines of process/audit markdown — it audits a prose regime the fork abolishes ·
~11k LOC of audit tooling in current form, `vector_audit` foremost (**markdown-only by construction** —
`rglob('*.md')`) · `skills/` (re-grow on recurrence, per the existing roster rule) ·
**`godot/skeleton`** — 539 LOC extending a `KeyBus` that exists nowhere; **regenerate from working
Python at W5, do not port the sketch**.

---

## 6. Waves

| | Content | Lane | Jordan | Falsifier |
|---|---|---|---|---|
| **W0** | Fork bootstrap: pure move of `engine/` + `systems/` + parity tests, everything packaged | IN | no | seed-42 `key_log_hash` byte-identical **AND** `pytest engine/tests` green **AND** zero imports escaping the copied set. **The hash alone is insufficient — it covers 38%** |
| **W1** | KeyBus class · log-owned seq (§4.2) · edges relation (§4.1) · `battle_count` → `battles_resolved` + `attacker_victories` | IN | no | paired-arm test: streams identical modulo seq · every edge participant ∈ module roster · edge count < 164 and equals the authored count · seed-42 reports 62 battles |
| **W2** | Orchestrator inversion: registration, resolver registry, `engine/`→`systems/` imports removed | IN | ruling: `engine_clock` = orchestrator substrate | AST check asserts **zero** `systems.*` imports under `engine/` and zero sibling imports under `systems/` outside registration |
| **W3** | Data centralization: prose params → typed JSON → cooked views, round-trip CI (the cook step of §2) | per-lane | **yes** — value collisions like the triple Combat Pool definition need a ruling each | round-trip CI red on any hand-edit of a generated view · full-tree uncited-constant gate green |
| **W4** | Module homes + authority closure: 14 homeless assigned, 8 authority-none authored or explicitly DEFERRED | per-lane | **yes** — canon authorship | 0 modules `authority: none` without a DEFERRED tag · 0 unresolved prose referents · 0 homeless |
| **W5** | Godot gate: `project.godot`, Godot 4.6 headless in CI, KeyBus.gd, JSON ingestion, combat parity | GO | **yes** — the strategy doc is PROPOSED; ratify first | a CI job running `godot --headless` on a seeded Python↔GDScript parity check. **Unknowable until then — no Godot binary exists in the current environment; make no Godot-side claim before this job is green** |

---

## 7. Held for Jordan (loud — nothing here ratifies on merge)

1. **`domain_actions` home** (ED-FA-0002) — blocks W4 and one edge family.
2. **Value collisions surfaced by W3**, Combat Pool's three definitions first.
3. **The Godot conversion strategy** is PROPOSED with unexecuted Gate-0 preconditions. W5 does not start
   until it is ratified.
4. **Fork point.** 8–9 MB Track-F tests fail at HEAD. Fork from the last green ancestor, **or** carry them
   as `xfail` with an ED citation — so the fork's suite starts green *and honest*. Never silently red.

---

## 8. Where this plan is most likely wrong

1. **The seed-42 golden is a weak fidelity oracle — measured, not suspected.** 38% coverage, 37 files at
   0%, `combat_engine_v1` in zero rows. *Settling measurement:* a multi-seed coverage sweep to find the
   reachable ceiling; anything still at 0% needs its own golden before its move counts as verified.
2. **"Audit tooling dies" may discard the ratchet that kept this repo honest.** `review_core` +
   `scope_ratchet` cost ~800 LOC; the failures they prevent are silent ones. *Settling measurement:* count
   fork-applicable signals in `review_baseline.yaml` — if more than 3 survive the prose purge, carry the core.
3. **Per-subsystem wrappers may mismatch Godot's node model** for synchronous cross-scale flows like
   `parliamentary_bridge`, which spans three subsystems. Unknowable without Godot; make it the *first*
   thing W5's parity harness tests.
4. **The prose-authority flip could orphan the 5 prose-authoritative modules** if their prose encodes
   intent the code never implemented. *Settling measurement:* per-module, diff prose-declared
   emits/consumes against code before W3 converts them — the same join that found the 55-declared /
   2-emitted gap.

---

## 9. Method note, carried forward deliberately

Every significant error in the session that produced this plan was a **false absence derived from a
proxy**: "not wired" (it was wired four ways), "no such guard" (it existed), "zero schema files",
mutation coverage reported as 0 → 3 → 8 as the scan widened, lane coverage 5 → 30 when derivation moved
from imports to path literals, prose counted as code three times. A green local validator run checked
**nothing**, because the gates are changeset-scoped and the tree was clean.

The rule this plan is written under, and which its execution should inherit: **count by execution, never
by phrasing; and treat every "X does not exist" as unverified until a positive control — a search for
something known to exist, by the same method — has been run.**
