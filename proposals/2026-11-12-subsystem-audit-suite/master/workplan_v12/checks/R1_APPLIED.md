# R1_APPLIED — repair lane R1 (Opus): the global repairs applied across parts 3 to 44

## Status: WORK RECORD (one round; a record of scripted edits to `master/workplan_v12/`; resolves nothing at runtime, CLAUDE.md §0.05; deleted with the suite when v12 is adopted)

Scripts: `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/r1/` (`common.py` the part list and field reader; one `rN_*.py` per repair, each run `--dry` first, then applied; the part 2 appendix scripts `parse_parts.py`, `graph.py`, `gates.py` extracted verbatim beside them). Baseline before any edit: `graph.py` on the tree as the check lanes left it reads S+G+R 521 edges, acyclic, 25 waves, 25 steps, hours path 356.5 h (part 2 §1.2 reproduced).

Appended repair by repair as each is applied (a restart resumes from the last section written).
