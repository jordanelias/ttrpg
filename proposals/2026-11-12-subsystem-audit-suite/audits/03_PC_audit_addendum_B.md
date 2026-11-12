# PC — adversarial steelman audit, addendum B

## Status: REFERENCE (an audit addendum; resolves nothing at runtime)

## Read at: 2c24c81 (working tree)

Addendum to `audits/03_PC_audit.md` (read at `601e715`; that file is not edited). It covers what the
first lane reported unread: `modules/combat/weapon_physics.py` and `weapons.py`, the workbench under
`systems/combat/`, `engine/season/decision/options.py` and `choose.py`, the whole `.designs/` combat
set, `videogame_mode_spec.md`, and the combat entries of `.audit/`. It then judges Jordan's
personal-combat intent of 2026-11-12 against that full set and gives a decision-ready design for the
per-phase approach and the automatic duel round. Findings continue the first audit's numbering
(`F-PC-15` onward); resolutions continue at `R-PC-26`. Probe scripts and outputs are in the scratchpad
named in §8. Every figure is a reading at this SHA with `PYTHONHASHSEED=0`.

## 0. Verdict of the addendum

**The first audit's verdict stands, and its proposal 5 is right in shape and wrong in three
particulars that matter to a builder: what a "phase" is, what state a round must carry, and where an
NPC's in-fight choice lives.** The detail is in §2 (corrections), §3 (the intent against the full
design set) and §4 (the design). The superseding proposal is
`proposals/03_PC_duel_round_and_approach_B.md`.

