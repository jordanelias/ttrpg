# Valoria — TTRPG design repo

Design source of truth: `jordanelias/ttrpg`. Companion implementation repo: `valoria-game` (Godot).

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

## Naming

Canonical name is **Solmund** — never **Galbados** (the deprecated name). Enforced by
`tools/ci_naming_check.py` (CI + pre-commit) and an edit-time nudge.

## Enforcement (where the gates live)

- **Authoritative tier — CI** (`.github/workflows/valoria-ci.yml`, on branch-protected `main`):
  register sizes, co-file rules, editorial markers, naming, PP-674 vetting, ED-citation integrity,
  sim anti-fabrication, plus the `tests/valoria/` unit tests. CI is the unbypassable boundary.
- **Local tier — advisory accelerators** (one-time setup per clone: `git config core.hooksPath .githooks`):
  `.githooks/pre-commit` runs the SAME validators against staged files via `python tools/valoria_local.py --staged`;
  `.claude/settings.json` wires an edit-time naming nudge, a SessionStart status banner, and a Stop handoff reminder.
  Bypass a local block with `git commit --no-verify` — CI still enforces.

Every rule lives once, in `tools/`, and is called by both CI and the local hooks. Never re-implement a rule.

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
