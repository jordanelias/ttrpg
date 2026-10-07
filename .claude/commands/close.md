---
description: Close a commit — the one full-suite run, the lane validator, the commit, the handoff.
---

Run this **after this commit's last edit, immediately before committing** — not after an individual
edit (CLAUDE.md §0.4).

1. **Provision, if this container has not been.** `python tools/session_provision.py` — silent,
   idempotent, installs `pyyaml pytest numpy pytest-xdist` only if absent. Without it step 3
   cannot run.

2. **Learn the container's known-red before debugging anything.** `cat .git/shallow` — if this is a
   shallow clone, `tests/valoria/test_forked_status.py` fails on arrival because the
   commits its `FORK:` rows name are out of reach. That is the clone, not `main`. Do not debug it.

3. **The full suite, ONCE.** `python -m pytest tests/valoria -q -n auto`.
   - **First decide whether to run it at all** (`CLAUDE.md` §0.4 cl.1): name what it can observe
     that CI's run on push will not. Prose, ledger, skill or link changes run only the test files
     that read what changed (`grep -rl <path> tests/`); CI is the full gate.
   - Red? Re-run **the failing file only** while you fix it. The full suite comes back once, when
     you believe you are done.
   - Touched `engine/season/`? Add `python -m pytest engine/season/tests -q -n auto`. Touched
     nothing it can reach? Do not run it.

4. **The lane's validator**, not all of them. `python tools/valoria_local.py --staged` runs the
   staged-file validators; it **does not run pytest**, so local-green is not CI-green. Then the one
   validator that owns what you touched — check `references/ci_checks_registry.yaml`'s `role:` line.
   - **Layer conformance:** if the diff touches `engine/season/` code, run the `layer-conformance`
     skill's Lens B on the files you changed; if it adds a tool, a guard, a hook or a governance
     rule, run Lens A. Its output is edits to this commit, not a document. A diff touching neither
     skips this.

5. **Commit.** `[scope] description` with scope ∈ the §2 vocabulary, **subject ≤ 72 characters**,
   detail in the body, citing any `PP-NNN` / `ED-NNN`. On `main`, branch first.

6. **Capture next actions** in your lane's `registers/handoffs/HANDOFF_<LANE>.md`. Root
   `HANDOFF.md` is for genuinely cross-cutting items only.

7. **Report honestly.** If a check failed or a step was skipped, say so. Name what you did not run
   and why.

**Do not** arm a check-in, a re-run or a wake-up of any kind afterwards (§11). End the turn.
