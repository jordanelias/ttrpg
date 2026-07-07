# Refuter R2 — faction oracle claims

_Archived verbatim from the agent's final message (2026-07-07)._

## Refutation Record — Independent Refuter R2

Scope note: I read only the charter (per relay-independence). While grepping broadly for "loop_safety"/"faction_canon" references I incidentally surfaced snippets of `cluster_C-FA.md`, `cluster_C-EMERGE.md`, `cluster_C-STUB.md`, `cluster_C-REACH.md` in grep output (they matched unrelated search terms). I did not read those files and did not use their content as evidence — all verdicts below rest on my own direct reads of `sim/`, `designs/`, `canon/`, `references/`, and one live Python probe.

---

**Claim 1 — sim faction oracle pre-LPS-1 defect**
**VERDICT: QUALIFIED**
- `sim/autoload/game_state.py:84-102` — `Faction` dataclass stat fields are exactly `{L, Sta, W, I, Mil}`; no Mandate/Treasury attribute. Zero hits for "treasury" anywhere in `sim/*.py`.
- `sim/personal/parliamentary_vote.py:13,21` and `sim/provincial/crown_initiative.py:135` explicitly alias `Mandate == Faction.L` — the sim treats scalar L as Mandate directly.
- `designs/provincial/faction_canon_v30.md:211-219,239-241` confirms LPS-1 (Jordan ruling 2026-05-30) declared the faction-scalar L/PS lineup "the defect" and specified Mandate = clamp(round(7T/(T+6))) over per-settlement q_s = 0.5L+0.5PS (`designs/territory/settlement_layer_v30.md:147-179`).
- **Refuting evidence found:** `sim/territory/registry.py:41-61` — the `Settlement` dataclass *does* declare per-settlement `legitimacy: int = 0` / `popular_support: int = 0` (§1.8 fields, added by schema migration #3, 2026-06-23, "closes audit gap G1" per `game_state.py:179-186`). This falsifies the claim's literal "no per-settlement Legitimacy/Popular-Support ... anywhere in sim/."
- However these fields are inert: grep confirms no other file in `sim/` reads or writes `.legitimacy`/`.popular_support`; no Mandate-aggregation formula (`T = ΣW_s·q_s/7`, `clamp(round(7T/(T+K)))`) exists anywhere; no `λ_continuity/λ_procedural/λ_expectation/λ_violation` accrual dynamics (`faction_canon_v30.md:157`) appear in any `.py` file.
- Net: the claim's *substance* (sim behaves per the pre-LPS-1 scalar model; no working Mandate/Treasury/accrual dynamics) is fully verified true; its literal "nowhere" wording is false (an unwired stub exists).
- Intent gate: **NOT-INTENDED** — the dead fields were added specifically to close a tracked audit gap (G1), evidencing acknowledged in-progress migration, not a deliberate choice to keep the scalar model.

**Claim 2 — Varfell/Hafenmark hardcoded invalid, falls through to Conquest**
**VERDICT: CONFIRMED**
- `sim/provincial/faction_action.py:90,106,128-129` — `_try_faction_unique` branches only on `faction.name == 'Crown'` / `'Church'`; line 128-129 `# Varfell + Hafenmark — BLOCKED on Pass 2d/2e + contamination audit` / `return 'invalid'` unconditionally.
- `faction_action.py:55-68` — `faction_take_action`: `roll<0.30` tries faction-unique; comment at line 62 "fall through to Conquest if faction-unique unavailable"; next branch `roll<0.65` is Conquest.
- Intent gate: **DELIBERATE** — explicitly commented, tracked interim state ("BLOCKED on Pass 2d/2e + contamination audit"), not a silent bug.

**Claim 3 — no damper on territory→Mil→conquest→territory; ledger's DAMPED(0.966) is a different loop**
**VERDICT: CONFIRMED**
- `faction_action.py:132-189` (`_try_conquest`) and `sim/provincial/massbattle.py:1791-1852` (`resolve_mass_battle`): pure Mil-derived unit resolution; loser takes flat `L-10`/`accord-25`, no catch-up bonus for weaker attackers, no size/territory-count-scaled penalty, `terrain=None` hardcoded (no defender-terrain modifier).
- `sim/peninsular/accounting.py:37-79`: no Mil decay/overextension tax; the one theoretically-available check, `insurgency_pipeline` (GD-3), fires only on `Uncontrolled` (owner=None) territories — grep across `sim/*.py` finds no code path that ever sets `territory.owner = None`, so this valve can never engage from the conquest loop.
- `archives/audit/2026-06-04-loop-safety-ledger/loop_safety_ledger.md:39,56,106`: "DAMPED (0.966)" is explicitly the **"D-series accounting (CI/Treasury/L-PS)"** row (DA outcomes → L/PS → strictness → DA Ob, damped via "Mandate↔L/PS mean-reversion, settlement §1.8") — the ledger's §2 register has no row at all for a territory/Mil/conquest loop. Per Claim 1, that Mandate↔L/PS mechanism isn't implemented in `sim/` anyway, so the "verified damped" verdict describes a loop that exists only on paper (and lives only in `archives/`, not cited by `CURRENT.md`).
- Intent gate: **NOT-INTENDED** — `sim/tests/test_mc_v18_regression.py:6-11` and CLAUDE.md §7 explicitly flag the resulting degenerate win-share ("one faction ~87%, two at 0%... nothing flags") as a known open problem.

**Claim 4 — settlement_layer_v30.md internal 5× Treasury contradiction**
**VERDICT: CONFIRMED**
- `designs/territory/settlement_layer_v30.md:47,51` — "Prosperity × 50 ... Gold income contribution to faction Treasury" / "Local Economy contributes to faction Treasury income."
- `designs/territory/settlement_layer_v30.md:169` — "faction Treasury income = `Σ settlement Prosperity × 10`, derived_stats §8.1."
- Cross-corpus corroboration (not required, but reinforces it isn't a fluke): `designs/scene/derived_stats_v30.md:308` (×10) vs `:378` (×50, tagged "PENDING" at `:550` — a caveat `settlement_layer_v30.md`'s own §1.3 table lacks).
- Doc is `## Status: CANONICAL — approved 2026-04-17` (line 3); §1.8 (the ×10 citation) was inserted later, "LPS-2e ... Jordan ruling 2026-05-30" (line 147) — a later edit that never reconciled against the original §1.3 table.
- Intent gate: **NOT-INTENDED** — no PENDING/ED marker reconciles the two figures anywhere in the document.

**Claim 5 — victory.py PS/Turmoil vs faction-doc PS/Popular-Support collision**
**VERDICT: CONFIRMED**
- `sim/autoload/victory.py:55,72-73,92` — "Canon: ... PS <= 6"; `# Political Stability is a world clock`; `ps = world.clocks.get('Turmoil', 0.0)  # PS mapped to Turmoil clock`.
- `canon/02_canon_constraints.md:38` and `victory.py:11-12` spell "Political Stability" in full everywhere in canon — "PS" as its shorthand is local to this module's comments.
- `designs/territory/settlement_layer_v30.md:154-155`, `designs/provincial/faction_canon_v30.md §5.1-5.3` repeatedly use "PS" = Popular Support.
- Intent gate: **NOT-INTENDED** — reads as an incidental local abbreviation, not a deliberate namespace decision.

**Claim 6 — live contest path uses deprecated legacy stub, not the promoted kernel; module_contracts declares dice_pool**
**VERDICT: CONFIRMED**
- `sim/personal/contest/__init__.py:20-28` (the package's own docstring): "The two live importers of the OLD single-compare stub keep resolving through this package, which re-exports the stub's public API from `sim.personal.contest_legacy_stub` ... `scene_dispatch.py:105 -> contest.run_contest(...)`; `parliamentary_vote.py:42 -> PERSUASION_*`."
- `sim/cross_scale/scene_dispatch.py:105-106` confirms the live call.
- Grep for `resolve_contest`/`Bout(` across `sim/`: matches only inside the `contest/` package itself and `sim/tests/test_contest_kernel.py` — zero non-package, non-test callers.
- `references/module_contracts.yaml:429` — `resolver: dice_pool` for `module: social_contest`.
- Intent gate: **DELIBERATE** — explicitly documented, staged "deprecate-not-delete" migration ("The NEXT stage folds the legacy run_contest into the wrapper"), a known tracked interim state.

**Claim 7 — legacy vs kernel pool formulas diverge structurally; large probability gap**
**VERDICT: CONFIRMED**
- `sim/personal/contest_legacy_stub.py:121-127` — `pool = (primary*2) + history + (-1*wounds) + fatigue_penalty; return max(1, pool)` = `max(1, 2P+H−W)`.
- `sim/personal/contest/primitives.py:208-211` — `Pool.BASE = 3  # [SEED]`; `size(faculty) = max(5, faculty*2 + Pool.BASE)` = `max(5, 2P+3)`; `resolver.py:286` confirms this is the pool actually used in kernel resolution.
- Grep for "wound"/"History" in `sim/personal/contest/*.py` (excluding tests): zero hits — kernel is provably History-invariant and wound-blind.
- `designs/scene/social_contest_v30.md:119` (canon §3) = "(Primary Attribute × 2) + History bonus" — matches the legacy stub, not the kernel's flat placeholder constant.
- Independent probe (`dice_engine.roll_pool`, TN7, N=200,000/scenario, 3 representative contestant pairs) comparing opposed-pool win-probability under legacy vs. kernel pool sizes: gaps of **9.5pp, 28.9pp, 15.9pp** — same order of magnitude as the cited 15–27pp (exact figure is scenario-dependent, not a fixed constant, but the claim's structural thrust is corroborated by direct simulation, not just formula inspection).
- Intent gate: **NOT-INTENDED** — `Pool.BASE = 3  # [SEED]` is self-labeled a placeholder; the package docstring defers the "v30 surface re-skin" (reconciling to canonical formulas like social_contest_v30.md §3) to an explicit future stage.

---

**Summary:** 6/7 CONFIRMED, 1/7 QUALIFIED (Claim 1 — true in substance, false in its literal "nowhere" wording due to an inert schema stub in `sim/territory/registry.py`). No claim fully REFUTED. Intent split: 2 DELIBERATE (Claims 2, 6 — both explicitly documented staged/interim states), 5 NOT-INTENDED (Claims 1, 3, 4, 5, 7 — unreconciled gaps, placeholders, or incidental collisions with no ratifying note).
