# Combat Engine — Four-Dimension Read-Only Audit + Remediation (SKELETON)

**Author:** PC-lane audit node (CLAUDE.md §0/§10) · **Date:** 2026-07-24 · **EDs:** ED-PC-0034..
**Subject:** `systems/combat/combat_engine_v1/` at the post-ED-PC-0029..0033 head (PR #231 merged).
**Charter (Jordan):** four independent read-only audits — **fiat, orphans, conflicts, tuning/balance** — each
covering *all directions and conditionals*; then resolve every finding in priority order, batch by batch, with an
adversarial audit after each batch.
**Prose:** `combat_four_dimension_audit_infill.md` (co-filed; method, evidence, per-finding detail, verification).
**Status: IN PROGRESS** — Batch 1 landed; Batches 2–6 pending.

## Method (skeleton)

Four `fable`-tier read-only auditors, structurally independent (each blind to the others' reasoning and to the
author's), read-only tooling, ablation/sim evidence required. Every finding re-verified by hand against the code
before acceptance — the anti-fabrication gate is leaky (CLAUDE.md §7), so no unverified claim is carried.
Aggregate evidence: ~96k ablation fights (orphans), 61,200-fight full grid + 30,158 mirror fights (tuning),
full-file reads + provenance spot-checks against `registers/editorial_ledger_pc.jsonl` (fiat, conflicts).

## Finding roster → remediation batches

| # | Dim | Finding | Sev | Batch | Status |
|---|---|---|---|---|---|
| F1 | tuning | `represent_measure_p` reads stale/native `sel_head`+grip → crowd gate path-dependent | high | 1 | **DONE** |
| F2 | conflicts | `overcommit_exposure` "floored at 0" false; negative value suppresses riposte below base | high | 1 | **DONE** |
| F3 | fiat | `contact.grab_sigma` edge-hazard sign-flips for grab skill > 1 | med | 1 | **DONE** |
| F4 | — | tradition-lever texture instrument under-powered (n=60, knife-edge) | — | 1 | **DONE** |
| F5 | orphans | 6 unread CFG keys, leaking into the Godot-facing engine-params JSON | high | 2 | pending |
| F6 | orphans | `CHOKE_BIND_K` — read lever multiplied by a hardcoded `0.0` at its only call site | high | 2 | pending |
| F7 | orphans | `close` damage param threaded through ~12 sites, never read | high | 2 | pending |
| F8 | orphans | 5 zero-caller functions; dead `Combatant.ready`; unreachable `QUAL`/`COVERAGE_GAP` `'partial'` | med | 2 | pending |
| F9 | orphans | retired imposition machinery still wired (`PREFERRED`/`preferred`/`profile`) | med | 2 | pending |
| F10 | conflicts | stale prose: poise `EFFECT_FLOOR`, facing-profile sign, "deliberately failing" tests that pass, phantom `disengage_prob`, `represent_p` magnitudes, `affords_halfsword` count, `TRUE_TIME_K` citation, `module_contracts` rows | med | 2 | pending |
| F11 | fiat+conflicts | `percussion_stagger`: inline second quality ladder + bypasses the `sel_*` single-source contract | med | 3 | pending |
| F12 | fiat | cut_thrust "versatile max" shear branch is dead (paid as thrust, read as swing) | high | 3 | pending |
| F13 | fiat | Nachreisen pursuit strike resolves at a flat `−0.3` σ, bypassing the σ-assembly | med-high | 3 | pending |
| F14 | fiat | `ATTACKER_BIAS=0.12` untagged/unledgered, duplicates the Vor system | high | 3 | pending |
| F15 | fiat | `UPSET_FLOOR=0.05` post-hoc result inversion (designer rule — tag, do not silently remove) | high | 3 | pending |
| F16 | tuning | deterministic first-actor race: a 1.5% tempo edge → 2:1 action monopoly; 20 g mass step swings 57↔42% | **structural** | 4 | pending |
| F17 | tuning | `closed = gap ≤ 0.3` latch is a cliff (+9pp across 2 cm); reach curve saturates by gap 1.5 | **structural** | 4 | pending |
| F18 | tuning | off-plate reach over-buff + identity erasure (26 weapons at 94±1; Jordan's ~0.75 target) | high | 4 | pending |
| F19 | tuning | plate damage path contradicts `adef_cap`: covert plate-killers (partisan/ranseur/guandao) | high | 5 | pending |
| F20 | tuning | jian/tsurugi plate paradox (0.04 gap-cap grading → ~95% of decided) | high | 5 | pending |
| F21 | tuning | flat `ADEF_CUT=−0.90` cutter cliff (a gambeson makes a falchion an 8% weapon) | high | 6 | pending |
| F22 | tuning | roster gaps: sparr_axe horn, falchion point, greatsword/odachi half-sword; staff can't wound | med-high | 6 | pending |
| F23 | orphans | ability/`eff_cw` surface hollow: 5 of 8 channels are identity ×1.0 for every legal build | med | 6 | pending |

**Cleared (checked, not findings):** no name-keyed weapon/tradition branches in live resolution; imposition gate is a
verified no-op; provenance spot-checks (ED-1041, ED-901, ED-PC-0002/0009/0022/0023/0027/0029..0033) all passed — **no
fabricated citation found**; wound-Ob / reach / armour-defeat / armour-fade sign conventions consistent across all
consumers; PEN_THR light-inertness and the represent-gate RNG-stream inertness hold exactly as documented; the
"Combat Pool defined three ways" hazard (CLAUDE.md §5) has collapsed to one quarantined stale surface.

## Batch ledger

| Batch | Scope | ED | Result |
|---|---|---|---|
| 1 | correctness bugs (F1–F4) | ED-PC-0034 | full suite green (686 passed, 1 xfailed) |
| 2 | dead code + stale prose (F5–F10) | — | pending |
| 3 | fiat retirement (F11–F15) | — | pending |
| 4 | structural thresholds (F16–F18) | — | pending |
| 5 | plate damage ↔ adef_cap (F19–F20) | — | pending |
| 6 | roster + cut grading (F21–F23) | — | pending |
