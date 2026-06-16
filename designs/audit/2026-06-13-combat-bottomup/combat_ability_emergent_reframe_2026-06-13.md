# Correction: traditions teach, they do not gate — the emergent reframe (PROVISIONAL)

**2026-06-13 · status: PROPOSED, Jordan-vetoable · supersedes the gate-chain framing (§3–§5) of `combat_ability_gating_chain_and_sets_2026-06-13.md`**

**The prior doc made `mode` *gate* technique access ("geometric ≠ tactile → the German is refused the atajo"). That
is a top-down conditional — a check on a descriptor — and it is the exact anti-pattern this project is built
against. Retracted. The tradition and mode names ("German", "tactile", "geometric") are *historical descriptors for
regions of the underlying primitive space*, not owners of the primitives. A tradition provides the ability to learn
what it requires; it does not gate tactile, or leverage, or anything. Reframed below so that every effect — including
incompatibility and sets — *emerges* from the primitives (developed competences + weapon physics + stats) rather
than being imposed on a label. Confirmed separately: cross-training a second tradition grants its weapons.**

`[READ: tradition.TRADITIONS channel profiles · combatant.WEAPONS physics — grepped this session]`
`[CORRECTION: prior doc §3 gate-chain / §4 hard-gate dissolution / §5 "refused" — replaced by the emergent model here]`
`[SELF-AUTHORED — bias risk: correcting my own error; owning it, not defending it]`

---

## §1 — The principle (restated, and where I broke it)

**Every mechanical effect emerges from the primitives** — your developed competences (the seven channels), your
weapon's real physical properties, your stats — through continuous functions. **Labels are descriptors of regions
in that primitive space; they organize and communicate, they never gate or trigger mechanics.** The engine sees
channels and physics, not the word "German."

Where I broke it: I let `mode` (a label) gate which techniques may be slotted. That is a conditional on a category —
top-down by construction. The fix is not a better gate; it is *no* gate. The incompatibility I was reaching for is
real, but it must **emerge**, not be declared.

A tradition, correctly, is a **learning-path**: it grants the ability to learn a coherent bundle — its techniques,
its weapon proficiencies, efficient development of certain channels. It is a curriculum over the primitive space,
not a fence around any primitive. Tactile competence is universal; the German school merely teaches a tactile-and-
leverage bind method efficiently, as a package.

---

## §2 — The four counters, re-derived emergently

**① Weapon → technique: continuous scaling, not a threshold gate.** Effectiveness *rises with* the real property —
winding with `blade_guard` (longsword 0.85, rapier 0.45, spear 0.20), breach with `percussion`/`mass`/`pob_frac`
(mace/poleaxe 8), grappling with `clinch`. These are real physical quantities, so scaling on them is bottom-up by
nature. The only **hard** gates are genuine *affordance* presence/absence — no point → cannot thrust; no blade →
cannot half-sword; no pommel → no pommel-strike. Those are not label-checks; they are the effectiveness function
reaching a true zero or an undefined motion. *(The dangling `mass`/`pob_frac` still get their consumer here.)*

**② Tradition → weapons: a learning-path, not a fence.** The tradition *teaches* weapon proficiency; proficiency is
a **developed competence** that mitigates the weapon's `hand` handling cost — not a binary label-gate. Cross-training
a second tradition grants the ability to learn its weapons (and its techniques and channel development). **Confirmed:
cross-training grants weapons.**

**③ Incompatibility: emergent from competence mismatch + the bounded budget.** The Spanish atajo runs on measure +
balance (Spanish profile: `measure 1.35, balance 1.30`). A German build (`tactile 1.35, leverage 1.30`; measure/
balance ≈ 1.0) **can slot the atajo — nothing refuses it — but it is weak in their hands**, because they have not
developed the channels it uses. To make it work they would spend the bounded competence budget *away* from the
tactile/leverage that powers their bind. So the German stays a binder by mechanics, not by fiat; the atajo is simply
a poor fit. **The `mode` field is a name for that channel-region — it gates nothing.** "What defending should do is
incompatible" is true *emergently*: the two defences live in different channel concentrations, and you cannot be
concentrated in both at once.

**④ Sets: emergent coherence, not a declared combo-check.** Techniques that share a channel **compound** — your
concentrated investment pays off across all of them, so a coherent build is naturally strong and a scattered one
naturally weak. Qualitatively-new **capstone** behaviors emerge when a profile becomes concentrated enough (a deep
tactile/leverage profile can sustain a bind-flow continuation a shallow profile cannot). A *purely declared*
set-bonus ("these three named skills equipped → bonus") would reintroduce the top-down pattern; the principled form
is shared-channel reinforcement + emergent capstones. *(If you want literal declared sets anyway, that is your design
call — flagged as the top-down shape; the emergent version achieves the same goal: combinations matter, qualitatively.)*

---

## §3 — The combinatorial concern, answered *better* by emergence

The earlier dissolution leaned on hard gates (weapon ∩ mode ∩ unlocked). Replace it:

> The player is **free to slot anything** — no gates. But the **bounded competence budget** means you cannot be good
> at everything. Coherent builds (techniques sharing channels) draw full value from concentrated investment →
> emergently strong. Scattered or cross-doctrine builds split the budget across channels they cannot all raise →
> emergently weak. **Incoherence self-punishes; coherence self-rewards.**

Balance emerges from the competence economy, not from imposed rules. This is *stronger* than the gate model: maximal
freedom **and** an emergent pressure toward coherence, with no unstated exceptions and no cliffs (the things the
resolution discipline flags). Degenerate free-mixing does not need to be forbidden — it is simply weak.

---

## §4 — Worked example, re-done

**German KdF build** (tactile/leverage concentration; proficient via the school, plus rapier from cross-training
Spanish).
- Slots **Winden** (longsword `blade_guard` 0.85 → strong) — full value from high tactile/leverage.
- *May* slot the **Spanish atajo-defence** — **permitted, not refused** — but it runs on measure/balance they have
  at ≈1.0, so it is weak in their hands. Raising measure/balance to power it would drain the budget that makes the
  bind dominant. The mechanics, not a rule, keep them a binder.
- Cross-training Spanish granted the rapier and the *ability to learn* destreza — but the bounded budget still forces
  the choice of what to be good at. Freedom to learn; emergence decides effectiveness.

No refusal anywhere. Identity holds because competence is real and concentrated, and off-profile techniques are
weak — emergently.

---

## §5 — What this changes / decisions

- **Supersedes** the prior doc's §3 gate-chain, §4 hard-gate dissolution, and §5 "refused" block. The rest of that
  doc (the three-relations disentangling — `set`/`mode`/adjacency as *descriptors*; the convergences;
  the authoring-burden bill) stands, now read as *descriptive structure feeding emergent functions*, not gates.
- **Decisions:** (a) **declared vs emergent sets** — recommend emergent (declared = top-down); your call. (b) the
  **effectiveness-function shapes** — how steeply a technique scales with its channels/properties (the sim-tunable
  that sets how sharply coherence is rewarded and incompatibility punished). (c) the genuine **hard affordance gates**
  — confirm the short list (point→thrust, blade→half-sword, pommel→pommel-strike) and that everything else is
  continuous. (d) the sim plan: free-build win-rates — verify coherent builds land strong and scattered builds land
  weak *without* any gate, and that no single coherent profile dominates (±2–3 pp across profiles at N≈3000).
- **Mechanical, not creative**; historical names stay anchored, mechanical fill graded `M`. The tradition/mode names
  remain *historical descriptors*, exactly as you said — used to communicate regions of the primitive space, never to
  gate it.

`[CONFIDENCE: high]` that emergent-not-gated is correct and that it answers the combinatorial concern better.
`[GAP: unvalidated]` — the effectiveness-function shapes and the emergent coherence/incompatibility need the sim test
before any of this is canon.

Provisional; engine unchanged. The model is now: **universal channel + physics primitives; traditions as
learning-paths that teach coherent bundles; effectiveness, incompatibility, and coherence all emergent from the
primitives and a bounded competence budget — no label gates.**
