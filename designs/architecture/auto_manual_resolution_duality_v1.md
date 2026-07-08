# Auto / Manual Resolution Duality (v1)

## Status: PROPOSED — drafted 2026-07-08 at Jordan's request; Jordan-vetoable throughout. Per ED-1094, review-and-merge of the PR that lands this ratifies the DOCTRINE by default; the open forks in §6 stay `needs_jordan` and are not ratified by that merge.
## ED: ED-SC-0013
## Origin: Jordan's Total-War framing, 2026-07-08 — "the extent to which faction parliament actions are the auto-resolve version of playing them out as a scene, in parallel to Total War where you can play the battle or auto it."

---

## 1. The principle

Every contested event in Valoria has two resolution **fidelities** of the *same* underlying conflict:

- **Auto-resolve** — the engine computes an outcome algorithmically on aggregate state, in one step.
- **Play it out** — the engine resolves the same conflict as a full personal-scale **scene**.

The scale-transition **zoom in / out** protocol (`scale_transitions_v30 §4`) **is** the toggle between them: **zoom out = auto-resolve; zoom in = play it out.** This is the Total War auto-resolve / fight-the-battle duality, and it is architecturally load-bearing — the two contest engines Valoria already carries are **not redundant**; they are one conflict at two fidelities.

## 2. The two fidelities (reference instance: the Parliamentary vote)

| | Auto-resolve | Play it out |
|---|---|---|
| **Engine** | `run_parliamentary_vote` — faction-scale §10 Mandate-pool roll on aggregate state (`sim/cross_scale/parliamentary_bridge.py`) | the personal social-contest kernel — argue-pool exchanges, genre/stasis/rhetoric, a *named* orator (`sim/personal/contest/`) |
| **Inputs** | aggregate faction stats (`L/Sta/W/I/Mil`) | concrete actors (attributes, History, Convictions, Beliefs) |
| **Cost** | one roll | a played scene |
| **Toggle** | stay zoomed out | `zoom_in` |

The Parliamentary vote wired in ED-SC-0006/0007 (now `ECHO_TRANSPORT` default ON) is Valoria's **first auto-resolver**. Its played-out counterpart is the promoted contest kernel — today reachable only in tests, because the personal party-derivation is unbuilt (ED-SC-0011).

## 3. The calibration constraint (the load-bearing part)

The auto-resolver and the played scene **must be distributionally consistent on matched inputs**:

> **E[ auto outcome | inputs ] ≈ E[ played outcome | inputs ].**

**Rationale — this is exploit-prevention, not aesthetics.** The auto-resolver emits *canonical* consequences (Mandate penalties, Domain Echoes) into the strategic layer. If the two modes diverge in expectation, whoever chooses the mode is **mode-shopping** for the better outcome — the political equivalent of save-scumming a battle. Consistency is what makes the choice of fidelity *free of strategic advantage*, leaving it a choice of **richness/agency** only. That is the property that lets both modes coexist.

**Acceptance oracle.** A **parity harness** comparing `parliamentary_bridge` (auto) against the personal kernel (played) on matched inputs, asserting the win / lose / compromise distributions agree within a stated tolerance. This is a new consistency gate — and it is the acceptance criterion for ED-SC-0011 (§5).

**Corollary.** The endgame is plausibly **one engine run at two fidelities**, not two independent mechanics. The kernel's own `faction.py` adapter (`coalition_vote` / `succession` — the §5 Parliamentary action modelled *on* the contest engine) is evidence the reduction is achievable. Whether to unify onto one engine or hold two engines consistent via the harness is an open fork (§6, FORK-A).

## 4. Escalation policy: default-auto, opt-in-play

- **Default is auto.** The engine auto-resolves every season's vote (`ECHO_TRANSPORT` ON). This matches the no-GM model (the engine resolves everything) and Total War (most battles auto-resolved).
- **A conflict escalates to a played scene when the stakes justify the fidelity** — e.g. the focal party is player-controlled, a Total Victory is reachable, or a Belief/Conviction is on the line. The existing mandatory scene triggers (`scale_transitions_v30 §4.3.2`) are the home for this escalation gate.
- **Who chooses to zoom** is, today, **engine policy** — there is no RTS-style player layer yet, so the escalation trigger is an engine rule. It becomes a player-facing control if/when a player layer lands (§6, FORK-D).

## 5. ED-SC-0011, reframed

ED-SC-0011 (contest live-dispatch — route `scene_dispatch` to the promoted kernel) is reframed as **the zoom-in expansion**: instantiate a concrete played contest (named orators with attributes / History / Convictions derived from aggregate faction state) that is **calibrated to the auto-resolver per §3**. Its acceptance gate is the parity harness. This converts the previously-"undefined party-derivation" into a **well-posed** problem: the derivation must produce actors whose *played* contest matches the *auto-resolved* vote distributionally. (It removes the reason the personal bridge was blocked — there was no target for the derivation to hit; now there is.)

## 6. Open forks (need Jordan — not ratified by merging this note)

- **FORK-A — one engine or two.** Unify the parliamentary auto-resolver onto the personal σ-kernel (run the kernel at faction fidelity), or keep two engines held consistent by the parity harness? *No default.*
- **FORK-B — the escalation predicate.** Exactly which conditions escalate a vote to a played scene? `§4.3.2` is the home; the specific stakes predicate is undecided.
- **FORK-C — calibration tolerance.** What distributional tolerance counts as "consistent," and on which outcome axis (pass/fail/committee share, Total-Victory rate, echo magnitude)?
- **FORK-D — the player layer.** When a player layer exists, is zoom-in a player *choice* (Total War) or an engine-forced *escalation* (narrative necessity), or both?

## 7. What this note does NOT do

It does not implement the parity harness, unify the engines, change the auto-resolver, or build the personal derivation. It states the duality as the design spine and reframes the ED-SC-0011 charter (§5).

The provisional parliamentary derivation shipped ON by default (proposer = lowest-Stability, establishment = highest-Mandate, others abstain) remains **retunable and is not ratified as canon** by this note.
