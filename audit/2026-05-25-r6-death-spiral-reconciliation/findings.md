# R6 Death Spiral Reconciliation Audit

**Date:** 2026-05-25
**Audit type:** Reconciliation between chat-handoff claims and main HEAD + canon.
**Main HEAD at audit time:** 9763d23
**Trigger:** Session handoff from prev chat citing two "death spirals" (Hafenmark Mil, Tension band L) in unpushed branch `patch-round-2-canon-military`. Branch state lost on container reset; only chat handoff text survives.

## Verdict

**Main is the canonical-baseline-of-record.** R6 branch work moved baseline *away* from canon, not toward it. The two reported "death spirals" were artifacts of canon drains the R6 branch had added to sim; main has none of those drains and produces canon-target balance exactly. No patches in this audit. Canon→sim implementation gaps logged for future scheduling.

## F1 — Main N=100 matches canon target exactly

| Metric        | Canon target | Main HEAD (seed 0, n=100) | R6 "final" (handoff-reported) |
|---------------|--------------|---------------------------|--------------------------------|
| Crown         | 40           | **40.0**                  | 37                             |
| Church        | 5            | **5.0**                   | 11                             |
| Hafenmark     | 1            | **1.0**                   | 0                              |
| Varfell       | 54           | **54.0**                  | 52                             |
| battles_mean  | —            | 34.2                      | 17.2                           |

Reproduce from `ttrpg/` root, HEAD `9763d23`:
```
python3 -c "import sys; sys.path.insert(0, '.'); import random; random.seed(0); import sim.mc_v18 as mc; r = mc.run_batch(n=100, base_seed=0); print(r.win_share, r.battles_mean)"
```

Runtime ~280s. Hafenmark winning 1% is canonical baseline, not pathology. Varfell at 54% is canonical, not over-dominance. R6's halved `battles_mean` (34.2 → 17.2) suggests R6's added drains were suppressing the action that produces battles.

## F2 — Handoff's drain locations do not exist on main

Chat handoff claims, verified against `git show 9763d23`:

| Handoff claim                                                          | Verification result                                                                                                                |
|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| "Battle losses drain Mil −0.1 at `faction_action.py:420` and `:454`"  | `faction_action.py` on main is **228 lines total**. No `adjust('Mil', …)` call anywhere in file.                                  |
| "§4.3 Turmoil 3-4 drains L−0.25/season continuously across all factions" | Section is **§4.4**, not §4.3 (numbering error in handoff). No L-drain handler exists in `accounting.py`, `ci_track.py`, `season.py`, or any sim file. |

Files audited (grep for `adjust\(.*['L'\|'Mil'\|'Mandate'\|'MS']` patterns): `faction_action.py`, `massbattle.py` (1905 L — only `Mil` references are `Unit.Mil` field init and one `[GAP]` docstring), `season.py`, `accounting.py`, `ci_track.py`, `ms_track.py`, `ip_track.py`, `rs_track.py`, `mc_v18.py`.

## F3 — Canon→sim implementation gaps (not for fix in this audit)

The following canon-specified mechanics are unimplemented in current sim. Main's calibrated balance assumes these gaps. Closing any of them is a balance project requiring N=100 telemetry per increment, not a single-commit fix.

### §B.3 mass_battle — Battle-loss Mil drain
> "Attacker wins → Defender Military −1; Defender wins → Attacker Military −1."

No `adjust('Mil', -1)` call in `massbattle.py`. Battle outcome modifies units in scope but not the parent faction's institutional Mil stat.

### §E.1 / §E.4 mass_battle — Battle → MS drain
> §E.1: "Substrate Fracture | Any inter-faction Battle | MS −1 (Campaign/War scale: MS −2)"
> §E.4: "Maximum MS change from battles: −3 per season (regardless of battle count within season)."

`world.battle_count` is incremented at `faction_action.py:187` but read only by `mc_v18.py` for reporting (`CampaignResult.battle_count`). `ms_track.apply_ms_delta()` exists but is not called from any battle pathway. §E.3 carve-outs (covert ops, Altonian Vanguard siege-only, Popular Uprisings, first 2 seasons of Löwenritter Coup) would need encoding alongside any implementation.

### §4.4 ci_political — Turmoil → Mandate
> Strain 3-4: "All factions: Mandate check at Accounting (Mandate pool vs Ob 1). Failure → Mandate −1"
> Strain 5-6, 7-8, 9-10 escalations with Accord-cap and additional MS drain at strain 9-10.

No Turmoil-band stat-effect handler exists. Confirms the handoff's intuition that this is a drain source — but the drain is **Mandate (M)**, **probabilistic** (Mandate-vs-Ob check), and **at Accounting only** (not continuous). The handoff's "L−0.25/season continuously" framing is wrong on stat (L vs M), wrong on frequency (continuous vs Accounting), wrong on magnitude (−0.25 vs −1), and wrong on determinism (continuous vs check-gated).

### §E.2 mass_battle — Deferred Accord/IP/Strain chain
ED-743 (2026-04-29) redirected battle-occurrence IP/Strain triggers to deferred Accord-based mechanism. Accord erosion → next Accounting → IP advance per `peninsular_strain §3.2` and Strain advance per `peninsular_strain §4.1`. Currently no accord_at_accounting handler in sim. ED-743 supersedes ED-623 (+2 → +3 IP per battle-season).

## F4 — R6 lineage interpretation

Most-plausible reading without recovered diff: R2–R6 was **implementing the F3 canon drains** into sim, observed the spirals their addition produced, and layered recuperate mechanics to compensate. The R6 "final" baseline (37/11/0/52, battles 17.2) is (canon drains added) + (partial recovery scaffolding), and is further from canon target (40/5/1/54) than main is. The "pairing principle" question — whether every spend needs a paired recuperate — was framed inside that drift, against the R6 stack, not against canon-as-implemented. The question becomes well-posed only after F3 gaps are closed; against current main it has no targets.

`[ASSUMPTION: this lineage reading — basis: R2-R6 commit content not recoverable; reconstructed from handoff narrative + canon→sim gap pattern. If specific R6 work was non-drain (e.g., new actions, AI improvements), it should be recovered separately via `conversation_search`.]`

## Recommendations

1. **Hold F3 as backlog, not urgent.** Closing any gap will re-break main's calibrated balance. Schedule as a multi-session project (§E.1 MS most discrete; §B.3 Mil and §4.4 Mandate both interactive with action economy). N=100 telemetry per increment, expected re-tune passes 2–4 per drain.
2. **No re-stack of R6.** Branch state was never pushed; container reset destroyed it. Cost of recovery (via `conversation_search` archaeology + manual re-derive) exceeds value, given F4's reading that R6 was iterating against drains main doesn't have. If R6 contained discrete non-drain improvements worth salvaging, recover those individually.
3. **Next priorities per handoff are independent of this audit:** Treaty AI (unlocks Peninsular Sovereignty victories) or Parliamentary Transfer (needs CB tracking). Either is unblocked.

## Sources

**Canon (verbatim citations above):**
- `designs/provincial/mass_battle_v30.md` §B.3 (battle Mil −1), §E.1 (battle MS −1), §E.2 (ED-743 deferred chain), §E.3 (exception carve-outs), §E.4 (−3/season cap)
- `designs/provincial/ci_political_v30.md` §4.4 (Turmoil → Mandate check by strain band)
- `canon/02_canon_constraints.md` (game-design constraints GD-1/2/3 referenced by mc_v18)
- `references/canonical_sources.yaml` (path canonicalization)

**Sim audited (no modifications):**
- `sim/mc_v18.py`, `sim/provincial/faction_action.py`, `sim/provincial/massbattle.py`
- `sim/peninsular/{season,accounting,ci_track,ms_track,ip_track,rs_track}.py`
- `sim/autoload/game_state.py` (battle_count field)

**Other:**
- Chat handoff 2026-05-25 — captured in session conversation, not committed to repo
- N=100 reproduction at HEAD `9763d23` performed in audit session, `random.seed(0)`, `base_seed=0`
