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

## 6. Sequencing

| | Content | Exit condition (falsifier) | Jordan |
|---|---|---|---|
| **W0** | Repoint the path-literal escapes; un-skip the silently-skipping parity class | A path-literal scan (not an import scan) shows zero escapes; the previously-skipping parity test runs and passes or fails honestly | no |
| **W1** | Close `save_replay_premise` — route direct `World` mutation through Key emission + `apply`, extending `echo_transport`'s existing pattern | A seeded campaign's Key log reconstructs `Faction.L` and `Territory.owner` from initial conditions; `wiring_manifest`'s `save_replay_premise` flips from `violated` | no — it restores a stated premise |
| **W2** | Author the `character_layer`: one `Character`/`Actor` dataclass in `World`; resolve the 9-vs-10 attribute roster | Personal-scale modules can hold state; roster is single-valued | **yes** — OPT-AV-1 |
| **W3** | Stage 0 rank 0-1: `personal_combat` → `live` (the combat branch is dead code today), then `mass_battle`, `social_contest`, `victory` | `wiring_map_check --summary` shows those four at `live`/`gated`; each has key-log parity per its `parity` field | no |
| **W4** | Invert the two extraction pipelines: table becomes source, Python constant becomes generated view; add the `citation` column (**0 of 324 `sim_params` records carry provenance**) | Round-trip CI red on a hand-edit of a generated view; every value traces to a `PP`/`ED` | per-value collisions: **yes** |
| **W5** | Build the cook step: JSON → `.tres` for the golden path | A generated `.tres` for all 51 canonical weapons (2 exist, hand-made) | no |
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

---

## 7. Held for Jordan

1. **ED-1006 — downward Key delivery.** Blocks any downward-dispatching orchestrator. Named the
   highest-value unauthored canon; non-termination is the runtime risk.
2. **OPT-AV-1 — the attribute roster.** Blocks `character_layer`, and through it every personal-scale
   module.
3. **ED-1051 — `engine_clock`.** `doc: null` temporal spine; the sole remaining T0 blocker.
4. **ED-FA-0002 — `domain_actions` home.**
5. **ED-MB-0043 — the two-disjoint-mass-battle-trees fork.** Must resolve before W0 copies one.
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
