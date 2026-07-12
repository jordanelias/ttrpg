# Skills-Ecosystem Audit & Remediation — 2026-07-12

**Status:** EXECUTED (ED-IN-0038..0042). Phase 7 of the audit-ecosystem consolidation begun
2026-07-11 (ED-IN-0032..0037, Phases 1–6) — see `references/id_reservations.yaml`'s IN-lane
comment for that prior batch's scope. This round ran an independent 3-agent parallel audit of
all 15 live `skills/*/SKILL.md` files against the architecture CLAUDE.md currently describes,
plus a separate sweep for structural gaps in the skill/tooling ecosystem.

## Verdict summary

| Skill | Verdict (pre-fix) | Fixed this pass |
|---|---|---|
| prose-writer | CURRENT | — |
| valoria-chunker | CURRENT | — |
| valoria-canon-guard | CURRENT | — |
| valoria-vector-audit | CURRENT | — |
| valoria-editorial-register | CURRENT | + PP-NNN protocol added (net-new capability, not a fix) |
| valoria-simulator | PARTIALLY STALE | ✅ HANDOFF split pointer |
| valoria-arc-generator | PARTIALLY STALE | ✅ dangling exit-0 line |
| valoria-atomizer | PARTIALLY STALE | ✅ dead orchestrator ref, combat priority target, co-file checker |
| valoria-mechanic-audit | STALE | ✅ ledger destination, output location |
| valoria-module-adjudicator | STALE | ✅ ledger destination, dead function ref |
| valoria-resolution-diagnostic | STALE | ✅ ledger destination |
| valoria-workplan-navigator | PARTIALLY STALE | ✅ ledger pointer, dashboard awareness |
| valoria-compiler | STALE (worst of the 7 non-combat skills) | ✅ full rework — see below |
| valoria-dice-model | PARTIALLY STALE | ✅ dangling ref removed + continuous mode added |
| valoria-combat-simulator | STALE (worst overall — superseded implementation, not just stale docs) | ✅ **retired** to `deprecated/skills/` |

## The dominant repeated defect

Three skills — `valoria-mechanic-audit` (Mode D), `valoria-module-adjudicator` (Stage 3),
`valoria-resolution-diagnostic` (Stage 3 NERS verdict) — each independently instructed P1/P2
findings to append to the **frozen flat** `canon/editorial_ledger.jsonl`, rather than the live
lane-split `canon/editorial_ledger_<lane>.jsonl` files that have held all new entries since the
2026-07-02 cutover (CLAUDE.md §3). This is the same defect, landed three times, in three
different skills — evidence the 2026-07-02 lane-split migration touched the ledger files and
`valoria-editorial-register` itself but never propagated to the *other* skills that also write
ledger entries. `module-adjudicator` additionally cited a dead `append_to_register` function
that only ever existed in the retired orchestrator's `github_ops.py`.

All three now point at the correct lane-split files and cite `valoria-editorial-register`'s ID
Law section for the allocation protocol, rather than re-stating it inline (avoids a fourth copy
drifting independently next time the protocol changes).

## valoria-combat-simulator — retired, not patched

This was not simple prose drift. Its bundled `scripts/combat_sim.py` is a **fully independent,
hand-hardcoded implementation** — a 9-weapon roster (`Short-LightCut`, `Short-HeavyCut`, …,
`Unarmed`) frozen at a 2026-03-31 docstring date — with zero relationship to the current
40-weapon `combat_engine_v1` roster (post-2026-07-02 morphology expansion). Two things already
supersede it:

1. `designs/scene/combat_engine_v1/workbench/balance.py` — the actively-maintained canonical
   balance harness. Wilson-CI-validated, position-swapped, reuses the canonical `fight()`
   resolver directly (no parallel model), covers weapon/attribute/tradition/armour sweeps
   across the full 40-weapon roster. CLI: `python workbench/balance.py [weapon|attr|tradition|all] [n]`.
2. `sim/personal/combat.py` — itself carries an explicit `[DEPRECATED 2026-06-23]` banner
   pointing at `combat_engine_v1` as canonical; not usable as a fallback either.

Given a fully superseded parallel implementation (not a documentation gap), retirement was the
right fix — confirmed with Jordan via `AskUserQuestion` before executing (options were retire /
minimal-patch / rearchitect-to-wrap-`balance.py`; retire was chosen). See
`deprecated/skills/README.md` and `ED-IN-0039` for the retirement record.

## valoria-dice-model — canonical continuous resolver added

`valoria_dice.py` implemented only the legacy discrete d10-pool model. `params/core.md`'s
`Continuous Engine` section designates `net ~ Normal(μ·N, σ·√N)` as **canonical for the
videogame/Godot implementation specifically** (Decision E, 2026-05-15), with the discrete rule
demoted to legacy/TTRPG-mode. Added `continuous_outcome_probs()`/`continuous_quick_check()` —
closed-form via the normal CDF, continuity-corrected per the ER-2 fix — and validated by direct
comparison against the existing discrete Monte Carlo (p_full within 0.003–0.008 across pool
sizes 4/8/12 at TN7 Ob3, consistent with the doc's own claimed ≤0.029 max deviation). See
`ED-IN-0040`.

## valoria-compiler — the deepest prose rework

Four independent breaks, all fixed: a nonexistent `canon/editorial_ledger.yaml` citation (real
files are the lane-split `.jsonl` set); a `compilation_current` gate reading a field that does
not exist anywhere in the live `references/canonical_sources.yaml`; an orphaned
`compilation/v[N]/[system]_checkpoint_[N].md` output path that nothing in the repo reads or
writes; and zero awareness of the ED-1094 "merge ratifies by default" convention that has
governed ratification since 2026-07-02. Replaced with: currency read from the target doc's own
`## Status:` line (CLAUDE.md §4); two real output modes (in-place ratification — the common case
— or an explicit full export to a dated `designs/audit/` folder); and explicit ED-1094
bookkeeping (flip `## Status:`, ED ledger, `CURRENT.md` in the same commit, loud-not-silent
exceptions). See `ED-IN-0038`.

## Gaps found — NOT closed this pass (Jordan triage, ED-IN-0042)

Priority order; full context in that ledger entry:

1. **No Godot port-readiness tracking.** The conversion strategy doc
   (`designs/audit/2026-06-10-godot-conversion-strategy/`) has an open 8-item register and
   unexecuted Gate-0 preconditions; no skill or tool surfaces its status. Suggested shape: a
   lightweight status skill modeled on `valoria-workplan-navigator`.
2. **`tools/export_engine_params.py` has no skill-level reminder.** It's the CI-blocking
   oracle→Godot-JSON round-trip (ED-1050/1052) — a session editing `combat_engine_v1/config.py`
   needs to know to regenerate it, and nothing currently says so outside the CI gate itself.
3. **No sim↔port key-log parity checker exists at all** (CLAUDE.md §6: "still known-red"). This
   is a missing *tool*, not a missing skill — a skill can't wrap a check that isn't built yet.
4. **Session lane-scoping (CLAUDE.md §3) is unenforced anywhere** — not CI, not a hook, not a
   skill. Suggested shape: an advisory check (Stop-hook or SessionStart banner) diffing a
   session's touched-file lanes against its allocated `ED-<LANE>` ids.
5. **`compliance_check.py`'s CI-blocking mode is absent from `valoria_local.py`** (CLAUDE.md §8,
   ED-1082 — "local-green ≠ compliance-green") and no skill surfaces the trap.
6. **`broken_dependency_checker.py`/`patch_propagation_checker.py`/`freshness_gate.py` are also
   absent from `valoria_local.py`**, without the explicit documented rationale
   `compliance_check.py` has — flagged to confirm intentional vs. oversight; more likely a
   `valoria_local.py` fix than a skill gap.

Non-gaps checked and found adequately covered: dashboard regeneration (fully CI-automated, no
session action needed), ED-`<LANE>`-NNNN allocation (thorough in `valoria-editorial-register`),
the ~20 blocking/report-only CI validators (all hook-wired, no skill needed), and philosophy
compliance (`valoria-canon-guard` is correctly the only skill of that shape — the rest are
handled by automatic hooks, not a parallel gap).

## Full per-skill line-level findings

Preserved from the three parallel research agents' reports (dashboard-retrofitted 8 / remaining
7 / ecosystem gaps) — available in this session's transcript; not re-transcribed here to avoid
duplicating ~340 lines of already-actioned detail against the fixes listed above. Every fix
described in the verdict table was applied directly to the cited skill's `SKILL.md` (or, for
combat-simulator, by retirement) in this same commit.
