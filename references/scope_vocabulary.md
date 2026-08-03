# Scope Vocabulary — canonical source of truth
**Status:** unified-vocabulary established (D6, partial — single source + drift guard done; the ~10 reduction is proposed, not executed) · documented 2026-05-31 (Lane B, roadmap 5.8 / resolved-decision D6)
**Drift guard:** `tests/valoria/test_scope_vocabulary.py` — asserts the commit-scope row below matches `CLAUDE.md` §2, and fails on divergence.
> ⚠ **Corrected 2026-08-01 (ED-IN-0119).** This line previously named `tests/hooks/test_scope_vocabulary.py`. That test imported `valoria_hooks`/`github_ops` — retired modules — and `sys.path.insert(0, '/home/claude')`; it could not import, and no CI job or hook ran it. **The advertised enforcement did not exist, and real drift accumulated behind it:** `design` was added to the live commit vocabulary and this doc still said 11. The old test is retired to `deprecated/tests/hooks/`. Only the COMMIT axis is guarded now — see the note under the table.

## The problem (D6)
Three constructs each carry a scope/type vocabulary, and they are **disjoint** — the same conceptual domain may be present in one and absent from another, with no single place defining the vocabulary. That drift is the defect D6 targets ("UNIFY"). This doc is the single place; the test enforces it.

## The three live constructs (verified 2026-05-31)
| Construct | Source (as of 2026-05-31) | Consumers | Members |
|---|---|---|---|
| **Commit scopes** | **`CLAUDE.md` §2** (the live authority; `valoria_hooks.COMMIT_FORMAT` is retired) | every commit message; `tests/valoria/test_scope_vocabulary.py` | editorial, patch, simulation, compilation, infrastructure, skill, cleanup, godot, phase, fix, bugfix, design (**12**) |
| **Session scopes** | `github_ops.SESSION_SCOPES` (L936) | `start_session_log` (L957), `assert_bootstrap` (hooks L133) | infrastructure, godot, editorial, design, simulation, audit, general (**7**) |
| **Task types** | `valoria_hooks.TASK_REQUIRED_FILES` keys (L84) | `task_gate` (L427), github_ops L1397 / L1037 | simulation, audit, canon_check, editorial, patch, compilation, propose_mechanic, design_proposal, design, infrastructure (**10**) |

> **Source status, 2026-08-01 (ED-IN-0119).** Only the COMMIT axis is live. `github_ops.SESSION_SCOPES` and `valoria_hooks.TASK_REQUIRED_FILES` were retired with the orchestrator, so the session-scope and task-type rows are **historical record**, not live vocabularies, and are deliberately NOT guarded — a guard over a vocabulary nothing consumes is the dead-gate defect this correction exists to remove.

## Why they differ — three axes, not one list
- **Session scope** = *what kind of work this session is* (broad work domains).
- **Commit scope** = *what kind of change this commit is* (domains **plus** change-verbs: fix / bugfix / phase / cleanup / skill).
- **Task type** = *which required-files gate applies* (gate-keyed task taxonomy).

A naive "make all three identical" is **wrong**: `fix`/`bugfix` are commit change-verbs with no meaning as a session scope or a required-files gate; `general` is a catch-all session with no commit/gate meaning; `canon_check`/`propose_mechanic`/`design_proposal` are gate-keyed task types, not commit verbs. Unification means *one vocabulary consistently spelled*, with each construct a documented view of it — not three identical sets.

## Canonical vocabulary — current union (the as-is source of truth · 17)
Grouped by which axes use each:
- **All three:** infrastructure, editorial, simulation
- **Session + task:** design, audit
- **Session + commit:** godot
- **Session only:** general
- **Commit + task:** patch, compilation
- **Commit only (change-verbs):** skill, cleanup, phase, fix, bugfix
- **Task only (gate-keyed):** canon_check, propose_mechanic, design_proposal

The drift guard asserts the live union equals this set: adding or removing a scope in any construct fails the test until this doc + the test are updated together.

## Proposed reduction to ~10 (D6 target) — REQUIRES JORDAN DECISION + NON-PARALLEL WINDOW
The reduction **removes currently-valid scopes**, which breaks any lane using a dropped value — and `COMMIT_FORMAT` is the shared commit gate that *every* lane imports. **Do not execute during a parallel window** (same class of hazard as the 5.3 SHA-split). Proposed core ~10 domain set: `infrastructure, editorial, design, simulation, audit, patch, compilation, godot, canon, general`. Decisions to settle (each removes a live scope → Jordan's call):
- Commit change-verbs `fix / bugfix / phase / cleanup / skill` — fold into domains and describe the change in the message body, OR keep a small separate change-type set. Do **not** force change-verbs into the domain vocabulary.
- `canon_check` → `canon`; `propose_mechanic` → `design` or `patch`; `design_proposal` → `design`.
- Keep `general` (catch-all session).

Until settled, the live 17-member union stands and the three constructs are unchanged.

## Migration discipline (when executed)
1. Change the vocabulary in one place; update `CLAUDE.md` §2 + this doc in the **same** commit (the test fails otherwise — that is the single-source enforcement working).
2. Sequence the `COMMIT_FORMAT` change to a window with **no other active lanes** (shared commit gate).
3. Re-run `python3 -m pytest tests/valoria/test_scope_vocabulary.py -q`.
