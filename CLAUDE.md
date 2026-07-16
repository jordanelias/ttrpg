# Valoria — TTRPG / videogame design repo

This repo is the **design source of truth** for **Valoria**, a Godot 4.6 videogame that fuses
personal-scale resolution (dice pools, skill checks, social contests) with a strategic layer
(territory control, faction politics, domain actions). **There is no GM — the engine resolves
everything.** Design docs keep their TTRPG/board-game mechanical detail; those abstractions *are*
the videogame's layers.

- **Design source of truth:** `jordanelias/ttrpg` (this repo).
- **Implementation repo:** `jordanelias/valoria-game` (Godot 4.6) — separate clone, frozen since 2026-05-04.

---

## 1. Read these first (currency)

The live canonical surface is **Generation v40** (consolidated, contracts-bound, Godot-ready). There
are more "current state" files than there should be; trust them in this strict priority order:

1. **`CURRENT.md`** — the **single human-readable index** of the live canonical head per subsystem.
   When unsure whether a doc is current, this is the authority. Last reconciled by hand (2026-06-28),
   so treat it as fresher than any filename or in-file version string.
2. **`HANDOFF.md`** — the **continuity index**: root file pointing to lane-scoped
   `registers/handoffs/HANDOFF_<LANE>.md` files (§3's `ED-<LANE>-NNNN` taxonomy: `MB, PC, FI, SC, FA, WR, IN,
   GO, SE`) plus genuinely cross-cutting pending work/decisions/next actions. Split 2026-07-02 to
   reduce concurrent-session merge-collision surface on one shared file, the same motivation
   behind the ID namespace itself. The SessionStart banner (`tools/session_status.py`) reads root
   `HANDOFF.md`'s "Next actions" section only — check your lane's file too.
3. **`references/canonical_sources.yaml`** + **`registers/mechanics_index.yaml`** — machine-readable
   indices. ⚠️ The `canonical_sha__*` pins in `canonical_sources.yaml` are **not verified against the
   working tree** (the only tooling re-syncs them *from* GitHub, which contradicts the working-tree
   rule). Treat the pins as advisory, not a trustworthy integrity signal.

**Ignore for currency** — these are stale or retired, do not resume from them:
- `README.md` — outdated navigational pointers; defers to the three files above.
- Retired session-log/checkpoint machinery (`session_log_*`, `session_logs/`,
  `deprecated/session_machinery/handoffs/` — old per-lane-A/B/C `.yaml` files, a **different,
  retired thing** from the live root-level `registers/handoffs/*.md` directory below, do not confuse them —
  `canon/session_checkpoint.md`, the `references/subsystems/{handoff,checkpoint,session_log}` docs)
  — **relocated to `deprecated/session_machinery/` (2026-07-01, ED-1084)**. NOT authoritative;
  **`HANDOFF.md` + `registers/handoffs/HANDOFF_<LANE>.md` are the only live continuity surface.** Do not
  write into or resume from anything under `deprecated/session_machinery/`.
- `deprecated/` (incl. `deprecated/archives/`, the former top-level `archives/` merged in 2026-07-16, ED-IN-0071 P5) — history only, never canonical.

---

## 2. How this repo is worked

- **The working tree is the source of truth.** Read and edit local files directly (Read/Write/Edit,
  Grep/Glob). **Do not re-fetch from the GitHub API** and do not trust memory over disk — the checkout
  is fresher than any cache. *(Caveat: some `tools/` still re-fetch from GitHub — see §6. Those are the
  exception being ported out, not the model to follow.)*
- **Commit with git.** Stage your own files explicitly and `git commit`; no bespoke wrapper. If you are
  on `main`, branch first. Commit message format:
  `[scope] description` where scope ∈
  `editorial, patch, simulation, compilation, infrastructure, skill, cleanup, godot, phase, fix, bugfix, design`.
  Cite `PP-NNN` / `ED-NNN` in the description when applicable.
- **Continuity = git history + `HANDOFF.md`/`registers/handoffs/HANDOFF_<LANE>.md`.** No session-log/checkpoint
  machinery is in use (despite retired files lingering — §1). When you pause mid-task, capture next
  actions in your lane's `registers/handoffs/HANDOFF_<LANE>.md` (or root `HANDOFF.md` only for genuinely
  cross-cutting items); a commit *is* the session close.
- **Merging a PR ratifies its PROPOSED contents by default (ED-1094, 2026-07-02).** If a PR lands a
  design doc, doctrine, or ledger entry tagged `PROPOSED`/`provisional`, Jordan's review-and-merge of
  that PR *is* the ratification — flip the doc's `## Status:` line, the ED ledger `status`/`needs_jordan`
  fields, and `CURRENT.md` as part of the same merge, not as a separate later step nobody triggers.
  **The exception must be loud, not silent:** if something in the PR genuinely needs separate,
  explicit sign-off beyond ordinary merge review, call it out prominently in the PR body as *held
  back* — never bundle a hard design call into a routine-work PR and rely on an unprompted follow-up
  to ratify it later. (This closes a real recurring failure: ED-1083's doctrine sat PROPOSED in `main`
  after PR #55 was reviewed and merged, because the prior convention required a distinct explicit
  ratification step that nothing forced to happen.)

---

## 3. Repository map

| Directory | Contents |
|---|---|
| `canon/` | Philosophical foundations (P-01..P-14), canonical timeline, canon constraints, self-rendering/leap-mechanism amendments. **The process registers moved OUT to `registers/` (2026-07-16, ED-IN-0071 P0)** — canon/ now holds only world/design truth. |
| `registers/` | Process ledgers/registers, moved out of `canon/` (ED-IN-0071 P0, 2026-07-16): editorial ledger (`editorial_ledger.jsonl` pre-cutover flat IDs + lane-split `editorial_ledger_<lane>.jsonl` for `ED-<LANE>-NNNN`, §3), patch register, supersession register, mechanics index, placeholder names. Old `canon/…` citations resolve via `references/restructure_ledger.md`'s alias map. |
| `registers/handoffs/` | Lane-scoped continuity: `HANDOFF_<LANE>.md` per `ED-<LANE>-NNNN` lane (§1), moved under `registers/` from top-level `handoffs/` (ED-IN-0071 P0b, 2026-07-16). Root `HANDOFF.md` (the index the SessionStart banner reads) **stays at repo root**. ⚠️ Do not confuse with the unrelated, retired `deprecated/session_machinery/handoffs/` (old per-lane-A/B/C `.yaml` files, a different concept — §1). |
| `designs/` | System design docs by subsystem: `architecture/` (Key substrate), `scene/` (combat engine, social contest), `provincial/` (mass battle, factions), `territory/`, `threadwork/`, `npcs/`, `articulation/`, `world/`, `audit/`. |
| `godot/` | The Godot port, consolidated out of THREE former homes (`designs/godot/`, `designs/videogame/`, `designs/audit/2026-06-10-godot-conversion-strategy/`) to a top-level primary (ED-IN-0071 P2, 2026-07-16): the PROPOSED governing `godot_conversion_strategy_v1.md`, the `godot_architecture_specification.md`, the 4 stale pre-`d+σ` docs, and `skeleton/` (§6). **Is** the eventual `res://` project root. Old paths alias via `references/restructure_ledger.md`. |
| `arcs/` | Generated **narrative content**, promoted out of `designs/arcs/` to a top-level primary (ED-IN-0071, 2026-07-16) — neither system-mechanics nor world-canon. Root holds the non-batch narrative (`arc_expansion`, `emergent_*`, `narrative_scenario_chains`, `throughline_resolutions`); the numbered arc batches (`arcs_01_04`…`arcs_46_55` + `arc_narrative_analysis`) live in `arcs/simulated/` (renamed from `gm_ref/`, root batches consolidated in). Arc **registers** (`arc_register*` tracking clocks/events/factions/territory/threads, formerly `references/arc_register*` + `references/arcs/`) live in `arcs/registers/` — distinct from the process ledgers in top-level `registers/`. Old paths alias via `references/restructure_ledger.md`. |
| `workplans/` | The master workplan + progress board, promoted out of `designs/workplans/` (ED-IN-0071 P1, 2026-07-16) to a top-level primary. `workplan_v6_progress.yaml` is the board the SessionStart banner reads (`tools/workplan_status.py`); `valoria_master_workplan_v6.md` is the live steering surface. Old `designs/workplans/…` paths alias via `references/restructure_ledger.md`. |
| `dashboard/` | The published GitHub-Pages status site, promoted out of `docs/dashboard/` (ED-IN-0071 P1). `tools/dashboard_data.py` writes `dashboard/data.json`; `.github/workflows/dashboard.yml` deploys it. |
| `proposals/` | Unratified design proposals, promoted out of `designs/proposals/` (ED-IN-0071 P1, 2026-07-16). Surfaced BY LOCATION by `tools/observability/build_proposals.py`. Old `designs/proposals/…` citations alias via `references/restructure_ledger.md`. |
| `params/` | Extracted mechanical parameters as **prose markdown tables** — `core.md` (dice), `board_game.md` (+ `bg/`), `contest.md`, `mass_combat.md`, `threadwork.md`, `factions*`. ⚠️ Numbers live as English tables, not typed data (see §5). |
| `references/` | Registries/indices — `canonical_sources.yaml`, `names_index.yaml`, `glossary.md`, `module_contracts.yaml`, `descriptor_registry.yaml`, `values_master.yaml`, propagation maps, throughlines. ⚠️ `values_master.yaml` is quarantined-stale (banner, ED-1084); the retired-machinery subsystem docs moved to `deprecated/session_machinery/` (ED-1084). |
| `tests/` | The `tests/valoria/` **pytest unit suite** (the only executable tests) + simulation outputs + coverage matrix. ⚠️ Also holds ~850KB of narrative/audit `*.md` ("emergent_arc_skeleton_test_*", session audits) that are **prose, not executable specs** — don't mine them as behavioral contracts. ⚠️ `tests/sim/` and `tests/sim_framework/` are **not** the `sim/` package below and not duplicates of each other — see `sim/README.md` for the three-way disambiguation before assuming any of them overlap. |
| `sim/` | Monte-Carlo / simulation code (`mc_v18.py`, per-scale subpackages) — the **1:1 Python reference the GDScript port is built from**. See `sim/README.md` + `sim/CONVENTIONS.md`, but note those docs understate progress (§7). `sim/README.md` also disambiguates against the confusingly-named `tests/sim/` and `tests/sim_framework/` (neither is this package). |
| `engine/` | Sigma-leverage engine armature + audit harness docs. The dead `engine_audit_harness.py` (hardcoded `/home/claude` paths) was retired to `deprecated/engine/` (2026-07-09) — do not resurrect. |
| `tools/` | All CI checks, validators, collators, generators. Intended invariant: every rule lives once. Some tools are dead or GitHub-dependent — §6. |
| `deprecated/` | History; not canonical. The two former graveyards are merged (ED-IN-0071 P5, fork #1): dead **content** under `deprecated/archives/` (the former top-level `archives/`), dead **code/machinery** under `deprecated/{tools,skills,engine,session_machinery,…}`. |

---

## 4. Conventions

- **Co-filing.** Many docs are a pair: `*_index.md` (skeleton/structure) + `*_infill.md` (prose).
  CI-enforced (`tools/ci_co_file_checker.py`) — keep the pair in sync.
- **Versioning ≠ currency.** Three orthogonal version axes coexist with **no reliable mapping**:
  filename `_v30`, in-file `## Version: vN.N`, and the `v40` generation marker (no file carries `_v40`).
  **A filename or in-file version cannot tell you what is current — only `CURRENT.md` and a head's
  `## Status:` line can.** Concrete hazard: `_v30` is nominally "current generation", but the current
  **combat** head is `designs/scene/combat_engine_v1/` (no `_v30`), while `combat_v30.md` is
  *PARTIALLY SUPERSEDED*. Always resolve combat via `CURRENT.md`, never by the `_v30` suffix.
- **ID systems.** `PP-NNN` patches (`registers/patch_register_active.yaml`), `ED-NNN` editorial items
  (`registers/editorial_ledger.jsonl`), `LB-NN` workplan lane-blocks. `references/id_reservations.yaml`
  is the allocation source of truth (read `next_free`, allocate, bump, co-commit — never max+1).
  **Two ED formats coexist (2026-07-02, ED-IN-0001):** the flat `ED-NNNN` sequence is **FROZEN**
  at `ED-1096` (two more flat IDs, ED-1095/1096, landed the same cutover day before the sequence
  fully stopped — `ED-1094` is the ruling that established the freeze, not the last ID issued
  under it; corrected 2026-07-11, ED-IN-0034, caught auditing `skills/valoria-editorial-register`
  against the ledger) — no new allocations, but permanently valid for existing citations — and all NEW EDs
  use the lane-tagged `ED-<LANE>-NNNN` format (e.g. `ED-MB-0001`), zero-padded to 4 digits. Lanes:
  `MB` mass battle, `PC` personal combat, `FI` field investigation, `SC` social contest,
  `FA` faction actions, `WR` world, `IN` infrastructure/cross-cutting, `GO` godot, `SE` settlements.
  Motivated by two same-session concurrent-allocation collisions on the flat sequence in one PR
  (see `ED-1094`'s ledger entry) — a lane tag makes cross-lane collision impossible by
  construction, not just by allocation discipline. Both formats resolve through the same
  citation-audit path (`tools/validate_ed_citations.py`) and currency gate
  (`tools/currency_consistency_check.py`) forever; no retrofit of pre-cutover entries.
  **The ledger file itself is lane-split too (2026-07-08):** an `ED-<LANE>-NNNN` entry lives in
  `registers/editorial_ledger_<lane>.jsonl` (lowercase lane code), not the flat
  `registers/editorial_ledger.jsonl` — mirroring the `HANDOFF.md` split below, and for the same
  merge-collision reason. Pre-cutover flat-ID entries stay in the main file (no retrofit). A
  lane file exists only once that lane has allocated an ED (no `_go.jsonl` yet). Both the main
  file and every lane file are "active, authoritative" — read all of them, not just one.
  **Session lane-scoping (convention, not yet CI-enforced):** a session should declare which
  lane its work belongs to (via the `ED-<LANE>` ids it allocates) and keep its commits/PRs scoped
  to that lane's files — avoid a single PR touching unrelated lanes except for genuinely
  cross-cutting `IN` work (like this namespace itself) or resolving a cross-lane collision.
- **Naming gate.** Canonical name is **Solmund** — never **Galbados** (deprecated). Enforced by
  `tools/ci_naming_check.py` (CI + pre-commit) and an edit-time nudge. Definition naming is centralized
  in `references/names_index.yaml`.

---

## 5. Data → Godot pipeline (READ before touching params or ingesting numbers)

This is the most fragile and most load-bearing surface for the videogame, and it has known traps. Do
not treat any "structured" data layer as ground truth without checking it against the prose.

- **Numbers live as prose, not typed data.** All mechanical parameters in `params/*.md` are markdown
  tables (unicode `×`, en-dashes, parenthetical caveats like "minimum 5", footnotes). A Godot importer
  **cannot ingest these directly** — there is no typed engine-params file yet.
- **`references/values_master.yaml` is auto-extracted and partly stale/wrong.** Its `formula` fields are
  byte-identical free-text English (not parseable ASTs); it indexes a **nonexistent** `params/combat.md`
  (~70 entries) and pulls 8 values from `params/threadwork_superseded.md`. **Do not lift numbers from it
  as canonical** — verify against the current prose head in `CURRENT.md` first.
- **Derived-stat schema is IN FLUX.** `descriptor_registry.yaml` marks the 9-attribute roster "IN FLUX",
  aggregates (`agg.body/mind/social`) as `placeholder` and not wired, and attribute keys as `warn` (not
  `block`). **Combat Pool is defined three different ways** across `values_master.yaml`, `params/core.md`
  (PP-247), and `module_contracts.yaml`. Do not bind Godot resource fields to these keys yet.
- **When you need a number for the engine:** resolve the subsystem head via `CURRENT.md` → read the prose
  param/design doc → cite the `PP-NNN`/`ED-NNN` that established it. Do not synthesize a value the ledger
  does not back (the anti-fabrication gate exists, but is leaky — §7).
- **Recommended (not yet built):** a typed engine-params YAML/JSON (numeric operands, structured
  formulas, explicit clamps) generated from the prose and CI round-trip-checked, ingested directly by
  Godot. Until that exists, every value crossing into Godot is hand-transcribed — flag drift risk.

---

## 6. Godot port pipeline (state of the bridge — READ before any "start implementation" task)

The conversion is **PROPOSED and largely un-executed**. The skeleton is illustrative, not buildable.
Do not represent the skeleton as a runnable head-start.

- **One home now.** The Godot material was consolidated from three scattered homes into the top-level
  `godot/` primary (ED-IN-0071 P2, 2026-07-16): the governing strategy (formerly under
  `designs/audit/2026-06-10-godot-conversion-strategy/`), `godot_architecture_specification.md` (formerly
  `designs/videogame/`), and the stale docs + `skeleton/` (formerly `designs/godot/`). Old paths alias.
- **Governing spec:** `godot/godot_conversion_strategy_v1.md`
  — status **PROPOSED (Jordan-vetoable throughout)**, with an open 8-item register and **unexecuted
  Gate-0 preconditions** (KeyStore v2, base classes, RNG service). It is the plan, **not yet a ratified
  contract**. Drive its register + Gate-0 to closure before treating any decision as fixed.
- **Skeleton is non-compilable.** `godot/skeleton/` covers only **1 of 27** modules
  (`personal_combat`) and `extends`/calls a spine (`BaseEngine`, `EngineModule`, `Key`, `KeyBus`,
  `GameState`, `Resolver`) **defined nowhere in the corpus**. It cannot be opened and run in Godot 4.6.
- **Port↔oracle discipline (ED-1050, resolved 2026-06-30).** `combat_config.gd` once hand-edited
  `adef_threshold` away from the canonical Python oracle with an inline `[AUDIT-FIX]`; Jordan resolved it
  by re-sweeping the oracle (`config.py`, monotone ADEF_THRESHOLD) and re-exporting — port and oracle now
  match. The rule stands: **never let a port "correct" its oracle in-place** — fix canon via the ledger,
  then re-export. Key-log parity is still known-red, but only because RESIST/GAP_EXPOSURE/gap-game logic
  has not yet been re-exported to `weapon_resource.gd`/`strike_module.gd` (ED-1050 residual).
- **~37% of contracts are not implementable specs.** In `references/module_contracts.yaml`, 10/27 modules
  have `doc: null` (no home design doc — including `engine_clock`, the temporal spine) and 11/27 resolvers
  are `[ASSUMPTION]`-grade. Porting beyond the combat slice is **blocked on authoring canon first** (start
  with `engine_clock`).
- **The four stale pre-`d+σ` docs** (`godot/{scene_tree_architecture,gm_to_engine_conversion,data_serialization_spec,implementation_sequence}.md`,
  all 2026-04-18) encode the pre-`d+σ` model — each carries a `⚠️ STALE / PARTIALLY SUPERSEDED` banner
  (flagged 2026-06-30, ED-1054) pointing at the strategy doc. (`godot/`'s other `.md` files —
  `README.md`, `godot_conversion_strategy_v1.md`, `godot_architecture_specification.md` — are current.)
  `data_serialization_spec.md` ships wrong schemas (writable `mandate`, 34 vs 35
  settlements). Do not implement from them; defer to the strategy doc + Key substrate.

---

## 7. Simulation / balance (the GDScript port's oracle — handle with care)

- `sim/` is the **1:1 Python reference** the port validates against (`sim/README.md`). It is ~11,400 LOC,
  partly stubbed (~19 `NotImplementedError`), with self-asserted `[PROVISIONAL]`/`[CANONICAL]` docstrings.
  Its `sim/README.md`/`CONVENTIONS.md` say "all modules are stubs" — **that is stale**; many modules are
  real and `mc_v18` runs campaigns.
- **The sim's own balance output has no regression oracle beyond the §8 smoke test.** `sim/tests/` now
  exists (a deterministic seeded regression + parity test — see §8's ED-1053 resolution), but no CI job
  executes full `mc_v18` campaigns. A seeded batch currently yields a degenerate win-share (one faction
  ~87%, two at 0%) that **nothing flags.** If you tune balance numbers for Godot, treat that gap as open —
  **add a deterministic seeded smoke assertion before trusting any full-campaign sim output.**
- **The anti-fabrication gate is leaky.** `tools/ci_sim_fabrication_check.py` whitelists constants by bare
  integer value globally and splits floats into integer tokens, so a fabricated constant can pass if its
  digits collide with any ledger value; it also only scans the changeset. **Do not rely on it to catch a
  made-up number — verify provenance by hand against the cited `canonical_source`.**
- Ledgers use ≥3 incompatible schemas and the checker reads only `value`; provenance fields are unchecked.
  None pin a generating git SHA. Treat ledger provenance as advisory.

---

## 8. Enforcement (where the gates live)

- **Authoritative tier — CI** (`.github/workflows/valoria-ci.yml`, branch-protected `main`): syntax,
  register sizes, hooks verifier, co-file rules, editorial markers, naming + names-consistency/drift,
  sim anti-fabrication, supersession, PP-674 vetting, ED-citation integrity, the `tests/valoria/` pytest
  suite, integrity, and compliance. **CI is the unbypassable boundary.**
- **Local tier — advisory accelerators** (one-time per clone: `git config core.hooksPath .githooks`):
  `.githooks/pre-commit` runs the SAME validators on staged files via `python tools/valoria_local.py
  --staged`; `.claude/settings.json` wires the edit-time naming nudge (`hook_naming_guard.py`), the
  SessionStart banner (`session_status.py`), and the Stop handoff reminder
  (`session_handoff_reminder.py`). Bypass a local block with `git commit --no-verify` — CI still enforces.

**Intended invariant:** every rule lives once, in `tools/`, called by both CI and local hooks. **Never
re-implement a rule.** Known violations of this invariant (treat as bugs, don't propagate):
- **Several tools were dead** (imported the orchestrator's `github_ops.py`, only present under
  `deprecated/`, or hardcoded `/home/claude`) and were **retired to `deprecated/tools/` /
  `deprecated/engine/` (2026-07-09, token-efficiency pass)**, mirroring the earlier
  `valoria-orchestrator` → `deprecated/skills/` retirement: `extract_values.py`,
  `extract_proper_nouns.py`, `valoria_collator.py`, `valoria_bulk_fix.py`, `file_lookup.py`,
  `compliance_dryrun.py`, `engine/engine_audit_harness.py`. None were invoked by CI, local
  hooks, or any skill — confirmed by grepping every workflow/hook/skill for each filename
  before moving. `skills/prose-writer/scripts/consistency_check.py` (the pre-`ci_naming_check.py`
  naming-gate matcher, GitHub-API-only) retired the same way, to
  `deprecated/skills/prose-writer/scripts/`. `tools/canon_coverage_check.py` is a **different**
  case — GitHub-API-based and unwired (`ci_job: ""` in `references/ci_checks_registry.yaml`) but
  explicitly awaiting Jordan's inclusion decision, not confirmed-dead legacy; left in place.
  (`compliance_check` is
  half-alive: its CI mode `--check-only --repo-state .` runs working-tree size caps and is a
  BLOCKING CI gate — note it is NOT in the local `valoria_local.py` list, so local-green ≠
  compliance-green; its orchestrator-era harness paths remain dead. ED-1082 correction.)
- **Observability apparatus consolidated (2026-07-15, ED-IN-0068).** `tools/observability/obs_core.py`
  is now the single owner of the primitives that were re-implemented ≥4 ways (editorial-ledger read,
  the 9-code lane roster **including GO**, the reconciled `## Status:` regex, the narrow needs-Jordan
  vs corpus-wide marker vocabularies, the `window.VALORIA_X` JS-bundle writer); the generators import
  it. `tools/observability/build_proposals.py` generates the **unified proposals/open-work register**
  (`PROPOSALS.md` triad — one lane-partitioned view of every unratified item, covering
  `proposals/` by location), refreshed by `audit-refresh.yml` alongside the decisions digest;
  it complements `DECISIONS.md` (marker-level debt) rather than duplicating it.
  `tools/build_apparatus_registry.py` generates `references/apparatus_registry.{yaml,md}` — the
  inventory of every tool/skill/hook/workflow with its output destination + format + orphan status
  (orphan flag derived from `structure_audit`'s import graph). That prune pass retired 4 zero-importer
  dead pure-function tools (`propagator`, `verify_cuts`, `coverage_matrix`, `find_references`) to
  `deprecated/tools/`. Still deliberately deferred (blocking-gate risk): migrating
  `currency_consistency_check`'s flat-file-only ledger reader and the `ci_audit_registry_check`
  all-entries reader onto `core` — each needs its own expected-delta test, not a drop-in.

*Resolved (ED-1053, 2026-06-30):* the three "integrity" gates — `broken_dependency_checker.py`,
`patch_propagation_checker.py`, `freshness_gate.py` — now read the **working tree** (no `GITHUB_PAT`,
no network), validating the checkout under test; `freshness_gate` computes blob SHAs locally
(`git hash-object`-equivalent) and is no longer dead. The duplicated token-size cap was single-sourced
from `references/atomization_rules.yaml`. The `sim/` reference now has a deterministic seeded CI test
(`sim/tests/`), and the sim-fabrication guard matches constants by `(variable, value)` and captures
full float literals. Residual: ~12 stale `canonical_sha__` pins surfaced by the now-local freshness
gate (refresh with `python3 tools/freshness_gate.py --update`); freshness stays report-only until then.

Run the unit tests locally: `pip install pyyaml pytest && python -m pytest tests/valoria -q`.

---

## 9. Task routing (which skill / surface for the job)

Claude Code discovers skills by name + description; invoke the one that fits. Skills live in `skills/`.

| If the task is… | Use |
|---|---|
| Writing infill prose | `prose-writer` |
| Dice/EV/pool/Momentum math, d10 success probs (+ Godot-canonical continuous mode) | `valoria-dice-model` |
| Combat-balance simulation | `designs/scene/combat_engine_v1/workbench/balance.py` directly (run `python workbench/balance.py [weapon\|attr\|tradition\|all] [n]`) — no skill wrapper; see §8's retirement note |
| Finding inert/inconsistent mechanics | `valoria-mechanic-audit` |
| Philosophy (P-01..P-14) compliance | `valoria-canon-guard` |
| Key IN → resolver → OUT contract closure | `valoria-module-adjudicator` |
| NERS resolver stress methodology | `valoria-resolution-diagnostic` |
| Emergent-arc generation | `valoria-arc-generator` |
| Editorial-debt workflow over the JSONL ledger | `valoria-editorial-register` |
| "Where are we in the workplan?" / resume-with-options / progress board | `valoria-workplan-navigator` |
| Index/infill doc hygiene | `valoria-atomizer` |
| Structural-debt corpus scan | `valoria-vector-audit` |
| Splitting an oversized doc into index + chunks | `valoria-chunker` |
| Assembling a canonical artifact (with canon-guard) | `valoria-compiler` |
| Incremental module-by-module sim build | `valoria-simulator` |

`valoria-orchestrator` is **retired** to `deprecated/skills/` (the old `/home/claude` GraphQL session
driver; superseded by the Claude Code-native model). `valoria-combat-simulator` is also **retired**
(2026-07-12, ED-IN-0039) — its bundled script was a hand-hardcoded, long-frozen 9-weapon model,
fully superseded by `designs/scene/combat_engine_v1/workbench/balance.py`, the actively-maintained
51-weapon canonical balance harness (40 added in the 2026-07-02 morphology expansion, plus the
original 11); see `deprecated/skills/README.md` for detail.

**General routing:** establish currency via `CURRENT.md` → check `HANDOFF.md` + your lane's
`registers/handoffs/HANDOFF_<LANE>.md` for in-flight/next actions → read the subsystem head and its `## Status:`
line → make the change in the working tree → run the
relevant `tools/` validator and `pytest tests/valoria` → commit with the `[scope]` format and any
`PP-NNN`/`ED-NNN` citation. When a number must cross into Godot, follow §5; when porting, follow §6/§7.

---

## 10. Model tiering for orchestrated / multi-agent work

When you fan work out across subagents — the **Agent** tool, or `agent()` calls in a **Workflow** script
— set the model **per task**. Subagents inherit the session model by default, so an un-annotated fan-out
on an Opus session runs Opus *everywhere*, which is slow and costly for work that doesn't need it.
Actively tier down; reserve Opus for genuine judgment. (This revives the retired orchestrator's routing
discipline — `deprecated/skills/valoria-orchestrator/references/model_routing_table.md` — updated for the
Claude Code-native `Agent`/`Workflow` tools and Opus 4.8.)

| Tier | Use for | Repo examples |
|---|---|---|
| **`haiku`** | Deterministic extraction; no real reasoning | chunking / section maps / indexing, find-replace + formatting, dice/probability arithmetic, ID & ED-citation extraction, table transcription, co-file pair listing, gathering excerpts |
| **`sonnet`** | Pattern recognition / bounded state-machine reasoning | mechanic audits (Modes A–E), single-scale sims (combat / thread / social / mass-battle), canon compliance yes-no checks, compilation + assembly, editorial propagation tracking, most `Explore`/`general-purpose` searches, routine infill drafts and doc edits |
| **`opus`** | Competing-considerations judgment; large-context synthesis | ambiguous design intent, setting/lore authorship, P-01..P-14 adjudication with trade-offs, module-contract closure, multi-doc synthesis, and the verify / judge / synthesis stage that *gates* a result |
| **`fable`** | The rare top-of-stack judgment nodes (added 2026-07-01, ED-1086 — availability restored 2026-07-01) | canonical-contract & **propagation-spec authorship** (the aggregate-up/distribute-down + termination artifact — doctrine ED-1083 §4), the emergence audit (seeded-sim + ablation verdicts, once runnable), deepest cross-corpus synthesis. Caveats: subscription metering (~50% weekly cap through 2026-07-07 — verify current terms); **no zero-data-retention** → use `opus` for retention-sensitive content; the safety classifier is irrelevant to game-design content. `fable` is an *upgrade trigger*, never a default — promote only on evidence a cheaper tier failed the node. |

**Downgrade triggers** — before spawning, ask: purely deterministic, or one-doc field extraction? →
`haiku`. Yes/no check against clear criteria, or bounded single-scale reasoning? → `sonnet`. Weighing
competing philosophical/design considerations, or synthesizing across dispersed docs? → `opus`. When
genuinely unsure, omit the override and inherit — but flag the stages above where a cheaper tier clearly
fits, rather than defaulting the whole fan-out to Opus.

**How to set it:**
- **Agent tool:** pass `model: "haiku" | "sonnet" | "opus" | "fable"` (e.g. `Explore`/`general-purpose`
  file-finding on `haiku`–`sonnet`; reserve `opus`+ for `Plan` and adjudication agents).
- **Workflow scripts:** set `opts.model` per `agent()` call, and `opts.effort: 'low'` for cheap
  mechanical stages — raising effort only for the hardest verify/judge stages. Mirror the tier in
  `meta.phases[].model` so the plan shows it. The canonical shape is **Haiku finders → Sonnet analyzers →
  Opus verifier/synthesizer.**

**Orchestration patterns** (from the 2026-07-01 workflow spec, ingested ED-1083 — see
`designs/architecture/holonic_container_doctrine_v1.md` for the doctrine side):
- **Agonist→antagonist is a relay, not a dialogue**: subagents are stateless and isolated —
  dispatch the producer, capture its output, dispatch the critic WITH that output, reconcile in the
  orchestrator. For audits this is *preferable*: a critic that never saw the producer's reasoning is
  more independent. Make independence structural: critic gets read-only tools.
- **Strong producer when producing; strong critic when auditing** — put the stronger tier where the
  binding constraint is.
- **Parallel write lanes need `isolation: worktree`** (one repo, colliding working trees otherwise);
  lanes return **fixed-format summaries**, not raw context — synthesis binds on the orchestrator's
  window.
- **Guardrails binding on every infill lane** (doctrine ED-1083 §2): implement the local rule only;
  declared I/O only; never special-case an entity/outcome (**scripting drift**); never grow a
  scale-local interface dialect (**shape divergence**).
- **Roster discipline (spec §7):** promote a role into `.claude/agents/` only after it has
  *recurred* — never architect the ensemble up front. No roster files exist yet by design; the
  watched candidates are a standing conformance-scanner and (once seeded headless sims + ablation
  are runnable) an emergence-auditor — see the 2026-07-01 decision queue.
