# Code leanness — duplication census, uncalled-code candidates, and a consolidation plan (ED-IN-0159)

## Status: REFERENCE — observation with evidence; nothing ruled, nothing executed

## Date: 2026-08-11 · Lane: IN (cross-cutting) · Baseline: `922ad1f`

**The mission this serves** (Jordan, 2026-08-11): *"make this project as lean as possible without
sacrificing mechanisms"*, where lean means **fewer files to continually track, review, edit and
audit** — not fewer bytes. **Scope is code**: `tools/`, `.githooks/`, `skills/*/scripts/`, `engine/`,
`systems/*/sim/`, `tests/`, and the `.py` committed inside `audit/`. Registers, logs and lane files
are explicitly **out of scope** — chunking those is fine.

**Method.** Read, then measure, then attack the measurement. Solo; no fan-out, no workflow. Every
figure below is from a command run against the working tree in this session. Three candidate
findings were discarded mid-analysis for method defects; §7 records them, because a census that
reports only what survived is not a census.

**Verification.** `pytest tests/valoria` 1775 passed · `valoria_local --staged` all gates passed ·
`build_engine_atlas --check` current.

---

## 1. The duplication census

**Population: 118 `.py` modules** under `tools/`, `tools/observability/`, `tools/sim_harness/`,
`.githooks/`, `skills/*/scripts/`.

### 1.1 Three shared libraries already exist. Adoption stalled.

| library | what it owns | imported by |
|---|---|---:|
| `tools/ci_common.py` | changed-file/diff plumbing, `read_text`, sim-reference roots | **11 / 118** |
| `tools/observability/obs_core.py` | ledger read, lane roster, `STATUS_RE`, needs-Jordan vocab, JS bundle writer | **9 / 118** |
| `tools/names.py` | naming gate primitives | **9 / 118** |
| `tools/registry.py` | register access | **2 / 118** |
| `tools/pathres.py` | **declares itself the SOLE PARSER** of `restructure_ledger.md` | **1 / 118** |

The problem is not an absent abstraction. It is that **the abstractions exist, are correct, and were
never adopted** — `obs_core` was built precisely to end this (its header documents the five
primitives it consolidated) and it reaches 8% of the tooling.

### 1.2 Primitive re-implementation

| primitive | independent implementations |
|---|---:|
| repo-root / path anchoring | **53** |
| YAML register load (`yaml.safe_load`) | **44** |
| staged/changed-file listing | 10 |
| `## Status:` parsing | 9 |
| the 9-lane roster | 9 |
| `restructure_ledger.md` parsing | 9 (6 genuinely parse it) |
| editorial-ledger read | 8 |
| `id_reservations` read | 8 |
| token estimation (`len//4`) | 6 |
| `PP-NNN` / `ED-NNN` regex | 6 |

### 1.3 Where the duplicates **disagree** — the consistency cost, measured

Duplication that agrees is cost. Duplication that disagrees is a defect. I tested for divergence
rather than assuming it.

**(a) `## Status:` — five live regexes, and they disagree on real files.**

| parser | pattern |
|---|---|
| `dashboard_data` | `^#{1,3}\s*Status:` — requires a hash, no space before the colon |
| `build_identifier_census` | `^##\s*Status:` — **exactly two** hashes |
| `ci_generation_consistency` | `#{0,3}\s*Status\s*:` — tolerant |
| `obs_core.STATUS_RE` | `^#{0,3}\s*Status\s*:` — the canonical one |
| `build_incompleteness` | `#{0,4}\s*Status\s*:` + a status vocabulary |

Across **551 tracked `.md`** (excluding `deprecated/`): **200 carry a Status line · 193 are read
identically by all five · 7 are DISPUTED.** The disputed set, in full:

- `workplans/valoria_master_workplan_v6.md` — **the live steering surface**
- `systems/ui/valoria_ui_ux_v4.md`
- `references/restructure_ledger.md`
- `engine/sim_reference_CONVENTIONS.md`
- `systems/combat/combat_engine_v1/README.md`
- `skills/valoria-simulator/SKILL.md`
- `audit/2026-08-06-social-contest-three-lens-audit/sources/03_consolidation.md`

Six of the seven are invisible to **both** `dashboard_data` and `build_identifier_census`; the
seventh to `build_identifier_census` alone. The failure is silent: the dashboard renders a corpus
that omits the master workplan's status and reports no error. **This is the residue after `obs_core`
already consolidated** — the divergence it fixed is documented in its own header (a GO-lane
undercount, disagreeing Status regexes), and it re-grew.

**(b) Repo-root — 15 distinct spellings for one concept.**

| spelling | sites |
|---|---:|
| `os.path.dirname(os.path.dirname(os.path.abspath(__file__)))` | 24 |
| `Path(__file__).resolve().parents[1]` | 6 |
| `os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)…` | 5 |
| `os.path.dirname(os.path.abspath(__file__))` | 5 |
| `os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))` | 4 |
| `Path(__file__).resolve().parents[2]` | 4 |
| `Path(__file__).resolve().parent` | 4 |
| …8 more spellings | 1–3 each |

`ci_common` already computes it — as `_REPO`, **underscore-private**, so it is not offered.

**(c) The 9-lane roster — 8 sites, agreeing today, diverged before.**

Verbatim `("MB","PC","FI","SC","FA","WR","IN","GO","SE")` in `ci_workplan_pointer_check`,
`broken_dependency_checker`, `handoff_atomize`, `validate_ed_citations`, `currency_consistency_check`,
plus `obs_core`'s canonical copy and two derived spellings. They agree **now**; `obs_core`'s header
records that one previously undercounted GO. **Adding a tenth lane today means editing 8 files.**

**(d) The TN-7 dice constants — five hardcodings across four files.**

Two files hardcode the **named constants** `MU_PER_DIE = 0.40` / `SD_PER_DIE = 0.80` —
`engine/autoload/sigma_leverage.py:100–101` and `audit/2026-06-03-contest-groundup/engine.py`
(the census §5 reports exactly these two). Two more hardcode **the same values as an unnamed
tuple**: `engine/autoload/dice_engine.py:56,60` and
`tests/sim/v32-combat-balance/m1_dice_sigma_core.py:28`, both as `7: (0.40, 0.800)`, plus a third
such table in `sigma_leverage.py:75`. So: **2 named + 3 tuple sites, 5 in total.** Values agree
today. The distinction matters for the remedy — a grep for the constant name finds two of five.

### 1.4 Checked and NOT found — the editorial-ledger readers

A first pass flagged that of 15 modules reading the editorial ledger, only 5 read the lane files —
implying ten tools silently see pre-cutover flat IDs only. **Refuted on inspection.** Most use the
glob `editorial_ledger*.jsonl`, which matches every lane file; my detector only recognised explicit
lane interpolation. Of the three genuine suspects: `index_gen.py`'s flat-file mentions are all in a
docstring describing its own superseded behaviour; `ci_claim_provenance_check.py`'s two filenames are
a hardcoded provenance-anchor map, not a reader; and `currency_consistency_check.py` reads the flat
file at :115 for a max-ED comparison **but globs all lane files at :152**, and documents the
limitation at :129–130. **No confirmed divergence.** Recorded because CLAUDE.md §8 still describes
`currency_consistency_check` as having a "flat-file-only ledger reader" — that description is now at
best half-true.

---

## 2. The provenance defect: 168 citations to a path that left the tree

**168 citations of `params/core.md` across 46 live `.py` files**, in the form
`# [canonical: params/core.md §Expected Value (per die), TN7]`. This is the annotation the
anti-fabrication gate is built around — the mechanism by which a constant in code names its authority.

`params/core.md` **does not exist**. It aliases `params/ → engine/params/`
(`restructure_ledger.md:720`), and `engine/params/` was **evacuated 2026-08-05** (ED-IN-0145) to fork
ref `c451bcb`. So every constant in the executable model currently cites an authority that is not in
the repository.

The 46 files span the whole executable surface: `engine/autoload/{sigma_leverage,dice_engine}.py`,
`systems/{combat,mass_battle,factions,overview}/…`, all of `tests/sim/mass_battle/`, the
`v32-combat-balance` harnesses, `tools/export_sim_params.py`, `tools/sim_harness/`, and
`skills/valoria-dice-model/`.

**The fix is available and byte-faithful.** ED-IN-0139 captured all 43 param files into
`engine/engine_params/params_tables.yaml` (669 KB) *before* the evacuation, keyed by original path —
the file literally contains `engine/params/bg/core.md:` as a key, with cells captured verbatim. So
the content is in the tree and addressable; only the pointer is stale. Repointing is mechanical, and
its falsifier is a grep count going to zero.

**This is the same disease as CLAUDE.md §0's PP-NNN finding** (433 of 452 cited patch numbers resolve
to no register), one register down: the provenance layer of the code, not the prose.

---

## 3. Uncalled code — scoped to what the evidence supports

### 3.1 What the method can and cannot see

Two independent passes: an AST import-graph (the repo's own `structure_audit.py`) and a scan for
`import X` / `python …/X.py` across every tracked text file. **Both have disqualifying blind spots
and I am not reporting either as a delete list.**

- The AST graph reported 64 orphans **including `combat_engine_v1.wrapper`**, which is demonstrably
  called (`combat_bridge.py:141`). `combat_engine_v1/` is a deliberate scripts-on-path directory whose
  internal imports are bare (`from weapons import …`), so the resolver cannot dot-qualify them.
  **Discarded.**
- The import/invoke scan reported 249 of 486 (51%) uncalled — **156 of which are `tests/valoria` and
  `tests/sim`**, which pytest collects by filename rather than importing. For those the measurement
  is meaningless. **Headline discarded**; the residue is below.

Neither sees dynamic imports or duck-typed doubles. Per §0.1 point 5, that makes grep tolerable
**only** where a guard can be written — so every item below is a *candidate for tracing*, and the
deliverable of that tracing is a guard, not a deletion.

### 3.2 Residue after correction (~93 files)

| tree | files | confidence |
|---|---:|---|
| `audit/*` probe scripts | 27 | **see §4 — these are not dead, they are unpromoted** |
| `systems/*` | 25 | low — needs per-module tracing |
| `engine/*` | 19 | low — needs per-module tracing |
| `tools/sim_harness/` | 15 | **high** — CLAUDE.md §3 independently flags the 28-file cluster as having no automated callers |
| `tools/` top-level | 6 | medium — `atomizer`, `doc_index_gen`, `valoria_rename`, `trace_execution_phases`, `build_identifier_census`, `gen_sigma_parity_goldens` |
| `skills/valoria-module-adjudicator` | 1 | low |

Four `systems/*/sim/` modules — `charter_liberties`, `home_sanctuary`, `hafenmark_equipment`,
`infrastructure_reclamation` — appeared in **both** passes. Independent rediscovery by methods with
different blind spots is the one ranking signal §10 credits, so these four are the place to start
tracing. It is **not** proof they are dead.

### 3.3 One genuine duplicate

`audit/2026-06-03-contest-groundup/engine.py` (59 lines) is a **standalone reimplementation of the
core resolution engine** — `MU_PER_DIE`, `SD_PER_DIE`, `OVERWHELM_SIGMA`, `eff_sigma`, `net_boost`,
the ED-884/ED-934 mu-shift semantics and the P-232 Ob floor — with the canonical constants hardcoded.
It is not a probe of the engine; it is a fork of it, and it cites ED and P numbers so a future reader
would reasonably treat its output as authoritative. Values match live today. Nothing would report it
if they stopped matching.

---

## 4. The audit probe scripts are not disposable — they are unpromoted instruments

I initially listed the 41 `.py` under `audit/` as clean deletion candidates. **That was wrong**, and
reading them is what showed it.

### 4.1 They still run

**38 of 41 have path anchors that all resolve.** Three are broken:
`wp_reach_authority_measurement.py` and `wt_spd_deleak_measurement.py` (both reach for
`designs/scene/combat_engine_v1`, pre-restructure) and `stageBC_test_obb_contact_toi.py` (reaches for
`audit/sim`).

I executed one. `audit/2026-07-22-combat-engine-stress-test/stress_battery.py` runs in ~110 s and
reports **22 checks: 21 PASS, 1 FAIL** —

```
## symmetry
  [FAIL] mirror-match ~50% (N=400): worst dev=0.500 @ arming/heavy p=0.000
```

A mirror match — identical combatants — returns p=0.000 for arming-sword/heavy-armour. Whether that
is a degenerate no-damage case or a genuine side bias I did not diagnose. **What matters here is that
a correctness-invariant battery covering determinism, mirror symmetry, numerical sanity, attribute
monotonicity, the upset cap and bounded runtime exists, executes today, reports a failure, and is in
no CI job.**

### 4.2 What they measure

**Class A — invariant / falsifier batteries** (belong in `tests/`):
`stress_battery.py` (22 mechanical invariants) · `grounding_battery.py` (falsifiable HEMA/physics
assertions against Williams 2003, Fiore, Talhoffer, Le Jeu de la Hache; reports MATCH/DIVERGE) ·
`symmetry_probe.py` (width-scaling side bias) · `reverse_pair_symmetry.py` (*"the cheapest invariant
the gauge has, and it fails today"*) · `topology_probe.py` (*"falsifier for every topology number
quoted in 06_master_synthesis.md"*) · `stageBC_test_obb_contact_toi.py` (an acceptance test) ·
`primitives_probe.py` (hammers the standing claim that weapon behaviour **emerges** from geometry
primitives with no weapon-name tables — the design philosophy under test) ·
`measure_colocation.py` (self-described as *"the standing measurement behind ED-MB-0056/0059"*).

**Class B — mechanism-value instruments. This class *is* the mission's own tooling:**

- `flag_ablation.py` — leave-one-out over every boolean flag: *"a flag whose removal HURTS is
  load-bearing; a flag whose removal HELPS is actively costing the historical result."*
- `harness.py` (combinatorial audit) — classifies every factor **WIRED-LIVE / WIRED-SITUATIONAL /
  DEAD** by event-divergence and win-share delta.
- `interaction.py` — pairwise lever classification: INDEPENDENT / MASKING / SYNERGY (degeneracy risk)
  / ANTAGONISM.
- `reachability_sweep.py` — per-row: *does **any** setting of the toggles move this into band?* A row
  invariant under all settings is unreachable by constants.
- `subphase_truncation_probe.py` — does the `MAX_SUB_PHASES` bound ever actually bite?

**The instrument that answers "what can we cut without sacrificing mechanisms" already exists, and it
is sitting unrun in an audit folder.** `harness.py` emits a DEAD classification per factor; that is a
strictly better dead-mechanism detector than the import-graph greps of §3, because it measures
*behavioural* deadness rather than *referential* deadness.

Relatedly, CLAUDE.md §10 lists a standing **emergence-auditor** as a watched agent-role candidate
blocked on *"once seeded headless sims + ablation are runnable."* Ablation is runnable. That blocker
is stale.

**Class C — diagnostic one-offs** (~15: `side_probe`, `side_face_probe`, `reface_probe`,
`cluster_probe`, `depth_probe`, `depth_factorial`, `granularity_probe`, `envelop_probe`,
`envelopment_stability_probe`, `close_ranks_probe`, `intent_probe`, `rout_probe`, `phasec_probe`,
`adversarial_pass`, `trace_backward`). Each localised one hypothesis for one finding. Forward value is
as **evidence for the finding they support**, not as tooling. They should stay where they are, beside
their write-ups.

**Class D — generators / drivers**: `render_scenarios.py`, `render_png.py`,
`scaled_orders_of_battle.py`, `gauge_run.py`, `run.py`, `mb_fieldbased_stress.py`,
`cannae_{historical,calib,bait}.py`. Reusable, and the historical-calibration set encodes Jordan
directives (the real Cannae OOB, 5000 v 8600, ~1.72:1) that exist nowhere else in executable form.

**Class E — retire or fix**: the 3 broken-anchor scripts, and the §3.3 forked engine.

---

## 5. The plan

Ordered by risk, not by size. **The governing constraint** — CLAUDE.md §8 already records that
migrating `currency_consistency_check`'s and `ci_audit_registry_check`'s readers onto the core was
*deliberately deferred* because "each needs its own expected-delta test, not a drop-in." That
judgment is right and generalises: **every migration of a blocking gate changes what that gate sees,
so each one ships with a test asserting the delta is the intended one.** This is why the plan is ~15
small changes and not one refactor.

### Phase 0 — no behaviour change, no judgment required

| # | Change | Falsifier |
|---|---|---|
| **0.1** | Replace the syntax-check job's hand-enumerated 32-file list with a glob over tracked `.py`. It names **32 of 108** `tools/*.py`; 76 are uncovered, including `pathres`, `handoff_atomize`, every `build_*`, and all of `tools/observability/`. | job compiles every tracked `.py`; a deliberately broken new file fails it |
| **0.2** | Repoint the **168** `params/core.md` provenance citations at `engine/engine_params/params_tables.yaml` (§2). | `grep -rn "params/core.md" --include=*.py` → 0; plus a test asserting no live `.py` cites an evacuated path |
| **0.3** | Fix or retire the 3 broken-anchor probes (§4.1). | each either executes or is gone |

### Phase 1 — one owner per primitive

**Do not create a fourth library.** Make `ci_common` the single import surface for `tools/`,
re-exporting `obs_core`'s already-canonical definitions. Each step is its own commit with its own
expected-delta test; order is deliberately cheapest-first so the pattern is proven on zero-risk
changes before it touches a gate.

| # | Change | Sites | Expected delta |
|---|---|---:|---|
| **1.1** | Publish `ci_common.REPO` (drop the underscore); migrate call sites | 53 → 1 | **none** — pure refactor. Any behaviour change is a bug |
| **1.2** | `ci_common.load_register(path)` wrapping `yaml.safe_load` + caching | 44 → 1 | none |
| **1.3** | `ci_common.LANES` re-exporting `obs_core`'s roster | 8 → 1 | none today; adding a lane becomes 1 edit |
| **1.4** | `ci_common.tokens()` | 6 → 1 | none |
| **1.5** | `ci_common.ID_RE` for `PP-NNN`/`ED-<LANE>-NNNN` | 6 → 1 | none |
| **1.6** | **`STATUS_RE` → `obs_core`'s single definition** | 5 → 1 | **NOT none — this is the one that must be asserted.** The 7 disputed docs of §1.3(a) become visible to `dashboard_data` and `build_identifier_census`. The test names all 7 and asserts they are now seen |
| **1.7** | Ledger read → `obs_core.read_ledger_entries` | 8 → 1 | per-gate expected-delta test, gates last |
| **1.8** | Make `pathres`'s SOLE PARSER claim true — migrate `broken_dependency_checker`, `build_identifier_census`, `ci_claude_workflow_paths`, `evacuation_plan`, `build_incompleteness`; **or delete the claim** | 6 → 1 | alias resolution identical on every current input |

A single-owner comment asserting a property the tree lacks is worse than no comment — it stops the
next reader from looking. 1.8 resolves that either way.

### Phase 2 — promote the instruments (delete nothing)

| # | Change | Falsifier |
|---|---|---|
| **2.1** | Promote Class A batteries into `tests/valoria/`. The `stress_battery` mirror-match FAIL and `reverse_pair_symmetry`'s known failure land as **`xfail(strict)` citing an ED** — a tracked failure, not a silent one | suite still green; removing an xfail marker turns it red |
| **2.2** | Promote Class B into a standing `tools/mechanism_census.py` — one owner over `flag_ablation` + `harness` + `interaction` + `reachability_sweep`, emitting a per-mechanism verdict (LOAD-BEARING / SITUATIONAL / DEAD / COSTING) | it reproduces each probe's published numbers on the same seeds |
| **2.3** | Run it. **Its output is the input to any decision about cutting mechanisms** — behavioural deadness beats referential deadness | a DEAD verdict is reproducible across seeds |
| **2.4** | Re-open the §10 emergence-auditor candidate, whose blocker ("once ablation is runnable") is stale | — |

### Phase 3 — uncalled code, guarded

| # | Change | Falsifier |
|---|---|---|
| **3.1** | Trace the 4 doubly-rediscovered `systems/*/sim/` modules (§3.2). Deliverable is a **guard**, not a delete | a test that fails if a live caller appears/disappears |
| **3.2** | Rule on `tools/sim_harness/` (28 files, 15 uncalled): promote the `pr119_governance` adapters or retire to `deprecated/tools/`, mirroring the 2026-07-09 precedent | nothing in CI/hooks/skills references it — re-confirm by grep before moving |
| **3.3** | Retire the forked engine (§3.3), or pin it to the live constants with a test that fails on divergence | mutate `MU_PER_DIE` live → the test fails |
| **3.4** | Then, and only then, the remaining `systems`/`engine` residue | per-module |

### What this is worth

**Not a large file-count reduction.** Phase 1 removes ~0 files; Phase 2 *adds* one owner while
retiring nothing; Phase 3's honest ceiling is the 15 `sim_harness` files plus whatever tracing
confirms. If the goal were file count alone, this plan would be a poor investment.

**It is a large edit-surface reduction**, which is the stated concern: the number of files you must
touch to change one rule goes 53→1, 44→1, 8→1, 6→1, 5→1. Adding a lane goes from 8 edits to 1.

**And it closes one live correctness class** — the seven documents whose status two tools cannot see —
**and one live provenance class** — 168 constants citing an evacuated authority.

---

## 6. Falsifiers

| claim | command |
|---|---|
| Status regexes disagree on 7 real files | run the five patterns over `git ls-files '*.md'`; union 200, intersection 193 |
| 168 citations to an absent path | `duplication_census.py` §2 → 168 across 46 files; `ls params/core.md engine/params/core.md` → both absent |
| the capture can absorb them | `grep -n "core\.md" engine/engine_params/params_tables.yaml` → key `engine/params/bg/core.md:` present |
| syntax gate covers 32 of 108 | diff the job's file list against `git ls-files 'tools/*.py' 'tools/**/*.py'` |
| the probes still run | `cd audit/2026-07-22-combat-engine-stress-test && python3 stress_battery.py` → 22 checks, 1 FAIL |
| `pathres` is not the sole parser | `grep -rln restructure_ledger tools/**/*.py` → 6 files |
| §3's orphan lists are unsound | `combat_engine_v1.wrapper` appears in the AST orphan list and is called at `engine/cross_scale/combat_bridge.py:141` |

## 7. What I discarded, and what I did not verify

**Discarded mid-analysis** (method defects, recorded so they are not re-derived):

1. **AST orphan count (64).** Cannot dot-resolve `combat_engine_v1`'s bare imports; reported a
   demonstrably-live module as an orphan.
2. **Import/invoke orphan count (249 / 51%).** 156 of them are pytest-collected test files, for which
   "never imported" measures nothing.
3. **"Ten ledger readers miss the lane files."** An artifact of my pattern detector not recognising
   the `editorial_ledger*.jsonl` glob (§1.4).

**Not verified:**

- The `stress_battery` mirror-match FAIL is **reported, not diagnosed.** It may be a degenerate
  no-damage case rather than a side bias. It needs a real look before it becomes an xfail with an ED.
- The other 40 probes were read but only **one** was executed. "38 anchors resolve" is a static
  check, not proof they run.
- The 25 `systems` + 19 `engine` candidates are **unconfirmed**; only 4 have two-method agreement.
- I did not measure how much of `tests/valoria`'s 153 modules is itself duplicated — the largest
  single code tree in the census population, deliberately left out of scope because pytest collection
  defeats the reference-based method used here.
- Phase 1's "expected delta: none" claims are **predictions**, not measurements. Each is exactly what
  its own migration test must establish.

---

## 8. Fable-5 read-only second pass — two of my findings overturned, five new confirmed

A `valoria-critic` agent (read-only: Read/Grep/Glob, no Bash, no writes — structural independence
per §10) was given this document and the consolidation sweep as **prior art to attack**, and asked to
work the lines they left uncovered. Its findings are adjudicated below. **I re-ran every load-bearing
claim with Bash**, which it could not; the verdicts are mine, the discoveries are its.

### 8.1 OVERTURNED — §3.2's four "possibly-uncalled" modules are reached, and my ranking signal was wrong

§3.2 named `charter_liberties`, `home_sanctuary`, `hafenmark_equipment` and
`infrastructure_reclamation` as the place to start tracing, on the strength of **two independent
methods agreeing** they were uncalled — invoking §10's rank-by-independent-rediscovery.

**All four are reached by a blocking test.** `engine/tests/test_pipeline_reach.py:749-755` lists them
in `_OI17_FULL_MODULE_ENTRYPOINTS`, and `test_oi17_full_module_conversions_are_stub_wired` (`:767-779`)
asserts each resolves as `stub_wired`. Re-run here: **1 passed.** All four are `stubwire.stub_resolve`
no-ops (`charter_liberties.py:27-32`, `home_sanctuary.py:29-42`, `hafenmark_equipment.py:30-35`,
`infrastructure_reclamation.py:29-34`) whose docstrings hold Jordan directives recorded nowhere else —
`home_sanctuary.py:5` (the T9 Ob +4 / 12-season exit condition), `infrastructure_reclamation.py:5`
(the attacker/defender pool formula). **Deleting any of them fails CI and destroys design content.**

**The reasoning error matters more than the wrong answer.** Both my methods were blind to *the same
thing* — `test_pipeline_reach.py` dispatches by **string module path**, invisible to an AST import
graph and to an `import X` grep alike. "Independent rediscovery" is a ranking signal only when the
blind spots actually differ; mine were correlated, so the agreement carried no information. I flagged
this hazard in §3.1 and then walked into it one section later.

**Phase 3.1 is therefore closed, not started** — the guard it asked me to write already exists, and
it is `test_pipeline_reach.py`. Any further tracing in `systems/`/`engine/` must grep string-form
module paths, not imports.

### 8.2 OVERTURNED — the apparatus registry's orphan count is an undercount by construction, and §F5 inherited it

`tools/build_apparatus_registry.py:213-220`: `invoked_by()` tags a tool `ci:<workflow>` if its
**basename appears anywhere in the workflow text**, and `:306-307` then sets `orphaned=False` for any
such tag. The syntax-check job is a bare `py_compile` list — so **being compiled counts as being
invoked.** Confirmed in the output: `references/apparatus_registry.md` reports `index_gen.py` (:90),
`atomizer.py` (:32), `doc_index_gen.py` (:83) and `valoria_rename.py` (:104) as "Invoked by
ci:valoria-ci.yml", while the registry's *own* row 165 — enumerating what `valoria-ci.yml` actually
invokes — lists none of them.

**This invalidates a number I used.** The consolidation sweep's F5 corrected CLAUDE.md's stale
"36 of 106 modules have zero automated callers" by citing "123 entries, 6 orphaned" from this
registry. The staleness of CLAUDE.md's figure stands; **my replacement figure does not.** Neither
number is a valid orphan census. F5's claim is narrowed to what remains true: the row is stale and
unguarded, and the correct count is *not currently computed by anything*.

### 8.3 The fold-in found a defect in my own plan: Phase 0.1 would destroy the orphan signal

§5 Phase 0.1 proposes replacing the syntax gate's hand-enumerated 32-file list with a glob. Measured
now: **46 of 108** `tools/*.py` have their basename somewhere in `valoria-ci.yml`. Under a glob that
becomes **108 of 108**, and by §8.2's mechanism `invoked_by()` would mark **every tool non-orphaned** —
silently zeroing the census.

**Phase 0.1 is amended:** glob the syntax job **and** exclude the syntax-check job from
`invoked_by()`'s scan in the same commit, with a test asserting a known-dead tool still reports
orphaned. Shipping the two halves separately makes the registry worse than it is today. This is the
§8-invariant hazard in miniature — a remedy for one gate corrupting a different gate's input.

### 8.4 CONFIRMED — dead code inside a blocking gate's file

`tools/compliance_check.py` calls **two functions that do not exist**: `_lazy_import()` at `:165` and
`check_all()` at `:306` (`grep -c 'def _lazy_import\|def check_all'` → **0**). Executed here:

```
$ python3 tools/compliance_check.py
  File "tools/compliance_check.py", line 306, in <module>
    violations = check_all()
NameError: name 'check_all' is not defined
```

The **live CI mode** (`--check-only --repo-state .`) is fully inline and unaffected — which is why
this has survived — but the file is half dead-on-arrival, and it is a **blocking gate's** file. No
census row records it, mine included.

It is one leg of a coherent inert cluster the agent assembled:

- The only skeleton/index policy rule targets `designs/**/*.md` (`references/atomization_rules.yaml:243-249`)
  — a tree **retired 2026-07-19**, so it matches nothing.
- `_check_index` reads `require_index_above` (`compliance_check.py:166`), a key absent from
  `atomization_rules.yaml`, whose rule uses `require_skeleton_above` (`:245`).
- `doc_index_gen.py` has no importers and no invocation beyond `py_compile`, while its **37 outputs**
  at `systems/**/*_index.md` carry **no freshness guard of any kind**.

Retiring `atomizer.py`, `doc_index_gen.py`, `index_gen.py` to `deprecated/tools/` and excising the
dead functions is a clean −3 files plus dead code out of a blocking gate. **Coupled edit:**
`tests/valoria/test_compliance_on_exceed_vocabulary.py:98-99` asserts `_on_exceed_severity(` appears
≥3 times, counting `_check_size` as one site. The 37 `*_index.md` files are a **Jordan call** — the
2026-07-26 ruling grandfathered existing pairs.

`index_gen.py` is separately dead on its own evidence: zero importers, and its only artifact carries
`<!-- auto-generated by index_gen.py — 2026-05-10T20:34:39Z -->`
(`registers/patch_register_index.md:3`) — untouched for three months. **Keep `valoria_rename.py`**: it
is the designated executor of `proposals/canonical_nomenclature_v1.md:231`.

### 8.5 CONFIRMED — three more single-owner opportunities in the gate tier

- **Two blocking size-cap gates overlap on one policy file.** `compliance_check`'s CI mode walks every
  `.md`/`.yaml` against `atomization_rules.yaml` (`:257-284`); `ci_register_size_check` enforces a
  hand-maintained `THRESHOLDS` dict, three of whose entries are read *from that same file* precisely
  because they kept drifting (`ci_register_size_check.py:39-48`, recording three incidents, ED-IN-0097).
  `tests/coverage_matrix.md`, `patch_register_active.yaml` and `module_contracts.yaml` are size-checked
  **twice per CI run by two tools**. Unique to `ci_register_size_check`: the `.jsonl` caps (`:81-125`),
  since compliance's walk skips non-`.md`/`.yaml` (`:259`). **Mechanism that must survive a merge:**
  `ci_register_size_check` runs in `valoria_local` and `compliance_check` deliberately does not
  (`ci_checks_registry.yaml:262` — "local-green != compliance-green"), so a merge must add the merged
  gate locally or local coverage regresses.
- **Two always-exit-0 tools sit in the BLOCKING job.** `ci_audit_registry_check`
  ("Always exits 0 by design", `ci_checks_registry.yaml:113`) at `valoria-ci.yml:132`, and
  `ci_supersession_check` ("Never fails the build", `:248`) at `:129`. Moving both to
  `validators-report` changes no behaviour and makes the blocking tier's membership truthful.
- **`ci_names_consistency.py` is a self-declared migration babysitter** (`:4-9`): it exists only while
  `descriptor_registry.yaml` / `proper_noun_registry.yaml` still carry mirror `name`/`canonical`
  fields, and says removing them is the follow-up. Finishing it retires a blocking gate, its CI line,
  its `valoria_local` row, and two registries' mirror fields.

### 8.6 CONFIRMED — `ci_checks_registry.yaml` documents a file that does not exist

`valoria_hooks.py` is **absent from the tree** (`find` → nothing), yet the registry — which calls
itself the single source of truth — references it **5 times**, including its level-4 definition
(`:14`), its field definitions (`:21-22`), and an entire `in_session_hooks` section (`:345-428`, ~18
hooks, some describing the ED-1084-retired checkpoint machinery at `:422-424`). Every `paired_hook:`
field on the live CI entries points into it. ~90 lines describing an enforcement level that does not
exist. Pruning changes nothing enforced.

### 8.7 Reframed, not discovered — two "duplications" that are ruled or docketed

- **The mass-battle dual engine** (§D of the brief, the highest hope for a real consolidation) is
  already docketed as **ED-MB-0065** with three measured blockers and a guard
  (`tests/valoria/test_j2_mass_battle_seam.py`), awaiting WITHDRAW/DEFER/EXECUTE. The feared *third*
  copy does not exist — the v22 source named at `systems/mass_battle/sim/massbattle.py:16` is already
  gone from disk. **Nothing new to propose.**
- **Personal combat is duplicated by design**: the DEPRECATED v30 resolver (`systems/combat/sim/combat.py:4-11`)
  is still the default campaign path (`engine/mc_v18.py:75`, `scene_dispatch.py:273`) while
  `combat_engine_v1` sits behind a default-OFF flag. Retiring the old resolver removes a whole
  duplicate mechanic — but the gate is **flag ratification, a design decision**, not a leanness edit.

### 8.8 `tests/valoria` — the tree I left out of scope

The agent sampled ~15 of 153 modules, chosen adversarially by name collision, and found **no
superseded or duplicate-fact modules**: every suspicious pair resolved to distinct, ED-cited, live
purposes (the three "pins" files guard three different facts; the three geometry files, three
different EDs). The real duplication is **boilerplate**: `conftest.py` is only the KNOWN_RED register
(`:35-65`), so **32 files repeat an identical `ENGINE = …combat_engine_v1` + `sys.path.insert` block**,
≥7 more repeat a `_SIM` block, and ~10 define local `_unit()` factories with differing defaults. One
conftest helper collapses the path setup; the factories need case-by-case judgment. **Zero files
removed, ~40 edit-sites collapsed.**

**And the instrument to finish the job already exists** — `references/test_register.json`, 132 files /
1,186 tests with a per-row "what it guards", generated and drift-gated blocking since ED-IN-0142
(`tests/valoria/test_test_register.py`). §7's "deliberately left out of scope because pytest
collection defeats the reference-based method" was true of *my* method and not of the repo's: the
same-fact analysis is a query against a register I did not know to use.

### 8.9 Amendments to §5

| # | change |
|---|---|
| **0.1** | **AMENDED** — glob the syntax job **and** exclude it from `invoked_by()` in the same commit (§8.3), with a test that a known-dead tool still reports orphaned |
| **0.4** | **NEW** — excise `_lazy_import`/`check_all` and the unreachable interactive branch from `compliance_check.py`; update `test_compliance_on_exceed_vocabulary.py:98-99` in the same commit |
| **0.5** | **NEW** — retire `atomizer.py`, `doc_index_gen.py`, `index_gen.py` to `deprecated/tools/`; delete the dead `designs/**` policy row |
| **0.6** | **NEW** — prune `in_session_hooks` / `paired_hook` from `ci_checks_registry.yaml` (§8.6) |
| **1.9** | **NEW** — merge the two size-cap gates onto the policy file, extended to `.jsonl`, **and add the merged gate to `valoria_local`** (§8.5) |
| **1.10** | **NEW** — move the two always-exit-0 tools to `validators-report` |
| **1.11** | **NEW** — finish the `ci_names_consistency` migration and retire the gate |
| **2.5** | **NEW** — one `conftest.py` path helper for the 32+7 bootstrap blocks (§8.8) |
| **3.1** | **CLOSED** — the guard already exists (§8.1) |

### 8.10 Still unverified

**F10 (PLAUSIBLE, not confirmed):** `tools/evacuation_plan.py:164-165` keeps the whole
`tests/sim/v32-combat-balance/` prefix as the parity oracle, but the actual consumers name only
`m1_dice_sigma_core.py` (`tools/gen_sigma_parity_goldens.py:9,91-94`;
`engine/tests/test_sigma_leverage_parity.py:11`; `build_fork.py:70-71`). Every out-of-directory hit on
the other ~25 module names was a substring false positive. **Do not act on this** until a
`MEASURED-BY:`/prose citation sweep confirms nothing cites the m2–r10 stations — moving a cited
instrument turns `ci_claim_provenance_check` red. Ceiling is ~26 files *relocated*, zero deleted.

Also unreached: 138 of 153 `tests/valoria` modules (use `test_register.json`), and the 25 `systems` +
19 `engine` low-confidence candidates from §3.2 — which, after §8.1, need string-path grepping rather
than import analysis.
