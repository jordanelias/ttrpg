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
| Squad-engagement concept v5: build slate (Part A) + all six Part C items ruled by Jordan 2026-09-25 | `ED-MB-0067` (5 rows) / `ED-MB-0068` / `ED-MB-0069` / `proposals/2026-09-25-squad-engagement-synthesis.md` | **d.1 EXECUTED and green**: `massbattle.py:_faction_to_unit` derives morale from `Faction.Sta` (round-half-up, floor 1/ceil 7); superseded the untagged morale-starting-formula sentence at `mass_battle_v30.md:230-231` — NOT PP-711, which is a different rule (the morale-reset) unaffected by this change. **Tier-1 build slate (A1 routes / A2 perception orders / A4 go-codes / A6 ammo) EXECUTED and green, `ED-MB-0069`**: three build/fix rounds, agonist-antagonist relay (Sonnet build, Opus adversarial review ×2), every round independently re-verified by direct execution — full detail and the F1-F13 finding list in the ledger row. `MB_AMMO_ENABLED` defaults ON; `bat.py`'s `cell_legacy_mor1` digest re-recorded. Still open: A8 (`ROUT_CASCADE_FRAC` sweep) and every Tier-2 item (A3+C5 officers, A7 terrain, C2/C3 coupling formula, C4's roll) — deferred, need a design/slice pass first. |
| Two disclosed, NOT-YET-fixed loose ends surfaced during the Tier-1 adversarial review | `ED-MB-0069`'s ledger row | (1) `tests/valoria/test_mass_battle_byte_exact.py`'s `BAT_PY` constant still points at `tests/sim/mass_battle/bat.py` (moved to `systems/mass_battle/sim/bat.py`) — the test currently passes/skips/xfails cleanly (no false green), so this is a stale-path fix, not urgent, but it is why `unit_legacy_mor0`/`cell_legacy_mor0` can't be re-verified against a byte-exact reference in this sandbox. (2) whether PP-711 (morale reset between battles) is actually enforced in the live campaign is UNDETERMINED — `reset_morale_between_battles` has no confirmed production call site (grep-verified); a docstring in `massbattle.py` wrongly claimed one and was corrected in place. Next step: check whether `engine/mc_v18.py`'s campaign loop achieves the same effect by building a fresh `Unit` per battle instead. |

## Standing orders — do not re-raise, do not do
| order | source |
|---|---|
| Two-trees fork is CLOSED — canon is `systems/mass_battle/sim/`; do not re-open which tree is oracle | `references/module_contracts.yaml:636` note, `ED-MB-0043`/`ED-IN-0127`/`ED-IN-0128` |
| `MB_STOCHASTIC_ROUT` default is ON (ratified) — do not treat as an open flag | `systems/mass_battle/sim/config.py:175` |
