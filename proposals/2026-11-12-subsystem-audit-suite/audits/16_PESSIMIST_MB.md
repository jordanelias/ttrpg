# MB — pessimist audit: NERS, premise and emergent narrative, of mass battle

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 2eba83c (working tree)

Scope: `modules/mass_battle/`, `systems/mass_battle/sim/`, `engine/season/loop/effects_army.py`, the host
seam (`engine/season/seam/wrappers/mass_battle.py`, `loop/sides.py`, `loop/effects_combat.py::_eff_march`),
Jordan's stated intent for mass battle (`AUDIT_BRIEF.md`: the cell-based army → unit → subformation →
troops hierarchy; mixed weapons at a fatigue and movement cost, archers carrying arming swords; Football
Manager, Total War, Ogre Battle, Unicorn Overlord, Bannerlord; the commanded and the auto-resolved battle
as one resolver), and five premise sentences of a battle. The first audit (`audits/04_MB_audit.md`,
F-MB-01..19) and its addendum (`04_MB_audit_addendum_B.md`, F-MB-20..26) and the ten `04_MB_*` proposals
are cited, not redone. Everything measured here is new work unless a finding id of theirs is named.

All runs: `PYTHONHASHSEED=0`; scripts and outputs under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_MB/`.

(Sections below are appended as the work proceeds; §0 is written last and placed first.)

