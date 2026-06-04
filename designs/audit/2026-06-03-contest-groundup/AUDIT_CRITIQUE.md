> **SUPERSEDED 2026-06-03** by `AUDIT_RECONCILED.md` (the master). Retained as history — do not follow
> independently. Its corrections are folded into the master; its leniency on `resist` (it retracted the
> finding wholesale and moved Robustness toward a pass) was pulled back there to "scale-fragile, MEDIUM,"
> keeping Robustness at partial.

---

# Adversarial Critique of the Full Audit (2026-06-03)

**Verdict.** The audit's HIGH headline finding is **false** — a ten-line seeded simulation shows the
`resist` mechanic works roughly as intended. The audit reached that wrong conclusion because it ran **no
simulations at all**, reasoning analytically where measurement was cheap and decisive. That single
methodological gap produced a false headline and left the audit's other quantitative claims unconfirmed
(two are now confirmed post-hoc). Beyond that, several findings are over-severitied, one is mis-mapped to
the wrong NERS criterion, and the verdict hedges. Net: the audit is **partially reliable** — its static,
architectural observations mostly stand; its behavioural and quantitative claims were untrustworthy as
issued, and one was simply wrong. The system is in **better** NERS shape than the audit concluded.

`[SELF-AUTHORED — bias risk]` This critiques my own audit of my own system — two layers of bias. The
specific thing I am incentivised to miss: the "inert mechanic" headline is dramatic and makes the audit
look sharp, so I am disproportionately reluctant to retract it, and tempted to offset the retraction by
foregrounding the two claims that *did* survive. The retraction is the most important output here; it
leads.

---

## C1 — The headline finding (resist inert) is REFUTED · CRITICAL

Audit finding 1 (HIGH) claimed `resist` cancels in the `PersuasionTrack` difference and is inert.
Measured (pools fixed at pro=10 / anti=8; only the abstainer count, hence `resist`, varies; seeded
identically so raw rolls align):

```
  resist=0 (0 abstain): committee 0.338 · fail 0.245 · pass 0.417
  resist=1 (1 abstain): committee 0.365 · fail 0.231 · pass 0.405
  resist=2 (2 abstain): committee 0.433 · fail 0.199 · pass 0.368
```

`resist` systematically pulls the outcome toward committee (committee +0.095, pass −0.049, fail −0.046
across 0→2) — the **intended** effect. The finding is wrong.

**Why the analysis failed.** My algebra ("subtract the same constant from both, the difference is
unchanged") assumed the common case is no-clipping. It is not: the pools are mandate *sums* (8–10), so
`roll_net` means are ≈3–4 — comparable to `resist` (1–2). `roll_net(8) < 2` occurs ~30% of trials, so the
`max(0,·)` floor bites *often*, and when it clips one side the difference does change, compressing the
track toward the neutral start. I noted this floor case in the finding and dismissed it as an "edge case";
it was the whole mechanism. I had the right observation and weighted it exactly backwards.

The one residual nit that survives: the magnitude of the compression is a tuned side effect of the floor,
not a designed quantity, so "does `resist` produce the *intended size* of committee-pull?" is a fair
question — but that is a LOW calibration note, not a HIGH inert-mechanic bug.

## C2 — Zero empirical work in a "comprehensive" audit · ROOT CAUSE · CRITICAL

The audit was entirely static (reading + arithmetic). There is a code-execution environment and a
62-test harness; running the three load-bearing claims took one block. Had I run it, C1 would not have
shipped. The same omission left two further claims unverified until now:

- **Faculty saturation (audit Phase 3) — CONFIRMED.** Mean reception degree by faculty: 1→1.60, 2→1.96,
  3→2.49, 4→2.63, 5→2.73, 6→2.80, 7→2.86. Marginal Δ: +0.35, +0.53 (steep through 3) then +0.14, +0.10,
  +0.07, +0.06 (flat). The inflection is at **faculty 3** (the Ob 2→1 floor), not "~4" as the audit
  estimated, and my estimated P(Overwhelming) figures (~0.7/~0.87) were close to actual (0.76/0.91) but
  were presented without an `[UNVERIFIED]` flag.
- **Bounded-loop null (audit Lesson 5) — CONFIRMED.** Ethos-spam vs a maximally sympathetic low-discipline
  judge: adv at budgets 10/20/40/80 = 22.8 / 44.0 / 84.8 / 163.1 (ratios 1.93 / 3.72 / 7.16 against an ×8
  budget span — slightly *sub*-linear), standing pinned at the 10.0 cap throughout. No acceleration; the
  null holds.

A static-only audit of a stochastic system is structurally inadequate. Measurement is not optional
"extra rigour" here; it is the discriminator the audit's own `honest_findings` discipline demands.

## C3 — Severity ranking mixed two axes · MEDIUM

`resist` was ranked #1 (HIGH) on *defect-clarity* (it was unambiguously wrong-looking). By the
diagnostic's own impact / exposure / irreversibility rubric it is LOW: a minor adapter flavour mechanic,
reachable only with high-mandate abstainers, fully reversible — and now not a defect at all. The ranking
never declared which axis it sorted on, and silently used "clearest bug" as a proxy for "highest impact."
By impact, the headline should have been the uncapped evidence weight or the Standing hub, not `resist`.

## C4 — Finding 2 (Standing conflation) overstates the coupling · MEDIUM

The audit justified the Lesson-1 finding with "you cannot change how much standing licenses an attack
without also changing how hard arguments land." That is partly false. The three effects have **separate
coefficients** — `SelfGating.MARGIN`, `Readiness.W_STANDING`, `Resonance.ETHOS_UNLOCK` — and are
independently tunable. What is shared is the *input* (standing's value), not the tuning knobs. The
Lesson-1 concern (one conceptual variable carrying three conceptual jobs) is legitimate, but the stated
mechanism is wrong, and the severity should drop to LOW.

## C5 — Finding 4 mis-mapped to Smoothness · MEDIUM

The audit exempts intended thresholds under Lesson 6, then flags the deliberate `deg >= 2` gate as an
"accidental-looking" Smoothness cliff — contradicting its own exemption logic. `deg >= 2` is a design
choice (I wrote it), no more accidental than the win/defeat thresholds it sits beside. Its real defect is
**information loss** — the engine resolves Failure vs Partial and the contest discards the distinction —
which is a *Necessary* concern, not a Smoothness one. The NERS-S "partial" rests partly on this mislabel;
S is cleaner than the audit stated.

## C6 — Finding 3 (evidence cap) inconsistent with the rest of the audit · LOW

The engine trusts the author on every `[SEED]` (`MERIT_SCALE`, `base_ob`, all venue weights). Singling out
evidence `weight` as MEDIUM while not flagging the general unclamped-author-input pattern is inconsistent,
and the "weight-10 blowout" relies on an author entering an absurd value. The genuinely distinct property
is that evidence is *readiness-free* (lands at full value with no built rapport) — that is the point worth
keeping; the missing-ceiling framing is over-severitied to LOW.

## C7 — Finding 10 (dead code) is over-claimed · LOW

Grepped (the audit asserted from reading alone): `Resonance.tension` is **unit-tested** (`tests.py:50-55`)
— engine-unused, but covered, not dead. `Leverage`'s off-ground branch is engine-unreachable
(`_reception` always passes `on_ground=True`) and not referenced by keyword in the suite. So the finding
conflated "engine-unused" with "dead"; `tension` is test-only surface, a weaker Necessary concern than
"dead weight." The NERS-N "fail" leaned partly on this overstatement.

## C8 — The NERS verdict hedges, and now needs revision · MEDIUM

Four "partials" with no stated pass/fail bar per criterion reads as fence-sitting, against the
review-mode rule to commit to a verdict. And the verdict is now stale: removing finding 1 lifts a Robust
ding; re-mapping finding 4 cleans Smoothness; downgrading findings 2/3/10 softens Elegant and Necessary.
A corrected provisional verdict: **N pass-with-cleanup** (only engine-unused/covered surface remains),
**R pass-with-one-note** (uncapped evidence weight is the sole real robustness item; small-coalition
variance is intended coarseness), **S pass** (no accidental cliff survives), **E partial** (the Standing
hub and the duplicated band logic remain). The system is meaningfully *cleaner* than the audit concluded;
the audit erred toward harshness on exactly the findings it did not measure.

## C9 — Scope an independent reviewer would add · MEDIUM

- **No audit of test coverage.** The audit flagged the suite is unseeded/exits-0 but never checked whether
  the 62 tests *cover the findings* (there is, for instance, no test pinning `resist`'s behaviour — which
  is why the bug-that-wasn't went unexamined).
- **No systematic win-condition edge enumeration.** E.g. `ProofBar` lets the defender win only by timeout,
  creating a stall incentive that interacts with the silence-clinch — unexplored.
- **Top-down corpus re-validation underdone.** The ask was "all directions." The audit spot-checked fault
  severities against the nigrahasthāna but did not systematically re-validate the venue-determined thesis
  against the three-genre (who-judges / what-decided) framework that motivates the whole design.

---

## What stands

The static, architecture-level findings are mostly measurement-independent and survive: the acyclic import
graph (re-confirmed), the spec/runtime split, the uncapped *readiness-free* evidence contribution (C6
re-scopes its severity, not its existence), the §5.5/Sacred-Veto fidelity gap, the unseeded/exit-0 test
suite, the clinch/win turn-order asymmetry, the duplicated band logic, and the engine-unused surface
(`tension`, off-ground). The corpus-grounding claims remain under-evidenced either way.

## Recommendation

1. Correct finding 1 in `FULL_AUDIT.md` — downgrade to a LOW calibration note ("`resist` functions;
   confirm intended magnitude of committee-pull") with the empirical table.
2. Re-issue the NERS verdict per C8, with a stated pass/fail bar and the empirical results folded in.
3. Add the empirical stress section (the three runs above) so the audit measures, not just reasons.
4. Re-rank the remaining findings by the impact/exposure/irreversibility rubric, not defect-clarity.
5. Add a test pinning `resist` and the other behavioural findings, so the suite would catch a regression
   — and seed it.
