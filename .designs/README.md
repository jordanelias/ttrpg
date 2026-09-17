<!-- ARCHIVED-NOT-CANON -->
# `.designs/` — quarantined design reference

**Nothing in this tree is canon, and nothing in it resolves at runtime.**

This directory holds the design prose that used to live under `systems/*/reference/` and at the
root of `engine/`. It was moved here on 2026-09-16 because that prose kept being swept up and read
as authority by sessions working on the game code, which is the failure `CLAUDE.md` §0.05 exists to
prevent: *code is the mechanism, prose is reference*.

The leading dot is the mechanism. Ripgrep — and therefore the agent search tools built on it —
skips hidden directories unless explicitly asked for them with `--hidden`, as does Python's
`glob.glob`. A session sweeping `systems/` for a term no longer finds forty superseded documents.

## Rules

- **Do not cite anything here as the reason a behaviour is correct.** Cite it for intent, history
  and vocabulary. If canon and code disagree, the code decides (§0.05).
- **Do not edit these files.** They are frozen at the state they were archived in.
- **Do not add to this tree.** New design work goes in `proposals/`.
- **Nothing points here.** `CURRENT.md`, `references/canonical_sources.yaml`,
  `references/module_contracts.yaml` and `registers/mechanics_index.yaml` no longer name these
  documents. Old paths resolve through `references/restructure_ledger.md` via `tools/pathres.py`.

## Layout

Original structure is preserved with the `reference/` segment dropped:

| was | is |
|---|---|
| `systems/<sub>/reference/<doc>.md` | `.designs/systems/<sub>/<doc>.md` |
| `systems/<sub>/<mid>/reference/<doc>.md` | `.designs/systems/<sub>/<mid>/<doc>.md` |
| `engine/<doc>.md` | `.designs/engine/<doc>.md` |

Every file carries its original path in its own banner, so provenance survives without the ledger.

230 documents. `engine/season/**` was deliberately **not** archived — that tree is live.
