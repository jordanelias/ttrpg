# Centralization & Single-Ownership Orchestration Plan v1

## Status: PROPOSED (merge ratifies per ED-1094, EXCEPT the §6 held-back forks — those are Jordan's alone) — ED-IN-0103, 2026-07-29

**Lane:** IN (infrastructure / cross-cutting). **Companion program to ED-IN-0091.**
**Pointer:** `workplans/POINTER_2026-07-29_centralization_single_owner.md` (Jordan's 2026-07-29
plans-in-workplans directive — every plan gets direct placement or a pointer).

**Provenance.** Authored from four read-only reconnaissance lanes over the working tree, planned by a
Fable-tier planner, then attacked by **two structurally independent read-only critics**
(`valoria-critic`, no write tools by construction) on disjoint lenses — one fact-checking every number
against HEAD, one attacking directive coverage and cross-program collision. A **third pass** then
attacked the *committed* artifacts — including the review record's own claims about what it had
fixed — and found that one of them was false (§2.4). **Three passes, six critics, 65 findings, 20 P1.**
Every one is reconciled below or recorded in `02_adversarial_review_2026-07-29.md`. Numbers here are
post-third-pass; the earlier drafts' counts were wrong in **eleven** places, each corrected in place
with the correction stated rather than silently applied.

---

## §0 · Relationship to the existing program

**Decision: a SEPARATE program, sequenced against ED-IN-0091's waves — not new waves W6+, not a
deepening of its Wave 4.** (1) ED-IN-0091's register/plan/disposition-map declare themselves
**immutable snapshots** whose corrections land only in `04_execution_ledger.md`; appending W6+ would
violate its own governance. (2) Different in kind: its Wave 4 executes *enumerated, known* rows
(OI-51/52/53/54/57/15/16); this program builds the *ownership and detection infrastructure* — WS1
completion, a lane table, a rework-flag convention, a duplication detector, and formula-ownership
repair — that no register row fully names. (3) Separate disposition maps keep each capstone's diff
honest.

### 0.1 Cross-program interlocks (BINDING — filed as routing rows in `04_execution_ledger.md` at W0, before any W1 work)

| # | Interlock | Term |
|---|---|---|
| 1 | **`tools/registry.py` retirement race** (critic B-F13) | ED-IN-0091 W4 item 5 offers "give the facade a consumer **or retire it**." If retirement executes first, this program's W1.3 and §1 predicate 2 lose their subject, and the ED-1082 grep-then-move precedent would find no consumers *precisely because W1 has not run*. **Corrected (critic C-F3):** the v1 text said W0 would add a stop-condition to ED-IN-0091 §4 — but §4 lives inside a file that program declares an **immutable snapshot**, which is this plan's own §0 reason (1) for not appending waves to it. Editing it would contradict the reason we are a separate program. **The executable form:** the interlock is expressed entirely in `04_execution_ledger.md` (the declared, writable status surface) as a `[CSO]` **blocking row** that ED-IN-0091's W4 must read before its item 5, and this plan is cited from that row. Honest label: this is **protocol on a shared writable surface**, which is stronger than prose but weaker than a gate. Making it a true gate needs Jordan to carve an amendment exception — §6 row 9. |
| 2 | **OI-40 scale reconciliation** | ED-IN-0091 W3 item 3 owns the IN-half. This program's W4 scale-binding *consumes* that outcome (or §6 row 1's ruling); it never re-derives it. |
| 3 | **`structure_audit.py` file-level overlap** (critic B-F9) | ED-IN-0091 W4 item 5 consolidates the `__main__`-guard predicate in the same file this program's W2.3/W2.4 edit. Logical scopes are disjoint; the *file* is not. Routing row names the file and states **ED-IN-0091 W4 merges first**; this program rebases. |
| 4 | **ED-IN-0073 character-decision remediation** (critic B-F6) | Its Phase 1 relocates `systems/characters/` → `systems/character/{generation,conviction,beliefs}/`, repoints 5 `descriptor_registry` entries + `module_contracts` `piety_track` `doc:`, and indexes into `values_master.yaml`. **A lane table cannot be authored against paths about to move.** W0 establishes its state: if dormant, cite that; if live, **W4's lane-table seeding waits on its Phase 1 or excludes `systems/characters/**` with a stated reason**. `values_master.yaml` gets a named single writer either way. Silence is not a disposition. |
| 5 | **`04_execution_ledger.md` two writers** (critic B-F7) | ED-IN-0091's shared-file single-writer table does not cover the ledger, because at authoring time it had one writer. This program adds the second. **Term: every row this program appends carries the `[CSO]` prefix in column 1, appended at end-of-table only.** W5 capstones diff both prefixes. |
| 6 | **ID partition** (critic B-F8) | 19 IN IDs (`0093–0111`) remain for **two** concurrent programs against a **frozen** reservations file — the exact unpartitioned-block collision class the lane namespace exists to prevent. **Term: ED-IN-0091 keeps `0093–0102`; this program takes `0103–0111`.** Recorded as a `[CSO]` ledger row at W0. Costs one line; makes collision impossible by construction. |
| 8 | **The three silently-dead gates** (§2.0; critic C-F9/C-F10) | `ci_formula_prose_check.py:87-89`, `canon_coverage_check.py:67` and the BLOCKING `validate_ed_citations.py:91,108,278` are dead-root instances in neither program's W4-item-3 list. Routing row names all three, assigns the **repoints + guards** to this program's W1/W2, and leaves ED-IN-0091's four enumerated sites with it. Without this row the §2.5 claim "added to both programs' scope" is filed by nothing. |
| 7 | **Reservation text is knowingly stale** (critic A-F9) | `id_reservations.yaml:225` scopes the block "for the ED-IN-0091 code-shape run." The file is frozen, so it is not amended. W0's ledger row is the record of the second consumer; the reservation comment is reconciled at ED-IN-0091's W5 capstone when the freeze lifts. |

**`registers/review_baseline.yaml`** — IN is sole writer among live sessions. This program's seedings
are separate, explicitly-ED'd PRs that never interleave with ED-IN-0091's W1 `stubs.count` seeding or
W4 `vocab.a17` protocol. A baseline **raise** is an explicit ED with a loud ED-1094 call-out, never
silent.

**What this program does NOT touch:** `systems/combat/**`; `tests/sim/mass_battle/**`;
`faction_action.py:349` (declared seam); `references/id_reservations.yaml`; any live lane's
`HANDOFF_<LANE>.md`; goldens outside the IN family; any D row or §5 fork of ED-IN-0091; ED-IN-0091's
five folder documents.

### 0.2 A directive conflict, recorded not silently resolved (critic B-F17)

Jordan's tiering directive reserves Fable for "planning and orchestration and highest level of
auditing/**synthesis**/digestion." CLAUDE.md §10's Fable row rules the opposite: "Read-only audit ·
planner · orchestrator · guardrail. **NOT synthesis or artifact authorship** (RULED 2026-07-28,
Jordan)." **This plan follows §10** — Fable appears only as the planner, the orchestrator, and W5's
read-only top-level audit; every artifact is authored by Sonnet or Opus. Recorded here so the
directive does not look unexecuted at capstone. If Jordan intends the 07-28 ruling relaxed, that is
§6 row 8.

---

## §1 · Acceptance — what "single ownership is enforced" means

Eight predicates, each with a named instrument. Predicate 8 exists because the pre-critic draft
dropped the **formula** half of the directive entirely (critic B-F1).

| # | Predicate | Instrument |
|---|---|---|
| 1 | **One parser per ownership-layer YAML.** `names_index.yaml`, `descriptor_registry.yaml`, `module_contracts.yaml` each `safe_load`-parsed by exactly one module; every other consumer imports the loader. Today: `ci_names_consistency.py:45` re-parses descriptor_registry; `quantity_registry.py:66` re-parses names_index; **19–21** files parse module_contracts (count rule: parse-sites, not mentions), **plus `wiring_map_check.py:45` which parses it by REGEX** and needs a `module_ids()` accessor, not a `safe_load` swap (critic A-F5) | `tests/valoria/test_sole_reader.py` (new) |
| 2 | **`tools/registry.py` is a real owner.** Both `ci_quantity_vocabulary_check.py` and `ci_formula_prose_check.py` resolve through the facade — **both, not either** (critic B-F14); verdicts byte-identical on the current corpus | `test_registry.py` + corpus verdict-parity capture. **NOT `apparatus_registry.orphaned`** — that flag already reads `false` because the detector counts the module's own unit test as an invoker (critic A-F7); fixing that classification is W2.6 |
| 3 | **No phantom authority.** Zero DEAD path references in `tools/**` and `skills/**/scripts/**` **source** — docstrings *and executed path constants*, carrying `ci_claude_workflow_paths.py`'s two-policy split: ALIASED is tolerable in prose, **FATAL in an executed expression** (critic B-F10). Scope covers **3 in-scope sites** for the `references/registry/*` class; append-only ledger + frozen-audit citations are explicitly excluded from repointing (critic A-F6) | **TWO instruments, split (critic C-F4)** — `build_incompleteness.scan_retired_tree_pointers` (scope widened) owns **retired-tree** pointers, and its `RETIRED_TREES = ("designs/","sim/")` regex *structurally cannot* match a never-existed path like `references/registry/README.md`; the nonexistent-path class is owned by the LIVE/ALIASED/DEAD resolver `ci_claude_workflow_paths.py:17-22` already declares. The v1 draft named only the first and would have shipped a falsifier its own instrument could not observe. Both feed review_core `paths.dead` |
| 4 | **Rework debt is machine-visible and ratcheted.** Every "built wrong / wrong lane / second owner" block carries `[REWORK ED-…]`; `build_decisions` ingests it; `review_core --check` counts it | `tests/valoria/test_rework_flag.py`; signal `rework.count` |
| 5 | **Duplication is detected by instrument.** Two signals: same-name-divergent-value module constants, and normalized-AST-identical function bodies — over a **declared corpus scope** (§2.3) | `test_structure_audit.py::test_dup_known_answer`; signal `dup.count` |
| 6 | **Every governed path has exactly one lane row.** `references/lane_ownership.yaml` covers all live roots; `build_decisions.LANE_PATH_PREFIXES` imports it, killing **44 dead prefixes — 41 `designs/` and 3 `sim/`** (critic A-F4; the `sim/` roots are a *second* retired tree, not a `designs/` variant — critic B-F12) | `tools/ci_lane_scale_check.py` known-answer tests; signals `lane.unmapped`, `lane.misplaced` |
| 7 | **Size-cap thresholds live once** — scoped to the **13 non-`.jsonl` paths**. ⚠️ `atomization_rules.yaml:113-115` states outright that "size caps for all ledger files live in `tools/ci_register_size_check.py`'s THRESHOLDS, **not here**" — a deliberate single-owner assignment in the *opposite* direction covering the 13 `.jsonl` paths. The v1 predicate would have silently reversed a documented ruling (critic C-F8); reversing it is now §6 row 10, not an implementation detail | `tests/valoria/test_size_limits_single_sourced.py`, generalizing `test_coverage_matrix_threshold.py` from one entry to the pattern |
| 8 | **Formula single-ownership is actually measured.** `ci_formula_prose_check.py` scans a **non-zero** census; every registered quantity has one `defining_surface`; every other carrier cites or textually matches it | the checker itself, with a guard asserting `rows > 0`; signal `formula.drift` |

---

## §2 · Primitives — ruthlessly preferring extension over new owners

### 2.0 The silently-dead-gate class — THREE instances, one blocking (expanded post-critic)

The buried lede is not one dead tool. It is a **pattern defect** in the §0.1-point-5 sense: each of
these was correct when written and stopped working because `designs/` was retired on 2026-07-19.
All three pass CI today while scanning nothing.

| # | Gate | Tier | Evidence | Signature |
|---|---|---|---|---|
| 1 | `tools/ci_formula_prose_check.py` | report-only, **the only formula-ownership instrument** | `DEFAULT_CENSUS` (`:87-89`) points into retired `designs/`; the census lives at `audit/2026-07-08-attribute-value-coherence-audit/02_census/quantity_census.yaml`; `load_census` (`:191-193`) returns `[]` on a missing path **without raising** | prints `0 census-drift + 0 live-drift findings across 0 formula-bearing quantities`, exits 0 |
| 2 | `tools/canon_coverage_check.py` | report-only, CI job `canon-coverage-check` | `DESIGNS_DIR` (`:67`) = `<repo>/designs`, which does not exist | prints `Unregistered with header: 0 / Registered without header: 0 / CLEAN — no drift detected` — where `references/ci_checks_registry.yaml` records its last real measurement as **1 unregistered-with-header + 28 registered-no-header (2026-07-11)**. The drift was not fixed; the scanner went blind |
| 3 | `tools/validate_ed_citations.py` | **BLOCKING** (`valoria-ci.yml`, in `ci-summary`'s `needs`) | `_walk_repo_files()` (`:278`) walks `('canon','designs','params','references','archives','deprecated')` — `designs/`, `params/`, `archives/` do not exist — and **never walks `systems/` or `engine/`** despite `SCAN_PREFIXES` (`:108`) declaring both. `WORKING_PREFIXES` (`:91`) is the dead `('designs/audit/', 'workplans/')` | the ED-citation gate effectively covers `canon/` + `references/` + `deprecated/` only |

**Precision, stated exactly** (critic C-F11): #1 is **dead by default**, not unconditionally — a
`--census` override exists at `:446`, but **no live invocation passes it**: CI runs
`python3 tools/ci_formula_prose_check.py --report` (`valoria-ci.yml:316`) and `valoria_local.py:43`
passes an empty arg list. `tests/valoria/test_ci_formula_prose_check.py:201-203` invokes `main()`
against the live tree and asserts only `== 0` — a green test over a zero-row scan, which is the
§0.1-point-2 failure reproduced inside the test suite.

**Fix, per §0.1 point 5 — one owner, every site routed through it, and a guard that fails on
recurrence.** The repoints are one-liners; the guards are the deliverable: `assert stats['rows'] > 0`
for #1, an equivalent non-empty-corpus assertion for #2, and `assert scanned_docs_under('systems/') > 0`
for #3. **Do not fix these three as one-offs** — that is precisely what produced them. The
detection-side sweep is §2.5.

**Sizing is unknown at plan time and stays unknown.** Because #1 and #2 have been blind, nobody knows
how much formula drift or canon-coverage drift exists. §1 predicate 8's first real measurement is a
W1 deliverable, not a plan-time number (§9 risk 4).

### 2.1 WS1 step 1.5 — ADOPTED as extension of existing owners; NO new module
Not the end-state flip (held, §6 row 3). (i) Route **both** vocabulary checkers through
`tools/registry.py`; (ii) `ci_names_consistency.py` imports `descriptor_registry.py`'s loader,
`quantity_registry.py` imports `names.py`'s loader; (iii) author `references/registry/README.md`
(PROPOSED, **held back loudly** — merging W1 does NOT ratify the flip) + generate
`pointer_debt_worklist.md` from `pointer_audit.py`'s real Category B/C output, closing the 3 in-scope
dangling citations. **Falsifier:** `test_sole_reader.py` + verdict parity.

### 2.2 Lane/scale ownership table — ADOPTED; the program's ONE new data artifact
`references/lane_ownership.yaml` (`{path, lane, status: assigned|declared_seam|misplaced|unassigned,
note, provenance}`) + `tools/lane_ownership.py` (sole reader) + `tools/ci_lane_scale_check.py`
(report-only). **Why not extend:** `lane_assignments.yaml` is the retired Lane-A/B/C concept with its
own collision warning and dead globs; `build_decisions.py` self-disclaims exhaustiveness at lines
66–69 and 79–87. Verified by critic: **no lane checker exists anywhere**; this is not a
re-implementation. **Falsifier:** two-lane fixture fails uniqueness; planted unmapped file reported.

### 2.3 Duplication detector — ADOPTED as a `--dup` mode on `structure_audit.py`; REJECTED as a new tool
`structure_audit.py` already owns the corpus AST walk; a second walker would be a second owner.

**CORPUS SCOPE IS THE DESIGN, not a detail (critic A-F1/A-F2).** The pre-critic draft predicted the
byte-identical `compute_degree` pair would be ~2 sites. **Measured: 26 definitions**, 24 of them in
`tests/sim/sim_mb_06_v5.py … v25.py` — a frozen versioned-snapshot harness corpus. A detector run
without scoping reports ~25 "duplicates" of one function and the stop-rule aborts the wave on the
plan's own wrong prediction. Worse, those files sit under `tests/sim/` but **not**
`tests/sim/mass_battle/`, so they were simultaneously in-scope for detection, out-of-scope for MB
inbound routing, and unprotected by the W5 no-touch assertion.

**Term:** `tests/sim/**` and `tests/sim_framework/**` are a **declared frozen-harness allowlist**,
excluded from `dup.count` and named in the detector's own output as excluded-with-count (never
silently dropped — CLAUDE.md §8's no-silent-caps rule). Live scope is `engine/**`,
`systems/**` (minus the two carve-outs), `tools/**`, `skills/**`.

⚠️ **The detector is designed NOT to report its own motivating example — say so, don't discover it
later (critic C-F5).** Corrected census: **26 definitions — 23 in `sim_mb_06_v*`, 25 under
`tests/sim/**`, exactly 1 in live scope** (`systems/mass_battle/sim/massbattle.py:640`); **25 are
mutually AST-identical**, `tests/sim/sim_mass_battle_SIM-MB-05.py:45` diverges (typed signature +
docstring, which survive `ast.dump`). So under filter 1 only one definition is in scope, and one
definition is not a duplicate. Under filter 2 the body is **four** top-level statements (three `if`s
+ a `return`), **below the ≥5 floor**. `dup.count` contribution from `compute_degree` is therefore
**zero, by design.** The cluster is a **hand-routed §6 row 5 item**, not a detector output — which
also means §9 risk 1's stop-rule must be calibrated against the detector's own expected yield, not
against this cluster.
**"Statement" is defined as top-level statements in the function body** (not recursive), and the ≥5
floor is a **plan-time assumption, not a measurement** — W2 stage 3 must justify it against a
measured false-positive rate before the signal is seeded.

⚠️ **Plan-time estimates, to be re-derived in W0 (critic C-F15).** The following ship without a
committed instrument and are explicitly NOT results: "45/102 value collisions", "`3.0` recurs 24×",
"19–21 module_contracts parse-sites" (a **range is an admission the count was never nailed down** and
must become a number with a stated counting rule before it enters an acceptance predicate), and the
58-file triage totals. W0 stage 1 lands the counting script that prints each; until then they are
leads. `03_plan_liveness_triage.md` is the triage's committed manifest.

Signals: (1) same-NAME module-level ALLCAPS constants with divergent values (allowlist `SCHEMA_VERSION`
+ test seeds — verified genuine false positives, 3 unrelated schemas); (2) `ast.dump` hash equality,
names normalized, docstrings stripped, ≥5-statement floor. **Same-value grouping is NOT emitted**
(measured useless: 45/102 collisions; `3.0` recurs 24× across unrelated concepts). Third-party tools
rejected — CI installs only `pyyaml`+`pytest`; jscpd needs a Node toolchain and mis-fires on a corpus
whose dominant mode is "same concept, independently re-derived."
**Falsifier:** planted fixture both directions; allowlist exercised (`assert checked >= N`); live
count reconciled against W0's re-derived census.

### 2.4 `tools/contracts_store.py` — ADOPTED, one new small module
The heaviest re-parse concentration, with `from:`-normalization inlined **at least four times**:

| site | form |
|---|---|
| `skills/valoria-vector-audit/scripts/structure_audit.py:378` | `_as_list()` helper |
| `tools/observability/build_graph.py:334-336` | inline `isinstance` branch |
| `tools/dashboard_data.py:918-924` | `_froms()` — its own comment names the identical hazard verbatim |
| `skills/valoria-vector-audit/scripts/workbench.py:120-121` | inline ternary |
| `skills/valoria-module-adjudicator/scripts/contract_flowchart.py:263-264` | **a divergent partial that is a LIVE BUG** — `",".join(frm or ["?"])` special-cases only the literal `"engine"`, so any other bare-string `from:` is joined character-wise (`faction_state` → `f,a,c,t,i,o,n,_,s,t,a,t,e`) |

⚠️ **Correction of record (critic C-F1).** The v1 draft claimed two sites and its review record
asserted the "exactly twice in production" figure had been "attacked repo-wide and **holds**." That
was **false** — one grep refutes it. An assertion that a claim survived adversarial attack, when it
did not, is the §0.1-point-3 failure this program was written to prevent, committed inside the
program's own review record. It is struck from `02_…md` and recorded here rather than quietly edited.
The `contract_flowchart.py` bug is a genuine find that the wrong count was hiding.

Migration deliberately
partial: W3 migrates the two inline sites, the top CI consumers, and **`wiring_map_check.py:45`'s
regex reader via a `module_ids()` accessor**; the long tail gets `[REWORK]` flags, not a 21-file
big-bang. **Falsifier:** old-vs-new normalization identity over the live file + per-migration mutation
check.

### 2.5 Prose-path checker — REJECTED as new; ADOPTED as the already-declared fold
Execute `ci_claude_workflow_paths.py:14-15`'s own stated end state (ED-IN-0085 P1), widened per §1
predicate 3 to **source, not just prose**. Confirmed non-overlapping with ED-IN-0091 W4 item 3:
`ci_common.sim_reference_roots()` owns *where the sim reference lives*; `RETIRED_TREES` owns *which
trees are retired* — different questions, both single-owned. Site fixes stay theirs; detection
widening is ours. **`ci_formula_prose_check.py:88` is added to both programs' scope via a routing
row** — neither owned it (critic B-F2).
**Falsifier:** must find `tools/registry.py:22` at HEAD before W1 repoints it.

### 2.6 Orphan-classification repair — ADOPTED, small
`build_apparatus_registry` counts a module's own unit test as an invoker, so `tools/registry.py`
reports `orphaned: false` today (critic A-F7). Test-only imports must classify as orphan or §1
predicate 2's ratchet cannot move. Also fixes its `imports:` under-reporting (misses `try/except`
imports at `registry.py:145,149`).

### 2.7 Size-cap single-sourcing — ADOPTED, but **NOT mechanical** (critic A-F3)
Re-measurement found **≥5 divergences**, not one: `propagation_map` 15k vs 10k *and a contradictory
second policy block at 5k* (the loader returns on first hit, so it would silently bind 10000 and never
see 5000); `arc_register` 20k vs 5k; `values_master` 40k vs 50k; `patch_register_index` 20k vs 6k;
`names_index` 8k vs generic 10k. **18 of 26 checker paths return `None` from `yaml_max_tokens`** — of which **13 are `.jsonl` with no
policy coverage of any kind** (there is no `**/*.jsonl` catch-all). *(The v1 draft said "12 of 26",
which is not reproducible under any counting rule — critic C-F7. Counting rule now stated: an entry
"resolves" iff `yaml_max_tokens` returns non-`None`; 8 of 26 do.)* So this stage
carries ≥5 threshold rulings, one duplicate-key repair, and 12 new policy rows — **sonnet/high with an
opus adjudication**, not the sonnet/low "template PR" the draft assumed. §6 row 6 is widened
accordingly.

### 2.8 Provenance-tag literals — ADOPTED as shared-literal extraction; merging NOT proposed
The three vocabularies check different things (constant citation / module-shape comments / claim
reproducibility). One importable tuple in `obs_core.py` (precedent: `DECISION_MARKERS`), each checker
keeping its accepted subset. **Falsifier:** before/after identical-verdict run of all three checkers.

---

## §3 · Waves

Execution **sonnet/opus only**. Critics via `hCritic` → `valoria-critic` (read-only by construction).
Every write lane `isolation: worktree`. §10 caching: one agent per shared-prefix family streams
first, then fan out; tier escalation only at phase boundaries. One PR per wave.

### Wave 0 — Re-verify + interlock (blocks everything) — 7 agents
| # | Stage | Agents | Tier / effort |
|---|---|---|---|
| 1 | Re-verify every claim this plan is load-bearing on against HEAD (the OI-44 staleness class) | 2 | sonnet, high |
| 2 | File all 7 §0.1 routing rows + the ED-IN-0091 §4 stop-condition (interlock 1) | 1 | sonnet, low |
| 3 | **Workplans compliance backfill** (§7): 7 pointer files + `workplans/README.md` convention rewrite | 1 | sonnet, low |
| 4 | Establish ED-IN-0073's state (interlock 4) and its effect on W4 sequencing | 1 | sonnet, high |
| 5 | Draft §6 docket in workplan §5 row format | 1 | **opus** |
| 6 | Critic relay | 1 | valoria-critic (opus) |

**Falsifier:** stage 1 must independently rediscover ≥1 stale claim on a corpus already known to
contain several — `assert corrections >= 1`. A verification pass finding zero has failed.

### Wave 1 — Ownership-layer repair — 8 agents
| # | Stage | Agents | Tier |
|---|---|---|---|
| 1 | **Repoint `ci_formula_prose_check.py`'s census + `rows > 0` guard; publish the first real A18 measurement** (§2.0) | 1 | sonnet, high |
| 2 | Size-cap single-sourcing: ≥5 rulings + duplicate-key repair + 12 policy rows | 1+1 | sonnet high + **opus** adjudicator |
| 3 | Kill the two ownership-layer second-parses | 1 | sonnet, high |
| 4 | Route **both** vocabulary checkers through the facade | 1+1 | sonnet + **opus** adjudicator |
| 5 | `references/registry/README.md` (held-back) + generated worklist; repoint 3 in-scope citations | 1 | sonnet, high |
| 6 | Critic relay | 1 | valoria-critic (opus) |

### Wave 2 — Flag & detection machinery — 9 agents
| # | Stage | Agents | Tier |
|---|---|---|---|
| 1 | `[REWORK]` marker: MARKERS row + `--check-rework` + `rework.count` + test | 1 | sonnet, high |
| 2 | Prose-path fold, **source-scoped with the alias-fatal split** + `paths.dead` | 1 | sonnet, high |
| 3 | `structure_audit --dup` + frozen-harness allowlist + known-answer fixtures + `dup.count` | 2 | sonnet, high |
| 4 | `contracts_store.py` + parity test (no migrations yet) | 1 | sonnet, high |
| 5 | Orphan-classification repair (§2.6) | 1 | sonnet, low |
| 6 | Signal-design adjudication (retiered from opus per critic B-F16 — parseability is mechanical) | 1 | sonnet, low |
| 7 | Critic relay + a dedicated refuter attacking dup-detector precision on live output | 2 | valoria-critic (opus) ×2 |

**Baselines are seeded at W5, not here** — seeding before W3/W4 apply their flags would make this
program's own flagging regress the ratchet.

### Wave 3 — Apply: dedup, migrate, flag — 9 agents
| # | Stage | Agents | Tier |
|---|---|---|---|
| 1 | Migrate the two inline normalizations + top CI consumers + `wiring_map_check`'s regex reader | 2 | sonnet, high |
| 2 | Triage every detector finding: dedup-here / `[REWORK]`+ED / inbound / docket | 1+1 | sonnet → **opus** |
| 3 | Execute the dedup-here set, each with parity test + mutation check | 2 | sonnet, high |
| 4 | **Append inbound items to the existing `MB §12` / `PC §15` INBOUND sections** — physical routing, not PR-body (critic B-F3) | 1 | sonnet, low |
| 5 | Critic relay | 2 | valoria-critic (opus) ×2 |

**Falsifier:** `assert dispositioned == detector_findings`. Stage 4 corrects the draft's regression —
ED-IN-0091 established that routing is **physical**: "A dedicated session reading only its own plan
misses nothing." A PR body is not a section of the MB plan. "Never lane-handoff writes" remains
correct for `HANDOFF_MB.md`; it is wrong for the INBOUND sections that exist to receive routing.

### Wave 4 — Lane/scale table + placement detection — 8 agents
| # | Stage | Agents | Tier |
|---|---|---|---|
| 1 | Seed `lane_ownership.yaml`, provenance per row (sequencing per interlock 4) | 1 | sonnet, high |
| 2 | Adjudicate judgment rows; `unassigned` + question where genuinely Jordan's | 1 | **opus** |
| 3 | `lane_ownership.py` + flip `LANE_PATH_PREFIXES` to import it (44 dead prefixes die) | 1 | sonnet, high |
| 4 | `ci_lane_scale_check.py` + known-answer tests; scale half per §5 | 2 | sonnet, high |
| 5 | Apply `[REWORK]` flags to **the detector's `lane.misplaced` output** — `assert flagged == detector_misplaced` | 1 | sonnet, low |
| 6 | Critic relay | 2 | valoria-critic (opus) ×2 |

### Wave 5 — Capstone — 8 agents
| # | Stage | Agents | Tier |
|---|---|---|---|
| 1 | Seed the six baselines (enumerated by name below) | 1 | sonnet, high |
| 2 | Re-run every detector; diff every §1 predicate | 1 | sonnet, high |
| 3 | Append `[CSO]` rows to `04_execution_ledger.md` | 1 | sonnet, low |
| 4 | Disposition-map diff — every row matched, every miss recorded AS a miss | 1 | **opus** |
| 5 | Top-level read-only adversarial audit | 1 | **fable** |
| 6 | 2× refuter critics over capstone claims (majority kill) | 2 | valoria-critic (opus) |
| 7 | `HANDOFF_IN.md` + root `HANDOFF.md` | 1 | sonnet, low |

*(v1 gave W5 no stage table, so its "7 agents" was unreconcilable — critic C-F14.)*

Seed the baselines **enumerated by name, not by count** — `rework.count`, `dup.count`, `paths.dead`,
`formula.drift`, `lane.unmapped`, `lane.misplaced` (six; the draft said "four" while naming five —
critic B-F11); re-run every detector; diff every §1 predicate; append `[CSO]` ledger rows; opus
disposition diff; **fable read-only top-level audit**; 2× refuter critics; `HANDOFF_IN.md` + root
`HANDOFF.md`.

---

## §4 · The rework flag

```python
# [REWORK ED-IN-0105]: second owner of from:-normalization — single owner is tools/contracts_store.py; migrate this parse
```

- **Grammar:** `[REWORK <ED-id>]: <reason naming the violated rule and the intended single owner>`.
  Block extent is conveyed by placement + the reason line, **not** a machine-parsed range grammar —
  a range syntax would be a second registry nobody maintains.
- **The note lives in the ED entry**, not the comment. **The editorial ledger IS the store; the code
  marker is the pointer.** No standalone flag-registry file exists or ever will — stubwire's
  derived-never-stored doctrine, applied to "built wrong" as stubwire applies it to "not built."
- **Ingestion:** one row in `build_decisions.MARKERS` (13 → 14; category `rework`, priority 2), so
  flags surface in `DECISIONS.md` beside all other marker-level debt. `--check-rework` prints
  `N rework flags` for `count_re`.
- **Not a fourth provenance vocabulary.** `[REWORK]` asserts a *defect*, not trust in a value, so it
  joins the `DECISION_MARKERS` open-item family (`[GAP`, `[STUB`, `[ASSUMPTION`, TODO). A constant
  inside a REWORK-flagged block still needs its own `[canonical:…]` tag; the axes are orthogonal and
  the checkers never read each other's markers.
- **Chill risk, and its falsifier:** requiring an ED per flag may push agents to prose TODOs instead.
  Falsifier — the DECISIONS digest showing `todo`-category growth alongside flat `rework` counts.

---

## §5 · Lane & scale compliance

**Authoring first — there is no ground truth today.** Verified: `lane_assignments.yaml` is the retired
Lane-A/B/C concept; `build_decisions.LANE_PATH_PREFIXES` self-disclaims exhaustiveness and carries 44
dead prefixes; ledger `files:` arrays exist only for MB/PC. **No exhaustive path→lane table exists and
no lane- or scale-placement check exists anywhere.** A detector built before the table has nothing to
be right about.

Each row carries `provenance:` naming which partial owner produced it. Two sources disagreeing → a
**conflict row** to opus adjudication; matched by none → `unassigned` **with the question written
down**. Nothing is guessed. Encoded-not-resolved: `systems/overview/` (CLAUDE.md "no lane" vs
`build_decisions.py:230` maps `systems/overview/sim/` → `SE`; `systems/overview/` itself has no row).

**Flagging without moving.** A confirmed misplacement gets `[REWORK ED-…]` at the file head naming the
correct home and owning lane. **The move is that lane's later work, never this program's.** The §5
hand-list (`systems/victory/` docs vs the live resolver at `engine/autoload/victory.py`;
`parliamentary_vote.py`/`parliamentary_stay.py` self-documented "(faction scale)" in an SC folder;
`engine/autoload/npc_ai.py` in the engine core with its doc home at `systems/npcs/`) is the
**expected-answer fixture, not the work-list** — the applied set is the detector's output
(critic B-F12).

**Scale half, stated honestly:** blocked on §6 row 1. Until it lands, the check emits the
4-vocabulary divergence table and **asserts nothing** — so at merge, **zero scale misplacements are
flagged.** That is a real, disclosed limitation of this program, not a silent one.

**Seam vs drift:** a seam has a citation (ruling, plan fork, CLAUDE.md slice note); drift has none.
Not flagged: `faction_action.py:349` (declared seam); the contest 6-module cycle; the MB two-tree
fork (ED-IN-0091 §5 fork 1 — Jordan's).

---

## §6 · Held for Jordan (loud — nothing here ratifies on merge)

| # | Fork | Default on offer | Blocks |
|---|---|---|---|
| 1 | **Scale-vocabulary reconciliation** — 4 vocabularies: `keys.py:62` runtime 4-enum; contracts/wiring 7-value; `mechanics_index_gen:96` 9-value spelling `peninsular`. Interacts with ED-IN-0091 §5 fork 5 | **Partial:** normalize `peninsular`→`peninsula`; declare `keys.py` sole enum owner, others import it. **None** for the substantive call — whether `scene`/`thread`/`provincial`/`primitive`/`service`/`cross_scale` are scales, facets, or errors | the entire scale half of §5 |
| 2 | **Attribute rosters ×3** — `descriptor_registry.yaml:33` (9), `glossary.md:31` (7, self-documents the conflict), `combatant.py:92` (7 params, non-mapping names). ED-IN-0029 UNRULED | **None.** Cross-flag the three sites with mutual citations. Do not bind | typed actor schema **+ the A18 warn→block flip (OPT-AV-6)** — the roster gates formula enforcement too (critic B-F15) |
| 3 | **WS1 end-state flip** — does `registry.py:22`'s aspiration still stand? | Author the README as PROPOSED; execute step 1.5 only. **Merging W1 does NOT ratify the flip** | nothing now |
| 4 | **`systems/overview/` lane** + lane status of `threadwork/`, `characters/`, `victory/` | overview → `unassigned` (CLAUDE.md text outranks a triage table's tag); no new lanes minted by this program | those rows stay `unassigned` |
| 5 | **Six dice/degree kernels** — divergence partly defended in-docstring (`sigma_leverage.degree:284`), partly canon-fork (ED-SC-0004, MB fork 6), with a 26-site identical cluster in the frozen harness corpus | **None** — spans three lanes and two held forks. Cross-flag each kernel citing the others; route the MB pair inbound; stop | kernel unification |
| 6 | **Size-cap divergences (≥5) + one contradictory duplicate policy key** | Per-row: keep the checker's value and record it in the policy with a reason, **except** the `propagation_map` duplicate block, which is a bug to delete either way | predicate 7 |
| 7 | **Workplans-pointer enforcement.** Premise corrected: **all 7 live plans are currently pointer-less**; W0 backfills them | Backfill now; **no new CI gate yet** — revisit if a plan lands pointer-less after the convention is documented | nothing |
| 8 | **The §0.2 tiering conflict** — does the 2026-07-28 Fable ruling stand, or does this directive relax it? | §10's ruling governs unless Jordan says otherwise | Fable's role in future programs |
| 9 | **May a companion program amend ED-IN-0091's immutable §4 stop-conditions?** Interlock 1 needs a real gate; the only binding mechanism lives inside a file declared immutable | Keep it as protocol on `04_execution_ledger.md` (weaker, but consistent with that program's governance). Carve an explicit amendment exception only if the `registry.py` race is judged worth it | whether interlock 1 is a gate or a protocol |
| 10 | **Ledger size-cap ownership reversal.** `atomization_rules.yaml:113-115` deliberately assigns the 13 `.jsonl` caps to `ci_register_size_check.py`'s THRESHOLDS, "not here". Predicate 7 would reverse that | **Keep the existing ruling** — scope predicate 7 to the 13 non-`.jsonl` paths and leave ledger caps where their owner put them. Reverse only if Jordan wants one policy file for all 26 | predicate 7's scope |

---

## §7 · Workplans compliance (Jordan's second directive — W0 stage 3)

**Rule as given:** *any* plan — workplan, session plan, implementation schedule — requires direct
placement in `workplans/` or a pointer file there.

**State at HEAD — LANDED, not pending.** *(The v1 text said "zero pointer files exist" and scheduled
their creation at W0. It was stale at its own commit: the pointers were created in the same commit
that shipped it — critic C-F2.)* `workplans/` now holds **9 `POINTER_*.md` files**, a rewritten
`README.md` carrying the convention, and **`tools/ci_workplan_pointer_check.py`**, its guard.

The backfill came from an independent triage of **58** plan-shaped files under `audit/`:
**7 LIVE** / 14 superseded / 7 complete / 29 historical / 1 unknown — **corrected by the third
adversarial pass to 8 LIVE**, because `audit/2026-07-22-mass-battle-stress-test/full_implementation_plan_v1.md`
was misclassified SUPERSEDED (critic D-F3). It is `Status: PROPOSED` under a `HANDOFF_MB.md:763`
section headed "**(IN PROGRESS)**" carrying Jordan's "nothing is golden" directive; grepping the
07-26 plan for its Phase-1 items (B1/B2/B3/B5, geometry, col_grid, octagon) returns none of them.
**A triage that buries a live plan is the exact failure the convention exists to prevent**, and it
happened on the first attempt — which is the argument for the guard, not against the convention.
The 9th pointer is this program's own plan.

**The guard, and the half it deliberately omits (critic D-F7).** `ci_workplan_pointer_check.py`
checks what is deterministic: five required fields, a lane from the roster, no duplicate targets,
and every `target:` resolving on disk. Mutation-verified — planting a dead target turns it red. It
does **not** check "every live plan has a pointer": that needs a liveness oracle, and liveness was
measured un-inferable, so a guessing guard would be wrong in both directions. That half is §6 row 7.
Per §0.1 point 5: ship the guard you can write; name the half you did not.

**Pointer files carry an explicit `liveness:` field, not an inferred one.** The triage established
that a `## Status:` heading is **not** a liveness signal in either direction: only 10 of 58 files
carry one and 7 of those 10 are dead, while 3 of the 7 live plans do carry one. Inference would be
wrong in both directions.

**Two disagreements the pointers must not inherit:** `HANDOFF_MB.md` labels the live MB plan
"v1 (superseded)" — that bullet predates PR #250's in-place v2 correction; and
`valoria_master_workplan_v6.md`'s MB row still calls `05_redesign_workplan.md` "the governing plan."
Both are recorded in the pointer notes as known-stale upstream text.

---

## §8 · Falsifiers (per §0.1 point 3)

| Claim | Falsifier |
|---|---|
| Re-verification actually verified | W0 `assert corrections >= 1` |
| One parser per governed YAML | `test_sole_reader.py` red on a planted second `safe_load` |
| Facade routing changed no verdicts | corpus verdict-parity capture — empty diff or the wave stops |
| Phantom-path detection works | widened scanner must find `tools/registry.py:22` at HEAD; and must find `ci_formula_prose_check.py:88`-class executed constants, not only docstrings |
| Formula ownership is measured | `rows > 0` guard; a run reporting 0 quantities FAILS instead of passing |
| REWORK machinery counts | plant a flag → DECISIONS ingestion + count + ratchet; delete the MARKERS row, all three fail |
| Dup detector precision | known-answer both directions; allowlist exercised; live count reconciled against W0's census; **excluded-harness count printed, never silently dropped** |
| `contracts_store` parity | old-vs-new identity + per-migration mutation check |
| Lane flags are exhaustive, not anecdotal | `assert flagged == detector_misplaced` |
| Size-caps single-sourced | red on a planted hardcoded limit |
| Every §1 signal is ratcheted | `set(§1 signals) ⊆ set(review_baseline keys)`, `assert checked >= 6` |
| Nothing MB/PC-owned was touched | W5 `git diff --stat` ∩ (`systems/combat/**`, `tests/sim/mass_battle/**`) empty — **asserted, not eyeballed** |

---

## §9 · Risks — where this plan is most likely wrong

1. **Detector noise remains the top risk**, even with the frozen-harness allowlist. The AST-identity
   signal may still over-fire on boilerplate. Stop-rule: live count ≫ W0 census halts the wave.
   Fallback: ship the constant-name signal only and **record the function-identity signal as
   not-built**, plainly.
2. **The lane table's judgment rows could encode wrong ownership silently** — the "wrong is silent"
   class §10 reserves the top tier for. Mitigations: provenance per row, unassigned-over-guess, opus
   adjudication, two critics. **Residual risk is real:** a plausible-but-wrong lane assignment can
   survive review because nothing runtime-checks it. The report-only period before any blocking is the
   honest acknowledgment.
3. **Three-way concurrency** (this program, ED-IN-0091, ED-IN-0073) in one lane against a frozen ID
   file. Interlocks 1–7 are the mitigation; interlock 1 is a hard stop-condition, the rest are
   protocol. Protocol is weaker than enforcement.
4. **The A18 measurement is unknown at plan time.** Because the checker has been dead, nobody knows how
   much formula drift exists. W1 stage 1's output could be 0 rows or 200; the plan cannot size
   predicate 8's remediation until it runs. **Stated, not smoothed** — if it is large, that becomes its
   own program and this plan says so rather than absorbing it.
5. **Facade routing could change checker verdicts subtly** (precedence order vs permissive
   normalization). Parity capture covers only the current corpus; a term class absent at HEAD could
   still diverge later.
6. **This plan trusts ED-IN-0091's disposition map as current** — its W0b logged two stale-claim
   corrections against its own register in a single day. W0 re-verifies only what this program is
   load-bearing on; a stale row outside that set could still misroute an inbound item.
7. **The scale half ships flagging nothing.** Fully blocked on §6 row 1. If Jordan does not rule, half
   of the "wrong lane or scale" directive is unexecuted — and this plan would rather say that than
   fake coverage.
