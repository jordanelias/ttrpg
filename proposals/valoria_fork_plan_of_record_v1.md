# Valoria Fork — Plan of Record

## Status: PROPOSED (ED-IN-0123, 2026-08-02). Jordan-vetoable throughout.
## Class: A — substrate/architecture. **Nothing here ratifies on merge.** §7 holds every decision that
## needs one, including four already held by registers this plan does not own.
## Supersedes: the v1 draft of the same day, which failed an independent critic pass (16
## CONFIRMED-WRONG). §9 records what it got wrong and why, because the failure mode is instructive
## and recurs. The corrected numbers are carried; the architecture is rebuilt.

---

## 0. Reading order for a new session (do this before anything else)

This plan is a conclusion. Without its inputs a new session will re-derive them badly — which is
exactly what its own v1 did, twice, and what §9 is about. **~19k words total; budget one read.**

| # | Read | Words | What you get wrong without it |
|---|---|---|---|
| 1 | `CLAUDE.md` §0–§1, §5, §8 | 7.4k | The currency protocol, the measurement discipline, and that every rule lives once |
| 2 | **`references/wiring_manifest.yaml`** | 1.4k | **The single most important file.** Build state + Godot state + port rank + parity target for all 27 modules and 8 adapters, plus the three foundation gaps. Skipping it is how v1 proposed rebuilding it |
| 3 | `systems/_architecture/holonic_container_doctrine_v1.md` §1–§2 | 1.3k | That the container shape is CANONICAL and frozen (`Key IN → resolver → OUT`), and that a second interface dialect is a named, forbidden failure mode |
| 4 | `godot/godot_conversion_strategy_v1.md` Parts V–VIII | 5.7k | Gate-0's five preconditions, the Stage-1 spine, the per-module ritual, and the 8 open Jordan items. **Do not write a port plan without this** |
| 5 | `audit/2026-07-30-mb-session-retrospective/00_lessons.md` | — | Guardrails G13–G21 and why `main` is CI-red. §3.1b bisects every failure to a named flag |
| 6 | This document | 2.7k | The Python-side Stage 0 the strategy assumes |

**Then orient by execution, not by reading** — every one of these works today:

```bash
python3 tools/wiring_map_check.py --check      # 27/27 modules · 8/8 adapters · tags resolve
python3 tools/wiring_map_check.py --summary    # the build-state ladder — Stage 0's metric
python3 tools/wiring_map_check.py --work-list   # the ranked port order. THE work-list
python3 tools/review_core.py --check            # repo-state verdict vs review_baseline.yaml
python3 tools/export_engine_params.py --check   # combat oracle → JSON round-trip (blocking)
python3 tools/export_sim_params.py --check      # 324 extracted constants, drift gate
```

**Do NOT read**, and this is load-bearing rather than advice: the 339,462 lines of process/audit
markdown (80% of the corpus). It audits a prose regime principle 7 supersedes. `engine/params/*.md`
in particular has **zero readers** in `engine/` or `systems/` — reading it to learn "the values" will
teach you a layer nothing executes.

**The one procedure that matters.** Before asserting anything does not exist, run a positive control:
search for something you *know* exists, by the same method, and confirm the method finds it. Every
significant error in this plan's history was a false absence derived from a proxy — see §9.

---

## 0.1 The thesis

**The Godot port already has a detailed, dependency-ordered strategy. The Python side does not.**

`godot/godot_conversion_strategy_v1.md` specifies Gate-0's five blocking preconditions, a spine
(kernel · KeyStore v2 · seeded RNG service · statechart · generated loaders), a six-step per-module
port ritual, a ten-item frictions register and an eight-item Jordan register. It is more complete
than anything this plan could add, and v1's central error was re-deriving it badly.

But Gate-0 **presupposes a Python side that is ready to be ported from**, and G0.5 states the
condition explicitly: *a module ports only from canonical/ratified sources… and halts on any value
untraceable to a cited source.* Measured against `references/wiring_manifest.yaml`:

| | modules | |
|---|---|---|
| **execute today** (`live` + `gated`) | **3 of 27** | mass_battle, victory, social_contest |
| reached but resolve nothing (`deferred`) | 10 | |
| real code the loop never calls (`unwired`) | 2 | personal_combat, threadwork |
| raise `NotImplementedError` (`stub`) | 3 | |
| specified in a doc, zero code (`design`) | 9 | |
| **nothing to port from** (`godot: no-oracle`) | **14 of 27** | |

**Three of twenty-seven modules run.** Jordan's principle 5 — *"100% runnable in Python, then
port"* — is therefore not a variation on the conversion strategy. It is **the missing Stage 0 that
the strategy's own Gate-0 assumes and nobody has planned.**

> **Reconciling with the tool.** `wiring_map_check.py --summary` reports over **modules AND adapters
> together — 35 units**: `deferred:11 · design:9 · gated:6 · stub:4 · unwired:3 · live:2`, and
> `python-oracle:17`. The table above is **modules only (27)**, because modules are the conversion
> units — one module contract = one conversion unit = one parity target (strategy §IV.3). Both are
> correct; they count different populations. Adapters contribute the other 8: `gated:5 · deferred:1 ·
> unwired:1 · stub:1`. Combined, **8 of 35 units execute.** Stated because a reader who runs the tool
> would otherwise think this plan's headline number is wrong.

That is this document's only real contribution. Everything else here is assembly.

---

## 1. What already exists (read before building anything)

v1 proposed building four things that exist. They are the fork's foundation, not its backlog.

| Asset | What it already is |
|---|---|
| **`references/wiring_manifest.yaml`** | The per-subsystem manifest, as DATA, anchored on stable tags so it survives restructures. 27 modules + 8 adapters, each with `build` / `godot` / `port_rank` / `parity` / note. Validated by `tools/wiring_map_check.py --check`; `--work-list` emits the ranked port order. **This is the work-list. Do not author another.** |
| **`references/module_contracts.yaml`** | The canonical container contract — uniform **Key IN → resolver → OUT**, schema-2, 27 modules. Per the holonic doctrine (CANONICAL, ratified 2026-07-02) this *is* the wrapper shape; guardrail 2 forbids growing a second dialect. |
| **`references/key_graph.json`** | The merged key graph (built this session): 56 types, producers/consumers reconciled across the registry and the contracts, zero genuine conflicts, guarded by 12 tests. |
| **Two live extraction pipelines** | `combat_engine_v1.json` (230 scalars, blocking round-trip gate, green) and `sim_params.json` (324 constants across 13 modules, `--check` clean). **554 typed values already extracted.** |

**The golden path is already named** (`wiring_manifest.yaml:42-45`): `personal_combat` is the only
unit with Python oracle + typed export + GDScript port. *"The template every other port copies."*

---

## 2. What Jordan's principles actually change

Six of the eight principles are already the repo's direction. Two change something:

**Principle 6 — Monte Carlo is a modelling tool, not the oracle.** This *resolves* conversion-strategy
Jordan register item #2 ("Python corpus role"), which has been carried unruled from the Workplan-R2
docket. It should be recorded as closing that item, not restated as new. Structurally it means
`mc_v18` (337 LOC — seeds, batches, `CampaignResult` analytics) is a **client** of the engine, and
`workbench/` (2,031 LOC) stays Python permanently.

**Principle 7 — code/tables outrank prose; prose is canon only without a code pair.** Now computable
and computed: **14 modules code-authoritative, 5 prose-authoritative, 8 with no authority at all.**
The 8 are the genuinely homeless set, and they are exactly the `godot: no-oracle` blockers.

### 2.1 The pipeline finding that reorders the data work

An end-to-end trace of every pipeline in the repo:

- `engine/params/*.md` — 43 files, 1,891 table lines — has **zero readers** in `engine/` or
  `systems/`. It is consumed only by drift-checkers in `tools/`.
- Two extraction pipelines produce **554 typed values**.
- **No pipeline delivers a value to anything that runs.** Every terminus is a test, a dashboard, or
  self-verification. `combat_engine_v1.json` is read by one test, one scan tool, and its own producer.

So "centralize values into tables" is **not a prose-conversion project**. The prose is already
vestigial; the code holds its constants inline; two tools already extract them. The work is to
**invert the extractions** (table becomes source, Python constant becomes generated view) and to
**build the consumer half** — the cook step, which external practice puts at the centre of any
content pipeline and which this repo has never had.

**The repo is producer-heavy and consumer-empty.**

---

## 3. Stage 0 — Python-side readiness (the missing stage)

The metric is the manifest's own `build` ladder. A module climbs:

```
design  →  stub  →  deferred  →  unwired  →  gated  →  live
(no code)  (raises) (resolves    (real code, (runs on a  (runs every
                     nothing)     no caller)  condition)   season)
```

**Stage 0's exit condition:** every module the fork intends to port reaches `live` or `gated`, and
`wiring_map_check --summary` reports it. That is a measurable, already-instrumented target — not a
new gate, an existing one used as a goal.

Ordering follows `port_rank`, which the manifest already assigns:

- **rank 0-1** — `personal_combat` (unwired; the golden path, and *the combat branch is dead code in
  the campaign*), `mass_battle`, `social_contest`, `victory`. **This is where Stage 0 starts.**
- **rank 2-3** — threadwork, territorial_piety, faction_state, faction_politics, piety_track,
  settlement_layer, clock_registry + five adapters.
- **rank 8** — the 14 `no-oracle` modules. **These need canon authored before code**, and per
  principle 7 their prose is authoritative *only until* code lands. `engine_clock` is the sole
  remaining T0 blocker (ED-1051) and gates the season/accounting cadence.
- **rank 9** — `settlement_economy` and `campaign_architecture` are marked `retire`. **The live
  roster is 25, not 27.**

### 3.0 What Stage 0 should expect, imported from the lanes that already did it

MB and PC have both advanced since `wiring_manifest.yaml`'s `as_of: 2026-07-29`, and their
experience is directly predictive of Stage 0's climb.

**`gated` → `live` will surface defects, and that is the point.** Guardrail **G20** (ED-MB-0061):
*"A test asserting a flag defaults OFF protects the ORACLE, not the engine."* Flipping 15 flags ON
in one commit surfaced **nine engine defects**, and the suite had contained **seven tests asserting
those flags must default OFF** — institutionalising the blind spot by making the unmeasured state
the protected state. The manifest's `gated` build state is literally *"runs only under a condition
(flag / eligibility / trigger)"*, so **every `gated` → `live` promotion in Stage 0 is a small
replay of that commit.** Expect defects; budget for them; do not read them as regressions.

**And do not let the metric bless a null system.** Guardrail **G13**: *"If doing nothing scores well
on your metric, the metric cannot validate a change."* An exclusion pass was reported as
"17.31% → 0.35% overlap" — the 0.35% arm had **deadlocked the engine**; cells were not overlapping
because they were not moving. Stage 0's metric is the build-state ladder, and a module can climb to
`live` while resolving nothing. **The ladder must be read alongside its `parity` field**, which the
manifest already assigns per module (key-log / typed-export round-trip / state read / data).

**PC has been shipping correctness batches, not scaffolding.** `ED-PC-0045..0052` across four PRs
added roughly **1,000 lines of new combat tests** — cut grading, close unwieldiness, curve recovery,
element reachability, spike ADEF, thrust arm heft, lever sign safety. `personal_combat` remains
`build: unwired` (the campaign never routes to it) while its *internal* correctness surface has
grown substantially. That combination — a well-tested engine the loop never calls — is precisely
what W3 exists to fix, and it means W3 is a **wiring** task, not a correctness task.

### 3.1 The three foundation gaps, which outrank every module

`wiring_manifest.yaml:93-102` records these and v1 omitted all three:

1. **`godot_spine`** — `BaseEngine` / `EngineModule` / `KeyBus` / `Resolver` / `GameState` are
   referenced by the skeleton with `class_name` defined **nowhere**. Gate-0. The skeleton is
   non-compilable, which is why it must be regenerated, not ported.
2. **`character_layer`** — no `Character`/`Actor` dataclass exists in `World`; 9- vs 10-attribute
   rival rosters, neither wired. **Every personal-scale port needs this first**, which puts it ahead
   of `personal_combat` despite that being rank 0.
3. **`save_replay_premise: violated`** — *the live strategic loop mutates `World` directly
   (`Faction.L`, `Territory.owner`) with no Key trace, so the Key log cannot reconstruct strategic
   state.* Save/replay/parity hold only for the echo-keyed slice.

Gap 3 is load-bearing and its consequences run further than the register states. The conversion
strategy's Stage 1 specifies **`save = serialize-the-log`**, and Stage 2 step 3 makes **Key-log
equality the master parity check**. Both rest on a premise the repo has already recorded as
violated. Independent corroboration from this session: a seeded campaign under `coverage` executes
**38% of statements**, leaves 37 files at 0%, and produces **zero rows for `combat_engine_v1`** —
which is the same fact the manifest states in words. **Closing gap 3 is the highest-value Python-side
work there is**, because parity, save/load and replay are one mechanism used three times.

---

## 4. Architecture — what the fork may and may not decide

**The container shape is already frozen and is not this plan's to change.** The holonic doctrine
(CANONICAL) fixes `Key IN → resolver → OUT` and its guardrail 2 forbids any scale growing its own
interface members. v1 proposed an `orchestrator.resolve()` channel; that is a second dialect, and it
is withdrawn.

**Downward delivery cannot be designed here.** The doctrine calls the propagation spec *"the
highest-value unauthored canon in the repo"* and names non-termination (up-event → down-event →
up-event) as the scariest runtime risk. It is conversion-strategy Jordan item #1 (ED-1006). **Any
orchestrator that dispatches downward into subsystems is designing that ruling by implication.** So:

> **The fork does not build a downward-dispatching orchestrator until ED-1006 is ruled.** Until then
> the interim rule (strategy §IV.2) applies and every downward edge is flagged.

What the fork *may* do without a ruling:

- **Keep the upward direction**, which is established: subsystems emit Keys; `KeyLog` validates and
  logs; `apply` closures land at the accounting boundary. That mechanism works and has two live
  emitters.
- **Close gap 3** by routing the strategic loop's direct `World` mutations through Key emission with
  paired `apply` — which is not new architecture, it is the *existing* `echo_transport` pattern
  extended to the writes that currently bypass it.
- **Own sequencing in the log.** `KeyLog` already maintains `_season_counters`; the per-emitter
  counters on `world` (`_echo_key_seq`, `_battle_key_seq`) are collision-free by naming accident.
  Compose on the existing counter rather than adding a second keying.

### 4.1 The edges relation — a generator fix, not a new file

`key_graph.json`'s `producers[]`/`consumers[]` arrays assert a full cross-product: **164 implied
edges from 56 types**, 11 types with both >1 producer and >1 consumer, `scene.dialogue` alone
asserting 3×4 = 12 edges nobody authored.

v1 proposed hand-authoring an `edges` relation. **That file's header says NEVER hand-edit**, and the
arrays are already a generated view — every row carries `registry_producers` / `contract_producers` /
`producer_status` precisely to reconcile the two authored sources. The two-representation problem is
**upstream**, in the registry-markdown / contracts-YAML pair. So: emit `edges` from
`build_key_graph.py` as a *third derived view* keyed `(type, producer, consumer)`, and fix
provenance in the generator's inputs. No new hand-maintained surface.

---

## 5. What the fork carries

**CARRIES** — `engine/` (substrate · autoload · cross_scale) · all `systems/*/sim` ·
`combat_engine_v1` (7,849 LOC incl. workbench) · `engine/tests` · the four assets of §1 ·
`export_engine_params.py` + `export_sim_params.py` (the two working pipelines) ·
`wiring_map_check.py` · the 7 canon files · the 280-file design corpus **as conversion input**.

> **CORRECTION 2026-08-03 (ED-MB-0043 resolved).** `tests/sim/mass_battle/` is **CANON** and must be
> CARRIED, despite living under `tests/`. The live campaign runs the *other*, staler tree
> (`systems/mass_battle/sim`, 5 modules vs 28). Carrying `systems/*/sim` wholesale and leaving
> `tests/` wholesale would take the stale engine and abandon the developed one. Directory is not
> authority here — the canon mass battle is misfiled, and the fork is the moment to re-home it.

**LEAVES** (source repo, frozen provenance) — `registers/` · `audit/` · `arcs/` · `workplans/` ·
`dashboard/` · the observability apparatus. Cite back by `repo@SHA + PP/ED`.

**UNRESOLVED, and it must be resolved before W0** — **`tests/sim/mass_battle`: 28 modules, 11,269
LOC, last advanced 2026-07-31.** The manifest calls it *"a RICHER unwired engine… (mislabeled a
frozen archive) — reconcile before porting"*; `CURRENT.md` holds the two-disjoint-code-trees fork for
Jordan under ED-MB-0043. A fork that copies `systems/mass_battle/sim` and leaves this behind may be
abandoning the better engine. **§7 item 5.**

**Self-containment is not yet true.** Measured: zero import escapes from `engine/`/`systems/`, but
**path-literal escapes exist** — `engine/tests/` reaches `skills/` (leaving), `audit/` (leaving),
`registers/`, and a retired `designs/` path whose load sits inside a bare `except`, so a parity class
**silently skips today**. W0's falsifier must scan path literals, not imports; v1's did not, and the
lesson was recorded in v1's own §9 before being violated in its §6.

---

## 5.5 The spine — `references/EXECUTION_MAP.md` (2026-08-03)

**The plan's waves were a list. They now hang off a spine.** `tools/build_execution_map.py` emits
the boot → season-loop → termination order joined against `module_contracts` (Key IN → resolver →
OUT, owned state), `wiring_manifest` (build / godot / rank / parity) and `key_graph`
(producers / consumers). Read it before the wave table below; the waves are *positions on it*.

```
boot ─ create_world(seed)          deterministic; the save/load entry point
     ├ victory.reset · scene_slate.clear
     ├ flags            DISPATCH_COMBAT_BRIDGE decided ONCE, stashed on world
     ├ substrate        TickScheduler + KeyLog  ← THE ORCHESTRATOR. Presence = ECHO_TRANSPORT
     └ subscribe        articulation → the only production subscriber wiring
loop ─ while not winner, max_s times
     ├ s1  advance_season          engine_clock is doc:null — ED-1051, the T0 blocker
     ├ s2  action_callback         ← THE PORT SEAM. Godot passes its own to drive UI scene flow
     │   ├ faction actions         per parliamentary faction holding territory
     │   ├ scene phase             MEASURED: 29 slots/campaign, ALL contest. No combat trigger
     │   ├ parliamentary vote      flag-gated on the scheduler
     │   └ ACTION→ACCOUNTING       deferred `apply` closures land HERE (OF-7), then next_tick()
     ├ s3  run_accounting          SIX steps: CI · MS(year-end, caller-gated) · insurgency
     │                             emergence · promotion(over a snapshot) · NPE · drift probe
     └ victory check (GD-1)        sets winner; the loop breaks on the NEXT iteration
term ─ fallback winner by territory count → CampaignResult{key_log_hash, keys_emitted}
                                            ← the Godot parity surface (strategy Stage 2)
```

**What the map measures, and what it does not.** Verified: the source anchors (re-checked against
the files by `tests/valoria/test_execution_map.py`), `executes` (derived from the manifest and
re-derived independently in test), the code/doc paths (21 declared, all resolve; **14 units have no
code yet**), and the key + owned-state joins. **Not** verified, and labelled
`modules_attribution: "authored-unverified"`: the per-phase module lists. Two derivations were
built and both discarded — per-file transitive imports gave every `mc_v18`-sourced phase the same
seven units; per-function local imports gave almost nothing, because this codebase splits
cross-subsystem calls between module-level and function-local imports while phase boundaries do not
align with function boundaries. **The correct instrument is dynamic** — trace a seeded campaign and
record which module code runs between phase markers. That is W-A below.

**Three numbers from the map that should drive sequencing:**

| | |
|---|---|
| units that execute | **8 of 35** |
| key types with both a producer and a consumer | **46 of 56** (2 have no producer, 8 no consumer) |
| owned scalars with two claimants | **1** — `CI (Church Influence)`: `ci_political` + `territorial_piety` |

---

## 6. Sequencing

| | Content | Exit condition (falsifier) | Jordan |
|---|---|---|---|
| **W0** | Repoint the path-literal escapes; un-skip the silently-skipping parity class | A path-literal scan (not an import scan) shows zero escapes; the previously-skipping parity test runs and passes or fails honestly | no |
| **W1** | ~~Close `save_replay_premise`~~ **DONE 2026-08-03 to `partial`** — the premise was less broken than recorded; one untraced ownership write (`parliamentary_transfer`) now emits `da.public_governance`. Residue: `mass_seizure` unexercised by the measured seed; `Faction.L` evidence thin (clamp saturation) | Reconstruction is **8/8** on `Territory.owner` at horizons 3/6/12/24, falsifier `tests/valoria/test_public_governance_transfer_key.py`. NOT flipped past `partial` — see §6.2 | no — it restored a stated premise |
| **W2** | Author the `character_layer`: one `Character`/`Actor` dataclass in `World`; resolve the 9-vs-10 attribute roster | Personal-scale modules can hold state; roster is single-valued | **yes** — OPT-AV-1 |
| **W3** | Stage 0 rank 0-1: `personal_combat` → `live` (the combat branch is dead code today), then `mass_battle`, `social_contest`, `victory` | `wiring_map_check --summary` shows those four at `live`/`gated`; each has key-log parity per its `parity` field | no |
| **W4** | Invert the two extraction pipelines: table becomes source, Python constant becomes generated view; add the `citation` column (**0 of 324 `sim_params` records carry provenance**) | Round-trip CI red on a hand-edit of a generated view; every value traces to a `PP`/`ED` | per-value collisions: **yes** |
| **W5** | ~~Build the cook step: JSON → `.tres`~~ **BLOCKED, measured 2026-08-03 — see §6.3.** There is no weapon JSON to cook from, and the `.tres` schema encodes a model the oracle retired | Unblocking needs (a) a typed weapon export and (b) the GDScript weapon resource re-derived from the current oracle | **yes** — (b) is a port change under ED-1050 discipline |
| **W6** | Stage 0 rank 2-3; then the 14 `no-oracle` modules, `engine_clock` first (ED-1051, the sole T0 blocker) | `authority: none` count reaches 0 or DEFERRED-with-citation | **yes** — canon authorship |
| **W7** | Godot Gate-0 (G0.1–G0.5) and the strategy's Stage 1 spine | The strategy's own gates. **No Godot claim is verifiable until `project.godot` and a Godot binary run in CI — neither exists** | **yes** — ratify the strategy first |

W0–W1 are the whole near-term critical path. They need no ruling and they make everything after them
measurable.

### 6.1 W0 as executed (2026-08-03) — including one item measurement struck

**Escapes: 10, not four.** The scan found ten distinct `(file, literal)` escapes out of
`engine/`+`systems/`, and the composition mattered more than the count: exactly **one was
runtime** — `engine/autoload/registry.py`, whose `load_index()` read
`registers/mechanics_index.yaml` from inside the engine's own autoload hub. Copy `engine/`
into a fresh repo and that file is broken on arrival. It had **zero callers** and the repo's
own structure audit had already classified it `VERIFIED_ORPHAN_NO_CALLSITE`, so it was
deleted rather than re-homed. Down to **6**, all test/workbench, none runtime.

**The parity class was two silent-skip channels, not one.** The known one was the bare
`except` on a retired `designs/audit/` path (184 cases dark for 15 days). The second was
structurally identical and unrecorded: every combat-surface comparison sat behind
`if not _numpy_available: pytest.skip(...)`, so a numpy-less environment tested nothing and
said so only as a skip. Both are gone. The fix is the same inversion §2.1 prescribes for
params — `tools/gen_sigma_parity_goldens.py` runs in the source repo where the oracles live
and emits a 1,758-row table; the test reads the table; `engine/` reaches nowhere.
**761 → 1,926 executing assertions, zero skips, no numpy dependency.**

**`combat_engine_v1` packaging: STRUCK.** The row required making it a package "so it is
importable and measurable", with `coverage` rows as the falsifier. Both halves are false.
Measured 2026-08-03: `import core, combat_systems, combatant, config` off `sys.path`
succeeds today, and `coverage run --source=systems/combat/combat_engine_v1` over two of its
own test modules reports **17 files at 75%** — `combat_systems.py` 98%, `core.py` 99%,
`wrapper.py` 93%, with only `capabilities.py` and `state_graph.py` at 0%.

The plan inferred an importability defect from §3.1's true observation that a *seeded
campaign* under coverage yields zero rows for `combat_engine_v1`. That is a **wiring** fact —
`personal_combat` is `build: unwired`, so the campaign never reaches combat — and it is
already W3's subject. Attributing it to packaging would have bought a 20-module import
rewrite of a working scripts-on-path tree, changing nothing the falsifier measures. CLAUDE.md
§3 records the non-package shape as deliberate (the `import systems` collision it resolved).
**The zero-rows observation belongs to W3 and is deleted from W0.**

### 6.3 W5 is blocked, and the two reasons are independent (measured 2026-08-03)

W5 reads "cook the typed JSON into `.tres` for the golden path", with the falsifier "a generated
`.tres` for all 51 canonical weapons (2 exist, hand-made)". Both halves of the pipeline are absent.

**1. There is no weapon data in the typed export.** `engine/engine_params/combat_engine_v1.json`
declares `source: config.py + core.py` and contains exactly two sections — `cfg` (204 constants) and
`core` (26). Zero weapons. The roster lives in `combatant.py` as `WEAPONS`, **53 entries** (not 51),
carrying rich per-part geometry: `elements[]`, `guards[]`, `haft`, `pommel`, `geo`, `_derived`. The
exclusion is deliberate, not an oversight — the export was scoped to the Class-C tuning constants.

**2. The `.tres` schema encodes a model the oracle retired.** Of its 15 fields:

| | |
|---|---|
| map directly to `WEAPONS` | 11 (incl. `reach_adj`, present on 27/53 — optional, not absent) |
| computed | 1 — `pob_frac` = `_derived['PoB_frac']` |
| **retired in Python, still LIVE in GDScript** | 2 — `reach`, `weight` |
| dead in both | 2 — `spd`, `handling` (zero reads in any `.gd`) |

`config.py:7` records *"Phase-3b: reach DERIVED from geometry (retires categorical reach=='long' +
HEAD_REACH + the reach_adj triple-duty)"*, and `combat_systems.wield_heft` is *"DERIVED, g-aware …
replaces the binary wt class"*. **0 of 53 weapons carry `reach`, `wt`, `weight`, `spd` or
`handling`.** Yet `strike_module.gd:110` still computes `4.0 + 2.0 * float(w.reach == "long") + …`
and `combat_config.gd:84` still branches on `weapon.weight == "heavy"`.

So generating 53 `.tres` in the current schema would require **inventing** `reach` and `weight` for
every weapon — fabricating values, and fabricating them into a superseded model. That is the ED-1050
defect ("never let a port correct its oracle in-place") reproduced 53 times instead of once. The
correct order is oracle-first: export the weapon roster, re-derive the GDScript resource from it,
then cook. Step two is a port change and therefore §7's, not this plan's.

**Note the shape.** This is the fourth wave whose stated premise did not survive measurement (W0
packaging, W3 wiring, W4 provenance, now W5). Every one was written from a true observation with one
inference too far, and every one was cheap to check and expensive to have acted on.

### 6.2 W1 as executed (2026-08-03) — the premise was mismeasured, not just unmet

The manifest's note said the strategic loop mutates `Faction.L` and `Territory.owner` **with no Key
trace**. Building the falsifier *before* the fix — replay the log onto a t0 snapshot, compare —
showed that to be too pessimistic in a way that mattered for scoping: `Faction.L` already
reconstructs from `Target.stat_deltas`, territorial conquest already reconstructs from
`scene.battle_concluded`, and **7 of 8** ownership changes rebuilt. W1 was one site, not a sweep.

**Finding the site required abandoning the grep.** An AST scan for attribute assignments reported
3 non-test `Territory.owner` writes and **zero** non-test `Faction.L` writes — a false absence, and
a confident one. `Faction.adjust()` writes via `setattr(self, stat, val)`, so the single owner that
**31 call sites** route through is invisible to that scan. Instrumenting `Territory.__setattr__`
across a seeded campaign attributed every write in one pass: `faction_action` 8,
`parliamentary_transfer` 1, `mass_seizure` 0.

**Three confounds in my own instrument, all of which flattered the result**, recorded because the
next reconstruction claim will meet them again:
1. `Faction.L` scored 4/4 rebuilt — but 3 of 4 factions sat **exactly on a clamp** (0.5 floor / 7.0
   ceiling), and a clamped rebuild agrees with a clamped actual whether or not the deltas are
   right. Only 1 comparison was ever informative. **Any L claim must report the off-boundary count.**
2. The first territory pass *counted* keys carrying transfer evidence without *applying* them, so
   "11/16 unreconstructable" measured my replay, not the log.
3. The season sweep varied nothing: `run_campaign(max_seasons=N)` is shadowed by
   `effective_params['CAMPAIGN_SEASONS']`, so four horizons ran identically. A control that
   controls nothing reads exactly like a control that does.

**Why it stops at `partial`.** `mass_seizure.py:292` is the third owner-write site and did not fire
on the measured seed — untested, not proven clean. And the replay rule (*`da.public_governance` +
`outcome: success` + `target_territory_id` ⇒ that territory is now `faction_id`'s*) is an
**interpretation the key-type registry does not declare**. It is sound for all three live emitters
today, but a dedicated `da.territorial_transfer` type would state it rather than imply it. **That is
a canon addition and therefore §7's, not this plan's** — the emitter deliberately uses only fields
already in the registered entry so that nothing here mints canon by implication.

---

### 6.4 Re-sequenced against the spine (2026-08-03) — three tracks, not one list

The original W0–W7 was a single ordered list. Measurement has since struck one item (W0 packaging),
blocked two on canon (W3, W5) and shown one premise mismeasured (W1). What remains does not
serialise, because **the blocked items are blocked on YOU, not on each other** — so it is three
tracks that run in parallel, each anchored to a phase of the spine.

**Track E — ENGINE (unblocked, mine).** Everything here is measurable against the spine today.

| | position on the spine | work | exit condition |
|---|---|---|---|
| **E1** | all phases | **Dynamic phase attribution.** Trace a seeded campaign, record which module code executes between phase markers. Replaces `authored-unverified` with measurement | every phase's module list is derived; the two failed static attempts are recorded in `build_execution_map.py` so this is not re-tried statically |
| **E2** | `loop.s2` → `s3` | **`Faction.L` reconstruction.** 30 of `Faction.adjust()`'s 31 call sites emit no Key. Route stat mutation through emission | `test_faction_l_reconstruction`'s strict xfail turns XPASS |
| **E3** | `boot.substrate`, `loop.s2.boundary` | **The 10 dead key types** — 2 with no producer, 8 with no consumer | each is wired, or DEFERRED with a citation |
| **E4** | `loop.s3` | **The one contested scalar** — `CI (Church Influence)` claimed by `ci_political` and `territorial_piety`. Single-owner it | `execution_map.json`'s contested count reaches 0 |
| **E5** | — | **The 240 uncited constants** (84/324 cited, 8 assumption-grade). Per-value canon lookups; paced, not bulk-run | `citation_coverage.uncited` falls, with every value traced |

**Track C — CANON (blocked on Jordan).** Each is a *decision*, not a task; none can be inferred
without designing your ruling by implication.

| | position | the question |
|---|---|---|
| **C1** | `loop.s2.scenes` | **What triggers a personal combat?** Nothing queues a combat scene — `evaluate_triggers` can only emit `contest`. This is why `personal_combat` (rank 0, the golden path, 75% covered) never runs |
| **C2** | `loop.s2.factions` | **The mass-battle rewire.** Canon is `tests/sim/mass_battle` (28 modules); the campaign calls the 5-module tree. Canon returns `{winner, turns, phases}`; the caller needs `{attacker_wins, degree, *_size_pct}`. **`degree` is the blocker** — canon has no four-band degree, and it drives the territorial outcome. Needs the mapping ruled, plus a faction→unit roster |
| **C3** | `loop.s1` | **`engine_clock`** — `doc: null` temporal spine, ED-1051, the sole T0 blocker |
| **C4** | all personal-scale | **The attribute roster** — OPT-AV-1; blocks `character_layer` |
| **C5** | `loop.s2.boundary` | **ED-1006 downward delivery** — blocks any downward-dispatching orchestrator |
| **C6** | — | **`da.territorial_transfer`** — or ratify that `da.public_governance` + `target_territory_id` means an ownership change. Today that rule is an interpretation the registry does not declare |

**Track I — INFRASTRUCTURE (unblocked, and I would do I1 first of everything).**

| | work | why it outranks engine work |
|---|---|---|
| **I1** | **Get `main` green.** 9 MB-lane failures, each bisected to a named flag under ED-MB-0061 | While `main` is red, CI carries **no signal** — a real regression and the background are indistinguishable. Every PR's aggregate is red; this session burned four wake-ups re-confirming the same nine |
| **I2** | **Make required checks specific, not aggregate.** `All Gates Green` counts *cancelled* jobs as failures, so it trips on any push that supersedes a running build | It generates notifications that generate work, with no defect behind them |
| **I3** | **The 14 units with no code** — the map's `no_code_declared` set. Each is a canon-authoring job (Track C) or a retire | It is the fork's real backlog, and it is now a generated list rather than a judgement |

**Ordering rule.** I1 → then Track E in parallel with whatever of Track C you rule. Nothing in E
depends on C except by position; nothing in C depends on E at all.

---

## 7. Held for Jordan

1. **ED-1006 — downward Key delivery.** Blocks any downward-dispatching orchestrator. Named the
   highest-value unauthored canon; non-termination is the runtime risk.
2. **OPT-AV-1 — the attribute roster.** Blocks `character_layer`, and through it every personal-scale
   module.
3. **ED-1051 — `engine_clock`.** `doc: null` temporal spine; the sole remaining T0 blocker.
4. **ED-FA-0002 — `domain_actions` home.**
5. ~~**ED-MB-0043 — the two-disjoint-mass-battle-trees fork.**~~ **RESOLVED 2026-08-03 by Jordan: the canon tree is `tests/sim/mass_battle/`** (commit/PR #274). Measured consequence, and it corrects §5: the LIVE campaign imports `systems.mass_battle.sim.massbattle` (faction_action.py:431), the 5-module 2,375-LOC tree with zero `PC_*` flags. Canon is the 28-module 11,269-LOC tree under `tests/`, which the campaign never calls. **The carry list said carry `systems/*/sim` and leave `tests/` — that would have carried the stale engine and left canon behind.** Every MB result (Track F, the bisects, geometry S1–S4, the 9 red tests) is measured on the tree the game does not execute.
6. **Fork point — CORRECTED, and it needs less from you than v1 claimed.** I reported the MB
   Track-F set as *non-deterministic* because CI showed 9 then 10 failures across commits that
   touched only markdown. **That was wrong, and the MB lane had already documented why.**
   `ED-MB-0061` (corrected 2026-07-31) states the count convention outright: *"Failure counts quoted
   as 16 and 9 are LOCAL runs. CI reports 17 and 10. The constant +1 is
   `test_mass_battle_byte_exact::test_byte_exact_cell_mode`, which SKIPS locally on a documented
   pre-existing non-portability and RUNS on CI."* And §3.1b, **"ALL FAILURES BISECTED (2026-07-30)"**,
   restores each failure by returning one named flag to OFF — `PC_FRICTION_CEV`,
   `PC_FRACTIONAL_POOL`, `PC_CELL_MORALE`, `PC_FACING_MODEL`, `PC_CLOSE_RANKS`, with exactly one
   (`per_cell_break_subsumes_the_body_level_one`) a genuine multi-flag interaction.
   So the red is **accounted, bisected, and attributed** — not a mystery and not flakiness. The fork
   carries the set as `xfail` citing ED-MB-0061, and the only thing needed from Jordan is
   confirmation that the flags-ON ruling stands.
7. **The conversion strategy's own eight open items** — carried by reference, not restated. Principle
   6 appears to close item #2; that should be recorded there.

---

## 8. Where this plan is most likely wrong

1. **Stage 0 may be larger than the fork.** Getting 25 modules to `live` is most of building the
   game. If so, the fork should carry a *subset* — the rank 0-3 spine — and leave the rest.
   *Settling measurement:* size W3 against the four rank 0-1 modules, then extrapolate from actuals.
2. **Closing `save_replay_premise` may be architecture, not plumbing.** If the strategic loop's
   writes cannot be expressed as Key `apply` closures without redesigning `World`, W1 is a much
   bigger wave. *Settling measurement:* attempt one — `Territory.owner` in `faction_action`, where a
   Key already fires alongside the write.
3. **The 5 prose-authoritative modules may encode intent the code never implemented.** *Settling
   measurement:* per-module, diff prose-declared `emits`/`consumes` against code — the same join
   that found the 55-declared / 2-emitted gap.
4. **`wiring_manifest.yaml` is dated `as_of: 2026-07-29` and is analysis-derived.** This plan leans
   on it heavily. PARTLY SETTLED: `wiring_map_check --check` passes (27/27 · 8/8 · all tags resolve)
   and the commit log since that date was reviewed — MB landed ED-MB-0045..0061 and PC landed
   ED-PC-0041..0052, neither of which moves a `build` verdict (PC's work is internal correctness;
   `personal_combat` is still `unwired`). *Remaining measurement:* spot-check three `build` verdicts
   against execution before committing to the ladder — `--check` validates that tags RESOLVE, not
   that the verdicts are still true.

5. **Stage 0's metric can be gamed by a null system** — G13's failure mode, imported at §3.0. A
   module can reach `live` while resolving nothing, which is what `deferred` already means. The
   ladder is only safe read together with each module's `parity` field. *Settling measurement:* for
   the first module promoted, assert its parity target passes, not merely that it executes.

---

## 9. Why v1 failed, recorded because the failure recurs

v1's measurements were sound — every graph number recomputed exactly by an independent reader. Its
architecture and scoping were not, and both defects had the same shape:

- It proposed building a per-subsystem manifest **that already existed** in `wiring_manifest.yaml`,
  along with the headline finding, the character-layer gap, and the violated save/replay premise.
- It reported **"14 homeless modules"** by reading `subsystem: null`. Six of those rows name a `doc:`
  in the adjacent field, and `mass_battle`'s row states outright that its `sim_module` is empty by
  **lane-ownership discipline, not absence**. The real number is 8. A decision — wrapper granularity
  — rested on a figure inflated 1.75× by not looking one field over.

Both are **false absence derived from a proxy**. v1's own §9 warned against exactly that, by name.
Writing the warning did not prevent committing the error twice inside the document containing it.

The operative rule, stated as a procedure rather than a principle because the principle demonstrably
does not transfer: **before asserting that something does not exist, run a positive control — search
for something you know exists, by the same method — and only then report the absence.** A rule that
is stated but not executed is a rule that will be broken by the person who stated it.
