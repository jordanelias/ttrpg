# Valoria — ttrpg repo

PAT: read from ~/.valoria_pat

Bootstrap on every session start:
1. Run quick_bootstrap() from github_ops
2. Report STATUS BLOCK (token, last_stage, next_action, P1-BLOCKER count)
3. STOP — wait for task.

Scripts: ~/github_ops.py and ~/valoria_hooks.py
Active repo: jordanelias/ttrpg (design source of truth)
Naming: always Solmund, never Galbados.
No memory substitution — always fetch from GitHub.
Commit path: h.safe_commit() only.
