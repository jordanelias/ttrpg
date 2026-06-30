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
2. **`HANDOFF.md`** — the **single live continuity surface**: pending work, decisions, next actions.
   The SessionStart banner (`tools/session_status.py`) reads its "Next actions" section.
3. **`references/canonical_sources.yaml`** + **`canon/mechanics_index.yaml`** — machine-readable
   indices. ⚠️ The `canonical_sha__*` pins in `canonical_sources.yaml` are **not verified against the
   working tree** (the only tooling re-syncs them *from* GitHub, which contradicts the working-tree
   rule). Treat the pins as advisory, not a trustworthy integrity signal.

**Ignore for currency** — these are stale or retired, do not resume from them:
- `README.md` — outdated navigational pointers; defers to the three files above.
- `session_log_current.md`, `session_log_archive.md`, `session-handoff-2026-05-06.md`,
  `session_logs/`, `handoffs/`, `canon/session_checkpoint.md` — **retired session-log/checkpoint
  machinery still present in the tree** (one even carries `status: active`). They are NOT
  authoritative; **`HANDOFF.md` is the only live continuity surface.** Do not write into them and do
  not resume from `canon/session_checkpoint.md`. *(Recommended cleanup, not yet done: move these under
  `deprecated/`.)*
- `archives/`, `deprecated/` — history only, never canonical.

---

## 2. How this repo is worked

- **The working tree is the source of truth.** Read and edit local files directly (Read/Write/Edit,
  Grep/Glob). **Do not re-fetch from the GitHub API** and do not trust memory over disk — the checkout
  is fresher than any cache. *(Caveat: some `tools/` still re-fetch from GitHub — see §6. Those are the
  exception being ported out, not the model to follow.)*
- **Commit with git.** Stage your own files explicitly and `git commit`; no bespoke wrapper. If you are
  on `main`, branch first. Commit message format:
  `[scope] description` where scope ∈
  `editorial, patch, simulation, compilation, infrastructure, skill, cleanup, godot, phase, fix, bugfix`.
  Cite `PP-NNN` / `ED-NNN` in the description when applicable.
- **Continuity = git history + `HANDOFF.md`.** No session-log/checkpoint machinery is in use (despite
  retired files lingering — §1). When you pause mid-task, capture next actions in `HANDOFF.md`; a
  commit *is* the session close.

---

## 3. Repository map

| Directory | Contents |
|---|---|
| `canon/` | Philosophical foundations (P-01..P-14), editorial ledger (`editorial_ledger.jsonl`), patch register, mechanics index, canonical timeline, supersession register |
| `designs/` | System design docs by subsystem: `architecture/` (Key substrate), `scene/` (combat engine, social contest), `provincial/` (mass battle, factions), `territory/`, `threadwork/`, `npcs/`, `articulation/`, `world/`, `audit/`, `workplans/`, `godot/` |
| `params/` | Extracted mechanical parameters as **prose markdown tables** — `core.md` (dice), `board_game.md` (+ `bg/`), `contest.md`, `mass_combat.md`, `threadwork.md`, `factions*`. ⚠️ Numbers live as English tables, not typed data (see §5). |
| `references/` | Registries/indices — `canonical_sources.yaml`, `names_index.yaml`, `glossary.md`, `module_contracts.yaml`, `descriptor_registry.yaml`, `values_master.yaml`, propagation maps, throughlines. ⚠️ `references/subsystems/{handoff,checkpoint,session_log}_subsystem.md` document **retired** machinery as if live — ignore them. |
| `tests/` | The `tests/valoria/` **pytest unit suite** (the only executable tests) + simulation outputs + coverage matrix. ⚠️ Also holds ~850KB of narrative/audit `*.md` ("emergent_arc_skeleton_test_*", session audits) that are **prose, not executable specs** — don't mine them as behavioral contracts. |
| `sim/` | Monte-Carlo / simulation code (`mc_v18.py`, per-scale subpackages) — the **1:1 Python reference the GDScript port is built from**. See `sim/README.md` + `sim/CONVENTIONS.md`, but note those docs understate progress (§7). |
| `engine/` | Sigma-leverage engine armature + audit harness. ⚠️ `engine_audit_harness.py` is **dead** (hardcoded `/home/claude` paths) — do not invoke. |
| `tools/` | All CI checks, validators, collators, generators. Intended invariant: every rule lives once. Some tools are dead or GitHub-dependent — §6. |
| `archives/`, `deprecated/` | History; not canonical. |

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
- **ID systems.** `PP-NNN` patches (`canon/patch_register_active.yaml`), `ED-NNN` editorial items
  (`canon/editorial_ledger.jsonl`), `LB-NN` workplan lane-blocks. Reserved-ID blocks are tracked and
  currently **exhausted** (ED ceiling 1042) — re-block before allocating new IDs
  (`references/id_reservations.yaml` + `HANDOFF.md`).
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

- **Governing spec:** `designs/audit/2026-06-10-godot-conversion-strategy/godot_conversion_strategy_v1.md`
  — status **PROPOSED (Jordan-vetoable throughout)**, with an open 8-item register and **unexecuted
  Gate-0 preconditions** (KeyStore v2, base classes, RNG service). It is the plan, **not yet a ratified
  contract**. Drive its register + Gate-0 to closure before treating any decision as fixed.
- **Skeleton is non-compilable.** `designs/godot/skeleton/` covers only **1 of 27** modules
  (`personal_combat`) and `extends`/calls a spine (`BaseEngine`, `EngineModule`, `Key`, `KeyBus`,
  `GameState`, `Resolver`) **defined nowhere in the corpus**. It cannot be opened and run in Godot 4.6.
- **The one ported module already disagrees with its oracle.** `combat_config.gd` hand-edits
  `adef_threshold` away from the canonical Python oracle (`designs/scene/combat_engine_v1/config.py`),
  with an inline `[AUDIT-FIX]` note — so Key-log parity (the master validation gate) cannot go green.
  **Never let a port "correct" its oracle in-place;** fix `config.py` in canon via the editorial ledger,
  then re-export.
- **~37% of contracts are not implementable specs.** In `references/module_contracts.yaml`, 10/27 modules
  have `doc: null` (no home design doc — including `engine_clock`, the temporal spine) and 11/27 resolvers
  are `[ASSUMPTION]`-grade. Porting beyond the combat slice is **blocked on authoring canon first** (start
  with `engine_clock`).
- **The four `designs/godot/*.md` docs are stale (all 2026-04-18) with no supersession banner** and encode
  the pre-`d+σ` model. `data_serialization_spec.md` ships wrong schemas (writable `mandate`, 34 vs 35
  settlements). Do not implement from them; defer to the strategy doc + Key substrate.

---

## 7. Simulation / balance (the GDScript port's oracle — handle with care)

- `sim/` is the **1:1 Python reference** the port validates against (`sim/README.md`). It is ~11,400 LOC,
  partly stubbed (~19 `NotImplementedError`), with self-asserted `[PROVISIONAL]`/`[CANONICAL]` docstrings.
  Its `sim/README.md`/`CONVENTIONS.md` say "all modules are stubs" — **that is stale**; many modules are
  real and `mc_v18` runs campaigns.
- **The sim has no tests and is never run in CI.** No `sim/tests/` exists; no CI job executes `mc_v18`.
  A seeded batch currently yields a degenerate win-share (one faction ~87%, two at 0%) that **nothing
  flags.** If you tune balance numbers for Godot, you have no regression oracle — **add a deterministic
  seeded smoke assertion before trusting any sim output.**
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
- **Some "integrity" gates re-fetch from GitHub** (`broken_dependency_checker.py`,
  `patch_propagation_checker.py`, `freshness_gate.py`) — they validate remote `main` and require
  `GITHUB_PAT`, not the working tree. This is the unfinished API→working-tree port.
- **Several tools are dead** (import the orchestrator's `github_ops.py`, only present under
  `deprecated/`, or hardcode `/home/claude`): `compliance_check`, `extract_values`, `extract_proper_nouns`,
  `freshness_gate`, `valoria_collator`, `valoria_bulk_fix`, `file_lookup`, `engine/engine_audit_harness.py`.
  They fail opaquely — don't assume "tool exists ⇒ rule enforced."
- **Token-size limits are enforced twice** with drifted thresholds (`ci_register_size_check.py` hardcoded
  dict vs `references/atomization_rules.yaml`).

Run the unit tests locally: `pip install pyyaml pytest && python -m pytest tests/valoria -q`.

---

## 9. Task routing (which skill / surface for the job)

Claude Code discovers skills by name + description; invoke the one that fits. Skills live in `skills/`.

| If the task is… | Use |
|---|---|
| Writing infill prose | `prose-writer` |
| Dice/EV/pool/Momentum math, d10 success probs | `valoria-dice-model` |
| Combat-balance simulation | `valoria-combat-simulator` |
| Finding inert/inconsistent mechanics | `valoria-mechanic-audit` |
| Philosophy (P-01..P-14) compliance | `valoria-canon-guard` |
| Key IN → resolver → OUT contract closure | `valoria-module-adjudicator` |
| NERS resolver stress methodology | `valoria-resolution-diagnostic` |
| Emergent-arc generation | `valoria-arc-generator` |
| Editorial-debt workflow over the JSONL ledger | `valoria-editorial-register` |
| Index/infill doc hygiene | `valoria-atomizer` |
| Structural-debt corpus scan | `valoria-vector-audit` |
| Splitting an oversized doc into index + chunks | `valoria-chunker` |
| Assembling a canonical artifact (with canon-guard) | `valoria-compiler` |
| Incremental module-by-module sim build | `valoria-simulator` |

`valoria-orchestrator` is **retired** to `deprecated/skills/` (the old `/home/claude` GraphQL session
driver; superseded by the Claude Code-native model).

**General routing:** establish currency via `CURRENT.md` → check `HANDOFF.md` for in-flight/next actions
→ read the subsystem head and its `## Status:` line → make the change in the working tree → run the
relevant `tools/` validator and `pytest tests/valoria` → commit with the `[scope]` format and any
`PP-NNN`/`ED-NNN` citation. When a number must cross into Godot, follow §5; when porting, follow §6/§7.
