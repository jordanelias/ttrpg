# Tradition gate — vacuum-balance, alternatives, adversarial review, reconciliation (PROVISIONAL)

**2026-06-13 · status: PROPOSED, Jordan-vetoable · companion to `combat_tradition_state_graph_gates_2026-06-13.md`**

**Verdict first: the imposition-gate idea is sound, but the sketched mechanism (symmetric style-clash)
*fails* the "each tradition equally good in a vacuum" constraint — measured, an 18.8 pp spread in
imposition-rate — and the cause is a channel-weight double-count. The repair is to decouple the
impose-rate from the raw channel weight and let differentiation live in *which* node (qualitative) plus a
cyclic/contextual matchup relation, with the in-node edge paid for. Whether the repaired gate beats simply
tuning the flat weights is a sim + legibility question, not settled here.**

`[SELF-AUTHORED — bias risk]` Reviews a Claude-authored proposal. The adversarial section (§2) is written to
attack it, not defend it; the recommendation (§4) concedes every objection that lands.
`[READ: tradition_gate.py — the sketched contest, measured below]`
`[READ: designs/audit/2026-05-29-combat-armature/martial_traditions_synthesis.md — C1 "no tradition globally best"; the cyclic/familiarity principles]`
`[READ: designs/audit/2026-05-28-combat-reframe/historical-precedents/manual-vs-combat-v32-bridge.md — Stance Counter "Hodge ~85% cyclic", kept authored]`

---

## §0 — The constraint and the measured failure

**The constraint.** "Each tradition should be as good as another in a vacuum" is the ratified **C1** ("no
tradition globally best") turned into a *design requirement* on the gate. Context — matchup, weapon,
duel-vs-battlefield — must still flip who is better (that is the whole point of C1); only the *unconditional*
average, over all opponents and contexts, must be flat.

**The failure (measured on the sketch).** Across the seven real traditions, average imposition-rate over a
uniform field of opponents:

| tradition | avg impose | net edge | defining-channel weight |
|---|---|---|---|
| japanese | 0.575 | +0.149 | 1.35 (precommit) |
| german | 0.574 | +0.148 | 1.35 (tactile) |
| spanish | 0.572 | +0.144 | 1.35 (measure) |
| italian | 0.526 | +0.053 | 1.30 (tempo) |
| filipino | 0.480 | −0.040 | 1.25 (tactile) |
| chinese | 0.387 | −0.227 | 1.15 (leverage) |
| english | 0.386 | −0.228 | 1.15 (tempo) |

**Spread = 18.8 pp** (japanese 0.575 vs english 0.386). The ranking tracks the defining-channel weight
almost exactly (1.35 → ~0.57, 1.15 → ~0.39). That is not vacuum-balance — a japanese fighter imposes its
fight ~15 pp more than the field average, an english fighter ~23 pp less, *before* the in-node edge
compounds.

**The cause — a double-count.** In the sketch the defining-channel weight is the **impose-contest input**.
In the full design that same weight is also the **in-node competence**. So a tradition with a bigger channel
number wins *twice*: it imposes its node more readily, and then fights better once there. The channel
magnitudes were authored as σ-multipliers (a quantitative dial); reusing them as the imposition driver
silently converts a dial into a global ranking. **Any methodology that feeds the raw channel weight into
both the gate and the node inherits this flaw.**

---

## §1 — Alternative methodologies

Five ways to drive the imposition, assessed on vacuum-balance · loop-safety · corpus-fidelity · elegance ·
implementability.

- **M1 — symmetric style-clash (the sketch).** Both pull via their defining channel; higher pull imposes.
  *Vacuum-balance: FAILS (measured).* Simple, intuitive. The double-count is the flaw.
- **M2 — cyclic / rock-paper-scissors imposition.** The preferred nodes form a cycle (e.g. bind ⟶ counter ⟶
  measure-hold ⟶ bind); imposition success depends on the *cyclic relationship* of the matchup, not channel
  size. *Vacuum-balance: holds by construction* (each tradition wins ~⅓, loses ~⅓, neutral ~⅓). **Directly
  precedented** — the Stance Counter is "Hodge ~85% cyclic" and was kept *authored* precisely because it
  resists derivation (bridge §7.1). Risk: a clean 3-cycle is a *construction* the richer corpus matchup web
  does not cleanly support, and pure RPS can feel arbitrary/gamey.
- **M3 — node-cost.** Imposing your node *costs* a resource (exposure / tempo / stamina) drawn from the
  engine's existing over-commit + pool economy. The advantage of fighting your fight is *paid for*, so the
  unconditional average self-balances (cost ≈ edge). Most *physically grounded* (it rides the
  already-present Silver-true-times exposure and the stamina/conc pools) and self-correcting (a too-strong
  imposition costs too much). Risk: cost ≈ edge is an *empirical* balance, sim-validated not guaranteed; it
  couples to the partly-top-down config coefficients.
- **M4 — familiarity-driven.** The impose edge comes from *knowledge-of-others* — you impose on a style you
  read, you fail on one that reads you (the corpus's "deep hook"; novelty self-damps, a bounded loop).
  *Vacuum-balance: holds* if the familiarity web is balanced. **But** the current `ADJACENT` set is
  *symmetric* (frozenset pairs), so in a pairwise contest familiarity cancels (both read each other equally)
  and yields no edge — M4 needs **directional** familiarity (A reads B better than B reads A) to produce one.
  That is a larger change to the familiarity system.
- **M5 — normalized impose × in-node-edge (explicit budget).** Give every tradition an equal *total*
  effectiveness budget by construction: a tradition that imposes more readily gets a correspondingly smaller
  in-node edge, so `impose-rate × in-node-edge = constant`. *Vacuum-balance: enforced by tuning.* Least
  elegant (hand-balanced), but the *discipline* sits on top of any mechanism and is the operational form of
  the constraint.

---

## §2 — Adversarial review (objective standpoint)

Attacking the gate, not defending it.

1. **Positive feedback / snowball.** Impose → better terms → impose again. The measured 18.8 pp impose-spread
   is *before* the in-node edge compounds; the realised win-rate spread could be worse. The damper (opposed,
   per-transition, probabilistic, counter-imposable) is necessary but its *adequacy* is unproven here.
2. **The double-count (measured).** §0's flaw is real and it is the dominant imbalance source; it indicts M1
   and any weight-reusing variant.
3. **NERS-E — over-engineering.** Is the gate worth it versus just tuning the flat weights? The honest test:
   the flat weights *cannot express the traditions qualitatively* (a 1.35 vs 1.30 multiplier is not "drags
   you into the bind"), which is the entire reason traditions exist — but if the gate cannot be made *both*
   vacuum-balanced *and* legible, the simpler flat tuning wins. The burden of proof is on the gate.
4. **State-graph entanglement.** The engine's transitions already consume the channel weights through σ
   (`bind_sigma`, `reach_sigma`, …). A gate that *also* consumes them risks compounding or conflicting with
   those σ-paths — double-dipping the very quantities it routes on. The gate must not re-spend σ the weights
   already feed.
5. **Player legibility.** If the imposition is an invisible probability shift, the qualitative benefit is
   lost and the gate is "flat tuning with extra steps." The imposed node must be *visible and playable*, or
   the apparatus is not earning its cost (objection 3 bites).
6. **Node-map fidelity.** japanese → counter (via precommit) and chinese → burst (via leverage) are partly
   *my* reading of the corpus. Forcing eight traditions into a small node taxonomy may distort what the
   manuals actually claim.
7. **Realism / agency.** Forcing a bind on an unwilling Italian — whose entire game is to *not be there* —
   is both historically off (the Italian voids/retreats) and potentially un-fun (the player loses agency).
   "Sets terms, not outcome" mitigates but does not resolve it.
8. **No alternative is free.** M2's clean cycle is a construction the richer web resists; M3's cost ≈ edge is
   an empirical hope; M4 needs directional familiarity; M5 is hand-tuning. Each buys vacuum-balance with a
   different cost.

---

## §3 — Reconciliation (cautious)

What survives the review:

- **Decouple the impose-rate from the raw channel weight** — this is non-negotiable; it is the measured
  flaw. Two clean routes: **(a)** normalise the impose-contest to an equal base rate (the weight no longer
  drives imposition; differentiation moves to node + matchup), or **(b)** let each channel weight drive
  *either* impose *or* in-node, never both.
- **Differentiate by node identity + a cyclic matchup relation, not by magnitude.** This is vacuum-balanced
  by construction (M2) and has direct precedent (the authored, Hodge-cyclic Stance Counter). It keeps the
  traditions *qualitatively* distinct — which is the point — without ranking them globally.
- **Pay for the in-node edge (M3).** A small node-cost from the existing exposure/stamina economy makes
  fighting-your-fight a *purchase*, self-balancing the edge and — crucially — giving the unwilling defender a
  principled **void/exit** (pay to refuse the imposition). This directly answers objection 7: the imposition
  is a *contest the defender can win at a cost*, not a lock.

Conceded, plainly:

- Vacuum-balance **cannot be proven analytically** for a gate riding the entangled state graph (objection 4);
  it must be **measured** and tuned to flat.
- The damper's adequacy against snowball (objection 1) is likewise a **sim** question.
- **Legibility is a requirement, not a nicety** (objection 5): the imposed node must surface to the player.
- I am **not** claiming a balanced gate exists and beats flat tuning. I am claiming: (i) the sketch fails
  vacuum-balance (measured); (ii) the cause is the double-count; (iii) decoupling + cyclic + node-cost is the
  principled repair; (iv) whether it is worth it is decided by the sim balance test and the legibility check.

---

## §4 — Consolidation (the recommendation)

**Recommended: a balanced-base-rate imposition gate.**

1. **Normalised impose-contest** — every tradition imposes at the same base rate in a vacuum (kills the
   18.8 pp spread). The contest still draws on `reading` (skill) and `familiarity` (knowledge), just **not**
   the raw defining-channel magnitude as a free edge.
2. **Differentiation = node + cycle** — *which* node a tradition imposes (the corpus's qualitative
   preferred-fight) plus a **cyclic relation** among the nodes (the bind ⟶ counter ⟶ measure-hold ⟶ bind
   family), balanced by construction, precedented by the Stance Counter.
3. **Node-cost** — imposing spends a little exposure/tempo/stamina from the existing economy; the defender
   may pay to **void/exit**. Self-balancing, and it makes the imposition a fair contest rather than a lock.
4. **Legibility** — the imposed node is visible to the player ("you've been drawn into the bind").
5. **Channel weights** keep their **in-node** role (the competence once you are there) — or fold into node
   identity — but do **not** also drive the impose-rate.

**Validation (the gate's gate).** Extend the weapon-physics harness to tradition matchups: measure each
tradition's **unconditional win-rate** across all opponents and contexts; **require flat within tolerance**
(≈ the parity-baseline noise floor, ±2–3 pp at N≈3000). Tune the cyclic relation + node-cost until flat.
Context *should* still flip the *conditional* advantage (C1) — only the unconditional mean must be level.

**Open decisions (Jordan):**
- **(a)** Adopt the gate at all, or accept flat σ-tuning (the NERS-E call — objection 3).
- **(b)** The cyclic node relation — does bind ⟶ counter ⟶ measure-hold ⟶ bind hold, or a richer/different
  structure? (This is design content, partly yours — objection 6.)
- **(c)** How hard a tradition may impose, and the node-cost magnitude (matchup-balance, sim-tuned).
- **(d)** Whether to extend `familiarity` to *directional* (unlocks the novelty self-damping hook, M4).

---

## §5 — Status / honesty

- `[CONFIDENCE: high]` on the measured failure and its cause (the double-count; the spread tracks the
  channel weight). `[CONFIDENCE: medium]` on the recommendation — the decouple + cyclic + node-cost repair is
  principled but **unvalidated**; vacuum-balance is a sim claim, not a proof.
- `[GAP: full-fight win-rates unmeasured]` The gate is not wired; no unconditional win-rate has been
  measured. The §4 validation is the build step.
- The tradition **content** (preferred fights) is the corpus's; the **mechanism**, the cyclic relation, and
  the node-cost are mechanical-tier proposals; **how hard to impose** is your matchup-balance call.
- Provisional. Commit alongside the stress-test results. Canon engine unchanged.
