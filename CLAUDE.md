# Valoria — TTRPG / videogame design repo

This repo is the **design source of truth** for **Valoria**, a Godot 4.6 videogame that fuses
personal-scale resolution (dice pools, skill checks, social contests) with a strategic layer
(territory control, faction politics, domain actions). There is no GM — the engine resolves
everything. Design docs keep their TTRPG/board-game mechanical detail; those abstractions *are*
the videogame's layers.

Design source of truth: `jordanelias/ttrpg` (this repo). Companion implementation repo:
`jordanelias/valoria-game` (Godot 4.6).

## Where "what's current" lives — read these first

- **`CURRENT.md`** — the single human-readable index of the live canonical surface (Generation **v40**).
  When unsure whether a doc is current, start here. Each subsystem row points at its current head.
- **`references/canonical_sources.yaml`** — machine-readable, SHA-pinned source of truth.
- **`canon/mechanics_index.yaml`** — machine-readable mechanics index.
- **`HANDOFF.md`** — live continuity / next-actions across sessions (see below).
- Superseded exploration lives under `archives/` and `deprecated/` — present for history, **not** canonical.

## How this repo is worked

- **The working tree is the source of truth.** Read and edit local files directly (Read/Write/Edit,
  Grep/Glob). Do not re-fetch from the GitHub API and do not trust memory over the files on disk —
  the checkout is fresher than any cache. (This replaces the old stateless-sandbox rule "always fetch
  from GitHub"; that rule no longer applies on a local clone.)
- **Commit with git.** Stage your own files explicitly and `git commit`; no bespoke commit wrapper.
  Commit message format: `[scope] description` where scope is one of:
  `editorial, patch, simulation, compilation, infrastructure, skill, cleanup, godot, phase, fix, bugfix`.
  Cite `PP-NNN` / `ED-NNN` in the description when applicable.
- **Continuity lives in git history + `HANDOFF.md`.** There is no session-log/checkpoint machinery.
  When you pause mid-task, capture next actions in `HANDOFF.md`; a commit *is* the session close.

## Repository map

| Directory | Contents |
|---|---|
| `canon/` | Philosophical foundations (P-01..P-14), editorial ledger (`editorial_ledger.jsonl`), patch register, mechanics index, canonical timeline, supersession register |
| `designs/` | System design docs by subsystem: `architecture/` (Key substrate), `scene/` (combat engine, social contest), `provincial/` (mass battle, factions), `territory/`, `threadwork/`, `npcs/`, `articulation/`, `world/`, `audit/`, `workplans/`, `godot/` |
| `params/` | Extracted mechanical parameters — `core.md` (dice), `board_game.md` (+ `bg/`), `contest.md`, `mass_combat.md`, `threadwork.md`, `factions*` |
| `references/` | Registries and indices — `canonical_sources.yaml`, `names_index.yaml`, `glossary.md`, `module_contracts.yaml`, propagation maps, throughlines |
| `tests/` | Simulation outputs, stress tests, coverage matrix, and the `tests/valoria/` pytest unit suite |
| `sim/` | Monte-Carlo / simulation code (`mc_v18.py`, per-scale subpackages); see `sim/README.md` + `sim/CONVENTIONS.md` |
| `engine/` | Sigma-leverage engine armature + audit harness |
| `tools/` | All CI checks, validators, collators, generators — every rule lives here once |
| `archives/`, `deprecated/` | History; not canonical |

## Conventions

- **Co-filing.** Many docs come as a pair: an `*_index.md` (skeleton/structure) plus an `*_infill.md`
  (prose). Co-file rules are CI-enforced (`tools/ci_co_file_checker.py`) — keep the pair in sync.
- **Versioning / generations.** The `_v30` suffix marks the **current** generation of a subsystem — it
  is *not* a stale tag. "v40" is a *generation marker* (consolidated, contracts-bound, Godot-ready), not
  a filename suffix; there is no blanket rename. A new version number is earned by the next actual major
  revision of a system, not by find-and-replace. See `CURRENT.md` for the rationale.
- **ID systems.** `PP-NNN` patches (`canon/patch_register_active.yaml`), `ED-NNN` editorial items
  (`canon/editorial_ledger.jsonl`), `LB-NN` workplan lane-blocks. Reserved-ID blocks are tracked; re-block
  before allocating new IDs (see `references/id_reservations.yaml` + `HANDOFF.md`).

## Naming

Canonical name is **Solmund** — never **Galbados** (the deprecated name). Enforced by
`tools/ci_naming_check.py` (CI + pre-commit) and an edit-time nudge. Definition naming is centralized in
`references/names_index.yaml`.

## Enforcement (where the gates live)

- **Authoritative tier — CI** (`.github/workflows/valoria-ci.yml`, on branch-protected `main`): syntax,
  register sizes, hooks verifier, co-file rules, editorial markers, naming + names-consistency/drift,
  sim anti-fabrication, supersession, PP-674 vetting, ED-citation integrity, the `tests/valoria/` pytest
  suite, integrity, and compliance. CI is the unbypassable boundary.
- **Local tier — advisory accelerators** (one-time setup per clone: `git config core.hooksPath .githooks`):
  `.githooks/pre-commit` runs the SAME validators against staged files via `python tools/valoria_local.py --staged`;
  `.claude/settings.json` wires an edit-time naming nudge (`hook_naming_guard.py`), a SessionStart status
  banner (`session_status.py`), and a Stop handoff reminder (`session_handoff_reminder.py`).
  Bypass a local block with `git commit --no-verify` — CI still enforces.

Every rule lives once, in `tools/`, and is called by both CI and the local hooks. **Never re-implement a rule.**

Run the unit tests locally: `pip install pyyaml pytest && python -m pytest tests/valoria -q`.

## Skills (`skills/`)

- `prose-writer` — narrative voice/technique spec for infill prose.
- `valoria-dice-model` — d10 success probabilities, EV, opposing rolls, pool/Fibonacci/Momentum math.
- `valoria-combat-simulator` — combat-balance simulation.
- `valoria-mechanic-audit` — systematic mechanical-consistency review (finds inert mechanics).
- `valoria-canon-guard` — philosophy-compliance (P-01..P-14) review.
- `valoria-module-adjudicator` — Key IN → resolver → OUT contract-closure checks.
- `valoria-resolution-diagnostic` — NERS resolver stress methodology.
- `valoria-arc-generator` — emergent-arc generation.
- `valoria-editorial-register` — editorial-debt workflow over `canon/editorial_ledger.jsonl`.
- `valoria-atomizer` — index/infill doc-hygiene convention.
- `valoria-vector-audit` — structural-debt corpus scan.
- `valoria-chunker` — structural splitting of an oversized doc into index + chunks.
- `valoria-compiler` — structural assembly of canonical artifacts with a canon-guard pass.
- `valoria-simulator` — incremental module-by-module sim build with a verification ledger.

`valoria-orchestrator` was retired to `deprecated/skills/` (it was the `/home/claude`
GraphQL-harness session driver; superseded by the Claude Code-native model — see HANDOFF.md).

Claude Code discovers skills by name + description; invoke the one that fits the task.
