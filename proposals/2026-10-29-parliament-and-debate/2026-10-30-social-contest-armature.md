# Social contest: the armature, and one scale for its influences

## Status: PROPOSED (reference; resolves nothing)

Producer's draft for one adversarial pass. Reads, in order: `2026-10-30-social-contest-primitives-and-kinds.md`
(**PK**; its `R-1..R-41` and `S-1..S-8` are cited by number and outrank everything here),
`...-reconciliation-and-distillation.md` (**RD**), `...-code-audit.md` (**CA**), `...-how-contests-occur.md` (**HO**),
`...-unification-plan.md` (**UP**), and the code and research cited at their lines. Every engine figure below was
computed by me with `engine/dice_engine/sigma_leverage.py::p_success` at this checkout. Canadian spelling.

---

## A. The armature on one page

**A contest is a venue row, a matter, and a sequence of acts. Each act is one draw. Draws move persons; persons
decide by their own act; the row says whose decision counts and who learns it.** Nothing else is structure.

1. **The row** (`engine/season/arrangements.yaml`, one per institution; R-12, R-15) names the **authority** the
   venue's force comes from (the parties, the polity, the church; R-34), the **decider** (`disposal`: the target, the
   parties, a bench of that authority's office-holders, or a count), the **action surface** it admits out of the one
   verb table and one speech-kind roster (R-33), the **weights** it gives offices and titles (R-31, R-38), its
   **reach**, and its **appeal route** to another authority (R-35). A kind of contest is a row; no row is a branch.

2. **The draw** is the one σ-leveraged continuous roll (R-5, R-6, R-22, R-32). Every influence enters exactly once,
   through one of three channels, chosen by **whose fact it is**:
   - **dice** (`pool`): what the actor holds (capability with presence, title, office weight in this venue scaled by
     the authority's local legitimacy, faction backing where the row keys it, evidence held, latitude);
   - **obstacle** (`Ob`): what the other side holds, as **its score ÷ 2** (R-5), plus terms belonging to the act or
     the document rather than to any person (aptness, R-16; forgery quality; the default where nobody resists);
   - **leverage** (σ, a μ-shift on the roll, soft-capped at ±1.5σ): what holds **between** actor and decider at this
     instant (reception, a fear pressed, circumstantial leverage, coherence with what the hearer already believes).

   The common scale is **the expected margin in net successes**, the unit `degree_from_net` grades:
   `E[m] = 0.4·N + 0.8·√N·softcap(s) − Ob`, spread `0.8·√N`. One obstacle point is one net success and is worth
   2.5 dice of mean at every pool; one σ is worth `0.8·√N` obstacle points (1.79 at 5D). At the reference pool
   (5D, R-40) one die ≈ 0.22σ, one Ob point ≈ 0.56σ.

3. **The decider** acts by its own verb: the target's belief moves (dyadic); each party `commit`s or there is an
   impasse (mutual; R-1); a seat-holder of the row's authority `determine`s, as a draw of its own (bench); members'
   `commit` edges are counted against a threshold and license or block the owner's own act (count; R-29). Advocates
   never write into a decider (R-19, R-23); they move the decider's claims and stances, which reach the decider's own
   act through the leverage channel.

4. **The world learns it** (R-21, S-3, S-6, S-7): the disposal is a Tenure edge, a Record or a licence; it is
   witnessed and spreads at the speed of news; Partial leaves a matter on the docket (R-17). The outcome rides; there
   is no retry before the same bench, and an appeal is a petition carried to the authority the row names (R-2, R-35).

**What cannot go on the scale** (§D.2): truth itself (it reaches the draw only as claims someone holds), the
authority's *availability* and the enforcement behind a disposal (gates and later acts, not dice), the admission of
an act (a gate), a lie discovered (a Record and a standing cost, not a modifier), and every effect whose size the
evidence does not support (a bounded sweep parameter, never a set magnitude).

**What executes today:** one integer roll at 2D against Ob 2 for nearly everyone, with leverage hard-coded 0 (CA §1).
The armature above is about one-fifth code (§F).
