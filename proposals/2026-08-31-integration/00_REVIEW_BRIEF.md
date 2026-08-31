# Adversarial review brief — the two work lines

## Status: BRIEF (2026-08-31) — planned by Fable 5; reviews by read-only critics; writing by Opus/Sonnet.

## The two bodies under review
**(a) THE NPC MATRIX / SEASON MACHINE** — `proposals/2026-08-30-play-space-coverage/`
plan · roster and findings · the machine views · six season lanes (~56 probes) · the coverage matrix ·
the gap report. Plus the fixes it produced: `proposals/2026-08-30-fixes/` (five documents).

**(b) THE ARCS** — `proposals/2026-08-30-arc-reachability/`
brief · three lanes over ~83 arcs · the synthesis.

## The code-shape surface — RESOLVED BY JORDAN 2026-08-31
Jordan first named "PR#341 proposed code shape"; asked, he confirmed **#342 is correct**. So:
**`proposals/2026-08-29-valoria-from-scratch/11_code_shape.md` (PR #342) is AUTHORITATIVE** for the
compliance axis. PR #341's owner map drops to a secondary lens, useful for its *discipline* only —
one owner per object, no orphans, no two-owner contests — since it analyses the superseded v2 suite
and its object list binds nothing. Both are described below; weight them accordingly.
- `proposals/2026-08-29-fable5-throughline-critique/04_keying_and_owner_map.md` (**PR #341**) — an
  owner map, keying register and modularization analysis. Note it analyses the *v2* suite, not the
  from-scratch one, so its **discipline** transfers (one owner per object; no orphans; no two-owner
  contests; the under/over-distillation tests) while its *object list* does not.
- `proposals/2026-08-29-valoria-from-scratch/11_code_shape.md` (**PR #342**) — the actual proposed
  code shape: the three signatures, the ownership table, the forbidden list, the module rules R-1/R-2,
  determinism, and the four structural tests.

## The four axes, and what each means here

**FACTUALITY.** Are the claims true? Check counts, quotes and citations against the documents they
name. **This is not a formality: this session has a documented record of synthesis error** — an audit
cited an object that does not exist ("the event-class parity list"), findings recorded as applied were
not applied, and a roster row was reported null when canon had it. Assume nothing; verify.

**LOGIC.** Do the conclusions follow from the evidence? Specifically test the inferential leaps, e.g.
whether "19 of 55 have a blocked core" supports "the most common single result"; whether
`MECHANISM: NO / STORY: YES` is legitimately a *win* rather than a redefinition of success; whether
convergence across lanes is real independence or shared-prompt contamination.

**RIGOUR.** Is the method sound? Sampling and selection bias, the verdict criteria's discriminating
power, whether the control was a fair control, whether verdicts are reproducible from the stated
evidence, and whether any lane graded its own homework.

**CODE-SHAPE COMPLIANCE.** Do the findings, and especially the **proposed fixes**, comply with the
proposed code shape? The forbidden list is explicit — no `World` parameter on a decision function, no
masking view, no function taking many persons and one event, no stored aggregate, no knowledge on the
thing known, no second resolver, no tier field on a faction, no flat additive modifier, no scheduled
recovery tick, no per-entity branch, no authored opportunity object. Plus R-1/R-2 (a module reads and
writes only its own state) and the owner-map discipline (one owner; no orphans).

## Discipline
- **Read-only. Attack, do not repair.** A proposed fix is not yours to rewrite.
- **Rank by severity and state a verdict**: SOUND · SOUND-WITH-CORRECTIONS · UNSOUND, per body.
- **Credit what survives.** An adversarial review that finds only faults is not calibrated and cannot
  be trusted on the faults it does find.
- Where the two code-shape surfaces disagree, say so rather than picking.
