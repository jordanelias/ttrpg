# Combat — Co-Primordial Throughlines & the Commitment=Recovery Axis

**Status:** Design-spine doc (mechanical-tier). The "why" beneath the engine — the throughlines and the two
poles every exchange converges on. Grounds the commitment-recovery model (`systems.recoverability_factor`).

## The two poles

A scene-combat exchange is a negotiation that converges on a single polarity: **hit your opponent vs. be hit
by your opponent.** In the engine this is literal: every throughline contributes a term to **`net_sigma`** (the
summed negotiation), which resolves through the continuous engine into a **`degree`** (fail / partial / success
/ overwhelming) — and the defender's mode decides whether that degree becomes a hit *on them* or a riposte *back*.
`net_sigma → degree → hit/be-hit` IS the convergence on the two poles.

## The co-primordial throughlines (and where each lives)

None of these is prior to the others — they are co-primordial, each defined *relative to the pairing* (the
corpus's throughline T5: measure/initiative/stance are properties of the pair, not the fighter):

| throughline | engine locus |
|---|---|
| **distance / measure** | `measure_gap`, the approach/close/reopen loop, `reach_sigma` |
| **reach** | `reach_base` (continuous, blade-length-grounded), the stop-hit, the reach↔armour rotation |
| **reading the opponent** | the read contest (`read_d` vs `read_a`), `legibility`, `familiarity`, `precommit` |
| **timing / tempo** | `weapon_tempo`/`close_tempo`, the ACT_THRESHOLD gate, the Vor/initiative substrate |
| **balance / structure** | `balance_eff`, `poise` (kuzushi), `stance_stability`, `anti_overcommit` |
| **technique** | history/skill, the defence modes (parry/dodge/wind), the bind, the counter |
| **weapon** | the continuous morphology (mass, pob, length, guards), `coupling`, the affordance gates |
| **commitment / recovery** | commit-depth × `recoverability_factor` → overcommit exposure (see below) |

A tradition is a *methodology* over these throughlines (which it fights to impose — `tradition_decomposition_v1`);
a weapon's morphology weights them (a long point owns measure; a forward-heavy head owns percussion but loses
recovery); stance and footwork set the moment-to-moment terms.

## Commitment = recovery (the master coupling)

The load-bearing reframe: **to commit to an action — offensive OR defensive — is, at the same instant, to give
up the ability to recover from it.** Commitment and recoverability are one axis seen from its two ends. So:

- **A feint is not a separate maneuver.** It is the *minimal-commitment / full-recovery* pole of that axis. In
  the engine `commit 2` already is the feint: minimal commitment, zero overcommit-exposure = full recovery. This
  is why feinting was dissolved into the attack (WS-5) — there was never a separate thing to model.
- **The cost of committing deep is irrecoverability**, and it is *physical*, derived (`recoverability_factor`)
  from the four factors:
  1. **footwork** — a lunge extends the body (low recovery); a grounded rotation stays recoverable. *(grip term —
     live once the Stance/grip writer lands.)*
  2. **point-of-balance × weight/heft** — the static turning moment `mass × pob_frac`: a forward-heavy mace
     (1.74×) "wants to continue" and can't be stopped; a hand-balanced rapier (0.95×) retracts instantly — *which
     is why a rapier can feint and a mace can't.* *(live now, off the WS-2 continuous morphology.)*
  3. **stance** — overhead-to-strike is pre-committed; guard-in-front keeps options open. *(grip term.)*
  4. **one/two-handed + extension** — an extended body is a committed body. *(grip term.)*

  `overcommit_exposure = max(0, COMMIT_EXPOSE_K·(commit−3) · recoverability_factor) − discipline`. A deep commit
  with an unrecoverable weapon is heavily exposed; a shallow one with a hand-balanced blade keeps the recovery
  budget — the feint. Measured effect: poleaxe/mace lose ~5pp in the duel (a committed blow they cannot recall),
  light blades unchanged.

## Why this matters for the rest of the plan

The throughline view is the test for any new lever: does it move a *real* axis, or duplicate one? It is also the
balancing frame (WS-8): you do not flatten the throughlines, you let each weapon/tradition own a different
convergence toward the two poles, and balance the *unconditional* mean (C1). Commitment=recovery, now physical,
is one throughline made honest; the same treatment is owed to the others as the engine deepens.
