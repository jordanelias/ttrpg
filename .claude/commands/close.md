---
description: Close a commit — layer conformance, the one full-suite run, the lane validator, the handoff, the commit.
---

Run this **after this commit's last edit, immediately before committing** — not after an individual
edit (CLAUDE.md §0.4).

1. **Provision, if this container has not been.** `python tools/session_provision.py` — silent,
   idempotent, installs `pyyaml pytest numpy pytest-xdist pytest-timeout` only if absent. Without it step 4
   cannot run.

2. **Learn the container's known-red before debugging anything.** run the failing file on `main`'s tree
   first, and `cat .git/shallow` — a shallow clone cannot reach the commits `FORK:` rows name. That is the
   clone, not `main`.

3. **Layer conformance, before the suite or beside it** (its output is code edits: either the suite
   runs after them, or it runs on a `git worktree` snapshot of `HEAD` taken before them and only what
   the edits reach re-runs after, `tests_for_diff.py --base <snapshot sha>`, as `methodology-execute`
   BATCH-CLOSE does). If the diff touches `engine/season/` or `modules/` code, run the `layer-conformance` skill's
   Lens B on the files you changed; if it adds a tool, a guard, a hook or a governance rule, run
   Lens A. Its output is edits to this commit, not a document. A diff touching neither skips this.

4. **The full suite, ONCE.** `python -m pytest tests/valoria -q -n auto`.
   - **First decide whether to run it at all** (`CLAUDE.md` §0.4 cl.1): name what it can observe
     that CI's run on push will not. Prose, ledger, skill or link changes run only the test files
     that read what changed (`grep -rl <path> tests/`); CI is the full gate.
   - **Run `python tools/tests_for_diff.py`** (add `--run` to execute it): it reads what this session changed and names the
     narrowest suites. An edit confined to `modules/` or `systems/` of combat, mass battle or social contest runs `-m <subsystem>`
     across all three trees; anything else (engine core, tools, registries) gets the full gates below. It cannot see a
     realm-level effect of a module edit (the season suite executes the modules too); CI's full run is that check.
   - **Pass `--timeout=<budget>` and `--durations=30`.** A test's budget is a multiple of its last
     `--durations` reading, never a guessed number; the run's `--timeout` is the largest budget among
     the tests it covers, and a run with no reading yet goes without one and becomes the reading. A
     timed-out test is reported as a measurement failure, not red or green. No `--maxfail`: it hides
     the red list.
   - Red? Re-run **the failing file only** while you fix it. The suite comes back once, when you
     believe you are done, over only what the fix diff reaches (`tests_for_diff.py --base`).
   - Touched `engine/season/`? Add `python -m pytest engine/season/tests -q -n auto --dist worksteal`. Touched
     nothing it can reach? Do not run it.

5. **The lane's validator**, not all of them. `python tools/valoria_local.py --staged` runs the
   staged-file validators; it **does not run pytest**, so local-green is not CI-green. Then the one
   validator that owns what you touched — check `references/ci_checks_registry.yaml`'s `role:` line.
6. **Capture next actions** in your lane's `registers/handoffs/HANDOFF_<LANE>.md`, so the commit
   carries them. Root `HANDOFF.md` is for genuinely cross-cutting items only.

7. **Commit.** `[scope] description` with scope ∈ the §2 vocabulary, **subject ≤ 72 characters**,
   detail in the body, citing any `PP-NNN` / `ED-NNN`. On `main`, branch first.

8. **Report honestly.** If a check failed or a step was skipped, say so. Name what you did not run
   and why.

**Do not** arm a check-in, a re-run or a wake-up of any kind afterwards (§11). End the turn.
