# Unification — What the Whole Docket Says (v1)

## Status: FILED — 2026-07-14 · ED-IN-0064 · the capstone across the entire PR (#138)

> One synthesis of the whole observatory docket — the per-subsystem map, the six-directional coverage, the three-axis
> value architecture, and the gap register — reconciled into a single picture, a single action surface, and an honest
> statement of what we know versus what is a lead. **Analytic instrument (Class A, self-exempting); leads, not
> verdicts** (the L0 validation gate FAILED 1/3); **every proposed fix HELD-BACK (ED-1094).** Where any sibling doc
> conflicts with this file on a *classification*, the gap register + `adversarial_review_v1.md` govern; this file is
> the through-line, not a new ruling.

---

## §0 · The one thesis

Every cut in this docket converges on a single claim:

> **Valoria's Key substrate is topology-neutral and sound — so the "missing" architecture is overwhelmingly
> *unbuilt wiring on already-determined logic* (complete-the-chain), not missing mechanisms. The genuine-mechanism
> surface is small and specific. That design choice concentrates *all* correctness into three loci: authoring
> discipline, two integration hubs, and one value-transformation primitive.**

The substrate delivers cross-scale in every direction through one update rule, with direction an *emergent* property
of a Key's `targets[]`/`scale_signature`/`causes[]` — no per-direction channel, no private channels. That elegance is
the finding's root cause: because there is no channel to be "missing," correctness cannot hide in apparatus — it lives
entirely in whether the addressing fields are authored, whether the hubs' resolvers are grounded, and whether the
value-transformation math is unified. The observatory's ~40 findings are almost all symptoms of those three.

---

## §1 · The four cuts are four lenses on one object

The docket looks at the same thing — the Key substrate + the 27 `module_contracts.yaml` modules + the `sim/`
reference — four ways, and they agree:

| Cut | Deliverable | What it sees | The shared conclusion it reaches |
|---|---|---|---|
| **Per-subsystem** | `subsystem_synthesis` + `subsystem_discussion` | 16 gameplay subsystems; a wide producer front → **two hubs** (`faction_state` in-13, `npc_behavior` in-12) → thin reader tier; a zero-Key trio; two retirement phantoms | the load is on the two hubs, and both are `[ASSUMPTION]` |
| **Directional** | `directional_coverage` | of 7 delivery directions, **2 live** (lateral + bottom-up Domain-Echo core), **2 annotation-debt** (the down-seams), **3 genuine** (diagonal zero-instances, uncalled resolvers, deferred decay) | direction is emergent → correctness = **authoring discipline** |
| **Three-axis** | `cross_scale_value_architecture` | objects (engine→module stack real only for combat; wrapper ≡ adapter); data (input-closed, output-leaky, location-dispersed); semantics (two regimes, quantize-throttle escalation, ~27 un-unified transformation rules) | the missing piece is **one value-transformation primitive** — which half-exists |
| **Gaps** | `gap_register` | two-tier `[CTC]` vs `[GENUINE]`: **~26 CTC · ~2–3 GENUINE · 1 deferral · 1 design-ruling · 5 no-action** | most "missing" architecture is unbuilt wiring on sound logic |

No thesis-level fracture: the annotation-debt-vs-genuine distinction is preserved consistently across all four
(gap register cat-D vs D-directional, directional, adversarial, synthesis §8). The three-axis cut is not a fifth
finding — it is the *mechanism-level explanation* of why the other three keep landing on "wiring, not mechanism."

---

## §2 · The three loci where all correctness concentrates

**Locus 1 — Authoring discipline (the transport layer).** Because direction is emergent, a value reaches its
cross-scale observer only if the emitter populates the addressing fields. Three fields, three states: `targets[]`
(sparse — the 8 §12.4 down-seams deliver *blind*), `causes[]` (empty — **zero** populated instances anywhere in
`sim/`, so the diagonal/provenance direction has never once run), `scale_signature` (type-populated, one instance
mislabel — the `scene_slate→piety_track` scale-enum artifact). This is not a mechanism gap; it is a discipline gap,
and it is where transport correctness lives.

**Locus 2 — The two integration hubs (the propagation layer).** `faction_state` (in-13) and `npc_behavior` (in-12)
are both L2 cut-vertices and both `[ASSUMPTION]`-grade resolvers. **The most value in the system flows through the
two least-certain resolutions.** Grounding these two — promoting their `deterministic_accounting` from
`[ASSUMPTION]` to verified-against-the-sim — is the single highest-leverage act in the entire docket, and it is CTC
(the contested-resolution path already has d+σ, ED-874; the accounting spine is specified).

**Locus 3 — One value-transformation primitive (the semantics layer).** The corpus runs **~27 distinct
value-transformation rules** across six saturation postures (saturating / weighted-mean / floor-mean / flat-sum /
threshold-count / homeostat) with **no shared aggregation contract** — plus two whole rungs that don't aggregate at
all (faction→national is *ruled* non-nested; the Territory tier is doctrine-only). The unifying primitive is **further
along than a blank slate**: it is *proposed as a schema* — the `Field`/`Gauge` primitive, `governance_type_registry_v1
§4.2` (`aggregate_fn`/`propagate_fn`/`decay_fn`) — and its saturation half is *already shipping one scale down* as the
σ-leverage kernel (`sim/autoload/sigma_leverage.py`: weighted-sum → `tanh` soft-cap → scale-invariant). It is blocked
on one Jordan ruling (OF-3's `decay()`) and the cross-tick convergence proof (the D.6 double-count).

---

## §3 · The genuine surface vs the complete-the-chain surface

The honest split — and the ratio *is* the headline:

**GENUINE (small — new mechanism or a ruling the surrounding logic doesn't determine):**
- **GAP-DIR-1** — author the *first* `causes[]` diagonal exemplar (the one clean genuine build; threadwork's §5.6
  Thread Echo is the natural seed).
- **GAP-A1** — `domain_actions`' strategic-turn home doc (leaning consolidation — the verbs exist fragmented across
  `params/bg/`, ED-FA-0002).
- **GAP-C4** — `env.crisis`' consumer (leaning CTC — `§2.6` points at `settlement_layer`).
- **Locus-3 work** — rule OF-3's `decay()` term, prove cross-tick convergence, and supply the collision primitive
  (GAP-E1/E2: the four un-unified radiation systems — MS distance-falloff, Calamity radiation, Turmoil↔Accord, Π
  homeostat).
- **GAP-G2** — a design ruling on whether `npc_behavior`'s non-scalar state is a registry quantity.

**COMPLETE-THE-CHAIN (large — the surrounding built logic determines the fix):**
ground the two `[ASSUMPTION]` hubs · wire the two built-but-uncalled resolvers (`compute_accord_echo`,
`propose_transfer`) · batch the 8 `!A6` `targets[]` annotations · key the zero-Key trio (`ci_political`,
`territorial_piety`; `victory` reads clocks directly) · register the pointer-debt · **flip `engine_clock`'s pointer**
(its home `propagation_spec_v1 §O.2` is canonical, only ED-1051 pends) · add a contract owner for the already-ticked
`MS` clock · retire `settlement_economy` + `campaign_architecture` · currency hygiene (the 4 unregistered heads, the
`combat_v30` drift, the vocab-debt in 3 concentrated docs, the CLAUDE.md §6 count refresh to 9/13). **~26 items.**

The ~10:1 CTC:GENUINE ratio is the intended shape — the architecture is mostly *sound logic awaiting wiring*.

---

## §4 · Epistemic status — how much to trust this, and why

**Leads, not verdicts.** The L0 gate FAILED 1/3 (P2: the 7 Convictions sit at throughline-degree 0 — structurally
isolated; a real corpus finding, GAP-H4). Findings are a prioritized lead-list; the authoritative per-module gate is
`valoria-module-adjudicator` (A1–A12), which wins any disagreement.

**Three confidence tiers — stated, not blurred:**
- **Machine-verified (hard):** the scorecard — 27 modules / 99 raw wiring edges / 2 L2 cycles / 9 `doc:null` / 13
  `[ASSUMPTION]` / 4 dangling / 0 phantom; G_code 173 / 268 / 3 cycles / 14 cut-vertices; pointer 52.7%; `faction_state`
  in-13 / `npc_behavior` in-12; validation FAILED 1/3. All re-checked against the committed JSON.
- **Hand-census (medium):** the `50/50/50`-across-`~49`-types field population and the `~27`-rule / six-posture
  transformation census — consolidated from `pressure_key_registry_v1.md` + registry grep, not an observatory metric;
  hedged accordingly.
- **Classifications (leads):** every CTC/GENUINE call — evidence-cited but downgraded by the failed gate.

**The confidence is earned, not asserted.** This docket was hardened through **five adversarial passes**: two gates on
the synthesis (a refute-by-default critic + a six-directional verifier), a four-agent pass on the three-axis doc (three
axis-skeptics + an intensifier), and two holistic skeptics on the whole PR. That process *found and fixed real errors* —
a load-bearing "collision of stresses" misattribution, a superseded-canon ΔLegitimacy citation, a fabricated `~60/40`,
two GENUINE→CTC reclassifications that hadn't propagated to sibling docs, and an infra-count miscount. The corrections
are logged in each doc's banner + `adversarial_review_v1.md`. What survived every pass — the scorecard, the transport
spot-checks, the Sufficient Scope order, the F1 guard, the two-hub finding, the convergence analysis — is what the
confidence rests on.

---

## §5 · The single prioritized action surface (ordered by leverage; all HELD-BACK)

1. **Ground the two `[ASSUMPTION]` hubs** (`faction_state`, `npc_behavior`) — CTC, highest leverage; every downstream
   value passes through them.
2. **Wire the two built-but-uncalled resolvers** — `compute_accord_echo` into `echo_transport`; `propose_transfer` off
   the `parliamentary_bridge` vote — CTC, the code already exists (un-deadens bottom-up Accord + top-down transfer).
3. **Batch the §12.4 `targets[]` annotation pass** (8 down-seams) — CTC, converts top-down/down-diagonal from
   annotation-debt to LIVE.
4. **Author the first `causes[]` diagonal exemplar** (threadwork §5.6) — the one clean GENUINE build; after one
   exemplar, further diagonals are CTC.
5. **Populate the `Field`/`Gauge` schema over the ~27 rules + rule OF-3's `decay()`** — the primitive; lift the shipped
   σ-leverage saturation kernel to the cross-scale grain; make Accord/Treasury instances rather than bespoke formulas.
6. **CTC cleanup sweep** — key the zero-Key trio; register pointer-debt; flip `engine_clock`'s pointer; add the `MS`
   contract owner; retire the two phantoms; currency hygiene.
7. **Close the deepest genuine work** — the cross-tick convergence proof (D.6) + the unified collision primitive
   (GAP-E1/E2).

---

## §6 · What this means for the videogame

Valoria's promise is that **personal-scale actions matter on the strategic layer**. The unification verdict: the
substrate *can* carry that promise — it is topology-neutral and delivers in all directions — and the pieces mostly
exist. But today only **two of seven directions are live end-to-end**; up-escalation is a deliberate **2-bit throttle**
(a scene moves a faction stat by at most ±2 of 7, once per scene — de-magnified to prevent scene-dominance); the live
bottom-up path fires at the **faction-aggregate** grain, not the **individual actor**; and the value-transformation
layer is un-unified with **no time-decay and no convergence proof**. So the "my character mattered strategically" beat
is *present but thin*, and the strategic layer can drift without entropy over a long campaign.

The path to the promise is not new mechanisms — it is the three loci: **author the addressing discipline** so events
reach their scales, **ground the two hubs** so the resolution is trustworthy, and **ship the one value-transformation
primitive** (proposed schema + shipped kernel + a `decay()` ruling) so cross-scale value aggregates, distributes,
weights, decays, and converges under one contract. Do those three, and Valoria's cross-scale design becomes a running
game rather than an elegant substrate awaiting its wiring.
