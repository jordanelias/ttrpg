# Ground-Up Contest — Stress Test (corrected system)

`[SELF-AUTHORED — bias risk]` Stress of the just-ratified corrected system. Verdict first; confirmations, then the failure surface.

## Verdict
The audit's P1 fix **holds under stress** and the resolver is now fair and skill-determinative. The stress surfaced one significant balance/design finding (appeals don't yet pay) and two depth/draw balance knobs — all `[SEED]`/design, none structural regressions.

## Confirmed sound
- **Turn-order fix holds at every scale.** honest vs honest, T=4: faculty 1v1 0.43/0.43, 2v2 0.47/0.48, 4v4 0.43/0.42, 7v7 0.26/0.27 — symmetric throughout (the 87/13 bias is gone everywhere, not just at 4v4).
- **Skill now reads cleanly** (turn order no longer confounds it): 4v4 0.43/0.42 → 5v3 0.60/0.27 → 6v2 0.90/0.07 → 7v1 0.98/0.02. Faculty determines the outcome, monotonically.
- **Defeat-conditions sound.** honest beats overreacher 1.00 (barred), staller 1.00 (silence), off-ground 0.96; honest vs honest **never clinches** (0%). (Off-ground wins 3.6% because it argues on-ground on even beats — a gamble, not an auto-loss; correct.)
- **No snowball.** A standing head start of 9 v 5 leaves the result at 0.43 vs the 0.43 baseline — the standing loop stays bounded.
- **Appeal routing works.** pure-ethos vs honest: honest 0.997 — ethos cannot win the verdict, because only logos advances merits.

## Failure surface (balance/design — for the pending pass)
- **F1 (significant): build-then-close is strictly dominated by logos-spam.** The tactician (ethos/pathos early, logos to close) beats honest (logos every turn) **0.000 of the time at every depth tested** (T=4 honest 0.999; T=8 honest 0.87; T=12+ all draws). The standing/room a tactician builds buys a small reception edge that never repays the merits it forgoes while building. **Appeals are functional but do not yet create the intended build-then-close depth — a player should just spam logos.** This is not a number tweak alone: making building pay needs a design choice — couple logos's merit-gain to built standing/room (so unsupported logos is weak), or add a readiness gate so raw logos hits a wall. That shape is Jordan's call.
- **F2 (balance): high-faculty contests draw ~half the time** (7v7 → 0.47 draws at T=4): two reliable strong sides cross threshold the same exchange. The clock depth needs to scale with pool, or T rises for strong matchups.
- **F3 (balance): the playable threshold window is ~T 4–8** (draws 14–20%); T=10 → 56% draws, T=14 → all draws. Sets the balance-pass range; the reception-variance band remains a Jordan feel call.

## Bottom line
The corrected resolver is fair, skill-determinative, and clinch-sound — the ratified claims hold under stress. The open work is the balance/design pass, and its first task is **F1**: appeals are wired but not yet worth using. That is the thing to fix before the contest's central tactical axis means anything.
