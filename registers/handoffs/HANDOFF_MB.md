# Handoff — MB (Mass Battle)

**Pointer index.** Every row names where its fact lives — a ledger id (its LAST row governs), a `path` or `path:line`, or a command to run. This file restates no count, status or date of state: open or run the pointer. The narrative this file used to carry is verbatim in `registers/handoffs/HANDOFF_MB_history.md` (and finished work in `HANDOFF_MB_closed.md`).

## Open
| item | where it lives | next step |
|---|---|---|
| Envelopment fork: combined-arms reframe vs gated seal-failure gradient | `ED-MB-0039` | Jordan rules (A) vs (B) |
| Remaining Tier-3 design calls (depth cap, envelopment-as-morale-collapse, graded cavalry refusal, Command sigma-ceiling, yield split) | `ED-MB-0041` | Jordan rules per item |
| `mass_battle` contract's `state: []` — empty, blocks port ripple/formula/pointer audits | `references/module_contracts.yaml:636` | Jordan rules whether/how to populate |
| CEV naming (rename to Clausewitz/Beyerchen friction?), dual 2:1 validation targets, emergence verdict | `ED-MB-0045` | Jordan rules each sub-item |
| `config.py` comment contradicts the shipped default | `systems/mass_battle/sim/config.py:315-317` | edit comment to match `MB_FRICTION_CEV` default `'1'` |
| R3 gauge scenario never engages (both sides `stance:'hold'`) | `tests/sim/gauge_mb.py:330-331` | apply the named one-line engineering fix (`ED-MB-0044`) |
| Dead-primitive dispositions unexecuted (`_octagon_dmg_mod`/`_SHAPE_BUILD`, `provenance.py`, `resolve_internal_collisions`) | `ED-MB-0057` | execute or re-adjudicate each disposition — `resolve_internal_collisions` re-adjudicated to DELETE, `proposals/2026-09-25-squad-engagement-synthesis.md` Part B |
| Squad-engagement concept v5, audited and reconciled against MB canon: build slate (Part A) + six items for Jordan (Part C) | `ED-MB-0067` / `proposals/2026-09-25-squad-engagement-synthesis.md` | Jordan rules Part C |

## Standing orders — do not re-raise, do not do
| order | source |
|---|---|
| Two-trees fork is CLOSED — canon is `systems/mass_battle/sim/`; do not re-open which tree is oracle | `references/module_contracts.yaml:636` note, `ED-MB-0043`/`ED-IN-0127`/`ED-IN-0128` |
| `MB_STOCHASTIC_ROUT` default is ON (ratified) — do not treat as an open flag | `systems/mass_battle/sim/config.py:175` |
