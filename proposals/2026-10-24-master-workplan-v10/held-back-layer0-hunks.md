# Held-back Layer 0/1 hunks of master workplan v10

## Status: PROPOSED. These hunks are NOT applied: they land only when Jordan merges the PR that carries them or answers M11. Merging this file ratifies nothing.

Each row is proposed text for a Layer 0 file. A row is applied by the position that owns it, in the held-back Layer 0 PR, and never by an agent's own motion. The `(RULED)` check was made before the hunk was listed: no `(RULED)` mark sits at or within the paragraph of the anchor.

| id | file | anchor (quoted words) | old text | new text | owner position | revert |
|---|---|---|---|---|---|---|
| H-L0-1 | `CLAUDE.md` §5 (Data to Godot pipeline), the sentence ending "Check the code first, every time." | "superseded by `degree_from_net` in `engine/autoload/dice_engine.py`" | `superseded by `degree_from_net` in `engine/autoload/dice_engine.py`). **Check the code first, every` | `superseded by `degree_from_net` in `engine/dice_engine/dice_engine.py`). **Check the code first, every` | CR-02 (c) (B10-01) | restore the old path; the owner file is `engine/dice_engine/dice_engine.py` and `engine/autoload/` does not exist in the tree, so the old text names a missing file |

Evidence for H-L0-1, read 2026-10-26: `grep -n 'engine/autoload' CLAUDE.md` finds one hit, in §5; `ls engine/autoload` fails; `engine/dice_engine/dice_engine.py` holds `degree_from_net`; `CURRENT.md`'s Dice row already names the new path.
