# sim/ Module Conventions

Status: [PROVISIONAL — Pass 2l armature scaffold 2026-05-17]

## Module-stub anatomy

Every sim module has a docstring header containing:

```python
"""
sim/<subpackage>/<module>.py — <one-line summary>

Canon source: designs/<path>.md(#section)
Params source: params/<path>.md
Game Design constraints applicable: GD-<n>, GD-<n>, …
Status: [PROVISIONAL — <Pass-N armature stub | implementation note> <date>]

Dependencies:
  - sim/<subpackage>/<module> — <why depended on>

Entry points:
  - <fn_signature(arg, arg) -> ReturnType>
"""
```

## Naming

- Module filenames match the mechanic name in `registers/mechanics_index.yaml`
  (snake_case)
- Entry-point function names are imperative verbs: `resolve_*`, `apply_*`,
  `compute_*`, `check_*`, `attempt_*`
- Class names are PascalCase: `MassBattleEngine`, `ConvictionTrack`,
  `PenisularStrainState`
- Constants are UPPER_SNAKE_CASE: `LETHALITY_SCALE`, `DICE_TN_VALUES`

## Dependency declarations

Every module lists its sim/ dependencies in the docstring header. Forbidden
patterns:

1. **Upward dependencies** — `sim/personal/*` modules MUST NOT import from
   `sim/peninsular/*` or `sim/provincial/*`. Direction: provincial → personal,
   peninsular → provincial, etc. (scale hierarchy enforces import direction).
2. **Cross-scale shortcuts** — bypassing `sim/cross_scale/handoff_rules.py`
   when moving between scales is forbidden. All scale transitions go through
   the handoff layer.
3. **Direct world-track writes** — faction-action modules MUST NOT write
   directly to `peninsular/ci_track.py` etc.; route through `accounting.py`.

## Entry-point conventions

Every public function:
- Takes its operands as keyword-or-positional args
- Returns a typed result object (dataclass / NamedTuple), never a bare dict
- Logs to `sim/autoload/audit_log.py` (pending) on every state-changing op
- Raises `RuntimeError` with specific message on canon violation

## NotImplementedError as the stub default

All Pass 2l armature stubs raise `NotImplementedError` with the module path
and origin pass tagged in the message. This lets test code import the module,
detect stub-vs-implementation status programmatically, and report progress
toward full armature occupancy.

## Canon binding

When a module references canon content (a mechanic value, a system version),
the citation goes in:
1. The module docstring `Canon source:` line (file-level)
2. An inline comment at the relevant function: `# Canon: designs/<path>#<section>`
3. The `registers/mechanics_index.yaml` entry for the mechanic

Module changes that affect mechanic shape require updating `mechanics_index.yaml`
in the same commit (Pass 2j enforcement, pending).

## GD constraint enforcement

When a module's behavior is governed by a GD constraint (canon/02_canon_constraints.md
§B), the GD ID is declared in the docstring header. Affected functions cite
the GD inline: `# GD-1: no faction-specific victory triggers permitted here`.

## Testing

Mirror structure under `sim/tests/`. Stub: every module has a corresponding
test file that confirms `NotImplementedError` is raised pre-implementation,
and that the module can be imported without error.
