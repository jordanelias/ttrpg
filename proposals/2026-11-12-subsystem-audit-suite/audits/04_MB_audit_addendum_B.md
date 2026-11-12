# MB — adversarial steelman audit, addendum B

## Status: REFERENCE (an audit addendum; resolves nothing at runtime)

## Read at: 6eff039 (working tree)

Addendum to `audits/04_MB_audit.md` (§0 to §18, read at `601e715`), written by a second lane with a fresh
reading budget. It does not repeat that audit. It takes what that audit reported as NOT READ (its §12 and
§18.4), reads it, corrects the first audit where the reading or a run shows it wrong, continues its
numbering (`F-MB-20` onward; resolutions `R-30` onward), and adds the sections the work order names:
the cell-based hierarchy, the manager-style battle, and the interfaces with the duel round, the campaign
layer and the shared roller. Proposals written by this lane are listed in §B6. The first audit and its five
proposals are not edited.

Section numbers here are prefixed `B` so that a citation of "§B3" cannot be mistaken for the first
audit's §3.

## B1. What this lane read

Marked **F** (read in full, to the end), **S** (read in sections, the sections named), **G** (read by search
only; every hit opened in context). Anything not listed was not read. This list was written as the reading
went, so the order is the order of reading.

### B1.1 The mass-battle design set (`.designs/systems/mass_battle/reference/`)

| document | how | what it holds that the first audit did not have |
|---|---|---|
| `military_layer_v30.md` | F | the campaign-side unit: a token with Type, Size, Discipline and **Experience** (Fresh, Seasoned, Veteran; +1 Power a step, capped by the faction's Military); muster output and prerequisites by territory Prosperity, Wealth and a **named officer's history** (cavalry, ranged); merging of same-type units; unpaid professionals lose Discipline; a siege action with a five-season cap and garrison supply; Accord gating muster. Half the file (§3) is the Church Influence formula and is not mass battle |
| `military_layer_v30_index.md` | F | generated index, no content |
| `mass_battle_flow_skeleton_v1.md` | F | a traced call graph of the engine as of `dcf38ef`, re-traced 2026-09-26. **Stale at HEAD**: its adapter (`resolve_mass_battle`, `_faction_to_unit`), its caller (`systems/factions/sim/faction_action.py`) and its driver (`engine/mc_v18.py`) no longer exist (`ls` fails on both paths). Its engine half is still an accurate outline of `run_battle`'s tick |
| `mass_battle_v30_index.md`, `_infill.md` | F | a generated heading index, and an infill that is a list of headings with nine stray sentences. The infill adds nothing the skeleton lacks; the one rule only it carries is PP-570's weight-of-numbers morale check, marked provisional |
| `mass_battle_v30.md` §A.1 to §A.14, Part B, Part D, Part E | F (re-read: this addendum's §B3 and §B4 are judged against it) | the first audit read it; re-read here for the hierarchy (§A.3, §A.3b, §A.4's sub-unit text, §A.5's span of control and ED-1090), the turn structure (§A.7), officers (§D.2) and the aftermath (§D.1) |

