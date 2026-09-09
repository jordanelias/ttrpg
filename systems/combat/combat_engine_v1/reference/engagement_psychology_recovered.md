# Engagement-Psychology Corpus — RECOVERED (scene-combat WS-0 salvage)

**Status:** Reconstructed-from-audit (mechanical-tier). The three originals
(`combat_engagement_psychology_findings.md`, `..._engine_proposal_unified.md`, `..._engine_proposal_refined.md`)
were staged in a dead sandbox `outputs/` and **never committed** — they survive only as *Reconciliation 3* of
`designs/audit/2026-06-28-combat-critique/recovered_reconcile_and_adversarial.md`, which audited all three against
the engine at HEAD. This file salvages their load-bearing content so WS-5 (The Approach + feint-as-attack) has a
grounded source. Tiers: T1 sport-science · T2/T3 fight-doctrine (the corpus self-corrected an "experts more
foolable" inversion). The salvage is the *findings*, not the lost prose.

## Why it matters

WS-5 reframes "regimes for controlling combat style" as **The Approach** — the pre-engagement contest to impose
your preferred paradigm — and dissolves feinting into the attack. This corpus is the psychological grounding for
both. Its headline: **most of the relevant psychology is already faithfully in the engine**; the genuine gaps are
narrow, which is exactly why WS-5 is a *reframe + small additions*, not new physics.

## A — Already faithful in the engine (confirmed against HEAD in Reconciliation 3)

These are not new work — they are the existing machinery WS-5's reframe sits on:

- **Disguise / telegraph = legibility.** `systems.legibility` (point 0.80 hard to read; cut/blunt 1.25 easy;
  +commit, +lunge) multiplies the defender's read. A low-legibility strike *is* the "from-nowhere" attack; a
  telegraph announces. → **This is feint-as-intrinsic already half-built**: the read-manipulation is a property of
  *how* you attack (head, commit, grip), not a separate move.
- **Active deception (feint) = the read contest.** `feint_eval` + the `read_d` vs `read_a` logistic is the
  forced-response/credibility contest, and (post-correction) is NOT a "better readers are more foolable" term.
- **Overcommit-exploit = the structural fact.** `read_win ∧ commit≥4 → Indes/sen steal + overcommit_exposure →
  riposte`. Rests on "a committed action can't simultaneously be defended" — biomechanics, not a perceptual deficit.
- **Two-sided measure** (approach / stop-hit / reopen) and **temperament** (`disp` → commit-skew / Vor-drift /
  counter-tilt) and **attacker-imposes-first / Vor** (the bounded-tanh initiative substrate) are all present and
  were explicitly NOT proposed for change.

**Implication for WS-5:** dissolving the separate `feint_eval` into the attack is a *consolidation of existing
faithful machinery* (legibility + read-contest are already the micro-read layer of an attack), which also clears
the audit's feint defects (the streak bug, the triple-debuff, precommit-isolated-to-feint) by construction.

## B — The genuine additions (the narrow gaps, distilled)

The corpus self-audited from ~11 candidate mechanics down to these — the distilled set WS-5 should carry:

1. **The regime-contest lens (§2) = The Approach.** The primary contest is *which regime the bout occupies* —
   a bias-space over **measure / contact / tempo**. The engine already produces measure emergently and biases
   tempo; the genuinely-missing pole is the **contact axis**. Hold the discipline (06-26): regimes are **biased
   weights over the existing `engagement()` machinery, NOT a regime-selection planner**.

2. **The contact axis (§5): clinch / disengage / choke** — the one genuinely-missing efficacy distinction.
   - **clinch** — force the fight to the close (the grappler's paradigm; consumes the dead `clinch` weapon field).
   - **disengage** — refuse/slip the bind (the rapierist's missing escape — your "Italian avoids the bind"); the
     loser of an imposition pays to void to it.
   - **choke** — the clinch's incapacitation finish.

3. **Wariness (ENG-1) — adversarially downgraded to low-sev, ship WITH the guard.** Commit-caution vs an unread
   tradition: scale the commit-depth skew by `WARINESS_K·(1−familiarity(ta,td))`, applied inside the existing
   `disp_lean` commit-skew (wrapper.py:98-106). **Mandatory hard spread-floor** so disposition+wariness can never
   collapse the {2,3,4,5} commit distribution to all-{2}. Byte-identical at familiarity 1.0. This becomes a property
   of the same micro-read layer as feint (you commit shallower against a style you can't read).

## C — Adversarial cautions carried forward (do not re-introduce washed-out mechanics)

- The pre-contact **seize** was cut 2026-06-05 after ablation ~0; do not revive it as-was (WS-4's seize decision).
- Every WS-5 lever clears the **ablation gate** (WS-8 §6) — non-zero bounded outcome impact or it is cut.
- Wariness must log as a deliberate 4th `familiarity` consumer and pass the worst-case spread-floor test.

## What this feeds

WS-5 consumes A (feint-as-intrinsic is a consolidation, not new physics), B (the regime/Approach lens + the
contact axis clinch/disengage/choke + wariness), and C (the ablation discipline). The contact-axis rows match the
`tradition_decomposition_v1.md` accesses (German *Ringen*→clinch; Italian *cavazione*→disengage).
