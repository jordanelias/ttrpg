# R8 — Trustworthy Equal-Value Verdict (armature reset, Build-8)

**Date:** 2026-05-29 · **Module:** `tests/sim/v32-combat-balance/r8_parity_harness.py` (defect-immune; budgets asserted) · **Status:** Class-C proposal result; no canon file edited. **Supersedes all prior session field-rates (R3/R4/R6/R7), which were harness-corrupted.**

`[SELF-AUTHORED — bias risk: I authored R1–R8 and the corrupted harness whose verdict this replaces. This is the corrected, defect-immune measurement.]`

## The rebuild (why this verdict is trustworthy)

R6/R7's verdicts were corrupted by (1) stdout-buffer interleaving and (2) an intermittent build-budget failure (Str built at budget 13). R8 is defect-immune:
- Self-contained on the **validated unit modules only** (R1/R2/R5 + M1/M5/M7); does not import R6/R7's suspect build/driver code.
- Builds **hardcoded and asserted to budget 18** at construction AND before every matchup (hard-fail otherwise).
- All results written to **JSON, read from file** — never piped stdout.
- Builds deep-copied into every call; the build dicts are read-only.

Run confirms budgets `{Agi:18, Str:18, End:18, Reading:18, Spirit:18}`.

## The verdict (each archetype plays its own best loadout, asymmetric, N=3000, Wilson CI)

| Build | Best loadout | Field rate | |
|---|---|---|---|
| **Str** | war hammer + heavy | **85.3%** CI[84.7,86.0] | **DOMINANT** |
| Agi | war hammer + heavy | 58.1% CI[57.2,59.0] | ok |
| End | longsword + heavy | 42.8% CI[41.9,43.7] | ok |
| Reading | longsword + none | 48.8% CI[47.8,49.7] | ok |
| **Spirit** | longsword + heavy | **12.3%** CI[11.7,12.9] | **DEAD** |

(After one Class-C tuning pass: Str channels reduced, Reading raised. Pre-tuning Str was 90%, Reading 20%, Spirit 26%.)

## What this means — the INVERSE of the corrupted picture

1. **Strength is strong, not dead.** The whole-session "Str dead" finding was the harness artifact. With R5's channels measured correctly, Str is the *strongest* archetype — **over-tuned at 85%.** Even the Agi build chooses the war hammer (Str's signature weapon), and Reading (Str 2, can't wield heavy) is stuck light. Decision-1 (give Str leverage) was correct design; it over-delivered.

2. **Agi / End / Reading cluster acceptably** (58 / 43 / 49) — within or near the 40–60% band. The Stamina split (decision-2) successfully tamed End (now 43%, no longer dominant). Reading reached parity after tuning. These three are close to equal-value.

3. **Spirit is the genuinely dead stat (12%).** Its only combat channel is stamina reserves, which rarely decide a short decisive phrase — so a Spirit-heavy build is ≈ a neutral build and loses to everyone's specialised edge.

## Two localized findings — both yours (project-owner contract)

The mechanism is right; what remains is calibration + one design gap, neither of which I should settle unilaterally:

1. **Str channel magnitudes are over-weighted (Class-C calibration).** Str's channels *stack* (bind + armour-defeat + stagger + heavy-weapon access + pressure). Tuning them down toward equal value is straightforward against this harness, but **how much cross-attribute value Str's control should carry is your calibration call.** The harness is now the reliable oracle: lower the seeds, re-run, watch the field rate.

2. **Spirit needs a SECOND combat channel (design decision).** Stamina-reserves alone is too thin to make Spirit competitive in a decisive duel. Equalising Spirit is **not** a seed-tuning task — it needs another role (candidates, your call: Spirit → Composure/will under pressure resisting stagger/fear; Spirit → a "second wind" that refreshes on a threshold; Spirit → resisting the Out-of-Breath penalty rather than just raising the reserve). Each is a new mechanic (N/Ω/Μ vetting).

## Honesty flags

- `[CONFIDENCE: high — budgets asserted ==18, results file-read (artifact-immune), CIs tight at N=3000. This supersedes every prior session field-rate.]`
- `[CORRECTION: the session-long "Strength is structurally dead" finding (R4/R6/R7) was a harness artifact (buffer interleaving + budget-13 Str builds). Corrected: Str is over-strong (85%); the real dead stat is Spirit (12%).]`
- `[ASSUMPTION: equal-value scoped to the six combat-active attributes; one-step best-response loadout (not full equilibrium); decisive one-phrase model.]`
- The harness is **locked at a sensible mid-point**, not hand-converged to a fake "all 50%." I stopped tuning rather than chase stochastic noise across five interacting knobs; the residual (Str high, Spirit low) is the real, localized work.

## Next

- **Str:** dial the Class-C channel magnitudes down (your calibration), re-run R8 — converges quickly now that the oracle is reliable.
- **Spirit:** pick a second Spirit combat channel (design), wire it into R5/R8, re-run.
- Then the six-attribute parity should land in-band and the omega Class-A vetting block can honestly assess Ω-d.
