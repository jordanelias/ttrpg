---
description: Close a commit — the one full-suite run, the lane validator, the commit, the handoff.
---

The close sequence from CLAUDE.md §0.4 and §0's last bullet, as steps rather than prose. Run it
**after this commit's last edit, immediately before committing** — not after an individual edit.

1. **Provision, if this container has not been.** `python tools/session_provision.py` — silent,
   idempotent, installs `pyyaml pytest numpy pytest-xdist` only if absent. A fresh remote container
   has pyyaml alone, so without this step step 3 cannot run at all.

2. **Learn the container's known-red before debugging anything.** `cat .git/shallow` — if this is a
   shallow clone, `tests/valoria/test_forked_status.py` fails two tests on arrival because the
   commits its `FORK:` rows name are out of reach. That is the clone, not `main`. Do not debug it.

3. **The full suite, ONCE.** `python -m pytest tests/valoria -q -n auto` — ~2m36s parallel, 9m01s
   serial, same 1817 tests. Omitting `-n auto` pays 3.5× for the same verdict.
   - Red? Re-run **the failing file only** while you fix it. The full suite comes back once, when
     you believe you are done. Red is not a licence to loop the gate.
   - Already green from before your last edits? Run it anyway — this is the per-commit shipping
     gate. But never run it a second time to re-confirm a green you already hold.
   - Touched `engine/season/`? Add `python -m pytest engine/season/tests -q -n auto`. Touched
     nothing it can reach? Do not run it — "everything, just in case" is the habit §0.4 ends.

4. **The lane's validator**, not all of them. `python tools/valoria_local.py --staged` is cheap and
   runs the staged-file validators; it **does not run pytest and never has**, so local-green is not
   CI-green. Then the one validator that owns what you touched — check
   `references/ci_checks_registry.yaml`'s `role:` line rather than guessing.

5. **Commit.** `[scope] description` with scope ∈ the §2 vocabulary, **subject ≤ 72 characters**,
   detail in the body, citing any `PP-NNN` / `ED-NNN`. On `main`, branch first.

6. **Capture next actions** in your lane's `registers/handoffs/HANDOFF_<LANE>.md`. Root
   `HANDOFF.md` is for genuinely cross-cutting items only.

7. **Report honestly.** If a check failed or a step was skipped, say so. A green claim you did not
   verify is worse than a red one you did. Name what you did not run and why.

**Do not** arm a check-in, a re-run or a wake-up of any kind afterwards (§11). Ending the turn is
how this repo waits.
